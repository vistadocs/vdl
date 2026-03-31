---
title: Event Capture Version 2.0 GUI User Guide (Updated EC*2*170)
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: GUI  (Updated EC*2*170)
app_code: EC
app_name: Event Capture System (ECS)
section: FIN
app_status: active
pkg_ns: EC
patch_ver: 2.0
patch_id: EC*2.0
group_key: "EC:EC:2.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - event
  - span
  - figure
  - capture
  - procedure
  - report
  - code
  - class
  - updated
  - unit
page_count: 0
word_count: 37232
section_count: 24
table_count: 1
figure_count: 9
appendix_count: 2
has_toc: False
is_stub: False
pub_date: May 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Event_Capture/ec_2_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Event_Capture/ec_2_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=39"
---

Event Capture System 2.0

Graphical User Interface

User Guide

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/001.png)

May 2025

Office of Information and Technology

Revision History

<table>
<caption><p><span id="_Ref94693184" class="anchor"></span>Table 1: Tier Support Contact Information</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 53%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>05/2025</td>
<td>2.8</td>
<td><p><strong>Updated for EC*2.0*170</strong></p>
<p>4.4.2.3 — Updated information for Step 8.</p>
<p>Figure 221: Add Event Code Screen was updated</p>
<p>4.4.7.5 — Updated Step 3, Step 5, and Figure 235: Copy Event Code Screen to DSS Unit</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>08/2024</td>
<td>2.7</td>
<td><p><strong>Updated for EC*2.0*169</strong></p>
<p>Updated release date and patch number</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>04/2024</td>
<td>2.6</td>
<td><p><strong>Updated for EC*2.0*165</strong></p>
<p>Updated release date and patch number</p>
<p>Removed outdated Index</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>10/2023</td>
<td>2.5</td>
<td><p><strong>Updated for EC*2.0*164</strong></p>
<p>Updated release date and patch number</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>06/2023</td>
<td>2.4</td>
<td><p><strong>Updated for EC*2.0*159</strong></p>
<p>Updated release date and patch number</p>
<p>Language was updated in the <a href="#introduction">Introduction</a> regarding the target audience for this document.</p>
<p>3 – Removed last bullet item to note in Step 5.</p>
<p>3 — Updated Figure 2: Grant Access to DSS Units by User</p>
<p>3.2 — Added content and image for ECACCESS security key.</p>
<p>4.1.1.2 – Updated Figure 31: Add Patient Procedure Detail Screen</p>
<p>4.1.1.3 — Added note for Diagnoses, Updated Problem List content</p>
<p>4.1.1.4 — Updated content related to adding multiple procedures</p>
<p>4.1.1.5 — Added new section: Add Multiple Patient Procedures; instructions and 6 figures</p>
<p>4.1.1.6 — Updated Figure 48: Edit Patient Procedure Screen</p>
<p>4.1.3 — Updated all figures for <a href="#multiple-datesmultiple-procedures">Multiple Dates Multiple Procedures</a> screens</p>
<p>4.1.3.3 — Added note to Step 7.</p>
<p>4.2.1.1 — Added Secondary Diagnosis field information, Sec Dx1 – Sec Dx 4</p>
<p>4.2.1.3, Step 2. — Added secondary diagnosis field names to list of spreadsheet headers</p>
<p>Updated twenty-six (26) <a href="#reports">report</a> selection screens to display new report names: Procedures by Clinic, and Event Capture Edit Log</p>
<p>4.3.1.10 — Procedure Summary Report: updated Preview and Export screen shots</p>
<p>Added section for new report: <a href="#procedures-by-clinic-report">Procedures by Clinic</a></p>
<p>Added Section for new report: <a href="#event-capture-edit-log-report">Event Capture Edit Log</a></p>
<p>4.4.3.1 — Updated Section: Assign User Access to DSS Units</p>
<p>4.4.7.2 — Add Event Code Screens: Updated existing screen shot to display new Add button. Updated content. Added new screenshot for clarity.</p>
<p>Added <strong>note</strong> to the following sections for diagnosis selection functionality:</p>
<blockquote>
<p>4.1.1.3, Step 11.</p>
<p>4.1.2.1, Step 15.</p>
<p>4.1.3.4, Step 7.</p>
</blockquote></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>11/2022</td>
<td>2.3</td>
<td><p><strong>Updated for EC*2.0*161</strong></p>
<p>Updated release date and patch number</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>07/2022</td>
<td>2.2</td>
<td><p><strong>Updated for EC*2.0*158</strong></p>
<p>Updated release date and patch number</p>
<p>Moved Step 11. in Add a Patient Procedure, for clarity</p>
<p>Modified Step 11. in Enter Information on the Add or Edit Patient Procedure Screens, for clarity</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>02/2022</td>
<td>2.1</td>
<td><p><strong>Updated for EC*2.0*156</strong></p>
<p><strong>Updated Sections:</strong></p>
<p>3 – Added note to Step 5.</p>
<p>4.1.1.1 – Added bullet item to Note in Step 5.</p>
<p>4.1.1.2 – Added clinic note in Step 2</p>
<p>4.1.1.3 – Updated Step 11. <em>Select the associated diagnosis code for the procedure</em>; Added bullet for Problem List details; Added clinic note in Step 10</p>
<p>4.1.2.1 – Updated Step 15. <em>Select the associated diagnosis code for the procedure</em>; Added clinic note to Step 14</p>
<p>4.1.3.4 – Updated Step 7. <em>Select the associated diagnosis code for the procedure</em>; Added clinic note to Step 6</p>
<p>4.3.1 – Added “Procedure Summary Report” to list of reports available to all users</p>
<p>4.3.1.10 – Added section “Procedure Summary Report”</p>
<p>4.4.2 – Added sentence to intro paragraph regarding option to Delete a DSS Unit</p>
<p>4.4.2.1 – Added Section “Delete a DSS Unit”</p>
<p>4.4.2.2 – Added Notes to Step 11. ; Updated Step 12. and Step 13. re: Send to PCE selection</p>
<p>4.4.2.3 – Updated Step 12. Choose the appropriate Send to PCE option</p>
<p>4.4.2.5 – Added bullet item to Note in Step 4.</p>
<p>4.4.7 – Added sentence to intro paragraph regarding option to delete Event Code Screens</p>
<p>4.4.7.1 – Added Section “Delete Event Code Screens”</p>
<p>4.4.7.2– Added clinic note to Step 3.</p>
<p>4.4.7.3 – Added clinic note to Step 3.</p>
<p><a href="#ExampleMessageDeleteDSSUnit">Appendix C</a> – Added content and images for when a DSS Unit or an Event Code Screen is deleted</p>
<p><strong>Changes in Figures/Tables:</strong></p>
<p>Updated Figure 31</p>
<p>Added Figure 35</p>
<p>Updated Figure 39</p>
<p>Updated Figure 48</p>
<p>Updated Figure 53</p>
<p>Added Figure 56</p>
<p>Updated Figure 63</p>
<p>Added Figure 65</p>
<p>Updated Figure 68</p>
<p>Added Figure 116, Figure 117, and Figure 118</p>
<p>Updated Table 2 (Clarified Associated Stop Code, Credit Stop Code, and CHAR4 Code)</p>
<p>Added Figure 185</p>
<p>Added Figure 187</p>
<p>Added Figure 190</p>
<p>Added Figure 219</p>
<p>Updated Figure 227 and Figure 228</p>
<p>Updated Figure 232 and Figure 233</p>
<p>Added Figure 252 and Figure 253</p>
<p>Updated All Report Selection Screens to include new report name</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>04/2021</td>
<td>2.0</td>
<td><p>Updated for EC*2.0*152</p>
<p>Updated Formatting</p>
<p>Updated for Compliance with Current OIT Style Guide</p></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>05/2020</td>
<td>1.0</td>
<td>Initial Release</td>
<td>Liberty IT Solutions</td>
</tr>
</tbody>
</table>

<span id="_Ref94693184" class="anchor"></span>Table 1: Tier Support Contact Information

Table of Contents

Table of Figures

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the Guide](#organization-of-the-guide)
    - [Assumptions](#assumptions)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operations](#continuity-of-operations)
  - [Section 508 Compliance](#section-508-compliance)
    - [Screen Readers](#screen-readers)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
    - [Authentication via CPRS SSO](#authentication-via-cprs-sso)
    - [Authentication via CCOW SSO](#authentication-via-ccow-sso)
    - [Authentication via Personal Identification Verification](#authentication-via-personal-identification-verification)
    - [Authentication via Access and Verify Codes](#authentication-via-access-and-verify-codes)
  - [Event Capture Main Menu](#event-capture-main-menu)
    - [Icon Shortcuts](#icon-shortcuts)
    - [Menu Bar](#menu-bar)
    - [Delete Test Patient Data](#delete-test-patient-data)
  - [Menu Bar for Specific Functions](#menu-bar-for-specific-functions)
    - [Data Entry Menu Bar](#data-entry-menu-bar)
    - [Spreadsheet Menu Bar](#spreadsheet-menu-bar)
    - [Reports Menu Bar](#reports-menu-bar)
    - [Management Menu Bars](#management-menu-bars)
  - [Changing User ID and Password](#changing-user-id-and-password)
  - [Exit System](#exit-system)
  - [Caveats and Exceptions](#caveats-and-exceptions)
  - [Online Documentation](#online-documentation)
  - [Timeout Feature](#timeout-feature)
- [Using the Software](#using-the-software)
  - [Data Entry Menu](#data-entry-menu)
    - [Data Entry by Patient](#data-entry-by-patient)
    - [Data Entry by Procedure](#data-entry-by-procedure)
    - [Multiple Dates/Multiple Procedures](#multiple-datesmultiple-procedures)
  - [Spreadsheet](#spreadsheet)
    - [Import a Regular Spreadsheet](#import-a-regular-spreadsheet)
    - [Import a State Veterans Home Spreadsheet](#import-a-state-veterans-home-spreadsheet)
    - [Upload Imported Spreadsheet Data](#upload-imported-spreadsheet-data)
    - [Upload Completion](#upload-completion)
  - [Reports](#reports)
    - [Reports Available to All Users](#reports-available-to-all-users)
    - [Reports Available to ECMGR Key Holders Only](#reports-available-to-ecmgr-key-holders-only)
  - [Management Menu](#management-menu)
    - [Location — Update Location Information](#location-update-location-information)
    - [DSS Units](#dss-units)
    - [Access by User — Grant Access to DSS Units by User](#access-by-user-grant-access-to-dss-units-by-user)
    - [Category — Add or Update Categories](#category-add-or-update-categories)
    - [Procedure — Add or Update Local Procedures](#procedure-add-or-update-local-procedures)
    - [Reason — Add or Update Procedure Reasons](#reason-add-or-update-procedure-reasons)
    - [Event Code Screens](#event-code-screens)
    - [Inactivate EC Screen — Identify Inactive Multiple Event Code Screens](#inactivate-ec-screen-identify-inactive-multiple-event-code-screens)
    - [Providers — Maintain Non-Licensed Providers](#providers-maintain-non-licensed-providers)
- [Troubleshooting](#troubleshooting)
  - [Access Issues](#access-issues)
  - [Log-On Issues](#log-on-issues)
  - [GUI Appears Distorted](#gui-appears-distorted)
    - [Example of Setting the Screen Resolution to 1920 x1080](#example-of-setting-the-screen-resolution-to-1920-x1080)
The *Event Capture System (ECS) Graphical User Interface (GUI) User Guide* provides instructions for using the Event Capture options within the GUI setting. The target audience for this manual includes the users of the Event Capture package, Tier 2 VistA Support Application Coordinators (ACs), and other software users.
The GUI provides a consistent, event-driven, Windows® style user interface for Event Capture.
The Event Capture software provides a mechanism to track and account for procedures and delivered services that other Veterans Health Information Systems and Technology Architecture (VistA) packages do not handle. The procedures and services tracked through Event Capture are associated with the following:
- The patient to whom they were delivered
- The provider requesting the service or procedure
- The Decision Support System (DSS) Unit responsible for delivering the service
DSS Units typically represent the smallest identifiable work unit in a clinical service at a medical center. Veterans Affairs Medical Centers (VAMCs) define the DSS Units. A DSS Unit can represent any of the following:
- An entire service
- A section of a service
- A small section within a section
- A medical equipment item used in patient procedures
The user must define the following items for every DSS Unit:
- Service: The service associated with the DSS Unit.
- Cost Center: The fiscal identifier for the service using the DSS Unit.
  Cost Centers are defined in detail in *Volume XIII —Cost Accounting* of the Financial Policy Volumes on the VA’s Office of Financial Policy web site.
- Medical Specialty: The specialty section associated with the DSS Unit.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECS GUI *User Guide* is intended for use as an instructional guide for using the Event Capture software. The user can use this manual in conjunction with the Event Capture GUI online help option.

Screen displays may vary among different sites, and the data may not appear on the monitor exactly as shown in this manual. Although ECS screens are subject to modification, the major menu options as they appear in this manual are fixed and are not subject to modification (except by the package developer).

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sub-paragraphs provide general information about how to use this document.

### Organization of the Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is organized into the following major sections:

[Introduction](#introduction) — This section provides a brief description of the purpose of the guide and an orientation into the document’s structure and use.

[System Summary](#_System_Summary) — This section provides a general description of the system written in non-technical terminology, the purpose for which the system is intended, the system configuration, data flows, user access and continuity of operations.

[Getting Started](#_Getting_Started) — This section provides a general walkthrough of the system from initiation through exit. The logical arrangement of the information enables functional personnel to understand the sequence and flow of the system.

*[Using the Software](#_Using_the_Software) —This section serves as reference to the user, covering vital aspects of this t*ool.

- Data Entry — ECS is programmed to allow the users to enter records and edit specific fields.
- Spreadsheet — ECS allows the uploading of data through spreadsheets. There are two types of spreadsheets: Regular Spreadsheets and State Veterans Home Spreadsheets. Information for both types is included in this guide.
- Reports — ECS Reports are designed according to Managerial Cost Accounting Office (MCAO) specifications. Users have the option of previewing the report, exporting the report into an Excel spreadsheet, or printing a hardcopy. Some reports are only accessible to users with the manager security key (ECMGR).
- Management Menu — This option accesses the menus needed for management of the Event Capture software. It includes, but is not limited to, allocation of DSS Units, assignment of users to DSS units, addition of local procedures and categories, and the creation of Event Code Screens.

[Troubleshooting](#_Troubleshooting) — This section provides general troubleshooting advice on issues encountered by users.

[Appendix](#acronyms-and-abbreviations) — The following appendices are included in this guide:

- Acronyms and Abbreviations — This section provides the user with a list of abbreviations and acronyms used throughout the document.
- Glossary — This section provides the user with definitions of terms used throughout the document.
- ECS Package Administrative Messages — This section provides the user with examples of relevant ECS notifications.
- Index — This section provides the user with an Index of major topics of interest.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, menus, and security keys required for ECS.
- User is using ECS to perform his/her job.
- User has validated access to ECS.
- User has completed any prerequisite training.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following disclaimers apply to all Department of Veterans Affairs (VA) user documentation.

#### Software Disclaimer

This software was developed at the VA by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code, this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this guide does not constitute endorsement by the VA of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To avoid displaying sensitive information regarding patients and staff, the examples in this guide contain pseudonyms or scrambled data instead of real names. Patients and staff will be referred to as “ECPATIENT, ONE”, “AAECPROVIDER, ONE”, or “USER, ONE.” Scrambled data are a series of random letters that replace a real name (e.g., “AAADY, JWHTRE”). Likewise, real social security numbers (SSNs), real addresses, and other personal identifiers are not used.

Note

- Many examples of previews or exported reports in this manual will only include a portion of the output produced for the purpose of saving space and maintaining clarity.
- Internal document links and VDL links in this manual are displayed in blue type.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation for Event Capture v2.0 includes the following:

- *Event Capture Deployment, Installation, Back-out and Rollback Guide* (DIBRG)
- *Event Capture Patch Description* (PD)
- *Event Capture Technical Manual* (TM)

These documents can be found on the [VA Software Document Library (VDL)](https://www.va.gov/vdl/) website.

Patch information and documentation is also available online at the MCA Learning Community for Event Capture website.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The three tiers of support documented herein are intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

Table 1 lists organizational contacts needed by site users for troubleshooting purposes. Support contacts are listed by name of service responsible to fix the problem, description of the incident escalation, associated tier level, and contact information (email and phone number).

<table>
<caption><p><span id="_Ref94777266" class="anchor"></span>Table 2: Element Name and Description</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Role</th>
<th>Org</th>
<th>Contact Info</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Local ECS Package Manager</td>
<td>Tier 0 Support</td>
<td>Veterans Health Administration (VHA)</td>
<td><p>ECS Package Manager/Site Dependent</p>
<p>The MCAO Phone List can be found on the VA’s MCAO online contact page.</p></td>
</tr>
<tr class="even">
<td>Local Managerial Cost Accounting (MCA) VISN Coordinator</td>
<td>Tier 0 Support</td>
<td>VHA</td>
<td><p>Site Dependent</p>
<p>The MCAO Phone List can be found on the VA’s MCAO online contact page.</p></td>
</tr>
<tr class="odd">
<td>OIT National Service Desk</td>
<td>Tier 1 Support</td>
<td>OIT</td>
<td><p>National Service Desk</p>
<p>Incident Management Automated Notification Reporting (ANR) Tool</p></td>
</tr>
</tbody>
</table>

<span id="_Ref94777266" class="anchor"></span>Table 2: Element Name and Description

<span id="_System_Summary" class="anchor"></span>

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Event Capture System (ECS) is a VistA Class I workload reporting system supporting operations of the VA MCAO. There are several VHA national programs mandating utilization of ECS in place of, or to augment, other workload capture information systems. For example, ECS is leveraged when programs cannot report workload in the form of Current Procedural Terminology (CPT) codes. Other times, ECS allows for more precise workload capture and reporting than otherwise possible through another VistA system.

Event Capture with all patches installed provides the following functions:

- Allows each VAMC to utilize the software for its own resource/costing needs
- Implements DSS Units
- Assigns user access
- Allows single and batch data entry for patient procedures
- Generates reports for workload and other statistical tracking
- Provides a graphical user interface (GUI) to the ECS application
- Allows user to upload patient encounter data to Event Capture from a spreadsheet
- Allows user to switch between Computerized Patient Record System (CPRS) and ECS without having to log back into the Event Capture (EC) GUI.exe

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the [*Event Capture Technical Manual*](#references-and-resources) for details related to system and site configuration.

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ECS captures both inpatient and outpatient workload and uses VHA-wide standardized procedures which help aid benchmarking and workload analysis. ECS captures basic resource utilization data, creates monthly extracts, and electronically transmits to DSS, Patient Care Encounter (PCE), and billing offices for processing which facilitates workload analysis, cost analysis, and transmission of billing.

Figure 1 represents the ECS data flow.

<span id="_Ref95142780" class="anchor"></span>Figure 1: ECS Data Flow Diagram

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/002.png)

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security keys are assigned in VistA using the option Key Management main menu and then choosing the submenu Allocation of Security Keys.

ECS provides the following security key options for user access:

- ECMGR: Gives a user access to the ECS Management Menu — only for Event Capture managers.
- ECACCESS: Gives a user the ability to grant or remove access to DSS Units that they have access to. Note that if the user also has the ECMGR key, ECACCESS will not have any effect.
- ECALLU: Gives a user access to all DSS Units (super user). This key should be assigned only to those managing the software (i.e., holders of the ECMGR key).
- ECNORPT: Restricts the user from accessing Event Capture reports.
- ECSPSH: Gives a user access to upload data from a spreadsheet (required for State Veterans Home Spreadsheet upload).

## Continuity of Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each site has a backup emergency plan in place in the event that the system goes down.

## Section 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 508 of the Rehabilitation Act Amendments of 1998 requires that when Federal agencies develop, procure, maintain, or use electronic and information technology, they shall ensure that the electronic and information technology enables persons with disabilities to have access to, and use of, information and data that is comparable to the access to and use of information and data by persons who are not individuals with disabilities, unless an undue burden would be imposed on the agency.

The Section 508 Accessibility Testing and Training Center (T&TC) was consulted and modifications to the GUI have been made to meet the requirements for Section 508 compliance. Event Capture was modified to enable screen readers to accurately interpret information on the screens. As a result, some buttons and boxes have been moved, replaced, or renamed, and some screen titles have been modified.

For more information on the VA Section 508 compliance efforts, please visit the Section 508 website.

### Screen Readers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ECS has been evaluated for the accessibility of application content with multiple commercial screen readers. ECS has been tested to ensure all screens work properly when a screen reader is active.

<span id="_Getting_Started" class="anchor"></span>

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Event Capture must be set up by using the options in the Event Capture Management Menu before any data can be entered. Access to this menu should be restricted to the ADPAC or Event Capture Package Manager and his/her designees. The Event Capture ADPAC should use the following steps as a guide for setting up the Event Capture software.

1.  Select security keys.
- See section 2.3 regarding User Access Levels for a description of ECS security keys.
2.  Select required VistA settings.
- Users must be assigned the EC GUI CONTEXT VistA menu option for the ECS GUI to work.
3.  Create an Event Capture Location.
- Create a location using the Location — Update Location Information option.

> **NOTE:** - The selected location must be in the INSTITUTION file (#4).

- At least one location must exist before DSS Units can be established.
4.  Establish DSS Units for each service.
- Contact each service for a list of its DSS Units, the names of its Event Capture users and the DSS Units for which they will enter data, and for individual product resource tracking needs.
- Use the DSS Unit — Add or Update DSS Units option to establish DSS Units for each service.

> **NOTE:** - At least one DSS Unit must exist before Event Code Screens can be created.

5.  Assign user access to specific DSS Units.
- Use the Access by User — Grant Access to DSS Units by User option (Figure 2) to assign user access to specific DSS Units for the users identified in Step 4.
- Assign the ECALLU security key only to those users who should have access to all DSS Units.

> **NOTE:** - Users must have access to DSS Units before they can begin entering data.

- Use the Access by User — Grant Access to DSS Units by User option to remove user access for a specific DSS Unit. Users with the ECALLU security key cannot be denied access to DSS Units.

<span id="_Ref100840860" class="anchor"></span>Figure 2: Grant Access to DSS Units by User

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/003.png)

6.  Create Categories.
- Use the Category — Add or Update Categories option to create categories before the user sets up Event Code Screens.

> **NOTE:** - Creating categories is optional.

- After completion of this step, the Category Report option on the Reports Menu can be used to print a report of the site’s categories.
7.  Create or edit local procedures in the EC NATIONAL PROCEDURE file (#725).
- Use the Procedure — Add or Update Local Procedures option to enter new, or edit existing, local procedures in the EC NATIONAL PROCEDURE file (#725).
- Adding local procedures is optional and not encouraged.

> **NOTE:** - Before starting this step, use the National/Local Procedure Report option on the Reports Menu to print a list of procedures with their associated CPT codes. This report can be quite lengthy if it includes national procedures, so it should be queued to print to a device during non-peak hours.

- An associated CPT code must be entered to pass local procedures to PCE.
- Use this option to edit, but not delete, existing local procedures and to select an associated CPT code if this workload data should be sent to PCE.
8.  Use the Event Code Screen — Add or Update Event Code Screens option to:
- Create an Event Code Screen for each procedure tracked in the Event Capture software.
- Enter or edit an optional active associated clinic for DSS Units that are marked to send data to PCE. If an Associated Clinic has non-conforming stop codes, the clinic will not be selectable.
- Enter or edit an optional procedure Synonym.
- Set Ask Reasons? radio button to Yes or No.
- Enter or edit procedure default Volume.

> **NOTE:** - An Event Code Screen for the procedure must be created before it can be used for data entry.

9.  Optional: Print the Event Code Screens Sorted by DSS Units
- Use the Print Category and Procedure Summary (Report) option on the Reports Menu to print the Event Code Screens sorted by DSS Units.

> **NOTE:** - Data entry clerks might find the output generated by this report useful as a procedure reference guide.

10. Event Capture set up is complete.
- Services can now enter data using the Data Entry options and provide summary reports using the Reports options.

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Event Capture is accessed through a desktop shortcut that points to the location of the EC GUI application (Figure 3). The executable file will be located on either a local or shared network drive. If the shortcut does not appear, refer to the Installation Guide for Event Capture, or ask the local support staff for assistance.

<span id="_Ref94693493" class="anchor"></span>Figure 3: ECS GUI Icon

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/004.png)

1.  Double-click the EC GUI shortcut to launch the application.

Once Event Capture is launched, there are 4 methods of providing user authentication:

- Single Sign-On (SSO) through CPRS
- Clinical Context Object Workgroup (CCOW)
- Personal Identification Verification (PIV) with Two-Factor Authentication (2FA)
- Access and Verify codes

### Authentication via CPRS SSO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ECS user authentication can be achieved via SSO through CPRS. This design is intended to increase the use of Event Capture by clinicians currently using CPRS.

The interface between CPRS and Event Capture enables users to access Event Capture from within CPRS through single sign-on. This is achieved by selecting the Event Capture Interface in the CPRS Tool Menu which allows the user to enter Event Capture patient procedures. When accessing Event Capture in this way, both user and patient context are maintained. This CPRS feature requires set up by the local Office of Information and Technology (OIT) and/or the Clinical Application Coordinator.

### Authentication via CCOW SSO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Event Capture includes CCOW SSO capability. If a user is signed onto another CCOW SSO-enabled system, launching Event Capture will not require the user to re-enter system Access and Verify codes. Likewise, if CCOW is enabled in Event Capture, other CCOW SSO compliant applications can use the current user’s authentication credentials from Event Capture. The status of the CCOW SSO is shown via an icon on a panel in the upper-right hand corner of the Main Menu (Figure 4). The hover help will display “Clinical Link On” if Event Capture was accessed with CCOW SSO enabled or “Clinical Link Off” if it was not. In addition, the icon on the panel will indicate current CCOW status. The CCOW feature requires set up by the local OIT.<span id="_Hlk94693553" class="anchor"></span>

Figure 4: Event Capture CCOW Status

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/005.png)

### Authentication via Personal Identification Verification 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two-Factor Authentication adds an additional layer of security beyond a traditional username and password combination. Event Capture can obtain credentials from a PIV card and Personal Identification Number (PIN) combination. When Event Capture is first launched, it will attempt to use a PIV card for authentication.

1.  Select your PIV card certificate (Figure 5):

<span id="_Ref94693644" class="anchor"></span>Figure 5: PIV Certificate Selection

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/006.png)

11. Enter the PIN and press the OK button (Figure 6)

<span id="_Ref94693698" class="anchor"></span>Figure 6: PIN Entry

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/007.png)

If PIV authentication is successful, the System Use Notification will appear (Figure 7). Click the OK button to complete the login process.

If PIV authentication fails, the prompt for Access and Verify codes will appear.

<span id="_Ref94693756" class="anchor"></span>Figure 7: System Use Notification

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/008.png)

### Authentication via Access and Verify Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If PIV authentication fails, authentication will revert to the traditional Access and Verify code method of VistA login (Figure 8). When this happens, enter valid Access and Verify codes, and click the OK button.

<span id="_Ref94694930" class="anchor"></span>Figure 8: VistA Login Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/009.png)

## Event Capture Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Event Capture software contains five possible main menu options. The availability of those options is dependent on the keys assigned to the user:

1.  Data Entry — All users have access to the Data Entry option.
1.  Spreadsheet — The user must hold the ECSPSH security key to have access to the Spreadsheet option.
2.  Reports — Users with the ECNORPT security key will *not* have access to the Reports option (Figure 10).
3.  Management Menu — The user must hold the ECMGR security key to have access to the Management Menu functions (Figure 9). Users without the ECMGR security key will have fewer reports available for selection than users with the ECMGR security key.
4.  Access by User — Users with the ECACCESS security key, but not the ECMGR security key, will have access to the Access by User option (Figure 11).

<span id="_Ref94696076" class="anchor"></span>Figure 9: User Holds the ECSPSH and ECMGR Security Keys

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/010.png)

<span id="_Ref94696195" class="anchor"></span>Figure 10: User Holds the ECSPSH, ECNORPT and ECMGR Security Keys

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/011.png)

<span id="_Ref129974886" class="anchor"></span>Figure 11: User Holds the ECSPSH and ECACCESS Security Keys

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/012.png)

### Icon Shortcuts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A toolbar is available with icons to access frequently used options quickly from the Main Menu in Event Capture (Figure 10).

Before the User Starts

- Only users with the ECSPSH security key will see the Go to the Spreadsheet Menu toolbar option.
- Only users without the ECNORPT security key will see the Go to the Reports Menu toolbar option.
- Only users with the ECMGR security key will see the Go to the Management Menu toolbar option.
- Only users with the ECMGR security key will see the Delete Test Patient Data toolbar option.

What the User Will See

- Under the menu bar on the ECS Main Menu, the toolbar presents the most frequently used options (Figure 12).
- The number of toolbar options visible will depend upon the individual user’s security key assignment.

<span id="_Ref94696251" class="anchor"></span>Figure 12: Icon Shortcuts

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/013.png)

### Menu Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Event Capture menu bar (Figure 13) enables the user to access shortcut commands.

<span id="_Ref94696324" class="anchor"></span>Figure 13: Main Menu Bar

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/014.png)

Before the User Starts

- Only users with the ECSPSH security key will see the Go to the Spreadsheet Menu toolbar option.
- Only users without the ECNORPT security key will see the Reports Menu option under the Function Menu.
- Only users with the ECMGR security key will see the Management Menu option under the Function Menu.
- Only users with the ECMGR security key will see the Delete Test Patient Data option under the Function Menu.

What the User Will See

- Under the Event Capture title bar on the ECS Main Menu, the menu bar presents the top-level commands (Figure 11).
- The File menu item enables the user to Exit the application.
- The Function menu item on the main window provides access to:
- Data Entry
- Spreadsheet (if the user has the proper security key)
- Reports (if the user has the proper security key)
- Management Menu (if the user has the proper security key)
- Delete Test Patient Data (if the user has the proper security key)
- The View menu item enables the user to show or hide the Toolbar and Status Bar.
- The Help menu item provides topic-specific help, or information about the Event Capture system.

Figure 14 displays the menu bar options with expanded menus.

<span id="_Ref94696381" class="anchor"></span>Figure 14: Main Menu Bar with Menus Expanded

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/015.png)

### Delete Test Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Main Menu provides management users the ability to delete test patient data. Running this option ensures that reports will not contain test patient data.

Before the User Starts

- Only users with the ECMGR security key will have access to the Delete Test Patient Data option.
- The Delete Test Patient Data option is only available on the ECS Main Menu.
- Test patient data entered for DSS Units CH103-109 is excluded from deletion when running this option.

What the User Will See

- After selecting the Delete Test Patient Data option from the ECS Main Menu (menu bar or toolbar), a Delete Test Patient dialog box will display (Figure 15).
- The Delete Test Patient dialog box informs the user to which account he or she is connected, the date and time the option was last run (if available) and the name of the person that last performed the option. The dialog also contains a warning message informing the user that deletion cannot be undone.

<span id="_Ref94696456" class="anchor"></span>Figure 15: Delete Test Patient Data Dialog Box

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/016.png)

## Menu Bar for Specific Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menu bar for the four ECS functions are described in the following subsections.

### Data Entry Menu Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Data Entry menu bar consists of the File, Edit, View, and Help menus (Figure 16).

<span id="_Ref94696694" class="anchor"></span>Figure 16: Data Entry Menu Bar Options

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/017.png)

- The File menu item provides the option for the user to exit the window.
- The Edit menu item provides access to Data Entry by Patient, Data Entry by Procedure, and Multiple/Multiple functions.
- The View menu item enables the user to show or hide the Toolbar and Status Bar.
- The Help menu item provides topic-specific help, or information about the Event Capture System.

Figure 17 shows the Data Entry menu bar options with the expanded menus.

<span id="_Ref94696877" class="anchor"></span>Figure 17: Data Entry with Menus Expanded

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/018.png)

### Spreadsheet Menu Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Spreadsheet menu bar consists of the File, Edit, EC Upload, Spreadsheet Options (if the user has the proper security key), and Help menus (Figure 18).

<span id="_Ref94696939" class="anchor"></span>Figure 18: Spreadsheet Menu Bar Options

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/019.png)

- The File menu item enables the user to Exit the window as well as Open Spreadsheet, Open State Veterans Home Spreadsheet, Close, Save, Save As, and Print a file.
- The Edit menu gives the user the option to Undo, Cut, Copy, Paste, Insert Row, Delete Row, Insert Column, or Delete Column.
- The EC Upload menu item enables the user to Upload Records to VistA.
- The Spreadsheet Options menu item enables the user to Change Column Headers or Change Duplicate Threshold.
- The Help menu item provides topic-specific help, or information about the Event Capture System.

Figure 19 shows the Spreadsheet menu bar options with the expanded menus.

<span id="_Ref94696998" class="anchor"></span>Figure 19: Spreadsheet Menu Bar with Menus Expanded

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/020.png)

### Reports Menu Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reports menu bar consists of the File, View, and Help menus (Figure 20).

<span id="_Ref94697037" class="anchor"></span>Figure 20: Reports Menu Bar Options

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/021.png)

- The File menu item enables the user to Exit the window.
- The View menu item enables the user to show or hide the Toolbar and Status Bar.
- The Help menu item provides topic-specific help, or information about the Event Capture System.

Figure 21 shows the Reports menu bar options with the expanded menus.

<span id="_Ref94697077" class="anchor"></span>Figure 21: Reports Menu with Menus Expanded

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/022.png)

### Management Menu Bars

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Event Capture Management Menu bar consists of the File, Table, View, and Help menus (Figure 22).

<span id="_Ref94697129" class="anchor"></span>Figure 22: Management Menu Options

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/023.png)

- The File menu item enables the user to Exit the window.
- The Table menu item provides access to Location, DSS Unit, Access by User, Category, Procedure, Reason, Event Code Screen, Inactivate EC Screen, and Providers functions.
- The View menu item enables the user to show or hide the Toolbar and Status Bar.
- The Help menu item provides topic-specific help, or information about the Event Capture system.

Figure 23 shows the expanded Management Menu bar options with expanded menus.<span id="_Hlk94697161" class="anchor"></span>

Figure 23: Management Menu with Menus Expanded

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/024.png)

## Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If PIV authentication is unavailable, users will need to use VistA access and verify codes to access ECS. To request changes to assigned access and verify codes, please contact the Office of Information Technology (OIT).

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Event Capture Main Menu, click the Exit button to exit the Event Capture GUI. Alternatively, from the same screen, users can go to File \> Exit, or click the Close window button in the top-right corner of the screen.

## Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On all ECS GUI screens, the previous Location entry will be saved and used as the default on subsequent Location fields.

## Online Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online help is available throughout the entire ECS GUI. To obtain online information for any screen, click the question mark button located on the toolbar ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/025.png) or at the bottom-right corner of the screen, click the Topic Help button ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/026.png). The information provided in the help menus corresponds to the information that is in this User Guide (Figure 24).

To obtain online information for a field, select that field and then press the \<F1\> key.

<span id="_Ref94697246" class="anchor"></span>Figure 24: Online Help Screen Example

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/027.png)

## Timeout Feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Event Capture includes a timeout feature consistent with CPRS. A countdown screen will display a warning of the pending timeout of the application when the Event Capture application is idle for a user-defined amount of time. If the user takes no action, the application will close. Click the “Do not close Event Capture” button to stay connected (Figure 25).

<span id="_Ref94697282" class="anchor"></span>Figure 25: Event Capture Timeout Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/028.png)

The amount of time for the timeout feature is user-defined at the application server level.

<span id="_Using_the_Software" class="anchor"></span>

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections detail the [Event Capture Main Menu](#event-capture-main-menu) options (Figure 9). Instructions are provided on how to perform tasks in each of the four main areas:

1.  [Data Entry](#data-entry-menu)
2.  [Spreadsheets](#_Spreadsheet)
3.  [Reports](#reports)
4.  [Management Menu](#_Toc477526651)

## Data Entry Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Data Entry Menu offers three options (Figure 26):

1.  [Data Entry by Patient](#data-entry-by-patient) — Enter/Edit Patient Procedures
5.  [Data Entry by Procedure](#_Data_Entry_by_2) — Batch (Same Procedure, Multiple Patients)
6.  [Multiple Dates/Procs](#multiple-datesmultiple-procedures) — Multiple Dates / Multiple Procedures

<span id="_Ref94697369" class="anchor"></span>Figure 26: Data Entry Menu

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/029.png)

### Data Entry by Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Data Entry by Patient allows the user to enter a single procedure for one patient, edit an existing patient procedure, or delete an existing patient procedure.

Before the User Starts

- Event Code Screens must be defined before entering any Event Capture data.

What the User Will See

- After selecting the Data Entry by Patient option, the Enter/Edit Patient Procedures screen will display (Figure 27), allowing the user to search by the Location, DSS Unit, Procedure Date Range, and Patient Identifier.
- After entering the desired selection criteria, any existing procedures for the selected patient will appear (Figure 29).

<span id="_Ref94697459" class="anchor"></span>Figure 27: Enter/Edit Patient Procedures Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/030.png)

#### Enter/Edit Patient Procedures Screen

To use the Enter/Edit Patient Procedures screen:

1.  Select a Location.
- If there is only one Location set up in ECS, the Location on the screen will default to that value.
- If there is more than one Location set up in ECS, the Location on the screen will default to the last Location used. To change the Location, choose a Location from the dropdown list.
12. Select a DSS Unit.
- If only one DSS Unit is assigned to the user, it will be the default selection. If more than one DSS Unit is assigned to the user, choose a DSS Unit from the dropdown list of accessible DSS Units.
- The user can add, edit, or delete any patient procedure for the selected DSS Unit.

> **NOTE:** - Be aware that any DSS Unit can be affected. Users should use caution and only add, delete, or modify DSS Units that they manage.

- To gain access to a DSS Unit, go the Management Menu and choose the DSS Unit — Add or Update DSS Units function to add the unit to the dropdown list. The ECMGR key is required.
13. Select a Date Range.
- The Procedure Date Range (from/through) will default to the system date. These fields may be edited by typing in a date (DD MMM YYYY) or by using the calendar dropdown (Figure 28).

> **NOTE:** - Date validation will prevent selecting a date in the future or displaying a Procedure From date later than the Procedures Through date.

<span id="_Ref94697549" class="anchor"></span>Figure 28: Calendar Dropdown for Date Range View

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/031.png)

14. Use the Patient Identifier field to select a patient.
- Enter one of the following:
- Patient Name (whole or partial, last name first)
- Social Security Number (SSN)
- Last four digits of the Patient Social Security Number
- First character of Last Name plus the last four digits of the SSN with no spaces
- Press \<Enter\> on the keyboard or click the Search button.
- Choose from the list of patients displayed.
15. View the Patient Procedures.
- Once the previous steps are complete, the bottom section of the window will display the patient procedures in chronological order for the selected search criteria (Figure 29). Each record will display the Category, Procedure, Date/Time, Volume, Associated Clinic, Ordering Section, Primary Diagnosis, and Primary Provider.

> **NOTE:** - Click the column header to sort the data in a different order.

- The Close, Add, and Topic Help buttons are always enabled. If patient procedures exist, the Update and Delete buttons will also be enabled.
- Click to highlight a patient procedure to select that row for updating or deleting.

<span id="_Ref94697610" class="anchor"></span>Figure 29: Procedure History for Sample Patient

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/032.png)

16. To modify patient procedures, choose from the following button options:
- Add — Click the button to enter a new patient procedure.
- Update — Click the button to edit the selected patient procedure.
- Delete — Click the button to delete the selected patient procedure.

#### Recent Visits Screen

To see the Recent Visits screen (Figure 30):

1.  On the Enter/Edit Patient Procedures screen, click the Add button to enter a new patient procedure.

> **NOTE:** - If the selected DSS Unit is set to send to PCE and recent visits exist, the Recent Visits screen will be displayed after clicking the Add button.

<span id="_Ref94697698" class="anchor"></span>Figure 30: Recent Visits Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/033.png)

17. Selection options on the Recent Visits screen.

One can select current day encounters from the Recent Visits, even if they occur after the current time. However, appointments and encounters that occur after the end of the current day will not be available for selection.

- On the Recent Visits screen, the user can choose one of three options:
1.  OK: Select the appropriate Appointment/Encounter from the Recent Visits. Click the OK button to close the screen. The Add Patient Procedure screen opens with the Procedure Date/Time and Associated Clinic fields pre-populated and not modifiable, based on the Appointment/Encounter selected on the Recent Visits screen (Figure 31). The Diagnosis field will also pre-populate, but information in this field *can* be modified by the user.

    Enter the procedure(s), answer classification questions as they pertain to that visit, and provider, and other pertinent fields if required (reasons, ordering section, and/or modifiers).
7.  Ignore: Click the Ignore button on the Recent Visits screen to go to the Add Patient Procedure screen to enter information for all fields.
8.  Cancel: Click the Cancel button to close the Recent Visits screen and return to the Enter/Edit Patient Procedures screen.

<span id="_Ref94697765" class="anchor"></span>Figure 31: Add Patient Procedure Detail Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/034.png)

- To update the record, select an active clinic from the list and then click the OK button.

> **NOTE:** - If the Associated Clinic for the selected record is no longer active, clicking the OK button will result in the display of the Error: Invalid Associated Clinic message dialog (Figure 32). The message dialog lists only active Associated Clinics.

- A clinic must exist in the CLINICS AND STOP CODES file (#728.44) prior to being available for selection in any Data Entry options.
- If an Associated Clinic has non-conforming stop codes, the clinic will not be selectable.
- Click the Cancel button to open the record and the Associated Clinic field will be blank.

<span id="_Ref94697926" class="anchor"></span>Figure 32: Error: Invalid Associated Clinic Message Dialog

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/035.png)

#### Enter Information on the Add Patient Procedure or Edit Patient Procedure Screen

The user can add or edit patient procedures performed on an individual patient using the [Add Patient Procedure](#Add_Patient_Procedure) screen, or the [Edit Patient Procedure](#add-multiple-patient-procedures) screen.

The following instructions and example assume that a user is entering a new procedure for a specified patient, and that the specified DSS Unit transmits data to PCE.

1.  Select a Category.
- If the Allow Category Use field in the DSS Unit Management setup is set to NO, then the Category field will be blank and disabled.
- If the Category field is defined for the specified DSS Unit, that Category will be the default value.
18. Select the Procedure Date and Time.
- The Procedure Date and Time field is not editable if a recent visit was selected on the Recent Visits screen.
- Typing \<N\> on the keyboard and then pressing \<Enter\> (instead of clicking the ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/036.png) button) will populate the Procedure Date & Time field with the current date and time, and will bypass the Select Date/Time dialog box (Figure 33).
- Clicking the Now button in the dialog box will enter the current system date and time.
- Clicking the Midnight button will display “23:59” as the time on the selected date.
- Until a valid date and time are selected, fields after the Procedure Date and Time field are not visible. Once a valid date and time are selected, the remaining fields become visible and available for input.

<span id="_Ref94697986" class="anchor"></span>Figure 33: Select Date/Time Dialog Box

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/037.png)

19. Select an Eligibility Code for this procedure.
- If the selected patient has only one Eligibility Code, that value defaults. Otherwise, select the Eligibility Code that applies to this procedure.
- The primary Eligibility Code displays as the default.
20. Select a Procedure Name.
- Select a Procedure from the dropdown list.
21. Enter the Volume for the procedure.
22. If applicable, the CPT Modifiers section will be enabled.
- Modifiers provide additional information about a CPT procedure. With functionality put in place by the Code Set Versioning project, only CPT modifiers that are active for the date and time of the event will show.
- Choose a modifier from the Modifiers Available list and click Include.
- Repeat as needed.
- To remove a modifier, choose it from the Modifiers Selected list and click Exclude.
- Press and hold the \<Ctrl\> key, and then click items to select multiple modifiers at one time.
23. If applicable, the Reasons field will be enabled.
- The user can enter up to three reasons.
- Reason \#1 must be entered before a second or third may be entered. Reason \#2 must be entered before a third may be entered.
- Reasons appear alphabetically in the dropdown.
- Once selected, a reason will not appear in the dropdown list for remaining reason fields.
- A reason can be selected by entering the initial letter(s) into the Reasons field. If the reason that appears is not the correct choice, click the down arrow on the reason dropdown to select another reason, or enter different letter(s).
24. If applicable, the mandatory classification questions section will be enabled.
- Select YES only if the treatment received relates to that classification.
- Press the \<F1\> key while in the Service Connected field to display a message dialog containing the patient’s service connection and any rated disabilities (Figure 34).

<span id="_Ref94698038" class="anchor"></span>Figure 34: Service Connection and Rated Disabilities Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/038.png)

25. Select the Ordering Section.
26. Select the Associated Clinic (if not already populated from the Recent Visits screen).

Note

- A clinic must exist in file \#728.44 Clinics and Stop Codes prior to being available for selection in any Data Entry options.
- If an Associated Clinic has non-conforming stop codes, the clinic will not be selectable.
27. Select the associated diagnosis code for the procedure (Figure 35).

Note

- If a recent visit is selected from the [Recent Visits](#_Recent_Visits_Screen) screen, the diagnoses box may be pre-populated; diagnoses can be added and removed by the user, as desired.
- Search for a diagnosis by entering one of the following in the Dx (Diagnosis) Lookup box:
- International Classification of Diseases (ICD) code (whole or partial)
- Diagnosis Name (whole or partial)
- Click the Binoculars (Search) button to the right of the Dx Lookup box or press \<Enter\> to begin the search.
- Select from the resulting dropdown list and click the Add Dx to List button to place the desired diagnosis in the Diagnoses box. The user can also double-click on a diagnosis to add it to the list.

Note

- If an ICD code is used to search for a diagnosis, the user can press \< Enter \> to place the diagnosis in the Diagnoses box.
- Repeat as needed to select and add multiple diagnoses.
- Existing diagnoses for the patient procedures, as shown in the Diagnoses box, may be removed, and the Primary Diagnosis may be changed by selecting a diagnosis and using the associated buttons to the left of the Diagnoses box. The primary diagnosis will always be the first entry in the diagnosis box.

<span id="_Ref94698111" class="anchor"></span>Figure 35: Data Entry Diagnoses Box

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/039.png)

28. Optional: Click the Problem List button (Figure 35) to open a list of problems for a patient with the following details (Figure 36):
- Status
- ICD Code with Description
- Onset Date
- Last Updated
- Provider
- Service
- The user may add a diagnosis to the list by double-clicking an item from the Problem List or by selecting an item from the Problem List and clicking the Add Dx to List button. Items with inactive ICD codes cannot be added to the diagnoses box and will return an error message if selected.
- If no information exists for the Problem List, a message dialog is displayed stating “There are no items in the problem list for NAME, PATIENT (XXX-XX-XXXX) DOB: m/d/yyyy.”

<span id="_Ref128035038" class="anchor"></span>Figure 36: Problem List

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/040.png)

29. Select the providers of the service. Use the Providers Available combo box to enter the following:
- Provider name (full or partial, last name first).
- Select the provider from the resulting dropdown list and click the Include button.
- To remove a provider, select from the Providers Selected list and click the Exclude button.
30. Click the Add button to file the current procedure and clear the fields, allowing for input of additional procedures for the selected patient.
31. Click the OK button to file the current procedure and return to the Enter/Edit Patient Procedures screen.
32. Click the Cancel button to return to the Enter/Edit Patient Procedures screen without filing the procedure.

> **NOTE:** - If the record transmits to PCE based on the DSS Unit on Management Menu set up, then all fields will be required.

- If the record does not transmit to PCE based on the DSS Unit on Management Menu set up, then the Associated Clinic and Diagnosis fields will be disabled.
- Occasion Of Service records will not require answers to Classification questions and will not require any diagnosis values.
- Press the \<F1\> key while in any field to display information pertaining to that field.

#### Add a Patient Procedure

The following instructions and example assume that a user is entering a patient procedure for a specified patient and that the specified DSS Unit transmits data to PCE. To add multiple procedures for a patient, see section 4.1.1.5 Add Multiple Patient Procedures.

1.  On the Event Capture Main Menu, select Data Entry.
33. On the Data Entry Menu, select Data Entry by Patient.
- The Enter/Edit Patient Procedures screen appears (Figure 37).
34. Select the Location and DSS Unit.
35. Allow the Procedure Date Range to default to today.
36. Select a Patient.

<span id="_Ref94698191" class="anchor"></span>Figure 37: Enter/Edit Patient Procedures Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/041.png)

37. Click Add.
38. If the DSS Unit is set to send to PCE, the Recent Visits screen will appear (Figure 38). Select a scheduled appointment and click OK.

<span id="_Ref94698230" class="anchor"></span>Figure 38: Recent Visits Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/042.png)

39. Complete the procedure-related fields on the Add Patient Procedure screen (Figure 39) according to the field-by-field instructions given in [Section 4.1.1.3](#_Add_Information_to_3) — Add Information to the Add Patient Procedure or Edit Patient Procedure Screen

<span id="_Toc462237032" class="anchor"></span>Figure 39: Add Patient Procedure Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/043.png)

40. Click Add to file the record and clear the fields, allowing for input of another procedure for this patient. Users may also opt to use the [Multiple Procedure](#add-multiple-patient-procedures)s feature to input multiple patient procedures at one time.
41. Click the OK button to save the record and return to the Enter/Edit Patient Procedures screen.
42. The Enter/Edit Patient Procedures screen displays any existing procedures for this patient (Figure 40).
43. Click the Close button to return to the Data Entry menu.

<span id="_Ref94698342" class="anchor"></span>Figure 40: Enter/Edit Patient Procedures with New Procedure Added

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/044.png)

#### Add Multiple Patient Procedures

The following instructions and example assume that a user is entering multiple procedures for a specified patient and that the specified DSS Unit transmits data to PCE.

1.  On the Event Capture Main Menu, select Data Entry.
44. On the Data Entry Menu, select Data Entry by Patient.
- The Enter/Edit Patient Procedures screen appears (Figure 41).
45. Select the Location and DSS Unit.
46. Allow the Procedure Date Range to default to today.
47. Select a Patient.
48. Click Add.

<span id="_Ref127970260" class="anchor"></span>Figure 41: Enter/Edit Patient Procedures Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/045.png)

49. If the DSS Unit is set to send to PCE, the [Recent Visits](#_Recent_Visits_Screen) screen will appear (Figure 38).

    The user can bypass this screen and go directly to the Add Patient Procedure screen by clicking the Ignore button.

    The user can select a visit from the list and click the OK button to partially populate the Add Patient Procedure screen (Figure 46) with the following:
- Date/Time
- Associated Clinic
- Diagnoses

<span id="_Ref127546667" class="anchor"></span>Figure 42: Recent Visits screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/046.png)

50. Once the Add Patient Procedures screen is open, select the square button to the left of the Procedure Name field to enter multiple procedures (Figure 43).

    When selected, the field will display “The Multiple Procedures feature is in use.”

> **NOTE:** - The Add button for this screen will be disabled when the Multiple Procedures feature is used.

<span id="_Ref151118103" class="anchor"></span>Figure 43: Multiple Procedures Button

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/047.png)

51. The Enter Multiple Procedures for an Encounter screen opens (Figure 44).
52. Input data into the available fields. Refer to section 4.1.1.3 for more detailed field instructions:
- Procedure Name — Select a Procedure from the dropdown list.
- Volume — Enter the Volume for the procedure.
- Reasons — The user can enter up to three reasons, which appear alphabetically in the dropdown menus.
- Modifiers Selected — Choose a modifier from the Modifiers Available list and click the Include button. To remove a modifier, choose it from the Modifiers Selected list and click the Exclude button. To select multiple modifiers at one time, press and hold the \<Ctrl\> key, and then click the appropriate button to include or exclude items.
53. Select the Add Procedure button to place information in the Procedures Selected box.
54. Repeat steps 10 and 11 to add procedures to the list, as desired. The number of procedures added by the user is shown in brackets beside the Procedures Selected label.

<span id="_Ref127547802" class="anchor"></span>Figure 44: Enter Multiple Procedures for an Encounter screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/048.png)

55. Optional: A procedure can be removed by selecting it from the list and clicking the Delete Procedure button.
56. Optional: Details of individual procedures can be viewed by selecting a procedure from the list and clicking on the View Details button. The View Procedure Record Details screen opens (Figure 45). Select the Close Procedure View button to return to the previous screen or select OK to return to the Add Patient Procedure Screen (Figure 46).

<span id="_Ref127873468" class="anchor"></span>Figure 45: View Procedure Record Details

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/049.png)

57. Click the OK button to return to the Add Patient Procedure screen when finished (Figure 46).

<span id="_Ref127548312" class="anchor"></span>Figure 46: Add Patient Procedure Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/050.png)

58. Complete the active fields on the Add Patient Procedure detail screen. Refer to section 4.1.1.3 for more detailed field instructions:
- Procedure Date & Time — Select a valid date and time (if not already populated by the [Recent Visits](#_Recent_Visits_Screen) screen).
- Encounter Related — Select YES only if the treatment received relates to that classification.
- Ordering Section — Select the Ordering Section.
- Associated Clinic — Select the Associated Clinic (if not already populated from the Recent Visits screen).
- Diagnoses — Select the diagnosis code(s) associated with the procedure; if populated from the Recent Visits screen, diagnoses can be edited.
- Providers Available — Select the provider(s) of the service.

> **NOTE:** - If a recent visit was selected from the [Recent Visits](#_Recent_Visits_Screen) screen, the Procedure Date & Time and Associated Clinic will be pre-populated and are not editable. The Diagnoses field will also be pre-populated but *is* editable by the user.

59. Click the OK button to save the record and return to the Enter/Edit Patient Procedures screen.
60. The Enter/Edit Patient Procedures screen displays any existing procedures for this patient (Figure 40).
61. Click the Close button to return to the Data Entry menu.

#### Edit a Patient Procedure

1.  On the [Event Capture Main Menu](#event-capture-main-menu), select Data Entry.
62. On the Data Entry Menu, select Data Entry by Patient.
63. The Enter/Edit Patient Procedures screen appears (Figure 47).

<span id="_Ref94698390" class="anchor"></span>Figure 47: Enter/Edit Patient Procedures Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/051.png)

64. Select the Location and DSS Unit.
65. Enter a Procedure Date Range by using the calendar dropdowns.
- The date fields default to the current system date.
66. Select a patient.
67. The lower portion of the screen displays the procedure(s) for the selected patient and the DSS Unit within the date range.
68. Select a procedure and click the Update button.
- The Edit Patient Procedure screen appears (Figure 48).

<span id="_Ref94698439" class="anchor"></span>Figure 48: Edit Patient Procedure Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/052.png)

69. Complete the procedure-related fields on the Edit Patient Procedure detail screen according to the field-by-field instructions given in [Section 4.1.1.3](#_Add_Information_to_3).
70. Click the Add button to file the record and clear the fields, allowing for input of another procedure for this patient.
71. Click the OK button to save the record and return to the Enter/Edit Patient Procedures screen.
- The Enter/Edit Patient Procedures summary screen displays the procedure(s) (Figure 47) entered for this patient.
72. Click the button to return to the Data Entry menu.

#### Delete a Patient Procedure

This section instructs the user on how to delete a Patient Procedure.

1.  On the Event Capture Main Menu, select Data Entry.
73. On the Data Entry Menu, select Data Entry by Patient.
- The Enter/Edit Patient Procedures summary screen appears (Figure 49).

<span id="_Ref94698503" class="anchor"></span>Figure 49: Enter/Edit Patient Procedures Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/053.png)

74. Select the Location and DSS Unit.
75. Enter a procedure date range by using the calendar dropdowns.
- The date fields default to the current system date.
76. Select a patient.
77. The lower portion of the screen displays the procedure(s) for the selected location, DSS Unit and patient within the date range.
78. Choose a procedure and click the Delete button.
- A confirmation message appears (Figure 50).

<span id="_Ref94698896" class="anchor"></span>Figure 50: Procedure Deleted Confirmation Dialog

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/054.png)

- Click the Yes button on the confirmation message dialog, and an Information message dialog appears to show the selected procedure was deleted for the patient (Figure 51). Click the OK button to return to the Enter/Edit Patient Procedures screen.
- Click the No button on the confirmation message dialog to return to the Enter/Edit Patient Procedures screen without deleting the procedure.

<span id="_Ref110336203" class="anchor"></span>Figure 51: Information Message

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/055.png)

- The screen will refresh to show the remaining procedures entered for this patient (Figure 52).
79. Click the Close button to return to the Data Entry menu.

<span id="_Ref94699512" class="anchor"></span>Figure 52: Enter/Edit Patient Procedures Screen with Procedure Deleted

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/056.png)

### Data Entry by Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Data Entry by Procedure option allows the user to enter or edit the same procedure for multiple patients.

Before the User Starts

- Event Code Screens must be defined before entering any Event Capture data.

What the User Will See

- After selecting Data Entry by Procedure, the Same Procedure, Multiple Patients screen will display (Figure 53).
- The left side of the screen contains information for the procedure that the system will use for all patients.

> **NOTE:** - The user will enter the procedure information only one time.

- The right side of the screen identifies each patient. The user will complete this section for each patient. Click the Add button to file the data and clear the fields to enter data for the next patient.
- The View button displays a listing of all patients entered for this procedure in this session.

<span id="_Toc455135716" class="anchor"></span>Figure 53: Same Procedure, Multiple Patients Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/057.png)

#### Add a Procedure for Multiple Patients

The following instructions and example assume that the user wants the specified DSS Unit to send data to PCE.

1.  Select a Location.
- If there is only one Location set up for the Event Capture System, the Location on the screen will default to that value.
- If there is more than one Event Capture Location set up, the Location will default to the last Location used. To change the Location, choose a Location from the dropdown list of available Event Capture Locations.
80. Select a DSS Unit.
- If one DSS Unit is defined in Event Capture, or if only one DSS Unit is assigned to the user, that DSS Unit will be the default value.
- If more than one DSS Unit is defined, a default will not be assigned. Choose a DSS Unit from the dropdown list of accessible DSS Units.
- To gain access to a DSS Unit, go to the Management Menu and choose the DSS Unit — Add or Update DSS Units function to add the unit to the dropdown list.
81. Select a Category.
- If only one category is defined for the specified DSS Unit, that category will be the default.
82. Select the Procedure Date and Time.
- Typing \<N\> and then pressing \<Enter\> in the field (instead of clicking the ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/058.png) button) will bypass the Select Date/Time dialog (Figure 54). If the Select Date/Time dialog is displayed, click the Now button to enter the current system date and time. When the Midnight button is clicked, “23:59” is displayed for the time on the date selected.
- Until a valid date and time are selected, fields after the Procedure Date and Time field are not visible. Once a valid date and time are selected, the remaining fields become visible and available for input.

<span id="_Ref94699633" class="anchor"></span>Figure 54: Select Date/Time Dialog

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/059.png)

83. Select a Procedure Name.
- Select a procedure from the dropdown list.
84. If applicable, the Reasons field will be enabled.
- The user can enter up to three reasons.
- Reason \#1 must be entered before a second or third may be entered. Reason \#2 must be entered before a third may be entered.
- Reasons appear alphabetically in the dropdown.
- A reason will not appear in the dropdown list for remaining reason fields as an option once selected.
- A reason can be selected by entering the initial letter(s) in the Reasons field. If the reason that appears is not the correct choice, click the down arrow on the reason dropdown to select another reason. or enter different letter(s).
85. If applicable, the CPT Modifiers section will be enabled.
- Modifiers provide additional information about a CPT procedure. With functionality put in place by the Code Set Versioning project, only CPT modifiers that are active for the date and time of the event will show.
- Choose a modifier from the Modifiers Available list and click the right pointer icon ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/060.png). Repeat as needed.
- To remove a modifier, choose it from the Modifiers Selected list and click the left pointer icon ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/061.png).
- Press and hold the \<Ctrl\> key, and then click items to select multiple modifiers at one time.
86. Select the providers of the services. Use the Providers Available text box to enter the following:
- Provider name (full or partial, last name first)
- Select the provider from the resulting dropdown list and click the right pointer icon ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/062.png).
- To remove a provider, select from the Providers Selected list and click the left pointer icon ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/063.png).
87. Use the Patient Identifier field to select a patient.
- Enter one of the following:
- Patient Name (whole or partial, last name first)
- Social Security Number
- Last four digits of the Patient Social Security Number
- First character of Last Name plus the last four digits of the SSN with no spaces
- Press \<Enter\> on the keyboard or click the Binoculars (Search) button.
- Choose from the list of patients displayed.
88. Select an Eligibility Code for this procedure.
- If the selected patient has only one Eligibility Code, that value defaults. Otherwise, select the Eligibility Code that applies to this procedure.
- The primary Eligibility Code displays as the default.
89. Enter the Volume for the procedure.
90. If applicable, the mandatory classification questions section will be enabled.
- Select YES only if the treatment received relates to that classification.
- Pressing the \<F1\> key while in the Service Connected field will open a message dialog displaying the patient’s service connection and any rated disabilities (Figure 55).

<span id="_Ref94699686" class="anchor"></span>Figure 55: Service Connection and Rated Disabilities Dialog

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/064.png)

91. Select the Ordering Section.
92. Select an Associated Clinic for the specified DSS Unit, if applicable.

Note

- A clinic must exist in file \#728.44 Clinics and Stop Codes prior to being available for selection in any Data Entry option.
- If an Associated Clinic has non-conforming stop codes, the clinic will not be selectable.
93. Select the associated diagnosis code for the procedure.
- Search for a diagnosis by entering one of the following in the Dx (Diagnosis) Lookup box (Figure 56):
- International Classification of Diseases (ICD) code (whole or partial)
- Diagnosis Name (whole or partial)
- Click the Binoculars (Search) button to the right of the Dx Lookup box or press \<Enter\> to begin the search.
- Select from the resulting dropdown list and click the Add Dx to List button to place the desired diagnosis in the Diagnoses box. The user can also double-click on a diagnosis to add it.

Note

- If an ICD code is used to search for a diagnosis, the user can press \<Enter\> to place the diagnosis in the Diagnoses box.
- Repeat as needed to select and add multiple diagnoses.
- Values in the Diagnoses box may be removed, or the Primary Diagnosis may be changed, by selecting a diagnosis and using the associated buttons to the left of the Diagnoses box. The primary diagnosis will always be the first entry in the Diagnoses box.

<span id="_Ref94699922" class="anchor"></span>Figure 56: Same Procedure, Multiple Patients, Data Entry Diagnoses Box

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/065.png)

94. Repeat steps 9 through 15 to add the same procedure for another patient.
95. Click the View button to verify that the list of patients entered is correct.
- The View Patients for this Procedure screen will list all the patients entered for the procedure that was selected (Figure 57).
96. When all patients have been added for the current procedure, click the OK button to file the records, or click the Cancel button to return to the Data Entry menu without filing the records.
97. To correct an entry, return to the Data Entry menu and select Data Entry by Patient.

<span id="_Ref94699998" class="anchor"></span>Figure 57: View Patients for this Procedure Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/066.png)

### Multiple Dates/Multiple Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Multiple Dates/Multiple Procedures option allows the user to add multiple dates and multiple patients for multiple procedures.

Before the User Starts

- Event Code Screens must be defined before entering any Event Capture data.

What the User Will See

- After selecting Multiple Dates/Multiple Procedures from the Data Entry Menu, the Multiple Dates/Multiple Procedures screen displays (Figure 58).
- The area at the top of the first screen provides common fields (Location, DSS Unit, and Category) as well as the Procedure Date/Time.
- The first three tabs allow the user to enter providers, procedures, and patients (Providers, Procedures, and Select Patient).
- The last two tabs allow the user to check the work before submitting (View Selected Patients and Records Pending Filing). The number of patients selected and the number of records pending are displayed on the tab headers.

<span id="_Ref104989584" class="anchor"></span>Figure 58: Multiple Dates/Multiple Procedures Screen — Initial Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/067.png)

#### Instructions for Common Fields

1.  Select a Location.
- If there is only one Location set up for the Event Capture System, the Location on the screen will default to that value.
- If there is more than one Event Capture Location set up, the Location will default to the last Location used. To change the Location, choose a Location from the dropdown list of available Event Capture Locations.
98. Select a DSS Unit.
- If one DSS Unit is defined in Event Capture, or if only one DSS Unit is assigned to the user, that DSS Unit will be the default value.
- If more than one DSS Unit is defined, a default will not be assigned. Choose a DSS Unit from the dropdown list of accessible DSS Units.
- To gain access to an existing DSS Unit, the Event Capture Manager must assign it to the user.
99. Select a Category.
- If categories are not allowed in the DSS Unit, the selection box will be disabled.
- If only one category is defined for the specified DSS Unit, that category will be the default.
100. Select the Procedure Date and Time by using the Select Date/Time dialog (Figure 59).

<span id="_Ref94700091" class="anchor"></span>Figure 59: Select Date/Time Dialog

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/068.png)

- Select date and time and click the OK button to close the dialog.
- Click the Add Date/Time button to add the choice to the Selected Dates / Times list.
- Select and add dates as needed.
- To remove a date, choose it from the list and click the Delete Date/Time button.

> **NOTE:** - The Procedure Date/Time field defaults to the current system date and time.

- To enter the current system date and time, click the Now button on the Select Date/Time dialog.
- When the Midnight button is clicked, “23:59” is displayed as the time on the date selected.
101. Click and complete the tabs for Providers, Procedures and Select Patient as described in the following sections:

     4.1.3.2 — [Add Information to the Providers Tab](#add-information-to-the-providers-tab)

     4.1.3.3 — [Add Information to the Procedures Tab](#add-information-on-the-procedures-tab)

     4.1.3.4 — [Add Information to the Select Patient Tab](#_Add_Information_to_2)
102. Use the View Selected Patients and Records Pending Filing tabs to check the work as described in the following sections:

     4.1.3.5 — [Verify Information Using the View Selected Patients Tab](#verify-information-using-the-view-selected-patients-tab)

     4.1.3.6 — [Verify Information Using the Records Pending Filing Tab](#verify-information-using-the-records-pending-filing-tab)
103. Click the Save button at the bottom of the screen to process the transactions shown on the Records Pending Filing tab and continue to enter a new set of entries.
104. Click the OK button at the bottom of the screen to process the transactions shown on the Records Pending Filing tab, and then return to the Data Entry menu.

#### Add Information to the Providers Tab

1.  Click the Providers tab to select one or more providers (Figure 60).

<span id="_Ref105140534" class="anchor"></span>Figure 60: Multiple Dates/Multiple Procedures Screen, Providers Tab

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/069.png)

105. Select a Provider.
- Use the Providers Available list to enter the full or partial provider name (last name first).
- Select the provider from the resulting dropdown list and click the Include button.
- To remove a provider, select from the Providers Selected list and click the Exclude button.
106. Repeat as needed to add providers.

#### Add Information on the Procedures Tab

1.  Click the Procedures tab to select one or more procedures (Figure 61).

<span id="_Ref94700262" class="anchor"></span>Figure 61: Multiple Dates/Multiple Procedures Screen, Procedures Tab

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/070.png)

107. Select a Procedure Name.
- Select a procedure from the dropdown list.
108. Enter the Volume for this procedure.
109. If applicable, the Reasons field will be enabled.
- The user can enter up to three reasons.
- Reason \#1 must be entered before a second may be entered. Reason \#2 must be entered before a third may be entered.
- Reasons appear alphabetically in the dropdown.
- A reason will not appear in the dropdown list for remaining reason fields as an option once selected.
- A reason can be selected by entering the initial letter(s) in the Reasons field. If the reason that appears is not the correct choice, click the down arrow on the reason dropdown to select another reason, or enter different letter(s).
110. If applicable, the Modifiers section will be enabled.
- Modifiers provide additional information about a CPT procedure. With functionality put in place by the Code Set Versioning project, only CPT modifiers that are active for the date and time of the event will display.
- Choose a Modifier from the Modifiers Available list and click the Include button.
- Repeat as needed.
- To remove a modifier, choose it from the Modifiers Selected list and click the Exclude button.
- Press and hold the \<Ctrl\> key, and then click items to select multiple modifiers at one time.
111. Click the Add Procedure button to add this procedure to the Procedures Selected list and display a blank screen ready for another entry.
112. To add another procedure, repeat the steps above.

Note

- Diagnoses which exist for the same location, procedure date/time, Associated Clinic and patient will be retrieved when those key fields are encountered for a new procedure.
113. To delete a procedure, choose it from the Selected Procedures list and click the Delete Procedure button.
114. To view a procedure in an expanded format, choose it from the Selected Procedures list and click the View Details button. The View Procedure Record Details screen (Figure 62) is not editable.
115. Click the Close Procedure View button to return to the Procedures tab

<span id="_Ref94700309" class="anchor"></span>Figure 62: View Procedure Record Details Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/071.png)

#### Add Information to the Select Patient Tab

1.  Click the Select Patient tab to select one or more patients (Figure 63).

<span id="_Ref94700390" class="anchor"></span>Figure 63: Multiple Dates/Multiple Procedures Screen, Select Patient Tab

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/072.png)

116. Use the Patient Identifier field to select a patient.
- Enter one of the following:
- Patient Name (whole or partial, last name first)
- Social Security Number
- Last four digits of the patient Social Security Number
- First character of Last Name plus the last four digits of the SSN with no spaces
- Press \<Enter\> or click the Binoculars (Search) button.
- Choose from the list of patients displayed.
117. Select an Eligibility Code for this procedure.
- If the selected patient has only one Eligibility Code, that value defaults. Otherwise, select the Eligibility Code that applies to this procedure.
- The primary Eligibility Code displays as the default.
118. If applicable, the mandatory Encounter Related classification questions section will be enabled.
- Select YES only if the treatment received relates to that classification.
- Pressing the \<F1\> key while in the Service Connected field will open a message dialog displaying the patient’s service connection and any rated disabilities (Figure 64).

<span id="_Ref94700439" class="anchor"></span>Figure 64: Service Connection and Rated Disabilities Dialog

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/073.png)

119. Select the Ordering Section.
120. Select the Associated Clinic.

Note

- A clinic must exist in file \#728.44 Clinics and Stop Codes prior to being available for selection in any Data Entry options.
- If an Associated Clinic has non-conforming stop codes, the clinic will not be selectable.
121. Select the associated diagnosis code for the procedure.

Note

- Diagnoses which exist for the same location, procedure date/time, Associated Clinic and patient will be retrieved when those key fields are encountered for a new procedure.
- Search for a diagnosis by entering one of the following in the Dx (Diagnosis) Lookup box (Figure 65):
- International Classification of Diseases (ICD) code (whole or partial)
- Diagnosis Name (whole or partial)
- Click the Binoculars (Search) button to the right of the Dx Lookup box or press \<Enter\> to begin the search.
- Select from the resulting dropdown list and click the Add a Dx button to place the desired diagnosis in the Diagnoses box. The user can also double-click on a diagnosis to add it.

Note

- If an ICD code is used to search for a diagnosis, the user can press \<Enter\> to place the diagnosis in the Diagnoses box.
- Repeat as needed to select and add multiple diagnoses.
- Values in the Diagnoses box may be removed, or the Primary Diagnosis may be changed, by selecting a diagnosis and using the associated buttons to the left of the Diagnoses box. The primary diagnosis will always be the first entry in the diagnosis box.

<span id="_Ref94700490" class="anchor"></span>Figure 65: Multiple Dates/Multiple Procedures, Select Patient Tab, Diagnoses Box

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/074.png)

122. Click the Add Patient button to add this patient to the list of Selected Patients and display a blank screen ready for another entry.
123. Use the View Selected Patients tab to check the work.

#### Verify Information Using the View Selected Patients Tab

The following instructions are used to verify information using the View Selected Patients tab, and to delete information for a specific patient.

Note that the number of patients selected by the user is displayed on the tab header.

1.  Click the View Selected Patients tab to review the list of selected patients (Figure 66).

<span id="_Ref94700566" class="anchor"></span>Figure 66: Multiple Dates/Multiple Procedures View Selected Patients Tab

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/075.png)

124. To remove a patient from the list, select a record and click the Delete Patient button. Click the Yes button on the Confirmation message dialog (Figure 67).

<span id="_Ref94700617" class="anchor"></span>Figure 67: Deleting Patient Confirmation Dialog

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/076.png)

125. To view a patient in an expanded format, select the record and click the View Details button.
- The patient record is not editable using the View Patient Record Detail screen (Figure 68).
126. Click the Close Patient View button to return to the View Selected Patients tab.

<span id="_Ref95316719" class="anchor"></span>Figure 68: View Patient Record Details Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/077.png)

#### Verify Information Using the Records Pending Filing Tab

The Records Pending Filing tab lists the individual records (transactions) that will be processed when the OK or Save button at the bottom of the screen is clicked (Figure 69).

1.  Click the Records Pending Filing tab to view a list of the records to be filed.

> **NOTE:** - The number of records pending is displayed on the tab header.

- This screen is not editable.

<span id="_Ref94700711" class="anchor"></span>Figure 69: Multiple Dates/Multiple Procedures Records Pending Filing Tab

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/078.png)

127. Click the OK button to return to the Data Entry menu or click Save to add more entries.
- After clicking the Save button, an information dialog will appear on the screen to show the number of records added (Figure 70).

<span id="_Ref94700763" class="anchor"></span>Figure 70: Information Dialog after Saving

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/079.png)

The records consist of every combination of the dates, procedures, and patients selected on the tabs described in the preceding sections, and the providers selected will be assigned to each record.

128. To change the list of records pending filing, review and revise the selections on the Providers, Procedures and Select Patient tabs. as well as the values on the Selected Dates/Times list.
129. To correct an entry, return to the Data Entry menu and select Data Entry by Patient.

## Spreadsheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data can be batch processed in the Event Capture GUI using the spreadsheet import and upload options. Two types of spreadsheets can be used for this data entry — the regular spreadsheet or the State Veterans Home spreadsheet. Both methods of import are launched from the Spreadsheet Upload screen. Once a spreadsheet is imported into Event Capture, the data can be uploaded to VistA.

### Import a Regular Spreadsheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Importing is the traditional method for batch processing spreadsheet data. The spreadsheet import functionality works with MS Excel® files, as well as with tab or comma delimited files.

Before the User Starts

- A template with default column order is available to aid in populating spreadsheets prior to import. The header row will not be processed when data is imported, and it should remain in the spreadsheet during the import process.
- Any spreadsheets that do not match the column layout of the template will be rejected at import.
- The ECS spreadsheet template is available on the VA Intranet, Program Documents page.
- Once the template is downloaded, save it to a local hard-drive for later use.
- Both \*.XLS (pre- 2007) and \*.XLSX versions of MS Excel spreadsheets are valid for use in the Event Capture spreadsheet import process.

What the User Will See

- After selecting the Spreadsheet option from the main menu, the Spreadsheet Upload screen displays a blank grid form (Figure 71).

<span id="_Ref94700810" class="anchor"></span>Figure 71: Spreadsheet Upload Screen Before Import

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/080.png)

Steps for importing a regular spreadsheet:

1.  Click the Open a Regular Spreadsheet button or select the Open Spreadsheet option from the File menu.
- A standard Select File dialog will display, allowing the user to select the spreadsheet to be imported.
130. Once the desired spreadsheet is selected for import, click the Open button.
- The data is then imported into Event Capture and will be displayed in the grid of the Spreadsheet Upload form (Figure 72).

<span id="_Ref105139735" class="anchor"></span>Figure 72: Imported Spreadsheet Data Shown in the Spreadsheet Upload Form

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/081.png)

#### Regular Spreadsheet Fields

The regular spreadsheet contains 37 columns. Each is described here:

Record Num: The Record Num field displays the Record Number, which is a unique number used to associate error messages with the correct row of data. If this field is blank, VistA validation will not be done. This is a required field.

Location: The Location field displays the station number, and it must exist in the INSTITUTION file (#4). This is a required field.

Pat SSN: The Pat SSN is the SSN of the patient for whom the procedure was done. It can contain only digits, and must exist in the PATIENT file (#2, ^DPT). If the SSN is shorter than 9 digits, it will be padded with leading zeros. This is a required field.

Patient LName: The Patient Lname (last name) field is the surname of the patient and must contain a value at least two characters in length. Combined with the Patient FName value (in the form “last name, first name”), it must match the name in the PATIENT file (#2) for the Patient SSN associated with the row in the spreadsheet. This is a required field.

Patient FName: The Patient Fname (first name) field is optional. However, together with the Patient LName (in the form “last name, first name”), it must match the name in the PATIENT file (#2) for the Patient SSN associated with the row in the spreadsheet.

DSS Unit Name: The DSS Unit Name field indicates the DSS Unit used for the patient procedure. The DSS Unit Name is not required if the DSS Unit IEN is filled in. If this field contains a value, then it must have a “B” cross-reference on the DSS UNIT file (#724).

DSS Department: Because the DSS Department is not necessarily unique, it is no longer being used to identify the DSS Unit. Values entered in this field will be ignored. Use the DSS Unit Name or the DSS Unit IEN to identify the DSS Unit.

DSS Unit IEN: The DSS Unit IEN is an alternate way to identify the DSS Unit used for the patient procedure. It is not required if the DSS Unit Name is filled in. If the DSS Unit IEN field contains a value, that value must exist in the DSS UNIT file (#724).

Proc Code: The Proc Code or CPT code represents the procedure performed for the patient. Any National Procedure, Local Procedure, or CPT code is valid for this field provided it exists in the EC NATIONAL PROCEDURE file (#725) or the CPT file (#81), and the Event Code Screen (comprised of the Location, DSS Unit, and Procedure) is active. This is a required field.

Volume: The Volume field usually indicates the number of procedures performed, but it can also be used to track the number of bed days, or the time increments spent performing the procedure. For example, if a 15-minute increment represents a unit, a Volume of 1 equals 15 minutes, a volume of 2 equals 30 minutes, etc. The volume must be a number from 1 to 99. This is a required field.

Ordering Sect: The Ordering Sect field is the name of the medical section which ordered the procedure for the patient. If the user enters a value for the Ordering Section, it will be validated against the "B" cross reference in the MEDICAL SPECIALTY file (#723). If the user leaves this field blank, the program will derive the Ordering Section from DSS UNIT file (#724) based on the DSS Unit IEN.

Enc Date/Time: The Enc Date/Time field is the Date and Time of the encounter. The value can be in any valid FileMan format. The 'seconds' are ignored; the month, day, and year can be separated by any special character (non-numeric, non-alpha) except '^' and '@'. This field is required.

> Examples:

> mm/dd/yy @hh:mm:ss

> mm/dd/yyyy @hh:mm:ss

> mm-dd-yy @hh:mm

> mmm dd,yyyy @hhmm

> mmddyy@hhmm

> N, N-1, N-5h, etc.

Category: The Category field provides Event Capture a common level to group associated procedures. Multiple procedures can be defined for each category. This field is optional and will be assigned a value of ‘0’ if blank. However, if the user enters a value, a “B” cross-reference for that value must exist in the EVENT CAPTURE CATEGORY file (#726).

Diag Code: The Diag Code field is the primary Diagnosis Code value. It must exist in the ICD DIAGNOSIS file (#80) and be active for the date/time of the encounter.

> **NOTE:** - The Diagnosis Code is only required for records sent to PCE and will be ignored otherwise. For DSS units set up as 'OOS', the diagnosis field will be ignored.

Sec Dx 1: The Sec Dx 1 field is a secondary Diagnosis Code value. It must exist in the ICD DIAGNOSIS file (#80) and be active for the date/time of the encounter.

> **NOTE:** - Secondary diagnosis codes are optional. For records NOT sent to PCE (including those with DSS set up as 'OOS'), the diagnosis codes will be ignored.

Sec Dx 2: The Sec Dx 2 field is a secondary Diagnosis Code value. It must exist in the ICD DIAGNOSIS file (#80) and be active for the date/time of the encounter.

> **NOTE:** - Secondary diagnosis codes are optional. For records NOT sent to PCE (including those with DSS set up as 'OOS'), the diagnosis codes will be ignored.

Sec Dx 3: The Sec Dx 3 field is a secondary Diagnosis Code value. It must exist in the ICD DIAGNOSIS file (#80) and be active for the date/time of the encounter.

> **NOTE:** - Secondary diagnosis codes are optional. For records NOT sent to PCE (including those with DSS set up as 'OOS'), the diagnosis codes will be ignored.

Sec Dx 4: The Sec Dx 4 field is a secondary Diagnosis Code value. It must exist in the ICD DIAGNOSIS file (#80) and be active for the date/time of the encounter.

> **NOTE:** - Secondary diagnosis codes are optional. For records NOT sent to PCE (including those with DSS set up as 'OOS'), the diagnosis codes will be ignored.

Assoc Clin Name: The Assoc Clin Name is the name of the Associated Clinic of the procedure. If the DSS Unit is set to send all records to PCE, either an Associated Clinic name or Associated Clinic IEN is required. If both are entered, only the IEN will be used to identify the Associated Clinic.

Assoc Clin IEN: The Assoc Clin IEN field is the IEN of the Associated Clinic of the procedure. If the DSS Unit is set to send all records to PCE, either an Associated Clinic name or Associated Clinic IEN is required. If both are entered, only the IEN will be used to identify the Associated Clinic.

Mod 1: The Mod 1 field provides additional information about a CPT procedure. Up to 5 unique Modifier codes can be entered for a procedure. The Mod 1 field is not required.

Mod 2: The Mod 2 field provides additional information about a CPT procedure. Up to 5 unique Modifier codes can be entered for a procedure. The Mod 2 field is not required.

Mod 3: The Mod 3 field provides additional information about a CPT procedure. Up to 5 unique Modifier codes can be entered for a procedure. The Mod 3 field is not required.

Mod 4: The Mod 4 field provides additional information about a CPT procedure. Up to 5 unique Modifier codes can be entered for a procedure. The Mod 4 field is not required.

Mod 5: The Mod 5 field provides additional information about a CPT procedure. Up to 5 unique Modifier codes can be entered for a procedure. The Mod 5 field is not required.

Agent Orange: The Agent Orange field indicates whether the encounter was related to Agent Orange exposure (Y) or was not related to Agent Orange exposure (N). When the spreadsheet is uploaded to VistA, validity checks will determine if a value is required in this field.

Ion Rad: The Ion Rad field indicates whether the encounter was related to Ionizing Radiation exposure (Y) or was not related to Ionizing Radiation exposure (N). When the spreadsheet is uploaded to VistA, validity checks will determine if a value is required in this field.

Service Conn: The Service Conn field identifies if the encounter is related to a service connected condition and represents whether the patient has Service Connected eligibility (Y) or does not have Service Connected eligibility (N). When the spreadsheet is uploaded to VistA, validity checks will determine if a value is required in this field

SW Asia: The SW Asia field indicates whether the encounter was related to Southwest Asia Conditions (Y) or was not related to Southwest Asia Conditions (N). When the spreadsheet is uploaded to VistA, validity checks will determine if a value is required in this field.

Mil Sexual Trauma: The Mil Sexual Trauma field indicates whether the encounter was related to Military Sexual Trauma (Y) or was not related to Military Sexual Trauma (N). When the spreadsheet is uploaded to VistA, validity checks will determine if a value is required in this field.

Head Neck Cancer: The Head Neck Cancer field indicates whether the encounter was related to Head and Neck Cancer (Y) or was not related to Head and Neck Cancer (N). When the spreadsheet is uploaded to VistA, validity checks will determine if a value is required in this field.

Combat Vet: The Combat Vet field indicates whether the encounter was related to the patient’s Combat Veteran status (Y) or was not related to the patient’s Combat Veteran status (N). When the spreadsheet is uploaded to VistA, validity checks will determine if a value is required in this field.

SHAD: The SHAD field indicates whether the encounter was related to Project Shipboard Hazard and Defense (SHAD) (Y) or was not related to Project SHAD (N). When the spreadsheet is uploaded to VistA, validity checks will determine if a value is required in this field.

Camp Lejeune: The Camp Lejeune field indicates whether the encounter was related to Camp Lejeune exposure (Y) or was not related to Camp Lejeune exposure (N). When the spreadsheet is uploaded to VistA, validity checks will determine if a value is required in this field.

Prov 1 Name or IEN: The Prov 1 Name or IEN field displays the primary Provider for the patient procedure being added. The name (last name, first name) must exist in the NEW PERSON file (#200) and have a "B" cross reference in that file. The Provider must have an active Person Class unless the DSS Unit is set to send no records to PCE; in that case, a Non-Licensed Provider (identified in the "Providers" option on the ECS Management Menu) may be entered.

> The provider's IEN may be entered instead of the name.

> A value is required in the Prov 1 Name or IEN field.

Prov 2 Name or IEN: The Prov 2 Name or IEN field displays the secondary Provider for the patient procedure being added. The name (last name, first name) must exist in the NEW PERSON file (#200) and have a "B" cross reference in that file. The Provider must have an active Person Class unless the DSS Unit is set to send no records to PCE; in that case, a Non-Licensed Provider (identified in the "Providers" option on the ECS Management Menu) may be entered.

> The provider's IEN may be entered instead of the name.

> The Prov 2 Name or IEN field is optional.

Prov 3 Name or IEN: The Prov 3 Name or IEN field displays the tertiary Provider for the patient procedure being added. The name (last name, first name) must exist in the NEW PERSON file (#200) and have a "B" cross reference in that file. The Provider must have an active Person Class unless the DSS Unit is set to send no records to PCE; in that case, a Non-Licensed Provider (identified in the "Providers" option on the ECS Management Menu) may be entered.

> The provider's IEN may be entered instead of the name.

> The Prov 3 Name or IEN field is optional.

Prov 4 Name or IEN: The Prov 4 Name or IEN field displays the fourth Provider for the patient procedure being added. The name (last name, first name) must exist in the NEW PERSON file (#200) and have a "B" cross reference in that file. The Provider must have an active Person Class unless the DSS Unit is set to send no records to PCE; in that case, a Non-Licensed Provider (identified in the "Providers" option on the ECS Management Menu) may be entered.

> The provider's IEN may be entered instead of the name.

> The Prov 4 Name or IEN field is optional.

Prov 5 Name or IEN: The Prov 5 Name or IEN field displays the fifth Provider for the patient procedure being added. The name (last name, first name) must exist in the NEW PERSON file (#200) and have a "B" cross reference in that file. The Provider must have an active Person Class unless the DSS Unit is set to send no records to PCE; in that case, a Non-Licensed Provider (identified in the "Providers" option on the ECS Management Menu) may be entered.

> The provider's IEN may be entered instead of the name.

> The Prov 5 Name or IEN field is optional.

Prov 6 Name or IEN: The Prov 6 Name or IEN field displays the sixth Provider for the patient procedure being added. The name (last name, first name) must exist in the NEW PERSON file (#200) and have a "B" cross reference in that file. The Provider must have an active Person Class unless the DSS Unit is set to send no records to PCE; in that case, a Non-Licensed Provider (identified in the "Providers" option on the ECS Management Menu) may be entered.

> The provider's IEN may be entered instead of the name.

> The Prov 6 Name or IEN field is optional.

Prov 7 Name or IEN: The Prov 7 Name or IEN field displays the seventh Provider for the patient procedure being added. The name (last name, first name) must exist in the NEW PERSON file (#200) and have a "B" cross reference in that file. The Provider must have an active Person Class unless the DSS Unit is set to send no records to PCE; in that case, a Non-Licensed Provider (identified in the "Providers" option on the ECS Management Menu) may be entered.

> The provider's IEN may be entered instead of the name.

> The Prov 7 Name or IEN field is optional.

#### Edit Cell Data on the Spreadsheet Upload Form

All imported data can be modified in the Spreadsheet Upload form. The information from the selected cell is displayed in the Cell Data edit box (located above the grid). The value can be changed in either the edit box or the cell itself.

Data in each cell can be cut, copied, or pasted using the edit menu functions (Figure 73). The contents of an individual cell can be deleted using either the Cell Data edit box, or by clicking twice in the cell to highlight the data and pressing the \<Delete\> key.

> **NOTE:** - Quickly double-clicking within the cell does not select the data within the cell. To select data within a cell, click once within the cell, then click again to select the cell’s contents.

To delete an entire record, click once on a cell within the record to be deleted, then press \<Ctrl + Delete\>. Alternatively, the user can select Edit \> Delete Row from the menu bar. Rows can be inserted using the Edit \> Insert Row function on the menu bar.

To delete a column within the Spreadsheet Upload form, select a cell within the column to be deleted, then use the Edit \> DeleteColumn function. Columns can also be inserted using the Edit \> Insert Column function on the menu bar.

For any accidental or undesired action performed, the user can undo that action by selecting Edit \> Undo or by pressing \<Ctrl + Z\>. The undo function can be used multiple times to undo multiple actions.

<span id="_Ref94700918" class="anchor"></span>Figure 73: Spreadsheet Upload — Edit Functions

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/082.png)

> **NOTE:** - Help is available for each column in the spreadsheet. Click any column, and then click the Help button ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/083.png).

#### Modify Column Order

When the Spreadsheet Upload form is opened, the column headers are displayed in a default order. The user can change the order of the columns if the EC Template is not used.

1.  Click the Column Header button ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/084.png), or select the Change Column Headers option from the Spreadsheet Options menu.
- The Column Headers form will be displayed (Figure 74).

<span id="_Ref94700955" class="anchor"></span>Figure 74: Column Headers Form

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/085.png)

131. To change the order of the columns, highlight the column heading from the list and click either the Move Up or Move Down button.
- Repeat Step 2 until the column order matches the columns order of the spreadsheet. Click the Apply button to save the column order.

> **NOTE:** - The default column header order is as follows:

1.  Record Num
5.  Location
6.  Pat SSN
7.  Pat LName
8.  Pat FName
9.  DSS Unit Name
10. DSS Department
11. DSS Unit Internal Entry Number (IEN)
12. Proc Code
13. Volume
14. Ordering Sect
15. Enc Date/Time
16. Category
17. Diag Code
18. Sec Dx 1
19. Sec Dx 2
20. Sec Dx 3
21. Sec Dx 4
22. Assoc Clinic Name
23. Assoc Clinic IEN
24. Mod 1
25. Mod 2
26. Mod 3
27. Mod 4
28. Mod 5
29. Agent Orange
30. Ion Rad
31. Service Conn
32. SW Asia
33. Mil Sexual Trauma
34. Head Neck Cancer
35. Combat Vet
36. SHAD
37. Camp Lejeune (Note: As of Patch EC\*2\*139, this column is a placeholder)
38. Prov 1 Name or IEN
39. Prov 2 Name or IEN
40. Prov 3 Name or IEN
41. Prov 4 Name or IEN
42. Prov 5 Name or IEN
43. Prov 6 Name or IEN
44. Prov 7 Name or IEN

### Import a State Veterans Home Spreadsheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

State Veterans Home facilities use Excel spreadsheets for tracking patient occupancy. Event Capture can directly import, and upload, the data from these spreadsheets.

Before the User Starts

- The State Veterans Home spreadsheet template is available for download from the State Veterans Home website.
- Once the template is downloaded, save it to a local hard-drive for later use.
- Both \*.XLS (pre- 2007) and \*.XLSX versions of MS Excel spreadsheets are valid for use in the Event Capture spreadsheet import process.
- The State Veterans Home Name is in the spreadsheet in cell B853. The name starts after the second space. All control, “^”, “;” and “:” characters are stripped from the text found in the cell. The name is then truncated to 25 characters.

What the User Will See

- From the Spreadsheet Upload screen, the user will click the State Home Spreadsheet icon ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/086.png) or use the menu to select File \> OpenState Home Spreadsheet.
- A Select File Dialog opens, prompting the user to locate and select the appropriate State Veterans Home spreadsheet (Figure 75).

<span id="_Ref94701002" class="anchor"></span>Figure 75: Select File Dialog — Open a State Veterans Home Spreadsheet

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/087.png)

> **NOTE:** - Multiple months of State Veterans Home data can be stored in a single spreadsheet by using tabbed worksheets to represent the various months. Only the worksheet that was active when the spreadsheet was last saved will be imported.

1.  Once the desired State Veterans Home spreadsheet is selected for import, click the Open button.
- A screen prompting the user for more information, including Facility Type, Location, DSS Unit, Date and Provider(s), is displayed (Figure 76).

<span id="_Ref94701058" class="anchor"></span>Figure 76: Additional Data Form for State Veterans Home Spreadsheet Import

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/088.png)

> **NOTE:** - All fields must contain data to import a State Veterans Home spreadsheet.

- Click the Cancel button on this screen to abort the import process.
132. Click the OK button on this screen to continue with the import.
- The data is then imported into Event Capture and will be displayed in the grid of the Spreadsheet Upload form.

### Upload Imported Spreadsheet Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start the upload process, click the Upload Records button ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/089.png) on the toolbar, or select the Upload Records to VistA option from the EC Upload menu.

Before the User Starts

- Each record in the imported spreadsheet is validated before being filed in the EVENT CAPTURE PATIENT file (#721).
- Two levels of validation occur:

  <u>The first level of validation</u> occurs within the Event Capture GUI application. A check for required information is performed, and no data transmits to VistA if this level of validation fails for any record in the spreadsheet.

  <u>The second level of validation</u> occurs on the server side for each record in the spreadsheet. Records that pass this level of validation are filed in the event Capture Patient file (#721); records that fail this level of validation are not filed. Records that are filed are removed from the spreadsheet grid, leaving only those records containing errors.

  Each of the remaining records in the spreadsheet will have its associated error message(s) displayed in the Error Messages box. The errored record(s) can then be edited before retransmitting or deleting.

> **NOTE:** - To highlight the cell in the grid that most likely caused the error, select an error message. This will assist in identifying, and correcting, missing or invalid data.

What the User Will See

- A progress bar will display indicating what percentage of the upload is complete.
- Any failures or errors will be reported to the user.

#### Spreadsheet Upload Errors

During the upload process, misspelled names, blank spaces, misaligned columns, missing data such as answers to service connected questions, duplicate records and others can lead to upload errors. These must be cleared before the record(s) will upload. When upload errors occur, a list of all errors (Service Connected errors and others) is available for export by clicking the Create Error XLS button on the Spreadsheet Upload screen (Figure 77).

The following errors may display while uploading data to VistA via the Spreadsheet option:

- Record Number: When transmitting records, each row in the spreadsheet needs a unique record number (i.e., 1, 2, 3, etc.). If this field is blank, VistA validation will not be done.
- Delphi messages
- Error getting column with record number
- Record number is a mandatory field
- Location: The location must exist in the INSTITUTION file (#4) (also known as ^DIC(4,D0,0), where D0 is the location number). During the spreadsheet upload process, Locations are identified by their STA6A identifiers.
- VistA message
- Location not in Institution file (#4) — Invalid Station Number
- Pat SSN: The Patient SSN must exist on the PATIENT file (#2) (also known as global file ^DPT). If the SSN is shorter than 9 digits, it will be filled with leading zeroes. Do not use dashes in the SSN.
- VistA messages
- No SSN x-ref on PATIENT file (#2)
- No SSN entry on PATIENT file (#2)
- No internal entry on PATIENT file (#2) for SSN x-ref
- SSN does not match SSN on PATIENT file (#2)
- Patient LName and Patient FName: The patient’s name (last name, first name) must match the name on the PATIENT file (#2) for that SSN.
- Delphi messages
- Error getting column with Patient LName
- Patient LName must be at least 2 characters long
- VistA messages
- Patient last name does not match VistA
- Patient first name does not match VistA
- DSS Unit Name: If this field contains a value, then it must have a “B” cross-reference on the DSS UNIT file (#724). The DSS Unit Name is not required if the DSS Unit IEN contains a value.
- VistA message
- Invalid DSS Unit Name
- DSS Unit IEN: If this field contains a value, then it must exist on the DSS UNIT file (#724). The DSS Unit IEN is not required if the DSS Unit Name contains a value.
- VistA message
- Invalid DSS Unit IEN
- Proc Code: This is the Procedure or the CPT code value (not the description). A National Procedure, Local Procedure or CPT code is valid for this column. Either the Procedure must exist in the EC NATIONAL PROCEDURE file (#725), or the CPT must exist in the CPT file (#81). In addition, the Event Code Screen must be active for the Location, DSS Unit IEN, and Procedure/CPT combination. With functionality put in place by the Code Set Versioning project, only CPT codes that are active for the date and time of the event are processed.
- VistA messages
- Procedure or “D” x-ref not on EC NATIONAL PROCEDURE file (#725)
- Procedure invalid for this Location and DSS Unit
- Unable to check for active EC Event Code Screen
- Volume: The volume must be a number from 1 through 99.
- Delphi error messages
- Error getting column with Volume number
- Volume is a mandatory field
- Volume has a limit of 2 digits
- VistA messages
- Volume must be a number from 1 to 99
- Volume must contain numeric characters only
- Ordering Section: This is the name of the Ordering Section. Validation (against the “B” cross-reference in the MEDICAL SPECIALTY file (#723)) occurs for Ordering Section values used in the spreadsheet. If this field is blank, the program will derive the Ordering Section from the DSS UNIT file (#724) using the DSS Unit IEN. The record will then be transmitted to the Event Capture filer program.
- VistA message
- Invalid Ordering Section
- Unable to determine Ordering Section
- Prov Name or IEN: This is the Provider’s last and first name as it appears in the “B” cross-reference of the NEW PERSON file (#200). If the provider also has a middle initial, then it should be included (e.g., ‘ECPROVIDER, SEVEN J’). If the system finds a partial match for the name, the application will return the provider information (provider name, IEN, specialty, subspecialty, person class), and the user can then determine which provider is correct. The Provider Name must have a “B” cross-reference in the NEW PERSON file (#200), and the person class must be active.
- VistA messages
- Provider has no B x-ref on NEW PERSON file (#200)
- Unable to determine person class
- Provider does not have an active person class
- Enc Date/Time: The Encounter Date/Time can be in any valid FileMan format.
- Examples
- mm/dd/yy @hh:mm
- mm/dd/yyyy @hh:mm
- mm-dd-yy @hh:mm
- mmddyy @hhmm
- N, N-1, N-1H, etc.
- VistA message
- Invalid encounter date/time
- Category: The Category field can be blank. If the user enters a value, it needs to have a “B” cross-reference in the EVENT CAPTURE CATEGORY file (#726).
- VistA message
- Category “B” x-ref not on EC Category file (#726)
- Diag Code: This is the primary Diagnosis Code value. It must exist on the ICD DIAGNOSIS file (#80). With functionality put in place by the Code Set Versioning project, only ICD codes that are active for the date and time of the event process are valid. The Diagnosis Code is only required for records sent to PCE. The system ignores it otherwise.
- VistA messages
- Diagnosis code is required for this DSS Unit
- Unable to retrieve Diagnosis IEN
- Assoc Clinic: This is the Associated Clinic name. It must have a “B” cross-reference on the HOSPITAL LOCATION file (#44), be of type “C” (clinic), and be active for that encounter date. The Associated Clinic must have conforming stop codes to be selectable. The Associated Clinic is only required for records sent to PCE; otherwise, it will be ignored.
- VistA messages
- Associated Clinic is required for this DSS Unit
- Assoc Clin “B” x-ref not found on HOSPITAL LOCATION file (#44)
- Assoc Clin not found on HOSPITAL LOCATION file (#44)
- Associated Clinic must be of type "C" (clinic)
- Associated Clinic inactive for this encounter date
- Modifier (1 through 5): This is the Modifier, or Modifiers, associated with the procedure.
- VistA message
- Modifier is invalid or duplicated for the selected procedure

#### Service Connected Questions Validation

The Service Connected (SC) classification data validation and requirements are similar to those for records entered using other ECS data entry options. To assist the user in gathering SC information, Event Capture generates a spreadsheet of SC-related deficiencies found when transmitting the data.

When recording patient data in ECS using the spreadsheet menu and the ECS unit is set to send “ALL Records” to Patient Care Encounter (PCE), the SC classification data must also be entered. The care being entered into ECS must be identified as being related to the SC condition with the value of “Yes” or “No”. The records that are missing the SC data will fail the upload process and will be displayed in the Error Messages area at the bottom-left of the Spreadsheet Upload form.

When a row fails validation, a Create Error XLS button will appear above the Error Messages box (Figure 77).

<span id="_Ref94708289" class="anchor"></span>Figure 77: Service Connected Error Messages and Create Error XLS Button

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/090.png)

Click the button to generate an Excel spreadsheet, which the user can then save, print, or email to help resolve the errors. Service Connected errors are displayed on the “SC data required” tab (Figure 78). Any other errors (non-Service Connected errors) are displayed on the “Other errors” tab (Figure 79).

<span id="_Ref94708384" class="anchor"></span>Figure 78: Export Errors — SC Data Required

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/091.png)

<span id="_Ref94708448" class="anchor"></span>Figure 79: Export Errors — Other Errors

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/092.png)

#### Duplicate Record Errors

If the system detects duplicate records when the spreadsheet uploads, a File Duplicate Record(s) checkbox appears on the screen. The duplicate records display in the Error Messages box. Checking the File Duplicate Record(s) box and retransmitting the spreadsheet files the duplicate records in the EVENT CAPTURE PATIENT file (#721).

> **NOTE:** - Duplicate overrides can be disabled (or allowed) for any given DSS Unit.

- If an override is attempted for a DSS Unit where Allow Duplicate Override is set to No, the override will not succeed and will produce an error message similar to “The DSS Unit Associated with this record does not allow duplicate entries — Record NOT filed.”
- The Edit DSS Unit screen can be used by managers to allow or prevent duplicate overrides.

If the user-defined threshold of duplicate records is reached, a screen is displayed with the options to continue processing the records, change the threshold, or abort the upload (Figure 80).

<span id="_Ref94708524" class="anchor"></span>Figure 80: Duplicate Record Threshold Reached Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/093.png)

- Continue: Resets the counter and resumes processing records.
- Change: Allows the user to change the duplicate record threshold.
- This threshold can also be altered prior to starting the upload process by selecting the Change Duplicate Threshold option from the Spreadsheet Options menu or by clicking the Duplicate Threshold button.
- Abort: Terminates the upload process.

### Upload Completion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As records are processed, the uploaded rows will be cleared from the data grid, and a progress indicator will display the number of rows uploaded and the number of records in error (Figure 81). When all rows have been uploaded, both the data grid and the Error Messages list will be clear of all records.

<span id="_Ref94708573" class="anchor"></span>Figure 81: Spreadsheet Upload Progress Indicator

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/094.png)

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections describe the reports available within Event Capture. Users can print, preview, or export the report data.

### Reports Available to All Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Twelve reports are available to all ECS users. ECMGR security key holders have access to additional reports as described in [Section 4.3.2](#_Toc477526623). Test patient data are excluded from reports (except test patient data entered for DSS Units CH103–109).

Before the User Starts

The following reports are available to all users (including ECMGR key holders):

1.  
2.  [DSS Unit Activity Report](#dss-unit-activity-report)
1.  [DSS Unit Workload Report](#_DSS_Unit_Workload)
2.  [ECS Records Failing Transmission to PCE Report](#_ECS_Records_Failing)
3.  [Event Capture Encounters Report](#event-capture-encounters-report)
4.  [Ordering Section Summary Report](#_Toc477526612)
5.  [Patient Summary Report](\l)
6.  [PCE Data Summary Report](#pce-data-summary-report)
7.  [Possible Late State Home Entries Report](#_Possible_Late_State)
8.  [Procedure Reasons Report](#_Toc477526619)
9.  [Procedure Summary Report](\l)
10. [Procedures by Clinic Report](#procedures-by-clinic-report)
11. [Provider Summary Report](\l)
12. [Provider (1–7) Summary Report](#provider-17-summary-report)

What the User Will See

- A list of reports will be available in the Select Report area (Figure 82).
- The DSS Unit Activity Report will be the default selection, and the corresponding selection criteria will display on the right side of the screen.

<span id="_Ref94708888" class="anchor"></span>Figure 82: Reports Available to All Users

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/095.png)

#### DSS Unit Activity Report

The DSS Unit Activity Report allows the user to print, display, or export all patients for the specified location(s) and DSS Unit(s), within a selected date range (Figure 83).

- The report can be sorted by patient, provider, or SSN.
- If more than one location has been set up, choose one or all locations.
1.  Enter a data range.
133. Select one or all Location(s).
134. Select one or all DSS Unit(s).
135. Choose Sort Method (Patient, Provider, or SSN) for the report.

> **NOTE:** - Only the last four digits of the patient’s SSN will appear on the preview of this report.

- The column order does <u>not</u> change with Sort Method when exported into Excel.
136. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94709028" class="anchor"></span>Figure 83: DSS Unit Activity Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/096.png)

The Report Preview output (Figure 84) includes Patient Name, Last four digits of Patient SSN, Inpatient/Outpatient Indicator, Procedure Date and Time, Procedure Code, Procedure Name, Volume, Primary Diagnosis, Associated Clinic Name, Stop Code, Credit Stop, CHAR4 Code, Primary Provider, and Synonym. After previewing the report, the user will have the option to export, print or close the report.

<span id="_Ref94709107" class="anchor"></span>Figure 84: Report Preview — DSS Unit Activity Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/097.png)

The Export output produces the same information for the selected criteria, in Excel format (Figure 85).

<span id="_Ref94709162" class="anchor"></span>Figure 85: Export — DSS Unit Activity Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/098.png)![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/099.png)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/100.png)![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/101.png)

#### DSS Unit Workload Report

The DSS Unit Workload Report displays the number of procedures performed in each of the selected DSS Units. Refer to Figure 86 for an example of the report selection screen.

- With functionality put in place by the Code Set Versioning project, CPT codes, five-character EC National Codes (when applicable), CPT modifiers and their associated descriptions are reflective of the date the event occurred.
1.  Enter a date range.
137. Select one or all location(s).
138. Select one or all DSS Unit(s).
139. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref110336292" class="anchor"></span>Figure 86: DSS Unit Workload Report Selection Criteria

![Figure 87 shows the output for the DSS Unit Workload Preview option. If the DSS Unit uses categories, it will list the procedures in each category and how many were performed. It will also list the total number of procedures for the unit, at the bottom of the unit listing. After previewing the report, the user will have the option to export, print or close the report.](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/102.png)

*Figure 87 shows the output for the DSS Unit Workload Preview option. If the DSS Unit uses categories, it will list the procedures in each category and how many were performed. It will also list the total number of procedures for the unit, at the bottom of the unit listing. After previewing the report, the user will have the option to export, print or close the report.*

<span id="_Ref94709459" class="anchor"></span>Figure 87: Report Preview — DSS Unit Workload Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/103.png)

The Export option produces the same information for the selected criteria in Excel format (Figure 88).

<span id="_Ref94709507" class="anchor"></span>Figure 88: Export — DSS Unit Workload Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/104.png)

<span id="_ECS_Records_Failing" class="anchor"></span>

#### ECS Records Failing Transmission to PCE Report

The ECS Records Failing Transmission to PCE Report provides a list of encounters and the reasons why records were not transmitted to PCE. Refer to Figure 89 for an example of the report selection screen.

- Locations, DSS Units, procedures, five-character EC National Codes (when applicable), and categories must be defined before using this option.
1.  Select the date range.
140. Select One, Multiple or All Locations
141. Select One, Multiple or All DSS Units
142. Select to Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94709578" class="anchor"></span>Figure 89: ECS Records Failing Transmission to PCE Report Selection Criteria

![Figure 90 shows the output for the Preview option of the ECS Records Failing Transmission to PCS Report. The Procedure Date/Time, Location, DSS Unit, Patient, Procedure, Category, last four digits of the Patient’s SSN, Provider(s) of care and Reasons for transmission failure are listed on the report. After previewing the report, the user has the option to export, print or close the report.](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/105.png)

*Figure 90 shows the output for the Preview option of the ECS Records Failing Transmission to PCS Report. The Procedure Date/Time, Location, DSS Unit, Patient, Procedure, Category, last four digits of the Patient’s SSN, Provider(s) of care and Reasons for transmission failure are listed on the report. After previewing the report, the user has the option to export, print or close the report.*

<span id="_Toc477526774" class="anchor"></span>Figure 90: Report Preview — ECS Records Failing Transmission to PCE Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/106.png)

The Export option produces the same information for the selected criteria in Excel format (Figure 91).

<span id="_Toc477526776" class="anchor"></span>Figure 91: Export — ECS Records Failing Transmission to PCE Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/107.png)![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/108.png)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/109.png)![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/110.png)

#### Event Capture Encounters Report

This option allows you to print/display/export Event Capture encounter data within a specified date range for selected locations and DSS units. Refer to Figure 92 to view the report selection screen.

- The report displays and counts the sum of occurrences by patient and DSS Unit during a selected date range. It also enables sorting by patient, provider, or clinic.
- Sorting by Patient (Figure 94) shows the sum of occurrences for the Patient across the date range that is selected.
- Sorting by Provider (Figure 95) shows the sum of occurrences for the Provider across the date range that is selected.
- Sorting by Clinic (Figure 96) shows the sum of occurrences for the Clinic across the date range that is selected.
- The report includes the fields Patient Name, SSN (last 4 digits), Inpatient or Outpatient (I/O), Date/Time, Provider \#1, DSS Unit and Volume.
1.  Select a date range.
143. Select one or all Locations.
144. Select one, all, or multiple DSS Unit(s).
145. Select Sort Method (Patient, Provider or Clinic).

<span id="_Ref94710635" class="anchor"></span>Figure 92: Event Capture Encounters Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/111.png)

146. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

- Only the last four digits of the patient’s SSN will appear on the preview of this report.

A report timeout warning and message dialog are displayed when All Locations, All DSS units, or large date ranges are selected (Figure 93).

<span id="_Ref110336348" class="anchor"></span>Figure 93: Event Capture Encounters Report Timeout Warning

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/112.png)

The preview output includes the Patient Name, SSN (last 4 digits), Inpatient or Outpatient (I/O), Date/Time, Provider \#1, DSS Unit, Volume, Clinic, Stop Code, Credit Stop Code, CHAR4 Code and MCA Labor Code.

The appearance of the report will vary slightly depending on the sort method selected (see Figure 94, Figure 95 and Figure 96).

<span id="_Ref94710762" class="anchor"></span>Figure 94: Report Preview — Event Capture Encounters Report Sorted by Patient

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/113.png)

<span id="_Ref94710780" class="anchor"></span>Figure 95: Report Preview — Event Capture Encounters Report Sorted by Provider

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/114.png)

<span id="_Ref94710793" class="anchor"></span>Figure 96: Report Preview — Event Capture Encounters Report Sorted by Clinic

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/115.png)

> **NOTE:** - The Export option produces the same information for the selected criteria in Excel format (Figure 97).

- The column order does not change with Sort Method when exported into Excel

<span id="_Ref94710849" class="anchor"></span>Figure 97: Export — Event Capture Encounters Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/116.png)

<span id="_Toc477526612" class="anchor"></span>

#### Ordering Section Summary Report

The Ordering Section Summary Report allows the user to print/display procedures ordered within a specified date range for a selected ordering section. Refer to Figure 98 for an example of the report selection screen.

- The design of this report is for a 132-column format.
- With functionality put in place by the Code Set Versioning project, CPT codes, five-character EC National Codes (when applicable), CPT modifiers and their associated descriptions are reflective of the date the event occurred.
- After previewing the report, the user will have the option to export, print or close the report.
1.  Enter a date range.
147. Select an Ordering Section.
148. Select a specific or all Location(s).
149. Select one, multiple, or all DSS Unit(s).
150. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref110336431" class="anchor"></span>Figure 98: Ordering Section Summary Report Selection Criteria

![Figure 99 is an image of the Ordering Section Summary Report from Preview.](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/117.png)

*Figure 99 is an image of the Ordering Section Summary Report from Preview.*

<span id="_Ref94710974" class="anchor"></span>Figure 99: Report Preview — Ordering Section Summary Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/118.png)

The Export option produces the information for the selected criteria in Excel format (Figure 100).<span id="_Toc477526787" class="anchor"></span>

Figure 100: Export — Ordering Section Summary Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/119.png) ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/120.png)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/121.png)![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/122.png)

#### Patient Summary Report

The Patient Summary Report allows the user to print/display procedure-related data within a specified date range for a selected patient. Refer to Figure 101 to view the report selection screen.

- The design of this report is for a 132-column format.
- With functionality put in place by the Code Set Versioning project, CPT codes, five-character EC National Codes (when applicable), CPT modifiers and their associated descriptions are reflective of the date the event occurred.
- The user can choose to include Procedure Reasons (EVENT CAPTURE PATIENT file (#721)) on the report. Up to three reasons will be included.
- The “Display Reasons on this report” option will clear when the user selects another report or upon exiting the screen.
- After previewing the report, the user will have the option to export, print or close the report (Figure 102).
1.  Enter a date range.
151. Use the Patient Identifier field to select a patient.
- Enter one of the following:
- Patient Name (whole or partial, last name first)
- Social Security Number
- Last four digits of the Patient Social Security Number
- First character of Last Name plus the last four digits of the SSN with no spaces
- Press \<Enter\> on the keyboard or click the Binoculars (Search) button.
- Choose from the list of patients displayed.
152. Click the Display Reasons on this report checkbox to include Procedure Reasons in the report (Figure 104).
153. Export, Preview, Print, or Cancel the report.

> Note:

- When printing, the default printer is the device most recently used.

<span id="_Ref94711180" class="anchor"></span>Figure 101: Patient Summary Report (without Reasons) — Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/123.png)

<span id="_Ref94711224" class="anchor"></span>Figure 102: Patient Summary Report (without Reasons) — Report Preview

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/124.png)

The Export option produces the information for the selected criteria in Excel format (Figure 103).

<span id="_Toc477526791" class="anchor"></span>Figure 103: Patient Summary Report (without Reasons) — Export

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/125.png) ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/126.png)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/127.png) ![Figure 105 and Figure 106 show examples of this report when the “Display Reasons on this report” option is selected on the report criteria screen (Figure 104).](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/128.png)

*Figure 105 and Figure 106 show examples of this report when the “Display Reasons on this report” option is selected on the report criteria screen (Figure 104).*

<span id="_Ref95304371" class="anchor"></span>Figure 104: Patient Summary Report (with Reasons) — Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/129.png)

<span id="_Ref95304322" class="anchor"></span>Figure 105: Patient Summary Report (with Reasons) — Report Preview

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/130.png)

The Export option produces the information for the selected criteria in Excel format (Figure 106).

<span id="_Ref94711374" class="anchor"></span>Figure 106: Patient Summary Report (with Reasons) — Export

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/131.png) ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/132.png)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/133.png) ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/134.png)

#### PCE Data Summary Report

The PCE Data Summary Report allows the user to print/display procedure data that was sent to the PCE software for a selected patient within a specified date range. Refer to Figure 107 to view the report selection screen.

- The design of this report is for a 132-column format.
- With functionality put in place by the Code Set Versioning project, CPT codes, five-character EC National Codes (when applicable), CPT modifiers, diagnosis codes and their associated descriptions are reflective of the date the event occurred.
1.  Enter a date range.
154. Use the Patient Identifier field to select a patient.
- Enter one of the following:
- Patient Name (whole or partial, last name first)
- Social Security Number
- Last four digits of the Patient Social Security Number
- First character of Last Name plus the last four digits of the SSN with no spaces
- Press \<Enter\> on the keyboard or click the Binoculars (Search) button.
- Choose from the list of patients displayed.
155. Export, Preview, Print, or Cancel the report.

<span id="_Ref110336666" class="anchor"></span>Figure 107: PCE Data Summary Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/135.png)

The Preview option output includes Patient Name, Date Range, Date/Time of procedure, Procedure Name (as sent to PCE), Volume, Provider, Location, Associated Clinic, Stop Code, Credit Stop Code, CHAR4 Code, MCA Labor Code, CPT Code, ICD-10 code and Modifier(s) (Figure 108). After previewing the report, the user has the option to export, print or close the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Toc477526798" class="anchor"></span>Figure 108: Report Preview — PCE Data Summary Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/136.png)

The Export option produces the information for the selected criteria in Excel format (Figure 109).

<span id="_Toc477526800" class="anchor"></span>Figure 109: Export — PCE Data Summary Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/137.png)

<span id="_Possible_Late_State" class="anchor"></span>

#### Possible Late State Home Entries Report

The Possible Late State Home Entries Report lists all possible late State Veterans Home entries for the selected date range. These are State Veterans Home records that were entered for prior months that could be included in a previously completed ECS Extract. Refer to Figure 110 for an example of the report selection screen.

> **NOTE:** - Late State Home entry reporting is limited to the current fiscal year. Late State Home records for previous fiscal years are not processed and will not be included on this report.

1.  Select a date range.
156. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94711662" class="anchor"></span>Figure 110: Possible Late State Home Entries Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/138.png)

The preview output includes the DSS Unit, Location, Patient Name, last 4 digits of SSN (full on export), Procedure Date/Time, Entered Date/Time, Entered By (export only), Procedure, Volume and Primary Provider. After previewing the report, the user will have the option to export, print or close the report.

<span id="_Toc38456194" class="anchor"></span>Figure 111: Report Preview — Possible Late State Home Entries Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/139.png)

The Export option produces the information for the selected criteria in Excel format (Figure 112).

<span id="_Toc67310306" class="anchor"></span>Figure 112: Export — Possible Late State Home Entries Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/140.png)

#### Procedure Reasons Report

The Procedures Reasons Report lists the reasons entered for Event Capture Procedures. Refer to Figure 113 for an example of the report selection screen.

> **NOTE:** - Locations, DSS Units, procedures, and procedure reasons must be defined before using this option.

- With functionality put in place by the Code Set Versioning project, CPT codes, five-character EC National Codes (when applicable), CPT modifiers, diagnosis codes and their associated descriptions are reflective of the date the event occurred.
1.  Select a date range.
157. Select one, all, or multiple Location(s).
158. Select one, all, or multiple Procedure Reasons.
159. Select one, all, or multiple DSS Unit(s).
160. Export, Preview, Print, or Cancel the report.

<span id="_Toc477526802" class="anchor"></span>Figure 113: Procedure Reasons Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/141.png)

The report preview output includes the Location, DSS Unit, Procedure Reason, the number of times the reason was used, Procedure Code, Procedure Name, Patient Name, last four digits of Patient SSN, Provider Name, and Date and Time of the procedure (Figure 114). After previewing the report, the user has the option to export, print or close the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94711991" class="anchor"></span>Figure 114: Report Preview — Procedure Reasons Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/142.png)

This report is exportable into an Excel spreadsheet. The tab in Excel is titled “Reasons” followed by the Date Range the user selected (Figure 115).

<span id="_Toc477526805" class="anchor"></span>Figure 115: Export — Procedure Reasons Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/143.png)

<span id="_Toc477526619" class="anchor"></span>

#### Procedure Summary Report

The Procedure Summary Report lists the patients seen for a selected Procedure with one or all Providers within a defined date range for selected Locations and DSS Units.

The selection criteria include Date Range, Provider(s), Location(s), DSS Unit(s), and Procedure.

Refer to Figure 116 for an example of the report selection screen.

1.  Enter a date range.
161. Select one or all Provider(s)
162. Select one, all, or multiple Location(s)
163. Select one, all, or multiple DSS Unit(s)
164. Select a Procedure
165. Export, Preview, Print, or Cancel the report

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94712083" class="anchor"></span>Figure 116: Procedure Summary Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/144.png)

The Preview output (Figure 117) includes the following:

The report header - Displayed at the top of the report. If a single DSS Unit is selected, the header will only be shown once. If multiple DSS Units or \<ALL\> DSS Units are selected, the header will be displayed every time records for a new DSS Unit are processed.

The report sub-header - Every time a new Location/DSS Unit combination is encountered, lines denoting the Location and DSS Unit are displayed.

Detail lines:

- Column header for the first detail line is “Category”.
- Column headers for the second detail line are “CPT Code”, ”Proc Code”, “Procedure Name”, “# UNIQUES” and “Volume\*”.
- Column header for the third detail line is “CPT Modifier (Volume)”.

Subtotal/Total lines:

- The “Totals for \[PROVIDER\]” line is displayed when a provider changes. This line displays the total number of unique patients seen by the provider for the selected procedure, and the total number of times the selected procedure was performed by the provider.
- The “Grand Totals for \[DSS UNIT\]” line is displayed when a DSS Unit changes. This line displays the Grand Total of unique patients seen for a selected procedure, as well as the Grand Total of times the selected procedure was completed for the DSS Unit.

> **NOTE:** - On the Grand Totals, the \# UNIQUES is not always the sum of all \# UNIQUES since each patient is only counted once for the selected procedure regardless of the number of times a patient is seen by other providers.

- If no records exist for the selected criteria, the following message is displayed to the user: “No data to report for the date range selected”.

<span id="_Ref94712131" class="anchor"></span>Figure 117: Preview — Procedure Summary Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/145.png)

The Export option produces the information for the selected criteria in Excel format (Figure 118)

<span id="_Ref95317128" class="anchor"></span>Figure 118: Export — Procedure Summary Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/146.png)

#### Procedures by Clinic Report

The Procedures by Clinic Report allows the user to print, preview, or export procedures used by a selected clinic.

The selection criteria include Date Range, Sort Method, Location, Clinic, and DSS Unit(s). Refer to Figure 119 for an example of the report selection screen.

1.  Enter a date range.
2.  Select Sort Method of Date or Patient.
3.  Select a Location.
4.  Select a Clinic.
5.  Select one, multiple, or all DSS Units.
6.  Export, Preview, Print, or Cancel the report.

<span id="_Ref127383145" class="anchor"></span>Figure 119: Procedures by Clinic Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/147.png)

The report preview (Figure 120) separates the output by DSS Unit. Each DSS Unit displays the Patient, SSN, Procedure Date/Time, Procedure Code, Procedure Name, Procedure Volume, and Provider.

<span id="_Ref127383189" class="anchor"></span>Figure 120: Preview — Procedures by Clinic Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/148.png)

The exportable version of the “Procedures by Clinic Report” displays the Location, DSS Unit (IEN \#), Clinic, Patient, SSN, Date of Procedure, Procedure Code, Procedure Name, Volume, and Provider Name (Figure 121).

<span id="_Ref127383264" class="anchor"></span>Figure 121: Export — Procedures by Clinic Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/149.png)

#### Provider Summary Report

The Provider Summary Report allows the user to print, preview, or export the number of procedures performed for one or all locations and one or all DSS Units within a specified date range. Within each DSS Unit for each location, the report is sorted by provider, category (if the DSS Unit is defined to sort procedures by category), and procedures (listed alphabetically). Refer to Figure 122 for an example of the report selection screen.

> **NOTE:** - Locations, DSS Units, categories, procedures, and procedure reasons must be defined before generating this report.

- The design of this report is for a 132-column format.
- With functionality put in place by the Code Set Versioning project, CPT codes, five-character EC National Codes (when applicable), CPT modifiers and their associated descriptions are reflective of the date the event occurred.
1.  Enter a date range.
166. Select one or all Location(s).
167. Select one or all DSS Unit(s).
168. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94712307" class="anchor"></span>Figure 122: Provider Summary Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/150.png)

The preview option output includes Location, DSS Unit, Provider, Category (if applicable), CPT Code, Procedure Code, Procedure Name, Procedure Reason, Volume, Modifier(s), and Total number of procedures performed by the provider within the specified date range (Figure 123).

> **NOTE:** - If Procedure Reason \#1 is not listed, the report prints “Reason Not Defined”.

<span id="_Ref94692682" class="anchor"></span>Figure 123: Preview — Provider Summary Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/151.png)

The Export option produces the information for the selected criteria in Excel format (Figure 124).

<span id="_Toc477526809" class="anchor"></span>Figure 124: Export — Provider Summary Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/152.png)

#### Provider (1–7) Summary Report

The Provider (1–7) Summary Report summarizes the workload of providers for a selected date showing how many times a specific procedure was performed on a patient with the selected provider. This report provides the ability to view up to seven provider numbers for providers within a Location/DSS Unit. Refer to Figure 125 to view the report selection screen.

> **NOTE:** - The design of this report is for a 132-column format.

- With functionality put in place by the Code Set Versioning project, CPT codes, five-character EC National Codes (when applicable), CPT modifiers and their associated descriptions are reflective of the date the event occurred.
1.  Enter a date range.
169. Enter the name of a Provider.
170. Select one, all or multiple Location(s).
171. Select one, all, or multiple DSS Unit(s).
172. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94712472" class="anchor"></span>Figure 125: Provider (1–7) Summary Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/153.png)

The Preview option output includes Procedure Code, Procedure Name, Patient Name, Last four digits of patient SSN, a matrix showing how many times a specific procedure was performed on a specific patient with the selected provider as Provider 1, Provider 2, to Provider 7, Modifier(s), Subtotals by procedure, and Grand Total of procedures (Figure 126) After previewing the report, the user has the option to export, print or close the report.

<span id="_Ref94712531" class="anchor"></span>Figure 126: Preview — Provider (1–7) Summary Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/154.png)

The Export option produces the information for the selected criteria in Excel format (Figure 127).

<span id="_Ref94712650" class="anchor"></span>Figure 127: Export — Provider (1–7) Summary Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/155.png)

<span id="_Toc477526623" class="anchor"></span>

### Reports Available to ECMGR Key Holders Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reports are available only to ECMGR key holders:

1.  [Category Report](#category-report)
13. [Disabled Category and Procedure Summary](#disabled-category-and-procedure-summary)
14. [DSS Units with any Associated Stop Code Errors](#_DSS_Units_with)
15. [DSS Units/Event Code Screens for Selected Procedure Code Report](#_Toc477526631)
16. [DSS Unit User Access Report](#_Toc477526633)
17. [Event Capture Edit Log Report](#event-capture-edit-log-report)
18. [Event Code Screens with CPT Codes Report](#_Toc477526635)
19. [Event Code Screens with Inactive Default Associated Clinic](#_Event_Code_Screens_2)
20. [Inactive Person Class Report (IPC)](#_Toc477526639)
21. [National / Local Procedure Codes with Inactive CPT Codes](#_Toc477526641)
22. [National / Local Procedure Report](#nationallocal-procedure-report-active-procedures)
23. [Print Category and Procedure Summary (Report)](#print-category-and-procedure-summary-report)
24. [Send No Records DSS Units Report](#send-no-records-dss-units-report)

ECMGR reports are displayed in the Select Report area, below the asterisk line (Figure 128).

<span id="_Ref94712700" class="anchor"></span>Figure 128: Report Selection Screen for ECMGR Key Holders

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/156.png)

#### Category Report

The Category Report allows Management users to print, preview, or export the established local categories. This report can be generated for active categories, inactive categories, or all categories. For inactive categories, the inactive date is included in the output. Refer to Figure 129 for an example of the report selection screen.

> **NOTE:** - Use the Category — Add or Update Categories option to create categories before selecting this report.

1.  Select the report.
173. Choose a status of Active, Inactive, or Both.
174. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94712750" class="anchor"></span>Figure 129: Category Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/157.png)

Selecting Active and then Preview produces output showing the list of active categories (Figure 130). After previewing the report, the user has the option to export, print or close the report.<span id="_Toc477849737" class="anchor"></span>

Figure 130: Report Preview — Category Report (Active)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/158.png)

The Export option produces the information for the selected criteria in Excel format (Figure 131).

<span id="_Ref94713286" class="anchor"></span>Figure 131: Export — Category Report (Active)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/159.png)

Selecting Inactive and then Preview produces output that displays inactive categories (Figure 132).

<span id="_Ref94713340" class="anchor"></span>Figure 132: Report Preview — Category Report (Inactive)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/160.png)

The Export option produces the information for the selected criteria in Excel format (Figure 133).

<span id="_Ref94713381" class="anchor"></span>Figure 133: Export — Category Report (Inactive)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/161.png)

Selecting Both and then Preview produces output that displays both active and inactive categories (Figure 134).

<span id="_Ref94713420" class="anchor"></span>Figure 134: Report Preview — Category Report (Both Active and Inactive)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/162.png)

The Export option produces the information for the selected criteria in Excel format (Figure 135).

<span id="_Toc477526822" class="anchor"></span>Figure 135: Export — Category Report (Both Active and Inactive)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/163.png)

#### Disabled Category and Procedure Summary 

This report allows Management users to print, preview, or export the ECS categories that have been disabled for one or all DSS Units within a specified location. Event Code Screens that are comprised of DSS Units that allow category use and have Event Code Screens defined using the disabled category will appear on this report. Refer to Figure 136 for an example of the report selection screen.

1.  Select the report.
175. Select one, all, or multiple Location(s).
176. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Toc477526824" class="anchor"></span>Figure 136: Disabled Category and Procedure Summary Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/164.png)

The report preview output includes the Run Date, Location, Service, DSS Unit Name and IEN, Send Status, and DSS Dept. For each disabled procedure, the report also includes Procedure Code, Procedure Name, Synonym, Clinic IEN, Clinic, Stop Code, Credit Stop Code, CHAR4 Code and MCA Labor Code (Figure 137). After previewing the report, the user has the option to export, print or close the report.<span id="_Toc455135788" class="anchor"></span>

Figure 137: Report Preview — Disabled Category and Procedure Summary

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/165.png)

The Export option produces the information for the selected criteria in Excel format (Figure 138). The exported output includes EC Screen Status, Location, Service, DSS Unit, DSS Unit IEN, DSS Dept., Send Status, DSS Unit Inactive, Disabled Category, CPT Code, Procedure Code, Procedure Name, Synonym, Clinic IEN, Clinic, Clinic Stop Code, Credit Stop Code, CHAR4 Code and MCA Labor Code.

<span id="_Ref94713833" class="anchor"></span>Figure 138: Export — Disabled Category and Procedure Summary

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/166.png)

#### DSS Units with any Associated Stop Code Errors Report

The Event Capture software restricts DSS-only workload to using valid Stop Codes. This report provides Management users a list of DSS Units with any error with the Associated Stop Code. Refer to Figure 139 for an example of the report selection screen.

> **NOTE:** - To assist sites in locating DSS Units that have invalid associated Stop Codes, the DSS Unit list with Secondary Associated Stop Codes is provided. This may be attached as a secondary menu option and run as often as needed. The only prompt is for Device.

- Select an active, non-secondary Stop Code to replace the Stop Code in the DSS Unit set up.
1.  Select the report.
177. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Toc455135791" class="anchor"></span>Figure 139: DSS Units with Any Associated Stop Code Errors Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/167.png)

The report preview produces output that includes the DSS Unit IEN and name, Associated Stop Code IEN and name, and the reason for the error (Figure 140). After previewing the report, the user has the option to export, print or close the report.

<span id="_Toc477526829" class="anchor"></span>Figure 140: Report Preview — DSS Units with Any Associated Stop Code Errors

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/168.png)

The Export option produces the information in Excel format (Figure 141).

<span id="_Toc477526831" class="anchor"></span>Figure 141: Export — DSS Units with Any Associated Stop Code Errors

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/169.png)

<span id="_Toc477526631" class="anchor"></span>

#### DSS Units/Event Code Screens for Selected Procedure Code Report

The DSS Units/Event Code (EC) Screens for Selected Procedure Code Report allows Management users to print, preview, or export DSS unit and EC screen data for a selected procedure code and specified locations. Refer to Figure 142 for an example of the report selection screen.

> **NOTE:** - The design of this report is for a 132-column format.

1.  Select the report.
178. Select one, all, or multiple Location(s).
179. Select a Procedure.
180. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94714350" class="anchor"></span>Figure 142: DSS Units/Event Code Screens for Selected Procedure Code Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/170.png)

<span id="_Toc190948623" class="anchor"></span>Figure 143: Report Preview — DSS Units/Event Code (EC) Screens for Selected Procedure Code Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/171.png)

This report is exportable into an Excel spreadsheet (Figure 144). The tab in Excel is titled “Selected Procedure Code”.

<span id="_Ref94714465" class="anchor"></span>Figure 144: Export — DSS Units/Event Code (EC) Screens for Selected Procedure Code Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/172.png)

<span id="_Toc477526633" class="anchor"></span>

#### DSS Unit User Access Report

The DSS Unit User Access Report allows Management users to print, preview, or export information regarding user with access to DSS unit data for specified locations and DSS units. Refer to Figure 145 for an example of the report selection screen.

> **NOTE:** - Similar information is available using the Management Menu \> Access by User option (Refer to [Section 4.4.3](#to-grant-access-to-a-dss-unit), Grant Access to DSS Units by User).

1.  Select the report.
181. Select one or all Location(s).
182. Select one, all, or multiple DSS Units.
183. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref110334207" class="anchor"></span>Figure 145: DSS Unit User Access Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/173.png)

The report preview produces output that includes DSS Unit Name, User Name, User IEN (from the New Person (#200) file), and Person Class/Classification (Figure 146). After previewing the report, the user has the option to export, print or close the report.

<span id="_Ref94714705" class="anchor"></span>Figure 146: Report Preview — DSS Unit User Access Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/174.png)

This report is exportable into an Excel spreadsheet (Figure 147). The tab in Excel is titled “DSS Unit User Access Report” and includes the information for the selected criteria.

<span id="_Ref94714739" class="anchor"></span>Figure 147: Export — DSS Unit User Access Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/175.png)

<span id="_Toc477526635" class="anchor"></span>

#### Event Capture Edit Log Report

This report displays the Entered or Edited by Staff Name field, in addition to the Location, DSS Unit, Procedure, Date of Procedure, Patient Name, last 4 digits of Patient SSN and Provider Name.

The selection criteria include Date Range, Sort Method, Location, and DSS Unit(s). Refer to Figure 148 for an example of the report selection screen.

1.  Select Date Range.
2.  Select Sort Method: Procedure Date or Staff Member.
3.  Select Location.
4.  Select One, Multiple, or All DSS Units.
5.  Export, Preview, Print, or Cancel the report.

<span id="_Ref127382859" class="anchor"></span>Figure 148: Event Capture Edit Log Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/176.png)

The Event Capture Edit Log Report output (Figure 149) is separated by DSS Unit and displays the Patient, last 4 digits of SSN, Procedure, Date of Procedure, Provider Name, and Entered/Edited by Staff Name fields.

<span id="_Ref127382920" class="anchor"></span>Figure 149: Preview — Event Capture Edit Log Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/177.png)

The exportable version of the Event Capture Edit Log Report (Figure 150) displays the Location, DSS Unit (IEN#), Patient, entire SSN, Procedure, Date of Procedure, Provider Name, and Entered or Edited by Staff Name fields.

<span id="_Ref127382963" class="anchor"></span>Figure 150: Export – Event Capture Edit Log Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/178.png)

#### Event Code Screens with CPT Codes Report

This option allows holders of the ECMGR key to print, preview, or export Event Code Screens with active and/or inactive CPT codes for one or all specific DSS Unit(s). Refer to Figure 151 for an example of the report selection screen.

1.  Select the report.
184. Select One or all Location(s).
185. Select one or all DSS Unit(s).

> **NOTE:** - If “All” is selected for the DSS Unit, the Category will also be set to “All” and will be disabled.

186. Select a Category.

> **NOTE:** - Categories only appear if the Event Code Screen uses categories to group procedures.

187. Select Active, Inactive, or Both (Active and Inactive) CPT Codes.
188. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94714779" class="anchor"></span>Figure 151: Event Code Screens with CPT Codes Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/179.png)

The report preview output includes Run Date and Time, Location, DSS Unit, Category, Procedure Name, National Number, CPT Code, Synonym, Associated Clinic, Stop Code, Credit Stop, CHAR4 Code and MCA Labor Code (Figure 152). After previewing the report, the user has the option to export, print or close the report.

> **NOTE:** - Inactive CPT codes are flagged with an \*I\* when printing both active and inactive codes.

- Category, Synonym, Associated Clinic and MCA Labor Code are included only when data is available for those items.

<span id="_Ref94714858" class="anchor"></span>Figure 152: Preview — Event Code Screens with CPT Codes Report

(Both Active and Inactive CPT Codes Selected)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/180.png)

This report is exportable into an Excel spreadsheet. The tab of the exported report indicates whether the report shows only active, only inactive, or both active and inactive CPT codes (Figure 153). When exporting the report, all Inactive CPT codes are flagged with an \*\*Inactive\*\* indicator.

<span id="_Ref94714918" class="anchor"></span>Figure 153: Event Code Screens with CPT Codes Report from Export

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/181.png)

#### Event Code Screens with Inactive Default Associated Clinic

The Event Code Screens with Inactive Default Associated Clinic report allows Management users to print, preview, or export inactive default associated clinic data for specified locations and DSS units. Refer to Figure 154 for an example of the report selection screen.

1.  Select the report.
189. Select one, all, or multiple Location(s).
190. Select one, all, or multiple DSS Unit(s).
191. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94714964" class="anchor"></span>Figure 154: Event Code Screens with Inactive Default Associated Clinic Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/182.png)

The report preview output includes DSS Unit Name, Location, Category, Procedure Code, Clinic IEN, and Clinic Name (Figure 155). After previewing the report, the user has the option to export, print or close the report.

<span id="_Toc477526844" class="anchor"></span>Figure 155: Preview — Event Code Screens with Inactive Default Associated Clinic

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/183.png)

The Export option produces the information for the selected criteria in Excel format (Figure 156).

<span id="_Ref94716166" class="anchor"></span>Figure 156: Export — Event Code Screens with Inactive Default Associated Clinic

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/184.png)

<span id="_Toc477526639" class="anchor"></span>

#### Inactive Person Class Report (IPC)

The Inactive Person Class Report (IPC) allows Management users to identify providers who do not have an assigned person class or an active person class in the NEW PERSON file (#200) for the date of the procedure. Refer to Figure 157 for an example of the report selection screen.

1.  Select the report.
192. Enter a date range.
193. Select Sort by Patient or Sort by Procedure.
194. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94771484" class="anchor"></span>Figure 157: Inactive Person Class Report Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/185.png)

The report preview output displays the Patient Name, SSN (last four), Date of Procedure, Provider, and any Errors (Figure 158). After previewing the report, the user has the option to export, print or close the report.

<span id="_Ref94771552" class="anchor"></span>Figure 158: Preview — Inactive Person Class Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/186.png)

The Export option produces the information for the selected criteria in Excel format (Figure 159).

> **NOTE:** - The column order does not change with Sort Order when exported into Excel.

<span id="_Ref94771589" class="anchor"></span>Figure 159: Export — Inactive Person Class Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/187.png)

<span id="_Toc477526641" class="anchor"></span>

#### National/Local Procedure Codes with Inactive CPT Codes

This report allows Management users to see a list of National and Local Procedure Codes with inactive CPT codes from the EC NATIONAL PROCEDURE file (#725). Refer to Figure 160 for an example of the report selection screen.

1.  Select the report.
195. Select the Preferred Report (National, Local, or Both)
196. Select the Sort Method (Procedure Name, Procedure Number, CPT Code, or CPT Inactive Date)
197. Select the Sort Order (Ascending or Descending)
198. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94771654" class="anchor"></span>Figure 160: National/Local Procedure Codes with Inactive CPT Codes Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/188.png)

The report preview header displays the user’s selected criteria (preferred report type and sort method), as well as the run date. The content of the report includes the Procedure Number, Procedure Name, CPT Code, and the Inactive Date (Figure 161). After previewing the report, the user has the option to export, print or close the report.

<span id="_Ref94771697" class="anchor"></span>Figure 161: Report Preview — National/Local Procedure Codes with Inactive CPT Codes Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/189.png)

The Export option produces the information for the selected criteria in Excel format (Figure 162).

<span id="_Toc477526852" class="anchor"></span>Figure 162: Export — National/Local Procedure Codes with Inactive CPT Codes Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/190.png)

#### National/Local Procedure Report — Active Procedures

The National/Local Procedures Report allows Management users to display a listing of Event Capture active or inactive procedures (See section 4.3.2.12 for an overview of the report for Inactive Procedures). Refer to Figure 163 to view the report selection screen.

> **NOTE:** - Use the Procedure — Add or Update Local Procedures option to create local procedures before using this option.

1.  Select the report.
199. Choose Active.
200. Choose a Preferred Report (National, Local, or Both).
201. Choose the Sort Method (Procedure Name or Procedure Number).
202. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Toc477526854" class="anchor"></span>Figure 163: National/Local Procedure Report (Active) Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/191.png)

For active procedures, the report preview output includes the user’s selected criteria (report type and sort method) in the header information. The report content includes the Procedure Name, Procedure Number, and CPT (Figure 164). After previewing the report, the user has the option to export, print or close the report.

<span id="_Toc477526856" class="anchor"></span>Figure 164: Report Preview — National/Local Procedure Report (Active)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/192.png)

The Export option produces the information for the selected criteria in Excel format (Figure 165).

<span id="_Toc477526858" class="anchor"></span>Figure 165: Export — National/Local Procedure Report (Active)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/193.png)

#### National/Local Procedure Report — Inactive Procedures

The National/Local Procedures Report allows Management users to display a listing of Event Capture active or inactive procedures (See [section](#nationallocal-procedure-report-active-procedures) 4.3.2.11 for an overview of the report for Active Procedures). Refer to Figure 166 to view the report selection screen.

> **NOTE:** - Use the Procedure — Add or Update Local Procedures option to create local procedures before using this option.

1.  Select the report.
203. Select Active or Inactive.

> **NOTE:** - Selecting the Inactive radio button disables the Preferred Report and Sort Method options.

204. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94772209" class="anchor"></span>Figure 166: National/Local Procedure Report (Inactive) Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/194.png)

For inactive procedures, the report preview output includes Procedure Name, Procedure Number, CPT, and the Inactive Date (Figure 167). After previewing the report, the user has the option to export, print or close the report.

<span id="_Ref94772427" class="anchor"></span>Figure 167: Preview — National/Local Procedure Report (Inactive)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/195.png)

The Export option produces the information for the selected criteria in Excel format (Figure 168).

<span id="_Toc477526862" class="anchor"></span>Figure 168: Export — National/Local Procedure Report (Inactive)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/196.png)

#### Print Category and Procedure Summary (Report)

The Print Category and Procedure Summary Report allows Management users to print, display, and export the Event Code Screens for one or all DSS Units within a specified location. Locations, DSS Units, local categories, and procedures must be defined before using this option. Refer to Figure 169 for an example of the report selection screen.

> **NOTE:** - Use the DSS Unit — Add or Update DSS Units option to create DSS Units categories before using this option.

- Use the Category — Add or Update Categories option to create categories before using this option.
- Use the Procedure — Add or Update Local Procedures option to create procedures before using this option.
1.  Select one or all Location(s).
2.  Select Active, Inactive or Both (Active and Inactive) DSS Units.
205. Select one, all, or multiple DSS Unit(s).
206. Select Active, Inactive or Both (Active and Inactive) Event Code Screens.
207. Export, Preview, Print or Cancel the report

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Ref94772510" class="anchor"></span>Figure 169: Print Category and Procedure Summary (Report) Selection Criteria

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/197.png)

The report preview output includes Run Date, Location, Service, DSS Unit, Send Status, DSS Dept., Category (if applicable), Procedure Code, Procedure Name, Synonym, Associated Clinic IEN (if applicable), Associated Clinic (if applicable), Stop Code, Credit Stop Code, CHAR4 Code and MCA Labor Code (Figure 170). After previewing the report, the user has the option to export, print or close the report.

<span id="_Toc477526865" class="anchor"></span>Figure 170: Report Preview — Print Category and Procedure Summary (Report)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/198.png)

The Export option produces the information for the selected criteria in Excel format (Figure 171).

<span id="_Toc477526867" class="anchor"></span>Figure 171: Export — Print Category and Procedure Summary (Report)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/199.png) ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/200.png)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/201.png) ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/202.png)

#### Send No Records DSS Units Report

The Send No Records DSS Units Report provides Management users with a list of active DSS Units with send to PCE status of Send NO RECORDS. Refer to Figure 172 to view the report selection screen.

1.  Select the report.
208. Export, Preview, Print, or Cancel the report.

> **NOTE:** - When printing, the default printer is the device most recently used.

<span id="_Toc477526869" class="anchor"></span>Figure 172: Send No Records DSS Units Report Required Fields

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/203.png)

The report preview output includes DSS Unit Name and IEN, Associated Stop Code \[and Credit Stop and CHAR4 Code if present\] (Figure 173). After previewing the report, the user has the option to export, print or close the report.<span id="_Toc477526871" class="anchor"></span>

Figure 173: Report Preview — Send No Records DSS Units Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/204.png)

The Export option produces the information for the selected criteria in Excel format (Figure 174).

<span id="_Ref94772764" class="anchor"></span>Figure 174: Export — Send No Records DSS Units Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/205.png)

<span id="_Toc477526651" class="anchor"></span>

## Management Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Management Menu is available to users with the ECMGR security key. This option accesses the menus needed for management of the Event Capture software. The main menu in the Management Menu provides the following management functions (Figure 175):

- [Location](#location-update-location-information) — Update Location Information
- [DSS Unit](#dss-units) — Add or Update DSS Units
- [Access by User](#access-by-user-grant-access-to-dss-units-by-user) — Grant Access to DSS Units by User
- [Category](#category-add-or-update-categories) — Add or Update Categories
- [Procedure](#procedure-add-or-update-local-procedures) — Add or Update Local Procedures
- [Reason](#reason-add-or-update-procedure-reasons) — Add or Update Procedure Reasons
- [Event Code Screen](#event-code-screens) — Add, Update or Copy Event Code Screens
- [Inactivate EC Screen](#_Toc67310187) — Identify/Inactivate Multiple Event Code Screens
- [Providers](#_Providers_—_Maintain) — Maintain Non-Licensed Providers

<span id="_Toc477526874" class="anchor"></span>Figure 175: Event Capture Management Main Menu

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/206.png)

### Location — Update Location Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Location option allows Management users to create or remove access to an Event Capture location and flag it as active or inactive for use in the Event Capture software. When creating a location, the selection can be an individual facility or a division if the facility is multidivisional.

Before the User Starts

- Location selected must be in the INSTITUTION file (#4).
- Locations must be created with this option before the user can establish DSS Units. No further options are functional until the user creates an Event Capture location.

What the User Will See

- A list of existing locations displays in a grid format (Figure 176).
- For each location listed, the following information is displayed (if available): Name, State, Facility Type, Station Number, IEN, and whether this location is current.
- The Name column contains the Location Name.
- The Station Number corresponds to the first part (the characters before the dash) of the feeder location when there is no division suffix.
- The IEN column contains the IEN of the INSTITUTION file (#4). The IEN corresponds to the first part (the characters before the dash) of the feeder location when there is a division suffix.
- A search field is available at the top of the screen, allowing the user to search for a specific location.

<span id="_Ref94775933" class="anchor"></span>Figure 176: Management Menu \[Locations\] Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/207.png)

From the Locations screen, the user can select a location by double-clicking on a row or by highlighting a row and then clicking the Update button. After selecting a location, an edit screen appears, allowing the user to either create the location as a current Event Capture location or to remove the selected location (Figure 177).

<span id="_Ref94775980" class="anchor"></span>Figure 177: Edit Location Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/208.png)

The rows within the Locations screen can be sorted by using the Sort menu (Figure 178) or by clicking on the column header. The default sort order will group locations based on whether they are current and lists the current locations group first. In addition, the default sort order lists the locations alphabetically within those groups.

<span id="_Ref94776015" class="anchor"></span>Figure 178: Sort Location Menu Options

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/209.png)

To create a current location, click the checkbox labeled “Create as current Event Capture location” and click the OK button (Figure 179). The location is “flagged” as active for use in the Event Capture software.

<span id="_Ref94776077" class="anchor"></span>Figure 179: Creating a Current Location

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/210.png)

To remove a current location, click the checkbox labeled “Remove as current Event Capture location” and click the OK button (Figure 180). The location is “flagged” as inactive for use in the Event Capture software.

<span id="_Ref94776841" class="anchor"></span>Figure 180: Removing a Current Location

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/211.png)

Click the Export button to export the Locations listing to Excel. The tab in Excel is titled “ECS Location Table Export” (Figure 181).

<span id="_Ref94776874" class="anchor"></span>Figure 181: Export — ECS Location Table

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/212.png)

### DSS Units 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to add, edit, activate or inactivate DSS Units for use with Event Capture. Additionally, DSS Units without workload may be deleted. DSS Units typically represent the smallest identifiable work unit in a clinical service at the medical center and are defined by the VA Medical Centers (VAMCs).

A DSS Unit can represent any of the following:

- An entire service
- A section of a service
- A small section within a section
- A medical equipment item used in patient procedures

Before the User Starts

- Use the Location — Update Location Information option to create an Event Capture location before using this option.
- A prompt displays a notification to enter an Associated Stop Code only if the send “All Records” to PCE is set to NO.
- No further options are functional until DSS Units are created.

What the User Will See

- A list of DSS Units displays in table format.

  The rows within the DSS Units table can be sorted by using the Sort drop-down menu (Figure 182) or by clicking on any column header. The default sort order will arrange DSS Unit Names alphabetically.

<span id="_Ref94777048" class="anchor"></span>Figure 182: Sort DSS Units Menu Items

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/213.png)

- A search field is available at the top of the screen, allowing the user to search for a specific DSS Unit. Options to search by “Active” or “Inactive” status are also available. Type in a partial search string, then click the binoculars button (Search) or hit \<Enter\>, to show entries meeting the search criteria.
- The screen contains the following columns:
- DSS Unit Name
- Unit IEN (becomes the end of the feeder location) — corresponds to the locally created Event Capture DSS Unit Name
- Active — Status for DSS Unit (Yes or No)
- PCE — Reflects if workload is set to pass to PCE. Values include:
- All — Send all records
- OOS — Send Occasion Of Service records
- No — Send no records
- DSS Dept
- Service
- Medical Specialty
- Cost Center

<span id="_Toc190948663" class="anchor"></span>Figure 183: Management Menu \[DSS Units\] Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/214.png)

The Print button enables users to print the report.

The Export button enables users to export the data to an Excel spreadsheet (Figure 184).

Click the Update button to update an existing DSS Unit or click the Add button to add a new one. The Edit a DSS Unit or Add a DSS Unit screen will appear.<span id="_Toc477526885" class="anchor"></span>

Figure 184: Export — DSS Units Table

![Table 2 lists the element name and description for each field that appears on the Add or Edit DSS Unit screen:](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/215.png)

*Table 2 lists the element name and description for each field that appears on the Add or Edit DSS Unit screen:*

<table>
<caption><p><span id="_Ref95140641" class="anchor"></span>Table 3: Acronyms and Abbreviations</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DSS Unit Name</td>
<td>The name of the DSS Unit being created</td>
</tr>
<tr class="even">
<td>DSS Dept. and DSS Unit IEN</td>
<td><p>The value used to identify the DSS Department to which the DSS Unit is associated (1 to 14 characters).</p>
<ul>
<li><p>The same DSS Department can be used for more than one DSS Unit</p></li>
<li><p>The DSS Unit IEN is a unique number assigned by the server, and is not editable in this screen</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Service</td>
<td>The service associated with this DSS Unit — from the SERVICE/SECTION file (#49)</td>
</tr>
<tr class="even">
<td>Medical Specialty</td>
<td>The medical specialty associated with this DSS Unit — from the MEDICAL SPECIALTY file (#723)</td>
</tr>
<tr class="odd">
<td>Cost Center</td>
<td>The cost center associated with this DSS Unit — from the COST CENTER file (#420.1). Cost centers are defined in MP4-Part V, Appendix B of the Fiscal Service cost manuals.</td>
</tr>
<tr class="even">
<td>DSS Unit Status</td>
<td><p>Active — Lists Active Event Code Screens</p>
<p>Inactive — Lists Inactive Event Code Screens</p></td>
</tr>
<tr class="odd">
<td>Event Code Screens</td>
<td><p>Inactivate — When an active DSS Unit is changed to inactive, all Event Code Screens within the DSS Unit are also inactivated.</p>
<p>Reactivate — When an inactive DSS Unit is changed to active, its Event Code Screens can either be reactivated or remain inactive.</p></td>
</tr>
<tr class="even">
<td>Default Date / Time</td>
<td><p>Now — The current date and time will populate during data entry</p>
<p>None — No default date and time will be populated during data entry. The user is required to enter the date and time of the patient procedure.</p></td>
</tr>
<tr class="odd">
<td>Allow Category Use</td>
<td><p>Yes — Use categories to group procedures during data entry</p>
<p>No — Do not use categories to group procedures during data entry</p></td>
</tr>
<tr class="even">
<td>Allow Duplicate Override</td>
<td><p>Yes — Spreadsheet data for this DSS Unit can have duplicates overridden and uploaded</p>
<p>No — Spreadsheet data for this DSS Unit will not allow duplicates to be overridden and uploaded</p></td>
</tr>
<tr class="odd">
<td>Send to PCE</td>
<td><p>Defines the method used to send the user’s data to PCE for the DSS Unit being created.</p>
<p>All Records — Send All Records</p>
<p>No Records — Send No Records</p>
<p>Occasion Of Service — For Occasion Of Service workload that is sent to PCE</p></td>
</tr>
<tr class="even">
<td>Associated Stop Code</td>
<td>This option will only appear when “No Records” or “Occasion Of Service” is selected for Send to PCE. Select the Stop Code associated with this DSS Unit. Be sure to select an active Stop Code.</td>
</tr>
<tr class="odd">
<td>Credit Stop Code</td>
<td>This option will only appear when “No Records” is selected for Send to PCE, and an Associated Stop Code has been selected. Select the Credit Stop Code associated with this DSS Unit.</td>
</tr>
<tr class="even">
<td>CHAR4 Code</td>
<td>This option will only appear when “No Records” is selected for Send to PCE, and an Associated Stop Code has been selected. Select the CHAR4 Code associated with this DSS Unit.</td>
</tr>
</tbody>
</table>

<span id="_Ref95140641" class="anchor"></span>Table 3: Acronyms and Abbreviations

> **NOTE:** - On both Add DSS Unit and Edit DSS Unit screens, the DSS Unit Status defaults to Active, and the Allow Category Use field defaults to No, but the user can select Yes.

- The default value for Allow Duplicate Override is No.
- When the Send to PCE option is set to No Records or Occasion Of Service, the Associated Stop Code field is enabled.
- When the Send to PCE option is set to All Records, the Associated Stop Code field will not be visible. All other default options can be changed.
- The user can search for the Associated Stop Code by either description or code. The Associated Stop Code will display and will include both the description and the code.

#### Delete a DSS Unit

The Edit drop-down menu at the top of the DSS Units window (Figure 185) allows the user to delete an unused DSS Unit. If the user selects Delete the selected DSS Unit from the drop-down menu, the following prompt is displayed: "The selected DSS Unit will be deleted. Continue?". If "Yes" is selected, the system will check for any workload on the DSS Unit and its associated Event Code Screens.

- If there is workload on the selected DSS Unit, then the DSS Unit will not be deleted.
- If there is no workload on the selected DSS Unit, then the DSS Unit and its associated Event Code Screens will be deleted.

<span id="_Ref94777335" class="anchor"></span>Figure 185: Edit DSS Units Menu

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/216.png)

> **NOTE:** - The VA MailMan service will send an automated message to the user listing the DSS Unit that has been deleted. An example of this message can be seen in [Appendix C](#ExampleMessageDeleteDSSUnit).

#### Add a DSS Unit

The Add a DSS Unit function allows the user to create a new DSS Unit within ECS.

1.  Click the Add button.
- The Add a DSS Unit Screen will display (Figure 186).

<span id="_Ref94777409" class="anchor"></span>Figure 186: Add a DSS Unit Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/217.png)

209. Enter a DSS Unit Name.
210. Enter a DSS Dept.
211. Select a Service from the list provided.
212. Select a Medical Specialty from the list provided.
213. Select a Cost Center from the list provided.
214. Select the DSS Unit Status to Active or Inactive.
215. Choose the Default Date / Time.
216. Choose whether to Allow Category Use.
- A site may choose to use Categories to group procedures when entering data. Allowing category use does not mean Categories are required, but merely gives the site the option to use Categories. Setting this flag to "No" will not allow the site to use Categories when creating an Event Code Screen.
217. Choose whether to Allow Duplicate Override.
218. Choose the appropriate Send to PCE option: All Records, No Records, or Occasion Of Service.

Note

- When the Send to PCE option is set to All Records, the Associated Stop Code field will not be visible.
- When the Send to PCE option is set to No Records or Occasion Of Service, the Associated Stop Code field will be visible.
- Credit Stop Code and CHAR4 Code fields will be visible when an Associated Stop Code is selected.
219. When the Send to PCE selection is set to <u>No Records</u>, then (Figure 187):
- An Associated Stop Code is required to be entered for the DSS Unit during setup.
- A Credit Stop Code may be added.
- A CHAR4 Code may be added.
220. When the Send to PCE selection is set to <u>Occasion Of Service</u>, then:
- An Associated Stop Code is required to be entered for the DSS Unit during setup.
221. Assign access to the DSS Unit.
222. Click the OK button when selections are complete.

<span id="_Ref94777456" class="anchor"></span>Figure 187: Add a DSS Unit — Send to PCE with No Records

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/218.png)

#### Update a DSS Unit

The Update DSS Unit option allows the user to edit DSS Units for use with Event Capture.

1.  Select a DSS Unit from the list of DSS Units on the Management Menu \[DSS Unit\] screen.
223. Click the Update button.
- The Edit DSS Unit screen will display for the selected DSS Unit (Figure 188)

<span id="_Ref94777513" class="anchor"></span>Figure 188: Edit DSS Unit Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/219.png)

224. Enter a DSS Unit Name.
225. Enter a DSS Dept.
226. Select a Service from the list provided.
227. Select a Medical Specialty from the list provided.
228. Select a Cost Center from the list provided.
229. Select a DSS Unit Status value of Active or Inactive
- When changing the status of the DSS Unit from Inactive toActive:
- Select the “Active” radio button under DSS Unit Status.
- An *Event Code Screens* group-box is displayed containing radio buttons and a grid. (Figure 189). The radio buttons are labeled “Reactivate” and “Remain Inactive”.
- To reactivate all the associated Event Code Screens, select “Reactivate”.
- To leave all associated Event Code Screens inactive, select “Remain Inactive”.
- Click OK to apply the change and file the record.

> **NOTE:** - If “Reactivate” is not selected, the Event Code Screens will remain inactive.

- When changing the status of the DSS Unit from Active toInactive:
- Select the “Inactive” radio button under the DSS Unit Status.
- Click OK to apply the change and file the record.

> **NOTE:** - When the DSS Unit Status is changed from “Active” to “Inactive”, the associated Event Code Screens are automatically inactivated.

<span id="_Toc477526887" class="anchor"></span>Figure 189: DSS Unit Status Change from Inactive to Active

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/220.png)

230. Choose the Default Date / Time.
231. Choose whether to Allow Category Use.
- If the DSS Unit is not used in any Event Code Screens, the "Allow Category Use" value can be toggled between "Yes" and "No". Once Event Code Screens using the DSS Unit have been defined, the user may change the "Allow Category Use" setting from "Yes" to "No" to disallow the use of Categories; however, if the "Allow Category Use" is set to "No", the radio buttons will be disabled, and the value cannot be changed.
- Allowing Category use does not mean Categories are required, but merely gives the site the option to use Categories. Setting this flag to "No" will not allow the site to use categories when creating an Event Code Screen.
232. Choose whether to Allow Duplicate Override.
233. Choose the appropriate Send to PCE option: All Records or No Records

> **NOTE:** - When updating an established DSS Unit, Send to PCE cannot be set to Occasion Of Service. Occasion Of Service can only be selected on initial DSS Unit setup. In addition, for an established DSS Unit with a Send to PCE set to Occasion Of Service, Send to PCE cannot be modified.

- When the Send to PCE option is set to <u>All Records</u>, the Associated Stop Code field will not be visible.
- When the Send to PCE selection is set to <u>No Records</u>, then (Figure 190):
- An Associated Stop Code must be entered for the DSS Unit during setup.
- A Credit Stop Code may be added.
- A CHAR4 Code may be added.

<span id="_Ref95318677" class="anchor"></span>Figure 190: Update a DSS Unit — Send to PCE with No Records

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/221.png)

234. Click the OK button when selections are complete.

#### To Grant Access to a DSS Unit

From the Add or Update DSS Units screens, the user has the option to give specific users access to the DSS Unit being added or edited.

1.  Click the Access button at the bottom of the Add or Edit DSS Unit screen.
- The Grant Access to DSS Unit Screen opens and has Include and Exclude fields (Figure 191).
235. Type the starting characters of the last name in the upper portion of the Excluded list box, or simply scroll through the list to search for a last name.
- The Excluded list box contains the names of all active VistA users at the site.
236. Grant access to a specific DSS unit by moving a user to the Included list box.
- Highlight a name in the Excluded list box and click the Include button or simply double-click the name in the Excluded list box.
- Access is denied by moving a user to the Excluded list box, either by highlighting a name in the Included list box and clicking the Exclude button, or by simply double-clicking the name in the Included list box.
237. Click the Apply button to save the changes and continue granting access to additional users or click the OK button to save the changes and return to the previous screen.

> **NOTE:** - The IEN and Person Class/Classification for a selected user appear below the associated Excluded or Included list box.

<span id="_Ref94777830" class="anchor"></span>Figure 191: Grant Access to DSS Unit

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/222.png)

#### To Disable Categories for a DSS Unit

1.  Select a DSS Unit which allows categories from the list of DSS Units and click the Update button.
- The Edit DSS Unit screen opens for the selected DSS Unit (Figure 192).

<span id="_Toc477526891" class="anchor"></span>Figure 192: Edit DSS Unit Screen Showing a DSS Unit Set to Allow Categories

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/223.png)

238. In the Allow Category Use section (Figure 193), click the No radio button, then click the OK button.

<span id="_Toc477526893" class="anchor"></span>Figure 193: Allow Category Use Set to No

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/224.png)

- A warning pop up window appears stating that if categories are disabled, this setting cannot be re-instated (Figure 194).
239. Click Yes to confirm.

<span id="_Toc477526895" class="anchor"></span>Figure 194: Disable Category Warning Pop Up Message

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/225.png)

- On the Edit DSS Unit screen, the Event Code Screens section shows “None” listed in the Category column. The Allow Category Use section is now disabled (Figure 195).

<span id="_Toc477526897" class="anchor"></span>Figure 195: Edit DSS Unit Screen After Disabling Categories

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/226.png)

240. Click OK to return to the Management Menu \[DSS Units\] screen.

> **NOTE:** - Once categories are disabled for a DSS Unit, any fields for entering category information for that DSS Unit will be disabled on all Event Capture screens.

- Once categories are disabled for a DSS Unit, any previously entered workload will remain available for viewing and editing.
- A report is available to Management users which lists all DSS Units that do not allow use of categories. (See [Section 4.3.2.2](#disabled-category-and-procedure-summary), Disabled Category and Procedure Summary).
- Event Code Screens without categories will remain available for use.

### Access by User — Grant Access to DSS Units by User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the User Starts

- Use extreme caution when using this option. Removing access to a specified DSS Unit for all users and inactivating the DSS Unit is not recommended without the permission of the associated service.
- Contact each service for a list of its Event Capture users and the DSS Units for which they enter data.
- The user must have access to a given DSS Unit before procedure data can be entered.
- Access can be provided to <u>all</u> DSS Units by assigning the ECALLU security key to a specified user (normally the DSS Manager or designee) using the Allocation of Security Keys option in the Key Management Menu under the Menu Management Menu.

> **NOTE:** - This option cannot be used to remove access to DSS Units for users who hold the ECALLU security key.

What the User Will See

- A list of users available for selection (Figure 196).
- For a selected user, the Available DSS Units and the Selected DSS Units display. Selected DSS Units represent the DSS Units for which the selected user has access

#### Assign User Access to DSS Units

1.  Select a user.

<span id="_Toc477526899" class="anchor"></span>Figure 196: Grant Access to DSS Units by User

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/227.png)

241. Select one or more DSS Unit(s) in the Available list by highlighting the selected unit(s) and clicking on the Include button (Figure 197).
- Press and hold the \<Ctrl\> key to select more than one DSS Unit.
- Move highlighted items to the Selected list by clicking the Include button.
- Similarly, access to DSS Units can be removed for the selected user by highlighting a DSS Unit in the Selected list, then clicking the Exclude button.

<span id="_Ref95128741" class="anchor"></span>Figure 197: Grant Access to DSS Units by User — Adding DSS Units

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/228.png) ![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/229.png)

242. Click the Apply button to apply the changes and continue working or click the OK button to apply the changes and exit the screen.

### Category — Add or Update Categories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows Management users to enter or edit, but <u>not delete</u>, local categories in the EVENT CAPTURE CATEGORY file (#726).

DSS Units can be defined to use categories to group procedures during data entry. Categories are facility-specific; therefore, users can use names that best suit their facility. For example, for a DSS Unit named “Audiology and Speech,” categories could be named “Speech Evaluation” and “Audiology Testing.” It is acceptable to have both DSS Units that do use categories and DSS Units that do not use categories defined at a facility.

Before the User Starts

- The user can ignore this option if the site’s DSS Units are defined for use without categories.
- Categories <u>cannot be deleted</u>, but this option can be used to <u>inactivate</u> or <u>reactivate</u> them.

What the User Will See

- After selecting Category — Add or Update Categories from the Management Menu, the first window displays a list of Category Names, the Date created, and the Inactivation Date (Figure 198).
- The Management Menu \[Categories\] screen provides options to Add or Update a category.

<span id="_Toc477526902" class="anchor"></span>Figure 198: Categories Main Screen on Management Menu

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/230.png)

#### Add Categories

1.  Click the Add button, or use the menu bar, and select Edit \> Add.
- The Add Category screen opens (Figure 199).
- The Status field defaults to “Active.”
243. Enter the name of the category to be added and click the OK button.

<span id="_Ref95129022" class="anchor"></span>Figure 199: Add Category Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/231.png)

#### Update Categories

1.  On the Management Menu \[Categories\] screen, select a category to modify and click Update.
- The Update Category screen displays (Figure 200).
244. Change the category to its new status by clicking Active or Inactive.
245. Click the OK button to file the change and return to the previous screen.
- The Management Menu \[Categories\] screen will reflect the changes made. If the category was inactivated, the Inactivation Date will display the current date.

<span id="_Ref105139145" class="anchor"></span>Figure 200: Update Category Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/232.png)

The Export button enables users to export the data to an Excel spreadsheet (Figure 201).<span id="_Toc422742875" class="anchor"></span>

Figure 201: Export — ECS Category Table

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/233.png)

### Procedure — Add or Update Local Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Procedure option allows the user to enter or edit, but <u>not delete</u> local procedures in the EC National Procedure file (#725).

Before the User Starts

- Before using this option, print the National/Local Procedure Report from the Reports menu of the Event Capture Main Menu to print a list of procedures with their associated CPT codes. This report can be lengthy if it includes national procedures. This should be queued to print to a device during non-peak hours.
- Enter an associated CPT code to pass local procedures to the PCE software.
- A local procedure code number is required for any new local procedure.
- The local number code must be five characters in length, starting with an uppercase alpha character, followed by four alphabetic or numeric characters. This number will be used as the national code number for the new local procedure.
- With functionality put in place by the Code Set Versioning project, only active CPT codes are made available, and are based on the date a local procedure is added.

What the User Will See

- After selecting Procedure — Add or Update Local Procedures from the Management Menu, the first screen displays a list consisting of Procedure Name, Number, CPT Code and Description, and Active status (Figure 202).
- The Procedure screen allows the user to select and display only Active or Inactive procedures via check-boxes on the upper left side of the screen.
- The Procedures screen allows the user to Add or Update a procedure via buttons on the lower right side of the screen.

<span id="_Ref95129282" class="anchor"></span>Figure 202: Management Menu \[Procedures\] Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/234.png)

#### Add Procedures

1.  Click the Add button, or use the menu bar, and select Edit \> Add.
- The Add Local Procedure screen opens (Figure 203).

<span id="_Ref95129349" class="anchor"></span>Figure 203: Add Local Procedure

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/235.png)

246. Enter the new local Procedure Name.
247. Enter the local Procedure Number.
248. Enter the CPT Code if the data will transmit to the PCE software.
- The CPT Code and Description field contains CPT Code look-up functionality. The user can search for an existing CPT Code by code, a portion of the code, or a part of the description.
249. Select the Status (Active or Inactive).
- The Status field defaults to “Active.”
250. Click the OK button. The new local procedure has been added.
- When attempting to file a new Local Procedure, the system compares the new procedure to the National Procedure code file to prevent duplication. If there is a conflict, a message is displayed, and the local procedure is not added.

#### Update Procedures

1.  Highlight the existing record and click the Update button or double-click the row.
- The Edit Local Procedure screen opens (Figure 204).

<span id="_Ref95129423" class="anchor"></span>Figure 204: Edit Local Procedure

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/236.png)

251. Edit the Procedure Name, Procedure Number, CPT Code and Description, and/or Status.
- Local procedures cannot be deleted, but the Status can be used to inactivate or reactivate them.
- The CPT code for a local procedure can be deleted by deleting the value in the CPT Code and Description field, then clicking the OK button.
252. Click the OK button.
- The updated local procedure appears on the Procedures screen. The highlighted row in Figure 205 shows the updated Procedure Name.<span id="_Toc477526912" class="anchor"></span>

Figure 205: Update After Editing a Local Procedure

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/237.png)

The Procedures listing can be exported to Excel. The tab in Excel is titled “ECS Procedure Table Export” (Figure 206).

<span id="_Ref95129524" class="anchor"></span>Figure 206: Export — Procedures

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/238.png)

### Reason — Add or Update Procedure Reasons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reasons are site-defined descriptions explaining why a procedure was performed for a patient.

Before the User Starts

- Users with the ECMGR security key can activate or inactivate existing reasons.
- If a reason is listed as inactive, it will not appear on the dropdown list for reasons on any screen.
- Event Capture managers can add a new reason using the Event Capture — New Reason screen.
- New reasons will immediately be available for use in data entry.

What the User Will See

- After selecting Reason — Add or Update Procedure Reasons from the Management Menu, the first screen displays a list of Active Reasons and Inactive Reasons (Figure 207).

<span id="_Ref105139484" class="anchor"></span>Figure 207: Management Menu \[Reasons\] Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/239.png)

#### Activate Reasons

1.  Highlight one or more items from the Inactive Reasons list box and click the Activate button.
- To move more than one reason, press and hold the \<Ctrl\> key and then highlight additional items (Figure 208).

<span id="_Ref95129643" class="anchor"></span>Figure 208: Reasons Screen with Inactive Reasons Selected

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/240.png)

The Inactive Reason(s) selected will appear in the Active Reasons column when the Activate button is clicked (Figure 209).

<span id="_Ref95129697" class="anchor"></span>Figure 209: Reasons Screen with Inactive Reasons Moved to the Active Column

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/241.png)

Click the Apply button to apply the changes and continue working or click the OK button to apply the changes and exit the screen. A confirmation prompt will appear. Click the Yes button to save the changes (Figure 210).

<span id="_Ref95129755" class="anchor"></span>Figure 210: Confirmation Prompt

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/242.png)

#### Inactivate Reasons

1.  Highlight item(s) from the Active Reasons list box and click the Inactivate button.
- To move more than one reason, click and hold the \<Ctrl\> key and then highlight additional items (Figure 211).

<span id="_Toc477526920" class="anchor"></span>Figure 211: Reasons Screen with Active Reasons Highlighted

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/243.png)

The Active Reason(s) selected will appear in the Inactive Reasons column when the Inactivate button is clicked (Figure 212).

<span id="_Ref95129853" class="anchor"></span>Figure 212: Reasons Screen with Active Reasons Moved to the Inactive Column

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/244.png)

Click the Apply button to apply the changes and continue working or click the OK button to apply the changes and exit the screen. A confirmation prompt will appear (Figure 213). Click the Yes button to save the changes.

<span id="_Ref105140123" class="anchor"></span>Figure 213: Confirmation Prompt

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/245.png)

#### Add a New Reason

1.  Click the Add button.
- The Event Capture — New Reason screen will appear (Figure 214).

<span id="_Ref95129950" class="anchor"></span>Figure 214: New Reason Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/246.png)

253. Type the name of the new reason, then click the OK button to add the reason to the Active Reasons column. Click the Cancel button to exit the screen without saving the record.
- Once the new reason is added, it will appear on the Reasons screen (Figure 215).

<span id="_Ref95129995" class="anchor"></span>Figure 215: Reasons Screen with New Reason Added

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/247.png)

### Event Code Screens 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to add, edit, or copy Event Code Screens for use with Event Capture. Additionally, Event Code Screens without workload may be deleted.

The Event Code Screen option allows the user to create Event Code Screens for one or all Event Capture locations. Event Code Screens define procedure information. During data entry users can select only the procedures defined in the Event Code Screens. For each screen, you are prompted to enter the following information:

- DSS Unit
- Category (If DSS Units are defined to group procedures by categories)
- Procedure

Before the User Starts

- Use the Location — Update Location Information option to create an Event Capture location before using this option.
- Use the DSS Unit — Add or Update DSS Units option to establish DSS Units before using this option.
- Event Code Screens must be defined before entering any Event Capture data.
- A prompt for Category occurs only if the Event Code Screen uses categories to group procedures.
- The user must define an active Associated Clinic and CPT code to pass Event Code procedures to PCE.
- With functionality put in place by the Code Set Versioning project, only active CPT codes can be selected, and they will be based on the date the Event Code Screen is being set up.
- The Event Code Screen enables the use of characters “/” and “-” in the search field.
- The Associated Clinic on the Event Code Screen is not auto-populated.
- The Print and Export buttons are available on the Event Code Screen.
- Users with the ECMGR key will be able to copy EC screens to another DSS Unit.

What the User Will See

- After selecting Event Code Screen — Add or Update Event Code Screens from the Management Menu, the first screen displays a drop-down box of DSS Units.
- Select a DSS Unit to display the Event Code Screen data. Options to search by “Active” or “Inactive” status are also available. Columns include Synonym, Procedure, Location, Default Associated Clinic, Category and Status (Figure 216).

<span id="_Ref95130058" class="anchor"></span>Figure 216: Event Code Screens Example

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/248.png)

- Click the Print button to print the Event Code Screens listing. When printing the report, the user will be prompted to choose Active, Inactive or All for the Clinic Status (Figure 217).

<span id="_Ref95130116" class="anchor"></span>Figure 217: Select Clinic Status for the Event Code Screens Listing

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/249.png)

- The Event Code Screens information can also be exported to Excel. The user will be prompted to choose Active, Inactive or All for the Clinic Status. The tab in Excel is titled “Event Code Table Export” (Figure 218).

<span id="_Ref95130162" class="anchor"></span>Figure 218: Exported Event Code Table Report

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/250.png)

#### Delete Event Code Screens

The Edit drop-down menu at the top of the Event Code Screens window (Figure 219) allows the user to delete an unused Event Code Screen. If the user selects Delete the selected Event Code Screen from the drop-down menu, the following prompt is displayed: "The selected Event Code Screen will be deleted. Continue?". If "Yes" is selected, the system will check for any workload on the Event Code Screen.

- If there is workload on the selected Event Code Screen, then the Event Code Screen will not be deleted.
- If there is no workload on the selected Event Code Screen, then the Event Code Screen will be deleted.

<span id="_Ref95130226" class="anchor"></span>Figure 219: Management Menu \[Event Code Screens\]

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/251.png)

> **NOTE:** - The VA MailMan service will send an automated message to the user listing the Event Code Screens that have been deleted. An example of this message can be seen in [Appendix C](#ExampleMessageDeleteEventCodeScreen).

#### Add Event Code Screens

1.  Select a DSS Unit from the dropdown list (Figure 220).
254. Click the Add button or use the menu bar and select Edit \> Add.
- The Add Event Code Screen will open (Figure 221).

<span id="_Ref128128546" class="anchor"></span>Figure 220 Management Menu \[Event Code Screens\] Select DSS Unit

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/252.png)

<span id="_Ref95130295" class="anchor"></span>Figure 221: Add Event Code Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/253.png)

255. Make selections in the corresponding fields: Category (if enabled), Location (one/multiple/all), Procedure, Status (active/inactive), Procedure Synonym, Default Volume, Ask Reasons and Default Associated Clinic.

Note

- A clinic must exist in file \#728.44 Clinics and Stop Codes prior to being available for selection in any Data Entry options.
- If an Associated Clinic has non-conforming stop codes, the clinic will not be selectable.
256. Click the Add button to file the record and add another procedure, if desired (Figure 221). Select a procedure from the Procedure dropdown list. Repeat.
257. Click the OK button to file the record and return to the Event Code Screen list.
- The Add Event Code Screen closes, and the newly added Event Code Screen(s) are displayed in the list (Figure 222).

<span id="_Ref95130385" class="anchor"></span>Figure 222: Event Code Screen Added

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/254.png)

> **NOTE:** - If the user selects an inactive Associated Clinic and then clicks OK, an error message appears (Figure 223). Click OK on the error message to close it and return to the Add Event Code Screen. From there, the user can select an active Associated Clinic.

<span id="_Ref95138821" class="anchor"></span>Figure 223: Add Event Code Screen — Record Not Filed Error

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/255.png)

#### Update Event Code Screens

1.  Select a DSS Unit from the dropdown list.
258. Highlight a procedure, then click the Update button or use the menu bar and select  
     Edit \> Update.
- The Update Event Code (EC) Screen form opens and displays the following fields: DSS Unit, Category, Location, Procedure, Status, Procedure Synonym, Default Volume, Ask Reasons, and Default Associated Clinic (Figure 224).

<span id="_Ref95138867" class="anchor"></span>Figure 224: Update Event Code Screen Example

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/256.png)

> **NOTE:** - If the user attempts to update an Event Code Screen that has an inactive Associated Clinic, an error message appears (Figure 225). The user has the option to select an appropriate active clinic or to leave the Associated Clinic blank.

<span id="_Ref95138927" class="anchor"></span>Figure 225: Update EC Screen Error — Invalid Associated Clinic

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/257.png)

259. On the Update Event Code Screen, update the Procedure Synonym, Default Volume, Status, Ask Reason and/or Default Associated Clinic field values as desired (Figure 226).
- The Default Associated Clinic list box displays only active locations in the HOSPITAL LOCATION file (#44) whose type is “C” (clinic) and is a “count” clinic.

Note

- A clinic must exist in file \#728.44 Clinics and Stop Codes prior to being available for selection in any Data Entry options.
- If an Associated Clinic has non-conforming stop codes, the clinic will not be selectable.

<span id="_Ref95138986" class="anchor"></span>Figure 226: Update Event Code Screen — Select Default Associated Clinic

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/258.png)

260. Click the OK button.
- The changes for the Event Code Screen record are filed. The Update Event Code Screen closes, and the updated Event Code Screen is displayed in the list.

#### Copy All Event Code Screens to Another DSS Unit

1.  Highlight an Event Code Screen that has an Active status (Figure 227).

<span id="_Ref95139050" class="anchor"></span>Figure 227: Event Code Screen with Active Status Selected

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/259.png)

261. From the menu bar, select Edit \> Copy all EC Screens to another DSS Unit (Figure 228).

<span id="_Ref95139117" class="anchor"></span>Figure 228: Edit \> Copy all EC Screens to another DSS Unit

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/260.png)

- The Select a target screen appears (Figure 229).

<span id="_Ref95139184" class="anchor"></span>Figure 229: Select a Target Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/261.png)

262. Select a target DSS Unit (usually newly created) from the dropdown list, and then click the OK button.

> **NOTE:** - The target DSS Unit is usually newly created by the user, but an existing DSS Unit may also be used.

- The Copy Event Code Screen to \[user-selected target DSS Unit\] window will open. See Figure 230 for an example.

<span id="_Ref95139263" class="anchor"></span>Figure 230: Copy Event Code Screen to DSS Unit

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/262.png)

- The Location, Status, Procedure Synonym, Default Volume, Ask Reasons and Default Associated Clinic fields can be modified on this screen.
- The DSS Unit and Procedure cannot be edited.

> **NOTE:** - If the DSS Unit is set up to not send records to PCE, the Default Associated Clinic is disabled.

263. Review the field selections and make edits (if necessary).
264. Click the OK button to save the changes and create the copy.
- The next Event Code (EC) Screen window will appear.
- To skip an Event Code Screen, click the Skipthis EC Screen button. The next Event Code Screen window will appear.
265. When all needed Event Code Screens are copied, select the Close button to return to the Event Code Screen.
- All the previous changes will be saved.
- One, many or all Event Code Screens can be copied.

> **NOTE:** - If the user does not select a Location when copying an Event Code Screen, the record will not be filed, and two error messages will appear (Figure 231).

- Click the OK button on each error dialog to return to the Copy Event Code Screens form and enter a Location.

<span id="_Ref95139376" class="anchor"></span>Figure 231: Record Not Filed Error Message for Key Data Missing

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/263.png)

#### Copy the Selected Event Code Screen to Other DSS Unit(s)

1.  Highlight an Event Code Screen that has an Active status (Figure 232).

<span id="_Ref95139443" class="anchor"></span>Figure 232: Event Code Screen with Active Status Selected

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/264.png)

266. From the menu bar, select Edit \> Copy the selected EC Screen to other DSS Unit(s) (Figure 233).

<span id="_Ref95321147" class="anchor"></span>Figure 233: Edit \> Copy the selected EC Screens to other DSS Unit(s)

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/265.png)

- The *Select one or more targets* screen appears (Figure 234).

<span id="_Ref95139548" class="anchor"></span>Figure 234: Select One or More Target DSS Units

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/266.png)

267. Select one or more target DSS Units from the list, and then click the OK button.

> **NOTE:** - The target DSS Unit is usually newly created by the user, but an existing DSS Unit may also be used.

- Multiple DSS Units may be selected by holding down the \<Ctrl\> key while mouse clicking on the desired DSS Units.

  The *Copy Event Code Screen to \[user-selected target DSS Unit\]* windows open (Figure 235) one at a time for each target DSS Unit selected in step 2, Figure 234. Follow steps 4 and 5 for each selection.

<span id="_Ref95139645" class="anchor"></span>Figure 235: Copy Event Code Screen to DSS Unit

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/267.png)

268. Review the field selections and make edits (if necessary).
- The Location, Status, Procedure Synonym, Default Volume, Ask Reasons and Default Associated Clinic fields can be modified on this screen.
- The DSS Unit and Procedure cannot be edited.
- If the DSS Unit is setup to not send records to PCE, the Default Associated Clinic is disabled.
269. Click the OK, Add, or Skip this EC Screen button:
- Click OK to save the changes and open the next *Copy Event Code Screen to \[user-selected target DSS Unit\]* window (Figure 235).
- Click Add to save the changes. To proceed to the next *Copy Event Code Screen to \[user-selected target DSS Unit\]* window, click the Skip this EC Screen button.
- Click Skipthis EC Screen to bypass copying the Event Code Screen for the selected DSS Unit and to open the next selection.
- When the Event Code Screen is copied to all selected DSS Units, the last window will close. All changes will be saved.

> **NOTE:** - If a Location is not selected when copying an Event Code Screen, the record will not be filed, and a message dialog will be displayed (Figure 236). Click the OK button on the message dialog to return to the Copy Event Code Screen form to enter a Location.

<span id="_Ref110336060" class="anchor"></span>Figure 236: Required Data Missing

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/268.png)

<span id="_Toc67310187" class="anchor"></span>

### Inactivate EC Screen — Identify Inactive Multiple Event Code Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inactivate EC Screen option allows the user to identify active Event Code (EC) Screens that use a selected EC product code.

Before the User Starts

- Users with the ECMGR security key can select an EC Product Code (CPT Code, National EC Procedure Code or Local EC Procedure Code) and then display all the DSS Units using the selected Product Code on the Inactivate Selected Event Code (EC) Screens for Given Procedure Code form.
- Choose to inactivate Event Code Screens by using the checkboxes in front of each entry.
- The user can display and print a list of Event Code Screens inactivated for a chosen EC Product Code.

What the User Will See

- After clicking the Inactivate EC Screen button on the Management Menu, the Event Capture — Inactivate Selected Event Code (EC) Screens for Given Procedure Code form will be displayed (Figure 237).

<span id="_Ref95139828" class="anchor"></span>Figure 237: Inactivate Selected Event Code (EC) Screens for Given Procedure Code

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/269.png)

#### Inactivate Event Code Screen(s)

1.  Enter an Event Capture Product Code (CPT Code, National EC Procedure Code, or Local EC Procedure Code) in the search field and click the Search button.
- All currently active Event Capture Product Codes are available for selection.
- The associated DSS Units with IENs, Locations and Categories appear for the EC Product Code selected (Figure 238).

<span id="_Ref95139896" class="anchor"></span>Figure 238: Inactivate Selected Event Code (EC) Screens with CPT Code Selected

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/270.png)

270. Use the checkboxes on the left side of the screen to select entries to be inactivated.
- The user can select multiple checkboxes (Figure 238).
271. Click the Apply button to apply the changes and continue working or click the OK button to apply the changes and exit the screen.
- A confirmation prompt will appear. Click the Yes button to continue inactivating the selections. Click No to return to the previous screen (Figure 239).

<span id="_Ref95139954" class="anchor"></span>Figure 239: Confirmation Prompt

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/271.png)

- When the user clicks Apply, a list of inactivated Event Code Screens is displayed (Figure 240).
- Click the Print button to print the list of inactivated EC screens.

<span id="_Ref95140017" class="anchor"></span>Figure 240: List of EC Screens That Were Inactivated

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/272.png)

272. Click the OK button.
- The changes are applied, and the user is returned to the Management Menu.
273. To verify that the Event Code Screens are inactivated, use the Inactivate Event Code Screens option, and reenter the Event Capture Product Code that was previously used.
- The list of DSS Units, Locations and Categories does not include the inactivated Event Code Screens.

<span id="_Providers_—_Maintain" class="anchor"></span>

### Providers — Maintain Non-Licensed Providers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the Package Manager user to create a list of Non-Licensed Providers (i.e., staff without a Person Class). Workload for non-licensed providers can be entered for DSS Units that do not send records to PCE.

Before the User Starts

- For DSS Units that <u>do not</u> send to PCE, both Non-Licensed Providers (without a Person Class) and Providers (with a Person Class) may be selected as providers when entering workload.
- For DSS Units that send records to PCE (including Occasion Of Service DSS Units), staff without a Person Class may not be selected as a provider.

What the User Will See

- After clicking the Providers button on the Management Menu, the Non-Licensed Provider Maintenance screen will be displayed (Figure 241).

<span id="_Ref95140093" class="anchor"></span>Figure 241: Non-Licensed Provider Maintenance Screen

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/273.png)

#### Add a Non-Licensed Provider

1.  Highlight a staff member name in the Excluded list box, then click the Include button (Figure 242).
274. Click OK to accept the changes.

<span id="_Ref105140241" class="anchor"></span>Figure 242: Adding a Non-Licensed Provider

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/274.png)

- Once a staff member has been added to the Included list as a non-licensed provider for any DSS Unit that does not send to PCE, this staff member will be selectable as a provider when entering workload (Figure 243).

<span id="_Ref95140211" class="anchor"></span>Figure 243: Non-Licensed Provider Selection for DSS Units that Do Not Send to PCE

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/275.png)

#### Remove a Non-Licensed Provider

1.  Highlight a staff member name in the Included list box, then click the Exclude button (Figure 244).
275. Click OK to accept the changes.

<span id="_Ref95140370" class="anchor"></span>Figure 244: Removing a Non-Licensed Provider

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/276.png)

- Once a staff member has been added to the Excluded list and removed as a non-licensed provider, the staff member will no longer be selectable as a provider when entering workload for DSS Units that do not send to PCE.

<span id="_Troubleshooting" class="anchor"></span>

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections present some typical problems experienced by end users and the corresponding resolutions.

## Access Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users need an Access Code and Verify Code obtained from their local OIT staff to use the Event Capture GUI.

## Log-On Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Event Capture is usually accessed through a desktop shortcut which points to the installation location. Ask the local support staff for assistance.

If Event Capture launches and then disappears or is not responding, make sure the IP address listed is correct and not blocked by firewall software for the system with which it is communicating. Local support staff is available to assist with issues.

## GUI Appears Distorted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the ECS GUI display appears to be missing scrollbars, columns, or rows, ensure that the screen resolution is set to a resolution of 1440 x 900, or greater. Settings available will be dependent upon the user’s monitor size.

### Example of Setting the Screen Resolution to 1920 x1080

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Right-click anywhere on the computer’s desktop to open the Desktop Context Menu (Figure 245).
2.  Select Display settings from the menu to open the window shown in Figure 246.

<span id="_Ref95140443" class="anchor"></span>Figure 245: Desktop Context Menu — Display Settings

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/277.png)

<span id="_Toc71276257" class="anchor"></span>Figure 246: Windows Display Resolution Settings

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/278.png)

276. Scroll down to view Scale and Layout settings.
277. Select 1920 x 1080 from the Display Resolution dropdown menu.

> **NOTE:** - Depending on the user's version of Windows, this may look different.

#### Acronyms and Abbreviations

Table 3 lists the acronyms and abbreviations used throughout the ECS User Guide.

| Acronym    | Description                                                     |
|------------|-----------------------------------------------------------------|
| 2FA        | Two-Factor Authentication                                       |
| AC         | Application Coordinator                                         |
| ADPAC      | Automated Data Processing Application Coordinator               |
| CCOW       | Clinical Context Object Workgroup                               |
| CHAR4      | A 4-character code                                              |
| CM         | Clinical Modification                                           |
| CPRS       | Computerized Patient Record System                              |
| CPT        | Current Procedural Terminology                                  |
| DSS        | Decision Support System                                         |
| Dx         | Diagnosis                                                       |
| EC         | Event Capture, also Event Code                                  |
| ECACCESS   | Security Key — Event Capture Access                             |
| ECALLU     | Security Key — Event Capture All DSS Units                      |
| ECMGR      | Security Key — Event Capture Manager                            |
| ECNORPT    | Security Key — Event Capture No Reports                         |
| ECPATIENT  | Event Capture Patient                                           |
| ECPROVIDER | Event Capture Provider                                          |
| ECS        | Event Capture System                                            |
| ECSPSH     | Security Key — Event Capture Spreadsheet                        |
| FY         | Fiscal Year                                                     |
| GUI        | Graphical User Interface                                        |
| ICD        | International Classification of Diseases                        |
| ID         | Identification                                                  |
| IEN        | Internal Entry Number                                           |
| IPC        | Inactive Person Class                                           |
| MAS        | Medical Administration Service                                  |
| MCA        | Managerial Cost Accounting                                      |
| MCAO       | Managerial Cost Accounting Office                               |
| NPCD       | National Patient Care Database                                  |
| OIT        | Office of Information and Technology                            |
| PCE        | Patient Care Encounter                                          |
| PIMS       | Patient Information Management System                           |
| PIV        | Personal Identification Verification                            |
| SC         | Service Connected                                               |
| SSN        | Social Security Number                                          |
| SSO        | Single Sign-on                                                  |
| T&TC       | Section 508 Accessibility Testing and Training Center           |
| VA         | Veterans Affairs                                                |
| VAMC       | Veterans Affairs Medical Center                                 |
| VDL        | VA Software Document Library                                    |
| VHA        | Veterans Health Administration                                  |
| VistA      | Veterans Health Information Systems and Technology Architecture |

<span id="_Ref110336100" class="anchor"></span>Table 4: Glossary of Terms

#### Glossary

Table 4 lists some of the terms used throughout the ECS FY24 User Guide.
<table>
<caption>Glossary terms.</caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Associated Clinic</td>
<td>The Associated Clinic of the Event Capture (EC) Procedure. CLINIC IEN is retrieved from the ASSOCIATED CLINIC field (#26) of the EVENT CAPTURE PATIENT file (#721).</td>
</tr>
<tr class="even">
<td>Associated Stop Code</td>
<td>The Stop Code that most closely represents the DSS Unit workload.</td>
</tr>
<tr class="odd">
<td>Category</td>
<td>Category provides Event Capture a common level to group associated procedures. Multiple procedures can be defined for each category.</td>
</tr>
<tr class="even">
<td>CCOW</td>
<td>In the context of health informatics, CCOW is a Health Level 7 international standard protocol designed to enable disparate applications to synchronize in real time, and at the user interface level.</td>
</tr>
<tr class="odd">
<td>CHAR4 Code</td>
<td>A 4-character code value of the associated clinic as specified from the DSS Clinics and Stop Code Worksheet File.</td>
</tr>
<tr class="even">
<td>Combat Veteran</td>
<td>Identifies if patient served in a combat zone. Veteran must have served in active duty in a theatre of combat operations during a period of war after the Persian Gulf War or in combat against a hostile force during a period of hostilities after November 11, 1998.</td>
</tr>
<tr class="odd">
<td>Computerized Patient Record System (CPRS)</td>
<td>Parameters are set up/maintained by the facility’s CPRS Coordinator/Clinical Application Coordinator (CAC).</td>
</tr>
<tr class="even">
<td>Cost Center</td>
<td>Cost Center reveals which service is using this DSS Unit.</td>
</tr>
<tr class="odd">
<td>Credit Stop Code</td>
<td><p>The Credit Stop Code (from the HOSPITAL LOCATION file [#44]) as determined by Medical Administration Service (MAS). This is a DSS Identifier assigned to a clinic and may be utilized in several ways. We can use it to identify different provider types (NP, PA, Psychologist, etc.) and for various program groups (Care Coordination, Telemedicine, etc.), or to give additional credit to a second service in a joint clinic.</p>
<p>DSS further uses credit stop codes to create unique feeder keys to identify clinic intermediate products. Examples are: 123 — Nutrition Individual, 124 — Nutrition Group, 372 — MOVE! Individual, 373 — MOVE! Group.</p></td>
</tr>
<tr class="even">
<td>Current Procedural Terminology (CPT) code</td>
<td>CPT codes are published by the American Medical Association. The purpose of the coding system is to provide uniform language that accurately describes medical, surgical, and diagnostic services.</td>
</tr>
<tr class="odd">
<td>Current Procedural Terminology (CPT) Modifier</td>
<td>CPT modifiers provide the ability to refine CPT procedure codes to better reflect procedures performed.</td>
</tr>
<tr class="even">
<td>DSS Unit</td>
<td>A DSS (Decision Support System) Unit defines the lowest level segment used for tracking hospital resources. These units can be a small work unit within a service or a large division within a service. Management at each facility is responsible for tailoring the DSS Units to fit its resource/cost reporting.</td>
</tr>
<tr class="odd">
<td>DSS Unit Number</td>
<td>This code is used for additional identification of DSS Units.</td>
</tr>
<tr class="even">
<td>Event Capture</td>
<td>Software designed to provide management tools necessary in tracking procedures not entered in other VistA packages.</td>
</tr>
<tr class="odd">
<td>Event Code Screen</td>
<td>Event Code Screens are unique combinations of location, DSS Unit, category, and procedure that define patient procedures.</td>
</tr>
<tr class="even">
<td>Graphical User Interface (GUI)</td>
<td>A type of display format that enables users to choose commands, initiate programs, and other options by selecting pictorial representations (icons) via a mouse or a keyboard.</td>
</tr>
<tr class="odd">
<td>ICD-10-CM</td>
<td>International Classification of Diseases, Tenth Revision, Clinical Modification codes (based on the World Health Organization codes).</td>
</tr>
<tr class="even">
<td>Internal Entry Number (IEN)</td>
<td>The number used to identify an entry within a file. Every record has a unique internal entry number.</td>
</tr>
<tr class="odd">
<td>Ionizing Radiation (ION RAD)</td>
<td>Exposure to ionizing radiation.</td>
</tr>
<tr class="even">
<td>Location</td>
<td>Initializing the user site as a location, the Event Capture software recognizes the user facility as a valid location to enter Event Capture data.</td>
</tr>
<tr class="odd">
<td>Medical Administration Service (MAS)</td>
<td>Now Patient Information Management System (PIMS).</td>
</tr>
<tr class="even">
<td>Ordering Section</td>
<td>The medical section ordering the patient’s procedure.</td>
</tr>
<tr class="odd">
<td>Patient Care Encounter (PCE)</td>
<td><p>The VistA Outpatient Encounters System. PCE builds a single encounter for each recorded instance of a patient receiving services within a clinic. PCE is the mechanism for the transmission of all encounter data to the National Patient Care Database (NPCD).</p>
<p>For outpatient encounters, DSS combines all instances with the same SSN, Date, and Primary Stop code into one outpatient encounter. However, on DSS, each of the clinic encounters of PCE appears as a resource utilization unit under the one encounter. This means that in DSS, a single outpatient encounter will be built by two or more records when they have a common encounter number.</p>
<p>The PCE column reflects if workload is set to pass to PCE. Values include:</p>
<p>All — Send all records</p>
<p>OOS — Send Occasion Of Service records</p>
<p>No — Send no records.</p></td>
</tr>
<tr class="even">
<td>Patient Information Management System (PIMS)</td>
<td>The Scheduling module of the PIMS Package provides for efficient and accurate collection, maintenance and output of data that allows VA Medical Centers to provide timely and quality care to its patients.</td>
</tr>
<tr class="odd">
<td>Procedure</td>
<td>A specific function performed on, or service provided to, a patient. Multiple procedures can be associated with a single category.</td>
</tr>
<tr class="even">
<td>Procedure Reason</td>
<td>A method of generically grouping patient procedures to further describe the event, often giving patient or provider information.</td>
</tr>
<tr class="odd">
<td>Procedure Synonym</td>
<td>See Synonym</td>
</tr>
<tr class="even">
<td>Provider</td>
<td>The provider of care performing the procedure. This provider can be a doctor, nurse, technician, or any designated team of medical professionals.</td>
</tr>
<tr class="odd">
<td>Reason</td>
<td>See Procedure Reason</td>
</tr>
<tr class="even">
<td>Security Key</td>
<td>Security Keys set a layer of protection on the range of computing capabilities available with a particular software application. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="odd">
<td>Service Connection</td>
<td>The service connection (SC) box on the Enter/Edit Patient Data screen in ECS must be answered if it displays as a required option for that patient. Adjudicated service connection means that the facts, shown by evidence, establish that a particular injury or disease resulting in disability was incurred coincident with service in the Armed Forces, or if preexisting such service, was aggravated therein.</td>
</tr>
<tr class="even">
<td>Southwest Asia Conditions</td>
<td>Patient encounter is related to exposure to Southwest Asia conditions while serving in the Southwest Asia Theater of operations.</td>
</tr>
<tr class="odd">
<td>Station Number</td>
<td>A Station Number uniquely identifies every VA primary facility and division; however, entries for some facility types do not have Station Numbers. Station Numbers are stored in Field #99 in the VistA M Server INSTITUTION file (#4).</td>
</tr>
<tr class="even">
<td>Stop Code</td>
<td>A three-digit number that is used in VHA to identify the services that a patient receives at a Department of Veterans Affairs (VA) medical facility. Stop codes are also used to capture workload statistics. A stop code could either be classified as a primary or secondary stop code, (which is referenced as credit stop code). The Stop Code (from the HOSPITAL LOCATION file [#44]) as determined by Medical Administration Service (MAS).</td>
</tr>
<tr class="odd">
<td>Synonym</td>
<td>A locally recognized name or description for a procedure. In VistA, this is a field in the OPTION file (#19). Options may be selected by their menu text or synonym.</td>
</tr>
<tr class="even">
<td>T&amp;TC</td>
<td>Section 508 Accessibility Testing and Training Center.</td>
</tr>
<tr class="odd">
<td>Unit IEN</td>
<td>The internal entry number (IEN) for this record. The number to identify this DSS unit locally at the user’s site (1 to 14 characters). The same DSS Unit number can be used for more than one DSS Unit.</td>
</tr>
<tr class="even">
<td>Verify Code</td>
<td>A secret password used along with the Access Code to provide secure user access to the VistA M Server. It is used by Kernel's Sign-on/Security system along with the Access code to validate the user's identity.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture (VistA) is the proprietary software developed for and used by the VA VHA to support its clinical and administrative functions at VA sites nationwide. It is both client- and server-based software. The client-based software is written in Java, Borland Delphi Pascal, and other GUI-based languages and runs on the Microsoft operating system. The server-based software is written in the M programming language and, via Kernel, runs on all major M implementations regardless of the vendor. It is composed of integrated clinical, infrastructure, and financial/administrative software applications. This internally developed portfolio of applications is recognized as the most comprehensive integrated health information system in the United States.</td>
</tr>
<tr class="even">
<td>Volume</td>
<td>Volume is usually associated with the number of procedures performed. This field can also be used to track number of bed days, or to track time increments spent performing the procedure. For example, if “15-minute increment” is the unit, volume of 1 = 15 minutes, volume of 2 = 30 minutes, etc.</td>
</tr>
</tbody>
</table>
Glossary terms.

#### ECS Package Administrative Messages

Set up an ECS mail group in VistA to receive relevant ECS notifications. Contact IT to set up a VistA ECS Mail Group so more than one person receives ECS administrative messages.

Examples of ECS package administrative email messages included in this section:

- [When a new ECS patch is released](#ExampleMessageECSPatchRelease)
- [When a patch updating the National Procedure Codes is released](\l)
- [When Event Code Screens are inactivated due to changes in National Procedure Codes](\l)
- [When terminated users result in access to DSS Units being affected](#ExampleMessageExample1UserTerminated)
- [When a DSS Unit with no workload is deleted](#ExampleMessageDeleteDSSUnit)
- [When an Event Code Screen with no workload is deleted](#ExampleMessageDeleteEventCodeScreen)

<span id="ExampleMessageECSPatchRelease" class="anchor"></span>When a new ECS patch is released

Figure 247 is a screen capture of an example of the email message a user could receive when an ECS patch is released.

<span id="_Ref95141675" class="anchor"></span>Figure 247: Example Email Message when an ECS Patch is Released

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/279.png)

When a patch updating the National Procedure Codes is released

Figure 248 is an example of the email message a user could receive when a patch that updates National Procedure Codes is released.

<span id="_Ref105140310" class="anchor"></span>Figure 248: Example Email Message for Updated National Procedure Codes Patch

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/280.png)

When EC Screens are inactivated due to changes in National Procedure Codes

When an EC NATIONAL PROCEDURES file (#725) patch is loaded, a review of the EVENT CODE SCREENS file (#720.3) is performed. Event Code Screens, which have either inactive CPT or procedure codes, or a procedure code with an inactive “default” CPT code attached, are reported.

Figure 249 is a screen capture of an example of the message a user could receive stating that Event Code Screens should be reviewed due to changes in the EC NATIONAL PROCEDURES file (#725).

> **NOTE:** After a patch updating file \#725:

- Check for Inactivated National Procedure Codes.
- Check for Event Code Screens with out-of-date procedure codes.

<span id="_Ref95141821" class="anchor"></span>Figure 249: Example of Event Code Screens to Review Message

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/281.png)

<span id="ExampleMessageExample1UserTerminated" class="anchor"></span>When terminated users result in access to DSS Units being affected

Figure 250 is a screen capture of an example of the email message a user could receive when an ECS User is terminated.

<span id="_Ref95142018" class="anchor"></span>Figure 250: Example 1 — ECS User Terminated Email Message

![Figure 251 is a screen capture of another example of the email message a user could receive when an ECS User is terminated.](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/282.png)

*Figure 251 is a screen capture of another example of the email message a user could receive when an ECS User is terminated.*

<span id="_Ref95142230" class="anchor"></span>Figure 251: Example 2 — ECS User Terminated Email Message

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/283.png)

<span id="ExampleMessageDeleteDSSUnit" class="anchor"></span>When a DSS Unit with no workload is deleted

Figure 252 shows an example of the automated MailMan message that arrives with the subject “DELETION OF UNUSED DSS UNIT FROM FILE \#724”. The accompanying message lists the deleted DSS Unit.

<span id="_Ref95142332" class="anchor"></span>Figure 252: Example Message when a DSS Unit is Deleted

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/284.png)

<span id="ExampleMessageDeleteEventCodeScreen" class="anchor"></span>When an Event Code Screen with no workload is deleted

Figure 253 shows an example of the automated MailMan message that arrives with the subject “DELETION OF UNUSED EVENT CODE SCREENS FROM File \#720.3”. The accompanying message lists the deleted Event Code Screen(s).

<span id="_Ref95321184" class="anchor"></span>Figure 253: Example Message when Event Code Screens are Deleted

![](event-capture-version-2-0-gui-user-guide-updated-ec-2-170/285.png)