---
title: Surgery Risk Assessment SRA*3.0*9 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: SRA
app_name: Surgery Risk Assessment
section: CLI
app_status: active
pkg_ns: SRA
patch_ver: 3.0
patch_id: SRA*3.0*9
group_key: "SRA:SRA:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: These release notes cover the changes to the VistA Surgery Risk Assessment (SRA) package for this release.
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - donor
  - surgery
  - risk
  - assessment
  - table
  - contents
  - disposition
  - vessel
  - span
  - cardiac
page_count: 0
word_count: 1110
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Risk_Assessment_(SRA)/SRA_3_P9_RN.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Risk_Assessment_(SRA)/SRA_3_P9_RN.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=437"
---

## Table of Contents

  - [## Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [Patch Information](#patch-information)
    - [DONOR VESSEL DISPOSITION Field Update](#donor-vessel-disposition-field-update)
    - [TRANSMISSION LAYOUTS File Data Update](#transmission-layouts-file-data-update)
    - [SRATSRV4 Routine Update](#sratsrv4-routine-update)
    - [Additional Documentation Updates](#additional-documentation-updates)
    - [New Routines](#new-routines)
---
title: |
  <span id="_Toc205632711" class="anchor"></span>VistA Surgery Risk Assessment
  SRA\*3.0\*9
  Release Notes
---
![](surgery-risk-assessment-sra-3-0-9-release-notes/001.png)
June 2024
Table of Contents

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The Surgery Risk Assessment (SRA) package is only installed on the Surgery Risk Assessment Database and is not intended to be installed at medical centers.

This enhancement to the VistA Surgery Risk Assessment package:

> 1\. Adds ‘NA’ FOR NOT APPLICABLE to the SET OF CODES for the DONOR VESSEL DISPOSITION field (#234) in the SURGERY RISK ASSESSMENT file (#139).

> 2\. Updates data in the STARTING LOCATION (#3) and ENDING LOCATION (#4) sub-fields in the FIELD NUMBER multiple (#139.42) within the TRANSMISSION LAYOUTS file (#139.4) to accommodate the new 2-character code for DONOR VESSEL DISPOSITION in NON-CARDIAC line 14 transmissions and to ensure proper parsing and filing.

> 3\. Modifies the SRATSRV4 routine to ensure proper filing of all positions following DONOR VESSEL DISPOSITION in NON-CARDIAC line 14 transmissions.

> 4\. Updates the SRA User and/or Technical Manuals to document the access required to add new Risk Assessment Download Schedule entries, the modifications to the Check for Risk Assessment Transmission Errors option \[SRAFERR\] introduced in SRA\*3.0\*10, and the modification to the SERVER DEVICE field (#227) in the OPTION file (#19) entry for SRATSRV after installation of SRA\*3.0\*0. These documentation updates are in addition to the documentation updates for the other changes in this patch.

This is a companion patch for SR\*3.0\*205 to accommodate the changes to surgery risk assessment transmissions and is required to be installed on the Surgery Risk Assessment Database prior to SR\*3.0\*205 at medical centers.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to the VistA Surgery Risk Assessment (SRA) package for this release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the VistA Surgery Risk Assessment package and applies to the changes made between this release and any previous release for this software.

## Patch Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### DONOR VESSEL DISPOSITION Field Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds ‘NA’ FOR NOT APPLICABLE to the SET OF CODES for the DONOR VESSEL DISPOSITION field (#234) in the SURGERY RISK ASSESSMENT file (#139). This is the first 2-character code for this field.

STANDARD DATA DICTIONARY \#139 -- SURGERY RISK ASSESSMENT FILE 6/11/24 PAGE 1

STORED IN ^SRA( (### ENTRIES) SITE: FOURWORD UCI: XXX,XXX (VERSION 3.0)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

139,234 DONOR VESSEL DISPOSITION 184;30 SET (audited)

Donor Vessel Disposition if not used

'N' FOR NO DONOR VESSELS RECEIVED;

'D' FOR DISCARDED;

'R' FOR RETURNED TO OPO;

'S' FOR STORED;

<span class="mark">'NA' FOR NOT APPLICABLE;</span>

LAST EDITED: MAR 02, 2023

HELP-PROMPT: Enter disposition of donor vessels.

DESCRIPTION:

Document disposition of donor vessels.

AUDIT: YES, ALWAYS

The DONOR VESSEL DISPOSITION field (#234) is transmitted to the Surgery Risk Assessment Database for Non-Cardiac & Cardiac Transplant surgery cases.

### TRANSMISSION LAYOUTS File Data Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment Database receives transmissions for 1-Liner, Non-Cardiac & Cardiac surgery cases. Non-Cardiac and 1-Liner transmission data is parsed & filed into the SURGERY RISK ASSESSMENT file (#139) on the Surgery Risk Assessment Database. Note: Cardiac transmission data is sent as a read-only message and captured using a different process by the National Surgery Office and is not sent through the processing routine. The DONOR VESSEL DISPOSITION field (#234) is not transmitted for 1-Liner surgery cases.

This patch accommodates for the proper parsing & filing of DONOR VESSEL DISPOSITION’s new 2-character ‘NA’ code (which is sent on line 14 in NON-CARDIAC transmissions) to the Surgery Risk Assessment Database by incrementing the DONOR VESSEL DISPOSITION (#234) field's ending position by one (from 75-75 to 75-76). This patch also increments the starting & ending positions by one for each of the 4 fields that follow DONOR VESSEL DISPOSITION on NON-CARDIAC: line 14:

- SURGEON VERIFYING UNET (#625) (from 76-105 to 77-106)
- SURGEON VER ORGAN PRE-ANES (#628) (from 106-135 to 107-136)
- SURGEON VER DONOR ORG PRE-ANES (#629) (from 136-165 to 137-166)
- SURGEON VER ORG PRE-TRANSPLANT (#632) (from 166-195 to 167-196)

Example: Print SRA Transmission Message Format for NON-CARDIAC: line 14

NON-CARDIAC: line 14

Position Field Name (field,file)

============================================================

15-21 ORGAN TO BE TRANSPLANTED (134,139)

22-31 UNOS NUMBER (137,139)

32-33 DONOR SEROLOGY HCV (154,139)

34-35 DONOR SEROLOGY HBV (186,139)

36-37 DONOR SEROLOGY CMV (199,139)

38-39 DONOR SEROLOGY HIV (205,139)

40-40 DONOR ABO TYPE (214,139)

41-41 RECIPIENT ABO TYPE (215,139)

42-42 BLOOD BANK ABO VERIFICATION (220,139)

43-54 D/T BLOOD BANK ABO VERIF (640,139)

55-55 OR ABO VERIFICATION (222,139)

56-67 D/T OR ABO VERIF (624,139)

68-68 UNET VERIF BY SURGEON (626,139)

69-69 ORGAN VER PRE-ANESTHESIA (627,139)

70-71 DONOR ORG VER PRE-ANES (630,139)

72-73 ORGAN VER PRE-TRANSPLANT (631,139)

74-74 DONOR VESSEL USAGE (233,139)

<span class="mark">75-76 DONOR VESSEL DISPOSITION (234,139)</span> \<-- end moved to 76<span class="mark">77-106 SURGEON VERIFYING UNET (625,139)</span> \<-- modified<span class="mark">107-136 SURGEON VER ORGAN PRE-ANES (628,139)</span> \<-- modified<span class="mark">137-166 SURGEON VER DONOR ORG PRE-ANES (629,139)</span> \<-- modified<span class="mark">167-196 SURGEON VER ORG PRE-TRANSPLANT (632,139)</span> \<-- modified

These increments to the starting & ending positions of the aforementioned fields are made via a data update in the STARTING LOCATION (#3) and ENDING LOCATION (#4) sub-fields in the FIELD NUMBER multiple (#139.42) within the TRANSMISSION LAYOUTS file (#139.4).

### SRATSRV4 Routine Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch updates the SRATSRV4 routine to accommodate for the possibility of up to 2 characters being transmitted in the DONOR VESSEL DISPOSITION field (#234) to the Surgery Risk Assessment Database for Non-Cardiac transplant surgery cases.

SRATSRV4 has data extracts that have been modified to ensure proper parsing and filing of the new 2-character code “NA” for NOT APPLICABLE to the DONOR VESSEL DISPOSITION field (#234) into the SURGERY RISK ASSESSMENT file (#139) for NON-CARDIAC: line 14 transmissions.

### Additional Documentation Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the SRA\*3.0\*9 Technical Manual, additional updates have been made to document:

- the SERVER DEVICE field (#227) in the OPTION file (#19) entry for SRATSRV should be set to “SRA” after the SRA\*3.0\*0 patch is installed
- FileMan Access Code “@” is required to add a new entry using the Risk Assessment Download Schedule (Enter/Edit) option \[SRA DOWNLOAD EDIT\]

In the SRA\*3.0\*9 User Manual, additional updates have been made to document:

- FileMan Access Code “@” is required to add a new entry using the Risk Assessment Download Schedule (Enter/Edit) option \[SRA DOWNLOAD EDIT\]
- the Check for Risk Assessment Transmission Errors option \[SRAFERR\] purges assessments older than three years (a code change made in SRA\*3.0\*10)

### New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### SRAENV9 (Environment Check Routine)

New routine SRAENV9 has been created to ensure that the patch is only installed on the Surgery Risk Assessment Database.

Upon loading the PackMan message, SRAENV9 runs to check for the Surgery Risk Assessment Database. If it detects that the patch is loading at a VA medical center, the load is aborted.

#### SRA39PO (Post-Install Routine)

New routine SRA39PO has been created to store pre-existing values for the sub-fields that are updated in the TRANSMISSION LAYOUTS file (#139.4) into an XTMP backup global, ^XTMP(“SRA39RR”).

The pre-existing values are stored in ^XTMP(“SRA39RR”) for 120 days before being purged automatically by the system.

#### SRA39RR (Restore Routine)

New routine SRA39RR has been created to restore pre-existing data values if data rollback is required.

To restore the pre-existing values from the XTMP backup global, run the RESTORE component of SRA39RR (RESTORE^SRA39RR) in a programmer prompt. This will retrieve the pre-existing values from the ^XTMP(“SRA39RR”) and re-apply them to the sub-fields in the TRANSMISSION LAYOUTS file (#139.4).