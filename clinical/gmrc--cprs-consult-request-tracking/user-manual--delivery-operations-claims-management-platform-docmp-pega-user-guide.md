---
title: Delivery Operations Claims Management Platform (DOCMP) â€“ Pega User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: Delivery Operations Claims Management Platform (DOCMP) â€“ Pega
app_code: GMRC
app_name: "CPRS: Consult/Request Tracking"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - work
  - items
  - span
  - docmp
  - document
  - queue
  - claims
  - number
  - button
  - supervisor
page_count: 0
word_count: 23914
section_count: 20
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: January 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/docmp_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/docmp_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Delivery Operations Claims Management Platform (DOCMP)

  Software Version 23.6

  User Guide
---

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/001.png)

January 2026

Office of Information and Technology (OIT)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

<table>
<caption><p>Table 1: Documentation Symbols and Descriptions</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 53%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01/06/2026</td>
<td>2.4</td>
<td><p>Updated screenshots and instructions to reflect new features implemented in DOCMP version 23.6:</p>
<ul>
<li><p>OHI Certificate case detail screen updated to display additional metadata.</p></li>
<li><p>Added notes detailing changes to the OHI certificate case detail and digital upload screens.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>11/25/2025</td>
<td>2.3</td>
<td><p>Updated screenshots and instructions to reflect new features implemented in DOCMP version 23.3:</p>
<ul>
<li><p><strong>Auto-select related cases</strong> checkbox added to the EEV and CHAMPVA Supervisor dashboards.</p></li>
<li><p>Added Sponsor and Beneficiary user interfaces for the Document Details and Digital Upload screens to align with the VA form 10-10D data model.</p></li>
<li><p><strong>Appeal Type</strong> and <strong>CARC Code</strong> columns added to the Appeals Supervisor work queue.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>08/12/2025</td>
<td>2.2</td>
<td><p>Updates made to reflect changes in DOCMP version 22.2:</p>
<ul>
<li><p>Updated screens and instructions to reflect display name changes on the BCPU (CHAMPVA) Supervisor and Claims Examiner dashboards.</p></li>
<li><p>Updated screens to reflect addition of Service Recovery workflow.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>07/01/2025</td>
<td>2.1</td>
<td><p>Updates made to reflect changes in DOCMP version 21.6:</p>
<ul>
<li><p>Added new functional details for CVA Call Center Supervisor role and SPC Supervisor roles.</p></li>
<li><p>Updated figures throughout the document to reflect removal of PEGA labels from the application.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>06/03/2025</td>
<td>2.0</td>
<td>Updates made to reflect changes in DOCMP version 21.4: Added functional detail for the SPC Supervisor and Call Center Analyst roles.</td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>05/06/2025</td>
<td>1.9</td>
<td><p>Updates made to reflect changes in DOCMP version 21.2:</p>
<ul>
<li><p>Added functional detail for the Logistics Specialist role.</p></li>
</ul>
<ul>
<li><p>Updated Appeal Specialist role detail to reflect the new capabilities added to the workflow.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>04/01/2025</td>
<td>1.8</td>
<td><p>Updates made to reflect changes in DOCMP version 20.6:</p>
<ul>
<li><p>Added Section 4.8.2. - Uploading Files as Attachments.</p></li>
<li><p>Replaced figures throughout the document to accurately reflect changes in the user interface.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>03/04/2025</td>
<td>1.7</td>
<td><p>Updates made to reflect changes in DOCMP version 20.4:</p>
<ul>
<li><p>Added functional details for the Appeal Supervisor role.</p></li>
<li><p>Added additional details to Spina Bifida Supervisor role to reflect newly added Digital Upload functionality.</p></li>
<li><p>Added Section 4.4.-Unassigning Cases and replaced figures in the document to accurately reflect changes in the user interface.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>02/04/2025</td>
<td>1.6</td>
<td><p>Updates made to reflect changes in DOCMP version 20.2:</p>
<ul>
<li><p>Added functional details for the Spina Bifida Supervisor role.</p></li>
<li><p>Added additional details to R&amp;R Supervisor and R&amp;R Claims Examiner roles and updated figures to reflect newly added Get Next Work functionality.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>01/07/2025</td>
<td>1.5</td>
<td><p>Updates made to reflect changes in DOCMP version 19.6:</p>
<p>Added additional functional details for the R&amp;R Supervisor, R&amp;R Claims Examiner, and Spina Bifida Claims Examiner roles.</p></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>12/10/2024</td>
<td>1.4</td>
<td><p>Updates made to reflect changes in DOCMP version 19.4:</p>
<p>Added additional functional details for the DCDM Program Support Clerk role.</p></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>11/19/2024</td>
<td>1.3</td>
<td><p>Updates made to reflect changes in DOCMP version 19.3:</p>
<ul>
<li><p>Added additional functional details for the Translation COR, Translation PM, Translators, BCPU Supervisor, and BCPU Voucher Examiner roles.</p></li>
<li><p>Replaced figures in the document to accurately reflect changes in the user interface.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>08/20/2024</td>
<td>1.2</td>
<td><p>Updates made to reflect changes in DOCMP version 18.2:</p>
<ul>
<li><p>Added additional functional details for the FMP Supervisor, FMP Claims Examiner, and Appeal Specialist roles.</p></li>
<li><p>Added Section 4.7.-Uploading Files to reflect new Digital Upload feature.</p></li>
<li><p>Replaced figures throughout the document to accurately reflect changes in the user interface.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>06/06/2024</td>
<td>1.1</td>
<td><p>Updates made to reflect changes in DOCMP version 1.1:</p>
<ul>
<li><p>Added additional instructional detail for the DCDM Supervisor role.</p></li>
<li><p>Added new section headings to improve readability.</p></li>
<li><p>Replaced figures throughout the document to accurately reflect the new user interface.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>01/18/2024</td>
<td>1.0</td>
<td>Initial Release.</td>
<td>VetsEZ</td>
</tr>
</tbody>
</table>

Table 1: Documentation Symbols and Descriptions

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as VistA end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

Table of Contents

Table of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the User Guide](#organization-of-the-user-guide)
    - [Assumptions](#assumptions)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
  - [Enterprise Service Desk and Organizational Contacts](#enterprise-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [Configuration](#configuration)
  - [Data Flows](#data-flows)
  - [User Access Roles](#user-access-roles)
  - [Continuity of Operation](#continuity-of-operation)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
  - [System Menu](#system-menu)
    - [Homepage Overview](#homepage-overview)
  - [User Role Functionality](#user-role-functionality)
    - [Read-Only User](#read-only-user)
    - [EEV Supervisor](#eev-supervisor)
    - [EEV Contact Representatives](#eev-contact-representatives)
    - [OHI Supervisor](#ohi-supervisor)
    - [OHI Voucher Examiner](#ohi-voucher-examiner)
    - [DCDM Supervisor](#dcdm-supervisor)
    - [DCDM Program Support Clerk (PSC)](#dcdm-program-support-clerk-psc)
    - [FMP Supervisor](#fmp-supervisor)
    - [FMP Claims Examiner](#fmp-claims-examiner)
    - [Appeal Supervisor](#appeal-supervisor)
    - [Appeal Specialist](#appeal-specialist)
    - [Translation COR](#translation-cor)
    - [Translation PM](#translation-pm)
    - [Translators](#translators)
    - [BCPU (CHAMPVA) Supervisor](#bcpu-champva-supervisor)
    - [BCPU (CHAMPVA) Claims Examiner](#bcpu-champva-claims-examiner)
    - [Service Recovery Contract Lead](#service-recovery-contract-lead)
    - [Service Recovery Contractor Claims Examiner](#service-recovery-contractor-claims-examiner)
    - [SB Supervisor](#sb-supervisor)
    - [SB Claims Examiner](#sb-claims-examiner)
    - [Logistics Specialist](#logistics-specialist)
    - [SPC Supervisor](#spc-supervisor)
    - [SPC/Call Center Analyst](#spccall-center-analyst)
    - [CVA Call Center Supervisor](#cva-call-center-supervisor)
  - [Logging Off](#logging-off)
- [Using the Application](#using-the-application)
  - [Conducting a Search](#conducting-a-search)
  - [Uploading Files](#uploading-files)
    - [Uploading Files with Digital Upload](#uploading-files-with-digital-upload)
    - [Uploading Files as Attachments](#uploading-files-as-attachments)
  - [Reviewing Case Documents](#reviewing-case-documents)
    - [Audit (History) Function](#audit-history-function)
    - [Escalating Case Documents](#escalating-case-documents)
  - [Editing Case Documents](#editing-case-documents)
    - [Bulk Editing Case Documents](#bulk-editing-case-documents)
  - [Assigning Cases](#assigning-cases)
    - [Assigning Cases in the Work Queue](#assigning-cases-in-the-work-queue)
    - [Assigning Cases in the Work List](#assigning-cases-in-the-work-list)
  - [Unassigning Cases](#unassigning-cases)
  - [Pulling Reports](#pulling-reports)
    - [Exporting Reports](#exporting-reports)
  - [Working with OHI Certificates](#working-with-ohi-certificates)
    - [Self-Assign a Document](#self-assign-a-document)
    - [View and Update OHI Certificates](#view-and-update-ohi-certificates)
- [Appendix A: Acronyms and Abbreviations](#appendix-a-acronyms-and-abbreviations)
The Delivery Operations Claims Management Platform (DOCMP) is a tool designed to provide the Department of Veterans Affairs (VA) with a way to receive, track, and archive incoming documents. It enables Veteran Family Medical Programs (VFMP) to process intakes of new beneficiary applications, process, and review reimbursement claims, and logs the documents’ history once it is scanned into the VA system. These all enable VFMP to file and reimburse Veterans and their beneficiaries in a timely manner.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide simple and comprehensive instructions for using the DOCMP user interface (UI) screens.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delivery Operations Claims Management Platform (DOCMP) User Guide will provide explanations of each screen and of all user interface options within the context of an easy-to-understand demonstration data scenario.

This document is also designed to provide the user with screen-by-screen “how to” information on the usage of DOCMP.

### Organization of the User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Section 1: Introduction

This section provides the purpose of this manual, an overview of the DOCMP software, disclaimers, conventions, and contact information for the user to seek additional information.

- Section 2:System Summary

This section provides a graphical representation of the DOCMP data flow and an explanation of the application’s user access levels.

- Section 3:Getting Started

This section provides initial steps to register a user with DOCMP, as well as a general walkthrough of the system from initiation through exit, enabling the user to understand the sequence and flow of the system.

- Section 4:Using the Software

This section provides users with step-by-step instructions on how to complete operations in DOCMP.

- Appendix A:Acronyms and Abbreviations

This section provides a list of acronyms and abbreviations found in this document.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- Users have been provided with the appropriate active roles and access to the DOCMP web application.
- Users have completed any prerequisite training on the DOCMP web application.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide uses the following methods to highlight different aspects of the material.

<table>
<caption>Table used for formatting purposes onlySample Documentation Symbols Descriptions. An "i" with a circle around it indicates additional information. A triangle with an exclamation point inside indicates caution.</caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Symbol</th>
<th>Description</th>
</tr>
<tr class="odd">
<th><ol>
<li></li>
</ol></th>
<th>Informs the reader of generally useful information related to the topic.</th>
</tr>
<tr class="header">
<th><ol>
<li></li>
</ol></th>
<th>Contains useful information for accomplishing specific tasks.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Table used for formatting purposes onlySample Documentation Symbols Descriptions. An "i" with a circle around it indicates additional information. A triangle with an exclamation point inside indicates caution.

## Enterprise Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For issues related to DOCMP that cannot be resolved by this guide or the site administrator, please contact the Enterprise Service Desk (ESD).

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DOCMP is accessed using a secure web browser and a secure Virtual Private Network (VPN).

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc218593785" class="anchor"></span>Figure 1: DOCMP Data Flow Diagram

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/002.png)

## User Access Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The access to each feature in DOCMP is aligned to user roles and responsibilities. Some features included in this User Guide will not be visible or available to all users. There are 24 DOCMP user access roles:

- VFMP Read-Only: This user type can only search and view documents and is unable to make any updates or submissions.
- Eligibility, Enrollment, and Verification (EEV) Supervisor: EEV Supervisors can use DOCMP to assign eligibility cases to their team members as well as generate reports on a variety of case-related information.
- EEV Contact Representatives: EEV Contact Representatives can use DOCMP to edit their assigned cases, view attachments to enter the beneficiary's demographics into Veterans Health Information Systems and Technology Architecture (VistA) and notate determination information.
- Office of Health Information (OHI) Supervisor: OHI Supervisors can use DOCMP to assign cases to their team members.
- OHI Voucher Examiner: OHI Voucher Examiners from the Review and Resolution Department (R&R) can use DOCMP to see the incoming OHI Certificates for applicants that are already entered into VistA and finalize their insurance eligibility.
- Document Control and Document Management (DCDM) Supervisor: DCDM Supervisors can use DOCMP to view and assign cases to other DCDM users and re-route incorrectly assigned cases to the appropriate team.
- DCDM Program Support Clerk (PSC): DCDM PSCs can use DOCMP to view cases, edit document metadata, and route incorrectly assigned cases to the appropriate team.
- Foreign Medical Program (FMP) Supervisor: FMP Supervisors can use DOCMP to view and assign cases to other FMP users and re-route incorrectly assigned cases to the appropriate team.
- FMP Claims Examiner: FMP Claims Examiners can use DOCMP to edit their assigned cases and view attachments.
- Appeal Supervisor: Appeal Supervisors can use DOCMP to view and assign cases to other Appeal users, review escalated cases, and re-route incorrectly assigned cases to the appropriate team.
- Appeal Specialist: Appeal Specialists can use DOCMP to view and edit document details, as well as self-assign cases sent to the Appeals queue.
- Translation Contract Office Representative (COR): Translation COR users can use DOCMP to review incoming documents that need translation, approve translated documents, and route completed items to the appropriate team for processing.
- Translation Program Manager (PM): Translation PMs can use DOCMP to verify document pages prior to translation, add language(s), and upload the final translation in PDF format to the DOCMP case file.
- Translators: Translators can use DOCMP to search for and view assigned documents ready for translation.
- Beneficiary Claims Processing Unit (BCPU) Supervisor: BCPU Supervisors can use DOCMP to assign Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) claims eligibility cases to their team members as well as generate reports on a variety of case-related information.
- BCPU Claims Examiner: BCPU Claims Examiners can use DOCMP to edit their assigned cases and view attachments.
- Service Recovery (SR) Contract Lead: SR Contract Leads can use DOCMP to view, edit, and assign cases to their team members.
- SR ContractorClaims Examiner: SR Contractor Claims Examiners can use DOCMP to edit their assigned cases and view attachments.
- Spina Bifida (SB) Supervisor: SB Supervisors can use DOCMP to assign cases to their team members, review escalated cases, pull reports, and re-route cases to the appropriate team as needed.
- SB Claims Examiner: SB Claims Examiners can use DOCMP to view and edit their assigned cases, as well as re-route cases to other team members.
- Logistics Specialist: Logistics Specialists can use DOCMP to view incoming documents and Logistics Mail reports.
- Specialty Contact Center (SPC) Supervisor: SPC Supervisors can use DOCMP to view, edit, and assign cases to their team members.
- SPC/Call Center Analyst: SPC Analysts (referred to as Call Center Analysts in this document) can use DOCMP to view and edit their assigned cases and review attachments.
- CHAMPVA (CVA) Call Center Supervisor: CVA Call Center Supervisors can use DOCMP to view cases, monitor the workload of various teams and upload new files into the application as needed.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA Enterprise Cloud (VAEC) handles the Continuity of Operations.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the process of gaining access to the DOCMP application and walks through the application from initiation to exit.

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DOCMP is accessed using a [VA Single Sign-On Internal (SSOi) login](https://pega.docmp.vaec.va.gov/prweb/PRAuth/DOCMP).

<span id="_Toc218593786" class="anchor"></span>Figure 2: VA Single Sign-On Page

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/003.png)

Click Sign In with VA PIV Card to authenticate your Personal Identity Verification (PIV) card and sign into the application. If you are not already connected to the VA network, the DOCMP Login Page will display when the URL is accessed.

<span id="_Toc218593787" class="anchor"></span>Figure 3: DOCMP Login Page

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/004.png)

To sign in from the login page complete the following steps:

1.  Enter your User name and Password.
2.  Select Log in.

Alternatively, you can select the Login with DOCMP_NP button to enable the SSOi login and sign in with your PIV credentials.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Homepage Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc218593788" class="anchor"></span>Figure 4: DOCMP Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/005.png)

The DOCMP homepage contains some general elements that are common to all user views:

- Dashboard - is the main content area of the application and displays content in individual tabs based on what the user has selected.

<span id="_Toc218593789" class="anchor"></span>Figure 5: DOCMP Dashboard

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/006.png)

- Application Header – located at the top of the page. Displays the application name and the role type of the active user. The header also includes the Get Next Work button (where applicable), the notifications icon, and the user profile icon.
2.  Notifications are not currently enabled at this time, but this feature will be available with a future release.

<span id="_Toc218593790" class="anchor"></span>Figure 6: DOCMP Application Header

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/007.png)

- Tabs – located below the Application Header. Displays the active content on the dashboard. When a new action is taken (e.g., selecting a document selection or conducting a search) a new tab will open.

<span id="_Toc218593791" class="anchor"></span>Figure 7: DOCMP Tabs

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/008.png)

- Sidebar Navigation – located on the left side of the page. Lists the operations available for each role type.

<span id="_Toc218593792" class="anchor"></span>Figure 8: DOCMP Sidebar Navigation

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/009.png)

## User Role Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DOCMP application offers different functionality for the operations specific to each of the user roles outlined in [Section 2.3](#user-access-roles). Once you have been assigned your role, you will be able to access its functions.

### Read-Only User 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Read-only users may run searches and view existing documents within the application but cannot make any changes or updates.

<span id="_Toc218593793" class="anchor"></span>Figure 9: Default Read-Only Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/010.png)

### EEV Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the EEV Supervisor role can assign cases to their team members, pull reports, and review escalated cases.

<span id="_Toc218593794" class="anchor"></span>Figure 10: EEV Supervisor Dashboard

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/011.png)

EEV Supervisors have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
3.  For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab that allows the user to choose from a variety of options to refine their search of available documents.
- Reports: Located within the sidebar navigation; opens a new tab which displays all reports that are available to view.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Get Next Work: This button is in the header at the top of the page. When selected, it opens the user’s next work item in a new tab.

#### EEV Supervisor Dashboard Overview

The EEV Supervisor dashboard contains three main sections:

- Daily Workload
  - Oldest Open Applications by Date
  - Workload Summary
- Work Queue
- Work List

#### Daily Workload

<span id="_Toc218593795" class="anchor"></span>Figure 11: EEV Supervisor Dashboard - Daily Workload Report

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/012.png)

The DailyWorkload section displays a report of the total workload inventory from the previous day, organized by type. The data shown in this report is updated daily. It contains the following fields:

- Beginning inventory: The total count of work items that were in the system at the end of the previous day.
- \# of items received: The number of new items received the previous day.
- Work completed: The number of work items marked as completed.
- Ending inventory: The total count of open work items in the system the last time the report was refreshed.
- Date received in HAC: Date when VFMP received the file; included in the Doc Batch Number.
- Days out: The number of days from date received to previous/current day.

Oldest Open Applications by Date is a read-only module that can be hidden or expanded and displays the three earliest creation dates of items listed in the work queue. The number displayed at the right is the total number of items that were created on that date.

<span id="_Toc218593796" class="anchor"></span>Figure 12: EEV Supervisor Dashboard – Oldest Applications Module

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/013.png)

The Workload section is located below the daily workload report and provides a summary of the total number of work items in each work queue category included in the daily workload.

<span id="_Toc218593797" class="anchor"></span>Figure 13: EEV Supervisor Dashboard – Workload Summary

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/014.png)

#### Work Queue Overview

The WorkQueue can be filtered by category and lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593798" class="anchor"></span>Figure 14: EEV Supervisor Dashboard – Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/015.png)

- Work Queue: Drop-down menu that allows a supervisor to select the category of work items they wish to view. Categories include:
  - Unassigned – All items that have not yet been assigned to a team member or queue.
  - Supervisor Action – Items that require action on behalf of the supervisor.
  - FMP Enrollments – Items related to claims submitted to the Foreign Medical Program (FMP).
- Assign To: Drop-down menu that lists team members or groups that can have cases assigned to them.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
4.  The Assign button is grayed out by default and is only enabled when a selection has been made from the Assign To drop-down menu.
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Auto select related cases: Checkbox that enables all documents in the same batch to be automatically selected for a desired action.
- Result Count: A read-only field that displays the total number of items still listed in the queue.

The items in the Work Queue are listed under the following column headings:

- Created Date: The date on which the document was uploaded into the system.
- Doc Batch Number: A system-generated number used to identify the batch associated with a document upload; especially useful when there are multiple documents associated with a case.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s SSN.
- Beneficiary Name: First and last name of the person named as beneficiary.
- Beneficiary SSN: The beneficiary’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Complete, etc.)

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593799" class="anchor"></span>Figure 15: EEV Supervisor Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/016.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
2.  Created Date From and To;
    - PDI/DocBatch Number; and
    - Doc Type drop down menu.
3.  Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List contains work items that have already been assigned to a particular user.

<span id="_Toc218593800" class="anchor"></span>Figure 16: EEV Supervisor Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/017.png)

- Work List: Drop-down menu that allows a supervisor to select a team member from the drop-down menu to see what has already been assigned to that individual.
- Assign To: Drop-down menu that lists team members or groups that can have cases assigned to them. A supervisor can also use this menu to unassign an item from a user and/or re-assign it to another team member, if desired.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
- Bulk Edit: Located above the work list, this button allows the user to select multiple cases and update them all with the same information or action.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are displayed under the following column headings:

- Created Date: The date on which the document was uploaded into the system.
- Doc Batch Number: A system-generated number used to identify the batch associated with a document upload; especially useful when there are multiple documents associated with a case.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s SSN.
- Beneficiary Name: First and last name of the person named as beneficiary.
- Beneficiary SSN: The beneficiary’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Complete, etc.)
- Owner: Displays the user that is currently assigned to work on the item.

### EEV Contact Representatives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the EEV Contact Representative role can view and edit the documents that have been assigned to them in DOCMP. After logging into the application, the EEV Contact Representative Dashboard displays. Their dashboard displays a table of work items that have been assigned to them.

<span id="_Toc218593801" class="anchor"></span>Figure 17: EEV Contact Representative Dashboard

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/018.png)

Contact Representative users have access to the following functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
5.  For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently opened documents.
- Get Next Work: This button is in the header at the top of the page. When selected, it opens the user’s next work item in a new tab.
- Bulk Edit: Located above the work list, this button allows the user to select multiple cases and update them all with the same information or action.
- Refresh button: This button allows the user to refresh the list to view the most recent items.

  The WorkQueue lists all items that have been assigned to the user and contains the following fields and column headings:
- Result Count: A read-only field that displays the total number of items that have been assigned to the user.
- Created Date: The date on which the document was uploaded into the system.
- Doc Batch Number: A system-generated number used to identify the batch associated with a document upload; especially useful when there are multiple documents associated with a case.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s Social Security Number (SSN).
- Beneficiary Name: First and last name of the person named as beneficiary.
- Beneficiary SSN: The beneficiary’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Complete, etc.)
- Owner: Displays the user that is currently assigned to work on the item.

### OHI Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the OHI Supervisor role can assign cases to their team members and review escalated cases.

<span id="_Toc218593802" class="anchor"></span>Figure 18: OHI Supervisor Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/019.png)

OHI Supervisors have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
6.  For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Reports: Located within the sidebar navigation; opens a new tab which displays all reports that are available to view.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Get Next Work: This button is in the header at the top of the page. When selected, it opens the user’s next work item in a new tab.

#### OHI Supervisor Dashboard Overview

The OHI Supervisor dashboard provides a Workload summary at the top of the page, displaying the total number of work items that have been submitted to the OHI queue.

<span id="_Toc218593803" class="anchor"></span>Figure 19: OHI Supervisor Dashboard – Workload

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/020.png)

After the Workload summary, the dashboard is divided into two main sections:

- Work Queue
- Work ListOldest Open Applications by Date is a read-only module that can be hidden or expanded and displays the three earliest creation dates of items listed in the work queue. The number displayed at the right is the total number of items that were created on that date.

<span id="_Toc218593804" class="anchor"></span>Figure 20: OHI Supervisor Dashboard – Oldest Applications Module

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/021.png)

#### Work Queue Overview

The WorkQueue can be filtered by category and lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593805" class="anchor"></span>Figure 21: OHI Supervisor Dashboard – Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/022.png)

- Work Queue: Drop-down menu that allows a supervisor to select the category of work items they wish to view. Categories include:
  - Unassigned – All items that have not yet been assigned to a team member or queue.
  - Supervisor Action – Items that require action on behalf of the supervisor.
- Assign To: Drop-down menu that lists team members or groups that can have cases assigned to them.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
7.  The Assign button is grayed out by default and is only enabled when a selection has been made from the Assign To drop-down menu.
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items still listed in the queue.

The items in the Work Queue are listed under the following column headings:

- Created Date: The date on which the document was uploaded into DOCMP.
- Doc Batch Number: A system-generated number used to identify the batch associated with a document upload; especially useful when there are multiple documents associated with a case.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s SSN.
- Beneficiary Name: First and last name of the person named as beneficiary.
- Beneficiary SSN: The beneficiary’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Complete, etc.)

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593806" class="anchor"></span>Figure 22: OHI Supervisor Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/023.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
4.  Created Date From and To;
    - PDI/DocBatch Number; and
    - Doc Type drop down menu.
5.  Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to a particular user.

<span id="_Toc218593807" class="anchor"></span>Figure 23: OHI Supervisor Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/024.png)

- Work List: Drop-down menu that allows a supervisor to select a team member from the drop-down menu to see what has already been assigned to that individual.
- Assign To: Drop-down menu that lists of team members or groups that can have cases assigned to them. A supervisor can also use this menu to unassign an item from a user and/or re-assign it to another team member, if desired.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
- Bulk Edit: Located above the work list, this button allows the user to select multiple cases and update them all with the same information or action.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- Created Date: The date on which the document was uploaded into the system.
- Doc Batch Number: A system-generated number used to identify the batch associated with a document upload; especially useful when there are multiple documents associated with a case.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s SSN.
- Beneficiary Name: First and last name of the person named as beneficiary.
- Beneficiary SSN: The beneficiary’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Complete, etc.)
- Owner: Displays the user that is currently assigned to work on the item.

### OHI Voucher Examiner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the OHI Voucher Examiner role can self-assign, view, and update OHI certificates in DOCMP. After logging into the application, the OHI Voucher Examiner user’s default view will be their Work Queue, which displays any work items that have already been assigned.

<span id="_Hlk155368243" class="anchor"></span>Figure 24: Default OHI Voucher Examiner Screen

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/025.png)

OHI Voucher Examiners have access to the following functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
8.  For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Get Next Work: This button is located in the header at the top of the page. When selected, it opens the user’s next work item in a new tab.
- Assign to Me: This button allows examiners to assign work items to themselves.
- Refresh button: This button allows the user to refresh the list to view the most recent items.

  The Work Queue lists all items that have already been assigned to the user and contains the following fields:
- Result Count: A read-only field that displays the total number of items that have been assigned to the user.
- Created Date: The date on which the document was uploaded into the system.
- Doc Batch Number: A system-generated number used to identify the batch associated with a document upload; especially useful when there are multiple documents associated with a case.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s SSN.
- Beneficiary Name: First and last name of the person named as beneficiary.
- Beneficiary SSN: The beneficiary’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Complete, etc.)

### DCDM Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Document Control and Document Management (DCDM) Supervisor role can view and assign cases to other DCDM users and re-route incorrectly assigned cases to the appropriate team as needed.

<span id="_Toc218593809" class="anchor"></span>Figure 25: DCDM Supervisor Homepage (1 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/026.png)

<span id="_Toc218593810" class="anchor"></span>Figure 26: DCDM Supervisor Homepage (2 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/027.png)

DCDM Supervisors have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
9.  For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Assign To: This button allows supervisors to assign or re-assign work items to other teams and DCDM users.

#### DCDM Supervisor Dashboard Overview

The DCDM Supervisor dashboard provides a Workload summary at the top of the page, displaying the total number of work items that have been submitted to the DCDM Reroutes queue.

<span id="_Toc218593811" class="anchor"></span>Figure 27: DCDM Supervisor Dashboard – Workload

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/028.png)

After the Workload summary, the dashboard is divided into two main sections:

- Work Queue
- Work List

#### Work Queue Overview

The WorkQueue can be filtered by category and lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593812" class="anchor"></span>Figure 28: DCDM Supervisor Dashboard – Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/029.png)

- Work Queue: Drop-down menu that allows a supervisor to select the category of work items they wish to view. DCDM Supervisors only have the DCDM Reroutes queue to work from.
- Result Count: A read-only field that displays the total number of items still listed in the queue.
- Assign To: Drop-down menu that allows supervisors to select the type of assignee (Users or Teams) to re-route cases to.
- Refresh button: This button allows the user to refresh the list to view the most recent items.

The items in the Work Queue are listed under the following column headings:

- Created Date: The date on which the document was uploaded into DOCMP.
- PDI/Doc Batch Number: A system-generated number used to identify the batch associated with a document upload; especially useful when there are multiple documents associated with a case.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Complete, etc.)

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593813" class="anchor"></span>Figure 29: DCDM Supervisor Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/030.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
6.  Created Date From and To;
7.  PDI/DocBatch Number; and
8.  Doc Type drop down menu.
9.  Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to a particular user.

<span id="_Toc218593814" class="anchor"></span>Figure 30: DCDM Supervisor Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/031.png)

- Work List: Drop-down menu that allows a DCDM supervisor to select themselves or another DCDM supervisor and display what items have already been assigned to them.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- Created Date: The date on which the document was uploaded into the system.
- PDI/Doc Batch Number: A system-generated number used to identify the batch associated with a document upload; especially useful when there are multiple documents associated with a case.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Complete, etc.)
- Owner: Displays the user that is currently assigned to work on the item.

### DCDM Program Support Clerk (PSC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Document Control and Document Management (DCDM) Program Support Clerk (PSC) role can view, edit, and reroute incorrectly assigned documents to the appropriate team as needed. After logging into the application, the DCDM PSC homepage displays.

<span id="_Toc218593815" class="anchor"></span>Figure 31: DCDM PSC Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/032.png)

DCDM PSC users have access to the following functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
10. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Reroute To: Drop-down menu that allows PSC users to select the appropriate team to re-route a selected case to.
- Refresh button: This button allows the user to refresh the list to view the most recent items.

  The Worklist displays all items that have been assigned to the user and contains the following fields and column headings:
- Result Count: A read-only field that displays the total number of items that have been assigned to the user.
- PDI/DocBatch Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document.
- Sponsor Name: First and last name of the Veteran.
- Sponsor SSN: The Veteran’s Social Security Number.
- Doc Status: Displays the working status of the item.
- Owner: Displays the user that is currently assigned to work on the item.

### FMP Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Foreign Medical Program (FMP) Supervisor role can view and assign cases to other FMP users and re-route incorrectly assigned cases to the appropriate team as needed.

<span id="_Toc218593816" class="anchor"></span>Figure 32: Default FMP Supervisor Homepage (1 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/033.png)

<span id="_Toc218593817" class="anchor"></span>Figure 33: Default FMP Supervisor Homepage (2 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/034.png)

FMP Supervisors have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
11. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Reports: Located within the sidebar navigation; opens a new tab which displays all reports that are available to view.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Get Next Work: This button is in the header at the top of the page. When selected, it opens the user’s next work item in a new tab.
- Assign To: This button allows supervisors to assign or re-assign work items to other teams and FMP users.

#### FMP Supervisor Dashboard Overview

The FMP Supervisor dashboard provides a Workload summary at the top of the page, displaying the total number of work items that have been submitted to the FMP Claims queue.

<span id="_Toc218593818" class="anchor"></span>Figure 34: FMP Supervisor Dashboard – Workload

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/035.png)

After the Workload summary, the dashboard is divided into two main sections:

- Work Queue
- Work List

#### Work Queue Overview

The WorkQueue lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593819" class="anchor"></span>Figure 35: FMP Supervisor Dashboard – Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/036.png)

- Work Queue: Drop-down menu that allows a supervisor to select the category of work items they wish to view. Categories include:
- FMP-Incoming/Unassigned: All items that have not yet been assigned to a team member or queue.
- FMP-Supervisor Action: Items that require action on behalf of the supervisor.
- Result Count: A read-only field that displays the total number of items still listed in the queue.
- Assign To: Drop-down menu that allows supervisors to select the type of assignee (Users or Teams) to re-route cases to.
- Refresh button: This button allows the user to refresh the list to view the most recent items.

The items in the Work Queue are listed under the following column headings:

- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the Veteran.
- Sponsor SSN: The Veteran’s Social Security Number.
- Document Status: Displays the working status of the item (e.g., FMP Incoming, Complete, etc.).

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593820" class="anchor"></span>Figure 36: FMP Supervisor Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/037.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
10. Created Date From and To;
11. PDI/DocBatch Number; and
12. Doc Type drop down menu.
13. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to a particular user.

<span id="_Toc218593821" class="anchor"></span>Figure 37: FMP Supervisor Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/038.png)

- Work List: Drop-down menu that allows a DCDM supervisor to select and display items assigned to the FMP claims queue or specific FMP users.
- Assign To: Drop-down menu that allows supervisors to select the assignee to route cases to. The Assign button is available to select once an assignee has been chosen from the list.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the Veteran.
- Sponsor SSN: The Veteran’s Social Security Number.
- Claim Number: The number assigned to a specific claim.
- Document Status: Displays the working status of the item (e.g., FMP Incoming, Complete, etc.).
- Owner: Displays the user that is currently assigned to work on the item.

### FMP Claims Examiner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Foreign Medical Program (FMP) Claims Examiner role can view and edit the documents that have been assigned to them in DOCMP. After logging into the application, the FMP Claims Examiner homepage displays.

<span id="_Toc218593822" class="anchor"></span>Figure 38: FMP Claims Examiner Dashboard

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/039.png)

FMP Claims Examiner users have access to the following functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
12. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Get Next Work: This button is in the header at the top of the page. When selected, it opens the user’s next work item in a new tab.
- Refresh button: This button allows the user to refresh the list to view the most recent items.

  The Worklist displays all items that have been assigned to the user and contains the following fields and column headings:
- Total Count: A read-only field that displays the total number of items that have been assigned to the user.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document.
- Sponsor Name: First and last name of the Veteran.
- Sponsor SSN: The Veteran’s Social Security Number.
- Claim Number: The number assigned to a specific claim.
- Document Status: Displays the working status of the item.

### Appeal Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Appeal Supervisor role can assign cases to their team members, review escalated cases, and route incorrectly assigned cases to the appropriate teams.

<span id="_Toc218593823" class="anchor"></span>Figure 39: Appeal Supervisor Homepage (1 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/040.png)

<span id="_Toc218593824" class="anchor"></span>Figure 40: Appeal Supervisor Homepage (2 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/041.png)

Appeal Supervisors have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
13. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

#### Appeal Supervisor Dashboard Overview

The Appeal Supervisor dashboard contains three main sections:

- Daily Workload (including a Workload summary)
- Work Queue
- Work List

#### Daily Workload

<span id="_Toc218593825" class="anchor"></span>Figure 41: Appeal Supervisor Dashboard - Daily Workload Report

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/042.png)

The DailyWorkload section displays a report of the total workload inventory from the previous day, organized by type. The data shown in this report is updated daily. It contains the following fields:

- Beginning inventory: The total count of work items that were in the system at the end of the previous day.
- \# of items received: The number of new items received the previous day.
- Work completed: The number of work items marked as completed.
- Ending inventory: The total count of open work items in the system the last time the report was refreshed.
- Date received in HAC: Date when VFMP received the file; included in the Doc Batch Number.
- Days out: The number of days from date received to previous/current day.

The Workload section is located below the daily workload report and provides a summary of the total number of work items in each work queue category included in the daily workload.

<span id="_Toc218593826" class="anchor"></span>Figure 42: Appeal Supervisor Dashboard – Workload

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/043.png)

#### Work Queue Overview

The WorkQueue can be filtered by category and lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593827" class="anchor"></span>Figure 43: Appeal Supervisor Dashboard – Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/044.png)

- Work Queue: Drop-down menu that allows a supervisor to select the category of work items they wish to view.
- Assign To: Drop-down menu that lists team members or groups that can have cases assigned to them.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
14. The Assign button is grayed out by default and is only enabled when a selection has been made from the Assign To drop-down menu.
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items listed in the queue.

The items in the Work Queue are listed under the following column headings:

- Priority: Displays a Yes or No value based on whether the item has been identified as a priority document.
- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Pages: Displays the total number of pages included in the document.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Beneficiary Name: First and last name of the person named as beneficiary.
- Beneficiary SSN: The beneficiary’s SSN.
- Appeal Type: Specifies the type of appeal the document is associated with.
- Claims Adjustment Reason Code (CARC) Code: Healthcare billing code used to specify the reason for the adjustment or denial of the claim associated with the appeal.
- Doc Status: Displays the working status of the item (e.g., Open, Pending Triage, etc.)

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593828" class="anchor"></span>Figure 44: Appeal Supervisor Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/045.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
14. Created Date From and To;
    - PDI/DocBatch Number; and
    - Doc Type drop down menu.
15. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to a particular user.

<span id="_Toc218593829" class="anchor"></span>Figure 45: Appeal Supervisor Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/046.png)

- Work List: Drop-down menu that allows a supervisor to select a team member from the drop-down menu to see what has already been assigned to that individual.
- Assign To: Drop-down menu that lists of team members or groups that can have cases assigned to them. A supervisor can also use this menu to unassign an item from a user and/or re-assign it to another team member, if desired.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- Priority: Displays a Yes or No value based on whether the item has been identified as a priority document.
- Created Date: The date on which the document was uploaded into the system.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Pages: Displays the total number of pages included in the document.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s SSN.
- Beneficiary Name: First and last name of the person named as beneficiary.
- Beneficiary SSN: The beneficiary’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Pending Triage, etc.)
- Owner: Displays the user that is currently assigned to work on the item.

### Appeal Specialist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Appeal Specialist role can view, edit, and self-assign cases in DOCMP.

<span id="_Toc218593830" class="anchor"></span>Figure 46: Appeal Specialist Homepage (1 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/047.png)

<span id="_Toc218593831" class="anchor"></span>Figure 47: Appeal Specialist Homepage (2 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/048.png)

Appeal Specialist users have access to the following functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
15. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

#### Appeal Specialist Dashboard Overview

The Appeal Specialist dashboard is divided into two main sections:

- Work Queue
- Work List
16. If desired, Appeal Specialist users can select the Work Queue heading link to collapse the entire Work Queue section and focus solely on their Work List.

#### Work Queue Overview

The WorkQueue table can be filtered by category and lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593832" class="anchor"></span>Figure 48: Appeal Specialist Dashboard – Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/049.png)

- Work Queue: Drop-down menu that allows the user to select the category of work items they wish to view.
- Assign To Me button: This button allows Appeal Specialist users to assign cases to themselves. When the button is selected, the case is removed from the work queue and displays in the user’s work list.
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items listed in the queue.

The items in the Work Queue are listed under the following column headings:

- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Page Count: Displays the total number of pages included in the document.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s SSN.
- Beneficiary Name: First and last name of the person named as beneficiary.
- Beneficiary SSN: The beneficiary’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Pending Triage, etc.)

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593833" class="anchor"></span>Figure 49: Appeal Specialist Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/050.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
16. Created Date From and To;
    - PDI/DocBatch Number; and
    - Doc Type drop down menu.
17. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to the user.

<span id="_Toc218593834" class="anchor"></span>Figure 50: Appeal Specialist Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/051.png)

- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- Created Date: The date on which the document was uploaded into the system.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Sponsor Name: First and last name of the sponsor.
- Sponsor SSN: The sponsor’s SSN.
- Beneficiary Name: First and last name of the person named as beneficiary.
- Beneficiary SSN: The beneficiary’s SSN.
- Doc Status: Displays the working status of the item (e.g., Open, Pending Triage, etc.)

### Translation COR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Translation Contract Office Representative (COR) role review and assess documents and/or individual pages that need translation and send to the Translation Program Manager (PM). After receiving notification from the PM that final translation is complete, the COR will approve the translated document and send it to the Foreign Medical Program (FMP) work queue for processing.

17. If a document should go to a team other than FMP Claims, the COR will need to add a comment specifying the correct destination and request that it be rerouted by the Document Control and Document Management (DCDM) team.

<span id="_Toc218593835" class="anchor"></span>Figure 51: Translation COR Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/052.png)

Translation CORs have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
18. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Reports: Located within the sidebar navigation; opens a new tab which displays all reports that are available to view.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

#### Translation COR Dashboard Overview

The Translation COR dashboard provides a Workload summary at the top of the page, displaying the total number of work items that have been submitted to the Translations queue.

<span id="_Toc218593836" class="anchor"></span>Figure 52: Translation COR Dashboard – Workload

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/053.png)

After the Workload summary, the dashboard is divided into two main sections:

- Work Queue
- Work List

#### Work Queue Overview

The WorkQueue lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593837" class="anchor"></span>Figure 53: Translation COR Dashboard – Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/054.png)

- Work Queue: Drop-down menu that allows a supervisor to select the category of work items they wish to view. Categories include:
- Pending Translation: Items that require COR review and verification to determine if they need translating or not.
- Translation COR-Approval Requests: Translated items that have been submitted final approval.
- COR – Pending Approval: Items waiting to be approved.
- Translation COR-Supervisor Action: Items that require action on behalf of the supervisor.
- Translators – Translation Requested: Items that have been assigned to the Translators queue.
- Translators - Unassigned Requests: Items that have not yet been assigned to a translator.
- Result Count: A read-only field that displays the total number of items still listed in the queue.
- Assign To: Drop-down menu that allows the COR to select an assignee to re-route cases to.
- Refresh button: This button allows the user to refresh the list to view the most recent items.

The items in the Work Queue are listed under the following column headings:

- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Page(s) to Translate: Specifies the page numbers within the document that need to be translated.
- Sponsor Name: First and last name of the Veteran.
- Sponsor SSN: The Veteran’s Social Security Number.
- Document Status: Displays the working status of the item (e.g., Pending Translation, Complete, etc.).

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593838" class="anchor"></span>Figure 54: Translation COR Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/055.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
18. Created Date From and To;
19. PDI/DocBatch Number; and
20. Doc Type drop down menu.
21. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to a particular user.

<span id="_Toc218593839" class="anchor"></span>Figure 55: Translation COR Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/056.png)

- Work List: Drop-down menu that allows a Translation COR to select and display items assigned to themselves, the PM, or specific translators.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Language(s): The language(s) the document needs to be translated to.
- Page(s) to Translate: Specifies the page numbers within the document that need to be translated.
- Document Status: Displays the working status of the item (e.g., FMP Incoming, Complete, etc.).
- Owner: Displays the user that is currently assigned to work on the item.

### Translation PM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Translation Program Manager (PM) role verify the document pages that should be translated and add languages as needed before assigning the document to a translator. Once the document has been translated, the translator will notify the PM, who then uploads a final PDF version of the translated document into DOCMP for the Contract Office Representative (COR) to review.

<span id="_Toc218593840" class="anchor"></span>Figure 56: Translation PM Homepage (1 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/057.png)

<span id="_Toc218593841" class="anchor"></span>Figure 57: Translation PM Homepage (2 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/058.png)

Translation PMs have access to the following main functions:

- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Reports: Located within the sidebar navigation; opens a new tab which displays all reports that are available to view.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

#### Translation PM Dashboard Overview

The Translation PM dashboard provides a Workload summary at the top of the page, displaying the total number of work items that have been submitted to the Translations queue.

<span id="_Toc218593842" class="anchor"></span>Figure 58: Translation PM Dashboard – Workload

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/059.png)

After the Workload summary, the dashboard is divided into two main sections:

- Work Queue
- Work List

#### Work Queue Overview

The WorkQueue lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593843" class="anchor"></span>Figure 59: Translation PM Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/060.png)

- Work Queue: Drop-down menu that allows the PM to select the category of work items they wish to view. Categories include:
  - Translators - Unassigned Requests: Items that have not yet been assigned to a translator.
- Translators – Secondary Review: Items that require additional review.
- Result Count: A read-only field that displays the total number of items still listed in the queue.
- Assign To: Drop-down menu that allows the COR to select an assignee to re-route cases to.
- Refresh button: This button allows the user to refresh the list to view the most recent items.

The items in the Work Queue are listed under the following column headings:

- Queue Received Date: The date on which the document was uploaded into DOCMP and added to the Translations queue.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Language(s): The language(s) the document needs to be translated to.
- Page(s) to Translate: Specifies the page numbers within the document that need to be translated.
- Doc Status: Displays the working status of the item (e.g., Translation Requested, Complete, etc.)

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593844" class="anchor"></span>Figure 60: Translation PM Dashboard – Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/061.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
22. Created Date From and To;
23. PDI/DocBatch Number; and
24. Doc Type drop down menu.
25. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to a particular user.

<span id="_Toc218593845" class="anchor"></span>Figure 61: Translation PM Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/062.png)

- Work List: Drop-down menu that allows the Translation PM to select and display items assigned to themselves, the COR, or specific translators.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Language(s): The language(s) the document needs to be translated to.
- Page(s) to Translate: Specifies the page numbers within the document that need to be translated.
- Queue Received Date: The date on which the document was uploaded into DOCMP and added to the Translations queue.
- Doc Status: Displays the working status of the item (e.g., FMP Incoming, Complete, etc.).
- Owner: Displays the user that is currently assigned to work on the item.

### Translators

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Translators select their work from a spreadsheet managed by the Translation Program Manager (PM) and can search for and view their assigned documents in DOCMP. Once the document has been translated, the translator will notify the PM through a business process external to DOCMP as this function is not available in the application at this time.

<span id="_Toc218593846" class="anchor"></span>Figure 62: Translator Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/063.png)

Translators have access to the following main functions:

- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

#### Translator Dashboard Overview

The Translation PM dashboard is divided into two main sections:

- Work Queue
- Work List

#### Work Queue Overview

The Translator WorkQueue displays items in the main Translations queue that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593847" class="anchor"></span>Figure 63: Translator Dashboard – Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/064.png)

- Work Queue: In the Translator view, this drop-down menu is read-only and displays items in the Translators - Unassigned Requests category.
- Result Count: A read-only field that displays the total number of items still listed in the queue.
- Refresh button: This button allows the user to refresh the list to view the most recent items.

The items in the Work Queue are listed under the following column headings:

- Queue Received Date: The date on which the document was uploaded into DOCMP and added to the Translations queue.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Language(s): The language(s) the document needs to be translated to.
- Page(s) to Translate: Specifies the page numbers within the document that need to be translated.
- Doc Status: Displays the working status of the item (e.g., Translation Requested, Complete, etc.).

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593848" class="anchor"></span>Figure 64: Translator Dashboard – Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/065.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
26. Created Date From and To;
27. PDI/DocBatch Number; and
28. Doc Type drop down menu.
29. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to the translator.

<span id="_Toc218593849" class="anchor"></span>Figure 65: Translator Dashboard – Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/066.png)

- Work List: In the Translator view, this drop-down menu is read-only, and displays items that have been assigned to the user.
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document (e.g., school certificate, Medicare, etc.).
- Language(s): The language(s) the document needs to be translated to.
- Page(s) to Translate: Specifies the page numbers within the document that need to be translated.
- Queue Received Date: The date on which the document was uploaded into DOCMP and added to the Translations queue.
- Doc Status: Displays the working status of the item (e.g., FMP Incoming, Complete, etc.).
- Owner: Displays the user that is currently assigned to work on the item.

### BCPU (CHAMPVA) Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Beneficiary Claims Processing Unit (BCPU) Supervisor role can assign cases to their team members, pull reports, and review escalated cases. The BCPU team works with Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) claims, so DOCMP displays this role as CHAMPVA Supervisor.

<span id="_Toc218593850" class="anchor"></span>Figure 66: Default BCPU Supervisor Homepage (1 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/067.png)

<span id="_Toc218593851" class="anchor"></span>Figure 67: Default BCPU Supervisor Homepage (2 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/068.png)

BCPU Supervisors have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
19. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Reports: Located within the sidebar navigation; opens a new tab which displays all reports that are available to view.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Get Next Work: This button is in the header at the top of the page. When selected, it opens the user’s next work item in a new tab.

#### BCPU (CHAMPVA) Supervisor Dashboard Overview

The BCPU Supervisor dashboard contains three main sections:

- Daily Workload (including a Workload summary)
- Work Queue
- Work List

#### Daily Workload

<span id="_Toc218593852" class="anchor"></span>Figure 68: BCPU Supervisor Dashboard - Daily Workload Report

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/069.png)

The DailyWorkload section displays a report of the total workload inventory from the previous day, organized by type. The data shown in this report is updated daily. It contains the following fields:

- Beginning inventory: The total count of work items that were in the system at the end of the previous day.
- \# of items received: The number of new items received the previous day.
- Work completed: The number of work items marked as completed.
- Ending inventory: The total count of open work items in the system the last time the report was refreshed.
- Date received in HAC: Date when VFMP received the file; included in the Doc Batch or PDI Number.
- Days out: The number of days from date received to previous/current day.

The Workload section of the BCPU Supervisor dashboard is located below the daily workload report and displays a summary of the total number of work items that have been submitted to the BCPU claims queue.

<span id="_Toc218593853" class="anchor"></span>Figure 69: BCPU Supervisor Dashboard – Workload

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/070.png)

After the Workload summary, the remainder of the dashboard consists of two main sections:

- Work Queue
- Work List

#### Work Queue Overview

The WorkQueue lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593854" class="anchor"></span>Figure 70: BCPU Supervisor Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/071.png)

- Work Queue: Drop-down menu that allows a supervisor to select the category of work items they wish to view. Categories include:
  - BCPU-Incoming/Unassigned – All items that have not yet been assigned to a team member or queue.
- BCPU-Supervisor Action – Items that require action on behalf of the supervisor.
- Assign To: Drop-down menu that allows supervisors to select the assignee to route cases to.
- Auto select related cases: Checkbox that enables all documents in the same batch to be automatically selected for a desired action.
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items still listed in the queue.

The items in the Work Queue are listed under the following column headings:

- Priority: Displays a Yes or No value based on whether or not the item has been identified as a priority document.
- Created Date: The date on which the document was uploaded into DOCMP.
- Page Count: Displays the total number of pages included in the document.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Shelf Work: A category that will display a Yes or No/False value based on whether or not shelf work has been associated with the case. The BCPU supervisor can manually select or change this field in the document details if needed.
- Doc Type: Specifies the type of document (e.g. CHAMPVA, CHAMPVA Foreign, etc.).
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Document Status: Displays the working status of the item (e.g., Pending BCPU Review, Complete, etc.).

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593855" class="anchor"></span>Figure 71: BCPU Supervisor Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/072.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
30. Created Date From and To;
31. PDI/DocBatch Number; and
32. Doc Type drop down menu.
33. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to a particular user.

<span id="_Toc218593856" class="anchor"></span>Figure 72: BCPU Supervisor Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/073.png)

- Work List: Drop-down menu that allows a BCPU supervisor to select and display items assigned to the BCPU claims queue or specific BCPU users.
- Assign To: Drop-down menu that allows supervisors to select the assignee to route cases to. The Assign button becomes available to select once an assignee has been chosen from the list.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- Priority: Displays a Yes or No value based on whether the item has been identified as a priority document.
- Assigned Date: The date which the document was assigned to the user.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Page Count: Displays the total number of pages included in the document.
- Doc Type: Specifies the type of document (e.g. CHAMPVA, CHAMPVA Foreign, etc.).
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Document Status: Displays the working status of the item (e.g., Pending BCPU Review, Complete, etc.).
- Owner: Displays the user that is currently assigned to work on the item.

### BCPU (CHAMPVA) Claims Examiner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Beneficiary Claims Processing Unit (BCPU) Claims Examiner role can view and edit the documents that have been assigned to them in DOCMP. The BCPU team works with CHAMPVA claims, so DOCMP displays this role as CHAMPVA Claims Examiner. After logging into the application, the BCPU Claims Examiner homepage displays.

<span id="_Toc218593857" class="anchor"></span>Figure 73: BCPU Claims Examiner Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/074.png)

BCPU Claims Examiner users have access to the following functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
20. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Get Next Work: This button is in the header at the top of the page. When selected, it opens the user’s next work item in a new tab.
- Refresh button: This button allows the user to refresh the list to view the most recent items.

  The WorkList displays all items that have been assigned to the user and contains the following fields and column headings:
- Priority: Displays a Yes or No value based on whether the item has been identified as a priority document.
- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Page Count: Displays the total number of pages included in the document.
- Doc Type: Specifies the type of document (e.g. CHAMPVA, CHAMPVA Foreign, etc.).
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Document Status: Displays the working status of the item (e.g., Pending BCPU Review, Complete, etc.).
- Owner: Displays the user that is currently assigned to work on the item.

### Service Recovery Contract Lead

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Service Recovery Contract Lead role can use DOCMP to view, edit, and assign cases to their team members or other Service Recovery users. After logging into the application, the SR Contract Lead homepage displays.

<span id="_Toc218593858" class="anchor"></span>Figure 74: SR Contract Lead Homepage (1 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/075.png)

<span id="_Toc218593859" class="anchor"></span>Figure 75: SR Contract Lead Homepage (2 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/076.png)

SR Contract Lead have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
21. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Get Next Work: This button is in the header at the top of the page. When selected, it opens the user’s next work item in a new tab.

#### Service Recovery Contract Lead Dashboard Overview

The SR Contract Lead dashboard contains three main sections:

- Daily Workload (including a Workload summary)
- Work Queue
- Work List

#### Daily Workload

<span id="_Toc218593860" class="anchor"></span>Figure 76: SR Contract Lead Dashboard - Daily Workload Report

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/077.png)

The DailyWorkload section displays a report of the total workload inventory from the previous day, organized by type. The data shown in this report is updated daily. It contains the following fields:

- Beginning inventory: The total count of work items that were in the system at the end of the previous day.
- \# of items received: The number of new items received the previous day.
- Work completed: The number of work items marked as completed.
- Ending inventory: The total count of open work items in the system the last time the report was refreshed.
- Date received in HAC: Date when VFMP received the file; included in the Doc Batch or PDI Number.
- Days out: The number of days from date received to previous/current day.

The Workload section is located below the daily workload report and displays a summary of the total number of work items that have been submitted to the Service Recovery queue.

<span id="_Toc218593861" class="anchor"></span>Figure 77: SR Contract Lead Dashboard – Workload

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/078.png)

After the Workload summary, the remainder of the SR Contract Lead dashboard consists of two main sections:

- Work Queue
- Work List

#### Work Queue Overview

The WorkQueue can be filtered by category and lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593862" class="anchor"></span>Figure 78: SR Contract Lead Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/079.png)

- Work Queue: Drop-down menu that allows a supervisor to select the category of work items they wish to view.
- Assign To: Drop-down menu that allows supervisors to select the assignee to route cases to.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
22. The Assign button is grayed out by default and is only enabled when a selection has been made from the Assign To drop-down menu.
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items still listed in the queue.

The items in the Work Queue are listed under the following column headings:

- Priority: Displays a Yes or No value based on whether the item has been identified as a priority document.
- Created Date: The date on which the document was uploaded into DOCMP.
- Page Count: Displays the total number of pages included in the document.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Shelf Work: A category that will display a Yes or No value based on whether shelf work has been associated with the case.
- Doc Type: Specifies the type of document.
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Document Status: Displays the working status of the item (e.g., Service Recovery Incoming, Complete, etc.).

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593863" class="anchor"></span>Figure 79: SR Contract Lead Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/080.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
34. Created Date From and To;
    - PDI/DocBatch Number; and
    - Doc Type drop down menu.
35. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to the user.

<span id="_Toc218593864" class="anchor"></span>Figure 80: SR Contract Lead Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/081.png)

- Work List: Drop-down menu that allows a supervisor to select a team member from the drop-down menu to see what has already been assigned to that individual.
- Assign To: Drop-down menu that lists team members or groups that can have cases assigned to them. A supervisor can also use this menu to unassign an item from a user and/or re-assign it to another team member, if desired.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- Priority: Displays a Yes or No value based on whether the item has been identified as a priority document.
- Assigned Date: The date which the document was assigned to the user.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Page Count: Displays the total number of pages included in the document.
- Doc Type: Specifies the type of document (e.g. Reopen, Walkthrough, etc.).
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Document Status: Displays the working status of the item (e.g., Service Recovery Incoming, Complete, etc.).
- Owner: Displays the user that is currently assigned to work on the item.

### Service Recovery Contractor Claims Examiner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Contractor Claims Examiner role can view and edit the documents that have been assigned to them in DOCMP. After logging into the application, the SR Contractor Claims Examiner homepage displays.

<span id="_Toc218593865" class="anchor"></span>Figure 81: SR Contractor Claims Examiner Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/082.png)

SR Contractor Claims Examiner users have access to the following functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
23. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.
- Get Next Work: This button is in the header at the top of the page. When selected, it opens the user’s next work item in a new tab.

  The Work list displays all items that have been assigned to the user and contains the following fields and column headings:
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.
- Priority: Displays a Yes or No value based on whether the item has been identified as a priority document.
- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Page Count: Displays the total number of pages included in the document.
- Shelf Work: A category that will display a Yes or No/False value based on whether shelf work has been associated with the case.
- Doc Type: Specifies the type of document.
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Document Status: Displays the working status of the item (e.g., Service Recovery Incoming, Complete, etc.).

### SB Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Spina Bifida (SB) Supervisor role can use DOCMP to assign cases to their team members, review escalated cases, pull reports, and re-route cases to the appropriate team as needed. After logging into the application, the Spina Bifida Supervisor homepage displays.

<span id="_Toc218593866" class="anchor"></span>Figure 82: Spina Bifida Supervisor Homepage (1 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/083.png)

<span id="_Toc218593867" class="anchor"></span>Figure 83: Spina Bifida Supervisor Homepage (2 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/084.png)

SB Supervisors have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
24. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Reports: Located within the sidebar navigation; opens a new tab which displays all reports that are available to view.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

#### SB Supervisor Dashboard Overview

The SB Supervisor dashboard provides a Workload summary at the top of the page, displaying the total number of work items that have been submitted to the Spina Bifida queue.

<span id="_Toc218593868" class="anchor"></span>Figure 84: SB Supervisor Dashboard – Workload

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/085.png)

After the Workload summary, the Spina Bifida Supervisor dashboard is divided into two main sections:

- Work Queue
- Work List

#### Work Queue Overview

The WorkQueue can be filtered by category and lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593869" class="anchor"></span>Figure 85: SB Supervisor Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/086.png)

- Work Queue: Drop-down menu that allows a supervisor to select the category of work items they wish to view.
- Assign To: Drop-down menu that allows supervisors to select the assignee to route cases to.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
25. The Assign button is grayed out by default and is only enabled when a selection has been made from the Assign To drop-down menu.
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items still listed in the queue.

The items in the Work Queue are listed under the following column headings:

- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Page Count: Displays the total number of pages included in the document.
- Doc Type: Specifies the type of document.
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Document Status: Displays the working status of the item (e.g., Spina Bifida Incoming, Complete, etc.).

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593870" class="anchor"></span>Figure 86: SB Supervisor Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/087.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
36. Created Date From and To;
    - PDI/DocBatch Number; and
    - Doc Type drop down menu.
37. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to the user.

<span id="_Toc218593871" class="anchor"></span>Figure 87: SB Supervisor Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/088.png)

- Work List: Drop-down menu that allows a supervisor to select a team member from the drop-down menu to see what has already been assigned to that individual.
- Assign To: Drop-down menu that lists team members or groups that can have cases assigned to them. A supervisor can also use this menu to unassign an item from a user and/or re-assign it to another team member, if desired.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- Assigned Date: The date which the document was assigned to the user.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Page Count: Displays the total number of pages included in the document.
- Doc Type: Specifies the type of document (e.g. Spina Bifida Claim or Appeal, etc.).
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Document Status: Displays the working status of the item (e.g., Spina Bifida Incoming, Complete, etc.).

### SB Claims Examiner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Spina Bifida (SB) Claims Examiner role can use DOCMP to view and edit their assigned cases. They can also re-route cases to other team members as needed. After logging into the application, the Spina Bifida Claims Examiner homepage displays.

<span id="_Toc218593872" class="anchor"></span>Figure 88: Spina Bifida Claims Examiner Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/089.png)

SB Claims Examiners have access to the following functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
26. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

The WorkList displays all items that have been assigned to the user and contains the following fields and column headings:

- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.
- Assigned Date: The date which the document was assigned to the user.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Page Count: Displays the total number of pages included in the document.
- Doc Type: Specifies the type of document (e.g. Spina Bifida Claim, Spina Bifida Correspondence, etc.).
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Document Status: Displays the working status of the item (e.g., Spina Bifida Incoming, Complete, etc.).

### Logistics Specialist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Logistics Specialist role can view documents and Logistics reports in DOCMP. After logging into the application, the Logistics Specialist user’s default view will be the Work Queue, which displays documents sent to the Logistics-Incoming Mail queue.

<span id="_Toc218593873" class="anchor"></span>Figure 89: Logistics Specialist Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/090.png)

Logistics Specialists have access to the following functions:

- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Reports: Located within the sidebar navigation; opens a new tab which displays all reports that are available to view.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

  The Work Queue lists all items sent to the Logistics-Incoming Mail queue under the following headings:
- Created Date: The date on which the document was uploaded into the system.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document (e.g., General Incoming).

### SPC Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Specialty Contact Center (SPC) Supervisor role can use DOCMP to assign cases to their team members, review cases, and re-route cases to the appropriate team as needed. After logging into the application, the SPC Supervisor homepage displays.

<span id="_Toc218593874" class="anchor"></span>Figure 90: SPC Supervisor Homepage (1 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/091.png)

<span id="_Toc218593875" class="anchor"></span>Figure 91: SPC Supervisor Homepage (2 of 2)

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/092.png)

SPC Supervisors have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
27. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

#### SPC Supervisor Dashboard Overview

The SPC Supervisor dashboard contains three main sections:

- Daily Workload (including a Workload summary)
- Work Queue
- Work List

#### Daily Workload

<span id="_Toc218593876" class="anchor"></span>Figure 92: SPC Supervisor Dashboard - Daily Workload Report

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/093.png)

The DailyWorkload section displays a report of the total workload inventory from the previous day, organized by type. The data shown in this report is updated daily. It contains the following fields:

- Beginning inventory: The total count of work items that were in the system at the end of the previous day.
- \# of items received: The number of new items received the previous day.
- Work completed: The number of work items marked as completed.
- Ending inventory: The total count of open work items in the system the last time the report was refreshed.
- Date received in HAC: Date when VFMP received the file; included in the Doc Batch or PDI Number.
- Days out: The number of days from date received to previous/current day.

The Workload section is located below the daily workload report and displays a summary of the total number of work items that have been submitted to the SPC queue.

<span id="_Toc218593877" class="anchor"></span>Figure 93: SPC Supervisor Dashboard – Workload Summary

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/094.png)

After the Workload summary, the remainder of the SPC Supervisor dashboard consists of two main sections:

- Work Queue
- Work List

#### Work Queue Overview

The WorkQueue can be filtered by category and lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593878" class="anchor"></span>Figure 94: SPC Supervisor Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/095.png)

- Work Queue: Drop-down menu that allows a supervisor to select the category of work items they wish to view.
- Assign To: Drop-down menu that allows supervisors to select the assignee to route cases to.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
28. The Assign button is grayed out by default and is only enabled when a selection has been made from the Assign To drop-down menu.
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items still listed in the queue.

The items in the Work Queue are listed under the following column headings:

- Priority: Displays a Yes or No value based on whether the item has been identified as a priority document.
- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document.
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Beneficiary SSN: Social Security number of the Veteran’s beneficiary.
- Doc Status: Displays the working status of the item (e.g., Pre-Auth Incoming, Complete, etc.).
- Preauthorization Type: Displays the type of preauthorization assigned to the item.

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593879" class="anchor"></span>Figure 95: SPC Supervisor Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/096.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
38. Created Date From and To;
    - PDI/DocBatch Number; and
    - Doc Type drop down menu.
39. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to the user.

<span id="_Toc218593880" class="anchor"></span>Figure 96: SPC Supervisor Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/097.png)

- Work List: Drop-down menu that allows a supervisor to select a team member from the drop-down menu to see what has already been assigned to that individual. They can also use this menu to view all work assigned to the SPC Call Center.
- Assign To: Drop-down menu that lists team members or groups that can have cases assigned to them. A supervisor can also use this menu to unassign an item from a user and/or re-assign it to another team member, if desired.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- Priority: Displays a Yes or No value based on whether or not the item has been identified as a priority document.
- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document.
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Beneficiary SSN: Social Security number of the Veteran’s beneficiary.
- Doc Status: Displays the working status of the item (e.g., Pre-Auth Incoming, Complete, etc.).
- Preauthorization Type: Displays the type of preauthorization assigned to the item.
- Owner: Displays the user that is currently assigned to work on the item.

### SPC/Call Center Analyst

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the Call Center Analyst role can view, edit, and self-assign cases in DOCMP.

<span id="_Toc218593881" class="anchor"></span>Figure 97: Call Center Analyst Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/098.png)

Call Center Analyst users have access to the following functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
29. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

#### Call Center Analyst Dashboard Overview

The Call Center Analyst dashboard is divided into two main sections:

- Work Queue
- Work List
30. If desired, Call Center Analyst users can select the Work Queue heading link to collapse the entire Work Queue section and focus solely on their Work List.

#### Work Queue Overview

The WorkQueue table can be filtered by category and lists all items that need to be assigned or reviewed. Items in the queue are listed from oldest to newest.

<span id="_Toc218593882" class="anchor"></span>Figure 98: Call Center Analyst Dashboard – Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/099.png)

- Work Queue: Drop-down menu that allows the user to select the category of work items they wish to view.
- Assign To: Drop-down menu that lists SPC supervisors that can have cases assigned to them.
- Assign: This button allows Call Center Analysts to assign cases to themselves or to a supervisor.
31. The Assign button is grayed out by default and is only enabled when a selection has been made from the Assign To drop-down menu.
- Refresh button: This button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items still listed in the queue.

The items in the Work Queue are listed under the following column headings:

- Priority: Displays a Yes or No value based on whether or not the item has been identified as a priority document.
- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document.
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Beneficiary SSN: Social Security number of the Veteran’s beneficiary.
- Doc Status: Displays the working status of the item (e.g., Pre-Auth Incoming, Complete, etc.).
- Preauthorization Type: Displays the type of preauthorization assigned to the item.

Users can customize their view of the items in the Work Queue using Work Queue Filters.

<span id="_Toc218593883" class="anchor"></span>Figure 99: Call Center Analyst Work Queue Filters

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/100.png)

1.  To filter the items listed in the Work Queue, select the Work Queue Filters link. The section will expand and display the following fields:
40. Created Date From and To;
    - PDI/DocBatch Number; and
    - Doc Type drop down menu.
41. Enter a value in either field and/or choose an option from the Doc Type drop-down menu and select Filter. The work queue will display only the items that meet the criteria you selected. Select the Clear button to display all queue results or begin a new search.

#### Work List Overview

The Work List section contains work items that have already been assigned to the user.

<span id="_Toc218593884" class="anchor"></span>Figure 100: Call Center Analyst Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/101.png)

- Work List: Drop-down menu that allows a Call Center Analyst to see what has already been assigned to them. Users can also use this menu to view all work assigned to the SPC Call Center.
- Assign To: Drop-down menu that lists SPC supervisors. A supervisor can also use this menu to unassign an item from a user and/or re-assign it to another team member, if desired.
- Assign: This button allows supervisors to assign or re-assign work items to their team members.
- Refresh button: Displayed as an image, this button allows the user to refresh the list to view the most recent items.
- Result Count: A read-only field that displays the total number of items contained in the list.

The items in the Work List are listed under the following column headings:

- Priority: Displays a Yes or No value based on if the item has been identified as a priority document.
- Created Date: The date on which the document was uploaded into DOCMP.
- PDI Number: A system-generated number used to uniquely identify a document upload.
- Doc Type: Specifies the type of document.
- Beneficiary Name: First and last name of the Veteran’s beneficiary.
- Beneficiary SSN: Social Security number of the Veteran’s beneficiary.
- Doc Status: Displays the working status of the item (e.g., Pre-Auth Incoming, Complete, etc.).
- Preauthorization Type: Displays the type of preauthorization assigned to the item.
- Owner: Displays the user that is currently assigned to work on the item.

### CVA Call Center Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the CHAMPVA (CVA) Call Center Supervisor role have a read-only ability to view cases, monitor the workload of other teams and upload new files into the application as needed.

<span id="_Toc218593885" class="anchor"></span>Figure 101: CVA Call Center Supervisor Homepage

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/102.png)

CVA Call Center Supervisors have access to the following main functions:

- New: This button activates the Digital Upload feature which allows users to electronically upload files into the application.
32. For more information and instruction on using this feature, refer to [Uploading Files with Digital Upload](#uploading-files-with-digital-upload).
- Search: This button is located within the sidebar navigation and when selected, opens a new tab allowing the user to choose from a variety of options to refine their search of available documents.
- Recents: Accessed from the sidebar navigation and lists the user’s most recently accessed documents.

#### CVA Call Center Supervisor Dashboard Overview

<span id="_Toc218593886" class="anchor"></span>Figure 102: CVA Call Center Supervisor Dashboard - Daily Workload Report

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/103.png)

The CVA Call Center Supervisor dashboard is comprised primarily of a DailyWorkload section which displays a report of the total workload inventory for multiple teams from the previous day, organized by the type of document. The data shown in this report is updated daily. It contains the following fields:

- Beginning inventory: The total count of work items that were in the system at the end of the previous day.
- \# of items received: The number of new items received the previous day.
- Work completed: The number of work items marked as completed.
- Ending inventory: The total count of open work items in the system the last time the report was refreshed.
- Date received in HAC: Date when VFMP received the file; included in the Doc Batch Number.
- Days out: The number of days from date received to previous/current day.

## Logging Off

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Properly exiting the application helps to prevent personal patient information from being visible to others. To re-enter the application, reload the DOCMP URL.

1.  To exit the DOCMP application, select the user profile icon in the top-right corner of the screen to open the drop-down menu.

<span id="_Toc218593887" class="anchor"></span>Figure 103: User Profile drop-down menu

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/104.png)

42. Select Log off.

# Using the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DOCMP provides user functionality for the following operations:

- Conducting a Search
- Uploading Files
- Uploading Files with Digital Upload
- Uploading Files as Attachments
- Reviewing Case Documents
- Audit (History) Function
- Escalating Case Documents
- Editing Cases
- Bulk Editing Case Documents
- Assigning Cases
- Assigning Cases in the Work Queue
- Assigning Cases in the Work List
- Unassigning Cases
- Pulling Reports
- Exporting Reports
- Working with OHI Certificates
- Self-Assign a Document
- View and Update OHI Certificates

## Conducting a Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any user role may run searches and view files in the DOCMP application. To conduct a search, follow the steps listed below:

1.  From the sidebar navigation menu, select Search. The DOCMP Search Options tab displays.

<span id="_Hlk155370332" class="anchor"></span>Figure 104: DOCMP Search Options Tab

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/105.png)

1.  The Search tab allows you to select the radio buttons for the type of search you want to conduct. The available data fields will change based on your selection. The options are as follows:
    - Sponsor Demographics
    - Beneficiary Demographics
    - PDI/Document Batch Number
    - Advanced
2.  Enter the search criteria into the applicable field(s) to locate the item you want to view.

<span id="_Hlk155781651" class="anchor"></span>Figure 105: DOCMP Search Option Entry

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/106.png)

33. For the purposes of this instruction, search criteria has been entered into the Sponsor Last Name field.
3.  Select the Search button. The search results display in the Result Count section of the page.

<span id="_Toc218593890" class="anchor"></span>Figure 106: DOCMP Search Results

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/107.png)

34. When conducting a new search, no results will display until the Search button has been selected.
2.  Select the Clear button if you want to start over with new search criteria.

## Uploading Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Uploading Files with Digital Upload

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any user role (except for Read-Only, Translation PM, and Translators) may upload files into the DOCMP application using the Digital Upload function. When a file is uploaded by a user, it will automatically save to the Work Queue of that user’s specific role (for example, an upload completed by an EEV Supervisor will save to the EEV Work Queue). To upload a file using this method, complete the following steps:

1.  From the Homepage, select the New button in the top left corner of the screen. The Digital Upload option will display.

<span id="_Toc218593891" class="anchor"></span>Figure 107: Digital Upload Button

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/108.png)

43. Select Digital Upload to begin adding your file(s). The Digital Upload function will open in a new tab and display the Step 1 of 3: Select Files to Upload screen.

<span id="_Toc218593892" class="anchor"></span>Figure 108: Digital Upload Step 1 - Select Files

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/109.png)

44. Select the ADD FILES link to begin adding your file(s). The Attach file(s) window will display.

<span id="_Toc218593893" class="anchor"></span>Figure 109: Digital Upload - Attach File(s) Screen

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/110.png)

45. Select the Select file(s) button. A File Explorer dialog box displays. Users also have the option to drag files into the area labeled Drag and drop files here.

<span id="_Toc218593894" class="anchor"></span>Figure 110: Digital Upload – File Explorer

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/111.png)

46. From File Explorer, select the desired document to upload. You can select multiple documents.
35. The recommended file types to upload are .gif, .jpg, .pdf, and .txt.
47. Select Open to upload the file into DOCMP. Once the document is uploaded, it will display below the file selection area.

<span id="_Toc218593895" class="anchor"></span>Figure 111: Digital Upload – Attached File

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/112.png)

48. When all files are uploaded, select the Attach button. The uploaded file will display in the Files list.

<span id="_Toc218593896" class="anchor"></span>Figure 112: Digital Upload – Added File

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/113.png)

36. If you are uploading multiple files for one application, you can select the same number for each of them in the Relationship ID drop-down menu. This tells the system that these files should be grouped together and assigned an appropriate document batch number. If your files are not related, you can leave this field blank.
49. Select the Next button. The Step 2 of 3: Select Document Type screen will display.

<span id="_Toc218593897" class="anchor"></span>Figure 113: Digital Upload – Step 2 - Select Document Type

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/114.png)

50. Select an option from the required Document Type drop-down menu, then select Next. The Step 3 of 3: Enter Document Details screen will display.
37. If you select the Mark as Complete checkbox in Step 2, the system will automatically require you to enter values for the Sponsor Name and Sponsor SSN fields in the document details. These fields are usually optional by default.

<span id="_Toc218593898" class="anchor"></span>Figure 114: Digital Upload – Step 3- Enter Document Details

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/115.png)

51. Confirm that the system has populated the Document Type drop-down menu correctly. Select the desired option from the Document Action drop-down menu (Open, Complete, or Resolveas Duplicate) and add any Comments that may be needed.
52. If applicable, select the Sponsor Information and/or Beneficiary Information tabs to review or add information in the remaining fields.
38. Additional tabs will display for VA Forms 10-10D (Certification) and 10-7959c OHI certification document types (Medicare Beneficiaries, Other Health Insurance, and Certification). Select and complete the fields in these tabs as needed.
53. Select SAVE AND FINISH. A Complete message will display with confirmation that the document was uploaded successfully. Select Close to exit.

<span id="_Toc218593899" class="anchor"></span>Figure 115: Upload Complete

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/116.png)

### Uploading Files as Attachments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with an Appeal user role (Appeal Supervisor or Appeal Specialist) can upload files as attachments to existing cases within the document details screen. To upload a document using this method, follow the steps outlined below:

1.  From the Work Queue or Work List, select the link for the case you would like to review. The details of the selected document will open in a new tab.

<span id="_Toc218593900" class="anchor"></span>Figure 116: Document Details Screen

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/117.png)

54. Select the Upload Files button to begin adding your file(s). The Upload Documents dialog box will display.

<span id="_Toc218593901" class="anchor"></span>Figure 117: Upload Documents Dialog Box

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/118.png)

55. Select the Select file(s) button. A File Explorer dialog box displays. Users also have the option to drag files into the area labeled Drag and drop files here.

<span id="_Toc218593902" class="anchor"></span>Figure 118: File Explorer Dialog Box

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/119.png)

56. From File Explorer, select the desired document to upload. Only files with the .pdf extension can be added here. You can select up to three documents.
39. The number of attachments that can be added using this method are limited to three PDF files.
57. Select Open to upload the file. Once the document is uploaded, it will display below the file selection area.

<span id="_Toc218593903" class="anchor"></span>Figure 119: Upload Documents – Attached File

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/120.png)

58. When all files have been added, select the Attach button. The uploaded file will display under the User uploaded files heading on the Details page.

<span id="_Toc218593904" class="anchor"></span>Figure 120: User Uploaded File

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/121.png)

40. The number of User uploaded files is limited to three PDFs. Once three files have been added, the Upload Files button will be disabled.

## Reviewing Case Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any user role may view documents in the DOCMP application. To view the details of a document, follow the steps listed below:

<span id="_Toc218593905" class="anchor"></span>Figure 121: User Dashboard

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/122.png)

1.  From the Dashboard, select the link under the Doc Batch Number column for the file you would like to view. A Review Document screen for the selected document will open in a new tab with the Details section displayed by default.

<span id="_Toc218593906" class="anchor"></span>Figure 122: Review Document Screen

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/123.png)

59. The Details section allows users to view additional information about the selected document, and is organized under the following tabs:
60. Document Details
61. Sponsor Information
62. Beneficiary Information

    Each of these tabs can be selected to view or edit the applicable information for the selected document.
41. Additional tabs will display for VA Forms 10-10D (Certification) and 10-7959c OHI certification document types (Medicare Beneficiaries, Other Health Insurance, and Certification). Select and complete the fields in these tabs as needed.
42. The Sponsor and Beneficiary Information tabs will not display for users with read-only access.
63. Select the Comments tab to review any comments that may have been added. If there are existing comments, the number of included comments will display next to the tab heading.
3.  Selecting the link displayed under Attachments will allow you to download and view a PDF copy of the full document.
64. To close an active document, hover your mouse or move your cursor over the tab then select the X that displays to the right of the document name/number.

<span id="_Toc218593907" class="anchor"></span>Figure 123: Close Document Tab

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/124.png)

### Audit (History) Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audit function tracks every action performed on a selected document and allows users to view that item’s history in a table organized by the following headings:

- Time: Displays the date and time a change was made to the document.
- Description: Summary of the action or change made to the document.
- Performed by: Displays the user that made the change.

To view the history of a case document from the Review Document screen, select the Audit tab. The History table will display.

<span id="_Toc218593908" class="anchor"></span>Figure 124: Document Audit Tab – History Table

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/125.png)

### Escalating Case Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Escalate function allows you to assign a document to a supervisor for further review or to request a rescan. To escalate a case, follow the steps listed below:

1.  From the Dashboard, select the link under the Doc Batch Number column for the file you would like to view. A Review Document screen will display.

<span id="_Toc218593909" class="anchor"></span>Figure 125: Review Document Screen

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/126.png)

2.  Select the Escalate button (located at the top right corner of the page) and a confirmation dialog box will display.

<span id="_Toc218593910" class="anchor"></span>Figure 126: Document Details – Escalate Confirmation Dialog Box

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/127.png)

65. Select Stay on Page if you want to continue working on the document. Select Yes, Escalate to confirm the escalation to your supervisor. When the escalation is complete, the system will return you to your dashboard.

## Editing Case Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with a Supervisor or Contact Representative role may edit case documents in the DOCMP application. The fields that can be edited include the beneficiary's name and SSN, dates, document type, and case status. To edit a case, complete the following steps:

<span id="_Toc218593911" class="anchor"></span>Figure 127: EEV Contact Representative User Dashboard

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/128.png)

1.  From the Dashboard, select the Doc Batch Number of the work item and the Review Document screen will open in a new tab.

<span id="_Toc218593912" class="anchor"></span>Figure 128: EEV Contact Representative Document Details Tab

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/129.png)

66. Under Details, confirm that the system has populated the Document Type drop-down menu correctly or select the correct option.
67. Select the desired option (Complete, Open, or Resolvedas Duplicate) from the Document Action drop-down menu.
68. If applicable, select the Sponsor Information and/or Beneficiary Information tabs to review or add information in the remaining fields if needed.
43. Additional tabs will display for VA Forms 10-10D and 10-7959c (OHI certification) document types as these include or require Certification, Medicare Beneficiaries, and/or Other Health Insurance information. Select and complete the fields in these tabs as needed.
69. Select the Comments tab to add any comments that may be needed.
70. When editing is complete, select SAVE. A confirmation message will display.

<span id="_Toc218593913" class="anchor"></span>Figure 129: Save Confirmation

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/130.png)

44. Select the GO BACK button if you want to return to your work list without saving your changes.
71. Select the Close button to exit the screen and return to the dashboard.

### Bulk Editing Case Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DOCMP allows users with an EEV Supervisor or EEV Contact Representative role to select multiple cases and update them all with the same information or action. To bulk edit a case, complete the following steps:

1.  From the Dashboard (or EEV Supervisor Work List), select the checkboxes next to the cases you want to edit.

<span id="_Toc218593914" class="anchor"></span>Figure 130: User Work List Selected Cases

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/131.png)

2.  Select the Bulk Edit button. The Bulk Edits dialog box displays.

<span id="_Toc218593915" class="anchor"></span>Figure 131: Bulk Edits Dialog Box

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/132.png)

3.  Enter the information or select the action you want to complete for the selected items.
4.  Select Update. The dialog box will close, and your update(s) will be visible in the work list.
45. Select the Cancel button if you want to return to your work list without saving your changes.

## Assigning Cases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Assigning Cases in the Work Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only users with a Supervisor role can assign cases in the application. To assign cases from the Work Queue, follow the steps listed below:

1.  From the Work Queue drop-down menu select Unassigned. All unassigned cases will be displayed on the dashboard.

<span id="_Hlk155371230" class="anchor"></span>Figure 132: Unassigned Work Queue

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/133.png)

72. Select the checkbox next to the case/document you want to assign.
73. From the Assign To drop-down menu, select the name of the individual you want to assign the file to.
74. Select Assign. The screen will update with a confirmation that an item has been assigned to the user.

<span id="_Toc218593917" class="anchor"></span>Figure 133: Assigned Document Confirmation Message

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/134.png)

46. You can also verify that the assignment was successful by selecting the worker’s name from the Work List drop-down menu. All cases assigned to that worker will be displayed.

### Assigning Cases in the Work List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assign cases from the work list, follow the steps listed below:

1.  From the Work List drop-down menu, select Assigned or the name of the user whose work list you are editing. The cases will be displayed on the dashboard.

<span id="_Toc218593918" class="anchor"></span>Figure 134: Assigned Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/135.png)

75. Select the checkbox next to the case/document you want to assign/re-assign.
76. From the Assign To drop-down menu, select the name of the individual you want to assign the file to.

<span id="_Toc218593919" class="anchor"></span>Figure 135: Work List – Assign To Selection

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/136.png)

77. Select Assign. The item will be removed from the work list.

## Unassigning Cases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with a Supervisor role can unassign cases in the application. To unassign a case, follow the steps listed below:

1.  From the Work List drop-down menu, select Assigned or the name of the user whose work list you are editing. The cases will be displayed on the dashboard.

<span id="_Toc218593920" class="anchor"></span>Figure 136: Assigned Work List

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/137.png)

78. Select the Unassign option from the Assign To drop-down menu. The Unassign button will display.

<span id="_Toc218593921" class="anchor"></span>Figure 137: Work List – Unassign Selection

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/138.png)

79. Select the checkbox(es) next to the case(s)/document(s) you want to unassign, then select the Unassign button. The item(s) will be removed from the work list.

## Pulling Reports 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with a Supervisor role (apart from DCDM and Appeal Supervisors) can pull reports in the application. To pull a report, follow the steps listed below:

1.  From the sidebar navigation menu, select the Reports option. The Reports tab displays listing the available reports for your user role.

<span id="_Hlk155371869" class="anchor"></span>Figure 138: Report Browser Tab

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/139.png)

80. Select the report type you want to view. The details of the report will display in a new tab.

<span id="_Toc218593923" class="anchor"></span>Figure 139: Report Details Tab

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/140.png)

### Exporting Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DOCMP allows Supervisor users to export report data to a PDF or Excel file. To export a report, follow the steps listed below:

1.  From the sidebar navigation menu, select the Reports option. The Reports tab displays.
2.  Select the report type you want to view. The details of the report will display in a new tab.
3.  From the Actions drop-down menu, select Refresh, Export to PDF, or Export to Excel. The system will automatically download the file in the chosen format (.pdf or .xlsx).

## Working with OHI Certificates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any user with an OHI Voucher Examiner role may self-assign, view, and update OHI certificates in the DOCMP application.

### Self-Assign a Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To self-assign a document, follow the steps listed below.

<span id="_Hlk155856864" class="anchor"></span>Figure 140: OHI Voucher Examiner Dashboard

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/141.png)

1.  From the Dashboard (OHI Voucher Examiner), select the checkbox next to the item in your Work Queue.
81. Select the Assign to Me button. The screen will update with confirmation that an item has been assigned to you.

<span id="_Toc218593925" class="anchor"></span>Figure 141: Self-assign Confirmation

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/142.png)

47. Alternatively, you can select the Get Next Work button which will assign to you the oldest document from the OHI Unassigned Work Queue.

### View and Update OHI Certificates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view and update OHI Certificates, follow the steps listed below:

1.  From the Dashboard (OHI Voucher Examiner) select the Doc Batch Number of the item from the Work List. The details of the selected document will open in a new tab.

<span id="_Toc218593926" class="anchor"></span>Figure 142: OHI Certificate Document Details

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/143.png)

82. The Details section allows users to view additional information about the selected document, and is organized under the following tabs:
83. Document Details
84. Sponsor Information
85. Beneficiary Information
86. Medicare Beneficiaries
87. Other Health Insurance
88. Certification

    Each of these tabs can be selected to view or edit the applicable information for the selected document.
89. Confirm the beneficiary information listed and select and complete the fields in the other tabs as needed.
90. Select the Comments tab to review any comments that may have been added. If there are existing comments, the number of included comments will display next to the tab heading.
4.  Selecting the link displayed under Attachments will allow you to download and view a PDF copy of the full document.
91. When finished, select Save. You will receive confirmation that the document was saved successfully.

<span id="_Toc218593927" class="anchor"></span>Figure 143: OHI Document Save Confirmation

![](delivery-operations-claims-management-platform-docmp-pega-user-guide/144.png)

# Appendix A: Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym     | Definition                                                                |
|-------------|---------------------------------------------------------------------------|
| BCPU    | Beneficiary Claims Processing Unit                                        |
| CHAMPVA | Civilian Health and Medical Program of the Department of Veterans Affairs |
| COR     | Contract Office Representative                                            |
| DOCMP   | Delivery Operations Claims Management Platform                            |
| DCDM    | Document Control and Document Management                                  |
| EEV     | Eligibility, Enrollment, and Verification                                 |
| ESD     | Enterprise Service Desk                                                   |
| FMP     | Foreign Medical Program                                                   |
| HAC     | Health Administration Center                                              |
| OHI     | Office of Health Information                                              |
| OIT     | Office of Information and Technology                                      |
| PDF     | Portable Document Format                                                  |
| PIV     | Personal Identity Verification                                            |
| PM      | Program Manager                                                           |
| PSC     | Program Support Clerk                                                     |
| R&R     | Review and Resolution Department                                          |
| SB      | Spina Bifida                                                              |
| SPC     | Specialty Contact Center                                                  |
| SR      | Service Recovery                                                          |
| SSN     | Social Security Number                                                    |
| URL     | Uniform Resource Locator                                                  |
| VA      | Department of Veterans Affairs                                            |
| VAEC    | VA Enterprise Cloud                                                       |
| VFMP    | Veteran Family Medical Programs                                           |
| VIP     | Veteran-focused Integrated Process                                        |
| VistA   | Veterans Health Information Systems and Technology Architecture           |
| VPN     | Virtual Private Network                                                   |