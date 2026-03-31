---
title: HBPC User Manual
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: 
app_code: HBPC
app_name: Home Based Primary Care
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: 
  - 44
  - 631
  - 632
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - report
  - date
  - patient
  - table
  - contents
  - class
  - hbpc
  - home
  - hbhc
  - discharge
page_count: 0
word_count: 26879
section_count: 41
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbh_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbh_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=68"
---

Home Based Primary CareUser Manual

![](hbpc-user-manual/001.png)

Version 1.0March 2001Revised August 2021Department of Veterans Affairs (VA)Office of Information and Technology (OIT)Revision History

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 39%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Patch #</strong></th>
<th><strong>Page</strong></th>
<th><strong>Description</strong></th>
<th><strong>Project Manager</strong></th>
<th><strong>Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>August 2021</td>
<td>32</td>
<td>Title, i, iii, II-4 – II-27, II-30, III-2 IV-1, IV-9, IV-11, VII-4, VIII-2</td>
<td><p>HBH*1*32:</p>
<ul>
<li><p>HBHC Edit Provider option now utilizes ListMan</p></li>
<li><p>Disabled the HBPC Provider File Report option and added a <strong><u>Note</u></strong> in that section</p></li>
<li><p>Added the disabled comment to <strong><u>HBHCRP8</u></strong></p></li>
<li><p>Added the PARENT SITE prompt to the <strong><u>System Parameters Edit</u></strong> option section where the choices for that prompt are configured</p></li>
<li><p>Added the new PARENT SITE prompt <strong><u>Note</u></strong> in the, Adding Evaluation/Admission, Discharge and Visit Data through HBPC section</p></li>
<li><p>Added 2 new PARENT SITE prompt <strong><u>Notes</u></strong> in the, Evaluation/Admission Data Entry section</p></li>
<li><p>Updated the <strong><u>System Parameters Edit</u></strong> wording</p></li>
<li><p>Updated the <strong><u>System Parameters Edit Example</u></strong> to include the PARENT SITE prompt</p></li>
<li><p>Updated the entire <strong><u>Provider File Data Entry</u></strong> section and added all the subsections underneath it</p></li>
<li><p>Added the <strong><u>PARENT SITE Field Auditing</u></strong> section and the subsections for the two methods underneath it</p></li>
<li><p>Added <strong><u>Parent Site</u></strong> to the Exiting and Field Jumping section</p></li>
<li><p>Added a <strong><u>Note</u></strong> in the Medical Foster Home Demographic section</p></li>
<li><p>Added the subsection <strong><u>Parent Site Information</u></strong> for the Medical Foster Home Demographic section</p></li>
<li><p>Added <strong><u>Parent Site</u></strong> to the Glossary</p></li>
<li><p>Updated the Title page, Revision History, Table of Contents, List of Figures (added), Index, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>May 2015</td>
<td>28</td>
<td><p>i</p>
<p>iv - vi</p>
<p><a href="#total-visits-by-date-range-report-80">V-14</a>, <a href="#total-visits-by-date-range-report-80">V15</a></p></td>
<td><p>Patch HBH*1*28 May 2015</p>
<p>- Updated Title Page</p>
<p>- Updated Revision History</p>
<p>- Updated Table of Contents</p>
<p>- Updated listing of CPT codes that are omitted from the report.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>August 2014</td>
<td>25</td>
<td><p>i-vi,</p>
<p><a href="#flow">I-2</a>,</p>
<p><a href="#icd1">III-1</a>,</p>
<p><a href="#icd2">III-2</a>,</p>
<p><a href="#icd6_1">IV-6</a>,</p>
<p><a href="#icd3">IV-12</a>,</p>
<p><a href="#icd4">IV-21</a>,</p>
<p><a href="#namechange1">V-1</a>,</p>
<p><a href="#icd5">V-7</a>,<br />
<a href="#icd6">V-12</a>,</p>
<p><a href="#icd7">V-17</a>,</p>
<p><a href="#icd8">V-21</a>,<br />
<a href="#screen2">VI-7</a>, <a href="#icd9">VII-33</a></p></td>
<td><p>Patch HBH*1*25 August 2014</p>
<p>- Updated Title Page</p>
<p>- Updated Revision History</p>
<p>- Updated Table of Contents</p>
<p>- Updated Data Flow Chart for ICD-10 (p. <a href="#flow">I-2</a>)</p>
<p>- Report renamed to ICD Code/Dx Text Date Range Report (pp. <a href="#icd1">III-1</a>, <a href="#namechange1">V-1</a>, <a href="#icd6">V-12</a>)</p>
<p>- Report renamed to Active Census with ICD Code/Text Report (pp. <a href="#icd2">III-2</a>, <a href="#namechange1">V-1</a>, <a href="#icd7">V-17</a>, <a href="#icd8">V-21</a>)</p>
<p>- Note added regarding ICD Code reports (pp. <a href="#p25_V_7">V-7</a>, <a href="#p25_V_12">V-12</a>, <a href="#p25_V_21">V-21</a>, <a href="#p25_VI_7">VI-7</a></p>
<p>- Updated to include ICD-10 (pp. <a href="#icd3">IV-12</a>, <a href="#icd4">IV-21</a>, <a href="#icd5">V-7</a>, <a href="#icd6">V-12</a>, <a href="#icd8">V-21</a>, <a href="#icd9">VII-33</a>)</p>
<p>- Updated screen shot for ICD-10 (pp. <a href="#icd5">V-7</a>, <a href="#icd6">V-12</a>, <a href="#icd8">V-21</a>, <a href="#screen2">VI-7</a>)</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>August 2009</td>
<td>24</td>
<td>VII-1 to VII 60</td>
<td>Patch HBH*1*24 August 2009 – Medical Foster Home (MFH) functionality added.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>February 2005</td>
<td>21</td>
<td><p>III-2</p>
<p>V-1, 17,19 &amp; 20</p></td>
<td><p>Patch HBH*1*21 January 2005 – New option added to the Census Reports Menu.</p>
<p>- Address Included Program Census (132)</p>
<p>- Expanded Program Census Report (80)</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>February 2005</td>
<td>21</td>
<td><p>III-2</p>
<p>V-1, 16</p></td>
<td><p>Patch HBH*1*21 January 2005 – New option added to the Reports Menu.</p>
<p>-Patient Days of Care by Date Range Report (80)</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>January 2003</td>
<td></td>
<td></td>
<td>Race: Obsolete Field 2003</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>January 2003</td>
<td></td>
<td></td>
<td>Race: Obsolete Field 2003</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>January 2003</td>
<td></td>
<td></td>
<td>Race: Obsolete Field 2003</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>January 2003</td>
<td></td>
<td></td>
<td>Removed Race: Obsolete Field</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Package Management](#package-management)
  - [Application Coordinator](#application-coordinator)
- [# Implementing and Maintaining the Software](#implementing-and-maintaining-the-software)
  - [Installation Check List for the Application Coordinator](#installation-check-list-for-the-application-coordinator)
  - [Assigning Menus and Keys](#assigning-menus-and-keys)
    - [HBPC Information System Menu](#hbpc-information-system-menu)
    - [Reports Menu](#reports-menu)
    - [[^1]Auto-Queue File Update](#1auto-queue-file-update)
  - [Assigning the HBH Mail Group](#assigning-the-hbh-mail-group)
  - [Using the Manager Menu in Implementation and Maintenance](#using-the-manager-menu-in-implementation-and-maintenance)
    - [System Parameters Edit](#system-parameters-edit)
    - [Provider File Data Entry](#provider-file-data-entry)
    - [Clinic File Data Entry](#clinic-file-data-entry)
    - [Team File Data Entry](#team-file-data-entry)
    - [HBPC Provider File Report (132) - DISABLED](#hbpc-provider-file-report-132-disabled)
    - [[^2]Pseudo Social Security Number Report (80)](#2pseudo-social-security-number-report-80)
    - [Re-Transmit File to Austin](#re-transmit-file-to-austin)
- [# Package Operations](#package-operations)
  - [Conventions Used in Examples](#conventions-used-in-examples)
  - [Package Online Help](#package-online-help)
  - [HBPC Information System Menu](#hbpc-information-system-menu-1)
- [# Adding and Editing Patient Data](#adding-and-editing-patient-data)
  - [Adding Evaluation/Admission, Discharge and Visit Data through HBPC](#adding-evaluationadmission-discharge-and-visit-data-through-hbpc)
  - [Adding Visit Data through other Encounter Software](#adding-visit-data-through-other-encounter-software)
  - [[^7]Appointment Management](#7appointment-management)
    - [Example: Making an Appointment for a Patient](#example-making-an-appointment-for-a-patient)
    - [Example: Using Check Out in Appointment Management](#example-using-check-out-in-appointment-management)
  - [Evaluation/Admission Data Entry](#evaluationadmission-data-entry)
    - [Complete Episode of Care](#complete-episode-of-care)
    - [Creating an Additional Episode of Care for a Patient](#creating-an-additional-episode-of-care-for-a-patient)
    - [Patient Demographic Information](#patient-demographic-information)
    - [Exiting and Field Jumping](#exiting-and-field-jumping)
  - [Discharge Data Entry](#discharge-data-entry)
    - [Complete Episode of Care](#complete-episode-of-care-1)
    - [Default Values](#default-values)
    - [Exiting and Field Jumping](#exiting-and-field-jumping-1)
- [Using the Reports Menu](#using-the-reports-menu)
  - [Evaluation/Admission Data Report by Patient (80)](#evaluationadmission-data-report-by-patient-80)
  - [[^13]Patient Visit Data Report (80)](#13patient-visit-data-report-80)
  - [Discharge Data Report by Patient (80)](#discharge-data-report-by-patient-80)
  - [Episode of Care/Length of Stay Report (80)](#episode-of-carelength-of-stay-report-80)
  - [Admissions/Discharges by Date Range Report (132)](#admissionsdischarges-by-date-range-report-132)
  - [[^15]Rejections from HBPC Program Report (132)](#15rejections-from-hbpc-program-report-132)
  - [[^16]Visit Data by Date Range Report (80)](#16visit-data-by-date-range-report-80)
  - [[^17]CPT Code Summary Report (80)](#17cpt-code-summary-report-80)
  - [[^18][^19]Provider CPT Code Summary Report (80)](#1819provider-cpt-code-summary-report-80)
  - [[^20]ICD Code/Dx Text by Date Range Report (80)](#20icd-codedx-text-by-date-range-report-80)
  - [[^21]Unique Patients by Date Range Summary Report (80)](#21unique-patients-by-date-range-summary-report-80)
  - [[^22]Total Visits by Date Range Report (80)](#22total-visits-by-date-range-report-80)
  - [[^24] Patient Days of Care by Date Range Report (80)](#24-patient-days-of-care-by-date-range-report-80)
  - [Census Reports Menu ...](#census-reports-menu)
    - [Program Census Report (80)](#program-census-report-80)
    - [[^28]Address Included Program Census (132)](#28address-included-program-census-132)
    - [[^29]Expanded Program Census Report (80)](#29expanded-program-census-report-80)
    - [[^30]Active Census with ICD Code/Text Report (132)](#30active-census-with-icd-codetext-report-132)
    - [Team Census Report (80)](#team-census-report-80)
    - [[^33]Case Manager Census Report (132)](#33case-manager-census-report-132)
    - [[^34]Provider Census Report (132)](#34provider-census-report-132)
- [Transmitting Data to Austin](#transmitting-data-to-austin)
  - [Build/Verify Transmission File](#buildverify-transmission-file)
  - [Form Errors Report (80)](#form-errors-report-80)
  - [Edit Form Errors Data](#edit-form-errors-data)
  - [Transmit File to Austin](#transmit-file-to-austin)
  - [[^42]Print Transmit History Report (80)](#42print-transmit-history-report-80)
- [Medical Foster Home Functionality](#medical-foster-home-functionality)
  - [Background](#background)
  - [MFH Basics](#mfh-basics)
  - [Using the Medical Foster Home (MFH) Menu](#using-the-medical-foster-home-mfh-menu)
    - [Blank MFH Worksheet Report (80)](#blank-mfh-worksheet-report-80)
    - [Demographic Data Entry for MFH](#demographic-data-entry-for-mfh)
    - [Parent Site Information](#parent-site-information)
    - [Inspection Data Entry for MFH](#inspection-data-entry-for-mfh)
    - [Training Data Entry for MFH](#training-data-entry-for-mfh)
    - [Edit MFH Form Errors Data](#edit-mfh-form-errors-data)
  - [MFH Reports ...](#mfh-reports)
    - [MFH File Data Report (132)](#mfh-file-data-report-132)
    - [Worksheet for MFH (80)](#worksheet-for-mfh-80)
    - [Inspection/Training Due Report for MFH (80)](#inspectiontraining-due-report-for-mfh-80)
    - [Rate Paid Report for MFH (80)](#rate-paid-report-for-mfh-80)
    - [License Due for MFH Report (80)](#license-due-for-mfh-report-80)
    - [Caregiver Age Report (132)](#caregiver-age-report-132)
    - [Form Errors Report for MFH (80)](#form-errors-report-for-mfh-80)
    - [Delimited Text File Output Menu for MFH ...](#delimited-text-file-output-menu-for-mfh)
    - [Inspection/Training Delimited Text File Output](#inspectiontraining-delimited-text-file-output)
    - [Rate Paid Delimited Text File Output](#rate-paid-delimited-text-file-output)
  - [Queued Options](#queued-options)
    - [Auto-queued Inspection/Training Reminder e-mail](#auto-queued-inspectiontraining-reminder-e-mail)
    - [Auto-queued License Due Reminder e-mail](#auto-queued-license-due-reminder-e-mail)
    - [Evaluation/Admission Data Entry](#evaluationadmission-data-entry-1)
    - [Patient Days of Care by Date Range Report (80)](#patient-days-of-care-by-date-range-report-80)
    - [Program Census Report (80)](#program-census-report-80-1)
    - [Build/Verify Transmission File](#buildverify-transmission-file-1)
    - [Form Errors Report (80)](#form-errors-report-80-1)
    - [Edit Form Errors Data](#edit-form-errors-data-1)
    - [Transmit File to Austin](#transmit-file-to-austin-1)
    - [Print Transmit History Report (80)](#print-transmit-history-report-80)
- [Glossary](#glossary)
- [Worksheets](#worksheets)
  - [Parameters, Teams, and Clinics](#parameters-teams-and-clinics)
- [Index](#index)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Based Primary Care (HBPC) package formally known as Hospital Based Home Care (HBHC) is a VISTA application developed for use by the HBPC Programs at the medical centers. The software:

- Allows the entry and storage of information on all Evaluations/Admissions,
- Scans Outpatient Encounters for all HBPC visits and stores the visit data,
- Allows the entry and storage of HBPC Discharge information,
- Provides reports covering all aspects of the data,
- Informs the staff when incomplete records for transmission are found,
- Transmits the data to Austin using MailMan.

## Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known legal requirements associated with the HBPC software.

## Application Coordinator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Application Coordinator sets up and maintains the data used by the package. At some sites, this same person may also be given the responsibility to assign menus and keys to new users. Generally, this person trains new users and troubleshoots any problems that arise with the software. (See <u>Implementing and Maintaining the Software</u>)

> **NOTE:** Some sites do not give users the ability to cancel an appointment or delete a checkout. At those sites, the Application Coordinator should assume that responsibility.

<span id="flow" class="anchor"></span>HBPC Data Flow Chart

|               |         |         |         |
|---------------|---------|---------|---------|
| Appt Mgmt | TIU | PCE | ECS |

# # Implementing and Maintaining the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter is designed for the HBPC Application Coordinator who is responsible for the implementation and maintenance of the software. Implementation entails the compilation of specific information that will be added to the package's database after the package is installed. The information includes who will be using the package, which menus and keys they should own, and other data that is required for use in the package (clinics, teams, etc.).

## Installation Check List for the Application Coordinator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to installation of the package:

- Determine the official startup date for HBPC package visit records to be electronically transmitted to Austin and give this information to the IRM (Information Resources Management) support person who will be installing the package.
- Review this chapter to get an overview of how menus and keys should be assigned and the types of data that you will need to implement the package.
- Complete the <u>Worksheets</u> at the end of this manual. The information will be used to complete the options System Parameters Edit, Clinic File Data Entry, Team File Data Entry and Provider File Data Entry. Look to those options for descriptions of the information you need for the worksheets.
- If you cannot assign menus and/or users to mail groups, give a copy of the Provider File Data Worksheet to the IRM support person who will be assigning the menus, keys, and mail group membership to users of the package.

After Installation of the package:

- Make sure you are assigned the HBPC Information System Menu.
- Make sure you are assigned the HBHC MANAGER and HBHC TRANSMIT keys.
- Set the system parameters using the System Parameters Edit option.
- Enter all Clinics used by the HBPC Program using the Clinic File Data Entry option.
- Enter all teams used by your HBPC Program using the Team File Data Entry option. Note: It is required that all providers for the program be assigned to a team.
- Add all HBPC providers using the Provider File Data Entry option utilizing the provider number scheme detailed in the help text.
- If not already done by IRM, assign menus and, where appropriate, keys to the users.
- Ask the IRM support person to set the Auto-queue File Update \[HBHC AUTO-QUEUED FILE UPDATE\] option to run daily, shortly after midnight.
- Ask IRM to assign members to the HBH mail group. These members receive messages concerning data errors and transmission confirmations.
- If not done by IRM, use VA FileMan to populate the Valid State Code file \#631.8 with any state codes that are used by your site.
- Finally, ask IRM to assign file access.

## Assigning Menus and Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HBPC Information System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign this menu to the Application Coordinator and any users who will be adding/editing data in the package.

> Any person assigned this menu who is also responsible for implementing and maintaining the package needs the HBHC MANAGER key to use the Manager Menu.

> Any person assigned this menu who is also responsible for transmitting the data to Austin, needs the HBHC TRANSMIT key. (This key should be limited to only those few people who will transmit the data.)

### Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There may be some users who will not be entering data but who need access to reports. Assign this menu to those users.

> PCE Clinical Reports Menu

> While the PCE Clinical Reports \[PXRR CLINICAL REPORTS\] menu is not a part of the HBPC software, the options can be useful in addition to the HBPC reports. See the PCE user manual for information on the use of these options.

> Patient Activity by Location \[PXRR PATIENT ACTIVITY BY LOC\]

> Caseload Profile by Clinic \[PXRR CASELOAD PROFILE BY CL\]

> PCE Encounter Summary \[PXRR PCE ENCOUNTER SUMMARY\]

> Diagnosis Ranked by Frequency \[PXRR MOST FREQUENT DIAGNOSES\]

> Location Encounter Counts \[PXRR LOCATION ENCOUNTER COUNTS\]

> Provider Encounter Counts \[PXRR PROVIDER ENCOUNTER COUNTS\]

### [^1]Auto-Queue File Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHC AUTO-QUEUED FILE UPDATE\]

This option is not attached to any menu and is not assigned to anyone. The option should be queued to run every day. It performs the HBHC Visit file \#632 update processing that is also found as part of the <u>Build/Verify Transmission File</u> option. The option runs against the Outpatient Encounter file \#409.68 covering the previous 7 days of appointments and updates the HBHC Visit file with both additions and cancellations for encounters.

If any errors are found during the Auto-queue File Update, the records with errors are placed in the HBHC Visit Error file \#634.2 and members of the HBH mail group are sent a mail message containing the following:

> Please run Form Errors Report option for HBHC errors to correct.

This gives you the opportunity to correct problems as they arise.

The HBHC Visit Error file is deleted and rebuilt as part of the scheduled auto-queued job. Therefore, the same record may be placed in the error file after each run over the 7 days if it is not corrected and you will receive a mail message each of those 7 days.

## Assigning the HBH Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Members of the HBH mail group receive data error messages after visit data is scanned. This group also receives any messages pertaining to the transmission of the data to Austin. Assign users to this mail group that will be responsible for correcting data or transmission errors.

## Using the Manager Menu in Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu is used to set up and maintain the system and is described fully in the following pages:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="system-parameters-edit" class="unnumbered">System Parameters Edit</h4></td>
<td>Contains default number of days to scan for data to be transmitted, transmit report printer, and parent site(s).</td>
</tr>
<tr class="even">
<td><h4 id="provider-file-data-entry" class="unnumbered">Provider File Data Entry</h4></td>
<td>Contains all the HBPC providers.</td>
</tr>
<tr class="odd">
<td><h4 id="clinic-file-data-entry" class="unnumbered">Clinic File Data Entry</h4></td>
<td><p>Contains all the HBPC clinics. Used when scanning for records to add to the HBHC Visit file.</p>
<p>Note: These clinics must exist in the Hospital Location file #44. The clinics must also exist in the HBHC Clinic file #631.6 for visits to be automatically added to the HBHC Visit file #632.</p></td>
</tr>
<tr class="even">
<td><h4 id="team-file-data-entry" class="unnumbered">Team File Data Entry</h4></td>
<td><p>Contains all the HBPC teams.</p>
<p>Note: There should be at least one team in this file.</p></td>
</tr>
<tr class="odd">
<td><h4 id="hbpc-provider-file-report-disabled" class="unnumbered">HBPC Provider File Report DISABLED</h4></td>
<td>The HBPC Provider File Report option was replaced with the <strong><u>PR Print Display</u></strong> action within the HBHC Edit Provider option</td>
</tr>
<tr class="even">
<td><h4 id="pseudo-social-security-number-report" class="unnumbered">Pseudo Social Security Number Report</h4></td>
<td>Displays invalid records containing pseudo (computer generated identification) SSNs.</td>
</tr>
<tr class="odd">
<td><h4 id="section-1" class="unnumbered"></h4></td>
<td></td>
</tr>
<tr class="even">
<td><h4 id="re-transmit-file-to-austin" class="unnumbered">Re-Transmit File to Austin</h4></td>
<td>This option is used only if Austin determines that it is needed.</td>
</tr>
</tbody>
</table>

### System Parameters Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHC EDIT SYSTEM PARAMETERS\]

Use this option to edit data in the HBHC System Parameters file \#631.9. You can enter or change:

- The number of days you want the package to scan back for appointments/encounters.
- The printer for the Transmit History Report.
- Site list configuration for the PARENT SITE prompt.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="number-of-visit-days-to-scan" class="unnumbered">Number of Visit Days to Scan</h4></td>
<td>The entry in this parameter is used by the package to determine the number of days to scan back through Outpatient Encounters for HBPC Clinic visits. (E.g., If the parameter is set at 7, all HBPC clinic appointments for the previous 7 days are added to the HBHC VISIT file. This parameter must be a number between 7 and 365 inclusive. Set the parameter to the lowest number that accurately reflects the data timelines for appointment management (e.g., if appointments are entered daily, then 7 would be appropriate).</td>
</tr>
<tr class="even">
<td><h4 id="transmit-report-printer" class="unnumbered"><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Transmit Report Printer</h4></td>
<td>This is the device that will print a copy of the Transmit History Report.</td>
</tr>
<tr class="odd">
<td><h4 id="parent-site" class="unnumbered">PARENT SITE</h4></td>
<td>This prompt is a required response and should be configured by each site to include the site options available that pertain to that site.</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patches HBH*1*6 July 1997 and HBH*1*8 January 1998 New field in file #631.9 (patch 6), added to System Parameters Edit (patch 8).<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

System Parameters Edit Example:

NUMBER OF VISIT DAYS TO SCAN: 7

TRANSMIT REPORT PRINTER: (Enter or select a printer for the Transmit Report.)

The "Parent Site" prompt selection should reflect the Austin

Mainframe HBPC Sanctioned Program facility number at your VA.

You must select a VA HBPC sanctioned site number or the HBPC

Admission Form will be rejected in Austin when the non-sanctioned

site number is used.

Select PARENT SITE:

#### PARENT SITE Field Auditing

The following audit information pertains to adding/deleting a parent site from the HBHC SYSTEM PARAMETERS (#631.9) file. Sites will need to contact a user with FileMan access at their site. There are two ways to audit a field in FileMan.

- AUDIT file inquiry
- View AUDIT trail on the file

#### AUDIT File Inqury

The advantage of this method is that the user’s name displays. The disadvantage is that the parent site name does not display.

In VA FileMan 22.2:

1.  Enter 5 at the Select Option prompt.
2.  Enter AUDIT at the Output from what File prompt.
3.  Enter 1 at the CHOOSE 1-2 prompt.
4.  Enter HBHC SYSTEM PARAMETERS at the Audit from what File prompt.

> **NOTE:** The inquiry is by date. Enter ?? to see a listing of dates.

5.  In the example below T, for today, was entered at the Select HBHC SYSTEM PARAMETER AUDIT prompt.
6.  Enter YES at the partial match to prompt.
7.  Enter YES at the Standard Captioned Output prompt.
8.  Enter NO at the Include Computed fields prompt.

> <span id="_Toc77590628" class="anchor"></span>Figure 1: AUDIT File Inquiry Example

> ![](hbpc-user-manual/002.png)

#### View AUDIT Trail on the File

The advantage of this method is that the audit information displays under each parent site. The disadvantage is that the user’s name does not display; However, the user’s internal entry number (IEN) from the NEW PERSON (#200) file is displayed.

> **NOTE:** Sometimes information for one parent site is displayed under the header for a different parent site depending on which parent sites are currently defined and which were deleted/added. Either way, the headers and details of the parent sites displayed in the are correct. This is how FileMan functions when storing and displaying audit information.

In VA FileMan 22.2:

1.  Enter 5 at the Select Option prompt.
2.  Enter HBHC SYSTEM PARAMETERS at the Audit from what File prompt.
3.  Enter YES at the Standard Captioned Output prompt.
4.  Enter NO at the Include Computed fields prompt.
5.  Enter YES at the Display Audit Trail prompt.

> <span id="_Toc77590629" class="anchor"></span>Figure 2: View AUDIT Trail on File Example

> ![](hbpc-user-manual/003.png)

### Provider File Data Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHC EDIT PROVIDER (631.4)\]

To track the work done by providers, the software needs a list of all the providers for the HBPC Program. Use this option to set up and maintain that list of providers in the HBHC Provider file \#631.4{XE “HBHC Provider file \#621.4: editing the file”}. The provider number creation scheme is detailed below and in the online help text.

Before using this option:

- HBPC teams should be added using the <u>Team File Data Entry</u>. Providers must belong to a team.
- All providers must first be members of the New Person file \#200.

#### Overview

ListMan layout is used for the Provider File Data Entry option. The Partial or full name prompt is the search method within this option and is the first prompt to be displayed. Four-digit provider numbers are assigned using the next available number containing the digits 0 through 9, where 0000 is not a valid number. There are 9999 assignable numbers and they operate independently at the VistA environment level. The next available number on the number wheel is assigned when adding a new provider. Only active provider information is displayed within this option.

<span id="_Toc77590630" class="anchor"></span>Figure 3: Example of Existing Matches for “Provid”

![](hbpc-user-manual/004.png)

The following sections will outline the actions presented at the bottom of the above figure.

- NP Display New Person Entries
- HP Display HBPC Provider(s)
- ALL Display All HBPC Providers
- AD Add New HBPC Provider
- ED Edit HBPC Provider File
- DD Detailed Display
- PR Print Display

#### NP Display New Person Entries

The NP action allows users to display new person entries. Users with an asterisk next to their name are providers. This action needs to be performed to add a new person entry, as a provider, with AD Add New HBPC Provider.

1.  Navigate to the Manager Menu option.
2.  Enter the Provider File Data Entry option.
3.  Enter a partial or full name in the Partial or full name prompt.

> **NOTE:** If no search results are found, the following message displays, “No matching entries in the NEW PERSON (#200) file.”

4.  Enter NP at the Select Item(s) prompt.

> <span id="_Toc77590631" class="anchor"></span>Figure 4: NP Provider File Data Entry Example

> ![](hbpc-user-manual/005.png)

5.  Enter a partial or full name in the Partial or full name prompt.

> <span id="_Toc77590632" class="anchor"></span>Figure 5: NP Provider File Data Entry Example Continued

> ![](hbpc-user-manual/006.png)

6.  The actions that can be performed from here are AD Add New HBPC Provider, DD Detailed Display, or PR Print Display.
    1.  Enter AD to add a user in the displayed list as a provider. Additional details are in the AD Add New HBPC Provider section.

> <span id="_Toc77590633" class="anchor"></span>Figure 6: AD Action within NP Provider File Data Example

![](hbpc-user-manual/007.png)

> **NOTE:** The \* symbol denotes a user is a provider in the New Person Entries list. Trying to add a provider will prompt the user with the message, “This provider has already been added with the HBPC Provider number of, their provider number.”

> <span id="_Toc77590634" class="anchor"></span>Figure 7: AD Action within NP Provider File Data Example Continued

> ![](hbpc-user-manual/008.png)

2.  Enter DD to see information about the user. Additional details are in the DD Detailed Display section.

> <span id="_Toc77590635" class="anchor"></span>Figure 8: DD Action within NP Provider File Data Example

![](hbpc-user-manual/009.png)

3.  Enter PR for print details of the active screen. The figure below will the NP screen displayed in the application using HOME. Additional details are in the PR Print Display section.

> <span id="_Toc77590636" class="anchor"></span>Figure 9: PR Action within NP Provider File Data Example

> ![](hbpc-user-manual/010.png)

#### HP Display HBPC Provider(s)

The HP action allows users to display specified active HBPC providers.

1.  Navigate to the Manager Menu option.
2.  Enter the Provider File Data Entry option.
3.  Enter a partial or full name in the Partial or full name prompt.

> **NOTE:** If no search results are found, the following message displays, “No matching entries in the NEW PERSON (#200) file.”

4.  Enter HP at the Select Item(s) prompt.

> <span id="_Toc77590637" class="anchor"></span>Figure 10: HP Provider File Data Entry Example

> ![](hbpc-user-manual/011.png)

5.  Enter a partial or full name in the Partial or full name prompt.

> <span id="_Toc77590638" class="anchor"></span>Figure 11: HP Provider File Data Entry Example Continued

> ![](hbpc-user-manual/012.png)

6.  The actions that can be performed from here are ED Edit HBPC Provider File, DD Detailed Display, or PR Print Display.
    1.  Enter ED to edit a provider’s associated team. Additional details are in the ED EDIT HBPC Provider File section.

> <span id="_Toc77590639" class="anchor"></span>Figure 12: ED Action within HP Provider File Data Example

![](hbpc-user-manual/013.png)

> **NOTE:** Only the HBHC Team prompt can be edited.

2.  Enter DD to see information about the user. Additional details are in the DD Detailed Display section.

> <span id="_Toc77590640" class="anchor"></span>Figure 13: DD Action within HP Provider File Data Example

![](hbpc-user-manual/014.png)

3.  Enter PR to view print details on the screen or send them to a device. Additional details are in the PR Print Display section.

> <span id="_Toc77590641" class="anchor"></span>Figure 14: PR Action within HP Provider File Data Example

![](hbpc-user-manual/015.png)

#### ALL Display All HBPC Providers

The ALL action allows users to display all active HBPC providers. The list can be displayed alphabetically or numerically.

1.  Navigate to the Manager Menu option.
2.  Enter the Provider File Data Entry option.
3.  Enter a partial or full name in the Partial or full name prompt.

> **NOTE:** If no search results are found, the following message displays, “No matching entries in the NEW PERSON (#200) file.”

4.  Enter ALL at the Select Item(s) prompt.
5.  Enter A or N at the Sort alphabetically or numerically prompt.

> <span id="_Toc77590642" class="anchor"></span>Figure 15: ALL Provider File Data Entry Example

> ![](hbpc-user-manual/016.png)

6.  The actions that can be performed from here are ED Edit HBPC Provider File, DD Detailed Display, or PR Print Display.
    1.  Enter ED to edit a provider’s associated team. Additional details are in the ED EDIT HBPC Provider File section.

> <span id="_Toc77590643" class="anchor"></span>Figure 16: ED Action within ALL Provider File Data Example

![](hbpc-user-manual/017.png)

> **NOTE:** Only the HBHC Team prompt can be edited.

2.  Enter DD to see information about the user. Additional details are in the DD Detailed Display section.

> <span id="_Toc77590644" class="anchor"></span>Figure 17: DD Action within ALL Provider File Data Example

![](hbpc-user-manual/018.png)

3.  Enter PR to view print details on the screen or send them to a device. Additional details are in the PR Print Display section.

> <span id="_Toc77590645" class="anchor"></span>Figure 18: PR Action within ALL Provider File Data Example

> ![](hbpc-user-manual/019.png)

> Note: If PR is entered on page 6, the user will need to navigate to page 6 after the PR screen displays. If the user wants a snapshot of information shown on a specific page being viewed, then the PS action is recommended.  

#### AD Add New HBPC Provider

The AD action allows users to add a new HBPC provider. This action can only be invoked after searching for users with NP Display New Person Entries.

If attempting to add a provider who is already a provider, the following message will be displayed, “This provider has already been added with the HBPC Provider number of 63.” Where 63 is an example representation of the provider number already assigned to the provider being added.

When there are 200 provider numbers remaining on the number wheel, a banner message will be displayed. This message will persist and count down as the last remaining provider numbers are assigned.

<span id="_Toc77590646" class="anchor"></span>Figure 19: 200 Remaining Provider Numbers Banner Message

![](hbpc-user-manual/020.png)

To add a new HBPC provider:

1.  Navigate to the Manager Menu option.
2.  Enter the Provider File Data Entry option.
3.  Enter a partial or full name in the Partial or full name prompt.

> **NOTE:** If no search results are found, the following message displays, “No matching entries in the NEW PERSON (#200) file.”

4.  Enter NP at the Select Item(s) prompt.
5.  Enter a partial or full name in the Partial or full name prompt.

> <span id="_Toc77590647" class="anchor"></span>Figure 20: AD Provider File Data Entry Example

> ![](hbpc-user-manual/021.png)

6.  Enter AD to add a user in the displayed list as a provider.
7.  Enter the sequence number for the desired New Person Entry from the list.
8.  Verify the name and enter YES to confirm adding them as a provider.
9.  Enter the team that the provider is a part of.

> <span id="_Toc77590648" class="anchor"></span>Figure 21: AD Provider File Data Entry Example Continued

![](hbpc-user-manual/022.png)

#### ED Edit HBPC Provider File

The ED action allows users to edit the HBPC provider file. This action cannot be invoked after using the NP Display New Person Entries action.

To edit a provider file:

1.  Navigate to the Manager Menu option.
2.  Enter the Provider File Data Entry option.
3.  Enter a partial or full name in the Partial or full name prompt.

> **NOTE:** If no search results are found, the following message displays, “No matching entries in the NEW PERSON (#200) file.”

4.  Enter HP or ALL at the Select Item(s) prompt. In the following steps HP will be the action used with HBH in the name prompt.

> <span id="_Toc77590649" class="anchor"></span>Figure 22: ED Provider File Data Entry Example

> ![](hbpc-user-manual/023.png)

5.  Enter ED in the Select Item(s) prompt.

> <span id="_Toc77590650" class="anchor"></span>Figure 23: ED Provider File Data Entry Example Continued

![](hbpc-user-manual/024.png)

6.  Enter the sequence number corresponding to the left of the provider’s name in the Enter sequence number of provider to edit prompt.
7.  Verify the provider selection.
8.  Enter the team they belong to in the HBHC Team prompt.

#### DD Detailed Display

The DD action allows users to enter the detailed display of an individual.

To view the detailed display:

1.  Navigate to the Manager Menu option.
2.  Enter the Provider File Data Entry option.
3.  Enter a partial or full name in the Partial or full name prompt.

> **NOTE:** If no search results are found, the following message displays, “No matching entries in the NEW PERSON (#200) file.”

4.  If the desired results were found, enter DD at the Select Item(s) prompt.
    1.  If the desired results were not found, use NP, HP, or ALL to find the desired individual first.

> <span id="_Toc77590651" class="anchor"></span>Figure 24: DD Provider File Data Entry Example

> ![](hbpc-user-manual/025.png)

#### PR Print Display

The PR action allows users to enter the print display on any actionable screen showing the Select Item(s) prompt. If using the PR action in an area with multiple pages, then the \<ENTER\> key can be used to tab through the pages.

> **NOTE:** If tabbing through the list of entries before invoking the PR action, the PS action can be used to capture the print display of the current page.

To use print display:

1.  Navigate to the Manager Menu option.
2.  Enter the Provider File Data Entry option.
3.  Enter a partial or full name in the Partial or full name prompt.

> **NOTE:** If no search results are found, the following message displays, “No matching entries in the NEW PERSON (#200) file.”

4.  If the desired results were found, enter PR at the Select Item(s) prompt.
    1.  If the desired results were not found, use NP, HP, or ALL to find the desired results.
    2.  Enter PR on an actionable screen or after invoking another action.
5.  Enter a device or enter HOME, to display on screen, at the DEVICE prompt.

> <span id="_Toc77590652" class="anchor"></span>Figure 25: PR Provider File Data Entry Example

> ![](hbpc-user-manual/026.png)

### Clinic File Data Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHC EDIT CLINIC (631.6)\]

This option allows you to add clinics in the HBHC Clinic file \#631.6. When the program scans through Outpatient Encounters for visits, it looks for visits/appointments to the clinics in this file.

> **NOTE:** Clinics cannot be deleted from the file so care should be taken when adding clinics.

Before using this option:

- The clinics you want to add must be in the Hospital Location file \#44.

Example: Adding a clinic

Select HBHC CLINIC NAME: ASSESSMENT CLINIC

Are you adding 'ASSESSMENT CLINIC' as a new HBHC CLINIC (the 4TH)? No// Y (Yes)

NAME: ASSESSMENT CLINIC// \<RET\>

Manager Menu ...

### Team File Data Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHC EDIT HBHC TEAM (633)\]

This option allows you to enter new and edit existing HBPC teams in the HBHC Team file \#633. There must be at least one team entry for each site. The team name is entered in a free text field of 1-30 characters. A team entry is required for each provider in the HBHC Provider file (see <u>Provider File Data Entry</u>).

Example: Adding a new team

Select HBHC TEAM NAME: BLUE TEAM

Are you adding 'BLUE TEAM' as a new HBHC TEAM (the 3RD)? No// Y (Yes)

NAME: BLUE TEAM// \<RET\>

Example: Changing a team name

Select HBHC TEAM NAME: HINES ISC

NAME: HINES // GREEN TEAM

Manager Menu ...

### HBPC Provider File Report (132) - DISABLED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP8\]

> **NOTE:** The HBPC Provider File Report option was replaced with the <u>PR Print Display</u> action within the HBHC Edit Provider option.

This option prints the contents of the HBHC Provider file. The report is sorted by Provider Name and includes: Provider Name, Provider Number, Degree, Grade/Step, FTEE, Team, and whether the provider number is Inactive. The report prints in 132 column format.

> **NOTE:** Send the report to a device that prints 132 columns.

Example:

\>\>\> HBPC Provider File Report \<\<\< Page: 1

Run Date: FEB 28, 2000

Provider Grade HBPC Inactive

Provider Name Number Degree /Step FTEE HBHC Team Prov \#

=================================================================================================================================

HBPCPROVIDER,THREE 103 BS SR/11 1.0 NUTRITIAN EVAL

---------------------------------------------------------------------------------------------------------------------------------

HBPCPROVIDER,FOUR 104 RN 11/9 1.0 NURSE EVAL/CARE

---------------------------------------------------------------------------------------------------------------------------------

HBPCPROVIDER,FIVE 104 MD 15/3 0.5 MED EVAL

---------------------------------------------------------------------------------------------------------------------------------

HBPCPROVIDER,SIX 106 0.0 MED EVAL Inactive

---------------------------------------------------------------------------------------------------------------------------------

HBPCPROVIDER,SEVEN 107 RN 11/2 1.0 NURSE EVAL/CARE

---------------------------------------------------------------------------------------------------------------------------------

==== End of Report ====

Manager Menu ...

### [^2]Pseudo Social Security Number Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHXRP14\]

A pseudo Social Security Number (SSN) is a computer generated identification. Use this option to find any patient possessing a pseudo SSN. Patient records having pseudo SSNs are considered invalid. A patient that falls into one of the following categories will appear on this report:

- Wrong patient – a patient selected in error, or
- Invalid SSN – a patient not selected in error but whose SSN is invalid due to being a computer generated SSN (e.g., nnn-nn-nnnnP), or
- Collateral – a collateral patient should not be tracked in the HBPC program. If your site wants to track collateral patients, create a collateral clinic(s) in the Hospital Location file \#44 but do not add it to the HBHC clinic file \#631.6.

These records must be corrected in the MAS Patient file \#2 prior to transmission to Austin.

####### Alerting User to Patients with Pseudo SSNs

> [^3]When using the option Evaluation/Admission Data Entry, you will receive a message that the patient has a pseudo SSN and you will be required to select another patient. However, patients added to the HBHC Visit file from the outpatient encounter data may be considered errors when the <u>Build/Verify Transmission File</u> or Auto-queue File Update option is run. A message will be sent to the HBH mail group in this instance.

####### Removing Records for Wrong Patients

1.  Cancel all HBPC appointments for the wrong patient.
2.  Use the <u>Edit Form Errors Data</u> option to clean up the HBHC Pseudo SSN Error(s) file.
3.  Edit the Number of Visit Days to Scan in the Build/Verify Transmission File option to a value large enough to ensure all cancelled appointments will be processed.

####### Removing Records with Invalid SSNs

1.  Contact MAS to correct the SSN.
2.  Use the <u>Edit Form Errors Data</u> option to clean up the HBHC Pseudo SSN Error(s) file.
3.  Edit the Number of Visit Days to Scan in the Build/Verify Transmission File option to a value large enough to ensure all cancelled appointments will be processed.

####### Removing Records for Collateral Patients

4.  Cancel all HBPC appointments for the collateral patient.
5.  Use the <u>Edit Form Errors Data</u> option to clean up the HBHC Pseudo SSN Error(s) file.
6.  Edit the Number of Visit Days to Scan in the Build/Verify Transmission File option to a value large enough to ensure all cancelled appointments will be processed.

Example:

\>\>\> HBPC Pseudo SSN Report \<\<\< Page: 1

Run Date: FEB 28, 2000

Patient Name SSN

================================================================================

HBPCPSEUDOPATIENT,ONE 000-000-0001P

==== End of Report ====

Manager Menu ...

### Re-Transmit File to Austin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRXMT\]

Use this option only if instructed to by Austin.

Depending on the nature of the problem and/or reason for re-transmitting, your local IRM technical support person, and possibly Austin as well, should be involved whenever this option is used. For example, if a transmit was incomplete due to a hardware failure, Austin may need to delete the "partial" transmit file received prior to the re-transmit.

The Re-Transmit File to Austin option should only be used when something unforeseen happened to the last transmission (e.g., garbled file data due to network problems, incomplete transmit due to hardware failure, etc.). The option re-sends thesameHBPC data included in the last filetransmitted to Austin, (i.e., the option <u>Build/Verify Transmission File</u> has NOT been run again since the last transmission to Austin). This option should be used instead of running the Transmit File to Austin option a second time, since the Re-Transmit File option invisibly updates fields used by the software package.

After selecting the option, the following messages appear:

This option re-transmits the same data included in the last file created for transmission to Austin. It should only be run under special circumstances and should be coordinated with Austin. Do you wish to continue? NO//

> Answering "No" or \<RET\> to this message returns the user to the Manager Menu with no transmission occurring.

> If the user answers "Yes" to the "Do you wish to continue?" prompt, the following message indicates a background job has been initiated to re-transmit the file to Austin.

Re-transmission request has been queued.

# # Package Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following chapters describe the use of the HBPC package.

## Conventions Used in Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In examples demonstrating the use of the software, the following conventions will be used:

> \<RET\> press return or enter key

> bolded text example response to a prompt

## Package Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Online help is available for all fields and options in the software. It can be accessed by entering one or two question marks at any field and three question marks at any select option prompt.

## HBPC Information System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each option has an internal name. The internal name begins with HBHC and is shown in brackets following each option below. Whenever (80) or (132) follows a report name, the report requires a device that prints 80 columns or 132 columns respectively.

> HBPC Information System Menu …\[HBHC INFORMATION SYSTEM MENU\]

Evaluation/Admission Data Entry \[HBHCADM\]

Discharge Data Entry \[HBHCDIS\]

Reports Menu ... \[HBHC REPORTS MENU\]

> Evaluation/Admission Data Report by Patient (80) \[HBHCRP2\]

> Patient Visit Data Report (80) \[HBHCRP3\]

> Discharge Data Report by Patient (80) \[HBHCRP5\]

> Episode of Care/Length of Stay Report (80) \[HBHCRP12\]

> Admissions/Discharges by Date Range Report (132) \[HBHCRP7\]

> Rejections from HBPC Program Report (132) \[HBHCRP16\]

> Visit Data by Date Range Report (80) \[HBHCRP4\]

> CPT Code Summary Report (80) \[HBHCRP17\]

> Provider CPT Code Summary Report (80) \[HBHCRP22\]

> <span id="icd1" class="anchor"></span> ICD Code/Dx Text by Date Range Report (80) \[HBHCR19A\]

> Unique Patients by Date Range Summary Report (80) \[HBHCRP20\]

> Total Visits by Date Range Report (80) \[HBHCRP21\]

> Patient Days of Care by Date Range Report (80) \[HBHCRP23\][^4]

> Census Reports Menu ... \[HBHC CENSUS REPORTS MENU\]

> Program Census Report (80) \[HBHCRP10\]

> Address Included Program Census (132) \[HBHCRP25\] [^5]

> Expanded Program Census Report (80) \[HBHCRP24\] [^6]

> <span id="icd2" class="anchor"></span>Active Census with ICD Code/Text Report (132) \[HBHCRP18\]

> Team Census Report (80) \[HBHCRP11\]

> Case Manager Census Report (132) \[HBHCRP6\]

> Provider Census Report (132) \[HBHCRP9\]

Transmission Menu ... \[HBHC TRANSMISSION MENU\]

> Build/Verify Transmission File \[HBHCFILE\]

> Form Errors Report (80) \[HBHCRP1\]

> Edit Form Errors Data \[HBHCUPD\]

> Transmit File to Austin \[HBHCXMT\] \*\* Locked with HBHC TRANSMIT \*\*

> Print Transmit History Report (80) \[HBHCR15A\]

> Manager Menu ... \[HBHC MANAGER MENU\] \*\* Locked with HBHC MANAGER \*\* (This menu is discussed under the section <u>Using the Manager Menu in Implementation and Maintenance</u>.)

> System Parameters Edit \[HBHC EDIT SYSTEM PARAMETERS\]

> Provider File Data Entry \[HBHC EDIT PROVIDER (631.4)\]

> Clinic File Data Entry \[HBHC EDIT CLINIC (631.6)\]

> Team File Data Entry \[HBHC EDIT HBHC TEAM (633)\]

> HBPC Provider File Report (132) \[HBHCRP8\] DISABLED (performed within the HBHC Edit Provider option)

> Pseudo Social Security Number Report (80) \[HBHXRP14\]

> Re-Transmit File to Austin \[HBHCRXMT\]

# # Adding and Editing Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Adding Evaluation/Admission, Discharge and Visit Data through HBPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three options for adding patient data into the HBPC package. These are discussed in depth later in this section.

Appointment Management Allows you to enter patient visit/appointment information. This data is stored in the Outpatient Encounter file \#409.68 held by the Patient Care Encounter package. When it is complete, the data is added to the HBHC Visit file \#632 through the Auto Queue HBHC File Update or the Build/Verify Transmission File option.

Evaluation/Admission Data Entry Allows you to document the patient’s evaluation and admission information which adds the data to the HBHC Patient file \#631. Once entered, and without errors, records are ready for transmission to Austin.

> **NOTE:** If the patient is not in a Medical Foster Home (MFH), the PARENT SITE prompt will display after the Patient Name prompt (if the patient has been previously admitted) or after the Patient Date prompt (if this is a new HBPC patient). This prompt requires a response. Managers can build a list of choices that will display in the PARENT SITE prompt from the parent site(s) defined in the System Parameters Edit option. Each site is required to define at least one parent site in the Systems Parameter Edit option.

> If the patient is in an MFH, the PARENT SITE prompt does not display. Parent site information is derived from the parent site defined for the MFH in the Demographic Data Entry option for MFH.

Discharge Data Entry Allows you to describe the patient at discharge to complete the record in the HBHC Patient file \#631. Once entered, and without errors, records are ready for transmission to Austin.

## Adding Visit Data through other Encounter Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Visit data entered through any of the following packages is also stored in the Outpatient Encounter file just as that entered using the option Appointment Management. Please see their respective manuals for use of the software.

|                                                 |                                                                                            |
|-------------------------------------------------|--------------------------------------------------------------------------------------------|
| Text Integration Utility (TIU)                  | Allows you to enter encounter data via progress notes.                                     |
| Event Capture System (ECS)                  | Allows you to enter encounter procedures which are not handled in any other VISTA package. |
| Automated Information Capture System (AICS) | Scans encounter data into the system.                                                      |

## [^7]Appointment Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[SDAM APPT MGT\]

This option utilizes the MAS Scheduling option, Appointment Management \[SDAM APPT MGT\] functionality, for entry of appointment data. Appointments entered and checked out via this option are added to the HBHC VISIT file \#632, and then are ready for transmission to Austin.

> **NOTE:** If appointments are entered after the visit has taken place, you will also be prompted for checkout information.

> **NOTE:** The Appointment Management option, \[HBHC APPOINTMENT\], is being retired and no longer hangs off the HBPC Information System menu. This is due to the impending implementation of the new Resource Scheduling Application (RSA) that is to replace the legacy scheduling options. IRM should add the original Appointment Management Option, \[SDAM APPT MGT\], as a secondary menu option for HBPC users to use once patch HBH\*1\*24 is installed. After the RSA is nationally released, the Appointment Management option and other legacy Scheduling options will be replaced by usage of the new RSA application.

### Example: Making an Appointment for a Patient 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following example may differ from what you see when making an appointment depending on clinic parameter settings.

1.  Entries can be made by selecting a patient or a clinic.
- To make several entries for a clinic, enter the clinic name following "C." (e.g., C.ASSESSMENT CLINIC to enter appointments for the Assessment Clinic)
- To make appointments for a specific patient, enter the patient's name following "P." (e.g., P.HBPCPATIENT,ONE)
2.  At the Select Action prompt, choose MA to make an appointment.
3.  Enter the name of the clinic.
4.  Select an Appointment Type.
5.  You may display the pending appointments or press the \<RET\> key.
6.  Enter a date to display clinic availability.
7.  Select a date and time for the appointment.
8.  You may choose to bypass or accept prompts for test stops, other info, or x-rays.
9.  You may then enter another clinic or the same clinic for another appointment for the same patient.

Select Patient name or Clinic name: P.HBPCPATIENT,ONEHBPCPATIENT,ONE 5-20-66

000000001 YES

Enrollment Priority: GROUP 1 Category: IN PROCESS End Date:

...OK? Yes// \<RET\> (Yes)

Appt Mgt Module Mar 16, 2000 13:02 Page: 1 of 1

Patient: HBPCPATIENT,ONE (0001) Outpatient

Total Appointment Profile \* - New GAF Required 02/15/00 thru 12/10/02

Clinic Appt Date/Time Status

1 Med Clinic Harvey Mar 09, 2000 10:45 Inpatient/Checked Out 11:30

2 Assessment Mar 17, 2000 09:00 Future

3 Phys Ther Bill Mar 24, 2000 09:00 Future

4 Phys Ther Bill Mar 31, 2000 09:00 Future

Enter ?? for more actions

CI Check In CL Change Clinic PR Provider Update

UN Unscheduled Visit CD Change Date Range DX Diagnosis Update

MA Make Appointment EP Expand Entry DE Delete Check Out

CA Cancel Appointment AE Add/Edit CP Procedure Update

NS No Show RT Record Tracking PC PC Assign or Unassign

DC Discharge Clinic PD Patient Demographics TI Display Team Information

AL Appointment Lists CO Check Out

PT Change Patient EC Edit Classification

Select Action: Quit// MA Make Appointment

Patient: HBPCPATIENT,ONE (0001) Outpatient

Select CLINIC: HBPCCLINIC1

APPOINTMENT TYPE: REGULAR// \<RET\>

DISPLAY PENDING APPOINTMENTS: NO//\<RET\>

CURRENT ENROLLMENT: OPT

DISPLAY CLINIC AVAILABILITY STARTING WHEN: 3/31 (MAR 31, 2000)

> **NOTE:** Where a 1 appears below, there is an available clinic time. Where a 0 appears, the clinic time is taken.

Diet Nancy

Mar 2000

TIME \|8 \|9 \|10 \|11 \|12 \|1 \|2 \|3 \|4

DATE \| \| \| \| \| \| \| \| \|

FR 31 \[1 1 1 1\|0 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

Apr 2000

MO 02 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

FR 07 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

MO 09 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

FR 14 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

MO 16 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

FR 21 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

MO 23 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

FR 28 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

MO 30 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

May 2000

FR 05 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

MO 07 \[1 1 1 1\|1 1 1 1\|1 1 1 1\|1 1 1 1\] \[1 1 1 1\|1 1 1 1\]

15 MINUTE APPOINTMENTS

DATE/TIME: 4/7@9A (APR 07, 2000@09:00)

15-MINUTE APPOINTMENT MADE

WANT PATIENT NOTIFIED OF LAB,X-RAY, OR EKG STOPS? No// \<RET\> (No)

OTHER INFO: \<RET\>

WANT PREVIOUS X-RAY RESULTS SENT TO CLINIC? No// \<RET\> (No)

Select CLINIC: \<RET\>Appt Mgt Module Mar 16, 2000 13:02 Page: 1 of 1

Patient: HBPCPATIENT,ONE (0001) Outpatient

Total Appointment Profile \* - New GAF Required 02/15/00 thru 12/10/02

Clinic Appt Date/Time Status

1 Med Clinic Harvey Mar 09, 2000 10:45 Inpatient/Checked Out 11:30

2 Assessment Mar 17, 2000 09:00 Future

3 Phys Ther Bill Mar 24, 2000 09:00 Future

4 Phys Ther Bill Mar 31, 2000 09:00 Future

#### HBPCCLINIC1 Apr 07, 2000 09:00 Future 

Enter ?? for more actions

CI Check In CL Change Clinic PR Provider Update

UN Unscheduled Visit CD Change Date Range DX Diagnosis Update

MA Make Appointment EP Expand Entry DE Delete Check Out

CA Cancel Appointment AE Add/Edit CP Procedure Update

NS No Show RT Record Tracking PC PC Assign or Unassign

DC Discharge Clinic PD Patient Demographics TI Display Team Information

AL Appointment Lists CO Check Out

PT Change Patient EC Edit Classification

Select Action: Quit// \<RET\> QUIT

### Example: Using Check Out in Appointment Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HBHC Visit file holds the Patient Name, Visit Date, Clinic, Provider, Diagnoses, and CPT Code procedures and modifiers for the visit. Checking Out the patient visit in Appointment Management allows you to add this information to the file.

1.  Entries can be searched for by patient or by clinic. Enter P. plus the patient's name or C. plus the clinic name.
2.  At the "Select Beginning Date" and “Select Ending Date” accept the default dates or enter different dates.
3.  For Action, select Check Out (CO).
4.  If you want, you can make a follow-up appointment.
5.  Enter a Check Out date and time.
6.  If there is a known service connected condition or an exposure and the visit was related, give the appropriate answer(s).
7.  Enter the provider for the appointment.
8.  Enter diagnoses for the appointment.
9.  Enter procedures and procedure modifiers for the appointment.

Select Patient name or Clinic name: C.ASSESSMENT CLINIC

Select Beginning Date: FEB 19, 2000// \<RET\> (FEB 19, 2000)

Select Ending Date: TODAY// \<RET\> (MAR 20, 2000)

Appt Mgt Module Mar 20, 2000 15:23:23 Page: 1 of 1

Clinic: ASSESSMENT CLINIC

No Action Taken/Action Required \* - New GAF Required 02/19/00 thru 03/20/00

Patient Appt Date/Time Status

1 0002 HBPCPATIENT,TWO Mar 17, 2000 09:00 No Action Taken

2 0001 HBPCPATIENT,ONE Mar 17, 2000 09:30 No Action Taken

3 0003 HBPCPATIENT,THREE Mar 17, 2000 10:00 No Action Taken

Enter ?? for more actions

CI Check In CL Change Clinic PR Provider Update

UN Unscheduled Visit CD Change Date Range DX Diagnosis Update

MA Make Appointment EP Expand Entry DE Delete Check Out

CA Cancel Appointment AE Add/Edit CP Procedure Update

NS No Show RT Record Tracking PC PC Assign or Unassign

DC Discharge Clinic PD Patient Demographics TI Display Team Information

AL Appointment Lists CO Check Out

PT Change Patient EC Edit Classification

Select Action: Quit// CO Check Out

Select Appointment(s): (1-6): 1

1 0002 HBPCPATIENT,TWO Mar 17, 2000 09:00 No Action Taken

Do you wish to make a follow-up appointment? YES// NO

Check out date and time: NOW// 3/17@9:30A (MAR 17, 2000@09:30)

--- Classification --- \[Required\]

Was treatment for SC Condition? NO

Was treatment related to Agent Orange Exposure? NOPAT/APPT/CLINIC: HBPCPATIENT,TWO MAR 17, 2000@09:00 ASSESSMENT CLINIC

PROVIDER: ...There are 0 PROVIDER(S) associated with this encounter.

- - E N C O U N T E R P R O V I D E R S - -

No. PROVIDER PERSON CLASS ON MAR 17, 2000@09:00

No PROVIDERS for this Encounter.

Enter PROVIDER: HBPCPROVIDER,TWO

Is this the PRIMARY provider for this ENCOUNTER? YES// \<RET\>PAT/APPT/CLINIC: HBPCPATIENT,TWO MAR 17, 2000@09:00 ASSESSMENT CLINIC

PROVIDER: ...There are 0 PROVIDER(S) associated with this encounter.

- - E N C O U N T E R P R O V I D E R S - -

No. PROVIDER PERSON CLASS ON MAR 17, 2000@09:00

1 HBPCPROVIDER,TWO\* PRIMARY Language/Audiologist

Enter PROVIDER: \<RET\>PAT/APPT/CLINIC: HBPCPATIENT,TWO MAR 17, 2000@09:00 ASSESSMENT CLINIC

ICD CODE: ...There are 0 ICD CODES associated with this encounter.

- - E N C O U N T E R D I A G N O S I S (ICD10 CODES) - -

No. ICD DESCRIPTION PROBLEM LIST

No DIAGNOSIS for this Encounter.

<span id="icd6_1" class="anchor"></span>

Enter Diagnosis : 230.1

ONE primary diagnosis must be established for each encounter!

Is this the PRIMARY DIAGNOSIS for this ENCOUNTER? YES// \<RET\>PAT/APPT/CLINIC: HBPCPATIENT,TWO MAR 17, 2000@09:00 ASSESSMENT CLINIC

ICD CODE: ...There is 1 ICD CODE associated with this encounter.

Previous Entry: 230.1

- - E N C O U N T E R D I A G N O S I S (ICD10 CODES) - -

No. ICD DESCRIPTION PROBLEM LIST

1 230.1\* CA IN SITU ESOPHAGUS PRIMARY

Enter NEXT Diagnosis : \<RET\>

Enter PROVIDER associated with PROBLEM: WILLIAMS,CATHY // \<RET\>PAT/APPT/CLINIC: HBPCPATIENT,TWO MAR 17, 2000@09:00 ASSESSMENT CLINIC

PROVIDER: ...Enter the provider associated with the CPT'S.....

CPT: ...There are 0 PROCEDURES associated with this encounter.

- - E N C O U N T E R P R O C E D U R E S (CPT CODES) - -

No. CPT CODE QUANTITY DESCRIPTION PROVIDER

Enter '+' for next page, '-' for last page.

Enter PROCEDURE (CPT CODE): nnnnn

Select CPT MODIFIER: \<RET\>PAT/APPT/CLINIC: HBPCPATIENT,TWO MAR 17, 2000@09:00 ASSESSMENT CLINIC

PROVIDER: ...Enter the provider associated with the CPT'S.....

CPT:

- - E N C O U N T E R P R O C E D U R E S (CPT CODES) - -

No. CPT CODE QUANTITY DESCRIPTION PROVIDER

1 nnnnn\* DIAGNOSTIC ...

How many times was this procedure performed: 1// \<RET\>

Enter PROVIDER associated with PROCEDURE: HBPCPROVIDER,TWO// \<RET\>PAT/APPT/CLINIC: HBPCPATIENT,TWO MAR 17, 2000@09:00 ASSESSMENT CLINIC

PROVIDER: ...Enter the provider associated with the CPT'S.....

CPT: ...There is 1 PROCEDURE associated with this encounter.

- - E N C O U N T E R P R O C E D U R E S (CPT CODES) - -

No. CPT CODE QUANTITY DESCRIPTION PROVIDER

1 nnnnn\* 1 DIAGNOSTIC ... HBPCPROVIDER,TWO

Enter '+' for next page, '-' for last page.

Enter NEXT PROCEDURE (CPT CODE): \<RET\>

\- - - - S o r r y A b o u t T h e W a i t - - - -

This information is being stored or monitored by Scheduling

Integrated Billing, Order Entry, Registration, Prosthetics

PCE/Visit Tracking and Automated Med Information Exchange.

Do you wish to see the check out screen? NO// \<RET\>

Appt Mgt Module Mar 20, 2000 15:59:45 Page: 1 of 1

Clinic: ASSESSMENT

No Action Taken/Action Required \* - New GAF Required 02/19/00 thru 03/20/00

Patient Appt Date/Time Status

No appointments meet criteria.

Enter ?? for more actions

CI Check In CL Change Clinic PR Provider Update

UN Unscheduled Visit CD Change Date Range DX Diagnosis Update

MA Make Appointment EP Expand Entry DE Delete Check Out

CA Cancel Appointment AE Add/Edit CP Procedure Update

NS No Show RT Record Tracking PC PC Assign or Unassign

DC Discharge Clinic PD Patient Demographics TI Display Team Information

AL Appointment Lists CO Check Out

PT Change Patient EC Edit Classification

Select Action: Quit// \<RET\>

## Evaluation/Admission Data Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCADM\]

Use this option to enter or edit evaluation and admission data (Form 3) for a patient. This data is stored in the HBHC Patient file \#631. A patient must already exist in the MAS Patient file \#2 before being entered into the HBPC package.

> **NOTE:** - If the patient IS NOT in a Medical Foster Home (MFH), the PARENT SITE prompt will display after the Patient Name prompt (if the patient has been previously admitted) or after the Patient Date prompt (if this is a new HBPC patient). This prompt requires a response. Each site is required to define at least one parent site in the Systems Parameter Edit option.

- If the patient IS in an MFH, parent site information is derived from the parent site defined for the MFH in the Demographic Data Entry option for MFH.

### Complete Episode of Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A "complete" episode of care consists of both an admission and a discharge, with each episode comprising a separate HBHC Patient file record. A "reject" also represents an episode of care. Therefore, a patient can have more than one episode of care record. The package will NOT allow the creation of an additional episode of care until the patient has been discharged from the previous episode.

A complete episode of care record should ONLY be edited if data correction is needed. Selection of an existing record is inappropriate if your intention is to create an additional episode of care. A message is displayed to remind you that the record may have been selected in error.

\*\*\* Record contains Discharge data indicating a Complete Episode of Care \*\*\*

### Creating an Additional Episode of Care for a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create another episode of care for the same patient, enclose the patient's name in double quotes at the "Select HBHC PATIENT NAME" prompt (e.g., "HBPCPATIENT,FOUR" or "S0004"). This informs the package that you want to create a new record in the HBHC Patient file for the same patient.

### Patient Demographic Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient demographic information [^8](Birth Year and Sex,) is pulled from the MAS Patient file \#2. If this data is incorrect, contact MAS to correct the data. It cannot be edited by HBPC personnel.

State Code, County Code, ZIP Code, Eligibility @ Evaluation, Period of Service, and Marital Status @ Evaluation come from the MAS Patient file and are displayed as default values. Press the \<RET\> or \<ENTER\> key if the default is valid, or type in the correct field information. Illinois is the default value in the following example:

STATE CODE: ILLINOIS// \<RET\> Accept the default or

STATE CODE: ILLINOIS// WISCONSIN type in the correct information.

### Exiting and Field Jumping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may ^ exit from the data entry process and return to the menu at any field prompt. Field jumping is not allowed due to branching logic contained within the data entry process.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="hbhc-patient-name" class="unnumbered">HBHC Patient Name</h4></td>
<td><p><strong>New Entry</strong>: Enter the name of a new patient to the HBHC Patient file:</p>
<p>Last name,First name (e.g., HBPCPATIENT,FOUR)</p>
<p>First initial of last name plus last 4 digits of the SSN (e.g., S0004)</p>
<p><strong>Creating Additional Episode of Care</strong>: Enter the name of a patient who has a previous complete episode of care or a reject record in HBPC:</p>
<p>Enter name in quotes ("HBPCPATIENT,FOUR" or "S0004")</p></td>
</tr>
<tr class="even">
<td colspan="2"><p>Answer Yes to the "Are you adding..." prompt.</p>
<p>If you choose a record that already contains discharge data, then the following message will appear:</p>
<p>* Record contains Discharge data indicating a Complete Episode of Care *</p>
<p>This message is a reminder that the record is considered to be complete and may have been selected in error. This record should only be edited if correction of existing data is needed. Selection of this record is inappropriate if your intention is to create an additional episode of care. If you want to start a new record, then “^” out at the next prompt and reenter the patient’s name in quotation marks “NAME,PATIENT”. If you want to edit a complete record, then continue.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><h4 id="hbhc-patient-date" class="unnumbered"><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>HBHC Patient Date</h4></td>
<td>Enter the date the patient was evaluated for or admitted to the HBPC Program.</td>
</tr>
<tr class="odd">
<td colspan="2"><p>The date is repeated as a default. Press the &lt;RET&gt; key to accept the date.</p>
<p>HBHC PATIENT DATE: <strong>2/29/2000</strong></p>
<p>DATE: FEB 29,2000// <strong>&lt;RET&gt;</strong></p>
<p><strong>Parent Site:</strong> Enter the parent site associated to this patient. If only one site is defined in the <strong>Systems Parameter Edit</strong> option, that site will appear as a default (this prompt will not appear if this patient is in a Medical Foster Home.).</p></td>
</tr>
<tr class="even">
<td><h4 id="state-code" class="unnumbered">State Code</h4></td>
<td>This is the state in which the patient resides. Either press the &lt;RET&gt; key to accept the default, or change the code.</td>
</tr>
<tr class="odd">
<td><h4 id="county-code" class="unnumbered">County Code</h4></td>
<td>This is the county in which the patient resides. Either press the &lt;RET&gt; key to accept the default, or change the code.</td>
</tr>
<tr class="even">
<td><h4 id="zip-code" class="unnumbered">ZIP Code</h4></td>
<td>This is the ZIP Code for the patient's address. Either press the &lt;RET&gt; key to accept the default, or change the code.</td>
</tr>
<tr class="odd">
<td><h4 id="eligibility-evaluation" class="unnumbered">Eligibility @ Evaluation</h4></td>
<td>This is the patient's eligibility.</td>
</tr>
<tr class="even">
<td><h4 id="birth-year" class="unnumbered">Birth Year</h4></td>
<td>This is the year the patient was born. If it is incorrect, contact MAS.</td>
</tr>
<tr class="odd">
<td><h4 id="period-of-service" class="unnumbered">Period of Service</h4></td>
<td>This is the period of time the patient served in the military.</td>
</tr>
<tr class="even">
<td><h4 id="sex" class="unnumbered">Sex</h4></td>
<td>This is the patient's sex. If it is incorrect, contact MAS.</td>
</tr>
<tr class="odd">
<td><h4 id="race" class="unnumbered"><a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a>Race</h4></td>
<td>This is the patient's race. If it is incorrect, contact MAS.</td>
</tr>
<tr class="even">
<td><h4 id="race-1" class="unnumbered">Race</h4></td>
<td>This is the patient's race. If it is incorrect, contact MAS.</td>
</tr>
<tr class="odd">
<td><h4 id="marital-status-evaluation" class="unnumbered">Marital Status @ Evaluation</h4></td>
<td>This is the patient's marital status. Either press the &lt;RET&gt; key to accept the default, or change the status.</td>
</tr>
<tr class="even">
<td><h4 id="living-arrangements-eval" class="unnumbered">Living Arrangements @ Eval</h4></td>
<td><p>Enter one of the following numeric codes (1-5, 9) that best defines the patient's living arrangements:</p>
<p>1 Alone</p>
<p>2 With Spouse</p>
<p>3 With Relatives</p>
<p>4 With Non-Relatives</p>
<p>5 Group Quarters, Not Health Related</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="last-agency-providing-care" class="unnumbered">Last Agency Providing Care</h4></td>
<td><p>Enter one of the following codes (1-3) that best describes the last agency providing care for the patient:</p>
<p>1 VA Provided Care</p>
<p>2 Non VA Care</p>
<p>3 VA Fee Basis/Contract</p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch HBH*1*8 January 1998 Field required.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>Patch HBH*1*19 January 2003 Race: Obsolete Field January 2003<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="type-of-last-care-agency" class="unnumbered">Type of Last Care Agency</h4></td>
<td><p>Enter one of the following codes (1-7, 9) that best describes the type of care provided by the last agency:</p>
<p>1 General Hospital</p>
<p>2 Specialty Hospital</p>
<p>3 Nursing Home</p>
<p>4 Residential Care Facility</p>
<p>5 Hospice</p>
<p>6 Community-Based Services</p>
<p>7 Self/Family, No Regular Source</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="admitreject-action" class="unnumbered">Admit/Reject Action</h4></td>
<td><p>Enter the code for either admitted to or rejected from the HBPC program.</p>
<p>1 Admit to HBHC</p>
<p>2 Reject from HBHC</p>
<p>If 1, skip to Primary Diagnosis @ Admission.</p></td>
</tr>
<tr class="odd">
<td><h4 id="rejectwithdraw-reason" class="unnumbered">Reject/Withdraw Reason</h4></td>
<td><p>Enter the 2 digit code that represents the reason the patient was rejected/withdrawn from the HBPC program.</p>
<p>10 Referral Withdrawn Due to Death</p>
<p>11 Other</p>
<p>01 Not Located in Service Area</p>
<p>02 Program Slot Not Available</p>
<p>03 Patient or Caregiver Refused HBHC</p>
<p>04 Suitable Caregiver Not Available</p>
<p>05 Home Environment Unsuitable</p>
<p>06 Referral Withdrawn (excludes death)</p>
<p>07 Patient's Condition Necessitates Institutional Care</p>
<p>08 Patient Can Be Effectively Treated as Outpatient</p></td>
</tr>
<tr class="even">
<td><h4 id="rejectwithdraw-disposition" class="unnumbered">Reject/Withdraw Disposition </h4></td>
<td><p>Enter the code that represents the patient's disposition.</p>
<p>1 Referred Back to Referral Source</p>
<p>2 Disposition Made by HBHC</p>
<p>Skip to Person Completing Evl/Adm Form.</p></td>
</tr>
<tr class="odd">
<td><h4 id="primary-diagnosis-admission" class="unnumbered">Primary Diagnosis @ Admission</h4></td>
<td><span id="icd3" class="anchor"></span>Enter the ICD9 or ICD10 diagnosis code for the patient's primary diagnosis.</td>
</tr>
<tr class="even">
<td><h4 id="secondary-diagnosis-adm" class="unnumbered">Secondary Diagnosis @ Adm</h4></td>
<td>Enter a secondary diagnosis. This is a free text field (1-30 characters). This information is not transmitted to Austin.</td>
</tr>
<tr class="odd">
<td><h4 id="vision-admission" class="unnumbered">Vision @ Admission</h4></td>
<td><p>Enter the code that best represents the patient's vision.</p>
<p>1 Normal or Minimal Loss</p>
<p>2 Moderate Loss</p>
<p>3 Severe Loss</p>
<p>4 Total Blindness</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="hearing-admission" class="unnumbered">Hearing @ Admission</h4></td>
<td><p>Enter the code that best represents the patient's hearing.</p>
<p>1 Normal or Minimal Loss</p>
<p>2 Moderate Loss</p>
<p>3 Severe Loss</p>
<p>4 Total Deafness</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="expressive-communication-adm" class="unnumbered">Expressive Communication @ Adm</h4></td>
<td><p>Enter the code that best describes the patient's ability to communicate with others.</p>
<p>1 Speaks and is Usually Understood</p>
<p>2 Speaks But is Understood Only with Difficulty</p>
<p>3 Uses Only Sign Language, Symbol Board or Writing</p>
<p>4 Uses Only Gestures, Grunts, or Primitive Symbols</p>
<p>5 Does Not Convey Needs</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="receptive-communication-adm" class="unnumbered">Receptive Communication @ Adm</h4></td>
<td><p>Enter the code that best describes the patient's ability to understand others.</p>
<blockquote>
<p>1 Usually Understands Oral Communication</p>
<p>2 Has Limited Comprehension of Oral Communication</p>
<p>3 Understands by Depending on Lip Reading, Written Material, or Sign Language</p>
<p>4 Understands Primitive Gestures, Facial Expres., Pictograms, and/or Env. Cues</p>
<p>5 Does Not Understand</p>
<p>9 Not Determined</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><h4 id="bathing-admission" class="unnumbered">Bathing @ Admission</h4></td>
<td><p>Enter the code that describes how much help the patient requires bathing.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="dressing-admission" class="unnumbered">Dressing @ Admission</h4></td>
<td><p>Enter the code that describes how much help the patient requires dressing.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="toilet-usage-admission" class="unnumbered">Toilet Usage @ Admission</h4></td>
<td><p>Enter the code that describes how much help the patient requires using the toilet.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="transferring-admission" class="unnumbered">Transferring @ Admission</h4></td>
<td><p>Enter the code that describes how much help the patient requires transferring.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="eating-admission" class="unnumbered">Eating @ Admission</h4></td>
<td><p>Enter the code that describes how much help the patient requires eating.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="walking-admission" class="unnumbered">Walking @ Admission</h4></td>
<td><p>Enter the code that describes how much help the patient requires walking.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="bowel-continence-admission" class="unnumbered">Bowel Continence @ Admission</h4></td>
<td><p>Enter the code that describes the patient's bowel continence.</p>
<p>1 Continent or Ostomy/Catheter Self Care</p>
<p>2 Incontinent Occasionally</p>
<p>3 Incontinent or Ostomy/Catheter Not self Care</p>
<p>9 Not Determined</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="bladder-continence-admission" class="unnumbered">Bladder Continence @ Admission</h4></td>
<td><p>Enter the code that describes the patient's bladder continence.</p>
<p>1 Continent or Ostomy/Catheter Self Care</p>
<p>2 Incontinent Occasionally</p>
<p>3 Incontinent or Ostomy/Catheter Not Self Care</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="mobility-admission" class="unnumbered">Mobility @ Admission</h4></td>
<td><p>Enter the code that describes the patient's mobility.</p>
<p>1 Goes Outdoors Without Help</p>
<p>2 Goes Outdoors With Help</p>
<p>3 Confined Indoors, Not Bed Disabled</p>
<p>4 Bed Disabled</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="adaptive-tasks-admission" class="unnumbered">Adaptive Tasks @ Admission</h4></td>
<td><p>Enter the code that describes the patient's ability to perform adaptive tasks.</p>
<p>1 No Help</p>
<p>2 Requires Help</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="behavior-problems-admission" class="unnumbered">Behavior Problems @ Admission</h4></td>
<td><p>Enter the code that describes whether or not the patient has behavior problems.</p>
<p>1 Does Not Exhibit This Characteristic</p>
<p>2 Exhibits This Characteristic</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="disorientation-admission" class="unnumbered">Disorientation @ Admission</h4></td>
<td><p>Enter the code that describes whether or not the patient is disoriented.</p>
<p>1 Does Not Exhibit This Characteristic</p>
<p>2 Exhibits This Characteristic</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="mood-disturbance-admissison" class="unnumbered">Mood Disturbance @ Admissison</h4></td>
<td><p>Enter the code that describes whether or not the patient has a mood disturbance.</p>
<p>1 Does Not Exhibit This Characteristic</p>
<p>2 Exhibits This Characteristic</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="caregiver-limitations-adm" class="unnumbered">Caregiver Limitations @ Adm</h4></td>
<td><p>Enter the level of limitations for the caregiver.</p>
<p>1 Minimal or None</p>
<p>2 Moderate</p>
<p>3 Moderately Severe</p>
<p>4 No Caregiver</p>
<p>9 Not Determined</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="section-4" class="unnumbered"></h4></td>
<td></td>
</tr>
<tr class="even">
<td><h4 id="person-completing-evladm-form" class="unnumbered">Person Completing Evl/Adm Form</h4></td>
<td>Enter the person's name that completed the form. Entering ?? brings up a list of choices. If you do not see the person who completed the form, that person must be entered into HBHC Provider file # 631.4. Use the option <u>Provider File Data Entry</u> to add the person to the file. This information is not transmitted to Austin.</td>
</tr>
<tr class="odd">
<td><h4 id="date-evaladm-form-completed" class="unnumbered">Date Eval/Adm Form Completed</h4></td>
<td>Enter the date the form was completed. This information is not transmitted to Austin.</td>
</tr>
<tr class="even">
<td><h4 id="case-manager" class="unnumbered">Case Manager</h4></td>
<td>Enter the person that is responsible for the case. Entering ?? brings up a list of choices. If you do not see the case manager's name, that person must be entered into HBHC Provider file # 631.4. Use the option <u>Provider File Data Entry</u> to add the person to the file. This information is not transmitted to Austin.</td>
</tr>
</tbody>
</table>

Messages

> Transmit Status Flag must be reset before editing this record is allowed. Do you wish to reset the Flag? NO//

This message is displayed if the record has previously been transmitted to Austin. Resetting the flag allows you to edit any data in the record. Answering “Yes” to the “Do you wish to reset the Flag?” prompt automatically generates a Form 6 Correction record behind the scenes. The Transmit Status Flag will be reset to “Needs to be Transmitted” status, and the record will be included in the next transmission to Austin. In short, answering “Yes” tells Austin to delete the previously transmitted record because this is a corrected replacement.

> \*\*\* Record contains Discharge data indicating a Complete Episode of Care \*\*\*

This message is a reminder that the record is considered to be complete and may have been selected in error. This record should only be edited if correction of existing data is needed. Selection of this record is inappropriate if your intention is to create an additional episode of care.

Example of an admission

> Select HBHC PATIENT NAME: HBPCPATIENT,FIVE 1-1-40 000000005 YES SC VETERAN

> Enrollment Priority: GROUP 2 Category: IN PROCESS End Date:

> Are you adding 'HBPCPATIENT,FIVE' as a new HBHC PATIENT (the 9TH)? No// Y

> (Yes)

> HBHC PATIENT DATE: T (FEB 29, 2000)

> DATE: FEB 29,2000// \<RET\>

> STATE CODE: ANYSTATE // \<RET\>

> COUNTY CODE: ANYCOUNTY (031)// \<RET\>

> ZIP CODE: 66611// \<RET\>

> ELIGIBILITY @ EVALUATION: Service Connected Less Than 50% (03)// \<RET\>

> BIRTH YEAR: 1940

> \*\*\* Contact MAS if value is incorrect. \*\*\*

> PERIOD OF SERVICE: Vietnam (07)// \<RET\>

> SEX: Male (1)

> \*\*\* Contact MAS if value is incorrect. \*\*\*

> RACE: White (1)

> \*\*\* Contact MAS if value is incorrect. \*\*\*

> MARITAL STATUS @ EVALUATION: Married (1)// \<RET\>

> LIVING ARRANGEMENTS @ EVAL: 1 Alone (1)

> LAST AGENCY PROVIDING CARE: 1 VA Provided Care (1)

> TYPE OF LAST CARE AGENCY: 5 Hospice (5)

> ADMIT/REJECT ACTION: 1 Admit to HBHC (1)

> PRIMARY DIAGNOSIS @ ADMISSION: 157.1 MAL NEO PANCREAS BODY COMPLICATION/COMORBIDITY

> SECONDARY DIAGNOSES @ ADM: \<RET\>

> VISION @ ADMISSION: 2 Moderate Loss (2)

> HEARING @ ADMISSION: 2 Moderate Loss (2)

> EXPRESSIVE COMMUNICATION @ ADM: 1 Speaks and is Usually Understood (1)

> RECEPTIVE COMMUNICATION @ ADM: 1 Usually Understands Oral Communication (1)

> BATHING @ ADMISSION: 2 Receives Help (2)

> DRESSING @ ADMISSION: 2 Receives Help (2)

> TOILET USAGE @ ADMISSION: 2 Receives Help (2)

> TRANSFERRING @ ADMISSION: 2 Receives Help (2)

> EATING @ ADMISSION: 2 Receives Help (2)

> WALKING @ ADMISSION: 3 Not Done or Done Without Patient Participation (3)

> BOWEL CONTINENCE @ ADMISSION: 2 Incontinent Occasionally (2)

> BLADDER CONTINENCE @ ADMISSION: 3 Incontinent or Ostomy/Catheter Not Self Care

> \(3\)

> MOBILITY @ ADMISSION: 3 Confined Indoors, Not Bed Disabled (3)

> ADAPTIVE TASKS @ ADMISSION: 2 Requires Help (2)

> BEHAVIOR PROBLEMS @ ADMISSION: 1 Does Not Exhibit This Characteristic (1)

> DISORIENTATION @ ADMISSION: 1 Does Not Exhibit This Characteristic (1)

> MOOD DISTURBANCE @ ADMISSION: 2 Exhibits This Characteristic (2)

> CAREGIVER LIMITATIONS @ ADM: 1 Minimal or None (1)

> PERSON COMPLETING EVL/ADM FORM: 100 HBPCPROVIDER,TWO HINES ISC

> ...OK? Yes// \<RET\> (Yes)

> DATE EVAL/ADM FORM COMPLETED: T (FEB 29, 2000)

> CASE MANAGER: 100 HBPCPROVIDER,TWO HINES ISC

> ...OK? Yes// \<RET\> (Yes)

## Discharge Data Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCDIS\]

This option allows you to enter and edit the discharge data (also known as Form 5) in the HBHC Patient file \#631.

### Complete Episode of Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A “complete” episode of care consists of both an admission and a discharge or a reject, with each episode being a separate HBHC Patient file record. An admission must exist before a discharge is allowed. The package will NOT allow the creation of an additional episode of care until the patient has been discharged from the last episode. This is the message you receive if you attempt to do this using the Evaluation/Admission Data Entry option.

> Select HBHC PATIENT NAME: "HBPCPATIENT,SIX" HBPCPATIENT,SIX 12-1-12 000000006 YES MILITARY RETIREE

> Are you adding ‘HBPCPATIENT,SIX' as a new HBHC PATIENT (the 13TH)? No//Y (Yes)

> HBHC PATIENT DATE: T (MAR 09, 2000)

> Patient must be discharged from last episode of care before new episode

> can be entered. Current episode not created.

### Default Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Default values for the discharge data fields are pulled from the corresponding admission record data whenever possible to simplify data entry. Simply press the \<RET\> or \<ENTER\> key if the default answer is valid, or type in the correct field information.

### Exiting and Field Jumping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may ^ exit from the data entry process and return to the menu at any field prompt. Field jumping is not allowed due to branching logic contained within the data entry process. (Example: If “Died on HBHC (4)” is entered at the “Discharge Status” prompt, the software goes directly (branches) to the “Cause of Death” prompt and no Discharge data field prompts are displayed.)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="hbhc-patient-name-1" class="unnumbered">HBHC Patient Name</h4></td>
<td><p>Enter the name of a patient in the HBHC Patient file:</p>
<p>Last name,First name (e.g., HBPCPATIENT,FOUR)</p>
<p>First initial of last name plus last 4 digits of the SSN (e.g., S0004)</p></td>
</tr>
<tr class="even">
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><h4 id="discharge-date" class="unnumbered">Discharge Date</h4></td>
<td>Enter the date the patient was discharged from the HBPC Program.</td>
</tr>
<tr class="even">
<td><h4 id="eligibility-discharge" class="unnumbered">Eligibility @ Discharge</h4></td>
<td>This is the patient's eligibility.</td>
</tr>
<tr class="odd">
<td><h4 id="marital-status-discharge" class="unnumbered">Marital Status @ Discharge</h4></td>
<td><p>Enter one of the following for the patient's marital status:</p>
<ol type="1">
<li><blockquote>
<p>Married</p>
</blockquote></li>
<li><blockquote>
<p>Widowed</p>
</blockquote></li>
<li><blockquote>
<p>Separated</p>
</blockquote></li>
<li><blockquote>
<p>Divorced</p>
</blockquote></li>
<li><blockquote>
<p>Never Married</p>
</blockquote></li>
</ol>
<blockquote>
<p>9 Not Determined</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h4 id="living-arrangements-dc" class="unnumbered">Living Arrangements @ D/C</h4></td>
<td><p>Enter one of the following numeric codes (1-5, 9) that best defines the patient's living arrangements:</p>
<p>1 Alone</p>
<p>2 With Spouse</p>
<p>3 With Relatives</p>
<p>4 With Non-Relatives</p>
<p>5 Group Quarters, Not Health Related</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="discharge-status" class="unnumbered">Discharge Status</h4></td>
<td><p>Enter one of the following for the status of the patient at discharge:</p>
<ol type="1">
<li><blockquote>
<p>Transferred to Other Provider</p>
</blockquote></li>
<li><blockquote>
<p>Anticipated Institutionalization</p>
</blockquote></li>
<li><blockquote>
<p>Family or Self Care/No Regular Source</p>
</blockquote></li>
<li><blockquote>
<p>Died on HBHC</p>
</blockquote></li>
<li><blockquote>
<p>Moved Away/Lost to Contact</p>
</blockquote></li>
</ol>
<blockquote>
<p>9 Not Determined</p>
</blockquote></td>
</tr>
</tbody>
</table>

The Discharge Status field value controls which field prompts are displayed for data entry. If you change the value of the Discharge Status field after other fields have been filled in, you may receive messages stating a particular type of data exists and no longer coincides with what you just selected.

Depending on your selection for Discharge Status, you will branch to prompts appropriate for the status. All records end with the two prompts: Person Completing D/C Form and Date Discharge Form Completed.

#### If Discharge Status Code = Branches to

1 Transferred to Other Provider Transfer Destination

Type of Destination Agency

2 Anticipated Institutionalization Transfer Destination

Type of Destination Agency

3 Family or Self Care/No Regular Source Primary Diagnosis @ Discharge

Caregiver Limitations @ Discharge

4 Died on HBHC Cause of Death

5 Moved Away/Lost to Contact Primary Diagnosis @ Discharge

Caregiver Limitations @ Discharge

9 Not Determined Primary Diagnosis @ Discharge

Caregiver Limitations @ Discharge

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="transfer-destination" class="unnumbered">Transfer Destination</h4></td>
<td><p>Enter the code that best describes the patient’s transfer destination. This field is only prompted for when the Discharge Status field contains either 1 (Transferred to Other Provider) or 2 (Anticipated Institutionalization).</p>
<p>1 VA Provided Care</p>
<p>2 Non VA Care</p>
<p>3 VA Fee Basis/Contract</p></td>
</tr>
<tr class="even">
<td><h4 id="type-of-destination-agency" class="unnumbered">Type of Destination Agency</h4></td>
<td><p>Enter the code that best represents the patient's type of</p>
<p>destination agency. This field is only prompted for when the Discharge Status field contains either 1 (Transferred to Other Provider) or 2 (Anticipated Institutionalization).</p>
<p>1 General Hospital</p>
<p>2 Specialty Hospital</p>
<p>3 Nursing Home</p>
<p>4 Residential Care Facility/Domiciliary</p>
<p>5 Hospice</p>
<p>6 Community-Based Services</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="cause-of-death" class="unnumbered">Cause of Death</h4></td>
<td>Enter the patient’s cause of death. This is a free text field (1 – 30 characters). This field is only prompted for when Discharge Status field contains 4 (Died on HBHC). This information is not transmitted to Austin.</td>
</tr>
<tr class="even">
<td><h4 id="primary-diagnosis-discharge" class="unnumbered">Primary Diagnosis @ Discharge</h4></td>
<td><span id="icd4" class="anchor"></span>Enter the ICD9 or ICD10 diagnosis code for the patient's primary diagnosis.</td>
</tr>
<tr class="odd">
<td><h4 id="secondary-diagnosis-dc" class="unnumbered">Secondary Diagnosis @ D/C</h4></td>
<td>Enter the secondary diagnosis. This is a free text field (1 – 30 characters). This information is not transmitted to Austin.</td>
</tr>
<tr class="even">
<td><h4 id="vision-discharge" class="unnumbered">Vision @ Discharge</h4></td>
<td><p>Enter the code that best represents the patient's vision.</p>
<p>1 Normal or Minimal Loss</p>
<p>2 Moderate Loss</p>
<p>3 Severe Loss</p>
<p>4 Total Blindness</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="hearing-discharge" class="unnumbered">Hearing @ Discharge</h4></td>
<td><p>Enter the code that best represents the patient's hearing.</p>
<p>1 Normal or Minimal Loss</p>
<p>2 Moderate Loss</p>
<p>3 Severe Loss</p>
<p>4 Total Deafness</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="expressive-communication-dc" class="unnumbered">Expressive Communication @ D/C</h4></td>
<td><p>Enter the code that best describes the patient's ability to communicate with others.</p>
<p>1 Speaks and is Usually Understood</p>
<p>2 Speaks But is Understood Only with Difficulty</p>
<p>3 Uses Only Sign Language, Symbol Board or Writing</p>
<p>4 Uses Only Gestures, Grunts, or Primitive Symbols</p>
<p>5 Does Not Convey Needs</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="receptive-communication-dc" class="unnumbered">Receptive Communication @ D/C</h4></td>
<td><p>Enter the code that best describes the patient's ability to understand others.</p>
<blockquote>
<p>1 Usually Understands Oral Communication</p>
<p>2 Has Limited Comprehension of Oral Communication</p>
<p>3 Understands by Depending on Lip Reading, Written Material, or Sign Language</p>
<p>4 Understands Primitive Gestures, Facial Expres., Pictograms, and/or Env. Cues</p>
<p>5 Does Not Understand</p>
<p>9 Not Determined</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h4 id="bathing-discharge" class="unnumbered">Bathing @ Discharge</h4></td>
<td><p>Enter the code that describes how much help the patient requires bathing.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="dressing-discharge" class="unnumbered">Dressing @ Discharge</h4></td>
<td><p>Enter the code that describes how much help the patient requires dressing.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="toilet-usage-discharge" class="unnumbered">Toilet Usage @ Discharge</h4></td>
<td><p>Enter the code that describes how much help the patient requires using the toilet.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="transferring-discharge" class="unnumbered">Transferring @ Discharge</h4></td>
<td><p>Enter the code that describes how much help the patient requires transferring.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="eating-discharge" class="unnumbered">Eating @ Discharge</h4></td>
<td><p>Enter the code that describes how much help the patient requires eating.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="walking-discharge" class="unnumbered">Walking @ Discharge</h4></td>
<td><p>Enter the code that describes how much help the patient requires walking.</p>
<p>1 No Help</p>
<p>2 Receives Help</p>
<p>3 Not Done or Done Without Patient Participation</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="bowel-continence-discharge" class="unnumbered">Bowel Continence @ Discharge</h4></td>
<td><p>Enter the code that describes the patient's bowel continence.</p>
<p>1 Continent or Ostomy/Catheter Self Care</p>
<p>2 Incontinent Occasionally</p>
<p>3 Incontinent or Ostomy/Catheter Not Self Care</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="bladder-continence-discharge" class="unnumbered">Bladder Continence @ Discharge</h4></td>
<td><p>Enter the code that describes the patient's bladder continence.</p>
<p>1 Continent or Ostomy/Catheter Self Care</p>
<p>2 Incontinent Occasionally</p>
<p>3 Incontinent or Ostomy/Catheter Not Self Care</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="mobility-discharge" class="unnumbered">Mobility @ Discharge</h4></td>
<td><p>Enter the code that describes the patient's mobility.</p>
<p>1 Goes Outdoors Without Help</p>
<p>2 Goes Outdoors With Help</p>
<p>3 Confined Indoors, Not Bed Disabled</p>
<p>4 Bed Disabled</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="adaptive-tasks-discharge" class="unnumbered">Adaptive Tasks @ Discharge</h4></td>
<td><p>Enter the code that describes the patient's ability to perform adaptive tasks.</p>
<p>1 No Help</p>
<p>2 Requires Help</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="behavior-problems-discharge" class="unnumbered">Behavior Problems @ Discharge</h4></td>
<td><p>Enter the code that describes whether or not the patient has behavior problems.</p>
<p>1 Does Not Exhibit This Characteristic</p>
<p>2 Exhibits This Characteristic</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="disorientation-discharge" class="unnumbered">Disorientation @ Discharge</h4></td>
<td><p>Enter the code that describes whether or not the patient is disoriented.</p>
<p>1 Does Not Exhibit This Characteristic</p>
<p>2 Exhibits This Characteristic</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="mood-disturbance-discharge" class="unnumbered">Mood Disturbance @ Discharge</h4></td>
<td><p>Enter the code that describes whether or not the patient has a mood disturbance.</p>
<p>1 Does Not Exhibit This Characteristic</p>
<p>2 Exhibits This Characteristic</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="odd">
<td><h4 id="caregiver-limitations-dc" class="unnumbered">Caregiver Limitations @ D/C</h4></td>
<td><p>Enter the level of limitations of the caregiver.</p>
<p>1 Minimal or None</p>
<p>2 Moderate</p>
<p>3 Moderately Severe</p>
<p>4 No Caregiver</p>
<p>9 Not Determined</p></td>
</tr>
<tr class="even">
<td><h4 id="person-completing-dc-form" class="unnumbered">Person Completing D/C Form</h4></td>
<td>Enter the person's name that completed the form. Entering?? brings up a list of choices. If you do not see the person who completed the form, that person must be entered into HBHC Provider file # 631.4. Use the option <u>Provider File Data Entry</u> to add the person to the file. This information is not transmitted to Austin.</td>
</tr>
<tr class="odd">
<td><h4 id="date-discharge-form-completed" class="unnumbered">Date Discharge Form Completed</h4></td>
<td>Enter the date the form was completed. This information is not transmitted to Austin.</td>
</tr>
</tbody>
</table>

Example: Discharging a patient to another institution

Select HBHC PATIENT NAME: HBPCPATIENT,SEVEN 5-20-66 000000007

Enrollment Priority: GROUP 1 Category: IN PROCESS End Date:

01-03-00

DISCHARGE DATE: T (FEB 29, 2000)

ELIGIBILITY @ DISCHARGE: Service Connected 50% or More (01)

// \<RET\> Service Connected 50% or More (01)

MARITAL STATUS @ DISCHARGE: 1 Married (1)

LIVING ARRANGEMENTS @ D/C: 2 With Spouse (2)

DISCHARGE STATUS: 2 Anticipated Institutionalization (2)

TRANSFER DESTINATION: 2 Non VA Care (2)

TYPE OF DESTINATION AGENCY: 3 Nursing Home (3)

PRIMARY DIAGNOSIS @ DISCHARGE: 102.2 EARLY SKIN YAWS NEC

SECONDARY DIAGNOSES @ D/C: \<RET\>

VISION @ DISCHARGE: 3 Severe Loss (3)

HEARING @ DISCHARGE: 3 Severe Loss (3)

EXPRESSIVE COMMUNICATION @ D/C: 4 Uses Only Gestures, Grunts, or Primitive Symbols (4)

RECEPTIVE COMMUNICATION @ D/C: 5 Does Not Understand (5)

BATHING @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

DRESSING @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

TOILET USAGE @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

TRANSFERRING @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

EATING @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

WALKING @ DISCHARGE: 3 Not Done or Done Without Patient Participation (3)

BOWEL CONTINENCE @ DISCHARGE: 3 Incontinent or Ostomy/Catheter Not Self Care (3)

BLADDER CONTINENCE @ DISCHARGE: 3 Incontinent or Ostomy/Catheter Not Self Care (3)

MOBILITY @ DISCHARGE: 3 Confined Indoors, Not Bed Disabled (3)

ADAPTIVE TASKS @ DISCHARGE: 2 Requires Help (2)

BEHAVIOR PROBLEMS @ DISCHARGE: 1 Does Not Exhibit This Characteristic (1)

DISORIENTATION @ DISCHARGE: 2 Exhibits This Characteristic (2)

MOOD DISTURBANCE @ DISCHARGE: 2 Exhibits This Characteristic (2)

CAREGIVER LIMITATIONS @ D/C: 3 Moderately Severe (3)

PERSON COMPLETING D/C FORM: 100 HBPCPROVIDER,TWO HINES ISC

...OK? Yes// \<RET\> (Yes)

DATE DISCHARGE FORM COMPLETED: T (FEB 29, 2000)

# Using the Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use of these reports is discussed in the following pages:

Evaluation/Admission Data Report by Patient (80) \[HBHCRP2\]

> Patient Visit Data Report (80) \[HBHCRP3\]

> Discharge Data Report by Patient (80) \[HBHCRP5\]

> Episode of Care/Length of Stay Report (80) \[HBHCRP12\]

> Admissions/Discharges by Date Range Report (132) \[HBHCRP7\]

> Rejections from HBPC Program Report (132) \[HBHCRP16\]

> Visit Data by Date Range Report (80) \[HBHCRP4\]

> CPT Code Summary Report (80) \[HBHCRP17\]

> <span id="namechange1" class="anchor"></span>ICD Code/Dx Text by Date Range Report (80) \[HBHCR19A\]

> Unique Patients by Date Range Summary Report (80) \[HBHCRP20\]

Total Visits by Date Range Report (80) \[HBHCRP21\]

[^9]Patient Days of Care by Date Range Report (80) \[HBHCRP23\]

> Census Reports Menu ... \[HBHC CENSUS REPORTS MENU\]

> Program Census Report (80) \[HBHCRP10\]

> [^10] Address Included Program Census (132) \[HBHCRP25\]

> [^11] Expanded Program Census Report (80) \[HBHCRP24\]

> Active Census with ICD Code/Text Report (132) \[HBHCRP18\]

> Team Census Report (80) \[HBHCRP11\]

> Case Manager Census Report (132) \[HBHCRP6\]

> Provider Census Report (132) \[HBHCRP9\]

Reports Menu …

## Evaluation/Admission Data Report by Patient (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP2\]

This report is useful for displaying all admission data fields for a particular patient, or for locating information on a specific episode of care. The report format mimics the Evaluation/Admission (Form 3) pre-printed form layout. Data entry accuracy can be verified by comparing the report printout to the original Form 3.

Example:

Select HBHC PATIENT NAME: HBPCPATIENT,FIVE 1-1-40 000000005 YES SC VETERAN

Enrollment Priority: GROUP 2 Category: IN PROCESS End Date: 02-29-00

DEVICE: HOME// (Enter a printer or press the \<RET\> key to print to your screen)

\>\>\> HBPC Patient Evaluation/Admission Data Report \<\<\<

Run Date: FEB 29, 2000

================================================================================

Patient Name: HBPCPATIENT,FIVE Last Four: 0004

================================================================================

1\. Hospital Number: 499 \| 20. Primary Diagnosis @ Adm: 157.1

--------------------------------------------------------------------------------

2\. Date: 02-29-00 \| 21. Secondary Diagnoses @ Adm:

--------------------------------------------------------------------------------

3\. State Code: 17 \| 22. Vision @ Admission: 2

--------------------------------------------------------------------------------

4\. County Code: 031 \| Hearing @ Admission: 2

--------------------------------------------------------------------------------

5\. ZIP Code: 60611 \| 23. Expressive Communication @ Adm: 1

--------------------------------------------------------------------------------

6\. Eligibility @ Evaluation: 03 \| 24. Receptive Communication @ Adm: 1

--------------------------------------------------------------------------------

7\. Birth Year: 1940 \| 25. Bathing @ Admission: 2

--------------------------------------------------------------------------------

8\. Period of Service: 07 \| Dressing @ Admission: 2

--------------------------------------------------------------------------------

9\. Sex: 1 \| Toilet Usage @ Admission: 2

--------------------------------------------------------------------------------

[^12]10. Race: 1 \| Transferring @ Admission: 2 \|

--------------------------------------------------------------------------------

11\. Marital Status @ Evaluation: 1 \| Eating @ Admission: 2

--------------------------------------------------------------------------------

12\. Living Arrangements @ Eval: 1 \| Walking @ Admission: 3

--------------------------------------------------------------------------------

13\. Last Agency Providing Care: 1 \| 26. Bowel Continence @ Admission: 2

--------------------------------------------------------------------------------

14\. Type of Last Care Agency: 5 \| Bladder Continence @ Admission: 3

--------------------------------------------------------------------------------

15\. Referred While Inpatient: 1 \| 27. Mobility @ Admission: 3

--------------------------------------------------------------------------------

16\. Admit/Reject Action: 1 \| 28. Adaptive Tasks @ Admission: 2

--------------------------------------------------------------------------------

17\. Reject/Withdraw Reason: \| 29. Behavior Problems @ Admission: 1

--------------------------------------------------------------------------------

18\. Reject/Withdraw Disposition: \| 30. Disorientation @ Admission: 1

--------------------------------------------------------------------------------

19\. SSN: 000-00-0004 \| 31. Mood Disturbance @ Admission: 2

--------------------------------------------------------------------------------

\| 32. Caregiver Limitations @ Adm: 1

--------------------------------------------------------------------------------

\| 33. Person Completing Eval/Adm: 100

--------------------------------------------------------------------------------

\| Date Eval/Adm Completed: 02-29-00

--------------------------------------------------------------------------------

\| Case Manager: 100

--------------------------------------------------------------------------------

Reports Menu …

## [^13]Patient Visit Data Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP3\]

Use this option to obtain a list of visit dates for a patient over a selected date range. The

report prints the Visit Date, Provider Name and Number, Diagnosis(es), CPT codes and CPT modifiers.

If there are no visits for the patient you select, the following message is displayed:

> This patient has no visits on file.

Example:

Select PATIENT NAME: HBPCPATIENT,SEVEN 5-20-66 000000007 YES ACTIVE DUTY

Enrollment Priority: GROUP 1 Category: IN PROCESS End Date:

Beginning Report Date: 2/1/00 (FEB 01, 2000)

Ending Report Date: T (FEB 29, 2000)

DEVICE: HOME// (Enter a device)

\>\>\> HBPC Patient: HBPCPATIENT,SEVEN 000-00-0007 Visit Data Report \<\<\< Page: 1

Run Date: FEB 29, 2000 Date Range: FEB 01, 2000 to

FEB 29, 2000

================================================================================

Visit Date: 02-10-2000 Prov No.: 102 Prov Name: HBPCPROVIDER,TWO

Diagnosis: 161.3 MAL NEO CARTILAGE LARYNX

CPT Code: 92502 EAR AND THROAT EXAMINATION

Modifier: - 26 PROFESSIONAL COMPONENT

--------------------------------------------------------------------------------

==== End of Report ====

Reports Menu …

## Discharge Data Report by Patient (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP5\]

Use this option to display all discharge data fields for a particular patient, or for locating specific episode of care information. Data entry accuracy can be verified by comparing the report printout to the original Form 5.

Example:

Select HBHC PATIENT NAME: HBPCPATIENT,SEVEN 5-20-66 000000007 YES ACTIVE DUTY

Enrollment Priority: GROUP 1 Category: IN PROCESS End Date:

01-03-00

DEVICE: HOME// (Enter a printer or press the \<RET\> key to print to your screen)

\>\>\> HBPC Patient Discharge Data Report \<\<\<

Run Date: FEB 29, 2000

================================================================================

Patient Name: HBPCPATIENT,SEVEN Last Four: 0007

================================================================================

1\. Hospital Number: 499 \| 20. Primary Diagnosis @ D/C: 102.2

--------------------------------------------------------------------------------

2\. Discharge Date: 02-29-00 \| 21. Secondary Diagnoses @ D/C:

--------------------------------------------------------------------------------

3\. Eligibility @ Discharge: 01 \| 22. Vision @ Discharge: 3

--------------------------------------------------------------------------------

4\. Marital Status @ Discharge: 1 \| Hearing @ Discharge: 3

--------------------------------------------------------------------------------

5\. Living Arrangements @ D/C: 2 \| 23. Expressive Communication @ D/C: 4

...

Reports Menu …

## Episode of Care/Length of Stay Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP12\]

This report mimics the Austin generated DMS COIN 157 report which is received quarterly. This report lists only those patients admitted or discharged in the date range specified.

> **NOTE:** To obtain an accurate census report, use the admission date for the patient that has been on the program the longest. An arbitrary date of 1/1/85 will provide the same results. This report will only print active patients.

[^14]The report is sorted by patient and includes: Patient Name, SSN, Admission Date, Discharge Date, and Length of Stay. It does the following:

- Calculates the length of stay on episodes without a Discharge Date,
- Prints "Active" in the Discharge Date column if there is no Discharge Date,
- Displays patients and length of stay totals by day, and
- For complete episodes of care, average length of stay and final totals are included.

Example:

Beginning Report Date: T-365 (MAR 02, 1999)

Ending Report Date: T (MAR 01, 2000)

DEVICE: HOME// (Enter a printer or press the \<RET\> key to print to your screen)

\>\>\> HBPC Episode of Care/Length of Stay Report \<\<\< Page: 1

Run Date: MAR 01, 2000 Date Range: MAR 02, 1999 to

MAR 01, 2000

Discharge Length

Patient Name SSN Date Date /Stay

================================================================================

HBPCPATIENT,EIGHT 000-00-0008 11-03-99 Active 119

--------------------------------------------------------------------------------

HBPCPATIENT,FIVE 000-00-0005 02-29-00 Active 1

--------------------------------------------------------------------------------

HBPCPATIENT,NINE 000-00-0009 12-03-99 12-03-99 0

--------------------------------------------------------------------------------

HBPCPATIENT,TWO 000-00-0002 01-03-00 02-29-00 57

--------------------------------------------------------------------------------

HBPCPATIENT,TEN 000-00-0010 12-02-99 Active 90

--------------------------------------------------------------------------------

Total Patients: 5 Total Days: 267

Complete Episodes of Care Only:

Total Patients: 2 Total Days: 57 Average Length of Stay: 28

==== End of Report ====

Reports Menu …

## Admissions/Discharges by Date Range Report (132)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP7\]

This report prints HBPC Admissions or Discharges for a selected date range. The report is sorted by Admission/Discharge Date and includes: Admission/Discharge Date, Patient Name, <span id="icd5" class="anchor"></span>SSN, and ICD9 or ICD10 Code and Diagnosis Text (Primary Diagnosis @ Admission/Discharge), with Total. The report requires a device that can print 132 column format.

<span id="p25_V_7" class="anchor"></span>Note: The column header in various ICD Code reports is customized to match the type of ICD code that appears in the report. If the report only covers ICD-9 era dates, the column header is ICD9; if the report covers only ICD-10 era dates, the column header is ICD10; and if the report covers both ICD-9 and ICD-10 era dates, the column header is ICD.

Example:

Select Admissions or Discharges: (A/D): Admissions

Beginning Report Date: 3/21/2000 (MAR 21, 2000)

Ending Report Date: T (MAR 28, 2000)

DEVICE: HOME// (Enter a device capable of printing 132 columns)

\>\>\> HBPC Admissions by Date Range Report \<\<\< Page: 1

Run Date: MAR 28, 2000 Date Range: MAR 21, 2000 to

MAR 28, 2000

Admission Date Patient Name SSN ICD9 Code Diagnosis Text

===============================================================================================================

11-03-99 HBPCPATIENT,EIGHT 000-00-0008 571.49 CHRONIC HEPATITIS NEC

---------------------------------------------------------------------------------------------------------------

12-02-99 HBPCPATIENT1,ONE 000-00-0011 230.2 CA IN SITU STOMACH

---------------------------------------------------------------------------------------------------------------

12-03-99 HBPCPATIENT,NINE 000-00-0009 231.0 CA IN SITU LARYNX

---------------------------------------------------------------------------------------------------------------

01-03-00 HBPCPATIENT,TWO 000-00-0002 147.8 MAL NEO NASOPHARYNX NEC

---------------------------------------------------------------------------------------------------------------

02-29-00 HBPCPATIENT,FIVE 000-00-0005 157.1 MAL NEO PANCREAS BODY

---------------------------------------------------------------------------------------------------------------

03-09-00 HBPCPATIENT1,TWO 000-00-0012 157.3 MAL NEO PANCREATIC DUCT

---------------------------------------------------------------------------------------------------------------

===============================================================================================================

Total Admissions: 6

===============================================================================================================

==== End of Report ====

Reports Menu …

## [^15]Rejections from HBPC Program Report (132)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP16\]

Use this option to print a list of rejections for a selected date range. The data is sorted by patient name and includes: Patient Name, SSN, Evaluation Date, and Reject/Withdraw Reason, with Total. The report requires a device that can print 132 column format.

Example:

Beginning Report Date: 3/1/2000 (MAR 01, 2000)

Ending Report Date: 3/31/2000 (MAR 31, 2000)

DEVICE: HOME// (Enter a device that is capable of printing 132 columns)

\>\>\> HBPC Rejections from Program Report \<\<\< Page: 1

Run Date: APR 05, 2000 Date Range: MAR 01, 2000 to

MAR 31, 2000

Patient Name SSN Date Reject/Withdraw Reason

===============================================================================================================

HBPCPATIENT1,THREE 000-00-0013 03-06-00 Not Located in Service Area (01)

---------------------------------------------------------------------------------------------------------------

===============================================================================================================

Program Rejections Total: 1

===============================================================================================================

==== End of Report ====

Reports Menu …

## [^16]Visit Data by Date Range Report (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP4\]

This report is sorted alphabetically by provider. Each provider starts a new page with a beginning page number of 1. The report contains the Visit Date, Patient, Last 4 of the SSN, Diagnosis(es), CPT Codes and Modifiers, with a visit total. A final visit total is included at the end of the report if all providers selected.

Do you wish to include ALL providers on the report? Yes// N (No)

Select HBPC Provider: HBPCPROVIDER,TWO HPT IRM FIELD OFFICE I

RM FIELD OFFICE 152 HBPCPROVIDER,TWO BLUE TEAM

...OK? Yes// \<RET\> (Yes)

Select HBPC Provider: \<RET\>

Beginning Report Date: 5/29 (MAY 29, 2000)

Ending Report Date: 6/2 (JUN 02, 2000)

DEVICE: HOME// (Enter a printer or press the \<RET\> key to view on screen.)

\>\>\> HBPC Visit Data by Date Range Report \<\<\< Page: 1

Provider: HBPCPROVIDER,TWO (152)

Run Date: JUN 02, 2000 Date Range: MAY 29, 2000 to

JUN 02, 2000

================================================================================

Visit Date: 06-02-2000 Patient Name: HBPCPATIENT,EIGHT Last 4: 0008

Diagnosis: 161.3 MAL NEO CARTILAGE LARYNX

CPT Code: 92502 EAR AND THROAT EXAMINATION

Modifier: - 26 PROFESSIONAL COMPONENT

Modifier: - 77 REPEAT PROCEDURE BY ANOTHER PHYSICIAN

--------------------------------------------------------------------------------

================================================================================

Provider: HBPCPROVIDER,TWO (152) Visits Total: 1

================================================================================

==== End of Report ====

Reports Menu …

## [^17]CPT Code Summary Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP17\]

Use this option to obtain totals for selected procedure(s) (CPT Codes) over a specified date range. You are prompted for a date range, and CPT Code(s) or range of codes for inclusion on the report. The data is sorted by CPT Code with totals for each CPT Code plus a grand total.

Example:

Beginning Report Date: 3/1/2000 (MAR 01, 2000)

Ending Report Date: 3/31/2000 (MAR 31, 2000)

Will CPT Codes selected be a Range of codes (Y/N)? NO

Select CPT: W0100 GENERAL MEDICAL EXAM, VA FAC

Select CPT: \<RET\>

DEVICE: HOME// (Enter a printer or press the \<RET\> key to print to your screen)

\>\>\> HBPC CPT Code Summary Report \<\<\< Page: 1

Run Date: APR 08, 2000 Date Range: MAR 01, 2000 to

MAR 31, 2000

CPT Code Total

================================================================================

W0100 GENERAL MEDICAL EXAM, VA FAC 2

--------------------------------------------------------------------------------

================================================================================

Total CPT Codes: 2

================================================================================

==== End of Report ====

Reports Menu …

## [^18][^19]Provider CPT Code Summary Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP22\]

Use this option to obtain a total for selected procedures performed by specific providers. You are prompted to enter a date range, CPT code(s) (can be range of CPTs), and Provider(s) for inclusion on report.

This report is sorted alphabetically by provider. Each provider starts a new page with a beginning page number of 1. A final procedure total is included at the end of the report if all providers selected.

Beginning Report Date: 3/1/2000 (MAR 01, 2000)

Ending Report Date: 3/31/2000 (MAR 31, 2000)

Will CPT Codes selected be a Range of codes (Y/N)? NO

Select CPT: W0100 GENERAL MEDICAL EXAM, VA FAC

Select CPT: \<RET\>

Select HBPC Provider: ?

Answer with HBHC PROVIDER NUMBER, or PROVIDER NAME

Choose from:

100 HBPCPROVIDER,EIGHT BLUE TEAM

101 HBPCPROVIDER,FOUR HINES TEAM 2

102 HBPCPROVIDER,TWO BLUE TEAM

104 HBPCPROVIDER,FIVE HINES TEAM 2

150 HBPCPROVIDER,THREE HINES TEAM 2

...

Select HBPC Provider: 150 HBPCPROVIDER,THREE

...OK? Yes// \<RET\> (Yes)

Select HBPC Provider: \<RET\>

DEVICE: HOME// (Enter a printer or press the \<RET\> key to print to your screen)

\>\>\> HBPC Provider: HBPCPROVIDER,THREE CPT Code Summary Report \<\<\< Page: 1

Run Date: APR 08, 2000 Date Range: MAR 01, 2000 to

MAR 31, 2000

CPT Code Total

================================================================================

W0100 GENERAL MEDICAL EXAM, VA FAC 2

--------------------------------------------------------------------------------

================================================================================

Total CPT Codes: 2

================================================================================

==== End of Report ====

Reports Menu …

## [^20]ICD Code/Dx Text by Date Range Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCR19A\]

<span id="icd6" class="anchor"></span>Use this option to print a list of all or selected patient diagnoses for visits over a specified date range. You are prompted to enter a date range, and the ICD9 or ICD10 Code(s), or category of codes, for inclusion on the report. The report is sorted by ICD9 or ICD10 Code category, then alphabetically by patient within the category, with totals for each ICD9 or ICD10 Code category, plus a grand total.

<span id="p25_V_12" class="anchor"></span>Note: The column header in various ICD Code reports is customized to match the type of ICD code that appears in the report. If the report only covers ICD-9 era dates, the column header is ICD9; if the report covers only ICD-10 era dates, the column header is ICD10; and if the report covers both ICD-9 and ICD-10 era dates, the column header is ICD.

Example:

Beginning Report Date: 12/1/99 (DEC 01, 1999)

Ending Report Date: 12/31/99 (DEC 31, 1999)

Do you wish to include ALL ICD Diagnosis Codes on the report? No// Y (Yes)

DEVICE: HOME// (Enter a printer or press the \<RET\> key to print to your screen)

\>\>\> HBPC ICD Code/Diagnosis Text by Date Range Report \<\<\< Page: 1

Run Date: MAR 28, 2000 Date Range: DEC 01, 1999 to

DEC 31, 1999

Patient Name SSN ICD9 Code/Diagnosis Text

================================================================================

HBPCPATIENT1,FOUR 000-00-0014 147.1 MAL NEO POST NASOPHARYNX

Category: 147 Count: 1

--------------------------------------------------------------------------------

HBPCPATIENT,TWO 000-00-0002 230.1 CA IN SITU ESOPHAGUS

Category: 230 Count: 1

--------------------------------------------------------------------------------

HBPCPATIENT1,FOUR 000-00-0014 416.8 CHR PULMON HEART DIS NEC

HBPCPATIENT,FIVE 000-00-0005 416.8 CHR PULMON HEART DIS NEC

HBPCPATIENT1,FIVE 000-00-0015 416.8 CHR PULMON HEART DIS NEC

Category: 416 Count: 3

--------------------------------------------------------------------------------

.....

================================================================================

ICD10 Diagnosis Categories Total: 46

================================================================================

==== End of Report ====

Reports Menu ...

## [^21]Unique Patients by Date Range Summary Report (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP20\]

Use this report to obtain a total for single and multiple visits by unique patients for a selected date range. You are prompted to enter the date range for inclusion on the report. The report prints separate totals for patients with a single visit only or multiple visits, plus a grand total for unique patients.

Example:

Beginning Report Date: 12/1/99 (DEC 01, 1999)

Ending Report Date: 12/31/99 (DEC 31, 1999)

DEVICE: HOME// (Enter a printer or press the \<RET\> key to print to your screen)

\>\>\> HBPC Unique Patients by Date Range Summary Report \<\<\< Page: 1

Run Date: MAR 28, 2000 Date Range: DEC 01, 1999 to

DEC 31, 1999

================================================================================

Total Patients with Single Appointment Only: 20

Total Patients with Multiple Appointments: 7

Total Unique Patients: 27

==== End of Report ====

Reports Menu …

## [^22]Total Visits by Date Range Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP21\]

Use this option to obtain a total number of visits for a selected date range. A visit is omitted from the report if it contains any of the CPT codes shown in the example. You can also select additional CPT codes to omit from the report. The report includes: Patient Name, the last four digits of the SSN, Total Visits per patient, Date (admitted to HBPC program) and Discharge Date (if applicable), with grand totals of patients and visits.

Example:

Beginning Report Date: 3/1/2000 (MAR 01, 2000)

Ending Report Date: 3/31/2000 (MAR 31, 2000)

Visits containing any of the following CPT Codes are omitted from report:

    Active                               Inactive/Historical

  98966  HC PRO PHONE CALL 5-10 MIN    99361  PHYSICIAN/TEAM CONFERENCE

  98967  HC PRO PHONE CALL 11-20 MIN   99362  PHYSICIAN/TEAM CONFERENCE

  98968  HC PRO PHONE CALL 21-30 MIN   99371  PHYSICIAN PHONE CONSULTATION

  99358  PROLONGED SERV, W/O CONTACT   99372  PHYSICIAN PHONE CONSULTATION

  99359  PROLONGED SERV, W/O CONTACT   99373  PHYSICIAN PHONE CONSULTATION

  99367  TEAM CONF W/O PAT BY PHYS     99376  CARE PLAN OVERSIGHT/OVER 60

  99368  TEAM CONF W/O PAT BY HC PRO

  99374  HOME HEALTH CARE SUPERVISION

  99375  HOME HEALTH CARE SUPERVISION

  99441  PHONE E/M PHYS/QHP 5-10 MIN

  99442  PHONE E/M PHYS/QHP 11-20 MIN

  99443  PHONE E/M PHYS/QHP 21-30 MIN

Enter any other CPT code you wish to omit: \<RET\>

Select one of the following:

A Alphabetical

V Number of Visits

[^23]Sort Preference: V// \<RET\> Number of Visits

DEVICE: HOME// (enter a printer or press the \<RET\> key to print to your screen)

\>\>\> HBPC Total Visits by Date Range, Visit Sort Report \<\<\< Page: 1

Run Date: APR 03, 2000 Date Range: MAR 01, 2000 to

MAR 31, 2000

Last Visit Discharge

Patient Name Four Total Date Date

================================================================================

Visits containing any of the following CPT Codes are omitted from report:

    Active                               Inactive/Historical

  98966  HC PRO PHONE CALL 5-10 MIN    99361  PHYSICIAN/TEAM CONFERENCE

  98967  HC PRO PHONE CALL 11-20 MIN   99362  PHYSICIAN/TEAM CONFERENCE

  98968  HC PRO PHONE CALL 21-30 MIN   99371  PHYSICIAN PHONE CONSULTATION

  99358  PROLONGED SERV, W/O CONTACT   99372  PHYSICIAN PHONE CONSULTATION

  99359  PROLONGED SERV, W/O CONTACT   99373  PHYSICIAN PHONE CONSULTATION

  99367  TEAM CONF W/O PAT BY PHYS     99376  CARE PLAN OVERSIGHT/OVER 60

  99368  TEAM CONF W/O PAT BY HC PRO

  99374  HOME HEALTH CARE SUPERVISION

  99375  HOME HEALTH CARE SUPERVISION

  99441  PHONE E/M PHYS/QHP 5-10 MIN

  99442  PHONE E/M PHYS/QHP 11-20 MIN

  99443  PHONE E/M PHYS/QHP 21-30 MIN

--------------------------------------------------------------------------------

HBPCPATIENT,FIVE 0005 1 MAR 03, 2000 MAR 03, 2000

--------------------------------------------------------------------------------

HBPCPATIENT1,TWO 0012 1 MAR 09, 2000 MAR 09, 2000

--------------------------------------------------------------------------------

HBPCPATIENT,NINE 0009 1 MAR 03, 1999 MAR 03, 2000

--------------------------------------------------------------------------------

...

--------------------------------------------------------------------------------

Total Patients with 1 Visit(s): 24

--------------------------------------------------------------------------------

HBPCPATIENT,TWO 0002 2 MAR 29, 2000 MAR 29, 2000

--------------------------------------------------------------------------------

Total Patients with 2 Visit(s): 1

--------------------------------------------------------------------------------

================================================================================

\*\*\*\*\*\* Total Visits Summary \*\*\*\*\*\*

================================================================================

Total Patients with 1 Visit(s): 24

Total Patients with 2 Visit(s): 1

------

Total Patients: 25

Total Visits: 26

==== End of Report ====

## [^24] Patient Days of Care by Date Range Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP23\]

Use this option to print HBPC Patient Days of Care by Date Range Report. Report includes: file internal entry number (IEN), Patient Name, Social Security Number (SSN), Date, Discharge Date, & Patient Days. Patient Days is calculated based on the user selectable date range. Summary totals of Patients and Patient Days are included for both Complete Episodes of Care and Active Cases.

Date of Discharge is omitted from the Patient Days total (e.g., Adm Date: 7/1/03, D/C Date: 7/5/03 would total 4 Patient Days, not 5). Report prints in 80 column format

Example:

Beginning Report Date: 10/01/03 (OCT 01, 2003)

Ending Report Date: 12/31/03 (DEC 31, 2003)

DEVICE: HOME// (Enter a device that prints 80 columns)

\>\>\> HBPC Patient Days of Care by Date Range Report \<\<\< Page: 1

Run Date: JUL 22, 2004 Date Range: OCT 01, 2003 to DEC 31, 2003

Discharge Patient

IEN Patient Name SSN Date Date Days

======================================================================================

\`1588 HBHpatient,One 000-04-2286 02-05-01 06-04-04 92

--------------------------------------------------------------------------------------

\`1903 HBHpatient,Two 000-01-0761 04-10-03 03-04-04 92

--------------------------------------------------------------------------------------

\`1869 HBHpatient,Three 000-08-7970 01-14-03 10-02-03 1

--------------------------------------------------------------------------------------

\`1274 HBHpatient,Four 000-13-2705 05-28-99 10-07-03 6

--------------------------------------------------------------------------------------

\`1884 HBHpatient,Five 000-11-6057 02-13-03 92

--------------------------------------------------------------------------------------

\`1847 HBHpatient,Six 000-06-9738 11-15-02 92

--------------------------------------------------------------------------------------

\`1909 HBHpatient,Seven 000-06-8732 04-22-03 12-16-03 76

--------------------------------------------------------------------------------------

\`1957 HBHpatient,Eight 000-26-1343 10-27-03 66

…

======================================================================================

\>\>\> Date Range: OCT 01, 2003 to DEC 31, 2003 \<\<\<

======================================================================================

Total Active Patients: 169

======================================================================================

Complete Episodes of Care Only:

Total Patients: 37 Total Patient Days in Date Range: 1,327

======================================================================================

Total Patients: 206 Total Patient Days in Date Range: 15,576

======================================================================================

==== End of Report ====

Reports Menu …

## Census Reports Menu ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHC CENSUS REPORTS MENU\]

The Census Reports Menu contains the following options:

Program Census Report (80) \[HBHCRP10\]

[^25] Address Included Program Census (132) \[HBHCRP25\]

[^26] Expanded Program Census Report (80) \[HBHCRP24\]

<span id="icd7" class="anchor"></span>Active Census with ICD Code/Text Report (132) \[HBHCRP18\]

Team Census Report (80) \[HBHCRP11\]

Case Manager Census Report (132) \[HBHCRP6\]

Provider Census Report (132) \[HBHCRP9\]

Reports Menu …

Census Reports Menu …

### Program Census Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP10\]

Use this option to obtain an HBPC census report for a specified date range. The report is sorted by patient name and includes: Patient Name, SSN, and [^27]Admission Date, with Total.

> **NOTE:** To obtain an accurate census report, use the admission date for the patient that has been on the program the longest. An arbitrary date of 1/1/85 will give you the same results. This report will only give you active patients.

Example:

Beginning Report Date: 1/1/99 (JAN 01, 1999)

Ending Report Date: 12/31/99 (DEC 31, 1999)

DEVICE: HOME// (Enter a printer or press the \<RET\> key to print to your screen)

\>\>\> HBPC Program Census Report \<\<\< Page: 1

Run Date: MAR 29, 2000 Date Range: JAN 01, 1999 to

DEC 31, 1999

Patient Name SSN Date

================================================================================

HBPCPATIENT,EIGHT 000-00-0008 NOV 03, 1999

--------------------------------------------------------------------------------

HBPCPATIENT1,SIX 000-00-0016 DEC 02, 1999

--------------------------------------------------------------------------------

...

--------------------------------------------------------------------------------

================================================================================

Program Census Total: 64

================================================================================

==== End of Report ====

Reports Menu …

Census Reports Menu …

### [^28]Address Included Program Census (132)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP25\]

This option prints the HBPC Address Included Program Census Report. The user is prompted to enter a date range for inclusion on the report. The report is sorted alphabetically by patient name & includes: Patient Name, Last 4, Admission Date, Address, City, ZIP Code, Phone Number, Case Manager, & Total. Report prints in 132 column format.

Example:

Beginning Report Date: 1/1/04 (JAN 01, 2004)

Ending Report Date: 1/31/04 (NOV 09, 2004)

DEVICE: HOME// (Enter a device that prints 132 columns)

\>\>\> HBPC Address Included Program Census Report \<\<\< Page: 1

Run Date: JUL 22, 2004 Date Range: JAN 01, 2004 to JAN 31, 2004

Last Admission ZIP Case

Patient Name Four Date Street Address City Code Phone Manager

=================================================================================================

HBHPT,ONE 0000 JAN 14, 2004 123 Oak Leaf Perch 70000 (000)320-0000 HBHPROVIDER1

-------------------------------------------------------------------------------------------------

HBHPT,TWO 0000 JAN 09, 2004 1355 Sherwood Rogers 90000 (000)280-0000 HBHPROVIDER2

-------------------------------------------------------------------------------------------------

HBHPT,THREE 0000 JAN 15, 2004 9584 Mouse Top Lane 90000 (000)980-0000 HBHPROVIDER2

-------------------------------------------------------------------------------------------------

HBHPT,FOUR 0000 JAN 15, 2004 911 Help Court Menu 40000 (000)920-0000 HBHPROVIDER3

-------------------------------------------------------------------------------------------------

HBHPT,FIVE 0000 JAN 08, 2004 938 George Dr Forman 20000 (000)430-0000 HBHPROVIDER4

-------------------------------------------------------------------------------------------------

HBHPT,SIX 0000 JAN 20, 2004 221 Normal Dr Lane 20000 (000)340-0000 HBHPROVIDER5

-------------------------------------------------------------------------------------------------

HBHPT,SEVEN 0000 JAN 14, 2004 982 Powder Puff Canes 90000 (000)950-0000 HBHPROVIDER4

=================================================================================================

Program Census Total: 7

=================================================================================================

==== End of Report ====

Reports Menu …

Census Reports Menu …

### [^29]Expanded Program Census Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP24\]

Use this option to print the HBPC Expanded Program Census Report. The user is prompted to enter the date range for inclusion on the report. The report is sorted by patient name and includes: Patient Name, Last 4, Admission Date, Case Manager, Most Recent Visit Date, Visit Discipline, & total. Report prints in 80 column format.

Example:

Beginning Report Date: 1/1/04 (FEB 01, 2005

Ending Report Date: 1/31/04 (NOV 01, 2006)

DEVICE: HOME// (Enter a device that prints 80 columns)

\>\>\> HBPC Expanded Program Census Report \<\<\< Page: 1

Run Date: JUL 22, 2004 Date Range: JAN 01, 2004 to JAN 31, 2004

Last Admission Case Most Recent Visit

Patient Name Four Date Manager Visit Date/Time Discipline

=======================================================================================

HBHPATIENT,ONE 4358 JAN 14, 0000 HBHPROVIDER,ONE JUN 08, 2004@14:00 RNP/PA

--------------------------------------------------------------------------------------

HBHPATIENT,TWO 9584 JAN 09, 0000 HBHPROVIDER,TWO JUN 30, 2004@11:00 Other

--------------------------------------------------------------------------------------

HBHPATIENT,TWO 5832 JAN 15, 0000 HBHPROVIDER,FOUR MAY 21, 2004@15:30 RNP/PA

--------------------------------------------------------------------------------------

HBHPATIENT,FOUR 4805 JAN 15, 0000 HBHPROVIDER,ONE JAN 26, 2004@07:30 RNP/PA

--------------------------------------------------------------------------------------

HBHPATIENT,FIVE 1220 JAN 08, 0000 HBHPROVIDER,ONE FEB 05, 2004@10:50 Soc Wrkr

--------------------------------------------------------------------------------------

HBHPATIENT,SIX 2549 JAN 20, 0000 HBHPROVIDER,FOUR JUL 02, 2004@11:30 Other

--------------------------------------------------------------------------------------

HBHPATIENT,SEVEN 8685 JAN 14, 0000 HBHPROVIDER,ONE MAR 16, 2004@9:30 RNP/PA

======================================================================================

Program Census Total: 7

======================================================================================

==== End of Report ====

Reports Menu …

Census Reports Menu …

### [^30]Active Census with ICD Code/Text Report (132)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP18\]

<span id="icd8" class="anchor"></span>Use this option to print the HBPC active census including diagnoses for a specified date range. The report is sorted by patient name, then by admission date, and includes: Patient Name, SSN, [^31]Admission Date, ICD9 or ICD10 Code, and ICD9 or ICD10 Text, with Total. Report requires 132 column print format.

> **NOTE:** To obtain an accurate census report, use the admission date for the patient that has been on the program the longest. An arbitrary date of 1/1/85 will give you the same results. This report will only give you active patients.

<span id="p25_V_21" class="anchor"></span>Note: The column header in various ICD Code reports is customized to match the type of ICD code that appears in the report. If the report only covers ICD-9 era dates, the column header is ICD9; if the report covers only ICD-10 era dates, the column header is ICD10; and if the report covers both ICD-9 and ICD-10 era dates, the column header is ICD.

Example:

Beginning Report Date: 1/1/1999 (JAN 01, 1999)

Ending Report Date: 12/31/1999 (DEC 31, 1999)

DEVICE: HOME// (Enter a device that prints 132 columns)

\>\>\> HBPC Active Census with ICD Code/Text Report \<\<\< Page: 1

Run Date: MAR 29, 2000 Date Range: JAN 01, 1999 to

DEC 31, 1999

Patient Name SSN Date ICD9 Code Diagnosis Text

=========================================================================================================

HBPCPATIENT,EIGHT 000-00-0008 NOV 03, 1999 416.8 CHR PULMON HEART DIS NEC

---------------------------------------------------------------------------------------------------------

HBPCPATIENT1,SIX 000-00-0016 DEC 02, 1999 416.8 CHR PULMON HEART DIS NEC

---------------------------------------------------------------------------------------------------------

...

---------------------------------------------------------------------------------------------------------

=========================================================================================================

Active Census Total: 64

=========================================================================================================

==== End of Report ====

Reports Menu …

Census Reports Menu …

### Team Census Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP11\]

Use this option to print a census report for each team over a selected date range. The report is sorted by Team and includes: Team Name, Patient Name, SSN, and [^32]Admission Date, with Totals for each Team and Final Totals for all Teams.

> **NOTE:** To obtain an accurate census report, use the admission date for the patient that has been on the program the longest. An arbitrary date of 1/1/85 will give you the same results. This report will only give you active patients.

Example:

Beginning Report Date: 1/1/99 (JAN 01, 1999)

Ending Report Date: 12/31/99 (DEC 31, 1999)

DEVICE: HOME// (Enter a printer or press the \<RET\> key to print to your screen)

\>\>\> HBPC Team Census Report \<\<\< Page: 1

HBPC Team: Blue Team

Run Date: MAR 29, 2000 Date Range: JAN 01, 1999 to

DEC 31, 1999

Patient Name SSN Date

================================================================================

HBPCPATIENT,EIGHT 000-00-0008 NOV 03, 1999

--------------------------------------------------------------------------------

HBPCPATIENT1,SIX 000-00-0016 DEC 02, 1999

--------------------------------------------------------------------------------

...

--------------------------------------------------------------------------------

Team: Blue Team Census Total: 14

...

================================================================================

All Team Census Total: 64

================================================================================

==== End of Report ====

Reports Menu …

Census Reports Menu …

### [^33]Case Manager Census Report (132)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP6\]

Use this option to print a report of the census for selected or all case managers over a date range. The report is sorted by Case Manager and includes: Case Manager, Patient Name, SSN, Admission Date, Street Address, City, ZIP Code, and Phone, with Totals for each Case Manager and Final Totals if 'All' is selected. Each Case Manager begins a new page starting with page number 1. The report prints in 132 column format.

> **NOTE:** To obtain an accurate census report, use the admission date for the patient that has been on the program the longest. An arbitrary date of 1/1/85 will give you the same results. This report will only give you active patients.

Example:

Do you wish to include ALL case managers on the report? Yes// \<RET\> (Yes)

Beginning Report Date: 11/1/99 (NOV 01, 1999)

Ending Report Date: 11/30/99 (NOV 30, 1999)

DEVICE: HOME// (Enter a printer that supports 132 column printout)

\>\>\> HBPC Case Manager Census Report \<\<\< Page: 1

Case Manager: XXXXXXXX,PROVIDER (150)

Run Date: MAR 28, 2000 Date Range: NOV 01, 1999 to

NOV 30, 1999

Patient Name SSN Date Street Address City ZIP Code Phone

===============================================================================================================

HBPCPATIENT,EIGHT 000-00-0008 11-03-99 187 NOWHERE ST CHICAGO 60612-3939 666-098-7654

---------------------------------------------------------------------------------------------------------------

HBPCPATIENT,TWO 000-00-0002 12-03-99 123 SYCAMORE AVE CHICAGO 60606 666-123-4567

---------------------------------------------------------------------------------------------------------------

....

Case Manager: HBPCPROVIDER,THREE (150) Case Census Total: 10

....

===============================================================================================================

All Case Census Total: 34

===============================================================================================================

==== End of Report ====

Reports Menu …

Census Reports Menu …

### [^34]Provider Census Report (132)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP9\]

Use this option to obtain a census report by provider(s) for a specified date range. The report can be run for All or individual Providers. Only patients with a current admission will be included. The report is sorted by Provider and includes: Provider Name, Provider Number, Patient Name, SSN, Admission Date, Street Address, City, ZIP Code, and Phone, with Totals for each Provider and Final Totals if 'All' is selected. Each provider begins a new page starting with page number 1. The report prints in 132 column format.

> **NOTE:** The admission date is irrelevant for the date range even though it will appear on this report.

Example:

Do you wish to include ALL providers on the report? Yes// N (No)

Select HBPC Provider: HBPCPROVIDER,THREE NCA IRM FIELD OFFICE

PHYSICIAN 150 HBPCPROVIDER,THREE

...OK? Yes// \<RET\> (Yes)

Select HBPC Provider: \<RET\>

Beginning Report Date: 1/1/99 (JAN 01, 1999)

Ending Report Date: 12/31/99 (DEC 31, 1999)

DEVICE: HOME// (Enter a device that prints 132 column format)

\>\>\> HBPC Provider Census Report \<\<\< Page: 1

Provider: HBPCPROVIDER,THREE (150)

Run Date: MAR 28, 2000 Date Range: NOV 01, 1999 to

NOV 30, 1999

Patient Name SSN Date Street Address City ZIP Code Phone

===============================================================================================================

HBPCPATIENT,EIGHT 000-00-0008 11-03-99 187 NOWHERE ST CHICAGO 60612-3939 555-098-7654

---------------------------------------------------------------------------------------------------------------

HBPCPATIENT,TWO 000-00-0002 12-03-99 123 SYCAMORE AVE CHICAGO 60606 555-123-4567

---------------------------------------------------------------------------------------------------------------

....

Provider: XXXXXXXX,PROVIDER (150) Case Census Total: 10

==== End of Report ====

# Transmitting Data to Austin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options in this menu should be used in the order that they appear.

1.  Build/Verify Transmission File: Builds the file that will be transmitted and checks the data for completeness.
2.  Form Errors Report (80): Prints out any errors found by the Build/Verify Transmission File option.
3.  Edit Form Errors Data:
- Lets you correct admission or discharge errors by prompting for only what is missing and then deletes the Admission and Discharge Errors files.
- Deletes the Visit Error(s) and the Pseudo SSN Error(s) files.
4.  Transmit File to Austin: Transmits the data to Austin.
5.  Print Transmit History Report (80): Prints a copy of the transmission.

#### Transmission Options Flow

######## START

Transmission Menu …

## Build/Verify Transmission File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCFILE\]

Use this option to create the data file for transmission to Austin. All records with a "Needs to be Transmitted" value in the Transmit Status Flag field are processed. This includes all new or corrected Admission and Discharge records. It also scans for all Visit records within a selected Number of Visit Days to Scan.[^35]

Each run of this option updates the HBHC Visit file \#632 and the HBHC Transmit file \#634. If there are invalid records, it also populates the appropriate HBHC Visit Error(s) file \#634.2, the HBHC Evaluation/Admission Error(s) file \#634.1, the HBHC Discharge Error(s) file \#634.3, and/or the HBHC Pseudo SSN Error(s) file \#634.5. Errors found through the verification process can be viewed by printing the <u>Form Errors Report (80)</u>.

The software considers the following as incomplete:

- Visits without provider, diagnosis code(s), CPT code(s),
- Admission and discharge records with missing data, or
- Records with erroneous data.

The HBHC Transmit file \#634 continues to grow each time this option is run until the <u>Transmit File to Austin</u> option is performed. Once transmitted, the data remains in this file until the next time the Build/Verify Transmission File option is used. This preserves the intact transmit file in case re-transmission to Austin is necessary.

Messages

1.  If you receive the following message, the Build/Verify Transmission File or the automated Visit File Update option has run and errors were found. To view the errors that need correcting, run the option Form Errors Report.

> Records containing errors exist and must be corrected before transmit

> file can be created or updated.

2.  [^36]If the tasked job runs to completion and there are no errors, the HBH Mail Group will receive the following mail message:

> \[Date\] HBHC Build Transmit File is complete with no errors found.

> Number of Visit days to Scan system parameter: nn

> Date range: \[Date\] thru \[Date\]

> Start time: \[Time\] End time: \[Time\] Elapsed minutes: nn

> \*\*\*\*\* Reminder: Please run Transmit file to Austin option. \*\*\*\*\*

3.  If the tasked job runs to completion and there are errors, the HBH Mail Group will receive the following mail message:

> Subj: APR 10,2000 HBHC File Update \[#52110\] 10 Apr 00 15:29 1 line

> From: HBHC FILE UPDATE MAIL GROUP In 'IN' basket. Page 1

> -------------------------------------------------------------------------------

> Please run Form Errors Report option for HBHC errors to correct.

> **NOTE:** Set the Number of Visit Days to Scan to a large enough number to include the entire transmit batch date range. See the example below where the parameter was changed from 7 to 42 to include the entire month of March from the date it is run (April 10).

Example Build with No Errors

This option builds the file for transmission to Austin. Do you wish to

continue? No// Y (Yes)

Select one of the following:

1 January

2 February

3 March

4 April

5 May

6 June

7 July

8 August

9 September

10 October

11 November

12 December

Month for which data is to be transmitted: 3// \<RET\> March

[^37]Number of Visit Days to Scan: 7// 42

[^38]Build Transmit File processing has been queued. Task number: 192757

HBH Mail Message Following a Build without Errors

Subj: APR 10,2000 HBHC Build Transmit File \[#52111\] 10 Apr 00 15:34

9 lines

From: HBHC BUILD TRANSMIT FILE MAIL GROUP In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

APR 10,2000 HBHC Build Transmit File is complete with no errors found.

Number of Visit Days to Scan system parameter: 42

Date range: FEB 29,2000 thru MAR 31,2000

Start time: 15:34:32 End time: 15:34:32 Elapsed minutes: 0

\*\*\*\*\* Reminder: Please run Transmit File to Austin option. \*\*\*\*\*

Transmission Menu …

## Form Errors Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCRP1\]

This report is used to determine which patient records contain errors. The errors are found during the data verification process of the <u>Build/Verify Transmission File</u> option or following a run of the Auto-queue File Update of the HBHC Visit file. It is printed alphabetically by patient last name. A blank space is provided to the left of Patient Name to allow you to check off the patient's name as errors are corrected.

#### Correcting Errors

1.  For visit errors, use the Appointment Management option. Visits entered utilizing Progress Notes are also accessible in Appointment Management under Add/Edit. [^39]If other options besides Appointment Management or Progress Notes were used for entry of visit data, there may be instances where the visits do not show in Appointment Management. In this case, whatever package was used for entering the data must be used to correct the data.
2.  For errors in Evaluation/Admission and Discharge records, use the option <u>Edit Form Errors Data</u>. The Edit Form Errors Data option also deletes the Visit Error(s) and Pseudo SSN Error(s) files.
3.  After making all the corrections, run the Build/Verify Transmission File option. It should always be run after correcting the data and prior to transmitting to Austin.

<span id="p25_VI_7" class="anchor"></span>Note: The column header in various ICD Code reports is customized to match the type of ICD code that appears in the report. If the report only covers ICD-9 era dates, the column header is ICD9; if the report covers only ICD-10 era dates, the column header is ICD10; and if the report covers both ICD-9 and ICD-10 era dates, the column header is ICD.

Example:

<span id="screen2" class="anchor"></span>DEVICE: HOME// (Enter a printer name or press the \<RET\> key to print to your screen)

\>\>\> HBPC Form Errors Report \<\<\< Page: 1

Run Date: MAR 29, 2000

Patient Last

File IEN Patient Name Four Visit Clinic Name Date Form

===================================================================================

\`37 HBPCPATIENT1,THREE 0013 n/a MAR 06, 2000 E/Adm

-----------------------------------------------------------------------------------

\`98 HBPCPATIENT1,TWO 0012 n/a MAR 09, 2000 E/Adm

-----------------------------------------------------------------------------------

\`98 HBPCPATIENT1,TWO 0012 n/a MAR 09, 2000 D/C

-----------------------------------------------------------------------------------

\`58 HBPCPATIENT,EIGHT 0008 ASSESSMENT MAR 24, 2000@16:00 Visit

Error: Provider Missing

ICD9: \* 230.1 CA IN SITU ESOPHAGUS \* Primary Dx

--------------------------------------------------------------------------------

> **NOTE:** Please use Appointment Management to Correct Visit Errors. [^40]Run

Edit Form Errors Data option when corrections are complete.

==== End of Report ====

Transmission Menu …

## Edit Form Errors Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCUPD\]

Use this option to correct errors found during the data verification process of the <u>Build/Verify Transmission File</u> option. This option also deletes the following error files:

- HBHC Evaluation/Admission Error(s) (#634.1)
- HBHC Visit Error(s) (#634.2)
- HBHC Discharge Error(s) (#634.3)
- HBHC Pseudo SSN Error(s) (#634.5)
1.  If the error is on an E/Adm or D/C Form (see example on previous page), then this option should be used to correct the errors. Do not use the options Evaluation/Admission Data Entry or Discharge Data Entry to correct the errors. You are prompted for a patient, then the routine prompts for the fields that are missing or invalid in each record. These errors are found when either the Build Verify Transmission File \[HBHCFILE\] or the Auto-queue File Update \[HBHC AUTO-QUEUED FILE UPDATE\] option is run and must be corrected before transmission to Austin is allowed.
2.  If the error is on a Visit form, then use <u>Appointment Management</u> or other appropriate outpatient encounter package to correct the data. After correcting the visit errors, this option must be accessed to clean up the Visit Error(s) file.
3.  If you should get a message like the following, use the option <u>Pseudo Social Security Number Report (80)</u> to find out which patient has a pseudo SSN.

> Patient visit records with pseudo social security numbers (SSNs) exist.

> Print the 'Pseudo Social Security Number Report' located on the HBHC Reports Menu to obtain a list of patients with invalid SSNs. HBHC must determine what corrective action is appropriate to eliminate these records from the HBHC Information System.

Transmission Menu …

## Transmit File to Austin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[^41]\[HBHCXMT\] Locked with HBHC TRANSMIT key

This option creates and transmits the HBPC MailMan messages to Austin using the data in the HBHC Transmit file \#634. All errors found via the <u>Build/Verify Transmission File</u> option must be corrected before transmission to Austin is allowed. This option is locked with the HBHC TRANSMIT security key.

With each run of the Build/Verify Transmission File, data is added to the Transmit file until the Transmit File to Austin option is run. Once transmitted, the file remains unchanged until the next time the Build/Verify Transmission File option is used.

The Application Coordinator and any other user(s) in the HBH Mail Group will receive confirmation messages from Austin upon receipt of the electronic transmission by Austin. (See HBPC Technical Manual for mail group information.) In the event that no confirmation messages are received within 24 hours of a transmission request being queued, the Application Coordinator should contact their local IRM for assistance (e.g., domain could be closed, network traffic/troubles, hardware failure, etc.).

Multiple mail messages may be generated by the software package for each Austin transmission. Each MailMan message contains a maximum of 100 HBPC records to conform to Austin message size specifications. A corresponding confirmation message should be received for every MailMan message received by Austin. For example if 845 records need transmitting, 9 MailMan messages would be generated (8 messages containing 100 records each, plus 1 message containing 45 records) and 9 confirmation messages should be received.

The subject of the Austin confirmation MailMan message is LTE9999 HBH CONFIRMATION. Sample message text:

> Ref: Your HBH message \#9999999 with Austin ID \#99999999, is assigned confirmation number 999999999999999. (numbers vary on each message)

#### Transmission Messages

After selecting the option, one of the following messages will appear:

1\. Transmission request has been queued.

> This message indicates that all records are correct and complete and a background job to transmit the file to Austin has been initiated by the software package.

2\. Records containing errors exist and must be corrected before file can be transmitted.

The above message indicates all errors detected by the Build/Verify Transmission File option must be corrected before the user can proceed.

Transmission Menu …

## [^42]Print Transmit History Report (80)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHCR15A\]

To keep a record of transmissions, use this option to print the transmission history. You are prompted for a date from within the last 12 transmit batches and also to select the forms for inclusion on the report.

A Transmit History Report for the current transmission batch can be generated automatically from the Transmit File to Austin option if a default printer is defined in the System Parameters file \#631.9 (see <u>System Parameters Edit</u>). If no printer is defined, no report will be generated at transmit time.

#### Example

1\. APR 10, 2000

Select Transmit Date: 1// \<RET\>

Select one of the following:

3 Admission

4 Visit

5 Discharge

6 Correction

A All

S Summary

Select Forms to Include: Summary// \<RET\>

DEVICE: HOME// (Enter a printer)

\>\>\> HBPC APR 10, 2000 Transmit, Summary Report \<\<\< Page: 1

Run Date: APR 10, 2000

Summary

================================================================================

Admit Eval/Adm Form 3 Total: 22

Reject Eval/Adm Form 3 Total: 2

Visit Form 4 Total: 102

Discharge Form 5 Total: 19

Correction Form 6 Total: 0

-----

All Forms Total: 145

==== End of Report ====

*(This page included for two-sided copying.)*

# Medical Foster Home Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Medical Foster Home (MFH) is a special add-on that only works at sites that have received MFH sanction status approval from the Director of Home & Community-Based Care in the Office of Geriatrics and Extended Care, VA Central Office (VACO). Sites that do not have this sanction should not utilize the MFH portion of the Home Based Primary Care (HBHC) Information System software.

 NOTE: Medical Foster Home (MFH) sanction status approval is required prior to utilization of the MFH portion of the Home Based Primary Care (HBHC) Information System software.  The MFH functionality described in this chapter is dormant for sites without an approved MFH sanction status.  Approval is received from the Director of Home & Community-Based Care, in the Office of Geriatrics and Extended Care, VA Central Office (VACO).

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Medical Foster Home (MFH) combines adult foster care in a privately owned residence located in the community, with Home Based Primary Care (HBPC) or Spinal Cord Injury Home Care (SCI-HC). MFH offers a safe alternative to nursing home placement, merging personal care in a private home with medical & rehabilitation support from specialized VA home care programs. Veterans placed in MFH meet nursing home admission criteria. Payment of MFH charges is the responsibility of the veteran.

## MFH Basics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HBPC MFH patients will be a subset of HBPC patients
- Each MFH Admission will begin a new episode of care record
- MFH episode of care records are MFH specific
- HBPC/MFH records will be ‘combo’ record, representing both a HBPC & MFH patient
- Discharge (D/C) Date from 'HBPC only' episode & Admission Date of MFH combo record for same patient, should be same date, since D/C Date is not counted in Patient Days calculation
- HBHC System Parameter, Med Foster Home Sanction Date, will turn on MFH functionality within HBPC Information System software; indicates MFH site
- MFH ‘home specific’ data will be collected in separate file, HBHC Medical Foster Home (#633.2)
- MFH home specific data for capacity purposes, not software enforcement of data validation
- HBPC Evaluation/Admission Data Entry will prompt for Medical Foster Home Patient (Yes/No), & Medical Foster Home Name (MFH must already exist in MFH file)
- MFH Patient field = Yes will indicate MFH patient for report purposes
- Certain reports will be capable of printing MFH population separately from HBPC, as a subset; subset only indicates MFH Report; HBPC reports will include both HBPC & MFH patients, with MFH patient designation indicated (e.g. Program Census & Patient Days of Care reports)

## Using the Medical Foster Home (MFH) Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \[HBHC MFH MENU\]

Use of these options is discussed in the following pages:

Blank MFH Worksheet Report (80) \[HBHCBLNK\]

Demographic Data Entry for MFH \[HBHC MFH DEMOGRAPHIC INPUT\]

Inspection Data Entry for MFH \[HBHC MFH INSPECTION INPUT\]

Training Data Entry for MFH \[HBHC MFH TRAINING INPUT\]

Edit MFH Form Errors Data \[HBHCUPDM\]

MFH Reports ... \[HBHC MFH REPORTS MENU\]

MFH File Data Report (132) \[HBHCRP26\]

Worksheet for MFH (80) \[HBHCWORK\]

Inspection/Training Due Report for MFH (80) \[HBHCRP27\]

Rate Paid Report for MFH (80) \[HBHCRP28\]

License Due for MFH Report (80) \[HBHCRP29\]

Caregiver Age Report (132) \[HBHCRP30\]

Form Errors Report for MFH (80) \[HBHCRP31\]

Delimited Text File Output Menu for MFH ... \[HBHC MFH TEXT FILE OUTPUT

MENU\]

Inspection/Training Delimited Text File Output \[HBHCTXT2\]

Rate Paid Delimited Text File Output \[HBHCTXT\]

### Blank MFH Worksheet Report (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \[HBHCBLNK\]

This option prints the HBPC Medical Foster Home (MFH) Blank Worksheet Report. This worksheet will be used for collection of all MFH demographic data fields specific to the home. Report prints in 80 column format.

\>\>\> HBPC Medical Foster Home (MFH) Blank Worksheet Report \<\<\< Page: 1

Address: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

City: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

State Code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

County Code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ZIP Code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Phone Number: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Opened Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Primary Caregiver Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Caregiver Date of Birth: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Maximum Patients: 1 2 3 Bedbound Patient Maximum: 0 1 2

License Required: Yes No License Expiration Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Closure Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Voluntary Closure: Yes No

Nurse Inspection:

Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Social Work Inspection:

Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Dietitian Inspection:

Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Fire/Safety Inspection:

Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

==== End of Report ====

### Demographic Data Entry for MFH 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHC MFH DEMOGRAPHIC INPUT\]

This option allows data entry of Medical Foster Home (MFH) demographic fields in the HBHC Medical Foster Home file (#633.2). Once entered, the MFH Name field (#.01) is not editable via this option. Inspection & Training data are entered via separate options.

> **NOTE:** If this MFH is being edited and a transaction has been built for AITC, the following message will display (YES, must be entered to continue):

> Transmit Status Flag must be reset before editing this record is allowed.

> Do you wish to reset the Flag? No//

Sample data entry session:

Select Medical Foster Home (MFH) Menu Option: Demographic Data Entry for MFH

Select HBHC MEDICAL FOSTER HOME NAME: MFH TEST 7

Are you adding 'MFH TEST 7' as a new HBHC MEDICAL FOSTER HOME (the 7TH)? No// Y (Yes)

ADDRESS: Address

CITY: City

STATE CODE: ARKANSAS

COUNTY CODE: 119 PULASKI 119

ZIP CODE: 72205

PHONE NUMBER: (501) 555-1234

OPENED DATE: 1/1/08 (JAN 01, 2008)

PRIMARY CAREGIVER NAME: Caregiver,Primary

CAREGIVER DATE OF BIRTH: 1/10/50 (JAN 10, 1950)

MAXIMUM PATIENTS: 2

BEDBOUND PATIENT MAXIMUM: 1

LICENSE REQUIRED: N No

CLOSURE DATE: \<RET\>

A Parent Site is required for each Medical Foster Home.

If you exit without entering a Parent Site, this entry

will not be transmitted to Austin until a Parent Site

is defined. An HBHC Medical Foster Home Error will be

generated by the transmission record verification process.

PARENT SITE:

### Parent Site Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Parent Site defined for a Medical Foster Home must be predefined in the Systems Parameters Edit option. If only one parent site is defined in the Systems Parameters Edit option, that site will appear as a default for parent site in the Demographic Data Entry option for MFH.

If the parent site for a MFH is changed after the AITC transaction has been built, the following message will appear:

This Medical Foster Home has had an AITC transaction built with the former Parent Site. All patients in this Medical Foster Home need to be reviewed using Option Evaluation/Admission Data Entry.

If the following message appears, answer YES:

Transmit Status Flag must be reset before editing this record is allowed

Do you wish to reset the Flag?

If the message does not display, no further action is needed for this patient.

Press any key to continue:

### Inspection Data Entry for MFH 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#########  \[HBHC MFH INSPECTION INPUT\]

This option allows data entry of the Medical Foster Home (MFH) Inspection multiples in the HBHC Medical Foster Home file (#633.2). Inspection data collected includes: Date of Inspection & Name of person performing the inspection for each of the following disciplines: Nurse, Social Work, Dietitian, & Fire/Safety. Person must exist in the New Person file (#200).

Sample data entry session:

Select Medical Foster Home (MFH) Menu Option: Inspection Data Entry for MFH

Select HBHC MEDICAL FOSTER HOME NAME: MFH TEST 7

Select NURSE INSPECTION DATE: 1/3/08 JAN 03, 2008

Are you adding 'JAN 03, 2008' as a new NURSE INSPECTION DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

NURSE INSPECTION NAME: Inspector, Nurse

Select SOCIAL WORK INSPECTION DATE: 1/2/08 JAN 02, 2008

Are you adding 'JAN 02, 2008' as a new SOCIAL WORK INSPECTION DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

SOCIAL WORK INSPECTION NAME: Inspector, Social Work

Select DIETITIAN INSPECTION DATE: 1/4/08 JAN 04, 2008

Are you adding 'JAN 04, 2008' as a new DIETITIAN INSPECTION DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

DIETITIAN INSPECTION NAME: Inspector, Dietitian

Select FIRE/SAFETY INSPECTION DATE: 1/4/08 JAN 04, 2008

Are you adding 'JAN 04, 2008' as a new FIRE/SAFETY INSPECTION DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

FIRE/SAFETY INSPECTION NAME: Inspector, Fire

### Training Data Entry for MFH 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHC MFH TRAINING INPUT\]

This option allows data entry of the Medical Foster Home (MFH) Training multiples in the HBHC Medical Foster Home file (#633.2). Training data collected includes: Date of Training. Training is tracked for each of the following categories: Home Operation, Fire/Safety, Medication Management, Personal Care, Infection Control, End of Life Issues, & Other. The Other category also prompts for Topic.

Sample data entry session:

Select Medical Foster Home (MFH) Menu Option: Training Data Entry for MFH

Select HBHC MEDICAL FOSTER HOME NAME: MFH TEST 7

Select HOME OPERATION TRAINING DATE: 1/2/08 JAN 02, 2008

Are you adding 'JAN 02, 2008' as a new HOME OPERATION TRAINING DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

Select FIRE/SAFETY TRAINING DATE: 1/4/08 JAN 04, 2008

Are you adding 'JAN 04, 2008' as a new FIRE/SAFETY TRAINING DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

Select MEDICATION MANAGEMENT TRN DATE: 1/2/08 JAN 02, 2008

Are you adding 'JAN 02, 2008' as a new MEDICATION MANAGEMENT TRN DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

Select PERSONAL CARE TRAINING DATE: 1/2/08 JAN 02, 2008

Are you adding 'JAN 02, 2008' as a new PERSONAL CARE TRAINING DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

Select INFECTION CONTROL TRAIN DATE: 1/2/08 JAN 02, 2008

Are you adding 'JAN 02, 2008' as a new INFECTION CONTROL TRAIN DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

Select END OF LIFE ISSUES TRAIN DATE: 1/2/08 JAN 02, 2008

Are you adding 'JAN 02, 2008' as a new END OF LIFE ISSUES TRAIN DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

Select OTHER TRAINING DATE: 1/3/08 JAN 03, 2008

Are you adding 'JAN 03, 2008' as a new OTHER TRAINING DATE (the 1ST for this HBHC MEDICAL FOSTER HOME)? No// Y (Yes)

TOPIC: Topic 1

### Edit MFH Form Errors Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCUPDM\]

This option allows editing of the HBPC Medical Foster Home (MFH) Form Errors Data. The user is prompted for a MFH name listed on the Form Errors Report for MFH (80) \[HBHCRP31\], then the software prompts only for the fields that are missing or invalid in each record. These errors are found when the Build/Verify Transmission File \[HBHCFILE\] option is run and must be corrected before transmission to Austin is allowed. The MFH Form Errors also appear on the HBPC Form Errors Report (80) \[HBHCRP1\].

Sample data entry session:

Select HBHC MEDICAL FOSTER HOME NAME: MFH TEST 25

=== Editing Medical Foster Home (MFH) Demographic data ===

CAREGIVER DATE OF BIRTH: 4/8/60 (APR 08, 1960)

LICENSE REQUIRED: N No

## MFH Reports ... 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHC MFH REPORTS MENU\]

The MFH Reports Menu contains the following options:

MFH File Data Report (132) \[HBHCRP26\]

Worksheet for MFH (80) \[HBHCWORK\]

Inspection/Training Due Report for MFH (80) \[HBHCRP27\]

Rate Paid Report for MFH (80) \[HBHCRP28\]

License Due for MFH Report (80) \[HBHCRP29\]

Caregiver Age Report (132) \[HBHCRP30\]

Form Errors Report for MFH (80) \[HBHCRP31\]

Delimited Text File Output Menu for MFH ... \[HBHC MFH TEXT FILE OUTPUT MENU\]

Inspection/Training Delimited Text File Output \[HBHCTXT2\]

Rate Paid Delimited Text File Output \[HBHCTXT\]

### MFH File Data Report (132) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCRP26\]

This option prints the HBHC Medical Foster Home (MFH) file (#633.2) report. The report is sorted alphabetically by Medical Foster Home Name & includes: Medical Foster Home Name, Opened Date, Primary Caregiver Name, Maximum Patients, Bedbound Patient Maximum, Closure Date, & Voluntary Closure. Report prints in 132 column format.

> **NOTE:** this report prints in 132 column format; format slightly altered to fit page

\>\>\> HBPC Medical Foster Home (MFH) File Data Report \<\<\< Page: 1

Run Date: JAN 09, 2008

Opened Primary Max Bed Closure Voluntary

MFH Name Date Caregiver Name Pts Pts Date Closure

======================================================================================

MFH TEST 1 01-01-00 Hbhcaregiver, One 3 1 04-30-05 Yes

--------------------------------------------------------------------------------------

MFH TEST 2 06-01-01 Hbhcaregiver, Two 2 0

--------------------------------------------------------------------------------------

MFH TEST 3 03-31-02 Hbhcaregiver, Three 3 2

--------------------------------------------------------------------------------------

MFH TEST 4 04-14-05 Hbhcaregiver, Four 3 0

--------------------------------------------------------------------------------------

MFH TEST 5 01-01-00 Hbhcaregiver, Five 3 1 04-30-07 Yes

--------------------------------------------------------------------------------------

MFH TEST 6 03-10-02 Hbhcaregiver, Six 2 0

--------------------------------------------------------------------------------------

MFH TEST 7 01-02-08 Hbhcaregiver, Seven 2 1

--------------------------------------------------------------------------------------

======================================================================================

Maximum Patients Total: 18

Bedbound Maximum Total: 5

Medical Foster Home (MFH) Total: 7

======================================================================================

==== End of Report ====

### Worksheet for MFH (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCWORK\]

This option prints the Medical Foster Home (MFH) Data Entry Worksheet. MFH must exist in HBHC Medical Foster Home file (633.2). Any data already on file will be printed on the report. A line of underscores will be printed when no data exists for a specific field. Worksheet prints in 80 column format.

\>\>\> HBPC Medical Foster Home (MFH) Worksheet Report \<\<\< Page: 1

Run Date: AUG 28, 2008

MFH Name: MFH TEST

==========================================================================

Address: Address

City: City

State Code: ARKANSAS

County Code: PULASKI (119)

ZIP Code: 72205

Phone Number: (501) 555-1234

Opened Date: JAN 01, 2008

Primary Caregiver Name: Caregiver, Primary

Caregiver Date of Birth: JAN 01, 1950

Maximum Patients: 3 Bedbound Patient Maximum: 0

License Required: Yes License Expiration Date: JUL 31, 2008

Closure Date: AUG 01, 2008 Voluntary Closure: No

Nurse Inspection:

Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Inspection(s):

Social Work Inspection:

Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Inspection(s):

Dietitian Inspection:

Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Inspection(s):

Fire/Safety Inspection:

Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Inspection(s):

Home Operation Training Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Training Date(s):

Fire/Safety Training Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Training Date(s):

Medication Management Training Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Training Date(s):

Personal Care Training Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Training Date(s):

Infection Control Training Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Training Date(s):

End of Life Issues Training Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Training Date(s):

Other Training Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topic: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previous Training Date(s):

==== End of Report ====

### Inspection/Training Due Report for MFH (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCRP27\]

This option prints the HBPC Medical Foster Home (MFH) Inspection or Training report. Inspection & Training data are multiples within the HBHC MEDICAL FOSTER HOME file (#633.2). The data includes inspections/training due within the next 6 months, based on month only. Report includes: inspections/training due & most recent inspection/training date. Report prints in 80 column format.

\>\>\> HBPC Medical Foster Home (MFH) Inspection(s) Due Report \<\<\< Page: 1

Run Date: AUG 10, 2007

===============================================================

No MFH inspections currently due.

==== End of Report ====

\>\>\> HBPC Medical Foster Home (MFH) Training Due Report \<\<\< Page: 1

Run Date: MAY 07, 2008

===============================================================

Home Operation Training Due in next 6 months:

Medical Foster Home Name Most Recent Home Operation Training Date

MFH TESTING AGAIN OCT 01, 2007

Fire/Safety Training Due in next 6 months:

Medical Foster Home Name Most Recent Fire/Safety Training Date

MFH TESTING AGAIN OCT 01, 2007

Medication Management Training Due in next 6 months:

Medical Foster Home Name Most Recent Medication Management Training

Date

MFH TESTING AGAIN OCT 01, 2007

Personal Care Training Due in next 6 months:

Medical Foster Home Name Most Recent Personal Care Training Date

MFH TESTING AGAIN OCT 01, 2007

Infection Control Training Due in next 6 months:

Medical Foster Home Name Most Recent Infection Control Training Date

MFH TESTING AGAIN OCT 01, 2007

End of Life Training Due in next 6 months:

Medical Foster Home Name Most Recent End of Life Training Date

MFH TESTING AGAIN OCT 01, 2007

Other Training Due in next 6 months:

Medical Foster Home Name Most Recent Other Training Date

MFH TESTING AGAIN OCT 01, 2007

==== End of Report ====

### Rate Paid Report for MFH (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCRP28\]

This option prints the HBPC Medical Foster Home (MFH) Rate Paid report. Rate Paid data is a multiple in the HBHC PATIENT file (#631). The user selects to sort the data by Patient or MFH, then to include Active ONLY, Individual, or All Patients or MFHs, then whether to include Current ONLY Rate or All Rates Paid. MFH sort also prompts for whether to include Discharged Patients. Report includes: Patient Name, Last Four, Rate Paid, Start Date, & Medical Foster Home Name. Report selection criteria is listed in the report header. Lowest, Highest, & Average Rate Paid are included at the end of the report. Report prints in 80 column format. Note that output can also be to delimited file format appropriate for spreadsheet import.

Samples of Rate Paid selection criteria prompts:

Sort by Patient or Medical Foster Home (MFH): (P/M): Patient

Include: Active ONLY, Individual, or All Patient(s): (O/I/A): O Active ONLY

Include: Current Rate, or All Rates Paid: (C/A): Current Rate

Format: Report, or File (Delimited): (R/F): Report Format

DEVICE: \<RET\>

Sort by Patient or Medical Foster Home (MFH): (P/M): Medical Foster Home (MFH)

Include: Active ONLY, Individual, or All MFH(s): (O/I/A): All

Include: Discharged Patients: (Y/N): Yes

Include: Current Rate, or All Rates Paid: (C/A): All Rates Paid

Format: Report, or File (Delimited): (R/F): Report Format

DEVICE: \<RET\>

Sort by Patient or Medical Foster Home (MFH): (P/M): Patient

Include: Active ONLY, Individual, or All Patient(s): (O/I/A): Individual

Include: Current Rate, or All Rates Paid: (C/A): Current Rate

Select HBHC PATIENT NAME: \`2300 HBHCPatient, Six 10-04-06 7-17-51 101227245 YES SC VETERAN FIRM A

Select HBHC PATIENT NAME: \<RET\>

Format: Report, or File (Delimited): (R/F): Report Format

DEVICE: \<RET\>

\>\>\> HBPC Medical Foster Home (MFH) Rate Paid Report \<\<\< Page: 1

Selected Criteria: All MFH(s) Current Rate Paid Include D/C Pts

Run Date: NOV 09, 2007

Last Rate Start

Medical Foster Home (MFH) Name Patient Name Four Paid Date

===============================================================================

MFH TEST 1 HBHCPATIENT,FIVE 7245 1800.00 01-01-07

-------------------------------------------------------------------------------

MFH TEST 2 HBHCPATIENT,SIX 0837 2500.00 08-10-07

-------------------------------------------------------------------------------

MFH TEST 3 HBHCPATIENT,SEVEN 1849 2400.00 11-01-07

-------------------------------------------------------------------------------

MFH TEST 3 HBHCPATIENT,EIGHT 0539 2000.00 02-01-07

-------------------------------------------------------------------------------

MFH TEST 4 HBHCPATINET,NINE 8674 2200.00 03-01-07

-------------------------------------------------------------------------------

===============================================================================

Lowest Rate: 1800.00 Highest Rate: 2500.00 Average Rate: 2180.00

===============================================================================

==== End of Report ====

\>\>\> HBPC Medical Foster Home (MFH) Rate Paid Report \<\<\< Page: 1

Selected Criteria: All Patient(s) All Rates Paid

Run Date: NOV 09, 2007

Last Rate Start

Patient Name Four Paid Date Medical Foster Home

===============================================================================

HBHCPATIENT,FIVE 7245 1800.00 01-01-07 MFH TEST 1

-------------------------------------------------------------------------------

HBHCPATIENT,SIX 0837 1200.00 06-10-07 MFH TEST 2

HBHCPATIENT,SIX 0837 2500.00 08-10-07 MFH TEST 2

-------------------------------------------------------------------------------

HBHCPATIENT,SEVEN 1849 2400.00 11-01-07 MFH TEST 3

-------------------------------------------------------------------------------

HBHCPATIENT,EIGHT 8674 2200.00 03-01-07 MFH TEST 4

-------------------------------------------------------------------------------

HBHCPATIENT,NINE 0539 2000.00 02-01-07 MFH TEST 3

-------------------------------------------------------------------------------

===============================================================================

Lowest Rate: 1200.00 Highest Rate: 2500.00 Average Rate: 2016.67

===============================================================================

==== End of Report ====

### License Due for MFH Report (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCRP29\]

This option prints the HBPC Medical Foster Home (MFH) License Due report. The report is sorted alphabetically by MFH Name & contains MFH Name & License Expiration Date. The report includes License Expiration Dates due to expire within 6 months, based on month only. The report prints in 80 column format.

\>\>\> HBPC Medical Foster Home (MFH) License Due Report \<\<\< Page: 1

Run Date: JAN 08, 2008

Medical Foster Home Name License Expiration Date

===============================================================================

MFH TEST 2 06-01-2008

MFH TEST 4 03-31-2008

==== End of Report ====

### Caregiver Age Report (132) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCRP30\]

This option prints the HBPC Medical Foster Home (MFH) Caregiver Age Report. The report is sorted alphabetically by MFH Name & includes: Medical Foster Home (MFH) Name, Opened Date, Primary Caregiver Name, Caregiver Date of Birth, & Age. Total number of MFHs & Average Caregiver Age are included at the end of the report. Report prints in 132 column format.

> **NOTE:** this report prints in 132 column format; format slightly altered to fit page

\>\>\> HBPC Medical Foster Home (MFH) Caregiver Age Report \<\<\< Page: 1

Run Date: MAR 05, 2008

MFH Name Opened Date Primary Caregiver Name Date of Birth Age

===============================================================================

MFH TEXT 7 10-03-07 HBHCCAREGIVER,ONE 02-04-33 75

-------------------------------------------------------------------------------

OLD FOLKS HOME 01-11-08 HBHCCAREGIVER,TWO 01-01-80 28

-------------------------------------------------------------------------------

MFH TEST 25 06-01-04 HBHCCAREGIVER,THREE 04-08-60 47

-------------------------------------------------------------------------------

MFH TEST 48 01-12-08 HBHCCAREGIVER,FOUR 02-20-50 58

-------------------------------------------------------------------------------

MFH TESTING 01-02-08 HBHCCAREGIVER,FIVE 01-01-87 21

-------------------------------------------------------------------------------

===============================================================================

Medical Foster Home (MFH) Total: 5

Average Caregiver Age: 45.8

===============================================================================

==== End of Report ====

### Form Errors Report for MFH (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCRP31\]

This option prints the HBHC Medical Foster Home (MFH) Form Errors Report for MFH option. The report is sorted alphabetically by MFH Name & includes: MFH File (#633.2) Internal Entry Number (IEN), MFH Name, & Opened Date. This option is both freestanding & is called from Form Errors Report \[HBHCRP1\] option. Report prints in 80 column format.

\>\>\> HBPC Medical Foster Home (MFH) Form Errors Report \<\<\< Page: 1

Run Date: MAR 04, 2008

MFH File IEN Medical Foster Home Name Opened Date

===============================================================================

\`6 MFH TESTING RESUMED

-------------------------------------------------------------------------------

\`7 MFH TESTING TOO 03-03-08

-------------------------------------------------------------------------------

==== End of Report ====

### Delimited Text File Output Menu for MFH ... 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHC MFH TEXT FILE OUTPUT MENU\]

The Delimited Text File Output Menu for MFH contains the following options:

Inspection/Training Delimited Text File Output \[HBHCTXT2\]

Rate Paid Delimited Text File Output \[HBHCTXT\]

### Inspection/Training Delimited Text File Output 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCTXT2\]

This option creates the HBPC Medical Foster Home (MFH) Inspection or Training data delimited text file, suitable for spreadsheet import. Inspection & Training data are multiples in the HBHC MEDICAL FOSTER HOME file (#633.2). Inspection multiples include: Nurse, Social Work, Dietitian, & Fire/Safety Inspections. Training multiples include: Home Operation, Fire/Safety, Medication Management, Personal Care, Infection Control, End of Life, & Other as training categories. Other training category also contains Topic field. File is delimited by "^".

Sample of Inspection delimited file data:

Medical Foster Home Name^MFH Closure Date^Inspection Discipline^Inspection Date^Inspector Name

MFH TEST 1^04-30-2005^Nurse^01-01-2007^INSPECTOR, NURSE

MFH TEST 1^04-30-2005^Social Work^02-01-2006^INSPECTOR, SOCIAL WORK

MFH TEST 1^04-30-2005^Dietitian^05-01-2006^INSPECTOR, DIETITIAN

MFH TEST 1^04-30-2005^Fire-Safety^03-01-2006^INSPECTOR, FIRE

MFH TEST 2^^Nurse^03-10-2006^INSPECTOR, NURSE

MFH TEST 2^^Nurse^11-01-2006^INSPECTOR, NURSE

MFH TEST 2^^Social Work^03-12-2006^INSPECTOR, SOCIAL WORK

MFH TEST 2^^Social Work^11-02-2006^INSPECTOR, SOCIAL WORK

MFH TEST 2^^Dietitian^03-14-2006^INSPECTOR, DIETITIAN

MFH TEST 2^^Dietitian^11-03-2006^INSPECTOR, DIETITIAN

MFH TEST 2^^Fire-Safety^03-30-2006^INSPECTOR, FIRE

MFH TEST 2^^Fire-Safety^11-04-2005^INSPECTOR, FIRE

MFH TEST 3^^Nurse^02-01-2002^INSPECTOR, NURSE

MFH TEST 3^^Nurse^02-01-2006^INSPECTOR, NURSE

MFH TEST 3^^Social Work^02-10-2002^INSPECTOR, SOCIAL WORK

MFH TEST 3^^Dietitian^02-20-2002^INSPECTOR, DIETITIAN

MFH TEST 3^^Dietitian^02-20-2004^INSPECTOR, DIETITIAN

MFH TEST 3^^Fire-Safety^02-28-2002^INSPECTOR, FIRE

MFH TEST 4^^Nurse^05-01-2005^INSPECTOR, NURSE

MFH TEST 4^^Nurse^05-02-2006^INSPECTOR, NURSE

MFH TEST 4^^Nurse^05-10-2007^INSPECTOR, NURSE

MFH TEST 4^^Social Work^05-02-2005^INSPECTOR, SOCIAL WORK

MFH TEST 4^^Social Work^05-03-2006^INSPECTOR, SOCIAL WORK

MFH TEST 4^^Social Work^05-04-2007^INSPECTOR, SOCIAL WORK

MFH TEST 4^^Dietitian^05-03-2005^INSPECTOR, DIETITIAN

MFH TEST 4^^Dietitian^05-04-2006^INSPECTOR, DIETITIAN

MFH TEST 4^^Fire-Safety^05-04-2005^INSPECTOR, FIRE

MFH TEST 4^^Fire-Safety^05-05-2006^INSPECTOR, FIRE

MFH TEST 5^04-30-2007^Nurse^06-01-2006^INSPECTOR, NURSE

MFH TEST 5^04-30-2007^Nurse^06-01-2007^INSPECTOR, NURSE

MFH TEST 5^04-30-2007^Social Work^07-10-2006^INSPECTOR, SOCIAL WORK

MFH TEST 5^04-30-2007^Dietitian^08-14-2006^INSPECTOR, DIETITIAN

MFH TEST 5^04-30-2007^Dietitian^08-14-2005^INSPECTOR, DIETITIAN

MFH TEST 5^04-30-2007^Fire-Safety^09-10-2006^INSPECTOR, FIRE

MFH TEST 6^^Nurse^11-20-2006^INSPECTOR, NURSE

MFH TEST 6^^Social Work^12-02-2006^INSPECTOR, SOCIAL WORK

MFH TEST 6^^Dietitian^01-16-2007^INSPECTOR, DIETITIAN

MFH TEST 6^^Fire-Safety^02-09-2007^INSPECTOR, FIRE

Sample of Training delimited file data:

Medical Foster Home Name^MFH Closure Date^Training Category^Training Date^Other Training Topic

MFH TEST 2^^Home Operation^02-02-2006

MFH TEST 2^^Fire-Safety^02-04-2006

MFH TEST 2^^Medication Management^02-20-2006

MFH TEST 2^^Personal Care^03-01-2006

MFH TEST 2^^Infection Control^04-01-2006

MFH TEST 2^^Infection Control^06-10-2007

MFH TEST 2^^End of Life^04-10-2006

MFH TEST 2^^Other^01-15-2006^Topic 1

MFH TEST 2^^Other^07-15-2007^Topic n

MFH TEST 3^^Home Operation^03-01-2002

MFH TEST 3^^Home Operation^09-01-2002

MFH TEST 3^^Fire-Safety^03-02-2002

MFH TEST 3^^Fire-Safety^09-02-2002

MFH TEST 3^^Medication Management^03-03-2002

MFH TEST 3^^Medication Management^09-03-2002

MFH TEST 3^^Medication Management^07-01-2007

MFH TEST 3^^Personal Care^03-04-2002

MFH TEST 3^^Personal Care^09-04-2002

MFH TEST 3^^Infection Control^03-05-2002

MFH TEST 3^^Infection Control^09-05-2002

MFH TEST 3^^End of Life^03-06-2002

MFH TEST 3^^End of Life^09-06-2002

MFH TEST 3^^Other^03-07-2002

MFH TEST 3^^Other^09-07-2002

MFH TEST 4^^Home Operation^05-01-2005

MFH TEST 4^^Home Operation^05-02-2006

MFH TEST 4^^Fire-Safety^05-02-2005

MFH TEST 4^^Medication Management^05-03-2005

MFH TEST 4^^Medication Management^05-08-2007

MFH TEST 4^^Personal Care^05-04-2005

MFH TEST 4^^Personal Care^05-15-2007

MFH TEST 4^^Infection Control^05-06-2005

MFH TEST 4^^End of Life^05-07-2005

MFH TEST 4^^Other^05-08-2005^Topic

MFH TEST 4^^Other^06-01-2007^Topic2

MFH TEST 5^04-30-2007^Infection Control^01-01-2007

### Rate Paid Delimited Text File Output 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCTXT\]

This option creates the HBPC Medical Foster Home (MFH) Rate Paid delimited text file,

suitable for spreadsheet import. Rate Paid data is a multiple in the HBHC PATIENT file

(#631). The user selects to sort the data by Patient or MFH, then to include Active ONLY, Individual, or All Patients or MFHs, then whether to include Current ONLY Rate or All Rates Paid. File includes: Patient Name, Last Four, Rate Paid, Start Date, for Patient sort, plus Medical Foster Home Name is included on MFH sort. MFH sort also prompts for whether to include Discharged Patients. File is delimited by "^".

Sample of Rate Paid selection criteria prompts:

Sort by Patient or Medical Foster Home (MFH): (P/M): Patient

Include: Active ONLY, Individual, or All Patient(s): (O/I/A): All

Include: Current Rate, or All Rates Paid: (C/A): All Rates Paid

DEVICE: \<RET\>

Sample delimited Rate Paid data based on the above selection criteria:

Patient Name^Last Four^Rate Paid^Start Date

CULPAHDFE,WUHTSXY IHYYDT^7245^1800^01-01-2007

DLQDT,AHXY^0837^1200^06-10-2007

DLQDT,AHXY^0837^2500^08-10-2007

FAXPHUT,UXKHUS A^1849^2400^11-01-2007

KDYF,LAGUHI C^8674^2200^03-01-2007

OIXZ,JADGGXUI C^0539^2000^02-01-2007

Sample of Rate Paid selection criteria prompts:

Sort by Patient or Medical Foster Home (MFH): (P/M): M Medical Foster Home (MFH)

Include: Active ONLY, Individual, or All MFH(s): (O/I/A): M All

Include: Current Rate, or All Rates Paid: (C/A): M All Rates Paid

Include: Discharged Patients: (Y/N): Y Yes

DEVICE: \<RET\>

Sample delimited Rate Paid data based on the above selection criteria:

Patient Name^Last Four^Rate Paid^Start Date^Medical Foster Home (MFH) Name

CULPAHDFE,WUHTSXY IHYYDT^7245^1800^01-01-2007^MFH TEST 1

DLQDT,AHXY^0837^1200^06-10-2007^MFH TEST 2

DLQDT,AHXY^0837^2500^08-10-2007^MFH TEST 2

FAXPHUT,UXKHUS A^1849^2400^11-01-2007^MFH TEST 3

OIXZ,JADGGXUI C^0539^2000^02-01-2007^MFH TEST 3

KDYF,LAGUHI C^8674^2200^03-01-2007^MFH TEST 4

## Queued Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto-queued Inspection/Training Reminder e-mail 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHC MFH AUTO-QUEUED REMINDERS\]

This option runs a monthly auto-queued batch job to create separate e-mail reminder messages for HBPC Medical Foster Home (MFH) Inspections &/or Training due within the next 3 months, based on month only. This job should be scheduled for the 1st day of each month, regardless of day of the week for 1st.

The MFH Inspection & Training data used by this option are multiples within the HBHC

MEDICAL FOSTER HOME file (#633.2).

Members in mail group HBHC MEDICAL FOSTER HOME receive the reminder mail messages.

Sample Inspection Due e-mails:

Subj: AUG 30, 2007 MFH Inspection Due Reminder \[#270\] 08/30/07@17:38 2 lines

From: \<"HBHC MFH INSPECTION REMINDER MAIL GROUP In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Nurse Inspection(s) Due in next 3 months:

Medical Foster Home Name Most Recent Nurse Inspection Date

MFH TEST 3 FEB 01, 2006

MFH TEST 4 MAY 02, 2006

Social Work Inspection(s) Due in next 3 months:

Medical Foster Home Name Most Recent Social Work Inspection Date

MFH TEST 3 FEB 10, 2002

MFH TEST 4 MAY 03, 2006

Dietitian Inspection(s) Due in next 3 months:

Medical Foster Home Name Most Recent Dietitian Inspection Date

MFH TEST 3 FEB 20, 2004

MFH TEST 4 MAY 04, 2006

Fire/Safety Inspection(s) Due in next 3 months:

Medical Foster Home Name Most Recent Fire/Safety Inspection Date

MFH TEST 3 FEB 28, 2002

MFH TEST 2 MAR 30, 2006

MFH TEST 4 MAY 05, 2006

Subj: AUG 30, 2007 MFH Inspection Due Reminder \[#270\] 08/30/07@17:38 2 lines

From: \<"HBHC MFH INSPECTION REMINDER MAIL GROUP In 'IN' basket. Page 1

-------------------------------------------------------------------------------

No MFH Inspection currently due.

Sample Training Due e-mail:

Subj: SEP 05, 2007 MFH Training Due Reminder \[#499\] 09/05/07@00:05:02 48 lines

From: \<"HBHC MFH TRAINING REMINDER MAIL GROUP In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Home Operation Training Due in next 3 months:

Medical Foster Home Name Most Recent Home Operation Training Date

MFH TEST 3 SEP 01, 2002

MFH TEST 2 FEB 02, 2006

MFH TEST 4 MAY 02, 2006

Fire/Safety Training Due in next 3 months:

Medical Foster Home Name Most Recent Fire/Safety Training Date

MFH TEST 3 SEP 02, 2002

MFH TEST 4 MAY 02, 2005

MFH TEST 2 FEB 04, 2006

Medication Management Training Due in next 3 months:

Medical Foster Home Name Most Recent Med Mgmt Training Date

MFH TEST 2 FEB 20, 2006

Personal Care Training Due in next 3 months:

Medical Foster Home Name Most Recent Personal Care Training Date

MFH TEST 3 SEP 04, 2002

MFH TEST 2 MAR 01, 2006

Infection Control Training Due in next 3 months:

Medical Foster Home Name Most Recent Infect Control Training Date

MFH TEST 3 SEP 05, 2002

MFH TEST 4 MAY 06, 2005

End of Life Training Due in next 3 months:

Medical Foster Home Name Most Recent End of Life Training Date

MFH TEST 3 SEP 06, 2002

MFH TEST 4 MAY 07, 2005

MFH TEST 2 APR 10, 2006

Other Training Due in next 3 months:

Medical Foster Home Name Most Recent Other Training Date

MFH TEST 3 SEP 07, 2002

### Auto-queued License Due Reminder e-mail 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHC MFH AUTO-Q LICENSE DUE\]

This option runs a monthly auto-queued batch job to create an e-mail message for HBPC

Medical Foster Home(s) (MFH) with License due within the next 3 months, based on month only. This job should be scheduled for the 1st day of each month, regardless of day of the week for 1st.

> **NOTE:** This option does NOT need to be scheduled to run for HBPC MFH sites which are

in states that do not require licensure.

The MFH License data used by this option resides in the HBHC MEDICAL FOSTER HOME file (#633.2).

Members in mail group HBHC MEDICAL FOSTER HOME receive the reminder mail message.

Subj: JAN 08, 2008 MFH License Due Reminder \[#933\] 01/08/08@17:30 3 lines

From: HBHC MFH LICENSE REMINDER MAIL GROUP In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Medical Foster Home Name License Expiration Date

MFH TEST 4 03-31-2008

=====================================================================

> **NOTE:** The MFH functionality is dormant on the following option for sites without an approved MFH sanction status.

Use of this option is discussed in the following pages:

Under HBPC Information System Menu ... \[HBHC INFORMATION SYSTEM MENU\]

Evaluation/Admission Data Entry \[HBHCADM\]

### Evaluation/Admission Data Entry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCADM\]

This option allows entering/editing of the evaluation/admission data in the HBHC Patient

File (#631).

If a site has a sanctioned MFH program, then the user is also prompted as in the sample below. The MFH functionality is dormant on this option for sites without an approved MFH sanction status.

> **NOTE:** A MFH patient admission always begins a new episode of care. If the patient was a current HBPC patient at the time of admission to MFH, then patient is discharged from the previous HBPC episode of care and a new episode is created for the MFH admission. This is to identify the admission date of when the patient became a MFH patient.

Please refer to the Evaluation/Admission Data Entry chapter for complete instructions for this option. This portion only covers the additional MFH prompts.

Select HBPC Information System Menu Little Rock VAMC Option: Evaluation/

Admission Data Entry

Select HBHC PATIENT NAME: MFHPATIENT, FOUR 11-2-31 66618604 2 NO NSC VETERAN

Enrollment Priority: GROUP 5 Category: ENROLLED End Date:

Are you adding 'MFHPATIENT, FOUR' as a new HBHC PATIENT (the 2527TH)? No// Y

(Yes)

HBHC PATIENT DATE: T (SEP 24, 2008)

MEDICAL FOSTER HOME PATIENT: Y Yes

MEDICAL FOSTER HOME NAME: MFH TEST

Select RATE PAID START DATE: T SEP 24, 2008

Are you adding 'SEP 24, 2008' as

a new RATE PAID START DATE (the 1ST for this HBHC PATIENT)? No// Y (Yes)

RATE PAID AMOUNT: 2200

DATE: SEP 24,2008// \<Enter\>

. . . (Starting with this prompt, this is the same as the Evaluation/Admission Data Entry form without MFH.)

> **NOTE:** The MFH functionality is dormant on the following options for sites without an approved MFH sanction status.

Use of these options is discussed in the following pages:

Under HBPC Reports Menu ... \[HBHC REPORTS MENU\]

...

Patient Days of Care by Date Range Report (80) \[HBHCRP23\]

Census Reports Menu ... \[HBHC CENSUS REPORTS MENU\]

Program Census Report (80) \[HBHCRP10\]

### Patient Days of Care by Date Range Report (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCRP23\]

The option prints HBPC Patient Days of Care by Date Range Report. Report includes: file internal entry number (IEN), Patient Name, Last Four, Date, Discharge Date, & Patient Days. Patient Days is calculated based on the user selectable date range. Summary totals of Patients and Patient Days are included for both Complete Episodes of Care and Active Cases. Date of Discharge is omitted from the Patient Days total (e.g. Adm Date: 7/1/03, D/C Date: 7/5/03 would total 4 Patient Days, not 5). Report prints in 80 column format.

This report requires the beginning date to be the oldest current active Admission on file, or an arbitrary date such as 1/1/85, to obtain the complete active census.

User is prompted to select HBPC or MFH report. HBPC report includes all HBPC patients in the user selected date range, with MFH patients indicated by having their MFH listed. MFH report includes only MFH patients in the user selected date range. Below are samples of both HBPC & MFH reports, with patient specific data omitted.

> **NOTE:** The MFH functionality is dormant on this report for sites without an approved MFH sanction status.

HBPC report (patient data omitted):

\>\>\> HBPC Patient Days of Care by Date Range Report \<\<\< Page: 1

Run Date: JAN 09, 2008 Date Range: JAN 01, 1985 to

JAN 09, 2008

Last Discharge Patient

IEN Patient Name Four Date Date Days MFH

===============================================================================

. . .

\>\>\> HBPC Patient Days of Care by Date Range Report \<\<\< Page: 329

Run Date: JAN 09, 2008 Date Range: JAN 01, 1985 to

JAN 09, 2008

Last Discharge Patient

IEN Patient Name Four Date Date Days MFH

===============================================================================

. . .

===============================================================================

\>\>\> Date Range: JAN 01, 1985 to JAN 09, 2008 \<\<\<

Total Active Patients: 137

===============================================================================

Complete Episodes of Care Only:

Total Patients: 1,828 Total Patient Days in Date Range: 741,663

===============================================================================

Total Patients: 1,965 Total Patient Days in Date Range: 892,358

===============================================================================

==== End of Report ====

MFH Report (patient data omitted):

\>\>\> HBPC MFH Patient Days of Care by Date Range Report \<\<\< Page: 1

Run Date: JAN 09, 2008 Date Range: JAN 01, 1985 to

JAN 09, 2008

Last Discharge Patient

IEN Patient Name Four Date Date Days MFH

===============================================================================

. . .

===============================================================================

\>\>\> Date Range: JAN 01, 1985 to JAN 09, 2008 \<\<\<

===============================================================================

Total Active Patients: 3

===============================================================================

Complete Episodes of Care Only:

Total Patients: 2 Total Patient Days in Date Range: 91

===============================================================================

Total Patients: 5 Total Patient Days in Date Range: 1,079

===============================================================================

==== End of Report ====

### Program Census Report (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCRP10\]

This option prints the HBPC Program Census Report. The user is prompted to enter the

date range for inclusion on the report. The report is sorted alphabetically by patient name and includes: Patient Name, Last Four, and Admission Date. Report prints in 80 column

format.

This report requires the beginning date to be the oldest current active Admission on file, or an arbitrary date such as 1/1/85, to obtain the complete active census.

User is prompted to select HBPC or MFH report. HBPC report includes all HBPC patients in the user selected date range, with MFH patients indicated by having their MFH listed. MFH report includes only MFH patients in the user selected date range. Below are samples of both HBPC & MFH reports, with patient specific data omitted.

> **NOTE:** The MFH functionality is dormant on this report for sites without an approved MFH sanction status.

HBPC Report:

\>\>\> Program Census Report \<\<\< Page: 1

Run Date: JAN 09, 2008 Date Range: JAN 01, 1985 to

JAN 09, 2008

Last

Patient Name Four Date Medical Foster Name Name

===============================================================================

HBHCPatient, One 1234 01-06-08 MFH Test One

. . .

===============================================================================

Program Census Total: 137

===============================================================================

==== End of Report ====

MFH Report:

\>\>\> HBPC Medical Foster Home (MFH) Program Census Report \<\<\< Page: 1

Run Date: JAN 09, 2008 Date Range: JAN 01, 1985 to

JAN 09, 2008

Last

Patient Name Four Date Medical Foster Name Name

===============================================================================

HBHCPatient, One 1234 01-06-08 MFH Test One

. . .

===============================================================================

Program Census Total: 3

===============================================================================

==== End of Report ====

> **NOTE:** The MFH functionality is dormant on the following options for sites without an approved MFH sanction status.

Use of these options is discussed in the following pages:

Under Transmission Menu ... \[HBHC TRANSMISSION MENU\]

Build/Verify Transmission File \[HBHCFILE\]

Form Errors Report (80) \[HBHCRP1\]

Edit Form Errors Data \[HBHCUPD\]

Transmit File to Austin \[HBHCXMT\]

Print Transmit History Report (80) \[HBHCR15A\]

Please refer to the Transmitting Data to Austin chapter for complete instructions. This section only covers the additional MFH functionality.

### Build/Verify Transmission File 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCFILE\]

This option builds the HBPC Transmission Data file (#634) used to transmit to Austin.

The records included in this file are verified for completeness and also for validity (e.g. no admission data should be included if the patient was rejected from the HBPC program).

If errors/omissions are found, the records in error are written to another file and must be corrected before transmission is allowed. Once the errors are corrected, this option must be run again to add the corrected records to the transmission file. This process (build file, correct errors, add corrected records via build file) may be repeated as necessary until all records are valid and included in the Transmission Data file.

If a site has a sanctioned MFH program, then the MFH data is also included as part of the build processing. The MFH functionality is dormant on this option for sites without an approved MFH sanction status.

### Form Errors Report (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCRP1\]

This option prints the HBPC Form Errors Report. The errors were found when the

Build/Verify Transmission File \[HBHCFILE\] option was run. The report is sorted by

Form, then by Patient Name and includes: Patient File IEN (internal entry number), Patient Name, Last Four, and corresponding Date. Visits also contain: Clinic Name, Error, Provider, <span id="icd9" class="anchor"></span>ICD9 or ICD10 Diagnosis, and CPT Code fields. Report prints in 80 column format.

If a site has a sanctioned MFH program, then the MFH data is also included as part of the report. The MFH functionality is dormant on this option for sites without an approved MFH sanction status.

The Form Errors Report for MFH (80) \[HBHCRP31\] option contains only the MFH errors portion of the Form Errors data.

### Edit Form Errors Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCUPD\]

This option allows editing of the HBPC Form Errors Data. The user is prompted for a patient, then the software prompts for the fields that are missing or invalid in each record. These errors are found when the Build/Verify Transmission File \[HBHCFILE\] option is run and must be corrected before transmission to Austin is allowed. Visit error corrections must be made using PCE options. Then the Edit Form Errors option must be accessed to clean up the Visit Error file.

If a site has a sanctioned MFH program, then the MFH Errors File is also cleaned up by accessing this option. The MFH functionality is dormant on this option for sites without an approved MFH sanction status.

MFH error corrections must be made using the Edit MFH Form Errors Data \[HBHCUPDM\] option. The user is prompted for a MFH name, then the software prompts for the fields that are missing or invalid in each record. This option also cleans up the MFH Errors File.

### Transmit File to Austin 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCXMT\]

This option creates and transmits the HBPC MailMan message using the Transmission Data in HBHC Transmit File (#634) to Austin. All Form Errors found via the Build/Verify Transmission File option must be corrected before transmission to Austin is allowed. A confirmation message will be returned from Austin upon receipt of the HBPC Transmission. This option is locked with the HBHC TRANSMIT security key.

If a site has a sanctioned MFH program, then the MFH data is also included as part of the transmit processing. The MFH functionality is dormant on this option for sites without an approved MFH sanction status.

### Print Transmit History Report (80) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### \[HBHCR15A\]

This option prints the HBPC Transmit History Report. The user is prompted for date from within the last 12 transmit batches & also selects forms for inclusion on the report.

The report includes: form number, patient name, last four, form date, plus Action on form 3 (admission), Provider Number & Provider Name on visits (form 4), & Admission or Discharge on form 6 (corrections).

A Transmit History Report for the current transmission batch can be generated

automatically from the Transmit File to Austin option \[HBHCXMT\] if a default printer is defined in System Parameters file (#631.9). If no printer is defined, no report will be

generated at transmit time.

If a site has a sanctioned MFH program, then the MFH data is also included as part of the report. The MFH functionality is dormant on this option for sites without an approved MFH sanction status.

\>\>\> HBPC FEB 14, 2008 Transmit, Summary Report \<\<\< Page: 1

Run Date: MAR 03, 2008

Summary

===============================================================================

Admit Eval/Adm Form 3 Total: 4

Reject Eval/Adm Form 3 Total: 0

Visit Form 4 Total: 68

Discharge Form 5 Total: 1

Correction Form 6 Total: 0

Medical Foster Home Form 7 Total: 16

-----

All Forms Total: 89

Number of Visits Total: 67

==== End of Report ====

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Application Coordinator | Person responsible for the implementation, training, and troubleshooting of the software package, also acts as liaison between the HBPC Program personnel and IRM.                                                                                                                                                                                                                                                                                                                                     |
| Branching               | Jumping from one spot to another when entering data. Branching determines which questions will be asked based on current values.                                                                                                                                                                                                                                                                                                                                                                       |
| Case Manager            | HBPC provider who is assigned responsibility for coordinating specific patient care.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| D/C                     | Discharge.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Default                 | The most probable answer to the field prompt. The value that appears between the field prompt and two slash marks (//). With the cursor resting next to the field prompt, you can either accept the default answer or enter your own answer. To accept the default, simply press the enter (or return) key. To change the default answer, type in your response.                                                                                                                                       |
| Device Prompt           | A prompt at which you identify where you want to send your report output.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Double Quotes           | The " symbol. Enclose patient name with double quotes to inform VA FileMan you wish to create an additional record with the same name as an existing record in the file. (e.g., "lastname,firstname"). This method is used to create additional episode of care records for a patient in the HBHC Patient file.                                                                                                                                                                                        |
| Enter                   | Accept the entry or default response to a prompt. Symbolized by \<ENTER\> or \<RET\> in this manual.                                                                                                                                                                                                                                                                                                                                                                                                   |
| Episode of Care         | An admission to the HBPC Program begins an episode of care. The episode ends when the patient is discharged from the Program. A complete episode of care must include an admission and a discharge or a reject.                                                                                                                                                                                                                                                                                        |
| Field                   | In the computing environment, a field is similar to the blank space on a form. Field refers to one element of information (e.g., patient name).                                                                                                                                                                                                                                                                                                                                                        |
| Field Prompt            | An online instruction that identifies the type of information you need to enter.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| File                    | A collection of related records treated as a unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Form 3                  | Evaluation/Admission data entry form.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Form 4                  | Visit Log data entry form.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Form 5                  | Discharge data entry form.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Form 6                  | Correction data entry form.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Free Text               | A data type that can contain any printable characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| HBHC                    | Hospital Based Home Care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| HBHC Provider file      | File number 631.4, contains unique HBPC information pertaining to HBPC providers.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| HBPC                    | Home Based Primary Care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Help                    | Assistance information which is available online. Enter 1 or 2 question marks at any field prompt to obtain help explaining what answer(s) the field prompt will accept. Enter 3 question marks at any “Select ... Option” prompt to obtain a description of the option.                                                                                                                                                                                                                               |
| IRM                     | Information Resources Management.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Jump                    | Command that allows you to go from a particular field within a data entry option to another field within that same option.                                                                                                                                                                                                                                                                                                                                                                             |
| Key                     | Special control that allows you to unlock and use options governing sensitive activities and information.                                                                                                                                                                                                                                                                                                                                                                                              |
| Mail Group              | A name assigned to a group of computer users. When you send a message to the group, each member of the mail group receives the message.                                                                                                                                                                                                                                                                                                                                                                |
| Menu                    | A list of options from which you can select an activity.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Option                  | A computing activity that you can select from a menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Package                 | The set of programs, files, documentation, online help, and installation procedures that constitute a given software application.                                                                                                                                                                                                                                                                                                                                                                      |
| Parent Site             | Selection from the MEDICAL CENTER DIVISION (#40.8) file defined at the VistA site level in the Systems Parameter Edit option. Each patient and Medical Foster Home are affiliated to a parent site. If a parent site is not defined for a patient or Medical Foster Home because admission or definition occurred before the install of HBH\*1.0\*32, the value from the HOSPITAL NUMBER (#4) field in the HBHC SYSTEMS PARAMETER (#631.9) file is used for AITC transmissions and management reports. |
| Populate                | To fill in a file with data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Prompt                  | A question or message from the computer requiring your response.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Queued                  | A task that is sent for processing in the background.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Record                  | A collection of data items that refer to a specific entity (e.g., patient name, social security number, date of birth, all referring to the same patient).                                                                                                                                                                                                                                                                                                                                             |
| Required Field          | A mandatory field, one that must not remain blank.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Return                  | On the computer keyboard, the key located where the carriage return is on a typewriter. Symbolized by \<RET\> in this manual.                                                                                                                                                                                                                                                                                                                                                                          |
| Security Key            | Special control that allows you to unlock and use options governing sensitive activities and information.                                                                                                                                                                                                                                                                                                                                                                                              |
| Software                | The set of programs that comprise the HBPC computer application.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Team                    | An interdisciplinary group of staff who care for a specific group of HBPC patients. Some HBPCs are composed of only one team; some have two teams, others three or more.                                                                                                                                                                                                                                                                                                                               |

# Worksheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following worksheets to prepare for the installation and implementation of the software.

## Parameters, Teams, and Clinics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Number Visit Days to Scan: \_\_\_\_\_

Transmit Report Printer: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Teams: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Clinics: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Active Census with ICD9 Code/Text Report, V-21
Adaptive Tasks @ Admission, IV-16
Adaptive Tasks @ Discharge, IV-24
Admissions/Discharges by Date Range Report, V-7
Admit/Reject Action, IV-13
Application Coordinator
duties, I-1
implemention of the software, II-1
Appointment Management
Making an appointment for a Patient, IV-3
using check out, IV-5
using the option, IV-3
Appointment Management, IV-1
Assigning menus and keys, II-3
Automated Information Capture System, IV-2
Auto-queue File Update, II-2, VI-6
Auto-queue HBHC File Update, II-3
B
Bathing @ Admission, IV-14
Bathing @ Discharge, IV-23
Behavior Problems @ Admission, IV-16
Behavior Problems @ Discharge, IV-25
Birth Year, IV-12
Bladder Continence @ Admission, IV-16
Bladder Continence @ Discharge, IV-24
Bowel Continence @ Admission, IV-15
Bowel Continence @ Discharge, IV-24
Build/Verify Transmission File, VI-1, VI-6, VI-9
example, VI-4
how the records are processed, VI-3
incomplete records definition, VI-3
messages, VI-3
regarding to Re-Transmit File to Austin, II-34
updating of HBHC Visit file, II-3
using the option, VI-3
C
Caregiver Limitations @ Adm, IV-16
Caregiver Limitations @ D/C, IV-25
Case Manager, IV-17
Case Manager Census Report, V-23
Cause of Death, IV-22
Census Reports Menu, V-17
Check out a patient
Appointment Management, IV-5
Clinic File Data Entry, II-1, II-5, II-29
County Code, IV-12
CPT Code Summary Report, V-10
D
Data Errors
correcting of, VI-8
Date Discharge Form Completed, IV-25
Date Eval/Adm Form Completed, IV-17
Default values, IV-19
Director of Home & Community-Based Car, VII-1
Discharge Data Entry, IV-1
example, IV-26
using the option, IV-19
Discharge Data Report by Patient, V-5
Discharge Date, IV-20
Discharge Status, IV-20
field branching, IV-21
Disorientation @ Admission, IV-16
Disorientation @ Discharge, IV-25
Dressing @ Admission, IV-15
Dressing @ Discharge, IV-23
E
Eating @ Admission, IV-15
Eating @ Discharge, IV-24
econdary Diagnosis @ Adm, IV-13
Edit Form Errors Data, VI-1
using the option, VI-8
Eligibility @ Discharge, IV-20
Eligibility @ Evaluation, IV-12
Episode of care
complete, IV-9, IV-19
creating a second episode, IV-9
editing of a complete episode, IV-9
Episode of Care/Length of Stay Report, V-6
Evaluation/Admission Data Entry, IV-1
example, IV-17
messages, IV-17
using the option, IV-9
Evaluation/Admission Data Report by Patient, V-2
Event Capture System, IV-2
Exiting, IV-10, IV-19
Exported menu, III-1
Expressive Communication @ Adm, IV-14
Expressive Communication @ D/C, IV-23
F
Field branching logic, IV-10, IV-19, IV-21
Field jumping, IV-10, IV-19
Form 4, IV-9
Form Errors Report, VI-1, VI-3
correcting errors, VI-6
using the option, VI-6
H
HBH mail group, II-2, II-4
HBH Mail Group
confirmation messages, VI-9
HBHC Clinic file \#631.6, II-29
HBHC Discharge Error(s) file \#634.3, VI-3
HBHC Evaluation/Admission Error(s) file \#634.1, VI-3
HBHC MANAGER key, II-1, II-3
HBHC Patient Date, IV-11
HBHC Patient file \#631, IV-9
HBHC Patient Name, IV-20
entering, selecting, IV-10
HBHC Pseudo SSN Error(s) file \#634.5, VI-3
HBHC System Parameters file \#631.9, II-6
HBHC Team file \#633, II-30
HBHC Transmit file \#634, VI-3, VI-9
HBHC TRANSMIT key, II-1, II-3, VI-9
HBHC Visit Error file \#634.2
populating, II-4
HBHC Visit Error(s) file \#634.2, VI-3
HBHC Visit file, VI-6
data collected from visit, IV-5
HBHC Visit file \#632, VI-3
updating of, II-3
HBPC Information System Menu
assigning to users, II-3
HBPC Provider File Report, II-5, II-31
Hearing @ Admission, IV-14
Hearing @ Discharge, IV-22
Home Based Primary Care, VII-1
I
ICD9 Code/Dx Text by Date Range Report, V-12
Implementation of the software
check list, II-1
check list prior to installation, II-1
Manager Menu, II-5
worksheets, II-1
Information System Menu, II-1
K
Keys
HBHC MANAGER, II-1
HBHC TRANSMIT, II-1
L
Last Agency Providing Care, IV-12
Living Arrangements @ D/C, IV-20
Living Arrangements @ Eval, IV-12
M
Making an appointment for a Patient, IV-3
Manager Menu, II-1
use in implementation of the software, II-5
Marital Status @ Discharge, IV-20
Marital Status @ Evaluation, IV-12
Medical Foster Home
Auto-queued Inspection/Training Reminder e-mail, VII-24
Auto-queued License Due Reminder e-mail, VII-26
Basics, VII-1
Blank MFH Worksheet Report, VII-2
Build/Verify Transmission File, VII-33
Caregiver Age Report, VII-18
Delimited Text File Output Menu, VII-19
Demographic Data Entry, VII-4
Edit MFH Form Errors Data, VII-8
e-mail, VII-24, VII-26
Evaluation/Admission Data Entry, VII-27
File Data Report, VII-9
Form Errors Report, VII-19, VII-34
Functionality, VII-1
Inspection Data Entry, VII-6
Inspection/Training Delimited Text File Output, VII-20
Inspection/Training Due Report, VII-13
License Due for MFH Report, VII-17
Menu, VII-2
Patient Days of Care by Date Range Report, VII-29
Print Transmit History Report, VII-36
Program Census Report, VII-31
Queued Options, VII-24
Rate Paid Delimited Text File Output, VII-22
Rate Paid Report, VII-15
Reports, VII-9
Training Data Entry, VII-7
Transmit File to Austin, VII-35
Transmit History, VII-36
Worksheet, VII-10
Messages
Build/Verify Transmission File, VI-3
found in Evaluation/Admission Data Entry, IV-17
Mobility @ Admission, IV-16
Mobility @ Discharge, IV-24
Mood Disturbance @ Admission, IV-16
Mood Disturbance @ Discharge, IV-25
N
Number of Visit Days to Scan, VI-3
Build/Verify Transmission File, VI-3, VI-4
setting of, II-6
O
Office of Geriatrics and Extended Care, VII-1
Outpatient Encounter file \#409.68, II-3
Outpatient Encounters, II-29
P
PARENT SITE, II-6, IV-1, IV-9, IV-11, VII-4, VIII-2
Patient demographic information, IV-9
Patient Visit Data Report, V-4
PCE Clinical Reports Menu, II-3
Period of Service, IV-12
Person Completing D/C Form, IV-25
Person Completing Evl/Adm Form, IV-17
Primary Diagnosis @ Admission, IV-13
Primary Diagnosis @ Discharge, IV-22
Print Transmit History Report, VI-1, VI-11
Printer for the Transmit Report
setting of, II-6
Program Census Report, V-18
Provider Census Report, V-24
Provider CPT Code Summary Report, V-11
Provider File Data Entry, II-1
Pseudo Social Security Number Report, II-5, II-32
Pseudo SSN
correcting record for Collateral patient, II-32
correcting record for wrong patient, II-32
correcting record with invalid SSN, II-32
definition, II-32
R
Race, IV-12
Receptive Communication @ Adm, IV-14
Receptive Communication @ D/C, IV-23
Reject/Withdraw Disposition, IV-13
Reject/Withdraw Reason, IV-13
Rejections from HBPC Programs Report, V-8
Reports Menu, V-1
assigning to users, II-3
Re-Transmit File to Austin, II-5
when to use or not use, II-34
S
Secondary Diagnosis @ D/C, IV-22
Sex, IV-12
State Code, IV-12
System Parameters Edit, II-1, II-5
use of option, II-6
System Parameters file
default printer, VI-11
T
Team Census Report, V-22
Team File Data Entry, II-1, II-5, II-30
Text Integration Utility, IV-2
Toilet Usage @ Admission, IV-15
Toilet Usage @ Discharge, IV-23
Total Visits by Date Range Report, V-14
Transfer Destination, IV-22
Transferring @ Admission, IV-15
Transferring @ Discharge, IV-24
Transmission messages, VI-9
Transmission options flow, VI-2
Transmit File to Austin, VI-1, VI-3
using the option, VI-9
when to use the Re-Transmit File to Austin option, II-34
Transmit Report Printer
setting of, II-6
Transmitting data to Austin, VI-1
Type of Destination Agency, IV-22
Type of Last Care Agency, IV-13
U
Unique Patients by Date Range Summary Report, V-13
V
Vision @ Admission, IV-14
Vision @ Discharge, IV-22
Visit data
adding through Appointment Management, IV-1
adding through Encounter software, IV-1
Visit Data by Date Range Report, V-9
W
Walking @ Admission, IV-15
Walking @ Discharge, IV-24
Worksheets, IX-1
Z
ZIP Code, IV-12
*(This page included for two-sided copying.)*
[^1]: Patch HBH\*1\*10 March 1998 New option.
[^2]: Patch HBH\*1\*2 May 1994 Added the option Pseudo Social Security Number Report.
[^3]: Patch HBH\*1\*2 May 1994 Software modified to recognize pseudo SSNs.
[^4]: Patch HBH\*1\*21 February 2005 – New option added to the Reports Menu
[^5]: Patch HBH\*1\*21 February 2005 – New option added to the Census Reports Menu
[^6]: Patch HBH\*1\*21 February 2005 – New option added to the Census Reports Menu
[^7]: Patch HBH\*1\*6 July 1997 Make Appointment option changed to call Appointment Management. Visit Data Entry and Cancel Appointment options were removed.
[^8]: Patch HBH\*1\*19 January 2003 Removed Race: O Race: Obsolete Field 2003bsolete Field
[^9]: Patch HBH\*1\*21 February 2005 – New option added to the Reports Menu
[^10]: Patch HBH\*1\*21 February 2005 – New option added to the Census Reports Menu
[^11]: Patch HBH\*1\*21 February 2005 – New option added to the Census Reports Menu
[^12]: Patch HBH\*1\*19 January 2003 Race: Obsolete Field January 2003
[^13]: Patch HBH\*1\*16 June 2000 – CPT modifiers added to report; report changed to 80 column format.
[^14]: Patch HBH\*1\*6 July 1997 Changes to report.
[^15]: Patch HBH\*1\*6 July 1997 New option
[^16]: Patch HBH\*1\*16 June 2000 – CPT modifiers added to report; report changed to 80 column format; selection of multiple providers.
[^17]: Patch HBH\*1\*6 July 1997 New option.
[^18]: Patch HBH\*1\*11 July 1998 New option.
[^19]: Patch HBH\*1\*16 June 2000 – Allows selection of multiple providers.
[^20]: Patch HBH\*1\*8 January 1998 New option.
[^21]: Patch HBH\*1\*8 January 1998 New option.
[^22]: Patch HBH\*1\*11 July 1998 New option.
[^23]: Patch HBH\*1\*13 March 1999 New functionality.
[^24]: Patch HBH\*1\*21 February 2005 – New option and example added to the Reports Menu
[^25]: Patch HBH\*1\*21 February 2005 – New option added to the Census Reports Menu
[^26]: Patch HBH\*1\*21 February 2005 – New option added to the Census Reports Menu
[^27]: Patch HBH\*1\*6 July 1997 Changed Admission Date header in report to Date.
[^28]: Patch HBH\*1\*21 February 2005 – New option and example added to the Census Reports Menu
[^29]: Patch HBH\*1\*21 February 2005 – New option and example added to the Census Reports Menu
[^30]: Patch HBH\*1\*6 July 1997 New option.
[^31]: Patch HBH\*1\*6 July 1997 Changed Admission Date header in report to Date.
[^32]: Patch HBH\*1\*6 July 1997 Changed Admission Date header in report to Date.
[^33]: Patch HBH\*1\*16 June 2000 – Allows selection of multiple providers; report formatting changes
[^34]: Patch HBH\*1\*16 June 2000 – Allows selection of multiple providers; report formatting changes
[^35]: Patch HBH\*1\*5 June 1995 Routine no longer excludes visits for the prior 7 days from the Austin transmission.
[^36]: Patch HBH\*1\*10 March 1998 Added mail messages for tasked job.
[^37]: Patch HBH\*1\*8 January 1998 Field added to option.
[^38]: Patch HBH\*1\*10 March 1998 The option was changed to a queued job and includes the display of a task number. The person who queued the job will receive a mail message when the job is complete.
[^39]: Patch HBH\*1\*10 March 1998 Ambulatory Care Reporting Project Interface Toolkit functionality added to software.
[^40]: Patch HBH\*1\*10 March 1998 Added message to "Run Edit Form Errors Data option ..." to report when visit errors exist.
[^41]: Patch HBH\*1\*8 January 1998 HBH Transmit key moved from the Transmission Menu to the Transmit File to Austin option.
[^42]: Patch HBH\*1\*6 July 1997 New option.
