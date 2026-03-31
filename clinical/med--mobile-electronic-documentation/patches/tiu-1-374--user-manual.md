---
title: TIU*1*374 Mobile Electronic Documentation (MED) User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Mobile Electronic Documentation (MED)
app_code: MED
app_name: Mobile Electronic Documentation
section: CLI
app_status: active
pkg_ns: TIU
patch_ver: 1
patch_id: TIU*1*374
group_key: "MED:TIU:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - patient
  - table
  - contents
  - notes
  - span
  - error
  - class
  - strong
  - documentation
  - cprs
page_count: 0
word_count: 11945
section_count: 42
table_count: 9
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mobile_Electronic_Documentation/TIU_MED_UM.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mobile_Electronic_Documentation/TIU_MED_UM.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=190"
---

Mobile Electronic Documentation (MED)User Manual

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/001.png)

December 2025Department of Veterans AffairsOffice of Information and Technology (OIT)

<span id="_Toc282582928" class="anchor"></span>

Revision History

<table>
<caption><p><span id="_Ref300639441" class="anchor"></span>Table 1. MED—Security keys for validating patient identification for manually entered MED patients</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 43%" />
<col style="width: 30%" />
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
<td>12/2025</td>
<td>3.0</td>
<td><p>Patch TIU*1.0*374</p>
<p>Corrected <a href="#delete-scratch-pad-text">Delete Scratch Pad Text</a> steps</p>
<p>Added missing V2 to TIU MED GUI RPC in sections:</p>
<ul>
<li><p><a href="#v2_1">Retrieving Patient Records Overview</a></p></li>
<li><p><a href="#v2_2">RPC Broker Error</a></p></li>
</ul>
<p>Updated Signon text in Retrieving Patient Records Procedures, step 2: <a href="#sign_on_1">Retrieve From Personal List</a> and <a href="#sign_on_2">Select a Patient</a></p>
<p>Updated Signon <a href="#sign_on_3">Glossary</a> text.</p>
<p>Updated document format and made 508 compliant</p></td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>06/02/2017</td>
<td>2.9</td>
<td><p>Update for Patch TIU*1*311</p>
<p>Two-Factor Authentication (2FA)</p>
<p>Updated all MED document file references to the following:</p>
<ul>
<li><blockquote>
<p>TIU_1_311_MED_IG.doc/pdf</p>
</blockquote></li>
<li><blockquote>
<p>TIU_MED_TM.doc/pdf</p>
</blockquote></li>
<li><blockquote>
<p>TIU_MED_UM.doc/pdf</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/21/2011</td>
<td>2.8</td>
<td><p>Tech review and edit updates based on review/feedback from <mark>REDACTED</mark> review:</p>
<ul>
<li><p>Updated all MED document file references to the following:</p></li>
</ul>
<ul>
<li><blockquote>
<p>TIU_1_262_MED_IG.doc/pdf</p>
</blockquote></li>
<li><blockquote>
<p>TIU_1_262_MED_TM.doc/pdf</p>
</blockquote></li>
<li><blockquote>
<p>TIU_1_262_MED_UM.doc/pdf</p>
</blockquote></li>
</ul>
<ul>
<li><p>Updated all footers to reference MED GUI Software Version 2.3 and documentation Patch TIU*1.0*262.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/15/2011</td>
<td>2.7</td>
<td><p>Tech review and edit updates based on review/feedback from <mark>REDACTED</mark> review:</p>
<ul>
<li><p>Updated the following highlighted text in the second paragraph in Chapter 2:</p></li>
</ul>
<p>"After starting MED, in order to access the MED menu toolbars, you <em>must</em> first retrieve a patient, then select a patient from the Patient Selection opening dialogue."</p>
<ul>
<li><p>Updated the second Note in Chapter 2, on Page 3. Added the following text:</p></li>
</ul>
<p>"While connected to the VA network/VistA, if you do not supply the appropriate signon credentials (i.e., VA Access and Verify codes) you can access MED but <em>cannot</em> retrieve patients and summaries. You <em>must</em> sign into MED using the appropriate signon credentials <em>before</em> being given access to retrieve patient information from VistA."</p>
<ul>
<li><p>Updated the Cautionary Note in Section 3.1 as follows:</p></li>
</ul>
<p>"<strong>CAUTION: If the patient name on the list is <em>not</em> a manually entered patient, when MED is started, any notes that have been imported over 7 days prior are deleted. Then, any patients that are over 7 days old and do <em>not</em> have any pending or imported notes are deleted as well.</strong>"</p>
<p>And in Section 10.3.1.</p>
<ul>
<li><p>Updated notes in Step 2 in Section 3.2. Changed "need" to "needed."</p></li>
<li><p>Updated entering date of Birth information in Step 2d under the "Manually Enter a Patient" bullet in Section 3.2, Retrieving Patient Records Procedures."</p></li>
<li><p>Updated the "Summary Tab Overview" section. Changed "which includes:" to "which may include:".</p></li>
<li><p>Added the following sentence to blank pages added so all chapter/document ends on an even page for double-sided printing:</p></li>
</ul>
<p>"This page intentionally left blank for double-sided printing."</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/05/2011</td>
<td>2.6</td>
<td><p>Tech review and edit updates based on review/feedback from MED Core team:</p>
<ul>
<li><p>Added Step 3 to Section 3.2, "Retrieving Patient Records Procedures" informing users to press the <strong>Close</strong> button to return to MED after selecting patients, as per <mark>REDACTED</mark></p></li>
<li><p>Updated introductory paragraph and Step 1 procedures in Section 7.3, "Create and Assign a Health Summary to MED," as per <mark>REDACTED</mark>.</p></li>
<li><p>Added all missing errors from the MED Technical Manual to Chapter 12, "Appendix B—Troubleshooting."<br />
<br />
Includes updates to the "Write Access Error" error description and resolution to state users <em>must</em> be given <strong>Full Control</strong> access permission to the MED directory (i.e., Read, Write, Modify, and Execute), as <mark>REDACTED</mark></p></li>
<li><p>Added a Note informing users to enter a Remedy ticket if the resolutions listed in the errors described in Chapter 12, "Appendix B—Troubleshooting," do not resolve the issue.</p></li>
<li><p>Added the "CPRS CHART – Library Not Registered Error" error message to Chapter 12, "Appendix B—Troubleshooting," as per feedback from <mark>REDACTED</mark></p></li>
<li><p>Updated index entries for error messages in Chapter 12, "Appendix B—Troubleshooting."</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/11/2011</td>
<td>2.5</td>
<td><p>Tech review and edit updates based on review/feedback from MED Core team:</p>
<ul>
<li><p>Removed patch compliance dates from the "<a href="#_Toc336755501">How to Use this Manual</a>", as per <mark>REDACTED</mark>.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/10/2011</td>
<td>2.4</td>
<td><p>Tech review and edit updates based on review/feedback from MED Core team:</p>
<ul>
<li><p>Updated "<a href="#assumptions_about_the_reader">Assumptions About the Reader</a>" section to remove reference to the M programming language, as per Robert Graziani (SQA) review.</p></li>
<li><p>Reordered and added content and updated intro paragraph in the "Starting MED" section, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Added definitions for Retrieving Patient Records vs. Selecting Patient Records in MED in the "Retrieving Patient Records Overview" and "<a href="#_Toc250450991">Glossary</a>" sections, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Updated procedures in Step 1 in the "Retrieving Patient Records Procedures" section.</p></li>
<li><p>Added commentary to "Select a Patient" button in the "Retrieving Patient Records Procedures" section, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Added a Note regarding entering "Last Name,First Name" and spaces after comma in the "Manually Enter a Patient" bullet in the "Retrieving Patient Records Procedures" section, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Updated the "Selecting a Patient" section as per <mark>REDACTED</mark> review.</p></li>
<li><p>Removed instructions for disabling retrieval of Health Summaries in the "Summary Tab Procedures" section, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Added Cautionary Note to Step 3 in the "Retrieve Health Summaries from VistA" section.</p></li>
<li><p>Updated the Notes in the "Creating Templates and Directory Access" section.</p></li>
<li><p>Updated figures in Step 6 in the "New Progress Notes" section, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Added a Note to the Description field for the TIU MED MANUAL PATIENT security key in Table 1, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Updated patient names in Table 2 through Table 5, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Updated the image and directory path for the MED database reference in the "MED Database Open Error" section.</p></li>
<li><p>Added compact database messages to the new "MED Database Compact Messages" section, as per Seth Thompson email.</p></li>
<li><p>Removed author references, other than Project Manager and Tech Writer, from "Revision History" section, as per Product Support review.</p></li>
<li><p>Updated the Note contact info in Step 2b in the "Retrieving Patient Records Procedures" section, as per Product Support review.</p></li>
<li><p>Removed "Product Support (PS)" from the "<a href="#intended_audience">Intended Audience</a>" section, as per Product Support review.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/27/2011</td>
<td>2.3</td>
<td><p>Tech review and edit updates based on review/feedback from Product Support team:</p>
<ul>
<li><p>Added all Mobile Electronic Device (MED) VistA patch references and Graphical User Interface (GUI) client software version to the Title page.</p></li>
<li><p>Added the "<a href="#_Toc18284794">Orientation</a>" section in accordance with national documentation standards. Moved topics from the "Introduction" section into this new section.</p></li>
<li><p>Added a note regarding Access/Verify code prompt in the "Retrieving Patient Records Procedures" section.</p></li>
<li><p>Deleted the procedures for deleting a manually entered patient from the "Delete Manually Entered Patients (Duplicates)" section. This information is in the <em>MED Technical Manual</em>.</p></li>
<li><p>Added a Cautionary Note warning users about disabling Health Summaries in the "Summary Tab Procedures" section.</p></li>
<li><p>Added the "Create and Assign a Health Summary to MED" section.</p></li>
<li><p>Updated content in the "Creating Templates and Directory Access" section. Removed procedures for setting up network directory, since that information is already in the <em>MED Technical Manual</em>.</p></li>
<li><p>Deleted and moved the procedures for deleting a template from the "Deleting Templates" section. This information was moved to the <em>MED Technical Manual</em>.</p></li>
<li><p>Updated the content in the "Editing Existing Notes" section.</p></li>
<li><p>Updated the content in the "Finding Text in Notes" section.</p></li>
<li><p>Updated the Cautionary Note in the "Saving Notes" section.</p></li>
</ul></td>
<td><p>Project Manager—Tim Landy</p>
<p>Tech Writer—Thom Blom</p></td>
</tr>
<tr class="odd">
<td>07/14/2011</td>
<td>2.2</td>
<td><p>Tech review and edit updates:</p>
<ul>
<li><p>Updated the "Saving Notes" section to say "Select a new patient" rather than "Start a new patient," as per <mark>REDACTED</mark> review.</p></li>
<li><p>Added reference to procedures for selecting a new patient and added text to the Cautionary Note regarding shutting down the laptop <em>before</em> properly closing MED, as per <mark>REDACTED</mark> review.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/12/2011</td>
<td>2.1</td>
<td><p>Tech review and edit updates:</p>
<ul>
<li><p>Updated the "Date Sensitivity" section in the "Import Criteria for Progress Notes" topic, as per Jeanie Scott review.</p></li>
<li><p>Remedy Tickets #487293, 50587, and 502588: Updated content regarding properly saving a MED note in the "Saving Notes" section, as per Jeanie Scott review.<br />
<br />
Added the "Delete Manually Entered Patients" section regarding removing manually entered patients from the MED database, as per Jeanie Scott review.</p></li>
<li><p>Added the "Write Scratch Pad Text," "Find Scratch Pad Text," and "Delete Scratch Pad Text" (Remedy Ticket #487029) topics to the "Scratch Pad Tab" section, as per Jeanie Scott review.</p></li>
<li><p>Remedy Ticket #487861: Updated the "Creating Templates and Directory Access" and "Deleting Templates" sections with screen captures, as per Jeanie Scott review.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/23/2011</td>
<td>2.0</td>
<td><p>Tech review and updates:</p>
<ul>
<li><p>Renamed document to remove patch reference ID.</p></li>
<li><p>Reformatted document to follow current national documentation standards and style guides.</p></li>
<li><p>Added alternate text to all images for Section 508 compliance.</p></li>
<li><p>Updated the "Introduction" section to be consistent across the MED documentation set.</p></li>
<li><p>Updated Index entries.</p></li>
<li><p>Remedy Ticket #485510: Added the "Date Sensitivity" section in the "Import Criteria for Progress Notes" topic.</p></li>
<li><p>Remedy Tickets #465060 and #487293: Added the "Saving Notes" section with a Cautionary Note of known software anomaly.</p></li>
<li><p>Remedy Ticket #476482: Corrected Step 4 in "New Progress Notes" section.</p></li>
<li><p>Remedy Ticket #485507: Added the "Creating Templates and Directory Access" and "Deleting Templates" sections. These sections will need additional content updates: detailed procedures, examples, and GUI screen captures.</p></li>
<li><p>Made grammar, punctuation, and spelling updates as needed.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>06/03/2010</td>
<td>1.0</td>
<td>Initial document.</td>
<td>MED Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref300639441" class="anchor"></span>Table 1. MED—Security keys for validating patient identification for manually entered MED patients

Contents

<span id="_Toc250450967" class="anchor"></span>

Figures and Tables

Figures

Tables

<span id="_Toc18284794" class="anchor"></span>Orientation

<span id="_Toc336755501" class="anchor"></span>How to Use this Manual

The Mobile Electronic Documentation (MED) application consists of both a Veterans Health Information Systems and Technology Architecture (VistA) M Server component and a Microsoft® Windows laptop/client workstation Graphical User Interface (GUI) component:

- Original VistA M Server Patch: TIU\*1.0\*244 (released date: 06/03/2010).
- Updated VistA M Server Patch: TIU\*1.0\*257 (released date: 01/21/2011).
- Documentation-only VistA M Server Patch TIU\*1.0\*262.
- Current Laptop/Client Workstation software: MED.exe Version 2.3.311.6.

This manual is organized to help users understand the basic layout of the MED software and provide users with information about the specific tasks performed. It includes sections on the following topics:

- Starting MED—How to start the application
- Retrieving Patient Records—Supplying patient credentials

Selecting a Patient—How to select a patient

- Patient Information Available from Any Tab—An explanation of the features that are available from each MED tab
- Printing from Within MED
- Summary Tab

Scratch Pad Tab

- Notes Tab

Importing MED Notes into CPRS

- Appendix A—Keyboard Shortcuts for Common MED Commands
- Appendix B—Troubleshooting
- Appendix C—Mobile Electronic Documentation (MED) Frequently Asked Questions (FAQ)

MED works in tandem with CPRS; however, this manual does *not* attempt to fully document how to create templates or describe other functions of CPRS.

REF: For installation instructions; lists of routines, files, and options; additional technical information; and user information on CPRS, see the CPRS documentation on the VA Document Library (VDL) at the following link: <http://www.va.gov/vdl/application.asp?appid=61>

<span id="intended_audience" class="anchor"></span>Intended Audience

The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Information Resource Management (IRM)
- Clinical Application Coordinators (CAC)
- Home Based Primary Care (HBPC) end-users
- Product Support (PS).

Legal Requirements

There are no special legal requirements involved in the use of MED software.

Disclaimers

This manual provides an overall explanation of how to configure the MED software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Web sites on the Internet and VA Intranet for a general orientation to VistA. For example, visit the Office of Information & Technology (OIT) VistA Development VA Intranet Web site:

<http://vaww.vista.med.va.gov/>

DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
- Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, an MED test patient and user names would be documented as follows: MEDPATIENT,ONE; MEDPATIENT,TWO; MEDPATIENT,THREE; MEDUSER,ONE, MEDUSER,TWO, MEDUSER,THREE, etc.
- Sample HL7 messages, "snapshots" of computer online displays (i.e., character-based screen captures/dialogues) and computer source code are shown in a *non*-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft® Windows images (i.e., dialogues or forms).
- User's responses to online prompts will be boldface.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter key on their keyboard. Other special keys are represented within angle brackets (\< \>). For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

> NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the TIU MED MGT key).

Documentation Navigation

This document uses Microsoft® Word's built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word 2007 (not the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the dropdown arrow in the "Choose commands from:" box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Click/Highlight the Back command and press the Add button to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Click/Highlight the Forward command and press the Add button to add it to your customized toolbar.
9.  Press OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

> NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic.

> REF: See the Mobile Electronic Documentation (MED) Technical Manual for further information.

Online Help

VistA M-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M-based software.

The MED laptop/client workstation software includes an MED GUI online help file (i.e., MED.chm). Instructions, procedures, and other information are available from the. To access the online help do either of the following:

- Inside MED, click on the Help \| Contents menu options from the MED GUI toolbar or press the F1 key while you have any MED dialogue screen open.
- Outside MED, double-click on the MED.chm file.

Obtaining Data Dictionary Listings

Technical information about VistA M-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

> REF: For details about obtaining data dictionaries and about the formats available, see the "List File Attributes" chapter in the "File Management" section of the VA FileMan Advanced User Manual.

<span id="assumptions_about_the_reader" class="anchor"></span>Assumptions about the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- Microsoft® Windows

Reference Materials

Readers who wish to learn more about MED should consult the following:

- *Mobile Electronic Documentation (MED) Installation Guide (TIU\*1.0\*262)*—Contains instructions for installing, configuring, and deploying MED on the VistA M Server and Laptop/Client Workstation.
- *Mobile Electronic Documentation (MED) Technical Manual*—Contains instructions for implementing and maintaining the MED software on the VistA M Server and Laptop/Client Workstation.
- *FORUM Patches: TIU\*1.0\*244, TIU\*1.0\*257, and TIU\*1.0\*262.*

VistA documentation is made available online in Microsoft® Word format and Adobe® Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe® Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe® Systems Incorporated at the following Website:

<http://www.adobe.com/>

VistA documentation can be downloaded from the VHA Software Document Library (VDL) Website:

<http://www4.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Product Support (PS) anonymous directories:

- Preferred Method <span class="mark">REDACTED</span>

  NOTE: This method transmits the files from the first available FTP server.

  REDACTED

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Starting MED](#starting-med)
- [Retrieving Patient Records](#retrieving-patient-records)
  - [Retrieving Patient Records Overview](#retrieving-patient-records-overview)
  - [Retrieving Patient Records Procedures](#retrieving-patient-records-procedures)
  - [Delete Manually Entered Patients (Duplicates)](#delete-manually-entered-patients-duplicates)
- [Selecting a Patient](#selecting-a-patient)
- [Patient Information Available from Any Tab](#patient-information-available-from-any-tab)
- [Printing from Within MED](#printing-from-within-med)
  - [Printing Health Summaries and Notes Overview](#printing-health-summaries-and-notes-overview)
  - [Printing Health Summaries and Notes Procedures](#printing-health-summaries-and-notes-procedures)
- [Summary Tab](#summary-tab)
  - [Summary Tab Overview](#summary-tab-overview)
  - [Summary Tab Procedures](#summary-tab-procedures)
    - [Retrieve Health Summaries from VistA](#retrieve-health-summaries-from-vista)
    - [Find Health Summary Text](#find-health-summary-text)
  - [Create and Assign a Health Summary to MED](#create-and-assign-a-health-summary-to-med)
- [Scratch Pad Tab](#scratch-pad-tab)
  - [Scratch Pad Tab Overview](#scratch-pad-tab-overview)
  - [Scratch Pad Procedures](#scratch-pad-procedures)
    - [Write Scratch Pad Text](#write-scratch-pad-text)
    - [Find Scratch Pad Text](#find-scratch-pad-text)
    - [Delete Scratch Pad Text](#delete-scratch-pad-text)
  - [Creating Templates and Directory Access](#creating-templates-and-directory-access)
  - [Deleting Templates](#deleting-templates)
- [Notes Tab](#notes-tab)
  - [Icons on the Notes Tab](#icons-on-the-notes-tab)
  - [Viewing Notes](#viewing-notes)
  - [Creating and Editing Notes](#creating-and-editing-notes)
  - [Editing Existing Notes](#editing-existing-notes)
  - [Saving Notes](#saving-notes)
  - [Finding Text in Notes](#finding-text-in-notes)
- [Importing MED Notes into CPRS](#importing-med-notes-into-cprs)
  - [Existing Progress Notes](#existing-progress-notes)
  - [New Progress Notes](#new-progress-notes)
  - [Import Criteria for Progress Notes](#import-criteria-for-progress-notes)
    - [Date Sensitivity](#date-sensitivity)
    - [Security Keys](#security-keys)
    - [Import Examples](#import-examples)
- [Appendix A—Keyboard Shortcuts for Common MED Commands](#appendix-akeyboard-shortcuts-for-common-med-commands)
  - [Navigation Commands](#navigation-commands)
  - [File Menu Commands](#file-menu-commands)
  - [Edit Menu Commands](#edit-menu-commands)
  - [View Menu Commands](#view-menu-commands)
  - [Tools Menu Commands](#tools-menu-commands)
  - [Action Menu Commands](#action-menu-commands)
  - [Help Menu Commands](#help-menu-commands)
- [Appendix B—Troubleshooting](#appendix-btroubleshooting)
  - [Patch is Not Current in VistA Error](#patch-is-not-current-in-vista-error)
  - [MED Missing Remote Procedure Calls (RPCs) in VistA Error](#med-missing-remote-procedure-calls-rpcs-in-vista-error)
  - [Invalid Pointer Operation Error](#invalid-pointer-operation-error)
  - [Application Context Error](#application-context-error)
  - [Write Access Error](#write-access-error)
  - [CPRS CHART – Library Not Registered Error](#cprs-chart-library-not-registered-error)
  - [MED Database Open Error](#med-database-open-error)
  - [MED Database Compact Messages](#med-database-compact-messages)
  - [Network Connection Error](#network-connection-error)
  - [RPC Broker Error](#rpc-broker-error)
  - [CPRS Error](#cprs-error)
  - [Invalid Date Error](#invalid-date-error)
  - [Missing Required Data Fields Error](#missing-required-data-fields-error)
- [Appendix C—Mobile Electronic Documentation (MED) Frequently Asked Questions (FAQ)](#appendix-cmobile-electronic-documentation-med-frequently-asked-questions-faq)
- [A](#a)
- [C](#c)
- [D](#d)
- [E](#e)
- [F](#f)
- [G](#g)
- [H](#h)
- [I](#i)
- [K](#k)
- [L](#l)
- [M](#m)
- [N](#n)
- [O](#o)
- [P](#p)
- [R](#r)
- [S](#s)
- [T](#t)
- [U](#u)
- [V](#v)
- [W](#w)
Mobile Electronic Documentation (MED) 2.3.311.6 is a Veterans Health Information Systems and Technology Architecture (VistA) software application. It enables Department of Veterans Affairs (VA) staff to access a patient's previously downloaded electronic medical record information when not connected to the VA network. MED is designed to work in tandem with the Computerized Patient Record System (CPRS) as temporary storage of patient notes. This includes the ability to enter notes using CPRS exported Templates (.txml). MED promotes user satisfaction and efficiency in the login and documentation process by allowing access to CPRS at the point of care (POC) and avoid the duplicate process of charting handwritten notes at the end of the day.
When providing health care services, Home and Community Care staff (e.g., physicians, nurses, dieticians, social workers, and health care providers) must travel to a variety of geographic locations in which Internet access and coverage is often unreliable or sometimes unavailable. MED does the following:
- Allows access to secure patient information without the need for wireless Internet connectivity.
- Promotes the security of patient information by removing the need to print and carry excessive amounts of patient-sensitive data out of the clinical setting and into the community.
- Allows users to view and download to their secured laptops/client workstations Health Summary and MED Created Notes for patients in Home Based Primary Care (HBPC) Clinics.
- Provides the ability to enter and review patient documentation (e.g., Progress Notes) remotely at the point of care (POC), such as patient's home, when they are not connected to the VA network.
- Enables the transfer of patient data documented in MED during a home visit to be imported into CPRS as a patient note, which becomes part of the patient record.
- Minimizes errors from home visits by removing the need for paper records or the need to manually transfer (e.g., copy and paste) patient data from a mobile device.
> CAUTION: This version of MED does not encrypt data. All laptops/client workstations (PC) are required to have full disk encryption and VA security policies. PCs should have normal health checks including security updates and antivirus.
> Please be aware that if a PC is assigned to multiple users, MED notes and health summaries include patient information that is viewable to all users of the PC. Therefore, all users of the PC must have the same level of security access to view this information.

# Starting MED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start the Mobile Electronic Documentation (MED) laptop/client workstation software, double-click the Launch MED shortcut icon on the laptop/client workstation desktop:

<span id="_Toc205454281" class="anchor"></span>Figure 1. MED—Desktop shortcut icon

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/002.png)

After starting MED, in order to access the MED menu toolbars, you *must* first retrieve a patient, then select a patient from the Patient Selection opening dialogue:

<span id="_Ref300652448" class="anchor"></span>Figure 2. MED—Patient Selection dialogue

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/003.png)

> REF: For more information on selecting patient records in MED, see Section 4, "Selecting a Patient," in this manual.

> NOTE: While connected to the VA network/VistA, if you do not supply the appropriate signon credentials you can access MED but cannot retrieve patients and summaries. You must sign into MED using the appropriate signon credentials before being given access to retrieve patient information from VistA.

> REF: If you encounter any errors when running MED, see "[Appendix B—Troubleshooting](#_Appendix_B—Troubleshooting)" for more information.

# Retrieving Patient Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Retrieving Patient Records Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient lists should be retrieved (not just selected) within Mobile Electronic Documentation (MED) on a regular basis in order to ensure updated Health Summaries for all the patients the clinician might visit (including unscheduled visits).

- Retrieving Patient Records — When you retrieve patient records in MED, you are obtaining updated patient data (e.g., Health Summaries) from Veterans Information Systems Technology Architecture (VistA) and updating the MED Microsoft® Access database. In order to retrieve patient records in MED, you *must* be connected to VistA and will be prompted to enter your VistA signon credentials.
- Selecting Patient Records -When you select patient records in MED, you are selecting previously retrieved patients from the MED Microsoft® Access database. In order to select patient records in MED, you do *not* need to be connected to VistA and will *not* be prompted to enter your VistA signon credentials.

REF: For more information on selecting patient records in MED, see Section 4, "Selecting a Patient," in this manual.

You can refresh patient information from Veterans Information Systems Technology Architecture (VistA) if you are connected to the Department of Veterans Affairs (VA) Network and have been assigned the Mobile Electronic Documentation secondary option \[TIU MED GUI RPC <span id="v2_1" class="anchor"></span>V2\]. This ensures that recent updates will be reflected. For example:

- Patient Information (e.g., Name, SSN, DOB)
- Health Summary

> CAUTION: If the patient name on the list is not a manually entered patient, when MED is started, any notes that have been imported over 7 days prior are deleted. Then, any patients that are over 7 days old and do not have any pending or imported notes are deleted as well.

> NOTE: Patient retrieval time is only affected if over 20 patients are retrieved at one time.

## Retrieving Patient Records Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To retrieve patient records, perform the following procedures:

> **NOTE:** While connected to the VA network/VistA, if you do not supply the appropriate signon credentials you can access MED but *cannot* retrieve patients and summaries. You *must* sign into MED using the appropriate signon credentials *before* being given access to retrieve patient information from VistA.

1.  Choose either of the following options to retrieve patient records:
- On the Patient Selection dialogue (Figure 2), click the Retrieve Patient(s) button.
- On the MED menu toolbar:
1.  Select the File menu.
2.  Select Retrieve Patient(s) menu option.

The following Retrieve Patient(s) dialogue opens:

> <span id="_Ref300650667" class="anchor"></span>Figure 3. MED—Retrieve Patient(s) dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/004.png)

2.  From the Retrieve Patient(s) dialogue (Figure 3), you have three choices to retrieve patients:
- Retrieve From Personal List—Retrieve from a CPRS Personal List. It is recommended that you create a Personal List in CPRS and keep it updated.
1.  Click the Retrieve From Personal List button.
3.  Sign <span id="sign_on_1" class="anchor"></span>onto VistA: Enter your signon credentials.

> **NOTE:** If you are not prompted for your signon credentials, contact IRM to verify that the correct IP address and port number have been assigned to the MED shortcut executable target line. <span class="mark">REDACTED</span>.

4.  Select one of your personal lists in the left pane under "Personal List."
5.  Check/Uncheck the patient(s) you want to download to MED in the middle pane under "Patients."
6.  Click the Retrieve Checked Patients button in the right pane.

> <span id="_Toc205454284" class="anchor"></span>Figure 4. MED—Retrieve Patient(s): Personal Lists dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/005.png)

- Select a Patient—Retrieve a single patient.
1.  Click the Select a Patient button to retrieve a single patient.
7.  Sign <span id="sign_on_2" class="anchor"></span>onto VistA: Enter your signon credentials.

> **NOTE:** If you are not prompted for your signon credentials, contact IRM to verify that the correct IP address and port number have been assigned to the MED shortcut executable target line. <span class="mark">REDACTED</span>.

8.  Select a patient from the displayed list in the left pane, as you would in CPRS.
9.  Click the Retrieve Patient button in the right pane.

> <span id="_Toc205454285" class="anchor"></span>Figure 5. MED—Retrieve Patient(s): Select Patient dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/006.png)

- Manually Enter a PatientNOTE: Manual entry is for adding a patient in the event you did not download the patient prior to leaving the facility, or there is an unscheduled visit.

REF: For important information about importing notes for manually entered patients, see the "Importing MED Notes into CPRS" section.

1.  Click the Manually Enter a Patient button.
10. Enter the Name in the following format as you would in VistA:

LAST NAME,FIRST NAME,MIDDLE INITIAL

> NOTE: If the user types Last Name,First Name with a space after the comma, the patient will not be recognized when attempting to import into CPRS.

11. Enter the nine-digit Social Security Number (SSN).
12. Enter the Date of Birth (DOB) by doing either of the following:
- To easily and quickly add the DOB, manually enter the month, day, and year as follows:
1.  Single click on the value you want to change.
2.  Enter the desired number.
3.  Repeat for all DOB values as needed.
- Select the date from the dropdown list. You will have to scroll through the calendar dates to arrive at the correct year, since the MED DOB year defaults to 1899.
13. Click the Save Patient button.

> <span id="_Toc205454286" class="anchor"></span>Figure 6. MED—Retrieve Patient(s): Manually enter a Patient dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/007.png)

The updated information will be stored in the local database and new or updated patients will be available at the "Patient Selection" screen.

> **NOTE:** Health Summaries are stored as .hsm files in the db folder of MED. This folder resides on the local laptop that is used for the Home Based Primary Care (HBPC) visits.

3.  Press the Close button once you have selected all of your patients from VistA in order to exit out of VistA and return to MED.

## Delete Manually Entered Patients (Duplicates)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A duplicate patient record in the MED database (i.e., identical Last Name, First Name, SSN, and DOB) may occur when a provider manually enters a patient into MED while in the field, because he/she does not see that the VistA patient has already been retrieved into the MED patient list (i.e., MED Access database). If the provider enters a note to the VistA retrieved patient record and *not* the manually entered record, it will not get imported.

When importing a note for a duplicate patient, the MED import process first finds the manually entered patient. Since the note was not added to the manually entered patient, MED does not find a note for that patient. The only way to import the note for that patient is to delete the manually entered patient from the MED Access database.

Manually entered patients will *never* be automatically deleted. These patients can only be deleted from the patient list through the database. To delete a manually added patient from the MED Access database/selection list contact your CAC or IRM for assistance.

# Selecting a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After starting the Mobile Electronic Documentation (MED) software, the Patient Selection dialogue appears, as shown below:

<span id="_Ref300651796" class="anchor"></span>Figure 7. MED—Patient Selection dialogue

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/008.png)

> **NOTE:** In order to select patient records in MED, you do not need to be connected to VistA and will not be prompted to enter your VistA signon credentials.

Select a patient record to view. If you have a list of patients from which to select, perform the follow procedures:

1.  On the MED Patient Selection dialogue, select the patient using one of the following methods:
    - Choose a patient from the displayed list of patient names.
    - Type the first letter of the patient's last name and the last four digits of the patient's Social Security Number (SSN) (e.g., M0001).

> MED will try to match what you entered to a patient and highlight that patient. The patient's name and other information will appear below in the Patient Box located below the Retrieve Patient(s) button.

2.  Verify that the correct patient is highlighted.
    - If the correct patient is highlighted, click OK.
    - If the correct patient is not highlighted:
      1.  Scroll through the list to find the correct patient.
      2.  Highlight the name.
      3.  Click OK.

> NOTE: If MED finds more than one patient with the same last name and same last four digits of the SSN, the possible matches will be shown above the dividing line. Select the correct patient and click OK.

3.  When you click OK, MED opens to the Summary Tab (see Section 7).

> If you do not have a list of patients to select from, you will need to click on the "Retrieve Patient(s)" button. The process of retrieving patients is described in the previous section.

# Patient Information Available from Any Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Information for the currently selected patient is located at the top of the MED window and is available from any tab. The patient information includes:

- Name
- Social Security Number (SSN)
- Date of Birth (DOB)

<span id="_Toc205454288" class="anchor"></span>Figure 8. MED—Patient information

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/009.png)

# Printing from Within MED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Printing Health Summaries and Notes Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MED allows you to print the following information for patients:

- Reports: Patients with Notes Report—Report showing the patients that have Notes and Pending/Imported Notes for the Current Patient
- Health Summaries
- Individual Patient Notes
- Scratch Pad entries

Use the instructions in the topics that follow to print MED reports to network Microsoft Windows printer.

## Printing Health Summaries and Notes Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To print Health Summaries, Scratch Pad entries, Reports, and multiple Notes in MED, perform the following procedures:

1.  Launch MED.
1.  Select a patient to make the MED menu options visible on the Patient Selection form (see Section 4).
2.  Select the File menu.
3.  Select the Print option, as shown below:

> <span id="_Toc205454289" class="anchor"></span>Figure 9. MED Menus—File and Print options (partial capture)

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/010.png)

2.  The MED Print Documents dialogue opens, as shown below:

> <span id="_Toc205454290" class="anchor"></span>Figure 10. MED—Print Documents dialogue: Sample list of notes that can be printed

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/011.png)

4.  Select the documents you want to print by checking the checkbox next to each item. The Health Summary, Scratch Pad entries, and the currently selected Note (if applicable) are checked by default.
5.  Click Print. The Print dialogue opens, as shown below:

> <span id="_Toc205454291" class="anchor"></span>Figure 11. MED—Print dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/012.png)

6.  Select the Printer to which the documents should be sent and click OK.

# Summary Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Summary Tab Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Summary Tab is the first dialogue screen you see after selecting a patient. This tab displays the Health Summary text-based overview of a patient's condition and history, which includes:

- Patient demographics
- Advance Directive information
- Active problems
- Allergies and postings
- Active medications
- Clinical reminders
- Lab results
- Vitals
- List of appointments or visits

The actual information available depends on the Health Summary selected in the MED parameters. The local Clinical Application Coordinator (CAC) can modify the Health Summary displayed in MED as desired by the site.

<span id="_Toc205454292" class="anchor"></span>Figure 12. MED—Health Summary tab dialogue

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/013.png)

The MED Health Summary displays a variety of information about a patient.

## Summary Tab Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can type or select an item in the Find in Health Summary list to quickly jump to a section within the Health Summary. Health Summaries are retrieved by default.

> CAUTION: The effect of disabling retrieval of Health Summaries results in no Health Summaries being displayed for all patients.

### Retrieve Health Summaries from VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To change if Health Summaries are retrieved from VistA, perform the following procedures:

1.  Launch MED:
1.  Select a patient to make the MED menu options visible on the Patient Selection form (see Section 4).
4.  Select the Tools menu.
5.  Select the Settings option, as shown below:

> <span id="_Toc205454293" class="anchor"></span>Figure 13. MED Menus—Tools and Settings options (partial capture)

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/014.png)

7.  The Users & Settings dialogue opens. If not already selected, click on the Data & Files tab, as shown below:

> <span id="_Toc205454294" class="anchor"></span>Figure 14. MED Users & Settings dialogue—Data & Files

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/015.png)

8.  Check/Uncheck the Retrieve Health Summaries checkbox option.

> CAUTION: Unchecking the Retrieve Health Summaries checkbox disables retrieving/displaying Health Summaries results for all patients.

### Find Health Summary Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To find specific text in the Health Summary, perform the following procedures:

1.  Click Health Summary text.
2.  Select Edit\Find. The Find dialogue opens, as shown below:

> <span id="_Toc205454295" class="anchor"></span>Figure 15. MED—Find dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/016.png)

9.  Enter the text that you want to find.
10. Click FindNext. If the text is found, it will be highlighted in the Health Summary.

> <span id="_Toc205454296" class="anchor"></span>Figure 16. MED—Health Summary tab: Find dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/017.png)

## Create and Assign a Health Summary to MED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Based Primary Care (HBPC) staff should develop a Health Summary that is suitable for the type of care that they will be providing to their patients. Only one Health Summary can be assigned to a user. The CAC is responsible for creating and assigning the HBPC Health Summaries that will be used:

1.  Review the current Health Summaries in CPRS:
1.  Select the Reports tab.
6.  Select Health Summary.
11. Create a robust vs. minimal Health Summary to be used with MED; however, the MED Health Summary does not replace the need to review a patient's record in CPRS in preparation for patient visits. The length of the summary does *not* affect the length of time it takes to retrieve patients.

> **NOTE:** Patient retrieval time is only affected if over 20 patients are retrieved at one time.

# Scratch Pad Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Scratch Pad Tab Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scratch Pad allows you to store notes and other information for referral. This information can be viewed and/or printed, but *cannot* be copied or imported into the Computerized Patient Record System (CPRS). The purpose for Scratch Pad is similar to a post-it note. The local Clinical Application Coordinator (CAC) can create templates for you to use in the Scratch Pad if desired by the site (see Section 8.3).

<span id="_Toc205454297" class="anchor"></span>Figure 17. MED—Scratch Pad tab dialogue

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/018.png)

## Scratch Pad Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Write Scratch Pad Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To write text in the Scratch Pad, perform the following procedures:

1.  Launch Mobile Electronic Documentation (MED).
2.  Click on the Scratch Pad tab.
3.  Enter any text in the white text box below the patient's Name, SSN, and DOB, as shown below:

### Find Scratch Pad Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To find specific text in the Scratch Pad, perform the following procedures:

1.  Click the Scratch Pad tab.
4.  Select Edit\Find. The Find dialogue opens, as shown below:

> <span id="_Toc205454298" class="anchor"></span>Figure 18. MED—Find dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/019.png)

12. Enter the text that you want to find.
13. Click FindNext. If the text is found, it will be highlighted in the Scratch Pad.

> <span id="_Toc205454299" class="anchor"></span>Figure 19. MED—Scratch Pad tab: Find dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/020.png)

### Delete Scratch Pad Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To delete text in the Scratch Pad, perform the following procedures:

1.  Highlight the text portion you want to delete.
2.  Press Delete.

## Creating Templates and Directory Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A user can create a "personal template" in Text Integration Utility (TIU) if your site has enabled the CPRS parameter to perform this task. If you have a "personal template" that you would like to use in MED, contact your CAC or IRM to assist you.

> REF: For information on how to create Personal Templates, please refer to the TIU User Manual.

The local site Clinical Application Coordinator (CAC) can create TIU templates (.txml format). The CAC then exports those templates, with the exception of Reminder Dialogs, through the CPRS Template Editor into the Templates folder on the network share directory for use with MED Scratch Pad. MED only recognizes template files with the .txml extension.

> NOTE: Reminder Dialogs cannot be used within the MED application. In addition, you can use patient data objects in any template, but the data will not populate until the template is imported into CPRS.

By creating a network location to store MED templates, template management can be maintained on the network server instead of each individual laptop/client workstation. Those templates will automatically be pulled from the shared network directory to the local laptop/client workstation Templates folder when the user launches MED:

C:/Program Files/Mobile Electronic Documentation/Templates

> REF: For more information on Network Share Templates directory, see the "Create a Network Share Download Directory" section in the Mobile Electronic Documentation (MED) Technical Manual.

## Deleting Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The local Clinical Application Coordinator (CAC) or IRM staff can delete templates for you.

REF: For more information on deleting templates, see the "Deleting Templates" section in the Mobile Electronic Documentation (MED) Technical Manual.

# Notes Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Notes tab you can create a new Mobile Electronic Documentation (MED) note for a patient and view existing Pending and Imported Notes. Documents on the Notes tab are organized in a directory tree structure on the left side of the screen.

## Icons on the Notes Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The icons in front of the document titles on the Notes tab help identify and categorize documents. For example:

- ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/021.png) Notes Pending Import into Computerized Patient Record System (CPRS).
- ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/022.png) Notes Imported into CPRS within the Past 7 Days.

## Viewing Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view the text of a Note, perform the following procedures:

1.  Click the Notes tab.
14. Select a document title from the "Notes for this Patient" section in the upper left pane of the screen. The text of the Note will be displayed on the right pane of the screen.

> <span id="_Toc205454300" class="anchor"></span>Figure 20. MED—Notes tab

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/023.png)

## Creating and Editing Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a new Note, perform the following procedures:

1.  Click the Notes tab.
2.  Select the type of note to create from the "Create a Note" section in the lower left pane of the screen.

> <span id="_Toc205454301" class="anchor"></span>Figure 21. MED—Create a Note dialogue: Sample list of note templates that can be created

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/024.png)

15. Click the Create Note button. The Template screen for the type of Note you selected appears.
16. Fill in the information as you do in CPRS, and then click OK.

> **NOTE:** Patient Data objects cannot be edited or deleted. The information for that object will be updated by MED when you import the note into CPRS.

> <span id="_Toc205454302" class="anchor"></span>Figure 22. MED—Home Based Primary Care (HBPC) template: CO-HBPC Note (D)

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/025.png)

## Editing Existing Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit an existing Note, perform the following procedures:

1.  Click the Notes tab.
17. Select a document from the left upper pane of the screen labeled "Notes for this patient". The text of the Note will be displayed on the right side of the screen labeled "Note".
18. Select Action\\Edit Note. You can now edit the Note.

    NOTE: Patient Data objects cannot be edited or deleted.

## Saving Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, the MED software does not provide a Save button or auto-save action on the Notes tab. As a workaround, to save a note and write the data to the MED database on the laptop/client workstation, do one of the following actions:

- Close the MED software using the Close button ("X"), as shown below:

<span id="_Ref299369275" class="anchor"></span>Figure 23. MED—Close button

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/026.png)

- Select a new patient (see Section 4).

> CAUTION: Do not shut down the laptop/client workstation before properly closing MED; otherwise, data may be lost!

> Simply pressing the OK button does not save the note. In order to save your note, you must close MED by pressing the Close button ("X"; see Figure 23) to exit out of MED prior to closing, shutting down, or putting your laptop on standby. If you do not close MED first, the last note you created will not be saved to the MED database.

## Finding Text in Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To find specific text in a Note, perform the following procedures:

1.  Click the Notes tab.
2.  Select a document from the left upper pane of the screen labeled "Notes for this patient". The text of the note will be displayed on the right side of the screen labeled "Note".
3.  Right-click the text of the note.
4.  Select Find. The Find dialogue opens, as shown below:

> <span id="_Toc205454304" class="anchor"></span>Figure 24. MED—Find dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/027.png)

19. Enter the text that you want to find.
20. Click FindNext. If the text is found, it is highlighted in the Note.

> <span id="_Toc205454305" class="anchor"></span>Figure 25. MED—Notes tab: Find dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/028.png)

# Importing MED Notes into CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Notes tab in the Computerized Patient Record System (CRPS) application you can import Notes from the Mobile Electronic Documentation (MED) application. You *must* be connected to the Department of Veterans Affairs (VA) network to import notes from MED into CRPS.

## Existing Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To import a MED Note into an existing CPRS Progress Note for a patient, perform the following procedures:

1.  Launch CPRS and select the patient whose notes you wish to import.

> <span id="_Toc205454306" class="anchor"></span>Figure 26. CPRS—Patient Selection dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/029.png)

21. Select the Notes tab of CPRS.
22. Create or Edit a note, and move the cursor to where you would like to import the MED Note.
23. Double-click Templates\Shared Templates\Mobile Electronic Documentation. The Select Note to Import dialogue will open, as shown below:

> <span id="_Toc205454307" class="anchor"></span>Figure 27. CPRS—Select Note to Import dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/030.png)

24. Select the note to import.
25. Click OK.
26. The note will be imported into the CPRS Note that is currently being edited.

> **NOTE:** Patient data objects embedded in the note will be retrieved from VistA and updated with the appropriate values at the time of the import.

## New Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a new MED Progress Note and import it for a patient into CPRS, perform the following procedures:

1.  Launch CPRS and select the Patient whose notes you wish to import.

> <span id="_Toc205454308" class="anchor"></span>Figure 28. CPRS—Patient Selection dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/031.png)

27. Select the Notes tab of CPRS.
28. Ensure that you are not editing an existing note.
29. Double-click: Templates\Shared Templates\Mobile Electronic Documentation\Import M.E.D. Notes.
30. Select the location (if prompted), and enter the Progress Note properties.

> <span id="_Toc205454309" class="anchor"></span>Figure 29. CPRS—Progress Note Properties dialogue

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/032.png)

31. If there is a template associated with the Progress Note Title, complete it as usual. The "Select Note to Import" dialogue opens, as shown below:

> <span id="_Toc205454310" class="anchor"></span>Figure 30. MED—Select Note to Import dialogue (sample 1 of 2)

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/033.png)

> <span id="_Toc205454311" class="anchor"></span>Figure 31. MED—Select Note to Import dialogue (sample 2 of 2)

> ![](tiu-1-374-mobile-electronic-documentation-med-user-manual/034.png)

32. Select the note to import.
33. Click OK.
34. The note will be imported into the newly created CPRS Note.

> **NOTE:** An MED Import Note can be associated with a CPRS Progress Note title allowing you to create and import a note as you do in CPRS.

## Import Criteria for Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Date Sensitivity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is important to note that when MED is started it checks progress note dates and does the following:

- If the patient name on the list is *not* a manually entered patient, when MED is started, any notes that have been imported over 7 days prior are deleted.
- Any patients that are currently on the user's patient list over 7 days old and that do *not* have any pending or imported notes are deleted as well.
- Manually entered patients will *never* be automatically deleted. These patients can only be deleted from the patient list through the database.

  IMPORTANT: In order to avoid deletion of any progress notes or patient lists from MED and to get the latest Health Summary information, users should retrieve their patient lists every day!

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have a progress note for a manually entered patient, you *must* hold one of the following MED security keys:

<table>
<caption><p><span id="_Ref300646450" class="anchor"></span>Table 2. Import Example—TIU MED MANUAL PATIENT security key</p></caption>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Security Key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TIU MED MANUAL PATIENT</strong></td>
<td><p>If you hold this security key, the following <em>must</em> match exactly:</p>
<ul>
<li><p>The first letter of the last name.</p></li>
<li><p>The first letter of the first name.</p></li>
</ul>
<blockquote>
<p><strong>NOTE:</strong> If the user types Last Name,First Name with a space after the comma, the patient will <em>not</em> be recognized when attempting to import into CPRS.</p>
</blockquote>
<ul>
<li><p>The date of birth (DOB).</p></li>
<li><p>The nine-digit Social Security Number (SSN).</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>TIU MED MANUAL OVERRIDE</strong></td>
<td><p>If you hold this security key, the full SSN <em>must</em> match exactly.</p>
<p>CAUTION: Most users must <em>not</em> be given the TIU MED MANUAL OVERRIDE security key.<br />
<br />
It is suggested that there be a document review and patient review before importing notes into patient records that have typographical or missing data that stops a user from importing the information as outlined with the TIU MED MANUAL PATIENT security key.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref300646450" class="anchor"></span>Table 2. Import Example—TIU MED MANUAL PATIENT security key

### Import Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For example, if you hold the TIU MED MANUAL PATIENT security key and have added a manually entered patient like the one shown below, you will be allowed to import.

<table>
<caption><p><span id="_Toc205454329" class="anchor"></span>Table 3. Import Example—TIU MED MANUAL OVERRIDE security key: Different names</p></caption>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>CPRS Patient:</strong></p>
<p><strong>Name:</strong> MED,PATIENT ONE</p>
<p><strong>DOB:</strong> 01/01/1950</p>
<p><strong>SSN:</strong> 000-44-0001</p></th>
<th><p><strong>MED Patient:</strong></p>
<p><strong>Name:</strong> MED,PATIENTS ONE</p>
<p><strong>DOB:</strong> 01/01/1950</p>
<p><strong>SSN:</strong> 000-44-0001</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc205454329" class="anchor"></span>Table 3. Import Example—TIU MED MANUAL OVERRIDE security key: Different names

However, if you have added a manually entered patient like any of those shown below, you will *not* be allowed to import if you only have the TIU MED MANUAL PATIENT security key.

Holders of the TIU MED MANUAL OVERRIDE security key *can* import patients with different names:

<table>
<caption><p><span id="_Toc205454330" class="anchor"></span>Table 4. Import Example—TIU MED MANUAL OVERRIDE security key: Different DOB</p></caption>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>CPRS Patient:</strong></p>
<p><strong>Name:</strong> MED,<strong><u>P</u></strong>ATIENT ONE</p>
<p><strong>DOB:</strong> 01/01/1950</p>
<p><strong>SSN:</strong> 000-44-0001</p></th>
<th><p><strong>MED Patient:</strong></p>
<p><strong>Name:</strong> MED,<strong><u>C</u></strong>ASE ONE</p>
<p><strong>DOB:</strong> 01/01/1950</p>
<p><strong>SSN:</strong> 000-44-0001</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc205454330" class="anchor"></span>Table 4. Import Example—TIU MED MANUAL OVERRIDE security key: Different DOB

Holders of the TIU MED MANUAL OVERRIDE key *can* import patients with different DOBs:

<table>
<caption><p><span id="_Ref300646459" class="anchor"></span>Table 5. Import Example—Unable to import due to different SSNs</p></caption>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>CPRS Patient:</strong></p>
<p><strong>Name:</strong> MED,PATIENT ONE</p>
<p><strong>DOB:</strong> 01/<strong><u>01</u></strong>/1950</p>
<p><strong>SSN:</strong> 000-44-0001</p></th>
<th><p><strong>MED Patient:</strong></p>
<p><strong>Name:</strong> MED,PATIENT ONE</p>
<p><strong>DOB:</strong> 01/<strong><u>21</u></strong>/1950</p>
<p><strong>SSN:</strong> 000-44-0001</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref300646459" class="anchor"></span>Table 5. Import Example—Unable to import due to different SSNs

This record *cannot* be imported regardless of the security key a user holds, since the SSN does not match:

<table>
<caption><p><span id="_Toc205454332" class="anchor"></span>Table 6. MED Navigation commands—Keyboard shortcuts</p></caption>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>CPRS Patient:</strong></p>
<p><strong>Name:</strong> MED,PATIENT ONE</p>
<p><strong>DOB:</strong> 01/01/1950</p>
<p><strong>SSN:</strong> 000-44-<strong><u>0001</u></strong></p></th>
<th><p><strong>MED Patient:</strong></p>
<p><strong>Name:</strong> MED,PATIENT ONE</p>
<p><strong>DOB:</strong> 01/01/1950</p>
<p><strong>SSN:</strong> 000-44-<u>0002</u></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc205454332" class="anchor"></span>Table 6. MED Navigation commands—Keyboard shortcuts

# Appendix A—Keyboard Shortcuts for Common MED Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix discusses the keyboard shortcut equivalents for common Mobile Electronic Documentation (MED) commands. This allows users who prefer using shortcuts or other users with limited vision or dexterity to use the software effectively and make it accessible.

## Navigation Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| MED Navigation Command                                                                                    | Keyboard Shortcut      |
|-----------------------------------------------------------------------------------------------------------|------------------------|
| Select the Health Summary tab                                                                             | Ctrl + S               |
| Select the Notes tab                                                                                      | Ctrl + N               |
| Advance to the next field, button, or control (left to right)                                             | Tab                    |
| To exit a field that accepts tabs (e.g., the text of a Note) and move to the next control (left to right) | Control + Tab          |
| To exit a field that accepts tabs and move to the previous control (right to left)                        | Shift + Control + Tab  |
| Pull down a list box                                                                                      | Down Arrow             |
| Navigate a list box                                                                                       | Up Arrow or Down Arrow |
| Select an item in a list box                                                                              | Enter                  |
| To switch between the tabbed page of a dialogue box                                                       | Control + Tab          |
| To toggle a check box on or off                                                                           | Spacebar               |

<span id="_Toc205454333" class="anchor"></span>Table 7. MED File menu commands—Keyboard shortcuts

## File Menu Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Menu Command     | Keyboard Shortcut         |
|-----------------------|---------------------------|
| Select New Patient    | Alt-F-N or Ctrl + Alt + N |
| Retrieve Patient List | Alt-F-L or Ctrl + Alt + P |
| Print                 | Alt-F-P or Ctrl + P       |
| Exit                  | Alt-F-X                   |

<span id="_Toc205454334" class="anchor"></span>Table 8. MED Edit menu commands—Keyboard shortcuts

## Edit Menu Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Edit Menu Command | Keyboard Shortcut   |
|-------------------|---------------------|
| Undo              | Alt-E-U or Ctrl + Z |
| Find              | Alt-E-F or Ctrl + F |
| Cut               | Alt-E-T or Ctrl + X |
| Copy              | Alt-E-C or Ctrl + C |
| Paste             | Alt-E-P or Ctrl + V |
| Select All        | Alt-E-A or Ctrl + A |

<span id="_Toc205454335" class="anchor"></span>Table 9. MED View menu commands—Keyboard shortcuts

## View Menu Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| View Menu Command | Keyboard Shortcut   |
|-------------------|---------------------|
| Summary Tab       | Alt-V-S or Ctrl + S |
| Notes Tab         | Alt-V-N or Ctrl + N |

<span id="_Toc205454336" class="anchor"></span>Table 10. MED Tools menu commands—Keyboard shortcuts

## Tools Menu Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Tools Menu Command | Keyboard Shortcut |
|--------------------|-------------------|
| Change Password    | Alt-T-P           |
| Users & Settings   | Alt-T-U           |
| Compact Database   | Alt-T-C           |

<span id="_Toc205454337" class="anchor"></span>Table 11. MED Action menu commands—Keyboard shortcuts

## Action Menu Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Action Menu Command | Keyboard Shortcut |
|---------------------|-------------------|
| Delete Note         | Alt-A-D           |
| Edit Note           | Alt-A-E           |

<span id="_Toc205454338" class="anchor"></span>Table 12. MED Help menu commands—Keyboard shortcuts

## Help Menu Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Help Menu Command | Keyboard Shortcut |
|-------------------|-------------------|
| Contents          | Alt-H-C           |
| About MED         | Alt-H-A           |

# Appendix B—Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix discusses the various errors and other messages you may encounter while using the Mobile Electronic Documentation (MED) application.

> **NOTE:** If the resolutions listed for the errors described in this section do *not* resolve the error or problem, <span class="mark">REDACTED</span>.

## Patch is Not Current in VistA Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed when an older version of MED is installed or is the wrong KIDS version in VistA:

<span id="_Toc303065793" class="anchor"></span>Figure 32. MED Error—Patch TIU\*1\*257 is not current in VistA

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/035.png)

Description:

MED is not installed or an older version is installed on VistA.

Resolution:

Install/Reinstall the latest patch.

## MED Missing Remote Procedure Calls (RPCs) in VistA Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed when an older version of MED is installed in VistA:

<span id="_Toc303065794" class="anchor"></span>Figure 33. MED Error—Missing RPCs

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/036.png)

Description:

MED is not installed or an older version is installed on VistA and is missing remote procedure calls (RPCs).

Resolution:

Install/Reinstall the latest patch.

## Invalid Pointer Operation Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed if the MED VistA KIDS install is not correct:

<span id="_Toc303065795" class="anchor"></span>Figure 34. MED Error—Invalid pointer operation

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/037.png)

Description:

The MED application is missing all the remote procedure calls (RPCs).

Resolution:

Install/Reinstall the latest patch.

## Application Context Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed for MED application context errors:

<span id="_Toc303065796" class="anchor"></span>Figure 35. MED Error—Application context

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/038.png)

Description:

Application context is a menu requirement for using all Remote Procedure Call (RPC) Broker calls. Each application has its own application context. The MED application context is TIU MED GUI RPC V2.

Resolution:

The TIU MED GUI RPC V2 menu option is distributed with Patch TIU\*1\*257 and needs to be assigned to all MED users, either on a common menu or one of the user's secondary menus.

## Write Access Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following access error may be displayed for MED application users who do *not* have the appropriate access permissions to the MED directory:

<span id="_Toc303065797" class="anchor"></span>Figure 36. MED Error—Write access permissions error

Exception EFCreateError in module MED.exe at 0002363E

Cannot create file "C:\Program Files\Mobile Electronic Documentation\med.err". Access is denied.

Description:

The user does not have the appropriate access permissions to the MED executable directory on the client workstation/laptop. In order for users to write the appropriate information while using the MED software, all users *must* be given Full Control access permission to the following MED application directory:

C:\Program Files\Mobile Electronic Documentation

Resolution:

Give all users Full Control access permission to the following MED application directory on the client workstation/laptop:

C:\Program Files\Mobile Electronic Documentation

## CPRS CHART – Library Not Registered Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following access error may be displayed when trying to import a MED note into CPRS for those MED application users who do *not* have the appropriate access permissions to the MED directory:

<span id="_Toc303065798" class="anchor"></span>Figure 37. MED Error—CPRS CHART – Library Not Registered Error

CPRS CHART – Library Not Registered

Description:

The user does *not* have the appropriate access permissions to the MED executable directory on the client workstation/laptop. In order for users to write the appropriate information while using the MED software, all users *must* be given Full Control access permission to the following MED application directory:

C:\Program Files\Mobile Electronic Documentation

Resolution:

Give all Home Based Primary Care (HBPC) users Full Control access permission to the following MED application directory on the client workstation/laptop:

C:\Program Files\Mobile Electronic Documentation

## MED Database Open Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed if there is a problem with opening the MED database:

<span id="_Toc303065799" class="anchor"></span>Figure 38. MED Error—Database is not installed correctly

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/039.png)

Description:

The MED.mdb database should be in the following db subdirectory:

C:\Program Files\Mobile Electronic Documentation\db\MED.mdb

Resolution:

Install/Reinstall Patch TIU\*1.0\*257 (TIU\*1.0\*257.KID package).

## MED Database Compact Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Warning Message:

The following warning message will be displayed when compacting the MED Microsoft® Access database:

<span id="_Toc303065800" class="anchor"></span>Figure 39. MED Warning—Database closing

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/040.png)

After clicking YES, you should see the following message:

<span id="_Toc303065801" class="anchor"></span>Figure 40. MED Information Message—Database Compacted

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/041.png)

After pressing OK, MED closes.

Description:

When the MED database meets or exceeds this size in the Suggest Compact After (MB) field (default value is 1024 MB), MED automatically prompts the user to compact the database. Currently, it is suggested the user answer No to compact the database when prompted. If users choose to compact the database they will see a series of warning and action messages (see above).

The MED.mdb database should be in the following db subdirectory:

C:\Program Files\Mobile Electronic Documentation \db\MED.mdb

> REF: For more information on compacting the MED database, see Step 3o in the "Configure Client Workstation" section in the *Mobile Electronic Documentation (MED) Technical Manual*.

Resolution:

Close and save all open notes *before* compacting the MED Microsoft® Access database.

## Network Connection Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following blank dialogues may be displayed if the MED RPC Broker fails to make a VistA connection:

<span id="_Toc303065802" class="anchor"></span>Figure 41. MED Error—Network Connection: Blank Retrieve Patient(s) dialogue (1 of 2)

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/042.png)

Or:

<span id="_Toc303065803" class="anchor"></span>Figure 42. MED Error—Network Connection: Blank Retrieve Patient(s) dialogue (2 of 2)

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/043.png)

Description:

There may be a very long pause after selecting Retrieve Patients, and then the Retrieve Patients dialogue is blank. MED is running but *not* connected to VistA.

Resolution:

Check the desktop shortcut. Verify that the IP server address and port number is correct. Also, check for a network connection error.

## RPC Broker Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message

You may see the following Remote Procedure Call (RPC) Broker error dialogue when starting MED:

<span id="_Toc298167198" class="anchor"></span>Figure 43. Errors—RPC Broker Error: Patient list retrieval error

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/044.png)

Description:

This means that the user has not been assigned the Mobile Electronic Documentation secondary option \[TIU MED GUI RPC <span id="v2_2" class="anchor"></span>V2\].

Resolution:

Contact the Information Resource Management (IRM) or Clinical Applications Coordinator (CAC) to gain access to the Mobile Electronic Documentation secondary option \[TIU MED GUI RPC V2\].

## CPRS Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message

You may see the following dialogue when trying to import notes into CPRS:

<span id="_Toc298167199" class="anchor"></span>Figure 44. Errors—CPRS - Patient Chart Error: Importing notes error message

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/045.png)

Description:

You may be trying to import MED notes on a computer that does not have MED installed. For example, MED is installed on the laptop/client workstation, but you are trying to import MED notes on another client workstation.

Resolution:

If MED is loaded on the laptop/client workstation, contact IRM for assistance to "re-register" the MEDImport.dll file and then restart CPRS.

## Invalid Date Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed during the patient import process:

<span id="_Toc303065806" class="anchor"></span>Figure 45. MED Error—Invalid date

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/046.png)

Description:

The Date of Birth (DOB) is in the wrong format in the MED database (MED.mdb). Click the OK button to retrieve more details.

Resolution:

Verify that the correct MED GUI Version is running on the laptop/client workstation. If it is the correct GUI, then the current patient information is from a prior version. To fix this, use the current MED GUI to retrieve the patient data and it will properly update the DOB in the MED database.

## Missing Required Data Fields Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following types of error messages may be displayed for missing data fields (highlighted):

<span id="_Toc303065807" class="anchor"></span>Figure 46. MED Error—Missing required data fields and Section 508 compliance: Active Caption Color

![](tiu-1-374-mobile-electronic-documentation-med-user-manual/047.png)

Description:

Required fields in templates that are missing data will display a warning message, and the missing fields will be highlighted in blue. Just as in CPRS, the template *cannot* be completed and saved unless the required fields are completed. Unlike CPRS regular dialog templates, the missing fields will be obviously marked.

> NOTE: Prior versions of MED highlighted required missing data fields in yellow. To make MED Section 508 compliant, the color of the fields is now set to Active Caption Color.

> REF: For more information on making templates Section 508 compliant, see the "Missing Required Data Fields Error" section in this manual.

Resolution:

Enter the missing required data fields.

Users can reset he highlight colors by changing the Microsoft® Windows theme.

# Appendix C—Mobile Electronic Documentation (MED) Frequently Asked Questions (FAQ)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 47%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Question</th>
<th>Answer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Will I need to purchase a certain device or hardware in order to use Mobile Electronic Documentation (MED)?</td>
<td>No. MED can run on any Microsoft® Windows-based laptop/client workstation, but is not designed for use with a tablet device.</td>
</tr>
<tr class="even">
<td>2</td>
<td>How can I get MED, and is it only available for the Home Based Primary Care (HBPC) Programs?</td>
<td>MED is a standalone application. All VA facility Information Technology (IT) departments have the software, which is installed on individual laptops/client workstations. MED is not restricted for use in the HBPC program. The software can be used by any VA staff needing access to the patient electronic medical records when not connected to the VA network.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Can I still use other programs such as CPRS, Microsoft (MS) Outlook or VistA when I am using MED.</td>
<td>Yes. You can use MED with other programs that IT has installed on the laptop/client workstation. MED actually requires interaction with VistA and CPRS for loading the patient information and transferring the notes into the clinical record.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Can I use MED at home?</td>
<td>Yes, if you have virtual private network (VPN) access. MED can be used with VPN in the office or at home. You can upload and download patient progress notes in MED while using VPN.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>What must I do prior to having the MED software loaded on my laptop?</td>
<td>To prepare for using MED, you will need a customized Health Summary. You will need a list of progress note templates that will be used with MED. The Clinical Application Coordinator will assist you to design customized health summaries and progress note templates that you will use in MED.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Do I need any special permission or security clearance in order to use the MED software?</td>
<td>No. The MED software meets all VA security and encryption requirements.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>How much time does it take to retrieve (download) a list of patients in MED?</td>
<td>For small lists of 20-30 patients, it takes approximately 3-5 minutes. Larger lists containing over 150 patients will take approximately 30-35 minutes to download into MED.</td>
</tr>
<tr class="even">
<td>8</td>
<td>Will MED alert the user to restricted patient records?</td>
<td>Yes. MED will start the retrieval process which includes restricted record. MED will display them at the end the retrieval process, alerting the user in the same manner that CPRS does. The user then has the option to continue to retrieve the restricted record or not to.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Can I complete clinical reminders when using MED?</td>
<td>No. As an option, you can complete a clinical reminder by editing a MED progress note once the template is uploaded into CPRS, prior to signature (completing the note).</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>Why can't I cut and paste from the scratch pad?</p>
<p>![](tiu-1-374-mobile-electronic-documentation-med-user-manual/048.png)</p></td>
<td>This is to ensure that users do not accidentally copy and paste into the wrong patient record. You can copy and paste into the scratch pad, but you cannot copy and paste from the scratch pad.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>Will the ePads for obtaining consents and signatures on Advanced Directives be compatible with the MED program? </td>
<td>MED is not designed for use with iMed Consent. MED is only compatible with CPRS.</td>
</tr>
<tr class="even">
<td>12</td>
<td>Will MED do appointing and scheduling?</td>
<td>No, MED doesn't link with either the Appointment Management or Event Capture modules.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>Can you enter Encounter information while working in MED?</td>
<td>The encounter will need to be created and completed in CPRS when transferring the notes from MED.</td>
</tr>
<tr class="even">
<td>14</td>
<td>What do I need to do to safeguard patient information in MED since it doesn't have its own password?</td>
<td>The patient information is protected on the laptop/client workstation using several key steps Virtual Private Network (VPN) security, encryption and protection while communicating with the VA servers (CPRS, VistA, Outlook, etc.), Microsoft® Windows-based password protection and User physical safeguard of the computer while signed on such as ensuring information not viewable or available to unauthorized users.</td>
</tr>
</tbody>
</table>

<span id="_Toc250450991" class="anchor"></span>Glossary

|                            |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPRS                       | Computerized Patient Record System, the VistA package (in both GUI and character-based formats) that provides access to most components of the patient chart.                                                                                                                                                                                                                                                      |
| CAC                        | Clinical Applications Coordinator. The CAC is a person at a hospital or clinic assigned to coordinate the installation, maintenance and upgrading of CPRS and other VistA software programs for the end users.                                                                                                                                                                                                     |
| HEALTH SUMMARY             | A VistA product that can be viewed through CPRS, Health Summaries are components of patient information extracted from other VistA applications.                                                                                                                                                                                                                                                                   |
| HBPC                       | Home Based Primary Care.                                                                                                                                                                                                                                                                                                                                                                                           |
| PROGRESS NOTES             | A component of TIU that can function as part of CPRS.                                                                                                                                                                                                                                                                                                                                                              |
| VISTA                      | Veterans Information Systems Technology Architecture.                                                                                                                                                                                                                                                                                                                                                              |
| MED                        | Mobile Electronic Documentation. Application that provides remote documentation and importing of notes into CPRS.                                                                                                                                                                                                                                                                                                  |
| MED NOTES                  | Notes created from exported CPRS Templates that can then be re-imported into CPRS.                                                                                                                                                                                                                                                                                                                                 |
| RETRIEVING PATIENT RECORDS | When you retrieve patient records in MED, you are obtaining updated patient data (e.g., Health Summaries) from Veterans Information Systems Technology Architecture (VistA) and updating the MED Microsoft® Access database. In order to retrieve patient records in MED, you *must* be connected to VistA and will be prompted to enter your VistA <span id="sign_on_3" class="anchor"></span>signon credentials. |
| SELECTING PATIENT RECORDS  | When you select patient records in MED, you are selecting previously retrieved patients from the MED Microsoft® Access database. In order to select patient records in MED, you do *not* need to be connected to VistA and will *not* be prompted to enter your VistA signon credentials.                                                                                                                          |

<span id="index" class="anchor"></span>Index

# A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access Error, 65

CPRS CHART – Library Not Registered Error, 66

Accessibility, 59

Action Menu Commands, 61

Adobe Website, xx

Appendix A—Keyboard Shortcuts for Common MED Commands, 59

Appendix B—Troubleshooting, 62

Appendix C—Mobile Electronic Documentation (MED) Frequently Asked Questions (FAQ), 74

Application Context Error, 65

Assumptions about the Reader, xix

# C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Callout Boxes, xvii

Commands

Action Menu, 61

Edit Menu, 60

File Menu, 59

Help Menu, 61

Keyboard Shortcuts, 59

Navigation, 59

Tools Menu, 60

View Menu, 60

Common MED Commands

Keyboard Shortcuts, 59

Contents, x

CPRS, 53

Importing Notes, 51

CPRS CHART – Library Not Registered Error, 66

CPRS Error, 71

Create a Note, 46

Creating Notes, 46

# D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database, 27

MED Database Compact Messages, 68

MED Database Open Error, 67

Dates

Progress Notes, 55

Desktop Shortcut, 22

Disclaimers, xvi

Document Title, 45

Documentation Conventions, xvii

Documentation Navigation, xviii

# E

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit Existing Notes, 48

Edit Menu Commands, 60

Editing Notes, 46

Errors, 62

Application Context, 65

CPRS, 71

CPRS CHART – Library Not Registered Error, 66

Invalid Date, 72

Invalid Pointer Operation, 64

MED Database Open, 67

MED Missing Remote Procedure Calls (RPCs) in VistA, 63

Missing Required Data Fields, 73

Network Connection, 69

Patch TIU\*1\*257 is Not Current in VistA, 62

RPC Broker, 71

Section 508, 73

Write Access, 65

Existing Progress Notes, 51

# F

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figures, xii

File Menu Commands, 59

Finding Text in Notes, 49

Frequently Asked Questions (FAQ), 74

# G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Glossary, 76

GUI

Online Help, xix

# H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Health Summary, 23, 32, 33, 34, 35, 38, 74

Find, 36, 37

Tab

Overview, 34

Procedures, 36

Find Text, 37

Retrieve, 36

Help

Online, xix

Help Menu Commands, 61

History, Revisions to Documentation and Patches, ii

Home Pages

Adobe Website, xx

VHA Software Document Library (VDL)

Website, xx

VistA Development Website, xvi

How to

Obtain Technical Information Online, xviii

Use this Manual, xv

# I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Icons on the Notes Tab, 44

Import Criteria for Progress Notes, 55

Importing

MED Notes into CPRS, 51

Intended Audience, xvi

Introduction, 21

Invalid Date Error, 72

Invalid Pointer Operation Error, 64

# K

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Keyboard Shortcuts

Common MED Commands, 59

# L

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Launching MED, 22

Legal Requirements, xvi

Library Not Registered Error

CPRS CHART, 66

# M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MED

Desktop Shortcut, 22

Introduction, 21

Notes Tab, 44

Printing, 32

Progress Notes Date Sensitivity, 55

Retrieving Patient Records, 23

Scratch Pad Tab, 40

Selecting a Patient, 29

Starting, 22

Tabs

Summary, 34

MED Database Compact Messages, 68

MED Database Open Error, 67

MED Missing Remote Procedure Calls (RPCs) in VistA Error, 63

Missing Required Data Fields Error, 73

Mobile Electronic Documentation option, 23, 71

# N

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Navigation Commands, 59

Network Connection Error, 69

New Progress Notes, 53

Notes, 60

Creating, 46

Edit Existing, 48

Editing, 46

Finding Text, 49

Icons, 44

Importing, 51

Viewing, 45

Notes Tab, 44

# O

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Obtaining

Data Dictionary Listings, xix

Technical Information Online, How to, xviii

Online

Help, xix

Options

Mobile Electronic Documentation option, 23, 71

TIU MED GUI RPC V2, 23, 71

TIU MED GUI RPC V2, 71

Orientation, xv

Overview

Health Summary

Tab, 34

Printing Health Summaries and Notes, 32

Retrieving Patient Records, 23

Scratch Pad Tab, 40

# P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch TIU\*1\*257 is Not Current in VistA Error, 62

Patient Information Available from Any Tab, 31

Patient Records

Retrieving, 23

Patient Selection, 24, 27

Patients

Selecting, 29

Permissions Error, 65

CPRS CHART – Library Not Registered, 66

Printing

Within MED, 32

Printing Health Summaries and Notes

Overview, 32

Procedures, 32

Procedures

Health Summary

Tab, 36

Find Text, 37

Retrieve, 36

Printing Health Summaries and Notes, 32

Retrieving Patient Records, 23

Scratch Pad Tab, 41

Delete Text, 42

Find Text, 41

Write Text, 41

Progress Note, 54

Progress Notes

Existing, 51

Import Criteria, 55

Importing into CPRS, 51

New, 53

PS Anonymous Directories, xx

# R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reader, Assumptions about the, xix

Reference Materials, xx

Requirements

Legal, xvi

Retrieve Patient(s), 24

Retrieving Patient Records, 23

Overview, 23

Procedures, 23

Revision History, ii

RPC Broker Error, 71

# S

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Scratch Pad Tab, 40

Overview, 40

Procedures, 41

Delete Text, 42

Find Text, 41

Write Text, 41

Security Keys, 56

TIU MED MANUAL OVERRIDE, 56

TIU MED MANUAL PATIENT, 56

Selecting a Patient, 29

Starting MED, 22

Summary

Tab, 34

# T

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table of Contents, x

Tables, xiv

Tabs

Notes, 44

Patient Information Available from Any Tab, 31

Scratch Pad, 40

Summary, 34

Template, 46, 54

TIU MED GUI RPC V2 Option, 23, 71

TIU MED GUI RPC V2 Option, 71

TIU MED MANUAL OVERRIDE Security Key, 56

TIU MED MANUAL PATIENT Security Key, 56

Tools Menu Commands, 60

Troubleshooting, 62

# U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

URLs

Adobe Website, xx

VHA Software Document Library (VDL)

Website, xx

VistA Development

Website, xvi

# V

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHA Software Document Library (VDL)

Website, xx

View Menu Commands, 60

Viewing Notes, 45

# W

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Warnings

MED Database Compact, 68

Web Pages

Adobe Website, xx

VHA Software Document Library (VDL)

Website, xx

VistA Development Website, xvi

Write Access Error, 65