---
title: PIMS Version 5.3 User Manual - Menus, Intro & Orientation, etc.
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Menus, Intro & Orientation, etc.
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: active
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 6
description: The Scheduling module of the PIMS Package is designed to assist in the set-up of clinics, scheduling of patients for clinic appointments, and the collection of an assortment of related workload data for reporting purposes. The Scheduling Menus, Intro & Orientation functionality provides the End-User
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - report
  - class
  - show
  - table
  - high
  - risk
  - health
  - mental
  - clinic
  - proactive
page_count: 0
word_count: 12034
section_count: 37
table_count: 12
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/PIMS_User_Manual-Menus_Intros_Orientation.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/PIMS_User_Manual-Menus_Intros_Orientation.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

## Table of Contents

  - [Orientation](#orientation)
  - [Intended Audience](#intended-audience)
  - [Legal Requirements](#legal-requirements)
  - [Disclaimers](#disclaimers)
  - [Documentation Conventions](#documentation-conventions)
  - [Documentation Navigation](#documentation-navigation)
  - [Assumptions](#assumptions)
  - [How to Use this Manual](#how-to-use-this-manual)
  - [On-line Help System](#on-line-help-system)
  - [Definitions, Acronyms, and Abbreviations](#definitions-acronyms-and-abbreviations)
  - [## VistA Documentation](#vista-documentation)
  - [General Support](#general-support)
  - [Introduction](#introduction)
  - [Use of the Software](#use-of-the-software)
  - [SD\5.3\588 Patch - High Risk Mental Health Proactive Report](#sd53588-patch-high-risk-mental-health-proactive-report)
  - [New Options](#new-options)
  - [High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] option](#high-risk-mh-proactive-adhoc-report-sd-mh-proactive-ad-hoc-report-option)
  - [High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] option](#high-risk-mh-proactive-nightly-report-sd-mh-proactive-bgj-report-option)
  - [Modified Options](#modified-options)
  - [High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] Option](#high-risk-mh-no-show-adhoc-report-sd-mh-no-show-ad-hoc-report-option)
  - [High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] option](#high-risk-mh-no-show-nightly-report-sd-mh-no-show-nightly-bgj-option)
  - [SD\5.3\578 Patch – High Risk Mental Health No Show Report](#sd53578-patch-high-risk-mental-health-no-show-report)
  - [New Options](#new-options-1)
  - [High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] option](#high-risk-mh-no-show-adhoc-report-sd-mh-no-show-ad-hoc-report-option-1)
  - [High Risk MH No-Show Nightly Report \[SD MH NO SHOW Nightly BGJ\] option](#high-risk-mh-no-show-nightly-report-sd-mh-no-show-nightly-bgj-option-1)
  - [Scheduling Menus](#scheduling-menus)
  - [Ambulatory Care Reports Menu](#ambulatory-care-reports-menu)
  - [Appointment Menu](#appointment-menu)
  - [Automated Service Connected Designation Menu](#automated-service-connected-designation-menu)
  - [Outputs Menu](#outputs-menu)
  - [## Supervisor Menu](#supervisor-menu)
  - [HRMHP No Show and Proactive Options & Features](#hrmhp-no-show-and-proactive-options-features)
  - [ACRP Database Conversion](#acrp-database-conversion)
  - [Actions Available from the CST Detail Screen](#actions-available-from-the-cst-detail-screen)
  - [Military Time Conversion Table](#military-time-conversion-table)
  - [Glossary](#glossary)
Department of Veterans AffairsOffice of Information and Technology (OIT)
![](pims-version-5-3-user-manual-menus-intro-orientation-etc/001.png)
Patient Information Management System (PIMS)Scheduling Menus, Introduction & Orientation ModuleUSER MANUALVersion 5.3
December 2020
Revision History
The following table displays the revision history for this document. Revisions to the documentation are based on patches, style updates, and new versions released to the field.
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 38%" />
<col style="width: 15%" />
<col style="width: 21%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Revision Dates</td>
<td>Page #</td>
<td>Description</td>
<td>Project Manager</td>
<td>Technical Writer</td>
</tr>
<tr class="even">
<td>Oct 2020</td>
<td>All</td>
<td><p>VistA Scheduling Graphical User Interface (VS GUI) patch:</p>
<p>Release 1.7.1 R1/SD*5.3*745 and 751 released 10/1/20 added menu option</p>
<p>Release 1.7.2.1 R2/SD*5.3*756 and 757 released 12/9/2020</p></td>
<td>REDACTED</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>Aug 2020</td>
<td>All</td>
<td><p>VistA Scheduling Graphical User Interface (VS GUI) patches:</p>
<p>SD*5.3*723 released 11/6/19</p>
<p>SD*5.3*731 released 11/19/19</p>
<p>SD*5.3*734 released 12/9/19</p>
<p>Release 1.6.0 released 12/17/19</p>
<p>SD*5.3*732 IOC only release 11/20/19</p>
<p>SD*5.3*740 released 1/30/20</p>
<p>SD*5.3*737 released 3/9/20</p>
<p>SD*5.3*744 released 3/25/20</p>
<p>SD*5.3*755 IOC only release 6/8/20</p>
<p>Release 1.7.0.2/694/695/762 released 8/19/20</p></td>
<td>REDACTED</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>Oct 2018</td>
<td><a href="#p20">20</a></td>
<td>Updated to reflect changes from patch SD*5.3*640, ACRP and APM HL7 Shutdown. This includes adding notations regarding the ACRP and APM transmissions and related menu options that are being disabled.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/2013</td>
<td>All</td>
<td><p>Added Vista Scheduling Patch SD*5.3*588, which adds two new Proactive reports, SD MH PROACTIVE BGJ REPORT and SD MH PROACTIVE AD HOC REPORT.</p>
<p><strong>NOTE: These reports are not part of the Scheduling Menus, Introduction &amp; Orientation Module, they are Stand-Alone Menu Options.</strong></p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>04/18/2012</td>
<td></td>
<td><p>Added Vista Scheduling Patch SD*5.3*578. It contained options titled SD MH NO SHOW AD HOC REPORT and SD MH NO SHOW NIGHTLY. These Scheduling Report options appear in the primary and secondary menu options.</p>
<p>Added screen printouts for new options in this Version 5.3 release. This manual has been updated to the latest Technical Publication Standards of OIT.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/25/2010</td>
<td></td>
<td>SD*5.3*568 – Added two new options to the SDSUP Menu: “Edit Clinic Stop Code Name- Local Entries Only” option and the “Clinic Edit Log Report” option.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>01/29/2009</td>
<td></td>
<td>Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/01/2008</td>
<td></td>
<td>DG*5.3*779 - Added New Enrollee Appointment Request Management Menu to the Appointment Menu</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/09/2007</td>
<td></td>
<td>Added Automated Service Connected Designation Menu to the Scheduling menu and referred users to the ASCD site in the VistA Documentation Library</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/07/2007</td>
<td></td>
<td>Removed Transitional Pharmacy Benefit Deferred Appt Record option from Outputs Menu</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>03/07/2007</td>
<td></td>
<td>Removed PCMM Reports Menu Documentation – PCMM now listed separately in the VistA Documentation Library</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/22/2007</td>
<td></td>
<td>SD*5.3*466 - Ambulatory Care, Phase II enhancements</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>
Table of Contents
List of TABLES
List of Figures

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scheduling Module is available on-line to a wide range of users throughout VA Medical Centers nationwide. It is integrated with the VA FileMan, which in turn allows the extraction of ad hoc reports by the following listed audiences.

Through Scheduling, necessary National Patient Care Database (NPCDB) workload is transparently collected and may be transmitted to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)).

Options described in this Scheduling Menus, Intro, and Orientation manual supply Users with tools that produce a variety of reports, direct data collection and distribution, and can generate notification / letters pertinent to Scheduling procedures. These Scheduling Report options appear in the primary and secondary menu options. The following are document conventions.

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audiences are listed below. This Scheduling module assists in the set-up of clinics, scheduling of patients for clinic appointments, and the collection of an assortment of related workload data for reporting purposes.

<span id="_Toc54883336" class="anchor"></span>Table : Intended Audience

| READERS/USERS                                               | AUDIENCEs |
|-------------------------------------------------------------|-----------|
| PRODUCT SUPPORT (PS) PERSONNEL                              | X         |
| OFFICE OF INFORMATION AND TECHNOLOGY (OIT)                  | X         |
| PRODUCT DEVELOPMENT (PD)—VISTA LEGACY DEVELOPMENT TEAMS     | X         |
| AUTOMATED DATA PROCESSING APPLICATION COORDINATOR (ADPACS)  | X         |
| HELP DESK PERSONNEL/INFORMATION TECHNOLOGY (IT) SPECIALISTS | X         |

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special legal requirements involved in the use of VistA software.

## Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides an overall explanation of how to use Scheduling software. Specifically it describes the outputs of this software and the various option the User may choose. There are a myriad of reports that can be viewed and printed. No attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA websites on the Internet and VA Intranet for a general orientation to VistA. For example, go to the Office of Information & Technology (OIT) VistA Development VA Intranet website: [REDACTED](http://vista.med.va.gov)

<span id="_Toc54883337" class="anchor"></span>Table : Disclaimers

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pims-version-5-3-user-manual-menus-intro-orientation-etc/002.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you can find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

## Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material. Various symbols/terms are used throughout the document to alert the reader to special information. The following table gives a description of each of these symbols/terms:

<span id="_Toc54883338" class="anchor"></span>Table : Documentation Conventions

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Symbol</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>![](pims-version-5-3-user-manual-menus-intro-orientation-etc/003.png)</td>
<td><p><strong>NOTE/REF:</strong> Used to inform the reader of general information including references to additional reading material.</p>
<p>In most cases you will need this information, or at least it will make the installation smoother and more understandable. Please read each note <em>before</em> executing the steps that follow it!</p></td>
</tr>
<tr class="odd">
<td>![](pims-version-5-3-user-manual-menus-intro-orientation-etc/004.png)</td>
<td><strong>CAUTION, DISCLAIMER, or RECOMMENDATION:</strong> Used to inform the reader to take special notice of critical information.</td>
</tr>
</tbody>
</table>

Descriptive text is presented in a proportional font (as represented by this font). "Snapshots" of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.

User's responses to online prompts and some software code reserved/key words will be bold typeface and highlighted in yellow. Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                   |                                                                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pims-version-5-3-user-manual-menus-intro-orientation-etc/005.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box that point to specific areas of a displayed image. |

Special Typeface will indicate a command and can be used as follows:

- All computer keys when referenced with a command (e.g., "press Enter" or "click OK").
- All references to computer dialogue tab or menu names (e.g., "go to the General tab" or "choose Properties from the Action menu").
- All values entered or selected by the user in computer dialogues (e.g., "Enter 'xyz' in the Server Name field" or "Choose the ABCD folder entry from the list").
- All user text (e.g., commands) typed or entered in a Command-Line prompt (e.g., “Enter the following command: CD xyz").
- Italicized Typeface will use Emphasis (e.g., do not proceed or you must do the following steps).
- All references to computer dialogue or screen titles (e.g., "in the Add Entries dialogue…").
- All document or publication titles and references (e.g., "see the ABC Installation Guide").
- Step-by-Step Instructions—for documentation purposes, explicit step-by-step instructions for repetitive tasks (e.g., "Open a Command-Line prompt") are generally only provided once.
- For subsequent steps that refer to that same procedure or task, please refer back to the initial step where those instructions were first described.

Conventions for displaying TEST data in this document are as follows:

- The first three digits (prefix) of any Social Security Numbers (SSN) must begin with either "000" or "666".
- Patient and usernames are formatted as \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in LSRP test patient and usernames would be documented as follows: LSRPPATIENT, ONE; LSRPPATIENT, TWO; LSRPPATIENT, THREE; etc.

## Documentation Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Document Navigation—this document uses Microsoft® Word's built-in navigation for internal hyperlinks. To add back and forward navigation buttons to your toolbar, do the following:

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

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Menu, Introduction & Orientation Module User Manual provides the User with powerful tools to generate a wide variety of scheduling-related reports and letters pertinent to procedures and follow ups. The User must understand current VA procedures and policies as they pertain to Normal Scheduling Operations. This software is easy to use and many options employ radio – button choices.

## How to Use this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Scheduling User Manual is provided in Adobe Acrobat PDF (portable document format) files. The Acrobat Reader is used to view the documents. If you do not have the Acrobat Reader loaded, it is available from the VistA Home Page, “Viewers” Directory.

Once you open the file, you may click on the desired entry name in the table of contents on the left side of the screen to go to that entry in the document. You may print any or all pages of the file. Click on the “Print” icon and select the desired pages. Then click “OK”. Each menu file contains a listing of the menu, a brief description of the options contained therein, and the actual option documentation. The option documentation gives a detailed description of the option and what it is used for. It contains any special instructions related to the option.

Other related materials are the PIMS Technical Manual, the PIMS Installation Guide, and the PIMS Release Notes. The PIMS Technical Manual is provided to assist OIT personnel in maintenance of the software. The Installation Guide provides assistance in installation of the package, and the Release Notes describe any modifications and enhancements to the software that are new to the version.

## On-line Help System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the format of a response is specific, there usually is a HELP message provided for that prompt. HELP messages provide lists of acceptable responses or format requirements that provide instruction on how to respond.

A HELP message can be requested by typing a "?" or "??". The HELP message will appear under the prompt, then the prompt will be repeated. For example, perhaps you see the prompt

> Sort by TREATING SPECIALTY:

And you need assistance so you answer enter "?" and the HELP message would appear.

> Sort by TREATING SPECIALTY:

> CHOOSE FROM:

- SURGERY
- CARDIOLOGY
- 12 PSYCHIATRY

> Sort by TREATING SPECIALTY:

For some prompts, the system will list the possible answers from which you may choose. Any time choices appear with numbers, the system will usually accept the number or the name. A HELP message may not be available for every prompt. If you enter a "?" or "??" at a prompt that does not have a HELP message, the system will repeat the prompt.

## Definitions, Acronyms, and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Scheduling Acronyms are listed at REDACTED

  
<span id="_Toc54883339" class="anchor"></span>Table : Related Manuals

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 35%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>DOCUMENTATION NAME</th>
<th>FILE NAME</th>
<th>LOCATION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinical Reminders Installation and Setup Guide</td>
<td><p>PXRM_2_18_IG.PDF</p>
<p>PXRM_2_18_IG.doc</p></td>
<td><p>VDL</p>
<p>Clinical Reminders website</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="even">
<td>Scheduling Patch 578 Installation and Setup Guide</td>
<td><p>SD_5_3_578_IG.PDF</p>
<p>SD_5_3_578_IG.doc</p></td>
<td>Anonymous Directories</td>
</tr>
<tr class="odd">
<td>Registration Install Guide</td>
<td>DG_5_3_836_IG.PDF</td>
<td>Anonymous Directories</td>
</tr>
<tr class="even">
<td>High Risk Mental Health Patient Project Installation and Setup Guide</td>
<td>PXRM_2_24_IG.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>High Risk Mental Health Patient Project Release Notes</td>
<td>PXRM_2_24_RN.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>Clinical Reminders Manager's Manual</td>
<td>PXRM_2_MM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>Health Summary User Manual</td>
<td>HSUM_2_7_104_UM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>Health Summary Technical Manual</td>
<td>HSUM_2_7_104_TM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>Text Integration Utility User Manual</td>
<td>TIUUM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>CPRS User Guide: GUI Version</td>
<td>CPRSGUIUM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>CPRS Technical Manual: GUI Version</td>
<td>CPRSGUITM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>CPRS Technical Manual</td>
<td>CPRSLMTM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>PIMS Scheduling User - Manual Menus, Intro &amp; Orientation</td>
<td>PIMsSchIntro.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>PIMS Scheduling User Manual - Outputs Menu</td>
<td>PIMsSchOutput.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>PIMS Technical Manual</td>
<td>PIMSTM.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="even">
<td>Patient Record Flags User Guide</td>
<td>PatRecFlagUG.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
<tr class="odd">
<td>Scheduling and Registration Installation Review Guide</td>
<td>SDDG_Install_Review.PDF</td>
<td>Anonymous Directories VDL</td>
</tr>
</tbody>
</table>

<span id="_Toc352145680" class="anchor"></span>

Table : Documentation Website Locations

|                                  |                                                         |                                                                                            |
|----------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------|
| SITE                             | URL                                                     | DESCRIPTION                                                                                |
| National Clinical Reminders site | REDACTED                                                | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| VistA Document Library           | [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/) | Contains manuals for Scheduling and related applications.                                  |

## ## VistA Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA documentation is made available online in Microsoft® Word format and Adobe® Acrobat Portable Document Format (PDF). The PDF documents must be read using the Adobe® Acrobat Reader, which is freely distributed by Adobe® Systems Incorporated at the following Website: [<u>http://www.adobe.com/</u>](http://www.adobe.com/)

VistA documentation can also be downloaded from the Product Support (PS) anonymous directories:

Preferred Method REDACTED

> **NOTE:** This method transmits the files from the first available FTP server.

- Albany OIFO - REDACTED
- Hines OIFO - REDACTED
- Salt Lake City OIFO - REDACTED

## General Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For support, site questions, and problems with the VistA software, please enter a National Remedy ticket to Scheduling (SD) or call the REDACTED at REDACTED for assistance.

Also, review the VDL Internet link for all released end-user documentation found at [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scheduling module of the PIMS Package is designed to assist in the set-up of clinics, scheduling of patients for clinic appointments, and the collection of an assortment of related workload data for reporting purposes. The Scheduling Menus, Intro & Orientation functionality provides the End-Users with tools that produce a variety of reports and letters pertinent to Scheduling procedures.

Through Scheduling, necessary National Patient Care Database (NPCDB) workload is transparently collected and may be transmitted to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). Scheduling is fully integrated with the VA FileMan, thus allowing the extraction of ad hoc reports by non-programming personnel.

Important features of the Scheduling module include clinic set-up and enrollment/discharge of patients from clinics. Outputs that may be generated include workload analysis reports and letters of notification regarding cancellation of clinics/appointments.

## Use of the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of the Scheduling Menus, Intro & Orientation User Manual provides instructions for the End-Users to successfully use the software with little or no assistance. It also lists and describes the menus/options with examples to implement and use the software.

## SD\*5.3\*588 Patch - High Risk Mental Health Proactive Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SD\*5.3\*588 High Risk Mental Health Proactive Report patch assists the Mental Health professionals in the tracking of veterans with the High Risk for Suicide Patient Record Flag (PRF) who have appointments for the day. This patch consists of the following new enhancements:

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](pims-version-5-3-user-manual-menus-intro-orientation-etc/006.png) | NOTE: These reports are not part of the Scheduling Menus, Introduction & Orientation Module, they are Stand-Alone Menu Options. |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|

## High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Ad Hoc proactive report will produce a list of patients with the high risk for suicide patient record flag that have scheduled appointments for a date range. It allows the user to enter dates into the future. The user will be asked to list only mental health appointments that are in the Reminder Location File or list all clinics both mental health and non- mental health. This report gives the user a bit more flexibility.

OIT staff will need to attach the High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] option to an appropriate menu for the Suicide Prevention Coordinator, or to a menu at the local suicide prevention staff's discretion.

The High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] option uses the Reminder Location File to check for Mental Health clinics.

Example: The new High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] option is displaying the High Risk MH Proactive Adhoc Report.

Select OPTION NAME: SD MH PROACTIVE AD HOC REPORT High Risk MH Proactive Adhoc Report

High Risk MH Proactive Adhoc Report

\*\*\*\*\*\*\*\*\*\*\*\*\*\* High Risk Mental Health Proactive Adhoc Report \*\*\*\*\*\*\*\*\*\*\*\*\*\*

Select Beginning Date: 04/04/13// T

Select Ending Date: 04/04/13// T+10

Select division: ALL//

Sort the report by:

A All clinics

M Mental Health clinics only

Sort by: (A)ll clinics A//

Select Clinic: ALL//

This output requires 80 column output

Select Device: UCX/TELNET Right Margin: 80// ^

DEVISC1A1:MNTVLL 3d1\>Q

DEVISC1A1:MNTVLL\>D ^XQ1

Select OPTION NAME: XU USER START-UP User start-up event

User start-up event

DEVISC1A1:MNTVLL\>Q

DEVISC1A1:MNTVLL\>D ^XQ1

Select OPTION NAME: SD MH PROACTIVE

1 SD MH PROACTIVE AD HOC REPORT High Risk MH Proactive Adhoc Report

2 SD MH PROACTIVE BGJ REPORT High Risk MH Proactive Nightly Report

CHOOSE 1-2: 1 SD MH PROACTIVE AD HOC REPORT High Risk MH Proactive Adhoc Report

High Risk MH Proactive Adhoc Report

\*\*\*\*\*\*\*\*\*\*\*\*\*\* High Risk Mental Health Proactive Adhoc Report \*\*\*\*\*\*\*\*\*\*\*\*\*\*

Select Beginning Date: 04/04/13// T

Select Ending Date: 04/04/13// T+10

Select division: ALL//

Sort the report by:

A All clinics

M Mental Health clinics only

Sort by: (A)ll clinics A//

Select Clinic: ALL//

This output requires 80 column output

Select Device: ;;99999 UCX/TELNET Right Margin: 80//

...SORRY, HOLD ON...

HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 1

CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: ANYCITY

1 TESTPATIENT,ONEXXXXX T1111 4/4/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/5/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/8/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/10/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/11/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

4/12/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX

HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 2

CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: ON THE HUDSON IN HISTORIC ANYWHERE

1 TESTPATIENT,TWOXXXX T0000 4/4/2013@08:00 SAMPLE CLINICXX

4/5/2013@08:00 SAMPLE CLINICXX

4/7/2013@08:00 SAMPLE CLINICXX

4/8/2013@08:00 SAMPLE CLINICXX

4/9/2013@08:00 SAMPLE CLINICXX

4/10/2013@08:00 SAMPLE CLINICXX

4/11/2013@08:00 SAMPLE CLINICXX

4/12/2013@08:00 SAMPLE CLINICXX

4/14/2013@08:00 SAMPLE CLINICXX

HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 3

CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: ANYWHERE1

1 TESTPATIENT,ONEXXXX T1111 4/4/2013@09:00 MENTAL HEALTH

4/5/2013@09:00 MENTAL HEALTH

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@09:00 MENTAL HEALTH

4/10/2013@09:00 MENTAL HEALTH

4/11/2013@09:00 MENTAL HEALTH

4/12/2013@09:00 MENTAL HEALTH

HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 4

CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58

Totals Page

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Division/Clinic Appointment Totals

Division/CLinic Unique

Patients

ANYCITY 1

ON THE HUDSON IN HISTORIC ANYWHERE 1

ANYWHERE1 1

<span id="_Toc54883348" class="anchor"></span>Figure 1: The new High Risk MH Proactive Adhoc Report

## High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new option should be used if you need to re-create the same report that is created by the scheduled SDAM BACKGROUND JOB after midnight each night. The option lists the scheduled appointments for Mental Health Clinics for today.

This report should not be scheduled to run nightly as it is kicked off by the Scheduling nightly background Job (SDAM BACKGROUND JOB) that should already be scheduled to run nightly on your system. This report is sent in a mail message to the members of the SD MH NO SHOW NOTIFICATION mail group.

Future appointments will be listed on this report. The number of days of future appointments that is listed is defaulted to 30 days in the future. Parameter SD MH PROACTIVE DAYS has been added to store the number of days to list future appointments. This parameter can be edited, within the range of 1 to 30, by the user by using the Edit Parameter Values \[XPAR EDIT PARAMETER\] option, changing the System value.

This proactive background job report will produce a list of patients with the high risk for suicide patient record flag and have scheduled appointments for today. This background job will produce a list of appointments (mental health clinics only) for those patients for the next day so that the Suicide Prevention Coordinators (SPC) can follow up and remind patients of their appointments for that day. The SPCs in the SD MH NO SHOW NOTIFICATION mail group will receive a mail message. All SPCs that need to receive this report should be a member of that mail group. The new option will kick off automatically every night with the running of the Scheduling Nightly Background Job.

OIT staff will need to attach the High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] option to an appropriate menu for the Suicide Prevention Coordinator, or to a menu at the local suicide prevention staff's discretion.

The High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] option uses the Reminder Location File to check for Mental Health clinics.

Example: The new High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] option is displaying the High Risk MH Proactive Nightly Report.

Select OPTION NAME: SD MH PROACTIVE BGJ REPORT High Risk MH Proactive

Nightly Report

High Risk MH Proactive Nightly Report

...SORRY, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

This report option generates a mail message containing the

High Risk Mental Health Proactive Nightly Report which is sent only

to individuals in the SD MH NO SHOW NOTIFICATION mailgroup.

DEVISC1A1:MNTVLL\>D ^XM

All Baskets, New Priority messages: 43

\*=New/!=Priority.............Subject................Lines.From.......Read/Rcvd

!1572. IN \[126400\] 01/27/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1573. IN \[126401\] 01/27/12 Pre-report National Flag 10 HRMH PRF GENERATE JOB

!1574. IN \[126403\] 01/27/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1575. IN \[126404\] 01/27/12 Pre-report National Flag 10 HRMH PRF GENERATE JOB

!1576. IN \[126509\] 02/01/12 Pre-report National Flag 49 HRMH PRF GENERATE JOB

!1577. IN \[126510\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1578. IN \[126511\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1579. IN \[126512\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1580. IN \[126513\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1581. IN \[126514\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1582. IN \[126515\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1583. IN \[126516\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1584. IN \[126517\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1585. IN \[126518\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1586. IN \[126519\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1587. IN \[126520\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1588. IN \[126521\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1589. IN \[126522\] 02/01/12 Pre-report National Flag 12 HRMH PRF GENERATE JOB

!1590. IN \[126523\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1591. IN \[126524\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

VA MailMan 8.0 service for FIEUDMNDS.DDUD_CUEJ@MNTVLL.REDACTED

You last used MailMan: 03/18/13@11:46

You have 861 new messages.

Select MailMan Option: READ/MANAGE MESSAGES

Select message reader: Classic//

Read mail in basket: IN// (2343 messages, 861 new)

Last message number: 2343 Messages in basket: 2343 (861 new)

Enter ??? for help.

IN Basket Message: 1// 2344

Enter message action (in IN basket): Ignore// Print

Print recipient list? No// NO

DEVICE: HOME// ;;99999 UCX/TELNET

MailMan message for FJRURURU,RMRMRH OI&T STAFF

Printed at MNTVLL.REDACTED 04/04/13@16:02

Subj: HRMH PROACTIVE NIGHTLY REPORT MESSAGE \# \[#136309\] 04/04/13@16:01

37 lines

From: POSTMASTER In 'IN' basket. Page 1

-----------------------------------------------------------------------------

Division Totals

Division Unique

Patients

ANYCITY 1

ON THE HUDSON IN HISTORI 1

ANYWHERE1 1

HIGH RISK MENTAL HEALTH PROACTIVE NIGHTLY REPORT PAGE 1

By Patient for Appointments on 4/4/13 Run: 4/4/2013@16:01

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: ANYCITY

1 TESTPATIENT,ONEXXXXX T0000 4/4/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXX

4/5/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXX

HIGH RISK MENTAL HEALTH PROACTIVE NIGHTLY REPORT PAGE 2

By Patient for Appointments on 4/4/13 Run: 4/4/2013@16:01

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: ON THE HUDSON IN HISTORI

1 TESTPATIENT,TWOXXXXX T1111 4/4/2013@08:00 SAMPLE CLINICXXX

4/5/2013@08:00 SAMPLE CLINICXXX

HIGH RISK MENTAL HEALTH PROACTIVE NIGHTLY REPORT PAGE 3

By Patient for Appointments on 4/4/13 Run: 4/4/2013@16:01

\# PATIENT PT ID APPT D/T CLINIC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION: ANYWHERE1

1 TESTPATIENT,ONEXXXXX T0000 4/4/2013@09:00 MENTAL HEALTH

4/5/2013@09:00 MENTAL HEALTH

<span id="_Toc54883349" class="anchor"></span>Figure 2: High Risk MH Proactive Nightly Report

## Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will list the patients who have the patient record flag High Risk for suicide and No Show an appointment in a mental health or non mental health clinic. The report will list the patient, emergency contacts, next of kin, future scheduled appointments, provider, and results. Mental Health clinics are face-to-face. Mental Health appointments are defined in the "VA-MH NO SHOW APPT CLINICS LL" Reminder Location List. The High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] option is modified to include the following changes:

- The provider name is now displayed directly under the No Show appointment information, to keep everything connected.
- Key for appointment status abbreviations (NS, NA, NAT) added to the heading and will now print on every page break.
- Appointment line now displays information in two lines:
- line one: count, patient name, Patient ID 1st initial last name+last 4 ssn, appointment D/T, 30 character clinic name
- line two: appointment status abbreviation, appointment provider name.
- Patient ID is now 5 characters: First initial of last name + last 4 of SSN.
- 30-character Clinic name in both future and appointment data information.
- AM and PM removed from the date/time of appt.
- The report now displays the name of the Mental Health Treatment Coordinator (MHTC) and the name of the care team they are assigned to in parentheses.
- The results of the no show patient contact are also included.
- Results added for resolution: Reminder term and health factor Information.

This is the High Risk Mental Health AD Hoc No show Report entry point that the user can run to display the report. This report will display all patients that did not show up for their scheduled appointment for a Mental Health clinic. It will list patient contact information, Next of Kin, emergency contact, clinic default provider, future scheduled appointments and results of attempts to contact the no showed patients. The user is asked for various sort criteria, a date range, divisions to display (one, many, all), and sort by Clinic, Reminder Location or Stop Codes (one, many, all).

Example: Modified High Risk MH No-Show Adhoc Report.

0 0 3 1

Select OPTION NAME: SD MH NO

1 SD MH NO SHOW AD HOC REPORT High Risk MH No-Show Adhoc Report

2 SD MH NO SHOW NIGHTLY BGJ High Risk MH No-Show Nightly Report

CHOOSE 1-2: 1 SD MH NO SHOW AD HOC REPORT High Risk MH No-Show Adhoc Report

High Risk MH No-Show Adhoc Report

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* High Risk Mental Health NO SHOW Adhoc Report \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Select Beginning Date: 04/08/13// T-6 (APR 02, 2013)

Select Ending Date: 04/08/13// T (APR 08, 2013)

Select division: ALL//

Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M//

Select Number of days to List Future Appointments: 30//1

This output requires 80 column output

Select Device: ;;99999 UCX/TELNET Right Margin: 80//

...HMMM, LET ME THINK ABOUT THAT A MOMENT...

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 1

MH CLINICS for Appointments 4/2/13-4/8/13 Run: 4/8/2013@11:02

\*STATUS: NS = No Show NA = No Show Auto Rebook NAT = No Action Taken

\# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* DIVISION/CLINIC/STOP: ANYCITY/D-PSYCHXXXXXXXXXXXXXXXXXXX/188

1 TESTPATIENT,ONEXXXX T0000 4/4/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXX

\*NS PHYSICIAN,THREE

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (SAMPLENAME TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

2 TESTPATIENT,ONEXXXX T0000 4/5/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

\*NS PHYSICIAN,THREE

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (SAMPLENAME TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

3 TESTPATIENT,ONEXXXX T0000 4/8/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXX

\*NSA PHYSICIAN,THREE

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (SAMPLENAME TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 2

MH CLINICS for Appointments 4/2/13-4/8/13 Run: 4/8/2013@11:02

\*STATUS: NS = No Show NA = No Show Auto Rebook NAT = No Action Taken

\# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION/CLINIC/STOP: ON THE HUDSON IN HISTORI/SAMPLE CLINIC/202

1 TESTPATIENT,TWO T1111 4/4/2013@08:00 SAMPLE CLINICXXX

\*NS PHYSICIAN,ONEXXXXXXXXXXXXX

Next of Kin:

NOK: CONTACT,PERSON

Emergency Contact:

E-Cont.: CONTACT,PERSON

MHTC: PHYSICIAN,MHTC (SAMPLENAME TEAM)

Future Scheduled Appointments:

4/8/2013@08:00 SAMPLE CLINICXXXX

4/9/2013@08:00 SAMPLE CLINICXXXX

Results:

2 TESTPATIENT,TWO E4646 4/5/2013@08:00 SAMPLE CLINICXXXX

\*NSA PHYSICIAN,ONEXXXXXXXXXXXXX

Next of Kin:

NOK: CONTACT,PERSON

Emergency Contact:

E-Cont.: CONTACT,PERSON

MHTC: PHYSICIAN,MHTC (SAMPLENAME TEAM)

Future Scheduled Appointments:

4/8/2013@08:00 SAMPLE CLINICXXXX

4/9/2013@08:00 SAMPLE CLINICXXXX

Results:

3 TESTPATIENT,TWO T1111 4/7/2013@08:00 SAMPLE CLINICXXXX

\*NS PHYSICIAN,ONEXXXXXXXXXXXXX

Next of Kin:

NOK: CONTACT,PERSON

Emergency Contact:

E-Cont.: CONTACT,PERSON

MHTC: PHYSICIAN,THREE (SAMPLENAME TEAM)

Future Scheduled Appointments:

4/8/2013@08:00 SAMPLE CLINICXXXX

4/9/2013@08:00 SAMPLE CLINICXXXX

Results:

4 TESTPATIENT,TWO T1111 4/8/2013@08:00 SAMPLE CLINICXXXX

\*NAT PHYSICIAN,ONEXXXXXXXXXXXXX

Next of Kin:

NOK: CONTACT,PERSON

Emergency Contact:

E-Cont.: CONTACT,PERSON

MHTC: PHYSICIAN,MHTC (SAMPLENAME TEAM)

Future Scheduled Appointments:

4/8/2013@08:00 SAMPLE CLINICXXXX

4/9/2013@08:00 SAMPLE CLINICXXXX

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 3

MH CLINICS for Appointments 4/2/13-4/8/13 Run: 4/8/2013@11:02

\*STATUS: NS = No Show NA = No Show Auto Rebook NAT = No Action Taken

\# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION/CLINIC/STOP: ANYWHERE1/MENTAL HEALTH/188

1 TESTPATIENT,ONEXXXX T0000 4/4/2013@09:00 MENTAL HEALTH

\*NAT PHYSICIAN,TWO

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (SAMPLENAME TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

2 TESTPATIENT,ONEXXXX T0000 4/5/2013@09:00 MENTAL HEALTH

\*NAT PHYSICIAN,TWO

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (SAMPLENAME TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

3 TESTPATIENT,ONEXXXX T0000 4/8/2013@09:00 MENTAL HEALTH

\*NAT PHYSICIAN,TWO

Work: (000)900-7000

Emergency Contact:

E-Cont.: CONTACT,TWO

MHTC: PHYSICIAN,MHTC (SAMPLENAME TEAM)

Future Scheduled Appointments:

4/8/2013@09:00 MENTAL HEALTH

4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXXXX

4/9/2013@09:00 MENTAL HEALTH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 4

MH CLINICS for Appointments 4/2/13-4/8/13 Run: 4/8/2013@11:02

Totals Page

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Division/Clinic Appointment Totals

Division/Clinic Unique

NS NSA NAT Patients

ANYCITY/D-PSYCHXXXXXXXXXXXXXXXXXXX 2 1 0 1

ON THE HUDSON IN HISTORI/SAMPLE CLINIC 2 1 1 1

ANYWHERE1/MENTAL HEALTH 0 0 3 1

<span id="_Toc54883350" class="anchor"></span>Figure 3: Modified High Risk MH No-Show Adhoc Report

## High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option should be used if you need to re-create the same report that is created by the scheduled SDAM BACKGROUND JOB after midnight each night. The option lists the “NO-SHOW”, “NO-SHOW AUTO REBOOK”, or “No Action Taken” appointments for Mental Health Clinics for the previous day.

This report should not be scheduled to run nightly as it is kicked off by the Scheduling nightly background Job (SDAM BACKGROUND JOB) that should already be scheduled to run nightly on your system.

This report is sent in a mail message to the members of the SD MH NO SHOW NOTIFICATION mail group.

Future appointments will list on this report. The number of days’ worth of future appointments that will list is defaulted to 30 days in the future. A new parameter SD MH NO SHOW DAYS has been added to store the number of days to list future appointments for. This parameter can be edited, within the range of 1 to 30, by the user by using the option \[XPAR EDIT PARAMETER\] Edit Parameter Values changing the System value. The High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] option was modified to include the following changes:

- The provider name is now displayed directly under the No Show appointment information, to keep everything connected.
- Key for appointment status abbreviations (NS, NA, NAT) added to the heading and will now print on every page break.
- Appointment line now displays information in two lines:
- line one: count, patient name, Patient ID 1st initial last name+last 4 ssn, appointment D/T, 30 character clinic name
- line two: appointment status abbreviation, appointment provider name.
- Patient ID is now 5 characters: First initial of last name + last 4 of SSN.
- 30-character Clinic name in both future and appointment data information.
- AM and PM removed from the date/time of appt.

The High Risk Mental Health No show Report entry point is called by the scheduling background job. This report will display all patients that did not show up for their scheduled appointment for a Mental Health clinic.  It will list clinic default provider and future scheduled appointments. The user will not be asked any sort criteria. The report will be sent via email to those persons that are in the SD MH NO SHOW NOTIFICATION mail group.

Example: High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] option is displaying a High Risk MH No-Show Nightly Report.

Select OPTION NAME: SD MH

1 SD MH NO SHOW AD HOC REPORT High Risk MH No-Show Adhoc Report

2 SD MH NO SHOW NIGHTLY BGJ High Risk MH No-Show Nightly Report

3 SD MH PROACTIVE AD HOC REPORT High Risk MH Proactive Adhoc Report

4 SD MH PROACTIVE BGJ REPORT High Risk MH Proactive Nightly Report

CHOOSE 1-4: 2 SD MH NO SHOW NIGHTLY BGJ High Risk MH No-Show Nightly Report

High Risk MH No-Show Nightly Report

...EXCUSE ME, HOLD ON...

This report option generates a mail message containing the

High Risk Mental Health No Show Nightly Report which is sent

only to individuals in the SD MH NO SHOW NOTIFICATION mailgroup.

DEVISC1A1:MNTVLL 7f3\>D ^XM

All Baskets, New Priority messages: 43

\*=New/!=Priority.............Subject...............Lines.From........Read/Rcvd

!1572. IN \[126400\] 01/27/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1573. IN \[126401\] 01/27/12 Pre-report National Flag 10 HRMH PRF GENERATE JOB

!1574. IN \[126403\] 01/27/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1575. IN \[126404\] 01/27/12 Pre-report National Flag 10 HRMH PRF GENERATE JOB

!1576. IN \[126509\] 02/01/12 Pre-report National Flag 49 HRMH PRF GENERATE JOB

!1577. IN \[126510\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1578. IN \[126511\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1579. IN \[126512\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1580. IN \[126513\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1581. IN \[126514\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1582. IN \[126515\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1583. IN \[126516\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1584. IN \[126517\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1585. IN \[126518\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1586. IN \[126519\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1587. IN \[126520\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

!1588. IN \[126521\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1589. IN \[126522\] 02/01/12 Pre-report National Flag 12 HRMH PRF GENERATE JOB

!1590. IN \[126523\] 02/01/12 Pre-report National Flag 47 HRMH PRF GENERATE JOB

!1591. IN \[126524\] 02/01/12 Pre-report National Flag 13 HRMH PRF GENERATE JOB

VA MailMan 8.0 service for FXXXXXX.XERY_NEYD@MNTVLL.REDACTED

You last used MailMan: 04/04/13@16:01

You have 861 new messages.

Select MailMan Option: READ/MANAGE MESSAGES

Select message reader: Classic//

Read mail in basket: IN// (2345 messages, 861 new)

Last message number: 2345 Messages in basket: 2345 (861 new)

Enter ??? for help.

IN Basket Message: 1// 2345

Subj: HRMH NO SHOW NIGHTLY REPORT MESSAGE \# \[#136421\] 04/08/13@11:00 18 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

Division/Clinic Appointment Totals

Division/CLinic Unique

NS NSA NAT Patients

ON THE HUDSON IN HISTORI/SAMPLE CLINIC 1 0 0 1

Printed at MNTVLL.REDACTED 04/08/13@11:00

Subj: HRMH NO SHOW NIGHTLY REPORT MESSAGE \# \[#136421\] 04/08/13@11:00 18 lines

From: POSTMASTER In 'IN' basket. Page 1

-----------------------------------------------------------------------------

Division/Clinic Appointment Totals

Division/Clinic

Unique

NS NSA NAT Patients ON THE HUDSON IN HISTORI/SAMPLE CLINIC 1 0 0 1

HIGH RISK MENTAL HEALTH NO SHOW NIGHTLY REPORT PAGE 1

By CLINIC for Appointments on 4/7/13 Run: 4/8/2013@10:59

\*STATUS: NS = No Show NSA = No Show Auto Rebook NAT = No Action Taken

\# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DIVISION/CLINIC/STOP: ON THE HUDSON IN HISTORI/SAMPLE CLINIC/202

1 TESTPATIENT,TWO T0000 4/7/2013@08:00 SAMPLE CLINICXX

\*NS PHYSICIAN,ONE

Future Scheduled Appointments:

4/8/2013@08:00 SAMPLE CLINICXXXX

4/9/2013@08:00 SAMPLE CLINICXXXX

4/10/2013@08:00 SAMPLE CLINICXXXX

Enter message action (in IN basket): Ignore//

End reached. Begin again? No// NO

<span id="_Toc54883351" class="anchor"></span>Figure 4: High Risk MH No-Show Nightly Report

## SD\*5.3\*578 Patch – High Risk Mental Health No Show Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SD\*5.3\*578 High Risk Mental Health No Show Report patch provides two new MH NO SHOW Scheduling Reports, High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\]  and High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\], for use by Suicide Prevention Coordinators and other Mental Health professionals. The reports will support following up with High Risk for Suicide patients who missed a scheduled MH appointment.

## New Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] option 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] option will display all patients that no showed for their scheduled appointment for a Mental Health clinic. The user is asked for the date range and divisions to display and the report is sorted by Clinic, Mental Health only clinics or Stop Codes. The report will display patient contact information, Next of Kin, emergency contact, clinic default provider, Mental Health Team Coordinator (MHTC) (future release), future scheduled appointments and results of attempts to contact the no showed patients (future release).

## High Risk MH No-Show Nightly Report \[SD MH NO SHOW Nightly BGJ\] option 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] is called by the scheduling nightly background job Appointment Status Update \[SDAM BACKGROUND JOB\]. This report will display all patients that no showed for their scheduled appointment for a Mental Health clinic. This will be an abbreviated report, listing only Patient appointment information and future scheduled appointments for the patient. As this is a background job, the report will display for the day before, for all the divisions and mental health clinics in the facility. The report will be sent via email to members of the SD MH NO SHOW NOTIFICATION mail group. This report can also be run by calling the option High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\]. Access to these two new options should be assigned to the appropriate personnel.

## Scheduling Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scheduling Menus, Intro & Orientation options provides the User with tools that produce a variety of reports and letters pertinent to Scheduling procedures. The following sections offer features and description of the options available in the Menus, Intro, and Orientation Menu. Appointment Menu Options are:

- Ambulatory Care Reporting (ACR) Menu (…)
- Appointment Menu (…)
- Automated Service Connected Designation Menu
- Outputs Menu (…)
- Supervisor Menu (…)

| ![](pims-version-5-3-user-manual-menus-intro-orientation-etc/007.png) | NOTE: The Scheduling Reports appear in the primary and secondary menu options. |
|---------------------------------------------------|------------------------------------------------------------------------------------|

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr class="header">
<th>![](pims-version-5-3-user-manual-menus-intro-orientation-etc/008.png)</th>
<th><p><strong>NOTE</strong>: MAS is an acronym for Medical Administration Service.</p>
<p>This service, where it still exists, is now generally referred to as Health Administration Service. Several file names, option names, and reports in the PIMS software contain the initials MAS. These will be retained to avoid confusion and ensure continuity.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Ambulatory Care Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: ACRP Reports Menu

ACRP Reports Menu

ACRP Ad Hoc Report Menu …

ACRP Ad Hoc Report

Delete an Ad Hoc Report Template

Display Ad Hoc Report Template Parameters

Print from Ad Hoc Template

Clinic Appointment Availability Report

Clinic Group Maintenance for Reports

Clinic Utilization Statistical Summary

Data Validation Menu …

Enc. by IP DSS ID/DSS ID by Freq. (IP0, IP1, IP2)

Means Test IP Visits & Unique (IP3, IP4, IP5)

Most Frequent 50 IP CPT Codes (IP6)

Most Frequent 50 IP ICD-9-CM Codes (IP7)

Most Frequent 20 IP Practitioner Types (IP8)

Visits and Unique IP SSNs by County (IP9)

Enc. by DSS ID/DSS ID by Freq. (OP0, OP1, OP2)

Means Test Visits & Uniques (OP3, OP4, OP5)

Most Frequent 50 CPT Codes (OP6)

Most Frequent 50 ICD-9-CM Codes (OP7)

Most Frequent 20 Practitioner Types (OP8)

Visits and Unique SSNs by County (OP9)

Encounter Activity Report

Encounter ‘Action Required’ Report

Means Test/Eligibility/Enrollment Report

Outpatient Diagnosis/Procedure Frequency Report

Outpatient Diagnosis/Procedure Code Search

Outpatient Encounter Workload Statistics

Patient Activity by Appointment Frequency

Patient Appointment Statistics

Patient Encounter List

Performance Monitor Menu

Performance Monitor Summary Report

Performance Monitor Detailed Report

Performance Monitor Retransmit Report (AAC)<span id="p20" class="anchor"></span>Note: This option has been placed out of order with patch SD\*5.3\*640 since ACRP and APM transmissions have been discontinued.

Review of Scheduling/PCE/Problem List Data

Retroactive Visits List

SC Veterans Awaiting Appointments

Trend of Facility Unique by 12 Month Date Ranges

Veterans Without Activity Since a Specified Date

Error Listing

Transmission Reports

Transmission History Report - Full

Transmission History for Patient

Supervisor Ambulatory Care Menu

Edit Appointment Type for Add/Edit Encounters

Check Transmitted Outpatient Encounter Files

Purge Ambulatory Care Reporting files

Scheduling/PCE Bad Pointer Count

Edit Outpatient Encounter

Purge rejections that are past database close-out

Data Transmission Report

Incomplete Encounter Management

Incomplete Encounter Reports

Alpha List of Incomplete Encounters

Encounters Transmitted with MT Status of U

Incomplete Encounter Error Report

Incomplete Encounters by Error Code

Summary Report - IEMM

Correct Incomplete Encounters

Retransmit Ambulatory Care Data by Date Range Note: This option has been placed out of order with patch SD\*5.3\*640 since ACRP transmission has been discontinued.

Retransmit Selected Error Code Note: This option has been placed out of order with patch SD\*5.3\*640 since ACRP transmission has been discontinued.

Selective Retransmission of NPCDB Rejections Note: This option has been placed out of order with patch SD\*5.3\*640 since ACRP transmission has been discontinued.

## Appointment Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These options allow the end-user to perform the functions of a Scheduling Clerk:

Example: Appointment Options

AM Appointment Management

CK Appointment Check-in/Check-out

Add/Edit Stop Codes

Append Ancillary Test to Appt.

Cancel Appointment

Chart Request

Check-in/Unscheduled Visit

Computer Generated Menu…

Computer Generated Appointment Type Listing

Edit Computer Generated Appointment Type

Batch Update Comp Gen Appt Type for C&Ps

Stop Code Listing (Computer Generated)

Delete Ancillary Test for Appt.

Discharge from Clinic

Display Appointments

Edit Clinic Enrollment Data

Enrollment Review Date Entry

Find Next Available Appointment

Make Appointment

Multiple Appointment Booking

Multiple Clinic Display/Book

New Enrollee Appointment Request Management Menu

Management Edit

Call List

Tracking Report

Multiple Clinic Display/Book

No-Shows

Team/Position Assignment/Re-Assignment

## Automated Service Connected Designation Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this module may be found in the VistA Documentation Library under Automated Service Connected Designation at the following address: <http://www.va.gov/vdl/application.asp?appid=174>

The Automated Service Connected Designation Menu option contains all menus and options needed to collect, edit, maintain and transmit Ambulatory Care information to the National Patient Care Database.

ASCD Reports are as follows:

- Compile ASCD Encounters by Date Range
- Edit ASCD Encounters by Date Range
- Edit ASCD Encounters by ListMan
- Edit Single ASCD Encounter

## Outputs Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc54883341" class="anchor"></span>Table : Scheduling Outputs Menu

| OPTION                                        | DESCRIPTION                                                                                                                                                                                                                                                                |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APPOINTMENT LIST                              | This option is used to generate appointment lists for one/many/all clinics for a specified date.                                                                                                                                                                           |
| APPOINTMENT MANAGEMENT REPORT                 | This option is used to print appointment lists that will help the site implement and manage the new appointment check in requirement.                                                                                                                                      |
| CANCELLED CLINIC REPORT                       | This option is used to generate a report to determine the number of cancelled clinic appointments for National Reporting purposes.                                                                                                                                         |
| CLINIC ASSIGNMENT LISTING                     | This option is used to monitor the size and composition of clinics. Over time, the listings can reflect clinic growth, shrinkage, etc.                                                                                                                                     |
| CLINIC LIST (DAY OF WEEK)                     | This option is used to generate a listing of all active clinics showing which days they meet and, if applicable, the days they will meet in the future.                                                                                                                    |
| CLINIC NEXT AVAILABLE APPT. MONITORING REPORT | This option provides an appointment monitoring tool which reflects the data collected for the access performance measure.                                                                                                                                                  |
| CLINIC PROFILE                                | This option is used to produce a profile of one/many/all clinics.                                                                                                                                                                                                          |
| DISPLAY CLINIC AVAILABILITY REPORT            | This option is used to provide a display of the clinic patterns for the clinics and date range selected. For each selected clinic, the option will print its clinic appointment pattern as well as a listing by appointment date/time of those patients who are scheduled. |
| ENROLLMENTS \> X DAYS                         | This option is used to produce a report showing all enrollments for a selected clinic which exceed a select number of days.                                                                                                                                                |
| FILE ROOM LIST                                | This option is used to generate a list of appointments for a specified day.                                                                                                                                                                                                |
| FUTURE APPOINTMENTS FOR INPATIENTS            | This option is used to produce a report that lists all patients admitted on a particular date that have pending appointments at the facility.                                                                                                                              |
| INPATIENT APPOINTMENT LIST                    | This option is used to produce a list of inpatients that have appointments scheduled for the facility's clinics.                                                                                                                                                           |
| MANAGEMENT REPORT FOR AMBULATORY PROCEDURES   | This option is used to print a statistical report of ambulatory procedures captured through the CPT coding of outpatient visits for a specified date range.                                                                                                                |
| NO-SHOW REPORT                                | This option is used to generate a report of all no-shows entered into the system for specified clinics.                                                                                                                                                                    |
| PATIENT PROFILE MAS                           | This option is used to generate a profile for a selected patient including demographic, clinic, eligibility and Means Test information.                                                                                                                                    |
| PRINT SCHEDULING LETTERS                      | This option is used to print any one of the following types of scheduling letters for a selected date range: Appointment Cancelled, Clinic Cancelled, No-Show or Pre-Appointment.                                                                                          |
| PROVIDER/DIAGNOSIS REPORT                     | This option is used to print a report of outpatient encounters for a selected date range sorting by Division and Outpatient Encounter Date. You also may choose two of the following additional sorts: Provider, Diagnosis, Patient, Clinic, or Stop Code.                 |
| RADIOLOGY PULL LIST                           | This option is used to generate a listing of all patients whose radiology reports/films are required for their scheduled appointments.                                                                                                                                     |
| ROUTING SLIPS                                 | This option is used to produce routing slips for one individual patient, all patients, or add-ons (patients scheduled for appointments since routing slips were last printed).                                                                                             |
| VISIT RPT BY TRANSMITTED OPT ENCOUNTER        | This option is used to generate a report providing encounter and visit information for a specified date range.                                                                                                                                                             |
| WORKLOAD REPORT                               | This option is used to generate a variety of reports showing clinic workload. These help in determining the kinds of activity within clinics during a specified date range.                                                                                                |

## ## Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the primary menu option that allows the user access to all supervisor functions of the scheduling module.

Detailed instructions for this menu option are in the Supervisor Menu User Guide. At time of publishing the file name is “User Manual – Supervisor Menu.” The list of current PIMS and other scheduling manuals can be found on the VistA Documentation Library (VDL)’s scheduling page: <https://www.va.gov/vdl/application.asp?appid=100>

Overview

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Add/Edit a Holiday</p>
<p>Appointment Inquiry</p>
<p>Appointment Status Update Menu ...</p>
<p>Appointment Status Update</p>
<p>Print Appointment Status Update (Date Range)</p>
<p>Purge Appointment Status Update Log File</p>
<p>View Appointment Status Update Date (Single Date)</p>
<p>Appointment Waiting Time Report</p>
<p>Appointments with missing resources</p>
<p>Appointments with no resource report</p>
<p>Automatically Fix Appointments with No Resource</p>
<p>Cancel Clinic Availability</p>
<p>Change Patterns to 30-60</p>
<p>Clinics without matching resource list</p>
<p>Clinic Edit Log Report</p>
<p>Convert Patient File Fields to PCMM</p>
<p>Create a resource</p>
<p>Create/Edit Local Cancellation Comments</p>
<p>Current MAS Release Notes</p>
<p>Edit Clinic Stop Code Name- Local Entries Only</p>
<p>Edit Resource</p>
<p>Edit resource for an appointment</p>
<p>Encounter Inquiry</p>
<p>Enter/Edit Letters</p>
<p>Inactivate a clinic</p>
<p>List Appointments and Encounters by status</p>
<p>Look up on Clerk Who Made Appointment</p>
<p>Manually Fix Appointments with No Resource</p>
<p>Non-Conforming Clinics Stop Code Report</p>
<p>Pending RTC Cleanup – by Date</p>
<p>Pending RTC Cleanup - FULL</p>
<p>Print Clinic Installation Checklist</p>
<p>Purge Scheduling Data</p>
<p>Reactivate a Clinic</p>
<p>Release Appointment Request Locks</p>
<p>Remap Clinic</p>
<p>Resource Inquiry</p>
<p>Restore Clinic Availability</p>
<p>Scheduling Parameters</p>
<p>Set up a Clinic</p>
<p>Sharing Agreement Category Update</p>
<p>VS GUI Help Pane Edit</p>
<p>Wait List (Sch/PCMM) Utilities ...</p>
<p>Inter-Facility Transfer Request</p>
<p>Inter-Facility Transfer Accept</p>
<p>Wait List Batch Clinic Change</p>
<p>Wait List Enter/Edit as a Scheduling Reminder</p>
<p>Open Closed EWL Entry</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
</tbody>
</table>

## HRMHP No Show and Proactive Options & Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Scheduling Reports are available when the High Risk Mental Health Patient – Reminder & Flag (HRMHP) project is installed at your site.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th>![](pims-version-5-3-user-manual-menus-intro-orientation-etc/009.png)</th>
<th><p>NOTE: The MH NO SHOW and the MH PROACTIVE reports are not part of the Scheduling menus.</p>
<p>OIT staff will need to assign these report options to the primary or secondary menu options of the Suicide Prevention Coordinator, Mental Health Treatment Coordinator, and other Mental Health Professionals.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc54883342" class="anchor"></span>Table : Mental Health No Show Options & Features

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>MH NO SHOW OPTIONS &amp; FEATURES</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>High Risk MH No-Show Adhoc Report [SD MH NO SHOW AD HOC REPORT]</td>
<td><p>This Scheduling option provides a High Risk MH No-Show Adhoc Report for use by Suicide Prevention Coordinators and other Mental Health professionals.</p>
<p>This report supports following up with High Risk for Suicide patients who missed a scheduled MH appointment. It displays all patients that no-showed for their scheduled appointment.</p></td>
</tr>
<tr class="even">
<td>High Risk MH No-Show Nightly Report [SD MH NO SHOW NIGHTLY BGJ]</td>
<td><p>This Scheduling option provides a High Risk MH No-Show Nightly Report. This report supports actions relating to following up with High Risk for Suicide patients that missed their MH appointment.</p>
<p>This report is generated at the end of the Scheduling Nightly Background Job (SDAM BACKGROUND JOB), and will be sent in a Mailman message to members of the SD MH NO SHOW NOTIFICATION mail group.</p>
<p>This report may also be run by calling the option High Risk MH No-Show Nightly Report.</p>
<p>Future appointments will list on this report. The number of days (quantity of future appointments) that will list is defaulted to 30 days in the future. A new parameter SD MH NO SHOW DAYS has been added to store the number of days to list future appointments for each patient on the report. This parameter can be edited by the user, within the range of 1 to 30, by using the option [XPAR EDIT PARAMETER] Edit Parameter Values.</p></td>
</tr>
<tr class="odd">
<td>High Risk MH Proactive Nightly Report [SD MH PROACTIVE BGJ REPORT]</td>
<td><p>This report is a background job that will list the daily appointments for patients with a High Risk for Suicide PRF.</p>
<p>This report will be kicked off by the Scheduling nightly background Job (SDAM BACKGROUND JOB) that should already be scheduled to run nightly on your system.</p>
<p>This report is sent in a mail message to members of the SD MH NO SHOW NOTIFICATION mail group.</p>
<p>Future appointments will be listed on this report. The number of days (of future appointments) is defaulted to 30 days in the future.</p>
<p>A new parameter SD MH PROACTIVE DAYS has been added to store the number of days to list future appointments for each patient on the report. This parameter can be edited by the user, within the range of 1 to 30, by using the option [XPAR EDIT PARAMETER] Edit Parameter Values.</p></td>
</tr>
<tr class="even">
<td>High Risk MH Proactive Adhoc Report [SD MH PROACTIVE AD HOC REPORT]</td>
<td><p>This Adhoc report option generates a proactive report that can be run by the users. This report is more flexible and allows users to refine the report to their specifications.</p>
<p>This option generates the HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY CLINIC for Appointments Report that can be sorted by all clinics or by Mental Health clinics only. This report allows users to refine the report to their specifications.</p>
<p>This report displays appointments for High Risk for Suicide patients that have appointments for today, by divisions for all patients with Patient Record Flag (PRF) High Risk for Suicide that have appointments in mental health clinics today, totals to show the number of unique patients by division, list patients alphabetically by division and by date/time of the appointment, and will also display national as well as local PRF activity.</p></td>
</tr>
<tr class="odd">
<td>High Risk MH No-Show Adhoc Report and High Risk MH No-Show Nightly Report</td>
<td><p>These reports support following up with High Risk for Suicide patients who missed a scheduled MH appointment. It displays all patients that no-showed for their scheduled appointment.</p>
<p>The following information has been added to BOTH reports:</p>
<ul>
<li><p>The provider name is displayed directly underneath the No Show Appointment information to keep everything connected.</p></li>
<li><p>Key for appointment status abbreviations (NS, NA, NAT) added to the heading and will now print on every page break.</p></li>
<li><p>Appointment line now displays information in two lines:</p>
<ul>
<li><p>line one: count, patient name. Patient ID 1st initial last name + last 4 SSN, appointment D/T, 30 character clinic name</p></li>
<li><p>line two: appointment status abbreviation, appointment provider name</p></li>
</ul></li>
<li><p>Patient ID is now 5 characters: first initial of last name + last 4 of SSN</p></li>
<li><p>30-character Clinic name in both future and appointment data information</p></li>
<li><p>AM and PM removed from the date/time of appointment.</p></li>
</ul>
<blockquote>
<p>The following information has been added only to the High Risk MH No-Show Adhoc Report:</p>
</blockquote>
<ul>
<li><p>The report now displays the name of the Mental Health Treatment Coordinator (MHTC) and the name of the care team they are assigned to in parentheses</p></li>
<li><p>The results of the no show patient contact</p></li>
<li><p>Results added for resolution: Reminder term and health factor Information.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## ACRP Database Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option has been exported as a stand-alone option to be run by OITin consultation with the Scheduling Supervisor or assigned to the Scheduling Supervisor to be run in consultation with OIT. It was implemented some time ago but included here for historical reference.

The purpose of the database conversion is to convert old Scheduling encounter information into the Visit Tracking/Patient Care Encounter (PCE) database. Scheduling encounters include appointments, add/edits, and dispositions.

All data from 10/1/96 on is already part of the PCE database and does not need to be converted. This one option provides the functionality necessary to accomplish all aspects of the database conversion.

The conversion is accomplished by creating Conversion Specification Templates (CSTs).

They contain the user-specified criteria that defines a set of records (based on a time frame) to be converted from the current file structure to the new file structure. The CST also maintains an error log and an event log for conversion-process tracking.

There are 3 functions (or events) relating to the CST.

1.  Estimate - Determines amount of disk space the conversion will take. Estimating is not mandatory. Once you’ve started the conversion, you cannot go back and estimate.
2.  Convert - Actually converts the data into PCE files.
3.  Cancel - Once canceled, no further action can be taken against a CST. However, another CST can be created that includes the same time frame.

Once the event has started, the actions shown on the CST Master List screen will go from “queued” to “started” to “completed” without user intervention. If the task never starts, contact OIT Service to find out why.

The templates listed on the CST Master List are in date range order.

When one is added, it will be placed on the list in date order. The asterisk (\*) before a date range indicates there is a gap between that date range and the entry preceding it.

The following ACRP Database Conversion parameters are set through the Display/Edit Parameters action.

<span id="_Toc54883343" class="anchor"></span>Table : ACRP Database Conversion Parameters

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PARAMETER</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Earliest Encounter Date</td>
<td>This field contains the earliest allowable date to convert encounters (cannot be before 10/1/80). For example, if 1/1/86 is entered in this field, encounters before 1/1/86 cannot be converted via the encounter conversion utilities. Additionally, all data from this date through 9/30/96 must be converted before the database conversion at your site can be designated as complete. Limit Conv Range To 1 Year: No// (0 Or No; 1 Or Yes). Set this field to YES if you wish to limit the Scheduling conversion date range for a CST to a maximum of 1 year.</td>
</tr>
<tr class="even">
<td>Default Disposition Clinic</td>
<td>If a valid disposition clinic cannot be determined for the division, this field contains the pointer to the disposition clinic that will be used for the conversion of dispositions.</td>
</tr>
<tr class="odd">
<td>Maximum Errors Allowed: 1000//</td>
<td>If a CST produces this number of errors in the CST Error Log, processing of the conversion for the template will be stopped. If this field contains no value, the system will use 1000.</td>
</tr>
<tr class="even">
<td>Display Cancelled Templates: No// (0 Or No; 1 Or Yes)</td>
<td>This parameter determines whether or not cancelled CSTs are included in the list of templates displayed while using the ACRP Database Conversion option.</td>
</tr>
<tr class="odd">
<td>Date Conversion Completed (Date)</td>
<td>This is the date the entire conversion has been completed at your site. After this date has been entered, no more CSTs can be run. You will only be allowed to make an entry at this parameter when all CSTs are either completed or canceled and when the date range from the earliest encounter date through 9/30/96 has completed conversion.</td>
</tr>
<tr class="even">
<td>Date Deletion Completed (Date)</td>
<td><p>This is the date the last of the following files were deleted from the system.</p>
<p>OPC (#40.1)</p>
<p>OPC ERRORS (#40.15)</p>
<p>SCHEDULING VISITS (#409.5)</p>
<p>OUTPATIENT DIAGNOSIS (#409.43)</p>
<p>OUTPATIENT PROVIDER (#409.44)</p>
<p>Once this date has been entered, the Scheduling software will no longer check these files for visit data. It will only use the PCE V-files.</p>
<p>You will only be allowed to make an entry at this parameter when all CSTs are either completed or canceled.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc54883344" class="anchor"></span>Table : Actions Available from the CST Master List Screen

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PARAMETER</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Add Template</td>
<td><p>These are used to create a CST. You cannot select a CST start date before 9/1/80. After creating a CST, you can initiate the estimate or convert event.</p>
<p>Both events can generate a bulletin when completed - the Scheduling Conversion Global Growth bulletin for the estimate event and the Scheduling Conversion Log bulletin for the convert event. Answer YES to the “Bulletin Upon Completion” prompts if you wish to be notified when the event has completed.</p></td>
</tr>
<tr class="even">
<td>Edit Template</td>
<td>Editing functions are used to perform the following: edit whether or not the bulletin is generated; edit date range when estimating; change event to convert after estimating. Can’t edit CST dates once conversion is started.</td>
</tr>
<tr class="odd">
<td>Schedule/Stop Event</td>
<td>Start, restart, or stop the current conversion event through this action.</td>
</tr>
<tr class="even">
<td>Cancel Template</td>
<td>Canceling functions are used to cancel a CST. You may wish to cancel if estimating showed the selected date range as too large. Once the selected date range has completed converting, the CST cannot be canceled. Even though a CST has been canceled, another CST may be created for the same time frame.</td>
</tr>
<tr class="odd">
<td>View Template</td>
<td>May display conversion data such as template date range, estimate results, last event, last action request, and estimated global growth.</td>
</tr>
<tr class="even">
<td>Mail Estimate Bulletin</td>
<td>Used to get a copy of the estimate bulletin without rerunning the estimate. Goes to the user and whoever has made a request to schedule/stop the event.</td>
</tr>
<tr class="odd">
<td>Refresh List</td>
<td>Used to refresh the screen and update the list with the most recent event status.</td>
</tr>
<tr class="even">
<td>Estimate Summary</td>
<td>Used to obtain a copy of the estimate summary. Categories include global block growth, new entries, modified entries, and global block estimates per entry. You may print summaries to include CST individually (answer YES to CST detail). This summary is used by OIT to help plan disk space requirements.</td>
</tr>
<tr class="odd">
<td>Display/Edit Parameters</td>
<td>Used to enter/edit the database conversion parameters. Some of these include setting the earliest allowable date to convert encounters and limiting the conversion range to one year.</td>
</tr>
<tr class="even">
<td>Convert Single Visit</td>
<td>Used to convert a single visit. The visit may be selected from available records by encounter, disposition, appointment, or standalone add/edit. Identifying information will be displayed for each selection to ensure you have selected the correct visit.</td>
</tr>
<tr class="odd">
<td>Delete Old Files</td>
<td>Once you have converted all the data, you may wish to delete the old Scheduling files. A list of the files that may be deleted will be displayed when selecting this action. It is recommended you back up these files before deletion. All data from your “earliest date to convert” to be converted (with no gaps) before these files can be deleted.</td>
</tr>
</tbody>
</table>

## Actions Available from the CST Detail Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CST Detail Screen is reached by utilizing the View Template action on the CST Master List Screen. No template selection is necessary for these actions as the template has already been selected.

<span id="_Toc54883345" class="anchor"></span>Table : Actions Available from the CST Detail Screen

| PARAMETER          | DESCRIPTION                                                                                                                                                                                             |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Edit Template          | Same as on the CST Master List screen.                                                                                                                                                                      |
| Schedule/Stop Event    | Same as on the CST Master List screen.                                                                                                                                                                      |
| Cancel Template        | Same as on the CST Master List screen.                                                                                                                                                                      |
| Action Request Log     | Prints a list of requests taken against the CST. Includes request date/time, action, event, start date/time, stop date/time (will only appear if an entry was made at the stop date/time prompt), and user. |
| Error Log              | Prints a list of errors for a selected CST. Includes error code number and error text.                                                                                                                      |
| Event Log              | Prints a list of events for a selected CST. Includes event date/time, status, and event.                                                                                                                    |
| Mail Estimate Bulletin | Same as on the CST Master List screen.                                                                                                                                                                      |

## Military Time Conversion Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc54883346" class="anchor"></span>Table : Military Time Conversion Table

| STANDARD       | MILITARY   |
|----------------|------------|
| 12:00 MIDNIGHT | 2400 HOURS |
| 11:00 PM       | 2300 HOURS |
| 10:00 PM       | 2200 HOURS |
| 9:00 PM        | 2100 HOURS |
| 8:00 PM        | 2000 HOURS |
| 7:00 PM        | 1900 HOURS |
| 6:00 PM        | 1800 HOURS |
| 5:00 PM        | 1700 HOURS |
| 4:00 PM        | 1600 HOURS |
| 3:00 PM        | 1500 HOURS |
| 2:00 PM        | 1400 HOURS |
| 1:00 PM        | 1300 HOURS |
| 12:00 NOON     | 1200 HOURS |
| 11:00 AM       | 1100 HOURS |
| 10:00 AM       | 1000 HOURS |
| 9:00 AM        | 0900 HOURS |
| 8:00 AM        | 0800 HOURS |
| 7:00 AM        | 0700 HOURS |
| 6:00 AM        | 0600 HOURS |
| 5:00 AM        | 0500 HOURS |
| 4:00 AM        | 0400 HOURS |
| 3:00 AM        | 0300 HOURS |
| 2:00 AM        | 0200 HOURS |
| 1:00 AM        | 0100 HOURS |

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Also please refer to the OI Master Glossary at REDACTED and at National Acronym Directory: REDACTED
<span id="_Toc54883347" class="anchor"></span>Table : Glossary
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>TERMS</strong></th>
<th><strong>DEFINITION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADD-ONS</td>
<td>Patients who have been scheduled for a visit after routing slips for a particular date have been printed.</td>
</tr>
<tr class="even">
<td>ALOS</td>
<td>Average Length of Stay</td>
</tr>
<tr class="odd">
<td>AMIS</td>
<td>Automated Management Information System</td>
</tr>
<tr class="even">
<td>ANCILLARY</td>
<td>A test added to an existing appointment (i.e. lab, x-ray, EKG) test</td>
</tr>
<tr class="odd">
<td>API</td>
<td>Application Program Interface</td>
</tr>
<tr class="even">
<td>ASU</td>
<td>Authorization/Subscription Utility</td>
</tr>
<tr class="odd">
<td>BILLINGS</td>
<td>Bills sent to veteran</td>
</tr>
<tr class="even">
<td>BRD</td>
<td>Business Requirements Document</td>
</tr>
<tr class="odd">
<td>CLINIC PULL LIST</td>
<td>A list of patients whose radiology/MAS records should be pulled from the file room for use in conjunction with scheduled clinic visits</td>
</tr>
<tr class="even">
<td>COLLATERAL</td>
<td>A visit by a non-veteran patient whose appointment is related to or visit associated with a service-connected patient's treatment.</td>
</tr>
<tr class="odd">
<td>COMPUTERIZED PATIENT RECORD SYSTEM (CPRS)</td>
<td>An integrated, comprehensive suite of clinical applications in VistA that work together to create a longitudinal view of the veteran’s Electronic Medical Record (EMR). CPRS capabilities include a Real Time Order Checking System, a Notification System to alert clinicians of clinically significant events, Consult/Request tracking and a Clinical Reminder System. CPRS provides access to most components of the patient chart.</td>
</tr>
<tr class="even">
<td>CPT</td>
<td>Current Procedural Terminology</td>
</tr>
<tr class="odd">
<td>CR</td>
<td>Clinical Reminders</td>
</tr>
<tr class="even">
<td>CST</td>
<td>Conversion Specification Templates</td>
</tr>
<tr class="odd">
<td>DBIA</td>
<td>Database Integration Agreement</td>
</tr>
<tr class="even">
<td>DRG</td>
<td>Diagnostic Related Group</td>
</tr>
<tr class="odd">
<td>GMTS</td>
<td>Health Summary namespace</td>
</tr>
<tr class="even">
<td>GUI</td>
<td>Graphic User Interface</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>Health Level Seven</td>
</tr>
<tr class="even">
<td>HRMHP</td>
<td>High Risk Mental Health Patient (HRMHP) - Reminder and Flag project is in support of the Improve Veteran Mental Health initiative #5, High Risk Mental Health.</td>
</tr>
<tr class="odd">
<td>ICR</td>
<td>Integration Control Reference</td>
</tr>
<tr class="even">
<td>IRT</td>
<td>Incomplete Records Tracking</td>
</tr>
<tr class="odd">
<td>IVMH</td>
<td>Improve Veteran Mental Health</td>
</tr>
<tr class="even">
<td>MEANS TEST</td>
<td>A financial report upon which certain patients' eligibility for care is based</td>
</tr>
<tr class="odd">
<td>MHTC</td>
<td><p>Mental Health Treatment Coordinator- The liaison between the patient and the mental health system at a VA site. There is only one Mental Health Treatment Coordinator per patient, and they are the key coordinator for behavioral health services care.</p>
<p>For more information about the MH Treatment Coordinator’s responsibilities, see VHA Handbook 1160.1, “Uniform Mental Health Services in VA Medical Centers for Clinics”. Note: In the handbook, the MHTC is called the Principal Mental Health Provider.</p></td>
</tr>
<tr class="even">
<td>MH</td>
<td>Mental Health</td>
</tr>
<tr class="odd">
<td>MHA3</td>
<td>Mental Health Assistant 3 package</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>NO SHOW</td>
<td>A person who did not report for a scheduled clinic visit without prior notification to the medical center.</td>
</tr>
<tr class="even">
<td>NON-COUNT</td>
<td>A clinic whose visits do not affect AMIS statistics.</td>
</tr>
<tr class="odd">
<td>NSR</td>
<td>New Service Request</td>
</tr>
<tr class="even">
<td>OE/RR</td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="odd">
<td>OPC</td>
<td>Outpatient Clinic</td>
</tr>
<tr class="even">
<td>OR</td>
<td>CPRS Order Entry/Results Reporting namespace</td>
</tr>
<tr class="odd">
<td>PAF</td>
<td>Patient Assessment File; where PAI information is stored until transmission to Austin.</td>
</tr>
<tr class="even">
<td>PAI</td>
<td>Patient Assessment Instrument</td>
</tr>
<tr class="odd">
<td>PCE</td>
<td>Patient Care Encounter</td>
</tr>
<tr class="even">
<td>PCMM</td>
<td>Primary Care Management Module</td>
</tr>
<tr class="odd">
<td>PRF</td>
<td>Patient Record Flag</td>
</tr>
<tr class="even">
<td>PMHP</td>
<td><p>See MHTC</p>
<p>Principal Mental Health Provider</p></td>
</tr>
<tr class="odd">
<td>PTF</td>
<td>Patient Treatment File</td>
</tr>
<tr class="even">
<td>PULL LIST</td>
<td>A list of patients whose radiology/PIMS records should be "pulled" from the file room for scheduled clinic visits</td>
</tr>
<tr class="odd">
<td>PX</td>
<td>Patient Care Encounter namespace</td>
</tr>
<tr class="even">
<td>PXRM</td>
<td>Clinical Reminders package namespace</td>
</tr>
<tr class="odd">
<td>RAM</td>
<td>Resource Allocation Methodology</td>
</tr>
<tr class="even">
<td>ROUTING SLIP</td>
<td>When printed for a specified date, it shows the current appointment time, clinic, location, and stop code. It also shows future appointments.</td>
</tr>
<tr class="odd">
<td>RPC</td>
<td>Remote Procedure Calls</td>
</tr>
<tr class="even">
<td>RSD</td>
<td>Requirements Specification Document</td>
</tr>
<tr class="odd">
<td>RUG</td>
<td>Resource Utilization Group</td>
</tr>
<tr class="even">
<td>SBR</td>
<td>Suicide Behavior Report</td>
</tr>
<tr class="odd">
<td>SHARING AGREEMENT</td>
<td>Agreement or contract under which patients from other government agencies or private facilities are treated.</td>
</tr>
<tr class="even">
<td>SME</td>
<td>Subject Matter Expert</td>
</tr>
<tr class="odd">
<td>SPECIAL SURVEY</td>
<td>An ongoing survey of care given to patients alleging Agent Orange or Ionizing Radiation exposure. Each visit by such patients must receive "special survey dispositioning" which records whether treatment provided was related to their exposure. This data is used for Congressional reporting.</td>
</tr>
<tr class="even">
<td>STOP CODE</td>
<td><p>A three-digit number corresponding to an additional stop/service a patient received in conjunction with a clinic visit.</p>
<p>Stop code entries are used so that medical facilities may receive credit for the services rendered during a patient visit.</p></td>
</tr>
<tr class="odd">
<td>THIRD PARTY</td>
<td>Billings where a party other than the patient is billed</td>
</tr>
<tr class="even">
<td>TIU</td>
<td>Text Integration Utility</td>
</tr>
<tr class="odd">
<td>TSR</td>
<td>Treating Specialty Report</td>
</tr>
<tr class="even">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Information System and Technology Architecture</td>
</tr>
</tbody>
</table>
