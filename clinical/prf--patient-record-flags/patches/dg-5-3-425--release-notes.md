---
title: DG*5.3*425 Patient Record Flags Phase I Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Patient Record Flags Phase I
app_code: PRF
app_name: Patient Record Flags
section: CLI
app_status: active
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*425
group_key: "PRF:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 4
description: The Patient Record Flags (DG\5.3\425) patch introduces changes and enhancements to the Registration V. 5.3 package in support of the Patient Record Flags initiative.
audience: 
keywords: 
  - record
  - flag
  - patient
  - table
  - assignment
  - contents
  - dgpf
  - flags
  - category
  - class
page_count: 0
word_count: 5808
section_count: 36
table_count: 78
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2003
revision_count: 4
revision_newest: 7/09/03
revision_oldest: 5/12/03
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/prfrn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/prfrn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=156"
---

![](dg-5-3-425-patient-record-flags-phase-i-release-notes/001.png)

Patient Record FlagsRelease Notes

### Patch DG\*5.3\*425

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

September 2003

### Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Health Systems Design & Development (HSD&D)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Patch DG\5.3\425](#patch-dg53425)
    - [Department of Veterans Affairs](#department-of-veterans-affairs)
- [Revision History](#revision-history)
- [<u> </u> Preface](#u-u-preface)
  - [Purpose of the Patch Release Notes](#purpose-of-the-patch-release-notes)
- [# # Introduction](#introduction)
  - [Overview](#overview)
- [# New Functionality](#new-functionality)
  - [Overview](#overview-1)
  - [New Options](#new-options)
  - [Patient Record Flags Main Menu](#patient-record-flags-main-menu)
    - [Menu Diagram](#menu-diagram)
  - [Record Flag Management](#record-flag-management)
  - [The new Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option can be accessed from the Patient Record Flags Main Menu option. This option provides a List Manager user interface for the management and administration of Patient Record Flags. Specifically, the following actions are provided within the Record Flag Management option.](#the-new-record-flag-management-dgpf-record-flag-management-option-can-be-accessed-from-the-patient-record-flags-main-menu-option-this-option-provides-a-list-manager-user-interface-for-the-management-and-administration-of-patient-record-flags-specifically-the-following-actions-are-provided-within-the-record-flag-management-option)
  - [Record Flag Assignment](#record-flag-assignment)
  - [The new Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option can be accessed from the new Patient Record Flags Main Menu option. This option provides a List Manager user interface for assigning Patient Record Flags to patients. Additionally, this option provides the ability to review and manage Patient Record Flag assignments. The following actions are provided within the Record Flag Assignment option.](#the-new-record-flag-assignment-dgpf-record-flag-assignment-option-can-be-accessed-from-the-new-patient-record-flags-main-menu-option-this-option-provides-a-list-manager-user-interface-for-assigning-patient-record-flags-to-patients-additionally-this-option-provides-the-ability-to-review-and-manage-patient-record-flag-assignments-the-following-actions-are-provided-within-the-record-flag-assignment-option)
  - [Record Flag Reports Menu](#record-flag-reports-menu)
  - [Flag Assignment Report](#flag-assignment-report)
  - [The new Flag Assignment Report \[DGPF FLAG ASSIGNMENT REPORT\] can be accessed from the Record Flag Reports Menu option. This option provides the ability to display/print a list of Record Flag Assignments that have been made to specific Category I (National) or Category II (Local) Patient Record Flags. Users will have the ability to enter a date range to limit the search for Record Flag Assignments that have been made to specific Category I (National) or Category II (Local) Patient Record Flags. The DGPF PRF ACCESS security key locks this option.](#the-new-flag-assignment-report-dgpf-flag-assignment-report-can-be-accessed-from-the-record-flag-reports-menu-option-this-option-provides-the-ability-to-displayprint-a-list-of-record-flag-assignments-that-have-been-made-to-specific-category-i-national-or-category-ii-local-patient-record-flags-users-will-have-the-ability-to-enter-a-date-range-to-limit-the-search-for-record-flag-assignments-that-have-been-made-to-specific-category-i-national-or-category-ii-local-patient-record-flags-the-dgpf-prf-access-security-key-locks-this-option)
  - [Assignments Due for Review Report](#assignments-due-for-review-report)
  - [The new Assignments Due for Review Report \[DGPF ASSIGNMENT DUE REVIEW RPT\] can be accessed from the Record Flag Reports Menu option. This option provides the ability to display/print a list of Record Flag Assignments that have been made to specific Category I (National) or Category II (Local) Patient Record Flags and now requires a review for appropriateness. The DGPF PRF ACCESS security key locks this option.](#the-new-assignments-due-for-review-report-dgpf-assignment-due-review-rpt-can-be-accessed-from-the-record-flag-reports-menu-option-this-option-provides-the-ability-to-displayprint-a-list-of-record-flag-assignments-that-have-been-made-to-specific-category-i-national-or-category-ii-local-patient-record-flags-and-now-requires-a-review-for-appropriateness-the-dgpf-prf-access-security-key-locks-this-option)
  - [PRF System Configuration](#prf-system-configuration)
  - [Patient Record Flag Background](#patient-record-flag-background)
  - [The new Patient Record Flag Background \[DGPF BACKGROUND PROCESSING\] option is the main driver for Patient Record Flag background processes. It is recommended that this option be scheduled to run daily during non-peak hours. The following functions are processed by this background option.](#the-new-patient-record-flag-background-dgpf-background-processing-option-is-the-main-driver-for-patient-record-flag-background-processes-it-is-recommended-that-this-option-be-scheduled-to-run-daily-during-non-peak-hours-the-following-functions-are-processed-by-this-background-option)
  - [## Display Active Patient Record Flag Assignments](#display-active-patient-record-flag-assignments)
  - [## Patient Lookup](#patient-lookup)
  - [New Patient Registration](#new-patient-registration)
  - [The following Registration (DG) options have been modified to automatically generate a query for patient record flag assignments when a new patient is registered at the facility.](#the-following-registration-dg-options-have-been-modified-to-automatically-generate-a-query-for-patient-record-flag-assignments-when-a-new-patient-is-registered-at-the-facility)
  - [Sharing Category I-Record Flag Assignments](#sharing-category-i-record-flag-assignments)
  - [Unsolicited Observation Update Interface](#unsolicited-observation-update-interface)
  - [Query Interface](#query-interface)
- [Technical Information](#technical-information)
  - [Overview](#overview-2)
  - [New Options](#new-options-1)
  - [New Protocols](#new-protocols)
  - [New Mail Groups](#new-mail-groups)
  - [New Security Keys](#new-security-keys)
  - [New List Templates](#new-list-templates)
  - [New HL7 Application Parameters](#new-hl7-application-parameters)
  - [New Files/Global](#new-filesglobal)
  - [New Database Integration Agreement (DBIA)](#new-database-integration-agreement-dbia)
  - [New/Modified Routines](#newmodified-routines)
  - [Background Jobs](#background-jobs)
|          |              |                                           |                                    |
|----------|--------------|-------------------------------------------|------------------------------------|
| Date | Revision | Description                           | Author                         |
| 5/12/03  | 1            | Initial Draft                             | <span class="mark">REDACTED</span> |
| 5/28/03  | 1.1          | Edit Review changes                       | <span class="mark">REDACTED</span> |
| 7/01/03  | 1.2          | Edit Background Process changes           | <span class="mark">REDACTED</span> |
| 7/09/03  | 1.2          | Edit Option/Protocol names & descriptions | <span class="mark">REDACTED</span> |

# <u> </u> Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose of the Patch Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes the new features and functionality of the Patient Record Flags (DG\*5.3\*425) patch. Additionally, this document includes a description of the technical components that are being exported with this patch.

> **NOTE:** The User Guide for the Patient Record Flags (DG\*5.3\*425) patch is presented separately. Details regarding the installation instructions for this patch are included in the Patient Record Flags (DG\*5.3\*425) patch message generated from the National Patch Module (NPM) on Forum. This patch introduces a new HL7 interface. Please refer to the Patient Record Flags HL7 Interface Specification for a detailed description of the Patient Record Flags HL7 interface.

Two additional patches, USR\*1\*24 and TIU\*1\*165, are being released as a separate distribution (host file) in support of patch DG\*5.3\*425.

[Purpose of the Patch Release Notes [iii](#purpose-of-the-patch-release-notes)](#purpose-of-the-patch-release-notes)

[1.1 Overview [1](#overview)](#overview)

# # # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Record Flags (DG\*5.3\*425) patch introduces changes and enhancements to the Registration V. 5.3 package in support of the Patient Record Flags initiative.

The VA Office of Inspector General (OIG) in its report "Evaluation of VHA's Policies and Practices for Managing Violent or Potentially Violent Psychiatric Patients" (6HI-A28-038, dated March 28, 1996) recommended that facilities communicate among themselves so that staff are aware of high risk patients regardless of where in the VHA system they may seek health care.

The Patient Record Flags module of the Registration package provides the functionality needed to implement the OIG's recommendation. Patient Record Flags (a.k.a. Computerized Patient Advisories) will alert VHA employees of patients whose behavior or characteristics may pose a threat either to the safety of the employee, the safety of other patients, or compromise the delivery of quality health care.

Patient Record Flags are separated into two categories: Category I and Category II.

Category I Patient Record Flags are established and approved at a national level and will be distributed for implementation by all facilities through software/patch releases. The assignment of a Category I flag to a patient or the modification of patient’s assignment to a Category I flag will be shared with all known treating facilities for the patient using VistA HL7 messaging. Modification of existing Category I flag assignments will be limited to the site designated as the "owner" during the record flag assignment process.

This patch distributes a single Category I flag, named "BEHAVIORAL", for implementation by all facilities. The purpose of this patient record flag is to alert VHA medical staff and employees of patients whose behavior or characteristics may pose a threat either to their safety, the safety of other patients, or compromise the delivery of quality health care.

Category II Patient Record Flags are established and approved at a local level by individual VISNs or facilities. The assignment of a Category II flag to a patient will not be shared between facilities.

For additional information, refer to VHA Directive 2003-048 "National Patient Record Flags".

# # New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the details of the new functionality being implemented with the Patient Record Flags (DG\*5.3\*425) software.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patient Record Flags Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Patient Record Flags Main Menu \[DGPF RECORD FLAGS MAIN MENU\] option is a stand-alone menu option. This is the master menu for the Patient Record Flags module and contains sub-menus and options that are available for use. This new menu option should be distributed to personnel responsible for the management and administration of Patient Record Flags and their assignment to patients. The DGPF PRF ACCESS security key locks this menu option.

### Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient Record Flags Main Menu

> \[DGPF RECORD FLAGS MAIN MENU\]

> \*\*LOCKED: DGPF PRF ACCESS\*\*

> \|

> \|

> \|------RM Record Flag Reports Menu

> \| \[DGPF RECORD FLAG REPORTS MENU\]

> \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \| \|

> \| \|

> \| \|-----------FAR Flag Assignment Report

> \| \| \[DGPF FLAG ASSIGNMENT REPORT\]

> \| \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \| \|

> \| \|-----------ADR Assignments Due For Review Report

> \| \[DGPF ASSIGNEMENT DUE REVIEW RPT\]

\| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \|

> \|------FA Record Flag Assignment

> \| \[DGPF RECORD FLAG ASSIGNMENT\]

> \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \|

> \|------FM Record Flag Management

> \| \[DGPF RECORD FLAG MANAGEMENT\]

> \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \|

> \|------IRM PRF System Configuration

> \[DGPF PRF SYSTEM CONFIGURATION\]

> \*\*LOCKED: DGPF PRF CONFIG\*\*

## Record Flag Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The new Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option can be accessed from the Patient Record Flags Main Menu option. This option provides a List Manager user interface for the management and administration of Patient Record Flags. Specifically, the following actions are provided within the Record Flag Management option.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Display Category I (National) record flag details
- Display Category II (Local) record flag details
- Add new Category II (Local) record flags

\- Requires DGPF LOCAL FLAG EDIT Security Key

- Edit Category II (Local) record flags

\- Requires DGPF LOCAL FLAG EDIT Security Key

- View/Sort list of Category II (Local) record flags
- List Manager standard hidden actions (i.e., Search List and Print List).

The DGPF PRF ACCESS security key locks this option.

## Record Flag Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The new Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option can be accessed from the new Patient Record Flags Main Menu option. This option provides a List Manager user interface for assigning Patient Record Flags to patients. Additionally, this option provides the ability to review and manage Patient Record Flag assignments. The following actions are provided within the Record Flag Assignment option.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Display the details of a patient’s record flag assignments including the history of the assignment.
- Assign a Patient Record Flag to a patient.

\- Requires DGPF RECORD FLAG ASSIGNMENT Security Key

- Review/Edit a patient’s record flag assignment.

\- Requires DGPF RECORD FLAG ASSIGNMENT Security Key

- Change the site ownership of a patient’s record flag assignment.

\- Requires DGPF RECORD FLAG ASSIGNMENT Security Key

- List Manager standard hidden actions (i.e., Search List and Print List).

The DGPF PRF ACCESS security key locks this option.

## Record Flag Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Record Flag Reports Menu \[DGPF RECORD FLAG REPORTS MENU\] option can be accessed from the new Patient Record Flags Main Menu option. This sub-menu option contains all of the reporting options for the Patient Record Flags module. Currently the two report options available on the Record Flag Reports Menu are the Flag Assignment Report \[DGPF FLAG ASSIGNMENT REPORT\] option and the Assignments Due For Review Report \[DGPF ASSIGNMENT DUE REVIEW RPT\] option. The DGPF PRF ACCESS security key locks this menu option.

> <u>Sub-Menu Diagram:</u>

> RM Record Flag Reports Menu

> \[DGPF RECORD FLAG REPORTS MENU\]

> \*\*LOCKED: DGPF PRF ACCESS\*\*

> \|

\|

> \|------FAR Flag Assignment Report

> \| \[DGPF FLAG ASSIGNMENT REPORT\]

> \| \*\*LOCKED: DGPF PRF ACCESS\*\*

> \|

> \|------ADR Assignments Due For Review Report

> \[DGPF ASSIGNMENT DUE REVIEW RPT\]

> \*\*LOCKED: DGPF PRF ACCESS\*\*

## Flag Assignment Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The new Flag Assignment Report \[DGPF FLAG ASSIGNMENT REPORT\] can be accessed from the Record Flag Reports Menu option. This option provides the ability to display/print a list of Record Flag Assignments that have been made to specific Category I (National) or Category II (Local) Patient Record Flags. Users will have the ability to enter a date range to limit the search for Record Flag Assignments that have been made to specific Category I (National) or Category II (Local) Patient Record Flags. The DGPF PRF ACCESS security key locks this option.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Assignments Due for Review Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The new Assignments Due for Review Report \[DGPF ASSIGNMENT DUE REVIEW RPT\] can be accessed from the Record Flag Reports Menu option. This option provides the ability to display/print a list of Record Flag Assignments that have been made to specific Category I (National) or Category II (Local) Patient Record Flags and now requires a review for appropriateness. The DGPF PRF ACCESS security key locks this option.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PRF System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new PRF System Configuration \[DGPF PRF SYSTEM CONFIGURATION\] option can be accessed from the new Patient Record Flags Main Menu option. This option allows IRM staff to enable or disable the Patient Record Flag HL7 interfaces.

- This option will provide the ability to enable or disable the Unsolicited Observation Update (ORU~R01) HL7 interface for the Patient Record Flags module. This interface is responsible for the transmission of unsolicited patient record flag (Category I) assignment data to a patient's sites of record.
- This option provides the ability to control the query (QRY~R02) HL7 interface. The interface may be enabled or disabled. Additionally, the option allows the type of PRF HL7 query (QRY~R02) interface that may be used, either a VistA HL7 'direct' connection or a VistA HL7 'deferred' connection.

The DGPF PRF CONFIG security key locks this option

## Patient Record Flag Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The new Patient Record Flag Background \[DGPF BACKGROUND PROCESSING\] option is the main driver for Patient Record Flag background processes. It is recommended that this option be scheduled to run daily during non-peak hours. The following functions are processed by this background option.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Send review notification messages for pending Patient Record Flag Assignment reviews

This process searches the PRF ASSIGNMENT file (#26.13) for Patient Record Flag assignments that are due for review of appropriateness. A MailMan message will be generated to the mail group associated with the record flag, notifying the members of the pending review.

2\. Auto retransmitting of rejected HL7 Patient Record Flag Assignment messages

This process searches the "ASTAT" cross reference of the PRF HL7 TRANSMISSION LOG file (#26.17) looking for transmissions with a status of REJECTED ("RJ"). A new HL7 message will be transmitted to all sites of record for the patient's record flag assignment.

## ## Display Active Patient Record Flag Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Patient Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The custom patient lookup module in VistA has been modified. When a patient lookup is performed on a patient having ACTIVE Patient Record Flag Assignments, the flags assigned to the patient will be displayed. Once the ACTIVE record flags assigned to the patient are displayed, users will have the ability to view the assignment narrative and the details associated with each flag assignment.

## New Patient Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The following Registration (DG) options have been modified to automatically generate a query for patient record flag assignments when a new patient is registered at the facility.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Register a Patient \[DG REGISTER PATIENT\]
- Load/Edit Patient Data \[DG LOAD PATIENT DATA\]
- 10-10T Registration \[DGRPT 10-10T REGISTRATION\]

The query will occur in real-time and will be sent to the patient's Coordinating Master of Record (CMOR) site. The query will search for and return all the patient's ACTIVE and INACTIVE Category I (National) Patient Record Flag Assignments to be filed in the local site's Patient Record Flags database.

If an ACTIVE Category I (National) record flag assignment is found for the patient, it will be displayed to the user. The user will then have the ability to view the details of each of the patient's ACTIVE PRF assignments.

## Sharing Category I-Record Flag Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Unsolicited Observation Update Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This interface is responsible for the transmission of unsolicited Category I Patient Record Flag assignment data to a patient's sites of record. Patient Record Flag assignment and assignment edit events will trigger an R01 message to be sent to each site listed for the patient in the TREATING FACILITY LIST file (#391.91) under the following circumstances:

- When a Category I Patient Record Flag is initially assigned to a patient.
- When an existing Category I Patient Record Flag assignment is edited.

## Query Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a patient is newly registered at a facility, a query is generated to the CMOR site searching for any existing Category I (National) record flag assignments that may exist for that patient. If any ACTIVE and INACTIVE Category I (National) record flag assignments exist at the CMOR site, they are returned to the querying site and filed for the patient. The CMOR must not be the local site and the patient must have a national ICN. The ICN, SSN, and DOB together are used as the unique patient identifier when querying the CMOR site for existing Category I (National) record flag assignments.

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides technical information related to the Patient Record Flags (DG\*5.3\*425) patch. Details regarding the installation instructions for this patch are included in the Patient Record Flags (DG\*5.3\*425) patch message generated from the National Patch Module (NPM) on Forum.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new OPTION(s) will be added:

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NAME:</td>
<td>DGPF RECORD FLAG ASSIGNMENT</td>
</tr>
<tr class="even">
<td>MENU TEXT:</td>
<td>Record Flag Assignment</td>
</tr>
<tr class="odd">
<td>DESCRIPTION:</td>
<td><p>This option provides a List Manager user interface for assigning Patient Record Flags to patients. Additionally, this option provides the ability to review and manage Patient Record Flag assignments. The following actions are provided within the Record Flag Assignment option.</p>
<ul>
<li><p>Assign a Patient Record Flag to a patient.</p></li>
<li><p>Display the details of a patient's record flag assignments including the history of the assignment.</p></li>
<li><p>Review/Edit a patient's record flag assignment.</p></li>
<li><p>Change the site ownership of a patient's record flag assignment.</p></li>
</ul></td>
</tr>
</tbody>
</table>

|              |                                                                                                                                                              |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF RECORD FLAGS MAIN MENU                                                                                                                                  |
| MENU TEXT:   | Patient Record Flags Main Menu                                                                                                                               |
| DESCRIPTION: | This menu option contains all menus and options needed to assign, manage, and report patient record flag information. This is a new stand-alone menu option. |

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NAME:</td>
<td>DGPF RECORD FLAG MANAGEMENT</td>
</tr>
<tr class="even">
<td>MENU TEXT:</td>
<td>Record Flag Management</td>
</tr>
<tr class="odd">
<td>DESCRIPTION:</td>
<td><p>This option will provide users with the ability to</p>
<ul>
<li><p>Create Category II (Local) Patient Record Flags</p></li>
<li><p>Edit Category II (Local) Patient Record Flags</p></li>
<li><p>List Category I (National) and Category II (Local) Patient Record Flags</p></li>
<li><p>Display details of Category I and Category II Patient Record Flags</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NAME:</td>
<td>DGPF BACKGROUND PROCESSING</td>
</tr>
<tr class="even">
<td>MENU TEXT:</td>
<td>Patient Record Flag Background</td>
</tr>
<tr class="odd">
<td>DESCRIPTION:</td>
<td><p>This option should be scheduled to run once a day.</p>
<p>The following functions are processed by this background option.</p>
<p>1. Send review notification messages for pending Patient Record Flag Assignment reviews</p>
<p>2. Auto retransmitting of rejected HL7 Patient Record Flag Assignment messages</p></td>
</tr>
</tbody>
</table>

|              |                                                          |
|--------------|----------------------------------------------------------|
| NAME:        | DGPF RECORD FLAG REPORTS MENU                            |
| MENU TEXT:   | Record Flag Reports Menu                                 |
| DESCRIPTION: | This menu contains patient record flag report functions. |

|              |                                                                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF FLAG ASSIGNMENT REPORT                                                                                                           |
| MENU TEXT:   | Flag Assignment Report                                                                                                                |
| DESCRIPTION: | This option enables a user to display or print all of the patient assignments for Category I and/or Category II Patient Record Flags. |

|              |                                                                                                                                                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF ASSIGNMENT DUE REVIEW RPT                                                                                                                                |
| MENU TEXT:   | Assignments Due For Review Report                                                                                                                             |
| DESCRIPTION: | This option will be used to display or print all Category I or Category II Patient Record Flag Assignments that are due for review within a given date range. |

|              |                                                                                            |
|--------------|--------------------------------------------------------------------------------------------|
| NAME:        | DGPF PRF SYSTEM CONFIGURATION                                                              |
| MENU TEXT:   | PRF System Configuration                                                                   |
| DESCRIPTION: | This option enables IRM staff to enable or disable the Patient Record Flag HL7 interfaces. |

## New Protocols 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new PROTOCOL(s) will be added.

|              |                                                                                                                                                    |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF ADD FLAG                                                                                                                                      |
| ITEM TEXT:   | Add New Record Flag                                                                                                                                |
| TYPE:        | Action                                                                                                                                             |
| DESCRIPTION: | This action protocol allows a user to add a new Category II (Local) flag within the Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option. |

|              |                                                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF ASSIGN FLAG                                                                                                                              |
| ITEM TEXT:   | Assign Flag                                                                                                                                   |
| TYPE:        | Action                                                                                                                                        |
| DESCRIPTION: | This action protocol permits the user to assign a flag to a patient within the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option. |

|              |                                                                                                                                                                             |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF CHANGE ASSIGNMENT OWNERSHIP                                                                                                                                            |
| ITEM TEXT:   | Change Assignment Ownership                                                                                                                                                 |
| TYPE:        | Action                                                                                                                                                                      |
| DESCRIPTION: | This action protocol permits the user to change the site ownership of a patient's flag assignment within the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option. |

|              |                                                                                                                                                                                                                                                        |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF CHANGE CATEGORY                                                                                                                                                                                                                                   |
| ITEM TEXT:   | Change Category                                                                                                                                                                                                                                        |
| TYPE:        | Action                                                                                                                                                                                                                                                 |
| DESCRIPTION: | This action protocol allows the user to change the category of the flag list being viewed within the Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option. The user may view either Category I (National) flags or Category II (Local) flags. |

|              |                                                                                                                                                                    |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF DISPLAY ASSIGNMENT DETAIL                                                                                                                                     |
| ITEM TEXT:   | Display Assignment Details                                                                                                                                         |
| TYPE:        | Action                                                                                                                                                             |
| DESCRIPTION: | This action protocol permits the user to view the details of a patient's flag assignment within the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option. |

|              |                                                                                                                                                              |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF DISPLAY FLAG DETAIL                                                                                                                                     |
| ITEM TEXT:   | Display Flag Detail                                                                                                                                          |
| TYPE:        | Action                                                                                                                                                       |
| DESCRIPTION: | This action protocol permits the user to view the details of a patient record flag within the Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option. |

|              |                                                                                                                                                     |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF EDIT ASSIGNMENT                                                                                                                                |
| ITEM TEXT:   | Edit Flag Assignment                                                                                                                                |
| TYPE:        | Action                                                                                                                                              |
| DESCRIPTION: | This action protocol permits the user to edit a patient's flag assignment within the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option. |

|              |                                                                                                                                                 |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF EDIT FLAG                                                                                                                                  |
| ITEM TEXT:   | Edit Record Flag                                                                                                                                |
| TYPE:        | Action                                                                                                                                          |
| DESCRIPTION: | This action protocol allows a user to edit a Category II (Local) flag within the Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option. |

|              |                                                                                                                                                                   |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF PRF ORF/R04 SUBSC                                                                                                                                            |
| TYPE:        | Subscriber                                                                                                                                                        |
| DESCRIPTION: | This protocol is the subscriber protocol for the Patient Record Flags query message (QRY~R02). The protocol will return an Observation results message (ORF~R04). |

|              |                                                                                                  |
|--------------|--------------------------------------------------------------------------------------------------|
| NAME:        | DGPF PRF ORU/R01 EVENT                                                                           |
| TYPE:        | Event Driver                                                                                     |
| DESCRIPTION: | This protocol is the event protocol for Patient Record Flags assignment transmissions (ORU~R01). |

|              |                                                                                                       |
|--------------|-------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF PRF ORU/R01 SUBSC                                                                                |
| TYPE:        | Subscriber                                                                                            |
| DESCRIPTION: | This protocol is the subscriber protocol for Patient Record Flags assignment transmissions (ORU~R01). |

|              |                                                                                           |
|--------------|-------------------------------------------------------------------------------------------|
| NAME:        | DGPF PRF QRY/R02 EVENT                                                                    |
| TYPE:        | Event Driver                                                                              |
| DESCRIPTION: | This protocol is the event protocol for the Patient Record Flags query message (QRY~R02). |

|              |                                                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF RECORD FLAG ASSIGNMENT MENU                                                                                      |
| TYPE:        | Menu                                                                                                                  |
| DESCRIPTION: | This protocol menu contains all the activities for creating, editing, and displaying patient record flag assignments. |

|              |                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF RECORD FLAG MANAGEMENT MENU                                                                           |
| TYPE:        | Menu                                                                                                       |
| DESCRIPTION: | This protocol menu contains all the activities for creating, editing, and displaying patient record flags. |

|              |                                                                                                                                     |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF SELECT PATIENT                                                                                                                 |
| ITEM TEXT:   | Select Patient                                                                                                                      |
| TYPE:        | Action                                                                                                                              |
| DESCRIPTION: | This action protocol permits the user to select a patient within the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option. |

|              |                                                                                                                                                                                                              |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF SORT FLAG LIST                                                                                                                                                                                          |
| ITEM TEXT:   | Change Sort                                                                                                                                                                                                  |
| TYPE:        | Action                                                                                                                                                                                                       |
| DESCRIPTION: | This action protocol allows the user to select a sort criteria for the flag list within the Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option. The list may be sorted by flag name or flag type. |

## New Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new MAIL GROUP(s) will be added.

|                         |                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------|
| NAME:                   | DGPF BEHAVIORAL FLAG REVIEW                                                                       |
| TYPE:                   | Public                                                                                            |
| ALLOW SELF ENROLLMENT?: | No                                                                                                |
| DESCRIPTION:            | This is the default mail group for receiving Patient Record Flag Assignment Review notifications. |

|                         |                                                                                                                                               |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:                   | DGPF HL7 TRANSMISSION ERRORS                                                                                                                  |
| TYPE:                   | Public                                                                                                                                        |
| ALLOW SELF ENROLLMENT?: | No                                                                                                                                            |
| DESCRIPTION:            | This mail group is used to notify Patient Record Flag administrators of transmission errors that occur during the processing of HL7 messages. |

## New Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new SECURITY KEY(s) will be added.

|              |                                                                                                                                                                                                                              |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF PRF ACCESS                                                                                                                                                                                                              |
| DESC NAME:   | Patient Record Flag Access                                                                                                                                                                                                   |
| DESCRIPTION: | This security key is used to control access to the Patient Record Flags module of the Registration package. Holders of this key will be able to display record flag detail, patient assignment detail, and generate reports. |

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<tbody>
<tr class="odd">
<td>NAME:</td>
<td>DGPF RECORD FLAG ASSIGNMENT</td>
</tr>
<tr class="even">
<td>DESC NAME:</td>
<td>Patient Record Flag Assignment</td>
</tr>
<tr class="odd">
<td>DESCRIPTION:</td>
<td><p>This security key will be used to control user access to the following protocol actions within the List Manager, Record Flag Assignment [DGPF RECORD FLAG ASSIGNMENT] option:</p>
<ul>
<li><p>AF Assign Flag [DGPF ASSIGN FLAG]</p></li>
<li><p>EF Edit Flag Assignment [DGPF EDIT ASSIGNMENT]</p></li>
<li><p>CO Change Assignment Ownership [DGPF CHANGE ASSIGNMENT OWNERSHIP]</p></li>
</ul></td>
</tr>
</tbody>
</table>

|              |                                                                                                                                                                                          |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF LOCAL FLAG EDIT                                                                                                                                                                     |
| DESC NAME:   | Local Patient Record Flag Edit                                                                                                                                                           |
| DESCRIPTION: | This security key will be used to control user access to the Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option action items, AF Add New Record Flag and EF Edit Record Flag. |

|              |                                                                                                             |
|--------------|-------------------------------------------------------------------------------------------------------------|
| NAME:        | DGPF PRF CONFIG                                                                                             |
| DESC NAME:   | Patient Record Flag Config                                                                                  |
| DESCRIPTION: | This security key controls access to the PRF System Configuration \[DGPF PRF SYSTEM CONFIGURATION\] option. |

## New List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new LIST TEMPLATE(s) will be added.

|               |                         |
|---------------|-------------------------|
| NAME:         | DGPF ACTIVE ASSIGNMENTS |
| TYPE OF LIST: | DISPLAY                 |

|               |                        |
|---------------|------------------------|
| NAME:         | DGPF ASSIGNMENT DETAIL |
| TYPE OF LIST: | DISPLAY                |

|               |                  |
|---------------|------------------|
| NAME:         | DGPF FLAG DETAIL |
| TYPE OF LIST: | DISPLAY          |

|               |                             |
|---------------|-----------------------------|
| NAME:         | DGPF RECORD FLAG ASSIGNMENT |
| TYPE OF LIST: | PROTOCOL                    |

|               |                             |
|---------------|-----------------------------|
| NAME:         | DGPF RECORD FLAG MANAGEMENT |
| TYPE OF LIST: | PROTOCOL                    |

<u>List Template/Protocol Diagram</u>

List Template: DGPF RECORD FLAG ASSIGNMENT

\|

\|---------- Menu Protocol: DGPF RECORD FLAG ASSIGNMENT MENU

\|

\|---------- Action Protocol: DGPF SELECT PATIENT

\|

\|---------- Action Protocol: DGPF ASSIGN FLAG

\|

\|---------- Action Protocol: DGPF EDIT FLAG ASSIGNMENT

\|

> \|---------- Action Protocol: DGPF CHANGE ASSIGNMENT OWNERSHIP

\|

\|---------- Action Protocol: DGPF DISPLAY ASSIGNMENT DETAIL

> \|

> \|------ List Template: DGPF ASSIGNMENT DETAIL

List Template: DGPF RECORD FLAG MANAGEMENT

\|

\|---------- Menu Protocol: DGPF RECORD FLAG MANAGEMENT MENU

\|

\|---------- Action Protocol: DGPF SORT FLAG LIST

\|

\|---------- Action Protocol: DGPF CHANGE CATEGORY

\|

\|---------- Action Protocol: DGPF ADD FLAG

\|

\|---------- Action Protocol: DGPF EDIT FLAG

\|

\| ---------- Action Protocol: DGPF DISPLAY FLAG DETAIL

> \|

> \|------ List Template: DGPF FLAG DETAIL

## New HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new HL7 APPLICATION PARAMETER(s) will be added.

|       |         |
|-------|---------|
| NAME: | PRF-QRY |

|       |             |
|-------|-------------|
| NAME: | PRF-QRYRESP |

|       |          |
|-------|----------|
| NAME: | PRF-RECV |

|       |          |
|-------|----------|
| NAME: | PRF-SEND |

## New Files/Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of new files being exported with this patch. Records in any of the Patient Record Flag files (#26.11 through \#26.18) should not be added, edited, or deleted except through the installation of national patches or use of the Patient Record Flag software that is part of Registration. Doing so would likely cause the Patient Record Flag database to become corrupted.

|           |                        |              |                                                                                                                                                                                                                                                                                                                          |
|-----------|------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File# | File Name          | Global   | Description                                                                                                                                                                                                                                                                                                          |
| 26.11     | PRF LOCAL FLAG         | ^DGPF(26.11, | This file contains a list of Category II (Local) Patient Record Flags that can be assigned to a patient. Use the Patient Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option to create/edit entries in this file.                                                                                              |
| 26.12     | PRF LOCAL FLAG HISTORY | ^DGPF(26.12, | This file contains the audit information associated with a record in the PRF LOCAL FLAG (#26.11) file. Entries in the PRF LOCAL FLAG HISTORY file are created automatically by the Patient Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option for each creation/edit of a PRF LOCAL FLAG (#26.11) file entry. |
| 26.13     | PRF ASSIGNMENT         | ^DGPF(26.13, | This file contains a list of Patient Record Flag assignments. Use the Patient Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option to create/edit entries in this file.                                                                                                                                         |
| 26.14     | PRF ASSIGNMENT HISTORY | ^DGPF(26.14, | This file contains the audit information associated with a record in the PRF ASSIGNMENT (#26.13) file. Entries in the PRF ASSIGNMENT HISTORY file are created automatically by the Patient Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option for each creation/edit of a PRF ASSIGNMENT (#26.13) file entry. |
| 26.15     | PRF NATIONAL FLAG      | ^DGPF(26.15, | This file contains a list of Category I (National) Patient Record Flags that can be assigned to a patient. Category I flags are established at a National level and any changes to this file or its entries should only be done through a national patch release.                                                        |
| 26.16     | PRF TYPE               | ^DGPF(26.16, | This file contains a list of usage classifications that can be applied to a Patient Record Flag. Additions or modifications to entries in this file should only be done through a national patch release.                                                                                                                |

|       |                          |              |                                                                                                                                                                                                                                                                                  |
|-------|--------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 26.17 | PRF HL7 TRANSMISSION LOG | ^DGPF(26.17, | This file contains a list of all Unsolicited Observation Update (ORU~R01) HL7 transmissions that have been generated at a site by the Patient Record Flags software module. Entries in this file are created/edited automatically by the Patient Record Flags HL7 interface.     |
| 26.18 | PRF PARAMETERS           | ^DGPF(26.18, | This file contains the configuration parameters for the Patient Record Flag module. The file should contain only one record numbered "1". Modifications to the file should only be done through the Patient Record Flag Configuration \[DGPF RECORD FLAG CONFIGURATION\] option. |

There is one new global, ^DGPF for Patient Record Flags. The ^DGPF global contains the following (8) new files.

|             |                          |                 |                            |
|-------------|--------------------------|-----------------|----------------------------|
| File \# | File Name            | Global Root | Journaling Recommended |
| 26.11       | PRF LOCAL FLAG           | ^DGPF(26.11,    | Yes                        |
| 26.12       | PRF LOCAL FLAG HISTORY   | ^DGPF(26.12,    | Yes                        |
| 26.13       | PRF ASSIGNMENT           | ^DGPF(26.13,    | Yes                        |
| 26.14       | PRF ASSIGNMENT HISTORY   | ^DGPF(26.14,    | Yes                        |
| 26.15       | PRF NATIONAL FLAG        | ^DGPF(26.15,    | Yes                        |
| 26.16       | PRF TYPE                 | ^DGPF(26.16,    | Yes                        |
| 26.17       | PRF HL7 TRANSMISSION LOG | ^DGPF(26.17,    | Yes                        |
| 26.18       | PRF PARAMETERS           | ^DGPF(26.18,    | Yes                        |

## New Database Integration Agreement (DBIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following callable entry point is available to external packages by Controlled Subscription to DBIA \#3860 only.

\$\$GETACT^DGPFAPI(DGDFN,DGPRF)

This function call returns the number of active patient record flag assignments for a given patient. If the optional second parameter is passed, then field data from the active assignments is returned that can be used for display and reporting of the assignments. The field data is returned in a two subscript array or global named by the second input parameter. The function sequentially numbers each active assignment starting with one (“1”). The sequential number is used as the first subscript of the return array. The second subscript of the return array is a mnemonic indicating the data that is contained in the array node. The array data is a two-piece circumflex-delimited string, where the first piece is the internal format value and the second piece is the external format value. Word processing array nodes contain two additional subscripts, with the third subscript indicating the line number and the fourth subscript being zero (“0”).

Required Input Parameters: DGDFN

Optional Input Parameters: DGPRF

(DGPRF must be a valid closed root variable or global name passed as a string)

Output Parameters:

DGPRF(nn,”APPRVBY”)

DGPRF(nn,”ASSIGNDT”)

DGPRF(nn,”CATEGORY”)

DGPRF(nn,”FLAG”)

DGPRF(nn,”FLAGTYPE”)

DGPRF(nn,”NARR”,line#,0)

DGPRF(nn”ORIGSITE”)

DGPRF(nn”OWNER”)

DGPRF(nn,”REVIEWDT”)

## New/Modified Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine(s)</strong></td>
<td><strong>New/Modified</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>DG10</td>
<td>Modified</td>
<td>Modified Load/Edit Patient Data option. For a new patient registration a query will occur in real-time and will be sent to the patient's Coordinating Master of Record (CMOR) site. If the local site is the CMOR site, no query will be generated. The query will search for and return all of the patient's ACTIVE and INACTIVE Category I (National) Patient Record Flag Assignments to be filed in the local site's Patient Record Flags database. If an ACTIVE Category I (National) record flag assignment is found for the patient, it will be displayed to the user. The user will then have the ability to view the details of each of the patient's ACTIVE PRF assignments.</td>
</tr>
<tr class="odd">
<td><p>DGPFAA,</p>
<p>DGPFAA1,</p>
<p>DGPFAA2,</p>
<p>DGPFAA3</p></td>
<td>New</td>
<td>Functions and procedures to validate, store and retrieve PRF ASSIGNMENT (#26.13) file data.</td>
</tr>
<tr class="even">
<td><p>DGPFAAH,</p>
<p>DGPFAAH1</p></td>
<td>New</td>
<td>Functions and procedures to validate, store and retrieve PRF ASSIGNMENT HISTORY (#26.14) file data.</td>
</tr>
<tr class="odd">
<td><p>DGPFALF,</p>
<p>DGPFALF1</p></td>
<td>New</td>
<td>Functions and procedures to validate, store and retrieve PRF LOCAL FLAG (#26.11) file data.</td>
</tr>
<tr class="even">
<td>DGPFALH</td>
<td>New</td>
<td>Functions and procedures to validate, store and retrieve PRF LOCAL FLAG HISTORY (#26.12) file data.</td>
</tr>
<tr class="odd">
<td>DGPFANF</td>
<td>New</td>
<td>Function to retrieve PRF NATIONAL FLAG (#26.15) file data.</td>
</tr>
<tr class="even">
<td>DGPFAPI</td>
<td>New</td>
<td>Functions and procedures used by packages and modules external to the Patient Record Flags module.</td>
</tr>
<tr class="odd">
<td>DGPFBGR</td>
<td>New</td>
<td>Background processing driver for review notifications and HL7 Rejection Retransmissions.</td>
</tr>
<tr class="even">
<td>DGPFDD</td>
<td>New</td>
<td>Trigger, executable help and output transform support functions and procedures for all Patient Record Flag files.</td>
</tr>
<tr class="odd">
<td>DGPFHLL</td>
<td>New</td>
<td>Functions and procedures to store and retrieve PRF HL7 TRANSMISSION LOG (#26.17) file data.</td>
</tr>
<tr class="even">
<td><p>DGPFHLQ,</p>
<p>DGPFHLQ1, DGPFHLQ2, DGPFHLQ3</p></td>
<td>New</td>
<td>Functions and procedures for building and parsing QRY~R03 and ORF~R04 HL7 messages.</td>
</tr>
<tr class="odd">
<td>DGPFHLR</td>
<td>New</td>
<td>Driver routine for receiving ORU~R01, ACK~R01, QRY~R03 and ORF~R04 HL7 messages.</td>
</tr>
<tr class="even">
<td>DGPFHLRT</td>
<td>New</td>
<td>Provides procedures for retransmitting rejected PRF ORU~R01 HL7 message.</td>
</tr>
<tr class="odd">
<td>DGPFHLS</td>
<td>New</td>
<td>Driver routine for sending ORU~R01, ACK~R01, QRY~R03 and ORF~R04 HL7 messages.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine(s)</strong></td>
<td><strong>New/Modified</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><p>DGPFHLU,</p>
<p>DGPFHLU1, DGPFHLU2, DGPFHLU3, DGPFHLU4, DGPFHLU5,</p>
<p>DGPFHLU6</p></td>
<td>New</td>
<td>Functions and procedures for building and parsing ORU~R01 and ACK~R01 HL7 messages.</td>
</tr>
<tr class="odd">
<td>DGPFHLUT</td>
<td>New</td>
<td>Utility and support functions for all Patient Record Flags HL7 interfaces.</td>
</tr>
<tr class="even">
<td>DGPFLF</td>
<td>New</td>
<td>Entry point for DGPF RECORD FLAG MANAGEMENT List Template.</td>
</tr>
<tr class="odd">
<td>DGPFLF1</td>
<td>New</td>
<td>Display builder procedures for the DGPF RECORD FLAG MANAGEMENT List Template.</td>
</tr>
<tr class="even">
<td>DGPFLF2</td>
<td>New</td>
<td>Entry points for the DGPF SORT FLAG LIST, DGPF CHANGE FLAG LIST, and DGPF DISPLAY FLAG DETAIL action protocols for the DGPF RECORD FLAG MANAGEMENT List Template.</td>
</tr>
<tr class="odd">
<td>DGPFLF3</td>
<td>New</td>
<td>Entry point for the DGPF ADD FLAG action protocol.</td>
</tr>
<tr class="even">
<td><p>DGPFLF4,</p>
<p>DGPFLF5</p></td>
<td>New</td>
<td>Entry point for the DGPF EDIT FLAG action protocol.</td>
</tr>
<tr class="odd">
<td>DGPFLF6</td>
<td>New</td>
<td>Support functions for the DGPF RECORD FLAG MANAGEMENT List Template.</td>
</tr>
<tr class="even">
<td><p>DGPFLFD,</p>
<p>DGPFLFD1</p></td>
<td>New</td>
<td>Entry point and display builder for DGPF FLAG DETAIL display List Template.</td>
</tr>
<tr class="odd">
<td>DGPFLMA</td>
<td>New</td>
<td>Entry point for DGPF RECORD FLAG ASSIGNMENT List Template.</td>
</tr>
<tr class="even">
<td>DGPFLMA1</td>
<td>New</td>
<td>Entry points for the DGPF SELECT PATIENT and DGPF DISPLAY FLAG action protocols for the DGPF RECORD FLAG ASSIGNMENT List Template.</td>
</tr>
<tr class="odd">
<td>DGPFLMA2</td>
<td>New</td>
<td>Entry point for DGPF ASSIGN FLAG action protocol of the DGPF RECORD FLAG ASSIGNMENT List Template.</td>
</tr>
<tr class="even">
<td>DGPFLMA3</td>
<td>New</td>
<td>Entry point for DGPF EDIT FLAG ASSIGNMENT action protocol of the DGPF RECORD FLAG ASSIGNMENT List Template.</td>
</tr>
<tr class="odd">
<td>DGPFLMA4</td>
<td>New</td>
<td>Entry point for DGPF CHANGE ASSIGNMENT OWNERSHIP action protocol of the DGPF RECORD FLAG ASSIGNMENT List Template.</td>
</tr>
<tr class="even">
<td>DGPFLMAD, DGPFLMU, DGPFLMU1</td>
<td>New</td>
<td>Entry point and display builder for the DGPF ASSIGNMENT DETAIL display List Template.</td>
</tr>
<tr class="odd">
<td><p>DGPFLMD,</p>
<p>DGPFLMD1</p></td>
<td>New</td>
<td>Entry point for the DGPF ACTIVE ASSIGNMENTS List Template.</td>
</tr>
<tr class="even">
<td>DGPFPARM</td>
<td>New</td>
<td>Entry/Edit procedure for maintaining the PRF PARAMETERS (#26.18) file and functions to verify enabled/disabled status of PRF module and HL7 interfaces.</td>
</tr>
<tr class="odd">
<td><p>DGPFRFA,</p>
<p>DGPFRFA1</p></td>
<td>New</td>
<td>Flag Assignment report prompts and builder.</td>
</tr>
<tr class="even">
<td><p>DGPFRFR,</p>
<p>DGPFRFR1</p></td>
<td>New</td>
<td>Flags Due for Review report prompts and builder.</td>
</tr>
<tr class="odd">
<td><p>DGPFUT,</p>
<p>DGPFUT1,</p>
<p>DGPFUT2</p></td>
<td>New</td>
<td>General support functions and procedures used by all Patient Record Flags interfaces.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine(s)</strong></td>
<td><strong>New/Modified</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>DGREG</td>
<td>Modified</td>
<td>Modified Register a Patient option. For a new patient registration a query will occur in real-time and will be sent to the patient's Coordinating Master of Record (CMOR) site. If the local site is the CMOR site, no query will be generated. The query will search for and return all of the patient's ACTIVE and INACTIVE Category I (National) Patient Record Flag Assignments to be filed in the local site's Patient Record Flags database. If an ACTIVE Category I (National) record flag assignment is found for the patient, it will be displayed to the user. The user will then have the ability to view the details of each of the patient's ACTIVE PRF assignments.</td>
</tr>
<tr class="odd">
<td>DGRPT</td>
<td>Modified</td>
<td>Modified 10-10T Registration option. For a new patient registration a query will occur in real-time and will be sent to the patient's Coordinating Master of Record (CMOR) site. If the local site is the CMOR site, no query will be generated. The query will search for and return all of the patient's ACTIVE and INACTIVE Category I (National) Patient Record Flag Assignments to be filed in the local site's Patient Record Flags database. If an ACTIVE Category I (National) record flag assignment is found for the patient, it will be displayed to the user. The user will then have the ability to view the details of each of the patient's ACTIVE PRF assignments.</td>
</tr>
<tr class="even">
<td>DGSEC</td>
<td>Modified</td>
<td>The custom patient lookup module in VistA has been modified. When a patient lookup is performed on a patient having ACTIVE Patient Record Flag assignments, the flags assigned to the patient will be displayed. Once the ACTIVE flags assigned to the patient are displayed, users will have the ability to view the assignment narrative and the details associated with each flag assignment.</td>
</tr>
<tr class="odd">
<td>DG53P425</td>
<td>New</td>
<td><p>This ENV/PRE/POST installation routine will create PRF PARAMETERS file (#26.18) entry at IEN "1". This file contains all the configuration parameters for the Patient Record Flag module. This routine also creates the Category I (National) BEHAVIORAL flag entry in the (PRF NATIONAL FLAG #26.15) file. This flag will be used to assign a National Record Flag to a patient that will be shared to all sites of record for the patient.</p>
<p>(may be deleted after successful patch installation)</p></td>
</tr>
</tbody>
</table>

## Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Record Flag Background \[DGPF BACKGROUND PROCESSING\] option is the main driver for Patient Record Flag background processes.

Using the SCHEDULE/UNSCHEDULE OPTIONS \[XUTM SCHEDULE\] option, it is recommended to schedule this option to run daily (i.e., RESCHEDULING FREQUENCY: D@2AM).

The following functions are processed by this background option.

1\. Send review notification messages for pending Patient Record Flag Assignment reviews

This process searches the PRF ASSIGNMENT file (#26.13) for Patient Record Flag assignments that are due for review of appropriateness. A MailMan message will be generated to the mail group associated with the record flag, notifying the members of the pending review.

2\. Auto retransmitting of rejected HL7 Patient Record Flag Assignment messages

This process searches the "ASTAT" cross reference of the PRF HL7 TRANSMISSION LOG file (#26.17) looking for transmissions with a status of REJECTED ("RJ"). A new HL7 message will be transmitted to all sites of record for the patient’s record flag assignment.