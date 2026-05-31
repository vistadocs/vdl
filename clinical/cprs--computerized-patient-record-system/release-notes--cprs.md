---
title: OR*3*546 Release Notes CPRS
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*546
group_key: CPRS:OR:3
file_numbers:
- '8989.5'
- '8989.51'
security_keys: []
menu_options: 0
description: '| Date | Version | Description | Author | |------------|-------------|-----------------|----------------------| | 06/17/2021 | 1.0 | Initial version | Liberty IT Solutions'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 774
section_count: 7
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: false
is_stub: false
pub_date: June 2021
revision_count: 1
revision_newest: 06/17/2021
revision_oldest: 06/17/2021
docx_url: https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_0_546_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_0_546_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=338
audit_applied: '2026-05-31'
master_source: OR*3*546 Release Notes CPRS
master_pub_date: June 2021
consolidated_from: 3 versions
prior_versions:
- OR*3.0*617 Release Notes CPRS
- OR*3*437 Release Notes CPRS
consolidated_title: release notes cprs
---

OR\*3.0\*546

Release Notes

![](or-3-546-release-notes-cprs/001.png)

June 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date   | Version | Description | Author           |
|------------|-------------|-----------------|----------------------|
| 06/17/2021 | 1.0         | Initial version | Liberty IT Solutions |

Revision History, including date of changes, version, description of changes, and author of changes.

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
- [Appendix A - Acronyms](#appendix-a-acronyms)
The SHRPE product makes enhancements to the Computerized Patient Record System (CPRS) to implement functionality that would assist CPRS users with the treatment of VA patients:
- Clinical Application Coordinators (CAC) at a site where additional information is to be displayed to the user in CPRS when the Other Than Honorable (OTH) button is enabled.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the description and history updates in CPRS (OR) routines in patch OR\*3.0\*546. These updates reflect changes to the OTH button in CPRS.

- Display of default message "Call Registration Team for Details" in the OTH button box.
- Display any additional information, up to 2 lines, along with the default message in the OTH button box. \*\*Note\*\* Additional lines are both optional.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the CPRS (OR) application and applies to the changes made between this release and any previous release of this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software with patch OR\*3.0\*546.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ability to add up to 2 additinoal lines for display in CPRS when the OTH button is active for a parint is a new feature added with OR\*3.0\*546.

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modification made by OR\*3.0\*546

This patch will be used for the CPRS portion of the Suicide High Risk Patient Enhancements (SHRPE) Localized Messaging story. This patch adds the capability to enter/edit the

entries made in the PARAMETER DEFINITION File (#8989.51) to the

OR OTH BTN MSG parameter. The parameter definition text for display will

utilize the new OR OTH BTN MSG ADD/EDIT option. This new option will be

nested under the following menu option tree in VistA:

CPRS Manager Menu/CPRS Configuration (Clin Coord)/GUI Parameters

This patch is part of a host file that will also include the REGISTRATION

Patch DG\*5 and INTEGRATED BILLING Patch IB\*2.0\*697.

This patch adds the following functionality:

1.  A new Graphical User Interface (GUI) Parameter, OR OTH BTN LOCAL MSG

will be created in the PARAMETER DEFINITION File (#8989.5)

2\. The text "Call Registration Team for Details." Will always display in

the OTH Button in CPRS GUI. It cannot be edited or deleted.

3\. When the menu option is entered via VistA to access setting/editing the

new parameter, the user will first be shown a display screen

describing what the new option requires and will display in the

CPRS GUI OTH Button.

The text reads:

Add/Edit Text for Display in OTH Button in CPRS

-----------------------------------------------

The text 'Call Registration Team for Details.' will always be displayed.

It cannot be edited or deleted.

All messages will display like this:

Call Registration Team for Details. Optional Line 1

Optional Line 2

Current Local Message:

Call Registration Team for Details.

4\. The user will then be prompted to optionally enter Line 1 and Line 2

of the local message.

Enter Line 1 (optional, 24 char max): //

Enter Line 2 (optional, 70 char max): //

5\. Single question mark "?" help text is available for each prompt.

6\. Double question mark "??" help text is also available for each prompt.

7\. The user can edit or delete either or both lines of the text

individually. Deleting Line 1 will not delete Line 2. Deleting

Line 2 will not delete Line 1.

8\. If data is entered for Line 1, it will be concatenated to the end

of the text "Call Registration Team for Details."

9\. If data is entered for Line 2, it will be on a line below the default

message and Line 1 (if Line 1 is populated).

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None at this time.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

- Deployment, Installation, Back-out, and Rollback Guide (DIBRG).

# Appendix A - Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                         |
|-------------|--------------------------------------------------------|
| CAC         | Clinical Application Coordinators                      |
| CPRS        | Computerized Patient Record System                     |
| DIBRG       | Deployment, Installation, Back-Out, and Rollback Guide |
| GUI         | Graphical User Interface                               |
| OIT         | Office of Information and Technology                   |
| OR          | Order Entry                                            |
| OTH         | Other Than Honorable                                   |
| SHRPE       | Suicide High Risk Patient Enhancements                 |
| VA          | Department of Veteran Affairs                          |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: OR*3.0*617 Release Notes CPRS

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) is part of the Veterans Health

Information Systems and Technology Architecture (VistA) suite of application packages.

CPRS enables you to enter, review, and continuously update information connected with

a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and

procedures, record a patient's allergies or adverse reactions to medications, request and

track consults, enter progress notes, diagnoses, and treatments for each encounter, and

enter discharge summaries. In addition, CPRS supports clinical decision-making and

enables you to review and analyze patient data.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the Patient Safety Issues (PSIs) and defect corrections for OR\*3.0\*617.

### Patient Safety Issues 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HITPS-11182 : Anticoagulation Management Tool (AMT) reverting dosing matrix to previous value when updating a patient's dosing regiment in AMT.

### Defects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  INC31115306 - VISTAOR-36624 - Anticoagulation Management Tool software reverting dosing matrix to previous value.

> <u>Problem:</u>

> When the user enters outside Lab data (with a previous date) and new Flowsheet data in the same session, the sort order returned to the Graphical User Interface is incorrect, due to the system thinking that flowsheet entry is older based on the outside lab date.

> <u>Resolution:</u>

> Fixed FLOWTT^ORAM1 to use Internal Entry Number to sort instead of \[FS DATE\] field ("B" index).

2.  INC32051845 - VISTAOR-36623 - Anti-coagulation Management Tool (AMT) needs to be rebuilt with a newer version of broker.

> <u>Problem:</u>

> After the installation of CPRS v33.106.2 at Heartland East, a problem was identified with the Broker Development Toolkit (BDK). Some users have a Certificate Policy that was unexpected by the BDK patch. This meant users were not allowed to log in to CPRS with their PIV card. The previous version of AMT (OR\*3\*600) was built with the same broker.

> <u>Resolution:</u>

> Updating to current version of broker, XWB\*1.1\*74 v3.

3.  INC35910518 - VISTAOR-38601 - "floating point value" Error when adding new warfarin patient to the Anticoagulation Management Tool.

> <u>Problem:</u>

> When adding a new patient to AMT, getting errors on first entering AMT and when updating the dosing grid. This was caused by a change in the Delphi form creation process, changing the order of some internal events.

> <u>Resolution:</u>

> Added a check for status of AMT startup for new patients.

4.  VISTAOR-38467 - ICR 10060 Violation - direct global read ^VA(200,IEN,0) in ORAM1.

> <u>Problem:</u>

> While editing routine ORAM1 preexisting ICR violations were found in tags FLOWTT+8 and LOCK+7 there were direct reads when only FileMan calls are allowed.

> <u>Resolution:</u>

> Edited the direct reads and replaced with FileMan calls.

5.  VISTAOR-40798 - ANTICOAG - Clinics sorting bug.

> <u>Problem:</u>

> If the parameter ORAM CLINIC NAME contains free text that will sort canonically before the total number of clinics, the top sorting clinic will get removed from the list and the Clinic count will show up on the list, if selected and used, this selection will cause errors.

> <u>Resolution:</u>

> Changed the GUI code to delete the count before sorting the data.
