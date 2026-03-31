---
title: Clinical Reminders Version 2 Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: anchor
doc_subject: 
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2
group_key: "PXRM:PXRM:2"
file_numbers: 
  - 801
security_keys: []
menu_options: 7
description: 1. [Map local findings to the national Reminder Terms. 20](#Setup_Steps) 2. [Run the Reminder Test option after term definition mapping is completed. 27](#2.__Run_the_Reminder_Test_option_after_t) 3. [Enter data through reminder dialogs to have information to test the extract functionality 27](#2.__
audience: 
keywords: 
  - blockquote
  - strong
  - class
  - table
  - style
  - width
  - reminder
  - colgroup
  - thead
  - tbody
page_count: 0
word_count: 23351
section_count: 6
table_count: 1
figure_count: 0
appendix_count: 5
has_toc: False
is_stub: False
pub_date: February 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_sg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_sg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](clinical-reminders-version-2-setup-guide/001.png)

> Clinical Reminders

> Version 2

> SETUP GUIDE

> February 2005

> Updated: July 2005

> Health Data Systems

> V*IST*A HSD&D

#### Department of Veterans Affairs

1.  [Map local findings to the national Reminder Terms. 20](#Setup_Steps)
2.  [Run the Reminder Test option after term definition mapping is completed. 27](#2.__Run_the_Reminder_Test_option_after_t)
3.  [Enter data through reminder dialogs to have information to test the extract functionality 27](#2.__Run_the_Reminder_Test_option_after_t)
4.  [Run a Reminders Due Report for a test period of time 27](#2.__Run_the_Reminder_Test_option_after_t)
5.  [Initiate a manual run from Reminder Extract Management – without transmitting. 27](#2.__Run_the_Reminder_Test_option_after_t)
6.  [Review the content of the Extract Summary 29](#6.___Review_the_content_of_the_Extract_S)
7.  [Run a reminder report for the patient lists created from the extract 30](#7.__Run_a_reminder_report_for_the_patien)
8.  [Turn on the logical Link in the HL7 package. 30](#7.__Run_a_reminder_report_for_the_patien)
9.  [Initiate the production account run of the Automatic QUERI Extracts/ Transmission. 32](#_bookmark9)
10. [Examine patient lists from first auto extract; run Health Summary or Reminder Reports 33](#_bookmark10)
11. [Review the Transmission History 33](#_bookmark10)
12. [After the first run is completed, review the content of the mail messages created 33](#_bookmark10)

> Revision History

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 17%" />
<col style="width: 35%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Revision Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Page or Chapter</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>May 2005</p>
</blockquote></td>
<td><blockquote>
<p>Page 21</p>
</blockquote></td>
<td><blockquote>
<p>Correction to condition</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Part_I:__Introduction_to_Clinical_Remind" class="anchor"></span><strong>Introduction</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>New Functionality in Clinical Reminders V. 2.0</strong></p>
<p>Clinical Reminders V. 2.0 (PXRM*2_0) adds four <em>new</em> Ischemic Heart Disease (IHD) reminder definitions, two <em>modified</em> reminder definitions, modified reminder dialogs, reminder taxonomies, and reminder terms and health factors to support Phase II of the IHD project. It also redistributes three Mental Health (MH) reminder definitions, along with the reminder dialogs, reminder taxonomies, and reminder terms, and health factors to support Phase II of the MH project.</p>
<p>Phase II contains compliance reporting and rollup functionality for the reminders distributed in Phase I.</p>
<p>Also included in Version 2.0:</p>
</blockquote>
<ul>
<li><p>Functionality for VA-GEC (Geriatric Extended Care)</p></li>
<li><p>Functionality for My Health<em>e</em>Vet Phase III Reminders</p></li>
</ul>
<blockquote>
<p><strong>Overview of Major Changes</strong></p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Compliance reporting and rollup functionality</strong></p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>New menus and options:</strong></p>
<p>Reminder Patient List Menu [PXRM PATIENT LIST MENU] This menu contains options for creation of term-based list rules that can be used in both extract processing and patient list creation.</p>
<p>Reminder Extract Menu [PXRM EXTRACT MENU]</p>
<p>This menu contains options that allow display and edit of extract finding rules used in the extract process and of extract parameters for use in extract processing.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Overview of</strong> <strong>Major Changes</strong></p>
</blockquote></th>
<th><ul>
<li><p><strong>Reminder Definition Enhancements</strong></p>
<ol type="1">
<li><p>Expanded and improved output format for Clinical Maintenance</p></li>
<li><p>Expanded output format in Reminder Inquiry</p></li>
<li><blockquote>
<p>Changes to finding date search (BEGINNING DATE and ENDING date)</p>
</blockquote></li>
<li><p>New finding modifiers</p>
<ol type="a">
<li><p>Occurrence Count</p></li>
<li><blockquote>
<p>Status list (See Appendix D.)</p>
</blockquote></li>
<li><blockquote>
<p>CONDITION Enhancements</p>
</blockquote></li>
</ol></li>
<li><blockquote>
<p>New finding types</p>
</blockquote>
<ol type="a">
<li><blockquote>
<p>Location List finding</p>
</blockquote></li>
<li><blockquote>
<p>Function findings</p>
</blockquote></li>
<li><blockquote>
<p>Computed findings enhancements</p>
</blockquote></li>
</ol></li>
<li><p>Custom Date Due capabilities</p></li>
<li><p>More information in the Reminder Test option output</p></li>
</ol></li>
</ul>
<blockquote>
<p><strong>Other changes:</strong></p>
</blockquote>
<ul>
<li><p>Historical entries are no longer flagged with an "E" following their date in the test option output, and are not shown as historical in the clinical maintenance output.</p></li>
<li><p>The Lab test names that are displayed now come directly from the Laboratory Test file. In V. 1.5, the national lab test name was displayed, so what you see for the name of the test may no longer match.</p></li>
<li><p>With the global indexes (installed with PXRM*1.5*12), we are able to make a more thorough search of the Patient Treatment File (PTF), plus we have included movement nodes for the first time. This means that for a taxonomy finding, you may find a result from PTF instead of the result from V POV or Problem List that is in your archived finding. As long as the PTF result is valid and newer than the archived result, this is okay.</p></li>
<li><p>In an effort to speed up taxonomy evaluation in v2.0, taxonomy expansions are loaded into memory. The upper limit for memory storage seems to be around 5,000 codes. If a large taxonomy is necessary, it could be split into pieces and included in a Reminder term.</p></li>
<li><p>All the national reminders that used the old MRD have been converted to use a function finding and the updated definitions are distributed in V. 2.0. Sites will need to convert their locally defined reminders. See Appendix E in the Install Guide for a detailed example.</p></li>
</ul>
<blockquote>
<p><strong>Example</strong>:</p>
<p>Customized PATIENT COHORT LOGIC to see if the Reminder applies to a patient:</p>
<p>FI(2)&amp;FI(11)&amp;(MRD(FI(2)))&gt;(MRD(FI(9)))&amp;'FI(13)</p>
<p>First define function finding 1 to be MRD(2)&gt;MRD(9) then change the customized cohort logic to: FI(2)&amp;FI(11)&amp;FF(1)&amp;’FI(13)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

- Reminder Dialog Enhancements
1.  New options on the Reminder Dialog Management menu: Dialog Reports ... \[PXRM DIALOG TOOLS MENU\]
    1.  Reminder Dialog Elements Orphan Report \[PXRM DIALOG ORPHAN REPORT\]
    2.  Empty Reminder Dialog Report \[PXRM DIALOG EMPTY REPORT\]
2.  Dialog overview and Dialog Summary actions added on the Dialog Edit screen on the Reminder Dialog (DI) option. These actions are available after a specific dialog is selected.
3.  New Branching/conditional logic added to dialog editing options that allows display of alternate checkboxes in dialogs, depending on whether defined conditions meet certain criteria.

> Overview of Major Changes

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Overview of Major Changes</strong></p>
</blockquote></th>
<th><ul>
<li><p><strong>NOIS fixes</strong></p></li>
</ul>
<blockquote>
<p>More than 75 NOIS and several E3Rs have been resolved by Clinical Reminders V. 2.0.</p>
</blockquote>
<ul>
<li><p><strong>E3R Enhancements</strong></p></li>
</ul>
<blockquote>
<p>E3R 15489 CHANGES TO REMINDER REPORT SELECTION CRITERIA</p>
<p>E3R #18249 NEED DESIGNATION OF PATIENT REMINDERS</p>
<p>“P” for patient has been added to the Usage field. This is intended for use by MyHealtheVet, but it can also be used by other packages that want to display patient reminders.</p>
<p>NOTE: “L” for List has also been added to the Usage field. This is intended for patient list use, and overrides other entries; i.e., if L is entered, the reminder will not show on the cover sheet in CPRS.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Part II: Setup Procedures](#part-ii-setup-procedures)
    - [MH Term Mapping](#mh-term-mapping)
    - [Example: Mapping a local finding to a Depression Screening Term](#example-mapping-a-local-finding-to-a-depression-screening-term)
    - [Example: GEC Note Titles](#example-gec-note-titles)
  - [APPENDIX A: Hints and Tips](#appendix-a-hints-and-tips)
  - [APPENDIX B: Glossary](#appendix-b-glossary)
    - [Acronyms](#acronyms)
    - [National Acronym Directory](#national-acronym-directory)
  - [APPENDIX C: National Reminders Rescission](#appendix-c-national-reminders-rescission)
    - [National Reminder Rescission and Renaming](#national-reminder-rescission-and-renaming)
    - [Status list](#status-list)
    - [New reminder status:](#new-reminder-status)
  - [Index](#index)
<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Overview of Major Changes</strong></p>
<p>During the installation of</p>
<p>V. 2.0, existing national reminders are rescinded, in part by renaming them ZZ*. ZZ is reserved for use as a scratch namespace (defined on FORUM, Package File). As such, sites may already have copied a reminder and used the prefix ZZ. Sites should review their local reminders, to ensure that this installation doesn’t write over any reminders.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Rescission of National Reminders</strong></p>
<p>The following national reminders are rescinded by changing VA to ZZVA in the name and replacing the Print Name with ZZ Print Name.</p>
<p>VA-*BREAST CANCER SCREEN VA-*CERVICAL CANCER SCREEN VA-*CHOLESTEROL SCREEN (F) VA-*CHOLESTEROL SCREEN (M)</p>
<p>VA-*COLORECTAL CANCER SCREEN (FOBT) VA-*COLORECTAL CANCER SCREEN (SIG.) VA-*FITNESS AND EXERCISE SCREEN</p>
<p>VA-*HYPERTENSION SCREEN VA-*INFLUENZA IMMUNIZATION VA-*PNEUMOCOCCAL VACCINE</p>
<p>VA-*PROBLEM DRINKING SCREEN</p>
<p>VA-*SEATBELT AND ACCIDENT SCREEN</p>
<p>VA-*TETANUS DIPHTHERIA IMMUNIZATION VA-*TOBACCO USE SCREEN</p>
<p>VA-*WEIGHT AND NUTRITION SCREEN</p>
<p>VA-ADVANCED DIRECTIVES EDUCATION VA-ALCOHOL ABUSE EDUCATION</p>
<p>VA-BLOOD PRESSURE CHECK VA-BREAST EXAM</p>
<p>VA-BREAST SELF EXAM EDUCATION VA-DIABETIC EYE EXAM</p>
<p>VA-DIABETIC FOOT CARE ED. VA-DIABETIC FOOT EXAM</p>
<p>VA-DIGITAL RECTAL (PROSTATE) EXAM VA-EXERCISE EDUCATION</p>
<p>VA-FECAL OCCULT BLOOD TEST VA-FLEXISIGMOIDOSCOPY</p>
<p>VA-INFLUENZA VACCINE VA-MAMMOGRAM</p>
<p>VA-NUTRITION/OBESITY EDUCATION VA-PAP SMEAR</p>
<p>VA-PNEUMOVAX VA-PPD</p>
<p>VA-PSA</p>
<p>VA-SEATBELT EDUCATION VA-TOBACCO EDUCATION VA-WEIGHT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Overview of Major Changes</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>CPRS GUI V25 Reminder Dialog Changes</strong></p>
</blockquote>
<ul>
<li><p>PSI-04-001: Template field data not in final note when processing multiple dialogs.</p></li>
<li><p>Fixed the problem introduced with CPRS 24 that caused multiple checkboxes showing for a single element.</p></li>
<li><p>Reminder Dialogs will remember their last position and size.</p></li>
<li><p>Changed reminder dialogs to only look at the Indent Progress Note field when checking to Indent the Progress Note Text. Users will no longer have to set the “PUT A BOX AROUND THE GROUP” to yes to Indent the Progress Note text</p></li>
<li><p>Fixed the problem with certain historical data not updating PCE. Functional Change: changed the OR call to DATA2PCE to not sync Historical Encounter data.</p></li>
</ul>
<blockquote>
<p>Sites will need to perform clean-up to files with any historical data that has not been filed.</p>
</blockquote>
<ul>
<li><p>Removed the Delphi code that requires users to enter Encounter data for a visit. (i.e. Service Connection)</p></li>
</ul>
<blockquote>
<p>Users can still enter encounter data in a Reminder Dialog by clicking on the Visit Info button.</p>
</blockquote>
<ul>
<li><p>New flag added to Reminders 2.0 to control who can access the Print Now functionality for the Women’s Health Review Reminders. When Patch 1 of Clinical Reminders 2.0 is installed, the Print Now functionality will be turned off. To turn it on, the site can use the WH Print Now Active OPTION on the CPRS Reminder Configuration menu.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Purpose_of_This_Guide" class="anchor"></span><strong>Purpose of This Guide</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Purpose of Clinical Reminders Setup Guide</strong></p>
<p>This Setup Guide is designed to help you prepare your site for the implementation of Clinical Reminders V. 2.0. It includes detailed information such as term mapping and extract/transmission of IHD and MH reminder data with Clinical Reminders V. 2.0.</p>
<p><strong>Our Target Audience</strong></p>
<p>We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package:</p>
</blockquote>
<ul>
<li><p>Clinical Application Coordinator (CAC)</p></li>
<li><p>Clinical Reminders Manager</p></li>
<li><p>Enterprise <strong>V</strong><em>IST</em><strong>A</strong> Support (EVS)</p></li>
<li><p>Software Quality Assurance (SQA)</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Other Sources of Information</strong></p>
</blockquote></td>
<td><blockquote>
<p>Refer to the Web sites listed below when you want to receive more background and technical information about PXRM V. 2.0, and to download this manual and related documentation.</p>
<p><strong>Background/Technical Information about Clinical Reminders</strong></p>
<p>From your Intranet, enter <a href="http://vista.med.va.gov/reminders">http://vista.med.va.gov/reminders</a> in the Address field to access the Clinical Reminders Main Web page.</p>
<p><strong>This Manual and Related Documentation</strong></p>
<p>From your Intranet, enter <a href="http://www.va.gov/vdl"><u>http://www.va.gov/vdl</u></a> in the Address field to access this manual, and those listed below, from the <strong>V</strong><em>IST</em><strong>A</strong> Documentation Library (VDL).</p>
</blockquote>
<ul>
<li><p>Install Guide</p></li>
<li><p>Clinician Guide</p></li>
</ul></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Documentation Retrieval Process</strong></p>
</blockquote></th>
<th><blockquote>
<p>Your site can also retrieve the Clinical Reminders V. 2.0 documentation listed below from the following FTP addresses. The preferred method is to “FTP” the files from <a href="ftp://ftp.fo-slc.med.va.gov/"><strong>download.vista.med.va.gov</strong></a>. This location automatically transmits files from the first available FTP Server to the appropriate directory on your system. (See the order listed below under the FTP Address column).</p>
<p><strong>Note:</strong> If you prefer, you can retrieve the software <em>directly</em> from one of the FTP Servers, listed below, under the FTP Address column.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### FTP Addresses Available for Downloading Clinical Reminders V. 2.0 Documentation

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 37%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>OI Field Office</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FTP Address</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Directory</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Albany</p>
</blockquote></td>
<td><mark><u>REDACTED</u></mark></td>
<td><blockquote>
<p><mark><u>REDACTED</u></mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><mark><u>REDACTED</u></mark></td>
<td><mark><u>REDACTED</u></mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark><u>REDACTED</u></mark></td>
<td><mark><u>REDACTED</u></mark></td>
</tr>
</tbody>
</table>
> Clinical Reminders V. 2.0 Documentation and Related File names
<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Manual</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Documentation File name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Installation Guide</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_IG.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Clinician Guide</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_UM.PDF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Setup Guide</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_SG.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Manager’s Manual (available within a few weeks after software release)</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_MM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><p><span id="Impact_on_Sites" class="anchor"></span><strong>Impact on Sites</strong></p>
<blockquote>
<p>Following release of the Clinical Reminders Index and Clinical Reminders 2.0, weekly support calls will be held for one month with HSD&amp;D, EVS and test sites to answer any questions field facilities may have regarding setup and installation.</p>
</blockquote>
<p>NOTE: Data rollup is based on how you map your local findings to the national terms.</p></th>
<th><blockquote>
<p><strong>Pre and Post-Installation Preparation and Setup</strong></p>
</blockquote>
<ul>
<li><p>National Reminder Rescission: Existing national reminders are renamed as part of V. 2.0 installation, using the ZZ- prefix. If you have used this prefix for local reminders, please review them to see if you will need to rename any.</p></li>
<li><p>Locally created computed findings may need to be updated.</p></li>
</ul>
<blockquote>
<p>For a Computed Finding in Clinical Reminders V. 1.5 to work in Clinical Reminders V. 2.0, if a computed reminder returns a TRUE, it must also return a date. Any sites experiencing computed finding errors with Clinical Reminders V. 1.5, should identify and fix the problems prior to installing Clinical Reminders</p>
<p>V. 2.0 into production.</p>
</blockquote>
<ul>
<li><blockquote>
<p>In V. 2.0 the Most Recent Date (MRD) functionality has been replaced with Function Findings (FF). Facilities should review their locally developed reminders and replace MRD with the new FF functionality. See the example in the Install Guide.</p>
</blockquote></li>
<li><blockquote>
<p>Four additional reporting IHD clinical reminders are distributed in version two of Clinical Reminders (PXRM*2.0). The installation installs the reminders into the host system through the reminder exchange utility. Four GEC reminders are also installed.</p>
</blockquote></li>
<li><blockquote>
<p>Other changes made in V. 2.0 may require modifications to some reminder definitions, related to the following:</p>
</blockquote>
<ul>
<li><p>Statuses</p></li>
<li><p>Computed Findings</p></li>
<li><p>Conditions</p></li>
</ul></li>
<li><blockquote>
<p>Term Mapping: As with all National Reminders, the IHD reminders are all built with reminder terms instead of individual health factors or other finding types. This allows a site to continue to use findings that already exist on the host system as data elements and to relate these local findings to the national terms. The individual health factors that match the reminder term are also distributed with the patch, so that a site that does not have a local finding can use the nationally distributed health factors to collect data. A detailed description of each distributed reminder’s term is included in the reminder description.</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Impact on Sites</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pre and Post-Installation, cont’d</strong></p>
</blockquote>
<ul>
<li><p><strong>Term Mapping, cont’d</strong></p></li>
</ul>
<blockquote>
<p>Phase II reminders includes all the terms released in Phase 1, as well as four new terms introduced for the reporting reminders. The new terms will require mapping, and if your site didn’t map terms for Phase 1, many of those will also require mapping.</p>
</blockquote>
<ul>
<li><p>Review patient lists and extract reports for reporting compliance totals using Reminder Patient List and Extract Management options.</p></li>
<li><p>Set up VA Geriatric Extended Care Referral (GEC) reminders and dialogs.</p></li>
<li><blockquote>
<p>Review Code Set Versioning messages, when they are received, and determine if modifications need to be made to Reminder Taxonomies.</p>
</blockquote></li>
<li><blockquote>
<p>QUERI extracts and transmissions</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>What sites will need to do to catch up to date on the QUERI extracts and transmissions if 2.0 is not installed into production in January 2005.</strong></p>
<p>The first extract period is January 2005, so sites have until the first 10 days to run the extract through TaskMan to be okay.</p>
<p>The extract parameters for VA-IHD QUERI and VA-MH QUERI will be released with the next reporting period for January 2005. So when sites run the extract for the first time using TaskMan to schedule the option, it will run the extract for January 2005. When this job is completed, the extract code will automatically change the next reporting period to February 2005. And when sites run the extract again using TaskMan to schedule the PXRM extract options, the extract will run against the month of February. So for every month that sites miss running the extract, they will need to schedule an auto-run using TaskMan and the PXRM extract options to schedule the job. They will need to do this for each month that they miss, to get caught up.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Impact on Sites</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pre and Post-Installation, cont’d</strong></p>
</blockquote>
<ul>
<li><p>QUERI extracts and transmissions, cont’d</p></li>
</ul>
<blockquote>
<p><strong>Catching up on the QUERI extracts and transmissions: Example</strong></p>
<p>Site A - to start running extract in March</p>
<p>They will need to schedule the extract option using FileMan for one time before running the March job. Once the first job is completed, they will then need to schedule the recurring extract option to run once a month, starting at the beginning of March. The first job will run the extract for the month of January; when that job is completed, the extract will then be set to run for the month of February. The first job will get them caught up.</p>
<p>Site B - to start running extract in April,</p>
<p>This site will need to run two TaskMan jobs for the extract option; this will then get them caught up to start recurring jobs.</p>
<p>Site C – to start running extract in May</p>
<p>This site will need to run three TaskMan jobs for the extract option; this will then get them caught up to start recurring jobs.</p>
<p>If a site needs to run the extract for multiple periods to get caught up, we recommend that the site schedule the extract to run one a day for the number of days to get caught up. Once the site is caught up. the site can then reschedule the extract option to run monthly. The option to schedule a task for an option is: 'Schedule/Unschedule Options'</p>
<p>Option name: XUTM SCHEDULE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Part II: Setup Procedures 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Chapter_1:_IHD_and_MH_Phase_2_Setup" class="anchor"></span><strong>Chapter 1: IHD and MH Phase 2 Setup</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Overview</strong></p>
<p><strong>IHD Reminder Definitions</strong></p>
<p>The following IHD reminder definitions are distributed with Version</p>
<p>2.0 of Clinical Reminders:</p>
<p><strong>VA-IHD LIPID PROFILE</strong></p>
<p>This national reminder identifies patients with known IHD (i.e., a documented ICD-9 code for IHD on or after 10/01/99) who have not had a serum lipid panel within the last year. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.</p>
<p><strong>VA-IHD ELEVATED LDL</strong></p>
<p>This national reminder identifies patients with known IHD (i.e., a documented ICD-9 code on or after 10/01/99) who have had a serum lipid panel within the last year, where the most recent LDL lab test (or documented outside LDL) is greater than or equal to 120 mg/dl. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.</p>
<p><strong>VA-*IHD LIPID PROFILE REPORTING</strong></p>
<p>This national IHD Lipid Profile Reporting reminder is used monthly to roll up LDL compliance totals for IHD patients. This reminder identifies patients with known IHD (i.e., a documented ICD-9 code for IHD) who have not had a serum lipid panel/LDL (calculated or direct lab package LDL) or documented outside LDL within the last two years. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.</p>
<p><strong>VA-*IHD ELEVATED LDL REPORTING</strong></p>
<p>This national IHD Elevated LDL Reporting reminder is used monthly to roll up compliance totals for management of IHD patients whose most recent LDL is greater than or equal to 120mg/dl. This national reminder identifies patients with known IHD (i.e., a documented</p>
<p>ICD-9 code) who have had a serum lipid panel within the last two years, where the most recent LDL lab test (or documented outside LDL) is greater than or equal to 120 mg/dl. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient. These compliance reminders are not for use in the Computerized Patient Record System (CPRS), so there are no related reminder dialogs.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NOTE: There are still discrepancies between the guidelines in these reminders and the EPRP guidelines. The QUERI group and the Reminder Definition developers are striving to reconcile the differences, as more information becomes available.</p>
</blockquote></th>
<th><blockquote>
<p><strong>IHD Reminders, cont’d</strong></p>
<p><strong>VA-*IHD 412 LIPID PROFILE REPORTING</strong></p>
<p>This national IHD 412 Lipid Profile Reporting reminder is used monthly to roll up LDL compliance totals for IHD 412 patients. This reminder identifies patients with known IHD 412.nn (i.e., a documented ICD-9 code for IHD 412.nn) who have not had a serum lipid panel/LDL (calculated or direct lab package LDL or documented outside LDL) within the last two years. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.</p>
<p><strong>VA-*IHD 412 ELEVATED LDL REPORTING</strong></p>
<p>This national IHD 412 Elevated LDL Reporting reminder is used quarterly to roll up compliance totals for management of IHD (412.nn) patients whose most recent LDL is greater than or equal to 120mg/dl. This reminder identifies patients with known IHD (i.e., a documented 412.nn ICD-9 code on or after 10/01/99) who have had a serum lipid panel within the last two years, where the most recent LDL lab test (or documented outside LDL) is greater than or equal to 120 mg/dl. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.</p>
<p><strong>Mental Health Reminders</strong></p>
<p>The following MH reminder definitions are re-distributed with Version 2 of Clinical Reminders:</p>
<p><strong>VA-ANTIPSYCHOTIC MED SIDE EFF EVAL</strong></p>
<p>The AIMS reminder has been designed to be due on all patients who are on any one of the antipsychotic medications (excluding ones like Compazine). The taxonomy for Schizophrenia is included in the reminder, but will not be part of the cohort logic. By leaving the taxonomy in the reminder, data roll-up can use the Report Extracts functionality in version 2, either with or without information on patients with Schizophrenia.</p>
<p><strong>VA-DEPRESSION SCREENING</strong></p>
<p>Screening for Depression using a standard tool should be done on a yearly basis. The yearly screening is satisfied by entry of a health factor indicating positive or negative results for the 2 question MacArthur screening tool or by entry of negative or positive results in the MH package. The reminder is also resolved by entry of information indicating that the patient is already being</p>
<p>treated/evaluated in a Mental Health clinic.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Mental Health Definitions (cont’d)

> VA-DEPRESSION SCREENING, cont’d

> Patients are automatically excluded from the cohort if they have a recent diagnosis of depression (ICD code in the past 1 year) and have either a CPT code for psychotherapy in the past 3 months or are on antidepressant medication (current supply of medication in the past 3 months).

#### VA-POS DEPRESSION SCREEN FOLLOWUP

> The reminder is applicable if the patient has positive depression screen in the past 1 year (VA-DEPRESSION SCREEN POSITIVE). If a more recent negative depression screen is entered, then the reminder becomes not applicable (VA- DEPRESSION SCREEN NEGATIVE).

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Setup_Steps" class="anchor"></span><strong>Setup Steps</strong></p>
<p><strong>TIP:</strong></p>
</blockquote>
<p> See the Clinical Reminders V. 2.0</p>
<blockquote>
<p>Installation Guide for install and post-install steps; for example, verifying that reminders and dialogs were installed.</p>
</blockquote></th>
<th><blockquote>
<p><strong>1. Map local findings to the national Reminder Terms.</strong></p>
<p><em>Option: Reminder Term Edit on the Reminder Term Management menu</em> on the <em>Reminder Management Menu.</em></p>
<p>Before using IHD and MH reminders, map the local findings your site uses to represent the national reminder terms.</p>
<p>Phase II reminders include all the terms released in Phase I. If your site hasn’t mapped these terms, several will require mapping, and others can be mapped if needed, to use local health factors. See the examples on following pages, if you need instructions.</p>
<p><strong>a. IHD reminder terms</strong></p>
<p>Four new terms that will require mapping are introduced for the IHD reporting reminders: VA-LDL&gt;129, VA-LDL &lt;100, VA- LDL 100-119, VA-LDL 120-129</p>
<p>The IHD reminders use reminder terms instead of individual health factors or other finding types, which lets you continue to use findings that may already exist in your system as data elements. These local findings can then be mapped to the national terms. The individual health factors that match the reminder term are also distributed with the patch, so that a site that doesn’t have local findings can use the nationally distributed health factors to collect data.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> IHD terms that *must* be mapped (no mapping included with distributed terms).

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 50%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Mapping Instructions</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Local Lab Tests or Orderables to Map</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>VA-LDL</strong></p>
</blockquote></td>
<td><blockquote>
<p>Enter the Laboratory Test names from the Lab</p>
<p>Package for calculated LDL and direct LDL.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA LDL</strong></p>
<p><strong>&lt;100</strong></p>
</blockquote></td>
<td><blockquote>
<p>Enter the Laboratory Test names from the Lab</p>
<p>Package for calculated LDL and direct LDL with a CONDITION to identify LDL values &lt;100.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA LDL 100- 119</strong></p>
</blockquote></td>
<td><blockquote>
<p>Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a</p>
<p>CONDITION to identify LDL values from 100- 119.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-LDL &gt;119</strong></p>
</blockquote></td>
<td><blockquote>
<p>Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a CONDITION to identify LDL values &gt; 119. Although the condition is defined in the reminder, also define the condition in the term so the term can be used for uses that don't involve the reminder definition. If your site uses comments frequently you may want to</p>
<p>change the condition to check for specific text.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

#### IHD terms that *must* be mapped (no mapping included with distributed terms):

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 47%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Mapping Instructions</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Local Lab Tests or Orderables to Map</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>VA-LDL &lt; 120</strong></p>
</blockquote></td>
<td><blockquote>
<p>Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a CONDITION to identify LDL values &lt;120.</p>
<p>Although the condition is defined in the reminder, also define the condition in the term so the term can be used for purposes that don't involve the reminder definition. If your site uses comments frequently you may want to change the condition to check for</p>
<p>specific text.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-LDL &gt;129</strong></p>
</blockquote></td>
<td><blockquote>
<p>Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a</p>
<p>CONDITION to identify LDL values &gt; 129.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-LDL 120-</strong></p>
<p><strong>129</strong></p>
</blockquote></td>
<td><blockquote>
<p>Enter the Laboratory Test names from the Lab</p>
<p>Package for calculated LDL and direct LDL with a CONDITION to identify LDL values 120-129.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-LIPID PROFILE ORDERABLE</strong></p>
</blockquote></td>
<td><blockquote>
<p>Add local orderable items that your site uses to order direct LDL and calculated LDL lab tests (including lipid profiles with an LDL). Add the</p>
<p>order dialog item to the reminder dialog definition.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Pre-mapped Terms (additional mapping optional)

> If desired, add local Health Factors or findings representing these terms.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 43%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Local Health Factors to Map</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>VA-IHD DIAGNOSIS</strong></p>
</blockquote></td>
<td><blockquote>
<p>No mapping is necessary. This term is distributed pre-mapped to the VA-ISCHEMIC HEART DISEASE taxonomy. The Active Problem list, Inpatient Primary Diagnosis and</p>
<p>Outpatient Encounter Diagnosis are used to search for ICD9 diagnoses.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-LIPID LOWERING MEDS</strong></p>
</blockquote></td>
<td><blockquote>
<p>This term is distributed pre-mapped to VA Generic Drug Names. Add any investigational drug names that are used but not mapped to the VA-Generic Drug. Enter the formulary drug names for investigation drugs.</p>
<p>Mapping non-investigative formulary drugs to the VA-GENERIC drugs in the Pharmacy Package will ensure the lipid lowering agents are found. The medications are informational</p>
<p>findings for this reminder.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

#### Pre-mapped Terms (additional mapping optional), cont’d

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 45%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Local Health Factors to Map</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>VA-LIPID LOWERING THERAPY MGMT – 2M</strong></p>
</blockquote></td>
<td><blockquote>
<p>The LIPID LOWERING MEDS INITIAL ORDER and LIPID LOWERING MEDS</p>
<p>ADJUSTED health factors are distributed pre- mapped to this term. If necessary, add local health factors representing these terms. Do not add orders or pharmacy medications as findings for</p>
<p>this term.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-LIPID LOWERING THERAPY MGMT – 6M</strong></p>
</blockquote></td>
<td><blockquote>
<p>The NO CHANGE IN IHD LIPID TREATMENT, OTHER DEFER ELEVATED LDL THERAPY, and LIPID MGMT</p>
<p>PROVIDED OUTSIDE health factors are distributed pre-mapped to this term. Add any local health factors, such as life expectancy &lt; 6 months, which your site is using that should defer</p>
<p>the lipid lowering management.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-LIPID MEDS CONTRAINDI-CATED</strong></p>
</blockquote></td>
<td><blockquote>
<p>Use the LIPID MEDS CONTRAINDICATED</p>
<p>health factor distributed with this term or add any local health factors representing contraindication to lipid lowering medications</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-ORDER LIPID PROFILE HEALTH FACTOR</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: ORDER LIPID PROFILE. Add any local health factor representing the order action. Do not add orderable items to this reminder term (see VA-LIPID</p>
<p>PROFILE ORDERABLE).</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-OTHER DEFER LIPID PROFILE</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: OTHER DEFER LIPID PROFILE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-OUTSIDE LDL &lt;100</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: OUTSIDE LDL</p>
<p>&lt;100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-OUTSIDE LDL &gt;129</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: OUTSIDE LDL</p>
<p>&gt;129</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-OUTSIDE LDL 100-</strong></p>
<p><strong>119</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: OUTSIDE LDL 100-119</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-OUTSIDE LDL 120-</strong></p>
<p><strong>129</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: OUTSIDE LDL 120-129</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-REFUSED</strong></p>
<p><strong>ELEVATED LDL THERAPY</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: REFUSED ELEVATED</p>
<p>LDL THERAPY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-REFUSED LIPID PROFILE</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: REFUSED LIPID PROFILE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-TRANSFERASE (AST) (SGOT)</strong></p>
</blockquote></td>
<td><blockquote>
<p>This term was distributed originally with the Hepatitis C Risk Assessment reminder. AST tests</p>
<p>should already be mapped at your site.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-UNCONFIRMED IHD DIAGNOSIS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Use the UNCONFIRMED IHD DIAGNOSIS</p>
<p>health factor distributed with this term or add any</p>
<p>local health factor representing an unconfirmed or incorrect IHD diagnosis.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Setup Steps</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Example: Mapping a Local Finding to the LDL Reminder Term</strong></p>
<p>Determine all labs tests that mean “LDL” LDL (CALCULATED) DIRECT LDL</p>
<p>NOTE: You can’t map panels -- only individual tests. Examples:</p>
<p>LDL CHOLESTEROL</p>
<p>LDL CHOLESTEROL, PASCO LDL, DIREC</p>
<p>NOTE: The reminder definition “LDL” finding contains the condition "I +V&gt;0." The “+” causes the result to be treated as a number. If it’s only text, it will treat it as a zero. This condition can be added to the reminder term also, if desired, but it isn’t necessary.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Mapping a local finding to an LDL Term

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Setup Steps</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>1. Map local findings to the national Reminder Terms (cont’d).</strong></p>
</blockquote>
<ol start="2" type="a">
<li><p><strong>Mental Health Reminder Terms</strong></p>
<ul>
<li><p>VA-DEPRESSION SCREENING Terms</p></li>
</ul></li>
</ol>
<blockquote>
<p>Sites that use a different screening tool than the 2-question MacArthur screening tool will need to create local health factors to indicate a positive or negative result and will need to map those local health factors to the national terms:</p>
</blockquote>
<ul>
<li><blockquote>
<p>VA-DEPRESSION SCREEN NEGATIVE</p>
</blockquote></li>
<li><blockquote>
<p>VA-DEPRESSION SCREEN POSITIVE</p>
</blockquote></li>
</ul>
<blockquote>
<p>Reminder terms are included in this reminder to indicate if patients cannot be screened due to an acute or chronic medical condition.</p>
</blockquote>
<ul>
<li><blockquote>
<p>VA-ACUTE MEDICAL CONDITION</p>
</blockquote></li>
<li><blockquote>
<p>VA-CHRONIC MEDICAL CONDITION</p>
</blockquote></li>
</ul>
<blockquote>
<p>The health factors for these terms are:</p>
</blockquote>
<ul>
<li><p>UNABLE TO SCREEN-ACUTE MED CONDITION (resolves the reminder for 3M)</p></li>
<li><p>UNABLE TO SCREEN-CHRONIC MED CONDITION (resolves the reminder for1Y).</p></li>
</ul>
<blockquote>
<p>The reminder term, DEPRESSION SCREEN DONE RESULT UNKNOWN, is included for sites where a health factor or exam is being collected to indicate that depression screening is being done using an appropriate tool, but the result (positive or negative) is not being recorded. This term is included ONLY to allow sites to make the conversion to collecting positive and negative screens—any health factors or exams that a site maps to this term should NOT be included for use on any dialog or on an encounter form and should not be used in the future.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### MH Term Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If desired, add local Health Factors, orderables, or findings representing these terms.

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Mapping</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-ACUTE MEDICAL CONDITION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-AIM EVALUATION NEGATIVE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-AIM EVALUATION POSITIVE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-ANTIDEPRESSANT MEDICATIONS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-ANTIPSYCHOTIC DRUGS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-CHRONIC MEDICAL CONDITION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-DEPRESSION ASSESS COMPLETED IN MHC</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-DEPRESSION ASSESS INCONCLUSIVE (? MDD)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-DEPRESSION ASSESS NEGATIVE (NOT MDD)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-DEPRESSION ASSESS POSITIVE (MDD)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-DEPRESSION DIAGNOSIS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-DEPRESSION SCREEN DONE RESULT UNKNOWN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-DEPRESSION SCREEN NEGATIVE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-DEPRESSION SCREEN POSITIVE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-DEPRESSION THERAPY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-DEPRESSION TO BE MANAGED IN PC</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-NO DEPRESSIVE SX NEED INTERVENTION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-PSYCHOTHERAPY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-REFERRAL TO MENTAL HEALTH</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-REFUSED AIM EVALUATION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-REFUSED ANTIPSYCHOTICS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-REFUSED DEPRESSION ASSESSMENT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-REFUSED DEPRESSION RX/INTERVENTION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-REFUSED DEPRESSION SCREENING</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-SCHIZOPHRENIA DIAGNOSIS</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

### Example: Mapping a local finding to a Depression Screening Term

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="2.__Run_the_Reminder_Test_option_after_t" class="anchor"></span><strong>Setup Steps, cont’d</strong></p>
</blockquote></th>
<th><ol start="2" type="1">
<li><blockquote>
<p><strong>Run the Reminder Test option after term definition mapping is completed.</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>Review the results of patient data with each of the findings mapped to the term.</p>
<p><em>Option: Reminder Test</em> on the <em>Reminder Managers Menu</em></p>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p><strong>Enter data through reminder dialogs to have information that can be used to test the extract functionality.</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>You may also enter data through the List Manager version of CPRS or other VISTA applications, such as Lab.</p>
</blockquote>
<ol start="4" type="1">
<li><blockquote>
<p><strong>Run a Reminders Due Report for a test period of time to determine if the patients who are reported are appropriate.</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>The report could be run for a national reminder, or create local reminders with one reminder term defined as a patient cohort finding item, then run the report to get findings by individual reminder term.</p>
<p><em>Option: Reminders Due Report on the Reminder Reports menu</em></p>
</blockquote>
<ol start="5" type="1">
<li><blockquote>
<p><strong>Initiate a manual run from Reminder Extract Management</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p><strong>– without transmitting.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Example: Manual Extract

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 10%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Reminder Managers Menu Option: <strong>XM</strong> Reminder Extract Menu</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MA Reminder Extract Management</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EP Extract Parameter Management</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EF Extract Finding Management</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EG Extract Finding Group Management</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LR List Rule Management</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Reminder Extract Menu Option: <strong>MA</strong> Reminder Extract Management</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Extract/Transmissions Mgmt</strong>. May 24, 2004@10:41:35 Page:</p>
</blockquote></td>
<td><blockquote>
<p>1 of</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Available Extract Parameters:</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Item Extract Type</p>
</blockquote></td>
<td><blockquote>
<p>Class</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 BP READING</p>
</blockquote></td>
<td><blockquote>
<p>LOCAL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2 VA-IHD QUERI</p>
</blockquote></td>
<td><blockquote>
<p>NATIONAL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3 VA-MH QUERI</p>
</blockquote></td>
<td><blockquote>
<p>NATIONAL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>EPM Extract Parameter Management QU Quit VSE View/Schedule Extract</p>
<p>Select Item: Quit// 2</p>
<p>Select Action: (EPM/VSE): VSE// <strong>&lt;Enter&gt;</strong> Examine/Schedule Extract</p>
</blockquote></td>
</tr>
</tbody>
</table>

*Example continued next page*

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Setup Steps, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>5. (cont’d) Initiate a manual run from Reminder Extract Management – without transmitting</strong>.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Example: Manual Extract

<table>
<colgroup>
<col style="width: 94%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Examine/Schedule Extract</strong> May 24, 2004@10:41:48 Page: 1 of 4</p>
<p>Extract Type: VA-IHD QUERI Next Extract Period: M6/2001</p>
<p>Scheduled to Run: View: Creation Date Order</p>
<p>Item Extract Summary Date Created Transmission Date Auto 1 VA-IHD QUERI 2001 M1/08 05/14/2004@15:00:42 Not Transmitted N</p>
</blockquote>
<p>3 VA-IHD QUERI 2001 M6/14 04/27/2004@11:58:53 Not Transmitted N</p>
<p>7 VA-IHD QUERI 2004 M2 02/18/2004@15:04:14 03/03/2004@11:41:19 N</p>
<p>9 VA-IHD QUERI 2001 M6/12 02/17/2004@16:00:02 Not Transmitted N</p>
<p>11 VA-IHD QUERI 2001 M6/10 12/08/2003@16:23:20 Not Transmitted N</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CV Change View ME Manual Extract TH Transmission History</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ES Extract Summary MT Manual Transmission QU Quit</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Item: Quit// <strong>me</strong> Manual Extract</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Select EXTRACT PERIOD (Mnn/yyyy): M6/2001// <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Are you sure you want to run a VA-IHD QUERI extract for M6 2001: N// <strong>YES</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transmit extract results to AAC : N// <strong>&lt;Enter&gt;</strong>O</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Queue a Reminder Extract VA-IHD QUERI for M6/2001</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Enter the date and time you want the job to start.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>It must be on or after 05/24/2004@14:03:36 <strong>05/24/2004@14:04</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Task number 5352505 queued.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Extract/Transmissions Mgmt.</strong> May 24, 2004@14:04:36 Page: 1 of</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Available Extract Parameters:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Item Extract Type Class</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 BP READING LOCAL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>2 VA-IHD QUERI NATIONAL</td>
<td></td>
</tr>
<tr class="odd">
<td>3 VA-MH QUERI NATIONAL</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>EPM Extract Parameter Management QU Quit VSE View/Schedule Extract</p>
<p>Select Item: Quit// 2</p>
<p>Select Action: (EPM/VSE): VSE// <strong>&lt;Enter&gt;</strong> Examine/Schedule Extract</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="6.___Review_the_content_of_the_Extract_S" class="anchor"></span><strong>Setup Steps, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>6. Review the content of the Extract Summary.</strong></p>
<p>Use the Reminder Extract Management option, to review extracted findings based on the reminder definitions</p>
<p>Check to see if the numbers match those for step 4. Alternatively, run the Reminder Report option Extract QUERI Totals or a Health Summary to review the findings extracted.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Examine/Schedule Extract

<table>
<colgroup>
<col style="width: 90%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Extract/Transmissions Mgmt. May 24, 2004@14:04:47 Page: 1 of 1</p>
<p>Available Extract Parameters:</p>
<p>Item Extract Type Class</p>
</blockquote>
<ol type="1">
<li><p>VA-IHD QUERI NATIONAL</p></li>
<li><p>VA-MH QUERI NATIONAL</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EPM Extract Parameter Management QU Quit</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VSE View/Schedule Extract</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Item: Quit// 1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Select Action: (EPM/VSE): VSE// Examine/Schedule Extract</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Examine/Schedule Extract May 24, 2004@14:04:47 Page: 1 of</p>
</blockquote></td>
<td>4</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Extract Type: VA-IHD QUERI</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Next Extract Period: M6/2001</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Scheduled to Run: View: Creation Date Order</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Item Extract Summary Date Created Transmission Date</p>
</blockquote></td>
<td>Auto</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 VA-IHD QUERI 2001 M6/15 05/24/2004@14:04:19 Not Transmitted</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3 VA-IHD QUERI 2001 M1/07 04/27/2004@13:05:32 Not Transmitted</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>CV Change View ME Manual Extract TH Transmission History</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>ES Extract Summary MT Manual Transmission QU Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Select Item: Next Screen// 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Select Action: (ES/MT/TH): ES// Extract Summary</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Extract Summary May 24, 2004@14:05:18 Page: 1 of 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Extract Summary Name: VA-IHD QUERI 2001 M6/15</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Extract Period: 06/01/2001 - 06/30/2001 Created: 05/24/2004@14:04:19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Item Patient List/Station/Reminder Total Appl. N/A Due Not Due</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>1 VA-*IHD QUERI 2001 M6 PTS WITH QUALIFY VISIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>660/VA-IHD LIPID PROFILE 2 2 0 0 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>660/VA-IHD ELEVATED LDL 2 2 0 1 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>6028/VA-IHD LIPID PROFILE 2 2 0 0 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>6028/VA-IHD ELEVATED LDL 2 0 2 0 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>2 VA-*IHD QUERI 2001 M6 PTS WITH QUALIFY AND ANCHOR VISIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>660/VA-*IHD LIPID PROFILE REPORTING 2 2 0 0 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>660/VA-*IHD ELEVATED LDL REPORTING 2 2 0 2 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>DPL Display Patient List QU Quit DSF Display/Suppress Finding Totals</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="7.__Run_a_reminder_report_for_the_patien" class="anchor"></span><strong>Setup Steps, cont’d</strong></p>
</blockquote></th>
<th><ol start="7" type="1">
<li><p><strong>Run a reminder report for the patient lists created from the extract and compare due totals to the extract summary.</strong></p></li>
</ol>
<blockquote>
<p>For example, run a report for reminder VA-IHD ELEVATED LDL against patient list VA-*IHD QUERI yyyy Mnn PTS WITH QUALIFY VISIT</p>
</blockquote>
<ol start="8" type="1">
<li><blockquote>
<p><strong>Turn on the logical Link in the HL7 package.</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>Before the IHD HL7 messages can be transmitted to Austin, each site most turn on the logical Link in the HL7 package in their production account. Enter PXRM7 at the HL LOGICAL LINK prompt, and accept the default of “Background” as the method for running the receiver.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Setting HL Logical Link

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Setup Steps, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>8. Editing the Logical Link in the HL7 package.</strong></p>
<p>If the link goes down for some reason (such as after standalone backups), check with your IRM service. You can re-set the link using the option shown on the previous page.</p>
<p>If you need to edit the link or reset the link to Autostart, use the “Link Edit” option, on the Interface Developer Options menu, as shown below:</p>
<p>For more information about Logical Links, see the VistA Health Level Seven (Hl7) Site Manager &amp; Developer Manual.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <span id="_bookmark9" class="anchor"></span>Setup Procedures (cont’d)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Setup Steps, cont’d</strong></p>
<p><strong>TIP:</strong></p>
<p> Programmer access is usually</p>
<p>required to use Taskman options.</p>
</blockquote></th>
<th><blockquote>
<p><strong>9. Initiate the production account run of the Automatic</strong></p>
<p><strong>QUERI Extracts/ Transmission.</strong></p>
<p>The automatic monthly extract of QUERI information is initiated from the options PXRM EXTRACT VA-IHD QUERI and PXRM VA-MH QUERI. These are activated through TaskMan options.</p>
<p>Use Schedule/Unschedule Options on the Taskman Management menu to schedule the PXRM VA-IHD QUERI and PXRM VA-MH QUERI options.</p>
<p><strong>Example: Scheduling the PXRM VA-IHD QUERI option</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Select OPTION NAME: <strong>XUTM MGR</strong> Taskman Management menu</p>
<p>Schedule/Unschedule Options One-time Option Queue</p>
<p>Taskman Management Utilities ... List Tasks</p>
<p>Dequeue Tasks Requeue Tasks Delete Tasks</p>
<p>Print Options that are Scheduled to run Cleanup Task List</p>
<p>Print Options Recommended for Queueing</p>
<p>Select Taskman Management Option: <strong>Schedule/Unschedule Options</strong></p>
<p>Select OPTION to schedule or reschedule: <strong>PXRM EXTRACT VA-IHD QUERI</strong> VA-IHD QUERI Extract run routine</p>
<p>Are you adding 'PXRM EXTRACT VA-IHD QUERI' as</p>
<p>a new OPTION SCHEDULING (the 50TH)? No// <strong>Y</strong> (Yes)</p>
<p>Edit Option Schedule Option Name: PXRM EXTRACT VA-IHD QUERI</p>
<p>Menu Text: VA-IHD QUERI Extract TASK ID:</p>
<p>QUEUED TO RUN AT WHAT TIME: JAN 10,2005@00:01</p>
<p>DEVICE FOR QUEUED JOB OUTPUT: Add note about what month to</p>
<p>QUEUED TO RUN ON VOLUME SET: start with; also about manually running Jan, if v2 not installed</p>
<p>RESCHEDULING FREQUENCY: 1M until Feb</p>
</blockquote>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING:</p>
<blockquote>
<p><strong>COMMAND: Press &lt;PF1&gt;H for help Insert</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark10" class="anchor"></span><strong>Setup Steps, cont’d</strong></p>
<p><strong>TIP:</strong></p>
<p> You can also get a list of the</p>
<p>extract totals with a new report on the Reminder Reports menu, Extract QUERI Totals.</p>
</blockquote></th>
<th><ol start="10" type="1">
<li><blockquote>
<p><strong>Examine the patient lists from the first auto extract and run either Health Summary or Reminder Reports from them.</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>Check to see if the numbers match those for step 4 and step 8.</p>
</blockquote>
<ol start="11" type="1">
<li><blockquote>
<p><strong>Review the Transmission History.</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>This displays the transmission times and individual HL7 messages and statuses for the selected extract summary.</p>
</blockquote>
<ol start="12" type="1">
<li><blockquote>
<p><strong>After the first run is completed, review the content of the mail messages created</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>Use the “Display/Suppress Findings Totals” action on the Reminder Extract Management option to review the findings extracted based on the reminder definitions.</p>
<p>Make sure that the mail messages and the findings include all the correct information from the IHD and MH reminder definitions.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Display Finding Totals

<table style="width:100%;">
<colgroup>
<col style="width: 75%" />
<col style="width: 9%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Examine/Schedule Extract May 24, 2004@14:53:20 Page: 1 of</p>
<p>Extract Type: VA-MH QUERI Next Extract Period:</p>
<p>Scheduled to Run: View: Creation Date Order</p>
<p>Item Extract Summary Date Created Transmission Date</p>
<p>1 VA-MH QUERI 2003 M11/04 12/18/2003@18:00:20 12/18/2003@18:00:27</p>
<p>2 VA-MH QUERI 2001 M10 11/26/2003@12:37:30 Not Transmitted</p>
<p>3 VA-MH QUERI 2003 M11/02 11/26/2003@09:43:37 Not Transmitted</p>
<p>4 VA-MH QUERI 2000 M2/01 09/08/2003@15:49 Not Transmitted</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
<p>Auto N N N</p>
<p>N</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>CV Change View ME Manual Extract TH Transmission History</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>ES Extract Summary MT Manual Transmission QU Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Select Item: Next Screen// <strong>ES</strong> Extract Summary</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Select (s): (1-11): <strong>1</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Extract Summary May 24, 2004@14:53:35 Page: 1 of 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Extract Summary Name: VA-MH QUERI 2003 M11/04</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Extract Period: 11/01/2003 - 11/30/2003 Created: 12/18/2003@18:00:20</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Item Patient List/Station/Reminder Total Appl. N/A Due Not Due</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>1 VA-*MH QUERI 2003 M11 QUALIFYING PC VISIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>660/VA-DEPRESSION SCREENING 4 4 0 2 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>660/VA-POS DEPRESSION SCREEN FOLLOWU 4 1 3 1 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DPL Display Patient List QU Quit</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DSF Display/Suppress Finding Totals</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Item: Quit// <strong>DSF</strong></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DSF Display/Suppress Finding Totals</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 VA-MH QUERI 2000 M2 QUALIFYING VISIT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>660/VA-DEPRESSION SCREENING 1000 899 101</td>
<td>200</td>
<td>699</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Finding Group: VA-DEPRESSION SCREEN NON APPLICABLE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Most recent finding patient counts for TOTAL patients</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>DEPRESSION DIAGNOSIS 20 20 0</td>
<td>20</td>
<td>0</td>
</tr>
<tr class="odd">
<td>PSYCHOTHERAPY 0 0 0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td>ANTIDEPRESSANT MEDICATION 0 0 0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Finding Group: VA-DEPRESSION SCREEN RESULT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Most recent finding patient counts for APPLICABLE patients</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DEPRESSION SCREEN NEGATIVE 0 0 0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td>DEPRESSION SCREEN POSITIVE 0 0 0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DSF Display/Suppress Finding Totals</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Item: Next Screen// NEXT SCREEN</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Finding Group: VA-REFUSED DEPRESSION SCREEN</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Most recent finding counts for TOTAL patients</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>REFUSED DEPRESSION SCREENING 0 0 0</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

> Example: Display Finding Totals, CONT’D

<table style="width:100%;">
<colgroup>
<col style="width: 55%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEPRESSION SCREEN NEGATIVE</p>
</blockquote></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th>0</th>
<th>0</th>
<th colspan="2"><blockquote>
<p>0</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DEPRESSION ASSESS INCONCLUSIVE</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td colspan="2"><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REFERRAL TO MENTAL HEALTH</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td colspan="2"><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DEPRESSION TO BE MANAGED IN PC</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td colspan="2"><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>660/VA-ANTIPSYCHOTIC MED SIDE EFF EV</p>
</blockquote></td>
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>997</td>
<td>1</td>
<td colspan="2"><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>DSF Display/Suppress Finding Totals Select Item: Next Screen// NEXT SCREEN</p>
<p>Extract Summary Jan 08, 2003@09:49:15 Page: 3 of 3</p>
<p>Extract Summary Name: VA MH QUERI 2000 M2</p>
<p>Extract Period: 02/01/2000 - 02/28/2000 Created: 01/03/2003</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>+Item Patient List/Station/Reminder</p>
</blockquote></td>
<td>Total</td>
<td><blockquote>
<p>Appl.</p>
</blockquote></td>
<td>N/A</td>
<td>Due</td>
<td><blockquote>
<p>Not</p>
</blockquote></td>
<td><blockquote>
<p>Due</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Finding Group: VA-ANTIPSYCHOTIC DRUGS</p>
<p>Most recent finding patient counts for</p>
</blockquote></td>
<td><blockquote>
<p>TOTAL</p>
</blockquote></td>
<td><blockquote>
<p>patients</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AIM EVALUATION NEGATIVE</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AIM EVALUATION POSITIVE</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REFUSED ANTIPSYCHOTICS</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REFUSED AIM EVALUATION</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="Chapter_2:_GEC_Setup" class="anchor"></span>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
<p>NOTES:</p>
</blockquote>
<ul>
<li><p>Dialog elements that have an order associated as a finding item will continue to be editable fields using the dialog editor.</p></li>
<li><p>Any local changes to the GEC dialogs will not be included with the reports or future national extracts.</p></li>
<li><p>GEC health factors are populated with a synonym for identification.</p></li>
<li><p>Although it’s technically possible, sites should not use the GEC health factors elsewhere. Phase II of the GEC project will involve national roll-up. Potential extraction rules may not be able to distinguish the data source.</p></li>
<li><blockquote>
<p>Users should not enter GEC health factors from the Encounter form. While it is possible to do so, Patient Care Encounter only allows one instance of a combination of the health factor, patient, and visit IEN. If one is entered via the Encounter, any subsequent entry of that health factor from the reminder dialog will not be available for the GEC reports. This is a consequence of the GEC report routines relying on the health factor’s Data Source.</p>
</blockquote></li>
</ul></th>
<th><blockquote>
<p><strong>Overview of VA-Geriatric Extended Care (GEC)</strong></p>
<p><strong>Basics</strong></p>
<p>The GEC Referral is comprised of four reminder dialogs: VA-GEC SOCIAL SERVICES, VA-GEC NURSING ASSESSMENT, VA- GEC CARE RECOMMENDATIONS, and VA-GEC CARE</p>
<p>COORDINATION. These dialogs are designed for use as TIU templates to enter data regarding the need for extended care. Data entered via the dialogs are captured as health factors to be used for local and national reporting.</p>
<p>The software also includes a new report menu that may be used for local analysis.</p>
<p><strong>GEC Health Factors</strong></p>
<p>The GEC Referral project distributes a large set of national health factors. They may be identified by the GEC namespace and constitute the foundation of the GEC Referral project. They establish a standard set of screening data, to be used across the Veterans Health Administration, and will be rolled-up nationally.</p>
<p>The Health Factor files include factors and categories. All factors must belong to a category. For this project, each section of the Referral is correlated to a health factor category. Once entered, the data is stored in the Patient Care Encounter files. The structure of these underlying files has a direct impact on the design of the GEC software. Extracting, viewing, and managing this set of data requires the GEC dialogs to remain as they are released.</p>
<p>Consequently, the Clinical Reminders package has been modified to prevent the GEC national reminders from being copied. This change was made to the Reminder Dialog, Dialog Group, and Dialog Element levels. To accommodate local business practices, sites will be permitted to add locally created health factors to the GEC dialogs. The LM Dialog Editor (Dialog Edit List) will display differently when editing national dialogs that have been locked.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Overview, cont’d</strong></p>
<p><strong>TIP:</strong></p>
</blockquote>
<p> NOTE: The Supply section of the VA-GEC</p>
<blockquote>
<p>NURSING ASSESS-</p>
<p>MENT dialog does not have health factors associated. As a result, they will not be available on the GEC Report menu options.</p>
<p>Sites can modify dialogs to accommodate local business practices. Sites may add locally created health factors to the GEC dialogs.</p>
</blockquote></th>
<th><blockquote>
<p><strong>GEC Referral Reminders and Dialogs</strong></p>
<p>The GEC reminders are comprised of dialogs and health factors only. They have neither cohort nor resolution logic, and will not become due. They are intended only as TIU templates and do not need to be assigned to the CPRS Cover Sheet. Due to potential complications with reporting and duplicate entries, it is recommended that the GEC dialogs not be added to the Reminders drawer/Cover sheet. The Referral was designed for inter-disciplinary use with dialogs created for separate services. However, a single user may perform them all. With only a few exceptions, each section of the dialogs is mandatory and is marked with an asterisk (*). The completion of all four dialogs constitutes a discrete episode of the GEC Referral.</p>
<p>The VA-GEC REFERRAL SOCIAL SERVICES, VA-GEC REFERRAL NURSING ASSESSMENT, and VA-GEC</p>
<p>REFERRAL CARE RECOMMENDATIONS dialogs comprise the clinical screening. The VA-GEC REFERRAL CARE COORDINATION dialog is used administratively to record the arrangement of and funding for extended care services. These dialogs may be performed in any order that local practices dictate. However, it is expected the screening portion will be completed prior to the coordination of services. When the screen is complete, a consult order should be placed to the service responsible for arranging services.</p>
<p><strong>GEC Consult Order</strong></p>
<p>Most sites have either an individual or a service responsible for arranging and coordinating extended care services. To accommodate local business practices and flexibility, sites may associate any consult service (or menu) they already have in place. If none exist, the sites may create a consult or establish some alternative practice to ensure that services are arranged and that the VA-GEC REFERRAL CARE COORDINATION dialog is</p>
<p>completed.</p>
<p>A placeholder for this consult is included at the end of the VA-GEC REFERRAL SOCIAL SERVICES, VA-GEC REFERRAL NURSING ASSESSMENT, and VA-GEC REFERRAL CARE</p>
<p>RECOMMENDATIONS dialogs. It must be substituted or deleted at the time of installation.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Overview, cont’d</strong></p>
<p><strong>TIP:</strong></p>
</blockquote>
<p> If a consult quick order isn’t available</p>
<blockquote>
<p>at the time of the installation of Clinical Reminders V. 2.0, the installer will need to enter a dummy, placeholder name.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Overview, cont’d Setup Steps</strong></p>
<p><strong>1. Set up a GEC Consult Service</strong></p>
</blockquote>
<ul>
<li><blockquote>
<p>Determine if a Consult Service exists for the management of extended care services.</p>
</blockquote>
<ol type="a">
<li><p>If it exists, this service can be used for the quick order and you can proceed to step 2.</p></li>
<li><p>If one does not exist, create a Consult Service by using the [GMRC Manager] option [GMRC SETUP REQUEST SERVICES]. After creating the consult service, add the new consult service to ALL SERVICES.</p></li>
<li><p>Recipients of the consult notifications should be GEC staff responsible for coordinating extended care service (or any appropriate tester).</p></li>
</ol></li>
<li><blockquote>
<p>Create a consult quick order using the “Enter/Edit Quick Orders” option on the Order Management Menu [ORCM MENU]. This order should be associated to the Consult Service in the Consult to Service/Specialty field of the quick order.</p>
</blockquote></li>
<li><blockquote>
<p>Provide the name of the consult quick order to the installer. The installer will then perform the installation and enter the name of the order at the prompt as above.</p>
</blockquote></li>
<li><blockquote>
<p>Sites will need to review the privileging status of those performing the GEC Referral. The staff assigned to place the consult order associated with the GEC dialogs will require the ability to place a consult order. (signature or release).</p>
</blockquote></li>
</ul>
<blockquote>
<p>NOTE: If this consult quick order isn’t available at the time of the installation of Clinical Reminders V2.0, the installer will need to enter a dummy name as a placeholder.</p>
<p><em><strong>See the examples on the following pages for creating a consult service and a consult quick order.</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>1. (cont’d) Set up Consult Services</strong></p>
<p>Follow the example below to set up a consult service.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Set Up Consult Services, cont’d</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>2. Add the GEC Consult Service to ALL SERVICES</strong></p>
<p>When you create a new service, it is <em>not</em> automatically linked into the Consults hierarchy. You must explicitly group each service under ALL SERVICES or under another service that in turn is grouped under ALL SERVICES. Until this is done, the new service is not visible in the service hierarchy and cannot be selected for any action.</p>
<p>Use the Set Up Consult Services (SS) action to group services</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Grouping the Extended Care service under ALL SERVICES

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Set Up Consult Services – linking to ALL SERVICES, cont’d</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>3. Create Consult Order</strong></p>
<p>Use the Order Menu Management option on the CPRS Configuration menu to create a consult order.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Creating Consult Order

> Select CPRS Manager Menu Option: PE CPRS Configuration (Clin Coord)

> AL Allocate OE/RR Security Keys KK Check for Multiple Keys

> DC Edit DC Reasons

> GP GUI Parameters ...

> GA GUI Access - Tabs, RPL MI Miscellaneous Parameters

> NO Notification Mgmt Menu ... OC Order Checking Mgmt Menu ... MM Order Menu Management ...

> LI Patient List Mgmt Menu ... FP Print Formats

> PR Print/Report Parameters ... RE Release/Cancel Delayed Orders US Unsigned orders search

> EX Set Unsigned Orders View on Exit NA Search orders by Nature or Status DO Event Delayed Orders Menu ...

> PM Performance Monitor Report

> Select CPRS Configuration (Clin Coord) Option: MM Order Menu Management OI Manage orderable items ...

> PM Enter/edit prompts

> GO Enter/edit generic orders QO Enter/edit quick orders ST Enter/edit order sets

> AC Enter/edit actions

> MN Enter/edit order menus

> AO Assign Primary Order Menu CP Convert protocols

> SR Search/replace components LM List Primary Order Menus

> DS Disable/Enable order dialogs CU Manage Consult Order Urgencies

> CS Review Quick Orders for Inactive ICD9 Codes

> Select Order Menu Management Option: QO Enter/edit quick orders Select QUICK ORDER NAME: GMRCT GEC REFERRAL

> Are you adding 'GMRCT GEC REFERRAL' as a new ORDER DIALOG? No// Y (Yes) TYPE OF QUICK ORDER: CONSULTS

> NAME: GMRCT GEC REFERRAL// \<Enter\>

> DISPLAY TEXT: GEC REFERRAL

> VERIFY ORDER: \<Enter\>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Create Consults Order, cont’d</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Example, cont’d

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
</blockquote></th>
<th><ol start="4" type="1">
<li><p><strong>Set the parameter TIU TEMPLATE REMINDER DIALOGS</strong></p>
<ul>
<li><p>To use a GEC dialog as a TIU template, use TIU TEMPLATE REMINDER DIALOGS on the General Parameter Tools menu (XPAR)</p></li>
<li><blockquote>
<p>Add the dialog name to be associated with the template</p>
</blockquote></li>
</ul></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Select Systems Manager Menu Option: ^TOOL General Parameter Tools

> LV List Values for a Selected Parameter LE List Values for a Selected Entity

> LP List Values for a Selected Package LT List Values for a Selected Template EP Edit Parameter Values

> ET Edit Parameter Values with Template EK Edit Parameter Definition Keyword

> Select General Parameter Tools Option: EP Edit Parameter Values

> --- Edit Parameter Values ---

> Select PARAMETER DEFINITION NAME: TIU TEMPLATE REMINDER DIALOGS Reminder Dialogs

> allows as Templates

> TIU TEMPLATE REMINDER DIALOGS may be set for the following:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 14%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>User</p>
</blockquote></th>
<th>USR</th>
<th><blockquote>
<p>[choose from NEW PERSON]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>SRV</td>
<td><blockquote>
<p>[choose from SERVICE/SECTION]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td>DIV</td>
<td><blockquote>
<p>[choose from INSTITUTION]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td>SYS</td>
<td><blockquote>
<p>[XSYSTEM.MED.VA.GOV]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter selection: 5 System XSYSTEM.MED.VA.GOV

> Select Display Sequence: ? Display Sequence Value

> 5 VA-GEC REFERRAL SOCIAL SERVICES

> 10 VA-GEC REFERRAL NURSING ASSESSMENT

> 15 VA-GEC REFERRAL CARE RECOMMENDATION

> Select Display Sequence: 20

> Are you adding 20 as a new Display Sequence? Yes// \<Enter\> YES

> Display Sequence: 20// \<Enter\> 20

> Clinical Reminder Dialog: VA-GEC REFERRAL CARE COORDINATION reminder dialog NATIONAL

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
<p><strong>TIP:</strong></p>
</blockquote>
<p> Refer to Appendix</p>
<blockquote>
<p>C in the TIU/ASU</p>
<p>Implementation Guide for complete instructions for creating &amp; implementing Interdisciplinary Notes</p>
</blockquote></th>
<th><ol start="5" type="1">
<li><p><strong>Create a Parent Note Title</strong></p></li>
</ol>
<blockquote>
<p><strong>GEC Interdisciplinary Notes</strong></p>
<p>The GEC Referral dialogs are intended for use as TIU templates. It is also expected that they will be used as part of a TIU Interdisciplinary (ID) note. This will require new TIU Document Definitions or the association of existing titles to the dialogs. This project does not stipulate the titles to be used, preferring to allow the sites to use those titles that would best suit their business practices. However, the Office of Geriatrics Extended Care strongly recommends that the parent ID note title be:</p>
<p>“GEC EXTENDED CARE REFERRAL”</p>
<p>Set up a standard parent note title for use as an interdisciplinary note for GEC. For guidance on interdisciplinary notes and business rules to support them, see the <em>TIU/ASU Implementation Guide</em>, Appendix C, Interdisciplinary Notes Setup Guide.</p>
</blockquote>
<ol start="6" type="1">
<li><blockquote>
<p><strong>Create four Child Note Titles</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>Make up four note titles and associate them with each new clinical reminder template. These will be child note titles. Child note titles in support of GEC are completely at the discretion of the local site.</p>
<p>This screen shot shows the titles used in the development account.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Example: GEC Note Titles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](clinical-reminders-version-2-setup-guide/002.png)

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
</blockquote></th>
<th><ol start="7" type="1">
<li><blockquote>
<p><strong>Associate the four note titles with the GEC dialogs</strong> (NOTE: requires membership in the Clinical Application Coordinator User Class.)</p>
</blockquote></li>
</ol>
<blockquote>
<p>To associate a dialog with a note title:</p>
</blockquote>
<ol type="1">
<li><p>Open the Notes tab</p></li>
<li><p>Click on the Options menu</p></li>
<li><p>Select Edit Shared Templates</p></li>
<li><p>Highlight “Document Titles”</p></li>
<li><p>Click New Template</p></li>
<li><p>Enter name</p></li>
<li><p>Select reminder dialog as Type</p></li>
<li><p>Enter dialog name</p></li>
<li><p>Enter note title in Associated Title field.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Associating Dialog with Note Title

![](clinical-reminders-version-2-setup-guide/003.png)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
</blockquote></th>
<th><ol start="7" type="1">
<li><p><strong>(cont’d ) Associate note titles with the GEC dialogs</strong></p></li>
</ol>
<blockquote>
<p>When you get to the template editor, choose Document Titles from the Shared Template hierarchy:</p>
<p>![](clinical-reminders-version-2-setup-guide/004.png)</p>
<p>Select New Template and create a new template. Enter or select the following:</p>
</blockquote>
<ul>
<li><p>Name</p></li>
<li><p>Select Reminder Dialog as the Template Type.</p></li>
<li><p>Select the GEC Reminder dialog from the drop-down list</p></li>
</ul>
<blockquote>
<p>![](clinical-reminders-version-2-setup-guide/005.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
<p>NOTE: The VA-GEC Referral Care Coordination dialog will be distributed with a TIU Object. The object, |VA-GEC STATUS|, will provide the user a real-time view of the current Referral’s dialog- completion status. It will present information similar to that found on the GEC Referral Status Display and can be used to determine if the Referral can be finalized. The object has been placed into a dialog element and can be viewed by clicking the checkbox.</p>
</blockquote></th>
<th><blockquote>
<p><strong>8. Set the GEC Status Check</strong></p>
<p>There is no limit to the entry of GEC Referral data. Since there may be multiple entries of the same health factors over time, and since the data is entered via separate dialogs, extraction and viewing requires the data to be discretely identified. The GEC software depends upon the user to indicate when the data from a given referral should be concluded. The referral is finalized using a new feature called the GEC Status Indicator. This indicator is presented to the user as a modal dialog at the conclusion of the VA-GEC CARE COORDINATION dialog. It will prompt the user to indicate the conclusion of the Referral with a Yes or No response and will list any missing dialogs. If Yes is selected, the data for the current episode of the Referral is closed. If No is selected, the Indicator is displayed and the data entered will be included with the current episode of the Referral. The Indicator will then be displayed with each succeeding GEC dialog until Yes is selected.</p>
<p>To assist the ongoing management of completing GEC Referrals, the GEC Status Indicator may be added to the CPRS GUI Tools drop-down menu. It may be set at the User or Team level. If added to the drop-down menu, the Indicator may be viewed at any time and used to close the referral if needed. GEC Status Check has been added to the CPRS Reminder Configuration menu on the Reminder Management Menu.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Example: Adding Status Indicator to CPRS Tools Menu

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
<p><strong>TIP:</strong></p>
<p> NOTE: The Indicator is used</p>
<p>to control the bundling of GEC data for reporting purposes and does not alter the behavior or actions of either Text Integration Utility or Patient Care Encounter.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Setting up VA-Geriatric Extended Care (GEC) Referral</strong></p>
<p><strong>GEC Status Check, cont’d Status Indicator Instructions</strong></p>
<p>This section is provided to illustrate the purpose and use of the GEC Status Indicator.</p>
<p>A GEC referral consists of four dialogs and is considered complete when all four are finished. Since a referral may be performed more than once, over time, using the same health factors, responses must be collected as discrete episodes in order to create meaningful reports. The software requires the user to finalize the referral and indicate that it is complete. The referral is finalized using the GEC Status Indicator. This Indicator is available to users upon completion of the GEC Care Coordination dialog. It is also available from the Tools drop-down menu if assigned.</p>
<p>The standard and expected course of events is for a user(s) to perform the Social Services, Nursing Assessment and Care Recommendations dialogs before the Care Coordination dialog. In that case, the Status Indicator first appears after the user has clicked the FINISH button on the Care Coordination dialog. It will prompt the user to indicate that the referral is complete.</p>
<p>If all the dialogs have been completed, the user may select Yes and the current episode of the referral will be closed to any additional data. If any of the other dialogs are missing, the user should select No. This will inform the system to continue collecting responses entered from the dialogs. Each subsequent selection of the FINISH button on the GEC dialogs will display the Status Indicator again, providing the opportunity to close the current episode of the referral. Any entry of a GEC dialog after the Yes button is selected initiates a new episode of the referral.</p>
<p>Alternatively, if the user selects Yes, then deletes the note and performs the dialog again, a new episode of the referral will be initiated. The same result will occur if a GEC dialog is performed from the Reminders drawer. (Due to the risks associated with this process, it is recommended that the GEC dialogs not be added to the Reminders drawer in CPRS).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
<p><strong>TIP:</strong></p>
<p> NOTE: The Indicator is used</p>
<p>to control the bundling of GEC data for reporting purposes and does not alter the behavior or actions of either Text Integration Utility or Patient Care Encounter.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Setting up VA-Geriatric Extended Care (GEC) Referral</strong></p>
<p><strong>GEC Status Check</strong></p>
<p><strong>Status Indicator Instructions, cont’d</strong></p>
<p>The Yes button should only be selected if the user is certain no changes are needed and they are ready to commit to the note’s authentication.</p>
<p>The Status Indicator does not update after the referral has been completed. Put another way, once a referral has been closed, it cannot be reopened. This same risk exists if a note is deleted after the Yes button has been selected and the user then reenters the dialog.</p>
<p>Users should <em>always</em> check the Status Indicator when a new referral is initiated on a patient. Doing so will provide the opportunity of closing any previous referral inadvertently left open.</p>
<p><strong>Example of Status Indicator when all dialogs are complete.</strong></p>
<p>![](clinical-reminders-version-2-setup-guide/006.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: GEC Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Setting up VA-Geriatric Extended Care (GEC) Referral</strong></p>
<p><strong>GEC Status Check</strong></p>
<p><strong>Status Indicator Instructions, cont’d</strong></p>
<p><strong>Example of Status Indicator when some dialogs are missing.</strong></p>
<p>![](clinical-reminders-version-2-setup-guide/007.png)</p>
<p><strong>GEC Referral Ad hoc Health Summaries</strong></p>
<p>Two new health summary components are distributed with this software:</p>
</blockquote>
<ul>
<li><p>GEC Completed Referral Count (GECC)</p></li>
<li><p>GEC Health Factor Category (GECH)</p></li>
</ul>
<blockquote>
<p>The first displays all GEC referral data according to the occurrence and time limits identified. The GEC Health Factor Category component, in conjunction with PX*1*123 and GMTS*2.7*63, permits GEC data to be viewed by health factor or health factor category. If a user should have access to these GEC reports, they must have access to the Ad Hoc Health Summary type. (This can be set using GMTS GUI HS LIST PARAMETERS.)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="_bookmark12" class="anchor"></span><strong>Chapter 2: GEC Setup, cont’d</strong></th>
<th><blockquote>
<p><strong>GEC Referral Reports</strong></p>
<p>The software includes a new set of reports that provide a variety of GEC health factor perspectives. The reports are released as an option within the Clinical Reminder namespace and may be assigned as necessary. The option is GEC Referral Report [PXRM GEC REFERRAL REPORT] and is on the PXRM MANAGERS</p>
<p>MENU. The reports capture data elements for reporting and tracking use of the GEC Referral Screening Tool. The reports may be generated in formatted or delimited output. The Summary (Score) report provides summary (calculated) totals from specific sections of the screening tool identified by the Office of Geriatrics Extended Care.</p>
<p><strong>GEC Reminder Terms</strong></p>
<p>Phase I of the GEC Referral project distributes a set of terms that will be used with Phase II. Since Phase II has not yet been initiated, the functional requirements and design have not been identified.</p>
<p>However, it is expected to include the national roll-up of GEC screening data using the Generic Extract Utility released concurrently with Clinical Reminders V. 2.0. To allow the greatest degree of flexibility in design, one reminder term is released for each GEC Referral health factor. The terms are mapped to the health factors on the VA-GEC REFERRAL reminder dialogs. The terms will be installed silently and reside dormant until Phase II of the GEC Referral project is implemented. The Reminder Definitions used to install these terms will be deleted after installation.</p>
<p><strong>Training</strong></p>
<p>The Office of Geriatric Extended Care (OGEC) will establish a web site to provide training on the GEC screening tool. This training module is being developed with assistance from Employee Education Service and built by ImageITS, a private firm. The module will consist of an interactive tutorial and reference material. OGEC will coordinate the training initiative and serve as the custodian of the web site’s content. Facilities may contact Employee Education Service or its website’s URL or for more information (vaww.ees.aac.va.gov).</p>
<p>The catalog # is PTCAR-EES-G152. The title is “Geriatric Referral Form.”</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark13" class="anchor"></span><strong>Chapter 3: Code Set Versioning</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Chapter 3: CSV Changes in Reminders</strong></p>
<p>Several changes and enhancements are included in Clinical Reminders</p>
<p>V. 2.0 in support of Code Set Versioning, mandated under the Health Information Portability and Accountability Act (HIPAA). The changes will insure that active ICD9, ICD0, and CPT codes are selectable in the CPRS GUI application while using Clinical Reminder Dialogs. It will also produce several email messages to the site users to help in deciding the correct usage of these codes in the Taxonomies and Dialogs.</p>
<p>PXRM*1.5*18, which contained the CSV changes, was previously released in conjunction with CSV_UTIL V. 1, Code Set Versioning, which contains routines, globals, and data dictionary changes to recognize code sets for the International Classification of Diseases, Clinical Modification (ICD-9-CM), Current Procedural Terminology (CPT) and Health Care Financing Administration (HCFA) Common Procedure Coding System (HCPCS). When implemented, the Lexicon will allow translation of these three code systems to select codes based upon a date that an event occurred with the Standards Development Organization (SDO) established specific code that existed on that event date.</p>
<p>Version 2 of Clinical Reminders includes all of the CSV changes contained in patch 18.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 3: CSV, cont’d</strong></p>
<p><strong>Code Text Descriptors</strong></p>
<p>At the time that CSV I was developed, a request was made to defer applicable text versioning to the next iteration, since many of the existing code set databases were not designed to store more than one description for each code. The current processes allow textual descriptions to be overwritten in the files. The follow-up project, Code Text Descriptors, adds the functionality of date-sensitive versioning for all applicable code text descriptors for the four code sets, effective with all textual changes occurring since October 1, 2002. Consistent with the new HIPAA requirements, this project will include expanding the storage of more than one description for each code in the HIPAA code set along applicable versioned dates when the code change occurs.</p>
</blockquote></th>
<th><blockquote>
<p><strong>What do sites need to do?</strong></p>
<p>No setup is required initially for the CSV changes. The Clinical Reminders application has been modified so that Clinical Application Coordinators (CACs) can identify ranges of codes where the adjacent values have changed because of a code set versioning update. A new option and several wording and format changes appear in taxonomy and dialog options.</p>
<p><strong>Changes in Clinical Reminders:</strong></p>
<p><strong>1. Mail Messages (List Manager and GUI)</strong></p>
<p>After Version 2 of Reminders is installed, you will start receiving mail messages about taxonomy/code updates and Reminder Dialog ICPT Code changes.</p>
<p>Those individuals assigned to the Reminders mail group at your site will receive the messages.</p>
<p><em><strong>NOTE: This mail group must be designated as Public</strong></em>.</p>
<p>These updates normally occur quarterly, so you shouldn’t receive these continuously.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 3: CSV, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>CSV Changes in Reminders</strong></p>
<p><strong>2. Taxonomy option changes</strong>:</p>
</blockquote>
<ul>
<li><p>New Reminder Taxonomy Inquiry</p></li>
</ul>
<blockquote>
<p>The following is an example of the new inquiry format (using the option “Inquire about Taxonomy Item”). The ranges for a code set will only be displayed if the taxonomy has a code range defined in the selected taxonomy. Highlighted portions of the inquiry display the changes that will be displayed for each code set category (ICD9, ICD0, and CPT). Other new fields are also highlighted:</p>
<p>Activation Dates (for ICD9, ICD0, and CPT) Inactivation Dates (for ICD9, ICD0, and CPT)</p>
<p>Selectable flag (for ICD9 and CPT; ICD0 are not selectable)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Inquire about Reminder Taxonomy Item – New Display Format

| Code  | ICD Operation/Procedure |     | Activation Inactivation |
|-------|-------------------------|-----|-------------------------|
| 91.46 | CELL BLK/PAP-FEMALE GEN |     | 10/01/1978              |

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 3: CSV, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>2. Taxonomy option changes, cont’d</strong>:</p>
<p><strong>Edit Taxonomy Item</strong></p>
<p>This is an example of using the Edit Taxonomy Item option to edit the ICD0 Low Value and ICD0 High Value codes. When a code is entered here, it must be a code that exists and may be active or inactive. No Text names may be entered. The 91.44 -</p>
<p>91.46 range will be the only edit we will retain from the testing that follows. After testing the prompt for different test scenarios, the “@” at the ICD0 LOW CODE can be used to delete each range of codes entered.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Edit Taxonomy Item’s ICD0 Low and High Code Example

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 3: CSV, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>2. Taxonomy option changes, cont’d</strong>:</p>
<p><strong>Edit Taxonomy Item</strong></p>
<p>This is an example of editing the ICD0 Low Value and ICD0 High Value codes using common codes (various active and inactive codes).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Editing the ICD0 Low Value and ICD0 High Value codes using common codes

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 3: CSV, cont’d</strong></p>
<p><strong>TIP:</strong></p>
<p> The mail group must be</p>
<p>designated as “Public.”</p>
</blockquote></th>
<th><blockquote>
<p><strong>3. Dialog Management option changes</strong></p>
<p>You can now define dialog elements with active or inactive diagnosis or procedure codes in the element’s FINDING ITEM and ADDITIONAL FINDING ITEMS multiple fields. The activation periods related to these codes are passed to the CPRS GUI. The CPRS GUI will only update PCE with diagnosis or procedure codes that are active on the patient’s encounter date. This will address those situations where a code is still active until the effective date is passed, and a new code won’t be active until after the effective date.</p>
<p><strong>New Reminders Dialog Management option</strong></p>
<p><strong>Inactive Codes Mail Message [PXRMCS INACTIVE DIALOG CODES]</strong></p>
<p>This option is used to search the Dialog File #801.41 for ICD and CPT Codes that have become inactive, and to send the report in a mail message to the Clinical Reminders mail group.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Inactive Codes Mail Message option

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 3: CSV, cont’d</strong></p>
</blockquote></th>
<th><ol start="3" type="1">
<li><p><strong>Dialog Management option changes, cont’d</strong></p></li>
</ol>
<blockquote>
<p><strong>Changes to Dialog Taxonomy display in Dialog Edit</strong></p>
<p>To see the taxonomy changes:</p>
</blockquote>
<ol type="1">
<li><p>Select DI, Reminder Dialog, from the Dialog Management menu</p></li>
<li><blockquote>
<p>Change View, CV, to Reminder Dialogs</p>
</blockquote></li>
<li><blockquote>
<p>Select a dialog with taxonomy elements from the list that appears</p>
</blockquote></li>
<li><blockquote>
<p>Select Dialog Text when the Dialog is displayed</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 86%" />
<col style="width: 5%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog Edit List</strong> Mar 16, 2004@10:10:05 Page: 1 of REMINDER DIALOG NAME: VA-*INFLUENZA IMMUNIZATION [NATIONAL] *LIMITED EDIT*</p>
<p><u>Item Seq. Dialog Overview</u></p>
</blockquote>
<ol type="1">
<li><p>5 Element: IM INFLUENZA DONE</p></li>
<li><p>10 Element: IM INFLUENZA CONTRA</p></li>
<li><p>15 Element: TX INFLUENZA IMMUNIZATION CODES</p></li>
<li><p>19 Element: SP OTHER TEXT</p></li>
<li><p>30 Group: GP IM REFUSAL</p></li>
</ol></th>
<th colspan="2"><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
<td><strong>&gt;&gt;&gt;</strong></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CO Copy Dialog DO Dialog Overview QU Quit</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DD Detailed Display DT Dialog Text</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DP Progress Note Text ED Edit/Delete Dialog</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Select Item: Quit// <strong>DT</strong> Dialog Text</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Dialog Edit List Mar 16, 2004@10:10:16 Page: 1 of</p>
</blockquote></td>
<td>4</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REMINDER DIALOG NAME: VA-*INFLUENZA IMMUNIZATION [NATIONAL] *LIMITED EDIT*</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Item Seq. Dialog Text</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 5 Element: IM INFLUENZA DONE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Text: Patient received influenza at this encounter.</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Add. Finding: IMMUNIZATION ADMIN [90471] (PROCEDURE)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Selectable codes: Activation Periods</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>90471 IMMUNIZATION ADMIN Jan 01, 1999</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Add. Finding: FLU VACCINE, 3 YRS, IM [90658] (PROCEDURE)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Selectable codes: Activation Periods</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>90658 FLU VACCINE, 3 YRS, IM Jan 01, 1999</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Add. Finding: VACCIN FOR INFLUENZA [11266] (DIAGNOSIS)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Selectable codes: Activation Periods</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>V04.8 VACCIN FOR INFLUENZA Oct 01, 1978-Oct 01, 2003</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Prompts: Series:</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>&gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>CO Copy Dialog DO Dialog Overview QU Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>DD Detailed Display DT Dialog Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>DP Progress Note Text ED Edit/Delete Dialog</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 3: CSV, cont’d</strong></p>
<p>Two-step process:</p>
</blockquote>
<ol type="1">
<li><p>Create element</p></li>
<li><p>Add element to dialog</p></li>
</ol></th>
<th><blockquote>
<p><strong>3. Dialog Management option changes, cont’d</strong></p>
<p><strong>Adding new taxonomy dialog elements to a dialog</strong></p>
<p>To add new taxonomy dialog elements to a reminder dialog, first create a new dialog element, and then add the element to the dialog.</p>
<p>NOTE: Remember to “Change View” to Dialog Elements.</p>
<p>Use the Add (AD) action to create a new dialog element to represent the taxonomy finding.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Create New Dialog Element

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Dialog List Mar 09, 2004@00:00:12 Page: 1 of 132 DIALOG VIEW (DIALOG ELEMENTS)</p>
<p>Item Dialog Name Dialog type Status</p>
</blockquote>
<ol type="1">
<li><p>00 TIU ELEMENT Dialog Element</p></li>
<li><p>00 TIU ELEMENT SUPPRESS Dialog Element</p></li>
<li><p>01 TIU ELEMENT Dialog Element</p></li>
<li><p>02 TIU ELEMENT Dialog Element</p></li>
<li><p>03 TIU ELEMENT Dialog Element</p></li>
<li><p>04 TIU ELEMENT Dialog Element</p></li>
<li><p>A A PAIN ASSESS MEMBER REPORTS Dialog Element</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AD Add CV Change View INQ Inquiry/Print CO Copy Dialog PT List/Print All QU Quit</p>
<p>Select Item: Next Screen// <strong>AD</strong> Add</p>
</blockquote>
<p>Select DIALOG to add: <strong>TEST CSV CERVICAL CANCER TAX</strong></p>
<p>Are you adding 'TEST CSV CERVICAL CANCER TAX' as</p>
<blockquote>
<p>a new REMINDER DIALOG (the 3388TH)? No// <strong>Y</strong> (Yes) Not used by any other dialog</p>
<p>NAME: TEST CSV CERVICAL CANCER TAX Replace DISABLE:</p>
<p>CLASS: <strong>L</strong> LOCAL SPONSOR:</p>
<p>REVIEW DATE:</p>
<p>RESOLUTION TYPE:</p>
<p>ORDERABLE ITEM:</p>
<p>FINDING ITEM: TX.COPY COPY CSV CERVICAL CANCER SCREEN Cervical cancer screL</p>
<p>...OK? Yes// Y (Yes) DIALOG/PROGRESS NOTE TEXT:</p>
<p>No existing text Edit? NO// YES</p>
<p>==[ WRAP ]==[ INSERT ]=====&lt; DIALOG/PROGRESS NOTE TEXT &gt;====[ &lt;PF1&gt;H=Help ]====</p>
<p>Click here to test Cervical Cancer taxonomy selection.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;===== ALTERNATE PROGRESS NOTE TEXT:</p>
<p>No existing text Edit? NO//</p>
<p>EXCLUDE FROM PROGRESS NOTE: SUPPRESS CHECKBOX:</p>
<p>Select ADDITIONAL FINDINGS: RESULT GROUP/ELEMENT:</p>
<p>Select SEQUENCE:</p>
<p>Input your edit comments. Edit? NO//</p>
<p>Select DIALOG to add:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 3: CSV, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>3. Dialog Management option changes, cont’d</strong></p>
<p><strong>Adding new taxonomy dialog elements to a dialog</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Add new dialog element to a Reminder Dialog definition

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog Edit List</strong> Mar 09, 2004@00:50:41 Page: 1 of 1</p>
<p>REMINDER DIALOG NAME: Pap Smear (local)</p>
<p>Sequence Dialog Details Disabled</p>
<p>10 Dialog group: GPZ PAP SMEAR DIALOG Dialog elements: 1 EX PAP DONE</p>
</blockquote>
<ol start="2" type="1">
<li><p>EX PAP DONE ELSEWHERE</p></li>
<li><p>HF PAP SMEAR CONTRAINDICATED</p></li>
<li><p>HF PATIENT REFUSED (PAP)</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CO Copy Dialog DO Dialog Overview QU Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DD Detailed Display DT Dialog Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DP Progress Note Text ED Edit/Delete Dialog</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Sequence: Quit// ED Edit/Delete Dialog</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NAME: Pap Smear (local)//</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISABLE:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CLASS: LOCAL//</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SPONSOR:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REVIEW DATE:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SOURCE REMINDER: Pap Smear-Screening (VHACHS)//</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Select SEQUENCE: 10// 20</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DIALOG ELEMENT/GROUP: TEST CSV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 TEST CSV ACTIVE AND INACTIVE CODES dialog element LOCAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2 TEST CSV CERVICAL CANCER TAX dialog element LOCAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3 TEST CSV WITH ONLY INACTIVE CODE dialog element LOCAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CHOOSE 1-3: 2 TEST CSV CERVICAL CANCER TAX dialog element LOCAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Select SEQUENCE:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Dialog Edit List</strong> Mar 09, 2004@00:51:55 Page: 1 of 3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REMINDER DIALOG NAME: Pap Smear (local)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sequence Dialog Details Disabled</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10 Dialog group: GPZ PAP SMEAR DIALOG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Dialog elements: 1 EX PAP DONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2 EX PAP DONE ELSEWHERE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3 HF PAP SMEAR CONTRAINDICATED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4 HF PATIENT REFUSED (PAP)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20 Dialog element: TEST CSV CERVICAL CANCER TAX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Finding type: REMINDER TAXONOMY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Finding item: COPY CSV CERVICAL CANCER SCREEN [TX(60)]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CO Copy Dialog DO Dialog Overview QU Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DD Detailed Display DT Dialog Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DP Progress Note Text ED Edit/Delete Dialog</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Sequence: Next Screen//</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark14" class="anchor"></span>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 4: MHV, cont’d</strong></p>
<p>NOTE: The components will display the results or reminder evaluation for all reminders that have a "P" in the Usage field. See the example below that shows the new P for Patient Usage entry.</p>
</blockquote></th>
<th><blockquote>
<p><strong>My Health<em>e</em>Vet, cont’d</strong></p>
<p>Reminders are being developed for veterans to view in their My Health<em>e</em>Vet record. The veteran will be able to click on a “Details” button to see the details of a reminder – comparable to the Clinical Maintenance screens in CPRS and Health Summary.</p>
<p>A patch (PXRM*2.0*2) will provide the functionality to display and view My Health Reminders that show as DUE, to remind the veteran of primary health care needs that should be addressed.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 4: MHV, cont’d</strong></p>
<p>NOTE: The components display the results for all reminders that have a "P" in the Usage field.</p>
<p>The new Health Summary types each contain just one component, the one with the same name as the type.</p>
</blockquote></th>
<th><blockquote>
<p><strong>My Health<em>e</em>Vet Health Summary Types</strong></p>
<p>Clinical Reminders V.2.0 contains new health summary components to support the My HealtheVet project. These components eliminate much of the technical text and code information that is contained in the CM component, and will display summary or detailed information on individual patient reminders to the patients.</p>
<p>Two new national Health Summary types were created to include the new health summary components: REMOTE MHV REMINDERS DETAIL and REMOTE MHV REMINDERS SUMMARY. These will</p>
<p>be available in health summaries on the reports tab in CPRS.</p>
<p>The health summary types will also be available to clinicians even if the patient is being seen at a different site.</p>
<p><strong>Example: MHVD Health Summary - Detail Display</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](clinical-reminders-version-2-setup-guide/008.png)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 4: MHV, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>My HealtheVet Health Summary</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: MHVS Health Summary, cont’d

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* CONFIDENTIAL AD HOC SUMMARY pg. 1 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* CRPATIENT,ONE 666-31-9898 1A(1&2) DOB: 07/13/1950

> MHVD - Detail Display

> --STATUS-- --DUE DATE-- --LAST DONE--

> Flu vaccine DUE NOW DUE NOW unknown All patients over the age of 50 should receive influenza vaccination unless they are allergic to eggs.

> Influenza or "flu" is a serious disease that spreads easily. It causes fever, chills, cough, fatigue, aches, or loss of appetite. It can progress to bronchitis, pneumonia and death. Flu causes thousands of deaths each year in the US that could be prevented if the flu shot or vaccine was received.

> The flu shot is recommended yearly for those who are at a higher risk to have severe flu if they catch the flu. They include:

- Anyone age 50 older.
- Anyone with long-term health problems of the lungs, heart, or kidney, asthma, or diabetes.
- Anyone who has a weak immune system from HIV/AIDs, steroid treatment, or cancer treatment.
- Residents of nursing homes or other long-term care facilities.

> The flu shot is not recommended for people who are allergic to eggs, had a severe reaction to flu shot in the past, allergic to thiomerosol, a history of Guillian-Barre Syndrome (GBS), or currently have a high fever.

> The flu shot or vaccine protects most people from the flu. Some may still catch the flu after having the shot but are likely to have a milder case.

> The flu shot does NOT cause the flu. It protects one from the flu. The vaccine is safe and it works. Most people will not have side effects. A few may feel sore at the site where the shot was given. Fewer may have fever, chills, headaches, or muscle aches. The best time to get

> a flu shot is in October or November. However, getting the flu shot later in December thru March will still give very good protection. VA Clinics usually offer flu shots from September thru March.

> Our records show that you have not received your flu shot for this season. Please get your flu shot soon or tell us if you already got one.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 4: MHV, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>My HealtheVet Health Summary</strong></p>
<p><strong>Example: MHVD Health Summary - Detail Display, cont’d</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Please check these web sites for more information: Web Site: CDC Influenza Home Page

> URL: <http://www.cdc.gov/ncidod/diseases/flu/fluvirus.htm>

> Web Site: Weekly Update on Influenza Rates

> URL: <http://www.cdc.gov/ncidod/diseases/flu/weekly.htm>

> CDC Site for weekly updates on the current influenza activity in the community.

> Web Site: Dept HHS Information on Influenza Vaccination

> URL: <http://odphp.osophs.dhhs.gov/pubs/guidecps/text/CH66.txt>

> Web Site: California Influenza Information

> URL: <http://www.dhs.ca.gov/ps/dcdc/VRDL/html/Flutable02-03.htm>

> Web Site: Patient Handout for Influenza Vaccine

> URL: <http://www.cdc.gov/nip/publications/VIS/vis-flu.pdf>

> Flu vaccine Due Now DUE NOW DUE NOW unknown All patients over the age of 50 should receive influenza vaccination unless they are allergic to eggs.

> Influenza or "flu" is a serious disease that spreads easily. It causes fever, chills, cough, fatigue, aches, or loss of appetite. It can progress to bronchitis, pneumonia and death. Flu causes thousands of deaths each year in the US that could be prevented if the flu shot or vaccine was received.

> The flu shot is recommended yearly for those who are at a higher risk to have severe flu if they catch the flu. They include: \* Anyone age 50 older. \* Anyone with long-term health problems of the lungs, heart, or kidney, asthma, or diabetes. \* Anyone who has a weak immune system from HIV/AIDs, steroid treatment, or cancer treatment. \* Residents of nursing homes or other long-term care facilities.

> The flu shot is not recommended for people who are allergic to eggs, had a severe reaction to flu shot in the past, allergic to thiomerosol, a history of Guillian-Barre Syndrome (GBS), or with high fever at the time. The flu shot or vaccine protects most people from the flu. Some may still catch the flu after having the shot but are likely to have a milder one.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 4: MHV, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>My HealtheVet Health Summary</strong></p>
<p><strong>Example: MHVD Health Summary - Detail Display, cont’d</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>The flu shot does NOT cause the flu. It protects one from the flu. The vaccine is safe and it works. Most people will not have side effects. A few may feel sore at the site where the shot was given. Fewer may have fever, chills, headaches, or muscle aches. The best time to get</p>
<p>a flu shot is in October or November. However, getting the flu shot later in December thru March will still give very good protection. VA Clinics offer flu shots usually from September thru March.</p>
<p>Our records show that you have not received your flu shot for this season. Please get your flu shot soon or tell us if you already got one.</p>
<p>Please check these web sites for more information: Web Site: CDC Influenza Home Page</p>
<p>URL: <a href="http://www.cdc.gov/ncidod/diseases/flu/fluvirus.htm">http://www.cdc.gov/ncidod/diseases/flu/fluvirus.htm</a></p>
<p>Web Site: Weekly Update on Influenza Rates</p>
<p>URL: <a href="http://www.cdc.gov/ncidod/diseases/flu/weekly.htm">http://www.cdc.gov/ncidod/diseases/flu/weekly.htm</a></p>
<p>CDC Site for weekly updates on the current influenza activity in the community.</p>
<p>Web Site: Dept HHS Information on Influenza Vaccination</p>
<p>URL: <a href="http://odphp.osophs.dhhs.gov/pubs/guidecps/text/CH66.txt">http://odphp.osophs.dhhs.gov/pubs/guidecps/text/CH66.txt</a></p>
<p>Web Site: California Influenza Information</p>
<p>URL: <a href="http://www.dhs.ca.gov/ps/dcdc/VRDL/html/Flutable02-03.htm">http://www.dhs.ca.gov/ps/dcdc/VRDL/html/Flutable02-03.htm</a></p>
<p>Web Site: Patient Handout for Influenza Vaccine</p>
<p>URL: <a href="http://www.cdc.gov/nip/publications/VIS/vis-flu.pdf">http://www.cdc.gov/nip/publications/VIS/vis-flu.pdf</a></p>
<p>Influenza Vaccine DUE NOW 12/10/2000 12/10/1999 Immunization: INFLUENZA = (12/10/1999)</p>
<p>Encounter Procedure = INFLUENZA IMMUNIZATION (12/10/1999)</p>
<p>Flu shot due yearly in patients any age that have a high risk for flu or pneumonia.</p>
<p>Encounter Diagnosis = DIABETES MELLI W/0 COMP TYP I (09/10/2001)</p>
<p>MENTAL TESTS ZZCOPYRIGHT DUE NOW DUE NOW unknown</p>
<p>Age match text for inquiry purposes</p>
</blockquote></td>
</tr>
</tbody>
</table>

![](clinical-reminders-version-2-setup-guide/009.png)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 4: MHV, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>My HealtheVet Health Summary</strong></p>
<p><strong>Example: MHVS Health Summary - Summary Display</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 4: MHV, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Adding My HealtheVet Health Summary to a User’s Health Summary in CPRS</strong></p>
<p><strong>The example below shows the sequence for adding the MHV health summary types to the CPRS Reports tab for a user</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## APPENDIX A: Hints and Tips 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Q: Is there any way to do a reminder report on an individual finding item?

> We want to add a check box that indicates depression is a new diagnosis. Is there a way to do a reminder report just on that one finding that will tell us how many of the patients that were seen that this was applicable for?

> A: Set up a local reminder with that one finding as a resolution finding. Define the reminder USAGE field as Reports, and then it will not appear on the cover sheet.

> Additional trick:

> Make the frequency to be 1 day, and put an OR for the resolution logic and AND for the COHORT logic. That then gives you output in the CM or health summary that gives the date it was last done so not only do you get a list of folks who have the finding but you also can tell when it was entered.

> Q: (NOIS) Need routine to print labels

> The site would like to print address labels for reminders that are due, to mail to the patients. Do you know of a site that my have this in place?

> A: CR V. 2.0 will allow you to save a patient from a due report to a patient list. From a patient list, you can print a report that displays the address in a delimited format for import/export to Word labels.

> Q: I have a couple of medication reminders that I have edited so that if the provider writes a new prescription, the reminder will be resolved temporarily by the pending medication order and not have to wait for the released date. I have the orderable items set to resolve the reminder if the status of the orderable item is pending. The order shows on the orders tab as pending and DOES NOT resolve the reminder. The reminder test output suggests to me that the pending order is not being used in the reminder evaluation.

> A: The future date needs to be added to the reminder at the Ending Date/Time prompt. The default is the end of the current day. If you want this to be further in the future, you need to enter something like T+3M.

#### Forced Value in Dialogs

> Q: I have an element that has a single ICD code in it and whenever this template is used, I want this ICD code to be entered and for it to automatically go in as the primary diagnosis.

> I can get the ICD code to be automatically entered but I cannot seem to create a forced value prompt from the PXRM PRIMARY DIAGNOSIS prompt that works correctly. If I set the forced value to PRIMARY or to PRIMARY DIAGNOSIS, it does not seem to work and the diagnosis is always recorded as the secondary diagnosis.

> Here is the element:

> NAME: TX V CODE FOR TB SCREEN Replace DISABLE:

> CLASS: LOCAL// SPONSOR: REVIEW DATE:

> RESOLUTION TYPE:

> ORDERABLE ITEM:

> FINDING ITEM: V74.1// DIALOG/PROGRESS NOTE TEXT:

> Enter ICD Code for "Screening for TB" (V code for checkout) Edit? NO// y YES

> ICD Code for "Screening for TB" (V code for checkout)

> ALTERNATE PROGRESS NOTE TEXT:

> No existing text Edit? NO//

> EXCLUDE FROM PROGRESS NOTE: YES// SUPPRESS CHECKBOX: SUPPRESS// Select ADDITIONAL FINDINGS:

> RESULT GROUP/ELEMENT:

> Select SEQUENCE: 5// SEQUENCE: 5//

> ADDITIONAL PROMPT/FORCED VALUE: PXRM PRIMARY DIAGNOSIS

> //

> OVERRIDE PROMPT CAPTION:

> START NEW LINE:

> EXCLUDE FROM PN TEXT: YES// REQUIRED: NO//

> Select SEQUENCE:

> Input your edit comments. Edit? NO//

> Here is the forced value that does not work:

> Forced value NAME: ICD PRIMARY DIAGNOSIS Replace DISABLE Forced value:

> CLASS: LOCAL// SPONSOR:

> REVIEW DATE:

> FORCED VALUE: PRIMARY// RESTRICTED TO FINDING TYPE: POV//

> A: Here's an undocumented feature. If you want the Primary diagnosis to automatically be populated, define a Prompt as below and apply it to the appropriate dialog element

> Forced value NAME: FORCE PRIMARY DIAGNOSIS Replace DISABLE Forced value:

> CLASS: LOCAL// SPONSOR:

> REVIEW DATE:

> FORCED VALUE: 1// \<\< Value of 1 will set the field TRUE. RESTRICTED TO FINDING TYPE: POV//

> Q: When Clinical Maintenance is run on a reminder that is applicable due to a problem list entry, why is today's date pulled rather than the date of problem list entry?

> A: There are two dates associated with ICD9 diagnoses found in PROBLEM LIST. There is the date entered and the date last modified. The PRIORITY field is used to determine if a problem is chronic or acute. *If the problem is chronic, Clinical Reminders will use today’s date in its date calculations; otherwise it will use the date last modified.* Problems that are “chronic” can never expire. Note that it only uses active problems unless the field USE INACTIVE PROBLEMS is yes.

> Q: Flu vaccine reminder

> Last year our flu vaccine reminder worked well, but now we are getting the following: This is how the reminder dialog is set up:

> Additional Finding: VACCIN FOR INFLUENZA \[11266\] Additional Finding: IMMUNIZATION ADMIN \[90471\] Additional Finding: FLU VACCINE, 3 YRS, IM \[90658\]

> Additional Finding: OFFICE/OUTPATIENT VISIT, EST \[99211\]

> I just put in a vaccine using the reminder and found the following show (the computer is automatically adding codes):

5.  CPT Code: 90471 IMMUNIZATION ADMIN
6.  CPT Code: 90658 FLU VACCINE, 3 YRS, IM
7.  CPT Code: 99211 OFFICE/OUTPATIENT VISIT, EST
8.  CPT Code: 90659 FLU VACCINE, WHOLE, IM \<-------
9.  Immunization: INFLUENZA \<-------
10. Immunization: FLU,3 YRS
11. Immunization: FLU,WHOLE \<------

> Any ideas as to why this is happening would be appreciated.

> A: Your Encounter Form for that specific clinic may have that code (90659) as a choice. If so, it's most probably being entered by either:

1.  The provider who checks out the appointment themselves. standalone. Clicking on the encounter

> button, brings up the encounter form codes that are on that EF for that clinic; or

2.  The checkout clerk may be just entering codes checked-off on the EF by the provider.

#### Q: How can I make reminder dialogs WYSIWYG for short lines of text?

> A: The new text formatter lets you format dialogs, as well as progress note text. Define your element like this, using the backslashes as shown:

> Example Output in CPRS Reminder Dialog:

> ![](clinical-reminders-version-2-setup-guide/010.png)

> NOTE: You can also use \<br\> for line breaks.

> Q: When I try to edit the Cover Sheet list in CPRS, it does not give me the option for System, location, service, division. I was assigning reminder folders to physicians and nurses through the GUI and now the Edit Cover Sheet Reminder List is grayed out for me. It will not allow me to edit for System, Division, Location, etc. I can only edit for myself (user). Where do we change this, so I can assign reminders through the GUI?

> A: Check to see if you have the PXRM CPRS CONFIGURATION menu. You may have it as part of the Eve menu. If you add it to your secondary menu, the option should no longer be grayed out on your Edit Cover Sheet Reminder list in GUI.

#### Q: Computed Finding – Location

> We would like to build a reminder that is applicable only to patients in specific locations (Domiciliary). These patients are followed by Primary Care providers in clinics where patients in an outpatient status are also seen. so simply displaying the reminder according to hospital location is

> not an option.

> Has anyone created a computed finding that would make my reminder applicable only to Dom patients? Or can anyone think of something besides a computed finding that will allow me to do this?

> A: Here’s one, which you might need to customize just a little for your site.

> First possibility. This is the one we use to check for patients in a NHCU, but really it's just hard coded to the location names of our two long-term care areas. I've changed the references to an NHCU to read "DOM,” but it would work no matter what location you are trying to find, as long as it is specific. Something like "11E" might not work.

> DOM(DFN,TEST,DATE,VALUE,TEXT) ;;LOCAL TO HINES - IS PATIENT IN DOM?

> N VAIN

> D INP^VADPT

> S TEST=0,DATE=""

> I \$P(VAIN(4),"^",2)\["ECC" S TEST=1,DATE=DT

> I \$P(VAIN(4),"^",2)\["RCF" S TEST=1,DATE=DT Q

> NAME: AJEY DOM PATIENT (local) ROUTINE:\<\<WHATEVER YOU NAME YOUR ROUTINE\>\>

> ENTRY POINT: DOM PRINT NAME: Is Patient in a DOM Location?

> You would want to change ECC to match something that your DOM locations had in their name, presumably "DOM".

> The other possibility is instead of looking in VAIN(4), which contains the patient location, to look in VAIN(3), if the treating specialty might be specific for something like a domiciliary.

#### Drug for patient cohort logic

> Q: Can I use a drug for patient cohort logic? I thought that I could, but then I tried the drug and use the logic of and it shows that the patient is not applicable for this reminder. Can anyone help me?

> A: You can use a DC or Drug Class as a finding as I've done on the reminder for Beta Blocker after an acute MI. Here's what it looks like:

> Select Reminder Definition Management Option: re Add/Edit Reminder Definition Select Reminder Definition: v1-beta BLOCKER AFTER MI LOCAL

> Select one of the following:

> A All reminder details

> G General

> B Baseline Frequency

> F Findings

> L Logic

> D Reminder Dialog

> W Web Addresses Select section to edit: f Findings Findings

> Choose from:

> DC CV100 \<---- That one right there!!!!

> HF ACTIVE OUTSIDE RX FOR BETA BLOCKER

> HF INACTIVATE BETA BLOCKER AFTER ACUTE MI RT LOW PULSE

> RT LOW SYSTOLIC BP

> TX ASTHMA

> TX HEART BLOCKS

> TX PRO-ACUTE MYOCARDIAL INFARCTION

> Select FINDING:

#### Q: Allocation Errors

> Why did the user error out while running a clinical reminder in CPRS?

> \$ZE= ETRAP+4^XWBTCPC:1, %DSM-E-ALLOC, allocation failure

> S XWBERC=\$\$EC^%ZOSV,XWBERR=\$C(24)\_"M ERROR="\_XWBERC\_\$C(13,10)\_"LAST REF="\_\$\$LG

> R^%ZOSV\_\$C(4)

> Last Global Ref: ^PXRMD(801.41,570,1)

> A: Probably two nodes were configured below the standard partition size. Once the partition size parameters were updated and the nodes re-booted, errors stopped.

> Q: Why is this Reminder not Due as Expected? The Rank Frequency (as relates to this problem) appears to be correct...

1.  Colonoscopy taxonomy (resolves 10 yr)
2.  Colonoscopy Done Elsewhere (resolves 10 yr)

> 6 FOBT taxonomy (for lab test) (resolves 1 yr)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* This particular patient shows:

> STATUS --DUE DATE-- --LAST DONE--

> Resolved 8/13/2011 8/13/2001

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 8/13/2001 Laboratory test: Blood Occult feces; value - Neg 11/10/1999 (E) Health Factor: COLONOSCOPY ELSEWHERE

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> We expect to see a DUE DATE of 11/10/2009 - 10 yrs from the Colonoscopy. Instead, he shows 10 years from the Lab Test date of 8/13/2001.

> A: For each item that had a Rank Frequency within the Reminder, it was suggested to make sure there was an Effective Period. I did, but it still didn't work. Then, I went back and for each element with Rank Frequency, I put in the Minimum Age field. I didn't think this was necessary because it was the same as the Baseline Frequency. But, once those were entered, it works beautifully, calculating the correct date.

> So, now we know to enter all the fields applicable if a Rank Frequency is entered, even if it appears to be duplication of information.

> Q: We've been having trouble getting this reminder to turn off. Could you look at my logic and tell me what I've done wrong?

> A: The problem is function findings do not have a date, so if they are the sole resolution finding, a resolution date cannot be determined. Try changing your resolution logic to FI(2)&FF(1). The resolution date would then be the most recent date for the Smoking Cessation Education but it would not be resolved unless at least three educations were done.

> Q: Which takes precedence: finding modifiers on terms or finding modifiers in the reminder definition?

> A: In most cases a finding modifier on a term takes precedence over the modifier in the definition. An exception to this is the Occurrence Count. The reason for this can be understood by looking at an example. Let’s say a term has been mapped to three findings with an Occurrence Count of 1 for finding 1, 2 for finding 2, and 3 for finding 3. If the maximum number of occurrences is found for each finding then how do you determine how many occurrences to display? In this case we would have 6 occurrences so we have the possibility of displaying anywhere between 1 and 6 of them. The solution is to display the number of occurrences specified at the definition level.

> Q: We have one user who can only see the "other" folder when he tries to process clinical reminders.

> What do we have to do so he can see the due and applicable folders?

> A: Have the user click on the red reminder clock and then click on the 'VIEW' command. Make sure that all the categories (DUE, APPLICABLE, etc.) have been checked.

#### Reminder Exchange Tip

> If you try to exchange a reminder containing a location list from one system to another and there is an inconsistency or mismatch between systems in the AMIS stop code, you will get the following error message. (in this case the system has two selectable entries for stop code 560.)

> REMINDER LOCATION LIST entry NEXUS STOP CODES FY05 is NEW,

> what do you want to do?

> Select one of the following:

> C Create a new entry by copying to a new name I Install

> Q Quit the install

> S Skip, do not install this entry

> Enter response: i Install

> Name associated with AMIS stop code does not match the one in the packed reminder:

> AMIS=560

> Site Name=ZZSUBSTANCE ABUSE - GROUP

> Name in packed reminder=SUBSTANCE ABUSE - GROUP

> The update failed, UPDATE^DIE returned the following error message: MSG("DIERR")=1^1

> MSG("DIERR",1)=701 MSG("DIERR",1,"PARAM",0)=3 MSG("DIERR",1,"PARAM",3)=GYNECOLOGY MSG("DIERR",1,"PARAM","FIELD")=.01

> MSG("DIERR",1,"PARAM","FILE")=810.90011

> MSG("DIERR",1,"TEXT",1)=The value 'GYNECOLOGY' for field CREDIT STOP TO EXCLUDE

> in CREDIT STOPS TO EXCLUDE SUB-FIELD in CLINIC STOP LIST SUB-FIELD in

> file REMINDER LOCATION LIST is not valid. MSG("DIERR","E",701,1)=

> REMINDER LOCATION LIST entry NEXUS STOP CODES FY05 did not get installed! Examine the above error message for the reason.

## APPENDIX B: Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> AAC Austin Automation Center
> AIMS Abnormal Involuntary Movement Scale API Application Programmer Interface.
> CAC Clinical Application Coordinator CPRS Computerized Patient Record System. DBIA Database Integration Agreement.
> EPRP External Peer Review Program
> GUI Graphical User Interface.
> HSR&D Health Services Research and Development HL7 Health Level 7
> IHD Ischemic Heart Disease
> MDD Major Depressive Disorder
> OQP Office of Quality and Performance QUERI Quality Enhancement Research Initiative SAS Simple Authentication and Security
> SRS Software Requirements Specification
> VHA Veterans Health Administration. VISN Veterans Integrated Service Networks.
> VIS*T*A Veterans Health Information System and Technology Architecture.

### National Acronym Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Definitions

> AAC SAS Files AAC SAS files contain data that is equivalent to data stored in

> the Reminder Extract Summary entry in the Reminder Extract Summary file. AAC manages SAS files for use by specifically defined users.

> Applicable The number of patients whose findings met the patient cohort

> reminder evaluation.

> Due The number of patients whose reminder evaluation status is due.

> Extract Parameter Parameters that define how to identify the patient cohort. A

> national extract entry is defined for each extract process. This entry defines an extract name, how often to automatically run the named extract process, the rules used to identify target patients, what reminders should be run against what patient list, what type of finding counts to accumulate, and where to transmit results.

> Extract Summary An extract summary containing the results of an extract process

> is created by this process in the Extract Summary File. This Extract Summary entry will help coordinators track the extract process through successful transmission processing by AAC.

> Extract Run A periodic extract job based on the Extract Parameter definition.

> The extract job creates an entry in the Reminder Extract Summary file. The extract job automatically starts a transmission job to transmit the extract summary data to a queue at the AAC. The successful completion of the Extract Run schedules the next periodic Extract Run.

> Finding Count Rules A Finding Count Rule defines the group of findings to

> accumulate, the type of finding total, and whether to use the TOTAL or APPLICABLE patient cohorts to calculate finding counts.

> Finding Group Group of Reminder Terms within the Extract Parameter File

> used for counting purposes.

> Finding Totals Totals derived using Finding Count Rules.

> HL7 Transmissions HL7 transmission packages contain HL7 messages that are

> processed between the transmitting system and AAC.

> List Rules A List Rule is a set of rules that define which findings shall be used to determine whether a patient should be added or removed from a patient list.

> National Database All sites running Mental Health QUERI software transmit their

> data to a new compliance totals database at the AAC.

> Not Applicable The number of patients whose findings did not meet the patient

> cohort reminder evaluation.

> Not Due The number of patients whose reminder evaluation status is not due.

> Reminder Definitions Reminder Definitions comprise the predefined set of finding

> items used to identify patient cohorts and reminder resolutions. Reminders are used for patient care and/or report extracts.

> Reminder Dialog Reminder Dialogs comprise a predefined set of text and findings

> that together provide information to the CPRS GUI, which collects and updates appropriate findings while building a progress note.

> Reminder Patient List A list of patients that is created from a set of List Rules and/or as

> a result of report processing. Each Patient List is assigned a name and is defined in the Reminder Patient List File. Reminder Patient Lists may be used as an incremental step to completing national extract processing or for local reporting needs. Patient Lists created from the Reminders Due reporting process are based on patients that met the patient cohort, reminder resolution, or specific finding extract parameters. These patient lists are used only at local facilities.

> Reminder Terms Predefined finding items that are used to map local findings to

> national findings, providing a method to standardize these findings for national use.

> Reminder Totals Totals that are accumulated from the reminder evaluation

> process based on the APPLICABLE, NOT APPLICABLE, DUE, AND NOT DUE statuses.

> Report Reminders Reminders may be defined specifically for national reporting.

> Report Reminders do not have a related Reminder Dialog in CPRS and are not used by clinicians for patient care. However, clinical reminders that are used in CPRS may also be used for national reminder reporting. All reminders targeted for national reporting are defined in Extract Parameters.

> Reporting Period Extract The extracts may be for monthly, quarterly, or yearly processing.

> The extracts are formatted and transmitted to the national database via HL7 messaging using a report format.

> Total The total number of patients in a patient list (denominator) based on the criteria defined in the Reminder List Rule file.

> Transmission Run The Transmission Run is started automatically by the Extract

> Run, but may also be manually scheduled. The extract process starts the Transmission Run just before completing the Extract Run. The Transmission Run transmits extract summary data to an AAC queue via HL7 transmissions. This data updates the Reminder Extract Summary entry for the reporting period.

## APPENDIX C: National Reminders Rescission 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See [<u>VHA Notice 2004-04</u>](http://vaww1.va.gov/vhapublications/ViewPublication.asp?pub_ID=1159) for more information about rescission of national reminders.

> When Clinical Reminders V.2.0 is installed, the following reminders are rescinded by:

1)  Setting the inactive flag.
2)  Setting the RESCISSION DATE field.
3)  Changing the name of the reminder.
4)  Changing the data in the PRINT NAME field

> NOTE: ZZ is reserved for use as a scratch namespace (defined on FORUM, Package File). As such, sites may already have copied a reminder and used the prefix ZZ. Sites should review their local reminders, to ensure that this installation doesn’t over-write any reminders.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 26%" />
<col style="width: 22%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Reminder Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>New Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Print Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>New Print Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-*BREAST CANCER</p>
<p>SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*BREAST</p>
<p>CANCER SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Breast Cancer</p>
<p>Screen</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Breast Cancer</p>
<p>Screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-*CERVICAL CANCER SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*CERVICAL CANCER SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Pap Smear</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Pap Smear</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-*CHOLESTEROL</p>
<p>SCREEN (F)</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*CHOLESTEROL</p>
<p>SCREEN (F)</p>
</blockquote></td>
<td><blockquote>
<p>Cholesterol Screen</p>
<p>(Female)</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Cholesterol Screen</p>
<p>(Female)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-*CHOLESTEROL</p>
<p>SCREEN (M)</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*CHOLESTEROL</p>
<p>SCREEN (M)</p>
</blockquote></td>
<td><blockquote>
<p>Cholesterol Screen</p>
<p>(Male)</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Cholesterol Screen</p>
<p>(Male)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-*COLORECTAL CANCER SCREEN (FOBT)</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*COLORECTAL CANCER SCREEN</p>
<p>(FOBT)</p>
</blockquote></td>
<td><blockquote>
<p>Fecal Occult Blood Test</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Fecal Occult Blood Test</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-*COLORECTAL</p>
<p>CANCER SCREEN (SIG.)</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*COLORECTAL</p>
<p>CANCER SCREEN (SIG.)</p>
</blockquote></td>
<td><blockquote>
<p>Flexisigmoidoscopy</p>
</blockquote></td>
<td><blockquote>
<p>ZZ</p>
<p>Flexisigmoidoscopy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-*FITNESS AND EXERCISE SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*FITNESS AND EXERCISE SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Exercise Education</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Exercise Education</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-*HYPERTENSION</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*HYPERTENSION</p>
</blockquote></td>
<td><blockquote>
<p>Hypertension</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Hypertension</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-*INFLUENZA</p>
<p>IMMUNIZATION</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*INFLUENZA</p>
<p>IMMUNIZATION</p>
</blockquote></td>
<td><blockquote>
<p>Influenza</p>
<p>Immunization</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Influenza</p>
<p>Immunization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-*PNEUMOCOCCAL VACCINE</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*PNEUMOCOC- CAL VACCINE</p>
</blockquote></td>
<td><blockquote>
<p>Pneumovax</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Pneumovax</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-*PROBLEM DRINKING</p>
<p>SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*PROBLEM</p>
<p>DRINKING SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Problem Drinking</p>
<p>Screen</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Problem Drinking</p>
<p>Screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-*SEATBELT AND</p>
<p>ACCIDENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*SEATBELT AND</p>
<p>ACCIDENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Seatbelt and Accident</p>
<p>Screen</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Seatbelt and</p>
<p>Accident Screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-*TETANUS DIPHTHERIA</p>
<p>IMMUNIZATION</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*TETANUS DIPHTHERIA</p>
<p>IMMUNIZATION</p>
</blockquote></td>
<td><blockquote>
<p>Tetanus Diphtheria (TD-Adult)</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Tetanus Diphtheria (TD-Adult)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-*TOBACCO USE</p>
<p>SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*TOBACCO USE</p>
<p>SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Tobacco Use</p>
<p>Screen</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Tobacco Use</p>
<p>Screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-*WEIGHT AND NUTRITION SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-*WEIGHT AND NUTRITION SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Weight and Nutrition Screen</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Weight and Nutrition Screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-ADVANCED DIRECTIVES EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-ADVANCED DIRECTIVES</p>
<p>EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>Advanced Directives Education</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Advanced Directives Education</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-ALCOHOL ABUSE EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-ALCOHOL ABUSE EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>Alcohol Abuse Education</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Alcohol Abuse Education</p>
</blockquote></td>
</tr>
</tbody>
</table>

### National Reminder Rescission and Renaming

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 26%" />
<col style="width: 22%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Reminder Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>New Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Print Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>New Print Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-BLOOD PRESSURE</p>
<p>CHECK</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-BLOOD</p>
<p>PRESSURE CHECK</p>
</blockquote></td>
<td><blockquote>
<p>Blood Pressure</p>
<p>Check</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Blood Pressure</p>
<p>Check</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-BREAST EXAM</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-BREAST EXAM</p>
</blockquote></td>
<td><blockquote>
<p>Breast Exam</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Breast Exam</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-BREAST SELF EXAM EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-BREAST SELF EXAM EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>Breast Self-Exam Education</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Breast Self-Exam Education</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 26%" />
<col style="width: 22%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Reminder Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>New Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Print Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>New Print Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-DIABETIC EYE</p>
<p>EXAM</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-DIABETIC EYE</p>
<p>EXAM</p>
</blockquote></td>
<td><blockquote>
<p>Diabetic Eye</p>
<p>Exam</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Diabetic Eye</p>
<p>Exam</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-DIABETIC FOOT CARE ED.</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-DIABETIC FOOT CARE ED.</p>
</blockquote></td>
<td><blockquote>
<p>Diabetic Foot Care Education</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Diabetic Foot Care Education</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-DIABETIC FOOT</p>
<p>EXAM</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-DIABETIC FOOT</p>
<p>EXAM</p>
</blockquote></td>
<td><blockquote>
<p>Diabetic Foot</p>
<p>Exam</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Diabetic Foot</p>
<p>Exam</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-DIGITAL RECTAL (PROSTATE) EXAM</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-DIGITAL</p>
<p>RECTAL (PROSTATE) EXAM</p>
</blockquote></td>
<td><blockquote>
<p>Digital Rectal (Prostate) Exam</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Digital Rectal (Prostate) Exam</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-EXERCISE</p>
<p>EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-EXERCISE</p>
<p>EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>Exercise Education</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Exercise</p>
<p>Education</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-FECAL OCCULT</p>
<p>BLOOD TEST</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-FECAL OCCULT</p>
<p>BLOOD TEST</p>
</blockquote></td>
<td><blockquote>
<p>Fecal Occult Blood</p>
<p>Test</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Fecal Occult</p>
<p>Blood Test</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA- FLEXISIGMOIDOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA- FLEXISIGMOIDOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>Flexisigmoidoscopy</p>
</blockquote></td>
<td><blockquote>
<p>ZZ</p>
<p>Flexisigmoidoscopy</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-INFLUENZA</p>
<p>VACCINE</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-INFLUENZA</p>
<p>VACCINE</p>
</blockquote></td>
<td><blockquote>
<p>Influenza</p>
<p>Vaccine</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Influenza Vaccine</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-</p>
<p>MAMMOGRAM</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-MAMMOGRAM</p>
</blockquote></td>
<td><blockquote>
<p>Mammogram</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Mammogram</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-NUTRITION/OBESITY EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA- NUTRITION/OBESITY</p>
<p>EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>Nutrition/Obesity Education</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Nutrition/Obesity Education</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-PAP SMEAR</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-PAP SMEAR</p>
</blockquote></td>
<td><blockquote>
<p>Pap Smear</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Pap Smear</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-PNEUMOVAX</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-PNEUMOVAX</p>
</blockquote></td>
<td><blockquote>
<p>Pheumovax</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Pheumovax</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-PPD</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-PPD</p>
</blockquote></td>
<td><blockquote>
<p>PPD</p>
</blockquote></td>
<td><blockquote>
<p>ZZ PPD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-PSA</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-PSA</p>
</blockquote></td>
<td><blockquote>
<p>PSA</p>
</blockquote></td>
<td><blockquote>
<p>ZZ PSA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-SEATBELT EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-SEATBELT EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>Seat Belt Education</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Seat Belt Education</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-TOBACCO</p>
<p>EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-TOBACCO</p>
<p>EDUCATION</p>
</blockquote></td>
<td><blockquote>
<p>Tobacco Cessation</p>
<p>Education</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Tobacco Cessation</p>
<p>Education</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WEIGHT</p>
</blockquote></td>
<td><blockquote>
<p>ZZVA-WEIGHT</p>
</blockquote></td>
<td><blockquote>
<p>Weight</p>
</blockquote></td>
<td><blockquote>
<p>ZZ Weight</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Exported National Reminders

#### VA-\*IHD 412 ELEVATED LDL REPORTING

1.  VA-\*IHD 412 LIPID PROFILE REPORTING
2.  VA-\*IHD ELEVATED LDL REPORTING
3.  VA-\*IHD LIPID PROFILE REPORTING
4.  VA-ANTIPSYCHOTIC MED SIDE EFF EVAL
5.  VA-DEPRESSION SCREENING
6.  VA-GEC REFERRAL CARE COORDINATION
7.  VA-GEC REFERRAL CARE RECOMMENDATION
8.  VA-GEC REFERRAL NURSING ASSESSMENT
9.  VA-GEC REFERRAL SOCIAL SERVICES
10. VA-GEC REFERRAL TERM SET (CC)
11. VA-GEC REFERRAL TERM SET (CR)
12. VA-GEC REFERRAL TERM SET (NA)
13. VA-GEC REFERRAL TERM SET (SS)
14. VA-HEP C RISK ASSESSMENT
15. VA-HTN ASSESSMENT BP \>=140/90
16. VA-HTN ASSESSMENT BP \>=160/100
17. VA-HTN LIFESTYLE EDUCATION
18. VA-IHD ELEVATED LDL
19. VA-IHD LIPID PROFILE
20. VA-IRAQ & AFGHAN POST-DEPLOY SCREEN
21. VA-MST SCREENING
22. VA-NATIONAL EPI LAB EXTRACT
23. VA-NATIONAL EPI RX EXTRACT
24. VA-POS DEPRESSION SCREEN FOLLOWUP
25. VA-QUERI REPORT IHD ELEVATED LDL
26. VA-QUERI REPORT LIPID STATUS
27. VA-WH MAMMOGRAM REVIEW RESULTS
28. VA-WH MAMMOGRAM SCREENING
29. VA-WH PAP SMEAR REVIEW RESULTS
30. VA-WH PAP SMEAR SCREENING

> Exported National Dialogs

1.  VA-AIMS
2.  VA-DEPRESSION ASSESSMENT
3.  VA-DEPRESSION SCREEN
4.  VA-GEC REFERRAL CARE COORDINATION
5.  VA-GEC REFERRAL CARE RECOMMENDATION
6.  VA-GEC REFERRAL NURSING ASSESSMENT
7.  VA-GEC REFERRAL SOCIAL SERVICES
8.  VA-HEP C RISK ASSESSMENT
9.  VA-HTN ELEVATED BP\>140/90
10. VA-HTN ELEVATED BP\>160/100
11. VA-HTN LIFESTYLE EDUCATION
12. VA-IHD ELEVATED LDL
13. VA-IHD LIPID PROFILE
14. VA-IRAQ & AFGHANISTAN POST DEPLOYMENT SCREENING
15. VA-MST SCREENING
16. VA-WH MAMMOGRAM REVIEW RESULTS
17. VA-WH MAMMOGRAM SCREENING
18. VA-WH PAP SMEAR REVIEW RESULTS
19. VA-WH PAP SMEAR SCREENING

> <span id="Appendix_D:_Status_Enhancements" class="anchor"></span><u>Appendix D: Status Enhancements</u>

> The status field in the reminder definition has been modified to work with Reminder terms. Assumptions for the rules for this prompt:

1.  The status field will not appear if the term has different types of finding items (e.g., Radiology procedure and a drug finding item)
2.  If the term contains drug finding items or taxonomies, the user will see the status field, but they will not be able to edit the field if the values in the RX TYPE are different or the Taxonomy types are different.
3.  If the Reminder Term contains drugs finding items, the only status that will display will be the status that corresponds to the RX TYPE at the term level. And a blank RX TYPE will be considered as if the user enters “ALL” at the RX TYPE.
4.  The Reminder Definition RX TYPE will override the term RX TYPE. So if the user has set up multiple drug finding items in the term and the RX TYPE is set to Inpatient and then they set the RX TYPE at the definition level to Outpatient, the user will only be able to select statuses that correspond to a RX TYPE of Outpatient.

> RXTYPE controls the search for medications. The possible RXTYPEs are: A - All

> I - Inpatient

> N - Non-VA meds O - Outpatient

> You may use any combination of the above in a comma-separated list.

> For example I,N would search for inpatient medications and non-VA meds.

> The default is to search for all possible types of medications. So a blank RXTYPE is equivalent to A.

#### Default Statuses

<table>
<colgroup>
<col style="width: 55%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Finding Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Status</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Inpatient Pharmacy</p>
</blockquote></td>
<td><blockquote>
<p>active</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Outpatient Pharmacy</p>
</blockquote></td>
<td><blockquote>
<p>active, suspended</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Orderable Item</p>
</blockquote></td>
<td><blockquote>
<p>active</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Problem List</p>
</blockquote></td>
<td><blockquote>
<p>active</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Radiology</p>
</blockquote></td>
<td><blockquote>
<p>active</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Non-VA meds

> Changes in the RXTYPE field were made to support the use of non-VA meds in Reminders.

> “A” replaces the previous “B”. During the installation of V. 2.0, all “B” values will be changed to “A”. If RXTYPE is null, then it will be treated like an “A”. If RXTYPE includes non-VA meds, they will be searched for automatically, with no changes to the definition or term. This works as follows: Non-VA meds are stored by Pharmacy Orderable item and not by dispense drug; however, a dispense drug entry can have a pointer to the Pharmacy Orderable Item. If the pointer exists and RXTYPE allows it, then a search for the corresponding non-VA med will be made.

### Status list

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 2 provides a Status List for finding types that have a status:

- Inpatient pharmacy
- Outpatient pharmacy
- Orders
- Problem List
- Radiology

> To be true, a finding has to have a status on the list, which is a change from V. 1.5, where status was not used for drugs. Your reminders that use these finding types may work differently in V. 2.0

#### Pharmacy Statuses

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 30%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Status</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>*</p>
</blockquote></td>
<td><blockquote>
<p>Wildcard</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE (NOI)</p>
</blockquote></td>
<td><blockquote>
<p>Rx is active – edit, renewal, D/C, copy, refill, partial etc., could be done</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>DATE OF DEATH</p>
<p>ENTERED (N)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>DELETED (O)</p>
</blockquote></td>
<td><blockquote>
<p>Manual delete by the supervisor – same as Rx does not exist; never shown in the profile or reports</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>DISCONTINUED (NOI)</p>
</blockquote></td>
<td><blockquote>
<p>Any D/C via the backdoor –Manual D/C, D/C due to</p>
<p>Renewal, D/C due to duplicate drug, D/C due to Drug- Drug interaction</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>DISCONTINUED (EDIT) (OI)</p>
</blockquote></td>
<td><blockquote>
<p>Any edit through the backdoor for an active Rx that results in a new Rx will have this set. This will be displayed in the patient profile with status ‘DE’</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>DISCONTINUED</p>
<p>(RENEWAL) (I)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>DISCONTINUED BY PROVIDER (O)</p>
</blockquote></td>
<td><blockquote>
<p>D/C via CPRS by the provider</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>DONE (O)</p>
</blockquote></td>
<td><blockquote>
<p>Not used</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>DRUG INTERACTIONS (O)</p>
</blockquote></td>
<td><blockquote>
<p>Pending due to Drug Interactions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>EXPIRED (OI)</p>
</blockquote></td>
<td><blockquote>
<p>Expired Rx, copy, partials, D/C are allowed</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>HOLD (OI)</p>
</blockquote></td>
<td><blockquote>
<p>When a Rx is put on hold, no action is allowed except D/C until it is taken off hold</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>NON-VERIFIED (I)</p>
</blockquote></td>
<td><blockquote>
<p>CPRS orders completed by a pharmacy tech. (not holding PSORPH key), need verification by a</p>
<p>Pharmacist (holder of PSORPH key)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>NON-VERIFIED (O)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>ON CALL (I)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>PROVIDER HOLD (O)</p>
</blockquote></td>
<td><blockquote>
<p>On hold via CPRS by the provider</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>PURGE (I)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>REFILL (O)</p>
</blockquote></td>
<td><blockquote>
<p>Not used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>REINSTATED (I)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>RENEWED (I)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 30%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>20</p>
</blockquote></th>
<th><blockquote>
<p>SUSPENDED (O)</p>
</blockquote></th>
<th><blockquote>
<p>An active Rx that has a future fill date</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> N=Non-VA Meds; O=Outpatient; I=Inpatient

> Editing a Status List

> You are prompted for a status only for those findings that have a status.

#### Example: (under Reminder Definition Management Option/RE Add/Edit Reminder Definition)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 72%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>*</p>
</blockquote></th>
<th><blockquote>
<p>WildCard</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>ACTIVE (NOI)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>DATE OF DEATH ENTERED</p>
</blockquote></td>
<td><blockquote>
<p>(N)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>DELETED (O)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>DISCONTINUED (NOI)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

13. NON-VERIFIED (O)
14. ON CALL (I)
15. PROVIDER HOLD (O)
16. PURGE (I)
17. REFILL (O)
18. REINSTATED (I)
19. RENEWED (I)
20. SUSPENDED (O)

> Select a Medication Status from the status list or enter '^' to Quit: 1 ACTIVE (NOI)

> Statuses already defined for this finding item: ACTIVE

> Select one of the following:

> A ADD STATUS

> D DELETE A STATUS

> DA DELETE ALL STATUSES

> S SAVE AND QUIT

> Q QUIT WITHOUT SAVING CHANGES

> Enter response: a ADD STATUS

> Select one of the following:

> \* WildCard

1.  ACTIVE (NOI)
2.  DATE OF DEATH ENTERED (N)
3.  DELETED (O)
4.  DISCONTINUED (NOI)
5.  DISCONTINUED (EDIT) (OI)
6.  DISCONTINUED (RENEWAL) (I)
7.  DISCONTINUED BY PROVIDER (O)
8.  DONE (O)
9.  DRUG INTERACTIONS (O)
10. EXPIRED (OI)
11. HOLD (OI)
12. NON VERIFIED (I)
13. NON-VERIFIED (O)
14. ON CALL (I)
15. PROVIDER HOLD (O)
16. PURGE (I)
17. REFILL (O)
18. REINSTATED (I)
19. RENEWED (I)
20. SUSPENDED (O)

> Select a Medication Status from the status list or enter '^' to Quit: 2 DATE OF DEATH ENTERED (N)

> Statuses already defined for this finding item: ACTIVE

> DATE OF DEATH ENTERED

> Select one of the following:

> A ADD STATUS

> D DELETE A STATUS

> DA DELETE ALL STATUSES

> S SAVE AND QUIT

> Q QUIT WITHOUT SAVING CHANGES

### New reminder status:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### CNBD for CanNot Be Determined. Clinical Maintenance display.

> The “Information about the reminder evaluation:” section is new.

> A warning message will be sent when the status can’t be determined.

> Example:

## Index 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> AAC SAS Files, 79
> Acronyms, 79
> Action, 39
> Allocation Errors, 75
> APPENDIX B: Glossary— Acronyms and Definitions, 79
> APPENDIX A: Hints and Tips, 71 APPENDIX C: NATIONAL REMINDERS
> RESCISSION, 82
> APPENDIX D: Status Enhancements, 86 Applicable, 79
> Automatic QUERI Extracts/ Transmission, 29
> Chapter 1: IHD and MH Phase 2 Setup, 15 Chapter 2: Set up VA-Geriatric Extended
> Care (GEC) Referral, 33, 48, 49, 50 Chapter 3: Code Set Versioning Changes in
> Reminders, 53
> Chapter 4: My HealtheVet, 62 Child Note Titles, 44
> Code Set Versioning Changes in Reminders, 53
> Computed Finding – Location, 74 CONDITION Enhancements, 2
> CPT, 53
> Custom Date Due, 2 Default Statuses, 86
> Definitions, 79
> Dialog Taxonomies, 59
> Drug for patient cohort logic, 74 Due, 79
> Edit Taxonomy Item’s ICD0 Low and High Code Example, 56
> Exported National Dialogs, 85 Exported National Reminders, 84 Extract Parameter, 79
> Extract Run, 80
> Extract Summary, 27, 79 Finding Count Rules, 80 finding date search, 2 Finding Group, 80
> Forced Value in Dialogs, 71 GEC, 33, 34, 48, 49, 50
> GEC Consult Order, 35 GEC Health Factors, 34
> GEC Interdisciplinary Notes, 44 GEC Referral Ad hoc Reports, 50
> GEC Referral Reminders, 35 GEC Referral Reports, 51 GEC Reminder Terms, 51
> GEC Status Check, 46, 47, 48, 49, 50
> Glossary, 79
> Health Information Portability and Accountability Act (HIPAA), 53
> HIPAA, 53
> HL LOGICAL LINK, 28
> HL7 Transmissions, 80
> ICD0, 53
> ICD9, 53
> IHD Reminder Definitions, 15
> IHD terms that *must* be mapped, 18, 19 Impact on Sites, 11, 12, 13
> Inactive Codes Mail Message, 58 List Rules, 80
> Location List finding, 2
> logical Link in the HL7 package, 28 mail messages, 30
> manual run, 25, 26
> Map local findings, 18, 22, 23
> Mental Health Reminder Terms, 22, 23 Mental Health Reminders, 16
> MH Term Mapping, 24 National Acronym Directory, 79 National Dialogs, 85
> National Reminders, 84
> NATIONAL REMINDERS RESCISSION, 82
> Not Applicable, 80
> Outpatient Pharmacy Statuses, 87 Patient List, 80
> patient lists, 28
> Pre-mapped Terms, 19, 20
> Print labels, 71
> PXRM EXTRACT MANAGEMENT, 25, 26
> PXRMCS INACTIVE DIALOG CODES, 58
> Rank Frequency, 76
> Reminder Definitions, 80
> Reminder Dialog, 25, 80 Reminder Patient List, 80
> Reminder report on an individual finding item, 71
> Reminder Terms, 80
> Reminder Test, 25
> Reminder Totals, 80 Reminders Due Report, 25 Report Reminders, 81 Reporting Period Extract, 81
> Set Up Consult Services (SS), 39 Standards Development Organization
> (SDO), 53
> Status list, 2, 87
> Statuses, 87
> Taxonomy option changes, 55, 56, 57
> Test option, 2
> TIU Document Definitions, 44 TIU Interdisciplinary (ID) note, 44 Transmission History, 30
> Transmission Run, 81
> VA-\*IHD 412 ELEVATED LDL REPORTING, 16
> VA-\*IHD 412 LIPID PROFILE REPORTING, 16
> VA-\*IHD ELEVATED LDL REPORTING, 15
> VA-\*IHD LIPID PROFILE REPORTING, 15
> VA-ANTIPSYCHOTIC MED SIDE EFF
> EVAL Terms, 23
> VA-DEPRESSION SCREENING Terms, 22
> VA-Geriatric Extended Care, 33, 34, 48, 49,
> 50
> VA-IHD ELEVATED LDL, 15 VA-IHD LIPID PROFILE, 15
> VA-POS DEPRESSION SCREEN FOLLOWUP Terms, 23
> WYSIWYG, 73
