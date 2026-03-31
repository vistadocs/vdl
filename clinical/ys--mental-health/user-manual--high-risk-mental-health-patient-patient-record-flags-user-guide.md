---
title: High Risk Mental Health Patient - Patient Record Flags User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: High Risk Mental Health Patient - Patient Record Flags
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 16
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - blockquote
  - table
  - patient
  - flag
  - contents
  - record
  - class
  - style
  - width
  - health
page_count: 0
word_count: 11694
section_count: 27
table_count: 7
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/patrecflagug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/patrecflagug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/001.png)

# PATIENT RECORD FLAGS (PRF) USER GUIDE


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [PATIENT RECORD FLAGS (PRF) USER GUIDE](#patient-record-flags-prf-user-guide)
- [Version 5.3](#version-53)
- [Revision History](#revision-history)
- [Orientation](#orientation)
  - [Legal Requirements](#legal-requirements)
  - [Intended Audience](#intended-audience)
  - [Disclaimers](#disclaimers)
  - [Documentation Conventions](#documentation-conventions)
  - [Documentation Navigation](#documentation-navigation)
  - [Reference Materials and Related Manuals](#reference-materials-and-related-manuals)
    - [Patient Record Flag](#patient-record-flag)
    - [Health Summary GMTS\2.7\ 104 Documentation](#health-summary-gmts27-104-documentation)
    - [CPRS OR\2.0\348 Documentation](#cprs-or20348-documentation)
  - [VistA Documentation](#vista-documentation)
  - [General Support](#general-support)
- [Introduction](#introduction)
  - [Patient Record Flag Usage](#patient-record-flag-usage)
    - [Updated PRF Narratives](#updated-prf-narratives)
- [Use of the Software](#use-of-the-software)
  - [New Functionality:](#new-functionality)
  - [DG\5.3\849 - DGPF New Category I Flag and Conversion Patch](#dg53849-dgpf-new-category-i-flag-and-conversion-patch)
    - [New National Patient Record Flag (PRF) for Suicide Prevention (HIGH RISK FOR SUICIDE)](#new-national-patient-record-flag-prf-for-suicide-prevention-high-risk-for-suicide)
    - [New DGPF CLINICAL HR Flag Review Mail Group](#new-dgpf-clinical-hr-flag-review-mail-group)
    - [New Convert Local HRMH PRF to National \[DGPF LOCAL TO NATIONAL CONVERT\] Option](#new-convert-local-hrmh-prf-to-national-dgpf-local-to-national-convert-option)
  - [DG\5.3\836 Patch – HRMH - Vista Changes For National Reminder & Flag](#dg53836-patch-hrmh-vista-changes-for-national-reminder-flag)
  - [Patient Record Flag Main Menu \[DGPF RECORD FLAG MAIN MENU\]](#patient-record-flag-main-menu-dgpf-record-flag-main-menu)
    - [Patient Record Flag Main Menu](#patient-record-flag-main-menu)
    - [RM - Record Flag Reports Menu](#rm-record-flag-reports-menu)
    - [FA - Record Flag Assignment](#fa-record-flag-assignment)
    - [FM - Record Flag Management](#fm-record-flag-management)
    - [TM - Record Flag Transmission MGMT](#tm-record-flag-transmission-mgmt)
    - [ED - Record Flag Enable Divisions](#ed-record-flag-enable-divisions)
  - [Record Flag Reports Menu](#record-flag-reports-menu)
    - [Assignment Action Not Linked Report \[DGPF ACTION NOT LINKED REPORT\]](#assignment-action-not-linked-report-dgpf-action-not-linked-report)
    - [Flag Assignment Report \[DGPF FLAG ASSIGNMENT REPORT\]](#flag-assignment-report-dgpf-flag-assignment-report)
    - [Patient Assignments Report \[DGPF PATIENT ASSIGNMENT REPORT\]](#patient-assignments-report-dgpf-patient-assignment-report)
    - [Assignments Due for Review Report \[DGPF ASSIGNMENT DUE REVIEW RPT\]](#assignments-due-for-review-report-dgpf-assignment-due-review-rpt)
    - [Assignments by Principal Investigator Report \[DGPF PRINCIPAL INVEST REPORT\]](#assignments-by-principal-investigator-report-dgpf-principal-invest-report)
  - [Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\]](#record-flag-assignment-dgpf-record-flag-assignment)
    - [SP - Select Patient](#sp-select-patient)
    - [DA - Display Assignment Details](#da-display-assignment-details)
    - [AF - Assign Flag](#af-assign-flag)
    - [EF - Edit Flag Assignment](#ef-edit-flag-assignment)
    - [CO - Change Assignment Ownership](#co-change-assignment-ownership)
  - [Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\]](#record-flag-management-dgpf-record-flag-management)
    - [CC - Change Category](#cc-change-category)
    - [CS - Change Sort](#cs-change-sort)
    - [DF - Display Flag Detail](#df-display-flag-detail)
    - [AF - Add New Record Flag](#af-add-new-record-flag)
    - [EF - Edit Record Flag](#ef-edit-record-flag)
  - [Record Flag Transmission Mgmt](#record-flag-transmission-mgmt)
    - [Record Flag Transmission Errors \[DGPF TRANSMISSION ERRORS\]](#record-flag-transmission-errors-dgpf-transmission-errors)
    - [Record Flag Manual Query \[DGPF MANUAL QUERY\]](#record-flag-manual-query-dgpf-manual-query)
  - [Record Flag Enable Divisions \[DGPF ENABLE DIVISIONS\]](#record-flag-enable-divisions-dgpf-enable-divisions)
- [Additional Patient Record Flag Information](#additional-patient-record-flag-information)
  - [PRF Display on Patient Look-up](#prf-display-on-patient-look-up)
  - [Patient Record Flag in CPRS](#patient-record-flag-in-cprs)
  - [Creating, Assigning, and Maintaining PRF](#creating-assigning-and-maintaining-prf)
  - [Documenting PRF](#documenting-prf)
  - [Prerequisites to Writing PRF Progress Notes](#prerequisites-to-writing-prf-progress-notes)
  - [PRF Note Titles](#prf-note-titles)
  - [Linking PRF Notes to Flag Actions](#linking-prf-notes-to-flag-actions)
  - [Marking PRF as Entered in Error](#marking-prf-as-entered-in-error)
    - [Viewing PRF in CPRS GUI](#viewing-prf-in-cprs-gui)
- [Glossary](#glossary)
- [APPENDIX A: Memorandum](#appendix-a-memorandum)
- [National Patient Record Flag for High Risk for Suicide](#national-patient-record-flag-for-high-risk-for-suicide)
- [APPENDIX B: VHA DIRECTIVE 2010-053 PATIENT RECORD FLAGS](#appendix-b-vha-directive-2010-053-patient-record-flags)
    - [PATIENT RECORD FLAGS](#patient-record-flags)
    - [BACKGROUND](#background)
    - [POLICY:](#policy)
    - [ACTION](#action)
    - [REFERENCES](#references)
    - [ATTACHMENT A](#attachment-a)
    - [ATTACHMENT B](#attachment-b)
    - [ATTACHMENT C](#attachment-c)
    - [ATTACHMENT D](#attachment-d)
    - [NEW SERVICE REQUESTS CATEGORY I PATIENT RECORD FLAG (PRF)](#new-service-requests-category-i-patient-record-flag-prf)
    - [PROCESS](#process)
    - [APPLICATION](#application)
> Patch DG\*5.3\*849

# Version 5.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> April 2013

> Department of Veterans Affairs Office of Information and Technology (OIT)

> This page intentionally left blank for double-sided printing.

# Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table displays the revision history for this document. Revisions to the documentation are based on patches, style updates, and new versions released to the field:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 47%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>DATE</th>
<th>REVISION</th>
<th>DESCRIPTION</th>
<th>AUTHOR</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>4/2013</td>
<td>2.0</td>
<td><p>The Patient Record Flag (PRF) User Guide Title Page was changed to include Patch DG*5.3*849 and the date of April 2013.</p>
<p>The DG*5.3*849 DGPF NEW CATEGORY I FLAG AND</p>
<p>CONVERSION patch implements the following <strong>new</strong> functionality:</p>
<p>National Patient Record Flag (PRF) for suicide prevention (HIGH RISK FOR SUICIDE)</p>
<p>Convert Local HRMH PRF to National [DGPF LOCAL TO NATIONAL</p>
<p>CONVERT] Option</p>
<p>DGPF CLINICAL HR FLAG REVIEW</p>
<p>mail group</p>
<p>Added copy of Memorandum For National Patient Record Flag For High Risk For Suicide.</p>
<p>VHA Directive 2010-053, <strong>Embedded</strong> PDF document.</p>
<p>New operating directions include updated screen captures and new DG routines.</p>
<p>Some naming conventions were addressed Added descriptions of functions.</p>
<p>Added Technical Publications upgrades.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Revision History

> Revision History (continued)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 47%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>02/2012</th>
<th>2.0</th>
<th><p>DG*5.3*836 - Registration patch with Patient Record Flag APIs. This Registration Patient Record Flag patch provides new interfaces used by the Scheduling and Reminder patches to determine the High Risk for Suicide Flag status on a specified date.</p>
<p>This patch implements two new Application Programming Interfaces (APIs) for retrieving Patient Record Flag (PRF) information in support of the High Risk Mental Health initiatives.</p></th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/2006</td>
<td>1.0</td>
<td>The original release of this manual was titled Patient Record Flag Phase III User Guide DG*5.3*650 and released on November 2006.</td>
<td>PIMS Technical Writer</td>
</tr>
</tbody>
</table>
# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no special legal requirements involved in the use of VistA software.

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 74%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>READERS/USERS</th>
<th><blockquote>
<p>AUDIENCE(s)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRODUCT SUPPORT (PS) PERSONNEL</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td>INFORMATION RESOURCE MANAGEMENT (IRM)</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PRODUCT DEVELOPMENT (PD)—VISTA LEGACY DEVELOPMENT TEAMS</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SUICIDE PREVENTION COORDINATOR (SPC)/MENTAL HEALTH (MH) PROFESSIONALS</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>AUTOMATED DATA PROCESSING APPLICATION COORDINATOR (ADPAC)</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td>HELP DESK PERSONNEL/INFORMATION TECHNOLOGY (IT) SPECIALISTS</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This guide provides Release Notes and post installation guidance. An overall explanation of how to configure the Patient Record Flag (PRF) software package is not in this abbreviated manual.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](high-risk-mental-health-patient-patient-record-flags-user-guide/002.png)</p>
</blockquote></th>
<th><blockquote>
<p>DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information the user can find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Orientation

## Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This guide uses several methods to highlight different aspects of the material:

> Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Symbol</th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](high-risk-mental-health-patient-patient-record-flags-user-guide/003.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>NOTE/REF:</strong> Used to inform the reader of general information including references to additional reading material.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Descriptive text is presented in a proportional font (as represented by this font). Conventions for displaying TEST data in this document are as follows:

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/004.png) The first three digits (prefix) of any Social Security Numbers (SSN) begin with either "000" or "666".

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/005.png) Patient and user names are formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry

> (e.g., A1PATIENT, ONE; A1USER,ONE).

> "Snapshots" of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and can be enclosed within a box.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/006.png) Emphases within a dialogue box are in bold typeface and highlighted in blue (e.g., STANDARD LISTENER: RUNNING).

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/007.png) Some software code reserved/key words are in bold typeface with alternate color font.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/008.png) References to "\<Enter\>" within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing

> \<PF1\>.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/009.png)Author's comments are displayed in italics or as "callout" boxes.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](high-risk-mental-health-patient-patient-record-flags-user-guide/010.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Orientation

## Documentation Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document uses Microsoft® Word's built-in navigation for internal hyperlinks. To add Back

> and Forward navigation buttons to your toolbar, do the following:

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/011.png) Right-click anywhere on the customizable Toolbar in Word 2007 (not the Ribbon section).

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/012.png) Select Customize Quick Access Toolbar from the secondary menu. ![](high-risk-mental-health-patient-patient-record-flags-user-guide/013.png) Press the dropdown arrow in the "Choose commands from:" box.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/014.png) Select All Commands from the displayed list.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/015.png) Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/016.png) Click/Highlight the Back command and press the Add button to add it to your customized toolbar.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/017.png) Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/018.png) Click/Highlight the Forward command and press the Add button to add it to your customized toolbar.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/019.png) Press OK.

> You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in the Microsoft® Word document when clicking on hyperlinks within the document.

## Reference Materials and Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The use of Patient Record Flags must be strictly controlled and implemented following the instruction provided in the documents listed below:

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/020.png) APPENDIX A - Memorandum National Patient Record Flag for High Risk for Suicide. ![](high-risk-mental-health-patient-patient-record-flags-user-guide/021.png) APPENDIX B - VHA Directive 2010-053, Patient Record Flags.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/022.png) VHA Directives are available on-line at the following link: [<u>http://vaww1.va.gov/vhapublications/index.cfm</u>](http://vaww1.va.gov/vhapublications/index.cfm)

> Readers who wish to learn more about PRF operations, features, files, options, and user information can view the VistA VA Software Document Library (VDL) at the following link: [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/)

> Orientation

### Patient Record Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>INFORMATION</p>
</blockquote></th>
<th><blockquote>
<p>DOCUMENT PROFILE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRF HL7 Interface Spec</td>
<td><blockquote>
<p>Patient Record Flag HL7 Interface Specification</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Phase 1 Release Notes</td>
<td><blockquote>
<p>Patient Record Flag Phase I Release Notes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Phase II Release Notes</td>
<td><blockquote>
<p>Patient Record Flag Phase II Release Notes</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Phase III Release Notes</td>
<td><blockquote>
<p>Patient Record Flag Phase III Release Notes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PRF User Guide (this manual)</td>
<td><blockquote>
<p>Patient Record Flag User Guide</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="Clinical_Reminders_PXRM*2*24_Documentati" class="anchor"></span>Clinical Reminders PXRM\*2\*24 Documentation

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>DOCUMENTATION</th>
<th><blockquote>
<p>DOCUMENTATION FILE NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>High Risk Mental Health Patient Project Installation and Setup</p>
<p>Guide</p></td>
<td><blockquote>
<p>PXRM_2_24_IG.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>High Risk Mental Health Patient</p>
<p>Project Release Notes Release Notes</p></td>
<td><blockquote>
<p>PXRM_2_24_RN.PDF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Clinical Reminders User Manual</td>
<td><blockquote>
<p>PXRM_2_UM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Clinical Reminders Manager’s Manual</td>
<td><blockquote>
<p>PXRM_2_MM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Health Summary GMTS\*2.7\* 104 Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>DOCUMENTATION</th>
<th><blockquote>
<p>DOCUMENTATION FILE NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Health Summary User Manual</td>
<td><blockquote>
<p>HSUM_2_7_104_UM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Health Summary Technical Manual</td>
<td><blockquote>
<p>HSUM_2_7_104_TM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="TIU*1*265_Documentation" class="anchor"></span>TIU\*1\*265 Documentation

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>DOCUMENTATION</th>
<th><blockquote>
<p>DOCUMENTATION FILE NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Text Integration Utility User</p>
<p>Manual</p></td>
<td><blockquote>
<p>TIUUM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Text Integration Utility Technical Manual</td>
<td><blockquote>
<p>TIUTM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

Orientation

### CPRS OR\*2.0\*348 Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>DOCUMENTATION</th>
<th><blockquote>
<p>DOCUMENTATION FILE NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CPRS User Guide: GUI Version</td>
<td><blockquote>
<p>CPRSGUIUM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CPRS Technical Manual: GUI Version</td>
<td><blockquote>
<p>CPRSGUITM.PDF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CPRS Technical Manual</td>
<td><blockquote>
<p>CPRSLMTM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="Scheduling_SD*5.3*588_and_Registration_D" class="anchor"></span>Scheduling SD\*5.3\*588 and Registration DG\*5.3\*849 Documentation

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>DOCUMENTATION</th>
<th><blockquote>
<p>DOCUMENTATION FILE NAME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PIMS Technical Manual</td>
<td><blockquote>
<p>PIMSTM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>PIMS SCHEDULING User</p>
<p>Manual - Outputs Menu</p></td>
<td><blockquote>
<p>PIMsSchOutput.PDF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>PIMS SCHEDULING User</p>
<p>Manual - Menus, Intro &amp; Orientation, etc.</p></td>
<td><blockquote>
<p>PIMsSchIntro.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Patient Record Flag User Guide</td>
<td><blockquote>
<p>PatRecFlagUG.PDF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Scheduling and Registration Installation Review Guide</td>
<td><blockquote>
<p>SDDG_Install_Review.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Orientation

> Documentation Website Locations

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 36%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SITE</p>
</blockquote></th>
<th><blockquote>
<p>URL</p>
</blockquote></th>
<th><blockquote>
<p>DESCRIPTION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>National Clinical Reminders site</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p>Contains manuals, PowerPoint presentations, and other information about Clinical Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VistA Document Library</td>
<td><blockquote>
<p><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Contains manuals for Patient Record Flags and related applications.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## VistA Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA documentation is made available online in Microsoft® Word format and Adobe® Acrobat Portable Document Format (PDF). The PDF documents must be read using the Adobe® Acrobat Reader, which is freely distributed by Adobe® Systems Incorporated at the following Website[: .](http://www.adobe.com/) VistA documentation can also be downloaded from the Product Support (PS) anonymous directories:

> NOTE: This method transmits the files from the first available File Transfer Protocol (FTP) server.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/023.png)![](high-risk-mental-health-patient-patient-record-flags-user-guide/024.png) <span class="mark">REDACTED</span>

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/025.png) <span class="mark">REDACTED</span>

> <span class="mark">REDACTED</span>

## General Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For support, site questions, and problems with the Patient Record Flag software packages, please enter a National Remedy ticket to MAS-Patient Record Flags or call the <span class="mark">REDACTED</span> for assistance.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patient Record Flag Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient Record Flags (PRFs) are used to alert Veterans Health Administration (VHA) medical staff and employees of patients whose behavior and characteristics may pose a threat either to their safety, the safety of other patients, or compromise the delivery of quality health care. PRFs assignments are displayed during the patient look-up process.

> The Patient Record Flag (PRF) software described within provides users with the ability to create, assign, inactivate, edit, produce reports, and view patient record flag alerts.

> Patient record flags are divided into Category I (national) and Category II (local) flags. Category I flags are nationally approved and distributed by VHA nationally released software for implementation by all facilities.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/026.png) Category I flags are shared across all known treating facilities for the patient utilizing VistA HL7 messaging. This uses the abstract messaging approach and encoding rules specified by HL7 for communicating data associated with various events in health care environments. For example, when a National Patient Record Flag assignment occurs in VistA, the event will trigger an update patient information message.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/027.png) Category II flags are locally established by individual VISNs or facilities. They are not shared between facilities.

> Each PRF includes a narrative that describes the reason for the flag and may include some suggested actions for users to take when they encounter the patient. Other information displayed to the user includes the Flag Type, Flag Category, Assignment Status, Initial Assignment Date, Approved by, Next Review Date, Owner Site, and Originating Site. When assigning a flag, authorized users must write a progress note that clinically justifies each flag assignment action.

> Introduction

### Updated PRF Narratives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: Please note that values between “\<” and “\>” in the narratives are placeholders and will be replaced with an actual value at run time.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NARRATIVE</p>
</blockquote></th>
<th><blockquote>
<p>DESCRIPTION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Narrative Text For National PRF Assignment Created By Auto- Conversion</td>
<td><blockquote>
<p>This national PRF entry was auto-created on &lt;DT&gt;, by the 'Convert Local HRMH PRF to National' option, and run by</p>
<p>&lt;USER&gt;. The fields are based on the local PRF &lt;FLAG&gt; which was inactivated by the auto conversion.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Narrative For The Inactivated Local PRF Assignment History</td>
<td><blockquote>
<p>This local PRF entry was inactivated by the 'Convert Local HRMH PRF to National' option run on &lt;DT&gt; by &lt;USER&gt;. A new national HIGH RISK FOR SUICIDE PRF was created using the information in this local PRF entry.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Inactivated Local Assignment History Text For National Conversion At Another Site</td>
<td><blockquote>
<p>Since a national HIGH RISK FOR SUICIDE PRF entry has been activated by another site in VistA, this local PRF entry was inactivated by the 'Convert Local HRMH PRF to National' option, run on &lt;DT&gt; by &lt;USER&gt;.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Assignment History Narrative For New National PRF</td>
<td><blockquote>
<p>New assignment for national PRF entry auto-created on &lt;DT&gt;, by the 'Convert Local HRMH PRF to National' option.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Use of the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section of the PRF User Guide provides instructions for the end-Users to successfully use the software with little or no assistance. It also list and describes the menus/options with examples to implement and use the software.

## New Functionality:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DG\*5.3\*849 - DGPF New Category I Flag and Conversion Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The DG\*5.3\*849 DGPF NEW CAT I FLAG AND CONVERSION patch supports the Improve Veteran Mental Health (IVMH) Initiative \#5, High Risk Mental Health (HRMH) National Reminder & Flag. This patch implements the following new functionality:

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/028.png) National Patient Record Flag (PRF) for suicide prevention (HIGH RISK FOR SUICIDE) ![](high-risk-mental-health-patient-patient-record-flags-user-guide/029.png) Convert Local HRMH PRF to National \[DGPF LOCAL TO NATIONAL CONVERT\]

> Option

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/030.png) DGPF CLINICAL HR FLAG REVIEW mail group.

### New National Patient Record Flag (PRF) for Suicide Prevention (HIGH RISK FOR SUICIDE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this National Category I Patient Record Flag is to alert Veterans Health Administration (VHA) Mental Health staff regarding patients who have a high risk for suicide that may pose a threat to themselves.

> The process to generate the new National Patient Record Flag (PRF) for suicide prevention (HIGH RISK FOR SUICIDE) (Category I) from a local (Category II) Patient Record Flag (PRF) will take the existing, active, local PRFs for high risk for suicide and determine whether a national PRF can be created. If there is an issue with generating a national PRF, an error message will be logged, or the record will be flagged for manual action by appropriate staff. In this case no national PRF is created and the local PRF will remain intact.

> When creating the new national PRF, the information from the local PRF will be used in the new national PRF. Upon successful creation of the new national PRF, the local PRF will be inactivated with a comment indicating a new national PRF has been created.

> Upon creation of the new national PRF, the existing Health Level 7 (HL7) messaging functionality will be used to transmit the national PRF information to other known treating facilities as is currently done when a National PRF is created through the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option.

> The new national flag record entry (HIGH RISK FOR SUICIDE) is added in the PRF NATIONAL FLAG file (#26.15).

> Use of the Software

### New DGPF CLINICAL HR Flag Review Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DGPF CLINICAL HR FLAG REVIEW mail group receives reports generated by the Convert Local HRMH PRF \[DGPF LOCAL TO NATIONAL CONVERT\] to National option. This mail group will also receive messages when the patient’s flag needs to be reviewed, following existing PRF review processes of continue, inactivate or delete.

### New Convert Local HRMH PRF to National \[DGPF LOCAL TO NATIONAL CONVERT\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new Convert Local HRMH PRF to National \[DGPF LOCAL TO NATIONAL CONVERT\] option allows the generation of the national PRF from local, active high risk for suicide PRFs.

> This option can be run in either

> Report-only or

> Processing mode.

> When this new option runs in the report-only mode, reports will be generated and sent to the

> new DGPF CLINICAL HR FLAG REVIEW mail group. This report displays:

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/031.png)local PRFs that can be processed to a national flag local PRFs with potential errors needing corrections local PRFs required to be processed manually.

> When the option runs in the processing mode, the actual processing of local PRFs to national PRFs will take place.

Use of the Software

> Example: The new Convert Local HRMH PRF to National \[DGPF LOCAL TO NATIONAL CONVERT\] option

> CHOOSE 1-10: 7 DGPF LOCAL TO NATIONAL CONVERT Convert Local HRMH PRF to

> National Convert Local HRMH PRF to National

> This option can be run in a report only mode which will provide a report of what actions the local-to-national processing will perform. Enter 'R' to run the Report Only mode, or 'P' to begin the local-to-national PRF processing.

> Select one of the following:

> R Report Only

> P Process Local-to-National Select which mode to run: R// Report Only

> ...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

> \>\> Results have been sent to the 'DGPF CLINICAL HR FLAG' mail group\>

> CHOOSE 1-10: 7 DGPF LOCAL TO NATIONAL CONVERT Convert Local HRMH PRF to

> National

> Convert Local HRMH PRF to National

> This option can be run in a report only mode which will provide a report of what actions the local-to-national processing will perform. Enter 'R' to run the Report Only mode, or 'P' to begin the local-to-national PRF processing.

> Select one of the following: R Report Only

> P Process Local-to-National

> Select which mode to run: P// Process Local-to-National

> ...HMMM, JUST A MOMENT PLEASE...

> \>\> Results have been sent to the 'DGPF CLINICAL HR FLAG' mail group

> Use of the Software

## DG\*5.3\*836 Patch – HRMH - Vista Changes For National Reminder & Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1)  DG\*5.3\*836 implements two new Application Programming Interface (APIs) used by the (2) Scheduling and (3) Reminder patches to determine the High Risk for Suicide flag status on a specified date.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/032.png) The first API call point will return the multiple assignment statuses, if applicable, for a specified Flag Name during a specified patient and date range. The Assignment History should be returned for assignment statuses that overlap the specified date range.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/033.png) The second API will return the list of patients with the specific Patient Record Flag active within a specified date range.

2)  The scheduling patch includes two new scheduling reports that identify no-show “High Risk for Suicide” patients that missed their MH appointments.
3)  The Reminder patch includes a new national reminder and reminder dialog that will be used by providers to document results of following up with a high risk for suicide patient that missed a MH appointment and a health summary type with MH-specific supporting information.

> During the installation of this patch sites were provided the opportunity to update the Parameter Definition for the local Patient Record Flag related to High Risk for Suicide. The default value is “HIGH RISK FOR SUICIDE”, which sites were encouraged to use. The value of this parameter can be changed by sites using the following programmer utility:

> D UPD^DG53836P: This utility will prompt for a new value for the Parameter Definition.

Use of the Software

## Patient Record Flag Main Menu \[DGPF RECORD FLAG MAIN MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example: Patient Record Flag Main Menu options

### Patient Record Flag Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 30%" />
<col style="width: 23%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>ABBR</th>
<th>OPTION/MENU NAME</th>
<th>TECHNICAL NAME</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RM</td>
<td>Record Flag Reports Menu</td>
<td>[DGPF RECORD FLAG REPORTS MENU]</td>
<td>This menu contains patient record flag report functions.</td>
</tr>
<tr class="even">
<td>FA</td>
<td><p>Record Flag Assignment</p>
<p>Locked with DGPF ASSIGNMENT Security Key</p></td>
<td>[DGPF RECORD FLAG ASSIGNMENT]</td>
<td><p>This option provides a List Manager user interface for assigning Patient Record Flag(s) to patients.</p>
<p>Additionally, this option provides the ability to review and manage Patient Record Flag assignments.</p>
<p>The following actions are provided within the patient Record Flag Assignment option:</p>
<p>Assign a Patient Record Flag(s) to a patient.</p>
<p>Display the details of a patient's record flag assignments including the history of the assignment.</p>
<p>Review/Edit a patient's record flag assignment.</p>
<p>Change the site ownership of a patient's record flag assignment.</p></td>
</tr>
</tbody>
</table>

> Use of the Software

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 30%" />
<col style="width: 23%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>FM</th>
<th>Record Flag Management Locked with DGPF MANAGER Security Key</th>
<th>[DGPF RECORD FLAG MANAGEMENT]</th>
<th><p>This option will provide users with the ability to: Create Category II (Local) Patient Record Flags</p>
<p>Edit Category II (Local) Patient Record Flags</p>
<p>List Category I (National) and Category II (Local) Patient Record Flags Display details of Category I and Category II Patient Record Flag</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TM</td>
<td>Record Flag Transmission Mgmt. Locked with DGPF TRANSMISSIONS</td>
<td>[DGPF - TRANSMISSION MGMT]</td>
<td>This option acts as a submenu containing options available to manage patient record flag transmissions.</td>
</tr>
<tr class="even">
<td>ED</td>
<td><p>Record Flag Enable Divisions</p>
<p>Locked with DGPF MANAGER</p></td>
<td>[DGPF ENABLE DIVISIONS]</td>
<td><p>This option allows multi- divisional facilities to enable/disable individual medical center divisions stored in the MEDICAL CENTER DIVISION (#40.8)</p>
<p>file as Patient Record Flag assignment owners.</p>
<p>Disabling a medical center division will only be allowed if there are no active Patient Record Flag assignments associated with the division.</p></td>
</tr>
</tbody>
</table>

Use of the Software

### RM - Record Flag Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| MENU ITEM                                                                     | DESCRIPTION                                                                                                                                                                                   |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Assignment Action Not Linked Report \[DGPF ACTION NOT LINKED REPORT\]         | This option is used to display PRF assignment history actions that are not linked to a TIU progress note for a specified date range.                                                          |
| Flag Assignment Report \[DGPF FLAG ASSIGNMENT REPORT\]                        | This option is used to display all of the patient assignments for Category I flags, Category II flags, or both by date range.                                                                 |
| Patient Assignments Report \[DGPF PATIENT ASSIGNMENT REPORT\]                 | This option is used to display all of the patient record flag assignments for a particular patient.                                                                                           |
| Assignments Due for Review Report \[DGPF ASSINMENT DUE REVIEW RPT\]           | This option is used to display all of the patient assignments for Category I flags, Category II flags, or both that are due for review within a selected date range.                          |
| Assignments Approved By Report \[DGPF APPROVED BY REPORT\]                    | This option is used to display all of the PRF assignment history actions for a single individual or all individuals who approved the assignment of patient record flags.                      |
| Assignments by Principal Investigator Report \[DGPF PRINCIPAL INVEST REPORT\] | This option is used to display all of the PRF assignment history actions for a single principal investigator or all principal investigators for a specified date range (research flags only). |

> Use of the Software

### FA - Record Flag Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| MENU ITEM                        | DESCRIPTION                                                                                                                                                                                                                                   |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SP - Select Patient              | Information provided on the selected patient includes social security number, Internal Control Number (ICN); Coordinating Master of Record (CMOR) site (site that is the authoritative source for the demographic fields); and date of birth. |
| DA - Display Assignment Details  | The "Approved By" field will display "Chief of Staff" if the site does not have ownership of the flag assignment.                                                                                                                             |
| AF - Assign Flag                 | This action is used to assign a flag to a patient.                                                                                                                                                                                            |
| EF - Edit Flag Assignment        | This action is used to continue a flag assignment, inactivate the assignment, or to designate that the assignment was entered in error.                                                                                                       |
| CO - Change Assignment Ownership | This action is used to change the ownership of a record flag assignment                                                                                                                                                                       |

### FM - Record Flag Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| MENU ITEM                | DESCRIPTION                                                                                                                                              |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| CC - Change Category     | The Category I flags are displayed on the screen when the option opens.                                                                                  |
| CS - Change Sort         | This action allows users to sort the flag list by flag name (alphabetically) or flag type.                                                               |
| DF - Display Flag Detail | This action is used to display information about the selected flag such as flag name, type, category, status, TIU Progress Note Title, description, etc. |
| AF - Add New Record Flag | This action allows the entry of a new Category II (local) patient record flag.                                                                           |
| EF - Edit Record Flag.   | This action allows editing of the fields associated with a Category II (local) patient record flag                                                       |

Use of the Software

### TM - Record Flag Transmission MGMT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>MENU ITEM</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Record Flag Transmission Errors [DGPF TRANSMISSION ERRORS]</td>
<td>This option provides the means to review rejected PRF HL7 update messages and retransmit them.</td>
</tr>
<tr class="even">
<td><p>Record Flag Manual Query</p>
<p>[DGPF MANUAL QUERY]</p></td>
<td>This option allows a user to query a selected treating facility for existing Category I Patient Record Flag (PRF) assignments for a selected patient.</td>
</tr>
</tbody>
</table>

### ED - Record Flag Enable Divisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| MENU ITEM                                              | DESCRIPTION                                                                                                                                                  |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Record Flag Enable Divisions \[DGPF ENABLE DIVISIONS\] | This option gives multi-divisional facilities the ability to enable/disable medical center divisions as a PRF owner site. Divisions are disabled by default. |

> Use of the Software

## Record Flag Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Assignment Action Not Linked Report \[DGPF ACTION NOT LINKED REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to display PRF assignment history actions that are not linked to a TIU progress note for a specified date range. The report can be printed for Category I flags, Category II flags, or both.

> Example: Assignment Action Not Linked To A Progress Note Report

| PATIENT        |     | SSN       |     | FLAG | NAME  |     | ACTION         |     | ACTION DATE |
|----------------|-----|-----------|-----|------|-------|-----|----------------|-----|-------------|
| ADTPATIENT,ONE |     | 666880015 |     | APEX | STUDY |     | NEW ASSIGNMENT |     | 06/29/05    |
|                |     |           |     |      |       |     | CONTINUE       |     | 07/29/05    |
|                |     |           |     |      |       |     | CONTINUE       |     | 08/29/05    |
|                |     |           |     |      |       |     | CONTINUE       |     | 09/29/05    |
| ADTPATIENT,TWO |     | 666769873 |     | APEX | STUDY |     | NEW ASSIGNMENT |     | 10/13/05    |

Use of the Software

### Flag Assignment Report \[DGPF FLAG ASSIGNMENT REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to display all of the patient assignments for Category I flags, Category II flags, or both by date range. If a single category is chosen, the user may further choose to display the assignment report for a single flag or all flags of that category.

> Information provided on the display for each flag includes patient name, social security number, date flag assigned; flag review date, flag status (active or inactive) and ownership site.

> If Category I and II flags are selected to print, the total assignments for each category will be displayed as well as the combined total number of assignments.

> Example: Flag Assignment Report

> Use of the Software

### Patient Assignments Report \[DGPF PATIENT ASSIGNMENT REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to display all of the patient record flag assignments for a particular patient. The report may be printed for active flags, inactive flags, or both.

> Example: Patient Assignments Report

<table style="width:100%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 6%" />
<col style="width: 27%" />
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p>PATIENT RECORD FLAG</p>
<p>PATIENT ASSIGNMENTS REPORT Page: 1</p>
<p>Report Selected: Both (ACTIVE &amp; INACTIVE) Printed: Oct 15, 2005@11:29</p>
<p>Patient: ADTPATIENT,ONE 666-01-0122</p>
<p>FLAG NAME CATEGORY APPROVED BY ENTERED REVIEW DT STATUS OWNING SITE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>BEHAVIORAL</p>
</blockquote></td>
<td><blockquote>
<p>I</p>
</blockquote></td>
<td><blockquote>
<p>APPROVER,ON 11/12/0</p>
</blockquote></td>
<td><blockquote>
<p>11/11/06</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p>MASTER PATI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APEX STUDY</p>
</blockquote></td>
<td><blockquote>
<p>II</p>
</blockquote></td>
<td><blockquote>
<p>APPROVER,TWO 03/26/05</p>
</blockquote></td>
<td><blockquote>
<p>04/25/07</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p>ALBANY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>&lt;End of Report&gt;</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Use of the Software

### Assignments Due for Review Report \[DGPF ASSIGNMENT DUE REVIEW RPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to display all of the patient assignments for Category I flags, Category II flags, or both that are due for review within a selected date range. If a single category is chosen, the report may be displayed for a single flag or all flags of that category.

> Information provided on the display for each flag includes patient name, social security number, date flag assigned, flag review date, and whether or not the review notification mail message has been sent. Reviews that are past due are signified by an asterisk (\*) next to the date in the Review Date column.

> If both Category I and II flags are selected, the total number of assignments for review for each category will be displayed as well as the combined total number of assignments for review.

> Example: Assignments Due For Review Report

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 4%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>ADTPATIENT,ONE</th>
<th></th>
<th>666456789</th>
<th></th>
<th>05/05/05</th>
<th></th>
<th>05/15/06</th>
<th></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADTPATIENT,TWO</td>
<td></td>
<td>000990909</td>
<td></td>
<td>04/17/05</td>
<td></td>
<td>04/16/06</td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Use of the Software

> <span id="Assignments_Approved_By_Report_[DGPF_APP" class="anchor"></span>Assignments Approved By Report \[DGPF APPROVED BY REPORT\] This option is used to display all of the PRF assignment history actions for a single individual or all individuals who approved the assignment of patient record flags. The report may be printed

> for Cat I flags, Cat II flags, or both; active flags, inactive flags, or both.

> Example: Assignments Approved By Report.

> PATIENT RECORD FLAG

> ASSIGNMENTS APPROVED BY REPORT Page: 1

> Date Range: 06/01/05 to 10/15/05 Printed: Oct 15, 2005@11:09

> Approved By: ADTPROVIDER,ONE

> Flag Name: BEHAVIORAL - Category I (National)

> PATIENT SSN ACTION ACTION DT REVIEW DT STATUS

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>================ ========== =============</th>
<th>=========</th>
<th><blockquote>
<p>=========</p>
</blockquote></th>
<th><blockquote>
<p>=========</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADTPATIENT,ONE 666120565 NEW ASSIGNMENT</td>
<td>07/23/05</td>
<td><blockquote>
<p>07/23/07</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ADTPATIENT,TWO 666769873 NEW ASSIGNMENT</td>
<td>08/11/05</td>
<td><blockquote>
<p>08/11/07</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Approved By: ADTPROVIDER,TWO

> Flag Name: BOB1 TEST LOCAL FLAG - Category II (Local)

> PATIENT SSN ACTION ACTION DT REVIEW DT STATUS

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><p>================ ========== =============</p>
<p>ADTPATIENT,TEN 666880015 NEW ASSIGNMENT</p></th>
<th><p>=========</p>
<p>09/29/05</p></th>
<th><blockquote>
<p>=========</p>
<p>10/09/05</p>
</blockquote></th>
<th><blockquote>
<p>=========</p>
<p>ACTIVE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CONTINUE</td>
<td>09/29/05</td>
<td>10/09/05</td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CONTINUE</td>
<td>09/29/05</td>
<td>10/09/05</td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Approved By: ADTPROVIDER,TWO

> Flag Name: BOB1 TEST LOCAL FLAG - Category II (Local)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>PATIENT</th>
<th><blockquote>
<p>SSN</p>
</blockquote></th>
<th><blockquote>
<p>ACTION</p>
</blockquote></th>
<th><blockquote>
<p>ACTION DT</p>
</blockquote></th>
<th><blockquote>
<p>REVIEW DT</p>
</blockquote></th>
<th><blockquote>
<p>STATUS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>================</td>
<td><blockquote>
<p>==========</p>
</blockquote></td>
<td><blockquote>
<p>=============</p>
</blockquote></td>
<td><blockquote>
<p>=========</p>
</blockquote></td>
<td><blockquote>
<p>=========</p>
</blockquote></td>
<td><blockquote>
<p>=========</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ADTPATIENT,TEN</td>
<td><blockquote>
<p>666880015</p>
</blockquote></td>
<td><blockquote>
<p>CONTINUE</p>
</blockquote></td>
<td><blockquote>
<p>09/29/05</p>
</blockquote></td>
<td><blockquote>
<p>10/09/05</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>CONTINUE</p>
</blockquote></td>
<td><blockquote>
<p>09/29/05</p>
</blockquote></td>
<td><blockquote>
<p>10/09/05</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Flag Name: BOBS TIU TEST FLAG - Category II (Local)

> PATIENT SSN ACTION ACTION DT REVIEW DT STATUS

> ================ ========== ============= ========= ========= ========= ADTPATIENT,TWO 666769873 NEW ASSIGNMENT 08/11/05 08/11/07 ACTIVE

> \<End of Report\>

Use of the Software

### Assignments by Principal Investigator Report \[DGPF PRINCIPAL INVEST REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to display all of the PRF assignment history actions for a single principal investigator or all principal investigators for a specified date range. The user may choose to print the report for active flags, inactive flags, or both.

> Investigators are associated with research type flags. For each flag listed on the report, all principal investigator names for that flag are displayed.

> Example: Assignments By Principal Investigator Report.

> Use of the Software

## Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Record Flag Assignment option is used to assign a flag(s) to a patient and to maintain those assignments.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/034.png)The "Review Date" field will display "N/A" (not applicable) when any of the following conditions exist:

> The most recent update to the PRF assignment was received from a remote system. The current PRF assignment status is Inactive.

> All PRF Record Flags assigned to a patient must be linked to a TIU Progress Note Title or the user will be unable to proceed with this option.

> DGPF ASSIGNMENT security key is required for access to this option.

> This option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows users to select items from the list and perform specific actions against those items. A description of each action in this option is provided below.

> Example: Record Flag Assignment

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Flag</p>
</blockquote></th>
<th><blockquote>
<p>Assigned</p>
</blockquote></th>
<th><blockquote>
<p>Review Date</p>
</blockquote></th>
<th><blockquote>
<p>Active Local</p>
</blockquote></th>
<th><blockquote>
<p>Owner Site</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 SUICIDE RISK</td>
<td><blockquote>
<p>08/01/12</p>
</blockquote></td>
<td><blockquote>
<p>10/30/12</p>
</blockquote></td>
<td><blockquote>
<p>YES YES</p>
</blockquote></td>
<td><blockquote>
<p>NORTHPORT VAMC</p>
</blockquote></td>
</tr>
</tbody>
</table>

Use of the Software

### SP - Select Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Information provided on the selected patient includes social security number, Internal Control Number (ICN); Coordinating Master of Record (CMOR) site (site that is the authoritative source for the demographic fields); and date of birth. Flag assigned to the patient will be listed with the following data elements.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/035.png) Flag Name

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/036.png) Assigned - Date flag was assigned.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/037.png) Review Date - Date flag will be up for review. ![](high-risk-mental-health-patient-patient-record-flags-user-guide/038.png) Active - Is the flag active? Yes or No.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/039.png) Local - Is the flag local? Yes or No.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/040.png) Owner Site - Site that has ownership of the flag.

### DA - Display Assignment Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This action is used to display the following information on a selected flag assignment.

> The "Approved By" field will display "Chief of Staff" if the site does not have ownership of the flag assignment. The Progress Note field will only be displayed if the site has assignment ownership.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/041.png) Flag Name ![](high-risk-mental-health-patient-patient-record-flags-user-guide/042.png) Flag Type

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/043.png) Flag Category

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/044.png) Assignment Status

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/045.png) Date of Initial Assignment ![](high-risk-mental-health-patient-patient-record-flags-user-guide/046.png) Last Review Date

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/047.png) Next Review Date ![](high-risk-mental-health-patient-patient-record-flags-user-guide/048.png) Owner Site

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/049.png) Originating Site

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/050.png) Flag Assignment Narrative ![](high-risk-mental-health-patient-patient-record-flags-user-guide/051.png) Flag Assignment History

- Action
- Action Date
- Entered By
- Approved By
- Progress Note

> Use of the Software

- Action Comments

### AF - Assign Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This action is used to assign a flag to a patient. Assigning a flag consists of entering the following fields. After completion, the data will be displayed for review before filing.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/052.png) Name of the flag (to see a list of the available flag names enter L.? for local flag and N.? for national flag)

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/053.png) Owner Site

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/054.png) Name of the individual who approved the assignment ![](high-risk-mental-health-patient-patient-record-flags-user-guide/055.png) Narrative text (reason) for the assignment

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/056.png) Review Date

### EF - Edit Flag Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This action is used to continue a flag assignment, inactivate the assignment, or to designate that the assignment was entered in error. It can also be used to update the assignment narrative. The reason must be entered for editing the assignment. Note: Category I flag assignments may only be edited by the owner site.

### CO - Change Assignment Ownership

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This action is used to change the ownership of a record flag assignment. The ownership of Category I flags may be changed to any of the patient’s treating facilities and to any of the divisions enabled for ownership at multi-divisional sites. The ownership of Category II flags may be changed to any of the divisions enabled for ownership at multi-divisional sites. This action would be taken if the patient changed his primary VA care site or special circumstances arose that warranted the transfer of the flag.

Use of the Software

## Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Record Flag Management option is used to create and maintain Category II patient record flags. It can also be used to display a list of Category I and II flags including the details of each.

> DGPF MANAGER Security key is required for access to this option.

> This option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows items to be selected from the list and perform specific actions against those items. A description of each action in this option is provided below.

> Example: Record Flag Management

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 32%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Flag Name</p>
</blockquote></th>
<th><blockquote>
<p>Flag Type</p>
</blockquote></th>
<th><blockquote>
<p>Flag Status</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 CANCER PROTOCOL</td>
<td><blockquote>
<p>RESEARCH</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2 DRUG SEEKING BEHAVIOR</td>
<td><blockquote>
<p>BEHAVIORAL</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3 INFECTIOUS DISEASE</td>
<td><blockquote>
<p>CLINICAL</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
</tr>
</tbody>
</table>

### CC - Change Category

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Category I flags are displayed on the screen when the option opens. Currently there are two National Category I Flags, Behavioral and High Risk for Suicide. This action allows users to change the category of the flag list being viewed.

### CS - Change Sort

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The flag list can be sorted alphabetically or by type of flag. Flag types are distributed with the software and cannot be added to or edited.

### DF - Display Flag Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This action is used to display information about the selected flag such as flag name, type, category, status, TIU Progress Note Title, description, etc. The enter/edit history of the flag is a part of this display.

> Use of the Software

### AF - Add New Record Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This action allows the entry of a new Category II (local) patient record flag. Entering a new flag consists of completing the following fields.

| FIELD                   | DESCRIPTION                                                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Record Flag Name        | Locally assigned name of the flag.                                                                                                                                                                                    |
| Status of the Flag      | Active or Inactive                                                                                                                                                                                                    |
| Type of Flag            | Clinical, Research, etc. Entries are distributed with the software.                                                                                                                                                   |
| Principal Investigator  | This prompt will only appear if the flag type is RESEARCH. Enter the investigator(s) associated with this research flag.                                                                                              |
| Review Frequency Days   | Number of days that may elapse between reviews of this flag assignment. Flags must be reviewed at least every two years. A value of zero indicates that NO automatic review will occur.                               |
| Notification Days       | Number of days prior to this flag assignment's review date that a notification is sent to the review group. A value of zero indicates that NO prior notification is required.                                         |
| Review Mail Group       | Name of the mail group that will receive notification that this flag assignment is due for review. Mail group name must begin with DGPF. It is further recommended that locally-defined mail groups begin with DGPFZ. |
| Progress Note Title     | Name of TIU Progress Note linked with the flag.                                                                                                                                                                       |
| Description of the Flag | A brief description of this patient record flag.                                                                                                                                                                      |

### EF - Edit Record Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This action allows editing of the fields associated with a Category II (local) patient record flag. The reason for editing the flag must be entered. If the STATUS field is changed from ACTIVE to INACTIVE, all patient record flag assignments associated with this flag will be inactivated.

Use of the Software

## Record Flag Transmission Mgmt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Record Flag Transmission Errors \[DGPF TRANSMISSION ERRORS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option provides the means to review rejected PRF HL7 update messages and retransmit them. The list may be sorted by patient name or date/time message received.

> The view message action will display details of the selected message. Data items may include error received date/time, message control ID, flag name, owner site, assignment transmitted to, assignment transmission date/time, and rejection reasons.

> The retransmit message action will retransmit all of the patient’s PRF assignment and history records to the site where the rejection message occurred.

> DGPF TRANSMISSIONS security key is required for access to this option.

> NOTE: The Record Flag Transmission Mgmt \[DGPF TRANSMISSION MGMT\] option and DGPF TRANSMISSIONS security key should only be assigned to a very few staff members at each site.

> Example: Transmission Errors Screen.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 23%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Patient Name</p>
</blockquote></th>
<th><blockquote>
<p>SSN</p>
</blockquote></th>
<th>Received</th>
<th><blockquote>
<p>Transmitted To</p>
</blockquote></th>
<th><blockquote>
<p>Owner Site</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1. ADTPATIENT, ONE</td>
<td><blockquote>
<p>2323</p>
</blockquote></td>
<td>12/03/04</td>
<td><blockquote>
<p>PORTLAND.VA.GOV</p>
</blockquote></td>
<td><blockquote>
<p>DEVVPP.F0-ALBA</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2. ADTPATIENT, TWO</td>
<td><blockquote>
<p>0565</p>
</blockquote></td>
<td>09/20/04</td>
<td><blockquote>
<p>PALO ALTO. VA.</p>
</blockquote></td>
<td><blockquote>
<p>GOV ZZ ALBANY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3. ADTPATIENT, SIX</td>
<td><blockquote>
<p>0888</p>
</blockquote></td>
<td>07/23/04</td>
<td><blockquote>
<p>DEVVPP.F0-ALBA</p>
</blockquote></td>
<td><blockquote>
<p>ZZ ALBANY</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4. ADTPATIENT, TEN</td>
<td><blockquote>
<p>4811</p>
</blockquote></td>
<td>03/29/05</td>
<td><blockquote>
<p>ZZ ALBANY</p>
</blockquote></td>
<td><blockquote>
<p>DEVVPP.F0-ALBA</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Use of the Software

### Record Flag Manual Query \[DGPF MANUAL QUERY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows a user to query a selected treating facility for existing Category I Patient Record Flag (PRF) assignments for a selected patient.

> The option displays a list of all Category I PRF assignments found at the queried treating facility. The query result details for a selected assignment can be displayed. Any Category I PRF assignment returned by the query that does not already exist at the facility is automatically added. If active flag assignments already exist at the requesting facility for the selected patient, they are displayed. The flag details for each flag may be viewed before sending the query.

> Example: This message is displayed when the Record Flag Manual Query \[DGPF MANUAL QUERY\] option successfully returns and files a PRF assignment that was missing at the requesting facility.

> Example: If no Category I flag assignments are found in the queried treating facility database for the selected patient, the following message is displayed.

> Example: The following message is displayed when the HL7 software has a problem communicating between the two facilities.

> Example: Record Flag Manual Query Results Screen

Use of the Software

## Record Flag Enable Divisions \[DGPF ENABLE DIVISIONS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option gives multi-divisional facilities the ability to enable/disable medical center divisions as a PRF owner site. Divisions are disabled by default.

> Once a division has been enabled, disabling it will only be allowed if there are no active assignments associated with that division.

> Users may choose to view a list of medical center divisions for the site. Data items displayed may include medical center division, PRF assignment ownership (enabled/disabled), edited by, edit date/time, and active PRF assignments (Yes/No).

> DGPF MANAGER Security key is required for access to this option.

> Use of the Software

# Additional Patient Record Flag Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PRF Display on Patient Look-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is an example of the patient record flag assignment information displayed on patient look-up for those patients with flag assignments. Category I flags will be listed first with the Category designation (Cat I or II) displayed. It is strongly recommended the user answer YES to viewing the active patient record flag details, especially for Category I (behavioral and / or High Risk for Suicide) and then review the detailed information that is possibly critical to patient and employee safety.

> Example: PRF Assignment Information on Patient Lookup

> Select Registration Menu Option: Load/Edit Patient Data

> Select PATIENT NAME: adtpatient, one ADTPATIENT,ONE 2-3-20 000456789

> 1 YES NSC VETERAN

> \>\>\> Active Patient Record Flag(s):

> \<BEHAVIORAL\> CATEGORY I

> Do you wish to view active patient record flag details? YES// \<RET\> Patient Record Flag Jun 05, 2003@07:22:55 Page: 1 of 4 Patient: ADTPATIENT, ONE (000456789) DOB: 02/03/20

> ICN: 5000000003V639492 CMOR: 1ALBANY

> \<\<\< Active Patient Record Flag Assignments \>\>\>

1.  Flag Name: \<BEHAVIORAL\> Category: I (NATIONAL)

> Type: BEHAVIORAL

> Assignment Narrative:

> On 4/8/03, this veteran was disruptive and threatening toward numerous staff. RECOMMEND: VA Police should be immediately called to standby until they and the clinician decide that standby is no longer necessary.

> Assignment Details:

> Initial Assignment: May 20, 2003 Approved By: ADTAPPROVER, ONE

> Next Review Date: May 20, 2005

> Owner Site: ALBANY VAMC (UPSTATE NEW YORK HCS)

> Originating Site: EL PASO VA HCS (EL PASO VA HCS) Progress Note Linked: No

> \+ Enter?? for more actions

> Select Action: Quit//

Use of the Software

## Patient Record Flag in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient Record Flags (PRF) are advisories that authorized users place on a patient’s chart to improve employee safety and the efficient delivery of health care. Each advisory or flag includes a narrative that describes the reason for the flag and may include some suggested actions for users to take when they encounter the patient. Other information displayed to the user includes the Flag Type, Flag Category, Assignment Status, Initial Assignment Date, Approved by, Next Review Date, Owner Site, and Originating Site. When assigning a flag, authorized users must write a progress note that clinically justifies each flag assignment action.

> Flags are defined in the PRF List Manager software either through a patch or by an authorized user. Once the flag definition exists, authorized users can use the following actions in the PRF software to assign and maintain the flag on a specific patient’s record: new assignment, continue, inactivate, mark as entered in error, and reactivate.

## Creating, Assigning, and Maintaining PRF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Some sites may have two different groups of users who work with Patient Record Flags: ![](high-risk-mental-health-patient-patient-record-flags-user-guide/057.png) administrative users who create, maintain, and assign flags

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/058.png) Clinical users that document why the flag was placed on the patient’s record.

> Authorized users can define Category II flags and edit their definitions. They assign and maintain the flag(s) on a patient’s record using the assignment actions in the PRF software through the List Manager interface: new assignment, continue, inactivate, mark as entered in error, and reactivate.

> When a PRF is removed a note explaining why it is being removed must be added. In practice, it is best to have the note thought through and written when the flag is removed.

## Documenting PRF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> With CPRS GUI v.26, each Patient Record Flag action (new assignment, continue, inactivate, reactivate, or mark as entered in error) must have a linked progress note that clinically justifies any action taken. Previously, each flag needed to have a progress note, but there was no link between the note and the flag action. Now when the user writes a PRF progress note, the user must link the note to a flag action. The note might also contain references to supporting documentation.

> In each flag definition, the user must select the previously created PRF progress note title that will document the reasons for any flag action. This is referred to as associating a progress note title with a PRF. Before a title can be associated with a PRF, the title must be created either by a patch for a national flag or by someone at the site for a local flag.

> For example, if a user were defining a Wandering flag in the PRF List Manager software, someone at the site must have already used TIU to create the appropriate note title in the correct document class. Then, the user defining the flag would associate a title such as, Patient Record Flag Category II – Risk, Wandering, by selecting that title from the list of available PRF progress note titles.

> Use of the Software

> Once the flag and the progress note title are associated, when the user writing a new progress note selects a PRF progress note title, CPRS displays the flag actions on the selected patient and whether each action has been linked to PRF progress note (Yes or No). For the new PRF note, the user then selects the available flag action to create the link between the note and the flag action.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SYMBOL</p>
</blockquote></th>
<th><blockquote>
<p>DESCRIPTION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](high-risk-mental-health-patient-patient-record-flags-user-guide/059.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>NOTE/REF:</strong> There is a one-to-one correspondence between flag actions and progress notes. Each PRF action for a patient can only be linked to one progress note; each progress note can only be linked to one flag action.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Prerequisites to Writing PRF Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before users can write progress notes that document PRF’s, PRF progress note titles must be set up correctly. Each PRF progress note title must be associated with a specific flag definition, and users must be assigned to the appropriate user classes to write specific kinds of notes. Also, someone must have assigned the flag to the patient.

> For users to write a progress note and correctly link the note to a flag action, sites must complete the following set up:

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/060.png) To write a PRF note for a Category I flag, the user must belong to the DGPF PATIENT RECORD FLAG MGR user class. Each site will be responsible for populating this user class.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/061.png) Because Category II Patient Record Flags are local, each site must determine if the site will create a user class and business rules to govern which users can write Category II PRF progress notes.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/062.png) The PRF note titles should follow the naming conventions described in the directive and be descriptive enough that users can tell which note title corresponds to which flag.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/063.png) The flag definition must contain the progress note title that documents actions for that flag - each PRF note title can only be associated with one flag.

> Category II PRF progress note titles must be in the Patient Record Flag Cat II document class under the Progress Notes document class to allow users to associate them with a PRF Category II definition. If the titles are not in this document class, they will not display when the user attempts to associate the title with a PRF Category II flag nor will CPRS get the information about which flag actions are linked. Progress note titles for Category I patient record flags are defined and associated by national patch.

Use of the Software

## PRF Note Titles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Currently, there are two Category I flags: Behavioral and High Risk for Suicide. The Progress Note titles for the two flags are:

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/064.png) Patient Record Flag Category I (for the Behavioral flag) ![](high-risk-mental-health-patient-patient-record-flags-user-guide/065.png) Patient Record Flag Category I – High Risk for Suicide

> To help sites that will be creating local Category II flags, four partially customizable Progress Note titles have been distributed:

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/066.png) Patient Record Flag Category II – Risk, Fall

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/067.png) Patient Record Flag Category II – Risk, Wandering ![](high-risk-mental-health-patient-patient-record-flags-user-guide/068.png) Patient Record Flag Category II – Research Study ![](high-risk-mental-health-patient-patient-record-flags-user-guide/069.png) Patient Record Flag Category II – Infectious Disease

> Clinical Application Coordinators (CACs) can customize these Category II titles by changing the text after the dash using TIU utilities. For example, the first title could be changed from “Patient Record Flag Category II – Risk, Fall” to “Patient Record Flag Category II – Behavioral, Drug Seeking” or other titles sites create.

> CACs can also create their own titles, but the title must follow the naming convention “Patient Record Flag Category II – *other text*” where *other text* is the text specific to the local note title.

## Linking PRF Notes to Flag Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the CPRS GUI, users must link a PRF progress note to a flag action when the user writes a PRF note. This linking can also be done through the List Manager interface using TIU options. In the CPRS GUI’s Progress Note Properties dialog, when a user selects a Patient Record Flag progress note title, CPRS displays a list of flag actions to which the note can be linked at the bottom of the dialog. This list shows all the actions for the flag and whether each action has been linked.

> Use of the Software

![](high-risk-mental-health-patient-patient-record-flags-user-guide/070.png)

> For progress note titles that document the justification for a patient record flag, users will be able to link the progress note to the specific flag action they are documenting. The example shown here is of a Category I PRF progress note and the Continue action to which the user would choose to link.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SYMBOL</p>
</blockquote></th>
<th><blockquote>
<p>DESCRIPTION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](high-risk-mental-health-patient-patient-record-flags-user-guide/071.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>NOTE</strong>: For PRF notes, users must select a flag action to link the note to before they can write the note—the same way users link a note with a consult. CPRS will not allow the user to write the note unless an unused flag action is selected. If the user does not select a flag action, CPRS displays a dialog that states, “Notes of this title require the selection of a patient record flag action”.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> When the user selects a PRF progress note title, CPRS displays this list of note actions only if sites have done the correct set-up as described earlier. The user must then pick the action (new assignment, inactivate, reactivate, continue, or entered in error) that the note is documenting.

> If a user is viewing a note and wants to see to which PRF action the note is linked, the user can select View \| Details on the Notes tab. The details include the flag name, the date, and the action that was linked.

> If a user writing a new progress note chooses a PRF progress note but CPRS does not display any flag actions for linking, one of the following has probably occurred:

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/072.png)The flag has not been assigned to this patient yet.

Use of the Software

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/073.png) The user has selected the wrong progress note title for the flag.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/074.png)If it is a Category I flag, the site may not own the flag.

## Marking PRF as Entered in Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Marking PRF as entered in error terminates the flag’s display in the patient’s record. However, if there was a progress note linked to the flag, the progress note is still in the patient’s record. If the flag was entered in error, an authorized TIU user should retract or retract and reassign the linked progress note.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SYMBOL</p>
</blockquote></th>
<th><blockquote>
<p>DESCRIPTION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](high-risk-mental-health-patient-patient-record-flags-user-guide/075.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>NOTE</strong>: Users should be aware that although the flag does not display, a history of this flag is kept in the Patient Record Flag software and users can reactivate the flag. To prevent users from entering notes on previous, inaccurate PRF actions, all previous PRF actions are hidden when a flag is marked as entered in error.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Viewing PRF in CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient Record Flags are displayed in the applications that use the patient look up, including the CPRS GUI. In the CPRS GUI, there are three places where users can see if a patient has PRF:

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/076.png) The Patient Record Flag pop-up box ![](high-risk-mental-health-patient-patient-record-flags-user-guide/077.png) The CPRS Cover Sheet

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/078.png) The Flag button (available from any tab)

> When the user selects a patient name, CPRS begins to load the record, displays any relevant

> messages (“means test required”, deceased patient, sensitive record, etc.), and then, if the record is flagged, displays a pop-up box with the flag titles for the selected patient to ensure that the user sees the flag. The pop-up box is shown below.

> The Patient Record Flag pop-up box displays a list of all flags for the patient, with the first flag in the list highlighted and the narrative for that flag displayed below the flag list and a list of links to notes that have been linked to flag actions. Category I flags are displayed first, followed by any Category II (or local) flags.

> Use of the Software

> The flag narrative is the text the person assigning the flag enters that they want the user to see. It should give the purpose of the flag and may also contain examples of past behavior and instructions for users to follow when encountering the patient. For example, the narrative for a particular Behavioral flag might state that a patient has been known to carry weapons and has verbally threatened VHA staff in the past. It may also recommend that users call the VA police if this patient comes in for care. However, Patient Record Flags are not intended to stigmatize nor discriminate, rather it is to protect VHA staff and patients to ensure the efficient delivery of health care.

> On the bottom of the Patient Record Flag popup box, CPRS displays a list of notes that are linked to specific flag actions. Links will only display for those notes that have been signed and linked to a flag action. When the user selects a link, CPRS displays the linked progress note for the action in a detailed display window.

> Users can review the flag or close the box.

> When the user is viewing a patient’s record, the Patient Record Flags can be viewed on the Cover Sheet or the Flag button. On the CPRS Cover Sheet, a new box called Patient Record Flags has been added above the Postings area. Flags for the selected patient are listed in the box.

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/079.png)The Flag button is visible from all CPRS tabs. The Flag button will be red if any Patient Record Flags are assigned. If no Flags are assigned the Flag button is grayed out. The Cover Sheet and Flag button are shown in the graphic below.

> This screen capture shows the red text on the Flag button indicating this patient’s record has PRF(s) and shows the flag list on the CPRS Cover Sheet.

> To View a Patient Record Flag when entering a Record, use the following steps:

1.  Select a patient from the Patient Selection screen by either double-clicking on a patient name or highlighting the name and pressing the \<Enter\> key.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SYMBOL</p>
</blockquote></th>
<th><blockquote>
<p>DESCRIPTION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](high-risk-mental-health-patient-patient-record-flags-user-guide/080.png)</p>
</blockquote></td>
<td><blockquote>
<p>NOTE: When the record loads, CPRS checks to see if the record is sensitive and displays a warning to the user that the user must acknowledge to proceed. Then, if the record has one or more flag, CPRS displays a pop-up box with the patient’s record flag title. The first flag is highlighted and the narrative details displayed below. If CPRS displays the pop-up box, the user must close this box before CPRS will load the patient chart.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Use of the Software

2.  ![](high-risk-mental-health-patient-patient-record-flags-user-guide/081.png)Then, select the Flag title to view the narrative by clicking the flag name or highlighting the flag name with the tab and arrow keys and pressing \<Tab\> (note that the number of flag in each category is listed after the category label).

> This graphic shows the Patient Record Flag pop-up box listing the patient’s flag(s), the narrative for the highlighted flag, and the links to any signed, linked progress notes documenting the reasons for the flag(s). Using the Flag button or clicking on a flag title on the Cover Sheet also displays this pop-up box. Category I flags are in the orange field, they blink, and the text changes color from white to black and back. Category II flags are in the field below.

> To view the linked progress note, select the appropriate link in the lower part of the dialog. When finished, select Close.

> When finished viewing the narrative, close the narrative box by choosing Close or pressing

> \<Enter\>.

> To View A Patient Record Flag When Already Viewing A Record, Use The Following Steps:

> Use of the Software

> Go the Cover Sheet by clicking the Cover Sheet tab or pressing Ctrl + S or use the Flag button by clicking Flag or pressing tab until the Flag button is highlighted and press \<Enter\>.

> Select the flag title to see the narrative details by clicking the title or using the Up and Down arrows to highlight the name and pressing \<Enter\>.

> When finished, close the box by clicking Close or pressing \<Enter\>.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>TERM</p>
</blockquote></th>
<th><blockquote>
<p>DEFINITION</p>
</blockquote></th>
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
<td>DBIA</td>
<td>Database Integration Agreement</td>
</tr>
<tr class="odd">
<td>DRG</td>
<td>Diagnostic Related Group</td>
</tr>
</tbody>
</table>
> Glossary
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>GMTS</th>
<th>Health Summary namespace</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GUI</td>
<td>Graphic User Interface</td>
</tr>
<tr class="even">
<td>HL7</td>
<td>Health Level Seven</td>
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
<td>MENTAL HEALTH TREATMENT COORDINATOR (MHTC)</td>
<td><p>The liaison between the patient and the mental health system at a VA site. There is only one Mental Health treatment coordinator per patient and they are the key coordinator for behavioral health services care.</p>
<p>For more information about the MH treatment coordinator’s responsibilities, see VHA Handbook 1160.1, “Uniform Mental Health Services in VA Medical Centers for Clinics,” page 3-4. Note: In the handbook, the MHTC is called the Principal Mental Health Provider.</p></td>
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
<td>MHTC</td>
<td>Mental Health Treatment Coordinator</td>
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
</tbody>
</table>
Glossary
| PAI                                     | Patient Assessment Instrument                                                                                                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCE                                     | Patient Care Encounter                                                                                                                                                                                                                                       |
| PCMM                                    | Primary Care Management Module                                                                                                                                                                                                                               |
| PRF                                     | Patient Record Flag                                                                                                                                                                                                                                          |
| PRINCIPAL MENTAL HEALTH PROVIDER (PMHP) | See MH Treatment Coordinator (MHTC)                                                                                                                                                                                                                          |
| PTF                                     | Patient Treatment File                                                                                                                                                                                                                                       |
| PULL LIST                               | A list of patients whose radiology/PIMS records should be "pulled" from the file room for scheduled clinic visits                                                                                                                                            |
| PX                                      | Patient Care Encounter namespace                                                                                                                                                                                                                             |
| PXRM                                    | Clinical Reminders package namespace                                                                                                                                                                                                                         |
| RAM                                     | Resource Allocation Methodology                                                                                                                                                                                                                              |
| REMINDER DEFINITIONS                    | These are pre-defined sets of findings that are used to identify patient cohorts and reminder resolutions. The reminder is used for patient care and/or report extracts.                                                                                     |
| REMINDER DIALOGS                        | These are pre-defined sets of text and findings that provide information to the CPRS GUI for collecting and updating appropriate findings while building a progress note.                                                                                    |
| REMINDER TERMS                          | Terms are used to map local findings to national findings, providing a method to standardize the findings for national use. These are also used for local grouping of findings for easier reference in reminders and are defined in the Reminder Terms file. |
| ROUTING SLIP                            | When printed for a specified date, it shows the current appointment time, clinic, location, and stop code. It also shows future appointments.                                                                                                                |
| RPC                                     | Remote Procedure Calls                                                                                                                                                                                                                                       |
| RSD                                     | Requirements Specification Document                                                                                                                                                                                                                          |
| RUG                                     | Resource Utilization Group                                                                                                                                                                                                                                   |
> Glossary
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>SBR</th>
<th>Suicide Behavior Report</th>
</tr>
</thead>
<tbody>
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
</tbody>
</table>

# APPENDIX A: Memorandum

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# National Patient Record Flag for High Risk for Suicide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/082.png)

# APPENDIX B: VHA DIRECTIVE 2010-053 PATIENT RECORD FLAGS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs Corrected Copy VHA DIRECTIVE 2010-053 Veterans Health Administration 02/03/2011

> Washington, DC 20420 December 3, 2010

### PATIENT RECORD FLAGS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  PURPOSE:

> This Veterans Health Administration (VHA) Directive outlines policy and guidance for the proper use of Patient Record Flags (PRF) to enhance safety for patients, employees, and visitors.

### BACKGROUND

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VHA is committed to a safety program that is systems based and focused on prevention, not on punishment or retribution. Preventative methods that target root causes are favored.
2.  A PRF alert, VHA employees to patients whose behavior, medical status, or characteristics may pose an <u>immediate</u> threat either to that patient’s safety, the safety of other patients or employees, or may otherwise compromise the delivery of safe health care in the initial moments of the patient encounter. PRF enhance both the right of all patients to receive confidential, safe, and appropriate health care, as well as the right of employees to a safe work environment. PRF permit employees to develop strategies for offering health care to even the most behaviorally challenging patients who, in an earlier era, might have been excluded from receiving VHA health care.
3.  PRF was originally developed for the specific purpose of improving safety in providing health care to patients who are identified as posing an unusual risk for violence. The use of PRF has expanded to address a limited number of additional safety vulnerabilities that present in the initial moments of a patient encounter. These PRFs are to be used very judiciously and approved either by appropriate local or VHA authorities.
4.  The effectiveness of PRF is paradoxically based upon the degree to which their appearance on the computer screen is so unusual that it captures the attention of the user. Inappropriate use of any PRF reduces the effectiveness of all PRFs. Frequent training of busy clinic clerks, emergency department triage nurses, pharmacy technicians, and other typical PRF users is necessary to ensure appropriate use, and to maintain alertness to any PRF.
5.  For ethical reasons, it is inappropriate to use a PRF in the absence of a clear risk to safety. The use of PRF can be ethically problematic for two reasons. First, a PRF stigmatizes patients, labeling them as difficult, whether for clinical or behavioral reasons. Second, a PRF compromises privacy because it reveals private patient information to anyone who opens the

> patient’s chart, regardless of whether that person has the need to know that would normally justify revealing such information. Accordingly, a PRF must only be used for a compelling safety reason which outweighs these ethical concerns.

6.  The use of PRF is limited to addressing immediate clinical safety issues. However, PRF are not an appropriate tool with which to alert employees to every potential safety issue. For example, a patient’s human immunodeficiency virus status is not an <u>immediate threat</u> to the safety of the patient or staff and thus is not appropriate as a PRF and additionally, would be in violation of the patient’s privacy as all users of the Computerized Patient Record System (CPRS) would see the PRF. With the practice of universal precautions, such flags may be redundant.
7.  The use of PRF for administrative or law enforcement purposes is strictly prohibited.

> Signaling a Veteran’s theatre or era of service, unresolved felony warrants, or fee-basis eligibility would be examples of prohibited uses of PRF. <u>Only</u> safety issues of an immediate <u>clinical</u> nature (e.g., recurring violence, high risk for suicide, missing patient) are permitted.

8.  A PRF is not the only tool available that may function as an alert for selected problems. Within CPRS some alert alternatives are: the patient problem list; Crisis Warning Allergies and Directives (CWAD) notes; and Veterans Heath Information Systems and Technology Architecture (VistA). However, only Category I PRF is to be used to signal high risk for seriously disruptive, threatening, or violent behavior.
9.  Blanket program or facility-level access restrictions, based upon the mere presence of a Category I PRF, are prohibited by this Directive. Category I PRF is intended to make it possible for VHA to offer clinical services even to patients who present significant clinical (risk of danger to others) safety challenges. The presence of a Category I PRF on a patient’s health record shall not, by itself, be grounds for refusing admission or services to a patient seeking care in a VHA facility or program. Nor should any PRF be automatic grounds for discharging a patient from a program to which the patient is entitled, and for which the patient is clinically appropriate. Each patient with a PRF is to be evaluated individually for appropriateness for any VHA service. The presence of any PRF should only be one factor in that calculation. Program managers or admission screeners may wish to seek consultation in assessing the suitability of a patient with a Category I PRF for entry into a program or use of a Department of Veterans Affairs (VA) service from the Disruptive Behavior Committee (DBC) or, depending upon the specific type of flag, the relevant body with responsibility for that flag.
10. Category I PRF–-Violent or Disruptive Behavior. Category I PRF is nationally approved and is distributed by VHA as nationally released software for implementation in all VHA facilities. The Category I flag is shared across all known treating facilities for a given patient. Use of Category I PRF is not optional. Individual Category I PRF is assigned locally in accordance with standards developed nationally for the Category I PRF type in question. Category I PRF become national information as part of the Master Patient Index and is displayed at all VHA facilities where the patient is registered. As a result, patients with a Category I PRF who present an immediate safety risk for seriously disruptive, threatening, or violent behavior, may be safely treated within VHA wherever they are registered and seek care. A Text Integrated Utility (TIU) Progress Note in the CPRS describing the rational for the PRF assignment must accompany all Category I PRF.
11. Category II Local PRF—Patient at Risk
1)  Category II PRF may be locally established by individual Veterans Integrated Service Networks (VISN) or facilities. Category II PRF is used in various VHA facilities for a range of purposes. Appropriate uses include:
    1.  Flagging patients who are enrolled in research trials involving potentially risky investigatory pharmaceuticals;
    2.  Flagging patients with a documented history of narcotics diversion or theft;
    3.  Flagging patients at high risk for suicidal behavior;
    4.  Flagging patients with spinal cord injuries;
    5.  Flagging homeless Veterans who have urgent medical test results pending; and
    6.  Flagging missing and wandering patients.
2)  The use of Category II PRF, like Category I PRF, must be strictly limited to information that is immediately needed for the delivery of safe and appropriate health care. A TIU Progress Note in the CPRS describing the rationale for the PRF assignment must also accompany all Category II PRFs.
    1.  Inappropriate Use of PRF. PRF must never be used for law enforcement or administrative purposes. An inappropriate use of PRF for law enforcement might include flagging of fugitive felon status. An inappropriate use of PRF for administrative purposes might include name changes, Operation Enduring Freedom or Operation Iraqi Freedom (OEF/OIF) status, etc.

### POLICY:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is VHA’s policy that all VHA facilities must install all PRF related patches by the mandatory installation date and initiate facility-wide use of PRF.

### ACTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2.  Deputy Under Secretary for Health for Operations and Management. The Deputy Under Secretary for Health for Operations and Management (10N) is responsible for providing oversight to the VISNs to ensure that PRF is appropriately implemented by each VISN.
3.  VISN Director. The VISN Director, or designee (e.g., the Network Mental Health Committee or other comparable VISN group), is responsible for oversight and implementation of this Directive at the VISN level.
4.  Medical Facility Director. The medical facility Director, or designee, is responsible for:
    1.  Ensuring that Category I PRF is originated and accessible. Individual Networks and facilities determine whether optional Category II PRF is to be used. *NOTE: Attachment B, Standards for PRF, defines the standards for the origination of, and access to, both Category I and Category II PRF.*
    2.  Establishing a process for requesting, assigning, reviewing, and evaluating PRF.
    3.  Establishing a plan to transition previous VistA, CPRS, local Class III Advisories, and any other behavioral alerts or warnings system in use, to VHA’s nationally released PRF software. *NOTE: As of September 25, 2003, only PRF computerized advisories as described in Attachment B are approved for use in the identification of patients who are at significant risk for violence.*
    4.  Ensuring that each Category I PRF assigned to a patient is reviewed at least every 2 years; however, reviews may be appropriate anytime a patient’s violence risk factors change significantly, the patient requests a review, or for other appropriate reasons.
    5.  Training appropriate staff in determining when a PRF is to be entered, how PRFs are entered, and how PRF and PRF-related documents are to be maintained and reviewed.
    6.  Evaluating the facility process to ensure that PRF is assigned appropriately.
    7.  Ensuring that each PRF in a patient’s record is accompanied by a TIU Progress Note. The TIU titles utilized must be:
        1.  PRF Category I, or
        2.  PRF Category II.
5.  Clinical Executives: Chief of Staff (COS) and Nurse Executive. The COS and Nurse Executive are responsible for:
    1.  Instituting procedures to ensure that the utilization of PRF and the associated processes for recommending PRF are ethical, clinically appropriate, supported by adequate resources, and used in accordance with this Directive.
    2.  Ensuring that patients are notified that a PRF has been placed in their health record and that they are informed of its contents.
    3.  Establishing a DBC or a Disruptive Behavior Board (DBB). (a) The DBC or DBB is responsible for:
1.  Coordinating, when possible and appropriate, with the clinicians responsible for the patient’s medical care, and recommending amendments to the treatment plan that may address factors that may reduce the patient’s risk of violence.
2.  Implementing the standards in Attachments A and B.
3.  Collecting and analyzing incidents of patient disruptive, threatening, or violent behavior.
4.  Assessing the risk of violence in individual patients.
5.  Informing patients they have a right to request amendment to the contents of a PRF, and providing the information for contacting the facility privacy officer in the event the patient wants to pursue an amendment.
6.  Identifying system problems.
7.  Identifying training needs relating to the prevention and management of disruptive behavior.
8.  Recommending to the COS other actions related to the problem of patient violence. (b) The DBC or DBB must be comprised of:
    1.  A senior clinician chair that has knowledge of, and experience in, assessment of violence;
    2.  A representative of the Prevention Management of Disruptive Behavior Program in the facility (see subpar. 5i);
    3.  VA Police;
    4.  Health Information Management Service and/or Privacy Officer (ad hoc);
    5.  Patient Safety and/or Risk Management official;
    6.  Regional Counsel (ad hoc);
    7.  Patient Advocate;
    8.  Other members as needed, with special attention to representatives of facility areas that are at high risk for violence, (e.g., emergency department, nursing home, inpatient psychiatry, and community-based outpatient clinics).
    9.  Representative of the Union Safety Committee; and
    10. Clerical and administrative support staff to accomplish the required tasks.
        1.  The DBC or DBB, whose primary focus is upon reducing the risk of patient violence toward employees and others, will offer technical advice to other PRF software users as appropriate.
        1.  Identifying a Suicide Prevention Coordinator who will be responsible for entering, maintaining, and deactivating Category II Suicide PRFs in accordance with VHA policy regarding the use of PRFs to identify patients at high risk for suicide.
        2.  Identifying an employee or employees who will be responsible for entering, reviewing, maintaining, and deactivating Category II PRFs for missing or wandering patients in accordance with VHA policy regarding management of wandering and missing patient events.
    1.  Facility Privacy Officer. The facility privacy officer is responsible for:
1)  Receiving requests from patients regarding an amendment to a PRF that has been placed in the patient’s health record.
2)  Amending the health record, as appropriate, according to VHA Handbook 1907.01.

### REFERENCES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Appelbaum PS, Dimieri RJ. “Protecting Staff from Assaults by Patients: OSHA Steps In,” <u>Psychiatric Services.</u> 46(4): 333-338, 1995.
2.  Guidelines for Preventing Workplace Violence for Health Care and Social Service Workers; U.S. Department of Labor, Occupational Safety and Health Administration, OSHA 3148, 1996.
3.  Environment of Care Guidebook, JCAHO, 1997.
4.  VA Suicide and Assaultive Behavior Task Force. Report of a Survey on Assaultive Behavior in VA Health Care Facilities; Feb. 15, 1995.
5.  Blow, FC; Barry, KL; et al. “Repeated Assaults by Patients in VA Hospital and Clinic Settings,” <u>Psychiatric Services</u>. 50(3): 390-394: 1999.
6.  OIG Evaluation of VHA’s Policies and Procedures for Managing Violent and Potentially
> Violent Psychiatric Patients (Report No. 6HI-A28-038).
7.  Drummond, D, et al., “Hospital Violence Reduction in High-risk Patients,” <u>Journal of the American Medical Association (JAMA)</u>. 261(17) 531-34, 1989.
8.  United States Postal Commission. Report of the Commission on a Safe and Secure Workplace. National Center on Addiction and Substance Abuse at Columbia University, New York 2000.(Goldstein N et al) Columbia University, August 2000.
9.  Hodgson MJ, Reed R, Craig T, Belton L, Lehman L, Warren N. Violence in healthcare facilities: lessons from VHA. <u>J Occup Environ Med.</u> 2004 ;46:1158-1165.
10. Secretary’s Letter to All VA Employees October 19, 2001 [<u>http://vaww1.va.gov/VASAFETY/DashoLetters/AllVAEmployeesAndVolunteersLett.pd</u> f](http://vaww1.va.gov/VASAFETY/DashoLetters/AllVAEmployeesAndVolunteersLett.pdf) *NOTE: This is an internal VA Web site not available to the public.*
11. VA Office of Occupational Safety and Health Intranet Site: [<u>http://vaww.va.gov/vasafety</u> .](http://vaww.va.gov/vasafety) *NOTE: This is an internal VA Web site not available to the public.* Includes links to the Prevention and Management of Disruptive Behavior, VA training program.
12. Public Law 105-220, Section 508.
13. Calhoun, FS, Weston, S.W. (2003). <u>Contemporary threat Management: A Practical guide</u> <u>for Identifying, Assessing, and Managing Individuals of Violent Intent.</u> Sand Diego, CA: Specialized Training Services.
14. Employee Education System, US Dept. of Veterans Affairs Training DVD: Preventing
> Violence in Healthcare: Identifying, assessing, and Managing Violence-Prone Patients, 2005.
15. Meloy, J.R. (2000). <u>Violence risk & threat Assessment: A Practical Guide for Mental Health & Criminal Justice Professionals.</u> San Diego, CA: Specialized Training Services.
16. Elbogen, EB; Beckham, JC;Butterfield, MI; Swartz, M; Swanson, J. “Assessing Risk of Violent Behavior Among Veterans with Severe Mental Illness.” <u>Journal of Traumatic Stress</u>, Vol. 21. February 2008, pp. 113-117.
17. Association of Threat Assessment Professionals (ATAP) [<u>http://www.atapworldwide.org/</u> .](http://www.atapworldwide.org/) r. RAGE-V, Risk Assessment Guideline Elements for Violence (2006). May be downloaded at no cost from [<u>http://www.atapworldwide.org/</u> <u>associations/8976/files/ documents/RAGE-V.pdf</u>](http://www.atapworldwide.org/%20associations/8976/files/%20documents/RAGE-V.pdf) .
19. White, SG, Meloy, JR. (2007) <u>WAVR-21, A Structured Professional Guide for the Workplace Assessment of Violence Risk.</u> San Diego, CA: Specialized Training Services.
20. Mental Health Initiatives memo, Deputy Undersecretary for Health Operations and Management, June 1, 2007.
21. Department of Veterans Affairs Office of the Inspector General. Implementing VHA Mental Health Initiatives for Suicide Prevention; May 10, 2007.
22. <u>Suicide Risk Assessment Guide Reference Manual,</u> which can be found at: [<u>http://vaww.mentalhealth.va.gov/files/suicideprevention/SuicideRiskGuide.doc</u>](http://vaww.mentalhealth.va.gov/files/suicideprevention/SuicideRiskGuide.doc) *NOTE: This is an internal VA Web site not available to the public.*
5.  RESPONSIBLE OFFICE: The Office of Patient Care Services, Office of Mental Health
> \(116\) is responsible for the contents of this VHA Directive. Questions may be referred to (202) 461-7364.
6.  RESCISSIONS: VHA Directive 2003-048, dated August 28, 2003 is rescinded. This Directive expires on December 31, 2015. JRobert A. Petzel, M.D. Under Secretary for Health

### ATTACHMENT A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VHA DIRECTIVE 2010-053

> December 3, 2010

> STANDARDS FOR CATEGORY I AND CATEGORY IIPATIENT RECORD FLAGS

> DISTRIBUTION: E-mailed to the VHA Publications Distribution List 12/8/2010

1.  BACKGROUND: A diverse group of patients present with certain behavioral or clinical risk factors that place special demands upon the health care system. It is both a privilege and a challenge for the Department of Veterans Affairs (VA) health care employees and facilities to offer safe and appropriate care to all patients. The safety of patients and the safety of staff who treat them, can be enhanced when carefully designed Patient Record Flags (PRF) immediately alert care providers to the presence of risk factors *that must be made known in the initial moments of a patient encounter*.
    1.  Because some of the most challenging patients may be nomadic, and because a patient’s electronic health record is increasingly available to other facilities, it is essential that conventions for creating, supporting, and maintaining computerized advisories be made uniform throughout VA’s health care system.
    2.  PRFs should never be used to punish or to discriminate against patients, nor should they be constructed merely for staff convenience. The effectiveness of PRFs depends upon limiting their use to those unusual risks that threaten the safe delivery of health care. Threats to the effective use of PRFs are their misuse and overuse.
    3.  Providing an environment that is safe for patients, visitors, and employees is a critical factor in health care. The safety of patients and staff, as well as the effectiveness of care and patients’ right to privacy and dignity, need not be compromised by threats of violence or other clinical safety risk factors. Risks associated with a history of violence or other risk factors can be limited when those risks are recognized and reported. Risks need to be addressed by an interdisciplinary group under senior clinical leadership and documented, when appropriate, in the patient's treatment plan. They must also be communicated in a standardized manner to those most at risk in an encounter with a “flagged” patient.
2.  PROCEDURES: Each facility must demonstrate its readiness to use PRF in a manner which is consistent with the standards and protocols outlined in this Directive.
    1.  As part of the patient health record, all PRFs are entered under the authority of the Chief of Staff (COS) or designee at each facility. *NOTE: PRF must be accorded the same confidentiality and security as any other part of the health record.*
    2.  The COS, or designee, at each facility is responsible for identifying those employees authorized to initiate, enter, and access PRF. The COS, or designee, must ensure that only those employees with a demonstrated need to know are permitted access to PRF menu options.
    3.  Access to viewing PRFs is recommended for employees who are likely to be the first to encounter a “flagged” patient, prior to or at the time of the patient's visit. Access

VHA DIRECTIVE 2010-053December 3, 2010

> includes viewing the type of PRF and the narrative associated with it. Those who access a PRF are responsible for communicating the PRF advisory to doctors, nurses, and others who have a need to know. The following are examples of medical center staff who have direct patient contact needing to view, or be made aware of PRF:

1.  Emergency room clerks and receptionists;
2.  Administrative Officer of the Day;
3.  Pharmacists and pharmacy technicians; (4) VA police officers;
5)  Enrollment clerks;
6)  Social Work staff;
7)  Triage and telephone care staff;
8)  Ward and clinic clerks;
9)  Insurance and billing staff;
10) Receptionists;
11) Travel clerks;
12) Laboratory clerks and technicians; (13) All medical staff;

> \(14\) Patient advocates; (15) All Nursing staff;

> \(16\) Decedent Affairs Clerk; (17) Scheduling staff;

18) Fee clerks; and
19) Release of Information Clerks.
    1.  PRF software is in place. Although facilities may respond appropriately to PRF transmitted from other facilities, only facilities that employ the criteria in this Directive may enter new Category I PRFs.
    2.  A Text Integration Utility (TIU) Progress Note must be entered at the same time as the entry of any PRF. This note must provide general guidance to PRF users, and should include a brief summary of the rationale for the existence of the specific PRF. The progress note, however, is not the same narrative as the PRF itself.
    3.  A process exists for the review of each flag for risk of violent behavior at least every 2 years. A review may be appropriate when: the risk factors change significantly; a patient with a PRF requests a review; or for other appropriate reasons as determined by the facility that established the flag. A reminder for an upcoming review must be generated 60 days prior to the 2-year anniversary date of each PRF.

VHA DIRECTIVE 2010-053December 3, 2010

4.  PRFs serve only to preserve and enhance the safety and appropriateness of patient care.
5.  PRFs alert staff to a potential risk only; they are advisories. At each patient encounter, the examining physician or other clinician remains responsible for making appropriate clinical decisions.
6.  Each facility must have clearly written definitions and entry criteria (that are consistent with this VHA Directive) for all Category I and Category II PRFs.
7.  PRF should be entered, only by employees who have been trained in the technical aspects of entry, with the appropriate criteria, and in the conventions for security, format, and terminology.
8.  PRF must be free of redundant language, slanderous or inflammatory labels, and must provide sufficient information or guidance for action. PRF narratives must be written in language sufficiently specific as to inform readers of the nature of the risk and recommended actions to reduce that risk. The PRF narrative should also avoid alluding to site-specific persons, acronyms, abbreviations, processes, buildings, or other descriptors unique to the originating site that would have no meaning for other sites where the Veteran may appear.
9.  In order for PRFs to be effective, they must be used only when necessary. PRFs should be deactivated when their usefulness has passed. Overuse dilutes the importance of a PRF. Each facility must exercise great care in establishing optional Category II PRFs. Only when there is a compelling immediate clinical safety issue should additional PRF types be utilized. PRF is not to be used for staff convenience, or to address administrative or law enforcement concerns. Category II PRF types must adhere to the standards as spelled out in this attachment.
10. Patients may request an amendment to the presence or content of a PRF advisory through the facility privacy officer.
11. The Deputy Under Secretary for Health for Operations and Management (10N) provides oversight to the Veterans Integrated Service Networks (VISN) to ensure that PRFs are appropriately implemented by the facilities.
12. All VHA staff must respond appropriately to the appearance of PRF.
13. All VISNs must establish processes for the origination and appropriate use of Category I PRFs.
    1.  All facilities are required to implement and respond to Category I PRFs, regardless of which facility originated the flag.
    2.  All facilities must participate in utilization of PRF, regardless of the originating facility for any individual advisory or type of PRF advisory. <u>Only the nationally developed PRF is to be</u> <u>utilized</u>.

VHA DIRECTIVE 2010-053December 3, 2010

14. The responsibility for ensuring the quality, timeliness, routine review, and documentation in support of a PRF advisory belongs to the originating facility.
    1.  The advisory itself will reference the authorizing facility and the COS or designee who can provide additional information about a specific PRF advisory. A facility that, in the course of providing care to a patient who was “flagged” by another facility, discovers new information that could influence the status of that advisory should not amend the original advisory, but instead should contact the originating facility with the new information.
    2.  The responsibility for ownership and maintenance of PRF needs to be transferred when it appears that a flagged patient has relocated to a new facility. The originating facility should make available to the new facility, copies of all documents and records in support of the advisory.
15. PRF Training.
    1.  Training must provide instruction on how to utilize PRF software on the assignment, continuation, inactivation, and review of flags.
    2.  Training content must address:
        1.  Various types of PRF;
        2.  Appropriate responses; (c) PRF confidentiality; and

> \(d\) Compliance with Public Law 105-220 Section 508 (see subpars. 5h and 5i).

VHA DIRECTIVE 2010-053December 3, 2010

### ATTACHMENT B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CATEGORY I PATIENT RECORD FLAGS (PRF):SPECIAL REQUIREMENTS

1.  Category I Violent and Disruptive Behavior are currently the only implemented *types* of Category I PRFs that are designed to appear in all Department of Veterans Affairs (VA) facilities where a Veteran is registered to receive care. All Category I PRFs require a Text Integrated Utility (TIU) Progress Note in the Computerized Patient Record System (CPRS).
2.  Category I Violent and Disruptive Behavior PRF describe patient risk factors that may pose an immediate threat to the safety of other patients, visitors, or employees. Category I Violent and Disruptive Behavior PRF also recommend specific behavioral limit settings or treatment-planning actions designed to reduce violence risk.
3.  Health care workers experience one of the highest rates of nonfatal injuries from workplace assault of any occupation in the United States (U.S.). Health care is one of only two industries that have merited special attention from the U.S. Occupational Safety and Health Administration (OSHA) (see subpars. 5a and 5b). When compared to employees of other health care systems, Veterans Heath Administration (VHA) employees are two and a half times more likely to suffer injuries in violent incidents involving patients (United States Postal Commission, 2000; Hodgson et al, 2004). In recognition, VHA has initiated a broad-based program of violence prevention, including performance monitors through the Office of the Deputy Under Secretary for Operations and Management. Efforts have included the redesign of the basic course for all employees, “Prevention and Management of Disruptive Behaviors,” and the development of new courses for geriatrics and other disciplines.
4.  The Joint Commission recently made patient violence and its prevention, a focus of the Environment of Care Standards (see subpar. 5c).
5.  VA’s Office of Inspector General (OIG) in its report “Evaluation of VHA’s Policies and Practices for Managing Violent or Potentially Violent Psychiatric Patients” (6HI-A28-038, dated March 28, 1996) recommended that facilities communicate among themselves so that staff are aware of high risk patients regardless of where in VHA’s system they may seek health care (see subpar. 5f).
6.  For PRF to assist in the prevention of adverse events when high risk patients travel between facilities, all facilities must follow uniform processes as described in current VHA policy on inter-facility transfer. This would include noting any existing Patient Record Flag. The effectiveness of PRFs depends upon limiting their use to those unusual clinical risks that <u>immediately</u> threaten health care safety and quality in the initial moments of a patient encounter.

VHA DIRECTIVE 2010-053December 3, 2010

7.  The safety of patients and employees, the effectiveness of care, and the patient’s right to privacy need not be compromised by threats of violence. Risk of violence can be mitigated by reporting, assessing, documenting, communicating, and developing treatment plans that specifically make violence reduction a treatment objective.
8.  The decision to enter a Category I Violent and Disruptive Behavior PRF must be made by the Disruptive Behavior Committee (DBC) or the Disruptive Behavior Board only after completion of an evidence-based, multidisciplinary, and multi-dimensional threat assessment, which considers static and dynamic violence risk factors present in the patient, violence risk mitigators, and violence risk factors associated with the setting where the incident occurred (see subpar. 5o). Attachment C describes a threat assessment protocol that meets these requirements. There may be other protocols or instruments that are suitable, but the burden is on any DBC to use a threat assessment protocol that is evidence-based.
9.  Competent prediction of violence is always multi-dimensional, and a thorough assessment of violence risk should consider factors relating not only to the patient but also to the training and behavior of the Department of Veterans Affairs (VA) employees, and to aspects of the situation in which the patient is treated.
10. The facility must develop a systematic approach for collecting reports involving incidents of disruptive, threatening, or violent behavior.
11. Interdisciplinary review and threat assessment of patient behavior is documented, and the documentation of this review and of all associated incident reports are kept in a secure location. In many cases, a summary of the threat assessment should be shared with the patient’s care providers in an effort to address the problem of violence risk in the patient’s treatment plan.
12. Appropriate training of staff, who in the course of their duties, must assess and document violence risk, as well as implement or recommend behavioral limits and treatment plans, will be documented. All DBC members should avail themselves of ongoing training opportunities available through the Employee Education System and VA’s Office of Occupational Safety and Health (see [<u>http://vaww1.va.gov/VASAFETY/OSH_Education.asp</u>](http://vaww1.va.gov/VASAFETY/OSH_Education.asp) ). *NOTE: This is an internal VA Web site not available to the public.*VHA DIRECTIVE 2010-053December 3, 2010

### ATTACHMENT C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> THREAT ASSESSMENT

> The purpose of Disruptive Behavior Committees (DBC) or Disruptive Behavior Boards (DBB) is to evaluate the risk of violence in a given setting or situation, with a given patient and to recommend measures that may be taken to mitigate that violence risk. This is often called

> “threat assessment.” In their 2007 guide entitled, <u>WAVR-21, A Structure Professional guide for</u> <u>the Workplace Assessment of Violence Risk</u>, White and Meloy describe the purpose of groups like DBCs:

> “*They will gather information concerning the context and critical aspects of the behavior in question, and about the employee or third party whose behavior has generated concern. The risk assessment professional will then synthesize and evaluate the data and apply careful professional judgment to answer the ultimate questions: Does the person whose conduct has generated concern pose a threat? And if so, what is the general level of threat? What steps can be taken to mitigate any risk, and what actions might exacerbate it?”*

> Examples of common sentinel events that should lead to a violence risk assessment by the DBC or DBB include, but are not limited to: a report of physical violence against patients or staff at a medical center or clinic; documented acts of repeated violence against others; credible reports verbal threats of harm against specific individuals, patients, staff, or the Department of Veterans Affairs’ (VA) property; reports of possession of weapons or objects used as weapons in a health care facility; a documented history of repeated nuisance, disruptive or larcenous behavior that disrupts the environment of care; or a documented history of repeated sexual harassment toward patients or staff.

> However, the mere occurrence of a sentinel event should not be cause to initiate a Category I Violent and Disruptive Behavior PRF. DBCs or DBBs are not “Flagging Committees.” Patients are not “flagged” because they have demonstrated disruptive behavior or because their Primary Care Provider or other provider, having been verbally abused or threatened, is upset and demands that the patient be flagged. DBCs apply a Category I Violent and Disruptive Behavior PRF to a patient’s record only when the DBC concludes in a review of violence risks and mitigators that to do so will likely reduce violence risk.

> All members of DBCs or DBBs should take advantage of training offered by VA Employee Education System (EES), and when possible, by outside vendors. The references in this Directive provide suggested resources for training and information on violence prediction and threat management.

VHA DIRECTIVE 2010-053December 3, 2010

> The following is one evidence-based threat assessment protocol suggested for use by DBCs or DBBs (adapted from Meloy, 2000 see subpar. 5o):

> Patient Risk Factors: (list of factors is not exhaustive and factors not equally weighted)

> Static Risk Factors: (Include additional detail for each item checked) Male Gender (10X risk for females).

> Veteran’s history of violence in and outside of health care facilities. Consider frequency and recency of violence, and severity of injury to victims, if any.

> <u>Additional Comments:</u>

> Veteran’s self-report of arrests and convictions for violent crimes. (Criminal background investigation data may be available in selected cases, if VA Police conclude that there is probable cause for obtaining and sharing this information on a need-to-know basis.)

> <u>Additional Comments:</u>

> Documented credible threats toward VA employees or patients. <u>Additional Comments:</u>

> Prior supervision/treatment plan failures, (e.g., probation, mandated Drug and Alcohol treatment.

> <u>Additional Comments:</u>

> Presence of serious psychiatric disorder, especially psychopathy or paranoia.

> <u>Additional Comments:</u>

> Head injury with Loss of Consciousness by history. <u>Additional Comments:</u>

> Dynamic Risk Factors: (Include additional detail for each item checked)

> Recent incidents of disruptions, threats, or violence in or out of health care settings.

> <u>Additional Comments:</u>

> Recent (past 6 mos) abuse of Central Nervous System (CNS) stimulants, including Cocaine and Methamphetamines.

> <u>Additional Comments:</u>

> Recent abuse of ETOH or other CNS disinhibitors. <u>Additional Comments</u>:

> Presence of situational stressors and destabilizing events, such as recent incarceration, death of loved ones, financial problems, estrangement from his or her family, homelessness, onset of acute medical problems, and other destabilizing events.

> <u>Additional Comments:</u>

> Chronic pain or narcotics seeking behavior. <u>Additional Comments:</u>

> Documented impulsivity (e.g., financial, sexual, or other decision making). <u>Additional Comments:</u>

> Veteran’s claims of weapons in his possession, especially new acquisition or relocation of firearms.

> <u>Additional Comments:</u>

> Risk Mitigation Factors: (Include additional detail for each item checked) Numerous visits to Medical Center without incidents.

> <u>Additional Comments:</u>

> Positive recommendation of Veteran’s health care providers. <u>Additional Comments</u>:

> Documentation of successful participation in substance abuse recovery program with a significant (60 days or more) period of sobriety.

> <u>Additional Comments:</u>

> Documented resolution of destabilizing events or factors. <u>Additional Comments:</u>

> Patient’s acknowledgement of his previous disruptive behavior with plans for preventing recurrence.

> <u>Additional Comments:</u>

> Changes in patient’s health status or mobility that would mitigate any threat the patient previously posed.

> <u>Additional Comments:</u>

> SETTING RISK FACTORS

> ![](high-risk-mental-health-patient-patient-record-flags-user-guide/083.png)![](high-risk-mental-health-patient-patient-record-flags-user-guide/084.png) Staffing issues (please describe): ![](high-risk-mental-health-patient-patient-record-flags-user-guide/085.png) Training deficits (please describe):

> Supervisory issues (please describe):

### ATTACHMENT D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VHA DIRECTIVE 2010-053

> December 3, 2010

### NEW SERVICE REQUESTS CATEGORY I PATIENT RECORD FLAG (PRF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  BACKGROUND

> Patient Record Flags were initially mandated by the Veterans Health Administration (VHA) Under Secretary for Health at the urging of the Department of Veterans Affairs (VA) Office of Inspector General (OIG) solely as a tool for reducing the risk of imminent violence associated with ‘high risk’ patients. On August 28, 2003, Directive 2003-048, National Patient Record Flags, was issued in conjunction with a release of revised Veterans Information System and Technology Architecture (VistA) Computerized Patient Record System (CPRS) software. By alerting VHA employees to a significant *immediate* risk of violence, this software enables health care providers and other VA employees who may encounter a high-risk patient to take measures to offer the patient safe and appropriate health care regardless of where, in the VHA system, the patient appears and regardless of where the PRF originated. While initially intended to address the problem of high-risk-for-violence patients only, the PRF software was recognized as offering potential additional uses. It is expected that New Service Requests (NSR) for additional <u>types</u> of Category I PRF may be proposed. This packet is intended to assist those who are considering the proposal of NSR for Category I PRF types.

### PROCESS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Applicants should thoroughly familiarize themselves with the VHA Patient Record Flag policy prior to completing the attached application. The policy addresses the specific use of Category I PRF for preventing violence, but also includes many standards that will be used to measure the appropriateness of any future Category I PRF uses. These standards have been reviewed in depth and approved by the VA OIG, the VA Center on Ethics, and others that continue to monitor the use of Category I PRF. Applicants can also find more information about the intent and proper use of PRFs on the PRF Web site: [<u>http://vaww.vistau.med.va.gov/vistau/PRF/default.htm</u>](http://vaww.vistau.med.va.gov/vistau/PRF/default.htm) . *NOTE: This is an internal VA Web site not available to the public.*
2.  Category I PRF are, by definition, disseminated throughout all VHA facilities where the patient is registered. Category II PRF, in contrast, are entered locally and appear only locally at the originating facility. The present packet relates to Category I (national) PRF only. However, Directive 2003-048 is clear that even ‘local’ (Category II) PRF should be used judiciously and, as with Category I PRF, *only* for alerting users to immediate threats to the clinical care and safety of patients or staff. The more PRFs of any type to which receptionists, clerks, and other VA employees must attend in the initial moments of an encounter with a patient, the less potent any PRF alert will be. More is not better when it comes to PRF.
3.  The responsibility for PRFs is assigned to the Office of Mental Health (116) under Patient Care Services (11). The Deputy Chief Patient Care Services, Officer for Mental Health Services

VHA DIRECTIVE 2010-053December 3, 2010

> \(116\) has authorized the formation of a PRF Advisory Review Board to review NSRs for new Category I PRFs. The PRF Advisory Review Board considers the NSR and other input required (textual or verbal presentation) and makes recommendation(s) back to the PRF Program Office (116A) to approve or disapprove with comments. The PRF Program Office (116A) then responds to the NSR with recommendation(s).

4.  The PRF Program Office (116A) forwards the decision to the Chief Officer of Patient Care Services (11) for any other action that may be required.
5.  Current membership of the PRF Advisory Group includes:
    1.  The Deputy Under Secretary for Health for Operations and Management (10N).
    2.  Patient Care Service, VA Central Office (11).
    3.  Health Information Management (HIM) Program Office, VHA Office of Health Information (19).
    4.  VA Office of Information and Technology (OI&T) (005), PRF Project Manager.
    5.  Field Subject Matter Experts, at least two at any given time.
    6.  Office of the General Counsel, VA Central Office (02).
    7.  National Center for Ethics, VA Central Office (10E).
    8.  VHA Occupation Health Program (136A).
6.  At the discretion of the chair, Deputy Chief Patient Care Services Officer for Mental Health (116), other subject matter experts may be called upon to evaluate specific NSRs.

### APPLICATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

7.  An online NSR application is available at: [<u>http://vista.med.va.gov/nsrd/</u>](http://vista.med.va.gov/nsrd/) and is accessed by pressing the New Request button.
8.  When filling out the form it is important to identify the unique issues of a PRF:
    1.  Describe the clinical safety issue to be addressed. Note that the use of PRFs is restricted to the communication of information of a clinical safety nature that must be available in the initial moments of a patient encounter. As PRFs are effective only to the extent that they are unusual stimuli in the user’s visual field, Category I PRF are to be used <u>only</u> for immediate clinical safety purposes, and <u>only</u> when there are no viable alternatives. Describe all possible alternatives to a PRF that you explored to meet your safety goals and objectives.
    2.  Other factors might include any additional factors that make this request a high clinical safety priority that must be available in the initial moments of a patient encounter. Provide all relevant VHA references, (e.g., Congressional Mandate, Directive,

> Secretary’s Performance Measure, studies). Note factors both inclusive and exclusive that would justify entry of a PRF of this proposed type into the health record of a given

> patient, and also the factors that would be used to determine that the PRF would be no longer necessary. Describe the frequency with which a PRF of this type would be reviewed and by whom. Note on what basis this frequency of review is proposed. Also note that the PRF must be accompanied by a CPRS progress note.