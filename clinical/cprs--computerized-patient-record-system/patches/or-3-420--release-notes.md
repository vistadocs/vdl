---
title: OR*3*420 Release Notes - Lab Monitoring CPRS GUI Version
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Lab Monitoring CPRS GUI Version
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*420
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - cprs
  - order
  - test
  - vista
  - patch
  - quick
  - added
  - results
page_count: 0
word_count: 960
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_420rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_420rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

CPRS Lab MonitoringPatch OR\*3.0\*420

Release Notes

![](or-3-420-release-notes-lab-monitoring-cprs-gui-version/001.png)

March 2017

Office of Information and Technology (OI&T)

.

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
This patch modifies the existing Pharmacy package in VistA to display the most recent associated lab results when a clinician is ordering medication using the Computerized Patient Record System (CPRS) Inpatient or Outpatient Medication Order dialogs.
This modification to VistA originated as a field-developed enhancement for local use at a VA facility. It was determined that the modification would be of benefit to the wider VistA user community, and so it is now being deployed nationally.
The following New Service Request (NSR) is resolved with this patch:
- NSR20100311 – CPRS Lab Monitoring

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to communicate changes to the VistA system resulting from implementation of OR\*3.0\*420.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users of the Pharmacy package in VistA and CPRS.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and enhancements introduced by this patch, as well as any known issues.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds no new VistA or CPRS features.

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ATTENTION (ESPECIALLY MULTI-DIVISIONAL FACILITIES):

This enhancement will not work properly for multi-divisional facilities or any sites that use different lab test names at different sites, as only one lab test name can be associated with each drug. To successfully implement this solution, all facilities/divisions that share a VistA system must use the same name for each monitored lab test. If this is not feasible or desired, then do not populate lab tests in the LAB TEST MONITOR field after installing this patch.

Example: If all divisions of your facility use a single laboratory test named CREATININE, then the software will work as intended. If individual divisions use specifically named lab tests such as KAN-CREATININE and WIC-CREATININE, then do not use those lab tests with this software enhancement.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Patch OR\*3.0\*420 modifies the existing Pharmacy package in VistA to display the most recent associated lab results when a clinician is ordering medication using the CPRS Inpatient or Outpatient Medication Order dialogs. Without this modification, the clinician must look in numerous locations for this information. The information is important for safe and effective medication management.

The lab results for the most recent lab test associated with an Orderable Item will be displayed in the Information field in the Medication Order dialog after an Orderable Item is selected. When a dispense drug is chosen (by selecting a dosage in the order dialog), the lab test information will be replaced by the National Standard Drug Information found in the MESSAGE (#101) field of the DRUG (#50) file. This message currently shows in CPRS when ordering a dispense drug and is not changed by this modification. Note: Follow-on work to allow persistence of the lab test information in the Medication Order dialog is expected to be addressed in CPRS v32.

In order to monitor lab results, lab tests are associated with an Orderable Item using the PSS DRUG ENTER/EDIT option in VistA by entering a lab test in the LAB TEST MONITOR (#17.2) field of the DRUG (#50) file.

To apply this functionality to Quick Orders, routine ORWDPLM2 can be used as a TIU OBJECT that can be added to a Quick Order. A site may use this optionally to add to a Quick Order to allow the functionality to be added to the comment section of the order. This is done by creating the OBJECT using the TIU Document Definitions option and inserting it into the comments field of the Quick Order. Upon selection of the Quick Order in CPRS, the monitored LAB results will appear on the Ordering screen. If assistance is needed for setting up TIU Objects inside Quick Orders, contact your Clinical Application Coordinator (CAC) or refer to the TIU User Manual for instructions. Note: The TIU OBJECT method will work for generalized Quick Orders only (orders assigned to Order Menus). It is not currently implemented for personal Quick Orders.

A new KERNEL system parameter (OR CPRS LAB DISPLAY ENABLED) is added by this patch to turn the functionality On/Off. Initially, this parameter is set to OFF (NO). A Clinical Application Coordinator (CAC) or Pharmacy Automated Data Processing Application Coordinator (ADPAC) at each site will need to set this parameter to the ON value (YES) to activate this functionality at the site.

The following new routines were added to implement this enhancement:

- ORWDPLM1 – displays LAB TEST MONITOR results for Lab tests.
- ORWDPLM2 – TIU Object calculations and displays.

The following routine was modified to implement this enhancement:

- ORWDPS2 – modified to call LAB TEST MONITOR results display modules in new routines ORWDPLM1 and ORWDPLM2

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional end-user documentation available for this patch includes:

- CPRS Technical Manual: GUI Version – cprsguitm.pdf
- CPRS User Guide: GUI Version – cprsguium.pdf
- Pharmacy Data Management User Manual – pss_1_um_r0317.pdf
- Text Integration Utility (TIU) Clinical Coordinator & User Manual – tiuum.pdf

These documents can be found in the VA Software Document Library (VDL).