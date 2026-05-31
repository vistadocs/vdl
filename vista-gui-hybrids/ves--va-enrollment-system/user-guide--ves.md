---
title: User Guide VES 6.3
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: null
app_code: VES
app_name: VA Enrollment System
section: GUI
app_status: archive
pkg_ns: VES
patch_ver: 6.3
patch_id: VES*6.3
group_key: VES:VES:6.3
file_numbers: []
security_keys: []
menu_options: 0
description: Veterans Health Administration (VHA) Enrollment System (VES)
audience: End users and package coordinators (ADPAC)
keywords: []
page_count: 0
word_count: 8225
section_count: 23
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: December 2022
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System_Archive/ves_6_3_ug.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System_Archive/ves_6_3_ug.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=293
audit_applied: '2026-05-31'
master_source: User Guide VES 6.3
master_pub_date: December 2022
consolidated_from: 19 versions
prior_versions:
- User Guide VES 6.0
- User Guide VES 6.1
- User Guide VES 6.10
- User Guide VES 6.11
- User Guide VES 6.12
- User Guide VES 6.13
- User Guide VES 6.14.5
- User Guide VES 6.14
- User Guide VES 6.15
- User Guide VES 6.2.2
- User Guide VES 6.2
- User Guide VES 6.4
- User Guide VES 6.5
- User Guide VES 6.6
- User Guide VES 6.7.1
- User Guide VES 6.7
- User Guide VES 6.8
- User Guide VES 6.9
consolidated_title: user guide ves
---

Veterans Health Administration (VHA) Enrollment System (VES) 6.3

Quick Start User Guide

![](user-guide-ves-6-3/001.png)

December 2022

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc119934838" class="anchor"></span>Table : Accessibility Software</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 54%" />
<col style="width: 17%" />
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
<td>12/03/2022</td>
<td>41.0</td>
<td><p><strong>VES V6.3</strong> added the following:</p>
<ul>
<li><p>Project References updated, p. 2</p></li>
<li><p>CC Determination Date on screens:</p>
<ul>
<li><p>Overview, pgs. 10-11</p></li>
<li><p>Community Care, p. 12</p></li>
<li><p>Community Care Determination, pgs. 13-14</p></li>
<li><p>Community Care History, pgs. 15-16</p></li>
</ul></li>
<li><p>Presumptive Psychosis on screens:</p>
<ul>
<li><p>Eligibility, pgs. 17-21</p></li>
<li><p>Edit Current Eligibility, pgs. 22-25</p></li>
<li><p>Eligibility History, pgs. 26-27</p></li>
<li><p>Secondary Eligibility Codes, p. 28</p></li>
</ul></li>
<li><p>Presumptive (38 USC 1702-38 CFR 17.109) Carveout VHAP, p. 29</p></li>
<li><p>"Clinical Evaluation" Carveout VHAP, p. 30</p></li>
<li><p>1010EZ / 1010EZR 2022 Form Updates:</p>
<ul>
<li><p>Overview, p. 31</p></li>
<li><p>Identity Traits, pgs. 32-33</p></li>
<li><p>Personal, p. 34</p></li>
<li><p>Financials, p. 35</p></li>
<li><p>Enrollment, p. 36</p></li>
</ul></li>
<li><p>Updated TPA Message Log description, p. 37</p></li>
<li><p>Updated VCA description, p.38</p></li>
<li><p>Updated COMPACT Act Error Message on UI description, p. 39</p></li>
</ul></td>
<td>BAHTW</td>
</tr>
</tbody>
</table>

<span id="_Toc119934838" class="anchor"></span>Table : Accessibility Software

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the Quick Start User Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A Quick Start User Guide is a technical communication document intended to give assistance to people using a particular system, such as the Veterans Health Administration (VHA) Enrollment System (VES). Technical writers generally compose, update, and maintain the Quick Start User Guide; however, programmers, product and project managers, or other technical staff can also compose, update, and maintain the Quick Start User Guide. Most quick start guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The Quick Start User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

Table of Contents

Table of Figures

List of Tables

[Table 1: Accessibility Software [8](#_Toc119934838)](#_Toc119934838)

[Table 2: Support Contact Information [40](#_Toc119934839)](#_Toc119934839)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Overview](#overview)
    - [Release Updates and Enhancements](#release-updates-and-enhancements)
    - [Organization of the Manual](#organization-of-the-manual)
    - [Assumptions](#assumptions)
    - [Installation, Maintenance, & Monitoring](#installation-maintenance-monitoring)
    - [Software Disclaimer](#software-disclaimer)
    - [User Guide Disclaimer](#user-guide-disclaimer)
    - [Project References](#project-references)
- [System Summary](#system-summary)
  - [System Design Document](#system-design-document)
  - [User Access Levels](#user-access-levels)
  - [ESM Application Information System Contingency Plan](#esm-application-information-system-contingency-plan)
  - [ESM Project Artifacts (VDL)](#esm-project-artifacts-vdl)
- [Getting Started](#getting-started)
  - [VES Layout](#ves-layout)
  - [VES Online Help](#ves-online-help)
  - [Compliance & Accessibility](#compliance-accessibility)
    - [Accessibility Software](#accessibility-software)
  - [Standard Data Service (SDS) Lookup Tables](#standard-data-service-sds-lookup-tables)
  - [Exiting VES](#exiting-ves)
  - [Caveats and Exceptions](#caveats-and-exceptions)
- [Significant Additions and Updates to VES Version 6.3](#significant-additions-and-updates-to-ves-version-63)
  - [CC Determination Date on screens:](#cc-determination-date-on-screens)
    - [Overview](#overview-1)
    - [Community Care](#community-care)
    - [Community Care Determination](#community-care-determination)
    - [Community Care History](#community-care-history)
  - [Presumptive Psychosis on screens:](#presumptive-psychosis-on-screens)
    - [Eligibility](#eligibility)
    - [Edit Current Eligibility](#edit-current-eligibility)
    - [Eligibility History](#eligibility-history)
    - [Secondary Eligibility Codes](#secondary-eligibility-codes)
  - ["Presumptive (38 USC 1702-38 CFR 17.109)" Carveout VHAP](#presumptive-38-usc-1702-38-cfr-17109-carveout-vhap)
  - ["Clinical Evaluation" Carveout VHAP](#clinical-evaluation-carveout-vhap)
  - [EZ / 1010 EZR 2022 Form Updates:](#ez-1010-ezr-2022-form-updates)
    - [Overview](#overview-2)
    - [Identity Traits](#identity-traits)
    - [Personal](#personal)
    - [Financials](#financials)
    - [Enrollment](#enrollment)
  - [Updated TPA Message Log description](#updated-tpa-message-log-description)
  - [Updated VCE Description](#updated-vce-description)
  - [Updated COMPACT Act Error Message on UI description](#updated-compact-act-error-message-on-ui-description)
- [Troubleshooting](#troubleshooting)
  - [National Service Desk and Other Contacts](#national-service-desk-and-other-contacts)
  - [Browser & Operating System Compatibility](#browser-operating-system-compatibility)
The Veterans Health Administration (VHA) Enrollment System (VES) is the primary Veterans Affairs (VA) system used to manage VA health benefits.
VES allows staff at the Health Eligibility Center (HEC), located in Atlanta, Georgia, to work more efficiently and determine patient eligibility in a timelier manner. Messaging with the VAMC (Department of Veterans Affairs Medical Center) allows for the adding and updating of beneficiary records to the enterprise enrollment system to be shared with the field.
VES is one component of the "system of systems" needed to implement the VistA/GUI Hybrids (formerly Health*<u>e</u>*Vet) REE (Registration, Eligibility & Enrollment) environment.
VES's two main functions are:
- Expert System (Messaging) provides a seamless bi-directional interface with external Veterans Health Administration (VHA) and non-VHA systems for data exchange of Veterans' information.
- Workflow (Case Management) that provides authorized VHA case representatives at the HEC and VAMC with a web interface to easily track, maintain, and manage cases associated with Veteran benefits. HEC and VAMC staff utilize VES to manage these "cases" to completion so that verified Eligibility & Enrollment can be determined.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this user guide is to familiarize users with important features and navigational elements of the VES application.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

President George W. Bush established a task force for returning Global War on Terror (GWOT) heroes who resulted in enhancements that improved delivery of Federal services and benefits to GWOT service members and Veterans. Among recommendations associated with task force was to focus on enhancing delivery of services and information to GWOT service members and Veterans within existing authority and resource levels.

### Release Updates and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click the [link](https://ves.va.gov/esr/webhelp/esr_help_project.htm#t=es_overview%2Fupdates_releases_enhancements.htm) to view current and past VES release updates and enhancements on the Online Help.

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Quick Start User Guide contains the following:

- Introduction
- System Summary
- Getting Started
- Significant Additions and Updates to VES Version
- Troubleshooting

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This quick start was written with the following assumed experience/skills of the audience:

- User has basic knowledge of VES (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, menus, and security keys required for VES.
- User is using VES to do their job.
- User has validated access to VES.
- User has completed any prerequisite training.

### Installation, Maintenance, & Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation, maintenance, and monitoring of VES updates are performed at the Austin Information Technology Center (AITC) on the third Saturday of each month.

### Software Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software was developed at the Department of Veterans Affairs (VA) by employees of the federal government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

### User Guide Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The appearance of external hyperlink references in this User Guide does not constitute endorsement by VA of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Project References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the following VES references:

- VES 6.3 Release Notes
- VES 6.3 Online Help

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Users require group membership to access SharePoint and Teams' links. To request access, contact the E&E Program Management Office (PMO) or use the request access option at the SharePoint site and specify group membership.

## System Design Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer the System Design Document (SDD). Please submit a [ServiceNow](https://yourit.va.gov/va) ticket to the NTL MNT EDB/ESR group for access to the SDD.

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the Buttons/Admin section where User Accounts, Profiles, Roles and Capability Sets explain the different user access levels of the VES.

## ESM Application Information System Contingency Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enrollment System Modernization (ESM) Application Information System Contingency Plan is stored in eMASS and is available upon request. Please submit a [ServiceNow](https://yourit.va.gov/va) ticket to the NTL MNT EDB/ESR group for access.

## ESM Project Artifacts (VDL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click the following [link](https://www.va.gov/vdl/section.asp?secid=4) to access the ESM Project Artifacts located in the VA Software Document Library (VDL). Scroll down to VA Enrollment System (VES) to access VES artifacts.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VES Layout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VES displays a beneficiary's record data. The "Menu Bar" and the "Person Search Tabs" provide access to various screens for viewing, updating, adding, and deleting information on VES.

Menu Bar

Menu Bar is where utility buttons for VES are located.

From the Menu Bar, users view Worklists, perform Veteran Merges, perform Health Level 7 (HL7), Community Care Network (CCN), Third-Party Administrator (TPA) and Military Service Data Sharing (MSDS) Message Searches, Load Registries, do an Undeliverable Mail Search, Generate/View Reports, Reference Thresholds/Enrollment Group Threshold (EGT) Settings, view Veterans Online Application (VOA) Re-submissions, Search and Add a New Person, and perform general Administrative functions such as enable or disable Veterans Community Care Eligibility (VCE) parameters.

![](user-guide-ves-6-3/002.png)

<span id="_Toc119934823" class="anchor"></span>Figure : Menu Bar

Summary

The Summary displays the beneficiary's Name, social security number (SSN), date of birth (DOB), date of death (DOD), Enrollment Status, Member ID (if available), and any other important information such as Open Work Items, Pending Merges, Sensitive Records, etc.

Sensitive Record information, if disclosed to the individual, may have serious adverse effects on the individual's mental or physical health. Such information may require explanation or interpretation by an intermediary or assistance in the information's acceptance and assimilation in order to preclude adverse impacts on the individual's mental or physical health.

![](user-guide-ves-6-3/003.png)

<span id="_Toc119934824" class="anchor"></span>Figure : Summary with a Sensitive Record

Person Search Tabs

Person Search Tabs are the area of the screen where the user may access the various kinds of information on record for the beneficiary to aid in determining his or her eligibility for enrollment in the VA healthcare system.

![](user-guide-ves-6-3/004.png)

<span id="_Toc119934825" class="anchor"></span>Figure : Person Search Tabs

2.  The terms [Veteran](javascript:hhctrl.TextPopup('A%20veteran%20is%20a%20person%20who%20has%20served%20in%20the%20armed%20forces.','Arial,10',10,10,00000000,0xffffff)), [beneficiary](javascript:hhctrl.TextPopup('A%20beneficiary%20is%20one%20that%20receives%20a%20benefit%20as%20in%20VA%20health%20care%20benefits.','Arial,10',10,10,00000000,0xffffff)), [patient](javascript:hhctrl.TextPopup('A%20patient%20is%20one%20who%20receives%20medical%20attention,%20care,%20or%20treatment.','Arial,10',10,10,00000000,0xffffff)), and [applicant](javascript:hhctrl.TextPopup('An%20applicant%20is%20one%20that%20applies%20for%20benefits%20as%20in%20VA%20health%20care%20benefits.','Arial,10',10,10,00000000,0xffffff)) are used interchangeably throughout VES. While not all applicants are Veterans or patients, not all applicants are beneficiaries either. Whether they are a Veteran, patient or beneficiary is determined AFTER the application for benefits is received and processed.

![](user-guide-ves-6-3/005.png)

<span id="_Toc119934826" class="anchor"></span>Figure : Summary and Main Screen on VES

Sorting Columns

For screens that contain listed data, ascending and descending sorting may be performed for any category by clicking on the category name or on the symbol ![](user-guide-ves-6-3/006.png). Re-clicking the category name or symbol re-sorts the previous sort.

![](user-guide-ves-6-3/007.png)

<span id="_Toc119934827" class="anchor"></span>Figure : Sorting Columns

VES Online Help is an Online Help system built in Adobe RoboHelp, an authoring and publishing tool. The VES Online Help delivers an output to VES users when clicking the context-sensitive help buttons, System Help or Screen Help.

## VES Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In VES, you can obtain information about windows or dialogs clicking the context-sensitive help button![](user-guide-ves-6-3/008.png) available VES in the upper right-hand corner of the "System Help" and "Screen Help".

System Help:

> System Help is the top upper-right context-sensitive help button ![](user-guide-ves-6-3/009.png).

Screen Help:

> Screen Help is the lower upper-right context-sensitive help button ![](user-guide-ves-6-3/010.png).

3.  If you roll over the Help icons in VES, screen tips will appear distinguishing between "System Help" and "Screen Help".

![](user-guide-ves-6-3/011.png)

<span id="_Toc63260923" class="anchor"></span>Figure 6: System Help and Screen Help

(an online Table of Contents (TOC) is a summary of your project with topics arranged by category)

<u>VES Online Help Tool Bar</u>

To the left of the VES Online Help, above the table of contents pane, a tool bar contains *Contents, Index, Search* and *Glossary* links.

Table of Contents: ![](user-guide-ves-6-3/012.png)

Contents displays an expanded table of contents.

- Collapse / Expand (![](user-guide-ves-6-3/013.png), ![](user-guide-ves-6-3/014.png) )
- Topics (![](user-guide-ves-6-3/015.png)) are categories of information in the VES Online Help. Clicking![](user-guide-ves-6-3/016.png), you can view the contents of topic in the main screen located to the right.

Index: ![](user-guide-ves-6-3/017.png)

Index displays a multi-level list of keywords and keyword phrases. These terms are associated with topics in the VES Online Help, and the keywords are intended to direct you to specific topics within the VES Online Help. Click the keyword to launch a topic from the TOC to the main screen. If the keyword is used with more than one topic, a list of topics displays under the keyword or keyword phrase in which the keyword or keyword phrase appears.

Search: ![](user-guide-ves-6-3/018.png)

Search provides a way to explore the content of the VES Online Help and find matches to VES-defined words. Unlike Index that lists author-defined keywords such as terms, synonyms, and cross-references, Search lists words used within the content of topics. To find a topic in which the word appears, click the letter link to display the words that begin with the letter being searched for. Words that appear once are in bold. Words that appear in multiple topics are listed with numbers. Click on a number to display the topic in the right-hand pane in which the word appears.

Glossary: ![](user-guide-ves-6-3/019.png)

Glossary provides a list of terms and definitions related to the subject-matter in VES. Click a letter in the top pane and see corresponding definitions that begin with the letter clicked in the lower pane.

The VES Online Help uses Adobe RoboHelp's 2017 WebHelp as its output and is 508-compliant. The Online Help opens in your web browser as a new window.

<u>Other buttons and functions</u>Hide/Show the left pane

Provides a larger viewing area of the open topic and hides the left pane.

1.  Click the Hide link in the upper left side of the right pane to hide the left pane.
2.  Click the Show link in the upper left side of the pane to show the left pane.

Browser Toolbar

Since there is not a browser toolbar at the top of the VES Online Help window, right-click within VES Online Help window and select either Back or Forward to go back and forward through the history of visited topics, print a topic, or perform other tasks available within the Windows context-sensitive commands.

4.  The Forward command is only available if the Back command has been used first. At that point the Forward command becomes available.

The TOC on the left side of the VES Online Help can also be used to navigate throughout the VES Online Help.

WebHelp Build Date

Click the Systems Parameters topic to view the WebHelp Build Date. The build date is next to the topic title.

Adjusting the main screen and TOC size

Adjust the width and height of the main screen window by dragging the edges of the window in or out.

Adjust the width of the table of contents pane by pointing to the right edge of the left pane until the mouse pointer turns into a line with arrows on each end: ![](user-guide-ves-6-3/020.png) Drag the pane to the right or left with the left mouse button held down.

*Navigating Help Topics*

5.  The following navigational techniques generally refer to the Online Help, where indicated, and not the written documentation:

*Links (Online Help)*\* symbol indicates a required field in the Online Help.

![](user-guide-ves-6-3/021.png) symbol indicates a required field in the user guide.

![](user-guide-ves-6-3/022.png) symbol is displayed when a submitted field has an error.

![](user-guide-ves-6-3/023.png) symbol ("data changed") is displayed when a type of data has changed on the *History*, *Veteran Merge*, and user-related confirmation windows.

6.  Indicates a note or item of special interest.

## Compliance & Accessibility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With every release, the Department of Veterans Affairs strives to improve accessibility in VES through the World Wide Web Consortium (W3C)'s Web Content Accessibility Guidelines (WCAG) 2.0, Levels A and AA.

It's important to mention that because Adobe RoboHelp displays a leveled hierarchy of contents through expanded and collapsed icons. VES users must click the collapsed ![](user-guide-ves-6-3/024.png)icon to display contents![](user-guide-ves-6-3/025.png)for that section and re-click the expanded ![](user-guide-ves-6-3/026.png) icon to close the contents of that section.

### Accessibility Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below lists accessibility software used to assist disabled users with VES.

<table>
<caption><p><span id="_Toc119934839" class="anchor"></span>Table : Support Contact Information</p></caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Accessibility Software</strong></th>
<th><strong>Description</strong></th>
<th><strong>Keyboard Shortcuts</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Jaws (Job Access with Speech)</td>
<td>Assists blind and visually impaired Veterans with reading screens on VES either with a text-to-speech output or a Braille display.</td>
<td><a href="https://doccenter.freedomscientific.com/doccenter/archives/training/jawskeystrokes.htm">JAWS Keystrokes</a></td>
</tr>
<tr class="even">
<td>ZoomText Magnifier / Reader</td>
<td>Magnifies VES screens to varying levels and assists Veterans with screen reading.</td>
<td><a href="https://www.zoomtext.com/help/tutorial/">ZoomText Tutorial</a></td>
</tr>
<tr class="odd">
<td>Dragon Naturally Speaking</td>
<td><p>Through dictating VES functions, assists disabled Veterans with VES document downloads</p>
<p>and exports.</p></td>
<td><a href="https://www.nuance.com/dragon/user-documentation.html">Dragon NaturallySpeaking User Documentation</a></td>
</tr>
</tbody>
</table>

<span id="_Toc119934839" class="anchor"></span>Table : Support Contact Information

If you have questions or comments regarding Adobe RoboHelp 2017 accessibility, please contact the [Adobe Accessibility Team](https://www.adobe.com/accessibility/feedback.html) and provide feedback on their feedback form. For further information on Adobe accessibility, please refer to the following link:

<https://www.adobe.com/accessibility/508standards.html>

## Standard Data Service (SDS) Lookup Tables 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SDS is a repository of enterprise-level reference tables. The SDS Lookup Tables contain information needed to define requirements and research the E&E process. The SDS Lookup Tables page enables a user to view information about a specific table (for example, table name, code, description, active status, date when a code became inactive). VES uses SDS tables in several of its applications.

Users access the SDS Lookup Tables screen by clicking the Reference Tables link at the top right of any VES screen.

To display the SDS Lookup Tables:

1.  Click the Reference Tables link and the SDS Lookup Tables page displays. SDS table and SDS History table names are listed in alphabetical order in the Navigation Bar.
3.  Select an SDS table name from the navigation bar. The right panel displays the first five columns in the selected table and the Table Name contains a link for downloading the whole table as an Excel spreadsheet. The Excel spreadsheet will display all the columns in the table.

![](user-guide-ves-6-3/027.png)

<span id="_Toc67408789" class="anchor"></span>Figure 7: SDS Lookup Table

*No data found for the selected table* displays if there is no data in an SDS Lookup Table.

## Exiting VES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To exit VES, click on the Sign Out link at the top of any page.

## Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None.

# Significant Additions and Updates to VES Version 6.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to VES 6.3 additions below in the Online Help.

## CC Determination Date on screens:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Overview</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll all the way down to the bottom of the <strong>Overview</strong> topic.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the updated <strong>Overview</strong> screen shot with the added <strong>CC Determination Date</strong> is correct and accurate.</p>
<p>![](user-guide-ves-6-3/028.png)</p>
<p><span id="_Toc119934830" class="anchor"></span>Figure : Overview</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Community Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Community Care</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>CC Determination Date</strong> definition.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the added <strong>CC Determination Date</strong> definition and screen shot are correct and accurate.</p>
<p>![](user-guide-ves-6-3/029.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Community Care Determination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Community Care</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Community Care Determination</strong> topic (still under the <strong>Community Care</strong> section).</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Community Care Outcome</strong> panel section.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Scroll down to the <strong>CC Determination Date</strong> definition (under the <strong>Community Care Program Collateral VCEs</strong> table).</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the added <strong>CC Determination Date</strong> definition is correct and accurate.</p>
<p>![](user-guide-ves-6-3/030.png)</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>Scroll down to the bottom of the topic.</td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>Confirm the updated <strong>Community Care Determination</strong> screen shot with the added <strong>CC Determination Date</strong> screen shot is correct and accurate.</p>
<p>![](user-guide-ves-6-3/031.png)</p>
<p><span id="_Toc119934831" class="anchor"></span>Figure : Community Care Determination</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Community Care History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Community Care</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Community Care Determination History</strong> topic (still under the <strong>Community Care</strong> section).</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Community Care Outcome</strong> panel section.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the added <strong>CC Determination Date</strong> definition is correct and accurate.</p>
<p>![](user-guide-ves-6-3/032.png)</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Scroll down to the bottom of the topic.</td>
</tr>
<tr class="even">
<td>8</td>
<td><p>Confirm the updated <strong>Community Care Determination History</strong> screen shot with the added <strong>CC Determination Date</strong> field is correct and accurate.</p>
<p>![](user-guide-ves-6-3/033.png)</p>
<p><span id="_Toc119934832" class="anchor"></span>Figure : Community Care Determination History</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Presumptive Psychosis on screens:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Eligibility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the <strong>Eligibility</strong> screen shot.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the updated <strong>Eligibility</strong> screen shot with the added <strong>Clinical Evaluations</strong> and <strong>Clinical Determinations</strong> panels are correct and accurate.</p>
<p>![](user-guide-ves-6-3/034.png)</p>
<p><span id="_Toc119934833" class="anchor"></span>Figure : Eligibility</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Navigate back to the Table of Contents.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Click the <strong>Clinical Evaluations</strong> section (still under the <strong>Eligibility</strong> section).</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the added <strong>Clinical Evaluations</strong> topic is correct and accurate.</p>
<p>![](user-guide-ves-6-3/035.png)</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>Navigate back to the Table of Contents.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Scroll down to the <strong>Clinical Determinations</strong> section (still under the <strong>Eligibility</strong> section).</td>
</tr>
<tr class="even">
<td>10</td>
<td>Click the <strong>Clinical Determinations</strong> topic (which has been renamed from "Other Eligibility Factors").</td>
</tr>
<tr class="odd">
<td>11</td>
<td>Click the <strong>Clinical Determinations History</strong> section.</td>
</tr>
<tr class="even">
<td>12</td>
<td>Scroll down to the <strong>Presumptive Psychosis</strong> panel.</td>
</tr>
<tr class="odd">
<td>13</td>
<td><p>Confirm the text under <strong>Presumptive Psychosis</strong> is correct and accurate.</p>
<p>![](user-guide-ves-6-3/036.png)</p></td>
</tr>
<tr class="even">
<td>14</td>
<td>Scroll down to the bottom of the topic.</td>
</tr>
<tr class="odd">
<td>15</td>
<td><p>Confirm the updated <strong>Clinical Determination History</strong> screen shot with the added <strong>Presumptive Psychosis</strong> panel is correct and accurate.</p>
<p>![](user-guide-ves-6-3/037.png)</p>
<p><span id="_Toc119934834" class="anchor"></span>Figure : Clinical Determination History</p></td>
</tr>
<tr class="even">
<td>16</td>
<td>Navigate back to the table of contents.</td>
</tr>
<tr class="odd">
<td>17</td>
<td>Click the <strong>View Clinical Determination</strong> topic (still under "Clinical Determinations").</td>
</tr>
<tr class="even">
<td>18</td>
<td>Scroll down to the <strong>Presumptive Psychosis</strong> panel.</td>
</tr>
<tr class="odd">
<td>19</td>
<td><p>Confirm the added text for "Presumptive Psychosis" and notes are correct and accurate.</p>
<p>![](user-guide-ves-6-3/038.png)</p></td>
</tr>
<tr class="even">
<td>20</td>
<td>Scroll down to the bottom of the topic.</td>
</tr>
<tr class="odd">
<td>21</td>
<td><p>Confirm the updated <strong>Clinical Determination</strong> screen shot with the added <strong>Presumptive Psychosis</strong> panel is correct and accurate.</p>
<p>![](user-guide-ves-6-3/039.png)</p>
<p><span id="_Toc119934835" class="anchor"></span>Figure : Clinical Determination</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Edit Current Eligibility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Edit Current</strong> <strong>Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>Presumptive Psychosis Screening</strong> definition (under <strong>Clinical Evaluations</strong>).</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the added <strong>Presumptive Psychosis Screening</strong> definition is correct and accurate.</p>
<p>![](user-guide-ves-6-3/040.png)</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>Scroll down to the <strong>Presumptive Psychosis Category</strong> definition.</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the added <strong>Presumptive Psychosis Category</strong> definition is correct and accurate.</p>
<p>![](user-guide-ves-6-3/041.png)</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>Scroll down to the <strong>Rules…</strong> (under the <strong>Presumptive Psychosis Category</strong> definition).</td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>Confirm the added <strong>Rules…</strong> and <strong>Note</strong> are correct and accurate.</p>
<p>![](user-guide-ves-6-3/042.png)</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>Scroll down to the bottom of the <strong>Edit Current Eligibility</strong> topic.</td>
</tr>
<tr class="odd">
<td>11</td>
<td><p>Confirm the updated <strong>Edit Current Eligibility</strong> screen shot with the added fields of "Presumptive Psychosis Screening" and "Presumptive Psychosis Category".</p>
<p>![](user-guide-ves-6-3/043.png)</p>
<p><span id="_Toc119934836" class="anchor"></span>Figure : Edit Current Eligibility</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Eligibility History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current</strong> <strong>Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Eligibility History</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Clinical Evaluations</strong> panel.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the text under <strong>Clinical Evaluations</strong> is correct and accurate.</p>
<p>![](user-guide-ves-6-3/044.png)</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Scroll down to the <strong>Clinical Determinations</strong> panel.</td>
</tr>
<tr class="even">
<td>8</td>
<td><p>Confirm the text under <strong>Clinical Determinations</strong> has been renamed from "Other Eligibility Factors".</p>
<p>![](user-guide-ves-6-3/045.png)</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td>Scroll down to the bottom of the topic.</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>Confirm the updated <strong>Eligibility History</strong> screen shot with the added <strong>Clinical Evaluations panel</strong>, and the updated <strong>Clinical Determinations</strong> panel (renamed from "Other Eligibility Factors") screen shot are correct and accurate.</p>
<p>![](user-guide-ves-6-3/046.png)</p>
<p><span id="_Toc119934837" class="anchor"></span>Figure : Eligibility History</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Secondary Eligibility Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Primary and Secondary Eligibility Codes</strong> topic.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>Clinical Evaluation</strong> secondary eligibility code definition.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the added text regarding the <strong>Clinical Evaluation</strong> carveout VHAP assignment below is correct and accurate.</p>
<p>![](user-guide-ves-6-3/047.png)</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>Scroll down to the <strong>Presumptive Psychosis secondary eligibility code</strong> definition.</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the text under "<strong>Presumptive Psychosis secondary eligibility code</strong>" is correct and accurate.</p>
<p>![](user-guide-ves-6-3/048.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## "Presumptive (38 USC 1702-38 CFR 17.109)" Carveout VHAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Reference</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Carveout VHAPs</strong> topic.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>Presumptive (38 USC 1702-38 CFR 17.109)</strong> carveout VHAP (profile code 135) definition.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the text for the <strong>Presumptive (38 USC 1702-38 CFR 17.109)</strong> carveout VHAP is correct and accurate.</p>
<p>![](user-guide-ves-6-3/049.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## "Clinical Evaluation" Carveout VHAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Still on the <strong>Carveout VHAPs</strong> topic, scroll down to the <strong>Clinical Evaluation</strong> carveout VHAP (profile code 308) definition.</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>Confirm the text for the <strong>Clinical Evaluation</strong> carveout VHAP is correct and accurate.</p>
<p>![](user-guide-ves-6-3/050.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## EZ / 1010 EZR 2022 Form Updates:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Overview</strong> topic.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the Indian field.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the added second bullet is correct and accurate.</p>
<p>![](user-guide-ves-6-3/051.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Identity Traits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Identity Traits</strong> topic.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>Self-Identified Gender Identity (SIGI)</strong> field definition.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the updated <strong>Self-Identified Gender Identity (SIGI)</strong> field definition is correct and accurate.</p>
<p>![](user-guide-ves-6-3/052.png)</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>Scroll down to the <strong>Race</strong> field definition.</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the updated <strong>Race</strong> field definition is correct and accurate.</p>
<p>![](user-guide-ves-6-3/053.png)</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>Scroll down to the <strong>Ethnicity</strong> field definition.</td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>Confirm the updated <strong>Ethnicity</strong> field definition is correct and accurate.</p>
<p>![](user-guide-ves-6-3/054.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Personal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Personal</strong> section (still under the <strong>Demographics</strong> section).</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the <strong>Indian</strong> field definition.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the updated <strong>Indian</strong> field text is correct and accurate (third bullet).</p>
<p>![](user-guide-ves-6-3/055.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Financials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Financials</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the "Print 1010EZ" and "Print 1010EZR" fields definition.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the updated text of both field definitions are correct and accurate.</p>
<p>![](user-guide-ves-6-3/056.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Enrollment</strong> section (still under the <strong>Person Search Tabs</strong> section).</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Veteran's Online Application</strong> topic.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the updated <strong>Veteran's Online Application</strong> text is correct and accurate.</p>
<p>![](user-guide-ves-6-3/057.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Updated TPA Message Log description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Community Care</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>TPA Message Log</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the added note is correct and accurate.</p>
<p>![](user-guide-ves-6-3/058.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Updated VCE Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Admin</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Click the <strong>VCE Parameter</strong> topic.</p>
<p><strong>Note:</strong> Veteran's Choice Eligibility (VCE).</p></td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the updated VCE Parameters definition is correct and accurate.</p>
<p>![](user-guide-ves-6-3/059.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Updated COMPACT Act Error Message on UI description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit Current Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Non-Veteran Eligibility Codes</strong> section.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Scroll down to the <strong>COMPACT Act (Override)</strong> radio button definition.</p>
<p><strong>Note:</strong> Veterans Comprehensive Prevention, Access to Care, and Treatment (COMPACT) Act of 2020.</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the added <strong>COMPACT Act (Override)</strong> radio button definition is correct and accurate (located at the very bottom of topic).</p>
<p>![](user-guide-ves-6-3/060.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## National Service Desk and Other Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 10%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Org</strong></th>
<th><strong>Contact Info</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OIT National Service Desk</td>
<td>OIT</td>
<td><ul>
<li><p>Agent Live Chat: Click the "Chat with us now" button in the lower right corner of the <a href="https://yourit.va.gov/va">yourIT Service portal</a> to launch Abel the Chatbot and type "chat with agent"</p></li>
<li><p>Self-Service: <a href="https://yourit.va.gov/va?id=sc_cat_item&amp;sys_id=3f1dd0320a0a0b99000a53f7604a2ef9">Create Incident</a></p></li>
<li><p>Phone: 855-673-4357</p></li>
<li><p>TTY (hearing-impaired only): 844-224-6186</p></li>
</ul></td>
</tr>
<tr class="even">
<td>VistA Patch Maintenance</td>
<td>OIT</td>
<td>Use the <a href="https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fyourit.va.gov%2Fva&amp;data=04%7C01%7C%7C7cee1b845c4d45ac27c908d8f878e8d3%7Ce95f1b23abaf45ee821db7ab251ab3bf%7C0%7C0%7C637532545466475272%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&amp;sdata=%2BFNyBzTgubTLPLgEKu9ZpkUQaKyiuSjmYUqrYK0jeOI%3D&amp;reserved=0">yourIT Service portal</a> – A ServiceNOW (SNOW) ticket is entered and the ticket assigned to the "NTL SUP Admin Team".</td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

## Browser & Operating System Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VES is functional through Windows using Chrome or Edge.

7.  Internet Explorer (IE) and Firefox are not supported browsers. Users who have permission to have Firefox should not be using it to access VES.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: User Guide VES 6.0

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Quick Start uses several methods to highlight different aspects of the material.

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

## Demographics screen field updates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section from the table of contents to the left of the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Click the <strong>Identity Traits</strong> topic.</p>
<p>![](user-guide-ves-6-0/028.png)</p>
<p><span id="_Toc96438332" class="anchor"></span>Figure 8: Identity Traits screen</p></td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Scroll down to the <strong>Race</strong> field. The following text and rules have been added:</p>
<p>![](user-guide-ves-6-0/029.png)</p>
<p><span id="_Toc96438333" class="anchor"></span>Figure 9: Race field on Identity Traits screen</p>
<p>![](user-guide-ves-6-0/030.png)</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Scroll down to the <strong>Ethnicity</strong> field. The following text and rules have been added:</p>
<p>![](user-guide-ves-6-0/031.png)</p>
<p><span id="_Toc96438334" class="anchor"></span>Figure 10: Ethnicity on Identity Traits screen</p>
<p>![](user-guide-ves-6-0/032.png)</p></td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Click the <strong>Identity Traits (Add a Person)</strong> topic on the table of contents.</p>
<p>![](user-guide-ves-6-0/033.png)</p>
<p><span id="_Toc96438335" class="anchor"></span>Figure 11: Identity Traits on Add a Person (AAP) screen</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Scroll down to the <strong>Race</strong> field. The following text and rules have been added:</p>
<p>![](user-guide-ves-6-0/034.png)</p>
<p>![](user-guide-ves-6-0/035.png)</p></td>
</tr>
<tr class="even">
<td>8</td>
<td><p>Scroll down to the <strong>Ethnicity</strong> field. The following text and rules have been added:</p>
<p>![](user-guide-ves-6-0/036.png)</p>
<p>![](user-guide-ves-6-0/037.png)</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td>Click the <strong>Personal</strong> section on the table of contents.</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>Click the <strong>Personal</strong> topic.</p>
<p>![](user-guide-ves-6-0/038.png)</p>
<p><span id="_Toc96438336" class="anchor"></span>Figure 12: Personal screen</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td><p>Scroll down to the <strong>Benefit Applied For</strong> field. The newly added text is as follows:</p>
<p>![](user-guide-ves-6-0/039.png)</p>
<p><span id="_Toc96438337" class="anchor"></span>Figure 13: Benefit Applied For dropdown on the Personal screen</p>
<p>![](user-guide-ves-6-0/040.png)</p></td>
</tr>
<tr class="even">
<td>12</td>
<td><p>Scroll down to the <strong>Marital Status</strong> field. The newly added text is as follows:</p>
<p>![](user-guide-ves-6-0/041.png)</p>
<p><span id="_Toc96438338" class="anchor"></span>Figure 14: Marital Status dropdown on the Personal screen</p>
<p>![](user-guide-ves-6-0/042.png)</p></td>
</tr>
<tr class="odd">
<td>13</td>
<td><p>Scroll down to the <strong>Religion</strong> field. The newly added text is as follows:</p>
<p>![](user-guide-ves-6-0/043.png)</p>
<p><span id="_Toc96438339" class="anchor"></span>Figure 15: Religion dropdown on the Personal screen</p>
<p>![](user-guide-ves-6-0/044.png)</p></td>
</tr>
<tr class="even">
<td>14</td>
<td><p>Click the <strong>Personal (Add a Person)</strong> topic on the table of contents.</p>
<p>![](user-guide-ves-6-0/045.png)</p>
<p><span id="_Toc96438340" class="anchor"></span>Figure 16: Personal on Add a Person (AAP) screen</p></td>
</tr>
<tr class="odd">
<td>15</td>
<td><p>Scroll down to the <strong>Benefit Applied For</strong> field. The newly added note is as follows:</p>
<p>![](user-guide-ves-6-0/046.png)</p>
<p><span id="_Toc96438341" class="anchor"></span>Figure 17: Benefit Applied For field on the Personal (AAP) screen</p>
<p>![](user-guide-ves-6-0/047.png)</p></td>
</tr>
<tr class="even">
<td>16</td>
<td><p>Scroll down to the <strong>Marital Status</strong> field. The newly added note is as follows:</p>
<p>![](user-guide-ves-6-0/048.png)</p>
<p><span id="_Toc96438342" class="anchor"></span>Figure 18: Marital Status on the Personal (AAP) screen</p>
<p>![](user-guide-ves-6-0/049.png)</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td><p>Scroll down to the <strong>Religion</strong> field. The newly added note is as follows:</p>
<p>![](user-guide-ves-6-0/050.png)</p>
<p><span id="_Toc96438343" class="anchor"></span>Figure 19: Religion field on the Personal (AAP) screen</p>
<p>![](user-guide-ves-6-0/051.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Demographics and VA Profile 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents of the online help.</td>
</tr>
<tr class="even">
<td>1</td>
<td><p>Click the <strong>Overview</strong> topic under the <strong>Demographics</strong> section.</p>
<p>RESULT: The <strong>Overview</strong> topic displays.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Scroll down to the <strong>Demographics and VA Profile</strong> dropdown link.</td>
</tr>
<tr class="even">
<td>3</td>
<td><p>Click the <strong>Demographics and VA Profile</strong> dropdown link. The following text ahas been added:</p>
<p>![](user-guide-ves-6-0/052.png)</p></td>
</tr>
</tbody>
</table>

## Demographics Overview Subtab Order Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section from the table of contents to the left of the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Overview</strong> topic.</td>
</tr>
<tr class="even">
<td>5</td>
<td><p>The Demographics Overview subtabs are the following order:</p>
<ul>
<li><p>Overview</p></li>
<li><p>Identity Traits</p></li>
<li><p>Personal</p></li>
<li><p>Addresses</p></li>
<li><p>Associates</p></li>
<li><p>Insurance</p></li>
</ul>
<p>![](user-guide-ves-6-0/053.png)</p>
<p>![](user-guide-ves-6-0/054.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## CP&E Veterans Health Administration Profile (VHAP) Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section from the table of contents to the left of the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Reference</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profile</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Carveout VHAPs</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>The CP&amp;E VHAPs include:</p>
<ul>
<li><p>CHAMPVA Standard (108)</p></li>
</ul>
<p>![](user-guide-ves-6-0/055.png)</p>
<p><span id="_Toc96438344" class="anchor"></span>Figure 20: CHAMPVA VHAP</p>
<ul>
<li><p>Beneficiary Spina Bifida (109)</p></li>
</ul>
<p>![](user-guide-ves-6-0/056.png)</p>
<p><span id="_Toc96438345" class="anchor"></span>Figure 21: Beneficiary Spina Bifida VHAP</p>
<ul>
<li><p>Beneficiary Children of Women of Vietnam Veterans (110)</p></li>
</ul>
<p>![](user-guide-ves-6-0/057.png)</p>
<p><span id="_Toc96438346" class="anchor"></span>Figure 22: Beneficiary Children of Women of Vietnam Veterans VHAP</p>
<ul>
<li><p>Veteran Foreign Medical Program (122)</p></li>
</ul>
<p>![](user-guide-ves-6-0/058.png)</p>
<p><span id="_Toc96438347" class="anchor"></span>Figure 23: Veteran Foreign Medical Program VHAP</p>
<ul>
<li><p>CHAMPVA Caregiver (305)</p></li>
</ul>
<p>![](user-guide-ves-6-0/059.png)</p>
<p><span id="_Toc96438348" class="anchor"></span>Figure 24: CHAMPVA Caregiver VHAP</p>
<ul>
<li><p>Camp Lejeune Family (306)</p></li>
</ul>
<p>![](user-guide-ves-6-0/060.png)</p>
<p><span id="_Toc96438349" class="anchor"></span>Figure 25: Camp Lejeune Family VHAP</p>
<p><em><strong>CHAMPVA Standard (108)</strong></em></p>
<p>![](user-guide-ves-6-0/061.png)</p>
<p><em><strong>Beneficiary Spina Bifida (109)</strong></em></p>
<p>![](user-guide-ves-6-0/062.png)</p>
<p><em><strong>Beneficiary Children of Women of Vietnam Veterans (110)</strong></em></p>
<p>![](user-guide-ves-6-0/063.png)</p>
<p><em><strong>Veteran Foreign Medical Program (122)</strong></em></p>
<p>![](user-guide-ves-6-0/064.png)</p>
<p><em><strong>Camp Lejeune Family (306)</strong></em></p>
<p>![](user-guide-ves-6-0/065.png)</p>
<p><em><strong>CHAMPVA Caregiver (305)</strong></em></p>
<p>![](user-guide-ves-6-0/066.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Carveout VHAP Updates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section from the table of contents to the left of the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Reference</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Click the <strong>Carveout VHAPs</strong> topic. The following updated Carveout VHAPs include:</p>
<ul>
<li><p>VA DoD Direct Resource Sharing Agreements (295)</p></li>
</ul>
<p>![](user-guide-ves-6-0/067.png)</p>
<p><span id="_Toc96438350" class="anchor"></span>Figure 26: VA DoD Direct Resource Sharing Agreements VHAP</p>
<ul>
<li><p>TRICARE (229)</p></li>
</ul>
<p>![](user-guide-ves-6-0/068.png)</p>
<p><span id="_Toc96438351" class="anchor"></span>Figure 27: TRICARE VHAP</p>
<ul>
<li><p>Active Duty (303)</p></li>
</ul>
<p>![](user-guide-ves-6-0/069.png)</p>
<p><span id="_Toc96438352" class="anchor"></span>Figure 28: Active Duty VHAP</p>
<ul>
<li><p>Joint Incentive Fund (304)</p></li>
</ul>
<p>![](user-guide-ves-6-0/070.png)</p>
<p><span id="_Toc96438353" class="anchor"></span>Figure 29: Joint Incentive Fund</p>
<p><em><strong>VA DoD Direct Resource Sharing Agreements (295)</strong></em></p>
<p>![](user-guide-ves-6-0/071.png)</p>
<p><em><strong>TRICARE (229)</strong></em></p>
<p>![](user-guide-ves-6-0/072.png)</p>
<p><em><strong>Active Duty (303)</strong></em></p>
<p>![](user-guide-ves-6-0/073.png)</p>
<p><em><strong>Joint Incentive Fund (304)</strong></em></p>
<p>![](user-guide-ves-6-0/074.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Enrollment updates: Application Signature Date and Application Method 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section from the table of contents to the left of the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Enrollment</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Click the <strong>Enrollment</strong> topic. The following screen has been updated to continue displaying the following fields after "Add a Person" is complete:</p>
<ul>
<li><p>Application Signature Date</p></li>
<li><p>Application Method</p></li>
</ul>
<p>![](user-guide-ves-6-0/075.png)</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>View Historical Enrollment</strong> topic under the <strong>Enrollment</strong> section on the table of contents of the Online Help.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following fields have been added to the <strong>View Historical Enrollment</strong> screen.</p>
<ul>
<li><p>Application Signature Date</p></li>
<li><p>Application Method</p></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td>![](user-guide-ves-6-0/076.png)</td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Four New Self-Reported Registration Reasons 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section from the table of contents to the left of the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit Current Eligibility</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Scroll down to the <strong>Self-Reported Registration Only Reasons</strong> section. The following new reasons added include:</p>
<ul>
<li><p>4<sup>th</sup> Mission</p></li>
<li><p>Clinical Evaluation</p></li>
<li><p>HUD-VASH</p></li>
<li><p>Immunizations</p></li>
</ul>
<p>![](user-guide-ves-6-0/077.png)</p>
<p>![](user-guide-ves-6-0/078.png)</p></td>
</tr>
<tr class="even">
<td></td>
<td>Click back to the <strong>Current Eligibility</strong> section from the table of contents to the left of the Online Help.</td>
</tr>
<tr class="odd">
<td></td>
<td>Click the <strong>Edit Current Eligibility (Add a Person)</strong> topic.</td>
</tr>
<tr class="even">
<td></td>
<td><p>Scroll down to the <strong>Self-Reported Registration Only Reasons</strong> section. The following new reasons added include:</p>
<ul>
<li><p>4<sup>th</sup> Mission</p></li>
<li><p>Clinical Evaluation</p></li>
<li><p>HUD-VASH</p></li>
<li><p>Immunizations</p></li>
</ul>
<p>![](user-guide-ves-6-0/079.png)</p>
<p>![](user-guide-ves-6-0/080.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## "EHBD" Updated to "E&E"

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

| Step | Action                                                                                                                                                                                                                                                             |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Click the Search icon ![](user-guide-ves-6-0/081.png) from the table of contents to the left of the Online Help. |
| 2        | Type in "EHBD" the search field section.                                                                                                                                                                                                                               |
| 3        | Confirm "E&E" has been noted as the replacement for "EHBD".                                                                                                                                                                                                            |

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Updated "Enrollment System" and "VES" to "Veterans Health Administration (VHA) Enrollment System (VES)" and "VES" 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Search</strong> icon ![](user-guide-ves-6-0/082.png) from the table of contents to the left of the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Type in "VES" the search field section. "Enrollment System" and "VES" has been replaced with "Veterans Health Administration (VHA)" and "VES" throughout the VES Online Help and VES quick start-user guide.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Enrollment System (VES)</strong> topic on the table of contents.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Scroll down to the <strong>Overview</strong> section. The following sentence has been added detailing the renaming of "ES" to "VES".</p>
<p>![](user-guide-ves-6-0/083.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### From: User Guide VES 6.1

## U.S. Department of Housing and Urban Development-VA Supportive Housing (HUD-VASH) updates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Reference</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Carveout VHAP</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Scroll down to the very bottom carveout VHAP on the carveout VHAP table.</p>
<p><strong>HUD-VASH Restricted Care</strong></p>
<p><strong>Code: 307</strong></p>
<p>![](user-guide-ves-6-1/028.png)</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>Navigate back to the table contents.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Click the <strong>Person Search Tabs</strong> section.</td>
</tr>
<tr class="even">
<td>8</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>10</td>
<td>Click the <strong>Edit Current Eligibility</strong> topic.</td>
</tr>
<tr class="odd">
<td>11</td>
<td><p>Confirm the new <strong>HUD-VASH</strong> field in the screen shot below.</p>
<p>![](user-guide-ves-6-1/029.png)</p>
<p><span id="_Toc103584041" class="anchor"></span>Figure 8: HUD-VASH field on the Edit Current Eligibility screen</p></td>
</tr>
<tr class="even">
<td>12</td>
<td><p>Scroll down to the <strong>HUD-VASH Non-Veteran Eligibility Code</strong> field. The following text and rules have been added:</p>
<p>![](user-guide-ves-6-1/030.png)</p>
<p>![](user-guide-ves-6-1/031.png)</p>
<p>![](user-guide-ves-6-1/032.png)</p>
<p>![](user-guide-ves-6-1/033.png)</p>
<p>![](user-guide-ves-6-1/034.png)</p></td>
</tr>
<tr class="odd">
<td>13</td>
<td>Navigate back to the table of contents.</td>
</tr>
<tr class="even">
<td>14</td>
<td>Click the <strong>Edit Current Eligibility (Add a Person)</strong> topic (still under the <strong>Current Eligibility</strong> section).</td>
</tr>
<tr class="odd">
<td>15</td>
<td><p>Confirm the new <strong>HUD-VASH</strong> field on the screenshot below.</p>
<p>![](user-guide-ves-6-1/035.png)</p>
<p><span id="_Toc103584042" class="anchor"></span>Figure 9: HUD-VASH field on the Edit Current Eligibility (AAP) screen</p></td>
</tr>
<tr class="even">
<td>16</td>
<td><p>Scroll down to the <strong>HUD-VASH Non-Veteran Eligibility Code</strong> field. The following text and rules have been added:</p>
<p>![](user-guide-ves-6-1/036.png)![](user-guide-ves-6-1/037.png)![](user-guide-ves-6-1/038.png)</p>
<p>![](user-guide-ves-6-1/039.png)</p>
<p>![](user-guide-ves-6-1/040.png)</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td>Click the <strong>Person Search Tabs</strong> section from the table of contents to the left of the Online Help.</td>
</tr>
<tr class="even">
<td>18</td>
<td>Click the <strong>Eligibility</strong> section</td>
</tr>
<tr class="odd">
<td>19</td>
<td>Click the <strong>Primary and Secondary Eligibility Codes</strong> topic.</td>
</tr>
<tr class="even">
<td>20</td>
<td>Scroll down to the <strong>Non-Veteran Eligibility Codes</strong> section with a list of a 1-10.</td>
</tr>
<tr class="odd">
<td>21</td>
<td><p>Confirm the added HUD-VASH text is correct as listed as number "10".</p>
<p>![](user-guide-ves-6-1/041.png)</p>
<p><span id="_Toc103584043" class="anchor"></span>Figure : HUD-VASH Non-Veteran Secondary Eligibility Code</p></td>
</tr>
<tr class="even">
<td>22</td>
<td><p>Scroll down to the <strong>Secondary Eligibility Codes</strong> section. HUD-VASH has been added as number "9" under the "Non-Veteran Eligibility Codes" section:</p>
<p>![](user-guide-ves-6-1/042.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Community Care Hardship Expiration Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Admin</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>E&amp;E Service</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>E&amp;E Service</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Scroll down to the very bottom of the <strong>E&amp;E Service</strong> topic. The following text and screen shot were added.</p>
<p>![](user-guide-ves-6-1/043.png)</p>
<p>![](user-guide-ves-6-1/044.png)</p>
<p><span id="_Toc103584044" class="anchor"></span>Figure : Hardship Expires</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Organized Extract Reports into Their Own Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Reports</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Report Descriptions</strong> topic.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Scroll down to the very bottom of the <strong>Report Descriptions</strong> topic until you reach "Extract Reports". The following "Extract Reports" section was added:</p>
<p>![](user-guide-ves-6-1/045.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## OIT Homeless Program Report Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Reports</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Report Descriptions</strong> topic.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Scroll down to the very bottom of the <strong>Report Descriptions</strong> topic until you reach "Extract Reports". The following report text was added:</p>
<p>![](user-guide-ves-6-1/046.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## VES Auto-Locks Accounts Inactive 90-Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>VES Overview</strong> section.</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>Click the <strong>VES Inactive Accounts</strong> topic. The following report text was added:</p>
<p>![](user-guide-ves-6-1/047.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Financials Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Financials</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Click the <strong>Financial Details</strong> topic. The following outdated text was removed from this topic:</p>
<p><del><strong>Note:</strong> The rules for setting GMT Copay Required or Pending Adjudication were changed beginning in calendar year 2010. This General Counsel ruling affected the Priority Group assigned to the Veteran.</del></p>
<p><del>Effective July 24th, 2014, the setting for "GMT Copay Required" or "Pending Adjudication", that had changed for those Veterans who met the Income and Net Worth ranges as described under the field "<em><strong><u>Do you want to send this for Adjudication?</u></strong></em>" below has been discontinued.</del></p>
<p><del>Veterans who had very low income where the GMT Threshold is less than the MTT and the person's net income is less than or equal to the GMTT, yet their net income plus assets was greater than the Net Worth Threshold, will be placed in Priority Group 7 is also no longer valid as of July 24th, 2014.</del></p>
<p><strong><del><u>Edit Financial Details (Income Year XXXX)</u></del></strong></p>
<blockquote>
<p><em><del><strong>Do you want to send this for Adjudication?: (Required)</strong> (Discontinued July 24th, 2014)</del></em></p>
<p><del>This displays only when after completing a current Means Test and the evaluation of total computed income, MT and GMT Thresholds. Threshold determines the means test status could be one of three statuses:</del></p>
<p><del>When the GMT Threshold is greater than the MT Threshold and the user selects:</del></p>
</blockquote>
<ul>
<li><blockquote>
<p><del>Yes - Outcome will be "MT Copay Required" or "GMT Copay Required".</del></p>
</blockquote></li>
<li><blockquote>
<p><del>No - MT Status will be set to GMT Copay Required.</del></p>
</blockquote></li>
</ul>
<blockquote>
<p><del>or</del></p>
<p><del>When the GMT Threshold is less than or equal to the MT Threshold and the user selects:</del></p>
</blockquote>
<ul>
<li><blockquote>
<p><del>Yes - MT Status will be set to Pending Adjudication.</del></p>
</blockquote></li>
<li><blockquote>
<p><del>No - If Net Income is greater than the GMT Threshold, MT Status will be set to MT Copay Required.</del></p>
</blockquote></li>
<li><blockquote>
<p><del>No - If Net Income is less than or equal to the GMT Threshold, MT Status will be set to GMT Copay Required.</del></p>
</blockquote></li>
</ul>
<p><strong><del><u>Assets</u></del></strong></p>
<p><del>On the <strong>Assets</strong> panel, the following fields are now disabled as of the 5.13 release; September 2020. Users can no longer enter data into these fields:</del></p>
<ul>
<li><p><del>Cash and Bank Account Balance</del></p></li>
<li><p><del>Land, Buildings Less Mortgage, and Liens</del></p></li>
<li><p><del>Other Property of Assets</del></p></li>
</ul>
<p><del>Disabling these fields prevents the supplemental adjudication question from being presented. The supplemental adjudication question is no longer required as part of the financial assessment process used to assign a Veteran's enrollment priority group, copay responsibilities and other benefits and should no longer be presented in any financial assessment scenario. VES will hide the three fields when completing a new Income Test OR viewing a historical Income Test with no values (zero or no data). Existing records display read-only values (greater than zero only) in the three fields ("Cash and Bank Account Balance", "Land, Buildings Less Mortgage, and Liens", and "Other Property of Assets") if they are on file for historical Income Tests.</del></p>
<p><del><strong>Note:</strong> VES users can enter a single "Income Test" each year for a record. The financial information entered as part of the "Income Test" will be used to automatically create a "Means Test" and/or "RX Copay/Pharmacy Test" depending on the type of financial testing that the Beneficiary is subject to.</del></p>
<ul>
<li><p><del>Income Test: Single test entered in VES that is used to gather financial information.</del></p></li>
<li><p><del>Means Test: If a Beneficiary is subject to means testing, information from the income test is used to create a means test. The status of the means test determines if the Beneficiary will be required to make copayments for treatment.</del></p></li>
<li><p><del>RX Copay/Pharmacy Test: If a Beneficiary is subject to RX Copay/Pharmacy testing, information from the income test is used to create a RX Copay/Pharmacy test. The status of the RX Copay/Pharmacy test determines if the Beneficiary will be required to make copayments for prescription medications.</del></p></li>
<li><p><del>Long Term Care (LTC) Test: If a Beneficiary is subject to Long Term Care testing, a separate Long Term Care (LTC) test will be completed. The status of the Long Term Care test determines if the Beneficiary will be required to make copayments for long term care services.</del></p></li>
</ul>
<p><strong><del>Means Test Pending Adjudication Status Changes</del></strong></p>
<p><del>The Means Test calculation is being updated to assure multiple things: (1) that new Means Tests are not put in a "Pending Adjudication" status forever, (2) that the Veteran is not placed in a priority group he or she does not qualify for; and (3) that the Veteran does not incorrectly appear to be waiting for adjudication of his or her means test. The outcome of these changes is that a new Means Test will no longer be placed in a "Pending Adjudication" status.</del></p>
<p><strong><del><u>Debts (pre-Feb. 2005 format):</u></del></strong></p>
<blockquote>
<p><em><strong><del>$:</del></strong></em></p>
<p><del>Here is where all debts are individually entered for the Veteran and Spouse only. Debt information is only collected for the pre-Feb 2005 Format Tests.</del></p>
<p><del>This data is shared with VistA.</del></p>
<p><em><strong><del>Rules...</del></strong></em></p>
</blockquote>
<ul>
<li><p><del><em>Debts</em> must be a dollar amount 0 to 9999999.00.</del></p></li>
<li><p><del><em>Debts</em> for a person cannot exceed the dollar amount in the asset type of Other Property or Assets amount for that same person.</del></p></li>
</ul></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Add Spouse (Financials Update)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents of the VES Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Financials</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Dependents</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Add/Edit Spouse</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the <strong>Add Spouse</strong> topic.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the added screen shots:</p>
<p>![](user-guide-ves-6-1/048.png)</p>
<p>![](user-guide-ves-6-1/049.png)</p>
<p><span id="_Toc103584045" class="anchor"></span>Figure 12: Add a Spouse (Before Registration)</p>
<p>![](user-guide-ves-6-1/050.png)</p>
<p>![](user-guide-ves-6-1/051.png)</p>
<p><span id="_Toc103584046" class="anchor"></span>Figure 13: Add a Spouse (After Registration)</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Scroll down to the following updated fields and confirm if the definitions are correct and accurate.</p>
<p>![](user-guide-ves-6-1/052.png)</p></td>
</tr>
<tr class="even">
<td>8</td>
<td><p>Scroll down to the following updated fields and confirm if the definitions are correct and accurate.</p>
<p>![](user-guide-ves-6-1/053.png)</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>Scroll down to the following updated fields and confirm if the definitions are correct and accurate.</p>
<p>![](user-guide-ves-6-1/054.png)</p>
<p>![](user-guide-ves-6-1/055.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## VDL Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>VES Overview</strong> section.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Acronyms and Definitions</strong> topic.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the "V" link located at the top of the topic.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Scroll down to the "VA Software Document Library" definition. Confirm the definition is correct and accurate.</p>
<p>![](user-guide-ves-6-1/056.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### From: User Guide VES 6.5

## Extend Combat Veteran Eligibility End Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Military Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the updated <strong>Military Service</strong> screen shot is correct and accurate. The Service Separation Date has been updated from 11/11/98 to 09/30/2013.</p>
<p>![](user-guide-ves-6-5/028.png)</p>
<p><span id="_Toc130894877" class="anchor"></span>Figure : Service Separation Date (Military Service)</p>
<p>Confirm that the updated requirements text in the <strong>Combat Veteran Eligibility End Date</strong> section is accurate and correct. This text has been added to further detail the requirements for each priority group for the Combat Veteran Eligible population.</p>
<p>![](user-guide-ves-6-5/029.png)</p>
<p><span id="_Toc130894878" class="anchor"></span>Figure : Updated Combat Veteran Eligibility End Date Help Text</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Add Agent Orange and Ionizing Radiation Exposure Locations in VES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility → Current Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Scroll down to the <strong>Reason Eligibility Status is Pending Verification</strong> information and verify that the included information is correct.</p>
<p>![](user-guide-ves-6-5/030.png)</p>
<p><span id="_Toc130894879" class="anchor"></span>Figure : Reason Eligibility Status is Pending Verification</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Eligibility History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Eligibility History</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Scroll down to the <strong>Reason Eligibility Status is Pending Verification</strong> information and verify that the included information is correct.</p>
<p>![](user-guide-ves-6-5/031.png)</p>
<p><span id="_Toc130894880" class="anchor"></span>Figure : Reason Eligibility Status is Pending Verification</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Current Eligibility → Edit Current Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit Current</strong> <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Agent Orange Exposure Location</strong> definition and information and then to the <strong>Radiation Exposure Method</strong> definition and information directly below.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the added <strong>Agent Orange Exposure Location</strong> information and the added <strong>Radiation Exposure Method</strong> information and screen shots are correct and accurate.</p>
<p>![](user-guide-ves-6-5/032.png)</p>
<p><span id="_Toc130894881" class="anchor"></span>Figure : Agent Orange Exposure Location List</p>
<p>![](user-guide-ves-6-5/033.png)</p>
<p><span id="_Toc130894882" class="anchor"></span>Figure : Radiation Exposure Method List</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Scroll down to the <strong>Reason Eligibility Status is Pending Verification</strong> information and verify that the included information is correct.</p>
<p>![](user-guide-ves-6-5/034.png)</p>
<p><span id="_Toc130894883" class="anchor"></span>Figure 14: Reason Eligibility Status is Pending Verification</p></td>
</tr>
<tr class="even">
<td>8</td>
<td><p>Scroll down to the <strong>Eligibility Reason Status Codes</strong> table and verify that the included information is correct.</p>
<p>![](user-guide-ves-6-5/035.png)</p>
<p><span id="_Toc130894884" class="anchor"></span>Figure 15: Eligibility Reason Status Codes</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Current Eligibility → Edit Currently Eligibility (Add a Person)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit Current</strong> <strong>Eligibility (Add a Person)</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Agent Orange Exposure Location</strong> definition and information and then to the <strong>Radiation Exposure Method</strong> definition and information directly below.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the added <strong>Agent Orange Exposure Location</strong> information and the added <strong>Radiation Exposure Method</strong> information and screen shots are correct and accurate.</p>
<p>![](user-guide-ves-6-5/036.png)</p>
<p><span id="_Toc130894885" class="anchor"></span>Figure : Agent Orange Exposure Location List</p>
<p>![](user-guide-ves-6-5/037.png)</p>
<p><span id="_Toc130894886" class="anchor"></span>Figure : Radiation Exposure Method List</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Scroll down to the <strong>Eligibility Reason Status Codes</strong> table and verify that the included information is correct.</p>
<p>![](user-guide-ves-6-5/038.png)</p>
<p><span id="_Toc130894887" class="anchor"></span>Figure 18: Eligibility Reason Status Codes</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Edit Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

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
<td>1</td>
<td>Click the <strong>Person Search</strong> option in the VHA Enrollment System (VES).</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> tab.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Edit Eligibility</strong> tab.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down and click <strong>Other Eligibility Factors.</strong></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the dropdown menu for <strong>Agent Orange Exposure Location.</strong></td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the added <strong>Agent Orange Exposure Locations</strong> are correct and confirm the updated <strong>Agent Orange Exposure Location</strong> screen shot is accurate.</p>
<p>![](user-guide-ves-6-5/039.png)</p>
<p><span id="_Toc130894888" class="anchor"></span>Figure : Agent Orange Exposure Location Drop-Down Menu (Edit Eligibility)</p></td>
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
<td>1</td>
<td>Click the <strong>Person Search</strong> option in the VHA Enrollment System (VES).</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> tab.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Edit Eligibility</strong> tab.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down and click <strong>Other Eligibility Factors.</strong></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the dropdown menu for <strong>Radiation Exposure Method.</strong></td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the added <strong>Radiation Exposure Methods</strong> are correct and confirm the updated <strong>Radiation Exposure Method</strong> screen shot is accurate.</p>
<p>![](user-guide-ves-6-5/040.png)</p>
<p><span id="_Toc130894889" class="anchor"></span>Figure : Radiation Exposure Method Drop-Down Menu (Edit Eligibility)</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Military Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

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
<td>1</td>
<td>Click the <strong>Person Search</strong> option in the VHA Enrollment System (VES).</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> tab.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the <strong>Agent Orange Exposure Location.</strong></td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the added <strong>Agent Orange Exposure Locations</strong> and confirm the updated <strong>Agent Orange Exposure Location</strong> screen shot is accurate.</p>
<p>![](user-guide-ves-6-5/041.png)</p>
<p><span id="_Toc130894890" class="anchor"></span>Figure : Agent Orange Exposure Location Drop-Down Menu (Military Service)</p></td>
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
<td>1</td>
<td>Click the <strong>Person Search</strong> option in the VHA Enrollment System (VES).</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> tab.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the <strong>Radiation Exposure Method.</strong></td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the added <strong>Radiation Exposure Methods</strong> and confirm the updated <strong>Radiation Exposure Methods</strong> screen shot is accurate.</p>
<p>![](user-guide-ves-6-5/042.png)</p>
<p><span id="_Toc130894891" class="anchor"></span>Figure : Radiation Exposure Method Drop-Down Menu (Military Service)</p></td>
</tr>
</tbody>
</table>

### Confirm the following Online Help updates.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<td>1</td>
<td>Click the <strong>Person Search</strong> option in the VHA Enrollment System (VES).</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> tab.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the <strong>Military Service Episodes – HEC.</strong></td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Click "Delete" which will prompt the following pop-up:</p>
<p>![](user-guide-ves-6-5/043.png)</p>
<p><span id="_Toc130894892" class="anchor"></span>Figure : MSE Information Deletion Pop-Up</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Click "OK" on the pop-up and then scroll down to the bottom and click the "Update" option. Confirm that the following pop-up will now appear:</p>
<p>![](user-guide-ves-6-5/044.png)</p>
<p><span id="_Toc130894893" class="anchor"></span>Figure : MSE Information Deletion and Update Pop-Up</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Enrollment → Current Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Enrollment</strong> tab.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Enrollment</strong> tab.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>Source of Enrollment</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the added <strong>Source of Enrollment</strong> information and screen shot are correct and accurate.</p>
<p>![](user-guide-ves-6-5/045.png)</p>
<p><span id="_Toc130894894" class="anchor"></span>Figure : Agent Orange and Ionizing Radiation Factors (Source of Enrollment)</p></td>
</tr>
</tbody>
</table>

Confirm the following Online Help updates.

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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Enrollment</strong> tab.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Enrollment</strong> tab.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>Enrollment Statuses</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the added <strong>Pending; Proof of PACT Act</strong> information added to the Enrollment Status table and the provided screen shot are correct and accurate.</p>
<p>![](user-guide-ves-6-5/046.png)</p>
<p><span id="_Toc130894895" class="anchor"></span>Figure : Pending; Proof of PACT Act (Enrollment Statuses Table)</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Military Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> tab.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the <strong>Agent Orange</strong> &amp; <strong>Radiation Exposure Method</strong> sections.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the added <strong>Agent Orange</strong> &amp; <strong>Radiation Exposure Method</strong> information is correct and accurate.</p>
<p>![](user-guide-ves-6-5/047.png)</p>
<p><span id="_Toc130894896" class="anchor"></span>Figure : Agent Orange Exposure Location List (Military Service)</p>
<p>![](user-guide-ves-6-5/048.png)</p>
<p><span id="_Toc130894897" class="anchor"></span>Figure : Radiation Exposure Method List (Military Service)</p></td>
</tr>
</tbody>
</table>

### From: User Guide VES 6.6

## Create new COMPACT Eligibility Rules for Registration Only and Pending Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Overview</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the updated <strong>Overview</strong> screen shot is correct and accurate. The COMPACT Act Eligible Indicator information has been updated.</p>
<p>![](user-guide-ves-6-6/028.png)</p>
<p><span id="_Toc136875533" class="anchor"></span>Figure : COMPACT Act Eligible Indicator Rules</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Primary and Secondary Eligibility Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Primary and Secondary Eligibility Codes</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Scroll down to the "COMPACT Act Eligible" Secondary Eligibility Rule Scenarios section and verify that the updated table is correct.</p>
<p>![](user-guide-ves-6-6/029.png)</p>
<p><span id="_Toc136875534" class="anchor"></span>Figure : "COMPACT Act Eligible" Secondary Eligibility Rule Scenarios Table</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Current Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit</strong> <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Scroll down to the <strong>Ineligible Reason: (Required if an Ineligible Date is entered)</strong> information and verify that the included information is correct.</p>
<p><strong>Removed Text</strong>: "When the user accepts the changes, the eligibility fields assign "COMPACT Act Eligible" with Code 24 (and abbreviation "COMPACT"), "Dishonorable VA or FFP" core VHAP, and a CCP VCE status of "Restricted" (R) or "Ineligible" (X).</p>
<p>![](user-guide-ves-6-6/030.png)</p>
<p><span id="_Toc136875535" class="anchor"></span>Figure : Rules for Ineligible Reason</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Change Indian Capability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Demographics → Personal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Scroll down to the <strong>Indian</strong> section and verify that the included information is correct.</p>
<p><strong>Removed Text:</strong></p>
<ul>
<li><p>VES displays the Veteran's "Yes" or "No" response to the ARE YOU AN INDIAN? question from the 10-10EZ or 10-10EZR form.</p></li>
<li><p>Attestation Date, Start Date, End Date, and Reversal Reason are hidden until the "Indian" field is set to "Yes" or "No".</p></li>
<li><p>Start Date, End Date, and Reversal Reason are hidden until the "Indian" field is set to "Yes", and the Enrollment Status is VERIFIED.</p></li>
<li><p>A reversal does not remove the "Indian" status entirely.</p></li>
</ul>
<p>![](user-guide-ves-6-6/031.png)</p>
<p><span id="_Toc136875536" class="anchor"></span>Figure : Demographics (Indian)</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Scroll down to the <strong>Attestation Date</strong> section (Directly underneath <strong>Indian</strong>) and verify that the included information is correct:</p>
<p>![](user-guide-ves-6-6/032.png)</p>
<p><span id="_Toc136875537" class="anchor"></span>Figure : Demographics (Attestation Date)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Demographics → Personal → Personal (Add a Person)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Personal (Add a Person)</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Scroll down to the <strong>Indian</strong> section and verify that the included information is correct.</p>
<p><strong>Removed Text:</strong></p>
<ul>
<li><p>VES displays the Veteran's "Yes" or "No" response to the ARE YOU AN INDIAN? question from the 10-10EZ or 10-10EZR form.</p></li>
<li><p>Attestation Date, Start Date, End Date, and Reversal Reason are hidden until the "Indian" field is set to "Yes" or "No".</p></li>
<li><p>Start Date, End Date, and Reversal Reason are hidden until the "Indian" field is set to "Yes", and the Enrollment Status is VERIFIED.</p></li>
<li><p>A reversal does not remove the "Indian" status entirely.</p></li>
</ul>
<p>![](user-guide-ves-6-6/033.png)</p>
<p><span id="_Toc136875538" class="anchor"></span>Figure : Demographics (Indian - Add a Person)</p></td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Scroll down to the <strong>Attestation Date</strong> section (Directly underneath <strong>Indian</strong>) and verify that the included information is correct:</p>
<p>![](user-guide-ves-6-6/034.png)</p>
<p><span id="_Toc136875539" class="anchor"></span>Figure : Demographics (Attestation Date)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Demographics → Personal → Personal History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Personal History</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following text was accurately removed.</p>
<p>![](user-guide-ves-6-6/035.png)</p>
<p><span id="_Toc136875540" class="anchor"></span>Figure : Attestation Date (Personal History)</p>
<p><strong>Removed Text:</strong></p>
<ul>
<li><p>Reflects the "Application Stamp Date", the date the self-identified "Indian" question on the 1010EZ or 1010EZR form received by VA.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Allow "No Residential Address" Records in CC Eligibility File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Demographics → Addresses → Residential Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click on the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Addresses</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Residential Addresses</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Verify that the included information is correct.</p>
<p>![](user-guide-ves-6-6/036.png)</p>
<p><span id="_Toc136875541" class="anchor"></span>Figure : Residential Address</p>
<p><strong>Removed Text:</strong></p>
<ul>
<li><p>Residential Address is required. The VES displays the error message "Residential Address is required" when attempting to complete a registration without a Residential Address.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## VA Profile Demographics Push

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility → VHA Profiles 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click on the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>View Historical VHA Profiles</strong> section towards the bottom of the page.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Verify that the included information is correct.</p>
<p>![](user-guide-ves-6-6/037.png)</p>
<p><span id="_Toc136875542" class="anchor"></span>Figure : View Historical VHA Profiles</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## VHAP Copay Effective Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility → VHA Profiles 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click on the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Verify that the included information is correct.</p>
<p>![](user-guide-ves-6-6/038.png)</p>
<p><span id="_Toc136875543" class="anchor"></span>Figure : View Historical VHA Profiles</p>
<p>![](user-guide-ves-6-6/039.png)</p>
<p><span id="_Toc136875544" class="anchor"></span>Figure : Copay Effective Date</p>
<p>![](user-guide-ves-6-6/040.png)</p>
<p><span id="_Toc136875545" class="anchor"></span>Figure : VHA Profiles Change History Screenshot</p>
<p>Removed:</p>
<p>![](user-guide-ves-6-6/041.png)VHA Profiles Assigned – Unselect to Unassign</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Edit Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following VES updates.

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
<td>1</td>
<td>Click the <strong>Person Search</strong> option in the VHA Enrollment System (VES).</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> tab.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the <strong>VHA Profiles</strong> and click "VIEW VHA PROFILES".</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the below screenshots are accurate.</p>
<p>![](user-guide-ves-6-6/042.png)</p>
<p><span id="_Toc136875546" class="anchor"></span>Figure : VHA Profiles Update</p></td>
</tr>
<tr class="odd">
<td><strong>5</strong></td>
<td><p>Once the top screenshot is confirmed, click "VIEW HISTORICAL VHA PROFILES" and review that the following screenshot is correct.</p>
<p>![](user-guide-ves-6-6/043.png)</p>
<p><span id="_Toc136875547" class="anchor"></span>Figure : VHA Profiles Change History Update</p></td>
</tr>
</tbody>
</table>

### From: User Guide VES 6.15

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer 

This manual provides an overall explanation and functionality of Veterans Health Administration (VHA) Enrollment System (VES) 6.15.0.

![](user-guide-ves-6-15/002.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the following VES references:

- VES 6.15.0 Release Notes
- VES 6.15.0 Online Help

### Person Search Tabs → Document Management → Search Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Document Management</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Search Documents</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/029.png)</p>
<p><span id="_Toc216947425" class="anchor"></span>Figure 8: Tribal Attestation Documents Section (Search)</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Document Management → Upload Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th> <strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Document Management</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Upload Documents</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/030.png)</p>
<p><span id="_Toc216947426" class="anchor"></span>Figure 9: Tribal Attestation Documents Section (Upload)</p></td>
</tr>
</tbody>
</table>

## VES Enable 60-Day Pre-Term for Deferred Veterans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Communications → Available for Mailing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Communications</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Available for Mailing</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/031.png)</p>
<p><span id="_Toc216947427" class="anchor"></span>Figure 10: Added TERA Initial Letter</p>
<p>![](user-guide-ves-6-15/032.png)</p>
<p><span id="_Toc216947428" class="anchor"></span>Figure 11: Added TERA Initial Letter (Final Letters)</p></td>
</tr>
</tbody>
</table>

## Remove Dollar Amount Restriction for Annual Check Amount  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility → Edit Current Eligibility → Edit Current Eligibility (Add a Person)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Edit Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit Current Eligibility (Add a Person)</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/033.png)</p>
<p><span id="_Toc216947429" class="anchor"></span>Figure 12: Annual Check Amount Rules (Add a Person)</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Eligibility → Edit Current Eligibility → Edit Current Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Edit Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/034.png)</p>
<p><span id="_Toc216947430" class="anchor"></span>Figure 13: Annual Check Amount Rules</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Eligibility → Edit Current Eligibility → Prisoner of War 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Edit Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Prisoner of War</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/035.png)</p>
<p><span id="_Toc216947431" class="anchor"></span>Figure 14: Annual Check Amount Rules (POW)</p></td>
</tr>
</tbody>
</table>

## Expire Hardships 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Financials → Financial Hardship → Financial Hardship Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Financials</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Financial Hardship</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Financial Hardship Overview</strong> section</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/036.png)</p></td>
</tr>
</tbody>
</table>

## Allow Saving of Tribal Affiliation Start Date in VES when Veteran is Deceased

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Demographics → Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Overview</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/037.png)</p>
<p><span id="_Toc216947432" class="anchor"></span>Figure 15: American Indian/Alaska Native Overview Updates</p>
<p>![](user-guide-ves-6-15/038.png)</p>
<p><span id="_Toc216947433" class="anchor"></span>Figure 16: American Indian/Alaska Native Overview Updates 2</p>
<p>![](user-guide-ves-6-15/039.png)</p>
<p><span id="_Toc216947434" class="anchor"></span>Figure 17: Updated Screenshot - Demographics Overview</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Overview</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/040.png)</p>
<p><span id="_Toc216947435" class="anchor"></span>Figure 18: American Indian/Alaska Native - Main Overview Updates</p>
<p>![](user-guide-ves-6-15/041.png)</p>
<p><span id="_Toc216947436" class="anchor"></span>Figure 19: American Indian/Alaska Native - Main Overview Updates 2</p>
<p>![](user-guide-ves-6-15/042.png)</p>
<p><span id="_Toc216947437" class="anchor"></span>Figure 20: Updated Screenshot - Main Overview</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Demographics → Personal → Personal History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Personal History</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/043.png)</p>
<p><span id="_Toc216947438" class="anchor"></span>Figure 21: Updated Screenshot - Personal History</p>
<p>![](user-guide-ves-6-15/044.png)</p>
<p><span id="_Toc216947439" class="anchor"></span>Figure 22: American Indian/Alaska Native Personal History</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Demographics → Personal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/045.png)</p>
<p><span id="_Toc216947440" class="anchor"></span>Figure 23: Updated Screenshot - Personal Section</p>
<p>![](user-guide-ves-6-15/046.png)</p>
<p><span id="_Toc216947441" class="anchor"></span>Figure 24: Updated American Indian/Alaska Native Personal Tab Text Update</p>
<p>![](user-guide-ves-6-15/047.png)</p>
<p><span id="_Toc216947442" class="anchor"></span>Figure 25: Updated American Indian/Alaska Native Personal Tab Text Update 2</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Demographics → Personal → Personal (Add a Person)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Overview</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/048.png)</p>
<p><span id="_Toc216947443" class="anchor"></span>Figure 26: Personal Add a Person Updated Screenshot</p>
<p>![](user-guide-ves-6-15/049.png)</p>
<p><span id="_Toc216947444" class="anchor"></span>Figure 27: American Indian/Alaska Native Updates - Personal (Add a Person)</p>
<p>![](user-guide-ves-6-15/050.png)</p>
<p><span id="_Toc216947445" class="anchor"></span>Figure 28: American Indian/Alaska Native Updates - Personal (Add a Person) 2</p>
<p>![](user-guide-ves-6-15/051.png)</p>
<p><span id="_Toc216947446" class="anchor"></span>Figure 29: American Indian/Alaska Native Updates - Personal (Add a Person) 3</p>
<p>![](user-guide-ves-6-15/052.png)</p>
<p><span id="_Toc216947447" class="anchor"></span>Figure 30: American Indian/Alaska Native Updates - Personal (Add a Person) 4</p></td>
</tr>
</tbody>
</table>

## Effective Date for VHAP Carveouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Bar → Reference → VHA Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Menu Bar</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Reference</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>VHA Profile</strong> section</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/053.png)</p>
<p><span id="_Toc216947448" class="anchor"></span>Figure 31: VHAP Carveout - Updated Text</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Eligibility → VHA Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Click the <strong>VHA Profiles</strong> section</td>
</tr>
<tr class="even">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-15/054.png)</p>
<p><span id="_Toc216947449" class="anchor"></span>Figure 32: VHA Profiles Assigned – Unselect to Unassign - Updated Text</p>
<p>![](user-guide-ves-6-15/055.png)</p>
<p><span id="_Toc216947450" class="anchor"></span>Figure 33: VHAP Effective Date</p>
<p>![](user-guide-ves-6-15/056.png)</p>
<p><span id="_Toc216947451" class="anchor"></span>Figure 34: Add VHAP Effective Date to E&amp;E Service</p></td>
</tr>
</tbody>
</table>

### From: User Guide VES 6.2

## "Enrollment System Community Care (ESCC)" to "VHA Enrollment System (VES) Integrated Veteran Care (IVC) Systems Impact (VES/IVC SI)" change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

| Step | Action                                                                           |
|----------|--------------------------------------------------------------------------------------|
| 1        | Click the Person Search Tabs section on the table of contents on the Online Help |
| 2        | Click the Eligibility section.                                                   |
| 3        | Click the Community Care section.                                                |
| 4        | Click the VES/IVC SI Quality Report topic.                                       |
| 6        | Confirm "ESCC" has been removed from this report.                                    |

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## "Expanded MH Care Non-Enrollee" field definition for Ineligible Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit Current Eligibility</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>MH CARE NON-ENROLEE</strong> field.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm text is correct and accurate.</p>
<p>![](user-guide-ves-6-2/028.png)</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Navigate back to the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>10</td>
<td>Click the <strong>Edit Current Eligibility (Add a Person)</strong> topic still under the <strong>Person Search Tabs</strong> section and under <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>Scroll down to the <strong>MH CARE NON-ENROLEE</strong> field.</td>
</tr>
<tr class="even">
<td>12</td>
<td><p>Confirm the added text is correct and accurate.</p>
<p>![](user-guide-ves-6-2/029.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Ineligible Reasons and Rules Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>VBA Query Status</strong> field.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following text is correct and accurate:</p>
<p>![](user-guide-ves-6-2/030.png)</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>Navigate back to the Table of Contents.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Click the <strong>Edit Current Eligibility</strong> topic (still under Current Eligibility)</td>
</tr>
<tr class="even">
<td>8</td>
<td>Scroll down to the <strong>Self-Reported Registration Only Reason (Required)</strong> field.</td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>Scroll down to <strong>CLINICAL EVALUATION</strong> in the bulleted list.</p>
<p>![](user-guide-ves-6-2/031.png)</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>Scroll down to the <strong>Remove All Rated SC Disabilities</strong> button definition.</td>
</tr>
<tr class="odd">
<td>11</td>
<td><p>Confirm the added text is accurate and correct.</p>
<p>![](user-guide-ves-6-2/032.png)</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>Scroll down to the <strong>Reason Eligibility Status is Pending Verification</strong> field</td>
</tr>
<tr class="odd">
<td>13</td>
<td><p>Confirm the added NOTE is correct and accurate.</p>
<p>![](user-guide-ves-6-2/033.png)</p></td>
</tr>
<tr class="even">
<td>14</td>
<td>Scroll down to the "Manual entry scenarios for service connected (SC) % and Ineligible information" text.</td>
</tr>
<tr class="odd">
<td>15</td>
<td><p>Confirm the text is correct and accurate.</p>
<p>![](user-guide-ves-6-2/034.png)</p>
<p>![](user-guide-ves-6-2/035.png)</p>
<p>![](user-guide-ves-6-2/036.png)</p>
<p>![](user-guide-ves-6-2/037.png)</p>
<p>![](user-guide-ves-6-2/038.png)</p>
<p>![](user-guide-ves-6-2/039.png)</p></td>
</tr>
<tr class="even">
<td>16</td>
<td>Scroll down to the <strong>Ineligible Reason</strong> field.</td>
</tr>
<tr class="odd">
<td>17</td>
<td><p>Confirm the added "Other" ineligible reason is accurate and correct.</p>
<p>![](user-guide-ves-6-2/040.png)</p></td>
</tr>
<tr class="even">
<td>18</td>
<td><p>Please confirm the first three bullets for the Ineligible Reason "<strong>Rules…"</strong> are correct and accurate:</p>
<p>![](user-guide-ves-6-2/041.png)</p></td>
</tr>
<tr class="odd">
<td>19</td>
<td>Navigate back to the table of contents.</td>
</tr>
<tr class="even">
<td>20</td>
<td>Click the <strong>Primary and Secondary Eligibility Codes</strong> topic.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>Scroll down to <strong>Special Tx Authority Care</strong> (under Secondary Eligibility Codes)</td>
</tr>
<tr class="even">
<td>22</td>
<td><p>Confirm the text is accurate and correct (#8 in the list).</p>
<p>![](user-guide-ves-6-2/042.png)</p></td>
</tr>
<tr class="odd">
<td>23</td>
<td>Navigate back to the table of contents.</td>
</tr>
<tr class="even">
<td>24</td>
<td>Click the <strong>Overview</strong> section (still under Current Eligibility).</td>
</tr>
<tr class="odd">
<td>25</td>
<td>Scroll down to "COMPACT ACT Eligibility" under the <strong>Update Current Eligibility:</strong> field.</td>
</tr>
<tr class="even">
<td>26</td>
<td><p>Confirm the added text is accurate and correct. Second, third and fourth bullet, plus the note under the fourth bullet.</p>
<p>![](user-guide-ves-6-2/043.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Core VHAP Updates: (Profile Codes: 222, 223, 225, 226, and 290)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Reference</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VA Profile</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Core VHAPS</strong> topic (still under the <strong>VHA Profiles</strong> section)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Veteran Restricted Med Benefits</strong> (222) core VHAP.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the text is correct and accurate.</p>
<p>![](user-guide-ves-6-2/044.png)</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Scroll down to the <strong>Non-Veteran Other Restricted Med Benefits</strong> (223) core VHAP.</td>
</tr>
<tr class="even">
<td>8</td>
<td><p>Confirm the text is correct and accurate.</p>
<p>![](user-guide-ves-6-2/045.png)</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td>Scroll down to the <strong>Humanitarian</strong> (225) core VHAP.</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>Confirm the text is correct and accurate.</p>
<p>![](user-guide-ves-6-2/046.png)</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>Scroll down to the <strong>Applicant in Process</strong> (226) core VHAP.</td>
</tr>
<tr class="even">
<td>12</td>
<td><p>Confirm the text is correct and accurate.</p>
<p>![](user-guide-ves-6-2/047.png)</p></td>
</tr>
<tr class="odd">
<td>13</td>
<td>Scroll down to the <strong>Ineligible</strong> (290) core VHAP.</td>
</tr>
<tr class="even">
<td>14</td>
<td><p>Confirm the text is correct and accurate.</p>
<p>![](user-guide-ves-6-2/048.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Clinical Evaluation Secondary Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Primary and Secondary Eligibility</strong> topic still under the <strong>Eligibility</strong> Section (under Person Search Tabs).</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the "Clinical Evaluation" secondary eligibility code (#9) under the <strong>Secondary Eligibility Code</strong> section</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following text for "Clinical Evaluation" is correct and accurate, (#9):</p>
<p>![](user-guide-ves-6-2/049.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## "Application Date" label changed to "Application Received Date"

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Overview</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the "Application Received Date" definition.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the "Application Received Date" definition is correct and accurate.</p>
<p>![](user-guide-ves-6-2/050.png)</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Overview</strong> screen shot.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the <strong>Overview</strong> screen shot has been updated to include "Application Received Date".</p>
<p>![](user-guide-ves-6-2/051.png)</p>
<p><span id="_Toc112061267" class="anchor"></span>Figure 8: Overview</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Navigate back to the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>8</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Scroll down to the <strong>Eligibility</strong> screen shot.</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>Confirm the <strong>Eligibility</strong> screen shot has been updated to include "Application Received Date".</p>
<p>![](user-guide-ves-6-2/052.png)</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>Navigate back to the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>11</td>
<td>Click the <strong>Current Eligibility</strong> topic section.</td>
</tr>
<tr class="odd">
<td>12</td>
<td>Scroll down to the "Application Received Date" definition.</td>
</tr>
<tr class="even">
<td>13</td>
<td><p>Confirm the "Application Received Date" definition is correct and accurate.</p>
<p>![](user-guide-ves-6-2/053.png)</p></td>
</tr>
<tr class="odd">
<td>14</td>
<td>Navigate back to the table of contents.</td>
</tr>
<tr class="even">
<td>15</td>
<td>Click the <strong>Eligibility History</strong> topic, still under the <strong>Current Eligibility</strong> topic.</td>
</tr>
<tr class="odd">
<td>16</td>
<td>Scroll down to the "Application Received Date" definition.</td>
</tr>
<tr class="even">
<td>17</td>
<td><p>Confirm the "Application Received Date" definition is correct and accurate.</p>
<p>![](user-guide-ves-6-2/054.png)</p></td>
</tr>
<tr class="odd">
<td>18</td>
<td>Scroll down to the <strong>Eligibility History</strong> screen shot.</td>
</tr>
<tr class="even">
<td>19</td>
<td><p>Confirm the <strong>Eligibility History</strong> screen shot has been updated to include "Application Received Date".</p>
<p>![](user-guide-ves-6-2/055.png)</p>
<p><span id="_Toc112061268" class="anchor"></span>Figure 9: Eligibility History</p></td>
</tr>
<tr class="odd">
<td>20</td>
<td>Navigate back to the table of contents.</td>
</tr>
<tr class="even">
<td>21</td>
<td>Click the <strong>Enrollment</strong> section.</td>
</tr>
<tr class="odd">
<td>22</td>
<td>Click the <strong>Cancelled/Declined/Override Enrollment (Includes Add a Person)</strong> topic.</td>
</tr>
<tr class="even">
<td>23</td>
<td><p>Confirm the <strong>Application Received Date</strong> field has been updated.</p>
<p>![](user-guide-ves-6-2/056.png)</p></td>
</tr>
<tr class="odd">
<td>24</td>
<td><p>Confirm the <strong>Enrollment</strong> screen shot has been updated to include "Application Received Date".</p>
<p>![](user-guide-ves-6-2/057.png)</p>
<p><span id="_Toc112061269" class="anchor"></span>Figure 10: Enrollment</p></td>
</tr>
<tr class="even">
<td>25</td>
<td>Navigate back to the table of contents.</td>
</tr>
<tr class="odd">
<td>26</td>
<td>Click the <strong>Enrollment History</strong> topic, still under the <strong>Current Eligibility</strong> topic.</td>
</tr>
<tr class="even">
<td>27</td>
<td><p>Confirm the <strong>Enrollment History</strong> screen shot has been updated to include "Application Received Date".</p>
<p>![](user-guide-ves-6-2/058.png)</p>
<p><span id="_Toc112061270" class="anchor"></span>Figure 11: Enrollment History</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### From: User Guide VES 6.8

## VES Communication History For Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Communications → Previously Mailed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Communications</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Previously Mailed</strong> section</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-8/028.png)</p>
<p><span id="_Toc151389053" class="anchor"></span>Figure : Enable Communication History</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Communication → Previously Mailed → Letter Mailed on Behalf of Veteran → Status History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following updates to the VES Enrollment System.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Communication</strong> tab in the VHA Enrollment System (VES).</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Previously Mailed</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Navigate to the <strong>Letter Mailed on Behalf of Veteran</strong> section and click the hyperlink under <strong>Name</strong>.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Navigate to the <strong>Status History</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the panel includes the name of the requesting person or process under the new "Mailed By" column.</p>
<p>![](user-guide-ves-6-8/029.png)</p>
<p><span id="_Toc151389054" class="anchor"></span>Figure : Previously Mailed/Mailed By</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### VES VHAP Updates for SERVICE Act, TERA Indicator & COMPACT Act

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Bar → Reference→ Core VHAPs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Reference</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Core VHAPs</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following sections have been added and that the information is accurate:</p>
<p><strong>Veteran Full Med Benefits Tx and Rx Copay Req 8 (219) Description:</strong></p>
<p>![](user-guide-ves-6-8/030.png)</p>
<p><span id="_Toc151389055" class="anchor"></span>Figure : Veteran Full Med Benefits Tx and Rx Copay Req 8 (219) Description</p>
<p><strong>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 7 (216) Description:</strong></p>
<p>![](user-guide-ves-6-8/031.png)</p>
<p><span id="_Toc151389056" class="anchor"></span>Figure : Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 7 (216) Description</p>
<p><strong>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 8 (217) Description:</strong></p>
<p>![](user-guide-ves-6-8/032.png)</p>
<p><span id="_Toc151389057" class="anchor"></span>Figure : Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 8 (217) Description</p>
<p><strong>Veteran Full Med Benefits Tx and Rx Copay Exmt (213) Description:</strong></p>
<p>![](user-guide-ves-6-8/033.png)</p>
<p><span id="_Toc151389058" class="anchor"></span>Figure : Veteran Full Med Benefits Tx and Rx Copay Exmt (213) Description</p>
<p>![](user-guide-ves-6-8/034.png)</p>
<p><span id="_Toc151389059" class="anchor"></span>Figure : Veteran Full Med Benefits Tx and Rx Copay Exmt (213) Description (con.)</p>
<p><strong>Veteran Full Med Benefits Tx and Rx Copay Exmt 6 (241) Description:</strong></p>
<p>![](user-guide-ves-6-8/035.png)</p>
<p><span id="_Toc151389060" class="anchor"></span>Figure : Veteran Full Med Benefits Tx and Rx Copay Exmt 6 (241) Description</p>
<p><strong>Veteran Full Med Benefits Tx and Rx Copay Req 6 (218) Description:</strong></p>
<p>![](user-guide-ves-6-8/036.png)</p>
<p><span id="_Toc151389061" class="anchor"></span>Figure : Veteran Full Med Benefits Tx and Rx Copay Req 6 (218) Description</p>
<p><strong>Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req (214) Description:</strong></p>
<p>![](user-guide-ves-6-8/037.png)</p>
<p><span id="_Toc151389062" class="anchor"></span>Figure : Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req (214) Description</p>
<p>![](user-guide-ves-6-8/038.png)</p>
<p><span id="_Toc151389063" class="anchor"></span>Figure : Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req (214) Description (con.)</p>
<p><strong>Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req 6 (242) Description:</strong></p>
<p>![](user-guide-ves-6-8/039.png)</p>
<p><span id="_Toc151389064" class="anchor"></span>Figure : Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req 6 (242) Description</p>
<p><strong>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 6 (215) Description:</strong></p>
<p>![](user-guide-ves-6-8/040.png)</p>
<p><span id="_Toc151389065" class="anchor"></span>Figure : Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 6 (215) Description</p>
<p><strong>Veteran Full Med Benefits Tx GMT and Rx Copay Req 6 (240) Description:</strong></p>
<p>![](user-guide-ves-6-8/041.png)</p>
<p><span id="_Toc151389066" class="anchor"></span>Figure : Veteran Full Med Benefits Tx GMT and Rx Copay Req 6 (240) Description</p>
<p><strong>Veteran Full Med Benefits Tx GMT Copay Req and Copay Exmt 6 (239) Description:</strong></p>
<p>![](user-guide-ves-6-8/042.png)</p>
<p><span id="_Toc151389067" class="anchor"></span>Figure : Veteran Full Med Benefits Tx GMT Copay Req and Copay Exmt 6 (239) Description</p>
<p><strong>Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Exmt (220) Description:</strong></p>
<p>![](user-guide-ves-6-8/043.png)</p>
<p><span id="_Toc151389068" class="anchor"></span>Figure : Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Exmt (220) Description</p>
<p><strong>Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Req (221) Description:</strong></p>
<p>![](user-guide-ves-6-8/044.png)</p>
<p><span id="_Toc151389069" class="anchor"></span>Figure : Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Req (221) Description</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Primary and Secondary Eligibility Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Primary and Secondary Eligibility Codes</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Scroll down and confirm that the following excerpt has been added:</p>
<p>![](user-guide-ves-6-8/045.png)</p>
<p><span id="_Toc151389070" class="anchor"></span>Figure : SERVICE ACT &amp; Recalculate Eligibility for Existing Veteran Records</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## VES Update SIGI Values & 10-10EZ/EZR Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility → Financials → Dependents → Add Edit Spouse→ Add Dependent Spouse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Financials</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Dependents</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the <strong>Add Edit Spouse</strong> section.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Click the <strong>Add Dependent Spouse</strong> section.</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the <strong>Self-Identified Gender Identity</strong> dropdown is present:</p>
<p>![](user-guide-ves-6-8/046.png)</p>
<p><span id="_Toc151389071" class="anchor"></span>Figure : SIGI Dropdown Help Text</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Financials → Dependents → Add Edit Spouse→ Edit Dependent Spouse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Financials</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Dependents</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the <strong>Add Edit Spouse</strong> section.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Click the <strong>Edit Dependent Spouse</strong> section.</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the <strong>Self-Identified Gender Identity</strong> dropdown is present:</p>
<p>![](user-guide-ves-6-8/047.png)</p>
<p><span id="_Toc151389072" class="anchor"></span>Figure : SIGI Dropdown Help Text</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Financials → Dependents → ADD SPOUSE→ Self-Identified Gender Identity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following updates to the VES Enrollment System.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Financial</strong> tab in the VHA Enrollment System (VES).</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Dependents</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>ADD SPOUSE</strong> button.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the <strong>Self-Identified Gender Identity</strong> dropdown is present:</p>
<p>![](user-guide-ves-6-8/048.png)</p>
<p><span id="_Toc151389073" class="anchor"></span>Figure : Self-Identified Gender Identity</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### From: User Guide VES 6.2.2

## "COMPACT Act" (Override) Radio Button on Edit Current Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit Current Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Non-Veteran Eligibility Codes</strong> section.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Scroll down to the <strong>COMPACT Act (Override)</strong> radio button definition.</p>
<p><strong>Note:</strong> Veterans Comprehensive Prevention, Access to Care, and Treatment (COMPACT) Act of 2020.</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the added <strong>COMPACT Act (Override)</strong> radio button definition is correct and accurate (located at the very bottom of topic).</p>
<p>![](user-guide-ves-6-2-2/028.png)</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>Scroll down to the updated <strong>Edit Current Eligibility</strong> screen shot (bottom of topic).</td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>Confirm the <strong>COMPACT Act (Override)</strong> radio button screen shot is correct and accurate.</p>
<p>![](user-guide-ves-6-2-2/029.png)</p>
<p><span id="_Toc115956222" class="anchor"></span>Figure : COMPACT Act (Override) Radio Button</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## COMPACT Act Eligibility Rules Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Scroll down to the <strong>COMPACT Act Eligibility Rules</strong> section (still on the <strong>Edit Current Eligibility</strong> topic, and located below the <strong>COMPACT Act</strong> field definition).</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>Confirm the added <strong>COMPACT Act Eligibility Rule Scenarios</strong> are correct and accurate.</p>
<p>![](user-guide-ves-6-2-2/030.png)</p>
<p>![](user-guide-ves-6-2-2/031.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## "Clinical Evaluation" Secondary Eligibility Rule Scenarios

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Scroll down to the "<strong>Clinical Evaluation</strong>" <strong>Secondary Eligibility Rule Scenarios</strong> section (still on the <strong>Edit Current Eligibility</strong> topic, and located below the <strong>COMPACT Act Eligibility Rules</strong>).</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>Confirm the added "<strong>Clinical Evaluation</strong>" <strong>Secondary Eligibility Rule Scenarios</strong> are correct and accurate.</p>
<p>![](user-guide-ves-6-2-2/032.png)![](user-guide-ves-6-2-2/033.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## COMPACT Act" (Override) Radio Button Disabled on Edit Current Eligibility (Add a Person (AAP))

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit Current Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the <strong>Edit Current Eligibility (Add a Person)</strong> topic.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Scroll down to the <strong>Non-Veteran Eligibility Codes</strong> section.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Scroll down to the <strong>COMPACT Act (Override)</strong> radio button definition.</td>
</tr>
<tr class="even">
<td>8</td>
<td><p>Confirm the added <strong>COMPACT Act (Override)</strong> radio button definition is correct and accurate (located at the very bottom of topic).</p>
<p>![](user-guide-ves-6-2-2/034.png)</p>
<p>![](user-guide-ves-6-2-2/035.png)</p>
<p><span id="_Toc115956223" class="anchor"></span>Figure : COMPACT Act (Override) Disabled Radio Button</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## "COMPACT Act" Carveout VHAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>References</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Click the <strong>Carveout VHAPs</strong> topic.</p>
<p><strong>Note:</strong> Veteran's Health Administration Profile (VHAP).</p></td>
</tr>
<tr class="odd">
<td>6</td>
<td>Scroll down to the <strong>COMPACT Act</strong> carveout VHAP (profile code 309) definition (last VHAP on the table).</td>
</tr>
<tr class="even">
<td>7</td>
<td><p>Confirm the added <strong>COMPACT Act</strong> carveout VHAP definition is correct and accurate.</p>
<p>![](user-guide-ves-6-2-2/036.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## VHAP Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td><p>Scroll to the <strong>HUD-VASH Restricted Care</strong> VHAP (profile 307) (still on the <strong>Carveout VHAP</strong> topic from the previous section, and above the <strong>COMPACT Act Eligible</strong> carveout VHAP).</p>
<p><strong>Note:</strong> U.S. Department of Housing and Urban Development-VA Supportive Housing (HUD-VASH).</p></td>
</tr>
<tr class="even">
<td>2</td>
<td><p>Confirm the <strong>HUD-VASH Restricted Care</strong> VHAP definition is correct and accurate.</p>
<p>![](user-guide-ves-6-2-2/037.png)</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>Navigate back to the <strong>Menu Bar</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Core VHAPs</strong> topic under the <strong>Reference</strong> section, and the <strong>VHA Profiles</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Veteran Restricted Med Benefits</strong> VHAP (profile code 222).</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the <strong>Veteran Restricted Med Benefits</strong> VHAP definition is correct and accurate.</p>
<p>![](user-guide-ves-6-2-2/038.png)</p></td>
</tr>
<tr class="odd">
<td>6</td>
<td>Scroll down to the <strong>Non-Veteran Other Restricted Med Benefits</strong> VHAP (profile 223).</td>
</tr>
<tr class="even">
<td>7</td>
<td><p>Confirm the <strong>Non-Veteran Other Restricted Med Benefits</strong> VHAP definition is correct and accurate.</p>
<p>![](user-guide-ves-6-2-2/039.png)</p></td>
</tr>
<tr class="odd">
<td></td>
<td>Scroll down to the <strong>Ineligible</strong> VHAP (profile 290).</td>
</tr>
<tr class="even">
<td></td>
<td><p>Confirm the <strong>Ineligible</strong> VHAP definition is correct and accurate.</p>
<p>![](user-guide-ves-6-2-2/040.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### From: User Guide VES 6.7

## Section 101 to include all WWII Veterans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Navigate to the <strong>COMPACT Act Eligible Indicator</strong> section and verify that the included information is correct.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>![](user-guide-ves-6-7/028.png)</p>
<p><span id="_Toc145071646" class="anchor"></span>Figure : COMPACT Act Eligible Indicator Overview</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Primary and Secondary Eligibility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>.2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Primary and Secondary Eligibility Codes</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Navigate to the <strong>Veteran Primary Eligibility Codes</strong> section and verify that the included information is correct.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Navigate down to the <strong>Notes</strong> section and verify that the following information is accurate.</p>
<p>VES assigns <strong>Veteran Secondary Eligibility Codes</strong>:</p>
<p>Navigate down to the Non-Veteran Secondary Eligibility Codes section and verify that the information is correct.</p></td>
</tr>
<tr class="even">
<td>6</td>
<td><p>![](user-guide-ves-6-7/029.png)</p>
<p><span id="_Toc145071647" class="anchor"></span>Figure : Veteran Secondary Eligibility Codes</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>![](user-guide-ves-6-7/030.png)</p>
<p><span id="_Toc145071648" class="anchor"></span>Figure : Secondary Eligibility Scenarios</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>![](user-guide-ves-6-7/031.png)</p>
<p><span id="_Toc145071649" class="anchor"></span>Figure : Secondary Eligibility Scenarios (cont.)</p></td>
</tr>
<tr class="odd">
<td>8.</td>
<td><p>![](user-guide-ves-6-7/032.png)</p>
<p><span id="_Toc145071650" class="anchor"></span>Figure : Add Date Range to World War II Entry</p></td>
</tr>
<tr class="even">
<td>9.</td>
<td><p>Navigate to the Compact Act Eligible Table and verify that the information is accurate.</p>
<p>![](user-guide-ves-6-7/033.png)</p>
<p><span id="_Toc145071651" class="anchor"></span>Figure : COMPACT Act Eligible Table</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Edit Current Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Edit Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Navigate to the <strong>COMPACT Act (Override)</strong> section and verify that the included information is correct.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>![](user-guide-ves-6-7/034.png)</p>
<p><span id="_Toc145071652" class="anchor"></span>Figure : COMPACT Act (Override) Rules</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Menu Bar → Reference → VHA Profiles → CORE VHAPs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Reference</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Navigate to the <strong>CORE VHAPs</strong> section and verify that the included information is correct.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>![](user-guide-ves-6-7/035.png)</p>
<p><span id="_Toc145071653" class="anchor"></span>Figure : Core VHAP Veteran Full Med Benefits</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Add an Uncharacterized Discharge Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Military Service → Military Service Episodes – HEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Military Service Episodes - HEC</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>Discharge Type</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Verify that the following information is accurate:</p>
<p>![](user-guide-ves-6-7/036.png)</p>
<p><span id="_Toc145071654" class="anchor"></span>Figure : Uncharacterized Discharge Type</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Z07 Consistency Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Demographics → Personal → Personal (Add a Person)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Personal (Add a Person)</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Verify that the following information is accurate:</p>
<p>![](user-guide-ves-6-7/037.png)![](user-guide-ves-6-7/038.png)</p>
<p><span id="_Toc145071655" class="anchor"></span>Figure : Update to Claim Folder Number and Claim Folder Location</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Demographics → Personal 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Verify that the following screenshot has been accurately updated to remove the "Same as SSN" button:</p>
<p>![](user-guide-ves-6-7/039.png)</p>
<p><span id="_Toc145071656" class="anchor"></span>Figure : Demographics - Removed SSN Button</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### From: User Guide VES 6.4

## Preferred Language Updates Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Demographics → Personal 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the updated <strong>Personal</strong> screen shot with the removed <strong>Language Entry Date</strong> and check box are correct and accurate.</p>
<p>![](user-guide-ves-6-4/028.png)</p>
<p><span id="_Toc125531082" class="anchor"></span>Figure 8: Personal History Screen</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the <strong>Language Entry Date</strong> information has been removed:</p>
<p>Removed "Language Entry Date" information:</p>
<p><strong>Language Entry Date: </strong></p>
<p>This is the date the Veteran's Preferred Language data was entered. The date can be entered manually or automatically.</p>
<p><strong>More...</strong></p>
<p>The initial value for the Language Entry Date field is blank.</p>
<p><strong>Language Entry Date scenarios: </strong></p>
<p>If no date is entered, then the value defaults to the current date upon a successful update.</p>
<p>If the user selects a value from the Preferred Language drop-down list, then the Language Entry Date field is blank, but can be edited. For example, if a Veteran enters his/her preferred language on a 10-10EZ form, the VES user should enter the date of the 10-10EZ form into the Language Entry Date field.</p>
<p><strong>Rules...</strong></p>
<p>The Language Entry Date cannot be a future date.</p>
<p>The Language Entry Date can be a date in the past. However, the date cannot be before the Veteran's date of birth.</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Demographics → Personal (Add a Person)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal (Add a Person)</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the updated <strong>Personal (Add a Person)</strong> screen shot with the removed <strong>Language Entry Date</strong> and check box are correct and accurate.</p>
<p>![](user-guide-ves-6-4/029.png)</p>
<p><span id="_Toc125531083" class="anchor"></span>Figure 9: Personal History Screen</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the <strong>Language Entry Date</strong> information has been removed:</p>
<p>Removed "Language Entry Date" information:</p>
<p><strong>Language Entry Date: </strong></p>
<p>This is the date the Veteran's Preferred Language data was entered. The date can be entered manually or automatically.</p>
<p><strong>More...</strong></p>
<p>The initial value for the Language Entry Date field is blank.</p>
<p><strong>Language Entry Date scenarios: </strong></p>
<p>If no date is entered, then the value defaults to the current date upon a successful update.</p>
<p>If the user selects a value from the Preferred Language drop-down list, then the Language Entry Date field is blank, but can be edited. For example, if a Veteran enters his/her preferred language on a 10-10EZ form, the VES user should enter the date of the 10-10EZ form into the Language Entry Date field.</p>
<p><strong>Rules...</strong></p>
<p>The Language Entry Date cannot be a future date.</p>
<p>The Language Entry Date can be a date in the past. However, the date cannot be before the Veteran's date of birth.</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Disable Date of Death

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Demographics → Personal 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>Date of Death</strong> definition and information.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the added <strong>Date of Death</strong> information and screen shots are correct and accurate.</p>
<p>![](user-guide-ves-6-4/030.png)</p>
<p><span id="_Toc125531084" class="anchor"></span>Figure : Modify Date of Death Help Text</p>
<p>![](user-guide-ves-6-4/031.png)</p>
<p><span id="_Toc125531085" class="anchor"></span>Figure : Date of Death Rules Text</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Demographics → Personal (Add a Person)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Personal (Add a Person)</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>Date of Death</strong> definition and information.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the added <strong>Date of Death</strong> information and screen shots are correct and accurate.</p>
<p>![](user-guide-ves-6-4/032.png)</p>
<p><span id="_Toc125531086" class="anchor"></span>Figure : Modify Date of Death Help Text</p>
<p>![](user-guide-ves-6-4/033.png)</p>
<p><span id="_Toc125531087" class="anchor"></span>Figure : Date of Death Rules Text</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### From: User Guide VES 6.14

## Update Document Management Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Document Management→ Search Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Document Management</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Search Documents</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-14/029.png)</p>
<p><span id="_Toc205888260" class="anchor"></span>Figure 8: Proof of Discharge Menu</p>
<p>![](user-guide-ves-6-14/030.png)</p>
<p><span id="_Toc205888261" class="anchor"></span>Figure 9: Administration Menu</p>
<p>![](user-guide-ves-6-14/031.png)</p>
<p><span id="_Toc205888262" class="anchor"></span>Figure 10: Tera Eligibility Menu</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Document Management → Upload Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Document Management</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Upload Documents</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-14/032.png)</p>
<p><span id="_Toc205888263" class="anchor"></span>Figure 11: Proof of Discharge Menu</p>
<p>![](user-guide-ves-6-14/033.png)</p>
<p><span id="_Toc205888264" class="anchor"></span>Figure 12: Administration Menu</p>
<p>![](user-guide-ves-6-14/034.png)</p>
<p><span id="_Toc205888265" class="anchor"></span>Figure 13: Tera Eligibility Menu</p></td>
</tr>
</tbody>
</table>

## Add and Change Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Communications → Available for Mailing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th> <strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Communications</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Available for Mailing</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-14/035.png)</p>
<p><span id="_Toc205888266" class="anchor"></span>Figure 14: VHA-EED Decision Notice Dishonorable</p>
<p>![](user-guide-ves-6-14/036.png)</p>
<p><span id="_Toc205888267" class="anchor"></span>Figure 15: VHA-EED Updated Form Numbers</p>
<p>![](user-guide-ves-6-14/037.png)</p>
<p><span id="_Toc205888268" class="anchor"></span>Figure 16: Eligible Letter Section</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Eligibility → Current Eligibility → Edit Current Eligibility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit</strong> <strong>Current Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-14/038.png)</p>
<p><span id="_Toc205888269" class="anchor"></span>Figure 17: Unlock Veteran Option</p>
<p>![](user-guide-ves-6-14/039.png)</p>
<p><span id="_Toc205888270" class="anchor"></span>Figure 18: Reason for Unlock Request Dropdown Menu</p></td>
</tr>
</tbody>
</table>

## Automate TERA Eligibility (Phase 2 of 3) - Cohort \#3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Military Service → Current Military Service 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Military Service</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-14/040.png)</p>
<p><span id="_Toc205888271" class="anchor"></span>Figure 19: Cohort #3</p>
<p>![](user-guide-ves-6-14/041.png)</p>
<p><span id="_Toc205888272" class="anchor"></span>Figure 20: TERA Indicator</p></td>
</tr>
</tbody>
</table>

## Restrict SW Asia Conditions Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Military Service → Current Military Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Military Service</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-14/042.png)</p>
<p><span id="_Toc205888273" class="anchor"></span>Figure 21: SW Asia Conditions</p></td>
</tr>
</tbody>
</table>

## Medicare Claim Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Demographics → Insurance → Add Medicare → Add/Update Insurance Carrier - Medicare

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Insurance</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Add Medicare</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the <strong>Add/Update Insurance Carrier - Medicare</strong> section.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-14/043.png)</p>
<p><span id="_Toc205888274" class="anchor"></span>Figure 22: Medicare Claim Number (Part A)</p>
<p>![](user-guide-ves-6-14/044.png)</p>
<p><span id="_Toc205888275" class="anchor"></span>Figure 23: Medicare Claim Number (Part B)</p></td>
</tr>
</tbody>
</table>

###

### From: User Guide VES 6.7.1

## VES Change Combat Veteran Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility → Current Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following sections have been removed:</p>
<p>Discharge Due to Disability</p>
<p>Military Disability Retirement</p>
<p>Agent Orange Exposure Location</p>
<p>Radiation Exposure Method</p>
<p>SW Asia Conditions</p>
<p>Camp Lejeune Eligibility</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Current Eligibility → Current Eligibility (Add a Person)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> section</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Current Eligibility (Add a Person)</strong> section</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following sections have been removed:</p>
<p>Discharge Due to Disability</p>
<p>Military Disability Retirement</p>
<p>Agent Orange Exposure Location</p>
<p>Radiation Exposure Method</p>
<p>SW Asia Conditions</p>
<p>Camp Lejeune Eligibility</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Military Service 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the following sections have been added and that the information is accurate:</p>
<p>![](user-guide-ves-6-7-1/028.png)</p>
<p><span id="_Toc148976675" class="anchor"></span>Figure 8: CVE End Date Rules</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### Person Search Tabs → Eligibility → Edit Eligibility → Other Eligibility Factors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search</strong> option in the VHA Enrollment System (VES).</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> tab.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Edit Eligibility</strong> tab.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down and click <strong>Other Eligibility Factors.</strong></td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the removed information is not available and that the updated screen shot is accurate.</p>
<p><strong>Removed:</strong></p>
<p>Discharge Due to Disability</p>
<p>Military Disability Retirement</p>
<p>Agent Orange Exposure Location</p>
<p>Radiation Exposure Method</p>
<p>SW Asia Conditions</p>
<p>Camp Lejeune Eligibility</p>
<p>![](user-guide-ves-6-7-1/029.png)</p>
<p><span id="_Toc148976676" class="anchor"></span>Figure 9: Other Eligibility Drop-Down Menu</p></td>
</tr>
</tbody>
</table>

### TERA Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Military Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the following sections have been added and that the information is accurate:</p>
<p>![](user-guide-ves-6-7-1/030.png)</p>
<p><span id="_Toc148976677" class="anchor"></span>Figure 10: TERA Indicator Updates</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

Confirm the following Online Help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
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
<td>1</td>
<td>Click the <strong>Person Search</strong> option in the VHA Enrollment System (VES).</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Scroll down to the Toxic Exposure Risk Activity section. and confirm the information is accurate:</p>
<p>![](user-guide-ves-6-7-1/031.png)</p>
<p><span id="_Toc148976678" class="anchor"></span>Figure 11: Toxic Exposure Risk Activity Radio Button Options</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

### From: User Guide VES 6.10

## VES Vietnam Service Episode Dates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Military Service → Period of Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>Step</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Period of Service</strong> section</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information was modified:</p>
<p>![](user-guide-ves-6-10/028.png)</p>
<p><span id="_Toc167772718" class="anchor"></span>Figure : Automatic HEC Period of Service List</p>
<p>![](user-guide-ves-6-10/029.png)</p>
<p><span id="_Toc167772719" class="anchor"></span>Figure : HEC Period of Service List</p></td>
</tr>
</tbody>
</table>

## VES Change Rejected Enrollment Status to Deferred

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility→ Enrollment→ Current Enrollment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Enrollment</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Current Enrollment</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-10/030.png)</p>
<p><span id="_Toc167772720" class="anchor"></span>Figure : Enrollment Statuses</p></td>
</tr>
</tbody>
</table>

## ESM Enable Confidential Address 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Demographics → Addresses →Confidential Mailing Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Addresses</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Confidential Mailing Address</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-10/031.png)</p>
<p><span id="_Toc167772721" class="anchor"></span>Figure : Current Confidential Communication Types</p></td>
</tr>
</tbody>
</table>

## TERA Updates for 10-10EZ, UI, VOA and Work Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Financials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Financials</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-10/032.png)</p>
<p><span id="_Toc167772722" class="anchor"></span>Figure : Print 1010EZ &amp; Print 1010EZR</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Enrollment → Veteran's Online Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Enrollment</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Veteran's Online Application</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-10/033.png)</p>
<p><span id="_Toc167772723" class="anchor"></span>Figure : Veteran's Online Application (VOA)</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Military Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-10/034.png)</p>
<p><span id="_Toc167772724" class="anchor"></span>Figure : Agent Orange Exposure Location</p>
<p>![](user-guide-ves-6-10/035.png)</p>
<p><span id="_Toc167772725" class="anchor"></span>Figure : TERA Indicator</p>
<p>![](user-guide-ves-6-10/036.png)</p>
<p><span id="_Toc167772726" class="anchor"></span>Figure : TERA Indicator - Cohort 1-3</p>
<p>Confirm the screenshot has been updated (found at the bottom of the Military Service section):</p>
<p>![](user-guide-ves-6-10/037.png)</p>
<p><span id="_Toc167772727" class="anchor"></span>Figure : Military Service Tab Screenshot</p></td>
</tr>
</tbody>
</table>

### From: User Guide VES 6.12

## VES Electronic Health Record Modernization (EHRM) Confidential and Temporary Phone Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Demographics → Addresses → Add/Edit Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Addresses</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Add/Edit Address</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-12/029.png)</p>
<p><span id="_Toc189660608" class="anchor"></span>Figure 8: Confidential Address &amp; Rule Updates</p>
<p>![](user-guide-ves-6-12/030.png)</p>
<p><span id="_Toc189660609" class="anchor"></span>Figure 9: Phone Type</p></td>
</tr>
</tbody>
</table>

## VES EHRM Automate Employee Only and Employee Veteran VHAPs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Bar → Reference → VHA Profile → Carveout VHAPs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Reference</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profile</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Carveout VHAPs</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-12/031.png)</p>
<p><span id="_Toc189660610" class="anchor"></span>Figure 10: Employee Only</p>
<p>![](user-guide-ves-6-12/032.png)</p>
<p><span id="_Toc189660611" class="anchor"></span>Figure 11: Employee Veteran</p></td>
</tr>
</tbody>
</table>

## VES Non-Medical Care Collection Fund (MCCF) Consolidated Patient Account Centers (CPAC) User Role and Member ID Label Update (Admin) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Demographics → Identity Traits 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Identity Traits</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-12/033.png)</p>
<p><span id="_Toc189660612" class="anchor"></span>Figure 12: Member ID (EPIDI)</p></td>
</tr>
</tbody>
</table>

### Menu Bar → Veteran → Veteran Search (Person Search)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Veteran</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Veteran Search (Person Search)</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-12/034.png)</p>
<p><span id="_Toc189660613" class="anchor"></span>Figure 13: Member ID (EDIPI) - Veteran Search</p>
<p>![](user-guide-ves-6-12/035.png)</p>
<p><span id="_Toc189660614" class="anchor"></span>Figure 14: Member ID (EDIPI) - Veteran Search 2</p></td>
</tr>
</tbody>
</table>

### From: User Guide VES 6.11

## VES Site Correlation (New ADD Treatment Facility button)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Facility

 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

 

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Facility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-11/029.png)</p>
<p><span id="_Toc179458256" class="anchor"></span>Figure 8: Facility Add Button Option</p>
<p>Confirm the following text been removed from the Online Help:</p>
<p>![](user-guide-ves-6-11/030.png)</p>
<p><span id="_Toc179458257" class="anchor"></span>Figure 9: Date &amp; Outpatient Days (Removed Text)</p></td>
</tr>
</tbody>
</table>

## VES Enable Edit for Employer Details, Mother's Maiden Name and Place of Birth

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Financials→ Dependents→ Add/Edit Spouse→ Edit Dependent Spouse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Financials</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Dependents</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Add/Edit Spouse</strong> section.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the <strong>Edit Dependent Spouse</strong> section.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-11/031.png)</p>
<p><span id="_Toc179458258" class="anchor"></span>Figure 10: Maiden Name Editable Fields</p>
<p>![](user-guide-ves-6-11/032.png)</p>
<p><span id="_Toc179458259" class="anchor"></span>Figure 11: Employment Status</p></td>
</tr>
</tbody>
</table>

## International Phone Numbers – Phase 1 Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Demographics → Addresses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Addresses</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-11/033.png)</p>
<p><span id="_Toc179458260" class="anchor"></span>Figure 12: Phone Numbers</p></td>
</tr>
</tbody>
</table>

## Persian Gulf Deployed Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Military Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Military Service</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-11/034.png)</p>
<p><span id="_Toc179458261" class="anchor"></span>Figure 13: Persian Gulf Indicator</p>
<p>![](user-guide-ves-6-11/035.png)</p>
<p><span id="_Toc179458262" class="anchor"></span>Figure 14: Persian Gulf Indicator (VES)</p></td>
</tr>
</tbody>
</table>

### From: User Guide VES 6.9

## VES Ineligible Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Communications → Available for Mailing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Communications</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Available for Mailing</strong> section</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-9/028.png)</p>
<p><span id="_Toc162419713" class="anchor"></span>Figure : 60-Day Pre-Term Letters and 1199 Eligibility Letters</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 94%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Communications</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Navigate to the <strong>Available for Mailing</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm that the following information has been added:</p>
<p>![](user-guide-ves-6-9/029.png)</p>
<p><span id="_Toc162419714" class="anchor"></span>Figure : Ineligible Letters</p>
<p>![](user-guide-ves-6-9/030.png)</p>
<p><span id="_Toc162419715" class="anchor"></span>Figure : Ineligible Letters Description</p></td>
</tr>
</tbody>
</table>

## VES TERA Verification Method 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Military Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Communications</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-9/031.png)</p>
<p><span id="_Toc162419716" class="anchor"></span>Figure : TERA Indicator</p></td>
</tr>
</tbody>
</table>

## VES Veteran's Online Application (VOA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility → Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Registration</strong> section</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-9/032.png)</p>
<p><span id="_Toc162419717" class="anchor"></span>Figure : VOA (Registration Only) Table</p></td>
</tr>
</tbody>
</table>

### From: User Guide VES 6.14.5

## VFMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → VFMP Eligibility Overview

 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

 

| Step | Action                                                                                                                                                           |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Click the Person Search Tabs section on the table of contents on the Online Help.                                                                                |
| 2        | Click the VFMP Eligibility Overview section.                                                                                                                     |
| 3        | Confirm all the added information to the new folders is accurate per the VFMP Requirements. Note: This is a completely new section and completely new tabs for VFMP. |

### Person Search Tabs → Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

 

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Communications</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-14-5/029.png)</p>
<p><span id="_Toc214637076" class="anchor"></span>Figure 8: Communications Overview</p></td>
</tr>
</tbody>
</table>

### Person Search Tabs → Communications → Comments 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

 

| Step | Action                                                                                                                                       |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Click the Person Search Tabs section on the table of contents on the Online Help.                                                            |
| 2        | Click the Communications section.                                                                                                            |
| 3        | Click the Comments section.                                                                                                                  |
| 4        | Confirm all the added information to the new folders is accurate per the VFMP Requirements. *Note: All folders under Comments are new sections.* |

### Person Search Tabs → Communications → Correspondence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

 

| Step | Action                                                                                                                                                                                       |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Click the Person Search Tabs section on the table of contents on the Online Help.                                                                                                            |
| 2        | Click the Communications section.                                                                                                                                                            |
| 3        | Click the Correspondence section.                                                                                                                                                            |
| 4        | Confirm all the added information to the new folders is accurate per the VFMP Requirements. *Note: Correspondence is a new section to house all the previous folders that fall under this list.* |

### Person Search Tabs→ Demographics → Insurance Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

 

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Demographics</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Insurance Overview</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-14-5/030.png)</p>
<p><span id="_Toc214637077" class="anchor"></span>Figure 9: Pharmacy Coverage</p></td>
</tr>
</tbody>
</table>

## Keyboard Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Troubleshooting → 508 Compliance & Accessibility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

 

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Troubleshooting</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>508 Compliance &amp; Accessibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-14-5/031.png)</p>
<p><span id="_Toc214637078" class="anchor"></span>Figure 10: Keyboard-Only User Accessibility Settings</p></td>
</tr>
</tbody>
</table>

###

### From: User Guide VES 6.13

## VBA Auto Registration to VES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Bar → ESR Registration → Status History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Menu Bar</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>ESR Registration</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Status History</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following information has been added:</p>
<p>![](user-guide-ves-6-13/029.png)</p>
<p><span id="_Toc195520463" class="anchor"></span>Figure 8: Auto Registration</p></td>
</tr>
</tbody>
</table>

## VES Allow Edit to CC Determination Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Person Search Tabs → Eligibility → Community Care→ Community Care Determination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following Online Help updates.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Click the <strong>Person Search Tabs</strong> section on the table of contents on the Online Help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Community Care</strong> section.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Community Care Determination</strong> section<strong>.</strong></td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Scroll to <strong>CC Determination Date</strong> and confirm the following information has been added:</p>
<p>![](user-guide-ves-6-13/030.png)</p>
<p><span id="_Toc195520464" class="anchor"></span>Figure 9: CC Determination Date</p></td>
</tr>
</tbody>
</table>
