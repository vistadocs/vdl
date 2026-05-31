---
title: ROR*1.5*42 Technical Manual/Security Guide
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: null
app_code: ROR
app_name: 'Registry: Clinical Case (CCR)'
section: CLI
app_status: active
pkg_ns: ROR
patch_ver: 1.5
patch_id: ROR*1.5*42
group_key: ROR:ROR:1.5
file_numbers:
- '1'
- '1.07'
- '1.5'
- '1.6'
- '2'
- '3'
- '3.5'
- '4'
- '4.5'
- '5'
- '6'
- '6.5'
- '6.6'
- '8'
- '9'
- '11'
- '16'
- '19'
- '24'
- '28'
- '30'
- '31'
- '32'
- '33'
- '34'
- '40'
- '40.7'
- '40.8'
- '41'
- '42'
- '42.4'
- '43'
- '44'
- '45'
- '45.84'
- '50'
- '50.605'
- '50.607'
- '52.2'
- '54'
- '55'
- '60'
- '63'
- '63.05'
- '71'
- '79'
- '80'
- '81'
- '120.8'
- '161.8'
- '162'
- '162.02'
- '162.03'
- '162.1'
- '162.11'
- '162.4'
- '162.5'
- '162.6'
- '200'
- '691.5'
- '798'
- '798.01'
- '798.02'
- '798.1'
- '798.12'
- '798.128'
- '798.2'
- '798.3'
- '798.31'
- '798.32'
- '798.4'
- '798.5'
- '798.6'
- '798.7'
- '798.73'
- '798.8'
- '798.87'
- '798.9'
- '799.1'
- '799.2'
- '799.34'
- '799.4'
- '799.41'
- '799.51'
- '799.53'
- '799.6'
- '799.61'
- '799.641'
- '900001'
security_keys:
- ADMIN
- HEPC ADMIN
- HEPC USER
- IRM
- PROVIDER
- ROR VA IRM
- USER
- VA GENERIC ADMIN
- VA GENERIC USER
menu_options: 53
description: The Clinical Case Registries (CCR)) software application collects data on the population of veterans with certain clinical conditions, namely Hepatitis C and Human Immunodeficiency Virus (HIV) infections.
audience: Technical staff, IRM, system administrators
keywords: []
page_count: 0
word_count: 53512
section_count: 37
table_count: 384
figure_count: 0
appendix_count: 2
has_toc: false
is_stub: false
pub_date: null
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Reg-Clinical_Case_Registries/ror1_5_42tm.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Reg-Clinical_Case_Registries/ror1_5_42tm.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=126
audit_applied: '2026-05-31'
master_source: ROR*1.5*42 Technical Manual/Security Guide
master_pub_date: 'null'
consolidated_from: 2 versions
prior_versions:
- ROR*1.5*41 Technical Manual/Security Guide
consolidated_title: technical manual/security guide
---

> Clinical Case Registries (CCR)

*Version 1.5*

![](ror-1-5-42-technical-manual-security-guide/001.png)

Technical Manual / Security Guide

*Documentation Revised June 2024For Patch ROR\*1.5\*42*THIS PAGE INTENTIONALLY LEFT BLANK

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [List of Tables](#list-of-tables)
- [List of Figures](#list-of-figures)
- [Preface](#preface)
  - [Typographical Conventions Used in the Manual](#typographical-conventions-used-in-the-manual)
  - [Navigating Hyperlinks](#navigating-hyperlinks)
  - [Screen Displays and Text Notes](#screen-displays-and-text-notes)
  - [Clinical Case Registries Software Application](#clinical-case-registries-software-application)
  - [Purpose of the Manual](#purpose-of-the-manual)
  - [Recommended Users](#recommended-users)
  - [Related Documents](#related-documents)
- [Introduction](#introduction)
  - [Overview](#overview)
  - [Software Features and Functions](#software-features-and-functions)
  - [About Clinical Case Registries 1.5](#about-clinical-case-registries-15)
    - [Decommissioned Software](#decommissioned-software)
    - [CCR Patches ROR\1.5\X](#ccr-patches-ror15x)
  - [Obtaining Software and Documentation](#obtaining-software-and-documentation)
  - [VistA Documentation on the Intranet](#vista-documentation-on-the-intranet)
  - [Accessibility Features in Clinical Case Registries 1.5](#accessibility-features-in-clinical-case-registries-15)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Implementation](#implementation)
  - [Maintenance](#maintenance)
    - [Re-index the ACL cross-reference](#re-index-the-acl-cross-reference)
    - [Edit Lab Search Criteria](#edit-lab-search-criteria)
    - [Edit Registry Parameters](#edit-registry-parameters)
    - [Historical Data Extraction](#historical-data-extraction)
    - [Print Log Files](#print-log-files)
    - [Pending Patients](#pending-patients)
  - [Manual Historical Data Extraction](#manual-historical-data-extraction)
    - [Overview](#overview-1)
    - [Historical Data Extraction Menu](#historical-data-extraction-menu)
    - [Data Extraction Instructions](#data-extraction-instructions)
    - [Data Transmission Instructions](#data-transmission-instructions)
- [CCR Structure and Process Overview](#ccr-structure-and-process-overview)
- [CCR Files](#ccr-files)
  - [Files and Globals List](#files-and-globals-list)
  - [File Diagrams (Pointers)](#file-diagrams-pointers)
- [Globals](#globals)
  - [Upgrade Installation](#upgrade-installation)
  - [Initial Installation](#initial-installation)
  - [Temporary Globals](#temporary-globals)
- [Routines](#routines)
  - [Routine List for CCR 1.5](#routine-list-for-ccr-15)
  - [Routine Sub-Namespaces](#routine-sub-namespaces)
  - [XINDEX](#xindex)
- [Exported Options](#exported-options)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
- [Protocols](#protocols)
  - [HL7 Protocols](#hl7-protocols)
  - [Event Protocols](#event-protocols)
- [Application Program Interfaces](#application-program-interfaces)
- [External Interfaces](#external-interfaces)
- [External Relations](#external-relations)
  - [Required Patches](#required-patches)
  - [Database Integration Agreements (DBIAs)](#database-integration-agreements-dbias)
- [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [Registry Selection Rules](#registry-selection-rules)
- [Software Product Security](#software-product-security)
  - [Alerts](#alerts)
  - [Remote Systems](#remote-systems)
  - [Contingency Planning](#contingency-planning)
  - [Interfacing](#interfacing)
  - [Electronic Signatures](#electronic-signatures)
  - [Security Keys](#security-keys)
- [<span id="AppB" class="anchor"></span>Using the Windows FTP Client](#span-idappb-classanchorspanusing-the-windows-ftp-client)
- [HL7 Message Definitions](#hl7-message-definitions)
- [Index](#index)
| Date            | Description                                                                                | Author / Role                                                |
|-----------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| June, 2024      | Final release for Patch ROR\*1.5\*42. See [Table 39](#patch-ror1.542) for Details.         | See CCR Redacted document for the list of authors and roles. |
| April, 2023     | Final release for Patch ROR\*1.5\*41. See [Table 38](#patch-ror1.541) for Details.         | See CCR Redacted document for the list of authors and roles. |
| November, 2022  | Final release for Patch ROR\*1.5\*40. See [Table 37](#patch-ror1.540) for Details.         | See CCR Redacted document for the list of authors and roles. |
| January, 2022   | Final release for Patch ROR\*1.5\*39. See [Table 36](#patch-ror1.539) for Details.         | See CCR Redacted document for the list of authors and roles. |
| June, 2021      | Final release for Patch ROR\*1.5\*38. See [Table 35](#patch-ror1.538) for Details.         | See CCR Redacted document for the list of authors and roles. |
| November, 2020  | Final release for Patch ROR\*1.5\*37. See [Table 34](#patch-ror1.537) for Details.         | See CCR Redacted document for the list of authors and roles. |
| May, 2020       | Final release for Patch ROR\*1.5\*36. See [Table 33](#patch-ror1.536) for Details.         | See CCR Redacted document for the list of authors and roles. |
| November, 2019  | Final release for Patch ROR\*1.5\*35. See [Table 32](#patch-ror1.535) for Details.         | See CCR Redacted document for the list of authors and roles. |
| March, 2019     | Final release for Patch ROR\*1.5\*34. See Table 31 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| July, 2018      | Final release for Patch ROR\*1.5\*33. See Table 30 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| April, 2018     | Final release for Patch ROR\*1.5\*32. See Table 29 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| November, 2017  | Final release for Patch ROR\*1.5\*31. See Table 28 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| May, 2017       | Final release for Patch ROR\*1.5\*30. See Table 28 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| June, 2015      | Final release for Patch ROR\*1.5\*29. See Table 26 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| May, 2016       | Final release for Patch ROR\*1.5\*28. See Table 25 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| June, 2015      | Final release for Patch ROR\*1.5\*26. See Table 24 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| June, 2015      | Final release for Patch ROR\*1.5\*25. See Table 23 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| April, 2015     | Final release for Patch ROR\*1.5\*27. See Table 22 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| October, 2014   | Final release for Patch ROR\*1.5\*24. See Table 21 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| August, 2014    | Final release for Patch ROR\*1.5\*22. See Table 20 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| April, 2014     | Final release for Patch ROR\*1.5\*21. See Table 19 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| March, 2013     | Final release for Patch ROR\*1.5\*20. See Table 18 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| August, 2014    | Final release for Patch ROR\*1.5\*19 to incorporate ICD10 codes. See Table 17 for Details. | See CCR Redacted document for the list of authors and roles. |
| August, 2012    | Final release for Patch ROR\*1.5\*18. See Table 16 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| April, 2012     | Final release for Patch ROR\*1.5\*17. See Table 15 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| September, 2011 | Final release for Patch ROR\*1.5\*15. See Table 14 for Details.                            | See CCR Redacted document for the list of authors and roles. |
| March 2011      | Patch ROR\*1.5\*14. See Table 13 for details.                                              | See CCR Redacted document for the list of authors and roles. |
| December, 2010  | Final release for Patch ROR\*1.5\*13. See Table 12 for details.                            | See CCR Redacted document for the list of authors and roles. |
| April, 2010     | Final release for Patch ROR\*1.5\*10: See Table 11 for details.                            | See CCR Redacted document for the list of authors and roles. |
| (unknown)       | Patch ROR\*1.5\*9 was a maintenance bug fix, and is not documented in this manual.         | See CCR Redacted document for the list of authors and roles. |
| July, 2009      | Technical Writer/SQA review and matchup with CCR User Manual for Patch ROR\*1.5\*8         | See CCR Redacted document for the list of authors and roles. |
| July, 2008      | Patch ROR\*1.5\*7: See Table 9 for details.                                                | See CCR Redacted document for the list of authors and roles. |
| May, 2008       | Patch ROR\*1.5\*6: See Table 8 for details.                                                | See CCR Redacted document for the list of authors and roles. |
| March, 2008     | Patch ROR\*1.5\*5: See Table 7 for details.                                                | See CCR Redacted document for the list of authors and roles. |
| December, 2007  | Patch ROR\*1.5\*4: See Table 6 for details.                                                | See CCR Redacted document for the list of authors and roles. |
| November, 2007  | Patch ROR\*1.5\*3: See Table 5 for details.                                                | See CCR Redacted document for the list of authors and roles. |
| October, 2007   | Patch ROR\*1.5\*2: See Table 4 for details.                                                | See CCR Redacted document for the list of authors and roles. |
| October 2006    | Patch ROR\*1.5\*1: See Table 3 for details.                                                | See CCR Redacted document for the list of authors and roles. |
| February, 2006  | Completely updated for version 1.5                                                         | See CCR Redacted document for the list of authors and roles. |
| June, 2002      | Initial release of CCR Version 1.0                                                         | See CCR Redacted document for the list of authors and roles. |
<span id="_Ref233443442" class="anchor"></span>Table 1 – Typographical Conventions
Table of Contents

# List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Typographical Conventions Used in the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fonts and other conventions shown in Table 1 are used throughout this document. Conventions for the use of graphic icons and other symbols are shown in Table 2.

<table>
<caption><p><span id="_Ref233443489" class="anchor"></span>Table 2 – Graphical Conventions</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 33%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Font</strong></th>
<th><strong>Used for…</strong></th>
<th><strong>Examples:</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Blue text, underlined</td>
<td>Hyperlink to another document or URL</td>
<td><a href="xxx.xxx.xxx.xxx">xxx.xxx.xxx.xxx</a></td>
</tr>
<tr class="even">
<td>Green text, dashed underlining</td>
<td>Hyperlink to a place in this document</td>
<td>"CCR accesses several other <a href="#Glos_VistA">Veterans Health Information Systems and Technology Architecture</a> (VistA) files…"</td>
</tr>
<tr class="odd">
<td rowspan="4">Courier New</td>
<td>Patch names</td>
<td>ROR*1.5*2, XYZ file #798.1</td>
</tr>
<tr class="even">
<td>VistA menu options</td>
<td>ACL – Re-index the ACL cross-reference</td>
</tr>
<tr class="odd">
<td>VistA filenames</td>
<td>Xxx</td>
</tr>
<tr class="even">
<td>VistA field names</td>
<td>Xxx</td>
</tr>
<tr class="odd">
<td>Franklin Gothic Demi</td>
<td>Keyboard keys</td>
<td>&lt; F1 &gt;, &lt; Alt &gt;, &lt; L &gt;, [Enter]</td>
</tr>
<tr class="even">
<td rowspan="5">Microsoft Sans Serif</td>
<td>Software Application names</td>
<td>Clinical Case Registries (CCR)</td>
</tr>
<tr class="odd">
<td>Registry names</td>
<td>CCR:HIV</td>
</tr>
<tr class="even">
<td>GUI database field names</td>
<td>Comment field</td>
</tr>
<tr class="odd">
<td>GUI report names</td>
<td>Procedures report</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Microsoft Sans Serif bold</td>
<td>GUI panel, pane, tab, button and command icon names</td>
<td><p><strong>Other Registries</strong> panel</p>
<p><strong>[Delete]</strong> button</p></td>
</tr>
<tr class="even">
<td>Times New Roman</td>
<td>Normal text</td>
<td>"… designed for use by designated Registry Coordinators, Managers, and Clinicians…."</td>
</tr>
<tr class="odd">
<td rowspan="3">Times New Roman Italic</td>
<td>Text emphasis</td>
<td>"It is <em>very</em> important…"</td>
</tr>
<tr class="even">
<td>National and International Standard names</td>
<td><em>International Statistical Classification of Diseases and Related Health Problems</em></td>
</tr>
<tr class="odd">
<td>Document names</td>
<td><em>Clinical Case Registries</em> <em>User Manual</em></td>
</tr>
</tbody>
</table>

<span id="_Ref233443489" class="anchor"></span>Table 2 – Graphical Conventions

| Graphic                                                                                                                                                                         | Used for…                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](ror-1-5-42-technical-manual-security-guide/002.png)                               | Information of particular interest regarding the current subject matter                |
| ![](ror-1-5-42-technical-manual-security-guide/003.png)                                               | A tip or additional information that may be helpful to the user                        |
| ![](ror-1-5-42-technical-manual-security-guide/004.png) | A warning concerning the current subject matter                                        |
| ![](ror-1-5-42-technical-manual-security-guide/005.png)                  | Information about the history of a function or operation; provided for reference only. |

<span id="_Toc165646458" class="anchor"></span>Table 3 – Patch ROR\*1.5\*2 Description

## Navigating Hyperlinks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, you will find hyperlinks of various types like those indicated in Table 1, above. Some will be to other places in this document, while others will take you to websites or other documents stored online. If the hyperlink is to another place in this document, use the web toolbar "back" button (![](ror-1-5-42-technical-manual-security-guide/006.png) ) to return to the point in the document where you clicked the link. If the link is external and takes you to a website, use the back button in your browser to return.

If you do not see the back button in the program you are using to read this document, use your program's View menu to turn on the Web toolbar. For example, in Microsoft® Word® 2003, first click <u>V</u>iew, then <u>T</u>oolbars; make sure the Web toolbar is selected.

## Screen Displays and Text Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this manual, the VistA user's response is shown in bold type, but it does not appear on the screen as bold. The bold part of the entry is the letter, or letters, that you must type so that the computer can identify the response. In most cases, you only have to enter the first few letters. This increases speed and accuracy.

Every response you type must be followed by pressing the \[Return\] key (or \[Enter\] for some keyboards). In VistA screen shots, whenever the Return or Enter key should be pressed, you will see the symbol \<RET\>. This symbol is not shown but is implied if there is bold input.

Within the "roll'n'scroll" part of the system, Help frames may be accessed from most prompts by entering one, two, or three question marks (?, ??, or ???).

Within the examples of actual terminal dialogues, additional information about the dialogue may be shown. This information is enclosed in brackets, for example, *{type ward name here},* and it does not appear on the screen.

## Clinical Case Registries Software Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Case Registries (CCR) software application supports the maintenance of local and national registries for clinical and resource tracking of care for patients with certain clinical conditions. National registries for [Hepatitis C](#Glos_HepatitisC) (CCR:HEPC) and [Human Immunodeficiency Virus](#Glos_HIV) (CCR:HIV) are available. Sixteen local registries were added in ROR\*1.5\*18, an additional local registry in ROR\*1.5\*21, eight additional local registries in ROR\*1.5\*24, two additional local registries in ROR\*1.5\*26, five additional local registries in ROR\*1.5\*28, two additional local registries in ROR\*1.5\*30, two additional local registries in ROR\*1.5\*31, two additional local registries in ROR\*1.5\*32, six additional local registries in ROR\*1.5\*33, three additional local registries in ROR\*1.5\*34, two additional local registries in ROR\*1.5\*35, one additional local registry in ROR\*1.5\*36, and one additional local registry in ROR\*1.5\*37. Data in local registries are not transmitted to the national database. This application allows access to important demographic and clinical data on all VHA patients with these conditions, and provides many capabilities to VA facilities that provide care and treatment to patients with these conditions, including clinical categorization of patients and automatic transmission of data in the two national registries to the VA's [National Case Registry](#Glos_NCR) It also provides clinical and administrative reports for local medical center use.

CCR accesses several other [Veterans Health Information Systems and Technology Architecture](#Glos_VistA) (VistA) files that contain information regarding other diagnoses, prescriptions, surgical procedures, laboratory tests, radiology exams, patient demographics, hospital admissions, and clinical visits. This access allows identified clinical staff to take advantage of the wealth of data supported through VistA.

## Purpose of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Clinical Case RegistriesUser Manual* provides detailed instructions for using the CCR software and its [graphical user interface](#Glos_GUI) (GUI). This document, the *CCR Technical Manual / Security Guide*, provides more technical information about the CCR application.

Throughout this document, the acronym CCR always refers to the application and its features, not to the individual registries. The HIV and Hepatitis C registries are referred to as CCR:HIV and CCR:HEPC respectively.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Information Resource Management (IRM) staff is required for installation and support of the CCR v1.5.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These related documents are available at <http://www.va.gov/vdl/application.asp?appid=126>.

- *Clinical Case Registries 1.5 Installation & Implementation Guide*
- *Clinical Case Registries 1.5 Release Notes*
- *Clinical Case Registries 1.5 User Manual*

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Case Registries (CCR)) software application collects data on the population of veterans with certain clinical conditions, namely [Hepatitis C](#Glos_HepatitisC) and [Human Immunodeficiency Virus](#Glos_HIV) (HIV) infections.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Case Registries (CCR) software uses pre-defined selection rules that identify patients with a disease-related [ICD-9](#Glos_ICD9) or [ICD-10](#Glos_ICD10) code or a positive result on a laboratory test and adds them to the registry. Patients added to local registries are automatically confirmed. Starting with Patch ROR\*1.5\*35, the national registries will automatically confirm patients as well. At the time of the patch installation, any pending patients will be confirmed setting the confirmation date to the patch installation date and any pending comments for those patients will be deleted.

A nightly background process transmits a set of predefined data via [HL7](#Glos_HL7) to the national CCR database at [Corporate Data Center Operations](#Glos_CDCO) (CDCO).[^1] Data from the national registries is aggregated in the same message. The CCR software creates a limited set of database elements to be stored locally in the VistA system, and focuses on assuring that the local listing is complete and accurate, that the desired data elements are extracted, and that data elements are appropriately transmitted to the national database.

| ![](ror-1-5-42-technical-manual-security-guide/007.png) | Note: Effective with Patch ROR\*1.5\*14, the extract code pulls Purchased Care Data. New ZIN/ZSV/ZRX segments were added to the HL7 message for this purpose (see updated tables starting on page [186](#TOC)). This change is transparent and seamless to users; no changes in process or method were made. |     |
|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|

<span id="_Toc165646459" class="anchor"></span>Table 4 – Patch ROR\*1.5\*2 Description

| ![](ror-1-5-42-technical-manual-security-guide/008.png) | Note: Effective with Patch ROR\*1.5\*18, if the user who performed the nightly task is not a valid user, CCR will abort with an access violation. If this error occurs, double-check the user permissions. The task needs to be rescheduled by an active user with the ROR VA IRM key. |     |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|

<span id="_Toc165646460" class="anchor"></span>Table 5 – Patch ROR\*1.5\*3 Description

| ![](ror-1-5-42-technical-manual-security-guide/009.png) | Note: Effective with Patch ROR\*1.5\*20, the Clinical Case Registries (CCR) application was brought into 508 compliance in many areas.                                |     |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| ![](ror-1-5-42-technical-manual-security-guide/010.png) | Note: Effective with Patch ROR\*1.5\*26, the Clinical Case Registries (CCR) application was brought into the Delphi XE5 development environment, with GUI conversion. |     |
| ![](ror-1-5-42-technical-manual-security-guide/011.png) | Note: Effective with Patch ROR\*1.5\*28, the Clinical Case Registries (CCR) application was brought into the Delphi XE8 development environment, with GUI conversion. |     |

<span id="_Toc165646461" class="anchor"></span>Table 6 – Patch ROR\*1.5\*4 Description

If there is more new data than is allowed by the registry parameter for a single CCR HL7 batch message (currently, five megabytes), the software will send several messages during a single night.

Data from the registries is used for both clinical and administrative reporting on both a local and national level. Each facility can produce local reports (information related to patients seen in their system). Reports from the national database are used to monitor clinical and administrative trends, including issues related to patient safety, quality of care and disease evolution across the national population of patients.

## Software Features and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCR provides these key features:

- Easy data access and navigation of the data files via the GUI.
- Semi-automatic sign-on to the VistA databases via the web-based GUI; a separate VistA log-in is not required, nor is emulation software such as !KEA or Attachmate Reflection.
- Automated development of local lists of patients with evidence of HIV or Hepatitis C infection.
- Automatic transmission of patient data from the local registry lists to a national database.
- Robust reporting capabilities.

CCR also provides the following functions:

- Tracking of patient outcomes relating to treatment.
- Identification and tracking of important trends in treatment response, adverse events, and time on therapy.
- Monitoring quality of care using both process and patient outcome measures.

## About Clinical Case Registries 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Version 1.5 of the CCR software (published via Patch ROR\*1.5\*1) introduced a single software package to support both the CCR:HEPC Registry and the CCR:HIV Registry (also called the Immunology Case Registry (ICR)). CCR provides access to both CCR:HIV and CCR:HEPC from a single interface; previously, these two registries were created and maintained through two separate software packages. Since the functional requirements for these registries were substantially the same, they were combined.

CCR 1.5 has also been enhanced by automation of the data collection system and transformed from an administrative database into a clinically relevant tool for patient management.

Each patch released since the original iteration of CCR 1.5 has added improvements and fixes; see CCR Patches ROR\*1.5\*X for details.

### Decommissioned Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Immunology Case Registry v2.1

Patients from ICR version 2.1 were migrated to CCR:HIV during the installation of patch ROR\*1\*5 (March 2004). After a transitional period when the two packages were used concurrently, ICR 2.1 was removed from service by patch IMR\*2.1\*21 (October 2005).

#### Hepatitis C Case Registry v1.0

Hepatitis C Case Registry (HCCR) v1.0 was removed from service with the release of CCR 1.5. Historical patient data from the previous Hepatitis C Registry was migrated to CCR:HEPC.

### CCR Patches ROR\*1.5\*X

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes provided by patches in the ROR\*1.5 series are shown in the following tables. Under "Type," "E" indicates an enhancement, "F" indicates a fix, and "M" denotes a modification (as to data). To jump to a particular patch, click (or \<Ctrl\>+\<Click\>) a green link below.

| [Patch ROR\*1.5\*1](#P01)                                      | [Patch ROR\*1.5\*2](#P02)                                      | [Patch ROR\*1.5\*3](#P03)             |                                       | [Patch ROR\*1.5\*4](#P04)             | [Patch ROR\*1.5\*5](#P05)             | [Patch ROR\*1.5\*6](#P06)             | [Patch ROR\*1.5\*7](#P07)             |
|----------------------------------------------------------------|----------------------------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
| [Patch ROR\*1.5\*8](#P08)                                      | (Patch ROR\*1.5\*9: maintenance patch; not documented herein)  |                                       |                                       | [Patch ROR\*1.5\*10](#patch-ror1.510) | [Patch ROR\*1.5\*13](#patch-ror1.513) | [Patch ROR\*1.5\*14](#patch-ror1.514) | [Patch ROR\*1.5\*15](#patch-ror1.515) |
| (Patch ROR\*1.5\*16: maintenance patch; not documented herein) |                                                                | [Patch ROR\*1.5\*17](#patch-ror1.517) |                                       | [Patch ROR\*1.5\*18](#patch-ror1.518) | [Patch ROR\*1.5\*19](#patch-ror1.519) | [Patch ROR\*1.5\*20](#patch-ror1.520) | [Patch ROR\*1.5\*21](#patch-ror1.521) |
| [Patch ROR\*1.5\*22](#patch-ror1.522)                          | (Patch ROR\*1.5\*23: maintenance patch; not documented herein) |                                       |                                       | [Patch ROR\*1.5\*24](#patch-ror1.524) | [Patch ROR\*1.5\*27](#patch-ror1.527) | [Patch ROR\*1.5\*25](#patch-ror1.525) | [Patch ROR\*1.5\*26](#patch-ror1.526) |
| [Patch ROR\*1.5\*28](#patch-ror1.528)                          | [Patch ROR\*1.5\*29](#patch-ror1.529)                          |                                       | [Patch ROR\*1.5\*30](#patch-ror1.530) | [Patch ROR\*1.5\*31](#patch-ror1.531) | [Patch ROR\*1.5\*32](#patch-ror1.532) | [Patch ROR\*1.5\*33](#patch-ror1.533) | [Patch ROR\*1.5\*34](#patch-ror1.534) |
| [Patch ROR\*1.5\*35](#patch-ror1.535)                          | [Patch ROR\*1.5\*36](#patch-ror1.536)                          |                                       | [Patch ROR\*1.5\*37](#patch-ror1.537) | [Patch ROR\*1.5\*38](#patch-ror1.538) | [Patch ROR\*1.5\*39](#patch-ror1.539) | [Patch ROR\*1.5\*40](#patch-ror1.540) | [Patch ROR\*1.5\*41](#patch-ror1.541) |
| [Patch ROR\*1.5\*42](#patch-ror1.542)                          |                                                                |                                       |                                       |                                       |                                       |                                       |                                       |

<span id="_Toc165646462" class="anchor"></span>Table 7 – Patch ROR\*1.5\*5 Description

#### Patch ROR\*1.5\*1

| Patch Number                                     | \#  | Description                                                                                                                                                                                                                            | Type |
|--------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| <span id="P01" class="anchor"></span>ROR\*1.5\*1 | 1   | Selected (Date) and Selection Rule columns added to the patient list on the Registry tab.                                                                                                                                              | E    |
|                                                  | 2   | When a report is opened, the Task Manager tab is activated.                                                                                                                                                                            | E    |
|                                                  | 3   | The Mode field is added to the Local Fields and Other Registries panels of the Report parameters to provide patient include and exclude filters.                                                                                       | E    |
|                                                  | 4   | A Delete button is added to the Patient Data Editor dialog box.                                                                                                                                                                        | E    |
|                                                  | 5   | A Patients panel is added to the Procedures report to use selected procedures performed and selected procedures not performed within a date range.                                                                                     | E    |
|                                                  | 6   | A Procedures panel is added to the Procedures report to indicate whether a procedure is an inpatient or outpatient one                                                                                                                 | E    |
|                                                  | 7   | The ICD-9 panel of the Diagnoses report is modified to be able to define groups and add ICD-9 codes to the groups.                                                                                                                     | E    |
|                                                  | 8   | The "Check if patient ever had an AIDS-OI" checkbox is automatically selected and the "Date of AIDS-OI" field is populated if an indicator disease Def box is selected in Section VIII of the CDC form in the Clinical Status section. | E    |
|                                                  | 9   | A new patient search parameter is added for the Registry tab: \# followed by the patient's 11-digit coded SSN.                                                                                                                         | E    |
|                                                  | 10  | The output format of the Combined Meds and Labs report is modified.                                                                                                                                                                    | E    |
|                                                  | 11  | The Patient Medication History report is modified with the addition of two radio buttons, Consider All and Selected Only to the Select Patient panel.                                                                                  | E    |
|                                                  | 12  | Fixed Microsoft® Windows Server 2003® issue.                                                                                                                                                                                           | F    |
|                                                  | 13  | Fixed missing CDC bitmap error.                                                                                                                                                                                                        | F    |
|                                                  | 14  | Fixed incorrect printing of the CDC form.                                                                                                                                                                                              | F    |

<span id="_Toc165646463" class="anchor"></span>Table 8 – Patch ROR\*1.5\*6 Description

#### Patch ROR\*1.5\*2

| Patch Number                                     | \#  | Description                                                                              | Type |
|--------------------------------------------------|-----|------------------------------------------------------------------------------------------|------|
| <span id="P02" class="anchor"></span>ROR\*1.5\*2 | 1   | Fixed RPC Broker timeout issue.                                                          | F    |
|                                                  | 2   | Fixed issues with duplicates in patient list.                                            | F    |
|                                                  | 3   | Fixed issues with lower-case characters in lab tests and medications data.               | F    |
|                                                  | 4   | Fixed issue with Reporting date entry not accepting "-T."                                | F    |
|                                                  | 5   | Fixed issue with un-checking of local fields in the Patient Data Editor not being saved. | F    |
|                                                  | 6   | Fixed issues with run-time errors using \$QUERY on non-Caché platforms.                  | F    |
|                                                  | 7   | Fixed issues with non-SSN patient identifier appearing on reports at non-VA sites.       | F    |

<span id="_Toc165646464" class="anchor"></span>Table 9 – Patch ROR\*1.5\*7 Description

#### Patch ROR\*1.5\*3

| Patch Number                                     | \#  | Description                                                                               | Type |
|--------------------------------------------------|-----|-------------------------------------------------------------------------------------------|------|
| <span id="P03" class="anchor"></span>ROR\*1.5\*3 | 1   | Accommodated Patch RA\*5\*75 (Radiology), which introduced a Reason for Study data field. | E    |
|                                                  | 2   | Addition of Task Control flag ("M") which signals the system to disable HL7 messaging.    | E    |

<span id="_Toc165646465" class="anchor"></span>Table 10 – Patch ROR\*1.5\*8 Description

#### Patch ROR\*1.5\*4

| Patch Number                                     | \#  | Description                                                                                      | Type |
|--------------------------------------------------|-----|--------------------------------------------------------------------------------------------------|------|
| <span id="P04" class="anchor"></span>ROR\*1.5\*4 | 1   | Added two additional ICD-9 codes needed for the nightly ROR registry update and data extraction. | E    |

<span id="_Ref257981135" class="anchor"></span>Table 11 – Patch ROR\*1.5\*10 Description

#### Patch ROR\*1.5\*5

| Patch Number                                     | \#  | Description                                                                          | Type |
|--------------------------------------------------|-----|--------------------------------------------------------------------------------------|------|
| <span id="P05" class="anchor"></span>ROR\*1.5\*5 | 1   | Fixed issue with Procedures without a Provider not being sent to AAC.                | F    |
|                                                  | 2   | Added drug identified as needed for nightly ROR registry update and data extraction. | E    |

<span id="_Toc165646467" class="anchor"></span>Table 12 – Patch ROR\*1.5\*13 Description

#### Patch ROR\*1.5\*6

| Patch Number                                     | \#  | Description                                               | Type |
|--------------------------------------------------|-----|-----------------------------------------------------------|------|
| <span id="P06" class="anchor"></span>ROR\*1.5\*6 | 1   | Added generic drug RALTEGRAVIR to VA GENERIC file \#50.6. | E    |

<span id="_Toc165646468" class="anchor"></span>Table 13 – Patch ROR\*1.5\*14 Description

#### Patch ROR\*1.5\*7

| Patch Number                                     | \#  | Description                                              | Type |
|--------------------------------------------------|-----|----------------------------------------------------------|------|
| <span id="P07" class="anchor"></span>ROR\*1.5\*7 | 1   | Added generic drug ETRAVIRINE to VA GENERIC file \#50.6. | E    |

<span id="_Ref302645128" class="anchor"></span>Table 14 – Patch ROR\*1.5\*15 Description

#### Patch ROR\*1.5\*8

| Patch Number                                     | \#  | Description                                                                                                                                                                                                                                                                                                  | Type |
|--------------------------------------------------|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| <span id="P08" class="anchor"></span>ROR\*1.5\*8 | 1   | Fixes the "access violation" seen when selecting Diagnoses Report (Remedy Tickets HD0000000262208 and HD0000000262209).                                                                                                                                                                                      | F    |
|                                                  | 2   | Inserts a Comment Field in the Pending Patient File necessary for tracking special conditions for a patient (see *CCR User Manual*, Pending Comment).                                                                                                                                                        | E    |
|                                                  | 3   | Adds the Comments panel to the Patient Data Editor screen (see 2 above).                                                                                                                                                                                                                                     | E    |
|                                                  | 4   | Adds the Comment field to Processing Pending Patient screen (see 2 above).                                                                                                                                                                                                                                   | E    |
|                                                  | 5   | Refreshes the Processing Pending Patient screen when comment is added or deleted (see 2 above).                                                                                                                                                                                                              | E    |
|                                                  | 6   | Adds radio buttons "Include," "Exclude," or "Ignore" to provide a filter limiting reports to patients who have diagnoses based on International Classification of Diseases, 9th edition (ICD-9) codes in Common Templates or Your Templates. This filter applies to all reports except the Diagnoses Report. | E    |
|                                                  | 7   | Modifies the Combined Meds and Labs report to require the user to assign a group name.                                                                                                                                                                                                                       | E    |
|                                                  | 8   | Modifies the Combined Meds and Labs report to provide the option to limit lab results to most recent.                                                                                                                                                                                                        | F    |
|                                                  | 9   | Modifies the Combined Meds and Labs report to "Include All" or "Selected Only" for lab results (Remedy Ticket HD0000000232223).                                                                                                                                                                              | E    |
|                                                  | 10  | Modifies the Combined Meds and Labs report, Pharmacy Prescription Utilization report, and the Patient Medication History report to include a new method of handling Investigational Drugs and Registry Medications on the Medications panel drop-down list.                                              | E    |
|                                                  |     |                                                                                                                                                                                                                                                                                                              |      |

<span id="_Ref320866525" class="anchor"></span>Table 15 – Patch ROR\*1.5\*17 Description

#### Patch ROR\*1.5\*10 

<table>
<caption><p><span id="_Ref331664104" class="anchor"></span>Table 16 – Patch ROR*1.5*18 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 30%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="5">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="6">1</td>
<td colspan="5">Adds new ICD-9 diagnosis groups to the Common Templates:</td>
<td rowspan="6">M</td>
</tr>
<tr class="even">
<td colspan="3">HCC</td>
<td>155.0</td>
<td>MAL NEO LIVER, PRIMARY</td>
</tr>
<tr class="odd">
<td colspan="3" rowspan="4">Esophageal Varices</td>
<td>456.0</td>
<td>ESOPHAG VARICES W BLEED</td>
</tr>
<tr class="even">
<td>456.1</td>
<td>ESOPH VARICES W/O BLEED</td>
</tr>
<tr class="odd">
<td>456.20</td>
<td>BLEED ESOPH VAR OTH DIS</td>
</tr>
<tr class="even">
<td>456.21</td>
<td>ESOPH VARICE OTH DIS NOS</td>
</tr>
<tr class="odd">
<td rowspan="16">2a</td>
<td colspan="5">Adds LOINC codes to CCR:HIV Patient ID:</td>
<td rowspan="16">M</td>
</tr>
<tr class="even">
<td><strong>LOINC_NUM</strong></td>
<td><strong>SHORTNAME</strong></td>
<td colspan="3"><strong>LONG_COMMON_NAME</strong></td>
</tr>
<tr class="odd">
<td>34591-8</td>
<td>HIV1 Ab Fld Ql EIA</td>
<td colspan="3">HIV 1 Ab [Presence] in Body fluid by Immunoassay</td>
</tr>
<tr class="even">
<td>34592-6</td>
<td>HIV1 Ab Fld Ql IB</td>
<td colspan="3">HIV 1 Ab [Presence] in Body fluid by Immunoblot (IB)</td>
</tr>
<tr class="odd">
<td>43009-0</td>
<td>HIV1+2 IgG Ser Ql</td>
<td colspan="3">HIV 1+2 IgG Ab [Presence] in Serum</td>
</tr>
<tr class="even">
<td>43010-8</td>
<td>HIV1+2 Ab XXX Ql</td>
<td colspan="3">HIV 1+2 Ab [Presence] in Unspecified specimen</td>
</tr>
<tr class="odd">
<td>43185-8</td>
<td>HIV 1 &amp; 2 Ab Patrn Ser IB-Imp</td>
<td colspan="3">HIV 1 &amp; 2 Ab band pattern [interpretation] in Serum by Immunoblot (IB)</td>
</tr>
<tr class="even">
<td>43599-0</td>
<td>HIV1 Ab Ser IF-aCnc</td>
<td colspan="3">HIV 1 Ab [Units/volume] in Serum by Immunofluorescence</td>
</tr>
<tr class="odd">
<td>44533-8</td>
<td>HIV1+2 Ab Ser Donr Ql</td>
<td colspan="3">HIV 1+2 Ab [Presence] in Serum from donor</td>
</tr>
<tr class="even">
<td>44607-0</td>
<td>HIV1 Ser EIA-Imp</td>
<td colspan="3">HIV 1 [interpretation] in Serum by Immunoassay</td>
</tr>
<tr class="odd">
<td>44873-8</td>
<td>HIV1+2 Ab Ser Ql IB</td>
<td colspan="3">HIV 1+2 Ab [Presence] in Serum by Immunoblot (IB)</td>
</tr>
<tr class="even">
<td>49580-4</td>
<td>HIV1+2 Ab XXX Ql Rapid</td>
<td colspan="3">HIV 1+2 Ab [Presence] in Unspecified specimen by Rapid test</td>
</tr>
<tr class="odd">
<td>49905-3</td>
<td>HIV1 Ab XXX Ql Rapid</td>
<td colspan="3">HIV 1 Ab [Presence] in Unspecified specimen by Rapid test</td>
</tr>
<tr class="even">
<td>5221-7</td>
<td>HIV1 Ab Ser Ql IB</td>
<td colspan="3">HIV 1 Ab [Presence] in Serum by Immunoblot (IB)</td>
</tr>
<tr class="odd">
<td>53379-4</td>
<td>HIV1 Ab XXX Ql</td>
<td colspan="3">HIV 1 Ab [Presence] in Unspecified specimen</td>
</tr>
<tr class="even">
<td>54086-4</td>
<td>HIV1+2 IgG Bld.Dot Ql</td>
<td colspan="3">HIV 1+2 IgG Ab [Presence] in Blood dot (filter paper)</td>
</tr>
<tr class="odd">
<td rowspan="7">2b</td>
<td colspan="5">Adds LOINC Codes to CCR:HEPC Patient ID:</td>
<td rowspan="7">M</td>
</tr>
<tr class="even">
<td><strong>LOINC NUM</strong></td>
<td><strong>SHORTNAME</strong></td>
<td colspan="3"><strong>LONG_COMMON_NAME</strong></td>
</tr>
<tr class="odd">
<td>47365-2</td>
<td>HCV Ab Ser Donr Ql EIA</td>
<td colspan="3">Hepatitis C virus Ab [Presence] in Serum from donor by Immunoassay</td>
</tr>
<tr class="even">
<td>47441-1</td>
<td>HCV Ab Ser Donr Ql</td>
<td colspan="3">Hepatitis C virus Ab [Presence] in Serum from donor</td>
</tr>
<tr class="odd">
<td>48576-3</td>
<td>HCV RNA XXX Ql bDNA</td>
<td colspan="3">Hepatitis C virus RNA [Presence] in Unspecified specimen by Probe &amp; signal amplification method</td>
</tr>
<tr class="even">
<td>51655-9</td>
<td>HCV RNA Fld Ql PCR</td>
<td colspan="3">Hepatitis C virus RNA [Presence] in Body fluid by Probe &amp; target amplification method</td>
</tr>
<tr class="odd">
<td>51657-5</td>
<td>HCV Ab Fld Ql</td>
<td colspan="3">Hepatitis C virus Ab [Presence] in Body fluid</td>
</tr>
<tr class="even">
<td>3</td>
<td colspan="5"><p>Updates (by changing date selection criteria) the Microbiology data extraction code to capture missing Microbiology data. Extract now uses "completion date" and/or "date collected."</p>
<p><em>Prior to this patch, the Microbiology data extraction was pulling data based on the 'completion date' (DATE REPORT COMPLETED, #.03 in the MICROBIOLOGY sub-file #63.05 of the LAB DATA file #63) alone. It was found that many sites do not populate that field, causing microbiology data to be omitted from the nightly extract to the central registry. The extract will now pull data based on the 'date collected' (DATE/TIMESPECIMEN TAKEN, #.01) if the 'completion date' is null.</em></p></td>
<td>E</td>
</tr>
<tr class="odd">
<td>4</td>
<td colspan="5"><p>Corrects Problem List Extraction by using DATE RESOLVED versus DATE RECORDED.</p>
<p><em>Previously, the Problem List Extraction was pulling data from the wrong field (DATE RECORDED, #1.09) to populate the 'date resolved' field in the extract. Data is now correctly pulled from the DATE RESOLVED field (#1.07) of the PROBLEM file (#9000011).</em></p></td>
<td>F</td>
</tr>
<tr class="even">
<td>5</td>
<td colspan="5"><p>Adds new OBR and OBX segments to the nightly extract to pull Immunization data and Skin Test data for Registry patients (see <em>CCR Technical Manual</em>).</p>
<p><em>The nightly and historical extracts have been enhanced to include OBR and OBX segments for Immunization data and Skin Test data for registry patients. Immunization data and Skin Test data will be pulled if the DATE LAST MODIFIED (#.13 in the VISIT file (#9000010) is within the extract range. For details of the data included in the segments, please refer to the CCR Technical Manual.</em></p></td>
<td>E</td>
</tr>
<tr class="odd">
<td>6</td>
<td colspan="5"><p>Changes nightly data extract to include patients on the Pending list.</p>
<p><em>The CCR data extract (both nightly and historical) previously included data for 'confirmed' patients only. It will now include data for 'pending' patients as well. Previously, the DON'T SEND field (#11) in the ROR REGISTRY RECORD file (#798) was set to 'true' when a pending patient was added to the registry. With patch 10, the DON'T SEND field will be set to 'true' for test patients only.</em></p></td>
<td>E</td>
</tr>
<tr class="even">
<td rowspan="5">7</td>
<td colspan="5">Adds three new reports:</td>
<td rowspan="5">E</td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>Model for End-Stage Liver Disease (MELD) Score by Range</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>Body Mass Index (BMI) by Range</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>Renal Function by Range</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><em>These reports can be executed from the GUI application. See the User Manual for additional report information.</em></td>
</tr>
<tr class="odd">
<td>8</td>
<td colspan="5">Modifies existing report headers to reflect the Other Diagnosis filter (added by ROR*1.5*8)</td>
<td>E</td>
</tr>
<tr class="even">
<td>9</td>
<td colspan="5">Adds ALL REGISTRY MEDICATIONS to the Medications Selection panel via a new [All Registry Meds] button. This is included in the Combined Meds and Labs, Patient Medication History, and Pharmacy Prescription Utilization reports.</td>
<td>E</td>
</tr>
<tr class="odd">
<td>10</td>
<td colspan="5"><p>Adds new checkbox to display Pending Comments on the List of Registry Patients report.</p>
<p><em>The "List of Registry Patients" report has been enhanced to include a "Pending Comments" column added to the Report Options. If this option is checked, an additional column called Pending Comments will be added as the right-most column of the report. If the Registry Status' Pending check box is not checked, the Pending Comments option will be disabled.</em></p></td>
<td>E</td>
</tr>
<tr class="even">
<td>11</td>
<td colspan="5"><p>Replaces Direct global and FileMan reads to the International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM) files with calls using supported Application Program Interfaces (APIs).</p>
<p><em>To support encapsulation of data in the ICD-9-CM package, direct global and FileMan reads previously used in the ROR namespace were replaced with calls using supported ICD-9-CM APIs. These supported APIs retrieve Diagnosis information needed by the CCR application for the extracts and reports.</em></p></td>
<td>E</td>
</tr>
<tr class="odd">
<td>12</td>
<td colspan="5"><p>Modifies Other Diagnosis filter to allow the user to remove group header from the "selected" box when the user removes a group from the "selected" panel.</p>
<p><em>If the user highlights the header and presses the delete key, the header will be deleted. In addition, if the user highlights the header and hits the left arrow, the header will be deleted. Previously, the header was not being removed from the selected box.</em></p>
<p><em>Reports with the 'Other Diagnoses' filter have been modified to display the selected diagnoses in the report header. One of the three formats shown below will be displayed on the report, depending on what the user selected.</em></p>
<p><em>Diagnoses: All</em></p>
<p><em>Diagnoses: Include abc, def, etc.</em></p>
<p><em>Diagnoses: Exclude abc, def, etc.</em></p></td>
<td>M</td>
</tr>
<tr class="even">
<td>13</td>
<td colspan="5">Modifies the "Help About" popup to conform to VA standards, including hyperlinks to reference documents.</td>
<td>E</td>
</tr>
<tr class="odd">
<td>14</td>
<td colspan="5">Modifies the online help file to make it <a href="#Glos_CSH">context-sensitive</a>.</td>
<td>E</td>
</tr>
<tr class="even">
<td>15</td>
<td colspan="5">Updates the GUI application to work toward adherence to the <a href="#Glos_508">Section 508</a> standards.</td>
<td>M</td>
</tr>
<tr class="odd">
<td>16</td>
<td colspan="5">Reports XML code have been updated to address a bug introduced in Internet Explorer 7 that was causing page breaks to not work correctly.</td>
<td>F</td>
</tr>
</tbody>
</table>

<span id="_Ref331664104" class="anchor"></span>Table 16 – Patch ROR\*1.5\*18 Description

#### Patch ROR\*1.5\*13 

<table>
<caption><p><span id="_Ref347992427" class="anchor"></span>Table 17 – Patch ROR*1.5*19 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Adds LOINC code 57006 to the VA HEPC entry of the Lab Search criteria in the ROR LAB SEARCH file (#798.9), sub-file LAB TEST (#2).</td>
<td>M</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>Enhances the nightly and historical HL7 extracts to include ORC and RXE segments for Non-VA medications for registry patients. Non-VA</p>
<p>medication data will be pulled if the DOCUMENTED DATE (#11) or the</p>
<p>DISCONTINUED DATE (#6) in the NON-VA MEDS sub-file (#52.2) of the PHARMACY PATIENT file (#55) is within the extract range.</p></td>
<td>E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Enhances the Patient Medication History report to allow users to select the most recent fill only, or all fills. The report output has been enhanced to include a column displaying the number of fills remaining.</td>
<td>E</td>
</tr>
<tr class="even">
<td>4</td>
<td>Reports BMI by Range, MELD Score by Range, and Renal Function by Range have been enhanced to allow users to sort the report output by the calculations. The BMI by Range report can be sorted by the BMI score. The MELD Score by Range report can be sorted by the MELD or the MELD-Na score. The Renal Function by Range report can be sorted by the CrCL or the eGFR score.</td>
<td>E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>All reports (except Outpatient Utilization, Inpatient Utilization, List of Registry Patients, and Current Inpatient List) will allow users to select specific clinics or divisions. All reports (except List of Registry Patients and Current Inpatient List) will allow users to select specific patients.</td>
<td>E</td>
</tr>
<tr class="even">
<td>6</td>
<td>When users want to select specific medications in the Combined Meds And Labs report or the Patient Medication History report, the text in the search box will automatically convert to uppercase.</td>
<td>E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The CCR GUI application will now check VistA for the CCR server version, and it will display a message if the CCR GUI and the CCR server version are out of sync with each other.</td>
<td>E</td>
</tr>
<tr class="even">
<td>8</td>
<td>The CCR GUI was updated to work towards becoming fully compliant with the <a href="#Glos_508">Section 508</a> standards.</td>
<td></td>
</tr>
<tr class="odd">
<td>9</td>
<td>An historical data extraction for Non-VA meds is added to the ROR HISTORICAL DATA EXTRACTION file (#799.6). It will automatically execute during the next nightly extract, and there is no manual intervention required by the sites. The extraction date range for this historical data extraction is 1/1/1985 through current date (installation date).</td>
<td>E</td>
</tr>
</tbody>
</table>

<span id="_Ref347992427" class="anchor"></span>Table 17 – Patch ROR\*1.5\*19 Description

#### Patch ROR\*1.5\*14 

| \#  |                                                                                                                                                                                                                                                                                                                                                    | Type |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| 1   | The 13 risk factors for the HIV registry have been changed from mandatory to optional.                                                                                                                                                                                                                                                             | E    |
| 2   | Currently, within the Patient Data Editor in the HIV registry, the user is prompted to click a checkbox if the patient "ever had an AIDS OI." This prompt and checkbox has been replaced with the question "Did the patient ever have an AIDS OI?" and the option to select either Yes, No, or Unknown has been added to the checkbox. | E    |
| 3   | The following mandatory question has been added to the Patient Data Editor: "Was your VHA facility/station the first health care setting (VA or non-VA) to diagnose HIV?" along with a checkbox to select either Yes, No or Unknown.                                                                                                   | E    |
| 4   | A new column has been added to the List of Registry Patients Report that allows the user to select "Diagnosed at this facility." This column indicates whether this facility was the first health care setting (VA or Non-VA) to diagnose HIV.                                                                                                     | E    |
| 5   | The nightly extract has been enhanced to include Purchased Care data for registry patients.                                                                                                                                                                                                                                                        | E    |
| 6   | The "MELD Score by Range" report has been renamed to "Liver Score By Range".                                                                                                                                                                                                                                                                       | E    |
| 7   | The "Liver Score by Range" report now includes the list of LOINC codes used in the report.                                                                                                                                                                                                                                                         | E    |
| 8   | The "Renal Score by Range" report now includes the list of LOINC codes used in the report.                                                                                                                                                                                                                                                         | E    |
| 9   | The "Liver Score by Range" report now includes APRI and FIB-4 calculations.                                                                                                                                                                                                                                                                        | E    |
| 10  | Patients will be automatically confirmed into the HEPC Registry if they have a positive Hepatitis C Virus (HCV) viral load test result.                                                                                                                                                                                                            | E    |
| 11  | This patch brings the Clinical Case Registries (CCR) application into 508 compliance in many areas.                                                                                                                                                                                                                                                | E    |
| 12  | A historical data extraction for Purchased Care is added to the ROR HISTORICAL DATA EXTRACTION file (#799.6) for automatic execution during the next nightly extract.                                                                                                                                                                              | E    |

<span id="_Ref378227921" class="anchor"></span>Table 18 – Patch ROR\*1.5\*20 Description

#### Patch ROR\*1.5\*15 

<table>
<caption><p><span id="_Ref347992301" class="anchor"></span>Table 19 – Patch ROR*1.5*21 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>Three new HCV generic Drugs, Telaprevir, Boceprevir and Rilpivirine</p>
<p>were approved by the FDA in May, 2011. These three medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>The Renal Function by Range Report has been enhanced to include a new option for calculating the eGFR called the CKD-EPI equation. The CKD-EPI GFR is an estimate of glomerular filtration (GFR) using serum creatinine and demographic factors. It is a relatively new equation that is believed to be superior to the MDRD GFR equation. If selected, the CKD-EPI scores are summarized on the report by chronic kidney disease stage</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>The result ranges panel on the Renal Function by Range report will include a note that reads, "Lab tests used to calculate renal function are identified by LOINC code. Your local lab ADPAC should be contacted regarding errors in LOINC codes."</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>4</td>
<td>The header on the Renal Function by Range report currently reads, "Lab tests used to calculate Cockcroft-Gault and/or eGFR by MDRD scores are identified by LOINC code." This text will be updated to read, "Lab tests used in calculations are identified by LOINC code."</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>5</td>
<td>The cover sheet text of the Renal Function by Range report will be amended to include the list of LOINC codes that are used. The new text on the Renal Function by Range report will read, "Lab tests used to calculate scores are identified by LOINC code. Your local lab ADPAC should be contacted regarding errors in LOINC codes."</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>The Liver Score by Range report has been modified to display only those tests used in the calculation of the liver scores selected by the user. If the user selects the APRI and/or FIB4 tests, then the Bili, Cr, INR, and Na rows should not appear on the report. If the user selects the MELD and/or MELDNA tests, then the AST, Platelet, and ALT rows should not appear on the report.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The result ranges panel on the Liver Score by Range report will include a note that reads, "Lab tests used in calculations are identified by LOINC code. Your local lab ADPAC should be contacted regarding errors in LOINC codes."</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>8</td>
<td>Users may now use Diagnosed at this VA as a local field. This is a CCR:HIV only option.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Users may now type ?? or click the <strong>All Divisions</strong> button to display all Divisions in the left-hand pick box.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>10</td>
<td>The CDC Form has been modified to correct the transposition of check box values for the Bisexual male and Intravenous/injection drug user questions.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>11</td>
<td>The CDC Form has been modified to check the appropriate checkbox if the user selects 'yes' to the question Received Clotting Factor for Hemophilia/Coagulation disorder.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>12</td>
<td>An invalid date check and error message have been added for the question, Received transfusion of blood/blood components (other than clotting factor) on the <strong>Risk Factors</strong> tab in the Patient Editor.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>13</td>
<td>A future date check and error message have been added for the question, Received transfusion of blood/blood components (other than clotting factor) on the <strong>Risk Factors</strong> tab in the Patient Editor.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>14</td>
<td>A future date check and error message have been added for the question, Did the patient ever have an AIDS OI? on the <strong>Clinical Status</strong> in the Patient Editor.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>15</td>
<td>An historical data extraction for Non-VA Meds has been added to the ROR HISTORICAL DATA EXTRACTION file (#799.6) for automatic execution during the next nightly extract.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>16</td>
<td>The Date Range panels (<strong>Date Range</strong>, <strong>Medications Date Range</strong>, <strong>Lab Tests Date Range</strong> and <strong>Utilization Date Range</strong>) were re-designed for easier use with Assistive Technology.</td>
<td colspan="2">M</td>
</tr>
</tbody>
</table>

<span id="_Ref347992301" class="anchor"></span>Table 19 – Patch ROR\*1.5\*21 Description

#### Patch ROR\*1.5\*17

| \#  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     | Type |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | A new HIV generic drug, EMTRICI./RILPIVIRINE/TENOFOVIR (Complera) was approved by the Food and Drug Administration (FDA). This new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients taking the new medication.                                                                                                                                                                                                                                                                                  | E   |      |
| 2   | The List of Registry Patients report has been enhanced to allow users to specify an Only Confirmed After date. If the user selects this feature, the Pending box will be disabled. This will allow users to generate a list of recently confirmed patients that have been added to the registry after a specific date.                                                                                                                                                                                                                                                                       | E   |      |
| 3   | A new diagnosis group, Post Traumatic Stress Disorder (PTSD), has been added to the common templates. The ICD code for PTSD is 309.81.                                                                                                                                                                                                                                                                                                                                                                                                                                                       | E   |      |
| 4   | Lab test selection on the Lab Utilization report, the Combined Meds and Labs report, the DAA Lab Monitoring report and the Edit Site Parameters option in the GUI has been changed to be case insensitive. For example, if a user enters "zinc" as a search criterion, all test names for "zinc" will be returned regardless of the case of the test name in file \#60 (e.g. zinc, Zinc, ZINC, zINC, etc.). This problem was reported in Remedy ticket \#215842.                                                                                                                             | M   |      |
| 5   | The text on the Result Ranges panel and the report header of the Liver Score by Range report have been modified to provide additional instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                           | M   |      |
| 6   | The text on the Result Ranges panel and the report header of the Renal Function by Range report have been modified to provide additional instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                        | M   |      |
| 7   | A new HepC report, Potential DAA Candidates, has been added to identify patients who may be eligible for the new HepC Direct Acting Anti-Viral(DAA) medications. The user may request a list of HepC patients with treatment histories of 'naive' and/or 'experienced'. Patients who are 'naive' have never taken any registry medications. Patients who are 'experienced' have not received DAA medications but have taken other registry medications. The user may choose to exclude experienced patients who have fills for other registry medications within a specified number of days. | E   |      |
| 8   | A new HepC report, DAA Lab Monitoring, has been added to monitor laboratory results for patients who have taken DAAs. The user may display the two most recent test results prior to the first DAA fill date as well as selected lab test results for X weeks after the first DAA fill date. The user may also restrict the lab test results after the first DAA fill date to be the most recent. Any registry medications for the patient filled 60 days before the first DAA fill date through today display automatically on the report.                                                  | E   |      |
| 9   | The preview and printing of the CDC form has been modified to correct the transposition of check box values for the risk factors, Bisexual male and the Intravenous/injection drug user.                                                                                                                                                                                                                                                                                                                                                                                                     | F   |      |
| 10  | An installation problem with the CCR help file referenced in Remedy ticket \#233500 is corrected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | F   |      |
| 11  | This patch brings the Clinical Case Registries (CCR) application into 508 compliance in many areas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | F   |      |

<span id="_Ref395710517" class="anchor"></span>Table 20 – Patch ROR\*1.5\*22 Description

#### Patch ROR\*1.5\*18

<table>
<caption><p><span id="_Ref406161072" class="anchor"></span>Table 21 – Patch ROR*1.5*24 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch is designed to allow reporting tools used with the national Hepatitis C and HIV registries to be used with local registries. Sixteen new local registries are added based on ICD9 codes provided by the national Office of Public Health/Population Health. The new registries represent patient diagnostic groups for:</p>
<p>Alzheimer's Disease</p>
<p>Amputation</p>
<p>Breast Cancer</p>
<p>Cerebrovascular Disease (CVD)</p>
<p>Chronic Obstructive Pulmonary Disease (COPD)</p>
<p>Chronic Renal Disease (CRD)</p>
<p>Congestive Heart Failure (CHF)</p>
<p>Diabetes</p>
<p>Dyslipidemia</p>
<p>Hypertension</p>
<p>Ischemic Heart Disease (IHD)</p>
<p>Low Vision/Blind</p>
<p>Mental Health</p>
<p>Multiple Sclerosis</p>
<p>Osteoarthritis</p>
<p>Rheumatoid Arthritis</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>An option, Initialize new registries (one time) is provided to schedule the initial build of the new registries. The option is locked with the ROR VA IRM security key. It is run one time and will search for patients with qualifying ICD9 codes linked to outpatient visits, problem lists and inpatient stays back to 1/1/1985. Patients added to a local registry are automatically confirmed. The confirmation date is set to the earliest date of the qualifying ICD9 code. Registries are not available to users until they are initialized.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Once the registries are initialized, the nightly job (ROR TASK) searches for new patients with qualifying ICD9 codes. Patients added to one of the 16 local registries are automatically confirmed. The confirmation date is set to the date of the qualifying ICD code.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>Only data from the national registries for HIV and Hepatitis C will be transmitted to the national database.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Two new security keys have been added, ROR VA GENERIC ADMIN and ROR VA GENERIC USER. These keys only provide access to the local registries. Users assigned the new ROR VA GENERIC ADMIN key will have the ability to delete patients from any of the sixteen local registries. Patients are deleted immediately and the deletion is logged in the technical log. If the patient has a future qualifying result, the patient is added back to the appropriate registry.</p>
<p>Users with the ROR VA GENERIC USER key will have the ability to run reports on all the local registries.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>It will no longer be necessary to run the option, Re-index the ACL cross-reference manually after assigning or un-assigning a security key. The user's access privileges will be automatically updated at the time the user logs on.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The Select a Registry screen displayed when the user logs on, will list all the registries to which the user has keys. The national registries for Hepatitis C and HIV will be listed first. The local registries will be listed next in alphabetical order separated from the national registries by a blank line.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td>The Patient screen for local registries does not include a Pending only checkbox or a Pending Comments column because patients added to local registries are automatically confirmed.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>Site parameters can be customized for local registries. The site parameters screen displays tabs for Lab Tests, Notifications and Local Fields. A generic tab on the right side of the screen displays laboratory tests. Select local laboratory tests under the Registry Lab tab and move them to the right. Once a laboratory test is added, it is displayed in the middle pane of the Registry Lab Patient Data Editor.</p>
<p>The names of VistA users who need to receive notifications about problems in registry processes can be added under the Notifications tab.</p>
<p>Local fields can also be added to individual local registries. These fields are used to include/exclude patients from reports.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>The following reports can be run for local registries:</p>
<p>BMI by Range Report</p>
<p>Clinic Follow Up Report</p>
<p>Combined Meds and Labs Report</p>
<p>Current Inpatient List Report</p>
<p>Diagnosis Report</p>
<p>General Utilization and Demographics Report</p>
<p>Procedures Report</p>
<p>Radiology Utilization Report</p>
<p>Inpatient Utilization Report</p>
<p>Lab Utilization Report</p>
<p>Liver Score by Range Report</p>
<p>Outpatient Utilization Report</p>
<p>Patient Medication History Report</p>
<p>Pharmacy Prescription Utilization Report</p>
<p>Renal Function by Range Report</p></td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>11</td>
<td>The List of Registry Patients can be run for local registries but has been modified for use with local registries. The Pending checkbox has been removed from the Report Status panel. Pending comments and First diagnosed at this facility checkboxes have been removed from the Report Options panel.</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>12</td>
<td><p>The following reports are not supported for local registries:</p>
<p>DAA Lab Monitoring Report</p>
<p>Potential DAA Candidates Report</p>
<p>Registry Lab Tests by Range Report</p>
<p>Registry Medications Report</p>
<p>VERA Reimbursement Report</p></td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>13</td>
<td>If the user has keys for the registries, the Other Registries selection panel will display those registries. Registries listed in this panel can be used to include/exclude patients on reports.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>14</td>
<td>The Common Template for Depression has been deleted and replaced with two new Common Templates for Major Depression and Other Depression. These templates are used to filter patients based on diagnoses when running reports.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>15</td>
<td>ROR TASK has been modified to automatically update all registries. It is no longer necessary to list registries in the TASK PARAMETERS field. The description of the option has been modified to reflect this change.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>16</td>
<td>The Select Patient panel has been added to the DAA Lab Monitoring report.</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref406161072" class="anchor"></span>Table 21 – Patch ROR\*1.5\*24 Description

#### Patch ROR\*1.5\*19

<table>
<caption><p><span id="_Ref381714483" class="anchor"></span>Table 22 – Patch ROR*1.5*27 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>The registry update process allows the Reason for Selection for a patient added to a Registry to include ICD-10 code in outpatient file, ICD-10 code in inpatient file, or ICD-10 code in the Problem List.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>The ICD-10 diagnoses and ICD-10 procedure codes can be searched for in the Report parameters.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>The ICD-10 diagnoses codes can be saved in Your Templates along with the ICD-9 diagnoses codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>The Common Templates were updated to include ICD-10 codes.</p>
<p>Note: The pre-install routine saves the current Common Templates in ^TMP("ROR",$J) global before updating them with ICD-9 and ICD-10 codes. Any changes done to Common Templates will be lost after the installation of this patch.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>The reports now show ICD-10 diagnoses and procedure codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>The CCR Registry information that is sent to the National Database via HL7 messages now differentiates between ICD-9 and ICD-10 diagnoses codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The CCR PD team released CCR Patch ROR*1.5*17 which added the new PTSD Common Template and two new HEPC reports. The changes have been absorbed into ROR*1.5*19 so that both patches may co-exist.</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>8</td>
<td>The CCR PD team released CCR Patch ROR*1.5*18 which includes the minimal technical code and data dictionary changes for 16 new registries. The changes have been absorbed into ROR*1.5*19 so that both patches may co-exist.</td>
<td colspan="2">M</td>
</tr>
</tbody>
</table>

<span id="_Ref381714483" class="anchor"></span>Table 22 – Patch ROR\*1.5\*27 Description

#### Patch ROR\*1.5\*20

<table>
<caption><p><span id="_Ref413159537" class="anchor"></span>Table 23 – Patch ROR*1.5*25 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>VA Product</p>
<p>COBICISTAT/ELVITEGRAVIR/EMTRICITABINE/TENOFOVIR DF TAB, ORAL</p>
<p>VA Generic</p>
<p>COBICISTAT/ELVITEGRAVIR/EMTRICITABINE/TENOFOVIR</p>
<ol type="1">
<li><p>VA Product: COBICISTAT/ELVITEGRAVIR/EMTRICITABINE/TENOFOVIR DFTAB,ORAL</p></li>
<li><p>VA Generic Name: COBICISTAT/ELVITEGRAVIR/EMTRICITABINE/TENOFOVIR</p></li>
<li><p>Dosage Form: TAB,<br />
ORAL</p></li>
<li><p>Strength: (5)<br />
Units:</p></li>
<li><p>Nat' Formulary Name: COBICISTAT/ELVITEGRAVIR/EMTRICITABINE/TENOFOVIR TAB,ORAL</p></li>
<li><p>VA Print Name: STRIBILD ORAL TAB</p></li>
<li><p>VA Product Identifier: C1522</p></li>
<li><p>Transmit to CMOP: Yes</p></li>
<li><p>VA Dispense Unit: TAB</p></li>
</ol></td>
<td>1</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch brings the Clinical Case Registries (CCR) application into</p>
<p>508 compliance in many areas.</p></td>
<td>2</td>
</tr>
</tbody>
</table>

<span id="_Ref413159537" class="anchor"></span>Table 23 – Patch ROR\*1.5\*25 Description

#### Patch ROR\*1.5\*21

<table>
<caption><p><span id="_Ref420942569" class="anchor"></span>Table 24 – Patch ROR*1.5*26 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following medication:</p>
<ul>
<li><p>VA Product: DOLUTEGRAVIR</p></li>
<li><p>VA Generic: DOLUTEGRAVIR</p></li>
</ul>
<p>This new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>A new local registry, Obstructive Sleep Apnea (VA APNEA), was added based on ICD9 codes provided by the  national Office of Public Health/Population Health. </td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>An additional selection panel titled "Sex" will be created.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>An additional selection panel titled "Additional Identifier" will be created.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>To  facilitate off-line record matching, patient ICN will be added to all reports, except the Current Inpatient List.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>The "Utilization Date Range" selection panel will be added to the Diagnosis Report in order to provide sites with the ability to run reports that limit output to patients with utilization within a specific date range.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Report enhancement for screen on gender.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td>Report enhancement for addition of optional ICN column.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>9</td>
<td>The nightly HL7 message will be updated to also include the number of reports run in all of the local registries including the new Obstructive Sleep Apnea Registry.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>This patch brings the Clinical Case Registries (CCR) application into</p>
<p>508 compliance in many areas.</p></td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref420942569" class="anchor"></span>Table 24 – Patch ROR\*1.5\*26 Description

#### Patch ROR\*1.5\*22

<table>
<caption><p><span id="_Ref480062722" class="anchor"></span>Table 25 – Patch ROR*1.5*28 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following new medications:</p>
<ul>
<li><p>VA Product: SIMEPREVIR</p></li>
<li><p>VA Generic: SIMEPREVIR</p></li>
<li><p>VA Product: SOFOSBUVIR</p></li>
<li><p>VA Generic: SOFOSBUVIR</p></li>
</ul>
<p>These new medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>An additional selection panel titled "OEF/OIF" will be created in the CCR GUI to allow selection of report content by a check for patient's OEF/OIF service status.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Report enhancements for screen on OEF/OIF/OND period of service, including updating the ROR REPORT PARAMETERS file (#799.34), field PARAMETER PANELS field (#1) to include the new panel '25' for OEF/OIF/OND.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>All local registries will be updated with the appropriate International Classification of Diseases, Tenth Revision (ICD-10) codes for compliance with national mandates.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>A modification was made to the RULE NAME field (#.01) in the ROR SELECTION RULE file (#798.2). The length of the field was increased from 30 to 40 characters.</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>6</td>
<td>A modification was made to the SELECTION RULE field (#.01), of the SELECTION RULE field (#3) (subfile #798.13) of the ROR REGISTRY PARAMETERS file (#798.1). The length of the field was increased from 30 to 40 characters.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The system will now notify a mail group if the nightly job [ROR TASK] does not run due to the initiating user no longer possessing the ROR VA IRM security key.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td><p>This patch brings the Clinical Case Registries (CCR) application into</p>
<p>508 compliance in many areas.</p></td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref480062722" class="anchor"></span>Table 25 – Patch ROR\*1.5\*28 Description

#### Patch ROR\*1.5\*24

<table>
<caption><p><span id="_Ref480062806" class="anchor"></span>Table 26 – Patch ROR*1.5*29 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>Eight new local registries were added based on ICD9 codes provided by the  national Office of Public Health/Population Health. </p>
<p>Osteoporosis (VA OSTEOPOROSIS), Prostate Cancer (VA PROSTATE CANCER), Lung Cancer (VA LUNG CANCER), Melanoma (VA MELANOMA), Colorectal Cancer (VA COLORECTAL CANCER), Pancreatic Cancer (VA COLORECTAL CANCER), Hepatocellular Carcinoma (VA HCC), ALS (VA ALS)</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>Removal of the requirement that a Hepatitis C GT lab test must be specified in the site parameters before the Potential DAA Candidates report can be run.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Addition of new HIV antibody and antigen codes to the VA HIV registry.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>Addition of new LOINC codes to the Hepatitis C registry antibody search.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>A new Hepatitis C report, Sustained Virologic Response, has been added to identify patients who have had a SVR after treatment with HepC antiviral medications.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>A modification was made to copy CCR application help files to the local workstation when CCR is accessed on a server or network.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>This patch brings the Clinical Case Registries (CCR) application into</p>
<p>508 compliance in many areas.</p></td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref480062806" class="anchor"></span>Table 26 – Patch ROR\*1.5\*29 Description

#### Patch ROR\*1.5\*27

<table>
<caption><p><span id="_Toc165646482" class="anchor"></span>Table 27 – Patch ROR*1.5*30 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following new medications:</p>
<ul>
<li><p>VA Product: ABC/DOL/3TC</p></li>
<li><p>VA Generic: ABACAVIR/DOLUTEGRAVIR/LAMIVUDINE</p></li>
<li><p>VA Product: LED/SOF</p></li>
<li><p>VA Generic: LEDIPASVIR/SOFOBUVIR</p></li>
<li><p>VA Product: OBV/PTV/r+DSV</p></li>
<li><p>VA Generic: DASABUVIR/OMBITASVIR/PARITAPREVIR/RITONAVIR</p></li>
</ul>
<p>These new medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>Modifications to the Potential DAA Candidate report to remove exclusion of patients who received Boceprevir or Telaprevir.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Modifications to the Potential DAA Candidate report to remove exclusion of patients who do not have genotype 1.</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>4</td>
<td>Correct the definition of Sustained virologic response (SVR) by removing the criteria that patients whose lab results starts with "&gt;" have SVR.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Correct the List of Patients Report selection screen by disabling the Registry Status Pending Comment check box if Pending is not checked. (GUI)</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>6</td>
<td>Update Help Files Copied to Local Drive for Network Installations (GUI)</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>7</td>
<td>This patch brings the Clinical Case Registries (CCR) application into Section 508 compliance in many areas.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td>Modified the global lock logic in routine RORLOCK to utilize the minimum default lock time system variable DILOCKTM rather than 3 seconds. This is a correction for a SACC violation reported in Remedy ticket #968114 (DILOCKTM not being utilized).</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Resolved a problem involving a maxstring error occurring in the nightly job. This was reported in Remedy tickets # 1228316 and 1227499</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>The post-initialization routine for this patch will:</p>
<ul>
<li><p>Reactivate any of the 8 registries added in patch ROR*1.5*24 that have been marked as inactive.</p></li>
<li><p>Add entries to the ROR LIST ITEM file (#799.1) for each of the 8 registries added in patch ROR*1.5*24 and the VA APNEA registry that are needed to allow the proper display of the Result Ranges panels on the BMI by Range, Liver Score by Range and Renal Function by Range reports.</p></li>
</ul></td>
<td colspan="2">F</td>
</tr>
</tbody>
</table>

<span id="_Toc165646482" class="anchor"></span>Table 27 – Patch ROR\*1.5\*30 Description

#### Patch ROR\*1.5\*25

| \#  | Description                                                                                                                                                                                                                                                                                                          |     | Type |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | The HL7 nightly extract option Registry Update & Data Extraction \[ROR TASK\] was modified to extract up to 25 ICD-10 diagnoses and procedures contained in an inpatient record.                                                                                                                                     | E   |      |
| 2   | The process to populate a new registry with qualifying patients was modified to use up to 25 ICD-10 diagnoses and procedures contained in an inpatient record.                                                                                                                                                       | E   |      |
| 3   | The selection logic for all CCR reports that screen the output based on diagnosis has been modified to check the additional fields added to the PTF file for ICD-10.                                                                                                                                                 | E   |      |
| 4   | The HL7 nightly extract option Registry Update & Data Extraction \[ROR TASK\] was modified so the Admitting Diagnosis OBX segment extraction logic only extracts the data from the PTF file (#45) for the PRINCIPAL DIAGNOSIS pre-1986 field (#80) if the PRINCIPAL DIAGNOSIS field (#79) does not contain any data. | M   |      |

<span id="_Ref448219212" class="anchor"></span>Table 28 – Patch ROR\*1.5\*31 Description

| ![](ror-1-5-42-technical-manual-security-guide/012.png) | Note: Patch ROR\*1.5\*25 is available only as part of the ICD-10 PTF File Modifications project along with six other patches, which are being released within a single Kernel Installation & Distribution System (KIDS) host file ICD_10_PTF_MODIFICATIONS.KID. The GUI portion of the ROR\*1.5\*25 patch will still be released as a separate .zip file. Refer to the installation guide for patch DG\*5.3\*884 for installation details as no individual installation guide will be provided for this patch. |
|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref534368869" class="anchor"></span>Table 29 – Patch ROR\*1.5\*32 Description

#### Patch ROR\*1.5\*26

<table>
<caption><p><span id="_Ref504478211" class="anchor"></span>Table 30 – Patch ROR*1.5*33 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Conversion of GUI from Delphi 2006 to Embarcardero XE5.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>Enhanced reporting functionality: A new Selection Panel on each report to allow the user to limit the report to Veterans based on the two categories of No SVR and SVR. This selection panel will not be included on the SVR report.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Enhanced reporting functionality: Updated the existing Potential Direct Acting Antiviral (DAA) Candidate report by adding an optional filter based on Fibrosis-4 (FIB-4) score and Liver Score Date Range filter(which is an option in the Liver Score by Range report) .</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>Enhanced reporting functionality: Updated the existing save as functionality so that when a user saves a report as a csv file that the information for all Veterans appears in one worksheet</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Create New Diagnosis group for Liver Transplantation and add it to the Common Templates. The new group will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>A situation reported in Remedy ticket INC000001240065 that involved the registry initialization job starting to run within a time period when it was supposed to be suspended has been fixed.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Create two new Local Registries, Total Knee Replacement and Total Hip Replacement. The new local registries will be defined using ICD-9, ICD-10, and CPT Codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td>Update M version check</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>9</td>
<td>The version of the CCR software is updated to 1.5.26</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>10</td>
<td>Modified Custom Controls within the CCR GUI to ensure Section 508 Certification.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>11</td>
<td><p>The post-initialization routine for this patch will:</p>
<blockquote>
<p>- Add the Liver Transplantation diagnosis group to common templates.</p>
<p>- Add new panels for FIB-4 and SVR to the appropriate reports.</p>
<p>- Add references to the new inpatient procedures fields to ROR METADATA file (#799.2).</p>
<p>- Add the 2 new registries to the ROR ICD SEARCH file (#798.5) along with their corresponding procedure codes (ICD-9, ICD-10 and CPT).</p>
<p>- Add new registries to the LIST ITEM file (#799.1) for each of the 2 registries added in this patch that are needed to allow the proper display of the Result Ranges panels on the BMI by Range, Liver Score by Range and Renal Function by Range reports.</p>
<p>- Schedule the Initialize new registries (one time) [ROR INITIALIZE] option to run.</p>
</blockquote></td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref504478211" class="anchor"></span>Table 30 – Patch ROR\*1.5\*33 Description

#### Patch ROR\*1.5\*28

<table>
<caption><p><span id="_Ref20206942" class="anchor"></span>Table 31 – Patch ROR*1.5*34 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Conversion of GUI from Delphi XE5 to Delphi XE8.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>Create five new Local Registries; Crohn's Disease, Dementia, Hepatitis B, Thyroid Cancer and Ulcerative Colitis. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>It was discovered that the CCR national database is missing some problem list entries for the patients in the HIV and Hepatitis-C registries dating from 2009 through 2011. To recover this data, this patch will force the CCR nightly job [ROR TASK] to perform a one time re-extract of all problem list entries that were added from 1/1/2009 to the present for patients in these two registries. This may cause a slight increase in the amount of time it takes the nightly job to finish the first time it runs after the installation of this patch.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>4</td>
<td>A problem was discovered with the header display if a user selects the "Complete" or "Summary" report option when running a report. The words "Complete Report" or "Summary Report" are supposed to display after the label Options:, but currently, nothing is being displayed there.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>This patch adds the following new medications:</p>
<ul>
<li><p>HIV registry: ATAZANAVIR/COBICISTAT</p></li>
<li><p>HIV registry: COBICISTAT/DARUNAVIR</p></li>
<li><p>HIV registry: ELVITEGRAVIR</p></li>
<li><p>HIV registry: ELBASVIR/GRAZOPREVIR</p></li>
<li><p>Hepatitis C registry: OMBITASVIR/PARATEPREVIR/RITONAVIR</p></li>
<li><p>Hepatitis C registry: DACLATASVIR</p></li>
</ul>
<p>These new medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>An additional selection panel titled "DAA Prescriptions" will be created for the DAA Lab Monitoring report.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The INPATIENT UTILIZATION report was modified to correct a defect found where the ICN value does not appear on the report when the user selects to include additional identifier in the report.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>8</td>
<td><p>When the VA TOTAL KNEE and VA TOTAL HIP registries were added to</p>
<p>the CCR system by a previous patch, the word Registry was not added to the display name of the registries. This was fixed in this patch by adding the word 'Registry' to the entry in the SHORT DESCRIPTION (#4) field of the ROR REGISTRY PARAMETERS file (#798.1) for the VA TOTAL KNEE and VA TOTAL HIP registry entries.</p></td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>9</td>
<td>A modification was made to allow the DAA Lab Monitoring report to use all drugs defined for the registry as well as locally defined drugs as screening criteria for the report.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>10</td>
<td>The version of the CCR software is updated to 1.5.28</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref20206942" class="anchor"></span>Table 31 – Patch ROR\*1.5\*34 Description

#### Patch ROR\*1.5\*29

| \#  | Description                                                                                                                                                                                                                                                                                                                                |     | Type |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | An additional selection panel titled "Diagnosis Date Range" will be created for the reports that use Other Diagnoses panel.                                                                                                                                                                                                                | E   |      |
| 2   | A new Hepatitis A report has been added to identify patients who either had Hepatitis A vaccine or have immunity to the Hepatitis A virus – or to identify patients who have not had the Hepatitis A vaccine and are not immune. It is available to all registries.                                                                        | E   |      |
| 3   | A new Hepatitis B report is to identify patients who either had Hepatitis B vaccine or have immunity to the Hepatitis B virus and do not have chronic HBV – or to identify patients who have not had Hepatitis B vaccine and are not immune and do not have chronic HBV. It is available to all registries except the Hepatitis B registry | E   |      |
| 4   | An additional selection panel titled "Patients" will be created for the Hepatitis A report.                                                                                                                                                                                                                                                | E   |      |
| 5   | An additional selection panel titled "Patients" will be created for the Hepatitis B report.                                                                                                                                                                                                                                                | E   |      |
| 6   | An additional selection panel titled "Vaccinations Date Range" will be created for the Hepatitis A and Hepatitis B reports.                                                                                                                                                                                                                | E   |      |
| 7   | An additional selection panel titled "Immunity Date Range" will be created for the Hepatitis A and Hepatitis B reports.                                                                                                                                                                                                                    | E   |      |
| 8   | The version of the CCR software is updated to 1.5.29                                                                                                                                                                                                                                                                                       | E   |      |

<span id="_Toc165646487" class="anchor"></span>Table – Patch ROR\*1.5\*35 Description

#### Patch ROR\*1.5\*30

<table>
<caption><p><span id="_Toc165646488" class="anchor"></span>Table – Patch ROR*1.5*36 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create two new Local Registries; Hypoparathyroidism and Idiopathic Pulmonary Fibrosis. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>It was discovered that the Hepatitis A and Hepatitis B reports were not finding all patients who have laboratory documented immunity.   HCV and HIV labs have always used case insensitive searches for positive LOINC results so results entered in mixed case  were missed.  The code has been modified to ignore case when searching for results.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>3</td>
<td>The caption on the Sex panel has been modified from Sex to Birth Sex. The output for the report headers and report columns were modified appropriately.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><p>Hepatitis C registry: SOFOSBUVIR/VELPATASVIR</p></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>The warning on the Potential DAA Candidates report has been updated to  remove the reference  to genotype 1, as the report no longer requires genotype 1.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Additional CCR GUI updates were made to work towards becoming fully</p>
<p>compliant with the Section 508 standards.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The version of the CCR software is updated to 1.5.30</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc165646488" class="anchor"></span>Table – Patch ROR\*1.5\*36 Description

#### Patch ROR\*1.5\*31

<table>
<caption><p><span id="_Toc165646489" class="anchor"></span>Table – Patch ROR*1.5*37 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create two new Local Registries; Adrenal Adenoma and Movement Disorders. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><p>Hepatitis C registry: SOFOSBUVIR/VELPATASVIR /VOXILAPREVIR</p></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>In the CCR GUI, a new AGE_RANGE panel has been added to all reports to allow filtering by age or date of birth. The new panel has been added in the GUI after the "Birth Sex" panel and a new column for Age/DOB has been added to all report headers following the Last 4 digits of SSN column. If the user selects all for "Age Range" no Age/DOB column is added.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>On the Pharmacy Prescription Utilization report, it was discovered that the patient ICN was missing on the portion of the report that lists the Highest Combined Outpatient (OP) and Inpatient (IP) Utilization Summary. The report has been updated to include the ICN.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>5</td>
<td>On the Diagnoses report, a modification was made to keep the display of Date of Death (DOD) consistent with other reports. Currently, if a time piece exists in VistA for the DOD, the Diagnoses report displays the DOD as the date with the time included. All the other reports display the DOD as just the date without the time. The time stamp has been removed from the Date of Death column on the Diagnoses report to ensure consistency among reports.</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>6</td>
<td>In the CCR GUI, the caption on the Additional Identifier panel has been modified from Additional Identifier to Additional Identifiers.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>7</td>
<td>In the CCR GUI, two new options have been added to the Additional Identifiers panel to allow the Patient Aligned Care Team (PACT) and/or Primary Care Provider (PCP) to be included on all the reports. Two new report columns, entitled "PACT" and "PCP," will be added to the report output following the column titled "ICN." If selected, these new report columns will be added everywhere "ICN" currently appears in reports.  The column widths for these new columns will be sized to accommodate approximately 30 characters.  If a patient does not have a PACT or PCP, the output will be blank.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td>In the CCR GUI, a modification was made on several of the "utilization" reports when the user selects the "Include details" option the associated edit control color has been updated to indicate to the user that the control is enabled.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>In the CCR GUI, a modification was made on the reports listed below to disable the Additional Identifiers panel if the Summary option was selected.</p>
<ul>
<li><p>BMI by Range</p></li>
<li><p>Diagnoses</p></li>
<li><p>General Utilization and Demographics</p></li>
<li><p>Inpatient Utilization</p></li>
<li><p>Lab Utilization</p></li>
<li><p>Outpatient Utilization</p></li>
<li><p>Pharmacy Prescription Utilization</p></li>
<li><p>Procedures</p></li>
<li><p>Radiology Utilization</p></li>
<li><p>Registry Medications</p></li>
<li><p>Renal Function by Range</p></li>
<li><p>VERA Reimbursement</p></li>
</ul></td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>10</td>
<td>On the General Utilization and Demographics report, a modification was made to the report to remove the "No data has been found" message if the Summary option is selected and there was data to generate a summary.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>11</td>
<td>The version of the CCR software is updated to 1.5.31</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc165646489" class="anchor"></span>Table – Patch ROR\*1.5\*37 Description

#### Patch ROR\*1.5\*32

<table>
<caption><p><span id="_Toc165646490" class="anchor"></span>Table – Patch ROR*1.5*38 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create two new Local Registries; Transgender and Frailty. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><p>HEP C registry: GLECAPREVIR/PIBRENTASVIR</p></li>
<li><p>HIV registry: DOLUTEGRAVIR/RILPIVIRINE</p></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>In the CCR GUI, a new "Admitting Diagnosis" column has been added to the Current Inpatient List report. The new column will be located after the "Room-Bed" column.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>On the Hepatitis A and Hepatitis B Immunity reports, the report results have been modified to look at the most recent immune status.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>The Patient Medication History report has been modified to include all medications even if the drugs are unmatched to the VA Products.</p>
<p>To resolve this issue the following changes have been made:</p>
<ul>
<li><p>The post install routine of the patch has been designed to collect existing drug matching on daily basis and store them in ROR files.</p></li>
<li><p>A nightly job which will be executed automatically is called Schedule ROR Drug Match [ROR DRUG MATCH]</p></li>
<li><p>The Patient Medication report has been modified to check the new matching nodes created by this patch if they do not exist in pharmacy side.</p></li>
</ul></td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>6</td>
<td>In the CCR GUI, the title on the Patient Data Editor screen has been modified to display the correct registry name when a local registry is selected.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>7</td>
<td>In the CCR GUI, the BMI by Range and Renal Function by Range CSV report output has been modified to not display "No data has been found" when the Summary only option was selected for the report.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>8</td>
<td>In the CCR GUI, a "More" button has been added after the "Patients found" count when there are more patients than the maximum number of patients to retrieve setting is set for.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>9</td>
<td>The version of the CCR software is updated to 1.5.32</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc165646490" class="anchor"></span>Table – Patch ROR\*1.5\*38 Description

#### Patch ROR\*1.5\*33

<table>
<caption><p><span id="_Toc165646491" class="anchor"></span>Table – Patch ROR*1.5*39 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create six new Local Registries; Transplant Heart, Transplant Intestine, Transplant Kidney, Transplant Liver, Transplant Lung and Transplant Pancreas. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch adds the following new medications:</p>
<ul>
<li><p>HIV registry: BICTEGRAVIR/EMTRICITABINE/TENOFOVIR ALAFENAMIDE</p></li>
<li><p>HIV registry: EFAVIRENZ/LAMIVUDINE/TENOFOVIR DISOPROXIL FUMARATE</p></li>
<li><p>HIV registry: LAMIVUDINE/TENOFOVIR DISOPROXIL FUMARATE</p></li>
</ul>
<p>The new medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>In the CCR GUI, a new "Future Appointments" panel has been added to the following reports for all registries:</p>
<ul>
<li><p>BMI by Range</p></li>
<li><p>Combined Meds and Labs</p></li>
<li><p>Hepatitis A Vaccine or Immunity</p></li>
<li><p>Hepatitis B Vaccine or Immunity</p></li>
<li><p>Liver Score by Range</p></li>
<li><p>Registry Lab Tests by Range</p></li>
<li><p>Renal Function by Range</p></li>
</ul>
<p>It has also been added in the Hepatitis C registry to the following report:</p>
<ul>
<li><p>Potential DAA Candidates</p></li>
</ul>
<p>The new panel has been added after the "Additional Identifiers" panel and a new "Next Appt" column has been added to the report data columns. If the user selects "All patients" then no "Next Appt" column is added.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>New LOINC codes have been added to the ROR LAB SEARCH file (#798.9) to add patients to the HIV pending patient list</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>5</td>
<td>On the Combined Meds and Labs, DAA Lab Monitoring, Hepatitis A Vaccine or Immunity and Hepatitis B Vaccine or Immunity reports, it was discovered sorting on the ICN, PACT or PCP columns was not working. The reports have been updated to sort properly on the ICN, PACT or PCP columns.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>6</td>
<td>The version of the CCR software is updated to 1.5.33</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc165646491" class="anchor"></span>Table – Patch ROR\*1.5\*39 Description

#### Patch ROR\*1.5\*34

<table>
<caption><p><span id="_Toc165646492" class="anchor"></span>Table – Patch ROR*1.5*40 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create three new Local Registries; Lymphoma, Non-Alcoholic SteatoHepatitis (NASH) and Interstitial Lung Disease (ILD). The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><blockquote>
<p>HIV registry: COBICISTAT/DARUNAVIR/EMTRICITABINE/TENOFOVIR AF</p>
</blockquote></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>In the CCR GUI, the "Future Appointments" panel has been added to the following reports for all registries:</p>
<ul>
<li><blockquote>
<p>Diagnoses</p>
</blockquote></li>
<li><blockquote>
<p>Procedures</p>
</blockquote></li>
</ul>
<p>The panel has been added after the "Additional Identifiers" panel and the "Next Appt" column has been added to the report data columns. If the user selects "All patients" then no "Next Appt" column is added.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>On all reports where the "Future Appointments" panel is available, a new "Clinic Name" column has been added to the right of the "Next Appt" column in the report output. If the user selects "All patients" then no "Clinic Name" column is added.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>On the Hepatitis A and Hepatitis B reports, fixed the display on LOINC codes on the report header.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>6</td>
<td>On the Current Inpatient List report, an "Admission Date" column has been added to the left of the "Admitting Diagnosis" column on the report output.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>On the Hepatitis A and Hepatitis B reports, the tool tips on the Vaccination Date Range and Immunity Date Range panels have been fixed.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>8</td>
<td>The version of the CCR software is updated to 1.5.34</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc165646492" class="anchor"></span>Table – Patch ROR\*1.5\*40 Description

#### Patch ROR\*1.5\*35

<table>
<caption><p><span id="_Toc165646493" class="anchor"></span>Table – Patch ROR*1.5*41 Description</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create two new Local Registries; Head/Neck Squamous Cell Cancer and Hypothyroidism. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><blockquote>
<p>HIV registry: DORAVIRINE</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: DORAVIRINE /LAMIVUDINE/TENOFOVIR</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: DOLUTEGRAVIR/LAMIVUDINE</p>
</blockquote></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>The two national registries, Hepatitis C and HIV, will now auto-confirm patients like the rest of the registries. At the time of the patch installation, any pending patients will be confirmed setting the confirmation date to the patch installation date and any pending comments for those patients will be deleted.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>The CCR software now supports 2 factor authentication (2FA) and single sign on using the new RPC broker.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>The CCR help system has been completely re-designed to work with Windows 10.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>6</td>
<td>The version of the CCR software is updated to 1.5.35</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc165646493" class="anchor"></span>Table – Patch ROR\*1.5\*41 Description

#### Patch ROR\*1.5\*36

| \#  | Description                                                                                                                 |     | Type |
|-----|-----------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | Create a new Local Registry; COVID-19. The new local registry will be defined using ICD-10 codes.                           | E   |      |
| 2   | The Lab Tests tab of the Edit Site Parameters screen has been fixed to not display the Microsoft Window's control name.     | F   |      |
| 3   | The Registry Meds tab of the Edit Site Parameters screen has been fixed to not display the Microsoft Window's control name. | F   |      |
| 4   | The version of the CCR software is updated to 1.5.36                                                                        | E   |      |

<span id="_Ref534369003" class="anchor"></span>Table – Patch ROR\*1.5\*42 Description

#### Patch ROR\*1.5\*37

| \#  | Description                                                                                                                                                                                                                   |     | Type |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | Create new Local Registry; Recent Patients. The new local registry will be defined using patient admission and visit dates. It will contain only those patients who have been seen in the previous two years at the facility. | E   |      |
| 2   | The VA COVID19 registry which was added with the previous patch, ROR\*1.5\*36, is modified to check Lab tests for positive test results for certain LOINC values.                                                             | E   |      |
| 3   | The version of the CCR software is updated to 1.5.37                                                                                                                                                                          | E   |      |

<span id="_Ref233529382" class="anchor"></span>Table 40 – Software and Documentation Sources

#### Patch ROR\*1.5\*38

| \#  | Description                                                                                                                                                                                                                                                                                                                                                                                                            |     | Type |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | The Clinical Case Registries (CCR) identifies patients with positive antibody results for inclusion in the HIV and HCV registries. This patch fixes an error where patients with laboratory results that are not positive are incorrectly categorized as positive and are incorrectly included in the HIV and HCV registries. Code changes have been made to the RORUPD04 and RORX024A routines to rectify this issue. | F   |      |
| 2   | The version of the CCR software is updated to 1.5.38                                                                                                                                                                                                                                                                                                                                                                   | E   |      |

<span id="_Toc165646496" class="anchor"></span>Table 41 – Files Included in Distribution

#### Patch ROR\*1.5\*39

<table>
<caption><p><span id="_Toc165646497" class="anchor"></span>Table 42 – CCR Menu Options</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>The display of Social Security Numbers (SSNs) and the last 4 of the SSN has been removed from all screens and report output (see NOTE below).</p>
<p><strong>NOTE:</strong> In May 2007, Office of Management and Budget (OMB) issued memorandum M-07-16, Safeguarding Against and Responding to the Breach of Personally Identifiable Information, requiring agencies to review their use of Social Security Numbers (SSNs) and to explore alternatives to using SSNs as personal identifiers for Federal employees and in Federal programs.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>2</td>
<td>The version of the CCR software is updated to 1.5.39</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc165646497" class="anchor"></span>Table 42 – CCR Menu Options

#### Patch ROR\*1.5\*40

<table>
<caption><p><span id="_Ref255459987" class="anchor"></span>Table 45 – Files and Globals Exported with CCR</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following new medications:</p>
<ul>
<li><blockquote>
<p>HIV registry: CABOTEGRAVIR</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: CABOTEGRAVIR/RILPIVIRINE</p>
</blockquote></li>
</ul>
<p>The new medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>2</td>
<td>The version of the CCR software is updated to 1.5.40</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref255459987" class="anchor"></span>Table 45 – Files and Globals Exported with CCR

#### Patch ROR\*1.5\*41

<table>
<caption><p><span id="_Ref249959130" class="anchor"></span>Table 46 – CCR 1.5 Routine List</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch changes the value of the NATIONAL (#.09) field in the ROR REGISTRY PARAMETERS (#798.1) file for two entries:</p>
<ul>
<li><blockquote>
<p>Hepatitis C registry: VA HEPC</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: VA HIV</p>
</blockquote></li>
</ul>
<p>Before the patch, the value is "1" (i.e., YES).</p>
<p>After the patch, the value is "0" (i.e., NO).</p>
<p>Prior to this patch, these two registries were considered "national" and their patient data was transmitted to a national database every day. All other registries in the package are considered "local" and their patient data is not transmitted to any other database.</p>
<p>With this patch, these two registries are changed to "local" too and their patient data will no longer be transmitted to any other database.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>2</td>
<td>The version of the CCR software is updated to 1.5.41</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref249959130" class="anchor"></span>Table 46 – CCR 1.5 Routine List

#### Patch ROR\*1.5\*42

<table>
<caption><p><span id="_Toc165646502" class="anchor"></span>Table 47 – Routine Sub-Namespaces</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><blockquote>
<p>HIV registry: LENACAPAVIR</p>
</blockquote></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>2</td>
<td>The VA TRANSGENDER registry is inactivated. The REGISTRY STATUS field (#11) of the ROR REGISTRY PARAMETERS (#798.1) file for this registry is set to 1 (i.e., INACTIVE). The daily update process will no longer update this registry. Also, this registry will no longer appear in the list of registries displayed to the users so they will not be able to select it.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>3</td>
<td>The Graphical User Interface (GUI) now supports the latest changes to the RPC Broker package. The latest Personal Identity Verification (PIV) certificate will be selected automatically, however, a new "/showcerts" command line switch was added to allow the user to display the PIV certificate selection screen in case it is needed.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>The version of the CCR software is updated to 1.5.42</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc165646502" class="anchor"></span>Table 47 – Routine Sub-Namespaces

## Obtaining Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR software (ROR 1_5) and documentation files are available for downloading from the VistA download site listed in Table 40.

| Name            | Address                   | Directory |
|-----------------|---------------------------|-----------|
| VistA downloads | See CCR Redacted document | Software  |

<span id="_Toc165646503" class="anchor"></span>Table 48 – Exported Options

The CCR software and accompanying guides and manuals are distributed as the following set of files:

<table>
<caption><p><span id="_Ref233448983" class="anchor"></span>Table 49 – Event Protocols</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 57%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Contents</th>
<th>Retrieval Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR1_5.KID</td>
<td>CCR Initial version 1.5 build (usually needed only for initial build, as at a new site)</td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>ROR1_5P42GUI.ZIP</td>
<td><p>Zipped GUI distributive</p>
<p>► CCRSETUP.EXE</p></td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>ROR1_5P42DOC1.ZIP</td>
<td><p>Zipped DOC distributive, which includes both .PDF and .DOCX formats:</p>
<p>► User Manual (ROR1_5_42UM)</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>ROR1_5P42DOC2.ZIP</td>
<td><p>► Installation and Implementation Guide (ROR1_5_42IG)</p>
<p>► Technical Manual / Security Guide (ROR1_5_42TM)</p>
<p>► Release Notes (ROR1_5_42RN)</p></td>
<td>BINARY</td>
</tr>
</tbody>
</table>

<span id="_Ref233448983" class="anchor"></span>Table 49 – Event Protocols

## VistA Documentation on the Intranet 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this product, including all of the software manuals, is available in the VistA Document Library (VDL). The Clinical Case Registries documentation may be found at <http://www.va.gov/vdl/application.asp?appid=126>.

For additional information about the CCR, access the CCR Home Page at the following address: See CCR Redacted document.

Training links and information are also available in the CCR Redacted document.

## Accessibility Features in Clinical Case Registries 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Keyboard shortcuts make the CCR GUI accessible to a wide range of users, including those with limited dexterity, low vision, or other disabilities. See the *Clinical Case Registries User Manual* (available at <http://www.va.gov/vdl/application.asp?appid=126>) for a complete list of keyboard shortcuts. [^2]

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Case Registries Maintenance menu \[RORMNT MAIN\] has the following options which sites can use to customize and maintain their use of the software:

| Option | Description                      |
|--------|----------------------------------|
| ACL    | Re-index the ACL cross-reference |
| ELS    | Edit Lab Search Criteria         |
| ERP    | Edit Registry Parameters         |
| HDE    | Historical Data Extraction       |
| PLF    | Print Log Files                  |
| PP     | Pending Patients                 |

<span id="_Toc165646505" class="anchor"></span>Table 50 – Application Program Interfaces

### Re-index the ACL cross-reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-technical-manual-security-guide/013.png) | Note: Effective with Patch ROR\*1.5\*18, the ACL Re-Index is no longer required. |     |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|-----|

<span id="_Toc165646506" class="anchor"></span>Table 51 – Prerequisite Patches

The ACL cross-reference of the ROR REGISTRY PARAMETERS file (#798.1) should be rebuilt after changes in the allocation of the security keys associated with any registry. Usually, this is done by the nightly task (the Registry Update & Data Extraction \[ROR TASK\] option). However, if you want the changes to take effect immediately, you can rebuild this cross-reference manually:

<span id="_Toc162942898" class="anchor"></span>Figure – Re-index the ACL Cross-reference

![](ror-1-5-42-technical-manual-security-guide/014.png)

### Edit Lab Search Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to enter the Lab Search criteria used by the registry update process. The criteria are updated via CCR patches and should not be edited without approval from Population Health Service and Product Support (PS).

<span id="_Toc162942899" class="anchor"></span>Figure – Edit Lab Search Criteria

![](ror-1-5-42-technical-manual-security-guide/015.png)

Each criterion includes one or more *triads* that consist of LOINC CODE, INDICATOR, and an optional INDICATED VALUE. The indicator defines the comparison operation applied to the Lab result. The Lab result is compared to the value of the INDICATED VALUE parameter. For example, if the internal value of this field is equal to 3 ("Greater Than") and the value of the INDICATED VALUE field is 5, then this indicator will be evaluated as True for all numeric Lab results values greater than 5.

The only exceptions are the Use Reference Range and Positive Result indicators; they ignore the value.

The Use Reference Range indicator checks to see if the result value is outside of the reference range defined for the Lab test.

For example, the POSITIVE, POS, REACT, and The Positive Result indicator selects a test result if the value…

- is equal to P

> or

- contains POS, DETEC or REA *and* does not contain NEG, NO,UNDET or IND.

DETECTABLE values will be picked up. At the same time, the NON-REACT, INDETERMINATE, and NEG values will be skipped.

> ![](ror-1-5-42-technical-manual-security-guide/016.png)Note: All string comparisons are case-insensitive.

The STATUS field allows users to temporarily inactivate the whole lab search criterion.

### Edit Registry Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to review/edit the registry parameters. These values can alter the way the system works on a site-by-site basis.

<span id="_Toc162942900" class="anchor"></span>Figure – Edit Registry Parameters

![](ror-1-5-42-technical-manual-security-guide/017.png)

This option is typically run during the implementation phase to enter Notifications and Log Event Types. All other parameters are set during the package installation and should not be edited without approval from PS or package developers.

- The REGISTRY UPDATED UNTIL and DATA EXTRACTED UNTIL parameters are initialized during the package installation; they will be subsequently updated by the nightly task. These fields should only be edited in situations such as a system failure.
- The EXTRACT PERIOD FOR NEW PATIENT parameter defines the number of days subtracted from the date a new patient first selection rule was passed that the extract process uses when extracting data. The value of this parameter for national registries cannot be changed by the users.
- The ENABLE LOG field allows you to turn the CCR log on or off. The log stores messages generated by different CCR processes (mostly, by the nightly task).
- The LOG EVENT multiple allows the system to monitor the registry on various levels. If this field is left empty (default), all events except debug messages are recorded in the log file. If the multiple contains one or more records, only events specified by these records and error messages will be recorded. Possible event types are:
  - Debug
  - Information
  - Data Quality
  - Warning
  - Database Error
  - Error

> Debug messages are intended for registry troubleshooting. These messages are exclusions from the above rule; they are not logged if ENABLE LOG is set to "Yes" and the LOG EVENT multiple is empty. Their recording can only be explicitly enabled.

> Information messages can be used as formatting elements (headers, trailers, separators, etc.) and as a source of additional information that may be helpful in the troubleshooting process.

> Data Quality messages indicate possible issues with the data in the FileMan files, such as missing or invalid values, ambiguous data, etc.

> Database Error messages most of these error messages are generated by the FileMan DBS calls. Usually, these messages indicate serious problems with the database. Database errors are recorded regardless of content of the LOG EVENT multiple.

> Error messages indicate fatal problems during the execution. Usually, processing of the patient data (or even the registry as a whole) stops after these errors. Errors are recorded regardless of content of the LOG EVENT multiple.

> You may enter a new LOG EVENT, if you wish select the type of event and if you want to enable recording of these events. If the list is empty, recording of all events is enabled. Otherwise, only events from the list and error messages will be recorded.

If you need to temporarily exclude the registry from the registry updates and data extractions, set the REGISTRY STATUS parameter to INACTIVE (1).

- Users referenced by the NOTIFICATION multiple receive VistA alerts about problems with the CCR software (such as data transmission problems).
- Value of the LAG DAYS parameter defines an overlap of the data searches during the registry updates and a data extraction delay during the regular data extractions. See the Technical Description of the field in the data dictionary for more information.
- Value of the ALERT FREQUENCY parameter determines how often e-mail notifications and VistA alerts are sent to the CDCO and local staff in case of problems with the site's CCR software (data extraction problems, unsent HL7 messages, etc.). For example, if the nightly task runs every night and the ALERT FREQUENCY is 2, then alerts and notifications will be sent every other night.
- If the ENABLE PROTOCOLS parameter is set to "Yes" (default), event protocols will be used by the package to speed up the registry processing. The protocols create references to the patient events in the ROR PATIENT EVENTS file (#798.3). Only those patients that have new references will be processed by the next registry update.

> ![](ror-1-5-42-technical-manual-security-guide/018.png)Note: If several registries are updated at the same time and at least one of them has this field set to "Yes", all these registries will be processed using event references.

- The MAXIMUM MESSAGE SIZE parameter defines the maximum size (in megabytes) of a batch HL7 message that can be sent to the CDCO. If this field is empty or contains 0, the size is not limited.

> ![](ror-1-5-42-technical-manual-security-guide/019.png)Note: You must coordinate your intentions with CDCO support personnel if you are going to edit this field.

### Historical Data Extraction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the Historical Data Extraction menu. See the Manual Historical Data Extraction section below for details.

<span id="_Toc162942901" class="anchor"></span>Figure – Historical Data Extraction

![](ror-1-5-42-technical-manual-security-guide/020.png)

### Print Log Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to print the CCR log files. It provides a history of all events that have occurred within the provided time frame.

<span id="_Toc162942902" class="anchor"></span>Figure – Print Log Files

![](ror-1-5-42-technical-manual-security-guide/021.png)

| ![](ror-1-5-42-technical-manual-security-guide/022.png) | Note: Logs that are older than 31 days are automatically purged by the nightly task. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|

<span id="_Ref335317845" class="anchor"></span>Table 52 – Database Integration Agreements

### Pending Patients 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you select this option, you are offered the List of Pending Errors option. This option lists all patients whose data caused errors during the Registry Update process.

The option prints a report containing a list of patients referenced by the ERROR multiples of the ROR PATIENT EVENTS file (#798.3). The list is sorted by the value of the COUNTER field. This field indicates how many times an error was recorded for the patient.

<span id="_Toc162942903" class="anchor"></span>Figure – Pending Patients

![](ror-1-5-42-technical-manual-security-guide/023.png)

This report can be used to find patients ignored by the registry update (until someone fixes the error(s) and resets value of the COUNTER field to 1).

## Manual Historical Data Extraction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If it is necessary to re-extract a large amount of registry data in the specified date range due to new data elements, problems in the data extraction code, etc., then the manual historical data extraction should be used.

The historical data extraction process runs independent of the nightly task. It gathers historical data for each registry patient and writes it to the host operating system files in HL7 format. Several menu options are provided to initiate and control the process.

Any data errors found will be reported on a log file, and the job will continue on to the next patient on the registry to get historical data. You can check the status of the run using the user interface. The user interface shows when the job is completed and indicates if any data errors were found.

After errors are fixed, the job can be re-run. This second run goes through all patients having errors during the first run and automatically creates an additional file. This process continues until the interface indicates that all patients are processed. After all patients have data extracted successfully, you can transmit all files created by this process to the national database using FTP or any other means.

### Historical Data Extraction Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Manual historical data extraction menu options are accessible from the Historical Data Extraction \[RORHDT MAIN\] menu:

<span id="_Toc162942904" class="anchor"></span>Figure – Historical Data Extraction Menu

![](ror-1-5-42-technical-manual-security-guide/024.png)

DS – Display Extraction Status

This option displays the status of a selected data extraction. The historical data extraction start and end dates, the output directory name, processed registries, and task table are displayed.

ED – Edit …

This option offers two more edit options when selected:

CT – Create Extraction Tasks

This option spreads historical data processing over several tasks in order to speed up the process.

EE – Edit Data Extraction

This option allows users to edit parameters of a manual historical data extraction in the ROR HISTORICAL DATA EXTRACTION file (#799.6).

ST – Start a Task

This option starts a data extraction task that was created with the Create Extraction Tasks option.

TT – Stop a Task

This option allows you to stop a running task and de-queue a scheduled task. The task can be restarted later. In that case, it will try to re-extract data that was not extracted during the previous runs due to errors. Then it will continue the extraction from the first unprocessed record from the group of patients defined for the task.

DL – Display Task Log

This option lets users see a log of any running/finished data extraction task. If any errors have been found, they will be logged here. Any errors should be fixed and then the task re-started.

### Data Extraction Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the steps below to perform the historical data extraction:

1.  Create the output directory.  
    Historical data extraction tasks create files containing historical data for registry patients. The host file system directory for these files must be created and defined in the parameters of the historical data extraction before the extraction tasks are run.  
      
    In VMS, create the directory as follows:

<span id="_Toc162942905" class="anchor"></span>Figure – Create the Output Directory

2.  ![](ror-1-5-42-technical-manual-security-guide/025.png)  
    Replace the *{VistA}* in the SET command with the VMS username (or UIC) associated with the VistA TaskMan processes.  
      
    ![](ror-1-5-42-technical-manual-security-guide/026.png)Note: See Appendix A for instructions on creating the output directory in a Windows environment.
3.  Define the name of the output directory in the data extraction parameters.  
    Use the Edit data extraction \[RORHDT EDIT EXTRACTION\] option to populate the historical data extraction parameters with the name of the output directory:

<span id="_Toc162942906" class="anchor"></span>Figure – Define Output Directory Name in Data Extraction Parameters

![](ror-1-5-42-technical-manual-security-guide/027.png)

4.  Create the data extraction task(s).  
    Use the Create Extraction Tasks \[RORHDT CREATE\] option to define the data extraction tasks:

<span id="_Toc162942907" class="anchor"></span>Figure – Create Data Extraction Task

![](ror-1-5-42-technical-manual-security-guide/028.png)

5.  Start the data extraction task(s).  
    Use the Start a Task \[RORHDT START\] option to start the data extraction task(s). The user can select a task using a value from the "ID" column:

<span id="_Toc162942908" class="anchor"></span>Figure – Start Data Extraction Task

![](ror-1-5-42-technical-manual-security-guide/029.png)  
It is not necessary to wait until the previous task finishes before scheduling the next one. You can schedule several tasks at the same time. Make sure that the system has enough resources for this and there will be no negative impact on the response time during business hours.

5\. Wait for task(s) completion.

The person who schedules the data extraction tasks will receive VistA alerts when they are complete (one alert per task).  
  
Meanwhile, you can use the Display Task Log \[RORHDT LOG\] option to display the data extraction status of a selected registry. The task log includes historical data extraction start and end dates, the output directory name, affected registries, and the task table.  
  
Table 43 shows the information displayed for each task in the table:  
<span id="_Ref232396862" class="anchor"></span>Table 43 – Task Information

| Task      | Description                                                                                                                                                                                |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID        | Internal Entry Number of the task (IEN).                                                                                                                                                   |
| File Name | A unique name based on site name and sequential number of the task. This file will contain the extracted results when the task has run; it will reside in the designated output directory. |
| Task      | Task number assigned by TaskMan to the data extraction task                                                                                                                                |
| Status    | Status of the data extraction task                                                                                                                                                         |

<span id="_Toc165646508" class="anchor"></span>Table 53 – Typographic Conventions (Segment Definitions)

The eight Status values are shown in Table 44.  
  
<span id="_Ref232396822" class="anchor"></span>Table 44 – Status Values

| Status                | Meaning                                                                             |
|-----------------------|-------------------------------------------------------------------------------------|
| Active: Pending       | Task is scheduled but is not currently running                                      |
| Active: Running       | Task is currently running                                                           |
| Active: Stopping      | Task was requested to stop but has not responded yet                                |
| Inactive: Finished    | Task has finished successfully                                                      |
| Inactive: Available   | Task was created without being scheduled or was edited without being rescheduled    |
| Inactive: Interrupted | Task was stopped by a user                                                          |
| Inactive: Crashed     | Task has stopped running due to a crash                                             |
| Inactive: Errors      | Task has completed but some patient data was not processed completely due to errors |

<span id="_Toc165646509" class="anchor"></span>Table 54 – HL7 Abbreviated Column Headings

In the example below, one of the tasks has the status of Inactive: Errors.

<span id="_Toc162942909" class="anchor"></span>Figure – Display Extraction Status

![](ror-1-5-42-technical-manual-security-guide/030.png)  
If you need to stop a task (*e.g.* due to a slow system response), use the Stop a Task \[RORHDT STOP\] option. You will be prompted to select a data extraction, and then the task table and task selection prompt will display.  
  
The system displays the De-queue the task? prompt (if the task is already running, the Stop the task? prompt displays instead). If NO is entered, no changes are made to the selected task. If YES is selected, the task is de-queued (or stopped).

<span id="_Toc162942910" class="anchor"></span>Figure – Stop a Task

![](ror-1-5-42-technical-manual-security-guide/031.png)

6.  Examine the task log(s).  
    If one or more data extraction tasks with problems are identified at the previous step, use the Display Task Log \[RORHDT LOG\] menu option to examine the logs of those tasks. You are prompted to select a data extraction, and then the task table and task selection prompt displays.

<span id="_Toc162942911" class="anchor"></span>Figure – Display Task Log

7.  ![](ror-1-5-42-technical-manual-security-guide/032.png)  
    In addition to the warnings and error messages, a task log also shows the date and time that the task was started and when it finished, how many patients were processed, the amount of errors that were encountered, the time (in seconds) that the task took to complete, and the average processing rate (patients per second).
8.  If there are errors, fix them and restart the tasks with errors.  
    After fixing the errors, restart the task(s) that had errors using the Start a Task \[RORHDT START\] option. This creates new files containing only the data for those patients who had errors during the previous run.  
      
    As shown in the example below, the rescheduling dialog is slightly different from that described in step 4:

<span id="_Toc162942912" class="anchor"></span>Figure – Start a Task

9.  ![](ror-1-5-42-technical-manual-security-guide/033.png)  
      
    If you decide to begin the historical data extraction process from scratch, first delete all historical data files from the output directory, then recreate the task table as shown below, and then return to step 4.

<span id="_Toc162942913" class="anchor"></span>Figure – Create Extraction Tasks

![](ror-1-5-42-technical-manual-security-guide/034.png)  
  
The only difference from the step 3 is the additional Overwrite the existing task table? prompt. Answer YES to that question.

### Data Transmission Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Background Information

You should transfer the historical data files to the national database via FTP. If the files were created in VMS, you can use the VMS FTP client. If you are using a Windows server, use either a command line or GUI client.

> ![](ror-1-5-42-technical-manual-security-guide/035.png) Note: Historical data files *must* be transmitted in binary mode.

#### Data Transmission Instruction

Follow the steps below to transmit the data using the VMS FTP (see the VMS documentation and/or online help for more details):

1.  Obtain the IP address, user name, and password for the FTP account.
2.  Enter the FTP command with the IP address as a parameter.
3.  Wait for the "Name (…):" prompt and enter your user name.
4.  Wait for the "Password:" prompt, and then enter your password (the characters of the password do not display on the screen).
5.  Change the transfer mode to binary using the SET TYPE IMAGE command.
6.  Send the historical data files (\*.HDT) from the output directory using the PUT command:  
    > FTP\> PUT *{disk and directory name}*\*.HDT
7.  Wait until the transfer is complete, and then verify that all files have uploaded successfully.
8.  Disconnect and exit the FTP client using the EXIT command.

The screen capture below shows a typical VMS FTP session:

<span id="_Toc162942914" class="anchor"></span>Figure – Typical VMS FTP Session

![](ror-1-5-42-technical-manual-security-guide/036.png)

![](ror-1-5-42-technical-manual-security-guide/037.png)Note: For information on using the Windows FTP client, see [Appendix B](#App_B).

# CCR Structure and Process Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCR consists of several parts:

- Data stored in VistA database files
- [M](#Glos_M) Programs in the ROR namespace
- [Data Dictionaries](#Glos_DD) necessary to achieve the specified requirements
- A [Delphi](#Glos_Delphi)-based [graphical user interface](#Glos_GUI) (GUI) "front-end" application
- Relevant [Remote Procedure Call](#Glos_RPC) (RPC) protocols

![](ror-1-5-42-technical-manual-security-guide/038.png)

![](ror-1-5-42-technical-manual-security-guide/039.png)

# CCR Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Files and Globals List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files and globals are exported with the CCR software:

<table>
<caption><p><span id="_Toc165646510" class="anchor"></span>Table 55 – HL7 Data Types</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 25%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>File Number</th>
<th>File Name</th>
<th>Global Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>798</strong></td>
<td><strong>ROR REGISTRY RECORD</strong></td>
<td><strong>^RORDATA(798,</strong></td>
<td>The ROR REGISTRY RECORD file contains records of local registries. Each record associates a patient with a registry and contains registry-specific and additional service information.</td>
</tr>
<tr class="even">
<td><strong>798.1</strong></td>
<td><strong>ROR REGISTRY PARAMETERS</strong></td>
<td><strong>^ROR(798.1,</strong></td>
<td>Records of the ROR REGISTRY PARAMETERS file contain various registry parameters and the data that indicates current registry state. Every registry must have a record in this file.</td>
</tr>
<tr class="odd">
<td><strong>798.2</strong></td>
<td><strong>ROR SELECTION RULE</strong></td>
<td><strong>^ROR(798.2,</strong></td>
<td>The ROR SELECTION RULE file contains definitions of the selection rules that are used to screen patients for addition to the registries.</td>
</tr>
<tr class="even">
<td><strong>798.3</strong></td>
<td><strong>ROR PATIENT EVENTS</strong></td>
<td><strong>^RORDATA(798.3,</strong></td>
<td><p>The ROR PATIENT EVENTS file is used to store references to those patients that were processed with errors and were not added to the registry, even if they potentially should have been added (see the ERROR multiple).</p>
<p>Moreover, the data references generated by the event protocols are stored in this file (see the EVENT multiple). These references are used to speed up the regular registry updates.</p></td>
</tr>
<tr class="odd">
<td><strong>798.4</strong></td>
<td><strong>ROR PATIENT</strong></td>
<td><strong>^RORDATA(798.4,</strong></td>
<td><p>The ROR PATIENT file contains patient information that is common for all local registries (mostly, demographic information).</p>
<p>Demographic data from this file is compared to that from the PATIENT file (#2) to determine if it has been changed since the last registry data extraction. These fields are updated with the values from the PATIENT file and the UPDATE DEMOGRAPHICS flag is set to "Yes" in all active registry records of the patient.</p></td>
</tr>
<tr class="even">
<td><strong>798.5</strong></td>
<td><strong>ROR ICD SEARCH</strong></td>
<td><strong>^ROR(798.5,</strong></td>
<td>This file stores all the ICD diagnostic codes used to identify patients for a given registry during the Registry Update process. The B cross reference for the ICD code is used in the EXPRESSION field of the ROR SELECTION RULES file (#798.2). The file design allows CCR to support an unlimited number of codes selected from the ICD DIAGNOSIS file (#80).</td>
</tr>
<tr class="odd">
<td><strong>798.6</strong></td>
<td><strong>ROR PHARMACY CODE</strong></td>
<td><strong>^ROR(798.6,</strong></td>
<td>This file contains a list of pointers to the VA DRUG CLASS file (#50.605). Within the Pharmacy package each class is linked to a group of medications. Each class on this file has an associated registry; the "AC" cross-reference groups all entries by registry.</td>
</tr>
<tr class="even">
<td><strong>798.7</strong></td>
<td><strong>ROR LOG</strong></td>
<td><strong>^RORDATA(798.7,</strong></td>
<td>The ROR LOG file is used for recording different kinds of events (errors, debug messages, etc.) that are generated by the CCR software.</td>
</tr>
<tr class="odd">
<td><strong>798.8</strong></td>
<td><strong>ROR TASK</strong></td>
<td><strong>^RORDATA(798.8,</strong></td>
<td>The ROR TASK file enhances the functionality of TaskMan and supports the package APIs used by the GUI to schedule and control the tasks, and view and print the reports.</td>
</tr>
<tr class="even">
<td><strong>798.9</strong></td>
<td><strong>ROR LAB SEARCH</strong></td>
<td><strong>^ROR(798.9,</strong></td>
<td><p>Lab search criteria are stored in this file. These criteria are referenced by the selection rules and used in the search for Lab results.</p>
<p><em>Update by (11): LOINC value 57006 is added to the VA HEPC Lab Search criteria in sub-file LAB TEST (#2).</em></p></td>
</tr>
<tr class="odd">
<td><strong>799.1</strong></td>
<td><strong>ROR LIST ITEM</strong></td>
<td><strong>^ROR(799.1,</strong></td>
<td>This file contains code sets used within different registries.</td>
</tr>
<tr class="even">
<td><strong>799.2</strong></td>
<td><strong>ROR METADATA</strong></td>
<td><strong>^ROR(799.2,</strong></td>
<td>The ROR METADATA file contains descriptors of the files, data elements and APIs used by the registry update subsystem (search engine). These descriptors define relationships between files ("file-processing tree") used by the search engine, data elements, and APIs.</td>
</tr>
<tr class="odd">
<td><strong>799.31</strong></td>
<td><strong>ROR XML ITEM</strong></td>
<td><strong>^ROR(799.31,</strong></td>
<td>The ROR XML ITEM file contains a list of XML tags and attributes that can be used in the reports.</td>
</tr>
<tr class="even">
<td><strong>799.33</strong></td>
<td><strong>ROR DATA AREA</strong></td>
<td><strong>^ROR(799.33,</strong></td>
<td>The ROR DATA AREA stores codes and names of the data areas referenced by the DATA AREA (the ROR HISTORICAL DATA EXTRACTION file) and the EVENT (the ROR PATIENT EVENTS file) multiples.</td>
</tr>
<tr class="odd">
<td><strong>799.34</strong></td>
<td><strong>ROR REPORT PARAMETERS</strong></td>
<td><strong>^ROR(799.34,</strong></td>
<td>The ROR REPORT PARAMETERS file stores the report definitions that are used by the ROR REPORT SCHEDULE remote procedure to schedule the reports.</td>
</tr>
<tr class="even">
<td><strong>799.4</strong></td>
<td><strong>ROR HIV RECORD</strong></td>
<td><strong>^RORDATA(799.4,</strong></td>
<td>The ROR HIV RECORD file stores the patients' data specific to the Human Immunodeficiency Virus Registry (CCR:HIV).</td>
</tr>
<tr class="odd">
<td><strong>799.49</strong></td>
<td><strong>ROR AIDS INDICATOR DISEASE</strong></td>
<td><strong>^ROR(799.49,</strong></td>
<td>The ROR AIDS INDICATOR DISEASE file contains definitions of the AIDS indicator diseases referenced by Part VIII of the HIV CDC form.</td>
</tr>
<tr class="even">
<td><strong>799.51</strong></td>
<td><strong>ROR GENERIC DRUG</strong></td>
<td><strong>^ROR(799.51,</strong></td>
<td>This file contains a list of registry specific generic drugs.</td>
</tr>
<tr class="odd">
<td><strong>799.53</strong></td>
<td><strong>ROR LOCAL FIELD</strong></td>
<td><strong>^ROR(799.53,</strong></td>
<td>The ROR LOCAL FIELD file stores definitions of local registry-specific fields created at the site.</td>
</tr>
<tr class="even">
<td><strong>799.6</strong></td>
<td><strong>ROR HISTORICAL DATA EXTRACTION</strong></td>
<td><strong>^RORDATA(799.6,</strong></td>
<td>Records of this file store parameters of the historical data extractions (backpulls) performed on the registries and reflect status of these data extractions.</td>
</tr>
</tbody>
</table>

<span id="_Toc165646510" class="anchor"></span>Table 55 – HL7 Data Types

## File Diagrams (Pointers)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc162942915" class="anchor"></span>Figure – Pointer Matrix Legend

![](ror-1-5-42-technical-manual-security-guide/040.png)

<span id="_Toc162942916" class="anchor"></span>Figure – File Pointers

![](ror-1-5-42-technical-manual-security-guide/041.png)

<span id="_Toc162942917" class="anchor"></span>Figure – File Pointers

<table>
<caption><p><span id="_Toc165646511" class="anchor"></span>Table 56 – Diagnostic Service Section ID (HL7 Table 0074)</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 11%" />
<col style="width: 3%" />
<col style="width: 2%" />
<col style="width: 22%" />
<col style="width: 2%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name (File #)</th>
<th colspan="2" rowspan="2">Type*</th>
<th colspan="2">File Name (File #)</th>
<th colspan="2" rowspan="2">File Pointed To</th>
</tr>
<tr class="odd">
<th>Pointer Field</th>
<th colspan="2">Pointer Field</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR HIV RECORD (#799.4)</td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REGISTRY RECORD ...........</p>
</blockquote></td>
<td>(N C )</td>
<td></td>
<td colspan="2"><strong>798</strong> ROR REGISTRY *</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td>PATIENT NAME</td>
<td></td>
<td>ROR PATIENT</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>REGISTRY</td>
<td></td>
<td>ROR REGISTRY PARAM*</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td>CONFIRMED BY</td>
<td></td>
<td>NEW PERSON</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>DELETED BY</td>
<td></td>
<td>NEW PERSON</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>m</td>
<td>SELECTI:SELECTI*</td>
<td></td>
<td>ROR SELECTION RULE</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>SELECTI:LOCATIO*</td>
<td></td>
<td>INSTITUTION</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>m</td>
<td>LOCAL F:LOCAL F*</td>
<td></td>
<td>ROR LOCAL FIELD</td>
</tr>
<tr class="even">
<td>ROR REGISTRY RECORD (#798)</td>
<td></td>
<td></td>
<td></td>
<td><strong>798.1</strong> ROR REGISTR*</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REGISTRY ..................</p>
</blockquote></td>
<td>(N C )</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ROR PATIENT EVENTS (#798.31)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ERROR:REGISTRY ............</p>
</blockquote></td>
<td>(N )</td>
<td></td>
<td></td>
<td>PROTOCOL</td>
<td></td>
<td>PROTOCOL</td>
</tr>
<tr class="even">
<td>ROR PHARMACY CODE (#798.6)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REGISTRY ..................</p>
</blockquote></td>
<td>(N C )</td>
<td></td>
<td></td>
<td>AUTOMATIC BACKPU</td>
<td></td>
<td>ROR HISTORICAL DAT*</td>
</tr>
<tr class="even">
<td>ROR LOG (#798.73)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REGISTRY ..................</p>
</blockquote></td>
<td>(N )</td>
<td></td>
<td>m</td>
<td>NOTIFIC:NOTIFIC*</td>
<td></td>
<td>NEW PERSON</td>
</tr>
<tr class="even">
<td>ROR TASK (#798.8)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>REGISTRY ..................</td>
<td>(N C )</td>
<td></td>
<td>m</td>
<td>REPORT :REPORT *</td>
<td></td>
<td>ROR REPORT PARAMET*</td>
</tr>
<tr class="even">
<td>ROR LIST ITEM (#799.1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>REGISTRY ..................</td>
<td>(N )</td>
<td></td>
<td>m</td>
<td>LOCAL T:LOCAL T*</td>
<td></td>
<td>LABORATORY TEST</td>
</tr>
<tr class="even">
<td>ROR GENERIC DRUG (#799.51)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>REGISTRY ..................</td>
<td>(N )</td>
<td></td>
<td></td>
<td>LOCAL T:LAB GRO*</td>
<td></td>
<td>ROR LIST ITEM</td>
</tr>
<tr class="even">
<td>ROR LOCAL FIELD (#799.53)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>REGISTRY ..................</td>
<td>(N )</td>
<td></td>
<td>m</td>
<td>LOCAL D:LOCAL D*</td>
<td></td>
<td>DRUG</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>LOCAL D:DRUG GR*</td>
<td></td>
<td>ROR LIST ITEM</td>
</tr>
<tr class="odd">
<td>ROR REGISTRY RECORD (#798.01)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>SELECTION RULE ............</td>
<td>(N )</td>
<td></td>
<td></td>
<td>798.2 ROR SELECT*</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td>798.3 ROR PATIENT*</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>PATIENT NAME</td>
<td></td>
<td>PATIENT</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>m</td>
<td>ERROR:REGISTRY</td>
<td></td>
<td>ROR REGISTRY PARAM*</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>EVENT:DATA AREA</td>
<td></td>
<td>ROR DATA AREA</td>
</tr>
<tr class="odd">
<td>ROR REGISTRY RECORD (#798)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PATIENT NAME ..............</td>
<td>(N C L )</td>
<td></td>
<td></td>
<td>798.4 ROR PATIENT</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR HISTORICAL DATA (#799.641)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>TASK:ERROR ................</td>
<td>(N C L )</td>
<td></td>
<td></td>
<td>PATIENT NAME</td>
<td></td>
<td>PATIENT</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td>PERIOD OF SERVICE</td>
<td></td>
<td>PERIOD OF SERVICE</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>m</td>
<td><p>798.5 ROR ICD SEARCH</p>
<p>ICD CODE:ICD CODE</p></td>
<td></td>
<td>ICD DIAGNOSIS</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td>798.6 ROR PHARMAC*</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>DRUG CLASS</td>
<td></td>
<td>VA DRUG CLASS</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td>REGISTRY</td>
<td></td>
<td>ROR REGISTRY PARAM*</td>
</tr>
<tr class="even">
<td>ROR TASK (#798.8)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LOG .......................</td>
<td>(N C )</td>
<td></td>
<td></td>
<td>798.7 ROR LOG</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>USER</td>
<td></td>
<td>NEW PERSON</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>m</td>
<td>REGISTRY:REGISTRY</td>
<td></td>
<td>ROR REGISTRY PARAM*</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>MESSAGE:PATIENT</td>
<td></td>
<td>PATIENT</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>798.8</strong> ROR TASK</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>REGISTRY</strong></td>
<td></td>
<td>ROR REGISTRY PARAM*</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>REPORT</strong></td>
<td></td>
<td>ROR REPORT PARAMET*</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>USER</strong></td>
<td></td>
<td>NEW PERSON</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>LOG</strong></td>
<td></td>
<td>ROR LOG</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>m</td>
<td><strong>REPORT :REPORT *</strong></td>
<td></td>
<td>ROR XML ITEM</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>m</td>
<td><strong>REPO:ATTR:ATTR*</strong></td>
<td></td>
<td>ROR XML ITEM</td>
</tr>
<tr class="even">
<td>ROR REGISTRY PARAMET (#798.128)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LOCAL TEST NAME:LAB GROUP .</td>
<td>(N )</td>
<td></td>
<td></td>
<td><strong>799.1 ROR LIST IT*</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>LOCAL DRUG NAME:DRUG GROUP</td>
<td>(N )</td>
<td></td>
<td></td>
<td><strong>REGISTRY</strong></td>
<td></td>
<td>ROR REGISTRY PARAM*</td>
</tr>
<tr class="odd">
<td>ROR GENERIC DRUG 9#799.51)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>DRUG GROUP ................</td>
<td>(N )</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR METADATA (#799.2)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PARENT ....................</td>
<td>(N )</td>
<td></td>
<td></td>
<td><strong>799.2</strong> ROR METADATA</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>PARENT</strong></td>
<td></td>
<td>ROR METADATA</td>
</tr>
<tr class="even">
<td>ROR TASK (#798.87)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>REPORT ELEMENT ............</td>
<td>(N )</td>
<td></td>
<td></td>
<td><strong>799.31</strong> ROR XML IT*</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>REPORT ELEMENT:ATTRIBUTE ..</td>
<td>(N C )</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR PATIENT EVENTS (#798.32)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>EVENT:DATA AREA ...........</td>
<td>(N )</td>
<td></td>
<td></td>
<td><strong>799.33</strong> ROR DATA A*</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR HISTORICAL DATA (#799.61)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>DATA AREA .................</td>
<td>(N )</td>
<td></td>
<td></td>
<td><strong>799.34</strong> ROR REPORT*</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR REGISTRY PARAMET (#798.12)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>REPORT STATS ..............</td>
<td>(N )</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ROR TASK (#798.8)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>REPORT ....................</td>
<td>(N )</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>799.4</strong> ROR HIV REC*</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>REGISTRY RECORD</td>
<td></td>
<td>ROR REGISTRY RECORD</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>STATION</strong></td>
<td></td>
<td>INSTITUTION</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>CDC FORM COMPLET*</strong></td>
<td></td>
<td>NEW PERSON</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>ONSET OF ILLNESS*</strong></td>
<td></td>
<td>STATE</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>AIDS DX – STATE</strong></td>
<td></td>
<td>STATE</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>m</td>
<td><strong>AIDS IN:AIDS IN*</strong></td>
<td></td>
<td>ROR AIDS INDICATOR*</td>
</tr>
<tr class="even">
<td>ROR HIV RECORD (#799.41)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>AIDS INDICATOR DISEASE ....</td>
<td>(N )</td>
<td></td>
<td></td>
<td><strong>799.49</strong> ROR AIDS I*</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>799.51</strong> ROR GENERI*</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>REGISTRY</strong></td>
<td></td>
<td>ROR REGISTRY PARAM*</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>DRUG GROUP</strong></td>
<td></td>
<td>ROR LIST ITEM</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>VA GENERIC</strong></td>
<td></td>
<td>VA GENERIC</td>
</tr>
<tr class="even">
<td>ROR REGISTRY RECORD (#798.02)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LOCAL FIELD ...............</td>
<td>(N C )</td>
<td></td>
<td></td>
<td><strong>799.53</strong> ROR LOCAL *</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>REGISTRY</strong></td>
<td></td>
<td>ROR REGISTRY PARAM*</td>
</tr>
<tr class="odd">
<td>ROR REGISTRY PARAMET (#798.1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>AUTOMATIC BACKPULL ........</td>
<td>(N )</td>
<td></td>
<td></td>
<td><strong>799.6</strong> ROR HISTORI</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>m</td>
<td>DATA AR:DATA AR*</td>
<td></td>
<td>ROR DATA AREA</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>m</td>
<td>TASK:ERROR:ERROR</td>
<td></td>
<td>ROR PATIENT</td>
</tr>
</tbody>
</table>

<span id="_Toc165646511" class="anchor"></span>Table 56 – Diagnostic Service Section ID (HL7 Table 0074)

<span id="_Toc162942918" class="anchor"></span>Figure – Pointers

![](ror-1-5-42-technical-manual-security-guide/042.png)

# Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Upgrade Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new globals are exported/allocated by the ROR 1.5 build if you install it an account that already has CCR v1.0 installed.

## Initial Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new globals are created during an initial installation of the KIDS build ROR 1.5: ^ROR and ^RORDATA.

The ^ROR global is quite small and mostly static. It contains the registry parameters, selection rules, Lab search definitions, etc.

The ^RORDATA global is a dynamic global and under most circumstances will be large. It will contain the registries, error logs, list of the event references, reports, etc. The sustained growth of ^RORDATA depends on the number of new patients in the registries (about 200 bytes per patient).

In the first couple of weeks, however, the global will grow faster because of the error logs (the ROR LOG file) and event references (the EVENT multiple of the ROR PATIENT EVENTS file). Both files are self-maintained and the nightly task (the Registry Update & Data Extraction \[ROR TASK\] option) purges the old records from these files automatically. The initial growth of these files depends on activity level (number of events) and quality of the data (number of error messages stored in the logs) at your site.

## Temporary Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR package uses the ^TMP and ^XTMP globals quite intensively, especially during the initial registry population. Please make sure that these globals are allocated in the database with enough free space.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routine List for CCR 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The [M](#Glos_M) routines listed in Table 46 are included in KIDS build ROR 1.5. The second line of each of these routines now looks like:

;;1.5;CLINICAL CASE REGISTRIES;\*\*\[Patch List\]\*\*;Feb 17, 2006;Build \[nn\]

The following M routines are included in CCR 1.5. Entries shaded in <span class="mark">yellow</span> were created/changed by Patch ROR\*1.5\*42.

| ![](ror-1-5-42-technical-manual-security-guide/043.png) | Note: Effective with Patch ROR\*1.5\*14, file checksums are no longer included in this manual. They are always included with the patch description, and can be checked with CHECK1^XTSUMBLD. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc165646512" class="anchor"></span>Table 57 – Segment Definition Examples

| Routine                            | Short Description                                   |
|----------------------------------------|---------------------------------------------------------|
|                                        |                                                         |
| ROR                                | CLINICAL CASE REGISTRIES                                |
| ROR01                              | CLINICAL CASE REGISTRIES                                |
| ROR02                              | CLINICAL CASE REGISTRIES                                |
| ROR10                              | NIGHTLY TASK UTILITIES                                  |
| ROR11                              | NIGHTLY TASK UTILITIES                                  |
| RORAPI01                           | CLINICAL REGISTRIES API                                 |
| RORBIN                             | BINARY OPERATIONS                                       |
| RORDD                              | DATA DICTIONARY UTILITIES                               |
| RORDD01                            | DATA DICTIONARY UTILITIES                               |
| RORERR                             | ERROR PROCESSING                                        |
| RORERR20                           | LIST OF ERROR MESSAGES                                  |
| ROREVT01                           | EVENT PROTOCOLS                                         |
| ROREXPR                            | PREPARATION FOR DATA EXTRACTION                         |
| ROREXT                             | DATA EXTRACTION & TRANSMISSION                          |
| ROREXT01                           | EXTRACTION & TRANSMISSION PROCESS                       |
| ROREXT02                           | DEFAULT MESSAGE BUILDER                                 |
| ROREXT03                           | REGISTRY DATA EXTRACTION (OVERFLOW)                     |
| ROREXTUT                           | DATA EXTRACT UTILITIES                                  |
| RORHDT                             | HISTORICAL DATA EXTRACTION                              |
| RORHDT01                           | HISTORICAL DATA EXTRACTION STATUS                       |
| RORHDT02                           | CREATE EXTRACTION TASK RECORDS                          |
| RORHDT03                           | MANIPULATIONS WITH EXTRACTION TASKS                     |
| RORHDT04                           | HISTORICAL DATA EXTRACTION PROCESS                      |
| RORHDT05                           | HISTORICAL DATA EXTRACTION FUNCTIONS                    |
| RORHDT06                           | HISTORICAL DATA EXTRACTION PARAMETERS                   |
| RORHDTAC                           | DATA EXTRACTION ACTION CONFIRMATIONS                    |
| RORHDTUT                           | HISTORICAL DATA EXTRACTION UTILITIES                    |
| RORHIV03                           | CONVERSION OF THE FILE \#158                            |
| RORHIVUT                           | HIV UTILITIES                                           |
| RORHL01                            | HL7 PATIENT DATA: PID,ZSP,ZRD                           |
| RORHL02                            | HL7 REGISTRY DATA: CSP,CSR,CSS                          |
| RORHL03                            | HL7 PHARMACY: ORC,RXE                                   |
| RORHL031                           | HL7 PHARMACY: UTILITIES                                 |
| RORHL04                            | HL7 RADIOLOGY: OBR,OBX                                  |
| RORHL05                            | HL7 AUTOPSY: OBR                                        |
| RORHL06                            | HL7 LIVER BIOPSY: OBR,OBX                               |
| RORHL07                            | HL7 INPATIENT PHARMACY: ORC,RXE                         |
| RORHL071                           | HL7 IV PHARMACY: ORC,RXE                                |
| RORHL08                            | HL7 INPATIENT DATA: PV1,OBR                             |
| RORHL081                           | HL7 INPATIENT DATA: OBX                                 |
| RORHL09                            | HL7 OUTPATIENT DATA: PV1,OBR,OBX                        |
| RORHL10                            | HL7 SURGICAL PATHOLOGY DATA: OBR,OBX                    |
| RORHL11                            | HL7 CYTOPATHOLOGY DATA: OBR,OBX                         |
| RORHL12                            | HL7 MICROBIOLOGY DATA: OBR                              |
| RORHL121                           | HL7 MICROBIOLOGY DATA: OBX                              |
| RORHL13                            | HL7 MEDICAL PROCEDURES (EKG): OBR,OBX                   |
| RORHL14                            | HL7 ALLERGY DATA: OBR,OBX                               |
| RORHL15                            | HL7 IV DATA: OBR, OBX                                   |
| RORHL16                            | HL7 VITALS DATA: OBR,OBX                                |
| RORHL17                            | HL7 PROBLEM LIST: OBR,OBX                               |
| RORHL18                            | HL7 IMMUNIZATION: OBR, OBX                              |
| RORHL19                            | HL7 SKIN TEST: OBR, OBX                                 |
| RORHL20                            | HL7 NON-VA MEDS: ORC, RXE                               |
| RORHL21                            | HL7 PURCHASED CARE : ZIN, ZSV, ZRX                      |
| RORHL7                             | HL7 UTILITIES                                           |
| RORHL7A                            | HL7 UTILITIES                                           |
| RORHLUT1                           | HL7 UTILITIES (HIGH LEVEL)                              |
| RORKIDS                            | INSTALL UTILITIES (LOW-LEVEL)                           |
| RORLOCK                            | LOCKS AND TYRANSACTIONS                                 |
| RORLOG                             | LOG FILE MANAGEMENT                                     |
| RORLOG01                           | LOG FILE MANAGEMENT (UTILITIES)                         |
| RORNTEG                            | KERNEL - Package checksum checker                       |
| RORNTEG0                           | KERNEL - Package checksum checker                       |
| RORP000                            | CCR V1.5 INSTALLATION ROUTINE                           |
| RORP000A                           | CCR V1.5 PRE-INSTALL CODE                               |
| RORP000B                           | CCR V1.5 POST-INSTALL CODE                              |
| RORP001                            | PATCH ROR\*1.5\*1 INSTALLATION ROUTINE                  |
| RORP004                            | PATCH ROR\*1.5\*4 PRE-INSTALLATION ROUTINE              |
| RORP005                            | PATCH ROR\*1.5\*5 PRE-TRANS/POST-INSTALL ROUTINE        |
| RORP006                            | PATCH ROR\*1.5\*6 PRE-TRANS/POST-INSTALL ROUTINE        |
| RORP007                            | PATCH ROR\*1.5\*7 PRE-TRANS/POST-INSTALL ROUTINE        |
| RORP010                            | CCR POST-INIT PATCH 10                                  |
| RORP011                            | CCR POST-INIT PATCH 13                                  |
| RORP013                            | CCR POST-INIT PATCH 13                                  |
| RORP014                            | CCR POST-INIT PATCH 14                                  |
| RORP015                            | CCR PRE/POST-INIT PATCH                                 |
| RORP017                            | POST INSTALL PATCH 17                                   |
| RORP018                            | POST INSTALL PATCH 18                                   |
| RORP019                            | CCR PRE/POST-INSTALL PATCH 19                           |
| RORP019A                           | CCR COMMON TEMPLATE CODES (PART A)                      |
| RORP019B                           | CCR COMMON TEMPLATE CODES (PART B)                      |
| RORP021                            | POST INSTALL PATCH 21                                   |
| RORP022                            | POST INSTALL PATCH 22                                   |
| RORP022A                           | POST INSTALL PATCH 22                                   |
| RORP024                            | POST INSTALL PATCH 24                                   |
| RORP025                            | POST INSTALL PATCH 25                                   |
| RORP026                            | POST INSTALL PATCH 26                                   |
| RORP026X                           | CLEANUP/CORRECTION - PATCH 26                           |
| RORP027                            | POST INSTALL PATCH 27                                   |
| RORP028                            | POST INSTALL PATCH 28                                   |
| RORP029                            | POST INSTALL PATCH 29                                   |
| RORP030                            | POST INSTALL PATCH 30                                   |
| RORP031                            | POST INSTALL PATCH 31                                   |
| RORP032                            | CCR PRE/POST INSTALL PATCH 32                           |
| RORP033                            | POST INSTALL PATCH 33                                   |
| RORP034                            | POST INSTALL PATCH 34                                   |
| RORP035                            | POST INSTALL PATCH 35                                   |
| RORP035A                           | POST INSTALL PATCH 35 (cont.)                           |
| RORP036                            | CCR PRE/POST INSTALL PATCH 36                           |
| RORP037                            | CCR PRE/POST INSTALL PATCH 37                           |
| RORP041                            | CCR PRE/POST INSTALL PATCH 41                           |
| <span class="mark">RORP042</span>  | <span class="mark">CCR PRE/POST INSTALL PATCH 42</span> |
| RORPUT01                           | EDIT LOINC AND DRUG CODE MULTIPLES                      |
| RORPUT02                           | DATA TRANSPORT FOR KIDS                                 |
| RORREP01                           | REGISTRY COMPARISON REPORT                              |
| RORREP02                           | VERSION COMPARISON REPORT (ICR)                         |
| RORRP007                           | RPC: LOGS & MESSAGES                                    |
| RORRP010                           | RPC: TASK MANAGER                                       |
| RORRP011                           | RPC: TASK MANAGER (REPORTS)                             |
| RORRP012                           | RPC: MISCELLANEOUS                                      |
| RORRP013                           | RPC: ACCESS & SECURITY                                  |
| RORRP014                           | RPC: REGISTRY INFO & PARAMETERS                         |
| RORRP015                           | RPC: DIVISIONS AND HOSPITAL LOCATIONS                   |
| RORRP016                           | RPC: ICD-9 CODES                                        |
| RORRP017                           | RPC: DRUGS AND CLASSES                                  |
| RORRP018                           | RPC: LIST OF LAB TESTS                                  |
| RORRP019                           | RPC: LIST OF PATIENTS                                   |
| RORRP020                           | RPC: PATIENT DATA UTILITIES                             |
| RORRP021                           | RPC: PATIENT DATA                                       |
| RORRP022                           | RPC: SELECTION RULES                                    |
| RORRP023                           | RPC: REGISTRY COORDINATORS                              |
| RORRP024                           | RPC: VISTA USERS                                        |
| RORRP025                           | RPC: RORICR CDC LOAD                                    |
| RORRP026                           | RPC: CDC UTILITIES                                      |
| RORRP027                           | RPC: RORICR CDC SAVE                                    |
| RORRP029                           | RPC: ADDRESS UTILITIES                                  |
| RORRP030                           | RPC: PATIENT DELETE                                     |
| RORRP031                           | RPC: LOCAL LAB TEST NAMES                               |
| RORRP032                           | RPC: LOCAL DRUG NAMES                                   |
| RORRP033                           | RPC: HIV PATIENT LOAD                                   |
| RORRP034                           | RPC: HIV PATIENT SAVE/CANCEL                            |
| RORRP035                           | RPC: GENERIC DRUG NAMES                                 |
| RORRP036                           | RPC: HEPC PATIENT LOAD                                  |
| RORRP037                           | RPC: HEPC PATIENT SAVE/CANCEL                           |
| RORRP038                           | RPC: USER AND PACKAGE PARAMETERS                        |
| RORRP040                           | RPC: LOCAL REGISTRY FIELDS                              |
| RORRP041                           | RPC: REGISTRY-SPECIFIC LAB RESULTS                      |
| RORRP042                           | RPC: CPT CODES                                          |
| RORSET01                           | REGISTRY SETUP ROUTINE                                  |
| RORSET02                           | REGISTRY INITIALIZATION FOR LOCAL REGISTRIES            |
| RORSETU1                           | SETUP UTILITIES (USER INTERFACE)                        |
| RORSETU2                           | SETUP UTILITIES (REGISTRY)                              |
| RORTSITE                           | PREPARE TEST SITES FOR GOING LIVE                       |
| RORTMP                             | TEMPORARY GLOBAL STORAGE                                |
| RORTSK                             | TASK MANAGER                                            |
| RORTSK01                           | (SUB)TASK UTILITIES                                     |
| RORTSK02                           | TASK MANAGER UTILITIES                                  |
| RORTSK03                           | TASK MANAGER OVERFLOW CODE                              |
| RORTSK10                           | REPORT RETRIEVING UTILITIES                             |
| RORTSK11                           | REPORT CREATION UTILITIES                               |
| RORTSK12                           | REPORT STATS UTILITIES                                  |
| RORTSK13                           | PARSER FOR REPORT PARAMETERS                            |
| RORTSK14                           | PARSER FOR REPORT PARAMETERS (TOOLS)                    |
| RORTXT                             | TEXT RESOURCE UTILITIES                                 |
| RORUPD                             | REGISTRY UPDATE                                         |
| RORUPD01                           | PROCESSING OF THE FILES                                 |
| RORUPD04                           | PROCESSING OF THE LAB DATA                              |
| RORUPD05                           | REGISTRY UPDATE (MULTITASK)                             |
| RORUPD06                           | REGISTRY UPDATE (MISCELLANEOUS)                         |
| RORUPD07                           | PROCESSING OF THE 'PROBLEM' FILE                        |
| RORUPD08                           | PROCESSING OF 'VISIT' & 'V POV' FILES                   |
| RORUPD09                           | PROCESSING OF THE 'PTF' FILE                            |
| RORUPD50                           | UPDATE THE PATIENT IN THE REGISTRIES                    |
| RORUPD51                           | UPDATE PATIENT'S DEMOGRAPHIC DATA (1)                   |
| RORUPD52                           | UPDATE PATIENT'S DEMOGRAPHIC DATA (2)                   |
| RORUPD62                           | HIV-SPECIFIC REGISTRY UPDATE CODE                       |
| RORUPDUT                           | REGISTRY UPDATE UTILITIES                               |
| RORUPEX                            | SELECTION RULE EXPRESSION PARSER                        |
| RORUPP01                           | PATIENT EVENTS (ERRORS)                                 |
| RORUPP02                           | PATIENT EVENTS (EVENTS)                                 |
| RORUPR                             | SELECTION RULES PREPARATION                             |
| RORUPR1                            | SELECTION RULES PREPARATION                             |
| RORUTL01                           | UTILITIES                                               |
| RORUTL02                           | UTILITIES                                               |
| RORUTL03                           | ENCRYPTION/DECRYPTION                                   |
| RORUTL04                           | REGISTRY STAT REPORT                                    |
| RORUTL05                           | MISCELLANEOUS UTILITIES                                 |
| RORUTL06                           | DEVELOPER ENTRY POINTS                                  |
| RORUTL07                           | TEST ENTRY POINTS                                       |
| RORUTL08                           | REPORT PARAMETERS UTILITIES                             |
| RORUTL09                           | LIST ITEM UTILITIES                                     |
| RORUTL10                           | LAB DATA SEARCH                                         |
| <span class="mark">RORUTL11</span> | <span class="mark">ACCESS AND SECURITY UTILITIES</span> |
| RORUTL14                           | PHARMACY DATA SEARCH                                    |
| RORUTL15                           | PHARMACY DATA SEARCH (TOOLS)                            |
| RORUTL16                           | PHARMACY DATA SEARCH (UTILITIES)                        |
| RORUTL17                           | REGISTRY INFORMATION UTILITIES                          |
| RORUTL18                           | MISCELLANEOUS UTILITIES                                 |
| RORUTL19                           | PATIENT DATA UTILITIES                                  |
| RORUTL20                           | INPATIENT PROCEDURES UTILITIES                          |
| RORUTL22                           | COLLECT ROR DRUG MATCH                                  |
| RORVM001                           | MAINTENANCE OPTIONS                                     |
| RORX000                            | DUMMY REPORT                                            |
| RORX001                            | LIST OF REGISTRY PATIENTS                               |
| RORX002                            | CURRENT INPATIENT LIST                                  |
| RORX003                            | GENERAL UTLIZATION AND DEMOGRAPHICS                     |
| RORX003A                           | GENERAL UTLIZATION AND DEMOGRAPHICS                     |
| RORX004                            | CLINIC FOLLOW UP                                        |
| RORX005                            | INPATIENT UTILIZATION                                   |
| RORX005A                           | INPATIENT UTILIZATION (QUERY)                           |
| RORX005B                           | INPATIENT UTILIZATION (SORT)                            |
| RORX005C                           | INPATIENT UTILIZATION (STORE)                           |
| RORX006                            | LAB UTILIZATION                                         |
| RORX006A                           | LAB UTILIZATION (QUERY & SORT)                          |
| RORX006C                           | LAB UTILIZATION (STORE)                                 |
| RORX007                            | RADIOLOGY UTILIZATION                                   |
| RORX007A                           | RADIOLOGY UTILIZATION (OVERFLOW)                        |
| RORX008                            | VERA REIMBURSEMENT REPORT                               |
| RORX008A                           | VERA REIMBURSEMENT REPORT                               |
| RORX009                            | PHARMACY PRESCRIPTION UTILIZATION                       |
| RORX009A                           | PRESCRIPTION UTILIZ. (QUERY & SORT)                     |
| RORX009C                           | PRESCRIPTION UTILIZ. (STORE)                            |
| RORX010                            | LAB TESTS BY RANGE REPORT                               |
| RORX011                            | PATIENT MEDICATION HISTORY                              |
| RORX012                            | COMBINED MEDS AND LABS REPORT                           |
| RORX012A                           | COMBINED MEDS AND LABS (QUERY & STORE)                  |
| RORX013                            | DIAGNOSIS CODES REPORT                                  |
| RORX013A                           | DIAGNOSIS CODES (QUERY & SORT)                          |
| RORX013C                           | DIAGNOSIS CODES (STORE)                                 |
| RORX014                            | REGISTRY MEDICATIONS REPORT                             |
| RORX014A                           | REGISTRY MEDS REPORT (QUERY & SORT)                     |
| RORX015                            | PROCEDURES (CPT) REPORT                                 |
| RORX015A                           | PROCEDURES (QUERY & SORT)                               |
| RORX015C                           | PROCEDURES (STORE)                                      |
| RORX016                            | OUTPATIENT UTILIZATION                                  |
| RORX016A                           | OUTPATIENT UTILIZATION (QUERY)                          |
| RORX016B                           | OUTPATIENT UTILIZATION (SORT)                           |
| RORX016C                           | OUTPATIENT UTILIZATION (STORE)                          |
| RORX018                            | BMI BY RANGE REPORT                                     |
| RORX018A                           | BMI BY RANGE REPORT                                     |
| RORX019                            | LIVER SCORE BY RANGE REPORT                             |
| RORX019A                           | LIVER SCORE BY RANGE REPORT                             |
| RORX020                            | RENAL FUNCTION BY RANGE REPORT                          |
| RORX020A                           | RENAL FUNCTION BY RANGE REPORT                          |
| RORX020B                           | RENAL FUNCTION BY RANGE REPORT                          |
| RORX021                            | HCV DAA CANDIDATES REPORT                               |
| RORX021A                           | HCV DAA CANDIDATES(QUERY & STORE)                       |
| RORX022                            | LAB DAA MONITOR REPORT                                  |
| RORX022A                           | LAB DAA MONITOR (CONT.)                                 |
| RORX023                            | SUSTAINED VIROLOGIC RESPONSE REPORT                     |
| RORX023A                           | SUSTAINED VIROLOGIC RESPONSE (CONT.)                    |
| RORX024                            | HEP A/B VACCINE/IMMUNITY REPORTS (QUERY & STORE)        |
| RORX024A                           | HEP A/B VACCINE/IMMUNITY REPORTS (QUERY & STORE)        |
| RORX025                            | HEP A/B VACCINE/IMMUNITY REPORTS (QUERY & STORE)        |
| RORXU001                           | REPORT UTILITIES                                        |
| RORXU002                           | REPORT BUILDER UTILITIES                                |
| RORXU003                           | REPORT BUILDER UTILITIES                                |
| RORXU004                           | REPORT UTILITIES (STATISTICS)                           |
| RORXU005                           | REPORT BUILDER UTILITIES                                |
| RORXU006                           | REPORT PARAMETERS                                       |
| RORXU007                           | PHARMACY-RELATED REPORT PARAMETERS                      |
| RORXU009                           | REPORT MODIFICATION UTILITY                             |
| RORXU010                           | REPORT MODIFICATION UTILITY                             |

<span id="_Toc165646513" class="anchor"></span>Table 58 – Batch Header Segments

## Routine Sub-Namespaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Namespace     | Description                                             |
|---------------|---------------------------------------------------------|
| RORAPI\*  | Supported APIs                                          |
| RORDD\*   | Routines used by the Data Dictionary                    |
| RORERR\*  | Error processing                                        |
| ROREVT\*  | Event protocols                                         |
| ROREX\*   | Regular data extraction & transmission                  |
| RORHDT\*  | Historical data extraction                              |
| RORHIV\*  | HIV Registry-specific routines                          |
| RORHL\*   | HL7 utilities                                           |
| RORKIDS\* | Low-level installation utilities (KIDS)                 |
| RORLOCK\* | Locks and transactions                                  |
| RORLOG\*  | Error recording                                         |
| RORPnnn\* | Patch installation routines (KIDS) (nnn = patch number) |
| RORPUT\*  | High-level installation utilities                       |
| RORREP\*  | Roll-and-scroll reports                                 |
| RORRP\*   | Remote procedures                                       |
| RORSET\*  | Registry setup routines                                 |
| RORTXT\*  | Text resource routines                                  |
| RORUP\*   | Registry update                                         |
| RORUTL\*  | Utilities                                               |
| RORVM\*   | Entry points for VistA menu options                     |
| RORXnnn\* | XML reports (nnn = report code)                         |
| RORXU\*   | Utilities for XML reports                               |

<span id="_Toc165646514" class="anchor"></span>Table 59 – BHS-9 Batch Name/ID/Type

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XINDEX is a routine that produces a report called the VA Cross-Reference. This report is a cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a listing of internal and external routine calls.

XINDEX is invoked from programmer mode: D ^XINDEX.

When selecting routines, select ROR\*.

# Exported Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menus and options exported by the build ROR 1.5 are all located in the ROR namespace. Individual options can be viewed by using the Option Function Inquiry \[XUINQUIRE\] option. This option can be found on the Menu Management \[XUMAINT\] menu, which is a sub-menu of the Systems Manager Menu \[EVE\] menu.

A diagram of the structure of the CCR menu and its options can be produced by using the Diagram Menus \[XUUSERACC\] option. Choosing XUUSERACC permits you to further select Menu Diagrams (with Entry/Exit Actions) \[XUUSERACC1\] or Abbreviated Menu Diagrams \[XUUSERACC2\] options.

<table>
<caption><p><span id="_Toc165646515" class="anchor"></span>Table 60 – Batch Trailer Segment</p></caption>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Broker Context</p>
<p><strong>[ROR GUI]</strong></p></td>
<td>This option holds the references to the package RPC Broker Calls used by the GUI to create an application context (for security purposes).</td>
</tr>
<tr class="even">
<td><p>Registry Setup</p>
<p><strong>[ROR SETUP]</strong></p></td>
<td>This option allows the user to enter parameters of the registry setup process, and to schedule the task that will populate the registry.</td>
</tr>
<tr class="odd">
<td><p>Registry Update &amp; Data Extraction</p>
<p><strong>[ROR TASK]</strong></p></td>
<td><p>This option starts the registry update and data extraction task that processes registries defined by the TASK PARAMETERS field. The field must contain a list of registry names separated by commas.</p>
<p>The following task parameters are optional. They can be defined on the second page of the option scheduling form (as the pairs of the variable names and values).</p>
<p><strong>RORFLCLR</strong> (Default: "") and <strong>RORFLSET</strong> (Default: EX)</p>
<p>These two parameters override the values of the flags that control the processing. Add the flags to the RORFLCLR variable to clear them and to the RORFLSET variable to set them. Below are the possible values of the parameters (can be combined):</p>
<p>D – Run the task(s) in Debug Mode</p>
<p>E – Use the event references (file #798.3)</p>
<p>S – Run the data extraction in single-task mode</p>
<p>X – Suspend the data extraction task in the same way as the registry update</p>
<p>M – Disable the HL7 messaging for local (user defined) registries.</p>
<p>When the M flag is set, HL7 messages will not be transmitted to Austin.</p>
<p><strong>RORMNTSK</strong> (Default: 2-3-AUTO)</p>
<p>Maximum number of the registry update subtasks. If this parameter is less than 2, all patients will be processed by the single main task. Otherwise, all patients can be distributed among several subtasks.</p>
<p>If N-M-AUTO is passed as the value of this parameter and difference between the end and start dates of the registry update is more than M days then N subtasks will be started. Otherwise, the single task will run.</p>
<p><strong>RORSUSP</strong> (Default: "")</p>
<p>Suspension parameters of the registry update and data extraction subtasks. The subtasks are not suspended by default. Parameter should contain start and end times of the suspension (in external format) separated by the "-". For example, the 7:00-18:00 value will suspend the subtasks from 7am until 6pm each day except weekends and holidays.</p></td>
</tr>
<tr class="even">
<td><p>Create Extraction Tasks</p>
<p><strong>[RORHDT CREATE]</strong></p></td>
<td>This option spreads historical data processing over several tasks in order to speed up the process.</td>
</tr>
<tr class="odd">
<td><p>Edit</p>
<p><strong>[RORHDT EDIT]</strong></p></td>
<td>This option displays a submenu when selected. The submenu contains options that are used to create and edit the parameters of the historical data extraction.</td>
</tr>
<tr class="even">
<td><p>Edit data extraction</p>
<p><strong>[RORHDT EDIT EXTRACTION]</strong></p></td>
<td>This option allows users to edit parameters of manual historical data extraction in the ROR HISTORICAL DATA EXTRACTION file (#799.6).</td>
</tr>
<tr class="odd">
<td><p>Edit Task Descriptor</p>
<p><strong>[RORHDT EDIT TASK]</strong></p></td>
<td>This option allows users to edit parameters of historical data extraction tasks in the ROR HISTORICAL DATA EXTRACTION file (#799.6).</td>
</tr>
<tr class="even">
<td><p>Display Task Log</p>
<p><strong>[RORHDT LOG]</strong></p></td>
<td>The Display Task Log option lets users see a log of any running or finished data extraction task. If any errors have been found, they will be logged here. Any errors should be fixed and then the task re-started.</td>
</tr>
<tr class="odd">
<td><p>Historical Data Extraction</p>
<p><strong>[RORHDT MAIN]</strong></p></td>
<td>This is a top level management option for the historical data extraction that gathers historical data for each registry patient that exists on the ROR REGISTRY RECORD file (#798) and creates flat text files that can be sent by FTP to a pre-defined area at the AAC. This is done independently of daily updates and extracts and requires some intervention of an IRM.</td>
</tr>
<tr class="even">
<td><p>Start a Task</p>
<p><strong>[RORHDT START]</strong></p></td>
<td>This option starts a data extraction task that was created with the Create Extraction Tasks option.</td>
</tr>
<tr class="odd">
<td><p>Display Extraction Status</p>
<p><strong>[RORHDT STATUS]</strong></p></td>
<td>This option displays the status of a selected data extraction. The historical data extraction start and end dates, the output directory name, processed registries, and task table are displayed.</td>
</tr>
<tr class="even">
<td><p>Stop a Task</p>
<p><strong>[RORHDT STOP]</strong></p></td>
<td>This option allows users to stop a running task or de-queue a task that is scheduled to run in the future.</td>
</tr>
<tr class="odd">
<td><p>ICR Version Comparison Report</p>
<p><strong>[RORICR VERSION COMPARISON]</strong></p></td>
<td><p>Provides a detailed comparison between the CCR:HIV and Immunology Case Registry v2.1. The ICR was officially retired on October 27, 2005 (patch IMR*2.1*21) and replaced by CCR:HIV.</p>
<p>This option is left for compatibility. If ICR v2.1 is not installed in the account, then the option will display an error message and quit.</p></td>
</tr>
<tr class="even">
<td><p>Re-index the ACL cross-reference</p>
<p><strong>[RORMNT ACL REINDEX]</strong></p></td>
<td>This option lets users re-index the ACL cross-reference of the ROR REGISTRY PARAMETERS file (#798.1). This cross-reference should be rebuilt after changes in the allocation of the security keys associated with any registry.</td>
</tr>
<tr class="odd">
<td><p>Edit Lab Search Criteria</p>
<p><strong>[RORMNT EDIT LAB SEARCH]</strong></p></td>
<td>This option is used to edit the Lab search criteria (stored in the ROR LAB SEARCH file (#798.9)) that are used by the registry update process to find patients with positive registry-specific Lab results.</td>
</tr>
<tr class="even">
<td><p>Edit Registry Parameters</p>
<p><strong>[RORMNT EDIT REG PARAMS]</strong></p></td>
<td>This option can be used to edit registry parameters in the ROR REGISTRY PARAMETERS file (#798.1).</td>
</tr>
<tr class="odd">
<td><p>Initialize new registries (one time)</p>
<p>[ROR INITIALIZE]</p></td>
<td><p>This option allows the user to schedule the task that will</p>
<p>populate the sixteen new registries added in ROR*1.5*18.</p></td>
</tr>
<tr class="even">
<td><p>Clinical Case Registries Maintenance</p>
<p><strong>[RORMNT MAIN]</strong></p></td>
<td>This menu contains miscellaneous maintenance options for the CCR package. Usually, they should be used only for troubleshooting.</td>
</tr>
<tr class="odd">
<td><p>List of Pending Errors</p>
<p><strong>[RORMNT PENDING ERRORS LIST]</strong></p></td>
<td><p>The option prints a report containing list of patients (referenced by the ERROR multiples of the ROR PATIENT EVENTS file (#798.3)) having erroneous data. The list is sorted by value of the COUNTER field (number of times that an error was recorded for a patient).</p>
<p>This report can be used to find patients ignored by the registry update (until someone fixes the error(s) and resets value of the COUNTER field to 1).</p></td>
</tr>
<tr class="even">
<td><p>Pending Patients</p>
<p><strong>[RORMNT PENDING PATIENTS]</strong></p></td>
<td>This menu groups the options used for maintenance of the ROR PATIENT EVENTS file (#798.3) containing event and error references.</td>
</tr>
<tr class="odd">
<td><p>Print Log Files</p>
<p><strong>[RORMNT PRINT LOGS]</strong></p></td>
<td>This option can be used to print messages recorded by the CCR software.</td>
</tr>
</tbody>
</table>

<span id="_Toc165646515" class="anchor"></span>Table 60 – Batch Trailer Segment

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No archiving functions are necessary with the CCR software.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Old event references are automatically purged by the nightly task (the \[ROR TASK\] option) from the EVENT multiple (2) of the ROR PATIENT EVENTS file (#798.3) no later than 60 days after they were entered there by the event protocols.

ROR LOG file (#798.7) entries are automatically purged 31 days after they are entered into this file.

Old tasks are automatically purged from the ROR TASK file (#798.8) 14 days after they are completed (the creation date is used for incomplete tasks).

# Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following [protocols](#Glos_Protocol) are exported with the KIDS build ROR 1.5.

## HL7 Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- ROR-SITE-DRIVER
- ROR-SITE-SUBSCRIBER

## Event Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three event protocols are used by CCR, as outlined in Table 49.

<table>
<caption><p><span id="_Toc165646516" class="anchor"></span>Table 61 – Clinical Study Phase Segment</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Protocol</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ROR EVENT LAB</strong></td>
<td><p>This protocol is used by the CCR package to maintain references to patients who have new lab results. The protocol should be subscribed to the LR7O ALL EVSEND RESULTS protocol (this is done by the KIDS during the installation).</p>
<p>If at least one of the defined registries enables event protocols, this protocol will process the Lab events and create references in the ROR PATIENT EVENTS file (#798.3). Otherwise, the protocol will be executed (if it is not disabled or unsubscribed manually) but will not call the processing routine (LAB^ROREVT01).</p></td>
</tr>
<tr class="even">
<td><strong>ROR EVENT PTF</strong></td>
<td><p>This protocol is used by the CCR package to maintain references to patients who have new admissions. ). The protocol should be subscribed to the DGPM MOVEMENT EVENT protocol (this is done by the KIDS during the installation).</p>
<p>If at least one of the defined registries enables event protocols, this protocol will process the movement events and create references in the ROR PATIENT EVENTS file (#798.3). Otherwise, the protocol will be executed (if it is not disabled or unsubscribed manually) but will not call the processing routine (PTF^ROREVT01).</p></td>
</tr>
<tr class="odd">
<td><strong>ROR EVENT VISIT</strong></td>
<td><p>This protocol is used by the CCR package to maintain references to patients who have new data in the V-files (VISIT, V POV, etc). The protocol should be subscribed to the PXK VISIT DATA EVENT protocol (this is done by the KIDS during the installation).</p>
<p>If at least one of the defined registries enables event protocols, this protocol will process the Lab events and create references in the ROR PATIENT EVENTS file (#798.3). Otherwise, the protocol will be executed (if it is not disabled or unsubscribed manually) but will not call the processing routine (VISIT^ROREVT01).</p></td>
</tr>
</tbody>
</table>

<span id="_Toc165646516" class="anchor"></span>Table 61 – Clinical Study Phase Segment

# Application Program Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Data Base Agreement (DBIA) \#4166 defines two controlled-subscription [Application Program Interfaces](#Glos_API) (APIs) that are supplied by CCR. The first of these APIs enumerates patients of the given registry (CCR:HEPC or CCR:HIV), and the other API enumerates registries within which the patient exists.

| API                                          | Description                                                               |                                                                          |                                                                    |
|----------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------|
| \$\$PATITER^RORAPI01(IDESC,REGNAME,MODE) | Creates an [iterator](#Glos_Iterator) of patients in the registry, where… |                                                                          |                                                                    |
|                                              | IDESC                                                                 | Refers to a local variable where the iterator descriptor will be created |                                                                    |
|                                              | REGNAME                                                               | Is the Registry name                                                     |                                                                    |
|                                              | \[MODE\]                                                              | Is a bit flag which defines the iteration mode (default = 3)         |                                                                    |
|                                              |                                                                           | 1                                                                    | Active patients (confirmed and not deleted)                        |
|                                              |                                                                           | 2                                                                    | (reserved)                                                         |
|                                              | Return Values                                                         | \<0                                                                  | Error code                                                         |
|                                              |                                                                           | 0                                                                    | OK                                                                 |
| \$\$NEXTPAT^RORAPI01(IDESC)              | Returns the next patient in the registry, where…                          |                                                                          |                                                                    |
|                                              | IDESC                                                                 | Refers to the iterator descriptor created by \$\$PATITER^RORAPI01.       |                                                                    |
|                                              | Return Values                                                         | \<0                                                                  | Error code                                                         |
|                                              |                                                                           | ""                                                                       | No more patients in the registry                                   |
|                                              |                                                                           | \>0                                                                  | Patient IEN (DFN)                                                  |
| \$\$REGITER^RORAPI01(IDESC,PATIEN,MODE)  | Creates an [iterator](#Glos_Iterator) of patient registries, where…       |                                                                          |                                                                    |
|                                              | IDESC                                                                 | Refers to a local variable where the iterator descriptor will be created |                                                                    |
|                                              | PATIEN                                                                | Is the Patient IEN (DFN)                                                 |                                                                    |
|                                              | \[MODE\]                                                              | Is a bit flag which defines the iteration mode (default = 3)             |                                                                    |
|                                              |                                                                           | 1                                                                    | Registries where the patient is active (confirmed and not deleted) |
|                                              |                                                                           | 2                                                                    | (reserved)                                                         |
|                                              | Return Values                                                         | \<0                                                                  | Error code                                                         |
|                                              |                                                                           | 0                                                                    | OK                                                                 |
| \$\$NEXTREG^RORAPI01(IDESC)              | Returns the next patient in the registry, where…                          |                                                                          |                                                                    |
|                                              | IDESC                                                                 | Refers to the iterator descriptor created by \$\$REGITER^RORAPI01.       |                                                                    |
|                                              | Return Values                                                         | \<0                                                                  | Error code                                                         |
|                                              |                                                                           | ""                                                                       | No more patients in the registry                                   |
|                                              |                                                                           | \>0                                                                  | Registry IEN                                                       |

<span id="_Toc165646517" class="anchor"></span>Table 62 – Clinical Study Registration Segment

Below is a usage example for these APIs taken from the source code of the RORAPI01 routine:

<span id="_Toc162942919" class="anchor"></span>Figure 22 – Sample Usage (RORAPI01 Routine)

![](ror-1-5-42-technical-manual-security-guide/044.png)

The following screenshot illustrates the output of the sample code:

<span id="_Toc162942920" class="anchor"></span>Figure - Sample Output (RORAPI01 Routine)

![](ror-1-5-42-technical-manual-security-guide/045.png)

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The National Database has an [HL7](#Glos_HL7) interface. This interface receives all data transmissions sent from all sites nationally, converts the data, and enters it into an [SQL](#Glos_SQL)-enabled database.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the KIDS build ROR 1.5 can be installed, the following software applications and patches must be installed and *fully* patched in your accounts:

| Application Name                               | Minimum Version |
|------------------------------------------------|-----------------|
| Automated Information Collection System (AICS) | V 3.0           |
| Adverse Reaction Tracking (ART)                | V 4.0           |
| Authorization/Subscription Utility (ASU)       | V 1.0           |
| Consult/Request Tracking                       | V 3.0           |
| Gen. Med. Rec.-Vitals                          | V 4.0           |
| Health Summary                                 | V 2.7           |
| HL7                                            | V 1.6           |
| Inpatient Medications (IM)                     | V 5.0           |
| Kernel                                         | V 8.0           |
| Laboratory                                     | V 5.2           |
| Lexicon Utility                                | V 2.0           |
| National Drug File (NDF)                       | V 4.0           |
| Order Entry/Results Reporting (OE/RR)          | V 3.0           |
| Outpatient Pharmacy                            | V 7.0           |
| Patient Care Encounter (PCE)                   | V 1.0           |
| Pharmacy Data Management (PDM)                 | V 1.0           |
| Problem List                                   | V 2.0           |
| Radiology/Nuclear Medicine                     | V 5.0           |
| RPC Broker                                     | V 1.1           |
| Registration                                   | V 5.3           |
| Scheduling                                     | V 5.3           |
| Text Integration Utilities (TIU)               | V 1.0           |
| ToolKit                                        | V. 7.3          |
| VA FileMan                                     | V 22.0          |
| Visit Tracking                                 | V 2.0           |

<span id="_Toc165646518" class="anchor"></span>Table 63 – Message Acknowledgment Segment

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the installation of the build ROR 1.5, the following patches must be installed:

<table>
<caption><p><span id="_Toc165646519" class="anchor"></span>Table 64 – Message Header Segment</p></caption>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Application Name</td>
<td>Patches</td>
</tr>
<tr class="even">
<td>Health Level Seven</td>
<td>HL*1.6*57</td>
</tr>
<tr class="odd">
<td>Registration</td>
<td>DG*5.3*471, DG*5.3*415, DG*5.3*631</td>
</tr>
<tr class="even">
<td>Automated Lab Instruments</td>
<td>LA*5.2*69, LA*5.2*68</td>
</tr>
<tr class="odd">
<td>Lab Service</td>
<td>LR*5.2*222, LR*5.2*232</td>
</tr>
<tr class="even">
<td>Medicine or Clinical Procedures</td>
<td>MC*2.3*34 or MD*1.0*1</td>
</tr>
<tr class="odd">
<td>National Drug File</td>
<td>PSN*4.0*53, PSN*4*79, PSN*4.0*104</td>
</tr>
<tr class="even">
<td>Pharmacy Data Management</td>
<td>PSS*1.0*101, PSS*1.0*105, PSS*1.0*97</td>
</tr>
<tr class="odd">
<td>Clinical Case Registries</td>
<td><p>ROR*1*41</p>
<p>(this patch is not required for initial installation)</p></td>
</tr>
<tr class="even">
<td>Scheduling</td>
<td>SD*5.3*254, SD*5.3*131</td>
</tr>
</tbody>
</table>

<span id="_Toc165646519" class="anchor"></span>Table 64 – Message Header Segment

## Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The list of approved DBIAs for CCR 1.5 is shown in Table 52.

|                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ror-1-5-42-technical-manual-security-guide/046.png) |

<span id="_Toc165646520" class="anchor"></span>Table 65 – Observation Request

<table>
<caption><p><span id="_Toc165646521" class="anchor"></span>Table 66 – Observation/Result Segment</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 51%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>File Number</th>
<th>Access</th>
<th>DBIA #</th>
<th>Comment*</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="7">PATIENT</td>
<td rowspan="7">2</td>
<td><p>Browse IENs</p>
<p>.02, .03, .06, .09, .351, 63</p></td>
<td>10035</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td><p>6^VADPT</p>
<p>(.1112, .301, .302, .323)</p></td>
<td>10061</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td><p>$$GETICN^MPIF001</p>
<p>(991.01)</p></td>
<td>2701</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td>-9 node</td>
<td>2762</td>
<td><strong>P</strong></td>
</tr>
<tr class="odd">
<td>.3721 (multiple)</td>
<td>174</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>63</td>
<td>998</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>EN^VAFHLPID</td>
<td>263</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td>CLINIC STOP</td>
<td>40.7</td>
<td><p>^DIC(40.7,D0,0)</p>
<p>.01, 1, 2</p>
<p>^DIC(40.7,'C',X,D0)</p></td>
<td>93-C</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>40.7</td>
<td>Read access to the file #40.7</td>
<td>557</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>MEDICAL CENTER DIVISION</td>
<td>40.8</td>
<td><p>.01, 1</p>
<p>"B", "C"</p></td>
<td>417</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>SPECIALTY</td>
<td>42.4</td>
<td><p>^DIC(42.4,D0,0)</p>
<p>.01</p></td>
<td>997</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td rowspan="2">CLINIC STOP</td>
<td rowspan="2">44</td>
<td><p>^SC(D0,0)</p>
<p>8</p></td>
<td>93-A</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>3.5</td>
<td>10040</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td rowspan="4">PTF</td>
<td rowspan="4">45</td>
<td>RPC^DGPTFAPI</td>
<td>3157</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td>80<br />
^DGPT( 'AAD',</td>
<td>3545</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td>Access to multiple fields</td>
<td>92</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>PTFICD^DGPTFUT</td>
<td>6130</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td>PTF CLOSE OUT</td>
<td>45.84</td>
<td><p>.01</p>
<p>"AC"</p></td>
<td>994</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td colspan="2" rowspan="7"><p>PHARMACY PATIENT</p>
<p>55</p></td>
<td><p>^PS(55,'AUDS',X,D0,D1)</p>
<p>^PS(55,D0,5,</p>
<p>.01, .5, 3, 1, 68</p>
<p>^PS(55,D0,5,D1,2)</p>
<p>9, 10, 26, 34</p>
<p>^PS(55,D0,5,D1,1,D2,0)</p>
<p>.01, .02, .03</p>
<p>^PS(55,D0,5,D1,11,D2,0)</p>
<p>.01, .02, .05, .03, .04, .06, .07, .08 ^PS(55,D0,'IV',</p>
<p>.01, .02, .03, .04, 108, .06, .08, .08, 104, 106, 132, .22 ^PS(55,D0,'IV',D1,AD,D2,0)</p>
<p>.01,.02</p>
<p>^PS(55,D0,'IV',D1,SOL,D2,0)</p>
<p>.01, 1</p>
<p>^PS(55,D0,'IV',D1,LAB,D2,0)</p>
<p>1, 2, 4, 6</p></td>
<td>2497</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td><p>^PS(55,D0,5,D1,0)</p>
<p>.01, 3, 4, 7, .25, 12, 39 ^PS(55,D0,5,D1,2)</p>
<p>26, 10, 34</p>
<p>^PS(55,D0,5,D1,1,D2,0)</p>
<p>.01, .02</p>
<p>^PS(55,DFN,5,'AUS',</p></td>
<td>117</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td><p>^PS(55,D0,'P',D1,0)</p>
<p>.01</p>
<p>^PS(55,DFN,'P','A',DATE,</p></td>
<td>90-B</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>OCL^PSOORRL, OEL^PSOORRL</td>
<td>2400</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>RX^PSO52API</td>
<td>4820</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td>EN^PSOORDER</td>
<td>1878</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td>^PSOHCSUM</td>
<td>330</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>OUTPATIENT SITE</td>
<td>59</td>
<td><p>^PS(59,D0,0)</p>
<p>.01, .06</p>
<p>^PS(59,D0,INI)</p>
<p>100</p></td>
<td>1876</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td rowspan="2">LAB</td>
<td rowspan="2">60</td>
<td><p>^LAB(60,D0,0)</p>
<p>.01, 1, 4, 5</p>
<p>^LAB(60,'B',</p>
<p>^LAB(60,'C',</p>
<p>^LAB(60,D0,2)</p></td>
<td>91-A</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>ATESTS^ORWLRR</td>
<td>2947</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>COLLECTION SAMPLE</td>
<td>62</td>
<td><p>^LAB(62,0)</p>
<p>.01</p></td>
<td>2210</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td rowspan="8">LAB DATA</td>
<td rowspan="8">63</td>
<td></td>
<td>67-C</td>
<td>Surgical pathology for liver biopsy</td>
</tr>
<tr class="odd">
<td></td>
<td>2503</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td></td>
<td>91-B</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>Autopsy node</td>
<td>3465</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td>$$GCPR^LA7QRY</td>
<td>3556</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>SPATH^LA7UTL03</td>
<td>4343</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>CPATH^LA7UTL03</td>
<td>4344</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>GETDATA^LA7UTL1A</td>
<td>4335</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>LABORATORY SITE</td>
<td>69.9</td>
<td>.01, 95.3</td>
<td>3557</td>
<td><strong>P</strong> Environment check routine</td>
</tr>
<tr class="odd">
<td>RAD/NUC MED PATIENT</td>
<td>70</td>
<td><p>^RADPT(D0,0)</p>
<p>.01</p>
<p>^RADPT(D0,'DT',D1,0)</p>
<p>.01, 2, 3, 4</p>
<p>^RADPT(D0,'DT',D1,'P',D2,0)</p>
<p>2, 3 6, 7, 8, 13, 14</p>
<p>^RADPT(D0,'DT',D1,'P',D2,'M',D3,0)</p>
<p>.01 ^RADPT(D0,'DT',D1,'P',D2,'CMOD',D3,0)</p>
<p>135</p>
<p>^RADPT(D0,'DT',D1,'P',D2,'H',</p>
<p>.01</p></td>
<td>65</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>RAD/NUC MED PROCEDURES</td>
<td>71</td>
<td><p>^RAMIS(71,D0,0)</p>
<p>.01, 9 , 10</p>
<p>^RAMIS(71,'D',X,DA)</p>
<p>9</p></td>
<td>118-B</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>EXAMINATION STATUS</td>
<td>72</td>
<td><p>^RA(72,D0,0)</p>
<p>.01</p>
<p>^RA(72,'B',X,DA)</p>
<p>.01</p>
<p>^RA(72,'AA',</p></td>
<td>118-D</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>RAD/NUC MED REPORTS</td>
<td>74</td>
<td><p>^RARPT(</p>
<p>5</p>
<p>^RARPT(D0,'R',</p>
<p>.01</p>
<p>^RARPT(D0,'I',</p>
<p>.01</p>
<p>^RARPT(D0,'H',</p>
<p>.01</p></td>
<td>15-C</td>
<td><strong>P</strong></td>
</tr>
<tr class="odd">
<td>LAB LOINC</td>
<td>95.3</td>
<td>.01, 95.3</td>
<td>3557</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td>PROTOCOL</td>
<td>101</td>
<td>.01, 4</td>
<td>872</td>
<td><p><strong>C</strong></p>
<p>Direct read in the screen; pointed to.</p></td>
</tr>
<tr class="odd">
<td>GMRV VITAL MEASUREMENT</td>
<td>120.5</td>
<td><p>EN1^GMRVUTO</p>
<p>^PXRMINDX(120.5,"PI"</p></td>
<td><p>1446</p>
<p>4290</p></td>
<td><p><strong>C</strong></p>
<p><strong>C</strong></p></td>
</tr>
<tr class="even">
<td>PATIENT ALLERGIES</td>
<td>120.8</td>
<td><p>^GMR(120.8,D0,10,D1,0)</p>
<p>REACTION (10,.01)</p>
<p>OTHER REACTION (10,1)</p></td>
<td>190-B</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>FEE BASIS PAYMENT</td>
<td>162, sub-file 162.02</td>
<td>.01, 1.5</td>
<td>5107</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>FEE BASIS PAYMENT</td>
<td>162, sub-file 162.03</td>
<td>.01, 5, 16, 28, 30</td>
<td>5107</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>FEE BASIS PHARMACY INVOICE</td>
<td>162.1 sub-file 162.11</td>
<td>.01, 1, 2, 9, 1.5, 1.6, 15</td>
<td>5409</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>VA FORM 10-7078</td>
<td>162.4</td>
<td>3.5, 4.5</td>
<td>5104</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>FEE BASIS INVOICE</td>
<td>162.5</td>
<td>4, 5, 6, 6.5, 6.6, 8, 19, 24, 30, 31, 32, 33, 34, 40, 41, 42, 43, 44, 54</td>
<td>not yet available</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td>PATIENT MOVEMENT</td>
<td>405</td>
<td><p>.01, .03, .06, .17</p>
<p>^DGPM('AMV1',</p>
<p>^DGPM('ATT1',</p></td>
<td>1480</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td rowspan="2">ELECTROCARDIOGRAM (EKG)</td>
<td rowspan="2">691.5</td>
<td>GET^MCARAPI</td>
<td>3780</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td>GET^MDAPI1</td>
<td>3854</td>
<td><strong>P</strong></td>
</tr>
<tr class="odd">
<td>HL7 ERROR MESSAGE FILE</td>
<td>771.7</td>
<td>.01</td>
<td>4493</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td rowspan="6">VISIT</td>
<td rowspan="6">9000010</td>
<td></td>
<td>1905</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td><p>SELECTED^VSIT</p>
<p>(returns selected visits)</p></td>
<td><p>1900-F</p>
<p>1905</p></td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td><p>$$LOOKUP^VSIT</p>
<p>(looks up a visit and returns its information)</p></td>
<td><p>1900-G</p>
<p>1906</p></td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>HISTORIC^VSIT</td>
<td>1907</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td>ENCEVENT^PXKENC</td>
<td><p>1889-F</p>
<p>1894</p></td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>Access to the 'AA' x-ref</td>
<td>2309</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>V POV</td>
<td>9000010.07</td>
<td>POV^PXAPIIB</td>
<td>1554</td>
<td><strong>P</strong></td>
</tr>
<tr class="odd">
<td>V IMMUNIZATION</td>
<td>9000010.11</td>
<td>C x-ref, .01, .03, .06, .07, 1201, 1202, 81101</td>
<td>5521</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td>V SKIN</td>
<td>9000010.12</td>
<td>C x-ref, .01, .03, .04, .05, .06, 1201, 1202, 81101</td>
<td>5520</td>
<td><strong>P</strong></td>
</tr>
<tr class="odd">
<td rowspan="6">PROBLEM</td>
<td rowspan="6">9000011</td>
<td>ACTIVE^GMPLUTL</td>
<td>928</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>$$MOD^GMPLUTL3</td>
<td>2644</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>FileMan captioned output of entire PROBLEM record.</td>
<td>2308</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>GETFLDS^GMPLEDT3</td>
<td>2977</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td>Subscription to the DGPM MOVEMENT EVENTS protocol</td>
<td>1181</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td>GET^GMPLWP</td>
<td>4743</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td></td>
<td><p>9000010.18</p>
<p>9000010.23</p>
<p>9000010.11</p>
<p>9000010.16</p>
<p>9000010.07</p>
<p>9000010.06</p>
<p>9000010.12</p>
<p>9000010.15</p>
<p>9000010</p>
<p>9000010.13</p>
<p>9000010</p></td>
<td>Subscription to the PXK VISIT DATA EVENT protocol</td>
<td>1298</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Subscription to the LR7O ALL EVSEND RESULTS</td>
<td>3565</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>BHS^HLFNC3</td>
<td>4481</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>$$EMPL^DGSEC4</td>
<td>3646</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>BLDPID^VAFCQRY</td>
<td>3630</td>
<td><strong>C</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>EN^VAFHLZRD</td>
<td>4535</td>
<td><strong>P</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>$$EN^VAFHLZSP</td>
<td>4536</td>
<td><strong>P</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>ZERO^PSS50, NDF^PSS50, DATA^PSS50, AND^PSS50, ARWS^PSS50, VAC^PSS50</td>
<td>4533</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>SITE^VASITE</td>
<td>10112</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>ZERO^PSS52P6</td>
<td>4549</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>PSS432^PSS55, PSS436^PSS55</td>
<td>4826</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>ZERO^PSN50P6</td>
<td>4540</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>ZERO^PSN50PP41</td>
<td>4531</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>DATA^PSN50P68</td>
<td>4545</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>VAGN^PSNAPIS</td>
<td>2531</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>C^PSN50P65, IEN^PSN50P65</td>
<td>4543</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>LIST^DIC</td>
<td>2051</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>GET1^DIQ, GETS^DIQ</td>
<td>2056</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>FILE^DIC</td>
<td>2053</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>$$CODEN^ICDCODE</td>
<td>3990</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>EN^MXMLPRSE</td>
<td>4149</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>FMADD^XLFDT, FMDIFF^XLFDT, FMTE^XLFDT, DT^XLFDT, DOW^XLFDT, FMTH^XLFDT, FMTHL7^XLFDT, HL7TFM^XLFDT, HTFM^XLFDT, NOW^XLFDT, SCH^XLFDT</td>
<td>10103</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>EN1^RAO7PC1</td>
<td>2043</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>EN3^RAO7PC1</td>
<td>2265</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>10103</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>$$CODEN^ICPTCOD, $$CPT^ICPTCOD, CODEN^ICPTCOD</td>
<td>1995</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>ROOT^DILFD, VFILE^DILFD, EXTERNAL^DILFD, PRD^DILFD</td>
<td>2055</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>GETCPT^SDOE</td>
<td>2546</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>ACTIVE^SDQ, CLOSE^SDQ, DATE^SDQ, INDEX^SDQ, OPEN^SDQ, PAT^SDQ, SCAN^SDQ, SCANCB^SDQ</td>
<td>2548</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>ERRCHK^SDQUT</td>
<td>2552</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>$$ICDOP^ICDCODE</td>
<td>3990</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>ADM^VADPT2</td>
<td>325</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>2^VADPT, 4^VADPT, 51^VADPT, IN5^VADPT, SVC^VADPT</td>
<td>10061</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>TESTPAT^VADPT</td>
<td>3744</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^ICD9(</td>
<td>5388</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>EN^GMVPXRM</td>
<td>3647</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>GETIEN^GMVGETVT</td>
<td>5047</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>LN^XLFMTH, PWR^XLFMTH, MAX^XLFMTH, MIN^XLFMTH</td>
<td>10105</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>DEM^VADPT</td>
<td>10061</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>PWR^XLFMTH</td>
<td>10105</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>HL7TFM^XLFDT</td>
<td>10103</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>FIND^DIC, FIND1^DIC</td>
<td>2051</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>DQ^DICQ</td>
<td>10008</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>UPDATE^DIE, FILE^DIE, VAL^DIE</td>
<td>2053</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DIK, EN^DIK, ENALL^DIK, IX^DIK, IX1^DIK</td>
<td>10013</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>CODEABA^ICDEX, FILE^ICDEX, OBA^ICDEX, CODEC^ICDEX, CODEN^ICDEX, CSI^ICDEX, ICDDX^ICDEX, ICDOP^ICDEX, SNAM^ICDEX, VLTD^ICDEX, VSTD^ICDEX, VSTP^ICDEX</td>
<td>5747</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>UP^XLFSTR, TRIM^XLFSTR, LJ^XLFSTR</td>
<td>10104</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>BASE^XLFUTL, CNV^XLFUTL, DEC^XLFUTL</td>
<td>2622</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^%DT, DD^%DT</td>
<td>10003</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>C^%DTC, NOW^%DTC, YMD^%DTC</td>
<td>10000</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^%ZIS, HOME^%ZIS</td>
<td>10086</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^%ZISC</td>
<td>10089</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>DEL^%ZISH, LIST^%ZISH, CLOSE^%ZISH, OPEN^%ZISH</td>
<td>2320</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^%ZTLOAD,$$S^%ZTLOAD, DQ^%ZTLOAD, ISQED^%ZTLOAD, RTN^%ZTLOAD, STAT^%ZTLOAD</td>
<td>10063</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>EN^DDIOL</td>
<td>10142</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>WIN^DGPMDDCF</td>
<td>1246</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>PTR2CODE^DGUTL4</td>
<td>3799</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>BLD^DIALOG, MSG^DIALOG</td>
<td>2050</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DIC</td>
<td>10006</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>FILE^DICN</td>
<td>10109</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>GET1^DID</td>
<td>2051</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DIE</td>
<td>10018</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>CREF^DILF, IENS^DILF, OREF^DILF, CLEAN^DILF, DA^DILF, DT^DILF, LOCK^DILF</td>
<td>2054</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DIM</td>
<td>10016</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DIR</td>
<td>10026</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>EN^DIU2</td>
<td>10014</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DIWP</td>
<td>10011</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DIWW</td>
<td>10029</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>INIT^HLFNC2, MSH^HLFNC2</td>
<td>2161</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>GENERATE^HLMA</td>
<td>2164</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>CREATE^HLTF</td>
<td>10108</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>MSGACT^HLUTIL, MSGSTAT^HLUTIL</td>
<td>3098</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>ICDDATA^ICDXCODE, ICDDESC^ICDXCODE</td>
<td>5699</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>IMRDEV^IMREDIT</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>ACESSERR^IMRERR</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>CYPATH^LA7UTL02</td>
<td>4344</td>
<td><strong>C</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>IMPDATE^LEXU</td>
<td>5679</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>IFLOCAL^MPIF001</td>
<td>2701</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>XMLHDR^MXMUTL</td>
<td>4153</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^XMD</td>
<td>10070</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>SENDMSG^XMXAPI</td>
<td>2729</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>ADD^XPAR, DEL^XPAR, GETLST^XPAR, GETWP^XPAR, PUT^XPAR, REP^XPAR</td>
<td>2263</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>UPDATE^XPDID</td>
<td>2172</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>COMPCP^XPDUTL,LAST^XPDUTL,NEWCP^XPDUTL,PATCH^XPDUTL,VERCP^XPDUTL,VERSION^XPDUTL,BMES^XPDUTL,MES^XPDUTL</td>
<td>10141</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>SETUP^XQALERT</td>
<td>10081</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>IEN^XUAF4, NS^XUAF4</td>
<td>2171</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>DTIME^XUP</td>
<td>4409</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>PROD^XUPROD</td>
<td>4440</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>H^XUS</td>
<td>10044</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>KILL^XUSCLEAN</td>
<td>10052</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>OWNSKEY^XUSRB</td>
<td>3277</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>OPTSTAT^XUTMOPT</td>
<td>1472</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>BROKER^XWBLIB</td>
<td>2198</td>
<td><strong>S</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>RTRNFMT^XWBLIB</td>
<td>2238</td>
<td><strong>S</strong></td>
</tr>
<tr class="odd">
<td colspan="5"><strong>* Comments: C = Controlled; P = Private; S = Supported</strong></td>
</tr>
</tbody>
</table>

<span id="_Toc165646521" class="anchor"></span>Table 66 – Observation/Result Segment

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no internal relations with this software.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables in this software

# Registry Selection Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Registry Selection Rules in Section 11 of the Clinical Case Registries *User Manual* for the lists of ICD-9, ICD-10 and LOINC codes used to populate the individual registries.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only users with CCR [security keys](#Glos_SecurityKeys) have access to the registries.

CCR transmits data to the national database through the VA network. This network has security protection in place.

All patients' Social Security Numbers (SSNs) are encrypted before transmission to an agreed-upon standard. The fields sent to CDCO become readable upon receipt of the data; however, only high-level users have access to the unencrypted fields when viewing the national database.

## Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system produces the following VA Alerts:

|                                                                               |                                        |
|-------------------------------------------------------------------------------|----------------------------------------|
| Alert                                                                         | Addressee                              |
| When an access violation occurs                                               | Coordinators                           |
| When the first update is completed (an e-mail is also sent to the mail group) | Initiator of the setup                 |
| When a report (or a generic task) is ready                                    | Initiator of the report (generic task) |
| Unsent HL7 message (an e-mail is also sent to the mail group)                 | Coordinators                           |
| Problems with the nightly task                                                | Coordinators                           |
| Historical data extraction task finished                                      | Initiator of the task                  |
| Error during the pre- or post-install (if scheduled)                          | Initiator of the build installation    |

<span id="_Toc165646522" class="anchor"></span>Table 67 – Common Order Segment

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data will be transmitted to the National CCR Registry via the [VistA](#Glos_VistA) [HL7](#Glos_HL7) system.

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites utilizing CCR should develop a local contingency plan to be used in the event of product problems in a live environment. The facility contingency plan must identify the procedure for maintaining functionality provided by this package in the event of system outage. Field station Information Security Officers (ISOs) may obtain assistance from their Regional Information Officer (RISO).

## Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No interfacing is used in the CCR software.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No electronic signatures are used in the CCR software.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users must have a valid VistA account and must be assigned at least one of the following VistA [security keys](#Glos_SecurityKeys):

- ROR VA GENERIC USER or ROR VA GENERIC ADMIN
- ROR VA HEPC USER or ROR VA HEPC ADMIN
- ROR VA HIV USER or ROR VA HIV ADMIN
- ROR VA IRM

Users with the ROR VA HIV/HEPC USER key will be displayed on the Show Registry Users window as "User."

> ![](ror-1-5-42-technical-manual-security-guide/047.png) *Users* will have GUI access that will enable them to run reports for the specified registry. The ROR VA GENERIC USER key grants the user access to the local registries added in Patch 18 and subsequent patches.

Users with this security key will be able to run reports.

Users with the ROR VA HIV/HEPC ADMIN key will be displayed on the Show Registry Users window as "Administrator."

> ![](ror-1-5-42-technical-manual-security-guide/048.png) *Administrators* will have full GUI access that will enable them to run reports, create local fields, and edit, confirm and delete patient records for the specified registry. The ROR VA GENERIC ADMIN key grants the user administration access to the local registries added in Patch 18 and subsequent patches..

Users with the ROR VA IRM key will be displayed on the Show Registry Users window as "[IRM](#Glos_IRM)."

> ![](ror-1-5-42-technical-manual-security-guide/049.png) *IRM Users* with this security key will have access to all CCR files in VistA but no access to the GUI. This key should be assigned to the IRM personnel authorized to maintain and troubleshoot the CCR package.

If any unauthorized users access this system, a VA alert will be sent to persons identified to receive registry notifications stating the date and time of the violation, the name of the user who attempted to access the system, and a record of the access violation will be written to the Access Violations folder of the Technical Log.

![](ror-1-5-42-technical-manual-security-guide/050.png)Note: Only users having these keys can access the records of the ROR REGISTRY RECORD (#798), ROR REGISTRY PARAMETERS (#798.1), ROR PATIENT (#798.4), ROR LOG (#798.7), ROR TASK (#798.8), and ROR HIV RECORD (#799.4) files via FileMan.

1.  Creating an Output Directory in Windows
    1.  Graphical User Interface
1.  Double-click the My Computer icon on the desktop.
2.  Choose a drive, then right-click the drive icon and select Properties from the pop-up menu.
3.  Make sure that the drive has enough free space for the new directory (about 500Mb), then click Cancel to close the Properties window.
4.  Double-click the drive icon.
5.  From the File menu, select New \| Folder, then type RORHDT over the New Folder name.
6.  Press \< Enter \>.
7.  Close the window.
    1.  Command Prompt
1.  From the Start menu, select Run…. The Run dialog box appears.  
    > ![](ror-1-5-42-technical-manual-security-guide/051.png)
2.  In the Open: field, enter CMD and click \< OK \>.  
    > The Command Prompt window opens:  
    > ![](ror-1-5-42-technical-manual-security-guide/052.png)  
    >   
    > In most cases, the current drive will be C: and you will see the C:\\ prompt. To create the directory on a different drive, type the letter of the drive followed by a colon (e.g., "D:"), and then press \< Enter \>.
3.  At the command prompt, type the DIR command followed by \< Enter \> to make sure that the drive has enough free space (about 500Mb). Look for a message like this at the end of the output: "N Dir(s) nn,nnn,nnn bytes free."  
    > ![](ror-1-5-42-technical-manual-security-guide/053.png)
4.  Type MKDIR followed by a space and the name of directory \RORHDT and press \< Enter \>.
5.  Type DIR \RORHDT and press \< Enter \> to make sure that the directory has been created.  
      
    C:\\D:  
      
    D:\\DIR  
    Volume in drive D is DATA  
    Volume Serial Number is 924D-6524  
      
    Directory of D:\\  
      
    12/18/2001 10:48a \<DIR\> CacheSys  
    08/30/2001 01:37p \<DIR\> VISTA  
    2 Dir(s) 16,823,896,064 bytes free  
      
    D:\\MKDIR \RORHDT  
      
    D:\\DIR \RORHDT  
      
    D:\\DIR \RORHDT  
    Volume in drive D is DATA  
    Volume Serial Number is 924D-6524  
      
    Directory of D:\RORHDT  
      
    05/08/2002 09:32a \<DIR\> .  
    05/08/2002 09:32a \<DIR\> ..  
    0 File(s) 0 bytes  
    2 Dir(s) 16,823,896,064 bytes free  
      
    D:\\
6.  Type EXIT and press \< Enter \> to close the command prompt window.

# <span id="App_B" class="anchor"></span>Using the Windows FTP Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

    1.  Transmit Using FTP Client

Use these steps to transmit the data using the Windows NT/2000/XP/7 FTP client (see Windows documentation and/or online help for more details):

1.  From the Start menu, select Run…
2.  In the Open: field, enter FTP and click \< OK \>.  
    > The FTP client window opens and the ftp\> prompt is displayed.  
    > ![](ror-1-5-42-technical-manual-security-guide/054.png)
3.  Enter the OPEN command with the IP address 10.168.97.208 as a parameter;
4.  At the Name (…): prompt, enter your user name.
5.  At the Password: prompt, enter your password. The characters of the password will not be displayed on the screen.
6.  Use the BIN command to change the transfer mode to binary, then initiate transfer of historical data files (\*.HDT) from the output directory using the MPUT command:  
    > FTP\> MPUT *{disk and directory name}*\\.HDT
7.  Confirm transmission of each file by pressing \< Enter \>.
8.  Use the QUIT command to disconnect and exit the FTP client.

The following screen capture shows a typical Windows FTP session:

<table>
<caption><p><span id="_Toc165646523" class="anchor"></span>Table 68 – Patient ID Segment</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ftp&gt; OPEN x.x.x.x</p>
<p>Connected to x.x.x.x.</p>
<p>220 Palo Alto CQM0 Server</p>
<p>User (x.x.x.x): {your username}</p>
<p>331 Please specify the password.</p>
<p>Password: {your password}</p>
<p>230 Login successful.</p>
<p>ftp&gt; BIN</p>
<p>200 Switching to Binary mode.</p>
<p>ftp&gt; MPUT D:\RORHDT\*.HDT</p>
<p>mput d:\rorhdt\ROR-605-01.HDT? &lt;RET&gt;</p>
<p>200 PORT command successful. Consider using PASV.</p>
<p>150 Ok to send data.</p>
<p>226 File receive OK.</p>
<p>ftp: 93003 bytes sent in 0.84Seconds 110.59Kbytes/sec.</p>
<p>mput d:\rorhdt\ROR-605-02.HDT? &lt;RET&gt;</p>
<p>200 PORT command successful. Consider using PASV.</p>
<p>150 Ok to send data.</p>
<p>226 File receive OK.</p>
<p>ftp: 91391 bytes sent in 0.98Seconds 93.25Kbytes/sec.</p>
<p>ftp&gt; QUIT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc165646523" class="anchor"></span>Table 68 – Patient ID Segment

> **NOTE:** If you need to transmit or retransmit a single file, use the PUT command:

ftp\> PUT {disk and directory name}\\{file name}

Example:

| ftp\> PUT D:\RORHDT\\ ROR-605-01.HDT |
|--------------------------------------|

<span id="_Toc165646524" class="anchor"></span>Table 69 – Patient Visit Segment

# HL7 Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR package sends patient data to the national registry as [HL7](#Glos_HL7) batch messages of CSU type. Each patient will be transmitted as an individual CSU message within the batch message.

1.  Typographic Conventions

The following conventions are specific *to this appendix only*. See paragraph 1 above for other typographic conventions.

- The HL7 segments in the table are color-coded according to their purpose:
  - HL7 structure segments are highlighted in 15% gray (BHS, MSH, and BTS).
  - Patient demographic data segments are highlighted in light green (PID, ZSP, and ZRD).
  - Patient's clinical data (registry-independent) segments are highlighted in turquoise (OBR, OBX, ORC, and RXE).
  - Patient's registry-specific data segments are highlighted in ivory (CSP, CSS, OBR, and OBX).
- Square brackets \[ \] denote optional segments (groups of segments).
- Curly brackets { } denote repeatable segments (groups of segments).
  1.  CSU – Clinical Trials Message (Event type C09)

The function of this message is to pass information relating to patients on the locally identified registries to a centralized database. The message includes patient demographics; registry information; and relevant clinical data.

1.  Normalized Structure of the CSU Message

<table>
<caption><p><span id="_Toc165646525" class="anchor"></span>Table 70 – Pharmacy/Treatment Encoded Order Segment</p></caption>
<colgroup>
<col style="width: 1%" />
<col style="width: 1%" />
<col style="width: 1%" />
<col style="width: 1%" />
<col style="width: 1%" />
<col style="width: 14%" />
<col style="width: 27%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><strong>Segment ID</strong></th>
<th><strong>Description</strong></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="6"><p><a href="#_BHS_–_Batch">BHS</a></p>
<p>{</p></td>
<td>Batch Header</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td colspan="5"><p><a href="#_MSH_–_Message_Header_Segment">MSH</a></p>
<p>{</p></td>
<td>Message Header</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="4"><a href="#_PID_–_Patient">PID</a></td>
<td>Patient Identification</td>
<td>Patient Demographics</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="4">[ <a href="#_ZSP_–_Service_1">ZSP</a> ]</td>
<td>Service Period</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="4">[ { <a href="#_ZRD_–_Rated_Disabilities_Segment">ZRD</a> } ]</td>
<td>Rated Disabilities</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="4">[ { <a href="#_ZSP_–_Service">PV1</a> } ]</td>
<td>Patient visit</td>
<td>Admissions/Outpatient data</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="4"><p><a href="#_CSR_–_Clinical_Study_Registration_S">CSR</a></p>
<p>[ {</p></td>
<td>Clinical Study Registration</td>
<td>Clinical Case Registry data</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="3"><p><a href="#_CSP_–_Clinical_Study_Phase_Segment">CSP</a></p>
<p>{</p></td>
<td>Clinical Study Phase</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2">[ {</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><a href="#_OBR">OBR</a></td>
<td>Observation Request</td>
<td rowspan="2">Inpatient/Outpatient, Radiology, Autopsy, Surgical Pathology, Cytopathology, Microbiology, Medical Procedures (EKG), Allergy, Immunization, IV, Skin Test, Vitals, Problem List, and Laboratory data</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>{ <a href="#_OBX_–_Observation/Result_Segment">OBX</a> }</td>
<td>Observation/Result</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><p>} ]</p>
<p>[ {</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><a href="#_ORC_–_Common_Order_Segment">ORC</a></td>
<td>Common Order</td>
<td rowspan="2">Pharmacy/Drug data</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>{ <a href="#_RXE_–_Pharmacy/Treatment_Encoded_Or">RXE</a> }</td>
<td>Pharmacy/Treatment Encoded Order</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2">} ]</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2">[</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>{ <a href="#_ORC_–_Common_Order_Segment">ZIN</a> }</td>
<td>Inpatient</td>
<td rowspan="3">Purchased Care data</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>{ <a href="#_RXE_–_Pharmacy/Treatment_Encoded_Or">ZSV</a> }</td>
<td>Outpatient</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>{ <a href="#_RXE_–_Pharmacy/Treatment_Encoded_Or">ZRX</a> }</td>
<td>Pharmacy</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2">]</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="3">}</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="4">} ]</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="5">}</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="6"><p>}</p>
<p><a href="#_BTS_–_Batch">BTS</a></p></td>
<td>Batch Trailer</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc165646525" class="anchor"></span>Table 70 – Pharmacy/Treatment Encoded Order Segment

2.  Expanded Structure of the CSU Message

<table style="width:100%;">
<caption><p><span id="_Toc165646526" class="anchor"></span>Table 71 – Rated Disabilities Segment</p></caption>
<colgroup>
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 15%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 38%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4"><strong>Segment ID</strong></td>
<td colspan="3"><strong>Description</strong></td>
<td colspan="3"><strong>Comments</strong></td>
</tr>
<tr class="even">
<td colspan="4"><a href="#_BHS_–_Batch">BHS</a></td>
<td colspan="3">Batch Header</td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"><p><a href="#_MSH_–_Message_Header Segment">MSH</a></p>
<p>{</p></td>
<td colspan="3">Message Header</td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><a href="#_PID_–_Patient_ID Segment">PID</a></td>
<td colspan="3">Pseudo-patient Identification</td>
<td colspan="3" rowspan="2"><p><strong>Registry State</strong></p>
<p>This group of segments is sent for each registry included in the data transmission.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><a href="#_CSR_–_Clinical_Study Registration S">CSR</a></td>
<td colspan="3">Clinical Study Registration</td>
</tr>
<tr class="even">
<td></td>
<td colspan="3">}</td>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="4">[ {</td>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"><p><a href="#_MSH_–_Message_Header Segment">MSH</a></p>
<p>[</p></td>
<td colspan="3">Message Header</td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><a href="#_PID_–_Patient">PID</a></td>
<td colspan="3">Patient Identification</td>
<td colspan="2" rowspan="12"><p><strong>Patient's Demographic and Clinical Data</strong></p>
<p>This group of segments is sent only if the corresponding data has been modified/added since the last data transmission.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="3">[ <a href="#_ZSP_–_Service_1">ZSP</a> ]</td>
<td colspan="3">Service Period</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3">[ { <a href="#_ZRD_–_Rated_Disabilities Segment">ZRD</a> } ]</td>
<td colspan="3">Rated Disabilities</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="3">[ { <a href="#_ZSP_–_Service">PV1</a> } ]</td>
<td colspan="3">Patient visit</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><a href="#_CSR_–_Clinical_Study Registration S">CSR</a></td>
<td colspan="3">Clinical Study Registration</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="3">[ {</td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><a href="#_OBR">OBR</a></td>
<td colspan="3">Observation Request</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2">{ <a href="#_OBX_–_Observation/Result_Segment">OBX</a> }</td>
<td colspan="3">Observation/Result</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><p>} ]</p>
<p>[ {</p></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2"><a href="#_ORC_–_Common_Order Segment">ORC</a></td>
<td colspan="3">Common Order</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2">{ <a href="#_RXE_–_Pharmacy/Treatment_Encoded Or">RXE</a> }</td>
<td colspan="3">Pharmacy/Treatment Encoded Order</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="3">} ]</td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"><p>]</p>
<p>[ {</p></td>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="4"><a href="#_PID_–_Patient">PID</a></td>
<td colspan="3">Patient Identification</td>
<td rowspan="3"><p><strong>Patient's Registry Data</strong></p>
<p>This group of segments contains the patient's registry data. It is sent for each registry included in the transmission if the patient belongs to that registry.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="4"><a href="#_CSR_–_Clinical_Study Registration S">CSR</a></td>
<td colspan="3">Clinical Study Registration</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="4">{ <a href="#_CSP_–_Clinical_Study Phase Segment">CSP</a> }</td>
<td colspan="3">Clinical Study Phase</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3">} ]</td>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="4"><p>} ]</p>
<p><a href="#_BTS_–_Batch">BTS</a></p></td>
<td colspan="3">Batch Trailer</td>
<td colspan="3"></td>
</tr>
</tbody>
</table>

<span id="_Toc165646526" class="anchor"></span>Table 71 – Rated Disabilities Segment

3.  Sample CSU Message

<span class="mark">BHS</span>\|^~\\\|ROR SITE\|640^PALO-ALTO.XXX.XXX.XXX^DNS\|ROR AAC\|

\|20050303020252-0800\|\|^P^CSU~C09^2.4^AL^NE\|\|64038648827\|

<span class="mark">MSH</span>\|^~\\\|ROR SITE\|\|\|\|\|\|CSU^C09^CSU_C09\|640105760888-1

\|P\|2.4\|\|\|AL\|NE\|USA

PID\|1\|\|0^^^^U\|\|PSEUDO^PATIENT

CSR\|VA HEPC^1.5\|\|640^PALO ALTO HCS^99VA4\|0^^^^U^3^20

PID\|1\|\|0^^^^U\|\|PSEUDO^PATIENT

CSR\|VA HIV^1.5\|\|640^PALO ALTO HCS^99VA4\|0^^^^U^0^101

<span class="mark">MSH</span>\|^~\\\|ROR SITE\|\|\|\|\|\|CSU^C09^CSU_C09\|640105760888-2

\|P\|2.4\|\|\|AL\|NE\|US

PID\|1\|\|1243567890V123456^^^USVHA&&0363^NI^VA FACILITY ID&640&L~325500^^^USVHA&&0363^PI^VA FACILITY ID&640&L\|\|\|\|19630408\|M\|\|2106-3-SLF^WHITE^0005^2106-3^WHITE^CDC\|^^^^95123\|\|\|\|\|\|\|\|00007600044\| \|\|2186-5-SLF^NOT HISPANIC OR LATINO^0189^2186-5^NOT HISPANIC OR LATINO^CDC\|\|\|\|\|\|\|""

ZSP\|1\|1\|30\|8\|""\|0\|0\|19700325

ZRD\|1\|7709^HODGKINS DISEASE\|100\|1

PV1\|1\|O\|640^^^^^408\|P\|\|\|10935^^^^^^^^^^^^PHYSICIAN\|\|\|\|\|\|\|\|\|\|\|

\|8710273\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|200403020815-0800\|\|\|\|\|\|0

CSR\|CCR^1.5\|\|640^PALO ALTO HCS^99VA4\|325500^^^USVHA^PI

OBR\|1\|\|45353453\|OP^Outpatient^C4\|\|\|1997040593-000600\|\|\|\|\|\|\|\|\|\|\|\|

\|\|\|\|\|PHY\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|499^HINES OIFO^99VA4

OBR\|2\|\|110120021658\|93000^ELECTROCARDIOGRAM^C4\|\|199504151100-0600\|199505161100-0600\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|EC\|F\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

\|612GF^MARTINEZ OPC/CREC^99VA4

OBX\|1\|FT\|INT^Interpretation^VA080\|CHANGES OR SERIAL\|RECOMMEND CLINICAL CORRELATION\|\|\|\|\|\|F

OBX\|2\|FT\|AUTO^Auto Instrument^VA080\|\|This is the Auto-Instrument Diagnosis, which is a free text word processing field

OBR\|3\|\|2050600309\|81129.0000^Hepatic Function Panel^99VA64\|\|

\|20050301101656-0800\|\|\|\|A\|^\|\|20050301101656-0800\|SER&SER/PLAS&HL7&SER/PLAS&SER/PLAS&LN\|30890\|\|\|\|87712\S\CH\S\6949697.898344\|\|20050301111748-0800\|\|LAB\|

OBX\|3\|\|777-3^PLATELETS:NCNC:PT:BLD:QN:AUTOMATED COUNT^LN

^85570.0000^Platelet Count Whole Blood^99VA64\|\|3.6\|g/dL\|3.3-4.8\|\|\|\|F\|\|2\|20020129082501-0700\|612GF^MARTINEZ O PC/CREC^99VA4

\|617-VA612GF^

OBX\|4\|\|LABC\|LCOMM\|Lab Comments go here\|\|\|\|\|\|F

ZIN\|36520\|20040408\|20040409\|1\|9153.70\|6445.16\|20040817\|DRG202\|20040408\|20040409\|1\|571.2\|456.20\|456.8\|305.1\|303.90\|42.33\|44.43ZSV\|2943-169-1-1\|20000908\|\|76091\|OPT SERVICES/TREATMENT FOR NSC DISABILITIES\|611.72\|OUTPATIENT HOSPITAL (22)ZRX\|8344-1\|6532803\|19931221\|CONDYLOX\|PODOFILOX 0.5% TOP SOLN\|0.5%\|1

PID\|2\|\|1243567890V123456^^^USVHA&&0363^NI^VA FACILITY ID&640&L~325500^^^USVHA&&0363^PI^VA FACILITY ID&640&L\|\|\|\|19630408\|M\|\|2106-3-SLF^WHITE^0005^2106-3^WHITE^CDC\|^^^^95123\|\|\|\|\|\|\|\|00007600044\| \|\|2186-5-SLF^NOT HISPANIC OR LATINO^0189^2186-5^NOT HISPANIC OR LATINO^CDC\|\|\|\|\|\|\|""

CSR\|VA HEPC^1.5\|\|640^PALO ALTO HCS^99VA4

\|325500^^^USVHA^PI\|\|20040328\|\|\|\|7^Automatically Added - ICD9^99VA799_1\|\|0^NO~1^YES~1^YES~0^NO~0^NO~0^NO~0^NO~0

^NO~0^NO~0^NO~0^NO~0^NO~9^UNKNOWN

CSP\|0^UPDATE\|20050225020252-0800\|20050226020252-0800

CSP\|1^SELECT\|200502241415-0800

<span class="mark">BTS</span>\|2

2.  ACK – Commit Acknowledgement Message

The CCR uses original HL7 acknowledgment rules. The responding application is required to send only a commit acknowledgment when the message is received and safely stored.

1.  Structure of the Message

|                                              |                        |         |        |              |
|----------------------------------------------|------------------------|---------|--------|--------------|
| Segment ID                               | Description        | OPT | RP | Comments |
| [BHS](#_BHS_–_Batch)                         | Batch Header           | R       |        |              |
| [MSA](#_MSA_–_Message_Acknowledgment Segmen) | Message Acknowledgment | R       |        |              |
| [BTS](#_BTS_–_Batch)                         | Batch Trailer          | R       |        |              |

<span id="_Toc165646527" class="anchor"></span>Table 72 – Service Period Segment

2.  Sample ACK Message

<span class="mark">BHS</span>\|^~\\\|ROR AAC\|\|ROR SITE\|\|20050303020500\|\|^^ACK^2.4

\|CA\|23423423423\|64038648827

<span class="mark">MSA</span>\|CA\|64038648827

<span class="mark">BTS</span>\|1

  

4.  HL7 Segment Definitions
    1.  Typographic Conventions

The following conventions are specific *to this appendix only*. Additional conventions used in this section can be found in Section C.1, Typographic Conventions and in Section 1.1, Preface

Typographical Conventions Used in the Manual.

|                   |                                                                                                                                        |                   |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Notation          | Description                                                                                                                            | Example           |
| Bold          | Literal                                                                                                                                | DNS           |
| \<…\>             | Name that represents the corresponding value                                                                                           | \<Race Code\> |
| \[…\]             | Optional element(s)                                                                                                                    | \[ss\]            |
| \|                | Or                                                                                                                                     | +\|-      |
| DD                | Day (1-31)                                                                                                                             | 05                |
| MM                | Month (1-12)                                                                                                                           | 10                |
| N                 | Digit (0-9)                                                                                                                            |                   |
| YY                | 2-digit year                                                                                                                           | 05                |
| YYYY              | 4-digit year                                                                                                                           | 2005              |
| Hh                | Hours (0-23)                                                                                                                           | 15                |
| Mm                | Minutes (0-59)                                                                                                                         | 05                |
| Ss                | Seconds (0-59)                                                                                                                         | 43                |
| Zzzz              | Time zone                                                                                                                              | 0600              |
| Blue              | Hyperlink. You can click on it to open the corresponding section in this document, external document, or website.                      | [See Notes](\l)   |
| N/A               | Field, component, or sub-component is not used by the package. Usually, it is empty but might have a value, which will be ignored.     |                   |
| Example vs. Value | Description of an element contains either the Example or the Value row. In the latter case, the element always has the provided value. |                   |

<span id="_Toc165646528" class="anchor"></span>Table 73 – Inpatient Segment

2.  HL7 Segment Table Definitions

For each HL7 segment, the data elements contained in the segment are described in table format under Field Definitions in the following sections. The abbreviated column headings contained in the tables and associated HL7 data types are also defined.

| Column Heading | Definition                                               |
|----------------|----------------------------------------------------------|
| SEQ            | Sequence of data element in segment                      |
| LEN            | Maximum length of data element                           |
| DT             | Data Type                                                |
| OPT            | Required/Optional (R=Required, O=Optional)               |
| RP/#           | Repeats/Maximum number of repetitions (Y for repeats)    |
| TBL#           | Number of corresponding HL7 user defined/supported table |
| ELEMENT NAME   | HL7 Element Name with VistA file and field location      |

<span id="_Toc165646529" class="anchor"></span>Table 74 – Outpatient Segment

| Column Heading | Definition                                        |
|----------------|---------------------------------------------------|
| CE             | Coded Element                                     |
| ID             | Coded values for HL7 tables                       |
| SI             | Sequence ID                                       |
| TS             | Date/Time Stamp                                   |
| XCN            | Extended Composite ID number for name and persons |

<span id="_Toc165646530" class="anchor"></span>Table 75 – Drug Segment

| Value | Description                                        |
|-------|----------------------------------------------------|
| AU    | Audiology                                          |
| BG    | Blood gases                                        |
| BLB   | Blood bank                                         |
| CUS   | Cardiac Ultrasound                                 |
| CTH   | Cardiac catheterization                            |
| CT    | CAT scan                                           |
| CH    | Chemistry                                          |
| CP    | Cytopathology                                      |
| EC    | Electrocardiac (e.g., EKG, EEC, Holter)            |
| EN    | Electroneuro (EEG, EMG,EP,PSG)                     |
| HM    | Hematology                                         |
| ICU   | Bedside ICU Monitoring                             |
| IMG   | Diagnostic Imaging                                 |
| IMM   | Immunology                                         |
| LAB   | Laboratory                                         |
| MB    | Microbiology                                       |
| MCB   | Mycobacteriology                                   |
| MYC   | Mycology                                           |
| NMS   | Nuclear medicine scan                              |
| NMR   | Nuclear magnetic resonance                         |
| NRS   | Nursing service measures                           |
| OUS   | OB Ultrasound                                      |
| OT    | Occupational Therapy                               |
| OTH   | Other                                              |
| OSL   | Outside Lab                                        |
| PAR   | Parasitology                                       |
| PAT   | Pathology (gross and histopathology, not surgical) |
| PHR   | Pharmacy                                           |
| PT    | Physical Therapy                                   |
| PHY   | Physician (Hx. Dx, admission note, etc.)           |
| PF    | Pulmonary function                                 |
| RAD   | Radiology                                          |
| RX    | Radiograph                                         |
| RUS   | Radiology ultrasound                               |
| RC    | Respiratory Care (therapy)                         |
| RT    | Radiation therapy                                  |
| SR    | Serology                                           |
| SP    | Surgical Pathology                                 |
| TX    | Toxicology                                         |
| URN   | Urinalysis                                         |
| VUS   | Vascular Ultrasound                                |
| VR    | Virology                                           |
| XRC   | Cineradiograph                                     |

<span id="_Toc165646531" class="anchor"></span>Table 76 – HL-7 Tables

1.  Reference Table Values

Within the segment information are references to tables (TBL#), when applicable.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Format</th>
<th>Valid Values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;Station Number&gt;<strong>^</strong>&lt;Station Name&gt;<strong>^DNS</strong></td>
<td>640^PALO-ALTO.XXX.XXX.XXX^DNS</td>
</tr>
<tr class="even">
<td>YYYYMMDD[hhmm[ss]] [<strong>+</strong>|<strong>-</strong>zzzz]</td>
<td><p>20050303020252-0800</p>
<p>20050303020252</p>
<p>200503030202+0600</p>
<p>200503030202</p>
<p>20050303</p></td>
</tr>
</tbody>
</table>

3.  <span id="_BHS_–_Batch" class="anchor"></span>BHS – Batch Header Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL# | Field Name                  | CCR                                        |
|-----|-----|-----|-----|------|------|-----------------------------|--------------------------------------------|
| 1   | 1   | ST  | R   |      |      | Batch Field Separator       | [See Notes](#_BHS-1_Batch_Field_Separator) |
| 2   | 4   | ST  | R   |      |      | Batch Encoding Characters   | [See Notes](#_BHS-2_Encoding_Characters)   |
| 3   | 15  | ST  | R   |      |      | Batch Sending Application   | [See Notes](#_BHS-3_Sending_Application)   |
| 4   | 72  | ST  | R   |      |      | Batch Sending Facility      | [See Notes](#_BHS-4_Sending_Facility)      |
| 5   | 15  | ST  | R   |      |      | Batch Receiving Application | [See Notes](#_MSH-5_Receiving_Application) |
| 6   | 20  | ST  | O   |      |      | Batch Receiving Facility    | N/A                                        |
| 7   | 26  | TS  | R   |      |      | Batch Creation Date/Time    | [See Notes](#_MSH-6_Receiving_Facility)    |
| 8   | 40  | ST  | O   |      |      | Batch Security              | N/A                                        |
| 9   | 23  | ST  | R   |      |      | Batch Name/ID/Type          | [See Notes](#_MSH_–_Message)               |
| 10  | 80  | ST  | C   |      |      | Batch Comment               | [See Notes](#_BHS-10_Batch_Comment)        |
| 11  | 20  | ST  | R   |      |      | Batch Control ID            | [See Notes](#_BHS-11_Batch_Control_ID)     |
| 12  | 20  | ST  | C   |      |      | Reference Batch Control ID  | [See Notes](#_MSH_–_Message_1)             |

1.  Field Definitions
    1.  <span id="_BHS-1_Batch_Field_Separator" class="anchor"></span>BHS-1 Batch Field Separator

|             |                                                                                                                                                                                                                                           |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the separator between the segment ID and the first real field, *BHS-2 Batch Encoding Characters*. As such it serves as the separator and defines the character to be used as a separator for the rest of the message. |
| Value:      | \| (ASCII 124)                                                                                                                                                                                                                        |

2.  <span id="_BHS-2_Encoding_Characters" class="anchor"></span>BHS-2 Batch Encoding Characters

|             |                                                                                                                                                          |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains four characters in the following order: the component separator; repetition separator; escape character; and subcomponent separator. |
| Value:      | ^~\\ (ASCII 94, 126, 92, and 38, respectively)                                                                                                       |

3.  <span id="_BHS-3_Sending_Application" class="anchor"></span>BHS-3 Batch Sending Application

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Definition:</td>
<td>This field uniquely identifies the sending application among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site-defined.</td>
</tr>
<tr class="even">
<td>Value:</td>
<td><ul>
<li><p>ACK: <strong>ROR AAC</strong></p></li>
<li><p>CSU: <strong>ROR SITE</strong></p></li>
</ul></td>
</tr>
</tbody>
</table>

1.  <span id="_BHS-4_Sending_Facility" class="anchor"></span>BHS-4 Batch Sending Facility

|             |     |                                                                                                                                         |                |                   |                     |
|-------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------|----------------|-------------------|---------------------|
| SEQ         | DT  |                                                                                                                                         | TBL#           | Component Name    | CCR                 |
| 1           | IS  |                                                                                                                                         | [0362](#T0362) | Namespace ID      | Station Number      |
| 2           | ST  |                                                                                                                                         |                | Universal ID      | Station Domain Name |
| 3           | ID  |                                                                                                                                         | [0301](#T0301) | Universal ID Type | DNS             |
| Definition: |     | This field contains the address of one of several occurrences of the same application within the sending system. Entirely site-defined. |                |                   |                     |
| Value:      |     | 640^PALO-ALTO.XXX.XXX.XXX^DNS                                                                                                           |                |                   |                     |

2.  <span id="_MSH-5_Receiving_Application" class="anchor"></span>BHS-5 Batch Receiving Application

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Definition:</td>
<td>This field uniquely identifies the receiving application among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site-defined.</td>
</tr>
<tr class="even">
<td>Value:</td>
<td><ul>
<li><p>ACK: <strong>ROR SITE</strong></p></li>
<li><p>CSU: <strong>ROR AAC</strong></p></li>
</ul></td>
</tr>
</tbody>
</table>

1.  <span id="_MSH-6_Receiving_Facility" class="anchor"></span>BHS-7 Batch Creation Date/Time

|             |                                                                                                                                                                                |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the date/time that the sending system created the message. If the time zone is specified, it will be used throughout the message as the default time zone. |
| Value:      | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]                                                                                                                                    |
| Example:    | 20050303020252-0800                                                                                                                                                        |

2.  <span id="_MSH_–_Message" class="anchor"></span>BHS-9 Batch Name/ID/Type

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 11%" />
<col style="width: 38%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>DT</th>
<th>TBL#</th>
<th>Component Name</th>
<th>CCR</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>N/A</td>
</tr>
<tr class="even">
<td>2</td>
<td>ID</td>
<td><a href="#T0103">0103</a></td>
<td>Processing ID</td>
<td></td>
</tr>
<tr class="odd">
<td>3</td>
<td>ID</td>
<td></td>
<td>&lt;Message Type&gt;<strong>~</strong>&lt;Trigger Event&gt;</td>
<td></td>
</tr>
<tr class="even">
<td>4</td>
<td>ID</td>
<td>0104</td>
<td>Version ID</td>
<td><strong>2.4</strong></td>
</tr>
<tr class="odd">
<td>5</td>
<td>ID</td>
<td><a href="#T0155">0155</a></td>
<td>Accept ACK Type</td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>ID</td>
<td><a href="#T0155">0155</a></td>
<td>Application ACK Type</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Definition:</td>
<td colspan="3"><p>This field contains the <em>Processing ID</em>, <em>Message Type</em>, <em>Trigger Event</em>, and several other characteristics of the message. The CCR package sends a CSU message type with the trigger event C09.</p>
<p>The CCR package always requests the commit acknowledgement but it does not require the application acknowledgement.</p></td>
</tr>
<tr class="even">
<td colspan="2">Example:</td>
<td colspan="3"><ul>
<li><p>ACK: <strong>^P^ACK^2.4</strong></p></li>
<li><p>CSU: <strong>^P^CSU~C09^2.4^AL^NE</strong></p></li>
</ul></td>
</tr>
</tbody>
</table>

1.  <span id="_BHS-10_Batch_Comment" class="anchor"></span>BHS-10 Batch Comment

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Definition:</td>
<td>This field is a comment field that is not further defined in the HL7 protocol.</td>
</tr>
<tr class="even">
<td>Example:</td>
<td><ul>
<li><p>ACK: <strong>CA</strong></p></li>
<li><p>Historical CSU: <strong>HISTORICAL DATA</strong></p></li>
<li><p>Nightly CSU: N/A</p></li>
</ul></td>
</tr>
</tbody>
</table>

1.  <span id="_BHS-11_Batch_Control_ID" class="anchor"></span>BHS-11 Batch Control ID

|             |                                                                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field is used to uniquely identify a particular batch. It is echoed back in the *BHS-12 Reference Batch Control ID* field of the commit acknowledgement. |
| Example:    | 64038648827                                                                                                                                               |

2.  <span id="_MSH_–_Message_1" class="anchor"></span>BHS-12 Reference Batch Control ID

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Definition:</td>
<td>This field contains the value of <em>BHS-11 Batch Control ID</em> when this batch was originally transmitted.</td>
</tr>
<tr class="even">
<td>Value:</td>
<td><p>CSU: <strong>N/A</strong></p>
<p><strong>ACK:</strong> Value of BHS-11 Batch Control ID from the original CSU batch.</p></td>
</tr>
<tr class="odd">
<td>Example:</td>
<td><strong>64038648827</strong></td>
</tr>
</tbody>
</table>

1.  Sample BHS Segments
    1.  ACK

BHS\|[^~\\](#_BHS-2_Encoding_Characters)\|[ROR AAC](#_BHS-3_Sending_Application)\|\|[ROR SITE](#_MSH-5_Receiving_Application)\|\|[20050303020500](#_MSH-6_Receiving_Facility)[\|\|^^ACK^2.4](#_MSH_–_Message)

\|[CA](#_BHS-10_Batch_Comment)\|[23423423423](#_BHS-11_Batch_Control_ID)\|[64040054123](#_BHS-12_Reference_Batch_Control ID)

2.  CSU

BHS\|[^~\\](#_BHS-2_Encoding_Characters)\|[ROR SITE](#_BHS-3_Sending_Application)\|[640^PALO-ALTO.XXX.XXX.XXX^DNS](#_BHS-4_Sending_Facility)\|[ROR AAC](#_MSH-5_Receiving_Application)\|

\|[20050303020252-0800](#_MSH-6_Receiving_Facility)\|\|[^P^CSU~C09^2.4^AL^NE](#_MSH_–_Message)\|\|[64038648827](#_BHS-11_Batch_Control_ID)\|

1.  <span id="_BTS_–_Batch" class="anchor"></span>BTS – Batch Trailer Segment

|     |     |     |     |     |      |      |                     |                                    |
|-----|-----|-----|-----|-----|------|------|---------------------|------------------------------------|
| SEQ |     | LEN | DT  | OPT | RP/# | TBL# | Field Name          | CCR                                |
| 1   | 10  |     | ST  | R   |      |      | Batch Message Count | [See Notes](#_BTS-1_Batch_Message) |
| 2   | 80  |     | ST  | O   |      |      | Batch Comment       | N/A                                |
| 3   | 100 |     | NM  | O   | Y    |      | Batch Totals        | N/A                                |

1.  Field Definitions
    1.  <span id="_BTS-1_Batch_Message" class="anchor"></span>BTS-1 Batch Message Count

|             |                                                                                |
|-------------|--------------------------------------------------------------------------------|
| Definition: | This field stores the count of individual messages contained within the batch. |
| Example:    | 235                                                                        |

2.  Sample BTS Segment

BTS\|[235](#_BTS-1_Batch_Message)

2.  <span id="_CSP_–_Clinical_Study_Phase_Segment" class="anchor"></span>CSP – Clinical Study Phase Segment

| SEQ |     | LEN | DT  | OPT | RP/# | TBL# | Field Name                  | CCR                                  |
|-----|-----|-----|-----|-----|------|------|-----------------------------|--------------------------------------|
| 1   | 30  |     | CE  | R   |      |      | Study Phase Identifier      | [See Notes](#_CSP-1_Study_Phase)     |
| 2   | 26  |     | TS  | R   |      |      | Date/time Study Phase Began | [See Notes](#_CSP-2_Date/time_Study) |
| 3   | 26  |     | TS  | C   |      |      | Date/time Study Phase Ended | [See Notes](#_CSP-3_Date/time_Study) |
| 4   | 250 |     | CE  | C   |      |      | Study Phase Evaluability    | N/A                                  |

The CSP segments represent different registry-specific events, store the corresponding dates, and/or group the subsequent segments.

If a segment with a particular value of the *CSP-1 Study Phase ID* field is not present in the message, then the corresponding values in the national database should not be changed.

1.  Field Definitions
    1.  <span id="_CSP-1_Study_Phase" class="anchor"></span>CSP-1 Study Phase ID

| SEQ | DT  | TBL# | Component Name                  | CCR                 |
|-----|-----|------|---------------------------------|---------------------|
| 1   | ST  |      | Identifier                      | Registry Event Code |
| 2   | ST  |      | Text                            | Registry Event Name |
| 3   | ST  |      | Name of Coding System           | N/A                 |
| 4   | ST  |      | Alternate Identifier            | N/A                 |
| 5   | ST  |      | Alternate Text                  | N/A                 |
| 6   | ST  |      | Name of Alternate Coding System | N/A                 |

|             |                                                                                          |             |
|-------------|------------------------------------------------------------------------------------------|-------------|
| Definition: | This field indicates type of the registry-specific event represented by the CSP segment. |             |
| Tables:     | Identifier                                                                           | Text    |
|             | 0                                                                                    | UPDATE  |
|             | 1                                                                                    | SELECT  |
|             | 2                                                                                    | ADD     |
|             | 3                                                                                    | CONFIRM |
|             | 4                                                                                    | DELETE  |
|             | 5                                                                                    | CDC     |
| Example:    | 0^UPDATE                                                                             |             |

2.  <span id="_CSP-2_Date/time_Study" class="anchor"></span>CSP-2 Date/time Study Phase Began

|             |                                                                                 |                                                          |
|-------------|---------------------------------------------------------------------------------|----------------------------------------------------------|
| Definition: | Meaning of this field depends on the value of the *CSP-1 Study Phase ID* field: |                                                          |
|             | UPDATE                                                                      | Start date/time of the data extraction                   |
|             | SELECT                                                                      | Date/time of the earliest selection rule                 |
|             | ADD                                                                         | Date/time when the patient was added to the registry     |
|             | CONFIRM                                                                     | Date/time when the patient was confirmed in the registry |
|             | DELETE                                                                      | Date/time when the patient was deleted from the registry |
|             | CDC                                                                         | Date/time of CDC data modification                       |
| Format:     | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]                                     |                                                          |
| Example:    | 200502100920-0800                                                           |                                                          |

3.  <span id="_CSP-3_Date/time_Study" class="anchor"></span>CSP-3 Date/time Study Phase Ended

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Definition:</td>
<td>Meaning of this field depends on the value of the <em>CSP-1 Study Phase ID</em> field:</td>
</tr>
<tr class="even">
<td>Value:</td>
<td><p><strong>UPDATE:</strong> End date/time of the data extraction</p>
<p>Otherwise: N/A</p></td>
</tr>
<tr class="odd">
<td>Format:</td>
<td>YYYYMMDD[hhmm[ss]] [<strong>+</strong>|<strong>-</strong>zzzz]</td>
</tr>
<tr class="even">
<td>Example:</td>
<td><strong>200502101015-0800</strong></td>
</tr>
</tbody>
</table>

2.  Sample CSP segment

CSP\|[0^UPDATE](#_CSP-1_Study_Phase)\|[20010806010000-0600](#_CSP-2_Date/time_Study_Phase Began)\|[20010806015030-0600](#_CSP-3_Date/time_Study_Phase Ended)

3.  <span id="_CSR_–_Clinical_Study_Registration_S" class="anchor"></span>CSR – Clinical Study Registration Segment

| SEQ |     | LEN | DT  | OPT | RP/# | TBL# | Field Name                              | CCR                                                  |
|-----|-----|-----|-----|-----|------|------|-----------------------------------------|------------------------------------------------------|
| 1   | 60  |     | EI  | R   |      |      | Sponsor Study ID                        | [See Notes](#_CSR-1_Sponsor_Study_ID)                |
| 2   | 60  |     | EI  | O   |      |      | Alternate Study ID                      | N/A                                                  |
| 3   | 250 |     | CE  | R   |      |      | Institution Registering the Patient     | [See Notes](#_CSR-3_Institution_Registering_the P)   |
| 4   | 30  |     | CX  | R   |      |      | Sponsor Patient ID                      | [See Notes](#_CSR-4_Sponsor_Patient_ID)              |
| 5   | 30  |     | CX  | O   |      |      | Alternate Patient ID - CSR              | N/A                                                  |
| 6   | 26  |     | TS  | C   |      |      | Date/Time Of Patient Study Registration | [See Notes](#_CSR-6_Date/time_of_Patient Study Re)   |
| 7   | 250 |     | XCN | O   | Y    |      | Person Performing Study Registration    | N/A                                                  |
| 8   | 250 |     | XCN | C   | Y    |      | Study Authorizing Provider              | N/A                                                  |
| 9   | 26  |     | TS  | C   |      |      | Date/time Patient Study Consent Signed  | [See Notes](#_CSR-9_Date/time_Patient_Study Conse)   |
| 10  | 250 |     | CE  | C   |      |      | Patient Study Eligibility Status        | [See Notes](#_CSR-10_Patient_Study_Eligibility St_1) |
| 11  | 26  |     | TS  | O   | Y/3  |      | Study Randomization Date/time           | N/A                                                  |
| 12  | 250 |     | CE  | C   | Y    |      | Randomized Study Arm                    | [See Notes](#_CSR-12_Randomized_Study_Arm)           |
| 13  | 250 |     | CE  | O   | Y/3  |      | Stratum for Study Randomization         | N/A                                                  |
| 14  | 250 |     | CE  | C   |      |      | Patient Evaluability Status             | N/A                                                  |
| 15  | 26  |     | TS  | C   |      |      | Date/time Ended Study                   | N/A                                                  |
| 16  | 250 |     | CE  | C   |      |      | Reason Ended Study                      | N/A                                                  |

1.  Field Definitions
    1.  <span id="_CSR-1_Sponsor_Study_ID" class="anchor"></span>CSR-1 Sponsor Study ID

|     |     |      |                   |                              |
|-----|-----|------|-------------------|------------------------------|
| SEQ | DT  | TBL# | Component Name    | CCR                          |
| 1   | ST  |      | Entity Identifier | Registry Name                |
| 2   | IS  |      | Namespace ID      | Software Version Information |
| 3   | ST  |      | Universal ID      | N/A                          |
| 4   | ID  |      | Universal ID Type | N/A                          |

|             |                                                                                                            |                                                                                                                        |
|-------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field holds the internal registry name, the version number, and the build number of the CCR software: |                                                                                                                        |
|             | Clinical Data:                                                                                             | CCR^\<Version Major\>.\<Version Minor\>\[.\<Latest Patch Number\>\[.\<Build Number\>\]\]               |
|             | Otherwise:                                                                                                 | \<Registry Name\>^\<Version Major\>.\<Version Minor\>\[.\<Latest Patch Number\>\[.\<Build Number\>\]\] |
| Examples:   | Clinical Data:                                                                                             | CCR^1.5.2.1                                                                                                        |
|             | Otherwise:                                                                                                 | VA HIV^1.5.2.1                                                                                                     |

2.  CSR-3 Institution Registering the Patient

|     |     |      |                                 |                                 |
|-----|-----|------|---------------------------------|---------------------------------|
| SEQ | DT  | TBL# | Component Name                  | CCR                             |
| 1   | ST  | 0005 | Identifier                      | Station Number (without suffix) |
| 2   | ST  |      | Text                            | Institution Name                |
| 3   | ST  |      | Name of Coding System           | 99VA4                       |
| 4   | ST  |      | Alternate Identifier            | N/A                             |
| 5   | ST  |      | Alternate Text                  | N/A                             |
| 6   | ST  |      | Name of Alternate Coding System | N/A                             |

|             |                                                                        |
|-------------|------------------------------------------------------------------------|
| Definition: | This field distinguishes the station where the local registry is held. |
| Example:    | 640^PALO ALTO HCS^99VA4                                            |

3.  <span id="_CSR-4_Sponsor_Patient_ID" class="anchor"></span>CSR-4 Sponsor Patient ID

|     |     |                |                                |                                                                  |
|-----|-----|----------------|--------------------------------|------------------------------------------------------------------|
| SEQ | DT  | TBL#           | Component Name                 | CCR                                                              |
| 1   | ST  |                | ID                             | Patient IEN (DFN)                                                |
| 2   | ST  |                | Check Digit                    |                                                                  |
| 3   | ID  | [0061](#T0061) | Code of the Check Digit Scheme |                                                                  |
| 4   | HD  | 0363           | Assigning Authority            |                                                                  |
| 5   | ID  | [0203](#T0203) | Identifier Type Code           |                                                                  |
| 6   | HD  |                | Assigning Facility             | Number of pending patients                                       |
| 7   | DT  |                | Effective Date                 | Number of reports that have been run since the last transmission |
| 8   | DT  |                | Expiration Date                | N/A                                                              |

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="3">Definition:</td>
<td>Clinical Data:</td>
<td><p>Both patient's clinical and patient's registry CSR segments contain the Internal Entry Number (DFN) of the patient's record at the sending facility in this field:</p>
<blockquote>
<p>&lt;DFN&gt;^^^<strong>USVHA^PI</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>Registry Data:</td>
<td>See Clinical Data</td>
</tr>
<tr class="odd">
<td>Registry State:</td>
<td><p>CSR segments in the Registry State section of the batch utilize the following format of this field:</p>
<p><strong>0^^^^U^</strong>&lt;Number of Pending Patients&gt;<strong>^</strong>&lt;Number of Reports&gt;</p></td>
</tr>
<tr class="even">
<td rowspan="2">Examples:</td>
<td colspan="2"><strong>15^^^USVHA^PI</strong></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>0^^^^U^3^20</strong></td>
</tr>
</tbody>
</table>

4.  CSR-6 Date/time of Patient Study Registration

|             |                 |                                                 |
|-------------|-----------------|-------------------------------------------------|
| Definition: | Clinical Data:  | N/A                                             |
|             | Registry Data:  | Date when the patient was added to the registry |
|             | Registry State: | N/A                                             |
| Format:     | YYYYMMDD        |                                                 |
| Examples:   | 20050210    |                                                 |

5.  CSR-9 Date/time Patient Study Consent Signed

|             |                 |                                                                                                                                      |
|-------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | Clinical Data:  | N/A                                                                                                                                  |
|             | Registry Data:  | Date of the AIDS OI (Clinical AIDS) is sent in this field if the corresponding check-box is selected on the Patient Edit dialog box. |
|             | Registry State: | N/A                                                                                                                                  |
| Format:     | YYYYMMDD        |                                                                                                                                      |
| Examples:   | 20050210    |                                                                                                                                      |

6.  CSR-10 Patient Study Eligibility Status

| SEQ | DT  | TBL# | Component Name                  | CCR           |
|-----|-----|------|---------------------------------|---------------|
| 1   | ST  | 0005 | Identifier                      | Code          |
| 2   | ST  |      | Text                            | Description   |
| 3   | ST  |      | Name of Coding System           | 99VA799_1 |
| 4   | ST  |      | Alternate Identifier            | N/A           |
| 5   | ST  |      | Alternate Text                  | N/A           |
| 6   | ST  |      | Name of Alternate Coding System | N/A           |

|             |                                             |                                                    |
|-------------|---------------------------------------------|----------------------------------------------------|
| Definition: | Clinical Data:                              | N/A                                                |
|             | Registry Data:                              | Reason for addition of the patient to the registry |
|             | Registry State:                             | N/A                                                |
| Tables:     | Code                                    | Description                                    |
|             | 7                                       | Automatically Added - ICD9                         |
|             | 8                                       | Reason for addition of the patient to the registry |
|             | 9                                       | Automatically Added - ICD9 and Lab                 |
| Example:    | 7^Automatically Added - ICD9^ 99VA799_1 |                                                    |

7.  <span id="_CSR-12_Randomized_Study_Arm" class="anchor"></span>CSR-12 Randomized Study Arm

|     |     |      |                                 |             |
|-----|-----|------|---------------------------------|-------------|
| SEQ | DT  | TBL# | Component Name                  | CCR         |
| 1   | ST  | 0005 | Identifier                      | Code        |
| 2   | ST  |      | Text                            | Description |
| 3   | ST  |      | Name of Coding System           | N/A         |
| 4   | ST  |      | Alternate Identifier            | N/A         |
| 5   | ST  |      | Alternate Text                  | N/A         |
| 6   | ST  |      | Name of Alternate Coding System | N/A         |

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="3">Definition:</td>
<td>Clinical Data:</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Registry Data:</td>
<td>Risk factors. 14<sup>th</sup> component indicates whether this site was the first site (VA or Non-VA) to diagnose HIV in the patient. Number of repetitions is registry-specific.</td>
</tr>
<tr class="odd">
<td>Registry State:</td>
<td>N/A</td>
</tr>
<tr class="even">
<td rowspan="4">Tables:</td>
<td><strong>Code</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="odd">
<td><strong>0</strong></td>
<td>NO</td>
</tr>
<tr class="even">
<td><strong>1</strong></td>
<td>YES</td>
</tr>
<tr class="odd">
<td><strong>9</strong></td>
<td>UNKNOWN</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><ul>
<li><p>0^NO~1^YES~1^YES~0^NO~0^NO~0^NO~0^NO~0^NO~0^NO~0^NO~0^NO~1^YES</p></li>
<li><p>0^NO~9^UNKNOWN</p></li>
<li><p>~~~~~~~~~~~~~9^UNKNOWN</p></li>
</ul></td>
</tr>
</tbody>
</table>

1.  Sample CSR segment

CSR\|[VA HEPC^1.5](#_CSR-1_Sponsor_Study_ID)\|\|[640^PALO ALTO HCS^99VA4](#_CSR-3_Institution_Registering_the P)\|[325500^^^USVHA^PI](#_CSR-4_Sponsor_Patient_ID)\|

\|[20040328](#_CSR-6_Date/time_of_Patient Study Re)\|\|\|[20050210](#_CSR-10_Patient_Study_Eligibility St)\|[7^Automatically Added - ICD9^99VA7991](#_CSR-10_Patient_Study_Eligibility St_1)\|

\|[0^NO~1^YES~1^YES~0^NO~0^NO~0^NO~0^NO~0^NO~0^NO~0^NO~0^NO~0^NO~9^UNKNOWN](#_CSR-12_Randomized_Study_Arm)~1^YES

1.  MSA – Message Acknowledgment Segment

|     |     |     |     |      |                |                             |                      |
|-----|-----|-----|-----|------|----------------|-----------------------------|----------------------|
| SEQ | LEN | DT  | OPT | RP/# | TBL#           | Field Name                  | CCR                  |
| 1   | 2   | ID  | R   |      | [0008](#T0008) | Acknowledgment Code         | [See Notes](#_MSA-1) |
| 2   | 20  | ST  | R   |      |                | Message Control ID          | [See Notes](#_MSA-2) |
| 3   | 80  | ST  | O   |      |                | Text Message                | [See Notes](#_MSA-3) |
| 4   | 15  | NM  | O   |      |                | Expected Sequence Number    | N/A                  |
| 5   | 1   | ID  | B   |      | 0102           | Delayed Acknowledgment Type | N/A                  |
| 6   | 250 | CE  | O   |      | 0357           | Error Condition             | N/A                  |

1.  Field Definitions
    1.  <span id="_MSA-1" class="anchor"></span>MSA-1 Acknowledgment Code

|             |                                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------|
| Definition: | This field holds the acknowledgment code, which defines whether the message was accepted or rejected. |
| Example:    | CA                                                                                                |

2.  <span id="_MSA-2" class="anchor"></span>MSA-2 Message Control ID

|             |                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the message control ID of the message sent by the sending system. This allows the sending system to associate the response with the original message. |
| Example:    | 64038648827                                                                                                                                                           |

3.  <span id="_MSA-3" class="anchor"></span>MSA-3 Text Message

|             |                                                                                         |
|-------------|-----------------------------------------------------------------------------------------|
| Definition: | This field will describe an error condition in the event of an AE or AR being returned. |

2.  Sample MSA Segment

MSA\|[CA](#_MSA-1)\|[64038648827](#_MSA-2)

2.  <span id="_MSH_–_Message_Header_Segment" class="anchor"></span>MSH – Message Header Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL#           | Field Name                              | CCR                                              |
|-----|-----|-----|-----|------|----------------|-----------------------------------------|--------------------------------------------------|
| 1   | 1   | ST  | R   |      |                | Field Separator                         | [See Notes](#_MSH-1_Field_Separator_1)           |
| 2   | 4   | ST  | R   |      |                | Encoding Characters                     | [See Notes](#_MSH-2_Encoding_Characters)         |
| 3   | 180 | HD  | O   |      | 0361           | Sending Application                     | [See Notes](#_MSH-3_Sending_Application)         |
| 4   | 180 | HD  | O   |      | 0362           | Sending Facility                        | N/A                                              |
| 5   | 180 | HD  | O   |      | 0361           | Receiving Application                   | N/A                                              |
| 6   | 180 | HD  | O   |      | 0362           | Receiving Facility                      | N/A                                              |
| 7   | 26  | TS  | R   |      |                | Date/Time Of Message                    | N/A                                              |
| 8   | 40  | ST  | O   |      |                | Security                                | N/A                                              |
| 9   | 15  | CM  | R   |      | 0076/ 0003     | Message Type                            | [See Notes](#_MSH-4_Sending_Facility)            |
| 10  | 20  | ST  | R   |      |                | Message Control ID                      | [See Notes](#_MSH-10_Message_Control)            |
| 11  | 3   | PT  | R   |      |                | Processing ID                           | [See Notes](#_MSH-11_Processing_ID)              |
| 12  | 60  | VID | R   |      | 0104           | Version ID                              | [See Notes](#_MSH-12_Version_ID)                 |
| 13  | 15  | NM  | O   |      |                | Sequence Number                         | N/A                                              |
| 14  | 180 | ST  | O   |      |                | Continuation Pointer                    | N/A                                              |
| 15  | 2   | ID  | O   |      | [0155](#T0155) | Accept Acknowledgment Type              | [See Notes](#_MSH-15_Accept_Acknowledgment)      |
| 16  | 2   | ID  | O   |      | [0155](#T0155) | Application Acknowledgment Type         | [See Notes](#_MSH-16_Application_Acknowledgment) |
| 17  | 3   | ID  | O   |      | 0399           | Country Code                            | [See Notes](#_MSH-17_Country_Code)               |
| 18  | 16  | ID  | O   | Y    | 0211           | Character Set                           | N/A                                              |
| 19  | 250 | CE  | O   |      |                | Principal Language Of Message           | N/A                                              |
| 20  | 20  | ID  | O   |      | 0356           | Alternate Character Set Handling Scheme | N/A                                              |
| 21  | 10  | ID  | O   | Y    | 0449           | Conformance Statement ID                | N/A                                              |

1.  Field Definitions
    1.  <span id="_MSH-1_Field_Separator_1" class="anchor"></span>MSH-1 Field Separator

|             |                                                                                                                                                                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the separator between the segment ID and the first real field, *MSH-2 Encoding Characters.* As such it serves as the separator and defines the character to be used as a separator for the rest of the message. |
| Example:    | \| (ASCII 124)                                                                                                                                                                                                                  |

2.  <span id="_MSH-2_Encoding_Characters" class="anchor"></span>MSH-2 Encoding Characters

|             |                                                                                                                                                              |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the four characters in the following order: the component separator; repetition separator; escape character; and subcomponent separator. |
| Example:    | ^~\\ (ASCII 94, 126, 92, and 38, respectively)                                                                                                           |

3.  <span id="_MSH-3_Sending_Application" class="anchor"></span>MSH-3 Sending Application

|             |                                                                                                                                                                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field uniquely identifies the sending application among all other applications within the network enterprise. The network enterprise consists of all those applications that participate in the exchange of HL7 messages within the enterprise. Entirely site defined. |
| Example:    | ROR SITE                                                                                                                                                                                                                                                                |

4.  <span id="_MSH-4_Sending_Facility" class="anchor"></span>MSH-9 Message Type

|     |     |      |                   |             |
|-----|-----|------|-------------------|-------------|
| SEQ | DT  | TBL# | Component Name    | CCR         |
| 1   | ID  | 0076 | Message Type      | CSU     |
| 2   | ID  | 0003 | Trigger Event     | C09     |
| 3   | ID  | 0354 | Message Structure | CSU_C09 |

|             |                                                                                                                                              |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the message type and trigger event for the message. The CCR package sends a CSU message type with the trigger event C09. |
| Example:    | CSU^C09^CSU_C09                                                                                                                          |

5.  <span id="_MSH-10_Message_Control" class="anchor"></span>MSH-10 Message Control ID

|             |                                                                                                                                                                                                    |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message Acknowledgment segment (MSA). |
| Example:    | 640105354833-1                                                                                                                                                                                 |

6.  <span id="_MSH-11_Processing_ID" class="anchor"></span>MSH-11 Processing ID

|     |     |                |                 |     |
|-----|-----|----------------|-----------------|-----|
| SEQ | DT  | TBL#           | Component Name  | CCR |
| 1   | ID  | [0103](#T0103) | Processing ID   |     |
| 2   | ID  | [0207](#T0207) | Processing Mode | N/A |

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Definition:</td>
<td><p>This field identifies the current status of the interface, the component is used to indicate if the area and circumstances of the transmission.</p>
<p>The CDCO should not file training or debugging data into their production database.</p></td>
</tr>
<tr class="even">
<td>Example:</td>
<td><strong>P</strong></td>
</tr>
</tbody>
</table>

7.  <span id="_MSH-12_Version_ID" class="anchor"></span>MSH-12 Version ID

|             |                                                                                                                            |
|-------------|----------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field is matched by the receiving system to its own HL7 version to be sure the message will be interpreted correctly. |
| Example:    | 2.4                                                                                                                    |

8.  <span id="_MSH-15_Accept_Acknowledgment" class="anchor"></span>MSH-15 Accept Acknowledgment Type

|             |                                                                                                                                                                                                     |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field defines whether the sending system requires an acknowledgment from the receiving system when a message is accepted. The CCCR package always requests the accept (commit) acknowledgment. |
| Example:    | AL                                                                                                                                                                                              |

9.  <span id="_MSH-16_Application_Acknowledgment" class="anchor"></span>MSH-16 Application Acknowledgment Type

|             |                                                                                                                                                                                                                    |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field defines whether the sending system requires an acknowledgment from the receiving system when a message has been validated by the application. The CCR package does not use application acknowledgments. |
| Example:    | NE                                                                                                                                                                                                             |

10. <span id="_MSH-17_Country_Code" class="anchor"></span>MSH-17 Country Code

|             |                                                            |
|-------------|------------------------------------------------------------|
| Definition: | This field contains the country of origin for the message. |
| Example:    | USA                                                    |

2.  Sample MSH Segment

MSH\|[^~\\](#_MSH-2_Encoding_Characters)\|[ROR SITE](#_MSH-3_Sending_Application)\|\|\|\|\|\|[CSU^C09^CSU_C09](#_MSH-4_Sending_Facility)\|[640105760888-2](#_MSH-10_Message_Control)\|[P](#_MSH-11_Processing_ID)\|[2.4](#_MSH-12_Version_ID)\|\|

\|[AL](#_MSH-15_Accept_Acknowledgment)\|[NE](#_MSH-16_Application_Acknowledgment)\|[USA](#_MSH-17_Country_Code)

3.  <span id="_OBR" class="anchor"></span>OBR – Observation Request

| SEQ | LEN | DT  | OPT | RP/# | TBL# | Field Name                              | CCR                                                |
|-----|-----|-----|-----|------|------|-----------------------------------------|----------------------------------------------------|
| 1   | 4   | SI  | O   |      |      | Set ID - OBR                            | [See Notes](#_OBR-1_Set_ID_– OBR)                  |
| 2   | 22  | EI  | C   |      |      | Placer Order Number                     | N/A                                                |
| 3   | 22  | EI  | C   |      |      | Filler Order Number                     | [See Notes](#_OBR-3_Filler_Order_Number)           |
| 4   | 250 | CE  | R   |      |      | Universal Service Identifier            | [See Notes](#_OBR-4_Universal_Service_ID)          |
| 5   | 2   | ID  | X   |      |      | Priority - OBR                          | N/A                                                |
| 6   | 26  | TS  | X   |      |      | Requested Date/Time                     | [See Notes](#_OBR-6_Requested_Date/Time)           |
| 7   | 26  | TS  | C   |      |      | Observation Date/Time                   | [See Notes](#_OBR-7_Observation_Date/Time)         |
| 8   | 26  | TS  | O   |      |      | Observation End Date/Time               | [See Notes](#_OBR-8_Observation_End_Date/Time)     |
| 9   | 20  | CQ  | O   |      |      | Collection Volume                       | N/A                                                |
| 10  | 250 | XCN | O   | Y    |      | Collector Identifier                    | N/A                                                |
| 11  | 1   | ID  | O   |      | 0065 | Specimen Action Code                    | [See Notes](#_OBR-11_Specimen_Action_Code)         |
| 12  | 250 | CE  | O   |      |      | Danger Code                             | [See Notes](#_OBR-13_Relevant_Clinical_Info)       |
| 13  | 300 | ST  | O   |      |      | Relevant Clinical Info.                 | [See Notes](#_OBR-13_Relevant_Clinical_Info.)      |
| 14  | 26  | TS  | C   |      |      | Specimen Received Date/Time             | [See Notes](#_OBR-16_Ordering_Provider)            |
| 15  | 300 | CM  | O   |      | 0070 | Specimen Source                         | [See Notes](#_OBR-15_Specimen_Source)              |
| 16  | 250 | XCN | O   | Y    |      | Ordering Provider                       | [See Notes](#_OBR-16_Ordering_Provider_1)          |
| 17  | 250 | XTN | O   | Y/2  |      | Order Callback Phone Number             | N/A                                                |
| 18  | 60  | ST  | O   |      |      | Placer Field 1                          | [See Notes](#_OBR-18_Placer_Field_1)               |
| 19  | 60  | ST  | O   |      |      | Placer Field 2                          | N/A                                                |
| 20  | 60  | ST  | O   |      |      | Filler Field 1                          | [See Notes](#_OBR-19_Placer_Field_2)               |
| 21  | 60  | ST  | O   |      |      | Filler Field 2                          | [See Notes](#_OBR-21_Filler_Field_2)               |
| 22  | 26  | TS  | C   |      |      | Results Rpt/Status Chng - Date/Time     | [See Notes](#_OBR-22_Results_Rpt/Status_Chng - Da) |
| 23  | 40  | CM  | O   |      |      | Charge to Practice                      | N/A                                                |
| 24  | 10  | ID  | O   |      | 0074 | Diagnostic Serv Sect ID                 | [See Notes](#_OBR-24_Diagnostic_Serv_Sect ID_1)    |
| 25  | 1   | ID  | C   |      | 0123 | Result Status                           | [See Notes](#_OBR-25_Result_Status)                |
| 26  | 400 | CM  | O   |      |      | Parent Result                           | [See Notes](#_OBR-25_Result_Status_1)              |
| 27  | 200 | TQ  | O   | Y    |      | Quantity/Timing                         | N/A                                                |
| 28  | 250 | XCN | O   | Y/5  |      | Result Copies To                        | N/A                                                |
| 29  | 200 | CM  | O   |      |      | Parent                                  | [See Notes](#_OBR-29_Parent)                       |
| 30  | 20  | ID  | O   |      | 0124 | Transportation Mode                     | N/A                                                |
| 31  | 250 | CE  | O   | Y    |      | Reason for Study                        | N/A                                                |
| 32  | 200 | CM  | O   |      |      | Principal Result Interpreter            | N/A                                                |
| 33  | 200 | CM  | O   | Y    |      | Assistant Result Interpreter            | N/A                                                |
| 34  | 200 | CM  | O   | Y    |      | Technician                              | N/A                                                |
| 35  | 200 | CM  | O   | Y    |      | Transcriptionist                        | N/A                                                |
| 36  | 26  | TS  | O   |      |      | Scheduled Date/Time                     | N/A                                                |
| 37  | 4   | NM  | O   |      |      | Number of Sample Containers             | N/A                                                |
| 38  | 250 | CE  | O   | Y    |      | Transport Logistics of Collected Sample | N/A                                                |
| 39  | 250 | CE  | O   | Y    |      | Collector's Comment                     | N/A                                                |
| 40  | 250 | CE  | O   |      |      | Transport Arrangement Responsibility    | [See Notes](#_OBR-40_Transport_Arrangement_Respon) |
| 41  | 30  | ID  | O   |      | 0224 | Transport Arranged                      | N/A                                                |
| 42  | 1   | ID  | O   |      | 0225 | Escort Required                         | N/A                                                |
| 43  | 250 | CE  | O   | Y    |      | Planned Patient Transport Comment       | N/A                                                |
| 44  | 250 | CE  | O   |      | 0088 | Procedure Code                          | [See Notes](#_OBR-44_Transport_Arrangement_Respon) |
| 45  | 250 | CE  | O   | Y    | 0340 | Procedure Code Modifier                 | N/A                                                |
| 46  | 250 | CE  | O   | Y    | 0411 | Placer Supplemental Service Information | [See Notes](#_OBR-46_Placer_Supplemental_Service ) |
| 47  | 250 | CE  | O   | Y    | 0411 | Filler Supplemental Service Information | N/A                                                |

1.  Field Definitions
    1.  OBR-1 Set ID – OBR

|             |                                                                                                                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the number that identifies this transaction. For the first occurrence of the segment, the sequence number shall be one, for the second occurrence, the sequence number shall be two, etc. |
| Example:    | 2                                                                                                                                                                                                         |

2.  <span id="_OBR-3_Filler_Order_Number" class="anchor"></span>OBR-3 Filler Order Number

| SEQ         | DT  | TBL#                | Component Name    |                                                                                                                                                                                           | CCR |
|-------------|-----|---------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| 1           | ST  |                     | Entity Identifier |                                                                                                                                                                                           |     |
| 2           | IS  |                     | Namespace ID      |                                                                                                                                                                                           |     |
| 3           | ST  |                     | Universal ID      |                                                                                                                                                                                           |     |
| 4           | ID  |                     | Universal ID Type |                                                                                                                                                                                           |     |
| Definition: |     | Allergy:            |                   | IEN in the PATIENT ALLERGIES file (#120.8)                                                                                                                                                |     |
|             |     | Autopsy:            |                   | Accession Number                                                                                                                                                                          |     |
|             |     | Cytopathology:      |                   | Accession Number                                                                                                                                                                          |     |
|             |     | Immunization:       |                   | IEN in the IMMUNIZATION file (#9000010.11, \#.01)                                                                                                                                         |     |
|             |     | Inpatient:          |                   | IEN in the PTF file (#45)                                                                                                                                                                 |     |
|             |     | IV:                 |                   | Order Number                                                                                                                                                                              |     |
|             |     | Laboratory data:    |                   | Accession Number (Host UID)                                                                                                                                                               |     |
|             |     | Med. Proc. (EKG):   |                   | IEN in the ELECTROCARDIOGRAM (EKG) file (#691.5)                                                                                                                                          |     |
|             |     | Microbiology:       |                   | Accession Number                                                                                                                                                                          |     |
|             |     | Outpatient:         |                   | IEN in the VISIT file (#9000010)                                                                                                                                                          |     |
|             |     | Problem list:       |                   | IEN in the INSTITUTION file (#4) concatenated with the Problem Number (values of the .06 and .07 fields of the PROBLEM file (# 9000011) accordingly). The number can have decimal places. |     |
|             |     | Radiology:          |                   | Case Number                                                                                                                                                                               |     |
|             |     | Skin Test:          |                   | IEN in the SKIN TEST file (#9000010.12, \#.01)                                                                                                                                            |     |
|             |     | Surgical Pathology: |                   | Accession Number                                                                                                                                                                          |     |
| Example:    |     | Allergy:            |                   | 123                                                                                                                                                                                   |     |
|             |     | Autopsy:            |                   | AU 02 462820                                                                                                                                                                          |     |
|             |     | Cytopathology:      |                   | CY 02 345                                                                                                                                                                             |     |
|             |     | Immunization:       |                   | 123                                                                                                                                                                                   |     |
|             |     | Inpatient:          |                   | 2495                                                                                                                                                                                  |     |
|             |     | Outpatient:         |                   | 904726                                                                                                                                                                                |     |
|             |     | IV:                 |                   | 123431345                                                                                                                                                                             |     |
|             |     | Laboratory data:    |                   | CH 02 1234                                                                                                                                                                            |     |
|             |     | Med. Proc. (EKG):   |                   | 110120021658                                                                                                                                                                          |     |
|             |     | Microbiology:       |                   | 324MI33221                                                                                                                                                                            |     |
|             |     | Problem list:       |                   | 24452.11                                                                                                                                                                              |     |
|             |     | Radiology:          |                   | 6989273.8975-1^072601-1445                                                                                                                                                            |     |
|             |     | Skin Test:          |                   | 123                                                                                                                                                                                   |     |
|             |     | Surgical Pathology: |                   | SP 95 345                                                                                                                                                                             |     |

3.  <span id="_OBR-4_Universal_Service_ID" class="anchor"></span>OBR-4 Universal Service ID

|             |     |                                                                                                                                                                                   |                                 |                                                                                                                                             |     |
|-------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----|
| SEQ         | DT  | TBL#                                                                                                                                                                              | Component Name                  |                                                                                                                                             | CCR |
| 1           | ST  | 0005                                                                                                                                                                              | Identifier                      |                                                                                                                                             |     |
| 2           | ST  |                                                                                                                                                                                   | Text                            |                                                                                                                                             |     |
| 3           | ST  |                                                                                                                                                                                   | Name of Coding System           |                                                                                                                                             |     |
| 4           | ST  |                                                                                                                                                                                   | Alternate Identifier            |                                                                                                                                             |     |
| 5           | ST  |                                                                                                                                                                                   | Alternate Text                  |                                                                                                                                             |     |
| 6           | ST  |                                                                                                                                                                                   | Name of Alternate Coding System |                                                                                                                                             |     |
| Definition: |     | This field contains the identifier code for the requested observation/test.                                                                                                       |                                 |                                                                                                                                             |     |
|             |     | Allergy:                                                                                                                                                                          |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Autopsy:                                                                                                                                                                          |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Cytopathology:                                                                                                                                                                    |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Immunization:                                                                                                                                                                     |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Inpatient:                                                                                                                                                                        |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | IV:                                                                                                                                                                               |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Laboratory data:                                                                                                                                                                  |                                 | NLT Code and Test Name                                                                                                                      |     |
|             |     | Med. Proc. (EKG):                                                                                                                                                                 |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Microbiology:                                                                                                                                                                     |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Outpatient:                                                                                                                                                                       |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Problem list:                                                                                                                                                                     |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Radiology:                                                                                                                                                                        |                                 | The Procedure Name will appear in the text part of this segment and the identifier will be the CPT code that relates to the procedure name. |     |
|             |     | Skin Test:                                                                                                                                                                        |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Surgical Pathology:                                                                                                                                                               |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Vitals:                                                                                                                                                                           |                                 | Generic Hard-coded CPT-4 Code                                                                                                               |     |
|             |     | Distinguishing between records for Allergy, IV, Medical Procedures, Lab, Radiology, Autopsy, Surgical and Cytopathology results can be done by a combination of OBR-4 and OBR-24. |                                 |                                                                                                                                             |     |
| Example:    |     | Laboratory data:                                                                                                                                                                  |                                 | 83020.0000^Hemoglobin^99VA64                                                                                                            |     |
|             |     | Radiology:                                                                                                                                                                        |                                 | 71020^CHEST X-RAY^C4^58^CHEST PA\T\LAT^99RAP                                                                                            |     |
| Value:      |     | Allergy:                                                                                                                                                                          |                                 | 95000^ALLERGY^C4                                                                                                                        |     |
|             |     | Autopsy:                                                                                                                                                                          |                                 | 88099^UNLISTED NECROPSY PROC^C4                                                                                                         |     |
|             |     | Cytopathology:                                                                                                                                                                    |                                 | 88108^CYTOPATHOLOGY, CONCENT^C4                                                                                                         |     |
|             |     | Immunization:                                                                                                                                                                     |                                 | 90749^IMMUNIZATION^C4                                                                                                                   |     |
|             |     | Inpatient:                                                                                                                                                                        |                                 | IP^Inpatient^C4                                                                                                                         |     |
|             |     | IV:                                                                                                                                                                               |                                 | 90780^IV^C4                                                                                                                             |     |
|             |     | Med. Proc. (EKG):                                                                                                                                                                 |                                 | 93000^ELECTROCARDIOGRAM^C4                                                                                                              |     |
|             |     | Microbiology:                                                                                                                                                                     |                                 | 87999^MICROBIOLOGY^C4                                                                                                                   |     |
|             |     | Outpatient:                                                                                                                                                                       |                                 | OP^Outpatient^C4                                                                                                                        |     |
|             |     | Problem list:                                                                                                                                                                     |                                 | 90125^HOSPITAL CARE,NEW, INTERMED.^C4                                                                                                   |     |
|             |     | Skin Test:                                                                                                                                                                        |                                 | 86486^SKIN TEST^C4                                                                                                                      |     |
|             |     | Surgical Pathology:                                                                                                                                                               |                                 | 88300^LEVEL I - SURGICAL PAT^C4                                                                                                         |     |
|             |     | Vitals:                                                                                                                                                                           |                                 | 94150^VITAL CAPACITY TEST^C4                                                                                                            |     |

4.  <span id="_OBR-6_Requested_Date/Time" class="anchor"></span>OBR-6 Requested Date/Time

|             |                                                                                                                                                                                                               |                                                                         |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Definition: | This field contains the number that identifies this transaction. For the first occurrence of the segment, the sequence number shall be one, for the second occurrence, the sequence number shall be two, etc. |                                                                         |
|             | Med. Proc. (EKG):                                                                                                                                                                                             | Date/Time of the EKG                                                    |
|             | Problem list:                                                                                                                                                                                                 | Date/Time when the problem was entered into the PROBLEM file (#9000011) |
| Format:     | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]                                                                                                                                                               |                                                                         |
| Example:    | 200502101015-0800                                                                                                                                                                                             |                                                                         |

5.  <span id="_OBR-7_Observation_Date/Time" class="anchor"></span>OBR-7 Observation Date/Time

|             |                                                                                                                                                                                   |                                                                                                                           |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the identifier code for the requested observation/test:                                                                                                       |                                                                                                                           |
|             | Allergy:                                                                                                                                                                          | Origination Date                                                                                                          |
|             | Autopsy:                                                                                                                                                                          | Autopsy Date                                                                                                              |
|             | Cytopathology:                                                                                                                                                                    | Exam Date                                                                                                                 |
|             | Inpatient:                                                                                                                                                                        | Admission Date/Time                                                                                                       |
|             | IV:                                                                                                                                                                               | Start Time                                                                                                                |
|             | Laboratory data:                                                                                                                                                                  | Date/Time when the specimen was taken                                                                                     |
|             | Med. Proc. (EKG):                                                                                                                                                                 | Date/Time of the last successful transfer through the automated interface (populated only if received from an instrument) |
|             | Microbiology:                                                                                                                                                                     | Accession Date                                                                                                            |
|             | Outpatient:                                                                                                                                                                       | Visit Date/Time                                                                                                           |
|             | Problem list:                                                                                                                                                                     | Approximate date when the problem appeared                                                                                |
|             | Radiology:                                                                                                                                                                        | Exam Date/Time                                                                                                            |
|             | Skin Test:                                                                                                                                                                        | Date Read                                                                                                                 |
|             | Surgical Pathology:                                                                                                                                                               | Date/Time when the specimen was taken                                                                                     |
|             | Vitals:                                                                                                                                                                           | N/A                                                                                                                       |
|             | Distinguishing between records for Allergy, IV, Medical Procedures, Lab, Radiology, Autopsy, Surgical and Cytopathology results can be done by a combination of OBR-4 and OBR-24. |                                                                                                                           |
| Format:     | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]                                                                                                                                           |                                                                                                                           |
| Example:    | 200502101015-0800                                                                                                                                                             |                                                                                                                           |

6.  <span id="_OBR-8_Observation_End_Date/Time" class="anchor"></span>OBR-8 Observation End Date/Time

|             |                                                         |                                                        |
|-------------|---------------------------------------------------------|--------------------------------------------------------|
| Definition: | This field is populated only in the following segments: |                                                        |
|             | Autopsy:                                                | Date of the final autopsy diagnoses                    |
|             | IV:                                                     | Stop Date                                              |
|             | Problem List:                                           | Date/Time when the problem was resolved or inactivated |
|             | Surgical Pathology:                                     | Date/Time when the report was completed                |
| Format:     | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]                 |                                                        |
| Example:    | 200502101015-0800                                   |                                                        |

7.  <span id="_OBR-11_Specimen_Action_Code" class="anchor"></span>OBR-11 Specimen Action Code

|             |                                                         |                                                             |
|-------------|---------------------------------------------------------|-------------------------------------------------------------|
| Definition: | This field is populated only in the following segments: |                                                             |
|             | Laboratory:                                             | Specimen Action Code                                        |
|             | Microbiology:                                           | Indicates whether the urine screen is positive or negative. |
| Tables:     | Value                                                   | Urine Screen                                            |
|             | N                                                       | Negative                                                    |
|             | P                                                       | Positive                                                    |
| Example:    | P                                                   |                                                             |

8.  <span id="_OBR-13_Relevant_Clinical_Info" class="anchor"></span>OBR-12 Danger Code

|             |     |                                                         |                                 |                                                                                      |     |
|-------------|-----|---------------------------------------------------------|---------------------------------|--------------------------------------------------------------------------------------|-----|
| SEQ         | DT  | TBL#                                                    | Component Name                  |                                                                                      | CCR |
| 1           | ST  | 0005                                                    | Identifier                      |                                                                                      | N/A |
| 2           | ST  |                                                         | Text                            |                                                                                      |     |
| 3           | ST  |                                                         | Name of Coding System           |                                                                                      | N/A |
| 4           | ST  |                                                         | Alternate Identifier            |                                                                                      | N/A |
| 5           | ST  |                                                         | Alternate Text                  |                                                                                      | N/A |
| 6           | ST  |                                                         | Name of Alternate Coding System |                                                                                      | N/A |
| Definition: |     | This field is populated only in the following segments: |                                 |                                                                                      |     |
|             |     | Laboratory Data:                                        |                                 | Infection Warning (value of the PAT. INFO. field (#.091) of the LAB DATA file (#63)) |     |
| Format:     |     | Free Text                                               |                                 |                                                                                      |     |

9.  <span id="_OBR-13_Relevant_Clinical_Info." class="anchor"></span>OBR-13 Relevant Clinical Info.

|             |                                                         |                        |
|-------------|---------------------------------------------------------|------------------------|
| Definition: | This field is populated only in the following segments: |                        |
|             | Autopsy:                                                | Reactant               |
|             | Immunization:                                           | Comments               |
|             | IV:                                                     | Schedule               |
|             | Microbiology:                                           | Site Specimen          |
|             | Problem List:                                           | Diagnosis Code (ICD-9) |
|             | Skin Test:                                              | Comments               |
| Example:    | Autopsy:                                                | ONION                  |
|             | Immunization:                                           | HISTORY OF ALLERGY     |
|             | IV:                                                     | ONCE                   |
|             | Microbiology:                                           | PERITONEAL             |
|             | Problem List:                                           | 097.1                  |
|             | Skin Test:                                              | positive 9.9cm         |

10. <span id="_OBR-16_Ordering_Provider" class="anchor"></span>OBR-14 Specimen Received Date/Time

|             |                                                         |                                                   |
|-------------|---------------------------------------------------------|---------------------------------------------------|
| Definition: | This field is populated only in the following segments: |                                                   |
|             | Laboratory Data:                                        | Collection Date/Time                              |
|             | Problem List:                                           | Date when the problem was resolved or inactivated |
| Format:     | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]                 |                                                   |
| Example:    | 200502101015-0800                                   |                                                   |

11. <span id="_OBR-15_Specimen_Source" class="anchor"></span>OBR-15 Specimen Source

|             |     |      |                                                        |                     |                 |       |
|-------------|-----|------|--------------------------------------------------------|---------------------|-----------------|-------|
| SEQ         | DT  | TBL# |                                                        | Component Name      |                 | CCR   |
| 1           | CE  |      |                                                        | Specimen Source     |                 | LOINC |
| 2           | TX  |      |                                                        | Additives           |                 | N/A   |
| 3           | TX  |      |                                                        | Free Text           |                 | N/A   |
| 4           | CE  |      |                                                        | Body Site           |                 | N/A   |
| 5           | CE  |      |                                                        | Site Modifier       |                 | N/A   |
| 6           | CE  |      |                                                        | Collection Modifier |                 | N/A   |
| 7           | CE  |      |                                                        | Specimen Role       |                 | N/A   |
| Definition: |     |      | This field is populated only in the following segment: |                     |                 |       |
|             |     |      | Laboratory Data:                                       |                     | Specimen Source |       |
| Example:    |     |      | UR&Urine&HL70070&UR&Urine&LN                       |                     |                 |       |

12. <span id="_OBR-16_Ordering_Provider_1" class="anchor"></span>OBR-16 Ordering Provider

| SEQ | DT  | TBL# | Component Name                                     | CCR                                           |
|-----|-----|------|----------------------------------------------------|-----------------------------------------------|
| 1   | ST  |      | ID Number                                          | IEN of the user in the NEW PERSON file (#200) |
| 2   | FN  |      | Family Name                                        | N/A                                           |
| 3   | ST  |      | Given Name                                         | N/A                                           |
| 4   | ST  |      | Second and further given names or initials thereof | N/A                                           |
| 5   | ST  |      | Suffix (e.g., JR or III)                           | N/A                                           |
| 6   | ST  |      | Prefix (e.g., DR)                                  | N/A                                           |
| 7   | IS  | 0360 | Degree (e.g., MD)                                  | N/A                                           |
| 8   | IS  | 0297 | Source Table                                       | N/A                                           |
| 9   | HD  |      | Assigning Authority                                | N/A                                           |
| 10  | ID  | 0200 | Name Type Code                                     | N/A                                           |
| 11  | ST  |      | Identifier Check Digit                             | N/A                                           |
| 12  | ID  | 0061 | Code identifying the check digit scheme employed   | N/A                                           |
| 13  | IS  |      | Identifier Type Code                               | Provider Class Name                           |
| 14  | HD  |      | Assigning Facility                                 | N/A                                           |
| 15  | ID  | 0465 | Name Representation Code                           | N/A                                           |
| 16  | CE  | 0448 | Name Context                                       | N/A                                           |
| 17  | DR  |      | Name Validity Range                                | N/A                                           |
| 18  | ID  | 0444 | Name Assembly Order                                | N/A                                           |

|             |                                                                                                                                |                                                         |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Definition: | This field identifies the individual who ordered the test. Provider name is not used to ensure the patient privacy protection. |                                                         |
| Format:     | Allergy:                                                                                                                       | \<Provider IEN\>^^^^^^^^^^^^\<Provider Class Name\> |
|             | Autopsy:                                                                                                                       | \<Provider IEN\>                                        |
|             | Cytopathology:                                                                                                                 | N/A                                                     |
|             | Immunization:                                                                                                                  | \<Provider IEN\>^^^^^^^^^^^^\<Provider Class Name\> |
|             | Inpatient:                                                                                                                     | N/A                                                     |
|             | IV:                                                                                                                            | N/A                                                     |
|             | Laboratory Data:                                                                                                               | \<Provider IEN\>                                        |
|             | Med. Proc. (EKG):                                                                                                              | N/A                                                     |
|             | Microbiology:                                                                                                                  | N/A                                                     |
|             | Outpatient:                                                                                                                    | N/A                                                     |
|             | Problem list:                                                                                                                  | \<Provider IEN\>^^^^^^^^^^^^\<Provider Class Name\> |
|             | Radiology:                                                                                                                     | \<Provider IEN\>^^^^^^^^^^^^\<Provider Class Name\> |
|             | Skin Test:                                                                                                                     | \<Provider IEN\>^^^^^^^^^^^^\<Provider Class Name\> |
|             | Surgical Pathology:                                                                                                            | \<Surgeon/Physician IEN\>                               |
|             | Vitals:                                                                                                                        | N/A                                                     |
| Example:    | 2177^^^^^^^^^^^^PHYSICIAN                                                                                                      |                                                         |

13. <span id="_OBR-18_Placer_Field_1" class="anchor"></span>OBR-18 Placer Field 1

|             |                                                        |                             |
|-------------|--------------------------------------------------------|-----------------------------|
| Definition: | This field is populated only in the following segment: |                             |
|             | Laboratory Data:                                       | Name of the Auto-instrument |
| Format:     | \<Name of Analyzer or Instrument\>^\<Card Address\>    |                             |

14. <span id="_OBR-19_Placer_Field_2" class="anchor"></span>OBR-20 Filler Field 1

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 60%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="6">Definition:</td>
<td colspan="2">This field is populated only in the following segments:</td>
</tr>
<tr class="even">
<td>Allergy:</td>
<td>Allergy type</td>
</tr>
<tr class="odd">
<td>IV:</td>
<td>Infusion rate</td>
</tr>
<tr class="even">
<td>Laboratory Data:</td>
<td>Reference to the node in the LAB DATA file (#63)</td>
</tr>
<tr class="odd">
<td>Microbiology:</td>
<td>Collection Sample</td>
</tr>
<tr class="even">
<td>Problem List:</td>
<td>Condition of the Record</td>
</tr>
<tr class="odd">
<td rowspan="5">Format:</td>
<td>Allergy:</td>
<td>Text</td>
</tr>
<tr class="even">
<td>IV:</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>Laboratory Data:</td>
<td><p>&lt;LRDFN&gt;\S\&lt;Subscript&gt;\S\&lt;Inverted D/T&gt;</p>
<blockquote>
<p>(\S\ - encoded ^ character)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Microbiology:</td>
<td>&lt;Name&gt;</td>
</tr>
<tr class="odd">
<td>Problem List:</td>
<td>&lt;Code&gt;</td>
</tr>
<tr class="even">
<td rowspan="4">Tables:</td>
<td>Code</td>
<td>Condition of the Problem Record</td>
</tr>
<tr class="odd">
<td>H</td>
<td>Hidden</td>
</tr>
<tr class="even">
<td>P</td>
<td>Permanent</td>
</tr>
<tr class="odd">
<td>T</td>
<td>Transcribed</td>
</tr>
<tr class="even">
<td rowspan="5">Examples:</td>
<td>Allergy:</td>
<td>FOOD</td>
</tr>
<tr class="odd">
<td>IV:</td>
<td>INFUSE OVER 30 MIN</td>
</tr>
<tr class="even">
<td>Laboratory Data:</td>
<td>42058\S\CH\S\6949770.89857</td>
</tr>
<tr class="odd">
<td>Microbiology:</td>
<td>FLD-PERITONEAL</td>
</tr>
<tr class="even">
<td>Problem List:</td>
<td>P</td>
</tr>
</tbody>
</table>

15. <span id="_OBR-21_Filler_Field_2" class="anchor"></span>OBR-21 Filler Field 2

|             |                                                        |               |
|-------------|--------------------------------------------------------|---------------|
| Definition: | This field is populated only in the following segment: |               |
|             | Microbiology:                                          | Sputum Screen |
| Format:     | Free Text                                          |               |

16. OBR-22 Results Rpt/Status Chng - Date/Time

|             |                                                        |                                  |
|-------------|--------------------------------------------------------|----------------------------------|
| Definition: | This field is populated only in the following segment: |                                  |
|             | Autopsy:                                               | Date/Time the report is released |
|             | Laboratory Data:                                       | Date/Time the report is released |
|             | Problem List:                                          | Date/Time Last Modified          |
| Format:     | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]                |                                  |
| Example:    | 200502101015-0800                                  |                                  |

17. OBR-24 Diagnostic Service Section ID

|             |                                                                                          |         |
|-------------|------------------------------------------------------------------------------------------|---------|
| Definition: | This field is the section of the diagnostic service where the observation was performed. |         |
| Value:      | Allergy:                                                                                 | TX  |
|             | Autopsy:                                                                                 | SP  |
|             | Cytopathology:                                                                           | CP  |
|             | Immunization:                                                                            | OTH |
|             | Inpatient:                                                                               | PHY |
|             | IV:                                                                                      | IMM |
|             | Laboratory Data:                                                                         | LAB |
|             | Med. Proc. (EKG):                                                                        | EC  |
|             | Microbiology:                                                                            | MB  |
|             | Outpatient:                                                                              | PHY |
|             | Problem list:                                                                            | TX  |
|             | Radiology:                                                                               | RAD |
|             | Skin Test:                                                                               | OTH |
|             | Surgical Pathology:                                                                      | SP  |
|             | Vitals:                                                                                  | EC  |

18. <span id="_OBR-25_Result_Status" class="anchor"></span>OBR-25 Result Status

|             |                                                                                          |            |                       |              |                |
|-------------|------------------------------------------------------------------------------------------|------------|-----------------------|--------------|----------------|
| Definition: | This field is the section of the diagnostic service where the observation was performed. |            |                       |              |                |
| Value:      | Allergy:                                                                                 |            | Observed/Historical   |              |                |
|             | Med. Proc. (EKG):                                                                        |            | Confirmation Status   |              |                |
|             | Microbiology:                                                                            |            | Sterility Control     |              |                |
|             | Problem list:                                                                            |            | Status of the Problem |              |                |
| Tables:     | Value                                                                                    | Allergy    | Med Proc (EKG)        | Microbiology | Problem Status |
|             | F                                                                                        | Observed   | Confirmed             | Positive     | Active         |
|             | R                                                                                        | Historical | Unconfirmed           | Negative     | Inactive       |
| Example:    | F                                                                                    |            |                       |              |                |

19. <span id="_OBR-25_Result_Status_1" class="anchor"></span>OBR-26 Parent Result

|             |     |      |                                                        |                                               |                                                                                              |     |
|-------------|-----|------|--------------------------------------------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------|-----|
| SEQ         | DT  | TBL# |                                                        | Component Name                                |                                                                                              | CCR |
| 1           | CE  |      |                                                        | OBX-3 observation identifier of parent result |                                                                                              |     |
| 2           | ST  |      |                                                        | OBX-4 sub-ID of parent result                 |                                                                                              |     |
| 3           | TX  |      |                                                        | Part of OBX-5 observation result from parent  |                                                                                              |     |
| Definition: |     |      | This field is populated only in the following segment: |                                               |                                                                                              |     |
|             |     |      | Laboratory Data:                                       |                                               | The PARENT RESULT uniquely identifies the parent result's OBX segment related to this order. |     |

20. <span id="_OBR-29_Parent" class="anchor"></span>OBR-29 Parent

|             |     |      |                                                        |                              |                                                                                   |     |
|-------------|-----|------|--------------------------------------------------------|------------------------------|-----------------------------------------------------------------------------------|-----|
| SEQ         | DT  | TBL# |                                                        | Component Name               |                                                                                   | CCR |
| 1           | EI  |      |                                                        | Parent's Placer Order Number |                                                                                   |     |
| 2           | EI  |      |                                                        | Parent's Filler Order Number |                                                                                   |     |
| Definition: |     |      | This field is populated only in the following segment: |                              |                                                                                   |     |
|             |     |      | Laboratory Data:                                       |                              | This field relates a child to its parent when a parent-child relationship exists. |     |

21. <span id="_OBR-40_Transport_Arrangement_Respon" class="anchor"></span>OBR-40 Transport Arrangement Responsibility

|             |     |                                                         |                                 |              |        |
|-------------|-----|---------------------------------------------------------|---------------------------------|--------------|--------|
| SEQ         | DT  | TBL#                                                    | Component Name                  |              | CCR    |
| 1           | ST  | 0005                                                    | Identifier                      |              |        |
| 2           | ST  |                                                         | Text                            |              |        |
| 3           | ST  |                                                         | Name of Coding System           |              | VA |
| 4           | ST  |                                                         | Alternate Identifier            |              | N/A    |
| 5           | ST  |                                                         | Alternate Text                  |              | N/A    |
| 6           | ST  |                                                         | Name of Alternate Coding System |              | N/A    |
| Definition: |     | This field is populated in the following segments only: |                                 |              |        |
|             |     | IV:                                                     |                                 | Type         |        |
| Tables:     |     | Value                                                   |                                 | IV Type Tect |        |
|             |     | A                                                       |                                 | Admixture    |        |
|             |     | C                                                       |                                 | Chemotherapy |        |
|             |     | H                                                       |                                 | Hyperal      |        |
|             |     | P                                                       |                                 | Piggyback    |        |
|             |     | S                                                       |                                 | Syringe      |        |
| Example:    |     | IV: P^Piggyback^VA                                  |                                 |              |        |

22. <span id="_OBR-44_Transport_Arrangement_Respon" class="anchor"></span>OBR-44 Procedure Code

| SEQ | DT  | TBL# | Component Name                  | CCR                             |
|-----|-----|------|---------------------------------|---------------------------------|
| 1   | ST  | 0005 | Identifier                      | Station Number (without suffix) |
| 2   | ST  |      | Text                            | Institution Name                |
| 3   | ST  |      | Name of Coding System           | 99VA4                       |
| 4   | ST  |      | Alternate Identifier            | N/A                             |
| 5   | ST  |      | Alternate Text                  | N/A                             |
| 6   | ST  |      | Name of Alternate Coding System | N/A                             |

|             |                                                                                                                          |
|-------------|--------------------------------------------------------------------------------------------------------------------------|
| Definition: | The OBR-44 holds the station/division that placed the order. This field is empty in the Allergy and Laboratory segments. |
| Example:    | 640^PALO ALTO HCS^99VA4                                                                                              |

23. OBR-46 Placer Supplemental Service Information

|     |     |      |                                 |     |
|-----|-----|------|---------------------------------|-----|
| SEQ | DT  | TBL# | Component Name                  | CCR |
| 1   | ST  | 0005 | Identifier                      |     |
| 2   | ST  |      | Text                            |     |
| 3   | ST  |      | Name of Coding System           | N/A |
| 4   | ST  |      | Alternate Identifier            | N/A |
| 5   | ST  |      | Alternate Text                  | N/A |
| 6   | ST  |      | Name of Alternate Coding System | N/A |

|             |                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                              |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Definition: | The OBR-46 contains supplemental service information sent from the placer system to the filler system for the universal procedure code reported in OBR-4, Universal Service ID. This field will be used to provide ordering information detail that is not available in other, specific fields in the OBR segment. Multiple supplemental service information elements may be reported. *\[Source: HL7 Standard v24, 4.5.3.46\]* |                                                              |
|             | Autopsy:                                                                                                                                                                                                                                                                                                                                                                                                                        | Value of the SERVICE field (14.5) of the LAB DATA file (#63) |
| Format:     | \<Service Code\>^\<Service Name\>                                                                                                                                                                                                                                                                                                                                                                                           |                                                              |
| Example:    | Autopsy:S^SURGERY                                                                                                                                                                                                                                                                                                                                                                                                      |                                                              |

2.  Sample OBR Segments
    1.  Allergy

OBR\|[1](#_OBR-1_Set_ID_– OBR)\|\|[AL 99 5](#_OBR-3_Filler_Order_Number)\|[95000^ALLERGY^C4](#_OBR-4_Universal_Service_ID)\|\|\|[1995051611-000600](#_OBR-7_Observation_Date/Time)\|\|\|\|\|\|\|\|

\|[8491^^^^^^^^^^^^STAFF PHYSICIAN](#_OBR-16_Ordering_Provider_1)\|\|[DF](#_OBR-18_Placer_Field_1)\|\|\|\|\|\|[TX](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|[R](#_OBR-25_Result_Status)

2.  Autopsy

OBR\|[2](#_OBR-1_Set_ID_– OBR)\|\|[AU 99 5](#_OBR-3_Filler_Order_Number)\|[88099^UNLISTED NECROPSY PROC^C4](#_OBR-4_Universal_Service_ID)\|\|\|[199505161100-0600](#_OBR-7_Observation_Date/Time)\|[199505200900-0600](#_OBR-8_Observation_End_Date/Time)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[SP](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[499^HINES OIFO^99VA4](#_OBR-44_Transport_Arrangement_Respon)\|\|[S^SURGERY](#_OBR-46_Placer_Supplemental_Service )

3.  Cytopathology

OBR\|[3](#_OBR-1_Set_ID_– OBR)\|\|[AU 99 5](#_OBR-3_Filler_Order_Number)\|[88108^CYTOPATHOLOGY, CONCENT^C4](#_OBR-4_Universal_Service_ID)\|\|\|[199505161100-0600](#_OBR-7_Observation_Date/Time)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[CP](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[499^HINES OIFO^99VA4](#_OBR-44_Transport_Arrangement_Respon)

4.  Inpatient

OBR\|[4](#_OBR-1_Set_ID_– OBR)\|\|[23443](#_OBR-3_Filler_Order_Number)\|[IP^Inpatient^C4](#_OBR-4_Universal_Service_ID)\|\|\|[1997040593-000600](#_OBR-7_Observation_Date/Time)\|\|\|\|\|\|\|\|\|

\|\|\|\|\|\|\|\|[PHY](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[499^HINES OIFO^99VA4](#_OBR-44_Transport_Arrangement_Respon)

5.  Immunizations

OBR\|[2](#_OBR-1_Set_ID_– OBR)\|\|[24917](#_OBR-3_Filler_Order_Number)\|[90749^IMMUNIZATION^C4](#_OBR-4_Universal_Service_ID)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[OTH](#_OBR-44_Transport_Arrangement_Respon)

6.  IV

OBR\|[5](#_OBR-1_Set_ID_– OBR)\|\|[IV 99 5](#_OBR-3_Filler_Order_Number)\|[90780^IV^C4](#_OBR-4_Universal_Service_ID)\|\|\|[1995051611-000600](#_OBR-7_Observation_Date/Time)

\|[1996030312-000600](#_OBR-8_Observation_End_Date/Time)\|\|\|\|\|[Schedule goes here – free text](#_OBR-13_Relevant_Clinical_Info.)\|\|\|\|\|\|

\|[Infusion Rate](#_OBR-18_Placer_Field_1)\|\|\|\|[IMM](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[P^Piggyback^VA^^^^](\l)\|\|\|

\|[499^HINES OIFO^99VA4](#_OBR-44_Transport_Arrangement_Respon)

7.  Laboratory data

OBR\|[6](#_OBR-1_Set_ID_– OBR)\|\|[2050600309](#_OBR-3_Filler_Order_Number)\|[81129.0000^Hepatic Function Panel^99VA64](#_OBR-4_Universal_Service_ID)\|\|

\|[20050301101656-0800](#_OBR-7_Observation_Date/Time)\|\|\|\|[A](#_OBR-11_Specimen_Action_Code)\|[^](#_OBR-13_Relevant_Clinical_Info)\|\|[20050301101656-0800](#_OBR-16_Ordering_Provider)\|[SER&SER/PLAS&HL7&SER/PLAS&SER/PLAS&LN](#_OBR-15_Specimen_Source)\|[30890](#_OBR-16_Ordering_Provider_1)\|\|\|\|[87712\S\CH\S\6949697.898344](#_OBR-19_Placer_Field_2)\|\|[20050301111748-0800](#_OBR-24_Diagnostic_Serv_Sect ID)\|\|[LAB](#_OBR-24_Diagnostic_Serv_Sect ID_1)

8.  Med. Proc. (EKG)

OBR\|[7](#_OBR-1_Set_ID_– OBR)\|\|[110120021658](#_OBR-3_Filler_Order_Number)\|[93000^ELECTROCARDIOGRAM^C4](#_OBR-4_Universal_Service_ID)\|\|[199504151100-0600](#_OBR-6_Requested_Date/Time)\|[199505161100-0600](#_OBR-7_Observation_Date/Time)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[EC](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|[F](#_OBR-25_Result_Status)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

\|[612GF^MARTINEZ OPC/CREC^99VA4](#_OBR-44_Transport_Arrangement_Respon)

9.  Microbiology

OBR\|[8](#_OBR-1_Set_ID_– OBR)\|\|[MI 99 5](#_OBR-3_Filler_Order_Number)\|[87999^MICROBIOLOGY^C4](#_OBR-4_Universal_Service_ID)\|\|\|[1997040511-000600](#_OBR-7_Observation_Date/Time)\|\|\|\|[P](#_OBR-11_Specimen_Action_Code)

\|\|[BLOOD](#_OBR-13_Relevant_Clinical_Info.)\|\|\|\|\|\|\|[Sample type – free text](#_OBR-19_Placer_Field_2)\|[Sputum Screen – free text](#_OBR-21_Filler_Field_2)\|\|\|[MB](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|[F](#_OBR-25_Result_Status)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[499^HINES OIFO^99VA4](#_OBR-44_Transport_Arrangement_Respon)

10. Outpatient

OBR\|[9](#_OBR-1_Set_ID_– OBR)\|\|[45353453](#_OBR-3_Filler_Order_Number)\|[OP^Outpatient^C4](#_OBR-4_Universal_Service_ID)\|\|\|[1997040593-000600](#_OBR-7_Observation_Date/Time)\|\|\|\|\|\|\|\|\|\|\|\|

\|\|\|\|\|[PHY](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[499^HINES OIFO^99VA4](#_OBR-44_Transport_Arrangement_Respon)

11. Problem List

OBR\|1\|\|[640.016](#_OBR-3_Filler_Order_Number)\|90125[^HOSPITAL CARE,NEW, INTERMED.^C4](#_OBR-4_Universal_Service_ID)\|\|[20100119](#_OBR-6_Requested_Date/Time)\|20091101\|20100119\|\|\|\|\|070.0\|20091201\|\|[35220^^^^^^^^^^^^STAFF PHYSICIAN](#_OBR-16_Ordering_Provider_1)\|\|\|\|P\|\|[20100119](#_OBR-6_Requested_Date/Time)\|\|[TX](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|[R](#_OBR-25_Result_Status)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[499^HINES OIFO^99VA4](http://vaww.oed.portal.va.gov/projects/registries/Application%20Data/Microsoft/SharePoint%20Drafts/partners.harris.com/vap/vaprograms/TEMP/Temporary%20Directory%201%20for%20ROR1_5P11DOC2.ZIP/l)

12. Radiology

OBR\|[2](#_OBR-1_Set_ID_– OBR)\|\|[6989798.8767-1^020101-1327^L](#_OBR-3_Filler_Order_Number)\|[75736^ANGIO PELVIC SELECT OR SUPRASELECT S&I^C4^288^ANGIO CAROTID CEREBRAL BILAT S\T\I^99RAP](#_OBR-4_Universal_Service_ID)\|\|\|[200102011232-0600](#_OBR-7_Observation_Date/Time)\|\|\|\|\|\|\|\|\|[2177^^^^^^^^^^^^STAFF RADIOLOGIST](#_OBR-16_Ordering_Provider_1)\|\|\|\|\|\|\|\|[RAD](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[499^HINES OIFO^99VA4](#_OBR-44_Transport_Arrangement_Respon)

13. Skin Test

OBR\|1\|\|2111\|86486^SKIN TEST^C4\|\|\|20010523\|\|\|\|\|\|\|\|\|35220^^^^^^^^^^^^STAFF PHYSICIAN\|\|\|\|\|\|\|\|OTH

14. Surgical Pathology

OBR\|[3](#_OBR-1_Set_ID_– OBR)\|\|[SP 99 5](#_OBR-3_Filler_Order_Number)\|[88300^ LEVEL I – SURGICAL PAT^C4](#_OBR-4_Universal_Service_ID)\|\|\|[19990316](#_OBR-7_Observation_Date/Time)

\|[199508021100-0600](#_OBR-8_Observation_End_Date/Time)\|\|\|\|\|\|\|\|[329](#_OBR-16_Ordering_Provider_1)\|\|\|\|\|\|\|\|[SP](#_OBR-24_Diagnostic_Serv_Sect ID_1)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

\|[499^HINES OIFO^99VA4](#_OBR-44_Transport_Arrangement_Respon)

15. Vitals

OBR\|[4](#_OBR-1_Set_ID_– OBR)\|\|\|[94150^VITAL CAPACITY TEST^C4](#_OBR-4_Universal_Service_ID)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[EC](#_OBR-24_Diagnostic_Serv_Sect ID_1)

\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[499^HINES OIFO^99VA4](#_OBR-44_Transport_Arrangement_Respon)

4.  <span id="_OBX_–_Observation/Result_Segment" class="anchor"></span>OBX – Observation/Result Segment

| SEQ | LEN   | DT  | OPT | RP/# | TBL#           | Field Name                         | CCR                                                |
|-----|-------|-----|-----|------|----------------|------------------------------------|----------------------------------------------------|
| 1   | 4     | SI  | O   |      |                | Set ID - OBX                       | [See Notes](#_OBX-1_Set_ID_– OBX)                  |
| 2   | 2     | ID  | C   |      | [0125](#T0125) | Value Type                         | [See Notes](#_OBX-2_Value_Type)                    |
| 3   | 250   | CE  | R   |      |                | Observation Identifier             | [See Notes](#_OBX-3_Observation_Identifier)        |
| 4   | 20    | ST  | C   |      |                | Observation Sub-ID                 | [See Notes](#_OBX-4_Observation_Sub-ID)            |
| 5   | 65536 | \*  | C   | Y    |                | Observation Value                  | [See Notes](#_OBX-5_Observation_Value)             |
| 6   | 250   | CE  | O   |      |                | Units                              | [See Notes](#_OBX-6_Units_1)                       |
| 7   | 60    | ST  | O   |      |                | Reference Ranges                   | [See Notes](#_OBX-7_References_Range)              |
| 8   | 5     | IS  | O   | Y/5  | [0078](#T0078) | Abnormal Flags                     | [See Notes](#_OBX-8_Abnormal_Flags)                |
| 9   | 5     | NM  | O   |      |                | Probability                        | N/A                                                |
| 10  | 2     | ID  | O   | Y    | 0080           | Nature of Abnormal Test            | N/A                                                |
| 11  | 1     | ID  | R   |      | 0085           | Observation Result Status          | [See Notes](#_Toc232396308)                        |
| 12  | 26    | TS  | O   |      |                | Date Last Observation Normal Value | [See Notes](#_OBX-12_Date_Last_Observation Normal) |
| 13  | 20    | ST  | O   |      |                | User Defined Access Checks         | [See Notes](#_OBX-14)                              |
| 14  | 26    | TS  | O   |      |                | Date/Time of the Observation       | [See Notes](#_OBX-14)                              |
| 15  | 250   | CE  | O   |      |                | Producer's ID                      | [See Notes](#_OBX-13_User_Defined_Access_Checks)   |
| 16  | 250   | XCN | O   | Y    |                | Responsible Observer               | [See Notes](#_OBX-16_Responsible_Observer_1)       |
| 17  | 250   | CE  | O   | Y    |                | Observation Method                 | [See Notes](#_OBX-17)                              |
| 18  | 22    | EI  | O   | Y    |                | Equipment Instance Identifier      | N/A                                                |
| 19  | 26    | TS  | O   |      |                | Date/Time of the Analysis          | N/A                                                |

1.  Field Definitions
    1.  OBX-1 Set ID – OBX

|             |                                                                                                                                                                                                             |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the number that identifies this transaction. For the first occurrence of the segment, the sequence number will be one, for the second occurrence, the sequence number will be two, etc. |
| Example:    | 2                                                                                                                                                                                                       |

2.  <span id="_OBX-2_Value_Type" class="anchor"></span>OBX-2 Value Type

|             |                                                                     |                          |
|-------------|---------------------------------------------------------------------|--------------------------|
| Definition: | This field identifies the format of the observation value in OBX-5. |                          |
| Tables:     | A subset of the [HL7 Table 0125 – Value type](#T0125) is used.      |                          |
|             | Value                                                               | Description              |
|             | CE                                                                  | Coded Entry              |
|             | FT                                                                  | Formatted Text (Display) |
|             | NM                                                                  | Numeric                  |
|             | ST                                                                  | String Data              |
|             | TS                                                                  | Time Stamp (Date & Time) |
| Example:    | ST                                                                  |                          |

3.  <span id="_OBX-3_Observation_Identifier" class="anchor"></span>OBX-3 Observation Identifier

<table style="width:100%;">
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 24%" />
<col style="width: 35%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>DT</th>
<th>TBL#</th>
<th colspan="2">Component Name</th>
<th>CCR</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>ST</td>
<td>0005</td>
<td colspan="2">Identifier</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>ST</td>
<td></td>
<td colspan="2">Text</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>3</td>
<td>ST</td>
<td></td>
<td colspan="2">Name of Coding System</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>4</td>
<td>ST</td>
<td></td>
<td colspan="2">Alternate Identifier</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td>ST</td>
<td></td>
<td colspan="2">Alternate Text</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>ST</td>
<td></td>
<td colspan="2">Name of Alternate Coding System</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td>ST</td>
<td></td>
<td colspan="2">Alternate Identifier 2</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>8</td>
<td>ST</td>
<td></td>
<td colspan="2">Alternate Text 2</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>9</td>
<td>ST</td>
<td></td>
<td colspan="2">Name of Alternate Coding System 2</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Definition:</td>
<td colspan="5">This field identifies the segment.</td>
</tr>
<tr class="odd">
<td colspan="2" rowspan="15">Format:</td>
<td colspan="2">Allergy:</td>
<td colspan="3"><ul>
<li><p><strong>CLAS^Drug Class^VA080</strong></p></li>
<li><p><strong>INGR^Ingredients^VA080</strong></p></li>
<li><p><strong>RCTS^Reactions^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">Autopsy:</td>
<td colspan="3"><ul>
<li><p><strong>AUCD^Clinical Diagnosis^VA080</strong></p></li>
<li><p><strong>AUPD^Pathological Diagnosis^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2">Cytopathology:</td>
<td colspan="3"><ul>
<li><p><strong>BCH^Brief Clinical History^VA080</strong></p></li>
<li><p><strong>CDIAG^Cytopathology Diagnosis^VA080</strong></p></li>
<li><p><strong>ICD9^ICD9^VA080</strong></p></li>
<li><p><strong>MICRO^Microscopic Description^VA080</strong></p></li>
<li><p><strong>OF^Operative Findings^VA080</strong></p></li>
<li><p><strong>PDIAG^Preoperative Diagnosis^VA080</strong></p></li>
<li><p><strong>POPDIAG^Postoperative Diagnosis^VA080</strong></p></li>
<li><p><strong>SPEC^Specimen^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">Inpatient:</td>
<td colspan="3"><ul>
<li><p><strong>INAD^Admitting Diagnosis^VA080</strong></p></li>
<li><p><strong>INBED^Bed-section Diagnosis^VA080</strong></p></li>
<li><p><strong>INDIS^Discharge Diagnosis^VA080</strong></p></li>
<li><p><strong>INOTR^Other Diagnosis^VA080</strong></p></li>
<li><p><strong>INPRI^Primary Dis. Diagnosis^VA080</strong></p></li>
<li><p><strong>INSURG^Surgical Procedures^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2">Immunization:</td>
<td colspan="3"><ul>
<li><p><strong>^Immunization Name</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">IV:</td>
<td colspan="3"><ul>
<li><p><strong>ADD^Additive^VA080</strong></p></li>
<li><p><strong>OTPR^Other Print Info^VA080</strong></p></li>
<li><p><strong>SOL^Solution^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2">Laboratory Data:</td>
<td colspan="3"><ul>
<li><p><strong>[&lt;LOINC^Text&gt;^LN^][&lt;NLT&gt;^&lt;Text&gt;^99VA64^]&lt;Local Test ID&gt;^&lt;Local Test Name&gt;^99VA63</strong></p>
<ul>
<li><p><strong>LABC^Lab Comment^VA080</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">Med. Proc. (EKG):</td>
<td colspan="3"><ul>
<li><p><strong>AUTO^Auto Instrument^VA080</strong></p></li>
<li><p><strong>INT^Interpretation^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2">Microbiology:</td>
<td colspan="3"><ul>
<li><p><strong>AFB-Bay Pines^TB Report^VA080</strong></p></li>
<li><p><strong>BACT^Bact^VA080</strong></p></li>
<li><p><strong>BACT-Bay Pines^Bact Smear/Prep^VA080</strong></p></li>
<li><p><strong>COMP^Specimen Comment^VA080</strong></p></li>
<li><p><strong>FUNG^Fungus-Yeast^VA080</strong></p>
<ul>
<li><p><strong>FUNGC^F-Y Comment^VA080</strong></p></li>
</ul></li>
<li><p><strong>GRAM^Gram Stain^VA080</strong></p></li>
<li><p><strong>MYCO^Mycobacterium^VA080</strong></p>
<ul>
<li><p><strong>MYCOAF^Myco Anti-F^VA080</strong></p></li>
<li><p><strong>MYCOAO^Myco Anti-O^VA080</strong></p></li>
<li><p><strong>MYCOC^Myco Comment^VA080</strong></p></li>
</ul></li>
<li><p><strong>MYCO-Bay Pines^Mycology Smear/Prep^VA080</strong></p></li>
<li><p><strong>ORG^Organism^VA080</strong></p>
<ul>
<li><p><strong>ORGA^Org Antibiotic^VA080</strong></p></li>
<li><p><strong>ORGAF^Org Antibiotic-F^VA080</strong></p></li>
<li><p><strong>ORGAO^Org Antibiotic-O^VA080</strong></p></li>
<li><p><strong>ORGC^Org Comment^VA080</strong></p></li>
</ul></li>
<li><p><strong>PAR^Parasite^VA080</strong></p>
<ul>
<li><p><strong>PARQ^Stage^VA080</strong></p></li>
<li><p><strong>PARC^Comment^VA080</strong></p></li>
</ul></li>
<li><p><strong>PARA-Bay Pines^Para Smear/Prep^VA080</strong></p></li>
<li><p><strong>PARP^Parasite Remark^VA080</strong></p></li>
<li><p><strong>VIRUS^Virus^VA080</strong></p></li>
<li><p><strong>VIRUSR^Virology RPT^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">Outpatient:</td>
<td colspan="3"><ul>
<li><p><strong>OCPT^Procedures^VA080</strong></p></li>
<li><p><strong>OICD9^Diagnosis^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2">Problem List:</td>
<td colspan="3"><ul>
<li><p><strong>EXPR^Expression^VA080</strong></p></li>
<li><p><strong>NOTE^Note Narrative^VA080</strong></p></li>
<li><p><strong>PRVN^Provider Narrative^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">Radiology:</td>
<td colspan="3"><ul>
<li><p><strong>CH^Clinical History^VA080</strong></p></li>
<li><p><strong>IT^Impression Text^VA080</strong></p></li>
<li><p><strong>RT^Report Text^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2">Skin Test:</td>
<td colspan="3"><ul>
<li><p><strong>^Skin Test name</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">Surgical Pathology:</td>
<td colspan="3"><ul>
<li><p><strong>BCH^Brief Clinical History^VA080</strong></p></li>
<li><p><strong>GDESC^Gross Decription^VA080</strong></p></li>
<li><p><strong>ICD9^ICD-9 Code^VA080</strong></p></li>
<li><p><strong>MDESC^Microscopic Description^VA080</strong></p></li>
<li><p><strong>OF^Operative Findings^VA080</strong></p></li>
<li><p><strong>PDIAG^Preoperative Diagnosis^VA080</strong></p></li>
<li><p><strong>POPDIAG^Postoperative Diagnosis^VA080</strong></p></li>
<li><p><strong>SPDIAG^Surgical Pathology Diagnosis^VA080</strong></p></li>
<li><p><strong>SPEC^Specimen^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2">Vitals:</td>
<td colspan="3"><ul>
<li><p><strong>Bay Pines^Blood Pressure^VA080</strong></p></li>
<li><p><strong>HT^Height^VA080</strong></p></li>
<li><p><strong>P^Pulse^VA080</strong></p></li>
<li><p><strong>PN^Pain^VA080</strong></p></li>
<li><p><strong>R^Respiration^VA080</strong></p></li>
<li><p><strong>T^Temperature^VA080</strong></p></li>
<li><p><strong>WT^Weight^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">Example:</td>
<td colspan="2">Laboratory Data:</td>
<td colspan="2"><p>718-7^HEMOGLOBIN:MCNC:PT:BLD:QN^LN</p>
<p>^83020.0000^Hemoglobin^99VA64^CH386^HGB^99VA63</p></td>
<td></td>
</tr>
</tbody>
</table>

1.  <span id="_OBX-4_Observation_Sub-ID" class="anchor"></span>OBX-4 Observation Sub-ID

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 20%" />
<col style="width: 62%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="5">Definition:</td>
<td colspan="2">This field contains the result observed by the observation producer. This field is populated in the following cases only:</td>
</tr>
<tr class="even">
<td>Laboratory Data:</td>
<td><ul>
<li><p>If OBX-3 contains the LOINC code and this field is blank then this is the main lab OBX segment.</p></li>
<li><p>If OBX-3 contains "LABC^Lab Comment" and this field contains "LCOMM", then the OBX-5 will contain the Lab Comment.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Med. Proc. (EKG):</td>
<td>If OBX-3 contains "INT^Interpretation", then this field may contain the Interpretation Code Modifier for Medical Procedure data.</td>
</tr>
<tr class="even">
<td>Microbiology:</td>
<td>If OBX-3 contains "MYCOAF^Myco Anti-F", "MYCOAO^Myco Anti-O", "ORGAF^Org Antibiotic-F", or "ORGAO^Org Antibiotic-O", then this field contains the microbiology field name.</td>
</tr>
<tr class="odd">
<td>Vitals:</td>
<td>Unique identifier for the record.</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2">Med. Proc. (EKG): <strong>CHANGES OR SERIAL</strong></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2">Laboratory Data: <strong>LCOMM</strong></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2">Microbiology: <strong>STR</strong></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2">Vitals: <strong>2355</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_OBX-5_Observation_Value" class="anchor"></span>OBX-5 Observation Value

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 60%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Definition:</td>
<td colspan="2"><p>This field contains the result(s) observed by the observation producer. The format depends on the data type in <strong>OBX-2</strong> and the content depends on <strong>OBX-3</strong>.</p>
<p>Vitals: <strong>&lt;Rate&gt;</strong>^<strong>&lt;Quality&gt;</strong>^<strong>&lt;Qualifiers&gt;</strong> - these values are always separated by the '^' character (even if other component separator is used), then the whole string is encoded according to the HL7 standard.</p></td>
</tr>
<tr class="even">
<td></td>
<td>Vitals:</td>
<td><p><strong>&lt;Rate&gt;^&lt;Quality&gt;^&lt;Qualifiers&gt;</strong></p>
<p>These values are always separated by the "<strong>^</strong>" character (even if other component separator is used), then the whole string is encoded according to the HL7 standard.</p></td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><ul>
<li><p>Vitals: <strong>34\S\Weak\S\QER</strong></p></li>
<li><p>Otherwise: <strong>103.9</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td rowspan="14">Notes:</td>
<td colspan="2">This field can be repeated in the following segments:</td>
</tr>
<tr class="odd">
<td>Allergy:</td>
<td><ul>
<li><p><strong>CLAS^Drug Class^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>Cytopathology:</td>
<td><ul>
<li><p><strong>ICD9^ICD9^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Immunization:</td>
<td><ul>
<li><p><strong>Reaction^Contraindicated</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>Inpatient:</td>
<td><ul>
<li><p><strong>INBED^Bed-section Diagnosis^VA080</strong></p></li>
<li><p><strong>INDIS^Discharge Diagnosis^VA080</strong></p></li>
<li><p><strong>INOTR^Other Diagnosis^VA080</strong></p></li>
<li><p><strong>INSURG^Surgical Procedures^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Skin Test:</td>
<td><ul>
<li><p><strong>Results^Reading</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>Surgical Pathology:</td>
<td><ul>
<li><p><strong>ICD9^ICD-9 Code^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2">This field can contain multi-line text in the following segments (lines are separated by "<strong>.br</strong>" enclosed in HL7 escape character):</td>
</tr>
<tr class="even">
<td>Autopsy:</td>
<td><ul>
<li><p><strong>AUCD^Clinical Diagnosis^VA080</strong></p></li>
<li><p><strong>AUPD^Pathological Diagnosis^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Cytopatholgy:</td>
<td><ul>
<li><p><strong>BCH^Brief Clinical History^VA080</strong></p></li>
<li><p><strong>CDIAG^Cytopathology Diagnosis^VA080</strong></p></li>
<li><p><strong>MICRO^Microscopic Description^VA080</strong></p></li>
<li><p><strong>OF^Operative Findings^VA080</strong></p></li>
<li><p><strong>PDIAG^Preoperative Diagnosis^VA080</strong></p></li>
<li><p><strong>POPDIAG^Postoperative Diagnosis^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>Med. Proc. (EKG):</td>
<td><ul>
<li><p><strong>AUTO^Auto Instrument^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Problem List:</td>
<td><ul>
<li><p><strong>NOTE^Note Narrative^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>Radiology:</td>
<td><ul>
<li><p><strong>CH^Clinical History^VA080</strong></p></li>
<li><p><strong>IT^Impression Text^VA080</strong></p></li>
<li><p><strong>RT^Report Text^VA080</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Surgical Pathology:</td>
<td><ul>
<li><p><strong>BCH^Brief Clinical History^VA080</strong></p></li>
<li><p><strong>GDESC^Gross Decription^VA080</strong></p></li>
<li><p><strong>MDESC^Microscopic Description^VA080</strong></p></li>
<li><p><strong>OF^Operative Findings^VA080</strong></p></li>
<li><p><strong>PDIAG^Preoperative Diagnosis^VA080</strong></p></li>
<li><p><strong>POPDIAG^Postoperative Diagnosis^VA080</strong></p></li>
<li><p><strong>SPEC^Specimen^VA080</strong></p></li>
</ul></td>
</tr>
</tbody>
</table>

1.  <span id="_OBX-6_Units_1" class="anchor"></span>OBX-6 Units

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 24%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>DT</th>
<th>TBL#</th>
<th colspan="2">Component Name</th>
<th>CCR</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>ST</td>
<td>0005</td>
<td colspan="2">Identifier</td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>ST</td>
<td></td>
<td colspan="2">Text</td>
<td></td>
</tr>
<tr class="odd">
<td>3</td>
<td>ST</td>
<td></td>
<td colspan="2">Name of Coding System</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>4</td>
<td>ST</td>
<td></td>
<td colspan="2">Alternate Identifier</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>5</td>
<td>ST</td>
<td></td>
<td colspan="2">Alternate Text</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>6</td>
<td>ST</td>
<td></td>
<td colspan="2">Name of Alternate Coding System</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td colspan="2" rowspan="5">Definition:</td>
<td colspan="4">This field is populated in the following cases only:</td>
</tr>
<tr class="even">
<td colspan="2">Inpatient:</td>
<td colspan="2">Bed Section, if OBX-3 contains "INOTR^Other Diagnosis" or "INBED^Bedsection Diagnosis"</td>
</tr>
<tr class="odd">
<td colspan="2">Laboratory Data:</td>
<td colspan="2">Unit of the observation value</td>
</tr>
<tr class="even">
<td colspan="2">Microbiology:</td>
<td colspan="2"><p>Quantity (free text), if OBX-3 contains any of these values:</p>
<p>"FUNG^Fungus-Yeast"</p>
<p>"MYCO^Mycobacterium"</p>
<p>"PARQ^Stage"</p></td>
</tr>
<tr class="odd">
<td colspan="2">Vitals:</td>
<td colspan="2">Value in metric system</td>
</tr>
<tr class="even">
<td colspan="2" rowspan="4">Examples:</td>
<td colspan="2">Inpatient:</td>
<td colspan="2"><strong>94^INTERMEDIATE MEDICINE – LTC</strong></td>
</tr>
<tr class="odd">
<td colspan="2">Laboratory Data:</td>
<td colspan="2"><strong>GM/DL</strong></td>
</tr>
<tr class="even">
<td colspan="2">Microbiology:</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="2">Vitals:</td>
<td colspan="2"><strong>182.88</strong></td>
</tr>
</tbody>
</table>

2.  <span id="_OBX-7_References_Range" class="anchor"></span>OBX-7 Reference Ranges

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 60%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="5">Definition:</td>
<td colspan="2">This field is populated in the following cases only:</td>
</tr>
<tr class="even">
<td>IV:</td>
<td><ul>
<li><p>Strength for additive, <em>if</em> OBX-3 contains "ADD^Additive"</p></li>
<li><p>Volume for solution, <em>if</em> <strong>OBX-3</strong> contains "<strong>SOL^Solution</strong>".</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Laboratory Data:</td>
<td>&lt;Lower&gt;<strong>-</strong>&lt;Upper&gt;</td>
</tr>
<tr class="even">
<td>Microbiology:</td>
<td><ul>
<li><p>&lt;MIC&gt; - Minimum Inhibitory Concentration (LAB DATA file (#63) MICROBIOLOGY multiple (5) ORGANISM multiple (12) ANTIBIOTIC multiple (200) 'MIC(ug/ml)' field (1)), <em>if</em> OBX-3 contains "ORGA^Org Antibiotic";</p></li>
<li><p>Acid Fast Stain result, <em>if</em> OBX-3 contains "AFB-SP^TB Report" (LAB DATA file (#63) MICROBIOLOGY multiple (5) ACID FAST STAIN (24)).</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Vitals:</td>
<td>Body Mass, <em>if</em> OBX-3 contains "WT^Weight"</td>
</tr>
<tr class="even">
<td rowspan="4">Examples:</td>
<td>IV:</td>
<td><strong>37 MG</strong></td>
</tr>
<tr class="odd">
<td>Laboratory Data:</td>
<td><strong>3.4-5.0</strong></td>
</tr>
<tr class="even">
<td>Microbiology:</td>
<td><strong>23</strong></td>
</tr>
<tr class="odd">
<td>Vitals:</td>
<td><strong>27</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_OBX-8_Abnormal_Flags" class="anchor"></span>OBX-8 Abnormal Flags

|             |                                                         |                              |
|-------------|---------------------------------------------------------|------------------------------|
| Definition: | This field is populated in the following segments only: |                              |
|             | Laboratory Data:                                        | Flag on Values for lab tests |
| Example:    | Laboratory Data:                                        | LL                       |

2.  <span id="_Toc232396308" class="anchor"></span>OBX-11 Observation Result Status

|             |                                                                                                    |                                                                     |
|-------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Definition: | This field contains the observation result status.                                                 |                                                                     |
| Tables:     | A subset of the [HL7 Table 0085 – Observation result status codes](#T0085) interpretation is used. |                                                                     |
|             | Value                                                                                              | Description                                                         |
|             | C                                                                                                  | Record coming over is a correction and thus replaces a final result |
|             | F                                                                                                  | Final results; Can only be changed with a corrected result          |
|             | I                                                                                                  | Specimen in lab; results pending                                    |
|             | P                                                                                                  | Preliminary results                                                 |
| Example:    | F                                                                                              |                                                                     |

3.  OBX-12 Date Last Observation Normal Value

|             |                                                      |                                                                             |
|-------------|------------------------------------------------------|-----------------------------------------------------------------------------|
| Definition: | This field is populated in the following cases only: |                                                                             |
|             | Allergy:                                             | Reactions Date/Time Entered                                                 |
|             | Inpatient:                                           | Bed-section End Date/Time, *if* OBX-3 contains "INBED^Bedsection Diagnosis" |
| Format:     | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]          |                                                                             |
| Example:    | 200502101015-0800                                |                                                                             |

4.  <span id="_OBX-14" class="anchor"></span>OBX-13 User Defined Access Checks

|             |                                                      |                                                                                                                                                                                                                |
|-------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field is populated in the following cases only: |                                                                                                                                                                                                                |
|             | Microbiology:                                        | \<MBC\> - Minimum Bactericidal Concentration (LAB DATA file (#63) MICROBIOLOGY multiple (5) ORGANISM multiple (12) ANTIBIOTIC multiple (200) 'MBC(ug/ml)' field (2)), if OBX-3 contains "ORGA^Org Antibiotic". |
| Example:    | 222                                              |                                                                                                                                                                                                                |

5.  OBX-14 Date/Time of the Observation

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 60%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="7">Definition:</td>
<td colspan="2">This field is populated in the following cases only:</td>
</tr>
<tr class="even">
<td>Immunization:</td>
<td>Event Date/Time</td>
</tr>
<tr class="odd">
<td>Inpatient:</td>
<td><ul>
<li><p>Bed Section Start Date, if OBX-3 contains "INBED^Bedsection Diagnosis";</p></li>
<li><p>Surgical Procedure Date, if OBX-3 contains "INSURG^Surgical Procedures";</p></li>
<li><p>Other Procedure Date, if OBX-3 contains "INOTR^Other Diagnosis".</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Laboratory Data:</td>
<td>Collection Date/Time</td>
</tr>
<tr class="odd">
<td>Microbiology:</td>
<td>Date/Time of the TB report approval, <em>if</em> OBX-3 contains "AFB-SP^TB Report")</td>
</tr>
<tr class="even">
<td>Skin Tests:</td>
<td>Event Date/Time</td>
</tr>
<tr class="odd">
<td>Vitals:</td>
<td>Date/Time of Measurement</td>
</tr>
<tr class="even">
<td>Format:</td>
<td colspan="2">YYYYMMDD[hhmm[ss]] [+|-zzzz]</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>200502101015-0800</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_OBX-13_User_Defined_Access_Checks" class="anchor"></span>OBX-15 Producer's ID

|     |     |      |                                 |                  |
|-----|-----|------|---------------------------------|------------------|
| SEQ | DT  | TBL# | Component Name                  | CCR              |
| 1   | ST  | 0005 | Identifier                      | Station Number   |
| 2   | ST  |      | Text                            | Institution Name |
| 3   | ST  |      | Name of Coding System           | 99VA4        |
| 4   | ST  |      | Alternate Identifier            | N/A              |
| 5   | ST  |      | Alternate Text                  | N/A              |
| 6   | ST  |      | Name of Alternate Coding System | N/A              |

<span id="_OBX-16_Responsible_Observer" class="anchor"></span>

|             |                                                      |
|-------------|------------------------------------------------------|
| Definition: | This field is populated in the following cases only: |
|             | Laboratory Data                                      |
| Example:    | 499^HINES OIFO^99VA4                             |

2.  <span id="_OBX-16_Responsible_Observer_1" class="anchor"></span>OBX-16 Responsible Observer

|     |     |      |                                                    |                                               |
|-----|-----|------|----------------------------------------------------|-----------------------------------------------|
| SEQ | DT  | TBL# | Component Name                                     | CCR                                           |
| 1   | ST  |      | ID Number                                          | IEN of the user in the NEW PERSON file (#200) |
| 2   | FN  |      | Family Name                                        |                                               |
| 3   | ST  |      | Given Name                                         |                                               |
| 4   | ST  |      | Second and further given names or initials thereof |                                               |
| 5   | ST  |      | Suffix (e.g., JR or III)                           |                                               |
| 6   | ST  |      | Prefix (e.g., DR)                                  |                                               |
| 7   | IS  | 0360 | Degree (e.g., MD)                                  | N/A                                           |
| 8   | IS  | 0297 | Source Table                                       | N/A                                           |
| 9   | HD  |      | Assigning Authority                                | N/A                                           |
| 10  | ID  | 0200 | Name Type Code                                     | N/A                                           |
| 11  | ST  |      | Identifier Check Digit                             | N/A                                           |
| 12  | ID  | 0061 | Code identifying the check digit scheme employed   | N/A                                           |
| 13  | IS  |      | Identifier Type Code                               | Provider Class Name                           |
| 14  | HD  |      | Assigning Facility                                 | N/A                                           |
| 15  | ID  | 0465 | Name Representation Code                           | N/A                                           |
| 16  | CE  | 0448 | Name Context                                       | N/A                                           |
| 17  | DR  |      | Name Validity Range                                | N/A                                           |
| 18  | ID  | 0444 | Name Assembly Order                                | N/A                                           |

|             |                                                                                  |                                                                                                                       |
|-------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Definition: | This field identifies the provider. It is populated in the following cases only: |                                                                                                                       |
|             | Laboratory Data:                                                                 | Technician who performed the analysis: \<User IEN\>-\<Station Number\>^\<Last Name\>^\<First Name\>^… |
|             | Outpatient:                                                                      | Procedure Provider and the Provider's Class Name: \<User IEN\>^^^^^^^^^^^^\<Provider Class Name\>                 |
| Example:    | 2177^^^^^^^^^^^^PHYSICIAN                                                    |                                                                                                                       |

3.  <span id="_OBX-17" class="anchor"></span>OBX-17 Observation Method

|     |     |      |                                 |     |
|-----|-----|------|---------------------------------|-----|
| SEQ | DT  | TBL# | Component Name                  | CCR |
| 1   | ST  | 0005 | Identifier                      |     |
| 2   | ST  |      | Text                            |     |
| 3   | ST  |      | Name of Coding System           |     |
| 4   | ST  |      | Alternate Identifier            | N/A |
| 5   | ST  |      | Alternate Text                  | N/A |
| 6   | ST  |      | Name of Alternate Coding System | N/A |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td colspan="2">This field is populated in the following cases only:</td>
</tr>
<tr class="even">
<td>Laboratory Data:</td>
<td><p>Observation Method</p>
<p>&lt;Workload Suffix Code&gt;<strong>^</strong>&lt;Name&gt;<strong>^99VA64_2</strong></p></td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>.3112^CHEM 1^99VA64_2</strong></td>
</tr>
</tbody>
</table>

4.  OBX-19 Date/Time of the Analysis

|     |     |      |                |     |
|-----|-----|------|----------------|-----|
| SEQ | DT  | TBL# | Component Name | CCR |
| 1   | ST  | 0005 | Identifier     |     |
|     |     |      |                |     |
|     |     |      |                |     |
|     |     |      |                |     |
|     |     |      |                |     |

|             |                                                      |                 |
|-------------|------------------------------------------------------|-----------------|
| Definition: | This field is populated in the following cases only: |                 |
|             | Immunization:                                        | Visit Date/Time |
|             | Skin Test:                                           | Visit Date/Time |
| Example:    | 200502101015-0800                                |                 |

1.  Sample OBX Segments
    1.  Allergy

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[INGR^Ingredients^VA080](#_OBX-3_Observation_Identifier)\|\|[Drug ingredients text](\l)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[CLAS^Drug Class^VA080](#_OBX-3_Observation_Identifier)\|\|[Drug Class Text](\l)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[3](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[RCTS^Reactions^VA080](#_OBX-3_Observation_Identifier)\|\|[Reactions Text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)\|[20021203](#_OBX-12_Date_Last_Observation Normal)

2.  Autopsy

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[AUCD^Clinical Diagnosis^VA080](#_OBX-3_Observation_Identifier)\|\|[Text Line \#1\\br\Text Line \#2](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[AUPD^Pathological Diagnosis^VA080](#_OBX-3_Observation_Identifier)\|\|[Text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

3.  Cytopathology

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[SPEC^Specimen^VA080](#_OBX-3_Observation_Identifier)\|\|[BLADDER WASH](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[BCH^Brief clinical History^VA080](#_OBX-3_Observation_Identifier)\|\|[HX BLADDER CA](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[3](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[MICRO^Microscopic Examination^VA080](#_OBX-3_Observation_Identifier)\|\|[CLASS I (Absence of atypical cells.)](#_OBX-5_Observation_Value)\|\|\|\|\|\| [F](#_OBX-11_Observation_Result_Status)

4.  Inpatient

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[INAD^Admitting Diagnosis^VA080](#_OBX-3_Observation_Identifier)\|\|[309.4](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[INPRI^Primary Dis Diagnosis^VA080](#_OBX-3_Observation_Identifier)\|\|[204.9](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[3](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[INDIS^Discharge Diagnosis^VA080](#_OBX-3_Observation_Identifier)\|\|[301.2](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[4](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[INBED^Bedsection Diagnosis^VA080](#_OBX-4_Observation_Sub-ID)\|\|[301.3~303.2](#_OBX-5_Observation_Value)\|[Bed Section](#_OBX-6_Units)\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)\|[199504151100-0600](#_OBX-12_Date_Last_Observation Normal)\|\|[199404151100-0600](#_OBX-14_Date/Time_of_the Observation)

OBX\|[5](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[INSURG^Surgical Procedures^VA080](#_OBX-3_Observation_Identifier)\|\|[84.3~34.3](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)\|\| \|[199504151100-0600](#_OBX-14_Date/Time_of_the Observation)

OBX\|[6](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[INOTR^Other Diagnosis^VA080](#_OBX-3_Observation_Identifier)\|\|[83.1~93.1](#_OBX-5_Observation_Value)\|[Bed Section](#_OBX-6_Units)\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)\|\|\|[199504151100-0600](#_OBX-14_Date/Time_of_the Observation)

5.  Immunization

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|\|[^TETANUS DIPTHERIA (TD-ADULT)](#_OBX-3_Observation_Identifier)\|\|^0\|\|\|\|\|\|\|\|\|20000315\|\|\|\|\|[200003151100-0400](#_OBX-14_Date/Time_of_the Observation)

6.  IV

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[ADD^Additive^VA080](#_OBX-3_Observation_Identifier)\|\|[Addative text](\l)\|\|[300](#_OBX-7_References_Range)\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[SOL^Solution^VA080](#_OBX-3_Observation_Identifier)\|\|[Solution text](#_OBX-5_Observation_Value)\|\|[300ml](#_OBX-7_References_Range)\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[3](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[OTPR^Other Print info.^VA080](#_OBX-3_Observation_Identifier)\|\|[Other print text](\l)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

7.  Laboratory Data

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|\|[777-3^PLATELETS:NCNC:PT:BLD:QN:AUTOMATED COUNT^LN](\l)

[^85570.0000^Platelet Count Whole Blood^99VA64](\l)\|\|[3.6](#_OBX-5_Observation_Value)\|[g/dL](#_OBX-6_Units)\|[3.3-4.8](#_OBX-7_References_Range)\|\|\|\|[F](#_OBX-11_Observation_Result_Status)\|\|[2](#_OBX-13_User_Defined_Access Checks)\|[20020129082501-0700](#_OBX-14_Date/Time_of_the Observation)\|[612GF^MARTINEZ O PC/CREC^99VA4](#_OBX-13_User_Defined_Access_Checks)

\|[617-VA612GF^](#_OBX-16_Responsible_Observer)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|\|[LABC](\l)\|[LCOMM](#_OBX-4_Observation_Sub-ID)\|[Lab Comments go here](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[3](#_OBX-1_Set_ID_– OBX)\|\|[777-3^PLATELETS:NCNC:PT:BLD:QN:AUTOMATED COUNT^LN](\l)

[^85570.0000^Platelet Count Whole Blood^99VA64](\l)\|[PRICE](#_OBX-4_Observation_Sub-ID)\|[300](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status) \|\|\|[200502281000-0800](#_OBX-14_Date/Time_of_the Observation)\|[640^PALO ALTO HEALTH CARE SYSTEM - PALO ALTO DIVSION^99VA4](#_OBX-13_User_Defined_Access Checks)\|[2785-640^DEVINZI^LARCY](#_OBX-16_Responsible_Observer_1)\|[.3112^CHEM 1^99VA64_2](#_OBX-17)\|

8.  Med. Proc. (EKG)

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[INT^Interpretation^VA080](#_OBX-3_Observation_Identifier)\|[CHANGES OR SERIAL](#_OBX-4_Observation_Sub-ID)\|[RECOMMEND CLINICAL CORRELATION](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[AUTO^Auto Instrument^VA080](#_OBX-3_Observation_Identifier)\|\|[This is the Auto-Instrument Diagnosis, which is a free text word processing field](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

9.  Microbiology

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[BACT^Bact^VA080](#_OBX-3_Observation_Identifier)\|\|[Bact Remarks](\l)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[GRAM^Gram Stain^VA080](#_OBX-3_Observation_Identifier)\|\|[Gram Stain Text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[3](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[ORGC^Org Comment^VA080](#_OBX-3_Observation_Identifier)\|\|[Org Comment](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[4](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[ORG^Organism^VA080](#_OBX-3_Observation_Identifier)\|\|[Organism Comment](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[5](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[ORGQ^Quantitiy^VA080](#_OBX-3_Observation_Identifier)\|\|[Organism Quantity](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[6](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[PAR^Parasite^VA080](#_OBX-3_Observation_Identifier)\|\|[Parasite Text](#_OBX-5_Observation_Value)\|[T](#_OBX-6_Units)\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[7](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[PARQ^Quantity^VA080](#_OBX-3_Observation_Identifier)\|\|[Parasite Quantity Text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[8](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[PARC^Comment^VA080](#_OBX-3_Observation_Identifier)\|\|[Parasite Comment Text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[9](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[PARP^Parasite Remark^VA080](#_OBX-3_Observation_Identifier)\|\|[Parasite Remark](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[10](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[COMP^Specimen Comment^VA080](#_OBX-3_Observation_Identifier)\|\|[Specimen Comment](\l)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

10. Outpatient

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[OCPT^Procedures^VA080](#_OBX-3_Observation_Identifier)\|\|[93455](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)\|\|\|\|

\|[2177^^^^^^^^^^^^PHYSICIAN](#_OBX-16_Responsible_Observer)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[OICD9^Diagnosis^VA080](#_OBX-3_Observation_Identifier)\|\|[309.2](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

11. Problem List

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[PRVN^Provider Narrative^VA080](#_OBX-3_Observation_Identifier)\|\|[Mood Disorder in conditions classified elsewhere (ICD-9-CM 293.83)](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[EXPR^Expression^VA080](#_OBX-3_Observation_Identifier)\|\|[Unresolved](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[NOTE^Note Narrative^VA080](#_OBX-3_Observation_Identifier)\|\|[Note goes here](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

12. Radiology

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[RT^Report Text^VA080](#_OBX-3_Observation_Identifier)\|\|[This is where the report test goes](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[IT^Impression Text^VA080](#_OBX-3_Observation_Identifier)\|\|[This is where the impression text goes](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[3](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[ACH^Additional Clinical History^VA080](#_OBX-3_Observation_Identifier)\|\|[This is where the additional clinical information goes](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

13. Skin Test

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|\|[^PPD](#_OBX-3_Observation_Identifier)\|\|[N^2](#_OBX-5_Observation_Value)\|\|\|\|\|\|\|\|\|20010518\|\|\|\|\|200105181015-0400

14. Surgical Pathology

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[SPEC^Specimen^VA080](#_OBX-3_Observation_Identifier)\|\|[This is the specimen text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[BCH^Brief clinical History^VA080](#_OBX-3_Observation_Identifier)\|\|[Clinical history text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[3](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[PDIAG^Preoperative Diagnosis^VA080](#_OBX-3_Observation_Identifier)\|\|[Preoperative diagnosis text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[4](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[OF^Operative Findings^VA080](#_OBX-3_Observation_Identifier)\|\|[Operative findings text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[5](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[POPDIAG^Postoperative Diagnosis^VA080](#_OBX-3_Observation_Identifier)\|\|[Preoperative text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[6](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[GDESC^Gross Decription^VA080](#_OBX-3_Observation_Identifier)\|\|[Gross description text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[7](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[MDESC^Microscopic Description^VA080](#_OBX-3_Observation_Identifier)\|\|[Microscopic description text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[8](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[SPDIAG^Surgical Pathology Diagnosis^VA080](#_OBX-3_Observation_Identifier)\|\|[Surgical pathology text](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

OBX\|[9](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[ICD9^ICD9^VA080](#_OBX-3_Observation_Identifier)\|\|[304.6](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

15. Vitals

OBX\|[1](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[BP^Blood Pressue^VA080](#_OBX-3_Observation_Identifier)\|[5853632](#_OBX-4_Observation_Sub-ID)\|[136/72\S\SITTING\S\L ARM;SITTING;CUFF;ADULT](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)\|\|\|[20050228091501-0800](#_OBX-14_Date/Time_of_the Observation)

OBX\|[2](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[T^Tempreture^VA080](#_OBX-3_Observation_Identifier)\|[5853636](#_OBX-4_Observation_Sub-ID)\|[98.2\S\\S\ORAL](#_OBX-5_Observation_Value)\|[36.8](#_OBX-6_Units)\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

\|\|\|[20050228091501-0800](#_OBX-14_Date/Time_of_the Observation)

OBX\|[3](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[R^Respiration^VA080](#_OBX-3_Observation_Identifier)\|[5853635](#_OBX-4_Observation_Sub-ID)\|[13\S\\S\SPONTANEOUS](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

\|\|\|[200502280915-0800](#_OBX-14_Date/Time_of_the Observation)

OBX\|[4](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[P^Pulse^VA080](#_OBX-3_Observation_Identifier)\|[5853634](#_OBX-4_Observation_Sub-ID)\|[76\S\\S\RADIAL;PALPATED](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

\|\|\|[20050228091501-0800](#_OBX-14_Date/Time_of_the Observation)

OBX\|[5](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[PN^Pain^VA080](#_OBX-3_Observation_Identifier)\|[5853633](#_OBX-4_Observation_Sub-ID)\|[0\S\\S\\](#_OBX-5_Observation_Value)\|\|\|\|\|\|[F](#_OBX-11_Observation_Result_Status)\|\|\|[20050228091501-0800](#_OBX-14_Date/Time_of_the Observation)

OBX\|[6](#_OBX-1_Set_ID_– OBX)\|[FT](#_OBX-2_Value_Type)\|[WT^Weight^VA080](#_OBX-3_Observation_Identifier)\|[5844022](#_OBX-4_Observation_Sub-ID)\|[195.7\S\\S\\](#_OBX-5_Observation_Value)\|[88.95](#_OBX-6_Units)\|[27](#_OBX-7_References_Range)\|\|\|\|[F](#_OBX-11_Observation_Result_Status)

\|\|\|[200502281300-0800](#_OBX-14_Date/Time_of_the Observation)

1.  <span id="_ORC_–_Common_Order_Segment" class="anchor"></span>ORC – Common Order Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL# | Field Name                       | CCR                                             |
|-----|-----|-----|-----|------|------|----------------------------------|-------------------------------------------------|
| 1   | 2   | ID  | R   | N    | 0119 | Order Control                    | [See Notes](#_ORC-1_Order_Control)              |
| 2   | 22  | EI  | C   |      |      | Placer Order Number              | [See Notes](#_ORC-2_Placer_Order_Number)        |
| 3   | 22  | EI  | C   |      |      | Filler Order Number              | N/A                                             |
| 4   | 22  | EI  | O   |      |      | Placer Group Number              | N/A                                             |
| 5   | 2   | ID  | O   | N    | 0038 | Order Status                     | [See Notes](#_ORC-9_Date/Time_of_Transaction)   |
| 6   | 1   | ID  | O   |      | 0121 | Response Flag                    | N/A                                             |
| 7   | 200 | TQ  | O   | Y    |      | Quantity/Timing                  | N/A                                             |
| 8   | 200 | CM  | O   |      |      | Parent                           | N/A                                             |
| 9   | 26  | TS  | O   |      |      | Date/Time of Transaction         | [See Notes](#ORC_9)                             |
| 10  | 250 | XCN | O   | Y    |      | Entered By                       | N/A                                             |
| 11  | 250 | XCN | O   | Y    |      | Verified By                      | N/A                                             |
| 12  | 250 | XCN | O   | Y    |      | Ordering Provider                | [See Notes](#_ORC-12_Ordering_Provider)         |
| 13  | 80  | PL  | O   |      |      | Enterer's Location               | N/A                                             |
| 14  | 250 | XTN | O   | Y/2  |      | Call Back Phone Number           | N/A                                             |
| 15  | 26  | TS  | O   |      |      | Order Effective Date/Time        | [See Notes](#_ORC-15_Order_Effective_Date/Time) |
| 16  | 250 | CE  | O   |      |      | Order Control Code Reason        | [See Notes](#_ORC-16_Order_Control_Code Reason) |
| 17  | 250 | CE  | O   |      |      | Entering Organization            | [See Notes](#_ORC-17_Entering_Organization)     |
| 18  | 250 | CE  | O   |      |      | Entering Device                  | N/A                                             |
| 19  | 250 | XCN | O   | Y    |      | Action By                        | N/A                                             |
| 20  | 250 | CE  | O   |      | 0339 | Advanced Beneficiary Notice Code | N/A                                             |
| 21  | 250 | XON | O   | Y    |      | Ordering Facility Name           | N/A                                             |
| 22  | 250 | XAD | O   | Y    |      | Ordering Facility Address        | N/A                                             |
| 23  | XTN | O   | Y   |      | XTN  | Ordering Facility Phone Number   | N/A                                             |
| 24  | XAD | O   | Y   |      | XAD  | Ordering Provider Address        | N/A                                             |
| 25  | CWE | O   | N   |      | CWE  | Order Status Modifier            | N/A                                             |

1.  Field Definitions
    1.  <span id="_ORC-1_Order_Control" class="anchor"></span>ORC-1 Order Control

|             |                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field determines the function of the order segment. For this interface the code will be set to indicate results follow. |
| Example:    | NW                                                                                                                       |

2.  <span id="_ORC-2_Placer_Order_Number" class="anchor"></span>ORC-2 Placer Order Number

|     |     |      |                   |        |
|-----|-----|------|-------------------|--------|
| SEQ | DT  | TBL# | Component Name    | CCR    |
| 1   | ST  |      | Entity Identifier | Number |
| 2   | IS  |      | Namespace ID      | Type   |
| 3   | ST  |      | Universal ID      | N/A    |
| 4   | ID  |      | Universal ID Type | N/A    |

|             |                                                                                  |                                |
|-------------|----------------------------------------------------------------------------------|--------------------------------|
| Definition: | This field contains an order number associated with the pharmacy data to follow. |                                |
|             | Inpatient:                                                                       | \<Order Number\>^IP        |
|             | Outpatient:                                                                      | \<Prescription Number\>^OP |
|             | Non-VA Meds:                                                                     | \<52.2 IEN\>^NVA           |
| Example:    | 1000000429^OP                                                                |                                |

3.  <span id="_ORC-9_Date/Time_of_Transaction" class="anchor"></span>ORC-5 Order Status

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="4">Definition:</td>
<td colspan="2">This field contains the status of the order.</td>
</tr>
<tr class="even">
<td>Inpatient:</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Outpatient:</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Non-VA Meds:</td>
<td><p>[???]<strong>^IP</strong> (Active)</p>
<p>[???]<strong>^DC</strong> (Discontinued)</p></td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><p><strong>[???]^IP</strong></p>
<p><strong>[???]^DC</strong></p></td>
</tr>
</tbody>
</table>

4.  <span id="ORC_9" class="anchor"></span>ORC-9 Date/Time of Transaction

|             |                                                      |                      |
|-------------|------------------------------------------------------|----------------------|
| Definition: | This field is populated in the following cases only: |                      |
|             | Outpatient:                                          | Release Date/Time    |
|             | Non-VA Meds:                                         | Documented Date/Time |
| Format:     | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]          |                      |
| Example:    | 20041006                                         |                      |

5.  <span id="_ORC-12_Ordering_Provider" class="anchor"></span>ORC-12 Ordering Provider

| SEQ | DT  | TBL# | Component Name                                     | CCR                                           |
|-----|-----|------|----------------------------------------------------|-----------------------------------------------|
| 1   | ST  |      | ID Number                                          | IEN of the user in the NEW PERSON file (#200) |
| 2   | FN  |      | Family Name                                        | N/A                                           |
| 3   | ST  |      | Given Name                                         | N/A                                           |
| 4   | ST  |      | Second and further given names or initials thereof | N/A                                           |
| 5   | ST  |      | Suffix (e.g., JR or III)                           | N/A                                           |
| 6   | ST  |      | Prefix (e.g., DR)                                  | N/A                                           |
| 7   | IS  | 0360 | Degree (e.g., MD)                                  | N/A                                           |
| 8   | IS  | 0297 | Source Table                                       | N/A                                           |
| 9   | HD  |      | Assigning Authority                                | N/A                                           |
| 10  | ID  | 0200 | Name Type Code                                     | N/A                                           |
| 11  | ST  |      | Identifier Check Digit                             | N/A                                           |
| 12  | ID  | 0061 | Code identifying the check digit scheme employed   | N/A                                           |
| 13  | IS  |      | Identifier Type Code                               | Provider Class Name                           |
| 14  | HD  |      | Assigning Facility                                 | N/A                                           |
| 15  | ID  | 0465 | Name Representation Code                           | N/A                                           |
| 16  | CE  | 0448 | Name Context                                       | N/A                                           |
| 17  | DR  |      | Name Validity Range                                | N/A                                           |
| 18  | ID  | 0444 | Name Assembly Order                                | N/A                                           |

|             |                                                                                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------------|
| Definition: | This field identifies the individual responsible for the request. Names are not used to ensure data protection. |
| Format:     | Documented By IEN^^^^^^^^^^^^PROVIDER CLASS                                                                     |
| Example:    | 2177^^^^^^^^^^^^PHD                                                                                         |

6.  <span id="_ORC-15_Order_Effective_Date/Time" class="anchor"></span>ORC-15 Order Effective Date/Time

|             |                                                |
|-------------|------------------------------------------------|
| Definition: | This field contains the order start date/time. |
| Format:     | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]    |
| Example:    | 200503140944-0800                          |

7.  ORC-16 Order Control Code Reason

|     |     |      |                                 |         |
|-----|-----|------|---------------------------------|---------|
| SEQ | DT  | TBL# | Component Name                  | CCR     |
| 1   | ST  | 0005 | Identifier                      | N/A     |
| 2   | ST  |      | Text                            | N/A     |
| 3   | ST  |      | Name of Coding System           | N/A     |
| 4   | ST  |      | Alternate Identifier            | N/A     |
| 5   | ST  |      | Alternate Text                  | NEW |
| 6   | ST  |      | Name of Alternate Coding System | N/A     |

|             |                                                                                            |
|-------------|--------------------------------------------------------------------------------------------|
| Definition: | This field identifies the reason for the order. For this interface, it will be set to new. |
| Value:      | ^^^^NEW                                                                                |

8.  <span id="_ORC-17_Entering_Organization" class="anchor"></span>ORC-17 Entering Organization

|     |     |      |                                 |                  |
|-----|-----|------|---------------------------------|------------------|
| SEQ | DT  | TBL# | Component Name                  | CCR              |
| 1   | ST  | 0005 | Identifier                      | Station Number   |
| 2   | ST  |      | Text                            | Institution Name |
| 3   | ST  |      | Name of Coding System           | 99VA64       |
| 4   | ST  |      | Alternate Identifier            | N/A              |
| 5   | ST  |      | Alternate Text                  | N/A              |
| 6   | ST  |      | Name of Alternate Coding System | N/A              |

|             |                                                                |
|-------------|----------------------------------------------------------------|
| Definition: | This field distinguishes the station where the order was made. |
| Format:     | Station Number^Station Name^99VA4                          |
| Value:      | 499^HINES OIFO^99VA4                                       |

2.  Sample ORC Segments
    1.  Inpatient

ORC\|[NW](#_ORC-1_Order_Control)\|[7338989V2726709^IP](#_ORC-2_Placer_Order_Number)\|\|\|\|\|\|\|\|\|\|[43882^^^^^^^^^^^^RESIDENT](#_ORC-12_Ordering_Provider)\|\|

\|[200503140944-0800](#_ORC-15_Order_Effective_Date/Time)\|[^^^^NEW](#_ORC-16_Order_Control_Code Reason)\|[640^PALO ALTO HCS^99VA4](#_ORC-17_Entering_Organization)

2.  Outpatient

ORC\|[NW](#_ORC-1_Order_Control)\|[5666184^OP](#_ORC-2_Placer_Order_Number)\|\|\|\|\|\|\|[20040517](#_ORC-9_Date/Time_of_Transaction)\|\|\|[7114^^^^^^^^^^^^NURSE PRACTITIONER](#_ORC-12_Ordering_Provider)\|\|\|[20040507](#_ORC-15_Order_Effective_Date/Time)\|[^^^^NEW](#_ORC-16_Order_Control_Code Reason)\|[640^PALO ALTO HCS^99VA4](#_ORC-17_Entering_Organization)

3.  Non-VA Meds

ORC\|NW\|1^NVA\|\|\|IP\|\|\|\|20070210150448-0500\|\|\|2229^^^^^^^^^^^^PHYSICIAN\|\|\|\|^^^^NEW\|442^CHEYENNE VAMC^99VA4

2.  <span id="_PID_–_Patient" class="anchor"></span>PID – Patient ID Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL#           | Field Name                        | CCR                                     |
|-----|-----|-----|-----|------|----------------|-----------------------------------|-----------------------------------------|
| 1   | 4   | SI  | O   |      |                | Set ID - PID                      | [See Notes](#_PID-2_Patient_ID)         |
| 2   | 20  | CX  | B   |      |                | Patient ID                        | N/A                                     |
| 3   | 250 | CX  | R   | Y    |                | Patient Identifier List           | [See Notes](#_PID-2_Patient_ID_1)       |
| 4   | 20  | CX  | B   | Y    |                | Alternate Patient ID - PID        | N/A                                     |
| 5   | 250 | XPN | R   | Y    |                | Patient Name                      | [See Notes](#_PID-5_Patient_Name_1)     |
| 6   | 250 | XPN | O   | Y    |                | Mother's Maiden Name              | N/A                                     |
| 7   | 26  | TS  | O   |      |                | Date/Time of Birth                | [See Notes](#_PID-7_Date/Time_of_Birth) |
| 8   | 1   | IS  | O   |      | [0001](#T0001) | Sex                               | [See Notes](#_PID-8_Sex)                |
| 9   | 250 | XPN | O   | Y    |                | Patient Alias                     | N/A                                     |
| 10  | 250 | CE  | O   | Y    | 0005           | Race and Collection Method        | [See Notes](#_PID-10_Race_and)          |
| 11  | 250 | XAD | O   | Y    |                | Patient Address                   | [See Notes](#_PID-11_Patient_address)   |
| 12  | 4   | IS  | B   |      | 0289           | County Code                       | N/A                                     |
| 13  | 250 | XTN | O   | Y    |                | Phone Number - Home               | N/A                                     |
| 14  | 250 | XTN | O   | Y    |                | Phone Number - Business           | N/A                                     |
| 15  | 250 | CE  | O   |      | 0296           | Primary Language                  | N/A                                     |
| 16  | 250 | CE  | O   |      | 0002           | Marital Status                    | N/A                                     |
| 17  | 250 | CE  | O   |      | 0006           | Religion                          | N/A                                     |
| 18  | 250 | CX  | O   |      |                | Patient Account Number            | N/A                                     |
| 19  | 16  | ST  | B   |      |                | SSN Number - Patient              | [See Notes](#_PID-19_SSN_–)             |
| 20  | 25  | DLN | O   |      |                | Driver's License Number - Patient | N/A                                     |
| 21  | 250 | CX  | O   | Y    |                | Mother's Identifier               | N/A                                     |
| 22  | 250 | CE  | O   | Y    | 0189           | Ethnic Group                      | [See Notes](#_PID-22_Ethnicity_and)     |
| 23  | 250 | ST  | O   |      |                | Birth Place                       | N/A                                     |
| 24  | 1   | ID  | O   |      | 0136           | Multiple Birth Indicator          | N/A                                     |
| 25  | 2   | NM  | O   |      |                | Birth Order                       | N/A                                     |
| 26  | 250 | CE  | O   | Y    | 0171           | Citizenship                       | N/A                                     |
| 27  | 250 | CE  | O   |      | 0172           | Veterans Military Status          | N/A                                     |
| 28  | 250 | CE  | O   |      | 0212           | Nationality                       | N/A                                     |
| 29  | 26  | TS  | O   |      |                | Patient Death Date and Time       | [See Notes](#_PID-29_Patient_Death)     |
| 30  | 1   | ID  | O   |      | 0136           | Patient Death Indicator           | N/A                                     |
| 31  | 1   | ID  | O   |      | 0136           | Identity Unknown Indicator        | N/A                                     |
| 32  | 20  | IS  | O   | Y    | 0445           | Identity Reliability Code         | N/A                                     |
| 33  | 26  | TS  | O   |      |                | Last Update Date/Time             | N/A                                     |
| 34  | 40  | HD  | O   |      |                | Last Update Facility              | N/A                                     |
| 35  | 250 | CE  | C   |      | 0446           | Species Code                      | N/A                                     |
| 36  | 250 | CE  | C   |      | 0447           | Breed Code                        | N/A                                     |
| 37  | 80  | ST  | O   |      |                | Strain                            | N/A                                     |
| 38  | 250 | CE  | O   | 2    | 0429           | Production Class Code             | N/A                                     |

1.  Field Definitions
    1.  <span id="_PID-2_Patient_ID" class="anchor"></span>PID-1 Set ID – PID

|             |                                                                                                                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the number that identifies this transaction. For the first occurrence of the segment, the sequence number shall be one, for the second occurrence, the sequence number shall be two, etc. |
| Value:      | 2                                                                                                                                                                                                         |

2.  <span id="_PID-2_Patient_ID_1" class="anchor"></span>PID-3 Patient Identifier List

|     |     |                |                                |     |
|-----|-----|----------------|--------------------------------|-----|
| SEQ | DT  | TBL#           | Component Name                 | CCR |
| 1   | ST  |                | ID                             |     |
| 2   | ST  |                | Check Digit                    |     |
| 3   | ID  | [0061](#T0061) | Code of the Check Digit Scheme |     |
| 4   | HD  | 0363           | Assigning Authority            |     |
| 5   | ID  | [0203](#T0203) | Identifier Type Code           |     |
| 6   | HD  |                | Assigning Facility             |     |
| 7   | DT  |                | Effective Date                 | N/A |
| 8   | DT  |                | Expiration Date                | N/A |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="4">Definition:</td>
<td colspan="2"><p>This field contains the list of identifiers (one or more) used by the healthcare facility to uniquely identify a patient (e.g., medical record number, billing number, birth registry, national unique individual identifier, etc.).</p>
<p>Currently, the CCR package uses 2 identifiers: Patient IEN (DFN) and Integration Control Number (if available). Patient IEN is concatenated with the station number by the receiver to create a unique identifier.</p></td>
</tr>
<tr class="even">
<td>ICN:</td>
<td>&lt;ICN&gt;<strong>^^^USVHA&amp;&amp;0363^NI^VA FACILITY ID&amp;</strong>&lt;Station Number&gt;<strong>&amp;L</strong></td>
</tr>
<tr class="odd">
<td>Patient EIN:</td>
<td>&lt;DFN&gt;<strong>^^^USVHA&amp;&amp;0363^PI^VA FACILITY ID&amp;</strong>&lt;Station Number&gt;<strong>&amp;L</strong></td>
</tr>
<tr class="even">
<td>Registry State:</td>
<td><p>PID segments in the registry-wide section of the batch utilize the following format of this field:</p>
<p><strong>0^^^^U</strong></p></td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><p><strong>1243567890V123456^^^USVHA&amp;&amp;0363^NI^VA FACILITY ID&amp;640&amp;L</strong></p>
<p><strong>~325500^^^USVHA&amp;&amp;0363^PI^VA FACILITY ID&amp;640&amp;L</strong></p></td>
</tr>
</tbody>
</table>

3.  <span id="_PID-5_Patient_Name_1" class="anchor"></span>PID-5 Patient Name

|             |                    |                                                                                                                                                            |
|-------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | Clinical Data:     |                                                                                                                                                            |
|             | Registry Data:     | Despite the fact that the *Patient Name* field is a required one, it is not populated in regular PID segments due to patient privacy and security reasons. |
|             | Registry State:    | PID segments in the registry-wide section of the batch have PSEUDO^PATIENT string in this field.                                                       |
| Example:    | PSEUDO^PATIENT |                                                                                                                                                            |

4.  <span id="_PID-7_Date/Time_of_Birth" class="anchor"></span>PID-7 Date/Time of Birth

|             |                                                          |
|-------------|----------------------------------------------------------|
| Definition: | This field contains the patient's date of birth.         |
| Format:     | YYYYMMDD (either day or both month and day can be zeros) |
| Example:    | 19521027                                             |

5.  <span id="_PID-8_Sex" class="anchor"></span>PID-8 Sex

|             |                                                                        |             |
|-------------|------------------------------------------------------------------------|-------------|
| Definition: | This field contains the patient's sex.                                 |             |
| Tables:     | A subset of the [HL7 Table 0001 - Administrative sex](#T0001) is used: |             |
|             | Value                                                                  | Description |
|             | F                                                                      | Female      |
|             | M                                                                      | Male        |
|             | O                                                                      | Other       |
|             | U                                                                      | Unknown     |
| Example:    | F                                                                  |             |

6.  <span id="_PID-10_Race_and" class="anchor"></span>PID-10 Race and Collection Method

|     |     |      |                                 |     |
|-----|-----|------|---------------------------------|-----|
| SEQ | DT  | TBL# | Component Name                  | CCR |
| 1   | ST  | 0005 | Identifier                      |     |
| 2   | ST  |      | Text                            |     |
| 3   | ST  |      | Name of Coding System           |     |
| 4   | ST  |      | Alternate Identifier            |     |
| 5   | ST  |      | Alternate Text                  |     |
| 6   | ST  |      | Name of Alternate Coding System |     |

|             |                                                                                      |                                           |
|-------------|--------------------------------------------------------------------------------------|-------------------------------------------|
| Definition: | This field refers to the patient's race.                                             |                                           |
| Format:     | The *Identifier* has the following format: \<Race ID\>-\<Collection Method ID\>. |                                           |
| Tables:     | ID                                                                                   | Race                                      |
|             | 1002-5                                                                               | AMERICAN INDIAN OR ALASKA NATIVE          |
|             | 2028-9                                                                               | ASIAN                                     |
|             | 2054-5                                                                               | BLACK OR AFRICAN MAERICAN                 |
|             | 2076-8                                                                               | NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER |
|             | 2106-3                                                                               | WHITE                                     |
|             | 0000-0                                                                               | DECLINED TO ANSWER                        |
|             | 9999-4                                                                               | UNKNOWN BY PATIENT                        |
|             | ID                                                                                   | Collection method                         |
|             | SLF                                                                                  | SELF IDENTIFICATION                       |
|             | PRX                                                                                  | PROXY                                     |
|             | OBS                                                                                  | OBSERVER                                  |
|             | UNK                                                                                  | UNKNOWN                                   |
| Example:    | 2106-3-SLF^WHITE^0005^2106-3^WHITE^CDC                                           |                                           |

7.  <span id="_PID-11_Patient_address" class="anchor"></span>PID-11 Patient address

| SEQ | DT  | TBL# | Component Name               | CCR |
|-----|-----|------|------------------------------|-----|
| 1   | ST  |      | Street Address               | N/A |
| 2   | ST  |      | Other Designation            | N/A |
| 3   | ST  |      | City                         | N/A |
| 4   | ST  |      | State or Province            | N/A |
| 5   | ST  |      | ZIP or Postal Code           |     |
| 6   | ID  | 0399 | Country                      | N/A |
| 7   | ID  | 0190 | Address Type                 | N/A |
| 8   | ST  |      | Other Geographic Designation | N/A |
| 9   | IS  | 0289 | County/Parish Code           | N/A |
| 10  | IS  | 0288 | Census Tract                 | N/A |
| 11  | ID  | 0465 | Address Representation Code  | N/A |
| 12  | DR  |      | Address Validity Range       | N/A |

|             |                                                                                                        |
|-------------|--------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the mailing address of the patient. The CCR HL7 interface sends only the zip code. |
| Format:     | NNNNN\[-NNN\]                                                                                      |
| Example:    | ^^^^60141-7008                                                                                     |

8.  <span id="_PID-19_SSN_–" class="anchor"></span>PID-19 SSN Number - Patient

|             |                                                                                  |
|-------------|----------------------------------------------------------------------------------|
| Definition: | This field contains the encoded social security number of the patient.           |
| Format:     | NNNNNNNNNNN\[P\] (11 digits followed by optional indicator of a pseudo-SSN). |
| Example:    | 60129282062                                                                  |

9.  <span id="_PID-22_Ethnicity_and" class="anchor"></span>PID-22 Ethnic Group

|     |     |      |                                 |     |
|-----|-----|------|---------------------------------|-----|
| SEQ | DT  | TBL# | Component Name                  | CCR |
| 1   | ST  |      | Identifier                      |     |
| 2   | ST  |      | Text                            |     |
| 3   | ST  |      | Name of Coding System           |     |
| 4   | ST  |      | Alternate Identifier            |     |
| 5   | ST  |      | Alternate Text                  |     |
| 6   | ST  |      | Name of Alternate Coding System |     |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Definition:</td>
<td colspan="2">This field refers to the patient's ethnicity.</td>
</tr>
<tr class="even">
<td>Format:</td>
<td colspan="2">The <em>Identifier</em> has the following format: &lt;Ethnicity ID&gt;<strong>-</strong>&lt;Collection Method ID&gt;.</td>
</tr>
<tr class="odd">
<td rowspan="10">Tables:</td>
<td>ID</td>
<td>Ethnicity</td>
</tr>
<tr class="even">
<td>2135-2</td>
<td>HISPANIC OR LATINO</td>
</tr>
<tr class="odd">
<td>2165-5</td>
<td>NOT HISPANIC OR LATINO</td>
</tr>
<tr class="even">
<td>0000-0</td>
<td>DECLINED TO ANSWER</td>
</tr>
<tr class="odd">
<td>9999-4</td>
<td>UNKNOWN BY PATIENT</td>
</tr>
<tr class="even">
<td>ID</td>
<td>Collection method</td>
</tr>
<tr class="odd">
<td>SLF</td>
<td>SELF IDENTIFICATION</td>
</tr>
<tr class="even">
<td>PRX</td>
<td>PROXY</td>
</tr>
<tr class="odd">
<td>OBS</td>
<td>OBSERVER</td>
</tr>
<tr class="even">
<td>UNK</td>
<td>UNKNOWN</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><p><strong>2186-5-SLF^NOT HISPANIC OR LATINO^0189</strong></p>
<p><strong>^2186-5^NOT HISPANIC OR LATINO^CDC</strong></p></td>
</tr>
</tbody>
</table>

10. <span id="_PID-29_Patient_Death" class="anchor"></span>PID-29 Patient Death Date and Time

|             |                                                                   |
|-------------|-------------------------------------------------------------------|
| Definition: | This field contains the date on which the patient death occurred. |
| Format:     | YYYYMMDD\[hhmm\[ss\]\] \[+\|-zzzz\]                       |
| Example:    | 195210271230                                                  |

2.  Sample PID Segment

PID\|[1](#_PID-2_Patient_ID)\|\|[1243567890V123456^^^USVHA&&0363^NI^VA FACILITY ID&640&L~325500^^^USVHA&&0363^PI^VA FACILITY ID&640&L](#_PID-2_Patient_ID_1)\|\|\|\|[19630408](#_PID-7_Date/Time_of_Birth)\|[M](#_PID-8_Sex)\|\|[2106-3-SLF^WHITE^0005^2106-3^WHITE^CDC](#_PID-10_Race_and)\|[^^^^95123](#_PID-11_Patient_address)\|\|\|\|\|\|\|\|[00007600044](#_PID-19_SSN_–)\| \|\|[2186-5-SLF^NOT HISPANIC OR LATINO^0189^2186-5^NOT HISPANIC OR LATINO^CDC](#_PID-22_Ethnicity_and)\|\|\|\|\|\|\|[""](#_PID-29_Patient_Death)

3.  <span id="_ZSP_–_Service" class="anchor"></span>PV1 – Patient Visit Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL# | Field Name                | CCR                                            |
|-----|-----|-----|-----|------|------|---------------------------|------------------------------------------------|
| 1   | 4   | SI  | O   |      |      | Set ID - PV1              | [See Notes](#_PV1-1_Set_ID_– PV1)              |
| 2   | 1   | IS  | R   |      | 0004 | Patient Class             | [See Notes](#_PV1-2_Patient_Class)             |
| 3   | 80  | PL  | O   |      |      | Assigned Patient Location | [See Notes](#_PV1-3_Assigned_Patient_Location) |
| 4   | 2   | IS  | O   |      | 0007 | Admission Type            | [See Notes](#_PV1-4_Admission_Type)            |
| 5   | 250 | CX  | O   |      |      | Preadmit Number           | N/A                                            |
| 6   | 80  | PL  | O   |      |      | Prior Patient Location    | [See Notes](#_PV1-6_Prior_Patient_Location)    |
| 7   | 250 | XCN | O   | Y    | 0010 | Attending Doctor          | [See Notes](#_PV1-7_Attending_Doctor)          |
| 8   | 250 | XCN | O   | Y    | 0010 | Referring Doctor          | N/A                                            |
| 9   | 250 | XCN | B   | Y    | 0010 | Consulting Doctor         | N/A                                            |
| 10  | 3   | IS  | O   |      | 0069 | Hospital Service          | N/A                                            |
| 11  | 80  | PL  | O   |      |      | Temporary Location        | N/A                                            |
| 12  | 2   | IS  | O   |      | 0087 | Preadmit Test Indicator   | N/A                                            |
| 13  | 2   | IS  | O   |      | 0092 | Re-admission Indicator    | N/A                                            |
| 14  | 6   | IS  | O   |      | 0023 | Admit Source              | N/A                                            |
| 15  | 2   | IS  | O   | Y    | 0009 | Ambulatory Status         | N/A                                            |
| 16  | 2   | IS  | O   |      | 0099 | VIP Indicator             | N/A                                            |
| 17  | 250 | XCN | O   | Y    | 0010 | Admitting Doctor          | N/A                                            |
| 18  | 2   | IS  | O   |      | 0018 | Patient Type              | N/A                                            |
| 19  | 30  | CX  | O   |      |      | Visit Number              | [See Notes](#_PV1_-_19_ Visit Number)          |
| 20  | 50  | FC  | O   | Y    | 0064 | Financial Class           | N/A                                            |
| 21  | 2   | IS  | O   |      | 0032 | Charge Price Indicator    | N/A                                            |
| 22  | 2   | IS  | O   |      | 0045 | Courtesy Code             | N/A                                            |
| 23  | 2   | IS  | O   |      | 0046 | Credit Rating             | N/A                                            |
| 24  | 2   | IS  | O   | Y    | 0044 | Contract Code             | N/A                                            |
| 25  | 8   | DT  | O   | Y    |      | Contract Effective Date   | N/A                                            |
| 26  | 12  | NM  | O   | Y    |      | Contract Amount           | N/A                                            |
| 27  | 3   | NM  | O   | Y    |      | Contract Period           | N/A                                            |
| 28  | 2   | IS  | O   |      | 0073 | Interest Code             | N/A                                            |
| 29  | 1   | IS  | O   |      | 0110 | Transfer to Bad Debt Code | N/A                                            |
| 30  | 8   | DT  | O   |      |      | Transfer to Bad Debt Date | N/A                                            |
| 31  | 10  | IS  | O   |      | 0021 | Bad Debt Agency Code      | N/A                                            |
| 32  | 12  | NM  | O   |      |      | Bad Debt Transfer Amount  | N/A                                            |
| 33  | 12  | NM  | O   |      |      | Bad Debt Recovery Amount  | N/A                                            |
| 34  | 1   | IS  | O   |      | 0111 | Delete Account Indicator  | N/A                                            |
| 35  | 8   | DT  | O   |      |      | Delete Account Date       | N/A                                            |
| 36  | 3   | IS  | O   |      | 0112 | Discharge Disposition     | [See Notes](#_PV1_-_36_ Discharge Disposition) |
| 37  | 25  | CM  | O   |      | 0113 | Discharged to Location    | N/A                                            |
| 38  | 250 | CE  | O   |      | 0114 | Diet Type                 | N/A                                            |
| 39  | 2   | IS  | O   |      | 0115 | Servicing Facility        | N/A                                            |
| 40  | 1   | IS  | B   |      | 0116 | Bed Status                | N/A                                            |
| 41  | 2   | IS  | O   |      | 0117 | Account Status            | N/A                                            |
| 42  | 80  | PL  | O   |      |      | Pending Location          | N/A                                            |
| 43  | 80  | PL  | O   |      |      | Prior Temporary Location  | N/A                                            |
| 44  | 26  | TS  | O   |      |      | Admit Date/Time           | [See Notes](#_PV1-44_Admit_Date/Time)          |
| 45  | 26  | TS  | O   |      |      | Discharge Date/Time       | [See Notes](#_PV1-45_Discharge_Date/Time)      |
| 46  | 12  | NM  | O   |      |      | Current Patient Balance   | N/A                                            |
| 47  | 12  | NM  | O   |      |      | Total Charges             | N/A                                            |
| 48  | 12  | NM  | O   |      |      | Total Adjustments         | N/A                                            |
| 49  | 12  | NM  | O   |      |      | Total Payments            | N/A                                            |
| 50  | 250 | CX  | O   |      | 0203 | Alternate Visit ID        | N/A                                            |
| 51  | 1   | IS  | O   |      | 0326 | Visit Indicator           | [See Notes](#_PV1-51_Visit_Indicator)          |
| 52  | 250 | XCN | B   | Y    | 0010 | Other Healthcare Provider | N/A                                            |

1.  Field Definitions
    1.  PV1-1 Set ID – PV1

|             |                                                                                                                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the number that identifies this transaction. For the first occurrence of the segment, the sequence number shall be one, for the second occurrence, the sequence number shall be two, etc. |
| Example:    | 1                                                                                                                                                                                                         |

2.  <span id="_PV1-2_Patient_Class" class="anchor"></span>PV1-2 Patient Class

|             |                                                                     |             |
|-------------|---------------------------------------------------------------------|-------------|
| Definition: | This field is used to categorize patients by the type of admission. |             |
| Tables:     | Value                                                               | Description |
|             | I                                                                   | Inpatient   |
|             | O                                                                   | Outpatient  |
| Example:    | I                                                               |             |

3.  <span id="_PV1-3_Assigned_Patient_Location" class="anchor"></span>PV1-3 Assigned Patient Location

|     |     |      |                      |                                    |
|-----|-----|------|----------------------|------------------------------------|
| SEQ | DT  | TBL# | Component Name       | CCR                                |
| 1   | IS  |      | Point of Care        | Station Number                     |
| 2   | IS  |      | Room                 | N/A                                |
| 3   | IS  |      | Bed                  | N/A                                |
| 4   | HD  |      | Facility             | N/A                                |
| 5   | IS  |      | Location Status      | N/A                                |
| 6   | IS  |      | Person Location Type | Clinic Stop Code (for outpatients) |
| 7   | IS  |      | Building             | N/A                                |
| 8   | IS  |      | Floor                | N/A                                |
| 9   | ST  |      | Location Description | N/A                                |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="3">Definition:</td>
<td colspan="2">This field identifies the station where the admission took place.</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>Station number for inpatient admissions is returned by the $$SITE^VASITE function and its suffix is removed.</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td><p>IEN of the station for outpatient visits is returned by the ENCEVENT^ PXKENC procedure. The station number is extracted from the corresponding record of the MEDICAL CENTER DIVISION file (#40.8) and stored "as is" (potentially, with the suffix).</p>
<p>Outpatient visits also have the <em>Person Location Type</em> component set to the clinic stop code.</p></td>
</tr>
<tr class="even">
<td rowspan="2">Format:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>&lt;Station Number (without suffix)&gt;</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>&lt;Station Number&gt;<strong>^^^^^</strong>&lt;Clinic Stop Code&gt;</td>
</tr>
<tr class="even">
<td rowspan="2">Example:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td><strong>499</strong></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td><strong>499UX^^^^^203</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_PV1-4_Admission_Type" class="anchor"></span>PV1-4 Admission Type

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Admission Type</td>
</tr>
<tr class="odd">
<td rowspan="6">Tables:</td>
<td>Value</td>
<td>Description</td>
</tr>
<tr class="even">
<td>A</td>
<td>Ancillary</td>
</tr>
<tr class="odd">
<td>C</td>
<td>Credit Stop</td>
</tr>
<tr class="even">
<td>P</td>
<td>Primary</td>
</tr>
<tr class="odd">
<td>O</td>
<td>Occasion of Service</td>
</tr>
<tr class="even">
<td>S</td>
<td>Stop Code</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>P</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_PV1-6_Prior_Patient_Location" class="anchor"></span>PV1-6 Prior Patient Location

|     |     |      |                      |                                                                  |
|-----|-----|------|----------------------|------------------------------------------------------------------|
| SEQ | DT  | TBL# | Component Name       | CCR                                                              |
| 1   | IS  |      | Point of Care        | N/A                                                              |
| 2   | IS  |      | Room                 | N/A                                                              |
| 3   | IS  |      | Bed                  | IEN of the bed section (specialty) in the SPECIALTY file (#42.4) |
| 4   | HD  |      | Facility             | N/A                                                              |
| 5   | IS  |      | Location Status      | N/A                                                              |
| 6   | IS  |      | Person Location Type | N/A                                                              |
| 7   | IS  |      | Building             | N/A                                                              |
| 8   | IS  |      | Floor                | N/A                                                              |
| 9   | ST  |      | Location Description | Name of the bed section (the .01 field of the file \#42.4)       |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>Bed section at the time of discharge</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>^^71^^^^^^LONG TERM PSYCHIATRY(&gt;45 DAYS)</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_PV1-7_Attending_Doctor" class="anchor"></span>PV1-7 Attending Doctor

| SEQ | DT  | TBL# | Component Name                                     | CCR                                    |
|-----|-----|------|----------------------------------------------------|----------------------------------------|
| 1   | ST  |      | ID Number                                          | User IEN in the NEW PERSON file (#200) |
| 2   | FN  |      | Family Name                                        | N/A                                    |
| 3   | ST  |      | Given Name                                         | N/A                                    |
| 4   | ST  |      | Second and further given names or initials thereof | N/A                                    |
| 5   | ST  |      | Suffix (e.g., JR or III)                           | N/A                                    |
| 6   | ST  |      | Prefix (e.g., DR)                                  | N/A                                    |
| 7   | IS  | 0360 | Degree (e.g., MD)                                  | N/A                                    |
| 8   | IS  | 0297 | Source Table                                       | N/A                                    |
| 9   | HD  |      | Assigning Authority                                | N/A                                    |
| 10  | ID  | 0200 | Name Type Code                                     | N/A                                    |
| 11  | ST  |      | Identifier Check Digit                             | N/A                                    |
| 12  | ID  | 0061 | Code identifying the check digit scheme employed   | N/A                                    |
| 13  | IS  |      | Identifier Type Code                               | Provider Class Name                    |
| 14  | HD  |      | Assigning Facility                                 | N/A                                    |
| 15  | ID  | 0465 | Name Representation Code                           | N/A                                    |
| 16  | CE  | 0448 | Name Context                                       | N/A                                    |
| 17  | DR  |      | Name Validity Range                                | N/A                                    |
| 18  | ID  | 0444 | Name Assembly Order                                | N/A                                    |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Attending Physician(s). Provider names are not used to ensure the patient privacy protection.</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>2177^^^^^^^^^^^^PHYSICIAN</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_PV1_-_19__Visit_Number" class="anchor"></span>PV1-19 Visit Number

|     |     |      |                                                  |                  |
|-----|-----|------|--------------------------------------------------|------------------|
| SEQ | DT  | TBL# | Component Name                                   | CCR              |
| 1   | ST  |      | ID                                               | IEN of the Visit |
| 2   | ST  |      | Check Digit                                      | N/A              |
| 3   | ID  | 0061 | Code identifying the check digit scheme employed | N/A              |
| 4   | HD  |      | Assigning Authority                              | N/A              |
| 5   | ID  | 0203 | Identifier Type Code                             | N/A              |
| 6   | HD  |      | Assigning Facility                               | N/A              |
| 7   | DT  |      | Effective Date                                   | N/A              |
| 8   | DT  |      | Expiration Date                                  | N/A              |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="3">Definition:</td>
<td colspan="2">This field contains the IEN of the visit and can be used to link up with the OBR segment for this visit.</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>IEN of the record of the PTF CLOSE OUT file (#45.84)</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>IEN of the record of the VISIT file (#9000010)</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>8710273</strong></td>
</tr>
</tbody>
</table>

1.  PV1-36 Discharge Disposition

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="3">Definition:</td>
<td colspan="2">This field contains the…</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>Disposition Code of the patient at time of discharge</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td rowspan="8">Tables:</td>
<td>Value</td>
<td>Description</td>
</tr>
<tr class="odd">
<td>1</td>
<td>REGULAR</td>
</tr>
<tr class="even">
<td>2</td>
<td>NBC OR WHILE ASIH</td>
</tr>
<tr class="odd">
<td>3</td>
<td>EXPIRATION 6 MONTH LIMIT</td>
</tr>
<tr class="even">
<td>4</td>
<td>IRREGULAR</td>
</tr>
<tr class="odd">
<td>5</td>
<td>TRANSFER</td>
</tr>
<tr class="even">
<td>6</td>
<td>DEATH WITH AUTOPSY</td>
</tr>
<tr class="odd">
<td>7</td>
<td>DEATH WITHOUT AUTOPSY</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>4</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_PV1-44_Admit_Date/Time" class="anchor"></span>PV1-44 Admit Date/Time

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>Admission Date/Time</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Visit Date/Time</td>
</tr>
<tr class="odd">
<td>Format:</td>
<td colspan="2">YYYYMMDD[hhmm[ss]] [<strong>+</strong>|<strong>-</strong>zzzz]</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>200403020815-0800</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_PV1-45_Discharge_Date/Time" class="anchor"></span>PV1-45 Discharge Date/Time

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>Discharge Date/Time</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Format:</td>
<td colspan="2">YYYYMMDD[hhmm[ss]] [+|-zzzz]</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>200403020815-0800</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_PV1-51_Visit_Indicator" class="anchor"></span>PV1-51 Visit Indicator

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Indicates if the visit has been deleted</td>
</tr>
<tr class="odd">
<td rowspan="3">Tables:</td>
<td>Value</td>
<td>Description</td>
</tr>
<tr class="even">
<td>0</td>
<td>Active</td>
</tr>
<tr class="odd">
<td>1</td>
<td>Deleted</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>0</strong></td>
</tr>
</tbody>
</table>

1.  Sample PV1 Segment

PV1\|[1](#_PV1-1_Set_ID_– PV1)\|[O](#_PV1-2_Patient_Class)\|[640^^^^^408](#_PV1-3_Assigned_Patient_Location)\|[P](#_PV1-4_Admission_Type)\|\|\|[10935^^^^^^^^^^^^PHYSICIAN](#_PV1-7_Attending_Doctor)\|\|\|\|\|\|\|\|\|\|\|

\|[8710273](#_PV1_-_19__Visit_Number)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[200403020815-0800](#_PV1-44_Admit_Date/Time)\|\|\|\|\|\|[0](#_PV1-51_Visit_Indicator)

1.  <span id="_RXE_–_Pharmacy/Treatment_Encoded_Or" class="anchor"></span>RXE – Pharmacy/Treatment Encoded Order Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL#           | Field Name                                                    | CCR                                                  |
|-----|-----|-----|-----|------|----------------|---------------------------------------------------------------|------------------------------------------------------|
| 1   | 200 | TQ  | R   |      |                | Quantity/Timing                                               | [See Notes](#_RXE-1_Quantity/Timing)                 |
| 2   | 250 | CE  | R   |      | 0292           | Give Code                                                     | [See Notes](#_RXE-2_Give_Code)                       |
| 3   | 20  | NM  | R   |      |                | Give Amount - Minimum                                         | [See Notes](#_RXE-3_Give_Amount_- Minimum)           |
| 4   | 20  | NM  | O   |      |                | Give Amount - Maximum                                         | [See Notes](#_RXE-4_Give_Amount_- Maximum)           |
| 5   | 250 | CE  | R   |      |                | Give Units                                                    | [See Notes](#_RXE-5_Give_Units)                      |
| 6   | 250 | CE  | O   |      |                | Give Dosage Form                                              | [See Notes](#_RXE-6_Give_Dosage_Form)                |
| 7   | 250 | CE  | O   | Y    |                | Provider's Administration Instructions                        | [See Notes](#_RXE-7_Provider's_Administration_Ins)   |
| 8   | 200 | CM  | C   |      |                | Deliver-to Location                                           | N/A                                                  |
| 9   | 1   | ID  | O   |      | 0167           | Substitution Status                                           | N/A                                                  |
| 10  | 20  | NM  | C   |      |                | Dispense Amount                                               | [See Notes](#_RXE-10_Dispense_Amount)                |
| 11  | 250 | CE  | C   |      |                | Dispense Units                                                | N/A                                                  |
| 12  | 3   | NM  | O   |      |                | Number of Refills                                             | N/A                                                  |
| 13  | 250 | XCN | C   | Y    |                | Ordering Provider's DEA Number                                | N/A                                                  |
| 14  | 250 | XCN | O   | Y    |                | Pharmacist/Treatment Supplier's Verifier ID                   | N/A                                                  |
| 15  | 20  | ST  | C   |      |                | Prescription Number                                           | [See Notes](#_RXE-17_Number_of_Refills/Doses_Disp)   |
| 16  | 20  | NM  | C   |      |                | Number of Refills Remaining                                   | N/A                                                  |
| 17  | 20  | NM  | C   |      |                | Number of Refills/Doses Dispensed                             | [See Notes](#_RXE-17_Number_of_Refills/Doses Disp_1) |
| 18  | 26  | TS  | C   |      |                | D/T of Most Recent Refill or Dose Dispensed                   | [See Notes](#_RXE-18_D/T_of_Most Recent Refill or)   |
| 19  | 10  | CQ  | C   |      |                | Total Daily Dose                                              | [See Notes](#_RXE-19_Total_Daily_Dose)               |
| 20  | 1   | ID  | O   |      | [0136](#T0136) | Needs Human Review                                            | [See Notes](#_RXE-20_Needs_Human_Review)             |
| 21  | 250 | CE  | O   | Y    |                | Pharmacy/Treatment Supplier's Special Dispensing Instructions | [See Notes](#_RXE-21_Pharmacy/Treatment_Supplier')   |
| 22  | 20  | ST  | C   |      |                | Give Per (Time Unit)                                          | [See Notes](#_RXE-22_Give_Per_(Time Unit))           |
| 23  | 6   | ST  | O   |      |                | Give Rate Amount                                              | [See Notes](#_RXE-23_Give_Rate_Amount)               |
| 24  | 250 | CE  | O   |      |                | Give Rate Units                                               | [See Notes](#_RXE-24_Give_Rate_Units)                |
| 25  | 20  | NM  | O   |      |                | Give Strength                                                 | N/A                                                  |
| 26  | 250 | CE  | O   |      |                | Give Strength Units                                           | N/A                                                  |
| 27  | 250 | CE  | O   | Y    |                | Give Indication                                               | [See Notes](#_RXE-27_Give_Indication)                |
| 28  | 20  | NM  | O   |      |                | Dispense Package Size                                         | N/A                                                  |
| 29  | 250 | CE  | O   |      |                | Dispense Package Size Unit                                    | N/A                                                  |
| 30  | 2   | ID  | O   |      | 0321           | Dispense Package Method                                       | [See Notes](#_RXE-30_Dispense_Package_Method)        |
| 31  | 250 | CE  | O   | Y    |                | Supplementary Code                                            | N/A                                                  |

1.  Field Definitions
    1.  <span id="_RXE-1_Quantity/Timing" class="anchor"></span>RXE-1 Quantity/Timing

| SEQ | DT  | TBL# | Component Name      | CCR |
|-----|-----|------|---------------------|-----|
| 1   | CQ  |      | Quantity            | N/A |
| 2   | CM  |      | Interval            | N/A |
| 3   | ST  |      | Duration            | N/A |
| 4   | TS  |      | Start Date/Time     | N/A |
| 5   | TS  |      | End Date/Time       | N/A |
| 6   | ST  |      | Priority            | N/A |
| 7   | ST  |      | Condition           | N/A |
| 8   | TX  |      | Text                |     |
| 9   | ID  | 0472 | Conjunction         | N/A |
| 10  | CM  |      | Order Sequencing    | N/A |
| 11  | CE  |      | Occurrence Duration | N/A |
| 12  | NM  |      | Total Occurrences   | N/A |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="4">Definition:</td>
<td colspan="2">This field is used by the pharmacy supplier to express the fully coded version of the drug or treatment timing.</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td><em>Text</em> element of this field contains the Schedule</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>""</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Non-VA Meds:</p></li>
</ul></td>
<td>dosage^schedule^^start date^discontinued date^^^medication route</td>
</tr>
<tr class="odd">
<td rowspan="3">Example:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>^^^^^^^Comprehensive Met Panel results from HINES DEVELOPMENT</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>""</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Non-VA Meds:</p></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-2_Give_Code" class="anchor"></span>RXE-2 Give Code

|     |     |      |                                 |                                                  |
|-----|-----|------|---------------------------------|--------------------------------------------------|
| SEQ | DT  | TBL# | Component Name                  | CCR                                              |
| 1   | ST  |      | Identifier                      | NDC                                              |
| 2   | ST  |      | Text                            | VA Product name                                  |
| 3   | ST  |      | Name of Coding System           | PSNDF                                        |
| 4   | ST  |      | Alternate Identifier            | NDF IEN concatenated with the VA drug class code |
| 5   | ST  |      | Alternate Text                  | Generic Name                                     |
| 6   | ST  |      | Name of Alternate Coding System | 99PSD                                        |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Definition:</td>
<td colspan="2">This field identifies the medical substance provided to the patient.</td>
</tr>
<tr class="even">
<td>Format:</td>
<td><ul>
<li><p>Non-VA Meds</p></li>
</ul></td>
<td>NDC code^VA Product Name^PSNDF^NDF IEN concatenated with the VA drug class code^Generic name^99PSD</td>
</tr>
<tr class="odd">
<td rowspan="2">Example:</td>
<td><ul>
<li><p>Non-VA Meds:</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Other</p></li>
</ul></td>
<td><strong>0002-1615-02^MAGNESIUM SULFATE 50% 1GM/2ML AMP^PSNDF^31-TN406^MAGNESIUM SO4 4MEQ/ML INJ^99PSD</strong></td>
</tr>
<tr class="odd">
<td>Note:</td>
<td><ul>
<li><p>Non-VA Meds</p></li>
</ul></td>
<td>If no IEN for the DRUG file (#50) exists for the Non-VA med drug, RXE-2 will contain data in RXE-2-5 only: the Orderable Item and Dose Form</td>
</tr>
</tbody>
</table>

1.  RXE-3 Give Amount - Minimum

|             |                                                                                                                    |
|-------------|--------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the ordered amount. This field is required but it is not used by the Clinical Case Registries. |
| Example:    | ""                                                                                                                 |

2.  RXE-4 Give Amount - Maximum

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Maximum Number of Refills</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>5</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-5_Give_Units" class="anchor"></span>RXE-5 Give Units

|     |     |      |                                 |                                                                           |
|-----|-----|------|---------------------------------|---------------------------------------------------------------------------|
| SEQ | DT  | TBL# | Component Name                  | CCR                                                                       |
| 1   | ST  |      | Identifier                      | N/A                                                                       |
| 2   | ST  |      | Text                            | N/A                                                                       |
| 3   | ST  |      | Name of Coding System           | N/A                                                                       |
| 4   | ST  |      | Alternate Identifier            | Drug Unit IEN (IEN of the record of the DRUG UNITS file (#50.607)).       |
| 5   | ST  |      | Alternate Text                  | Drug Unit Name (value of the .01 field of the DRUG UNITS file (#50.607)). |
| 6   | ST  |      | Name of Alternate Coding System | 99PSU                                                                 |

|             |                                                          |
|-------------|----------------------------------------------------------|
| Definition: | This field contains the units for the Give Amount field. |
| Example:    | ^^^130^MIC/1.5ML^99PSU                               |

2.  <span id="_RXE-6_Give_Dosage_Form" class="anchor"></span>RXE-6 Give Dosage Form

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Release Date/Time</td>
</tr>
<tr class="odd">
<td>Format:</td>
<td colspan="2">YYYYMMDD[hhmm[ss]] [<strong>+</strong>|<strong>-</strong>zzzz]</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>200403020815-0800</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-7_Provider's_Administration_Ins" class="anchor"></span>RXE-7 Provider's Administration Instructions

| SEQ | DT  | TBL# | Component Name                  | CCR |
|-----|-----|------|---------------------------------|-----|
| 1   | ST  |      | Identifier                      | N/A |
| 2   | ST  |      | Text                            | SIG |
| 3   | ST  |      | Name of Coding System           | N/A |
| 4   | ST  |      | Alternate Identifier            | N/A |
| 5   | ST  |      | Alternate Text                  | N/A |
| 6   | ST  |      | Name of Alternate Coding System | N/A |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="3">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td rowspan="2">Ordering provider's instructions to the person administering the drug. This field corresponds to the SIG, and it is free text.</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Non-VA Meds:</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Format:</td>
<td colspan="2">^Disclaimer text (Limited to 4000 characters)</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>^APP 1 PATCH TO SKIN QAM AND REMOVE HS (TO REPLACE NITROGLYCERIN 6.5MG SA CAP)</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-10_Dispense_Amount" class="anchor"></span>RXE-10 Dispense Amount

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>This field contains the amount dispensed. Valid entries are between 1 and 99999999 with up to 2 decimal places allowed.</td>
</tr>
<tr class="odd">
<td>Format:</td>
<td colspan="2">NNNNNNNN[.N[N]]</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>900.75</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-17_Number_of_Refills/Doses_Disp" class="anchor"></span>RXE-15 Prescription Number

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="3">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Refill Indicator</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Non-VA Meds:</p></li>
</ul></td>
<td>CPRS order number</td>
</tr>
<tr class="even">
<td rowspan="3">Tables:</td>
<td>Value</td>
<td>Description</td>
</tr>
<tr class="odd">
<td>1</td>
<td>Refill</td>
</tr>
<tr class="even">
<td>2</td>
<td>Partial</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>1</strong></td>
</tr>
</tbody>
</table>

1.  RXE-17 Number of Refills/Doses Dispensed

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Refill Number</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>3</strong></td>
</tr>
</tbody>
</table>

1.  RXE-18 D/T of Most Recent Refill or Dose Dispensed

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>Last date/time when the dose should be given (stop date/time)</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Date/time when the most recent fill/refill was dispensed (fill date/time)</td>
</tr>
<tr class="odd">
<td>Format:</td>
<td colspan="2">YYYYMMDD[hhmm[ss]] [<strong>+</strong>|<strong>-</strong>zzzz]</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>200403020815-0800</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-19_Total_Daily_Dose" class="anchor"></span>RXE-19 Total Daily Dose

|     |     |      |                |     |
|-----|-----|------|----------------|-----|
| SEQ | DT  | TBL# | Component Name | CCR |
| 1   | NM  |      | Quantity       |     |
| 2   | CE  |      | Units          | N/A |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Total Daily Dose. Valid entries range from 1 to 90.</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>15</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-20_Needs_Human_Review" class="anchor"></span>RXE-20 Needs Human Review

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Indicator of whether the drug has been transmitted to CMOP</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>Y</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-21_Pharmacy/Treatment_Supplier'" class="anchor"></span>RXE-21 Pharmacy/Treatment Supplier's Special Dispensing Instructions

| SEQ | DT  | TBL# | Component Name                  | CCR |
|-----|-----|------|---------------------------------|-----|
| 1   | ST  |      | Identifier                      |     |
| 2   | ST  |      | Text                            | N/A |
| 3   | ST  |      | Name of Coding System           | N/A |
| 4   | ST  |      | Alternate Identifier            | N/A |
| 5   | ST  |      | Alternate Text                  | N/A |
| 6   | ST  |      | Name of Alternate Coding System | N/A |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="3">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>Medication Route</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Clinic Stop Code</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Non-VA Meds:</p></li>
</ul></td>
<td>Pharmacy/Treatment Supplier's Special Dispensing Instructions</td>
</tr>
<tr class="even">
<td>Format:</td>
<td><ul>
<li><p>Non-VA Meds:</p></li>
</ul></td>
<td>Clinic Stop Code^^^Clinic IEN &amp; Clinic Name</td>
</tr>
<tr class="odd">
<td rowspan="3">Example:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td><strong>Oral</strong></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td><strong>208</strong></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Non-VA Meds:</p></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

1.  RXE-22 Give Per (Time Unit)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Last Dispensed Date/Time</td>
</tr>
<tr class="odd">
<td>Format:</td>
<td colspan="2">YYYYMMDD[hhmm[ss]] [<strong>+</strong>|<strong>-</strong>zzzz]</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>200403020815-0800</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-23_Give_Rate_Amount" class="anchor"></span>RXE-23 Give Rate Amount

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Unit Cost</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>30.45</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-24_Give_Rate_Units" class="anchor"></span>RXE-24 Give Rate Units

| SEQ | DT  | TBL# | Component Name                  | CCR |
|-----|-----|------|---------------------------------|-----|
| 1   | ST  |      | Identifier                      |     |
| 2   | ST  |      | Text                            | N/A |
| 3   | ST  |      | Name of Coding System           | N/A |
| 4   | ST  |      | Alternate Identifier            | N/A |
| 5   | ST  |      | Alternate Text                  | N/A |
| 6   | ST  |      | Name of Alternate Coding System | N/A |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>Units per Dose. Valid entries range from 0 to 30, with up to 2 decimal places.</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Format:</td>
<td colspan="2">NN[.N[N]]</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>12.25</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-27_Give_Indication" class="anchor"></span>RXE-27 Give Indication

| SEQ | DT  | TBL# | Component Name                  | CCR |
|-----|-----|------|---------------------------------|-----|
| 1   | ST  |      | Identifier                      |     |
| 2   | ST  |      | Text                            |     |
| 3   | ST  |      | Name of Coding System           | N/A |
| 4   | ST  |      | Alternate Identifier            | N/A |
| 5   | ST  |      | Alternate Text                  | N/A |
| 6   | ST  |      | Name of Alternate Coding System | N/A |

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Patient Status</td>
</tr>
<tr class="odd">
<td>Example:</td>
<td colspan="2"><strong>6^OTHER FEDERAL</strong></td>
</tr>
</tbody>
</table>

1.  <span id="_RXE-30_Dispense_Package_Method" class="anchor"></span>RXE-30 Dispense Package Method

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2">Definition:</td>
<td><ul>
<li><p>Inpatient:</p></li>
</ul></td>
<td>N/A</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Outpatient:</p></li>
</ul></td>
<td>Mail/Window</td>
</tr>
<tr class="odd">
<td rowspan="3">Tables:</td>
<td>Value</td>
<td>Description</td>
</tr>
<tr class="even">
<td>AD</td>
<td>Automatic Dispensing – Mail</td>
</tr>
<tr class="odd">
<td>TR</td>
<td>Traditional – Window</td>
</tr>
<tr class="even">
<td>Example:</td>
<td colspan="2"><strong>TR</strong></td>
</tr>
</tbody>
</table>

1.  Sample RXE Segments
    1.  Inpatient

RXE\|[^^^^^^^QID PRN](#_RXE-1_Quantity/Timing)\|[17478-0216-12^NAPHAZOLINE HCL 0.1% SOLN,OPH^PSNDF^900-OP800^NAPHAZOLINE HCL 0.1% OPH SOLN^99PSD](#_RXE-2_Give_Code)\|[""](#_RXE-3_Give_Amount_- Minimum)\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|[200505301100-0800](#_RXE-18_D/T_of_Most Recent Refill or)\|\|\|[BOTH EYE](#_RXE-21_Pharmacy/Treatment_Supplier')\|\|\|[1](#_RXE-24_Give_Rate_Units)

2.  Outpatient

RXE\|[""](#_RXE-1_Quantity/Timing)\|[00056-0510-30^EFAVIRENZ 600MG TAB^PSNDF^3528-AM800](\l)

[^EFAVIRENZ 600MG TAB^99PSD](\l)\|[""](#_RXE-3_Give_Amount_- Minimum)\|[6](#_RXE-4_Give_Amount_- Maximum)\|[^^^20^MG^99PSU](#_RXE-5_Give_Units)\|[20050302](#_RXE-6_Give_Dosage_Form)\|[^TAKE ONE TABLET BY MOUTH EVERY DAY](#_RXE-7_Provider's_Administration_Ins)\|\|\|[30](#_RXE-10_Dispense_Amount)\|\|\|\|\|1\|\|[4](#_RXE-17_Number_of_Refills/Doses Disp)\|[20050228](#_RXE-18_D/T_of_Most Recent Refill or)\|[30](#_RXE-19_Total_Daily_Dose)\|[Y](#_RXE-20_Needs_Human_Review)\|[324](#_RXE-21_Pharmacy/Treatment_Supplier')

\|[200503021422-0800](#_RXE-22_Give_Per_(Time Unit))\|[8.0047](#_RXE-23_Give_Rate_Amount)\|\|\|\|[3^SC LESS THAN 50%](#_RXE-27_Give_Indication)\|\|\|[AD](#_RXE-30_Dispense_Package_Method)

3.  Non-VA Meds

RXE\|30 MILLILITERS^EVERY DAY AS NEEDED^^20070101^20070610083028-0500^^^MOUTH\|00395-1670-16^MILK OF MAGNESIA^PSNDF^2206-GA108^MILK OF MAGNESIA^99PSD\|\|\|\|\|\*\*IF NO IMPROVEMENT IN 12 HOURS CALL MD\*\*\|\|\|\|\|\|\|\|3359826\|\|\|\|\|\|323^^^1175&HBPC–PHARMACY

1.  <span id="_ZRD_–_Rated_Disabilities_Segment" class="anchor"></span>ZRD – Rated Disabilities Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL#             | Field Name                   | CCR                                     |
|-----|-----|-----|-----|------|------------------|------------------------------|-----------------------------------------|
| 1   | 4   | SI  | R   |      |                  | Set ID – ZRD                 | [See Notes](#_ZRD-1_Set_ID_1)           |
| 2   | 4   | CE  | R   |      |                  | Disability Condition         | [See Notes](#_ZRD-2_Rated_Disabilities) |
| 3   | 3   | NM  | R   |      |                  | Disability %                 | [See Notes](#_ZRD-3_Disability_%)       |
| 4   | 1   | IS  | O   |      | [VA001](#TVA001) | Service Connected            | [See Notes](#_ZRD-4_Service_Connected)  |
| 5   | 30  | ST  | O   |      |                  | Service Connected Conditions | N/A                                     |
| 6   | 3   | NM  | O   |      |                  | Percentage                   | N/A                                     |
| 7   | 1   | IS  | O   |      | 0136             | Service Dental Injury        | N/A                                     |
| 8   | 1   | IS  | O   |      | 0136             | Service Teeth Extracted      | N/A                                     |
| 9   | 8   | DT  | O   |      |                  | Date of Dental Treatment     | N/A                                     |
| 10  | 100 | ST  | O   |      |                  | Condition                    | N/A                                     |
| 11  | 8   | DT  | O   |      |                  | Date Condition First Noted   | N/A                                     |

1.  <span id="_ZRD-1_Set_ID_1" class="anchor"></span>ZRD-1 Set ID – ZRD

|             |                                                                                                                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the number that identifies this transaction. For the first occurrence of the segment, the sequence number shall be one, for the second occurrence, the sequence number shall be two, etc. |
| Example:    | 2                                                                                                                                                                                                         |

2.  <span id="_ZRD-2_Rated_Disabilities" class="anchor"></span>ZRD-2 Disability Condition

|     |     |      |                                 |                |
|-----|-----|------|---------------------------------|----------------|
| SEQ | DT  | TBL# | Component Name                  | CCR            |
| 1   | ST  |      | Identifier                      | DX Code        |
| 2   | ST  |      | Text                            | Condition Name |
| 3   | ST  |      | Name of Coding System           | N/A            |
| 4   | ST  |      | Alternate Identifier            | N/A            |
| 5   | ST  |      | Alternate Text                  | N/A            |
| 6   | ST  |      | Name of Alternate Coding System | N/A            |

|             |                                                                                                                                      |                        |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| Definition: | This field holds the disability condition for this patient.                                                                          |                        |
| Code        | See the DISABILITY CONDITION file (#31) for possible values of the *DX Code* and *Condition Name*. Some examples are provided below: |                        |
|             | Code                                                                                                                                 | Condition Name         |
|             | 5000                                                                                                                                 | OSTEOMYELITIS          |
|             | 5001                                                                                                                                 | BONE DISEASE           |
|             | 5002                                                                                                                                 | RHEUMATOID ARTHRITIS   |
|             | 5003                                                                                                                                 | DEGENERATIVE ARTHRITIS |
|             | 5004                                                                                                                                 | ARTHRITIS              |
| Example:    | 5002^RHEUMATOID ARTHRITIS                                                                                                        |                        |

3.  <span id="_ZRD-3_Disability_%" class="anchor"></span>ZRD-3 Disability %

|             |                                                                                         |
|-------------|-----------------------------------------------------------------------------------------|
| Definition: | This field holds the percentage at which the VA rated this disability for this patient. |
| Format:     | Values range from 0 to 100.                                                             |
| Example:    | 45                                                                                  |

4.  <span id="_ZRD-4_Service_Connected" class="anchor"></span>ZRD-4 Service Connected

|             |                                                              |                       |
|-------------|--------------------------------------------------------------|-----------------------|
| Definition: | This field indicates if the disability is service connected. |                       |
| Code        | Value                                                        | Description           |
|             | 0                                                            | Not Service Connected |
|             | 1                                                            | Service Connected     |
| Example:    | 1                                                        |                       |

5.  Sample ZRD Segment

ZRD\|[1](#_ZRD-1_Set_ID_1)\|[7709^HODGKINS DISEASE](#_ZRD-2_Rated_Disabilities)\|[100](#_ZRD-3_Disability_%)\|[1](#_ZRD-4_Service_Connected)

2.  <span id="_ZSP_–_Service_1" class="anchor"></span>ZSP – Service Period Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL#             | Field Name                   | CCR                                     |
|-----|-----|-----|-----|------|------------------|------------------------------|-----------------------------------------|
| 1   | 4   | SI  | R   |      |                  | Set ID – ZSP                 | [See Notes](#_ZSP-1_Set_ID)             |
| 2   | 1   | ID  | R   |      | [VA001](#TVA001) | Service Connected?           | [See Notes](#_ZSP-2_Service_Connected?) |
| 3   | 3   | NM  | O   |      |                  | Service Connected Percentage | [See Notes](#_ZSP-3_Service_Connected)  |
| 4   | 2   | IS  | O   |      | VA011            | Period of Service            | [See Notes](#_ZSP-4_Period_of)          |
| 5   | 1   | ST  | O   |      |                  | Vietnam Service Indicated    | [See Notes](#_ZSP-5_Vietnam_Service)    |
| 6   | 1   | ID  | O   |      | [VA001](#TVA001) | Permanent & Total Disability | [See Notes](#_ZSP-6_Permanent_&)        |
| 7   | 1   | ID  | O   |      | [VA001](#TVA001) | Unemployable                 | [See Notes](#_ZSP-7_Unemployable)       |
| 8   | 26  | TS  | O   |      |                  | SC Award Date                | [See Notes](#_ZSP-8_SC_Award)           |

1.  Field Definitions
    1.  <span id="_ZSP-1_Set_ID" class="anchor"></span>ZSP-1 Set ID – ZSP

|             |                                                          |
|-------------|----------------------------------------------------------|
| Definition: | This field holds the Set ID. The set ID is 1 by default. |
| Example:    | 1                                                    |

2.  <span id="_ZSP-2_Service_Connected?" class="anchor"></span>ZSP-2 Service Connected?

|             |                                                                     |                       |
|-------------|---------------------------------------------------------------------|-----------------------|
| Definition: | This field indicates if the patient condition is service connected. |                       |
| Code        | Value                                                               | Description           |
|             | 0                                                                   | Not Service Connected |
|             | 1                                                                   | Service Connected     |
| Example:    | 0                                                               |                       |

3.  <span id="_ZSP-3_Service_Connected" class="anchor"></span>ZSP-3 Service Connected Percentage

|             |                                                        |
|-------------|--------------------------------------------------------|
| Definition: | This field holds the percentage of service connection. |
| Format:     | Values range from 0 to 100.                            |
| Example:    | 60                                                 |

4.  <span id="_ZSP-4_Period_of" class="anchor"></span>ZSP-4 Period of Service

|             |                                                                         |                         |
|-------------|-------------------------------------------------------------------------|-------------------------|
| Definition: | This field holds the period of service that best describes the patient. |                         |
| Tables:     | Value                                                                   | Description             |
|             | 0                                                                       | KOREAN                  |
|             | 1                                                                       | WORLD WAR I             |
|             | 2                                                                       | WORLD WAR II            |
|             | 3                                                                       | SPANISH AMERICAN        |
|             | 4                                                                       | PRE-KOREAN              |
|             | 5                                                                       | POST-KOREAN             |
|             | 6                                                                       | OPERATION DESERT SHIELD |
|             | 7                                                                       | VIETNAM ERA             |
|             | 8                                                                       | POST-VIETNAM            |
|             | 9                                                                       | OTHER OR NONE           |
|             |                                                                         | ...                     |
|             | Y                                                                       | CAV/NPS                 |
|             | N                                                                       | MERCHANT MARINE         |

|          |       |
|----------|-------|
| Example: | 9 |

5.  <span id="_ZSP-5_Vietnam_Service" class="anchor"></span>ZSP-5 Vietnam Service Indicated

|             |                                                        |             |
|-------------|--------------------------------------------------------|-------------|
| Definition: | This field indicates if the patient served in Vietnam. |             |
| Tables:     | Value                                                  | Description |
|             | ""                                                     |             |
|             | N                                                      | No          |
|             | U                                                      | Unknown     |
|             | Y                                                      | Yes         |
| Example:    | N                                                  |             |

6.  <span id="_ZSP-6_Permanent_&" class="anchor"></span>ZSP-6 Permanent & Total Disability

|             |                                                                                                               |                  |
|-------------|---------------------------------------------------------------------------------------------------------------|------------------|
| Definition: | This field indicates if the patient is permanently and totally disabled due to a service-connected condition. |                  |
| Tables:     | Value                                                                                                         | Description      |
|             | 0                                                                                                             | Not P&T Disabled |
|             | 1                                                                                                             | P&T Disabled     |
| Example:    | 0                                                                                                         |                  |

7.  <span id="_ZSP-7_Unemployable" class="anchor"></span>ZSP-7 Unemployable

|             |                                                                                           |              |
|-------------|-------------------------------------------------------------------------------------------|--------------|
| Definition: | This field indicates if the patient is unemployable due to a service connected condition. |              |
| Tables:     | Value                                                                                     | Description  |
|             | 0                                                                                         | Employable   |
|             | 1                                                                                         | Unemployable |
| Example:    | 1                                                                                     |              |

8.  <span id="_ZSP-8_SC_Award" class="anchor"></span>ZSP-8 SC Award Date

|             |                                                                                                                                       |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This field contains the date on which the service connection is effective. If no date has been entered, the null string will be sent. |
| Format:     | YYYYMMDD                                                                                                                              |
| Example:    | 19761205                                                                                                                          |

2.  Sample ZSP Segment

ZSP\|[1](#_ZSP-1_Set_ID)\|[1](#_ZSP-2_Service_Connected?)\|[30](#_ZSP-3_Service_Connected)\|[8](#_ZSP-4_Period_of)\|[""](#_ZSP-5_Vietnam_Service)\|[0](#_ZSP-6_Permanent_&)\|[0](#_ZSP-7_Unemployable)\|[19700325](#_ZSP-8_SC_Award)

3.  ZIN – Purchased Care Inpatient Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL# | Field Name            | CCR                 |
|-----|-----|-----|-----|------|------|-----------------------|---------------------|
| 1   | 10  | NM  | R   |      |      | Key                   | [See Notes](#ZIN01) |
| 2   | 8   | DT  | O   |      |      | Treatment "From" Date | [See Notes](#ZIN02) |
| 3   | 8   | DT  | O   |      |      | Treatment "To" Date   | [See Notes](#ZIN03) |
| 4   | 2   | NM  | O   |      |      | Discharge Type Code   | [See Notes](#ZIN04) |
| 5   | 9   | ST  | O   |      |      | Billed Charges        | [See Notes](#ZIN05) |
| 6   | 8   | ST  | O   |      |      | Amount Paid           | [See Notes](#ZIN06) |
| 7   | 8   | DT  | R   |      |      | Date Finalized        | [See Notes](#ZIN07) |
| 8   | 30  | ST  | O   |      |      | Discharge DRG         | [See Notes](#ZIN08) |
| 9   | 8   | DT  | O   |      |      | Date of Admission     | [See Notes](#ZIN09) |
| 10  | 8   | DT  | O   |      |      | Date of Discharge     | [See Notes](#ZIN10) |
| 11  | 5   | NM  | O   |      |      | Covered Days          | [See Notes](#ZIN11) |
| 12  | 7   | ST  | O   |      |      | ICD 1                 | [See Notes](#ZIN12) |
| 13  | 7   | ST  | O   |      |      | ICD 2                 | [See Notes](#ZIN13) |
| 14  | 7   | ST  | O   |      |      | ICD 3                 | [See Notes](#ZIN14) |
| 15  | 7   | ST  | O   |      |      | ICD 4                 | [See Notes](#ZIN15) |
| 16  | 7   | ST  | O   |      |      | ICD 5                 | [See Notes](#ZIN16) |
| 17  | 6   | ST  | O   |      |      | Procedure 1           | [See Notes](#ZIN17) |
| 18  | 6   | ST  | O   |      |      | Procedure 2           | [See Notes](#ZIN18) |
| 19  | 6   | ST  | O   |      |      | Procedure 3           | [See Notes](#ZIN19) |
| 20  | 6   | ST  | O   |      |      | Procedure 4           | [See Notes](#ZIN20) |
| 21  | 6   | ST  |     |      |      | Procedure 5           | [See Notes](#ZIN21) |

1.  <span id="TOC" class="anchor"></span>Field Definitions
    1.  <span id="ZIN01" class="anchor"></span>ZIN-1 Key

|             |                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the IEN in the FEE BASIS INVOICE file (#162.5). This is a unique key representing the inpatient record for the patient. |
| Example:    | 1567                                                                                                                        |

2.  <span id="ZIN02" class="anchor"></span>ZIN-2 Treatment "From" Date

|             |                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the TREATMENT FROM DATE (#5) in the FEE BASIS INVOICE file (#162.5). This is the starting date for the invoice. |
| Example:    | 20110228                                                                                                            |

3.  ZIN-3 Treatment "To" Date

|             |                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the TREATMENT TO DATE (#6) in the FEE BASIS INVOICE file (#162.5). This is the ending date for the invoice. |
| Example:    | 20110228                                                                                                        |

4.  <span id="ZIN04" class="anchor"></span>ZIN-4 Discharge Type Code

|             |                                                                                                                                                                                                            |                                  |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Definition: | This is the DISCHARGE TYPE CODE (#6.5) in the FEE BASIS INVOICE file (#162.5). It is a pointer to the FEE BASIS DISPOSITION CODE file (#162.6). This is the type of discharge associated with the invoice. |                                  |
| Code:       | Value                                                                                                                                                                                                      | Description                      |
|             | 1                                                                                                                                                                                                          | TO HOME OR SELF CARE             |
|             | 2                                                                                                                                                                                                          | TO ANOTHER SHORT-TERM FACILITY   |
|             | 3                                                                                                                                                                                                          | TO SKILLED NURSING FACILITY      |
|             | 4                                                                                                                                                                                                          | TO INTERMEDIATE NURSING FACILITY |
|             | 5                                                                                                                                                                                                          | TO ANOTHER TYPE OF FACILITY      |
|             | 6                                                                                                                                                                                                          | TO HOME FOR HOME HEALTH SERVICES |
|             | 7                                                                                                                                                                                                          | LEFT AGAINST MEDICAL ADVICE      |
|             | 8                                                                                                                                                                                                          | DIED                             |
|             | 9                                                                                                                                                                                                          | STILL A PATIENT                  |
| Example:    | 4                                                                                                                                                                                                      |                                  |

5.  <span id="ZIN05" class="anchor"></span>ZIN-5 Billed Charges

|             |                                                                                                                                                                        |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the BILLED CHARGES field (#6.6) in the FEE BASIS INVOICE file (#162.5). It is the amount that the VA was initially billed by the vendor for an inpatient stay. |
| Example:    | 1284.91                                                                                                                                                            |

6.  <span id="ZIN06" class="anchor"></span>ZIN-6 Amount Paid

|             |                                                                                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the AMOUNT PAID field (#8) in the FEE BASIS INVOICE file (#162.5). It is the amount actually paid to the vendor for the service provided. |
| Example:    | 1284.91                                                                                                                                       |

7.  <span id="ZIN07" class="anchor"></span>ZIN-7 Date Finalized

|             |                                                                                                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the DATE FINALIZED field (#19) in the FEE BASIS INVOICE file (#162.5). It is the date the invoice was vouchered by Fiscal. |
| Example:    | 20110228                                                                                                                       |

8.  <span id="ZIN08" class="anchor"></span>ZIN-8 Discharge DRG

|             |                                                                                                                            |
|-------------|----------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the external value of the DISCHARGE DRG field (#24) in the FEE BASIS INVOICE file (#162.5). It is the grouped DRG. |
| Example:    | DRG202                                                                                                                 |

9.  <span id="ZIN09" class="anchor"></span>ZIN-9 Date of Admission

|             |                                                                                  |
|-------------|----------------------------------------------------------------------------------|
| Definition: | This is the DATE OF ADMISSION field (#3.5) in the VA FORM 10-7078 file (#162.4). |
| Example:    | 20110228                                                                     |

10. <span id="ZIN10" class="anchor"></span>ZIN-10 Date of Discharge

|             |                                                                                  |
|-------------|----------------------------------------------------------------------------------|
| Definition: | This is the DATE OF DISCHARGE field (#4.5) in the VA FORM 10-7078 file (#162.4). |
| Example:    | 20110228                                                                     |

11. <span id="ZIN11" class="anchor"></span>ZIN-11 Covered Days

|             |                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the COVERED DAYS field (#54) in the FEE BASIS INVOICE file (#162.5). The number of inpatient days that will be paid. |
| Example:    | 1                                                                                                                        |

12. <span id="ZIN12" class="anchor"></span>ZIN-12 ICD 1

|             |                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the ICD1 field (#30) in the FEE BASIS INVOICE file (#162.5). The first valid ICD code associated with this payment. |
| Example:    | 303.00                                                                                                                      |

13. <span id="ZIN13" class="anchor"></span>ZIN-13 ICD 2

|             |                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the ICD2 field (#31) in the FEE BASIS INVOICE file (#162.5). The second valid ICD code associated with this payment. |
| Example:    | 303.00                                                                                                                       |

14. <span id="ZIN14" class="anchor"></span>ZIN-14 ICD 3

|             |                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the ICD3 field (#32) in the FEE BASIS INVOICE file (#162.5). The third valid ICD code associated with this payment. |
| Example:    | 303.00                                                                                                                      |

15. <span id="ZIN15" class="anchor"></span>ZIN-15 ICD 4

|             |                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the ICD4 field (#33) in the FEE BASIS INVOICE file (#162.5). The fourth valid ICD code associated with this payment. |
| Example:    | 303.00                                                                                                                       |

16. <span id="ZIN16" class="anchor"></span>ZIN-16 ICD 5

|             |                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the ICD5 field (#34) in the FEE BASIS INVOICE file (#162.5). The fifth valid ICD code associated with this payment. |
| Example:    | 303.00                                                                                                                      |

17. <span id="ZIN17" class="anchor"></span>ZIN-17 Procedure 1

|             |                                                                                                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the PROC1 field (#40) in the FEE BASIS INVOICE file (#162.5). The first valid procedure code associated with this payment. |
| Example:    | 94.68                                                                                                                              |

18. <span id="ZIN18" class="anchor"></span>ZIN-18 Procedure 2

|             |                                                                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the PROC2 field (#41) in the FEE BASIS INVOICE file (#162.5). The second valid procedure code associated with this payment. |
| Example:    | 94.68                                                                                                                               |

19. <span id="ZIN19" class="anchor"></span>ZIN-19 Procedure 3

|             |                                                                                                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the PROC3 field (#42) in the FEE BASIS INVOICE file (#162.5). The third valid procedure code associated with this payment. |
| Example:    | 94.68                                                                                                                              |

20. <span id="ZIN20" class="anchor"></span>ZIN-20 Procedure 4

|             |                                                                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the PROC4 field (#43) in the FEE BASIS INVOICE file (#162.5). The fourth valid procedure code associated with this payment. |
| Example:    | 94.68                                                                                                                               |

21. <span id="ZIN21" class="anchor"></span>ZIN-21 Procedure 5

|             |                                                                                                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the PROC5 field (#44) in the FEE BASIS INVOICE file (#162.5). The fifth valid procedure code associated with this payment. |
| Example:    | 94.68                                                                                                                              |

2.  Sample ZIN Segment

ZIN\|36520\|20040408\|20040409\|1\|9153.70\|6445.16\|20040817\|DRG202\|20040408\|20040409\|1\|571.2\|456.20\|456.8\|305.1\|303.90\|42.33\|44.43

4.  ZSV – Purchased Care Outpatient Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL# | Field Name                  | CCR                 |
|-----|-----|-----|-----|------|------|-----------------------------|---------------------|
| 1   | 28  | ST  | R   |      |      | Key                         | [See Notes](#ZSV01) |
| 2   | 8   | DT  | O   |      |      | Date of Treatment           | [See Notes](#ZSV02) |
| 3   | 2   | NM  | O   |      |      | Fee Program Code            | [See Notes](#ZSV03) |
| 4   | 5   | ST  | R   |      |      | Service Provided (CPT code) | [See Notes](#ZSV04) |
| 5   | 200 | ST  | O   |      |      | Purpose of Visit            | [See Notes](#ZSV05) |
| 6   | 7   | ST  | O   |      |      | Primary Diagnosis           | [See Notes](#ZSV06) |
| 7   | 60  | ST  | O   |      |      | Place of Service            | [See Notes](#ZSV07) |

1.  Field Definitions
    1.  <span id="ZSV01" class="anchor"></span>ZSV-1 Key

|             |                                                                                                                                                                                              |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is a combination of 4 IENs: FEE BASIS PAYMENT file (#162), sub-file \#162.01, sub-file \#162.02, and \#162.03. This is a unique key representing the outpatient record for the patient. |
| Example:    | 4561-1-2-1                                                                                                                                                                               |

2.  <span id="ZSV02" class="anchor"></span>ZSV-2 Date of Treatment

|             |                                                                                                                                                    |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the INITIAL TREATMENT DATE (#.01) in the FEE BASIS PAYMENT file (#162), sub-file \#162.02. The date that the treatment/service took place. |
| Example:    | 20110228                                                                                                                                       |

3.  <span id="ZSV03" class="anchor"></span>ZSV-3 Fee Program Code

|             |                                                                                                                                                                                                                           |                                  |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Definition: | This is the internal value of the \*FEE PROGRAM field (#1.5) in the FEE BASIS PAYMENT file (#162). It is a pointer to the FEE BASIS PROGRAM file (#161.8). This is the Fee Basis program that this payment is related to. |                                  |
| Code:       | Value                                                                                                                                                                                                                     | Description                      |
|             | 2                                                                                                                                                                                                                         | OUTPATIENT                       |
|             | 3                                                                                                                                                                                                                         | PHARMACY                         |
|             | 4                                                                                                                                                                                                                         | COMP & PENSION                   |
|             | 5                                                                                                                                                                                                                         | DENTAL                           |
|             | 6                                                                                                                                                                                                                         | CIVIL HOSPITAL                   |
|             | 7                                                                                                                                                                                                                         | CONTRACT NURSING HOME            |
|             | 8                                                                                                                                                                                                                         | CHAMPVA                          |
|             | 9                                                                                                                                                                                                                         | CONTRACT READJUSTMENT COUNSELING |
|             | 10                                                                                                                                                                                                                        | CONTRACT HALFWAY HOUSES          |
|             | 11                                                                                                                                                                                                                        | HOME HEALTH SERVICES             |
|             | 12                                                                                                                                                                                                                        | OTHER INSTITUTIONAL SERVICES     |
|             | 13                                                                                                                                                                                                                        | DIALYSIS                         |
|             | 14                                                                                                                                                                                                                        | OXYGEN SERVICES                  |
|             | 15                                                                                                                                                                                                                        | STATE HOME                       |
| Example:    | 4                                                                                                                                                                                                                     |                                  |

4.  <span id="ZSV04" class="anchor"></span>ZSV-4 Service Provided (CPT code)

|             |                                                                                                                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the SERVICE PROVIDED field (#.01) in the FEE BASIS PAYMENT file (#162), sub-file \#162.03. It is a pointer to the CPT file (#81). It represents the outpatient and ancillary service provided to the Fee Basis patient. |
| Example:    | 74170                                                                                                                                                                                                                       |

5.  <span id="ZSV05" class="anchor"></span>ZSV-5 Purpose of Visit

|             |                                                                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the PURPOSE OF VISIT field (#16) in the FEE BASIS PAYMENT file (#162), sub-file \#162.03. It is the purpose that the veteran received the service provided. |
| Example:    | OPT SERVICES/TREATMENT FOR NSC DISABILITIES                                                                                                                         |

6.  <span id="ZSV06" class="anchor"></span>ZSV-6 Primary Diagnosis

|             |                                                                                                                                                |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the PRIMARY DIAGNOSIS field (#28) in the FEE BASIS PAYMENT file (#162), sub-file \#162.03. It is the primary diagnosis of the patient. |
| Example:    | 592.0                                                                                                                                          |

7.  <span id="ZSV07" class="anchor"></span>ZSV-7 Place of Service

|             |                                                                                                                                                            |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the PLACE OF SERVICE field (#30) in the FEE BASIS PAYMENT file (#162), sub-file \#162.03. It is where the service was administered to the veteran. |
| Example:    | 1284.91                                                                                                                                                |

2.  Sample ZSV Segment

ZSV\|2184-169-1-1\|20040509\|\|74170\|OPT SERVICES/TREATMENT FOR NSC DISABILITIES\|592.0\|OUTPATIENT HOSPITAL (22)

5.  ZRX – Purchased Care Drug Segment

| SEQ | LEN | DT  | OPT | RP/# | TBL# | Field Name          | CCR                 |
|-----|-----|-----|-----|------|------|---------------------|---------------------|
| 1   | 16  | ST  | R   |      |      | Key                 | [See Notes](#ZRX01) |
| 2   | 8   | ST  | O   |      |      | Prescription Number | [See Notes](#ZRX02) |
| 3   | 8   | DT  | O   |      |      | Date Rx Filled      | [See Notes](#ZRX03) |
| 4   | 45  | ST  | R   |      |      | Drug Name           | [See Notes](#ZRX04) |
| 5   | 40  | ST  | O   |      |      | Generic Drug Name   | [See Notes](#ZRX05) |
| 6   | 20  | ST  | O   |      |      | Drug Strength       | [See Notes](#ZRX06) |
| 7   | 15  | ST  | O   |      |      | Drug Quantity       | [See Notes](#ZRX07) |

1.  Field Definitions
    1.  <span id="ZRX01" class="anchor"></span>ZRX-1 Key

|             |                                                                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition: | This is a combination of 2 IENs: FEE BASIS PHARMACY INVOICE file (#162.1), and sub-file \#162.11. This is a unique key representing the drug record for the patient. |
| Example:    | 6543-1                                                                                                                                                           |

2.  <span id="ZRX02" class="anchor"></span>ZRX-2 Prescription Number

|             |                                                                                                                  |
|-------------|------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the PRESCRIPTION NUMBER field (#.01) in the FEE BASIS PHARMACY INVOICE file (#162.1), sub-file \#162.11. |
| Example:    | 1234567                                                                                                      |

3.  <span id="ZRX03" class="anchor"></span>ZRX-3 Date Rx Filled

|             |                                                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------|
| Definition: | This is the DATE PRESCRIPTION FILLED field (#2) in the FEE BASIS PHARMACY INVOICE file (#162.1), sub-file \#162.11. |
| Example:    | 19931221                                                                                                        |

4.  <span id="ZRX04" class="anchor"></span>ZRX-4 Drug Name

|             |                                                                                                      |
|-------------|------------------------------------------------------------------------------------------------------|
| Definition: | This is the DRUG NAME field (#1) in the FEE BASIS PHARMACY INVOICE file (#162.1), sub-file \#162.11. |
| Example:    | CONDYLOX                                                                                             |

5.  <span id="ZRX05" class="anchor"></span>ZRX-5 Generic Drug Name

|             |                                                                                                         |
|-------------|---------------------------------------------------------------------------------------------------------|
| Definition: | This is the GENERIC DRUG field (#9) in the FEE BASIS PHARMACY INVOICE file (#162.1), sub-file \#162.11. |
| Example:    | PODOFILOX 0.5% TOP SOLN                                                                                 |

6.  <span id="ZRX06" class="anchor"></span>ZRX-6 Drug Strength

|             |                                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------|
| Definition: | This is the STRENGTH field (#1.5) in the FEE BASIS PHARMACY INVOICE file (#162.1), sub-file \#162.11. |
| Example:    | 0.5%                                                                                                  |

7.  <span id="ZRX07" class="anchor"></span>ZRX-7 Drug Quantity

|             |                                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------|
| Definition: | This is the QUANTITY field (#1.6) in the FEE BASIS PHARMACY INVOICE file (#162.1), sub-file \#162.11. |
| Example:    | 30                                                                                                |

2.  Sample ZRX Segment

ZRX\|6543-1\|1234567\|19931221\|CONDYLOX\|PODOFILOX 0.5% TOP SOLN\|0.5%\|1

6.  HL7 Tables

| Table                                           | Type                                              | Name                                               |         | Value  | Description                                                                                                                                                                 |                                                                                                                                                                                                                |
|-------------------------------------------------|---------------------------------------------------|----------------------------------------------------|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0001                                        | <span id="T0001" class="anchor"></span>User   | Administrative sex                             |         | A      | Ambiguous                                                                                                                                                                   |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | F      | Female                                                                                                                                                                      |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | M      | Male                                                                                                                                                                        |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | N      | Not applicable                                                                                                                                                              |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | O      | Other                                                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | U      | Unknown                                                                                                                                                                     |                                                                                                                                                                                                                |
| 0004                                        | User                                          | Patient class                                  |         | B      | Obstetrics                                                                                                                                                                  |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | C      | Commercial Account                                                                                                                                                          |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | E      | Emergency                                                                                                                                                                   |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | I      | Inpatient                                                                                                                                                                   |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | N      | Not Applicable                                                                                                                                                              |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | O      | Outpatient                                                                                                                                                                  |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | P      | Preadmit                                                                                                                                                                    |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | R      | Recurring patient                                                                                                                                                           |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | U      | Unknown                                                                                                                                                                     |                                                                                                                                                                                                                |
| 0005                                        | User                                          | Race                                           |         | 1002-5 | American Indian or Alaska Native                                                                                                                                            |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | 2028-9 | Asian                                                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | 2054-5 | Black or African American                                                                                                                                                   |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | 2076-8 | Native Hawaiian or Other Pacific Islander                                                                                                                                   |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | 2106-3 | White                                                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | 2131-1 | Other Race                                                                                                                                                                  |                                                                                                                                                                                                                |
| 0008                                        | <span id="T0008" class="anchor"></span>HL7    | Acknowledgment code                            |         | AA     | Original mode: Application Accept - Enhanced mode: Application acknowledgment: Accept                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | AE     | Original mode: Application Error - Enhanced mode: Application acknowledgment: Error                                                                                         |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | AR     | Original mode: Application Reject - Enhanced mode: Application acknowledgment: Reject                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | CA     | Enhanced mode: Accept acknowledgment: Commit Accept                                                                                                                         |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | CE     | Enhanced mode: Accept acknowledgment: Commit Error                                                                                                                          |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | CR     | Enhanced mode: Accept acknowledgment: Commit Reject                                                                                                                         |                                                                                                                                                                                                                |
| 0061                                        | <span id="T0061" class="anchor"></span>HL7    | Check digit scheme                             |         | ISO    | ISO 7064: 1983                                                                                                                                                              |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | M10    | Mod 10 algorithm                                                                                                                                                            |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | M11    | Mod 11 algorithm                                                                                                                                                            |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | NPI    | Check digit algorithm in the US National Provider Identifier                                                                                                                |                                                                                                                                                                                                                |
| 0078                                        | <span id="T0078" class="anchor"></span>User   | Abnormal Flags                                 |         | \<     | Below absolute low-off instrument scale                                                                                                                                     |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | \>     | Above absolute high-off instrument scale                                                                                                                                    |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | A      | Abnormal (applies to non-numeric results)                                                                                                                                   |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | AA     | Very abnormal (applies to non-numeric units, analogous to panic limits for numeric units)                                                                                   |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | B      | Better--use when direction not relevant                                                                                                                                     |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | D      | Significant change down                                                                                                                                                     |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | H      | Above high normal                                                                                                                                                           |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | HH     | Above upper panic limits                                                                                                                                                    |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | I      | Intermediate\*                                                                                                                                                              |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | L      | Below low normal                                                                                                                                                            |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | LL     | Below lower panic limits                                                                                                                                                    |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | MS     | Moderately susceptible\*                                                                                                                                                    |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | N      | Normal (applies to non-numeric results)                                                                                                                                     |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | null   | No range defined, or normal ranges don't apply                                                                                                                              |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | R      | Resistant\*                                                                                                                                                                 |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | S      | Susceptible\*                                                                                                                                                               |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | U      | Significant change up                                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | VS     | Very susceptible\*                                                                                                                                                          |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | W      | Worse--use when direction not relevant                                                                                                                                      |                                                                                                                                                                                                                |
| <span id="T0085" class="anchor"></span>0085 | HL7                                           | Observation result status codes interpretation |         | C      | Record coming over is a correction and thus replaces a final result                                                                                                         |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | D      | Deletes the OBX record                                                                                                                                                      |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | F      | Final results; Can only be changed with a corrected result.                                                                                                                 |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | I      | Specimen in lab; results pending                                                                                                                                            |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | N      | Not asked; used to affirmatively document that the observation identified in the OBX was not sought when the universal service ID in OBR-4 implies that it would be sought. |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | O      | Order detail description only (no result)                                                                                                                                   |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | P      | Preliminary results                                                                                                                                                         |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | R      | Results entered -- not verified                                                                                                                                             |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | S      | Partial results                                                                                                                                                             |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | U      | Results status change to final without retransmitting results already sent as "preliminary" (e.g., radiology changes status from preliminary to final)                      |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | W      | Post original as wrong, e.g., transmitted for wrong patient                                                                                                                 |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | X      | Results cannot be obtained for this observation                                                                                                                             |                                                                                                                                                                                                                |
| 0103                                        | <span id="T0103" class="anchor"></span>HL7    | Processing ID                                  |         | D      | Debugging                                                                                                                                                                   |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | P      | Production                                                                                                                                                                  |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | T      | Training                                                                                                                                                                    |                                                                                                                                                                                                                |
| 0125                                        | <span id="T0125" class="anchor"></span>HL7    | Value type                                     |         | AD     | Address                                                                                                                                                                     |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | CE     | Coded Entry                                                                                                                                                                 |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | CF     | Coded Element With Formatted Values                                                                                                                                         |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | CK     | Composite ID With Check Digit                                                                                                                                               |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | CN     | Composite ID And Name                                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | CP     | Composite Price                                                                                                                                                             |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | CX     | Extended Composite ID With Check Digit                                                                                                                                      |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | DT     | Date                                                                                                                                                                        |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | ED     | Encapsulated Data                                                                                                                                                           |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | FT     | Formatted Text (Display)                                                                                                                                                    |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | MO     | Money                                                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | NM     | Numeric                                                                                                                                                                     |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | PN     | Person Name                                                                                                                                                                 |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | RP     | Reference Pointer                                                                                                                                                           |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | SN     | Structured Numeric                                                                                                                                                          |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | ST     | String Data.                                                                                                                                                                |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | TM     | Time                                                                                                                                                                        |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | TN     | Telephone Number                                                                                                                                                            |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | TS     | Time Stamp (Date & Time)                                                                                                                                                    |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | TX     | Text Data (Display)                                                                                                                                                         |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | XAD    | Extended Address                                                                                                                                                            |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | XCN    | Extended Composite Name And Number For Persons                                                                                                                              |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | XON    | Extended Composite Name And Number For Organizations                                                                                                                        |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | XPN    | Extended Person Name                                                                                                                                                        |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | XTN    | Extended Telecommunications Number                                                                                                                                          |                                                                                                                                                                                                                |
| 0136                                        | <span id="T0136" class="anchor"></span>HL7    | Yes/no indicator                               |         | N      | No                                                                                                                                                                          |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | Y      | Yes                                                                                                                                                                         |                                                                                                                                                                                                                |
| 0155                                        | <span id="T0155" class="anchor"></span>HL7    | Accept/application acknowledgment conditions   |         | AL     | Always                                                                                                                                                                      |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | ER     | Error/reject conditions only                                                                                                                                                |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | NE     | Never                                                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | SU     | Successful completion only                                                                                                                                                  |                                                                                                                                                                                                                |
| 0203                                        | <span id="T0203" class="anchor"></span>User   | Identifier type                                |         | AM     | American Express                                                                                                                                                            |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | AN     | Account number                                                                                                                                                              |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | BA     | Bank Account Number                                                                                                                                                         |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | BR     | Birth registry number                                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | BRN    | Breed Registry Number                                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | DI     | Diner's Club card                                                                                                                                                           |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | DL     | Driver's license number                                                                                                                                                     |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | DN     | Doctor number                                                                                                                                                               |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | DR     | Donor Registration Number                                                                                                                                                   |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | DS     | Discover Card                                                                                                                                                               |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | EI     | Employee number                                                                                                                                                             |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | EN     | Employer number                                                                                                                                                             |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | FI     | Facility ID                                                                                                                                                                 |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | GI     | Guarantor internal identifier                                                                                                                                               |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | GN     | Guarantor external identifier                                                                                                                                               |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | HC     | Health Card Number                                                                                                                                                          |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | JHN    | Jurisdictional health number (Canada)                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | LN     | License number                                                                                                                                                              |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | LR     | Local Registry ID                                                                                                                                                           |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | MA     | Medicaid number                                                                                                                                                             |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | MC     | Medicare number                                                                                                                                                             |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | MCN    | Microchip Number                                                                                                                                                            |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | MR     | Medical record number                                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | MS     | MasterCard                                                                                                                                                                  |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | NE     | National employer identifier                                                                                                                                                |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | NH     | National Health Plan Identifier                                                                                                                                             |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | NI     | National unique individual identifier                                                                                                                                       |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | NNxxx  | National Person Identifier where xxx is the ISO table 3166 3-character (alphabetic) country code                                                                            |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | NPI    | National provider identifier                                                                                                                                                |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | PEN    | Pension Number                                                                                                                                                              |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | PI     | Patient internal identifier                                                                                                                                                 |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | PN     | Person number                                                                                                                                                               |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | PRN    | Provider number                                                                                                                                                             |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | PT     | Patient external identifier                                                                                                                                                 |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | RR     | Railroad Retirement number                                                                                                                                                  |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | RRI    | Regional registry ID                                                                                                                                                        |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | SL     | State license                                                                                                                                                               |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | SR     | State registry ID                                                                                                                                                           |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | SS     | Social Security number                                                                                                                                                      |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | U      | Unspecified                                                                                                                                                                 |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | UPIN   | Medicare/HCFA's Universal Physician Identification numbers                                                                                                                  |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | VN     | Visit number                                                                                                                                                                |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | VS     | VISA                                                                                                                                                                        |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | WC     | WIC identifier                                                                                                                                                              |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | WCN    | Workers' Comp Number                                                                                                                                                        |                                                                                                                                                                                                                |
|                                                 |                                                   |                                                    |         | XX     | Organization identifier                                                                                                                                                     |                                                                                                                                                                                                                |
| 0207                                        | <span id="T0207" class="anchor"></span>HL7    | Processing mode                                | A       |        |                                                                                                                                                                             | Archive                                                                                                                                                                                                        |
|                                                 |                                                   |                                                    | I       |        |                                                                                                                                                                             | Initial load                                                                                                                                                                                                   |
|                                                 |                                                   |                                                    | R       |        |                                                                                                                                                                             | Restore from archive                                                                                                                                                                                           |
|                                                 |                                                   |                                                    | T       |        |                                                                                                                                                                             | Current processing, transmitted at intervals (scheduled or on demand). This is the default mode (if the value is omitted).                                                                                     |
| 0301                                        | <span id="T0301" class="anchor"></span>HL7    | Universal ID type                              | DNS     |        |                                                                                                                                                                             | An Internet dotted name. Either in ASCII or as integers                                                                                                                                                        |
|                                                 |                                                   |                                                    | GUID    |        |                                                                                                                                                                             | Same as UUID.                                                                                                                                                                                                  |
|                                                 |                                                   |                                                    | HCD     |        |                                                                                                                                                                             | The CEN Healthcare Coding Scheme Designator. (Identifiers used in DICOM follow this assignment scheme.)                                                                                                        |
|                                                 |                                                   |                                                    | HL7     |        |                                                                                                                                                                             | Reserved for future HL7 registration schemes                                                                                                                                                                   |
|                                                 |                                                   |                                                    | ISO     |        |                                                                                                                                                                             | An International Standards Organization Object Identifier                                                                                                                                                      |
|                                                 |                                                   |                                                    | L, M, N |        |                                                                                                                                                                             | These are reserved for locally defined coding schemes.                                                                                                                                                         |
|                                                 |                                                   |                                                    | Random  |        |                                                                                                                                                                             | Usually a base64 encoded string of random bits. The uniqueness depends on the length of the bits. Mail systems often generate ASCII string "unique names," from a combination of random bits and system names. |
|                                                 |                                                   |                                                    | UUID    |        |                                                                                                                                                                             | The DCE Universal Unique Identifier                                                                                                                                                                            |
|                                                 |                                                   |                                                    | x400    |        |                                                                                                                                                                             | An X.400 MHS format identifier                                                                                                                                                                                 |
|                                                 |                                                   |                                                    | x500    |        |                                                                                                                                                                             | An X.500 directory name                                                                                                                                                                                        |
| 0362                                        | <span id="T0362" class="anchor"></span>User   | Sending/receiving facility                     | NNN     |        |                                                                                                                                                                             | Station number from the INSTITUTION file (#4) without suffix.                                                                                                                                                  |
| VA001                                       | <span id="TVA001" class="anchor"></span>Local | Yes/No                                         | 0       |        |                                                                                                                                                                             | No                                                                                                                                                                                                             |
|                                                 |                                                   |                                                    | 1       |        |                                                                                                                                                                             | Yes                                                                                                                                                                                                            |

<span id="_Toc228789362" class="anchor"></span>

1.  Glossary[^3]

| [  A  ](\l)   | [  B  ](#G_B) | [  C  ](#G_C) | [  D  ](#G_D) | [  E  ](#G_E) | [  F  ](#G_F) | [  G  ](#G_G) | [  H  ](#G_H) | [  I  ](#G_I) |     | [  K  ](#G_K) | [  L  ](#G_L) | [  M  ](#G_M) |
|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|-----|---------------|---------------|---------------|
| [  N  ](#G_N) | [ O ](#G_O)   | [ P ](#G_P)   |               | [  R  ](#G_R) | [  S  ](#G_S) | [  T  ](#G_T) | [  U  ](#G_U) | [  V  ](#G_V) |     | [  X  ](#G_X) |               |               |
| [0-9](#G_09)  |               |               |               |               |               |               |               |               |     |               |               |               |

*Control-click character to see entries; missing character means no entries for that character.*

| Term or Acronym                                 | Description                    |
|-------------------------------------------------|--------------------------------|
| <span id="G_09" class="anchor"></span>0 - 9 |                                |
| 508                                             | *See* [Section 508](#Glos_508) |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><strong>A</strong></td>
</tr>
<tr class="even">
<td colspan="2">AAC</td>
<td><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a><strong>.</strong></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_AccessCode" class="anchor"></span>Access Code</td>
<td>With each sign-on to <a href="#Glos_VistA">VistA</a>, the user must enter two codes to be recognized and allowed to proceed: the Access Code and Verify Code. The Access Code is assigned by IRM Service and is used by the computer to recognize the user. Each user has a unique access code. The only way this code can be changed is for the IRM Service to edit it. When the code is established by IRM, it is encrypted; that is, it is "scrambled" according to a cipher. The code is stored in the computer only in this encrypted form. Thus, even if the access code is viewed, the viewer cannot determine what the user actually types to tell the computer this code. <em>See also</em> <a href="#Glos_VerifyCode">Verify Code</a>.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_AIDS" class="anchor"></span>Acquired Immunodeficiency Syndrome (AIDS)</td>
<td>AIDS is a disease of the human immune system caused by the human immunodeficiency virus (HIV). This condition progressively reduces the effectiveness of the immune system and leaves individuals susceptible to opportunistic infections and tumors.</td>
</tr>
<tr class="odd">
<td colspan="2">ADPAC</td>
<td><em>See</em> <a href="#Glos_ADPAC">Automated Data Processing Application Coordinator</a><strong>.</strong></td>
</tr>
<tr class="even">
<td colspan="2">AIDS</td>
<td><em>See</em> <a href="#Glos_AIDS">Acquired Immunodeficiency Syndrome</a><strong>.</strong></td>
</tr>
<tr class="odd">
<td colspan="2">AITC</td>
<td><em>See</em> <a href="#Glos_AITC">Austin Information Technology Center</a></td>
</tr>
<tr class="even">
<td colspan="2">AMIS</td>
<td><em>See</em> <a href="#Glos_AMIS">Automated Management Information System</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ARV" class="anchor"></span>Antiretroviral (medications)</td>
<td><p>Medications for the treatment of infection by <a href="#Glos_retrovirus">retroviruses</a>, primarily <a href="#Glos_HIV">HIV</a>.</p>
<p><em>See also</em> <a href="#Glos_HAART">Highly Active Antiretroviral Therapy</a>.</p></td>
</tr>
<tr class="even">
<td colspan="2">API</td>
<td>See <a href="#Glos_API">Application Program Interface</a>.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_API" class="anchor"></span>Application Program Interface (API)</td>
<td><p>The interface (calling conventions) by which an application program accesses operating system and other services. An API is defined at source code level and provides a level of abstraction between the application and the <a href="#Glos_Kernel">kernel</a> (or other privileged utilities) to ensure the portability of the code.</p>
<p>An API can also provide an interface between a high level language and lower level utilities and services which were written without consideration for the calling conventions supported by compiled languages. In this case, the API's main task may be the translation of parameter lists from one format to another and the interpretation of call-by-value and call-by-reference arguments in one or both directions.</p>
<p><em>See also</em> 11, Application Program Interfaces<strong>.</strong></p></td>
</tr>
<tr class="even">
<td colspan="2">ARV</td>
<td><em>See</em> <a href="#Glos_ARV">Antiretroviral (medications).</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_AITC" class="anchor"></span>Austin Automation Center (AAC)</td>
<td><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a></td>
</tr>
<tr class="even">
<td colspan="2">Austin Information Technology Center (AITC)</td>
<td>AITC is a recognized, award-winning Federal data center within the Department of Veterans Affairs (VA). It provides a full complement of cost-efficient e-government solutions to support the information technology (IT) needs of customers within the Federal sector. AITC has also implemented a program of enterprise "best practice" initiatives with major vendor partners that ensures customers receive enhanced, value-added IT services through the implementation of new technologies at competitive costs.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ADPAC" class="anchor"></span>Automated Data Processing Application Coordinator (ADPAC)</td>
<td>The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they [Run] into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or Information Resource Management (IRM).</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_AMIS" class="anchor"></span>Automated Management Information System (AMIS)</td>
<td>The VHA Decision Support System (DSS) is a national automated management information system based on commercial software to integrate data from clinical and financial systems for both inpatient and outpatient care. The commercial software is utilized with interfaces developed to transport data into the system from the <a href="#Glos_VistA">Veterans Health Information Systems and Technology Architecture</a> (VistA), the National Patient Care Database (NPCD), the Patient Treatment File (PTF), and various VA financial information systems. The VHA began implementation of DSS in 1994. Full implementation was completed in 1999 and DSS is now used throughout the VA healthcare system.</td>
</tr>
<tr class="odd">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="2">to Glossary Contents</td>
</tr>
</tbody>
</table>

| Term or Acronym                            |                      | Description                                                                                                                         |     |
|--------------------------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----|
| <span id="G_B" class="anchor"></span>B |                      |                                                                                                                                     |     |
| B-Type Option                              |                      | In VistA, an option designed to be run only by the [RPC Broker](#Glos_RPCBroker), and which cannot be run from the menu system. |     |
| Borland® Delphi®                           |                      | *See* [Delphi](#Glos_Delphi)                                                                                                        |     |
| [ BACK ](#_Toc228789362)               | to Glossary Contents |                                                                                                                                     |     |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><span id="G_C" class="anchor"></span><strong>C</strong></td>
</tr>
<tr class="even">
<td colspan="2">CCOW</td>
<td><em>See</em> <a href="#Glos_CCOW">Clinical Context Object Workgroup</a></td>
</tr>
<tr class="odd">
<td colspan="2">CCR</td>
<td><em>See</em> <a href="#Glos_CCR">Clinical Case Registries</a></td>
</tr>
<tr class="even">
<td colspan="2">CDC</td>
<td><em>See</em> <a href="#Glos_CDC">Centers for Disease Control and Prevention</a></td>
</tr>
<tr class="odd">
<td colspan="2">CDCO</td>
<td><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CDC" class="anchor"></span>Centers for Disease Control and Prevention (CDC)</td>
<td><p>The CDC is one of the major operating components of the United States Department of Health and Human Services. It includes a number of Coordinating Centers and Offices which specialize in various aspects of public health, as well as the National Institute for Occupational Safety and Health (NIOSH).</p>
<p><em>See</em> <a href="http://www.cdc.gov/about/organization/cio.htm">http://www.cdc.gov/about/organization/cio.htm</a></p></td>
</tr>
<tr class="odd">
<td colspan="2">Center for Quality Management in Public Health (CQM)</td>
<td>CQM, based in the VA Palo Alto Health Care System, functions as part of the VA Public Health Strategic Health Care Group at VA Central Office in Washington, DC. CQM was first established with a primary focus on HIV care; the mission expanded to include Hepatitis C issues in January 2001. In line with the mission of its organizational parent, the CQM mission further expanded to include work on various issues and conditions with public health significance, including operational support and management of data from the Clinical Case Registries (CCR) software.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CCR" class="anchor"></span>Clinical Case Registries (CCR)</td>
<td><strong>The Clinical Case Registries (</strong>CCR) application collects data on the population of veterans with certain clinical conditions, namely <a href="#Glos_HepatitisC">Hepatitis C</a> and <a href="#Glos_HIV">Human Immunodeficiency Virus</a> (HIV) infections.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CCOW" class="anchor"></span>Clinical Context Object Workgroup (CCOW)</td>
<td><p>CCOW is an <a href="#Glos_HL7">HL7</a> standard protocol designed to enable disparate applications to synchronize in real-time, and at the user-interface level. It is vendor independent and allows applications to present information at the desktop and/or portal level in a unified way.</p>
<p>CCOW is the primary standard protocol in healthcare to facilitate a process called "Context Management." Context Management is the process of using particular "subjects" of interest (e.g., user, patient, clinical encounter, charge item, etc.) to 'virtually' link disparate applications so that the end-user sees them operate in a unified, cohesive way.</p>
<p>Context Management can be utilized for both CCOW and non-CCOW compliant applications. The CCOW standard exists to facilitate a more robust, and near "plug-and-play" interoperability across disparate applications.</p>
<p>Context Management is often combined with <a href="#Glos_SSO">Single Sign On</a> applications in the healthcare environment, but the two are discrete functions. Single Sign On is the process that enables the secure access of disparate applications by a user through use of a single authenticated identifier and password.</p></td>
</tr>
<tr class="even">
<td colspan="2">Comma-Delimited Values (CDV)</td>
<td><em>See</em> <a href="#Glos_CSV">Comma-Separated Values</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CSV" class="anchor"></span>Comma-Separated Values (CSV)</td>
<td>"Separated" or "delimited" data files use specific characters (delimiters) to separate its values. Most database and spreadsheet programs are able to read or save data in a delimited format. The comma-separated values file format is a delimited data format that has fields separated by the comma character and records separated by newlines. Excel can import such a file and create a spreadsheet from it.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CPRS" class="anchor"></span>Computerized Patient Record System (CPRS)</td>
<td>A Computerized Patient Record (CPR) is a comprehensive database system used to store and access patients' healthcare information. CPRS is the Department of Veteran's Affairs electronic health record software. The CPRS organizes and presents all relevant data on a patient in a way that directly supports clinical decision making. This data includes medical history and conditions, problems and diagnoses, diagnostic and therapeutic procedures and interventions. Both a graphic user interface version and a character-based interface version are available. CPRS provides a single interface for health care providers to review and update a patient's medical record, and to place orders, including medications, special procedures, x-rays, patient care nursing orders, diets, and laboratory tests. CPRS is flexible enough to be implemented in a wide variety of settings for a broad spectrum of health care workers, and provides a consistent, event-driven, Windows-style interface.</td>
</tr>
<tr class="odd">
<td colspan="2"><em>Contextor</em> software</td>
<td><p>Sentillion <em>Contextor</em> can be embedded within an application to implement most of <a href="#Glos_CCOW">CCOW</a>'s context participant behaviors. <em>Contextor</em> is compatible with any CCOW-compliant context manager and is designed to simplify writing applications that support the CCOW standard. It includes these development environment components:</p>
<ul>
<li><p>CCOW-compliant code samples of Windows and Web applications</p></li>
<li><p>Development-only version of Sentillion Context Manager</p></li>
<li><p>Development tools for simulating and observing the behavior of a context-enabled desktop</p></li>
<li><p>Configuration and administration tool</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CDCO" class="anchor"></span>Corporate Data Center Operations (CDCO)</td>
<td>Federal data center within the Department of Veterans Affairs (VA). As a franchise fund, or fee-for-service organization, CDCO-Austin provides cost-efficient IT enterprise solutions to support the information technology needs of customers within the Federal sector. <em>Formerly</em> the Austin Automation Center (AAC); <em>formerly</em> the Austin Information Technology Center (AITC).</td>
</tr>
<tr class="odd">
<td colspan="2">CPRS</td>
<td><em>See</em> <a href="#Glos_CPRS">Computerized Patient Record System</a></td>
</tr>
<tr class="even">
<td colspan="2">CPT</td>
<td><em>See</em> <a href="#Glos_CPT">Current Procedural Terminology</a></td>
</tr>
<tr class="odd">
<td colspan="2">CSV</td>
<td><em>See</em> <a href="#Glos_CSV">Comma-Separated Values</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CPT" class="anchor"></span>Current Procedural Terminology (CPT)</td>
<td><p>CPT® is the most widely accepted medical nomenclature used to report medical procedures and services under public and private health insurance programs. CPT codes describe a procedure or service identified with a five-digit CPT code and descriptor nomenclature. The CPT code set accurately describes medical, surgical, and diagnostic services and is designed to communicate uniform information about medical services and procedures among physicians, coders, patients, accreditation organizations, and payers for administrative, financial, and analytical purposes. The current version is the CPT 2009.</p>
<p><em>Note:</em> CPT® is a registered trademark of the American Medical Association.</p></td>
</tr>
<tr class="odd">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="2">to Glossary Contents</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><span id="G_D" class="anchor"></span><strong>D</strong></td>
</tr>
<tr class="even">
<td><span id="Glos_DBIA" class="anchor"></span>Database Integration Agreement (DBIA)</td>
<td><strong>M</strong> code is not "compiled and linked," so any code is open to anyone to call. The same is true for the data. This permits an incredible level of integration between applications, but it is "too open" for some software architects' liking. The VA has instituted Database Integration Agreements to enforce external policies and procedures to avoid unwanted dependencies.</td>
</tr>
<tr class="odd">
<td>Data Dictionary</td>
<td>A data structure that stores meta-data, i.e. data about data. The term "data dictionary" has several uses; most generally it is thought of as a set of data descriptions that can be shared by several applications. In practical terms, it usually means a table in a database that stores the names, field types, length, and other characteristics of the fields in the database tables.</td>
</tr>
<tr class="even">
<td>DBIA</td>
<td><em>See</em> <a href="#Glos_DBIA">Database Integration Agreement</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_Delphi" class="anchor"></span>Delphi</td>
<td><p>Delphi® is a software development package, formerly from Borland® and now developed by Embarcadero Technologies.® This is the software that was used to produce the CCR application.</p>
<p><em>See also</em> <a href="http://www.embarcadero.com/products/delphi">http://www.embarcadero.com/products/delphi</a></p></td>
</tr>
<tr class="even">
<td>DFN</td>
<td><em>See</em> <a href="#Glos_FileNumber">File Number</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td>to Glossary Contents</td>
</tr>
</tbody>
</table>

| Term or Acronym                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| <span id="G_E" class="anchor"></span>E                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
| Epoetin                                                                     | Epoetin Alfa is used for treating anemia in certain patients with kidney failure, HIV, or cancer.                                                                                                                                                                                                                                                                                                                                                                                                |     |
| <span id="Glos_XML" class="anchor"></span>Extensible Mark-up Language (XML) | An initiative from the W3C defining an "extremely simple" dialect of [SGML](#Glos_SGML) suitable for use on the World-Wide Web.                                                                                                                                                                                                                                                                                                                                                                  |     |
| Extract Data Definition                                                     | A set of file and field numbers which identify the data that should be retrieved during the extraction process.                                                                                                                                                                                                                                                                                                                                                                                  |     |
| Extract Process                                                             | This process is run after the [update process](#Glos_UpdateProcess). This function goes through patients on the local registry and, depending on their status, extracts all available data for the patient since the last extract was run. This process also updates any demographic data held in the local registry for all existing patients that have changed since the last extract. The extract transmits any collected data for the patient to the national database via [HL7](#Glos_HL7). |     |
| [ BACK ](#_Toc228789362)                                                | to Glossary Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |     |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 1%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_F" class="anchor"></span><strong>F</strong></td>
</tr>
<tr class="even">
<td colspan="2">FDA</td>
<td colspan="3"><em>See</em> <strong>Food and Drug Administration</strong></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_FileNumber" class="anchor"></span>File Number</td>
<td colspan="3">In <a href="#Glos_VistA">VistA</a>, the local/facility patient record number (patient file internal entry number).</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_FileMan" class="anchor"></span>FileMan</td>
<td colspan="3"><p>FileMan is a set of <a href="#Glos_M">M</a> utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.</p>
<p>Its first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_FTP" class="anchor"></span>File Transfer Protocol (FTP)</td>
<td colspan="3">FTP is a client-server protocol which allows a user on one computer to transfer files to and from another computer over a network. It is defined in <a href="http://www.ietf.org/rfc/rfc959.txt">STD 9, RFC 959</a>.</td>
</tr>
<tr class="even">
<td colspan="2">Food and Drug Administration (FDA)</td>
<td colspan="3">FDA is an agency of the United States Department of Health and Human Services and is responsible for regulating and supervising the safety of foods, dietary supplements, drugs, vaccines, biological medical products, blood products, medical devices, radiation-emitting devices, veterinary products, and cosmetics. The FDA also enforces section 361 of the Public Health Service Act and the associated regulations, including sanitation requirements on interstate travel as well as specific rules for control of disease on products ranging from pet turtles to semen donations for assisted reproductive medicine techniques.</td>
</tr>
<tr class="odd">
<td colspan="2">FTP</td>
<td colspan="3"><em>See</em> <a href="#Glos_FTP">File Transfer Protocol</a></td>
</tr>
<tr class="even">
<td colspan="2">Function key</td>
<td colspan="3">A key on a computer or terminal keyboard which can be programmed so as to cause an operating system command interpreter or application program to perform certain actions. On some keyboards/computers, function keys may have default actions, accessible on power-on. For example, <strong>&lt;F1&gt;</strong> is traditionally the function key used to activate a help system.</td>
</tr>
<tr class="odd">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_G" class="anchor"></span><strong>G</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_Globals" class="anchor"></span>Globals</td>
<td colspan="3"><p><a href="#Glos_M">M</a> uses globals, variables which are intrinsically stored in files and persist beyond the program or process completion. Globals appear as normal variables with the caret character in front of the name. For example, the <strong>M</strong> statement…</p>
<p>SET ^A("first_name")="Bob"</p>
<p>…will result in a new record being created and inserted in the file structure, persistent just as a file persists in an operating system. Globals are stored, naturally, in highly structured data files by the language and accessed only as <strong>M</strong> globals. Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of <strong>M</strong> is based on its ability to handle all this flawlessly and invisibly to the programmer.</p>
<p>For all of these reasons, one of the most common <strong>M</strong> programs is a database management system. <a href="#Glos_FileMan">FileMan</a> is one such example. <strong>M</strong> allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_GUI" class="anchor"></span>Graphical User Interface (GUI)</td>
<td colspan="3"><p>A graphical user interface (or GUI, often pronounced "gooey") is a graphical (rather than purely textual) user interface to a computer. A GUI is a particular case of user interface for interacting with a computer which employs graphical images and widgets in addition to text to represent the information and actions available to the user. Usually the actions are performed through direct manipulation of the graphical elements. A GUI takes advantage of the computer's graphics capabilities to make the program easier to use.</p>
<p><em>Sources:</em></p>
<p><a href="http://en.wikipedia.org/wiki/GUI">http://en.wikipedia.org/wiki/GUI</a></p>
<p><a href="http://www.webopedia.com/TERM/G/Graphical_User_Interface_GUI.html">http://www.webopedia.com/TERM/G/Graphical_User_Interface_GUI.html</a></p>
<p><em>See also</em> <a href="#Glos_UI">User Interface</a></p></td>
</tr>
<tr class="even">
<td colspan="2">GUI</td>
<td colspan="3"><em>See:</em> <a href="#Glos_GUI">Graphical User Interface</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th>Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_H" class="anchor"></span><strong>H</strong></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">HAART</td>
<td colspan="2"><em>See</em> <a href="#Glos_HAART">Highly Active Antiretroviral Treatment</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_HL7" class="anchor"></span>Health Level 7 (HL7)</td>
<td colspan="2">One of several American National Standards Institute (ANSI)–accredited Standards Developing Organizations operating in the healthcare arena. "Level Seven" refers to the highest level of the International Standards Organization's (ISO) communications model for Open Systems Interconnection (OSI)— the application level. The application level addresses definition of the data to be exchanged, the timing of the interchange, and the communication of certain errors to the application. The seventh level supports such functions as security checks, participant identification, availability checks, exchange mechanism negotiations and, most importantly, data exchange structuring. HL7 focuses on the interface requirements of the entire health care organization. Source: <a href="http://www.hl7.org/about/index.cfm">http://www.hl7.org/about/index.cfm</a>.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Hep C; HEPC</td>
<td colspan="2"><a href="#Glos_HepatitisC">Hepatitis C</a>; the Hepatitis C Registry</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_HepatitisC" class="anchor"></span>Hepatitis C</td>
<td colspan="2"><p>A liver disease caused by the hepatitis C virus (HCV). HCV infection sometimes results in an acute illness, but most often becomes a chronic condition that can lead to cirrhosis of the liver and liver cancer.</p>
<p><em>See</em> <a href="http://www.cdc.gov/hepatitis/index.htm">http://www.cdc.gov/hepatitis/index.htm</a></p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HAART" class="anchor"></span>Highly Active Antiretroviral Treatment (HAART)</td>
<td colspan="2">Antiretroviral drugs are medications for the treatment of infection by retroviruses, primarily <a href="#Glos_HIV">HIV</a>. When several such drugs, typically three or four, are taken in combination, the approach is known as highly active antiretroviral therapy, or HAART. The American National Institutes of Health and other organizations recommend offering antiretroviral treatment to all patients with <a href="#Glos_AIDS">AIDS</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">HIV</td>
<td colspan="2"><em>See</em> <a href="#Glos_HIV">Human Immunodeficiency Virus</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">HL7</td>
<td colspan="2"><em>See</em> <a href="#Glos_HL7">Health Level 7</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">HTML</td>
<td colspan="2"><em>See</em> <a href="#Glos_HTML">Hypertext Mark-up Language</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HIV" class="anchor"></span>Human Immunodeficiency Virus (HIV)</td>
<td colspan="2"><p>HIV is a lentivirus (a member of the retrovirus family) that can lead to acquired immunodeficiency syndrome (<a href="#Glos_AIDS">AIDS</a>), a condition in humans in which the immune system begins to fail, leading to life-threatening opportunistic infections. HIV is different from most other viruses because it attacks the immune system. The immune system gives our bodies the ability to fight infections. HIV finds and destroys a type of white blood cell (T cells or CD4 cells) that the immune system must have to fight disease.</p>
<p>See <a href="http://www.cdc.gov/hiv/">http://www.cdc.gov/hiv/</a>.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_hypertext" class="anchor"></span>hypertext</td>
<td colspan="2">A term coined around 1965 for a collection of documents (or "nodes") containing cross-references or "links" which, with the aid of an interactive browser program, allow the reader to move easily from one document to another.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HTML" class="anchor"></span>Hypertext Mark-up Language (HTML)</td>
<td colspan="2">A <a href="#Glos_hypertext">hypertext</a> document format used on the World-Wide Web. HTML is built on top of <a href="#Glos_SGML">SGML</a>. "Tags" are embedded in the text. A tag consists of a "&lt;", a "directive" (in lower case), zero or more parameters and a "&gt;". Matched pairs of directives, like "&lt;title&gt;" and "&lt;/title&gt;" are used to delimit text which is to appear in a special place or style.</td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="4">to Glossary Contents</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_I" class="anchor"></span><strong>I</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_ICD9" class="anchor"></span>ICD-9</td>
<td colspan="3"><p><em>International Statistical Classification of Diseases and Related Health Problems</em>, ninth edition (commonly abbreviated as "ICD-9") provides numeric codes to classify diseases and a wide variety of signs, symptoms, abnormal findings, complaints, social circumstances and external causes of injury or disease. Every health condition can be assigned to a unique category and given a code, up to six characters long. Such categories can include a set of similar diseases. The "-9" refers to the ninth edition of these codes.</p>
<p><em>See also</em> <a href="#Glos_CPT">Current Procedural Terminology</a></p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ICD10" class="anchor"></span>ICD-10</td>
<td colspan="3"><p><em>International Statistical Classification of Diseases and Related Health Problems</em>, tenth edition (commonly abbreviated as "ICD-10") provides numeric codes to classify diseases and a wide variety of signs, symptoms, abnormal findings, complaints, social circumstances and external causes of injury or disease. Every health condition can be assigned to a unique category and given a code, up to seven characters long. Such categories can include a set of similar diseases. The "-10" refers to the tenth edition of these codes.</p>
<p><em>See also</em> <a href="#Glos_CPT">Current Procedural Terminology</a></p></td>
</tr>
<tr class="even">
<td colspan="2">ICN</td>
<td colspan="3"><em>See</em> <a href="#Glos_ICN">Integration Control Number</a></td>
</tr>
<tr class="odd">
<td colspan="2">ICR</td>
<td colspan="3">See <a href="#Glos_ICR">Immunology Case Registry</a></td>
</tr>
<tr class="even">
<td colspan="2">IEN</td>
<td colspan="3"><em>See</em> <a href="#Glos_IEN">Internal Entry Number</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ICR" class="anchor"></span>Immunology Case Registry (ICR)</td>
<td colspan="3">Former name for <a href="#Glos_CCR">Clinical Case Registries</a> HIV (CCR:HIV).</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_IRM" class="anchor"></span>Information Resources Management (IRM)</td>
<td colspan="3">The service which is involved in planning, budgeting, procurement and management-in-use of VA's information technology investments.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ICN" class="anchor"></span>Integration Control Number (ICN)</td>
<td colspan="3">The national VA patient record number.</td>
</tr>
<tr class="even">
<td colspan="2">Interface</td>
<td colspan="3">An interface defines the communication boundary between two entities, such as a piece of software, a hardware device, or a user.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_IEN" class="anchor"></span>Internal Entry Number (IEN)</td>
<td colspan="3">The number which uniquely identifies each item in the VistA database.</td>
</tr>
<tr class="even">
<td colspan="2">IRM, IRMS</td>
<td colspan="3"><em>See</em> <a href="#Glos_IRM">Information Resources Management</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_Iterator" class="anchor"></span>iterator</td>
<td colspan="3">An object or routine for accessing items from a list, array or stream one at a time.</td>
</tr>
<tr class="even">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

| Term or Acronym                                     |                      |                                                                                                                                 | Description |     |
|-----------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------|-----|
| <span id="G_K" class="anchor"></span>K          |                      |                                                                                                                                 |             |     |
| !KEA                                                |                      | Terminal emulation software. No longer in use in VHA; replaced by *Reflection*.                                                 |             |     |
| <span id="Glos_Kernel" class="anchor"></span>Kernel |                      | The VistA software that enables VistA applications to coexist in a standard operating system independent computing environment. |             |     |
| Keys                                                |                      | *See* [Security Keys](#Glos_SecurityKeys)                                                                                       |             |     |
| [ BACK ](#_Toc228789362)                        | to Glossary Contents |                                                                                                                                 |             |     |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_L" class="anchor"></span><strong>L</strong></td>
</tr>
<tr class="even">
<td colspan="2">Laboratory Information Manager (LIM)</td>
<td colspan="3">Manager of the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other <a href="#Glos_CPRS">Computerized Patient Record System</a> functions.</td>
</tr>
<tr class="odd">
<td colspan="2">Local Registry</td>
<td colspan="3">The local file of patients that were grandfathered into the registry or have passed the selection rules and been added to the registry.</td>
</tr>
<tr class="even">
<td colspan="2">Local Registry Update</td>
<td colspan="3">This process adds new patients (that have had data entered since the last update was run and pass the selection rules) to the local registry.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_LOINC" class="anchor"></span>Logical Observation Identifiers Names and Codes (LOINC)</td>
<td colspan="3"><p>LOINC© is designed to facilitate the exchange and pooling of clinical results for clinical care, outcomes management, and research by providing a set of universal codes and names to identify laboratory and other clinical observations. The Regenstrief Institute, Inc., an internationally renowned healthcare and informatics research organization, maintains the LOINC database and supporting documentation.</p>
<p><em>See</em> <a href="http://loinc.org/">http://loinc.org/</a></p></td>
</tr>
<tr class="even">
<td colspan="2">LOINC</td>
<td colspan="3"><em>See</em> <a href="#Glos_LOINC">Logical Observation Identifiers Names and Codes</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_M" class="anchor"></span><strong>M</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_M" class="anchor"></span>M</td>
<td colspan="3"><p><strong>M</strong> is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. MUMPS data structures are sparse, using strings of characters as subscripts.</p>
<p><strong>M</strong> was formerly (and is still commonly) called MUMPS, for <em>Massachusetts General Hospital Utility Multiprogramming System</em>.</p></td>
</tr>
<tr class="odd">
<td colspan="2">Massachusetts General Hospital Utility Multi-Programming System</td>
<td colspan="3"><em>See</em> <a href="#Glos_M">M</a><strong>.</strong></td>
</tr>
<tr class="even">
<td colspan="2">Message (HL7)</td>
<td colspan="3"><p>An Individual message is, according to the HL7 standard, an "atomic unit of data transferred between systems." HL7 defines a series of electronic messages to support administrative, logistical, financial as well as clinical processes. Since 1987 the standard has been updated regularly. Structurally all individual message contains a header. Some contains body and others don't.</p>
<p>All HL7 messages are made up of segments, composites and primitive data types.</p>
<p>An HL7 message consists of the following data elements: Message type, Message event and Message structure.</p>
<p>The standard also allows, however, the notion of a logical message, whose data is physically broken down to more than one individual messages and correlated together using a logical message id in message headers. The breakup of a message into individual messages is driven primarily by message length negotiated between parties engaging in message exchanges.</p>
<p><em>Sources:</em> <a href="http://publib.boulder.ibm.com/infocenter/wbihelp/v6rxmx/index.jsp?topic=/com.ibm.wbia_adapters.doc/doc/healthcare/hl7mst34.htm">http://publib.boulder.ibm.com/infocenter/wbihelp/v6rxmx/index.jsp?topic=/com.ibm.wbia_adapters.doc/doc/healthcare/hl7mst34.htm</a> and <a href="http://www.hl-7.org/HL7-messages.asp">http://www.hl-7.org/HL7-messages.asp</a>.</p></td>
</tr>
<tr class="odd">
<td colspan="2">MDI</td>
<td colspan="3"><em>See</em> <a href="#Glos_MDI">Multiple Document Interface</a></td>
</tr>
<tr class="even">
<td colspan="2">Medical SAS Datasets</td>
<td colspan="3">The VHA Medical SAS Datasets are national administrative data for VHA-provided health care utilized primarily by veterans, but also by some non-veterans (e.g., employees, research participants).</td>
</tr>
<tr class="odd">
<td colspan="2">Message (HL7)</td>
<td colspan="3"><p>A <em>message</em> is the atomic unit of data transferred between systems. It is comprised of a group of segments in a defined sequence. Each message has a message type that defines its purpose. For example, the ADT (admissions/discharge/transfer) Message type is used to transmit portions of a patient's ADT data from one system to another. A three character code contained within each message identifies its type.</p>
<p><em>Source:</em> Health Level Seven, Health Level Seven, Version 2.3.1, copyright 1999, p. E-18., quoted in <strong>See CCR Redacted document</strong>.</p></td>
</tr>
<tr class="even">
<td colspan="2">Middleware</td>
<td colspan="3">In computing, middleware consists of software agents acting as an intermediary between different application components. It is used most often to support complex, distributed applications. The software agents involved may be one or many.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_MDI" class="anchor"></span>Multiple Document Interface (MDI)</td>
<td colspan="3"><p>MDI is a Windows function that allows an application to display and lets the user work with more than one document at the same time. This interface improves user performance by allowing them to see data coming from different documents, quickly copy data from one document to another and many other functions.</p>
<p>These files have the .MDI filename extension.</p></td>
</tr>
<tr class="even">
<td colspan="2">MUMPS</td>
<td colspan="3"><em>See</em> <a href="#Glos_M">M</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th colspan="2">Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_N" class="anchor"></span><strong>N</strong></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><span id="Glos_Namespace" class="anchor"></span>Namespace</td>
<td>A logical partition on a physical device that contains all the artifacts for a complete <a href="#Glos_M">M</a> system, including <a href="#Glos_Globals">globals</a>, <a href="#Glos_Routine">routines</a>, and libraries. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines. In VistA, namespaces are usually dedicated to a particular function. The <strong>ROR</strong> namespace, for example, is designed for use by <a href="#Glos_CCR">CCR</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><span id="Glos_NCR" class="anchor"></span>National Case Registry (NCR)</td>
<td>All sites running the CCR software transmit their data to the central database for the registry.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><span id="Glos_NPCD" class="anchor"></span>National Patient Care Database (NPCD)</td>
<td><p>The NPCD is the source data for the VHA Medical SAS Datasets. NPCD is the VHA's centralized relational database (a data warehouse) that receives encounter data from VHA clinical information systems. It is updated daily.</p>
<p>NPCD records include updated patient demographic information, the date and time of service, the practitioner(s) who provided the service, the location where the service was provided, diagnoses, and procedures. NPCD also holds information about patients' assigned Primary Care Provider and some patient status information such as exposure to Agent Orange, Ionizing Radiation or Environmental Contaminants, Military Sexual Trauma, and Global Assessment of Functioning.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">NPCD</td>
<td><em>See</em> <a href="#Glos_NPCD">National Patient Care Database</a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="4">to Glossary Contents</td>
</tr>
</tbody>
</table>

| Term or Acronym                                                                                        |                      |                                                                                                                                                                                                                                                                                                                                                    | Description |
|--------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| <span id="G_O" class="anchor"></span>O                                                             |                      |                                                                                                                                                                                                                                                                                                                                                    |             |
| <span id="Glos_OITFO" class="anchor"></span>Office of Information and Technology Field Office (OI&TFO) |                      | As directed by the Chief Information Officer (CIO), the Office of Information & Technology (OI&T) delivers available adaptable, secure and cost effective technology services to the Department of Veterans Affairs (VA) and acts as a steward for all VA's IT assets and resources. Field Offices are located at various sites around the nation. |             |
| OIFO                                                                                                   |                      | *See* [Office of Information and Technology Field Office](#Glos_OITFO)                                                                                                                                                                                                                                                                             |             |
| OI&TFO                                                                                                 |                      | *See* [Office of Information and Technology Field Office](#Glos_OITFO)                                                                                                                                                                                                                                                                             |             |
| [ BACK ](#_Toc228789362)                                                                           | to Glossary Contents |                                                                                                                                                                                                                                                                                                                                                    |             |

| Term or Acronym                                                   |                      |                                                                                                                                                                                                                                                                                                                                                                        | Description |
|-------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| <span id="G_P" class="anchor"></span>P                        |                      |                                                                                                                                                                                                                                                                                                                                                                        |             |
| <span id="Glos_Peginterferon" class="anchor"></span>peginterferon |                      | Peginterferon alfa-2b is made from human proteins that help the body fight viral infections. Peginterferon alfa-2b is used to treat chronic hepatitis C in adults, often in combination with another medication called [ribavirin](#Glos_Ribavirin).                                                                                                                   |             |
| <span id="Glos_Protocol" class="anchor"></span>Protocol           |                      | A protocol is a convention or standard that controls or enables the connection, communication, and data transfer between two computing endpoints. In its simplest form, a protocol can be defined as the rules governing the syntax, semantics, and synchronization of communication. Protocols may be implemented by hardware, software, or a combination of the two. |             |
| [ BACK ](#_Toc228789362)                                      | to Glossary Contents |                                                                                                                                                                                                                                                                                                                                                                        |             |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th>Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_R" class="anchor"></span><strong>R</strong></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Reflection</td>
<td colspan="2"><strong>Terminal emulation software</strong> used to connect personal computers to mainframe servers made by IBM, Hewlett Packard and other manufacturers running UNIX, VMS and other operating systems.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Registry</td>
<td colspan="2">The VHA Registries Program supports the population-specific data needs of the enterprise including (but not limited to) the <a href="#Glos_CCR">Clinical Case Registries</a>, Oncology Tumor Registry, Traumatic Brain Injury Registry, Embedded Fragment Registry and Eye Trauma Registry.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Registry Medication</td>
<td colspan="2">A defined list of medications used for a particular registry.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_RPC" class="anchor"></span>Remote Procedure Call (RPC)</td>
<td colspan="2"><p>A type of protocol that allows one program to request a service from a program located on another computer network. Using RPC, a system developer need not develop specific procedures for the server. The client program sends a message to the server with appropriate arguments and the server returns a message containing the results of the program executed. In this case, the GUI client uses an RPC to log the user on to <strong>VistA</strong>. And to call up, and make changes to, data that resides on a <strong>VistA</strong> server.</p>
<p><em>See also</em> <a href="#Glos_RPCBroker">Remote Procedure Call (RPC) Broker</a></p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_RPCBroker" class="anchor"></span>Remote Procedure Call (RPC) Broker</td>
<td colspan="2"><p>A piece of middleware software that allows programmers to make program calls from one computer to another, via a network. The RPC Broker establishes a common and consistent foundation for client/server applications being written under the VistA umbrella. The RPC Broker acts as a bridge connecting the client application front-end on the workstation (in this case, the Delphi Query Tool application) to the M –based data and business rules on the server. It serves as the communications medium for messaging between VistA client/server applications. Upon receipt, the message is decoded, the requested remote procedure call is activated, and the results are returned to the calling application. Thus, the RPC Broker helps bridge the gap between the traditionally proprietary VA software and other types of software.</p>
<p><em>See also</em> <a href="#Glos_RPC">Remote Procedure Call (RPC)</a></p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_retrovirus" class="anchor"></span>Retrovirus</td>
<td colspan="2">Any of a family of single-stranded RNA viruses having a helical envelope and containing an enzyme that allows for a reversal of genetic transcription, from RNA to DNA rather than the usual DNA to RNA, the newly transcribed viral DNA being incorporated into the host cell's DNA strand for the production of new RNA retroviruses: the family includes the AIDS virus and certain oncogene-carrying viruses implicated in various cancers.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_Ribavirin" class="anchor"></span>ribavirin</td>
<td colspan="2">Ribavirin is an antiviral medication. Ribavirin must be used together with an interferon alfa product (such as <a href="#Glos_Peginterferon">Peginterferon</a>)to treat chronic hepatitis C.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Roll-and-scroll, roll'n'scroll</td>
<td colspan="2">"Scrolling" is a display framing technique that allows the user to view a display as moving behind a fixed frame. The scrolling action typically causes the data displayed at one end of the screen to move across it, toward the opposite end. When the data reach the opposite edge of the screen they are removed (i.e., scroll off of the screen). Thus, old data are removed from one end while new data are added at the other. This creates the impression of the display page being on an unwinding scroll, with only a limited portion being visible at any time from the screen; i.e., the display screen is perceived as being stationary while the displayed material moves (scrolls) behind it. Displays may be scrolled in the top-bottom direction, the left-right direction, or both. Traditionally, VistA data displays have been referred to as "roll-and-scroll" for this reason.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">ROR</td>
<td colspan="2">The ROR <a href="#Glos_Namespace">namespace</a> in <a href="#Glos_M">M</a>, used for the CCR application and related <strong>VistA</strong> data files.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_Routine" class="anchor"></span>Routine</td>
<td colspan="2">A set of programming instructions designed to perform a specific limited task.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">RPC</td>
<td colspan="2"><em>See</em> <a href="#Glos_RPC">Remote Procedure Call (RPC)</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">RPC Broker</td>
<td colspan="2"><em>See</em> <a href="#Glos_RPCBroker">Remote Procedure Call Broker</a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="4">to Glossary Contents</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_S" class="anchor"></span><strong>S</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_508" class="anchor"></span>Section 508</td>
<td colspan="3"><p>Section 508 of the Rehabilitation Act as amended, <a href="http://frwebgate.access.gpo.gov/cgi-bin/getdoc.cgi?dbname=browse_usc&amp;docid=Cite:+29USC794d">29 U.S.C. Section 794(d)</a>, requires that when Federal agencies develop, procure, maintain, or use electronic and information technology, they shall ensure that this technology is accessible to people with disabilities. Agencies must ensure that this technology is accessible to employees and members of the public with disabilities to the extent it does not pose an "undue burden." Section 508 speaks to various means for disseminating information, including computers, software, and electronic office equipment.</p>
<p>The Clinical Case Registry must be 508 compliant, able to extract data as needed including <a href="#Glos_SNOMED">SNOMED</a> codes.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SecurityKeys" class="anchor"></span>Security Keys</td>
<td colspan="3">Codes which define the characteristic(s), authorization(s), or privilege(s) of a specific user or a defined group of users. The VistA option file refers to the security key as a "lock." Only those individuals assigned that "lock" can used a particular VistA option or perform a specific task that is associated with that security key/lock.</td>
</tr>
<tr class="even">
<td colspan="2">Selection Rules</td>
<td colspan="3">A pre-defined set of rules that define a registry patient.</td>
</tr>
<tr class="odd">
<td colspan="2">Sensitive Information</td>
<td colspan="3">Any information which requires a degree of protection and which should be made available only to authorized system users.</td>
</tr>
<tr class="even">
<td colspan="2">Server</td>
<td colspan="3">In information technology, a server is a computer system that provides services to other computing systems—called clients—over a network. The server is where VistA M-based data and Business Rules reside, making these resources available to the requesting server.</td>
</tr>
<tr class="odd">
<td colspan="2">SGML</td>
<td colspan="3"><em>See</em> <a href="#Glos_SGML">Standardized Generic Markup Language</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SSO" class="anchor"></span>Single Sign On (SSO)</td>
<td colspan="3">Single Sign On is the process that enables the secure access of disparate applications by a user through use of a single authenticated identifier and password.</td>
</tr>
<tr class="odd">
<td colspan="2">Site Configurable</td>
<td colspan="3">A term used to refer to features in the system that can be modified to meet the needs of each local site.</td>
</tr>
<tr class="even">
<td colspan="2">SNOMED</td>
<td colspan="3"><em>See</em> <a href="#Glos_SNOMED">Systematized Nomenclature of Medicine</a></td>
</tr>
<tr class="odd">
<td colspan="2">SQL</td>
<td colspan="3"><em>See</em> <a href="#Glos_SQL">Structured Query Language</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SGML" class="anchor"></span>Standardized Generic Markup Language (SGML)</td>
<td colspan="3">A generic markup language for representing documents. SGML is an International Standard that describes the relationship between a document's content and its structure. SGML allows document-based information to be shared and re-used across applications and computer platforms in an open, vendor-neutral format.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SQL" class="anchor"></span>Structured Query Language (SQL)</td>
<td colspan="3">An industry-standard language for creating, updating and, querying relational database management systems. SQL was developed by IBM in the 1970s for use in System R. It is the de facto standard as well as being an ISO and ANSI standard. It is often embedded in general purpose programming languages.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SNOMED" class="anchor"></span>Systematized Nomenclature of Medicine (SNOMED)</td>
<td colspan="3">SNOMED is a terminology that originated as the systematized nomenclature of pathology (SNOP) in the early 1960s under the guidance of the College of American Pathologists. In the late 1970s, the concept was expanded to include most medical domains and renamed SNOMED. The core content includes text files such as the concepts, descriptions, relationships, ICD-9 mappings, and history tables. SNOMED represents a terminological resource that can be implemented in software applications to represent clinically relevant information comprehensive (&gt;350,000 concepts) multi-disciplinary coverage but discipline neutral structured to support data entry, retrieval, maps etc.</td>
</tr>
<tr class="odd">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_T" class="anchor"></span><strong>T</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_TSPR" class="anchor"></span>Technical Services Project Repository (TSPR)</td>
<td colspan="3"><p>The TSPR is the central data repository and database for VA Health IT (VHIT) project information.</p>
<p><strong>See CCR Redacted document</strong>.</p></td>
</tr>
<tr class="odd">
<td colspan="2">Terminal emulation software</td>
<td colspan="3">A program that allows a personal computer (PC) to act like a (particular brand of) terminal. The PC thus appears as a terminal to the host computer and accepts the same escape sequences for functions such as cursor positioning and clearing the screen. Attachmate <em>Reflection</em> is widely used in VHA for this purpose.</td>
</tr>
<tr class="even">
<td colspan="2">Tool tips</td>
<td colspan="3">Tool tips are "hints" assigned to menu items which appear when the user "hovers" the mouse pointer over a menu.</td>
</tr>
<tr class="odd">
<td colspan="2">TSPR</td>
<td colspan="3"><em>See</em> <a href="#Glos_TSPR">Technical Services Project Repository</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_U" class="anchor"></span><strong>U</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_UpdateProcess" class="anchor"></span>Update Process</td>
<td colspan="3">With Patch 35 (ROR*1.5*35), patients are automatically confirmed into the regsitries. Prior to Patch 35, when patient records were first selected by the CCR, their status was marked as Pending. These patient records were identified via the automatic nightly registry update process and had to be validated before being confirmed in the registry.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_UI" class="anchor"></span>User Interface (UI)</td>
<td colspan="3"><p>A user interface is the means by which people (the users) interact with a particular machine, device, computer program or other complex tool (the system). The user interface provides one or more means of:</p>
<p>• Input, which allows the users to manipulate the system</p>
<p>• Output, which allows the system to produce the effects of the users' manipulation</p>
<p>The interface may be based strictly on text (as in the traditional "roll and scroll" IFCAP interface), or on both text and graphics.</p>
<p>In computer science and human-computer interaction, the user interface (of a computer program) refers to the graphical, textual and auditory information the program presents to the user, and the control sequences (such as keystrokes with the computer keyboard and movements of the computer mouse) the user employs to control the program.</p>
<p><em>See also</em> <a href="#Glos_GUI">Graphical User Interface</a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_V" class="anchor"></span><strong>V</strong></td>
</tr>
<tr class="even">
<td colspan="2">VERA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VERA">Veterans Equitable Resource Allocation</a></td>
</tr>
<tr class="odd">
<td colspan="2">Vergence</td>
<td colspan="3"><em>Vergence</em>® software from Sentillion provides a single, secure, efficient and safe point of access throughout the healthcare enterprise, for all types of caregivers and applications. <em>Vergence</em> unifies single sign-on, role-based application access, context management, strong authentication and centralized auditing capabilities into one fully integrated, out-of-the box clinical workstation solution.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VerifyCode" class="anchor"></span>Verify Code</td>
<td colspan="3"><p>With each sign-on to VistA, the user must enter two codes to be recognized and allowed to proceed: the <em>Access Code</em> and <em>Verify Code</em>. Like the Access Code, the Verify Code is also generally assigned by IRM Service and is also encrypted. This code is used by the computer to verify that the person entering the access code can also enter a second code correctly. Thus, this code is used to determine if users can verify who they are.</p>
<p><em>See also</em> <a href="#Glos_AccessCode">Access Code</a></p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VERA" class="anchor"></span>Veterans Equitable Resource Allocation (VERA)</td>
<td colspan="3"><p>Since 1997, the VERA System has served as the basis for allocating the congressionally appropriated medical care budget of the Department of Veterans Affairs (VA) to its regional networks. A 2001 study by the RAND Corporation showed that "[in] spite of its possible shortcomings, VERA appeared to be designed to meet its objectives more closely than did previous VA budget allocation systems."</p>
<p><em>See</em> <a href="http://www.rand.org/pubs/monograph_reports/MR1419/">http://www.rand.org/pubs/monograph_reports/MR1419/</a></p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VistA" class="anchor"></span>Veterans Health Information Systems and Technology Architecture (VistA)</td>
<td colspan="3"><p>VistA is a comprehensive, integrated health care information system composed of numerous software modules.</p>
<p>.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VHA" class="anchor"></span>Veterans Health Administration (VHA)</td>
<td colspan="3">VHA administers the United States Veterans Healthcare System, whose mission is to serve the needs of America's veterans by providing primary care, specialized care, and related medical and social support services.</td>
</tr>
<tr class="even">
<td colspan="2">VHA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VHA">Veterans Health Administration</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VISN" class="anchor"></span>Veterans Integrated Service Network (VISN)</td>
<td colspan="3"><a href="#Glos_VHA">VHA</a> organizes its local facilities into networks called VISNS (VA Integrated Service Networks). At the VISN level, VistA data from multiple local facilities may be combined into a data warehouse.</td>
</tr>
<tr class="even">
<td colspan="2">VISN</td>
<td colspan="3"><em>See</em> <a href="#Glos_VISN">Veterans Integrated Service Network</a></td>
</tr>
<tr class="odd">
<td colspan="2">VistA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VistA">Veterans Health Information Systems and Technology Architecture</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc228789362"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

| Term or Acronym                            |                      |                                                | Description |
|--------------------------------------------|----------------------|------------------------------------------------|-------------|
| <span id="G_X" class="anchor"></span>X |                      |                                                |             |
| XML                                        |                      | *See* [Extensible Mark-up Language](#Glos_XML) |             |
| [ BACK ](#_Toc228789362)               | to Glossary Contents |                                                |             |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

!
!KEA, 6
A
CCR, 40
accessibility features, 40
acronym
CCR, 4
ADMIN security key, 104
adverse events
trends, 6
application
CCR, 3
C
CCR
acronym, 4
application, 3
archiving, 83
data access, 6
data collection automation, 6
downloading software, 39
emulation software, 6
features of, 5
graphical user interface, 6
GUI, 6
*Installation & Implementation Guide*, 4
intranet Home Page, 40
key features, 6
Maintenance menu, 41
national database, 5
navigation, 6
overview of, 5, 211
purginging, 83
*Release Notes*, 4
selection rules, 5
semiautomatic sign-on, 6
single sign-on, 6
software, 3
*User Manual*, 4
version 1.5, 5
CDCO, 5
codes
ICD-9, 5
conventions
typographical, 2
Corporate Data Center Operations, 5
Cross Reference Report, 79
D
dashed underlining, 2
data
automatic transmission, 6
clinical, 4
demographic, 4
Hepatitis C, 5
HIV, 5
Human Immunodeficiency Virus, 5
stored in local VistA system, 5
data collection automation, 6
documentation
in VistA Document Library, 40
sources, 39
documents
related, 4
downloading CCR software, 39
DPGM MOVEMENT EVENT, 84
E
event protocol
DPGM MOVEMENT EVENT, 84
ROR DATA EVENT0, 84
ROR-EVENT-LAB, 84
ROR-EVENT-PTF, 84
ROR-EVENT-VISIT, 84
exported options, 80
F
Features of CCR, 211
file
ROR LOG file (#798.7), 83
ROR PATIENT EVENTS file (#798.3), 83
ROR task file (#798.8), 83
ROR-PATIENT-EVENTS (798.3), 84
files
admissions, 4
diagnoses, 4
laboratory tests, 4
patient demographics, 4
prescriptions, 4
radiology exams, 4
surgical procedures, 4
visits, 4
VistA, 4
fonts, 2
G
graphical user interface, 4
green text, 2
GUI, 4
H
HCCR. *See* CCR:HEPC
Hepatitis C Registry. See CCR:HEPC
Historical Data Extraction
Create the Output Directory, 49
Historical Data Extraction menu
Create Data Extraction Task option, 50
Define Output Directory Name option, 50
Start a Task option, 50
Task Information, 51
Status values, 52
HIV Registry. See CCR:HIV
HL7, 5
HL7 protocol
ROR-SITE-DRIVER, 84
ROR-SITE-SUBSCRIBER, 84
I
ICD-9 codes, 5
icon
history, 3
note, 2
tip, 2
warning, 2
icons, 2
ICR. *See* CCR:HIV, *See* CCR:HIV
*Installation & Implementation Guide*, 4
IRM
security key, 104
K
key features, 6
keyboard
shortcuts, 40
keyboard keys, 2
keys
keyboard, 2
KIDS Build
Global ^ROR, 69
Global ^RORDATA, 69
L
LAB^ROREVT01, 84
lists
local patients, 6
patients with evidence of HEPC, 6
patients with evidence of HIV, 6
local patient lists, 6
local reports, 6
M
Maintenance menu, 41
ACL option, 41
Edit Lab Search Criteria option, 41, 42
Edit Registry Parameters option, 41, 43
ELS option, 41
ERP option, 41
HDE option, 41
Historical Data Extraction menu, 48
Historical Data Extraction option, 41, 45, 48
Pending Patients option, 41, 47
PLF option, 41
PP option, 41
Print Log Files option, 41, 46
Re-Index the ACL cross-reference option, 41
menu
EVE, 80
Menu Management, 80
Systems Manager Menu, 80
XUMAINT, 80
messages
multiple, 6
monitoring
patient outcome measures, 6
process measures, 6
quality of care, 6
trends, 6
multiple messages, 6
N
names
documents, 2
field, 2
GUI buttons, 2
GUI command icons, 2
GUI panels, 2
GUI panes, 2
GUI tabs, 2
patches, 2
registry, 2
reports, 2
software applications, 2
standards, 2
Namespaces
Sub Namespaces, 78
National Case Registry, 4
national CCCR database, 5
nightly background process, 5
O
observation/result, 147
option
Abbreviated Menu Diagrams, 80
Broker Context, 80
Clinical Case Registries Maintenance, 82
Create Extraction Tasks, 81
Diagram Menus, 80
Display Extraction Status, 81
Display Task Log, 81
Edit \[ Extraction Tasks\], 81
Edit data extraction, 81
Edit Lab Search Criteria, 82
Edit Task Description, 81
Historical Data Extraction, 81
ICR Version Comparison Report, 82
List of Pending Errors, 82
Option Function Inquiry, 80
Pending Patients, 82
Print Log Files, 82
Registry Setup, 80
Registry Update & Data Extraction, 80
Re-index the ACL cross reference, 82
ROR GUI, 80
ROR SETUP, 80
ROR TASK, 80
RORHDT CREATE, 81
RORHDT EDIT, 81
RORHDT EDIT EXTRACTION, 81
RORHDT EDIT TASK, 81
RORHDT LOG, 81
RORHDT MAIN, 81
RORHDT START, 81
RORHDT STATUS, 81
RORHDT STOP, 81
RORICR VERSION COMPARISON, 82
RORMNT ACL REINDEX, 82
RORMNT EDIT LAB SEARCH, 82
RORMNT MAIN, 82
RORMNT PENDING ERRORS LIST, 82
RORMNT PENDING PATIENTS, 82
RORMNT PRINT LOGS, 82
Start a Task, 81
Stop a Task, 81
Systems Menu Diagrams (with Entry/Exit Actions, 80
XUINQUIRE, 80
XUUSERACC, 80
XUUSERACC1, 80
XUUSERACC2, 80
options
exported, 80
outcomes
tracking, 6
P
patches
ROR\*1.5 series, 7
patient outcomes
tracking, 6
process
data transmission, 5
nightly background, 5
protocol
DPGM MOVEMENT EVENT, 84
ROR-EVENT-LAB, 84
ROR-EVENT-PTF, 84
ROR-EVENT-VISIT, 84
ROR-SITE-DRIVER, 84
ROR-SITE-SUBSCRIBER, 84
Q
quality of care, 6
R
Reflection, 6
registries, 3
registry
HEPC, 4
HIV, 4
related documents, 4
*Release Notes*, 4
reports
administrative, 4
administrative data, 6
clinical, 4
clinical data, 6
local, 6
robust capabilities, 6
VA Cross Reference, 79
ROR LOG file (#798.7), 83
ROR PATIENT EVENTS file (#798.3), 83
ROR TASK file (#798.8), 83
ROR\*1.5 series patches, 7
ROR-EVENT-LAB, 84
ROR-EVENT-PTF, 84
ROR-EVENT-VISIT, 84
RORMNT MAIN, 41
ROR-PATIENT-EVENTS (798.3), 84
ROR-SITE-DRIVER, 84
ROR-SITE-SUBSCRIBER, 84
routine
LAB^ROREVT01, 84
PTF^ROREVT0 1, 84
Routines
Sub Namespaces, 78
XINDEX, 79
S
screen display
\<RET\>, 3
bold type, 3
user response, 3
selection rules, 5
shortcuts
keyboard, 40
software
CCR, 3
customize, 41
decommissioned, 7
distribution, 39
files, 39
Hepatitis C Case Registry v1.0, 7
Immunology Case Registry v2.1, 7
maintain, 41
sources, 39
sources
software and documentation, 39
Sub Namespaces, 78
symbols, 2
T
task parameter
ROR SETUP, 80
RORFLCLR, 80
RORMNTSK, 80
RORSUSP, 81
time on therapy
trends, 6
tracking
clinical, 3
tracking patient outcomes, 6
tracking trends, 6
training
hyperlinks, 40
information, 40
VistA University, 40
VistAU, 40
treatment response trends, 6
trend monitoring, 6
trends
adverse events, 6
time on therapy, 6
tracking, 6
treatment response, 6
typefaces, 2
typographical conventions, 2
U
user interface
graphical, 4
*User Manual*, 4
user response, 3
{bracketed information}, 3
question marks, 3
Return/Enter key, 3
USER security key, 104
users
Information Resource Management, 4
IRM, 4
V
VA Cross Reference Report, 79
variable
clear
RORFLCLR, 80
set
RORFLSET, 80
[^1]: CDCO was formerly known as the Austin Automation Center (AAC). CDCO is managed by the VHA Center for Quality Management in Public Health (CQMPH).
[^2]: added code changes/fixes for Section 508 compliance. Reference Clinical Case Registry Interim Test Report 10209 March 13 2013.
[^3]: Document revision for Patch ROR\*1.5\*10, January 2010, added/expanded many definitions and much explanatory material.
