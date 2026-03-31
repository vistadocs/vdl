---
title: VHIE Portal User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: VHIE Portal
app_code: VAP
app_name: Veterans Authorization and Preferences
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 1
description: > The Veterans Health Information Exchange (VHIE) Program was tasked by the Department of Veterans Affairs (VA) to replace the eHealth Exchange (eHX) solution with a commercial-off- the-shelf (COTS) product called the HealthShare Enterprise Platform (HEP). As part of the enhancement, HealthShare (HS
audience: 
keywords: 
  - strong
  - blockquote
  - table
  - class
  - vhie
  - bookmark
  - portal
  - span
  - figure
  - style
page_count: 0
word_count: 11506
section_count: 20
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Veterans_Authorization_and_Preferences_(VAP)/vdif_ug_vhie_portal.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Veterans_Authorization_and_Preferences_(VAP)/vdif_ug_vhie_portal.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=222"
---

# Veterans Health Information Exchange (VHIE) Portal Build 3.6 VHIE Portal User Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Veterans Health Information Exchange (VHIE) Portal Build 3.6 VHIE Portal User Guide](#veterans-health-information-exchange-vhie-portal-build-36-vhie-portal-user-guide)
    - [Version 3.7](#version-37)
    - [Department of Veterans Affairs (VA) Office of Information and Technology (OIT)](#department-of-veterans-affairs-va-office-of-information-and-technology-oit)
    - [Revision History](#revision-history)
    - [Artifact Rationale](#artifact-rationale)
    - [List of Tables](#list-of-tables)
    - [List of Figures](#list-of-figures)
- [Introduction](#introduction)
  - [Purpose](#purpose)
- [System Summary](#system-summary)
- [Getting Started](#getting-started)
  - [VHIE Portal Roles](#vhie-portal-roles)
  - [VHIE Portal New User Request Instructions](#vhie-portal-new-user-request-instructions)
    - [Step 1. Complete Training](#step-1-complete-training)
    - [Step 2. Submit Access Request](#step-2-submit-access-request)
  - [Log in Via SSOi](#log-in-via-ssoi)
  - [Understanding the Functionalities](#understanding-the-functionalities)
  - [Exit System](#exit-system)
- [Using the Software](#using-the-software)
  - [Patient Search](#patient-search)
    - [Prerequisite](#prerequisite)
  - [Patient Detail Summary](#patient-detail-summary)
    - [Prerequisite](#prerequisite-1)
    - [View Patient Demographic Details](#view-patient-demographic-details)
    - [Patient-Centric Functions](#patient-centric-functions)
  - [Consent Status Tab](#consent-status-tab)
    - [Prerequisite](#prerequisite-2)
    - [Participation Preference: Opt-Out of Sharing (Not Participating)](#participation-preference-opt-out-of-sharing-not-participating)
    - [Participation Preference: Patient Re-Participate in Sharing](#participation-preference-patient-re-participate-in-sharing)
    - [Deceased Patient Notification Message](#deceased-patient-notification-message)
  - [Comments Tab](#comments-tab)
    - [Prerequisite](#prerequisite-3)
  - [Generate Documents Tab](#generate-documents-tab)
    - [Prerequisite](#prerequisite-4)
  - [Facilities Tab](#facilities-tab)
    - [Prerequisite](#prerequisite-5)
  - [Search Menu—Return to Patient Search](#search-menureturn-to-patient-search)
    - [Prerequisite](#prerequisite-6)
  - [Reports—Dashboard Widgets](#reportsdashboard-widgets)
    - [Prerequisite](#prerequisite-7)
  - [Reports—Detailed HIE and Consent Reports](#reportsdetailed-hie-and-consent-reports)
    - [Prerequisite](#prerequisite-8)
    - [Consent Directive Detailed Report](#consent-directive-detailed-report)
    - [Legacy Detailed Report](#legacy-detailed-report)
    - [Patient Opt-Out Detailed Report](#patient-opt-out-detailed-report)
  - [Reports—Summary HIE and Consent Reports](#reportssummary-hie-and-consent-reports)
    - [Prerequisite](#prerequisite-9)
    - [Consent Directive Summary Report](#consent-directive-summary-report)
    - [Patient Opt-Out Summary Report](#patient-opt-out-summary-report)
  - [Admin Menu—Partner Organizations and Facilities List](#admin-menupartner-organizations-and-facilities-list)
    - [Prerequisite](#prerequisite-10)
    - [Access or Modify Partner Organizations List](#access-or-modify-partner-organizations-list)
    - [Access or Modify Facilities List](#access-or-modify-facilities-list)
  - [Welcome Menu—User Preferences, User Guide, and About VHIE Portal](#welcome-menuuser-preferences-user-guide-and-about-vhie-portal)
    - [Prerequisite](#prerequisite-11)
    - [Set or Update User’s Default Facility](#set-or-update-users-default-facility)
    - [Prerequisite](#prerequisite-12)
    - [Access User Guide](#access-user-guide)
    - [View System Software Information](#view-system-software-information)
- [Troubleshooting](#troubleshooting)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
![](vhie-portal-user-guide/001.png)

### Version 3.7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

August 2020

### Department of Veterans Affairs (VA) Office of Information and Technology (OIT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 49%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/27/2020</td>
<td>3.7</td>
<td><blockquote>
<p>Updates:</p>
</blockquote>
<ul>
<li><p>Section <a href="#vhie-portal-new-user-request-instructions"><u>3.2</u></a>: Inserted Health Information Exchange (HIE) portal new user request instructions.</p></li>
<li><p>Added captions to all figures throughout.</p></li>
<li><blockquote>
<p>Updated document to follow current standards and style guidelines.</p>
</blockquote></li>
<li><blockquote>
<p>Reformatted content with bullet or numbered lists where appropriate.</p>
</blockquote></li>
<li><blockquote>
<p>Spelled out first occurrence of all acronyms.</p>
</blockquote></li>
<li><blockquote>
<p>Added acronyms to <a href="#_bookmark163"><u>Table 21</u></a>.</p>
</blockquote></li>
<li><p>Verified document is Section 508 conformant (e.g., added alternate text to all images, verified first table rows are repeated heading rows, etc.).</p></li>
</ul></td>
<td><blockquote>
<p>VA Tech Writer: <a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></p>
</blockquote></td>
</tr>
<tr class="even">
<td>04/2020</td>
<td>3.6</td>
<td><blockquote>
<p>Updates:</p>
</blockquote>
<ul>
<li><p>Updated language from AITC to AWS.</p></li>
<li><p>Update Section <a href="#getting-started"><u>3</u></a> to include instructions for requesting access to the VHIE Portal.</p></li>
</ul></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>03/2020</td>
<td>3.5</td>
<td><blockquote>
<p>Replaced screenshots to mask all data resembling PII format and structure.</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td>03/2020</td>
<td>3.4</td>
<td><ul>
<li><p>Removed <strong>Recent Activity</strong> tab, <strong>Accounting of Disclosures</strong> tab, and the <strong>Disclosures Detailed Report</strong> for the current Patch 3.6 release.</p></li>
<li><p>Updated VHIE Portal Roles table and description in Section <a href="#patient-search"><u>4.1</u></a>. to differentiate Prod and Non-Prod AD policy groups.</p></li>
</ul></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>03/2020</td>
<td>3.3</td>
<td>Updated Section <a href="#patient-search"><u>4.1</u></a> to include description for all VHIE Roles.</td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td>03/2020</td>
<td>3.2</td>
<td>Added Section <a href="#patient-search"><u>4.1</u></a> to let ROI Operators know the appropriate VHIE Role to use when requesting access to the VHIE Portal.</td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>03/2020</td>
<td>3.1</td>
<td><p>Updated Sections <a href="#view-patient-demographic-details"><u>4.2.2</u></a> and <a href="#patient-centric-functions"><u>4.2.3</u></a> with updated screenshots to reflect updated VA Forms for Opt-Out and Re-participation.</p>
<blockquote>
<p>Updated Section 4.14.3 with updated screenshot to reflect the most recent software version.</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 49%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>03/2020</td>
<td>3.0</td>
<td><p>Updated Section <a href="#getting-started"><u>3</u></a> to include the Production Uniform Resource Locator (URL).</p>
<blockquote>
<p>Removed/updated sub-sections under Sections <a href="#admin-menupartner-organizations-and-facilities-list"><u>4.11</u></a> and <a href="#welcome-menuuser-preferences-user-guide-and-about-vhie-portal"><u>4.12</u></a> regarding the reports that are hidden from the GUI for the current release (Deceased Veteran Detailed, Expiring Consent Detailed, Deceased Veteran Summary, Disclosures Summary).</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12/2019</td>
<td>2.9</td>
<td>Update Section <a href="#patient-search"><u>4.1</u></a> Patient Search to include expected response for loading an Inactive Patient for Build 3.1.</td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>09/2019</td>
<td>2.8</td>
<td>Updated Section <a href="#special-instructions-for-error-correction"><u>5.1</u></a> Special Instructions for Error Correction and updated instructions for exporting to Comma-Separated Values (CSV) and Save Extensible Markup Language (XML) throughout the document.</td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/2019</td>
<td>2.7</td>
<td><blockquote>
<p>Updated additional language and labels for tables/figures.</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>08/2019</td>
<td>2.6</td>
<td><blockquote>
<p>Updated based on PMO review.</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/2019</td>
<td>2.5</td>
<td><blockquote>
<p>Updated UIs and content to reflect changes during Build 3.</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>06/11/2019</td>
<td>2.4</td>
<td><blockquote>
<p>Updated content, tables, and figures to reflect Build 3 functionalities.</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td>04/16/2019</td>
<td>2.3</td>
<td><blockquote>
<p>Updated UIs and language throughout to reflect most recent design changes.</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>04/05/2019</td>
<td>2.2</td>
<td>Added a note in Section <a href="#generate-documents-tab"><u>4.5</u></a> to let users know Print functionality is available through the browser.</td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td>03/15/2019</td>
<td>2.1</td>
<td><blockquote>
<p>Added a note under “Generate Documents” to recommend users to allow pop-ups and redirects in the browser’s setting for the VHIE Portal.</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>02/28/2019</td>
<td>2.0</td>
<td><blockquote>
<p>Updated content, images, and document text to reflect Maintaining Internal Systems and Strengthening Integrated Outside Networks (MISSION) Act language.</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td>01/17/2019</td>
<td>1.0</td>
<td><blockquote>
<p>Initial Draft.</p>
</blockquote></td>
<td><blockquote>
<p>VHIE Agile Development</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A user guide is a technical communication document intended to give assistance to people using a system, such as Veterans Health Information Systems and Technology Architecture (VistA) end-users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The user guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

### List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Table 14: Patient Opt-Out Summary Report 57](#_bookmark120)
> [Table 15: Access or Modify Partner Organizations List 61](#_bookmark128)
> [Table 16: Access or Modify Facilities List 66](#_bookmark135)
> [Table 17: Set or Update User’s Default Facility 71](#_bookmark146)
> [Table 18: Access User Guide 75](#_bookmark152)
> [Table 19: View System Software Information 77](#_bookmark156)
> [Table 20: Special Instructions for Error Correction 79](#_bookmark161)
> [Table 21: Acronyms and Abbreviations 81](#_bookmark163)

### List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Figure 26: VHIE Portal—“Patient Detail” Screen: Deceased Veteran Notification](#_bookmark60) [Message 27](#_bookmark60)
> [Figure 27: VHIE Portal—“Patient Detail” Screen: Add Comment Button 28](#_bookmark64)
> [Figure 28: VHIE Portal—“Patient Detail” Screen: Adding Comments 29](#_bookmark65)
> [Figure 29: VHIE Portal—“Patient Detail” Screen: Viewing Comments 30](#_bookmark66)
> [Figure 30: VHIE Portal—Generate Documents Tab: Generate CCD 1.1, CCD 2.1, and](#_bookmark70) [C32 31](#_bookmark70)
> [Figure 31: Sample Health Summary Document 32](#_bookmark71)
> [Figure 32: VHIE Portal—Generate Documents Tab: Saving CCD 1.1 as XML File 33](#_bookmark72)
> [Figure 33: Sample Dialog to Save XML Document 33](#_bookmark73)
> [Figure 34: Selecting Tool to Open XML File 34](#_bookmark74)
> [Figure 35: VHIE Portal—Generate Documents Tab: Generating a C62 File 35](#_bookmark76)
> [Figure 36: VHIE Portal—Generate Documents Tab: Reviewing Documents 36](#_bookmark77)
> [Figure 37: Downloading and Saving XML File 37](#_bookmark78)
> [Figure 38: Selecting Tool to Open XML File 38](#_bookmark79)
> [Figure 39: VHIE Portal—Facilities Tab: View Patient's Treatment Facilities 39](#_bookmark82)
> [Figure 40: VHIE Portal—Return to Patient Search 40](#_bookmark85)
> [Figure 41: VHIE Portal—Selecting Consent Activity Dashboard Report 41](#_bookmark89)
> [Figure 42: Consent Activity Dashboard—Sample Web Calls within 24 Hours Report 42](#_bookmark90)
> [Figure 43: VHIE Portal—Selecting User Activity Dashboard Report 43](#_bookmark91)
> [Figure 44: User Activity Dashboard—Sample User Logins within Past 24 Hours Report](#_bookmark92)
> [...................................................................................................................................... 43](#_bookmark92)
> [Figure 45: Detailed Reports Menu—Selecting Detailed HIE and Consent Reports 44](#_bookmark95)
> [Figure 46: Detailed Reports Menu—Selecting Consent Directive Detailed Report 45](#_bookmark98)
> [Figure 47: Consent Directive Detailed Report—Selecting Search Criteria 46](#_bookmark99)
> [Figure 48: Sample Consent Directive Detailed Report—Exporting to a CSV File 47](#_bookmark100)
> [Figure 49: Detailed Reports Menu—Selecting Legacy Detailed Report 48](#_bookmark103)
> [Figure 50: Legacy Detailed Report—Selecting Search Criteria 49](#_bookmark104)
> [Figure 51: Sample Legacy Detailed Report—Exporting to a CSV File 49](#_bookmark105)
> [Figure 52: Detailed Reports Menu—Selecting Patient Opt-Out Detailed Report 50](#_bookmark108)
> [Figure 53: Patient Opt-Out Detailed Report—Selecting Search Criteria 51](#_bookmark109)
> [Figure 54: Sample Patient Opt-Out Detailed Report—Export and View Options 52](#_bookmark110)
> [Figure 55: Reports Menu—Summary HIE and Consent Reports 53](#_bookmark113)
> [Figure 56: Summary Reports Menu—Selecting Consent Directive Summary Report 54](#_bookmark116)
> [Figure 57: Consent Directive Summary Report—Selecting Search Criteria 55](#_bookmark117)
> [Figure 58: Sample Consent Directive Summary Report—Exporting to a CSV File 56](#_bookmark118)
> [Figure 59: Summary Reports Menu—Selecting Patient Opt-Out Summary Report 57](#_bookmark121)
> [Figure 60: Patient Opt-Out Summary Report—Selecting Search Criteria 58](#_bookmark122)
> [Figure 61: Sample Patient Opt-Out Summary Report—Exporting to a CSV File 59](#_bookmark123)
> [Figure 62: Admin Menu—Partner Organizations and Facilities List 60](#_bookmark126)
> [Figure 63: Admin Menu—Selecting Organizations 61](#_bookmark129)
> [Figure 64: Partner Organizations—Adding a New Partner Organization 62](#_bookmark130)
> [Figure 65: Add Partner Organization—Entering Required Fields and Saving New](#_bookmark131) [Partner Organization 63](#_bookmark131)
> [Figure 66: Partner Organizations—Selecting an Existing Partner Organization 64](#_bookmark132)
> [Figure 67: Edit Partner Organizations—Editing Required Fields and Saving Changes or](#_bookmark133) [Deleting a Partner Organization 65](#_bookmark133)
> [Figure 68: Admin Menu—Selecting Facilities 66](#_bookmark136)
> [Figure 69: Facilities—Adding a New Facility 66](#_bookmark137)
> [Figure 70: Add Facility—Entering Required Fields and Saving New VA Facility 67](#_bookmark138)
> [Figure 71: Facilities—Selecting an Existing Facility 68](#_bookmark139)
> [Figure 72: Edit Facility—Editing Required Fields and Saving Changes or Deleting a](#_bookmark140) [Facility 69](#_bookmark140)
> [Figure 73: Welcome Menu—User Preferences, User Guide, and About VHIE Portal 70](#_bookmark143)
> [Figure 74: VHIE Portal—Landing Page: Notification Message to Set Default Facility 71](#_bookmark147)
> [Figure 75: Welcome Menu—Selecting User Preferences 72](#_bookmark148)
> [Figure 76: Default Facility—Setting Default Facility 73](#_bookmark149)
> [Figure 77: Default Facility—Removing Default Facility 74](#_bookmark150)
> [Figure 78: Welcome Menu—Selecting User Guide 75](#_bookmark153)
> [Figure 79: VA Software Document Library (VDL)—VHIE Portal User Guide PDF 76](#_bookmark154)
> [Figure 80: Welcome Menu—Selecting About VHIE Portal 77](#_bookmark157)
> [Figure 81: “About VHIE Portal” Screen 78](#_bookmark158)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Veterans Health Information Exchange (VHIE) Program was tasked by the Department of Veterans Affairs (VA) to replace the eHealth Exchange (eHX) solution with a commercial-off- the-shelf (COTS) product called the HealthShare Enterprise Platform (HEP). As part of the enhancement, HealthShare (HS) will consume legacy applications that rely on the connection with the eHX Adapter, and in this case, the Veteran Authorization and Preferences (VAP) system.

> At a high-level, VAP manages a Patient’s Consent, also known as the Patient’s Participation Preferences (PPP) and the requests for generating Clinical Document Architecture (CDA)-type documents for selected Veterans, as well as generate and display Health Information Exchange (HIE) and Consent reports. To improve user experience and provide a more streamlined and robust interface, the VAP interface and functionalities will be replaced by a custom-coded interface known, henceforth, as the VHIE Portal.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of the VHIE Portal User Guide is to familiarize internal Veterans Health Administration (VHA) personnel and other authorized users about using the VHIE Portal interface.

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIE Portal application is hosted on Amazon Web Service (AWS). The system is only accessible within the VA intranet to authorized users. The VHIE Portal is intended for internal VHIE users to perform consent management tasks.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the steps for logging in and understanding the VHIE Portal functionalities.

## VHIE Portal Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When requesting access to the VHIE Portal, the following VHIE Portal roles are available based on the level of access that is required.

> ![](vhie-portal-user-guide/002.png) NOTE: The AD Policy Groups for the Non-Production and Production Environments are differentiated by “NPD” and “PRD” at the end of the AD Policy Group name. Operators of the system will need to submit for the “PRD” role when requesting access (e.g., VHIE Operators would submit for the role of “AAC VDIF VHIE Operators PRD”).

> <span id="_bookmark8" class="anchor"></span>Table 1: VHIE Portal Roles Description

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 55%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Role Name</strong></th>
<th><strong>Role Description</strong></th>
<th><strong>AD Policy Groups</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>AAC VDIF</p>
<p>VHIE Data Quality Reporters</p></td>
<td>These users run and view results for Data Quality Reports, and all other Reports available to the VHIE Operators, perform patient searches, as well as download the CDA documents as XML, but do not have the ability to edit consent policies. There are no specific Data Quality reports implemented in VHIE Portal currently.</td>
<td><ul>
<li><p>AAC VDIF VHIE Data Quality Reporters NPD</p></li>
<li><p>AAC VDIF VHIE Data Quality Reporters PRD</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>AAC VDIF VHIE</p>
<p>Operators</p></td>
<td>These users have the same access as the Veterans Data Integration and Federation (VDIF) Reporters, plus can search for patients, view patient details, retrieve CDA Patient Summary documents in HyperText Markup Language (HTML) or XML, as well as edit eHX consent policies for a Veteran (i.e., set a Veteran to opt-out or re-participate in eHX data-sharing).</td>
<td><ul>
<li><p>AAC VDIF VHIE Operators NPD</p></li>
<li><p>AAC VDIF VHIE Operators PRD</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>AAC VDIF</p>
<p>VHIE Portal Technical Administrators</p></td>
<td>These users are technical administrators, who have access to the full VHIE Portal site, plus technical- admin-only resources, but do not have access to any tester-only resources. For the current build, this role has the same resources as the VDIF Super User role.</td>
<td><ul>
<li><p>AAC VDIF VHIE Portal Tech Admin NPD</p></li>
<li><p>AAC VDIF VHIE Portal Tech Admin PRD</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>AAC VDIF</p>
<p>VHIE Portal Testers</p></td>
<td>These users have access to the full VHIE Portal site, including the tester-only resources. For the current build, only the capability to view CDA patient summary documents as XML is a tester-only resource.</td>
<td><ul>
<li><p>AAC VDIF VHIE Portal Testers NPD</p></li>
<li><p>AAC VDIF VHIE Portal Testers PRD</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>AAC VDIF VHIE</p>
<p>Reporters</p></td>
<td>These users run and view results for the detailed and summary reports (but cannot run an individual patient search or edit consent policies).</td>
<td><ul>
<li><p>AAC VDIF VHIE Reporters NPD</p></li>
<li><p>AAC VDIF VHIE Reporters PRD</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>AAC VDIF</p>
<p>VHIE Super Users</p></td>
<td>These users are administrative users at the business level, and have the same access as the VDIF Operators, plus all of the Admin reports and functions, but do not have access to the technical-admin-only resources and tester-only resources.</td>
<td><ul>
<li><p>AAC VDIF VHIE Super Users NPD</p></li>
<li><p>AAC VDIF VHIE Super Users PRD</p></li>
</ul></td>
</tr>
</tbody>
</table>

## VHIE Portal New User Request Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to request access to the VHIE Portal. There are two steps needed to request access to the VHIE Portal:

- [Step 1. Complete Training](#step-1.-complete-training)
- [Step 2. Submit Access Request](#step-2.-submit-access-request)

> ![](vhie-portal-user-guide/003.png)NOTE: If you need assistance with completing this process, please contact your supervisor/community coordinator.

### Step 1. Complete Training

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Complete required training in the VA Talent Management System (TMS):

1.  Log into the [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp)<u>)</u> and complete the following training or view current certificates in the “My Learning History”:

#### VA Privacy and Information Security Awareness and Rules of Behavior (VA 10176)

- Privacy and HIPAA Training (VA 10203)
2.  <span id="_bookmark11" class="anchor"></span>Save completed training certificates:
1.  Save the completion certificates from both courses in a folder on your desktop.
2.  Open the folder where you saved the certificates.
3.  Select both certificates by holding the CTRL key and selecting each certificate.
4.  Right click on one of the certificates and select Send To  Compressed (zipped) folder, as shown in [<u>Figure 1</u>](#_bookmark12):

> ![](vhie-portal-user-guide/004.png)<span id="_bookmark12" class="anchor"></span>Figure 1: Zipping together Completed Training Certificates

5.  Name the new Zip file created in the same folder: “Certifications.zip,” as shown in [<u>Figure 2</u>](#_bookmark13):

> ![](vhie-portal-user-guide/005.png)<span id="_bookmark13" class="anchor"></span>Figure 2: Verifying Training Certificates Zip File Name

> ![](vhie-portal-user-guide/006.png)NOTE: You will upload this file to the Electronic Permission Access System (ePAS) request in [<u>Step 2</u>](#step-2.-submit-access-request) of these instructions.

### Step 2. Submit Access Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Submit an access request via OIT Electronic Permission Access System (ePAS) 9957:

1.  Navigate to the Office of Information and Technology (OIT) [<u>Electronic Permission</u> <u>Access System (ePAS) e9957</u>](https://epas.r02.med.va.gov/submit.cfm?action=select&doc_type=524) page.
2.  Ensure that the “*EO: System Access Request (e9957)*” document is selected from the drop-down list, as shown in [<u>Figure 3</u>](#_bookmark15):

> ![](vhie-portal-user-guide/007.png)<span id="_bookmark15" class="anchor"></span>Figure 3: Selecting the “EO: System Access Request (e9957)” Document

3.  Select Create Document.

> ![](vhie-portal-user-guide/008.png) NOTE: In the steps that follow, you will complete entries for the following tabs on the e9957 form in the following order:

- Request tab ([<u>Step 4</u>](#_bookmark16))
- Type of Access tab ([<u>Step 5</u>](#_bookmark18))
- Comment tab ([<u>Step 6</u>](#_bookmark23))

> ![](vhie-portal-user-guide/009.png)CAUTION: Do *not* submit until all steps have been completed!

4.  <span id="_bookmark16" class="anchor"></span>From the Request tab, complete *all* required fields (yellow shading on the e9957 form), as well as the *non*-required fields (clear/white text boxes on the e9957 form) that are highlighted below:
1.  Complete the “Request” section entries:
    - Action: Choose “Modification of Account”
    - Type of Employment: choose “VA Staff” or “Contractor”
    - Deactivation Date: Enter an expiration date for the access or the end date for the contract if request is for contractor staff
2.  Complete the “General Information” section entries:
    - Full Legal Name (Last, First, and Middle Initial).
    - Previous Name (if applicable).
    - Start Date: Date when you started working at the VA or when your current contract started.
    - Mailing Address: Mailing address of the VA site where you work or the Field Office with which you are affiliated.
    - Duty Title: Your title.
    - Duty Station: Unless geographically located at one of the regional Information Technology Centers (ITC), select Other from the drop-down list. If Other, list the duty station: Enter the site/facility where you are affiliated.
    - Company: Enter “Department of Veterans Affairs” or the name of your company.
    - Department: Enter the identity of the VA department you support.
    - Office: Enter your VA office or “100% Remote.”
    - Mail Code/Division: Enter the mail code for the VA site or the field office with which you are affiliated.
    - Phone Number: Provide your phone number.
    - Project/Application Code: Enter “VDIF” for Veterans Data Integration & Federation program
    - AD Username: The Active Directory (AD) username is listed as the Alias in the Microsoft Outlook Global Address List (GAL) under the General tab, as shown in [<u>Figure 4</u>](#_bookmark17):

> ![](vhie-portal-user-guide/010.png)<span id="_bookmark17" class="anchor"></span>Figure 4: Microsoft Outlook Global Address List (GAL)—General Tab

3.  Complete the “Approver Information” section entries:
    - Supervisor: Use the “Lookup Supervisor…” button to search for and select your immediate supervisor.
    - Designated Approving Officer (DAO): Use the “Lookup DAO…” button to search for and select your service chief.

> ![](vhie-portal-user-guide/011.png) NOTE: The supervisor and DAO can be the same approver.

1.  On t<span id="_bookmark18" class="anchor"></span>he Type of Access tab, complete the following “LAN Access” section entries:
1.  Check the LAN and Exchange Access checkbox, as shown in [<u>Figure 5</u>](#_bookmark19):

> ![](vhie-portal-user-guide/012.png)<span id="_bookmark19" class="anchor"></span>Figure 5: LAN and Exchange Access Checkbox

2.  Update the Security Groups:
    1.  Press the Select Security Group button.
    2.  From the “Select Security Group” dialog in the Search for Group field, type “AAC VDIF”, as shown in [<u>Figure 6</u>](#_bookmark20):

> ![](vhie-portal-user-guide/013.png)<span id="_bookmark20" class="anchor"></span>Figure 6: Searching for “AAC VDIF” Security Groups

3.  Click Search.
4.  Select appropriate Security Group:
    - AAC VDIF VHIE Reporters PRD—Users run and view results for the detailed and summary reports (individual patient search or edit consent policies are *not* available.

> *OR*

- AAC VDIF VHIE Operators PRD—Same access as the VDIF Reporters, plus users can search for patients, view patient details, retrieve CDA Patient Summary documents in HTML or XML, as well as edit eHX consent policies, i.e., set a Veteran to opt-out or re-participate in eHX data-sharing.
5.  Click OK.
3.  Scroll to the bottom of the page and complete the “Affirmations” dialog entries. Check the “Affirmation” checkbox, as shown in [<u>Figure 7</u>](#_bookmark21):

> ![](vhie-portal-user-guide/014.png)<span id="_bookmark21" class="anchor"></span>Figure 7: Affirmations Dialog—Signing Document

4.  Complete the “Security and Privacy” dialog entries ([<u>Figure 8</u>](#_bookmark22)):
    1.  Select Browse.
    2.  Locate and attach the ZIP file containing certificates that you created in [<u>Step 2</u>](#_bookmark11).
    3.  Enter the date of your last “Rules of Behavior” training. To ensure the date is entered correctly, use the “calendar” icon to select the date.

> ![](vhie-portal-user-guide/015.png)<span id="_bookmark22" class="anchor"></span>Figure 8: Security and Privacy Dialog Entries

1.  <span id="_bookmark23" class="anchor"></span>On the Comments tab, do the following:
1.  Type the following text into the “Comments” box, as shown in [<u>Figure 9</u>](#_bookmark24):

#### This request is for Single Sign On – internal (SSOi) to the VHIE Portal, under the VDIF program. I will be using my PIV for logging into the VHIE Portal.

> <span id="_bookmark24" class="anchor"></span>Figure 9: Entering Comment Text

![](vhie-portal-user-guide/016.png)

2.  Select the Save and Submit button, see [<u>Figure 9</u>.](#_bookmark24)
3.  If prompted with the “Signature” dialog pop-up, as shown in [<u>Figure 10</u>,](#_bookmark25) do the following:
    1.  Select the Click here to digitally sign this document link.
    2.  When prompted, enter your Personal Identity Verification (PIV) smart card pin.

> ![](vhie-portal-user-guide/017.png)<span id="_bookmark25" class="anchor"></span>Figure 10: Apply Digital Signature

## Log in Via SSOi

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Take the following steps to log in via Single Sign On – internal (SSOi):

> ![](vhie-portal-user-guide/018.png) NOTE: Once integrated with SSOi, users will only use their PIV card for login per VA’s HSPD-12 implementation of mandatory PIV, unless a special exemption is permitted, and the user requires a VA username and password.

<span id="_bookmark27" class="anchor"></span>Table 2: Log in via SSOi

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>Navigate to the “<strong>VHIE Portal Login</strong>” screen at <a href="http://vaww.telehealth.va.gov/quality/tmp/index.asp"><em><mark>REDACTED</mark></em></a></p>
<blockquote>
<p>![](vhie-portal-user-guide/019.png) <strong>NOTE</strong>: If presented with the website’s security certificate error (<a href="#_bookmark28"><u>Figure 11</u></a>), select “<strong>Continue to this website (not recommended)</strong>”.</p>
<p><span id="_bookmark28" class="anchor"></span><strong>Figure 11: Sample Error Message—Problem with Website's Security Certificate</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/020.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2.</td>
<td><p>Log in using your PIV card (<a href="#_bookmark29"><u>Figure 12</u></a>).</p>
<blockquote>
<p><span id="_bookmark29" class="anchor"></span><strong>Figure 12: “VA Single Sign-On” Screen (PIV Card)</strong></p>
<p>![](vhie-portal-user-guide/021.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3.</td>
<td><p>Select the appropriate certificate and select <strong>OK</strong>.</p>
<blockquote>
<p>![](vhie-portal-user-guide/022.png) <strong>NOTE:</strong> Always select the second certificate as the authentication certificate (<a href="#_bookmark30"><u>Figure 13</u></a>). If you see more than two certificates displayed, make sure to clear your browser’s cached certificates under <strong>Internet Tools</strong>.</p>
<p><span id="_bookmark30" class="anchor"></span><strong>Figure 13: Windows Security—"Select a Certificate” Screen</strong></p>
<p>![](vhie-portal-user-guide/023.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>4.</td>
<td><p>Enter the PIN associated with your PIV card and select <strong>OK</strong> (<a href="#_bookmark31"><u>Figure 14</u></a>).</p>
<blockquote>
<p><span id="_bookmark31" class="anchor"></span><strong>Figure 14: ActivClient Login—PIV PIN Pop-Up Screen</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>5.</td>
<td><p>Arrive at the “<strong>VHIE Portal</strong>” Landing Page (<a href="#_bookmark32"><u>Figure 15</u></a>).</p>
<blockquote>
<p><span id="_bookmark32" class="anchor"></span><strong>Figure 15: VHIE Portal—Landing Page</strong></p>
<p>![](vhie-portal-user-guide/024.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Understanding the Functionalities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIE Portal provides the following functionalities:

- “VHIE Portal” Landing Page
- Patient Search
- View Patient Demographic Details
- Participation Preference: Patient Not Participating
- Participation Preference: Patient Re-participate
- Deceased Patient Notification Message
- View or Add Patient Comments
- Generate Documents (CDA-type Health Documents)
- View Patient’s VA Treatment Facilities
- Search Menu – Return to Patient Search
- Report Menu – Consent Activity Dashboard
- Report Menu – User Activity Dashboard
- Report Menu – Detailed HIE and Consent Reports
- Report Menu – Summary HIE and Consent Reports
- Admin Menu – View or Modify Partner Organization(s) List
- Admin Menu – View or Modify Facilities List
- Welcome Menu – Set or Update User’s Default Facility
- Welcome Menu – Access User Guide
- Welcome Menu – View System Software Information

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Log out of the VHIE Portal by selecting the Logout option under the Welcome menu at the top of the screen.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to use the application with the following assumed experience/skills of the audience:

- Users have basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).
- Users are using the VHIE Portal to do their jobs.
- Users have been provided active roles and access to the VHIE Portal.
- Users have completed any prerequisite training.

> Consult your supervisor or the VA Help Desk if you need help meeting any of the above conditions.

## Patient Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Search allows for a VHIE user to search by the following patient identifiers:

- Social Security Number (SSN)
- First Name
- Last Name.

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user has logged in via SSOi or another VA-approved method for authentication.

<span id="_bookmark38" class="anchor"></span>Table 3: Patient Search

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1.</td>
<td><p>Complete the <strong>Social Security Number</strong>, <strong>First Name</strong>, and <strong>Last Name</strong> fields, and then select</p>
<p><strong>Search</strong> (<a href="#_bookmark39"><u>Figure 16</u></a>).</p>
<blockquote>
<p>![](vhie-portal-user-guide/025.png) <strong>NOTE</strong>: The <strong>Social Security Number</strong>, <strong>First Name</strong>, and <strong>Last Name</strong> fields are all required fields. The <strong>Social Security Number</strong> field accepts numeric characters with and without dashes (e.g., <strong>xxx-xxx-xxxx</strong> and <strong>xxxxxxxxxx</strong>).</p>
<p><span id="_bookmark39" class="anchor"></span><strong>Figure 16: VHIE Portal—"Patient Search” Screen</strong></p>
<p>![](vhie-portal-user-guide/026.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2.</td>
<td><p>Form validation is enforced to ensure that users complete each field in the correct format (<a href="#_bookmark40"><u>Figure</u></a> <a href="#_bookmark40"><u>17</u></a>).</p>
<blockquote>
<p><span id="_bookmark40" class="anchor"></span><strong>Figure 17: VHIE Portal—"Patient Search” Screen: Field Validation</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>A progress bar will display to indicate that a patient search is processing (<a href="#_bookmark41"><u>Figure 18</u></a>).</p>
<blockquote>
<p><span id="_bookmark41" class="anchor"></span><strong>Figure 18: VHIE Portal—“Patient Search” Screen: Data Entries (Masked) and Progress Status Bar</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vhie-portal-user-guide/027.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>4.</p>
</blockquote></td>
<td><p>If the patient’s record has <em>not</em> been loaded from the Legacy system, a notification message will display for the user to try the search again later (<a href="#_bookmark42"><u>Figure 19</u></a>).</p>
<blockquote>
<p><span id="_bookmark42" class="anchor"></span><strong>Figure 19: VHIE Portal—Notification Message: Patient Loading and to Try Search Later</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vhie-portal-user-guide/028.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Patient Detail Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After retrieving a record from a patient search, the VHIE user will be able to view the patient’s demographic details and perform various patient-centric tasks, depending on the role(s) assigned to the VHIE user.

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has successfully retrieved a record from a Patient Search.

### View Patient Demographic Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The patient’s demographic details will be displayed at the top of the screen (if available) for the VHIE user to view, as shown in [<u>Figure 20</u>](#_bookmark46):

> ![](vhie-portal-user-guide/029.png)<span id="_bookmark46" class="anchor"></span>Figure 20: VHIE Portal—"Patient Detail” Screen: Patient Demographic Details

### Patient-Centric Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following functional tabs ([<u>Figure 21</u>](#_bookmark48)) allow the VHIE user to navigate to different pages to perform various tasks and retrieve important information on the patient:

#### Consent Status

- Comments
- Generate Documents (CDA-type Health Documents)
- Facilities (Patient’s VA Treatment Facilities)

> ![](vhie-portal-user-guide/030.png)<span id="_bookmark48" class="anchor"></span>Figure 21: VHIE Portal—"Patient Detail” Screen: Patient-Centric Information Tabs

## Consent Status Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Consent Status tab displays status information about the patient’s participation preferences for:

- Health Treatment
- Social Security Administration (SSA)-authorization for Coverage
- Historical participation preference information

> The “Consent Status” page also allows the VHIE user to initiate the workflows to process the patient’s preference to either participate or not participate in sharing of health information for treatment.

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has successfully retrieved a record from a patient search.

### Participation Preference: Opt-Out of Sharing (Not Participating)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the patient is currently participating in the sharing of Health information, a VHIE user can take the following steps to update the patient’s consent status so that the patient is opted-out of sharing.

#### Prerequisite

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has successfully retrieved a record from a Patient Search.
- The Patient has an opt-in consent status.

> <span id="_bookmark52" class="anchor"></span>Table 4: Patient Opt-Out of Sharing

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>If the Veteran is currently participating in sharing, there will be an <strong>Opt-Out</strong> button under the “<strong>Participation</strong>” section (<a href="#_bookmark53"><u>Figure 22</u></a>). Select the <strong>Opt-Out</strong> button to open the participation form and fill out the required information.</p>
<blockquote>
<p><span id="_bookmark53" class="anchor"></span><strong>Figure 22: VHIE Portal—"Patient Detail” Screen: Opt-Out Button</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/031.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>Complete the required information fields and select the <strong>Save</strong> button to update the Veteran’s participation status (<a href="#_bookmark54"><u>Figure 23</u></a>).</p>
<blockquote>
<p><span id="_bookmark54" class="anchor"></span><strong>Figure 23: VHIE Portal—"Opt-Out of Sharing” Screen</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>

### Participation Preference: Patient Re-Participate in Sharing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the patient is currently opted-out of sharing, a VHIE user can take the following steps to change the patient’s consent status so that the patient is opted-in for sharing.

#### Prerequisite

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has successfully retrieved a record from a Patient Search.
- The Patient has an opt-out consent status.

> ![](vhie-portal-user-guide/032.png)NOTE: If the patient has an explicitly opted-out (*not* participating) preference in the legacy system, the opt-out preference is honored in HealthShare. A message will also display under the patient’s “Detail” section to notify the user of the patient’s “Not Participating” preference.

> <span id="_bookmark56" class="anchor"></span>Table 5: Patient Re-Participate in Sharing

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1.</td>
<td><p>If the veteran is currently <em>not</em> participating in sharing, there will be an <strong>Opt-In</strong> button under the “<strong>Participation</strong>” section (<a href="#_bookmark57"><u>Figure 24</u></a>). Select the <strong>Opt-In</strong> button to open the participation form and fill out the required information.</p>
<blockquote>
<p><span id="_bookmark57" class="anchor"></span><strong>Figure 24: VHIE Portal—“Patient Detail”: Opt-In Button</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/033.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2.</td>
<td><p>Complete the required information fields, then select the <strong>Save</strong> button to update the Veteran’s participation status (<a href="#_bookmark58"><u>Figure 25</u></a>).</p>
<blockquote>
<p><span id="_bookmark58" class="anchor"></span><strong>Figure 25: VHIE Portal—“Reparticipate in Sharing” Screen</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Deceased Patient Notification Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the Patient is deceased, a message will display in the “Patient Detail” and “Participation” sections ([<u>Figure 26</u>](#_bookmark60)) to notify the user that the patient is deceased.

> ![](vhie-portal-user-guide/034.png) NOTE: If the deceased patient had a Participate in Sharing Preference for Treatment, this preference will be honored for a period of six (6) months from the date of death.

#### Prerequisite

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has successfully retrieved a record from a Patient Search.

> ![](vhie-portal-user-guide/035.png)<span id="_bookmark60" class="anchor"></span>Figure 26: VHIE Portal—“Patient Detail” Screen: Deceased Veteran Notification Message

## Comments Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A VHIE user can select the Comments tab to view or add general comments about the patient.

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has successfully retrieved a record from a Patient Search.

> <span id="_bookmark63" class="anchor"></span>Table 6: View/Add Patient Comments

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>To add a comment, under the <strong>Comments</strong> tab, select <strong>Add Comment</strong> (<a href="#_bookmark64"><u>Figure 27</u></a>).</p>
<blockquote>
<p><span id="_bookmark64" class="anchor"></span><strong>Figure 27: VHIE Portal—“Patient Detail” Screen: Add Comment Button</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/036.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>Complete the <strong>Add Comment</strong> field and select the <strong>Post Comment</strong> button to submit comment (<a href="#_bookmark65"><u>Figure 28</u></a>).</p>
<blockquote>
<p><span id="_bookmark65" class="anchor"></span><strong>Figure 28: VHIE Portal—“Patient Detail” Screen: Adding Comments</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/037.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>The most current comment will display as the top comment (<a href="#_bookmark66"><u>Figure 29</u></a>).</p>
<blockquote>
<p>![](vhie-portal-user-guide/038.png) <strong>NOTE</strong>: Comments posted in this area are only viewable in VHIE Portal.</p>
<p><span id="_bookmark66" class="anchor"></span><strong>Figure 29: VHIE Portal—“Patient Detail” Screen: Viewing Comments</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/039.png)</p></td>
</tr>
</tbody>
</table>

## Generate Documents Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A VHIE user can select the Generate Documents tab in the “Patient Detail” page to generate the following documents:

#### CCD v1.1

- CCD v2.1

#### C32

- C62
- Single Encounter Summary (SES)

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has successfully retrieved a record from a Patient Search.

#### ![](vhie-portal-user-guide/040.png)NOTE:

1.  When generating a CCD v1.1, CCD v2.1, or C32, the artifact is generated in a new browser window.
2.  When generating a C62 or SES, the results may return multiple documents and the user can choose which C62 or SES documents to view.
3.  If the user experiences any issues with generating a document, it is recommended to configure the browser’s security and privacy settings for the VHIE Portal to allow pop- ups and redirects.

> If generating a C62, use the Google Chrome web browser for best result. Contents of the C62 text note are base64 encoded, requiring the browser to translate the data link Uniform Resource Locator (URL), which IE is *not* doing for the C62.

4.  To print the CDA-type document, the user can use the browser’s built-in Print functionality to either print or do a print preview.

> <span id="_bookmark69" class="anchor"></span>Table 7: Generate CCD 1.1, CCD 2.1, and C32

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>Under the <strong>Generate Documents</strong> tab, select <strong>CCD 1.1</strong>, <strong>CCD 2.1</strong>, or <strong>C32</strong> as the <strong>Document Type</strong></p>
<p>and select <strong>Generate</strong> (<a href="#_bookmark70"><u>Figure 30</u></a>).</p>
<blockquote>
<p><span id="_bookmark70" class="anchor"></span><strong>Figure 30: VHIE Portal—Generate Documents Tab: Generate CCD 1.1, CCD 2.1, and C32</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/041.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>If available, the selected health document (<a href="#_bookmark71"><u>Figure 31</u></a>) will generate in a new browser window.</p>
<blockquote>
<p><span id="_bookmark71" class="anchor"></span><strong>Figure 31: Sample Health Summary Document</strong></p>
<p>![](vhie-portal-user-guide/042.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>To download the <strong>CCD 1.1</strong>, <strong>CCD 2.1</strong>, or <strong>C32</strong> as an XML, select the document under the</p>
<p><strong>Document Type</strong> field and select <strong>Save XML</strong> (<a href="#_bookmark72"><u>Figure 32</u></a>).</p>
<blockquote>
<p><span id="_bookmark72" class="anchor"></span><strong>Figure 32: VHIE Portal—Generate Documents Tab: Saving CCD 1.1 as XML File</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/043.png)</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><p>The user will be prompted to save the file as an XML Document. Select the appropriate save location and select <strong>Save</strong> (<a href="#_bookmark73"><u>Figure 33</u></a>).</p>
<blockquote>
<p><span id="_bookmark73" class="anchor"></span><strong>Figure 33: Sample Dialog to Save XML Document</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>5.</p>
</blockquote></td>
<td><p>If using Google Chrome as the browser, the user <em>must</em> open the saved file using Google Chrome or another XML viewer application (e.g., Microsoft [MS] Edge or Notepad), see <a href="#_bookmark74"><u>Figure</u></a> <a href="#_bookmark74"><u>34</u></a>.</p>
<blockquote>
<p>![](vhie-portal-user-guide/044.png) <strong>NOTE</strong>: If the user is using Internet Explorer (IE) as the browser when downloading the XML, this step is <em>not</em> necessary as IE is used as the default browser for the XML viewer.</p>
<p>For more information, see Section <a href="#troubleshooting"><u>5</u></a>, “<a href="#troubleshooting"><u>Troubleshooting</u></a>.”</p>
<p><span id="_bookmark74" class="anchor"></span><strong>Figure 34: Selecting Tool to Open XML File</strong></p>
<p>![](vhie-portal-user-guide/045.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark75" class="anchor"></span>Table 8: Generate C62 and SES

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>Under the <strong>Generate Documents</strong> tab, select either <strong>C62</strong> or <strong>Encounter Summary</strong> as the</p>
<blockquote>
<p><strong>Document Type</strong> and select <strong>Generate</strong> (<a href="#_bookmark76"><u>Figure 35</u></a>).</p>
<p>![](vhie-portal-user-guide/046.png) <strong>NOTE</strong>: If generating a <strong>C62</strong>, use the Google Chrome web browser for best result. Contents of the <strong>C62</strong> text note are <strong>base64</strong> encoded, requiring the browser to translate the data link URL, which IE is <em>not</em> doing for the <strong>C62</strong>.</p>
<p><span id="_bookmark76" class="anchor"></span><strong>Figure 35: VHIE Portal—Generate Documents Tab: Generating a C62 File</strong></p>
<p>![](vhie-portal-user-guide/047.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>If multiple documents are returned, select <strong>View Document</strong> to generate the appropriate document or select <strong>Save XML</strong> to download and save the XML (<a href="#_bookmark77"><u>Figure 36</u></a>).</p>
<blockquote>
<p>![](vhie-portal-user-guide/048.png) <strong>NOTE</strong>: <strong>View Document</strong> will open the document in a new browser window and <strong>Save XML</strong></p>
<p>will prompt the user to save the file as an XML document.</p>
<p><span id="_bookmark77" class="anchor"></span><strong>Figure 36: VHIE Portal—Generate Documents Tab: Reviewing Documents</strong></p>
<p>![](vhie-portal-user-guide/049.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>When downloading the XML, Save the file as an <strong>XML</strong> type (<a href="#_bookmark78"><u>Figure 37</u></a>).</p>
<p><span id="_bookmark78" class="anchor"></span><strong>Figure 37: Downloading and Saving XML File</strong></p>
<blockquote>
<p>![](vhie-portal-user-guide/050.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><p>If using Google Chrome as the browser, the user <em>must</em> open the saved file using Google Chrome or another XML viewer application (e.g., MS Edge or Notepad), see <a href="#_bookmark79"><u>Figure 38</u></a>.</p>
<blockquote>
<p>![](vhie-portal-user-guide/051.png) <strong>NOTE</strong>: If the user is using IE as the browser when downloading the XML, this step is <em>not</em> necessary as IE is used as the default browser for the XML viewer. For more information, see Section <a href="#troubleshooting"><u>5</u></a>, “<a href="#troubleshooting"><u>Troubleshooting</u></a>.”</p>
<p><span id="_bookmark79" class="anchor"></span><strong>Figure 38: Selecting Tool to Open XML File</strong></p>
<p>![](vhie-portal-user-guide/052.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Facilities Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A VHIE user can select the Facilities tab in the “Patient Detail” page ([<u>Figure 39</u>](#_bookmark82)) to view the Patient’s VA Treatment Facilities.

> ![](vhie-portal-user-guide/053.png) NOTE: The Patient’s VA Treatment Facilities information under the Facilities tab is read-only.

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has successfully retrieved a record from a Patient Search.

> <span id="_bookmark82" class="anchor"></span>Figure 39: VHIE Portal—Facilities Tab: View Patient's Treatment Facilities

![](vhie-portal-user-guide/054.png)

## Search Menu—Return to Patient Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From within the VHIE Portal, a VHIE user can select the Patient Search option at the top of the web page ([<u>Figure 40</u>](#_bookmark85)) to return to the default “Patient Search” page.

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has successfully retrieved a record from a Patient Search.

> ![](vhie-portal-user-guide/055.png)<span id="_bookmark85" class="anchor"></span>Figure 40: VHIE Portal—Return to Patient Search

## Reports—Dashboard Widgets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From within the VHIE Portal, a VHIE user can select the Reports option at the top of the web page ([<u>Figure 41</u>](#_bookmark89)) to select and generate either of the following dashboards:

- Consent Activity Dashboard—Displays the number of web calls made to the VHIE Portal within the past 24-hours.
- User Activity Dashboard—Displays the number of user logins to the VHIE Portal within the past 24-hours.

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has been assigned the appropriate roles to generate VHIE reports.

> <span id="_bookmark88" class="anchor"></span>Table 9: Reports - Dashboard Widgets

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1.</td>
<td><p>To generate the <strong>Consent Activity Dashboard</strong>, under the <strong>Reports</strong> menu, select</p>
<p><strong>Consent Activity Dashboard</strong> (<a href="#_bookmark89"><u>Figure 41</u></a>).</p>
<blockquote>
<p><span id="_bookmark89" class="anchor"></span><strong>Figure 41: VHIE Portal—Selecting Consent Activity Dashboard Report</strong></p>
<p>![](vhie-portal-user-guide/056.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2.</td>
<td><p>If there have been web calls made to the VHIE Portal application for consent activities within the past <strong>24-hours</strong>, the information will display in the generated graph (<a href="#_bookmark90"><u>Figure</u></a> <a href="#_bookmark90"><u>42</u></a>).</p>
<blockquote>
<p><span id="_bookmark90" class="anchor"></span><strong>Figure 42: Consent Activity Dashboard—Sample Web Calls within 24 Hours Report</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3.</td>
<td><p>To generate the <strong>User Activity Dashboard</strong>, under the <strong>Reports</strong> menu, select <strong>User Activity Dashboard</strong> (<a href="#_bookmark91"><u>Figure 43</u></a>).</p>
<blockquote>
<p><span id="_bookmark91" class="anchor"></span><strong>Figure 43: VHIE Portal—Selecting User Activity Dashboard Report</strong></p>
<p>![](vhie-portal-user-guide/057.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4.</td>
<td><p>If any user accounts were logged into the VHIE Portal application within the past <strong>24- hours</strong>, the information will display in the generated graph (<a href="#_bookmark92"><u>Figure 44</u></a>).</p>
<blockquote>
<p><span id="_bookmark92" class="anchor"></span><strong>Figure 44: User Activity Dashboard—Sample User Logins within Past 24 Hours Report</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Reports—Detailed HIE and Consent Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From within the VHIE Portal, a VHIE user can select the Reports option at the top of the web page ([<u>Figure 45</u>](#_bookmark95)) to select and generate the Detailed HIE and Consent Reports. The Detailed HIE and Consent Reports includes the following:

#### Consent Directive Detailed Report

- Legacy Detailed Report
- Patient Opt-Out Detailed Report

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has been assigned the appropriate roles to generate VHIE reports.

> ![](vhie-portal-user-guide/058.png)<span id="_bookmark95" class="anchor"></span>Figure 45: Detailed Reports Menu—Selecting Detailed HIE and Consent Reports

### Consent Directive Detailed Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Consent Directive Detailed Report provides a detailed listing of specified "participate in sharing" and "opt-out of sharing" activities for one or more patients for a selected range of dates at selected VA Authenticating facilities.

> <span id="_bookmark97" class="anchor"></span>Table 10: Consent Directive Detailed Report

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>From the <strong>Reports</strong> menu, select <strong>Detailed Reports</strong>, and then select <strong>Consent Directive Detailed Report</strong> (<a href="#_bookmark98"><u>Figure 46</u></a>).</p>
<blockquote>
<p><span id="_bookmark98" class="anchor"></span><strong>Figure 46: Detailed Reports Menu—Selecting Consent Directive Detailed Report</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/059.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>Complete the appropriate search criteria, then select <strong>Search</strong> (<a href="#_bookmark99"><u>Figure 47</u></a>).</p>
<blockquote>
<p><span id="_bookmark99" class="anchor"></span><strong>Figure 47: Consent Directive Detailed Report—Selecting Search Criteria</strong></p>
<p>![](vhie-portal-user-guide/060.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>In the returned results, the user can export the report to a <strong>.CSV</strong> (Comma-Separated Values) file by selecting <strong>Export CSV</strong> (<a href="#_bookmark100"><u>Figure 48</u></a>).</p>
<blockquote>
<p><span id="_bookmark100" class="anchor"></span><strong>Figure 48: Sample Consent Directive Detailed Report—Exporting to a CSV File</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/061.png)</p></td>
</tr>
</tbody>
</table>

### Legacy Detailed Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Legacy Detailed Report shows historical consent data of the Patient’s Participation Preferences (PPP; legacy opt-in and opt-out consent policies), prior to the Maintaining Internal Systems and Strengthening Integrated Outside Networks (MISSION) Act.

> <span id="_bookmark102" class="anchor"></span>Table 11: Legacy Detailed Report

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>From the <strong>Reports</strong> menu, select <strong>Detailed Reports</strong>, and then select <strong>Legacy Detailed Report</strong></p>
<blockquote>
<p>(<a href="#_bookmark103"><u>Figure 49</u></a>).</p>
<p><span id="_bookmark103" class="anchor"></span><strong>Figure 49: Detailed Reports Menu—Selecting Legacy Detailed Report</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/062.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2.</td>
<td><p>Complete the appropriate search criteria, then select <strong>Search</strong> (<a href="#_bookmark104"><u>Figure 50</u></a>).</p>
<blockquote>
<p><span id="_bookmark104" class="anchor"></span><strong>Figure 50: Legacy Detailed Report—Selecting Search Criteria</strong></p>
<p>![](vhie-portal-user-guide/063.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3.</td>
<td><p>In the returned results, the user can export the report to a <strong>.CSV</strong> file by selecting <strong>Export CSV</strong></p>
<p>(<a href="#_bookmark105"><u>Figure 51</u></a>).</p>
<blockquote>
<p><span id="_bookmark105" class="anchor"></span><strong>Figure 51: Sample Legacy Detailed Report—Exporting to a CSV File</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/064.png)</p></td>
</tr>
</tbody>
</table>

### Patient Opt-Out Detailed Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Opt-Out Detailed Report provides a detailed listing of patients that are opt-out of sharing.

> <span id="_bookmark107" class="anchor"></span>Table 12: Patient Opt-Out Detailed Report

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>From the <strong>Reports</strong> menu, select <strong>Detailed Reports</strong>, and then select <strong>Patient Opt-Out Detailed Report</strong> (<a href="#_bookmark108"><u>Figure 52</u></a>).</p>
<blockquote>
<p><span id="_bookmark108" class="anchor"></span><strong>Figure 52: Detailed Reports Menu—Selecting Patient Opt-Out Detailed Report</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/065.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>Complete the appropriate search criteria, and then select <strong>Search</strong> (<a href="#_bookmark109"><u>Figure 53</u></a>).</p>
<blockquote>
<p><span id="_bookmark109" class="anchor"></span><strong>Figure 53: Patient Opt-Out Detailed Report—Selecting Search Criteria</strong></p>
<p>![](vhie-portal-user-guide/066.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>In the returned results for the <strong>Patient Opt-Out Detailed Report</strong> (<a href="#_bookmark110"><u>Figure 54</u></a>), the user can:</p>
<ol type="a">
<li><p><strong>Export</strong> the report to a <strong>.CSV</strong> file by selecting <strong>Export CSV</strong>.</p></li>
<li><blockquote>
<p><strong>View</strong> the SSA Portable Document Format (PDF) by selecting the <strong>View</strong> button next to the SSA consent.</p>
</blockquote></li>
</ol>
<blockquote>
<p><span id="_bookmark110" class="anchor"></span><strong>Figure 54: Sample Patient Opt-Out Detailed Report—Export and View Options</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/067.png)</p></td>
</tr>
</tbody>
</table>

## Reports—Summary HIE and Consent Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From within the VHIE Portal, a VHIE user can select the Reports option at the top of the web page ([<u>Figure 55</u>](#_bookmark113)) to select and generate the Summary HIE and Consent Reports. The Summary HIE and Consent Reports includes the following:

#### Consent Directive Summary Report

- Patient Opt-Out Summary Report

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has been assigned the appropriate roles to generate VHIE reports.

> ![](vhie-portal-user-guide/068.png)<span id="_bookmark113" class="anchor"></span>Figure 55: Reports Menu—Summary HIE and Consent Reports

### Consent Directive Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Consent Directive Summary Report provides a summary listing of the selected Consent Directive totals for a selected range of dates at the selected Authenticating facility or facilities.

> <span id="_bookmark115" class="anchor"></span>Table 13: Consent Directive Summary Report

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>From the <strong>Reports</strong> menu, select <strong>Consent Directive Summary Report</strong> (<a href="#_bookmark116"><u>Figure 56</u></a>).</p>
<blockquote>
<p><span id="_bookmark116" class="anchor"></span><strong>Figure 56: Summary Reports Menu—Selecting Consent Directive Summary Report</strong></p>
<p>![](vhie-portal-user-guide/069.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>Complete the appropriate search criteria, and then select <strong>Search</strong> (<a href="#_bookmark117"><u>Figure 57</u></a>).</p>
<blockquote>
<p><span id="_bookmark117" class="anchor"></span><strong>Figure 57: Consent Directive Summary Report—Selecting Search Criteria</strong></p>
<p>![](vhie-portal-user-guide/070.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>In the returned results, the user can export the report to a <strong>.CSV</strong> file by selecting <strong>Export CSV</strong></p>
<p>(<a href="#_bookmark118"><u>Figure 58</u></a>).</p>
<blockquote>
<p><span id="_bookmark118" class="anchor"></span><strong>Figure 58: Sample Consent Directive Summary Report—Exporting to a CSV File</strong></p>
<p>![](vhie-portal-user-guide/071.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Patient Opt-Out Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Opt-Out Summary Report provides a summary listing of patients that are opt-out of sharing.

> <span id="_bookmark120" class="anchor"></span>Table 14: Patient Opt-Out Summary Report

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>From the <strong>Reports</strong> menu, select <strong>Patient Opt-Out Summary Report</strong> (<a href="#_bookmark121"><u>Figure 59</u></a>).</p>
<blockquote>
<p><span id="_bookmark121" class="anchor"></span><strong>Figure 59: Summary Reports Menu—Selecting Patient Opt-Out Summary Report</strong></p>
<p>![](vhie-portal-user-guide/072.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>Complete the appropriate search criteria, and then select <strong>Search</strong> (<a href="#_bookmark122"><u>Figure 60</u></a>).</p>
<blockquote>
<p><span id="_bookmark122" class="anchor"></span><strong>Figure 60: Patient Opt-Out Summary Report—Selecting Search Criteria</strong></p>
<p>![](vhie-portal-user-guide/073.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>In the returned results, the user can export the report to a <strong>.CSV</strong> file by selecting <strong>Export CSV</strong></p>
<p>(<a href="#_bookmark123"><u>Figure 61</u></a>).</p>
<blockquote>
<p><span id="_bookmark123" class="anchor"></span><strong>Figure 61: Sample Patient Opt-Out Summary Report—Exporting to a CSV File</strong></p>
<p>![](vhie-portal-user-guide/074.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Admin Menu—Partner Organizations and Facilities List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From within the VHIE Portal, a VHIE user can select Admin at the top of the web page ([<u>Figure</u>](#_bookmark126) [<u>62</u>](#_bookmark126)) to access and modify the list of Partner Organizations and Facilities.

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user has been assigned the appropriate roles to access and modify the list of Partner Organizations and VA Facilities.

> ![](vhie-portal-user-guide/075.png)<span id="_bookmark126" class="anchor"></span>Figure 62: Admin Menu—Partner Organizations and Facilities List

### Access or Modify Partner Organizations List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIE admin user can access the list of Partner Organizations to view, edit, delete, or add new organizations.

#### Prerequisite

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user is provided with elevated admin privileges to access and modify the list of Partner Organizations.

> <span id="_bookmark128" class="anchor"></span>Table 15: Access or Modify Partner Organizations List

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>From the <strong>Admin</strong> menu, select <strong>Organizations</strong> (<a href="#_bookmark129"><u>Figure 63</u></a>).</p>
<blockquote>
<p><span id="_bookmark129" class="anchor"></span><strong>Figure 63: Admin Menu—Selecting Organizations</strong></p>
<p>![](vhie-portal-user-guide/076.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>To add a new Partner Organization, select <strong>Add Partner Organization</strong> (<a href="#_bookmark130"><u>Figure 64</u></a>).</p>
<p><span id="_bookmark130" class="anchor"></span><strong>Figure 64: Partner Organizations—Adding a New Partner Organization</strong></p>
<blockquote>
<p>![](vhie-portal-user-guide/077.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>Complete the appropriate required fields, and then select <strong>Save</strong> to add the new Partner Organization (<a href="#_bookmark131"><u>Figure 65</u></a>).</p>
<blockquote>
<p><span id="_bookmark131" class="anchor"></span><strong>Figure 65: Add Partner Organization—Entering Required Fields and Saving New Partner Organization</strong></p>
<p>![](vhie-portal-user-guide/078.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><p>To edit or delete an existing Partner Organization, select the targeted organization name (<a href="#_bookmark132"><u>Figure</u></a> <a href="#_bookmark132"><u>66</u></a>).</p>
<blockquote>
<p><span id="_bookmark132" class="anchor"></span><strong>Figure 66: Partner Organizations—Selecting an Existing Partner Organization</strong></p>
</blockquote>
<p>![](vhie-portal-user-guide/079.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>5.</p>
</blockquote></td>
<td><p>Complete the appropriate required fields and select <strong>Save</strong> to edit the organization or select</p>
<blockquote>
<p><strong>Delete</strong> to remove the organization from the list (<a href="#_bookmark133"><u>Figure 67</u></a>).</p>
<p><span id="_bookmark133" class="anchor"></span><strong>Figure 67: Edit Partner Organizations—Editing Required Fields and Saving Changes or Deleting a Partner Organization</strong></p>
<p>![](vhie-portal-user-guide/080.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Access or Modify Facilities List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIE admin user can access the list of VA Facilities to view, edit, delete, or add new facilities.

#### Prerequisite

- The user has logged in via SSOi or another VA-approved method for authentication.
- The user is provided with elevated admin privileges to access and modify the list of VA Facilities.

> <span id="_bookmark135" class="anchor"></span>Table 16: Access or Modify Facilities List

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1.</td>
<td><p>From the <strong>Admin</strong> menu, select <strong>Facilities</strong> (<a href="#_bookmark136"><u>Figure 68</u></a>).</p>
<blockquote>
<p><span id="_bookmark136" class="anchor"></span><strong>Figure 68: Admin Menu—Selecting Facilities</strong></p>
<p>![](vhie-portal-user-guide/081.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2.</td>
<td><p>To add a new VA Facility, select <strong>Add Facility</strong> (<a href="#_bookmark137"><u>Figure 69</u></a>).</p>
<blockquote>
<p><span id="_bookmark137" class="anchor"></span><strong>Figure 69: Facilities—Adding a New Facility</strong></p>
<p>![](vhie-portal-user-guide/082.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>Complete the appropriate required fields, then select <strong>Save</strong> to add the new VA Facility (<a href="#_bookmark138"><u>Figure</u></a> <a href="#_bookmark138"><u>70</u></a>).</p>
<blockquote>
<p><span id="_bookmark138" class="anchor"></span><strong>Figure 70: Add Facility—Entering Required Fields and Saving New VA Facility</strong></p>
<p>![](vhie-portal-user-guide/083.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><p>To edit or delete an existing VA Facility, select the targeted facility name (<a href="#_bookmark139"><u>Figure 71</u></a>).</p>
<blockquote>
<p><span id="_bookmark139" class="anchor"></span><strong>Figure 71: Facilities—Selecting an Existing Facility</strong></p>
<p>![](vhie-portal-user-guide/084.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>5.</p>
</blockquote></td>
<td><p>Complete the appropriate required fields and select <strong>Save</strong> to edit the facility or select <strong>Delete</strong> to remove the facility from the list (<a href="#_bookmark140"><u>Figure 72</u></a>).</p>
<blockquote>
<p><span id="_bookmark140" class="anchor"></span><strong>Figure 72: Edit Facility—Editing Required Fields and Saving Changes or Deleting a Facility</strong></p>
<p>![](vhie-portal-user-guide/085.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Welcome Menu—User Preferences, User Guide, and About VHIE Portal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From within the VHIE Portal, a VHIE user can select the displayed username at the top of the web page ([<u>Figure 73</u>](#_bookmark143)) to select the Welcome menu items:

- User Preferences—Set or update a default facility.
- User Guide—Access the *Portal User Guide*.
- About VHIE Portal—View information about the VHIE Portal software.

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user has logged in via SSOi or another VA-approved method for authentication.

> ![](vhie-portal-user-guide/086.png)<span id="_bookmark143" class="anchor"></span>Figure 73: Welcome Menu—User Preferences, User Guide, and About VHIE Portal

### Set or Update User’s Default Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIE user can set or remove their default facility from the notification message at the “VHIE Portal” Landing Page or by selecting User Preferences from the Welcome menu, under the username.

### Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user has logged in via SSOi or another VA-approved method for authentication.

> <span id="_bookmark146" class="anchor"></span>Table 17: Set or Update User’s Default Facility

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>If the VHIE user has <em>not</em> set a default facility, a notification message displays at the “<strong>VHIE Portal</strong>” Landing Page after login (<a href="#_bookmark147"><u>Figure 74</u></a>).</p>
<blockquote>
<p>![](vhie-portal-user-guide/087.png) <strong>NOTE</strong>: The notification message will continue to display at the “<strong>VHIE Portal</strong>” Landing Page until the VHIE user has set a default facility.</p>
<p><span id="_bookmark147" class="anchor"></span><strong>Figure 74: VHIE Portal—Landing Page: Notification Message to Set Default Facility</strong></p>
<p>![](vhie-portal-user-guide/088.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>If the VHIE user moves on from the “<strong>VHIE Portal</strong>” Landing Page without setting a default facility, the VHIE user can access the web page to set a default facility by selecting <strong>User Preferences</strong> from the <strong>Welcome</strong> menu (<a href="#_bookmark148"><u>Figure 75</u></a>).</p>
<blockquote>
<p><span id="_bookmark148" class="anchor"></span><strong>Figure 75: Welcome Menu—Selecting User Preferences</strong></p>
<p>![](vhie-portal-user-guide/089.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>Select the VA Facility from the drop-down list to use as the default facility, then select <strong>Set Default Facility</strong> (<a href="#_bookmark149"><u>Figure 76</u></a>).</p>
<blockquote>
<p><span id="_bookmark149" class="anchor"></span><strong>Figure 76: Default Facility—Setting Default Facility</strong></p>
<p>![](vhie-portal-user-guide/090.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><p>After setting a default facility, the VHIE user can set a new default facility at any time or remove the current default facility by selecting <strong>Remove Default Facility</strong> (<a href="#_bookmark150"><u>Figure 77</u></a>).</p>
<blockquote>
<p><span id="_bookmark150" class="anchor"></span><strong>Figure 77: Default Facility—Removing Default Facility</strong></p>
<p>![](vhie-portal-user-guide/091.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Access User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIE user can access the VHIE Portal User Guide by selecting User Guide from the

> Welcome menu, under the username.

#### Prerequisite

> The user has logged in via SSOi or another VA-approved method for authentication.

> <span id="_bookmark152" class="anchor"></span>Table 18: Access User Guide

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>From the <strong>Welcome</strong> menu, select <strong>User Guide</strong> (<a href="#_bookmark153"><u>Figure 78</u></a>).</p>
<blockquote>
<p><span id="_bookmark153" class="anchor"></span><strong>Figure 78: Welcome Menu—Selecting User Guide</strong></p>
<p>![](vhie-portal-user-guide/092.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>The VHIE user is automatically re-directed to the VA Software Document Library (VDL) to download the PDF file of the applicable VHIE Portal User Guide (<a href="#_bookmark154"><u>Figure 79</u></a>).</p>
<blockquote>
<p><span id="_bookmark154" class="anchor"></span><strong>Figure 79: VA Software Document Library (VDL)—VHIE Portal User Guide PDF</strong></p>
<p>![](vhie-portal-user-guide/093.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

### View System Software Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VHIE user can view the system status and software version of the VHIE Portal by selecting

> About VHIE Portal from the Welcome menu, under the username.

#### Prerequisite

> The user has logged in via SSOi or another VA-approved method for authentication.

> <span id="_bookmark156" class="anchor"></span>Table 19: View System Software Information

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><p>From the <strong>Welcome</strong> menu, select <strong>About VHIE Portal</strong> (<a href="#_bookmark157"><u>Figure 80</u></a>).</p>
<blockquote>
<p><span id="_bookmark157" class="anchor"></span><strong>Figure 80: Welcome Menu—Selecting About VHIE Portal</strong></p>
<p>![](vhie-portal-user-guide/094.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>The information is displayed for the software version and the system status of the VHIE Portal (<a href="#_bookmark158"><u>Figure 81</u></a>).</p>
<blockquote>
<p><span id="_bookmark158" class="anchor"></span><strong>Figure 81: “About VHIE Portal” Screen</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark161" class="anchor"></span>Table 20: Special Instructions for Error Correction

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 39%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>User Interface</strong></th>
<th><strong>Error</strong></th>
<th><strong>Cause</strong></th>
<th><strong>Resolution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Login Screen</td>
<td>User does not have permissions.</td>
<td>This is caused when the user account, passed from SSOi, is <em>not</em> mapped to the VHIE Portal user access list.</td>
<td>If you need access or have existing permissions, contact the Enterprise Service Desk (ESD) for support.</td>
</tr>
<tr class="even">
<td>Patient Search Screen</td>
<td><p>SSN is required.</p>
<p>Last Name is required.</p>
<p>First Name is required.</p></td>
<td>The SSN, Last Name, and First Name fields <em>must</em> be filled before pressing the <strong>Search</strong> button. Any or all of these errors can occur depending on which fields were filled in and which were not.</td>
<td>The SSN, Last Name, and First Name fields <em>must</em> all be filled in before pressing the <strong>Search</strong> button.</td>
</tr>
<tr class="odd">
<td>Patient Search Screen</td>
<td>SSN is not valid.</td>
<td>The SSN field needs to contain <strong>nine</strong> (<strong>9</strong>) numeric characters. This error occurs if less than <strong>nine</strong> (<strong>9</strong>) numeric characters or any <em>non</em>-numeric characters are entered.</td>
<td>The SSN field <em>must</em> contain exactly <strong>nine</strong> (<strong>9</strong>) numeric and no other characters before pressing the <strong>Search</strong> button. (The Last Name and First Name fields <em>must</em> also be populated.)</td>
</tr>
<tr class="even">
<td>Patient Search Screen</td>
<td><p>Last Name is not valid.</p>
<p>First Name is not valid.</p></td>
<td>The Last Name and First Name fields <em>must</em> contain alphabetic characters only. Some special characters, such as periods and apostrophes, are allowed. Either or both errors can occur depending on which fields were filled incorrectly.</td>
<td>The Last Name and First Name fields <em>must</em> contain only alphabetic characters before pressing the <strong>Search</strong> button. (Some special characters are allowed, such as periods and apostrophes.)</td>
</tr>
<tr class="odd">
<td>Opt-out of Sharing Screen</td>
<td>Patient Signature Date <em>must</em> be after the date the authorization was signed.</td>
<td>This message occurs when you choose the <strong>Opt-out</strong> option on the “<strong>Opt-out of Sharing</strong>” screen if the patient signature date entered is earlier than the date the authorization was originally signed.</td>
<td>The Patient Signature Date field on the “<strong>Opt-out of Sharing</strong>” screen <em>must</em> be filled with a date later than the date the authorization was originally signed if you choose "<strong>Opt-out</strong>" as the reason.</td>
</tr>
<tr class="even">
<td><p>Export Disclosures Report to</p>
<p>.CSV</p></td>
<td><p>Date column is not displaying the date in a standard Date and</p>
<p>Time format</p></td>
<td>This is a result of Excel automatically converting the text file into a different into a default format.</td>
<td><ol type="1">
<li><p>Right-click on the <strong>Date</strong></p></li>
</ol>
<blockquote>
<p>column.</p>
</blockquote>
<ol start="2" type="1">
<li><p>Select <strong>Format Cells</strong>.</p></li>
<li><p>Under the <strong>Number</strong> tab, select <strong>Date</strong> as the <strong>Category</strong>.</p></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 39%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>User Interface</strong></th>
<th><strong>Error</strong></th>
<th><strong>Cause</strong></th>
<th><strong>Resolution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>when opening using Excel.</td>
<td></td>
<td>4. Select the format <strong>Type</strong> to display the Date and Time (e.g., <strong>2/14/12 1:30 PM</strong>).</td>
</tr>
<tr class="even">
<td>View Saved XML for Disclosures Reports and CDA- type Health Documents</td>
<td>Saved XML displays error message on the browser.</td>
<td>If using Google Chrome as the browser, after opening the XML file, the file is opened using IE as the default application.</td>
<td><ul>
<li><p><strong>Resolution 1:</strong></p></li>
</ul>
<blockquote>
<p>Use Microsoft (MS) Internet Explorer (IE) as the browser when downloading XML.</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Resolution 2:</strong></p>
</blockquote></li>
</ul>
<blockquote>
<p>If using Google Chrome as the browser, the user <em>must</em> open the saved file using Google Chrome or another XML viewer application (e.g., MS Edge or Notepad).</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark163" class="anchor"></span>Table 21: Acronyms and Abbreviations

| Term | Definition                                                             |
|----------|----------------------------------------------------------------------------|
| 508      | Section 508 Accessibility                                                  |
| AD       | Active Directory                                                           |
| AWS      | Amazon Web Service                                                         |
| CDA      | Clinical Document Architecture                                             |
| COTS     | Commercial-Off-the-Shelf                                                   |
| CSV      | Comma-Separated Values                                                     |
| DAO      | Designated Approving Officer                                               |
| DoD      | Department of Defense                                                      |
| eHX      | eHealth Exchange                                                           |
| ePAS     | Electronic Permission Access System                                        |
| ESR      | Enrollment System Redesign                                                 |
| GAL      | Global Address List                                                        |
| HC IdM   | Healthcare Identity Management                                             |
| HEP      | HealthShare Enterprise Platform                                            |
| HITSP    | Healthcare Information Technology Standards Panel                          |
| HS       | HealthShare                                                                |
| HTML     | HyperText Markup Language                                                  |
| ICN      | Integration Control Number (MVI)                                           |
| ID       | Identifier or Identification                                               |
| IE       | Internet Explorer                                                          |
| LAN      | Local Area Network                                                         |
| MISSION  | Maintaining Internal Systems and Strengthening Integrated Outside Networks |
| MS       | Microsoft                                                                  |
| MVI      | Master Veteran Index                                                       |
| PDF      | Portable Document Format                                                   |
| PII      | Personally Identifiable Information                                        |
| PIV      | Personal Identity Verification                                             |
| POC      | Point of Contact                                                           |

| Term | Definition                                                  |
|----------|-----------------------------------------------------------------|
| PPP      | Patient’s Participation Preferences                             |
| SES      | Single Encounter Summary                                        |
| SSA      | Social Security Administration                                  |
| SSN      | Social Security Number                                          |
| SSOi     | Single Sign On – internal                                       |
| TMS      | Talent Management System                                        |
| UG       | User Guide                                                      |
| UI       | User Interface                                                  |
| URL      | Uniform Resource Locator                                        |
| VA       | Department of Veterans Affairs                                  |
| VAP      | Veterans Authorizations and Preferences                         |
| VDIF     | Veterans Data Integration and Federation                        |
| VDL      | VA Software Document Library                                    |
| VHA      | Veterans Health Administration                                  |
| VHIE     | Veterans Health Information Exchange                            |
| VIP      | Veteran-focused Integrated Process                              |
| VistA    | Veterans Health Information Systems and Technology Architecture |
| VLER     | Virtual Lifetime Electronic Record                              |
| WWW      | World Wide Web                                                  |
| XML      | Extensible Markup Language                                      |