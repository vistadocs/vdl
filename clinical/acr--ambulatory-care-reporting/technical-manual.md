---
title: Ambulatory Care Reporting Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: plain
doc_subject: Ambulatory Care Reporting
app_code: ACR
app_name: Ambulatory Care Reporting
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: 
  - 44
security_keys: []
menu_options: 17
description: This section defines the HL7 message transactions that are necessary to support the outpatient database interface for the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)).
audience: 
keywords: 
  - strong
  - class
  - table
  - patient
  - contents
  - even
  - style
  - width
  - date
  - message
page_count: 0
word_count: 64992
section_count: 111
table_count: 76
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: May 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Ambulatory_Care_Reporting/acr_p_pimstm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Ambulatory_Care_Reporting/acr_p_pimstm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=116"
---

Patient Information Management System (PIMS)Patient Registration, Admission, Discharge, Transfer, And Appointment SchedulingTechnical Manual

![](ambulatory-care-reporting-technical-manual/001.png)

Version 5.3October 2018Department of Veterans AffairsOffice of Information and TechnologyProduct Development

This Page Left Blank Intentionally

<span id="_Toc522259202" class="anchor"></span>Revision History

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>DATE</strong></th>
<th><strong>PAGE #</strong></th>
<th><strong>DESCRIPTION</strong></th>
<th><strong>PROJECT MANAGER</strong></th>
<th><strong>TECHNICAL WRITER</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Oct 2018</td>
<td><a href="#p2">2</a>, <a href="#p11">3</a>, <a href="#p4">167</a></td>
<td>Updated to reflect changes from patch SD*5.3*640, ACRP and APM HL7 Shutdown. This includes adding notations regarding the ACRP and APM transmissions and related menu options that are being disabled.</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>May 2014</td>
<td><p><a href="#ICDp9">9</a></p>
<p><u><a href="#dg1---diagnosis-information-segment">182</a>-</u><a href="#icdp183">183</a></p></td>
<td><p>SD*5.3*593 – Changed ICD9 to ICD in Callable Routines</p>
<p>Updated the DG1 - Diagnosis Information Segment table</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/23/2013</td>
<td></td>
<td><p>SD*5.3*588 – High Risk Mental Health Proactive Report patch exported the following:</p>
<p>Updated the Implementation and Maintenance Section Eligibility/ID Maintenance Menu with current information and four new SD parameters.</p>
<p>Updated Routines Section new and modified SD routines.</p>
<p>Updated Exported Options Section with two new SD and two modified SD options.</p>
<p>Updated Callable Routines/Entry Points/Application Program Interfaces Sections with SD routine information.</p>
<p>Updated External Relationships Section with the Scheduling Reports required patch information.</p>
<p>DG*5.3*849 – DGPF New Cat 1 Flag and Conversion &amp; Supporting Reports patch</p>
<p>Updated Implementation and Maintenance Section with PRF NATIONAL FLAG file (#26.15) new entry.</p>
<p>Updated Routines Section with new DG routines.</p>
<p>Updated Exported Options Section with new Convert Local HRMH PRF to National Action [DGPF LOCAL TO NATIONAL CONVERT] option<em><strong>.</strong></em></p>
<p>Updated Reference Material Section with SD and DG manual releases. Corrected existing reference manuals names.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/12/2012</td>
<td></td>
<td>SD*5.3*589 – Minor updates, Added 404.61: MH PCMM STOP CODES file to file list</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/18/2012</td>
<td></td>
<td>Updated API List</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/18/2012</td>
<td></td>
<td><p>Phase I - Patches included in the High Risk Mental Health (HRMH) Project:</p>
<p>Patch DG*5.3*836 - HRMH-VISTA CHANGES FOR NATIONAL REMINDER &amp; FLAG. This is a Registration patch containing Patient Record Flag APIs.</p>
<p>DGPFAPIH and DGPFAPIU are new routines.</p>
<p>Patch SD*5.3*578 – HIGH RISK MENTAL HEALTH NO SHOW REPORT. This is a Scheduling patch with a new nightly run and Ad-hoc Missed Appt Report option.</p>
<p>Added two new Scheduling reports that identify no-show “high risk for suicide” patients that missed their MH appointments.</p>
<p>SDMHAD, SDMHAD1, SDMHNS, and SDMHNS1 are new routine.</p>
<p>SD MH NO SHOW NIGHTLY BGJ and No Show Nightly Background Job are being added to the Background Job Options.</p>
<p>Glossary of Terms added.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01/04/2011</td>
<td></td>
<td>DG*5.3*754 – ESR 3.1 – removed the Confidential Address Phone Number from the HL7 PID Segment Tables.</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/18/2010</td>
<td></td>
<td>DG*5.3*754 – ESR 3.1 – Updated Alpha Subscripts section, added ADD^VADPT (29) &amp; “CPN”, added OPD^VADPT (8) &amp; “WP”.</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/05/2009</td>
<td></td>
<td>DG*5.3*754 – ESR 3.1 – Updated VADPT Variables section, added ADD^VADPT (Conf. Phone Number, OPD^VADPT (Patient’s Phone Number (Work), added SEQ 13 to the PID - Patient Identification Segment.</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/30/2009</td>
<td></td>
<td><p>DG*5.3*688 and SD*5.3*441</p>
<p>Enrollment VistA Changes Release 2 (EVC R2)</p>
<p>Added additional Value of “O” for “Other” to Table VA0046 - Agent Orange Exposure Location. Removed Unknown value.</p>
<p>Changed Environmental Contaminants to SW Asia Conditions.</p>
<p>Added entries to Part 5 of the CALLABLE ENTRY POINTS IN VADPT section.</p>
<p>SVC^VADPT modified to add VASV (14) and VASV (14,1) to the VASV array for project SHAD. Added alpha subscripts to ADD^VADPT section. Added alpha subscripts to SVC^VADPT to reflect the alpha translation.</p>
<p>Replaced HL7 Control Segment - 2.3.6 PID-Patient Identification Segment table - with referral to MPI site on VDL.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01/29/2009</td>
<td></td>
<td>Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC)</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/23/2008</td>
<td></td>
<td>DG*5.3*763 – Hold Debt to DMC – Added ENROLLMENT RATED DISABILITY UPLOAD AUDIT file to the Files Section (File List) and Security Section (FileMan Access Codes). Added DGEN RD UPLOAD AUDIT PURGE background job option.</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/01/2008</td>
<td></td>
<td>DG*5.3*779 – Added DGEN NEACL MGT RPT1BK background job option</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>06/20/2008</td>
<td></td>
<td>DG*5.3*782 – updated Religion File</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/04/2008</td>
<td></td>
<td>DG*5.3*644 – Home Telehealth enhancements</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/16/2008</td>
<td></td>
<td>SD*5.3*253, SD*5.3*275, SD*5.3*283, SD*5.3*285, SD*5.3*301, SD*5.3*310, SD*5.3*316, SD*5.3*347, SD*5.3*508 – Added/updated Scheduling Application Programmer Interfaces (APIs) section</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/26/2007</td>
<td></td>
<td>DG*5.3*707 – added “HL7 Generic PID,EVN,PV1 Segment Builder established by MPI” to the HL7 Interface Specifications section</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/27/2006</td>
<td></td>
<td>DG*5.3*650 - added two new files - #26.19 and #26.21</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/20/2006</td>
<td></td>
<td>DG*5.3*689 OEF/OIF Enhancements - updated SVC^VADPT Variable segment section</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/28/2006</td>
<td></td>
<td>DG*5.3*692 Enhancement - updated HL7 Interface Spec for Transmission of Ambulatory Care Data</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>03/22/2006</td>
<td></td>
<td>DG*5.3*687 Maintenance – remove PTF Archive/Purge function</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/12/2005</td>
<td></td>
<td><p>DG*5.3*624 - (10-10EZ 3.0)</p>
<p>Deleted DGRPT 10-10T REGISTRATION input template in the Compiled Template Routines section</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/05/2005</td>
<td></td>
<td>DG*5.3*666 Enhancement - added Background Job Option</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/15/2004</td>
<td></td>
<td>Manual updated to comply with SOP 192-352 Displaying Sensitive Data</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/9/2004</td>
<td></td>
<td>DG*5.3*415-Race and Ethnicity Addition to VADPT variable section (patch released in 2003, change omitted in error)</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

This Page Left Blank Intentionally

Table of Contents

This Page Left Blank Iintentionally

<span id="_Toc522259203" class="anchor"></span>Figures

None

<span id="_Toc522259204" class="anchor"></span>Tables

[Table 1 - Documentation Symbol / Term Descriptions [xxii](#_Toc323812330)](#_Toc323812330)

This Page Left Blank Intentionally

<span id="_Toc522259205" class="anchor"></span>Orientation

<span id="_Toc522259206" class="anchor"></span>Intended Audience

This technical manual is a required documentation component that provides sufficient technical information about the software for programmers and technical personnel to operate and maintain the software with only minimal assistance from the product support personnel.

<span id="_Toc522259207" class="anchor"></span>How to Use this Manual

The PIMS Technical Manual has been divided into sections for general clarity and simplification of the information being presented. This manual is intended to be a reference document. While the user is free to review the entire document, it is best used by selecting specific sections which contain the information sought for a particular need.

Information concerning package security may be found in the Security section of this manual.

The PIMS Technical Manual is provided in its native format (M.S. Word) and as a searchable Adobe Acrobat PDF (portable document format) file. An Acrobat Reader may be used to view the documents. If you do not have the Acrobat Reader loaded, it is available from the VISTA Home Page, “Viewers” Directory.

Once the file is opened, click on the desired entry name in the table of contents on the left side of the screen to go to that entry in the document. Any or all pages of the file may be printed. Click on the “Print” icon and select the desired pages. Then click “OK”.

Each menu file contains a listing of the menu, a brief description of the options contained therein, and the actual option documentation. The option documentation gives a detailed description of the option and what it is used for. It contains any special instructions related to the option.

<span id="_Toc522259208" class="anchor"></span>Documentation Navigation

Document Navigation—this document uses Microsoft® Word's built-in navigation for internal hyperlinks. To add back and forward navigation buttons to the toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word 2007 (not the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the dropdown arrow in the "Choose commands from:" box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column to the Back command (green circle with arrow pointing left).
6.  Click/Highlight the Back command and press the Add button to add to the customized toolbar.
7.  Scroll through the command list in the left column to the Forward command (green circle with arrow pointing right).
8.  Click/Highlight the Forward command and press the Add button to add to the customized toolbar.
9.  Press OK.

The Back and Forward command buttons in the Toolbar are now available to navigate back and forth in the Word document when clicking on hyperlinks within the document.

<span id="_Toc522259209" class="anchor"></span>Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

Various symbols/terms are used throughout the document to alert the reader to special information. The following table gives a description of each of these symbols/terms:

<span id="_Toc323812330" class="anchor"></span>Table 1 - Documentation Symbol/Term Descriptions

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Symbol</td>
<td>Description</td>
</tr>
<tr class="even">
<td>![](ambulatory-care-reporting-technical-manual/002.png)</td>
<td><p><strong>NOTE/REF:</strong> Used to inform the reader of general information including references to additional reading material.</p>
<p>In most cases users will need this information, or at least it will make the installation smoother and more understandable. Please read each note <em>before</em> executing the steps that follow it!</p></td>
</tr>
<tr class="odd">
<td>![](ambulatory-care-reporting-technical-manual/003.png)</td>
<td><strong>CAUTION, DISCLAIMER, or RECOMMENDATION:</strong> Used to inform the reader to take special notice of critical information.</td>
</tr>
</tbody>
</table>

Descriptive text is presented in a proportional font (as represented by this font).

"Snapshots" of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.

- User's responses to online prompts and some software code reserved/key words will be bold typeface and highlighted in yellow.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                   |                                                                                                                                            |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ambulatory-care-reporting-technical-manual/004.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- Bold Typeface:
  - All computer keys when referenced with a command (e.g., "press Enter" or "click OK").
  - All references to computer dialogue tab or menu names (e.g., "go to the General tab" or "choose Properties from the Action menu").
  - All values entered or selected by the user in computer dialogues (e.g., "Enter 'xyz' in the Server Name field" or "Choose the ABCD folder entry from the list").
  - All user text (e.g., commands) typed or entered in a Command-Line prompt (e.g., "Enter the following command: CD xyz").
- Italicized Typeface:
  - Emphasis (e.g., do *not* proceed or you *must* do the following steps).
  - All reference to computer dialogue or screen titles (e.g., "in the *Add Entries* dialogue…").
  - All document or publication titles and references (e.g., "see the *ABC Installation Guide*").

Step-by-Step Instructions—for documentation purposes, explicit step-by-step instructions for repetitive tasks (e.g., "Open a Command-Line prompt") are generally only provided once. For subsequent steps that refer to that same procedure or task, please refer back to the initial step where those instructions were first described.

Conventions for displaying TEST data in this document are as follows:

- The first three digits (prefix) of any Social Security Numbers (SSN) must begin with either "000" or "666".
- Patient and user names are formatted as follows:  
    
  \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry.  
    
  For example, in LSRP test patient and user names would be documented as follows: LSRPPATIENT, ONE; LSRPPATIENT, TWO; LSRPPATIENT, THREE; etc.

<span id="_Toc522259210" class="anchor"></span>On-line Help System

When the format of a response is specific, there usually is a HELP message provided for that prompt. HELP messages provide lists of acceptable responses or format requirements which provide instruction on how to respond.

A HELP message can be requested by typing a "?" or "??". The HELP message will appear under the prompt, then the prompt will be repeated. For example, at the following prompt

Sort by TREATING SPECIALTY:

enter "?" and the HELP message would appear.

Sort by TREATING SPECIALTY?

CHOOSE FROM:

SURGERY

CARDIOLOGY

12 PSYCHIATRY

Sort by TREATING SPECIALTY:

For some prompts, the system will list the possible answers from which to choose. Any time choices appear with numbers, the system will usually accept the number or the name.

A HELP message may not be available for every prompt. If a "?" or "??" is entered at a prompt that does not have a HELP message, the system will repeat the prompt.

<span id="_Toc522259211" class="anchor"></span>Acronyms

National Acronym Directory: <http://vaww1.va.gov/Acronyms/>

<span id="_Toc522259212" class="anchor"></span>Reference Materials

The following manuals are available from the VistA Documentation Library (VDL) <http://www.va.gov/vdl>:

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 32%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>DOCUMENTATION NAME</strong></th>
<th><strong>FILE NAME</strong></th>
<th><strong>LOCATION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>High Risk Mental Health Patient Project Installation and Setup Guide</td>
<td>PXRM_2_24_IG.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="even">
<td>PIMS Technical Manual</td>
<td>PIMSTM.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="odd">
<td>PIMS Scheduling User Manual - Outputs Menu</td>
<td>PIMsSchOutput.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="even">
<td>PIMS Scheduling User Manual - Menus, Intro &amp;Orientation, etc.</td>
<td>PIMsSchIntro.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="odd">
<td>Patient Record Flag User Guide</td>
<td>PatRecFlagUG.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="even">
<td>Scheduling and Registration Installation and Setup Guide</td>
<td>SDDG_Install_Review.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="odd">
<td>High Risk Mental Health Patient Project Installation and Setup Guide</td>
<td><p>PXRM_2_18_IG.PDF</p>
<p>PXRM_2_18_IG.doc</p></td>
<td><p>VDL</p>
<p>Clinical Reminders website</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="even">
<td>Scheduling Patch 578 Installation and Setup Guide</td>
<td>SD_5_3_578_IG.PDF</td>
<td>Anonymous Directories</td>
</tr>
<tr class="odd">
<td>Registration Patch 836 Installation and Setup Guide</td>
<td>DG_5_3_836_IG.PDF</td>
<td>Anonymous Directories</td>
</tr>
</tbody>
</table>

# Introduction & Software Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction & Software Purpose](#introduction-software-purpose)
  - [Namespace Conventions](#namespace-conventions)
  - [Background Job Options](#background-job-options)
  - [SACC Exemptions/Non-Standard Code](#sacc-exemptionsnon-standard-code)
  - [Primary Care Management Module (PCMM) Overview](#primary-care-management-module-pcmm-overview)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Eligibility ID/Maintenance Menu](#eligibility-idmaintenance-menu)
  - [Station Number (Time Sensitive) Enter/Edit (D ^VASITE0)](#station-number-time-sensitive-enteredit-d-vasite0)
  - [New SD Parameters](#new-sd-parameters)
  - [PRF NATIONAL FLAG file (#26.15)](#prf-national-flag-file-2615)
- [Routines](#routines)
  - [Routines To Map](#routines-to-map)
  - [Callable Routines](#callable-routines)
  - [Compiled Template Routines](#compiled-template-routines)
    - [Input Templates](#input-templates)
    - [Print Templates](#print-templates)
    - [Compiled Cross-Reference Routines](#compiled-cross-reference-routines)
  - [Routine List](#routine-list)
  - [New and Modified Routines](#new-and-modified-routines)
  - [Patch SD\5.3\588 Routines](#patch-sd53588-routines)
  - [Patch DG\5.3\849 Routines](#patch-dg53849-routines)
  - [Patch SD\5.3\578 Routines](#patch-sd53578-routines)
  - [Patch DG\5.3\836 Routines](#patch-dg53836-routines)
- [Files](#files)
  - [Globals and Files](#globals-and-files)
  - [File List](#file-list)
- [Files and Templates in the PIMS Package](#files-and-templates-in-the-pims-package)
  - [File Flow (Relationships between files)](#file-flow-relationships-between-files)
  - [Templates](#templates)
  - [VA FileMan Functions](#va-fileman-functions)
- [Exported Options](#exported-options)
  - [Menu Diagrams](#menu-diagrams)
  - [Exported Protocols](#exported-protocols)
  - [Exported Options](#exported-options-1)
  - [Exported Remote Procedures](#exported-remote-procedures)
  - [Exported HL7 Applications for Ambulatory Care Reporting](#exported-hl7-applications-for-ambulatory-care-reporting)
  - [Exported HL7 Applications For Inpatient Reporting To National Patient Care Database](#exported-hl7-applications-for-inpatient-reporting-to-national-patient-care-database)
  - [Exported HL7 Applications for Home Telehealth Care Database](#exported-hl7-applications-for-home-telehealth-care-database)
  - [Exported Scheduling Options](#exported-scheduling-options)
  - [Exported DG Option](#exported-dg-option)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
  - [ADT Module](#adt-module)
  - [ACRP Database Conversion Option](#acrp-database-conversion-option)
  - [HL7 Purger](#hl7-purger)
- [Callable Routines/Entry Points/Application Program Interfaces](#callable-routinesentry-pointsapplication-program-interfaces)
    - [^SDMHAD](#sdmhad)
    - [^SDMHAD1](#sdmhad1)
    - [^SDMHNS](#sdmhns)
    - [^SDMHNS1](#sdmhns1)
    - [^SDAMQ](#sdamq)
    - [^SDMHPRO1](#sdmhpro1)
    - [EN^SDMHAP](#ensdmhap)
- [External/Internal Relations](#externalinternal-relations)
  - [External Relations](#external-relations)
- [DBIA Agreements](#dbia-agreements)
  - [DBIA AGREEMENTS - CUSTODIAL PACKAGE](#dbia-agreements-custodial-package)
  - [DBIA AGREEMENTS - SUBSCRIBER PACKAGE](#dbia-agreements-subscriber-package)
  - [Internal Relations](#internal-relations)
  - [Package-Wide Variables](#package-wide-variables)
  - [VADPT Variables](#vadpt-variables)
    - [Scheduling Variables](#scheduling-variables)
    - [Patient Record Flag Variables](#patient-record-flag-variables)
  - [VAUTOMA](#vautoma)
  - [VAFMON](#vafmon)
  - [AIT](#ait)
- [How To Generate On-Line Documentation](#how-to-generate-on-line-documentation)
  - [XINDEX](#xindex)
  - [INQUIRE TO OPTION FILE](#inquire-to-option-file)
  - [PRINT OPTIONS FILE](#print-options-file)
  - [LIST FILE ATTRIBUTES](#list-file-attributes)
  - [Security](#security)
    - [General Security](#general-security)
    - [Security Keys](#security-keys)
    - [Legal Requirements](#legal-requirements)
  - [FileMan Access Codes](#fileman-access-codes)
- [VADPT Variables](#vadpt-variables-1)
  - [SUPPORTED REFERENCES](#supported-references)
  - [CALLABLE ENTRY POINTS IN VADPT](#callable-entry-points-in-vadpt)
    - [DEM^VADPT](#demvadpt)
    - [ELIG^VADPT](#eligvadpt)
    - [MB^VADPT](#mbvadpt)
    - [SVC^VADPT](#svcvadpt)
    - [ADD^VADPT](#addvadpt)
    - [OAD^VADPT](#oadvadpt)
    - [INP^VADPT](#inpvadpt)
    - [IN5^VADPT](#in5vadpt)
    - [OPD^VADPT](#opdvadpt)
    - [REG^VADPT](#regvadpt)
    - [SDE^VADPT](#sdevadpt)
    - [SDA^VADPT](#sdavadpt)
    - [PID^VADPT](#pidvadpt)
    - [PID^VADPT6](#pidvadpt6)
    - [ADM^VADPT2](#admvadpt2)
    - [KVAR^VADPT](#kvarvadpt)
    - [KVA^VADPT](#kvavadpt)
    - [COMBINATIONS](#combinations)
  - [Alpha Subscripts](#alpha-subscripts)
- [Scheduling Application Programmer Interfaces (APIs)](#scheduling-application-programmer-interfaces-apis)
    - [Special Features](#special-features)
  - [SDAPI - EXAMPLES](#sdapi-examples)
  - [SDAPI - Data Fields](#sdapi-data-fields)
  - [SDAPI - Filters](#sdapi-filters)
    - [Available Data Filters](#available-data-filters)
    - [Input – Other Array Entries](#input-other-array-entries)
    - [Other Array Entries](#other-array-entries)
    - [SDAPI - Error Codes](#sdapi-error-codes)
    - [SDAPI - Constraints](#sdapi-constraints)
    - [Application Programmer Interface - GETAPPT](#application-programmer-interface-getappt)
  - [Application Programmer Interface - NEXTAPPT](#application-programmer-interface-nextappt)
  - [Application Programmer Interface - GETPLIST](#application-programmer-interface-getplist)
  - [Application Programmer Interface - PATAPPT](#application-programmer-interface-patappt)
- [Data Fields](#data-fields)
  - [Available Data Fields](#available-data-fields)
  - [FILTERS](#filters)
    - [Valid Appointment Status Filters](#valid-appointment-status-filters)
    - [Valid Patient Status Filters](#valid-patient-status-filters)
    - [### Valid Patient Status and Appointment Status Filter Combinations](#valid-patient-status-and-appointment-status-filter-combinations)
  - [Application Programmer Interface - SDIMO](#application-programmer-interface-sdimo)
  - [Configuring Bar Code Label Printers for Print Patient Label Option](#configuring-bar-code-label-printers-for-print-patient-label-option)
    - [Hardware Setup](#hardware-setup)
    - [Software Setup](#software-setup)
  - [Control Code Overview](#control-code-overview)
    - [Patient Label Print Routine Control Code Use](#patient-label-print-routine-control-code-use)
    - [Label Printer Setup Examples](#label-printer-setup-examples)
    - [Zebra Label Printer](#zebra-label-printer)
  - [Intermec Label Printer](#intermec-label-printer)
- [HL7 Interface Specification for Transmission of Ambulatory Care Data](#hl7-interface-specification-for-transmission-of-ambulatory-care-data)
  - [Assumptions](#assumptions)
    - [Message Content](#message-content)
    - [Data Capture and Transmission](#data-capture-and-transmission)
    - [Background Messages](#background-messages)
    - [Batch Messages & Acknowledgements](#batch-messages-acknowledgements)
    - [VA MailMan Lower Level Protocol](#va-mailman-lower-level-protocol)
  - [HL7 Control Segments](#hl7-control-segments)
  - [Message Definitions](#message-definitions)
  - [Segment Table Definitions](#segment-table-definitions)
  - [Message Control Segments](#message-control-segments)
    - [MSH - MESSAGE HEADER SEGMENTS](#msh-message-header-segments)
    - [BHS - Batch Header Segment](#bhs-batch-header-segment)
    - [BTS - Batch Trailer Segment](#bts-batch-trailer-segment)
    - [MSA - MESSAGE ACKNOWLEDGMENT SEGMENT](#msa-message-acknowledgment-segment)
    - [EVN - EVENT TYPE SEGMENT](#evn-event-type-segment)
  - [PID - Patient Identification Segment](#pid-patient-identification-segment)
    - [PD1 - Patient Additional Demographic Segment](#pd1-patient-additional-demographic-segment)
    - [PV1 - Patient Visit Segment](#pv1-patient-visit-segment)
    - [PV2 - Patient Visit - Additional Information Segment](#pv2-patient-visit-additional-information-segment)
    - [DG1 - Diagnosis Information Segment](#dg1-diagnosis-information-segment)
    - [PR1 - Procedure Information Segment](#pr1-procedure-information-segment)
    - [### ROL - Role Segment](#rol-role-segment)
    - [ZPD - VA-Specific Patient Information Segment](#zpd-va-specific-patient-information-segment)
    - [ZEL - VA-Specific Patient Eligibility Segment](#zel-va-specific-patient-eligibility-segment)
    - [VA-Specific Income Segment](#va-specific-income-segment)
    - [ZCL - VA-Specific Outpatient Classification Segment](#zcl-va-specific-outpatient-classification-segment)
    - [Zsc - VA-Specific Stop Code Segment](#zsc-va-specific-stop-code-segment)
    - [ZSP - VA-Specific Service Period Segment](#zsp-va-specific-service-period-segment)
    - [ZEN - VA-Specific Enrollment Segment](#zen-va-specific-enrollment-segment)
  - [PURPOSE](#purpose)
  - [Trigger Events and Message Definitions](#trigger-events-and-message-definitions)
    - [Update Patient Information (A08)](#update-patient-information-a08)
    - [Delete a Patient Record (A23)](#delete-a-patient-record-a23)
  - [SUPPORTED AND USER-DEFINED HL7 TABLES](#supported-and-user-defined-hl7-tables)
    - [TABLE 0001 - SEX](#table-0001-sex)
    - [TABLE 0002 - MARITAL STATUS](#table-0002-marital-status)
    - [TABLE 0003 - EVENT TYPE CODE](#table-0003-event-type-code)
    - [TABLE 0008 - ACKNOWLEDGMENT CODE](#table-0008-acknowledgment-code)
    - [TABLE 0023 - ADMIT SOURCE (USER DEFINED)](#table-0023-admit-source-user-defined)
    - [TABLE 0051 - DIAGNOSIS CODE (USER DEFINED)](#table-0051-diagnosis-code-user-defined)
    - [TABLE 0069 - HOSPITAL SERVICE (USER DEFINED)](#table-0069-hospital-service-user-defined)
    - [TABLE 0076 - MESSAGE TYPE](#table-0076-message-type)
    - [TABLE 0088 - PROCEDURE CODE (USER DEFINED)](#table-0088-procedure-code-user-defined)
    - [TABLE 0115 - SERVICING FACILITY (USER DEFINED)](#table-0115-servicing-facility-user-defined)
    - [TABLE 0133 - PROCEDURE PRACTITIONER TYPE (USER DEFINED)](#table-0133-procedure-practitioner-type-user-defined)
    - [TABLE 0136 - YES/NO INDICATOR](#table-0136-yesno-indicator)
    - [TABLE SD001 - SERVICE INDICATOR (STOP CODE)](#table-sd001-service-indicator-stop-code)
    - [TABLE SD008 - OUTPATIENT CLASSIFICATION TYPE](#table-sd008-outpatient-classification-type)
    - [TABLE SD009 - PURPOSE OF VISIT](#table-sd009-purpose-of-visit)
    - [TABLE VA01 - YES/NO](#table-va01-yesno)
    - [TABLE VA02 - CURRENT MEANS TEST STATUS](#table-va02-current-means-test-status)
    - [TABLE VA04 - ELIGIBILITY](#table-va04-eligibility)
    - [TABLE VA05 - DISABILITY RETIREMENT FROM MILITARY](#table-va05-disability-retirement-from-military)
    - [TABLE VA06 - ELIGIBILITY STATUS](#table-va06-eligibility-status)
    - [TABLE VA07 - RACE](#table-va07-race)
    - [TABLE VA08 - RELIGION](#table-va08-religion)
    - [TABLE VA08 – RELIGION (CONT.)](#table-va08-religion-cont)
    - [TABLE VA10 - MEANS TEST INDICATOR](#table-va10-means-test-indicator)
    - [TABLE VA11 - PERIOD OF SERVICE](#table-va11-period-of-service)
    - [TABLE VA12 - TYPE OF INSURANCE](#table-va12-type-of-insurance)
    - [TABLE VA0015 - ENROLLMENT STATUS](#table-va0015-enrollment-status)
    - [TABLE VA0016 - REASON CANCELED/DECLINED](#table-va0016-reason-canceleddeclined)
    - [TABLE VA0021 - ENROLLMENT PRIORITY](#table-va0021-enrollment-priority)
    - [TABLE VA0022 - RADIATION EXPOSURE METHOD](#table-va0022-radiation-exposure-method)
    - [TABLE VA0023 - PRISONER OF WAR LOCATION](#table-va0023-prisoner-of-war-location)
    - [TABLE VA0024 - SOURCE OF ENROLLMENT](#table-va0024-source-of-enrollment)
    - [TABLE VA0046 - AGENT ORANGE EXPOSURE LOCATION](#table-va0046-agent-orange-exposure-location)
    - [TABLE NPCD 001 - NATIONAL PATIENT CARE DATABASE ERROR CODES](#table-npcd-001-national-patient-care-database-error-codes)
  - [HL7 Interface Specification for the Transmission of PCMM Primary Care Data](#hl7-interface-specification-for-the-transmission-of-pcmm-primary-care-data)
  - [Assumptions](#assumptions-1)
    - [Message Content](#message-content-1)
    - [Data Capture and Transmission](#data-capture-and-transmission-1)
    - [Background Messages](#background-messages-1)
    - [VA MailMan Lower Level Protocol](#va-mailman-lower-level-protocol-1)
  - [Message Definitions](#message-definitions-1)
  - [Segment Table Definitions](#segment-table-definitions-1)
  - [Message Control Segments](#message-control-segments-1)
    - [MSH - Message Header Segment](#msh-message-header-segment)
    - [EVN - Event Type Segment](#evn-event-type-segment-1)
    - [PID - Patient Identification Segment](#pid-patient-identification-segment-1)
    - [ZPC – VA Specific Primary Care Information Segment](#zpc-va-specific-primary-care-information-segment)
- [HL7 message transactions](#hl7-message-transactions)
  - [Trigger Events and Message Definitions](#trigger-events-and-message-definitions-1)
    - [Update Patient Information (A08)](#update-patient-information-a08-1)
    - [Business Rules](#business-rules)
- [SUPPORTED AND USER-DEFINED HL7 TABLES](#supported-and-user-defined-hl7-tables-1)
  - [Table 0001 - Sex](#table-0001-sex-1)
  - [Table 0002 - Marital Status](#table-0002-marital-status-1)
  - [Table 0003 - Event Type Code](#table-0003-event-type-code-1)
  - [Table 0005 - Race](#table-0005-race)
  - [Table 0006 - Religion](#table-0006-religion)
  - [Table 0006 – Religion (cont.)](#table-0006-religion-cont)
  - [Table 0076 - Message Type](#table-0076-message-type-1)
- [HL7 Interface Specification for PCMM Primary Care Acknowledgement Processing](#hl7-interface-specification-for-pcmm-primary-care-acknowledgement-processing)
  - [Message Control Segments](#message-control-segments-2)
    - [MSH - Message Header Segment](#msh-message-header-segment-1)
    - [MSA Message Acknowledgment Segment](#msa-message-acknowledgment-segment-1)
    - [ERR Error Segment](#err-error-segment)
    - [ZPC VA Specific - Primary Care Information Segment](#zpc-va-specific-primary-care-information-segment-1)
  - [Specific Transaction Examples](#specific-transaction-examples)
  - [Supported and User Defined Tables](#supported-and-user-defined-tables)
    - [Table 008 Acknowledgement Code](#table-008-acknowledgement-code)
    - [PCMM Error Code Table](#pcmm-error-code-table)
- [HL7 Interface Specification for VIC Card VistA to NCMD](#hl7-interface-specification-for-vic-card-vista-to-ncmd)
  - [Assumptions](#assumptions-2)
  - [Message Content](#message-content-2)
  - [Data Capture and Transmission](#data-capture-and-transmission-2)
  - [VA TCP/IP Lower Level Protocol](#va-tcpip-lower-level-protocol)
    - [Message Definitions](#message-definitions-2)
    - [Segment Table Definitions](#segment-table-definitions-2)
    - [Message Control Segments](#message-control-segments-3)
    - [MSH - Message Header Segment](#msh-message-header-segment-2)
    - [MSA – Message Acknowledgment Segment](#msa-message-acknowledgment-segment-2)
    - [PID - Patient Identification Segment](#pid-patient-identification-segment-2)
    - [ORC-Common Order Segment](#orc-common-order-segment)
    - [RQD-Requisition Detail Segment](#rqd-requisition-detail-segment)
    - [NTE – Notes and Comments](#nte-notes-and-comments)
  - [Trigger Events and Message Definitions](#trigger-events-and-message-definitions-2)
  - [ORM - General Order Message (event O01)](#orm-general-order-message-event-o01)
  - [ORR – General Order Response Message response to any ORM (event O02)](#orr-general-order-response-message-response-to-any-orm-event-o02)
  - [Supported and User Defined HL7 Tables](#supported-and-user-defined-hl7-tables-2)
    - [Table 0003 - Event Type Code](#table-0003-event-type-code-2)
    - [Table 0008 – Acknowledgment Code](#table-0008-acknowledgment-code-1)
    - [Table 0076 - Message Type](#table-0076-message-type-2)
    - [Table 0119 – Order Control Codes](#table-0119-order-control-codes)
- [HL7 GENERIC PID, EVN, PV1 SEGMENT BUILDER ESTABLISHED BY MPI](#hl7-generic-pid-evn-pv1-segment-builder-established-by-mpi)
  - [Integration Agreement (IA) \#3630](#integration-agreement-ia-3630)
    - [Custodial Package](#custodial-package)
  - [API: BLDEVN^VAFCQRY](#api-bldevnvafcqry)
  - [API: BLDPD1^VAFCQRY](#api-bldpd1vafcqry)
  - [API: BLDPID^VAFCQRY](#api-bldpidvafcqry)
- [HL7 Interface Specification for Home Telehealth (HTH)](#hl7-interface-specification-for-home-telehealth-hth)
  - [Assumptions](#assumptions-3)
  - [Message Content](#message-content-3)
  - [Data Capture and Transmission](#data-capture-and-transmission-3)
- [VA TCP/IP Lower Level Protocol](#va-tcpip-lower-level-protocol-1)
  - [HL7 CONTROL SEGMENTS](#hl7-control-segments-1)
  - [Message Definitions](#message-definitions-3)
  - [Segment Table Definitions](#segment-table-definitions-3)
  - [Message Control Segments](#message-control-segments-4)
- [Glossary](#glossary)
- [Military Time Conversion Table](#military-time-conversion-table)
- [Alphabetical Index of PIMS Terms](#alphabetical-index-of-pims-terms)
The VISTA PIMS package provides a comprehensive range of software supporting the administrative functions of patient registration, admission, discharge, transfer, and appointment scheduling.. Its functions apply throughout a patient's inpatient and/or outpatient stay from registration, eligibility and Means Testing through discharge with on-line transmission of PTF (Patient Treatment File) data and/or NPCDB (National Patient Care Database) data to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). The ADT module aids in recovery of cost of care by supplying comprehensive PTF/RUG-II options and Means Test options.
The ADT and Scheduling modules of PIMS are fully integrated with the VA FileMan, thus allowing ad hoc reports to be extracted by non-programmer personnel. ADT is integrated with V. 2.1 of the Fee Basis software allowing Fee personnel to register patients through a select Fee option.
Related manuals include the PIMS User Manual, the PIMS Release Notes, which describe version specific changes to the PIMS package, and PIMS Installation Guide.
Several features have been designed into the PIMS package to maximize efficiency and maintain control over user access of specified sensitive patient records. The Consistency Checker reduces entry of inaccurate information by warning the user about incompatible or missing data. The Patient Sensitivity function allows a level of security to be assigned to certain records within a database in order to maintain control over unauthorized access. The Patient Lookup screens user access of these sensitive records, as well as providing for more efficient and faster retrieval of patient entries.
Tracking and calculation of data is performed transparently by the system to provide a variety of reports which assist in day-to-day operations as well as provide management with the necessary information to analyze workload and promote quality of care. Highlights include the following.
• Automation of the Daily Gains and Losses Sheet and Bed Status Report
• Inpatient Listings
• Seriously Ill Listings
• Bed Availability Reports
• AMIS Reporting
• Disposition Reporting
• Generic code sheets for reporting AMIS segments
• Automation of Appointment Status Update
Notifications for PIMS may be displayed for admissions, death discharges, deaths, and unscheduled (1010) visits. The notifications (ADMISSION, DECEASED, and UNSCHEDULED (1010) VISIT) will be displayed for patients who are defined as members of a list in the OE/RR LIST file (#100.21). The recipients of the notifications would need to be defined as users in the same OE/RR LIST entry. The notifications will appear as "alerts" when the user is prompted to select an option from a menu. Please refer to the documentation for CPRS for more information concerning OR notifications.

## Namespace Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespaces assigned to the PIMS package are DG, DPT, SD, SC, and VA.

## Background Job Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>OPTION NAME</strong></th>
<th><strong>SUGGESTED RUN FREQUENCY</strong></th>
<th><strong>DEVICE REQUIRED</strong></th>
<th><strong>REMARKS</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DG G&amp;L RECALCULATION AUTO</td>
<td>Nightly</td>
<td>NO</td>
<td>Recommended to run @ 9PM</td>
</tr>
<tr class="even">
<td>DG PRE-REGISTER NIGHT JOB</td>
<td>Nightly</td>
<td>NO</td>
<td>Run during off hours. Set to null device for MSM sites.</td>
</tr>
<tr class="odd">
<td>DG PTF BACKGROUND JOB</td>
<td>Nightly</td>
<td>NO</td>
<td>Run during off hours</td>
</tr>
<tr class="even">
<td>DG RUG BACKGROUND JOB</td>
<td>Daily</td>
<td>YES</td>
<td>-</td>
</tr>
<tr class="odd">
<td>DG RUG SEMI ANNUAL - TASKED</td>
<td>*</td>
<td>YES</td>
<td>*Queued in advance to run on 10/1 and 4/1</td>
</tr>
<tr class="even">
<td>DG SENSITIVE RCDS RPT-TASK</td>
<td>Nightly</td>
<td>NO</td>
<td>Run after midnight</td>
</tr>
<tr class="odd">
<td>DGEN NEACL MGT RPT1BK</td>
<td>Daily</td>
<td>YES</td>
<td>-</td>
</tr>
<tr class="even">
<td>DGEN RD UPLOAD AUDIT PURGE</td>
<td>Daily or Weekly</td>
<td>NO</td>
<td>Purges entries from the ENROLLMENT RATED DISABILITY, UPLOAD AUDIT file (#390) after 365 days</td>
</tr>
<tr class="odd">
<td>DGPF BACKGROUND PROCESSING</td>
<td>Daily</td>
<td>NO</td>
<td>Run during off hours</td>
</tr>
<tr class="even">
<td>DGQE BACKGROUND PROCESSING</td>
<td>Nightly</td>
<td>NO</td>
<td>Run during off hours</td>
</tr>
<tr class="odd">
<td><p>SCDX AMBCAR NIGHTLY XMIT</p>
<p><span id="p2" class="anchor"></span><strong>Note:</strong> This option has been placed out of order with patch SD*5.3*640 since ACRP transmission has been discontinued.</p></td>
<td>Nightly</td>
<td>NO</td>
<td>Collects workload information and sends it to NPCDB in Austin via HL7 messages</td>
</tr>
<tr class="even">
<td>SCENI IEMM SUMMARY BULLETIN</td>
<td>Nightly</td>
<td>NO</td>
<td>Run after nightly transmission to Austin</td>
</tr>
<tr class="odd">
<td>SCMC PCMM HL7</td>
<td>Nightly</td>
<td>NO</td>
<td>Collects PCMM data that needs to be transmitted to Austin in HL7 format</td>
</tr>
<tr class="even">
<td><p>SCRPW APM TASK JOB</p>
<p><span id="p11" class="anchor"></span><strong>Note:</strong> This option has been placed out of order with patch SD*5.3*640 since APM transmission has been discontinued.</p></td>
<td>Monthly</td>
<td>NO</td>
<td>Runs on the 15th of the current month after hours. Generates info rolled up to AITC (formerly AAC) Additional Performance Monitors (TIU).</td>
</tr>
<tr class="odd">
<td>OPTION NAME</td>
<td>SUGGESTED RUN FREQUENCY</td>
<td>DEVICE REQUIRED</td>
<td>REMARKS</td>
</tr>
<tr class="even">
<td>SDAM BACKGROUND JOB</td>
<td>Nightly</td>
<td>NO</td>
<td>-</td>
</tr>
<tr class="odd">
<td><p>SDOQM PM NIGHTLY JOB</p>
<p><strong>Note:</strong> This option has been placed out of order with patch SD*5.3*640 since APM transmission has been discontinued.</p></td>
<td>As directed</td>
<td>YES</td>
<td>Suggested run time @ 2 AM</td>
</tr>
<tr class="even">
<td>VAFC BATCH UPDATE</td>
<td>30 minutes</td>
<td>NO</td>
<td>Transmits changes to key patient demographical data</td>
</tr>
<tr class="odd">
<td>VAFH PIVOT PURGE</td>
<td>Weekly</td>
<td>NO</td>
<td>Purges entries greater than 1.5 years old from ADT/HL7 PIVOT file (#391.71)</td>
</tr>
</tbody>
</table>

## SACC Exemptions/Non-Standard Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain the SACC exemptions for the PIMS package.

1\. FORUM

2\. DBA Menu

3\. SACC Exemptions Menu

4\. Display Exemptions for a Package Option

5\. Select SACC Exemptions package: ADT SD

## Primary Care Management Module (PCMM) Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Primary Care Management Module was developed to assist VA facilities in implementing primary care. It will support both primary care teams and non-primary care teams. PCMM’s functionality is divided into eight areas:

- Setup & Define Team
- Assign Staff to Positions in Teams
- Assign Patient to Team
- Assign Patient to Practitioner via Team Position and Enroll in a Clinic
- Reports/Outputs/Mail Messages
- Tools to Ease Startup Process of Primary Care
- Other Changes to Scheduling Package
- Application Program Interface (API) calls.

PCMM uses a Graphical User Interface (GUI) to control the startup, setup, and assignment functions. To use the functionality in the PCMM, a site will need a Microsoft Windows workstation which has a connection to VistA (either LAN or serial connection) for each location where a patient or staff member is assigned to a team. A typical site will want one workstation for each team, one for the PIMS ADPAC, plus one for the manager in charge of primary care. Existing Scheduling functionality will continue to be useable from “roll and scroll” terminals.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of the PIMS Technical Manual provides information to assist technical support staff with the implementation and maintenance of the software. This section should include information regarding the entry of required site-specific data, including where applicable.

The PIMS package may be tailored specifically to meet the needs of the various sites. Instructions may be found in the User Manual under the ADT Module, Supervisor ADT and the Scheduling Module, Supervisor. A variety of options are included in these sections allowing each site to define its own configuration. The ADT portion of the PIMS package will function around the parameters defined through the MAS Parameter Entry/Edit option while the Scheduling portion parameters are defined through the Scheduling Parameters option.

A great many other options are included in these Supervisor sections which assist in site configuration and maintenance functions. Among them are options which allow for specification of mail groups to receive certain bulletins, definition of devices, designation of transmission routers, entry/edit of Means Test data, ward set-up, and clinic set-up. All configurations may be modified at any time as the site's needs change.

The Scheduling Parameters file (#404.91) may be used to modify the behavior of PCMM. The USE USR CLASS FUNCTIONALITY? field (#801) can be used to turn on/off the user class functionality provided by the Authorizations/ Subscriptions software. This functionality allows certain staff members/users (especially clinicians) to be classified in a very specific manner (e.g., cardiologist), and yet the software can determine that the staff member is a member of a more general class (e.g., provider).

If a site has A/S installed prior to the PCMM installation, PCMM will default to use the user class functionality. Sites that have not populated the USR CLASS MEMBERSHIP file (#8930.3) for their potential team members should have this parameter set to NO. Sites that have fully populated this file should set this parameter to YES because the assignment of staff members to teams will be less error-prone and faster than the unscreened selection from the NEW PERSON file (#200).

The CHECK PC TEAM AT DISCHARGE? field (#802) can be used to turn off the PCMM functionality which, upon inpatient discharge, checks the patient's primary care assignments. If the patient has current primary care data, it is displayed. If the patient does not have a current primary care team assignment, the user will be prompted to assign the patient to a primary care team.

The ENABLE AUTOLINK FUNCTIONALITY? field (#803) should be turned off until OE/RR is installed. Although there is no harm in allowing users to add/edit auto link data, this will not be usable until OE/RR is installed. The auto link functionality was added for use by OE/RR teams.

## Eligibility ID/Maintenance Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Eligibility/ID Maintenance Menu provides the options needed to accommodate VA/DOD sharing agreement requirements with regard to Patient Identification Number. For most medical centers, the PT ID will be the social security number of the patient and the SHORT ID will be the last four digits of the patient's social security number. For those sites with DOD sharing agreements using VA/DOD software developed by the Dallas CIOFO, the PT ID will be determined by the ID number given that patient by the military.

For most sites, each eligibility simply needs to be associated with the VA STANDARD format. This association was first accomplished during the post-init of MAS V. 5.0.

Other than The Primary Eligibility ID Reset (All Patients) option, the remaining six options would only be used by DOD sites using VA/DOD software developed by the Dallas CIOFO. They should not be run without Central Office and/or DOD approval/direction. Please contact your local CIOFO for guidance if you feel your site needs to utilize these options.

Below is a brief description of each option and its utilization:

PRIMARY ELIGIBILITY ID RESET (ALL PATIENTS) - This option will set/reset the IDs associated with each patient's primary eligibility code. This utility will be called when first installing the new eligibility data structure. It will run automatically as part of the PIMS clean-up routine process.

The option can be executed multiple times with no harmful effects. It should be run during non-peak hours, preferably over a weekend. A MailMan message will be sent to the user when the job is completed showing the start and completion date/time.

ELIGIBILITY CODE ENTER/EDIT - This option allows the user to enter/edit eligibility codes used by the site. It should be run for all ELIGIBILITY file entries to associate each entry with an MAS Eligibility code and an Identification Format.

Example: ELIGIBILITY CODE ENTER/EDIT option (user responses are shown in boldface type).

Select ELIGIBILITY CODE NAME: MARINE CORPS

ARE YOU ADDING 'MARINE CORPS' AS A NEW ELIGIBILITY CODE (THE 5TH)? YES

ELIGIBILITY CODE MAS ELIGIBILITY CODE: OTHER FEDERAL AGENCY 4

NAME: MARINE CORPS// \<RET\>

ABBREVIATION: MC

PRINT NAME: MARINE CORPS (Enter abbreviated Eligibility Code name for

output in limited space)

INACTIVE: \<RET\> (Null response for active; 1 - YES for inactive)

MAS ELIGIBILITY CODE: OTHER FEDERAL AGENCY// \<RET\>

ID FORMAT: DOD

AGENCY: ARMY Select SYNONYM: \<RET\>

ID FORMAT ENTER/EDIT - This option allows the user to enter/edit Identification formats with description.

RESET ALL IDS FOR A PATIENT - This option is used to reset the corresponding IDs for all eligibilities for a single patient. The patient's eligibilities will be listed as the ID is reset. This utility would be used if, for some reason, a patient's ID got corrupted.

RESET ALL IDS FOR ALL PATIENTS - This option resets all IDs corresponding to each of the patient's eligibilities. The option should be executed during non-peak hours. When the job is completed, a MailMan message will be generated to the user showing the start and completion date/time.

SPECIFIC ELIGIBILITY ID RESET (ALL PATIENTS) - After prompting for an eligibility code and queue-to-run time, this option will update the IDs for all patients having the selected eligibility. This utility would allow a site to update their database with the new value if the ID FORMAT field in the ELIGIBILITY CODE file changed.

The option should be run during off hours. When the job is completed, a MailMan message will be generated to the user showing the start and completion date/time.

SPECIFIC ID FORMAT RESET - This option prompts for an ID format; then, all patients that have eligibility codes associated with that ID format will have their IDs reset. The utility allows sites to update their database if the DEFAULT LONG ID VALUE CODE field in the IDENTIFICATION FORMAT file was modified. This option should be executed during off hours. When the job is completed, a MailMan message will be sent to the user showing the start and completion date/time.

## Station Number (Time Sensitive) Enter/Edit (D ^VASITE0)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The STATION NUMBER (TIME SENSITIVE) file (#389.9) is used to hold the time sensitive station number data. This file was initially populated by the post init routine for MAS V. 5.2. One entry was created for each medical center division with an effective date of Jan 1, 1980. It is not necessary to modify this data unless the station number for a division changes or a new division is added.

Entering a new medical center division name through the Supervisor ADT Menu of the ADT module of PIMS will automatically create a new entry in this file. New divisions may not be added through this routine entry point.

The Station Number (Time Sensitive) Enter/Edit routine entry point is used to change an existing station number or enter a new station number for a new division. If you are changing a station number for a division, you should enter a new effective date and the new station number for that division.

Once a new division has been added, you should select the new division and enter the effective date and new station number. The IS PRIMARY DIVISION field should be set to YES for the division where the station number has no suffix. Only one division may be primary at any given time.

## New SD Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New SD parameters were exported by patch SD\*5.3\*588 - High Risk Mental Health Proactive Report, and added to the following files:

| NEW SD PARAMETERS                                                                                                                                                                        | FILES                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| SD MH PROACTIVE DAYS PARAMETERS - Stores the number of days to list future appointments for the High Risk MH Proactive Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\].                     | PARAMETER file (#8989.5)             |
| SD MH NO SHOW DAYS PARAMETERS- Stores the number of days to list future appointments for the High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\].                          | PARAMETER file (#8989.5)             |
| SD MH PROACTIVE DAYS PARAMETER - The default value for is 30. This value can be changed, within the range of 1 to 30, by using the Edit Parameter Values \[XPAR EDIT PARAMETER\] option. | PARAMETER DEFINITION file (#8989.51) |
| SD MH NO SHOW DAYS PARAMETER - The default value for is 30. This value can be changed, within the range of 1 to 30, by using the Edit Parameter Values \[XPAR EDIT PARAMETER\] option.   | PARAMETER DEFINITION file (#8989.51) |

## PRF NATIONAL FLAG file (#26.15)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new national flag data entry (HIGH RISK FOR SUICIDE) is placed in the PRF NATIONAL FLAG file (#26.15) by the DG\*5.3\*849 DGPF NEW CAT1 FLAG AND CONVERSION patch:

| FILE NUMBER | FILE NAME     | NEW DATA ENTRY    |
|-----------------|-------------------|-----------------------|
| 26.15           | PRF NATIONAL FLAG | HIGH RISK FOR SUICIDE |

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a list of routines or instruct the user how/where to find this information online:

## Routines To Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routine mapping is not required with VMS/Cache systems.

## Callable Routines 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \$\$GETACT^DGPFAPI                                                      | Obtain active Patient Record Flag assignments            |
|-------------------------------------------------------------------------|----------------------------------------------------------|
| \$\$INSTPCTM^SCAPMC                                                     | Institution & team for pt's pc team                      |
| \$\$PRCL^SCAPMC                                                         | Practitioners for a Clinic                               |
| \$\$PRPT^SCAPMC                                                         | Practitioners for a Patient                              |
| \$\$PRTM^SCAPMC                                                         | Practitioners for a Team                                 |
| \$\$PTTM^SCAPMC                                                         | Patients for a Team                                      |
| \$\$SITE^VASITE                                                         | Obtain Station Number Information                        |
| \$\$TMPT^SCAPMC                                                         | Teams for a Patient                                      |
| DGINPW                                                                  | Obtain Inpatient Status                                  |
| DGPMLOS                                                                 | Obtain Length of Stay by Admission                       |
| \$\$GETALL^SCAPMCA                                                      | Return assignment information                            |
| \$\$OUTPTAP^SDUTL3                                                      | Return associate pc provider information                 |
| \$\$OUTPTRP^SDUTL3                                                      | Return primary care provider information                 |
| \$\$DATA2PTF^DGAPI                                                      | Send data to PTF                                         |
| CPTINFO^DGAPI                                                           | Get CPTs from PTF                                        |
| PTFINFOR^DGAPI                                                          | Delete CPTs from PTF                                     |
| \$\$DELCPT^DGAPI                                                        | Get Prof Serv Dates from PTF                             |
| \$\$DELPOV^DGAPI                                                        | Delete POVs from PTF                                     |
| ICDINFO^DGAPI                                                           | <span id="ICDp9" class="anchor"></span>Get ICDs from PTF |
| \$\$SDAPI^SDAMA301                                                      | Get Appointments                                         |
| GETAPPT^SDAMA201                                                        | Get Appointments for a Patient                           |
| NEXTAPPT^SDAMA201                                                       | Get Next Appointment (1 Appointment) for a Patient       |
| GETPLIST^SDAMA202                                                       | Get Appointments for a Clinic                            |
| \$\$PATAPPT^SDAMA204                                                    | Does Patient Have Any Appointments?                      |
| \$\$SDIMO^SDAMA203                                                      | Scheduling API for IMO                                   |
| SDOE                                                                    | ACRP Interface Toolkit                                   |
| SDQ                                                                     | ACRP Interface Toolkit                                   |
| SDUTL3                                                                  | Utility to enter and view primary care fields            |
| \$\$COMMANUM^VAFCADT2                                                   | Build a list of numbers separated by comma               |
| VACPT                                                                   | Display CPT Copyright Info                               |
| VADATE                                                                  | Generic Date Routine                                     |
| VADPT                                                                   | Obtain Patient Information                               |
| VALM                                                                    | List Manager                                             |
| BLDPID^VAFCQRY                                                          | Builds the PID HL7 segment                               |
| \$\$EVN^VAFHLEVN                                                        | Builds the EVN HL7 segment                               |
| \$\$EN^VAFHLPD1                                                         | Builds the PD1 HL7 segment                               |
| \$\$SITE^VASITE                                                         | Returns the institution and station numbers              |
| VAFMON                                                                  | Obtain Income or Dependent Information                   |
| VATRAN                                                                  | Establish VADATS Transmission Variables                  |
| VATREDIT                                                                | Enter/Edit TRANSMISSION ROUTERS File                     |
| VAUQWK                                                                  | Quick Lookup for Patient Data                            |
| VAUTOMA                                                                 | Generic One, Many, All Routine                           |
| See the Package-Wide Variables section of this manual for entry points. |                                                          |

## Compiled Template Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended you recompile the following templates at 4000 bytes.

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| FILE \# | TEMPLATE NAME              | ROUTINES |
|-------------|--------------------------------|--------------|
| 2           | DG CONSISTENCY CHECKER         | DGRPXC\*     |
|             | DG LOAD EDIT SCREEN 7          | DGRPXX7\*    |
|             | DGRP COLLATERAL REGISTER       | DGRPXCR\*    |
|             | SDM1                           | SDM1T\*      |
| 40.8        | DGTS                           | DGXTS        |
| 44          | SDB                            | SDBT\*       |
| 45          | DG PTF CREATE PTF ENTRY        | DGPTXC\*     |
|             | DG PTF POST CREATE             | DGPTXCA\*    |
|             | DG 101                         | DGPTX1\*     |
|             | DG 401                         | DGPTX4\*     |
|             | DG 501                         | DGPTX5\*     |
|             | DG 501F                        | DGPTX5F\*    |
|             | DG 701                         | DGPTX7\*     |
| 45.5        | DG PTF ADD MESSAGE             | DGPTXMS\*    |
| 46.1        | DG801                          | DGPTX8\*     |
| 405         | DGPM ADMIT                     | DGPMX1\*     |
|             | DGPM TRANSFER                  | DGPMX2\*     |
|             | DGPM DISCHARGE                 | DGPMX3\*     |
|             | DGPM CHECK-IN LODGER           | DGPMX4\*     |
|             | DGPM LODGER CHECK-OUT          | DGPMX5\*     |
|             | DGPM SPECIALTY TRANSFER        | DGPMX6\*     |
|             | DGPM ASIH ADMIT                | DGPMXA\*     |
| 408.21      | DGMT ENTER/EDIT ANNUAL INCOME  | DGMTXI       |
|             | DGMT ENTER/EDIT EXPENSES       | DGMTXE       |
|             | DGRP ENTER/EDIT ANNUAL         |              |
|             | INCOME                         | DGRPXIS      |
|             | DGRP ENTER/EDIT MON BENEFITS   | DGRPXMB      |
| 408.22      | DGMT ENTER/EDIT DEPENDENTS     | DGMTXD       |
|             | DGMT ENTER/EDIT MARITAL STATUS | DGMTXM       |
| 408.31      | DGMT ENTER/EDIT COMPLETION     | DGMTXC       |
| 409.5       | SDAMBT                         | SDXA\*       |
|             | SDXACSE                        | SDXACSE\*    |
| 409.68      | SD ENCOUNTER ENTRY             | SDAMXOE\*    |
|             | SD ENCOUNTER LOG               | SDAMXLG      |

### Print Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| FILE \# | TEMPLATE NAME    | ROUTINES |
|-------------|----------------------|--------------|
| 45          | DG PTF PT BRIEF LIST | DGPTXB\*     |
| 45.86       | DGPT QUICK PROFILE   | DGPTXCP\*    |
| 409.65      | SDAMVLD              | SDAMXLD      |

### Compiled Cross-Reference Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| FILE \# | TEMPLATE NAME        | ROUTINES |
|-------------|--------------------------|--------------|
| 45          | PTF                      | DGPTXX\*     |
| 405         | PATIENT MOVEMENT         | DGPMXX\*     |
| 408.21      | INDIVIDUAL ANNUAL INCOME | DGMTXX1\*    |
| 408.22      | INCOME RELATION          | DGMTXX2\*    |
| 408.31      | ANNUAL MEANS TEST        | DGMTXX3\*    |

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain a listing of the routines contained in the PIMS package.

1\. Programmer Options Menu

2\. Routine Tools Menu

3\. First Line Routine Print Option

4\. Routine Selector: DG\* (ADT) SD\* SC\* (Scheduling)

## New and Modified Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch SD\*5.3\*588 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new and modified routines were exported by patch SD\*5.3\*588 - HIGH RISK MENTAL HEALTH PROACTIVE REPORT. Not all routines can or should be used. Please refer to the outstanding Integration Agreement before attempting to use these routines:

| NEW SD ROUTINES | MODIFIED SD ROUTINES |
|---------------------|--------------------------|
| SDMHAP              | SDAMQ                    |
| SDMHAP1             | SDMHAD                   |
| SDMHPRO             | SDMHAD1                  |
| SDMHPRO1            | SDMHNS                   |
|                     | SDMHNS1                  |

## Patch DG\*5.3\*849 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These new DG routines were exported by patch DG\*5.3\*849 - DGPF NEW CAT1 FLAG AND CONVERSION. Not all routines can or should be used. Please refer to the outstanding Integration Agreement before attempting to use these routines:

| NEW DG ROUTINES | MODIFIED DG ROUTINES |
|---------------------|--------------------------|
| DG53849P            |                          |
| DGPFCNR             |                          |
| DGPFCNV             |                          |

## Patch SD\*5.3\*578 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SD\*5.3\*578 - These are the new and modified routines. Not all can or should be used. Please refer to the outstanding Integration Agreement before attempting to run these.

SDMHAD - This is the High Risk Mental Health AD Hoc No show Report entry point that the user can run to display the report. This report will display all patients that did not show up for their scheduled appointment for a Mental Health clinic. It will list patient contact information, Next of Kin, emergency contact, clinic default provider, future scheduled appointments and results of attempts to contact the no showed patients. The user is asked for various sort criteria , a date range, divisions to display (one, many, all), and sort by Clinic, Reminder Location or Stop Codes (one, many, all)

^SDMHAD1 - This is the print routine for the High Risk Mental Health AD HOC No Show Report. The report lists the patient that no showed for the mental health appointment, the date the of the appointment, the clinic and stop code. It also lists the contact information for the patient, the Next of Kin, emergency contacts, clinic provider, future scheduled appointments and results of efforts in contacting the patient.

^SDMHNS - This is the High Risk Mental Health No show Report entry point that is called by the scheduling background job. This report will display all patients that did not show up for their scheduled appointment for a Mental Health clinic. It will list patient contact information, Next of Kin, emergency contact, clinic default provider, future scheduled appointments and results of attempts to contact the no showed patients. The user will not be asked any sort criteria, the report will list for the day before the background job run, for all the divisions in the facility and mental health clinics in the facility. The report will be sent via email to those persons that are in the SD MH NO SHOW NOTIFICATION mail group.

^SDMHNS1 - This is the print routine for the High Risk Mental Health No Show Report run from the scheduling nightly background job. The report lists the patient that no showed for the mental health appointment, the date the of the appointment, the clinic and stop code. It also lists the contact information for the patient, the Next of Kin, emergency contacts, clinic provider, future scheduled appointments and results of efforts in contacting the patient. The report will be sent via email to those persons that are in the SD MH NO SHOW NOTIFICATION mail group.

SDAMQ modified

^SDAMQ G STARTQ:'\$\$SWITCH

- N SDSTART,SDFIN
- K ^TMP("SDSTATS",\$J)
- S SDSTART=\$\$NOW^SDAMU D ADD^SDAMQ1
- D EN^SDAMQ3(SDBEG,SDEND) ; appointments
- D EN^SDAMQ4(SDBEG,SDEND) ; add/edits
- D EN^SDAMQ5(SDBEG,SDEND) ; dispositions
- D EN^SDMHNS ;High Risk Mental Health NO Show report
- S SDFIN=\$\$NOW^SDAMU D UPD^SDAMQ1(SDBEG,SDEND,SDFIN,.05)
- D BULL^SDAMQ1

## Patch DG\*5.3\*836 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG\*5.3\*836 - This Registration Patient Record Flag patch provides new interfaces used by the Scheduling and Reminder patches to determine the High Risk for Suicide flag status on a specified date.

GETINF^DGPFAPIH - DGPFAPIH is both a Routine and API Integration agreement. DGPFAPIH - This routine implements the two Application Programming Interface call points for retrieving Patient Record Flag information. One call point is for a specific patient and record and the second call point is for a list of patients with a specific, active, Patient Record Flag.

This API will obtain the Patient Record Flag assignment information and status for the specified patient, patient record flag and date range. The return data will be provided in an array using the target_root specified by the user or in the default array variable DGPFAPI1. The DATE/TIME field (#.02) of the PRF ASSIGNMENT HISTORY File (#26.14) entry will determine whether the entry falls within the specified date range. If no date range is specified, all entries will be returned

GETLST^DGPFAPIH - This API will retrieve a list of patients active at some point within a specified date range for a specified Patient Record Flag. The date range is required for this API, though the same date can be entered to specify a single date. The return data will be provided in an array using the target root specified by the user or in the default array variable DGPFAPI2. The DATE/TIME field (#.02) of the PRF ASSIGNMENT HISTORY File (#26.14) entry will determine whether the entry falls within the specified date range.

BLDMAIN^DGPFAPIH - This API builds the main return array for the specified patient. The array contains the PRF assignment data retrieved from the appropriate Local or National assignment file

BLDHIST^DGPFAPIH - This API collects and builds the return array containing the PRF assignment history data.

ACTIVE^DGPFAPIU - DGPFAPIU - This routine provides support utilities and functions for the new Application Programming Interface calls.

This procedure will check if the Patient Record Flag was active at any point during the specified date range. The procedure accepts a date range parameter which specifies whether “A”ll dates or only a “S”pecified date range is to be checked.

The PRF Assignment History File (#26.14) was not designed for this type of date interaction so the algorithm in this procedure has to make a number of assumptions when interpreting the dates and PRF actions. While there can only be one “New Assignment” entry, it is possible to have multiple “Continue”, “Inactivate” and “Reactivate” action entries. In addition, the “Entered In Error” action can pose additional issues with determining a status during a specific date range.

CHKDATE^DGPFAPIU - Check for valid start and end dates. Set up the DGRANGE parameter with the validated dates and set DGRANGE top element to “A” for all dates, or “S” for a specific range of dates

CHKDFN^DGPFAPIU - This function checks for a valid patient by checking the DFN in the Patient File (#2). If a valid patient is found, the patient name is returned, otherwise, the error text from the DIQ call is returned.

ASGNDATE^DGPFAPIU - Get the initial Assignment Date/Time of the Patient Record Flag by looking for the “NEW ASSIGNMENT” action in the PRF ASSIGNMENT HISTORY File (#26.14).

GETFLAG^DGPFAPIU - This function gets the variable pointer value for the Patient Record Flag passed in. The PRF is passed in as a text value. If the optional flag category is passed in, only that category will be checked for the PRF. If no category is passed in, then first the National category will be checked,

This Page Left Blank Intentionally

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a list of the software files. For each file, include the file number, file name, a list of any special templates (print, sort, input, edit) that come with the file, and brief description of the data or instruct the user how/where to find this information online. Indicate what data comes with the files and whether or not that data overwrites existing data. Optionally include information about file pointer relationships.

## Globals and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main globals used in the PIMS package are ^DG, ^DPT, ^DGPM, ^SC, and ^SCE.

The main files are PATIENT, PATIENT MOVEMENT, MAS MOVEMENT TYPE, PTF, CENSUS, WARD LOCATION, and HOSPITAL LOCATION.

The PIMS Package also uses globals ^DGSL, ^DGIN, ^DGS, ^DGAM, ^DGCPT, ^DGICD9, ^DGWAIT, ^DGPR, ^DGMT, ^DGPT, ^DGM, ^DGNT, ^DGP, ^DGPF, ^DGQE, ^ICPT, ^VA, ^VAS, ^VAT, ^DIC, ^SCPT, ^SCTM, ^SDASF, ^SDASE, ^SDV, ^SD, ^SDD.

Journaling of the following globals is mandatory: ^DPT, ^DGEN, ^DGPT, ^DGPM, ^SDV, ^SC, ^SCE, ^SCTM, ^SDD.

Journaling of the following globals is optional: ^DGS, ^DG.

Journaling of the following global is recommended: ^DGPF.

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| FILE NUMBER | FILE NAME          | GLOBAL   |
|-----------------|------------------------|--------------|
| 2               | PATIENT                | ^DPT(        |
| 5               | STATE                  | ^DIC(5,      |
| 8               | ELIGIBILITY CODE       | ^DIC(8,      |
| 8.1\*\*         | MAS ELIGIBILITY CODE   | ^DIC(8.1,    |
| 8.2\*           | IDENTIFICATION FORMAT  | ^DIC(8.2,    |
| 10\*            | RACE                   | ^DIC(10,     |
| 11\*\*          | MARITAL STATUS         | ^DIC(11,     |
| 13\*            | RELIGION               | ^DIC(13,     |
| 21\*\*          | PERIOD OF SERVICE      | ^DIC(21,     |
| 22\*\*          | POW PERIOD             | ^DIC(22,     |
| 23\*            | BRANCH OF SERVICE      | ^DIC(23,     |
| 25\*            | TYPE OF DISCHARGE      | ^DIC(25,     |
| 26.11           | PRF LOCAL FLAG         | ^DGPF(26.11, |
| 26.12           | PRF LOCAL FLAG HISTORY | ^DGPF(26.12, |

| FILE NUMBER | FILE NAME                         | GLOBAL    |
|-----------------|---------------------------------------|---------------|
| 26.13           | PRF ASSIGNMENT                        | ^DGPF(26.13,  |
| 26.14           | PRF ASSIGNMENT HISTORY                | ^DGPF(26.14,  |
| 26.15           | PRF NATIONAL FLAG                     | ^DGPF(26.15,  |
| 26.16           | PRF TYPE                              | ^DGPF(26.16,  |
| 26.17           | PRF HL7 TRANSMISSION LOG              | ^DGPF(26.17,  |
| 26.18           | PRF PARAMETERS                        | ^DGPF(26.18,  |
| 26.19           | PRF HL7 QUERY LOG                     | ^DGPF(26.19,  |
| 26.21           | PRF HL7 EVENT                         | ^DGPF(26.21,  |
| 27.11           | PATIENT ENROLLMENT                    | ^DGEN(27.11,  |
| 27.12           | ENROLLMENT QUERY                      | ^DGEN(27.12,  |
| 27.14           | ENROLLMENT / ELIGIBILITY UPLOAD AUDIT | ^DGENA(27.14, |
| 27.15           | ENROLLMENT STATUS                     | ^DGEN(27.15,  |
| 27.16           | ENROLLMENT GROUP THRESHOLD            | ^DGEN(27.16,  |
| 27.17\*         | CATASTROPHIC DISABILITY REASONS       | ^DGEN(27.17,  |
| 28.11           | NOSE AND THROAT RADIUM HISTORY        | ^DGNT(28.11,  |
| 29.11           | MST HISTORY                           | ^DGMS(29.11,  |
| 30\*\*          | DISPOSITION LATE REASON               | ^DIC(30,      |
| 35\*            | OTHER FEDERAL AGENCY                  | ^DIC(35,      |
| 35.1            | SHARING AGREEMENT CATEGORY            | ^DG(35.1,     |
| 35.2            | SHARING AGREEMENT SUB-CATEGORY        | ^DG(35.2)     |
| 37\*\*          | DISPOSITION                           | ^DIC(37,      |
| 38.1            | DG SECURITY LOG                       | ^DGSL(38.1,   |

| FILE NUMBER | FILE NAME              | GLOBAL  |
|-----------------|----------------------------|-------------|
| 38.5            | INCONSISTENT DATA          | ^DGIN(38.5, |
| 38.6\*\*        | INCONSISTENT DATA ELEMENTS | ^DGIN(38.6, |
| 39.1\*          | EMBOSSED CARD TYPE         | ^DIC(39.1,  |
| 39.2\*          | EMBOSSING DATA             | ^DIC(39.2,  |
| 39.3            | EMBOSSER EQUIPMENT FILE    | ^DIC(39.3,  |
| 39.4            | ADT / HL7 TRANSMISSION     | ^DIC(39.4,  |
| 39.6            | VIC REQUEST                | ^DGQE(39.6, |
| 39.7            | VIC HL7 TRANSMISSION LOG   | ^DGQE(39.7, |
| 40.7\*          | CLINIC STOP                | ^DIC(40.7,  |
| 40.8            | MEDICAL CENTER DIVISION    | ^DG(40.8,   |
| 40.9\*\*        | LOCATION TYPE              | ^DIC(40.9   |
| 41.1            | SCHEDULED ADMISSION        | ^DGS(41.1,  |
| 41.41           | PRE-REGISTRATION AUDIT     | ^DGS(41.41, |
| 41.42           | PRE-REGISTRATION CALL LIST | ^DGS(41.42, |
| 41.43           | PRE-REGISTRATION CALL LOG  | ^DGS(41.43, |
| 41.9            | CENSUS                     | ^DG(41.9,   |
| 42              | WARD LOCATION              | ^DIC(42,    |
| 42.4\*          | SPECIALTY                  | ^DIC(42.4,  |
| 42.5            | WAIT LIST                  | ^DGWAIT(    |
| 42.55\*\*       | PRIORITY GROUPING          | ^DIC(42.55, |
| 42.6            | AMIS 334-341               | ^DGAM(334,  |
| 42.7            | AMIS 345&346               | ^DGAM(345,  |

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 46%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><br />
FILE NUMBER</strong></th>
<th><strong>FILE NAME</strong></th>
<th><strong>GLOBAL</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>43</td>
<td>MAS PARAMETERS</td>
<td>^DG(43,</td>
</tr>
<tr class="even">
<td>43.1</td>
<td>MAS EVENT RATES</td>
<td>^DG(43.1,</td>
</tr>
<tr class="odd">
<td>43.11</td>
<td>MAS AWARD</td>
<td>^DG(43.11,</td>
</tr>
<tr class="even">
<td>43.4</td>
<td>VA ADMITTING REGULATION</td>
<td>^DIC(43.4,</td>
</tr>
<tr class="odd">
<td>43.5</td>
<td>G&amp;L CORRECTIONS</td>
<td>^DGS(43.5,</td>
</tr>
<tr class="even">
<td>43.61</td>
<td>G&amp;L TYPE OF CHANGE</td>
<td>^DG(43.61,</td>
</tr>
<tr class="odd">
<td>43.7</td>
<td>ADT TEMPLATE</td>
<td>^DG(43.7,</td>
</tr>
<tr class="even">
<td>44</td>
<td>HOSPITAL LOCATION</td>
<td>^SC(</td>
</tr>
<tr class="odd">
<td>45</td>
<td>PTF</td>
<td>^DGPT(</td>
</tr>
<tr class="even">
<td>45.1</td>
<td>SOURCE OF ADMISSION</td>
<td>^DIC(45.1,</td>
</tr>
<tr class="odd">
<td>45.2</td>
<td>PTF TRANSFERRING FACILITY</td>
<td>^DGTF(</td>
</tr>
<tr class="even">
<td>45.3*</td>
<td>SURGICAL SPECIALTY</td>
<td>^DIC(45.3,</td>
</tr>
<tr class="odd">
<td>45.4*</td>
<td>PTF DIALYSIS TYPE</td>
<td>^DG(45.4,</td>
</tr>
<tr class="even">
<td>45.5</td>
<td>PTF MESSAGE</td>
<td>^DGM(</td>
</tr>
<tr class="odd">
<td>45.6*</td>
<td>PLACE OF DISPOSITION</td>
<td>^DIC(45.6,</td>
</tr>
<tr class="even">
<td>45.61*</td>
<td>PTF ABUSED SUBSTANCE</td>
<td>^DIC(45.61,</td>
</tr>
<tr class="odd">
<td>45.64*</td>
<td>PTF AUSTIN ERROR CODES</td>
<td>^DGP(45.64,</td>
</tr>
<tr class="even">
<td>45.68</td>
<td>FACILITY SUFFIX</td>
<td>^DIC(45.68,</td>
</tr>
<tr class="odd">
<td>45.7</td>
<td>FACILITY TREATING SPECIALTY</td>
<td>^DIC(45.7,</td>
</tr>
<tr class="even">
<td>45.81*</td>
<td>STATION TYPE</td>
<td>^DIC(45.81,</td>
</tr>
<tr class="odd">
<td>45.82*</td>
<td>CATEGORY OF BENEFICIARY</td>
<td>^DIC(45.82,</td>
</tr>
<tr class="even">
<td>45.83</td>
<td>PTF RELEASE</td>
<td>^DGP(45.83,</td>
</tr>
</tbody>
</table>

| FILE NUMBER | FILE NAME                            | GLOBAL    |
|-----------------|------------------------------------------|---------------|
| 45.84           | PTF CLOSE OUT                            | ^DGP(45.84,   |
| 45.85           | CENSUS WORKFILE                          | ^DG(45.85,    |
| 45.86\*         | PTF CENSUS DATE                          | ^DG(45.86,    |
| 45.87           | PTF TRANSACTION REQUEST LOG              | ^DGP(45.87,   |
| 45.88\*         | PTF EXPANDED CODE CATEGORY               | ^DIC(45.88,   |
| 45.89\*         | PTF EXPANDED CODE                        | ^DIC(45.89,   |
| 45.9            | PAF                                      | ^DG(45.9,     |
| 45.91           | RUG-II                                   | ^DG(45.91,    |
| 46              | INPATIENT CPT CODE                       | ^DGCPT(46     |
| 46.1            | INPATIENT POV                            | ^DGICT9(46.1, |
| 47\*\*          | MAS FORMS AND SCREENS                    | ^DIC(47,      |
| 48\*\*          | MAS RELEASE NOTES                        | ^DG(48,       |
| 48.5\*\*        | MAS MODULE                               | ^DG(48.5,     |
| 389.9           | STATION NUMBER (TIME SENSITIVE)          | ^VA(389.9,    |
| 390             | ENROLLMENT RATED DISABILITY UPLOAD AUDIT | ^DGRDUA(390,  |
| 391\*\*         | TYPE OF PATIENT                          | ^DG(391,      |
| 391.1           | AMIS SEGMENT                             | ^DG(391.1,    |
| 391.31          | HOME TELEHEALTH PATIENT                  | ^DGHT(391.31, |
| 403.35          | SCHEDULING USER PREFERENCE               | ^SCRS(403.35, |
| 403.43\*        | SCHEDULING EVENT                         | ^SD(403.43,   |
| 403.44\*        | SCHEDULING REASON                        | ^SD(403.44,   |
| 403.46\*        | STANDARD POSITION                        | ^SD(403.46,   |

| FILE NUMBER | FILE NAME                       | GLOBAL     |
|-----------------|-------------------------------------|----------------|
| 403.47\*        | TEAM PURPOSE                        | ^SD(403.47,    |
| 404.41          | OUTPATIENT PROFILE                  | ^SCPT(404.41,  |
| 404.42          | PATIENT TEAM ASSIGNMENT             | ^SCPT(404.42,  |
| 404.43          | PATIENT TEAM POSITION ASSIGNMENT    | ^SCPT(404.43,  |
| 404.44          | PCMM PARAMETER                      | ^SCTM(404.44,  |
| 404.45          | PCMM SERVER PATCH                   | ^SCTM(404.45,  |
| 404.46          | PCMM CLIENT PATCH                   | ^SCTM(404.46,  |
| 404.471         | PCMM HL7 TRANSMISSION LOG           | ^SCPT(404.471, |
| 404.472         | PCMM HL7 ERROR LOG                  | ^SCPT(404.472, |
| 404.48          | PCMM HL7 EVENT                      | ^SCPT(404.48,  |
| 404.49          | PCMM HL7 ID                         | ^SCPT(404.49,  |
| 404.51          | TEAM                                | ^SCTM(404.51,  |
| 404.52          | POSITION ASSIGNMENT HISTORY         | ^SCTM(404.52,  |
| 404.53          | PRECEPTOR ASSIGNMENT HISTORY        | ^SCTM(404.53,  |
| 404.56          | TEAM AUTOLINK                       | ^SCTM(404.56,  |
| 404.57          | TEAM POSITION                       | ^SCTM(404.57,  |
| 404.58          | TEAM HISTORY                        | ^SCTM(404.58,  |
| 404.59          | TEAM POSITION HISTORY               | ^SCTM(404.59,  |
| 404.61          | MH PCMM STOP CODES                  | ^SCTM(404.61,  |
| 404.91          | SCHEDULING PARAMETER                | ^SD(404.91,    |
| 404.92\*        | SCHEDULING REPORT DEFINTION         | ^SD(404.92,    |
| 404.93\*        | SCHEDULING REPORT FIELDS DEFINITION | ^SD(404.93,    |

| FILE NUMBER | FILE NAME                       | GLOBAL    |
|-----------------|-------------------------------------|---------------|
| 404.94\*        | SCHEDULING REPORT GROUP             | ^SD(404.94,   |
| 404.95\*        | SCHEDULING REPORT QUERY TEMPLATE    | ^SD(404.95,   |
| 404.98          | SCHEDULING CONVERSION SPECIFICATION | ^SD(404.98,   |
| 405             | PATIENT MOVEMENT                    | ^DGPM(        |
| 405.1           | FACILITY MOVEMENT TYPE              | ^DG(405.1,    |
| 405.2\*\*       | MAS MOVEMENT TYPE                   | ^DG(405.2,    |
| 405.3\*\*       | MAS MOVEMENT TRANSACTION TYPE       | ^DG(405.3,    |
| 405.4           | ROOM-BED                            | ^DG(405.4,    |
| 405.5\*\*       | MAS OUT-OF-SERVICE                  | ^DG(405.5,    |
| 405.6           | ROOM-BED DESCRIPTION                | ^DG(405.6,    |
| 406.41\*\*      | LODGING REASON                      | ^DG(406.41,   |
| 407.5           | LETTER                              | ^VA(407.5,    |
| 407.6\*\*       | LETTER TYPE                         | ^VA(407.6,    |
| 407.7\*\*       | TRANSMISSION ROUTERS                | ^VAT(407.7,   |
| 408             | DISCRETIONARY WORKLOAD              | ^VAT(408,     |
| 408.11\*        | RELATIONSHIP                        | ^DG(408.11,   |
| 408.12          | PATIENT RELATION                    | ^DGPR(408.12, |
| 408.13          | INCOME PERSON                       | ^DGPR(408.13, |
| 408.21          | INDIVIDUAL ANNUAL INCOME            | ^DGMT(408.21, |
| 408.22          | INCOME RELATION                     | ^DGMT(408.22, |
| 408.31          | ANNUAL MEANS TEST                   | ^DGMT(408.31, |

| FILE NUMBER     | FILE NAME                          | GLOBAL   |
|---------------------|----------------------------------------|--------------|
| 408.32\*\*          | MEANS TEST STATUS                      | ^DG(408.32,  |
| 408.33\*\*          | TYPE OF TEST                           | ^DG(408.33,  |
| 408.34\*\*          | SOURCE OF INCOME TEST                  | ^DG(408.34,  |
| 408.41              | MEANS TEST CHANGES                     | ^DG(408.41,  |
| 408.42\*\*          | MEANS TEST CHANGES TYPE                | ^DG(408.42,  |
| 409.1\*\*           | APPOINTMENT TYPE                       | ^SD(409.1,   |
| 409.2\*\*           | CANCELLATION REASONS                   | ^SD(409.2,   |
| 409.41\*\*          | OUTPATIENT CLASSIFICATION TYPE         | ^SD(409.41,  |
| 409.42              | OUTPATIENT CLASSIFICATION              | ^SDD(409.42, |
| 409.45\*\*          | OUTPATIENT CLASSIFICATION              | ^SD(409.45,  |
| STOP CODE EXCEPTION |                                        |              |
| 409.62\*\*          | APPOINTMENT GROUP                      | ^SD(409.62,  |
| 409.63\*\*          | APPOINTMENT STATUS                     | ^SD(409.63,  |
| 409.64              | QUERY OBJECT                           | ^SD(409.64,  |
| 409.65              | APPOINTMENT STATUS UPDATE LOG          | ^SDD(409.65, |
| 409.66\*\*          | APPOINTMENT TRANSACTION TYPE           | ^SD(409.66   |
| 409.67              | CLINIC GROUP                           | ^SD(409.67,  |
| 409.68              | OUTPATIENT ENCOUNTER                   | ^SCE(        |
| 409.73              | TRANSMITTED OUTPATIENT ENCOUNTER       | ^SD(409.73,  |
| 409.74              | DELETED OUTPATIENT ENCOUNTER           | ^SD(409.74,  |
| 409.75              | TRANSMITTED OUTPATIENT ENCOUNTER ERROR | ^SD(409.75,  |
| 409.76\*\*          | TRANSMITTED OUTPATIENT ENCOUNTER       | ^SD(409.76,  |

| FILE NUMBER | FILE NAME                  | GLOBAL   |
|-----------------|--------------------------------|--------------|
| ERROR CODE      |                                |              |
| 409.77          | ACRP TRANSMISSION HISTORY      | ^SD(409.77,  |
| 409.91          | ACRP REPORT TEMPLATE           | ^SDD(409.91, |
| 409.92          | ACRP REPORT TEMPLATE PARAMETER | ^SD(409.92,  |

\*File comes with data\*\* File comes with data which will overwrite existing data, if specified.

# Files and Templates in the PIMS Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain information concerning the files and templates contained in the PIMS package.

## File Flow (Relationships between files)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan Menu

2\. Data Dictionary Utilities Menu

3\. List File Attributes Option

4\. Enter File \# or range of File \#s

5\. Select Listing Format: Standard

6\. You will see what files point to the selected file. To see what files the selected file points to, look for fields that say “POINTER TO”.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File:

- Print Template
- Sort Template
- Input Template
- List Template

4\. Sort by: Name

5\. Start with name: DG to DGZ, VA to VAZ, (ADT) SD to SDZ, SC to SCZ (scheduling)

6\. Within name, sort by: \<RET\>

7\. First print field: Name

## VA FileMan Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Included with the ACRP Reports Menu is the FileMan function, SCRPWDATA. This function can be used from within the OUTPATIENT ENCOUNTER file to provide any of the following data elements as data within FileMan output. It may be used to sort or print data.

This function has one argument which is the name (or acronym) of the data element you wish to return. For example, if you wish to sort or print a patient's current GAF score, the function could be used as follows.

THEN PRINT FIELD: SCRPWDATA("GAF SCORE (CURRENT)");"CURRENT GAF SCORE";L8

(OR)

THEN PRINT FIELD: SCRPWDATA("DXGC");"CURRENT GAF SCORE";L8

VA FileMan Function Data elements that have multiple values (like procedure codes, diagnoses, etc.) are returned as a single semicolon delimited string which may be as long as 245 characters. Some data of these elements may be omitted due to truncation to stay within this limit.

The following is a list of data elements and associated acronyms that may be specified as arguments to the SCRPWDATA function.

| VA FILEMAN FUNCTIONS            |             |
|-------------------------------------|-------------|
| DATA ELEMENT                    | ACRONYM |
| CATEGORY: AMBULATORY PROCEDURE      |             |
| EVALUATION & MANAGEMENT CODES       | APEM        |
| AMBULATORY PROCEDURE (NO E&M CODES) | APAP        |
| ALL AMBULATORY PROCEDURE CODES      | APAC        |
| CATEGORY: CLINIC                    |             |
| CLINIC NAME                         | CLCN        |
| CLINIC GROUP                        | CLCG        |
| CLINIC SERVICE                      | CLCS        |
| CATEGORY: DIAGNOSIS                 |             |
| PRIMARY DIAGNOSIS                   | DXPD        |
| SECONDARY DIAGNOSIS                 | DXSD        |
| ALL DIAGNOSES                       | DXAD        |
| GAF SCORE (HISTORICAL)              | DXGH        |
| GAF SCORE (CURRENT)                 | DXGC        |

| VA FILEMAN FUNCTIONS               |             |
|----------------------------------------|-------------|
| DATA ELEMENT                       | ACRONYM |
| CATEGORY: ENROLLMENT (CURRENT)         |             |
| ENROLLMENT DATE (CURRENT)              | ECED        |
| SOURCE OF ENROLLMENT (CURRENT)         | ECSE        |
| ENROLLMENT STATUS (CURRENT)            | ECES        |
| ENROLLMENT FACILITY RECEIVED (CURRENT) | ECFR        |
| ENROLLMENT PRIORITY (CURRENT)          | ECEP        |
| ENROLLMENT EFFECTIVE DATE (CURRENT)    | ECEF        |

| VA FILEMAN FUNCTIONS                  |             |
|-------------------------------------------|-------------|
| DATA ELEMENT                          | ACRONYM |
| CATEGORY: ENROLLMENT (HISTORICAL)         |             |
| ENROLLMENT DATE (HISTORICAL)              | EHED        |
| SOURCE OF ENROLLMENT (HISTORICAL)         | EHSE        |
| ENROLLMENT STATUS (HISTORICAL)            | EHES        |
| ENROLLMENT FACILITY RECEIVED (HISTORICAL) | EHFR        |
| ENROLLMENT PRIORITY (HISTORICAL)          | EHEP        |
| ENROLLMENT EFFECTIVE DATE (HISTORICAL)    | EHEF        |

| VA FILEMAN FUNCTIONS        |             |
|---------------------------------|-------------|
| DATA ELEMENT                | ACRONYM |
| CATEGORY: OUTPATIENT ENCOUNTER  |             |
| PATIENT                         | OEPA        |
| ORIGINATING PROCESS TYPE        | OEOP        |
| APPT. TYPE                      | OEAT        |
| STATUS                          | OEST        |
| ELIG. OF ENCOUNTER              | PEPW        |
| MEANS TEST (HISTORICAL)         | PEMH        |
| MEANS TEST (CURRENT)            | PEMC        |
| SC PERCENTAGE                   | PESP        |
| AGENT ORANGE EXPOSURE           | PEAO        |
| IONIZING RADIATION EXPOSURE     | PEIR        |
| SW ASIA CONDITIONS EXPOSURE     | PEEC        |
| CATEGORY: PRIMARY CARE      |             |
| PC PROVIDER (HISTORICAL)        | PCPH        |
| PC TEAM (HISTORICAL)            | PCTH        |
| PC PROVIDER (CURRENT)           | PCPC        |
| PC TEAM (CURRENT)               | PCTC        |
| CATEGORY: PROVIDER          |             |
| PRIMARY PROVIDER                | PRPP        |
| SECONDARY PROVIDER              | PRSP        |
| ALL PROVIDERS                   | PRAP        |
| PRIMARY PROVIDER PERSON CLASS   | PRPC        |
| SECONDARY PROVIDER PERSON CLASS | PRSC        |
| ALL PROVIDERS PERSON CLASS      | PRAC        |

| VA FILEMAN FUNCTIONS     |             |
|------------------------------|-------------|
| DATA ELEMENT             | ACRONYM |
| CATEGORY: STOP CODE      |             |
| PRIMARY STOP CODE            | SCPC        |
| SECONDARY STOP CODE          | SCSC        |
| BOTH STOP CODES              | SCBC        |
| CREDIT PAIR                  | SCCP        |
| CATEGORY: V FILE ELEMENT |             |
| EXAMINATION                  | VFEX        |
| HEALTH FACTOR                | VFHF        |
| IMMUNIZATION                 | VFIM        |
| PATIENT EDUCATION            | VFPE        |
| TREATMENTS                   | VFTR        |
| SKIN TEST                    | VFST        |

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a list of the options exported with the software, indicating distribution of menus to users. Any restrictions on menu distribution are noted. When the option’s availability is based on the level of system access requiring permissions the name of the type of access (e.g., security keys and/or roles) and authorization is included.

The following are the steps you may take to obtain information about menus, exported protocols, exported options, exported remote procedures, and exported HL7 applications concerning the PIMS package.

## Menu Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Programmers Options
- Menu Management Menu
- Display Menus and Options Menu
- Diagram Menus
- Select User or Option Name: O.DG Manager Menu (ADT) O.SDMGR (Scheduling)

## Exported Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VA FileMan Menu
- Print File Entries Option
- Output from what File: PROTOCOL
- Sort by: Name
- Start with name: DG to DGZ, VA to VAZ (ADT) SD to SDZ, SC to SCZ (Scheduling)
- Within name, sort by: \<RET\>
- First print field: Name

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VA FileMan Menu
- Print File Entries Option
- Output from what File: OPTION
- Sort by: Name
- Start with name: DG to DGZ, VA to VAZ (ADT)
- SD to SDZ, SC to SCZ (Scheduling)
- Within name, sort by: \<RET\>
- First print field: Name

## Exported Remote Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VA FileMan Menu
- Print File Entries Option
- Output from what File: REMOTE PROCEDURE
- Sort by: Name
- Start with name: DG to DGZ, VA to VAZ (ADT) SD to SDZ, SC to SCZ (Scheduling)
- Within name, sort by: \<RET\>
- First print field: Name

## Exported HL7 Applications for Ambulatory Care Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HL7 Main Menu
- V1.6 Options Menu
- Interface Workload Option
- Look for AMBCARE-DHCP and NPCD-AAC\*

## Exported HL7 Applications For Inpatient Reporting To National Patient Care Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HL7 Main Menu
- V1.6 Options Menu
- Interface Workload Option
- Look for VAFC PIMS and NPTF

## Exported HL7 Applications for Home Telehealth Care Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- DG HOME TELEHEALTH

\*AAC stands for Austin Automation Center. The name of that facility has been changed to Austin Information Technology Center.

## Exported Scheduling Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new and modified Scheduling options were exported by the SD\*5.3\*588 HIGH RISK MENTAL HEALTH PROACTIVE REPORT patch:

| NEW SCHEDULING OPTIONS                                                       | MENU ASSIGNMENTs |
|----------------------------------------------------------------------------------|----------------------|
| High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] Option     | Stand-Alone Option   |
| High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] Run Routine | Stand-Alone Option   |

| MODIFIED SCHEDULING OPTIONS                                               | MENU ASSIGNMENTs |
|-------------------------------------------------------------------------------|----------------------|
| High Risk MH No-Show Adhoc Report \[SD MH NO SHOW AD HOC REPORT\] option      | Stand-Alone Option   |
| High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] Run Routine | Stand-Alone Option   |

## Exported DG Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Convert Local HRMH PRF to National Action \[DGPF LOCAL TO NATIONAL CONVERT\] option is exported by the DG\*5.3\*849 DGPF NEW CAT1 FLAG AND CONVERSION patch:

| NEW DG OPTION                                                                   | MENU ASSIGNMENT |
|-------------------------------------------------------------------------------------|---------------------|
| Convert Local HRMH PRF to National Action \[DGPF LOCAL TO NATIONAL CONVERT\] option | Stand-Alone Option  |

This Page Left Blank Intentionally

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the archiving capabilities of the software and any necessary instructions or guidelines:

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the release of PIMS V. 5.3, a new archive / purge option has been created for PTF-related records. Please refer to the Release Notes for details.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PIMS package allows for purging of data associated with log of user access to sensitive records, consistency checker, scheduled admissions, local breakeven data for DRGs, special transaction requests, and scheduling data. Following is a list of the purge options and where the documentation may be found in the user manual.

## ADT Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ADT MODULE                                    |                           |
|---------------------------------------------------|---------------------------|
| OPTION NAME                                   | MENU NAME             |
| Purge Breakeven Data for a Fiscal Year            | PTF                       |
| Purge Special Transaction Request Log             | PTF                       |
| Purge Non-Sensitive Patients from Security Log    | Security Officer          |
| Purge Record of User Access from Security Log     | Security Officer          |
| Purge Inconsistent Data Elements                  | Supervisor ADT            |
| Purge Scheduled Admissions                        | Supervisor ADT            |
| SCHEDULING MODULE                             |                           |
| OPTION NAME                                   | MENU NAME             |
| Purge Ambulatory Care Reporting files             | Ambulatory Care Reporting |
| Purge Appointment Status Update Log File          | Supervisor                |
| Purge rejections that are past database close-out | Ambulatory Care Reporting |
| Purge Scheduling Data                             | Supervisor                |

## ACRP Database Conversion Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the database conversion is to convert old Scheduling encounter information into the Visit Tracking / Patient Care Encounter (PCE) database. Once you have converted all the data, you may wish to delete the old Scheduling files. A list of the files which may be deleted will be displayed when selecting the *Delete OldFiles* action in this option. It is recommended you back up these files before deletion.

## HL7 Purger

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that the option Purge Message Text File Entries \[HL PURGE TRANSMISSIONS\] be scheduled to run every day or every other day.

# Callable Routines/Entry Points/Application Program Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the callable routines, entry points, and Application Program Interfaces (APIs) that can be called by other software. Included is a brief description of the functions, required variables, and any restrictions.

### ^SDMHAD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the High Risk Mental Health AD Hoc No show Report entry point that the user can run to display the report. This report will display all patients that did not show up for their scheduled appointment for a Mental Health clinic. It will list patient contact information, Next of Kin, emergency contact, clinic default provider, future scheduled appointments, Mental Health Treatment Coordinator and care team and results of attempts to contact the no showed patients. The user is asked for various sort criteria , a date range, divisions to display (one, many, all), and sort by Clinic, Reminder Location or Stop Codes (one, many, all).

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th colspan="9"><strong>^SDMHAD</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enhancement Category</td>
<td colspan="2">New</td>
<td>Modify</td>
<td colspan="3">Delete</td>
<td colspan="3">No Change</td>
</tr>
<tr class="even">
<td>SRS Traceability</td>
<td colspan="9"></td>
</tr>
<tr class="odd">
<td>Related Options</td>
<td colspan="9">High Risk MH No-Show Adhoc Report [SD MH NO SHOW AD HOC REPORT] option</td>
</tr>
<tr class="even">
<td rowspan="2">Related Routines</td>
<td colspan="5">Routines “Called By”</td>
<td colspan="4">Routines “Called”</td>
</tr>
<tr class="odd">
<td colspan="5"><strong>^SDMHNS</strong></td>
<td colspan="4"><p><strong>NOW^%DTC $$GETINF^DGPFAPIH</strong></p>
<p><strong>CLOSE^DGUTQ WAIT^DICD</strong></p>
<p><strong>LOCLIST^PXRMLOCF</strong></p>
<p><strong>$$RANGE^SDAMQ</strong></p>
<p><strong>ASK2^SDDIV</strong></p>
<p><strong>^SDMHAD1</strong></p>
<p><strong>^SDMHNS1</strong></p>
<p><strong>^VADATE</strong></p>
<p><strong>PID^VADPT6</strong></p>
<p><strong>FIRST^VAUTOMA</strong></p>
<p><strong>PATIENT^VAUTOMA</strong></p></td>
</tr>
<tr class="even">
<td>Data Dictionary References</td>
<td colspan="9"><p><strong>^DG(40.8 DIVISION</strong></p>
<p><strong>^DIC(40.7 CLIONIC STOP</strong></p>
<p><strong>^DPT( PATIENT</strong></p>
<p><strong>^PXRMD(810.9 REMINDEDR LOCATION</strong></p>
<p><strong>^SC( HOSPITAL LICATION</strong></p>
<p><strong>^TMP(</strong></p>
<p><strong>^TMP($J</strong></p></td>
</tr>
<tr class="odd">
<td>Related Protocols</td>
<td colspan="9">N/A</td>
</tr>
<tr class="even">
<td>Related Integration Agreements</td>
<td colspan="9">TBD</td>
</tr>
<tr class="odd">
<td>Data Passing</td>
<td>Input</td>
<td colspan="3">Output Reference</td>
<td colspan="3">Both</td>
<td>Global Reference</td>
<td>Local</td>
</tr>
<tr class="even">
<td>Input Attribute Name and Definition</td>
<td colspan="9"><p>Name:</p>
<p>Definition:</p></td>
</tr>
<tr class="odd">
<td>Output Attribute Name and Definition</td>
<td colspan="9"><p>Name:</p>
<p>Definition:</p></td>
</tr>
<tr class="even">
<td colspan="10">Current Logic</td>
</tr>
<tr class="odd">
<td colspan="10"></td>
</tr>
<tr class="even">
<td colspan="10">Modified Logic (Changes are in bold)</td>
</tr>
<tr class="odd">
<td colspan="10"><p>User is asked to choose the date range.</p>
<p>User is asked to choose the Divisions in the facility ( one, many, `all)</p>
<p>User is asked to choose the sort criteria, by clinic, by Mental Health Clinic Quick List, by stop code ( one, many, all)</p>
<p>If the sort is by the by Mental Health Clinic Quick List (by one, or many) Check API (LOCKLIST^PXRMLOCF) to find the clinics that are associated with the reminder list(s) that were chosen.</p>
<ul>
<li><p>Check to see if the division/clinic/stop have been selected and if the clinic and stop code are a valid</p></li>
</ul>
<p>mental health pair.</p>
<p>-Set ^TMP(“SDNSHOW”,$J with the valid choices</p>
<p>Find the patients in the date range that had a no show, no show auto rebook or no action taken appointment for a mental health clinic</p>
<p>-Loop through the ^TMP(“SDNSHOW”,$J global</p>
<blockquote>
<p>Within that loop, check the Hospital Location “S” X-ref to see if the patient has an appointment</p>
<p>In the date range.. ^SC(clinic,”S”,date</p>
</blockquote>
<p>- If there is a match, set up the global ^TMP(“SDNS”, SORT ( clinic, reminder location or stop code)</p>
<p>Call ^SDMHAD1 routine to print the report.</p></td>
</tr>
</tbody>
</table>

### ^SDMHAD1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the print routine for the High Risk Mental Health AD HOC No Show Report. The report lists the patient that no showed for the mental health appointment, the date the of the appointment, the clinic and stop code. It also lists the contact information for the patient, the Next of Kin, emergency contacts, clinic provider, future scheduled appointments, Mental Health Treatment Coordinator and care team and results of efforts in contacting the patient.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th colspan="9"><strong>^SDMHAD1</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enhancement Category</td>
<td colspan="2">New</td>
<td>Modify</td>
<td colspan="3">Delete</td>
<td colspan="3">No Change</td>
</tr>
<tr class="even">
<td>SRS Traceability</td>
<td colspan="9"></td>
</tr>
<tr class="odd">
<td>Related Options</td>
<td colspan="9">N/A</td>
</tr>
<tr class="even">
<td rowspan="2">Related Routines</td>
<td colspan="5">Routines “Called By”</td>
<td colspan="4">Routines “Called”</td>
</tr>
<tr class="odd">
<td colspan="5"><strong>^SDMHAD</strong></td>
<td colspan="4"><p><strong>C^%DTC</strong></p>
<p><strong>$$GET1^DIQ</strong></p>
<p><strong>^DIR</strong></p>
<p><strong>$$HLPHONE^HLFNC</strong></p>
<p><strong>$$SDAPI^SDAMA301</strong></p>
<p><strong>HEAD^SDMHAD</strong></p>
<p><strong>^VADATE</strong></p>
<p><strong>KVAR^VADPT</strong></p>
<p><strong>OAD^VADPT</strong></p>
<p><strong>PID^VADPT6</strong></p></td>
</tr>
<tr class="even">
<td>Data Dictionary References</td>
<td colspan="9"><p><strong>^DIC(40.7 CLINIC STOP</strong></p>
<p><strong>^DPT( PATIENT</strong></p>
<p><strong>^SC( HOSPITAL LOCATION</strong></p>
<p><strong>^TMP(</strong></p>
<p><strong>^TMP($J</strong></p>
<p><strong>^VA(200</strong> <strong>NEW PERSON</strong></p></td>
</tr>
<tr class="odd">
<td>Related Protocols</td>
<td colspan="9">N/A</td>
</tr>
<tr class="even">
<td>Related Integration Agreements</td>
<td colspan="9">N/A</td>
</tr>
<tr class="odd">
<td>Data Passing</td>
<td>Input</td>
<td colspan="3">Output Reference</td>
<td colspan="3">Both</td>
<td>Global Reference</td>
<td>Local</td>
</tr>
<tr class="even">
<td>Input Attribute Name and Definition</td>
<td colspan="9"><p>Name:</p>
<p>Definition:</p></td>
</tr>
<tr class="odd">
<td>Output Attribute Name and Definition</td>
<td colspan="9"><p>Name:</p>
<p>Definition:</p></td>
</tr>
<tr class="even">
<td colspan="10">Current Logic</td>
</tr>
<tr class="odd">
<td colspan="10"></td>
</tr>
<tr class="even">
<td colspan="10">Modified Logic (Changes are in bold)</td>
</tr>
<tr class="odd">
<td colspan="10"><p>The code will loop through the ^TMP(“SDNS”, SORT ( clinic, reminder location or stop code) global</p>
<p>- A header will print for each division (alphabetical) which will include the following information: the</p>
<p>The second line will designate how the report will be sorted and printed. This example, sorts by clinic.</p>
<p>MENTAL HEALTH NO SHOW REPORT NOV 10,2010@09:34 PAGE 1</p>
<p>BY CLINIC</p>
<p>PATIENT PT ID EVENT D/T CLINIC STOP CODE</p>
<p>*</p>
<p>DIVISION: ALBANY</p>
<p>If the sort is by the reminder location the following will print:</p>
<p>MENTAL HEALTH NO SHOW REPORT NOV 10,2010@09:34 PAGE 1</p>
<p>BY REMINDER LOCATION LIST</p>
<p>PATIENT PT ID EVENT D/T CLINIC STOP CODE</p>
<p>*</p>
<p>DIVISION/REM LOC LIST: ALBANY/VA-MH QUERI PC CLINIC STOPS</p>
<p>- The patient name , ID, date of no showed appointment, clinic and the stop code will print</p>
<p>For each patient listed, the following information if available will print:</p>
<ul>
<li><p>Patient phone numbers for home, office, cell</p></li>
<li><p>Next of Kin information, contact, relationship to patient and address and phone numbers</p></li>
<li><p>Emergency contact information, contact, relationship to patient, address and phone numbers</p></li>
<li><p>Default provider for the clinic they no showed for</p></li>
<li><p>Mental Health Treatment Coordinator and Care team (in Parenthesis)</p></li>
<li><p>Future scheduled appointments, clinic, date and location of the clinic</p></li>
<li><p>The results of efforts to contact the patient. (information from clinical reminder API)</p></li>
</ul>
<p>If there are no patients the heading will print with no records available.</p>
<p>MENTAL HEALTH NO SHOW REPORT NOV 10,2010@09:54 PAGE 1</p>
<p>BY CLINIC</p>
<p>PATIENT PT ID EVENT D/T CLINIC STOP CODE</p>
<p>*</p>
<p>&gt;&gt;&gt;&gt;&gt;&gt; NO RECORDS FOUND &lt;&lt;&lt;&lt;&lt;&lt;</p></td>
</tr>
</tbody>
</table>

### ^SDMHNS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the High Risk Mental Health No show Report entry point that is called by the scheduling background job. This report will display all patients that did not show up for their scheduled appointment for a Mental Health clinic. It will list patient contact information, Next of Kin, emergency contact, clinic default provider, future scheduled appointments Mental Health Treatment Coordinator and care team and results of attempts to contact the no showed patients. The user will not be asked any sort criteria, the report will list for the day before the background job run, for all the divisions in the facility and mental health clinics in the facility. The report will be sent to members of the SD MH NO SHOW NOTIFICATION mail group.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th colspan="9"><strong>^SDMHNS</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enhancement Category</td>
<td colspan="2">New</td>
<td>Modify</td>
<td colspan="3">Delete</td>
<td colspan="3">No Change</td>
</tr>
<tr class="even">
<td>SRS Traceability</td>
<td colspan="9"></td>
</tr>
<tr class="odd">
<td>Related Options</td>
<td colspan="9">N/A</td>
</tr>
<tr class="even">
<td rowspan="2">Related Routines</td>
<td colspan="5">Routines “Called By”</td>
<td colspan="4">Routines “Called”</td>
</tr>
<tr class="odd">
<td colspan="5"><strong>^SDAMQ</strong></td>
<td colspan="4"><p><strong>C^%DTC</strong></p>
<p><strong>NOW^%DTC</strong></p>
<p><strong>HOME^%ZIS</strong></p>
<p><strong>XMY^DGMTUTL</strong></p>
<p><strong>$$LINE^SDMHAD</strong></p>
<p><strong>$$LINE1^SDMHAD</strong></p>
<p><strong>START^SDMHAD</strong></p>
<p><strong>$$SETSTR^SDMHNS1</strong></p>
<p><strong>SET1^SDMHNS1</strong></p>
<p><strong>^VADATE</strong></p>
<p><strong>^XMD</strong></p>
<p><strong>EN^XUTMDEVQ</strong></p></td>
</tr>
<tr class="even">
<td>Data Dictionary References</td>
<td colspan="9"><p><strong>^TMP("SDNS"</strong></p>
<p><strong>^XMB(3.8 MAIL GROUP</strong></p></td>
</tr>
<tr class="odd">
<td>Related Protocols</td>
<td colspan="9">N/A</td>
</tr>
<tr class="even">
<td>Related Integration Agreements</td>
<td colspan="9">N/A</td>
</tr>
<tr class="odd">
<td>Data Passing</td>
<td>Input</td>
<td colspan="3">Output Reference</td>
<td colspan="3">Both</td>
<td>Global Reference</td>
<td>Local</td>
</tr>
<tr class="even">
<td>Input Attribute Name and Definition</td>
<td colspan="9"><p>Name:</p>
<p>Definition:</p></td>
</tr>
<tr class="odd">
<td>Output Attribute Name and Definition</td>
<td colspan="9"><p>Name:</p>
<p>Definition:</p></td>
</tr>
<tr class="even">
<td colspan="10">Current Logic</td>
</tr>
<tr class="odd">
<td colspan="10"></td>
</tr>
<tr class="even">
<td colspan="10">Modified Logic (Changes are in bold)</td>
</tr>
<tr class="odd">
<td colspan="10"><p>The variable SDXFLG is set to 1 ; This flag is set to 1 when running from the background Job</p>
<p>The date range is set to T-1 from the date the SD Nightly Background Job is run.</p>
<p>The Division is set to ALL the divisions in the facility.</p>
<p>The sort criteria, is set All Clinics.</p>
<p>Call is made to START ^SDMHAD</p>
<ul>
<li><p>Check to see if the division/clinic/stop have been selected and if the clinic and stop code are a valid</p></li>
</ul>
<p>mental health pair.</p>
<p>-Set ^TMP(“SDNSHOW”,$J with the valid choices</p>
<p>Find the patients in the date range that had a no show appointment, no show auto rebook or no action taken for a mental health clinic</p>
<p>-Loop through the ^TMP(“SDNSHOW”,$J global</p>
<blockquote>
<p>Within that loop, check the Hospital Location “S” X-ref to see if the patient has an appointment</p>
<p>In the date range.. ^SC(clinic,”S”,date</p>
</blockquote>
<p>- If there is a match, set up the global ^TMP(“SDNS”, SORT ( clinic, reminder location or stop code)</p>
<p>Call to ^SDMHNS1 routine to set up the global ^TMP(“SDNS”,$J, LINE NUMBER,0) that hold the data for sending an email message to all persons in the email group SD MH NO SHOW NOTIFICATION.</p>
<p>Variables are set up to send the data in a mail message.</p>
<p>SDGRP is set to the mail group number for SD MH NO SHOW NOTIFICATION</p>
<p>XMSUB the subject of the email is set to MN NO SHOW REPORT MESSAGE</p>
<p>XMTEXT is set to the global containing the data ^TMP(“SDNS”,$J, LINE #,0)</p>
<p>Call is made to set up and send the mail message D ^XMD the user will be able to print out the email message to a printer for a hard copy through mailman.</p>
<p>The report will be almost identical to the AD HOC report except it will have mailman designation in the heading.</p></td>
</tr>
</tbody>
</table>

### ^SDMHNS1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the print routine for the High Risk Mental Health No Show Report run from the scheduling nightly background job. The report lists the patient that no showed for the mental health appointment, the date the of the appointment, the clinic and stop code. It also lists the, clinic provider and future scheduled appointments for the patient up to 30 days out. The report will be sent to members of the SD MH NO SHOW NOTIFICATION mail group.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th colspan="9"><strong>^SDMHNS1</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enhancement Category</td>
<td colspan="2">New</td>
<td>Modify</td>
<td colspan="3">Delete</td>
<td colspan="3">No Change</td>
</tr>
<tr class="even">
<td>SRS Traceability</td>
<td colspan="9"></td>
</tr>
<tr class="odd">
<td>Related Options</td>
<td colspan="9">N/A</td>
</tr>
<tr class="even">
<td rowspan="2">Related Routines</td>
<td colspan="5">Routines “Called By”</td>
<td colspan="4">Routines “Called”</td>
</tr>
<tr class="odd">
<td colspan="5"><strong>^SDMHNS</strong></td>
<td colspan="4"><p><strong>C^%DTC</strong></p>
<p><strong>$$GET1^DIQ</strong></p>
<p><strong>$$HLPHONE^HLFNC</strong></p>
<p><strong>$$SDAPI^SDAMA301</strong></p>
<p><strong>HEAD^SDMHNS</strong></p>
<p><strong>$$SETSTR^SDUL1</strong></p>
<p><strong>^VADATE</strong></p>
<p><strong>KVAR^VADPT</strong></p>
<p><strong>OAD^VADPT</strong></p>
<p><strong>PID^VADPT6</strong></p></td>
</tr>
<tr class="even">
<td>Data Dictionary References</td>
<td colspan="9"><p><strong>^DIC(40.7 CLINIC STOP</strong></p>
<p><strong>^DPT( PATIENT</strong></p>
<p><strong>^SC( HOSPITAL LOCATION</strong></p>
<p><strong>^TMP(</strong></p>
<p><strong>^TMP("SDNS"</strong></p>
<p><strong>^TMP($J</strong></p>
<p><strong>^VA(200 NEW PERSON</strong></p></td>
</tr>
<tr class="odd">
<td>Related Protocols</td>
<td colspan="9">N/A</td>
</tr>
<tr class="even">
<td>Related Integration Agreements</td>
<td colspan="9">N/A</td>
</tr>
<tr class="odd">
<td>Data Passing</td>
<td>Input</td>
<td colspan="3">Output Reference</td>
<td colspan="3">Both</td>
<td>Global Reference</td>
<td>Local</td>
</tr>
<tr class="even">
<td>Input Attribute Name and Definition</td>
<td colspan="9"><p>Name:</p>
<p>Definition:</p></td>
</tr>
<tr class="odd">
<td>Output Attribute Name and Definition</td>
<td colspan="9"><p>Name:</p>
<p>Definition:</p></td>
</tr>
<tr class="even">
<td colspan="10">Current Logic</td>
</tr>
<tr class="odd">
<td colspan="10"></td>
</tr>
<tr class="even">
<td colspan="10">Modified Logic (Changes are in bold)</td>
</tr>
<tr class="odd">
<td colspan="10"><p>The code will loop through the ^TMP(“SDNS”, Clinic, global</p>
<p>- A header will be set into the ^TMP(“SDNS”,$J,LINE #,0) global for each division (alphabetical)</p>
<p>which will include the following information:</p>
<p>The second line will designate how the report will be sorted and printed. The background job will</p>
<p>only print the report by Clinic.</p>
<p>MENTAL HEALTH NO SHOW REPORT NOV 10,2010@09:34 PAGE 1</p>
<p>BY CLINIC</p>
<p>PATIENT PT ID EVENT D/T CLINIC STOP CODE</p>
<p>*</p>
<p>DIVISION: ALBANY</p>
<ul>
<li><p>For each patient listed, the following information if available will be set into the ^TMP(“SDNS”,$J,LINE #,0) global:</p>
<ul>
<li><p>Patient phone numbers for home, office, cell</p></li>
<li><p>Next of Kin information, contact, relationship to patient and address and phone numbers</p></li>
<li><p>Emergency contact information, contact, relationship to patient, address and phone numbers</p></li>
<li><p>Default provider for the clinic they no showed for</p></li>
<li><p>Mental Health Treatment Coordinator MHTC and care team (in parenthesis)</p></li>
<li><p>Future scheduled appointments, clinic, date and location of the clinic</p></li>
<li><p>The results of efforts to contact the patient. (information from clinical reminder API)</p></li>
</ul></li>
</ul>
<p>If there are no patients the heading will print with no records available.</p>
<p>MENTAL HEALTH NO SHOW REPORT NOV 10,2010@09:54 PAGE 1</p>
<p>BY CLINIC</p>
<p>PATIENT PT ID EVENT D/T CLINIC STOP CODE</p>
<p></p>
<p>&gt;&gt;&gt;&gt;&gt;&gt; NO RECORDS FOUND &lt;&lt;&lt;&lt;&lt;&lt;</p></td>
</tr>
</tbody>
</table>

### ^SDAMQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th colspan="9"><strong>^SDAMQ</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enhancement Category</td>
<td colspan="2">New</td>
<td>Modify</td>
<td colspan="3">Delete</td>
<td colspan="3">No Change</td>
</tr>
<tr class="even">
<td>SRS Traceability</td>
<td colspan="9"></td>
</tr>
<tr class="odd">
<td>Related Options</td>
<td colspan="9">Nightly job for PM data extract [<strong>SDOQM PM NIGHTLY JOB]</strong></td>
</tr>
<tr class="even">
<td rowspan="2">Related Routines</td>
<td colspan="5">Routines “Called By”</td>
<td colspan="4">Routines “Called”</td>
</tr>
<tr class="odd">
<td colspan="5"></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td>Data Dictionary References</td>
<td colspan="9">N/A</td>
</tr>
<tr class="odd">
<td>Related Protocols</td>
<td colspan="9">N/A</td>
</tr>
<tr class="even">
<td>Related Integration Agreements</td>
<td colspan="9">N/A</td>
</tr>
<tr class="odd">
<td>Data Passing</td>
<td>Input</td>
<td colspan="3">Output Reference</td>
<td colspan="3">Both</td>
<td>Global Reference</td>
<td>Local</td>
</tr>
<tr class="even">
<td>Input Attribute Name and Definition</td>
<td colspan="9"><p>Name:</p>
<p>Definition:</p></td>
</tr>
<tr class="odd">
<td>Output Attribute Name and Definition</td>
<td colspan="9"><p>Name:</p>
<p>Definition:</p></td>
</tr>
<tr class="even">
<td colspan="10">Current Logic</td>
</tr>
<tr class="odd">
<td colspan="10"><p>START ;</p>
<p>G STARTQ:'$$SWITCH</p>
<p>N SDSTART,SDFIN</p>
<p>K ^TMP("SDSTATS",$J)</p>
<p>S SDSTART=$$NOW^SDAMU D ADD^SDAMQ1</p>
<p>D EN^SDAMQ3(SDBEG,SDEND) ; appointments</p>
<p>D EN^SDAMQ4(SDBEG,SDEND) ; add/edits</p>
<p>D EN^SDAMQ5(SDBEG,SDEND) ; dispositions</p>
<p>S SDFIN=$$NOW^SDAMU D UPD^SDAMQ1(SDBEG,SDEND,SDFIN,.05)</p>
<p>D BULL^SDAMQ1</p>
<p>STARTQ K SDBEG,SDEND,SDAMETH,^TMP("SDSTATS",$J) Q</p></td>
</tr>
<tr class="even">
<td colspan="10">Modified Logic (Changes are in bold)</td>
</tr>
<tr class="odd">
<td colspan="10"><p>START ;</p>
<p>G STARTQ:'$$SWITCH</p>
<p>N SDSTART,SDFIN</p>
<p>;N SDMHNOSH ; set for no show report</p>
<p>K ^TMP("SDSTATS",$J)</p>
<p>S SDSTART=$$NOW^SDAMU D ADD^SDAMQ1</p>
<p>D EN^SDAMQ3(SDBEG,SDEND) ; appointments</p>
<p>D EN^SDAMQ4(SDBEG,SDEND) ; add/edits</p>
<p>D EN^SDAMQ5(SDBEG,SDEND) ; dispositions</p>
<p>S SDFIN=$$NOW^SDAMU D UPD^SDAMQ1(SDBEG,SDEND,SDFIN,.05)</p>
<p>D BULL^SDAMQ1</p>
<p>STARTQ K SDBEG,SDEND,SDAMETH,^TMP("SDSTATS",$J) Q</p>
<p>;</p>
<p>AUTO ; -- nightly job entry point</p>
<p>G:'$$SWITCH AUTOQ</p>
<p>; -- do yesterday's first</p>
<p>S X1=DT,X2=-1 D C^%DTC</p>
<p>S (SDOPCDT,SDBEG)=X,SDEND=X+.24,SDAMETH=1 D START</p>
<p><strong>D EN^SDMHNS</strong></p>
<p><strong>D EN^SDMHPRO</strong></p></td>
</tr>
</tbody>
</table>

EN^SDMHPRO

This routine is the front end of the Proactive background job report and sets up the data to be printed.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th colspan="9"><h3 id="ensdmhpro" class="unnumbered"> EN^SDMHPRO</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Enhancement Category</strong></td>
<td colspan="2"><strong>New</strong></td>
<td><strong>Modify</strong></td>
<td colspan="3"><strong>Delete</strong></td>
<td colspan="3"><strong>No Change</strong></td>
</tr>
<tr class="even">
<td><strong>Requirement Traceability Matrix</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="odd">
<td><strong>Related Options</strong></td>
<td colspan="9"><strong>High Risk MH Proactive Nightly Report [SD MH PROACTIVE BGJ REPORT] option</strong></td>
</tr>
<tr class="even">
<td rowspan="2">Related Routines</td>
<td colspan="5">Routines “Called By”</td>
<td colspan="4">Routines “Called”</td>
</tr>
<tr class="odd">
<td colspan="5"><strong>^SDAMQ</strong></td>
<td colspan="4"><p><strong>NOW^%DTC</strong></p>
<p><strong>$$LINE^SDMHAP</strong></p>
<p><strong>$$LINE1^SDMHAP</strong></p>
<p><strong>START^SDMHAP RET^SDMHAP1</strong></p>
<p><strong>$$SETSTR^SDMHPRO1 SET1^SDMHPRO1 XMY^SDUTL2 $$FMTE^XLFDT</strong></p>
<p><strong>^XMD</strong></p></td>
</tr>
<tr class="even">
<td><strong>Data Dictionary (DD) References</strong></td>
<td colspan="9"><p><strong>^TMP(</strong></p>
<p><strong>^TMP("SDMHP"</strong></p>
<p><strong>^XMB(3.8</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Related Protocols</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="even">
<td><strong>Related Integration Control Registrations (ICRs)</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="odd">
<td><strong>Data Passing</strong></td>
<td><strong>Input</strong></td>
<td colspan="3"><strong>Output Reference</strong></td>
<td colspan="3"><strong>Both</strong></td>
<td><strong>Global Reference</strong></td>
<td><strong>Local</strong></td>
</tr>
<tr class="even">
<td><strong>Input Attribute Name and Definition</strong></td>
<td colspan="9"><p><strong>Name: None</strong></p>
<p><strong>Definition:</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Output Attribute Name and Definition</strong></td>
<td colspan="9"><p><strong>Name: None</strong></p>
<p><strong>Definition:</strong></p></td>
</tr>
<tr class="even">
<td colspan="10"><strong>Current Logic</strong></td>
</tr>
<tr class="odd">
<td colspan="10"><strong>None</strong></td>
</tr>
<tr class="even">
<td colspan="10"><strong>Modified Logic (Changes are in bold)</strong></td>
</tr>
<tr class="odd">
<td colspan="10"><p><strong>The variable SDXFLG is set to 1 ; This flag is set to 1 when running from the background Job</strong></p>
<p><strong>The date range is set to T from the date the SD Nightly Background Job is run.</strong></p>
<p><strong>The Division is set to ALL the divisions in the facility.</strong></p>
<p><strong>The sort criteria, is set All Clinics.</strong></p>
<p><strong>Call is made to START ^SDMHPRO</strong></p>
<p><strong>Check to see if the clinics are mental health clinics in the Reminder location file</strong></p>
<p><strong>-Set ^TMP(“SDPRO”,$J with the valid choices</strong></p>
<p><strong>Find the patients in the date range that had an appointment for a mental health clinic</strong></p>
<p><strong>-Loop through the ^TMP(“SDPRO”,$J global</strong></p>
<p><strong>Within that loop, check the Hospital Location “S” X-ref to see if the patient has an appointment</strong></p>
<p><strong>In the date range.. ^SC(clinic,”S”,date</strong></p>
<p><strong>- If there is a match, set up the global ^TMP(“SDPRO1”, SORT ( clinic, reminder location or stop code)</strong></p>
<p><strong>Call to ^SDMHPRO1 routine to set up the global ^TMP(“SDMHP”,$J, LINE NUMBER,0) that hold the data for sending an email message to all persons in the email group SD MH NO SHOW NOTIFICATION.</strong></p>
<p><strong>Variables are set up to send the data in a mail message.</strong></p>
<p><strong>SDGRP is set to the mail group number for SD MH NO SHOW NOTIFICATION</strong></p>
<p><strong>XMSUB the subject of the email is set to MN NO SHOW REPORT MESSAGE #</strong></p>
<p><strong>XMTEXT is set to the global containing the data ^TMP(“SDNS”,$J, LINE #,0)</strong></p>
<p><strong>Call is made to set up and send the mail message D ^XMD the user will be able to print out the email message to a printer for a hard copy through mailman.</strong></p>
<p><strong>The report will be identical to the AD HOC report except it will have mailman designation in the heading.</strong></p></td>
</tr>
</tbody>
</table>

### ^SDMHPRO1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is called by routine SDMHPRO and is the routine that prints out the Proactive Background Job report.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th colspan="9"><h3 id="ensdmhpro1" class="unnumbered"> EN^SDMHPRO1</h3></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Enhancement Category</strong></td>
<td colspan="2"><strong>New</strong></td>
<td><strong>Modify</strong></td>
<td colspan="3"><strong>Delete</strong></td>
<td colspan="3"><strong>No Change</strong></td>
</tr>
<tr class="even">
<td><strong>Requirement Traceability Matrix</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="odd">
<td><strong>Related Options</strong></td>
<td colspan="9"><strong>High Risk MH Proactive Nightly Report [SD MH PROACTIVE BGJ REPORT] option</strong></td>
</tr>
<tr class="even">
<td rowspan="2">Related Routines</td>
<td colspan="5">Routines “Called By”</td>
<td colspan="4">Routines “Called”</td>
</tr>
<tr class="odd">
<td colspan="5"><strong>^SDMHPRO</strong></td>
<td colspan="4"><p><strong>C^%DTC</strong></p>
<p><strong>$$SDAPI^SDAMA301</strong></p>
<p><strong>COUNT^SDMHPRO</strong></p>
<p><strong>HEAD^SDMHPRO</strong></p>
<p><strong>HEAD1^SDMHPRO</strong></p>
<p><strong>TOTAL^SDMHPRO</strong></p>
<p><strong>$$SETSTR^SDUL1</strong></p>
<p><strong>PID^VADPT6</strong></p>
<p><strong>$$FMTE^XLFDT</strong></p></td>
</tr>
<tr class="even">
<td><strong>Data Dictionary (DD) References</strong></td>
<td colspan="9"><p><strong>^DG(40.8</strong></p>
<p><strong>^DIC(40.7</strong></p>
<p><strong>^DPT(</strong></p>
<p><strong>^DPT("B"</strong></p>
<p><strong>^SC(</strong></p>
<p><strong>^TMP(</strong></p>
<p><strong>^TMP("SDMHP"</strong></p>
<p><strong>^TMP("SDPRO1"</strong></p>
<p><strong>^TMP($J</strong></p>
<p><strong>^VA(200</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Related Protocols</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="even">
<td><strong>Related Integration Control Registrations (ICRs)</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="odd">
<td><strong>Data Passing</strong></td>
<td><strong>Input</strong></td>
<td colspan="3"><strong>Output Reference</strong></td>
<td colspan="3"><strong>Both</strong></td>
<td><strong>Global Reference</strong></td>
<td><strong>Local</strong></td>
</tr>
<tr class="even">
<td><strong>Input Attribute Name and Definition</strong></td>
<td colspan="9"><p><strong>Name: None</strong></p>
<p><strong>Definition:</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Output Attribute Name and Definition</strong></td>
<td colspan="9"><p><strong>Name: None</strong></p>
<p><strong>Definition:</strong></p></td>
</tr>
<tr class="even">
<td colspan="10"><strong>Current Logic</strong></td>
</tr>
<tr class="odd">
<td colspan="10"><strong>None</strong></td>
</tr>
<tr class="even">
<td colspan="10"><strong>Modified Logic (Changes are in bold)</strong></td>
</tr>
<tr class="odd">
<td colspan="10"><p><strong>The code will loop through the ^TMP(“SDPRO1” global</strong></p>
<p><strong>- A totals page will print out of the unique patients at the beginning of the report.</strong></p>
<p><strong>- A header will print for each division (alphabetical) which will include the following information: the</strong></p>
<p><strong>- The second line will designate how the report will be sorted and printed. This example, sorts by clinic.</strong></p>
<p><strong>- The patient name , ID, date of appointment, clinic</strong></p>
<p><strong>PROACTIVE HIGH RISK REPORT PAGE 1</strong></p>
<p><strong>by CLINIC for Appointments 9/24/11-10/14/11 Run: 10/14/2011@12:39</strong></p>
<p><strong>PATIENT PT ID APPT D/T CLINIC</strong></p>
<p><strong></strong></p>
<p><strong>DIVISION: ALBANY</strong></p>
<p><strong>1 Schedulingpatient, One 0000 10/3/2011 9:00 am D-PSYCHXXXXXXXXXX</strong></p>
<p><strong>PROACTIVE HIGH RISK REPORT PAGE 2</strong></p>
<p><strong>by CLINIC for Appointments 9/24/11-10/14/11 Run: 10/4/2011@12:39</strong></p>
<p><strong>PATIENT PT ID APPT D/T CLINIC</strong></p>
<p><strong></strong></p>
<p><strong>DIVISION: ON THE HUDSON IN HISTORIC TROY</strong></p>
<p><strong>1 Schedulingpatient, One 0000 9/29/2011 11:00 am LIZ'S MENTAL HEALTH CLI</strong></p>
<p><strong>10/3/2011 3:00 pm LIZ'S MENTAL HEALTH CLI</strong></p>
<p><strong>2 Schedulingpatient, TWO 6666 10/4/2011 10:00 am LIZ'S MENTAL HEALTH CLI</strong></p>
<p><strong>PROACTIVE HIGH RISK REPORT PAGE 3</strong></p>
<p><strong>by CLINIC for Appointments 9/24/11-10/14/11 Run: 10/4/2011@12:39</strong></p>
<p><strong>PATIENT PT ID APPT D/T CLINIC</strong></p>
<p><strong></strong></p>
<p><strong>DIVISION: TROY1</strong></p>
<p><strong>1 Schedulingpatient, One 0000 9/30/2011 11:00 am MENTAL HEALTH</strong></p>
<p><strong>2 Schedulingpatient, TWO 6666 10/5/2011 10:00 am MENTAL HEALTH</strong></p>
<p><strong>PROACTIVE HIGH RISK REPORT PAGE 4</strong></p>
<p><strong>by CLINIC for Appointments 9/24/11-10/14/11 Run: 10/4/2011@12:39</strong></p>
<p><strong>Totals Page</strong></p>
<p><strong></strong></p>
<p><strong>Division/Clinic Appointment Totals</strong></p>
<p><strong>Division/CLinic Unique</strong></p>
<p><strong>Patients</strong></p>
<p><strong>ALBANY 1</strong></p>
<p><strong>ON THE HUDSON IN HISTORIC TROY 2</strong></p>
<p><strong>TROY1 2</strong></p>
<p><strong>If there are no patients the heading will print with no records available.</strong></p>
<p><strong>PROACTIVE HIGH RISK REPORT PAGE 3</strong></p>
<p><strong>by CLINIC for Appointments 9/24/11-10/14/11 Run: 10/4/2011@12:39</strong></p>
<p><strong>PATIENT PT ID APPT D/T CLINIC</strong></p>
<p><strong></strong></p>
<p><strong>&gt;&gt;&gt;&gt;&gt;&gt; NO RECORDS FOUND &lt;&lt;&lt;&lt;&lt;&lt;</strong></p></td>
</tr>
</tbody>
</table>

### EN^SDMHAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is the front end of the Proactive Ad Hoc report and sets up the data to be printed.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th colspan="9"><strong>EN^SDMHAP</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Enhancement Category</strong></td>
<td colspan="2"><strong>New</strong></td>
<td><strong>Modify</strong></td>
<td colspan="3"><strong>Delete</strong></td>
<td colspan="3"><strong>No Change</strong></td>
</tr>
<tr class="even">
<td><strong>Requirement Traceability Matrix</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="odd">
<td><strong>Related Options</strong></td>
<td colspan="9"><strong>High Risk MH No-Show Adhoc Report [SD MH NO SHOW AD HOC REPORT] option</strong></td>
</tr>
<tr class="even">
<td rowspan="2">Related Routines</td>
<td colspan="5">Routines “Called By”</td>
<td colspan="4">Routines “Called”</td>
</tr>
<tr class="odd">
<td colspan="5"></td>
<td colspan="4"><p><strong>C^%DTC</strong></p>
<p><strong>NOW^%DTC</strong></p>
<p><strong>^%ZIS</strong></p>
<p><strong>^%ZTLOAD</strong></p>
<p><strong>$$GETINF^DGPFAPIH</strong></p>
<p><strong>$$GETFLAG^DGPFAPIU</strong></p>
<p><strong>CLOSE^DGUTQ</strong></p>
<p><strong>WAIT^DICD</strong></p>
<p><strong>D^DIR</strong></p>
<p><strong>SWITCH^SDAMU</strong></p>
<p><strong>ASK2^SDDIV</strong></p>
<p><strong>^SDMHAP1</strong></p>
<p><strong>HEAD^SDMHPRO</strong></p>
<p><strong>^SDMHPRO1</strong></p>
<p><strong>$$SETSTR^SDMHPRO1</strong></p>
<p><strong>SET1^SDMHPRO1</strong></p>
<p><strong>PID^VADPT6</strong></p>
<p><strong>$$FDATE^VALM1</strong></p>
<p><strong>FIRST^VAUTOMA</strong></p>
<p><strong>$$FMTE^XLFDT</strong></p></td>
</tr>
<tr class="even">
<td><strong>Data Dictionary (DD) References</strong></td>
<td colspan="9"><p><strong>^%ZOSF("TEST"</strong></p>
<p><strong>^DG(40.8</strong></p>
<p><strong>^DIC(40.7</strong></p>
<p><strong>^DPT(</strong></p>
<p><strong>^PXRMD(810.9</strong></p>
<p><strong>^SC(</strong></p>
<p><strong>^SC("AST"</strong></p>
<p><strong>^TMP(</strong></p>
<p><strong>^TMP("SDPRO"</strong></p>
<p><strong>^TMP("SDPRO1"</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Related Protocols</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="even">
<td><strong>Related Integration Control Registrations (ICRs)</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="odd">
<td><strong>Data Passing</strong></td>
<td><strong>Input</strong></td>
<td colspan="3"><strong>Output Reference</strong></td>
<td colspan="3"><strong>Both</strong></td>
<td><strong>Global Reference</strong></td>
<td><strong>Local</strong></td>
</tr>
<tr class="even">
<td><strong>Input Attribute Name and Definition</strong></td>
<td colspan="9"><p><strong>Name: None</strong></p>
<p><strong>Definition:</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Output Attribute Name and Definition</strong></td>
<td colspan="9"><p><strong>Name: None</strong></p>
<p><strong>Definition:</strong></p></td>
</tr>
<tr class="even">
<td colspan="10"><strong>Current Logic</strong></td>
</tr>
<tr class="odd">
<td colspan="10"><strong>None</strong></td>
</tr>
<tr class="even">
<td colspan="10"><strong>Modified Logic (Changes are in bold)</strong></td>
</tr>
<tr class="odd">
<td colspan="10"><p><strong>User is asked to choose the date range.</strong></p>
<p><strong>User is asked to choose the Divisions in the facility ( one, many, `all)</strong></p>
<p><strong>Report will sort by clinic.</strong></p>
<p><strong>User will be asked to list report by <u>A</u>ll clinics ( mental health and not mental health ) or <u>M</u>ental Health clinics only</strong></p>
<ul>
<li><p><strong>If All clinics the user can choose all the clinics in the facility</strong></p></li>
<li><p><strong>If Mental Health clinics only, the user will choose only clinics that have stop codes located in the</strong></p></li>
</ul>
<p><strong>Reminder Location List VA-MH NO SHOW APPT CLINICS LL</strong></p>
<ul>
<li><p><strong>Set ^TMP( “SDPRO”,$J with the valid choices</strong></p></li>
</ul>
<p><strong>Find the patients in the date range with High Risk for Mental Health patient record flag that have an appointment.</strong></p>
<p><strong>-Loop through the ^TMP(“SDPRO”,$J global</strong></p>
<ul>
<li><p><strong>Within that loop, check the Hospital Location “S” X-ref to see if the patient has an appointment</strong></p></li>
</ul>
<blockquote>
<p><strong>In the date range.. ^SC(clinic,”S”,date</strong></p>
</blockquote>
<p><strong>- If there is a match, set up the global ^TMP(“SDPRO1”, SORT by clinic</strong></p>
<p><strong>Call ^SDMHAP1 routine to print the report.</strong></p></td>
</tr>
</tbody>
</table>

EN^SDMHAP1

This routine is called by routine SDMHAP and is the routine that prints out the Proactive Ad Hoc report.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th colspan="9"><strong>EN^SDMHAP1</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Enhancement Category</strong></td>
<td colspan="2"><strong>New</strong></td>
<td><strong>Modify</strong></td>
<td colspan="3"><strong>Delete</strong></td>
<td colspan="3"><strong>No Change</strong></td>
</tr>
<tr class="even">
<td><strong>Requirement Traceability Matrix</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="odd">
<td><strong>Related Options</strong></td>
<td colspan="9"><strong>High Risk MH Proactive Adhoc Report [SD MH PROACTIVE AD HOC REPORT] option</strong></td>
</tr>
<tr class="even">
<td rowspan="2">Related Routines</td>
<td colspan="5">Routines “Called By”</td>
<td colspan="4">Routines “Called”</td>
</tr>
<tr class="odd">
<td colspan="5"><strong>^SDMHAP</strong></td>
<td colspan="4"><p><strong>C^%DTC</strong></p>
<p><strong>^DIR</strong></p>
<p><strong>$$SDAPI^SDAMA301</strong></p>
<p><strong>HEAD^SDMHAP</strong></p>
<p><strong>HEAD1^SDMHAP</strong></p>
<p><strong>COUNT^SDMHPRO</strong></p>
<p><strong>TOTAL1^SDMHPRO</strong></p>
<p><strong>PID^VADPT6</strong></p>
<p><strong>$$FMTE^XLFDT</strong></p></td>
</tr>
<tr class="even">
<td><strong>Data Dictionary (DD) References</strong></td>
<td colspan="9"><p><strong>^DIC(40.7</strong></p>
<p><strong>^DPT(</strong></p>
<p><strong>^TMP(</strong></p>
<p><strong>^TMP($J</strong></p>
<p><strong>^VA(200</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Related Protocols</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="even">
<td><strong>Related Integration Control Registrations (ICRs)</strong></td>
<td colspan="9"><strong>N/A</strong></td>
</tr>
<tr class="odd">
<td><strong>Data Passing</strong></td>
<td><strong>Input</strong></td>
<td colspan="3"><strong>Output Reference</strong></td>
<td colspan="3"><strong>Both</strong></td>
<td><strong>Global Reference</strong></td>
<td><strong>Local</strong></td>
</tr>
<tr class="even">
<td><strong>Input Attribute Name and Definition</strong></td>
<td colspan="9"><p><strong>Name: None</strong></p>
<p><strong>Definition:</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Output Attribute Name and Definition</strong></td>
<td colspan="9"><p><strong>Name: None</strong></p>
<p><strong>Definition:</strong></p></td>
</tr>
<tr class="even">
<td colspan="10"><strong>Current Logic</strong></td>
</tr>
<tr class="odd">
<td colspan="10"><strong>None</strong></td>
</tr>
<tr class="even">
<td colspan="10"><strong>Modified Logic (Changes are in bold)</strong></td>
</tr>
<tr class="odd">
<td colspan="10"><p><strong>The code will loop through the ^TMP(“SDPRO1” global</strong></p>
<p><strong>- A header will print for each division (alphabetical) which will include the following information: the</strong></p>
<p><strong>- The second line will designate how the report will be sorted and printed. This example, sorts by clinic.</strong></p>
<p><strong>- The patient name , ID, date of appointment, clinic</strong></p>
<p><strong>- A totals page will print out of the unique patients.</strong></p>
<p>HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 1</p>
<p>CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58</p>
<p># PATIENT PT ID APPT D/T CLINIC</p>
<p></p>
<p>DIVISION: ALBANY</p>
<p>1 TESTPATIENT,ONEXXXXX T1111 4/4/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX</p>
<p>4/5/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX</p>
<p>4/8/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX</p>
<p>4/9/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX</p>
<p>4/10/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX</p>
<p>4/11/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX</p>
<p>4/12/2013@08:00 D-PSYCHXXXXXXXXXXXXXXXXXXXXX</p>
<p>HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 2</p>
<p>CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58</p>
<p># PATIENT PT ID APPT D/T CLINIC</p>
<p>*</p>
<p>DIVISION: ON THE HUDSON IN HISTORIC TROY</p>
<p>1 TESTPATIENT,TWOXXXX T0000 4/4/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX</p>
<p>4/5/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX</p>
<p>4/7/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX</p>
<p>4/8/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX</p>
<p>4/9/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX</p>
<p>4/10/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX</p>
<p>4/11/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX</p>
<p>4/12/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX</p>
<p>4/14/2013@08:00 LIZ'S MENTAL HEALTH CLINICXXX</p>
<p>HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 3</p>
<p>CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58</p>
<p># PATIENT PT ID APPT D/T CLINIC</p>
<p></p>
<p>DIVISION: TROY1</p>
<p>1 TESTPATIENT,ONEXXXX T1111 4/4/2013@09:00 MENTAL HEALTH</p>
<p>4/5/2013@09:00 MENTAL HEALTH</p>
<p>4/8/2013@09:00 MENTAL HEALTH</p>
<p>4/9/2013@09:00 MENTAL HEALTH</p>
<p>4/10/2013@09:00 MENTAL HEALTH</p>
<p>4/11/2013@09:00 MENTAL HEALTH</p>
<p>4/12/2013@09:00 MENTAL HEALTH</p>
<p>HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 4</p>
<p>CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58</p>
<p>Totals Page</p>
<p></p>
<p>Division/Clinic Appointment Totals</p>
<p>Division/CLinic Unique</p>
<p>Patients</p>
<p>ALBANY 1</p>
<p>ON THE HUDSON IN HISTORIC TROY 1</p>
<p>TROY1 1</p>
<p><strong>If there are no patients the heading will print with no records available.</strong></p>
<p>HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY PAGE 4</p>
<p>CLINIC for Appointments 4/4/13-4/14/13 Run: 4/4/2013@15:58</p>
<p>PATIENT PT ID APPT D/T CLINIC</p>
<p></p>
<p>&gt;&gt;&gt;&gt;&gt;&gt; NO RECORDS FOUND &lt;&lt;&lt;&lt;&lt;&lt;</p></td>
</tr>
</tbody>
</table>

This Page Left Blank Intentionally

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains any special relationships and agreements between the routines and/or files/fields in this software and dependencies. List any routines essential to the software functions, for example:

Provide information on whether an outpatient facility could function without programs relating to inpatient activity and avoid system failure.

Specify the version of VA FileMan, Kernel, and other software required to run this software.

Include a list of Integration Agreements (IA) with instructions for obtaining detailed information for each, or instruct the user how/where to find this information online

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum package versions are required: VA FileMan V. 21.0, Kernel V. 8.0, Kernel Toolkit V. 7.3, VA MailMan V. 7.1, CPRS V. 28, PXRM V. 2.0.18, PCE V. 1.0, IB V. 2.0, IFCAP V. 3.0, DRG Grouper V. 13.0, HL7 V. 1.6, and Generic Code Sheet V. 1.5. Sites should verify that all patches to these packages have been installed.

> **NOTE:** For Scheduling Reports to run correctly, patch DG\*5.3\*836 and DG\*5.3\*849 need to be installed and reminder location list 'VA-MH NO SHOW APPT CLINICS LL' in File (#810.9) must be current.

If your site is running any of the following packages, you MUST be running the listed version or higher.

| MINIMUM VERSION BASELINE                                                               |         |
|--------------------------------------------------------------------------------------------|---------|
| AMIE                                                                                       | None    |
| CPRS (OR V. 3.0\*280)                                                                      | V. 1.0  |
| Dental                                                                                     | V. 1.2  |
| Dietetics                                                                                  | V. 4.33 |
| Inpatient Meds                                                                             | None    |
| IVM                                                                                        | V. 2.0  |
| Laboratory                                                                                 | V. 5.2  |
| Mental Health                                                                              | V. 5.0  |
| Nursing                                                                                    | V. 2.2  |
| Occurrence Screening                                                                       | V. 2.0  |
| Outpatient Pharmacy                                                                        | V. 7.0  |
| Patient Funds                                                                              | V. 3.0  |
| Radiology/Nuclear Medicine                                                                 | V. 4.5  |
| Record Tracking                                                                            | V. 2.0  |
| Social Work                                                                                | V. 3.0  |
| Utilization Review                                                                         | V. 1.06 |
| NOTE: If you are not running one of the above packages, you do NOT need to install it. |         |

You must have all current Kernel V. 8.0, Kernel Toolkit V. 7.3, VA FileMan V. 21.0, RPC Broker V. 1.0, and PIMS V. 5.3 patches installed prior to the installation of PCMM (SD\*5.3\*41, DG\*5.3\*84).

You must have KIDS patch 44 (XU\*8\*44) installed prior to loading the VIC software.

CPRS will be using the PCMM files and GUI interface

The following is a list of all elements that are checked for installation of Ambulatory Care Reporting Project.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 27%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3"><strong>AMBULATORY CARE REPORTING PROJECT ELEMENTS</strong></td>
</tr>
<tr class="even">
<td><strong>ELEMENT CHECKED</strong></td>
<td><strong>CHECK PERFORMED</strong></td>
<td><strong>REQUIRED FOR INSTALL</strong></td>
</tr>
<tr class="odd">
<td>PCE V. 1.0</td>
<td>Installed</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>HL7 V. 1.6</td>
<td>Installed</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>XU*8.0*27</td>
<td>Installed</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>HL*1.6*8</td>
<td>Installed</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>IB*2.0*60</td>
<td>Installed</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Q-ACS.MED.VA.GOV in DOMAIN file (#4.2)</td>
<td>Entry exists</td>
<td>Yes<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
</tr>
<tr class="odd">
<td>SD*5.3*41</td>
<td>Installed</td>
<td>No</td>
</tr>
<tr class="even">
<td>RA*4.5*4</td>
<td>Installed</td>
<td>No<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></td>
</tr>
<tr class="odd">
<td>LR*5.2*127</td>
<td>Installed</td>
<td>No<a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a></td>
</tr>
<tr class="even">
<td>SOW*3*42</td>
<td>Installed</td>
<td>No</td>
</tr>
<tr class="odd">
<td>OPC GENERATION MAIL GROUP field (#216) of the MAS PARAMETER file (#43)</td>
<td>Contains valid Mail Group</td>
<td>No</td>
</tr>
<tr class="even">
<td colspan="3"><p>This domain was distributed by patch XM*DBA*99.</p>
<p>Not installing this patch will result in the loss of workload credit.</p>
<p>Not installing this patch will result in the loss of workload credit.</p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"></li>
<li id="fn2"></li>
<li id="fn3"></li>
</ol>
</aside>

# DBIA Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps are used to obtain the database integration agreements for the PIMS package.

## DBIA AGREEMENTS - CUSTODIAL PACKAGE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. FORUM

2\. DBA Menu

3\. Integration Agreements Menu

4\. Custodial Package Menu

5\. Active by Custodial Package Option

6\. Select Package Name: Registration or Scheduling

## DBIA AGREEMENTS - SUBSCRIBER PACKAGE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. FORUM

2\. DBA Menu

3\. Integration Agreements Menu

4\. Subscriber Package Menu

5\. Print Active by Subscriber Package Option

6\. Start with subscriber package:

- DG to DGZ, VA to VAZ (ADT)
- SD to SDZ, SC to SCZ (scheduling)

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any PIMS option in File 19 which is a menu option should be able to run independently provided the user has the appropriate keys and FileMan access.

In order to use the PCMM client software, the user must be assigned the SC PCMM GUI WORKSTATION option as either a primary or secondary menu option - unless the user has been assigned the XUPROGMODE security key.

This key, usually given to IRM staff, allows use of the client software without the SC PCMM GUI WORKSTATION option being assigned.

## Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with the PIMS package.

## VADPT Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the VADPT Variables section of this file.

### Scheduling Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SDUTL3 contains utilities used to display and retrieve data from the CURRENT PC TEAM and CURRENT PC PRACTITIONER fields in the PATIENT file.

Documentation can also be found in the routine.

\$\$OUTPTPR^SDUTL3(PARM 1) - displays data from CURRENT PC

PRACTITIONER field

Input PARM 1 The internal entry of the PATIENT file.

Output CURRENT PC PRACTIONER in Internal^External format.

If look-up is unsuccessful, 0 will be returned.

\$\$OUTPTTM^SDUTL3(PARM 1) - displays data from CURRENT PC TEAM field.

Input PARM 1 The internal entry of the PATIENT file.

Output CURRENT PC TEAM in Internal^External format. If

look-up is unsuccessful, 0 will be returned.

\$\$OUTPTAP^SDUTL3(PARM 1, PARM 2)

Input PARM 1 The internal entry of the PATIENT file.

Input PARM 2 The relevant data.

Output Pointer to File 200^external value of the name.

\$\$GETALL^SCAPMCA(PARM 1, PARM 2, PARM 3)

This tag returns all information on a patient’s assignment. Please review the documentation in the SCAPMCA routine.

INPTPR^SDUTL3(PARM 1, PARM 2) - stores data in CURRENT PC

PRACTITIONER field.

Input PARM 1 The internal entry of the PATIENT file.

PARM 2 Pointer to the NEW PERSON file indicating the

practitioner associated with the patient's care.

Output SDOKS 1 if data is stored successfully; 0 otherwise

INPTTM^SDUTL3(PARM 1, PARM 2) - stores data in CURRENT PC TEAM field.

Input PARM 1 The internal entry of the PATIENT file.

PARM 2 Pointer to the TEAM file indicating the team associated

with the patient's care.

Output SDOKS 1 if data is stored successfully; 0 otherwise

### Patient Record Flag Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Agreement Applicable

Example: How to access Integration Aagreements

      4903     NAME: PATIENT RECORD FLAG DATA RETRIEVAL

  CUSTODIAL PACKAGE: REGISTRATION                              

SUBSCRIBING PACKAGE: SCHEDULING                                

                        Scheduling requires Patient Record Flag information

                        as part of a new missed appointment report supporting

                        the High Risk Mental Health Initiative.  This report

                        needs to be able to determine which patients  missing

                        a recent appointment have a specified Patient Record

                        Flag assigned. 

                     CLINICAL REMINDERS                        

                        Retrieval of High Risk Mental Health Patient Flag

                        information. 

                     HEALTH SUMMARY                            

                        ADDED 7/19/2011

              USAGE: Controlled Subscri  ENTERED: JAN  6,2011

             STATUS: Active              EXPIRES:

           DURATION: Till Otherwise Agr  VERSION:

        DESCRIPTION:                        TYPE: Routine

   These API's provide a means to retrieve detailed Patient Record Flag

   information by patient and patient record flag, and, to retrieve a list of

   patients with a specific assigned patient record flag during a specified

   date range. 

     ROUTINE: DGPFAPIH

   COMPONENT:  GETINF

               This function will return detailed information from the

               Patient Record Flag files for the specified patient and PRF

               flag.  A date range for active PR Flags is optional.  Data

               array output example:

               DGARR("ASSIGNDT") - Date of initial assignment.

                      i.e. 3110131.093248^Jan 31, 2011@09:32:48)

               DGARR("CATEGORY") - National or Local flag category.

                      i.e. II (LOCAL)^II (LOCAL) DGARR("FLAG") - Variable

               pointer to Local/National flag files and flag name.

                      i.e. 1;DGPF(26.11,^HIGH RISK FOR SUICIDE

               DGARR("FLAGTYPE") - Type of flag usage. 

                      i.e. 1^BEHAVIORAL DGARR("HIST",n,"ACTION") - Type of

               action for history entry

                      i.e. 1^NEW ASSIGNMENT DGARR("HIST",n,"APPRVBY") -

               Person approving the flag assignment

                      i.e. 112345^PERSON,STEVE DGARR("HIST",1,"COMMENT",1,0)
               - Comment for record assignment action

                      i.e "New record flag assignment."

               DGARR("HIST",n,"DATETIME") - Date/Time of Action

                      i.e. 3110131.093248^JAN 31, 2011@09:32:48

               DGARR("HIST",n,"TIULINK") - Pointer to the TIU Document file

               (#8925)

                      i.e. "^" DGARR("NARR",n,0) - Describes the purpose and

               instructions for the application of the flag.

                      i.e. "TEST ENTRY" DGARR("ORIGSITE") - Site that

               initially assigned this flag (Relevant to National flags only)

                      i.e. 500^ALBANY.VA.GOV DGARR("OWNER") - Site which

               currently "Owns" this flag (Relevant to National flags only)

                       i.e. 500^ALBANY.VA.GOV DGARR("REVIEWDT") - Date for

               next review of record flag assignment

                      i.e. 3110501^MAY 01, 2011 DGARR("TIUTITLE") - Pointer

               to the TIU Document Definition file (#8925.1)

                      i.e. 1309^PATIENT RECORD FLAG CATEGORY II - RESEARCH

               STUDY

   VARIABLES:  Input     DGDFN

                           This is the DFN (IEN) for the patient in the

                           PATIENT File (#2).  This is a required variable. 

   VARIABLES:  Input     DGPRF

                           Variable pointer to either the PRF LOCAL FLAG File

                           (#26.11) or to the PRF NATIONAL FLAG file

                           (#26.15).  This is a required variable. 

                            

                           For National Flags:  IEN;DGPF(26.15,

                              For Local Flags:  IEN;DGPF(26.11,

   VARIABLES:  Input     DGSTART

                           Start date for when to begin search for active PRF

                           flags.  This date must be in FM format, i.e.
                           3110106.  This variable is optional, if null,

                           searches will begin with the earliest assigned

                           entry in the PRF ASSIGNMENT HISTORY file (#26.14)

   VARIABLES:  Input     DGEND

                           End date for the search for active PRF entries.

                           This date must be in FM format, i.e. 3110107.

                           This variable is optional, if null or not passed

                           in, all entries to the end of the PRF ASSIGNMENT

                           HISTORY file (#26.14) will be searched. 

   VARIABLES:  Both      DGARR

                           This variable contains the array name for the

                           return data.  This is optional.  If an array name

                           is not specified, the return data is returned in

                           local array "DGPFAPI1". 

   VARIABLES:  Output    DGRSLT

                           Return value from the API call.  Returns "1" if

                           the API was successful in returning PRF data,

                           returns "0" if the API was unsuccessful in

                           returning PRF data. 

   COMPONENT:  GETLST

               This function call returns a list of patients with a specified

               Patient Record Flag assigned for a specified date range. 

                

                 DGARR(DFN,n) - Patient Name^VPID^Date of initial

               assignment^National or Local flag category^flag name

                

               Example:

                  DGARR(9999955648,0)="EASPATIENT,ONE

               A^5000000295V790537^3100201.103713^II (LOCAL)^HIGH RISK FOR

               SUICIDE"

   VARIABLES:  Input     DGPRF

                           Variable pointer to either the PRF LOCAL FLAG File

                           (#26.11) or the PRF NATIONAL FLAG File (#26.15).

                           This variable is required. 

                            

                              National:  IEN;DGPF(26.15,

                                 Local:  IEN;DGPF(26.11,

   VARIABLES:  Input     DGSTART

                           This is the start date to begin searching for

                           patients with the assigned Patient Record Flag.

                           This date must be in FM format, i.e. 3100110. This

                           variable is optional. 

   VARIABLES:  Input     DGEND

                           This is end date for the search range for patients

                           with the assigned Patient Record Flag.  This date

                           must be in FM format, i.e. 3100112. This variable

                           is optional. 

   VARIABLES:  Both      DGARR

                           This variable contains the array name where the

                           returned patient information will be placed.  This

                           is optional, if an array name is not specified,

                           the data will be returned in a TMP Global,

                           ^TMP("PRFLST")

   VARIABLES:  Output    DGRSLT

                           This variable returns a count of the patients

                           placed in the return list. 

           KEYWORDS: PATIENT RECORD FLAGS

                      \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Example: Inquire to an Integration Control Registration

Select INTEGRATION CONTROL REGISTRATIONS Option: inq  Inquire to an Integration Control Registration

Select INTEGRATION REFERENCES: dgpfapiu  5491     REGISTRATION     Controlled Subscription     PATIENT RECORD FLAG VARIABLE POINTER     DGPFAPIU

DEVICE: ;;999  SSH VIRTUAL TERMINAL

INTEGRATION REFERENCE INQUIRY \#5491            MAY  3,2012  10:27    PAGE 1

-----------------------------------------------------------------------------

      5491     NAME: PATIENT RECORD FLAG VARIABLE POINTER

  CUSTODIAL PACKAGE: REGISTRATION                               

SUBSCRIBING PACKAGE: SCHEDULING                                

                     CLINICAL REMINDERS                        

                     HEALTH SUMMARY                            

                        ADDED 7/19/2011

              USAGE: Controlled Subscri  ENTERED: JAN 31,2011

             STATUS: Active              EXPIRES:

           DURATION: Till Otherwise Agr  VERSION:

        DESCRIPTION:                        TYPE: Routine

   Builds and returns a variable pointer to the Patient Record Flag National

   or Local files based on the textual flag name. 

     ROUTINE: DGPFAPIU

   COMPONENT:  GETFLAG

               Get the variable pointer value for the flag text passed in.

   VARIABLES:  Input     DGPRF

                           Name of the Patient Record Flag in the PRF

                           NATIONAL FLAG file, \#26.15, or in the PRF LOCAL

                           FLAG file, \#26.11.  The value passed in must match

                           the NAME field, \#.01, and is a free text value. 

   VARIABLES:  Input     DGCAT

                           Optional File category value.  This value is either

                           "N" to lookup the pointer value in the National

                           file, or "L" to lookup the pointer value in the

                           PRF Local file.  If null, both the National and

                           Local files will be checked for the pointer value. 

   VARIABLES:  Output    DGRSLT

                           Returns one of the following values:

                              IEN;DGPF(National or Local File number,  i.e.

                           1;DGPF(26.11,

                            

                           Will return "-1;NOT FOUND"  If no flag is found

                           matching the test

                                       "-1;NOT ACTIVE" If the flag is not

                           currently active. 

           KEYWORDS:

#### DGPFAPIH

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><p>GETINF^DGPFAPIH (Increment 1)</p>
<p>DGPFAPIH is both a Routine and API / Integration agreement (# 4903)</p></th>
<th><p>DGPFAPIH - This routine implements the two Application Programming Interface call points for retrieving Patient Record Flag information. One call point is for a specific patient and record and the second call point is for a list of patients with a specific, active, Patient Record Flag.</p>
<p>This API will obtain the Patient Record Flag assignment information and status for the specified patient, patient record flag and date range. The return data will be provided in an array using the target_root specified by the user or in the default array variable DGPFAPI1. The DATE/TIME field (#.02) of the PRF ASSIGNMENT HISTORY File (#26.14) entry will determine whether the entry falls within the specified date range. If no date range is specified, all entries will be returned</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GETLST^DGPFAPIH (Increment 1)</td>
<td>This API will retrieve a list of patients active at some point within a specified date range for a specified Patient Record Flag. The date range is required for this API, though the same date can be entered to specify a single date. The return data will be provided in an array using the target_root specified by the user or in the default array variable DGPFAPI2. The DATE/TIME field (#.02) of the PRF ASSIGNMENT HISTORY File (#26.14) entry will determine whether the entry falls within the specified date range.</td>
</tr>
</tbody>
</table>

#### DGPFAPIU

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>DGPFAPIU (Increment 1)</th>
<th><p>This routine provides support utilities and functions for the new Application Programming Interface calls.</p>
<p>This procedure will check if the Patient Record Flag was active at any point during the specified date range. The procedure accepts a date range parameter which specifies whether “A”ll dates or only a “S”pecified date range is to be checked.</p>
<p>The PRF Assignment History File (#26.14) was not designed for this type of date interaction so the algorithm in this procedure has to make a number of assumptions when interpreting the dates and PRF actions. While there can only be one “New Assignment” entry, it is possible to have multiple “Continue”, “Inactivate” and “Reactivate” action entries. In addition, the “Entered In Error” action can pose additional issues with determining a status during a specific date range. See Appendix B for examples of date range and PRF History status entries.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GETFLAG^DGPFAPIU (Increment 1)</td>
<td><p>This function gets the variable pointer value for the Patient Record Flag passed in. The PRF is passed in as a text value. If the optional flag category is passed in, only that category will be checked for the PRF. If no category is passed in, then first the National category will be checked,</p>
<p>In the integration Agreement # 5491</p></td>
</tr>
</tbody>
</table>

## VAUTOMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAUTOMA is a routine which will do a one/many/all prompt - returning the chosen values in a subscripted variable specified by the calling programmer.

<u>INPUT VARIABLES:</u>

VAUTSTR string which describes what is to be entered.

VAUTNI defines if array is sorted alphabetically or numerically.

VAUTVB name of the subscripted variable to be returned.

VAUTNALL define this variable if you do not want the user to be given the ALL option.

Other variables as required by a call to ^DIC (see VA FileMan Programmers Manual).

<u>OUTPUT VARIABLES:</u>

As defined in VAUTVB

## VAFMON

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAFMON is a routine which will return income or dependent information on a patient.

<u>\$\$INCOME^VAFMON(PARM 1,PARM 2)</u>

PARM 1 The internal entry of the PATIENT file.

PARM 2 The date the income is calculated for.

<u>\$\$DEP^VAFMON(PARM 1,PARM 2)</u>

PARM 1 - The internal entry of the PATIENT file.

PARM 2 - The date the income is calculated for.

## AIT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the Ambulatory Care Reporting Project Interface Toolkit. The AIT is a set of programmer tools that provide access to outpatient encounter data.

# How To Generate On-Line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes some of the various methods by which users may secure PIMS technical documentation.

On-line technical documentation pertaining to the PIMS software, in addition to that which is located in the help prompts and on the help screens which are found throughout the PIMS package, may be generated through utilization of several KERNEL options.

These include but are not limited to: XINDEX, Menu Management Inquire Option File, Print Option File, and FileMan List File Attributes.

Entering question marks at the "Select ... Option:" prompt may also provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option. Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each.

Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for that option.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the VISTA Kernel Reference Manual.

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to VISTA Programming Standards. The XINDEX output may include the following components: compiled list of errors and warnings, routine listing, local variables, global variables, naked globals, label references, and external references.

By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from VISTA Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the PIMS package, specify the following namespaces at the "routine(s) ?\>" prompt: DG\*, DPT\*, SD\*, VA\*, SC\*.

PIMS initialization routines which reside in the UCI in which XINDEX is being run, compiled template routines, and local routines found within the PIMS namespaces should be omitted at the "routine(s) ?\>" prompt.

To omit routines from selection, preface the namespace with a minus sign (-).

## INQUIRE TO OPTION FILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Menu Manager option provides the following information about a specified option(s): option name, menu text, option description, type of option, and lock (if any). In addition, all items on the menu are listed for each menu option.

To secure information about PIMS options, the user must specify the name or namespace of the option(s) desired. Below is a list of namespaces associated with the PIMS package.

- DG - Registration, ADT, Means Test, PTF/RUG
- DPT - Patient File Look-up, Patient Sensitivity
- SD and SC - Scheduling
- VA - Generic utility processing

## PRINT OPTIONS FILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This utility generates a listing of options from the OPTION file. The user may choose to print all of the entries in this file or may elect to specify a single option or range of options.

To obtain a list of PIMS options, the following option namespaces should be specified: DG to DGZ, SD to SDZ.

## LIST FILE ATTRIBUTES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates.

In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates.

## Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### General Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routines that generate statistics for AMIS or NPCDB workload should NOT be locally modified.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps to obtain information about the security keys contained in the PIMS package.

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: SECURITY KEY

4\. Sort by: Name

5\. Start with name:

- DG to DGZ, VA to VAZ (ADT)
- SD to SDZ, SC to SCZ (scheduling)

6\. Within name, sort by: \<RET\>

7\. First print field: Name

8\. Then print field: Description

### Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PIMS software package makes use of Current Procedural Terminology (CPT) codes that is an American Medical Association (AMA) copyrighted product. Its use is governed by the terms of the agreement between the Department of Veterans Affairs and the AMA. The CPT copyright notice is displayed for various PIMS users and should not be turned off.

## FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of recommended FileMan Access Codes associated with each file contained in the PIMS package. This list may be used to assist in assigning users appropriate FileMan Access Codes.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><strong>FILEMAN ACCESS CODES</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>PATIENT</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="odd">
<td>5</td>
<td>STATE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>8</td>
<td>ELIGIBILITY CODE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>8.1</td>
<td>MAS ELIGIBILITY CODE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>8.2</td>
<td>IDENTIFICATION FORMAT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>10</td>
<td>RACE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>11</td>
<td>MARITAL STATUS</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>13</td>
<td>RELIGION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>21</td>
<td>PERIOD OF SERVICE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>22</td>
<td>POW PERIOD</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>23</td>
<td>BRANCH OF SERVICE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>25</td>
<td>TYPE OF DISCHARGE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>26.11</td>
<td>PRF LOCAL FLAG</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>26.12</td>
<td>PRF LOCAL FLAG HISTORY</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>26.13</td>
<td>PRF ASSIGNMENT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>26.14</td>
<td>PRF ASSIGNMENT HISTORY</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 30%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><strong>FILEMAN ACCESS CODES</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>26.15</td>
<td>PRF NATIONAL FLAG</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>26.16</td>
<td>PRF TYPE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>26.17</td>
<td>PRF HL7 TRANSMISSION LOG</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>26.18</td>
<td>PRF PARAMETERS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>26.19</td>
<td>PRF HL7 QUERY LOG</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>26.21</td>
<td>PRF HL7 EVENT</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>27.11</td>
<td>PATIENT ENROLLMENT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>27.12</td>
<td>ENROLLMENT QUERY LOG</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>27.14</td>
<td><p>ENROLLMENT/ELIGIBILITY</p>
<p>UPLOAD AUDIT</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>27.15</td>
<td>ENROLLMENT STATUS</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>27.16</td>
<td>ENROLLMENT GROUP THRESHOLD</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>27.17</td>
<td>CATASTROPHIC DISABILITY REASONS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>28.11</td>
<td>NOSE AND THROAT RADIUM HISTORY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>29.11</td>
<td>MST HISTORY</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>30</td>
<td>DISPOSITION LATE REASON</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">FILEMAN ACCESS CODES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>35</td>
<td>OTHER FEDERAL AGENCY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>35.1</td>
<td>SHARING AGREEMENT CATEGORY</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>35.2</td>
<td>SHARING AGREEMENT SUB-CATEGORY</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>37</td>
<td>DISPOSITION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>38.1</td>
<td>DG SECURITY LOG</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="odd">
<td>38.5</td>
<td>INCONSISTENT DATA</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>38.6</td>
<td>INCONSISTENT DATA ELEMENTS</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>39.1</td>
<td>EMBOSSED CARD TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>39.2</td>
<td>EMBOSSING DATA</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>39.3</td>
<td>EMBOSSER EQUIPMENT FILE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>39.4</td>
<td>ADT/HL7 TRANSMISSION</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>39.6</td>
<td>VIC REQUEST</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>39.7</td>
<td>VIC HL7 TRANSMISSION LOG</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">FILEMAN ACCESS CODES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>40.7</td>
<td>CLINIC STOP</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>40.8</td>
<td>MEDICAL CENTER DIVISION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>40.9</td>
<td>LOCATION TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>41.1</td>
<td>SCHEDULED ADMISSION</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="even">
<td>41.41</td>
<td>PRE-REGISTRATION AUDIT</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="odd">
<td>41.42</td>
<td>PRE-REGISTRATION CALL LIST</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="even">
<td>41.43</td>
<td>PRE-REGISTRATION CALL LOG</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="odd">
<td>41.9</td>
<td>CENSUS</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>42</td>
<td>WARD LOCATION</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="odd">
<td>42.4</td>
<td>SPECIALTY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>42.5</td>
<td>WAIT LIST</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="odd">
<td>42.55</td>
<td>PRIORITY GROUPING</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>42.6</td>
<td>AMIS 334-341</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="odd">
<td>42.7</td>
<td>AMIS 345&amp;346</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="even">
<td>43</td>
<td>MAS PARAMETERS</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>43.1</td>
<td>MAS EVENT RATES</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="even">
<td>43.11</td>
<td>MAS AWARD</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">FILEMAN ACCESS CODES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>43.4</td>
<td>VA ADMITTING REGULATION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>43.5</td>
<td>G&amp;L CORRECTIONS</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="even">
<td>43.61</td>
<td>G&amp;L TYPE OF CHANGE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>43.7</td>
<td>ADT TEMPLATE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>44</td>
<td>HOSPITAL LOCATION</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="odd">
<td>45</td>
<td>PTF</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>45.1</td>
<td>SOURCE OF ADMISSION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>45.2</td>
<td>PTF TRANSFERRING FACILITY</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="even">
<td>45.3</td>
<td>SURGICAL SPECIALTY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>45.4</td>
<td>PTF DIALYSIS TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>45.5</td>
<td>PTF MESSAGE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>45.6</td>
<td>PLACE OF DISPOSITION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>45.61</td>
<td>PTF ABUSED SUBSTANCE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>45.64</td>
<td>PTF AUSTIN ERROR CODES</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>45.68</td>
<td>FACILITY SUFFIX</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>45.7</td>
<td>FACILITY TREATING SPECIALTY</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="even">
<td>45.81</td>
<td>STATION TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">FILEMAN ACCESS CODES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>45.82</td>
<td>CATEGORY OF BENEFICIARY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>45.83</td>
<td>PTF RELEASE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>45.84</td>
<td>PTF CLOSE OUT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>45.85</td>
<td>CENSUS WORKFILE</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>45.86</td>
<td>PTF CENSUS DATE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>45.87</td>
<td>PTF TRANSACTION REQUEST LOG</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>45.88</td>
<td>PTF EXPANDED CODE CATEGORY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>45.89</td>
<td>PTF EXPANDED CODE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>45.9</td>
<td>PAF</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="odd">
<td>45.91</td>
<td>RUG-II</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>46</td>
<td>INPATIENT CPT</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>#</td>
<td>@</td>
</tr>
<tr class="odd">
<td>46.1</td>
<td>INPATIENT POV</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>#</td>
<td>@</td>
</tr>
<tr class="even">
<td>47</td>
<td>MAS FORMS AND SCREENS</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>#</td>
<td>@</td>
</tr>
<tr class="odd">
<td>48</td>
<td>MAS RELEASE NOTES</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>48.5</td>
<td>MAS MODULE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">FILEMAN ACCESS CODES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>389.9</td>
<td>STATION NUMBER (TIME SENSITIVE)</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>390</td>
<td>ENROLLMENT RATED DISABILITY UPLOAD AUDIT</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>391</td>
<td>TYPE OF PATIENT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>391.1</td>
<td>AMIS SEGMENT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>391.31</td>
<td>HOME TELEHEALTH PATIENT</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>403.35</td>
<td>SCHEDULING USER PREFERENCE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>403.43</td>
<td>SCHEDULING EVENT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>403.44</td>
<td>SCHEDULING REASON</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>403.46</td>
<td>STANDARD POSITION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>403.47</td>
<td>TEAM PURPOSE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>404.41</td>
<td>OUTPATIENT PROFILE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.42</td>
<td>PATIENT TEAM ASSIGNMENT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>404.43</td>
<td>PATIENT TEAM POSITION ASSIGNMENT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.44</td>
<td>PCMM PARAMETER</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">FILEMAN ACCESS CODES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>404.45</td>
<td>PCMM SERVER PATCH</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.46</td>
<td>PCMM CLIENT PATCH</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>404.471</td>
<td>PCMM HL7 TRANSMISSION LOG</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.472</td>
<td>PCMM HL7 ERROR LOG</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>404.48</td>
<td>PCMM HL7 EVENT</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.49</td>
<td>PCMM HL7 ID</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>404.51</td>
<td>TEAM</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.52</td>
<td>POSITION ASSIGNMENT HISTORY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>404.53</td>
<td>PRECEPTOR ASSIGNMENT HISTORY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.56</td>
<td>TEAM AUTOLINK</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>404.57</td>
<td>TEAM POSITION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.58</td>
<td>TEAM HISTORY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>404.59</td>
<td>TEAM POSITION HISTORY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.61</td>
<td>MH PCMM STOP CODES</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>404.91</td>
<td>SCHEDULING PARAMETER</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.92</td>
<td>SCHEDULING REPORT DEFINITION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">FILEMAN ACCESS CODES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>404.93</td>
<td>SCHEDULING REPORT FIELDS DEFINITION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.94</td>
<td>SCHEDULING REPORT GROUP</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>404.95</td>
<td>SCHEDULING REPORT QUERY TEMPLATE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>404.98</td>
<td>SCHEDULING CONVERSATION SPECIFICATION TEMPLATE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>405</td>
<td>PATIENT MOVEMENT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>405.1</td>
<td>FACILITY MOVEMENT TYPE</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="even">
<td>405.2</td>
<td>MAS MOVEMENT TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>405.3</td>
<td>MAS MOVEMENT TRANSACTION TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>405.4</td>
<td>ROOM-BED</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="odd">
<td>405.5</td>
<td>MAS OUT-OF-SERVICE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>405.6</td>
<td>ROOM-BED DESCRIPTION</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="odd">
<td>406.41</td>
<td>LODGING REASON</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="even">
<td>407.5</td>
<td>LETTER</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">FILEMAN ACCESS CODES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>407.6</td>
<td>LETTER TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>407.7</td>
<td>TRANSMISSION ROUTERS</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>408</td>
<td>DISCRETIONARY WORKLOAD</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>408.11</td>
<td>RELATIONSHIP</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>408.12</td>
<td>PATIENT RELATION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>408.13</td>
<td>INCOME PERSON</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>408.21</td>
<td>INDIVIDUAL ANNUAL INCOME</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>408.22</td>
<td>INCOME RELATION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>408.31</td>
<td>ANNUAL MEANS TEST</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>408.32</td>
<td>MEANS TEST STATUS</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>408.33</td>
<td>TYPE OF TEST</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>408.34</td>
<td>SOURCE OF INCOME TEST</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>408.41</td>
<td>MEANS TEST CHANGES</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>408.42</td>
<td>MEANS TEST CHANGES TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>409.1</td>
<td>APPOINTMENT TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>409.2</td>
<td>CANCELLATION REASONS</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">FILEMAN ACCESS CODES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>409.41</td>
<td>OUTPATIENT CLASSIFICATION TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>409.42</td>
<td>OUTPATIENT CLASSIFICATION</td>
<td>@</td>
<td>d</td>
<td>D</td>
<td>D</td>
<td>D</td>
</tr>
<tr class="even">
<td>409.45</td>
<td>OUTPATIENT CLASSIFICATION STOP CODE EXCEPTION</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>409.62</td>
<td>APPOINTMENT GROUP</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>409.63</td>
<td>APPOINTMENT STATUS</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>409.64</td>
<td>QUERY OBJECT</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>409.65</td>
<td>APPOINTMENT STATUS UPDATE LOG</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>409.66</td>
<td>APPOINTMENT TRANSACTION TYPE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>409.67</td>
<td>CLINIC GROUP</td>
<td>@</td>
<td></td>
<td>D</td>
<td>@</td>
<td>D</td>
</tr>
<tr class="odd">
<td>409.68</td>
<td>OUTPATIENT ENCOUNTER</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>409.73</td>
<td>TRANSMITTED OUTPATIENT ENCOUNTER</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">FILEMAN ACCESS CODES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FILE</p>
<p>NUMBER</p></td>
<td><p>FILE</p>
<p>NAME</p></td>
<td><p>DD</p>
<p>ACCESS</p></td>
<td><p>RD</p>
<p>ACCESS</p></td>
<td><p>WR</p>
<p>ACCESS</p></td>
<td><p>DEL</p>
<p>ACCESS</p></td>
<td><p>LAYGO</p>
<p>ACCESS</p></td>
</tr>
<tr class="even">
<td>409.74</td>
<td>DELETED OUTPATIENT ENCOUNTER</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>409.75</td>
<td>TRANSMITTED OUTPATIENT ENCOUNTER ERROR</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>409.76</td>
<td>TRANSMITTED OUTPATIENT ENCOUNTER ERROR CODE</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>409.77</td>
<td>ACRP TRANSMISSION HISTORY</td>
<td>@</td>
<td>d</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>409.91</td>
<td>ACRP REPORT TEMPLATE</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>409.92</td>
<td>ACRP REPORT TEMPLATE PARAMETER</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

# VADPT Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VADPT is a utility routine designed to provide a central point where a programmer can obtain information concerning a patient's record. Supported entry points are provided which will return demographics, inpatient status, eligibility information, etc.

Access to patient information is not limited to using the supported entry points in VADPT. Integration agreements can be established through the DBA between PIMS and other packages to reference information. Additionally, several data elements are supported without an integration agreement.

## SUPPORTED REFERENCES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following references to patient information (PATIENT file \#2) are supported without an integration agreement. All nationally distributed cross-references on these fields are also supported.

| FIELD NAME                | FIELD \#  | GLOBAL LOCATION | TYPE OF ACCESS |
|---------------------------|-----------|-----------------|----------------|
| NAME                      | (#.01)    | 0;1             | Read           |
| SEX                       | (#.02)    | 0;2             | Read           |
| DATE OF BIRTH             | (#.03)    | 0;3             | Read           |
| AGE                       | (#.033)   | N/A             | Read           |
| MARITAL STATUS            | (#.05)    | 0;5             | Read           |
| RACE                      | (#.06)    | 0;6             | Read           |
| OCCUPATION                | (#.07)    | 0;7             | Read           |
| RELIGIOUS PREFERENCE      | (#.08)    | 0;8             | Read           |
| DUPLICATE STATUS          | (#.081)   | 0;18            |                |
| PATIENT MERGED TO         | (#.082)   | 0;19            |                |
| CHECK FOR DUPLICATE       | (#.083)   | 0;20            |                |
| SOCIAL SECURITY NUMBER    | (#.09)    | 0;9             | Read           |
| REMARKS                   | (#.091)   | 0;10            | Read           |
| PLACE OF BIRTH \[CITY\]   | (#.092)   | 0;11            | Read           |
| PLACE OF BIRTH \[STATE\]  | (#.093)   | 0;12            | Read           |
| WHO ENTERED PATIENT       | (#.096)   | 0;15            | Read           |
| DATE ENTERED INTO FILE    | (#.097)   | 0;16            | Read           |
| WARD LOCATION             | (#.1)     | .1;1            | Read           |
| ROOM-BED                  | (#.101)   | .101;1          | Read           |
| CURRENT MOVEMENT          | (#.102)   | .102;1          | Read           |
| TREATING SPECIALTY        | (#.103)   | .103;1          | Read           |
| PROVIDER                  | (#.104)   | .104;1          | Read           |
| ATTENDING PHYSICIAN       | (#.1041)  | .1041;1         | Read           |
| CURRENT ADMISSION         | (#.105)   | .105;1          | Read           |
| LAST DMMS EPISODE NUMBER  | (#.106)   | .106;1          | Read           |
| LODGER WARD LOCATION      | (#.107)   | .107;1          | Read           |
| CURRENT ROOM              | (#.108)   | .108;1          | Read           |
| CONFIDENTIAL PHONE NUMBER | (#.1315)  | .1315           | Read           |
| CURRENT MEANS TEST STATUS | (#.14)    | 0;14            | Read           |
| DATE OF DEATH             | (#.351)   | .35;1           | Read           |
| DEATH ENTERED BY          | (#.352)   | .35;2           | Read           |
| PRIMARY LONG ID           | (#.363)   | .36;3           |                |
| PRIMARY SHORT ID          | (#.364)   | .36;4           |                |
| CURRENT PC PRACTITIONER   | (#404.01) | PC;1            | Read           |
| CURRENT PC TEAM           | (#404.02) | PC;2            | Read           |
| LAST MEANS TEST           | (#999.2)  | N/A             | Read           |

## CALLABLE ENTRY POINTS IN VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### DEM^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This entry point returns demographic information for a patient.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAPTYP This optional variable can be set to the internal number of a patient eligibility. The variable can be used to indicate the patient's type such as VA, DOD, or IHS through the eligibility. If this variable is not defined or the eligibility does not exist, the VA patient IDs will be returned.

VAHOW This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VADM(1) would be VADM("NM"))

2 -- return the output in the ^UTILITY global with numeric subscripts (e.g., ^UTILITY("VADM",\$J,1))

12 -- return the output in the ^UTILITY global with alpha subscripts (e.g., ^UTILITY("VADM",\$J,"NM"))

VAROOT This optional variable can be set to a local variable or global name in which to return the output. (e.g., VAROOT="DGDEM")

OUTPUT:

VADM(1) The NAME of the patient. (e.g., ADTPATIENT,ONE)

VADM(2) The SOCIAL SECURITY NUMBER of the patient in internal^external format.

(e.g., 000456789^000-45-6789)

VADM(3) The DATE OF BIRTH of the patient in internal^external format.

(e.g., 2551025^OCT 25,1955)

VADM(4) The AGE of the patient as of today, unless a date of death exists, in which case the age returned will be as of that date. (e.g., 36)

VADM(5) The SEX of the patient in internal^external format. (e.g., M^MALE)

VADM(6) The DATE OF DEATH of the patient, should one exist, in internal^external format.

(e.g., 2881101.08^NOV 1,1988@08:00)

VADM(7) Any REMARKS concerning this patient which may be on file. (e.g., Need to obtain dependent info.)

VADM(8) The RACE of the patient in internal^external format. (e.g., 1^WHITE,NON-HISPANIC)

> **NOTE:** This has been left for historical purposes only as the RACE field has been replaced by the RACE INFORMATION multiple.

VADM(9) The RELIGION of the patient in internal^external format. (e.g., 99^CATHOLIC)

VADM(10) The MARITAL STATUS of the patient in internal^external format. (e.g., 1^MARRIED)

VADM(11) Number of entries found in the ETHNICITY INFORMATION multiple. (e.g., 1)

VADM(11,1..n) Nth repetition of ETHNICITY INFORMATION for the patient in internal^external format. (e.g., 1^HISPANIC OR LATINO)

VADM(11,1..n,1) METHOD OF COLLECTION for the Nth repetition of ETHNICITY

INFORMATION for the patient in internal^external format. (e.g., 2^PROXY))

VADM(12) Number of entries found in the RACE INFORMATION multiple.

(e.g., 1)

VADM(12,1..n) Nth repetition of RACE INFORMATION for the patient in internal^external format. (e.g., 11^WHITE)

VADM(12,1..n,1) METHOD OF COLLECTION for the Nth repetition of RACE INFORMATION for the patient in internal^external format. (e.g., 2^PROXY))

VA("PID") The PRIMARY LONG ID for a patient. The format of this variable will depend on the type of patient if VAPTYP is set. (e.g., 000-45-6789)

VA("BID") The PRIMARY SHORT ID for a patient. The format of this variable will depend on the type of patient if VAPTYP is set. (e.g., 6789)

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or ^DPT(DFN,0) is not defined

### ELIG^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This entry point returns eligibility information for a patient.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAHOW This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAEL(1) would be VAEL("EL"))

2 -- return the output in the ^UTILITY global with numeric subscripts (e.g., ^UTILITY("VAEL",\$J,1))

12 -- return the output in the ^UTILITY global with alpha subscripts (e.g., ^UTILITY("VAEL",\$J,"EL"))

VAROOT This optional variable can be set to a local variable or global name in which to return the output. (e.g., VAROOT="DGELG")

OUTPUT:

VAEL(1) The PRIMARY ELIGIBILITY CODE of the patient in internal^external format. (e.g., 1^SERVICE CONNECTED 50-100%)

VAEL(1,#) An array of other PATIENT ELIGIBILITIES to which the patient is entitled to care, in internal^external format. The \# sign represents the internal entry number of the eligibility in the ELIGIBILITY CODE file. (e.g., 13^PRISONER OF WAR)

VAEL(2) The PERIOD OF SERVICE of the patient in internal^external format.

(e.g., 19^WORLD WAR I)

VAEL(3) If the SERVICE CONNECTED? field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If service connected, the SERVICE CONNECTED PERCENTAGE field will be returned in the second piece. (e.g., 1^70)

VAEL(4) If the VETERAN (Y/N)? field is YES, a "1" will be returned; otherwise, a "0" will be returned. (e.g., 1)

VAEL(5) If an INELIGIBLE DATE exists, a "0" will be returned indicating the patient is ineligible; otherwise, a "1" will be returned. (e.g., 0)

VAEL(5,1) If ineligible, the INELIGIBLE DATE of the patient in internal^external format. (e.g., 2880101^JAN 1,1988)

VAEL(5,2) If ineligible, the INELIGIBLE TWX SOURCE in internal^external format.

(e.g., 2^REGIONAL OFFICE)

VAEL(5,3) If ineligible, the INELIGIBLE TWX CITY. (e.g., ALBANY)

VAEL(5,4) If ineligible, the INELIGIBLE TWX STATE from which the ineligible notification was received in internal^external format.

(e.g., 36^NEW YORK)

VAEL(5,5) If ineligible, the INELIGIBLE VARO DECISION. (e.g., UNABLE TO VERIFY)

VAEL(5,6) If ineligible, the INELIGIBLE REASON. (e.g., NO DD214)

VAEL(6) The TYPE of patient in internal^external format. (e.g., 1^SC VETERAN)

VAEL(7) The CLAIM NUMBER of the patient. (e.g., 123456789)

VAEL(8) The current ELIGIBILITY STATUS of the patient in internal^external format. (e.g., V^VERIFIED)

VAEL(9) The CURRENT MEANS TEST STATUS of the patient CODE^

NAME. (e.g., A^MEANS TEST EXEMPT)

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or

^DPT(DFN,0) is not defined

### MB^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This entry point returns monetary benefit information for a patient.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAHOW This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAMB(1) would be VAMB("AA"))

2 -- return the output in the ^UTILITY global with numeric subscripts

(e.g., ^UTILITY("VAMB",\$J,1))

12 -- return the output in the ^UTILITY global with alpha subscripts

(e.g., ^UTILITY("VAMB",\$J,"AA"))

VAROOT This optional variable can be set to a local variable or global name in which to return the output. (e.g., VAROOT="DGMB")

OUTPUT:

VAMB(1) If the RECEIVING A&A BENEFITS? field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving A&A benefits, the TOTAL ANNUAL VA CHECK AMOUNT will be returned in the second piece. (e.g., 1^1000)

VAMB(2) If the RECEIVING HOUSEBOUND BENEFITS? field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving housebound benefits, the TOTAL ANNUAL VA CHECK AMOUNT will be returned in the second piece. (e.g., 1^0)

VAMB(3) If the RECEIVING SOCIAL SECURITY field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving social security, the AMOUNT OF SOCIAL SECURITY will be returned in the second piece. (e.g., 0)

VAMB(4) If the RECEIVING A VA PENSION? field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving a VA pension, the TOTAL ANNUAL VA CHECK AMOUNT will be returned in the second piece. (e.g., 1^563.23)

VAMB(5) If the RECEIVING MILITARY RETIREMENT? field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving military retirement, the AMOUNT OF MILITARY RETIRE-MENT will be returned in the second piece. (e.g., 0)

VAMB(6) The RECEIVING SUP. SECURITY (SSI) field is being eliminated. Since v5.2, a "0" is returned for this variable.

VAMB(7) If the RECEIVING VA DISABILITY? field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving VA disability, the TOTAL ANNUAL VA CHECK AMOUNT will be returned in the second piece. (e.g., 0)

VAMB(8) If the TYPE OF OTHER RETIRE-MENT field is filled in, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving other retirement, the AMOUNT OF OTHER RETIREMENT will be returned in the second piece. (e.g., 1^2500.12)

VAMB(9) If the GI INSURANCE POLICY? field is YES, a "1" will be returned in the first piece; otherwise, a "0" will be returned. If receiving GI insurance, the AMOUNT OF GI INSURANCE will be returned in the second piece. (e.g., 1^100000)

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or

^DPT(DFN,0) is not defined

### SVC^VADPT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This entry point returns service information for a patient.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAHOW This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VASV(1) would be

VASV("VN")) 2 -- return the output in the ^UTILITY global with numeric subscripts (e.g., ^UTILITY("VASV",\$J,1))

12 -- return the output in the ^UTILITY global with alpha subscripts (e.g., ^UTILITY("VASV",\$J,"VN"))

VAROOT This optional variable can be set to a local variable or global name in which to return the output. (e.g., VAROOT="DGSVC")

OUTPUT:

VASV(1) If the VIETNAM SERVICE

INDICATED field is YES, a "1" will be returned; otherwise a "0" will be returned. (e.g., 0)

VASV(1,1) If Vietnam Service, the VIETNAM

FROM DATE in internal^external format. (e.g., 2680110^JAN 10,1968)

VASV(1,2) If Vietnam Service, the VIETNAM TO DATE in internal^external format.

(e.g., 2690315^MAR 15,1969)

VASV(2) If the AGENT ORANGE EXPOS. INDICATED field is YES, a "1" will be returned; otherwise a "0" will be returned. (e.g., 0)

VASV(2,1) If Agent Orange exposure, the AGENT ORANGE REGISTRATION DATE in internal^external format.

(e.g., 2870513^MAY 13,1987)

VASV(2,2) If Agent Orange exposure, the AGENT ORANGE EXAMINATION DATE in internal^external format.

(e.g., 2871101^NOV 1,1987)

VASV(2,3) If Agent Orange exposure, AGENT ORANGE REPORTED TO C.O. date in internal^external format.

(e.g., 2871225^DEC 25,1987)

VASV(2,4) If Agent Orange exposure, AGENT ORANGE REGISTRATION \#.

(e.g., 123456)

VASV(2,5) If Agent Orange exposure, the AGENT ORANGE EXPOSURE LOCATION in

internal^external format

(e.g., V^VIETNAM)

VASV(3) If the RADIATION EXPOSURE INDICATED field is YES, a "1" will be returned; otherwise a "0" will be returned (e.g., 0)

VASV(3,1) If Radiation Exposure, RADIATION REGISTRATION DATE in internal^external format.

(e.g., 2800202^FEB 02,1980)

VASV(3,2) If Radiation Exposure, RADIATION EXPOSURE METHOD in internal^external format.

(e.g., T^NUCLEAR TESTING)

VASV(4) If the POW STATUS INDICATED field is YES, a "1" will be returned; otherwise a "0" will be returned.

(e.g., 0)

VASV(4,1) If POW status, POW FROM DATE in internal^external format.

(e.g., 2450319^MAR 19,1945)

VASV(4,2) If POW status, POW TO DATE in internal^external format.

(e.g., 2470101^JAN 1,1947)

VASV(4,3) If POW status, POW CONFINEMENT LOCATION in internal^external format.

(e.g., 2^WORLD WAR II - EUROPE)

VASV(5) If the COMBAT SERVICE INDICATED field is YES, a "1" will be returned; otherwise a "0" will be returned. (e.g., 0)

VASV(5,1) If combat service, COMBAT FROM DATE in internal^external format.

(e.g., 2430101^JAN 1,1943)

VASV(5,2) If combat service, COMBAT TO DATE in internal^external format.

(e.g., 2470101^JAN 1,1947)

VASV(5,3) If combat service, COMBAT SERVICE LOCATION in internal^external format.

(e.g., 2^WORLD WAR II - EUROPE)

VASV(6) If a SERVICE BRANCH \[LAST\] field is indicated, a "1" will be returned in the first piece; otherwise a "0" will be returned. (e.g., 0)

VASV(6,1) If service branch, BRANCH OF SERVICE field in internal^external format. (e.g., 3^AIR FORCE)

VASV(6,2) If service branch, SERVICE NUMBER field in internal^external

format. (e.g., 123456789)

VASV(6,3) If service branch, SERVICE DISCHARGE TYPE in internal^external format.

(e.g., 1^HONORABLE)

VASV(6,4) If service branch, SERVICE ENTRY DATE in internal^external format.

(e.g., 2440609^JUN 9,1944)

VASV(6,5) If service branch, SERVICE SEPARATION DATE in internal^external format.

(e.g., 2480101^JAN 1,1948)

VASV(6,6) If service branch, SERVICE COMPONENT in internal code^external format.

(e.g., R^REGULAR)

VASV(7) If a SERVICE SECOND EPISODE field is indicated, a "1" will be returned; otherwise a "0" will be returned. (e.g., 0)

VASV(7,1) If second episode, BRANCH OF SERVICE field in internal^external format. (e.g., 3^AIR FORCE)

VASV(7,2) If second episode, SERVICE NUMBER field in internal^external format. (e.g., 123456789)

VASV(7,3) If second episode, SERVICE DISCHARGE TYPE in internal^external format.

(e.g., 1^HONORABLE)

VASV(7,4) If second episode, SERVICE ENTRY DATE in internal^external format.

(e.g., 2440609^JUN 9,1944)

VASV(7,5) If second episode, SERVICE SEPARATION DATE in internal^external format.

(e.g., 2480101^JAN 1,1948)

VASV(7,6) If second episode, SERVICE COMPONENT in

internal^external format.

(e.g., R^REGULAR)

VASV(8) If a SERVICE THIRD EPISODE field is indicated, a "1" will be returned; otherwise a "0" will be returned. (e.g., 0)

VASV(8,1) If third episode, BRANCH OF SERVICE field in internal^external format. (e.g., 3^AIR FORCE)

VASV(8,2) If third episode, SERVICE NUMBER field in internal^external format.

(e.g., 123456789)

VASV(8,3) If third episode, SERVICE DIS-CHARGE TYPE in internal^external

format. (e.g., 1^HONORABLE)

VASV(8,4) If third episode, SERVICE ENTRY DATE in internal^external format.

(e.g., 2440609^JUN 9,1944)

VASV(8,5) If third episode, SERVICE SEPARATION DATE in

internal^external format.

(e.g., 2480101^JAN 1,1948)

VASV(8,6) If third episode, SERVICE COMPONENT in

internal code^external format.(e.g., R^REGULAR)

VASV(9) If the CURRENT PH INDICATOR field is YES, a “1” will be returned;

otherwise a “0” will be returned (e.g., 0)

VASV(9,1) If the CURRENT PH INDICATOR field is YES, CURRENT PURPLE

HEART STATUS in internal^external format.(e.g., 2^IN PROCESS)

VASV(9,2) If the CURRENT PH INDICATOR field is NO, CURRENT PURPLE

HEART REMARKS in internal^external format. (e.g., 5^VAMC)

VASV(10) Is either 1 or 0, 1 if there is a value for Combat Vet End Date, 0 if not

VASV(10,1) Internal Combat Vet End Date ^external Combat Vet End Date

(e.g., 3060101^JAN 1, 2006)

VASV(11) the \# of OIF conflict entries found for the veteran in the SERVICE \[OEF OR OIF\] \#2.3215 SUB-FILE.

\[n = 1-\> total number of OIF conflict entries\]

VASV(11,n,1) SERVICE LOCATION ( \#2.3215; .01) internal code=1^external (e.g., 1^OIF) ‘n’--\> This number will be used to provide a unique number for each OIF or a conflict being returned.

VASV(11,n,2) OEF/OIF FROM DATE ( \#2.3215; .02) internal format ^external format (e.g.,

3060101^JAN 1, 2006) ‘n’--\> This number will be used to provide a unique number for each OIF conflict being returned.

VASV(11,n,3) OEF/OIF TO DATE ( \#2.3215; .03) internal format ^external format (e.g., 3060101^MAR 1, 2006) ‘n’--\> This number will be used to provide a unique number for each OIF conflict being returned.

VASV(12) the \# of OEF conflict entries found for the veteran in the SERVICE \[OEF OR OIF\] \#2.3215 SUB-FILE. \[n = 1-\>VASV(12)\]

VASV(12,n,1) SERVICE LOCATION ( \#2.3215; .01) internal code = 2 ^external

(e.g., 2^OEF) ‘n’--\> This number will be used to provide a unique number for each OEF conflict being returned.

VASV(12,n,2) OEF/OIF FROM DATE ( \#2.3215; .02) internal format ^external format (e.g., 3060101^JAN 1, 2006) ‘n’--\> This number will be used to provide a unique number for each OEF conflict being returned.

VASV(12,n,3) OEF/OIF TO DATE ( \#2.3215; .03) internal format ^external format (e.g., 3060101^MAR 1, 2006) ‘n’--\> This number will be used to provide a unique number for each OEF conflict being returned.

VASV(13) the \# of UNKNOWN OEF/OIF conflict entries found for the veteran in the SEVICE \[OEF OR OIF\] \#2.3215 SUB-FILE. \[n = 1-\>VASV(13)\]

VASV(13,n,1) SERVICE LOCATION ( \#2.3215; .01) internal CODE = 3^external format (e.g., 3^UNKNOWN OEF/OIF) ‘n’--\> This number will be used to provide a unique number for each UNKNOWN OEF/OIF conflict being returned.

VASV(13,n,2) OEF/OIF FROM DATE ( \#2.3215; .02) internal format ^external format (e.g., 3060101^JAN 1, 2006) ‘n’--\> This number will be used to provide a unique number for each UNKNOWN OEF/OIF conflict being returned.

VASV(13,n,3) OEF/OIF TO DATE ( \#2.3215; .03) internal format ^external format (e.g., 3060101^MAR 1, 2006) ‘n’--\> This number will be used to provide a unique number for each UNKNOWN OEF/OIF conflict being returned.

VASV(14) If the PROJ 112/ SHAD field is populated, a "1" will be returned; otherwise, a "0" will be returned (e.g., 0)

VASV(14,1) If the PROJ 112/SHAD field is populated, PROJ 112/SHAD in internal^external format. (e.g., 1^YES)

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or

^DPT(DFN,0) is not defined

### ADD^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This entry point returns address data for a patient. If a temporary address is in effect, the data returned will be that pertaining to that temporary address; otherwise, the permanent patient address information will be returned.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAHOW This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAPA(1) would be VAPA("L1"))

2 -- return the output in the ^UTIL-ITY global with numeric subscripts (e.g., ^UTILITY(“VAPA”, \$J,1))

12 -- return the output in the ^UTILITY global with alpha subscripts (e.g., ^UTILITY("VAPA",\$J,"L1"))

VAROOT This optional variable can be set to a local variable or global name in which to return the output.(e.g., VAROOT="DGADD")

VAPA("P") This optional variable can be set to force the return of the patient's permanent address. The permanent address array will be returned regardless of whether or not a temporary address is in effect.

(e.g., VAPA("P")="")

VAPA("CD") This is an optional input parameter set to an effective date in VA File Manager format to manipulate the active/inactive status returned in the VAPA(12) node. The indicator reflects the active status as of the date specified or the current date if VAPA("CD") is undefined.

VATEST("ADD",9) This optional variable can be defined to a beginning date in VA File-Manager format. If the entire range specified is not within the effective time window of the temporary address start and stop dates, the patient's regular address is returned. (e.g., VATEST("ADD",9)=2920101)

VATEST("ADD",10) This optional variable can be defined to a ending date in VA FileManager format. If the entire range specified is not within the effective time window of the temporary address start and stop dates, the patient's regular address is returned. (e.g., VATEST("ADD",10)=2920301)

OUTPUT:

VAPA(1) The first line of the STREET ADDRESS.

(e.g., 123 South Main Street)

VAPA(2) The second line of the STREET ADDRESS. (e.g., Apartment \#1245.)

VAPA(3) The third line of the STREET ADDRESS. (e.g., P.O. Box 1234)

VAPA(4) The CITY corresponding to the street address previously indicated. (e.g., ALBANY)

VAPA(5) The STATE corresponding to the city previously indicated in internal^external format.

(e.g., 6^CALIFORNIA)

VAPA(6) The ZIP CODE of the city previously indicated. (e.g., 12345)

VAPA(7) The COUNTY in which the patient is residing in internal^external format.

(e.g., 1^ALAMEDA)

VAPA(8) The PHONE NUMBER of the location in which the patient is currently residing. (e.g., (123) 456-7890)

VAPA(9) If the address information provided pertains to a temporary address, the TEMPORARY ADDRESS START DATE in internal^external format.

(e.g., 2880515^MAY 15,1988)

VAPA(10) If the address information provided pertains to a temporary address, the TEMPORARY ADDRESS END DATE in internal^external format. (e.g., 2880515^MAY 15,1988)

VAPA(11) The ZIP+4 (5 or 9 digit zip code) of the city previously indicated in internal^external format. (e.g., 123454444^12345-4444)

VAPA(12) Confidential Address Active indicator. (O=Inactive 1=Active)

VAPA(13) The first line of the Confidential Street Address.

VAPA(14) The second line of the Confidential Street Address.

VAPA(15) The third line of the Confidential Street Address.

VAPA(16) The city for the Confidential Address.

VAPA(17) The state for the Confidential Address in internal^external format. (e.g., 36^NEW YORK)

VAPA(18) The 5 digit or 9 digit Zip Code for the Confidential Address in internal^external format. (e.g., 12208^12208 or 122081234^12208-1234)

VAPA(19) The county for the Confidential Address in internal^external format. (e.g., 1^ALBANY)

VAPA(20) The start date for the Confidential Address in internal^external format. (e.g., 3030324^MAR 24,2003)

VAPA(21) The end date for the Confidential Address in internal^external format. (e.g., 3030624^JUN 24,2003)

VAPA(22,N) The Confidential Address Categories in internal^external format^status (n=internal value) (e.g., VAPA(22,4)=4^MEDICAL RECORDS^Y)

VAPA(23) The Permanent or Temporary Province (if temp address is current

and active, it’s temp)

VAPA(24) The Permanent or Temporary Postal Code (if temp address is current and active, it's temp)

VAPA(25) The Permanent or Temporary Country (if temp address is current and active, it's temp)

VAPA(26) The Confidential Province

VAPA(27) The Confidential Postal Code

VAPA(28) The Confidential Country

VAPA(29) The Confidential Phone Number

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or

^DPT(DFN,0) is not defined

### OAD^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This entry point returns other specific address information.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAHOW This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAOA(1) would be VAOA("L1"))

2 -- return the output in the ^UTILITY global with numeric subscripts

(e.g., ^UTILITY("VAOA",\$J,1))

12 -- return the output in the ^UTILITY global with alpha subscripts

(e.g., ^UTILITY("VAOA,\$J,"L1")

VAROOT This optional variable can be set to a local variable or global name in which to return the output. (e.g., VAROOT="DGOA")

VAOA("A") This optional variable may be passed to indicate which specific address the programmer wants returned. If it is not defined, the PRIMARY NEXT-OF-KIN will be returned. Otherwise, the following will be returned based on information desired.

VAOA("A") =1 primary emergency contact

VAOA("A") =2 designee for personal effects

VAOA("A") =3 secondary next-of-kin

VAOA("A") =4 secondary emergency contact

VAOA("A") =5 patient employer

VAOA("A") =6 spouse's employer

OUTPUT:

VAOA(1) The first line of the STREET ADDRESS.

(e.g., 123 South First Street)

VAOA(2) The second line of the STREET ADDRESS. (e.g., Apartment 9D)

VAOA(3) The third line of the STREET ADDRESS. (e.g., P.O. Box 1234)

VAOA(4) The CITY in which the contact/employer resides.(e.g., NEWINGTON)

VAOA(5) The STATE in which the contact/employer resides in internal^external format. (e.g., 6^CALIFORNIA)

VAOA(6) The ZIP CODE of the location in which the contact/employer resides.

(e.g., 12345)

VAOA(7) The COUNTY in which the contact/employer resides in internal^external format. (e.g., 1^ALAMEDA)

VAOA(8) The PHONE NUMBER of the contact/employer.

(e.g., (415) 967-1234)

VAOA(9) The NAME of the contact or, in case of employment, the employer to whom this address information applies. (e.g., SMITH,ROBERT P.)

VAOA(10) The RELATIONSHIP of the contact (if applicable) to the patient; otherwise, null. (e.g., FATHER)

VAOA(11) The ZIP+4 (5 or 9 digit zip code) of the location in which the contact/employer resides in internal^external format. (e.g., 123454444^12345-4444)

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or

^DPT(DFN,0) is not defined

### INP^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This entry point will return data related to an inpatient episode.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAHOW This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAIN(1) would be VAIN("AN"))

2 -- return the output in the ^UTILITY global with numeric subscripts

(e.g., ^UTILITY("VAIN",\$J,1))

12 -- return the output in the ^UTILITY global with alpha subscripts

(e.g., ^UTILITY("VAIN,\$J,"AN")

VAROOT This optional variable can be set to a local variable or global name in which to return the output.(e.g., VAROOT="DGIN")

VAINDT This optional variable may be set to a past date/time for which the programmer wishes to know the patient's inpatient status. This must be passed as an internal VA FileManager date/time format. If time is not passed, it will assume anytime during that day. If this variable is not defined, it will assume now as the date/time. (e.g., 2880101.08)

Output: VAIN(1) The INTERNAL NUMBER \[IFN\] of the admission if one was found for the date/time requested. If no inpatient episode was found for the date/time passed, then all variables in the VAIN array will be returned as null.(e.g., 123044)

VAIN(2) The PRIMARY CARE PHYSICIAN \[PROVIDER\] assigned to the patient at the date/time requested in internal^external format.(e.g., 3^SMITH,JOSEPH L.)

VAIN(3) The TREATING SPECIALTY assigned to the patient at the date/time requested in internal^external format.(e.g., 19^GERIATRICS)

VAIN(4) The WARD LOCATION to which the patient was assigned at the date/time requested in internal^external format.(e.g., 27^IBSICU)

VAIN(5) The ROOM-BED to which the patient was assigned at the date/time requested in external format.(e.g., 123-B)

VAIN(6) This will return a "1" in the first piece if the patient is in a bed status; otherwise, a "0" will be returned. A non-bed status is made based on the last transfer type to a non-bed status, (i.e., authorized absence, unauthorized absence, etc.) The second piece will contain the name of the last transfer type should one exist.(e.g., 1^FROM AUTHORIZED ABSENCE)

VAIN(7) The ADMISSION DATE/TIME for the patient in internal^external format.

(e.g., 2870213.0915^FEB 13,1987@09:15)

VAIN(8) The ADMISSION TYPE for the patient in internal^external format.

(e.g., 3^DIRECT)

VAIN(9) The ADMITTING DIAGNOSIS for the patient. (e.g., PSYCHOSIS)

VAIN(10) The internal entry number of the PTF record corresponding to this admission. (e.g., 2032)

VAIN(11) The ATTENDING PHYSICIAN in internal^external format.

(e.g., 25^ADTPROVIDER,ONE)

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or^DPT(DFN,0) is not defined

### IN5^VADPT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This entry point will return data related to an inpatient episode.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAHOW This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAIP(1) would be VAIP("MN"))

2 -- return the output in the ^UTILITY

global with numeric subscripts

(e.g., ^UTILITY("VAIP",\$J,1))

12 -- return the output in the ^UTILITY global with alpha subscripts

(e.g., ^UTILITY("VAIP",\$J,"MN")

VAROOT This optional variable can be set to a local variable or global name in which to return the output.(e.g., VAROOT="DGI5")

VAIP("D") This optional variable can be defined as follows.

VAIP("D") =VA FileManager date in internal format. If the patient was an inpatient at the date/time passed, movement data pertaining to that date/time will be returned.

VAIP("D") ="LAST" Movement data pertaining to the last movement on file, regardless if patient is a current inpatient.

VAIP("D") =valid date without time Will return movement data if patient was an inpatient at any time during the day on the date that was passed in.

VAIP("D") - not passed Will return movement data if the patient was in inpatient based on "now".

VAIP("L") This optional variable, when passed, will include lodgers movements in the data. (e.g., VAIP("L")="")

VAIP("V") Can be defined as the variable used instead of VAIP (e.g., VAIP("V")="SD")

VAIP("E") This optional variable is defined as the internal file number of a specific movement. If this is defined, VAIP("D") is ignored.

(e.g., VAIP("E")=123445)

VAIP("M") This optional variable can be passed as a "1" or a "0" (or null).

VAIP("M")=0 - The array returned will be based on the admission movement associated with the movement date/time passed.

VAIP("M")=1 - The array returned will be based on the last movement associated with the date/time passed.

OUTPUT:

VAIP(1) The INTERNAL FILE NUMBER

\[IFN\] of the movement found for the specified date/time. (e.g., 231009)

VAIP(2) The TRANSACTION TYPE of the movement in internal^external format where:

1=admission

2=transfer

3=discharge

4=check-in lodger

5=check-out lodger

6=specialty transfer

(e.g., 3^DISCHARGE)

VAIP(3) The MOVEMENT DATE/TIME in internal^external date format.

(e.g., 2880305.09^MAR 5,1988@09:00)

VAIP(4) The TYPE OF MOVEMENT in internal^external format.

(e.g., 4^INTERWARD TRANSFER)

VAIP(5) The WARD LOCATION to which patient was assigned with that movement in internal^external format. (e.g., 32^1B-SURG)

VAIP(6) The ROOM-BED to which the patient was assigned with that movement in internal^external format. (e.g., 88^201-01)

VAIP(7) The PRIMARY CARE PHYSICIAN assigned to the patient in internal^external format. (e.g., 3^ADTPROVIDER,TEN)

VAIP(8) The TREATING SPECIALTY assigned with that movement in internal^external format. (e.g., 98^OPTOMETRY)

VAIP(9) The DIAGNOSIS assigned with that movement. (e.g., UPPER GI BLEEDING)

VAIP(10) This will return a "1" in the first piece if the patient is in a bed status; otherwise, a "0" will be returned. A non-bed status is made based on the last transfer type, if one exists, and a transfer to a non-bed status, (i.e., authorized absence, unauthorized absence, etc.) The second piece will contain the name of the last transfer type should one exist. (e.g., 1^FROM AUTHORIZED ABSENCE)

VAIP(11) If patient is in an absence status on the movement date/time, this will return the EXPECTED RETURN DATE from absence in internal^external format.

(e.g., 2880911^SEP 11,1988)

VAIP(12) The internal entry number of the PTF record corresponding to this admission. (e.g., 2032)

VAIP(13) The INTERNAL FILE NUMBER of the admission associated with this movement. (e.g., 200312)

VAIP(13,1) The MOVEMENT DATE/TIME in internal^external format.

(e.g., 2881116.08^NOV 16,1988@08:00)

VAIP(13,2) The TRANSACTION TYPE in internal^external format.

(e.g., 1^ADMISSION)

VAIP(13,3) The MOVEMENT TYPE in internal^external format.

(e.g., 15^DIRECT)

VAIP(13,4) The WARD LOCATION associated with this patient with this movement in internal^external format.(e.g., 5^7BSCI)

VAIP(13,5) The PRIMARY CARE PHYSICIAN assigned to the patient for this movement in internal^external format. (e.g., 16^JONES, CHARLES C)

VAIP(13,6) The TREATING SPECIALTY for the patient for this movement in internal^external format.(e.g., 3^NEUROLOGY)

VAIP(14) The INTERNAL FILE NUMBER of the last movement associated with this movement.

(e.g., 187612)

VAIP(14,1) The MOVEMENT DATE/TIME in internal^external format.(e.g., 2881116.08^NOV 16,1988@08:00)

VAIP(14,2) The TRANSACTION TYPE in internal^external format.

(e.g., 2^TRANSFER)

VAIP(14,3) The MOVEMENT TYPE in internal^external format.

(e.g., 4^INTERWARD TRANSFER)

VAIP(14,4) The WARD LOCATION associated with this patient with this movement in internal^external format.

(e.g., 5^7BSCI)

VAIP(14,5) The PRIMARY CARE PHYSICIAN assigned to the patient for this movement in internal^external format.(e.g., 16^JONES, CHARLES C)

VAIP(14,6) The TREATING SPECIALTY for the patient for this movement in internal^external format.(e.g., 3^NEUROLOGY)

VAIP(15) The INTERNAL FILE NUMBER of the movement which occurred immediately prior to this one, if one exists. (e.g., 153201)

VAIP(15,1) The MOVEMENT DATE/TIME in internal^external format.

(e.g., 2881116.08^NOV 16,1988@08:00)

VAIP(15,2) The TRANSACTION TYPE in internal^external format.

(e.g., 2^TRANSFER)

VAIP(15,3) The MOVEMENT TYPE in internal^external format.

(e.g., 4^INTERWARD TRANSFER)

VAIP(15,4) The WARD LOCATION associated with this patient with this movement in internal^external format.

(e.g., 5^7BSCI)

VAIP(15,5) The PRIMARY CARE PHYSICIAN assigned to the patient for this movement in internal^external format.

(e.g., 16^ADTPROVIDER,TWO)

VAIP(15,6) The TREATING SPECIALTY for the patient for this movement in internal^external format.(e.g., 3^NEUROLOGY)

VAIP(16) The INTERNAL FILE NUMBER of the movement which occurred immediately following this one, if one exists. (e.g., 146609)

VAIP(16,1) The MOVEMENT DATE/TIME in internal^external format.

(e.g., 2881116.08^NOV 16,1988@08:00)

VAIP(16,2) The TRANSACTION TYPE ininternal^external format.

(e.g., 2^TRANSFER)

VAIP(16,3) The MOVEMENT TYPE in internal^external format.

(e.g., 4^INTERWARD TRANSFER)

VAIP(16,4) The WARD LOCATION associated with this patient with this movement in internal^external format. (e.g., 5^7BSCI)

VAIP(16,5) The PRIMARY CARE PHYSICIAN assigned to the patient for this movement in internal^external format. (e.g., 16^ADTPROVIDER,THREE)

VAIP(16,6) The TREATING SPECIALTY for the patient for this movement in internal^external format.(e.g., 3^NEUROLOGY)

VAIP(17) The INTERNAL FILE NUMBER of the discharge associated with this movement. (e.g., 1902212)

VAIP(17,1) The MOVEMENT DATE/TIME in internal^external format.(e.g., 2881116.08^NOV 16,1988@08:00)

VAIP(17,2) The TRANSACTION TYPE in internal^external format.(e.g., 3^DISCHARGE)

VAIP(17,3) The MOVEMENT TYPE in internal^external format.(e.g., 16^REGULAR)

VAIP(17,4) The WARD LOCATION associated with this patient for this movement iinternal^external format.(e.g., 5^7BSCI)

VAIP(17,5) The PRIMARY CARE PHYSICIAN assigned to the patient for this movement in internal^external format.(e.g., 16^ADTPROVIDER,ONE)

VAIP(17,6) The TREATING SPECIALTY for the patient for this movement in internal^external format. (e.g., 3^NEUROLOGY)

VAIP(18) The ATTENDING PHYSICIAN assigned to the patient for this movement in internal^external format.(e.g., 25^ADTPROVIDER,TEN)

VAIP(19,1) Will contain whether or not the patient chose to be excluded from the facility directory for the admission related to this movement in internal^external format.(e.g., 1^YES)

VAIP(19,2) Date/time answer to facility directory question was answered in internal^external format.

(e.g., 3030426.08^APR26,2003@08:00)

VAIP(19,3) User entering answer to facility directory question in internal^external format.

(e.g., 1934^ADTEMPLOYEE,ONE)

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or^DPT(DFN,0) is not defined

### OPD^VADPT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Returns other pertinent patient data which is commonly used but not contained in any other calls to VADPT.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAHOW This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array will be returned with numeric subscripts.

1 -- return the output array with alpha subscripts - see alpha subscripts section (e.g., VAPD(1) would be VAPD("BC"))

2 -- return the output in the ^UTILITY global with numeric subscripts

(e.g., ^UTILITY("VAPD",\$J,1))

12 -- return the output in the ^UTILITY global with alpha subscripts

(e.g., ^UTILITY("VAPD",\$J,"BC")

VAROOT This optional variable can be set to a local variable or global name in which to return the output.(e.g., VAROOT="DGPD")

OUTPUT:

VAPD(1) The PLACE OF BIRTH \[CITY\].

(e.g., SAN FRANCISCO)

VAPD(2) The PLACE OF BIRTH \[STATE\] in internal^external format.(e.g., 6^CALIFORNIA)

VAPD(3) The FATHER'S NAME.(e.g., ADTFATHER,ONE)

VAPD(4) The MOTHER'S NAME.(e.g., MARY)

VAPD(5) The MOTHER'S MAIDEN NAME.(e.g., ADTMOTHER,ONE)

VAPD(6) The patient's OCCUPATION.(e.g., CARPENTER)

VAPD(7) The patient's EMPLOYMENT STATUS in internal^external format.

(e.g., 4^SELF EMPLOYED)

VAPD(8) The patient's Phone Number (work)

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or

^DPT(DFN,0) is not defined

### REG^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Returns REGISTRATION/DISPOSITION data.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAROOT This optional variable can be set to a local variable or global name in which to return the output. (e.g., VAROOT="DGADD")

VARP("F") Can be defined as the "from" date for which registrations are desired. This must be passed as a valid VA File-Manager date. (e.g., VARP("F")=2930101)

VARP("T") Can be defined as the "to" date for which registrations are desired. This must be passed as a valid VA File-Manager date. If neither VARP("F") nor VARP("T") are defined, all registrations will be returned. (e.g., VARP("T")=2930530)

VARP("C") Can be defined as the number of registrations you want returned in the array.

(e.g., VARP("C")=5 - will return 5 most recent)

OUTPUT:

^UTILITY("VARP",\$J,#,"I") Internal format

^UTILITY("VARP",\$J,#,"E") External format

Piece 1 Registration Date/Time

Piece 2 Status

Piece 3 Type of Benefit applied for

Piece 4 Facility Applying to

Piece 5 Who Registered

Piece 6 Log out (disposition) date/time

Piece 7 Disposition Type

Piece 8 Who Dispositioned

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or ^DPT(DFN,0) is not defined

### SDE^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Returns ACTIVE clinic enrollments for a patient.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

OUTPUT:

^UTILITY("VAEN",\$J,#,"I") Internal format

^UTILITY("VAEN",\$J,#,"E") External format

Piece 1 Clinic Enrolled in

Piece 2 Enrollment Date

Piece 3 OPT or AC

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or ^DPT(DFN,0) is not defined

### SDA^VADPT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Returns APPOINTMENT DATE/TIME data for a patient.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VASD("T") Can be defined as the "to" date for which registrations are desired. This must be passed as a valid VA File-Manager date. If neither VASD("F") nor VASD("T") are defined, all future appointments will be returned.

VASD("F") Can be defined as the "from" date for which appointments are desired. This must be passed as a valid VA File-Manager date. If not defined, it is assumed only future appointments should be returned.

VASD("W") Can be passed as the specific STATUS desired in the following format. If not passed, only those appointments which are still scheduled (or kept in the event of a past date) for both inpatients and outpatients will be returned.

If VASD("W")

Contains a These appts. are returned

1 Active/Kept

2 Inpatient appts. only

3 No-shows

4 No-shows, auto-rebook

5 Cancelled by Clinic

6 Cancelled by Clinic, auto rebook

7 Cancelled by Patient

8 Cancelled by Patient,

auto rebook

9 No action taken

VASD("C", Clinic IFN)Can be set up to contain only those internal file entries from the HOSPITAL LOCATION file for clinics which you would like to see appointments for this particular patient.

You may define this array with just one clinic or with many. If you do not define this variable, it will be assumed that you want appointments for this patient in all clinics returned.

OUTPUT:

^UTILITY("VASD",\$J,#,"I") Internal format

^UTILITY("VASD",\$J,#,"E") External format

Piece 1 Date/Time of Appointment

Piece 2 Clinic

Piece 3 Status

Piece 4 Appointment Type

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or

^DPT(DFN,0) is not defined

### PID^VADPT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This call is used to obtain the patient identifier in long and brief format.

INPUT:

DFN This required variable is the internal

entry number in the PATIENT file.

VAPTYP This optional variable can be set to the internal number of a patient eligibility. The variable can be used to indicate the patient's type such as VA, DOD, or IHS through the eligibility. If this variable is not defined or the eligibility does not exist, the VA patient IDs will be returned.

OUTPUT:

VA("PID") The long patient identifier.

(e.g., 000-22-3333P)

VA("BID") The short patient identifier. (e.g., 3333P)

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or

^DPT(DFN,0) is not defined

### PID^VADPT6 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This call returns the same variables as the call mentioned above, but will eliminate the unnecessary processing time required calling PID^VADPT.

### ADM^VADPT2 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This returns the internal file number of the admission movement. If VAINDT is not defined, this will use "NOW" for the date/time.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file.

VAINDT This optional variable may be set to a past date/time for which the programmer wishes to know the patient's inpatient status. This must be passed as an internal VA FileManager date/time format.

(e.g., 2880101.08)

OUTPUT:

VADMVT Returns the internal file number of the admission movement.

VAERR The error flag will have one of the following values.

0 -- no errors encountered

1 -- error encountered - DFN or ^DPT(DFN,0) is not defined

### KVAR^VADPT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This call is used to remove all variables defined by the VADPT routine. The programmer should elect to utilize this call to remove the arrays which were returned by VADPT.

### KVA^VADPT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This call is used as above and will also kill the VA("BID") and VA("PID") variables.

### COMBINATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following calls may be made to return a combination of arrays with a single call.

INPUT:

DFN This required variable is the internal entry number in the PATIENT file. See specific call for other variable input

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Output:</strong></th>
<th><blockquote>
<p><strong>DEMOGRAPHIC</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ELIGIBILITY</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>INPATIENT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>INPATIENT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ADDRESS</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>SERVICE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>MONETARY</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>REGISTRATION</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ENROLLMENT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>APPOINTMENT</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CALL</strong></td>
<td><blockquote>
<p><strong>VADM</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VAEL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VAIN</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VAIP</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VAPA</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VASV</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VAMB</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>UTILITY("VARP"</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>UTILITY("VAEN"</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>UTILITY("VASD"</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>OERR</td>
<td>X</td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1</td>
<td>X</td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>X</td>
<td>X</td>
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
<td>3</td>
<td></td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>4</td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>8</td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>9</td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td>10</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td>51</td>
<td>X</td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>52</td>
<td></td>
<td>X</td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>53</td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ALL</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td>A5</td>
<td>X</td>
<td>X</td>
<td></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td>X</td>
</tr>
</tbody>
</table>

## Alpha Subscripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| CALL       | VARIABLE  | ALPHA TRANSLATION |
|------------|-----------|-------------------|
| DEM^VADPT  | VADM(1)   | VADM("NM")        |
|            | VADM(2)   | VADM("SS")        |
|            | VADM(3)   | VADM("DB")        |
|            | VADM(4)   | VADM("AG")        |
|            | VADM(5)   | VADM("SX")        |
|            | VADM(6)   | VADM("EX")        |
|            | VADM(7)   | VADM("RE")        |
|            | VADM(8)   | VADM("RA")        |
|            | VADM(9)   | VADM("RP")        |
|            | VADM(10)  | VADM("MS")        |
| ELIG^VADPT | VAEL(1)   | VAEL("EL")        |
|            | VAEL(1,#) | VAEL("EL",#)      |
|            | VAEL(2)   | VAEL("PS")        |
|            | VAEL(3)   | VAEL("SC")        |
|            | VAEL(4)   | VAEL("VT")        |
|            | VAEL(5)   | VAEL("IN")        |
|            | VAEL(5,#) | VAEL("IN",#)      |
|            | VAEL(6)   | VAEL("TY")        |
|            | VAEL(7)   | VAEL("CN")        |
|            | VAEL(8)   | VAEL("ES")        |
|            | VAEL(9)   | VAEL("MT")        |

| CALL      | VARIABLE  | ALPHA TRANSLATION |
|-----------|-----------|-------------------|
| MB^VADPT  | VAMB(1)   | VAMB("AA")        |
|           | VAMB(2)   | VAMB("HB")        |
|           | VAMB(3)   | VAMB("SS")        |
|           | VAMB(4)   | VAMB("PE")        |
|           | VAMB(5)   | VAMB("MR")        |
|           | VAMB(6)   | VAMB("SI")        |
|           | VAMB(7)   | VAMB("DI")        |
|           | VAMB(8)   | VAMB("OR")        |
|           | VAMB(9)   | VAMB("GI")        |
| SVC^VADPT | VASV(1)   | VASV("VN")        |
|           | VASV(1,#) | VASV("VN",#)      |
|           | VASV(2)   | VASV("AO")        |
|           | VASV(2,#) | VASV("AO",#)      |
|           | VASV(3)   | VASV("IR")        |
|           | VASV(3,#) | VASV("IR",#)      |
|           | VASV(4)   | VASV("PW")        |
|           | VASV(4,#) | VASV("PW",#)      |
|           | VASV(5)   | VASV("CS")        |
|           | VASV(5,#) | VASV("CS",#)      |
|           | VASV(6)   | VASV("S1")        |

| CALL | VARIABLE   | ALPHA TRANSLATION |
|------|------------|-------------------|
|      | VASV(6,#)  | VASV("S1",#)      |
|      | VASV(7)    | VASV("S2")        |
|      | VASV(7,#)  | VASV("S2",#)      |
|      | VASV(8)    | VASV("S3")        |
|      | VASV(8,#)  | VASV("S3",#)      |
|      | VASV(9)    | VASV(“PH”)        |
|      | VASV(9,#)  | VASV(“PH”,#)      |
|      | VASV(10)   | VASV(“CV”)        |
|      | VASV(10,#) | VASV(“CV”,#)      |
|      | VASV(11)   | VASV(“OIF”)       |
|      | VASV(11,#) | VASV(“OIF”,#)     |
|      | VASV(12)   | VASV(“OEF”)       |
|      | VASV(12,#) | VASV(“OEF”,#)     |
|      | VASV(13)   | VASV(“UNK”)       |
|      | VASV(13,#) | VASV(“UNK”,#)     |
|      | VASV(14)   | VASV(“SHD”)       |
|      | VASV(14,#) | VASV(“SHD”,#)     |

| CALL      | VARIABLE | ALPHA TRANSLATION |
|-----------|----------|-------------------|
| ADD^VADPT | VAPA(1)  | VAPA("L1")        |
|           | VAPA(2)  | VAPA("L2")        |
|           | VAPA(3)  | VAPA("L3")        |
|           | VAPA(4)  | VAPA("CI")        |
|           | VAPA(5)  | VAPA("ST")        |
|           | VAPA(6)  | VAPA("ZP")        |
|           | VAPA(7)  | VAPA("CO")        |
|           | VAPA(8)  | VAPA("PN")        |
|           | VAPA(9)  | VAPA("TS")        |
|           | VAPA(10) | VAPA("TE")        |
|           | VAPA(11) | VAPA("Z4")        |
|           | VAPA(12) | VAPA(“CCA”)       |
|           | VAPA(13) | VAPA(“CL1”)       |
|           | VAPA(14) | VAPA(“CL2”)       |
|           | VAPA(15) | VAPA(“CL3”)       |
|           | VAPA(16) | VAPA(“CCI”)       |
|           | VAPA(17) | VAPA(“CST”)       |
|           | VAPA(18) | VAPA(“CZP”)       |
|           | VAPA(19) | VAPA(“CCO”)       |
|           | VAPA(20) | VAPA(“CCS”)       |
|           | VAPA(21) | VAPA(“CCE”)       |
|           | VAPA(22) | VAPA(“CTY”)       |
|           | VAPA(23) | VAPA(“PR”)        |

| CALL      | VARIABLE | ALPHA TRANSLATION |
|-----------|----------|-------------------|
|           | VAPA(24) | VAPA(“PC”)        |
|           | VAPA(25) | VAPA(“CT”)        |
|           | VAPA(26) | VAPA(“CPR”)       |
|           | VAPA(27) | VAPA(“CPC”)       |
|           | VAPA(28) | VAPA(“CCT”)       |
|           | VAPA(29) | VAPA(“CPN”)       |
| OAD^VADPT | VAOA(1)  | VAOA("L1")        |
|           | VAOA(2)  | VAOA("L2")        |
|           | VAOA(3)  | VAOA("L3")        |
|           | VAOA(4)  | VAOA("CI")        |
|           | VAOA(5)  | VAOA("ST")        |
|           | VAOA(6)  | VAOA("ZP")        |
|           | VAOA(7)  | VAOA("CO")        |
|           | VAOA(8)  | VAOA("PN")        |
|           | VAOA(9)  | VAOA("NM")        |
|           | VAOA(10) | VAOA("RE")        |
|           | VAOA(11) | VAOA("Z4")        |
| INP^VADPT | VAIN(1)  | VAIN("AN")        |
|           | VAIN(2)  | VAIN("DR")        |
|           | VAIN(3)  | VAIN("TS")        |

| CALL      | VARIABLE | ALPHA TRANSLATION |
|-----------|----------|-------------------|
|           | VAIN(4)  | VAIN("WL")        |
|           | VAIN(5)  | VAIN("RB")        |
|           | VAIN(6)  | VAIN("BS")        |
|           | VAIN(7)  | VAIN("AD")        |
|           | VAIN(8)  | VAIN("AT")        |
|           | VAIN(9)  | VAIN("AF")        |
|           | VAIN(10) | VAIN("PT")        |
|           | VAIN(11) | VAIN("AP")        |
| IN5^VADPT | VAIP(1)  | VAIP("MN")        |
|           | VAIP(2)  | VAIP("TT")        |
|           | VAIP(3)  | VAIP("MD")        |
|           | VAIP(4)  | VAIP("MT")        |
|           | VAIP(5)  | VAIP("WL")        |
|           | VAIP(6)  | VAIP("RB")        |
|           | VAIP(7)  | VAIP("DR")        |
|           | VAIP(8)  | VAIP("TS")        |
|           | VAIP(9)  | VAIP("MF")        |
|           | VAIP(10) | VAIP("BS")        |
|           | VAIP(11) | VAIP("RD")        |
|           | VAIP(12) | VAIP("PT")        |

| CALL      | VARIABLE   | ALPHA TRANSLATION |
|-----------|------------|-------------------|
|           | VAIP(13)   | VAIP("AN")        |
|           | VAIP(13,#) | VAIP("AN",#)      |
|           | VAIP(14)   | VAIP("LN")        |
|           | VAIP(14,#) | VAIP("LN",#)      |
|           | VAIP(15)   | VAIP("PN")        |
|           | VAIP(15,#) | VAIP("PT",#)      |
|           | VAIP(16)   | VAIP("NN")        |
|           | VAIP(16,#) | VAIP("NN",#)      |
|           | VAIP(17)   | VAIP("DN")        |
|           | VAIP(17,#) | VAIP("DN",#")     |
|           | VAIP(18)   | VAIP("AP")        |
| OPD^VADPT | VAPD(1)    | VAPD("BC")        |
|           | VAPD(2)    | VAPD("BS")        |
|           | VAPD(3)    | VAPD("FN")        |
|           | VAPD(4)    | VAPD("MN")        |
|           | VAPD(5)    | VAPD("MM")        |
|           | VAPD(6)    | VAPD("OC")        |
|           | VAPD(7)    | VAPD("ES")        |
|           | VAPD(8)    | VAPD("WP")        |

# Scheduling Application Programmer Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scheduling functions and data that support outpatient scheduling are being re-engineered and re-hosted as a Government Off-the-Shelf (GOTS) application. During implementation, the appointment data currently stored in the Patient sub-file (2.98) and the Hospital Location sub-files (44.001, 44.003) have been moved into an Enterprise Oracle database on an external platform.

The API released in an implementing patch is one of several that provide the only authorized interface to appointment data. It is designed to retrieve appointments from either data source: VistA or the Oracle database.

Existing direct global references to Scheduling globals, as well as FileManager calls in all M-based applications, must be removed or redesigned. There are several possible options described below:

1)  Remove. Eliminate uses of appointment data whenever possible. Access to appointment data over the network may be slower than direct access in VistA. For example, if the application displays patient appointments as a convenience feature, the display could be removed from the function because the user can get the same information directly using the Scheduler Graphical User Interface (GUI). Keeping the display in the application may become an inconvenience feature when the network is slow or unavailable. This strategy emphasizes application un-coupling in preparation for a future Clinical Context Object Workgroup (CCOW)-based application environment.
2)  Replace. If the appointment data are required to support the business processes of the application, one of the encapsulation APIs must be used to interface the application with the new Resource Scheduling System. The look and feel of the application will remain the same although retrieval times may be slower.
    1.  Data Layer. To optimize an application process that uses appointments, it is important to call the API only once during process execution. In most cases to achieve this it will be necessary to use the API to create a data layer. The API is called once and stores the data in a temporary global. Business processing does not start until after all the required data are retrieved in the ‘data layer’.
    2.  Error Handling. As the data is retrieved from a remote database, errors could occur which may be returned to applications; therefore, it is also important to design error handling. If this is implemented now, it will not be necessary to add it later when the data is retrieved from the remote database.

### Special Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the special features of the Scheduling Replacement API "SDAPI" that retrieves appointment information stored in sub-files 2.98, 44.001, and 44.003. Appointment data can be retrieved by patient(s), clinic(s), both, or neither. Three other appointment fields are available for filtering. See “SDAPI - Filters” for a complete list of available appointment filters.

This API is an encapsulation API and has special features.

- Flexibility. This API can be implemented now without re-programming later because it will retrieve the same information from either database (FM globals or SQL tables). Each field in the table below has been assigned an independent identifying number that is used in the input parameter of the API. See “SDAPI - Data Fields” for a more detailed list of the available data fields.

| 1   | APPOINTMENT DATE/TIME                  |
|-----|----------------------------------------|
| 2   | CLINIC IEN and NAME                    |
| 3   | APPOINTMENT STATUS                     |
| 4   | PATIENT DFN and NAME                   |
| 5   | LENGTH OF APPOINTMENT                  |
| 6   | COMMENTS                               |
| 7   | OVERBOOK                               |
| 8   | ELIGIBILITY OF VISIT IEN and NAME      |
| 9   | CHECK-IN DATE/TIME                     |
| 10  | APPOINTMENT TYPE IEN and NAME          |
| 11  | CHECK-OUT DATE/TIME                    |
| 12  | OUTPATIENT ENCOUNTER IEN               |
| 13  | PRIMARY STOP CODE IEN and CODE         |
| 14  | CREDIT STOP CODE IEN and CODE          |
| 15  | WORKLOAD NON-COUNT                     |
| 16  | DATE APPOINTMENT MADE                  |
| 17  | DESIRED DATE OF APPOINTMENT            |
| 18  | PURPOSE OF VISIT and SHORT DESCRIPTION |
| 19  | EKG DATE/TIME                          |
| 20  | X-RAY DATE/TIME                        |
| 21  | LAB DATE/TIME                          |
| 22  | STATUS                                 |
| 23  | X-RAY FILMS                            |
| 24  | AUTO-REBOOKED APPOINTMENT DATE/TIME    |
| 25  | NO-SHOW/CANCEL DATE/TIME               |
| 26  | RSA APPOINTMENT ID                     |
| 28  | DATA ENTRY CLERK DUZ AND NAME          |
| 29  | NO-SHOW/CANCELED BY DUZ AND NAME       |
| 30  | CHECK-IN USER DUZ AND NAME             |
| 31  | CHECK-OUT USER DUZ AND NAME            |
| 32  | CANCELLATION REASON IEN AND NAME       |
| 33  | CONSULT LINK                           |

> **NOTE:** Field 27 is reserved for the 2507 Request IEN to be available in a future release.

Error Code 101. The API returns error code 101 when the network is too slow or is down. Applications that depend upon information stored in an external database must be re-programmed to handle this condition. Without network error handling, applications may either hang indefinitely or error out. At this point, there is one error code to indicate a network problem. See “SDAPI - Error Codes” for a complete list of all API error codes.

Error Code 116. The API returns error code 116 when the data returned from the RSA database doesn't match the data on VistA. An example of this would be if the RSA returns an IEN that doesn't exist on VistA. Applications must be re-programmed to handle this condition. See “SDAPI - Error Codes” for a complete list of all API error codes.

Error Code 117. The API returns error code 117 when the other error codes don’t apply. This error code will incorporate any additional errors that may be included or returned in the future. Adding this error code will prevent re-coding of current applications, as these new error codes are introduced. See “SDAPI - Error Codes” for a complete list of all API error codes.

External Data Source. The API is designed to be used with an external database. The API pulls over all the data required by the application function in one request and stores it in a temporary global. The temporary global can then be used in place of the Hospital Location sub-files (44.001, 44.003) and the Patient sub-file (2.98) to perform the business logic of the application, separating the data layer from the business layer. See the example below.

Example: The process of encapsulation will involve, in part, replacing direct global references in routines with APIs. As an example, consider the following piece of code. This code is designed to retrieve appointment date/time, patient DFN and name, and length of appointment for all DGCLN clinic appointments up to DGLAST date.

F S DGDATE=\$O(^SC(DGCLN,"S",DGDATE)) Q:'DGDATE!(DGDATE\>DGLAST) D

. S DGAPT=0 F S DGAPT=\$O(^SC(DGCLN,"S",DGDATE,1,DGAPT)) Q:'DGAPT D

. . S DGPAT=\$P(^SC(DGCLN,"S",DGDATE,1,DGAPT,0),U,1)

. . I \$G(DGPAT) S DGPATNAM=\$P(^DPT(DGPAT,0),U,1))

. . S DGLOAPPT=\$P(^SC(DGCLN,"S",DGDATE,1,DGAPT,0),U,2)

CONTINUE PROCESSING AS NEEDED

Using the API, the code may be changed as follows:

> ;DATA LAYER

> S DGARRAY(1)=";"\_DGLAST

> S DGARRAY("FLDS")="1;4;5"

> S DGARRAY(2)=DGCLN

> S DGCNT=\$\$SDAPI^SDAMA301(.DGARRAY)

> ;BUSINESS LAYER

> ; if data is returned, process appointment data

> I DGCNT\>0 S DGPAT=0 F S DGPAT=\$O(^TMP(\$J,”SDAMA301”,DGCLN,DGPAT)

Q:DGPAT=”” D

> . S DGDATE=0 F S DGDATE=\$O(^TMP(\$J,"SDAMA301",DGCLN,DGPAT,DGDATE)

Q:DGDATE="" D

> .. S DGLOAPPT=\$P(\$G(^TMP(\$J,”SDAMA301”,DGCLN,DGPAT,DGDATE)),U,5) ;length

of appt

> .. S DGPINFO=\$P(\$G(^TMP(\$J,”SDAMA301”,DGCLN,DGPAT,DGDATE)),U,4) ;patient

DFN and Name

> .. S DGPATNAM=\$P(DGPINFO,";",2) ;patient name

> .. continue processing appointment data as needed

> ; if error returned, process error

> I DGCNT\<0 D

> . ;check error array for DATABASE IS UNAVAILABLE error

> . I \$D(^TMP(\$J,”SDAMA301,101)) D

> .. process error as needed (calling application to determine how to

handle this)

> . ;check error array for DATA MISMATCH error

> . I \$D(^TMP(\$J,”SDAMA301,116)) D

> .. process error as needed (calling application to determine how to

handle this)

> ;kill the temporary array

> I DGCNT'=0 K ^TMP(\$J,”SDAMA301”)

Application Programmer Interface - SDAPI

Name: SDAPI ; Retrieve Filtered Appointment Data

Declaration: \$\$SDAPI^SDAMA301(.ARRAY)

Description: This API returns filtered appointment information and should be called

using an EXTRINSIC call. To use this API, subscribe to Integration Agreement \#4433.

Argument: ARRAY – An array, passed by value, that is defined and name-spaced by

the calling application, containing the following parameters:

> <u>Field List</u> Required, ARRAY("FLDS"). List of appointment field IDs requested,

> each ID separated by a semicolon or “ALL” to indicate all fields are being requested. See “SDAPI - Data Fields” for a complete list of available appointment fields and their associated IDs.

> <u>Filters</u> Optional. See “SDAPI - Filters” for a complete list of available

> appointment filters and their input array format.

> <u>Max Appts</u> Optional, ARRAY("MAX"). Maximum appointments requested. See

> “SDAPI - Filters” for a description and valid values of this array entry.

> <u>Sort</u> Optional, ARRAY(“SORT”). Allows the output to be sorted by patient

> DFN, instead of by Patient and Clinic IENs. See “SSDAPI - Filters” for a description and valid values of this array entry.

> <u>Purged</u> Optional, ARRAY(“PURGED”). Output will include non-canceled

> appointments that were purged from the Hospital Location file yet still exist on the patient file. See “SDAPI - Filters” for a description and the valid value for this array entry. If this optional array entry is passed into the API, there are 2 other conditions that must be met else error 115 will be generated: ARRAY(4) must be populated, and several fields will not be available to request because those fields are either located on the Hospital Location file (which was purged of the appointment) or are calculated using data from the Hospital Location file. Those fields are 5-9, 11, 22, 28, 30, 31, and 33. See “SDAPI - Data Fields” for a description of those fields.

RETURN VALUES:

From the extrinsic call, this API will return “-1” if an error occurred, “0” if no appointment is found that matches the filter criteria, or account of the returned appointments. If no appointment is found that matches the filter criteria, the ^TMP(\$J,”SDAMA301”) global will not be generated.

If appointments are found that match the filter criteria, fields 1 through 5 and 7 through 26 of the appointments will be returned in:

> ^TMP(\$J,”SDAMA301”,SORT1,SORT2,APPT DATE/TIME)

> =field1^field2^field3^…

> where SORT1 and SORT2 are driven by the patient filter and defined

> in the table below, and field1 is appointment data ID 1 (appt date/time)

> if requested, field2 is appointment data ID 2 (clinic IEN and name) if

> requested, etc. Note: Piece 6 will always be null, because if field 6

> (Appointment comments) is requested, the comments will appear on

> the subscript (“C”) of the global reference:

> ^TMP(\$J,”SDAMA301”,SORT1,SORT2,APPT DATE/TIME,”C”)=field 6.

> Fields 28 through 33 will be returned in:

> ^TMP(\$J,”SDAMA301”,SORT1,SORT2,APPT DATE/TIME,0) =

> field28^field29^field30^…

| Patient Filter is… | Sort Values                               |
|--------------------|-------------------------------------------|
| Populated          | SORT1 is Patient DFN, SORT2 is Clinic IEN |
| Not Populated      | SORT1 is Clinic IEN, SORT2 is Patient DFN |

In addition, there is another filter value which can be set to alter the output. If ARRAY(“SORT”)=”P”, then the output will only include the subscript Patient DFN and not Clinic IEN, overriding the Sort Values described above. IE. ^TMP(\$J,”SDAMA301”,DFN,APPT DATE/TIME)=field1^field2…

> **NOTE:** As mentioned above, field 6 will always be null and if field 6 (Appointment Comments) is requested, the comments will appear on the next subscript (“C”) of the global reference.

> IE. ^TMP(\$J,”SDAMA301”,DFN,APPT DATE/TIME,”C”)=field 6.

> If an error occurs, the error codes and messages will be returned in

> ^TMP(\$J,”SDAMA301”,error code) = error message

> See “SDAPI - Error Codes” for a list of error codes and messages.

Other: When processing has completed, kill the temporary array:

> ^TMP(\$J,”SDAMA301”)

> See “SDAPI - Constraints” for constraints.

## SDAPI - EXAMPLES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\) <u>By Clinic</u>. Get all appointments for clinic 501 on 01/05/04. Get patient DFN and name, and appointment status. Note that the output will be sorted first by clinic, then patient, then appointment date/time. Clinic is first sort because the patient filter is not populated.

N SDARRAY,SDCOUNT,SDDFN,SDDATE,SDAPPT,SDPAT,SDPATNAM,SDSTATUS

S SDARRAY(1)="3040105;3040105"

S SDARRAY(2)=501

S SDARRAY("FLDS")="4;3" order is irrelevant

S SDCOUNT=\$\$SDAPI^SDAMA301(.SDARRAY)

I SDCOUNT\>0 D

. ;get patient

. S SDDFN=0 F S SDDFN=\$O(^TMP(\$J,"SDAMA301",501,SDDFN)) Q:SDDFN="" D

. . ;get appointment date/time

. . S SDDATE=0 F S SDDATE=\$O(^TMP(\$J,"SDAMA301",501,SDDFN,SDDATE)) Q:SDDATE="" D

. . . S SDAPPT=\$G(^TMP(\$J,"SDAMA301",501,SDPATDFN,SDDATE)) ;appointment data

. . . S SDSTATUS=\$P(\$G(SDAPPT),"^",3) ;appointment status

. . . S SDPAT=\$P(\$G(SDAPPT),"^",4) ;patient DFN and Name

. . . S SDPATNAM=\$P(\$G(SDPAT),";",2) ;patient Name only

continue processing this appointment as needed

I SDCOUNT\<0 D

do processing for errors 101 and 116

when finished with all processing, kill the output array

I SDCOUNT'=0 K ^TMP(\$J,"SDAMA301")

2)<u>By Patient</u>. Get the next (after today) scheduled/regular appointment for patient 100. Get the appointment date/time, clinic IEN and name, and appointment status. Note that the output will be sorted first by patient, then clinic, then appointment date/time. Patient is first sort because it is populated.

N SDARRAY,SDCOUNT,SDCLIEN,SDDATE,SDAPPT,SDSTATUS,SDCLINFO,SDCLNAME

S SDARRAY(1)=DT\_".2359"

S SDARRAY(3)="R;I"

S SDARRAY(4)=100

S SDARRAY("MAX")=1

S SDARRAY("FLDS")="1;2;3"

S SDCOUNT=\$\$SDAPI^SDAMA301(.SDARRAY)

I SDCOUNT\>0 D

. ;get clinic

. S SDCLIEN=0 F S SDCLIEN=\$O(^TMP(\$J,"SDAMA301",100,SDCLIEN)) Q:SDCLIEN="" D

. . ; get appointment date/time

. . S SDDATE=0 F S SDDATE=\$O(^TMP(\$J,"SDAMA301",100,SDCLIEN,SDDATE)) Q:SDDATE="" D

. . . S SDAPPT=\$G(^TMP(\$J,"SDAMA301",100,SDCLIEN,SDDATE)) ;appointment data

. . . S SDSTATUS=\$P(SDAPPT,"^",3) ;appt status

. . . S SDCLINFO=\$P(SDAPPT,"^",2) ;clinic IEN and Name

. . . S SDCLNAME=\$P(SDCLINFO,";",2) ;clinic Name only

continue processing this appointment as needed

I SDCOUNT\<0 D

do processing for errors 101 and 116

when finished with all processing, kill output array

I SDCOUNT'=0 K ^TMP(\$J,"SDAMA301")

3)<u>By Patient and Clinic</u>. Get all appointments for patient 100 in clinic 501, for January 2004. Get the appointment date/time and credit stop code IEN. Note that the output will be sorted first by patient, then clinic, then appointment date/time. Patient is first sort because it is populated.

N SDARRAY,SDCOUNT,SDDATE,SDAPPT,SDCRSTOP

S SDARRAY(1)="3040101;3040131"

S SDARRAY(2)=501

S SDARRAY(4)=100

S SDARRAY("FLDS")="1;14;16"

S SDCOUNT=\$\$SDAPI^SDAMA301(.SDARRAY)

I SDCOUNT\>0 D

. ; get appointment date/time

. S SDDATE=0 F S SDDATE=\$O(^TMP(\$J,"SDAMA301",100,501,SDDATE)) Q:SDDATE="" D

. . S SDAPPT=\$G(^TMP(\$J,"SDAMA301",100,501,SDDATE)) ;appointment data

. . S SDCREDIT=\$P(SDAPPT,"^",14) ;credit stop code IEN

. . I \$G(SDCREDIT)'=";" S SDCRIEN=\$P(SDCREDIT,";",1) ;credit stop code IEN only

continue processing this appointment as needed

I SDCOUNT\<0 D

do processing for errors 101 and 116

when finished with all processing, kill output array

I SDCOUNT'=0 K ^TMP(\$J,"SDAMA301")

4)<u>By neither Patient nor Clinic</u>. Get all appointments for primary stop code 300, for January 2004. Get the appointment status. Note that the output will be sorted first by clinic, then patient, then appointment date/time. Clinic is first sort because the patient filter is not populated.

N SDARRAY,SDCOUNT,SDCLIEN,SDDFN,SDDATE,SDAPPT,SDSTATUS

S SDARRAY(1)="3040101;3040131"

S SDARRAY(13)=300

S SDARRAY(4)=100

S SDARRAY("FLDS")="3"

S SDCOUNT=\$\$SDAPI^SDAMA301(.SDARRAY)

I SDCOUNT\>0 D

. ; get clinic

. S SDCLIEN=0 F S SDCLIEN=\$O(^TMP(\$J,"SDAMA301",SDCLIEN)) Q:SDCLIEN="" D

. . ; get patient

. . S SDDFN=0 F S SDDFN=\$O(^TMP(\$J,"SDAMA301",SDCLIEN,SDDFN)) Q:SDDFN="" D

. . . ; get appointment date/time

. . . S SDDATE=0 F S SDDATE=\$O(^TMP(\$J,"SDAMA301",SDCLIEN,SDDFN,SDDATE)) Q:SDDATE="" D

. . . . S SDSTATUS=\$P(\$G(^TMP(\$J,"SDAMA301",100,501,SDDATE)),"^",3) ;appointment status

continue processing this appointment as needed

I SDCOUNT\<0 D

do processing for errors 101 and 116

when finished with all processing, kill output array

I SDCOUNT'=0 K ^TMP(\$J,"SDAMA301")

> **WARNING:** For the quickest performance, this API should be run with a patient and/or clinic filter. Omission of both filters will result in a lengthy query (time and data).

5)<u>By Clinic with “Sort” filter defined</u>.  Get all appointments for clinic 501 on 01/05/04.  Get patient DFN and name, and appointment status.  Note that the output will be sorted first by patient, then appointment date/time.  Patient is only sort because the SORT filter is populated.

N SDARRAY,SDCOUNT,SDDFN,SDDATE,SDAPPT,SDPAT,SDPATNAM,SDSTATUS

S SDARRAY(1)="3040105;3040105"

S SDARRAY(2)=501

S SDARRAY("SORT")="P"

S SDARRAY("FLDS")="4;3" order is irrelevant

S SDCOUNT=\$\$SDAPI^SDAMA301(.SDARRAY)

I SDCOUNT\>0 D

.;get patient

.S SDDFN=0 F  S SDDFN=\$O(^TMP(\$J,"SDAMA301",SDDFN)) Q:SDDFN="" D

. . ; get appointment date/time

. . S SDDATE=0 F  S SDDATE=\$O(^TMP(\$J,"SDAMA301",SDDFN,SDDATE)) Q:SDDATE="" D

. . . S SDAPPT=\$G(^TMP(\$J,"SDAMA301",SDDFN,SDDATE)) ;appointment data

. . . S SDSTATUS=\$P(\$G(SDAPPT),"^",3) ;appointment status

. . . S SDPAT=\$P(\$G(SDAPPT),"^",4) ;patient DFN and Name

. . . S SDPATNAM=\$P(\$G(SDPAT),";",2) ;patient Name only

;continue processing this appointment as needed

I SDCOUNT\<0 D

do processing for errors 101 and 116

when finished with all processing, kill the output array

I SDCOUNT'=0 K ^TMP(\$J,"SDAMA301")

6)<u>By Clinic with “Sort” filter defined</u>. Get all appointments for Clinic 501 on 01/05/04.  Get patient DFN, and name, and appointment comments.  Note that the output will be sorted first by patient, then appointment date/time, and the comments will appear on the next reference with the subscript “C”.  Patient is only sort because the SORT filter is populated.

N SDARRAY,SDCOUNT,SDDFN,SDDATE,SDAPPT,SDPAT,SDPATNAM,SDCMMNT

S SDARRAY(1)="3040105;3040105"

S SDARRAY(2)=501

S SDARRAY("SORT")="P"

S SDARRAY("FLDS")="4;6" order is irrelevant

S SDCOUNT=\$\$SDAPI^SDAMA301(.SDARRAY)

I SDCOUNT\>0 D

. ; get patient

. S SDDFN=0 F  S SDDFN=\$O(^TMP(\$J,"SDAMA301",SDDFN)) Q:SDDFN="" D

. . ; get appointment date/time

. . S SDDATE=0 F  S SDDATE=\$O(^TMP(\$J,"SDAMA301",SDDFN,SDDATE)) Q:SDDATE="" D

. . . S SDAPPT=\$G(^TMP(\$J,"SDAMA301",SDDFN,SDDATE)) ;appointment data

. . . S SDPAT=\$P(\$G(SDAPPT),"^",4) ;patient DFN and Name

. . . S SDPATNAM=\$P(\$G(SDPAT),";",2) ;patient Name only

. . . S SDCMMNT=\$G(^TMP(\$J, ,"SDAMA301",SDDFN,SDDATE,"C"))

continue processing this appointment as needed

I SDCOUNT\<0 D

do processing for errors 101 and 116

when finished with all processing, kill the output array

I SDCOUNT'=0 K ^TMP(\$J,"SDAMA301")

7) Does patient 999 have any appointments on file?

N SDARRAY,SDCOUNT

S SDARRAY(4)=999

S SDARRAY("FLDS")=1

S SDARRAY("MAX")=1

S SDCOUNT=\$\$SDAPI^SDAMA301(.SDARRAY)

I SDCOUNT\>0 D

patient has appointments on file

I SDCOUNT\<0 D

do processing for errors 101 and 116

kill output array when processing is done

I SDCOUNT'=0 K ^TMP(\$J,"SDAMA301")

8) Similar to example \#4, but with a global list of patients

N SDARRAY,SDCOUNT,SDCLIEN,SDDFN,SDDATE,SDAPPT,SDSTATUS

S SDARRAY(1)="3040101;3040131"

S SDARRAY(13)=300

S ^SDDFN(1019974)=""

S ^SDDFN(1019975)=""

S ^SDDFN(1019976)=""

S ^SDDFN(1019977)=""

S ^SDDFN(1019978)=""

S ^SDDFN(1019979)=""

S SDARRAY(4)="^SDDFN("

S SDARRAY("FLDS")="3"

S SDCOUNT=\$\$SDAPI^SDAMA301(.SDARRAY)

I SDCOUNT\>0 D

. ; get clinic

. S SDCLIEN=0 F S SDCLIEN=\$O(^TMP(\$J,"SDAMA301",SDCLIEN)) Q:SDCLIEN="" D

. . ;get patient

. . S SDDFN=0 F S SDDFN=\$O(^TMP(\$J,"SDAMA301",SDCLIEN,SDDFN)) Q:SDDFN="" D

. . . ; get appointment date/time

. . . S SDDATE=0 F S SDDATE=\$O(^TMP(\$J,"SDAMA301",SDCLIEN,SDDFN,SDDATE)) Q:SDDATE="" D

. . . . S SDSTATUS=\$P(\$G(^TMP(\$J,"SDAMA301",100,501,SDDATE)),"^",3) ;appointment status

continue processing this appointment as needed

I SDCOUNT\<0 D

do processing for errors 101 and 116

when finished with all processing, kill output array and user-defined

patient list

I SDCOUNT'=0 K ^TMP(\$J,"SDAMA301")

K ^SDDFN

## SDAPI - Data Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Available Appointment Data Fields:

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>FIELD NAME</strong></th>
<th><strong>DATA TYPE</strong></th>
<th><strong>Format/Valid Values</strong></th>
<th><strong>Description</strong></th>
<th><strong>Examples of Returned Data</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>APPOINTMENT DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>The scheduled Appointment Date/Time</td>
<td><p>3031215.113</p>
<p>3031201.0815</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>CLINIC IEN and NAME</td>
<td>TEXT</td>
<td>ID^name</td>
<td>Clinic IEN and name</td>
<td><p>150;CARDIOLOGY</p>
<p>32;BLOOD DONOR</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>APPOINTMENT STATUS</td>
<td>TEXT</td>
<td><p><strong>R (</strong>Scheduled/Kept)</p>
<p><strong>I</strong> (Inpatient)</p>
<p><strong>NS</strong> (No-Show)</p>
<p><strong>NSR</strong> (No-Show, Rescheduled)</p>
<p><strong>CP</strong> (Cancelled by Patient)</p>
<p><strong>CPR</strong> (Cancelled by Patient, Rescheduled)</p>
<p><strong>CC</strong> (Cancelled by Clinic)</p>
<p><strong>CCR</strong> (Cancelled by Clinic, Rescheduled)</p>
<p><strong>NT</strong> (No Action Taken)</p></td>
<td>The status of the appointment.</td>
<td><p>R;SCHEDULED/KEPT</p>
<p>I;INPATIENT</p>
<p>NS;N0-SHOW</p>
<p>NSR;NO-SHOW &amp; RESCHEDULED</p>
<p>CP;CANCELLED BY PATIENT</p>
<p>CPR;CANCELLED BY PATIENT &amp; RESCHEDULED</p>
<p>CC;CANCELLED BY CLINIC</p>
<p>CCR;CANCELLED BY CLINIC &amp; RESCHEDULED</p>
<p>NT;NO ACTION TAKEN</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>PATIENT DFN and NAME</td>
<td>TEXT</td>
<td>DFN;name</td>
<td>Patient DFN and Patient Name.</td>
<td><p>34877;JONES,BOB</p>
<p>455;SCHILSON,BRIAN</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>LENGTH OF APPOINTMENT</td>
<td>TEXT</td>
<td>NNN</td>
<td>The scheduled length of appointment, in minutes.</td>
<td><p>20</p>
<p>60</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>COMMENTS</td>
<td>TEXT</td>
<td>free text</td>
<td>Any comments associated with the appointment.</td>
<td><p>PATIENT NEEDS WHEELCHAIR</p>
<p><strong>Note: Comments shall be located on the “C” subscript.</strong></p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>OVERBOOK</td>
<td>TEXT</td>
<td><strong>Y</strong> or <strong>N</strong></td>
<td>“Y” if appointment is an overbook else “N”.</td>
<td><p>Y</p>
<p>N</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>ELIGIBILITY OF VISIT IEN and NAME</td>
<td>TEXT</td>
<td><strong>Local</strong> IEN; <strong>Local</strong> Name; <strong>National</strong> IEN; <strong>National</strong> Name</td>
<td>Local &amp; National Eligibility codes and names associated with the appointment.</td>
<td><p>2;AID &amp; ATTENDANCE;2;AID &amp; ATTENDANCE</p>
<p>7;ALLIED VETERAN;7;ALLIED VETERAN</p>
<p>12; COLLATERAL OF VET.; 13; COLLATERAL OF VET.</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td>CHECK-IN DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>Date/time the patient checked in for the appointment.</td>
<td>3031215.113</td>
</tr>
<tr class="even">
<td>10</td>
<td>APPOINTMENT TYPE IEN and NAME</td>
<td>TEXT</td>
<td>IEN;name</td>
<td>Type of Appointment IEN and name.</td>
<td><p>1;COMPENSATION &amp; PENSION</p>
<p>3;ORGAN DONORS</p>
<p>7; COLLATERAL OF VET.</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>CHECK-OUT DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>Date/time the patient checked out of the appointment.</td>
<td>3031215.113</td>
</tr>
<tr class="even">
<td>12</td>
<td>OUTPATIENT ENCOUNTER IEN</td>
<td>TEXT</td>
<td>NNN</td>
<td>The outpatient encounter IEN associated with this appointment.</td>
<td>4578</td>
</tr>
<tr class="odd">
<td>13</td>
<td>PRIMARY STOP CODE IEN and CODE</td>
<td>TEXT</td>
<td>IEN;code</td>
<td>Primary Stop code IEN and code associated with the clinic.</td>
<td>301;350</td>
</tr>
<tr class="even">
<td>14</td>
<td>CREDIT STOP CODE IEN and CODE</td>
<td>TEXT</td>
<td>IEN;code</td>
<td>Credit Stop code IEN and code associated with the clinic.</td>
<td>549;500</td>
</tr>
<tr class="odd">
<td>15</td>
<td>WORKLOAD NON-COUNT</td>
<td>TEXT</td>
<td><strong>Y</strong> or <strong>N</strong></td>
<td>“Y” if clinic is non-count else “N”.</td>
<td><p>Y</p>
<p>N</p></td>
</tr>
<tr class="even">
<td>16</td>
<td>DATE APPOINTMENT MADE</td>
<td>DATE</td>
<td>YYYMMDD</td>
<td>Date the appointment was entered into the Scheduling system.</td>
<td>3031215</td>
</tr>
<tr class="odd">
<td>17</td>
<td>DESIRED DATE OF APPOINTMENT</td>
<td>DATE</td>
<td>YYYMMDD</td>
<td>The date the clinician or patient desired for the scheduling of this appointment.</td>
<td>3031215</td>
</tr>
<tr class="even">
<td>18</td>
<td>PURPOSE OF VISIT</td>
<td>TEXT</td>
<td>Code (1, 2, 3, or 4) and short description (C&amp;P, 10-10, SV, or UV)</td>
<td>The Purpose of Visit.</td>
<td><p>1;C&amp;P</p>
<p>2;10-10</p>
<p>3;SV</p>
<p>4;UV</p></td>
</tr>
<tr class="odd">
<td>19</td>
<td>EKG DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>The scheduled date/time of the EKG tests in conjunction with this appointment.</td>
<td>3031215.083</td>
</tr>
<tr class="even">
<td>20</td>
<td>X-RAY DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>The scheduled date/time of the X-RAY in conjunction with this appointment.</td>
<td>3031215.083</td>
</tr>
<tr class="odd">
<td>21</td>
<td>LAB DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>The scheduled date/time of the Lab tests in conjunction with this appointment.</td>
<td>3031215.083</td>
</tr>
<tr class="even">
<td>22</td>
<td>STATUS</td>
<td>TEXT</td>
<td>Status Code, Status Description, Print Status, Checked In Date/Time, Checked Out Date/Time, and Admission Movement IFN</td>
<td>Status Information for the Visit.</td>
<td>8;INPATIENT APPOINTMENT;INPATIENT/CHECKED OUT;;3030218.1548;145844</td>
</tr>
<tr class="odd">
<td>23</td>
<td>X-RAY FILMS</td>
<td>TEXT</td>
<td><strong>Y</strong> or <strong>N</strong></td>
<td>“<strong>Y</strong>” if x-ray films are required at clinic else “<strong>N</strong>”.</td>
<td><p>Y</p>
<p>N</p></td>
</tr>
<tr class="even">
<td>24</td>
<td>AUTO-REBOOKED APPOINTMENT DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>The date/time that the appointment was Auto-Rebooked (rescheduled) to.</td>
<td>3031215.083</td>
</tr>
<tr class="odd">
<td>25</td>
<td>NO-SHOW / CANCEL DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD.HHMM</td>
<td>The date/time that the appointment was No-Showed or Cancelled.</td>
<td>3031215.083</td>
</tr>
<tr class="even">
<td>26</td>
<td>RSA APPOINTMENT ID</td>
<td>TEXT</td>
<td>NNN</td>
<td>The unique numeric Oracle ID that identifies a specific RSA appointment. This field will be null for appointments in legacy VistA.</td>
<td>34983</td>
</tr>
<tr class="odd">
<td>28</td>
<td>DATA ENTRY CLERK</td>
<td>TEXT</td>
<td>DUZ;Name</td>
<td>The DUZ and name of the clerk who scheduled the appointment.</td>
<td>24569;PERSON,NEW A</td>
</tr>
<tr class="even">
<td>29</td>
<td>NO-SHOW / CANCELED BY</td>
<td>TEXT</td>
<td>DUZ;Name</td>
<td>The DUZ and name of the clerk who no-showed or canceled the appointment.</td>
<td>24569;PERSON,NEW A</td>
</tr>
<tr class="odd">
<td>30</td>
<td>CHECK IN USER</td>
<td>TEXT</td>
<td>DUZ;Name</td>
<td>The DUZ and name of the clerk who checked in the appointment.</td>
<td>24569;PERSON,NEW A</td>
</tr>
<tr class="even">
<td>31</td>
<td>CHECK OUT USER</td>
<td>TEXT</td>
<td>DUZ;Name</td>
<td>The DUZ and name of the clerk who checked out the appointment.</td>
<td>24569;PERSON,NEW A</td>
</tr>
<tr class="odd">
<td>32</td>
<td>CANCELLATION REASON</td>
<td>TEXT</td>
<td>DUZ;Name</td>
<td>IEN and Name of Cancellation Reason.</td>
<td>11;OTHER</td>
</tr>
<tr class="even">
<td>33</td>
<td>CONSULT LINK</td>
<td>TEXT</td>
<td>NNN</td>
<td>The Consult Link IEN associated with the appointment.</td>
<td>23123</td>
</tr>
<tr class="odd">
<td colspan="6">Note: Field 27 is reserved for the 2507 Request IEN to be available in a future release.</td>
</tr>
</tbody>
</table>

## SDAPI - Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Available Data Filters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

INPUT

Six fields will allow a filter. All 6 fields can be filtered in one API call. A null/undefined filter will result in all values being returned.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 28%" />
<col style="width: 40%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>APPOINTMENT DATA TO BE FILTERED</strong></td>
<td><strong>ARRAY ENTRY</strong></td>
<td><strong>Format</strong></td>
<td><strong>Examples of M code to set array with filter values</strong></td>
</tr>
<tr class="even">
<td>APPOINTMENT DATE/TIME</td>
<td>ARRAY(1)</td>
<td><p>Range of appointment date/times, "from" and "to" date/time separated by semicolon. Dates must be FileMan format YYYMMDD.HHMMSS</p>
<p>ARRAY(1)="from date; to date"</p></td>
<td><p>S ARRAY(1)="3030101;3030101" (one day)</p>
<p>S ARRAY(1)="3040101" (appts after 2003)</p>
<p>S ARRAY(1)=";3031231" (all appts thru 3031231)</p>
<p>S ARRAY(1)=DT (all appts from today forward)</p>
<p>S ARRAY(1)=DT_";3041231" (all appts from today through 3041231)</p></td>
</tr>
<tr class="odd">
<td>CLINIC IEN</td>
<td>ARRAY(2)</td>
<td><p>List of valid clinic IENs (each separated by a semicolon) or a global root or a local root. Clinic must exist on Hospital Location file.</p>
<p>ARRAY (2) ="ien1; ien2" etc.</p>
<p>ARRAY(2)="^global("</p>
<p>ARRAY(2)="^global(#"</p>
<p>ARRAY(2)="^global(#,"</p>
<p>ARRAY(2)="local("</p>
<p>ARRAY(2)="local(#"</p>
<p>ARRAY(2)="local(#,"</p></td>
<td><p>S ARRAY(2)=300</p>
<p>S ARRAY(2)="300;301;304"</p>
<p>S ARRAY(2)="^GBL("</p>
<p>S ARRAY(2)="^GBL(""DFN"""</p>
<p>S ARRAY(2)="^GBL(""DFN"","</p>
<p>S ARRAY(2)="LOCAL("</p>
<p>S ARRAY(2)="LOCAL(""DFN"""</p>
<p>S ARRAY(2)="LOCAL(""DFN"","</p></td>
</tr>
<tr class="even">
<td>APPOINTMENT STATUS</td>
<td>ARRAY(3)</td>
<td><p>List of valid Appointment Status values, each separated by a semicolon. Valid values:</p>
<p><strong>R (</strong>Scheduled/Kept)</p>
<p><strong>I</strong> (Inpatient)</p>
<p><strong>NS</strong> (No-Show)</p>
<p><strong>NSR</strong> (No-Show, Rescheduled)</p>
<p><strong>CP</strong> (Cancelled by Patient)</p>
<p><strong>CPR</strong> (Cancelled by Patient, Rescheduled)</p>
<p><strong>CC</strong> (Cancelled by Clinic)</p>
<p><strong>CCR</strong> (Cancelled by Clinic, Rescheduled)</p>
<p><strong>NT</strong> (No Action Taken)</p>
<p>ARRAY (3) ="status1; status2" etc.</p></td>
<td><p>S ARRAY(3)="I"</p>
<p>S ARRAY(3)="R;I;NT"</p>
<p>S ARRAY(3)="CC;CCR;CP;CPR"</p></td>
</tr>
<tr class="odd">
<td>PATIENT DFN</td>
<td>ARRAY(4)</td>
<td><p>List of valid patient DFNs (each separated by a semicolon) or a global root or a local root. DFN must exist on PATIENT file.</p>
<p>ARRAY (4) ="dfn1; dfn2" etc.</p>
<p>ARRAY(4)="^global("</p>
<p>ARRAY(4)="^global(#"</p>
<p>ARRAY(4)="^global(#,"</p>
<p>ARRAY(4)="local("</p>
<p>ARRAY(4)="local(#"</p>
<p>ARRAY(4)="local(#,"</p></td>
<td><p>S ARRAY(4)=7179940</p>
<p>S ARRAY(4)="7179940;7179939;7179920"</p>
<p>S ARRAY(4)="^GBL("</p>
<p>S ARRAY(4)="^GBL(""IENLIST"""</p>
<p>S ARRAY(4)="^GBL(""IENLIST"","</p>
<p>S ARRAY(4)="LOCAL("</p>
<p>S ARRAY(4)="LOCAL(""IENLIST"""</p>
<p>S ARRAY(4)="LOCAL(""IENLIST"","</p></td>
</tr>
<tr class="even">
<td>PRIMARY STOP CODE</td>
<td>ARRAY(13)</td>
<td><p>List of valid Primary Stop Code values (not IENs). Must be a valid AMIS REPORTING STOP CODE (field #1) on the CLINIC STOP file (#40.7).</p>
<p>ARRAY (13) ="code1; code2" etc.</p></td>
<td><p>S ARRAY(13)=197</p>
<p>S ARRAY(13)="197;198;200;203;207"</p></td>
</tr>
<tr class="odd">
<td>DATE APPOINTMENT MADE</td>
<td>ARRAY(16)</td>
<td><p>Range of Date Appointment Made dates; "from" and "to" dates separated by a semicolon. Dates must be in the FileMan format YYYMMDD</p>
<p>(note: time is not allowed).</p>
<p>Array(16)= "from date; to date</p></td>
<td><p>S ARRAY(16)= "3040101;3040101" (all appts that have a Date Appointment Made date of 3040101)</p>
<p>S ARRAY(16)= "3040101" (appts that have a Date Appointment Made date from 3040101 forward)</p>
<p>S ARRAY(16)= ";3031231" (all appts that have a Date Appointment Made date through 3031231)</p>
<p>S ARRAY(16)=DT (all appts that have a Date Appointment Made date from today forward)</p>
<p>S ARRAY(16)= DT_";3041231" (all appts that have a Date Appointment Made date from today through 3041231)</p></td>
</tr>
</tbody>
</table>

### Input – Other Array Entries 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 23%" />
<col style="width: 40%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>DESCRIPTION</strong></td>
<td><strong>ARRAY ENTRY</strong></td>
<td><strong>Format</strong></td>
<td><strong>Examples of Array with filter</strong></td>
</tr>
<tr class="even">
<td>Field List - <strong>Required</strong>.</td>
<td>ARRAY("FLDS")</td>
<td><p>List of appointment field IDs, each separated by a semicolon. Order of fields is irrelevant. See “Data Fields” for the list of appointment field IDs. Or if all fields are required, then set array to “ALL” (case is irrelevant).</p>
<p>ARRAY ("FLDS") ="id1; id2; id3", etc.</p>
<p>ARRAY(“FLDS”)=”ALL”</p></td>
<td><p>ARRAY("FLDS")="1;2;3;6;7;14;20"</p>
<p>ARRAY("FLDS")=1</p>
<p>ARRAY("FLDS")=”ALL”</p>
<p>ARRAY("FLDS")=”all”</p></td>
</tr>
<tr class="odd">
<td>Max Appointments - Optional</td>
<td>ARRAY("MAX")</td>
<td><p>Maximum number of appointments requested. Must be a whole number not equal to 0.</p>
<p>ARRAY("MAX")=value</p>
<p>If value &gt; 0 or value=”” return first “<strong>N</strong>” appointments.</p>
<p>Else if value &lt; 0 return last <strong>“N</strong>” appointments.</p></td>
<td><p>ARRAY("MAX")=1</p>
<p>ARRAY("MAX")=-1</p></td>
</tr>
<tr class="even">
<td>Sort Appointments by Patient DFN – Optional</td>
<td>ARRAY(“SORT”)</td>
<td><p>Allows the output to be sorted by Patient, instead of by Patient and Clinic. Must be set to ‘P’.</p>
<p>ARRAY(“SORT”)=value</p></td>
<td>ARRAY("SORT")="P"</td>
</tr>
<tr class="odd">
<td>Include Purged Appointments - Optional</td>
<td>ARRAY(“PURGED”)</td>
<td><p>Allows the user to receive non-canceled Appts that were purged from sub-file #44.003.</p>
<p>ARRAY(“PURGED”)=1</p></td>
<td>ARRAY(“PURGED”)=1</td>
</tr>
</tbody>
</table>

The Field List array entry must be populated, or else error 115 will be generated. See “SDAPI - Error Codes” for a complete list of error codes and messages.

The Maximum Appointments array entry is best used to retrieve the next or last “n” appointments for 1 patient and/or 1 clinic, in conjunction with the appointment date/time filter.

> **NOTE:** If the Maximum Appointment array entry is set to a valid value and more than 1 patient and/or more than 1 clinic are passed to the API, or if no patient and clinic is passed to the API, the error 115 will be generated. See “SDAPI - Error codes” for a complete list of error codes and messages.

EXAMPLE:

APPOINTMENT DATA TO BE FILTERED

ARRAY ENTRY Format Examples of M code to set array with filter values

APPOINTMENT DATE/TIME ARRAY(1) Range of appointment date/times, "from" and "to" date/time separated by semicolon. Dates must be FileMan format YYYMMDD.HHMMSS

ARRAY(1)="from date; to date"

S ARRAY(1)="3030101;3030101" (one day)

S ARRAY(1)="3040101" (appts after 2003)

S ARRAY(1)=";3031231" (all appts thru 3031231)

S ARRAY(1)=DT (all appts from today forward)

S ARRAY(1)=DT\_";3041231" (all appts from today through 3041231)

CLINIC IEN ARRAY(2) List of valid clinic IENs (each separated by a semicolon) or a global root or a local root. Clinic must exist on Hospital Location file.

ARRAY(2)="ien1;ien2" etc.

ARRAY(2)="^global("

ARRAY(2)="^global(#"

ARRAY(2)="^global(#,"

ARRAY(2)="local("

ARRAY(2)="local(#"

ARRAY(2)="local(#,"

S ARRAY(2)=300

S ARRAY(2)="300;301;304"

S ARRAY(2)="^GBL("

S ARRAY(2)="^GBL(""DFN"""

S ARRAY(2)="^GBL(""DFN"","

S ARRAY(2)="LOCAL("

S ARRAY(2)="LOCAL(""DFN"""

S ARRAY(2)="LOCAL(""DFN"","

APPOINTMENT STATUS ARRAY(3) List of valid Appointment Status values, each separated by a semicolon. Valid values:

R (Scheduled/Kept)

I (Inpatient)

NS (No-Show)

NSR (No-Show, Rescheduled)

CP (Cancelled by Patient)

CPR (Cancelled by Patient, Rescheduled)

CC (Cancelled by Clinic)

CCR (Cancelled by Clinic, Rescheduled)

NT (No Action Taken)

ARRAY(3)="status1;status2" etc.

S ARRAY(3)="I"

S ARRAY(3)="R;I;NT"

S ARRAY(3)="CC;CCR;CP;CPR"

PATIENT DFN ARRAY(4) List of valid patient DFNs (each separated by a semicolon) or a global root or a local root. DFN must exist on PATIENT file.

ARRAY(4)="dfn1;dfn2" etc.

ARRAY(4)="^global("

ARRAY(4)="^global(#"

ARRAY(4)="^global(#,"

ARRAY(4)="local("

ARRAY(4)="local(#"

ARRAY(4)="local(#,"

S ARRAY(4)=7179940

S ARRAY(4)="7179940;7179939;7179920"

S ARRAY(4)="^GBL("

S ARRAY(4)="^GBL(""IENLIST"""

S ARRAY(4)="^GBL(""IENLIST"","

S ARRAY(4)="LOCAL("

S ARRAY(4)="LOCAL(""IENLIST"""

S ARRAY(4)="LOCAL(""IENLIST"","

PRIMARY STOP CODE ARRAY(13) List of valid Primary Stop Code values (not IENs). Must be a valid AMIS REPORTING STOP CODE (field \#1) on the CLINIC STOP file (#40.7).

ARRAY(13)="code1;code2" etc.

S ARRAY(13)=197

S ARRAY(13)="197;198;200;203;207"

DATE APPOINTMENT MADE ARRAY(16) Range of Date Appointment Made dates; "from" and "to" dates separated by a semicolon. Dates must be in the FileMan format YYYMMDD

(note: time is not allowed).

Array(16)= "from date; to date"

S ARRAY(16)= "3040101;3040101" (all appts that have a Date Appointment Made date of 3040101)

S ARRAY(16)= "3040101" (appts that have a Date Appointment Made date from 3040101 forward)

S ARRAY(16)= ";3031231" (all appts that have a Date Appointment Made date through 3031231)

S ARRAY(16)=DT (all appts that have a Date Appointment Made date from today forward)

S ARRAY(16)= DT\_";3041231" (all appts that have a Date Appointment Made date from today through 3041231)

### Other Array Entries 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

INPUT

DESCRIPTION ARRAY ENTRY Format Examples of Array with filter

Field List - Required. ARRAY("FLDS")

List of appointment field IDs, each separated by a semicolon. Order of fields is irrelevant. See “Data Fields” for the list of appointment field IDs. Or if all fields are required, then set array to “ALL” (case is irrelevant).

ARRAY("FLDS")="id1;id2;id3", etc.

ARRAY(“FLDS”)=”ALL” ARRAY("FLDS")="1;2;3;6;7;14;20"

ARRAY("FLDS")=1

ARRAY("FLDS")=”ALL”

ARRAY("FLDS")=”all”

Max Appointments - Optional ARRAY("MAX") Maximum number of appointments requested. Must be a whole number not equal to 0.

ARRAY("MAX")=value

If value \> 0 or value=”” return first “N” appointments.

Else if value \< 0 return last “N” appointments.

ARRAY("MAX")=1

ARRAY("MAX")=-1

Sort Appointments by Patient DFN – Optional ARRAY(“SORT”) Allows the output to be sorted by Patient, instead of by Patient and Clinic. Must be set to ‘P’.

ARRAY(“SORT”)=value ARRAY("SORT")="P"

Include Purged Appointments - Optional ARRAY(“PURGED”) Allows the user to receive non-canceled Appts that were purged from sub-file \#44.003.

ARRAY(“PURGED”)=1 ARRAY(“PURGED”)=1

The Field List array entry must be populated, or else error 115 will be generated. See “SDAPI - Error Codes” for a complete list of error codes and messages.

The Maximum Appointments array entry is best used to retrieve the next or last “n” appointments for 1 patient and/or 1 clinic, in conjunction with the appointment date/time filter.

> **NOTE:** If the Maximum Appointment array entry is set to a valid value and more than 1 patient and/or more than 1 clinic are passed to the API, or if no patient and clinic is passed to the API, the error 115 will be generated. See “SDAPI - Error codes” for a complete list of error codes and messages.

### SDAPI - Error Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Codes and Associated Messages

| Error Code                                                                                                                                                                                                                                                                                      | Error Message         | Occurs…                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------|
| 101                                                                                                                                                                                                                                                                                             | DATABASE IS UNAVAILABLE   | If the Scheduling database or VistALink is unavailable                                          |
| 115                                                                                                                                                                                                                                                                                             | INVALID INPUT ARRAY ENTRY | If the input array has an invalid entry or the field list is null                               |
| 116                                                                                                                                                                                                                                                                                             | DATA MISMATCH             | If VistA and the database are out of sync. i.e., the database returns an IEN not found on VistA |
| 117                                                                                                                                                                                                                                                                                             | SDAPI ERROR               | For catching new error codes that could be added at a later time.                               |
| Error codes 101, 116 and 117 will not occur until the RSA has been implemented. Coding for these error codes needs to be done now so that no other coding changes will need to be made in the future. Each application will need to decide how to handle the return of those three error codes. |                           |                                                                                                 |

### SDAPI - Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

API CONSTRAINTS

Cancelled appointments are returned only if the patient filter is populated.

Cancelled appointments will always have null values in the following fields:

Length of Appointment Eligibility of Visit Comments

Check-Out Date/Time Check-In Date/Time Overbook

If you want canceled appointments, but don’t want to specify a subset of patients, then set the patient filter \[ARRAY(4)\] equal to “^DPT(“. This will result in canceled appointments being returned. Note, however, that this will decrease the performance time of the API, as it will spin through the entire VistA Patient file, looking for appointments in the specified clinics (if filter is populated). It will, however, have no negative performance impact when it retrieves appointments from the RSA.

The Max Appointments array entry can only be used with 1 patient and/or 1 clinic. If multiple patients and/or clinics are passed or no clinic and/or patient is passed, an error message will be generated.

Use of the PURGED array parameter requires 2 conditions to be met: the patient filter must be populated; and the field list must not contain fields 5-9, 11, 22, 28, 30, 31, or 33, otherwise error 115 will be returned.

### Application Programmer Interface - GETAPPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Name: GETAPPT ; Retrieve Appointment Data for a Patient ID

Declaration: GETAPPT^SDAMA201(SDIEN,SDFIELDS,SDAPSTAT, SDSTART,SDEND,SDRESULT,SDIOSTAT)

Description: Returns appointment information for a specific patient ID. To use this API, subscribe

to Integration Agreement \#3859.

Arguments: SDIEN Patient IEN (required)

SDFIELDS Field List (optional, each field number separated by a semi-colon)

> SDAPSTAT Appointment Status Filter (optional, each value separated by a semi-colon. See “Filters” for default and valid values)

> SDSTART Start Date (optional, internal FileMan format)

> SDEND End Date (optional, internal FileMan format)

> SDRESULT Local variable to hold returned appointment Count (optional, passed by reference)

> SDIOSTAT Patient Status Filter (optional, see “Filters” for default and valid values)

Field List: A null value in this parameter will result in ALL appointment data fields being returned. See “Data Fields” for a list of the field numbers and corresponding data available in this API.

Return Values: If no errors occur and appointments are found, SDRESULT will contain the appointment count and the requested data will be returned in: ^TMP(\$J,”SDAMA201”,”GETAPPT”,x,y) = field y data where ‘x’ is an incremental appointment count (starting with 1) and ‘y’ is the field number requested.

If no errors occur and no appointments are found, then SDRESULT will contain a value of 0 and the ^TMP(\$J,”SDAMA201”,”GETAPPT”,x,y) array will not be generated.

If an error occurs, SDRESULT will be –1 and the error codes and messages will be returned in ^TMP(\$J,”SDAMA201”,”GETAPPT”,”ERROR”,error code) = error message. See “Error Codes” for a list of error codes and messages.

Other: When processing has completed, kill the temporary array: ^TMP(\$J,”SDAMA201”,”GETAPPT”)

GETAPPT EXAMPLES

1\) Retrieve scheduled/kept inpatient appointment date/time, clinic ID, appt status, comments, and patient status for patient 99 from 1/1/02 through 1/31/02:

\>D GETAPPT^SDAMA201(99,”1;2;3;6;12”,”R”,3020101,3020131,.SDRESULT,”I”)

\>ZW SDRESULT

SDRESULT=3

\>ZW ^TMP(\$J,”SDAMA201”,”GETAPPT”)

^TMP(1000,”SDAMA201”,”GETAPPT”,1,1)=3020101.10

^TMP(1000,”SDAMA201”,”GETAPPT”,1,2)=130^TOM’S CLINIC

^TMP(1000,”SDAMA201”,”GETAPPT”,1,3)=”R”

^TMP(1000,”SDAMA201”,”GETAPPT”,1,6)=”PATIENT REQUESTS A RIDE HOME”

^TMP(1000,”SDAMA201”,”GETAPPT”,1,12)=”I”

^TMP(1000,”SDAMA201”,”GETAPPT”,2,1)=3020115.08

^TMP(1000,”SDAMA201”,”GETAPPT”,2,2)= 150^BOB’S CLINIC

^TMP(1000,”SDAMA201”,”GETAPPT”,2,3)=”R”

^TMP(1000,”SDAMA201”,”GETAPPT”,2,6)=

^TMP(1000,”SDAMA201”,”GETAPPT”,2,12)=”I”

^TMP(1000,”SDAMA201”,”GETAPPT”,3,1)=3020115.09

^TMP(1000,”SDAMA201”,”GETAPPT”,3,2)= 150^BOB’S CLINIC

^TMP(1000,”SDAMA201”,”GETAPPT”,3,3)=”R”

^TMP(1000,”SDAMA201”,”GETAPPT”,3,6)=”WHEELCHAIR REQUESTED”

^TMP(1000,”SDAMA201”,”GETAPPT”,3,12)=”I”

2\) Retrieve inpatient and outpatient appointment date/time, clinic ID, appointment status, and comments for patient 99 from 1/1/02 at 8am through 1/31/02 for scheduled/kept appointments:

\>D GETAPPT^SDAMA201(99,”1;2;3;6”,”R”,3020101.08,3020131,.SDRESULT)

\>ZW SDRESULT

SDRESULT=2

\>ZW ^TMP(\$J,”SDAMA201”,”GETAPPT”)

^TMP(1000,”SDAMA201”,”GETAPPT”,1,1)=3020101.10

^TMP(1000,”SDAMA201”,”GETAPPT”,1,2)=130^TOM’S CLINIC

^TMP(1000,”SDAMA201”,”GETAPPT”,1,3)=”R”

^TMP(1000,”SDAMA201”,”GETAPPT”,1,6)=”PATIENT REQUESTS A RIDE HOME”

^TMP(1000,”SDAMA201”,”GETAPPT”,2,1)=3020115.09

^TMP(1000,”SDAMA201”,”GETAPPT”,2,2)= 150^BOB’S CLINIC

^TMP(1000,”SDAMA201”,”GETAPPT”,2,3)=”R”

^TMP(1000,”SDAMA201”,”GETAPPT”,2,6)=”WHEELCHAIR REQUESTED”

## Application Programmer Interface - NEXTAPPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Name: NEXTAPPT ; Retrieve Next Appointment Data for a Patient ID

Declaration: \$\$NEXTAPPT^SDAMA201(SDIEN,SDFIELDS,

SDAPSTAT,SDIOSTAT)

Description: This API returns requested next appointment information for a patient ID and should be called using an EXTRINSIC call. The "next" appointment is defined as the next appointment on file after the current date/time. To use this API, subscribe to Integration Agreement \#3859.

Arguments: SDIEN Patient IEN (required)

> SDFIELDS Field List (optional, each field number separated by a semi-colon)

> SDAPSTAT Appointment Status Filter (optional, each value separated by a semi-colon. See “Filters” for default and valid values)

> SDIOSTAT Patient Status Filter (optional, see “Filters” for default and valid values)

> Field List: A null value in this parameter will result in NO appointment data fields being returned. See “Data Fields” for a list of the field numbers and corresponding data available in this API.

Return Values: This API will return “-1” if an error occurred, “0” if no future appointment is found, or “1” if a future appointment was found.

If no future appointment is found, then the ^TMP(\$J,”SDAMA201”,”NEXTAPPT”,y) array will not be generated.

If the user enters an optional field list and a future appointment is found, the data for the next appointment will be returned in ^TMP(\$J,”SDAMA201”,”NEXTAPPT”,y) = field y data where ‘y’ is the field number requested.

If an error occurs, the error codes and messages will be returned in ^TMP(\$J,”SDAMA201”,”NEXTAPPT”,”ERROR”,error code) = error message. See “Error Codes” for a list of error codes and messages.

Other: When processing has completed, kill the temporary array:

^TMP(\$J,”SDAMA201”,”NEXTAPPT”)

NEXTAPPT EXAMPLES

1\) See if patient 321 has a future appointment (inpatient or outpatient).

> I \$\$NEXTAPPT^SDAMA201(321) D

> insert code here to continue processing as needed

No appointment data is returned from the above example because no fields were passed in.

2\) If patient 99 has a future scheduled inpatient appointment, retrieve appointment date/time, clinic ID, appointment status, and patient status:

I \$\$NEXTAPPT^SDAMA201(99,”1;2;3;12”,”R”,”I”) D

S NEXTDATE=\$G(^TMP(\$J,”SDAMA201”,”NEXTAPPT”,1))

S CLINIEN=+\$G(^TMP(\$J,”SDAMA201”,”NEXTAPPT”,2))

S APPTSTAT=\$G(^TMP(\$J,”SDAMA201”,”NEXTAPPT”,3))

S PATSTATS=\$G(^TMP(\$J,”SDAMA201”,”NEXTAPPT”,12))

\>ZW ^TMP(\$J,”SDAMA201”,”NEXTAPPT”)

^TMP(1000,”SDAMA201”,”NEXTAPPT”,1)=3030115.10

^TMP(1000,”SDAMA201”,”NEXTAPPT”,2)=130^SAM’S CLINIC

^TMP(1000,”SDAMA201”,”NEXTAPPT”,3)=R

^TMP(1000,”SDAMA201”,”NEXTAPPT”,12)=”I”

3\) If patient 111 has a future appointment (scheduled, cancelled, or no-show), retrieve appointment date/time, clinic ID, appointment status, and patient status:

I \$\$NEXTAPPT^SDAMA201(111,”1;2;3;12”) D

S NEXTDATE=\$G(^TMP(\$J,”SDAMA201”,”NEXTAPPT”,1))

S CLINIEN=+\$G(^TMP(\$J,”SDAMA201”,”NEXTAPPT”,2))

S APPTSTAT=\$G(^TMP(\$J,”SDAMA201”,”NEXTAPPT”,3))

S PATSTATS=\$G(^TMP(\$J,”SDAMA201”,”NEXTAPPT”,12))

\>ZW ^TMP(\$J,”SDAMA201”,”NEXTAPPT”)

^TMP(1000,”SDAMA201”,”NEXTAPPT”,1)=3030130.10

^TMP(1000,”SDAMA201”,”NEXTAPPT”,2)=130^SAM’S CLINIC

^TMP(1000,”SDAMA201”,”NEXTAPPT”,3)=C

^TMP(1000,”SDAMA201”,”NEXTAPPT”,12)=””

Note that a cancelled appointment was returned above because the appointment status filter was undefined and it was the next appointment on the file. The patient status was returned with a value of null.

## Application Programmer Interface - GETPLIST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Name: GETPLIST ; Retrieve Appointment Data for a Clinic ID

Declaration: GETPLIST^SDAMA202(SDIEN,SDFIELDS,SDAPSTAT,

SDSTART,SDEND,SDRESULT, SDIOSTAT)

Description: Returns requested clinic appointment information for a specific clinic ID. To use this API, subscribe to Integration Agreement \#3869. Note: This API will return appointment information for ‘regular’, ‘no-show’, and ‘no action taken’ appointments only; while the appointment data is located in VistA, cancelled appointments will not be returned because they are not retained on the Hospital Location sub-files (44.001, 44.003).

Arguments: SDIEN Clinic IEN (required)

> SDFIELDS Field List (optional, each field number separated by a semi-colon)

> SDAPSTAT Appointment Status Filter (optional, each value separated by a semi-colon. See “Filters” for default and valid values)

> SDSTART Start Date/time (optional, internal FileMan format)

> SDEND End Date/time (optional, internal FileMan format)

> SDRESULT Local variable to hold returned appointment count (optional, passed by reference)

> SDIOSTAT Patient Status Filter (optional, see “Filters” for default and valid values)

Field List: A null value in this parameter will result in ALL appointment data fields being returned. See “Data Fields” for a list of the field numbers and corresponding data available in this API.

Return Values: If no errors occur and appointments are found, SDRESULT will contain the appointment count and the data will be returned in ^TMP(\$J,”SDAMA202”,”GETPLIST”,x,y) = field y data where ‘x’ is an incremental appointment count (starting with 1) and ‘y’ is the field number requested.

If no errors occur and no appointments are found, then SDRESULT will contain a value of 0 and the ^TMP(\$J,”SDAMA202”,”GETPLIST”,x,y) array will not be generated.

If an error occurs, SDRESULT will be –1 and the error codes and messages will be returned in ^TMP(\$J,”SDAMA202”,”GETPLIST”,”ERROR”,error code) = error message. See “Error Codes” for a list of error codes and messages.

Other: When processing has completed, kill the temporary array:

^TMP(\$J,”SDAMA202”,”GETPLIST”)

  
GETPLIST EXAMPLE

Retrieve inpatient and outpatient appointment date/time, patient ID, and length of appointment for clinic 100 for 1/1/02 from 8am to 10am:

\>D GETPLIST^SDAMA202(100,”1;4;5”,,3020101.08,3020101.1,.SDRESULT)

\>ZW SDRESULT

SDRESULT=4

\>ZW ^TMP(\$J,”SDAMA202”,”GETPLIST”)

^TMP(1000,”SDAMA202”,”GETPLIST”,1,1)=3020101.08

^TMP(1000,”SDAMA202”,”GETPLIST”,1,4)=4564^JONES,CANDACE

^TMP(1000,”SDAMA202”,”GETPLIST”,1,5)=60

^TMP(1000,”SDAMA202”,”GETPLIST”,2,1)=3020101.09

^TMP(1000,”SDAMA202”,”GETPLIST”,2,4)=9007^HEADRICK,ANITA

^TMP(1000,”SDAMA202”,”GETPLIST”,2,5)=30

^TMP(1000,”SDAMA202”,”GETPLIST”,3,1)=3020101.093

^TMP(1000,”SDAMA202”,”GETPLIST”,3,4)=24389^SIMPSON,LEANORA

^TMP(1000,”SDAMA202”,”GETPLIST”,3,5)=30

^TMP(1000,”SDAMA202”,”GETPLIST”,4,1)=3020101.1

^TMP(1000,”SDAMA202”,”GETPLIST”,4,4)=40374^SMITH,SAMUEL

^TMP(1000,”SDAMA202”,”GETPLIST”,4,5)=30

## Application Programmer Interface - PATAPPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Name: PATAPPT ; Check for existence of any appointment for a patient

Declaration: PATAPPT^SDAMA204(SDDFN)

Description: Returns 1, 0, -1 according to the existence of appointment(s) for a patient ID. To use this API, please subscribe to Integration Agreement \#4216.

Argument: SDDFN Patient IEN (required)

Return Values: Patient scheduling record(s) Value Returned

Appointment(s) on file 1

No Appointment(s) on file 0

Error - 1

Depending on the existence of appointment(s) for a specific patient ID, an extrinsic value will be returned according to the Return Values table listed above.

If an error occurs, a –1 will be returned, and a node with error information will be created.

The format will be:

W \$\$PATAPPT^SDAMA204(0) -1

The error information will reside in the following node:

ZW ^TMP(634,"SDAMA204","PATAPPT","ERROR")

^TMP(634,"SDAMA204","PATAPPT","ERROR",114)="INVALID PATIENT ID"

See “Error Codes” for a list of error codes and messages.

This function does not remove the ^TMP node created when an error occurs. It is the calling program’s responsibility to delete the node.

PATAPPT EXAMPLES

The following examples show the initialization of variable X with the value from the function \$\$PATAPPT^SDAMA204(SDDFN):

1\) Patient Appointments Exists

Cache\>S X=\$\$PATAPPT^SDAMA204(123)

Cache\>W X

1

2\) No Patient Appointments Exists

Cache\>S X=\$\$PATAPPT^SDAMA204(11)

Cache\>W X

0

3\) Invalid Patient ID

Cache\>S X=\$\$PATAPPT^SDAMA204(0)

Cache\>W X

-1

Cache\>ZW ^TMP(\$J,"SDAMA204","PATAPPT","ERROR")

^TMP(659,"SDAMA204","PATAPPT","ERROR",114)="INVALID PATIENT ID"

ERROR CODES

Error Codes and Associated Messages

101 DATABASE IS UNAVAILABLE

102 PATIENT ID IS REQUIRED

103 INVALID FIELD LIST

104 CLINIC ID IS REQUIRED

105 INVALID START DATE

106 INVALID END DATE

108 FACILITY ID IS REQUIRED

109 INVALID APPOINTMENT STATUS FILTER

110 ID MUST BE NUMERIC

111 START DATE CAN’T BE AFTER END DATE

112 INVALID PATIENT STATUS FILTER

113 APPT STATUS AND PATIENT STATUS FILTER COMBINATION UNSUPPORTED IN VISTA

114 INVALID PATIENT ID

# Data Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Available Data Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 20%" />
<col style="width: 23%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ID</strong></td>
<td><strong>FIELD NAME</strong></td>
<td><strong>DATA TYPE</strong></td>
<td><strong>Format or Valid Values</strong></td>
<td><strong>Description</strong></td>
<td><strong>Examples of Returned Data</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>APPOINTMENT DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD@HHMM</td>
<td>The scheduled Appointment Date/Time</td>
<td><p>3021215@113</p>
<p>3021201@0815</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>CLINIC ID and NAME</td>
<td>POINTER and TEXT</td>
<td>ID^name</td>
<td>Clinic ID and name</td>
<td><p>150^CARDIOLOGY</p>
<p>32^TOM’S CLINIC</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>APPOINTMENT STATUS</td>
<td>ALPHA</td>
<td><p><strong>N</strong> (No-Show)</p>
<p><strong>C</strong> (Cancelled)</p>
<p><strong>R</strong> (Scheduled/Kept)</p>
<p><strong>NT</strong> (No Action Taken)</p></td>
<td>The status of the appointment. N for no-show appointment, C for cancelled appointment (cancelled for ANY reason), NT for no action taken, and R for a future appointment or a past kept appointment</td>
<td><p>N</p>
<p>C</p>
<p>R</p>
<p>NT</p></td>
</tr>
<tr class="odd">
<td>4</td>
<td>PATIENT ID and NAME</td>
<td>POINTER and TEXT</td>
<td>ID^name</td>
<td>Patient ID and name</td>
<td><p>34877^JONES,BOB</p>
<p>455^SCHILSON,BRIAN</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>LENGTH OF APPOINTMENT</td>
<td>NUMERIC</td>
<td>NNN</td>
<td>The scheduled length of appointment, in minutes</td>
<td><p>20</p>
<p>60</p></td>
</tr>
<tr class="odd">
<td>6</td>
<td>COMMENTS</td>
<td>TEXT</td>
<td>free text</td>
<td>Any comments associated with the appointment</td>
<td>PATIENT NEEDS WHEELCHAIR</td>
</tr>
<tr class="even">
<td>7</td>
<td>OVERBOOK</td>
<td>TEXT</td>
<td><strong>Y</strong> or <strong>N</strong></td>
<td>“Y” if appointment is an overbook else “N”</td>
<td><p>Y</p>
<p>N</p></td>
</tr>
<tr class="odd">
<td>8</td>
<td>ELIGIBILITY OF VISIT ID and NAME</td>
<td>POINTER and TEXT</td>
<td>ID^name</td>
<td>Eligibility code and name associated with the appointment</td>
<td><p>2^AID &amp; ATTENDANCE</p>
<p>7^ALLIED VETERAN</p>
<p>13^COLLATERAL OF VET.</p></td>
</tr>
<tr class="even">
<td>9</td>
<td>CHECK-IN DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD@HHMM</td>
<td>Date/time the patient checked in for the appointment</td>
<td>3021215@113</td>
</tr>
<tr class="odd">
<td>10</td>
<td>APPOINTMENT TYPE ID and NAME</td>
<td>POINTER and TEXT</td>
<td>ID^name</td>
<td>Type of appointment ID and name</td>
<td><p>1^COMPENSATION &amp; PENSION</p>
<p>3^ORGAN DONORS</p>
<p>7^COLLATERAL OF VET.</p></td>
</tr>
<tr class="even">
<td>11</td>
<td>CHECK-OUT DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD@HHMM</td>
<td>Date/time the patient checked out of the appointment</td>
<td>3021215@113</td>
</tr>
<tr class="odd">
<td>12</td>
<td>PATIENT STATUS</td>
<td>TEXT</td>
<td><p><strong>I</strong></p>
<p><strong>O</strong></p>
<p>null</p></td>
<td>For future, scheduled appointments, the current status of the patient. For past, kept appointments, the status at the time of the appointment. For cancelled and no-show appointments, this will be null</td>
<td><p>I</p>
<p>O</p>
<p>“”</p></td>
</tr>
</tbody>
</table>

## FILTERS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Valid Appointment Status Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SDAPSTAT filter parameter can be used if you wish to screen on appointment status. If this parameter contains a value or set of values, then those appointments will be returned in the resulting array set. Request more than 1 value in the filter by separating them with a semi-colon (i.e. SDAPSTAT=”R;NT”).

A null or undefined value will result in all being returned.

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Appt Status Filter value</th>
<th>Appointment Status Value(s) Returned</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>R</td>
<td>R (scheduled/kept)</td>
</tr>
<tr class="even">
<td>N</td>
<td>N (no-show)</td>
</tr>
<tr class="odd">
<td>C</td>
<td>C (cancelled)</td>
</tr>
<tr class="even">
<td>NT</td>
<td>NT (no action taken)</td>
</tr>
<tr class="odd">
<td>Null (default)</td>
<td><p>ALL appointment status values will be returned:</p>
<p>R (scheduled/kept)</p>
<p>N (no-show)</p>
<p>C (cancelled)</p>
<p>NT (no action taken)</p></td>
</tr>
</tbody>
</table>

### Valid Patient Status Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SDIOSTAT filter parameter can be used if you wish to retrieve only inpatient records or only outpatient records. A null or undefined value will result in both being returned.

| Patient Status Filter value | Description                                      |
|-----------------------------|--------------------------------------------------|
| I                           | Inpatient                                        |
| O                           | Outpatient                                       |
| Null (default)              | Both will be returned (inpatient and outpatient) |

### ### Valid Patient Status and Appointment Status Filter Combinations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the design of VistA, the patient status (new field \#12) of appointments that are cancelled, no-show, or no action taken, will not be available. If the patient status field is requested, a null value will be returned in the ^TMP output global for this field. Patient status is determined by analyzing the value of the STATUS field (#3) on the Patient subfile (2.98).

Inpatient appointments contain an “I” in this field and are identified only if the field has not been changed (cancelled, etc.). Therefore, if the user wishes to specifically request only inpatient appointments (using the Patient Status filter = ”I”), then the Appointment Status filter must be set to “R”.

Any other value in the Appointment Status filter (including null or undefined) will cause an error (#113) to be generated and returned in the ^TMP global. The same is true when specifically requesting outpatient appointments. To retrieve No-Show, Cancelled, or No Action Taken appointments, the Patient Status filter must be left null or undefined. See table below for results of combinations of these two filters.

| Patient Status Filter | Appointment Status Filter                             | Valid/Invalid | Patient Status value in ^TMP (if requested)                                                                                    |
|-----------------------|-------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------|
| I or O                | R                                                     | Valid         | I for inpatient appointments, O for outpatient appointments                                                                    |
| I or O                | N                                                     | Invalid       | N/A                                                                                                                            |
| I or O                | C                                                     | Invalid       | N/A                                                                                                                            |
| I or O                | NT                                                    | Invalid       | N/A                                                                                                                            |
| I or O                | Any combination of R, N, C, and NT                    | Invalid       | N/A                                                                                                                            |
| I or O                | Null/Undefined                                        | Invalid       | N/A                                                                                                                            |
| Null/Undefined        | R                                                     | Valid         | I for inpatient appointments; O for outpatient appointments                                                                    |
| Null/Undefined        | N                                                     | Valid         | Null                                                                                                                           |
| Null/Undefined        | C                                                     | Valid         | Null                                                                                                                           |
| Null/Undefined        | NT                                                    | Valid         | Null                                                                                                                           |
| Null/Undefined        | Null/Undefined, or any combination of R, N, C, and NT | Valid         | I or O for scheduled/kept inpatient and outpatient appointments; null for cancelled, no-show, and no action taken appointments |

| Patient Status filter key | Appointment Status filter key     |
|---------------------------|-----------------------------------|
| I = Inpatient             | R = scheduled/kept appointments   |
| O = Outpatient            | N = all no-show appointments      |
|                           | C = all cancelled appointments    |
|                           | NT = no action taken appointments |

## Application Programmer Interface - SDIMO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Name : SDIMO; Inpatient Medications for Outpatients

Declaration: \$\$SDIMO^SDAMA203(SDCLIEN,SDDFN)

Description: This API returns encounter date/time for a clinic IEN and patient DFN. If the patient does not have an encounter in the specified clinic today (or yesterday if current time is before 6am), then the patient’s scheduled appointment date/time for that clinic, today or in the future (or yesterday if current time is before 6am), is returned. This API should be called using an EXTRINSIC call.

Arguments: SDCLIEN Clinic IEN (required)

SDDFN Patient DFN (required)

| RETURN VALUES: |                                                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------------------------------|
| 1              | Patient has at least one encounter today or one scheduled appointment today or in the future in the authorized clinic |
| 0              | Patient does not have an encounter today or an appointment today or in the future in the authorized clinic            |
| -1             | Clinic is not authorized, clinic is inactive, or clinic IEN is null                                                   |
| -2             | Patient DFN is null                                                                                                   |
| -3             | Scheduling Database is unavailable                                                                                    |
| SDIMO(1)       | Encounter date/time or appointment date/time                                                                          |

If a 1 is returned, then the variable SDIMO(1) will contain the encounter or appointment date/time. If something other than a 1 is returned, the variable SDIMO(1) will not be created.

Other: When processing has completed, the variable SDIMO(1) needs to be killed.

SDIMO EXAMPLES:

1\) Is patient 123 authorized to receive inpatient medication at clinic 800?

I \$\$SDIMO^SDAMA203(800,123) D

S APPTDT=\$G(SDIMO(1))

K SDIMO(1)

;continue processing as needed

2\) Example of handling an error:

S SDRESULT=\$\$SDIMO^SDAMA203(800,123)

I SDRESULT\<1 D

I SDRESULT=-1 D

process clinic error as needed

Configuring Bar Code Label Printers

## Configuring Bar Code Label Printers for Print Patient Label Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ambulatory-care-reporting-technical-manual/005.png)The Veteran Identification Card (VIC) provided by the VIC Replacement project does not support embossing of protected health information. Instead, a new Print Patient Label \[DG PRINT PATIENT LABEL\] option will allow labels to be printed with the patient’s protected health information.

The labels will contain the patient’s name, social security number, and date of birth. An optional fourth line contains the patient’s inpatient location (ward and room#).

The labels may be affixed to medical record forms in lieu of using the current embossed cards to imprint this information.

EXAMPLE LABEL

The Print Patient Label \[DG PRINT PATIENT LABEL\] option was exported with the Veteran ID Card (VIC) Replacement patch (DG\*5.3\*571). This option was placed on the ADT Outputs Menu \[DG OUTPUTS MENU\] option.

This option supports plain text printing to dot matrix and laser printers by prompting the user for the number of lines that the label stock can contain. In addition, bar code label printers, such as Zebra and Intermec, are supported on systems that have installed the Kernel Support for Bar Code Printers patch (XU\*8\*205).

### Hardware Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files.

### Software Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bar code label printers, such as the Zebra and Intermec printers, require control codes to be defined in the CONTROL CODES subfile (#3.2055) of the TERMINAL TYPE file (#3.2).

The patient label print routine (DGPLBL) checks for the existence of the control codes before attempting to execute. Presently, the patient label print routine (DGPLBL) uses eight control codes. DBIA \#3435 allows direct MUMPS read access to the CONTROL CODES subfile (#3.2055) of the TERMINAL TYPE file (#3.2).

It is not required that all control codes be defined - just build the necessary control codes for the selected printer.

## Control Code Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These are the control codes that are currently used by the patient label print routine (DGPLBL). In order for the routine to work correctly, these control codes must be entered through FileMan in the CONTROL CODES subfile (#3.2055) of the TERMINAL TYPE file (#3.2) using the names listed below.

CODE DESCRIPTION

FI Format Initialization

FE Format End

SL Start of Label

EL End of Label

ST Start of Text

ET End of Text

STF Start of Text Field

ETF End of Text Field

### Patient Label Print Routine Control Code Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following pseudo-code listing shows the flow and the points at which each of the control codes are used. It is not required that all control codes be defined - just build the necessary control codes for the selected printer.

a\. Label print routine invoked.

b\. Control codes loaded into local array DGIOCC. Variable DGIOCC is defined to indicate whether or not control codes exist.

c\. Format Initialization.

d\. For each label printed:

- Start of Label
- Start of Text\*
- Start of Text Field\*
- Text Information\*
- End of Text Field\*
- End of Text\*
- End of Label.

e\. Format End.

\* indicates items that may be executed repeatedly

### Label Printer Setup Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are examples of the control codes setup in the CONTROL CODES subfile (#3.2055) of the TERMINAL TYPE file (#3.2) for the Zebra and Intermec label printers.

These printers were used during the development process, and the examples are provided to guide the user in the control code setup. The examples provided are based on a 1 ½ by 3 ½ inch label.

### Zebra Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: Control Codes Setup for Horizontal Labels

NUMBER: 1

ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION

CONTROL CODE: W "^XA",!,"^LH0,0^FS",!

NUMBER: 2

ABBREVIATION: SL

FULL NAME: START LABEL

CONTROL CODE: W "^XA",! S DGY=30,DGX=10

NUMBER: 3

ABBREVIATION: ST

FULL NAME: START TEXT

CONTROL CODE: W "^FO",DGX,",",DGY,"^A0N,30,30" S DGY=DGY+40

NUMBER: 4

ABBREVIATION: STF

FULL NAME: START TEXT FIELD

CONTROL CODE: W "^FD"

NUMBER: 5

ABBREVIATION: ETF

FULL NAME: END TEXT FIELD

CONTROL CODE: W "^FS",!

NUMBER: 6

ABBREVIATION: EL

FULL NAME: END LABEL

CONTROL CODE: W "^XZ",!

EXAMPLE 2: CONTROL CODES SETUP FOR VERTICAL LABELS

NUMBER: 1

ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION

CONTROL CODE: W "^XA",!,"^LH0,0^FS",!

NUMBER: 2

ABBREVIATION: SL

FULL NAME: START LABEL

CONTROL CODE: W "^XA",! S DGY=50,DGX=190

NUMBER: 3

ABBREVIATION: ST

FULL NAME: START TEXT

CONTROL CODE: W "^FO",DGX,",",DGY,"^A0R,30,20" S DGX=DGX-40

NUMBER: 4

ABBREVIATION: STF

FULL NAME: START TEXT FIELD

CONTROL CODE: W "^FD"

NUMBER: 5

ABBREVIATION: ETF

FULL NAME: END TEXT FIELD

CONTROL CODE: W "^FS",!

NUMBER: 6

ABBREVIATION: EL

FULL NAME: END LABEL

CONTROL CODE: W "^XZ",!

## Intermec Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Intermec label printers require that a label format be sent to the printer prior to sending any data to print. The label format is defined in an M routine, which is then defined in the OPEN EXECUTE field (#6) of the TERMINAL TYPE file (#3.2).

Two sample formats are provided with patch DG\*5.3\*571 in routine DGPLBL1.

The entry point HINTERM^DGPLBL1 creates a horizontal format label and the entry point VINTERM^DGPLBL1 creates a vertical format label. The following setup examples show the OPEN EXECUTE (#6) and CONTROL CODES (#55) field values that were used in the development process and are provided to guide the user in this setup.

The examples are based on a 1 ½ by 3 ½ inch label.

Example: Control Codes Setup for Horizontal Labels

OPEN EXECUTE: D HINTERM^DGPLBL1

NUMBER: 1

ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION

CONTROL CODE: W "\<STX\>R;\<ETX\>",!

NUMBER: 2

ABBREVIATION: SL

FULL NAME: START LABEL

CONTROL CODE: W "\<STX\>\<ESC\>E2\<ETX\>",!,"\<STX\>\<CAN\>\<ETX\>",!

NUMBER: 3

ABBREVIATION: ST

FULL NAME: START TEXT

CONTROL CODE: W "\<STX\>”

NUMBER: 4

ABBREVIATION: ET

FULL NAME: END TEXT

CONTROL CODE: W "\<CR\>\<ETX\>",!

NUMBER: 5

ABBREVIATION: EL

FULL NAME: END LABEL

CONTROL CODE: W "\<STX\>\<ETB\>\<ETX\>",!

EXAMPLE: CONTROL CODES SETUP FOR VERTICAL LABELS

OPEN EXECUTE: D VINTERM^DGPLBL1

NUMBER: 1

ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION

CONTROL CODE: W "\<STX\>R;\<ETX\>",!

NUMBER: 2

ABBREVIATION: SL

FULL NAME: START LABEL

CONTROL CODE: W "\<STX\>\<ESC\>E2\<ETX\>",!,"\<STX\>\<CAN\>\<ETX\>",!

NUMBER: 3

ABBREVIATION: ST

FULL NAME: START TEXT

CONTROL CODE: W "\<STX\>”

NUMBER: 4

ABBREVIATION: ET

FULL NAME: END TEXT

CONTROL CODE: W "\<CR\>\<ETX\>",!

NUMBER: 5

ABBREVIATION: EL

FULL NAME: END LABEL

CONTROL CODE: W "\<STX\>\<ETB\>\<ETX\>",!

# HL7 Interface Specification for Transmission of Ambulatory Care Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="p4" class="anchor"></span>NOTE:  Starting October 1, 2018, the Ambulatory Care nightly job and Performance Monitor data extract daily transmissions, and monthly APM Performance Monitor Task generated from each VistA site are no longer needed to be sent to the AITC; the NPCDB is being shut down in Austin and the Corporate Data Warehouse (CDW) is replacing the database as the authoritative source. The VistA extracts done to populate the CDW will replace the need for the HL7 transmission.

This transmission has been stopped with Scheduling patch SD\*5.3\*640. This patch release includes:

- Disable AMB-CARE and SDPM logical links in the HL LOGICAL LINK file (#870).
- Unschedule the following three tasks:
  - Ambulatory Care Nightly Transmission to NPCDB \[SCDX AMBCAR NIGHTLY XMIT\]
  - Nightly job for PM data extract \[SDOQM PM NIGHTLY JOB\]
  - Schedule APM Performance Monitor Task \[SCRPW APM TASK JOB\].
- Place the following options ‘out of order’:
- Ambulatory Care Nightly Transmission to NPCDB \[SCDX AMBCAR NIGHTLY XMIT\]
- Retransmit Ambulatory Care Data by Date Range \[SCDX AMBCAR RETRANS BY DATE\]
- Retransmit Selected Error Code \[SCDX AMBCAR RETRANS ERROR\]
- Selective Retransmission of NPCDB Rejections \[SCDX AMBCAR RETRANS SEL REJ\]
- Schedule APM Performance Monitor Task \[SCRPW APM TASK JOB\]
- Performance Monitor Retransmit Report (AAC) \[SCRPW PM RETRANSMIT REPORT\]
- Nightly job for PM data extract \[SDOQM PM NIGHTLY JOB\]

This interface specification specifies the information needed for Ambulatory Care data reporting. This data exchange will be triggered by specific outpatient events that relate to workload credit in VISTA. The basic communication protocol will be addressed, as well as the information that will be made available and how it will be obtained.

This application uses an abstract message approach and encoding rules specified by HL7. HL7 is used for communicating data associated with various events which occur in health care environments. For example, when a check out occurs in VISTA, the event will trigger an update patient information message. This message is an unsolicited transaction to all external systems interfacing with VISTA.

The formats of these messages conform to the Version 2.3 HL7 Interface Standards where applicable. HL7 custom message formats ("Z" segments) are used only when necessary.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assumptions have been made at the beginning of this project in order to help define the scope and meet the initial needs in interfacing with the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)).

### Message Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data sent in the HL7 messages will be limited to the information that can be processed by the AITC, with the exception of the PID and ZPD segments, which will be populated using the nationally supported VISTA call. The data sent will also be limited to what is available in VISTA.

In order to capture the most information, specific outpatient events will generate messages to the AITC systems. This is not intended to cover all possible outpatient events, only those events which may result in the capture of workload information and data needed to update the National Patient Care Database (NPCDB).

The mode for capturing data for outpatient events was chosen to capture as much of the data as possible. (See Data Capture and Transmission (1.2.2) for further information on the mode for capturing the outpatient events.)

### Data Capture and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When AICS, PIMS, and PCE options or calls are used to update specific outpatient encounter data in VISTA, these events and changes will be captured. Any changes made to the VISTA database in non-standard ways, such as a direct global set by an application or by MUMPS code, will not be captured.

### Background Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A nightly background job will be sending HL7 messages for each outpatient encounter event for the day.

### Batch Messages & Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Batch messages will be used to transmit the outpatient encounter events.

Each batch message sent will be acknowledged at the application level. The batch acknowledgment will contain acknowledgment messages only for those messages containing errors.

Using this mode, it is possible that an empty batch acknowledgment will be sent. This will happen only when all messages in the batch being acknowledged were accepted.

### VA MailMan Lower Level Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 V. 1.6 of the VA MailMan lower level protocol (LLP) will be used. This version of the VA MailMan LLP differs from HL7 V. 1.5 in that a blank line is placed between each segment in the message \[denoting a carriage return\].

## HL7 Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the HL7 control segments supported by VistA. The messages are presented separately and defined by category. Segments are also described. The messages are presented in the following categories:

- Message Control
- Unsolicited Transactions from VistA (Section 3)

## Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the VISTA perspective, all incoming or outgoing messages are handled or generated based on an event.

In this section, and the following sections, these elements will be defined for each message:

- The trigger events
- The message event code
- A list of segments used in the message
- A list of fields for each segment in the message

Each message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. A \[ \] indicates the segment is optional, the { } indicates the segment is repeatable.

For each message category there will be a list of HL7 standard segments or "Z" segments used for the message.

## Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each segment, the data elements are described in table format. The table includes the sequence number (SEQ), maximum length (LEN), data type (DT), required or optional (R/O), repeatable (RP/#), the table number (TBL \#), the element name, and the VISTA description.

Each segment is described in the following sections.

## Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments which are contained in message types described in this document. These are generic descriptions.

Any time any of the segments described in this section are included in a message in this document, the VISTA descriptions and mappings will be as specified here, unless otherwise specified in that section.

### MSH - MESSAGE HEADER SEGMENTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sequences are as follows

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 19%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="8"><strong>MSH - MESSAGE HEADER SEGMENT</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SEQ</td>
<td>LEN</td>
<td>DT</td>
<td>R/O</td>
<td>RP/#</td>
<td>TBL#</td>
<td>ELEMENT NAME</td>
<td>VISTA DESCRIPTION</td>
</tr>
<tr class="even">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td>Recommended value is ^ (caret)</td>
</tr>
<tr class="odd">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<p>Component = ~ (tilde)</p>
<p>Repeat = | (bar)</p>
<p>Escape = \ (back slash)</p>
<p>Subcomponent = &amp; (ampersand)</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td><p>When originating from facility:</p>
<p>AMBCARE-DH441</p>
<p>When originating from NPCDB NPCD-AAC*</p></td>
</tr>
<tr class="odd">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td><p>When originating from facility:</p>
<p>Station's facility number</p>
<p>When originating from NPCDB: 200</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Date and time message was created</td>
</tr>
<tr class="odd">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p>2 Components</p>
<p>Component 1: Refer to Table 0076</p>
<p>Component 2: Refer to Table 0003</p></td>
</tr>
<tr class="odd">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by VISTA HL7 Package</td>
</tr>
<tr class="even">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td>P (production)</td>
</tr>
<tr class="odd">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>2.3 (Version 2.3)</td>
</tr>
<tr class="even">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td>NE (never acknowledge)</td>
</tr>
<tr class="odd">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td>AL (always acknowledge)</td>
</tr>
<tr class="even">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td colspan="8">*AAC stands for Austin Automation Center. The name of that facility has been changed to Austin Information Technology Center.</td>
</tr>
</tbody>
</table>

### BHS - Batch Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>R/O</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><strong>ELEMENT NAME</strong></th>
<th><strong>V<em>IST</em>A DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Batch Field Separator</td>
<td>Recommended value is <strong>^</strong> (caret)</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Batch Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<p>Component = <strong>~</strong> (tilde)</p>
<p>Repeat = <strong>|</strong> (bar)</p>
<p>Escape = <strong>\</strong> (back slash)</p>
<p>Subcomponent = <strong>&amp;</strong> (ampersand)</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Sending Application</td>
<td><p>When originating from facility:</p>
<p><strong>AMBCARE-DH142</strong></p>
<p>When originating from NPCDB:</p>
<p><strong>NPCD-AAC*</strong></p></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Sending Facility</td>
<td><p>When originating from facility:</p>
<p>Station's facility number</p>
<p>When originating from NPCDB:</p>
<p><strong>200</strong></p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Receiving Application</td>
<td><p>When originating from facility:</p>
<p><strong>NPCD-AAC</strong></p>
<p>When originating from NPCDB:</p>
<p><strong>AMBCARE-DH142</strong></p></td>
</tr>
<tr class="even">
<td>6</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Receiving Facility</td>
<td><p>When originating from facility:</p>
<p><strong>200</strong></p>
<p>When originating from NPCDB:</p>
<p>Station’s facility number</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Batch Creation Date/Time</td>
<td>Date and time batch message was created</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Security</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td></td>
<td><em>20</em></td>
<td><em>ST</em></td>
<td></td>
<td></td>
<td></td>
<td><em>Batch Name/ID/Type</em></td>
<td><p><em>4 Components</em><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><em>:</em></p>
<p><em>Component 1: Not used</em></p>
<p><em>Component 2: <strong>P</strong></em></p>
<p><em>Component 3: <strong>ADT|Z00</strong></em></p>
<p><em>Component 4: <strong>2.3</strong></em></p></td>
</tr>
<tr class="even">
<td>10</td>
<td>80</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Comment</td>
<td><p>2 Components<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a>:</p>
<p>Component 1: <em>Refer to Table 0008</em></p>
<p>Component 2: Text Message</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Control ID</td>
<td>Automatically generated by <strong>V<em>IST</em>A</strong> HL7 Package</td>
</tr>
<tr class="even">
<td>12</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Reference Batch Control ID</td>
<td>Batch Control ID of batch message being acknowledged</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"></li>
<li id="fn2"><p>The <strong>V</strong><em>IST</em><strong>A</strong> HL7 package has placed special meaning on this field. Note that this field is only used with batch acknowledgments.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

The VISTA HL7 package has placed special meaning on this field.

\*AAC stands for Austin Automation Center. The name of that facility has been changed to Austin Information Technology Center.

### BTS - Batch Trailer Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BTS - BATCH TRAILER SEGMENT

| SEQ | LEN | DT | R/O | RP/# | TBL# | ELEMENT NAME    | V*IST*A DESCRIPTION         |
|---------|---------|--------|---------|----------|----------|---------------------|---------------------------------|
| 1       | 10      | ST     |         |          | 0093     | Batch Message Count | Number of messages within batch |
| 2       | 80      | ST     |         |          | 0094     | Batch Comment       | Not used                        |
| 3       | 100     | CM     |         | Y        | 0095     | Batch Totals        | Not used                        |

### MSA - MESSAGE ACKNOWLEDGMENT SEGMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT | R/O | RP/# | TBL# | ELEMENT NAME            | V*IST*A DESCRIPTION                                                  |
|---------|---------|--------|---------|----------|----------|-----------------------------|--------------------------------------------------------------------------|
| 1       | 2       | ID     | R       |          | 0008     | Acknowledgment Code         | *Refer to Table 0008*                                                    |
| 2       | 20      | ST     | R       |          |          | Message Control ID          | Message Control ID of message being acknowledged                         |
| 3       | 80      | ST     |         |          | NPCD 001 | Text Message                | Repetitive list of error codes denoting why the message was rejected[^1] |
| 4       | 15      | NM     |         |          |          | Expected Sequence Number    | Not used                                                                 |
| 5       | 1       | ID     |         |          | 0102     | Delayed Acknowledgment Type | Not used                                                                 |
| 6       | 100     | CE     |         |          |          | Error Condition             | Not used                                                                 |

### EVN - EVENT TYPE SEGMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT | R/O | RP/# | TBL# | ELEMENT NAME        | V*IST*A DESCRIPTION  |
|---------|---------|--------|---------|----------|----------|-------------------------|--------------------------|
| 1       | 3       | ID     | R       |          | 0003     | Event Type Code         | *Refer to Table 0003*    |
| 2       | 26      | TS     | R       |          |          | Date/Time of Event      | Date/Time Event Occurred |
| 3       | 26      | TS     |         |          |          | Date/Time Planned Event | Not used                 |
| 4       | 3       | ID     |         |          | 0062     | Event Reason Code       | Not used                 |
| 5       | 60      | CN     |         |          | 0188     | Operator ID             | Not used                 |

## PID - Patient Identification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to “Section 3.15.PID-Patient Identification Segment” in the “MPI/PD HL7 Interface Specification” manual found on the VistA Documentation Library (VDL) at the following address.

<http://www.va.gov/vdl/application.asp?appid=16>

### PD1 - Patient Additional Demographic Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>V<em>IST</em>A DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td>Y</td>
<td>0223</td>
<td>LIVING DEPENDENCY</td>
<td>NOT USED</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0220</td>
<td>LIVING ARRANGEMENT</td>
<td>NOT USED</td>
</tr>
<tr class="odd">
<td>3</td>
<td>90</td>
<td>XON</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>PATIENT PRIMARY FACILITY<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td><p><u>8 COMPONENTS</u></p>
<p>FACILITY NAME</p>
<p>NOT USED</p>
<p>FACILITY NUMBER</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>90</td>
<td>XCN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>PATIENT PRIMARY CARE PROVIDER NAME &amp; ID NO.</td>
<td><p><u>14 COMPONENTS</u></p>
<p><u>2 SUB-COMPONENTS</u></p>
<p>POINTER TO ENTRY IN NEW PERSON FILE (#200)</p>
<p>FACILITY NUMBER</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>THIS WILL ALWAYS BE VA200 (NEW PERSON FILE)</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p>
<p>NOT USED</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0231</td>
<td>STUDENT INDICATOR</td>
<td>NOT USED</td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0295</td>
<td>HANDICAP</td>
<td>NOT USED</td>
</tr>
<tr class="odd">
<td>7</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0315</td>
<td>LIVING WILL</td>
<td>NOT USED</td>
</tr>
<tr class="even">
<td>8</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0316</td>
<td>ORGAN DONOR</td>
<td>NOT USED</td>
</tr>
<tr class="odd">
<td>9</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>SEPARATE BILL</td>
<td>NOT USED</td>
</tr>
<tr class="even">
<td>10</td>
<td>2</td>
<td>CX</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>DUPLICATE PATIENT</td>
<td>NOT USED</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0125</td>
<td>PUBLICITY INDICATOR</td>
<td>NOT USED</td>
</tr>
<tr class="even">
<td>12</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>01293</td>
<td>PROTECTION INDICATOR</td>
<td>NOT USED</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>This element is only available from CIRN enabled facilities.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

### PV1 - Patient Visit Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN   | DT  | R/O | RP/# | TBL# | ELEMENT NAME              | V*IST*A DESCRIPTION                                     |
|-----|-------|-----|-----|------|------|---------------------------|---------------------------------------------------------|
| 1   | 4     | SI  |     |      |      | Set ID - Patient Visit    | Sequential Number                                       |
| 2   | 1     | ID  | R   |      | 0004 | Patient Class             | This will always be O (outpatient)                      |
| 3   | 12    | CM  |     |      |      | Assigned Patient Location | Not used                                                |
| 4   | 4     | ID  |     |      | 0007 | Admission Type            | *Refer to Table SD009 (Purpose of Visit)*               |
| 5   | 20    | ST  |     |      |      | Preadmit Number           | Not used                                                |
| 6   | 12    | CM  |     |      |      | Prior Patient Location    | Not used                                                |
| 7   | 60    | CN  |     |      | 0010 | Attending Doctor          | Not used                                                |
| 8   | 60    | CN  |     |      | 0010 | Referring Doctor          | Not used                                                |
| 9   | 60    | CN  |     | Y    | 0010 | Consulting Doctor         | Not used                                                |
| 10  | 3     | ID  |     |      | 0069 | Hospital Service          | Not used                                                |
| 11  | 12    | CM  |     |      |      | Temporary Location        | Not used                                                |
| 12  | 2     | ID  |     |      | 0087 | Preadmit Test Indicator   | Not used                                                |
| 13  | 2     | ID  |     |      | 0092 | Readmission Indicator     | Not used                                                |
| 14  | 3     | ID  |     |      | 0023 | Admit Source              | *Refer to Table 0023 (Location of Visit)*               |
| 15  | 2     | ID  |     | Y    | 0009 | Ambulatory Status         | Not used                                                |
| 16  | 2     | ID  |     |      | 0099 | VIP Indicator             | Not used                                                |
| 17  | 60    | CN  |     |      | 0010 | Admitting Doctor          | Not used                                                |
| 18  | 2     | ID  |     |      | 0018 | Patient Type              | Not used                                                |
| 19  | 15    | NM  |     |      |      | Visit Number              | Pointer to entry in OUTPATIENT ENCOUNTER file (#409.68) |
| 20  | 50    | CM  |     | Y    | 0064 | Financial Class           | Not used                                                |
| 21  | 2     | ID  |     |      | 0032 | Charge Price Indicator    | Not used                                                |
| 22  | 2     | ID  |     |      | 0045 | Courtesy Code             | Not used                                                |
| 23  | 2     | ID  |     |      | 0046 | Credit Rating             | Not used                                                |
| 24  | 2     | ID  |     | Y    | 0044 | Contract Code             | Not used                                                |
| 25  | 8     | DT  |     | Y    |      | Contract Effective Date   | Not used                                                |
| 26  | 12    | NM  |     | Y    |      | Contract Amount           | Not used                                                |
| 27  | 3     | NM  |     | Y    |      | Contract Period           | Not used                                                |
| 28  | 2     | ID  |     |      | 0073 | Interest Code             | Not used                                                |
| 29  | 1     | ID  |     |      | 0110 | Transfer to Bad Debt Code | Not used                                                |
| 30  | 8     | DT  |     |      |      | Transfer to Bad Debt Date | Not used                                                |
| 31  | 10    | ID  |     |      | 0021 | Bad Debt Agency Code      | Not used                                                |
| 32  | 12    | NM  |     |      |      | Bad Debt Transfer Amount  | Not used                                                |
| 33  | 12    | NM  |     |      |      | Bad Debt Recovery Amount  | Not used                                                |
| 34  | 1     | ID  |     |      | 0111 | Delete Account Indicator  | Not used                                                |
| 35  | 8     | DT  |     |      |      | Delete Account Date       | Not used                                                |
| 36  | 3     | ID  |     |      | 0112 | Discharge Disposition     | Not used                                                |
| 37  | 25    | CM  |     |      | 0113 | Discharged to Location    | Not used                                                |
| 38  | 2     | ID  |     |      | 0114 | Diet Type                 | Not used                                                |
| 39  | 7[^2] | ID  |     |      | 0115 | Servicing Facility        | Facility number and suffix                              |
| 40  | 1     | ID  |     |      | 0116 | Bed Status                | Not used                                                |
| 41  | 2     | ID  |     |      | 0117 | Account Status            | Not used                                                |
| 42  | 12    | CM  |     |      |      | Pending Location          | Not used                                                |
| 43  | 12    | CM  |     |      |      | Prior Temporary Location  | Not used                                                |
| 44  | 26    | TS  |     |      |      | Admit Date/Time           | Date/time of encounter                                  |
| 45  | 26    | TS  |     |      |      | Discharge Date/Time       | Not used                                                |
| 46  | 12    | NM  |     |      |      | Current Patient Balance   | Not used                                                |
| 47  | 12    | NM  |     |      |      | Total Charges             | Not used                                                |
| 48  | 12    | NM  |     |      |      | Total Adjustments         | Not used                                                |
| 49  | 12    | NM  |     |      |      | Total Payments            | Not used                                                |
| 50  | 20    | CM  |     |      |      | Alternate Visit ID        | Unique Identifier (PCE)                                 |

### PV2 - Patient Visit - Additional Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 31%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>ELEMENT NAME</th>
<th><p>Vista</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>80</td>
<td>PL</td>
<td>C</td>
<td></td>
<td></td>
<td>00181</td>
<td>Prior Pending Location</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>2</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0129</td>
<td>00182</td>
<td>Accommodation Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00183</td>
<td>Admit Reason</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00184</td>
<td>Transfer Reason</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>5</td>
<td>25</td>
<td>ST</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00185</td>
<td>Patient Valuables</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>6</td>
<td>25</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00186</td>
<td>Patient Valuables Location</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td>Y</td>
<td>0130</td>
<td>00187</td>
<td>Visit User Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00188</td>
<td>Expected Admit Date/Time</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00189</td>
<td>Expected Discharge Date/Time</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>3</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00711</td>
<td>Estimated Length of Inpatient Stay</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>3</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00712</td>
<td>Actual Length of Inpatient Stay</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>12</td>
<td>50</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00713</td>
<td>Visit Description</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>13</td>
<td>250</td>
<td>XCN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00714</td>
<td>Referral Source Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00715</td>
<td>Previous Service Date</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00716</td>
<td>Employment Illness Related Indicator</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0213</td>
<td>00717</td>
<td>Purge Status Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>17</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00718</td>
<td>Purge Status Date</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>18</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0214</td>
<td>00719</td>
<td>Special Program Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>19</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00720</td>
<td>Retention Indicator</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>20</td>
<td>1</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00721</td>
<td>Expected Number of Insurance Plans</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>21</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0215</td>
<td>00722</td>
<td>Visit Publicity Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td>Y</td>
<td>0136</td>
<td>00723</td>
<td>Visit Protection Indicator</td>
<td>Visit Protection Indicator</td>
</tr>
<tr class="odd">
<td>23</td>
<td>250</td>
<td>XON</td>
<td>O</td>
<td></td>
<td></td>
<td>00724</td>
<td>Clinic Organization Name</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>24</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0216</td>
<td>00725</td>
<td>Patient Status Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>25</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0217</td>
<td>00726</td>
<td>Visit Priority Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>26</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00727</td>
<td>Previous Treatment Date</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>27</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0112</td>
<td>00728</td>
<td>Expected Discharge Disposition</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>28</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00729</td>
<td>Signature on File Date</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>29</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00730</td>
<td>First Similar Illness Date</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>30</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0218</td>
<td>00731</td>
<td>Patient Charge Adjustment Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>31</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0219</td>
<td>00732</td>
<td>Recurring Service Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>32</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00733</td>
<td>Billing Media Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>33</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00734</td>
<td>Expected Surgery Date and Time</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>34</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00735</td>
<td>Military Partnership Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>35</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00736</td>
<td>Military Non-Availability Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>36</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00737</td>
<td>Newborn Baby Indicator</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>37</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00738</td>
<td>Baby Detained Indicator</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>38</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0430</td>
<td>01543</td>
<td>Mode of Arrival Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>39</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0431</td>
<td>01544</td>
<td>Recreational Drug Use Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>40</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0432</td>
<td>01545</td>
<td>Admission Level of Care Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>41</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0433</td>
<td>01546</td>
<td>Precaution Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>42</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0434</td>
<td>01547</td>
<td>Patient Condition Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>43</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0315</td>
<td>00759</td>
<td>Living Will Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>44</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0316</td>
<td>00760</td>
<td>Organ Donor Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>45</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0435</td>
<td>01548</td>
<td>Advance Directive Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>46</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>01549</td>
<td>Patient Status Effective Date</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>47</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>01550</td>
<td>Expected LOA Return Date/Time</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>48</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>01841</td>
<td>Expected Pre-admission Testing Date/Time</td>
<td>Not used</td>
</tr>
</tbody>
</table>

### DG1 - Diagnosis Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VISTA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>Set ID ‑ Diagnosis</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0053</td>
<td>Diagnosis Coding Method</td>
<td><p>I9 = ICD-9-CM</p>
<p>I10 = ICD-10-CM</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>8</td>
<td>CE</td>
<td>R</td>
<td></td>
<td>0051</td>
<td>Diagnosis Code</td>
<td><p>Diagnosis code from OUTPATIENT DIAGNOSIS (#409.43) and ICD DIAGNOSIS (#80) files</p>
<p>Refer to Table 0051 for sample listing of possible values</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>60</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Diagnosis Description</td>
<td><p>Corresponding diagnosis description from ICD DIAGNOSIS (#80) file</p>
<p>Refer to Table 0051 for sample listing of possible values</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Diagnosis Date/Time</td>
<td>Date/time of encounter</td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0052</td>
<td>Diagnosis Type</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td>0118</td>
<td>Major Diagnostic Category</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>4</td>
<td>ID</td>
<td></td>
<td></td>
<td>0055</td>
<td>Diagnostic Related Group</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>DRG Approval Indicator</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0056</td>
<td>DRG Grouper Review Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td>0083</td>
<td>Outlier Type</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>12</td>
<td>3</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Outlier Days</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>13</td>
<td>12</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Outlier Cost</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>4</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Grouper Version And Type</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>NM</td>
<td><span id="icdp183" class="anchor"></span><mark>O</mark></td>
<td></td>
<td></td>
<td>Diagnosis Priority</td>
<td>Will contain 1 if this is the primary diagnosis for the episode</td>
</tr>
<tr class="even">
<td>16</td>
<td>60</td>
<td>CN</td>
<td></td>
<td></td>
<td></td>
<td>Diagnosing Clinician</td>
<td>Not used</td>
</tr>
</tbody>
</table>

### PR1 - Procedure Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>V<em>IST</em>A DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>Set ID - Procedure</td>
<td>Sequential Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0089</td>
<td>Procedure Coding Method</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td>CE</td>
<td>R</td>
<td></td>
<td>0088</td>
<td>Procedure Code</td>
<td><p>3 Components:</p>
<p>1. Procedure Code</p>
<p>2. Corresponding procedure description from CPT file (#81)</p>
<p>3. Coding Method (this will always be C4)</p>
<p><em>Refer to Table 0088 for sample listing of possible procedure codes and descriptions</em></p></td>
</tr>
<tr class="even">
<td>4</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Procedure Description</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Procedure Date/Time</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0090</td>
<td>Procedure Type</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>4</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Procedure Minutes</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>60</td>
<td>CN</td>
<td></td>
<td></td>
<td></td>
<td>Anesthesiologist</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0019</td>
<td>Anesthesia Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>4</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Anesthesia Minutes</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>60</td>
<td>CN</td>
<td></td>
<td></td>
<td></td>
<td>Surgeon</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>12</td>
<td>60</td>
<td>CM</td>
<td></td>
<td>Y</td>
<td></td>
<td>Procedure Practitioner</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>13</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0059</td>
<td>Consent Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>2</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Procedure Priority</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>80</td>
<td>CD</td>
<td></td>
<td></td>
<td></td>
<td>Associated Diagnosis Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>16</td>
<td>80</td>
<td>CE</td>
<td></td>
<td>Y</td>
<td>0340</td>
<td>Procedure Code Modifier</td>
<td><p>3 Components:</p>
<p>1. Modifier Code</p>
<p>2. Corresponding modifier</p>
<p>description from CPT</p>
<p>MODIFIER file (#81.3)</p>
<p>3. Coding Method C=CPT</p>
<p>H=HCPCS</p>
<p><em>Refer to Table 0340 for sample</em></p>
<p><em>listing of possible modifier</em></p>
<p><em>codes and descriptions</em></p></td>
</tr>
</tbody>
</table>

### ### ROL - Role Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>V<em>IST</em>A DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>60</td>
<td>EI</td>
<td>R</td>
<td></td>
<td></td>
<td>Role Instance ID</td>
<td><p><u>4 Components</u></p>
<p>Entity Identifier<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a> <a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0287</td>
<td>Action Code</td>
<td>This will always be CO (correct)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>Role</td>
<td><p><u>6 Components</u></p>
<p>Provider Type Code</p>
<p>Not used</p>
<p>This will always be VA8932.1 (PERSON CLASS file)</p>
<p>Primary Encounter Provider Designation</p>
<p>Not used</p>
<p>This will always be VA01</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>80</td>
<td>XCN</td>
<td>R</td>
<td>Y/2</td>
<td></td>
<td>Role Person</td>
<td><p><u>14 Components</u></p>
<p><strong>Repetition 1</strong></p>
<p><u>2 Sub-Components</u></p>
<p>Pointer to entry in NEW PERSON file (#200)</p>
<p>Facility Number</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>This will always be <strong>VA200</strong> (NEW PERSON file)</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p><strong>Repetition 2</strong></p>
<p>SSN</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>This will always be <strong>SSA</strong> (Social Security Administration)</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Role Begin Date/Time</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Role End Date/Time</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>80</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Role Duration</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>80</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Role Action Reason</td>
<td>Not used</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>This element will be 1-15 characters/digits followed by a hyphen (-) followed by 3 characters/digits followed by a hyphen (-) followed by 1-15 digits followed by an asterisk (*) followed by 1-4 digits. (Ex: 123AZ-ALB-1934*1)<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>The trailing set of digits (i.e., everything to the right of the asterisk) are an appended Set ID and should be treated as such.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

### ZPD - VA-Specific Patient Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#   | V*IST*A ELEMENT NAME                  |
|-----|-----|-----|-----|------|--------|---------------------------------------|
| 1   | 4   | SI  | R   |      |        | SET ID - PATIENT ID                   |
| 2   | 60  | ST  |     |      |        | REMARKS                               |
| 3   | 20  | ST  |     |      |        | PLACE OF BIRTH CITY                   |
| 4   | 2   | ST  |     |      |        | PLACE OF BIRTH STATE                  |
| 5   | 2   | ID  |     |      | VA02   | CURRENT MEANS TEST STATUS             |
| 6   | 35  | ST  |     |      |        | FATHER'S NAME                         |
| 7   | 35  | ST  |     |      |        | MOTHER'S NAME                         |
| 8   | 1   | ID  |     |      | VA01   | RATED INCOMPETENT                     |
| 9   | 19  | TS  |     |      |        | DATE OF DEATH                         |
| 10  | 48  | PN  |     |      |        | COLLATERAL SPONSOR                    |
| 11  | 1   | ID  |     |      | VA01   | ACTIVE HEALTH INSURANCE?              |
| 12  | 1   | ID  |     |      | VA01   | COVERED BY MEDICAID?                  |
| 13  | 19  | TS  |     |      |        | DATE MEDICAID LAST ASKED              |
| 14  | 1   | ID  |     |      | VA07   | RACE[^3]                              |
| 15  | 3   | ID  |     |      | VA08   | RELIGION[^4]                          |
| 16  | 1   | ID  |     |      | VA01   | HOMELESS INDICATOR                    |
| 17  | 1   | ID  |     |      |        | POW STATUS INDICATED?                 |
| 18  | 2   | ID  |     |      | VA12   | TYPE OF INSURANCE                     |
| 19  | 1   | ID  |     |      | VA14   | MEDICATION COPAYMENT EXEMPTION STATUS |
| 20  | 1   | ID  |     |      | VA0023 | PRISONER OF WAR LOCATION CODE         |
| 21  | 30  | ST  |     |      |        | PRIMARY CARE TEAM                     |

### ZEL - VA-Specific Patient Eligibility Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#   | V*IST*A ELEMENT NAME                       |
|-----|-----|-----|-----|------|--------|--------------------------------------------|
| 1   | 4   | SI  | R   |      |        | SET ID                                     |
| 2   | 2   | ID  |     |      | VA04   | ELIGIBILITY CODE                           |
| 3   | 16  | CK  |     |      |        | LONG ID                                    |
| 4   | 12  | ST  |     |      |        | SHORT ID                                   |
| 5   | 1   | ID  |     |      | VA05   | DISABILITY RETIREMENT FROM MIL.            |
| 6   | 8   | NM  |     |      |        | CLAIM FOLDER NUMBER                        |
| 7   | 40  | ST  |     |      |        | CLAIM FOLDER LOCATION                      |
| 8   | 1   | ID  |     |      | VA01   | VETERAN?                                   |
| 9   | 30  | ST  |     |      |        | TYPE OF PATIENT                            |
| 10  | 1   | ID  |     |      | VA06   | ELIGIBILITY STATUS                         |
| 11  | 8   | DT  |     |      |        | ELIGIBILITY STATUS DATE                    |
| 12  | 8   | DT  |     |      |        | ELIGIBILITY INTERIM RESPONSE               |
| 13  | 50  | ST  |     |      |        | ELIGIBILITY VERIFICATION METHOD            |
| 14  | 1   | ID  |     |      | VA01   | RECEIVING A&A BENEFITS?                    |
| 15  | 1   | ID  |     |      | VA01   | RECEIVING HOUSEBOUND BENEFITS?             |
| 16  | 1   | ID  |     |      | VA01   | RECEIVING A VA PENSION?                    |
| 17  | 1   | ID  |     |      | VA01   | RECEIVING A VA DISABILITY?                 |
| 18  | 1   | ID  |     |      | VA01   | EXPOSED TO AGENT ORANGE                    |
| 19  | 1   | ID  |     |      | VA01   | RADIATION EXPOSURE INDICATED?              |
| 20  | 1   | ID  |     |      | VA01   | SW ASIA CONDITIONS?                        |
| 21  | 5   | NM  |     |      |        | TOTAL ANNUAL VA CHECK AMOUNT               |
| 22  | 1   | ID  |     |      | VA0022 | RADIATION EXPOSURE METHOD CODE             |
| 23  | 1   | ID  |     |      | VA0036 | MILITARY SEXUAL TRAUMA STATUS              |
| 24  | 8   | DT  |     |      |        | DATE MILITARY SEXUAL TRAUMA STATUS CHANGED |
| 25  | 7   | ID  |     |      | VA0115 | SITE DETERMINING MST STATUS                |
| 26  | 8   | DT  |     |      |        | AGENT ORANGE REGISTRATION DATE             |
| 27  | 8   | DT  |     |      |        | AGENT ORANGE EXAM DATE                     |
| 28  | 6   | NM  |     |      |        | AGENT ORANGE REGISTRATION \#               |
| 29  | 1   | ID  |     |      | VA0046 | AGENT ORANGE EXPOSURE LOCATION             |
| 30  | 8   | DT  |     |      |        | RADIATION REGISTRATION DATE                |
| 31  | 8   | DT  |     |      |        | SW ASIA COND EXAM DATE                     |
| 32  | 8   | DT  |     |      |        | SW ASIA COND REGISTRATION DATE             |
| 33  | 8   | DT  |     |      |        | MONETARY BEN. VERIFY DATE                  |
| 34  | 8   | DT  |     |      |        | USER ENROLLEE VALID THROUGH                |
| 35  |     |     |     |      |        | USER ENROLLEE SITE                         |
| 36  |     |     |     |      |        | ELIGIBILITY VERIFICATION SOURCE AND SITE   |
| 37  | 1   | ID  |     |      | VA01   | COMBAT VETERAN                             |
| 38  | 8   | DT  |     |      |        | COMBAT VETERAN STATUS END DATE             |
| 39  | 1   | ID  |     |      | VA01   | DISCHARGE DUE TO DISABILITY?               |
| 40  | 1   | ID  |     |      | VA01   | PROJECT 112/SHAD?                          |

### VA-Specific Income Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | V*IST*A ELEMENT NAME         |
|-----|-----|-----|-----|------|------|------------------------------|
| 1   | 4   | SI  | R   |      |      | SET ID                       |
| 2   | 1   | ID  |     |      | VA01 | MARRIED LAST CALENDAR YEAR   |
| 3   | 1   | ID  |     |      | VA01 | LIVED WITH PATIENT           |
| 4   | 8   | NM  |     |      |      | AMOUNT CONTRIBUTED TO SPOUSE |
| 5   | 1   | ID  |     |      | VA01 | DEPENDENT CHILDREN           |
| 6   | 1   | ID  |     |      | VA01 | INCAPABLE OF SELF-SUPPORT    |
| 7   | 1   | ID  |     |      | VA01 | CONTRIBUTED TO SUPPORT       |
| 8   | 1   | ID  |     |      | VA01 | CHILD HAD INCOME             |
| 9   | 1   | ID  |     |      | VA01 | INCOME AVAILABLE TO YOU      |
| 10  | 2   | NM  |     |      |      | NUMBER OF DEPENDENT CHILDREN |
| 11  | 2   | ST  |     |      |      | NUMBER OF DEPENDENTS         |
| 12  | 10  | NM  |     |      |      | PATIENT INCOME               |
| 13  | 2   | ID  |     |      | VA10 | MEANS TEST INDICATOR         |

### ZCL - VA-Specific Outpatient Classification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#  | VISTA ELEMENT NAME             |
|-----|-----|-----|-----|------|-------|--------------------------------|
| 1   | 4   | SI  | R   |      |       | SET ID                         |
| 2   | 2   | ID  | R   |      | SD008 | Outpatient Classification Type |
| 3   | 50  | ST  |     |      |       | Value                          |

### Zsc - VA-Specific Stop Code Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#  | VISTA ELEMENT NAME                |
|-----|-----|-----|-----|------|-------|-----------------------------------|
| 1   | 4   | SI  | R   |      |       | Sequential number                 |
| 2   | 4   | ID  | R   |      | SD001 | Stop Code                         |
| 3   | 30  | ST  |     |      | SD001 | Name                              |
| 4   | 1   | NM  |     |      |       | Cost Distribution Center          |
| 5   | 1   | ID  |     |      |       | Current Exempt. Fr Classification |

### ZSP - VA-Specific Service Period Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | V*IST*A ELEMENT NAME         |
|-----|-----|-----|-----|------|------|------------------------------|
| 1   | 4   | SI  | R   |      |      | SET ID                       |
| 2   | 1   | ID  | R   |      | VA01 | Service Connected?           |
| 3   | 3   | NM  |     |      |      | Service Connected Percentage |
| 4   | 2   | ID  |     |      | VA11 | Period of Service            |
| 5   | 1   | ST  |     |      |      | VIETNAM SERVICE INDICATED?   |
| 6   | 1   | ID  |     |      | VA01 | P&T                          |
| 7   | 1   | ID  |     |      | VA01 | UNEMPLOYABLE                 |
| 8   | 19  | TS  |     |      |      | SC AWARD DATE                |

### ZEN - VA-Specific Enrollment Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#   | V*IST*A ELEMENT NAME      |
|-----|-----|-----|-----|------|--------|---------------------------|
| 1   | 4   | SI  | R   |      |        | SET ID                    |
| 2   | 8   | DT  |     |      |        | ENROLLMENT DATE           |
| 3   | 1   | ID  |     |      | VA0024 | SOURCE OF ENROLLMENT      |
| 4   | 1   | ID  |     |      | VA0015 | ENROLLMENT STATUS         |
| 5   | 1   | ID  |     |      | VA0016 | REASON CANCELED/DECLINED  |
| 6   | 60  | TX  |     |      |        | CANCELED/DECLINED REMARKS |
| 7   | 7   | ID  |     |      | VA0115 | FACILITY RECEIVED         |
| 8   | 7   | ID  |     |      | VA0115 | PRIMARY FACILITY          |
| 9   | 1   | ID  |     |      | VA0021 | ENROLLMENT PRIORITY       |
| 10  | 8   | DT  |     |      |        | EFFECTIVE DATE            |

## PURPOSE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the HL7 message transactions that are necessary to support the outpatient database interface for the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)).

These messages will use the generic HL7 format, so that they can be expanded later to support new interfaces at other facilities.

## Trigger Events and Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each triggering event is listed below, along with the applicable form of the message to be exchanged. The notation used to describe the sequence, optionally, and repetition of segments is described in the HL7 Final Standard Manual, Chapter 2, Section 2.4.8, Chapter Formats for Defining Abstract Messages, and in summary form, in Section 2.1 of this document.

### Update Patient Information (A08)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Event Driver will be triggered under the following circumstances:

- When an outpatient appointment is checked out
- When a checked out outpatient appointment is edited
- When stop codes for an outpatient appointment are added or edited
- When a check out creates an occasion of service

Taking advantage of the outpatient event driver, this will trigger an A08 message to be sent. The receiving system will replace any data that exists with the “new” data that is transmitted with this message.

ADT ADT Message

MSH Message Header

EVN Event Type

PID Patient Identification

PD1 Patient Additional Demographic

PV1 Patient Visit

PV2 Patient Visit Additional Information

\[ { DG1 } \] Diagnosis Information

{ PR1 } Procedure Information

{ROL} Role

ZPD VA-Specific Patient Information

ZEL VA-Specific Patient Eligibility Information

ZIR VA-Specific Income

{ZCL} VA-Specific Outpatient Classification

{ZSC} VA-Specific Stop Code

ZSP VA-Specific Service Period

ZEN VA Specific Enrollment

ACK General Acknowledgment Message

MSH Message Header

MSA Message Acknowledgment

### Delete a Patient Record (A23)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a check out is deleted, this message instructs the receiver to delete the information for this patient’s visit.

ADT ADT Message

MSH Message Header

EVN Event Type

PID Patient Identification

PD1 Patient Additional Demographic

PV1 Patient Visit

ZPD VA-Specific Patient Information

ACK General Acknowledgment Message

MSH Message Header

MSA Message Acknowledgment

## SUPPORTED AND USER-DEFINED HL7 TABLES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TABLE 0001 - SEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

F FEMALE

M MALE

O OTHER

U UNKNOWN

### TABLE 0002 - MARITAL STATUS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

A SEPARATED

D DIVORCED

M MARRIED

S SINGLE

W WIDOWED

### TABLE 0003 - EVENT TYPE CODE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

A08 UPDATE PATIENT INFORMATION

A23 DELETE PATIENT RECORD

### TABLE 0008 - ACKNOWLEDGMENT CODE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

AA APPLICATION ACKNOWLEDGMENT: ACCEPT

AE APPLICATION ACKNOWLEDGMENT: ERROR

AR APPLICATION ACKNOWLEDGMENT: REJECT

CA ACCEPT ACKNOWLEDGMENT: COMMIT ACCEPT

CE ACCEPT ACKNOWLEDGMENT: COMMIT ERROR

CR ACCEPT ACKNOWLEDGMENT: COMMIT REJECT

### TABLE 0023 - ADMIT SOURCE (USER DEFINED)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Used for Location of Visit. Sample listing of possible values.

VALUE DESCRIPTION

1 THIS FACILITY

6 OTHER FACILITY

### TABLE 0051 - DIAGNOSIS CODE (USER DEFINED)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use ICD DIAGNOSIS (#80) file, Code Number (.01) for value and Diagnosis (3) for

Description. Sample listing of possible values.

VALUE DESCRIPTION

253.2 PANHYPOPITUITARISM

253.3 PITUITARY DWARFISM

253.4 ANTER PITUITARY DIS NEC

253.5 DIABETES INSIPIDUS

253.6 NEUROHYPOPHYSIS DIS NEC

253.7 IATROGENIC PITUITARY DIS

253.8 DISEASES OF THYMUS NEC

253.9 PITUITARY DISORDER NOS

254.1 ABSCESS OF THYMUS

254.8 DISEASES OF THYMUS NEC

254.9 DISEASE OF THYMUS NOS

255.1 HYPERALDOSTERONISM

255.2 ADRENOGENITAL DISORDERS

### TABLE 0069 - HOSPITAL SERVICE (USER DEFINED)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use SPECIALTY file (#42.4), PTF Code (.001). Sample listing of possible values.

VALUE DESCRIPTION

2 CARDIOLOGY

6 DERMATOLOGY

7 ENDOCRINOLOGY

8 GEM ACUTE MEDICINE

12 CORONARY CARE UNIT

12 EMERGENCY MEDICINE

15 GENERAL MEDICINE

21 BLIND REHAB

31 GEM INTERMEDIAT E CARE

55 EVAL/BRF TRMT PTSD

72 ALCOHOL

85 DOM

88 DOMICILIARY PTSD

91 GASTROENTEROLOGY

92 GEN INTERMEDIATE PSYCH

### TABLE 0076 - MESSAGE TYPE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

ADT ADT MESSAGE

ACK GENERAL ACKNOWLEDGMENT

### TABLE 0088 - PROCEDURE CODE (USER DEFINED)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample listing of possible values.

VALUE DESCRIPTION

10141 INCISION AND DRAINAGE OF HEMATOMA; COMPLICATED

### TABLE 0115 - SERVICING FACILITY (USER DEFINED)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample listing of possible values.

VALUE DESCRIPTION

512 9AC Perry Point (Nursing Home)

### TABLE 0133 - PROCEDURE PRACTITIONER TYPE (USER DEFINED)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample listing of possible values.

VALUE OCCUPATION SPECIALTY SUBSPECIALTY

V110000 Physicians (M.D.) and Osteopaths (D.O.)

V110100 Physicians (M.D.) and Osteopaths (D.O.) Addiction Medicine

V110300 Physicians (M.D.) and Osteopaths (D.O.) Allergy and Immunology

V110301 Physicians (M.D.) and Osteopaths (D.O.) Allergy and Immunology Clinical and Laboratory

V110200 Physicians (M.D.) and Osteopaths (D.O.) Allergy

V110400 Physicians (M.D.) and Osteopaths (D.O.) Anesthesiology

V110401 Physicians (M.D.) and Osteopaths (D.O.) Anesthesiology Critical Care

V110402 Physicians (M.D.) and Osteopaths (D.O.) Anesthesiology Pain Management

### TABLE 0136 - YES/NO INDICATOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

Y YES

N NO

### TABLE SD001 - SERVICE INDICATOR (STOP CODE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample listing of possible values.

VALUE DESCRIPTION

104 PULMONARY FUNCTION

105 X-RAY

106 EEG

107 EKG

108 LABORATORY

109 NUCLEAR MEDICINE

110 CARDIOVASCULAR NUCLEAR MED

111 ONCOLOGICAL NUCLEAR MED

112 INFECTIOUS DISEASE NUCLEAR MED

113 RADIONUCLIDE TREATMENT

114 SING PHOTON EMISS TOMOGRAPHY

115 ULTRASOUND

117 NURSING

118 HOME TREATMENT SERVICES

119 COMM NURSING HOME FOLLOW-UP

### TABLE SD008 - OUTPATIENT CLASSIFICATION TYPE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

1 AGENT ORANGE

2 IONIZING RADIATION

3 SERVICE CONNECTED

4 SW ASIA CONDITIONS

5 MILITARY SEXUAL TRAUMA

6 HEAD AND/OR NECK CANCER

7 COMBAT VETERAN

8 PROJECT 112/SHAD

### TABLE SD009 - PURPOSE OF VISIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Value denotes a combination of Purpose of Visit & Appointment Type.

VALUE PURPOSE OF VISIT APPOINTMENT TYPE

0101 C&P COMPENSATION & PENSION

0102 C&P CLASS II DENTAL

0103 C&P ORGAN DONORS

0104 C&P EMPLOYEE

0105 C&P PRIMA FACIA

0106 C&P RESEARCH

0107 C&P COLLATERAL OF VET.

0108 C&P SHARING AGREEMENT

0109 C&P REGULAR

0111 C&P SERVICE CONNECTED

0201 10-10 COMPENSATION & PENSION

0202 10-10 CLASS II DENTAL

0203 10-10 ORGAN DONORS

0204 10-10 EMPLOYEE

0205 10-10 PRIMA FACIA

0206 10-10 RESEARCH

0207 10-10 COLLATERAL OF VET.

0208 10-10 SHARING AGREEMENT

0209 10-10 REGULAR

0211 10-10 SERVICE CONNECTED

0301 SCHEDULED VISIT COMPENSATION & PENSION

0302 SCHEDULED VISIT CLASS II DENTAL

0303 SCHEDULED VISIT ORGAN DONORS

0304 SCHEDULED VISIT EMPLOYEE

0305 SCHEDULED VISIT PRIMA FACIA

0306 SCHEDULED VISIT RESEARCH

0307 SCHEDULED VISIT COLLATERAL OF VET.

0308 SCHEDULED VISIT SHARING AGREEMENT

0309 SCHEDULED VISIT REGULAR

0311 SCHEDULED VISIT SERVICE CONNECTED

0401 UNSCHED. VISIT COMPENSATION & PENSION

0402 UNSCHED. VISIT CLASS II DENTAL

0403 UNSCHED. VISIT ORGAN DONORS

0404 UNSCHED. VISIT EMPLOYEE

0405 UNSCHED. VISIT PRIMA FACIA

0406 UNSCHED. VISIT RESEARCH

0407 UNSCHED. VISIT COLLATERAL OF VET.

0408 UNSCHED. VISIT SHARING AGREEMENT

0409 UNSCHED. VISIT REGULAR

0411 UNSCHED. VISIT SERVICE CONNECTED

### TABLE VA01 - YES/NO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

0 NO

1 YES

N NO

Y YES

U UNKNOWN

### TABLE VA02 - CURRENT MEANS TEST STATUS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Type of Care (#.03) field of MEANS TEST STATUS (#408.32) file.

VALUE DESCRIPTION

D DISCRETIONARY

M MANDATORY

N NOT APPLICABLE

### TABLE VA04 - ELIGIBILITY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Name (#.01) field of MAS ELIGIBILITY CODE (#8.1) file.

VALUE DESCRIPTION

1 SERVICE CONNECTED 50% to 100%

2 AID & ATTENDANCE

3 SC LESS THAN 50%

4 NSC - VA PENSION

5 NSC

6 OTHER FEDERAL AGENCY

7 ALLIED VETERAN

8 HUMANITARIAN EMERGENCY

9 SHARING AGREEMENT

10 REIMBURSABLE INSURANCE

12 CHAMPVA

13 COLLATERAL OF VET.

14 EMPLOYEE

15 HOUSEBOUND

16 MEXICAN BORDER WAR

17 WORLD WAR I

18 PRISONER OF WAR

19 TRICARE/CHAMPUS

21 CATASTROPHIC DISABILITY

22 PURPLE HEART RECIPIENT

### TABLE VA05 - DISABILITY RETIREMENT FROM MILITARY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Disability Ret. From Military? (#.362) field of PATIENT (#2) file.

VALUE DESCRIPTION

0 NO

1 YES, RECEIVING MILITARY RETIREMENT

2 YES, RECEIVING MILITARY RETIREMENT IN LIEU OF VA COMPENSATION

3 UNKNOWN

### TABLE VA06 - ELIGIBILITY STATUS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Eligibility Status (#.3611) field of PATIENT (#2) file.

VALUE DESCRIPTION

P PENDING VERIFICATION

R PENDING RE-VERIFICATION

V VERIFIED

### TABLE VA07 - RACE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Abbreviation (#2) field of RACE (#10) file.

VALUE DESCRIPTION

1 HISPANIC, WHITE

2 HISPANIC, BLACK

3 AMERICAN INDIAN OR ALASKA NATIVE

4 BLACK, NOT OF HISPANIC ORIGIN

5 ASIAN OR PACIFIC ISLANDER

6 WHITE, NOT OF HISPANIC ORIGIN

7 UNKNOWN

### TABLE VA08 - RELIGION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Code (#3) field of RELIGION (#13) file.

VALUE DESCRIPTION

0 ROMAN CATHOLIC CHURCH

1 JUDAISM

2 EASTERN ORTHODOX

3 BAPTIST

4 METHODIST

5 LUTHERAN

6 PRESBYTERIAN

7 UNITED CHURCH OF CHRIST

8 EPISCOPALIAN

9 ADVENTIST

10 ASSEMBLY OF GOD

11 BRETHREN

12 CHRISTIAN SCIENTIST

13 CHURCH OF CHRIST

14 CHURCH OF GOD

15 DISCIPLES OF CHRIST

16 EVANGELICAL COVENANT

17 FRIENDS

18 JEHOVAH'S WITNESSES

19 LATTER DAY SAINTS

20 ISLAM

21 NAZARENE

22 OTHER

23 PENTECOSTAL

24 PROTESTANT

25 PROTESTANT, NO DENOMINATION

26 REFORMED

27 SALVATION ARMY

28 UNITARIAN-UNIVERSALISM

29 UNKNOWN/NO PREFERENCE

30 NATIVE AMERICAN

31 ZEN BUDDHISM

### TABLE VA08 – RELIGION (CONT.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Code (#3) field of RELIGION (#13) file.

VALUE DESCRIPTION

32 AFRICAN RELIGIONS

33 AFRO-CARIBBEAN RELIGIONS

34 AGNOSTICISM

35 ANGLICAN

36 ANIMISM

37 ATHEISM

38 BABI & BAHA’I FAITHS

39 BON

40 CAO DAI

41 CELTICISM

42 CHRISTIAN (NON-SPECIFIC)

43 CONFUCIANISM

44 CONGREGATIONAL

45 CYBERCULTURE RELIGIONS

46 DIVINATION

47 FOURTH WAY

48 FREE DAISM

49 FULL GOSPEL

50 GNOSIS

51 HINDUISM

52 HUMANISM

53 INDEPENDENT

54 JAINISM

55 MAHAYANA

56 MEDITATION

57 MESSIANIC JUDAISM

58 MITRAISM

59 NEW AGE

60 NON-ROMAN CATHOLIC

61 OCCULT

62 ORTHODOX

63 PAGANISM

64 PROCESS, THE

65 REFORMED/PRESBYTERIAN

66 SATANISM

67 SCIENTOLOGY

68 SHAMANISM

69 SHIITE (ISLAM)

70 SHINTO

71 SIKISM

72 SPIRITUALISM

73 SUNNI (ISLAM)

74 TAOISM

75 THERAVADA

76 UNIVERSAL LIFE CHURCH

77 VAJRAYANA (TIBETAN)

78 VEDA

79 VOODOO

80 WICCA

81 YAOHUSHUA

82 ZOROASTRIANISM

83 ASKED BUT DECLINED TO ANSWER

### TABLE VA10 - MEANS TEST INDICATOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| VALUE | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AS    | This Means Test category includes all compensable service-connected (0-100%) veterans and special category veterans. Special category veterans include: Mexican Border War and World War I veterans; former Prisoners of War; and patients receiving care for conditions potentially related to exposure to either Agent Orange (Herbicides), Ionizing Radiation or SW Asia Conditions. This category also includes 0% non-compensable service-connected veterans when they are treated for a service-connected condition.                                                                                                                       |
| AN    | This Means Test category includes NSC veterans who are required to complete VA Form 10-10F (Financial Worksheet) and those NSC veterans in receipt of VA pension, aid and attendance, housebound allowance, or entitled to State Medicaid. This category may also include 0% non-compensable service-connected veterans when they are not treated for a service-connected condition and are placed in this category based on completion of a Means Test.                                                                                                                                                                                         |
| C     | This Means Test category includes those veterans who, based on income and/or net worth, are required to reimburse VA for care rendered. This category also includes those pending adjudication. This category may also include 0% non-compensable service-connected veterans when they are not treated for a service-connected condition and are placed in this category based on completion of a Means Test.                                                                                                                                                                                                                                    |
| G     | This Means Test category includes veterans whose income is less than or equal to the MT threshold and whose estate value is greater than or equal to the net worth threshold, or such veterans whose income is greater than the MT threshold, but less than or equal to the GMT threshold, and whose estate value is less than the net worth threshold.                                                                                                                                                                                                                                                                                          |
| N     | This Means Test category includes only non-veterans receiving treatment at VA facilities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| X     | This Means Test category includes treatment of patients who are not required to complete the Means Test for the care being provided. If the veteran was admitted prior to July 1, 1986 with no change in the level of care being received, (i.e., if the patient was in the Nursing Home Care Unit (NHCU) on June 30, 1986 and has remained in the NHCU since that date with no transfer to the hospital for treatment), the "X" Means Test indicator will be accepted. This category also includes patients admitted to the domiciliary, patients seen for completion of a compensation and pension examination, and Class II dental treatment. |
| U     | This Means Test category includes only those patients who require a Means Test, and the Means Test has not been done/completed. The National Patient Care Database will not accept the transaction unless the Means Test has been completed.                                                                                                                                                                                                                                                                                                                                                                                                     |

### TABLE VA11 - PERIOD OF SERVICE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

0 KOREAN

1 WORLD WAR I

2 WORLD WAR II

3 SPANISH AMERICAN

4 PRE-KOREAN

5 POST-KOREAN

6 OPERATION DESERT SHIELD

7 VIETNAM ERA

8 POST-VIETNAM

9 OTHER OR NONE

A ARMY - ACTIVE DUTY

B NAVY, MARINE - ACTIVE DUTY

C AIR FORCE - ACTIVE DUTY

D COAST GUARD - ACTIVE DUTY

E RETIRED, UNIFORMED FORCES

F MEDICAL REMEDIAL ENLIST

G MERCHANT SEAMEN - USPHS

H OTHER USPHS BENEFICIARIES

I OBSERVATION/EXAMINATION

J OFFICE OF WORKERS COMP

K JOB CORPS/PEACE CORPS

L RAILROAD RETIREMENT

M BENEFICIARIES-FOREIGN GOV

N HUMANITARIAN (NON-VET)

O CHAMPUS RESTORE

P OTHER REIMBURS. (NON-VET)

Q OTHER FEDERAL - DEPENDENT

R DONORS (NON-VET)

S SPECIAL STUDIES (NON-VET)

T OTHER NON-VETERANS

U CHAMPVA - SPOUSE, CHILD

V CHAMPUS

W CZECHOSLOVAKIA/POLAND SVC

X PERSIAN GULF WAR

Y CAV/NPS

Z MERCHANT MARINE

### TABLE VA12 - TYPE OF INSURANCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

0 NO INSURANCE

1 MAJOR MEDICAL

2 DENTAL

3 HMO

4 PPO

5 MEDICARE

6 MEDICAID

7 CHAMPUS

8 WORKMAN COMP

9 INDEMNITY

10 PRESCRIPTION

11 MEDICARE SUPPLEMENTAL

12 ALL OTHER

### TABLE VA0015 - ENROLLMENT STATUS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

1 UNVERIFIED

2 VERIFIED

3 INACTIVE

4 REJECTED

5 SUSPENDED

6 TERMINATED

7 CANCELED/DECLINED

8 EXPIRED

9 PENDING

### TABLE VA0016 - REASON CANCELED/DECLINED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

1 DISSATISFIED WITH CARE

2 GEOGRAPHIC ACCESS

3 OTHER INSURANCE

4 OTHER

### TABLE VA0021 - ENROLLMENT PRIORITY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

1 PRIORITY 1

2 PRIORITY 2

3 PRIORITY 3

4 PRIORITY 4

5 PRIORITY 5

6 PRIORITY 6

7 PRIORITY 7

8 PRIORITY 8

### TABLE VA0022 - RADIATION EXPOSURE METHOD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

2 NAGASAKI - HIROSHIMA

3 NUCLEAR TESTING

4 BOTH

### TABLE VA0023 - PRISONER OF WAR LOCATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

4 WORLD WAR I

5 WORLD WAR II - EUROPE

6 WORLD WAR II - PACIFIC

7 KOREAN

8 VIETNAM

9 OTHER

A PERSIAN GULF WAR

B YUGOSLAVIA AS A COMBAT ZONE

### TABLE VA0024 - SOURCE OF ENROLLMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

1 VAMC

2 HEC

3 OTHER VAMC

### TABLE VA0046 - AGENT ORANGE EXPOSURE LOCATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

K KOREAN DMZ

V VIETNAM

O OTHER

### TABLE NPCD 001 - NATIONAL PATIENT CARE DATABASE ERROR CODES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample listing of possible values.

VALUE DESCRIPTION

100 EVENT TYPE SEGMENT

200 PATIENT NAME

205 DATE OF BIRTH

210 SEX

215 RACE

## HL7 Interface Specification for the Transmission of PCMM Primary Care Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This interface specification specifies the information needed for PCMM Primary Care data reporting. This data exchange will be triggered by specific events in the PCMM package. The basic communication protocol will be addressed, as well as the information that will be made available and how it will be obtained.

This application will use the abstract message approach and encoding rules specified by HL7. HL7 is used for communicating data associated with various events that occur in health care environments.

For example, when a patient is assigned to a primary care team in PCMM, the event will trigger a PCMM primary care update message. This message is an unsolicited transaction to all external systems interfacing with VISTA.

The formats of these messages conform to the Version 2.3 HL7 Interface Standards where applicable. HL7 custom message formats ("Z" segments) are used only when necessary.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assumptions have been made at the beginning of this project in order to help define the scope and meet the initial needs in interfacing with the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)).

### Message Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data sent in the HL7 messages will be limited to the information that can be processed by the AITC, with the exception of the PID segment, which will be populated using the nationally supported VISTA call. The data being sent will also be limited to what is available in VISTA.

In order to capture the most information, specific PCMM events will generate messages to the AITC systems. This is not intended to cover all possible PCMM events; only those which may result in the capture of primary care data needed to update the National Patient Care Database (NPCD). The mode for capturing data for PCMM events was chosen to capture as much of the data as possible. (See Data Capture and Transmission (1.2.2) for further information on the mode for capturing the PCMM events.)

Per the HL7 standards, Primary Care data fields that are transmitted as null (“”) will delete data from the NPCD. A field that is transmitted as blank does not delete data; it simply means take no action on the field. In the ZPC segment, if field Provider Assignment ID has a value and all remaining fields are nulls, Austin should do the following.

If this record exists, delete it from the database.

If this record does not exist, ignore this segment.

### Data Capture and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When PCMM options or calls are used to update specific primary care data in VISTA, these events and changes will be captured. Any changes made to the VISTA database in non-standard ways, such as a direct global set by an application or by MUMPS code, will not be captured.

### Background Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A nightly background job will be sending HL7 messages for the appropriate PCMM primary care event for the day.

### VA MailMan Lower Level Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 V. 1.6 of the VA MailMan lower level protocol (LLP) will be used. This version of the VA MailMan LLP differs from HL7 V. 1.5 in that a blank line is placed between each segment in the message \[denoting a carriage return\].

## Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the VISTA perspective, all incoming or outgoing messages are handled or generated based on an event.

In this section, and the following sections, these elements will be defined for each message:

- The trigger events
- The message event code
- A list of segments used in the message
- A list of fields for each segment in the message

Each message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. A \[ \] indicates the segment is optional, the { } indicates the segment is repeatable. For each message category there will be a list of HL7 standard segments or "Z" segments used for the message.

## Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each segment, the data elements are described in table format. The table includes the sequence number (SEQ), maximum length (LEN), data type (DT), required or optional (R/O), repeatable (RP/#), the table number (TBL \#), the element name, and the VISTA description. Each segment is described in the following sections.

## Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments that are contained in message types described in this document. These are generic descriptions. Any time any of the segments described in this section are included in a message in this document, the VISTA descriptions and mappings will be as specified here, unless otherwise specified in that section.

### MSH - Message Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th><em>VISTA</em> DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td>Recommended value is ^ (caret)</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<p>Component = ~ (tilde)</p>
<p>Repeat = | (bar)</p>
<p>Escape = \ (back slash)</p>
<p>Sub-component = &amp; (ampersand)</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td>PCMM-212</td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td>Station's facility number</td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>NPCD-PCMM</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Facility=200</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Date and time message was created</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p><u>2 Components</u></p>
<p><em>Refer to Table 0076</em></p>
<p><em>Refer to Table 0003</em></p></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by VistA HL7 Package</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td>P (production)</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>2.3 (Version 2.3)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td>NE (never acknowledge)</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td>AL (always acknowledge)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td>Not used</td>
</tr>
</tbody>
</table>

### EVN - Event Type Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME            | V*IST*A DESCRIPTION      |
|-----|-----|-----|-----|------|------|-------------------------|--------------------------|
| 1   | 3   | ID  | R   |      | 0003 | Event Type Code         | *Refer to Table 0003*    |
| 2   | 26  | TS  | R   |      |      | Date/Time of Event      | Date/Time Event Occurred |
| 3   | 26  | TS  |     |      |      | Date/Time Planned Event | Not used                 |
| 4   | 3   | ID  |     |      | 0062 | Event Reason Code       | Not used                 |
| 5   | 60  | CN  |     |      | 0188 | Operator ID             | Not used                 |

### PID - Patient Identification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME               | V*IST*A DESCRIPTION                         |
|-----|-----|-----|-----|------|------|----------------------------|---------------------------------------------|
| 1   | 4   | SI  |     |      |      | Set ID - Patient ID        | Always 1                                    |
| 2   | 20  | CK  |     |      |      | Patient ID (External ID)   | Integration Control Number (ICN)            |
| 3   | 20  | CM  | R   | Y    |      | Patient ID (Internal ID)   | Pointer to entry in PATIENT file            |
| 4   | 12  | ST  |     |      |      | Alternate Patient ID       | Primary Short ID                            |
| 5   | 48  | PN  | R   |      |      | Patient Name               | Name                                        |
| 6   | 30  | ST  |     |      |      | Mother's Maiden Name       | Mother’s maiden name                        |
| 7   | 26  | TS  |     |      |      | Date of Birth              | Date of birth                               |
| 8   | 1   | ID  |     |      | 0001 | Sex                        | *Refer to Table 0001*                       |
| 9   | 48  | PN  |     | Y    |      | Patient Alias              | Alias                                       |
| 10  | 1   | ID  |     |      | 0005 | Race                       | Race                                        |
| 11  | 106 | AD  |     | Y    |      | Patient Address            | Address                                     |
| 12  | 4   | ID  |     |      |      | County Code                | VA County Code                              |
| 13  | 40  | TN  |     | Y    |      | Phone Number – Home        | Phone number (residence)                    |
| 14  | 40  | TN  |     | Y    |      | Phone Number - Business    | Phone number (work)                         |
| 15  | 25  | ST  |     |      |      | Language - Patient         | Not used                                    |
| 16  | 1   | ID  |     |      | 0002 | Marital Status             | *Refer to Table 0002*                       |
| 17  | 3   | ID  |     |      | 0006 | Religion                   | Religion                                    |
| 18  | 20  | CK  |     |      |      | Patient Account Number     | Not used                                    |
| 19  | 16  | ST  |     |      |      | SSN Number - Patient       | Social security number and pseudo indicator |
| 20  | 25  | CM  |     |      |      | Driver's Lic Num - Patient | Not used                                    |
| 21  | 20  | CK  |     |      |      | Mother's Identifier        | Not used                                    |
| 22  | 1   | ID  |     |      | 0189 | Ethnic Group               | Not used                                    |
| 23  | 25  | ST  |     |      |      | Birth Place                | Not used                                    |
| 24  | 2   | ID  |     |      |      | Multiple Birth Indicator   | Not used                                    |
| 25  | 2   | NM  |     |      |      | Birth Order                | Not used                                    |
| 26  | 3   | ID  |     | Y    | 0171 | Citizenship                | Not used                                    |
| 27  | 60  | CE  |     |      | 0172 | Veterans Military Status   | Not used                                    |

### ZPC – VA Specific Primary Care Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>V<em>IST</em>A DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Provider Assignment ID</td>
<td><p>Facility – number</p>
<p>Example: 500-234 Where: 500 = Facility number 234 = Pointer to full ID in PCMM HL7 IDfile (404.49).</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>90</td>
<td>XCN</td>
<td>R</td>
<td></td>
<td></td>
<td>Provider ID</td>
<td><p><u>14 Components</u></p>
<p><u>2 Sub-Components</u></p>
<p>Pointer to entry in NEW PERSON file (#200)</p>
<p>Facility Number</p>
<p>&lt;family name (ST) &gt; &amp; &lt; last_name_prefix (ST)&gt;</p>
<p>&lt;given name (ST)&gt;</p>
<p>&lt;middle initial or name (ST)&gt;</p>
<p>&lt;suffix (e.g., JR or III) (ST)&gt;</p>
<p>&lt;prefix (e.g., DR) (ST)&gt;</p>
<p>&lt;degree (e.g., MD) (IS)&gt;</p>
<p>This will always be VA200 (NEW PERSON file)</p>
<p>Not used</p>
<p>Assigning Facility (HD) - This will be the facility number</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>Date Provider Assigned</td>
<td>File POSITION ASSIGNMENT HISTORY (404.52), field .02 –or-PRECEPTOR ASSIGNMENT HISTORY (404.53), field .02.</td>
</tr>
<tr class="even">
<td>4</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Date Provider Unassigned</td>
<td>Date is derived from STATUS field (.04) in both POSITION ASSIGNMENT HISTORY (404.52), and PRECEPTOR ASSIGNMENT HISTORY (404.53).</td>
</tr>
<tr class="odd">
<td>5</td>
<td>3</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>Provider Type Code</td>
<td><p>PCP = Primary Care Provider</p>
<p>AP = Associate Provider</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>20</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Provider Person Class</td>
<td><p><u>3 Components</u></p>
<p>Provider Type Code</p>
<p>Not used</p>
<p>This will always be VA8932.1 (PERSON CLASS file)</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>Set ID</td>
<td>This field is used to sequentially number multiple Primary Care (ZPC) segments.</td>
</tr>
<tr class="even">
<td>8</td>
<td>9</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Provide Social Security Number</td>
<td>SSN (#9) field of the NEW PERSON (#200) file.</td>
</tr>
</tbody>
</table>

# HL7 message transactions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the HL7 message transactions that are necessary to support the primary care data in the NPCD for the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC). These messages will use the generic HL7 format, so that they can be expanded later to support new interfaces at other facilities.

## Trigger Events and Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each triggering event is listed below, along with the applicable form of the message to be exchanged. The notation used to describe the sequence, option, and repetition of segments is described in the HL7 Final Standard Manual, Chapter 2, Section 2.4.8, Chapter Formats for Defining Abstract Messages, and in summary form, in Section 2.1 of this document.

### Update Patient Information (A08)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCMM Primary Care trigger events will create an entry into the PCMM HL7 EVENT file (#404.48) under the following circumstances.

- When a patient is assigned/unassigned to a position
- When an existing patient assignment is edited
- When an existing patient assignment is deleted
- When a provider is assigned/unassigned to a position
- When an existing provider assignment is edited
- When an existing provider assignment is deleted

A recurring job will process the PCMM HL7 EVENT file and trigger an A08 message to be sent for each patient marked for transmission. The receiving system will replace any data that exists with the “new” data that is transmitted with this message based on the Provider Assignment ID field.

### Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an entry is deleted, a ZPC segment will be sent showing the Provider Assignment ID and the remaining fields as null (“”). This will delete the current record.

ADT ADT Message

MSH Message HeaderEVN Event TypePID Patient Identification

{ZPC} PCMM Primary Care Data

# SUPPORTED AND USER-DEFINED HL7 TABLES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table 0001 - Sex

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

F FEMALE

M MALE

O OTHER

U UNKNOWN

## Table 0002 - Marital Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

A SEPARATED

D DIVORCED

M MARRIED

S SINGLE

W WIDOWED

## Table 0003 - Event Type Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

A08 UPDATE PATIENT INFORMATION

## Table 0005 - Race

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

1 HISPANIC, WHITE

2 HISPANIC, BLACK

3 AMERICAN INDIAN OR ALASKA NATIVE

4 BLACK, NOT OF HISPANIC ORIGIN

5 ASIAN OR PACIFIC ISLANDER

6 WHITE, NOT OF HISPANIC ORIGIN

7 UNKNOWN

## Table 0006 - Religion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

0 ROMAN CATHOLIC CHURCH

1 JUDAISM

2 EASTERN ORTHODOX

3 BAPTIST

4 METHODIST

5 LUTHERAN

6 PRESBYTERIAN

7 UNITED CHURCH OF CHRIST

8 EPISCOPALIAN

9 ADVENTIST

10 ASSEMBLY OF GOD

11 BRETHREN

12 CHRISTIAN SCIENTIST

13 CHURCH OF CHRIST

14 CHURCH OF GOD

15 DISCIPLES OF CHRIST

16 EVANGELICAL COVENANT

17 FRIENDS

18 JEHOVAH'S WITNESSES

19 LATTER DAY SAINTS

20 ISLAM

21 NAZARENE

22 OTHER

23 PENTECOSTAL

24 PROTESTANT

25 PROTESTANT, NO DENOMINATION

26 REFORMED

27 SALVATION ARMY

28 UNITARIAN-UNIVERSALISM

29 UNKNOWN/NO PREFERENCE

30 NATIVE AMERICAN

31 ZEN BUDDHISM

32 AFRICAN RELIGIONS

33 AFRO-CARIBBEAN RELIGIONS

34 AGNOSTICISM

35 ANGLICAN

36 ANIMISM

37 ATHEISM

38 BABI & BAHA’I FAITHS

39 BON

40 CAO DAI

41 CELTICISM

42 CHRISTIAN (NON-SPECIFIC)

43 CONFUCIANISM

44 CONGREGATIONAL

45 CYBERCULTURE RELIGIONS

46 DIVINATION

47 FOURTH WAY

48 FREE DAISM

49 FULL GOSPEL

## Table 0006 – Religion (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

50 GNOSIS

51 HINDUISM

52 HUMANISM

53 INDEPENDENT

54 JAINISM

55 MAHAYANA

56 MEDITATION

57 MESSIANIC JUDAISM

58 MITRAISM

59 NEW AGE

60 NON-ROMAN CATHOLIC

61 OCCULT

62 ORTHODOX

63 PAGANISM

64 PROCESS, THE

65 REFORMED/PRESBYTERIAN

66 SATANISM

67 SCIENTOLOGY

68 SHAMANISM

69 SHIITE (ISLAM)

70 SHINTO

71 SIKISM

72 SPIRITUALISM

73 SUNNI (ISLAM)

74 TAOISM

75 THERAVADA

76 UNIVERSAL LIFE CHURCH

77 VAJRAYANA (TIBETAN)

78 VEDA

79 VOODOO

80 WICCA

81 YAOHUSHUA

82 ZOROASTRIANISM

83 ASKED BUT DECLINED TO ANSWER

## Table 0076 - Message Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

ADT ADT MESSAGE

This Page Is Intentionally left blank for pagination conventions

# HL7 Interface Specification for PCMM Primary Care Acknowledgement Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AUSTIN INFORMATION TECHNOLOGY CENTER (AITC) (formerly Austin Automation Center (AAC)) ERROR PROCESSING

This section describes the process by which acknowledgment (ACK) messages are generated by the AITC back to the VISTA originating site, advising them of a successful or failed (error) HL7 message transmission.

Section 1.1 provides a general description of the validation process that occurs at the AITC. Section 1.2 describes the message control segments contained in the acknowledgment message. Section 1.3 provides examples of specific transactions that will occur between VISTA and the AITC.

The sections below describe the HL7 supported and user defined tables.

Austin Information Technology Center (AITC) (formerly Austin Automation Center (AAC)) Validation Process

After PCMM HL7 (ADT~A08) messages are sent from VISTA, the AITC will do the following.

- Accept the message - At this stage the message may reject for reasons unrelated to its content or format (system down, missing MSH segment, etc.). Austin will not generate an ACK message. The sending application will be responsible for retransmitting messages that are not acknowledged.
- Pass it on to the receiving application, which performs one of the following functions.
- Processes the message successfully, generating a response message with a value of AA in MSA-1-acknowledgment code.
- OR– sends an error response, providing error information in segments in the response message (see 1.2) with a value of AE in MSA-1-acknowledgment code.
- Pass the response message back to the VISTA originating site.

## Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments that are contained in the general acknowledgement response message.

> ACK General Acknowledgment

> MSH Message Header

> MSA Message Acknowledgment

> \[ERR\] Error 1.2.3

When a PCMM HL7 (ADT~A08) message is successfully accepted by the receiving system, the optional Error (ERR) segment will not be returned to the sending system in the general acknowledgement message.

When a PCMM HL7 (ADT~A08) message is rejected by the receiving system, the Error (ERR) segment is a repeating field and will contain the error and location of each error identified. Each repeating field will be in the following format.

Components: \<segment ID (ST)\>^\<sequence (NM)\>^\<field position (NM)\>^\<code identifying error (CE)\>

The 1st component identifies the segment ID.

The 2nd component is an index if there is more than one segment of type \<segment ID\>.

The 3rd component is the error’s field position within the segment.

The 4th component is the error code from the user-defined PCMM Error Code table.

### MSH - Message Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th><em>VISTA</em> DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td>Recommended value is ^ (caret)</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<p>Component = ~ (tilde)</p>
<p>Repeat = | (bar)</p>
<p>Escape = \ (back slash)</p>
<p>Sub-component = &amp; (ampersand)</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td>NPCD-AAC*</td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td>Facility=200</td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>PCMM-212</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Station’s facility number</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Date and time message was created</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p><u>2 Components</u></p>
<p><em>Refer to Table 0076</em></p>
<p><em>Refer to Table 0003</em></p></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by V<em>IST</em>A HL7 Package</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td>P (production)</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>2.2 (Version 2.2)</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td>NE (never acknowledge)</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td>AL (always acknowledge)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td>Not used</td>
</tr>
</tbody>
</table>

\*AAC stands for Austin Automation Center. The name of that facility has been changed to Austin Information Technology Center.

### MSA Message Acknowledgment Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|     |     |     |     |      |      |                             |                                                       |
|-----|-----|-----|-----|------|------|-----------------------------|-------------------------------------------------------|
| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME                | VISTA DESCRIPTION                                     |
| 1   | 2   | ID  | R   |      | 0008 | Acknowledgment Code         | Refer to Table 008                                    |
| 2   | 20  | ST  | R   |      |      | Message Control ID          | Message Control ID of the message being acknowledged. |
| 3   | 80  | ST  | R   |      |      | Text Message                | Not used                                              |
| 4   | 15  | NM  |     |      |      | Expected Sequence Number    | Not used                                              |
| 5   | 1   | ID  |     |      | 0102 | Delayed Acknowledgment Type | Not used                                              |
| 6   | 100 | CE  |     |      |      | Error Condition             | Not used                                              |

### ERR Error Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 24%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SEQ</td>
<td>LEN</td>
<td>DT</td>
<td>R/O</td>
<td>RP/#</td>
<td>TBL#</td>
<td>ELEMENT NAME</td>
<td>VISTA DESCRIPTION</td>
</tr>
<tr class="even">
<td>1</td>
<td>80</td>
<td>CM</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Error Code and Location</td>
<td><p>Segment ID (ST)</p>
<p>Sequence (NM)</p>
<p>4 numbers long. Strip off leading zeros on V<em>IST</em>A side.</p>
<p>Field position (NM)</p>
<p>Code identifying error (CE)</p>
<p>(See PCMM Error Code Table (section 1.4.2))</p></td>
</tr>
</tbody>
</table>

### ZPC VA Specific - Primary Care Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>V<em>IST</em>A DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Provider Assignment ID</td>
<td><p>Facility – number</p>
<p>Example:500-234 Where:500 = Facility number 234 = Pointer to full IDin PCMM HL7 IDfile (404.49).</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>90</td>
<td>XCN</td>
<td>R</td>
<td></td>
<td></td>
<td>Provider ID</td>
<td><p><u>14 Components</u></p>
<p><u>2 Sub-Components</u></p>
<p>Pointer to entry in NEW PERSON file (#200)</p>
<p>Facility Number</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>This will always be VA200 (NEW PERSON file)</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p>
<p>Not used</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>Date Provider Assigned</td>
<td>File POSITION ASSIGNMENT HISTORY (404.52), field .02 –or-PRECEPTOR ASSIGNMENT HISTORY (404.53), field .02.</td>
</tr>
<tr class="even">
<td>4</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Date Provider Unassigned</td>
<td>Date is derived from STATUS field (.04) in both POSITION ASSIGNMENT HISTORY (404.52), and PRECEPTOR ASSIGNMENT HISTORY (404.53).</td>
</tr>
<tr class="odd">
<td>5</td>
<td>3</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>Provider Type Code</td>
<td><p>PCP = Primary Care Provider</p>
<p>AP = Associate Provider</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>20</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Provider Person Class</td>
<td><p><u>3 Components</u></p>
<p>Provider Type Code</p>
<p>Not used</p>
<p>This will always be VA8932.1 (PERSON CLASS file)</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>Set ID*</td>
<td>This field is used to sequentially number multiple Primary Care (ZPC) segments.</td>
</tr>
</tbody>
</table>

\* = New field added

Information Technology Center.

## Specific Transaction Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section describes specific HL7 transactions that will occur between PCMM (VISTA) and the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)).

General Acknowledgment (ACK) message advising of a successful PCMM HL7 (ADT~A08) transmission at the Application Level.

PCMM HL7 (ADT~A08) message is sent from VISTA to the AITC.

MSH^~\|\\^PCMM-210^500^NPCD-AAC^200^20000307150556^^ADT~A08^02651^P^2.2^^^NE^AL^USA

EVN^A08^20000307

PID^1^""^7168987~1~M10^6221^TEST~PATIENT^""^19330303^U^^7^""~""~""~""~""\~\~~""~""^^""^""^^U^29^^443366221^^^^^^^^^^

ZPC^500-509^70&500\~\~\~\~\~\~~VA200\~\~\~\~\~~^19961203^19961203^PCP^""^1

ZPC^500-510^123456852&500\~\~\~\~\~\~~VA200\~\~\~\~\~~^19961204^19961211^PCP^""^2

ZPC^500-511^170&500\~\~\~\~\~\~~VA200\~\~\~\~\~~^19970317^19970318^PCP^""^3

AITC then sends a General Acknowledgment (ACK) message back to VISTA advising of a successful PCMM HL7 (ADT~A08) transmission.

MSH^~\|\\^NPCD-AAC^200^PCMM-210^500^20000229^^ACK~A08^50002175^P^2.2^^^NE^AL

MSA^AA^02651

General Acknowledgment (ACK) message advising of a failed PCMM HL7 (ADT~A08) transmission at the Application Level.

PCMM HL7 (ADT~A08) message is sent from VISTA to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)), with ZPC~3~date provider assigned invalid in both the 2nd and 3rd ZPC segments.

MSH^~\|\\^PCMM-210^500^NPCD-AAC^200^20000307150556^^ADT~A08^02651^P^2.2^^^NE^AL^USA

EVN^A08^20000307

PID^1^""^7168987~1~M10^6221^TEST~PATIENT^""^19330303^U^^7^""~""~""~""~""\~\~~""~""^^""^""^^U^29^^443366221^^^^^^^^^^

ZPC^500-509^70&500\~\~\~\~\~\~~VA200\~\~\~\~\~~^19961203^19961203^PCP^""^1

ZPC^500-510^123456852&500\~\~\~\~\~\~~VA200\~\~\~\~\~~^##19961204^19961211^PCP^""^2

ZPC^500-511^170&500\~\~\~\~\~\~~VA200\~\~\~\~\~~^9970317^19970318^PCP^""^3

AITC then sends a General Acknowledgment (ACK) message back to VISTA advising of a failed PCMM HL7 (ADT~A08) transmission.

MSH^~\|\\^NPCD-AAC^200^PCMM-210^500^20000229^^ACK~A08^50002175^P^2.2^^^NE^AL

MSA^AE^02651

ERR^ZPC~0002~3~320M\|ZPC~0003~3~320M

## Supported and User Defined Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Table 008 Acknowledgement Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Value Description

AA Original mode: Application Accept

Enhanced mode: Application Acknowledgment: Accept

AE Original mode: Application Error

Enhanced mode: Application Acknowledgment: Error

AR Original mode: Application Reject

Enhanced mode: Application Acknowledgment: Reject

CA Enhanced mode: Accept Acknowledgment: Commit Accept

CE Enhanced mode: Accept Acknowledgment: Commit Error

CR Enhanced mode: Accept Acknowledgment: Commit Reject

### PCMM Error Code Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                  |                        |                                                                                                      |
|------------------|------------------------|------------------------------------------------------------------------------------------------------|
| Error Number     | Field Number           | Edit Description                                                                                     |
| *000 Series* |                        |                                                                                                      |
| *Miscellaneous*  |                        |                                                                                                      |
|                  |                        |                                                                                                      |
| 0000             |                        |                                                                                                      |
| 001M             | Segment Name           | EVN Segment missing                                                                                  |
| 002M             | Segment Name           | PID Segment missing                                                                                  |
| 003M             | Segment Name           | ZPC Segment missing                                                                                  |
| 005M             | Segment Name           | Invalid Segment name                                                                                 |
|                  |                        |                                                                                                      |
| *100 Series* |                        |                                                                                                      |
| EVN Segment      |                        |                                                                                                      |
| 104M             | Event Date             | Required. Must be a valid date. Must be less than or equal to processing date.                       |
| 106M             | Event Time             | If present time must be numeric. Must be a valid time.                                               |
| 110M             | MSH Message Control ID | Required                                                                                             |
| 113M             | Event Type Segment     | Required. Must be 'A08'.                                                                             |
| 200 Series   |                        |                                                                                                      |
| PID Segment      |                        |                                                                                                      |
| 200M             | Patient Name           | Required. Must be alphanumeric. Must not be all numeric. Must not be all blanks.                     |
| 210M             | Patient ID (Internal)  | Required. Must be numeric.                                                                           |
| 220M             | Date of Birth          | Required                                                                                             |
| 221M             | Date of Birth          | Required. Century/Year must be numeric and less than the processing Century/Year.                    |
| 223M             | Date of Birth          | Required. Must be a valid date.                                                                      |
| 224M             | Date of Birth          | Required. Must be less than the processing date.                                                     |
| 230M             | Sex                    | Must be blank or match table. (Refer to table T0001).                                                |
| 240M             | Race                   | Must be a valid code. (Refer to table VA07) or null.                                                 |
| 250M             | Marital Status         | Must be a valid code. (Refer to table T0002).                                                        |
| 260M             | State                  | Must be a valid state code. (Refer to table AA015).                                                  |
| 261M             | County                 | Must be blank or when combined with numeric state code must be a valid code. (Refer to table AA015). |

PCMM ERROR CODE TABLE, CONT.

|                         |                                      |                                                                                                            |
|-------------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------|
| Error Number            | Field Name                           | Edit Description                                                                                           |
| 262M                    | Address Line 1                       | Must not be all numerics                                                                                   |
| 263M                    | Address Line 2                       | Must not be all numerics                                                                                   |
| 264M                    | Address - City                       | Must be alphanumeric. Must not be all numeric.                                                             |
| 270M                    | Religion                             | Must be blank or a valid code. (Refer to table VA08).                                                      |
| 280M                    | Address - Zip Code                   | Must be numeric. First five digits must not be all zeros. If last four digits exist, them must be numeric. |
| 290M                    | Social Security Number               | Required. Must be numeric. Must be greater than zeros.                                                     |
| 291M                    | Social Security Number               | Required. Last byte must be 'P' or blank.                                                                  |
| *300 Series*        |                                      |                                                                                                            |
| *ZPC SegmentUpdates* |                                      |                                                                                                            |
| 300M                    | Provider Assignment ID               | Required. Must be a valid station number followed by a dash then all numerics.                             |
| 310M                    | Provider ID                          | Required. Must be numeric ID followed by a valid facility number.                                          |
| 320M                    | Date Provider Assigned               | Required. Must be a valid date and can be a future date.                                                   |
| 330M                    | Date Provider Unassigned             | Optional                                                                                                   |
| 340M                    | Provider Type Code                   | Required. Must be 'PCP' or 'AP'.                                                                           |
| 350M                    | Provider Person Class (seq 6 comp1)  | Optional. If present the Provider Type Code must be a valid Practitioner Type Code (table T0133).          |
| 360M                    | Provider Person Class (seq 6 comp 2) | Required. Must be VA8932.1                                                                                 |
| 370M                    | Provider SSN                         | Required. SSN not numeric or all zeros.                                                                    |

|                       |                                      |                                                                                |
|-----------------------|--------------------------------------|--------------------------------------------------------------------------------|
| Error Number          | Field Number                         | Edit Description                                                               |
| ZPC *Segment Deletes* |                                      |                                                                                |
| 300M                  | Provider Assignment ID               | Required. Must be a valid station number followed by a dash then all numerics. |
|                       | Provider ID                          | Will be null                                                                   |
| 3                     | Date Provider Assigned               | Will be null                                                                   |
| 3                     | Date Provider Unassigned             | Will be null                                                                   |
| 3                     | Provider Type Code                   | Will be null                                                                   |
| 3                     | Provider Person Class (seq 6 comp1)  | Will be null                                                                   |
| 360M                  | Provider Person Class (seq 6 comp 2) | Will be null                                                                   |

This Page Is Intentionally left blank for pagination conventions

# HL7 Interface Specification for VIC Card VistA to NCMD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a Veteran’s ID Card (VIC) Image Capture workstation retrieves demographic data from VistA, a record will be created in a VistA file to indicate that a VIC request is pending under the following exception conditions.

- The patient does not have a National Integrated Control Number (ICN).
- The eligibility/enrollment information needed to determine the patient’s eligibility for a VIC is incomplete.
- The current status of the veteran’s claim for Purple Heart eligibility is either pending or in-process.

A Health Level 7 (HL7) message will be used to notify the National Card Management Directory (NCMD) when these exceptions have been resolved.

This specifies the information needed to either release the previous hold or cancel a pending VIC order request and communicate the order action to the NCMD.

The data exchange will be triggered when the daily VistA re-evaluation of the pending VIC order request finds that a National ICN exists and the VIC eligibility can be determined.

The basic communication protocol will be addressed, as well as the information that will be made available and how it will be obtained.

This application will use the abstract message approach and encoding rules specified by HL7. HL7 is used for communicating data associated with various events which occur in health care environments.

The formats of these messages conform to the Version 2.4 HL7 Interface Standards where applicable.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The transmission of VIC requests from VistA to the NCMD assumes the following.

- All VistA sites will have installed VistA HL7 software and it is operational.
- The veteran’s demographics and digital photograph have been previously loaded into the NCMD.

## Message Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data sent in the HL7 messages will be limited to the information that is required to uniquely identify the patient and request the VIC card. The data transmitted will be limited to available VistA data.

## Data Capture and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The following event trigger will generate a General Order Message (ORM~O01).
- VistA re-evaluates a pending VIC card request and the associated patient has a nationally assigned ICN and the necessary eligibility/enrollment information needed to determine the patient’s VIC eligibility.

> **NOTE:** Any modification made to the VistA database in non-standard ways, such as a direct global set by an application or by MUMPS code, will not be captured.

## VA TCP/IP Lower Level Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 V. 1.6 TCP/IP lower level protocol (LLP) will be used which implements the HL7 Minimal Lower Layer Protocol (MLLP) referenced in section C.4 of Appendix C of the Health Level 7 Implementation Guide (v2.3).

HL7 CONTROL SEGMENTS - This section defines the HL7 control segments supported by VistA. The messages are presented separately and defined by category. Segments are also described. The messages are presented in the Message Control category.

### Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the VistA perspective, all incoming or outgoing messages are handled or generated based on an event.

In this section and the following sections, the following elements will be defined for each message.

- Trigger events
- Message event code
- List of segments used in the message
- List of fields for each segment in the message

Each message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. A \[ \] indicates the segment is optional, the { } indicates the segment is repeatable. For each message category, there will be a list of HL7 standard segments used for the message.

### Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each segment, the data elements are described in table format. The table includes the sequence number (SEQ), maximum length (LEN), data type (DT), required or optional (R/O), repeatable (RP/#), the table number (TBL#), the element name, and the VistA description. Each segment is described in the following sections.

### Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments that are contained in message types described in this document. These are generic descriptions. Any time any of the segments described in this section are included in a message in this document, the VistA descriptions and mappings will be as specified here unless otherwise specified in that section.

### MSH - Message Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td>Recommended value is ^ (caret)</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<p>Component = ~ (tilde)</p>
<p>Repeat = | (bar)</p>
<p>Escape = \ (back slash)</p>
<p>Sub-component = &amp; (ampersand)</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td>Sending station's facility number from Institution field of HL7 Communication Parameters file.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Receiving station’s facility number from Institution field of HL Logical Link file.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Date and time message was created.</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p>2 Components</p>
<p>Refer to Table 0076</p>
<p>Refer to Table 0003</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by VISTA HL7 Package.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td>P (production)</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>Version ID field of event protocol in Protocol file.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td>NE (never acknowledge)</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td>AL (always acknowledge)</td>
</tr>
<tr class="odd">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td>USA</td>
</tr>
<tr class="even">
<td>18</td>
<td>6</td>
<td>ID</td>
<td></td>
<td>Y/3</td>
<td>0211</td>
<td>Character Set</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>19</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Principal Language of Message</td>
<td>Not used</td>
</tr>
</tbody>
</table>

### MSA – Message Acknowledgment Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| 2.3.1 | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME                | VistA DESCRIPTION                                     |
|-------|-----|-----|-----|------|------|-----------------------------|-------------------------------------------------------|
| 1     | 2   | ID  | R   |      | 0008 | Acknowledgment Code         | Refer to HL7 table 0008                               |
| 2     | 20  | ST  | R   |      |      | Message Control ID          | Message Control ID of the message being acknowledged. |
| 3     | 80  | ST  | O   |      |      | Text Message                | Free text error message                               |
| 4     | 15  | NM  | O   |      |      | Expected Sequence Number    | Not used                                              |
| 5     | 1   | ID  | B   |      | 0102 | Delayed Acknowledgment Type | Not used                                              |
| 6     | 100 | CE  | O   |      |      | Error Condition             | Not used                                              |

### PID - Patient Identification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td></td>
<td></td>
<td></td>
<td>Set ID - Patient ID</td>
<td>Always set to ‘1’</td>
</tr>
<tr class="even">
<td>2</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient ID (External ID)</td>
<td>Social Security Number field of Patient file.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>20</td>
<td>CM</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Patient ID (Internal ID)</td>
<td><p>Integrated Control Number (ICN) field of Patient file.</p>
<p>Component 1: ICN w/checksum</p>
<p>Component 2: Null</p>
<p>Component 3: Null</p>
<p>Component 4: Assigning authority (subcomponent 1: ‘USVHA’, subcomponent 3: ‘L’</p>
<p>Component 5: Type ‘NI’</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>12</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Alternate Patient ID</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>5</td>
<td>48</td>
<td>PN</td>
<td>R</td>
<td></td>
<td></td>
<td>Patient Name</td>
<td>Name</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Maiden Name</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date of Birth</td>
<td>Date of birth</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0001</td>
<td>Sex</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>48</td>
<td>PN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Patient Alias</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0005</td>
<td>Race</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>106</td>
<td>AD</td>
<td></td>
<td>Y</td>
<td></td>
<td>Patient Address</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>12</td>
<td>4</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>County Code</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>13</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Phone Number – Home</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Phone Number – Business</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>15</td>
<td>25</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Language – Patient</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0002</td>
<td>Marital Status</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>17</td>
<td>3</td>
<td>ID</td>
<td></td>
<td></td>
<td>0006</td>
<td>Religion</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>18</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient Account Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>19</td>
<td>16</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>SSN Number – Patient</td>
<td>Social security number and pseudo indicator.</td>
</tr>
<tr class="even">
<td>20</td>
<td>25</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
<td>Driver's Lic Num – Patient</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>21</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Identifier</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0189</td>
<td>Ethnic Group</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>23</td>
<td>25</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Birth Place</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>24</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Multiple Birth Indicator</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>25</td>
<td>2</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Birth Order</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>26</td>
<td>3</td>
<td>ID</td>
<td></td>
<td>Y</td>
<td>0171</td>
<td>Citizenship</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>27</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td>0172</td>
<td>Veterans Military Status</td>
<td>Not used</td>
</tr>
</tbody>
</table>

### ORC-Common Order Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME              | VistA DESCRIPTION   |
|-----|-----|-----|-----|------|------|---------------------------|---------------------|
| 1   | 2   | ID  | R   |      | 0119 | Order Control             | Refer to Table 0119 |
| 2   | 22  | EI  | C   |      |      | Placer Order Number       | Not used            |
| 3   | 22  | EI  | C   |      |      | Filler Order Number       | Not used            |
| 4   | 22  | EI  |     |      |      | Placer Group Number       | Not used            |
| 5   | 2   | ID  |     |      | 0038 | Order Status              | Not used            |
| 6   | 1   | ID  |     |      | 0121 | Response Flag             | Not used            |
| 7   | 200 | TQ  |     |      |      | Quantity/timing           | Not used            |
| 8   | 200 | CM  |     |      |      | Parent                    | Not used            |
| 9   | 26  | TS  |     |      |      | Date/Time of Transaction  | Not used            |
| 10  | 120 | XCN |     |      |      | Entered By                | Not used            |
| 11  | 120 | XCN |     |      |      | Verified By               | Not used            |
| 12  | 120 | XCN |     |      |      | Ordering Provider         | Not used            |
| 13  | 80  | PL  |     |      |      | Enterer’s Location        | Not used            |
| 14  | 40  | XTN |     | Y/2  |      | Call Back Phone Number    | Not used            |
| 15  | 26  | TS  |     |      |      | Order Effective Date/Time | Not used            |
| 16  | 200 | CE  |     |      |      | Order Control Code Reason | Not used            |
| 17  | 60  | CE  |     |      |      | Entering Organization     | Not used            |
| 18  | 60  | CE  |     |      |      | Entering Device           | Not used            |
| 19  | 120 | XCN |     |      |      | Action By                 | Not used            |

### RQD-Requisition Detail Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME                | VistA DESCRIPTION                                       |
|-----|-----|-----|-----|------|------|-----------------------------|---------------------------------------------------------|
| 1   | 4   | SI  |     |      |      | Requisition Line Number     | Always set to “1”                                       |
| 2   | 60  | CE  | C   |      |      | Item Code – Internal        | Not used                                                |
| 3   | 60  | CE  | C   |      |      | Item Code – External        | NCMD Card ID (.01) field from VIC REQUEST (#39.6) file. |
| 4   | 60  | CE  | C   |      |      | Hospital Item Code          | Not used                                                |
| 5   | 6   | NM  |     |      |      | Requisition Quantity        | Not used                                                |
| 6   | 60  | CE  |     |      |      | Requisition Unit of Measure | Not used                                                |
| 7   | 30  | IS  |     |      | 0319 | Dept. Cost Center           | Not used                                                |
| 8   | 30  | IS  |     |      | 0320 | Item Natural Account Code   | Not used                                                |
| 9   | 60  | CE  |     |      |      | Deliver to ID               | Not used                                                |
| 10  | 8   | DT  |     |      |      | Date Needed                 | Not used                                                |

### NTE – Notes and Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>O</td>
<td></td>
<td></td>
<td>Set ID</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>105</td>
<td>Source of Comment</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>3</td>
<td>65536</td>
<td>FT</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Comment</td>
<td><p>1<sup>st</sup> repetition: String “POW:” followed by single character Prisoner Of War indicator calculated from the PATIENT ELIGIBILITIES (#361) field of the PATIENT (#2) file and the current enrollment status derived from the supported call $$STATUS^DGENA.</p>
<p>Example: <strong>POW:Y</strong></p>
<p>2<sup>nd</sup> repetition: String “PH:” followed by single character Purple Heart indicator calculated from CURRENT PH INDICATOR (#.531) and CURRENT PURPLE HEART STATUS (#.532) fields of the PATIENT (#2) file.</p>
<p>Example: <strong>PH:N</strong></p></td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>364</td>
<td>Comment Type</td>
<td>Not used</td>
</tr>
</tbody>
</table>

## Trigger Events and Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each triggering event is listed below along with the applicable form of the message to be exchanged. The notation used to describe the sequence, option, and repetition of segments is described in the HL7 V. 2.4 Standard Specification Manual, Chapter 2, and in summary form, in Section 2.1 of this document.

## ORM - General Order Message (event O01)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ORM~O01 message to be sent to the NCMD

ORM Order Message Section

MSH Message Header

PID Patient Identification

ORC Common Order

RQD Requisition Detail

NTE Notes and Comments

SAMPLE MESSAGE

MSH^~\|\\^VIC NCMD SEND^500~<span class="mark">REDACTED</span>~DNS^VIC NCMD RECV^NCMD^20031008144616-0400^^ORM~O01^50018835^P^2.4^^^NE^AL^USA

PID^1^222-33-4444\~~^1001178082V735077\~\~~USVHA&&L~NI^^DOE~JOHN^^

19500404^^^^^^^^^^^^222334444

ORC^RL

RQD^1^^22233444-DOE-1

NTE^^^POW:N\|PH:Y

## ORR – General Order Response Message response to any ORM (event O02)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon receipt of a VIC Card request order message, the NCMD will respond with an ORR~O02 message.

ORR Order Response Message

MSH Message Header

MSA Message Acknowledgment

SAMPLE MESSAGES

General Order Response (ORR~O02) message when the General Order Message (ORM~O01) is successful.

MSH^~\|\\^VIC NCMD RECV^NCMD^VIC NCMD SEND^500~ <span class="mark">REDACTED</span> ~DNS^20031008144616-0400^^ORR~O02^782218835^P^2.4^^^NE^AL^USA

MSA^AA^50018835

General Order Response (ORR~O02) message when the General Order Message (ORM~O01) fails.

MSH^~\|\\^VIC NCMD RECV^NCMD^VIC NCMD SEND^500~ <span class="mark">REDACTED</span> ~DNS^20031008144616-0400^^ORR~O02^782218835^P^2.4^^^NE^AL^USA

MSA^AE^50018835^CardID not on file

## Supported and User Defined HL7 Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Table 0003 - Event Type Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

O01 ORM – Order Message

O02 ORR – Order Response

### Table 0008 – Acknowledgment Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

AA Original mode: Application Accept

Enhanced mode: Application acknowledgment: Accept

AE Original mode: Application Error

Enhanced mode: Application acknowledgment: Error

AR Original mode: Application Reject

Enhanced mode: Application acknowledgment: Reject

CA Enhanced mode: Accept acknowledgment: Commit Accept

CE Enhanced mode: Accept acknowledgment: Commit Error

CR Enhanced mode: Accept acknowledgment: Commit Reject

### Table 0076 - Message Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

ORM Order Message

ORR Order Acknowledgment Message

### Table 0119 – Order Control Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VALUE DESCRIPTION

RL Release Previous Hold

CA Cancel Order Request

This Page Is Intentionally left blank for pagination conventions

# HL7 GENERIC PID, EVN, PV1 SEGMENT BUILDER ESTABLISHED BY MPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes functionality that can be used by other applications to dynamically build fully populated PID, EVN, and PV1 segments for use in communicating to and from VistA and/or HeV VistA.

This document specifies the information needed by applications to utilize the generic HL7 v2.4 segment builders. In order for applications to utilize this functionality they must first subscribe to the Integration Agreement \#3630 described below.

For more information about the specific data elements included in these segments, see the MPI HL7 v2.4 Interface Specification on the VDL at the following address:

http://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index\_(MPI)

## Integration Agreement (IA) \#3630

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Integration Agreement consists of three Health Level 7 (HL7), Version 2.4 segment builders in the form of the following APIs:

- BLDEVN^VAFCQRY
- BLDPD1^VAFCQRY
- BLDPID^VAFCQRY

These generic segment builders can be used to build Version 2.4 HL7 PID, EVN and PD1 segments.

### Custodial Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REGISTRATION has the following Subscribing Packages

- MASTER PATIENT INDEX VISTA
- CLINICAL INFO RESOURCE NETWORK
- OUTPATIENT PHARMACY
- CLINICAL PROCEDURES
- PHARMACY BENEFITS MANAGEMENT
- RADIOLOGY/NUCLEAR MEDICINE
- GEN. MED. REC. - VITALS
- ADVERSE REACTION TRACKING
- LAB SERVICE
- CLINICAL CASE REGISTRIES

## API: BLDEVN^VAFCQRY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description: The entry point builds the EVN segment via version 2.4 including the Treating Facility last treatment date and event reason.

Format BLDEVN^VAFCQRY

INPUT VARIABLES

DFN: Internal Entry Number of the patient in the PATIENT file (#2).

SEQ: Variable consisting of sequence numbers delimited by commas that will be used to

build the message.

EVN: (Passed by reference). This is the array location to place EVN segment result.

The array can have existing values when passed.

HL: Array that contains the necessary HL variables (init^hlsub).

EVR : Event reason that triggered this message.

ERR: Array used to return an error.

## API: BLDPD1^VAFCQRY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description: This entry point will build the version 2.4 PD1 segment.

Format BLDPD1^VAFCQRY

INPUT VARIABLES

DFN: Internal Entry Number of the patient in the PATIENT file (#2).

SEQ: Variable consisting of sequence numbers delimited by commas that will be used to build the message.

PD1: (Passed by reference). Array location to place PD1 segment result. The array can have existing values when passed.

HL: Array that contains the necessary HL variables (init^hlsub).

ERR: Array used to return an error.

## API: BLDPID^VAFCQRY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description: This entry point will build the version 2.4 PID segment.

Format

BLDPID^VAFCQRY

INPUT VARIABLES

DFN: Internal Entry Number of the patient in the PATIENT file (#2).

CNT: The value to be place in PID seq#1 (SET ID).

SEQ: Variable consisting of sequence numbers delimited by commas that will be used to build the message.

"ALL" can be passed to get all available fields in the PID Segment that are available. This is the default.

PID: (Passed by reference). The array location to place PID segment result, the array can have existing values when passed.

HL: Array that contains the necessary HL variables (init^hlsub).

ERR: Array used to return an error.

# HL7 Interface Specification for Home Telehealth (HTH)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Telehealth application is in support of the Care Coordination Program that involves the use of Home Telehealth technologies. Home Telehealth helps the Veterans Health Administration (VHA) by 836creating a framework for optimizing the overall development and implementation of Telemedicine in VHA.

This document specifies the information needed for activation and inactivation of Home Telehealth patients with their perspective HTH vendors.

This application will use the abstract message approach and encoding rules specified by HL7. HL7 is used for communicating data associated with various events which occur in health care environments.

The formats of these messages conform to the Version 2.4 HL7 Interface Standards.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The transmission of HTH registration/inactivation requests from VistA to the HTH vendors assumes the following.

- All VistA sites will have installed VistA HL7 software and it is operational.
- The associated VistA Consult Patch GMRC\*3\*42 has been installed and HTH consults activated.

## Message Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data sent in the HL7 messages will be limited to the information that is required to uniquely identify the patient and requested by the HTH vendors. The data transmitted will be recorded and available in VistA.

## Data Capture and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following event trigger will generate a Register a Patient (Event A04).

- Provider evaluates patient and refers patient for HTH care by submitting a consult request. A pending consult request goes to the HTH Care Coordinator and verifies eligibility. A registration request is submitted to HTH vendor by using Patient Sign-Up/Activation \[DGHT PATIENT SIGNUP\] menu option.
- The protocol DG HOME TELEHEALTH ADT-A04 CLIENT in PROTOCOL file (#101) is used for the Patient Sign-Up/Activation process.
- The entry DG HOME TELEHEALTH in the HL7 APPLICATION PARAMETER file (#771) is used for processing outgoing HL7 messages from the Home Telehealth vendors.
- The entry HTAPPL in the HL7 APPLICATION PARAMETER file (#771) is used for processing incoming HL7 messages from the Home Telehealth vendors.

The following entries in the HL LOGICAL LINK file (#870) facilitate the transmission of Home Telehealth patient data to Home Telehealth vendor server system via the Austin Interface.

- DG HT AMD
- DG HT ATI
- DG HT HH
- DG HT VIT
- DG HT VN
- DG HTH

The mail group DGHTERR generates mail messages for any transmission rejects received from the vendor server.

The following event trigger will generate an inactivation of a Patient (Event A03).

- HTH Care Coordinator determines patient care is now complete. An inactivation request is submitted to HTH vendor Patient Inactivation \[DGHT PATIENT INACTIVATION\] menu option.
- The protocol DG HOME TELEHEALTH ADT-A03 CLIENT in the PROTOCOL file (#101) is used for the Patient Inactivation process.
- The entry DG HOME TELEHEALTH in the HL7 APPLICATION PARAMETER file (#771) is used for processing outgoing HL7 messages from the Home Telehealth vendors.
- The entry HTAPPL in the HL7 APPLICATION PARAMETER file (#771) is used for processing incoming HL7 messages from the Home Telehealth vendors.

The following entries in the HL LOGICAL LINK file (#870) facilitate the transmission of Home Telehealth patient data to Home Telehealth vendor server system via the Austin Interface.

- DG HT AMD
- DG HT ATI
- DG HT HH
- DG HT VIT
- DG HT VN
- DG HTH

The mail group DGHTERR generates mail messages for any transmission rejects received from the vendor server.

> **NOTE:** Any modification made to the VistA database in non-standard ways, such as a direct global set by an application or by MUMPS code, will not be processed appropriately.

# VA TCP/IP Lower Level Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 V. 1.6 TCP/IP lower level protocol (LLP) will be used which implements the HL7 Minimal Lower Layer Protocol (MLLP) referenced in section C.4 of Appendix C of the Health Level 7 Implementation Guide (v2.4).

## HL7 CONTROL SEGMENTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the HL7 control segments supported by VistA. The messages are presented separately and defined by category. Segments are also described. The messages are presented in the Message Control category.

## Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the VistA perspective, all incoming or outgoing messages are handled or generated based on an event.

In this section and the following sections, the following elements will be defined for each message.

- Trigger events
- Message event code
- List of segments used in the message
- List of fields for each segment in the message

Each message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. A \[ \] indicates the segment is optional, the { } indicates the segment is repeatable. For each message category, there will be a list of HL7 standard segments used for the message.

## Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each segment, the data elements are described in table format. The table includes the sequence number (SEQ), maximum length (LEN), data type (DT), required or optional (R/O), repeatable (RP/#), the table number (TBL#), the element name, and the VistA description. Each segment is described in the following sections.

## Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments that are contained in message types described in this document. These are generic descriptions. Any time any of the segments described in this section are included in a message in this document, the VistA descriptions and mappings will be as specified here unless otherwise specified in that section.

MSH - MESSAGE HEADER SEGMENT

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SEQ</td>
<td>LEN</td>
<td>DT</td>
<td>R/O</td>
<td>RP/#</td>
<td>TBL#</td>
<td>ELEMENT NAME</td>
<td>VistA DESCRIPTION</td>
</tr>
<tr class="even">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td>Recommended value is ^ (caret)</td>
</tr>
<tr class="odd">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<p>Component = ~ (tilde)</p>
<p>Repeat = | (bar)</p>
<p>Escape = \ (back slash)</p>
<p>Sub-component = &amp; (ampersand)</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td>Sending station's facility number from Institution field of HL7 Communication Parameters file.</td>
</tr>
<tr class="even">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="odd">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Receiving station’s facility number from Institution field of HL Logical Link file.</td>
</tr>
<tr class="even">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Date and time message was created.</td>
</tr>
<tr class="odd">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p>2 Components</p>
<p>Refer to Table 0076</p>
<p>Refer to Table 0003</p></td>
</tr>
<tr class="odd">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by VISTA HL7 Package.</td>
</tr>
<tr class="even">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td>P (production)</td>
</tr>
<tr class="odd">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>Version ID field of event protocol in Protocol file.</td>
</tr>
<tr class="even">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td>NE (never acknowledge)</td>
</tr>
<tr class="odd">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td>AL (always acknowledge)</td>
</tr>
<tr class="even">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td>USA</td>
</tr>
<tr class="odd">
<td>18</td>
<td>6</td>
<td>ID</td>
<td></td>
<td>Y/3</td>
<td>0211</td>
<td>Character Set</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>19</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Principal Language of Message</td>
<td>Not used</td>
</tr>
</tbody>
</table>

EVN – EVENT TYPE SEGMENT

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SEQ</td>
<td>LEN</td>
<td>DT</td>
<td>R/O</td>
<td>RP/#</td>
<td>TBL#</td>
<td>ELEMENT NAME</td>
<td>VistA DESCRIPTION</td>
</tr>
<tr class="even">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td>Recommended value is ^ (caret)</td>
</tr>
<tr class="odd">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p>Recommended delimiter values:</p>
<p>Component = ~ (tilde)</p>
<p>Repeat = | (bar)</p>
<p>Escape = \ (back slash)</p>
<p>Sub-component = &amp; (ampersand)</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td>Sending station's facility number from Institution field of HL7 Communication Parameters file.</td>
</tr>
<tr class="even">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="odd">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Receiving station’s facility number from Institution field of HL Logical Link file.</td>
</tr>
<tr class="even">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Date and time message was created.</td>
</tr>
<tr class="odd">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p>2 Components</p>
<p>Refer to Table 0076</p>
<p>Refer to Table 0003</p></td>
</tr>
<tr class="odd">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by VISTA HL7 Package.</td>
</tr>
<tr class="even">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td>P (production)</td>
</tr>
<tr class="odd">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>Version ID field of event protocol in Protocol file.</td>
</tr>
<tr class="even">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td>NE (never acknowledge)</td>
</tr>
<tr class="odd">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td>AL (always acknowledge)</td>
</tr>
<tr class="even">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td>USA</td>
</tr>
<tr class="odd">
<td>18</td>
<td>6</td>
<td>ID</td>
<td></td>
<td>Y/3</td>
<td>0211</td>
<td>Character Set</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>19</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Principal Language of Message</td>
<td>Not used</td>
</tr>
</tbody>
</table>

PID - PATIENT IDENTIFICATION SEGMENT

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SEQ</td>
<td>LEN</td>
<td>DT</td>
<td>R/O</td>
<td>RP/#</td>
<td>TBL#</td>
<td>ELEMENT NAME</td>
<td>VistA DESCRIPTION</td>
</tr>
<tr class="even">
<td>1</td>
<td>4</td>
<td>SI</td>
<td></td>
<td></td>
<td></td>
<td>Set ID - Patient ID</td>
<td>Always set to ‘1’</td>
</tr>
<tr class="odd">
<td>2</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient ID (External ID)</td>
<td>Social Security Number field of Patient file.</td>
</tr>
<tr class="even">
<td>3</td>
<td>20</td>
<td>CM</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Patient ID (Internal ID)</td>
<td><p>Integrated Control Number (ICN) field of Patient file.</p>
<p>Component 1: ICN w/checksum</p>
<p>Component 2: DFN</p>
<p>Component 3: Null</p>
<p>Component 4: Assigning authority (subcomponent 1: ‘USVHA’, subcomponent 3: ‘L’</p>
<p>Component 5: Type ‘NI’</p></td>
</tr>
<tr class="odd">
<td>4</td>
<td>12</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Alternate Patient ID</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>5</td>
<td>48</td>
<td>PN</td>
<td>R</td>
<td></td>
<td></td>
<td>Patient Name</td>
<td>Name</td>
</tr>
<tr class="odd">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Maiden Name</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date of Birth</td>
<td>Date of birth</td>
</tr>
<tr class="odd">
<td>8</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0001</td>
<td>Sex</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>9</td>
<td>48</td>
<td>PN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Patient Alias</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>10</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0005</td>
<td>Race</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>11</td>
<td>106</td>
<td>AD</td>
<td></td>
<td>Y</td>
<td></td>
<td>Patient Address</td>
<td>Home Address</td>
</tr>
<tr class="odd">
<td>12</td>
<td>4</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>County Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>13</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Phone Number – Home</td>
<td>Home Phone Validated</td>
</tr>
<tr class="odd">
<td>14</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Phone Number – Business</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>15</td>
<td>25</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Language – Patient</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>16</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0002</td>
<td>Marital Status</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>17</td>
<td>3</td>
<td>ID</td>
<td></td>
<td></td>
<td>0006</td>
<td>Religion</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>18</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient Account Number</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>19</td>
<td>16</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>SSN Number – Patient</td>
<td>Social security number and pseudo indicator.</td>
</tr>
<tr class="odd">
<td>20</td>
<td>25</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
<td>Driver's Lic Num – Patient</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>21</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Identifier</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>22</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0189</td>
<td>Ethnic Group</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>23</td>
<td>25</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Birth Place</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>24</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Multiple Birth Indicator</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>25</td>
<td>2</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Birth Order</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>26</td>
<td>3</td>
<td>ID</td>
<td></td>
<td>Y</td>
<td>0171</td>
<td>Citizenship</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>27</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td>0172</td>
<td>Veterans Military Status</td>
<td>Not used</td>
</tr>
</tbody>
</table>

PD1 - PATIENT ADDITIONAL DEMOGRAPHIC SEGMENT

|     |     |     |     |      |      |       |                                             |
|-----|-----|-----|-----|------|------|-------|---------------------------------------------|
| SEQ | LEN | DT  | OPT | RP/# | TBL# | ITEM# | ELEMENT NAME                                |
| 1   | 2   | IS  | O   | Y    | 0223 | 00755 | Living Dependency                           |
| 2   | 2   | IS  | O   |      | 0220 | 00742 | Living Arrangement                          |
| 3   | 250 | XON | O   | Y    |      | 00756 | Patient Primary Facility                    |
| 4   | 250 | XCN | B   | Y    |      | 00757 | Patient Primary Care Provider Name & ID No. |
| 5   | 2   | IS  | O   |      | 0231 | 00745 | Student Indicator                           |
| 6   | 2   | IS  | O   |      | 0295 | 00753 | Handicap                                    |
| 7   | 2   | IS  | O   |      | 0315 | 00759 | Living Will Code                            |
| 8   | 2   | IS  | O   |      | 0316 | 00760 | Organ Donor Code                            |
| 9   | 1   | ID  | O   |      | 0136 | 00761 | Separate Bill                               |
| 10  | 250 | CX  | O   | Y    |      | 00762 | Duplicate Patient                           |
| 11  | 250 | CE  | O   |      | 0215 | 00743 | Publicity Code                              |
| 12  | 1   | ID  | O   |      | 0136 | 00744 | Protection Indicator                        |
| 13  | 8   | DT  | O   |      |      | 01566 | Protection Indicator Effective Date         |
| 14  | 250 | XON | O   | Y    |      | 01567 | Place of Worship                            |
| 15  | 250 | CE  | O   | Y    | 0435 | 01568 | Advance Directive Code                      |
| 16  | 1   | IS  | O   |      | 0441 | 01569 | Immunization Registry Status                |
| 17  | 8   | DT  | O   |      |      | 01570 | Immunization Registry Status Effective Date |
| 18  | 8   | DT  | O   |      |      | 01571 | Publicity Code Effective Date               |
| 19  | 5   | IS  | O   |      | 0140 | 01572 | Military Branch                             |
| 20  | 2   | IS  | O   |      | 0141 | 00486 | Military Rank/Grade                         |
| 21  | 3   | IS  | O   |      | 0142 | 01573 | Military Status                             |

PV1 PATIENT VISIT SEGMENT

| SEQ | LEN | DT  | OPT | RP/# | TBL#                                                                                                                                                                                                                                   | ITEM# | ELEMENT NAME                                                                                                                                                                                                                                                                                                                                    |
|-----|-----|-----|-----|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | 4   | SI  | O   |      |                                                                                                                                                                                                                                        | 00131 | Set ID - PV1                                                                                                                                                                                                                                                                                                                                    |
| 2   | 1   | IS  | R   |      | 0004                                                                                                                                                                                                                                   | 00132 | Patient Class                                                                                                                                                                                                                                                                                                                                   |
| 3   | 80  | PL  | O   |      |                                                                                                                                                                                                                                        | 00133 | Assigned Patient Location                                                                                                                                                                                                                                                                                                                       |
| 4   | 2   | IS  | O   |      | 0007                                                                                                                                                                                                                                   | 00134 | Admission Type                                                                                                                                                                                                                                                                                                                                  |
| 5   | 250 | CX  | O   |      |                                                                                                                                                                                                                                        | 00135 | Preadmit Number                                                                                                                                                                                                                                                                                                                                 |
| 6   | 80  | PL  | O   |      |                                                                                                                                                                                                                                        | 00136 | Prior Patient Location                                                                                                                                                                                                                                                                                                                          |
| 7   | 250 | XCN | O   | Y    | 0010                                                                                                                                                                                                                                   | 00137 | Attending Doctor                                                                                                                                                                                                                                                                                                                                |
| 8   | 250 | XCN | O   | Y    | 0010                                                                                                                                                                                                                                   | 00138 | Referring Doctor                                                                                                                                                                                                                                                                                                                                |
| 9   | 250 | XCN | B   | Y    | 0010                                                                                                                                                                                                                                   | 00139 | Consulting Doctor                                                                                                                                                                                                                                                                                                                               |
| 10  | 3   | IS  | O   |      | 0069                                                                                                                                                                                                                                   | 00140 | Hospital Service                                                                                                                                                                                                                                                                                                                                |
| 11  | 80  | PL  | O   |      |                                                                                                                                                                                                                                        | 00141 | Temporary Location                                                                                                                                                                                                                                                                                                                              |
| 12  | 2   | IS  | O   |      | 0087                                                                                                                                                                                                                                   | 00142 | Preadmit Test Indicator                                                                                                                                                                                                                                                                                                                         |
| 13  | 2   | IS  | O   |      | 0092                                                                                                                                                                                                                                   | 00143 | Re-admission Indicator                                                                                                                                                                                                                                                                                                                          |
| 14  | 6   | IS  | O   |      | 0023                                                                                                                                                                                                                                   | 00144 | Admit Source                                                                                                                                                                                                                                                                                                                                    |
| 15  | 2   | IS  | O   | Y    | [<u>0009</u>](file:///\\v17.MED.VA.GOV\..\..\vhaisbadamsr\AppData\Local\Microsoft\Users\vhaisbadamsr\AppData\Local\Microsoft\Users\vhaispsteelr\Local%20Settings\Temporary%20Internet%20Files\Content.Outlook\Local%20Settings\Temp\l) | 00145 | Ambulatory Status [<u>0009</u>](file://\\v17.med.va.gov\vhaisbadamsr\AppData\Local\Microsoft\Users\vhaisbadamsr\AppData\Local\Microsoft\Users\vhaispsteelr\AppData\Local\Microsoft\Windows\Temporary%20Internet%20Files\Content.Outlook\Local%20Settings\Local%20Settings\Temporary%20Internet%20Files\Content.Outlook\Local%20Settings\Temp\l) |
| 16  | 2   | IS  | O   |      | 0099                                                                                                                                                                                                                                   | 00146 | VIP Indicator                                                                                                                                                                                                                                                                                                                                   |
| 17  | 250 | XCN | O   | Y    | 0010                                                                                                                                                                                                                                   | 00147 | Admitting Doctor                                                                                                                                                                                                                                                                                                                                |
| 18  | 2   | IS  | O   |      | 0018                                                                                                                                                                                                                                   | 00148 | Patient Type                                                                                                                                                                                                                                                                                                                                    |
| 19  | 250 | CX  | O   |      |                                                                                                                                                                                                                                        | 00149 | Visit Number                                                                                                                                                                                                                                                                                                                                    |
| 20  | 50  | FC  | O   | Y    | 0064                                                                                                                                                                                                                                   | 00150 | Financial Class                                                                                                                                                                                                                                                                                                                                 |
| 21  | 2   | IS  | O   |      | 0032                                                                                                                                                                                                                                   | 00151 | Charge Price Indicator                                                                                                                                                                                                                                                                                                                          |
| 22  | 2   | IS  | O   |      | 0045                                                                                                                                                                                                                                   | 00152 | Courtesy Code                                                                                                                                                                                                                                                                                                                                   |
| 23  | 2   | IS  | O   |      | 0046                                                                                                                                                                                                                                   | 00153 | Credit Rating                                                                                                                                                                                                                                                                                                                                   |
| 24  | 2   | IS  | O   | Y    | 0044                                                                                                                                                                                                                                   | 00154 | Contract Code                                                                                                                                                                                                                                                                                                                                   |
| 25  | 8   | DT  | O   | Y    |                                                                                                                                                                                                                                        | 00155 | Contract Effective Date                                                                                                                                                                                                                                                                                                                         |
| 26  | 12  | NM  | O   | Y    |                                                                                                                                                                                                                                        | 00156 | Contract Amount                                                                                                                                                                                                                                                                                                                                 |
| 27  | 3   | NM  | O   | Y    |                                                                                                                                                                                                                                        | 00157 | Contract Period                                                                                                                                                                                                                                                                                                                                 |
| 28  | 2   | IS  | O   |      | 0073                                                                                                                                                                                                                                   | 00158 | Interest Code                                                                                                                                                                                                                                                                                                                                   |
| 29  | 4   | IS  | O   |      | 0110                                                                                                                                                                                                                                   | 00159 | Transfer to Bad Debt Code                                                                                                                                                                                                                                                                                                                       |
| 30  | 8   | DT  | O   |      |                                                                                                                                                                                                                                        | 00160 | Transfer to Bad Debt Date                                                                                                                                                                                                                                                                                                                       |
| 31  | 10  | IS  | O   |      | 0021                                                                                                                                                                                                                                   | 00161 | Bad Debt Agency Code                                                                                                                                                                                                                                                                                                                            |
| 32  | 12  | NM  | O   |      |                                                                                                                                                                                                                                        | 00162 | Bad Debt Transfer Amount                                                                                                                                                                                                                                                                                                                        |
| 33  | 12  | NM  | O   |      |                                                                                                                                                                                                                                        | 00163 | Bad Debt Recovery Amount                                                                                                                                                                                                                                                                                                                        |
| 34  | 1   | IS  | O   |      | 0111                                                                                                                                                                                                                                   | 00164 | Delete Account Indicator                                                                                                                                                                                                                                                                                                                        |
| 35  | 8   | DT  | O   |      |                                                                                                                                                                                                                                        | 00165 | Delete Account Date                                                                                                                                                                                                                                                                                                                             |
| 36  | 3   | IS  | O   |      | 0112                                                                                                                                                                                                                                   | 00166 | Discharge Disposition                                                                                                                                                                                                                                                                                                                           |
| 37  | 47  | DLD | O   |      | 0113                                                                                                                                                                                                                                   | 00167 | Discharged to Location                                                                                                                                                                                                                                                                                                                          |
| 38  | 250 | CE  | O   |      | 0114                                                                                                                                                                                                                                   | 00168 | Diet Type                                                                                                                                                                                                                                                                                                                                       |
| 39  | 2   | IS  | O   |      | 0115                                                                                                                                                                                                                                   | 00169 | Servicing Facility                                                                                                                                                                                                                                                                                                                              |
| 40  | 1   | IS  | B   |      | 0116                                                                                                                                                                                                                                   | 00170 | Bed Status                                                                                                                                                                                                                                                                                                                                      |
| 41  | 2   | IS  | O   |      | 0117                                                                                                                                                                                                                                   | 00171 | Account Status                                                                                                                                                                                                                                                                                                                                  |
| 42  | 80  | PL  | O   |      |                                                                                                                                                                                                                                        | 00172 | Pending Location                                                                                                                                                                                                                                                                                                                                |
| 43  | 80  | PL  | O   |      |                                                                                                                                                                                                                                        | 00173 | Prior Temporary Location                                                                                                                                                                                                                                                                                                                        |
| 44  | 26  | TS  | O   |      |                                                                                                                                                                                                                                        | 00174 | Admit Date/Time                                                                                                                                                                                                                                                                                                                                 |
| 45  | 26  | TS  | O   | Y    |                                                                                                                                                                                                                                        | 00175 | Discharge Date/Time                                                                                                                                                                                                                                                                                                                             |
| 46  | 12  | NM  | O   |      |                                                                                                                                                                                                                                        | 00176 | Current Patient Balance                                                                                                                                                                                                                                                                                                                         |
| 47  | 12  | NM  | O   |      |                                                                                                                                                                                                                                        | 00177 | Total Charges                                                                                                                                                                                                                                                                                                                                   |
| 48  | 12  | NM  | O   |      |                                                                                                                                                                                                                                        | 00178 | Total Adjustments                                                                                                                                                                                                                                                                                                                               |
| 49  | 12  | NM  | O   |      |                                                                                                                                                                                                                                        | 00179 | Total Payments                                                                                                                                                                                                                                                                                                                                  |
| 50  | 250 | CX  | O   |      | 0203                                                                                                                                                                                                                                   | 00180 | Alternate Visit ID                                                                                                                                                                                                                                                                                                                              |
| 51  | 1   | IS  | O   |      | 0326                                                                                                                                                                                                                                   | 01226 | Visit Indicator                                                                                                                                                                                                                                                                                                                                 |
| 52  | 250 | XCN | B   | Y    | 0010                                                                                                                                                                                                                                   | 01274 | Other Healthcare Provider                                                                                                                                                                                                                                                                                                                       |

MSA – MESSAGE ACKNOWLEDGMENT SEGMENT

|     |     |     |     |      |      |                             |                                                       |
|-----|-----|-----|-----|------|------|-----------------------------|-------------------------------------------------------|
| SEQ | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME                | VistA DESCRIPTION                                     |
| 1   | 2   | ID  | R   |      | 0008 | Acknowledgment Code         | Refer to HL7 table 0008                               |
| 2   | 20  | ST  | R   |      |      | Message Control ID          | Message Control ID of the message being acknowledged. |
| 3   | 80  | ST  | O   |      |      | Text Message                | Free text error message                               |
| 4   | 15  | NM  | O   |      |      | Expected Sequence Number    | Not used                                              |
| 5   | 1   | ID  | B   |      | 0102 | Delayed Acknowledgment Type | Not used                                              |
| 6   | 100 | CE  | O   |      |      | Error Condition             | Not used                                              |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Also please refer to the following sites.
OI Master Glossary: <http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm>
National Acronym Directory: <http://vaww1.va.gov/Acronyms/>
<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>ADD-ONS</th>
<th>Patients who have been scheduled for a visit after routing slips for a particular date have been printed.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ALOS</td>
<td>Average Length of Stay</td>
</tr>
<tr class="even">
<td>AMIS</td>
<td>Automated Management Information System</td>
</tr>
<tr class="odd">
<td>ANCILLARY</td>
<td>A test added to an existing appointment (i.e. lab, x-ray, EKG) test</td>
</tr>
<tr class="even">
<td>API</td>
<td>Application Program Interface</td>
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
<td>Computerized Patient Record System (CPRS)</td>
<td>An integrated, comprehensive suite of clinical applications in VistA that work together to create a longitudinal view of the veteran’s Electronic Medical Record (EMR). CPRS capabilities include a Real Time Order Checking System, a Notification System to alert clinicians of clinically significant events, Consult/Request tracking and a Clinical Reminder System. CPRS provides access to most components of the patient chart.</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Computerized Patient Record System</td>
</tr>
<tr class="odd">
<td>CPT</td>
<td>Current Procedural Terminology</td>
</tr>
<tr class="even">
<td>CR</td>
<td>Clinical Reminders</td>
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
<td>ICR</td>
<td>Integration Control Reference</td>
</tr>
<tr class="odd">
<td>IRT</td>
<td>Incomplete Records Tracking</td>
</tr>
<tr class="even">
<td>IVMH</td>
<td>Improve Veteran Mental Health</td>
</tr>
<tr class="odd">
<td>MEANS TEST</td>
<td>A financial report upon which certain patients' eligibility for care is based</td>
</tr>
<tr class="even">
<td>Mental Health Treatment Coordinator (MHTC)</td>
<td><p>The liaison between the patient and the mental health system at a VA site. There is only one Mental Health treatment coordinator per patient and they are the key coordinator for behavioral health services care.</p>
<p>For more information about the MH treatment coordinator’s responsibilities, see VHA Handbook 1160.1, “Uniform Mental Health Services in VA Medical Centers for Clinics,” page 3-4. Note: In the handbook, the MHTC is called the Principal Mental Health Provider.</p></td>
</tr>
<tr class="odd">
<td>MH</td>
<td>Mental Health</td>
</tr>
<tr class="even">
<td>MHA3</td>
<td>Mental Health Assistant 3 package</td>
</tr>
<tr class="odd">
<td>MHTC</td>
<td>Mental Health Treatment Coordinator</td>
</tr>
<tr class="even">
<td>NO SHOW</td>
<td>A person who did not report for a scheduled clinic visit without prior notification to the medical center.</td>
</tr>
<tr class="odd">
<td>NON-COUNT</td>
<td>A clinic whose visits do not affect AMIS statistics.</td>
</tr>
<tr class="even">
<td>NSR</td>
<td>New Service Request</td>
</tr>
<tr class="odd">
<td>OE/RR</td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="even">
<td>OPC</td>
<td>Outpatient Clinic</td>
</tr>
<tr class="odd">
<td>OR</td>
<td>CPRS Order Entry/Results Reporting namespace</td>
</tr>
<tr class="even">
<td>PAF</td>
<td>Patient Assessment File; where PAI information is stored until transmission to Austin.</td>
</tr>
<tr class="odd">
<td>PAI</td>
<td>Patient Assessment Instrument</td>
</tr>
<tr class="even">
<td>PCE</td>
<td>Patient Care Encounter</td>
</tr>
<tr class="odd">
<td>PCMM</td>
<td>Primary Care Management Module</td>
</tr>
<tr class="even">
<td>PRF</td>
<td>Patient Record Flag</td>
</tr>
<tr class="odd">
<td>Principal Mental Health Provider (PMHP)</td>
<td>See MH Treatment Coordinator (MHTC)</td>
</tr>
<tr class="even">
<td>PTF</td>
<td>Patient Treatment File</td>
</tr>
<tr class="odd">
<td>PULL LIST</td>
<td>A list of patients whose radiology/PIMS records should be "pulled" from the file room for scheduled clinic visits</td>
</tr>
<tr class="even">
<td>PX</td>
<td>Patient Care Encounter namespace</td>
</tr>
<tr class="odd">
<td>PXRM</td>
<td>Clinical Reminders package namespace</td>
</tr>
<tr class="even">
<td>RAM</td>
<td>Resource Allocation Methodology</td>
</tr>
<tr class="odd">
<td>Reminder Definitions</td>
<td>These are pre-defined sets of findings that are used to identify patient cohorts and reminder resolutions. The reminder is used for patient care and/or report extracts.</td>
</tr>
<tr class="even">
<td>Reminder Dialogs</td>
<td>These are pre-defined sets of text and findings that provide information to the CPRS GUI for collecting and updating appropriate findings while building a progress note.</td>
</tr>
<tr class="odd">
<td>Reminder Terms</td>
<td>Terms are used to map local findings to national findings, providing a method to standardize the findings for national use. These are also used for local grouping of findings for easier reference in reminders and are defined in the Reminder Terms file.</td>
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
<td>An ongoing survey of care given to patients alleging Agent Orange or Ionizing Radiation exposure. Each visit by such patients must receive "special survey dispositioning" which records whether treatment provided was related to their exposure. This data is used for Congressional reporting purposes.</td>
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
<td>Text Integration Utility namespace</td>
</tr>
<tr class="odd">
<td>TIU</td>
<td>Text Integration Utility</td>
</tr>
<tr class="even">
<td>TSR</td>
<td>Treating Specialty Report</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Information System and Technology Architecture</td>
</tr>
</tbody>
</table>

# Military Time Conversion Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

This Page Is Intentionally left blank for pagination conventions

# Alphabetical Index of PIMS Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ACRP Ad Hoc Report

ACRP Database Conversion

Add / Edit a Holiday

Add / Edit Stop Codes

Alpha List of Incomplete Encounters

Append Ancillary Test to Appt.

Appointment Check-in / Check-out

Appointment List

Appointment Management

Appointment Management Report

Appointment Status Update

Appointment Waiting Time Report

Batch Update Comp Gen Appt Type for C&Ps

Call List

Cancel Appointment

Cancel Clinic Availability

Cancelled Clinic Report

Change Patterns to 30-60

Chart Request

Check Transmitted Outpatient Encounter Files

Check-in / Unsched. Visit

Clinic Appointment Availability Report

Clinic Assignment Listing

Clinic Edit Log Report

Clinic Group Maintenance for Reports

Clinic List (Day of Week)

Clinic Next Available Appt. Monitoring Report

Clinic Profile

Clinic Utilization Statistical Summary

Computer Generated Appointment Type Listing

Convert Patient File Fields to PCMM

Correct Incomplete Encounters

Current MAS Release Notes

Data Transmission Report

Delete an Ad Hoc Report Template

Delete Ancillary Test for Appt.

Discharge from Clinic

Display Ad Hoc Report Template Parameters

Display Appointments

Display Clinic Availability Report

Edit Appointment Type for Add / Edit Encounters

Edit Clinic Enrollment Data

Edit Clinic Stop Code Name- Local Entries Only

Edit Computer Generated Appointment Type

Edit Outpatient Encounter

Enc. by DSS ID / DSS ID by Freq. (OP0, OP1, OP2)

Enc. by IP DSS ID / DSS ID by Freq. (IP0, IP1, IP2)

Encounter ‘Action Required’ Report

Encounter Activity Report

Encounters Transmitted with MT Status of U

Enrollment Review Date Entry

Enrollments \> X Days

Enter / Edit Letters

Error Listing

File Room List

Find Next Available Appointment

Future Appointments for Inpatients

High Risk MH No-Show Adhoc Report

High Risk MH No-Show Nightly Report

Inactivate a Clinic

Incomplete Encounter Error Report

Incomplete Encounters by Error Code

Inpatient Appointment List

Look Up on Clerk Who Made Appointment

Make Appointment

Make Consult Appointment

Management Edit

Management Report for Ambulatory Procedures

Means Test / Eligibility / Enrollment Report

Means Test IP Visits & Unique (IP3, IP4, IP5)

Means Test Visits & Uniques (OP3, OP4, OP5)

Most Frequent 20 IP Practitioner Types (IP8)

Most Frequent 20 Practitioner Types (OP8)

Most Frequent 50 CPT Codes (OP6)

Most Frequent 50 ICD-9-CM Codes (OP7)

Most Frequent 50 IP CPT Codes (IP6)

Most Frequent 50 IP ICD-9-CM Codes (IP7)

Multiple Appointment Booking

Multiple Clinic Display / Book

Non-Conforming Clinics Stop Code Report

No-Show Report

No-Shows

Outpatient Diagnosis / Procedure Code Search

Outpatient Diagnosis / Procedure Frequency Report

Outpatient Encounter Workload Statistics

Patient Activity by Appointment Frequency

Patient Appointment Statistics

Patient Encounter List

Patient Profile MAS

Performance Monitor Detailed Report

Performance Monitor Retransmit Report (AAC)

Performance Monitor Summary Report

Print Appointment Status Update (Date Range)

Print from Ad Hoc Template

Print Scheduling Letters

Provider / Diagnosis Report

Purge Ambulatory Care Reporting files

Purge Appointment Status Update Log File

Purge rejections that are past database close-out

Purge Scheduling Data

Radiology Pull List

Reactivate a Clinic

Remap Clinic

Restore Clinic Availability

Retransmit Ambulatory Care Data by Date Range

Retransmit Selected Error Code

Retroactive Visits List

Review of Scheduling / PCE / Problem List Data

Routing Slips

SC Veterans Awaiting Appointments

Scheduling / PCE Bad Pointer Count

Scheduling Parameters

Selective Retransmission of NPCDB Rejections

Set up a Clinic

Sharing Agreement Category Update

Stop Code Listing (Computer Generated)

Summary Report - IEMM

Team / Position Assignment / Re-Assignment

Tracking Report

Transmission History for Patient

Transmission History Report - Full

Trend of Facility Uniques by 12 Month Date Ranges

Veterans Without Activity Since a Specified Date

View Appointment Status Update Date (Single Date)

Visit Rpt by Transmitted OPT Encounter

Visits and Unique IP SSNs by County (IP9)

Visits and Unique SSNs by County (OP9)

Workd Report

[^1]: Special meaning placed on this field to support multiple rejection reasons by the National Patient Care Database (NPCDB).

[^2]: According to the HL7 standard, the maximum length of this element is 2.

[^3]: This element is also found in the Patient Identification (PID) segment.

[^4]: This element is also found in the Patient Identification (PID) segment.