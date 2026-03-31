---
title: TBI Version 4.2 Polytrauma User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Polytrauma
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
  - table
  - contents
  - glos
  - polytrauma
  - even
  - blockquote
  - anchor
page_count: 0
word_count: 27076
section_count: 29
table_count: 27
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: January 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbiptum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbiptum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=198"
---

---
title: |
  <span id="_Toc495855387" class="anchor"></span>Traumatic Brain Injury (TBI)

  Polytrauma Edition User Manual
---

![](tbi-version-4-2-polytrauma-user-manual/001.png)

January 2018

Office of Information and Technology (OIT)

Product Development

Revision History

<table style="width:100%;">
<caption><p><span id="_Toc501011965" class="anchor"></span>Table 1 - Typographical Conventions</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 32%" />
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Version</td>
<td>Description</td>
<td>Author</td>
<td>Reviewer(s)</td>
<td>Review Type</td>
<td>Issue Date</td>
</tr>
<tr class="even">
<td>0.1</td>
<td>First Draft</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td></td>
<td>8/30/10</td>
</tr>
<tr class="odd">
<td>0.2</td>
<td>Second Draft</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td>Technical</td>
<td>9/22/10</td>
</tr>
<tr class="even">
<td>0.3</td>
<td>Third Draft</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td>Edit</td>
<td>9/22/10</td>
</tr>
<tr class="odd">
<td>1.0</td>
<td>Version 1 - Final</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td></td>
<td>9/22/10</td>
</tr>
<tr class="even">
<td>1.1</td>
<td>Minor textual edits, scrubbed screenshots of potential PII</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td></td>
<td>9/08/11</td>
</tr>
<tr class="odd">
<td>1.2</td>
<td>Updated for Increment 4. No major updates, minor formatting updates</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td></td>
<td>4/25/12</td>
</tr>
<tr class="even">
<td>4.0</td>
<td>Version 4 - Final</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td>Peer</td>
<td>5/1/12</td>
</tr>
<tr class="odd">
<td>4.1</td>
<td>Updated screenshots</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td></td>
<td>4/8/14</td>
</tr>
<tr class="even">
<td>4.2</td>
<td>Updated screenshots and language for PRC and PTRP</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td></td>
<td>8/10/14</td>
</tr>
<tr class="odd">
<td>4.3</td>
<td>Reviewed for TBI Enhancements Increment 1. No updates necessary.</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td></td>
<td>7/7/15</td>
</tr>
<tr class="even">
<td>4.4</td>
<td><p>Removed FireFox as an approved Web Browser and updated document dates.</p>
<p>Added version 4.4 to the title page.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td></td>
<td>11/31/15</td>
</tr>
<tr class="odd">
<td>4.5</td>
<td>Updated for new release and 508 compliance.</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td></td>
<td>10/31/17</td>
</tr>
<tr class="even">
<td>4.6</td>
<td>Updated for changes to User Roles.</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td></td>
<td>12/01/17</td>
</tr>
</tbody>
</table>

<span id="_Toc501011965" class="anchor"></span>Table 1 - Typographical Conventions

Table of Contents

List of Tables

Table of Figures

1.  
2.  Introduction

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
    - [TBI Administrator](#tbi-administrator)
    - [TBI Editor](#tbi-editor)
    - [TBI Read Only](#tbi-read-only)
    - [TBI Polytrauma Editor](#tbi-polytrauma-editor)
    - [TBI Polytrauma Read Only](#tbi-polytrauma-read-only)
    - [TBI Reporting User National](#tbi-reporting-user-national)
    - [TBI Reporting User VISN](#tbi-reporting-user-visn)
    - [TBI Reporting User Station](#tbi-reporting-user-station)
    - [TBI Rehabilitation and Polytrauma Clinicians](#tbi-rehabilitation-and-polytrauma-clinicians)
    - [TBI Technical Support Administrator](#tbi-technical-support-administrator)
- [# Software Details](#software-details)
  - [Starting the Application](#starting-the-application)
  - [Logging In](#logging-in)
  - [Default Registry Page](#default-registry-page)
- [TBI Registry Tabs](#tbi-registry-tabs)
  - [Accessing Tasks](#accessing-tasks)
  - [Error and Warning Messages](#error-and-warning-messages)
  - [TBI Registry Applications](#tbi-registry-applications)
- [Polytrauma Entries Application](#polytrauma-entries-application)
  - [Polytrauma Rehabilitation Center (PRC) Admission and Follow Up](#polytrauma-rehabilitation-center-prc-admission-and-follow-up)
  - [Polytrauma Transitional Rehabilitation Program (PTRP) Admission and Follow Up](#polytrauma-transitional-rehabilitation-program-ptrp-admission-and-follow-up)
- [Polytrauma Patient Lookup Application](#polytrauma-patient-lookup-application)
  - [Polytrauma Patients Lookup](#polytrauma-patients-lookup)
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
- [Pop-up Windows](#pop-up-windows-1)
- [Web-based Application (WBA) Elements](#web-based-application-wba-elements)
- [Text Box](#text-box)
- [Radio Button](#radio-button)
- [Command Buttons](#command-buttons)
- [Date Fields](#date-fields)
- [Drop-down List](#drop-down-list)
- [List Box](#list-box)
- [Faded (“Grayed Out”) Choices](#faded-grayed-out-choices)
- [Keyboard Commands](#keyboard-commands)
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
- [Using the \< Ctrl \>, \< Alt \> and \< Esc \> Keys](#using-the-ctrl-alt-and-esc-keys)
- [Resizing the Browser Screen](#resizing-the-browser-screen)
- [Windows Accessibility Features](#windows-accessibility-features)
- [StickyKeys](#stickykeys)
- [FilterKeys](#filterkeys)
- [ToggleKeys](#togglekeys)
- [MouseKeys](#mousekeys)
- [HighContrast](#highcontrast)
- [Glossary](#glossary)

## Typographical Conventions Used in the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other conventions are used:

<table>
<caption><p><span id="_Toc501011966" class="anchor"></span>Table 2 - Graphical Conventions</p></caption>
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

<span id="_Toc501011966" class="anchor"></span>Table 2 - Graphical Conventions

| Graphic                                                                                                                                                                                 | Used for…                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](tbi-version-4-2-polytrauma-user-manual/002.png)            | Information of particular interest regarding the current subject matter.               |
| ![](tbi-version-4-2-polytrauma-user-manual/003.png)                                                              | A tip or additional information that may be helpful to the user.                       |
| ![](tbi-version-4-2-polytrauma-user-manual/004.png)                                                           | A warning concerning the current subject matter.                                       |
| ![](tbi-version-4-2-polytrauma-user-manual/005.png) | Information about the history of a function or operation; provided for reference only. |
| ![](tbi-version-4-2-polytrauma-user-manual/006.png)                | Indicates an action or process which is optional                                       |
| ![](tbi-version-4-2-polytrauma-user-manual/007.png)                      | Indicates a resource available either in this document or elsewhere                    |

<span id="_Toc501011967" class="anchor"></span>Table 3 - Locations for Documentation Files

## Command Buttons and Command Icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Command Button/Icon                                                                                                                       | Description                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tbi-version-4-2-polytrauma-user-manual/008.png)                                           | A command button initiates an action. It is a rectangular “3-dimensional” shape with a label that specifies what action will be performed when the button is clicked. |
| ![](tbi-version-4-2-polytrauma-user-manual/009.png)      | Common examples are shown at left. Command buttons that end with three dots indicate that selecting the command may evoke a subsidiary window.                        |
| ![](tbi-version-4-2-polytrauma-user-manual/010.png)                                              | In some cases, a command icon performs the same function, but appears on the menu bar and has a plain, flat appearance. One example is shown at left.                 |
| ![](tbi-version-4-2-polytrauma-user-manual/011.png) | In the text of this document, both command button and command icon names appear inside square brackets. Examples: \[Search\], \[Save\].                               |

<span id="_Toc501011968" class="anchor"></span>Table 4 - Document File Sets

## The Traumatic Brain Injury Registry Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](tbi-version-4-2-polytrauma-user-manual/012.png)Note: Throughout this document, the terms…

- “Registry” and “TBI” both refer to the Traumatic Brain Injury Registry
- “Traumatic Brain Injury Registry” and the corresponding acronym TBI Registry both refer to the [Web-based application (WBA)](#Glos_WBA) described in this document.

The Traumatic Brain Injury Registry application (TBI Registry) supports the maintenance of local and national registries for clinical and resource tracking of care for such Veterans. The TBI Registry software application allows case managers to identify Veterans who participated in Operation Enduring Freedom (OEF) or Operation Iraqi Freedom (OIF) and who sustained a head injury and thus are potential traumatic brain injury (TBI) patients. The TBI Registry permits the case manager to oversee and track the comprehensive evaluation of these patients. It also provides 17 types of reports used for tracking the evaluation and care of individuals identified as possible TBI candidates.

TBI Registry accesses several other [Veterans Health Information Systems and Technology Architecture](#Glos_VistA) ([VistA](#Glos_VistA)) files that contain information regarding other diagnoses, prescriptions, surgical procedures, laboratory tests, radiology exams, patient demographics, hospital admissions, and clinical visits. This access allows identified TBI Registry users to take advantage of the wealth of data supported through VistA.

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

The Traumatic Brain Injury (TBI) Registry software application collects data on the population of Veterans who participated in Operation Enduring Freedom/Operation Iraqi Freedom (OEF/OIF). These individuals need to be seen within 30 days for a comprehensive TBI evaluation. Each facility can produce local reports (information related to patients evaluated and treated in their system).

## Project Scope and Objectives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document applies to the TBI Registry project OBS-104-05-01-004. It does not address a broader vision that may apply to a future integration of multiple medical data registries.

In the early stages of planning for the TBI Registry, one approach considered a gradual implementation of functionality supporting very basic operations by making temporary modifications to the existing Veterans Health Information Systems and Technology Architecture (VistA) system. These modifications were limited in scope and temporary in nature and as such have been developed as an interim solution. This interim solution is under consideration for delivery. The development of the TBI Registry described in this document describes a more mature product to replace the interim solution.

## Traumatic Brain Injury Registry Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TBI Registry consists of the following applications:

- Polytrauma Entries Application: Provides a Web-based repository of patients identified as having sustained multiple injuries in the OEF/OIF missions.
- TBI and Polytrauma Patient Lookup: An application that searches the TBI Registry’s data for available information on patients.
- TBI Registry User Administration: Provides information about the TBI Registry’s users and management of the system.
- TBI Role Administration: Provides management and control of access to the system through the use of defined user roles.

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Basic data about individuals is provided by the data feed from the VA [National Data Systems (NDS)](#Glos_NDS). One purpose of TBI Registry is to provide a means of making text data “[computable](#Glos_computabledata).”

The TBI Registry is not installed on your computer workstation. Rather, TBI Registry runs in a Web [browser](#Glos_Browser) from a location on the VA [intranet](#Glos_Intranet). For that reason, TBI Registry is referred to as a “Web-based application” (WBA). If you have already used any program which runs in a Web browser, especially another registry program (like the Embedded Fragments Registry), the TBI Registry will seem familiar to you. Although it is likely that the application will run on many different Web browsers, please see [Appendix E](#AppendixE) for the browsers which have been tested and approved for use with TBI Registry.

![](tbi-version-4-2-polytrauma-user-manual/013.png)Note: This document does not attempt to explain everything about how to operate in the Web browser environment itself; if you need help with using a browser, please contact your supervisor for information about training in browser use.

<table>
<caption><p><span id="_Toc501011969" class="anchor"></span>Table 5 - Tabs by Role</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-polytrauma-user-manual/014.png)</th>
<th><p><strong>WARNING:</strong> This application will display <a href="#Glos_PII">personally identifiable information</a> (<a href="#Glos_PII">PII</a>). When you have finished using the application, you should <em>close all instances of your browser</em> that may be running (not just the one you used to access the application).</p>
<p>If you do not, PII could be compromised if another user accesses your Web browser.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc501011969" class="anchor"></span>Table 5 - Tabs by Role

### Data Receipt and Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Basic Patient Data

Within the TBI Registry, basic patient information is provided by the “[back-end](#Glos_backend)” system and is [read only (RO)](#Glos_RO). Since the data feed process is designed to produce a single record for each person, there should not be multiple records for the same person, although that could happen. In the future, a process will be available to allow users to place the record into a “pending” status until the duplicates can be resolved.

## Release History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since this is the first release of the software, there is no past “history” to record here. Future releases will include that history. Changes provided by releases are shown in the following series of tables. Under “Type,” “E” indicates an enhancement, “F” a fix, and “M” a modification. Click on the green links immediately below to jump directly to a specific release.

### TBI Registry Release 1.0 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                     | Type |
|-----|-------------------------------------------------|------|
| 1   | Published application for first production use. | E    |

<span id="_Toc501011970" class="anchor"></span>Table 6 – Tasks by Role

## Obtaining Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no TBI Registry software distributives. Since TBI Registry is a Web-based application, only a VA-approved Web [browser](#Glos_Browser) (see the list at [Appendix D](#AppendixD)) and access to the VA [intranet](#Glos_Intranet) is required.

Documentation files are available for downloading from the following Office of Information and Technology Field Offices (OI&T FO) \[ANONYMOUS SOFTWARE\] directories. [File Transfer Protocol (FTP)](#Glos_FTP) client software may be useful, although it is possible to download these files using a Web browser as well.

| OIFO                               | FTP Address                        | Directory                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

<span id="_Toc501011971" class="anchor"></span>Table 7 - Task Categories and Descriptions

The TBI REGISTRY guides and manuals are distributed as the following set of files.

<table>
<caption><p><span id="_Toc265044311" class="anchor"></span>Table 8 - TBI Registry Applications</p></caption>
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
<p>►      TBI Application User Manual (TBI_INC4_UM_062312_Final)</p>
<p>►      TBI Instruments User Manual (TBIINSUM_INC4_UM_062312_Final)</p>
<p>►      TBI Polytrauma User Manual (TBIPTUM_INC4_UM_062312_Final)</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>TBI REGISTRY2_0DOC2.ZIP</td>
<td><p>►      TBI Installation Guide (TBIIG_INC4_UM_062312_Final)</p>
<p>►      TBI Systems Management Guide (TBITM_INC4_UM_062312_Final)</p></td>
<td>BINARY</td>
</tr>
</tbody>
</table>

<span id="_Toc265044311" class="anchor"></span>Table 8 - TBI Registry Applications

## Documentation on the Intranet 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this product, including all of the software manuals, is also available in the Health*<u>e</u>*Vet section of the VA Software Document Library (VDL). The Defense/Veterans Traumatic Brain Injury Registry documentation may be found at <http://www.va.gov/vdl/application.asp?appid=198>.

1.  About the Application

# Software Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc501011973" class="anchor"></span>Table 9 - Standard Web Browser Shortcut Keys</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-polytrauma-user-manual/015.png)</th>
<th><p><strong>WARNING:</strong> This application will display <a href="#Glos_PII">personally identifiable information</a> (<a href="#Glos_PII">PII</a>). When you have finished using the application, you should <em>close all instances of your browser</em> that may be running (not just the one you used to access the application).</p>
<p>If you do not, PII could be compromised if another user accesses your Web browser.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc501011973" class="anchor"></span>Table 9 - Standard Web Browser Shortcut Keys

## Web-based Application Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a [Web-based application](#Glos_WBA); see [Appendix D](#AppendixD) for a description of typical Web-based application (WBA) elements.

## Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two kinds of online help are or will be available: help for using the browser itself, and help for TBI Registry.

| ![](tbi-version-4-2-polytrauma-user-manual/016.png) | Help files are available by clicking on the ![](tbi-version-4-2-polytrauma-user-manual/017.png) icon. Help files are available for the Polytrauma application. |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc501011974" class="anchor"></span>Table 10 - Approved Browsers

### Browser Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have little or no familiarity with the browser environment, information can be found by accessing the browser’s Help file. Depending on the browser you are using and the way it may have been customized, the following methods may be used:

| ![](tbi-version-4-2-polytrauma-user-manual/018.png) | Pressing the \< F1 \> key is the traditional way to access online help. In a Web-based application like TBI Registry, \< F1 \> will provide help about how to operate the *browser* itself.                               |
|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tbi-version-4-2-polytrauma-user-manual/019.png) | The help icon in Internet Explorer is typically found somewhere on the light gray browser menu bars at the top of the screen. How your browser is set up will determine whether or not this icon appears on your browser. |
| <u>H</u>elp                                                                                                                | Click the Help menu option on the browser’s menu bar.                                                                                                                                                                     |

### Application Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](tbi-version-4-2-polytrauma-user-manual/020.png) *This feature is not available for Build 1; accordingly, the material in this section has been “grayed out.” When online help is available, this document will be revised. In Build 1, if you see and click on the TBI Registry help icon, you will see only a “placeholder” Web page.*

The Help icon, available on every screen of the application, opens the TBI Registry online help file. In most cases, the help offered will be specific to the topic or screen that you were viewing when you clicked the icon. In some cases, however, a specific help topic may not be available, in which case you will see the table of contents for the help file. From that point, you may browse and search for more specific help. The online help file is contained in a series of Web pages.

![](tbi-version-4-2-polytrauma-user-manual/021.png)Note: Since TBI Registry is not a “desktop” application (that is, it does not reside on your computer desktop), pressing \< F1 \> will not open TBI Registry help. Instead, it will open help for the browser that you are using. <span class="mark"></span>

### Accessibility Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Standard Web browser keyboard shortcuts and application design elements help to make TBI Registry accessible to a wide range of users, including those with limited dexterity, low vision, or other disabilities.

![](tbi-version-4-2-polytrauma-user-manual/022.png) For a complete list of keyboard shortcuts, see Appendix A.

![](tbi-version-4-2-polytrauma-user-manual/023.png) For more information about accessibility features, see Appendix D. <span class="mark"></span>

## Date of Death and Deceased Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some Registry programs perform “deceased checks” of files for each patient in the local registry to validate whether or not the patient is deceased. Although TBI Registry does not perform such a check, it does capture the Date of Death, if that information is entered in the source files. This is particularly true of the files for the polytrauma application. For the referral to be sent to TBI Registry, the patient is screened via the two OEF/OIF clinical reminders in VistA. However unlikely it is that a new referral would be received for a deceased patient there is nothing in the system presently to prevent such a record from being edited.

## Screen Areas and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While there are some differences in screen appearance from one task area to another, the general layout is as shown below; ![](tbi-version-4-2-polytrauma-user-manual/024.png) indicate the parts of the screen. Please take a few moments to familiarize yourself with the various screen areas before you begin.

![](tbi-version-4-2-polytrauma-user-manual/025.png)

<span id="_Toc501011975" class="anchor"></span>Figure 1 - Screen Areas

### Banner Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Across the top of the screen is the BANNER AREA. It displays the VA logo and the registry name.

### Tabs (Common Navigation Area)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TABS immediately below the application title provide a COMMON NAVIGATION AREA that you will see in all registry programs. These elements allow you to select the type of task to be performed. For more information a list of tasks assigned to you (depending on your role) is available in

Table 6 – Tasks by Role

- My Tasks: To see a list of tasks assigned to you.
- Patients: To view and edit patient records.
- Administration: To create user accounts and assign roles. This tab is only visible to people who have administrative credentials.

| ![](tbi-version-4-2-polytrauma-user-manual/026.png) | Note: The left-right order of tabs may be different from that depicted in this document. The final release of TBI Registry will be “patient-centric,” and the <span class="smallcaps">Patient</span> tab will become the primary tab for users. Functionality for tabs other than the <span class="smallcaps">Patient</span> tab will, however, be essentially the same as discussed in this document. |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Breadcrumbs 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Note the so-called <span class="mark">“BREADCRUMBS”</span> below the tabs (showing, in this case, <span class="smallcaps">PATIENTS \> POLYTRAUMA PATIENTS)</span>; this shows you where you are within the application, how you got there, and the current page's logical parent pages in the information hierarchy.

### Left Navigation Bar 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a TAB is selected, the available tasks for that tab are displayed in the <span class="mark">LEFT NAVIGATION BAR</span> at the far left of the screen.

### Content Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <span class="mark">CONTENT AREA</span> contains a number of Web parts, specific to the registry and specific to which common navigation item was selected. Example: In TBI Registry, this screen could show a list of patients. The contents of this area will change depending on which task you have selected. In some cases, the area expands to allow display room for more information, and the <span class="mark">LEFT NAVIGATION BAR</span> temporarily disappears.

## User Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your ability to use various features of TBI Registry will depend upon your assigned role. Some choices will not be available to you if your role does not call for that particular task. You may be assigned more than one role. Roles are assigned by the TBI Administrator. The available roles are described in the following sections.

### TBI Administrator 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a TBI Administer, you have “super-user” access and you can perform the following activities:

- Edit all polytrauma entries
- Access the administration section of the Registry and create, edit, and delete user permissions

### TBI Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a TBI Editor, you can perform the following activities:

- Edit polytrauma referral records that are mapped to VISN/stations assigned to the user for their role.

| ![](tbi-version-4-2-polytrauma-user-manual/027.png) | Note: The TBI Editor role requires VISN/Station mapping for each user assigned to this role. |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|

### TBI Read Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a TBI Read Only user, you can perform the following activities:

- Open polytrauma referrals (in read only mode) that are mapped to VISNs/stations assigned to the user for their role.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-polytrauma-user-manual/028.png)</th>
<th><p><strong>Note:</strong> The TBI Read Only User role requires VISN/Station mapping for each user assigned to this role.</p>
<p>Also, if the user has the same VISN/station mapping in the editor role, the edit access will take precedence.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### TBI Polytrauma Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a TBI Polytrauma Editor, you can perform the following activities:

- Edit polytrauma referral records that are mapped to VISN/stations assigned to the user for their role.

| ![](tbi-version-4-2-polytrauma-user-manual/029.png) | Note: The TBI Polytrauma Editor role requires VISN/Station mapping for each user assigned to this role. |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|

### TBI Polytrauma Read Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a TBI Polytrauma Read Only user, you can perform the following activities:

- Open polytrauma referrals (in read only mode) that are mapped to VISNs/stations assigned to the user for their role.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-polytrauma-user-manual/030.png)</th>
<th><p><strong>Note:</strong> The TBI Polytrauma Read Only User role requires VISN/Station mapping for each user assigned to this role.</p>
<p>Also, if the user has the same VISN/station mapping in the editor role, the edit access will take precedence.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### TBI Reporting User National

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users provided this role can generate reports where all facility information will included in the report results.

### TBI Reporting User VISN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users provided this role can generate reports where only facility information for a specific Veterans Integrated Service Network (VISN) will included in the report results.

### TBI Reporting User Station

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users provided this role can generate reports where facility information for only a station will included in the report results.

### TBI Rehabilitation and Polytrauma Clinicians

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users assigned this role will have the appropriate permissions for running the TBI Instrument reports.

### TBI Technical Support Administrator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users assigned this role will have the appropriate permissions to provide only technical site support.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>TABS</th>
<th><blockquote>
<p>TBI ADMINISTRATOR</p>
</blockquote></th>
<th><blockquote>
<p>TBI EDITOR</p>
</blockquote></th>
<th><blockquote>
<p>TBI READ ONLY USER</p>
</blockquote></th>
<th><blockquote>
<p>TBI POLYTrauma Editor</p>
</blockquote></th>
<th><blockquote>
<p>tbi polytrauma read only user</p>
</blockquote></th>
<th><blockquote>
<p>TBI Reporting User National</p>
</blockquote></th>
<th><blockquote>
<p>TBI Reporting User VISN</p>
</blockquote></th>
<th><blockquote>
<p>TBI Reporting User Station</p>
</blockquote></th>
<th><blockquote>
<p>TBI Rehabilitaion and Polytrauma Clinicians</p>
</blockquote></th>
<th><blockquote>
<p>TBI Technical Support Administrator</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span class="smallcaps">My Tasks</span></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><span class="smallcaps">Patients</span></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><span class="smallcaps">Administration</span></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><span class="smallcaps">Reporting</span></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th>TASKS</th>
<th><blockquote>
<p>TBI ADMINISTRATOR</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TBI EDITOR</p>
</blockquote></th>
<th><blockquote>
<p>TBI READ ONLY USER</p>
</blockquote></th>
<th><blockquote>
<p>TBI POLYTrauma Editor</p>
</blockquote></th>
<th><blockquote>
<p>tbi polytrauma read only user</p>
</blockquote></th>
<th><blockquote>
<p>TBI Reporting User National</p>
</blockquote></th>
<th><blockquote>
<p>TBI Reporting User VISN</p>
</blockquote></th>
<th><blockquote>
<p>TBI Reporting User Station</p>
</blockquote></th>
<th><blockquote>
<p>TBI Rehabilitaion and Polytrauma Clinicians</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TBI Technical Support Administrator</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="12"><strong>Add New</strong></td>
<td></td>
</tr>
<tr class="even">
<td>Polytrauma: Add New</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Polytrauma: View</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Polytrauma: Edit</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="12"><strong>Patient Lookup</strong></td>
<td></td>
</tr>
<tr class="even">
<td>TBI Patients</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Polytrauma Patients</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="12"><strong>Administration (Roles)</strong></td>
<td></td>
</tr>
<tr class="odd">
<td>Users</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Roles Matrix</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="12"><strong>Reporting</strong></td>
<td></td>
</tr>
<tr class="even">
<td>Polytrauma</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Instruments</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="12"><strong>Technical Support (Site Only)</strong></td>
<td></td>
</tr>
<tr class="odd">
<td>N/A</td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# # Software Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Starting the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start TBI Registry, follow these steps:

1.  Make sure that you are logged on to Windows and the VA network using the appropriate identity.
2.  ![](tbi-version-4-2-polytrauma-user-manual/031.png) Open your Web browser. The browser opens the site that you have designated as your home page. *Note:* At this time TBI no longer supports FireFox as a browser.

> ![](tbi-version-4-2-polytrauma-user-manual/032.png)

<span id="_Toc501011976" class="anchor"></span>Figure 2 - Internet Explorer

3.  In the address bar, enter the Web address of the application page, which will be provided to you when you are designated as an authorized user.

## Logging In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many registry-associated programs, including TBI Registry, use Windows authentication provided by [Active Directory (AD)](#Glos_AD). Your user identity is detected at the time of initial login to the VA network, so a separate login or authentication is not required to run TBI Registry. Security messages will advise you if you are not logged in, have insufficient privileges, etc. This means that if you are already logged into your usual domain, the Web page which provides TBI Registry should load automatically without challenge. You should be able to open your Web browser, enter the URL, and see TBI Registry run automatically.

If you are logged in and you see either of the two “challenge” pop-up windows, or have other questions related to AD, please contact your Information Resources Management (IRM) for assistance.

![](tbi-version-4-2-polytrauma-user-manual/033.png)

The authentication of your TBI Registry role(s), and your privileges, takes place behind the scenes. Following successful authentication, you will be re-directed to TBI Registry.

## Default Registry Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your default Registry page opens. For most TBI Registry users, this will be some variant of the <span class="smallcaps">My Tasks</span> screen:

![](tbi-version-4-2-polytrauma-user-manual/034.png)

<span id="_Toc501011977" class="anchor"></span>Figure 3 - My Tasks \> Polytrauma \> Add New

At the top are the VA logo, title, search function, and TABS (My Tasks, Patients, Reporting, and Administration). The tabs shown/available will depend upon your role. The first available task for the My Tasks tab is automatically selected, based on your role. Note that the breadcrumb trail shows where you are: My Tasks \> Referrals \> New.

- My Tasks: Displays any tasks assigned to you.
- Patients: Allows you to search for a patient already in the Registry, view and edit patient records.
- Administration: Permits you to assign users and user roles; view and sort user/role lists; view and edit user records.

# TBI Registry Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Accessing Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To understand how the various tasks associated with TBI Registry are performed, it’s necessary to discuss the TBI Registry tabs. The TBI Registry uses the tabs as task-oriented viewers. Tasks available to you are shown on the left navigation panel, based on the role(s) you have been assigned. Figure 3 shows the tasks available for some roles under the <span class="smallcaps">My Tasks</span> tab.

![](tbi-version-4-2-polytrauma-user-manual/035.png)

<span id="_Toc501011978" class="anchor"></span>Figure 4 - My Tasks and the Left Navigation Panel

On your user screen, you will see all the tasks associated with that tab–– but not all of them may be available to you. Availability depends on your assigned role. Contact your supervisor or the TBI Registry Administrator for questions about your role.

| TAB        | TASK CATEGORY   | ACTIVITY   |
|----------------|---------------------|----------------|
| My Tasks       | Polytrauma          | View/Edit      |
|                |                     | Add New        |
| Patients       | Polytrauma Patients | Lookup Patient |
| Administration | Users               | Search         |
|                |                     | Edit           |
|                |                     | Edit Roles     |
|                |                     | Remove         |
|                | Role Matrix         | Search         |

When you “hover” your mouse pointer over a tab or task that is available to you, a Web address ([URL](#glos_URL)) will appear at the bottom of your browser window, just above the Windows \[Start\] button. If the task is not available, the destination address will not appear, indicating that you do not have access to that task.

![](tbi-version-4-2-polytrauma-user-manual/036.png)

<span id="_Toc501011979" class="anchor"></span>Figure 5 - Destination Address Shows Availability

| ![](tbi-version-4-2-polytrauma-user-manual/037.png) | Note: The URL you see will be different from the one shown in Figure 5 - Destination Address Shows Availability |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|

| ![](tbi-version-4-2-polytrauma-user-manual/038.png) | Important: When you hover near a task item, a highlighting rectangle in lighter blue (similar to the one marking Add New and View/Edit in Figure 6 will appear around the task. To see or to select the link, however, you must click on the task text itself, not just the highlighting rectangle. |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](tbi-version-4-2-polytrauma-user-manual/039.png)</th>
<th><p><strong>Note:</strong> Depending on your browser settings, the task text may or may not show underlining when you hover over it. If the task is not available, or if there is no actual task associated with the text, you will not see a destination displayed, as in Figure 6 – No Task Available</p>
<p>![](tbi-version-4-2-polytrauma-user-manual/040.png)<strong>Note:</strong> The tasks available in the <span class="smallcaps">LEFT NAVIGATION BAR</span> will only include those assigned to your role(s). See Table 6 for tasks available for each role. Also see Table 7 for a listing of all polytrauma tasks.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](tbi-version-4-2-polytrauma-user-manual/041.png)

<span id="_Ref264881117" class="anchor"></span>Figure 6 – No Task Available

![](tbi-version-4-2-polytrauma-user-manual/042.png)Note: The tasks available in the <span class="smallcaps">LEFT NAVIGATION BAR</span> will only include those assigned to your role(s). See Table 6 for tasks available for each role. Also see Table 7 for a listing of all polytrauma tasks.

## Error and Warning Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If required data elements are not entered on a TBI Registry data entry screen, you will see a popup error message like this one:

![](tbi-version-4-2-polytrauma-user-manual/043.png)

<span id="_Toc501011981" class="anchor"></span>Figure 7 - Data Errors Message

If you try to navigate away from a screen without saving or otherwise completing the screen, you will see this popup warning:

![](tbi-version-4-2-polytrauma-user-manual/044.png)

<span id="_Toc501011982" class="anchor"></span>Figure 8 -Navigating Away from Page

## TBI Registry Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TBI Registry consists of the following applications:

| APPLICATION                      | DESCRIPTION                                                                                                       |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Polytrauma Entries               | Provides a Web-based repository of patients identified as having sustained multiple injuries in the OEF/OIF missions. |
| Polytrauma Patient Lookup        | An application that searches the TBI Registry’s data for available information on patients.                           |
| TBI Registry User Administration | Provides information about the TBI Registry’s users and management of the system.                                     |
| TBI Role Administration          | Provides management and control of access to the system through the use of defined user roles.                        |

Depending on your role(s), you’ll have access to certain applications. To select an application click on a tab located immediately below the TBI Registry banner. Once a tab is selected, the available applications for that tab are displayed in the Task Bar at the far left of the screen. You can navigate through an application by observing the “breadcrumbs” located directly underneath the tabs. The breadcrumbs show you the forward path you’ve selected.

![](tbi-version-4-2-polytrauma-user-manual/045.png)

<span id="_Toc501011983" class="anchor"></span>Figure 9 - Navigating through the TBI Registry Applications

| ![](tbi-version-4-2-polytrauma-user-manual/046.png) | You can use the Windows navigation arrows (located at the top left corner of your Windows toolbar) to move back through the Registry screens. |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|

Part C. Using the Polytrauma Entries Application

# Polytrauma Entries Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Polytrauma Entries application allows the case manager to track patients with multiple injuries. These injuries may be multiple traumatic brain injuries or injuries elsewhere on the body that are not traumatic brain injuries. There are no reporting options for this application. It is designed simply to track Veterans with multiple traumas.

## Polytrauma Rehabilitation Center (PRC) Admission and Follow Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To begin, click on the tab “My Tasks” and then on the link “Add New.” Select PRC as the Type of Entry. Select Admission or Follow Up as the Type of Submission. Enter the patient’s Social Security Number (SSN) and the patient’s First Name and Last Name (see Error! Not a valid bookmark self-reference.).

![](tbi-version-4-2-polytrauma-user-manual/047.png)

<span id="_Toc501011984" class="anchor"></span>Figure 10 PRC Admission/Follow-Up 1 of 5

Continue to fill in the following fields: Address Line 1, Address Line 2, City, County, State, Country, Postal Code, Home Phone, E-mail Address, Home Veterans Affairs Medical Center (VAMC), Military Service Branch, Military Duty Status, and Military Discharge Status (see Figure 10).

Continue to fill in the following fields: Military Service Branch, Military Duty Status at Admission, Military Status at Discharge, and Polytrauma VAMC. Additional tracking information includes the Military Treatment Facility (MTF)/ Referral source.

![](tbi-version-4-2-polytrauma-user-manual/048.png)

<span id="_Toc501011985" class="anchor"></span>Figure 11 PRC Admission/Follow-up 2 of 5

Additional tracking information includes including Injury Date, Injury Geographic Location, Blast Injury, Vehicle Injury, Bullet Injury, Physical Assault, Other Injury, and Other Injury Description. These fields have drop-down lists for you to select a value. The Date fields allow you to enter the date in the dd/mm/yyyy format or you can click on the calendar icon and select a date from the calendar that displays (see Figure 11).

Beneath that is another group of check boxes under Injury Details. These include: Brain Injury, Eye Injury/Visual Impairment, Soft Tissue/Orthopedic Injuries, Nerve Injuries, Burns, Amputation, Gastro-Intestinal/Bowel, Cardiovascular Injury, Infection, Fractures, Wounds/Shrapnel, Ear Injury/Hearing, Lung Injuries, Behavioral Health Conditions, Spinal Cord Injury, Internal Organ/Other, Pain, and Other (see Figure 11).

![](tbi-version-4-2-polytrauma-user-manual/049.png)

<span id="_Toc501011986" class="anchor"></span>Figure 12 PRC Admission/Follow Up 3 of 5

In the Treatment section the Detailed Emerging Consciousness Etiology field is a drop-down list of possibilities. Other fields in this section includes: Date of Injury Resulting in Disorder off Consciousness, Date Patient Emerged, JFK Coma Recovery Scale, Genito-Urinary Injuries. Enter values in the Admission FIM Code, the Admission Date, the FRG Code, the Number of Days off unit, the Discharge FIM Code, and the Rehab Discharge Date fields. The Date fields allow you to input the date in the dd/mm/yyyy format or you can click on the calendar icon and select a date from the calendar that displays (see Figure 12).

![](tbi-version-4-2-polytrauma-user-manual/050.png)Note: An FIM Code is a scoring mechanism used to indicate the degree of a Veteran’s injuries. The smaller the score, the worse the injury. FIM codes are established for all the various regions of the body.

![](tbi-version-4-2-polytrauma-user-manual/051.png)

<span id="_Toc501011987" class="anchor"></span>Figure 13 - PRC Admissions/Follow Up 4 of 5

![](tbi-version-4-2-polytrauma-user-manual/052.png)Note: The discharge date can be the current date, if applicable or a date in the past (if the case manager is catching up on the records).

The Discharge To field is a drop down list of possibilities. Make a selection from this field. There is another group of check boxes under Follow Up Clinical Needs. The follow-up Clinical Needs section of the graphical user interface (GUI) requires the case manager to select from the following check boxes:

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

Then the case manager can click the Save button to save the edits or click the Close button to close without saving the changes (see Figure 13).

![](tbi-version-4-2-polytrauma-user-manual/053.png)

<span id="_Toc501011988" class="anchor"></span>Figure 14 PRC Admissions/Follow Up 5 of 5

## Polytrauma Transitional Rehabilitation Program (PTRP) Admission and Follow Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To begin, click on the tab “My Tasks” and then on the link “Add New.” Select PTRP as the Type of Entry. Select Admission or Follow Up as the Type of Submission. Enter the patient’s Social Security Number (SSN) and the patient’s First Name and Last Name (see [Figure 13](#G_X3)).

Continue to fill in the following fields: Address Line 1, Address Line 2, City, County, State, Country, Postal Code, Home Phone, E-mail Address, Home Veterans Affairs Medical Center (VAMC), Military Service Branch, Military Duty Status, and Military Discharge Status, and Polytrauma VAMC (see [Figure 13](#G_X3)).

![](tbi-version-4-2-polytrauma-user-manual/054.png)

<span id="G_X3" class="anchor"></span>Figure 15 Adding a New Patient Admission/Follow-Up to the Polytrauma Transitional Rehabilitation Program (PTRP)

Beneath that is the PTRP section. Select the Program. Continue to fill in the other fields which includes the following: Preinjury Primary Person Living With, Preinjury Residence, Primary Preinjury Employment Status, Secondary Preinjury Employment Status.

Then enter the MPAI for Abilities, Adjustment, Participation, and Total. Make a selection from the radio buttons for MPAI Question 26 Residence and MPAI Question 26 Discharge. Then enter values for Satisfaction with Life (Admissions), Satisfaction with Life (Discharge), and Participation Assessment with Recombined Tools (PART), Primary Person Living with (Discharge), and Residence (Discharge) (see [Figure 14](#G_X4)).

![](tbi-version-4-2-polytrauma-user-manual/055.png)

<span id="G_X4" class="anchor"></span>Figure 16 PTRP and MPAI Questions

# Polytrauma Patient Lookup Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](tbi-version-4-2-polytrauma-user-manual/056.png)To protect the privacy of TBI Registry patients, both actual Social Security Numbers (SSNs) and stand-in (called PseudoSSNs) numbers are used in TBI Registry applications. PseudoSSNs are identified by the use of three zeros for the first three numbers of the nine-digit SSN (for example: 000-03-2857) or the use of the letter “P” (for “Pseudo”) as a suffix of a SSN (for example: 242-59-9250P).

<span id="_Toc501011991" class="anchor"></span>Figure 17 - New Polytrauma Patient Screen

## Polytrauma Patients Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a search of the Registry for polytrauma patients:

1.  Click the Patients tab to open the PATIENTS \> TBI PATIENTS screen.
2.  Navigate to the PATIENTS \> POLYTRAUMA PATIENTS screen by clicking the item, “Polytrauma Patients” located in the Left Navigation Bar (see Figure 18).

> The task, Polytrauma Patients, is highlighted by a light blue box.  

You can initiate a search for a patient by providing either the patient’s Social Security Number (SSN) or PseudSSN or their last name. You can also search for patients by their date of injury or by VISN.

![](tbi-version-4-2-polytrauma-user-manual/057.png)

<span id="_Toc501011992" class="anchor"></span>Figure 18 - Polytrauma Patients Lookup Screen

3.  Place the cursor in the labeled text box and type the patient’s SSN (or PseudoSSN) or last name in the appropriate text box (see Figure 18).

> When entering the SSN or Pseudo SSN of a patient, you can enter numbers in the text box with or without hyphens, for example: 000020003 or 000-02-0003. Both formats are accepted by the application.

4.  Click the Search button located at the bottom of the screen (see Figure 18).

> If the search is successful, you can view the patient’s SSN (or PseudoSSN), first and last name, the Polytrauma Center the patient visited, the injury date, and the admission date in the results panel located at the bottom of the screen (See Figure 19).

> If no information for the SSN (or PseudoSSN) or Patient Last Name is located, the results panel displays the message, “No Records” (see Figure 20).

![](tbi-version-4-2-polytrauma-user-manual/058.png)

<span id="_Ref303326036" class="anchor"></span>Figure 19 - Polytrauma Patients Search Results Screen

![](tbi-version-4-2-polytrauma-user-manual/059.png)

<span id="_Toc501011994" class="anchor"></span>Figure 20 - Polytrauma Results Panel, No Records

> If you are looking for patients who were screened during a certain time span, you can enter a time span in the text boxes labeled Injury Date From (mm/dd/yyyy) and Injury Date To (mm/dd/yyyy).

5.  Type a time span of days, months, or years in the appropriate text boxes.
6.  Click the Search button located at the bottom of the screen.

![](tbi-version-4-2-polytrauma-user-manual/060.png)

<span id="_Toc501011995" class="anchor"></span>Figure 21 - Searching for Patients by Time Span

> If the search locates patient data, you can view this data in the results panel located at the bottom of the screen (see Figure 22).

![](tbi-version-4-2-polytrauma-user-manual/061.png)

<span id="_Toc501011996" class="anchor"></span>Figure 22 - Searching for Patients Over Time Span

> If you enter in a date in the “Screening Date From (mm/dd/yyyy)” text box, but leave the “Screening Date To (mm/dd/yyyy)” text box empty, the application will search for all records from the Screening Date From value to the present day (see Figure 23).

> ![](tbi-version-4-2-polytrauma-user-manual/062.png)

<span id="_Toc501011997" class="anchor"></span>Figure 23 - Searching for Patients from a Set Date to Present

> You can also search for patients by individual VISNs. The VISNs available to you in the drop-down list will depend on your role and access privileges. You can only select one VISN at a time.

7.  Click the arrow located on the right side of the drop-down list to view the VISN list’s choices.
8.  Click a value in the drop-down lists to select it and then click the Search button.

The results panel at the bottom of the screen will display the results of your search.

![](tbi-version-4-2-polytrauma-user-manual/063.png)

<span id="_Toc501011998" class="anchor"></span>Figure 24 - Polytrauma Patient Search by VISN Results

Once you have located a patient using the features of the Patients \> Polytrauma Patients screen and have the results of your search displayed in the Lookup Patient panel, you can view additional information on the patient and edit the patient’s referral by using the following step.

9.  Click the View box located on the extreme left of the results panel to view the Patient ID screen (see Figure 25).

![](tbi-version-4-2-polytrauma-user-manual/064.png)

<span id="_Toc501011999" class="anchor"></span>Figure 25 - Polytrauma Patients Screen Link

If your role allows access to the Polytrauma Edit task, this step will take you to the My Tasks \> Polytrauma \> Edit Tracking Item ID: screen.

Part D. Using the User Administration Application

# User Administration Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Administration Application allows an administrator to view, edit, and sort user roles. The administrator is a global role that is not specific to any facility.

At <span class="smallcaps">Administration \> List Users</span>, a list displays on the GUI. The NT Usernames and names have been removed from the image for security purposes.

![](tbi-version-4-2-polytrauma-user-manual/065.png)

<span id="_Toc268528400" class="anchor"></span>Figure 26 - Administration \> List Users Screen

You can download the list to Excel using the “Download to Excel” button at the bottom of the <span class="smallcaps">List All User/Roles</span> screen.

![](tbi-version-4-2-polytrauma-user-manual/066.png)

<span id="_Toc268528401" class="anchor"></span>Figure 27 – List all User Roles

You can also select Edit User ID to make edits to User IDs. The editable fields are text fields.

![](tbi-version-4-2-polytrauma-user-manual/067.png)

<span id="_Toc268528402" class="anchor"></span>Figure 28 - Edit Users IDs Screen

## Role Administration Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Role Administration Application allows the administrator to select Edit User Roles and then complete fields on the GUI to edit the user’s roles.

First go to <span class="smallcaps">Administration \> Add/Edit Users \> Add New User</span> to add a new user.

![](tbi-version-4-2-polytrauma-user-manual/068.png)

<span id="_Toc501012003" class="anchor"></span>Figure 29 - Add New User Screen

Go to the Edit User Roles Information to edit the user’s roles.

Once a veteran’s information is entered in the Polytrauma Application, those records can be viewed and edited. To do this, go to <span class="smallcaps">My Tasks \> Polytrauma \> View / Edit</span>.

![](tbi-version-4-2-polytrauma-user-manual/069.png)

<span id="_Toc501012004" class="anchor"></span>Figure 30 - Polytrauma View/Edit Users Screen

Roles can be edited using the drop-down lists and check boxes provided. The editable fields in the Roles section of the GUI are:

- TBI Administrator (drop-down list with VISN Access)
- TBI Polytrauma Editor (drop-down list with VISN Access)
- TBI Polytrauma Read Only (drop-down list with VISN Access)

Click Save to save the changes or click Close to close the GUI without saving.

![](tbi-version-4-2-polytrauma-user-manual/070.png)

<span id="_Toc268528405" class="anchor"></span>Figure 31 - Edit Roles Screen

![](tbi-version-4-2-polytrauma-user-manual/071.png)

<span id="_Toc501012006" class="anchor"></span>Figure 32 - Edit Roles Screen (Part 2)

![](tbi-version-4-2-polytrauma-user-manual/072.png)

<span id="_Toc501012007" class="anchor"></span>Figure 33 - Edit Roles Screen (Part 3)

![](tbi-version-4-2-polytrauma-user-manual/073.png)

<span id="_Toc501012008" class="anchor"></span>Figure 34 - Edit Roles Screen (Part 4)

![](tbi-version-4-2-polytrauma-user-manual/074.png)

<span id="_Toc501012009" class="anchor"></span>Figure 35 - Edit Roles Screen (Part 5)

There is also a TBI Read Only option.

![](tbi-version-4-2-polytrauma-user-manual/075.png)

<span id="_Toc501012010" class="anchor"></span>Figure 36 - TBI Edit User Roles (Read Only User Role)

![](tbi-version-4-2-polytrauma-user-manual/076.png)Note: For Read Only access, all the fields are grayed out.

![](tbi-version-4-2-polytrauma-user-manual/077.png)

<span id="_Toc501012011" class="anchor"></span>Figure 37 - Assigning VISN Access Screen

Select the VISN Access and TBI Reporting User Station.

![](tbi-version-4-2-polytrauma-user-manual/078.png)

<span id="_Toc501012012" class="anchor"></span>Figure 38 - TBI Reporting User Station

> Select User Roles from the drop-down list provided.

![](tbi-version-4-2-polytrauma-user-manual/079.png)

<span id="_Toc501012013" class="anchor"></span>Figure 39 - Station Access Screen

Using the task bar to the far left of the screen, the case manager can also use the Role Administration application to list users:

![](tbi-version-4-2-polytrauma-user-manual/080.png)

<span id="_Toc501012014" class="anchor"></span>Figure 40 - Role Administration Screen

There is a search function text box, with Search and Clear buttons to the right of the field.

Add New User:

![](tbi-version-4-2-polytrauma-user-manual/081.png)

<span id="_Toc501012015" class="anchor"></span>Figure 41 - Add New User Screen

List All User/Roles:

![](tbi-version-4-2-polytrauma-user-manual/082.png)

<span id="_Toc501012016" class="anchor"></span>Figure 42 - List All User/Roles Screen

Part E. About the TBI Interface

THIS PAGE LEFT INTENTIONALLY BLANK

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

A checkbox toggles between a YES/NO, ON/OFF setting. It is usually a square box containing a check mark  or X. Clicking the box or pressing the spacebar toggles the checkbox setting. In some instances, check boxes may be used to provide more than one choice; in such cases, more than one box can be selected.

#### Radio Button

A radio button, also known as an option button, is a small, hollow circle adjacent to text. Radio buttons appear in sets. Each button represents a single choice and normally only one button may be selected at any one time. Clicking on the radio button places a solid dot in the circle, selecting the option. Clicking a selected radio button de-selects it, removing the dot. As one radio button is selected, others within the category switch off. For example, Male or Female may be offered as choices through two radio buttons.

#### Command Buttons and Command Icons

A command button initiates an action. It is a rectangular shape with a label that specifies what action will be performed when the button is clicked. A common example is the search key. ![](tbi-version-4-2-polytrauma-user-manual/083.png)

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

Part F. Appendices

# Standard Web Browser Shortcut Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the following table, two or more keys connected by a comma (,) indicate that the keys should be pressed in succession. Keys connected by a plus sign (+) indicate that the keys should be pressed at the same time. These keys can be used while running DSSA in a Web browser.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 0%" />
<col style="width: 31%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">BROWSER OPTION</th>
<th colspan="2">SHORTCUT</th>
<th>IE</th>
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
</tr>
<tr class="even">
<td><blockquote>
<p>Bookmark, new (for current page)</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; D &gt;</p>
</blockquote></td>
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
</tr>
<tr class="odd">
<td><blockquote>
<p>Find [on the page displayed]</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; F &gt;</p>
</blockquote></td>
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
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Location in history, go to next</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; + &lt; &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>&lt; Space &gt;</p>
</blockquote></td>
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
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>&lt; Backspace &gt;</p>
</blockquote></td>
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
</tr>
<tr class="even">
<td><blockquote>
<p>Home page, go to</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; + &lt; Home &gt;</p>
</blockquote></td>
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
</tr>
<tr class="even">
<td><blockquote>
<p>Open location</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; L &gt;</p>
</blockquote></td>
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
</tr>
<tr class="even">
<td><blockquote>
<p>Select All [on the page displayed]</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; A &gt;</p>
</blockquote></td>
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
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;M&gt;</p>
</blockquote></td>
<td><blockquote>
<p>(move)</p>
</blockquote></td>
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
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;N&gt;</p>
</blockquote></td>
<td><blockquote>
<p>(minimize)</p>
</blockquote></td>
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
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;C&gt;</p>
</blockquote></td>
<td><blockquote>
<p>(close)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

# VA Approved Internet Browsers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following VA-approved browsers have been tested for use with DSSA and are believed to be fully functional. If you encounter unusual problems, please submit a Remedy report and/or consult with your local IRM.

| BROWSER                       | VERSION(S) | REMARKS                          |
|-------------------------------|------------|----------------------------------|
| Microsoft® Internet Explorer® | 6.x, 7.x   | Does not support tabbed browsing |

# Web-based Application Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Web Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In a Web-based application, a “page” is the specific area on your computer screen used by a program. You might start on a launch page, for example, and use the menus available to you to move to another, more specific task-oriented page. If you have more than one browser window running at the same time, you can go from one window to another by clicking in each of those windows or by using [\< Alt \>+\< Tab \>](#Glos_AltTab). You can also move, close, or minimize the application window to make room for another window (see Changing (Resizing) a Browser Window for further instructions on these functions).

# Pop-up Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These are windows that pop up within (or on top of) a window to provide or request information. They require a response before they will close. Clicking buttons with the words \[OK\], \[Cancel\], \[Exit\], or by pressing the \< Esc \> key closes these windows.

# Web-based Application (WBA) Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe typical WBA elements.

# Text Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The appearance of the text boxes change from a plain line border (SAMPLE 1) to an almost three-dimensional, pale yellow-highlighted field when you tab to it or click in it (SAMPLE 2).

![](tbi-version-4-2-polytrauma-user-manual/084.png)

<span id="_Toc501012017" class="anchor"></span>Figure 43 - Text Box Sample 1

![](tbi-version-4-2-polytrauma-user-manual/085.png)

<span id="_Toc501012018" class="anchor"></span>Figure 44 - Text Box Sample 2

Type your entry into the text box. The entry will not be saved until you tab away from or otherwise exit from the text box. In cases where the format of your entry is important, a sample will appear near the box. The relative width of these boxes is usually a reflection of the number of characters you are allowed to enter. Sometimes (as with date fields) there may also be a “date picker” next to the field.

You should see a “tool tip” pop up when you hover your mouse pointer over the text box.

![](tbi-version-4-2-polytrauma-user-manual/086.png)

<span id="_Toc501012019" class="anchor"></span>Figure 45 - Tool Tip for Text Box

SAMPLE: ![](tbi-version-4-2-polytrauma-user-manual/087.png)

A checkbox “toggles” (changes) between a YES / NO, ON / OFF setting. It is typically a square box which can contain a check mark ![](tbi-version-4-2-polytrauma-user-manual/088.png) or an “X” ☒ and is usually accompanied by text. Clicking the box or tabbing to the field and pressing the spacebar toggles the checkbox setting. In some instances, check boxes may be used to provide more than one choice; in such cases, more than one box can be selected. Sometimes, a pre-determined “default” entry will be made for you in a checkbox; you can change the default if needed.

# Radio Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAMPLE: ![](tbi-version-4-2-polytrauma-user-manual/089.png)

A radio button, also known as an option button, is a small, hollow circle adjacent to text. Radio buttons usually appear in sets, with each button representing a single choice; normally, only one button in the set may be selected at any one time. Clicking on the radio button places a solid dot in the circle, selecting the option. Clicking a selected radio button de-selects it, removing the dot. As one radio button is selected, others within the category switch off. For example, Male or Female may be offered as choices through two radio buttons, but you can only select one of the choices.

# Command Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Command Buttons</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>![](tbi-version-4-2-polytrauma-user-manual/090.png)</p>
<p>![](tbi-version-4-2-polytrauma-user-manual/091.png)</p></td>
<td><p>A command button initiates an action. It is a rectangular “3-dimensional” shape with a label that specifies what action will be performed when the button is clicked. Common examples are shown at left. Command buttons that end with three dots indicate that selecting the command may evoke a subsidiary window.</p>
<p>In the text of this document, command button names appear inside square brackets. <em>Examples:</em> [Search], [Save].</p></td>
</tr>
<tr class="even">
<td>![](tbi-version-4-2-polytrauma-user-manual/092.png)</td>
<td>The [Cancel] command allows you to cancel the action about to be taken, or to discard changes made on a form. For example, when closing an application, you may be prompted to validate the action to close. If you click the [Cancel] button, the application will not close and you will resume from the point at which the close action was initiated. Or, on a data screen, you may use the [Cancel] button to discard any changes you may have made to the data and close the tab.</td>
</tr>
<tr class="odd">
<td>![](tbi-version-4-2-polytrauma-user-manual/093.png)</td>
<td>The [Select] command is used to select records for editing.</td>
</tr>
<tr class="even">
<td>![](tbi-version-4-2-polytrauma-user-manual/094.png)</td>
<td>The [Search] command is used to find one or more records. When at least one character is typed in a lookup dialog box, clicking the [Search] button will bring up matching entries. In many cases, leaving the lookup box blank will find all such records. Enter the search string and click [Search]<strong>.</strong> Searches are case-insensitive and use “contains” logic.</td>
</tr>
<tr class="odd">
<td>![](tbi-version-4-2-polytrauma-user-manual/095.png)</td>
<td>The [OK] command is used to accept a default choice, or to agree with performing an action.</td>
</tr>
<tr class="even">
<td><p>![](tbi-version-4-2-polytrauma-user-manual/096.png)</p>
<p>![](tbi-version-4-2-polytrauma-user-manual/097.png)</p></td>
<td>Other command buttons may be unique to a specific screen. For example, the [Clear Triage] button is used when editing a Referral record and you wish to “clear” (or undo) the triage decision just made. These buttons are described under the discussion of the individual screen(s) to which they apply.</td>
</tr>
</tbody>
</table>

# Date Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAMPLE: ![](tbi-version-4-2-polytrauma-user-manual/098.png)

Date fields are identified by their labels, but otherwise look like an ordinary text field. They may have an associated popup calendar. The month and day components of the date may consist of one or two digits and the year must consist of four digits (*e.g.*, 07/27/2007). You may use either slashes (/) or dashes (-) to separate the month, day and year. The selected entry will not be effective until you tab away from or otherwise exit the date field; at that point, the year will be reformatted, if necessary, to four digits; likewise, if you use dashes as separators, they will be converted to slashes.

# Drop-down List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A drop-down list (sometimes called a “pull-down” list) is displayed as a box with an arrow button on the right side (SAMPLE 1). Such a list allows you to select one item from the list. The current choice (or a prompt) is visible in a small rectangle; when you click on the arrow, a list of items is revealed (SAMPLE 2). Click on one of the entries to make it your choice; the list disappears.

![](tbi-version-4-2-polytrauma-user-manual/099.png)

<span id="_Toc501012020" class="anchor"></span>Figure 46 - Dropdown Sample 1

![Figure 42 - Dropdown Sample 2](tbi-version-4-2-polytrauma-user-manual/100.png)

*Figure 42 - Dropdown Sample 2*

A drop-down list (sometimes called a “pull-down” list) is displayed as a box with an arrow button on the right side (SAMPLE 1). Such a list allows you to select one item from the list. The current choice (or a prompt) is visible in a small rectangle; when you click on the arrow, a list of items is revealed (SAMPLE 2). Click on one of the entries to make it your choice; the list disappears.

To select multiple items from a drop-down list, first pick one item or a value from the drop-down list and click the \[Add\] button. To add an additional item from the drop-down list, choose that item from the drop-down and again click \[Add\].

![](tbi-version-4-2-polytrauma-user-manual/101.png)

# List Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAMPLE: ![](tbi-version-4-2-polytrauma-user-manual/102.png)

The list box shows a list of items. If more items exist than can be seen in the box, a scroll bar appears on the side of the box. Click the desired entry to select it from the list.

# Faded (“Grayed Out”) Choices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a web-based application, DSSA does not use grayed-out choices. If a choice is unavailable, it will simply not appear on screen or (if it is a link) will not respond to clicking.

# Keyboard Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](tbi-version-4-2-polytrauma-user-manual/103.png) | Keyboard keys and onscreen buttons are shown in different style brackets throughout this manual to differentiate them from on-screen buttons or menu options: \< Ctrl \> and \< Enter \> are on the keyboard, \[Close\] is a command button on the screen. |
|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](tbi-version-4-2-polytrauma-user-manual/104.png) See [Appendix B](#AppendixB) for a complete listing of keyboard shortcuts.

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
<p>![](tbi-version-4-2-polytrauma-user-manual/105.png)</p></th>
<th><p>![](tbi-version-4-2-polytrauma-user-manual/106.png)</p>
<p><span id="_Toc501012021" class="anchor"></span>Figure 47 – Read Only Data Fields</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Generally speaking, the read-only data thus shown is pre-populated by data feeds from various sources.

# Tab Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the \< Tab \> key or the mouse to move between fields. Do *not* use the \< Enter \> or \< Return \> key, which is usually reserved for the default command button or action.

| ![](tbi-version-4-2-polytrauma-user-manual/107.png) | Tip: In most cases, you may move “backward” to a previous field by holding down the \< Shift \> key and pressing \< Tab \>. |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|

# Changing (Resizing) a Browser Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Windows and columns displayed within DSSA cannot be resized, although the size of the browser window can be changed. To change the size of a browser window, position the mouse pointer over the right edge of the column or the outside edge of the window, left click, and while holding the mouse button down, move the mouse and “drag” to change the size of the window or column. Position the mouse pointer over one corner and drag diagonally to increase the size of the entire window.

![](tbi-version-4-2-polytrauma-user-manual/108.png)Note: Also see Resizing the Browser Screen for tips on how to maximize or minimize browser windows using the keyboard.

# Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SAMPLE: ![](tbi-version-4-2-polytrauma-user-manual/109.png)

Provides generalized help on the application, or specialized help for the area in which you are currently working. See Online Help for more information.

# Command Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OK

SAMPLE: ![](tbi-version-4-2-polytrauma-user-manual/110.png)

Confirms the input and initiates the action defined by the window. Also indicates that you agree with the default choice shown in the window.

Save

SAMPLE: ![](tbi-version-4-2-polytrauma-user-manual/111.png)

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

# Using the \< Ctrl \>, \< Alt \> and \< Esc \> Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some of the current features of the TBI navigation may not be intuitive if you are using assistive technology (for example, a screen reader like [JAWS](#Glos_JAWS)). Remember that the following statements apply to the browser, not to TBI.

In many situations, pressing \< Ctrl \> + a letter that represents the function will perform a function (for example, \< Ctrl \>+\< P \> activates the browser <u>P</u>rint menu).

\< Alt \>+\< F4 \> closes the browser (and also closes DSSA).

\< Esc \> often may be used to close dialog boxes and pop-ups.

# Resizing the Browser Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instead of clicking the browser’s Maximize ![](tbi-version-4-2-polytrauma-user-manual/112.png) button, you can press \< Alt \>+\< space \> and then select Ma<u>x</u>imize by pressing \< x \>. If you wish to minimize the screen, you may press \< Alt \>+\< space \> and then select Mi<u>n</u>imize by pressing \< n \>.

![](tbi-version-4-2-polytrauma-user-manual/113.png)

<span id="_Toc501012022" class="anchor"></span>Figure 48 - Resizing the Browser Screen

You can also resize your browser window to match the resolution of your monitor. For example, to resize the window to 1024 x 768 pixels, enter the following into the browser address box and press \< Enter \>: javascript:window.resizeTo(1024,768); (yes, include the semicolon at the end).

<http://www.petefreitag.com/item/633.cfm>

# Windows Accessibility Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Windows® operating system offers a number of accessibility shortcuts which can be useful. These are “toggled” options, meaning that you perform the specified action once to turn the option on and then again to turn it off.

| ![](tbi-version-4-2-polytrauma-user-manual/114.png) | Warning: Using some of these options will dramatically change the way your computer keyboard functions. If all else fails, reboot your computer to clear any such selections. |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Each option will produce a popup confirmation window like those pictured below. Each of these confirmation pop-ups has the same three choice buttons, in this order left to right: \[OK\], \[Cancel\], and \[Settings\]. \[OK\] is always the default choice.

# StickyKeys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

StickyKeys lets you use the \< Shift \>, \< Ctrl \> or \< Alt \> keys by pressing one key at a time, rather than having to press these keys in conjunction with another key.

Press \< Shift \> five times to toggle StickyKeys on and off:

![](tbi-version-4-2-polytrauma-user-manual/115.png)

<span id="_Toc501012023" class="anchor"></span>Figure 49 - Turning on StickyKeys

# FilterKeys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FilterKeys causes Windows to ignore brief or repeated keystrokes and slows down the keyboard repeat rate.

Press down and hold the right-hand \< Shift \> key for eight seconds to toggle FilterKeys on and off:

![](tbi-version-4-2-polytrauma-user-manual/116.png)

<span id="_Toc501012024" class="anchor"></span>Figure 50 - Turning on FilterKeys

# ToggleKeys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ToggleKeys causes a tone to sound when you press the \< Caps Lock \>, \< Num Lock \>, or \< Scroll Lock \> keys.

Press down and hold the \< Num Lock \> key for five seconds to turn ToggleKeys on and off:

![](tbi-version-4-2-polytrauma-user-manual/117.png)

<span id="_Toc501012025" class="anchor"></span>Figure 51 - Turning on ToggleKeys

# MouseKeys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MouseKeys lets you control the mouse pointer by using the numeric keypad on your keyboard.

Press the left-hand \< Alt \> key plus the left-hand \< Shift \> key plus the \< Num Lock \> key to toggle MouseKeys on and off:

![](tbi-version-4-2-polytrauma-user-manual/118.png)

<span id="_Toc501012026" class="anchor"></span>Figure 52 - Turning on MouseKeys

# HighContrast

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HighContrast improves readability for people with visual impairments by applying a special system color scheme and font size.

Press the left-hand \< Shift \> key plus the left-hand \< Alt \> key plus the \< Print Screen \> key to toggle HighContrast on and off:

![](tbi-version-4-2-polytrauma-user-manual/119.png)

<span id="_Toc253397868" class="anchor"></span>Figure 53 - Turning on HighContrast

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
<td colspan="3"><span id="Glos_AltTab" class="anchor"></span>&lt; Alt &gt;+&lt; Tab &gt;</td>
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
<p>Microsoft® Internet Explorer® is an example for browsers for the World-Wide Web. They act as clients to remote web servers.</p></td>
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
<td colspan="2">context-sensitive help</td>
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
<td colspan="2">Function key</td>
<td colspan="3">A key on a computer or terminal keyboard which can be programmed so as to cause an operating system command interpreter or application program to perform certain actions. On some keyboards/computers, function keys may have default actions, accessible on power-on. For example, &lt;F1&gt; is traditionally the function key used to activate a help system.</td>
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
<td colspan="2">MTFs</td>
<td colspan="3"><em>Acronym for</em> Medical Treatment Facilities</td>
</tr>
<tr class="odd">
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
| Term or Acronym                                                                     |                      |                                                                                                                                                                                                                                                                                                                                                                        | Description |
|-------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| <span id="G_P" class="anchor"></span>P                                          |                      |                                                                                                                                                                                                                                                                                                                                                                        |             |
| <span id="Glos_PCS" class="anchor"></span>Patient Care Services (PCS), Office of    |                      | OPCS oversees VHA's clinical programs that support and improve Veterans' health care. The VA's broad approach to Veteran care incorporates expert knowledge, clinical practice and patient care guidelines in all aspects of care.                                                                                                                                     |             |
| PCS                                                                                 |                      | *See* [Patient Care Services](#Glos_PCS)                                                                                                                                                                                                                                                                                                                               |             |
| <span id="Glos_PII" class="anchor"></span>Personally Identifiable Information (PII) |                      | PII refers to information that can be used to uniquely identify, contact, or locate a single person or can be used with other sources to uniquely identify a single individual.                                                                                                                                                                                        |             |
| PII                                                                                 |                      | *See* [Personally Identifiable Information](#Glos_PII)                                                                                                                                                                                                                                                                                                                 |             |
| Protocol                                                                            |                      | A protocol is a convention or standard that controls or enables the connection, communication, and data transfer between two computing endpoints. In its simplest form, a protocol can be defined as the rules governing the syntax, semantics, and synchronization of communication. Protocols may be implemented by hardware, software, or a combination of the two. |             |
| Provider                                                                            |                      | An organization or individual who delivers health care in a professional, systematic way to any individual in need of health care services. For purposes of the TBI, Providers will be considered as individual health care practitioners.                                                                                                                             |             |
| [ BACK ](#glossary)                                                             | to Glossary Contents |                                                                                                                                                                                                                                                                                                                                                                        |             |
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
<td colspan="2">screen reader</td>
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
<td colspan="2">SQL</td>
<td colspan="3"><em>See</em> <a href="#Glos_SQL">Structured Query Language</a></td>
</tr>
<tr class="even">
<td colspan="2">SQL Server</td>
<td colspan="3"><em>See</em> <a href="#Glos_SQLServer">Structured Query Language Server</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SSIS" class="anchor"></span>SQL Server Integration Services (SSIS)</td>
<td colspan="3"><p>SSIS is a component of the Microsoft <a href="#Glos_SQL">SQL Server</a> database software which can be used to perform a broad range of data migration tasks.</p>
<p>SSIS is a platform for data integration and workflow applications. It features a data warehousing tool used for data <a href="#Glos_ETL">extraction, transformation, and loading (ETL)</a>. The tool may also be used to automate maintenance of SQL Server databases and updates to extremely complex data.</p></td>
</tr>
<tr class="even">
<td colspan="2">SSIS</td>
<td colspan="3"><em>See</em> <a href="#Glos_SSIS">SQL Server Integration Services</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SGML" class="anchor"></span>Standardized Generic Markup Language (SGML)</td>
<td colspan="3">A generic markup language for representing documents. SGML is an International Standard that describes the relationship between a document’s content and its structure. SGML allows document-based information to be shared and re-used across applications and computer platforms in an open, vendor-neutral format.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SQL" class="anchor"></span>Structured Query Language (SQL)</td>
<td colspan="3"><p>An industry-standard language for creating, updating and, querying relational database management systems. SQL was originally based upon relational algebra. Its scope includes data query and update, schema creation and modification, and data access control. The data displayed in TBI is stored in SQL databases.</p>
<p>Typically, the acronym SQL (<em>pronounced</em> “sequel”) is used instead of the actual phrase.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SQLServer" class="anchor"></span>Structured Query Language Server (SQL Server)</td>
<td colspan="3">A relational database management system (RDBMS) which is part of the Microsoft® BackOffice® family of servers. SQL Server was designed for client/server use and is accessed by applications using SQL. It runs on Windows NT version 3.5 or higher and is compliant with the ANSI SQL-92 and FIPS 127-2 SQL standards.</td>
</tr>
<tr class="even">
<td colspan="2">Surveillance</td>
<td colspan="3">Systematic collection, analysis, and interpretation of health data about a disease or condition.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SEER" class="anchor"></span>Surveillance, Epidemiology and End Results (SEER)</td>
<td colspan="3">A program of the National Cancer Institute, SEER is a source of information on cancer incidence and survival in the United States.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SNOMED" class="anchor"></span>Systematized Nomenclature of Medicine (SNOMED)</td>
<td colspan="3">SNOMED is a terminology that originated as the systematized nomenclature of pathology (SNOP) in the early 1960s under the guidance of the College of American Pathologists. In the late 1970s, the concept was expanded to include most medical domains and renamed SNOMED. The core content includes text files such as the concepts, Descriptions, relationships, ICD-9 mappings, and history tables. SNOMED represents a terminological resource that can be implemented in software applications to represent clinically relevant information comprehensive (&gt;350,000 concepts) multi-disciplinary coverage but discipline neutral structured to support data entry, retrieval, maps, etc.</td>
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
<td colspan="2"><span id="Glos_VSSC" class="anchor"></span>VHA Support Service Center (VSSC)</td>
<td colspan="3">The VHA Support Service Center (VSSC) was established in 1996 as an information and technical support arm for VHA healthcare operations. The VSSC delivers information, tools and technical and analytical services to support the management of field operations. The VSSC reports to the ADUSH/OM and is governed by an Advisory Board that sets organizational goals and priorities. The VSSC is structured as a decentralized, virtual organization that is customer driven and outcome oriented. The VSSC organization includes Network Services (Capital Assets, Planning and Data Analysis and Veteran Service and Advocacy), Information Management and Analysis.</td>
</tr>
<tr class="even">
<td colspan="2">VISN</td>
<td colspan="3"><em>See</em> <a href="#Glos_VISN">Veterans Integrated Service Network</a></td>
</tr>
<tr class="odd">
<td colspan="2">VistA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VistA">Veterans Health Information Systems and Technology Architecture</a></td>
</tr>
<tr class="even">
<td colspan="2">VRAD</td>
<td colspan="3">VA/DOD Reporting and Analysis Data Mart</td>
</tr>
<tr class="odd">
<td colspan="2">VSSC</td>
<td colspan="3"><em>See</em> <a href="#Glos_VSSC">VHA Support Service Center</a></td>
</tr>
<tr class="even">
<td colspan="2">VTA</td>
<td colspan="3">Veteran Tracking Application</td>
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
| Term or Acronym         |                      |                                                | Description |
|-------------------------|----------------------|------------------------------------------------|-------------|
| X                   |                      |                                                |             |
| XML                     |                      | *See* [Extensible Mark-up Language](#Glos_XML) |             |
| [ BACK ](#glossary) | to Glossary Contents |                                                |             |
