---
title: Enterprise Program Reporting System (EPRS) User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: Enterprise Program Reporting System (EPRS)
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
  - eprs
  - date
  - span
  - search
  - class
  - table
  - reporting
  - contents
  - contractor
  - guide
page_count: 0
word_count: 14076
section_count: 20
table_count: 2
figure_count: 2
appendix_count: 2
has_toc: False
is_stub: False
pub_date: May 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/eprs_ui_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/eprs_ui_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

---
title: |
  <span id="_Hlk100738314" class="anchor"></span>Enterprise Program Reporting System (EPRS)

  <span id="_Toc52223626" class="anchor"></span>Software Version 1.37

  <span id="_Toc52223627" class="anchor"></span>User Interface User Guide
---

![](enterprise-program-reporting-system-eprs-user-guide/001.png)

May 2023

Office of Information and Technology (OIT)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

<table style="width:100%;">
<caption><p>Table 1. Documentation Symbols and Descriptions</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 46%" />
<col style="width: 23%" />
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
<td>05/12/2023</td>
<td>28.0</td>
<td><p>Software Version 1.37 updates:</p>
<ul>
<li><p>Added Incentive/Disincentive Factor 5 (IDF5) pages, Search and Add.</p></li>
<li><p>Added screenshots and text instructions for IDF5 Add, Search pages, and the Search Results Display</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>03/29/2023</td>
<td>27.0</td>
<td>Document version and date updated. No frontend User Interface changes for Software Version 1.36.</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>02/01/2023</td>
<td>26.0</td>
<td><p>Software Version 1.35 updates:</p>
<ul>
<li><p>Removed fields from the Search, Add, and Edit pages on the Complaints and Congressional Inquiry screens.</p></li>
<li><p>Updated screen captures to reflect field removals and general display changes.</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>12/27/2022</td>
<td>25.0</td>
<td><p>Software Version 1.34 updates:</p>
<ul>
<li><p>Added the Progress Tracking tab to the Search, Add, and Edit pages for Deviations.</p></li>
<li><p>Made the Region field mandatory for the Congressional Inquiries and Complaints Add pages.</p></li>
<li><p>Updates screen captures due to updated UI screen changes.</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>11/10/2022</td>
<td>24.0</td>
<td><p>Software Version 1.33 updates:</p>
<ul>
<li><p>Added Export Data download instructions to the Search pages for Complaints, Congressional Inquiry, Corrective Action Plan, Deviations, Waivers, and Credentialing Audit.</p></li>
<li><p>Updated screen captures due to updated UI screen changes.</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>09/28/2022</td>
<td>23.0</td>
<td><p>Software Version 1.32 updates:</p>
<ul>
<li><p>Updated the Type of Entry drop-down menu to include White House Hotline selection on the Congressional Inquiry Search, Add, and Edit screens.</p></li>
<li><p>Updated screen captures due to field appearance changes.</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>08/30/2022</td>
<td>22.0</td>
<td><p>Software Version 1.31 updates:</p>
<ul>
<li><p>Updated screen captures due to font change.</p></li>
<li><p>Updated Quality Check Search as Region is now multiselect.</p></li>
<li><p>Updated Quality Check screens due to an order change of the Release and Return buttons.</p></li>
<li><p>Updated search result screens as they now include the Rows to Display drop-down menu.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>07/29/2022</td>
<td>21.0</td>
<td><p>Software Version 1.30 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Updated Credentialing Audit screens. Is On LEIE? was updated on the screen.</p></li>
<li><p>Updated CAP and Congressional Inquiry screens for style changes.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>06/17/2022</td>
<td>20.0</td>
<td><p>Software Version 1.29 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Updated Document Upload references to include .ppt and .pptx file types.</p></li>
<li><p>Updated Document Upload screen captures.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>05/18/2022</td>
<td>19.0</td>
<td><p>Software Version 1.28 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Added note for Clear Filters function.</p></li>
<li><p>Updated screens to include deliverable export function.</p></li>
<li><p>Updated Credentialing Audit to include LEIE and DEA Number field.</p></li>
<li><p>Updated Quality Check search screens to include Release and Return buttons</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>04/13/2022</td>
<td>18.0</td>
<td><p>Software Version 1.27 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Updated Deliverable Name drop-down menu to multiselect drop-down list.</p></li>
<li><p>Updated the Edit CCN Corrective Action Plan screen. This screen now includes the History section that displays the name/date the record was created/modified.</p></li>
<li><p>Updated note for Document Upload.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>03/23/2022</td>
<td>17.0</td>
<td><p>Software Version 1.26 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Added QASP Category menu options screen capture in the Deviations section.</p></li>
<li><p>Added Reconsideration checkbox to Add Deviations screen.</p></li>
<li><p>Updated fields and definitions in Deviations section.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>02/23/2022</td>
<td>16.0</td>
<td><p>Software Version 1.25 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Updated the screen for the Decisions and Outcome tab under Edit Deviations.</p></li>
<li><p>Updated the Edit screen for: Complaints, Congressionals, Waivers, and Deviations.</p></li>
<li><p>Added a note stating that when uploading a duplicate document and saving the record, the confirmation pop-up appears after user selects save.</p></li>
<li><p>Added a note stating that when deleting a document and saving the record, the confirmation pop-up appears after user selects save.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>01/19/2022</td>
<td>15.0</td>
<td><p>Software Version 1.24 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Added Document Upload section to Congressional Inquiry screen.</p></li>
<li><p>Updated the Decisions &amp; Outcome tab. Deviations Notification of Outcomes checkboxes enabled.</p></li>
<li><p>Updated Deviations screens to reflect the change to the multi-select fields as they are now drop-down menus.</p></li>
<li><p>Updated CAP screens to reflect the change to the multi-select fields as they are now drop-down menus.</p></li>
<li><p>Updated the Edit Congressional Inquiry screen to include the History section.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>12/08/2021</td>
<td>14.0</td>
<td><p>Software Version 1.22 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Updated CCN Deviations section.</p></li>
<li><p>Updated Notification of Outcome options.</p></li>
<li><p>Performance Objective (PO) 1 Performance Element (PE) 7 – 10 options for Regions 1 – 4 selections were added to the drop-down menu within the CCN Deviations and CAPS UI.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>10/27/2021</td>
<td>13.0</td>
<td><p>Software Version 1.20 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Updated CCN Deviations section.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>09/15/2021</td>
<td>12.0</td>
<td><p>Software Version 1.19 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Updated CCN Complaints section. The screen now displays the Document Upload section.</p></li>
<li><p>Updated CCN Deviations section. The screen now displays the Decisions &amp; Outcome tab.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>08/04/2021</td>
<td>11.0</td>
<td><p>Software Version 1.17 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Updated Waiver section. Added Document Upload section.</p></li>
<li><p>Updated Network Support Credentialing section name to Credentialing Audit.</p></li>
<li><p>Updated CCN Issues section name to CCN Complaints.</p></li>
<li><p>Updated CCN Issues section. Added COR Tracking section to Complaints, Grievances, Appeals, and Disputes pages.</p></li>
<li><p>Updated CCN Congressional Inquiry section. Added COR Tracking section to Congressional and VA Inquires pages.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>06/16/2021</td>
<td>10.0</td>
<td><p>Software Version 1.15 updates:</p>
<ul>
<li><p>Updated screen captures and fields.</p></li>
<li><p>Updated Quality Check section. Region 5 added to Region menu options.</p></li>
<li><p>Updated CCN Issues section. ECAT ID field added to Details section.</p></li>
<li><p>Updated CCN Corrective Action Plans (CAP) section. Added Document Upload section.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>03/31/2021</td>
<td>9.0</td>
<td><ul>
<li><p>Software Version 1.11 updates:</p></li>
<li><p>Updated screen captures.</p></li>
<li><p>Added Network Support Credentialing section.</p></li>
<li><p>Updated order of sections found under 3.3 System Menu.</p></li>
<li><p>Updated order of sections found under 4. Using the Software.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>02/24/2021</td>
<td>8.0</td>
<td><p>Software Version 1.10.3.1 updates:</p>
<ul>
<li><p>Updated screen captures.</p></li>
<li><p>Updated Congressionals section.</p></li>
<li><p>Performed redaction.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>01/13/2021</td>
<td>7.0</td>
<td><p>Software Version 1.10.2.1 updates:</p>
<ul>
<li><p>Updated screen captures.</p></li>
</ul>
<ul>
<li><p>Updated CCN Waivers section.</p></li>
<li><p>Updated CCN Corrective Action Plan (CAP) section.</p></li>
<li><p>Performed redaction.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>11/20/2020</td>
<td>6.0</td>
<td><p>Software Version 1.10.1.0 updates:</p>
<ul>
<li><p>Updated screen captures.</p></li>
</ul>
<ul>
<li><p>Updated Congressionals section.</p></li>
<li><p>Updated Deviations section.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>10/30/2020</td>
<td>5.0</td>
<td><p>Software Version 1.10.0.0 updates:</p>
<ul>
<li><p>Updated screen captures.</p></li>
<li><p>Updated instructions in the Gaining Initial Access to EPRS section.</p></li>
</ul>
<ul>
<li><p>Updated Complaints to CCN Issues.</p></li>
<li><p>Added Region 3 and Region 4 options to Quality Check section.</p></li>
<li><p>Updated Appendix A: Troubleshooting SharePoint UIs screens.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>06/09/2020</td>
<td>4.0</td>
<td><p>Software Version 1.5.0.1 updates:</p>
<ul>
<li><p>Updated screen captures and figure numbers</p></li>
<li><p>Relocated all references to Power BI reports to the Office of Community Care Informatics and Data Analytics Reporting User Guide</p></li>
</ul></td>
<td>Business Team &amp; Business Contractor Support (Guidehouse &amp; ERPi)</td>
</tr>
<tr class="even">
<td>04/01/2020</td>
<td>3.0</td>
<td><p>Software Version 1.3.0.7 updates:</p>
<ul>
<li><p>Updated screen captures</p></li>
<li><p>Added CCN Corrective Action Plan</p></li>
<li><p>Added CCN Deviations</p></li>
<li><p>Added CCN Waivers</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>11/07/2019</td>
<td>2.1</td>
<td><ul>
<li><p>Updated Power BI screen captures</p></li>
<li><p>Updated Power BI steps and instructions</p></li>
</ul></td>
<td>Informatics &amp; Data Analytics (IDA); Business Team Contractor Support (Guidehouse &amp; ERPi)</td>
</tr>
<tr class="even">
<td>10/01/2019</td>
<td>2.0</td>
<td><p>Software Version 1.1.0 updates:</p>
<ul>
<li><p>Updated screen captures.</p></li>
<li><p>Added Quality Check Dashboard content.</p></li>
<li><p>Added User Access Levels information.</p></li>
<li><p>Added Data Flows section information.</p></li>
<li><p>Updated Congressional Inquiry verbiage/screens.</p></li>
<li><p>Included Power BI</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>5/24/2019</td>
<td>1.0</td>
<td>Initial Draft</td>
<td>AbleVets</td>
</tr>
</tbody>
</table>

Table 1. Documentation Symbols and Descriptions

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the User Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as VistA end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

Table of Contents

Table of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the Manual](#organization-of-the-manual)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
- [Getting Started](#getting-started)
  - [Gaining Initial Access to EPRS](#gaining-initial-access-to-eprs)
  - [Logging On](#logging-on)
  - [System Menu](#system-menu)
    - [Navigating EPRS SharePoint](#navigating-eprs-sharepoint)
  - [Exiting the System](#exiting-the-system)
- [Using the Software](#using-the-software)
  - [Quality Check](#quality-check)
    - [Quality Check Search Workflow](#quality-check-search-workflow)
  - [CCN Complaints](#ccn-complaints)
    - [Add Complaints, Grievances, Appeals, and Disputes Workflow](#add-complaints-grievances-appeals-and-disputes-workflow)
    - [Search for Complaints, Grievances, Appeals, and Disputes Workflow](#search-for-complaints-grievances-appeals-and-disputes-workflow)
  - [CCN Congressional Inquiry](#ccn-congressional-inquiry)
    - [Add New Congressional Inquiry Workflow](#add-new-congressional-inquiry-workflow)
    - [Search for Congressional Inquiries Workflow](#search-for-congressional-inquiries-workflow)
  - [CCN Corrective Action Plans (CAP)](#ccn-corrective-action-plans-cap)
    - [Add CCN Corrective Action Plan (CAP) Workflow](#add-ccn-corrective-action-plan-cap-workflow)
    - [Search CCN Corrective Action Plan (CAP) Workflow](#search-ccn-corrective-action-plan-cap-workflow)
  - [CCN Deviations](#ccn-deviations)
    - [Add Deviation Workflow](#add-deviation-workflow)
    - [Search Deviation Workflow](#search-deviation-workflow)
  - [CCN Waivers](#ccn-waivers)
    - [Add Waivers Workflow](#add-waivers-workflow)
    - [Search Waivers Workflow](#search-waivers-workflow)
  - [Credentialing Audit](#credentialing-audit)
    - [Search Credentialing Review Workflow](#search-credentialing-review-workflow)
  - [Incentive/Disincentive Factor 5 (IDF5)](#incentivedisincentive-factor-5-idf5)
    - [Add IDF5 Reporting](#add-idf5-reporting)
    - [Search IDF5 Reporting](#search-idf5-reporting)
- [Appendix A: Troubleshooting SharePoint UIs](#appendix-a-troubleshooting-sharepoint-uis)
- [Appendix B: Acronyms and Abbreviations](#appendix-b-acronyms-and-abbreviations)
The Enterprise Program Reporting System (EPRS) will enable Veterans Health Administration (VHA) leadership, VHA Office of Community Care (OCC) staff, Veterans Integrated Service Network (VISN) leadership, and Department of Veterans Affairs (VA) Medical Center (VAMC) leadership to access program and operational reporting for the Community Care Program (CCP). This access will support contractor accountability and allow for program improvement. EPRS integrates with the Corporate Data Warehouse (CDW) and the Data Access Service (DAS). Through CDW EPRS pulls data elements captured by internal VA IT systems, and through DAS EPRS receives Community Care Network (CCN) Contractor Deliverables. These linkages enable EPRS to generate reports from data gathered across CCP. Data will be imported into EPRS daily for up-to-date reporting.
As enacted by the VA Maintaining Internal Systems and Strengthening Integrated Outside Networks Act of 2018 (MISSION Act) and the implementation of the Community Care Network (CCN), the VA is implementing an integrated, high performing health care network in partnership with community providers to improve Veteran access to care. EPRS has been designed to track and monitor adherence to network adequacy performance objectives.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide simple and comprehensive instructions for using the EPRS User Interface (UI) Screens (developed using SharePoint).

The EPRS SharePoint UI screens enable CCN Administrators to add, edit, and manage key contracting data elements such as Congressional and VA Inquiries and CCN Issues. The UI screens also enable the CCN Administrators to review CCN Contractor Deliverable data for quality, to assess data integrity before either releasing the data for ingestion or rejecting and returning the data to the contractor for correction.

Access to each UI in EPRS is aligned to user roles and responsibilities. Some features included in this User Guide will not be visible or available to all users. Access requests will be routed to the EPRS Product Owner for disposition.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Enterprise Program Reporting System (EPRS) v1.31 User Guide* will provide explanations of all user interface options within the context of an easy-to-understand demonstration data scenario. These interface options are the EPRS SharePoint UI screens.

This document is also designed to provide the user with screen-by-screen “how to” information on the usage of EPRS.

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 1: Introduction

The Introduction section provides the purpose of this manual, an overview of the EPRS software, an overview of the software used, project references, contact information for the user to seek additional information, and an acronyms and abbreviations list for this manual.

Section 2: System Summary

The System Summary section provides a graphical representation of the equipment, communication, and networks used by the system, user access levels, how the software will be accessed, and contingencies and alternative modes of operation.

Section 3: Getting Started

The Getting Started section provides a general walk-through of the system from initiation through exit, enabling the user to understand the sequence and flow of the system.

Section 4: Using the Software

This section gives the user the “how to” information for using EPRS, including many step-by-step procedures.

Appendix A: Troubleshooting SharePoint UIs

This section provides troubleshooting for the EPRS user.

Appendix B: Acronyms and Abbreviations

This section provides a list of acronyms and abbreviations found in this document.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written under the following assumptions of the audience’s experience/skills:

- User has basic knowledge of Microsoft SharePoint.
- User has a working knowledge of the business process supported by the data entry and Quality Check functionality.
- User has been provided the appropriate active roles, menus, and security keys for EPRS, as required per the access criteria developed by Informatics and Data Analytics (IDA).

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are currently no coordination requirements for EPRS.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code (USC) this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material.

| Symbol                                                                                                                                                   | Description                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](enterprise-program-reporting-system-eprs-user-guide/002.png) | CAUTION: Used to caution the reader to take special notice of critical information. |

1.  Notes are used to inform the reader of general information including references to additional reading material.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following resources are maintained by the EPRS Product Owner and the EPRS project team:

- EPRS Solutions SharePoint Site
- EPRS Training Module in Talent Management System
- Community Care National Portal, Operational Guidebook Chapter 10

Questions on business requirements, system access, and other related matters should be directed to the EPRS Project Team.

Questions on technical issues in using the system should be reported as a YourIT Help Desk.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For issues related to EPRS that cannot be resolved by this manual or the site administrator, please contact the National Service Desk.

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Users will access EPRS through their internet browser and secure VPN connection or VA Intranet.
- Users access the EPRS Quality Check interface and contract administration data entry screens through Microsoft SharePoint.
- Access to each UI in EPRS is aligned to user roles and responsibilities. Some features included in this User Guide will not be visible or available to all users. Access requests will be routed to the EPRS Quality Check interface Product Owner for disposition.

Instructions for accessing each portal are detailed in Section 3.

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data from the CCN contractor is transmitted to EPRS via DAS. This information flows through a series of orchestrated web services calls between DAS and EPRS. DAS will conduct a syntactical check of each Deliverable, and upon successful completion the Deliverable will be transmitted to the EPRS Quality Check. Once a data file is received in Quality Check, an automated message will be sent to the designated Business Owners for that Deliverable to notify them that the file is available for review. The Business Owners will be directed to the EPRS Quality Check UI to review the data for completeness and quality. If a Deliverable does not pass this review, the Business Owner will Return the file to the contractor for correction and resubmission. When a Deliverable passes the review, the Business Owner will “Release” the data to the ODS, ready for ETL into DW for EPRS.

EPRS offers a set of user entry screens (hosted by EPRS SharePoint), which enable the user to input data for Accreditation Waivers, Complaints & Grievances, Congressional Inquiries, Corrective Action Plans (CAPs), Network Adequacy Deviations, and Network Support Credentialing Reviews, which are then stored in the EPRS ODS for ETL into the DW.

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2.  Additional user permissions and instructions will be included in this section with future iterations of the document.

There are three EPRS user access levels

- EPRS Members – Edit permission levels. Can view, add, update, and delete list items and documents.
- EPRS Owners – Full Control permission levels. Has full control.
- EPRS Visitors – Read permission levels. Can view pages and list items and download documents.

Access to each report or feature in EPRS is aligned to user roles and responsibilities. Some features included in this User Guide will not be visible or available to all users. Access requests will be routed to the EPRS Product Owner for disposition.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA Enterprise Cloud (VAEC) handles the Continuity of Operations.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the EPRS SharePoint UI and the EPRS Power BI application, from initiation through exit.

## Gaining Initial Access to EPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain access to the EPRS User Interface, the applicant must first complete an Access Form located on the EPRS Solutions SharePoint page. The applicant must also secure their supervisor’s approval and document it on the Access Form. The applicant must then submit the completed form to the CCN Contracting Officer’s Representative (COR) Records Management team for CCN Approval Authority disposition. The CORs will review the form, determine whether to approve or deny the request, and return the signed form to the applicant. If the request is approved, the applicant must then submit a VA Help Desk request via YourIT and attach the completed Access form.

The applicant will be notified via ticket update once access is granted, whereupon the approved user can then access EPRS. Once EPRS access is no longer required for the fulfillment of the user’s responsibilities, the user (or their supervisor) is requested to submit another VA Help Desk request via YourIT, to have their access revoked.

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPRS UI screens for inputting data are accessed through Microsoft SharePoint.

Users with the appropriate access permissions can access ERPS through the EPRS SharePoint site.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Navigating EPRS SharePoint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPRS SharePoint offers seven landing pages: Quality Check, CCN Complaints, CCN Congressional Inquiry, CCN Corrective Action Plan, CCN Deviations, CCN Waivers, and Credentialing Audit.

<span id="_Toc42529453" class="anchor"></span>Figure 1: EPRS Home Page SharePoint Page

![](enterprise-program-reporting-system-eprs-user-guide/003.png)

#### Quality Check

This functionality enables the COR / Business Owners to review contractor deliverables for completeness and compliance with formatting requirements, before releasing the deliverable to the EPRS Operational Data Store (ODS).

<span id="_Toc42529456" class="anchor"></span>Figure 2: Quality Check SharePoint Page

![](enterprise-program-reporting-system-eprs-user-guide/004.png)

#### CCN Complaints

The COR and business owners have responsibility for tracking any formal complaints or grievances filed against CCP or its contractors. This UI screen enables these personnel to create, input, and otherwise administer these formal complaints and grievances.

<span id="_Toc42529454" class="anchor"></span>Figure 3: Complaints, Grievances, Appeals and Disputes SharePoint Page

> ![](enterprise-program-reporting-system-eprs-user-guide/005.png)

#### CCN Congressional Inquiry

The CORs are responsible for managing any Congressional and VA Inquires into the EPRS User Interface (UI) as part of CCP performance. This UI screen enables these personnel to create, update, and administer these inquiries.

<span id="_Toc42529455" class="anchor"></span>Figure 4: Congressional Inquiries SharePoint Page

![](enterprise-program-reporting-system-eprs-user-guide/006.png)

#### CCN Corrective Action Plan

CCN Corrective Action Plan enables the COR to input and administer corrective action plans (CAPs) for CCN contractor regions and their VA medical centers (VAMCs). Each quarter that a facility is included on a CAP counts against the network adequacy score for that facility as well as the aggregate score for its CCN contractor region. This UI enables the COR to input, track, and administer CAPs across a range of performance areas.

<span id="_Toc42529459" class="anchor"></span>Figure 5: Corrective Action Plans SharePoint Page

![](enterprise-program-reporting-system-eprs-user-guide/007.png)

#### CCN Deviations

The CCN Deviations UI enables the COR to input and administer Network Adequacy Deviations for a CCN contractor region. These deviations are granted to exempt a region's network adequacy QASP scores from penalization for network limitations beyond their scope of control. This UI screen enables the COR and Network Management personnel to input and administer these deviations, which are finite in duration.

<span id="_Toc42529458" class="anchor"></span>Figure 6: Deviations SharePoint Page

![](enterprise-program-reporting-system-eprs-user-guide/008.png)

#### CCN Waivers

CCN Waivers enables the COR to input and administer Waivers of Accreditation requirements for a CCN contractor region. These accreditation waivers are applied to provider or facility limitations that might otherwise prevent a provider or facility from providing Veteran care through CCP. This UI screen enables the COR to input or administer these waivers, which are finite in duration.

<span id="_Toc42529457" class="anchor"></span>Figure 7: Waiver SharePoint Page

![](enterprise-program-reporting-system-eprs-user-guide/009.png)

#### Credentialing Audit

The monthly Provider Credentialing Audit Quality Review process provides reasonable assurance providers are licensed and meet the minimum criteria to be part of the CCN provider network.

<span id="_Toc119589571" class="anchor"></span>Figure 8: Credentialing Audit SharePoint Page

![](enterprise-program-reporting-system-eprs-user-guide/010.png)

## Exiting the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To exit the EPRS SharePoint close any tabs that are open, select your name from the upper right corner, and select Sign Out.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPRS provides user functionality for the following items:

- Quality Check
  - Search Quality Check
  - Edit Quality Check
- CCN Complaints
  - Add Complaints, Grievances, Appeals, and Disputes
  - Search Complaints, Grievances, Appeals, and Disputes
  - Edit Complaints, Grievances, Appeals, and Disputes
- CCN Congressional Inquiry
  - Add New Congressional Inquiry
  - Search Congressional Inquiry
  - Edit Congressional Inquiry
- CCN Corrective Action Plan
  - Add New Corrective Action Plan
  - Search Corrective Action Plan
  - Edit Corrective Action Plan
- CCN Deviations
  - Add New CCN Deviations
  - Search CCN Deviations
  - Edit CCN Deviations
- CCN Waivers
  - Add New CCN Waivers
  - Search CCN Waivers
  - Edit CCN Waivers
- Credentialing Audit
  - Search Credentialing Review
  - Edit Credentialing Records Review

## Quality Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Quality Check enables the community care business owner to conduct a spot-audit of CCN contractor data to ensure quality and reliability before releasing the data for ingestion into the EPRS ODS. The ability to view data, return it to the contractor for correction, or release it to make it available for reporting is accessible via the EPRS Quality Check UI.

Data from the CCN contractor is transmitted to EPRS via DAS. This information flows through a series of orchestrated web services calls between DAS and EPRS. DAS will conduct a syntactical check of each deliverable, upon successful completion of which the deliverable will be transmitted to the EPRS quality check. The business owner will be directed to the EPRS Quality Check UI to review the data for completeness and quality. If no action is taken by the fourth business day, the system sends a second notification. The user will search for and select the file to review and determine its accuracy. If there is reason to not accept the file, Return is selected along with a Return Reason. To approve and release the file so that EPRS can intake the data and make it available for reporting, the business owner selects to release the document.

<span id="_Toc119589572" class="anchor"></span>Figure 9: Quality Check Dashboard

![](enterprise-program-reporting-system-eprs-user-guide/011.png)

- Region – the region that the VAMC or contractor is assigned to. The multiselect drop-down menu lists the options available to the specific region’s contractor.
  - Region 1
  - Region 2
  - Region 3
  - Region 4
  - Region 5
- Deliverable Name – Deliverables that the contractor is responsible for.

<span id="_Toc119589573" class="anchor"></span>Figure 10: Deliverable Name Menu Options

> ![](enterprise-program-reporting-system-eprs-user-guide/012.png)

- Frequency – Length of time the deliverable needs to be reported.
  - 30 days after SHCD then monthly
  - 60 days following conclusion of the survey quarter
  - Monthly
  - Quarterly
  - Weekly
- Reporting Period End Date – date for the last day in the reporting period. Field that allows you to input or select the calendar icon to select a date.
- Business Owner – Field to enter the name of the business owner. Name needs to be the Full First and Last Name is logged in the record.
- Status – This is the business owner status that describes whether the report is:
  - Pending
  - Processed
  - Released
  - Returned

### Quality Check Search Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To perform a Quality Check, follow the steps listed below:

- From the EPRS SharePoint page, select Search under Quality Check. The Quality Check Dashboard page displays.

<span id="_Toc119589574" class="anchor"></span>Figure 11: Quality Check Search Dashboard

![](enterprise-program-reporting-system-eprs-user-guide/013.png)

- Region – multiselect drop-down list, select the region(s) of the deliverable.
- Deliverable Name­ – multiselect drop-down list, select the name(s) of the deliverable.
- Frequency – drop-down menu, select the frequency option.
- Reporting Period End Date field to enter or select the end date.
- Business Owner – field to enter the name of the Business Owner.
- Status drop-down menu – select Pending, Processed, Released, or Returned.
- Select Search. The Quality Check results display at the bottom of the window.
3.  To clear the fields and start your search over, select Clear Filters.

<span id="_Toc119589575" class="anchor"></span>Figure 12: Quality Check Search Results

![](enterprise-program-reporting-system-eprs-user-guide/014.png)

- From the search records, select the ID number to view the file for that record.

<span id="_Toc119589576" class="anchor"></span>Figure 13: Quality Check Record (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/015.png)

<span id="_Toc119589577" class="anchor"></span>Figure 14: Quality Check Record (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/016.png)

- Enter the Business Owner name in the field.
- From the Quality Check Dashboard, select Release to release the file so it can then be processed at some point to the ETL to make it available for reporting on or select Return to return the file (and enter a return reason).
4.  Only those with permission levels of EPRS Owner or EPRS Members will have access to Release or Return files.
5.  When a file is returned, nothing happens at that point. EPRS will not send any notifications. When the form is released, the file gets processed, and the data becomes available to ETL for reporting.
- Select Download Data to export the Quality Check information to an Excel file.

## CCN Complaints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section documents the process for responding to and resolving Complaints, Grievances, Appeals, and Disputes against the CCN contractor.

<span id="_Toc119589578" class="anchor"></span>Figure 15: Complaints, Grievances, Appeals, and Disputes Page (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/017.png)

The fields and menus found within the Add, Search, and Edit pages are defined below:

Details Section

- Referral ID
- Urgent Care Number
- Contractor Tracking Number
- ECAT ID
- Issue Type (required field)
  - Appointment Availability of Network Provider
  - Care Coordination
  - Claims
  - Customer Service
  - Eligibility
  - Geoaccesibility of Network Provider
  - Provider Issue
  - Request for Information
- VA Tracking Number
- Type of Entry – The type of complaint submitted.
  - P - Complaints
  - A - Appeals
  - G - Grievances
  - D - Disputes
- QASP Category – The Quality Assurance Surveillance Plan that the complaint falls under.
  - Primary Care
  - General Dentistry
  - General Care
  - Complementary & Integrative HC Services
  - Specialty DentistryDemographics Section:
- CCN Contractor – Contractor the complaint is related to.
  - Optum
  - TriWest
- Region (required field) – VAMC region the complaint is related to.
  - 1
  - 2
  - 3
  - 4
  - 5
- State – Drop-down menu.
- VISN – Veterans Integrated Services Network that the complaint is related to.
- VAMC Station Number/Name – the VA Medical Center (VAMC) name the complaint is related to.

Issue Timeline Section

- Date Received by Contractor (required field) – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Date Contractor Submitted to VA (required field) – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Date Contractor Submits Relevant Background Information to VA – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Date VA Requests Supplemental Information from the Contractor – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Date Contractor Acknowledges Supplemental Information Request – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Date VA Receives Full Written response from CCN Contractor – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Full Written Response Extension Request by CCN Contractor – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Full Written Response VA Contracting Office Approved Extension – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Request for Additional Information

<span id="_Toc119589579" class="anchor"></span>Figure 16: Complaints, Grievances, Appeals, and Disputes Page (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/018.png)

COR Tracking Section

- Issue Subject – Field to enter the type of issue.
- Comments – Field to enter additional comments.
- Document Upload – Allows you to upload files that include pdf, .doc, .docx, .ppt, .pptx, .txt, .xls, .xlsx, .csv, .bmp, .jpg, .jpeg, and .png.

### Add Complaints, Grievances, Appeals, and Disputes Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add/record CCN Complaints, Grievances, Appeals, or Disputes data into EPRS, follow the steps listed below:

- From the EPRS SharePoint page, select Add under CCN Issues. The Add Complaints, Grievances, Appeals, and Disputes page displays.

<span id="_Toc42529460" class="anchor"></span>Figure 17: Add Complaints, Grievances, Appeals, and Disputes Page

![](enterprise-program-reporting-system-eprs-user-guide/019.png)

- In the Details section, enter the Referral ID in the field and then select Populate. The system will auto-populate the QASP Category field within the Details section and the CCN Contractor, Region (required field), State, VISN, and VAMC Station Number/Name fields within the Demographics section.

<span id="_Toc52394491" class="anchor"></span>Figure 18: Add Complaints Auto Populated Fields

![](enterprise-program-reporting-system-eprs-user-guide/020.png)

- Urgent Care Number field – enter the number.
- Contractor Tracking Number field, enter the number.
- ECAT ID field, enter the ID number.
- Issue Type drop-down menu, select Appointment Availability of Network Provider, Care Coordination, Claims, Customer Service, Eligibility, Geoaccessibility of Network Provider, Provider Issue, or Request for Information. *(This is a required field.)*
- VA Tracking Number field, enter the number.
- Type of Entry drop-down menu, select P- Complaints, A- Appeals, G- Grievances, or D- Disputes.

> Issue Timeline Section

- DateReceived by Contractor field, enter the date or select a date using the pop-up calendar. *(This is a required field.)*
- DateReceived by Contractor Submitted to VA field, enter the date. *(This is a required field.)*
- Date Contractor Submits Relevant Background Information to VA field, enter the date.
- Date VA Requests Supplemental Information from Contractor field, enter the date.
- Date Contractor Acknowledges Request for Supplemental Information field, enter the date.
- Date VA Receives Full written response from CCN Contractor field, enter the date.
- Full Written Response Extension Request by CCN Contractor field, enter the date.
- Full Written Response VA Contracting Office Approved Extension field, enter the date.
- Select the Request for Additional Information check box to request additional information.

> COR Tracking Section

- Issue Subject field, enter subject for the issue.
- Comments field, enter any comments pertaining to the issue.
- Document Upload section, upload files that pertain to the Complaint. Accepted file types include .pdf, .doc, .docx, .ppt, .pptx, .txt, .xls, .xlsx, .csv, .bmp, .jpg, .jpeg, and .png.
6.  When uploading a duplicate document and saving the record, a confirmation message displays after the user selects Save. When deleting a document and saving the record, the confirmation message displays after the user selects Save.
- Select Add. A message displays at the top of the page stating that the issue was successfully added. After the issue is successfully saved, the form will clear.

### Search for Complaints, Grievances, Appeals, and Disputes Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To search Complaints, Grievances, Appeals, and Disputes, follow the steps listed below:

- From the EPRS SharePoint page, select Search under CCN Complaints. The Search Complaints, Grievances, Appeals, and Disputes page displays.

<span id="_Toc42529462" class="anchor"></span>Figure 19: Search Complaints, Grievances, Appeals, and Disputes Page (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/021.png)

<span id="_Toc119589583" class="anchor"></span>Figure 20: Search Complaints, Grievances, Appeals, and Disputes Page (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/022.png)

- Details, Demographics, Issue Timeline, and COR Tracking sections – fields to enter your search information.
- Select Search. The Complaints, Grievances, Appeals, and Disputes Search Results display.
7.  To clear the fields and start your search over, select Clear Filters.

<span id="_Toc42529463" class="anchor"></span>Figure 21: Complaints, Grievances, Appeals, and Disputes Search Results

![](enterprise-program-reporting-system-eprs-user-guide/023.png)

- Select Download Data to export the Complaints, Grievances, Appeals, and Disputes information to an Excel file.

#### Edit Complaints, Grievances, Appeals, and Disputes Workflow

Once a search is initiated and displayed from the Complaints, Grievances, Appeals, and Disputes section, you can select the Complaints, Grievances, Appeals, or Disputes to edit the fields. Follow the steps listed below to edit the inquiry:

- From the Complaints search results, select the ID for the Complaint or Grievance you would like to edit. The selected Edit Complaints, Grievances, Appeals, and Disputes page displays.

<span id="_Toc52394494" class="anchor"></span>Figure 22: Edit Complaints, Grievances, Appeals, and Disputes Page

![](enterprise-program-reporting-system-eprs-user-guide/024.png)

- Edit the fields as needed.
- Select Save. The Update was Successful confirmation message displays.

## CCN Congressional Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section allows the CORs to create, update, and administer Congressional and VA Inquires.

<span id="_Toc135215938" class="anchor"></span>Figure 23: Congressional and VA Inquiries Search Fields (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/025.png)

Details Section

- Inquiry ID – field to enter the issue.
- Referral ID
- Urgent Care Number
- QASP Category – select the related Quality Assurance Surveillance Plan.
- Type of Entry – select whether this entry was submitted through Congressionals, VA, or White House Hotline.
- Inquiry Type – select the category that best fits this inquiry.
- Contractor Tracking Number
- VA Tracking Number
- ECAT IDDemographics Section
- Region – select the region where this inquiry originated.
- Veteran Congressional District – field to enter Congressional District of the VA where the inquiry is located.
- CCN Contractor
- VISN
- VAMC Station Number/Name
- State
- VAMC Congressional DistrictCongressional/VA Inquiry Timeline Section
- Date Received by Contractor– the date is in the original inquiry record.
- Date Contractor Submitted to VA – the date is in the original inquiry record.
- Date VA Request Supplemental Information from Contractor
- Date Contractor Acknowledges Request for Supplemental Information
- Date VA Receives Full Written Response from Contractor
- Inquiry Closed Date
  - Request for Additional Information – if needed, check this box to request for more information.
  - Inquiry Closed­ – check this box if the inquiry is closed/resolved.

<span id="_Toc119589586" class="anchor"></span>Figure 24: Congressional and VA Inquiries Search Fields (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/026.png)

COR Tracking Section

- Inquiry Subject
- Closed Report Date
- Check Back
- Check Back Due Date
- Comments

### Add New Congressional Inquiry Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps to add a new Congressional or VA Inquiry into EPRS are noted below.

- From the Congressional Inquiries SharePoint page, select Add. The Add Congressional and VA Inquiries page displays.

<span id="_Toc42529465" class="anchor"></span>Figure 25: Add Congressional and VA Inquires

![](enterprise-program-reporting-system-eprs-user-guide/027.png)

- In the Demographics section, enter the Referral ID in the field and then select Populate. The system will auto-populate the QASP Category within the Details section and Region (required field), CCN Contractor, VISN, VAMC Station Number/Name, State, and VAMC Congressional District fields within the Demographics section. If there is no Referral ID, these fields can be manually entered.

<span id="_Toc42529466" class="anchor"></span>Figure 26: Add Congressional Inquiry – CCN Network Congressionals Auto Populated Fields

![](enterprise-program-reporting-system-eprs-user-guide/028.png)

- Details section – enter the Contractor Tracking Number in the field provided.
- Urgent Care Number field – enter the urgent care number.
- QASP Category drop-down menu – select the QASP category, if not already auto-populated.
- Type of Entry drop-down menu – select C-Congressional Inquiry, V-VA Inquiry, or W-White House Inquiry.
- Inquiry Type drop-down menu – select the type of inquiry.
- Contractor Tracking Number field­ – enter the tracking number.
- VA Tracking Number field – enter the tracking number.
- ECAT ID field – enter the Emergency Care Authorization Tool ID.
- Demographics section – select the Region from the drop-down menu, if not already auto-populated. (*This is a required field.)*
- Veteran Congressional District field – enter the congressional district number.
- CCN Contractor field – enter the CCN, if not already auto-populated.
- From the VISN drop-down menu, select the Veterans Integrated Service Network, if not already auto-populated.
- State field – enter the state for the inquiry, if not already auto-populated.
- VAMC Congressional District field – enter the district information, if not already auto-populated.
- Congressional/VA Inquiry Timeline section – enter the date in the DateReceived by Contractor field or select a date using the pop-up calendar. (*This is a required field.)*
- DateContractor Submitted to VA field – enter the date or select a date using the pop-up calendar. (*This is a required field.)*
- DateVA Requests Supplemental Information from Contractor field – enter the date or select a date using the pop-up calendar.
- DateContractor Acknowledges Request for Supplemental Information field – enter the date or select a date using the pop-up calendar.
- DateVA Receives Full Written Response from Contractor field – enter the date or select a date using the pop-up calendar.
- Inquiry Closed Date field – enter the date or select a date using the pop-up calendar.
  - Select the Request for Additional Information check box to request additional information.
  - Select the Inquiry Closed check box if the inquiry is closed.
- COR Tracking section – enter the subject for the issue in the Inquiry Subject field.

<span id="_Toc119589589" class="anchor"></span>Figure 27: COR Tracking Section

![](enterprise-program-reporting-system-eprs-user-guide/029.png)

- Inquiry Subject
- Closed Report Date field – enter or select the date the report was closed.
- Check Back drop-down menu – select For Closing, For Sending in Closed Report, or No Action Required.
- Check BackDue Date field – enter or select the due date.
- Comments field – enter any comments pertaining to the inquiry.
- Document Upload section – upload files that pertain to the inquiry. Accepted file types include .pdf, .doc, .docx, .ppt, .pptx, .txt, .xls, .xlsx, .csv, .bmp, .jpg, .jpeg, and .png.

<span id="_Toc119589590" class="anchor"></span>Figure 28: Document Upload Section

![](enterprise-program-reporting-system-eprs-user-guide/030.png)

8.  When uploading a duplicate document and saving the record, a confirmation message displays after the user selects Save. When deleting a document and saving the record, the confirmation message displays after the user selects Save.
- Select Add. A message displays at the top of the page stating that the inquiry was successfully added. After the inquiry is successfully saved, the form will clear.

### Search for Congressional Inquiries Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To search Congressional or VA Inquiries, follow the steps listed below:

- From the Congressional Inquiries SharePoint page, select Search. The Search Congressional and VA Inquiries page displays.

<span id="_Toc42529467" class="anchor"></span>Figure 29: Search Congressional and VA Inquiries (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/031.png)

<span id="_Toc119589592" class="anchor"></span>Figure 30: Search Congressional and VA Inquiries (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/032.png)

- Details, Demographics, Congressional VA Inquiry Timeline, and COR Tracking sections, enter the information into the fields you would like to search by.
- Select Search. The Congressional and VA Inquiries Search Results display.
- Select Download Data to export the Congressional and VA Inquiries information to an Excel file.
9.  To clear the fields and start your search over, select Clear Filters.<span id="_Toc52394498" class="anchor"></span>

Figure 31: Congressional and VA Inquiries Search Results

![](enterprise-program-reporting-system-eprs-user-guide/033.png)

#### Edit Congressional Inquiry Workflow

Once a search is initiated and displayed from the Congressional section, you can select the inquiry to edit the fields. Follow the steps listed below to edit the inquiry:

- From the Congressional and VA Inquiries search results, select the ID for the inquiry you would like to edit. The selected inquiry displays in the Edit Congressional and VA Inquiries window.

<span id="_Toc52394499" class="anchor"></span>Figure 32: Edit Congressional and VA Inquiries (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/034.png)

<span id="_Toc119589595" class="anchor"></span>Figure 33: Edit Congressional and VA Inquiries (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/035.png)

- Edit the fields as needed.
- Select Save. The Update was Successful confirmation message displays.

## CCN Corrective Action Plans (CAP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This functionality enables the COR to input and administer CAPs for CCN contractor regions and their VAMCs. Each quarter that a facility is included on a CAP counts against the Network Adequacy score for that facility as well as the aggregate score for its CCN contractor region. This UI enables the COR to input, track, and administer CAPs across a range of performance areas.

<span id="_Toc119589596" class="anchor"></span>Figure 34: Add CCN Corrective Action Plan (CAP) Page (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/036.png)

The fields and menus found within the CAP Add, Search, and Edit pages are defined below:

CAP Assessed Time Period section:

- Quarter – Drop-down menu that allows the user to select the quarter. This is a required field.
  - First (Oct. – Dec.)
  - Second (Jan. – Mar.)
  - Third (Apr. – Jun.)
  - Fourth (Jul. – Sep.)
- Fiscal Year – Drop-down menu that allows the user to select the year. This is a required field.

CAP Assessed Location section:

- Region – Select the region that the contractor and VAMC(s) listed in the CAP is located in. Selecting a region will auto-populate the contractor name. It will also filter the VISN and VAMC to those assigned to the region.
  - 1
  - 2
  - 3
  - 4
  - 5
- Contractor Name – will auto populate after the region value is selected. Optum or TriWest.
- VISN – the Veterans Integrated Services Networks that the CAP applies to.
- VAMC Station Number/Name – VAMC station the CAP applies to.

<span id="_Toc119589597" class="anchor"></span>Figure 35: Add CCN Corrective Action Plan (CAP) Page (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/037.png)

CAP Information section:

- Performance Objective/Contract Requirement – This will be populated by options that is available to the region you select earlier. Performance objectives are conditions the contractor must meet to stay compliant with VA’s specifications.
- Performance Element/Contract Requirement Subsection
- Contractor CAP Submission Date – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- CAP Start Date
- Target Performance Date – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Actual Performance – Deficiency Percentage
- ThresholdPercentage – This auto populates based on the percentage you record in the Actual Performance – Deficiency Percentage field. It can vary from Marginal to Good
- Status
- COR Signature
- COR Signature Date – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Document Upload – Allows you to upload files that include pdf, .doc, .docx, .ppt, .pptx, .txt, .xls, .xlsx, .csv, .bmp, .jpg, .jpeg, and .png.

### Add CCN Corrective Action Plan (CAP) Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add/record CCN Corrective Action Plan (CAP) into EPRS, follow the steps listed below:

- From the EPRS SharePoint page, select Add under CCN Corrective Action Plan. The Add CCN Corrective Action Plan (CAP) page displays.

<span id="_Toc52394515" class="anchor"></span>Figure 36: Add Corrective Action Plan (CAP) Page

![](enterprise-program-reporting-system-eprs-user-guide/038.png)

10. Fields marked with an asterisk (\*) are required,

CAP Assessed Time Period

- Quarter drop-down menu – select First (Oct.-Dec.), Second (Jan.-Mar.), Third (Apr.-Jun.), or Fourth (Jul.-Sep.). (*This is a required field.)*
- Fiscal Year drop-down menu – select the year. (*This is a required field.)*CAP Assessed Location
- Region drop-down menu, select the region for the CAP. (*This is a required field.)*
- The Contractor Name field is auto populated based on the region selection made.
- VISN field – select the VISN from the list of options. Hold down the Ctrl key to select multiple values.
- VAMC Station Number/Name – select the station number/name for the CAP. Hold down the Ctrl key to select multiple values. (*This is a required field.)*CAP Information
- Performance Objective/Contract Requirement drop-down menu, select the objective for the CAP. You must select a region prior to making a selection. (*This is a required field.)*
- Performance Element/Contract Requirement Subsection drop-down menu – select the requirement.
- Contractor CAP Submission Date field – enter/select the date. (*This is a required field.)*
- CAP Start Date field – enter the start date. (*This is a required field.)*
- Target Performance Date field – enter the target date. (*This is a required field.)*
- Actual Performance-Deficiency Percentage field – enter the percentage.
- The Threshold Percentage field is auto populated based on the Actual Performance-Deficiency Percentage selection made.
- The Status field is auto populated with a status of Active when a new CAP record is added.
- COR Signature field – the COR will enter their signature. (*This is a required field.)*
- The COR Signature Date field is auto populated once a value is entered and saved in the COR Signature field. (*This is a required field.)*

> Document Upload section – upload files that pertain to the CAP. Accepted file types include .pdf, .doc, .docx, .ppt, .pptx, .txt, .xls, .xlsx, .csv, .bmp, .jpg, .jpeg, and .png.

11. When uploading a duplicate document and saving the record, a confirmation message displays after the user selects Save. When deleting a document and saving the record, the confirmation message displays after the user selects Save.
- Select Add. A message displays at the top of the page stating that it was successfully added.

### Search CCN Corrective Action Plan (CAP) Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To search CCN Corrective Action Plans, follow the steps listed below:

- From the CCN Corrective Action Plan SharePoint page, select Search. The Search Waiver page displays.

<span id="_Toc52394517" class="anchor"></span>Figure 37: Search Corrective Action Plan Page (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/039.png)

CAP Assessed Time Period section – enter the information into the fields you would like to search by.

CAP Assessed Location section – enter the information into the fields you would like to search by.

<span id="_Toc52395635" class="anchor"></span>Figure 38: Search Corrective Action Plan (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/040.png)

CAP Information section – enter the information into the fields you would like to search by.

Select Search. The CCN Corrective Action Plan search results display at the bottom of the window.

Select Download Data to export the CCN Corrective Action Plan information to an Excel file.

12. To clear the fields and start your search over, select Clear Filters.

<span id="_Toc52395636" class="anchor"></span>Figure 39: Corrective Action Plan Search Results

![](enterprise-program-reporting-system-eprs-user-guide/041.png)

#### Edit CCN Corrective Action Plan (CAP) Workflow

Once a search is initiated and displayed from the CCN Corrective Action Plan section, you can select the Waiver to edit the fields. Follow the steps listed below to edit the inquiry:

- From the CCN Corrective Action Plan search results, select the ID for the inquiry you would like to edit. The selected inquiry displays in the Edit CCN Corrective Action Plan window.

<span id="_Toc52394520" class="anchor"></span>Figure 40: Edit CCN Corrective Action Plan (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/042.png)

<span id="_Toc119589603" class="anchor"></span>Figure 41: Edit CCN Corrective Action Plan (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/043.png)

- Edit the fields as needed.
- Select Save. The Update was Successful confirmation message displays.

## CCN Deviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This functionality enables the COR to input and administer Deviations for a CCN contractor region. These deviations are granted to exempt a region’s QASP scores and other contract requirement(s) from penalization for limitations beyond their scope of control. This User Interface (UI) screen enables the COR to input and administer these deviations, which are finite in duration.

<span id="_Toc119589604" class="anchor"></span>Figure 42: CCN Deviations (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/044.png)

The fields and menus found within the CCN Deviations Search page are defined below:

- Request Details Section
  - Deviation ID – ID that is automatically created by EPRS after a Deviation is recorded.
  - CCN Contractor Request Date – Date on the Deviation request form.
  - Region – Region location for the Deviation. Selecting a region will auto-populate the CCN contractor field. It will also filter the VAMC and performance objective to those assigned to the region and contractor.
    - 1
    - 2
    - 3
    - 4
    - 5
  - CCN Contractor
    - Optum
    - TriWest
  - VAMC Station Number/Name – VAMC the deviation request applies to.
  - County(ies) – County or counties the deviation request applies to. This is often based on the VAMC selected.
  - Performance Objective /Contract Requirement – The performance objectives that the contractors are obligated to achieve based on their contract.
  - Performance Element/Contract Requirement Subsection – Subsection of performance objective/contract requirement.
  - Associated SEOC – Standard Episodes of Care associated with the deviation request.
  - Taxonomy Code – Taxonomy code associated with the deviation request you are recording.
  - Specialty – Specialty service associated with the deviation request.
  - QASP Category – List of Quality Assurance Surveillance Plan categories.

<span id="_Toc119589605" class="anchor"></span>Figure 43: QASP Category Menu Options

![](enterprise-program-reporting-system-eprs-user-guide/045.png)

- Resubmission – Checkbox. When a COR sees a discrepancy or invalid data in a deviation document sent from a contractor, they will ask for corrections. A resubmission document contains the corrected information from the provider.
- Reconsideration – Checkbox. When a COR does not approve a deviation, they will return it and notify the contractor. The contractor may send a document requesting a reconsideration with detailed information on why the initial document should be acceptable.
- Associated Deviation ID – ID for associated deviation.

<span id="_Toc119589606" class="anchor"></span>Figure 44: CCN Deviations (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/046.png)

- Decisions & Outcome Section
  - Network Adequacy Recommendation
  - Network Adequacy Signature
  - COR Recommendation
  - COR Signature
  - CO Decision
  - CO Decision Date – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Approved Deviation Details Section
  - Approval Date – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
  - Start Date for PMR – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
  - Next Review Date – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
  - Expiration Date – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
- Progress Tracking Section
  - Date Received from Network Support – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
  - Date Sent to SAC – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
  - Checkback Date to SAC – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
  - Date Received from SAC – Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.

### Add Deviation Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add/record Network Adequacy Deviations into EPRS, follow the steps listed below:

- From the EPRS SharePoint page, select Add under CCN Deviations. The Add Deviation page displays.

<span id="_Toc52394508" class="anchor"></span>Figure 45: Add Deviations Page

![](enterprise-program-reporting-system-eprs-user-guide/047.png)

13. Fields marked with an asterisk (\*) are required,

In the Request Details section, enter the CCN Contractor Request Date found on the Deviation request form. (*This is a required field.)*

From the Region drop-down menu, select Region 1, 2, 3, 4, or 5. Selecting a Region will auto-populate the CCN contractor field. It will also filter the VAMC and performance objective to those assigned to the region and contractor. (*This is a required field.)*

The CCN Contractor field is auto-populated from the region selection. Verify that the selection of Optum or TriWest is correct. (*This is a required field.)*

From the VAMC Station Number / Name drop-down menu, select VAMC(s) the deviation request applies to.

From the County(ies) drop-down menu, select the county or counties that the deviation request applies to. This is often based on the VAMC selected.

From the Performance Objective / Contract Requirement drop-down menu, select the performance objectives that the contractors are obligated to achieve based on their contract.

From the Performance Element / Contract Requirement Subsection drop-down menu, select the subsection of performance objective / contract requirement.

From the Associated SEOC drop-down menu, select the Standard Episodes of Care associated with the deviation request.

From the Taxonomy Code drop-down menu, select the taxonomy code associated with the deviation request you are recording.

From the Specialty drop-down menu, select the specialty service associated with the deviation request.

From the QASP Category drop-down menu, select the Quality Assurance Surveillance Plan category associated with the deviation request.

Select the Resubmission checkbox to confirm that the deviation request needed to be resubmitted.

Select the Reconsideration checkbox to confirm a request for reconsideration.

In the Associated Deviation ID field, enter the ID for associated deviation.

Select the Rationale tab.

<span id="_Toc119589608" class="anchor"></span>Figure 46: Rationale Tab

![](enterprise-program-reporting-system-eprs-user-guide/048.png)

Select if the contractor attested to review.

Select if the contractor identified new providers.

Select if the contractor found providers outside of the standards.

In the Source of Research fields, enter the sources used.

In the Other section, enter additional comments.

Select the Justification tab.

<span id="_Toc52394510" class="anchor"></span>Figure 47: Justification Tab

![](enterprise-program-reporting-system-eprs-user-guide/049.png)

In the Justification for Deviation field, enter a detailed explanation.

Under the Non-Contracted Providers section, select if No other Providers Available or Separate file of Providers Attached.

In the Provider / Facility Name field enter the provider / facility name.

Enter the number in the NPI# field.

Enter the street address for the provider.

Enter the city in the Provider City field.

From the State drop-down menu, select the state.

Enter the zip code in the Provider Zip Code field.

Enter the phone number for the provider in the Provider Phone Number field.

In the Reason for Not Contracting field, enter a reason.

In the Additional Notes field, enter additional comments.

Select the Resolution tab.

<span id="_Toc119589610" class="anchor"></span>Figure 48: Resolution Tab

![](enterprise-program-reporting-system-eprs-user-guide/050.png)

In the Contractor POC field, enter the name of the contractor point of contact. (*This is a required field.)*

In the Phone field, enter the phone number for the contractor point of contact. (*This is a required field.)*

In the Extension field, enter the phone extension for the contractor point of contact.

In the Email field, enter the email address for the contractor point of contact. (*This is a required field.)*

In the Resolution Plan field, enter a detailed resolution plan. (*This is a required field.)*

Select the Internal Review tab.

<span id="_Toc119589611" class="anchor"></span>Figure 49: Internal Review Tab

![](enterprise-program-reporting-system-eprs-user-guide/051.png)

Enter comments in the VA Comments field.

Select the Decisions & Outcome tab.

<span id="_Toc119589612" class="anchor"></span>Figure 50: Decisions & Outcome Tab

![](enterprise-program-reporting-system-eprs-user-guide/052.png)

14. The Decisions & Outcome tab should only be completed while editing the deviation within the Edit Deviation section. The Decisions & Outcome fields will only be completed by the Network Adequacy group, COR, or CO. For additional information on completing this tab, please see section 4.5.2.1 Edit Deviation.

<span id="_Toc135215966" class="anchor"></span>Figure 51: Progress Tracking Tab

![](enterprise-program-reporting-system-eprs-user-guide/053.png)

Enter date received from the Network Support focal in the Date Received from Network Support field.

Enter date sent to SAC in the Date Sent to SAC field.

Enter date received from SAC in the Date Received from SAC field.

<span id="_Toc135215967" class="anchor"></span>Figure 52: Upload Document Section

![](enterprise-program-reporting-system-eprs-user-guide/054.png)

In the Document Upload section, upload files that pertain to the deviation. Accepted file types include .pdf, .doc, .docx, .ppt, .pptx, .txt, .xls, .xlsx, .csv, .bmp, .jpg, .jpeg, and .png.

15. When uploading a duplicate document and saving the record, a confirmation message displays after the user selects Save. When deleting a document and saving the record, the confirmation message displays after the user selects Save.

Select Add. A message displays at the top of the page stating that it was successfully added.

### Search Deviation Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To search deviations, follow the steps listed below:

- From the Deviation SharePoint page, select Search. The Search Deviation page displays.

<span id="_Toc52394511" class="anchor"></span>Figure 53: Search Deviations Page (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/055.png)

<span id="_Toc119589615" class="anchor"></span>Figure 54: Search Deviations Page (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/056.png)

In the Request Details, Decisions & Outcomes, and Approved Deviation Details sections, enter the information into the fields you would like to search by.

Select Search. The Deviation Search Results display at the bottom of the window.

Select Download Data to export the Deviation Search Results information to an Excel file.

16. To clear the fields and start your search over, select Clear Filters.

<span id="_Toc52395630" class="anchor"></span>Figure 55: Deviation Search Results

![](enterprise-program-reporting-system-eprs-user-guide/057.png)

#### Edit Deviation Workflow

Once a search is initiated and displayed from the Deviation section, you can select the deviation to edit the fields. Follow the steps listed below to edit the inquiry:

- From the deviation search results, select the ID for the inquiry you would like to edit. The selected inquiry displays in the Edit Deviation window.

<span id="_Toc52394514" class="anchor"></span>Figure 56: Edit Deviation (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/058.png)

<span id="_Toc119589618" class="anchor"></span>Figure 57: Edit Deviation (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/059.png)

Edit the fields as needed.

Select the Decisions & Outcome tab. This tab is broken down into three sections and will need to be completed by the appropriate group for that section: Network Adequacy, COR, or CO.

<span id="_Toc119589619" class="anchor"></span>Figure 58: Decisions & Outcome Tab

![](enterprise-program-reporting-system-eprs-user-guide/060.png)

In the Network Adequacy Only section, select Approved or Not Approved from the Network AdequacyRecommendations drop-down menu. *Completed by the Network Adequacy team.*

In the Network Adequacy Signature field, the Network Adequacy business owner will enter their signature. *Completed by the Network Adequacy team.*

In the Approval Date field, enter or select the approval date. *Completed by the Network Adequacy team.*

In the Start Date for PMR field, enter or select the start date. *Completed by the Network Adequacy team.*

In the Next Review Date field, enter or select the date for the next review. *Completed by the Network Adequacy team.*

In the Expiration Date field, enter or select the expiration date. *Completed by the Network Adequacy team.*

In the Date VAMC Note Sent field, enter or select the date the notice was manually sent to the VAMC. *Completed by the Network Adequacy team.*

In the CO Only section, select Approved or Not Approved from the CO Decision drop-down menu. *Completed by the CO.*

In the CO Decision Date field, enter or select the decision date. *Completed by the CO.*

In the COR Only section, select Approved or Not Approved from the COR Recommendation drop-down menu. *Completed by the COR.*

In the COR Signature field, the COR will enter their signature. *Completed by the COR.*

From the Notification of Outcome section, select one or more of the options: Clinical Integration, Network Support, Regional PM. *Completed by the COR.*

17. Depending on the options selected, an email will be automatically sent out to the Clinical Integration, Network Support, or Regional PM groups.

Select Save. The Update was Successful confirmation message displays.<span id="_Toc52223671" class="anchor"></span>

Figure 59: Progress Tracking Tab

![](enterprise-program-reporting-system-eprs-user-guide/061.png)

In the Date Received from Network Support field, enter or select the date the notice was manually received from Network Support. *Completed by the COR.*

In the Date Sent to SAC field, enter or select the date the notice was manually sent to SAC. *Completed by the COR.*

The Checkback Date to SAC is auto-populated as the Date Sent to SAC entry + 10 business days.

In the Date Received from SAC field, enter or select the date the notice was manually received from SAC. *Completed by the COR.*

## CCN Waivers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This functionality enables the COR to input and administer Waivers of Credentialing and Accreditation requirements for a CCN contractor Region. These Waivers are applied to provider or facility limitations that might otherwise prevent a provider or facility from providing Veteran care through CCP. This UI screen enables the COR to input or administer these waivers, which are finite in duration.

<span id="_Toc119589620" class="anchor"></span>Figure 60: CCN Waiver (1 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/062.png)

The fields and menus found within the CCN Search Waivers page are defined below:

- Waiver ID – This ID is automatically created by EPRS after a Waiver is recorded (Every workflow such as CAPs, complaints, etc., should have an ID on the search page and Edit page that was created by EPRS)
- VAMC Station Number – VAMC(s) that the waiver request applies to.

<span id="_Toc119589621" class="anchor"></span>Figure 61: CCN Waiver (2 of 2)

![](enterprise-program-reporting-system-eprs-user-guide/063.png)

- Region – The CCN region the waiver request applies to. Selecting a Region will filter the VAMC and CCN Contractor form fields on the page.
- State – The state the waiver applies to.
- CCN Contractor – The contractor that requested the waiver. If on the Add page, it’s automatically selected for user.
- Provider/Organization Name
- Service/Provider Type
- Impact Category
- VISN – This is filtered by the region you select. Select the VISNs listed in the waiver request.
- Waiver Request Date – Field to enter date.
- Waiver Approved Date – Field to enter date.
- Waiver Effective Date – Field to enter date.
- Waiver Review Date – Field to enter date.
- Waiver Expiration Date – Field to enter date.
- Waiver Status – Drop-down menu to select Status option.

### Add Waivers Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add/record waivers into EPRS, follow the steps listed below:

- From the EPRS SharePoint page, select Add under CCN Waivers. The Add Waiver page displays.

<span id="_Toc52394500" class="anchor"></span>Figure 62: Add Waiver Page

![](enterprise-program-reporting-system-eprs-user-guide/064.png)

18. Fields marked with an asterisk (\*) are required.

In the Demographics section, from the Region drop-down menu, select the region number. (*This is a required field.)*

The CCN Contractor field is auto populated based on the Region selection made.

From the VAMC Station Number/Name field, select the station number/name. (*This is a required field.)*

The State field is auto populated based on the VAMC Station selection made.

From the Service / Provider Type drop-down menu, select the service / provider type from the list of options.

From the VISN field, select the VISN from the list of options.

In the Provider / OrganizationName field, enter the name for the provider / organization. (*This is a required field.)*

Select the Justification tab.

<span id="_Toc52394501" class="anchor"></span>Figure 63: Justification Tab

![](enterprise-program-reporting-system-eprs-user-guide/065.png)

In the Why are you unable to get accreditation? field, enter a detailed reason what is preventing the requestor from obtaining accreditation. (*This is a required field.)*

In the What are your proposed alternative accreditation / qualification standards? field, enter a detailed proposed alternative. (*This is a required field.)*

In the How will you assure the Veteran will receive a similar standard of quality? field, enter a detailed explanation. (*This is a required field.)*

Select the Impact Statement tab.

<span id="_Toc52394502" class="anchor"></span>Figure 64: Impact Statement Tab

![](enterprise-program-reporting-system-eprs-user-guide/066.png)

From the Impact Category drop-down menu, select the Rurality, Accessibility, or Patient Care.

In the What is the potential impact to Veteran? field, enter a detailed explanation of the potential impact the Veteran might experience. (*This is a required field.)*

In the What is the potential impact to Network Accreditation? field, enter a detailed explanation of the potential impact to Network Accreditation. (*This is a required field.)*

Select the Duration of Waiver Request tab.

<span id="_Toc52394503" class="anchor"></span>Figure 65: Duration of Waiver Request Tab

![](enterprise-program-reporting-system-eprs-user-guide/067.png)

In the Waiver Request Date field, enter / select the date the waiver was requested. (*This is a required field.)*

In the Waiver Approved Date field, if the waiver was approved by the time you are entering this record, enter / select the date the waiver was approved.

In the Waiver Effective Date field, if the waiver was approved by the time you are entering this record, enter / select the date the waiver took effect.

In the Length of Waiver in Days field, the system will calculate the number of days the waiver is in effect. The number will update after saving the record and refreshing the page.

In the Waiver Review Date (Prior to Expiration Date) field, enter / select the date the waiver was reviewed.

In the Waiver Expiration Date field, enter / select the date the waiver expires.

From the Waiver Status drop-down menu, select Approved, Expired, Pending, or Rejected for the status.

In the Duration until Waiver Expiration in Days field, the system will calculate the number of days until the waiver expires. The number will update after saving the record and refreshing the page.

Select the Legal / Contractual Impact tab.

<span id="_Toc52394504" class="anchor"></span>Figure 66: Legal/Contractual Impact Tab

![](enterprise-program-reporting-system-eprs-user-guide/068.png)

In the List any effects on contractual and clinical standards, business requirements, contractual legal reviews, etc. field, enter a detailed list. (*This is a required field.)*

In the List any areas that still meet credentialing requirements, specific to type of institution, group, or agency not being waived in this process field, enter a detailed list. (*This is a required field.)*

<span id="_Toc119589627" class="anchor"></span>Figure 67: Add Waiver Document Upload Section

![](enterprise-program-reporting-system-eprs-user-guide/069.png)

In the Document Upload section, upload files that pertain to the waiver. Accepted file types include .pdf, .doc, .docx, .ppt, .pptx, .txt, .xls, .xlsx, .csv, .bmp, .jpg, .jpeg, and .png.

19. When uploading a duplicate document and saving the record, a confirmation message displays after the user selects Save. When deleting a document and saving the record, the confirmation message displays after the user selects Save.

Select Add. A message displays at the top of the page stating it was successfully added.

### Search Waivers Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To search Waivers, follow the steps listed below:

- From the WaiverSharePoint page, select Search. The Search Waiver page displays.

<span id="_Toc52394505" class="anchor"></span>Figure 68: Search Waiver Page

![](enterprise-program-reporting-system-eprs-user-guide/070.png)

In the Demographics section, enter the information into the fields you would like to search by.

Select Search. The Waiver Search Results display at the bottom of the window.

Select Download Data to export the Waiver Search Results information to an Excel file.

20. To clear the fields and start your search over, select Clear Filters.

<span id="_Toc52394506" class="anchor"></span>Figure 69: Waiver Search Results

![](enterprise-program-reporting-system-eprs-user-guide/071.png)

#### Edit Waivers Workflow

Once a search is initiated and displayed from the waivers section, you can select the waiver to edit the fields. Follow the steps listed below to edit the inquiry:

- From the WaiversSearch Results, select the ID for the inquiry you would like to edit. The selected inquiry displays in the Edit Waiver window.

<span id="_Toc52394507" class="anchor"></span>Figure 70: Edit Waiver

![](enterprise-program-reporting-system-eprs-user-guide/072.png)

Edit the fields as needed.

Select Save. The Update was Successful confirmation message displays.

## Credentialing Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The monthly Provider Credentialing Audit Quality Review process provides reasonable assurance providers are licensed and meet the minimum criteria to be part of the CCN provider network.

<span id="_Toc119589631" class="anchor"></span>Figure 71: Credentialing Audit Search Fields

![](enterprise-program-reporting-system-eprs-user-guide/073.png)

<span id="_Toc119589632" class="anchor"></span>Figure 72: Credentialing Records Review Fields

![](enterprise-program-reporting-system-eprs-user-guide/074.png)

The fields and menus found within the Credentialing Audit Search and Credentialing Records Review page are defined below:

- Review Time Period – Information about the audit report's date. Reports are pulled monthly.
  - Review Fiscal Year – Drop-down menu of fiscal year options.
  - Review Quarter – Drop-down menu. Fiscal quarter options: 1, 2, 3, 4.
  - Review Month – Drop-down menu of calendar month options.
- Provider Location – The provider’s location should correspond to the location recorded in the NPI Registry.
  - Region - Drop-down menu. Region options: 1, 2, 3, 4, and 5.
  - State - Drop-down menu of state options.
  - City - Drop-down menu of city options.
  - Zip - Field to enter the zip code.
  - NPI - National Provider Identifier (NPI) record number.
- Provider Information – The following information needs to be verified by reviewing the provider’s Provider Profile Management System (PPMS) licensing information and NPI Registry information.
  - Provide Type - Drop-down menu of provider type options.
  - Provider Name - Drop-down menu of provider options.
  - Specialty - Drop-down menu of specialty service options.
  - Date Pulled for PPMS Providers - The date that EPRS retrieved the data to create this report. Field where the user enters the date in the format MM/DD/YYYY manually or selects the date from the calendar field.
  - Review Status – Drop-down menu options:
    - Incomplete
    - Primary Complete
    - Secondary Complete
  - License Number – Field to enter the license number.
  - Licensed State – Drop-down menu of specialty state options.
- Document Review – *Credentialing Records Review page only section.*
  - DEA Number – *Credentialing Records Reviewpage only field*. A DEA Registration Number is a unique identifier provided by the Drug Enforcement Agency to medical practitioners like pharmacists, nurse practitioners, doctors, dentists, etc., allowing them to prescribe, dispense and administer drugs defined to be Controlled Dangerous Substances.
  - Is On LEIE? – *Credentialing Records Review page only field*. The Office of Inspector General's List of Excluded Individuals/Entities (LEIE) provides information to the health care industry, patients and the public regarding individuals and entities currently excluded from participation in Medicare, Medicaid, and all other federal health care programs.
- Primary Review – *Credentialing Records Review page only section.*
  - DEA Status – Drop-down menu with list of options:
    - Incomplete
    - N/A
    - Pass
    - Fail
  - State Licensed – Drop-down menu with list of options:
    - Incomplete
    - N/A
    - Pass
    - Fail

### Search Credentialing Review Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To search monthly Provider Credentialing Audit Quality Reviews, follow the steps listed below:

- From the Credentialing Audit page, select Search. The Credentialing Review Search page displays.

<span id="_Toc119589633" class="anchor"></span>Figure 73: Credentialing Review Search Page

![](enterprise-program-reporting-system-eprs-user-guide/075.png)

In the Review Time Period section, enter the information into the fields you would like to search by.

In the Provider Location section, enter the information into the fields you would like to search by.

In the Provider Information section, enter the information into the fields you would like to search by.

Select Search. The Credentialing Review search results display at the bottom of the window.

Select Download Data to export the Credentialing Review information to an Excel file.

21. To clear the fields and start your search over, select Clear Filters.

<span id="_Toc119589634" class="anchor"></span>Figure 74: Credentialing Review Search Results

![](enterprise-program-reporting-system-eprs-user-guide/076.png)

#### Edit Credentialing Records Review Workflow

Once a search is initiated and displayed from the Credentialing Review section, you can select the record to edit the fields. Follow the steps listed below to edit the record:

- From the Credentialing Review Search Results, select the ID for the record you would like to edit. The selected record displays in the Edit Credentialing Records Review page.

<span id="_Toc119589635" class="anchor"></span>Figure 75: Edit Credentialing Records Review

![](enterprise-program-reporting-system-eprs-user-guide/077.png)

- Edit the fields in the Document Review, Primary Review, Secondary Review, and Comments sections as needed.
- Select Submit. The Update was Successful confirmation message displays.

## Incentive/Disincentive Factor 5 (IDF5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Incentive/Disincentive Factor 5 (IDF5) (Improper Payments and Elimination Recovery Act (IPERA) Adjudication and Payment Rules) will result in a percentage of the universe of healthcare claims submitted which accurately conform to the contracted rates. This will be calculated by using an independent third-party auditor who will audit quarterly to determine accuracy of payments to reduce improper payments. The auditor will provide VA and the contractor the quarterly statistical projection of improper payment and accuracy of payments. These performance thresholds will be negotiated on an annual basis to allow for continuous improvement on the reduction of improper payments.

### Add IDF5 Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add IDF5 records into EPRS, follow the instructions below.

<span id="_Toc135215991" class="anchor"></span>Figure 76: IDF5 Add Fields

![](enterprise-program-reporting-system-eprs-user-guide/078.png)

- Region – Drop-down menu with list of options. Select a Region: 1, 2, 3, 4 or 5.
- Quarter – Drop-down menu with list of options. Select a Quarter:
  - First (Oct. – Dec.)
  - Second (Jan. – Mar.)
  - Third (Apr. – Jun.)
  - Fourth (Jul. – Sep.)
- Audit Report Type: – Drop-down menu with applicable options populated based on user input to the Region field. Select the appropriate Audit Report Type: Annual or Quarterly.
22. If user selects Regions 1, 2, or 3 the following options will populate:  
    - Independent Audit Quarterly Report (1-3)  
    - Independent Audit Annual Statistical Projection of Improper Payments Report (1-3)  
    If user selects Regions 4 or 5, the following options will populate:  
    - Independent Audit Quarterly Report (4/5)  
    - Independent Audit Annual Report (4/5)
- CCN Contractor – Enter the CCN Contractor Name.
- Fiscal Year – Drop-down menu with list of options. Select Fiscal Year: 2018, 2019, 2020, 2021, 2022, 2023.
- Annual Error Rate or Quarterly Error Rate – this field will display based on the user’s selection from the Audit Report Type options. Enter the Annual or Quarterly Error Rate in Percentage form.

In the Document Upload section, upload files that pertain to the record if needed. Accepted file types include .pdf, .doc, .docx, .ppt, .pptx, .txt, .xls, .xlsx, .csv, .bmp, .jpg, .jpeg, and .png.

23. When uploading a duplicate document and saving the record, a confirmation message displays after the user selects Save. When deleting a document and saving the record, the confirmation message displays after the user selects Save.
- Select Add. A message displays at the top of the page stating it was successfully added.

### Search IDF5 Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To Search IDF5 records into EPRS, follow the instructions below.

<span id="_Toc135215992" class="anchor"></span>Figure 77: IDF5 Search Fields

![](enterprise-program-reporting-system-eprs-user-guide/079.png)

- Region – Drop-down menu with list of options. Select a Region: 1, 2, 3, 4 or 5.
- Quarter – Drop-down menu with list of options. Select a Quarter:
  - First (Oct. – Dec.)
  - Second (Jan. – Mar.)
  - Third (Apr. – Jun.)
  - Fourth (Jul. – Sep.)
- Audit Report Type: – Drop-down menu with applicable options populated based on user input to the Region field. Select the appropriate Audit Report Type: Annual or Quarterly.
24. If user selects Regions 1, 2, or 3 the following options will populate:  
    - Independent Audit Quarterly Report (1-3)  
    - Independent Audit Annual Statistical Projection of Improper Payments Report (1-3)  
    If user selects Regions 4 or 5, the following options will populate:  
    - Independent Audit Quarterly Report (4/5)  
    - Independent Audit Annual Report (4/5)
- Quarterly Error Rate – Field to enter Quarterly Error Rate in Percentage form.
- CCN Contractor – Enter the CCN Contractor Name.
- Fiscal Year – Drop-down menu with list of options. Select Fiscal Year: 2018, 2019, 2020, 2021, 2022, 2023.
- Annual Error Rate – Field to enter the Annual or Quarterly Error Rate in Percentage form.
- Incentive/Disincentive Percent – Field to enter the Incentive/Disincentive Percentage number.
- Select Search. The search results will display below the search form.

<span id="_Toc135215993" class="anchor"></span>Figure 78 Example of IDF5 Search Results Display

![](enterprise-program-reporting-system-eprs-user-guide/080.png)

- Select Download Data to export the IDF5 Report information to an Excel file.
25. To clear the fields and start your search over, select Clear Filters.

# Appendix A: Troubleshooting SharePoint UIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The missing fields error message displays when one or more fields are missing. Verify that all fields with a red asterisk are filled in.

<span id="_Toc52394524" class="anchor"></span>Figure 79: Missing Fields Error Message

![](enterprise-program-reporting-system-eprs-user-guide/081.png)

The Referral ID Not Found error message displays when you try to find a referral ID that cannot be located.

<span id="_Toc52394526" class="anchor"></span>Figure 80: Referral ID Not Found Error Message

![](enterprise-program-reporting-system-eprs-user-guide/082.png)

# Appendix B: Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym     | Definition                                                                             |
|-------------|----------------------------------------------------------------------------------------|
| CAP         | Corrective Action Plans                                                                |
| CCN         | Community Care Network                                                                 |
| CCP         | Community Care Program                                                                 |
| CDW         | Corporate Data Warehouse                                                               |
| COR         | Contracting Officer’s Representative                                                   |
| CRT         | Congressional Response Team                                                            |
| DAS         | Data Access Service                                                                    |
| DW          | Data Warehouse                                                                         |
| EPRS        | Enterprise Program Reporting System                                                    |
| ETL         | Extract, Transfer, and Load                                                            |
| IDA         | Informatics & Data Analytics                                                           |
| MISSION Act | Maintaining Internal Systems and Strengthening Integrated Outside Networks Act of 2018 |
| NSD         | National Service Desk                                                                  |
| OCC         | Office of Community Care                                                               |
| ODS         | Operational Data Store                                                                 |
| OIT         | Office of Information and Technology                                                   |
| QASP        | Quality Assurance Surveillance Program                                                 |
| SHCD        | Start of Health Care Delivery                                                          |
| UI          | User Interface                                                                         |
| VA          | Department of Veterans Affairs                                                         |
| VAEC        | VA Enterprise Cloud                                                                    |
| VAMC        | VA Medical Center                                                                      |
| VDL         | VA Software Document Library                                                           |
| VHA         | Veterans Health Administration                                                         |
| VISN        | Veterans Integrated Service Network                                                    |
| VistA       | Veterans Health Information Systems and Technology Architecture                        |
| VPN         | Virtual Private Network                                                                |