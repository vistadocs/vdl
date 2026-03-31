---
title: CPT Version 6 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: CPT
app_name: Current Procedural Terminology
section: FIN
app_status: active
pkg_ns: CPT
patch_ver: 6
patch_id: CPT*6
group_key: "CPT:CPT:6"
file_numbers: []
security_keys: []
menu_options: 0
description: - [May 1997IntroductionCommentsPackage Updates](#may-1997introductioncommentspackage-updates) > New Options > Obsolete Options > New Routines > Changed Routines > Obsolete Routines > Obsolete Files > New Sort Templates > New Print Templates > Obsolete Print Templates Other Package Modifications > Sc
audience: 
keywords: 
  - icpt
  - release
  - codes
  - routines
  - dgya
  - procedure
  - package
  - modifications
  - apis
  - obsolete
page_count: 0
word_count: 528
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Current_Proc_Terminology_(CPT)/cpt6_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Current_Proc_Terminology_(CPT)/cpt6_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=33"
---

Current Procedural Terminology (CPT) V. 6.0 Release Notes

# May 1997IntroductionCommentsPackage Updates


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [May 1997IntroductionCommentsPackage Updates](#may-1997introductioncommentspackage-updates)
> New Options
> Obsolete Options
> New Routines
> Changed Routines
> Obsolete Routines
> Obsolete Files
> New Sort Templates
> New Print Templates
> Obsolete Print Templates
Other Package Modifications
> Scheduling Modifications
> PCE Modifications
> ADT/R Modifications
Introduction
This release of the Current Procedural Terminology (CPT) contains the 1997 procedure codes. The effective date for the ambulatory procedure codes for this release will be 6/2/97.
CPT was a submodule of Registration with numerous integration agreements allowing accessibility. In addition, other packages had duplicate files to the CPT file in their own namespaces to facilitate their usage of the data. This release is a redesign to move CPT to its own ICPT namespace. It incorporates such data as is needed by the other packages, eliminating file redundancy. It includes APIs accessible to all for ready access to the data. Modifiers are also included in this release.
Comments
1\. The effective date for the CPT codes released in V. 6.0 is 6/2/97. Nationally inactivated CPT codes will NOT be selectable after the effective date of 6/2/97.
2\. There are several new APIs associated with this release of CPT. The APIs and descriptions may be found in the Routines section of the CPT Technical Manual.
Package Updates
New Options
ICPT CPT CODES INACTIVE
ICPT MODIFIERS BY RANGE
ICPT NEW CPT CODES
ICPT OUTPUT MENU
ICPT REVISED CPT CODES
Obsolete Options
DGYA AMBUL PROC LOCAL ACTIVE
DGYA CPT CODES INACTIVE
DGYA NEW CPT CODES
DGYA OUTPUT MENU
DGYA REVISED CPT CODES
New Routines
All ICPT routines are new with this release.
Changed Routines
DGYACPT has been changed to point to the ICPT routines. The DGYACPT entry points will no longer be supported 18 months after the CPT package release date.
Obsolete Routines
DGYA\* except DGYACPT.
Obsolete Files
81.4 - CPT MODIFIER CATEGORY
81.5 - CPT SOURCE
New Sort Templates
ICPT MODIFIERS FOR RANGE
ICPT NEW/INACTIVE CODES
New Print Templates
ICPT MODIFIERS BY RANGE
ICPT PRINT
Obsolete Print Templates
DGYA MODIFIER DESCRIPTION
DGYA PRINT
Other Package Modifications
Scheduling Modifications
There are changes to Scheduling V. 5.3 with the CPT V. 6.0 release.
Routines SDAMBAE2 and SDAMBAE3 have been modified to change the references to the AMBULATORY PROCEDURE file (#409.71) and the AMBULATORY PROCEDURE TIME SENSITIVE DATA file (#409.72) to appropriate reference to CPT files and APIs. These routines will be installed with the CPT package.
The data dictionary for the SCHEDULING VISITS file (#409.5) is modified so that the PROCEDURE fields (#21-25) of the CLINIC STOP CODE multiple (Field \#10) will point to the CPT file (#81) instead of to the now obsolete AMBULATORY PROCEDURE file (#409.71).
The affected input templates for File \#409.5 are brought in - SDAMBT and SDXACASE.
Files \#409.71 and \#409.72 will no longer be maintained.
See associated patch SD\*5.3\*111 for a complete description of CPT-related scheduling changes.
Patient Care Encounter (PCE) Modifications
There are changes to PCE V. 1.0 with the CPT V. 6.0 release.
Routine PXBUTL has been changed such that all references to File \#409.72 have been replaced with the appropriate CPT APIs.
See associated patch PX\*1.0\*32.
ADT/R Modifications
There are changes to ADT/R V. 5.3 with the CPT V. 6.0 release.
Routine VAFHLPR1 has been changed such that the reference to File \#409.71 has been removed. Routine VACPT has been modified to use the new COPY^ICPTAPIU API for displaying the CPT Copyright text.
See associated patch DG\*5.3\*123.
