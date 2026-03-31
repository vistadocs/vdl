---
title: EAS*1*174 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: EAS
app_name: Enrollment Application System
section: FIN
app_status: active
pkg_ns: EAS
patch_ver: 1
patch_id: EAS*1*174
group_key: "EAS:EAS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - release
  - test
  - exemption
  - contents
  - span
  - vista
  - veteran
  - medal
  - honor
page_count: 0
word_count: 1406
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_174_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_174_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=121"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Enrollment System Modernization (ESM) Phase 2

  Veterans Health Information Systems and Technology Architecture (VistA)  
  Registration, Eligibility & Enrollment (REE)

  EAS\*1.0\*174

  Release Notes
---

![](eas-1-174-release-notes/001.png)

December 2019

Office of Information and Technology (OIT)

Table of Contents

List of Figures

List of Tables

[Table 1: EAS\*1.0\*174 Enhancements and Modifications [2](#_Ref533696768)](#_Ref533696768)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [This Release](#this-release)
  - [New Features and Functions Added](#new-features-and-functions-added)
  - [Enhancements and Modifications](#enhancements-and-modifications)
  - [Known Issues](#known-issues)
- [Product Documentation](#product-documentation)
The release of Veterans Health Information System and Technology Architecture (VistA) Registration, Eligibility & Enrollment (REE) Enrollment Application System (EAS) patch EAS\*1.0\*174 supports the enhancements for the Enterprise Health Benefits Determination (EHBD) program that focuses on updates for the Enrollment System Modernization (ESM) Phase 2 project, which supports Enrollment System Community Care (ESCC) and Enrollment System (ES) Sustainment.

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release Notes cover the changes to the VistA REE EAS system for this release. EAS\*1.0\*174 is also being released in support of the ES 5.6 release. Refer to Informational Patch EAS\*1.0\*178 for additional details regarding the ES release.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of VistA REE and applies to the changes made between this release and any previous release for this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software is being released as a patch (PackMan) message. The PackMan message includes the EAS\*1.0\*174 patch, which also supports the ES 5.6 release.

IMPORTANT NOTE: The following patches, which all include functionality for Medal of Honor, will be released concurrently and should be installed in the following order:

1.  VistA REE Registration (DG) patch DG\*5.3\*972, released with Income Verification Match (IVM) patch IVM\*2.0\*183 in Host File DG_53_P972.KID, ensures Veterans awarded Medal of Honor are placed in Priority Group 1 and are exempt from copayments for health care and medications.
2.  Patch IVM\*2.0\*183, released with DG\*5.3\*972 in Host File DG_53_P972.KID, modifies how VistA determines if an income test is the active current test per Veteran's Financial Assessment (VFA) rules and adds a condition that Medal of Honor recipients are not subject to income testing.
3.  Patch EAS\*1.0\*174 ensures VistA users can exempt Veterans awarded Medal of Honor from Long Term Care (LTC) copayments and LTC income testing.
4.  Integrated Billing (IB) patch IB\*2.0\*627 will need to be installed directly after EAS\*1.0\*174 as the full functionality of Medal of Honor will not be apparent until IB\*2.0\*627 is installed.

The following sections provide a summary of the enhancements and modifications to the existing software for VistA REE with the release of patch EAS\*1.0\*174.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new features or functions added to VistA REE for EAS\*1.0\*174.

## Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently the Add a New Long Term Care (LTC) Copayment Test \[EASEC LTC COPAY TEST ADD\] option determines if a Veteran qualifies for an automatic LTC Copay Test exemption without consideration of the Veteran's Medal of Honor (MOH) status. If the Veteran does not qualify for an automatic exemption, the user can manually select from a sub-set of the LTC Copay Test exemption reasons, and the user can also complete the detailed income test (LTC Copayment Exemption Test).

Public Law 114-315 amends United States Code Title 38 Section 1710(a), 1710B, and 1722A and exempts Veterans awarded MOH from copayments for health care, medications, and extended care services.

Additionally, PL 114-315 provides that all Veterans awarded the MOH currently enrolled for Veterans Affairs (VA) hospital care and medical services, and whose Veterans Health Administration (VHA) enrollment records are not currently assigned to Priority Group 1, will have their enrollment record updated to reflect enrollment in Priority Group 1 and exemption from copayments for health care, medications, and extended care services.

Patch EAS\*1.0\*174 ensures VistA users can exempt Veterans awarded MOH from LTC copayments and LTC income testing.

Table 1 shows the enhancements and modifications included in the EAS\*1.0\*174 release as tracked in Rational Team Concert (RTC) Requirements Management (RM).

<table>
<caption><p><span id="_Ref533696768" class="anchor"></span>Table 1: EAS*1.0*174 Enhancements and Modifications</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RTC<br />
RM #</strong></th>
<th><strong>Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1005712</td>
<td>CR 745614: If MOH is Yes - Not subject to Income Testing in VistA REE</td>
</tr>
<tr class="even">
<td>1005714</td>
<td>CR 745614: MOH is Yes - Exempt from All Copayments</td>
</tr>
</tbody>
</table>

<span id="_Ref533696768" class="anchor"></span>Table 1: EAS\*1.0\*174 Enhancements and Modifications

List of Updates

This patch includes the following enhancements to VistA REE:

1.  VistA is updated to add a new LTC reason for exemption entry "VETERAN AWARDED MEDAL OF HONOR" in the LTC CO-PAY EXEMPTION file (#714.1).

![](eas-1-174-release-notes/002.png)

<span id="_Toc21531718" class="anchor"></span>Figure 1: LTC Reason for Exemption “Veteran Awarded Medal of Honor” in LTC CO-PAY EXEMPTION file (#714.1)

2.  When a VistA REE user selects the Add a New LTC Copayment Test \[EASEC LTC COPAY TEST ADD\] option, VistA first determines if the Veteran qualifies for an automatic exemption. The automatic exemption logic now also considers whether the Veteran is awarded Medal of Honor.
    1.  Medal of Honor is inserted into the hierarchy of automatic exemptions in the following order:

> <u>Number</u> <u>Name</u>  
> 1 COMPENSABLE SC DISABILITY  
> 14 VETERAN AWARDED MEDAL OF HONOR  
> 10 INCOME (LAST YEAR) BELOW LTC THRESHOLD  
> 12 INCOME (CURRENT YEAR) BELOW LTC THRESHOLD

2.  VistA automatically selects the new MOH LTC reason for exemption that is highest in the hierarchy, so a Veteran that is awarded Medal of Honor and has an eligibility of Compensable Service Connected will be assigned the LTC reason for exemption "COMPENSABLE SC DISABILITY.
3.  When the CURRENT MOH INDICATOR field (#.541) in the PATIENT file (#2) is YES and the Veteran is not Service Connected (SC) Compensable, the new MOH LTC reason for exemption is assigned.

![](eas-1-174-release-notes/003.png)

<span id="_Toc21531719" class="anchor"></span>Figure 2: New MOH LTC Reason for Exemption – CURRENT MOH INDICATOR = YES / Veteran Not SC Compensable

3.  When the Veteran does not have an eligibility or income that qualifies for automatic exemption from LTC copayments and income testing, the Add a New LTC Copayment Test \[EASEC LTC COPAY TEST ADD\] option functionality is unchanged. When the system prompts for the "Reason for Exemption:", the user may enter "??" to view the user-selectable reasons for exemption. None of the automatically selectable reasons, including "VETERAN AWARDED MEDAL OF HONOR" will be displayed or selectable.

![](eas-1-174-release-notes/004.png)

<span id="_Toc21531720" class="anchor"></span>Figure 3: Add a New LTC Copayment Test - User Selectable Reasons for Exemption

4.  When a user selects Edit an Existing LTC Copayment Test \[EASEC LTC COPAY TEST EDIT\] option for a Veteran that is awarded MOH and has an existing LTC copayment test, the user will not be able to edit the test.
    1.  If the test status is EXEMPT, the Status and Reason for Exemption will display.

![](eas-1-174-release-notes/005.png)

<span id="_Toc21531721" class="anchor"></span>Figure 4: LTC Copayments Menu EXEMPT Status and Reason for Exemption Display

2.  When a user selects Edit an Existing LTC Copayment Test \[EASEC LTC COPAY TEST EDIT\] option for a Veteran that has an existing LTC copayment test and has a status of NON-EXEMPT, the following message will be displayed after the LTC copayment test: "Veteran is Awarded Medal of Honor - Add a New LTC Copayment Test to update status".

![](eas-1-174-release-notes/006.png)

<span id="_Toc21531722" class="anchor"></span>Figure 5: LTC Copayments Menu NON-EXEMPT Message Display

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No known or open issues were identified in this release.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

<u>Title File Name FTP Mode</u>

EAS\*1.0\*174 Release Notes EAS_1_174_RN.PDF (binary)  
Long Term Care Copayment  
V. 1.0 User Manual EAS_1_LTC_UM.PDF (binary)

The preferred method is to retrieve files from REDACTED This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

Hines: REDACTED  
Salt Lake City: REDACTED

Documentation can also be found on the VA Software Documentation Library at:

<http://www.va.gov/vdl/>