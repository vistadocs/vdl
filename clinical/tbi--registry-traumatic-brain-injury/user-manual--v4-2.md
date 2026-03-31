---
title: TBI Version 4.2 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: TBI
app_name: "Registry: Traumatic Brain Injury"
section: CLI
app_status: active
pkg_ns: TBI
patch_ver: 4.2
patch_id: TBI*4.2
group_key: "TBI:TBI:4.2"
file_numbers: []
security_keys: []
menu_options: 3
description: The Veterans Health Administration (VHA) is charged with supporting the Presidential Task Force on Returning Global War on Terror Heroes. The Task Force has stated in the Global War on Terror (GWOT) report (recommendation P-7) that the Department of Veterans Affairs (VA) shall “create a ‘Traumatic B
audience: 
keywords: 
  - class
  - colspan
  - span
  - strong
  - table
  - contents
  - even
  - glos
  - patient
  - anchor
page_count: 0
word_count: 32677
section_count: 36
table_count: 52
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: November 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbium.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbium.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=198"
---

---
title: |
  <span id="_Toc495855387" class="anchor"></span>Traumatic Brain Injury (TBI)

  User Manual
---

![](tbi-version-4-2-user-manual/001.png)

November 2015

Office of Information and Technology (OIT)

Product Development

Revision History

|         |                                                                                                                                                                                                  |                                    |                                    |             |            |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|------------------------------------|-------------|------------|
| Version | Description                                                                                                                                                                                      | Author                             | Reviewer(s)                        | Review Type | Issue Date |
| 1.5     | Revised Section 10 for reporting in BIOXL and the Cube datamodel, Removed reference to Firefox in 3.2.1., Removed Firefox from the approved browsers in appendix B, appendix D and the Glossary. | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |             | 11/3/2015  |
| 1.4     | TBI Enhancements Increment 1 - Revised Section 10 for reporting in BIOXL and the Cube datamodel                                                                                                  | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |             | 7/7/15     |
| 1.2     | Increment 6 – no updates                                                                                                                                                                         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |             | 8/28/14    |
| 1.2     | Updated for Increment 4. No major updates, minor formatting updates                                                                                                                              | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |             | 4/25/12    |
| 1.1     | Updated screen shots, incorporated client edits                                                                                                                                                  | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |             | 9/08/11    |
| 1.0     | Final Version – Incorporating comments from BO                                                                                                                                                   | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | Peer        | 2/28/11    |
| 0.5     | Final Updates                                                                                                                                                                                    | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |             | 8/04/10    |
| 0.4     | Incorporating Edits                                                                                                                                                                              | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |             | 8/3/10     |
| 0.3     | Peer Review                                                                                                                                                                                      | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | Peer        | 7/20/10    |
| 0.2     | Update                                                                                                                                                                                           | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |             | 6/23/10    |
| 0.1     | Initial Version                                                                                                                                                                                  | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |             | 11/17/09   |

<span id="_Toc265044303" class="anchor"></span>Table 1 – Typographical Conventions

Table of Contents

List of Tables

Table of Figures

1.  Introduction

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Typographical Conventions Used in the Manual](#typographical-conventions-used-in-the-manual)
  - [Command Buttons and Command Icons](#command-buttons-and-command-icons)
  - [The Traumatic Brain Injury Registry Application](#the-traumatic-brain-injury-registry-application)
  - [Purpose of the Manual](#purpose-of-the-manual)
  - [Recommended Users](#recommended-users)
  - [Hardware Recommendations](#hardware-recommendations)
  - [Related Documents](#related-documents)
- [Background](#background)
  - [Project Scope and Objectives](#project-scope-and-objectives)
  - [Traumatic Brain Injury Registry Processes](#traumatic-brain-injury-registry-processes)
    - [Overview](#overview)
    - [Data Receipt and Processing](#data-receipt-and-processing)
  - [Release History](#release-history)
    - [TBI Registry Release 1.0](#tbi-registry-release-10)
  - [Obtaining Software and Documentation](#obtaining-software-and-documentation)
  - [Documentation on the Intranet](#documentation-on-the-intranet)
- [Software Overview](#software-overview)
  - [Web-based Application Elements](#web-based-application-elements)
  - [Online Help](#online-help)
    - [Browser Help](#browser-help)
    - [Application Help](#application-help)
    - [Accessibility Features](#accessibility-features)
  - [Date of Death and Deceased Check](#date-of-death-and-deceased-check)
  - [Screen Areas and Functions](#screen-areas-and-functions)
    - [Banner Area](#banner-area)
    - [Tabs (Common Navigation Area)](#tabs-common-navigation-area)
    - [Breadcrumbs](#breadcrumbs)
    - [Left Navigation Bar](#left-navigation-bar)
    - [Content Area](#content-area)
  - [User Roles](#user-roles)
    - [TBI Registry Administrator](#tbi-registry-administrator)
    - [TBI Registry Editor](#tbi-registry-editor)
    - [TBI Registry Read Only User](#tbi-registry-read-only-user)
    - [TBI Registry Polytrauma Editor](#tbi-registry-polytrauma-editor)
    - [TBI Registry Polytrauma Read Only User](#tbi-registry-polytrauma-read-only-user)
    - [TBI Registry Reporting User (National, VISN, Station)](#tbi-registry-reporting-user-national-visn-station)
- [Software Details](#software-details)
  - [Starting the Application](#starting-the-application)
  - [Logging In](#logging-in)
  - [Default Registry Page](#default-registry-page)
- [TBI Registry Tabs](#tbi-registry-tabs)
  - [Accessing Tasks](#accessing-tasks)
  - [Error and Warning Messages](#error-and-warning-messages)
  - [TBI Registry Applications](#tbi-registry-applications)
- [Tracking TBI Referrals](#tracking-tbi-referrals)
  - [New TBI Referrals](#new-tbi-referrals)
  - [Editing a New Referral Record](#editing-a-new-referral-record)
    - [New Referrals Screen Fields](#new-referrals-screen-fields)
  - [In Process Referrals](#in-process-referrals)
- [My Tasks \> Referrals \> In Process](#my-tasks-referrals-in-process)
  - [Editing In Process Referrals](#editing-in-process-referrals)
    - [Successful Scheduling Attempts](#successful-scheduling-attempts)
    - [Unsuccessful Scheduling Attempts](#unsuccessful-scheduling-attempts)
    - [In Process Referrals Screen Fields](#in-process-referrals-screen-fields)
  - [Completed Referrals](#completed-referrals)
    - [Completed Referrals Screen Fields](#completed-referrals-screen-fields)
- [Polytrauma Entries Application](#polytrauma-entries-application)
- [TBI and Polytrauma Patient Lookup Application](#tbi-and-polytrauma-patient-lookup-application)
  - [TBI Patients Lookup](#tbi-patients-lookup)
  - [Polytrauma Patients Lookup](#polytrauma-patients-lookup)
- [Reports Application](#reports-application)
  - [BI Office](#bi-office)
  - [Cube Data Model](#cube-data-model)
    - [Measurements](#measurements)
  - [SSRS Reports](#ssrs-reports)
- [User Administration Application](#user-administration-application)
  - [Role Administration Application](#role-administration-application)
- [About the TBI Interface](#about-the-tbi-interface)
  - [Graphical User Interface (GUI) Conventions](#graphical-user-interface-gui-conventions)
    - [Windows](#windows)
    - [Pop-up Windows](#pop-up-windows)
    - [Windows GUI Elements](#windows-gui-elements)
- [Standard Web Browser Shortcut Keys](#standard-web-browser-shortcut-keys)
- [VA Approved Internet Browsers](#va-approved-internet-browsers)
- [Web-based Application Elements](#web-based-application-elements-1)
- [Web Pages](#web-pages)
- [# Pop-up Windows](#pop-up-windows-1)
- [# Web-based Application (WBA) Elements](#web-based-application-wba-elements)
- [Text Box](#text-box)
- [Checkbox](#checkbox)
- [Radio Button](#radio-button)
- [Command Buttons](#command-buttons)
- [Date Fields](#date-fields)
- [Drop-down List](#drop-down-list)
- [List Box](#list-box)
- [# Faded (“Grayed Out”) Choices](#faded-grayed-out-choices)
- [# Keyboard Commands](#keyboard-commands)
- [Read-Only Data Fields](#read-only-data-fields)
- [Tab Key](#tab-key)
- [Changing (Resizing) a Browser Window](#changing-resizing-a-browser-window)
- [Online Help](#online-help-1)
- [Command Buttons](#command-buttons-1)
- [System Timeout](#system-timeout)
- [Accessibility Features](#accessibility-features-1)
- [Application Accessibility Features](#application-accessibility-features)
- [# Activating Drop-down Lists](#activating-drop-down-lists)
- [Navigating the Date Picker Calendar Pop-ups](#navigating-the-date-picker-calendar-pop-ups)
- [Browser Accessibility Features](#browser-accessibility-features)
- [# Using the \< Ctrl \>, \< Alt \> and \< Esc \> Keys](#using-the-ctrl-alt-and-esc-keys)
- [Resizing the Browser Screen](#resizing-the-browser-screen)
- [Windows Accessibility Features](#windows-accessibility-features)
- [StickyKeys](#stickykeys)
- [FilterKeys](#filterkeys)
- [# ToggleKeys](#togglekeys)
- [MouseKeys](#mousekeys)
- [HighContrast](#highcontrast)
- [Glossary](#glossary)

## Typographical Conventions Used in the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other conventions are used:

<table>
<caption><p><span id="_Toc263150471" class="anchor"></span>Table 2 – Graphical Conventions</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 33%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Font</strong></th>
<th><strong>Used for…</strong></th>
<th><strong>Examples:</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Blue text, underlined</td>
<td>Hyperlink to another document or URL</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Green text, dotted underlining</td>
<td>Hyperlink within this document</td>
<td>See Release History for details.</td>
</tr>
<tr class="odd">
<td>Courier New</td>
<td>Patch names, VistA filenames</td>
<td>Patch names will be in this font</td>
</tr>
<tr class="even">
<td>Franklin Gothic Demi</td>
<td><p>Keyboard keys</p>
<p>Web application panel, pane, tab, and button names</p></td>
<td><p>&lt; F1 &gt;, &lt; Alt &gt;, &lt; L &gt;</p>
<p>Other Registries panel</p>
<p>[Delete] button</p></td>
</tr>
<tr class="odd">
<td>Microsoft Sans Serif</td>
<td>Software Application names</td>
<td>Traumatic Brain Injury (TBI)</td>
</tr>
<tr class="even">
<td rowspan="4">Microsoft Sans Serif bold</td>
<td>Registry names</td>
<td><strong>TBI</strong></td>
</tr>
<tr class="odd">
<td>Database field names</td>
<td><strong>Mode field</strong></td>
</tr>
<tr class="even">
<td>Report names</td>
<td><strong>National Summary Report</strong></td>
</tr>
<tr class="odd">
<td>Organization and Agency Names</td>
<td><strong>DoD, VA</strong></td>
</tr>
<tr class="even">
<td>Microsoft Sans Serif, 50% gray and italics</td>
<td>Read-only fields</td>
<td><em>Procedures</em></td>
</tr>
<tr class="odd">
<td>Times New Roman</td>
<td>Normal text</td>
<td>Information of particular interest</td>
</tr>
<tr class="even">
<td rowspan="3">Times New Roman Italic</td>
<td>Text emphasis</td>
<td>“It is <em>very</em> important . . .”</td>
</tr>
<tr class="odd">
<td>National and International Standard names</td>
<td><em>International Statistical Classification of Diseases and Related Health Problems</em></td>
</tr>
<tr class="even">
<td>Document names</td>
<td><em>Traumatic Brain Injury (TBI) Registry User Manual</em></td>
</tr>
</tbody>
</table>

<span id="_Toc263150471" class="anchor"></span>Table 2 – Graphical Conventions

| Graphic                                                                                          | Used for…                                                                          |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](tbi-version-4-2-user-manual/002.png) | Information of particular interest regarding the current subject matter.               |
| ![](tbi-version-4-2-user-manual/003.png) | A tip or additional information that may be helpful to the user.                       |
| ![](tbi-version-4-2-user-manual/004.png) | A warning concerning the current subject matter.                                       |
| ![](tbi-version-4-2-user-manual/005.png) | Information about the history of a function or operation; provided for reference only. |
| ![](tbi-version-4-2-user-manual/006.png)  | Indicates an action or process which is optional                                       |
| ![](tbi-version-4-2-user-manual/007.png)  | Indicates a resource available either in this document or elsewhere                    |

<span id="_Toc265044305" class="anchor"></span>Table 3 – Locations for Documentation Files

## Command Buttons and Command Icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](tbi-version-4-2-user-manual/008.png)        | A command button initiates an action. It is a rectangular “3-dimensional” shape with a label that specifies what action will be performed when the button is clicked. |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tbi-version-4-2-user-manual/009.png)      | Common examples are shown at left. Command buttons that end with three dots indicate that selecting the command may evoke a subsidiary window.                        |
| ![](tbi-version-4-2-user-manual/010.png)             | In some cases, a command icon performs the same function, but appears on the menu bar and has a plain, flat appearance. One example is shown at left.                 |
| ![](tbi-version-4-2-user-manual/011.png) | In the text of this document, both command button and command icon names appear inside square brackets. Examples: \[Search\], \[Save\].                               |

<span id="_Toc268531717" class="anchor"></span>Table 4 – Document File Sets

## The Traumatic Brain Injury Registry Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref264906012" class="anchor"></span>Table 5 – Tabs by Role</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-user-manual/012.png)</th>
<th><p><strong>Note:</strong> Throughout this document, the terms…</p>
<ul>
<li><blockquote>
<p>“Registry” and “TBI” both refer to the Traumatic Brain Injury Registry,</p>
</blockquote></li>
<li><p>“Traumatic Brain Injury Registry” and the corresponding acronym TBI Registry both refer to the <a href="#Glos_WBA">Web-based application (WBA)</a> described in this document.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref264906012" class="anchor"></span>Table 5 – Tabs by Role

The Traumatic Brain Injury Registry application (TBI Registry) supports the maintenance of local and national registries for clinical and resource tracking of care for such Veterans. The TBI Registry software application allows case managers to identify Veterans who participated in Operation Enduring Freedom (OEF) or Operation Iraqi Freedom (OIF) and who sustained a head injury and thus are potential traumatic brain injury (TBI) patients. The TBI Registry permits the case manager to oversee and track the comprehensive evaluation of these patients. It also provides 17 types of reports used for tracking the evaluation and care of individuals identified as possible TBI candidates.

## Purpose of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This user manual provides instructions for using the TBI Registry, which has been developed for the Department of Veterans Affairs (VA) in support Veterans who are potential TBI patients.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TBI Registry software is designed for use by designated case managers who are responsible for screening and overseeing the records of patients both seen and not seen for the comprehensive TBI evaluation.

## Hardware Recommendations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please see the *Registries Installation & Configuration Guide for Web-based Applications (RICG)* for hardware recommendations.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These related documents are available at <http://www.va.gov/vdl/application.asp?appid=198>.

# Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Administration (VHA) is charged with supporting the Presidential Task Force on Returning Global War on Terror Heroes. The Task Force has stated in the *Global War on Terror (GWOT)* report (recommendation P-7) that the Department of Veterans Affairs (VA) shall “create a ‘Traumatic Brain Injury’ Surveillance Center and Registry to monitor returning service members who have possibly sustained head injury and thus may potentially have a traumatic brain injury in order to provide early medical intervention.”

The Traumatic Brain Injury (TBI) Registry software application collects data on the population of Veterans who participated in Operation Enduring Freedom/Operation Iraqi Freedom (OEF/OIF). These individuals need to be seen within 30 days for a comprehensive evaluation. Each facility can produce local reports (information related to patients evaluated and treated in their system).

## Project Scope and Objectives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document applies to the TBI Registry project OBS-104-05-01-004. It does not address a broader vision that may apply to a future integration of multiple medical data registries.

In the early stages of planning for the TBI Registry, one approach considered a gradual implementation of functionality supporting very basic operations by making temporary modifications to the existing Veterans Health Information Systems and Technology Architecture (VistA) system. These modifications were limited in scope and temporary in nature and as such have been developed as an interim solution. This interim solution is under consideration for delivery. The development of the TBI Registry described in this document describes a more mature product to replace the interim solution.

## Traumatic Brain Injury Registry Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TBI Registry consists of the following applications:

- TBI Referral Tracking Application: Patients identified as having sustained potentially traumatic brain injuries in the OEF/OIF missions and who agree to be seen are then scheduled for a comprehensive evaluation within 30 days. If that appointment is not kept, the system tries to schedule another appointment within 30 days. he system makes a third attempt to schedule the comprehensive evaluation within 30 days. After that, the system closes the record.
- Polytrauma Entries Application: Provides a Web-based repository of patients identified as having sustained multiple injuries in the OEF/OIF missions.
- TBI and Polytrauma Patient Lookup: An application that searches the TBI Registry’s data for available information on patients.
- TBI Registry User Administration: Provides information about the TBI Registry’s users and management of the system.
- TBI Role Administration: Provides management and control of access to the system through the use of defined user roles.
- TBI Referral Reports (17 total reports—11 screening and consultation reports and 6 tracking reports): Provides summary reports based on the patient data residing in the TBI Registry for viewing on the VA [intranet](#Glos_Intranet) or through downloadable formats \[Adobe Acrobat Reader Portable Document Format (PDF) and Microsoft Excel\].

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Basic data about individuals is provided by the data feed from the VA [National Data Systems (NDS)](#Glos_NDS). One purpose of TBI Registry is to provide a means of making text data “[computable](#Glos_computabledata).”

The TBI Registry is not installed on your computer workstation. Rather, TBI Registry runs in a Web [browser](#Glos_Browser) from a location on the VA [intranet](#Glos_Intranet). For that reason, TBI Registry is referred to as a “Web-based application” (WBA). If you have already used any program which runs in a Web browser, especially another registry program (like the Embedded Fragments Registry), the TBI Registry will seem familiar to you. Although it is likely that the application will run on many different Web browsers, please see [Appendix E](#AppendixE) for the browsers which have been tested and approved for use with TBI Registry.

| ![](tbi-version-4-2-user-manual/013.png) | Note: This document does not attempt to explain everything about how to operate in the Web browser environment itself; if you need help with using a browser, please contact your supervisor for information about training in browser use. |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref264880552" class="anchor"></span>Table 6 – Tasks by Role

<table>
<caption><p><span id="_Ref264906184" class="anchor"></span>Table 7 – Report Access</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-user-manual/014.png)</th>
<th><p><strong>WARNING:</strong> This application will display <a href="#Glos_PII">personally identifiable information</a> (<a href="#Glos_PII">PII</a>). When you have finished using the application, you should <em>close all instances of your browser</em> that may be running (not just the one you used to access the application).</p>
<p>If you do not, PII could be compromised if another user accesses your Web browser.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref264906184" class="anchor"></span>Table 7 – Report Access

### Data Receipt and Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Basic Patient Data

Within the TBI Registry, basic patient information is provided by the “[back-end](#Glos_backend)” system and is [read only (RO)](#Glos_RO). Since the data feed process is designed to produce a single record for each person, there should not be multiple records for the same person, although that could happen. In the future, a process will be available to allow users to place the record into a “pending” status until the duplicates can be resolved.

#### Referral Review Process

A designated reviewer (the Medical Professional) then reviews the record and either approves or returns the record for more information:

- If not approved, the record is returned to the reviewer.
- If approved, the patient is confirmed into the TBI Registry. If monitoring or consultation was specified during the triage decision, a workflow is set up to enable appropriate actions.
- If an ineligibility decision is upheld, the patient is not accepted into the TBI Registry and the record is closed.

#### Other Uses of TBI Registry

TBI Registry is also used to make a determination regarding the next steps for obtaining additional information on the patient that will be relevant to the information maintained in the TBI Registry. TBI Registry will handle the possibility of a patient being referred multiple times, as well as the actions taken by the reviewer in TBI Registry when a referral is determined ineligible. The TBI Registry does *not*, however, cover actions the reviewer may take that are not supported by interaction with the system (such as notifying the local provider of a decision to identify the patient as ineligible).

## Release History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since this is the first release of the software, there is no past “history” to record here. Future releases will include that history. Changes provided by releases are shown in the following series of tables. Under “Type,” “E” indicates an enhancement, “F” a fix, and “M” a modification. Click on the green links immediately below to jump directly to a specific release.

### TBI Registry Release 1.0 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                     | Type |
|-----|-------------------------------------------------|------|
| 1   | Published application for first production use. | E    |

<span id="_Ref264958910" class="anchor"></span>Table 8 – Task Categories and Tasks

## Obtaining Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no TBI Registry software distributives. Since TBI Registry is a Web-based application, only a VA-approved Web [browser](#Glos_Browser) (see the list at [Appendix D](#AppendixD)) and access to the VA [intranet](#Glos_Intranet) is required.

Documentation files are available for downloading from the following Office of Information and Technology Field Offices (OI&T FO) \[ANONYMOUS SOFTWARE\] directories. [File Transfer Protocol (FTP)](#Glos_FTP) client software may be useful, although it is possible to download these files using a Web browser as well.

| OIFO                               | FTP Address                        | Directory                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

<span id="_Toc265044311" class="anchor"></span>Table 9 - TBI Registry Applications

The TBI REGISTRY guides and manuals are distributed as the following set of files.

<table>
<caption><p><span id="_Ref264909147" class="anchor"></span>Table 10 - Referral Subcategories</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 55%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Contents</th>
<th>Retrieval Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TBI REGISTRY2_0DOC1.ZIP</td>
<td><p>Zipped DOC distributive, which includes both .PDF and .DOC formats:</p>
<p>►      TBI Application User Manual (TBIUM_INC4_UM_062312_Final)</p>
<p>►      TBI Instruments User Manual (TBIINSUM_INC4_UM_062312_Final)</p>
<p>►      TBI Polytrauma User Manual (TBIPTUM_INC4_UM_062312_Final)</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>TBI REGISTRY2_0DOC2.ZIP</td>
<td><p>►      TBI Installation Guide (TBI_INC4_IG_062312_Final)</p>
<p>►      TBI Systems Management Guide (TBI_INC4_TM_062312_Final)</p></td>
<td>BINARY</td>
</tr>
</tbody>
</table>

<span id="_Ref264909147" class="anchor"></span>Table 10 - Referral Subcategories

## Documentation on the Intranet 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this product, including all of the software manuals, is also available in the Health*<u>e</u>*Vet section of the VA Software Document Library (VDL). The Defense/Veterans Traumatic Brain Injury Registry documentation may be found at <http://www.va.gov/vdl/application.asp?appid=198>.

2.  About the Application

# Software Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref264987225" class="anchor"></span>Table 11 – New Referrals Screen Fields</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-user-manual/015.png)</th>
<th><p><strong>WARNING:</strong> This application will display <a href="#Glos_PII">personally identifiable information</a> (<a href="#Glos_PII">PII</a>). When you have finished using the application, you should <em>close all instances of your browser</em> that may be running (not just the one you used to access the application).</p>
<p>If you do not, PII could be compromised if another user accesses your Web browser.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref264987225" class="anchor"></span>Table 11 – New Referrals Screen Fields

## Web-based Application Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a [Web-based application](#Glos_WBA); see [Appendix D](#AppendixD) for a description of typical Web-based application (WBA) elements.

## Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two kinds of online help are or will be available: help for using the browser itself, and help for TBI Registry.

| ![](tbi-version-4-2-user-manual/016.png) | Help files are available by clicking on the ![](tbi-version-4-2-user-manual/017.png) icon. Help files are available for the Tracking, Polytrauma, Administration, and Reporting applications. |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref264991269" class="anchor"></span>Table 12 – In Process Fields

### Browser Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have little or no familiarity with the browser environment, information can be found by accessing the browser’s Help file. Depending on the browser you are using and the way it may have been customized, the following methods may be used:

| ![](tbi-version-4-2-user-manual/018.png) | Pressing the \< F1 \> key is the traditional way to access online help. In a Web-based application like TBI Registry, \< F1 \> will provide help about how to operate the *browser* itself.                               |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tbi-version-4-2-user-manual/019.png) | The help icon in Internet Explorer is typically found somewhere on the light gray browser menu bars at the top of the screen. How your browser is set up will determine whether or not this icon appears on your browser. |
| <u>H</u>elp                                                                                          | Click the Help menu option on the browser’s menu bar.                                                                                                                                                                     |

<span id="_Ref265036797" class="anchor"></span>Table 13 – New Referrals Screen Fields

### Application Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](tbi-version-4-2-user-manual/020.png) *This feature is not available for Build 1; accordingly, the material in this section has been “grayed out.” When online help is available, this document will be revised. In Build 1, if you see and click on the TBI Registry help icon, you will see only a “placeholder” Web page.*

The Help icon, available on every screen of the application, opens the TBI Registry online help file. In most cases, the help offered will be specific to the topic or screen that you were viewing when you clicked the icon. In some cases, however, a specific help topic may not be available, in which case you will see the table of contents for the help file. From that point, you may browse and search for more specific help. The online help file is contained in a series of Web pages.

| ![](tbi-version-4-2-user-manual/021.png) | Note: Since TBI Registry is not a “desktop” application (that is, it does not reside on your computer desktop), pressing \< F1 \> will not open TBI Registry help. Instead, it will open help for the browser that you are using. |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc268528412" class="anchor"></span>Table 14 – Standard Web Browser Shortcut Keys

| ![](tbi-version-4-2-user-manual/022.png) | Note: The display you see in the actual help file may vary from the illustration below. |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|

<span id="_Toc268528413" class="anchor"></span>Table 15 – Approved Browsers

<span class="mark"></span>![](tbi-version-4-2-user-manual/023.png)

<span id="_Toc268528351" class="anchor"></span>Figure 1 – Sample Online Help Page

### Accessibility Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Standard Web browser keyboard shortcuts and application design elements help to make TBI Registry accessible to a wide range of users, including those with limited dexterity, low vision, or other disabilities.

![](tbi-version-4-2-user-manual/024.png) For a complete list of keyboard shortcuts, see Appendix A.

![](tbi-version-4-2-user-manual/025.png) For more information about accessibility features, see Appendix D. <span class="mark"></span>

## Date of Death and Deceased Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some Registry programs perform “deceased checks” of files for each patient in the local registry to validate whether or not the patient is deceased. Although TBI Registry does not perform such a check, it does capture the Date of Death, if that information is entered in the source files. This is particularly true of the files for the polytrauma application. For the referral to be sent to TBI Registry, the patient is screened via the two OEF/OIF clinical reminders in VistA. However unlikely it is that a new referral would be received for a deceased patient there is nothing in the system presently to prevent such a record from being edited.

## Screen Areas and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](tbi-version-4-2-user-manual/026.png)While there are some differences in screen appearance from one task area to another, the general layout is as shown below; ![](tbi-version-4-2-user-manual/027.png) indicate the parts of the screen. Please take a few moments to familiarize yourself with the various screen areas before you begin.

<span id="_Toc268528352" class="anchor"></span>Figure 2 – Screen Areas

### Banner Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Across the top of the screen is the BANNER AREA. It displays the VA logo and the registry name.

### Tabs (Common Navigation Area)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TABS immediately below the application title provide a COMMON NAVIGATION AREA that you will see in all registry programs. These elements allow you to select the type of task to be performed. For more information a list of tasks assigned to you (depending on your role) is available in Table 6.

- My Tasks: To see a list of tasks assigned to you.
- Patients: To view and edit patient records.
- Reporting: To select and view 17 reports.
- Administration: To create user accounts and assign roles. This tab is only visible to people who have administrative credentials.
- Help: Online help is not yet available for TBI Registry, and although you may see the help icon and tab label in the initial build of the application, only a “placeholder” help page is available. Help is expected to be fully functional for Build 2.

| ![](tbi-version-4-2-user-manual/028.png) | Note: The left-right order of tabs may be different from that depicted in this document. The final release of TBI Registry will be “patient-centric,” and the <span class="smallcaps">Patient</span> tab will become the primary tab for users. Functionality for tabs other than the <span class="smallcaps">Patient</span> tab will, however, be essentially the same as discussed in this document. |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Breadcrumbs 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Note the so-called <span class="mark">“BREADCRUMBS”</span> below the tabs (showing, in this case, <span class="smallcaps">REPORTING)</span>; this shows you where you are within the application, how you got there, and the current page's logical parent pages in the information hierarchy.

### Left Navigation Bar 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a TAB is selected, the available tasks for that tab are displayed in the <span class="mark">LEFT NAVIGATION BAR</span> at the far left of the screen.

### Content Area 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <span class="mark">CONTENT AREA</span>contains a number of Web parts, specific to the registry and specific to which common navigation item was selected. Example: In TBI Registry, this screen could show a list of patients. The contents of this area will change depending on which task you have selected. In some cases, the area expands to allow display room for more information, and the <span class="mark">LEFT NAVIGATION BAR</span> temporarily disappears.

## User Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your ability to use various features of TBI Registry will depend upon your assigned role. Some choices will not be available to you if your role does not call for that particular task. You may be assigned more than one role. Roles are assigned by the TBI Registry Administrator. The available roles are described in the following sections.

### TBI Registry Administrator 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As an administrator, you have “super-user” access and you can perform the following activities:

- Edit all TBI referrals
- Edit all Polytrauma entries
- Access the administration section of the Registry and create, edit, and delete user permissions

| ![](tbi-version-4-2-user-manual/029.png) | Note: The administrator cannot access reports without having a reporting role assigned. |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|

### TBI Registry Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As an editor, you can perform the following activities:

- Edit TBI referrals that are mapped to VISNs/stations assigned to the user for their role.

| ![](tbi-version-4-2-user-manual/030.png) | Note: The TBI Registry Editor role requires VISN/Station mapping for each user assigned to this role. |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|

### TBI Registry Read Only User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a read only user, you can perform the following activities:

- Open TBI referrals (in read only mode) that are mapped to VISNs/stations assigned to the user for their role.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-user-manual/031.png)</th>
<th><p><strong>Note:</strong> The TBI Registry Read Only User role requires VISN/Station mapping for each user assigned to this role.</p>
<p>Also, if the user has the same VISN/station mapping in the editor role, the edit access will take precedence.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### TBI Registry Polytrauma Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a polytrauma editor, you can perform the following activities:

- Edit polytrauma referral records that are mapped to VISN/stations assigned to the user for their role.

| ![](tbi-version-4-2-user-manual/032.png) | Note: The TBI Registry Polytrauma Editor role requires VISN/Station mapping for each user assigned to this role. |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|

### TBI Registry Polytrauma Read Only User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a polytrauma read only user, you can perform the following activities:

- Open polytrauma referrals (in read only mode) that are mapped to VISNs/stations assigned to the user for their role.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-user-manual/033.png)</th>
<th><p><strong>Note:</strong> The TBI Registry Polytrauma Read Only User role requires VISN/Station mapping for each user assigned to this role.</p>
<p>Also, if the user has the same VISN/station mapping in the editor role, the edit access will take precedence.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### TBI Registry Reporting User (National, VISN, Station)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a reporting user, you can perform the following activities within the boundaries that your role permits:

- National:
  - Access all reports that have a defined national scope
  - Access all VISNs with reports that have a defined VISN scope
  - Access all stations within reports that have a defined station scope
- VISN:
  - Access all reports that have a defined VISN scope
  - Access all reports that have a station scope defined that falls under the VISNs the user has been granted access. (Example: If a user has been granted access to VISNs 1 and 2, they can also pull up reports for all stations that fall below VISNs 1 and 2.)
  - Cannot access reports of national scope, unless the user is a national reporting user as well.
- Station:
  - Access all reports that have a defined station scope.
  - Cannot access reports of national scope, unless the user is a national reporting user as well.

| ![](tbi-version-4-2-user-manual/034.png) | Note: The TBI Registry Reporting User role requires station mapping for each user assigned to this role. |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|

Table 5 shows the tabs available for each role; Table 6 shows the tasks available for all roles. Table 7 describes report access based on assigned roles.

| TABS                                          | ADMINISTRATOR | TBI EDITOR | TBI READ ONLY USER | POLYTRAUMA EDITOR | POLYTRAUMA READ ONLY USER | REPORTING USER |
|-----------------------------------------------|---------------|------------|--------------------|-------------------|---------------------------|----------------|
| <span class="smallcaps">My Tasks</span>       |               |            |                    |                   |                           |                |
| <span class="smallcaps">Patients</span>       |               |            |                    |                   |                           |                |
| <span class="smallcaps">Reporting</span>      |               |            |                    |                   |                           |                |
| <span class="smallcaps">Administration</span> |               |            |                    |                   |                           |                |

| TASKS                              | ADMINISTRATOR | TBI EDITOR | TBI READ ONLY USER | POLYTRAUMA EDITOR | POLYTRAUMA READ ONLY USER | REPORTING USER |
|------------------------------------|---------------|------------|--------------------|-------------------|---------------------------|----------------|
| Tracking                       |               |            |                    |                   |                           |                |
| Referrals: New/View                |               |            |                    |                   |                           |                |
| Referrals: New/Edit                |               |            |                    |                   |                           |                |
| Referrals: In Process              |               |            |                    |                   |                           |                |
| Referrals: Completed               |               |            |                    |                   |                           |                |
| Polytrauma: Add New                |               |            |                    |                   |                           |                |
| Polytrauma: View                   |               |            |                    |                   |                           |                |
| Polytrauma: Edit                   |               |            |                    |                   |                           |                |
| Patient Lookup                 |               |            |                    |                   |                           |                |
| TBI Patients                       |               |            |                    |                   |                           |                |
| Polytrauma Patients                |               |            |                    |                   |                           |                |
| Administration (Roles)         |               |            |                    |                   |                           |                |
| Users                              |               |            |                    |                   |                           |                |
| Roles Matrix                       |               |            |                    |                   |                           |                |
| Reports                        |               |            |                    |                   |                           |                |
| Screening and Consultation Reports |               |            |                    |                   |                           |                |
| Tracking Reports                   |               |            |                    |                   |                           |                |

| REPORTS                          | ACCESS BY ROLES                                                                                                                                                                                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Initial Screening Reports        |                                                                                                                                                                                                                  |
| National Summary                     | Only visible to national users.                                                                                                                                                                                  |
| VISN Summary                         | Only visible for national or VISN users. If VISN user, viewing is determined by access privileges.                                                                                                               |
| Station Summary                      | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s) and all child stations. |
| Positive Screen Detail               | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s) and all child stations. |
| Missed Screen Detail                 | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s) and all child stations. |
| Veteran Search/Questions             | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s).                        |
| Comprehensive Evaluation Reports |                                                                                                                                                                                                                  |
| VHA Summary                          | Only visible to national users.                                                                                                                                                                                  |
| VISN Summary                         | Visible to national and VISN users.                                                                                                                                                                              |
| VISN Comparison                      | Only visible to national users.                                                                                                                                                                                  |
| VISN Facility Comparison             | Visible to national users and VISN users.                                                                                                                                                                        |
| Facility Detail                      | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s) and all child stations. |
| Appointment Tracking Reports     |                                                                                                                                                                                                                  |
| Status Counts                        | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s) and all child stations. |
| TBI Diagnosis Counts                 | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s) and all child stations. |
| TBI Evaluation Team Counts           | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s) and all child stations. |
| Time to Complete \>= 30 Counts       | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s) and all child stations. |
| Average Time to Complete Eval.       | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s) and all child stations. |
| Attempts Counts                      | Visible to national, VISN, and station users. Constraints are determined by access privileges. Station users are limited to their station(s) and VISN users are limited to their VISN(s) and all child stations. |

# Software Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Starting the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start TBI Registry, follow these steps:

1.  Make sure that you are logged on to Windows and the VA network using the appropriate identity.
2.  ![](tbi-version-4-2-user-manual/035.png) Open your Web browser. The browser opens the site that you have designated as your home page. *Note:* At this time TBI no longer supports FireFox as a browser.

| ![](tbi-version-4-2-user-manual/036.png) |
|-----------------------------------------------------------------------------------------------------|
| Internet Explorer                                                                                   |

3.  In the address bar, enter the Web address of the application page, which will be provided to you when you are designated as an authorized user.

## Logging In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many registry-associated programs, including TBI Registry, use Windows authentication provided by [Active Directory (AD)](#Glos_AD). Your user identity is detected at the time of initial login to the VA network, so a separate login or authentication is not required to run TBI Registry. Security messages will advise you if you are not logged in, have insufficient privileges, etc. This means that if you are already logged into your usual domain, the Web page which provides TBI Registry should load automatically without challenge. You should be able to open your Web browser, enter the URL, and see TBI Registry run automatically.

If you are logged in and you see either of the two “challenge” pop-up windows, or have other questions related to AD, please contact your Information Resources Management (IRM) for assistance.

| Internet Explorer                                                                                    |
|------------------------------------------------------------------------------------------------------|
| ![](tbi-version-4-2-user-manual/037.png) |

The authentication of your TBI Registry role(s), and your privileges, takes place behind the scenes. Following successful authentication, you will be re-directed to TBI Registry.

## Default Registry Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your default Registry page opens. For most TBI Registry users, this will be some variant of the <span class="smallcaps">My Tasks</span> screen:

![](tbi-version-4-2-user-manual/038.png)

<span id="_Toc268528357" class="anchor"></span>Figure 3 – My Tasks \> Reporting

At the top are the VA logo, title, search function, and TABS (My Tasks, Patients, Reporting, and Administration). The tabs shown/available will depend upon your role. The first available task for the My Tasks tab is automatically selected, based on your role. Note that the breadcrumb trail shows where you are: Reporting.

- My Tasks: Displays any tasks assigned to you.
- Patients: Allows you to search for a patient already in the Registry, view and edit patient records.
- Reporting: Allows you to select a report.
- Administration: Permits you to assign users and user roles; view and sort user/role lists; view and edit user records.

# TBI Registry Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Accessing Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To understand how the various tasks associated with TBI Registry are performed, it’s necessary to discuss the TBI Registry tabs. The TBI Registry uses the tabs as task-oriented viewers. Tasks available to you are shown on the left navigation panel, based on the role(s) you have been assigned. Figure 4 shows the tasks available for some roles under the <span class="smallcaps">My Tasks</span> tab.

![](tbi-version-4-2-user-manual/039.png)

<span id="_Toc268528358" class="anchor"></span>Figure 4 – My Tasks and Left Navigation Panel

In many of the samples shown in this document, you will see all possible tasks shown as available, and all the tasks are listed in Table 8 below. On your user screen, you will also see all the tasks associated with that tab–– but not all of them may be available to you. Availability depends on your assigned role. Contact your supervisor or the TBI Registry Administrator for questions about your role.

| Tab        | Task Category   | Activity   | Tab   | Task Category                | Report                     |
|----------------|---------------------|----------------|-----------|----------------------------------|--------------------------------|
| My Tasks       | Referrals           | New            | Reporting | Initial Screening Reports        | National Summary               |
|                |                     | In Process     |           |                                  | VISN Summary                   |
|                |                     | Completed      |           |                                  | Station Summary                |
|                |                     |                |           |                                  | Positive Screen Detail         |
|                | Polytrauma          | View/Edit      |           |                                  | Missed Screen Detail           |
|                |                     |                |           |                                  | Veteran Search/Questions       |
|                |                     | Add New        |           |                                  |                                |
|                |                     |                |           | Comprehensive Evaluation Reports | VHA Summary                    |
| Patients       | TBI Patients        | Lookup Patient |           |                                  | VISN Summary                   |
|                |                     |                |           |                                  | VISN Comparison                |
|                | Polytrauma Patients | Lookup Patient |           |                                  | VISN Facility Comparison       |
|                |                     |                |           |                                  | Facility Detail                |
| Administration | Users               | Search         |           | Appointment Tracking Reports     | Status Counts                  |
|                |                     | Edit           |           |                                  | TBI Diagnosis Counts           |
|                |                     | Edit Roles     |           |                                  | TBI Evaluation Team Counts     |
|                |                     | Remove         |           |                                  | Time to Complete \>=30 Counts  |
|                |                     |                |           |                                  | Average Time to Complete Eval. |
|                | Role Matrix         | Search         |           |                                  | Attempts Counts                |

When you “hover” your mouse pointer over a tab or task that is available to you, a Web address ([URL](#glos_URL)) will appear at the bottom of your browser window, just above the Windows \[Start\] button. If the task is not available, the destination address will not appear, indicating that you do not have access to that task.

![](tbi-version-4-2-user-manual/040.png)

<span id="_Ref264880878" class="anchor"></span>Figure 5 – Destination Address Shows Availability

| ![](tbi-version-4-2-user-manual/041.png) | Note: The URL you see will be different from the one shown in Figure 5. |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|

| ![](tbi-version-4-2-user-manual/042.png) | Important: When you hover near a task item, a highlighting rectangle in lighter blue (similar to the one marking Completed in Figure 6 will appear around the task. To see or to select the link, however, you must click on the task text itself, not just the highlighting rectangle. |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](tbi-version-4-2-user-manual/043.png) | Note: Depending on your browser settings, the task text may or may not show underlining when you hover over it. If the task is not available, or if there is no actual task associated with the text, you will not see a destination displayed, as in Figure 6 – No Task Available |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](tbi-version-4-2-user-manual/044.png)![](tbi-version-4-2-user-manual/045.png)

<span id="_Ref264881117" class="anchor"></span>Figure 6 – No Task Available

| ![](tbi-version-4-2-user-manual/046.png) | Note: The tasks available in the <span class="smallcaps">LEFT NAVIGATION BAR</span> will only include those assigned to your role(s). See Table 6 for tasks available for each role. Also see Table 8 for a listing of all tasks. |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Error and Warning Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If required data elements are not entered on a TBI Registry data entry screen, you will see a popup error message like this one:

![](tbi-version-4-2-user-manual/047.png)

<span id="_Toc268528361" class="anchor"></span>Figure 7 – Data Errors Message

If you try to navigate away from a screen without saving or otherwise completing the screen, you will see this popup warning:

![](tbi-version-4-2-user-manual/048.png)

<span id="_Toc268528362" class="anchor"></span>Figure 8 – Navigating Away from Page

## TBI Registry Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TBI Registry consists of the following applications:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>APPLICATION</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p><strong>TBI Referral Tracking</strong></p></li>
</ol></td>
<td>Provides tracking of patients identified as having sustained potentially traumatic brain injuries in the OEF/OIF missions and who agree to be seen are then scheduled for a comprehensive evaluation within 30 days. If that appointment is not kept, the system tries again to schedule another appointment within 30 days. If that appointment is not kept, the system makes a third attempt to schedule the comprehensive evaluation within 30 days. After that, the system closes the record.</td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li><p><strong>Polytrauma Entries</strong></p></li>
</ol></td>
<td>Provides a Web-based repository of patients identified as having sustained multiple injuries in the OEF/OIF missions.</td>
</tr>
<tr class="odd">
<td><ol start="3" type="1">
<li><p><strong>TBI and Polytrauma Patient Lookup</strong></p></li>
</ol></td>
<td>An application that searches the TBI Registry’s data for available information on patients.</td>
</tr>
<tr class="even">
<td><ol start="4" type="1">
<li><p><strong>TBI Registry User Administration</strong></p></li>
</ol></td>
<td>Provides information about the TBI Registry’s users and management of the system</td>
</tr>
<tr class="odd">
<td><ol start="5" type="1">
<li><p><strong>TBI Role Administration</strong></p></li>
</ol></td>
<td>Provides management and control of access to the system through the use of defined user roles.</td>
</tr>
<tr class="even">
<td><ol start="6" type="1">
<li><p><strong>TBI Referral Reports</strong></p></li>
</ol></td>
<td>(17 total reports—11 screening and consultation reports and 6 tracking reports): Provides summary reports based on the patient data residing in the TBI Registry for viewing on the VA <a href="#Glos_Intranet">intranet</a> or through downloadable formats (Adobe Acrobat Reader Portable Document Format (PDF) and Microsoft Excel).</td>
</tr>
</tbody>
</table>

Depending on your role(s), you’ll have access to certain applications. To select an application click on a tab located immediately below the TBI Registry banner. Once a tab is selected, the available applications for that tab are displayed in the Task Bar at the far left of the screen. You can navigate through an application by observing the “breadcrumbs” located directly underneath the tabs. The breadcrumbs show you the forward path you’ve selected.

![](tbi-version-4-2-user-manual/049.png)<span id="_Toc268528364" class="anchor"></span>Figure 9 – Navigating Through TBI Registry Applications

| ![](tbi-version-4-2-user-manual/050.png) | You can use the Windows navigation arrows (located at the top left corner of your Windows toolbar) to move back through the Registry screens. |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|

Part C. Using the TBI Tracking Application

# Tracking TBI Referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Tracking application to record whether a Veteran who served in OEF/OIF, and who has been positively screened for a traumatic brain injury, receives a consultation within 30 days of the Veteran’s referral. The TBI Referrals application tracks whether the appointment was made and whether the patient showed up for the appointment as scheduled or whether they rescheduled the appointment. If the patient did not make it to the appointment, the system triggers a second appointment within 30 days. If the patient fails to show up for the second appointment, a third appointment within 30 days is triggered. If the patient fails to attend the third appointment, the system closes the case.

## New TBI Referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

My Tasks \> Referrals \> New

![](tbi-version-4-2-user-manual/051.png)To view new referrals to the TBI Registry, click on the “My Tasks” tab to view Referrals. By default, the list of new referrals appears in the content area of the screen. A referral indicates that the Veteran has been referred for evaluation for a variety of reasons, typically through the use of the [CPRS](#Glos_CPRS) screening tool. Descriptions of the three subcategories of referrals are available in Table 10.

![](tbi-version-4-2-user-manual/052.png)

<span id="_Toc268528365" class="anchor"></span>Figure 10 – My Tasks \> Referrals \> New

You can arrange the following categories of referral data in ascending or descending order by clicking the data column headings:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>ID</p></li>
</ul></th>
<th><ul>
<li><p>Screening Date</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>SSN</p></li>
</ul></td>
<td><ul>
<li><p>VAMC</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Patient Name</p></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>CATEGORY</th>
<th>SUBCATEGORY</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3"><ol type="1">
<li><p><strong>Referrals</strong></p></li>
</ol></td>
<td><ol start="2" type="1">
<li><p><strong>New</strong></p></li>
</ol></td>
<td><ol start="3" type="1">
<li><p>Patients who have only the pre-populated information from the VistA</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>In Process</strong></td>
<td>Patients who are scheduled for consultation and evaluation</td>
</tr>
<tr class="odd">
<td><strong>Completed</strong></td>
<td>Patients who have received consultation and evaluation or have failed to attend a third appointment to receive these services.</td>
</tr>
</tbody>
</table>

You can generate, view, or print out a hard copy version of a Veteran’s TBI Health Factor Search Report that lists the following data:

- IRAQ Service Heath Factor Search Results
- TBI Screening – Determination Heath Factor Search Results
- TBI Screening – All Other Health Factor Search Results

![](tbi-version-4-2-user-manual/053.png)Figure 11 is a sample TBI Health Factor Search Report. To create a PDF or Excel file of the report, click the down arrow in the “Select a format” text box and click either Acrobat (PDF) file or Excel and then click “Export”.

<span id="_Ref264906937" class="anchor"></span>Figure 11 – TBI Health Factor Search Report

A Microsoft Windows screen will open and if you chose a PDF or Excel format, Figure 12 appears providing you with choices to open the file and view the report, save the report to a file, or cancel the download process. Once you’ve download the file, you can print a hard copy version of the report to an available printer.

<span id="_Ref264906992" class="anchor"></span>Figure 12 – File Download Pop-up Window  
![](tbi-version-4-2-user-manual/054.png)

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-user-manual/055.png)</th>
<th><p><strong>WARNING:</strong> This application will display <a href="#Glos_PII">personally identifiable information</a> (<a href="#Glos_PII">PII</a>). When you have finished using the application, you should <em>close all instances of your browser</em> that may be running (not just the one you used to access the application).</p>
<p>If you do not, PII could be compromised if another user accesses your Web browser.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](tbi-version-4-2-user-manual/056.png)You can then open a Veteran’s Edit Referral screen by clicking the select button located on the far right of the content area of the screen as seen in Figure 13.

<span id="_Ref264907074" class="anchor"></span>Figure 13 – Opening a Veteran’s Tracking Detail Fields

| ![](tbi-version-4-2-user-manual/057.png) | Note: The information on traumatic brain injuries in Veterans only dates back to April 2007 when the VA first began compiling information on Veterans with traumatic brain injury and polytrauma injuries. |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Editing a New Referral Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

My Tasks \> Referrals \> New \> Edit Referral ID: 0000

You can open a Veteran’s Edit Referral screen by clicking the Select button located on the far right of the content area of the screen as seen in Figure 13.

You will then view the Edit Referral screen as shown in Figure 14. This screen contains the following fields:

1.  Name
2.  SSN#
3.  Date of Screening

![](tbi-version-4-2-user-manual/058.png)You then fill in a proposed date of consultation in the text box highlighted in Figure 15. The first appointment must be within 30 days of the screening date.

<span id="_Ref264882535" class="anchor"></span>Figure 14 – New \> Edit Referral Screen

![](tbi-version-4-2-user-manual/059.png)<span id="_Toc268528371" class="anchor"></span>Figure 15 – Consultation Text Box

| ![](tbi-version-4-2-user-manual/060.png) | WARNING: If a consultation date is not entered, and you attempt to save any data input, a warning message displays. |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|

You must then select and enter a calendar date for the patient’s evaluation.

| ![](tbi-version-4-2-user-manual/061.png) | WARNING: If an evaluation date is not entered, and you attempt to save any data input, an error message displays. |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|

| ![](tbi-version-4-2-user-manual/062.png) | Note: Whenever you click the Save button located at the bottom of the My Tasks \> Referrals \> New \> Edit Referral screen, and whether or not you have entered any data into the text boxes or selected an option in the pull-down menus, the status of the referral will change from “New” to “In Process”. |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Figure 16 shows the error message you will see if you attempt to save the date you’ve entered into the Consultation Date text box without also entering an evaluation date. The consultation date will be saved to the patient’s file, but the consultation tracking process can’t be completed until the evaluation date is entered.

You can close the pop-up window and continue to enter data in the Edit Referral screen by clicking the OK button located in the Save Successful pop-up window.

<span id="_Ref265035976" class="anchor"></span>Figure 16 – Consultation Date Error Message

![](tbi-version-4-2-user-manual/063.png)

### New Referrals Screen Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 11 contains a list of all fields, subfields, and descriptions for the My Tasks \> Referrals \> New \> Edit Referral ID: 0000 screen.

| FIELD                                                        | SUBFIELD                                    | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Facility:                                                    |                                                 | The facility where the TBI screen was completed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Name/SSN# of Patient with Positive Screen and Desiring Eval: |                                                 | Patient identifier for the OEF/OIF Veteran that had a positive TBI screen and agreed to a comprehensive TBI evaluation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Date of Screening (mm/dd/yyyy):                              |                                                 | Date the TBI Screening was completed. The value is listed as a date range from April 2007 (04/01/2007) to the present date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Date of Consult/Referral (mm/dd/yyyy):                       |                                                 | Date when a consultation was submitted/referral made for the comprehensive TBI evaluation. The value is listed as a date range from April 2007 (04/01/2007) to the present date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Not Applicable:                                              |                                                 | This is a check box that should be selected when a consultation or referral was not submitted. Selection of this check box will activate the “Other Consult/Referral Status” field for further clarification.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Other Consult/Referral Status:                               |                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                  | Consult Not Submitted:                      | This option should be selected when a consult was not submitted or a referral was not made for the comprehensive TBI evaluation. Selection of this field will prompt for the user to take follow up action. The status of this case cannot be moved to “Completed” until appropriate action has been taken and indicated on the Web application.                                                                                                                                                                                                                                                                                                 |
|                                                                  | Evaluation without Referral/Consult:        | This option should be selected when the comprehensive TBI evaluation was completed without submission of a consultation or the making of a referral due to facility practice patterns.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Attempts to Contact Patient for Scheduling Purposes:         |                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                  | Unable:                                     | The initial attempt to contact the patient for scheduling needs to occur within 5 days of the receipt of the consultation/referral for a comprehensive TBI evaluation. Two additional attempts must occur within 14 days from the positive screen. If all three attempts to contact the patient within the first 14 days of the positive screen are unsuccessful, a certified letter is sent to the patient providing contact information should they desire to call for an appointment. This letter must be sent within 14 days of the positive screen. All efforts to contact the patient should be documented in the patient’s health record. |
|                                                                  | Scheduled: Date Offered by Facility:        | The patient was successfully contacted and the patient agreed to an appointment scheduled on the date offered by the facility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                  | Scheduled: Date Requested by Patient:       | The patient was successfully contacted and the appointment was made on a date requested by the patient.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                  | Refused:                                    | The patient was successfully contacted for scheduling purposes, but the patient refused the offer of a comprehensive TBI evaluation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                  | Unavailable:                                | The patient is not available for scheduling due to reasons beyond their control (e.g., incarceration, death, or redeployment).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Date Scheduled with TBI Evaluation Team (mm/dd/yyyy)         |                                                 | Corresponds with appointment date for comprehensive TBI evaluation that is scheduled in CPRS/VistA. Value reflects date range from April 2007 (04/01/2007) to the present date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Time to Scheduled Appointment with TBI Evaluation Team:      |                                                 | Calculated value that is the difference in days between the date of the positive TBI screen and the date of the scheduled appointment with the TBI evaluation team.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Delay in Completing Evaluation:                              |                                                 | Delays in completing a scheduled appointment can occur for a number of reasons. The tracking application defines these delays as:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                  | No Show:                                    | The patient did not show for their scheduled appointment for the comprehensive evaluation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                  | Cancellation by Patient:                    | The patient cancelled their scheduled appointment for the comprehensive TBI evaluation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                  | Cancellation by Clinic:                     | The clinic cancelled the scheduled appointment for the comprehensive TBI evaluation. (Note that this response does not justify not completing the evaluation and will create a new entry beginning with the “Contact” fields.)                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                  | Delay in Consult/Referral Submission:       | The time delay in completing the TBI evaluation was impacted by a delay in submission of the consultation or referral to the TBI evaluation team.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                  | No Delay in Completing an Evaluation:       | This option is selected if the TBI evaluation process fell within 30 days of the positive TBI screening.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                  | Clinic Capacity:                            | This option is selected if your available clinic does not have sufficient appointment time slots to meet the demand.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                  | Delay in Successful Patient Contact:        | This option is selected when the clinic makes multiple attempts to contact the patient before successfully establishing contact and scheduling the appointment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Date Evaluation Completed (mm/dd/yyyy)                       |                                                 | Entry of date when the comprehensive TBI evaluation was completed by the TBI evaluation team. The calendar provides a date range from April 2007 (04/01/2007) to the present date.. From this entry, the Time to Completed Evaluation value is calculated as the difference in days between the date of the positive TBI screen and the date the TBI evaluation was completed.                                                                                                                                                                                                                                                                   |
| Time to Completed Evaluation:                                |                                                 | Calculated value that is the difference in days between the date of the positive TBI screen and the date the TBI evaluation was completed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Definitive TBI Diagnosis:                                    |                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                  | Yes                                         | Response indicating positive results of the comprehensive TBI evaluation resulting in a definitive diagnosis of TBI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                  | No                                          | Response indicating negative results of the comprehensive TBI evaluation resulting in a definitive diagnosis of no TBI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Responsible TBI Evaluation Team (Service/Clinic):            |                                                 | Response represents the Service/Clinic responsible for completing the TBI evaluation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                  | PM&R                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                  | Neurology                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                  | Behavioral Health                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                  | Primary Care With Specialty Training in TBI |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                  | Other                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Status:                                                      |                                                 | New                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## In Process Referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have saved a “New” referral record, the status of the record changes to “In Process.” This change is reflected in the Breadcrumbs and in the Status field located at the bottom of the screen’s content area.

Figure 17 shows that the screen’s layout and data fields are identical to the New Referral Records screen. The two main differences involve the highlighted Breadcrumbs and the Status field.

# My Tasks \> Referrals \> In Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](tbi-version-4-2-user-manual/064.png)To view In Process referrals in the TBI Registry, click the “My Tasks” tab to view Referrals. Click in the light blue box surrounding the title of this subcategory and the content area of the screen will display a list of all patients undergoing the consultation and evaluation segment of the referral process. A referral is generated when a Veteran is identified as a potential TBI patient for a variety of reasons, typically involving the application of the screening tool used in [CPRS](#Glos_CPRS). Descriptions of all three subcategories of referrals are available in Table 10.

## Editing In Process Referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you edit and save a New Process referral, it is transferred to the In Process subcategory. Navigating the In Process screen is very similar to editing the New Process screen.

![](tbi-version-4-2-user-manual/065.png)My Tasks \> Referrals \> In Process \> Edit Referral ID:

<span id="_Ref264988817" class="anchor"></span>Figure 17 – In Process Referral Screen

### Successful Scheduling Attempts 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you contact a patient and the individual is able to meet established appointment dates for consultation with a physician and the date established to meet with the TBI Evaluation Team, the following In Process \> Edit Referral ID: 0000 fields must be complete:

- Date of Consult/Referral
- Attempts to Contact Patient for Scheduling Purposes:
- Date Scheduled with TBI Evaluation Team
- Delay in Completing Evaluation
  - No Delay in Completing Evaluation
- Date Evaluation Completed
- Definitive TBI Diagnosis
- ![](tbi-version-4-2-user-manual/066.png)Responsible TBI Evaluation Team (Service/Clinic)

Figure 18 shows successful In Process consultation and evaluation results.

<span id="_Ref264988976" class="anchor"></span>Figure 18 –Successful Referral Scheduling

Once the patient has fulfilled all scheduling requirements, and you’ve updated the data in the patient’s file, you can click either the Save button to keep the referral in process or click the Complete button to move the referral to the Referrals Completed process.

### Unsuccessful Scheduling Attempts 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Attempts to contact the patient to set a consultation date must be identified. By clicking the arrow on the pull-down menu, you can select one of the following values:

- Unable
- Scheduled: Date Offered By Facility
- Scheduled: Date Requested By Patient
- Refused
- Unavailable

Once the patient is seen by the doctor, you can enter the date into the evaluation completion date text box. If not, a reason must be entered. The categories of reasons available in the pull-down menu for the Delay in Completing Evaluation field are:

- No Show
- Cancellation By Patient
- Cancellation By Clinic
- Delay in Consult/Referral Submission
- No Delay in Completing Evaluation
- Clinic Capacity
- Delay in Successful Patient Contact

![](tbi-version-4-2-user-manual/067.png)The system then triggers a second appointment and the process begins again. A total of three appointments are scheduled for the patient to see a doctor during the mandated TBI application timeframe. After three failed attempts, the system closes out the patient’s file. Figure 19 shows the referral file of a patient where two attempts have been made to complete the evaluation process. One more attempt will be made and then tracked to complete the process.

<span id="_Ref303341061" class="anchor"></span>Figure 19 - Completing an In Process Referral

Once you have entered all required data to the patient’s “In Process” referral, you can click the Complete button located at the bottom of the In Process \> Edit Referral screen.

### In Process Referrals Screen Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 12 contains a list of all fields, subfields, and descriptions for the My Tasks \> Referrals \> In Process \> Edit Referral ID: 0000 screen.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 27%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FIELD</strong></th>
<th><strong>SUBFIELD</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Facility:</strong></td>
<td></td>
<td>The facility where the TBI screen was completed.</td>
</tr>
<tr class="even">
<td><strong>Name/SSN# of Patient with Positive Screen and Desiring Eval:</strong></td>
<td></td>
<td>Patient identifier for the OEF/OIF Veteran that had a positive TBI screen and agreed to a comprehensive TBI evaluation.</td>
</tr>
<tr class="odd">
<td><strong>Date of Screening (dd/mm/yyyy):</strong></td>
<td></td>
<td>Date the TBI Screening was completed. The value is listed as a date range from April 2007 (04/01/2007) to the present date.</td>
</tr>
<tr class="even">
<td><strong>Date of Consult/Referral (mm/dd/yyyy):</strong></td>
<td></td>
<td>Date when a consultation was submitted/referral made for the comprehensive TBI evaluation. The value is listed as a date range from April 2007 (04/01/2007) to the present date.</td>
</tr>
<tr class="odd">
<td><strong>Not Applicable:</strong></td>
<td></td>
<td>This is a check box that should be selected when a consultation or referral was not submitted. Selection of this check box will activate the “Other Consult/Referral Status” field for further clarification.</td>
</tr>
<tr class="even">
<td><strong>Other Consult/Referral Status:</strong></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Consult Not Submitted:</strong></td>
<td>This option should be selected when a consult was not submitted or a referral was not made for the comprehensive TBI evaluation. Selection of this field will prompt for the user to take follow up action. The status of this case cannot be moved to “Completed” until appropriate action has been taken and indicated on the Web application.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Evaluation without Referral/Consult:</strong></td>
<td>This option should be selected when the comprehensive TBI evaluation was completed without submission of a consultation or the making of a referral due to facility practice patterns.</td>
</tr>
<tr class="odd">
<td><strong>Attempts to Contact Patient for Scheduling Purposes:</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Unable:</strong></td>
<td>The initial attempt to contact the patient for scheduling needs to occur within 5 days of the receipt of the consultation/referral for a comprehensive TBI evaluation. Two additional attempts must occur within 14 days from the positive screen. If all three attempts to contact the patient within the first 14 days of the positive screen are unsuccessful, a certified letter is sent to the patient providing contact information should they desire to call for an appointment. This letter must be sent within 14 days of the positive screen. All efforts to contact the patient should be documented in the patient’s health record.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Scheduled: Date Offered by Facility:</strong></td>
<td>The patient was successfully contacted and the patient agreed to an appointment scheduled on the date offered by the facility.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Scheduled: Date Requested by Patient:</strong></td>
<td>The patient was successfully contacted and the appointment was made on a date requested by the patient.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Refused:</strong></td>
<td>The patient was successfully contacted for scheduling purposes, but the patient refused the offer of a comprehensive TBI evaluation.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Unavailable:</strong></td>
<td>The patient is not available for scheduling due to reasons beyond their control (e.g., incarceration, death, or redeployment).</td>
</tr>
<tr class="odd">
<td><strong>Date Scheduled with TBI Evaluation Team (mm/dd/yyyy)</strong></td>
<td></td>
<td>Corresponds with appointment date for comprehensive TBI evaluation that is scheduled in CPRS/VistA. Value reflects a date range from April 2007 (04/01/2007) to the present date.</td>
</tr>
<tr class="even">
<td><strong>Time to Scheduled Appointment with TBI Evaluation Team:</strong></td>
<td></td>
<td>Calculated value that is the difference in days between the date of the positive TBI screen and the date of the scheduled appointment with the TBI evaluation team.</td>
</tr>
<tr class="odd">
<td><strong>Delay in Completing Evaluation:</strong></td>
<td></td>
<td>Delays in completing a scheduled appointment can occur for a number of reasons. The tracking application defines these delays as:</td>
</tr>
<tr class="even">
<td></td>
<td><strong>No Show:</strong></td>
<td>The patient did not show for their scheduled appointment for the comprehensive evaluation.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Cancellation by Patient:</strong></td>
<td>The patient cancelled their scheduled appointment for the comprehensive TBI evaluation.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Cancellation by Clinic:</strong></td>
<td>The clinic cancelled the scheduled appointment for the comprehensive TBI evaluation. (Note that this response does not justify not completing the evaluation and will create a new entry beginning with the “Contact” fields.)</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Delay in Consult/Referral Submission:</strong></td>
<td>The time delay in completing the TBI evaluation was impacted by a delay in submission of the consultation or referral to the TBI evaluation team.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>No Delay in Completing an Evaluation:</strong></td>
<td>This option is selected if the TBI evaluation process fell within 30 days of the positive TBI screening.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Clinic Capacity:</strong></td>
<td>This option is selected if your available clinic does not have sufficient appointment time slots to meet the demand.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Delay in Successful Patient Contact:</strong></td>
<td>This option is selected when the clinic makes multiple attempts to contact the patient before successfully establishing contact and scheduling the appointment.</td>
</tr>
<tr class="odd">
<td><strong>Second Attempt to Contact Patient for Scheduling Purposes:</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Unable:</strong></td>
<td>The initial attempt to contact the patient for scheduling needs to occur within 5 days of the receipt of the consultation/referral for a comprehensive TBI evaluation. Two additional attempts must occur within 14 days from the positive screen. If all three attempts to contact the patient within the first 14 days of the positive screen are unsuccessful, a certified letter is sent to the patient providing contact information should they desire to call for an appointment. This letter must be sent within 14 days of the positive screen. All efforts to contact the patient should be documented in the patient’s health record.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Scheduled: Date Offered by Facility:</strong></td>
<td>The patient was successfully contacted and the patient agreed to an appointment scheduled on the date offered by the facility.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Scheduled: Date Requested by Patient:</strong></td>
<td>The patient was successfully contacted and the appointment was made on a date requested by the patient.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Refused:</strong></td>
<td>The patient was successfully contacted for scheduling purposes, but the patient refused the offer of a comprehensive TBI evaluation.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Unavailable:</strong></td>
<td>The patient is not available for scheduling due to reasons beyond their control (e.g., incarceration, death, or redeployment).</td>
</tr>
<tr class="odd">
<td><strong>Second Date Scheduled with TBI Evaluation Team (mm/dd/yyyy):</strong></td>
<td></td>
<td>Corresponds with appointment date for comprehensive TBI evaluation that is scheduled in CPRS/VistA. Value reflects a date range from April 2007 (04/01/2007) to the present date.</td>
</tr>
<tr class="even">
<td><strong>Second Time to Schedule Appointment with TBI Evaluation Team:</strong></td>
<td></td>
<td>Calculated value that is the difference in days between the date of the positive TBI screen and the date of the scheduled appointment with the TBI evaluation team.</td>
</tr>
<tr class="odd">
<td><strong>Second Delay in Completing Evaluation:</strong></td>
<td></td>
<td>Delays in completing a scheduled appointment can occur for a number of reasons. The tracking application defines these delays as:</td>
</tr>
<tr class="even">
<td></td>
<td><strong>No Show</strong></td>
<td>The patient did not show for their scheduled appointment for the comprehensive evaluation.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Cancellation by Patient</strong></td>
<td>The patient cancelled their scheduled appointment for the comprehensive TBI evaluation.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Cancellation by Clinic</strong></td>
<td>The clinic cancelled the scheduled appointment for the comprehensive TBI evaluation. (Note that this response does not justify not completing the evaluation and will create a new entry beginning with the “Contact” fields.)</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Delay in Consult/Referral Submission</strong></td>
<td>The time delay in completing the TBI evaluation was impacted by a delay in submission of the consultation or referral to the TBI evaluation team.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>No Delay in Completing an Evaluation:</strong></td>
<td>This option is selected if the TBI evaluation process fell within 30 days of the positive TBI screening.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Clinic Capacity:</strong></td>
<td>This option is selected if your available clinic does not have sufficient appointment time slots to meet the demand.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Delay in Successful Patient Contact:</strong></td>
<td>This option is selected when the clinic makes multiple attempts to contact the patient before successfully establishing contact and scheduling the appointment.</td>
</tr>
<tr class="odd">
<td><strong>Third Attempt to Contact Patient for Scheduling Purposes:</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Unable:</strong></td>
<td>The initial attempt to contact the patient for scheduling needs to occur within 5 days of the receipt of the consultation/referral for a comprehensive TBI evaluation. Two additional attempts must occur within 14 days from the positive screen. If all three attempts to contact the patient within the first 14 days of the positive screen are unsuccessful, a certified letter is sent to the patient providing contact information should they desire to call for an appointment. This letter must be sent within 14 days of the positive screen. All efforts to contact the patient should be documented in the patient’s health record.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Scheduled: Date Offered by Facility:</strong></td>
<td>The patient was successfully contacted and the patient agreed to an appointment scheduled on the date offered by the facility.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Scheduled: Date Requested by Patient:</strong></td>
<td>The patient was successfully contacted and the appointment was made on a date requested by the patient.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Refused:</strong></td>
<td>The patient was successfully contacted for scheduling purposes, but the patient refused the offer of a comprehensive TBI evaluation.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Unavailable:</strong></td>
<td>The patient is not available for scheduling due to reasons beyond their control (e.g., incarceration, death, or redeployment).</td>
</tr>
<tr class="odd">
<td><strong>Third Date Scheduled with TBI Evaluation Team (mm/dd/yyyy):</strong></td>
<td></td>
<td>Corresponds with appointment date for comprehensive TBI evaluation that is scheduled in CPRS/VistA. Value reflects a date range from April 2007 (04/01/2007) to the present date.</td>
</tr>
<tr class="even">
<td><strong>Third Time to Schedule Appointment with TBI Evaluation Team:</strong></td>
<td></td>
<td>Calculated value that is the difference in days between the date of the positive TBI screen and the date of the scheduled appointment with the TBI evaluation team.</td>
</tr>
<tr class="odd">
<td><strong>Third Delay in Completing Evaluation:</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>No Show</strong></td>
<td>The patient did not show for their scheduled appointment for the comprehensive evaluation.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Cancellation by Patient</strong></td>
<td>The patient cancelled their scheduled appointment for the comprehensive TBI evaluation.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Cancellation by Clinic</strong></td>
<td>The clinic cancelled the scheduled appointment for the comprehensive TBI evaluation. (Note that this response does not justify not completing the evaluation and will create a new entry beginning with the “Contact” fields.)</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Delay in Consult/Referral Submission</strong></td>
<td>The time delay in completing the TBI evaluation was impacted by a delay in submission of the consultation or referral to the TBI evaluation team.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>No Delay in Completing an Evaluation:</strong></td>
<td>This option is selected if the TBI evaluation process fell within 30 days of the positive TBI screening.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Clinic Capacity:</strong></td>
<td>This option is selected if your available clinic does not have sufficient appointment time slots to meet the demand.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Delay in Successful Patient Contact:</strong></td>
<td>This option is selected when the clinic makes multiple attempts to contact the patient before successfully establishing contact and scheduling the appointment.</td>
</tr>
<tr class="odd">
<td><strong>Date Evaluation Completed (mm/dd/yyyy):</strong></td>
<td></td>
<td><p>Entry of date when the comprehensive TBI evaluation was completed by the TBI evaluation team. The calendar provides a date range from April 2007 (04/01/2007) to the present date.</p>
<p>From this entry, the Time to Completed Evaluation value is calculated as the difference in days between the date of the positive TBI screen and the date the TBI evaluation was completed.</p></td>
</tr>
<tr class="even">
<td><strong>Time to Completed Evaluation:</strong></td>
<td></td>
<td>Calculated value that is the difference in days between the date of the positive TBI screen and the date the TBI evaluation was completed.</td>
</tr>
<tr class="odd">
<td><strong>Definitive TBI Diagnosis:</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Yes</strong></td>
<td>Value is a positive response indicating the results of the comprehensive TBI evaluation resulted in a definitive diagnosis of TBI.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>No</strong></td>
<td>Value is a negative response indicating the results of the comprehensive TBI evaluation resulted in a definitive diagnosis of no TBI.</td>
</tr>
<tr class="even">
<td><strong>Responsible TBI Evaluation Team (Service/Clinic):</strong></td>
<td></td>
<td>Response represents the Service/Clinic responsible for completing the TBI evaluation.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>PM&amp;R</strong></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Neurology</strong></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Behavioral Health</strong></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Primary Care With Specialty Training in TBI</strong></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Other</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Status:</strong></td>
<td></td>
<td>In Process</td>
</tr>
</tbody>
</table>

## Completed Referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This change is reflected in the “Breadcrumbs” and in the Status field located at the bottom of the screen’s content area.

Figure 17 shows that the screen’s layout and data fields are identical to the New Referral Records screen. The two main differences involve the highlighted Breadcrumbs and the Status field.

My Tasks \> Referrals \> Completed

![](tbi-version-4-2-user-manual/068.png)To view In Process referrals in the TBI Registry, click on the “My Tasks” tab to view Referrals. Click in the light blue box surrounding the title of this subcategory and the content area of the screen will contain a list of all patients undergoing the second part of the referral process. A referral is an indication that the person was referred for a variety of reasons, typically including the application of the screening tool used in [CPRS](#Glos_CPRS).

Descriptions of all three subcategories of referrals are available in Table 10.

### Completed Referrals Screen Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 13 contains a list of all fields, subfields, and descriptions for the My Tasks \> Referrals \> Completed \> Edit Referral ID: 0000 screen.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 27%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FIELD</strong></th>
<th><strong>SUBFIELD</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Facility:</strong></td>
<td></td>
<td>The facility where the TBI screen was completed.</td>
</tr>
<tr class="even">
<td><strong>Name/SSN# of Patient with Positive Screen and Desiring Eval:</strong></td>
<td></td>
<td>Patient identifier for the OEF/OIF Veteran that had a positive TBI screen and agreed to a comprehensive TBI evaluation.</td>
</tr>
<tr class="odd">
<td><strong>Date of Screening (mm/dd/yyyy):</strong></td>
<td></td>
<td>Date the TBI Screening was completed. The value is listed as a date range from April 2007 (04/01/2007) to the present date.</td>
</tr>
<tr class="even">
<td><strong>Date of Consult/Referral (mm/dd/yyyy):</strong></td>
<td></td>
<td>Date when a consultation was submitted/referral made for the comprehensive TBI evaluation. The value is listed as a date range from April 2007 (04/01/2007) to the present date.</td>
</tr>
<tr class="odd">
<td><strong>Not Applicable:</strong></td>
<td></td>
<td>This is a check box that should be selected when a consultation or referral was not submitted. Selection of this check box will activate the “Other Consult/Referral Status” field for further clarification.</td>
</tr>
<tr class="even">
<td><strong>Other Consult/Referral Status:</strong></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Consult Not Submitted:</strong></td>
<td>The status of this case cannot be moved to “Completed” until appropriate action has been taken and indicated on the Web application.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Evaluation without Referral/Consult:</strong></td>
<td>This option should be selected when the comprehensive TBI evaluation was completed without submission of a consultation or the making of a referral due to facility practice patterns.</td>
</tr>
<tr class="odd">
<td><strong>Attempts to Contact Patient for Scheduling Purposes:</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Unable:</strong></td>
<td>The initial attempt to contact the patient for scheduling had to occur within 5 days of the receipt of the consultation/referral for a comprehensive TBI evaluation. Two additional attempts occurred within 14 days from the positive screen. If all three attempts to contact the patient within the first 14 days of the positive screen were unsuccessful, a certified letter was sent to the patient providing contact information should they ever desire to call for an appointment. This letter was sent within 14 days of the positive screen. All efforts to contact the patient would be documented in the patient’s health record.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Scheduled: Date Offered by Facility:</strong></td>
<td>The patient was successfully contacted and the patient agreed to an appointment scheduled on the date offered by the facility.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Scheduled: Date Requested by Patient:</strong></td>
<td>The patient was successfully contacted and the appointment was made on a date requested by the patient.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Refused:</strong></td>
<td>The patient was successfully contacted for scheduling purposes, but the patient refused the offer of a comprehensive TBI evaluation.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Unavailable:</strong></td>
<td>The patient was not available for scheduling due to reasons beyond their control (e.g., incarceration, death, or redeployment).</td>
</tr>
<tr class="odd">
<td><strong>Date Scheduled with TBI Evaluation Team (mm/dd/yyyy)</strong></td>
<td></td>
<td>Corresponds with appointment date for comprehensive TBI evaluation that was scheduled in CPRS/VistA. Value reflects a date range from April 2007 (04/01/2007) to the present date.</td>
</tr>
<tr class="even">
<td><strong>Time to Scheduled Appointment with TBI Evaluation Team:</strong></td>
<td></td>
<td>Calculated value that is the difference in days between the date of the positive TBI screen and the date of the scheduled appointment with the TBI evaluation team.</td>
</tr>
<tr class="odd">
<td><strong>Delay in Completing Evaluation:</strong></td>
<td></td>
<td>Delays in completing a scheduled appointment can occur for a number of reasons. The tracking application defines these delays as:</td>
</tr>
<tr class="even">
<td></td>
<td><strong>No Show:</strong></td>
<td>The patient did not show for their scheduled appointment for the comprehensive evaluation.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Cancellation by Patient:</strong></td>
<td>The patient cancelled their scheduled appointment for the comprehensive TBI evaluation.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Cancellation by Clinic:</strong></td>
<td>The clinic cancelled the scheduled appointment for the comprehensive TBI evaluation. (Note that this response does not justify not completing the evaluation and would have created a new entry beginning with the “Contact” fields.)</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Delay in Consult/Referral Submission:</strong></td>
<td>The time delay in completing the TBI evaluation was impacted by a delay in submission of the consultation or referral to the TBI evaluation team.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>No Delay in Completing an Evaluation:</strong></td>
<td>This option was selected if the TBI evaluation process fell within 30 days of the positive TBI screening.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Clinic Capacity:</strong></td>
<td>This option was selected if the available clinic did not have sufficient appointment time slots to meet the demand.</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Delay in Successful Patient Contact:</strong></td>
<td>This option was selected when the clinic made multiple attempts to contact the patient before successfully establishing contact and scheduling the appointment.</td>
</tr>
<tr class="odd">
<td><strong>Date Evaluation Completed (mm/dd/yyyy)</strong></td>
<td></td>
<td><p>Entry of date when the comprehensive TBI evaluation was completed by the TBI evaluation team. The calendar provides a date range from April 2007 (04/01/2007) to the present date..</p>
<p>From this entry, the Time to Completed Evaluation value was calculated as the difference in days between the date of the positive TBI screen and the date the TBI evaluation was completed.</p></td>
</tr>
<tr class="even">
<td><strong>Time to Completed Evaluation:</strong></td>
<td></td>
<td>Calculated value that is the difference in days between the date of the positive TBI screen and the date the TBI evaluation was completed.</td>
</tr>
<tr class="odd">
<td><strong>Definitive TBI Diagnosis:</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Yes</strong></td>
<td>Response indicating positive results of the comprehensive TBI evaluation resulting in a definitive diagnosis of TBI.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>No</strong></td>
<td>Response indicating negative results of the comprehensive TBI evaluation resulting in a definitive diagnosis of no TBI.</td>
</tr>
<tr class="even">
<td><strong>Responsible TBI Evaluation Team (Service/Clinic):</strong></td>
<td></td>
<td>Response represents the Service/Clinic that was responsible for completing the TBI evaluation.</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>PM&amp;R</strong></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Neurology</strong></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Behavioral Health</strong></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Primary Care With Specialty Training in TBI</strong></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Other</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Status:</strong></td>
<td></td>
<td>Completed</td>
</tr>
</tbody>
</table>

Part D. Using the Polytrauma Entries Application

# Polytrauma Entries Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Polytrauma Entries application allows the case manager to track patients with multiple injuries. These injuries may be multiple traumatic brain injuries or injuries elsewhere on the body that are not traumatic brain injuries. There are no reporting options for this application. It is designed simply to track Veterans with multiple traumas.

To begin, click on the tab “My Tasks” and then on the link “Add New.” Enter the patient’s Social Security Number (SSN) and/or the Patient Last Name (see Figure 20).

![](tbi-version-4-2-user-manual/069.png)

<span id="_Ref268521291" class="anchor"></span>Figure 20 – Adding a New Polytrauma Patient

Continue to fill in the following fields: Address Line 1, Address Line 2, City, County, State, Country, Postal Code, Home Phone, E-mail Address, Home Veterans Affairs Medical Center (VAMC), Military Service Branch, Military Duty Status, and Military Discharge Status (see Figure 21).

![](tbi-version-4-2-user-manual/070.png)

<span id="_Ref268521556" class="anchor"></span>Figure 21 – Adding Polytrauma Patient Data

Additional tracking information includes the MTF source and tracking information fields, including Injury Date, Combat Location, Blast Explosion, Vehicle Injury, Bullet Injury, Other Injury, and Other Injury Description. These fields have drop-down lists for you to select a value. The Date fields allow you to enter the date in the dd/mm/yyyy format or you can click on the calendar icon and select a date from the calendar that displays (see Figure 22).

![](tbi-version-4-2-user-manual/071.png)

<span id="_Ref268521646" class="anchor"></span>Figure 22 – Adding Polytrauma Patient Tracking Data

Beneath that is another group of check boxes under Injury Details. These include: Brain Injury, Eye Injury/Visual Impairment, Soft Tissue/Orthopedic Injuries, Nerve Injuries, Burns, Amputation, Gastro-Intestinal/Bowel, Cardiovascular Injury, Infection, Fractures, Wounds/Shrapnel, Ear Injury/Hearing, Lung Injuries, Behavioral Health Conditions, Spinal Cord Injury, Internal Organ/Other, Pain, and Other (see Figure 23).

![](tbi-version-4-2-user-manual/072.png)

<span id="_Ref268521718" class="anchor"></span>Figure 23 - Adding Polytrauma Injury Details

In the Treatment section, enter Provider Information. Fields in this section include: Provider Location, ID Number, Name, E-mail, Polytrauma VAMC, Admission Functional Independence Measure (FIM) Code, Admission Date, Functional Related Group (FRG) Code, Discharge FIM Code, Rehab Discharge Date, Discharged To, and Follow up. Under Follow up the options are Ortho, Physical Therapy (PT), Neurology, <u>Speech-language Pathologists (</u>SLP), Physiatry, Community Re-entry, Occupational Therapy (OT), and Vocational Rehabilitation and Employment (VR&E) Assessment, and Follow up Site. The Date fields allow you to enter a date in the dd/mm/yyyy format or you can click on the calendar icon and select a date from the calendar that displays.

| ![](tbi-version-4-2-user-manual/073.png) | Note: A FIM score is a scoring mechanism used to indicate the level of functioning and support needed for an individual patient. The smaller the score (18 is the minimum score), the worse the injury. FIM codes are established for 18 different functional tasks. |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](tbi-version-4-2-user-manual/074.png) | Note: The discharge date can be the current date, if applicable or a date in the past (if the case manager is catching up on the records). |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|

Polytrauma patients are specific to four specialized medical centers: Richmond Veterans Affairs Medical Center (VAMC), James A. Haley Veterans Hospital (Tampa, FL), Palo Alto Health Care System – Palo Alto Division, and the Minneapolis VAMC. A fifth Polytrauma Rehabilitation Center is scheduled to open in FY12 at the South Texas Health Care System – San Antonio Division (see Figure 24).

![](tbi-version-4-2-user-manual/075.png)

<span id="_Ref268522040" class="anchor"></span>Figure 24 – Adding Polytrauma Treatment Data

Enter values in the Admission FIM Code, the Admission Date, the FRG Code, the Discharge FIM Code, and the Rehab Discharge Date fields. The Date fields allow you to input the date in the dd/mm/yyyy format or you can click on the calendar icon and select a date from the calendar that displays (see Figure 25).

![](tbi-version-4-2-user-manual/076.png)

<span id="_Ref268522097" class="anchor"></span>Figure 25 – Adding Admission and Discharge Data

The Discharged To field is a drop-down list of possibilities. Make a selection from this field (see Figure 26).

![](tbi-version-4-2-user-manual/077.png)

<span id="_Ref268522324" class="anchor"></span>Figure 26 – Adding Discharge to Data

The follow-up Clinical Needs section of the graphical user interface (GUI) requires the case manager to select from the following check boxes:

- Ortho
- Neurology
- Psychiatry
- OT
- IPT
- SLP
- Community Re-entry
- VR&E Assessment
- Other

Then there is a Follow-up Site Description text field where notations can be entered. Finally, the editable text fields of the Follow-up Provider Information section of the GUI are:

- Follow-up Polytrauma Case Manager
- Location
- Phone
- Email

Then the case manager can click the Save button to save the edits or click the Close button to close without saving the changes (see ![](tbi-version-4-2-user-manual/078.png)

Figure 27).

![](tbi-version-4-2-user-manual/079.png)

<span id="_Toc423685669" class="anchor"></span>Figure 27 – Completing Polytrauma Patient Entry

Part E. Using the TBI and Polytrauma  
Patient Lookup Application

# TBI and Polytrauma Patient Lookup Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To protect the privacy of TBI Registry patients, both actual Social Security Numbers (SSNs) and stand-in (called PseudoSSNs) numbers are used in TBI Registry applications. PseudoSSNs are identified by the use of three zeros for the first three numbers of the nine-digit SSN (for example: 000-03-2857) or the use of the letter “P” (for “Pseudo”) as a suffix of a SSN (for example: 242-59-9250P).

## TBI Patients Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a search of the Registry for TBI patients:

1.  Click the Patient tab to open the PATIENTS \> TBI PATIENTS screen.

> Note that the task, TBI Patients, located in the Left Navigation bar, is highlighted by a light blue box (see Figure 28).

> You can initiate a search by providing either the patient’s Social Security Number (SSN) or PseudoSSN or the patient’s name.

2.  Type the patient’s SSN or PseudoSSN or the patient’s name in the appropriate text boxes.
3.  ![](tbi-version-4-2-user-manual/080.png)![](tbi-version-4-2-user-manual/081.png)Click the Search button located at the bottom of the screen.

<span id="_Ref265008827" class="anchor"></span>Figure 28 – TBI Patients Lookup Screen

> ![](tbi-version-4-2-user-manual/082.png)If the search was successful, you can view the patient’s data in the results panel located at the bottom of the screen (see Figure 29).

<span id="_Ref265012099" class="anchor"></span>Figure 29 – TBI Patients Search Results Screen

4.  Click the View box located on the extreme left of the results panel to view the Patient Information screen.

You can review detailed information for the patient (see Figure 30).

<span id="_Ref265013314" class="anchor"></span>Figure 30 - TBI Patient Information Screen

5.  ![](tbi-version-4-2-user-manual/083.png)Click on the word, <u>View</u> in the View Patient Health Factors panel (located at the bottom of the Patient Information screen, see Figure 30), to generate a TBI Health Factor Search Report (see Figure 31).

<span id="_Ref265014605" class="anchor"></span>Figure 31 – TBI Health Factor Search Report

> ![](tbi-version-4-2-user-manual/084.png)Click the arrow on the “Select a format” drop-down menu (located on the task bar underneath the Breadcrumbs bar, see Figure 32 to select a format for exporting the report if you need to create an electronic copy.

> The “Select a format” drop-down menu offers two options: and Acrobat PDF file or Excel.

6.  Click “Acrobat (PDF) file” to select it and then click “Export.”

> A File Download window appears with options to Open, Save, or Cancel the file (see Figure 33).

7.  Click the Save button and a Save As window appears (see Figure 34).
8.  Choose a destination for the file and click the Save button. The Download complete window appears (Figure 35).
9.  Click the Open button to view the report or the Close button to close the PDF file.

<span id="_Ref265015953" class="anchor"></span>Figure 32 – Export TBI Health Factor Search Report

![](tbi-version-4-2-user-manual/085.png)

<span id="_Ref265019049" class="anchor"></span>Figure 33 – File Download Window![](tbi-version-4-2-user-manual/086.png)

![](tbi-version-4-2-user-manual/087.png)<span id="_Toc423685676" class="anchor"></span>Figure 34 – Save as Window

<span id="_Ref265019152" class="anchor"></span>Figure 35 – TBI Search Report Download Complete Window![](tbi-version-4-2-user-manual/088.png)

> If you have access to the TBI Referrals application, you can use the Edit box (located at the bottom of the Patient Information screen) to access the task screen to edit the patient’s referrals record.

10. Navigate to the Patient Information screen and click Edit (see Figure 36).

> The My Tasks \> Referrals \> New \> Edit Referral ID: 1431 screen will open (see Figure 37).

11. Use the steps located in Section Editing a New Referral Record to update the data in this Referral screen (see Figure 37).

<span id="_Ref265022245" class="anchor"></span>Figure 36 – TBI Edit Referral ID Screen![](tbi-version-4-2-user-manual/089.png)

<span id="_Ref265022370" class="anchor"></span>Figure 37 – Edit Referral ID: 1431![](tbi-version-4-2-user-manual/090.png)

## Polytrauma Patients Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a search of the Registry for TBI Polytrauma patients:

1.  Click the Patient tab to open the PATIENTS \> POLYTRAUMA PATIENTS screen.

> Note that the task, Polytrauma Patients, located in the Left Navigation bar, is highlighted by a light blue box (see Figure 28).

> You can initiate a search by typing in a time range in the appropriate text boxes.

2.  Type in a time range in the Injury Date From (mm/dd/yyyy) and the Injury Date To (mm/dd/yyyy) text boxes.
3.  Click the arrow on the “VISN:” drop-down menu located at the bottom of the screen.
4.  Click on a VISN option in the drop-down menu to select it.
5.  Click the Search button located at the bottom of the screen.

<span id="_Toc268528394" class="anchor"></span>Figure 38 – Polytrauma Patients Lookup Screen![](tbi-version-4-2-user-manual/091.png)

> If the search was successful or unsuccessful, you can view the patient in the results panel located at the bottom of the screen (see Figure 39).

> If this search had been successful, you could have viewed the Polytrauma Patient Information by following steps similar to those in Section 9.1 TBI Patients Lookup.

![](tbi-version-4-2-user-manual/092.png)<span id="_Toc423685681" class="anchor"></span>Figure 39 – Polytrauma Lookup Patients Results

Part F. Using the Reports Application

# Reports Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## BI Office

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BI Office from Pyramid Analytics (PA) is the VA's reporting and analytics platform, intended to replace the older proClarity product (which is no longer supported by Microsoft). BI Office is a fully web-based platform that supports decision-making and data analysis through interactive reports and dashboards as well as print-ready publications and data-based alerting. The VA Business Intelligence Service Line (BISL) maintains an area in the VA Pulse environment to view training webinars, ask questions and provides information regarding BI Office.

<https://www.vapulse.net/login.jspa?referer=%252Fcommunity%252Fbusiness-intelligence-service-line-bisl%252Fpyramid-analytics>

A large number of users have already been granted access to PA however, should users need to be granted there is a self-enrollment portal at <https://vaww.dwh.cdw.portal.va.gov/TechTeam/SSAS/SitePages/Pyramid_Access.aspx> .

![](tbi-version-4-2-user-manual/093.png)

<span id="_Toc423685682" class="anchor"></span>Figure 40 – Pyramid Analytics Access

Once enrolled users will be able to access the help and training available at <https://www.vapulse.net> and in the [TBI Reporting Dashboard](https://bioffice.pa.cdw.va.gov/default.aspx?bookid=50b8a48c-0265-4f8e-8d79-eeccc2a851ef|ispasFalse|report842c94d0-a442-4443-9d24-8a368ca3b4a7|ws1|wsb0|isDisabledAnalyticsFalse|isDashboardPanelOnTrue).

## Cube Data Model

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Measurements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Distinct Patients
2.  Completed Surveys
3.  Basic Score Count
4.  Avg Basic Score
5.  Advanced Score Count
6.  Avg Advanced Score
7.  Cognitive Count
8.  Avg Cognitive Score
9.  Emotional Count
10. Avg Emotional Score
11. Sensory Somatic Count
12. Avg Sensory Somatic Score
13. Vestibular Count
14. Avg Vestibular Score
15. Total Score Count
16. Avg Total Score
17. T Score Below 61 Count
18. Avg T Score Below 61
19. T Score Count
20. Avg Total T Score
21. T Score Over 60 Count
22. Avg T Score Over 60

Dimensions

1.  Age Group
    1.  Hierarchies – None
    2.  Attributes
        1.  Age Group Key
        2.  Age Group
2.  Providers
    1.  Hierarchies – None
    2.  Attributes
        1.  Provider ID
        2.  Full Name
3.  Institutions
    1.  Hierarchies
        1.  Institutions: VISNVISTANAMEFacility Name
    2.  Attributes
1.  Institution Key
2.  Institution ID
3.  Display Name
    1.  VISN
4.  VISTAName
    1.  Institution Name
    2.  Station Number
4.  Patients
    1.  Attributes
        1.  Patient ICN
        2.  SSN
        3.  Service Branch
        4.  Full Name
        5.  Gender
        6.  Ethnicity
        7.  Race
        8.  OEF OIF Roster
        9.  Last Service Separation Date
        10. Marital Status
5.  Survey Details
    1.  Hierarchies – None
    2.  Attributes
        1.  Choice Name
        2.  Choice Text
        3.  Question Number
        4.  Question Text
        5.  Survey Name
6.  Survey Type
    1.  Attributes
        1.  Survey Name
        2.  

## SSRS Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There remain three SSRS reports which were left for convenience to the clinician, on the landing page from CPRS under the SSN text box there are two buttons ‘View Last Three Instruments’ and ‘View All Instruments’ which link to reports for either the last three instruments on record or all of the instruments on record for that specific patient.

![](tbi-version-4-2-user-manual/094.png)

<span id="_Toc423685683" class="anchor"></span>Figure 41 – View Last Three and View All Instruments

By clicking either on either the “View Last Three Instruments” button or the “View All Instruments” button (as shown in Figure 41 above) will bring up a report with the list of the Instruments, either the last three or all of the instruments for the patient selected.

![](tbi-version-4-2-user-manual/095.png)

<span id="_Toc423685684" class="anchor"></span>Figure 42 – List of Instruments

By clicking on the “View Notes” link (as shown in Figure 42 above), the details of the instrument you selected to view will be displayed on the screen.

Both the “View Last Three Instruments” page and the “View All Instruments” Page offer a Standard Title Bar that can be used to Zoom, Search, Export, Refresh and Print Data from the pages. When on the View Notes Pages a left hand arrow \<- is enabled which allows the User to go back to the previous page versus the TBI Landing page.

![](tbi-version-4-2-user-manual/096.png)

<span id="_Toc423685685" class="anchor"></span>Figure 43 – Title Bar

The large ![](tbi-version-4-2-user-manual/097.png) Back Button on the bottom of the pages always returns the user to the TBI Landing page in which they will need to re-type in the patients Social Security Number to search for Instruments once again. In Figure 44 below is an example of the output that the View Notes page will display.

![](tbi-version-4-2-user-manual/098.png)

<span id="_Toc423685686" class="anchor"></span>Figure 44 – View Notes Page

Part G. Using the User Administration Application

# User Administration Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Administration Application allows an administrator to view, edit, and sort user roles. The administrator is a global role that is not specific to any facility. The administrator can do anything in the TBI Registry except create the reports (reports are created by Reporting role users only).

At <span class="smallcaps">Administration \> List Users</span>, a list displays on the GUI.

![](tbi-version-4-2-user-manual/099.png)

<span id="_Toc268528400" class="anchor"></span>Figure 45 – Administration \> List Users Screen

You can download the list to Excel using the “Download to Excel” button at the bottom of the <span class="smallcaps">List All User/Roles</span> screen.

![](tbi-version-4-2-user-manual/100.png)

<span id="_Toc268528401" class="anchor"></span>Figure 46 – List all User Roles

You can also select Edit User ID to make edits to User IDs. The editable fields are text fields.

![](tbi-version-4-2-user-manual/101.png)

<span id="_Toc268528402" class="anchor"></span>Figure 47 – Edit Users IDs Screen

## Role Administration Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Role Administration Application allows the administrator to select Edit User Roles and then complete fields on the GUI to edit the user’s roles.

First go to <span class="smallcaps">Administration \> Add/Edit Users \> Add New User</span> to add a new user.

![](tbi-version-4-2-user-manual/102.png)

<span id="_Toc268528403" class="anchor"></span>Figure 48 – Add New User Screen

Go to the Edit User Roles Information to edit the user’s roles.

Once a Veteran’s information is entered in the Polytrauma Application, those records can be viewed and edited. To do this, go to <span class="smallcaps">My Tasks \> Polytrauma \> View / Edit</span>.

![](tbi-version-4-2-user-manual/103.png)

<span id="_Toc268528404" class="anchor"></span>Figure 49 - Polytrauma View/Edit Users Screen

Roles can be edited using the drop-down lists and check boxes provided. The editable fields in the Roles section of the GUI are:

- TBI Administrator (drop-down list with VISN Access)
- TBI Editor (drop-down list with VISN Access)
- TBI Read Only (drop-down list with VISN Access)
- TBI Polytrauma Editor (drop-down list with VISN Access)
- TBI Polytrauma Read Only (drop-down list with VISN Access)
- TBI Reporting User National (drop-down list with VISN Access)
- TBI Reporting User VISN (drop-down list with VISN Access)
- TBI Reporting User Station (drop-down list with VISN Access)

Then click Save to save the changes or click Close to close the GUI without saving.

![](tbi-version-4-2-user-manual/104.png)

<span id="_Toc268528405" class="anchor"></span>Figure 50 – Edit Roles Screen

There is also a TBI Read Only option.

| ![](tbi-version-4-2-user-manual/105.png) | Note: For Read Only access, all the fields are grayed out. |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|

![](tbi-version-4-2-user-manual/106.png)

<span id="_Toc268528406" class="anchor"></span>Figure 51 – Assigning VISN Access Screen

Select the VISN Access and TBI Reporting User Station.

![](tbi-version-4-2-user-manual/107.png)

<span id="_Toc423685694" class="anchor"></span>Figure 52 – TBI Reporting User Station

Select User Roles from the drop-down list provided.

![](tbi-version-4-2-user-manual/108.png)

<span id="_Toc268528407" class="anchor"></span>Figure 53 – Station Access Screen

Using the task bar to the far left of the screen, the case manager can also use the Role Administration application to list users:

![](tbi-version-4-2-user-manual/109.png)

<span id="_Toc268528408" class="anchor"></span>Figure 54 – Role Administration Screen

There is a search function text box, with Search and Clear buttons to the right of the field.

Add New User:

![](tbi-version-4-2-user-manual/110.png)

<span id="_Toc268528409" class="anchor"></span>Figure 55 – Add New User Screen

List All User/Roles:

![](tbi-version-4-2-user-manual/111.png)

<span id="_Toc423685698" class="anchor"></span>Figure 56 – List All User/Roles Screen  

Part G. About the TBI Interface

# About the TBI Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Graphical User Interface (GUI) Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TBI uses a GUI similar to those used in many Microsoft Windows<sup>®</sup> or Apple Macintosh<sup>®</sup> programs. If you have already used programs with these screens, the TBI GUI will seem familiar to you. TBI is only implemented on the Microsoft Windows platform at this time.

If you have little or no familiarity with the Microsoft Windows GUI environment, information can be found by accessing the Microsoft Windows Help file.

### Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An “application window” is the area on your computer screen the program uses. If you have more than one program running at the same time, you can go from one program to another by clicking in each application window. You can also move, close, or minimize the application window to make room for another window. (See Help in Windows for further instructions on these functions.)

### Pop-up Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These are “miniature” windows that pop up within a window to provide or request information. Ordinarily, they require some action before they will disappear. Clicking on buttons with the words \[OK\], \[Cancel\], or \[Exit\], or something similar, usually closes these windows.

### Windows GUI Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe typical Windows GUI elements used in TBI’s applications.

#### Text Box

Type the desired characters into the edit box. The selected entry will not be effective until you tab away from or otherwise exit the text box.

#### Checkbox

A checkbox toggles between a YES/NO, ON/OFF setting. It is usually a square box containing a check mark  or X. Clicking the box or pressing the spacebar toggles the checkbox setting. In some instances, checkboxes may be used to provide more than one choice; in such cases, more than one box can be selected.

#### Radio Button

A radio button, also known as an option button, is a small, hollow circle adjacent to text. Radio buttons appear in sets. Each button represents a single choice and normally only one button may be selected at any one time. Clicking on the radio button places a solid dot in the circle, selecting the option. Clicking a selected radio button de-selects it, removing the dot. As one radio button is selected, others within the category switch off. For example, Male or Female may be offered as choices through two radio buttons.

#### Command Buttons and Command Icons

A command button initiates an action. It is a rectangular shape with a label that specifies what action will be performed when the button is clicked. A common example is the search key. ![](tbi-version-4-2-user-manual/112.png)

#### Data Fields

The date field is identified by “\_\_/\_\_/\_\_” or a date “mm/dd/yyyy” and will usually have an associated Pop-up Calendar (see Pop-up Calendars). The month and day components of the date must consist of two digits and the year must consist of four digits (i.e., 02/02/1996). The selected entry will not be effective until you tab off or exit from the date field.

#### Drop-down List

A drop-down list is displayed as a box with an arrow button on the right side. Such boxes usually display one entry at a time. Choose from a vertical list of choices that display when you click the downward arrow. Select the entry you want by clicking the list entry.

#### Keyboard Commands

Keyboard commands can be used throughout the TBI application by pressing and holding the \<Alt\> key and then pressing the appropriate key to perform the command. The key to press in order to perform the command is identified by an underlined character on the screen. For example, the Task Manager tab can be displayed by pressing and holding the \<Alt\> key and then pressing the \<T\> key.

Keyboard keys and onscreen buttons are shown in different style brackets throughout this manual to differentiate them from on-screen buttons or menu options: \<Ctrl\> and \<Enter\> are on the keyboard, \[Close\] is a command button or icon on the screen.

#### Tab Key

Use the \<Tab\> key or the mouse to move between fields. Do *not* use the \<Enter\> or \<Return\> key, which is usually reserved for the default command button or action.

#### Text Box

Type the desired characters into the edit box. The selected entry will not be effective until you tab away from or otherwise exit from the text box.

#### Changing (Resizing) a Window

Most windows and columns displayed in the TBI application can be resized. To change the size of a window, position the mouse pointer over the right edge of the column or the outside edge of the window, left click, and while holding the mouse button down, move the mouse and “drag” to change the size of the window or column. Position the mouse pointer over one corner and drag diagonally to increase the size of the entire window.

#### Cancel

When used in a prompt, \[Cancel\] allows you to cancel the action about to be taken. For example, when closing an application, you may be prompted to validate the action to close. If you click the \[Cancel\] button, the application will not close and you will resume from the point at which the close action was initiated.

#### Close

This command closes the active window.

#### Edit

This command is used to edit information.

#### Run Report

Run Report is a command button found in the upper left portion of the screens that allows you to run the report based on the parameters selected in the GUI.

#### Save

Saves all changes made since the last save action. If you attempt to save and all required fields have not yet been completed, you will receive a notification that the required fields must be completed before saving.

#### Save As

This command is used to export to a file a report produced in TBI. With the report open, clicking on the Save As menu option will produce a window labeled “Save the report as” in which you will indicated the file location where you wish to store the report. You will need to name the file and choose the format in which it will be saved.

#### Search

After at least one character is typed in a lookup dialog box, clicking the \[Search\] button will bring up matching entries.

#### Selecting Multiple Items from a Drop-down List

A variety of lists are displayed throughout the TBI application from which you can select one or more items.

To select all items in a range between two separate entries, hold the \<Shift\> key and click on the first item in the range, and then click the last item in the range. All of the items between the first and last will be highlighted.

To select multiple separate entries from a list, hold the \<Ctrl\> key and click each of the items you want to select.

#### Undo

Reverses all changes made since the last save action and redisplays the original data.

#### Right-click Menus

Most Windows-based XE “Windows about right-click menus” applications provide some sort of pull-down menu when you click the right mouse button over a GUI XE “GUI right click menu options” element.

Part H. Appendices

# Standard Web Browser Shortcut Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the following table, two or more keys connected by a comma (,) indicate that the keys should be pressed in succession. Keys connected by a plus sign (+) indicate that the keys should be pressed at the same time. These keys can be used while running DSSA in a Web browser.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 0%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">BROWSER OPTION</th>
<th colspan="2">SHORTCUT</th>
<th>IE</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Bookmark menu</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; B &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Bookmark, new (for current page)</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; D &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Browser window, new</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; N &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Browser window, close</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; + &lt; F4 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>*</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Close browser window</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; + &lt; F4 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>*</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Exit browser</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; + &lt; F4 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>*</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Find [on the page displayed]</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; F &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Help</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>&lt; F1 &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Location in history, go to next</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; + &lt; &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>&lt; Space &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Location in history, go to previous</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; + &lt; &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>&lt; Backspace &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Location, open</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; L &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Home page, go to</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; + &lt; Home &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>New browser window</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; N &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Open location</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; L &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Print…</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; , &lt; F &gt; , &lt; P &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select All [on the page displayed]</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; A &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Tab, close</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; W &gt;</p>
</blockquote></td>
<td><blockquote>
<p>n/a*</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tab, open new</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; T &gt;</p>
</blockquote></td>
<td><blockquote>
<p>n/a*</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="6"><blockquote>
<p>Window management</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;R&gt;</p>
</blockquote></td>
<td><blockquote>
<p>(restore)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;M&gt;</p>
</blockquote></td>
<td><blockquote>
<p>(move)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;S&gt;</p>
</blockquote></td>
<td><blockquote>
<p>(size)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;N&gt;</p>
</blockquote></td>
<td><blockquote>
<p>(minimize)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;X&gt;</p>
</blockquote></td>
<td><blockquote>
<p>(maximize)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;C&gt;</p>
</blockquote></td>
<td><blockquote>
<p>(close)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p>* In versions prior to 8.0 (not currently authorized for VA use, and not tested with the application)</p>
</blockquote></td>
</tr>
</tbody>
</table>

# VA Approved Internet Browsers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following VA-approved browsers have been tested for use with DSSA and are believed to be fully functional. If you encounter unusual problems, please submit a Remedy report and/or consult with your local IRM.

| BROWSER                       | VERSION(S) | REMARKS                          |
|-------------------------------|------------|----------------------------------|
| Microsoft® Internet Explorer® | 6.x, 7.x   | Does not support tabbed browsing |
|                               |            |                                  |

# Web-based Application Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Web Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In a Web-based application, a “page” is the specific area on your computer screen used by a program. You might start on a launch page, for example, and use the menus available to you to move to another, more specific task-oriented page. If you have more than one browser window running at the same time, you can go from one window to another by clicking in each of those windows or by using [\< Alt \>+\< Tab \>](#Glos_AltTab). You can also move, close, or minimize the application window to make room for another window (see Changing (Resizing) a Browser Window for further instructions on these functions).

# # Pop-up Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These are windows that pop up within (or on top of) a window to provide or request information. They require a response before they will close. Clicking buttons with the words \[OK\], \[Cancel\], \[Exit\], or by pressing the \< Esc \> key closes these windows.

# # Web-based Application (WBA) Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe typical WBA elements.

# Text Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SAMPLES: | 1                                                                                                     | 2                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
|          | ![](tbi-version-4-2-user-manual/113.png) | ![](tbi-version-4-2-user-manual/114.png) |

Note how the appearance of the box changes: from a plain line border (SAMPLE 1) to an almost three-dimensional, pale yellow-highlighted field when you tab to it or click in it (SAMPLE 2).

Type your entry into the text box. The entry will not be saved until you tab away from or otherwise exit from the text box. In cases where the format of your entry is important, a sample will appear near the box. The relative width of these boxes is usually a reflection of the number of characters you are allowed to enter. Sometimes (as with date fields) there may also be a “date picker” next to the field.

You should see a “tool tip” pop up when you hover your mouse pointer over the text box.

![](tbi-version-4-2-user-manual/115.png)

<span id="_Toc263150463" class="anchor"></span>Figure 57 – Tool Tip for Text Box

# Checkbox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAMPLE: ![](tbi-version-4-2-user-manual/116.png)

A checkbox “toggles” (changes) between a YES / NO, ON / OFF setting. It is typically a square box which can contain a check mark ![](tbi-version-4-2-user-manual/117.png) or an “X” ☒ and is usually accompanied by text. Clicking the box or tabbing to the field and pressing the spacebar toggles the checkbox setting. In some instances, checkboxes may be used to provide more than one choice; in such cases, more than one box can be selected. Sometimes, a pre-determined “default” entry will be made for you in a checkbox; you can change the default if needed.

# Radio Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAMPLE: ![](tbi-version-4-2-user-manual/118.png)

A radio button, also known as an option button, is a small, hollow circle adjacent to text. Radio buttons usually appear in sets, with each button representing a single choice; normally, only one button in the set may be selected at any one time. Clicking on the radio button places a solid dot in the circle, selecting the option. Clicking a selected radio button de-selects it, removing the dot. As one radio button is selected, others within the category switch off. For example, Male or Female may be offered as choices through two radio buttons, but you can only select one of the choices.

# Command Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SAMPLES</p>
<p>![](tbi-version-4-2-user-manual/119.png)</p>
<p>![](tbi-version-4-2-user-manual/120.png)</p></th>
<th><p>A command button initiates an action. It is a rectangular “3-dimensional” shape with a label that specifies what action will be performed when the button is clicked. Common examples are shown at left. Command buttons that end with three dots indicate that selecting the command may evoke a subsidiary window.</p>
<p>In the text of this document, command button names appear inside square brackets. <em>Examples:</em> [Search], [Save].</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](tbi-version-4-2-user-manual/121.png)</td>
<td>The [Cancel] command allows you to cancel the action about to be taken, or to discard changes made on a form. For example, when closing an application, you may be prompted to validate the action to close. If you click the [Cancel] button, the application will not close and you will resume from the point at which the close action was initiated. Or, on a data screen, you may use the [Cancel] button to discard any changes you may have made to the data and close the tab.</td>
</tr>
<tr class="even">
<td>![](tbi-version-4-2-user-manual/122.png)</td>
<td>The [Select] command is used to select records for editing.</td>
</tr>
<tr class="odd">
<td>![](tbi-version-4-2-user-manual/123.png)</td>
<td>The [Search] command is used to find one or more records. When at least one character is typed in a lookup dialog box, clicking the [Search] button will bring up matching entries. In many cases, leaving the lookup box blank will find all such records. Enter the search string and click [Search]<strong>.</strong> Searches are case-insensitive and use “contains” logic.</td>
</tr>
<tr class="even">
<td>![](tbi-version-4-2-user-manual/124.png)</td>
<td>The [OK] command is used to accept a default choice, or to agree with performing an action.</td>
</tr>
<tr class="odd">
<td><p>![](tbi-version-4-2-user-manual/125.png)</p>
<p>![](tbi-version-4-2-user-manual/126.png)</p></td>
<td>Other command buttons may be unique to a specific screen. For example, the [Clear Triage] button is used when editing a Referral record and you wish to “clear” (or undo) the triage decision just made. These buttons are described under the discussion of the individual screen(s) to which they apply.</td>
</tr>
</tbody>
</table>

# Date Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAMPLE: ![](tbi-version-4-2-user-manual/127.png)

Date fields are identified by their labels, but otherwise look like an ordinary text field. They may have an associated popup calendar. The month and day components of the date may consist of one or two digits and the year must consist of four digits (*e.g.*, 07/27/2007). You may use either slashes (/) or dashes (-) to separate the month, day and year. The selected entry will not be effective until you tab away from or otherwise exit the date field; at that point, the year will be reformatted, if necessary, to four digits; likewise, if you use dashes as separators, they will be converted to slashes.

# Drop-down List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SAMPLE 1: | ![](tbi-version-4-2-user-manual/128.png) |
|-----------|-------------------------------------------------------------------------------------------------------|
| SAMPLE 2: | ![](tbi-version-4-2-user-manual/129.png) |

A drop-down list (sometimes called a “pull-down” list) is displayed as a box with an arrow button on the right side (SAMPLE 1). Such a list allows you to select one item from the list. The current choice (or a prompt) is visible in a small rectangle; when you click on the arrow, a list of items is revealed (SAMPLE 2). Click on one of the entries to make it your choice; the list disappears.

To select multiple items from a drop-down list, first pick one item or a value from the drop-down list and click the \[Add\] button. To add an additional item from the drop-down list, choose that item from the drop-down and again click \[Add\].

![](tbi-version-4-2-user-manual/130.png)

# List Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAMPLE: ![](tbi-version-4-2-user-manual/131.png)

The list box shows a list of items. If more items exist than can be seen in the box, a scroll bar appears on the side of the box. Click the desired entry to select it from the list.

# # Faded (“Grayed Out”) Choices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a web-based application, DSSA does not use grayed-out choices. If a choice is unavailable, it will simply not appear on screen or (if it is a link) will not respond to clicking.

# # Keyboard Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](tbi-version-4-2-user-manual/132.png) | Keyboard keys and onscreen buttons are shown in different style brackets throughout this manual to differentiate them from on-screen buttons or menu options: \< Ctrl \> and \< Enter \> are on the keyboard, \[Close\] is a command button on the screen. |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](tbi-version-4-2-user-manual/133.png) See [Appendix B](#AppendixB) for a complete listing of keyboard shortcuts.

# Read-Only Data Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Items in fields that appear as shown below are read-only; that is, they cannot be entered or changed directly via the screen on which they appear. In this manual, when such screens are shown, they are usually accompanied by an “INCLUDES:” list of fields; on those lists, read-only fields are shown in a 50% gray, italicized typeface:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INCLUDES:</p>
<ul>
<li><p><em>Encounter Information</em></p></li>
<li><p><em>Provider Information</em></p>
<ul>
<li><p><em>Name</em></p></li>
<li><p><em>Address</em></p></li>
<li><p><em>Phone</em></p></li>
<li><p><em>Other</em></p></li>
</ul></li>
</ul>
<p>![](tbi-version-4-2-user-manual/134.png)</p></th>
<th><p>![](tbi-version-4-2-user-manual/135.png)</p>
<p><span id="_Toc423685700" class="anchor"></span>Figure 58 – Read Only Data Fields</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Generally speaking, the read-only data thus shown is pre-populated by data feeds from various sources.

# Tab Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the \< Tab \> key or the mouse to move between fields. Do *not* use the \< Enter \> or \< Return \> key, which is usually reserved for the default command button or action.

| ![](tbi-version-4-2-user-manual/136.png) | Tip: In most cases, you may move “backward” to a previous field by holding down the \< Shift \> key and pressing \< Tab \>. |
|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|

# Changing (Resizing) a Browser Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Windows and columns displayed within DSSA cannot be resized, although the size of the browser window can be changed. To change the size of a browser window, position the mouse pointer over the right edge of the column or the outside edge of the window, left click, and while holding the mouse button down, move the mouse and “drag” to change the size of the window or column. Position the mouse pointer over one corner and drag diagonally to increase the size of the entire window.

| ![](tbi-version-4-2-user-manual/137.png) | Note: Also see Resizing the Browser Screen for tips on how to maximize or minimize browser windows using the keyboard. |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|

# Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAMPLE: ![](tbi-version-4-2-user-manual/138.png)

Provides generalized help on the application, or specialized help for the area in which you are currently working. See Online Help for more information.

# Command Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### OK

SAMPLE: ![](tbi-version-4-2-user-manual/139.png)

Confirms the input and initiates the action defined by the window. Also indicates that you agree with the default choice shown in the window.

######### Save

SAMPLE: ![](tbi-version-4-2-user-manual/140.png)

Saves all changes made since the last save action. If you attempt to save and all required fields have not yet been completed, you will receive notification that the required fields must be completed before saving.

# System Timeout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A timeout function is automatically enforced in DSSA. When you open the application, your activity is programmatically monitored. If there is no activity for 20 minutes, the application will begin to shut itself down.

The “Application Time Out” message window displays for 30 seconds. If there is still no activity within 30 seconds, the application automatically closes; a countdown of seconds remaining is displayed.

# Accessibility Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Application Accessibility Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Activating Drop-down Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can activate drop-down lists from the keyboard. Simply tab to the drop-down list field and press the up \<  \> or down arrow key \<  \>.

# Navigating the Date Picker Calendar Pop-ups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the date selection pop-up calendars (known as “date pickers”) may be somewhat problematic for those using screen readers such as [JAWS](#Glos_JAWS). The pop-up date picker calendar is essentially a graphic, rather than text, feature that is designed to be navigated using the mouse. There are no keyboard equivalents in this application. You can, however, simply type a properly-formatted date into the text box.

# Browser Accessibility Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Using the \< Ctrl \>, \< Alt \> and \< Esc \> Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some of the current features of the TBI navigation may not be intuitive if you are using assistive technology (for example, a screen reader like [JAWS](#Glos_JAWS)). Remember that the following statements apply to the browser, not to TBI.

In many situations, pressing \< Ctrl \> + a letter that represents the function will perform a function (for example, \< Ctrl \>+\< P \> activates the browser <u>P</u>rint menu).

\< Alt \>+\< F4 \> closes the browser (and also closes DSSA).

\< Esc \> often may be used to close dialog boxes and pop-ups.

# Resizing the Browser Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instead of clicking the browser’s Maximize ![](tbi-version-4-2-user-manual/141.png) button, you can press \< Alt \>+\< space \> and then select Ma<u>x</u>imize by pressing \< x \>. If you wish to minimize the screen, you may press \< Alt \>+\< space \> and then select Mi<u>n</u>imize by pressing \< n \>.

![](tbi-version-4-2-user-manual/142.png)

<span id="_Toc253397863" class="anchor"></span>Figure 59 – Resizing the Browser Screen

You can also resize your browser window to match the resolution of your monitor. For example, to resize the window to 1024 x 768 pixels, enter the following into the browser address box and press \< Enter \>: javascript:window.resizeTo(1024,768); (yes, include the semicolon at the end).

<http://www.petefreitag.com/item/633.cfm>

# Windows Accessibility Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Windows® operating system offers a number of accessibility shortcuts which can be useful. These are “toggled” options, meaning that you perform the specified action once to turn the option on and then again to turn it off.

| ![](tbi-version-4-2-user-manual/143.png) | Warning: Using some of these options will dramatically change the way your computer keyboard functions. If all else fails, reboot your computer to clear any such selections. |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Each option will produce a popup confirmation window like those pictured below. Each of these confirmation pop-ups has the same three choice buttons, in this order left to right: \[OK\], \[Cancel\], and \[Settings\]. \[OK\] is always the default choice.

# StickyKeys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

StickyKeys lets you use the \< Shift \>, \< Ctrl \> or \< Alt \> keys by pressing one key at a time, rather than having to press these keys in conjunction with another key.

Press \< Shift \> five times to toggle StickyKeys on and off:

![](tbi-version-4-2-user-manual/144.png)

<span id="_Toc253397864" class="anchor"></span>Figure 60 – Turning on StickyKeys

# FilterKeys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FilterKeys causes Windows to ignore brief or repeated keystrokes and slows down the keyboard repeat rate.

Press down and hold the right-hand \< Shift \> key for eight seconds to toggle FilterKeys on and off:

![](tbi-version-4-2-user-manual/145.png)

<span id="_Toc253397865" class="anchor"></span>Figure 61 – Turning on FilterKeys

# # ToggleKeys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ToggleKeys causes a tone to sound when you press the \< Caps Lock \>, \< Num Lock \>, or \< Scroll Lock \> keys.

Press down and hold the \< Num Lock \> key for five seconds to turn ToggleKeys on and off:

![](tbi-version-4-2-user-manual/146.png)

<span id="_Toc253397866" class="anchor"></span>Figure 62 – Turning on ToggleKeys

# MouseKeys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MouseKeys lets you control the mouse pointer by using the numeric keypad on your keyboard.

Press the left-hand \< Alt \> key plus the left-hand \< Shift \> key plus the \< Num Lock \> key to toggle MouseKeys on and off:

![](tbi-version-4-2-user-manual/147.png)

<span id="_Toc253397867" class="anchor"></span>Figure 63 – Turning on MouseKeys

# HighContrast

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HighContrast improves readability for people with visual impairments by applying a special system color scheme and font size.

Press the left-hand \< Shift \> key plus the left-hand \< Alt \> key plus the \< Print Screen \> key to toggle HighContrast on and off:

![](tbi-version-4-2-user-manual/148.png)

<span id="_Toc253397868" class="anchor"></span>Figure 64 – Turning on HighContrast

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Glossary
| [A](#G_A)    | [B](#G_B) | [C](#G_C)   | [D](#G_D)   | [E](#G_E) | [F](#G_F) | [G](#G_G) | [H](#G_H) | [I](#G_I) | [J](#G_J)   | [K](#G_K) | [L](#G_L) | [M](#G_M) |
|--------------|-----------|-------------|-------------|-----------|-----------|-----------|-----------|-----------|-------------|-----------|-----------|-----------|
| [N](#G_N)    | [O](#G_O) | [ P ](#G_P) | [ Q ](#G_Q) | [R](#G_R) | [S](#G_S) | [T](#G_T) | [U](#G_U) | [V](#G_V) | [ W ](#G_W) | [X](#G_X) |           |           |
| [0-9](#G_09) |           |             |             |           |           |           |           |           |             |           |           |           |
*Control-click character to see entries; missing character means no entries for that character.*
| Term or Acronym                                 |                      |                                | Description |
|-------------------------------------------------|----------------------|--------------------------------|-------------|
| <span id="G_09" class="anchor"></span>0 - 9 |                      |                                |             |
| 508                                             |                      | *See* [Section 508](#Glos_508) |             |
| [ BACK ](#glossary)                         | to Glossary Contents |                                |             |
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 75%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th colspan="2">Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_A" class="anchor"></span><strong>A</strong></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">Alliance, The</td>
<td colspan="2"><em>See</em> <a href="#Glosa_NAHIT">National Alliance for Health Information Technology</a></td>
</tr>
<tr class="odd">
<td colspan="3"><span id="Glos_AltTab" class="anchor"></span><strong>&lt; Alt &gt;+&lt; Tab &gt;</strong></td>
<td colspan="2">This keystroke combination used for switching between top-level windows without using the mouse; hence it was named <em>Task Switcher</em>. Casual users may press &lt; Alt &gt;+&lt; Tab &gt; to alternate between the two most recent tasks, but used to its full potential, &lt; Alt &gt;+&lt; Tab &gt; can switch to any running program. The list of tasks is kept in an order with the most recently used tasks at the front. Tab does not need to be pressed as many times to move the task selection cursor from the front of the list to a nearer task—the more recently used, the easier to get back.</td>
</tr>
<tr class="even">
<td colspan="3">AAC</td>
<td colspan="2"><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a><strong>.</strong></td>
</tr>
<tr class="odd">
<td colspan="3">ACoS CoC</td>
<td colspan="2"><em>See</em> American College of Surgeons Commission on Cancer</td>
</tr>
<tr class="even">
<td colspan="3">Acquired Immune Deficiency Syndrome (AIDS)</td>
<td colspan="2"><p>Disease of the immune system characterized by increased susceptibility to opportunistic infections, to certain cancers, and to neurological disorders. Caused by a retrovirus and transmitted chiefly through blood or blood products that enter the body's bloodstream, especially by sexual contact or contaminated hypodermic needles.</p>
<p>AIDS is a disease of the human immune system caused by the human immunodeficiency virus (HIV). This condition progressively reduces the effectiveness of the immune system and leaves individuals susceptible to opportunistic infections and tumors.</p></td>
</tr>
<tr class="odd">
<td colspan="3"><span id="Glos_AD" class="anchor"></span>Active Directory (AD)</td>
<td colspan="2">AD is a technology created by Microsoft that provides a variety of network services, including user authentication. For TBI, AD essentially keeps track of who the users are and what TBI functions they are authorized to perform.</td>
</tr>
<tr class="even">
<td colspan="3">Active Dual Consumer</td>
<td colspan="2">A beneficiary who has received or can potentially receive health care from the Department of Defense (DoD) and/or Department of Veterans Affairs (VA). An ADC beneficiary can be considered as Dual <strong>Eligible</strong> or Dual <strong>User,</strong> or both.</td>
</tr>
<tr class="odd">
<td colspan="3">ADC</td>
<td colspan="2"><em>See</em> Active Dual Consumer</td>
</tr>
<tr class="even">
<td colspan="3">ADPAC</td>
<td colspan="2"><em>See</em> <a href="#Glos_ADPAC">Automated Data Processing Application Coordinator</a><strong>.</strong></td>
</tr>
<tr class="odd">
<td colspan="3">AFIP</td>
<td colspan="2"><em>See</em> Armed Forces Institute of Pathology</td>
</tr>
<tr class="even">
<td colspan="3">AHIMA</td>
<td colspan="2"><em>See</em> American Health Information Management Association</td>
</tr>
<tr class="odd">
<td colspan="3">AHLTA</td>
<td colspan="2"><em>See</em> <a href="#Glos_AHLTA">Armed Forces Health Longitudinal Technology Application</a></td>
</tr>
<tr class="even">
<td colspan="3">AIDS</td>
<td colspan="2"><em>See</em> Acquired Immune Deficiency Syndrome</td>
</tr>
<tr class="odd">
<td colspan="3">AITC</td>
<td colspan="2"><em>See</em> <a href="#Glos_AITC">Austin Information Technology Center</a></td>
</tr>
<tr class="even">
<td colspan="3">AJCC</td>
<td colspan="2"><em>See</em> American Joint Commission on Cancer</td>
</tr>
<tr class="odd">
<td colspan="3">Aliquot</td>
<td colspan="2"><p>Contained an exact number of times in something else —used of a divisor or part. Fractional.</p>
<p>Chemistry, Pharmacology: comprising a known fraction of a whole and constituting a sample: an aliquot quantity of acid for analysis. As a noun: <em>an aliquot part</em>.</p></td>
</tr>
<tr class="even">
<td colspan="3">American College of Surgeons Commission on Cancer (ACoS CoC)</td>
<td colspan="2">A consortium of professional organizations dedicated to improving survival and quality of life for cancer patients through standard-setting, prevention, research, education, and the monitoring of comprehensive quality care.</td>
</tr>
<tr class="odd">
<td colspan="3">American Health Information Management Association (AHIMA)</td>
<td colspan="2">Professional group which strives to improve healthcare by advancing best practices and standards for health information management. Considered a trusted source for education, research, and professional credentialing.</td>
</tr>
<tr class="even">
<td colspan="3">American Joint Commission on Cancer (AJCC)</td>
<td colspan="2">Organization established in 1959 to formulate and publish systems of classification of cancer, including staging and end results reporting.</td>
</tr>
<tr class="odd">
<td colspan="3">Analyte</td>
<td colspan="2">A chemical substance that is the subject of chemical analysis.</td>
</tr>
<tr class="even">
<td colspan="3"><span id="Glos_AHLTA" class="anchor"></span>Armed Forces Health Longitudinal Technology Application (AHLTA)</td>
<td colspan="2"><p>AHLTA, the military's electronic health record (EHR), marks a significant new era in healthcare for the Military Health System (MHS) and the nation. In his January 2004 State of the Union address, the President set the goal of ensuring most Americans had an EHR by 2014. The Department of Defense is leading this effort by completing the implementation of AHLTA, the interoperable, globally-accessible, protected, and always available EHR for Uniformed Services members, retirees and their families by 2011. AHLTA gives healthcare providers access to data about beneficiaries' conditions, prescriptions, diagnostic tests and additional information essential to providing quality care.</p>
<p><em>Source:</em> <a href="http://www.ahlta.us/about.php">http://www.ahlta.us/about.php</a></p></td>
</tr>
<tr class="odd">
<td colspan="3">Armed Forces Institute of Pathology (AFIP)</td>
<td colspan="2">Provides diagnostic consultations on pathologic specimens from military, Veterans, and civilian medical, dental and veterinary sources. Conducts scientific research in fields such as environmental pathology and toxicology, infectious diseases, oncology and forensic science.</td>
</tr>
<tr class="even">
<td colspan="3">Austin Automation Center (AAC)</td>
<td colspan="2"><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a></td>
</tr>
<tr class="odd">
<td colspan="3"><span id="Glos_AITC" class="anchor"></span>Austin Information Technology Center (AITC)</td>
<td colspan="2">AITC is a recognized, award-winning Federal data center within the Department of Veterans Affairs (VA). It provides a full complement of cost-efficient e-government solutions to support the information technology (IT) needs of customers within the Federal sector. AITC has also implemented a program of enterprise “best practice” initiatives with major vendor partners that ensures customers receive enhanced, value-added IT services through the implementation of new technologies at competitive costs.</td>
</tr>
<tr class="even">
<td colspan="3"><span id="Glos_ADPAC" class="anchor"></span>Automated Data Processing Application Coordinator (ADPAC)</td>
<td colspan="2">The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they run into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or Information Resource Management (IRM).</td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="4">to Glossary Contents</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><span id="G_B" class="anchor"></span><strong>B</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_backend" class="anchor"></span>back-end</td>
<td>Any software or system which performs either the final stage in a process, or a task not apparent to the user.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_Browser" class="anchor"></span>browser</td>
<td><p>A program which allows a person to read <a href="#Glos_hypertext">hypertext</a>. The browser provides some means of viewing the contents of nodes (or "pages") and of navigating from one node to another. A browser is required in order to access the TBI software application.</p>
<p>Microsoft® Internet Explorer® is a browser for the World-Wide Web. It acts as client to remote web servers.</p></td>
</tr>
<tr class="even">
<td colspan="2">BVAMC</td>
<td><em>See</em> Baltimore Veterans Affairs Medical Center</td>
</tr>
<tr class="odd">
<td colspan="2">Biomonitoring (or Biological Monitoring)</td>
<td>Process of assessing and measuring clinical response to toxins introduced into the body as a result of embedded fragment trauma. Specimens are collected and sent to a laboratory to establish baseline levels of analytes. The process of collection and analysis is then repeated periodically to develop a <a href="#Glos_Longitudinal">longitudinal</a> assessment for diagnosis, corrective treatment and prognosis.</td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="2">to Glossary Contents</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><span id="G_C" class="anchor"></span><strong>C</strong></td>
</tr>
<tr class="even">
<td colspan="2">CAC</td>
<td>Clinical Application Coordinator</td>
</tr>
<tr class="odd">
<td colspan="2">Case</td>
<td>The collection of information maintained on patients that have been included in a registry.</td>
</tr>
<tr class="even">
<td colspan="2">Case Finding</td>
<td>Those activities associated with the identification of patients for potential inclusion in a registry.</td>
</tr>
<tr class="odd">
<td colspan="2">Case Tracking</td>
<td>Those activities associated with monitoring patients that have met the criteria for inclusion in a registry through the case finding process.</td>
</tr>
<tr class="even">
<td colspan="2">CCHIT</td>
<td>Certification Commission of Health Information Technology</td>
</tr>
<tr class="odd">
<td colspan="2">CCR</td>
<td>Clinical Case Registry</td>
</tr>
<tr class="even">
<td colspan="2">CDC</td>
<td><em>See</em> <a href="#Glos_CDC">Centers for Disease Control and Prevention</a></td>
</tr>
<tr class="odd">
<td colspan="2">CDC</td>
<td>Center for Disease Control</td>
</tr>
<tr class="even">
<td colspan="2">CDCO</td>
<td><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a></td>
</tr>
<tr class="odd">
<td colspan="2">CDW</td>
<td><em>See</em> <a href="#Glos_CDW">Corporate Data Warehouse</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CQM" class="anchor"></span>Center for Quality Management in Public Health (CQM)</td>
<td>CQM, based in the VA Palo Alto Health Care System, functions as part of the VA Public Health Strategic Health Care Group at VA Central Office in Washington, DC. CQM was first established with a primary focus on HIV care; the mission expanded to include Hepatitis C issues in January 2001. In line with the mission of its organizational parent, the CQM mission further expanded to include work on various issues and conditions with public health significance, including operational support and management of data from the TBI.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CDC" class="anchor"></span>Centers for Disease Control and Prevention (CDC)</td>
<td><p>The CDC is one of the major operating components of the United States Department of Health and Human Services. It includes a number of Coordinating Centers and Offices which specialize in various aspects of public health, as well as the National Institute for Occupational Safety and Health (NIOSH).</p>
<p><em>See</em> <a href="http://www.cdc.gov/about/organization/cio.htm">http://www.cdc.gov/about/organization/cio.htm</a></p></td>
</tr>
<tr class="even">
<td colspan="2">Chain of Custody</td>
<td>Chain of custody refers to the chronological documentation, and/or "paper trail," showing the custody, control, transfer, analysis, and disposition of specimens, whether physical or electronic. A chain of custody form is used to document these events for biological monitoring and fragment analysis kit tracking in the TBI application.</td>
</tr>
<tr class="odd">
<td colspan="2">CHPPM</td>
<td><em>See</em> <a href="#Glos_USAPHC">U.S. Army Public Health Command (Provisional)</a>.</td>
</tr>
<tr class="even">
<td colspan="2">Clinical Application Coordinator</td>
<td>A clinically experienced person who guides and supports clinicians, IT experts, and others through design, adoption, tailoring, and use of clinical computing systems such as an electronic medical record. A CAC teaches, trains, supports and innovates.</td>
</tr>
<tr class="odd">
<td colspan="2">Clinical Reminder</td>
<td>A clinical reminder is a software decision support tool that defines evaluation and resolution logic for a given clinical activity. The evaluation logic defines conditions in the database including the presence or absence of specified criteria such as diagnoses, procedures, health factors, medications, or demographic variables (e.g., age, gender). A reminder may or may not require provider resolution, depending on its purpose and design, through a user interface, also known as a reminder dialog. Also, in accordance with the underlying logic, reminders may be used to collect specified patient information that may or may not be related to the dialog.</td>
</tr>
<tr class="even">
<td colspan="2">Comma-Delimited Values (CDV)</td>
<td><em>See</em> <a href="#Glos_CSV">Comma-Separated Values</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CSV" class="anchor"></span>Comma-Separated Values (CSV)</td>
<td>“Separated” or “delimited” data files use specific characters (delimiters) to separate its values. Most database and spreadsheet programs are able to read or save data in a delimited format. The comma-separated values file format is a delimited data format that has fields separated by the comma character and records separated by newlines. Excel can import such a file and create a spreadsheet from it.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_computabledata" class="anchor"></span>computable data</td>
<td><em>Computable data</em> is a representation of data values in a form that can be machine-processed and reasoned upon. It is usually depicted in a code value from some formal terminology where semantic links are meaningful and support activities such as decision support. At the present, data available on eye injuries and treatment within the VA lack this computable data. Free text information (such as that in the <a href="#Glos_TIU">TIU</a> “eye notes”) is helpful and valuable to a caregiver, but does not allow the computer to provide the assistance that would be possible if a more structured representation were available. For instance, support functions such as allergy checking, automated reporting of measurements and test results, and so on each require computable data.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CPRS" class="anchor"></span>Computerized Patient Record System (CPRS)</td>
<td>A Computerized Patient Record (CPR) is a comprehensive database system used to store and access patients’ healthcare information. CPRS is the Department of Veterans Affairs electronic health record software. The CPRS organizes and presents all relevant data on a patient in a way that directly supports clinical decision making. This data includes medical history and conditions, problems and diagnoses, diagnostic and therapeutic procedures and interventions. Both a graphic user interface version and a character-based interface version are available. CPRS provides a single interface for health care providers to review and update a patient’s medical record, and to place orders, including medications, special procedures, x-rays, patient care nursing orders, diets, and laboratory tests. CPRS is flexible enough to be implemented in a wide variety of settings for a broad spectrum of health care workers, and provides a consistent, event-driven, Windows-style interface.</td>
</tr>
<tr class="even">
<td colspan="2">Context-Sensitive Help</td>
<td><p>Online help is topic-oriented, procedural or reference information delivered through computer software. It is a form of user assistance. Most online help is designed to give assistance in the use of a software application or operating system, but can also be used to present information on a broad range of subjects.</p>
<p>When a user presses the [F1] key while using the GUI application, the application automatically opens the online help file (which is distributed and installed alongside the application file itself).</p>
<p><strong>Context-sensitive help</strong> is a kind of online help that is obtained from a specific point in the state of the software, providing help for the situation that is associated with that state.</p>
<p>Context-sensitive help, as opposed to general online help or online manuals, doesn't need to be accessible for reading as a whole. Each topic is supposed to describe extensively one state, situation, or feature of the software.</p>
<p>Context-sensitive help can be implemented using <a href="http://en.wikipedia.org/wiki/Tooltip">tooltips</a>, which either provide a terse Description of a <a href="http://en.wikipedia.org/wiki/GUI_widget">GUI widget</a> or display a complete topic from the help file. Other commonly used ways to access context-sensitive help start by clicking a button. One way uses a per widget button that displays the help immediately. Another way changes the <a href="http://en.wikipedia.org/wiki/Mouse_pointer">mouse pointer</a> shape to a question mark, and then, after the user clicks a widget, the help appears.</p>
<p>Context-sensitive help is most used in, but is not limited to, <a href="http://en.wikipedia.org/wiki/GUI">GUI</a> environments. Examples are <a href="http://en.wikipedia.org/wiki/Microsoft">MiDVEIRosoft's</a> <a href="http://en.wikipedia.org/wiki/Windows_Help">WinHelp</a>, <a href="http://en.wikipedia.org/wiki/Sun_Microsystems">Sun's</a> <a href="http://en.wikipedia.org/wiki/JavaHelp">JavaHelp</a> or Panviva's <a href="http://www.supportpoint.com/">SupportPoint</a>.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CDCO" class="anchor"></span>Corporate Data Center Operations (CDCO)</td>
<td><p>Federal data center within the Department of Veterans Affairs (VA). As a franchise fund, or fee-for-service organization, CDCO-Austin provides cost-efficient IT enterprise solutions to support the information technology needs of customers within the Federal sector. <em>Formerly</em> the Austin Automation Center (AAC); <em>formerly</em> the Austin Information Technology Center (AITC).</p>
<p><em>See</em> <mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CDW" class="anchor"></span>Corporate Data Warehouse (CDW)</td>
<td><p>CDW is a national repository comprising data from several Veterans Health Administration (VHA) clinical and administrative systems. The CDW’s objective is to provide data and tools to support management decision making, performance measurement and research objectives. Its premise is that incorporating data from multiple differing data sets throughout the VHA into one standard database structure will facilitate reporting and data analysis at the enterprise level. The CDW operates within the VA Office of Information &amp; Technology’s Field Operations Business Intelligence Service Line.</p>
<p>CDW data are stored in a relational database. Multiple VA data sources are being merged so that cohorts will be definable by attributes such as ICD-9 codes and CPT codes from both inpatient and outpatient encounters or from abnormal values of vital signs like blood pressure, weight and height, within a target time period.</p>
<p>These data are kept current by frequent updates with new data from the source data-bases so timely data are available for research. When the CDW database is updated, changed data values are written over, not maintained. These incremental updates are, however, flagged with a new “last update” date. In addition, if a data transmission indicates an encounter record has been deleted from the source database, it is instead flagged in the CDW as “deleted" (Delete Flag = Y) so that original demographic data can always be recovered.</p>
<p><em>Source:</em> <a href="http://www.virec.research.va.gov/DataSourcesName/CDW/CDW.htm">http://www.virec.research.va.gov/DataSourcesName/CDW/CDW.htm</a></p>
<p><em>See also:</em> <a href="#Glos_DataWarehouse">Data warehouse</a></p></td>
</tr>
<tr class="odd">
<td colspan="2">CPRS</td>
<td><em>See</em> <a href="#Glos_CPRS">Computerized Patient Record System</a></td>
</tr>
<tr class="even">
<td colspan="2">CPT</td>
<td><em>See</em> <a href="#Glos_CPT">Current Procedural Terminology</a></td>
</tr>
<tr class="odd">
<td colspan="2">CPT-4</td>
<td><em>See</em> <a href="#Glos_CPT">Current Procedural Terminology</a></td>
</tr>
<tr class="even">
<td colspan="2">CQM</td>
<td><em>See</em> <a href="#Glos_CQM">Center for Quality Management in Public Health</a></td>
</tr>
<tr class="odd">
<td colspan="2">Creatinine</td>
<td><p>Used as a measurement of renal function as part of the biological monitoring process.</p>
<p>A crystalline end product of creatine metabolism which occurs in urine, muscle, and blood. Creatinine levels in blood and urine may be used to calculate the creatinine clearance for further process to takes place, which would reflect the glomerular filtration rate (GFR). The GFR is clinically and vitally important because it is a measurement of renal function.</p></td>
</tr>
<tr class="even">
<td colspan="2">CSV</td>
<td><em>See</em> <a href="#Glos_CSV">Comma-Separated Values</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CPT" class="anchor"></span>Current Procedural Terminology (CPT or CPT-4)</td>
<td><p>CPT® is the most widely accepted medical nomenclature used to report medical procedures and services under public and private health insurance programs. CPT codes describe a procedure or service identified with a five-digit CPT code and descriptor nomenclature. The CPT code set accurately describes medical, surgical, and diagnostic services and is designed to communicate uniform information about medical services and procedures among physicians, coders, patients, accreditation organizations, and payers for administrative, financial, and analytical purposes. The current version is the CPT-4 (4th Edition), 2009.</p>
<p><em>Note:</em> CPT® is a registered trademark of the American Medical Association.</p></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="2">to Glossary Contents</td>
</tr>
</tbody>
</table>
| Term or Acronym                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="G_D" class="anchor"></span>D                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Data Dictionary                                                                          | A data structure that stores meta-data, *i.e.,* data about data. The term “data dictionary” has several uses; most generally it is thought of as a set of data Descriptions that can be shared by several applications. In practical terms, it usually means a table in a database that stores the names, field types, length, and other characteristics of the fields in the database tables.                                                                                                                                                                |
| Data Transfer Agreement (DTA)                                                            | Agreement between two or more VA departments, or between a VA department and an outside agency. DTAs cover transfers of data or information between agencies or departments in order to maintain appropriate administrative, technical and physical security safeguards to prevent unauthorized use and to protect the confidentiality of the data.                                                                                                                                                                                                           |
| <span id="Glos_DataWarehouse" class="anchor"></span>Data Warehouse                       | A system for storing, retrieving and managing large amounts of data. Data warehouse software often includes sophisticated compression and hashing techniques for fast searches, as well as advanced filtering. A data warehouse is often a relational database containing a recent snapshot of corporate data and optimized for searching. Planners and researchers can use this database without worrying about slowing down day-to-day operations of the production database. The latter can be optimized for transaction processing (inserts and updates). |
| Decentralized Hospital Computer Program (DHCP)                                           | Obsolete term; [VistA](#Glos_VistA) is the modern equivalent                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Defense Health Information Management System (DHIMS)                                     | System designed to provide a trusted, comprehensive health information management system that seamlessly captures, manages and shares health information from the Theater of Operations to the home front and beyond. This is, roughly, the DoD equivalent of [CPRS](#Glos_CPRS).                                                                                                                                                                                                                                                                             |
| <span id="Glos_DVEIR" class="anchor"></span>Defense/Veterans Eye Injury Registry (DVEIR) | DVEIR helps identify and document treatment of all OEF/OIF service members with ocular injuries.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="Glos_DoD" class="anchor"></span>Department of Defense (DoD)                    | A department of the U.S. Federal government, charged with ensuring that the military capacity of the U.S. is adequate to safeguard the national security.                                                                                                                                                                                                                                                                                                                                                                                                     |
| DHCP                                                                                     | Decentralized Hospital Computer Program (obsolete term; [VistA](#Glos_VistA) is the modern equivalent)                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DHIMS                                                                                    | *See* Defense Health Information Management System                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DoD                                                                                      | *See* [Department of Defense](#Glos_DoD)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DTA                                                                                      | *See* Data Transfer Agreement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Dual Consumer                                                                            | A patient who is eligible for health care under DoD and VA health plans, or who has been assigned to a joint venture site and meets the requirements under a DoD/VA sharing agreement for coverage of specified clinical services.                                                                                                                                                                                                                                                                                                                            |
| Dual User                                                                                | A patient who has received care at both a DoD facility and a VA facility. Dual users are a subset population of Active Dual Consumers.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DVEIR                                                                                    | *See* [Defense/Veterans Eye Injury Registry](#Glos_DVEIR)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [ BACK ](#glossary)                                                                  | to Glossary Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_E" class="anchor"></span><strong>E</strong></td>
</tr>
<tr class="even">
<td colspan="2">EHR</td>
<td colspan="2"><em>See</em> <a href="#Glos_EHR">Electronic Health Record</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_EHR" class="anchor"></span>Electronic Health Record (EHR)</td>
<td colspan="2">An evolving concept, defined as a longitudinal collection of electronic health information about individual patients or populations. It is a record in digital format that can be shared across different health care settings, by being embedded in network-connected enterprise-wide information systems.</td>
</tr>
<tr class="even">
<td colspan="2">Embedded Metal Fragments Registry (EMFR)</td>
<td colspan="2">DoD system for tracking information relevant to injuries associated with embedded metal fragments.</td>
</tr>
<tr class="odd">
<td colspan="2">Embedded Metal Fragments Registry (EMFR) data extract</td>
<td colspan="2"><p>This extract includes the following read-only data:</p>
<ul>
<li><p>Social Security Number</p></li>
<li><p>Lab ID Number</p></li>
<li><p>Fragment ID Number (may be multiple IDs for each patient)</p></li>
<li><p>Date Fragment Received at Lab</p></li>
<li><p>Date of Fragment Producing Event</p></li>
<li><p>Lab Report Date</p></li>
<li><p>Fragment Description</p></li>
<li><p>Mass of Fragment</p></li>
<li><p>Units for Mass</p></li>
<li><p>Units for Fragment Measurements</p></li>
<li><p>Length of Fragment</p></li>
<li><p>Height of Fragment</p></li>
<li><p>Width of Fragment</p></li>
<li><p>Indication that Fragment is Radioactive</p></li>
<li><p>Results of Radioactivity Testing</p></li>
<li><p>Comments</p></li>
</ul>
<p>For each Fragment ID Number:</p>
<ul>
<li><p>Analytical Method Code</p></li>
<li><p>Analytical Method Description</p></li>
<li><p>Other Analytical Method Description</p></li>
<li><p>Analyte Name</p></li>
<li><p>Analyte Results</p></li>
<li><p>Analyte Comments</p></li>
<li><p>Chemical Abstract Service (CAS) Number</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">Epidemiology</td>
<td colspan="2">A branch of medical science that deals with the incidence, distribution and control of disease in a population.</td>
</tr>
<tr class="odd">
<td colspan="2">ESM</td>
<td colspan="2">Enterprise System Manager, Office of Enterprise Systems Management</td>
</tr>
<tr class="even">
<td colspan="2">ETL</td>
<td colspan="2"><em>See</em> <a href="#Glos_ETL">Extract, Transform and Load</a></td>
</tr>
<tr class="odd">
<td colspan="2">EVIR</td>
<td colspan="2"><em>See</em> <a href="#Glos_MEVIR">Military Eye/Vision Injury Registry</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_XML" class="anchor"></span>Extensible Mark-up Language (XML)</td>
<td colspan="2">An initiative from the W3C defining an “extremely simple” dialect of <a href="#Glos_SGML">SGML</a> suitable for use on the World-Wide Web.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ETL" class="anchor"></span>Extract, Transform and Load (ETL)</td>
<td colspan="2">ETL is a process in database usage and especially in data warehousing that involves extracting data from outside sources; transforming it to fit operational needs (which can include quality levels); and loading it into the end target (database or data warehouse).</td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="2">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 1%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_F" class="anchor"></span><strong>F</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_FRC" class="anchor"></span>Federal Recovery Coordinator (FRC)</td>
<td colspan="3"><p>FRCs help severely injured combat Veterans and their families maneuver through military and Veterans’ treatment and benefits programs.</p>
<p>There are 14 Federal Recovery Coordinators responsible for fewer than 300 cases of the most severely injured combat Veterans who face complicated treatment and recovery plans.</p></td>
</tr>
<tr class="odd">
<td colspan="2">FHP&amp;R</td>
<td colspan="3"><em>See</em> <a href="#Glos_OFHPR">Office of Force Health Protection and Readiness</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_FTP" class="anchor"></span>File Transfer Protocol (FTP)</td>
<td colspan="3">A client-server protocol which allows a user on one computer to transfer files to and from another computer over a TCP/IP network. Also the client program the user executes to transfer files. It is defined in STD 9, RFC 959.</td>
</tr>
<tr class="odd">
<td colspan="2">Firewall</td>
<td colspan="3">A firewall is a part of a computer system or network that is designed to block unauthorized access while permitting authorized communications. It is a device or set of devices configured to permit, deny, encrypt, decrypt, or proxy all (in and out) computer traffic between different security domains based upon a set of rules and other criteria.</td>
</tr>
<tr class="even">
<td colspan="2">Fragment</td>
<td colspan="3">Any piece of material that is or has been embedded in the body as a result of injury. Also known as shrapnel.</td>
</tr>
<tr class="odd">
<td colspan="2">FRC</td>
<td colspan="3"><em>See</em> <a href="#Glos_FRC">Federal Recovery Coordinator</a></td>
</tr>
<tr class="even">
<td colspan="2">FTP</td>
<td colspan="3"><em>See</em> <a href="#Glos_FTP">File Transfer Protocol</a></td>
</tr>
<tr class="odd">
<td colspan="2">FIM</td>
<td colspan="3">Functional Independence Measure</td>
</tr>
<tr class="even">
<td colspan="2">Function key</td>
<td colspan="3">A key on a computer or terminal keyboard which can be programmed so as to cause an operating system command interpreter or application program to perform certain actions. On some keyboards/computers, function keys may have default actions, accessible on power-on. For example, &lt;F1&gt; is traditionally the function key used to activate a help system.</td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_G" class="anchor"></span><strong>G</strong></td>
</tr>
<tr class="even">
<td colspan="2">Global War On Terror (GWOT)</td>
<td colspan="3"><em>Obsolete term; see</em> Overseas Contingency Operation</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_GUI" class="anchor"></span>Graphical User Interface (GUI)</td>
<td colspan="3"><p>A graphical user interface (or GUI, often pronounced “gooey”) is a graphical (rather than purely textual) user interface to a computer. A GUI is a particular case of user interface for interacting with a computer which employs graphical images and widgets in addition to text to represent the information and actions available to the user. Usually the actions are performed through direct manipulation of the graphical elements. A GUI takes advantage of the computer’s graphics capabilities to make the program easier to use.</p>
<p><em>Sources:</em></p>
<p><a href="http://en.wikipedia.org/wiki/GUI">http://en.wikipedia.org/wiki/GUI</a></p>
<p><a href="http://www.webopedia.com/TERM/G/Graphical_User_Interface_GUI.html">http://www.webopedia.com/TERM/G/Graphical_User_Interface_GUI.html</a></p>
<p><em>See also</em> <a href="#Glos_UserInterface">User Interface</a></p></td>
</tr>
<tr class="even">
<td colspan="2">GUI</td>
<td colspan="3"><em>See:</em> <a href="#Glos_GUI">Graphical User Interface</a></td>
</tr>
<tr class="odd">
<td colspan="2">GWOT</td>
<td colspan="3">Global War On Terror (<em>obsolete term; see</em> Overseas Contingency Operation).</td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th>Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_H" class="anchor"></span><strong>H</strong></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">HTML</td>
<td colspan="2"><em>See</em> <a href="#Glos_HTML">Hypertext Mark-up Language</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_hypertext" class="anchor"></span>hypertext</td>
<td colspan="2">A term coined around 1965 for a collection of documents (or "nodes") containing cross-references or "links" which, with the aid of an interactive browser program, allow the reader to move easily from one document to another.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HTML" class="anchor"></span>Hypertext Mark-up Language (HTML)</td>
<td colspan="2">A <a href="#Glos_hypertext">hypertext</a> document format used on the World-Wide Web. HTML is built on top of <a href="#Glos_SGML">SGML</a>. "Tags" are embedded in the text. A tag consists of a "&lt;", a "directive" (in lower case), zero or more parameters and a "&gt;". Matched pairs of directives, like "&lt;title&gt;" and "&lt;/title&gt;" are used to delimit text which is to appear in a special place or style.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_HAIG" class="anchor"></span>Healthcare Analysis &amp; Information Group (HAIG)</td>
<td colspan="2">A field unit of Clinical Affairs and Information Management in Milwaukee, WI. Functions as a provider of information syntheses, analyses, report formatting, and dissemination of many types of information and tools in support of national policies, strategic planning and decision-making processes. HAIG develops corporate reports, proceedings, analyses, and disseminates information through the use of state-of-the art technology including survey design, statistical analysis, customized publications, web design/management, and advanced computer applications.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">HAIG</td>
<td colspan="2"><em>See</em> <a href="#Glos_HAIG">Healthcare Analysis &amp; Information Group</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">HAIISS</td>
<td colspan="2"><em>See</em> <a href="#Glos_HAIISS">Healthcare Associated Infection and Influenza Surveillance System</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HAIISS" class="anchor"></span>Healthcare Associated Infection and Influenza Surveillance System (HAIISS)</td>
<td colspan="2">VHA is seeking to leverage its advanced electronic medical records to establish a comprehensive electronic surveillance system for monitoring healthcare-associated infections and antibiotic resistance trends, as well as influenza and other emerging infectious diseases or syndromes potentially associated with bioterrorist activity. This project is now being merged with the project known as Electronic Surveillance System for the Early Notification of Community-based Epidemics (ESSENCE) and will be managed separately from the Registries projects.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">HDR</td>
<td colspan="2">Health Data Repository</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">HDS</td>
<td colspan="2">Health Data Systems</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Health Factor</td>
<td colspan="2">A health factor is a computerized component that captures patient information that for which no standard code exists, such as Family History of Alcohol Abuse, Lifetime Non-smoker, No Risk Factors for Hepatitis C, etc. See also, Clinical Reminders.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><a href="http://www.himss.org">HIMSS</a></td>
<td colspan="2"><em>See</em> <a href="#Glos_HIMSS">Healthcare Information and Management Systems Society</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_HIMSS" class="anchor"></span>Healthcare Information and Management Systems Society (HIMSS)</td>
<td colspan="2">HIMSS is a healthcare-stakeholder membership organization exclusively focused on providing global leadership for the optimal use of information technology (IT) and management systems for the betterment of healthcare.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">HIV</td>
<td colspan="2"><em>See</em> Human Immunodeficiency Virus</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Human Immuno-deficiency Virus (HIV)</td>
<td colspan="2"><p>HIV is a lentivirus (a member of the retrovirus family) that can lead to acquired immunodeficiency syndrome (AIDS), a condition in humans in which the immune system begins to fail, leading to life-threatening opportunistic infections. HIV is different from most other viruses because it attacks the immune system. The immune system gives our bodies the ability to fight infections. HIV finds and destroys a type of white blood cell (T cells or CD4 cells) that the immune system must have to fight disease.</p>
<p>See <a href="http://www.cdc.gov/hiv/topics/basic/index.htm">http://www.cdc.gov/hiv/topics/basic/index.htm</a>.</p></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="4">to Glossary Contents</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_I" class="anchor"></span><strong>I</strong></td>
</tr>
<tr class="even">
<td colspan="2">ICD-9</td>
<td colspan="3"><em>See</em> <a href="#Glos_ICD9">International Statistical Classification of Diseases and Related Health Problems</a></td>
</tr>
<tr class="odd">
<td colspan="2">IDMC</td>
<td colspan="3"><em>See</em> <a href="#Glos_IDMC">Information and Data Management Committee</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_IDMC" class="anchor"></span>Information and Data Management Committee (IDMC)</td>
<td colspan="3">IDMC is the advisory group to the Under Secretary for Health through the National Leadership Board (NLB) on Information Technology (IT) issues. The IDMC membership is comprised of a cross section of Veterans Health Administration (VHA) leadership representing VHA health care programs and operations, and helps ensure IT investments support corporate goals. The IDMC works collaboratively with other committees and groups concerned with IT-related issues.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_IRM" class="anchor"></span>Information Resources Management (IRM)</td>
<td colspan="3">The service which is involved in planning, budgeting, procurement and management-in-use of VA's information technology investments.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_IT" class="anchor"></span>Information Technology (IT)</td>
<td colspan="3">Refers to applied computer systems (both hardware and software), and often including networking and telecommunications, usually in the context of a business or other enterprise. Often the name of the part of an enterprise that deals with all things electronic.</td>
</tr>
<tr class="odd">
<td colspan="2">Integration Control Number (ICN)</td>
<td colspan="3">The national VA patient record number.</td>
</tr>
<tr class="even">
<td colspan="2">Interface</td>
<td colspan="3">An interface defines the communication boundary between two entities, such as a piece of software, a hardware device, or a user.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ICD9" class="anchor"></span>International Statistical Classification of Diseases and Related Health Problems (ICD-9)</td>
<td colspan="3"><p>The <em>International Statistical Classification of Diseases and Related Health Problems</em>, Ninth Edition (commonly abbreviated as “ICD-9”) provides numeric codes to classify diseases and a wide variety of signs, symptoms, abnormal findings, complaints, social circumstances and external causes of injury or disease. . Every health condition can be assigned to a unique category and given a code, up to six characters long. Such categories can include a set of similar diseases. . The “-9” refers to the ninth edition of these codes; the tenth edition has been published, but is not in widespread use at this time.</p>
<p><em>See also</em> <a href="#Glos_CPT">Current Procedural Terminology</a></p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_Intranet" class="anchor"></span>intranet</td>
<td colspan="3">Any network which provides similar services within an organization to those provided by the Internet outside it, but which is not necessarily connected to the Internet. The commonest example is the use by a company of one or more World-Wide Web servers on an internal TCP/IP network for distribution of information within the company. . The VA intranet hosts TBI as well as other programs and information.</td>
</tr>
<tr class="odd">
<td colspan="2">IRM</td>
<td colspan="3"><em>See</em> <a href="#Glos_IRM">Information Resources Management</a></td>
</tr>
<tr class="even">
<td colspan="2">IT</td>
<td colspan="3"><em>See</em> <a href="#Glos_IT">Information Technology</a></td>
</tr>
<tr class="odd">
<td colspan="2"><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_J" class="anchor"></span><strong>J</strong></td>
</tr>
<tr class="even">
<td colspan="2">JAWS</td>
<td colspan="3"><em>See</em> <a href="#Glos_JAWS">Job Access with Speech</a></td>
</tr>
<tr class="odd">
<td colspan="2">Job Access with Speech (JAWS)</td>
<td colspan="3">Refers to a software product for visually impaired users. The software is produced by the Blind and Low Vision Group of Freedom Scientific. See <a href="http://en.wikipedia.org/wiki/JAWS_%28screen_reader%29">http://en.wikipedia.org/wiki/JAWS_%28screen_reader%29</a> and <a href="http://www.freedomscientific.com/fs_products/software_jaws.asp">http://www.freedomscientific.com/fs_products/software_jaws.asp</a>.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_JMeWS" class="anchor"></span>Joint Medical Workstation (JMeWS)</td>
<td colspan="3">Military commanders need to have online, near-real-time medical situational awareness for forward-deployed forces during Operation Iraqi Freedom (OIF). JMeWS provides that capability. Like <a href="#Glos_AHLTA">AHLTA</a>-T and JPTA, JMeWs is an integral part of the TMIP-J capability.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_JTPA" class="anchor"></span>Joint Patient Tracking Application (JPTA)</td>
<td colspan="3">JTPA tracks the location and disposition of ill or injured patients as they move through the echelons of care, from the U.S. Central Command theater of operations, to Landstuhl Regional Medical Center and back to selected Military Health System or Department of Veterans Affairs medical facilities in the U.S.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_JTTS" class="anchor"></span>Joint Theater Trauma System (JTTS)</td>
<td colspan="3"><p>JTTS is an approach to providing improved trauma care across the continuum of the Levels of Care to trauma patients, especially in the battlefield environment. Its mission is to:</p>
<ul>
<li><blockquote>
<p>Establish and maintain a Department of Defense Trauma Registry System to capture data and provide information on care and outcomes of military and civilian trauma patients.</p>
</blockquote></li>
<li><blockquote>
<p>Provide the Department of Defense and other authorized interests with timely and relevant information about care and outcomes of military and civilian injuries.</p>
</blockquote></li>
<li><blockquote>
<p>Create a research strategy that supports reduction of morbidity and mortality in military and civilian trauma patients.</p>
</blockquote></li>
<li><blockquote>
<p>Establish and maintain a trauma outcomes database to analyze and evaluate clinical decision making and measure subsequent outcomes for improving treatment modalities.</p>
</blockquote></li>
</ul>
<ul>
<li><p>- Provide activities of each of the services with full and complete access to data resident in the DoD Trauma Registry.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_JTTR" class="anchor"></span>Joint Theatre Trauma Registry (JTTR)</td>
<td colspan="3"><p>JTTR is the DoD's data repository collecting and hosting all trauma related data. Sited at Fort Sam Houston, Texas, helps track casualty information from Iraq and Afghanistan to give senior leaders the concrete information they need as they make decisions about everything from what protective gear troops will use to how to better deliver combat casualty care. JTTR also helps ensure that decision makers have more than anecdotal evidence to guide their decisions that directly affect troops on the ground.</p>
<p>The registry captures details about wounds received and the medical care provided from combat support hospitals, aboard ships and aircraft and throughout the course of their treatment, as well as the results. This shows medical care providers what treatments were most effective as they apply those lessons learned to other patients with similar wounds. Medical care providers call this the most important stage of the patient's treatment and ultimate recovery. The registry also helps medical instructors better tailor their training for the theater.</p>
<p>Providing more information and speeding up its delivery is a slow, labor-intensive process that involves sorting through files of hand-written notes from weary battlefield healthcare providers, extracting the critical details, translating them into medical codes and entering them into the database. Nevertheless, the database is providing combat trauma care information which was never before available, and certainly not while the war was still under way. In the past, medical data from the theater was never collected, and inpatient records were retired to the National Personnel Records Center in St. Louis as soon as each patient left the hospital.</p>
<p>NOTE: JTTR data can only be shared with government entities.</p></td>
</tr>
<tr class="even">
<td colspan="2">JPTA</td>
<td colspan="3"><em>See</em> <a href="#Glos_JTPA">Joint Patient Tracking Application</a></td>
</tr>
<tr class="odd">
<td colspan="2">JTTR</td>
<td colspan="3"><em>See</em> <a href="#Glos_JTTR">Joint Theatre Trauma Registry</a></td>
</tr>
<tr class="even">
<td colspan="2">JTTS</td>
<td colspan="3"><em>See</em> <a href="#Glos_JTTS">Joint Theater Trauma System</a></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>
| Term or Acronym                            |                      |                                                                                                                                                 | Description |     |
|--------------------------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----|
| <span id="G_K" class="anchor"></span>K |                      |                                                                                                                                                 |             |     |
| Kit                                        |                      | Medical supplies used to collect specimens or fragments. Also referred to as specimen collection kit or fragment collection kit as appropriate. |             |     |
| [ BACK ](#glossary)                    | to Glossary Contents |                                                                                                                                                 |             |     |
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_L" class="anchor"></span><strong>L</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_Longitudinal" class="anchor"></span>Longitudinal</td>
<td colspan="3">Occurring over a period of time.</td>
</tr>
<tr class="odd">
<td colspan="2">Laboratory Information Manager (LIM)</td>
<td colspan="3">Manager of the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other <a href="#Glos_CPRS">Computerized Patient Record System</a> functions.</td>
</tr>
<tr class="even">
<td colspan="2">Local Registry</td>
<td colspan="3">The local file of patients that were grandfathered into the registry or have passed the selection rules and been added to the registry.</td>
</tr>
<tr class="odd">
<td colspan="2">Local Registry Update</td>
<td colspan="3">This process adds new patients (that have had data entered since the last update was run and pass the selection rules) to the local registry.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_LOINC" class="anchor"></span>Logical Observation Identifiers Names and Codes (LOINC)</td>
<td colspan="3"><p>LOINC<sup>©</sup> is designed to facilitate the exchange and pooling of clinical results for clinical care, outcomes management, and research by providing a set of universal codes and names to identify laboratory and other clinical observations. The Regenstrief Institute, Inc., an internationally renowned healthcare and informatics research organization, maintains the LOINC database and supporting documentation.</p>
<p><em>See</em> <a href="http://loinc.org/">http://loinc.org/</a></p></td>
</tr>
<tr class="odd">
<td colspan="2">LOINC</td>
<td colspan="3"><em>See</em> <a href="#Glos_LOINC">Logical Observation Identifiers Names and Codes</a></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_M" class="anchor"></span><strong>M</strong></td>
</tr>
<tr class="even">
<td colspan="2">Medical SAS Datasets</td>
<td colspan="3">The VHA Medical SAS Datasets are national administrative data for VHA-provided health care utilized primarily by Veterans, but also by some non-Veterans (e.g., employees, research participants).</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_MEVIR" class="anchor"></span>Military Eye/Vision Injury Registry (MEVIR)</td>
<td colspan="3"><p>The Vision Center of Excellence and an accompanying Military Eye Injury Registry were provisions of the <a href="http://www.eyeresearch.org/leg_updates/12.20.07.html"><strong><u>Military Eye Trauma Treatment Act</u></strong> (METTA)</a> that were included in the Fiscal Year (FY) 2008 National Defense Authorization Act, passed in late January 2008.</p>
<p>The Vision Center of Excellence addresses the prevention, diagnosis, mitigation, treatment, and rehabilitation of military eye injuries, as well as coordinates work on the Injury Registry. The Center also facilitates vision research, including research on prevention, visual dysfunction related to traumatic brain injury (TBI), and military eye injuries. Although the Vision Center of Excellence is a Department of Defense (DOD) program, it coordinates with the Department of Veterans Affairs (VA). It is headquartered in the Washington, D.C. area and coordinates with Clinical Centers of Excellence around the country at existing medical centers.</p></td>
</tr>
<tr class="even">
<td colspan="2">MHA3</td>
<td colspan="3">Mental Health Assessment – 3</td>
</tr>
<tr class="odd">
<td colspan="2">MTFs</td>
<td colspan="3">Medical Treatment Facilities</td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>
<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th colspan="2">Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_N" class="anchor"></span><strong>N</strong></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">NAACCR</td>
<td><em>See</em> <a href="#Glos_NAACCR">North American Association of Central Cancer Registries</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">NAHIT</td>
<td><em>See</em> <a href="#Glosa_NAHIT">National Alliance for Health Information Technology</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><span id="Glosa_NAHIT" class="anchor"></span>National Alliance for Health Information Technology (NAHIT)</td>
<td>NAHIT was founded in 2002 as a technical standards organization. In 2004, it launched a comprehensive directory of healthcare IT standards, intended to be a starting point and common ground for healthcare organizations and vendors that are discussing IT implementations. In 2005, NAHIT began calling itself “The Alliance.” NAHIT ceased operation on 9/30/2009, saying it had accomplished its mission.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><span id="Glos_NCI" class="anchor"></span>National Cancer Institute (NCI)</td>
<td>NCI coordinates the National Cancer Program, which conducts and supports research, training, health information dissemination, and other programs with respect to the cause, diagnosis, prevention, and treatment of cancer, rehabilitation from cancer, and the continuing care of cancer patients and the families of cancer patients.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">National Case Registry (NCR)</td>
<td>All sites running the TBI software transmit their data to the central database for the registry.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><span id="Glos_NDS" class="anchor"></span>National Data Service (NDS)</td>
<td>NDS is a division of Information Assurance, VHA Office of Information. It maintains an inventory of corporate databases and produces the Corporate Databases Monograph. NDS is the primary source for data coming in to the Data Store.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><span id="Glos_NHIN" class="anchor"></span>National Health Information Network (NHIN)</td>
<td>NHIN is a collection of standards, protocols, legal agreements, specifications, and services that enables the secure exchange of health information over the internet. The NHIN is a key component of the nationwide health information technology strategy and will provide a common platform for health information exchange across diverse entities, within communities and across the country.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><span id="Glos_NLB" class="anchor"></span>National Leadership Board (NLB)</td>
<td>NLB plays an active and extensive role in determining VHA policy, strategy, and oversight of organizational performance. It serves as a forum to advise the Under Secretary for Health regarding the Department’s mission, goals, and priorities. The NLB also develops and disseminates information both internal and external to the organization, and facilitates the inclusion of diverse views and opinions of various organizational constituencies within VHA.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><span id="Glos_NPCD" class="anchor"></span>National Patient Care Database (NPCD)</td>
<td><p>The NPCD is the source data for the VHA Medical SAS Datasets. NPCD is the VHA's centralized relational database (a data warehouse) that receives encounter data from VHA clinical information systems. It is updated daily.</p>
<p>NPCD records include updated patient demographic information, the date and time of service, the practitioner(s) who provided the service, the location where the service was provided, diagnoses, and procedures. NPCD also holds information about patients' assigned Primary Care Provider and some patient status information such as exposure to Agent Orange, Ionizing Radiation or Environmental Contaminants, Military Sexual Trauma, and Global Assessment of Functioning.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><span id="Glos_NTEO" class="anchor"></span>National Training and Education Office (NT&amp;EO)</td>
<td>Veterans Health Administration’s Office of Information (VHA OI) NT&amp;EO provides materials that address the function and purpose of the Bi-directional Laboratory Data Sharing initiative for sites’ executive level management and IRM staff.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">NCI</td>
<td><em>See</em> <a href="#Glos_NCI">National Cancer Institute</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">NDS</td>
<td><em>See</em> <a href="#gLOS_nds">National Data Service</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">NHIN</td>
<td><em>See</em> <a href="#Glos_NHIN">National Health Information Network</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">NLB</td>
<td><em>See</em> <a href="#Glos_NLB">National Leadership Board</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><span id="Glos_NAACCR" class="anchor"></span>North American Association of Central Cancer Registries (NAACCR)</td>
<td>A professional organization that develops and promotes uniform data standards for cancer registration; provides education and training; certifies population-based registries; aggregates and publishes data from central cancer registries; and promotes the use of cancer surveillance data and systems for cancer control and epidemiologic research, public health programs, and patient care to reduce the burden of cancer in North America.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">NPCD</td>
<td><em>See</em> <a href="#Glos_NPCD">National Patient Care Database</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">NT&amp;EO</td>
<td><em>See</em> <a href="#Glos_NTEO">National Training and Education Office</a></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="4">to Glossary Contents</td>
</tr>
</tbody>
</table>
|                                                                                                     |                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term or Acronym                                                                                     |                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="G_O" class="anchor"></span>O                                                          |                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| OCO                                                                                                 |                      | *See* [Overseas Contingency Operation](#Glos_OCO)                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| OEF/OIF                                                                                             |                      | Operation Enduring Freedom/Operation Iraqi Freedom                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| OEF/OIF Coordinators and Case Managers                                                              |                      | Each VA Medical Center has an OEF/OIF case management team, consisting of a nurse or social worker program manager leading the program; a nurse or social worker case manager providing clinical case management services; and a transition patient advocate acting as an ombudsman for the patient and family. The OEF/OIF Coordinators and Case Managers may initiate the referral to the TBI and need to be aware of the TEFSC protocols; however, they will not need access to the registry. |
| <span id="Glos_OFHPR" class="anchor"></span>Office of Force Health Protection and Readiness (OFHPR) |                      | OFHPR serves as the principal staff assistant and advisor to the Assistant Secretary of Defense (Health Affairs) for all DoD deployment medicine policies, programs, and activities. In carrying out these responsibilities the office is responsible for deployment related health policy, doctrine, theater information systems, system rightsizing, and international agreements.                                                                                                             |
| OPCS                                                                                                |                      | *See* [Patient Care Services](#Glos_PCS)                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| OIT                                                                                                 |                      | Office of Information Technology                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="Glos_OCO" class="anchor"></span>Overseas Contingency Operation (OCO)                      |                      | Term used to replace the terms Global War on Terror (GWOT) and "Long War." Per direction from the Office of Management and Budget (OMB) through the VA Communications Division, the terms *GWOT* and *Long War* are no longer to be used and are being replaced with *Overseas Contingency Operation*.                                                                                                                                                                                           |
| [ BACK ](#glossary)                                                                             | to Glossary Contents |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Term or Acronym                                                                     |                       |                                                                                                                                                                                                                                                                                                                                                                        | Description |
|-------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| <span id="G_P" class="anchor"></span>P                                          |                       |                                                                                                                                                                                                                                                                                                                                                                        |             |
| <span id="Glos_PCS" class="anchor"></span>Patient Care Services (PCS), Office of    |                       | OPCS oversees VHA's clinical programs that support and improve Veterans' health care. The VA's broad approach to Veteran care incorporates expert knowledge, clinical practice and patient care guidelines in all aspects of care.                                                                                                                                     |             |
| PCS                                                                                 |                       | *See* [Patient Care Services](#Glos_PCS)                                                                                                                                                                                                                                                                                                                               |             |
| <span id="Glos_PII" class="anchor"></span>Personally Identifiable Information (PII) |                       | PII refers to information that can be used to uniquely identify, contact, or locate a single person or can be used with other sources to uniquely identify a single individual.                                                                                                                                                                                        |             |
| PII                                                                                 |                       | *See* [Personally Identifiable Information](#Glos_PII)                                                                                                                                                                                                                                                                                                                 |             |
| Protocol                                                                            |                       | A protocol is a convention or standard that controls or enables the connection, communication, and data transfer between two computing endpoints. In its simplest form, a protocol can be defined as the rules governing the syntax, semantics, and synchronization of communication. Protocols may be implemented by hardware, software, or a combination of the two. |             |
| Provider                                                                            |                       | An organization or individual who delivers health care in a professional, systematic way to any individual in need of health care services. For purposes of the TBI, Providers will be considered as individual health care practitioners.                                                                                                                             |             |
| [ BACK ](#glossary)                                                             | tvo Glossary Contents |                                                                                                                                                                                                                                                                                                                                                                        |             |
| Term or Acronym                            | Description |
|--------------------------------------------|-------------|
| <span id="G_Q" class="anchor"></span>Q |             |
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th>Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_R" class="anchor"></span><strong>R</strong></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Raw Lab Results</td>
<td colspan="2">Lab results from either the Baltimore VAMC laboratory or from the AFIP laboratory that have not been reviewed or interpreted by a TEFSC Provider.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">RCB</td>
<td colspan="2"><em>See</em> <a href="#Glos_RCB">Recognized Certification Body</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_RO" class="anchor"></span>read only (RO)</td>
<td colspan="2">The term <em>read only</em> usually refers to something that can be read, but not written to or modified. In programming, a data variable can be declared as RO, which prevents modification to the values. In TBI, this applies specifically to several categories of data, including basic information about a patient.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Referral</td>
<td colspan="2">To send or direct for treatment, aid, information, or decision. For the purposes of the TBI, a referral may also mean the data sent to identify a patient being referred.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Registry</td>
<td colspan="2"><p>The VHA Registries Program supports the population-specific data needs of the enterprise including (but not limited to) the <a href="#Glos_CCR">Defense/Veterans Eye Injury Registry</a>, Oncology Tumor Registry, Traumatic Brain Injury Registry, Embedded Fragment Registry and Eye Trauma Registry.</p>
<p><em>Also,</em> a database containing a collection of data relating to a disease or condition.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">RO</td>
<td colspan="2"><em>See</em> <a href="#Glos_RO">read only</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Roll-and-scroll, roll’n’scroll</td>
<td colspan="2">“Scrolling” is a display framing technique that allows the user to view a display as moving behind a fixed frame. The scrolling action typically causes the data displayed at one end of the screen to move across it, toward the opposite end. When the data reach the opposite edge of the screen they are removed (i.e., scroll off of the screen). Thus, old data are removed from one end while new data are added at the other. This creates the impression of the display page being on an unwinding scroll, with only a limited portion being visible at any time from the screen; i.e., the display screen is perceived as being stationary while the displayed material moves (scrolls) behind it. Displays may be scrolled in the top-bottom direction, the left-right direction, or both. Traditionally, VistA data displays have been referred to as “roll-and-scroll” for this reason.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Routine</td>
<td colspan="2">A set of programming instructions designed to perform a specific limited task.</td>
<td></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="4">to Glossary Contents</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_S" class="anchor"></span><strong>S</strong></td>
</tr>
<tr class="even">
<td colspan="2">Screen Reader</td>
<td colspan="3"><p>“Screen reader” software is designed to make personal computers using Microsoft Windows® accessible to blind and visually impaired users. It accomplishes this by providing the user with access to the information displayed on the screen via text-to-speech or by means of a Braille display and allows for comprehensive keyboard interaction with the computer.</p>
<p>It also allows users to create custom scripts using the JAWS Scripting Language, which can alter the amount and type of information which is presented by applications, and ultimately makes programs that were not designed for accessibility (such as programs that do not use standard Windows controls) usable through JAWS.</p></td>
</tr>
<tr class="odd">
<td colspan="2">Screening</td>
<td colspan="3">The process of determining if a Veteran should be referred to the TBI for follow-up.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_508" class="anchor"></span>Section 508</td>
<td colspan="3"><p>Section 508 of the Rehabilitation Act as amended, <a href="http://frwebgate.access.gpo.gov/cgi-bin/getdoc.cgi?dbname=browse_usc&amp;docid=Cite:+29USC794d">29 U.S.C. Section 794(d)</a>, requires that when Federal agencies develop, procure, maintain, or use electronic and information technology, they shall ensure that this technology is accessible to people with disabilities. Agencies must ensure that this technology is accessible to employees and members of the public with disabilities to the extent it does not pose an “undue burden.” Section 508 speaks to various means for disseminating information, including computers, software, and electronic office equipment.</p>
<p>The TBI must be 508 compliant, able to extract data as needed including <a href="#Glos_SNOMED">SNOMED</a> codes.</p></td>
</tr>
<tr class="odd">
<td colspan="2">SEER</td>
<td colspan="3"><em>See</em> <a href="#Glos_SEER">Surveillance, Epidemiology and End Results</a></td>
</tr>
<tr class="even">
<td colspan="2">Selection Rules</td>
<td colspan="3">A pre-defined set of rules that define a registry patient.</td>
</tr>
<tr class="odd">
<td colspan="2">Sensitive Information</td>
<td colspan="3">Any information which requires a degree of protection and which should be made available only to authorized system users.</td>
</tr>
<tr class="even">
<td colspan="2">Server</td>
<td colspan="3">In information technology, a server is a computer system that provides services to other computing systems—called clients—over a network. The server is where VistA M-based data and Business Rules reside, making these resources available to the requesting server.</td>
</tr>
<tr class="odd">
<td colspan="2">SGML</td>
<td colspan="3"><em>See</em> <a href="#Glos_SGML">Standardized Generic Markup Language</a></td>
</tr>
<tr class="even">
<td colspan="2">Single Sign On</td>
<td colspan="3">Single Sign On is the process that enables the secure access of disparate applications by a user through use of a single authenticated identifier and password.</td>
</tr>
<tr class="odd">
<td colspan="2">Site Configurable</td>
<td colspan="3">A term used to refer to features in the system that can be modified to meet the needs of each local site.</td>
</tr>
<tr class="even">
<td colspan="2">SNOMED</td>
<td colspan="3"><em>See</em> <a href="#Glos_SNOMED">Systematized Nomenclature of Medicine</a></td>
</tr>
<tr class="odd">
<td colspan="2">SLP</td>
<td colspan="3">Speech-language Pathologists.</td>
</tr>
<tr class="even">
<td colspan="2">SQL</td>
<td colspan="3"><em>See</em> <a href="#Glos_SQL">Structured Query Language</a></td>
</tr>
<tr class="odd">
<td colspan="2">SQL Server</td>
<td colspan="3"><em>See</em> <a href="#Glos_SQLServer">Structured Query Language Server</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SSIS" class="anchor"></span>SQL Server Integration Services (SSIS)</td>
<td colspan="3"><p>SSIS is a component of the Microsoft <a href="#Glos_SQL">SQL Server</a> database software which can be used to perform a broad range of data migration tasks.</p>
<p>SSIS is a platform for data integration and workflow applications. It features a data warehousing tool used for data <a href="#Glos_ETL">extraction, transformation, and loading (ETL)</a>. The tool may also be used to automate maintenance of SQL Server databases and updates to extremely complex data.</p></td>
</tr>
<tr class="odd">
<td colspan="2">SSIS</td>
<td colspan="3"><em>See</em> <a href="#Glos_SSIS">SQL Server Integration Services</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SGML" class="anchor"></span>Standardized Generic Markup Language (SGML)</td>
<td colspan="3">A generic markup language for representing documents. SGML is an International Standard that describes the relationship between a document’s content and its structure. SGML allows document-based information to be shared and re-used across applications and computer platforms in an open, vendor-neutral format.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SQL" class="anchor"></span>Structured Query Language (SQL)</td>
<td colspan="3"><p>An industry-standard language for creating, updating and, querying relational database management systems. SQL was originally based upon relational algebra. Its scope includes data query and update, schema creation and modification, and data access control. The data displayed in TBI is stored in SQL databases.</p>
<p>Typically, the acronym SQL (<em>pronounced</em> “sequel”) is used instead of the actual phrase.</p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SQLServer" class="anchor"></span>Structured Query Language Server (SQL Server)</td>
<td colspan="3">A relational database management system (RDBMS) which is part of the Microsoft® BackOffice® family of servers. SQL Server was designed for client/server use and is accessed by applications using SQL. It runs on Windows NT version 3.5 or higher and is compliant with the ANSI SQL-92 and FIPS 127-2 SQL standards.</td>
</tr>
<tr class="odd">
<td colspan="2">Surveillance</td>
<td colspan="3">Systematic collection, analysis, and interpretation of health data about a disease or condition.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SEER" class="anchor"></span>Surveillance, Epidemiology and End Results (SEER)</td>
<td colspan="3">A program of the National Cancer Institute, SEER is a source of information on cancer incidence and survival in the United States.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SNOMED" class="anchor"></span>Systematized Nomenclature of Medicine (SNOMED)</td>
<td colspan="3">SNOMED is a terminology that originated as the systematized nomenclature of pathology (SNOP) in the early 1960s under the guidance of the College of American Pathologists. In the late 1970s, the concept was expanded to include most medical domains and renamed SNOMED. The core content includes text files such as the concepts, Descriptions, relationships, ICD-9 mappings, and history tables. SNOMED represents a terminological resource that can be implemented in software applications to represent clinically relevant information comprehensive (&gt;350,000 concepts) multi-disciplinary coverage but discipline neutral structured to support data entry, retrieval, maps, etc.</td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_T" class="anchor"></span><strong>T</strong></td>
</tr>
<tr class="even">
<td colspan="2">“The Alliance”</td>
<td colspan="3"><em>See</em> <a href="#Glosa_NAHIT">National Alliance for Health Information Technology</a></td>
</tr>
<tr class="odd">
<td colspan="2">TBI</td>
<td colspan="3"><em>See</em> <a href="#Glos_TBI">Traumatic Brain Injuries</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_TSPR" class="anchor"></span>Technical Services Project Repository (TSPR)</td>
<td colspan="3"><p>The TSPR is the central data repository and database for VA Health IT (VHIT) project information.</p>
<p><em>See</em> <a href="http://tspr.vista.med.va.gov/tspr/default.htm">http://tspr.VistA.med.va.gov/tspr/default.htm</a></p></td>
</tr>
<tr class="odd">
<td colspan="2">Terminal emulation software</td>
<td colspan="3">A program that allows a personal computer (PC) to act like a (particular brand of) terminal. The PC thus appears as a terminal to the host computer and accepts the same escape sequences for functions such as cursor positioning and clearing the screen. Attachmate <em>Reflection</em> is widely used in VHA for this purpose.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_TIU" class="anchor"></span>Text Integration Utilities (TIU)</td>
<td colspan="3"><p>TIU simplifies the use and management of clinical documents for both clinical and administrative medical facility personnel. In connection with the Authorization/ Subscription Utility (ASU), a facility can set up policies and practices for determining who is responsible or has the privilege for performing various actions on required documents.</p>
<p><em>See</em> complete discussion in <a href="#AppendixE">Appendix E</a>.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_TMDS" class="anchor"></span>Theater Medical Data Store (TMDS)</td>
<td colspan="3"><p>The main purpose of TMDS is to give health care providers an unclassified Web-based means of accessing the same theater medical information collected by the <a href="#Glos_JMeWS">Joint Medical Workstation</a> (JMeWS). Because TMDS uses the same baseline code as JMeWS, medical surveillance and medical command and control features can be activated in support of unclassified operations during a disaster or mass casualty event in the Continental United States or elsewhere.</p>
<p>On May 1, 2008, the Joint Patient Tracking Application (JPTA) was merged with TMDS into a single application, which retained the name of TMDS. All data transferred to the Veterans Tracking Application will come from TMDS.</p>
<p>TMDS is built on the same baseline code as the <a href="#Glos_JMeWS">Joint Medical Workstation</a> (JMeWS), but the features that make JMeWS a classified system (such as medical command and control and the aggregation of population health data for medical surveillance) have been turned off in TMDS to allow it to be run on the Non-classified but Sensitive Internet Protocol Network (NIPRNet).</p></td>
</tr>
<tr class="even">
<td colspan="2">TMDS</td>
<td colspan="3"><em>See</em> <a href="#Glos_TMDS">Theater Medical Data Store</a></td>
</tr>
<tr class="odd">
<td colspan="2">Tool tips</td>
<td colspan="3">Tool tips are “hints” assigned to menu items which appear when the user “hovers” the mouse pointer over a menu.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_TBI" class="anchor"></span>Traumatic Brain Injuries (TBI)</td>
<td colspan="3">The Traumatic Brain Injuries (TBI) Registry software application allows case managers to identify those Veterans who participated in Operation Enduring Freedom (OEF) or Operation Iraqi Freedom (OIF) and who sustained a head injury and thus are potential traumatic brain injury (TBI) patients. The TBI application permits the case manager to oversee and track the comprehensive evaluation of those patients. It also provides 17 types of reports used for tracking the evaluation and care of individuals identified as possible TBI candidates.</td>
</tr>
<tr class="odd">
<td colspan="2">TSPR</td>
<td colspan="3"><em>See</em> <a href="#Glos_TSPR">Technical Services Project Repository</a></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_U" class="anchor"></span><strong>U</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="glos_URL" class="anchor"></span>Uniform Resource Locator (URL)</td>
<td colspan="3">(<em>Formerly</em> <u>Universal</u> Resource Locator). A standard way of specifying the location of an object, typically a web page, on the Internet. URLs are the form of address used on the World-Wide Web. In TBI the URL is typically a Web page which displays another application screen.</td>
</tr>
<tr class="odd">
<td colspan="2">URL</td>
<td colspan="3"><em>See</em> Uniform Resource Locator</td>
</tr>
<tr class="even">
<td colspan="2">USAF</td>
<td colspan="3"><em>Acronym for</em> United States Air Force</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_USAPHC" class="anchor"></span>U.S. Army Public Health Command (Provisional)</td>
<td colspan="3"><p>The former U.S. Army Center for Health Promotion and Preventive Medicine is now the U.S. Army Public Health Command (Provisional). The overall objectives of the USAPHC are to:</p>
<ul>
<li><p>Enhance health and wellness of Soldiers and military retirees, their families, and Army civilian employees</p></li>
<li><p>Optimize public health support to the Army</p></li>
<li><p>Create a single point of accountability and responsibility for public health within the Medical Command</p></li>
<li><p>Improve planning and use of Army public health assets across the full spectrum of installations and activities</p></li>
</ul>
<p><em>See</em> <a href="http://usachppm.apgea.army.mil/APHC/">http://usachppm.apgea.army.mil/APHC/</a></p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_UserInterface" class="anchor"></span>User Interface</td>
<td colspan="3"><p>A user interface is the means by which people (the users) interact with a particular machine, device, computer program or other complex tool (the system). The user interface provides one or more means of:</p>
<p>• Input, which allows the users to manipulate the system</p>
<p>• Output, which allows the system to produce the effects of the users’ manipulation</p>
<p>The interface may be based strictly on text (as in the traditional “roll and scroll” IFCAP interface), or on both text and graphics.</p>
<p>In computer science and human-computer interaction, the user interface (of a computer program) refers to the graphical, textual and auditory information the program presents to the user, and the control sequences (such as keystrokes with the computer keyboard and movements of the computer mouse) the user employs to control the program.</p>
<p><em>See also</em> <a href="#Glos_GUI">Graphical User Interface</a></p></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_V" class="anchor"></span><strong>V</strong></td>
</tr>
<tr class="even">
<td colspan="2">VA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VA">Veterans Affairs</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VADIR" class="anchor"></span>VA/DoD Information Repository (VADIR)</td>
<td colspan="3"><p>The VADIR database was established to support a One VA/DoD data-sharing initiative in order to consolidate data transfers between DoD and VA. The DoD Defense Manpower Data Center (DMDC) stage shared data as defined in a Memorandum of Understanding (MOU), and transmits data to VADIR. The VADIR data are used to assist in determining Veteran benefits.</p>
<p>(Note: Health data is not collected in VADIR.)</p></td>
</tr>
<tr class="even">
<td colspan="2">VACO</td>
<td colspan="3"><em>See</em> <a href="#Glos_VHACO">Veterans Affairs Central Office</a></td>
</tr>
<tr class="odd">
<td colspan="2">VADIR</td>
<td colspan="3"><em>See</em> <a href="#Glos_VADIR">VA/DoD Information Repository</a></td>
</tr>
<tr class="even">
<td colspan="2">VALU</td>
<td colspan="3">Veteran's Affairs Learning University</td>
</tr>
<tr class="odd">
<td colspan="2">VAMC</td>
<td colspan="3"><em>Acronym for</em> Veterans Affairs Medical Center</td>
</tr>
<tr class="even">
<td colspan="2">VBA</td>
<td colspan="3">Veterans Benefits Administration</td>
</tr>
<tr class="odd">
<td colspan="2">Veteran Tracking Application (VTA)</td>
<td colspan="3">A VA version of the <a href="#Glos_JTPA">Joint Patient Tracking Application</a> which provides clinicians access to medical records on combat wounded soldiers throughout the continuum of care, from the battlefield to a VA hospital.</td>
</tr>
<tr class="even">
<td colspan="2">Veteran Tracking Application (VTA) data extract</td>
<td colspan="3"><p>This extract includes the following read-only data:</p>
<ul>
<li><p>Patient Last Name</p></li>
<li><p>Patient First Name</p></li>
<li><p>Social Security Number</p></li>
<li><p>ICD-9 Codes (used by DoD in their case definition algorithm)</p></li>
<li><p>Subjective Objective Assessment and Plan (SOAP) Note Keywords (used by DoD in their case definition algorithm)</p></li>
<li><p>Patient Address Line1</p></li>
<li><p>Patient Address Line2</p></li>
<li><p>Patient City</p></li>
<li><p>Patient State</p></li>
<li><p>Patient Zip/Postal Code</p></li>
<li><p>Patient Phone (primary)</p></li>
</ul>
<p>Patient email address</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VHACO" class="anchor"></span>Veterans Affairs Central Office (VACO)</td>
<td colspan="3">The VA “headquarters” offices, located in Washington DC, which oversees field operations throughout the VA.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VA" class="anchor"></span>Veterans Affairs, Department of (VA)</td>
<td colspan="3"><p>The VA mission is to serve America's Veterans and their families with dignity and compassion and to be their principal advocate in ensuring that they receive medical care, benefits, social support, and lasting memorials promoting the health, welfare, and dignity of all Veterans in recognition of their service to this Nation.</p>
<p>VA is the second largest Federal department and has over 278,000 employees. Among the many professions represented in the vast VA workforce are physicians, nurses, counselors, statisticians, architects, computer specialists, and attorneys. As advocates for Veterans and their families, the VA community is committed to providing the very best services with an attitude of caring and courtesy.</p></td>
</tr>
<tr class="odd">
<td colspan="2">Veterans Affairs Learning University (VALU)</td>
<td colspan="3">VALU supports all employee learning and performance improvement across VA.</td>
</tr>
<tr class="even">
<td colspan="2">Veterans Benefits Administration (VBA)</td>
<td colspan="3">VBA, in partnership with the Veterans Health Administration and the National Cemetery Administration, provides benefits and services to the Veterans and their families in a responsive, timely and compassionate manner in recognition of their service to the Nation.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VHA" class="anchor"></span>Veterans Health Administration (VHA)</td>
<td colspan="3">VHA administers the United States Veterans Healthcare System, whose mission is to serve the needs of America’s Veterans by providing primary care, specialized care, and related medical and social support services.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VistA" class="anchor"></span>Veterans Health Information Systems and Technology Architecture (VistA)</td>
<td colspan="3"><p>VistA is a comprehensive, integrated health care information system composed of numerous software modules.</p>
<p><em>See</em> <a href="http://www.va.gov/vista_monograph/docs/2008VistAHealtheVet_Monograph.pdf">http://www.va.gov/VistA_monograph/docs/2008VistAHealtheVet_Monograph.pdf</a> and <a href="http://www.virec.research.va.gov/DataSourcesName/VISTA/VISTA.htm">http://www.virec.research.va.gov/DataSourcesName/VISTA/VISTA.htm</a>.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VISN" class="anchor"></span>Veterans Integrated Service Network (VISN)</td>
<td colspan="3"><a href="#Glos_VHA">VHA</a> organizes its local facilities into networks called VISNS (VA Integrated Service Networks). At the VISN level, VistA data from multiple local facilities may be combined into a data warehouse.</td>
</tr>
<tr class="even">
<td colspan="2">VHA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VHA">Veterans Health Administration</a></td>
</tr>
<tr class="odd">
<td colspan="2">VAMC</td>
<td colspan="3">Veterans Affairs Medical Center</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VSSC" class="anchor"></span>VHA Support Service Center (VSSC)</td>
<td colspan="3">The VHA Support Service Center (VSSC) was established in 1996 as an information and technical support arm for VHA healthcare operations. The VSSC delivers information, tools and technical and analytical services to support the management of field operations. The VSSC reports to the ADUSH/OM and is governed by an Advisory Board that sets organizational goals and priorities. The VSSC is structured as a decentralized, virtual organization that is customer driven and outcome oriented. The VSSC organization includes Network Services (Capital Assets, Planning and Data Analysis and Veteran Service and Advocacy), Information Management and Analysis.</td>
</tr>
<tr class="odd">
<td colspan="2">VISN</td>
<td colspan="3"><em>See</em> <a href="#Glos_VISN">Veterans Integrated Service Network</a></td>
</tr>
<tr class="even">
<td colspan="2">VistA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VistA">Veterans Health Information Systems and Technology Architecture</a></td>
</tr>
<tr class="odd">
<td colspan="2">VRAD</td>
<td colspan="3">VA/DOD Reporting and Analysis Data Mart</td>
</tr>
<tr class="even">
<td colspan="2">VSSC</td>
<td colspan="3"><em>See</em> <a href="#Glos_VSSC">VHA Support Service Center</a></td>
</tr>
<tr class="odd">
<td colspan="2">VTA</td>
<td colspan="3">Veteran Tracking Application</td>
</tr>
<tr class="even">
<td colspan="2"><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_W" class="anchor"></span><strong>W</strong></td>
</tr>
<tr class="even">
<td colspan="2">WBA</td>
<td colspan="2"><em>See</em> <a href="#Glos_WBA">Web-Based Application</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_WBA" class="anchor"></span>Web-based Application (WBA)</td>
<td colspan="2"><p>In software engineering, a web application is an application that is accessed via a web browser over a network such as the Internet or an intranet. The term may also mean a computer software application that is hosted in a browser-controlled environment (e.g. a Java applet) or coded in a browser-supported language (such as JavaScript, possibly combined with a browser-rendered markup language like HTML) and reliant on a common Web browser to render the application executable.</p>
<p>Web applications are popular due to the ready availability of web browsers, and the convenience of using a web browser as a client, sometimes called a thin client. The ability to update and maintain web applications without distributing and installing software on potentially thousands of client computers is a key reason for their popularity, as is the inherent support for cross-platform compatibility. Common web applications include webmail, online retail sales, online auctions, wikis and many other functions. The TBI is a WBA.</p>
<p><em>See also</em> <a href="#Glos_UserInterface">User Interface</a></p></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
</tr>
</tbody>
</table>
| Term or Acronym                            |                      |                                                | Description |
|--------------------------------------------|----------------------|------------------------------------------------|-------------|
| <span id="G_X" class="anchor"></span>X |                      |                                                |             |
| XML                                        |                      | *See* [Extensible Mark-up Language](#Glos_XML) |             |
| [ BACK ](#glossary)                    | to Glossary Contents |                                                |             |
