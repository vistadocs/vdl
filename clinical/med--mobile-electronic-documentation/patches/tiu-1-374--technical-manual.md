---
title: TIU*1*374 Mobile Electronic Documentation (MED) Technical Manual
doc_type: TM
doc_label: Technical Manual
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
menu_options: 2
description: 
audience: 
keywords: 
  - table
  - error
  - contents
  - patient
  - span
  - documentation
  - strong
  - class
  - templates
  - mobile
page_count: 0
word_count: 11379
section_count: 23
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mobile_Electronic_Documentation/TIU_MED_TM.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mobile_Electronic_Documentation/TIU_MED_TM.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=190"
---

Mobile Electronic Documentation (MED)Technical Manual

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/001.png)

December 2025Department of Veterans AffairsOffice of Information and Technology (OIT)

<span id="_Toc298228216" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref300639470" class="anchor"></span>Table 1. MED—Security keys required for manually entered patients in MED</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 47%" />
<col style="width: 27%" />
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
<td>2.9</td>
<td><p>Patch TIU*1.0*374</p>
<p>Removed <a href="#removed_not_rpc">non-RPCs</a> from Remote Procedure Calls (RPCs):</p>
<ul>
<li><p>TIU MED GUI RPC V2</p></li>
<li><p>TIU MED GUI VERSION</p></li>
</ul>
<p>Added missing V2 to TIU MED GUI RPC in sections <a href="#added_v2_1">RPC Broker Error</a></p>
<p>Updated document format and made 508 compliant</p></td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>06/02/2017</td>
<td>2.8</td>
<td><p>Update for Patch TIU*1*311</p>
<p>Two-Factor Authentication (2FA)</p>
<p>Updated all MED document file references to the following:</p>
<ul>
<li><p>TIU_1_311_MED_IG.doc/pdf</p></li>
<li><p>TIU_MED_TM.doc/pdf</p></li>
<li><p>TIU_MED_UM.doc/pdf</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/21/2011</td>
<td>2.7</td>
<td><p>Tech review and edit updates based on review/feedback from <mark>REDACTED</mark> review:</p>
<ul>
<li><p>Updated all MED document file references to the following:</p></li>
</ul>
<ul>
<li><p>TIU_1_262_MED_IG.doc/pdf</p></li>
<li><p>TIU_1_262_MED_TM.doc/pdf</p></li>
<li><p>TIU_1_262_MED_UM.doc/pdf</p></li>
</ul>
<ul>
<li><p>Updated all footers to reference MED GUI Software Version 2.3 and documentation Patch TIU*1.0*262.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/15/2011</td>
<td>2.6</td>
<td><p>Tech review and edit updates based on review/feedback from <mark>REDACTED</mark> review:</p>
<ul>
<li><p>Updated first bullet in Step 3 in Section 2.1.3. Changed "deploring" to "deploying."</p></li>
<li><p>Updated note in Step 3d in Section 2.1.3. Changed "need" to "needed."</p></li>
<li><p>Added the following sentence to blank pages added so all chapter/document ends on an even page for double-sided printing:</p></li>
</ul>
<p>"This page intentionally left blank for double-sided printing."</p>
<ul>
<li><p>Updated first bullet in Section 2.5.1.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/05/2011</td>
<td>2.5</td>
<td><p>Tech review and edit updates based on review/feedback from MED Core team:</p>
<ul>
<li><p>Updated the following sections to indicate users <em>must</em> be given <strong>Full Control</strong> access permission to the MED directory (i.e., Read, Write, Modify, and Execute), as per <mark>REDACTED</mark></p></li>
</ul>
<ul>
<li><p>Section 2.1.1, "Create a Network Share Download Directory."</p></li>
<li><p>Section 2.1.3, "Configure Client Workstation."</p></li>
<li><p>"Write Access Error" error description and resolution to state.</p></li>
</ul>
<ul>
<li><p>Added a Note informing users to enter a Remedy ticket if the resolutions listed in the errors described in Chapter 4, "Troubleshooting—Error Messages," do not resolve the issue.</p></li>
<li><p>Added the "CPRS CHART – Library Not Registered Error" error message to Chapter 4, "Troubleshooting—Error Messages," as per feedback from R Hines.</p></li>
<li><p>Updated index entries for error messages in Chapter 4, "Troubleshooting—Error Messages."</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/11/2011</td>
<td>2.4</td>
<td><p>Tech review and edit updates based on review/feedback from MED Core team:</p>
<ul>
<li><p>Removed patch compliance dates from the "<a href="#_Toc336755501">How to Use this Manual</a>", as per <mark>REDACTED</mark></p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/10/2011</td>
<td>2.3</td>
<td><p>Tech review and edit updates based on review/feedback from MED Core team:</p>
<ul>
<li><p>Added Note to the Description field for the TIU MED MANUAL PATIENT security key in Table 1 and Table 7, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Renamed section to the "MED Software Summary Setup Procedures" section as per <mark>REDACTED</mark> review.</p></li>
<li><p>Updated responsible parties for obtaining and exporting templates in the "Create a Network Share Download Directory" section, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Added a Note regarding compacting the MED database in Step 3o in the "Configure Client Workstation" section, as per <mark>REDACTED</mark> reviews.</p></li>
<li><p>Added a Note regarding Hyperlinks in TIU templates in the "Guidelines for Creating Section 508 Compliant TIU Templates" section, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Added a Note and updated Step 3 regarding deleting templates on Network Share Templates directory rather than the laptop/client workstations to the "Deleting Templates" section as per <mark>REDACTED</mark> review.</p></li>
<li><p>Added Cautionary Note to the procedures in the "Delete Manually Entered Patients (Duplicates)" section, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Updated patient names in Table 2 through Table 5, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Added a Note and Reference to Step 2 in the "Create a Network Share Download Directory" section.</p></li>
<li><p>Updated the image and directory path for the MED database reference in the "MED Database Open Error" section.</p></li>
<li><p>Added compact database messages to the new "MED Database Compact Messages" section, as per Seth Thompson email.</p></li>
<li><p>Added definitions for Retrieving Patient Records vs. Selecting Patient Records in MED in the "<a href="#_Toc294679256">Glossary</a>" sections, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Removed author references, other than Project Manager and Tech Writer, from "Revision History" section, as per Product Support review.</p></li>
<li><p>Removed "HBPC" and "Product Support" from "<a href="#intended_audience">Intended Audience</a>" section, as per Product Support review.</p></li>
<li><p>Added reference to Microsoft Access database in the "<a href="#assumptions_about_the_reader">Assumptions about the Reader</a>" section, as per Product Support review.</p></li>
<li><p>Added phrase "to the network share directory" to Step 3c in the "Create a Network Share Download Directory" section, as per Product Support review.<br />
<br />
Also, updated last Note in this section to specify those users maintaining the network share Templates folder, as per Product Support review.</p></li>
<li><p>Corrected sample IP and port information in the "Configure Client Workstation" section, as per Product Support review.</p></li>
<li><p>Corrected option name and removed security key from the "Health Summary Parameter Delete Option [TIU MED DEL PARM]" section, as per Product Support review.</p></li>
<li><p>Updated references to the installer in the "Verify and Prepare MED Templates for Use with CPRS" section, as per Product Support review.</p></li>
<li><p>Updated procedures in the "Delete Manually Entered Patients (Duplicates)" section, as per Product Support review.</p></li>
<li><p>Removed lock from the TIU MED DEL PARM option in Table 6, as per Product Support review.</p></li>
<li><p>Corrected option name in the "RPC Broker Error" section, as per Product Support review.</p></li>
<li><p>Added the GUI version 2.3 to the Resolution in the "Invalid Date Error" section, as per Product Support review.</p></li>
<li><p>Updated the Note contact information in Step 3d in the "Configure Client Workstation" section, as per Product Support review.</p></li>
<li><p>Updated the Note in Step 2 in the "Configure Client Workstation" section, as per Product Support review.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/27/2011</td>
<td>2.2</td>
<td><p>Tech review and edit updates based on review/feedback from Product Support team:</p>
<ul>
<li><p>Added all Mobile Electronic Device (MED) VistA patch references and Graphical User Interface (GUI) client software version to the Title page.</p></li>
<li><p>Added the "<a href="#_Toc18284794">Orientation</a>" section in accordance with national documentation standards. Moved topics from the "Introduction" section into this new section.</p></li>
<li><p>Renamed the "Reference Materials" section. Also added patch descriptive text.</p></li>
<li><p>Moved and renamed the "Create a Network Share Download Directory" section prior to MED client workstation configuration steps.</p></li>
<li><p>Added the "Deleting Templates" section; extracted from the User Manual.</p></li>
<li><p>Added the "Delete Manually Entered Patients (Duplicates)" section under the "Progress Notes Import Criteria" section to include instructions on how to manually delete patients from the MED database.</p></li>
<li><p>Updated the "Configure Client Workstation" section:</p></li>
</ul>
<ul>
<li><p>Deleted information on setting the MED.exe program file properties in Step 1 to just reference the desktop shortcut properties.</p></li>
<li><p>Added procedures to set permission for the Mobile Electronic Documentation folder in Step 2.</p></li>
<li><p>Added Step 3 procedures to configure the MED default "Template Update Path".</p></li>
</ul>
<ul>
<li><p>Added the "Write Access Error" error message section in the "Troubleshooting—Error Messages" section.</p></li>
<li><p>Updated the summary steps in the "Create a Network Share Download Directory" section.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/12/2011</td>
<td>2.1</td>
<td><p>Tech review and updates:</p>
<ul>
<li><p>Deleted patch references to and figure for "Error Message: Packing a reminder dialog" in the "Introduction" section, as per Jeanie Scott review.</p></li>
<li><p>Updated the "Implementation and Maintenance" section. Consolidated configuration information, as per Jeanie Scott review.</p></li>
<li><p>Updated the "Manage Mobile Electronic Documentation Option [TIU MED MANAGEMENT]" section, as per Jeanie Scott review.</p></li>
<li><p>Updated the "Health Summary Parameter Delete Option [TIU MED DEL PARM]" section, as per Jeanie Scott review.</p></li>
<li><p>Updated the "Date Sensitivity" section in the "Progress Notes Import Criteria" topic, as per Jeanie Scott review.</p></li>
<li><p>Updated Table 6. MED exported options, as per Jeanie Scott review.</p></li>
</ul></td>
<td><p>Project Manager—Tim Landy</p>
<p>Tech Writer—Thom Blom</p></td>
</tr>
<tr class="even">
<td>06/23/2011</td>
<td>2.0</td>
<td><p>Tech review and updates:</p>
<ul>
<li><p>Renamed document to remove patch reference ID.</p></li>
<li><p>Reformatted document to follow current national documentation standards and style guides.</p></li>
<li><p>Added alternate text to all images for Section 508 compliance.</p></li>
<li><p>Updated the "Introduction" section to be consistent across the MED documentation set.</p></li>
<li><p>Updated Index entries.</p></li>
<li><p>Removed the "Install MED" section from the "Implementation and Maintenance" section, since the procedures listed are duplicated in, the <em>MED Installation Guide</em>.</p></li>
<li><p>Remedy Ticket #485510: Added the "Date Sensitivity" section in the "Progress Notes Import Criteria" section.</p></li>
<li><p>Remedy Tickets #487029 and 491510: Kept prefix as "<strong>ScratchPad_</strong>" in the <em>MED Technical Manual</em>. Updated <em>MED Installation Guide</em> to match.</p></li>
<li><p>Made grammar, punctuation, and spelling updates as needed.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01/21/2011</td>
<td>1.1</td>
<td><p>Tech review and updates:</p>
<ul>
<li><p>Page 12: Updated screen capture with new version numbers.</p></li>
<li><p>Page 15: Added new RPC. Added a Note about option TIU MED GUI RPC V2 replacing TIU MED GUI RPC.</p></li>
<li><p>Page 17: Added error messages.</p></li>
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

<span id="_Ref300639470" class="anchor"></span>Table 1. MED—Security keys required for manually entered patients in MED

Contents

<span id="_Toc394379186" class="anchor"></span>

Figures and Tables

Figures

Tables

<span id="_Toc18284794" class="anchor"></span>Orientation

<span id="_Toc336755501" class="anchor"></span>How to Use this Manual

The Mobile Electronic Documentation (MED) application consists of both a Veterans Health Information Systems and Technology Architecture (VistA) M Server component and a Microsoft® Windows laptop/client workstation Graphical User Interface (GUI) component:

- Original VistA M Server Patch: TIU\*1.0\*244 (released date: 06/03/2010).
- Updated VistA M Server Patch: TIU\*1.0\*257 (released date: 01/21/2011).
- Documentation-only VistA M Server Patch TIU\*1.0\*311.
- Current Laptop/Client Workstation software: MED.exe Version 2.3.311.6.

This manual provides technical information regarding the implementation and maintenance of the MED VistA M Server and Microsoft® Windows laptop/client workstation components.

MED works in tandem with CPRS; however, this manual does *not* attempt to fully document how to create templates or describe other functions of CPRS.

REF: For installation instructions; lists of routines, files, and options; additional technical information; and user information on CPRS, see the CPRS documentation on the VA Document Library (VDL) at the following link:

<http://www.va.gov/vdl/application.asp?appid=61>

<span id="intended_audience" class="anchor"></span>Intended Audience

The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Information Resource Management (IRM)
- Clinical Application Coordinators (CAC)

Legal Requirements

There are no special legal requirements involved in the use of MED software.

Disclaimers

This manual provides an overall explanation of how to configure the MED software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Web sites on the Internet and VA Intranet for a general orientation to VistA. For example, visit the Office of Information & Technology (OIT) VistA Development VA Intranet Website:

<span class="mark">REDACTED</span>

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

  NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.
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

> **NOTE:** Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic.

REF: See the *Mobile Electronic Documentation (MED) Technical Manual* for further information.

Online Help

VistA M-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M-based software.

The MED laptop/client workstation software includes an MED GUI online help file (i.e., MED.chm). Instructions, procedures, and other information are available from the. To access the online help do either of the following:

- Inside MED, click on the Help \| Contents menu options from the MED GUI toolbar or press the F1 key while you have any MED dialogue screen open.
- Outside MED, double-click on the MED.chm file.

Obtaining Data Dictionary Listings

Technical information about VistA M-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

REF: For details about obtaining data dictionaries and about the formats available, see the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*.

<span id="assumptions_about_the_reader" class="anchor"></span>Assumptions about the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- Microsoft® Windows, including Microsoft Access database.
- M programming language

Reference Materials

Readers who wish to learn more about MED should consult the following:

- *Mobile Electronic Documentation (MED) Installation Guide (TIU\*1.0\*311)*—Contains instructions for installing, configuring, and deploying MED on the VistA M Server and Laptop/Client Workstation.
- *Mobile Electronic Documentation (MED) User Manual*—Contains instructions on how to use the MED software.
- *FORUM Patches: TIU\*1.0\*244, TIU\*1.0\*257, and TIU\*1.0\*262.*

VistA documentation is made available online in Microsoft® Word format and Adobe® Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe® Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe® Systems Incorporated at the following Website:

<http://www.adobe.com/>

VistA documentation can be downloaded from the VHA Software Document Library (VDL) Website:

<http://www4.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Product Support (PS) anonymous directories:

- Preferred Method <span class="mark">REDACTED</span>

  NOTE: This method transmits the files from the first available FTP server.

<span class="mark">REDACTED</span>

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [MED Software Summary Setup Procedures](#med-software-summary-setup-procedures)
    - [Create a Network Share Download Directory](#create-a-network-share-download-directory)
    - [Configure VistA M Server](#configure-vista-m-server)
    - [Configure Client Workstation](#configure-client-workstation)
  - [Manage Mobile Electronic Documentation Option \[TIU MED MANAGEMENT\]](#manage-mobile-electronic-documentation-option-tiu-med-management)
  - [Health Summary Parameter Delete Option \[TIU MED DEL PARM\]](#health-summary-parameter-delete-option-tiu-med-del-parm)
  - [Verify and Prepare MED Templates for Use with CPRS](#verify-and-prepare-med-templates-for-use-with-cprs)
    - [Guidelines for Creating Section 508 Compliant TIU Templates](#guidelines-for-creating-section-508-compliant-tiu-templates)
    - [Deleting Templates](#deleting-templates)
  - [Progress Notes Import Criteria](#progress-notes-import-criteria)
    - [Date Sensitivity](#date-sensitivity)
    - [Delete Manually Entered Patients (Duplicates)](#delete-manually-entered-patients-duplicates)
    - [Security Keys](#security-keys)
    - [Import Examples](#import-examples)
- [Routines, Options, Security Keys, and Remote Procedure Calls](#routines-options-security-keys-and-remote-procedure-calls)
  - [Routines](#routines)
  - [Options](#options)
  - [Security Keys](#security-keys-1)
  - [Remote Procedure Calls (RPCs)](#remote-procedure-calls-rpcs)
- [Troubleshooting—Error Messages](#troubleshootingerror-messages)
  - [Not Current Patch in VistA Error](#not-current-patch-in-vista-error)
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
  CAUTION: This version of MED does *not* encrypt data. All laptops/client workstations (PC) are required to have full disk encryption and VA security policies. PCs should have normal health checks including security updates and antivirus.Please be aware that if a PC is assigned to multiple users, MED notes and health summaries include patient information that is viewable to all users of the PC. Therefore, all users of the PC *must* have the same level of security access to view this information.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## MED Software Summary Setup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Create a Network Share Download Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a network share directory to store distribution files and include templates with MED, perform the following procedures:

1.  The Information Resource Management (IRM) network staff needs to create a network share download directory (e.g., \\VHA...\TIU MED).
2.  The IRM network staff downloads and unzips the MED distribution file into network share download directory to obtain the MOBILEELECTRONICDOCUMENTATION_TIU-1-311.MSI installer.

> NOTE: The MOBILEELECTRONICDOCUMENTATION_TIU-1-311.MSI installer runs standalone and installs the MED software on a laptop/client workstation.

REF: For MED installation instructions on the laptop/client workstation, see the *Mobile Electronic Documentation (MED) Installation Guide (TIU\*1.0\*311)*.

3.  The Clinical Applications Coordinator (CAC) obtains the TIU templates (.txml files) that will be used in MED from the POC for MED. The CAC includes those TIU templates that are found on the Computerized Patient Record System (CPRS) Notes Tab to be associated with the MED installation:
1.  The IRM network staff creates a sub-folder called "Templates" under the network share download directory in Step 1:

\\VHA...\TIU MED\\Templates

- The person setting the template path *must* be assigned the Mobile Electronic Documentation secondary option \[TIU MED GUI RPC V2\].
- All Clinical Application Coordinators (CAC) need Full Control access permission (i.e., Read, Write, Modify, and Execute) to this folder.
- All non-CAC users need Read-only access permission to this folder.
1.  (Optional) Create sub-folders for different provider types (e.g., Dietitian, Nurse, and Pharmacist) to store discipline-specific templates. You will need to know the names of individual personnel and their discipline as well as the laptops/client workstations they will be using.

<span id="_Toc205539410" class="anchor"></span>Figure 1. Sample MED templates directory with sample provider sub-directories

> ![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/002.png)

2.  The CAC (with Full Control access permission to the network share directory) exports any TIU templates, with the exception of Reminder Dialogs, through the CPRS Template Editor into the Templates folder on the network share directory.

    NOTE: Reminder Dialogs *cannot* be used within the MED application. In addition, you can use patient data objects in any template, but the data will *not* populate until the template is imported into CPRS.
3.  Add a "ScratchPad\_" prefix (be sure to include the underscore) to the name of any TIU templates that are to be used as Scratch Pad templates in MED (e.g., ScratchPad\_*NAMEOFTEMPLATE*.txml).

    NOTE: Users who will import, delete, and maintain templates on the network share server *must* have Full Control access permission to the Templates folder.

### Configure VistA M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To configure the MED VistA M Server software on the VistA M Server, perform the following procedures:

1.  Verify the Mobile Electronic Documentation folder and the Import M.E.D. Notes template were installed in the TIU TEMPLATE file (#8927) as part of Computerized Patient Record System (CPRS) (see Section 2.4).

    CAUTION: If the Mobile Electronic Documentation folder and the Import M.E.D. Notes template are *not* installed in CPRS, <u>STOP</u>! Have your Clinical Application Coordinator (CAC) enter a National Remedy ticket to Text Integrated Utilities (TIU) for assistance!
2.  Assign the TIU MED MGT security key to IRM/CAC staff, if not already assigned.

    REF: For more information on this security key, see Table 7.
3.  Assign the following secondary options to the IRM/CAC staff so they can set, modify, and delete MED parameters:
- MANAGE MOBILE ELECTRONIC DOCUMENTATION option \[TIU MED MANAGEMENT\].
- HEALTH SUMMARY PARAMETER DELETE option \[TIU MED DEL PARM\].

  REF: For more information on these options, see Table 6.
4.  Assign the following security keys to those individuals who will be tasked with validating patient identification for manually entered MED patients (e.g., CAC and Home Based Primary Care \[HBPC\] super users):
- TIU MED MANUAL PATIENT.
- TIU MED MANUAL OVERRIDE.

  CAUTION: Only a select few users should be given the TIU MED MANUAL OVERRIDE security key. Most users should not be given this key.It is suggested that there be a document review and patient review before importing notes into patient records that have typographical or missing data that stops a user from importing the information as outlined with the TIU MED MANUAL PATIENT security key.

> REF: For more information on these security key, see Table 7.

5.  Assign the Mobile Electronic Documentation secondary option \[TIU MED GUI RPC V2\] to HBPC users.

REF: For more information on this option, see Table 6.

6.  Set/Delete the Health Summary Type for MED parameter \[TIU MED HSTYPE\] to generate Health Summaries in MED
- Use the MANAGE MOBILE ELECTRONIC DOCUMENTATION option \[TIU MED MANAGEMENT\] to set the TIU MED HSTYPE parameter (see Section 2.2).
- Use the HEALTH SUMMARY PARAMETER DELETE option \[TIU MED DEL PARM\] to delete the TIU MED HSTYPE parameter (see Section 2.3).

  REF: For detailed installation instructions, see the *Mobile Electronic Documentation (MED) Installation Guide* (i.e., TIU_1_311_MED_IG.pdf).

### Configure Client Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To configure the MED software on the Microsoft® laptop/client workstation (PC), perform the following procedures:

1.  Update the "Launch MED" desktop shortcut with your site IP and RPC Broker port as follows:
1.  Right-click on the MED launch icon on the desktop.
4.  Select the Properties menu.
5.  Select the Shortcut tab.
6.  In the target field append the IP address or Domain Name Service (DNS) and port information after the MED.exe location. For example:

"C:\Program Files\Mobile Electronic Documentation\MED.exe" <span class="mark">REDACTED</span>

Set Permission for the Mobile Electronic Documentation folder.

On the HBPC laptop/client workstation, do the following:

1.  Navigate to the following directory:

C:\Program Files\Mobile Electronic Documentation

2.  Right click on the Mobile Electronic Documentation folder.
7.  Select Properties.
8.  Select the group or user name in the upper portion of the Properties dialogue.
9.  Check the Write checkbox under the Allow column in the lower portion of the Properties dialogue.
10. Press OK.

    NOTE: In order for users to write the appropriate information while using the MED software, they *must* have Full Control access permission to this folder; otherwise, they will get access violation errors when launching MED.
2.  Configure the following MED settings on the client workstation (procedures follow):
- MED default "Template Update Path"—Indicate here MED should search for updated templates. Before deploying the HBPC laptop/client workstation to the user, the IRM or CAC *must* retrieve and select a patient in MED on each laptop/client workstation and add the network Templates path so the templates will be available for use in MED.
- Health Summaries—Set Health Summaries to automatically download for patients (see also Step 6 in Section 2.1.2).
- Database Settings—Indicate when MED should suggest compacting its database.
1.  Launch MED. Select a patient to make the MED menu options visible on the Patient Selection form.
2.  Click Retrieve Patient(s).
3.  Click Select a Patient.
4.  Sign onto VistA: Enter your signon credentials.

> **NOTE:** If you are not prompted for signon credentials, contact IRM to verify that the correct IP address and port number have been assigned to the MED shortcut executable target line. <span class="mark">REDACTED</span>.

5.  Select a patient to retrieve form the list.
6.  Click Retrieve Patient.
7.  Once the patient is retrieved, click Close.
8.  The MED Patient Select window is displayed; select the patient name again and click OK.
9.  Select the Tools menu and then select the Settings option, as shown below:

> <span id="_Toc299468386" class="anchor"></span>Figure 2. MED—Settings menu option

> ![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/003.png)

10. In the Users & Settings dialogue, if not already selected, click on the Data & Files tab.
11. Enter the following directory path (created in Step 3a in Section 2.1.1) in the "Template Update Path" field (Figure 3):

\\VHA...\TIU MED\Templates

12. Verify that the Retrieve Health Summaries checkbox is checked, as shown below:

> <span id="_Ref299466726" class="anchor"></span>Figure 3. MED Users & Settings dialogue—Data & Files

> ![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/004.png)

> NOTE: Unchecking the Retrieve Health Summaries checkbox makes updating the patient list faster; however, patient health summary information (e.g., Active Medications, Labs, etc.) will *not* be available to staff when using MED.

These templates will become available for the user of that laptop/client workstation after MED is closed and re-opened. MED checks the "Template Update Path" folder on startup and updates templates if applicable. If the template updates folder is inaccessible either due to connectivity (i.e., not connected to the VA Network to access the folder) or security (i.e., do not have Read permissions to the template updates folder), MED proceeds with the current templates in its local directory and template updates will be made at a later date when connectivity and security issues are resolved.

13. In the Users & Settings dialogue, select the Database tab, as shown below:

> <span id="_Toc205539413" class="anchor"></span>Figure 4. MED—Database tab: Setting the Suggest Compact After (MB) and Suggest Compact fields

> ![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/005.png)

14. In the Suggest Compact check box, check or uncheck whether MED should suggest compacting the database to the user. If this is checked, then suggesting a compact occurs when MED is started, and the database size exceeds what is entered in the Suggest Compact After (MB) field.
15. In the Suggest Compact After (MB) text box, enter the size in Megabytes that MED should suggest a database compact. (This option only applies if Suggest Compact is checked.)  
    >   
    > When the MED database meets or exceeds this size, MED automatically prompts the user to compact the database. Currently, it is suggested the user answer No to compact the database when prompted.

> NOTE: Compacting the MED Microsoft® Access database allows for maximum efficiency and increased speeds. However, based on the current default setting of 1024 MB and the fact that notes are purged after 7 days, it is unlikely that users will often be prompted to compact the MED database.

> Future versions of the software will be increasing this default value and correct some underlying code issues.

REF: For sample warning and information message related to compacting the MED database, see Section 4.8.

16. Click Close when done to save these changes.
3.  Verify and prepare MED templates for use with CPRS (see Section 2.4).

    REF: For detailed installation instructions, see the *Mobile Electronic Documentation (MED) Installation Guide* (i.e., TIU_1_311_MED_IG.pdf).

## Manage Mobile Electronic Documentation Option \[TIU MED MANAGEMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MANAGE MOBILE ELECTRONIC DOCUMENTATION option \[TIU MED MANAGEMENT\] allows IRM/CAC staff to set or modify the Health Summary Type for MED parameter \[TIU MED HSTYPE\].

The TIU MED HSTYPE is used to generate Health Summaries in MED. The site needs to identify an existing Health Summary or create a new Health Summary that will be used with the MED software.

To set the TIU MED HSTYPE parameter, the IRM/CAC staff needs to perform the following procedures:

1.  Select the MANAGE MOBILE ELECTRONIC DOCUMENTATION option \[TIU MED MANAGEMENT\].

    NOTE: To use this option, users *must* be assigned the TIU MED MGT security key.
2.  At the "Enter Selection" prompt, select one of the following options:
- 1—User \[choose from NEW PERSON\].  
    
  At the "Please Select USER" prompt enter a user name in the NEW PERSON file (#200).
- 2—Service \[choose from SERVICE/SECTION\].  
    
  At the "Please select a SERVICE" prompt enter the service in the SERVICE/SECTION file (#49).
- 3—Division \[choose from INSTITUTION\].  
    
  At the "Please select a DIVISION:" prompt, enter the institution in the INSTITUTION file (#4).
- 4—System \[XXXXXXXX.MED.VA.GOV\]  
    
  Choose from the local system (e.g., ANYWHERE.MED.VA.GOV).

<span id="_Toc205539414" class="anchor"></span>Figure 5. Manage Mobile Electronic Documentation option—Sample user dialogue

Select Clinical Informatics Main Menu Option: MANAGE MOBILE ELECTRONIC DOCUMENTATION

TIU MED HSTYPE may be set for the following:

1 User \[choose from NEW PERSON\]

2 Service \[choose from SERVICE/SECTION\]

3 Division \[choose from INSTITUTION\]

4 System \[ANYWHERE.MED.VA.GOV\]

Enter Selection: 4 \<Enter\> System

Enter a HS for SYSTEM \[ANYWHERE.MED.VA.GOV\]: HBPC MED//

## Health Summary Parameter Delete Option \[TIU MED DEL PARM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HEALTH SUMMARY PARAMETER DELETE option \[TIU MED DEL PARM\] allows IRM/CAC staff to delete the Health Summary Type for MED parameter \[TIU MED HSTYPE that had been previously set. Once deleted, MED uses the Health Summary designated at a higher level, such as at the system level.\].

> **NOTE:** Use the MANAGE MOBILE ELECTRONIC DOCUMENTATION option \[TIU MED MANAGEMENT\] to modify the currently set Health Summary type (see Section 2.2).

To delete the TIU MED HSTYPE parameter, the IRM/CAC staff needs to perform the following procedures:

1.  Select the HEALTH SUMMARY PARAMETER DELETE option \[TIU MED DEL PARM\].
2.  At the "Enter Selection" prompt, select one of the following options:
- 1—User \[choose from NEW PERSON\].  
    
  At the "Please Select USER" prompt enter a user name in the NEW PERSON file (#200).
- 2—Service \[choose from SERVICE/SECTION\].  
    
  At the "Please select a SERVICE" prompt enter the service in the SERVICE/SECTION file (#49).
- 3—Division \[choose from INSTITUTION\].  
    
  At the "Please select a DIVISION:" prompt, enter the institution in the INSTITUTION file (#4).
- 4—System \[XXXXXXXX.MED.VA.GOV\]  
    
  Choose from the local system (e.g., ANYWHERE.MED.VA.GOV).
3.  At the "Delete the Health Summary for \[XXXXXXXX\]?" prompt, enter YES.
4.  At the "Are you SURE? NO//" prompt, enter YES to confirm the deletion.

> <span id="_Toc205539415" class="anchor"></span>Figure 6. Health Summary Parameter Delete option—Sample user dialogue

Select Clinical Informatics Main Menu Option: HEALTH

Delete a Health Summary for the following:

1 User \[choose from NEW PERSON\]

2 Service \[choose from SERVICE/SECTION\]

3 Division \[choose from INSTITUTION\]

4 System \[ANYWHERE.MED.VA.GOV\]

Enter Selection: 1 \<Enter\> User

Please Select USER: MED, PATIENT ONE

Delete the Health Summary for \[MED, PATIENT ONE\]? YES

Are you SURE? NO// YES

## Verify and Prepare MED Templates for Use with CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After Patch TIU\*1\*244 was installed on the VistA M Server, the post-installation process should have done the following:

- Created the "Mobile Electronic Documentation" TIU template folder under the "Shared Templates" TYPE field (#.03) in the TIU TEMPLATE file (#8927), which store the TIU templates (.txml files) that are found on the CPRS Notes tab.
- Added the "Import M.E.D. Notes" TIU template. This template is used for importing the MED notes, in the following directory on the client workstation:

C:/Program Files/Mobile Electronic Documentation/Templates

- Added the MED NOTE IMPORT .COM object in the OE/RR COM OBJECTS file (#101.15).
- Added the TIU MED HSTYPE parameter in the PARAMETER DEFINITION NAME file (#8989.51).

The MOBILEELECTRONICDOCUMENTATION_TIU-1-311.MSI installer runs standalone and installs the MED software on a laptop/client workstation. MED copies all template files (.txml) from the network shared Templates folder into the laptop/client workstation's Templates folder. The templates are immediately available for use.

> **NOTE:** The .txml files are TIU templates that are found on the CPRS Notes tab through the Template Editor. You can export any TIU template through the Template Editor with the exception of Reminder Dialogs. Reminder Dialogs are *not* supported in MED.

You can use patient data objects in any template, but the data will *not* populate *until* the template is imported in CPRS.

Adding the prefix "ScratchPad\_" to the name of a TIU template allows the template to be used on the Scratch Pad of MED (e.g., ScratchPad\_*NAMEOFTEMPLATE*.txml). Due to space limitations on the Scratch Pad tab of MED, you can only add a few Scratch Pad templates.

The Clinical Application Coordinator (CAC) *must* verify that the Mobile Electronic Documentation template folder and the Import M.E.D. Notes template were installed in the TIU TEMPLATE file (#8927) as part of CPRS.

To verify the existence of the folder and template, perform the following procedures:

1.  Open the Computerized Patient Record System (CPRS) application.
2.  Select the Notes tab.
3.  Click the Templates button.
4.  Expand the Shared Templates folder.
5.  Verify that the Mobile Electronic Documentation folder and the Import M.E.D. Notes template exists, as shown below:

> <span id="_Toc297834996" class="anchor"></span>Figure 7. CPRS—Verifying the Mobile Electronic Documentation folder and the Import M.E.D. Notes template exists

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/006.png)

> **CAUTION:** If the Mobile Electronic Documentation folder and the Import M.E.D. Notes template are *not* installed in CPRS, <u>STOP</u>! Have your CAC enter a National Remedy ticket to Text Integrated Utilities (TIU) for assistance!

### Guidelines for Creating Section 508 Compliant TIU Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of guidelines to use when creating Section 508 compliant TIU templates for use in CPRS and MED. By following these guidelines, templates will work appropriately (e.g., when a visually impaired user is using a screen reader).

- The following Template Field Types can be used:
- Word Processing
- Edit Box
- Combo Box
- Check Box
- Radio Button
- Number
- Text
- The following Template Field Types should *not* be used:
- Button
- Hyperlink—Hyperlinks do *not* work in MED! Nor when an MED note is imported into CPRS.
- Date
- The Template Field can be designated to print on separate lines or designated as required in the set up.
- Defaults values should *not* be set for any Template Field, as the screen reader *cannot* interpret them correctly as a default choice.
- Do *not* use a field within a field in your template design as the screen reader *cannot* follow the secondary dialog box, as shown below:

> <span id="_Toc205539417" class="anchor"></span>Figure 8. CPRS Templates—Section 508 compliant: Do *not* use a field within a field

> ![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/007.png)

- The Screen Reader Stop Code and the Screen Reader Continue Code Template Fields exported with TIU should *not* be used, as shown below:

> <span id="_Toc205539418" class="anchor"></span>Figure 9. Templates—Section 508 compliant: Screen Reader Stop Code and Screen Reader Continue Code fields should not be used

> ![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/008.png)

### Deleting Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The local Clinical Application Coordinator (CAC) or IRM staff can delete templates for you.

To delete an MED template, perform the following procedures:

1.  Navigate to the Network Share Templates directory location from which you wish to delete the stored MED templates (See Section 2.1.1).

    NOTE: Delete templates from the Network Share Templates directory rather than from the local laptop/client workstation Templates directory.
2.  Locate and select the template you want to delete.
3.  Make the template inaccessible by changing the .txml extension on the template to .delete.

Changing the template name on the network location updates the Templates directory on the laptop/client workstation, as long as the directory path on the Data & Files tab in the Users & Settings dialogue points to that network location (see Section 2.1.1).

## Progress Notes Import Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Date Sensitivity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is important to note that when MED is started it checks progress notes dates and does the following:

- If the patient name on the list is *not* a manually entered patient, when MED is started, any notes that have been imported over 7 days prior are deleted. Then, any patients that are over 7 days old and do *not* have any pending or imported notes are deleted as well.
- Any patients that are currently on the user's patient list over 7 days old and that do not have any pending or imported notes are deleted as well.

  IMPORTANT: In order to avoid deletion of any progress notes or patient lists from MED and to get the latest Health Summary information, users should retrieve their patient lists every day!

### Delete Manually Entered Patients (Duplicates)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A duplicate patient record in the MED database (i.e., identical Last Name, First Name, SSN, and DOB) may occur when a provider manually enters a patient into MED while in the field, because he/she does not see that the VistA patient has already been retrieved into the MED patient list (i.e., MED Access database). If the provider enters a note to the VistA retrieved patient record and *not* the manually entered record, it will not get imported.

When importing a note for a duplicate patient, the MED import process first finds the manually entered patient. Since the note was not added to the manually entered patient, MED does not find a note for that patient. The only way to import the note for that patient is to delete the manually entered patient from the MED Microsoft® Access database.

Manually entered patients will *never* be automatically deleted. These patients can only be deleted from the patient list through the database.

To delete a manually added patient from the MED Microsoft® Access database/selection list:

> **CAUTION:** Contact the CAC or IRM to delete any records from the MED Microsoft® Access database!

1.  Navigate to the following directory on the laptop/client workstation:

C: Program Files/Mobile Electronic Documentation/db/

1.  Create a backup of the MED.mdb Microsoft® Access database.
2.  Double-click on the Microsoft® Access MED.mdb file.
3.  Under the "Tables" listing in the left pane, double-click on the Patients table.
4.  Select (click on) the row with the manually added patient that you want to delete.

    NOTE: Make sure that you position the cursor to the far left of the row, so that the entire row gets selected.
5.  Right-click to open the secondary popup menu.
6.  Select Delete Record.
7.  Close the database file by clicking the \[X\] button in the upper right area of the window.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have a progress note for a manually entered patient, you *must* hold one of the following MED security keys:

<table>
<caption><p><span id="_Ref300646307" class="anchor"></span>Table 2. Import Example—TIU MED MANUAL PATIENT security key</p></caption>
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
<td>TIU MED MANUAL PATIENT</td>
<td><p>This security key allows users to enter manual patient notes in MED. If you hold this security key, the following <em>must</em> match exactly:</p>
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
<td>TIU MED MANUAL OVERRIDE</td>
<td><p>This security key allows users to enter manual patient notes in MED. If you hold this security key, the full SSN <em>must</em> match exactly.</p>
<p>CAUTION: Only a select few users should be given the TIU MED MANUAL OVERRIDE security key. Most users should <em>not</em> be given this key.<br />
<br />
It is suggested that there be a document review and patient review before importing notes into patient records that have typographical or missing data that stops a user from importing the information as outlined with the TIU MED MANUAL PATIENT security key.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref300646307" class="anchor"></span>Table 2. Import Example—TIU MED MANUAL PATIENT security key

### Import Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For example, if you hold the TIU MED MANUAL PATIENT security key and have added a manually entered patient like the one shown below, you will be allowed to import.

<table>
<caption><p><span id="_Toc294679287" class="anchor"></span>Table 3. Import Example—TIU MED MANUAL OVERRIDE security key: Different names</p></caption>
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

<span id="_Toc294679287" class="anchor"></span>Table 3. Import Example—TIU MED MANUAL OVERRIDE security key: Different names

However, if you have added a manually entered patient like any of those shown below, you will *not* be allowed to import if you only have the TIU MED MANUAL PATIENT security key.

Holders of the TIU MED MANUAL OVERRIDE security key *can* import patients with different names:

<table>
<caption><p><span id="_Toc294679288" class="anchor"></span>Table 4. Import Example—TIU MED MANUAL OVERRIDE security key: Different DOB</p></caption>
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

<span id="_Toc294679288" class="anchor"></span>Table 4. Import Example—TIU MED MANUAL OVERRIDE security key: Different DOB

Holders of the TIU MED MANUAL OVERRIDE key *can* import patients with different DOBs:

<table>
<caption><p><span id="_Ref300646314" class="anchor"></span>Table 5. Import Example—Unable to import due to different SSNs</p></caption>
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

<span id="_Ref300646314" class="anchor"></span>Table 5. Import Example—Unable to import due to different SSNs

This record *cannot* be imported regardless of the security key a user holds, since the SSN does not match:

<table>
<caption><p><span id="_Ref297876448" class="anchor"></span>Table 6. MED exported options</p></caption>
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

<span id="_Ref297876448" class="anchor"></span>Table 6. MED exported options

# Routines, Options, Security Keys, and Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain a list of Routines for the Mobile Electronic Documentation (MED) application and what they do, go to the programmer prompt in the appropriate account, and do the following:

<span id="_Toc36014104" class="anchor"></span>Figure 10. Routines: Obtaining routine information for MED

Select Systems Manager Menu Option: PR \<Enter\> ogrammer Options

KIDS Kernel Installation & Distribution System ...

NTEG Build an 'NTEG' routine for a package

PG Programmer mode

Calculate and Show Checksum Values

Delete Unreferenced Options

Error Processing ...

Global Block Count

List Global

Map Pointer Relations

Number base changer

Routine Tools ...

Test an option not in your menu

Verifier Tools Menu ...

Select Programmer Options Option: ROUT \<Enter\> ine Tools

%Index of Routines

Check Routines on Other CPUs

Compare local/national checksums report

Compare routines on tape to disk

Compare two routines

Copy Packman Routines to VMS File (\*)

Delete Routines

First Line Routine Print

Flow Chart Entire Routine

Flow Chart from Entry Point

Group Routine Edit

Input routines

List Routines

Load/refresh checksum values into ROUTINE file

Modified Routine Menu ...

Output routines

Routine Edit

Routines by Patch Number

Variable changer

Version Number Update

Select Routine Tools Option: LIST \<Enter\> Routines

Routine Print:

Want to start each routine on a new page: Yes// \<Enter\>

Want line numbers: No// \<Enter\>

All Routines? No =\> No

Routine: TIU MED\*

Routine: \<Enter\>

nnnn routines

DEVICE: HOME//

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following VistA TIU options are exported with the MED software:

<table>
<caption><p><span id="_Ref297876491" class="anchor"></span>Table 7. MED exported security keys</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 32%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Text</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TIU MED MANAGEMENT</td>
<td>MANAGE MOBILE ELECTRONIC DOCUMENTATION</td>
<td><p>Use this option to select the desired Health Summary Report.</p>
<p>This option allows Information Resource Management (IRM)/Clinical Application Coordinator (CAC) staff to set or modify the parameter that is used to generate Health Summaries in MED. The site needs to identify an existing Health Summary or create a new Health Summary that is used with the MED software.</p>
<p><strong>NOTE:</strong> This option is locked with the TIU MED MGT security key.</p></td>
</tr>
<tr class="even">
<td>TIU MED DEL PARM</td>
<td>HEALTH SUMMARY PARAMETER DELETE</td>
<td>Use this option to delete Health Summaries that have been previously set.</td>
</tr>
<tr class="odd">
<td>TIU MED GUI RPC V2</td>
<td>Mobile Electronic Documentation</td>
<td><p>This option creates the desired context for the GUI application on the VistA server.</p>
<p><strong>NOTE:</strong> The TIU MED GUI RPC V2 option installed with Patch TIU*1.0*257 replaces the TIU MED GUI RPC option installed with Patch TIU*1.0*244.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref297876491" class="anchor"></span>Table 7. MED exported security keys

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following security keys are exported with the MED software:

<table>
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
<td>TIU MED MGT</td>
<td>This security key allows IRM/CAC staff access to TIU MED options.</td>
</tr>
<tr class="even">
<td>TIU MED MANUAL PATIENT</td>
<td><p>This security key allows users to enter manual patient notes in MED. If you hold this security key, the following <em>must</em> match exactly:</p>
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
<tr class="odd">
<td>TIU MED MANUAL OVERRIDE</td>
<td><p>This security key allows users to enter manual patient notes in MED. If you hold this security key, the full SSN <em>must</em> match exactly.</p>
<p>CAUTION: Only a select few users should be given the TIU MED MANUAL OVERRIDE security key. Most users should <em>not</em> be given this key.<br />
<br />
It is suggested that there be a document review and patient review before importing notes into patient records that have typographical or missing data that stops a user from importing the information as outlined with the TIU MED MANUAL PATIENT security key.</p></td>
</tr>
</tbody>
</table>

## Remote Procedure Calls (RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <span id="removed_not_rpc" class="anchor"></span>following Remote Procedure Calls (RPCs) are exported with the MED software:

- TIU MED GET HEALTH SUMMARY
- TIU MED GET LIST DATA
- TIU MED GET PATIENT DATA
- TIU MED GET PATIENT LISTS
- TIU MED GET VERSION
- TIU MED LAST5
- TIU MED LIST ALL
- TIU MED PATIENT MANAGEMENT

# Troubleshooting—Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the various errors and other messages you may encounter while using the Mobile Electronic Documentation (MED) application.

## Not Current Patch in VistA Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed when an older version of MED is installed or is the wrong KIDS version in VistA:

<span id="_Toc205539420" class="anchor"></span>Figure 11. MED Error—Patch TIU\*1\*257 is not current in VistA

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/009.png)

Description:

MED is not installed or an older version is installed on VistA.

Resolution:

Install/Reinstall the latest patch.

## MED Missing Remote Procedure Calls (RPCs) in VistA Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed when an older version of MED is installed in VistA:

<span id="_Toc205539421" class="anchor"></span>Figure 12. MED Error—Missing RPCs

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/010.png)

Description:

MED is not installed or an older version is installed on VistA and is missing remote procedure calls (RPCs).

Resolution:

Install/Reinstall the latest patch.

## Invalid Pointer Operation Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed if the MED VistA KIDS install is not correct:

<span id="_Toc205539422" class="anchor"></span>Figure 13. MED Error—Invalid pointer operation

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/011.png)

Description:

The MED application is missing all the remote procedure calls (RPCs).

Resolution:

Install/Reinstall the latest patch.

## Application Context Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed for MED application context errors:

<span id="_Toc205539423" class="anchor"></span>Figure 14. MED Error—Application context

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/012.png)

Description:

Application context is a menu requirement for using all Remote Procedure Call (RPC) Broker calls. Each application has its own application context. The MED application context is TIU MED GUI RPC V2.

Resolution:

The TIU MED GUI RPC V2 menu option needs to be assigned to all MED users, either on a common menu or one of the user's secondary menus.

## Write Access Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following access error may be displayed for MED application users who do *not* have the appropriate access permissions to the MED directory:

<span id="_Toc205539424" class="anchor"></span>Figure 15. MED Error—Write access permissions error

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

<span id="_Toc205539425" class="anchor"></span>Figure 16. MED Error—CPRS CHART – Library Not Registered Error

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

<span id="_Toc205539426" class="anchor"></span>Figure 17. MED Error—Database is not installed correctly

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/013.png)

Description:

The MED.mdb database should be in the following db subdirectory:

C:\Program Files\Mobile Electronic Documentation\db\MED.mdb

Resolution:

Install/Reinstall Patch TIU\*1.0\*257 (TIU\*1.0\*257.KID package).

## MED Database Compact Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Warning Message:

The following warning message will be displayed when compacting the MED Microsoft® Access database:

<span id="_Toc205539427" class="anchor"></span>Figure 18. MED Warning—Database closing

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/014.png)

After clicking YES, you should see the following message:

<span id="_Toc205539428" class="anchor"></span>Figure 19. MED Information Message—Database Compacted

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/015.png)

After pressing OK, MED closes.

Description:

When the MED database meets or exceeds this size in the Suggest Compact After (MB) field (default value is 1024 MB), MED automatically prompts the user to compact the database. Currently, it is suggested the user answer No to compact the database when prompted. If users choose to compact the database they will see a series of warning and action messages (see above).

The MED.mdb database should be in the following db subdirectory:

C:\Program Files\Mobile Electronic Documentation \db\MED.mdb

REF: For more information on compacting the MED database, see Step 3o in the "Configure Client Workstation" section in the *Mobile Electronic Documentation (MED) Technical Manual*.

Resolution:

Close and save all open notes *before* compacting the MED Microsoft® Access database.

## Network Connection Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following blank dialogues may be displayed if the MED RPC Broker fails to make a VistA connection:

<span id="_Toc205539429" class="anchor"></span>Figure 20. MED Error—Network Connection: Blank Retrieve Patient(s) dialogue (1 of 2)

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/016.png)

Or:

<span id="_Toc205539430" class="anchor"></span>Figure 21. MED Error—Network Connection: Blank Retrieve Patient(s) dialogue (2 of 2)

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/017.png)

Description:

There may be a very long pause after selecting Retrieve Patients, and then the Retrieve Patients dialogue is blank. MED is running but *not* connected to VistA.

Resolution:

Check the desktop shortcut. Verify that the IP server address and port number is correct. Also, check for a network connection error.

## RPC Broker Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message

You may see the following Remote Procedure Call (RPC) Broker error dialogue when starting MED:

<span id="_Toc298167198" class="anchor"></span>Figure 22. Errors—RPC Broker Error: Patient list retrieval error

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/018.png)

Description:

This means that the user has not been assigned the Mobile Electronic Documentation secondary option \[TIU MED GUI RPC <span id="added_v2_1" class="anchor"></span>V2\].

Resolution:

Contact the Information Resource Management (IRM) or Clinical Applications Coordinator (CAC) to gain access to the Mobile Electronic Documentation secondary option \[TIU MED GUI RPC V2\].

## CPRS Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message

You may see the following dialogue when trying to import notes into CPRS:

<span id="_Toc298167199" class="anchor"></span>Figure 23. Errors—CPRS - Patient Chart Error: Importing notes error message

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/019.png)

Description:

You may be trying to import MED notes on a computer that does not have MED installed. For example, MED is installed on the laptop/client workstation, but you are trying to import MED notes on another client workstation.

Resolution:

If MED is loaded on the laptop/client workstation, contact IRM for assistance to "re-register" the MEDImport.dll file and then restart CPRS.

## Invalid Date Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following error may be displayed during the patient import process:

<span id="_Toc205539433" class="anchor"></span>Figure 24. MED Error—Invalid date

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/020.png)

Description:

The Date of Birth (DOB) is in the wrong format in the MED database (MED.mdb). Click the OK button to retrieve more details.

Resolution:

Verify that the correct MED GUI Version is running on the laptop/client workstation. If it is the correct GUI, then the current patient information is from a prior version. To fix this, use the current MED GUI to retrieve the patient data and it will properly update the DOB in the MED database.

## Missing Required Data Fields Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message:

The following types of error messages may be displayed for missing data fields (highlighted):

<span id="_Toc205539434" class="anchor"></span>Figure 25. MED Error—Missing required data fields and Section 508 compliance: Active Caption Color

![](tiu-1-374-mobile-electronic-documentation-med-technical-manual/021.png)

Description:

Required fields in templates that are missing data will display a warning message, and the missing fields will be highlighted in blue. Just as in CPRS, the template *cannot* be completed and saved unless the required fields are completed. Unlike CPRS regular dialog templates, the missing fields will be obviously marked.

> **NOTE:** Prior versions of MED highlighted required missing data fields in yellow. To make MED Section 508 compliant, the color of the fields is now set to Active Caption Color.

REF: For more information on making templates Section 508 compliant, see the "Guidelines for Creating Section 508 Compliant TIU Templates" section in this manual.

Resolution:

Enter the missing required data fields.

Users can reset he highlight colors by changing the Microsoft® Windows theme.

<span id="_Toc294679256" class="anchor"></span>Glossary

|                            |                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPRS                       | Computerized Patient Record System, the VistA package (in both GUI and character-based formats) that provides access to most components of the patient chart.                                                                                                                                                                                                         |
| CAC                        | Clinical Applications Coordinator. The CAC is a person at a hospital or clinic assigned to coordinate the installation, maintenance and upgrading of CPRS and other VistA software programs for the end users.                                                                                                                                                        |
| HEALTH SUMMARY             | A VistA product that can be viewed through CPRS, Health Summaries are components of patient information extracted from other VistA applications.                                                                                                                                                                                                                      |
| HBPC                       | Home Based Primary Care.                                                                                                                                                                                                                                                                                                                                              |
| PROGRESS NOTES             | A component of TIU that can function as part of CPRS.                                                                                                                                                                                                                                                                                                                 |
| VISTA                      | Veterans Information Systems Technology Architecture.                                                                                                                                                                                                                                                                                                                 |
| MED                        | Mobile Electronic Documentation. Application that provides remote documentation and importing of notes into CPRS.                                                                                                                                                                                                                                                     |
| MED NOTES                  | Notes created from exported CPRS Templates that can then be re-imported into CPRS.                                                                                                                                                                                                                                                                                    |
| RETRIEVING PATIENT RECORDS | When you retrieve patient records in MED, you are obtaining updated patient data (e.g., Health Summaries) from Veterans Information Systems Technology Architecture (VistA) and updating the MED Microsoft® Access database. In order to retrieve patient records in MED, you must be connected to VistA and will be prompted to enter your VistA signon credentials. |
| SELECTING PATIENT RECORDS  | When you select patient records in MED, you are selecting previously retrieved patients from the MED Microsoft® Access database. In order to select patient records in MED, you do not need to be connected to VistA and will not be prompted to enter your VistA signon credentials.                                                                                 |

<span id="_Toc298228253" class="anchor"></span>Index

# A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access Error, 30

CPRS CHART – Library Not Registered Error, 30

Adobe Website, xvii

Application Context Error, 29

Assumptions about the Reader, xvi

# C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Callout Boxes, xv

Client workstation

Configure, 6

Configuring

Client Workstation, 6

VistA M Server, 5

CPRS

Notes Tab, 12, 13

Verify and Prepare MED Templates for Use with CPRS, 12

CPRS CHART – Library Not Registered Error, 30

CPRS Error, 35

Create Network Share Directory, 3

# D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data & Files Tab, 7

Database

MED Database Compact Messages, 32

MED Database Open Error, 31

Database Tab, 8

Dates

Progress Notes, 17

Disclaimers, xiv

Documentation Conventions, xiv

Documentation Navigation, xv

# E

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Messages

Troubleshooting, 27

Errors, 27

Application Context, 29

CPRS, 35

CPRS CHART – Library Not Registered Error, 30

Invalid Date, 36

Invalid Pointer Operation, 28

MED Database Open, 31

MED Missing Remote Procedure Calls (RPCs) in VistA, 28

Missing Required Data Fields, 36

Network Connection, 33

Patch TIU\*1\*257 is Not Current in VistA, 27

RPC Broker, 34

Section 508, 37

Write Access, 30

Examples

Import, 20

# F

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figures, xi

Files

OE/RR COM OBJECTS (#101.15), 12

# G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Glossary, 39

GUI

Online Help, xvi

Guidelines

Creating Section 508 Compliant TIU Templates, 14

# H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Health Summary, 6, 9, 11

Deleting the TIU MED HSTYPE Parameter, 11

Setting the TIU MED HSTYPE Parameter, 9

Health Summary Parameter Delete Option, 5, 6, 11, 24

Health Summary Type for MED Parameter, 6, 9, 11

Help

Online, xvi

History, Revisions to Documentation and Patches, iii

Home Pages

Adobe Website, xvii

VHA Software Document Library (VDL)

Website, xvii

VistA Development Website, xiv

How to

Obtain Technical Information Online, xvi

Use this Manual, xiii

# I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementation, 3

Import

Criteria

Progress Notes, 17

Date Sensitivity, 17

Examples, 20

Security Keys, 19

Examples, 20

Intended Audience, xiii

Introduction, 1

Invalid Date Error, 36

Invalid Pointer Operation Error, 28

# K

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Keys, 19, 25

# L

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Legal Requirements, xiii

Library Not Registered Error

CPRS CHART, 30

# M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Maintenance, 3

Manage Mobile Electronic Documentation Option, 5, 6, 9, 11, 24

MED

Options, 24

Progress Notes Date Sensitivity, 17

Remote Procedure Calls, 26

Routines, 23

Security Keys, 25

Progress Notes, 19

Set Up Network Share Directory for MED Templates, 3

Software Summary Setup Procedures, 3

Verify and Prepare MED Templates for Use with CPRS, 12

MED Database Compact Messages, 32

MED Database Open Error, 31

MED Missing Remote Procedure Calls (RPCs) in VistA Error, 28

Menus

TIU MED MANAGEMENT, 24

Missing Required Data Fields Error, 36

Mobile Electronic Documentation option, 35

Mobile Electronic Documentation Option, 3, 6, 24

# N

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network Connection Error, 33

# O

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Obtaining

Data Dictionary Listings, xvi

Technical Information Online, How to, xvi

OE/RR COM OBJECTS File (#101.15), 12

Online

Help, xvi

Options, 24

Health Summary Parameter Delete, 5, 6, 11, 24

Manage Mobile Electronic Documentation, 5, 6, 9, 11, 24

Mobile Electronic Documentation, 24

Mobile Electronic Documentation option, 35

Mobile Electronic Documentation Option, 3, 6

TIU MED DEL PARM, 5, 6, 11, 24

TIU MED GUI RPC V2, 35

TIU MED GUI RPC V2, 3, 6, 24, 35

TIU MED MANAGEMENT, 5, 6, 9, 11, 24

Orientation, xiii

# P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Parameters

Health Summary Type for MED, 6, 9, 11

TIU MED HSTYPE, 6, 9, 11

Patch TIU\*1\*257 is Not Current in VistA Error, 27

Permissions Error, 30

CPRS CHART – Library Not Registered, 30

Progress Notes

Import Criteria, 17

Date Sensitivity, 17

Examples, 20

Security Keys, 19

PS Anonymous Directories, xvii

# R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reader, Assumptions about the, xvi

Reference Materials, xvii

Remote Procedure Calls, 26

Requirements

Legal, xiii

Revision History, iii

Routines, 23

RPC Broker Error, 34

RPCs, 26

# S

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Scratch Pad

Tab, 13

Templates, 13

Section 508

Creating Section 508 Compliant TIU Templates, 14

Security Keys, 25

Progress Notes, 19

TIU MED MANUAL OVERRIDE, 5, 19, 20, 25

TIU MED MANUAL PATIENT, 5, 19, 20, 25

TIU MED MGT, 5, 10, 24, 25

Server

Configure Client Workstation, 6

Configure VistA M Server, 5

# T

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Tables, xii

Tabs

CPRS Notes, 12, 13

Data & Files, 7

Database, 8

Scratch Pad, 13

Templates

Create Network Share Directory for MED Templates, 3

Creating Section 508 Compliant TIU Templates, 14

Scratch Pad, 13

Verify and Prepare MED Templates for Use with CPRS, 12

TIU MED DEL PARM Option, 5, 6, 11, 24

TIU MED GUI RPC V2 Option, 35

TIU MED GUI RPC V2 Option, 3, 6, 24, 35

TIU MED HSTYPE Parameter, 6, 9, 11

Deleting, 11

Setting, 9

TIU MED MANAGEMENT Menu, 24

TIU MED MANAGEMENT Option, 5, 6, 9, 11

TIU MED MANUAL OVERRIDE Security Key, 5, 19, 20, 25

TIU MED MANUAL PATIENT Security Key, 5, 19, 20, 25

TIU MED MGT Security Key, 5, 10, 24, 25

Troubleshooting

Error Messages, 27

# U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

URLs

Adobe Website, xvii

VHA Software Document Library (VDL)

Website, xvii

VistA Development

Website, xiv

# V

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify and Prepare MED Templates for Use with CPRS, 12

VHA Software Document Library (VDL)

Website, xvii

VistA M Server

Configure, 5

# W

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Warnings

MED Database Compact, 32

Web Pages

Adobe Website, xvii

VHA Software Document Library (VDL)

Website, xvii

VistA Development Website, xiv

Write Access Error, 30