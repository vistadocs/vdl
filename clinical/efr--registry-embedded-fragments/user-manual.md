---
title: Embedded Fragments Version 1 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: EFR
app_name: "Registry: Embedded Fragments"
section: CLI
app_status: active
pkg_ns: EFR
patch_ver: 1
patch_id: EFR*1
group_key: "EFR:EFR:1"
file_numbers: []
security_keys: []
menu_options: 10
description: The [VHA](#Glos_VHA) is charged with supporting the Presidential Task Force on Returning Global War on Terror Heroes. The Task Force has stated in the Global War on Terror (GWOT) report (recommendation P-7)[^1] that the [VA](#Glos_VA) shall “create an ‘Embedded Fragment’ Surveillance Center and Regi
audience: 
keywords: 
  - class
  - span
  - colspan
  - table
  - fragments
  - embedded
  - manual
  - version
  - glos
  - contents
page_count: 0
word_count: 48139
section_count: 68
table_count: 131
figure_count: 0
appendix_count: 5
has_toc: False
is_stub: False
pub_date: August 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg_Embedded Fragments_(EFR)/efr_incr5_um_062212_v1_1.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg_Embedded Fragments_(EFR)/efr_incr5_um_062212_v1_1.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=223"
---

EMBEDDED FRAGMENT REGISTRY (EFR)Version 4.1

| ![](embedded-fragments-version-1-user-manual/001.png) |
|------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc327881631" class="anchor"></span>Table 1 – Typographical Conventions

User Manual

August 2013

Revision History

| Ver | Description                                                                                                                          | Authors & Role\*                   | Review |          | Issue Date |
|-----|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|--------|----------|------------|
|     |                                                                                                                                      |                                    | By     | Type\*\* |            |
| 1.0 | DRAFT FOR Version 1.0 documentation release                                                                                          | <span class="mark">REDACTED</span> |        |          | 09/29/2010 |
| 2.0 | Updated for Increment 3. Added Data Export section. Updated Lab Orders and Lab Results to include Biological Monitoring screen shots | <span class="mark">REDACTED</span> |        |          | 05/25/2011 |
| 3.0 | Updated for Increment 4.                                                                                                             | <span class="mark">REDACTED</span> |        |          | 12/27/2011 |
| 4.0 | Updated for Increment 5.                                                                                                             | <span class="mark">REDACTED</span> |        |          | 06/19/2012 |
| 4.1 | Update Figure 120 for Sprint 5 Work Item \#20744 – Patient/Provider Letter comments before signature                                 | <span class="mark">REDACTED</span> |        |          | 08/02/2013 |

<span id="_Toc327881632" class="anchor"></span>Table 2 – Graphical Conventions

<span class="mark">REDACTED</span>  

Table of Contents

List of Figures

List of Tables

1.  <span id="_Toc327881323" class="anchor"></span>Introduction

# Orientation


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Orientation](#orientation)
  - [Typographical Conventions Used in the Manual](#typographical-conventions-used-in-the-manual)
  - [Command buttons and Command icons](#command-buttons-and-command-icons)
  - [The Embedded Fragment Registry Application](#the-embedded-fragment-registry-application)
  - [Purpose of the Manual](#purpose-of-the-manual)
  - [Recommended Users](#recommended-users)
  - [Hardware Recommendations](#hardware-recommendations)
- [Background](#background)
  - [Project Scope and Objectives](#project-scope-and-objectives)
  - [The Embedded Fragment Registry Process](#the-embedded-fragment-registry-process)
    - [Overview](#overview)
    - [Data Receipt and Processing](#data-receipt-and-processing)
  - [Release History](#release-history)
    - [EFR Release 1.0](#efr-release-10)
    - [EFR Release 4.0](#efr-release-40)
    - [EFR Release 5.0](#efr-release-50)
  - [Obtaining Software and Documentation](#obtaining-software-and-documentation)
  - [Documentation on the Intranet](#documentation-on-the-intranet)
- [Software Overview](#software-overview)
  - [Web-Based Application Elements](#web-based-application-elements)
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
- [Software Details](#software-details)
  - [Starting the Application](#starting-the-application)
  - [Logging In](#logging-in)
  - [Default Registry Screen](#default-registry-screen)
- [Patients tab](#patients-tab)
  - [Patient Not Found](#patient-not-found)
  - [Patient Search Results](#patient-search-results)
    - [Patient Information](#patient-information)
    - [Workflow Information](#workflow-information)
    - [Related Diagnoses](#related-diagnoses)
    - [Lab Tests of Interest](#lab-tests-of-interest)
  - [Manual Referral](#manual-referral)
    - [Create Referral](#create-referral)
- [My Tasks tab](#my-tasks-tab)
  - [My Tasks Queue](#my-tasks-queue)
  - [Error and Warning Messages](#error-and-warning-messages)
  - [Task Categories and Tasks](#task-categories-and-tasks)
  - [Follow-Up Event Reminders](#follow-up-event-reminders)
  - [Reviewing/Editing a Referral Record](#reviewingediting-a-referral-record)
- [Reporting tab](#reporting-tab)
    - [Lists and Reports Controls](#lists-and-reports-controls)
  - [Referral report](#referral-report)
    - [Number of Referrals Received by VA Facility](#number-of-referrals-received-by-va-facility)
    - [Number of Referrals by Risk Category](#number-of-referrals-by-risk-category)
    - [Referrals by Status and Average Number of Days between Referral and Triage](#referrals-by-status-and-average-number-of-days-between-referral-and-triage)
  - [Data Export](#data-export)
- [Administration tab](#administration-tab)
- [EFR Processes](#efr-processes)
  - [The Triage Process](#the-triage-process)
  - [Screens and Navigation Hierarchy](#screens-and-navigation-hierarchy)
- [My Tasks \> Referrals](#my-tasks-referrals)
  - [My Tasks \> Referrals \> New](#my-tasks-referrals-new)
    - [Sorting the List](#sorting-the-list)
    - [Filtering by Last Name](#filtering-by-last-name)
    - [My Tasks \> Referrals \> New \> Ref \# NNNN](#my-tasks-referrals-new-ref-nnnn)
  - [My Tasks \> Referrals \> \[Accepted\] Open Referrals](#my-tasks-referrals-accepted-open-referrals)
  - [My Tasks \> Referrals \> \[Accepted\] Closed Referrals](#my-tasks-referrals-accepted-closed-referrals)
  - [My Tasks \> Referrals \> \[Accepted\] Follow Ups](#my-tasks-referrals-accepted-follow-ups)
  - [My Tasks \> Referrals \> Ineligible](#my-tasks-referrals-ineligible)
- [# Workflow Processes](#workflow-processes)
  - [Specimen Processes](#specimen-processes)
  - [The Biomonitoring Process](#the-biomonitoring-process)
  - [The Fragment Analysis Process](#the-fragment-analysis-process)
- [My Tasks \> Lab Kits](#my-tasks-lab-kits)
  - [My Tasks \> Lab Kits \> New](#my-tasks-lab-kits-new)
    - [Lab Kits Required Report (Kit Orders Report)](#lab-kits-required-report-kit-orders-report)
    - [View or Edit a New Lab Kit Record](#view-or-edit-a-new-lab-kit-record)
  - [My Tasks \> Lab Kits \> Tracking](#my-tasks-lab-kits-tracking)
    - [Lab Kits \> Tracking Queue](#lab-kits-tracking-queue)
    - [View or Edit a Tracking Lab Kit Record](#view-or-edit-a-tracking-lab-kit-record)
  - [My Tasks \> Lab Kits \> Received](#my-tasks-lab-kits-received)
    - [Lab Kits Received Queue](#lab-kits-received-queue)
    - [View or Edit a Received Lab Kit Record](#view-or-edit-a-received-lab-kit-record)
  - [My Tasks \> Lab Kits \> Voided](#my-tasks-lab-kits-voided)
    - [Voided Lab Kits Queue](#voided-lab-kits-queue)
    - [View a Voided Record](#view-a-voided-record)
- [My Tasks \> Questionnaires/Forms](#my-tasks-questionnairesforms)
  - [My Tasks \> Questionnaires/Forms \> New](#my-tasks-questionnairesforms-new)
    - [Fragment Questionnaire](#fragment-questionnaire)
    - [The Biomonitoring Questionnaire](#the-biomonitoring-questionnaire)
  - [My Tasks \> Questionnaires/Forms \> In Process](#my-tasks-questionnairesforms-in-process)
  - [My Tasks \> Questionnaires/Forms \> Completed](#my-tasks-questionnairesforms-completed)
- [# My Tasks \> Lab Orders](#my-tasks-lab-orders)
  - [Lab Orders \> New](#lab-orders-new)
    - [New Fragment Analysis Lab Orders](#new-fragment-analysis-lab-orders)
    - [New Biological Monitoring Lab Orders](#new-biological-monitoring-lab-orders)
  - [Lab Orders \> Awaiting Results](#lab-orders-awaiting-results)
    - [Filtering Lab Results](#filtering-lab-results)
  - [Lab Orders \> Voided](#lab-orders-voided)
  - [Lab Orders \> Closed](#lab-orders-closed)
    - [Closed Fragment Analysis Orders](#closed-fragment-analysis-orders)
    - [Closed Biological Monitoring Orders](#closed-biological-monitoring-orders)
- [My Tasks \> Lab Results](#my-tasks-lab-results)
  - [Lab Results \> New](#lab-results-new)
    - [New Fragment Analysis Lab Results](#new-fragment-analysis-lab-results)
    - [New Lab Results Biological Monitoring](#new-lab-results-biological-monitoring)
  - [Lab Results \> In Process](#lab-results-in-process)
  - [Lab Results \> Accepted](#lab-results-accepted)
  - [Lab Results \> Voided](#lab-results-voided)
- [My Tasks \> Interpretation & Follow Up](#my-tasks-interpretation-follow-up)
  - [My Tasks \> Interpretation & Follow Up \> New](#my-tasks-interpretation-follow-up-new)
    - [My Tasks \> Interpretation & Follow Up \> New \> Workflow ID \[Biomonitoring\]](#my-tasks-interpretation-follow-up-new-workflow-id-biomonitoring)
    - [My Tasks \> Interpretation & Follow Up \> New \> Workflow ID \[Fragment Analysis\]](#my-tasks-interpretation-follow-up-new-workflow-id-fragment-analysis)
  - [Interpretation & Follow Up \> In Process](#interpretation-follow-up-in-process)
  - [Interpretation & Follow Up \> Interpreted](#interpretation-follow-up-interpreted)
    - [Printing an Interpretation Letter](#printing-an-interpretation-letter)
    - [Batch Printing](#batch-printing)
  - [My Tasks \> Contact Logs](#my-tasks-contact-logs)
  - [Contact Logs](#contact-logs)
    - [All Contacts](#all-contacts)
    - [Creating or Editing a Contact Log](#creating-or-editing-a-contact-log)
- [Patients tab](#patients-tab-1)
  - [Patient Search Results](#patient-search-results-1)
  - [Patient Data Display](#patient-data-display)
  - [Patient Not Found](#patient-not-found-1)
- [Administration tab](#administration-tab-1)
  - [Administration \> Users](#administration-users)
    - [Administration \> Edit User](#administration-edit-user)
    - [Administration \> Edit User Roles](#administration-edit-user-roles)
    - [Administration \> Users \> Remove User](#administration-users-remove-user)
    - [Administration \> Users \> Add New User](#administration-users-add-new-user)
  - [Administration \> Role Matrix](#administration-role-matrix)
  - [Administration \> Reference Ranges](#administration-reference-ranges)
    - [Editing a Reference Range](#editing-a-reference-range)
  - [Administration \> Auto Triage](#administration-auto-triage)
  - [Administration \> DoD Fragment Data](#administration-dod-fragment-data)

## Typographical Conventions Used in the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, fonts and other conventions are used as shown in the following tables:

<table>
<caption><p><span id="_Ref266257896" class="anchor"></span>Table 3 – VA-Approved Internet Browsers</p></caption>
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
<td>Hyperlink to another document or <a href="#glos_URL">Uniform Resource Locator (URL)</a></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Green text, dotted underlining</td>
<td>Hyperlink within this document</td>
<td>See 1.5 below for details.</td>
</tr>
<tr class="odd">
<td>Courier New</td>
<td>Computer dialog, “DOS” filenames</td>
<td>XYZ.doc</td>
</tr>
<tr class="even">
<td>Franklin Gothic Demi</td>
<td><p>Keyboard keys</p>
<p>Web application tab</p>
<p>Button names</p></td>
<td><p>&lt; F1 &gt;, &lt; Alt &gt;, &lt; L &gt;</p>
<p>Administration tab</p>
<p>[Delete] button</p></td>
</tr>
<tr class="odd">
<td rowspan="5">Microsoft Sans Serif</td>
<td>Software Application names</td>
<td>EFR</td>
</tr>
<tr class="even">
<td>Registry names</td>
<td>Embedded Fragment Registry (EFR)</td>
</tr>
<tr class="odd">
<td>Database field names</td>
<td>Mode field</td>
</tr>
<tr class="even">
<td>Report names</td>
<td>Procedures report</td>
</tr>
<tr class="odd">
<td>Organization and Agency Names</td>
<td>DoD, VA</td>
</tr>
<tr class="even">
<td>Microsoft Sans Serif, 50% gray and italics</td>
<td>Read-only fields</td>
<td><em>Procedures</em></td>
</tr>
<tr class="odd">
<td>(Any font)</td>
<td>Editable text fields</td>
<td>Text fields with light yellow background</td>
</tr>
<tr class="even">
<td>Calibri</td>
<td>References to the content area components (panels, fields, labels, etc.)</td>
<td>Insofar as possible, fonts and colors which match what you see on screen: <strong>Patient panel</strong>.</td>
</tr>
<tr class="odd">
<td>Times New Roman</td>
<td>Normal text</td>
<td>“… designed for use by designated Registry Coordinators, Managers, and Clinicians….”</td>
</tr>
<tr class="even">
<td rowspan="3">Times New Roman Italic</td>
<td>Text emphasis</td>
<td>“It is <em>very</em> important…”</td>
</tr>
<tr class="odd">
<td>National and International Standard names</td>
<td><em>International Statistical Classification of Diseases and Related Health Problems</em></td>
</tr>
<tr class="even">
<td>Document names</td>
<td><em>Embedded Fragment Registry User Manual</em></td>
</tr>
</tbody>
</table>

<span id="_Ref266257896" class="anchor"></span>Table 3 – VA-Approved Internet Browsers

| Graphic                                                                                                              | Used for…                                                           |
|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/002.png)     | Information of particular interest regarding the current subject matter |
| ![](embedded-fragments-version-1-user-manual/003.png)      | A tip or additional information that may be helpful to the user         |
| ![](embedded-fragments-version-1-user-manual/004.png) | A warning concerning the current subject matter                         |
| ![](embedded-fragments-version-1-user-manual/005.png)                     | Indicates an action or process which is optional                        |
| ![](embedded-fragments-version-1-user-manual/006.png)                     | Indicates a resource available either in this document or elsewhere     |

<span id="_Ref253055842" class="anchor"></span>Table 4 – Tasks by Role

## Command buttons and Command icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref262720889" class="anchor"></span>Table 5 – Task Categories and Tasks</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](embedded-fragments-version-1-user-manual/007.png)</p>
<p>![](embedded-fragments-version-1-user-manual/008.png)</p>
<p>![](embedded-fragments-version-1-user-manual/009.png)</p>
<p>![](embedded-fragments-version-1-user-manual/010.png)</p></th>
<th><p>A command button initiates an action. It is a rectangular “3-dimensional” shape with a label that specifies what action will be performed when the button is clicked. Common examples are shown at left. Command buttons that end with three dots indicate that selecting the command may evoke a subsidiary window.</p>
<p>In some cases, a command icon performs the same function, but appears on the menu bar and has a plain, flat appearance. Examples are shown at left.</p>
<p>In the text of this document, both command button and command icon names appear inside square brackets. <em>Examples:</em> [Search], [Save].</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref262720889" class="anchor"></span>Table 5 – Task Categories and Tasks

## The Embedded Fragment Registry Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Embedded Fragment Registry application (EFRA) supports the maintenance of local and national registries for clinical and resource tracking of care for such Veterans. This application allows access to important demographic and clinical data on all [Veterans Healthcare Administration (VHA)](#Glos_VHA) patients with these conditions, and provides many capabilities to [Veterans Affairs (VA)](#Glos_VA) facilities that provide care and treatment to patients with these conditions, including clinical categorization of patients. It also will provide (in a future build) clinical and administrative reports for the [Toxic Embedded Fragment Surveillance Center (TEFSC)](#Glos_TEFSC) and local medical center use.

EFRA accesses several other [Veterans Health Information Systems and Technology Architecture](#Glos_VistA) ([VistA](#Glos_VistA)) files that contain information regarding other diagnoses, prescriptions, surgical procedures, laboratory tests, radiology exams, patient demographics, hospital admissions, and clinical visits. This access allows identified clinical staff to take advantage of the wealth of data supported through VistA.

<table>
<caption><p><span id="_Toc312737946" class="anchor"></span>Table 6 – Screen Numbers &amp; Hierarchy</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/011.png)</th>
<th><p><strong>Note:</strong> Throughout this document…</p>
<ul>
<li><blockquote>
<p>The Embedded Fragment Registry is referred both as “EFR” and as “the Registry.”</p>
</blockquote></li>
<li><p>“Embedded Fragment Registry Application” and the corresponding acronym EFRA both refer to the <a href="#Glos_WBA">web-based application (WBA)</a> described in this document.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc312737946" class="anchor"></span>Table 6 – Screen Numbers & Hierarchy

## Purpose of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This User Manual provides instructions for using EFRA, which has been developed in support of the EFR.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EFRA *User Manual* is designed for use by [TEFSC](#Glos_TEFSC) personnel who are responsible for entering and reviewing data on patients whose records are being considered for inclusion in the Registry.

## Hardware Recommendations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please see the *Registries Installation & Configuration Guide for Web-Based Applications (RICG)* for hardware recommendations.

# Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The [VHA](#Glos_VHA) is charged with supporting the Presidential Task Force on Returning Global War on Terror Heroes. The Task Force has stated in the *Global War on Terror (GWOT)* report (recommendation P-7)[^1] that the [VA](#Glos_VA) shall “create an ‘Embedded Fragment’ Surveillance Center and Registry to monitor returning service members who have possibly retained fragments of materials in order to provide early medical intervention.”

The potential for short and long term health effects related to embedded fragments and knowledge of the large number of injuries to soldiers in Iraq resulting in embedded fragments, many composed of hazardous materials, led to the decision that all Veterans with embedded fragments should be identified, screened and monitored by the [VA](#Glos_VA). The [TEFSC](#Glos_TEFSC) has been established at the <span class="mark">REDACTED</span> to coordinate this effort.

A critical component of the TEFSC medical surveillance program is the development of a Registry providing access to the names, contact information, medical history, biological monitoring data and fragment analyses information for all Veterans who have one or more embedded fragments or who are likely to have embedded fragments. The Registry will be used as a medical surveillance tool by providing a mechanism to identify Veterans with embedded fragments; manage clinical data related to embedded fragments; and develop medical and surgical guidelines that will enable the TEFSC staff and [VA](#Glos_VA) clinicians to deliver appropriate medical care to these Veterans.

## Project Scope and Objectives 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document applies to the EFR project OBS-104-05-01-004, defined under the authority of [TEFSC](#Glos_TEFSC). It does not address a broader vision that may apply to a future integration of multiple medical data registries.

In the early stages of planning for TEFSC, one approach considered a gradual implementation of functionality supporting very basic TEFSC operations by making temporary modifications to the existing [VistA](#Glos_VistA) system. These modifications were limited in scope and temporary in nature and as such have been developed as an interim solution. This interim solution is under consideration for delivery. The development of EFRA described in this document envisions a more mature product to replace the interim solution.

This document describes software features that support TEFSC business operations for a limited scope of roles and responsibilities. In the longer term perspective, another solution will be required to address an expanded scope of business practice to support the broader goals of TEFSC.

## The Embedded Fragment Registry Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EFRA is a software product which supports the maintenance of local and national registries for clinical and resource tracking of care for Veterans with embedded fragments in their bodies. This application allows access to important demographic and clinical data on all Veterans who may have such injuries, regardless of whether they have been or are currently being seen in a [VHA](#Glos_VHA) facility for these injuries. EFRA also offers many capabilities to [VA](#Glos_VA) facilities that provide care and treatment to patients with these conditions, including clinical categorization of patients and, later, automatic transmission of data to the joint [DoD](#Glos_DoD)/VA Registry.

The [VA](#Glos_VA) does not currently maintain data about embedded fragments in a computable format. The data is maintained within the [VistA](#Glos_VistA) Hospital Information System (HIS) under the [Computerized Patient Record System (CPRS)](#Glos_CPRS) in a non-computable text format gathered from questionnaires (see [Appendix B](#AppendixB)) completed by patients or clinicians. The data must be extracted manually and entered into EFRA to be later exported to the Registry.

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Basic data about individuals is provided by the data feed from the [VA](#Glos_VA) Corporate Data Warehouse (CDW). One purpose of EFRA is to provide a means of making text data “[computable](#Glos_computabledata).”

EFRA is not installed on your computer workstation. Rather, EFRA runs in a web [browser](#Glos_Browser) from a location on the VA [intranet](#Glos_Intranet). For that reason, EFRA is referred to as a [WBA](#Glos_WBA). If you have already used any program which runs in a web browser, especially another Registry program (like the [Traumatic Brain Injury](#Glos_TBI) Registry applications), then EFRA will seem familiar to you. Although it is likely that the application will run on many different web browsers, please see Table 3 for the browsers which have been tested and approved for use with EFRA. These browsers have been tested for use with EFRA and are believed to be fully functional. If you encounter unusual problems, please submit a Remedy report and/or consult with your local IRM.

| ![](embedded-fragments-version-1-user-manual/012.png) | Note: This document does not attempt to explain everything about how to operate in the web browser environment itself; if you need help with using a browser, please contact your supervisor for information about training in browser use. |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc327881637" class="anchor"></span>Table 7 – Browser Shortcut Keys

<table>
<caption><p><span id="_Toc327881638" class="anchor"></span>Table 8 – EFR Health Factors</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/013.png)</th>
<th><p><strong>WARNING:</strong> This application will display <a href="#Glos_PII">personally identifiable information</a> (<a href="#Glos_PII">PII</a>). When you have finished using the application, you should <em>close all instances of your browser</em> that may be running (not just the one you used to access the application).</p>
<p>If you do not, PII could be compromised if another user accesses your web browser.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc327881638" class="anchor"></span>Table 8 – EFR Health Factors

| Browser                      | Version(s) | Remarks                          |
|------------------------------|------------|----------------------------------|
| Microsoft® Internet Explorer | 6.x, 7.x   | Does not support tabbed browsing |
| Mozilla® Firefox             | 3.x        | Supports tabbed browsing         |
|                              |            |                                  |
|                              |            |                                  |
|                              |            |                                  |

### Data Receipt and Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Basic Patient Data

Within EFRA, basic Patient information is provided by the “[back-end](#Glos_backend)” system and is [read only (RO)](#Glos_RO). Since the data feed process is designed to produce a single record for each person, there should not be multiple records for the same person, although that could happen. In the future, a process will be available to allow users to place the record into a “pending” status until the duplicates can be resolved. In the meantime, there is a work-around process for handling duplicates; see 11.1.3.6 below.

#### The Triage Process

Patients being recommended as candidates for inclusion in the EFR may be referred by local [VA](#Glos_VA) Providers or identified by the [DoD](#Glos_DoD). Once the referral records are received by EFR, they go through a process known as “[triage](#Glos_Triage).” This process determines whether or not the patient will be admitted to the EFR, and, if so, what follow-up actions are to be taken. More details on triage may be found at 10 below.

#### Referral Review Process

A designated reviewer (the Medical Professional) then reviews the record and either approves or returns the record for more information.

- If not approved, the record is returned to the EFR TEFSC Nurse (usually referred to as simply “Nurse”).
- If approved, the patient is confirmed into the Registry. If monitoring or consultation was specified during the triage decision, a [workflow](#Glos_workflow) is set up to enable appropriate actions.
- If an ineligibility decision is upheld, the patient is not accepted into the Registry and the record is closed.

#### Other Uses of EFRA

EFRA is also used to make a determination regarding the next steps for obtaining additional information on the patient that will be relevant to the information maintained in the EFR application. EFRA will handle the possibility of a patient being referred multiple times, as well as the actions taken by the Nurse in EFRA when a referral is determined ineligible. EFRA does *not*, however, cover actions the Nurse may take that are not supported by interaction with the system (such as notifying the Local Provider of a decision to identify the patient as ineligible).

## Release History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes provided by releases are shown in the following series of tables. Under “Type,” “E” indicates an enhancement, “F” a fix, and “M” a modification. Click on the green links immediately below to jump directly to a specific release.

| EFR Release 1.0 | EFR Release 4.0 | EFR Release 5.0 |     |
|-----------------|-----------------|-----------------|-----|

### EFR Release 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                     | Type |
|-----|-------------------------------------------------|------|
| 1   | Published application for first production use. | E    |

### EFR Release 4.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                       | Type |
|-----|---------------------------------------------------------------------------------------------------|------|
| 1   | Added information describing the super users’ ability to edit interpretation letter               | M    |
| 2   | Added section regarding importing the VTA extract data on the                                     | M    |
| 3   | Added information pertaining to importing Biomonitoring Lab Results from the Baltimore TEFSC lab. | M    |
| 4   | Added information describing the super users’ ability to unaccept lab results                     | M    |
| 5   | Added VTA data export information                                                                 | M    |
| 6   | Added information describing the Auto-Triage process                                              | M    |
| 7   | Updated new Lab Kit screens and information                                                       | M    |

### EFR Release 5.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 85%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Modified the Patients export to include a column to contain the patient's Service Branch. The Service Branch is displayed in the patient information panel at the top of the Lab Orders screen.</td>
<td>M</td>
</tr>
<tr class="even">
<td>2</td>
<td>Assess Biomonitoring Questionnaire wizard for performance improvements, including the Fragment Form.</td>
<td>F</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Completed Fragment Collection Form not retaining data </td>
<td>F</td>
</tr>
<tr class="even">
<td>4</td>
<td>Exception occurred when more than 4000 characters are entered for “Reason for Contact” / “Textual Record of the contact Conversation” fields in Add Comment screen </td>
<td>F</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Added OEF/OIF Indicator, Iraq Afghan Service Health Factor, and Service Separation Date to Referral screens; OEF/OIF and Service Separation Date to Patients export; Added Iraq/Afghan Service health factor as new column on Patients export.</p>
<p>Updated all EFR referrals to include Iraq/Afghan Service health factor  (just an ETL data conversion exercise)</p></td>
<td>E</td>
</tr>
<tr class="even">
<td>6</td>
<td>Added a new button and a screen to the Lab Tests of Interest Patient look up when a match is present; added a new export for Related Lab Tests</td>
<td>E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>VTA ICD9 code update</td>
<td>F</td>
</tr>
<tr class="even">
<td>8</td>
<td>Added ICD10 capabilities</td>
<td>M</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Filter by site number (or more than one site number)</td>
<td>M</td>
</tr>
<tr class="even">
<td>10</td>
<td>Lookup patient by Lab Request (TEF) number</td>
<td>M</td>
</tr>
<tr class="odd">
<td>11</td>
<td>Added a DoD Fragment Data message on the Referral screen; New buttons and new screens under Workflows in Patient Lookup for DoD Fragment Data; Display raw data from DoD lab(s); Enter DoD fragment data into EFR; New Export to reflect the frag data entered in 2(b).</td>
<td>E</td>
</tr>
<tr class="even">
<td>12</td>
<td>Allow creation of manual referral</td>
<td>E</td>
</tr>
<tr class="odd">
<td>13</td>
<td>Create referral when only 2nd Clinical Reminder is completed in VistA </td>
<td>M</td>
</tr>
<tr class="even">
<td>14</td>
<td>Back button on referral screen loads wrong queue</td>
<td>F</td>
</tr>
</tbody>
</table>

## Obtaining Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no EFRA software distributives. Since EFRA is a web-based application, only a [VA](#Glos_VA)-approved web [browser](#Glos_Browser) (see list at [Appendix D](#AppendixD)) and access to the VA [intranet](#Glos_Intranet) is required.

Documentation files are available for downloading from the following Office of Information and Technology Field Offices (OI&T FO) \[ANONYMOUS SOFTWARE\] directories. [File Transfer Protocol (FTP)](#Glos_FTP) client software may be useful, although it is possible to download these files using a web browser as well.

| OIFO                               | FTP Address                        | Directory                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

The EFRA guides and manuals are distributed as the following set of files:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 58%" />
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
<td>EFRA5_0DOC1.ZIP</td>
<td><p>Zipped DOC distributive, which includes both .PDF and .DOC formats:</p>
<p>►      User Manual (EFRA5_0_UM)</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>EFRA5_0DOC2.ZIP</td>
<td><p>►      Registries Installation &amp; Configuration Guide (REG5_0_IG)</p>
<p>►      Systems Management Guide (EFRA5_0_SM)</p></td>
<td>BINARY</td>
</tr>
</tbody>
</table>

## Documentation on the Intranet 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this product, including all of the software manuals, is also available in the Health*<u>e</u>*Vet section of the [VA](#Glos_VA) Software Document Library (VDL). Following national release of the application, the Embedded Fragment Registry documentation may be found at <http://www4.va.gov/vdl/application.asp?appid=187>. The documentation set includes:

- *Registries Installation & Configuration Guide for Web-Based Applications*
- *EFR Systems Management and Security Guide*
- *EFR User Manual* (this document)
2.  <span id="_Toc327881342" class="anchor"></span>About the Application

# Software Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/014.png)</th>
<th><p><strong>WARNING:</strong> This application will display <a href="#Glos_PII">personally identifiable information</a> (<a href="#Glos_PII">PII</a>). When you have finished using the application, you should <em>close all instances of your browser</em> that may be running (not just the one you used to access the application). Also be sure to safeguard any screen prints or reports which may contain PII.</p>
<p>If you do not, PII could be compromised if another user accesses your web browser.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Web-Based Application Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a [web-based application](#Glos_WBA); see [Appendix D](#AppendixD) for a description of typical [WBA](#Glos_WBA) elements.

## Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two kinds of online help are or will be available: help for using the browser itself, and help for EFRA.

### Browser Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have little or no familiarity with the browser environment, information can be found by accessing the browser’s Help file. Depending on the browser you are using and the way it may have been customized, the following methods may be used:

| ![](embedded-fragments-version-1-user-manual/015.png)     | Pressing the \< F1 \> key is the traditional way to access online help. In a web-based application like EFRA, \< F1 \> will provide help about how to operate the *browser* itself.                                                                                                      |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/016.png) | The help icon in Internet Explorer® is typically found somewhere on the light gray browser menu bars at the top of the screen. How your browser is set up will determine whether or not this icon appears on your browser. The Firefox® browser typically does not display such an icon. |
| <u>H</u>elp                                                                                          | Click the Help menu option on the browser’s menu bar.                                                                                                                                                                                                                                    |

### Application Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Help icon, available on every screen of the application, opens the EFRA online help file. In most cases, the help offered will be specific to the topic or screen that you were viewing when you clicked the icon. In some cases, however, a specific help topic may not be available, in which case you will see the table of contents for the help file. From that point, you may browse and search for more specific help. The online help file is contained in a series of web pages.

| ![](embedded-fragments-version-1-user-manual/017.png) | Note: Since EFRA is not a “desktop” application (that is, it does not reside on your computer desktop), pressing \< F1 \> will not open EFRA help. Instead, it will open help for the browser that you are using. |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](embedded-fragments-version-1-user-manual/018.png) | Note: The display you see in the actual help file may vary from the illustration below. |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|

<span class="mark"></span>![](embedded-fragments-version-1-user-manual/019.png)

<span id="_Toc327881480" class="anchor"></span>Figure 1 – Sample Online Help Page

## Accessibility Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Standard web browser keyboard shortcuts and application design elements help to make EFRA accessible to a wide range of users, including those with limited dexterity, low vision, or other disabilities.

![](embedded-fragments-version-1-user-manual/020.png) For a complete list of keyboard shortcuts, see Appendix A.

![](embedded-fragments-version-1-user-manual/021.png) For more information about accessibility features, see Appendix B.

## Date of Death and Deceased Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some Registry programs perform “deceased checks” of files for each patient in the local registry to validate whether or not the patient is deceased. Although EFRA does not perform such a check, it does capture the Date of Death, if that information is entered in the source files. In order for the referral to be sent to EFRA, the patient is screened via the two [Operation Enduring Freedom/](#Glos_OEF)[Operation Iraqi Freedom](#Glos_OIF) (OEF/OIF) clinical reminders in [VistA](#Glos_VistA). It seems unlikely that a new referral would be received for a deceased patient. At present, there is nothing in the system to prevent such a record from being edited.

## Screen Areas and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While there are some differences in screen appearance from one task area to another, the general layout is as shown below; ![](embedded-fragments-version-1-user-manual/022.png) indicate the parts of the screen. Please take a few moments to familiarize yourself with the various screen areas before you begin.

![](embedded-fragments-version-1-user-manual/023.png)

<span id="_Ref261865025" class="anchor"></span>Figure 2 – Screen Areas

### Banner Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Across the top of the screen is the BANNER AREA. It displays the [VA](#Glos_VA) logo and the Registry name.

### Tabs (Common Navigation Area)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TABS immediately below the application title provide a COMMON NAVIGATION AREA that you will see in all Registry web-based applications. These elements allow you to select the type of task to be performed.

- Patients: To view and edit patient records. MORE INFORMATION: 18 below
- My Tasks: To see a list of tasks assigned to you. MORE INFORMATION: 10 below
- Administration: To create user accounts and assign roles. Only visible to people who have administrative credentials. MORE INFORMATION: 19 below
- Help: Complete online help is not yet available for EFRA, and although you may see the help icon and the tab label in the initial build of the application, only a “placeholder” help page may be available. Fully functional help is expected to be available in Build 2.

| ![](embedded-fragments-version-1-user-manual/024.png) | Note: The left-right order of tabs may be different from that depicted in this document. EFRA has adopted a “patient-centric” approach, and the <span class="smallcaps">Patient</span> tab will be the primary tab for most EFRA users. Regardless of the display order and which tab is set as the default, the functionality for all tabs will, however, be essentially the same as discussed in this document. |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Breadcrumbs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Note the so-called <span class="mark">BREADCRUMBS</span> which appear below the tabs (showing, in this case, <span class="smallcaps">My Tasks \> Referrals \> New</span>); this shows you where you are within the application, how you got there, and the current page's logical parent pages in the information hierarchy. The breadcrumbs *cannot* be used for navigation.

![](embedded-fragments-version-1-user-manual/025.png)

<span id="_Toc327881482" class="anchor"></span>Figure 3 – Breadcrumbs

### Left Navigation Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a TAB is selected, the available tasks for that tab are displayed in the <span class="mark">LEFT NAVIGATION BAR </span>at the far left of the screen.

![](embedded-fragments-version-1-user-manual/026.png)

<span id="_Toc327881483" class="anchor"></span>Figure 4 – Left Navigation Bar

### Content Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <span class="mark">CONTENT AREA</span>contains a number of web parts, specific to the Registry and specific to which common navigation item was selected. Example: In EFRA, this screen could show a list of patients. The contents of this area will change depending on which task you have selected. In some cases, the area expands to allow display room for more information, and the <span class="mark">LEFT NAVIGATION BAR </span>temporarily disappears.

For reference purposes, the content area is typically composed of panels (and sometimes subpanels within those panels), the various data fields, and labels. Please see Figure 5.

![](embedded-fragments-version-1-user-manual/027.png)

<span id="_Ref269395724" class="anchor"></span>Figure 5 – Typical Content Area Components

Panel contents are presented inside blue-gray borders with rounded corners. Here, for example, is a typical Patient panel. In this sample, the panel outline has been darkened somewhat so that it shows up in print; on the screen, the panel outline color may be a lighter or darker shade, depending on your monitor settings:

![](embedded-fragments-version-1-user-manual/028.png)

<span id="_Toc327881485" class="anchor"></span>Figure 6 – Typical Patient Panel

Insofar as possible, text references to the content area components will be shown with colors and fonts that match what you see on screen (for example, the Patient panel as shown above).

# User Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your ability to use various features of EFRA will depend upon your assigned role. Some choices will not be available to you if your role does not call for that particular task. You may be assigned more than one role. Roles are assigned by a member of the EFR TEFSC Administration Staff. The available roles are:

- EFR TEFSC Nurse: The EFR TEFSC Nurse (or TEFSC Nurse, or Nurse) is responsible for interaction with [VA](#Glos_VA) providers and patients to assist with information gathering required to make Registry population determinations and coordination of clinical consultations. The Nurse is also responsible for reviewing new referrals and making the preliminary decision on whether a patient should be admitted to the Registry, and what follow-up action is required. This is the process called [triage](#Glos_Triage).
- EFR Data Entry Personnel: When biomonitoring specimen collection kits are returned to TEFSC, they contain a completed biomonitoring questionnaire; when fragment collection kits are returned to TEFSC they contain a completed fragment specimen collection form. The EFR Data Entry Personnel (or Data Entry Personnel, or Data Entry) record information from the forms into EFRA. In addition, if they learn of changes to alternate contact information from the form received, they may edit form details and add, edit, or delete alternate contact information associated with the patient.
- EFR Administration Staff: The EFR Administration Staff (or Administration Staff, or Admin Staff, or Administrator) is responsible for administrative activities associated with placing kit orders with third party vendors for specimens and fragments. The Administrator will also manage kit tracking and sample tracking. Finally, Administrator can assign or edit user roles.
- EFR TEFSC Coordinator (Super User): The EFR TEFSC Coordinator (or TEFSC Coordinator, or Coordinator) is ultimately responsible for following EFR patients through their lifecycle of involvement with [TEFSC](#Glos_TEFSC). The Coordinator is responsible for keeping the TEFSC Providers informed of status of cases. Another responsibility of the Coordinator is to perform population level surveillance using data captured in the EFR. The Coordinator also has the capability to conduct the triage process. As a Super User, this role also provides assistance to other users when needed.
- EFR TEFSC Provider: EFR TEFSC Providers (or TEFSC Providers) are the physicians located at the [TEFSC](#Glos_TEFSC). They act as subject matter experts on the standards of care as they apply to Veterans who have embedded fragments. Through analysis of EFR data they develop handbooks and directives that convey care guidelines to the Local [VA](#Glos_VA) Providers at VAMC facilities. TEFSC Providers also interpret lab results for individual patients to provide treatment recommendations to the Local VA Providers. TEFSC Providers also have the capability to conduct the triage process.

Table 4 shows the tasks available for various roles.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Role</th>
<th>Access</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TEFSC Nurse</td>
<td><ul>
<li><p>Referrals</p></li>
<li><p>Contact Log (TEFSC Nurse cannot delete a contact log entry)</p></li>
<li><p>Patients</p></li>
<li><p>Questionnaires/Forms</p></li>
<li><p>Lab Results</p></li>
<li><p>Interpretation &amp; Follow Up</p></li>
</ul></td>
</tr>
<tr class="even">
<td>TEFSC Data Entry Personnel</td>
<td><ul>
<li><p>Lab Kits</p></li>
<li><p>Lab Orders</p></li>
<li><p>Lab Results</p></li>
<li><p>Contact Log (Admin Staff cannot delete a contact log entry)</p></li>
<li><p>Patients</p></li>
<li><p>Interpretation &amp; Follow Up (Interpreted – printing)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Admin Staff (aka TEFSC Administrator)</td>
<td><ul>
<li><p>Lab Kits</p></li>
<li><p>Lab Orders</p></li>
<li><p>Lab Results</p></li>
<li><p>Contact Log (Admin Staff cannot delete a contact log entry)</p></li>
<li><p>Patients</p></li>
<li><p>Interpretation &amp; Follow Up (Interpreted – printing)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>TEFSC Provider</td>
<td><ul>
<li><p>Referrals</p></li>
<li><p>Interpretation &amp; Follow Up</p></li>
<li><p>Contact Log (TEFSC Provider cannot delete a contact log entry)</p></li>
<li><p>Patients</p></li>
<li><p>Questionnaires/Forms</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>TEFSC Coordinator (Super user)</td>
<td><ul>
<li><p>All EFR application functionality, including Administration functions and Reports</p></li>
</ul></td>
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
<th>![](embedded-fragments-version-1-user-manual/029.png)</th>
<th><p><strong>Tip:</strong> If you do not know (or cannot remember) your assigned role(s), look at the bottom of any screen. You will see your user name plus the roles assigned to you:</p>
<p>Current User:   First Last name<br />
Role(s): EFR TEFSC COORDINATOR (Super User), EFR Admin Staff, EFR TEFSC PROVIDER, EFR TEFSC NURSE, EFR Data Entry Personnel</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Software Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Starting the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start EFRA, follow these steps:

1.  Make sure that you are logged on to Windows<sup>®</sup> and the [VA](#Glos_VA) network using the appropriate identity.
2.  ![](embedded-fragments-version-1-user-manual/030.png)![](embedded-fragments-version-1-user-manual/031.png) Start your web browser. The browser opens the site that you have designated as your home page.

| ![](embedded-fragments-version-1-user-manual/032.png) | ![](embedded-fragments-version-1-user-manual/033.png) |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Firefox                                                                                              | Internet Explorer                                                                                    |

3.  In the address bar, enter the web address of the application page, which will be provided to you when you are designated as an authorized user.

## Logging In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many registry-associated programs, including EFRA, use Windows authentication provided by [Active Directory (AD)](#Glos_AD). Your user identity is detected at the time of initial login to the [VA](#Glos_VA) network, so a separate login or authentication is not normally required to run EFRA. Security messages will advise you if you are not logged in, have insufficient privileges, etc. This means that if you are already logged into your usual domain, the web page which provides EFRA should load automatically without challenge. You should be able to open your web browser, enter the Uniform Resource Locator (URL), and see EFRA run automatically.

If you are logged in and you see either of the two “challenge” pop-up windows, or have other questions related to AD, please contact your IRM for assistance.

| Internet Explorer                                                                                  | Firefox                                                                                            |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/034.png) | ![](embedded-fragments-version-1-user-manual/035.png) |

The authentication of your EFRA role(s), and your privileges, takes place behind the scenes. Following successful authentication, you will be re-directed to EFRA.

## Default Registry Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you enter the application URL and log in (if required), your default EFR screen opens.

EFR incorporates a “patient-centric” approach, and it also includes a reminder capability to alert you to upcoming actions to be taken. The first screen you see will normally be the <span class="smallcaps">Patients Lookup</span> screen (Figure 7). If you have reminders stored in the system, you will first see the <span class="smallcaps">Follow Up Event Reminders</span> screen (see 7.4 below).

![](embedded-fragments-version-1-user-manual/036.png)

<span id="_Ref272247468" class="anchor"></span>Figure 7 – Patients Lookup Screen

From any screen, however, you can also jump to other sections of the program by using the TABS and the <span class="mark">LEFT NAVIGATION BAR </span>(see 3.5 above).

# Patients tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From any area of the application, you can search for a patient already in the Registry. Click on the Patients tab; the <span class="smallcaps">Patients \> Patients Lookup</span> screen appears and displays the Lookup Patient panel.

![](embedded-fragments-version-1-user-manual/037.png)

<span id="_Toc327881487" class="anchor"></span>Figure 8 – Patients \> Patients Lookup

You can search using the patient’s social security number (SSN), patient’s First and/or Last Name, [Integration Control Number (ICN)](#Glos_ICN), or a combination. EFRA uses “contains” search logic. *Do not* use “wildcard” indicators like “\*” or “?” in your search.

Here we enter the Last Name and click on \[Search\] (or, you may press the \< Enter \> key). Note how the text entry box background changes to light yellow when you start entering text.

![](embedded-fragments-version-1-user-manual/038.png)

<span id="_Toc327881488" class="anchor"></span>Figure 9 – Patient Search Pane

INCLUDES:

- Lookup Patient \[all text boxes\]
  - SSN
  - First Name
  - Last Name
  - ICN

![](embedded-fragments-version-1-user-manual/039.png) When you have entered the data, click the \[Search\] button.

## Patient Not Found

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a patient is not found using your search criteria, you will see this result:

![](embedded-fragments-version-1-user-manual/040.png)

<span id="_Toc327881489" class="anchor"></span>Figure 10 – No EFR Patients Found

Your options are:

| ![](embedded-fragments-version-1-user-manual/041.png) | Click \[OK\] to continue searching the Registries database for the patient record. |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/042.png) | Click \[Cancel\] to cancel the search and look for another patient                 |

If the patient is not in the Registries database, EFR will display a notification:

![](embedded-fragments-version-1-user-manual/043.png)

<span id="_Toc327881490" class="anchor"></span>Figure 11 – Patient Not Found

Enter new search information and click \[Search\] to search for a new patient. If a patient is found in the Registry that needs to be added to EFR, refer to Section 6.3 6.3Manual Referral.

## Patient Search Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this case, we find several patients:

![](embedded-fragments-version-1-user-manual/044.png)

<span id="_Toc327881491" class="anchor"></span>Figure 12 – Patient Search Results

To view complete information for a patient, click on one of the selection buttons at the right of the row listing the patient. Buttons will be shown as available (that is, not grayed-out) only if there are any such records for the patient.

| ![](embedded-fragments-version-1-user-manual/045.png) | To see information about the patient, click the \[Patient Information\] button. MORE INFORMATION: 6.2.1 below                             |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/046.png)     | To see the [workflows](#Glos_workflow) associated with this patient, click the \[Workflows\] button. MORE INFORMATION: 6.2.2 below        |
| ![](embedded-fragments-version-1-user-manual/047.png) | The \[Related Diagnoses\] button is shown available only if there are any such diagnoses for the patient. MORE INFORMATION: 6.2.2.4 below |
| ![](embedded-fragments-version-1-user-manual/048.png)   | The \[Lab Tests\] button is shown available only if there are any lab tests of interest for the patient. MORE INFORMATION: 6.2.4 below    |

### Patient Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All available patient data is displayed. Note that the data in the Patient Information panel (which was brought over from [VistA](#Glos_VistA)) is read-only here.

![](embedded-fragments-version-1-user-manual/049.png)

<span id="_Toc327881492" class="anchor"></span>Figure 13 – Patient Selected – Patient Information Shown

INCLUDES:

- Patient Information \[all pre-filled text\]
  - *ICN* \| *SSN*
  - *Full Name*
  - *Home VAMC*
  - *Gender* \| *Birth Date*
  - *Race* \| *Death Date*
  - *Marital Status* \| *Ethnicity*
  - *Address* \| *City*
  - *Address Line 2* \| *State*
  - *Address Line 3* \| *Postal Code*
  - *County* \| *Country*
  - *Home Phone* \| *Work Phone*
- Patient Alternate Contact Information \[all text fields except as noted\]

You may enter data in the Patient Alternative Contact Information panel \[all text boxes unless otherwise noted\]

- Alternate Street Address 1 \| 2 \| 3
- Alternate City
- Alternate State
- Alternate ZIP
- Alternate Country
- Alternate Home Telephone
- Alternate Work Telephone
- Alternate Mobile Telephone
  - Preferred Alternate Telephone Number \[ radio buttons; select one\]
    - Home
    - Work
    - Mobile
- Email Address

Again, note that the text field turns light yellow when you begin to enter text:

![](embedded-fragments-version-1-user-manual/050.png)

<span id="_Toc327881493" class="anchor"></span>Figure 14 – Patient Alternate Contact Information (Showing New Data Entry)

![](embedded-fragments-version-1-user-manual/051.png) Click \[Cancel\] to discard any changes you have made, or to exit without making any changes. You return to the referral record screen.

![](embedded-fragments-version-1-user-manual/052.png) Or, click the \[Save\] button to save the data you entered. A popup is displayed:

![](embedded-fragments-version-1-user-manual/053.png)

<span id="_Toc327881494" class="anchor"></span>Figure 15 – Save Successful Popup Message

![](embedded-fragments-version-1-user-manual/054.png) Click \[OK\] to dismiss the popup.

The screen now shows the updates you made in the appropriate fields. Make other changes as needed and click \[Save\]. When you have made all desired changes, use the LEFT NAVIGATION BAR or the TABS to continue with other tasks.

### Workflow Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you select a workflow record for a patient, you see the list of referrals as well as information about contact entries and workflows (if any) associated with that patient:

#### No Contact Entries, No Workflows, No DoD Fragment Data

Here is a referral with no contact entries, no workflows:

![](embedded-fragments-version-1-user-manual/055.png)

<span id="_Toc327881495" class="anchor"></span>Figure 16 – Referral Record (No Contacts, Workflows, or DoD Fragment Data)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/056.png)</th>
<th>To see the referral record, click the [Select Referral] button. MORE INFORMATION: 11.1.3 below.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Since there are no contact entries or DoD Fragment data, the [Select Contact Entries], [Display Source DoD Fragment Data], and [Enter/View DoD Fragment Data] buttons respectively are unavailable (grayed out).</p>
<p>If Contact Entries are present, refer to Section 11.1.3.4 below. If DoD Fragment Data is present, refer to Section 6.2.2.4 below.</p></td>
</tr>
<tr class="even">
<td>![](embedded-fragments-version-1-user-manual/057.png)</td>
<td>Click [Cancel] to return to the patient search results.</td>
</tr>
</tbody>
</table>

#### No Contact Entries, One Workflow

Here we see a referral with no contact entries and one workflow:

![](embedded-fragments-version-1-user-manual/058.png)

<span id="_Toc327881496" class="anchor"></span>Figure 17 – Referral Record (Contacts / Workflows)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/059.png)</th>
<th>To see the referral record, click the [Select Referral] button. MORE INFORMATION: 11.1.3 below.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Since there are no contact entries or DoD Fragment data, the [Select Contact Entries], [Display Source DoD Fragment Data], and [Enter/View DoD Fragment Data] buttons respectively are unavailable (grayed out).</p>
<p>If Contact Entries are present, refer to Section 11.1.3.4 below. If DoD Fragment Data is present, refer to Section 6.2.2.4 below.</p></td>
</tr>
<tr class="even">
<td>![](embedded-fragments-version-1-user-manual/060.png)</td>
<td>Click [Select] to view the associated lab kits (MORE INFORMATION: Section 13 below), Questionnaires/Forms (MORE INFORMATION: Section 14 below), lab orders (MORE INFORMATION: Section 0 below), Lab Results (MORE INFORMATION: Section 16 below) and/or Interpretation &amp; Diagnosis (MORE INFORMATION: Section 17 below).</td>
</tr>
<tr class="odd">
<td>![](embedded-fragments-version-1-user-manual/061.png)</td>
<td>Click [Cancel] to return to the patient search results.</td>
</tr>
</tbody>
</table>

#### Contact Entries, Multiple Workflows

And here is a referral which has reminders (see 7.4 below) as well as both contacts and workflows:

![](embedded-fragments-version-1-user-manual/062.png)

<span id="_Toc327881497" class="anchor"></span>Figure 18 – Referral Record (Contacts / Workflows; No DoD Fragment Data)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/063.png)</th>
<th>To see the referral record, click the [Select Referral] button. MORE INFORMATION: 11.1.3 below.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](embedded-fragments-version-1-user-manual/064.png)</td>
<td>Click the [Select Contact Entries] to view the Contact Entries. MORE INFORMATION: 11.1.3.4 below</td>
</tr>
<tr class="even">
<td colspan="2"><p>Since there is no DoD Fragment data, the [Display Source DoD Fragment Data] and [Enter/View DoD Fragment Data] buttons respectively are unavailable (grayed out).</p>
<p>If DoD Fragment Data is present, refer to Section 6.2.2.4 below.</p></td>
</tr>
<tr class="odd">
<td>![](embedded-fragments-version-1-user-manual/065.png)</td>
<td>Click [Select] to view the associated lab kits (MORE INFORMATION: Section 13 below), Questionnaires/Forms (MORE INFORMATION: Section 14 below), lab orders (MORE INFORMATION: Section 0 below), Lab Results (MORE INFORMATION: Section 16 below) and/or Interpretation &amp; Diagnosis (MORE INFORMATION: Section 17 below).</td>
</tr>
<tr class="even">
<td>![](embedded-fragments-version-1-user-manual/066.png)</td>
<td>Click [Cancel] to return to the patient search results.</td>
</tr>
</tbody>
</table>

#### DoD Fragment Data

When DoD Fragment data is present for a patient, the \[Display Source DoD Fragment Data\] and the \[Enter/View DoD Fragment Data\] are highlighted.

![](embedded-fragments-version-1-user-manual/067.png)

<span id="_Toc327881498" class="anchor"></span>Figure 19 – DoD Data Present

Opening DoD Fragment Source Data

DoD Fragment data will need to be added manually from the source spreadsheet.

Clicking \[Display Source DoD Fragment Data\] displays all extracted DoD source data:

![](embedded-fragments-version-1-user-manual/068.png)

<span id="_Toc327881499" class="anchor"></span>Figure 20 – DoD Source Data

| ![](embedded-fragments-version-1-user-manual/069.png)   | Click \[Open/Download\] to open the source data in a separate Excel spreadsheet. The system will prompt you to \[Open\] or \[Save\] the spreadsheet. Opening the spreadsheet will open the Excel file in a new window with all associated functionality. |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/070.png) | Click \[Back\] to return to the Workflow Screen.                                                                                                                                                                                                         |

The source spreadsheet opens:

![](embedded-fragments-version-1-user-manual/071.png)

<span id="_Toc327881500" class="anchor"></span>Figure 21 – Sample Source Spreadsheet

| ![](embedded-fragments-version-1-user-manual/072.png) | Note: Each spreadsheet will be formatted differently, depending on which of the three DoD labs submitting the information. |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|

Adding DoD Fragment Data

To add fragment data, click \[Enter / View DoD Fragment Data\].

![](embedded-fragments-version-1-user-manual/073.png)

<span id="_Toc327881501" class="anchor"></span>Figure 22 – Enter / View DoD Fragment Data Screen

Initially, this process must be completed in the following order:

- Add Lab Data
- Add Fragment Data
- Add Analyte Data

Once the initial fragment has been entered, additional Labs/Fragments/Analytes can be added in any order, following each process, respectively.

Adding Lab Data

On the DoD Fragment Click Add Lab Data:

![](embedded-fragments-version-1-user-manual/074.png)

<span id="_Toc327881502" class="anchor"></span>Figure 23 – Adding DoD Lab Data

INCLUDES:

- DoD Patient Information panel
- *Patient Name*
- *SSN*
- DoD Labe Data panel \[all checkboxes except as noted\]
- Lab Name \| Lab Repot Date
- Lab Code \| Lab ID
- Accession Number \| Producing Event Date

| ![](embedded-fragments-version-1-user-manual/075.png) | Click \[Save\] to save the updated Lab information and return to the DoD Fragment Data screen. |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/076.png) | Click \[Back\] to discard the changes and return to the.                                       |

Adding Fragment Data

After adding the Lab Data, click Add Fragment Data. The Add Fragment Data screen opens:

![](embedded-fragments-version-1-user-manual/077.png)

<span id="_Toc327881503" class="anchor"></span>Figure 24 – Adding DoD Fragment Data

INCLUDES:

- DoD Fragment Data panel
- Fragment ID \| Description
- Mass
- Mass Unit of Measure
- Dimensions panel
  - Length \| Length Unit of Measure
  - Height \| Height Unit of Measure
  - Width \| Width Unit of Measure
- Radioactive Indicator \[Yes No Not Tested\] \| Radioactive Results
- Comments
- Tissue Sent Indicator \[Yes No\] \| Tissue Associated with Fragment Details

| ![](embedded-fragments-version-1-user-manual/078.png) | Click \[Save\] to save the updated fragment information and return to the DoD Fragment Data screen. |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/079.png) | Click \[Back\] to discard the changes and return to the DoD Fragment Data screen.                   |

Add Analyte Data

After adding the Fragment Data, click Add Analyte Data. The Add Analyte Data screen opens:

![](embedded-fragments-version-1-user-manual/080.png)

<span id="_Toc327881504" class="anchor"></span>Figure 25 – Adding DoD Analyte Data

INCLUDES:

- Analyte Data panel
- Analyte \[Drop-down box\] \| Analysis Method \[Text box\]
- Analysis Type \[Drop-down box\] \| CAS Number \[Text box\]
- Result \[Text box\] \| Comments \[Text box\]

| ![](embedded-fragments-version-1-user-manual/081.png) | Click \[Save\] to save the updated fragment information and return to the DoD Fragment Data screen. |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/082.png) | Click \[Back\] to discard the changes and return to the DoD Fragment Data screen.                   |

The Analyte drop-down box contains a list of all the available analytes:

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/083.png)</th>
<th><p>INCLUDES:</p>
<p>Aluminum</p>
<p>Antimony</p>
<p>Chromium</p>
<p>Cobalt</p>
<p>Copper</p>
<p>Iron</p>
<p>Isotopic Du</p>
<p>Lead</p>
<p>Manganese</p>
<p>Molybdenum</p>
<p>Nickel</p>
<p>Tin</p>
<p>Titanium</p>
<p>Tungsten</p>
<p>Uranium</p>
<p>Vanadium</p>
<p>Zinc</p>
<p>Other</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Selecting Other exposes the Other Analyte text box:

![](embedded-fragments-version-1-user-manual/084.png)

<span id="_Toc327881505" class="anchor"></span>Figure 26 – Other Analyte Text Box

The Analysis Type drop-down box contains a list of the analysis types:

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/085.png)</th>
<th><p>INCLUDES:</p>
<p>Surface Analysis</p>
<p>Whole Fragment Analysis</p>
<p>None</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Related Diagnoses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you click the \[Related Diagnoses\] button associated with a patient, you see the related diagnoses:

![](embedded-fragments-version-1-user-manual/086.png)

<span id="_Toc327881506" class="anchor"></span>Figure 27 – Referral Record (Contacts / Workflows)

This is a read-only list; no entries or changes are allowed here. If the list is lengthy, however, you can sort it by clicking on one of the column headings.

INCLUDES:

For each related diagnosis:

- *ICD Code*
- *Description*
- *Encounter Date*
- *Site \#*
- *Facility Name*

![](embedded-fragments-version-1-user-manual/087.png) Click \[Cancel\] to return to the patient search results.

### Lab Tests of Interest

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patients who are included in EFR can receive care at conceivably any VA facility. When EFR patients receive care at a VA facility and are assigned a specific lab test as a result of that care, the EFRA captures the diagnosis code and/or lab test and results.

When you click the \[Lab Tests\] button associated with a patient, you see the related lab tests:

![](embedded-fragments-version-1-user-manual/088.png)

<span id="_Toc327881507" class="anchor"></span>Figure 28 – Lab Tests of Interests

INCLUDES:

- Patient Information panel \[all pre-filled text\]
- *Patient Name*
- *SSN*
- Related Lab Tests panel \[all pre-filled text\]
- *Test Name*
- *Result Date \| Date Specimen Collected \| Result \| Result Units \| Ref Low \| Ref High \| Abnormal Indicator \| Request Site Number \| Result Site Number \| LOINC*

| ![](embedded-fragments-version-1-user-manual/089.png) | Click \[Back\] to return to the Patient Lookup screen. |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------|

## Manual Referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a manual referral, click \[Create Referral\].

![](embedded-fragments-version-1-user-manual/090.png)

### Create Referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create Referral screen is similar to the Patient Information screen, however, all pertinent information needs to be added to the EFR.

![](embedded-fragments-version-1-user-manual/091.png)

INCLUDES:

- Patient panel
  - *ICN \| Name \| Zip \| SSN \| DOB*
  - *OEF/OIF Indicator \| Iraq/Afghan Service \| Service Separation Date*
- Referral Details panel
  - *Referral Date \| Created By*
- Risk Category panel
  - This section initially is blank. The risk category is calculated by the presence of certain health factors. When the manual referral is saved the EFRA will calculate the Risk Category
- Veterans Affairs Medical Center panel
  - Facility Name \[Drop-down box\] \| Contact Name
  - Address 1 \| Contact Email
  - Address 2 \| Contact Phone
  - Address 3 \| Contact FAX
  - City
  - State
  - Zip/Postal
  - Country
- Primary Care Physician panel
  - Name \| Address 1
  - Phone \| Address 2
  - Email \| Address 3
  - FAX Number \| City
  - State
  - Zip/Postal
  - Country
- Health Factors panel \[All of the following are Check boxes unless otherwise stated\]
  - Fragments panel
    - Embedded Fragments Present \[Check box with Text box\]
    - No Embedded Fragments \[Check box\]
  - Injury Type panel
    - Bullet Injury
    - No Bullet Injury
    - Blast/Explosion Injury
    - No Blast/Explosion Injury
  - Blast Explosion Type panel
    - IED
    - RPG
    - Land Mine
    - Grenade
    - Enemy Fire
    - Friendly Fire
    - Unknown Type \[Check box with Text box\]
  - Fragments in Body panel
    - Fragments in Body
    - No Fragments in Body
    - Unknown if Fragments in Body
  - Radiography panel
    - Fragments in Radiograph
    - Not Documented on Radiograph
    - Unknown if Fragments on Radio Graph
  - Vehicle panel
    - In Vehicle
    - Not In Vehicle
  - Surgery panel
    - Fragments Removed in Surgery
    - Fragments Not Removed in Surgery
    - Unknown if Removed in Surgery
  - Laboratory panel
    - Fragments Sent to Lab
    - Fragments Not Sent to Lab
    - Unknown if Fragments Sent to Lab
  - Unable to Screen panel
    - Acute Illness \[Check box with Text box\]
    - Severe Cognitive Impairment \[Check box with Text Box\]
    - Refused Screening Tool
- Triage Referral panel
  - Accept \[Radio button\]
    - For Biomonitoring \[Check box\]
    - For Fragment Analysis \[Check box\]
  - Accepted – No Action Required \[Radio button\]
  - Ineligible \[Radio button\]
    - Ineligibility Reason \[Text box\]

| ![](embedded-fragments-version-1-user-manual/092.png) | Click \[Save\] to save the patient information and add them to the EFR.        |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/093.png) | Click \[Back\] to discard the changes and return to the Patient Lookup screen. |
| ![](embedded-fragments-version-1-user-manual/094.png) | The \[Add Contact\] button is greyed out and is not used on this screen.       |

# My Tasks tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## My Tasks Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to understand how the various tasks associated with EFRA are performed, it’s necessary to discuss the EFRA <span class="smallcaps">My Tasks</span> tab. EFRA uses the <span class="smallcaps">My Tasks</span> tab as a task-oriented viewer. Tasks available to you are shown on the left navigation panel, based on the role(s) you have been assigned. In many of the samples shown in this document, you will see all possible tasks shown as available, and all the tasks are listed in Table 5 below. On your user screen, you will also see all the tasks associated with that tab–– but not all of them may be available to you. Availability depends on your assigned role. Contact your supervisor or the TEFSC Admin Staff for questions about your roles.

![](embedded-fragments-version-1-user-manual/095.png)

<span id="_Ref273444807" class="anchor"></span>Figure 29 – My Tasks tab and Left Navigation Panel

When you “hover” your mouse pointer over a tab or task that is available to you, a web address ([URL](#glos_URL)) will appear at the bottom of your browser window, just above the Windows \[Start\] button. If the task is not available, no destination address will appear, indicating that you do not have access to that task.

![](embedded-fragments-version-1-user-manual/096.png)

<span id="_Ref265078527" class="anchor"></span>Figure 30 – Destination Address Shows Task Availability

| ![](embedded-fragments-version-1-user-manual/097.png) | Note: The [URL](#glos_URL) you see will be different from the one shown in Figure 30. |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|

| ![](embedded-fragments-version-1-user-manual/098.png) | Important: When you hover near a task item, a highlighting rectangle in lighter blue (similar to the one marking New in Figure 29 above) will appear around the task. In order to see or to select the link, however, you must click on the task text itself, not just the highlighting rectangle. |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](embedded-fragments-version-1-user-manual/099.png) | Note: Depending on your browser settings, the task text may or may not show underlining when you hover over it. If the task is not available, or if there is no actual task associated with the text, you will not see a destination displayed, as in Figure 31. |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](embedded-fragments-version-1-user-manual/100.png)

<span id="_Ref262742429" class="anchor"></span>Figure 31 – Task Not Available

| ![](embedded-fragments-version-1-user-manual/101.png) | Note: The tasks available in the <span class="smallcaps">LEFT NAVIGATION BAR</span> will only include those assigned to your role(s). See Table 4 – Tasks by Role for tasks available for each role. See Table 5 for a listing of all tasks. |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Error and Warning Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If required data elements are not entered on an EFRA data entry screen, or if formatting errors are detected, a popup error message like this one may display:

![](embedded-fragments-version-1-user-manual/102.png)

<span id="_Toc327881511" class="anchor"></span>Figure 32 – Message from webpage (data errors)

If you try to navigate away from a screen without saving or otherwise completing the screen, a popup error warning may display:

![](embedded-fragments-version-1-user-manual/103.png)

<span id="_Toc327881512" class="anchor"></span>Figure 33 – Navigating Away from Page

## Task Categories and Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists all tasks for all roles. For details, click on the internal link in the MORE INFO columns.

| Task Category        | Task                    | MORE INFO |     | Task Category              |              | Task             | MORE INFO |
|----------------------|-------------------------|-----------|-----|----------------------------|--------------|------------------|-----------|
| Referrals            |                         | 11        |     | Lab Orders                 |              |                  | 0         |
|                      | New                     | 11.1      |     |                            |              | New              | 15.1      |
|                      | Accepted – Open Cases   | 11.2      |     |                            |              | Awaiting Results | 15.2      |
|                      | Accepted – Closed Cases | 11.3      |     |                            |              | Voided           | 15.3      |
|                      | Ineligible              | 11.5      |     |                            |              | Closed           |           |
| Lab Kits             |                         | 13        |     | Lab Results                |              |                  | 16        |
|                      | New                     | 13.1      |     |                            |              | New              | 16.1      |
|                      | Tracking                | 13.2      |     |                            |              | In Process       | 16.2      |
|                      | Received                | 13.3      |     |                            |              | Accepted         | 0         |
|                      | Voided                  | 13.4      |     |                            |              | Voided           |           |
| Questionnaires/Forms |                         | 14        |     | Interpretation & Follow Up |              |                  | 17        |
|                      | New                     | 14.1      |     |                            |              | New              | 17.1      |
|                      | In Process              | 14.2      |     |                            |              | In Process       | 17.2      |
|                      | Completed               | 14.3      |     |                            |              | Interpreted      | 17.3      |
|                      |                         |           |     | Contact Logs               |              |                  | 17.3.1    |
|                      |                         |           |     |                            | All Contacts |                  | 17.5      |

## Follow-Up Event Reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you start work on an assigned record but do not finish work, or if you do not have needed information available, you may set a reminder for yourself. The next time you run the application, rather than seeing the Patients screen first, you will instead see these reminders displayed:

![](embedded-fragments-version-1-user-manual/104.png)

You may either…

1.  ![](embedded-fragments-version-1-user-manual/105.png) Click the \[Select\] button to choose the records needing attention and work on them, or…
2.  Set a “snooze” period for each such record. For each referral listed:
    - Select a snooze period from the (Select Period) drop-down list. Note that the \[Snooze\] button is inactive (grayed-out) until you select a snooze period.

![](embedded-fragments-version-1-user-manual/106.png)

- ![](embedded-fragments-version-1-user-manual/107.png) Click the \[Snooze\] button.
3.  Or, you can ignore the reminder by clicking on another tab.

| ![](embedded-fragments-version-1-user-manual/108.png) | Note: You can also see these records at any time by choosing <span class="smallcaps">My Tasks \> Referrals \> Accepted \> Follow Ups</span> (see 11.4 below). |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Reviewing/Editing a Referral Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you select a referral record, the referral information appears:

![](embedded-fragments-version-1-user-manual/109.png)

<span id="_Toc327881513" class="anchor"></span>Figure 34 – Referral Record (Part 1)

INCLUDES:

- Patient panel \[all pre-filled text\]
- *ICN \| Name\* \| SSN \| DOB\* Link to other records for this patient.*
- Referral Details panel \[all pre-filled text\]
- *Referral date \| Date Sent to TEFSC \| Reviewed Date \| Reviewed by*
- Risk Category panel
- *Risk Category text* \[pre-filled, read-only text box\]
- Veterans Affairs Medical Center panel
- *Facility Name \| Contact Name*
- *Address 1 \| 2 \| 3 \| Contact Email*
- *City \| Contact Phone*
- *State \| Contact Fax*
- *Zip/Postal*
- *Country*

![](embedded-fragments-version-1-user-manual/110.png)

<span id="_Toc327881514" class="anchor"></span>Figure 35 – Referral Record (Part 2)

INCLUDES:

- Primary Care Physician panel \[all pre-populated text boxes; may be changed\]
- Name \| Address 1
- Phone \| Address 2
- Email \| Address 3
- Health Factors panel \[all checkboxes except as noted\]
- Fragments panel
  - Embedded Fragments Present
  - No Embedded Fragments
- Injury Type panel
  - Bullet Injury
  - No Bullet Injury
  - Blast/Explosion Injury
  - No Blast/Explosion Injury
- Blast/Explosion Type panel
  - IED
  - RPG
  - Land Mine
  - Grenade
  - Enemy Fire
  - Friendly Fire
  - Unknown Type
  - Other
  - Other \[text box\]
- Fragments in Body panel
  - Fragments in Body
  - No Fragments in Body
  - Unknown if Fragments in Body
  - Radiography panel
  - Fragments on Radiograph
  - Not Documented on Radiograph
  - Unknown if Fragments on Radiograph
- Vehicle panel
  - In Vehicle
  - Not in Vehicle
- Surgery panel
  - Fragments Removed in Surgery
  - Fragments Not Removed in Surgery
  - Unknown if Removed in Surgery
- Laboratory panel
  - Fragments Sent to Lab
  - Fragments not Sent to Lab
  - Unknown if Fragments Sent to Lab
- Unable to Screen panel
  - Acute Illness
  - Severe Cognitive Impairment
  - Refused Screening
- Workflows panel \[all pre-filled text\]
  - Workflow ID \| Specimen Type \| Workflow Status \| Last Updated
  - ![](embedded-fragments-version-1-user-manual/111.png) \[Add Workflow\] button

When you have entered all available data, you may…

![](embedded-fragments-version-1-user-manual/112.png) Click the \[Save\] button to save the data you entered. A popup is displayed:

![](embedded-fragments-version-1-user-manual/113.png)

<span id="_Toc327881515" class="anchor"></span>Figure 36 – Save Successful Popup Message

![](embedded-fragments-version-1-user-manual/114.png) Click \[OK\] to dismiss the popup.

![](embedded-fragments-version-1-user-manual/115.png) Click the \[Back\] button to return to the list.

![](embedded-fragments-version-1-user-manual/116.png) Click the \[Add Contact\] button to add a new contact record.

# Reporting tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Formal reporting functionality is available in EFRA 4.0.

- Referral report

In addition, an internal report called the Kit Orders Report is available from the Lab Kits detail screen.

Other printed outputs (including notification letters to providers and patients) are included as part of the work flow. See the [Subject Index](#_Toc259014245) “reports” entries for pointers to such reports.

Finally, data exports are listed in [Section 8.3](#data-export). Unlike the standard reports, data exports generate excel spreadsheets formatted for use in client statistical software rather than human analysis.

### Lists and Reports Controls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the top of most CCR onscreen reports or lists are the various controls you can use. These controls are similar to those found in other [Portable Document Format (PDF)](#Glos_PDF) presentations, and are available for most reports or lists.

![](embedded-fragments-version-1-user-manual/117.png)

<span id="_Toc327881516" class="anchor"></span>Figure 37 – Report Controls

#### Page Controls

You can move from one page of the list to another by using the page controls:

| ![](embedded-fragments-version-1-user-manual/118.png) | ![](embedded-fragments-version-1-user-manual/119.png) | ![](embedded-fragments-version-1-user-manual/120.png) | ![](embedded-fragments-version-1-user-manual/121.png) | ![](embedded-fragments-version-1-user-manual/122.png) |
|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| *first record in list*                             | *previous record*                                  | *record number* of *the total number of records*   | *next record*                                      | *last record*                                      |

#### Zoom Control

You can change the zoom level of the onscreen list by using the zoom control:

| ![](embedded-fragments-version-1-user-manual/123.png) | ![](embedded-fragments-version-1-user-manual/124.png) |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|

#### Search for Text

You can search for text on the list by using the search box:

![](embedded-fragments-version-1-user-manual/125.png)

Enter your search text in the box provided, and then click the \[Find\] command icon. Click \[Next\] to see the next match.

#### Specify Format and Export

You can specify the format for an export from the list, using the Export control. You may choose to export to an Excel (spreadsheet) file or to an Acrobat (PDF) file:

| ![](embedded-fragments-version-1-user-manual/126.png) | ![](embedded-fragments-version-1-user-manual/127.png) |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|

![](embedded-fragments-version-1-user-manual/128.png) After selecting the format, click the \[Export\] command icon to the right of the drop-down list.

#### Refresh Control

![](embedded-fragments-version-1-user-manual/129.png) Click the \[Refresh\] command icon to refresh the list.

#### Print Control

![](embedded-fragments-version-1-user-manual/130.png) Click the \[Print\] command icon to print directly from the screen to your default printer.

## Referral report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is a summary of unique referrals initiated within the time period selected.

![](embedded-fragments-version-1-user-manual/131.png)

<span id="_Toc327881517" class="anchor"></span>Figure 38 – Referral Report Selection Criteria

Specify the inclusive time period you wish by entering the start and end dates in the text boxes provided.

![](embedded-fragments-version-1-user-manual/132.png) Click \[Run Report\] to create the report.

The notice “Report is being generated” may appear momentarily while the report is being prepared. The report will then appear on screen.

There are three parts (labeled as “pages”) for the report:

1.  Number of Referrals Received by VA Facility
2.  Number of Referrals by Risk Category
3.  Referrals by Status and Average Number of Days Between Referral and Triage

You can use the navigation controls at the top of the report to move from one part (“page”) of the report to another. These are essentially the same controls found on any [portable document format (PDF)](#Glos_PDF) page. You can also use the control to export the report to a format of your choice. See Section 8.1.1 above for details.

### Number of Referrals Received by VA Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Page 1 of the Referral Report lists the number of referrals received by each VA facility. The list is sorted by facility number.

![](embedded-fragments-version-1-user-manual/133.png)

<span id="_Toc327881518" class="anchor"></span>Figure 39 – Referral Report (Page 1)

### Number of Referrals by Risk Category

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Page 2 of the Referral Report lists the number of referrals by risk category. There are five risk categories.

1.  This screening tool indicates that the patient has had a fragment removed at surgery or has a documented retained fragment.
2.  This screening tool indicates that the patient has a high likelihood of having a retained fragment.
3.  This screening tool indicates that the veteran possibly has a retained fragment as a result of injuries sustained while serving in the area of conflict.
4.  This screening tool indicates that the veteran likely does not have a retained fragment as a result of injuries sustained while serving in the area of conflict.
5.  Unspecified.

![](embedded-fragments-version-1-user-manual/134.png)

<span id="_Toc327881519" class="anchor"></span>Figure 40 – Referral Report (Page 2)

### Referrals by Status and Average Number of Days between Referral and Triage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Page 3 of the Referral Report shows a summary of the referrals by status, and includes a table showing the average number of days between referral and triage.

![](embedded-fragments-version-1-user-manual/135.png)

<span id="_Toc327881520" class="anchor"></span>Figure 41 – Referral Report (Page 3)

## Data Export

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As previously explained, the data export function exports specific reports in a format compatible with client statistical software. Since the exports are not meant for human analysis, the individual exports will not be shown in this manual.

![](embedded-fragments-version-1-user-manual/136.png)

<span id="_Toc327881521" class="anchor"></span>Figure 42 – Data Exports

INCLUDES:

- Data Exports
  - Referrals
  - Bio Questionnaires
  - Fragment Forms
  - Bio Labs
  - Fragment Labs
  - Related Diagnoses
  - Contact Logs
  - Patients
  - VTA Data Extract
  - DoD Fragment Data
  - Related Lab Tests

# Administration tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Administration application allows the Admin Staff to view, edit, and sort user roles. The Admin Staff role is designed to be a global role that is not specific to any facility. For EFRA version 1.0, however, the Admin Staff is specific to each facility. The Admin Staff can view, edit, and manage users and user roles. Refer to Section 19.1.1 for more information

3.  <span id="_Ref261953068" class="anchor"></span>
4.  The EFR Processes

# EFR Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EFR processes include:

- Specimen Processes
- The Biomonitoring Process
- The Fragment Analysis Process

## The Triage Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patients being recommended as candidates for inclusion in the EFR may be referred by local [VA](#Glos_VA) Providers or identified by the [DoD](#Glos_DoD).

Patients in each of these populations are screened in [CPRS](#Glos_CPRS) to identify them as possible candidates for inclusion. Local [VA](#Glos_VA) providers use CPRS to screen candidates for referral to the EFR based on [clinical reminders](#Glos_ClinicalReminder) (batteries of questions posed to the patient during the patient encounter). Responses to these questions are captured in [health factors](#Glos_HealthFactor). Once the screening is complete and the patient is found to meet the criteria for referral, the patient's relevant referral data are sent to EFRA so that a final determination can be made.

The process of evaluating the patient’s record to make that determination and to identify what actions will be required by [TEFSC](#Glos_TEFSC) to begin collecting information relevant to the patient’s care, is known as [*triage*](#Glos_Triage). The goal of triage is to make a determination as to whether the patient is eligible for admission to the EFR, and what follow-up action is required. This triage process also helps ensure that there is a single unique record for each patient who is to be admitted to the Registry. Finally, triage is the method by which patients are either admitted to the Registry or deemed ineligible for the Registry.

The data are sent in referrals from [CPRS](#Glos_CPRS), and these referrals enter a queue in EFRA for review by the Nurse (see 4, User Roles). The Nurse uses EFRA to review new referrals and to triage these referrals, making a determination regarding acceptance into the Registry.

If the patient whose record is being triaged has data in the [Veteran Tracking Application (VTA)](#Glos_VTA) [data extract file](#Glos_VTA_DataExtract), the Nurse may view that information during triage and use it to facilitate the triage decision-making process. Once the record has been triaged, if the patient has data in the VTA data extract file and/or the [DoD](#Glos_DoD) [Embedded Metal Fragment Registry (EMFR)](#Glos_EMFR) [data extract file](#Glos_EMFR_DataExtract), the system will associate the information in those files with the patient’s EFR record.

After reviewing all the available information, the Nurse makes the preliminary triage decision and records it in EFRA.

The EFR TEFSC Provider and the EFR TEFSC Coordinator (see 4, User Roles) may also conduct the triage process.

See Figure 43 – Triage Process for a graphic representation of the triage process.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](embedded-fragments-version-1-user-manual/137.png)</p>
<p><span id="_Ref262720261" class="anchor"></span>Figure 43 – Triage Process</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The off-page connector ( ![](embedded-fragments-version-1-user-manual/138.png) ) in Figure 43 refers to Figure 66 – Specimen Processes.

## Screens and Navigation Hierarchy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are currently 60 sections used in EFRA. The section numbers and names are shown below. The navigational hierarchy is also indicated by indents within the table; for example, Section 1 provides access to Sections 2 and 3.

| Screen Number and Title           |                                                                 |                                                    |                                                                         |
|-----------------------------------|-----------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------------------------|
| <span class="smallcaps">1</span>  | <span class="smallcaps">Patient Lookup</span>                   |                                                    |                                                                         |
|                                   | <span class="smallcaps">2</span>                                |                                                    | <span class="smallcaps">Patient information</span>                      |
|                                   | <span class="smallcaps">3</span>                                |                                                    | <span class="smallcaps">Workflows</span>                                |
|                                   | <span class="smallcaps">4</span>                                |                                                    | <span class="smallcaps">DoD Fragment Data</span>                        |
|                                   | <span class="smallcaps">5</span>                                |                                                    | <span class="smallcaps">Related Diagnoses</span>                        |
|                                   | <span class="smallcaps">6</span>                                |                                                    | <span class="smallcaps">Lab tests</span>                                |
| <span class="smallcaps">7</span>  | <span class="smallcaps">Referral Queue</span>                   |                                                    |                                                                         |
|                                   | <span class="smallcaps">8</span>                                |                                                    | <span class="smallcaps">Referral Details (New)</span>                   |
|                                   | <span class="smallcaps">9</span>                                |                                                    | <span class="smallcaps">Referral Details (Accepted)</span>              |
|                                   | <span class="smallcaps">10</span>                               |                                                    | <span class="smallcaps">Referral Details (Closed)</span>                |
|                                   | <span class="smallcaps">11</span>                               |                                                    | <span class="smallcaps">Referral Details (Closed)</span>                |
|                                   | <span class="smallcaps">12</span>                               |                                                    | <span class="smallcaps">Referral Details (Ineligible)</span>            |
| <span class="smallcaps">13</span> | <span class="smallcaps">Lab Kit Queue (New)</span>              |                                                    |                                                                         |
|                                   | <span class="smallcaps">14</span>                               |                                                    | <span class="smallcaps">Lab Kit Details (New)</span>                    |
|                                   | <span class="smallcaps">15</span>                               |                                                    | <span class="smallcaps">Lab Kit Details (Tracking)</span>               |
|                                   | <span class="smallcaps">16</span>                               |                                                    | <span class="smallcaps">Lab Kit Details (Received)</span>               |
|                                   | <span class="smallcaps">17</span>                               |                                                    | <span class="smallcaps">Lab Kit Details (Voided)</span>                 |
| <span class="smallcaps">18</span> | <span class="smallcaps">Questionnaire/Forms Queue</span>        |                                                    |                                                                         |
|                                   | <span class="smallcaps">19</span>                               |                                                    | <span class="smallcaps">Questionnaire/Forms (New)</span>                |
|                                   | <span class="smallcaps">20</span>                               |                                                    | <span class="smallcaps">Questionnaire/Forms (In Process)</span>         |
|                                   | <span class="smallcaps">21</span>                               |                                                    | <span class="smallcaps">Questionnaire/Forms (Completed)</span>          |
| <span class="smallcaps">22</span> | <span class="smallcaps">Lab Orders Queue</span>                 |                                                    |                                                                         |
|                                   | <span class="smallcaps">23</span>                               |                                                    | <span class="smallcaps">Lab Orders (New)</span>                         |
|                                   | <span class="smallcaps">24</span>                               |                                                    | <span class="smallcaps">Lab orders (Awaiting Results)</span>            |
|                                   | <span class="smallcaps">25</span>                               |                                                    | <span class="smallcaps">Lab Orders (Voided)</span>                      |
|                                   | <span class="smallcaps">26</span>                               |                                                    | <span class="smallcaps">Lab Orders (Closed)</span>                      |
| <span class="smallcaps">27</span> | <span class="smallcaps">Lab Results Queue</span>                |                                                    |                                                                         |
|                                   | <span class="smallcaps">28</span>                               |                                                    | <span class="smallcaps">Lab Results (New)</span>                        |
|                                   | <span class="smallcaps">29</span>                               |                                                    | <span class="smallcaps">Lab Results (In Process)</span>                 |
|                                   | <span class="smallcaps">30</span>                               |                                                    | <span class="smallcaps">Lab Results (Accepted)</span>                   |
|                                   | <span class="smallcaps">31</span>                               |                                                    | <span class="smallcaps">Lab Results (Voided)</span>                     |
| <span class="smallcaps">32</span> | <span class="smallcaps">Interpretation & Follow Up Queue</span> |                                                    |                                                                         |
|                                   | <span class="smallcaps">33</span>                               |                                                    | <span class="smallcaps">Interpretation & Follow Up (New)</span>         |
|                                   | <span class="smallcaps">34</span>                               |                                                    | <span class="smallcaps">Interpretation & Follow Up (In Process)</span>  |
|                                   | <span class="smallcaps">35</span>                               |                                                    | <span class="smallcaps">Interpretation & Follow Up (Interpreted)</span> |
| <span class="smallcaps">36</span> | <span class="smallcaps">Contact Log Queue</span>                |                                                    |                                                                         |
|                                   | <span class="smallcaps">37</span>                               |                                                    | <span class="smallcaps">Contact Log Details</span>                      |
| <span class="smallcaps">38</span> | <span class="smallcaps">Patient Lookup</span>                   |                                                    |                                                                         |
|                                   | <span class="smallcaps">39</span>                               |                                                    | <span class="smallcaps">Patient Lookup Details</span>                   |
| <span class="smallcaps">40</span> | <span class="smallcaps">Reporting</span>                        |                                                    |                                                                         |
|                                   | <span class="smallcaps">41</span>                               |                                                    | <span class="smallcaps">Patient Lookup Details</span>                   |
| <span class="smallcaps">42</span> | <span class="smallcaps">Data Export</span>                      |                                                    |                                                                         |
|                                   | <span class="smallcaps">43</span>                               | <span class="smallcaps">Referrals</span>           |                                                                         |
|                                   | <span class="smallcaps">44</span>                               | <span class="smallcaps">Bio Questionnaires</span>  |                                                                         |
|                                   | <span class="smallcaps">45</span>                               | <span class="smallcaps">Fragment Forms</span>      |                                                                         |
|                                   | <span class="smallcaps">46</span>                               | <span class="smallcaps">Bio Labs</span>            |                                                                         |
|                                   | <span class="smallcaps">47</span>                               | <span class="smallcaps">Fragment Labs</span>       |                                                                         |
|                                   | <span class="smallcaps">48</span>                               | <span class="smallcaps">Relegated Diagnoses</span> |                                                                         |
|                                   | <span class="smallcaps">49</span>                               | <span class="smallcaps">Contact Logs</span>        |                                                                         |
|                                   | <span class="smallcaps">50</span>                               | <span class="smallcaps">Patients</span>            |                                                                         |
|                                   | <span class="smallcaps">51</span>                               | <span class="smallcaps">VTA Data Extract</span>    |                                                                         |
|                                   | <span class="smallcaps">52</span>                               | <span class="smallcaps">DoD Fragment Data</span>   |                                                                         |
|                                   | <span class="smallcaps">53</span>                               | <span class="smallcaps">Related Lab Tests</span>   |                                                                         |
| <span class="smallcaps">54</span> | <span class="smallcaps">Administration Queue</span>             |                                                    |                                                                         |
|                                   | <span class="smallcaps">55</span>                               |                                                    | <span class="smallcaps">Users</span>                                    |
|                                   | <span class="smallcaps">56</span>                               |                                                    | <span class="smallcaps">Role Matrix</span>                              |
|                                   | <span class="smallcaps">57</span>                               |                                                    | <span class="smallcaps">Reference Ranges</span>                         |
|                                   | <span class="smallcaps">58</span>                               |                                                    | <span class="smallcaps">Auto Triage</span>                              |
|                                   | <span class="smallcaps">59</span>                               |                                                    | <span class="smallcaps">DoD Fragment Data</span>                        |
| <span class="smallcaps">60</span> | <span class="smallcaps">Help</span>                             |                                                    |                                                                         |

# My Tasks \> Referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/139.png)A referral is an indication that the person referred *may* be eligible for inclusion in the EFR. A patient or Veteran may be referred for a variety of reasons, typically including the screening tool used in [CPRS](#Glos_CPRS).

| CATEGORY  | SUBCATEGORY  | DESCRIPTION                                                                                    | MORE INFO |
|-----------|--------------|------------------------------------------------------------------------------------------------|-----------|
| Referrals | New          | Patients who have only the pre-populated information from the [VistA](#Glos_VistA) data feed   | 11.1      |
|           | Accepted     | Patients who have been accepted into the EFR                                                   |           |
|           | Open Cases   | Patients who have been accepted, but whose EFR record is still being processed                 | 11.2      |
|           | Closed Cases | Patients who have been accepted, and whose EFR record has been completed                       | 11.3      |
|           | Ineligible   | Patients who were referred, but who have been deemed ineligible for inclusion in the Registry. | 11.5      |

## My Tasks \> Referrals \> New

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th>AVAILABILITY:</th>
<th>TEFSC Nurse</th>
<th>SCREEN NAME:</th>
<th>Referral Queue</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">ACCESS: To access this screen, select <span class="smallcaps">My Tasks &gt;</span> <span class="smallcaps">Referrals &gt; New</span></td>
</tr>
<tr class="even">
<td colspan="4"><p>PURPOSE: The system receives a list of referrals from the <a href="#Glos_VistA">VistA</a> system. A TEFSC Nurse uses this screen to see who is in the system and to select an applicable referral. The referral list can be filtered by Status (New, Accepted, Open Cases, Closed Cases, and Ineligible) or by Last Name.</p>
<p>Once the Nurse has found the referral of interest, the [Select] button can be used to pull up the referral details screen, as described in Section 11.1.3.</p></td>
</tr>
</tbody>
</table>

The Referral Queue screen displays patients who have been referred for possible inclusion in the Registry. Such a referral is typically as a result of the patient’s identification as a candidate based on responses to the [CPRS](#Glos_CPRS) screening tool.

![](embedded-fragments-version-1-user-manual/140.png)

<span id="_Toc327881523" class="anchor"></span>Figure 44 – Referral Queue

EFRA displays a list of records that are available to you. Your task is to look at the new referrals, and then to “triage” those referrals and ensure that there is a single unique record for each patient who is to be admitted to the Registry. This screen shows new patients brought into the system by the data feed from[[VistA](#Glos_VistA)](#Glos_VistA). On the screen, you see the basic “person identifiers” for the patients:

INCLUDES:

> All data elements are pre-populated text unless otherwise noted.

- Filter by Last Name \[textbox\]
  - \[Go\] button
  - \[Clear\] button
- *Ref \#:* The referral number, a unique personal identifier that is internal to EFRA—it’s easier to remember than the long Social Security Number (SSN).
- *Patient Name:* The patient’s last name followed by the first name.
- *Site \#:* The facility that referred the patient.
- *Referral Date:* The date the record was received from the [NDS](#gLOS_nds).
- *Status:* There are four possible status indicators for referrals. All referrals listed on this screen should be <span class="smallcaps">New</span>.
  - <span class="smallcaps">New</span>
  - <span class="smallcaps">\[Accepted\] Open Cases</span>
  - <span class="smallcaps">\[Accepted\] Closed Cases</span>
  - <span class="smallcaps">Ineligible</span>
- ![](embedded-fragments-version-1-user-manual/141.png) Click the \[Select\] button on the right of the row containing the record in order to view or edit the record. MORE INFORMATION: 11.1.3
- Paging: When more than one page of results is available, use the numbered links (1 <u>2</u> <u>3</u>…) at the bottom of the page to move forward or back.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/142.png)</th>
<th><p><strong>Important:</strong> There are two internal identifying numbers that you need to know about and distinguish between:</p>
<p>Ref # or Referral Number identifies a record of a patient who has been referred for consideration. This is pre-assigned by the system.</p>
<p>Workflow ID: <a href="#Glos_TEFSC">TEFSC</a> may set up workflows for Biomonitoring, Fragment Analysis, or Consultation per referral. Those cases are identified by Workflow ID. A Workflow ID is assigned if the patient referred is accepted into the Registry and a workflow is established (see <strong>Error! Reference source not found.</strong>).</p>
<p>When all potential duplicate records for a patient have been resolved, there should only be a single Ref # for any given individual. There may, however, be multiple Workflow IDs for that patient.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Sorting the List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default sort order for records displayed on this screen is the Ref \#, with the highest Ref \# (that is, the most recent) listed first. You can sort the list by clicking on any of the underlined column headings:

![](embedded-fragments-version-1-user-manual/143.png)

<span id="_Toc327881524" class="anchor"></span>Figure 45 – Sorting Listings

If you have a lengthy list, sorting may take a few seconds. During the sort, a JavaScript<sup>®</sup> message and a “counter” like this one may appear at the bottom of your browser window:

![](embedded-fragments-version-1-user-manual/144.png)

<span id="_Toc327881525" class="anchor"></span>Figure 46 – JavaScript Sort Message and Counter

### Filtering by Last Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can also filter the list by the patient’s last name, as shown in Figure 47. Enter the name you want in the Filter by Last Name: box and then click the \[Go\] button. The sample below shows the result of a search for patient(s) with a last name that includes “Six.”

![](embedded-fragments-version-1-user-manual/145.png)

<span id="_Ref257807921" class="anchor"></span>Figure 47 – Search Results

You can also clear the search results (thereby restoring the original list) by clicking the \[Clear\] button.

### My Tasks \> Referrals \> New \> Ref \# NNNN 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 33%" />
<col style="width: 12%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>AVAILABILITY:</th>
<th>TEFSC Nurse</th>
<th>SCREEN NAME:</th>
<th>Referral Details (New)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">ACCESS: To access this screen, click [Select] button at the right side of the row containing the patient’s name on the screen which lists new referrals.</td>
</tr>
<tr class="even">
<td colspan="4"><p>PURPOSE: A TEFSC Nurse reviews a patient’s case by looking at the <a href="#Glos_HealthFactor">health factors</a> that were created in <a href="#Glos_VistA">VistA</a> for that patient. The Nurse decides whether to accept or reject that patient from the Registry. If the patient is being accepted, the Nurse decides if a biomonitoring or fragment analysis workflow needs to be created for that patient. If there are errors in either health factors or the referral’s metadata, the Nurse can edit those items and save them.</p>
<p>A Nurse can go back to an already existing (saved) referral and review/change the patient’s metadata and health factors.</p>
<p>Additionally, the Nurse can create additional biomonitoring or fragment analysis workflows. This functionality is available for patients who require a follow up treatment.</p></td>
</tr>
</tbody>
</table>

After you select a record from the <span class="smallcaps">New Referrals</span> list, you will see the detail screen which shows all the information currently available about the selected patient.

| ![](embedded-fragments-version-1-user-manual/146.png) | Note: The screen for this task occupies a great deal of monitor width. You may have to scroll right and left as well as up and down when viewing or working on this screen. Some screen shots which follow do not show the banner, tabs, breadcrumbs, or the LEFT NAVIGATION BAR. Other screen shots may be divided in order to show all the contents. Finally, some screen displays shown below are in landscape format to provide greater width in this document. |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

When you select a patient record from the <span class="smallcaps">Referral \> New</span> list, the record for that referral is presented using several panels containing information about the patient and the referral. Using [CPRS](#Glos_CPRS) as your source, make all the entries that you can, and then do the referral triage. For information about how the information is obtained and organized in CPRS, see Sample CPRS Screen Shots.

#### My Tasks \> Referrals \> New \> Ref \# NNNN

![](embedded-fragments-version-1-user-manual/147.png)

<span id="_Toc327881527" class="anchor"></span>Figure 48 – Referral Details (New)

INCLUDES:

- *Patient panel*
  - *ICN \| Name \| SSN \| DOB*
  - *OEF/OIF Indicator \| Iraq/Afghan Service \| Service Separation Date*
- Referral Details panel
  - Pre-populated text:
    - *Referral Date \[when the patient was referred\]*
    - *Date Sent to [TEFSC](#Glos_TEFSC) \[when the record was sent to TEFSC\]*
    - *Reviewed Date\[date the record was triaged\]*
    - *Reviewed By\[name of individual who performed the record triage\]*
  - Risk Category panel pre-populated using [CPRS](#Glos_CPRS) information; calculated based on what health factors the referral has.

| ![](embedded-fragments-version-1-user-manual/148.png) |
|----------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc327881528" class="anchor"></span>Figure 49 – Risk Category Description

> Possible choices on the drop-down list:

- This screening tool indicates that the patient has a high likelihood of having a retained fragment
- This screening tool indicates that the patient has had a fragment removed at surgery or has a documented retained fragment
- This screening tool indicates that the Veteran likely does not have a retained fragment as a result of injuries sustained while serving in the area of conflict
- This screening tool indicates that the Veteran possibly has a retained fragment as a result of injuries sustained while serving in the area of conflict
- Veterans Affairs Medical Center panel \[medical center where the patient is currently being seen\]
  - Facility Name \[select from drop-down list; address, city, state ZIP and country fields are automatically populated within a few seconds after you select a name… but the entries can be changed if necessary.\]
  - Address 1, 2, 3
  - City \| State \| ZIP/Postal
  - Country
  - Contact Name
  - Contact Email
  - Contact Phone
  - Contact Fax
- Primary Care Physician panel \[all text boxes\]
  - Name
  - Phone
  - Email
  - Fax Number
  - Address 1,2,3
  - City \| State \| ZIP/Postal
  - Country
- Health Factors panel \[all checkboxes unless otherwise indicated\]
  - Fragments panel
    - Embedded Fragments Present
    - No Embedded Fragments
  - Injury Type panel
    - Bullet Injury
    - No Bullet Injury
    - Blast/Explosion Injury
    - No Blast/Explosion Injury
  - Blast/Explosion Type panel
    - IED
    - RPG
    - Land Mine
    - Grenade
    - Enemy Fire
    - Friendly Fire
    - Unknown Type
    - Other
      - Other Blast/Explosion type \[text box\]
  - Fragments in Body panel
    - Fragments in Body
    - No Fragments in Body
    - Unknown if Fragments in Body
  - Radiography panel
    - Fragments on Radiograph
    - Not Documented on Radiograph
    - Unknown if Fragments on Radiograph
  - Vehicle panel
    - In Vehicle
    - Not in Vehicle
  - Surgery panel
    - Fragments Removed in Surgery
    - Fragments Not Removed in Surgery
    - Unknown if Removed in Surgery
  - Laboratory panel
    - Fragments Sent to Lab
    - Fragments Not Sent to Lab
    - Unknown if Fragments Sent to Lab
  - Unable to Screen panel
    - Acute Illness
      - Acute Illness type \[text box\]
    - Severe Cognitive Impairment
      - Cognitive Impairment type \[text box\]
    - Refused Screening Tool
- \[View DoD EMFR Related Data\] button displays the VTA Patient Details.
- The EFRA displays whether or not the patient has a matching entry in the DoD data extract file and the date that data was received.
- Triage Referral panel

> Review the data entries you have made. When you have decided the disposition, check one of the primary radio buttons under Triage Referral to indicate whether your triage decision for this patient is to…

> ![](embedded-fragments-version-1-user-manual/149.png)

<span id="_Toc327881529" class="anchor"></span>Figure 50 – Triage Referral Options

- Accept the patient into the Registry. This creates a “workflow” in the system, meaning that some action must be taken and followed. Selecting the Accept option will make the three “For” choices available. You may check one, two or all three. *If* you select Accept, one or more of the following choices *must* also be checked:
  - For Biomonitoring
  - For Fragment Analysis
  - For Consultation
- Accepted – No Action Required. This triage status means that the patient is included in the Registry without any follow up activity (*e.g.*, biomonitoring, fragment analysis, clinical consultation). Consequently, no workflow is involved and, essentially, these records just sit in the Registry. In the future, Biomonitoring, Fragment Analysis, or a Clinical Consultation may be performed for the patient. Also, the EFR may collect lab test results and ICD-9 codes of interest from the patient’s facility (this functionality is expected in Build 2).
- Ineligible
  - Ineligibility Reason (text entry). If Ineligible is selected, a reason for the patient’s ineligibility *must* be entered. This is a free-text field.

![](embedded-fragments-version-1-user-manual/150.png) After you click \[OK\] at the bottom of the screen, and assuming the save is successful, you will see a popup indicating a successful save:

![](embedded-fragments-version-1-user-manual/151.png)

<span id="_Toc327881530" class="anchor"></span>Figure 51 – Save Successful Popup

Click \[OK\] to dismiss the popup.

The Triage Referral panel is replaced by either the Workflows panel display or the Triage Status panel display.

If you selected one or more of the three Accept for choices, you see the Workflows panel display. If you checked more than one Accept for choice, all will show up on the workflow display. Note the Workflow ID which has now been assigned in each case.

| Accept for Biomonitoring                                                                            | Accept for Fragment Analysis                                                                        |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/152.png)  | ![](embedded-fragments-version-1-user-manual/153.png) |
| Accept for Consultation                                                                             |                                                                                                     |
| ![](embedded-fragments-version-1-user-manual/154.png) |                                                                                                     |

<span id="_Toc327881531" class="anchor"></span>Figure 52 – Triage - “Accept for…” Workflow Displays

If you selected Accepted – No Action Required, you see the Accepted – No Action Required display.

| Accepted – No Action Required                                                                         |
|-------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/155.png) |

<span id="_Toc327881532" class="anchor"></span>Figure 53 – Triage - Accepted - No Action Required Display

If you selected Ineligible, then that display appears.

| Ineligible                                          |
|-----------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/156.png) |

<span id="_Toc327881533" class="anchor"></span>Figure 54 – Triage - Ineligible Status Display

#### VTA Patient Details

If a referred patient has a matching entry in the VTA extract file, the EFRA will display the \[View DoD EMFR Related Data\] button to view the VTA data extract data. Matches are performed automatically and the contained data on the VTA Extract screen is display only.

![](embedded-fragments-version-1-user-manual/157.png)

<span id="_Toc327881534" class="anchor"></span>Figure 55 – VTA Extract Patient Information

INCLUDES:

- VTA Patient Information Details panel
  - *SSN*
  - *Patient ICN*
  - *Patient Name*
  - *Street Address*
  - *City*
  - *State*
  - *Zip/Postal Code*
  - *Home Phone*
  - *Work Phone*
  - *OEF/OIF Indicator*
  - *Date of Birth*
  - *Date of Death*
  - *Gender*
  - *Service Branch Code*
- Case Definition Details panel
  - *ICD9 Code \| Description*
  - *Soap Note Keywords*

| ![](embedded-fragments-version-1-user-manual/158.png) | Click \[Back\] to return to the patient referral record. |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------|

#### Adding a Workflow

If you have chosen one, but not all, of the Accept options, you can add another workflow if desired; select another workflow from the drop-down list in the Workflows panel:

![](embedded-fragments-version-1-user-manual/159.png)

<span id="_Toc327881535" class="anchor"></span>Figure 56 – Adding a Workflow

> ![](embedded-fragments-version-1-user-manual/160.png) After you make your selection, click \[Add Workflow\]. The Workflows panel redisplays:

![](embedded-fragments-version-1-user-manual/161.png)

<span id="_Toc327881536" class="anchor"></span>Figure 57 – Added Workflow Display

> This process may be done during the initial triage review, or later (after the record has been saved).

> Clear Triage panel

> ![](embedded-fragments-version-1-user-manual/162.png) If you select Accepted – No Action Required or Ineligible, you can use the \[Clear Triage\] button to reverse the choice. The screen redisplays and again presents the Triage Referral panel. You cannot use this option, however, if you have already selected one of the Accept choices.

#### Adding Contact Information

![](embedded-fragments-version-1-user-manual/163.png)

<span id="_Toc327881537" class="anchor"></span>Figure 58 – Add Contact Button

![](embedded-fragments-version-1-user-manual/164.png)

![](embedded-fragments-version-1-user-manual/165.png) You can also add a contact name and other information, independent of the triage decision or other data you record. Click the \[Add Contact\] button at the bottom of the screen. MORE INFORMATION: 17.3.1 below

#### Saving the Triage

When you have recorded the referral triage decision (and ineligibility reason, if applicable) you can…

![](embedded-fragments-version-1-user-manual/166.png) Click the \[Cancel\] button to discard the changes you have made and return to <span class="smallcaps">My Tasks \> Referrals \> New</span>.

![](embedded-fragments-version-1-user-manual/167.png) Click the \[OK\] button to save the record. When you click \[OK\], and assuming the save is successful, you will see a popup indicating this:

![](embedded-fragments-version-1-user-manual/168.png)

<span id="_Toc327881538" class="anchor"></span>Figure 59 – Save Successful Popup

Click \[OK\] to dismiss the popup. The record is saved and you may safely leave the screen.

Use the LEFT NAVIGATION BAR to choose your next task.

#### Handling Duplicate Referrals

From time to time, you may run across duplicate referrals. These are records which come into your task queue and which are for the same person. Such records may be caused by a variety of situations. For example, perhaps the patient visited two different facilities in rapid succession and a referral was generated at each facility. Regardless of the reason, such duplicates must be resolved, because each patient admitted to the Registry must have a single referral record.

Please see the two-part illustration below.

![](embedded-fragments-version-1-user-manual/169.png)

<span id="_Toc327881539" class="anchor"></span>Figure 60 – Duplicate Records

Note the warning banner at the top of the form, advising you that this is a duplicate record.

![](embedded-fragments-version-1-user-manual/170.png)

<span id="_Ref261959260" class="anchor"></span>Figure 61 – Duplicate Record Warning Banner

The duplicate record is automatically marked as Ineligible. However, it can be changed to eligible and edited. Any edits made to a duplicate record are for that record only and will not affect the previous referral. A link is provided to that previous record (<u>Go to Previously Triaged Referral</u>) as shown in Figure 61.

#### Duplicate Health Factor

Certain referrals may contain multiple health factors of the same type indicated for a single referral, as received by the EFR application from the source system. When you encounter this issue, the system will display a warning message.

![](embedded-fragments-version-1-user-manual/171.png)

To continue editing the record, click \[Ok\]; the record will be editable. Contact the Harris Helpdesk and resolve the duplicate on the database side.

## My Tasks \> Referrals \> \[Accepted\] Open Referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                                                  | See Table 4 – Tasks by Role | SCREEN NAME: | Referral Queue |
|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------|----------------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \></span> <span class="smallcaps">Referrals \> \[Accepted\] Open</span> |                             |              |                |

OPEN Referrals are those which have been accepted into the Registry and for which a workflow (*i.e.*, Biomonitoring, Fragment Analysis, or Consultation) has been recommended, but for which the workflow is not yet complete.

The application will display a list of records that are available to you. This provides a method for you to check on progress of Open Cases records, or to provide updates if needed. On this screen, you see the usual basic person identifiers for the patients.

Records are listed in the same manner as for <span class="smallcaps">New</span> records.

![](embedded-fragments-version-1-user-manual/172.png)

<span id="_Toc327881541" class="anchor"></span>Figure 62 – \[Accepted\] Open Referrals

![](embedded-fragments-version-1-user-manual/173.png) Select a record to look at or work on by clicking the \[Select\] button at the right of the row containing the record. The process of editing the record is the same as shown under <span class="smallcaps">My Tasks \> Referrals \> New</span>, starting at 11.1.3 above.

## My Tasks \> Referrals \> \[Accepted\] Closed Referrals 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                                                    | See Table 4 – Tasks by Role | SCREEN NAME: | Referral Queue |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------|----------------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \></span> <span class="smallcaps">Referrals \> \[Accepted\] Closed</span> |                             |              |                |

CLOSED Referrals are those which have been triaged and for which…

- No action has been recommended, or…
- Any recommended [workflow](#Glos_workflow) has been completed

A referral is considered <span class="smallcaps">CLOSED</span> when all workflows associated with that referral have been completed. If the patient is accepted into the Registry and triaged as <span class="smallcaps">Accepted/No Action</span>, that patient record would appear as <span class="smallcaps">CLOSED</span> immediately because there is no workflow involved.

If you don’t see this screen, select the <span class="smallcaps">Referrals \> \[Accepted\] CLOSED</span> task. The application will display a list of records that are available to you. This provides a method for you to check on progress of Closed Cases records, or to provide updates if needed. On this screen, you see the usual basic person identifiers for the patients.

Records are listed in the same manner as for <span class="smallcaps">New</span> records (see Figure 63).

![](embedded-fragments-version-1-user-manual/174.png)

<span id="_Ref269824377" class="anchor"></span>Figure 63 – \[Accepted\] Closed Referrals

It may be necessary to later view these records, or to change data previously entered in light of new information that has become available. Only minimal demographic data and the triage decision are stored in the database.

![](embedded-fragments-version-1-user-manual/175.png) Select a record to look at or work on by clicking the \[Select\] button at the right of the row containing the record. The process of editing the record is the same as shown under <span class="smallcaps">My Tasks \> Referrals \> New</span>, starting at 11.1.3 above.

## My Tasks \> Referrals \> \[Accepted\] Follow Ups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                                                        | See Table 4 – Tasks by Role | SCREEN NAME: | Referral Queue |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------|----------------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \></span> <span class="smallcaps">Referrals \> \[Accepted\] Follow Ups</span> |                             |              |                |

FOLLOW UPS are those which have been triaged and for which a reminder has been created (see 7.4 above).

If you don’t see this screen, select the <span class="smallcaps">Referrals \> \[Accepted\] Follow Ups</span> task. The application will display a list of records that are available to you. This provides a method for you to review records tagged for follow-up, or to provide updates if needed. On this screen, you see the usual basic person identifiers for the patients.

Records are listed in the same manner as for <span class="smallcaps">New</span> records (see Figure 63).

![](embedded-fragments-version-1-user-manual/176.png)

<span id="_Toc327881543" class="anchor"></span>Figure 64 – \[Accepted\] Follow Ups

It may be necessary to later view these records, or to change data previously entered in light of new information that has become available.

![](embedded-fragments-version-1-user-manual/177.png) Select a record to look at or work on by clicking the \[Select\] button at the right of the row containing the record. The process of editing the record is the same as shown under <span class="smallcaps">My Tasks \> Referrals \> New</span>, starting at 11.1.3 above.

| ![](embedded-fragments-version-1-user-manual/178.png) | Note: You may also see these records at startup, when the Follow Up Event Reminders screen displays (see 7.4 above). |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|

## My Tasks \> Referrals \> Ineligible

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                                           | See Table 4 – Tasks by Role | SCREEN NAME: | Referral Queue |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------|----------------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \></span> <span class="smallcaps">Referrals \> Ineligible</span> |                             |              |                |

These are records which have been through the triage process and marked as Ineligible. The system retains the referral even if it is deemed ineligible. The referral details cannot be edited after it is deemed ineligible; you can, however, clear the triage— which makes the referral no longer ineligible, and returns it to the <span class="smallcaps">Referral \> New</span> queue.

| ![](embedded-fragments-version-1-user-manual/179.png) | Important: Changing status from Ineligible to another status should normally be done only in the event new evidence of fragments is found. |
|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|

![](embedded-fragments-version-1-user-manual/180.png)

<span id="_Toc327881544" class="anchor"></span>Figure 65 – My Tasks \> Referrals \> Ineligible

If you don’t see this screen, select the <span class="smallcaps">Referrals \> Ineligible</span> task. The application will display a list of records that are available to you. This provides a method for you to view Ineligible records, or to provide updates if needed. On this screen, you see the usual basic person identifiers for the patients.

Records are listed in the same manner as for <span class="smallcaps">New</span> records.

![](embedded-fragments-version-1-user-manual/181.png) Select a record to look at or work on by clicking the \[Select\] button at the right of the row containing the record. The process of editing the record is the same as shown under <span class="smallcaps">My Tasks \> Referrals \> New</span>, starting at 11.1.3 above.

5.  
6.  <span id="_Toc327881397" class="anchor"></span>Workflow Processes

# # Workflow Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Specimen Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the triage process, a referred patient may be accepted into the Registry for a number of purposes, including for Biological Monitoring and/or for Fragment Analysis, each of which involve examination of specimens. Although the tests for these two types of follow up are different, the basic process is the same.

The patient may be asked to gather a specimen (*e.g.,* urine), a blood sample may be drawn, or fragments may be removed from the patient's body. Any or all of these samples may then be tested for the presence and/or level of various substances.

See Figure 66 – Specimen Processes for a graphic representation of the common processes for specimens.

For discussions of the workflows, see:

- The Biomonitoring Process: 12.2 below
- The Fragment Analysis Process: 12.3 below

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](embedded-fragments-version-1-user-manual/182.png)</p>
<p><span id="_Ref262712718" class="anchor"></span>Figure 66 – Specimen Processes</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Off-page connectors in Figure 66 refer to:

| ![](embedded-fragments-version-1-user-manual/183.png) | Figure 67 – Biomonitoring Process | ![](embedded-fragments-version-1-user-manual/184.png) | Figure 68 – Fragment Analysis Process |
|-----------------------------------------------------|-----------------------------------|-----------------------------------------------------|---------------------------------------|

## The Biomonitoring Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Biomonitoring is one of the workflows which may be initiated based on.

Either the [VA](#Glos_VA) Provider may request a biomonitoring lab kit, or the TEFSC Admin Staff may initiate the process.

- TEFSC Admin Staff:
  - Opens Specimen Transaction
  - Notifies [Therapak](#Glos_Therapak) (vendor) to ship biomonitoring kit(s)
  - Updates the tracking data
- EFRA:
  - Accesses data
  - Tracks receipt
  - Records results
- Therapak:
  - Sends specimen kit, along with instructions and questionnaire, to the [VA](#Glos_VA) requestor
- Patient:
  - Collects a 24-hour urine specimen and completes questionnaire
  - Sends the sample and completed questionnaire to the Home VAMC
- Home VAMC Lab:
  - Sends specimen lot to [BVAMC](#Glos_BVAMC) Lab
  - Notifies [TEFSC](#Glos_TEFSC) by fax that specimen has been sent (and provides tracking number)
- TEFSC Admin Staff:
  - Updates tracking data
- EFRA:
  - Accesses data
  - Tracks receipt
  - Records results
- [BVAMC](#Glos_BVAMC) Lab:
  - Receives specimen
  - Processes specimen per BVAMC SOP

See Figure 67 – Biomonitoring Process for a graphic representation of the process.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](embedded-fragments-version-1-user-manual/185.png)</p>
<p><span id="_Ref261964453" class="anchor"></span>Figure 67 – Biomonitoring Process</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## The Fragment Analysis Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fragment Analysis may be initiated based on the EFR Process. The [VA](#Glos_VA) Provider may request a fragment analysis lab kit, or the TEFSC Admin Staff may initiate the process. See Figure 68 – Fragment Analysis Process for a graphic representation of the fragment analysis process. Explanatory text continues immediately following the figure.

- TEFSC Admin Staff initiates fragment analysis, or [VA](#Glos_VA) Provider requests fragment analysis kit
- TEFSC Admin Staff:
  - Opens fragment transaction
  - Notifies [Therapak](#Glos_Therapak) to ship kit
  - Updates tracking data
- Therapak sends to [VA](#Glos_VA) requestor:
  - Fragment collection kit
  - Instructions
  - Checklist
- Requesting VAMC:
  - Removes fragments
  - Prepares fragments for shipment
  - Sends fragment(s) and completed checklist to [TEFSC](#Glos_TEFSC) Lab
- TEFSC Admin Staff:
  - Logs sample
  - Pulls questionnaire
  - Assigns ID \#
  - Updates tracking data
  - Sends fragments to AFIP
- AFIP:
  - Receives fragments
  - Processes per AFIP SOP
- Whenever [TEFSC](#Glos_TEFSC) tracking data is updated, EFRA:
  - Accesses data
  - Tracks receipt
  - Records results
- See Figure 68 – Fragment Analysis Process for a graphic representation of the process.

![](embedded-fragments-version-1-user-manual/186.png)

<span id="_Ref262656579" class="anchor"></span>Figure 68 – Fragment Analysis Process

# My Tasks \> Lab Kits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once patients are accepted into EFR and identified for biomonitoring or fragment analysis, one or more specimen collection kits will be required. For biomonitoring, the local VAMC will supply the patient with a specimen collection kit, while for fragment analysis the VAMC will use a fragment collection kit to gather fragments from the patient’s body. These two types of collection kits are usually generically referred to as “lab kits.” Oftentimes, the local VAMC stockpiles kits that are used to supply the patient. Some VAMCs, however, do not stock lab kits. EFRA provides the TEFSC Administrator the ability to order kits, either as replacements for kits used from stock or, where stocks are not maintained, to fulfill any orders for patient specimen collections. An order can also be placed to provide a kit for an individual patient or bulk orders may be placed for groups of patients sorted by receiving facility. These orders are not tracked in EFRA.

## My Tasks \> Lab Kits \> New

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 33%" />
<col style="width: 12%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>AVAILABILITY:</th>
<th>EFR TEFSC Administrator</th>
<th>SCREEN NAME:</th>
<th>Lab Kit Queue (New)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">ACCESS: To access this screen, select <span class="smallcaps">My Tasks &gt; Lab Kits &gt; New</span></td>
</tr>
<tr class="even">
<td colspan="4"><p>PURPOSE: Whenever the nurse creates a Biomonitoring or Fragment workflow on the referral screen, a blank lab order is being created. All those blank lab orders represent a patient who needs to be provided with a urine sample or fragment kit.</p>
<p>The purpose of Kit ordering is to order those kits from a company called <a href="#Glos_Therapak">Therapak</a>, provide the patient with the kits and track proper receipt of the kit at the laboratory.</p>
<p>This Lab Kit Queue represents a list of all lab kits which are in stock or which may need to be ordered, grouped by Institution.</p></td>
</tr>
</tbody>
</table>

This screen shows the number of sample kits needed at various hospitals and other facilities, as well as the names of the patients for whom the kits are to be ordered. You can sort the list by any of the underlined headings; see 11.1.1 for sorting information. Note that the requirements are initially sorted by Institution Name, and then by the Kit Type (Fragment Analysis or Biological Monitoring). If there are no patients found that require specimen collection kits to be ordered, that fact is shown on screen.

![](embedded-fragments-version-1-user-manual/187.png)<span id="_Ref265589615" class="anchor"></span>

Figure 69 – My Tasks \> Lab Kits \> New

### Lab Kits Required Report (Kit Orders Report)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can get a printout of the list (the “Kit Orders Report”). Here are the steps for using this report to facilitate the process of determining which sites need kits ordered from Therapak versus using their own stock, and recording this information in EFRA.

1\. Access the <span class="smallcaps">My Tasks \> Lab Kits \> New</span> screen (Figure 70):

![](embedded-fragments-version-1-user-manual/188.png)

<span id="_Ref273532645" class="anchor"></span>Figure 70 – My Tasks \> Lab Kits \> New (Report)

2\. ![](embedded-fragments-version-1-user-manual/189.png) Click the \[Print Lab Kits Required\] button to generate the report and display it on screen (Figure 71):

![](embedded-fragments-version-1-user-manual/190.png)

<span id="_Ref265594007" class="anchor"></span>Figure 71 – Lab Kits Required Report

3.  Use this printed report as your work list.
4.  Manually mark the report accordingly in the Site Contacted or Contacted By Site columns.
5.  In EFRA, return to the <span class="smallcaps">Lab Kits/New</span> screen.

![](embedded-fragments-version-1-user-manual/191.png)

<span id="_Toc327881551" class="anchor"></span>Figure 72 – Lab Kits Required Report

6.  For each facility you contacted and marked on the printed report, click the \[Select\] button.
7.  The Kit Orders details screen will display for the facility you selected.

![](embedded-fragments-version-1-user-manual/192.png)

<span id="_Toc327881552" class="anchor"></span>Figure 73 – Lab Kit Orders for Selected Facility

8.  Mark the appropriate check box (Site Contacted or Contacted by Site) to record your action in EFRA. Click \[Save\] to record all of your changes.

EFRA is now aware of which facilities/patients had kits ordered and which facilities/patients used stock from the facility.

### View or Edit a New Lab Kit Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Returning to the <span class="smallcaps">My Tasks \> Lab Kits \> New</span> screen (see

Figure 69 above).

![](embedded-fragments-version-1-user-manual/193.png)

<span id="_Toc327881553" class="anchor"></span>Figure 74 – My Tasks \> Lab Kits \> New (Institution Listing)

![](embedded-fragments-version-1-user-manual/194.png) To view or edit any of the <span class="smallcaps">New</span> records, click the \[Select\] button at the right of the row which identifies the institution for which you wish to see or edit information.

When an institution is selected from the Lab Kit Queue (New) screen (

Figure 69, above), the detailed record of the specified type of kits needed for that institution is displayed.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 33%" />
<col style="width: 12%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>AVAILABILITY:</th>
<th>EFR TEFSC Administrator</th>
<th>SCREEN NAME:</th>
<th>Lab Kit Details (New)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">ACCESS: To access this screen, select an institution from the list displayed at <span class="smallcaps">My Tasks &gt; Lab Kits &gt; New</span></td>
</tr>
<tr class="even">
<td colspan="4"><p>PURPOSE: This screen is shown after you select a particular institution (hospital) for kit tracking. The screen shows all patients that need a kit, either for biomonitoring or fragment analysis.</p>
<p>You will need to contact the hospital and ask how many kits they already have in stock. After you have determined the number of kits already available, you can order the remainder from <a href="#Glos_Therapak">Therapak</a> and mark those items off on this screen, marking it as “used stock” (Used Stock checkbox) or “ordered” (Order Kit checkbox).</p>
<p>In addition to marking the kit, you can make changes in the kit ordering data (for example, if a contact person changed or their address information is different).</p></td>
</tr>
</tbody>
</table>

![](embedded-fragments-version-1-user-manual/195.png)

<span id="_Toc327881554" class="anchor"></span>Figure 75 – View/Edit Lab Kit Records (Biomonitoring)

![](embedded-fragments-version-1-user-manual/196.png)

<span id="_Toc327881555" class="anchor"></span>Figure 76 – View/Edit Lab Kit Records (Fragment Analysis)

You can directly edit any of the institution records on this screen. On this screen, you may indicate that a stock kit was used for a patient (Used Stock checkbox), or that a kit is to be ordered (Order Kit checkbox). You may also add or edit information. To see additional records (if any) use the page number links at the bottom of the list.

INCLUDES:

- For each record \[all text boxes unless otherwise noted\]:
  - Used Stock \[checkbox\]
  - Order Kit \[checkbox\]
  - *Workflow ID \[pre-populated text\]*
  - *Patient (last name, first name) \[pre-populated text\]*
  - Order Date
  - VAMC Contact
  - VAMC Contact Phone \#
  - Address Line 1 \| 2 \| 3
  - City
  - State
  - ZIP
  - \[ZIP\] +4
  - Country

When you have finished editing or ordering…

![](embedded-fragments-version-1-user-manual/197.png) Click the \[Save\] button to save any updates and return to the <span class="smallcaps">New</span> list, or…

![](embedded-fragments-version-1-user-manual/198.png) Click the \[Cancel\] button to exit the screen without saving the order and return to the <span class="smallcaps">New</span> list.

## My Tasks \> Lab Kits \> Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](embedded-fragments-version-1-user-manual/199.png) | <span id="LabKitQueueNotNew" class="anchor"></span>Note: There are three possible Lab Kit statuses that are “not new.” They all use the Lab Kit Queue (Not New) screen for list displays and the Lab Kit Details (Not New) for details. The status is shown in the Status column on the screen. |     |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Lab Kits whose status is…                                                                                            | Are those which…                                                                                                                                                                                                                                                                                    |     |
| Tracking                                                                                                             | are awaiting arrival at the Baltimore laboratory.                                                                                                                                                                                                                                                   |     |
| Received                                                                                                             | have been received already at the Baltimore laboratory.                                                                                                                                                                                                                                             |     |
| Voided                                                                                                               | have been lost, or are no longer applicable for other reasons.                                                                                                                                                                                                                                      |     |

### Lab Kits \> Tracking Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 33%" />
<col style="width: 12%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>AVAILABILITY:</th>
<th>EFR TEFSC Administrator</th>
<th>SCREEN NAME:</th>
<th>Lab Kit Queue (Not New) (see <a href="#LabKitQueueNotNew">Note</a>)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">ACCESS: To access this screen, select <span class="smallcaps">My Tasks &gt; Lab Kits &gt; Tracking</span></td>
</tr>
<tr class="even">
<td colspan="4"><p>PURPOSE: This screen is shown after you select a particular institution (hospital) for kit tracking. The screen shows all patients that need a kit, either for biomonitoring or fragment analysis.</p>
<p>You will need to contact the hospital and ask how many kits they already have in stock. After you have determined the number of kits already available, you can order the remainder from <a href="#Glos_Therapak">Therapak</a> and mark those items off on this screen, marking it as “ordered” or as “used stock.”</p>
<p>In addition to marking the kit, you can make changes in the kit ordering meta data (for example, if a contact person changed or their address information is different).</p></td>
</tr>
</tbody>
</table>

<span class="smallcaps">My Tasks \> Lab Kits \> Tracking</span> shows the kits which have been ordered and which are being tracked:

![](embedded-fragments-version-1-user-manual/200.png)

<span id="_Toc327881556" class="anchor"></span>Figure 77 – My Tasks \> Lab Kits \> Tracking Queue

INCLUDES:

All are read-only, pre-populated text except \[Select\] button.

- *Workflow ID*
- *Patient Name*
- *Site \#*
- *Sending Facility*
- *City*
- *Contact Person*
- *Kit Type*
- *Date Contacted*
- \[Select\] Button

To see additional records (if any) use the page number links at the bottom of the list.

![](embedded-fragments-version-1-user-manual/201.png) To view or edit a record, click the \[Select\] button at the right of the row which displays the workflow record.

### View or Edit a Tracking Lab Kit Record 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 33%" />
<col style="width: 12%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>AVAILABILITY:</th>
<th>EFR TEFSC Administrator</th>
<th>SCREEN NAME:</th>
<th>Lab Kit Details (Not New) (see <a href="#LabKitQueueNotNew">Note</a>)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">ACCESS: To access this screen, select a record from the list displayed at <span class="smallcaps">My Tasks &gt; Lab Kits &gt; Tracking</span></td>
</tr>
<tr class="even">
<td colspan="4"><p>PURPOSE: This screen is shown after you select a specific Workflow ID record.</p>
<p>In addition to marking the kit, you can make changes in the kit ordering data (for example, if a contact person changed or their address information is different).</p></td>
</tr>
</tbody>
</table>

When a specific workflow ID is selected, the record displays:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](embedded-fragments-version-1-user-manual/202.png)</p>
<p><span id="_Toc327881557" class="anchor"></span>Figure 78 – My Tasks &gt; Lab Kits &gt; Ordered &gt; Workflow ID NNNN</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

INCLUDES:

- *Kit Order Details* panel \[all text boxes unless otherwise noted\]
  - *Workflow ID \[prefilled text\]*
  - *Patient Name \[prefilled text\]*
  - Date Contacted \[mm/dd/yyyy\]
  - *TEFSC Representative \[prefilled text\]*
  - VAMC Contact
  - Address Part 1,2,3
  - City
  - State
  - ZIP
  - Country
  - Telephone#
  - *Kit Type \[prefilled text\]*
- Returned Kit Details panel \[all text boxes unless otherwise noted\]
  - *VAMC Facility \[prefilled text\]*
  - VAMC Contact
  - Courier Tracking \#
  - Kit Sent by VA Date
  - Kit Received Date
  - Questionnaire Received panel
    - Yes No radio buttons
  - Reason Tracking Transaction Closed \[drop-down list\]

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/203.png)</th>
<th><ul>
<li><blockquote>
<p>Kit Lost</p>
</blockquote></li>
<li><blockquote>
<p>Patient Refusal</p>
</blockquote></li>
<li><blockquote>
<p>Other</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Comments

When you have finished editing or reviewing the record…

![](embedded-fragments-version-1-user-manual/204.png) Click \[Save\] to save the record and return to the list, or…

![](embedded-fragments-version-1-user-manual/205.png) Click \[Receive\] to indicate that the kit has been received, or…

![](embedded-fragments-version-1-user-manual/206.png) Click \[Void\] to indicate that the kit has been lost, or the order is no longer applicable for other reasons.

![](embedded-fragments-version-1-user-manual/207.png) Click \[Cancel\] to abandon any changes made and return to the list.

## My Tasks \> Lab Kits \> Received 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a kit has been ordered, the record for that kit is marked as <span class="smallcaps">Tracking.</span> The record will show up in the <span class="smallcaps">Lab Kits \> Tracking</span> queue. When the kit is actually received in the lab, it should be marked as received.

### Lab Kits Received Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                                                                       | EFR TEFSC Administrator | SCREEN NAME: | Lab Kit Queue (Not New) (see [Note](#LabKitQueueNotNew)) |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------|----------------------------------------------------------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \> Lab Kits \> Received</span>                                                               |                         |              |                                                          |
| PURPOSE: This screen lists kits which have been received at the Baltimore laboratory. You can use this screen to review the kits and select one for further detail. |                         |              |                                                          |

<span class="smallcaps">My Tasks \> Lab Kits \> Received</span> shows the kits which have been received:

![](embedded-fragments-version-1-user-manual/208.png)

<span id="_Toc327881558" class="anchor"></span>Figure 79 – My Tasks \> Lab Kits \> Received

### View or Edit a Received Lab Kit Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/209.png) To view or edit a record, click the \[Select\] button at the right of the row which displays the order record. The Kit Order and Returned Kit details display:

![](embedded-fragments-version-1-user-manual/210.png)

<span id="_Toc327881559" class="anchor"></span>Figure 80 – My Tasks \> Lab Kits \> Received \> Workflow ID NNNN

INCLUDES:

- Kit Order Details \[all text boxes unless otherwise indicated\]
  - *Workflow ID \[pre-filled text\]*
  - *Patient Name \[pre-filled text\]*
  - Date Contacted (mm/dd/yyyy)
  - *TEFSC Representative \[pre-filled text\]*
  - VAMC Contact
  - Address Part1, Part2, Part3
  - City
  - State
  - ZIP
  - Country
  - Telephone \#
  - *Kit Type \[pre-filled text\]*
- Returned Kit Details \[all text boxes unless otherwise indicated\]
  - *VAMC Facility \[pre-filled text\]*
  - VAMC Contact
  - Courier Tracking \#:
  - Kit Sent by VA Date
  - Kit Received Date
    - Questionnaire Received \[Yes No radio buttons\]
  - Reason Tracking Transaction Closed \[drop-down list\]

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/211.png)</th>
<th><ul>
<li><p>Kit Lost</p></li>
<li><p>Patient Refusal</p></li>
<li><p>Other</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Comments
- \[Save\] button
- *\[Receive\] button*
- *\[Void\] button*
- \[Cancel\] button

When you have finished editing or reviewing the record, click…

![](embedded-fragments-version-1-user-manual/212.png) Click \[Save\] to save the record and return to the list, or…

![](embedded-fragments-version-1-user-manual/213.png) Click \[Cancel\] to abandon any changes made and return to the list.

Note that since the kit has already been marked as received, both the \[Receive\] and \[Void\] buttons are unavailable (grayed-out).

| ![](embedded-fragments-version-1-user-manual/214.png) | Important: Do not navigate away from the page or close your browser without clicking either \[Save\] or \[Cancel\]. |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|

## My Tasks \> Lab Kits \> Voided 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Voided Lab Kits Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                                                                  | EFR TEFSC Administrator | SCREEN NAME: | Lab Kit Queue (Not New) (see [Note](#LabKitQueueNotNew)) |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------|----------------------------------------------------------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \> Lab Kits \> Voided</span>                                                            |                         |              |                                                          |
| PURPOSE: This screen lists kits which have been marked as voided. You can use this screen to review the list of voided kits and select one for further detail. |                         |              |                                                          |

<span class="smallcaps">My Tasks \> Lab Kits \> Voided</span> shows the kits which have been voided:

![](embedded-fragments-version-1-user-manual/215.png)

<span id="_Toc327881560" class="anchor"></span>Figure 81 – My Tasks \> Lab Work \> Lab Kits \>Voided

### View a Voided Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A voided record may only be viewed; only an Administrator (Super-User) may edit such records (see Note below).

![](embedded-fragments-version-1-user-manual/216.png) Click the \[Select\] button at the right of the row which displays the order record. The Voided Kit Order details are displayed. Note that the data fields are either pre-populated read-only text or are grayed out, and cannot be selected for editing.

![](embedded-fragments-version-1-user-manual/217.png)

<span id="_Toc327881561" class="anchor"></span>Figure 82 – My Tasks \> Lab Kits \> Voided \> Workflow ID NNNN

INCLUDES:

- *Kit Order Details panel*
  - *Workflow ID*
  - *Patient Name*
  - *Date Contacted*
  - *Kit Ordered Date*
  - *TEFSC Representative*
  - *VAMC Contact*
  - *AddressPart1 \| AddressPart2 \| AddressPart3*
  - *City \| State \| Zip \| Country*
  - *Telephone Number*
  - *Kit Type*
- *Returned Kit Details panel*
  - *VAMC Facility*
  - *VAMC Contact*
  - *Courier Tracking \#*
  - *Kit Sent by VA Date*
  - *Kit Received Date*
    - *Questionnaire Received \[yes/no\]*
  - *Reason Tracking Transaction Closed*
  - *Comments*

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/218.png)</th>
<th><p><strong>Note:</strong> Only an Administrator (Super-User) can edit this record.</p>
<ul>
<li><p>![](embedded-fragments-version-1-user-manual/219.png) Click the [Save] button first; the screen redisplays.</p></li>
<li><p>Edit the fields.</p></li>
<li><p>![](embedded-fragments-version-1-user-manual/220.png) Click the [Save] button again.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](embedded-fragments-version-1-user-manual/221.png) Click the \[Un-Void\] button to return the record to the Tracking queue.

![](embedded-fragments-version-1-user-manual/222.png) When you have finished reviewing the record, click \[Cancel\] to return to the list.

Note that since the kit has already been marked as voided, both the \[Receive\] and \[Void\] buttons are unavailable (they are grayed out).

7.  <span id="_Toc327881415" class="anchor"></span>Questionnaires/Forms

# My Tasks \> Questionnaires/Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AVAILABILITY: See Table 4 – Tasks by Role

When biomonitoring specimen collection kits are returned to [TEFSC](#Glos_TEFSC) they contain a completed biomonitoring questionnaire. When fragment collection kits are returned to TEFSC they contain a completed fragment specimen collection form. Data Entry Personnel record the information contained in the questionnaires or forms into EFRA. In addition, if they learn of changes to alternate contact information from the form received, they may edit form details and add, edit, or delete alternate contact information associated with the patient.

| ![](embedded-fragments-version-1-user-manual/223.png) | Important: The biomonitoring questionnaires in EFRA should not be confused with the patient questionnaires in CPSR (as shown in Appendix G. below). |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|

- My Tasks \> Questionnaires/Forms \> New
- My Tasks \> Questionnaires/Forms \> In Process
- My Tasks \> Questionnaires/Forms \> Completed

## My Tasks \> Questionnaires/Forms \> New

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                | EFR TEFSC Administrator | SCREEN NAME: | Bio Questionnaire/Fragment Form Queue |
|--------------------------------------------------------------------------------------------------------------|-------------------------|--------------|---------------------------------------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \> Questionnaires/Forms \> New</span> |                         |              |                                       |

![](embedded-fragments-version-1-user-manual/224.png)

<span id="_Toc327881562" class="anchor"></span>Figure 83 – My Tasks \> Questionnaires/Forms \> New

Note that there are two types of questionnaire (shown in the Type column)—one for biological monitoring, and another for fragment analysis. It is possible for the same patient to have either or both.

![](embedded-fragments-version-1-user-manual/225.png) To edit or view a questionnaire record, click the \[Select\] button at the right of the row which displays the order record. The first question, along with any responses already recorded, displays as shown in Figure 84.

### Fragment Questionnaire

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Fragment Questionnaire – Fragment Body Location

![](embedded-fragments-version-1-user-manual/226.png)

<span id="_Ref262724600" class="anchor"></span>Figure 84 – Fragment Collection Kit (Fragment Location)

INCLUDES:

- *Patient Information panel*
  - *Name*
  - *DOB*
  - *SSN*
  - *Gender*
  - *Home Phone \| Work Phone \| Cell Phone*
  - *Address1 \| Address 2 \| Address 3*
  - *City \| State \| Zip Code*
- Fragment Collection Kit Form Details *panel*
  - Fragment 1 location in body \[text field\]

![](embedded-fragments-version-1-user-manual/227.png) To see the next question, click the \[Next Question\] command icon.

![](embedded-fragments-version-1-user-manual/228.png) To save the questionnaire and return to the list, click the \[Save\] command icon.

There are two other screens identical to the one above, except the text field is for fragment \#2 and \#3.

After the first screen you will also have the option to…

![](embedded-fragments-version-1-user-manual/229.png) Return to the previous screen.

| ![](embedded-fragments-version-1-user-manual/230.png) | Important: When you have buttons like \[Previous Question\], please use that button rather than your browser \[Back\] button. If you use the browser \[Back\] button, you may lose any changes you have made. |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](embedded-fragments-version-1-user-manual/231.png) | Note: After this point, all of the questions have the same patient information displayed at the top of the screen. For that reason, only the question itself will be shown and discussed for the remaining questions. |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Fragment Questionnaire – Removal Date

![](embedded-fragments-version-1-user-manual/232.png)

<span id="_Toc327881564" class="anchor"></span>Figure 85 – Fragment Collection Kit (Removal Date)

INCLUDES:

- Fragment Collection Kit Form Details panel
  - Fragment Removal Date \[text field\]

| ![](embedded-fragments-version-1-user-manual/233.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/234.png)                  | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/235.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Fragment Questionnaire – Injury Location panel

![](embedded-fragments-version-1-user-manual/236.png)

<span id="_Toc327881565" class="anchor"></span>Figure 86 – Fragment Collection Kit (Injury Location)

INCLUDES:

- Fragment Collection Kit Form Details panel
  - Location where the Veteran received the injury that resulted in shrapnel or fragments being removed from or remaining in the body \[drop-down list\]

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 17%" />
<col style="width: 43%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">![](embedded-fragments-version-1-user-manual/237.png)</th>
<th><p>Afghanistan</p>
<p>Iraq</p>
<p>Other</p></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">![](embedded-fragments-version-1-user-manual/238.png)</td>
<td colspan="3">To see the previous question, click the [Previous Question] command icon.</td>
</tr>
<tr class="even">
<td colspan="2">![](embedded-fragments-version-1-user-manual/239.png)</td>
<td colspan="3">To see the next question, click the [Next Question] command icon.</td>
</tr>
<tr class="odd">
<td colspan="2">![](embedded-fragments-version-1-user-manual/240.png)</td>
<td colspan="3">To save the questionnaire and return to the list, click the [Save] command icon.</td>
</tr>
</tbody>
</table>

#### Fragment Questionnaire – Current VA Facility

![](embedded-fragments-version-1-user-manual/241.png)

<span id="_Toc327881566" class="anchor"></span>Figure 87 – Fragment Collection Kit Details (Current VA Facility)

INCLUDES:

- Fragment Collection Kit Form Details panel
  - Name of VA Medical Center where the Veteran is currently receiving care \[text box\]

| ![](embedded-fragments-version-1-user-manual/242.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/243.png)                  | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/244.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Fragment Questionnaire – Current VA Facility Address

![](embedded-fragments-version-1-user-manual/245.png)

<span id="_Toc327881567" class="anchor"></span>Figure 88 – Fragment Collection Kit Details (Current VA Facility Address)

INCLUDES:

- Fragment Collection Kit Form Details panel
  - Address of VA Medical Center where the Veteran is currently receiving care \[text boxes\]
    - Address 1 \| Address 2 \| Address 3
    - City \| State \| Zip \| Zip plus 4

| ![](embedded-fragments-version-1-user-manual/246.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/247.png)                  | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/248.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Fragment Questionnaire – Referring Surgeon/Care Provider Name

![](embedded-fragments-version-1-user-manual/249.png)

<span id="_Toc327881568" class="anchor"></span>Figure 89 – Fragment Collection Kit Details (Referring Surgeon/Care Provider Name)

INCLUDES:

- Fragment Collection Kit Form Details panel
  - Referring Surgeon/Care Provider Name \[text box\]

| ![](embedded-fragments-version-1-user-manual/250.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/251.png)                  | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/252.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Fragment Questionnaire – Page Number

![](embedded-fragments-version-1-user-manual/253.png)

<span id="_Toc327881569" class="anchor"></span>Figure 90 – Fragment Collection Kit Details (Pager Number)

INCLUDES:

- Fragment Collection Kit Form Details panel
  - Pager Number \[text box\]

| ![](embedded-fragments-version-1-user-manual/254.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/255.png)                  | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/256.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Fragment Questionnaire – Telephone Number

![](embedded-fragments-version-1-user-manual/257.png)

<span id="_Toc327881570" class="anchor"></span>Figure 91 – Fragment Collection Kit Details (Telephone Number)

INCLUDES:

- Fragment Collection Kit Form Details
  - Telephone Number panel \[text box\]

| ![](embedded-fragments-version-1-user-manual/258.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/259.png)                  | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/260.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Fragment Questionnaire – Fax Number

![](embedded-fragments-version-1-user-manual/261.png)

<span id="_Toc327881571" class="anchor"></span>Figure 92 – Fragment Collection Kit Details (Fax Number)

INCLUDES:

- Fragment Collection Kit Form Details panel
  - Fax Number (to receive report) \[text box\]

| ![](embedded-fragments-version-1-user-manual/262.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/263.png)                  | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/264.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Fragment Questionnaire – Referring Facility Contact Name

![](embedded-fragments-version-1-user-manual/265.png)

<span id="_Toc327881572" class="anchor"></span>Figure 93 – Fragment Collection Kit Details (Referring Facility Contact)

INCLUDES:

- Fragment Collection Kit Form Details panel
  - Referring Facility Contact Name \[text box\]

| ![](embedded-fragments-version-1-user-manual/266.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/267.png)                  | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/268.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Fragment Questionnaire – Referring Facility Contact Phone

![](embedded-fragments-version-1-user-manual/269.png)

<span id="_Toc327881573" class="anchor"></span>Figure 94 – Fragment Collection Kit Details (Referring Facility Contact Phone)

INCLUDES:

- Fragment Collection Kit Form Details panel
  - Referring Facility Contact Phone Number \[text box\]

| ![](embedded-fragments-version-1-user-manual/270.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/271.png)                  | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/272.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Completing the Fragment Questionnaire

![](embedded-fragments-version-1-user-manual/273.png)

<span id="_Toc327881574" class="anchor"></span>Figure 95 – Completing the Fragment Questionnaire

INCLUDES:

- Fragment Collection Kit Form Details panel

> You have completed the Questionnaire. If you wish to save your responses, click the Complete Questionnaire button.

| ![](embedded-fragments-version-1-user-manual/274.png) | To see the previous question, click the \[Previous Question\] command icon.                          |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/275.png) | To save the questionnaire and return to the list, click the \[Complete Questionnaire\] command icon. |

After you click the \[Complete Questionnaire\] command icon, you will return to the first page of the questionnaire to see the “successful completion” notice:

![](embedded-fragments-version-1-user-manual/276.png)

<span id="_Toc327881575" class="anchor"></span>Figure 96 – Fragment Questionnaire (Successful Completion)

### The Biomonitoring Questionnaire

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Biomonitoring Questionnaire – Date Completed, VA Facility

![](embedded-fragments-version-1-user-manual/277.png)

<span id="_Toc327881576" class="anchor"></span>Figure 97 – Biological Monitoring Specimen Kit Questionnaire

INCLUDES:

- *Patient Information panel*
  - *Name*
  - *DOB*
  - *SSN*
  - *Gender*
  - *Home Phone \| Work Phone \| Cell Phone*
  - *Address1 \| Address 2 \| Address 3*
  - *City \| State \| Zip Code*
- Biological Monitoring Specimen Collection Kit Questionnaire panel \[all text fields unless otherwise indicated\]
  - Date Form Completed
  - Name of VA medical center where you are currently receiving care
  - Location of VA Medical Center where you are currently receiving care
    - Address 1 \| Address 2 \| Address 3
    - City \| State \| Zip \| Zip plus 4

![](embedded-fragments-version-1-user-manual/278.png) To see the next question, click the \[Next Question\] command icon.

![](embedded-fragments-version-1-user-manual/279.png) To save the questionnaire and return to the list, click the \[Save\] command icon.

There are two other screens identical to the one above, except the text field is for fragment \#2 and \#3.

After the first screen you will also have the option to…

![](embedded-fragments-version-1-user-manual/280.png) Return to the previous screen.

| ![](embedded-fragments-version-1-user-manual/281.png) | Important: When you have buttons like \[Previous Question\], please use that button rather than your browser \[Back\] button. If you use the browser \[Back\] button, you may lose any changes you have made. |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](embedded-fragments-version-1-user-manual/282.png) | Note: After this point, all of the questions have the same patient information displayed at the top of the screen. For that reason, only the question itself will be shown and discussed for the remaining questions. |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Biomonitoring Questionnaire – Service Branch, Injury Location and Date, Referred By (items 1 – 3)

![](embedded-fragments-version-1-user-manual/283.png)

<span id="_Toc327881577" class="anchor"></span>Figure 98 – Service Branch, Injury Location and Date, Referred By (Items 1-3)

INCLUDES:

- Biological Monitoring Specimen Collection Kit Questionnaire panel
  - Branch of Service \[drop-down list\]
  - Location where you received the injury that resulted in shrapnel or fragments being removed or remaining in your body \[drop-down list\]

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/284.png)</th>
<th><p>Afghanistan</p>
<p>Iraq</p>
<p>Other</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Date of Injury \[text field\]
- Who referred you to the VA Medical Center for evaluation of embedded fragments? \[drop-down list\]

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/285.png)</th>
<th><p>Department of Veterans Affairs</p>
<p>VA Health Care Provider</p>
<p>Department of Defense-Force Health Protection and Readiness Office</p>
<p>Another Department of Defense Office</p>
<p>Self-Referred</p>
<p>Other</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](embedded-fragments-version-1-user-manual/286.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/287.png)     | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/288.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

| ![](embedded-fragments-version-1-user-manual/289.png) | Important: When you have buttons like \[Previous Question\], please use that button rather than your browser \[Back\] button. If you use the browser \[Back\] button, you may lose any changes you have made. |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Biomonitoring Questionnaire – Injured by Bullet or Blast/Explosion (Items 4 & 5)

![](embedded-fragments-version-1-user-manual/290.png)

<span id="_Toc327881578" class="anchor"></span>Figure 99 – Biomonitoring Questionnaire – Bullets, Blast or Explosion

INCLUDES:

- Biological Monitoring Specimen Collection Kit Questionnaire panel
  - Were you injured by a bullet? \[Yes No radio buttons\]
  - Were you injured as a result of a blast or explosion? \[Yes No radio buttons\]

| ![](embedded-fragments-version-1-user-manual/291.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/292.png)     | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/293.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Biomonitoring Questionnaire – Distance from Explosion, In or On Vehicle (Items 5a, 6 & 7)

If the answer to Item 5 is “yes,” then the following additional questions appear. Otherwise, you will skip directly to Item 8.

![](embedded-fragments-version-1-user-manual/294.png)

<span id="_Toc327881579" class="anchor"></span>Figure 100 – Distance from Explosion, In or On Vehicle (Items 5a, 6 & 7)

INCLUDES:

- Biological Monitoring Specimen Collection Kit Questionnaire panel
  - If yes \[to Item 5 above\], approximately how many meters were you from the explosion? \[text box\]
  - Were you in or on a vehicle at the time of the blast or explosion? panel \[Yes No radio buttons\]
  - Was the blast or explosion caused by (check all that apply) \[checkboxes\]
    - Improvised Explosive Device (IED)
    - Rocket Propelled Grenade (RPG)
    - Land mine
    - Grenade
    - Enemy fire
    - Friendly fire
    - Unknown
    - Other

| ![](embedded-fragments-version-1-user-manual/295.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/296.png)     | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/297.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Biomonitoring Questionnaire – Where Injured (Item 8)

![](embedded-fragments-version-1-user-manual/298.png)

<span id="_Toc327881580" class="anchor"></span>Figure 101 – Biomonitoring Questionnaire – Where Injured (Item 8)

INCLUDES:

- Biological Monitoring Specimen Collection Kit Questionnaire
  - Where were you injured? Please check the boxes indicating the body area(s) where you were injured.

| 1\. Front Head                                                                                        |                                                                                    | 1\. Back Head                   |     |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------|-----|
| 2\. Front Neck                                                                                        |                                                                                    | 2\. Back Neck                   |     |
| 3\. Chest                                                                                             |                                                                                    | 6\. Upper Back                  |     |
| 4\. Abdomen                                                                                           |                                                                                    | 7\. Lower Back                  |     |
| 5\. Groin/Pelvis                                                                                      |                                                                                    | 8\. Buttocks                    |     |
| 9\. Left Shoulder                                                                                     |                                                                                    | 18\. Right Shoulder             |     |
| 10\. Left Upper Arm                                                                                   |                                                                                    | 19\. Right Upper Arm            |     |
| 11\. Left Lower Arm                                                                                   |                                                                                    | 20\. Right Lower Arm            |     |
| 12\. Left Hand, Wrist, Fingers                                                                        |                                                                                    | 21\. Right Hand, Wrist, Fingers |     |
| 13\. Left Upper Leg and Thigh                                                                         |                                                                                    | 22\. Right Upper Leg and Thigh  |     |
| 14\. Left Knee                                                                                        |                                                                                    | 23\. Right Knee                 |     |
| 15\. Left Lower Leg                                                                                   |                                                                                    | 24\. Right Lower Leg            |     |
| 16\. Left Ankle                                                                                       |                                                                                    | 25\. Right Ankle                |     |
| 17\. Left Foot and Toes                                                                               |                                                                                    | 26\. Right Foot and Toes        |     |
| ![](embedded-fragments-version-1-user-manual/299.png) | To see the previous question, click the \[Previous Question\] command icon.        |                                 |     |
| ![](embedded-fragments-version-1-user-manual/300.png)     | To see the next question, click the \[Next Question\] command icon.                |                                 |     |
| ![](embedded-fragments-version-1-user-manual/301.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |                                 |     |

#### Biomonitoring Questionnaire – Fragments and Treatment (Items 9 – 11)

![](embedded-fragments-version-1-user-manual/302.png)

<span id="_Toc327881581" class="anchor"></span>Figure 102 – Biomonitoring Questionnaire – Fragments and Treatment (Items 9 - 11)

INCLUDES:

- Biological Monitoring Specimen Collection Kit Questionnaire panel
  - Did you have shrapnel, fragments or bullets removed during surgery?
  - Do you have retained fragments or shrapnel in your body from bullets or a blast of explosion?
  - Where were you treated for this injury (mark all that apply)?
    - In the field
    - At a Combat Support Hospital
    - At Landstuhl, Germany
    - At a U.S. based Medical Treatment Facility
    - At a VA Medical Center

| ![](embedded-fragments-version-1-user-manual/303.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/304.png)     | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/305.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Biomonitoring Questionnaire – Other Foreign Bodies or Unrelated Fragments, Urine Collection (Items 12 – 13)

![](embedded-fragments-version-1-user-manual/306.png)

<span id="_Toc327881582" class="anchor"></span>Figure 103 – Biomonitoring Questionnaire – Other Foreign Bodies or Unrelated Fragments, Urine Collection (Items 12 – 13)

INCLUDES:

- Biological Monitoring Specimen Collection Kit Questionnaire panel
  - Do you have any other foreign material in your body such as a joint replacement or pacemaker?
  - Do you have shrapnel or fragments in your body that are not related to the injury discussed above?
  - Has a 24 hour urine collection for monitoring for exposure to the contents of the shrapnel or fragments been performed?

| ![](embedded-fragments-version-1-user-manual/307.png) | To see the previous question, click the \[Previous Question\] command icon.        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/308.png)     | To see the next question, click the \[Next Question\] command icon.                |
| ![](embedded-fragments-version-1-user-manual/309.png) | To save the questionnaire and return to the list, click the \[Save\] command icon. |

#### Biomonitoring Questionnaire – Other Foreign Bodies or Unrelated Fragments, Urine Collection (Items 12 – 13)

![](embedded-fragments-version-1-user-manual/310.png)

INCLUDES:

- Biological Monitoring Specimen Collection Kit Questionnaire panel

> You have completed the Questionnaire. If you wish to save your responses, click the Complete Questionnaire button.

| ![](embedded-fragments-version-1-user-manual/311.png) | To see the previous question, click the \[Previous Question\] command icon.                          |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/312.png) | To save the questionnaire and return to the list, click the \[Complete Questionnaire\] command icon. |

After you click the \[Complete Questionnaire\] command icon, you will return to the first page of the questionnaire to see the “successful completion” notice:

![](embedded-fragments-version-1-user-manual/313.png)

<span id="_Toc327881583" class="anchor"></span>Figure 104 – Successful Save and Completion

## My Tasks \> Questionnaires/Forms \> In Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/314.png)

<span id="_Toc327881584" class="anchor"></span>Figure 105 – Questionnaires/Forms \> In Process

Note that there are two types of questionnaire (shown in the Type column)—one for biological monitoring, and another for fragment analysis. It is possible for the same patient to have either or both.

![](embedded-fragments-version-1-user-manual/315.png) To edit or view onscreen a questionnaire record, click the \[Select\] button at the right of the row which displays the order record. The first question, along with any responses already recorded, displays as shown in Figure 84.

| ![](embedded-fragments-version-1-user-manual/316.png) | Note: The screens for <span class="smallcaps">In Process</span> kits are the same as those for <span class="smallcaps">New</span> kits. For that reason, they are not shown in this section. Please refer to the screen shots and explanations of the data elements starting at 14.1.1 above. |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](embedded-fragments-version-1-user-manual/317.png) To view an onscreen tabular report (called the Questionnaire Summary), click the \[View\] button at the right of the row which displays the order record. A sample of such a report appears in Figure 106.

![](embedded-fragments-version-1-user-manual/318.png)

<span id="_Ref262738793" class="anchor"></span>Figure 106 – Sample "View" Report

You may print the report just as you might any other web page, by using your browser’s print command.

![](embedded-fragments-version-1-user-manual/319.png) To close the report, click the \[Close\] button at the bottom of the screen.

## My Tasks \> Questionnaires/Forms \> Completed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/320.png)

<span id="_Toc327881586" class="anchor"></span>Figure 107 – Questionnaires/Forms \> Completed

Note that there are two types of questionnaire (shown in the Type column)—one for biological monitoring, and another for fragment analysis. It is possible for the same patient to have either or both.

![](embedded-fragments-version-1-user-manual/321.png) To edit or view onscreen a questionnaire record, click the \[Select\] button at the right of the row which displays the order record. The first question, along with any responses already recorded, displays as shown in Figure 84.

| ![](embedded-fragments-version-1-user-manual/322.png) | Note: The screens for <span class="smallcaps">In Process</span> kits are the same as those for <span class="smallcaps">New</span> kits. For that reason, they are not shown in this section. Please refer to the screen shots and explanations of the data elements starting at 14.1.1 above. |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

8.  <span id="_Toc327881422" class="anchor"></span>Lab Orders

# # My Tasks \> Lab Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AVAILABILITY: See Table 4 – Tasks by Role

For any lab orders that are placed with the metals lab, the [TEFSC](#Glos_TEFSC) Admin Staff records the lab order information into the EFR application and print the lab order form that is shipped with the specimen to the metals lab. The [BVAMC](#Glos_BVAMC) Lab is used to analyze creatinine levels in urine samples but, for all other analysis, the specimen is sent to the metals lab. Only lab order information for orders being shipped to the metals lab is covered here. The TEFSC Admin Staff also utilizes the EFR system capabilities provided in this use case to edit an existing order or cancel an existing order. A patient may have multiple occurrences of biomonitoring and/or fragment analysis over time.

## Lab Orders \> New

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th>AVAILABILITY:</th>
<th>TEFSC Nurse</th>
<th>SCREEN NAME:</th>
<th>Lab Order Queue</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">ACCESS: To access this screen, select <span class="smallcaps">My Tasks &gt; Lab Orders &gt; New</span></td>
</tr>
<tr class="even">
<td colspan="4"><p>PURPOSE: After a biomonitoring or fragment analysis kit has been received, TEFSC needs to place an order with the laboratory. The orders are placed in the lab orders screen.</p>
<p>Biomonitoring lab orders result in a paper document generated by the application, which will then be handed over to the laboratory.</p>
<p>For Fragment Analysis, no paper document is being generated, but the actual lab order is handled outside the application, with the lab order screen just used for tracking purposes.</p>
<p>The lab queue presents a view of all workflows that need a lab analysis ordered.</p>
<p>Once the Nurse has found the referral of interest, the [Select] button can be used to pull up the referral details screen, as described in 11.1.3.</p></td>
</tr>
</tbody>
</table>

![](embedded-fragments-version-1-user-manual/323.png)

<span id="_Toc327881587" class="anchor"></span>Figure 108 – Lab Orders \> New (List)

### New Fragment Analysis Lab Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/324.png)

<span id="_Toc327881588" class="anchor"></span>Figure 109 – New Lab Orders (Details)

INCLUDES:

- Patient Information \[pre-filled text\]
  - *Name* \| *SSN*
  - *Service Branch* \| *Service Status*
- Lab Request
  - *Sample Type* \[pre-filled text\]
  - *Lab Request \#* \[pre-filled text\]
  - Lab Request Date \[text box\]
  - Date Sample Received at metals Lab \[text box\]

Note that since these lab orders are still awaiting completion, the \[Save\] button is unavailable (grayed-out) until you enter new data.

![](embedded-fragments-version-1-user-manual/325.png) Click the \[Save\] button to save the data you entered. The screen redisplays, now showing the updates you made in the appropriate fields.

![](embedded-fragments-version-1-user-manual/326.png) If the order is complete, click the \[Complete\] button.

![](embedded-fragments-version-1-user-manual/327.png) If the order is to be voided, click the \[Void\] button.

![](embedded-fragments-version-1-user-manual/328.png) Or, click \[Back\] to discard any changes you have made, or to exit without making any changes. You return to the lab order list.

### New Biological Monitoring Lab Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/329.png)

<span id="_Toc327881589" class="anchor"></span>Figure 110 - New Biological Monitoring Lab Orders (Detail)

INCLUDES:

- Patient Information \[pre-filled text\]
  - *Name* \| *SSN*
  - *Service Branch* \| *Service Status*
- Lab Request
  - *Sample Type* \[pre-filled text\]
  - *Lab Request \#* \[pre-filled text\]
  - Lab Request Date \[text box\]
  - Date Sample Received at metals Lab \[text box\]
  - BSO Number \[text box\]
  - Tracking Number \[text box\]
  - *Sample ID Number* \[pre-filled text\]
  - Sample Description \[text box\]
  - Sample Instructions \[text box\]
- Analytes
  - Aluminum \| Arsenic \| Cadmium \| Chromium
  - Cobalt \| Copper \| Iron \| Manganese
  - Nickel \| Lead \| Uranium \| Uranium

> \| 235/238

- Tungsten \| Zinc \| All
- Other \[text box\]

Note that since the lab orders are still awaiting completion, the \[Save\] button is unavailable (grayed-out) until you enter new data. The \[Print\] button is grayed-out until the record is moved to the Awaiting Results queue. This function prints the letter sent to the TEFSC lab.

![](embedded-fragments-version-1-user-manual/330.png) Click the \[Save\] button to save the data you entered. The screen redisplays, now showing the updates you made in the appropriate fields.

![](embedded-fragments-version-1-user-manual/331.png) If the order is complete, click the \[Complete\] button.

![](embedded-fragments-version-1-user-manual/332.png) If the order is to be voided, click the \[Void\] button.

![](embedded-fragments-version-1-user-manual/333.png) Or, click \[Cancel\] to discard any changes you have made, or to exit without making any changes. You return to the lab order list.

## Lab Orders \> Awaiting Results 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th>AVAILABILITY:</th>
<th>TEFSC Nurse</th>
<th>SCREEN NAME:</th>
<th>Lab Order Queue</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">ACCESS: To access this screen, select <span class="smallcaps">My Tasks &gt; Lab Orders &gt; Awaiting Results</span></td>
</tr>
<tr class="even">
<td colspan="4"><p>PURPOSE: This screen displays all the available voided lab orders</p>
<p>Once the user has found the lab order of interest, click the [Select] button to view the Lab Order details screen.</p></td>
</tr>
</tbody>
</table>

![](embedded-fragments-version-1-user-manual/334.png)

<span id="_Toc327881590" class="anchor"></span>Figure 111 – Lab Orders \> Awaiting Results

| ![](embedded-fragments-version-1-user-manual/335.png) | Click \[Select\] to view the lab order. The fields and functionality on the in Process screens are identical to those depicted [Section 15.1.1](#new-fragment-analysis-lab-orders) and [15.1.2](#new-biological-monitoring-lab-orders) for both Fragment Analysis and Biological Monitoring respectively, with one exception. The \[Print\] button for Biological Monitoring is now available to print the letter sent to the TEFSI lab. |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Filtering Lab Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To filter the lab results, select the appropriate filter in the Filter by drop-down menu.

![](embedded-fragments-version-1-user-manual/336.png)

Enter the appropriate filter information.

| ![](embedded-fragments-version-1-user-manual/337.png) | Click \[Go\] to apply the filter.                     |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/338.png) | Click \[Clear\] to reset the contents of the filters. |

## Lab Orders \> Voided

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th>AVAILABILITY:</th>
<th>TEFSC Nurse</th>
<th>SCREEN NAME:</th>
<th>Lab Order Queue</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">ACCESS: To access this screen, select <span class="smallcaps">My Tasks &gt; Lab Orders &gt; Voided</span></td>
</tr>
<tr class="even">
<td colspan="4"><p>PURPOSE This screen displays all the available voided lab orders</p>
<p>Once the user has found the lab order of interest, click the [Select] button to view the Lab Order details screen.</p></td>
</tr>
</tbody>
</table>

The fields and functionality on the Voided screens are identical to those depicted [Section 15.1.1](#new-fragment-analysis-lab-orders) and [15.1.2](#new-biological-monitoring-lab-orders) for both Fragment Analysis and Biological Monitoring respectively. The only changes are:

Since such lab orders have been voided, the \[Complete\], \[Print\], and \[Void\] buttons are unavailable (grayed-out). The \[Save\] button has been replaced with the \[Un-Void\] button.

| ![](embedded-fragments-version-1-user-manual/339.png) | Click \[Un-Void\] to return the order to the Awaiting Results queue.                                                          |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/340.png)    | Click \[Back\] to discard any changes you have made, or to exit without making any changes. You return to the lab order list. |

To filter the lab orders, refer to Section 15.2.1.

## Lab Orders \> Closed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th>AVAILABILITY:</th>
<th>TEFSC Nurse</th>
<th>SCREEN NAME:</th>
<th>Lab Order Queue</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">ACCESS: To access this screen, select <span class="smallcaps">My Tasks &gt; Lab Orders &gt; Closed</span></td>
</tr>
<tr class="even">
<td colspan="4"><p>PURPOSE: This screen displays all the available voided lab orders</p>
<p>Once the user has found the lab order of interest, click the [Select] button to view the Lab Order details screen.</p></td>
</tr>
</tbody>
</table>

![](embedded-fragments-version-1-user-manual/341.png)

<span id="_Toc327881591" class="anchor"></span>Figure 112 – Lab Orders \> Closed

To filter the lab orders, refer to Section 15.2.1.

### Closed Fragment Analysis Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The fields and functionality on the Closed order screen are identical to those depicted [Section 15.1.1](#new-fragment-analysis-lab-orders). Closed Fragment Analysis orders are set for read only. All other options are unavailable. Click the \[Back\] button to return to the Closed lab order list.

### Closed Biological Monitoring Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The fields and functionality on the Closed order screen are identical to those depicted [Section 15.1.2](#new-biological-monitoring-lab-orders). Closed Biological Monitoring orders are set for read only. Your options are:

![](embedded-fragments-version-1-user-manual/342.png) Click the \[Print\] button to print the letter to send to the TEFSI lab

![](embedded-fragments-version-1-user-manual/343.png) Or, click \[Back\] to discard any changes you have made, or to exit without making any changes. You return to the Closed lab order list.

# My Tasks \> Lab Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AVAILABILITY: See Table 4 – Tasks by Role

Once an EFR patient's biomonitoring lab order results are made available from the [BVAMC](#Glos_BVAMC) Lab via electronic interface, the TEFSC Admin Staff views the lab order results and closes the associated lab order by acknowledging receipt.

Biomonitoring lab results (but not Fragment lab results) are received via electronic interface from the BVAMC lab. Each lab result is reviewed manually by the Nurse, who can either accept or void the lab result. Each lab order can only have one accepted lab result, so if multiple lab results come in for the same order, the Nurse has to decide which one is correct and manually void all other ones.

## Lab Results \> New

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/344.png)

<span id="_Toc327881592" class="anchor"></span>Figure 113 – Lab Results \> New (List)

### New Fragment Analysis Lab Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/345.png)

<span id="_Toc327881593" class="anchor"></span>Figure 114 – New Fragment Analysis Lab Result (Detail)

INCLUDES:

- Patient Information \[pre-filled text\]
  - *Name* \| *SSN*
  - *Service Branch* \| *Service Status*
- Lab Report Details \[all text boxes except as noted\]
  - *Kit Received Date* \[pre-filled text\]
  - Metals Lab Report Date \| Accession \#
  - Lab Code \| Lab ID
  - Producing Event Date
- Create Fragment button
- Fragment Data
  - Fragment ID \# \| Description \| \[Select\] button

![](embedded-fragments-version-1-user-manual/346.png) Click the \[Save\] button to save the data you entered. The screen redisplays, now showing the updates you made in the appropriate fields.

![](embedded-fragments-version-1-user-manual/347.png) Or, click \[Void\] to void the lab result. The system will display a warning:

![](embedded-fragments-version-1-user-manual/348.png)

Click \[Ok\] to void the record. The record will be moved Voided section. Click \[Cancel\] to go back to the record.

![](embedded-fragments-version-1-user-manual/349.png) Or, click \[Cancel\] to discard any changes you have made, or to exit without making any changes. If any changes were made to the record, the system will display a warning:

![](embedded-fragments-version-1-user-manual/350.png)

Click \[Ok\] to discard any changes and return to the lab results screen. Click \[Cancel\] to stay on the record.

Before selecting any of these options, you may click the <u>Go To Associated Lab Order</u> text link to see the lab order associated with these results.

#### Lab Results\> New \>Create Fragment

The \[Create Fragment\] button appears on both the Fragment Analysis New and In Process Lab Results. To enter multiple fragments:

1.  Click the \[Create Fragment\] the previous screen (either the Lab Results \> New or Lab Results \> In Process screen).
2.  Enter all of the appropriate information in the necessary fields.
3.  Click the \[Save\] button to return to the Lab Results screen.
4.  Repeat this process for all fragments.

![](embedded-fragments-version-1-user-manual/351.png)

<span id="_Toc327881594" class="anchor"></span>Figure 115 – Create Fragment Entry Screen

INCLUDES:

- Fragment Data
  - Fragment ID \# \[text box\] \| Description {text box\]
  - Mass \[text box\] \[drop-down list\] \| Dimensions
    - Length \[text box\] \[drop-down list\]
    - Height \[text box\] \[drop-down list\]
    - Width \[text box\] \[drop-down list\]
- Radioactive \[Yes No radio buttons\] \| Radioactive Result \[text box\]
- Comments \[text box\]
- Tissue Sent \[Yes No radio buttons\] \| Tissue Associated with Fragment

> Details \[text box\]

- Analyte Data panel \[pre-filled text\]
  - \[Edit\] and \[Delete\] buttons
  - Analyte
  - Analysis Method
  - Analysis Type
  - Result %
  - Comments
  - CAS Number

![](embedded-fragments-version-1-user-manual/352.png) Click the \[Save\] button to save the data you entered. The screen redisplays, now showing the updates you made in the appropriate fields.

![](embedded-fragments-version-1-user-manual/353.png) Or, click \[Void\] to void the lab result. The system will display a warning:

![](embedded-fragments-version-1-user-manual/354.png)

Click \[Ok\] to void the record. The record will be moved Voided section. Click \[Cancel\] to go back to the record.

![](embedded-fragments-version-1-user-manual/355.png) Or, click \[Cancel\] to discard any changes you have made, or to exit without making any changes. If any changes were made to the record, the system will display a warning:

![](embedded-fragments-version-1-user-manual/356.png)

Click \[Ok\] to discard any changes and return to the lab results screen. Click \[Cancel\] to stay on the record.

Before selecting any of these options, you may click the <u>Go To Associated Lab Order</u> text link to see the lab order associated with these results.

### New Lab Results Biological Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/357.png)

<span id="_Toc327881595" class="anchor"></span>Figure 116 –New Biological Monitoring Lab Results (Detail)

INCLUDES:

- Patient Information \[pre-filled text\]
  - *Full Name* \| *Birth Date* \| *ICN*
  - *SSN* \| *Gender*
- Lab Report Details \[all text boxes except as noted\]
  - *Kit Received Date*
  - Lab Contact \| Accession \[UID\] \# \| Lab Report Date
  - *Lab Name* \| *Specimen Type* \| Specimen Collection

> Date

- Producing Event Date
- Lab Tests
  - Elapsed Time (hours) \| Total Volume (ml) \| Volume of Analyte

> Tests (ml)

- \[Edit\] Button \| \[Delete\] Button
- Drop-Down Lists:
  - Test Name \| Analyte Name \| Analysis Method \|  
    Reference Range Unit \| Above Lab Reference Range \[check box\]
- Text Boxes:
  - Result \| Lab Reference Range \| Evaluation Note \| Comments
- \[Add Analyte\] Button

![](embedded-fragments-version-1-user-manual/358.png) Click the \[Save\] button to save the data. The screen redisplays, now showing the updates you made in the appropriate fields.

![](embedded-fragments-version-1-user-manual/359.png) Or, click \[Void\] to void the lab result. The system will display a warning:

![](embedded-fragments-version-1-user-manual/360.png)

Click \[Ok\] to void the record. The record will be moved Voided section. Click \[Cancel\] to go back to the record.

![](embedded-fragments-version-1-user-manual/361.png) Or, click to accept the lab results. You return to the lab results list. The system will display a warning:

![](embedded-fragments-version-1-user-manual/362.png)

Click \[Ok\] to accept the record. You will be moved to the Accepted section. Click \[Cancel\] to go back to the record.

![](embedded-fragments-version-1-user-manual/363.png) Or, click \[Back\] to discard any changes you have made, or to exit without making any changes. If any changes were made to the record, the system will display a warning:

![](embedded-fragments-version-1-user-manual/364.png)

Click \[Ok\] to discard any changes and return to the lab results screen. Click \[Cancel\] to stay on the record.

Before selecting any of these options, you may click the <u>Go To Associated Lab Order</u> text link to see the lab order associated with these results.

## Lab Results \> In Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The fields and functionality on the Voided screens are identical to those depicted [Section 16.1.1](#new-fragment-analysis-lab-results) and [16.1.2](#lab-results-new-create-fragment) for both Fragment Analysis and Biological Monitoring respectively; with one exception. The \[Accept\] button is now available on the Fragment Analysis In Process Screen.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/365.png)</th>
<th><p><strong>Note:</strong> The EFR lab interface will retrieve lab results for patients who have a Biomonitoring lab order in the EFR application. The lab interface will use a patient’s SSN to match EFR patients in the Registries database to patients in the Research file in the Baltimore lab system.</p>
<p>The EFR lab interface will attempt to retrieve lab results only for patients whose lab results are not in an ‘Accepted’ state in the EFR application. A patient’s lab results may be edited manually while in an ‘In Process’ state. However, the interface will continue to retrieve results as long as the patient’s results remain in the ‘In Process’ queue. A manually edited result will be overwritten by results retrieved by the interface upon its next execution. Likewise, the EFR application will continue to allow new lab results to be entered manually for a patient but those results may potentially be overwritten by the interface until the results are accepted.</p>
<p>The EFR lab interface will continue to retrieve lab results for a patient until the patient’s lab results are marked as ‘Accepted’ in the EFR application. Patient lab results retrieved by the EFR lab interface will be placed in the Lab Results/In Process queue where they will be manually reviewed and ‘accepted’.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Lab Results \> Accepted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you accept a Lab Result, the record is set as read only. Your options are:

| ![](embedded-fragments-version-1-user-manual/366.png) | Click the \[Unaccept\] button to return the record to the Lab Results \> In Process queue. This option is only available to the TEFSC Administrator (Super user). |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/367.png) | Click the \[Back\] button to return to the list of accepted lab results.                                                                                          |

## Lab Results \> Voided

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The fields and functionality on the Voided screens are identical to those depicted [Section 16.1.1](#new-fragment-analysis-lab-results) and [16.1.2](#lab-results-new-create-fragment) for both Fragment Analysis and Biological Monitoring respectively. Voided records are editable. Enter all appropriate information and click:

![](embedded-fragments-version-1-user-manual/368.png) Click the \[Un-Void\] button to save the data you entered and return the record to the In Process queue. The screen redisplays, in the In Process queue, showing the updates you made in the appropriate fields.

![](embedded-fragments-version-1-user-manual/369.png) Or, click to accept the lab results. You return to the lab results list. The system will display a warning:

![](embedded-fragments-version-1-user-manual/370.png)

Click \[Ok\] to accept the record. You will be moved to the Accepted section. Click \[Cancel\] to go back to the record.

![](embedded-fragments-version-1-user-manual/371.png) Or, click \[Back\] to discard any changes you have made, or to exit without making any changes. On the Fragment Analysis screen, the back button is replaced with the \[Cancel\] button, however, the functionality remains identical. If any changes were made to the record, the system will display a warning:

![](embedded-fragments-version-1-user-manual/372.png)

Click \[Ok\] to discard any changes and return to the lab results screen. Click \[Cancel\] to stay on the record.

9.  <span id="_Toc327881440" class="anchor"></span>Interpretation & Follow Up

# My Tasks \> Interpretation & Follow Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a patient's lab results have been received, the [TEFSC](#Glos_TEFSC) Provider will be notified (using methods outside the scope of EFRA). The TEFSC Provider accesses a patient's lab results in order to assess their care for TEFSC concerns. The TEFSC Provider also records the interpretation and communicates this to the Patient and to the Local [VA](#Glos_VA) Provider (or Primary Care Physician, if available). The system produces separate hardcopy letters which are sent directly to the Patient and Local VA Provider. An Alternate Local VA Provider may also be designated as a recipient. The Provider can also modify an existing interpretation, discontinue or proceed with follow up biomonitoring on a patient, identify lab results that are deemed to indicate high concentrations of an analyte found in the lab result, and define custom reference ranges to aid in the communication of the results.

## My Tasks \> Interpretation & Follow Up \> New 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                                                             | See Table 4 – Tasks by Role | SCREEN NAME: | Interpretation Queue |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------|----------------------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \> Interpretation & Follow Up \> New</span>                                        |                             |              |                      |
| PURPOSE: This screen lists those patients who have been accepted into the Registry for either Biological Monitoring (Biomonitoring) or Fragment Analysis. |                             |              |                      |

![](embedded-fragments-version-1-user-manual/373.png)

<span id="_Toc327881596" class="anchor"></span>Figure 117 – My Tasks \> Interpretation & Follow Up \> New

Note the column headed Specimen Type. A patient may have one, two or all three of the various types: biological monitoring, fragment analysis, or consultation.

| ![](embedded-fragments-version-1-user-manual/374.png)  | To edit or view a workflow questionnaire record, click the \[Select\] button at the right of the row which displays the workflow record. The workflow information displays as shown in 17.1.1 and 17.1.2 below. |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/375.png) | Click \[Print Completed Letters\] to print all letters from the Batch Printing queue.                                                                                                                           |

### My Tasks \> Interpretation & Follow Up \> New \> Workflow ID \[Biomonitoring\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detail screens for Biomonitoring and Fragment Analysis present different data. The screen for Biomonitoring is shown below, in three parts.

![](embedded-fragments-version-1-user-manual/376.png)

<span id="_Ref273538798" class="anchor"></span>Figure 118 – My Tasks \> Interpretation & Follow Up \> New \> Workflow ID nnnn (Biological Monitoring, Part 1)

INCLUDES:

- *Patient Information*
  - *Full Name \| Birth Date \| ICN*
  - *SSN \| Gender \| Zip Code*
- Lab Report Details \[all text boxes unless otherwise indicated\]
  - *Kit Received Date \[pre-filled text\]*
  - Lab Contact
  - Accession (UID)
  - *Lab Report Date \[pre-filled text\]*
  - *Lab Name \[pre-filled text\]*
  - *Specimen Type \[pre-filled text\]*
  - Specimen Collection Date (mm/dd/yyyy) \[text box\]
- *Lab Tests \[all pre-filled text\] \[may repeat, as for CREATININE test, CONCENTRATION test, etc.\]*
  - *Elapsed Time \| Total Volume \| Volume of Analyte Tests*
  - *Test Name \| Analysis Method \| Analyte*
  - *Result*
  - *Comments*
  - *TEFSC Reference Range*
  - *Lab Reference Range*
    - *Lab Reference Range \|* Above TEFSC Reference Range \[Yes/No\]
    - *Above Lab Reference Range*

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/377.png)</th>
<th><p><strong>Note:</strong> The patient’s Full Name field displayed on the <span class="smallcaps">My Tasks&gt;Interpretation &amp; Follow Up&gt;New (or In Process)&gt;Workflow ID</span> <em><span class="smallcaps">n</span></em> screen has been hyperlinked to the patient’s Workflows screen. Similar functionality exists on the Referrals screen for Open and Closed referrals.</p>
<p>Clicking the hyperlink will display the Workflow Information screen for the patient.</p>
<p>Clicking [Cancel] on the Workflows screen will return to the previous screen from which the hyperlink was clicked.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](embedded-fragments-version-1-user-manual/378.png)<span id="_Ref273538799" class="anchor"></span>

Figure 119 – My Tasks \> Interpretation & Follow Up \> New \> Workflow ID nnnn (Biological Monitoring, Part 2)

INCLUDES:

- Provider Address \[all pre-filled text\]
- *Primary care Physician \| Local VAMC Contact \[all prefilled text\]*
  - \[Send to PCP\] button \| \[Send to Contact\] button
- Provider Address \[all text boxes\]
  - Name
  - Facility Name
  - Address Part 1, 2, 3
  - City
  - State
  - ZIP
  - Country
  - Telephone \#
- Patient Address \[all text boxes\]
  - Name
  - Address Part 1, 2, 3
  - City
  - State
  - ZIP
  - Country
  - Telephone \#
- Interpretation Notes to Provider
  - Provider Notes \[text box\]

![](embedded-fragments-version-1-user-manual/379.png)

<span id="_Toc327881599" class="anchor"></span>Figure 120 – My Tasks \> Interpretation & Follow Up \> New \> Workflow ID nnnn (Biological Monitoring, Part 3)

INCLUDES:

- Interpretation Notes to Patient
  - Patient Notes \[text box\]
- Letter Information \[all text boxes unless otherwise indicated\]
  - Provider Letter From
  - Provider Letter Subject (Patient name and last 4 digits of SSN will be appended to end)
  - Signing Clinician \[select from drop-down list\]

> ![](embedded-fragments-version-1-user-manual/380.png)

- CC Name
- Provider Letter Comment Before Signature
- Patient Letter Comment Before Signature
- Biomonitoring Follow Up
  - Need Biomonitoring Follow Up?
    - Yes \| No
  - Follow Up Biomonitoring Due Date (mm/dd/yyyy) \[text box\]
  - Remind Me On (mm/dd/yyyy) \[text box\]

When you have finished editing or reviewing the record…

| ![](embedded-fragments-version-1-user-manual/381.png) | Click \[Save\] to save the record and return to the list.                                                                 |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/382.png)       | Click \[Interpret Complete\] to mark the record as complete and return to the list. The record will be In Process status. |
| ![](embedded-fragments-version-1-user-manual/383.png)   | Click \[Add to Print Queue\] to add the letter to the Batch Printing queue.                                               |
| ![](embedded-fragments-version-1-user-manual/384.png) | Click \[Preview Provider Letter\] to print a letter to the VA Provider.\*                                                 |
| ![](embedded-fragments-version-1-user-manual/385.png)    | Click \[Preview Patient Letter\] to print a letter to the Patient.\*                                                      |
| ![](embedded-fragments-version-1-user-manual/386.png)    | Click \[Back\] to abandon any changes made and return to the list.                                                        |

> *\*This option is not available in the New queue.*

### My Tasks \> Interpretation & Follow Up \> New \> Workflow ID \[Fragment Analysis\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detail screens for Fragment Analysis and Biomonitoring present different data. Below is the screen for Fragment Analysis.

![](embedded-fragments-version-1-user-manual/387.png)

<span id="_Toc327881600" class="anchor"></span>Figure 121 – My Tasks \> Interpretation & Follow Up \> New \[Fragment Analysis\] \> Workflow ID NNNN

INCLUDES:

- *Patient Information*
  - *Full Name \| ICN*
  - *SSN \| Gender*
  - *Birth Date*
- *Lab Report Details \[all pre-filled text\]*
  - *Metals Lab Report Date \| Accession \#*
  - *Lab Code \| Lab ID*
  - *Producing Event Date*
- *Fragment Data \[all pre-filled text\]*
  - *Fragment ID# \| Description \| \[Select button\]*
- *Analyte Data \[prefilled text in columns\]*
  - *Analyte \| Analysis Method \| Analysis Type \| Result % \| Comments \| CAS Number*
- *Primary Care Physician \| Local VAMC Contact*
  - *PCP Address \| Local VAMC Address*
  - *\[Send to PCP Button\] \| \[Send to Contact Button\]*
- Provider Address panel \[all text boxes\]
  - Name
  - Facility name
  - Address Part 1 \| Part 2 \| Part 3
  - City \| State \| Zip \| Country
  - Telephone#
- *Patient Address*
  - Name
  - Address Part 1 \| Part 2 \| Part 3
  - City \| State \| Zip \| Country
  - Telephone#
- Interpretation Notes to Provider panel \[text box\]
- Interpretation Notes to Patient panel \[text box\]
- Letter Information \[all text boxes unless otherwise indicated\]
  - Provider Letter From
  - Provider Letter Subject (Patient name and last 4 digits of SSN will be appended to end)
  - Signing Clinician \[select from drop-down list\]

> ![](embedded-fragments-version-1-user-manual/388.png)

- CC Name
- Provider Letter Comment Before Signature
- Patient Letter Comment Before Signature

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/389.png)</th>
<th><p><strong>Note:</strong> The patient’s Full Name field displayed on the <span class="smallcaps">My Tasks&gt;Interpretation &amp; Follow Up&gt;New (or In Process)&gt;Workflow ID</span> <em><span class="smallcaps">n</span></em> screen has been hyperlinked to the patient’s Workflows screen. Similar functionality exists on the Referrals screen for Open and Closed referrals.</p>
<p>Clicking the hyperlink will display the Workflow Information screen for the patient.</p>
<p>Clicking [Cancel] on the Workflows screen will return to the previous screen from which the hyperlink was clicked.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

When you have finished editing or reviewing the record…

| ![](embedded-fragments-version-1-user-manual/390.png) | Click \[Save\] to save the record and return to the list.                                                                 |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/391.png)       | Click \[Interpret Complete\] to mark the record as complete and return to the list. The record will be In Process status. |
| ![](embedded-fragments-version-1-user-manual/392.png)   | Click \[Add to Print Queue\] to add the letter to the Batch Printing queue.                                               |
| ![](embedded-fragments-version-1-user-manual/393.png) | Click \[Preview Provider Letter\] to print a letter to the VA Provider.\*                                                 |
| ![](embedded-fragments-version-1-user-manual/394.png)    | Click \[Preview Patient Letter\] to print a letter to the Patient.\*                                                      |
| ![](embedded-fragments-version-1-user-manual/395.png)    | Click \[Back\] to abandon any changes made and return to the list.                                                        |

> *\*These options are not available in the New queue.*

## Interpretation & Follow Up \> In Process 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                             | See Table 4 – Tasks by Role | SCREEN NAME: | \[???\] |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------|---------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \> Interpretation & Follow Up \> In Process</span> |                             |              |         |
| PURPOSE: This screen is designed to show the interpretation records currently in process.                                 |                             |              |         |

![](embedded-fragments-version-1-user-manual/396.png)

<span id="_Toc327881601" class="anchor"></span>Figure 122 – My Tasks \> Interpretation & Follow Up \> In Process

Note that there are two types of specimens (shown in the Specimen Type column)—one for biological monitoring, and another for fragment analysis. It is possible for the same patient to have either or both.

| ![](embedded-fragments-version-1-user-manual/397.png) | To edit or view onscreen a record, click the \[Select\] button at the right of the row which displays the order record. |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|

To edit or view onscreen a record, click the \[Select\] button at the right of the row which displays the order record.

| ![](embedded-fragments-version-1-user-manual/398.png) | Note: The screens for <span class="smallcaps">In Process</span> records are the same as those for <span class="smallcaps">New</span> records. For that reason, they are not shown in this section. Please refer to the screen shots and explanations of the data elements starting at 17.1 above. |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

When you have finished editing or reviewing the record…

| ![](embedded-fragments-version-1-user-manual/399.png) | Click \[Save\] to save the record and return to the list.                                                                 |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/400.png)       | Click \[Interpret Complete\] to mark the record as complete and return to the list. The record will be In Process status. |
| ![](embedded-fragments-version-1-user-manual/401.png)   | Click \[Add to Print Queue\] to add the letter to the Batch Printing queue.                                               |
| ![](embedded-fragments-version-1-user-manual/402.png) | Click \[Preview Provider Letter\] to print a letter to the VA Provider. The letter is printed from this screen.           |
| ![](embedded-fragments-version-1-user-manual/403.png)    | Click \[Preview Patient Letter\] to print a letter to the Patient. The letter is printed from this screen.                |
| ![](embedded-fragments-version-1-user-manual/404.png)    | Click \[Back\] to abandon any changes made and return to the list.                                                        |

## Interpretation & Follow Up \> Interpreted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                              | See Table 4 – Tasks by Role | SCREEN NAME: | \[???\] |
|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------|---------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \> Interpretation & Follow Up \> Interpreted</span> |                             |              |         |
| PURPOSE: This screen is designed to show the records for which interpretation is complete.                                 |                             |              |         |

![](embedded-fragments-version-1-user-manual/405.png)

<span id="_Toc327881602" class="anchor"></span>Figure 123 – Interpretation & Follow Up \> Interpreted

Note that there are two specimens (shown in the Specimens Type column)—one for biological monitoring, and another for fragment analysis. It is possible for the same patient to have either or both.

| ![](embedded-fragments-version-1-user-manual/406.png)                  |     | To edit or view onscreen a record, click the \[Select\] button at the right of the row which displays the order record.                                                                                                                                                                                |     |     |
|----------------------------------------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| ![](embedded-fragments-version-1-user-manual/407.png) |     | Note: The screens for <span class="smallcaps">Interpreted</span> records are the same as those for <span class="smallcaps">New</span> records. For that reason, they are not shown in this section. Please refer to the screen shots and explanations of the data elements starting at 17.1 above. |     |     |

The primary difference between this type of record and the earlier ones is that the record would carry complete lab tests and fragment analyses, like these:

![](embedded-fragments-version-1-user-manual/408.png)

<span id="_Toc327881603" class="anchor"></span>Figure 124 – Complete Lab Test Results

You would likely also see completed interpretation notes, like this:

![](embedded-fragments-version-1-user-manual/409.png)

<span id="_Toc327881604" class="anchor"></span>Figure 125 – Completed Interpretation Notes

When you have finished editing or reviewing the record…

| ![](embedded-fragments-version-1-user-manual/410.png) | Click \[Save\] to save the record and return to the list. This ability to edit a completed interpretation letter is only available to the TEFSC Administrator (Superuser). All other users, the \[Save\] button will be greyed-out. |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/411.png)       | Click \[Interpret Complete\] to mark the record as complete and return to the list. The record will be In Process status.\*                                                                                                         |
| ![](embedded-fragments-version-1-user-manual/412.png)   | Click \[Add to Print Queue\] to add the letter to the Batch Printing queue.\*                                                                                                                                                       |
| ![](embedded-fragments-version-1-user-manual/413.png) | Click \[Preview Provider Letter\] to print a letter to the VA Provider. The letter is printed from this screen.                                                                                                                     |
| ![](embedded-fragments-version-1-user-manual/414.png)    | Click \[Preview Patient Letter\] to print a letter to the Patient. The letter is printed from this screen.                                                                                                                          |
| ![](embedded-fragments-version-1-user-manual/415.png)    | Click \[Back\] to abandon any changes made and return to the list.                                                                                                                                                                  |
|                                                                                                       | *\* These options are not available from the Interpreted queue.*                                                                                                                                                                    |

### Printing an Interpretation Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After clicking \[Preview Provider Letter\] or \[Preview Patient Letter\], the EFRA will display the interpretation letter.

| ![](embedded-fragments-version-1-user-manual/416.png) | Note: The screens for Patient and Provider Interpretation are identical. For that reason, only the provider letter is shown Figure 126. |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|

![](embedded-fragments-version-1-user-manual/417.png)

<span id="_Ref312833553" class="anchor"></span>Figure 126 – Interpretation Letter Preview

On the task bar at the top of the letter:

| ![](embedded-fragments-version-1-user-manual/418.png) | Scrolls between the pages of the letter.                                                                                  |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/419.png)                                                   | Exports the letter to one of the listed formats (PDF, Excel or Word). Select the appropriate format and click \[Export\]. |
| ![](embedded-fragments-version-1-user-manual/420.png) | Refreshes the data in the letter.                                                                                         |
| ![](embedded-fragments-version-1-user-manual/421.png)    | Prints the letter.                                                                                                        |

### Batch Printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clicking the \[Add to Print Queue\] button on the My Tasks \> Interpretation & Follow Up \> New \> Workflow ID \[Biomonitoring\], My Tasks \> Interpretation & Follow Up \> New \> Workflow ID \[Fragment Analysis\], and either Interpretation & Follow Up \> In Process screens adds that letter to the Batch Print Queue.

To print all letters in the print queue, click \[Print Completed Letters\] on the My Tasks \> Interpretation & Follow Up \> New screen, refer to Section 17.3.1 Printing an Interpretation Letter for details on printing.

| ![](embedded-fragments-version-1-user-manual/422.png) | Note: The letters in the batch print queue are not official completed letters. They are draft versions for review only. |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|

## My Tasks \> Contact Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| AVAILABILITY:                                                                                                  | See Table 4 – Tasks by Role | SCREEN NAME: | \[???\] |
|----------------------------------------------------------------------------------------------------------------|-----------------------------|--------------|---------|
| ACCESS: To access this screen, select <span class="smallcaps">My Tasks \> \[Contact Logs\] All Contacts</span> |                             |              |         |
| PURPOSE: This screen is designed to show all of the contact logs.                                              |                             |              |         |

During the course of managing a case in the EFR, it is often necessary for [TEFSC](#Glos_TEFSC) personnel to contact providers, patients, or their representatives. It may also be necessary or advantageous to have the patient visit the TEFSC for certain activities. The contact log will serve as a chronological record detailing the relevant information recorded during these communications with the provider, patient, or their representatives.

![](embedded-fragments-version-1-user-manual/423.png)

## Contact Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### All Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/424.png)

<span id="_Toc327881606" class="anchor"></span>Figure 127 – Contact Logs \> All Contacts

When you select the <span class="smallcaps">Contact Logs \> All Contacts</span> task, you will see the list of contact logs, as shown above.

![](embedded-fragments-version-1-user-manual/425.png) Select a record to look at or work on by clicking the \[Select\] button at the right of the row containing the record. Or, if you have triaged a referral and clicked \[Add Contact\] (see 11.1.3.4 above) and if no contact log has previously been established, you will see the New Log screen. You will see the same information in either, as shown in Figure 128.

### Creating or Editing a Contact Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/426.png)

<span id="_Ref257709064" class="anchor"></span>Figure 128 – Contact Log

INCLUDES:

- *Patient*
  - *ICN*
  - *Name*
  - *SSN*
  - *DOB*
- Contact Log Details (all text entry boxes unless otherwise indicated)
  - Person Contacted Last Name
  - Person Contacted First Name
  - Date and Time Contact was Made
  - *Name of Person Initiating Contact (provided by application)*
  - Method of Contact \[w/ drop-down list\]
  - Person Contacted Telephone Number
  - Person Contacted Email
  - Person Contacted Addr1
  - Person Contacted Addr2
  - Person Contacted Addr3
  - Person Contacted City
  - Person Contacted State
  - Person Contacted ZIP Code+4
  - Person Contacted Country
  - Reason for Contact
  - Textual Record of the Contact Conversation \[w/ text entry box\]
  - Telemedicine Consultation with Provider? \[Yes No radio buttons\]
  - Telemedicine Consultation with Patient? \[Yes No radio buttons\]
  - Inpatient Evaluation Recommended? \[Yes No radio buttons\]
  - Inpatient Evaluation Completed Date
  - Follow Up Contact Needed? \[Yes No radio buttons\]
  - Follow Up Contact Required By Date
  - Follow Up Contact Completed Date

Enter the available information. From here, you can…

| ![](embedded-fragments-version-1-user-manual/427.png) | Save the Contact information and exit the Contact form |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/428.png) | Cancel the edit and close the Contact record           |

<span id="_Toc259014232" class="anchor"></span>

10. Patients Tab

# Patients tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From any area of the application, you can search for a patient already in the Registry. Click on the Patients tab; the <span class="smallcaps">Patients \> Patients Lookup</span> screen appears and displays the Lookup Patient pane. You can search using either the SSN, patient Last Name, or a combination. EFRA uses “contains” search logic. *Do not* use “wildcard” indicators like “\*” or “?” in your search.

Here we enter the Last Name and click on \[Search\] (or, you may press the \< Enter \> key). Note how the text entry box background changes to light yellow when you start entering text.

![](embedded-fragments-version-1-user-manual/429.png)

<span id="_Toc327881608" class="anchor"></span>Figure 129 – Patient Search Pane

INCLUDES:

- Lookup Patient \[all text boxes\]
  - SSN
  - First Name
  - Last Name
  - ICN

![](embedded-fragments-version-1-user-manual/430.png) When you have entered the data, click the \[Search\] button.

## Patient Search Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this case, we find several patients (only two shown here):

![](embedded-fragments-version-1-user-manual/431.png)

<span id="_Toc327881609" class="anchor"></span>Figure 130 – Patient Search Results

![](embedded-fragments-version-1-user-manual/432.png) To view complete information for a patient, click on the \[Select\] button at the right of the row listing the patient.

## Patient Data Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All available patient data is displayed. Note that the data in the Patient Information pane (which was brought over from [VistA](#Glos_VistA)) is read-only here. You may, however, enter data in the Patient Alternative Contact pane.

INCLUDES:

- Patient Information \[all pre-filled text\]
  - *ICN*
  - *SSN*
  - *Full Name*
  - *Home VAMC*
  - *Gender*
  - *Birth Date*
  - *Race*
  - *Death Date*
  - *Marital Status*
  - *Ethnicity*
  - *Address \| Address Line 2 \| Address Line 3*
  - *City \| State \| Postal Code \| County \| Country*
  - *Home Phone \| Work Phone*
- Patient Alternate Contact Information \[all text boxes unless otherwise noted\]
  - Alternate Street Address 1 \| 2 \| 3
  - Alternate City \| State \| ZIP \| Country
  - Alternate Home Telephone
  - Alternate Work Telephone
  - Alternate Mobile Telephone
    - Preferred Alternate Telephone Number \[ radio buttons; select one\]
      - Home
      - Work
      - Mobile
  - Email Address

Again, note that the text field turns light yellow when you begin to enter text:

![](embedded-fragments-version-1-user-manual/433.png)

<span id="_Toc327881610" class="anchor"></span>Figure 131 – Patient Data Display (Showing New Data Entry)

![](embedded-fragments-version-1-user-manual/434.png) Click the \[Save\] button to save the data you entered. The screen redisplays, now showing the updates you made in the appropriate fields. Make other changes as needed and click \[Save\]. When you have made all desired changes, use the LEFT NAVIGATION BAR or the TABS to continue with other tasks.

![](embedded-fragments-version-1-user-manual/435.png) Or, click \[Cancel\] to discard any changes you have made, or to exit without making any changes. You return to the search results screen.

## Patient Not Found

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a patient is not found using your search criteria, you will see this result:

![](embedded-fragments-version-1-user-manual/436.png)

<span id="_Toc327881611" class="anchor"></span>Figure 132 – Patient Not Found

Use the LEFT NAVIGATION BAR or the TABS to continue with other tasks.

11. <span id="_Toc327881458" class="anchor"></span>Administration Tab

# Administration tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Administration Application allows the Admin Staff to view, edit, and sort user roles. The Admin Staff role is designed to be a global role that is not specific to any facility. The Admin Staff can view, edit, and manage users and user roles.

## Administration \> Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At <span class="smallcaps">Administration \> Users</span>, a list of all users displays on the screen.

![](embedded-fragments-version-1-user-manual/437.png)

<span id="_Toc327881612" class="anchor"></span>Figure 133 – Administration \> Users List

Use this screen to see users and to edit information about the user (“profile” information), to edit the user’s roles, or to remove the user from the list of authorized users. You can search for a specific user, or leave the search field empty and click \[Search\] to see all users. Search results are displayed as shown above.

| ![](embedded-fragments-version-1-user-manual/438.png) | To edit information about the user, click the \[Edit\] button beside the user’s name. MORE INFORMATION: 19.1.1*.*              |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/439.png) | To edit information about the user’s role, click the \[Edit Roles\] button beside the user’s name. MORE INFORMATION: 19.1.2*.* |
| ![](embedded-fragments-version-1-user-manual/440.png)   | To remove the user from the list, click the \[Remove\] button. You will be asked to confirm the removal.                           |
| ![](embedded-fragments-version-1-user-manual/441.png) | To add a new user, click the \[Add\] button at the bottom of the screen. MORE INFORMATION: 19.1.4.                                 |

### Administration \> Edit User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](embedded-fragments-version-1-user-manual/442.png)

<span id="_Ref263149043" class="anchor"></span>Figure 134 – Administration \> Users \> Name

INCLUDES:

- Edit User Account Information \[all text boxes\]
  - NT Username
  - Full Name
  - First Name
  - Middle Name
  - Last Name
  - Maiden Name
  - Employee Number
  - Job Title
  - Email Address
  - Telephone
  - Fax

When you have recorded the new or changed information…

| ![](embedded-fragments-version-1-user-manual/443.png) | Click the \[Save\] button to save the record. There is no acknowledgment message; the edit screen redisplays with the updated information.                                                                               |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/444.png)    | Click the \[Close\] button to close the edit screen and return to the list of users. Remember that the state in which you left the information at the time you click \[Close\] is what will be retained in the database. |

Use the LEFT NAVIGATION BAR to choose your next task.

### Administration \> Edit User Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The available roles are:

- Admin Staff: The Admin Staff is responsible for administrative activities associated with placing kit orders with third party vendors for specimens and fragments. The Admin Staff will also manage kit tracking and sample tracking.
- TEFSC COORDINATOR (Super User): The TEFSC Coordinator is ultimately responsible for following EFR patients through their lifecycle of involvement with [TEFSC](#Glos_TEFSC). The TEFSC Coordinator is responsible for keeping the TEFSC Providers informed of status of cases. Another responsibility of the TEFSC Coordinator is to perform population level surveillance using data captured in the EFR.
- TEFSC PROVIDER: TEFSC Providers are the physicians located at the [TEFSC](#Glos_TEFSC). They act as subject matter experts on the standards of care as they apply to Veterans who have embedded fragments. Through analysis of EFR data they develop handbooks and directives that convey care guidelines to the Local [VA](#Glos_VA) Providers at VAMC facilities. TEFSC Providers also interpret lab results for individual patients to provide treatment recommendations to the Local VA Providers.
- TEFSC NURSE: The TEFSC Nurse is responsible for interaction with [VA](#Glos_VA) providers and patients to assist with information gathering required to make Registry population determinations and coordination of clinical consultations.
- Data Entry Personnel: When biomonitoring specimen collection kits are returned to [TEFSC](#Glos_TEFSC), they contain a completed biomonitoring questionnaire. When fragment collection kits are returned to TEFSC they contain a completed fragment specimen collection form. Data Entry Personnel record information from the forms into EFRA. In addition, if they learn of changes to alternate contact information from the form received, they may edit form details and edit, or delete alternate contact information associated with the patient.

![](embedded-fragments-version-1-user-manual/445.png)

<span id="_Toc327881614" class="anchor"></span>Figure 135 – Administration \> Users \> Name \> Roles

INCLUDES:

- Edit User Role Information
  - *User Profile \[all pre-filled text\]*
    - *NT Username*
    - *Full Name*
    - *Job Title*
  - Roles \[all checkboxes; check one, several, or all\]
    - Admin Staff
    - TEFSC Coordinator (Super User)
    - TEFSC Provider
    - TEFSC Nurse
    - TEFSC Data Entry Personnel

When you have recorded the new or changed information…

| ![](embedded-fragments-version-1-user-manual/446.png) | Click the \[Save\] button to save the record. There is no acknowledgment message; the edit screen redisplays with the updated information.                                                                               |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/447.png)    | Click the \[Close\] button to close the edit screen and return to the list of users. Remember that the state in which you left the information at the time you click \[Close\] is what will be retained in the database. |

Use the LEFT NAVIGATION BAR to choose your next task.

### Administration \> Users \> Remove User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you click the \[Remove\] button on the user list screen, you will be asked to confirm the removal:

![](embedded-fragments-version-1-user-manual/448.png)

<span id="_Toc327881615" class="anchor"></span>Figure 136 – Confirm User Removal

| ![](embedded-fragments-version-1-user-manual/449.png) | Click \[OK\] to remove the user                                           |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/450.png) | Click \[Cancel\] to cancel the removal and leave the user in the database |

### Administration \> Users \> Add New User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Searching the User Database

On the Administration \> User screen, click \[Add User\].

In order to limit the number of duplicate users, you must first do a search to determine if the username is already in the database. Enter the complete NT username.

![](embedded-fragments-version-1-user-manual/451.png)

<span id="_Toc327881616" class="anchor"></span>Figure 137 – Administration \> Add User \> Search

| ![](embedded-fragments-version-1-user-manual/452.png)     | Click \[Search\] to execute the search.                                                |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/453.png)     | Click \[Clear\] to clear the search field of all contents                              |
| ![](embedded-fragments-version-1-user-manual/454.png) | Click \[Close\] to cancel the process and return to the Administration \> Users screen |

#### New Username Does Not Exist

If the username you entered is not found in the database, you will see the view/edit screen for user changes (as shown in Figure 134 above). Complete and save the information as shown in that section.

| ![](embedded-fragments-version-1-user-manual/455.png) | Important: Verify the user role information is accurate. If a role is not assigned, the user will not be able to access EFRA. See 19.1.2 above. |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|

#### New Username Already Exists

If the username you entered already exists, you will see this screen:

![](embedded-fragments-version-1-user-manual/456.png)

<span id="_Toc327881617" class="anchor"></span>Figure 138 – Username Exists

The system advises you that a user by this name is already in the database. While you cannot add the new username, you can see the details about the existing username:

| ![](embedded-fragments-version-1-user-manual/457.png) | Click the \[View/Edit User Account\] button. The view/edit screen for user changes appears (as shown in Figure 134 above). |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/458.png) | Or, click the \[Close\] button to return to the user list.                                                                 |

## Administration \> Role Matrix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to managing users and their roles by name, you can also see a list of users and all their associated user roles. Clicking the user’s ID number brings up the Administration \> Edit User Roles screen.

![](embedded-fragments-version-1-user-manual/459.png)

<span id="_Toc327881618" class="anchor"></span>Figure 139 – Administration \> Role Matrix

You can download the list in a format suitable for loading into Excel.

| ![](embedded-fragments-version-1-user-manual/460.png) | Click the \[Download to Excel\] button. You will see a popup like this:                                  |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
|                                                                                                       | ![](embedded-fragments-version-1-user-manual/461.png)       |
| ![](embedded-fragments-version-1-user-manual/462.png) | Click \[Open\] to run Excel and insert the contents of the list into the spreadsheet EFR User Roles.xls. |
| ![](embedded-fragments-version-1-user-manual/463.png) | Click \[Save\] to save the list to your hard drive.                                                      |
| ![](embedded-fragments-version-1-user-manual/464.png) | Click \[Cancel\] to cancel the file download.                                                            |

If you click \[Open\], you may see this notice:

![](embedded-fragments-version-1-user-manual/465.png)

<span id="_Toc327881619" class="anchor"></span>Figure 140 – Excel Format Warning

Click \[Yes\] to run Excel and insert the contents of the downloaded file.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 93%" />
</colgroup>
<thead>
<tr class="header">
<th>![](embedded-fragments-version-1-user-manual/466.png)</th>
<th><p><strong>Note:</strong> Although the spreadsheet will display the same notice seen on the list screen…</p>
<p> To sort please click table headings  </p>
<p>… you cannot sort using this method. We suggest that you delete the row carrying the notice and use Excel’s built-in sort utilities if you wish.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Administration \> Reference Ranges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reference Ranges screen provides TEFSC the ability to maintain their own reference ranges for lab results. The TEFSC reference range is the acceptable level of metals in a patient’s bloodstream.

![](embedded-fragments-version-1-user-manual/467.png)

<span id="_Toc327881620" class="anchor"></span>Figure 141 – Administration \> Reference Ranges

| ![](embedded-fragments-version-1-user-manual/468.png) | Click \[Edit\] next to the appropriate analyte to adjust the reference range. |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|

### Editing a Reference Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Administration \> Reference Range \> Analyte screen, adjust the reference range as appropriate.

![](embedded-fragments-version-1-user-manual/469.png)

<span id="_Toc327881621" class="anchor"></span>Figure 142 – Administration \> Reference Range \> Edit Analyte

INCLUDES:

- *Test Name*
- *Analyte Name*
- TEFSC Reference Range
- Unit \[Drop-Down Menu\]

| ![](embedded-fragments-version-1-user-manual/470.png) | Click \[Update\] to save the changes to the analyte                               |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| ![](embedded-fragments-version-1-user-manual/471.png) | Click \[Cancel\] to discard the changes and return to the Reference Range screen. |

## Administration \> Auto Triage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TEFSC Administrator (Superuser) has the ability to automatically triage all new referrals in the referral queue. To auto-triage qualifying referrals, click \[Run Auto Triage\]:

![](embedded-fragments-version-1-user-manual/472.png)

<span id="_Toc327881622" class="anchor"></span>Figure 143 – Run Auto Triage

This automatic triaging functionality is executable at any point in time by the superuser role. The EFRA will automatically pull in the referrals according to the following qualifications:

1.  The system triages new referrals to a biomonitoring workflow that have one of the following risk categories:
2.  The Auto-triage indicates that the patient has had a fragment removed at surgery or has a documented retained fragment
3.  The Auto-triage indicates that the patient has a high likelihood of having a retained fragment
4.  The Auto-triage indicates the veteran possibly has a retained fragment as a result of injuries sustained while serving in the area of conflict.
5.  The system triages new referrals that show the veteran likely does not have a retained fragment as a result of injuries sustained while serving in the area of conflict as ineligible, with an ineligibility reason of "Likely does not have fragment."
6.  The system triages new referrals that have the Unable to Screen health factor (for any reason) as Ineligible only where there are no health factors present from the second clinical reminder. For these scenarios, the Auto-triage generates the ineligibility reason as the name of the health factor as it appears on the screen (i.e., Acute Illness, Severe Cognitive Impairment, or Refused Screening Tool).
7.  The system triages duplicate referrals as ineligible with an ineligibility reason of "Duplicate."
8.  The "Reviewed By" as reflected on the Referral screen and in the Referral export will indicate SYSTEM as the user for any referral triaged by this script.
9.  The data validation rules applied on the referral screen for the VA Contact fields would not be applicable to this script; whatever data is sent from the source systems will be written to the database as received.

## Administration \> DoD Fragment Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Administration \> DoD Fragment Data screen displays read-only information regarding the date of the last DoD extract.

![](embedded-fragments-version-1-user-manual/473.png)

<span id="_Toc327881623" class="anchor"></span>Figure 144 – Administration \> DoD Fragment Data Extract

12. <span id="_Toc327881470" class="anchor"></span>Appendixes
1.  <span id="_Toc327881471" class="anchor"></span>Browsers and Web-Based Applications

    <span id="_Toc327881472" class="anchor"></span>A.1. Standard Web Browser Shortcut Keys

In the following table, two or more keys connected by a plus sign (+) indicate that the keys should be pressed at the same time. Keys connected by a comma (,) indicate that the keys should be pressed in succession. These keys can be used while running EFRA in a web browser.

<table style="width:100%;">
<colgroup>
<col style="width: 0%" />
<col style="width: 35%" />
<col style="width: 0%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 0%" />
<col style="width: 10%" />
<col style="width: 0%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><strong>Browser Option</strong></th>
<th colspan="2"><strong>Shortcut</strong></th>
<th colspan="2"><strong>IE</strong></th>
<th colspan="2"><strong>Firefox</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Bookmark menu</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Ctrl &gt; + &lt; B &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Bookmark, new (for current page)</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Ctrl &gt; + &lt; D &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Browser window, new</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Ctrl &gt; + &lt; N &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Browser window, close</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Alt &gt; + &lt; F4 &gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>*</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Close browser window</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Alt &gt; + &lt; F4 &gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>*</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Exit browser</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Alt &gt; + &lt; F4 &gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>*</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Find [on the page displayed]</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Ctrl &gt; + &lt; F &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Help</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; F1 &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Location in history, go to next</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Alt &gt; + &lt; &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>&lt; Space &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Location in history, go to previous</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Alt &gt; + &lt; &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>&lt; Backspace &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Location, open</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Ctrl &gt; + &lt; L &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Home page, go to</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Alt &gt; + &lt; Home &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>New browser window</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Ctrl &gt; + &lt; N &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Open location</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Ctrl &gt; + &lt; L &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Print…</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Alt &gt; , &lt; F &gt; , &lt; P &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select All [on the page displayed]</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Ctrl &gt; + &lt; A &gt;</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Tab, close</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Ctrl &gt; + &lt; W &gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>n/a*</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tab, open new</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt; Ctrl &gt; + &lt; T &gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>n/a*</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="6"><blockquote>
<p>Window management</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;R&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(restore)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;M&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(move)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;S&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(size)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;N&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(minimize)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;X&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(maximize)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>&lt; Alt &gt; + &lt; space &gt;, &lt;C&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(close)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="8"><blockquote>
<p>* In versions prior to 8.0 (not currently authorized for VA use, and not tested with the application)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc327881473" class="anchor"></span>A.2. Web Pages

In a web-based application, a “page” is the specific area on your computer screen used by a program. You might start on a launch page, for example, and use the menus available to you to move to another, more specific task-oriented page. If you have more than one browser window running at the same time, you can go from one window to another by clicking in each of those windows or by using [\< Alt \>+\< Tab \>](#Glos_AltTab). You can also move, close, or minimize the application window to make room for another window (see A.2.12. Changing (Resizing) a Browser Window for further instructions on these functions).

Elements which may appear on web pages are shown in the following paragraphs.

A.2.1. Pop-up Windows

These are windows that pop up within (or on top of) a window to provide or request information. Ordinarily, they require some action before they will disappear. Clicking on buttons with the words \[OK\], \[Cancel\], \[Exit\], or something similar usually closes these windows. Sometimes, they can be dismissed by pressing the \< Esc \> key.

A.2.1. Text Box

| SAMPLES: | 1                                                                                                  | 2                                                                                               |
|----------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
|          | ![](embedded-fragments-version-1-user-manual/474.png) | ![](embedded-fragments-version-1-user-manual/475.png) |

Note how the appearance of the box changes: from a plain line border (SAMPLE 1) to an almost three-dimensional, pale yellow-highlighted field when you tab to it or click in it (SAMPLE 2).

Type your entry into the text box. The entry will not be saved until you tab away from or otherwise exit from the text box. In cases where the format of your entry is important, a sample will appear near the box. The relative width of these boxes is usually a reflection of the number of characters you are allowed to enter. Sometimes (as with date fields) there may also be a “date picker” next to the field; see A.2.16. Pop-up Calendars for details.

You should see a “tool tip” pop up when you hover your mouse pointer over the text box.

![](embedded-fragments-version-1-user-manual/476.png)

<span id="_Toc327881624" class="anchor"></span>Figure 145 – Tool Tip for Text Box

A.2.3. Checkbox

SAMPLE: ![](embedded-fragments-version-1-user-manual/477.png)

A checkbox “toggles” (changes) between a YES / NO, ON / OFF setting. It is typically a square box which can contain a check mark ![](embedded-fragments-version-1-user-manual/478.png) or an “X” ☒ and is usually accompanied by text. Clicking the box or tabbing to the field and pressing the spacebar toggles the checkbox setting. In some instances, checkboxes may be used to provide more than one choice; in such cases, more than one box can be selected. Sometimes, a pre-determined “default” entry will be made for you in a checkbox; you can change the default if needed.

A.2.4. Radio button

SAMPLE: ![](embedded-fragments-version-1-user-manual/479.png)

- A radio button, also known as an option button, is a small, hollow circle adjacent to text. Radio buttons usually appear in sets, with each button representing a single choice; normally, only one button in the set may be selected at any one time. Clicking on the radio button places a solid dot in the circle, selecting the option. Clicking a selected radio button de-selects it, removing the dot. As one radio button is selected, others within the category switch off. For example, Male or Female may be offered as choices through two radio buttons, but you can only select one of the choices. Similarly, some questions require a “yes” or a “no” response: Yes No.

A.2.5. Command button

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SAMPLES</p>
<p>![](embedded-fragments-version-1-user-manual/480.png)</p>
<p>![](embedded-fragments-version-1-user-manual/481.png)</p></th>
<th><p>A command button initiates an action. It is a rectangular “3-dimensional” shape with a label that specifies what action will be performed when the button is clicked. Common examples are shown at left. Command buttons that end with three dots indicate that selecting the command may evoke a subsidiary window.</p>
<p>In the text of this document, command button names appear inside square brackets. <em>Examples:</em> [Search], [Save].</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](embedded-fragments-version-1-user-manual/482.png)</td>
<td>The [Cancel] command allows you to cancel the action about to be taken, or to discard changes made on a form. For example, when closing an application, you may be prompted to validate the action to close. If you click the [Cancel] button, the application will not close and you will resume from the point at which the close action was initiated. Or, on a data screen, you may use the [Cancel] button to discard any changes you may have made to the data and close the tab.</td>
</tr>
<tr class="even">
<td>![](embedded-fragments-version-1-user-manual/483.png)</td>
<td>The [Select] command is used to select records for editing.</td>
</tr>
<tr class="odd">
<td>![](embedded-fragments-version-1-user-manual/484.png)</td>
<td>The [Search] command is used to find one or more records. When at least one character is typed in a lookup dialog box, clicking the [Search] button will bring up matching entries. In many cases, leaving the lookup box blank will find all such records. Enter the search string and click [Search]<strong>.</strong> Searches are case-insensitive and use “contains” logic.</td>
</tr>
<tr class="even">
<td>![](embedded-fragments-version-1-user-manual/485.png)</td>
<td>The [OK] command is used to accept a default choice, or to agree with performing an action.</td>
</tr>
<tr class="odd">
<td><p>![](embedded-fragments-version-1-user-manual/486.png)</p>
<p>![](embedded-fragments-version-1-user-manual/487.png)</p></td>
<td>Other command buttons may be unique to a specific screen. For example, the [Clear Triage] button is used when editing a Referral record and you wish to “clear” (or undo) the triage decision just made. These buttons are described under the discussion of the individual screen(s) to which they apply.</td>
</tr>
</tbody>
</table>

A.2.6. Date fields

SAMPLE: ![](embedded-fragments-version-1-user-manual/488.png)

Date fields are identified by their labels, but otherwise look like an ordinary text field. They may have an associated popup calendar (see A.2.16. Pop-up Calendars). The month and day components of the date may consist of one or two digits and the year must consist of four digits (*e.g.*, 7/27/07 or 7/27/2007). You may use either slashes (/) or dashes (-) to separate the month, day and year. The selected entry will not be effective until you tab away from or otherwise exit the date field; at that point, the year will be reformatted, if necessary, to four digits; likewise, if you use dashes as separators, they will be converted to slashes.

A.2.7. Drop-Down List

| SAMPLE 1: | ![](embedded-fragments-version-1-user-manual/489.png) |
|-----------|-------------------------------------------------------------------------------------------------------|
| SAMPLE 2: | ![](embedded-fragments-version-1-user-manual/490.png)    |

A drop-down list (sometimes called a “pull-down” list) is displayed as a box with an arrow button on the right side (SAMPLE 1). Such a list allows you to select one item from the list. The current choice (or a prompt) is visible in a small rectangle; when you click on the arrow, a list of items is revealed (SAMPLE 2). Click on one of the entries to make it your choice; the list disappears.

To select multiple items from a drop-down list, first pick one item or a value from the drop-down list and click the \[Add\] button. To add an additional item from the drop-down list, choose that item from the drop-down and again click \[Add\].

![](embedded-fragments-version-1-user-manual/491.png)

A.2.7. List Box

SAMPLE: ![](embedded-fragments-version-1-user-manual/492.png)

The list box shows a list of items. If more items exist than can be seen in the box, a scroll bar appears on the side of the box. Click the desired entry to select it from the list.

A.2.8. Faded (“Grayed Out”) Choices

As a web-based application, EFRA does not use grayed-out choices. If a choice is unavailable, it will simply not appear on screen, or (if it is a link) will not respond to clicking.

A.2.9. Keyboard Commands

| ![](embedded-fragments-version-1-user-manual/493.png) | Keyboard keys and onscreen buttons are shown in different style brackets throughout this manual to differentiate them from on-screen buttons or menu options: \< Ctrl \> and \< Enter \> are on the keyboard, \[Close\] is a command button on the screen. |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](embedded-fragments-version-1-user-manual/494.png) See [Appendix B](#AppendixB) for a complete listing of keyboard shortcuts.

A.2.10. Read-Only Data Fields

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
<p>![](embedded-fragments-version-1-user-manual/495.png)</p></th>
<th>![](embedded-fragments-version-1-user-manual/496.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Generally speaking, the read-only data thus shown is pre-populated by data feeds from various sources.

A.2.11. Tab Key

Use the \< Tab \> key or the mouse to move between fields. Do *not* use the \< Enter \> or \< Return \> key, which is usually reserved for the default command button or action.

| ![](embedded-fragments-version-1-user-manual/497.png) | Tip: In most cases, you may move “backward” to a previous field by holding down the \< Shift \> key and pressing \< Tab \>. |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|

A.2.12. Changing (Resizing) a Browser Window

Windows and columns displayed within EFRA cannot be resized, although the size of the browser window can be changed. To change the size of a browser window, position the mouse pointer over the right edge of the column or the outside edge of the window, left click, and while holding the mouse button down, move the mouse and “drag” to change the size of the window or column. Position the mouse pointer over one corner and drag diagonally to increase the size of the entire window.

| ![](embedded-fragments-version-1-user-manual/498.png) | Note: Also see Resizing the Browser Screen for tips on how to maximize or minimize browser windows using the keyboard. |
|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|

A.2.13. Online Help

SAMPLE: ![](embedded-fragments-version-1-user-manual/499.png)

Provides generalized help on the application, or specialized help for the area in which you are currently working. See Online Help for more information.

A.2.14. OK button

SAMPLE: ![](embedded-fragments-version-1-user-manual/500.png)

Confirms the input and initiates the action defined by the window. Also indicates that you agree with the default choice shown in the window.

A.2.15. Save button

SAMPLE: ![](embedded-fragments-version-1-user-manual/501.png)

Saves all changes made since the last save action. If you attempt to save and all required fields have not yet been completed, you will receive notification that the required fields must be completed before saving.

A.2.16. Pop-up Calendars

| ![](embedded-fragments-version-1-user-manual/502.png) | Note: This function will be included in a future increment. |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|

SAMPLE: ![](embedded-fragments-version-1-user-manual/503.png)

Pop-up calendars are used throughout EFRA. Click the calendar icon ![](embedded-fragments-version-1-user-manual/504.png) next to the entry box to open the “date picker.”

| *Example:* | ![](embedded-fragments-version-1-user-manual/505.png) |
|------------|---------------------------------------------------------------------------------------------------------------------------------------|

You can select or change the date displayed on the calendar using the methods described in the following table.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>To Select/Change…</th>
<th>Do this:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Month</strong></td>
<td><p>To change the month, click on the down arrow [  ] next to the month at the top of the calendar.</p>
<p>![](embedded-fragments-version-1-user-manual/506.png)</p></td>
</tr>
<tr class="even">
<td><strong>Day</strong></td>
<td>Click the actual day of the week on the calendar. Or, use the left and right arrows to move through the days of the month.</td>
</tr>
<tr class="odd">
<td><strong>Year</strong></td>
<td>Click on the down arrow next to the year.</td>
</tr>
</tbody>
</table>

A.2.16. System Timeout

| ![](embedded-fragments-version-1-user-manual/507.png) | Note: This function will be included in a future increment. |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|

A timeout function is automatically enforced in EFRA. When you open the application, your activity is programmatically monitored. If there is no activity for 20 minutes, the application will begin to shut itself down.

The “Application Time Out” message window displays for 30 seconds. If there is still no activity within 30 seconds, the application automatically closes; a countdown of seconds remaining is displayed.

A.2.17. Activating Drop-Down Lists

You can activate drop-down lists from the keyboard. Simply tab to the drop-down list field and press the up \<  \> or down arrow key \<  \>.

A.2.18. Navigating the Date Picker Calendar Pop-ups

Using the date selection pop-up calendars (known as “date pickers”) may be somewhat problematic for those using screen readers such as [JAWS](#Glos_JAWS). The pop-up date picker calendar is essentially a graphic, rather than text, feature that is designed to be navigated using the mouse. There are no keyboard equivalents in this application. You can, however, simply type a properly-formatted date into the text box.

A.2.19. Using the \< Ctrl \>, \< Alt \> and \< Esc \> Keys

Some of the current features of the EFRA navigation may not be intuitive if you are using assistive technology (for example, a screen reader like [JAWS](#Glos_JAWS)). Remember that the following statements apply to the browser, not to EFRA.

In many situations, pressing \< Ctrl \> + a letter that represents the function will perform a function (for example, \< Ctrl \>+\< P \> activates the browser <u>P</u>rint menu).

\< Alt \>+\< F4 \> closes the browser (and also closes EFRA).

\< Esc \> often may be used to close dialog boxes and pop-ups.

A.2.20. Resizing the Browser Screen

Instead of clicking the browser’s Maximize ![](embedded-fragments-version-1-user-manual/508.png) button, you can press \< Alt \>+\< space \> and then select Ma<u>x</u>imize by pressing \< x \>. If you wish to minimize the screen, you may press \< Alt \>+\< space \> and then select Mi<u>n</u>imize by pressing \< n \>.

![](embedded-fragments-version-1-user-manual/509.png)

<span id="_Toc253397863" class="anchor"></span>Figure 146 – Resizing the Browser Screen

You can also resize your browser window to match the resolution of your monitor. For example, to resize the window to 1024 x 768 pixels, enter the following into the browser address box and press \< Enter \>: javascript:window.resizeTo(1024,768); (yes, include the semicolon at the end). This works both in Internet Explorer (shown below) and in Firefox, although with slightly different results. *Source:* <http://www.petefreitag.com/item/633.cfm>

#### Windows Accessibility Features

The Windows operating system offers a number of accessibility shortcuts which can be useful. These are “toggled” options, meaning that you perform the specified action once to turn the option on, and then again to turn it off.

| ![](embedded-fragments-version-1-user-manual/510.png) | Warning: Using some of these options will dramatically change the way your computer keyboard functions. If all else fails, reboot your computer to clear any such selections. |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Each option will produce a popup confirmation window like those pictured below. Each of these confirmation pop-ups has the same three choice buttons, in this order left to right: \[OK\], \[Cancel\], and \[Settings\]. \[OK\] is always the default choice.

B.1. StickyKeys

StickyKeys lets you use the \< Shift \>, \< Ctrl \> or \< Alt \> keys by pressing one key at a time, rather than having to press these keys in conjunction with another key.

Press \< Shift \> five times to toggle StickyKeys on and off:

![](embedded-fragments-version-1-user-manual/511.png)

<span id="_Toc253397864" class="anchor"></span>Figure 147 – Turning on StickyKeys

B.2. FilterKeys

FilterKeys causes Windows to ignore brief or repeated keystrokes and slows down the keyboard repeat rate.

Press down and hold the right-hand \< Shift \> key for eight seconds to toggle FilterKeys on and off:

![](embedded-fragments-version-1-user-manual/512.png)

<span id="_Toc253397865" class="anchor"></span>Figure 148 – Turning On FilterKeys

B.3. ToggleKeys

ToggleKeys causes a tone to sound when you press the \< Caps Lock \>, \< Num Lock \>, or \< Scroll Lock \> keys.

Press down and hold the \< Num Lock \> key for five seconds to turn ToggleKeys on and off:

![](embedded-fragments-version-1-user-manual/513.png)

<span id="_Toc253397866" class="anchor"></span>Figure 149 – Turning On ToggleKeys

B.4. MouseKeys

MouseKeys lets you control the mouse pointer by using the numeric keypad on your keyboard.

Press the left-hand \< Alt \> key plus the left-hand \< Shift \> key plus the \< Num Lock \> key to toggle MouseKeys on and off:

![](embedded-fragments-version-1-user-manual/514.png)

<span id="_Toc253397867" class="anchor"></span>Figure 150 – Turning On MouseKeys

B.5. HighContrast

HighContrast improves readability for people with visual impairments by applying a special system color scheme and font size.

Press the left-hand \< Shift \> key plus the left-hand \< Alt \> key plus the \< Print Screen \> key to toggle HighContrast on and off:

![](embedded-fragments-version-1-user-manual/515.png)

<span id="_Toc253397868" class="anchor"></span>Figure 151 – Turning on HighContrast

2.  <span id="_Toc327881474" class="anchor"></span>Status Indicators

The following table shows the possible status indicators for various kinds of EFRA records.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 33%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th>Record Type</th>
<th>Possible Status Indicators</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="5"><blockquote>
<p>Referral</p>
</blockquote></td>
<td><blockquote>
<p>New</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Accepted</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>In Process</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Completed</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Ineligible</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Lab Kits</p>
</blockquote></td>
<td><blockquote>
<p>New</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Ordered</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Received</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Canceled</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Questionnaires</p>
</blockquote></td>
<td><blockquote>
<p>New</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>In Process</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Completed</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Lab Orders</p>
</blockquote></td>
<td><blockquote>
<p>New</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>In Process</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Completed</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Voided</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Closed</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Lab Results</p>
</blockquote></td>
<td><blockquote>
<p>New</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>In Process</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Accepted</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Interpretation &amp; Diagnosis</p>
</blockquote></td>
<td><blockquote>
<p>New</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>In Process</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Interpreted</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Contact Logs</p>
</blockquote></td>
<td><blockquote>
<p>All Contacts</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

3.  <span id="_Toc245276012" class="anchor"></span>Standard Web Browser Shortcut Keys

In the following table, two or more keys connected by a comma (,) indicate that the keys should be pressed in succession. Keys connected by a plus sign (+) indicate that the keys should be pressed at the same time. These keys can be used while running EFRA in a web browser.

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
<th colspan="2">Browser Option</th>
<th colspan="2">Shortcut</th>
<th>IE</th>
<th>Firefox</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Bookmark (menu)</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; B &gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Bookmark, add for current location</p>
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
<td>*</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Close browser window</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; + &lt; F4 &gt;</p>
</blockquote></td>
<td>*</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Exit browser</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Alt &gt; + &lt; F4 &gt;</p>
</blockquote></td>
<td>*</td>
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
<td>n/a*</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tab, open new</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; Ctrl &gt; + &lt; T &gt;</p>
</blockquote></td>
<td>n/a*</td>
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

4.  <span id="_Toc327881476" class="anchor"></span>VA Approved Internet Browsers

The following [VA](#Glos_VA)-approved browsers have been tested for use with EFRA and are believed to be fully functional. If you encounter unusual problems, please submit a Remedy report and/or consult with your local IRM.

| Browser                      | Version(s)   | Remarks                          |
|------------------------------|--------------|----------------------------------|
| Microsoft® Internet Explorer | 6.0 or later | Does not support tabbed browsing |
| Mozilla® Firefox             | 3.x          | Supports tabbed browsing         |
|                              |              |                                  |
|                              |              |                                  |
|                              |              |                                  |

5.  <span id="_Toc327881477" class="anchor"></span>List of EFR Health Factors

| Health Factor                         | Category           | Comment field? |
|---------------------------------------|--------------------|----------------|
| EF-BLAST SOURCE OTHER                 | EMBEDDED FRAGMENTS | yes            |
| EF-BLAST SOURCE UNKNOWN               | EMBEDDED FRAGMENTS |                |
| EF-BLAST/EXPLOSION INJURY             | EMBEDDED FRAGMENTS |                |
| EF-BULLET INJURY                      | EMBEDDED FRAGMENTS |                |
| EF-CONTACT EMAIL                      | EMBEDDED FRAGMENTS | yes - optional |
| EF-CONTACT NAME                       | EMBEDDED FRAGMENTS | yes            |
| EF-CONTACT PHONE NUMBER               | EMBEDDED FRAGMENTS | yes            |
| EF-ENEMY FIRE                         | EMBEDDED FRAGMENTS |                |
| EF-FRAGMENTS IN BODY                  | EMBEDDED FRAGMENTS |                |
| EF-FRAGMENTS NOT REMOVED IN SURGERY   | EMBEDDED FRAGMENTS |                |
| EF-FRAGMENTS NOT SENT TO LAB          | EMBEDDED FRAGMENTS |                |
| EF-FRAGMENTS ON RADIOGRAPH            | EMBEDDED FRAGMENTS |                |
| EF-FRAGMENTS REMOVED IN SURGERY       | EMBEDDED FRAGMENTS |                |
| EF-FRAGMENTS SENT TO LAB              | EMBEDDED FRAGMENTS |                |
| EF-FRIENDLY FIRE                      | EMBEDDED FRAGMENTS |                |
| EF-GRENADE                            | EMBEDDED FRAGMENTS |                |
| EF-IED                                | EMBEDDED FRAGMENTS |                |
| EF-IN VEHICLE                         | EMBEDDED FRAGMENTS |                |
| EF-LAND MINE                          | EMBEDDED FRAGMENTS |                |
| EF-NO BLAST/EXPLOSION INJURY          | EMBEDDED FRAGMENTS |                |
| EF-NO BULLET INJURY                   | EMBEDDED FRAGMENTS |                |
| EF-NO FRAGMENTS IN BODY               | EMBEDDED FRAGMENTS |                |
| EF-NO FRAGMENTS ON RADIOGRAPH         | EMBEDDED FRAGMENTS |                |
| EF-NOT IN VEHICLE                     | EMBEDDED FRAGMENTS |                |
| EF-REFUSED SCREENING TOOL             | EMBEDDED FRAGMENTS |                |
| EF-RPG                                | EMBEDDED FRAGMENTS |                |
| EF-UNKNOWN IF FRAGMENTS IN BODY       | EMBEDDED FRAGMENTS |                |
| EF-UNKNOWN IF FRAGMENTS ON RADIOGRAPH | EMBEDDED FRAGMENTS |                |
| EF-UNKNOWN IF REMOVED IN SURGERY      | EMBEDDED FRAGMENTS |                |
| EF-UNKNOWN IF SENT TO LAB             | EMBEDDED FRAGMENTS |                |
| SEVERE CHRONIC COGNITIVE IMPAIRMENT   | MENTAL HEALTH      | yes            |
| UNABLE TO SCREEN - ACUTE ILLNESS      | MENTAL HEALTH      | yes            |
| EMBEDDED FRAGMENTS PRESENT            | IRAQ/AFGHANISTAN   | yes - optional |
| NO EMBEDDED FRAGMENTS                 | IRAQ/AFGHANISTAN   |                |

6.  <span id="_Ref266369352" class="anchor"></span>Sample CPRS Screen Shots

The following screen shots illustrate the questionnaire filled out in [CPRS](#Glos_CPRS).

![](embedded-fragments-version-1-user-manual/516.png)

![](embedded-fragments-version-1-user-manual/517.png)

![](embedded-fragments-version-1-user-manual/518.png)

![](embedded-fragments-version-1-user-manual/519.png)

![](embedded-fragments-version-1-user-manual/520.png)

![](embedded-fragments-version-1-user-manual/521.png)

![](embedded-fragments-version-1-user-manual/522.png)

![](embedded-fragments-version-1-user-manual/523.png)

![](embedded-fragments-version-1-user-manual/524.png)

![](embedded-fragments-version-1-user-manual/525.png)

![](embedded-fragments-version-1-user-manual/526.png)

![](embedded-fragments-version-1-user-manual/527.png)

######## Glossary

| [  A  ](#G_A) | [  B  ](#G_B) | [  C  ](#G_C) | [  D  ](#G_D) | [  E  ](#G_E) | [  F  ](#G_F) | [  G  ](#G_G) | [  H  ](#G_H) | [  I  ](#G_I) | [  J  ](#G_J) | [  K  ](#G_K) | [  L  ](#G_L) | [  M  ](#G_M) |
|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
| [  N  ](#G_N) | [  O](#G_O)   | [  P ](#G_P)  | [  Q ](#G_Q)  | [  R  ](#G_R) | [  S  ](#G_S) | [  T  ](#G_T) | [  U  ](#G_U) | [  V  ](#G_V) | [ W ](#G_W)   | [  X  ](#G_X) | Y             | Z             |
| [0-9](#G_09)  |               |               |               |               |               |               |               |               |               |               |               |               |

*Control-click character to see entries; grayed-out character means no entries for that character.*

| Term or Acronym                             |                      |                                | Description |
|---------------------------------------------|----------------------|--------------------------------|-------------|
| <span id="G_09" class="anchor"></span>0 - 9 |                      |                                |             |
| 508                                         |                      | *See* [Section 508](#Glos_508) |             |
| [ BACK ](#glossary)                     | to Glossary Contents |                                |             |

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
<td colspan="4"><span id="G_A" class="anchor"></span>A</td>
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
<td colspan="2">AD is a technology created by Microsoft that provides a variety of network services, including user authentication. For EFRA, AD essentially keeps track of who the users are and what EFRA functions they are authorized to perform.</td>
</tr>
<tr class="even">
<td colspan="3">Active Dual Consumer</td>
<td colspan="2">A beneficiary who has received or can potentially receive health care from the <a href="#Glos_DoD">Department of Defense (DoD)</a> and/or <a href="#Glos_VA">Department of Veterans Affairs (VA).</a> An ADC beneficiary can be considered as Dual <strong>Eligible</strong> or Dual <strong>User,</strong> or both.</td>
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
<p>Chemistry, Pharmacology. comprising a known fraction of a whole and constituting a sample: an aliquot quantity of acid for analysis. As a noun: <em>an aliquot part</em>.</p></td>
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
<td colspan="3"><span id="G_B" class="anchor"></span>B</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_backend" class="anchor"></span>back-end</td>
<td>Any software or system which performs either the final stage in a process, or a task not apparent to the user.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_BVAMC" class="anchor"></span>Baltimore Veterans Affairs Medical Center (BVAMC)</td>
<td>The BVAMC is home to the <a href="#Glos_TEFSC">Toxic Embedded Fragment Surveillance Center</a> (<a href="#Glos_TEFSC">TEFSC</a>)</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_Browser" class="anchor"></span>browser</td>
<td><p>A program which allows a person to read <a href="#Glos_hypertext">hypertext</a>. The browser provides some means of viewing the contents of nodes (or "pages") and of navigating from one node to another. A browser is required in order to access the EFRA software application.</p>
<p>Microsoft® Internet Explorer and Firefox are examples for browsers for the World-Wide Web. They act as clients to remote web servers.</p></td>
</tr>
<tr class="odd">
<td colspan="2">BVAMC</td>
<td><em>See</em> Baltimore Veterans Affairs Medical Center</td>
</tr>
<tr class="even">
<td colspan="2">Biomonitoring (or Biological Monitoring)</td>
<td>Process of assessing and measuring clinical response to toxins introduced into the body as a result of embedded fragment trauma. Specimens are collected and sent to a laboratory to establish baseline levels of analytes. The process of collection and analysis is then repeated periodically to develop a <a href="#Glos_Longitudinal">longitudinal</a> assessment for diagnosis, corrective treatment and prognosis.</td>
</tr>
<tr class="odd">
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
<td colspan="3"><span id="G_C" class="anchor"></span>C</td>
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
<td>CQM, based in the VA Palo Alto Health Care System, functions as part of the VA Public Health Strategic Health Care Group at VA Central Office in Washington, DC. CQM was first established with a primary focus on HIV care; the mission expanded to include Hepatitis C issues in January 2001. In line with the mission of its organizational parent, the CQM mission further expanded to include work on various issues and conditions with public health significance, including operational support and management of data from the EFRA.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CDC" class="anchor"></span>Centers for Disease Control and Prevention (CDC)</td>
<td><p>The CDC is one of the major operating components of the United States Department of Health and Human Services. It includes a number of Coordinating Centers and Offices which specialize in various aspects of public health, as well as the National Institute for Occupational Safety and Health (NIOSH).</p>
<p><em>See</em> <a href="http://www.cdc.gov/about/organization/cio.htm">http://www.cdc.gov/about/organization/cio.htm</a></p></td>
</tr>
<tr class="even">
<td colspan="2">Chain of Custody</td>
<td>Chain of custody refers to the chronological documentation, and/or "paper trail," showing the custody, control, transfer, analysis, and disposition of specimens, whether physical or electronic. A chain of custody form is used to document these events for biological monitoring and fragment analysis kit tracking in the EFR application.</td>
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
<td colspan="2"><span id="Glos_ClinicalReminder" class="anchor"></span>Clinical Reminder</td>
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
<p>Context-sensitive help is most used in, but is not limited to, <a href="http://en.wikipedia.org/wiki/GUI">GUI</a> environments. Examples are <a href="http://en.wikipedia.org/wiki/Microsoft">Microsoft's</a> <a href="http://en.wikipedia.org/wiki/Windows_Help">WinHelp</a>, <a href="http://en.wikipedia.org/wiki/Sun_Microsystems">Sun's</a> <a href="http://en.wikipedia.org/wiki/JavaHelp">JavaHelp</a> or Panviva's <a href="http://www.supportpoint.com/">SupportPoint</a>.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CDCO" class="anchor"></span>Corporate Data Center Operations (CDCO)</td>
<td><p>Federal data center within the Department of Veterans Affairs (VA). As a franchise fund, or fee-for-service organization, CDCO-Austin provides cost-efficient IT enterprise solutions to support the information technology needs of customers within the Federal sector. <em>Formerly</em> the Austin Automation Center (AAC); <em>formerly</em> the Austin Information Technology Center (AITC).</p>
<p><em>See</em> <a href="http://www.aac.va.gov/index.php">http://www.aac.va.gov/index.php</a>.</p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CDW" class="anchor"></span>Corporate Data Warehouse (CDW)</td>
<td><p>CDW is a national repository comprising data from several <a href="#Glos_VHA">Veterans Health Administration (VHA)</a> clinical and administrative systems. The CDW’s objective is to provide data and tools to support management decision making, performance measurement and research objectives. Its premise is that incorporating data from multiple differing data sets throughout the VHA into one standard database structure will facilitate reporting and data analysis at the enterprise level. The CDW operates within the VA Office of Information &amp; Technology’s Field Operations Business Intelligence Service Line.</p>
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

| Term or Acronym                                                                          |                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="G_D" class="anchor"></span>D                                                   |                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Data Dictionary                                                                          |                      | A data structure that stores meta-data, *i.e.,* data about data. The term “data dictionary” has several uses; most generally it is thought of as a set of data Descriptions that can be shared by several applications. In practical terms, it usually means a table in a database that stores the names, field types, length, and other characteristics of the fields in the database tables.                                                                                                                                                                |
| Data Transfer Agreement (DTA)                                                            |                      | Agreement between two or more VA departments, or between a VA department and an outside agency. DTAs cover transfers of data or information between agencies or departments in order to maintain appropriate administrative, technical and physical security safeguards to prevent unauthorized use and to protect the confidentiality of the data.                                                                                                                                                                                                           |
| <span id="Glos_DataWarehouse" class="anchor"></span>Data Warehouse                       |                      | A system for storing, retrieving and managing large amounts of data. Data warehouse software often includes sophisticated compression and hashing techniques for fast searches, as well as advanced filtering. A data warehouse is often a relational database containing a recent snapshot of corporate data and optimized for searching. Planners and researchers can use this database without worrying about slowing down day-to-day operations of the production database. The latter can be optimized for transaction processing (inserts and updates). |
| Decentralized Hospital Computer Program (DHCP)                                           |                      | Obsolete term; [VistA](#Glos_VistA) is the modern equivalent                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Defense Health Information Management System (DHIMS)                                     |                      | System designed to provide a trusted, comprehensive health information management system that seamlessly captures, manages and shares health information from the Theater of Operations to the home front and beyond. This is, roughly, the [DoD](#Glos_DoD) equivalent of [CPRS](#Glos_CPRS).                                                                                                                                                                                                                                                                |
| <span id="Glos_DVEIR" class="anchor"></span>Defense/Veterans Eye Injury Registry (DVEIR) |                      | DVEIR helps identify and document treatment of all [OEF](#Glos_OEF)/[OIF](#Glos_OIF) service members with ocular injuries. Since eye injuries frequently result from fragments, there is a relationship between the two Registries… but not between the two applications.                                                                                                                                                                                                                                                                                     |
| <span id="Glos_DoD" class="anchor"></span>Department of Defense (DoD)                    |                      | A department of the U.S. federal government, charged with ensuring that the military capacity of the U.S. is adequate to safeguard the national security.                                                                                                                                                                                                                                                                                                                                                                                                     |
| DHCP                                                                                     |                      | Decentralized Hospital Computer Program (obsolete term; [VistA](#Glos_VistA) is the modern equivalent)                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DHIMS                                                                                    |                      | *See* Defense Health Information Management System                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DoD                                                                                      |                      | *See* [Department of Defense](#Glos_DoD)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DTA                                                                                      |                      | *See* Data Transfer Agreement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Dual Consumer                                                                            |                      | A patient who is eligible for health care under [DoD](#Glos_DoD) and VA health plans, or who has been assigned to a joint venture site and meets the requirements under a DoD/VA sharing agreement for coverage of specified clinical services.                                                                                                                                                                                                                                                                                                               |
| Dual User                                                                                |                      | A patient who has received care at both a [DoD](#Glos_DoD) facility and a VA facility. Dual users are a subset population of Active Dual Consumers.                                                                                                                                                                                                                                                                                                                                                                                                           |
| DVEIR                                                                                    |                      | *See* [Defense/Veterans Eye Injury Registry](#Glos_DVEIR)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [ BACK ](#glossary)                                                                  | to Glossary Contents |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 79%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_E" class="anchor"></span>E</td>
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
<td colspan="2"><span id="Glos_EMFR" class="anchor"></span>Embedded Metal Fragments Registry (EMFR)</td>
<td colspan="2"><a href="#Glos_DoD">DoD</a> system for tracking information relevant to injuries associated with embedded metal fragments.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_EMFR_DataExtract" class="anchor"></span>Embedded Metal Fragments Registry (EMFR) data extract</td>
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
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_F" class="anchor"></span>F</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_FRC" class="anchor"></span>Federal Recovery Coordinator (FRC)</td>
<td colspan="2"><p>FRCs help severely injured combat Veterans and their families maneuver through military and Veterans’ treatment and benefits programs.</p>
<p>There are 14 Federal Recovery Coordinators responsible for fewer than 300 cases of the most severely injured combat Veterans who face complicated treatment and recovery plans.</p></td>
</tr>
<tr class="odd">
<td colspan="2">FHP&amp;R</td>
<td colspan="2"><em>See</em> <a href="#Glos_OFHPR">Office of Force Health Protection and Readiness</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_FTP" class="anchor"></span>File Transfer Protocol (FTP)</td>
<td colspan="2">A client-server protocol which allows a user on one computer to transfer files to and from another computer over a TCP/IP network. Also the client program the user executes to transfer files. It is defined in STD 9, RFC 959.</td>
</tr>
<tr class="odd">
<td colspan="2">Firewall</td>
<td colspan="2">A firewall is a part of a computer system or network that is designed to block unauthorized access while permitting authorized communications. It is a device or set of devices configured to permit, deny, encrypt, decrypt, or proxy all (in and out) computer traffic between different security domains based upon a set of rules and other criteria.</td>
</tr>
<tr class="even">
<td colspan="2">Fragment</td>
<td colspan="2">Any piece of material that is or has been embedded in the body as a result of injury. Also known as shrapnel.</td>
</tr>
<tr class="odd">
<td colspan="2">FRC</td>
<td colspan="2"><em>See</em> <a href="#Glos_FRC">Federal Recovery Coordinator</a></td>
</tr>
<tr class="even">
<td colspan="2">FTP</td>
<td colspan="2"><em>See</em> <a href="#Glos_FTP">File Transfer Protocol</a></td>
</tr>
<tr class="odd">
<td colspan="2">Function key</td>
<td colspan="2">A key on a computer or terminal keyboard which can be programmed so as to cause an operating system command interpreter or application program to perform certain actions. On some keyboards/computers, function keys may have default actions, accessible on power-on. For example, &lt;F1&gt; is traditionally the function key used to activate a help system.</td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_G" class="anchor"></span>G</td>
</tr>
<tr class="even">
<td colspan="2">Global War On Terror (GWOT)</td>
<td colspan="2"><em>Obsolete term; see</em> <a href="#Glos_OCO">Overseas Contingency Operation</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_GUI" class="anchor"></span>Graphical User Interface (GUI)</td>
<td colspan="2"><p>A graphical user interface (or GUI, often pronounced “gooey”) is a graphical (rather than purely textual) user interface to a computer. A GUI is a particular case of user interface for interacting with a computer which employs graphical images and widgets in addition to text to represent the information and actions available to the user. Usually the actions are performed through direct manipulation of the graphical elements. A GUI takes advantage of the computer’s graphics capabilities to make the program easier to use.</p>
<p><em>Sources:</em></p>
<p><a href="http://en.wikipedia.org/wiki/GUI">http://en.wikipedia.org/wiki/GUI</a></p>
<p><a href="http://www.webopedia.com/TERM/G/Graphical_User_Interface_GUI.html">http://www.webopedia.com/TERM/G/Graphical_User_Interface_GUI.html</a></p>
<p><em>See also</em> <a href="#Glos_UserInterface">User Interface</a></p></td>
</tr>
<tr class="even">
<td colspan="2">GUI</td>
<td colspan="2"><em>See:</em> <a href="#Glos_GUI">Graphical User Interface</a></td>
</tr>
<tr class="odd">
<td colspan="2">GWOT</td>
<td colspan="2">Global War On Terror (<em>obsolete term; see</em> Overseas Contingency Operation).</td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 80%" />
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
<td colspan="5"><span id="G_H" class="anchor"></span>H</td>
</tr>
<tr class="even">
<td colspan="2">HTML</td>
<td colspan="3"><em>See</em> <a href="#Glos_HTML">Hypertext Mark-up Language</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_hypertext" class="anchor"></span>hypertext</td>
<td colspan="3">A term coined around 1965 for a collection of documents (or "nodes") containing cross-references or "links" which, with the aid of an interactive browser program, allow the reader to move easily from one document to another.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HTML" class="anchor"></span>Hypertext Mark-up Language (HTML)</td>
<td colspan="3">A <a href="#Glos_hypertext">hypertext</a> document format used on the World-Wide Web. HTML is built on top of <a href="#Glos_SGML">SGML</a>. "Tags" are embedded in the text. A tag consists of a "&lt;", a "directive" (in lower case), zero or more parameters and a "&gt;". Matched pairs of directives, like "&lt;title&gt;" and "&lt;/title&gt;" are used to delimit text which is to appear in a special place or style.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_HAIG" class="anchor"></span>Healthcare Analysis &amp; Information Group (HAIG)</td>
<td colspan="3">A field unit of Clinical Affairs and Information Management in Milwaukee, WI. Functions as a provider of information syntheses, analyses, report formatting, and dissemination of many types of information and tools in support of national policies, strategic planning and decision-making processes. HAIG develops corporate reports, proceedings, analyses, and disseminates information through the use of state-of-the art technology including survey design, statistical analysis, customized publications, web design/management, and advanced computer applications.</td>
</tr>
<tr class="even">
<td colspan="2">HAIG</td>
<td colspan="3"><em>See</em> <a href="#Glos_HAIG">Healthcare Analysis &amp; Information Group</a></td>
</tr>
<tr class="odd">
<td colspan="2">HAIISS</td>
<td colspan="3"><em>See</em> <a href="#Glos_HAIISS">Healthcare Associated Infection and Influenza Surveillance System</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HAIISS" class="anchor"></span>Healthcare Associated Infection and Influenza Surveillance System (HAIISS)</td>
<td colspan="3">VHA is seeking to leverage its advanced electronic medical records to establish a comprehensive electronic surveillance system for monitoring healthcare-associated infections and antibiotic resistance trends, as well as influenza and other emerging infectious diseases or syndromes potentially associated with bioterrorist activity. This project is now being merged with the project known as Electronic Surveillance System for the Early Notification of Community-based Epidemics (ESSENCE) and will be managed separately from the Registries projects.</td>
</tr>
<tr class="odd">
<td colspan="2">HDR</td>
<td colspan="3">Health Data Repository</td>
</tr>
<tr class="even">
<td colspan="2">HDS</td>
<td colspan="3">Health Data Systems</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_HealthFactor" class="anchor"></span>Health Factor</td>
<td colspan="3">A health factor is a computerized component that captures patient information that for which no standard code exists, such as Family History of Alcohol Abuse, Lifetime Non-smoker, No Risk Factors for Hepatitis C, etc. See also, Clinical Reminders.</td>
</tr>
<tr class="even">
<td colspan="2"><a href="http://www.himss.org">HIMSS</a></td>
<td colspan="3"><em>See</em> <a href="#Glos_HIMSS">Healthcare Information and Management Systems Society</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_HIMSS" class="anchor"></span>Healthcare Information and Management Systems Society (HIMSS)</td>
<td colspan="3">HIMSS is a healthcare-stakeholder membership organization exclusively focused on providing global leadership for the optimal use of information technology (IT) and management systems for the betterment of healthcare.</td>
</tr>
<tr class="even">
<td colspan="2">HIV</td>
<td colspan="3"><em>See</em> Human Immunodeficiency Virus</td>
</tr>
<tr class="odd">
<td colspan="2">Human Immunodeficiency Virus (HIV)</td>
<td colspan="3"><p>HIV is a lentivirus (a member of the retrovirus family) that can lead to acquired immunodeficiency syndrome (AIDS), a condition in humans in which the immune system begins to fail, leading to life-threatening opportunistic infections. HIV is different from most other viruses because it attacks the immune system. The immune system gives our bodies the ability to fight infections. HIV finds and destroys a type of white blood cell (T cells or CD4 cells) that the immune system must have to fight disease.</p>
<p>See <a href="http://www.cdc.gov/hiv/topics/basic/index.htm">http://www.cdc.gov/hiv/topics/basic/index.htm</a>.</p></td>
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
<td colspan="4"><span id="G_I" class="anchor"></span>I</td>
</tr>
<tr class="even">
<td colspan="2">ICD-9</td>
<td colspan="2"><em>See</em> <a href="#Glos_ICD9">International Statistical Classification of Diseases and Related Health Problems</a></td>
</tr>
<tr class="odd">
<td colspan="2">ICN</td>
<td colspan="2"><em>See</em> <a href="#Glos_ICN">Integration Control Number</a></td>
</tr>
<tr class="even">
<td colspan="2">IDMC</td>
<td colspan="2"><em>See</em> <a href="#Glos_IDMC">Information and Data Management Committee</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_IDMC" class="anchor"></span>Information and Data Management Committee (IDMC)</td>
<td colspan="2">IDMC is the advisory group to the Under Secretary for Health through the National Leadership Board (NLB) on Information Technology (IT) issues. The IDMC membership is comprised of a cross section of Veterans Health Administration (VHA) leadership representing VHA health care programs and operations, and helps ensure IT investments support corporate goals. The IDMC works collaboratively with other committees and groups concerned with IT-related issues.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_IRM" class="anchor"></span>Information Resources Management (IRM)</td>
<td colspan="2">The service which is involved in planning, budgeting, procurement and management-in-use of VA's information technology investments.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_IT" class="anchor"></span>Information Technology (IT)</td>
<td colspan="2">Refers to applied computer systems (both hardware and software), and often including networking and telecommunications, usually in the context of a business or other enterprise. Often the name of the part of an enterprise that deals with all things electronic.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_ICN" class="anchor"></span>Integration Control Number (ICN)</td>
<td colspan="2">The national VA patient record number.</td>
</tr>
<tr class="odd">
<td colspan="2">Interface</td>
<td colspan="2">An interface defines the communication boundary between two entities, such as a piece of software, a hardware device, or a user.</td>
</tr>
<tr class="even">
<td colspan="2">Interim Solution</td>
<td colspan="2">Temporary registry solution being developed by the VSSC; includes referral page, application for TEFSC, and a Structured Query Language (SQL) Database (DB). This interim solution is under consideration for delivery. The development of EFRA, as described in this document, envisions a more mature product to replace the interim solution.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ICD9" class="anchor"></span>International Statistical Classification of Diseases and Related Health Problems (ICD-9)</td>
<td colspan="2"><p>The <em>International Statistical Classification of Diseases and Related Health Problems</em>, Ninth Edition (commonly abbreviated as “ICD-9”) provides numeric codes to classify diseases and a wide variety of signs, symptoms, abnormal findings, complaints, social circumstances and external causes of injury or disease. Every health condition can be assigned to a unique category and given a code, up to six characters long. Such categories can include a set of similar diseases. The “-9” refers to the ninth edition of these codes; the tenth edition has been published, but is not in widespread use at this time.</p>
<p><em>See also</em> <a href="#Glos_CPT">Current Procedural Terminology</a></p></td>
</tr>
<tr class="even">
<td colspan="2">Interpreted Lab Results</td>
<td colspan="2">Lab results from either the Baltimore VAMC laboratory or from the AFIP laboratory that have been reviewed and interpreted by a TEFSC Provider.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_Intranet" class="anchor"></span>intranet</td>
<td colspan="2">Any network which provides similar services within an organization to those provided by the Internet outside it, but which is not necessarily connected to the Internet. The commonest example is the use by a company of one or more World-Wide Web servers on an internal TCP/IP network for distribution of information within the company. The VA intranet hosts EFRA as well as other programs and information.</td>
</tr>
<tr class="even">
<td colspan="2">IRM</td>
<td colspan="2"><em>See</em> <a href="#Glos_IRM">Information Resources Management</a></td>
</tr>
<tr class="odd">
<td colspan="2">IT</td>
<td colspan="2"><em>See</em> <a href="#Glos_IT">Information Technology</a></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
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
<td colspan="4"><span id="G_J" class="anchor"></span>J</td>
</tr>
<tr class="even">
<td colspan="2">JAWS</td>
<td colspan="2"><em>See</em> <a href="#Glos_JAWS">Job Access with Speech</a></td>
</tr>
<tr class="odd">
<td colspan="2">Job Access with Speech (JAWS)</td>
<td colspan="2">Refers to a software product for visually impaired users. The software is produced by the Blind and Low Vision Group of Freedom Scientific. See <a href="http://en.wikipedia.org/wiki/JAWS_%28screen_reader%29">http://en.wikipedia.org/wiki/JAWS_%28screen_reader%29</a> and <a href="http://www.freedomscientific.com/fs_products/software_jaws.asp">http://www.freedomscientific.com/fs_products/software_jaws.asp</a>.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_JMeWS" class="anchor"></span>Joint Medical Workstation (JMeWS)</td>
<td colspan="2">Military commanders need to have online, near-real-time medical situational awareness for forward-deployed forces during Operation Iraqi Freedom (OIF). JMeWS provides that capability. Like <a href="#Glos_AHLTA">AHLTA</a>-T and JPTA, JMeWS is an integral part of the TMIP-J capability.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_JTPA" class="anchor"></span>Joint Patient Tracking Application (JPTA)</td>
<td colspan="2">JTPA tracks the location and disposition of ill or injured patients as they move through the echelons of care, from the U.S. Central Command theater of operations, to Landstuhl Regional Medical Center and back to selected Military Health System or Department of Veterans Affairs medical facilities in the U.S.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_JTTS" class="anchor"></span>Joint Theater Trauma System (JTTS)</td>
<td colspan="2"><p>JTTS is an approach to providing improved trauma care across the continuum of the Levels of Care to trauma patients, especially in the battlefield environment. Its mission is to:</p>
<p>- Establish and maintain a Department of Defense Trauma Registry System to capture data and provide information on care and outcomes of military and civilian trauma patients.</p>
<p>- Provide the Department of Defense and other authorized interests with timely and relevant information about care and outcomes of military and civilian injuries.</p>
<p>- Create a research strategy that supports reduction of morbidity and mortality in military and civilian trauma patients.</p>
<p>- Establish and maintain a trauma outcomes database to analyze and evaluate clinical decision making and measure subsequent outcomes for improving treatment modalities.</p>
<p>- Provide activities of each of the services with full and complete access to data resident in the <a href="#Glos_DoD">DoD</a> Trauma Registry.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_JTTR" class="anchor"></span>Joint Theatre Trauma Registry (JTTR)</td>
<td colspan="2"><p>JTTR is the <a href="#Glos_DoD">DoD</a>'s data repository collecting and hosting all trauma related data. Sited at Fort Sam Houston, Texas, helps track casualty information from Iraq and Afghanistan to give senior leaders the concrete information they need as they make decisions about everything from what protective gear troops will use to how to better deliver combat casualty care. JTTR also helps ensure that decision makers have more than anecdotal evidence to guide their decisions that directly affect troops on the ground.</p>
<p>The Registry captures details about wounds received and the medical care provided from combat support hospitals, aboard ships and aircraft and throughout the course of their treatment, as well as the results. This shows medical care providers what treatments were most effective as they apply those lessons learned to other patients with similar wounds. Medical care providers call this the most important stage of the patient's treatment and ultimate recovery. The Registry also helps medical instructors better tailor their training for the theater.</p>
<p>Providing more information and speeding up its delivery is a slow, labor-intensive process that involves sorting through files of hand-written notes from weary battlefield healthcare providers, extracting the critical details, translating them into medical codes and entering them into the database. Nevertheless, the database is providing combat trauma care information which was never before available, and certainly not while the war was still under way. In the past, medical data from the theater was never collected, and inpatient records were retired to the National Personnel Records Center in St. Louis as soon as each patient left the hospital.</p>
<p>NOTE: JTTR data can only be shared with government entities.</p></td>
</tr>
<tr class="even">
<td colspan="2">JPTA</td>
<td colspan="2"><em>See</em> <a href="#Glos_JTPA">Joint Patient Tracking Application</a></td>
</tr>
<tr class="odd">
<td colspan="2">JTTR</td>
<td colspan="2"><em>See</em> <a href="#Glos_JTTR">Joint Theatre Trauma Registry</a></td>
</tr>
<tr class="even">
<td colspan="2">JTTS</td>
<td colspan="2"><em>See</em> <a href="#Glos_JTTS">Joint Theater Trauma System</a></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
</tr>
</tbody>
</table>

| Term or Acronym                        |                      |                                                                                                                                                 | Description |
|----------------------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| <span id="G_K" class="anchor"></span>K |                      |                                                                                                                                                 |             |
| Kit                                    |                      | Medical supplies used to collect specimens or fragments. Also referred to as specimen collection kit or fragment collection kit as appropriate. |             |
| [ BACK ](#glossary)                | to Glossary Contents |                                                                                                                                                 |             |

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
<td colspan="4"><span id="G_L" class="anchor"></span>L</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_Longitudinal" class="anchor"></span>Longitudinal</td>
<td colspan="2">Occurring over a period of time.</td>
</tr>
<tr class="odd">
<td colspan="2">Laboratory Information Manager (LIM)</td>
<td colspan="2">Manager of the laboratory files in <a href="#Glos_VistA">VistA</a>. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other <a href="#Glos_CPRS">Computerized Patient Record System</a> functions.</td>
</tr>
<tr class="even">
<td colspan="2">Local Registry</td>
<td colspan="2">The local file of patients that were grandfathered into the Registry or have passed the selection rules and been added to the Registry.</td>
</tr>
<tr class="odd">
<td colspan="2">Local Registry Update</td>
<td colspan="2">This process adds new patients (that have had data entered since the last update was run and pass the selection rules) to the local Registry.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_LOINC" class="anchor"></span>Logical Observation Identifiers Names and Codes (LOINC)</td>
<td colspan="2"><p>LOINC<sup>©</sup> is designed to facilitate the exchange and pooling of clinical results for clinical care, outcomes management, and research by providing a set of universal codes and names to identify laboratory and other clinical observations. The Regenstrief Institute, Inc., an internationally renowned healthcare and informatics research organization, maintains the LOINC database and supporting documentation.</p>
<p><em>See</em> <a href="http://loinc.org/">http://loinc.org/</a></p></td>
</tr>
<tr class="odd">
<td colspan="2">LOINC</td>
<td colspan="2"><em>See</em> <a href="#Glos_LOINC">Logical Observation Identifiers Names and Codes</a></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
</tr>
</tbody>
</table>

| Term or Acronym                                                                         |                      |                                                                                                                                                                                                    | Description |
|-----------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| <span id="G_M" class="anchor"></span>M                                                  |                      |                                                                                                                                                                                                    |             |
| Medical SAS Datasets                                                                    |                      | The VHA Medical SAS Datasets are national administrative data for VHA-provided health care utilized primarily by Veterans, but also by some non-Veterans (e.g., employees, research participants). |             |
| <span id="Glos_MEVIR" class="anchor"></span>Military Eye/Vision Injury Registry (MEVIR) |                      | <span class="mark">\[???\] \[CANNOT FIND ANY REFERENCE TO THIS ON THE Military Health System website ([www.health.mil](http://www.health.mil)). IS IT OBSOLETE?\]</span>                           |             |
| MTFs                                                                                    |                      | *Acronym for* Medical Treatment Facilities                                                                                                                                                         |             |
| [ BACK ](#glossary)                                                                 | to Glossary Contents |                                                                                                                                                                                                    |             |

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
<td colspan="4"><span id="G_N" class="anchor"></span>N</td>
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
<td>All sites running the EFRA software transmit their data to the central database for the Registry.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">National Data Service (NDS)</td>
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
<td><mark>[???]</mark></td>
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

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Term or Acronym</td>
<td>Description</td>
</tr>
<tr class="even">
<td colspan="3"><span id="G_O" class="anchor"></span>O</td>
</tr>
<tr class="odd">
<td colspan="2">OCO</td>
<td><em>See</em> <a href="#Glos_OCO">Overseas Contingency Operation</a></td>
</tr>
<tr class="even">
<td colspan="2">OEF/OIF</td>
<td>See <a href="#Glos_OEF">Operation Enduring Freedom</a> <em>and</em> Operation Iraqi Freedom.</td>
</tr>
<tr class="odd">
<td colspan="2">OEF/OIF Clinical Reminder</td>
<td><p>A clinical reminder designed to assist in screening candidates for the Embedded Fragment Registry. The clinical reminder consists of a questionnaire targeted at identifying health factors pertaining to EFR:</p>
<p>Afghan and Iraq Post-Deployment Screen<br />
EMBEDDED FRAGMENTS PRESENT<br />
NO EMBEDDED FRAGMENTS</p></td>
</tr>
<tr class="even">
<td colspan="2">OEF/OIF Coordinators and Case Managers</td>
<td>Each VA Medical Center has an OEF/OIF case management team, consisting of a nurse or social worker program manager leading the program; a nurse or social worker case manager providing clinical case management services; and a transition patient advocate acting as an ombudsman for the patient and family. The OEF/OIF Coordinators and Case Managers may initiate the referral to the EFR and need to be aware of the TEFSC protocols; however, they will not need access to the Registry. <em>See also</em> <a href="#Glos_OEF">Operation Enduring Freedom</a> <em>and</em> Operation Iraqi Freedom.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_OFHPR" class="anchor"></span>Office of Force Health Protection and Readiness (OFHPR)</td>
<td>OFHPR serves as the principal staff assistant and advisor to the Assistant Secretary of Defense (Health Affairs) for all <a href="#Glos_DoD">DoD</a> deployment medicine policies, programs, and activities. In carrying out these responsibilities the office is responsible for deployment related health policy, doctrine, theater information systems, system rightsizing, and international agreements.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_OIT" class="anchor"></span>Office of Information and Technology (OI&amp;T)</td>
<td>Delivers available, adaptable, secure, and cost effective technology services; supports the goal of delivering world-class service to veterans and their families through effective communication and management of people, technology, business processes and financial processes.</td>
</tr>
<tr class="odd">
<td colspan="2">OPCS</td>
<td><em>See</em> <a href="#Glos_PCS">Patient Care Services</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_OEF" class="anchor"></span>Operation Enduring Freedom (OEF)</td>
<td>Military operation in Afghanistan and Iraq. Used mostly in conjunction with Operation Iraqi Freedom, which refers to another similar operation.</td>
</tr>
<tr class="odd">
<td colspan="2">OIF</td>
<td><em>See</em> Operation Iraqi Freedom</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_OIF" class="anchor"></span>Operation Iraqi Freedom (OIF)</td>
<td>Military operation in Afghanistan and Iraq. Used mostly in conjunction with <a href="#Glos_OEF">Operation Enduring Freedom</a>, which refers to another similar operation.</td>
</tr>
<tr class="odd">
<td colspan="2">OEF</td>
<td><em>See</em> <a href="#Glos_OEF">Operation Enduring Freedom</a>. <em>See also</em> Operation Iraqi Freedom</td>
</tr>
<tr class="even">
<td colspan="2">OEF/OIF</td>
<td><em>See</em> <a href="#Glos_OEF">Operation Enduring Freedom</a> <em>and</em> Operation Iraqi Freedom.</td>
</tr>
<tr class="odd">
<td colspan="2">OI&amp;T</td>
<td><em>See</em> <a href="#Glos_OIT">Office of Information and Technology</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_OCO" class="anchor"></span>Overseas Contingency Operation (OCO)</td>
<td>Term used to replace the terms Global War on Terror (GWOT) and "Long War." Per direction from the Office of Management and Budget (OMB) through the VA Communications Division, the terms <em>GWOT</em> and <em>Long War</em> are no longer to be used and are being replaced with <em>Overseas Contingency Operation</em>.</td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="2">to Glossary Contents</td>
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
<td colspan="4"><span id="G_P" class="anchor"></span>P</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_PCS" class="anchor"></span>Patient Care Services, Office of (OPCS)</td>
<td colspan="2">OPCS oversees VHA's clinical programs that support and improve Veterans' health care. The VA's broad approach to Veteran care incorporates expert knowledge, clinical practice and patient care guidelines in all aspects of care.</td>
</tr>
<tr class="odd">
<td colspan="2">PDF</td>
<td colspan="2"><em>See</em> <a href="#Glos_PDF">Portable Document Format</a></td>
</tr>
<tr class="even">
<td colspan="2">PCS</td>
<td colspan="2"><em>See</em> <a href="#Glos_PCS">Patient Care Services</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_PII" class="anchor"></span>Personally Identifiable Information (PII)</td>
<td colspan="2">PII refers to information that can be used to uniquely identify, contact, or locate a single person or can be used with other sources to uniquely identify a single individual.</td>
</tr>
<tr class="even">
<td colspan="2">PII</td>
<td colspan="2"><em>See</em> <a href="#Glos_PII">Personally Identifiable Information</a></td>
</tr>
<tr class="odd">
<td colspan="2">PMO</td>
<td colspan="2"><em>See</em> <a href="#Glos_PMO">Program Management Office</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_PDF" class="anchor"></span>Portable Document Format (PDF)</td>
<td colspan="2">A file format for representing documents in a manner that is independent of the original application software, hardware, and operating system used to create those documents. A PDF file can describe documents containing any combination of text, graphics, and images in a device-independent and resolution independent format.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_PMO" class="anchor"></span>Program Management Office (PMO)</td>
<td colspan="2"><p><mark>[???]</mark></p>
<p><mark>[DOES THIS REFER TO THE VHA PMO, THE VA PMO, OR WHAT?]</mark></p></td>
</tr>
<tr class="even">
<td colspan="2">Protocol</td>
<td colspan="2">A protocol is a convention or standard that controls or enables the connection, communication, and data transfer between two computing endpoints. In its simplest form, a protocol can be defined as the rules governing the syntax, semantics, and synchronization of communication. Protocols may be implemented by hardware, software, or a combination of the two.</td>
</tr>
<tr class="odd">
<td colspan="2">Provider</td>
<td colspan="2">An organization or individual who delivers health care in a professional, systematic way to any individual in need of health care services. For purposes of the EFR project, Providers will be considered as individual health care practitioners. Providers coordinate health care of patients that are included in EFRA.</td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_Q" class="anchor"></span>Q</td>
</tr>
<tr class="even">
<td colspan="2">questionnaire</td>
<td colspan="2"><p><mark>[???] [NEED GOOD DEFINITION OF JUST WHAT A QUESTIONNAIRE IS]</mark></p>
<p><mark>See also</mark></p></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
</tr>
</tbody>
</table>

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
<td colspan="4"><span id="G_R" class="anchor"></span>R</td>
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
<td colspan="2">The term <em>read only</em> usually refers to something that can be read, but not written to or modified. In programming, a data variable can be declared as RO, which prevents modification to the values. In EFRA, this applies specifically to several categories of data, including basic information about a patient.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_RCB" class="anchor"></span>Recognized Certification Body (RCB)</td>
<td colspan="2">The certification of electronic health record software is recognized to be a two part process: (1) the Secretary of the Department Health and Human Services (the Secretary) recognizing specific enumerated criteria for the certification of electronic health record (EHR) software, and (2) certification to the criteria and standards so recognized by the Secretary. An organization/entity recognized to carry out the second step of this process is referred to as a Recognized Certification Body (RCB).</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Referral</td>
<td colspan="2">To send or direct for treatment, aid, information, or decision. For the purposes of the EFR application, a referral may also mean the data sent to identify a patient being referred.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Registry</td>
<td colspan="2"><p>The VHA Registries Program supports the population-specific data needs of the enterprise including (but not limited to) the <a href="#Glos_CCR">Defense/Veterans Eye Injury Registry</a>, Oncology Tumor Registry, Traumatic Brain Injury Registry, Embedded Fragment Registry and Eye Trauma Registry.</p>
<p><em>Also,</em> a database containing a collection of data relating to a disease or condition.</p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">RO</td>
<td colspan="2"><em>See</em> <a href="#Glos_RO">read only</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Roll-and-scroll, roll’n’scroll</td>
<td colspan="2">“Scrolling” is a display framing technique that allows the user to view a display as moving behind a fixed frame. The scrolling action typically causes the data displayed at one end of the screen to move across it, toward the opposite end. When the data reach the opposite edge of the screen they are removed (i.e., scroll off of the screen). Thus, old data are removed from one end while new data are added at the other. This creates the impression of the display page being on an unwinding scroll, with only a limited portion being visible at any time from the screen; i.e., the display screen is perceived as being stationary while the displayed material moves (scrolls) behind it. Displays may be scrolled in the top-bottom direction, the left-right direction, or both. Traditionally, <a href="#Glos_VistA">VistA</a> data displays have been referred to as “roll-and-scroll” for this reason.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Routine</td>
<td colspan="2">A set of programming instructions designed to perform a specific limited task.</td>
<td></td>
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
<td colspan="4"><span id="G_S" class="anchor"></span>S</td>
</tr>
<tr class="even">
<td colspan="2">screen reader</td>
<td colspan="2"><p>“Screen reader” software is designed to make personal computers using Microsoft Windows accessible to blind and visually impaired users. It accomplishes this by providing the user with access to the information displayed on the screen via text-to-speech or by means of Braille display and allows for comprehensive keyboard interaction with the computer.</p>
<p>It also allows users to create custom scripts using the JAWS Scripting Language, which can alter the amount and type of information which is presented by applications, and ultimately makes programs that were not designed for accessibility (such as programs that do not use standard Windows controls) usable through JAWS.</p></td>
</tr>
<tr class="odd">
<td colspan="2">Screening</td>
<td colspan="2">The process of determining if a Veteran should be referred to TEFSC for embedded fragment follow-up.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_508" class="anchor"></span>Section 508</td>
<td colspan="2"><p>Section 508 of the Rehabilitation Act as amended, <a href="http://frwebgate.access.gpo.gov/cgi-bin/getdoc.cgi?dbname=browse_usc&amp;docid=Cite:+29USC794d">29 U.S.C. Section 794(d)</a>, requires that when Federal agencies develop, procure, maintain, or use electronic and information technology, they shall ensure that this technology is accessible to people with disabilities. Agencies must ensure that this technology is accessible to employees and members of the public with disabilities to the extent it does not pose an “undue burden.” Section 508 speaks to various means for disseminating information, including computers, software, and electronic office equipment.</p>
<p>The Clinical Case Registry must be 508 compliant, able to extract data as needed including <a href="#Glos_SNOMED">SNOMED</a> codes.</p></td>
</tr>
<tr class="odd">
<td colspan="2">SEER</td>
<td colspan="2"><em>See</em> <a href="#Glos_SEER">Surveillance, Epidemiology and End Results</a></td>
</tr>
<tr class="even">
<td colspan="2">Selection Rules</td>
<td colspan="2">A pre-defined set of rules that define a Registry patient.</td>
</tr>
<tr class="odd">
<td colspan="2">Sensitive Information</td>
<td colspan="2">Any information which requires a degree of protection and which should be made available only to authorized system users.</td>
</tr>
<tr class="even">
<td colspan="2">Server</td>
<td colspan="2">In information technology, a server is a computer system that provides services to other computing systems—called clients—over a network. The server is where <a href="#Glos_VistA">VistA</a> M-based data and Business Rules reside, making these resources available to the requesting server.</td>
</tr>
<tr class="odd">
<td colspan="2">SGML</td>
<td colspan="2"><em>See</em> <a href="#Glos_SGML">Standardized Generic Markup Language</a></td>
</tr>
<tr class="even">
<td colspan="2">Single Sign On</td>
<td colspan="2">Single Sign On is the process that enables the secure access of disparate applications by a user through use of a single authenticated identifier and password.</td>
</tr>
<tr class="odd">
<td colspan="2">Site Configurable</td>
<td colspan="2">A term used to refer to features in the system that can be modified to meet the needs of each local site.</td>
</tr>
<tr class="even">
<td colspan="2">SNOMED</td>
<td colspan="2"><em>See</em> <a href="#Glos_SNOMED">Systematized Nomenclature of Medicine</a></td>
</tr>
<tr class="odd">
<td colspan="2">Specimen</td>
<td colspan="2">A portion or quantity of material for use in testing, examination, or study. For the purposes of the EFR application, specimens will typically involve urine, blood or tissue collected from a patient.</td>
</tr>
<tr class="even">
<td colspan="2">SQL</td>
<td colspan="2"><em>See</em> <a href="#Glos_SQL">Structured Query Language</a></td>
</tr>
<tr class="odd">
<td colspan="2">SQL Server</td>
<td colspan="2"><em>See</em> <a href="#Glos_SQLServer">Structured Query Language Server</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SSIS" class="anchor"></span>SQL Server Integration Services (SSIS)</td>
<td colspan="2"><p>SSIS is a component of the Microsoft <a href="#Glos_SQL">SQL Server</a> database software which can be used to perform a broad range of data migration tasks.</p>
<p>SSIS is a platform for data integration and workflow applications. It features a data warehousing tool used for data <a href="#Glos_ETL">extraction, transformation, and loading (ETL)</a>. The tool may also be used to automate maintenance of SQL Server databases and updates to extremely complex data.</p></td>
</tr>
<tr class="odd">
<td colspan="2">SSIS</td>
<td colspan="2"><em>See</em> <a href="#Glos_SSIS">SQL Server Integration Services</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SGML" class="anchor"></span>Standardized Generic Markup Language (SGML)</td>
<td colspan="2">A generic markup language for representing documents. SGML is an International Standard that describes the relationship between a document’s content and its structure. SGML allows document-based information to be shared and re-used across applications and computer platforms in an open, vendor-neutral format.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SQL" class="anchor"></span>Structured Query Language (SQL)</td>
<td colspan="2"><p>An industry-standard language for creating, updating and, querying relational database management systems. SQL was originally based upon relational algebra. Its scope includes data query and update, schema creation and modification, and data access control. The data displayed in EFRA is stored in SQL databases.</p>
<p>Typically, the acronym SQL (<em>pronounced</em> “sequel”) is used instead of the actual phrase.</p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SQLServer" class="anchor"></span>Structured Query Language Server (SQL Server)</td>
<td colspan="2">A relational database management system (RDBMS) which is part of the Microsoft® BackOffice® family of servers. SQL Server was designed for client/server use and is accessed by applications using SQL. It runs on Windows NT version 3.5 or higher and is compliant with the ANSI SQL-92 and FIPS 127-2 SQL standards.</td>
</tr>
<tr class="odd">
<td colspan="2">Surveillance</td>
<td colspan="2">Systematic collection, analysis, and interpretation of health data about a disease or condition.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SEER" class="anchor"></span>Surveillance, Epidemiology and End Results (SEER)</td>
<td colspan="2"><mark>[???] [DOES THIS REFER TO THE NCI’S SEER? OR SOMETHING ELSE?] [IF IT’S NCI, THEN WE SHOULD ADD THE LINK HERE: <a href="http://seer.cancer.gov/">http://seer.cancer.gov/</a></mark></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SNOMED" class="anchor"></span>Systematized Nomenclature of Medicine (SNOMED)</td>
<td colspan="2">SNOMED is a terminology that originated as the systematized nomenclature of pathology (SNOP) in the early 1960s under the guidance of the College of American Pathologists. In the late 1970s, the concept was expanded to include most medical domains and renamed SNOMED. The core content includes text files such as the concepts, Descriptions, relationships, ICD-9 mappings, and history tables. SNOMED represents a terminological resource that can be implemented in software applications to represent clinically relevant information comprehensive (&gt;350,000 concepts) multi-disciplinary coverage but discipline neutral structured to support data entry, retrieval, maps etc.</td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
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
<td colspan="3"><span id="G_T" class="anchor"></span>T</td>
</tr>
<tr class="even">
<td colspan="2">“The Alliance”</td>
<td><em>See</em> <a href="#Glosa_NAHIT">National Alliance for Health Information Technology</a></td>
</tr>
<tr class="odd">
<td colspan="2">TBI</td>
<td><em>See</em> <a href="#Glos_TBI">Traumatic Brain Injuries</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_TSPR" class="anchor"></span>Technical Services Project Repository (TSPR)</td>
<td><p>The TSPR is the central data repository and database for VA Health IT (VHIT) project information.</p>
<p><em>See</em> <a href="http://tspr.vista.med.va.gov/tspr/default.htm">http://tspr.VistA.med.va.gov/tspr/default.htm</a></p></td>
</tr>
<tr class="odd">
<td colspan="2">TEFSC</td>
<td><em>See</em> <a href="#Glos_TEFSC">Toxic Embedded Fragment Surveillance Center</a></td>
</tr>
<tr class="even">
<td colspan="2">TEFSC Coordinator</td>
<td>A person (role) at the Toxic Embedded Fragment Surveillance Center responsible for the continuity of patients' interactions with the center.</td>
</tr>
<tr class="odd">
<td colspan="2">Terminal emulation software</td>
<td>A program that allows a personal computer (PC) to act like a (particular brand of) terminal. The PC thus appears as a terminal to the host computer and accepts the same escape sequences for functions such as cursor positioning and clearing the screen. Attachmate <em>Reflection</em> is widely used in VHA for this purpose.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_TIU" class="anchor"></span>Text Integration Utilities (TIU)</td>
<td><p>TIU simplifies the use and management of clinical documents for both clinical and administrative medical facility personnel. In connection with the Authorization/ Subscription Utility (ASU), a facility can set up policies and practices for determining who is responsible or has the privilege for performing various actions on required documents.</p>
<p><em>See</em> complete discussion in <a href="#AppendixE">Appendix E</a>.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_TMDS" class="anchor"></span>Theater Medical Data Store (TMDS)</td>
<td><p>The main purpose of TMDS is to give health care providers an unclassified Web-based means of accessing the same theater medical information collected by the <a href="#Glos_JMeWS">Joint Medical Workstation</a> (JMeWS). Because TMDS uses the same baseline code as JMeWS, medical surveillance and medical command and control features can be activated in support of unclassified operations during a disaster or mass casualty event in the Continental United States or elsewhere.</p>
<p>On May 1, 2008, the Joint Patient Tracking Application (JPTA) was merged with TMDS into a single application, which retained the name of TMDS. All data transferred to the Veterans Tracking Application will come from TMDS.</p>
<p>TMDS is built on the same baseline code as the <a href="#Glos_JMeWS">Joint Medical Workstation</a> (JMeWS), but the features that make JMeWS a classified system (such as medical command and control and the aggregation of population health data for medical surveillance) have been turned off in TMDS to allow it to be run on the Non-classified but Sensitive Internet Protocol Network (NIPRNet).</p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_Therapak" class="anchor"></span>Therapak</td>
<td>Therapak Corporation is a leading supplier of diagnostic test kits used by hospitals, physicians, laboratories and pharmaceutical companies. Therapak currently provides the biomonitoring and fragment analysis kits used by EFR.</td>
</tr>
<tr class="odd">
<td colspan="2">TMDS</td>
<td><em>See</em> <a href="#Glos_TMDS">Theater Medical Data Store</a></td>
</tr>
<tr class="even">
<td colspan="2">Tool tips</td>
<td>Tool tips are “hints” assigned to menu items which appear when the user “hovers” the mouse pointer over a menu.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_TEFSC" class="anchor"></span>Toxic Embedded Fragment Surveillance Center (TEFSC)</td>
<td><p>The TEFSC mission is to follow OEF/OIF Veterans with fragments and to identify and treat potential health problems early.</p>
<p>TEFSC clinical care and surveillance of OEF/OIF Veterans injured by a bullet, blast or explosion includes:</p>
<ul>
<li><p>Maintaining a Registry of OEF and OIF Veterans who have had a fragment removed or who still have a fragment in their body.</p></li>
<li><p>Using information from the Registry to write guidelines for medical care.</p></li>
<li><p>Providing guidelines for medical care to other VA healthcare providers across the country.</p></li>
<li><p>Providing special testing for chemicals that might be released from the fragments.</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_TBI" class="anchor"></span>Traumatic Brain Injuries (TBI)</td>
<td>The Traumatic Brain Injuries (TBI) Registry software application allows case managers to identify those Veterans who participated in Operation Enduring Freedom (OEF) or Operation Iraqi Freedom (OIF) and who sustained a head injury and thus are potential traumatic brain injury (TBI) patients. The TBI application permits the case manager to oversee and track the comprehensive evaluation of those patients. It also provides 17 types of reports used for tracking the evaluation and care of individuals identified as possible TBI candidates.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_Triage" class="anchor"></span>Triage</td>
<td>For the purposes of the Embedded Fragment Registry application, triage refers to the process of making a decision regarding the follow-on treatment and inclusion of a patient in the EFR that has been referred to the TEFSC.</td>
</tr>
<tr class="even">
<td colspan="2">Triage Algorithm</td>
<td>For the purposes of the Embedded Fragment Registry application, the triage algorithm refers to the procedure or computation applied in the process of making a decision regarding the follow-on treatment and inclusion of a patient in the EFR that has been referred to the TEFSC.</td>
</tr>
<tr class="odd">
<td colspan="2">TSPR</td>
<td><em>See</em> <a href="#Glos_TSPR">Technical Services Project Repository</a></td>
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
<td colspan="4"><span id="G_U" class="anchor"></span>U</td>
</tr>
<tr class="even">
<td colspan="2"><span id="glos_URL" class="anchor"></span>Uniform Resource Locator (URL)</td>
<td colspan="2">(<em>Formerly</em> <u>Universal</u> Resource Locator). A standard way of specifying the location of an object, typically a web page, on the Internet. URLs are the form of address used on the World-Wide Web. In EFRA, the URL is typically a web page which displays another application screen.</td>
</tr>
<tr class="odd">
<td colspan="2">URL</td>
<td colspan="2"><em>See</em> Uniform Resource Locator</td>
</tr>
<tr class="even">
<td colspan="2">USAF</td>
<td colspan="2"><em>Acronym for</em> United States Air Force</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_USAPHC" class="anchor"></span>U.S. Army Public Health Command (Provisional)</td>
<td colspan="2"><p>The former U.S. Army Center for Health Promotion and Preventive Medicine is now the U.S. Army Public Health Command (Provisional). The overall objectives of the USAPHC are to:</p>
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
<td colspan="2"><p>A user interface is the means by which people (the users) interact with a particular machine, device, computer program or other complex tool (the system). The user interface provides one or more means of:</p>
<p>• Input, which allows the users to manipulate the system</p>
<p>• Output, which allows the system to produce the effects of the users’ manipulation</p>
<p>The interface may be based strictly on text (as in the traditional “roll and scroll” IFCAP interface), or on both text and graphics.</p>
<p>In computer science and human-computer interaction, the user interface (of a computer program) refers to the graphical, textual and auditory information the program presents to the user, and the control sequences (such as keystrokes with the computer keyboard and movements of the computer mouse) the user employs to control the program.</p>
<p><em>See also</em> <a href="#Glos_GUI">Graphical User Interface</a></p></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
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
<td colspan="5"><span id="G_V" class="anchor"></span>V</td>
</tr>
<tr class="even">
<td colspan="2">VA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VA">Veterans Affairs</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VADIR" class="anchor"></span>VA/DoD Information Repository (VADIR)</td>
<td colspan="3"><p>The VADIR database was established to support a One VA/<a href="#Glos_DoD">DoD</a> data-sharing initiative in order to consolidate data transfers between DoD and VA. The DoD Defense Manpower Data Center (DMDC) stage shared data as defined in a Memorandum of Understanding (MOU), and transmits data to VADIR. The VADIR data are used to assist in determining Veteran benefits.</p>
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
<td colspan="2">Verified Referral</td>
<td colspan="3">A patient’s referral information in the EFR application that has been verified by TEFSC through a process of comparing an incoming referral to referral information previously stored in the EFR application and selecting the most appropriate response. This process ‘builds’ the verified referral.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VTA" class="anchor"></span>Veteran Tracking Application (VTA)</td>
<td colspan="3">A VA version of the <a href="#Glos_JTPA">Joint Patient Tracking Application</a> which provides clinicians access to medical records on combat wounded soldiers throughout the continuum of care, from the battlefield to a VA hospital.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VTA_DataExtract" class="anchor"></span>Veteran Tracking Application (VTA) data extract</td>
<td colspan="3"><p>This extract includes the following read-only data:</p>
<ul>
<li><p>Patient Last Name</p></li>
<li><p>Patient First Name</p></li>
<li><p>Social Security Number</p></li>
<li><p>ICD-9 Codes (used by <a href="#Glos_DoD">DoD</a> in their case definition algorithm)</p></li>
<li><p>Subjective Objective Assessment and Plan (SOAP) Note Keywords (used by DoD in their case definition algorithm)</p></li>
<li><p>Patient Address Line1</p></li>
<li><p>Patient Address Line2</p></li>
<li><p>Patient City</p></li>
<li><p>Patient State</p></li>
<li><p>Patient Zip/Postal Code</p></li>
<li><p>Patient Phone (primary)</p></li>
<li><p>Patient email address</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VHACO" class="anchor"></span>Veterans Affairs Central Office (VACO)</td>
<td colspan="3">The VA “headquarters” offices, located in Washington DC, which oversees field operations throughout the VA.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VA" class="anchor"></span>Veterans Affairs, Department of (VA)</td>
<td colspan="3"><p>The VA mission is to serve America's Veterans and their families with dignity and compassion and to be their principal advocate in ensuring that they receive medical care, benefits, social support, and lasting memorials promoting the health, welfare, and dignity of all Veterans in recognition of their service to this Nation.</p>
<p>VA is the second largest Federal department and has over 278,000 employees. Among the many professions represented in the vast VA workforce are physicians, nurses, counselors, statisticians, architects, computer specialists, and attorneys. As advocates for Veterans and their families, the VA community is committed to providing the very best services with an attitude of caring and courtesy.</p></td>
</tr>
<tr class="even">
<td colspan="2">Veterans Affairs Learning University (VALU)</td>
<td colspan="3">VALU supports all employee learning and performance improvement across VA.</td>
</tr>
<tr class="odd">
<td colspan="2">Veterans Benefits Administration (VBA)</td>
<td colspan="3">VBA, in partnership with the Veterans Health Administration and the National Cemetery Administration, provides benefits and services to the Veterans and their families in a responsive, timely and compassionate manner in recognition of their service to the Nation.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VHA" class="anchor"></span>Veterans Health Administration (VHA)</td>
<td colspan="3">VHA administers the United States Veterans Healthcare System, whose mission is to serve the needs of America’s Veterans by providing primary care, specialized care, and related medical and social support services.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VistA" class="anchor"></span>Veterans Health Information Systems and Technology Architecture (VistA)</td>
<td colspan="3"><p>VistA is a comprehensive, integrated health care information system composed of numerous software modules.</p>
<p><em>See</em> <a href="http://www.va.gov/vista_monograph/docs/2008VistAHealtheVet_Monograph.pdf">http://www.va.gov/VistA_monograph/docs/2008VistAHealtheVet_Monograph.pdf</a> and <a href="http://www.virec.research.va.gov/DataSourcesName/VISTA/VISTA.htm">http://www.virec.research.va.gov/DataSourcesName/VISTA/VISTA.htm</a>.</p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VISN" class="anchor"></span>Veterans Integrated Service Network (VISN)</td>
<td colspan="3"><a href="#Glos_VHA">VHA</a> organizes its local facilities into networks called VISNS (VA Integrated Service Networks). At the VISN level, VistA data from multiple local facilities may be combined into a data warehouse.</td>
</tr>
<tr class="odd">
<td colspan="2">VHA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VHA">Veterans Health Administration</a></td>
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
<td colspan="3"><em>See</em> <a href="#Glos_VTA">Veteran Tracking Application</a></td>
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
<td colspan="4"><span id="G_W" class="anchor"></span>W</td>
</tr>
<tr class="even">
<td colspan="2">WBA</td>
<td colspan="2"><em>See</em> <a href="#Glos_WBA">Web-Based Application</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_WBA" class="anchor"></span>Web-Based Application (WBA)</td>
<td colspan="2"><p>In software engineering, a web application is an application that is accessed via a web browser over a network such as the Internet or an intranet. The term may also mean a computer software application that is hosted in a browser-controlled environment (e.g. a Java applet) or coded in a browser-supported language (such as JavaScript, possibly combined with a browser-rendered markup language like HTML) and reliant on a common web browser to render the application executable.</p>
<p>Web applications are popular due to the ready availability of web browsers, and the convenience of using a web browser as a client, sometimes called a thin client. The ability to update and maintain web applications without distributing and installing software on potentially thousands of client computers is a key reason for their popularity, as is the inherent support for cross-platform compatibility. Common web applications include webmail, online retail sales, online auctions, wikis and many other functions. The EFRA is a WBA.</p>
<p><em>See also</em> <a href="#Glos_UserInterface">User Interface</a></p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_workflow" class="anchor"></span>Workflow</td>
<td colspan="2">EFR provides two complex workflows: Biomonitoring and Fragment Analysis. Each referral can have multiple workflows, also known as cases. Each case contains up to five activities which reflect the stage the workflow case currently is in. Each referral, case and activity has a status that indicates progress of the particular item.</td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
</tr>
</tbody>
</table>

| Term or Acronym                        |                      |                                                | Description |
|----------------------------------------|----------------------|------------------------------------------------|-------------|
| <span id="G_X" class="anchor"></span>X |                      |                                                |             |
| XML                                    |                      | *See* [Extensible Mark-up Language](#Glos_XML) |             |
| [ BACK ](#glossary)                | to Glossary Contents |                                                |             |

<span id="_Toc259014245" class="anchor"></span>Subject Index

C

CCR

downloading software, 11

overview of, 260

recommended users of, 5

D

Dceasedcheck, 19

Documentation

in VistA Document Library, 12

Download CCR software, 11

F

Features of CCR, 260

G

GUI

parts of the screen, 16

H

Hlpmenuoptions, 17

M

Mnu

Help, 17

O

OEF, 275

OIF, 275

Operation Enduring Freedom (OEF), 275

Operation Iraqi Freedom (OIF), 275

P

Prtsofthescreen, 16

Ptient

deceased, 19

R

Registry, 275

reports

clinical and admin, 4

controls, 63

Lab Kit Orders Report, 112

Lab Report Details, 167, 172, 179, 186

Questionnaire Summary, 154

Referral report, 65

referrals by risk category, 66

referrals received by facility, 65

average number of days between referral and triage, 68

referrals by status, 68

Reporting tab, 63

[^1]: *Global War on Terror (GWOT) Report, 4/19/2007 (see* <http://tspr.vista.med.va.gov/warboard/ProjectDocs/Embedded_Fragments_Registry/GWOT_TF_Report_042407.pdf>). Note that even though the term “global war on terror” is now deprecated, this historical document nonetheless forms the basis for the EFR charter.