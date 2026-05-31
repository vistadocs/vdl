---
title: DATUP Version 4.0.1 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: null
app_code: PRED
app_name: 'Pharmacy: Pharmacy Data Update (DATUP)'
section: GUI
app_status: active
pkg_ns: PRED
patch_ver: 4.0.1
patch_id: PRED*4.0.1
group_key: PRED:PRED:4.0.1
file_numbers: []
security_keys: []
menu_options: 0
description: These release notes cover the changes to DATUP version (v) 4.0.1 First Databank (FDB) Framework (Fwk) Upgrade v4.5 for this release.
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 886
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: July 2024
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/PRED_4_0_P2_RN.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/PRED_4_0_P2_RN.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=203
audit_applied: '2026-05-31'
master_source: DATUP Version 4.0.1 Release Notes
master_pub_date: July 2024
consolidated_from: 5 versions
prior_versions:
- DATUP Version 2 Release Notes
- DATUP Version 3.0.01 Release Notes
- DATUP Version 3 Release Notes
- PRED*4*3 DATUP Version 4.0.3 Release Notes
consolidated_title: datup release notes
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
  <span id="_Toc205632711" class="anchor"></span>Data Update (DATUP) 4.0.1
  PRED\*4\*2
  Release Notes
---
![](datup-version-4-0-1-release-notes/001.png)
July 2024
Department of Veterans Affairs (VA)
Office of Information and Technology (OIT)
Table of Contents

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy Reengineering (PRE) Project provided innovative enhancements to Clinical Decision Support (CDS) within the Veterans Health Administration (VHA). Medication order checks are accomplished through the synergistic functionality of multiple applications, including Medication Order Check Healthcare Application (MOCHA), Pharmacy Product System-National (PPS-N), Pharmacy Enterprise Customization System (PECS), and Data Update (DATUP).

DATUP is a utility that runs an automated process to maintain the First Databank Drug Information Framework (commonly abbreviated as FDB-DIF) and VA custom data used by regional MOCHA instances and at the national level by PPS-N.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to DATUP version (v) 4.0.1 First Databank (FDB) Framework (Fwk) Upgrade v4.5 for this release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of DATUP FDB Fwk Upgrade v4.5 and applies to the changes made between this release and any previous release for this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issue for FDB Fwk Upgrade v4.5 DATUP 4.0.1 / PRED\*4\*2.

### New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable (N/A) to the FDB Fwk Upgrade v4.5 DATUP 4.0.1 / PRED\*4\*2 release.

### Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHA, Patient Care Services, and Pharmacy Benefits Management (PBM) has requested the FDB Fwk upgrade from version 3.3 to version 4.5 for VA Pharmacy applications. DATUP will be upgrading the Application Programming Interface (API) calls in support of the FDB Fwk version 4.5 upgrade.

The following are the enhancements and modifications to the FDB Fwk Upgrade v4.5 DATUP 4.0.1 / PRED\*4\*2 release

- FDB Fwk version 4.5 Application Programming Interfaces (APIs) to be integrated into the DATUP application
- Modifications to methods and code-flow to be in compliance with FDB v4.5 constructs
- FDB-6309 - DATUP: File naming issue - 4.5 custom update files have null in the file name after being processed and placed in the droid/custom folder
- FDB-6309 - DATUP: File naming issue - 4.5 custom update files have null in the file name after being processed and placed in the droid/custom folder
- FDB-7912 - PECS/DATUP/MOCHA: (Step 1) Validate DRC dose unit customizations
- FDB-7756 - DATUP: Null pointer exception thrown by FDB v4.5.11.2 DDI Screening API as part of DATUP's validation during update file loads
- FDB-7756 - DATUP: Null pointer exception thrown by FDB v4.5.11.2 DDI Screening API as part of DATUP's validation during update file loads
- FDB-7755 - DATUP: Upgrade to use FDB v4.5.13.1 and latest version of mocha common jar following MOCHA upgrade to FDB v4.5.13.1
- FDB-7651 - PECS/DATUP/MOCHA: (Step 1) Validate DRC rate field customizations
- FDB-8112 - DATUP/PPS-N: Create cron script for file processing and validate in PPS-N lower environments
- FDB-7713 - DATUP: Integrate and validate sustainment build PRED\*3\*6
- FDB-8247 - PECS/DATUP/MOCHA: Update Jenkinsfile to refer to targetBranch following upgrade of GitForensics plugin and removal of defaultBranch naming
- FDB-7800 - DATUP/PECS: Load FDB v4.5 standard update files into SQA environment to correct misspelling of capusles/kilogram/day dose unit
- FDB-8337 - DATUP: Improve handling of DB connections to mitigate connection pool exceptions
- FDB-6756 - PECS/DATUP/MOCHA: (Step 1) Low and high frequency customizations
- FDB-8297 - DATUP: Update log4j2.xml application logging configuration to retain only last 10 files and ensure appropriate log levels are used when writing to logs to omit extraneous information

### Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There were no known defects at the time that this document was written.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation describing the new functionality introduced by this patch is available. Upon National Release, the documentation will be in the form of Adobe Acrobat files. Documentation will be found on the VA Software Documentation Library at:

<https://www.va.gov/vdl/application.asp?appid=203>

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
<td><p>PRED_4_0_P2_RN.DOCX</p>
<p>PRED_4_0_P2_RN.PDF</p></td>
<td>DATUP 4.0.1 PRED*4*2 Release Notes</td>
<td>Binary</td>
</tr>
<tr class="even">
<td><p>PRED_4_0_P2_DIBR.DOCX</p>
<p>PRED_4_0_P2_DIBR.PDF</p></td>
<td>DATUP 4.0.1 PRED*4*2 Deployment, Installation, Back-Out, Rollback Guide</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td><p>PRED_4_0_P2_IG.DOCX</p>
<p>PRED_4_0_P2_IG.PDF</p></td>
<td>DATUP 4.0.1 PRED*4*2 Installation Guide</td>
<td>Binary</td>
</tr>
</tbody>
</table>

Table of PSO\*7\*467 Release DocumentationTable includes file description, file name, and FTP mode

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DATUP Version 2 Release Notes

## Functional Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Update Files:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Copies the image files included in the First Databank Incremental Update files to the file system so that PPS-N can display those images.

## Architectural Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DATUP updated from FDB-DIF 3.2 to FDB-DIF 3.3 API and Schema

2.  Data Update (DATUP) v2.0 June 2014 Release Notes
