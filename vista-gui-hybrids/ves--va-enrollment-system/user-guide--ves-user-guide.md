---
title: VES Version 5.18 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: null
app_code: VES
app_name: VA Enrollment System
section: GUI
app_status: archive
pkg_ns: VES
patch_ver: 5.18
patch_id: VES*5.18
group_key: VES:VES:5.18
file_numbers: []
security_keys: []
menu_options: 0
description: '''Installation, Maintenance, & Monitoring heading update, p. 2 COMPACT ACT description, p. 11 COMPACT Act updates on the Overview screen, pgs. 12-13 COMPACT ACT: Dishonorable VA or FFP (302) VHAP, p. 14 COMPACT Act Core VHAP updates, pgs.'''
audience: End users and package coordinators (ADPAC)
keywords: []
page_count: 0
word_count: 8579
section_count: 31
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: October 2021
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System_Archive/es_5_18_ug.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System_Archive/es_5_18_ug.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=293
audit_applied: '2026-05-31'
master_source: VES Version 5.18 User Guide
master_pub_date: October 2021
consolidated_from: 2 versions
prior_versions:
- VES Version 5.17 User Guide
consolidated_title: ves user guide
---

Enrollment System 5.18

User Guide-Quick Start

![](ves-version-5-18-user-guide/001.png)

October 2021

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc83889333" class="anchor"></span>Table 1: Support Contact Information</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 55%" />
<col style="width: 18%" />
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
<td>10/16/2021</td>
<td>36.0</td>
<td><p><strong>ES V5.18</strong> added the following:</p>
<ul>
<li><p>Installation, Maintenance, &amp; Monitoring heading update, p. 2</p></li>
<li><p>COMPACT ACT description, p. 11</p></li>
<li><p>COMPACT Act updates on the Overview screen, pgs. 12-13</p></li>
<li><p>COMPACT ACT: Dishonorable VA or FFP (302) VHAP, p. 14</p></li>
<li><p>COMPACT Act Core VHAP updates, pgs. 16-27</p>
<ul>
<li><p>Veteran Full Med Benefits Tx and Rx Copay Exmt (213)</p></li>
<li><p>Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req (214)</p></li>
<li><p>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 6 (215)</p></li>
<li><p>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 7 (216)</p></li>
<li><p>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 8 (217)</p></li>
<li><p>Veteran Full Med Benefits Tx and Rx Copay Req 6 (218)</p></li>
<li><p>Veteran Full Med Benefits Tx and Rx Copay Req 8 (219)</p></li>
<li><p>Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Exmt (220)</p></li>
<li><p>Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Req (221)</p></li>
<li><p>Veteran Restricted Med Benefits (222)</p></li>
<li><p>Non Veteran Other Restricted Med Benefits (223)</p></li>
<li><p>Restricted Examination Only (224)</p></li>
<li><p>Applicant in Process (226)</p></li>
<li><p>Ineligible (290)</p></li>
<li><p>Removed "a Pending Adjudication" from the following: </p>
<ul>
<li><p>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 6 (215)</p></li>
<li><p>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 8 (217)</p></li>
</ul></li>
</ul></li>
<li><p>COMPACT Act: Community Care Program (CCP) VHAP update, pgs. 28-29</p>
<ul>
<li><p>Veteran Plan CCP Restricted Care (300)</p></li>
</ul></li>
<li><p>COMPACT Act: Ineligible Reason Code, pgs. 30-31</p></li>
<li><p>Secondary Eligibility Determination of "COMPACT Act Eligible" rules, pgs 32-34</p></li>
<li><p>Secondary Eligibility Code Updates, p. 35</p></li>
<li><p>Megabus Act description, p. 36</p></li>
<li><p>Megabus MST: SPECIAL TX AUTHORITY CARE, p. 37</p></li>
<li><p>CCN Regions Map update, pgs. 38-39</p></li>
<li><p>Paginating and Filtering User Profiles, p. 40</p></li>
<li><p>Carveout VHAP description update, p. 41</p></li>
<li><p>CCP VHAP description update, p. 42</p></li>
<li><p>Core VHAP description update, p. 43</p></li>
</ul></td>
<td>TeamLibertyTW</td>
</tr>
</tbody>
</table>

<span id="_Toc83889333" class="anchor"></span>Table 1: Support Contact Information

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the User Guide-Quick Start is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide-Quick Start is a technical communication document intended to give assistance to people using a particular system, such as the Enrollment System (ES). It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most quick start guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide-Quick Start is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

Table of Contents

Table of Figures

List of Tables

[Table 1: Support Contact Information [3](#_Toc83889333)](#_Toc83889333)

[Table 2: Accessibility Software [9](#_Toc83889334)](#_Toc83889334)

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
    - [Documentation Conventions](#documentation-conventions)
    - [Project References](#project-references)
  - [National Service Desk and Other Contacts](#national-service-desk-and-other-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [ESM Application Information System Contingency Plan](#esm-application-information-system-contingency-plan)
  - [ESM Project Artifacts SharePoint Site](#esm-project-artifacts-sharepoint-site)
  - [Browser & Operating System Compatibility](#browser-operating-system-compatibility)
- [Getting Started](#getting-started)
  - [Enrollment System (ES) Layout](#enrollment-system-es-layout)
  - [ES Online Help](#es-online-help)
  - [Compliance & Accessibility](#compliance-accessibility)
    - [Accessibility Software](#accessibility-software)
  - [Standard Data Service (SDS) Lookup Tables](#standard-data-service-sds-lookup-tables)
  - [Exiting ES](#exiting-es)
  - [Caveats and Exceptions](#caveats-and-exceptions)
- [Significant Additions and Updates to ES Version 5.18](#significant-additions-and-updates-to-es-version-518)
  - [COMPACT Act Description](#compact-act-description)
  - [COMPACT Act on the Overview screen](#compact-act-on-the-overview-screen)
  - [COMPACT Act: Dishonorable VA or FFP VHAP (302)](#compact-act-dishonorable-va-or-ffp-vhap-302)
  - [COMPACT Act: Core VHAP Updates](#compact-act-core-vhap-updates)
  - [COMPACT Act: Community Care Program (CCP) Restricted Care (300) VHAP updates](#compact-act-community-care-program-ccp-restricted-care-300-vhap-updates)
  - [COMPACT Act: Ineligible Reason Code](#compact-act-ineligible-reason-code)
  - [COMPACT Act: Secondary Eligibility Determination of "COMPACT Act Eligible" rules](#compact-act-secondary-eligibility-determination-of-compact-act-eligible-rules)
  - [COMPACT Act: Secondary Eligibility Code Updates](#compact-act-secondary-eligibility-code-updates)
  - [Megabus Act Description](#megabus-act-description)
  - [Megabus MST: SPECIAL TX AUTHORITY CARE](#megabus-mst-special-tx-authority-care)
  - [CCN Regions Map Update](#ccn-regions-map-update)
  - [Paginating and Filtering User Profiles](#paginating-and-filtering-user-profiles)
  - [Carveout VHAP Description Update](#carveout-vhap-description-update)
  - [CCP VHAP Description Update](#ccp-vhap-description-update)
  - [Core VHAP Description Update](#core-vhap-description-update)
- [Troubleshooting](#troubleshooting)
The Enrollment System (ES) is the primary Veterans Affairs (VA) system used to manage VA health benefits.
ES allows staff at the Health Eligibility Center (HEC), located in Atlanta, Georgia, to work more efficiently and determine patient eligibility in a timelier manner. Messaging with the VAMC (Department of Veterans Affairs Medical Center) allows for the adding and updating of beneficiary records to the enterprise enrollment system to be shared with the field.
ES is one component of the "system of systems" needed to implement the Health*<u>e</u>*Vet REE (Registration, Eligibility & Enrollment) environment.
ES's two main functions are:
- Expert System (Messaging) provides a seamless bi-directional interface with external Veterans Health Administration (VHA) and non-VHA systems for data exchange of Veterans' information.
- Workflow (Case Management) that provides authorized VHA case representatives at the HEC and VAMC with a web interface to easily track, maintain, and manage cases associated with Veteran benefits. HEC and VAMC staff utilize ES to manage these "cases" to completion so that verified Eligibility & Enrollment can be determined.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this user guide is to familiarize users with important features and navigational elements of the ES application.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

President George W. Bush established a task force for returning Global War on Terror (GWOT) heroes who resulted in enhancements that improved delivery of Federal services and benefits to GWOT service members and Veterans. Among recommendations associated with task force was to focus on enhancing delivery of services and information to GWOT service members and Veterans within existing authority and resource levels.

### Release Updates and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click the [link](https://vaww.esr.aac.va.gov/esr/webhelp/esr_help_project.htm#t=online_help%2Fupdates_releases_enhancements.htm) to view current and past ES release updates and enhancements on the online help.

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This User Guide-Quick Start guide contains the following:

- Introduction
- System Summary
- Getting Started
- Significant Additions and Updates to ES Version
- Troubleshooting

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This quick start was written with the following assumed experience/skills of the audience:

- User has basic knowledge of ES (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, menus, and security keys required for ES.
- User is using ES to do their job.
- User has validated access to ES.
- User has completed any prerequisite training.

### Installation, Maintenance, & Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation, maintenance, and monitoring of ES updates are performed at the Austin Information Technology Center (AITC) on the third Saturday of each month.

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the federal government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by VA of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Quick Start uses several methods to highlight different aspects of the material.

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

### Project References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the following Enrollment System references:

- ES 5.17 Release Notes
- ES 5.17 Online Help

## National Service Desk and Other Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc83889334" class="anchor"></span>Table 2: Accessibility Software</p></caption>
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

<span id="_Toc83889334" class="anchor"></span>Table 2: Accessibility Software

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Users require group membership to access SharePoint and Teams' links. To request access, contact the E&E Program Management Office (PMO) or use the request access option at the SharePoint site and specify group membership.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer the Enrollment Health Benefits Determination (EHBD) Technical and Architectural Roadmaps on the ES SharePoint [here](https://dvagov.sharepoint.com/sites/OITEPMOESMESInternal/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x012000340A8C41EC79E44DA183F79D56F6B25B&viewid=9050ce4e%2Dda9e%2D4c93%2Da44a%2D6ce79985864d&id=%2Fsites%2FOITEPMOESMESInternal%2FShared%20Documents%2FLegacy%20Systems%2FESM%2FESM%20Project%20Artifacts).

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the Production Operations Manual (POM) on the ES SharePoint [here](https://dvagov.sharepoint.com/sites/OITEPMOESMESInternal/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x012000340A8C41EC79E44DA183F79D56F6B25B&viewid=9050ce4e%2Dda9e%2D4c93%2Da44a%2D6ce79985864d&id=%2Fsites%2FOITEPMOESMESInternal%2FShared%20Documents%2FLegacy%20Systems%2FESM%2FESM%20Project%20Artifacts).

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the Buttons/Admin section where User Accounts, Profiles, Roles and Capability Sets explain the different user access levels of the ES.

## ESM Application Information System Contingency Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the Enrollment System Modernization (ESM) Application Information System Contingency Plan on the ES SharePoint [here](https://dvagov.sharepoint.com/sites/OITEPMOESMESInternal/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x012000340A8C41EC79E44DA183F79D56F6B25B&id=%2Fsites%2FOITEPMOESMESInternal%2FShared%20Documents%2FLegacy%20Systems%2FESM%2FESM%20Project%20Artifacts%2FRegion%207%2DAustin%20ITC%2DESR%20Application%20%2D%20ISCP%2Epdf&parent=%2Fsites%2FOITEPMOESMESInternal%2FShared%20Documents%2FLegacy%20Systems%2FESM%2FESM%20Project%20Artifacts).

## ESM Project Artifacts SharePoint Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click the following [link](https://dvagov.sharepoint.com/sites/OITEPMOESMESInternal/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x012000340A8C41EC79E44DA183F79D56F6B25B&viewid=9050ce4e%2Dda9e%2D4c93%2Da44a%2D6ce79985864d&id=%2Fsites%2FOITEPMOESMESInternal%2FShared%20Documents%2FLegacy%20Systems%2FESM%2FESM%20Project%20Artifacts) to access the ESM Project Artifacts SharePoint site.

## Browser & Operating System Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ES is functional through Windows using Chrome or Edge.

2.  Internet Explorer (IE) and Firefox are not supported browsers. Users who have permission to have Firefox should not be using it to access ES.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Enrollment System (ES) Layout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ES displays a beneficiary's record data. The "Menu Bar" and the "Person Search Tabs"  provide access to various screens for viewing, updating, adding, and deleting information on ES.

Menu Bar

Menu Bar is where utility buttons for ES are located. From the Menu Bar, users view Worklists, perform Veteran Merges, perform Health Level 7 (HL7), Community Care Network (CCN), Third-Party Administrator (TPA) and Military Service Data Sharing (MSDS) Message Searches,  Load Registries, do an Undeliverable Mail Search, Generate/View Reports, Reference Thresholds/Enrollment Group Threshold (EGT) Settings, view Veterans Online Application (VOA) Re-submissions, Search and Add a New Person, and perform general Administrative functions such as enable or disable Veterans Community Care Eligibility (VCE) parameters.

 

![](ves-version-5-18-user-guide/002.png)

<span id="_Toc83889326" class="anchor"></span>Figure 1: Menu Bar

Summary

The Summary displays the beneficiary's Name, social security number (SSN), date of birth (DOB), date of death (DOD), Enrollment Status, Member ID (if available), and any other important information such as Open Work Items, Pending Merges, Sensitive Records, etc..

Sensitive Record information, if disclosed to the individual, may have serious adverse effects on the individual's mental or physical health. Such information may require explanation or interpretation by an intermediary or assistance in the information's acceptance and assimilation in order to preclude adverse impacts on the individual's mental or physical health.

![](ves-version-5-18-user-guide/003.png)

<span id="_Toc83889327" class="anchor"></span>Figure 2: Summary with a Sensitive Record

 

Person Search Tabs

Person Search Tabs are the area of the screen where the user may access the various kinds of information on record for the beneficiary to aid in determining his or her eligibility for enrollment in the VA healthcare system.

 

![](ves-version-5-18-user-guide/004.png)

<span id="_Toc83889328" class="anchor"></span>Figure 3: Person Search Tabs

3.  The terms [Veteran](javascript:hhctrl.TextPopup('A%20veteran%20is%20a%20person%20who%20has%20served%20in%20the%20armed%20forces.','Arial,10',10,10,00000000,0xffffff)), [beneficiary](javascript:hhctrl.TextPopup('A%20beneficiary%20is%20one%20that%20receives%20a%20benefit%20as%20in%20VA%20health%20care%20benefits.','Arial,10',10,10,00000000,0xffffff)), [patient](javascript:hhctrl.TextPopup('A%20patient%20is%20one%20who%20receives%20medical%20attention,%20care,%20or%20treatment.','Arial,10',10,10,00000000,0xffffff)), and [applicant](javascript:hhctrl.TextPopup('An%20applicant%20is%20one%20that%20applies%20for%20benefits%20as%20in%20VA%20health%20care%20benefits.','Arial,10',10,10,00000000,0xffffff)) are used interchangeably throughout ES. While not all applicants are Veterans or patients, not all applicants are beneficiaries either.  Whether they are a Veteran, patient or beneficiary is determined AFTER the application for benefits is received and processed.

 

![](ves-version-5-18-user-guide/005.png)

<span id="_Toc83889329" class="anchor"></span>Figure 4: Summary and Main Screen on ES

 

Sorting Columns

For screens that contain listed data, ascending and descending sorting may be performed for any category by clicking on the category name or on the symbol ![](ves-version-5-18-user-guide/006.png). Re-clicking the category name or symbol re-sorts the previous sort.

 

![](ves-version-5-18-user-guide/007.png)

<span id="_Toc83889330" class="anchor"></span>Figure 5: Sorting Columns

ES Online Help is an Online Help system built in Adobe RoboHelp, an authoring and publishing tool. The ES Online Help delivers an output to ES users when clicking the context-sensitive help buttons, System Help or Screen Help.

## ES Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In ES, you can obtain information about windows or dialogs clicking the context-sensitive help button![](ves-version-5-18-user-guide/008.png) available ES in the upper right-hand corner of the "System Help" and "Screen Help".

System Help:

> System Help is the top upper-right context-sensitive help button ![](ves-version-5-18-user-guide/009.png).

Screen Help:

> Screen Help is the lower upper-right context-sensitive help button ![](ves-version-5-18-user-guide/010.png).

4.  If you roll over the Help icons in ES, screen tips will appear distinguishing between "System Help" and "Screen Help".

![](ves-version-5-18-user-guide/011.png)

<span id="_Toc63260923" class="anchor"></span>Figure 6: System Help and Screen Help

(an online Table of Contents (TOC) is a summary of your project with topics arranged by category)

<u>ES Online Help Tool Bar</u>

To the left of the ES Online Help, above the table of contents pane, a tool bar contains *Contents, Index, Search* and *Glossary* links.

Table of Contents: ![](ves-version-5-18-user-guide/012.png)

Contents displays an expanded table of contents.

- Collapse / Expand (![](ves-version-5-18-user-guide/013.png), ![](ves-version-5-18-user-guide/014.png) )
- Topics (![](ves-version-5-18-user-guide/015.png)) are categories of information in the ES Online Help. Clicking![](ves-version-5-18-user-guide/016.png), you can view the contents of topic in the main screen located to the right.

Index: ![](ves-version-5-18-user-guide/017.png)

Index displays a multi-level list of keywords and keyword phrases. These terms are associated with topics in the ES Online Help and the keywords are intended to direct you to specific topics within the ES Online Help. Click the keyword to launch a topic from the TOC to the main screen. If the keyword is used with more than one topic, a list of topics displays under the keyword or keyword phrase in which the keyword or keyword phrase appears.

Search: ![](ves-version-5-18-user-guide/018.png)

Search provides a way to explore the content of the ES Online Help and find matches to ES-defined words. Unlike Index that lists author-defined keywords such as terms, synonyms, and cross-references, Search lists words used within the content of topics. To find a topic in which the word appears, click the letter link to display the words that begin with the letter being searched for. Words that appear once are in bold. Words that appear in multiple topics are listed with numbers. Click on a number to display the topic in the right-hand pane in which the word appears.

Glossary: ![](ves-version-5-18-user-guide/019.png)

Glossary provides a list of terms and definitions related to the subject-matter in ES. Click a letter in the top pane and see corresponding definitions that begin with the letter clicked in the lower pane.

The Enrollment System Help text uses Adobe RoboHelp's 2017 WebHelp as its output and is 508-compliant. The Online Help opens in your web browser as a new window.

<u>Other buttons and functions</u>Hide/Show the left pane

Provides a larger viewing area of the open topic and hides the left pane.

1.  Click the Hide link in the upper left side of the right pane to hide the left pane.
2.  Click the Show link in the upper left side of the pane to show the left pane.

Browser Toolbar

Since there is not a browser toolbar at the top of the ES Online Help window, right-click within ES Online Help window and select either Back or Forward to go back and forward through the history of visited topics, print a topic, or perform other tasks available within the Windows context-sensitive commands.

5.  The Forward command is only available if the Back command has been used first. At that point the Forward command becomes available.

The TOC on the left side of the ES Online Help can also be used to navigate throughout the ES Online Help.

WebHelp Build Date

Click the Systems Parameters topic to view the WebHelp Build Date. The build date is next to the topic title.

Adjusting the main screen and TOC size

Adjust the width and height of the main screen window by dragging the edges of the window in or out.

Adjust the width of the table of contents pane by pointing to the right edge of the left pane until the mouse pointer turns into a line with arrows on each end: ![](ves-version-5-18-user-guide/020.png) Drag the pane to the right or left with the left mouse button held down.

*Navigating Help Topics*

6.  The following navigational techniques generally refer to the Online Help, where indicated, and not the written documentation:

*Links (Online Help)*\* symbol indicates a required field in the Online Help.

![](ves-version-5-18-user-guide/021.png) symbol indicates a required field in the user guide.

![](ves-version-5-18-user-guide/022.png) symbol is displayed when a submitted field has an error.

![](ves-version-5-18-user-guide/023.png) symbol ("data changed") is displayed when a type of data has changed on the *History*, *Veteran Merge*, and user-related confirmation windows.

7.  Indicates a note or item of special interest.

## Compliance & Accessibility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With every release, the Department of Veterans Affairs strives to improve accessibility in the Enrollment System through the World Wide Web Consortium (W3C)'s Web Content Accessibility Guidelines (WCAG) 2.0, Levels A and AA.

It's important to mention that because Adobe RoboHelp displays a leveled hierarchy of contents through expanded and collapsed icons. Enrollment System users must click the collapsed ![](ves-version-5-18-user-guide/024.png)icon to display contents![](ves-version-5-18-user-guide/025.png)for that section and re-click the expanded ![](ves-version-5-18-user-guide/026.png) icon to close the contents of that section.

### Accessibility Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below lists accessibility software used to assist disabled users with the Enrollment System.

<table>
<caption>Accessbility Software Table.</caption>
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
<td>Assists blind and visually impaired Veterans with reading screens on ES either with a text-to-speech output or a Braille display.</td>
<td><a href="https://doccenter.freedomscientific.com/doccenter/archives/training/jawskeystrokes.htm">JAWS Keystrokes</a></td>
</tr>
<tr class="even">
<td>Window-Eyes</td>
<td>Reads specific text on an ES screen to a disabled Veteran. </td>
<td><a href="http://www.gwmicro.com/Window-Eyes/Manual/HTML/advanced.html">Window-Eyes Manual</a></td>
</tr>
<tr class="odd">
<td>MAGic </td>
<td>Magnifies ES screens to varying levels and assists Veterans with screen reading.</td>
<td><a href="https://www.freedomscientific.com/training/MAGicKeystrokes.htm">MAGic Keystrokes</a></td>
</tr>
<tr class="even">
<td>ZoomText Magnifier / Reader</td>
<td>Magnifies ES screens to varying levels and assists Veterans with screen reading.</td>
<td><a href="https://www.zoomtext.com/help/tutorial/">ZoomText Tutorial</a></td>
</tr>
<tr class="odd">
<td>Dragon Naturally Speaking</td>
<td><p>Through dictating ES functions, assists disabled Veterans with ES document downloads</p>
<p>and exports.</p></td>
<td><a href="https://www.nuance.com/dragon/user-documentation.html">Dragon NaturallySpeaking User Documentation</a></td>
</tr>
</tbody>
</table>

Accessbility Software Table.

If you have questions or comments regarding Adobe RoboHelp 2017 accessibility, please contact the [Adobe Accessibility Team](https://www.adobe.com/accessibility/feedback.html) and provide feedback on their feedback form. For further information on Adobe accessibility, please refer to the following link:

<https://www.adobe.com/accessibility/508standards.html>

## Standard Data Service (SDS) Lookup Tables 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SDS is a repository of enterprise-level reference tables. The SDS Lookup Tables contain information needed to define requirements and research the E&E process. The SDS Lookup Tables page enables a user to view information about a specific table (for example, table name, code, description, active status, date when a code became inactive). ES uses SDS tables in several of its applications.

Users access the SDS Lookup Tables screen by clicking the Reference Tables link at the top right of any ES screen.

To display the SDS Lookup Tables:

1.  Click the Reference Tables link and the SDS Lookup Tables page displays. SDS table and SDS History table names are listed in alphabetical order in the Navigation Bar.
3.  Select an SDS table name from the navigation bar. The right panel displays the first five columns in the selected table and the Table Name contains a link for downloading the whole table as an Excel spreadsheet. The Excel spreadsheet will display all the columns in the table.

![](ves-version-5-18-user-guide/027.png)

<span id="_Toc67408789" class="anchor"></span>Figure 7: SDS Lookup Table

*No data found for the selected table* displays if there is no data in an SDS Lookup Table.

## Exiting ES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To exit ES, click on the Sign Out link at the top of any page.

## Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None.

# Significant Additions and Updates to ES Version 5.18

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to 5.18 additions in below.

## COMPACT Act Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Person Search Tabs</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>COMPACT Act</strong> topic (at the bottom of the Eligibility book).</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the description is correct and accurate.</p>
<p><em>Veterans Comprehensive Prevention, Access to Care, and Treatment Act of 2020, better known as the Veterans COMPACT Act of 2020, supports administrative processes for Public Law No. 116-214.</em></p>
<p><em>COMPACT Act improves Department of Veterans Affairs transition assistance, suicide prevention for Veterans, and care and services for women Veterans. The COMPACT Act was signed into law on December 5th, 2020.</em></p>
<p>![](ves-version-5-18-user-guide/028.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## COMPACT Act on the Overview screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

<table>
<caption>Step/action table to disable autofill functionality from the ICN text field while using Chrome.</caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
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
<td>Click the <strong>Person Search Tabs</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Overview</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Scroll down to the "Update Current Eligiblity" field defintion.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the text and tables within each collapse/expand link is accurate.</p>
<ul>
<li><p>COMPACT Act eligibility</p></li>
<li><p>ineligible date</p></li>
<li><p>ineligible reason text</p></li>
<li><p>ineligible reason code</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/029.png)</p>
<p>![](ves-version-5-18-user-guide/030.png)</p>
<p>![](ves-version-5-18-user-guide/031.png)</p>
<p>![](ves-version-5-18-user-guide/032.png)</p>
<p>![](ves-version-5-18-user-guide/033.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## COMPACT Act: Dishonorable VA or FFP VHAP (302)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Menu Bar</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>References</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Core VHAPs</strong> topic.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the following text was added for the following new core VHAP. "Dishonorable VA or FFP".</p>
<p>![](ves-version-5-18-user-guide/034.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## COMPACT Act: Core VHAP Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Menu Bar</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>References</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Core VHAPs</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following text was added:</p>
<p><em>"For eligible individuals, under Veterans Comprehensive Prevention, Access to Care, and Treatment Act of 2020 (COMPACT), Section 201, VA will furnish, reimburse, pay for emergent suicide care, make referrals, as appropriate, for care following the period of emergent suicide care. Eligible individuals are ones who served in the active military service, regardless of length of service, and who were discharged, excluding anyone who received a dishonorable discharge or was discharged or dismissed by reason."</em></p>
<p>…to the following core VHAPs:</p>
<ul>
<li><p>Veteran Full Med Benefits Tx and Rx Copay Exmt (213)</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/035.png)</p>
<ul>
<li><p>Veteran Full Med Benefits Tx Copay Exmt and Rx Copay Req (214)</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/036.png)</p>
<ul>
<li><p>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 6 (215)</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/037.png)</p>
<ul>
<li><p>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 7 (216)</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/038.png)</p>
<ul>
<li><p>Veteran Full Med Benefits Tx Copay Req and Rx Copay Exmt 8 (217).</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/039.png)</p>
<ul>
<li><p>Veteran Full Med Benefits Tx and Rx Copay Req 6 (218)</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/040.png)</p>
<ul>
<li><p>Veteran Full Med Benefits Tx and Rx Copay Req 8 (219)</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/041.png)</p>
<ul>
<li><p>Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Exmt (220)</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/042.png)</p>
<ul>
<li><p>Veteran Full Med Benefits Tx GMT Copay Req and Rx Copay Req (221)</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/043.png)</p>
<ul>
<li><p>Veteran Restricted Med Benefits (222)</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/044.png)</p>
<ul>
<li><p>Non Veteran Other Restricted Med Benefits (223)</p></li>
</ul>
<p>![](ves-version-5-18-user-guide/045.png)</p>
<ul>
<li><p>Restricted Examination Only (224)</p></li>
</ul>
<p>Added the following text to core VHAP 224:</p>
<p><em>"For eligible individuals, under Veterans Comprehensive Prevention, Access to Care, and Treatment Act of 2020 (COMPACT), Section 201, VA will furnish, reimburse, pay for emergent suicide care, make referrals, as appropriate, for care following the period of emergent suicide care. Eligible individuals are Veterans who served in the active military service, regardless of length of service, and who were discharged, excluding anyone who received a dishonorable discharge or was discharged or dismissed by reason or while serving in the Armed Forces, was the victim of a physical assault of a sexual nature, a battery of a sexual nature, or sexual harassment."</em></p>
<p>![](ves-version-5-18-user-guide/046.png)</p>
<ul>
<li><p>Applicant in Process (226)</p></li>
</ul>
<p>Added the following text to core VHAP 226:</p>
<p><em>"For eligible individuals, under Veterans Comprehensive Prevention, Access to Care, and Treatment Act of 2020 (COMPACT), Section 201, VA will furnish, reimburse, pay for emergent suicide care, make referrals, as appropriate, for care following the period of emergent suicide care. Eligible individuals are Veterans who served in the active military service, regardless of length of service, and who were discharged, excluding anyone who received a dishonorable discharge or was discharged or dismissed by reason or while serving in the Armed Forces, was the victim of a physical assault of a sexual nature, a battery of a sexual nature, or sexual harassment."</em></p>
<p>\![](ves-version-5-18-user-guide/047.png)</p>
<ul>
<li><p>Ineligible (290)</p></li>
</ul>
<p>Added the following text to core VHAP 290:</p>
<p><em>"For eligible individuals, under Veterans Comprehensive Prevention, Access to Care, and Treatment Act of 2020 (COMPACT), Section 201, VA will furnish, reimburse, pay for emergent suicide care, make referrals, as appropriate, for care following the period of emergent suicide care. Eligible individuals are Veterans who served in the active military service, regardless of length of service, and who were discharged, excluding anyone who received a dishonorable discharge or was discharged or dismissed by reason or while serving in the Armed Forces, was the victim of a physical assault of a sexual nature, a battery of a sexual nature, or sexual harassment."</em></p>
<p>![](ves-version-5-18-user-guide/048.png)</p></td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the following text was removed from core VHAP "215":</p>
<p>Removed "a Pending Adjudication" (third bullet):</p>
<p>![](ves-version-5-18-user-guide/049.png)</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the following text was removed from core VHAP "217":</p>
<p>Removed "a Pending Adjudication" (from first bullet):</p>
<p>![](ves-version-5-18-user-guide/050.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## COMPACT Act: Community Care Program (CCP) Restricted Care (300) VHAP updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Menu Bar</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>References</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>CCP VHAPs</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following text was added to "Veteran Plan CCP Restricted Care" (300) VHAP:</p>
<p><em>The VHAP Veteran Plan CCP Restricted Care is assigned to:</em></p>
<p><em><u>Not enrolled covered Veterans</u>: Veterans who are NOT enrolled and non-Veterans who have the following eligibility:</em></p>
<p><em> </em></p>
<ul>
<li><p><em>SC 0% to 40%; SC 0% (non-compensable)</em></p></li>
<li><p><em>Was discharged or released from active military service for a disability incurred or aggravated in the line of duty for a 12-month period following discharge or release</em></p></li>
<li><p><em>Military Sexual Trauma (MST) Non-Veteran (Active Duty)</em></p></li>
<li><p><em>Emergent Mental Health (MH) Other-Than-Honorable (OTH) or Extended MH OTH</em></p></li>
</ul>
<p><em><u>COMPACT Act 2020 eligible Veterans</u>: Veterans who served in the active military service, regardless of length of service, and who were discharged, excluding anyone who received a dishonorable discharge or was discharged or dismissed by reason; are not enrolled in the health care system established by section 1705 of this title; and served in the Armed Forces for a period of more than 100 cumulative days: and was deployed in a theater of combat operations, or while serving in the Armed Forces, was the victim of a physical assault of a sexual nature, a battery of a sexual nature, or sexual harassment.</em></p>
<p>![](ves-version-5-18-user-guide/051.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## COMPACT Act: Ineligible Reason Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Person Search Tabs</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligibility</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>Ineligible Reason Code (Required)</strong> field.</td>
</tr>
<tr class="odd">
<td></td>
<td><p>Confirm the definition text and the rules under this field are correct.</p>
<p>![](ves-version-5-18-user-guide/052.png)</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>Navigate to the table of contents (on the left of the system help).</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Click the <strong>Edit Current Eligibility (Add a Person)</strong> topic.</td>
</tr>
<tr class="even">
<td>7</td>
<td>Scroll down to the <strong>Ineligible Reason Code (Required)</strong> field</td>
</tr>
<tr class="odd">
<td>8</td>
<td><p>Confirm the definition text and the rules under this field are correct.</p>
<p>![](ves-version-5-18-user-guide/053.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## COMPACT Act: Secondary Eligibility Determination of "COMPACT Act Eligible" rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Person Search Tabs</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Current Eligiblity</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Edit Current Eligiblity</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Ineligible Reason Code (Required):</strong> field.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Scroll down to the <strong>Secondary Eligibility Determination of "COMPACT Act" Eligible rules</strong>.</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the rules are correct and accurate.</p>
<p>![](ves-version-5-18-user-guide/054.png)</p>
<p>![](ves-version-5-18-user-guide/055.png)</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>Click the <strong>Person Search Tabs</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Click the <strong>Eligibility</strong> book.</td>
</tr>
<tr class="even">
<td>10</td>
<td>Click the <strong>Current Eligiblity</strong> book.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>Click the <strong>Edit Current Eligiblity (Add a Person)</strong> topic.</td>
</tr>
<tr class="even">
<td>12</td>
<td>Scroll down to the <strong>Ineligible Reason Code (Required):</strong> field.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>Scroll down to the <strong>Secondary Eligibility Determination of "COMPACT Act" Eligible rules</strong>.</td>
</tr>
<tr class="even">
<td>14</td>
<td><p>Confirm the rules are correct and accurate.</p>
<p>![](ves-version-5-18-user-guide/056.png)</p>
<p>![](ves-version-5-18-user-guide/057.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## COMPACT Act: Secondary Eligibility Code Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Person Search Tabs</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Secondary Eligibility Codes</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Secondary Eligibility Codes</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Veteran Eligiblity Codes:</strong> list.</td>
</tr>
<tr class="even">
<td>7</td>
<td><p>Confirm "COMPACT Act Eligible" and "Special TX Authority Care" are added to the list, and correct.</p>
<p>![](ves-version-5-18-user-guide/058.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Megabus Act Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Person Search Tabs</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Megabus Act</strong> topic (at the bottom of the Eligibility book).</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Confirm the Megabus Act decription is correct and accurate.</p>
<p><em>The Megabus Act (aka Section 5301 of the Johnny Isakson and David P. Roe, M.D. Veterans Health Care and Benefits Improvement Act of 2020) offers Military Service Trauma (MST) related health care services to Veterans and former Service Members with an "Other Than Honorable (OTH)" discharge.</em></p>
<p>![](ves-version-5-18-user-guide/059.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Megabus MST: SPECIAL TX AUTHORITY CARE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Person Search Tabs</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Other Eligibility Factors</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Scroll down to the <strong>SPECIAL TX AUTHORITY CARE</strong> field.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the text definition, if/then table, and note within this definition is correct and accurate.</p>
<p>![](ves-version-5-18-user-guide/060.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## CCN Regions Map Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Person Search Tabs</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Eligibility</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>Community Care</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>CCN Message Log</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Scroll down to the <strong>Manage Demographic Contact Information (Manage State/Regions)</strong> section.</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Confirm the FIVE updated regions and the updated map screen shot.</p>
<p>![](ves-version-5-18-user-guide/061.png)</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Navigate to the table of contents (on the left of the system help).</td>
</tr>
<tr class="even">
<td>8</td>
<td>Click the Community Care Determination topic (still under the Community Care book)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Scroll down to the "CCN Contractor Region" field definition.</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>Confirm the FIVE updated regions and the updated map screen shot.</p>
<p>![](ves-version-5-18-user-guide/062.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Paginating and Filtering User Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Menu Bar</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>Admin</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>User Profiles</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the second <strong>User Profiles</strong> book.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the View User Profiles topic.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Scroll down to the "Paginating and Filtering User Profiles" section</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the following text added for paginating and filtering user profiles is correct and accurate:</p>
<p>![](ves-version-5-18-user-guide/063.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Carveout VHAP Description Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Menu Bar</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>References</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Carveout VHAP</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following text added to the Carveout VHAP topic is correct and accurate:</p>
<p><em>Carveout VHA Profiles (VHAPs) are optional and may or may not be assigned together or separately to a Veteran's core VHAP.</em></p>
<p>![](ves-version-5-18-user-guide/064.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## CCP VHAP Description Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Menu Bar</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>References</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>CCP VHAP</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following text added to the CCP VHAP topic is correct and accurate:</p>
<p><em>Community Care Program (CCP) VHA Profiles (VHAPs) are categorized as a carveout and are optional, and may or may not be assigned together or separately to a Veteran's core VHAP.</em></p>
<p>![](ves-version-5-18-user-guide/065.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Core VHAP Description Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td>Click the <strong>Menu Bar</strong> book on the table of contents on the online help.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Click the <strong>References</strong> book.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Click the <strong>VHA Profiles</strong> book.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Click the <strong>Core VHAP</strong> topic.</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Confirm the following text added to the Core VHAP topic is correct and accurate:</p>
<p><em>Core VHA Profiles (VHAPs) describe the eligible benefits and copay responsibilities of a Beneficiary.A record can only have one core VHAP at a time. Because a record can only have one core VHAP at a time, a record will be placed in the best core VHAP available to the Beneficiary.</em></p>
<p>![](ves-version-5-18-user-guide/066.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the Troubleshooting section of the [Production Operations Manual (POM)](#data-flows) on the ES SharePoint.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: VES Version 5.17 User Guide

### Austin Information Technology Center

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation, maintenance, and monitoring of ES updates are performed at the Austin Information Technology Center (AITC) on the third Saturday of each month.

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the federal government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by VA of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

## OTH (Other Than Honorable) Pending 20-0986

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td><p>Click the following folders and topics on the table of contents:</p>
<ol type="1">
<li><p>Person Search Tabs</p></li>
<li><p>Eligibility</p></li>
<li><p>Current Eligibility</p></li>
<li><p>Edit Current Eligibility (Add a Person)</p></li>
</ol>
<p>![](ves-version-5-17-user-guide/028.png)</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>Scroll down to the <strong>Reason Eligibility Status is Pending Verification</strong> field.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the highighted text of "OTH (Other Than Honorable) Pending 20-0986".</p>
<p>![](ves-version-5-17-user-guide/029.png)</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>Navigate back to the TOC.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the <strong>Edit Current Eligibility</strong> topic (still under the <strong>Current Eligibility</strong> folder).</td>
</tr>
<tr class="even">
<td>6</td>
<td>Scroll down to the <strong>Reason Eligibility Status is Pending Verification</strong> field.</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the highighted text of "OTH (Other Than Honorable) Pending 20-0986".</p>
<p>![](ves-version-5-17-user-guide/030.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.

## Updated "Document Name" dropdown list; Archived Document Names

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm the following online help updates.

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
<td><p>Click the following folders and topics on the table of contents:</p>
<ol type="1">
<li><p>Person Search Tabs</p></li>
<li><p>Document Management</p></li>
<li><p>Search Documents topic</p></li>
</ol>
<p>![](ves-version-5-17-user-guide/031.png)</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>Scroll down to the <strong>Income Verification Document (IVD)</strong> field.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Confirm the highighted bulleted list.</p>
<p>![](ves-version-5-17-user-guide/032.png)</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>Navigate back to the TOC.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Click the <strong>Upload Documents</strong> topic (still under the <strong>Document Management</strong> folder).</td>
</tr>
<tr class="even">
<td>6</td>
<td>Scroll down to the <strong>Income Verification Document (IVD)</strong> field.</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>Confirm the highighted text.</p>
<p>![](ves-version-5-17-user-guide/033.png)</p></td>
</tr>
</tbody>
</table>

Step/action table to disable autofill functionality from the ICN text field while using Chrome.
