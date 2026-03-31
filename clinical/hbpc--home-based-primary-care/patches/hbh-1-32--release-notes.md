---
title: HBH*1*32 HBPC Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: HBPC
app_name: Home Based Primary Care
section: CLI
app_status: active
pkg_ns: HBH
patch_ver: 1
patch_id: HBH*1*32
group_key: "HBPC:HBH:1"
file_numbers: []
security_keys: []
menu_options: 0
description: These release notes cover the changes to Home Base Primary Care for the HBH\1.0\32 release.
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - hbpcare
  - provider
  - number
  - hbpc
  - table
  - contents
  - release
  - site
  - hbhc
  - update
page_count: 0
word_count: 1083
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbh_1_0_p32_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbh_1_0_p32_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=68"
---

## Table of Contents

  - [## Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [Patch Information](#patch-information)
    - [Site Preparation](#site-preparation)
  - [This Release](#this-release)
    - [New Features and Functions Added](#new-features-and-functions-added)
    - [Enhancements and Modifications to Existing](#enhancements-and-modifications-to-existing)
    - [Known Issues](#known-issues)
  - [Product Documentation](#product-documentation)
---
title: |
  <span id="_Toc205632711" class="anchor"></span>Home Based Primary Care
  HBH\*1.0\*32
  Release Notes
---
![](hbh-1-32-hbpc-release-notes/001.png)
August 2021
Table of Contents

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch includes the following enhancements:

1.  Modify the VistA-HBPC module to increase the number of providers that can be assigned unique Provider Number from the current limit of 2,999 to an upper limit of 9,999.
2.  Modify the VistA-HBPC module to add the site number with suffix-level granularity to patient-level HBPC data for each patient admission to an HBPC Program.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to Home Base Primary Care for the HBH\*1.0\*32 release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of Home Base Primary Care and applies to the changes made between this release and any previous release for this software.

## Patch Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HBH\*1.0\*32 includes specific pre-installation, post-installation, and prerequisite installation details that have been highlighted in the accompanying *Deployment, Installation, Back-out, and Rollback Guide* (DIBR). The list below contains the corresponding section number and title, within the DIBR, where the details can be found.

- 3.2.3 Site Preparation (which is also outlined in the next section, Site Preparation)
- 4.1 Pre-Installation and System Requirements
- 4.2 Platform Installation and Preparation
- 4.9.1 KIDS Verification

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites have been instructed to perform two FileMan searches. These searches will determine the presence of the following two conditions:

1.  If any providers are defined for more than one active HBHC provider number
2.  If an active HBHC provider number is defined for more than one provider.

    A visual inspection is needed to determine if either of the two conditions are present. If the FileMan searches have not yet been performed, they are listed below:
1.  Search to determine if any provider is defined with more than one active HBPC provider number.

> **NOTE:** Before inactivating one of the numbers, determine if these are different providers who have the same name.

Figure : Example search for providers with more than one active HBPC provider number

![](hbh-1-32-hbpc-release-notes/002.png)

2.  FileMan search to determine if active HBHC provider numbers are defined for more than one provider.

Figure : Example search for active provider numbers defined for more than one provider

![](hbh-1-32-hbpc-release-notes/003.png)

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issue for HBH\*1.0\*32.

### New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the new features and functions added to the HBH\*1.0\*32 release.

#### HBPCARE-15 - VistA environment provider number wheels

#### HBPCARE-18 - Identify unused provider numbers in the number wheel

#### HBPCARE-19 - Auto-assign the next available chronological provider number in the number wheel

#### HBPCARE-32 - Convert Provider File Data Entry in HBHC Edit Provider option from VistA Roll and Scroll to ListMan functionality

#### HBPCARE-35 - Provide additional details when adding new provider in HBHC Edit Provider Number

#### HBPCARE-36 - Alert user if provider has been previously defined

#### HBPCARE-53 - "PARENT SITE" prompt help text

#### HBPCARE-54 - Station Number AITC Record Transmission

#### HBPCARE-55 - Patient facility AITC error handling

#### HBPCARE-56 - Pad provider number with leading zeros in AITC Transmission

#### HBPCARE-57 - ListMan Print Functions

#### HBPCARE-61 - Notify Installer if HBH\*1.0\*32 patch install is halted

#### HBPCARE-62 - Inactive HBPC providers returning to the HBPC program at a facility

#### HBPCARE-63 - Inactive provider display in HBHC Edit Provider Number option

#### HBPCARE-64 - Max Number of Providers Reached Message

#### HBPCARE-66 - Check Transmission status upon edit of PARENT SITE prompt

#### HBPCARE-76 - Check for active providers sharing the same provider number

#### HBPCARE-77 - Check for the same user being assigned to more than one active HBPC provider number

#### HBPCARE-78 - Transmit correct transaction types if PARENT SITE prompt is edited but patient has NOT been discharged

#### HBPCARE-79 - Transmit correct transaction types if PARENT SITE prompt is edited on a patient with a complete episode of care.

#### HBPCARE-80 - Build local HBPC facility list

#### HBPCARE-81 - Use local HBPC facility list

#### HBPCARE-82 - Default HBPC Program Facility "PARENT SITE"

#### HBPCARE-83 - Make "PARENT SITE" a required prompt

#### HBPCARE-87 - SYSTEM PARAMETERS EDIT Select Parent Site Definition Help Statement

#### HBPCARE-88 - Add "PARENT SITE" prompt to DEMOGRAPHIC DATA ENTRY FOR MFH option

### Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modifications to the HBH\*1.0\*32 release.

#### HBPCARE-9 - Maintain 4-digit HBPC provider numbers

#### HBPCARE-11 - Update HBPC provider number logic from Edit Provider Number option

#### HBPCARE-12 - Update HBPC provider number logic on the Input Transform

#### HBPCARE-13 - Expand first and second provider number digits to allow 0 thru 9

#### HBPCARE-14 - Maintain existing provider number definitions

#### HBPCARE-16 - Update HBHC Edit Provider Number option to prompt for provider name first

#### HBPCARE-17 - Update message when Provider not found while in the HBHC Edit Provider Number option

#### HBPCARE-20 - Update Mailman logic to allow for HBPC test account transmissions

#### HBPCARE-27 - Transmission message type 3 admission facility ID update

#### HBPCARE-28 - Transmission message type 4 visit facility ID update

#### HBPCARE-29 - Transmission message type 5 discharge facility ID update

#### HBPCARE-30 - Transmission message type 6 correction facility ID update

#### HBPCARE-31 - Transmission message type 7 Medical Foster Home facility ID update

#### HBPCARE-33 - Remove ability to inactivate HBPC Providers

#### HBPCARE-34 - Discontinue VistA @ symbol deletion functionality in the HBHC Edit Provider option

#### HBPCARE-43 - Update Mailman logic to allow for HBPC test account RE-transmissions

#### HBPCARE-50 - New prompt addition to HBHC Evaluation/Admission Data Entry option

#### HBPCARE-65 - Update Data Dictionary info for deprecated fields in HBHC EDIT PROVIDER file \#631.4

#### HBPCARE-67 - Disable the HBPC Provider File Report option from the Manager Menu

#### HBPCARE-69 - Review HBPC Management Reports for HBPC Provider data usage

#### HBPCARE-70 - Evaluation/Admission Data Report by Patient

#### HBPCARE-71 - Discharge Data by Patient

#### HBPCARE-72 - Form Errors Report

#### HBPCARE-75 - Update references from HBHC to HBPC for HBHC EDIT PROVIDER option

### Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No known issues.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

- Installation Guide
- Security Guide
- Technical Manual
- User Manual

All release documentation will be housed in the vista-home-based-primary-care-product repository of GitHub EC, the SOFTWARE library, and the Veterans Document Library (VDL).