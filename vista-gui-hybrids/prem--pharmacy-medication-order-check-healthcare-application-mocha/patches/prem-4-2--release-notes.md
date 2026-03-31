---
title: PREM*4*2 MOCHA Server Version Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: MOCHA Server Version
app_code: PREM
app_name: "Pharmacy: Medication Order Check Healthcare Application (MOCHA)"
section: GUI
app_status: active
pkg_ns: PREM
patch_ver: 4
patch_id: PREM*4*2
group_key: "PREM:PREM:4"
file_numbers: []
security_keys: []
menu_options: 0
description: These release notes cover the changes to MOCHA version (v) 4.0.2 First Databank (FDB) Framework (Fwk) Upgrade v4.5 for this release.
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - mocha
  - table
  - contents
  - prem
  - release
  - upgrade
  - version
  - application
  - documentation
  - order
page_count: 0
word_count: 1034
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Medication_Order_Check_HC_Applic/PREM_4_0_P2_RN.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Medication_Order_Check_HC_Applic/PREM_4_0_P2_RN.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=201"
---

## Table of Contents

  - [## Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [This Release](#this-release)
    - [New Features and Functions Added](#new-features-and-functions-added)
    - [Enhancements and Modifications to Existing](#enhancements-and-modifications-to-existing)
  - [Known Issues](#known-issues)
  - [Product Documentation](#product-documentation)
---
title: |
  <span id="_Toc205632711" class="anchor"></span>Medication Order Check Healthcare Application (MOCHA) 4.0.2
  PREM\*4\*2
  Release Notes
---
![](prem-4-2-mocha-server-version-release-notes/001.png)
May 2025
Office of Information and Technology (OIT)
Table of Contents

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The First Databank (FDB) Framework (Fwk) Upgrade Project provided innovative enhancements to Clinical Decision Support (CDS) within the Veterans Health Administration (VHA). Medication order checks are accomplished through the synergistic functionality of multiple applications, including Medication Order Check Healthcare Application (MOCHA), Pharmacy Product System-National (PPS-N), and Data Update (DATUP).

MOCHA Server is a Java Enterprise Edition (JEE) application, used by the MOCHA Veterans Health Information Systems and Technology Architecture (VistA) Pharmacy Application to perform enhanced order checks using the FDB MedKnowledge Framework. MOCHA Server is a VA-built custom web application; it is not a legacy or commercial off the shelf (COTS) application or an Enterprise Shared Service (ESS). FDB MedKnowledge Framework is a drug data product that provides the latest identification and safety information on medications, along with the latest algorithms used to perform order checks.

The following patches are included in the FDB Fwk v4.5 Upgrade: DATUP (PRED\*4\*1, PRED\*4\*2, and PRED\*4\*3), MOCHA (PREM\*4\*1 and PREM\*4\*2), PPS-N (PREN\*4\*1), PECS (PREC\*7\*1), and VistA (PSS\*1\*254, PSJ\*5\*423, and PSO\*7\*779).

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to MOCHA version (v) 4.0.2 First Databank (FDB) Framework (Fwk) Upgrade v4.5 for this release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of MOCHA FDB Fwk Upgrade v4.5 and applies to the changes made between this release and any previous release for this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issue for MOCHA 4.0.2 / FDB Fwk Upgrade v4.5 PREM\*4\*2.

### New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable (N/A) to the FDB Fwk Upgrade v4.5 MOCHA 4.0.2 / PREM\*4\*2 release.

### Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHA, Patient Care Services, and Pharmacy Benefits Management (PBM) has requested the FDB Fwk upgrade from version 3.3 to version 4.5 for VA Pharmacy applications. MOCHA Server will be upgrading the Application Programming Interface calls in support of the FDB Fwk version 4.5 upgrade.

The following are the enhancements and modifications to the FDB Fwk Upgrade version 4.5 MOCHA 4.0.2 / PREM\*4\*2 release.

- FDB Fwk v4.5 Application Programming Interfaces (APIs) to be integrated into the MOCHA application. The vendor documentation has the behavioral and content differences between version 3.3 and 4.5
- FDB-7651 - PECS/DATUP/MOCHA: (Step 1) Validate DRC rate field customizations
- FDB-7025 - VistA/MOCHA: Max Daily in General Dosing Range messages
- FDB-8143 - VistA/MOCHA: PSS Drug Dosing Lookup does not return customized dose units
- FDB-8158 - MOCHA: Upgrade build to use FDB v4.5.14.1 - MISC
- FDB-8172 - MOCHA/VistA: Order Check resulting in Invalid Order message for continuous routes
- FDB-6593 - MOCHA/VistA: Update source element returned in drug-drug check response so can distinguish between VA custom and FDB standard DDI records
- FDB-8247 - PECS/DATUP/MOCHA: Update Jenkinsfile to refer to targetBranch following upgrade of GitForensics plugin and removal of defaultBranch naming
- FDB-8171 - MOCHA: Update XSD file to accommodate new database values for dose route, type, and unit. Remove unnecessary properties files
- FDB-8339 - MOCHA: Improve handling of DB connections to mitigate connection pool exceptions
- FDB-6756 - PECS/DATUP/MOCHA: (Step 1) Low and high frequency customizations
- FDB-8489 - MOCHA: Upgrade build to use FDB v4.5.14.1 - MISC
- FDB-8021- MOCHA/DATUP/PECS: Integrate and validate sustainment build PREM\*3\*6 for MOCHA and then rebuild DATUP and PECS with updated MOCHA common jar
- FDB-8348 - PECS/DATUP/MOCHA: (Step 1) Upgrade and validate Professional Monograph customizations
- FDB-8610 - MOCHA: Dose unit conversion error returned when performing order check with specific dose units
- FDB-8300 - MOCHA: Update log4j2.xml application logging configuration to retain only last 10 files and ensure appropriate log levels are used when writing to logs to omit extraneous information
- FDB-8974 - MOCHA: Upgrade to new FDB v4.5.15.1 API that fixes UOM conversion issue due to mixed case
- FDB-9095 - MOCHA/VistA/CPRS: FDB Fwk v4.5 Pre-Prod IOC Issue tracker#15 - Form based failed with unable to convert ML to MG message
- FDB-9097 - MOCHA/VistA/CPRS: FDB Fwk v4.5 Pre-Prod IOC Issue tracker#16 - Customized dose unit not working for gcnseq 6330

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- In version 3.3, the dose units are in all uppercase. Version 4.5 the dose units are lowercase. There is no current workaround for this issue.
- In version 3.3, the decimal precision is three decimal places. Version 4.5, the decimal precision is five decimal places. There is no current workaround for this issue.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation describing the new functionality introduced by this patch is available. Upon National Release, the documentation will be in the form of Adobe Acrobat files. Documentation will be found on the VA Software Documentation Library at:

<https://www.va.gov/vdl/application.asp?appid=201>

<table>
<caption>Table of PSO*7*467 Release DocumentationTable includes file description, file name, and FTP mode</caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 44%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Title</strong></th>
<th><strong>FTP Mode</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PREM_4_0_P2_RN.DOCX</p>
<p>PREM_4_0_P2_RN.PDF</p></td>
<td>MOCHA 4.0.2 PREM*4*2 Release Notes</td>
<td>Binary</td>
</tr>
<tr class="even">
<td><p>PREM_4_0_P2_DIBR.DOCX</p>
<p>PREM_4_0_P2_DIBR.PDF</p></td>
<td>MOCHA 4.0.2 PREM*4*2 Deployment, Installation, Back-Out, Rollback Guide</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td><p>PREM_4_0_P2_IG.DOCX</p>
<p>PREM_4_0_P2_IG.PDF</p></td>
<td>MOCHA 4.0.2 PREM*4*2 Installation Guide</td>
<td>Binary</td>
</tr>
</tbody>
</table>

Table of PSO\*7\*467 Release DocumentationTable includes file description, file name, and FTP mode