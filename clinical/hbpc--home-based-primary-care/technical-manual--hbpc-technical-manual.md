---
title: HBPC Technical Manual
doc_type: TM
doc_label: Technical Manual
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
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - hbhc
  - home
  - class
  - table
  - contents
  - foster
  - date
  - medical
  - package
  - discharge
page_count: 0
word_count: 6345
section_count: 6
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbh_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbh_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=68"
---

Home Based Primary CareTechnical Manual

![](hbpc-technical-manual/001.png)

Version 1.0March 2001Revised August 2021Department of Veterans AffairsOffice of Information and TechnologyProduct Development

######### Revision History

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 39%" />
<col style="width: 17%" />
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
<td>Title, i, iii, 7, 8, 19, 29</td>
<td><p>HBH*1.0*32:</p>
<ul>
<li><p>Removed Issue Templates and the HBHC EDIT PROVIDER references for 631.4 <strong><u>HBHC Provider</u></strong></p></li>
<li><p>Added the last sentence to the <strong><u>Note</u></strong> for 631.9 HBHC System Parameters</p></li>
<li><p>Added <strong><u>HBHCHOSPX</u></strong> for parent site to the Variables Used section</p></li>
<li><p>Added the <strong><u>Parent Site</u></strong> entry into the Glossary</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>August2014</td>
<td>25</td>
<td>i-ii, <a href="#flow">2</a>, <a href="#icd1">12</a>, <a href="#icd2">16</a>, <a href="#icd3">18</a>, <a href="#icd4">19</a></td>
<td><p>Patch HBH*1*25 August 2014</p>
<ul>
<li><p>Updated Title Page</p></li>
</ul>
<p>– Updated data flow diagram to include ICD-10 (p. <a href="#p2">2</a>)</p>
<p>– Updated Report Titles:</p>
<blockquote>
<p>– Report renamed to ICD Code/Dx Text Date Range Report (pp. <a href="#icd1">12</a>)</p>
<p>– Report renamed to Active Census with ICD Code/Text Report (p. <a href="#icd1">12</a>)</p>
</blockquote>
<p>Updated to include ICD-10 (pp. <a href="#icd2">16</a>, <a href="#icd3">18</a>, <a href="#icd4">19</a>)</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>January 2009</td>
<td>24</td>
<td>Throughout</td>
<td>Patch HBH*1*24 April 2008 – Medical Foster Home (MFH) functionality added; <strong>Note:</strong> ONLY sites who have received MFH sanction status approval from VACO should implement the MFH functionality; MFH functionality is dormant for sites without an approved MFH sanction status; MFH info dispersed throughout the manual where applicable; specific MFH Implementation Chapter included</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>February 2005</td>
<td>21</td>
<td>14, 15, &amp; 19</td>
<td><p>Patch HBH*1*21 February 2005</p>
<p>– New variables</p>
<ul>
<li><p>HBHCCASE – case manager</p></li>
<li><p>HBHCDISC – discipline</p></li>
</ul>
<p>HBHCSTOP – stop code</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>February 2005</td>
<td>21</td>
<td>10</td>
<td><p>Patch HBH*1*21 February 2005 – New option added to the Census Reports Menu.</p>
<p>- Address Included Program Census (132)</p>
<p>- Expanded Program Census Report (80)</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>February 2005</td>
<td>21</td>
<td>10</td>
<td><p>Patch HBH*1*21 February 2005</p>
<p>– New option added to the Reports Menu.</p>
<p>– Patient Days of Care by Date Range Report (80)</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Installation Check List](#installation-check-list)
  - [Assigning Menus and Keys](#assigning-menus-and-keys)
    - [HBPC Information System Menu](#hbpc-information-system-menu)
    - [Reports Menu](#reports-menu)
    - [Auto-Queue File Update](#auto-queue-file-update)
    - [Note: ONLY sites who have received MFH sanction status approval from VACO should schedule the following two options:](#note-only-sites-who-have-received-mfh-sanction-status-approval-from-vaco-should-schedule-the-following-two-options)
    - [Auto-queued Inspection/Training Reminder e-mail](#auto-queued-inspectiontraining-reminder-e-mail)
  - [Assigning the HBH Mail Group](#assigning-the-hbh-mail-group)
    - [Assigning the HBHC MEDICAL FOSTER HOME Mail Group](#assigning-the-hbhc-medical-foster-home-mail-group)
- [Routines](#routines)
- [Exported Options](#exported-options)
- [Archiving and Purging](#archiving-and-purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
- [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [Variables Used](#variables-used)
- [Software Product Security](#software-product-security)
  - [MFH Implementation Check List](#mfh-implementation-check-list)
- [Glossary](#glossary)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is meant to be used by IRM support for the implementation and maintenance of the Home Based Primary Care (HBPC) package formally known as Hospital Based Home Care (HBHC).

The Home Based Primary Care package is a VISTA application developed for use by the HBPC Programs at the medical centers. The software:

- Allows the entry and storage of information on all Evaluations/Admissions,
- Scans Outpatient Encounters for all HBPC visits and stores the visit data,
- Allows the entry and storage of HBPC Discharge information,
- Provides reports covering all aspects of the data,
- Informs the staff when incomplete records for transmission are found,
- Transmits the data to Austin using MailMan.

Patch HBH\*1\*24 brings in Medical Foster Home (MFH) functionality.

\*\*\*\*\* Important!! \*\*\*\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Note: Only sites that have received Medical Foster Home (MFH) sanction status approval from the Director of Home & Community-Based Care in the Office of Geriatrics and Extended Care, VA Central Office (VACO), should be utilizing the MFH portion of the Home Based Primary Care (HBPC) Information System software. The MFH functionality is controlled by the MED FOSTER HOME SANCTION DATE field (#8) in HBHC SYSTEM PARAMETERS file (#631.9). This field should be blank until site receives official sanction date from VACO. The MFH functionality is dormant for sites without an approved MFH sanction status. Please see MFH Implementation Chapter for MFH functionality setup specifics.

Background: Medical Foster Home (MFH) combines adult foster care in a privately owned residence located in the community, with Home Based Primary Care (HBPC) or Spinal Cord Injury Home Care (SCI-HC). MFH offers a safe alternative to nursing home placement, merging personal care in a private home with medical & rehabilitation support from specialized VA home care programs. Veterans placed in MFH meet nursing home admission criteria. Payment of MFH charges is the responsibility of the veteran.  
<span id="p2" class="anchor"></span>HBPC Data Flow <span id="flow" class="anchor"></span>

|               |         |         |         |     |
|---------------|---------|---------|---------|-----|
| Appt Mgmt | TIU | PCE | ECS |     |

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter is for the IRM support person who will be implementing the software. Much of the implementation work can be done by an end user assigned the role of the application coordinator, so this information is also available in the user manual.

## Installation Check List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to installation of the package:

- Obtain the official startup date for visit records to be electronically transmitted to Austin from the application coordinator.
- Review this chapter to get an overview of how menus and keys should be assigned.
- Ask the application coordinator or a person who works for Home Based Primary Care to complete the Worksheets at the end of the user manual. The information will be used to complete the options System Parameters Edit, Clinic File Data Entry, Team File Data Entry and Provider File Data Entry once the package is installed. These worksheets can also be used to determine who receives what menus and who should belong to the HBH mail group.

After Installation of the package:

- Make sure you are assigned the HBHC MANAGER key and the HBPC Information System Menu.
- Use the following options or ask the application coordinator for the package to enter all set up data in the program:
1.  System Parameters Edit.
2.  Clinic File Data Entry.
3.  Team File Data Entry. Note: It is required that all providers for the program be assigned to a team.
4.  Provider File Data Entry.
- Assign menus and, where appropriate, keys to the users.
- Set the Auto-queue File Update \[HBHC AUTO-QUEUED FILE UPDATE\] option to run daily, shortly after midnight.
- Assign members to the HBH mail group.
- Using FileMan, populate the Valid State Code file \#631.8 with any state codes that are used by your site.
- Refer to the MFH Implementation Chapter ONLY if your site has received Medical Foster Home (MFH) sanction status approval from the Director of Home & Community-Based Care in the Office of Geriatrics and Extended Care, VA Central Office (VACO). The MFH functionality is controlled by the MED FOSTER HOME SANCTION DATE field (#8) in HBHC SYSTEM PARAMETERS file (#631.9). This field should be blank until site receives official sanction date from VACO. The MFH functionality is dormant for sites without an approved MFH program.

## Assigning Menus and Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HBPC Information System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign this menu to the Application Coordinator and any users who will be adding/editing data in the package.

> Any person assigned this menu who is also responsible for implementing and maintaining the package needs the HBHC MANAGER key to use the Manager Menu.

> Any person assigned this menu who is also responsible for transmitting the data to Austin, needs the HBHC TRANSMIT key. (This key should be limited to only those few people who will transmit the data.)

> Note: ONLY sites who have received MFH sanction status approval from VACO should assign anyone the HBHC MEDICAL FOSTER HOME key. It locks the Medical Foster Home (MFH) Menu \[HBHC MFH MENU\] option. The MFH functionality is dormant for sites without an approved MFH sanction status.

### Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There may be some users who will not be entering data but who need access to reports. Assign this menu to those users.

> PCE Clinical Reports Menu

> While the PCE Clinical Reports \[PXRR CLINICAL REPORTS\] menu is not a part of the HBPC software, the options can be useful in addition to the HBPC reports.

> Patient Activity by Location \[PXRR PATIENT ACTIVITY BY LOC\]

> Caseload Profile by Clinic \[PXRR CASELOAD PROFILE BY CL\]

> PCE Encounter Summary \[PXRR PCE ENCOUNTER SUMMARY\]

> Diagnosis Ranked by Frequency \[PXRR MOST FREQUENT DIAGNOSES\]

> Location Encounter Counts \[PXRR LOCATION ENCOUNTER COUNTS\]

> Provider Encounter Counts \[PXRR PROVIDER ENCOUNTER COUNTS\]

### Auto-Queue File Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHC AUTO-QUEUED FILE UPDATE\]

This option is not attached to any menu and is not assigned to anyone. The option should be queued to run every day. It performs the HBHC Visit file \#632 update processing that is also found as part of the Build/Verify Transmission File option. The option runs against the Outpatient Encounter file \#409.68 covering the previous 7 days of appointments and updates the HBHC Visit file with both additions and cancellations for encounters.

If any errors are found during the Auto-queue File Update, the records with errors are placed in the HBHC Visit Error file \#634.2 and members of the HBH mail group are sent a mail message containing the following:

> Please run Form Errors Report option for HBHC errors to correct.

This gives them the opportunity to correct problems as they arise.

The HBHC Visit Error file is deleted and rebuilt as part of the scheduled auto-queued job. Therefore, the same record may be placed in the error file after each run over the 7 days if it is not corrected, and the HBH mail group will receive a mail message each of those 7 days.

### Note: ONLY sites who have received MFH sanction status approval from VACO should schedule the following two options:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto-queued Inspection/Training Reminder e-mail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[HBHC MFH AUTO-QUEUED REMINDERS\]

This option is not attached to any menu and is not assigned to anyone. The option should be queued to run the 1<sup>st</sup> calendar day of each month. The option runs against the HBHC MEDICAL FOSTER HOME file (#633.2) Inspection & Training multiples. Members of the HBHC MEDICAL FOSTER HOME mail group are sent a mail message if any inspections or training sessions are due within the next 3 months, based on month only.

Auto-queued License Due Reminder e-mail

\[HBHC MFH AUTO-Q LICENSE DUE\]

This option is not attached to any menu and is not assigned to anyone. The option should be queued to run the 1<sup>st</sup> calendar day of each month. The option runs against the HBHC MEDICAL FOSTER HOME file (#633.2) License Expiration Date data. Members of the HBHC MEDICAL FOSTER HOME mail group are sent a mail message if any licenses are due within the next 3 months, based on month only.

## Assigning the HBH Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Members of the HBH mail group receive data error messages after visit data is scanned. This group also receives any messages pertaining to the transmission of the data to Austin. Assign users to this mail group that will be responsible for correcting data errors or receiving transmission/confirmation messages.

### Assigning the HBHC MEDICAL FOSTER HOME Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** ONLY sites who have received MFH sanction status approval from VACO should assign anyone to the HBHC MEDICAL FOSTER HOME.

Members of the HBHC MEDICAL FOSTER HOME mail group receive mail messages on the 1<sup>st</sup> of each month for inspections, training sessions, or licenses due for the MFH.  
Files

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 29%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td>File #</td>
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>631</td>
<td>HBHC Patient</td>
<td><p>This file contains demographic, admission, discharge, and record transmission data.</p>
<p>Input Template(s):</p>
<p>HBHC DISCHARGE</p>
<p>HBHC UPDATE DISCHARGE</p></td>
</tr>
<tr class="odd">
<td>631.1</td>
<td>HBHC Reject/Withdraw Reason</td>
<td>This file contains reason for rejecting or withdrawing HBPC patients. It is exported with data and is referenced by the HBHC Patient (#631) file. Entries should not be added to or edited in this file.</td>
</tr>
<tr class="even">
<td>631.2</td>
<td>HBHC Expressive Communication</td>
<td>This file contains selections for expressive communication. It is exported with data and is referenced by the HBHC Patient (#631) file. Entries should not be added to or edited in this file.</td>
</tr>
<tr class="odd">
<td>631.3</td>
<td>HBHC Receptive Communication</td>
<td>This file contains selections for receptive communication. It is exported with data and is referenced by the HBHC Patient (#631) file. Entries should not be added to or edited in this file.</td>
</tr>
<tr class="even">
<td>631.4</td>
<td>HBHC Provider</td>
<td>This file contains Provider data. The Provider name field is a pointer to VA (#200).</td>
</tr>
<tr class="odd">
<td>*631.5</td>
<td>HBHC Type of Visit</td>
<td>This file contains types of visits. It is exported with data and is referenced by the HBHC Visit (#632) file. Entries should not be added to or edited in this file.</td>
</tr>
<tr class="even">
<td>631.6</td>
<td>HBHC Clinic</td>
<td>This file contains HBHC Clinic data. The Clinic Name field is a pointer to Hospital Location (#44) file.</td>
</tr>
<tr class="odd">
<td>631.7</td>
<td>HBHC Period of Service</td>
<td>This file contains selections for HBHC Period of Service. It is exported with data and is referenced by HBHC Patient (#631) file. Entries should not be added to or edited in this file.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 29%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td>631.8</td>
<td>HBHC Valid State Code</td>
<td>This file is the HBHC Valid State Code file and contains state codes which are site specific. All state codes must exist in State file (#5).</td>
</tr>
<tr class="even">
<td>631.9</td>
<td>HBHC System Parameters</td>
<td><p>This file contains HBHC System Parameters data and is exported with one record.</p>
<p><strong>Note:</strong> This file should only contain ONE record.</p>
<p>The Package Name (#.01) field contains 'Hospital Based Home Care' and is not editable. The Last Mail Message Date field is maintained by the package and is not editable. The Package Startup Date field is entered by IRM on the virgin installation of the package and is not editable. The Package Startup Date represents the earliest allowable date for visit data being transmitted to Austin. The Number of Visit Days to Scan field can be edited by the user. The Transmit Report Printer, if defined by the user, will automatically print the Transmit History Report when the Transmit File to Austin option is run.</p>
<p><strong>Note:</strong> MED FOSTER HOME SANCTION DATE field should be blank unless site has obtained official MFH sanction status from VACO. One or more VA HBPC sanctioned sites are defined as PARENT SITE(S).</p></td>
</tr>
<tr class="odd">
<td>632</td>
<td>HBHC Visit</td>
<td>This file includes visit and record transmission data.</td>
</tr>
<tr class="even">
<td>633</td>
<td>HBHC Team</td>
<td>This file contains the HBHC Team data and is referenced by HBHC Provider (#631.4) file.</td>
</tr>
<tr class="odd">
<td>633.2</td>
<td>HBHC MEDICAL FOSTER HOME</td>
<td><p>This file contains the HBHC Medical Foster Home (MFH) demographic data pertaining to the home itself.</p>
<p>Input Template(s):</p>
<p>HBHC MFH DEMOGRAPHIC INPUT</p>
<p>HBHC MFH INSPECTION INPUT</p>
<p>HBHC MFH TRAINING INPUT</p></td>
</tr>
<tr class="even">
<td>633.1</td>
<td>HBHC Error Messages for Visits</td>
<td>This file contains HBHC Error Messages for Visit data. It is exported with data, and is referenced by the HBHC Visit Error(s) (#634.2) file. Entries should not be added to or edited in this file.</td>
</tr>
<tr class="odd">
<td>634</td>
<td>HBHC Transmit</td>
<td>This file contains HBHC admission, visit, discharge, and correction records for transmission to Austin. MFH records will be included if a site has a sanctioned MFH program.</td>
</tr>
<tr class="even">
<td>634.1</td>
<td>HBHC Evaluation/Admission Error(s)</td>
<td>This file contains HBHC Evaluation/Admission Errors found during verification of records for transmission to Austin. Fields missing data and/or records with data inconsistencies are considered errors.</td>
</tr>
</tbody>
</table>

|       |                                   |                                                                                                                                                                                               |
|-------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 634.2 | HBHC Visit Error(s)               | This file contains HBHC Visit Errors found during verification of records for transmission to Austin. Fields missing data are considered errors.                                              |
| 634.3 | HBHC Discharge Error(s)           | This file contains HBHC Discharge Errors found during verification of records for transmission to Austin. Fields missing data and/or records with data inconsistencies are considered errors. |
| 634.4 | HBHC Form 6 Corrections           | This file contains HBHC Form 6 Correction records awaiting transmission to Austin.                                                                                                            |
| 634.5 | HBHC Pseudo SSN Error(s)          | This file contains records with pseudo SSNs which are considered errors and should not be transmitted to Austin.                                                                              |
| 634.6 | HBHC Transmit History             | This file contains data from the last 12 transmit batches. Data is maintained by the package, no user input is allowed.                                                                       |
| 634.7 | HBHC MEDICAL FOSTER HOME ERROR(S) | This file contains HBHC MFH Errors found during verification of records for transmission to Austin. Fields missing data are considered errors.                                                |

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All routines in this package are namespaced HBH\*. You can obtain a list of the routines and their first line descriptions using the option First Line Routine Print.

PRINTS FIRST LINES

routine(s) ? \> HBH\*

searching directory ...

routine(s) ? \> \<RET\>

(A)lpha, (D)ate ,(P)atched, OR (S)ize ORDER: A// \<RET\>

Include line 2? NO// \<RET\>

DEVICE: HOME// (Enter a printer or \<RET\> to bring the output to your screen)

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See <u>Assigning Menus and Keys</u> for information on distribution of menus and assignment of keys.

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

> [^1] Patient Days of Care by Date Range Report (80) \[HBHCRP23\]

> Total Visits by Date Range Report (80) \[HBHCRP21\]

> Census Reports Menu ... \[HBHC CENSUS REPORTS MENU\]

> Program Census Report (80) \[HBHCRP10\]

> [^2] Address Included Program Census (132) \[HBHCRP25\]

> [^3] Expanded Program Census Report (80) \[HBHCRP24\]

> Active Census with ICD Code/Text Report (132) \[HBHCRP18\]

> Team Census Report (80) \[HBHCRP11\]

> Case Manager Census Report (132) \[HBHCRP6\]

> Provider Census Report (132) \[HBHCRP9\]

Transmission Menu ... \[HBHC TRANSMISSION MENU\]

> Build/Verify Transmission File \[HBHCFILE\]

> Form Errors Report (80) \[HBHCRP1\]

> Edit Form Errors Data \[HBHCUPD\]

> Transmit File to Austin \[HBHCXMT\] \*\* Locked with HBHC TRANSMIT \*\*

> Print Transmit History Report (80) \[HBHCR15A\]

> Manager Menu ... \[HBHC MANAGER MENU\] \*\* Locked with HBHC MANAGER \*\*

> System Parameters Edit \[HBHC EDIT SYSTEM PARAMETERS\]

> Provider File Data Entry \[HBHC EDIT PROVIDER (631.4)\]

> Clinic File Data Entry \[HBHC EDIT CLINIC (631.6)\]

> Team File Data Entry \[HBHC EDIT HBHC TEAM (633)\]

> HBPC Provider File Report (132) \[HBHCRP8\]

> Pseudo Social Security Number Report (80) \[HBHXRP14\]

> Re-Transmit File to Austin \[HBHCRXMT\]

Medical Foster Home (MFH) Menu ... \[HBHC MFH MENU\]

\*\* Locked with HBHC MEDICAL FOSTER HOME

Blank MFH Worksheet Report (80) \[HBHCBLNK\]

Demographic Data Entry for MFH \[HBHC MFH DEMOGRAPHIC

INPUT\]

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

Delimited Text File Output Menu for MFH ... \[HBHC MFH

TEXT FILE OUTPUT MENU\]

Inspection/Training Delimited Text File Output \[HBHCTXT2\]

Rate Paid Delimited Text File Output \[HBHCTXT\]

The Integration Agreement that allowed the cloned Appointment Management option, \[HBHC APPOINTMENT\], to hang on the HBPC Information System Menu has been retired. Retirement was due to impending implementation of the new Resource Scheduling Application (RSA) that is to replace the legacy scheduling options. IRM should add the original Appointment Management Option, \[SDAM APPT MGT\], as a secondary menu option for HBPC users to use once patch HBH\*1\*24 is installed. Once the RSA has been nationally released, the Appointment Management option and other legacy Scheduling options will be going away. When the option is ultimately removed, there should be no work for HBPC to do as the new RSA application will be hosted outside of VistA, requiring startup of a GUI application.

<u>Reminder</u>: Please assign the original Appointment Management Option, \[SDAM APPT MGT\], as a secondary menu option for HBPC users as appropriate

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving or purging capabilities available in this program.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following external packages are required by this software:

> VA FileMan V. 22

> Kernel V. 7.1

> MailMan V. 8

PIMS V. 5.3

Under the DBA menu on Forum, you can use the Subscriber and Custodial Package Menus to view integration agreements between the HBPC package and other VISTA software. Note the integration agreements are under the package name of HOSPITAL BASED HOME CARE:

Subscriber Agreements

Select Integration Agreements Menu Option: Subscriber Package Menu

1 Print ACTIVE by Subscribing Package

2 Print ALL by Subscribing Package

Select Subscriber Package Menu Option: 1 Print ACTIVE by Subscribing Package

\* Previous selection: SUBSCRIBING PACKAGE equals HOSPITAL BASED HOME CARE

START WITH SUBSCRIBING PACKAGE: FIRST// HOSPITAL BASED HOME CARE

GO TO SUBSCRIBING PACKAGE: LAST// HOSPITAL BASED HOME CARE

DEVICE: (Enter a device)

Custodial Agreements

Select Integration Agreements Menu Option: 8 Custodial Package Menu

1 ACTIVE by Custodial Package

2 Print ALL by Custodial Package

3 Supported References Print All

Select Custodial Package Menu Option: 1 ACTIVE by Custodial Package

Select PACKAGE NAME: HOSPITAL BASED HOME CARE HBH

DEVICE: HOME// (Enter a device)

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the HBPC package options are stand alone.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables.

# Variables Used

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Variable Represents

==============================================

HBHC scratch

HBHC1 scratch

HBHC12 discharge status of 1 or 2

HBHC2 scratch

HBHC3 scratch

HBHC359 discharge status of 3, 5, or 9

HBHC3XMT form 3 transmit status

HBHC5XMT form 5 transmit status

HBHCACTN action

HBHCADDT admission date

HBHCADTA adaptive tasks @ admission

HBHCADTD adaptive tasks @ discharge

HBHCAFLG admission data flag

HBHCAGCY agency

HBHCAGE caregiver age

HBHCAPDT appointment date

HBHCBEDM bedbound patient maximum

HBHCBEG1 beginning date 1

HBHCBEG2 beginning date 2

HBHCBGDT beginning date

HBHCBHVA behavior problems @ admission

HBHCBHVD behavior problems @ discharge

HBHCBLDA bladder continence @ admission

HBHCBLDD bladder continence @ discharge

HBHCBLNK blank

HBHCBTHA bathing @ admission

HBHCBTHD bathing @ discharge

HBHCBWLA bowel continence @ admission

HBHCBWLD bowel continence @ discharge

HBHCBXRF B cross-reference

HBHCBYR birth year

HBHCC column

HBHCCARE last agency providing care

[^4]HBHCCASE case manager

HBHCCAT <span id="icd2" class="anchor"></span>ICD9 and ICD10 category

HBHCCATB ICD9 and ICD10 category beginning

HBHCCATE ICD9 and ICD10 category ending

HBHCCDOB caregiver date of birth

HBHCCDTS creation date/time/seconds

HBHCCKDT check date

Variable Represents

==============================================

HBHCCLM1 column 1

HBHCCLOS medical foster home (MFH) close date

HBHCCLN clinic

HBHCCNT count

HBHCCNT1 count 1

HBHCCNT4 form 4 count

HBHCCNT5 form 5 count

HBHCCNT6 form 6 count

HBHCCNTA admit count

HBHCCNTR reject count

HBHCCNTY county

HBHCCOLM column

HBHCCONT continue flag

HBHCCP10 CPT code 10

HBHCCPT CPT code

HBHCCPT1 CPT code 1

HBHCCPT2 CPT code 2

HBHCCPT3 CPT code 3

HBHCCPT4 CPT code 4

HBHCCPT5 CPT code 5

HBHCCPT6 CPT code 6

HBHCCPT7 CPT code 7

HBHCCPT8 CPT code 8

HBHCCPT9 CPT code 9

HBHCCPTA CPT code array

HBHCCPTB beginning CPT code

HBHCCPTE ending CPT code

HBHCCPTL CPT code list array

HBHCCURJ current J loop value

HBHCCURK current K loop value

HBHCCURL current L loop value

HBHCDAT date

HBHCDATE date

HBHCDAYS days

HBHCDDTA discharge data flag

HBHCDEST destination

HBHCDFLG discharge data flag

HBHCDFLT default

HBHCDFN data file number

HBHCDIED died flag

HBHCDIR DIR response

[^5]HBHCDISC discipline

HBHCDLMT delimiter value

Variable Represents

==============================================

HBHCDPT DPT (patient)

HBHCDPT0 DPT node 0 (patient file)

HBHCDPTA DPT address node (patient file)

HBHCDR DR string

HBHCDR1 DR string 1

HBHCDR2 DR string 2

HBHCDR3 DR string 3

HBHCDR4 DR string 4

HBHCDR5 DR string 5

HBHCDRSA dressing @ admission

HBHCDRSD dressing @ discharge

HBHCDSDT discharge date

HBHCDSOA disorientation @ admission

HBHCDSOD disorientation @ discharge

HBHCDT date

HBHCDX <span id="icd3" class="anchor"></span>diagnosis (ICD9 and ICD10 code)

HBHCDX( diagnosis (ICD9 and ICD10 code) array

HBHCDX1 diagnosis (ICD9 and ICD10 code) 1

HBHCDX2 diagnosis (ICD9 and ICD10 code) 2

HBHCDX3 diagnosis (ICD9 and ICD10 code) 3

HBHCDX4 diagnosis (ICD9 and ICD10 code) 4

HBHCDX5 diagnosis (ICD9 and ICD10 code) 5

HBHCDXL diagnosis list array

HBHCDXPC diagnosis piece

HBHCEATA eating @ admission

HBHCEATD eating @ discharge

HBHCEL eligibility

HBHCELGD eligibility @ discharge

HBHCELGE eligibility @ evaluation

HBHCEND1 ending date 1

HBHCEND2 ending date 2

HBHCEXCA expressive communication @ admission

HBHCEXCD expressive communication @ discharge

HBHCFFFL form feed flag

HBHCFILE file

HBHCFL file

HBHCFLAG flag

HBHCFLD field

HBHCFLD1 field 1

HBHCFLD2 field 2

HBHCFLD3 field 3

HBHCFLG flag

HBHCFORM form

HBHCFTOT final total

Variable Represents

==============================================

HBHCHDR header

HBHCHEAD header

HBHCHERA hearing @ admission

HBHCHERD hearing @ discharge

HBHCHOSP hospital

HBHCHOSPX parent site

HBHCI loop counter

HBHCICD0 ICD Diagnosis node 0

HBHCICDA primary diagnosis @ admission

HBHCICDD primary diagnosis @ discharge

HBHCICDP <span id="icd4" class="anchor"></span>diagnosis (ICD9 and ICD10 code) pointer

HBHCIEN internal entry number

HBHCINFO information

HBHCIOP device name (.01 in device file \#3.5)

HBHCJ loop counter

HBHCK loop counter

HBHCKEEP keep flag

HBHCL loop counter

HBHCLEAP leap year flag

HBHCLIVD living arrangements @ discharge

HBHCLIVE living arrangements @ evaluation

HBHCLMTA caregiver limitations @ admission

HBHCLMTD caregiver limitations @ discharge

HBHCLNME last name

HBHCLNTH length

HBHCLOS length of stay

HBHCLREQ license required

HBHCLSDT last date

HBHCLST4 last 4 digits of social security number

HBHCM loop counter

HBHCMARD marital status @ discharge

HBHCMARE marital status @ evaluation

HBHCMFHN medical foster home (MFH) name

HBHCMFHP medical foster home (MFH) pointer

HBHCMFHR medical foster home (MFH) report

HBHCMFHS medical foster home (MFH) site

HBHCMO month

HBHCMOBA mobility @ admission

HBHCMOBD mobility @ discharge

HBHCMOD CPT Modifier

HBHCMODA mood disturbance @ admission

HBHCMODD mood disturbance @ discharge

HBHCMPT medical foster home (MFH) patient

HBHCMRDT most recent date

HBHCMS marital status

Variable Represents

==============================================

HBHCMSG message

HBHCMXPT maximum patients

HBHCN name

HBHCNAM name

HBHCNAME name

HBHCNBR number

HBHCNDX index

HBHCNDX1 index 1

HBHCNDX2 index 2

HBHCNM name

HBHCNOD0 node 0

HBHCNOD2 node 2

HBHCNOD3 node 3

HBHCNOD4 node 4

HBHCNODE node

HBHCNOW now

HBHCNSHP no hospital flag (used in patch 2)

HBHCOEP outpatient encounter pointer

HBHCONE one

HBHCOPEN medical foster home (MFH) open date

HBHCPAGE page

HBHCPC piece

HBHCPC1 piece 1

HBHCPC2 piece 2

HBHCPC3 piece 3

HBHCPCNT provider count

HBHCPHON phone number

HBHCPIEN provider internal entry number

HBHCPRCT percent

HBHCPRTR printer

HBHCPRV provider

HBHCPRV( provider array

HBHCPRV1 provider 1

HBHCPRV1( outpatient provider array

HBHCPRVL provider list array

HBHCPRVN provider number

HBHCPRVP provider pointer

HBHCPS period of service

HBHCPSRV period of service

HBHCPT patient

HBHCQ quit flag

HBHCQ1 quit flag 1

HBHCQAI QA indicator

HBHCRACE race

Variable Represents

==============================================

HBHCRC race

HBHCREC record

HBHCRECA receptive communication @ admission

HBHCRECD receptive communication @ discharge

HBHCREJ reject/withdraw reason

HBHCREJD reject/withdraw disposition

HBHCRFLG rejection data flag

HBHCRFIN referred while inpatient

HBHCRTPD rate paid amount

HBHCRTDT rate paid start date

HBHCSCE0 outpatient encounter zero node

HBHCSEX sex

HBHCSP1 space 1

HBHCSP10 space 10

HBHCS101 space 101

HBHCS131 space 131

HBHCS136 space 136

HBHCSP16 space 16

HBHCSP18 space 18

HBHCSP2 space 2

HBHCSP3 space 3

HBHCSP4 space 4

HBHCSP5 space 5

HBHCSP6 space 6

HBHCSP61 space 61

HBHCSP66 space 66

HBHCSP74 space 74

HBHCSP8 space 8

HBHCSSN social security number

HBHCST state

HBHCSTAT status

HBHCSTDT package startup date

[^6]HBHCSTOP stop code

HBHCSUB subscript

HBHCSX sex

HBHCTDY today

HBHCTEAM team

HBHCTEXT text

HBHCTFLG transfer data flag

HBHCTIME time

HBHCTLTA toilet usage @ admission

HBHCTLTD toilet usage @ discharge

HBHCTMP temporary

Variable Represents

==============================================

HBHCTMP( temporary array

HBHCTMP1 temporary 1

HBHCTMP2 temporary 2

HBHCTMP3 temporary 3

HBHCTMP4 temporary 4

HBHCTOT total

HBHCTOT1 total 1

HBHCTOT2 total 2

HBHCTRN training

HBHCTRNA transferring @ admission

HBHCTRND transferring @ discharge

HBHCTXT text

HBHCTYP type

HBHCTYPE type

HBHCTYPS type with an "s" (plural)

HBHCUPD update flag

HBHCVISA vision @ admission

HBHCVISD vision @ discharge

HBHCVSTP visit file (9000010) pointer

HBHCWHO who

HBHCWHOC who capitalized

HBHCWHOS who with an "s" (plural)

HBHCWLKA walking @ admission

HBHCWLKD walking @ discharge

HBHCWRD1 word 1

HBHCWRD2 word 2

HBHCWRD3 word 3

HBHCX scratch

HBHCXMT3 form 3 transmit status

HBHCXMT4 form 4 transmit status

HBHCXMT5 form 5 transmit status

HBHCXMT7 form 7 transmit status

HBHCXREF cross-reference

HBHCY "-" underline

HBHCY0 Y(0) data

HBHCY12 12 underline characters

HBHCY20 20 underline characters

HBHCY30 30 underline characters

HBHCY40 40 underline characters

HBHCY50 50 underline characters

HBHCY65 65 underline characters

HBHCYEAR year

HBHCYN yes/no

HBHCZ "=" underline

Variable Represents

==============================================

HBHCZIP ZIP code

HBHCZRO4 four zeroes

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All HBHC files are exported with FileMan security codes set to "@" for Data Dictionary, Read, Write, Delete, LAYGO, & Audit file access. Each of the files listed below will need the FileMan security code changed from "@" to an appropriate code for the HBPC service. Each service will need to determine the proper access level for their users.

Data Dictionary and Audit access are reserved for the IRMS staff. Delete access should NOT be allowed on any HBHC files since these files point to or are referenced by other files. Read and/or Write Access is granted by virtue of the menu options that reference each file.

NUMBER NAME DD RD WR DEL LAYGO AUDIT

---------------------------------------------------------------------------------------------------------------------------------

631 HBHC PATIENT @ @ @ @ @ @

631.1 HBHC REJECT/WITHDRAWEL REASON @ @ @ @ @ @

631.2 HBHC EXPRESSIVE COMMUNICATION @ @ @ @ @ @

631.3 HBHC RECEPTIVE COMMUNICATION @ @ @ @ @ @

631.4 HBHC PROVIDER @ @ @ @ @ @

631.5 HBHC TYPE OF VISIT @ @ @ @ @ @

631.6 HBHC CLINIC @ @ @ @ @ @

631.7 HBHC PERIOD OF SERVICE @ @ @ @ @ @

631.8 HBHC VALID STATE CODE @ @ @ @ @ @

631.9 HBHC SYSTEM PARAMETER @ @ @ @ @ @

632 HBHC VISIT @ @ @ @ @ @

633 HBHC TEAM @ @ @ @ @ @

633.1 HBHC ERROR MESSAGES FOR VISITS @ @ @ @ @ @

633.2 HBHC MEDICAL FOSTER HOME @ @ @ @ @ @

634 HBHC TRANSMIT @ @ @ @ @ @

634.1 HBHC EVALUATION/ADMISSION

ERROR(S) @ @ @ @ @ @

634.2 HBHC VISIT ERROR(S) @ @ @ @ @ @

634.3 HBHC DISCHARGE ERROR(S) @ @ @ @ @ @

634.4 HBHC FORM 6 CORRECTIONS @ @ @ @ @ @

634.5 HBHC PSEUDO SSN ERROR(S) @ @ @ @ @ @

634.6 HBHC TRANSMIT HISTORY @ @ @ @ @ @

634.7 HBHC MEDICAL FOSTER HOME @ @ @ @ @ @

ERROR(S)

Security Keys

HBHC TRANSMIT

> This key locks the Transmit File to Austin \[HBHCXMT\] option and should be assigned to users responsible for data transmission to Austin.

HBHC MANAGER

> This key locks the HBHC Manager Menu \[HBHC MANAGER MENU\] option and should be assigned to the Application Coordinator.

> **NOTE:** ONLY sites who have received MFH sanction status approval from VACO should assign anyone the HBHC MEDICAL FOSTER HOME key. The MFH functionality is dormant for sites without an approved MFH sanction status.

HBHC MEDICAL FOSTER HOME

> This security key locks the Medical Foster Home (MFH) Menu \[HBHC MFH MENU\] option.

Mail Group

> The HBH mail group receives messages concerning visit record data errors and Austin transmission confirmation messages.

Legal Requirements

There are no known legal requirements associated with the HBPC package.

MFH Implementation Chapter

## MFH Implementation Check List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to implementation of the MFH functionality brought in by patch HBH\*1\*24:

- Obtain the official MFH sanction date from the HBPC Program Director, or the application coordinator.
- Review the Assigning Menus and Keys chapter to get an overview of how menus and keys should be assigned.
- Ask the application coordinator or a person who works for Home Based Primary Care to complete the Clinic, Team, & Provider Worksheets at the end of the user manual. The information will be used to complete the options Clinic File Data Entry, Team File Data Entry and Provider File Data Entry as the MFH functionality is implemented. These worksheets can also be used to determine who receives what menus and keys and who should belong to the HBHC MEDICAL FOSTER HOME mail group.

After Installation of patch HBH\*1\*24:

- Using FileMan, populate the MED FOSTER HOME SANCTION DATE field (#8) in the HBHC SYSTEM PARAMETERS FILE (#631.9) with the VACO approved sanction date. This field should be blank unless site receives official sanction date from VACO. The MFH functionality is dormant for sites without an approved MFH sanction status.
- Make sure you are assigned the HBHC MEDICAL FOSTER HOME key and the HBPC Information System Menu.
- Contact your local person who maintains the Hospital Location File (#44) Clinics to have MFH Clinics created. The HBPC primary stop codes (170-178) & also the MFH secondary stop code 162 (effective date 10/1/08) are to be utilized for the MFH clinics.
- Use the following options or ask the application coordinator for the package to enter all set up data in the program:
5.  Clinic File Data Entry.
6.  Team File Data Entry. Note: It is required that all providers for the program be assigned to a team.
7.  Provider File Data Entry.
- Assign menus and, where appropriate, keys to the users.
- Set the options Auto-queued Inspection/Training Reminder e-mail \[HBHC MFH AUTO-QUEUED REMINDERS\] and Auto-queued License Due Reminder e-mail \[HBHC MFH AUTO-Q LICENSE DUE\] to run on the 1<sup>st</sup> calendar day of each month, shortly after midnight.
- Assign file access per the HBPC Package Security Guide instructions99.
- Assign members to the HBHC MEDICAL FOSTER HOME mail group.
- Using FileMan, populate the Valid State Code file \#631.8 with any additional state codes that will be used by your site for MFH purposes.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Application Coordinator</td>
<td>Person responsible for the implementation, training, and troubleshooting of the software package, also acts as liaison between the HBPC Program personnel and IRM.</td>
</tr>
<tr class="even">
<td>Branching</td>
<td>Jumping from one spot to another when entering data. Branching determines which questions will be asked based on current values.</td>
</tr>
<tr class="odd">
<td>Case Manager</td>
<td>HBPC provider who is assigned responsibility for coordinating specific patient care.</td>
</tr>
<tr class="even">
<td>D/C</td>
<td>Discharge.</td>
</tr>
<tr class="odd">
<td>Default</td>
<td>The most probable answer to the field prompt. The value that appears between the field prompt and two slash marks (//). With the cursor resting next to the field prompt, you can either accept the default answer or enter your own answer. To accept the default, simply press the enter (or return) key. To change the default answer, type in your response.</td>
</tr>
<tr class="even">
<td>Device Prompt</td>
<td>A prompt at which you identify where you want to send your report output.</td>
</tr>
<tr class="odd">
<td>Double Quotes</td>
<td>The " symbol. Enclose patient name with double quotes to inform VA FileMan you wish to create an additional record with the same name as an existing record in the file. (e.g., "lastname,firstname"). This method is used to create additional episode of care records for a patient in the HBHC Patient file.</td>
</tr>
<tr class="even">
<td>Enter</td>
<td>Accept the entry or default response to a prompt. Symbolized by &lt;ENTER&gt; or &lt;RET&gt; in this manual.</td>
</tr>
<tr class="odd">
<td>Episode of Care</td>
<td>An admission to the HBPC Program begins an episode of care. The episode ends when the patient is discharged from the program. A complete episode of care must include an admission and a discharge or a reject.</td>
</tr>
<tr class="even">
<td>Field</td>
<td>In the computing environment, a field is similar to the blank space on a form. Field refers to one element of information (e.g., patient name).</td>
</tr>
<tr class="odd">
<td>Field Prompt</td>
<td>An online instruction that identifies the type of information you need to enter.</td>
</tr>
<tr class="even">
<td>File</td>
<td>A collection of related records treated as a unit.</td>
</tr>
<tr class="odd">
<td>Form 3</td>
<td>Evaluation/Admission data entry form.</td>
</tr>
<tr class="even">
<td>Form 4</td>
<td>Visit Log data entry form.</td>
</tr>
<tr class="odd">
<td>Form 5</td>
<td>Discharge data entry form.</td>
</tr>
<tr class="even">
<td>Form 6</td>
<td>Correction data entry form.</td>
</tr>
<tr class="odd">
<td>Form 7</td>
<td>Medical Foster Home transmit record type.</td>
</tr>
<tr class="even">
<td>Free Text</td>
<td>A data type that can contain any printable characters.</td>
</tr>
<tr class="odd">
<td>HBHC</td>
<td>Hospital Based Home Care.</td>
</tr>
<tr class="even">
<td>HBHC Provider file</td>
<td>File number 631.4, contains unique HBPC information pertaining to HBPC providers.</td>
</tr>
<tr class="odd">
<td>HBPC</td>
<td>Home Based Primary Care.</td>
</tr>
<tr class="even">
<td>Help</td>
<td>Assistance information which is available online. Enter 1 or 2 question marks at any field prompt to obtain help explaining what answer(s) the field prompt will accept. Enter 3 question marks at any “Select ... Option” prompt to obtain a description of the option.</td>
</tr>
<tr class="odd">
<td>IRM</td>
<td>Information Resources Management.</td>
</tr>
<tr class="even">
<td>Jump</td>
<td>Command that allows you to go from a particular field within a data entry option to another field within that same option.</td>
</tr>
<tr class="odd">
<td>Key</td>
<td>Special control that allows you to unlock and use options governing sensitive activities and information.</td>
</tr>
<tr class="even">
<td>Mail Group</td>
<td>A name assigned to a group of computer users. When you send a message to the group, each member of the mail group receives the message.</td>
</tr>
<tr class="odd">
<td>Medical Foster Home</td>
<td><p>Medical Foster Home (MFH) combines adult foster care in a</p>
<p>privately owned residence located in the community, with Home Based Primary Care (HBPC) or Spinal Cord Injury Home Care (SCI-HC). MFH offers a safe alternative to nursing home placement, merging personal care in a private home with medical &amp; rehabilitation support from specialized VA home care programs. Veterans placed in MFH meet nursing home admission criteria. Payment of MFH charges is the responsibility of the veteran.</p></td>
</tr>
<tr class="even">
<td>Menu</td>
<td>A list of options from which you can select an activity.</td>
</tr>
<tr class="odd">
<td>MFH</td>
<td>See Medical Foster Home</td>
</tr>
<tr class="even">
<td>Option</td>
<td>A computing activity that you can select from a menu.</td>
</tr>
<tr class="odd">
<td>Package</td>
<td>The set of programs, files, documentation, online help, and installation procedures that constitute a given software application.</td>
</tr>
<tr class="even">
<td>Parent Site</td>
<td>Selection from the MEDICAL CENTER DIVISION (#40.8) file defined at the VistA site level in option Systems Parameter Edit. Each patient and Medical Foster Home are affiliated to a parent site. If a parent site is not defined for a patient or Medical Foster Home because admission or definition occurred before the install of HBH*1.0*32, the value from the HOSPITAL NUMBER (#4) field in the HBHC SYSTEMS PARAMETER (#631.9) file is used for AITC transmissions and management reports.</td>
</tr>
<tr class="odd">
<td>Populate</td>
<td>To fill in a file with data.</td>
</tr>
<tr class="even">
<td>Prompt</td>
<td>A question or message from the computer requiring your response.</td>
</tr>
<tr class="odd">
<td>Queued</td>
<td>A task that is sent for processing in the background.</td>
</tr>
<tr class="even">
<td>Record</td>
<td>A collection of data items that refer to a specific entity (e.g., patient name, social security number, date of birth, all referring to the same patient).</td>
</tr>
<tr class="odd">
<td>Required Field</td>
<td>A mandatory field, one that must not remain blank.</td>
</tr>
<tr class="even">
<td>Return</td>
<td>On the computer keyboard, the key located where the carriage return is on a typewriter. Symbolized by &lt;RET&gt; in this manual .</td>
</tr>
<tr class="odd">
<td>Security Key</td>
<td>Special control that allows you to unlock and use options governing sensitive activities and information.</td>
</tr>
<tr class="even">
<td>Software</td>
<td>The set of programs that comprise the HBPC computer application.</td>
</tr>
<tr class="odd">
<td>Team</td>
<td>An interdisciplinary group of staff who care for a specific group of HBPC patients. Some HBPCs are composed of only one team; some have two teams, others three or more.</td>
</tr>
</tbody>
</table>
*(This page included for two-sided copying.)*
[^1]: Patch HBH\*1\*21 February 2005 – New option added to the Reports Menu
[^2]: Patch HBH\*1\*21 February 2005 – New option added to the Census Reports Menu
[^3]: Patch HBH\*1\*21 February 2005 – New option added to the Census Reports Menu
[^4]: Patch HBH\*1\*21 – New variable
[^5]: Patch HBH\*1\*21 – New variable
[^6]: Patch HBH\*1\*21 – New variable
