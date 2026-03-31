---
title: VistA Imaging System Clinical Capture User Manual
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: VistA Imaging System Clinical Capture
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 3
description: 
audience: 
keywords: 
  - capture
  - table
  - clinical
  - imaging
  - contents
  - image
  - vista
  - manual
  - window
  - class
page_count: 0
word_count: 15734
section_count: 117
table_count: 8
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: November 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_capture_user_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_capture_user_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![](vista-imaging-system-clinical-capture-user-manual/001.png)

VistA Imaging System Clinical Capture User Manual

> November 2017 – Revision 9 MAG\*3.0\*189

> Department of Veterans Affairs Product Development

> Health Provider Systems

> Clinical Capture User Manual VistA Imaging MAG\*3.0\*189 November 2017

> Property of the US Government

> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development group.

> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

> VistA Imaging Office of Enterprise Development Department of Veterans Affairs

> Internet: <u>REDACTED</u>

> SharePoint: <u>REDACTED</u>

#### Revision History

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Rev</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>April 2010</td>
<td>.9</td>
<td>Initial draft, <u>REDACTED</u></td>
</tr>
<tr class="even">
<td>July 2010</td>
<td>1.0</td>
<td>Final <u>REDACTED</u></td>
</tr>
<tr class="odd">
<td>May 2011</td>
<td>1.1</td>
<td><ul>
<li><p>P106 updates (rev 2). <u>REDACTED</u></p></li>
<li><p>Globally updated screen shot of the Select Image Association dialog box, Format dialog box</p></li>
<li><p>Updated sections <em>Batch Capture Transfer Buttons</em>, <em>Batch Capture Options window</em>, <em>Imaging Workstation Configuration Window</em>, <em>Image Format</em>, <em>Association, Security Keys.</em></p></li>
<li><p>Added new sections <em>TeleReader Consult</em> and <em>Selecting a TeleReader Consult</em></p></li>
</ul></td>
</tr>
<tr class="even">
<td>May 2011</td>
<td>2.0</td>
<td><ul>
<li><p>P117 updates. <u>REDACTED</u></p></li>
<li><p>Globally updated screen shots of the main Capture window to show the new DICOM data field.</p></li>
<li><p>Globally updated screens shots of Input source window</p></li>
<li><p>Deleted QA Review section</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>November 2012</td>
<td>3.0</td>
<td><p>P122 updates. <u>REDACTED</u></p>
<ul>
<li><p>Revised sections: <em>Acronyms</em>, <em>Document/Image Capture Summary Steps</em>, <em>Document/Image Capture with Clinical Capture</em>, <em>Logging In &amp; Starting Clinical Capture</em>, <em>Attaching a Scanned Document to a Different Author’s Progress Note</em>, <em>Selecting a TeleReader Consult</em>, <em>Display Area</em>, <em>Image Manipulation Buttons</em>, <em>Scanning Documents as a Single Image</em>, <em>Scanning Documents as a Group (Study)</em>, <em>Options menu</em>, <em>Appendix A: Supplemental Logon Screens</em>.</p></li>
<li><p>Added new sections: <em>Image Annotation</em>, <em>Annotation Permissions</em>, <em>Annotating Images</em>, <em>Annotation Tools</em>, <em>Drawing Lines</em>, <em>Making Freehand Drawings</em>, <em>Drawing Rectangles</em>, <em>Adding Text to Images</em>, <em>Drawing Ellipses</em>, <em>Drawing Arrows</em>,</p></li>
</ul>
<p><em>Highlighting Areas</em>, <em>Using the Ruler</em>, <em>Calibrating Rulers, Measuring Angles in Images, Selecting Annotations, Moving Selected Annotations, Resizing</em></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Rev</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><em>Annotations, Deleting Annotations, Exiting Annotation Mode and Saving Annotations with the Image, Using the Annotation Property Editor, Setting Line/Arrow Properties, Setting Line/Arrow Shape Properties, Setting Line/Arrow Color Properties, Setting Freehand Properties, Setting Freehand Line Properties, Setting Freehand Color Properties, Setting Rectangle/Highlighter Properties, Setting Rectangle/Highlighter Shape Properties, Setting Rectangle/Highlighter Color Properties, Setting Text Properties, Setting Text Font Styles and Sizes</em>, <em>Editing Text, Setting Text Color Properties</em>, <em>Setting Ellipse Properties</em>, <em>Setting Ellipse Shape Properties</em>, <em>Setting Ellipse Color Properties</em>, <em>Setting Ruler Properties</em>, <em>Setting Ruler Font Styles and Sizes</em>, <em>Setting the Ruler Shape Properties</em>, <em>Setting Ruler Color Properties</em>, <em>Modifying Start Line Length and End Line Length</em>, <em>Setting Protractor Properties</em>, <em>Setting Protractor Font Styles and Sizes</em>, <em>Setting the Protractor Shape Properties</em>, <em>Setting Protractor Color Properties</em>, <em>Setting Global Annotation Attributes</em>, <em>Default Values for Annotations</em>, <em>Setting Global Annotation Attributes from the Options Menu</em>, <em>Setting Global Annotation Font Attributes</em>, <em>Setting Global Annotation Line Width Attributes</em>, <em>Setting Global Annotation Color Attributes</em>, <em>Setting Global Annotation Opacity Attributes</em>, <em>Setting Global Annotation Arrow Attributes</em>.</td>
</tr>
<tr class="even">
<td>May 2013</td>
<td>4.0</td>
<td><p>Updated for Patch 129. <u>REDACTED</u></p>
<ul>
<li><p>Revised sections: <em>Conventions, Acronyms, Logging In and Starting Clinical Capture, Selecting a Patient, Configuration Settings Bar, Progress Note, Discharge Summaries, Clinical Procedures List, Creating an Addendum for Progress Notes, Create New Progress Notes, Progress Notes Window Options, Show Related Notes / Addendums, Using Keyboard Shortcuts, Alternate Viewer Options, Help Menu, Appendix A: Supplemental Logon Screens</em>.</p></li>
<li><p>Added new sections: <em>Creating an Addendum for Progress Notes, Starting Clinical Capture When Using CCOW, Starting Clinical Capture from CPRS, Starting Clinical Capture as a Standalone Application, Context Menu,</em> and <em>Appendix B: Clinical Context Object Workgroup</em>.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>August 2013</td>
<td>5.0</td>
<td><p>Updated for Patch 140. <u>REDACTED</u></p>
<p>Revised sections: <em>Input Source, Format, Menu Options and Functions, All Settings, and others</em>. Added sections <em>Combine TIF Scans</em>, <em>Combine PDF Scans</em>, <em>Scanning to PDF.</em></p></td>
</tr>
<tr class="even">
<td>July 2016</td>
<td>6.0</td>
<td><p>Updated for Patch 151 <u>REDACTED</u></p>
<p>Revised sections: Progress Notes Windows Options, Note Listing Status Bar, and Display Area</p>
<p>Added details from the What’s New document.</p></td>
</tr>
<tr class="odd">
<td>April 2017</td>
<td>7.0</td>
<td>Updated the Starting Clinical Capture as a Standalone Application section and Appendix A with 2FA PIV/PIN directions that replace the access/verify login process.</td>
</tr>
<tr class="even">
<td>June 2017</td>
<td>8.0</td>
<td><p>Updated for Patch 178 <u>REDACTED</u></p>
<p>Revised section: Starting Clinical Capture as a Standalone Application wording in step 4, page 17.</p></td>
</tr>
<tr class="odd">
<td>November 2017</td>
<td>9.0</td>
<td><p>Updates for MAG*3.0*189, adding directions to save configuration default and options for single image or study group settings in the Savings section under Document/ Image Capture with Clinical Capture. Removed the What’s New section. <u>REDACTED</u></p>
<p>Updated Table of Content Table and removed extra spacing. <u>REDACTED</u></p></td>
</tr>
</tbody>
</table>

> This page intentionally left blank.
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Terms of Use](#terms-of-use)
  - [About This Manual](#about-this-manual)
  - [Related Manuals](#related-manuals)
  - [MAG\3.0\Conventions](#mag30conventions)
  - [Acronyms](#acronyms)
  - [Getting Help](#getting-help)
- [Document Scanning Overview](#document-scanning-overview)
- [Document/Image Capture with Clinical Capture](#documentimage-capture-with-clinical-capture)
  - [Logging In and Starting Clinical Capture](#logging-in-and-starting-clinical-capture)
  - [Selecting a Patient](#selecting-a-patient)
  - [Configuration Settings Bar](#configuration-settings-bar)
  - [Input Source \\ Image Format](#input-source-image-format)
  - [Saving](#saving)
  - [Mode](#mode)
  - [Other](#other)
  - [Association Choices](#association-choices)
  - [Why Scan Documents?](#why-scan-documents)
  - [Document/ Image Capture Summary Steps](#document-image-capture-summary-steps)
- [Selecting a Capture Configuration](#selecting-a-capture-configuration)
  - [Configurations](#configurations)
  - [Selecting Capture Settings](#selecting-capture-settings)
  - [Configuration Settings Bar](#configuration-settings-bar-1)
  - [Configuration Buttons](#configuration-buttons)
  - [Creating Configuration Buttons](#creating-configuration-buttons)
- [Entering Data](#entering-data)
  - [Required Input Fields](#required-input-fields)
  - [Capture Date](#capture-date)
  - [Document Date](#document-date)
  - [Event Date](#event-date)
  - [Entering Data for the Image](#entering-data-for-the-image)
  - [Hold Value Option](#hold-value-option)
- [Patient Only Images](#patient-only-images)
- [Administrative Documents](#administrative-documents)
- [Attaching Documents to Notes or Reports](#attaching-documents-to-notes-or-reports)
  - [Selecting a Progress Note (TIU)](#selecting-a-progress-note-tiu)
  - [Configuring the Default Display Preferences for Progress Notes](#configuring-the-default-display-preferences-for-progress-notes)
  - [Filtering Options for Select Progress Note List](#filtering-options-for-select-progress-note-list)
  - [Preferences for Progress Notes](#preferences-for-progress-notes)
  - [Show Related Notes / Addendums](#show-related-notes-addendums)
  - [Progress Note Icons](#progress-note-icons)
  - [Selecting a Surgical Case](#selecting-a-surgical-case)
  - [Select Directory of Images to Import](#select-directory-of-images-to-import)
  - [Selecting a Radiology Exam](#selecting-a-radiology-exam)
  - [Selecting a Laboratory Specimen](#selecting-a-laboratory-specimen)
  - [Selecting a Medicine Procedure](#selecting-a-medicine-procedure)
  - [Selecting a Clinical Procedure](#selecting-a-clinical-procedure)
  - [Selecting a TeleReader Consult](#selecting-a-telereader-consult)
- [Image Index Guidelines](#image-index-guidelines)
  - [Indexing Documents](#indexing-documents)
  - [Entering Date and Origin](#entering-date-and-origin)
  - [Entering ‘Type,’ ‘Specialty,’ and ‘Proc/Event’ Values](#entering-type-specialty-and-procevent-values)
  - [Entering Image Descriptions](#entering-image-descriptions)
- [Image Capture Options](#image-capture-options)
  - [Scanning Documents as a Single Image](#scanning-documents-as-a-single-image)
  - [Scanning Multiple-Page TIFFs](#scanning-multiple-page-tiffs)
  - [Scanning to PDF](#scanning-to-pdf)
  - [Image Quality](#image-quality)
- [Image Annotation](#image-annotation)
- [Completing Capture](#completing-capture)
  - [Scan Document or Color Picture](#scan-document-or-color-picture)
  - [Meteor/Orion Imaging Boards](#meteororion-imaging-boards)
  - [Digital and Still Video Camera Input](#digital-and-still-video-camera-input)
    - [Using the TWAIN Interface](#using-the-twain-interface)
  - [Validate Image Data](#validate-image-data)
  - [Display Area](#display-area)
  - [Image Manipulation Buttons](#image-manipulation-buttons)
  - [Warning Panel for Patient Change](#warning-panel-for-patient-change)
  - [Approving the Image](#approving-the-image)
  - [Image Function Buttons](#image-function-buttons)
  - [Batch Capture Transfer Buttons](#batch-capture-transfer-buttons)
  - [Batch Capture Options window](#batch-capture-options-window)
  - [Long Image Description](#long-image-description)
  - [Confirmation Window](#confirmation-window)
  - [Indicating Completion of a Study](#indicating-completion-of-a-study)
  - [Save Image Data to VistA](#save-image-data-to-vista)
  - [Fails](#fails)
- [Importing Documents/Images](#importing-documentsimages)
  - [Import File from Workstation](#import-file-from-workstation)
  - [Import Directory List](#import-directory-list)
- [Timesavers](#timesavers)
  - [Using Keyboard Shortcuts](#using-keyboard-shortcuts)
  - [Using “Auto-Settings” to Save Keystrokes](#using-auto-settings-to-save-keystrokes)
  - [Defining Display Area Defaults](#defining-display-area-defaults)
  - [Settings](#settings)
- [Miscellaneous](#miscellaneous)
  - [Image Copy](#image-copy)
  - [File Copy Progress Bar](#file-copy-progress-bar)
- [Menu Options and Functions](#menu-options-and-functions)
  - [File Menu](#file-menu)
  - [Menu Options](#menu-options)
  - [TIU Business Rules](#tiu-business-rules)
  - [Context Menu](#context-menu)
  - [Options Menu](#options-menu)
  - [Tools Menu](#tools-menu)
  - [Configurations Menu](#configurations-menu)
  - [Capture Configuration List](#capture-configuration-list)
  - [Save Capture Configuration](#save-capture-configuration)
  - [Clear Configuration values](#clear-configuration-values)
  - [Properties Saved with Configuration Definitions](#properties-saved-with-configuration-definitions)
  - [‘Association’ Configuration Settings](#association-configuration-settings)
  - [Workstation Configuration](#workstation-configuration)
  - [Imaging Workstation Configuration Window](#imaging-workstation-configuration-window)
- [Clinical Capture System Manager Options](#clinical-capture-system-manager-options)
  - [System Manager Menu](#system-manager-menu)
- [Workstation Configuration](#workstation-configuration-1)
  - [Button/Field Options:](#buttonfield-options)
  - [Demo Options](#demo-options)
  - [Image Association](#image-association)
  - [Image Format](#image-format)
  - [Import Options](#import-options)
  - [Input Source](#input-source)
  - [Input Source Options](#input-source-options)
  - [Login Options](#login-options)
  - [Medicine Options](#medicine-options)
  - [Remote Site Options](#remote-site-options)
  - [Save Options](#save-options)
  - [SYSAutoUpdate](#sysautoupdate)
  - [SYSConfigurations](#sysconfigurations)
  - [SYSFonts](#sysfonts)
  - [SYSLastPositions](#syslastpositions)
  - [SYSMeteor](#sysmeteor)
  - [SYSSETTINGS](#syssettings)
  - [SYSTWAIN](#systwain)
  - [TeleReader Options](#telereader-options)
  - [VISTA MUSE](#vista-muse)
  - [Workstation Settings](#workstation-settings)
- [Utilities Menu](#utilities-menu)
  - [Controlled Image](#controlled-image)
  - [Setting the Controlled Image Property](#setting-the-controlled-image-property)
- [Image Menu](#image-menu)
- [Help Menu](#help-menu)
  - [VistA Imaging Capture User Guide](#vista-imaging-capture-user-guide)
  - [Error Code Lookup…](#error-code-lookup)
  - [About…](#about)
- [Security Keys](#security-keys)
- [Appendix A: Supplemental Logon Screens](#appendix-a-supplemental-logon-screens)
- [Appendix B: Clinical Context Object Workgroup](#appendix-b-clinical-context-object-workgroup)
  - [CCOW Overview](#ccow-overview)
  - [Patient Context in Clinical Capture](#patient-context-in-clinical-capture)
- [Appendix C: Discontinued Menu Options](#appendix-c-discontinued-menu-options)
  - [The Help Menu and Submenu items have changed.](#the-help-menu-and-submenu-items-have-changed)
> This manual explains how to configure and use the Clinical Capture software for Image Capture. Clinical Capture is a part of the VistA Imaging System. This manual is intended for use by clinical and administrative staff responsible for incorporating captured images into a patient’s electronic medical record.
> This manual assumes the users are familiar with the Windows environment, and that the Clinical Capture workstation being used has been configured to perform Image Capture. For more information about the Clinical Capture software, refer to the Imaging System Users Guide.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In compliance with Food and Drug Administration (FDA) and VA policies, authorization to use this software is contingent on the execution of a Site Agreement between the VistA Imaging Office of Enterprise Development (OED) group and the site where this software is installed.

> In addition to any restrictions noted in the Site Agreement, the following restrictions apply:

| ![](vista-imaging-system-clinical-capture-user-manual/002.png) | No modifications may be made to this software without the express written consent of the VistA Imaging National Project Manager.                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vista-imaging-system-clinical-capture-user-manual/003.png) | The Food and Drug Administration classifies this software as a medical device. Modifications to the computer where this software is installed, such as the installation of unapproved hardware or software, will adulterate the medical device. The use of an adulterated medical device violates US Federal Law (21CFR820). |

## About This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual has two major sections:

- Task-Oriented Manual
- Reference Manual

> Task Oriented Manual explains tasks associated with Clinical Capture with steps involved and accompanying screenshots.

> Reference Manual is the section that describes all the available Menu Options and functions associated with Clinical Capture.

> This manual contains the following chapters:

> The Document Scanning Overview provides general information about document scanning and summarizes the document scanning process.

> Document Scanning with Clinical Capture provides how-to instructions for each major part of Image capture and the suggested Capture process.

> The Timesavers chapter describes some of Clinical Capture’s timesaving features.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Additional information about document scanning and Clinical Capture can be found in the following documents:

- Imaging System Technical Manual
- Imaging System Installation Guide
- [<u>VistA Document Library</u>](http://www.va.gov/vdl/section.asp?secid=1)
- Health Information Management Service, <u>REDACTED</u>
- <u>REDACTED</u>

## MAG\*3.0\*Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual uses the following conventions:

- For the purpose of this manual Document and/or Image are used synonymously and the capture process is the same for each.
- GUI elements (menu item, button, and field) are presented in bold font.
- References to sections in this document or to other documents are in *italics*.
- Notifications or controls that are identified by a phrase are enclosed in single quotation marks. For example: Click the ‘Share this folder as’ option.
- Instructions for using menus are condensed using the ‘ \| ’ (pipe) symbol. For example: Click File \| Save means: Click the File menu, then click the Save option.
- Useful or supplementary information is indicated by a TIP.
- Important or required information is indicated by a NOTE.
- Warnings concerning potential data loss or device misuse are indicated by: ![](vista-imaging-system-clinical-capture-user-manual/004.png)

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Acronym</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CCOW</td>
<td><blockquote>
<p>Clinical Context Object Workgroup</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CPRS</td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>EKG</td>
<td><blockquote>
<p>Electrocardiogram</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FAQ</td>
<td><blockquote>
<p>Frequently Asked Questions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FDA</td>
<td><blockquote>
<p>Food and Drug Administration</p>
</blockquote></td>
</tr>
<tr class="even">
<td>HIMS</td>
<td><blockquote>
<p>Health Information Management Service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HRN</td>
<td><blockquote>
<p>Health Record Number</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Acronym</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IHS</td>
<td><blockquote>
<p>Indian Health Service</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PAL</td>
<td><blockquote>
<p>Phase Alternate Line, the predominant video system or standard mostly used overseas</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>QA</td>
<td><blockquote>
<p>Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RGB</td>
<td>Red, Green, Blue, the device-dependent color model used in color televisions, video and image devices</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td><blockquote>
<p>Social Security Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>TIU</td>
<td><blockquote>
<p>Text Integration Utility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>TWAIN</td>
<td><blockquote>
<p>Though not a real acronym, TWAIN is the name of the standard interface for image acquisition devices first released in 1992 that came from an archaic form of the word “two”.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA</td>
<td><blockquote>
<p>Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VHA</td>
<td><blockquote>
<p>Veteran Health Administration</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VistA</td>
<td><blockquote>
<p>Veterans Health Information System and Technology Architecture</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you encounter any problems using this software, contact your local Imaging Coordinator or support staff. <u>REDACTED</u>

# Document Scanning Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter provides general information about document scanning using Clinical Capture and summarizes the document scanning process.

# Document/Image Capture with Clinical Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides how-to instructions for each major part of the document/image capture process. It covers:

- Logging in and starting Clinical Capture
- Selecting a capture configuration
- Selecting a patient
- Attaching documents to notes or reports
- Image index guidelines
- Image capture options
- Adding annotations
- Completing capture

> NOTE: VistA Imaging Clinical Capture software is highly configurable. Its appearance may not match the examples shown in this manual.

## Logging In and Starting Clinical Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The method used to start Clinical Capture can vary, depending on how VistA Imaging is set up at your site and on whether it is using Clinical Context Object Workgroup (CCOW) or not.

#### Starting Clinical Capture When Using CCOW

> CCOW is a standard for synchronizing common data. If it is installed on the workstation and operational, it synchronizes the patient context for all CCOW-compliant applications that are running on the workstation.

> If you are using CCOW, when you start Clinical Capture, the Context menu appears in the menu bar and the patient context is synchronized with Clinical Display and CPRS. That is, if any of these applications are open, the patient that is displayed in Clinical Capture will match the one displayed in Clinical Display and/or in CPRS. If Clinical Display is running, you will not have to log into VistA and you will not be presented with the VistA Sign-on box. In addition to this, you will see the CCOW icon ![](vista-imaging-system-clinical-capture-user-manual/005.png) next to the Select Patient button on the Vista Imaging Capture window. For more information about CCOW and patient context, see <span id="_bookmark174" class="anchor"></span>*[Appendix B: Clinical](\l)* [*Context Object Workgroup*.](#_bookmark174)

#### Starting Clinical Capture from CPRS

> You usually start Clinical Capture from CPRS when there is a need to review information in the patient’s medical record. The current patient in Clinical Capture will always match the current patient in CPRS even if you are not using CCOW. The patient context is synchronized using Windows Messaging.

> You can start Clinical Capture from CPRS by selecting CPRS \| Tools \| VistA Imaging Capture

> or as a standalone application. For more information, see the *CPRS User Guide*.

#### Starting Clinical Capture as a Standalone Application

> Starting Clinical Capture as a standalone application refers to starting the application from the Start menu on the workstation, rather than from CPRS. If you are using CCOW and if there are CCOW-compliant applications that are already running on the workstation, when you start Clinical Capture, it joins the current context and no longer runs as a ‘standalone’ application.

#### To start Clinical Capture as a standalone application:

1.  Double-click the Capture shortcut ![](vista-imaging-system-clinical-capture-user-manual/006.png) on the Windows desktop.
2.  If a shortcut is not available, click ![](vista-imaging-system-clinical-capture-user-manual/007.png), then choose All Programs \| VistA Imaging Programs \| VistA Imaging Clinical Capture 32-bit. Depending on how your site is configured, you may see supplemental Logon screens. Please refer to *[Appendix A: Supplemental Logon Screens](\l)* for additional information.
3.  Make sure you have a valid PIV card attached to the computer. You will be prompted to select a certificate: Then click on the OK button.

![](vista-imaging-system-clinical-capture-user-manual/008.png)

> If you are using CCOW and if Clinical Display is running skip this step. Your user is already logged into VistA and you are not prompted to enter your access and verify codes into the VistA Sign-on dialog box.

4.  Next, you will be prompted to enter your PIN. Enter your PIN and click on the OK button.

> ![](vista-imaging-system-clinical-capture-user-manual/009.png)

> Upon successful authentication and login, the user will be allowed to continue to the application. When an attempt to log in with PIV/PIN fails to authenticate 2FA, the application will prompt for Access/Verify codes \[credentials\]. If the VistA Sign-on box is returned, enter your Access and Verify codes, and then click OK.

![](vista-imaging-system-clinical-capture-user-manual/010.png)

> Once you are granted access to the system, the Clinical Capture client connects to VistA and the VistA Imaging Capture window displays.

![](vista-imaging-system-clinical-capture-user-manual/011.png)

> Note: If you are not using CCOW, you will not see the Context menu and the icon next to the Select Patient button.

## Selecting a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section explains how to select patients using VistA Imaging Clinical Capture. You have to select a patient when you are running Clinical Capture as a standalone application and when you are not using CCOW or when you start Clinical Capture and neither CPRS nor Clinical Display are running.

#### NOTES:

1)  If you start Clinical Capture from CPRS and CCOW is not running, the current patient in Clinical Capture will always match the current patient in CPRS. When you need to change patients, you will need to use CPRS.
2)  If you are using CCOW, the current patient in Clinical Capture will always match the current patient in CPRS and/or Clinical Display.

> For more information about CCOW and patient context, see *[Appendix B: Clinical Context Object](#_bookmark174)* [*Workgroup*.](#_bookmark174)

#### To select a patient:

1.  Log in to VistA Imaging Clinical Capture.
2.  In the VistA Imaging Clinical Capture screen, use any of these ways to select patient lookup:
    - Click the Select Patient button in the VistA Imaging Clinical Capture screen. If CCOW is installed, there is an icon next to the button as illustrated in the following image.

![](vista-imaging-system-clinical-capture-user-manual/012.png)

- Choose File \| Select Patient.

![](vista-imaging-system-clinical-capture-user-manual/013.png)

- Press CTRL+P.
- Press ALT + P.
3.  In the Patient box of the Patient Lookup dialog box, type the name of the patient you want to capture images for.

![](vista-imaging-system-clinical-capture-user-manual/014.png)

> Enter the patient’s last name first (no need to enter the entire name), or enter the first letter of the last name and the last four digits in the SSN (no spaces). If you enter both the last name and the first name, use only a comma to separate the names. VistA Imaging will not recognize a patient name if you use spaces. If you are located at an Indian Health Service (IHS) site, you can use the Health Record Number (HRN) for the patient identification.

4.  Press Enter to perform the patient lookup.

> If an exact match is found for information entered, that patient is selected and the patient lookup window is closed.

> If there is more than one matching name, a list of names will be displayed along with the Patient’s Photo ID where available. When Patient Photo is unavailable, a silhouette is displayed as shown in the following image.

> ![](vista-imaging-system-clinical-capture-user-manual/015.png)

5.  Select the patient you want to use. Then click OK.

## Configuration Settings Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The top of the VistA Imaging Clinical Capture window looks like this:

![](vista-imaging-system-clinical-capture-user-manual/016.png)

> The Configuration Settings bar has options that you can select to capture an image. Below is a screenshot of the configuration bar and explanation of options follows.

> Near the top of the VistA Imaging Clinical Capture window, under the menus is the Configuration Settings Bar.

![](vista-imaging-system-clinical-capture-user-manual/017.png)

- The options are: Input Source, Image Format, Association, Saving

> (Study/Single), Mode and Other.

- The words in blue & bold are the default configuration settings.
- The configuration buttons are below the configuration settings.

> NOTE: If one or more configuration buttons are present, click the button that is appropriate for the type of document being scanned. Configuration buttons can be different from workstation to workstation, and are usually named for particular documents. These are configurable buttons based on the configurations that are frequently used.

## Input Source \\ Image Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the input source from the menu bar by clicking the Source ![](vista-imaging-system-clinical-capture-user-manual/018.png) button. Or select the image format by clicking the Format ![](vista-imaging-system-clinical-capture-user-manual/019.png) button.

> The Imaging Workstation configuration window opens.

> The Source/Format tab of the Imaging Workstation configuration window contains the most commonly used sources and formats.

![](vista-imaging-system-clinical-capture-user-manual/020.png)

> The Legacy tab of the Imaging Workstation configuration window includes contains the formats that are rarely used.

![](vista-imaging-system-clinical-capture-user-manual/021.png)

> The input source identifies the type of capture device being configured. It may be any of the following (either on the Source/Format tab or the Legacy tab):

- A Lumisys x-ray scanner, model 75 or 100, which produces a 1K x 1K x 8-bit gray scale image and optionally a 2K x 2K x 12-bit diagnostic quality gray scale image.
- The Matrox Meteor/Orion boards capture standard NTSC and PAL analog video in composite, RGB and S-Video (Y/C) formats. They are capable of handling color or black and white input. Captured images are 640x480x24 bits.
- Image Import from the local disk or a network drive.
- A standard TWAIN device such as a color, x-ray, or document scanner or a still video camera; these may produce a 1-bit or 8-bit black and white image or a 8-bit or 24-bit color image.
- A customized TWAIN source called Scanned Document which produces a 1-bit 300x300 dpi document (G4 FAX quality).

#### NOTES:

> TWAIN

> Clicking the TWAIN Source button displays a list of all TWAIN sources connected to the workstation.

- If only one TWAIN Source is connected to the workstation, which is usually the case:
  - It will be automatically selected.
  - No list will be displayed if the button is selected.
- If TWAIN Capture - Twain window has been selected as the input source, another window will be opened when 'Capture' is clicked. This is the TWAIN Window for the TWAIN device. Each TWAIN Device has its own TWAIN Window and TWAIN Image Types, In the TWAIN Window, image format and other image parameters will need to be selected.
- Be sure that the image format selected for the VistA Image Capture corresponds to the image type selected on the TWAIN window. Depending on the equipment manufacturer, different TWAIN Image Types may be listed, and not all vendors support all of these image formats.

#### Changing Image Formats

> When changing an input source on the Configuration Window, the Image Formats that are grayed-out (disabled) will also change. The Imaging System knows which Image Formats are applicable to each input Source and will enable-disable Image Formats as appropriate.

#### Disabled Selections

> Because of the complexity of multiple Image Formats and input Sources, there might be a situation where all Image Formats are disabled. If this situation occurs, contact the System Manager.

> ![](vista-imaging-system-clinical-capture-user-manual/022.png)

> NOTE: The greater gray scale or color dpi chosen, the larger the physical file created. This will affect transmission and storage processing times.

## Saving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is the option to save images as Study group or Single Image. Choose this option by clicking the Saving button. This property defines whether the captured images are saved as a part of a study (Group) or as a single image.

> When a single image is to be associated with the package report, (i.e., TIU Note), then Single Image should be used. This is generally the setting for document scanning and includes saving a multiple page document as a single image, such as a PDF. Study (Group) should only be used when multiple images are associated with the same package report. Generally, this is the setting for importing images, such as digital photographs.

> A special situation occurs when only one image is saved in a Study (Group); this is referred to as a *group of one*. Although a group of one will work, extra processing is required by Imaging functions in Clinical Capture, Display and the Background Processor. Also, the user has extra steps to complete when capturing to an image group. A group of one has been known to cause issues with Clinical Display and the Background Processor and most recently with Clinical Capture.

#### The Imaging team strongly recommends that the Saving option be changed to Single Image instead of Study (Group) and that the existing Configuration Buttons on the workstation be changed to Single Image instead of Study (Group).

> Note: Prior to MAG\*3.0\*189 the default setting for saving was Study (Group). For workstations that have not had previous versions of Clinical Capture installed, the default setting will be Single Image after installing MAG\*3.0\*189.

![](vista-imaging-system-clinical-capture-user-manual/023.png)

> A new utility (introduced in MAG\*3.0\*189) in the Clinical Capture client will enable the user to change all existing configurations from Study (Group) to Single Image.

#### Running the Utility:

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Run the utility from the Clinical Capture main window menu: Configurations | Modify Configurations: change Group to Single</th>
<th>![](vista-imaging-system-clinical-capture-user-manual/024.png)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>A confirmation window will display showing counts of existing configurations.</p>
<p>Click “OK.”</p></td>
<td>![](vista-imaging-system-clinical-capture-user-manual/025.png)</td>
</tr>
<tr class="even">
<td>The result will be displayed as a message at the bottom of the main window.</td>
<td>![](vista-imaging-system-clinical-capture-user-manual/026.png)</td>
</tr>
<tr class="odd">
<td><p>Optionally, you can verify that the changes were implemented by running the utility again.</p>
<p>Now, as shown on the right, there are no configurations defined as an Image Group.</p></td>
<td>![](vista-imaging-system-clinical-capture-user-manual/027.png)</td>
</tr>
</tbody>
</table>

> Changing from Single Image to Study (Group):

> If a site does capture multiple images to a Study (Group), you can modify and save an existing configuration button.

> To modify the existing configuration, follow the directions below:

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Click an existing configuration button that has Saving set to Single.</p>
<p>The configuration will be applied to the properties and fields of the Clinical Capture main window.</p></th>
<th><blockquote>
<p>![](vista-imaging-system-clinical-capture-user-manual/028.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Change from Single Image to Study (Group) .</p>
<p>Click “OK.”</p></td>
<td>![](vista-imaging-system-clinical-capture-user-manual/029.png)</td>
</tr>
<tr class="even">
<td>Now save the configuration.</td>
<td>![](vista-imaging-system-clinical-capture-user-manual/030.png)</td>
</tr>
<tr class="odd">
<td><p>The Save Configuration dialog window will display. The button’s name should be displayed, but if it’s not, retype the name exactly as it displayed on the button before you modified it.</p>
<p>Click “OK.”</p></td>
<td>![](vista-imaging-system-clinical-capture-user-manual/031.png)</td>
</tr>
<tr class="even">
<td>Click “OK” to overwrite the existing configuration.</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>![](vista-imaging-system-clinical-capture-user-manual/032.png)</td>
</tr>
</tbody>
</table>

## Mode

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is the option to save capture images OnLine. OnLine mode enables saving to VistA, Test Mode enables testing the device, but not saving to VistA. In Test Mode, Images are not saved. Choose this option by clicking the Mode button.

![](vista-imaging-system-clinical-capture-user-manual/033.png)

## Other

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option provides “Other” settings for input source. Choose this option by clicking the Other

> button.

![](vista-imaging-system-clinical-capture-user-manual/034.png)

## Association Choices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Click the Association button in the configuration toolbar to choose an Image Association. The options available for Image Association Choices are explained below. From the Select Image Association window, select one of the available options:

- VistA Package options (on the left side of the Select Image Association Window shown below), or
- Patient Only options (on the right side of the window shown below).

#### Choices include:

![](vista-imaging-system-clinical-capture-user-manual/035.png)

> After all selections have been made, the information will be displayed on the main Capture window.

> NOTE: Required information has an asterisk next to the selection field.

#### VistA Package Options

> Explanation of the VistA Package Options is provided in this section.

> NOTE: The screen shots shown below are partial to show the selected association only and do not show the entire capture window.

> Laboratory: When the Laboratory Package option is selected in Association, the capture window will display the following:

![](vista-imaging-system-clinical-capture-user-manual/036.png)

> The following window will be displayed once you click the Select Laboratory Specimen ![](vista-imaging-system-clinical-capture-user-manual/037.png) Button from the main Capture window. Select a Pathology Lab selection from this window to populate related information in the main Capture window.

> ![](vista-imaging-system-clinical-capture-user-manual/038.png)

> Medicine: When the Medicine Package option is selected in Association, the capture window will display the following:

![](vista-imaging-system-clinical-capture-user-manual/039.png)

> Click the Select Medicine Procedure button to select from the list of available options as shown in the image below. Select the procedure and click OK to populate related information in the main capture window.

> ![](vista-imaging-system-clinical-capture-user-manual/040.png)

> Progress Note: When the Progress Note Package option is selected in Association, the capture window will display the following:

![](vista-imaging-system-clinical-capture-user-manual/041.png)

> Click Select Progress Note button to display a list of available Progress notes for the selected patients shown in the image below. Select the note and click OK to populate related information in the main capture window.

> ![](vista-imaging-system-clinical-capture-user-manual/042.png)

> Clinical Procedures: When the Clinical Procedures Package option is selected in Association, the capture window will display the following:

![](vista-imaging-system-clinical-capture-user-manual/043.png)

> Click Select Clinical Procedure button to display a list of available Clinical Procedures for the selected patient as shown in the image below. Select the procedure and click OK to populate related information in the main capture window. For more information, refer to Clinical Procedure Package Procedures listed on the VistA Document Library.

> ![](vista-imaging-system-clinical-capture-user-manual/044.png)

> Surgery: When the Surgery Package option is selected in Association, the capture window will display the following:

![](vista-imaging-system-clinical-capture-user-manual/045.png)

> Click Select Surgery Case button to display a list of available Surgery Cases for the selected patient as shown in the image below. Select the case and click OK to populate related information in the main capture window.

![](vista-imaging-system-clinical-capture-user-manual/046.png)

> Radiology: When the Radiology Package option is selected in Association, the capture window will display the following:

![](vista-imaging-system-clinical-capture-user-manual/047.png)

> Click Select Radiology Exam button to display a list of available Radiology Exams for the selected patient, as shown in the image below. Select the case and click OK to populate related information in the main capture window.

![](vista-imaging-system-clinical-capture-user-manual/048.png)

> TeleReader Consult: When the TeleReader Consult Package option is selected in Association, the capture window will display the following:

![](vista-imaging-system-clinical-capture-user-manual/049.png)

> Click Select TeleReader Consult button to display a list of available TeleReader consult requests for the selected patient, as shown in the image below. Select the consult request and click OK to populate related information in the main capture window.

> ![](vista-imaging-system-clinical-capture-user-manual/050.png)

#### Patient Only

> Under Patient Only, there are three options available: Clinical, Photo ID and Administrative as shown below.

> Clinical: When Clinical is selected under Association, the capture window will display the following:

![](vista-imaging-system-clinical-capture-user-manual/051.png)

> Photo ID: When Photo ID Option is selected under Association, the capture window will display the following:

![](vista-imaging-system-clinical-capture-user-manual/052.png)

> Administrative: When Administrative Option is selected under Association, the capture window will display the following:

![](vista-imaging-system-clinical-capture-user-manual/053.png)

> NOTES:

- VistA Imaging has the optional functionality of limiting a user's ability to capture images to certain packages based on assigned Imaging Capture Keys.
- If a dialog window appears with a message similar to: *You don't have the proper Security Keys to capture Medicine Images,* contact the system manager.
- If images are being captured for a Study (Group) and the study is not yet complete, all Association choices will be disabled. The study must be closed by clicking 'Study Complete' before a new Association can be selected.

## Why Scan Documents?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VHA Directive 2001-045 requires that all VA medical centers implement a document imaging system by September 30, 2004. This directive states that all medical facilities must scan certain clinical documents to make them part of a patient’s electronic medical record. The directive specifically mentions advance directives and consent forms.

> Data that can be entered directly into CPRS should not be scanned.

> To comply with this directive, and to support the goal making a patient’s complete medical record available online, the following types of documents should be scanned.

- Consent forms and other documents with “wet” signatures of patients, practitioners, or other personnel
- Advance Directives
- Fee Basis Reports should be available from inside CPRS
- Results/reports from medical procedures that are not acquired directly from the instrument or entered in the VistA system.
- Means Tests
- Outside medical reports

> Additional types of documents can be scanned according to HIMS Directives referred to in the section [*Related Manuals*.](\l)

## Document/ Image Capture Summary Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Document scanning with Clinical Capture involves the following general steps. These steps are described in detail in the following chapter.

> NOTE: The order of steps 3 - 7 may vary, depending on how document scanning is set up.

1.  Log into VistA Imaging Capture program.

> *Some sites may choose to start Capture from CPRS.*

2.  Select a patient.

> *If you started Capture from CPRS, a patient will already be selected.*

3.  Select the appropriate “capture configuration” for the documents to be scanned.

> *Some Capture workstations will use a single capture configuration that is selected automatically. If multiple capture configurations are defined, a capture configuration will need to be selected by the user.*

4.  Define how the document will be added to a patient’s record.

> *Some scanned documents are linked directly to a patient record, while others are attached to a specific procedure or progress note.*

5.  Enter additional index information.

> *Depending on capture configuration selected, some information is pre-defined. Additional index values may need to be entered by the user.*

6.  Review the document for accuracy and readability before scanning. Also verify patient information before scanning.
7.  Capture the document/ Image.

> *With the proper equipment, multiple page documents can be scanned in a single operation and saved as a single PDF file or single TIF file. Multiple images such as digital photographs can be imported and saved as a “group” of images.*

> NOTE: For Telereader consults, only the first page is captured. Scan all other pages separately.

8.  Verify the patient ID, input data, and image quality.

> *Visually inspect the input data and image quality before capturing the image.*

> NOTE: Sites belonging to the Indian Health Service (IHS) can use the Health Record Number (HRN) to verify the patient identification.

9.  Finalize Capture.

> *When the capture is complete, the image will be available for display at other workstations.*

# Selecting a Capture Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vista-imaging-system-clinical-capture-user-manual/054.png)

> In the image shown above:

- Area A is the 'Current Settings' toolbar or 'Configuration Settings' bar. This toolbar allows you to select individual configuration settings.
- B is the 'Configuration Buttons' toolbar. A capture configuration refers to the group of saved settings that is associated with a Configuration Button.

> When you select the menu option: 'Configurations \| Save Configuration', you will be saving the current capture settings as a Configuration.

> Once a configuration button is clicked, the configuration settings become the current capture settings. You can change the current capture settings without changing the Capture Configuration. When you click the Configuration button again, the settings will be changed back to the values of the configuration button that was clicked.

## Selecting Capture Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before scanning a document, you will need to select the capture settings pertaining to the document to be scanned. Capture settings defines how the Capture program sets certain basic parameters when a document is scanned.

> The following steps are the suggested sequence of entering settings:

1.  Select a patient as described in previous sections.
2.  Then select a progress note or a procedure.
3.  Enter date in Doc/Image Date box.

![](vista-imaging-system-clinical-capture-user-manual/055.png)

4.  Click in the box to open the date/time selector window. Select Date/ Time and click OK.

> NOTE: Time selection is not required.

![](vista-imaging-system-clinical-capture-user-manual/056.png)

> Note: The Help button displays a list of keystrokes for navigating dates, as shown.

![](vista-imaging-system-clinical-capture-user-manual/057.png)

5.  After Selecting Date, enter additional required information by choosing from index field choices. The images below show some of the available choices for Doc/ Image Type and Specialty.

![](vista-imaging-system-clinical-capture-user-manual/058.png)![](vista-imaging-system-clinical-capture-user-manual/059.png)

> If you need assistance in determining which configuration settings should be used, contact your Clinical or Imaging Coordinator or HIMS department for guidance.

## Configuration Settings Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The image below shows the Configuration settings bar. All these options are explained in detail in sections to follow.

![](vista-imaging-system-clinical-capture-user-manual/060.png)

## Configuration Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If one or more configuration buttons are present, click the button that is appropriate for the type of document being scanned. Configuration buttons are often different from workstation to workstation, and are usually named for particular documents. These are configurable buttons based on the configurations that are frequently used.

> A sample screenshot of Configuration buttons is shown below. The configuration buttons can be configured at the workstation and the steps to save configuration buttons are described below.

![](vista-imaging-system-clinical-capture-user-manual/061.png)

> NOTE: Some sites choose to save index field values as a part of a capture configuration. If this is the case, you will see automatically selected values in some of the index fields on the left side of the Capture window.

> NOTE: You may see “Hold Value” icon ![](vista-imaging-system-clinical-capture-user-manual/062.png) next to some of the fields. For more information about “Hold Value”, see page 43

## Creating Configuration Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The image capture settings can be changed by:

- the Imaging Workstation configuration window,
- the Imaging Workstation: Capture configurations list window,
- clicking a Configuration Settings Button, located just below the menus, (Source,

#### Format, Association, Saving, Mode, Other) Examples:

> Source/Format tab is opened as shown below when the Source or Format buttons are clicked.

> ![](vista-imaging-system-clinical-capture-user-manual/063.png)

> Association - Window opens as shown below when clicked on Association button

![](vista-imaging-system-clinical-capture-user-manual/064.png)

> Just below the Configuration settings buttons and their displayed settings, are the saved configurations or Workstation Configurations.

![](vista-imaging-system-clinical-capture-user-manual/065.png)

> When one of these saved configuration buttons is clicked, the VistA Imaging Capture window is changed to the saved configurations of that button.

#### Save Configuration

> This dialog can be used to save the current state of the main Capture window as a new configuration or to overwrite an existing configuration.

> Enter a new or existing configuration name.

> ![](vista-imaging-system-clinical-capture-user-manual/066.png)

> If an existing configuration name is entered a confirmation dialog will appear.

![](vista-imaging-system-clinical-capture-user-manual/067.png)

# Entering Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Input Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Image Dates

> VistA Imaging can store 3 dates related to each image. These date fields are collected for imaging users. The dates can be used to filter and sort images.

## Capture Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Image Capture Date is stored in the VistA Imaging Database. This field is computed by the software when the image is added to the VistA Database.

## Document Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The "Document Date" is the Date/Time of the creation of the "original" document or image.
- There are situations when this date field is not known.

> Example 1: A CD is brought to the VA (from another agency) and imported into a radiology study.

- The Document Date will be the date the study was performed and images captured at that agency.
- The Capture Date will be the date it was stored in VistA Imaging.
- Example 2: An Advanced Directive is signed by a patient and the document is scanned into VistA Imaging at a later date.
- The Document Date will be the date the Advanced Directive was signed by the patient.
- The Capture Date will be the date the paper document was scanned and stored in VistA Imaging.

## Event Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This date is filed automatically and is not editable by the user. The date can be a Date/Time or Date only, depending on its association.

> When the information is associated with a patient (not VistA Package) then this field contains the Capture Date/Time.

> Additional Data required to capture an image to the patient record, depends on the association selected, and includes the following settings:

- Patient
- Study Performed
- Procedure Date
- Doc / Image Type
- Image Short Description
- Image File

> Optional data includes:

- Specialty
- Proc/Event
- Image long description

> A validity check is performed when the 'Image OK' ![](vista-imaging-system-clinical-capture-user-manual/068.png) button is clicked. If data is missing, a message is displayed in the message box at the bottom of the window and input focus is set to the field that needs data or the button that opens the selection window for the required data.

## Entering Data for the Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a screenshot of the Image Data in the Clinical Capture main window.

![](vista-imaging-system-clinical-capture-user-manual/069.png)

- If a Patient Photo ID is on file, it will be displayed to the left of the Patient Name.
- The fields with a gray background are filled by VistA Imaging when the user makes selections.

> The input data fields include:

- Patient ID (name and SSN is input from the VistA Select Patient information)

#### Study Performed

- Procedure Date (and Time - input by the system)
- Doc/Image Date
- Origin

> ![](vista-imaging-system-clinical-capture-user-manual/070.png)

- Doc/Image Type (selected from a list),

> Note: For a TeleReader Consult association, select IMAGE or CONSULT.

- Specialty (\* optional, selected from a list),
- Proc/Event (\* optional, selected from a list)
- Image Description (generated from the previous selections, user can add/modify the entry).

> If the VistA Imaging Capture window is resized a scroll bar may become visible.

> Press \<TAB\> to move from field to field, as an alternative to scrolling. The area will scroll automatically so that the current input field will be in the visible area.

> When the 'Image OK' ![](vista-imaging-system-clinical-capture-user-manual/071.png) button is clicked, VistA Imaging checks the data fields required to save an image to VistA. If any required fields are missing, VistA Imaging will warn the user.

![](vista-imaging-system-clinical-capture-user-manual/072.png)

> If the Save as window is set to Study (Group), then when the last image in the Group is saved and the Study Complete button is clicked -- you will be given the option of entering a 'Long Description' for this group. Long image descriptions are displayed as the first paragraph of Image Reports.

> Index fields that are to be populated by the user are displayed on the left side of the main Capture window. Each field has a pull-down list populated with values common to all VistA Imaging sites. The user can use the mouse or the keyboard to select values for each field.\*(see below)

> ![](vista-imaging-system-clinical-capture-user-manual/073.png)

> \* asterisks in the graphic above, denote a required field

> The Specialty and Proc/Event Fields are unique in that a value selected for one of the two fields *will be used to filter (reduce) the contents of the pull-down list for the other field.*

> This filtering should reduce the selection of inappropriate entries, and gives the user a smaller, more relevant list of choices. If a user needs to display the unfiltered pull-down lists, they can delete the contents of either field, or use the Refresh Index Lists option under the Tools menu.

> {\* The contents of each pull-down list can be fine-tuned by setting the Status field (#4) in files 2005.83, 2005.84, and 2005.85. When Status = Active (Active is the default value), the related index value is present in the appropriate pull-down list. If Status is set to Inactive, the related index value is not available as an option.}

## Hold Value Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option enables user to ‘hold’ Image information for successive captures of images/Image Groups thus avoiding the need to reenter information that remains constant for a series of images / Image Groups. Open Hold Value window clicking Configurations \| Select Hold Values option.

> Click in the box to the left of the field that is to be retained. All fields that are not checked will be cleared after each image is captured.

> ‘Hold Value’ Feature

![](vista-imaging-system-clinical-capture-user-manual/074.png)

> Hold Value can be used for any input field in the left side of the Capture window, even those fields that are not directly entered by the user.

> You can turn Hold Value on or off by:

- checking or clearing the check box the particular field in the 'Hold Values’ window,
- right-clicking a particular field on the main Capture window, or

> When Hold Value is active for a particular field, a push pin icon appears next to the field.

> See image below.

> ![](vista-imaging-system-clinical-capture-user-manual/075.png)

> When Hold Value is turned on for a field:

- The value for that field will be retained until it is explicitly changed by the user.
- If a field containing patient-specific information is ‘held’, and the patient is changed, the field will be updated with the new information, but the Hold Value option will remain active.

> NOTE: Hold Value settings are cleared when a user exits the Capture application unless they have saved the settings as a configuration button.

# Patient Only Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Click the Association button and select one of the three options available under Patient Only: Clinical, Photo ID or Administrative as shown in the following image.

![](vista-imaging-system-clinical-capture-user-manual/076.png)

> Images with Patient Only association are not associated with any Packages. When Clinical option is selected under association, Study Performed changes to CLIN on the left side of the Capture Screen. ![](vista-imaging-system-clinical-capture-user-manual/077.png)

> Also NOTE that the images with Patient Only Association can be displayed through Clinical Display but NOT referenced in CPRS.

# Administrative Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Administrative documents can be scanned using the Administrative association.

1.  Select a Patient by clicking the 'Select Patient' button.
2.  Select the type of administrative document to be scanned from the list. For example, MEANS TEST may be selected.
3.  Enter the document's date such as 12/14/2001 or T for today’s date.

> The Image Description will say MEANS TEST (10-10EZ) or whatever Document type was selected from the pull-down list. The description may be edited.

![](vista-imaging-system-clinical-capture-user-manual/078.png)

1.  Place MEANS TEST document on scanner.
2.  Click the capture button to begin scanning.
3.  Check the 'MultiPg Doc' box if you wish to use the automatic document feeder on your scanner. Leave this box unchecked if using the flatbed scanner.
4.  Click the capture button to begin scanning.
5.  The scanned image will appear on the right side.

> If you have the menu item Options\| Show Configuration Messages checked, you will be asked to confirm the save settings. NOTE: This setting is saved as a user preference.

![](vista-imaging-system-clinical-capture-user-manual/079.png)

6.  Click the OK button to confirm.

# Attaching Documents to Notes or Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the Association ![](vista-imaging-system-clinical-capture-user-manual/080.png) value in the configuration settings bar displays a VistA package—such as Medicine, Progress Notes (TIU), or Surgery—you will need to select a VistA report or progress note to “attach” the scanned document to.

![](vista-imaging-system-clinical-capture-user-manual/081.png)

> The steps used to select progress notes or reports vary based on the package that the note or report is stored in. Detailed steps for each package are covered in the following subsections.

## Selecting a Progress Note (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  After Selecting a Patient, choose option Progress Note after clicking the Association button in the configuration settings toolbar. Click OK.

![](vista-imaging-system-clinical-capture-user-manual/082.png)

Once Progress Note Association is selected, Association value displays TIU as shown below.

![](vista-imaging-system-clinical-capture-user-manual/083.png)

2.  Click ![](vista-imaging-system-clinical-capture-user-manual/084.png) button located on the left side of the Capture window. The Progress Notes window will open.
3.  In the list of progress notes for the current patient, click the note that you want to associate with the scanned document.
4.  Click OK. The Progress Notes window will close.
5.  Verify that the left side of the Capture window shows appropriate values in the Study Performed, Note Date, and Image Description fields. For information on entering values in the other fields, see the <span id="_bookmark55" class="anchor"></span>*[Image Index Guidelines](\l)* section.

#### Progress Note, Discharge Summaries, Clinical Procedures List

> To open Progress Notes window:

1.  In the Clinical Capture main window, select a patient.
2.  Click the Select Progress Note button in the left pane. The Progress Notes window displays.

![](vista-imaging-system-clinical-capture-user-manual/085.png)

> The Progress Notes window lists progress notes, discharge summaries and clinical procedures.

> You use this window to:

- View the notes for the selected patient
- Create new progress notes for the selected patient. For information about the procedure, see the *[Create New Progress Notes](#create-new-progress-notes)* section.
- Enter addendums to progress notes and assign status to progress notes. For information about the procedures, see the section *Creating an Addendum for Progress Notes*.

> By default, the Progress Notes window shows the last 25 signed notes for the patient. You can display more notes by clicking the More button (display option), which is available if the patient has more than 25 signed notes. You can use the other buttons above the list of notes to customize the display of the data in the Progress Notes window. Each button is a display option and a toggle switch. When you click the button, it becomes active (selected). When you click it again, the button becomes inactive.

- Preview – When this button is selected, the lower part of the window displays the content of the selected progress note.
- My Notes – When this button is selected, only the progress notes created by you (the user who is logged on) are displayed.
- Signed – When this button is selected, signed progress notes are displayed.
- More – Clicking this button displays more notes in the window (in batches of 25).
- UnSigned – When this button is selected, unsigned notes are displayed.
- UnCosigned – When this button is selected, un-cosigned notes are displayed.
- By Author… – This button allows you to display notes only by a specific author. Clicking the button opens a dialog box in which you can select the user whose notes you want to display.

## Configuring the Default Display Preferences for Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can specify the default display options for the progress notes in the Progress Note List Options window, which is illustrated in the following image.

![](vista-imaging-system-clinical-capture-user-manual/086.png)

#### To configure the default display options for progress notes:

1.  In the Progress Notes window, click the menu: Options\| List Options…
2.  In the Progress Note List Options window that displays, modify the current options as desired. You can specify the following parameters:
    - Number of Signed Notes to Return – Specifies the number of signed notes that are displayed in the window.
    - Select Date button – Specifies the starting date for the notes that are displayed.
    - Progress Note Listing – Select the Display Status Icons in list checkbox if you want the notes list to show an icon indicating their status.
    - Note information (main window) – Select the Display Note-Status Icons in list checkbox if you want the notes to show an icon indicating their status in the main window. The icon displays next to the note status in the Note-Status-Loc field. ![](vista-imaging-system-clinical-capture-user-manual/087.png)

![](vista-imaging-system-clinical-capture-user-manual/088.png)

3.  When done, click OK to save your changes.

#### Creating an Addendum for Progress Notes

> You can add an ‘addendum’ to an existing signed (or electronically filed) progress note. An addendum inherits many of the properties of its parent note. However, it has its own status and can have its own text and/or attached image.

> The use of addenda is optional.

#### To create an addendum:

1.  Open the Progress Notes window and click the Select Note tab.
2.  Select the note to which you want to add the addendum.
3.  Click the Make Addendum checkbox on the right side of the dialog box. (This checkbox does not appear when unsigned notes and addendums are selected. )

![](vista-imaging-system-clinical-capture-user-manual/089.png)

4.  Enter the addendum text and select the status to be applied to the addendum when the image capture is complete.

> Existing addenda *for signed notes*, if present, can be shown or hidden using the View \| Show Related Notes Addendums option in the Progress Notes window.

> ![](vista-imaging-system-clinical-capture-user-manual/090.png)When addenda are hidden, a + sign indicates if a note has an addendum. When addenda are visible each addendum is listed under its related note.

> NOTE that when addenda are displayed:

- Column sorting is disabled.
- Signed or unsigned notes can be displayed, but not both at the same time.
  - When unsigned notes are displayed, sorting is based on the date of the unsigned note or the date of any of that note’s unsigned addenda.
  - When signed notes are displayed, sorting is based on the date of the signed note (the date of any addenda are not considered).
  - For the purposes of sorting, electronically filed notes are considered signed.

#### Create New Progress Notes

> You can create a new progress note in Capture, to reduce the need to switch back and forth from CPRS.

#### To create a new note:

1.  In the Clinical Capture main window click the Select Progress Note button.
2.  In the Progress Notes window that displays, click the Create New Note tab.

![](vista-imaging-system-clinical-capture-user-manual/091.png)

3.  In the Author box, change the author of the note, if necessary.

> Tip: Entering the first few characters will display a list of all entries that match these characters.

> ![](vista-imaging-system-clinical-capture-user-manual/092.png)

4.  Select the location of the visit from the Visit Location list .
5.  The Note Status area allows you to indicate what the status of the note should be set to *once the image capture is complete*. For more details about setting a note’s status see the *[Sign or Electronically File Progress Notes](\l)* section.
6.  The Enter Text box can be used to enter text for the note. Boilerplate text, if defined, may be present already. (Templates, however, are not implemented. To work with a template, the note must be created using CPRS.)
7.  The note title area can be populated by selecting a note from the scroll list, or by entering the first few characters of the note title (which causes a clickable list of matching note titles to display).

#### Sign or Electronically File Progress Notes

> You can assign a status to a progress note directly from Capture. To do this, open the Progress Notes window, and then select an existing note or create a new note. Then click an option in the status area indicating what the status of the note should be.

> ![](vista-imaging-system-clinical-capture-user-manual/093.png)

- When Un-Signed is selected, the note status is not changed when the capture is complete.
- When Signed is selected, the user will be prompted to enter a signature after completing the image capture, and the note’s status is updated automatically.
- When the Electronically Filed option is selected, the note is considered ‘closed’ when the capture is complete—no signature is needed. This option should be used for notes/scanned documents (such as consent forms) that do not require a clinician’s signature. The Electronically Filed option is only visible to users that have the security key, MAG NOTE EFILE. Only users who have this new key can set a note’s status to Electronically Filed.

#### Attaching a Scanned Document to Different Author’s Progress Note

> A site may elect to scan documents and attach them to Progress Notes. There are various ways to attach documents to progress notes.

> There are two ways to save the attachments as Single or Study/Group this example is for a Single Capture. Study/Group has an extra button in the Capture window.

#### To attach a document or an image to a note that alerts the provider that he/she has an unsigned note:

1.  Logon to VI capture/select the patient if running as a standalone system.
2.  Click the configuration button created for the particular capture type.

> Some index fields will be filled in depending on how the configuration button was created.

> The capture staff will determine what fields need to be filled in.

> ![](vista-imaging-system-clinical-capture-user-manual/094.png)

3.  Click the Select Progress Note button.
4.  Under the Create New Note tab:
    1.  Change the Author by typing in a few initials of the last name, all matching entries are listed.
    2.  Select the Visit Location.
    3.  Select the New Note Status.
    4.  Select the note TITLE.
    5.  Click the OK button.

![](vista-imaging-system-clinical-capture-user-manual/095.png)

5.  On the main Capture window the Note Date and Document Image Date will need to be filled in; and are based on site policy, (could be date of service, date of scan, date of order etc.…) both fields could have the same date or different dates.
6.  Click the Capture button.

> The item scans and is viewable in the capture window. Use the tools for best view.

7.  Click the Image OK button.

> A confirmation window displays on the screen

8.  Click Image OK ![](vista-imaging-system-clinical-capture-user-manual/096.png) or Cancel (if you click cancel the document is removed from the screen and you can re-scan), if you click OK and it is a Single Saved Capture the document will be saved.

> The provider will get an Alert in CPRS that they have an unsigned note.

> Until the provider signs the note other users will not be able to see the attached document. The exception being if the site has setup specific business rules to allow others to view images when there is an unsigned note.

#### Progress Notes Window Options

## Filtering Options for Select Progress Note List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the button bar used to filter the list of available Progress Notes, the Signed, Unsigned, and UnCosigned buttons can be used in any combination.

![](vista-imaging-system-clinical-capture-user-manual/097.png)

## Preferences for Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can customize aspects of the Progress Notes window such as the number and start date of notes to retrieve, and whether or not to use status icons in the notes listing and in the main Capture window. The user selects a number of signed notes to return and a start from date, then clicks the OK button. The selected number of notes starting from the start from date and going backward (newest notes are first) will be listed in the Progress Notes list. The Progress Notes List Options window limits the list of Notes retrieved from the VistA system to 100. Only the predefined counts of 25, 50 and 100 can be entered into the edit box. The user must click one of

> the predefined buttons to populate the edit box. Only a start from date needs to be selected by the user.

> The Progress Note List Options dialog box can be accessed from the Progress Notes window by clicking Options \| List Options. The Sign Note option is available from

> the Options menu. You can also use the My Notes button to list only your own notes.

![](vista-imaging-system-clinical-capture-user-manual/098.png)

> Note Listing Status Bar

> The status bar displays the total number of notes listed, the counts of each selected status, the total number of notes listed, and the selected start date. The user can click the <u>Start from Date</u> link to select a new date. When the More button is clicked, 100 additional notes will be added to the end of the list. The date range that is displayed will change to match the current list of notes. If all TIU Notes for a patient have been listed, the More button will be disabled (greyed out).

> The information panel below the More button describes:

- The number of notes currently listed
- The start from date
- The date of the last TIU note in the list

> ![](vista-imaging-system-clinical-capture-user-manual/099.png)

#### Consults

> If the Title of the new Note is a ‘Consult’ title VistA Imaging will display a list of Patient Consults and require that the user make a selection.

#### ![](vista-imaging-system-clinical-capture-user-manual/100.png)

#### Consult Select Window

> The Cons \# column displays the Consult ID of the consult. The list of consults is also sorted by the Cons \# column. The user can click the column header of any column to sort the list by entries in that column.

> The Consult is marked as “Complete” when:

1)  The Image Capture process is successful, and
2)  The resulting status of the Note is 'Complete' by signing, or electronically filing the Note.

> NOTE: If the title selected is Consult Title and the patient selected does not have any consults, a message dialog indicating the patient does not have any consults will be displayed.

## Show Related Notes / Addendums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vista-imaging-system-clinical-capture-user-manual/101.png)

> When the menu option View\|Show Related Notes/Addendums is selected, all signed notes and the addendums related to the signed notes are displayed in a ‘Tree Style’ list. Addendums are listed directly under the note and are indented. Unsigned notes are displayed in a separate pane.

![](vista-imaging-system-clinical-capture-user-manual/102.png)

> When the menu option Show Related Notes/Addendums is not checked, a list of completed Notes for the patient are displayed sorted by date.

> When the Show Related Notes/Addendums option is checked, sorting of the columns is disabled.

#### Workload Credit

> Users of VistA Imaging Capture can create new Notes to associate with captured images (scanned or imported images/ documents). By default, the visit status of new notes created in VistA Imaging Capture is set to 'Historical'. This ensures that the visit is not used for workload credit.

#### Historical visit

> Historical visit status is used for documenting a visit that occurred sometime in the past (exact time may be unknown) or at some other locations (possibly non-VA) and is not used for workload credit, they can be used for setting up the reminder maintenance system.

- By default, visit status *via VistA Imaging Capture* is set to historical. This ensures that the visit is not used for workload credit for documents captured.

> Frequently Asked Questions

> The scanning FAQ document is posted on the HIM website under "Document Scanning" at <u>REDACTED</u> .

> The document scanning webpage also contains links to scanning websites, examples of position descriptions/standards and examples of policies and procedures.

## Progress Note Icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section explains some of the icons that are used for actions related to progress notes and to the status of progress notes.

- ![](vista-imaging-system-clinical-capture-user-manual/103.png)![](vista-imaging-system-clinical-capture-user-manual/104.png)Create New Note ![](vista-imaging-system-clinical-capture-user-manual/105.png) Used when creating a new note.
- Make Addendum Used when adding an addendum to a selected note.
- Completed Note Indicates that the status of the selected note is completed.
- Unsigned Note![](vista-imaging-system-clinical-capture-user-manual/106.png) Indicates that the status of the selected note is unsigned..

> The intended status of a note can be:

- ![](vista-imaging-system-clinical-capture-user-manual/107.png)Signed ( )
- ![](vista-imaging-system-clinical-capture-user-manual/108.png)Electronically Filed ( ) or
- Unsigned (![](vista-imaging-system-clinical-capture-user-manual/109.png) )

## Selecting a Surgical Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgery Case List is used to select a case to be associated with the captured images. After Selecting a Patient, choose option Surgery after clicking the Association ![](vista-imaging-system-clinical-capture-user-manual/110.png) button in the configuration settings toolbar. Click OK.

> ![](vista-imaging-system-clinical-capture-user-manual/111.png)

> ![](vista-imaging-system-clinical-capture-user-manual/112.png)Click the button located on the left side of the Capture window.

> Select the case to be associated with the documents you will be scanning.

> ![](vista-imaging-system-clinical-capture-user-manual/113.png)

> The Surgery Case List is used to select a case to be associated with the captured images. Select an entry from the list and click the 'OK' button. See image below.

> The Surgery Case List box will close.

#### Notes:

> The widths of the columns can be changed by selecting the column dividers and dragging them to the left or right. There are alternate ways to select a Surgery Case from the list.

> See Import Image Directory.

> If there are no Surgery Cases associated with the selected Patient, a warning message is displayed as shown below.

> ![](vista-imaging-system-clinical-capture-user-manual/114.png)

## Select Directory of Images to Import

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Imaging Capture is in 'Import Mode' when 'Import' has been selected as the input Source. In Import Mode, the directory from which images are to be imported must be selected.

> Open the 'Select ‘All files’ in Directory (or Selected Images)' window, using one of the following options:

- Clicking the folder ![](vista-imaging-system-clinical-capture-user-manual/115.png) button in the left frame of the capture window.
- Selecting the menu option '*Options*\|*Import* Directory'

![](vista-imaging-system-clinical-capture-user-manual/116.png)

- Click the Import directory that is displayed, or right-click the Import directory file list and select “Select Files to Import” Option.

![](vista-imaging-system-clinical-capture-user-manual/117.png)

- Select the Drive, Directory and file mask (\*.TIF). The images in that directory matching the mask will be displayed in the file list box.
- When the 'Open' button is clicked, the image files will be redisplayed in the Import directory file list box on the Main Capture window.

> ![](vista-imaging-system-clinical-capture-user-manual/118.png)

![](vista-imaging-system-clinical-capture-user-manual/119.png)

#### Notes:

> The images displayed in the file list box in this window are for display purposes only. Images aren't selected from this window, just the directory.

> If 'Save as default' is checked, the Drive, Directory and file mask will be saved by the system and used as defaults the next time this window is opened.

> File mask or file filters are used to limit which files will be displayed in the file list box. The most familiar mask is '\*.\*'. This will display all files. Alternate masks can be typed, or selected from the list.

> Verify that the left side of the Capture window shows appropriate values for Study Performed, Case Date, and Image Description. For information on entering values in the other fields, see the *[Image Index Guidelines](#_bookmark55)* section.

## Selecting a Radiology Exam

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After Selecting a Patient, choose option Radiology by clicking the Association ![](vista-imaging-system-clinical-capture-user-manual/120.png) button in the configuration settings toolbar. Click OK.

![](vista-imaging-system-clinical-capture-user-manual/121.png)

> Click the ![](vista-imaging-system-clinical-capture-user-manual/122.png) button located on the left side of the Capture window. Select the procedure that you want to associate with the documents you will be scanning, then click OK.

![](vista-imaging-system-clinical-capture-user-manual/123.png)

> Verify that the left side of the Capture window shows appropriate values for Study Performed, Exam Date, Case Number, and Image Description. For information on entering values in the other fields, see the *[Image Index Guidelines](#_bookmark55)* section.

## Selecting a Laboratory Specimen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After Selecting a Patient, choose option Laboratory after clicking the Association ![](vista-imaging-system-clinical-capture-user-manual/124.png) button in the configuration toolbar. Click OK.

![](vista-imaging-system-clinical-capture-user-manual/125.png)

1)  Click the ![](vista-imaging-system-clinical-capture-user-manual/126.png) button located on the left side of the Capture window.

![](vista-imaging-system-clinical-capture-user-manual/127.png)

> Note: If selected lab is for a different patient then the patient in the main capture window changes to match the selected lab.

2)  Click the arrow next to the Section list, and select the section that you want to display a list of lab specimens for. Then enter the accession year and number in the Accession Year and Number boxes.
3)  Click Search. A list of specimens for the section you selected will be displayed.
4)  Select specimen, then click OK. The Anatomic Pathology Lab selection window will close.
5)  Select a value for the Objective field (use “1” if there is no applicable objective).
6)  Select a value for the Stain field (use “NONE” if there is no applicable stain).
7)  Verify that the left side of the Capture window shows appropriate values for the lab-related fields, Study Performed, Specimen Date, Accession No., and Image Description.

## Selecting a Medicine Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After Selecting a Patient, choose option Medicine after clicking the Association ![](vista-imaging-system-clinical-capture-user-manual/128.png) button in the configuration toolbar. Click OK.

![](vista-imaging-system-clinical-capture-user-manual/129.png)

> You can either select an existing medical procedure, or create a new medicine procedure.

#### Selecting an Existing Medicine Procedure

> The screenshot of the Medicine Procedure/Subspecialty window is below.

![](vista-imaging-system-clinical-capture-user-manual/130.png)

> To select an Existing Medicine Procedure follow the steps below:

1)  Click the ![](vista-imaging-system-clinical-capture-user-manual/131.png) button located on the left side of the Capture window. The Medicine Procedure/Subspecialty dialog will open.
2)  Double-click a Procedure/Subspecialty.
3)  Then click to select a Procedure/Subspecialty Date/Time
4)  Click OK or double-click the procedure to choose. The Medicine Procedure/Subspecialty list will close.
5)  Verify that the left side of the Capture window show appropriate values for Study Performed, Procedure Date, and Image Description. For information on entering values in the other fields, see the *[Image Index Guidelines](#_bookmark55)* section.

#### Notes:

- The Procedure/Subspecialty will remain selected when this window is opened again.
- The Procedure/Subspecialty list can be limited to certain procedure types based on assigned ‘Imaging Capture keys'. In the Selection area located near the bottom of the dialog, click the second option.

#### Creating a New Medicine Procedure

> Shown below is a screenshot of the Medicine Procedure/Subspecialty list window.

![](vista-imaging-system-clinical-capture-user-manual/132.png)

> After Selecting a Patient, choose option Medicine after clicking the Association ![](vista-imaging-system-clinical-capture-user-manual/133.png) button in the configuration toolbar. Click OK.

> ![](vista-imaging-system-clinical-capture-user-manual/134.png)

> ![](vista-imaging-system-clinical-capture-user-manual/135.png)Click the button located on the left side of the Capture window. The Medicine Procedure/Subspecialty List dialog will open.

#### Create New Procedure for Selected Subspecialty

- To create a new procedure, before the image is saved.
- The current date/time is used for the procedure.
- Click in the box to Create 'NEW' procedure now, or the procedure is created when clicking the OK button on the main capture window.

> In the list on the left side of the window, select the specialty for the procedure that you are creating.

> NOTE: Depending on the Security Keys assigned to user, some procedures may or may not be visible.

> In the Selection area located near the bottom of the dialog, click the first option and Click OK.

> The Medicine Procedure/Subspecialty list will close, and the new medical procedure will be created.

> Verify that the left side of the Capture window show appropriate values for Study Performed, Procedure Date, and Image Description. For information on entering values in the other fields, see the *[Image Index Guidelines](#_bookmark55)* section.

## Selecting a Clinical Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After Selecting a Patient, choose option Clinical Procedure after clicking the Association ![](vista-imaging-system-clinical-capture-user-manual/136.png) button in the configuration toolbar. Click OK.

![](vista-imaging-system-clinical-capture-user-manual/137.png)

> Click the ![](vista-imaging-system-clinical-capture-user-manual/138.png) button located on the left side of the Capture window, just below the patient’s name. The Clinical Procedure Requests window will open.

![](vista-imaging-system-clinical-capture-user-manual/139.png)

> Select the Clinical Procedure you want to associate with the image you are capturing. Select one of the three Capture Action options near the bottom of the dialog (see explanation below).

#### Capture Action

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select</strong></th>
<th><strong>If the following is true</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A consent form is being scanned and attached to this procedure.</td>
<td><p>The scanned document is a consent form. ‘CONSENT’ will be added to the Image Description field. (Additional instrument results can still</p>
<p>be linked to the procedure request later).</p></td>
</tr>
<tr class="even">
<td>This procedure will NOT be receiving a report or additional information from the instrument.</td>
<td>The scanned document is the last image to be captured before the associated note is signed.</td>
</tr>
<tr class="odd">
<td>This procedure will be receiving a report or additional data from the instrument.</td>
<td>There will be additional images or report files added to this procedure. A staff member will use the CPUser software to identify these reports before the associated note is signed.</td>
</tr>
</tbody>
</table>

> After choosing the appropriate option, click the OK button.

> If the Visit Listing box displays, select a date from the Visit list, or enter a new visit date in the New Visit Date/Time box. Then click OK to close the Visit listing box.

> Click OK when finished.

> After selecting a clinical procedure, verify that the left side of the Capture window shows appropriate values for Study Performed, Procedure Date, and Image Description.

## Selecting a TeleReader Consult

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In the Clinical Capture application window, click the Association button (below the menu bar) to associate your captured image(s) with a service or specialty.

> Note: You can also create and click a configuration button to associate a captured image to a TeleReader Consult.

![](vista-imaging-system-clinical-capture-user-manual/140.png)

> The Select Image Association dialog box is displayed.

> Important: The options should be enabled as shown. If they are disabled (grayed out), contact your system administrator to configure your setup properly.

![](vista-imaging-system-clinical-capture-user-manual/141.png)

2.  Select the TeleReader Consult option (clicking OK is not necessary when the close on select checkbox is selected, as shown).

> Note: When TeleReader Consult is selected in the Select Image Association dialog box, the Import option is selected in the Select input source dialog box and “Convert to DICOM” is displayed in place of “Copy to Server”.

> ![](vista-imaging-system-clinical-capture-user-manual/142.png)

3.  Select the appropriate patient

> The patient’s photo, name, patient ID number, and Social Security number are displayed.

4.  Click the Saving button (below the menu bar).

> In the Saving as window displayed, select Study (Group) or Single Image (clicking OK is not necessary when the close on select checkbox is selected, as shown).

![](vista-imaging-system-clinical-capture-user-manual/143.png)

5.  Click the Select TeleReader Consult button now displayed.

![](vista-imaging-system-clinical-capture-user-manual/144.png)

> The TeleReader Consult Requests window is displayed.

> ![](vista-imaging-system-clinical-capture-user-manual/145.png)

6.  Select the consult request that you are using to associate with the images and click OK. In the Capture window, the consult date is filled in. The service (Teledermatology in this example) populates the fields for Study Performed and Image Desc.

![](vista-imaging-system-clinical-capture-user-manual/146.png)

7.  Select the appropriate data for the Doc/Image Date and Origin fields.
8.  Select IMAGE or CONSULT for the Doc/Image Type field.
9.  Select the appropriate data for the Specialty and ProcEvent fields.
10. Click the Select Value button next to the DICOM data field.

> The DICOM Header Data Entry window is displayed.

![](vista-imaging-system-clinical-capture-user-manual/147.png)

11. Select data for the fields for Body Part Examined and Laterality, and click Save.

> The image is converted to a DICOM file format (\*.dcm file).

12. In the lower left list box, import the photo(s) in one of two ways:

> Important: The photos must be uncompressed JPEG or TIFF files.

- If you are uploading the photos to a drive, click the Select Files to Import icon shown, navigate to that drive and select it to make all the photos available.

![](vista-imaging-system-clinical-capture-user-manual/148.png)

- Or, copy all the photos to the default C:\Program Files\VistA\Imaging\import folder shown.

> All the imported files are displayed in the lower left pane.

# Image Index Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All captures are indexed. The capture window has various index fields that can be filled in manually or saved as part of a configuration. Fields that have an asterisk to the left of the Index field title are required and must be filled in for the document/image to be saved.

## Indexing Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is essential that scanned documents are properly indexed (categorized) so they can be easily retrieved in the future. The following sections explain how this is done for scanned documents.

> *Entering the Date and Origin*

> *Entering ‘Type,’ ‘Specialty,’ and ‘Proc/Event’ Values Entering Image Descriptions*

> NOTE: Additional fields will be present for documents that are attached to Radiology or Lab reports. Values for these fields are selected as described below.

## Entering Date and Origin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a scanned document is attached to a progress note or report, the Capture program will automatically use the date of the progress note or report. However, if the scanned document is to be linked directly to a patient, you will need to enter the date manually.

> The Origin field, which indicates if the document is an internal VA document or if it is from an external source, will default to VA.

> To enter the date and set the document origin Use the mouse or the Tab key to select the Document Date field. (Depending on your configuration settings, this field may appear as the “Doc/Image Date” field.)

> Type the date in MM/DD/YY format. Enter the date that the document was created or signed (not the date the document was scanned). The scanning date is saved automatically.

> If you need to change the value for Origin, select the Origin field, and choose the appropriate value from the pull-down list.

## Entering ‘Type,’ ‘Specialty,’ and ‘Proc/Event’ Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Type, Specialty, and Proc/Event fields will typically need to have values selected by the user. (If “Patient (Admin)” is selected as part of the current capture configuration, the Specialty and Proc/Event fields will not be present.)

> These fields may also have pre-defined values specified as part of the active capture configuration. Pre-defined values can be changed if needed.

> To set Type, Specialty, and Proc/Event, select the field you want to enter a value for.

> A value must be present in the Type field to complete a capture. Values for Specialty and Proc/Event should be set according to the policies at your site.

> If are you not sure which values should be entered for these fields, contact your Clinical or Imaging Coordinator for guidance.

> Use the pull down list to select a value appropriate to the document being scanned. You can choose a value by:

- Clicking the arrow to open the pull-down list, and then clicking a value.
- Typing the first letters for the value you want to select. Matching values will be displayed automatically. When the desired value is displayed, press Tab to move to the next field.

## Entering Image Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Capture program provides two areas where descriptions can be entered: the Image Description field and the Long Image Description field.

- The Image Description field will have a value automatically added when you select a progress note or report. If there is no progress note or report selected for the scanned document, the Image Description field will automatically have a value added when you select a Document/Image Type.
- The Long Image Description field is a free text field that can be used to record additional information about a scanned document. The contents of both of these fields can be edited by clicking them with the mouse, and then typing the information you want to enter.

# Image Capture Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section explains how a document is actually scanned using the Capture program. Please note that the setup at individual sites may alter how scanning is performed.

> NOTE: If you are scanning several documents with similar characteristics, use the Hold Value feature.

> Documents can be scanned as single images, single or multi-page PDF. The method you should use depends on the type of scanner and on the scanning procedures at your site.

## Scanning Documents as a Single Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify that the patient referenced on the document to be scanned matches the current patient shown in the Capture window.
2.  ![](vista-imaging-system-clinical-capture-user-manual/149.png)Verify that Single is shown in the Capture window configuration bar.

> When the Single option is selected, the document will be saved as a Single Image. If the Single option is not selected, click the Saving button to change the option to Single.

3.  Place the document to be scanned into the scanner’s feeder or onto flatbed.
4.  If the document has several pages, and if you are using a scanner equipped with a document feeder, verify that the MultiPg Doc. checkbox is checked. This will allow you to scan all pages in the document into a single image file. Click Capture![](vista-imaging-system-clinical-capture-user-manual/150.png) or press ALT+C to begin scanning.
5.  If the TWAIN window opens, you can accept the current scanning parameters by clicking Scan, or you can alter the settings (such as page size), and then click Scan.
6.  ![](vista-imaging-system-clinical-capture-user-manual/151.png)When the scanned document is displayed on the right side of the Capture window, check the quality of the image.
7.  Use the scroll bars and the Zoom slider to ensure that all text is visible and legible. If needed, use the DeSpeckle tool ![](vista-imaging-system-clinical-capture-user-manual/152.png) to remove stray pixels (black dots) from the image.
8.  If the image is rotated or upside down, use the orientation buttons to correct the problem. If the image is slightly crooked, use the DeSkew ![](vista-imaging-system-clinical-capture-user-manual/153.png) button to straighten the image.
9.  Click to flip or rotate image vertically![](vista-imaging-system-clinical-capture-user-manual/154.png).
10. Click to flip or rotate image horizontally ![](vista-imaging-system-clinical-capture-user-manual/155.png)
11. If the image is a multi-page document, use the paging controls to check each page.
12. If image quality is acceptable, click Image OK or press ALT+K.
13. If the image is NOT acceptable, click Cancel or press ALT+L, then re-scan the image.

## Scanning Multiple-Page TIFFs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can scan multiple pages as TIFFs or PDFs. This section describes the steps of scanning multiple-page TIFFs. For more information about scanning multiple pages as PDFs, see the section <span id="_bookmark63" class="anchor"></span>[*Scanning to PDF*](\l).

#### To scan multiple pages as TIFFs:

1.  Select the Source settings button ![](vista-imaging-system-clinical-capture-user-manual/156.png) in the Capture main window. The Imaging workstation configuration window opens.
2.  In the Source/Format tab of the Imaging workstation configuration window, do the following:
    1.  Select Scanned Document or Twain window.
    2.  Select the MultiPg Doc. checkbox.
    3.  Select Document (1 bit TIF G4 FAX).

![](vista-imaging-system-clinical-capture-user-manual/157.png)

3.  Click the OK button ![](vista-imaging-system-clinical-capture-user-manual/158.png)to return to the Capture main window.
4.  Click the Capture button ![](vista-imaging-system-clinical-capture-user-manual/159.png) on the Capture main window.
5.  If you want to add more images to the current scan, select

#### Options \| Combine TIF Scans.

6.  Repeat the previous step for each additional image you want to add to the current scan.
7.  Click the Image OK button ![](vista-imaging-system-clinical-capture-user-manual/160.png) to save the scan.

## Scanning to PDF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Clinical Capture allows you to scan color or black and white images and save the image as a multipage PDF.

> Scanning to PDF is useful because it lets you:

- Reduce the size of the scanned files by converting them to PDF. PDFs are much smaller than uncompressed TIFF files, which take a lot of storage space and take longer to transport over the network.
- Add pages to the current scan by selecting Combine PDF from the Options menu. This feature lets you resume scanning if there was a paper jam without having to start all over again.

#### To scan to PDF:

1.  Select the Source settings button ![](vista-imaging-system-clinical-capture-user-manual/161.png) in the Capture main window. The Imaging workstation configuration window opens.
2.  In the Source/Format tab of the Imaging workstation configuration window, do the following:
    1.  Select the PDF (Adobe Document) checkbox.
    2.  Select True Color (24-bit JPG).
    3.  Select the MultiPg Doc. checkbox.

> ![](vista-imaging-system-clinical-capture-user-manual/162.png)

> The Capture button becomes Capture (PDF) and the Review button becomes available.

![](vista-imaging-system-clinical-capture-user-manual/163.png)![](vista-imaging-system-clinical-capture-user-manual/164.png)

3.  Click the OK button to return to the Capture main window.
4.  Click the Capture PDF button on the Capture main window.
5.  If you want to add more images to the current scan, select

#### Options \| Combine PDF Scans.

6.  Repeat the previous step for each additional page you want to add to the current PDF.
7.  If you want to open the PDF in a separate Adobe Acrobat Reader window, click the

> Review button ![](vista-imaging-system-clinical-capture-user-manual/165.png).

> The PDF opens in a separate window allowing you to view the entire file and to use the Acrobat Reader navigation controls to page through the PDF before saving it.

8.  If you are satisfied with the result, click the Image OK button ![](vista-imaging-system-clinical-capture-user-manual/166.png) to complete the scan and save the PDF.

## Image Quality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When the scanned document is displayed on the right side of the Capture window, check the quality of the image.
- Use the scroll bars (not shown) and the Zoom slider to ensure all text is visible and legible. If needed, the DeSpeckle tool can be used to remove stray pixels

> (black dots) from the image, by clicking the DeSpeckle Button ![](vista-imaging-system-clinical-capture-user-manual/167.png) above the image captured.

- Drag to zoom in/out Click to remove "noise".
- ![](vista-imaging-system-clinical-capture-user-manual/168.png)![](vista-imaging-system-clinical-capture-user-manual/169.png)![](vista-imaging-system-clinical-capture-user-manual/170.png)![](vista-imaging-system-clinical-capture-user-manual/171.png)If the image is rotated or upside down, use the orientation buttons to correct the problem. If the image is slightly crooked, use the DeSkew ![](vista-imaging-system-clinical-capture-user-manual/172.png) button to straighten the image.
- Click the button to flip image vertically.
- Click the button to flip image horizontally.
- Click the button to rotate image left or counter-clockwise.
- Click the button to rotate image right or clockwise.
- If the image is a multi-page document, use the paging controls to check each page. Correct any problems found.
- If the image is NOT acceptable, click ![](vista-imaging-system-clinical-capture-user-manual/173.png) or press ALT+L, then re-scan the image. If image quality is acceptable, click Cancel ![](vista-imaging-system-clinical-capture-user-manual/174.png) or press ALT+K.

# Image Annotation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Annotations are no longer created in the Clinical Capture application. The user of the Clinical Capture client will have the option to automatically open the captured image in a separate window of Clinical Display for annotation.

> The user will also have an option to select an image from the Latest Patient Images window, and have that image open in a window of Clinical Display.

> The option to automatically/manually open images for annotation in Clinical Display became available with Clinical Display Patch 167. The Clinical Capture client will communicate with the Clinical Display client by sending windows messages to the Clinical Display client.

> Note: Until Clinical Display Patch 167 is installed, the user will have to manually open the image from the Display client for annotation.

# Completing Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging Capture Window can use a number of different capture mechanisms to acquire images:

- [*Import File from Workstation*](\l)
- [*Scan Document or Color Picture*](\l)
- [*Meteor/Orion Imaging Boards*](\l)
- [*Digital and Still Video Camera Input*](\l)

> Once an Image has been captured, VistA Imaging will display the image in the Display area and enable the 'Image OK' ![](vista-imaging-system-clinical-capture-user-manual/175.png) and 'Cancel' ![](vista-imaging-system-clinical-capture-user-manual/176.png) buttons. The image manipulation buttons are also available if required.

> If the captured image is not the correct image or not of good quality, click the 'Cancel' ![](vista-imaging-system-clinical-capture-user-manual/177.png) button to discard the image.

> If the Image is correct and the quality is good, click the 'Image OK' ![](vista-imaging-system-clinical-capture-user-manual/178.png) button.

## Scan Document or Color Picture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Requirement: All document scanning must be at a minimum of 300 x 300 dpi. VistA Imaging can acquire images from TWAIN devices including:

> • ,

- TWAIN-compliant document scanners still/video cameras
- If 'TWAIN Capture - Twain Window' is selected as the input source, another window will open when 'Capture' is clicked. This is the TWAIN Window for the TWAIN device. Each TWAIN Device has its own TWAIN Window and TWAIN Image Types.
- In the TWAIN Window, TWAIN image type and other image parameters need to be selected. Click on the prescan and/or scan buttons to perform the scan. The image will be passed to the Image Box of the VistA Imaging Capture Window for approval.

> Please see the device manual for image adjustments and other details.

## Meteor/Orion Imaging Boards

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Meteor/Orion boards installed in a workstation display live images.

> When the Capture button is clicked on the VistA Imaging Capture main window, the VistA Imaging Capture window (shown below) will appear.

1)  A live image is displayed.
2)  To obtain a still image -- click the Freeze button

![](vista-imaging-system-clinical-capture-user-manual/179.png)

3)  Review the quality of the image,
    - If not satisfactory, click the Freeze button again. The window will resume the display of live images.
    - If the image is satisfactory, click the Image OK ![](vista-imaging-system-clinical-capture-user-manual/180.png) button.
4)  The VistA Imaging Capture main window will then move to the foreground, the "frozen" image will appear in the Display area of the main window.
5)  Prior to capture, Review all the patient information and the image,
    - If not correct, click Cancel.
    - If the image and data are correct, click the Image OK ![](vista-imaging-system-clinical-capture-user-manual/181.png) button to save them in the patient's record.
6)  If a Study (Group) of several images, is being performed, click the Capture button to return to the live image display window.

## Digital and Still Video Camera Input

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Digital Camera

> These cameras are used by staff in the:

- Wound Care Clinic
- Home Based Primary Care
- Dermatology Clinic
- OR
- Plastic Surgery
- Podiatry
- Outpatient Clinics
- Nursing Home
- Administrative
- Police office (for Patient Photo ID)

> Most of the cameras can transfer their images by connecting to a PC that has a USB port.

- the camera is turned on in display mode
- the camera appears in the Windows Explorer as a 'removable' drive
- images can be copied to an 'import' folder on the PC hard drive
- to store the images in the patient record, select the import folder when running VistA Imaging Capture

#### Still Video Camera

> If the input device is a still video camera (which records full motion video) with a TWAIN interface, it must be connected to the workstation. Consult the instructions for the camera to see if turning off the workstation is recommended before proceeding.

> There are several kinds of interfaces:

- Images are recorded by the camera prior to being connected to the workstation.
- The camera operates in live mode, inputting images as they are captured.
- The camera provides a download mode (non-TWAIN) that places all images in a directory on the workstation.

### Using the TWAIN Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Images are recorded by the camera prior to being connected to the workstation. When the 'Capture' button is clicked the camera will be started and a series of images will probably appear in the TWAIN window (depending on the software provided with the camera). Follow the instructions provided with the camera and select the image to be captured. The captured image will appear in the image box on the Capture window.
2.  The camera operates in live mode, inputting images as they are captured. Follow the instructions provided with the camera. As images are captured and indicated acceptable, they will appear in the image box on the Capture window.

> Using the Download Function

3.  The camera provides a download mode (non-TWAIN) that places all images in a directory or as a mapped drive on the workstation. This method may be preferred because of its speed. In this case, follow the instructions with the camera. Be sure that the downloaded images are stored in a standard format such as JPEG, BMP, or TIF. Then use the VistA Imaging Import mode to import the images into VistA.

## Validate Image Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Imaging capture validates the Image data in the following ways:

#### Patient

> User must have selected a patient

#### Procedure

> User must have selected a procedure or a category

#### Doc/Image Date - Image Date

> Usually entered by system. Taken from the associated procedure date. But if one of the three Patient Only associations (Clinical, Photo ID, Administrative) is selected, then the user has to enter the date. It is a standard FileMan Date/Time look up. i.e. 'T' 'T-1' etc. are accepted input values.

#### Image File

> User must have captured or imported an Image. It will be visible in the Image box on the Capture window.

#### Image Description

> Must be entered by user. (User can accept the system default description)

#### Image Long Description

> (Optional)

## Display Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Display Area has image manipulation buttons to modify the image before saving it. See the *Image Manipulation Buttons* section for more information.

> The Display Area and its controls enable the viewing, verifying and manipulating of the image prior to capture.

![](vista-imaging-system-clinical-capture-user-manual/182.png)

> Prior to capture: Images are displayed for medical and/or administrative review.

> When the Capture button is clicked, a Confirmation window appears.

![](vista-imaging-system-clinical-capture-user-manual/183.png)

> At the bottom of the VistA Imaging Capture window is a status bar.

1)  An internal check is done by the software to determine that the image and data are ready for the capture process
    - the current status message is: "Image data is Valid"
    - this is not a medical or administrative review
2)  The bottom right corner of the window has a progress meter -- currently showing 5%.
    - this indicates that the initial step of the Capture process has begun
3)  The Confirm window displays information about the image currently shown in the Display area.
    - Review the quality of the image and the data in the Confirm window.
    - If the displayed image and data are accurate, then click the OK button to save the image to VistA.
      - After the image capture is completed, check the status bar for any further messages.
      - If a Study (Group) is being captured, then continue the capture process.
    - If the image and/or data are not satisfactory, then click the Cancel button to discard the image.
      - Correct the image and/or data information before resuming the Capture process.

> The VistA Imaging Capture main window can also act as an Image Browser by selecting 'Import' as the 'Input source' and then scrolling through the Import directory file listing: As each image name is selected, it will be shown in the Display area.

> ![](vista-imaging-system-clinical-capture-user-manual/184.png)

## Image Manipulation Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vista-imaging-system-clinical-capture-user-manual/185.png)

> The right side of the window under the Tool Bar has the Image manipulation buttons and the image box.

> When an image is captured, it is shown in the Display area.

> Caution: Any changes made to the Image, except sizing operations, will be saved when 'Image OK' ![](vista-imaging-system-clinical-capture-user-manual/186.png) button is clicked.

- Sizing operations include: Zooming, fit Width, fit Height and fit in Window.

#### Button descriptions:

> ![](vista-imaging-system-clinical-capture-user-manual/187.png)Document control (paging is enabled for multi- page images).

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>![](vista-imaging-system-clinical-capture-user-manual/188.png)</th>
<th><p><strong>Reset the image</strong></p>
<p>To its original orientation, contrast and brightness. (This does not reload the image from disk, to do that during Import, simply click again on the image in the Import directory listing.)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](vista-imaging-system-clinical-capture-user-manual/189.png)</td>
<td>Fit the image - Into the Display area.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>![](vista-imaging-system-clinical-capture-user-manual/190.png)</th>
<th><blockquote>
<p><strong>Fit</strong> the image <strong>height Fit</strong> the image <strong>width</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](vista-imaging-system-clinical-capture-user-manual/191.png)</td>
<td>Zoom image to actual size (1 pixel to 1 pixel)</td>
</tr>
<tr class="even">
<td>![](vista-imaging-system-clinical-capture-user-manual/192.png)</td>
<td><blockquote>
<p><strong>Flip</strong> image <strong>vertically Flip</strong> image <strong>horizontally</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>![](vista-imaging-system-clinical-capture-user-manual/193.png)</td>
<td><strong>Rotate</strong> image 90 degrees <strong>to the left</strong>, Rotate the image 90 degrees <strong>to the right</strong></td>
</tr>
<tr class="even">
<td>![](vista-imaging-system-clinical-capture-user-manual/194.png)</td>
<td><p><strong>Invert all the colors</strong> in an image. Each color is replaced by its color complement.</p>
<blockquote>
<p>For example, white becomes black, and red becomes blue.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>![](vista-imaging-system-clinical-capture-user-manual/195.png)</td>
<td><p>Open a <strong>Pan Window</strong>.</p>
<blockquote>
<p>Use the mouse in the pan window to move the visible area of a zoomed Image</p>
</blockquote></td>
</tr>
<tr class="even">
<td>![](vista-imaging-system-clinical-capture-user-manual/196.png)</td>
<td>Position the mouse over the Image, and <strong>drag (pan)</strong> the visible area of a zoomed image</td>
</tr>
<tr class="odd">
<td>![](vista-imaging-system-clinical-capture-user-manual/197.png)</td>
<td><strong>Click</strong> to turn <strong>'magnifying glass' on or off</strong>. When this tool is turned on, dragging the left mouse button over an image displays a portion of the image at a greater magnification.</td>
</tr>
<tr class="even">
<td>![](vista-imaging-system-clinical-capture-user-manual/198.png)</td>
<td><strong>Zoom</strong> in on <strong>selected area</strong>.</td>
</tr>
</tbody>
</table>

## Warning Panel for Patient Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once a patient is selected using any of the above described methods and an image is displayed in the capture window, any change to the Patient selected will cause Clinical Capture to display a Warning Panel as shown below. The Warning Panel alerts that the Patient has changed since an image was loaded. At this point, there are two available options:

- “Continue” with the patient change using the Continue ![](vista-imaging-system-clinical-capture-user-manual/199.png) button to keep the image displayed in the capture window so that it can be used for the newly selected patient.
- “Cancel Image” using Cancel Image ![](vista-imaging-system-clinical-capture-user-manual/200.png) button to clear the image displayed in the capture window

> ![](vista-imaging-system-clinical-capture-user-manual/201.png)

## Approving the Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vista-imaging-system-clinical-capture-user-manual/202.png)When the image displayed in the image box is acceptable, click the 'Image OK' button.

> ![](vista-imaging-system-clinical-capture-user-manual/203.png)![](vista-imaging-system-clinical-capture-user-manual/204.png)A confirmation window will open and display the Image information. Click 'OK' to approve or click 'Cancel' to discard the Image and Image data.

> If there are more images for this procedure, use the Capture button again to capture them.

#### Note:

- When one of the data input fields has the input focus the 'Image OK' button is set as the 'window default button'. When \<Enter\> is pressed the window default button will be clicked.
- \<TAB\> doesn't have to be pressed repeatedly to get to the 'Image OK' button, simply press \<Enter\> while focus is on one of the input fields.
- Of course \<TAB\> can be pressed repeatedly to get to the 'Image OK' button, or click the 'Image OK' button with the mouse.

## Image Function Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These buttons are used during the capturing of a patient image. (Click an area of graphic for help on specific buttons.)

![](vista-imaging-system-clinical-capture-user-manual/205.png)

> The 'Image function buttons' consist of:

- Capture ![](vista-imaging-system-clinical-capture-user-manual/206.png) Activates the Input device to Capture (Acquire) the image.
- Image OK ![](vista-imaging-system-clinical-capture-user-manual/207.png) Indicate approval of the captured image.
- Cancel ![](vista-imaging-system-clinical-capture-user-manual/208.png) Discard the captured image.
- Study Complete ![](vista-imaging-system-clinical-capture-user-manual/209.png) Indicates that all images have been captured for the Study.
- Review ![](vista-imaging-system-clinical-capture-user-manual/210.png) Opens the document in an Adobe Reader window allowing you to view the full PDF.

## Batch Capture Transfer Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the images in the list box that you want to place in the batch capture list (below the list box) and then click one of the following icons:

> • ![](vista-imaging-system-clinical-capture-user-manual/211.png) To move selected images to the batch capture list

> • ![](vista-imaging-system-clinical-capture-user-manual/212.png) To move all images to the batch capture list

> Note: You can move all or selected images back to the list box by clicking either icon:

- ![](vista-imaging-system-clinical-capture-user-manual/213.png) To remove selected images from the batch capture list
- ![](vista-imaging-system-clinical-capture-user-manual/214.png) To remove all the images from the batch capture list

## Batch Capture Options window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If Import has been selected as the Source the Batch Capture option will be available.

> Batch capturing provides the capability of selecting multiple images from an import directory and have them all saved to an Image Group when 'Image OK' is clicked.

> ![](vista-imaging-system-clinical-capture-user-manual/215.png)Clicking the check box or selecting the 'Options\|Batch Capture Options' menu option will open the 'Batch Capture Options' window.

![](vista-imaging-system-clinical-capture-user-manual/216.png)

> 'Prompt for Image description' provides the opportunity to enter a different description for each image. If this is not checked, all images will have the same short description.

> Note: When 'prompt for image description' is checked the 'Batch Capture image description' window will be displayed before each image is saved to the VistA Image File.

> 'Delete Image File from Import Directory' will delete the Image File from the workstation directory.

> Caution: When the Delete Image File from Import Directory checkbox is checked, image files WILL BE AUTOMATICALLY DELETED from the import directory after they are captured. If the capture process was not successful, the image will no longer be available in the import directory. Therefore, it is recommended that after several single and/or groups of images are captured, you verify the capture by viewing the images using Imaging Display. Verify the first few images for each image capture device before this checkbox is checked. If the checkbox is unchecked, you can manually delete the images that are no longer needed..

> If '(do not show this window)' is checked then the 'Batch Capture Options' window will not be displayed when the 'Batch' check box is checked from the main capture window.

> Note: The 'Batch Capture Options' window can be displayed by selecting the '*Options*\|*Batch* Capture Options' menu item.

> ![](vista-imaging-system-clinical-capture-user-manual/217.png)

> Change the description and press \<Enter\> or click 'OK' to save the current image and continue on to the next image.

> If 'Skip this image' is clicked, the current image will be discarded and processing will continue with the next image in the batch list.

## Long Image Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Entry of a long image description is optional. Type any description in the scroll box provided. Long image descriptions are displayed as the first paragraph of Image Reports.

![](vista-imaging-system-clinical-capture-user-manual/218.png)

> Note: The mouse can be used to 'drag' the 'Long Description' field and make it smaller/larger for easier input of data. Position the mouse over the sizing bar above the 'Long Description' text and when the mouse changes to the horizontal crossbeams click down with the left mouse button and move the cursor to a new position for the top of the long description field then release the mouse button.

- Word wrap can be turned on/off.
- Paragraph indents and formatting will be saved.
- right-click to display the shortcut edit menu. Available options are: Undo, Cut, Copy, Paste, Delete, Select All.

> The Long Description field also has a minimum and maximum height and the system won't let the user size the field beyond them.

## Confirmation Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Confirmation window displays the Image data that is about to be saved to the patient record.

> When ![](vista-imaging-system-clinical-capture-user-manual/219.png)is clicked, a validity check is performed on the input data If the input data is valid, then the Confirmation Window will display.

![](vista-imaging-system-clinical-capture-user-manual/220.png)

> Click 'OK' to save the Image to the patient record

> Click 'Cancel' ![](vista-imaging-system-clinical-capture-user-manual/221.png) to stop the process and return to the capture window.

> Note: The Confirmation Window is only displayed if the menu option '*Options*\| *Show Confirmation messages*' is checked.

## Indicating Completion of a Study

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When all images have been captured for a procedure, click the Study Complete button of the Capture Window. The progress indicator at the bottom of the window will display. A group of images will be created and associated with the patient's report.

## Save Image Data to VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A new entry is made in the Image File.

- The entry consists of the image data along with a pointer to the procedure in the associated clinical package.
- A pointer to the Image File entry is entered in the procedure entry of the associated package.

> If either of these two actions fails, or an error occurs, the image capture fails.

## Fails

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the capturing of an Image Fails. The Imaging system will delete any entries made in the Image File and associated Package Files.

- The image is not written to long term storage.
- The user will have to fix whatever problem caused the failure.
- The system manager should be called if required.

# Importing Documents/Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Import File from Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In a number of cases, an image has been captured to a file on the local workstation. This is typical with commercially-available image capture systems. As long as these files are in a standard format, they can be imported into the VistA Imaging system. Even manufacturers who use a proprietary file format may offer an export function which will save another copy of the file in a standard format.

> The standard VistA Capture Window can be used to import images from the local workstation drive.

> To import images:

- First select the directory on the local system where the images to be imported are located (see the *Import Directory List* section below).
- Next select the image filename from the file list box on the capture window (see Select Image File to be imported).
- Then click the 'Capture' button.

> Note: When importing files, the 'Batch Capture' option is available.

- In 'Batch Capture' mode, multiple image files can be captured and saved at one time.

## Import Directory List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Imaging Capture is in 'Import Mode' when 'Import' has been selected as the input Source. In Import Mode, the directory of images to be imported must be selected.

![](vista-imaging-system-clinical-capture-user-manual/222.png)

> Open the Workstation Settings window – Import Directories tab, by selecting the menu option Options \| Import Directory Options.

![](vista-imaging-system-clinical-capture-user-manual/223.png)

> Click Add Directory Button ![](vista-imaging-system-clinical-capture-user-manual/224.png) to add a new directory to the Import Directory List.

> When the OK button is clicked, the image files will be redisplayed in the Import directory file list box on the Main Capture window.

#### Notes:

> The images displayed in the file list box in this window are for display purposes only. Images are not selected from this window – just the directory from which to import images is selected. The images available in the selected directory are displayed in the bottom left frame of the capture window. A screenshot is included below.

![](vista-imaging-system-clinical-capture-user-manual/225.png)

> If 'Save as default' is checked, the Drive Directory and file mask will be saved by the system and used as defaults the next time this window is opened.

> File mask or file filters are used to limit which files will be displayed in the file list box. The most familiar mask is '\*.\*'. This will display all files. Alternate masks can be typed, or selected from the list.

# Timesavers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Topics covered in this section:

- [*Using Keyboard Shortcuts*](\l)
- [*Using “Auto-Settings” to Save Keystrokes*](#using-auto-settings-to-save-keystrokes)
- [*Defining Display Area Defaults*](\l)
- [*Settings*](\l)

## Using Keyboard Shortcuts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can speed up the capture process by using the keyboard for frequently repeated actions. The following table summarizes keyboard shortcuts that can be used in the Capture window.

> Certain “Auto-Settings” may modify the behaviors described below. For more information about Auto-Settings, see the *[Using “Auto-Settings” to Save Keystrokes](#using-auto-settings-to-save-keystrokes)* section.

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>To :</strong></th>
<th><strong>Do This…</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Start scanning a document</td>
<td>Press ALT+C</td>
</tr>
<tr class="even">
<td>Discard a scanned document (Cancel)</td>
<td>Press Alt + N</td>
</tr>
<tr class="odd">
<td>Add long description</td>
<td>Press ALT+L</td>
</tr>
<tr class="even">
<td>Finalize a scan (Image OK)</td>
<td>Press ALT+K</td>
</tr>
<tr class="odd">
<td>Complete a study Press</td>
<td>ALT+E</td>
</tr>
<tr class="even">
<td>Select a new patient</td>
<td>Press ALT+P</td>
</tr>
<tr class="odd">
<td>Move from one input field to the next</td>
<td><p>Press TAB. A selected field will contain</p>
<p>a blinking cursor. A selected button will be displayed with a dotted border.</p></td>
</tr>
<tr class="even">
<td>Move to previous input field</td>
<td>Press SHIFT-TAB</td>
</tr>
<tr class="odd">
<td>Open a pull-down list</td>
<td>Press TAB until the field is selected, and then press the Down Arrow key.</td>
</tr>
<tr class="even">
<td>Select an item in a pull-down list</td>
<td><p>Type the first few letters of the value you want to enter in the field, or use the Up Arrow or Down Arrow keys. When the</p>
<p>appropriate item is selected, press ENTER.</p></td>
</tr>
<tr class="odd">
<td>Close a pull-down list (without selecting a value)</td>
<td>Press ESC (the Escape key)</td>
</tr>
</tbody>
</table>

## Using “Auto-Settings” to Save Keystrokes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Options in the Auto-Settings tab can be used to reduce the number of keystrokes or mouse used during document scanning.

> To specify Auto-settings for a user

> In the main menu, click Options \| Auto Settings. The Capture Session Settings dialog will open.

> In the Auto-Settings tab, select or clear each option as desired.

> When you are finished, click OK. Your changes will take effect immediately.

> To associate the settings with the current login and to ensure that they are retained for future sessions, click Options \| User Preferences \| Save Preferences.

## Defining Display Area Defaults

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a document is scanned, it will be displayed in the right side of the Capture window using a default zoom and image position. You can define what the default zoom and position can be using the following steps. Once defined, these settings can be associated with your login and then will “follow” you from workstation to workstation.

> To specify Display Area defaults

> In the main menu, click Options \| Scrollbar/Zoom Settings. The Capture Session Settings dialog will open.

## Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the Scrollbar and Zoom Settings tab, choose one of the following options:

| Settings              | Explanation                                                                                                                                                                                                                                                           |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fit to Window Setting     | Displays entire captured image at largest size possible, given the current dimensions of the display area.                                                                                                                                                                |
| Repeat Settings           | Displays captured image using the zoom and position of the previously captured image. (Position is used only if the current zoom Last Displayed image does not permit the entire image to be shown in the display area.)                                                  |
| Always Use these Settings | Allows the user to apply whatever settings are used for current image for all subsequent captured images.                                                                                                                                                                 |
| Positional                | The position can be Center, Upper Left, Upper Right, Lower Left, or Lower Right, and is selected by clicking the box control near the bottom of the dialog. (Position is used only if the current zoom does not permit the entire image to be shown in the display area.) |

> When you are finished, click OK. Changes will take effect immediately.

> To associate the settings with the current login and to ensure that they are retained for future sessions, click Options \| User Preferences \| Save Preferences.

# Miscellaneous

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Image Copy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Images are copied to storage in a separate thread. This enables the Clinical Capture application to maintain connection/communication to the VistA System during the image copy.

## File Copy Progress Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the file is large and/or network access is slow, the image could take longer than usual. When this happens, a File progress bar will become visible on the bottom status bar of the Clinical Capture application. This is a visual indicator to the user that the copy is working, but taking longer than usual.

![](vista-imaging-system-clinical-capture-user-manual/226.png)

# Menu Options and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Topics covered in this section:

- *File*
- *Context menu*
- *Options menu*
- *Tools menu*
- *Configurations menu*
- *Capture Configuration list*
- *Save Capture Configuration*
- *Clear Configuration values*
- *Properties saved with configuration definitions*
- *‘Association’ configuration settings*
- *Workstation configuration*
- *Imaging Workstation Configuration window*

## File Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The File menu is mainly for patient selection and login options. Those options are described in separate the sections Selecting a Patient and Logging In and Starting Clinical Capture.

![](vista-imaging-system-clinical-capture-user-manual/227.png)

#### Select Patient…

> (see the section, Selecting a Patient)

#### Latest Patient Images…

> (See the section: Patient's Latest Window Overview)

#### Open Image for Annotation after Image OK

> If this menu option is checked, captured images will be opened in a separate window of the Display client. The user can annotate and/or verify that the image was captured correctly.

> Note: The menu options that refer to opening images in Clinical Display will only be available when Clinical Display Patch 167 is installed.

#### Login, Logout, Remote Login, 1 Patient Name

> (See the section : 'Logging In and Starting Clinical Capture')

#### Exit

> This will close the Clinical Display application.

#### Patient's Latest Window Overview

> The Latest Patient Images menu option will open the Patient's Latest Images window.

> When the user selects an item from the list, information for the image and the image itself are displayed in the panels to the right of the list. This screen has three areas: an Image Information panel, an Image Display panel (matching the information in the Clinical Display client) and a Main Menu.

![](vista-imaging-system-clinical-capture-user-manual/228.png)

> The Toolbar has options for the user to :

- List a certain number of the latest patient images.
- Refresh the current list of images
- Retrieve the next number of patient images.
- Three check boxes to enable the user to filter the listed images by the application that was used to capture the image.

## Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-clinical-capture-user-manual/229.png)</p>
</blockquote></th>
<th>Exit: Close the window.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-clinical-capture-user-manual/230.png)</p>
</blockquote></td>
<td><p>Stay on Top: If checked, then this window will stay on top of other windows.</p>
<p>Refresh: Reload the list of Patient images.</p>
<p>Image Count Select 50, 100 or 200 images to display. Note: The user can click the More button to list more of the patient's images.</p>
<p>Retrieve Group Info for Selected Image: (see details below)</p>
<p>The Image Group of the selected image will be selected and information will be displayed in the Image Information panel.</p>
<p>Enter an Image Group IEN…</p>
<p>An alternate way to select an Image Group is to enter the ID# of an Existing Group.</p>
<p>Open Image in Clinical Display:</p>
<p>The selected image will be opened in a separate window in Clinical Display.</p></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>Note:</strong> The option to open an image in Clinical Display will be visible when Patch 167 of Clinical</p>
<p>Display has been installed. This option is intended to be used for annotating or verifying the patient image.</p></td>
</tr>
</tbody>
</table>

> Retrieve Group Info for Selected Image:

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>When an Image Group has been selected, the Capture to Group button will be visible above the Image Information panel.</th>
<th><blockquote>
<p>![](vista-imaging-system-clinical-capture-user-manual/231.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>When the Capture to Group button is selected, the window will close, and input focus will change to the Main Clinical Capture window. The user can then start capturing additional images to the selected image group.</p>
<p>A panel above the Image Box will remind the user that these images are being captured to an Existing Group. The user can click the Cancel button if they want to cancel capturing images to this group.</p>
<p><strong>(cutout of Main Capture Window)</strong></p>
<p>![](vista-imaging-system-clinical-capture-user-manual/232.png)</p></td>
</tr>
</tbody>
</table>

![](vista-imaging-system-clinical-capture-user-manual/233.png)

> Check Boxes: “Include images captured through these application” (New)

- The user can choose to filter the images that are listed by the device that captured the image. This gives the user the option to view only the images that were captured on a Clinical Capture workstation.

> Descriptions: column headers of Image list.

- IEN : This is the Image Identifier
- CID : This refers to the application that captured the image and is the same as the checkboxes at the top of the window: C = Clinical Capture client, I = Import API, D = DICOM Gateway

> Group IEN: This is the Group Identifier. Images with the same Group IEN are contained in the same Image Group. Images without a Group IEN are single images.

## TIU Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the Patient's Latest Images window, TIU Business Rules are followed when Images are viewed. TIU Business Rules may disable some scanning personnel from viewing the images after the image has been captured to a TIU Note.

> The System Manager can disable TIU Business Rules for a scanning workstation if needed.

> To disable, open the mag.ini in notepad. Add a new entry in the \[Workstation Settings\] section. The new entry is: SkipBusinessRules=FALSE.

> When that entry is in the mag.ini, a user with the MAG SYSTEM Security key can enable/disable TIU Business rules on this workstation by opening the Workstation Configuration editor from the System Manager menu.

> Example:

> \[Workstation Settings\] SkipBusinessRules=FALSE

## Context Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Context menu is used to manipulate patient context when Clinical Capture is used with CCOW.

![](vista-imaging-system-clinical-capture-user-manual/234.png)

> The Context menu provides access to these sub-menus:

- Show Context
- Suspend Context
- Resume Get Context
- Resume Set Context

> For a description of these options and for more information about CCOW and patient context, see [*Appendix B: Clinical Context Object Workgroup*.](#_bookmark174)

## Options Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains various options provided to users under the Options menu used to customize the capture workstation as needed.

![](vista-imaging-system-clinical-capture-user-manual/235.png)

#### Import Options

> Use the Import Options menu option to customize the import settings or to select the files from one of the pre-set import directories. See the *[Importing Documents / Images](\l)* section for more information. The Import Options menu option has two sub-menus:

- Import Directory Options – Choose this option to customize the import directory settings for the workstation (set the default directory, add a new directory or remove an existing directory). Selecting this option opens the Import Directories tab in the Workstation settings dialog box, which is illustrated in the following figure.

![](vista-imaging-system-clinical-capture-user-manual/236.png)

> You can also access the Import Directories tab in the Workstation settings dialog box by selecting Options \| Import Directory Options.

- Select Files to Import – Choose this option to select images from a pre-set import directory.

#### Batch Capture Options

> Select this option to change the options for batch capture of images. If the Prompt for Image Description option is selected, a description for each image in the batch has to be entered before saving.

> If the Delete Image File from Import Directory option is selected, the image will be deleted from import directory after importing and saving in Clinical Capture.

![](vista-imaging-system-clinical-capture-user-manual/237.png)

#### Alternate Viewer Options

> Use the Alternate Viewer Options menu option to customize the alternate viewer settings, which specify the viewer in which different file types are displayed. Video files, PDFs, images in DICOM format and text files can either be displayed in the Clinical Capture window or an alternate viewer. Selecting Options \| Alternate Viewer Options opens the Alternate Viewer Options dialog box, which is illustrated in the following image.

![](vista-imaging-system-clinical-capture-user-manual/238.png)

> By default, video files play in the Imaging Video player in Clinical Capture. If you want to change this option, select the Use Alternate Viewer Option. Selecting this option plays video files using alternate video player.

> Note: AVI files can be captured in VistA Imaging only.

> By default PDFs, images in DICOM format and text files are displayed in the Clinical Capture window. If you want files of any of these types to be displayed in an alternate viewer, select the relevant check box next to the file type.

> Click OK in the Alternate Viewer Options dialog box to save your settings.

#### Auto Settings

> Use the Auto-settings option to select the user options for tab and keyboard actions for the user session. Selecting Options \| Auto-settings opens the Auto-Settings tab of the User Session settings dialog box, which is illustrated in the following image.

![](vista-imaging-system-clinical-capture-user-manual/239.png)

#### Scroll Bar/Zoom Settings

> Use the Scroll Bar/Zoom settings option to customize the default zoom and scroll bar settings for a user. Selecting Options \| Scroll Bar/Zoom settings opens the Scroll Bar and Zoom Settings tab of the User Session settings dialog box, which is illustrated in the following image.

![](vista-imaging-system-clinical-capture-user-manual/240.png)

#### Visit Location

> Option to select the default ‘location’ for new Progress notes when creating new TIU Notes.

> Visit Locations are locations found in the hospital (i.e. Wards, Clinics). User selects the Visit Location where the procedure took place.

> The value of Visit Location is an entry in the HOSPITAL LOCATION File (#44).

![](vista-imaging-system-clinical-capture-user-manual/241.png)

#### Show Hints

> When the Show Hints option is selected, hints (tooltips) are displayed when you mouse over a toolbar button or a field.

![](vista-imaging-system-clinical-capture-user-manual/242.png)

#### Show Confirmation Messages

> When the Show Confirmation messages option is checked, you will be prompted to confirm your choices and actions at certain points of the capture process. For example, a window may display prompting you to confirm an action by clicking OK.

> The Show Confirmation messages option should be checked for new users of VistA Imaging Clinical Capture.

![](vista-imaging-system-clinical-capture-user-manual/243.png)

#### Toolbars

> Use the Toolbars option to customize the toolbars that are displayed.

![](vista-imaging-system-clinical-capture-user-manual/244.png)

> When an option is *checked,* the Capture window toolbar will be visible and display the saved configurations as buttons.

> When *checked*, the current settings will be displayed at the top of the Capture Window. Click on a setting button to quickly change that setting only.

#### Configuration Buttons -Left/Top

> The user has the option to display the Configuration Toolbar on the left or top of the Clinical Capture main window.

> Positioning Configuration buttons on the left will enable the image box to be larger, making the image easier to view.

#### User Preferences

> Use the User Preferences option to save all capture session settings controlled from the Options

> menu to the VistA system.

> Once you save these settings, they will be applied every time you log into Clinical Capture, regardless of the workstation you are logged into.

> ![](vista-imaging-system-clinical-capture-user-manual/245.png)

#### Message History

> Use the Message History option to display the Message History Window.

![](vista-imaging-system-clinical-capture-user-manual/246.png)

> For more information about the Message History, see the *MagLogger User Guide*.

#### Combine TIF Scans

> The option Combine TIF Scans of the Options menu allows you to add more images to the currently scanned image before you save the image.

> It is useful if after you scan an image you realize that you need to capture additional images and add them to the current scan.

> The option is available only after you click the Capture button and before you click Image OK.

> When you capture an image, after you click the Capture button, the button becomes grayed out.

![](vista-imaging-system-clinical-capture-user-manual/247.png)

> If you want to add more images to the current scan, you can do so either by selecting Combine TIF Scans from the Options menu.

![](vista-imaging-system-clinical-capture-user-manual/248.png)

> When you choose Combine TIF Scans, the Capture button becomes enabled again allowing you to add more images to the current scan.

![](vista-imaging-system-clinical-capture-user-manual/249.png)

#### Combine PDF Scans

> The option Combine PDF Scans of the Options menu allows you to add more pages to the currently scanned PDF before you save it (by clicking Image OK).

> It is useful if after you scan a PDF, you realize that you need to add more pages to the current PDF scan.

> The option is available only when the current scan is a PDF, after you click the Capture (PDF)

> button and before you click Image OK to save the current scan.

> When you finish scanning the pages to a PDF, the Capture PDF button becomes grayed out.

![](vista-imaging-system-clinical-capture-user-manual/250.png)

> If you want to add more images to the current scan, you can do so either by selecting Options\| Combine PDF Scans.

![](vista-imaging-system-clinical-capture-user-manual/251.png)

> When you choose Combine PDF Scans, the Capture (PDF) button becomes enabled again allowing you to add more pages to the current scan.

![](vista-imaging-system-clinical-capture-user-manual/252.png)

> For more information about scanning to PDF, see [*Scanning to PDF*.](#_bookmark63)

#### Icon / Shortcut Key Legend

> This sub-section provides an explanation of the icons and shortcuts available and the legend.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Import List, Note Icons, General</strong></th>
<th>This menu has a legend of icons available in Clinical Capture.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Import List</strong></td>
<td><p><strong>Import List</strong> options tab has an explanation of the icons available in Import List Directory.</p>
<p>![](vista-imaging-system-clinical-capture-user-manual/253.png)</p></td>
</tr>
<tr class="even">
<td><strong>Note Icons</strong></td>
<td><p><strong>Note Icons</strong> options tab has an explanation of the icons available in Progress Notes Window.</p>
<p>![](vista-imaging-system-clinical-capture-user-manual/254.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>General</strong></th>
<th><p><strong>General</strong> options tab has an explanation of the icons available in Capture.</p>
<p>![](vista-imaging-system-clinical-capture-user-manual/255.png)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ShortCut Keys</strong></td>
<td><p><strong>ShortCut Keys</strong> tab shows a list of Shortcut Keys available in Clinical Capture. Below are screenshots of all available shortcuts.</p>
<p>![](vista-imaging-system-clinical-capture-user-manual/256.png)</p></td>
</tr>
</tbody>
</table>

| ShortCut Keys Continued  | ![](vista-imaging-system-clinical-capture-user-manual/257.png)         |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ShortCut Keys Continued… | ![](vista-imaging-system-clinical-capture-user-manual/258.png) |

| ShortCut Keys Continued… | ![](vista-imaging-system-clinical-capture-user-manual/259.png) |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides an explanation for the options available under the Tools Menu.

![](vista-imaging-system-clinical-capture-user-manual/260.png)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option</strong></th>
<th><strong>Explanation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CPRS Link Options</strong></td>
<td><p>The CPRS Link Options is enabled if VistA Imaging Capture was started from the CPRS 'Tools' menu.</p>
<p>Selecting this option opens the Imaging &lt;-&gt; CPRS Link window.</p>
<p>The link between CPRS and Imaging can be disabled (broken).</p></td>
</tr>
<tr class="even">
<td><strong>Refresh Index lists</strong></td>
<td>Operate on the Index.</td>
</tr>
<tr class="odd">
<td><strong>Realign Index Fields</strong></td>
<td>Executes the code to ‘align’ the index fields … i.e. the input fields on the left side of the window.</td>
</tr>
</tbody>
</table>

## Configurations Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides an explanation for the options available under the Configuration Menu.

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option</strong></th>
<th><strong>Explanation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](vista-imaging-system-clinical-capture-user-manual/261.png)<strong>Configuration Settings</strong></td>
<td><p>Opens the <strong>Configuration settings</strong> window. This option provides access to a submenu. The submenu lets you open the main Configurations dialog, or any of the dialogs typically opened from the configuration settings toolbar. The sub-menu options are: Source; Format; Association; Saving; Mode; Other.</p>
<p>Image Capture settings can be changed using this option.</p></td>
</tr>
<tr class="even">
<td><strong>Select 'Hold' Values</strong></td>
<td><p>Hold values window opens. You can choose fields to hold values here.</p>
<p>![](vista-imaging-system-clinical-capture-user-manual/262.png)</p></td>
</tr>
<tr class="odd">
<td><strong>Configuration List</strong></td>
<td><p>Opens Configuration List</p>
<p>window. See below for more.</p></td>
</tr>
<tr class="even">
<td><strong>Save Configuration</strong></td>
<td>Saves current configuration settings</td>
</tr>
<tr class="odd">
<td><strong>Clear Configuration Values</strong></td>
<td>Clears saved configuration settings</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Modify Configurations: change Group to Single...</strong></th>
<th><p>Enables the user to change all existing configurations</p>
<p>from Study (Group) to Single Image.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Numbers 1,2, 3</strong></td>
<td>Represent recently saved configurations</td>
</tr>
</tbody>
</table>

#### All Settings

> The All Settings option opens the Imaging Workstation configuration window. The window has different tabs that contain all configuration settings. You can change these settings in the tabs of the Imaging Workstation configuration window.

## Capture Configuration List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Configurations window is where capture configurations can be created, edited and deleted. Click the ![](vista-imaging-system-clinical-capture-user-manual/263.png) button to view the current configuration list.

![](vista-imaging-system-clinical-capture-user-manual/264.png)

> The Capture configuration list, which is used to display information about current configuration definitions, provides flexibility in how that information is displayed.

#### Configuration Info. Pane

> This is the pane on the right side of the Capture Configurations list window. This pane

> displays the specifics of a selected configuration definition.

![](vista-imaging-system-clinical-capture-user-manual/265.png)

> The top portion of the pane shows the 'standard' set of properties that can be set from the main Capture window or from the Configurations dialog.

- also includes an "Other" entry that can display specific settings such as:
- Batch - if it is checked during an import.
- Interactive - if Meteor/Orion ‘Interactive’ is checked while using a Meteor/Orion capture board.
- Multi Page - if the MultiPg Doc checkbox is checked during a Twain capture.

> The *bottom portion of the pane* shows settings for the new Hold Value feature, and any initial values saved for specific index fields.

#### Configuration list

> The configuration list on the left side of the window provides the following features:

![](vista-imaging-system-clinical-capture-user-manual/266.png)

- Selecting (clicking) a configuration definition will display settings for that definition on the right side of the window. In previous versions, clicking a list item would cause those settings to be applied.
- Selecting (clicking) a configuration definition, and then clicking Save, will cause the current settings in the main Capture window to be saved to (overwrite) the currently selected configuration definition.
- When a configuration is selected, it can be applied by pressing \<Enter\>, or by clicking OK. The dialog will close when a configuration is applied.
- A configuration can also be applied by double-clicking it with the mouse, or by right-clicking it, then selecting Apply.

> When these methods are used to apply a configuration:

- The dialog will remain open.
- The configuration list can be sorted by column heading by double-clicking the heading.
- The columns in the configuration list can be also resized based on the available space in the dialog or based on the information in each column. Resize options are available under the Options menu.
- The user can customize the configuration list by selecting which columns are displayed or not.

> This feature is available by choosing *Options* \| *Column Select*.

> View menu options let a user choose between views for the configuration list.

1)  “Detail” view, containing details for each configuration definition.

![](vista-imaging-system-clinical-capture-user-manual/267.png)

2)  'List' view, an abbreviated list showing only the names of the configuration definitions. Details of a selected configuration are shown on the right side of the Capture Configurations window.

![](vista-imaging-system-clinical-capture-user-manual/268.png)

> Menu for Capture configurations list

> There is a menu bar at the top of the Capture Configurations dialog. All functionality for this dialog is accessible from the menu.

> Menu options are summarized below. Menu & Functionality

#### Options menu

- *Apply Selected Configuration:* applies selected configuration to main Capture window.
- *Fit Columns to Form:* resizes each column to fit in the visible area of the list.
- *Column Select:* opens the Column Selector window
  - The user can select which columns to display in the detail view of the configuration list.
- *Stay On Top*
- If checked, this window will stay on top of all other windows in the application.

#### View menu

- List/Details:
- Switches between List and Detail views.
- Displays or hides the Capture Configurations dialog toolbar, described below.

#### Toolbar

> View menu can turn the toolbar on and off.

![](vista-imaging-system-clinical-capture-user-manual/269.png)

> The OK button can be used to apply the currently selected configuration definition and close the Capture Configurations window.

## Save Capture Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Click Save Configuration option under Configuration Menu. Name the Configuration created then click OK.

![](vista-imaging-system-clinical-capture-user-manual/270.png)

> This dialog can be used to save the current state of the main Capture window as a new or existing set of configuration settings.

## Clear Configuration values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to clear the Image Workstation configuration screen of all its values except for the patient demographics.

![](vista-imaging-system-clinical-capture-user-manual/271.png)

1)  Configurations Settings - option provides access to a submenu. The submenu lets you open the main Configurations dialog, or any of the dialogs typically opened from the configuration settings toolbar.
2)  Select Hold Values - option that opens the Hold Values dialog.
3)  Save Configuration - option allows direct access to the Save Configuration dialog.

> ![](vista-imaging-system-clinical-capture-user-manual/272.png)

> This dialog can be used to save the current state of the main Capture window as a new or existing set of configuration settings.

## Properties Saved with Configuration Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following properties will be saved when a capture configuration definition is defined: The properties:

- For each input field, the status of the ‘Hold Value’ feature will be saved. This feature can be used in some situations to reduce repetitive data entry.
- The current value of the index fields: Type, Specialty and Proc/Event will be saved.
- The current value of the existing Image Description field will be saved.
- When Twain Window or Scanned Document is selected, the user can specify if multiple page documents are being scanned or not.

## ‘Association’ Configuration Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vista-imaging-system-clinical-capture-user-manual/273.png)

| Designation       | Use For                                        |
|-----------------------|----------------------------------------------------|
| Patient Only/Clinical | Outside medical records, discharge summaries, etc. |
| Patient Only/Photo ID | Photo ID                                           |

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Patient Only/</p>
<p>Administrative</p></th>
<th>Advance directives, means test forms, etc.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Workstation Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Workstation Configuration allows the system manager to define a default configuration when VistA Imaging Capture is initially installed on a workstation.

> An example of a default configuration is:

- Enabling only the input Sources, image Formats and Associations (medical and/or administrative images) that apply to this workstation.
- Defining default settings for input Source, Format and Association.

> Because of the default configuration VistA Imaging Capture will be configured to begin capturing images when it is started.

> Note: Some of the choices on the configuration window for input Source, image Format and Association will be grayed-out (disabled) because of the default configuration. If there is a need to have configuration settings enabled contact the System Manager.

## Imaging Workstation Configuration Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The toolbar used to show current settings at the top of the Capture window.

- Clicking the title of each setting will launch its dialog.

![](vista-imaging-system-clinical-capture-user-manual/274.png)

> The related areas in the Imaging Workstation Configuration dialog:

> 'Auto Detect Image Format' for imported images:

- When images are imported from an image server (Source = Import), the Capture program will automatically determine the proper image format based on the filename extension (JPG, PDF, etc.) of the image. This will reduce the chances of

> the incorrect image format being selected, and allows batch captures for groups of images with mixed formats.

> This feature is reflected:

- in the main Capture window, when Import is selected as a Source,
1)  The Image Format indicated at the top of the window will initially appear blank.
2)  The Image Format of the image being captured will be shown when the capture is complete.
3)  The Image Format will be updated with each new capture.

> *For example:*

1)  Source initially set to Import

![](vista-imaging-system-clinical-capture-user-manual/275.png)

2)  Capture occurs, imported file is PDF format

![](vista-imaging-system-clinical-capture-user-manual/276.png)

3)  Next capture occurs, imported file is AVI format

![](vista-imaging-system-clinical-capture-user-manual/277.png)

> The Use Format of Imported Image option will automatically be selected when the Source is set to Import. Other Format options will be disabled. This affects the Select Image Format dialog and the Format area of the Imaging Workstation Configuration dialog.

#### The Convert to DICOM option for Source Import:

> The Convert to DICOM option allows converting images to DICOM format. You can select the Convert to DICOM option from the list box for Import. When Convert to DICOM is selected, the Format : DICOM(VL Photo Image Storage) is selected automatically. You must use the Convert to DICOM option when TeleReader Consult is selected as the Association choice.

> ![](vista-imaging-system-clinical-capture-user-manual/278.png)

> The Image Format is used to indicate the type of image resulting from the capture process. You can select the format either on the Source/Format tab or on the Legacy tab of the Image Workstation Configuration window.

> Possible formats include:

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Image Format</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>True Color TGA</td>
<td>24-bit image</td>
</tr>
<tr class="even">
<td>True Color JPG</td>
<td><p>Meteor produces 640x480 pixels</p>
<p>TWAIN produces a variety of resolutions: 256 color; 8-bit color image; variable spatial resolution depending on source.</p></td>
</tr>
<tr class="odd">
<td>X-ray</td>
<td>8 or 12-bit grayscale image</td>
</tr>
<tr class="even">
<td>X-ray (JPG)</td>
<td>8-bit 8-bit grayscale JPG image</td>
</tr>
<tr class="odd">
<td>Black and White</td>
<td>8-bit grayscale image: 768x486 or 640x480 pixels</td>
</tr>
<tr class="even">
<td>Document (TIF uncompressed) 1-bit</td>
<td>300x300 dpi (or other resolution)</td>
</tr>
</tbody>
</table>

| Image Format      | Description                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Document (TIF G4 FAX) | TIFF G4 compression                                                                                                                                              |
| Bitmap (uncompressed) | BMP image                                                                                                                                                        |
| Adobe                 | PDF Adobe Acrobat document                                                                                                                                       |
| Rich Text             | RTF Rich Text Format document                                                                                                                                    |
| Motion Video          | AVI motion video file                                                                                                                                            |
| Text File             | TXT file                                                                                                                                                         |
| Web Document          | HTM Hypertext Markup file                                                                                                                                        |
| Web Document          | XML Extensible Markup Language file                                                                                                                              |
| Audio                 | WAV sound file                                                                                                                                                   |
| X-ray                 | Used for scanned x-ray films of any sort: includes Lumisys; may be used for other black and white images where exact manipulation of the grayscale is necessary. |

> NOTE: The greater gray scale or color dpi chosen the larger the physical file created. This will affect transmission and storage processing times.

# Clinical Capture System Manager Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These are options that are available only to those who have the MAG SYSTEM KEY assigned to them. If you do not have the MAG SYSTEM KEY assigned to you, you will not have these options available to you.

## System Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Imaging Capture: System Manager Menu option

> The System Manager Menu option in VistA Imaging Capture will be visible for users that have the Imaging Security Key "MAG SYSTEM" assigned to them.

![](vista-imaging-system-clinical-capture-user-manual/279.png)

#### Workstation Configuration Editor

> Opens the Workstation configuration window where workstation settings can be modified. This is an alternate way to access the Workstation configuration window. This menu item simply runs MAGSYS.EXE

#### Apply Workstation Settings

> Applies the current configuration settings from the Workstation configuration file to the VistA Imaging Capture Application.

#### Show ImageGear Info : to msg window

> Opens the message history window and displays information about the current image. (Intended for debugging purposes)

#### Save "Captured Image" As

> Save an Image to the workstation. (intended for debugging and demonstration purposes)

#### Select a Write Directory

> This option opens a window to select the Network Directory to save captured images to. (This is the only way to save an image to a directory other than the 'WRITE LOCATION' field in the SITE PARAMETERS File. The directory chosen will remain in effect for the remainder of this Capture session.

#### Advanced Batch Capture Options

> Opens the 'Batch Capture Options' window.

> During Image Import, if the check box 'Copy all associated files.' is checked, the import directory will be searched for files with the .BIG or .TXT extension that match the Imported filename. These files will be copied to the Network Directory along with the Imported Image.

#### Big File ON, (Save Big File to Network Also)

> If using the Lumisys 100 scanner capable of scanning BIG files, check this option and the BIG file will be saved along with the reduced image.

#### Net Security ON

> Turns ON/OFF Imaging Network security.

> When Imaging Network security is ON, the Imaging system will make a connection to the Imaging Network Server as a user that is defined in the Imaging Site Parameters File and break the connection when the Image is opened, or fails to open.

> When Imaging Network Security is OFF, Imaging makes no attempt to connect to a network directory. The workstation must have a drive mapped to the Network directory to be able to capture images or the user that is logged in to the workstation must have access to the Imaging Network server. (intended for debugging purposes)

#### Change Timeout Value

> The VistA Imaging Capture Session will time out after a specific time of inaction. That time is set in the IMAGE SITE PARAMETERS File. That setting can be changed for individual workstations with this menu option. The changed setting will remain in effect

> until it is changed again. If the setting is changed to '0' (zero) then the entry from the IMAGE SITE PARAMETERS file will be used as the timeout.

#### Set Workstation's Alternate Video Viewer

> Select this option to open a file selection dialog widow. In this dialog window, select a video file viewer to use for all video files. VistA Imaging displays video files (AVI Files are the only video files supported in V. 2.5) in the VistA Imaging Video Display window by default. For an alternate video viewer to be used for video files, the 'Use Alternate Video Player' radio button must be selected in the Video File Options window.

> The 'Options\|Video File options' menu option opens the 'Video File Options' window. The User can select 'Use Alternate Video Player'.

> If 'Use Alternate Video Player' is selected, all video files will be opened in the video file viewer that is associated with files of type '\*.AVI' defined through the operation system. The System Manager can change the alternate video file viewer for the workstation to a video file viewer selected in the open file dialog window.

# Workstation Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Imaging Workstation Configuration Editor controls many workstation parameters for the VistA Imaging System. This option is only available to the holder of the MAG SYSTEM Security Key.

![](vista-imaging-system-clinical-capture-user-manual/280.png)

## Button/Field Options:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains an explanation of options under Button/Field Options. \[Button / Field Options\] selectable at runtime: NO

> This Section is for options that relate to edit fields and buttons in VistA Imaging Capture. (Currently only the Image description edit field has options.)

> CreateDefaultImageDesc=TRUE default: TRUE:

> In the process of capturing an Image, a description must be entered for the Image. Set this entry = TRUE and the Imaging System will create a default Image description.

> ImageDesc= (Three choices for the ImageDesc entry)

> When the Image description date entry field has the input focus, the cursor can be positioned at various positions and the text can be selected or not selected.

1)  Selected (Windows default)

> Text will be selected and typing by user will overwrite text.

2)  NoSelectCursorEnd

> Text not selected, typing by user will be appended to the end of the text.

3)  NoSelectCursorHome

> Text not selected, typing by user will be inserted at beginning of the text.

> NOTE: You can always type in whatever description you like. This option is intended for anyone, but especially for users capturing groups of images, or many related images. This will allow a default image entry, and additional text appended to it, without the need to first Un-Select the text or reposition the cursor.

#### Copy Options

> \[Copy Options\] selectable at runtime: YES

> CopyMode: default : ThreadStream

> The copy mode entry has three choices that define how the image will be copied to the Tier 1 storage

> Thread : copy is performed in a separate thread. This enables the Clinical Capture application to maintain connection/communication to the VistA System during the image copy.

> ThreadStream: copy is performed in a separate thread similar to the Thread method. A ThreadStream is optimized for speed of copy.

> Normal : copy is performed in the main thread. (This is the method used in Clinical capture versions prior to 151)

> Note: The default entry is ThreadStream. The other entries are available in case of issues. Users can select the older mode of image copy instead of re-installing an older version of Clinical Capture.

## Demo Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[Demo Options\] selectable at runtime: NO

> Open Abstract Window=TRUE default = TRUE

> Set the Open Abstracts Window = TRUE if you want the Abstracts window to always open when you select a demo patient. NOTE: you can open the Abstracts window at any time by clicking the Abstracts button, or selecting the 'View\|Abstracts' menu option on the Imaging Display window.

## Image Association

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[Image Association\] selectable at runtime: YES

> This section of the mag.ini file controls which VistA package the captured image will be associated with and, hence, where the reports associated with the image will be located. Choices include:

> Laboratory =FALSE default=FALSE

> Medicine =FALSE default=FALSE

> Radiology =FALSE default=FALSE

> Surgery =FALSE default=FALSE

> PhotoID =FALSE default=FALSE

> Progress Notes =FALSE default=FALSE

> TeleReader Consult=FALSE default=FALSE

> None =FALSE default=FALSE

> Default=None default=NONE

> The Default item should be set for the package which is most commonly used for image capture from this workstation. The Image Capture window will be initially configured for the default package when the window is opened. Select the package to be changed from the list box shown by clicking it. Use the radio buttons at the bottom to select True or False. The Imaging System Capture window user will be able to select from all Associations set to True.

> To set the default package, select Default from the list box. Select the abbreviation for the default package from the pull-down list shown below. All entries in the Association section have TRUE/FALSE switches. At least one switch must be set to TRUE, and the default specialty should not be set to NONE. Only those entries set to TRUE are selectable by the user at runtime through the menu option Options\|Configuration .

> Setting None=TRUE will allow you to select a User Defined Specialty/Category to associate with the image.

## Image Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ImageFormat\] selectable at Runtime: YES

> The following is a list of all of the possible image types. All entries in the Image Format section have true/false switches. At least one switch must be set to TRUE, and the default image type cannot be set to NONE. Only those entries set to TRUE are selectable by the user at runtime through the menu option 'Options\|Configuration'.

> True Color TGA=TRUE default FALSE True Color JPG=TRUE default FALSE

> 256 Color=TRUE default FALSE

> Xray=TRUE default FALSE

> Xray JPEG=FALSE default FALSE

> Black and White=TRUE default FALSE

> Document TIF Uncompressed=TRUE default FALSE

> Document TIF G4 FAX=TRUE default FALSE

> Motion Video=TRUE default FALSE

> DICOM=TRUE default FALSE

> Audio=TRUE default FALSE

> Default=Xray default NONE

> You can prevent unnecessary confusion for the user, and phone calls for help if you enable ( device =TRUE) for only the Image types that will be captured at this workstation.

> Example: A workstation is connected to a Lumisys Scanner; the site manager has enabled Image Type 'Xray' only. On another workstation attached to a HP ScanJet he has enabled 'True Color JPG' and 'Document TIF G4 FAX'

> Note: The Image format that is chosen by the user is saved with the image. The Image Type determines which Image Viewer to use when displaying the image with VistA Imaging Display.

## Import Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[Import Options\] selectable at runtime: YES/NO

> Type=Copy to Server default 'Convert to TGA' selectable at runtime: NO DefaultImportDir=c:\image: default 'C:\\ selectable at runtime: YES (The default directory of images to import)

> DefaultMask=\*.TGA: default '\*.\*' selectable at runtime: YES (The default mask; only files matching the mask will be listed.)

> The 'Import' input source allows the user to select an existing image file from their local workstation or Network directory to be imported into the VistA Imaging System.

> Importing involves identification of the patient and other image-related information. The import may be done in several different ways:

> The Type entry has 3 choices

1)  Copy to Server
2)  Convert to TGA
3)  Convert File Format to Default

> The Copy to Server mode means that the imported file will be copied to the server, receiving a new name assigned by VistA. The file extension of the copied file will be the same as that of the original file. The file is copied exactly. This option is especially important for a compressed file format such as JPEG. Its use means that the image data is not compressed again, resulting in further loss of quality. The VistA Imaging Display

> software will support the following formats: TGA, TIF, BMP, JPG, PCX, GIF, MAC, MSP, PSD, PCD, PCT (raster images in version 1 and version 2), Sun Raster, WMF (raster only), WPG (raster only). For any other formats, please ask the imaging staff (301-427-3700.)

> The Convert to TGA mode is required at sites that are still operating Imaging version 1.0 display workstations based on Truevision Vista boards. This mode resaves the imported image to the Imaging file server using the TGA file format. This is an uncompressed format.

> The Convert File Format to Default allows sites to convert to a selected ImageType format. The Image will be converted to the selected 'ImageType'. Image Type is selectable at runtime from the menu option 'Options\|Configuration'. Only those types marked as TRUE in the \[ImageType\] section of the MAG.INI file are selectable at runtime. Currently only TGA, TIF, JPG are supported.

> Note: DefaultImportDir, DefaultMask, properties are saved at runtime if the user checks the 'Save setting as default' checkbox on the 'Select Import Directory' Window.

## Input Source

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[Input Source\] selectable at runtime YES

> The VistA Imaging System allows many types of image capture. This section of the MAG.INI files controls the input types that are allowed from a particular workstation. The following input types are supported:

- Lumisys 75 xray scanner
- Lumisys 150 xray scanner
- Meteor Video Capture Board with Millennium VGA board
- TWAIN-TWAIN compliant devices (devices that support a TWAIN interface)
- Import - Import Mode allows the user to select an image that is residing on a disk on the workstation and import it into the VistA Imaging System.
- Three modes of import are supported "Copy to Server", "Convert to TGA" and "Convert File Format to Default". (See the section \[Import Options\])
- ScannedDocument - Twain device capture of 1 bit Document Images.

> Each entry has a TRUE/FALSE switch, which controls user access during an Imaging Capture Session. At least one device MUST have 'device=TRUE'. The default setting MUST be set to something other than NONE. To change values, click the input type you wish to modify. You will see two radio buttons at the bottom of the window. Select the TRUE or the FALSE button. The value will change in the file, for example, Lumisys75=TRUE. Only those entries set to TRUE are selectable by the user at runtime through the menu option 'Options\|Configuration'

> Note : All workstations are capable of Importing an Image. No device is necessary for this type of Image Capture.

> You can prevent unnecessary confusion for the user, and phone calls for help, if you enable ( device =TRUE) only the devices that are available to this workstation for capturing of images.

## Input Source Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[Input Source Options\] selectable at runtime YES

- 256 Color Enabled=FALSE, default FALSE:

> Set the 256 Color Enabled entry = TRUE if the Scanner you are using is capable of scanning 256 Color Images (8-bit color.)

## Login Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[LOGIN Options\] selectable at runtime NO

> LoginOnStartup=TRUE, default TRUE:

> You can set LoginOnStartup=FALSE to disable the automatic login to the VISTA System. You can always login or logout by selecting the 'File\|Login', 'File\|Logout' Options.

> AllowRemoteLogin=FALSE default FALSE

> This setting determines whether the initial login ( if LoginOnStartup=TRUE ) will display a list of Remote VistA Sites to choose from.

> Local VistA=BROKERSERVER default: BROKERSERVER

> First, the Local VistA site must be defined. This is the VAMC that the Imaging System will connect to. The name typed into the edit box for the local site must match exactly an entry in the workstation's c:\windows\hosts. file.

> Local VistA port=9200 default 9200

> This entry refers to the TCP/IP port on the VISTA System that the Kernel Broker 'listener' process is using. Refer to the Kernel Broker documentation. Usually the port is 9200. If no entry is made 9200 is used.

## Medicine Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[Medicine Options\] selectable at Runtime YES

> Capturing images and associating the image with a Medicine procedure can be made a little smoother with the following settings.

> Create New/List Existing= (choice of 2) default=Create New

1)  CreateNew
2)  ListExisting

> Create Procedure stub first=FALSE default=FALSE

> If the Imaging workstation will always be associating the captured images to New medicine procedures, then select Create New, this will set the Medicine procedure selection window default to Create /New procedure.

> If 'ListExisting' is selected then the medicine procedure selection window will default to showing a list of patient procedures for the selected Medicine SubSpecialty.

> When a captured image is associated with a New medicine procedure, the medicine procedure isn't normally created until the first image is saved. If the user has a need to edit the medicine procedure text before the image is saved set Create Procedure stub first=TRUE. The user will have to be logged into VistA Imaging to edit the procedure text.

## Remote Site Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[Remote Site Options\] selectable at runtime NO

> RemoteImageViewsEnabled default=TRUE

> The user can choose to disable Remote Image Views by setting this value to false.

## Save Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SaveOptions\] selectable at runtime YES Default=Group (2 Choices for Default) default=GROUP

1)  Group
2)  Single

> The user of the Imaging System Capture window has the option of saving multiple images as a 'Study Group' or of saving the images as 'Single' images. The default value is SINGLE . You can set the switch to GROUP or SINGLE.

## SYS_AutoUpdate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SYS_Autoupdate\]

> This section of the configuration file is no longer valid. VistA Imaging Auto updating is no longer supported. For other automatic installation methods, consult the *VistA Imaging Installation Guide*.

## SYS_Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SYS_Configurations\] selectable at runtime YES 1=Import,JPEG,Med,Group=+import+TrueColorJPG+medicine+imagegroup++online

> 2=Import,JPEG,Lab,Single=+import+TrueColorJPG+laboratory+NoImageGroup++online

> These entries are modified by the Imaging Application: do not modify these yourself. These entries keep information for the user definable 'Hot Buttons'. The 'Hot Buttons' allow the user to quickly change the Input Type, Image Type, Specialty, Single/Group and Mode settings to saved values. 'Hot Buttons' are described in the 'Imaging Workstation Configuration' Window section.

> By creating Hot Buttons for a Capture workstation ( creating Hot Buttons is optional ) you will allow the user to switch configurations with one click of the mouse. The user will not have to take the time to select each setting from the list of available Image Types, Input Types, Specialties, etc.

> Note: The entries shown here are examples only. When you first setup an Imaging Workstation for Capture, there are no Capture configurations defined.

## SYS_Fonts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SYS_Fonts\] selectable at runtime NO

> This is used by the Imaging System to record the fonts of certain controls and windows in the Imaging Applications.

> Some of the controls that the font can be changed are: Report Window, Patient Lookup selection list, Surgery selection list and others.

> Do not modify these entries yourself, it is maintained by the imaging system.

## SYS_LastPositions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SYS_LastPositions\] selectable at runtime NO

> This is used by the Imaging System to record the last positions of the application's windows. Do not modify these entries yourself, it is maintained by the imaging system.

## SYS_Meteor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[Sys_Meteor\] selectable at runtime YES

> These entries are modified by the Imaging Application: do not modify these settings yourself. These entries are used by the system as parameters for capturing images with the Meteor Input Type.

## SYS_SETTINGS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SYS_SETTINGS\] This section is no longer applicable. It will be removed in a future patch.

## SYS_TWAIN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SYS_TWAIN\]

> Default = \<TWAIN Device Name\>

> This entry is modified by the Imaging Application: do not modify this setting yourself. This is the default TWAIN device used by Clinical Capture.

## TeleReader Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[TeleReader Options\] selectable at runtime: YES

> HideDiscontinuedConsults default = TRUE

> Set this to True to hide discontinued consults from the Telereader worklist.

## VISTA MUSE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[VISTAMUSE\] selectable at runtime: YES

> The VISTAMUSE section holds information specific to the VistA MUSE windows. These windows interface with the Marquette MUSE Database to access patient EKG’s.

> DEBUG default=FALSE

> Change Debug = TRUE to enable the MUSE EKG debug functions.

## Workstation Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[Workstation Settings\] selectable at runtime: NO These are workstation settings that relate to various areas of VistA Imaging. ID=IRD default=UNKnown

> Workstation ID, i.e. 'IAD' a unique identifier for this workstation, used in the Imaging Access Log File (2006.95.)

> Location=Ruth's_Desk default=UNKnown:

> Location of the workstation, a unique free text field, i.e. "GI Conference Room." Abstracts created=True default=TRUE

> This should be set to True if the Image Abstract is to be created by the workstation. If set to FALSE the Image Abstract will be created by the Imaging Background Processor Workstation.

> Save Radiology BIG file=True default=FALSE

> This should be set to True if the 2k x 2k scanned x-ray file is to be saved along with the 1k x 1k file and the abstract.

> Display JukeBox Abstracts=TRUE, default TRUE:

> Displaying Abstracts that are located on the JukeBox takes longer than if the abstracts are on the magnetic image server. To stop the display of Jukebox Abstracts set this entry = FALSE.

> Log Session Actions=FALSE default FALSE

> A record of all Actions performed by the user of Imaging System display window can be saved by setting this entry = TRUE.

> MUSE Enabled=TRUE default FALSE

> MUSE Demo Mode=FALSE default FALSE

> Not for general use. This setting is for Demonstrations given by the Imaging Implementation team.

> Allow Image SaveAS=FALSE default FALSE

> Not for general use. This setting is for saving images to the local drive, to be used in demonstrations of the Imaging system.

> Fake Name=Fake,PatientName default 'Fake,PatientName'

> Allow Fake Name=TRUE default FALSE

> The Fake Name will be used on all Imaging Display windows and reports from VistA. Only Textual changes are made. Images that have the patient name visible will still have the patient name visible in this type of demo.

> This is a way of demonstrating the Imaging system to an audience using a Real Patient. This is not for general use.

> Note: When displaying images using Fake,PatientName, the Images are the Real images for the patient and for Images that have the patient name burned into the image, the name will be visible. This is typical for Ultrasound and Angiography/Fluoroscopy images. This mode of Demonstration should be used with caution. The Images to be shown in a demonstration of this type should be viewed beforehand to make sure the patient name is not visible.

> Workstation Timeout minutes=120 default 0

> This setting if other than 0 (zero) will override the Imaging application timeout fields in the Imaging Site Parameters File. It will apply to all Imaging applications run on this workstation.

> i.e. Display, Capture, VistARad.

> If this setting is 0 (zero) then the timeouts that are entered in the Imaging Site Parameters File will apply.

> \[Workstation Settings\] selectable/changeable at runtime YES

> Use Alternate Video Viewer=FALSE default FALSE

> VistA Imaging will display Video files (only video files of type AVI) in a custom Video Window. An Alternate viewer can be selected. Set this value to TRUE and video files will display in the default video viewer defined for the workstation. (see "Alternate Video Viewer")

> If no alternate viewer has been defined for this workstation then the video file will display in the default viewer defined for the Windows operating system. This setting is changeable from the Video File Options window.

> Alternate Video Viewer="" default ""

> Select the menu option 'System Manager\|Set Workstation's Alternate Video Viewer' to define a specific video viewer for this workstation.

> Play Video File=FALSE default FALSE

> Setting this value to TRUE will automatically play the video file when selected. This setting is changeable from the Video File Options window.

> VistA Imaging Capture Application:

> The following settings apply to VistA Imaging Capture:

> \[Workstation Settings\] selectable/changeable at runtime YES Import List height=123

> The last height of the 'Import file list' is saved. The height can be changed by 'dragging' the separator bar directly above the Import list.

> LongDesc height=80

> The last height of the 'Long Description' field is saved. The height can be changed by 'dragging' the separator bar directly above the Long description field.

> Config Toolbar=TRUE default TRUE

> The visible state of the Configuration Toolbar is saved. Select (check) the Capture menu option 'Options\| Saved Configurations Toolbar' to display the toolbar.

> Settings Toolbar=TRUE default TRUE

> The visible state of the Settings Toolbar is saved. Select (check) the Capture menu option Options\|Current Settings Toolbar to display the Settings Toolbar.

> Large Slider Controls=TRUE default TRUE

> The size of the slider controls is saved. Slider controls are used to change the Brightness, Contrast and Zoom values for the Image. Select (check) the Capture menu option 'Options\|Large Slider controls' to change the size.

> Close Quick Setting=TRUE default TRUE

> Capture Hints=TRUE default TRUE

> Select (check) the Capture menu option 'Options\| Show Hints' to have hints display when the mouse is above a control. This value is saved.

> Capture Confirmation=TRUE default TRUE

> Select (check) the Capture menu option 'Options\| Show Confirmation messages' to activate the confirmation window function. When active, a confirmation window will be displayed before images are saved to VistA.

> Capture Maximized=TRUE default FALSE

> This setting is saved when the Capture application is closed. If the Capture window was maximized when it was closed, it will be maximized when it is started again.

> Data Entry Width=300

> The width of the 'Data Entry panel' is saved. ToolBarPosition=TOP default TOP

> In the Capture Application, the Image manipulation toolbar can be repositioned. The last position is saved. To reposition, right-click the toolbar to activate the shortcut menu and select from Top, Left or Right.

# Utilities Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section explains the Utilities Menu options located in the Menu Bar.

![](vista-imaging-system-clinical-capture-user-manual/281.png)

## Controlled Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section explains the Controlled Image option under the utilities Menu. Below is an explanation of Controlled Image as well as how to capture controlled images using the Utilities Menu.

> Shown below is the default abstract for Controlled Image:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>![](vista-imaging-system-clinical-capture-user-manual/282.png)</th>
<th><blockquote>
<p>This abstract is displayed when an Image is marked as ‘Controlled’ A controlled image won’t display in the Abstracts window. But will display normally when selected. This gives the Physician a visual indication that there is something sensitive about the Image.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The Controlled Image field can be used to specify that the image contains graphics or data of a sensitive nature. The Display Client gives the user a visual indication through the use of icons and abstracts that the image is controlled.

> The Controlled Image property gives the site the opportunity of marking an Image as controlled. In the image list and tree view controls of the Imaging Display Client, controlled images will have an icon displayed in the first column that distinguishes it as controlled. The Abstract for a controlled image will not be shown. Instead of the abstract, a bitmap signifying that this image is controlled will be shown. When the image is opened, it will display as always. The controlled value can be changed for an image in the Image Index Edit window. Users with the Security Key ‘MAG EDIT’ will have access to the Index Edit window.

## Setting the Controlled Image Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Imaging Capture:

#### Capturing Single Image

> In VistA Imaging Capture, when you are capturing a single image, before you click the ‘Capture’ button, select the menu option ‘Utilities’ \| ‘Controlled Image’. The phrase ‘Controlled Image’ will be displayed to the left of the Capture Button as a visual indication that the image about to be captured will be flagged as controlled.

#### Capturing Group Using Batch Capture

> In VistA Imaging Capture, when you are capturing a batch of images as an Image Group, before you click the ‘Capture’ button, select the menu option ‘Utilities’ \| ‘Controlled Image’. The phrase ‘Controlled Image’ will be displayed to the left of the Capture Button as a visual indication that the Image Group about to be captured will be flagged as controlled.

#### Capturing Group (not using batch capture)

> In VistA Imaging Capture, when you are capturing multiple images as an Image Group, before you click the ‘Capture’ button, select the menu option ‘Utilities’ \| ‘Controlled Image’. The phrase ‘Controlled Image’ will be displayed to the left of the Capture Button as a visual indication that the Image about to be captured will be flagged as controlled. This gives a way to mark only certain images of the Group as ‘Controlled’.

# Image Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Image Menu has options for Image manipulation. See below for explanation of the available options.

![](vista-imaging-system-clinical-capture-user-manual/283.png)

#### Zoom

![](vista-imaging-system-clinical-capture-user-manual/284.png)

> Zoom sub-menu has options to size/re-size an image. Click To…

> Zoom In to zoom in to an image Zoom Out to zoom out of an image

> Fit to Width to fit the image to the window width (horizontal)

> Fit to Height to fit the image to the height of the window (vertical)

> Fit to Window to fit image to the entire window (vertical and horizontal) Actual Size to show image in its original size

#### Mouse

![](vista-imaging-system-clinical-capture-user-manual/285.png)

> The Mouse sub-menu has editing options available to size/re-size an image. Click To…

> Pan to pan image by dragging mouse

> Magnify to magnify an image where the mouse is clicked

> Zoom to zoom into an area of the image selected with the mouse Pointer to go back to mouse pointer

#### Rotate

![](vista-imaging-system-clinical-capture-user-manual/286.png)

> The Rotate sub-menu has options to change image orientation. Click To…

> Right to rotate an image to the right

> Left to rotate an image to the left

> 180 to rotate an image 180 degrees Flip Horizontal to flip an image horizontally Flip Vertical to flip an image vertically

#### Scroll

![](vista-imaging-system-clinical-capture-user-manual/287.png)

> The Scroll sub-menu has options to scroll through the image. Click To…

> Top Left scroll to the top left corner of the image Top Right scroll to the top right corner of the image Bottom Left scroll to the bottom left corner of the image

> Bottom Right scroll to the bottom right corner of the image Left scroll to the left

> Right scroll to the right

> Up scroll up

> Down scroll down

#### Page

![](vista-imaging-system-clinical-capture-user-manual/288.png)

> The Page sub-menu has options to scroll through multiple pages, if available Click To…

> First go to first image in study

> Prev go to previous image

> Next go to next image

> Last go to last image

#### Reset

> Resets image to its original size.

#### Clear

> Clears image from the capture window.

#### Contrast/Brightness

![](vista-imaging-system-clinical-capture-user-manual/289.png)

> The Contrast/Brightness sub-menu has options to adjust image contrast and brightness. Click To…

> Contrast + increase image contrast

> Contrast - decrease image contrast

> Brightness + increase image contrast

> Brightness - decrease image contrast

#### Other options:

![](vista-imaging-system-clinical-capture-user-manual/290.png)

> Invert invert an image

> Reset reset image back to the original state

> Clear clears image from the screen

> Open Pan Window opens a pan image window. Pan window indicates the area within

> the image that is being examined

> DeSpeckle despeckle image

> DeSkew deskew image - straighten images that have been captured at an angle

> Copy to Clipboard copy image Paste from Clipboard paste image

# Help Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vista-imaging-system-clinical-capture-user-manual/291.png)

## VistA Imaging Capture User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Opens the current User Guide from the VistA Imaging SharePoint.

## Error Code Lookup…

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Opens the 'Error Lookup' window. A short description will be displayed for the error code entered.

![](vista-imaging-system-clinical-capture-user-manual/292.png)

## About…

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Displays Version information for VistA Imaging Clinical Capture.

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: If the ‘CAPTURE KEYS’ site parameter has been initialized, (set to True), the following keys will need to be assigned appropriately.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Capture-related Security Keys</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAG CAPTURE</td>
<td>Allow capture of clinical images without a VistA Package association (i.e. ‘Patient Only: Clinical’ on the Imaging Capture configuration window).</td>
</tr>
<tr class="even">
<td>MAG NOTE EFILE</td>
<td>User can electronically file notes without an electronic signature from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP ADMIN</td>
<td>Allow capture of administrative images to image association ‘Patient Only : Administrative’</td>
</tr>
<tr class="even">
<td>MAGCAP CP</td>
<td>Allow capture of Clinical Procedure images.</td>
</tr>
<tr class="odd">
<td>MAGCAP LAB</td>
<td>User can capture Laboratory images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP MED C</td>
<td>User can capture Cardiology images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP MED G</td>
<td>User can capture GI images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP MED GEN</td>
<td>User can capture Generic Medicine images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP MED H</td>
<td>User can capture Hematology images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP MED HI</td>
<td>User can capture Internal Medicine / Hematology images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP MED I</td>
<td>User can capture Internal Medicine images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP MED N</td>
<td>User can capture Neurology images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP MED P</td>
<td>User can capture Pulmonary / Endoscopy images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP MED PF</td>
<td>User can capture Pulmonary Function Test images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP MED R</td>
<td>User can capture Rheumatology images from the Imaging Capture workstation.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Capture-related Security Keys</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAGCAP MED Z</td>
<td>User can capture Consult images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP PHOTOID</td>
<td>User can capture Photo ID images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP RAD</td>
<td>User can capture Radiology images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP SUR</td>
<td>User can capture Surgery images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP TIU</td>
<td>User can capture TIU images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP TRC</td>
<td>User can capture images associated with a TelerReader Consult from the Imaging Capture workstation.</td>
</tr>
</tbody>
</table>

# Appendix A: Supplemental Logon Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When logging in to Clinical Capture you may see some screens that are not described in the section [*Logging In and Starting Clinical Capture*.](\l) This appendix describes an alternate logon method, which includes these screens. You will see these screens when using remote login (logging into a VistA system at another site) and if the site has different divisions to which your user can log in.

> ![](vista-imaging-system-clinical-capture-user-manual/293.png)![](vista-imaging-system-clinical-capture-user-manual/294.png)To log into Clinical Capture as a standalone application (not from CPRS), from the workstation do the following:

- Double-click the Capture shortcut on the Windows desktop.

> If a shortcut is not available, click , then choose All Programs \| VistA Imaging Programs \| VistA Imaging Clinical Capture 32-bit.

- Select the server you have been instructed to log in to from the Connect To window. Then, click OK.

![](vista-imaging-system-clinical-capture-user-manual/295.png)

- If the server is *not* listed in the drop down list of the Connect To window, select New from the list and enter the Address and Port Number in the Add Server window that displays. You can get the server information from either your site administrator or by calling the help desk. Then, click OK.

![](vista-imaging-system-clinical-capture-user-manual/296.png)

- Select a certificate and click on the OK button.

![](vista-imaging-system-clinical-capture-user-manual/297.png)

- Next, enter your PIN and click on the OK button.

![](vista-imaging-system-clinical-capture-user-manual/298.png)

> Upon successful authentication and login, the user will be allowed to continue to the application. When an attempt to log in with PIV/PIN fails to authenticate 2FA, the application will revert the user to the Access/Verify screen. If the VistA Sign-on box displays, type your access and verify codes in the Access Code and Verify Code boxes, then click OK.

> ![](vista-imaging-system-clinical-capture-user-manual/299.png)

- If the site has multiple divisions and if the account you are using to log into VistA can log into these divisions, the Select Division window displays, prompting you to select the division in which you want to log on. If you see this window, select your division and click OK.

![](vista-imaging-system-clinical-capture-user-manual/300.png)

> The VistA Imaging Capture window appears as shown in the following screenshot. Yours may be different depending on Capture buttons and how the application has been configured.

![](vista-imaging-system-clinical-capture-user-manual/301.png)

# Appendix B: Clinical Context Object Workgroup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CCOW Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Clinical Context Object Workgroup (CCOW) is an HL7 standard for clinical context management which synchronizes applications so that they are mutually aware of common elements. Clinical Capture is CCOW-compliant and uses this standard to interface with CPRS, Clinical Display, TeleReader, and other CCOW-compliant applications.

> CCOW maintains user context and patient context.

- Because CCOW maintains user context, when you are using a CCOW-compliant application (such as CPRS) and you start another CCOW-compliant application (such as Clinical Capture) you will be automatically signed on to the second application will automatically sign on to VistA with the same user credentials as the first.
- Because CCOW maintains patient context when you select a patient in CPRS or Clinical Display, the same patient is also selected in the other application. You can suspend the patient context and select a different patient in Clinical Capture. When the patient context has been suspended, you can re-establish the connection with the CCOW vault (where the patient context is stored) and get that patient context. You can also set the patient context in the CCOW vault. When you set the patient context from Clinical Capture, the CCOW patient that is open in Clinical Capture becomes the CCOW patient and that patient gets displayed in CPRS and/or Clinical Display.

> To learn more about CCOW follow this link: <u>REDACTED</u>

## Patient Context in Clinical Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Clinical Capture enables you to show patient context, suspend patient context, get patient context, and set patient context. You perform these actions manually through the options of the Context menu. The following table explains these options.

| Menu Option    | Description                                                                                                                                                                                                                                                                    |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Show Context       | Use this option to display the current patient (CCOW patient) in the message history log of the Clinical Capture main screen.                                                                                                                                                      |
| Suspend Context    | Use this option to break the connection to the patient in the CCOW vault (the CCOW patient). Suspending the context lets you select a different patient in Clinical Capture from the one in the other CCOW-compliant applications that are running (CPRS and/or Clinical Display). |
| Resume Get Context | Use this option to re-establish the connection to the CCOW vault and to display the patient that is in the CCOW vault in Clinical Capture.                                                                                                                                         |
| Resume Set Context | Use this option to re-establish the connection to the CCOW vault and to change the patient in vault with the one that is selected in Clinical Capture. The patient will be displayed in the other CCOW-compliant applications that are running (CPRS and/or Clinical Display).     |

> These icons, which appear in the Clinical Capture main screen, next to the Select Patient button, indicate that Clinical Capture is using CCOW and the patient status of the patient context in Clinical Capture.

|     | Clinical Capture is in context. The patient in Clinical Capture is the patient in the CCOW vault. |
|-----|---------------------------------------------------------------------------------------------------|
|     | Context is suspended. The patient in Clinical Capture is not the patient in the CCOW vault.       |
|     | Context is changing.                                                                              |

# Appendix C: Discontinued Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following menu options have been taken off the main menu of the Capture Application.

> The design and functionality of the Clinical Capture client has changed over the years, and the following menu items no longer provide needed functionality and have been removed.

- Options \| Import Directory Options This was a duplicate menu item.
- Options \| Field Tabbing Sequence Functionality no longer needed.
- Tools \| Refresh Index lists Functionality no longer needed.
- Tools \| Realign Index Fields Functionality no longer needed.

#### Field 'Tabbing' Sequence

> Use the Field 'Tabbing' Sequence menu option to change the position and tabbing order of the Clinical Capture controls. Clicking this option opens the Tabbing Sequence editor with the current tabbing order of the fields. This is illustrated in the following image.

![](vista-imaging-system-clinical-capture-user-manual/302.png)

> Select a field and press the Up or Down arrows to change the tabbing order as preferred.

## The Help Menu and Submenu items have changed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Overview:

> Context help has always been available to the user. To use context help, position the cursor in an edit field or select a button and press the F1 Key. However, the help topics displayed in context- sensitive help are out-of-date.

> The Clinical Capture User Manual is an on-line PDF document that has been kept up-to-date. A new Help Menu item has been added that gives the user the ability to open this user manual.

> Other Help menu items are no longer applicable. They refer to older help documents that are out-of-date.

> The following Help Submenu items have been removed. Help \| Contents

> Help \| Imaging Capture Window Help \| System Manager Help Help \| Document Scanning

> Help \| Admin/Means Test1

> Help \| Version 2.5 Testing Updates Help \| Use Internet Explorer for Help

> Note: The user has the option of showing the menu items that have been removed. A configuration setting exists to display or hide the menu items that have been removed.

> In the Workstation Configuration Editor select the 'Workstation Settings' section. In that section, select the property 'Show Old Menu Items'. Change the value to “TRUE”. The removed menu items will be visible the next time you open Clinical Capture.

> This section explains the discontinued Help Menu options in VistA Imaging Capture.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Contents</th>
<th>Opens the contents page of On-Line help for VistA Imaging.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Imaging</p>
<p>Capture Window</p></td>
<td>Opens the Imaging Capture Window page of On-Line Help.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>System Manager help</th>
<th><p>Opens the 'Options for MAG SYSTEM key holders help topics.</p>
<p>![](vista-imaging-system-clinical-capture-user-manual/303.png)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Document Scanning</td>
<td><p>Displays 'DocScan.hlp' help file.</p>
<p>![](vista-imaging-system-clinical-capture-user-manual/304.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Admin/Means Test</th>
<th><p>Displays the Admin/Means Test Help file</p>
<p>![](vista-imaging-system-clinical-capture-user-manual/305.png)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Use Internet Explorer for help</td>
<td><p>Launches the Internet Explorer to open help files</p>
<p>![](vista-imaging-system-clinical-capture-user-manual/306.png)</p></td>
</tr>
</tbody>
</table>