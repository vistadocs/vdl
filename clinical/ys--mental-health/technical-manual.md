---
title: Mental Health Assistant Phase 3 Security Technical Manual/Security Guide
doc_type: TM
doc_label: Technical Manual
doc_layer: plain
doc_subject: Mental Health Assistant Phase 3 Security /Security Guide
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: 
  - 200
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - class
  - blockquote
  - even
  - table
  - style
  - width
  - patient
  - contents
  - code
  - health
page_count: 0
word_count: 31928
section_count: 27
table_count: 8
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: May 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_mha_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_mha_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

Mental HealthAndMental Health Assistant Version 3

> ![](mental-health-assistant-phase-3-security-technical-manual-security-guide/001.png)

Technical Manual/Security GuideVersion 2.5March 2012Revised September 2021Department of Veterans AffairsOffice of Information and Technology (OIT)Product DevelopmentRevision History

<table style="width:100%;">
<caption>This table displays the document's revision history by date, version, change, project manager, and team</caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 28%" />
<col style="width: 23%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Change</strong></th>
<th><strong>Project Manager</strong></th>
<th><strong>Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sept. 2021</td>
<td>2.5</td>
<td>Patch YS*5.01*191: Informational patch for redactions and 508 comp.</td>
<td>CPRS Dev. Team</td>
<td>CPRS Dev. Team</td>
</tr>
<tr class="even">
<td>May 2021</td>
<td>2.4</td>
<td>Patch YS*5.01*170: Updated the OPTION file (#19) entry in the Mental Health Remote Procedure Context Option section. Made the “Routines Deleted by Mental Health Patch 60” table more readable.</td>
<td>CPRS Development Team</td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>Dec. 2020</td>
<td>2.3</td>
<td>Updated dates</td>
<td>REDACTED</td>
<td><p>Liberty IT Solutions</p>
<p>HI&amp;M Team</p></td>
</tr>
<tr class="even">
<td>Nov. 2020</td>
<td>2.2</td>
<td>Revised for grammar and spelling errors</td>
<td>VA</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Nov. 2020</td>
<td>2.1</td>
<td>Updated version for patch 149. Added Appendix B. Updated Remote Systems, Transmission Options, File Manager Access Codes, and sections and footers.</td>
<td>REDACTED</td>
<td><p>Liberty IT Solutions</p>
<p>HI&amp;M Team</p></td>
</tr>
<tr class="even">
<td>August 2020</td>
<td>2.0</td>
<td>Updated version for patch 166. Added DBIA #4480 to Mental Health File Relationships table.</td>
<td>REDACTED</td>
<td>Liberty ITS HI&amp;M Project Team</td>
</tr>
<tr class="odd">
<td>March 2020</td>
<td>1.9</td>
<td>Updated version for Patch 150</td>
<td>REDACTED</td>
<td>Booz Allen SPP Project Team</td>
</tr>
<tr class="even">
<td>June 2019</td>
<td>1.8</td>
<td>Updated version for Patch 145</td>
<td>REDACTED</td>
<td>Booz Allen SPP Project Team</td>
</tr>
<tr class="odd">
<td>May 2019</td>
<td>1.7</td>
<td>Updated version for Patch 147</td>
<td>REDACTED</td>
<td>Booz Allen SPP Project Team</td>
</tr>
<tr class="even">
<td>Feb. 2019</td>
<td>1.6</td>
<td>Updated version for Patches 138, 139</td>
<td>REDACTED</td>
<td>Booz Allen SPP Project Team</td>
</tr>
<tr class="odd">
<td>Sept. 2018</td>
<td>1.5</td>
<td>Updated version for Patch 136</td>
<td>REDACTED</td>
<td>Booz Allen SPP Project Team</td>
</tr>
<tr class="even">
<td>August 2018</td>
<td>1.4</td>
<td>Updated version numbers for Patch 134</td>
<td>REDACTED</td>
<td>Booz Allen SPP Project Team</td>
</tr>
<tr class="odd">
<td>March 2018</td>
<td>1.3</td>
<td>Updated Title and Footers;</td>
<td>REDACTED</td>
<td>Booz Allen SPP Project Team</td>
</tr>
<tr class="even">
<td>August 2014</td>
<td>1.2</td>
<td><p>Updated Title page</p>
<p>Updated Revision</p>
<p>History, p. i-ii</p>
<p>Updated Table of</p>
<p>Contents, pp. iii-iv</p>
<p>Changed ICD9 reference to ICD on page 19.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>29 Feb. 2012</td>
<td>1.1</td>
<td>Added table “MHA3 Patch YS*5.01*129 exports the following folders and files” to page 14</td>
<td>REDACTED</td>
<td><p>MHE-OM</p>
<p>Developer Team</p></td>
</tr>
<tr class="even">
<td>13 Feb. 2012</td>
<td>1.0</td>
<td>Removed “YS GAF Score Sent” from the mail group list. Final version. Peer review done and accepted</td>
<td>MHE-OM Team</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6 Feb. 2012</td>
<td>0.4</td>
<td>Uploaded to VA SharePoint for peer review</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>2 Feb. 2012</td>
<td>0.4</td>
<td>Content from Security Guide incorporated into document. Document renamed to reflect change.</td>
<td>REDACTED</td>
<td>MHE Developer Team</td>
</tr>
<tr class="odd">
<td>23 Jan. 2012</td>
<td>0.3</td>
<td>Updated by developers. Obsolete content deleted.</td>
<td>REDACTED</td>
<td>MHE Developer Team</td>
</tr>
<tr class="even">
<td>7 Jan. 2012</td>
<td>0.2</td>
<td>Format Changes</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7-Jul-11</td>
<td>0.1</td>
<td>Initial Draft</td>
<td>REDACTED</td>
<td>MHE-OM Team</td>
</tr>
</tbody>
</table>

This table displays the document's revision history by date, version, change, project manager, and team

(This page included for double-sided copying)

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
    - [Software and Manual Retrieval](#software-and-manual-retrieval)
    - [VistA Intranet](#vista-intranet)
    - [Screen Displays](#screen-displays)
- [Implementation & Maintenance](#implementation-maintenance)
  - [Minimum Requirements](#minimum-requirements)
  - [Routines and Checksums](#routines-and-checksums)
  - [Routine Descriptions](#routine-descriptions)
- [Files](#files)
  - [File Descriptions](#file-descriptions)
  - [VA File Manager Access Codes](#va-file-manager-access-codes)
  - [Pointer Relations](#pointer-relations)
- [Exported Options](#exported-options)
  - [Mental Health Menu Distributions](#mental-health-menu-distributions)
  - [Transmission Options \[YSCL HL7 MAIN\]](#transmission-options-yscl-hl7-main)
  - [Clinical Record \[YSCLINRECORD\]](#clinical-record-ysclinrecord)
  - [Seclusion/Restraint \[YSSR SEC/RES\]](#seclusionrestraint-yssr-secres)
  - [Seclusion/Restraint Report Utilities \[YSSR REPORTS\]](#seclusionrestraint-report-utilities-yssr-reports)
  - [Global Assessment of Functioning](#global-assessment-of-functioning)
  - [MHS Manager](#mhs-manager)
  - [Mental Health System Site Parameters](#mental-health-system-site-parameters)
  - [MHA2 Psych Test Utilities](#mha2-psych-test-utilities)
  - [Seclusion/Restraint Management Utilities](#seclusionrestraint-management-utilities)
  - [MHA3 Utilities](#mha3-utilities)
- [Menu Diagrams](#menu-diagrams)
- [Mental Health Protocols (File \#101)](#mental-health-protocols-file-101)
- [Remote Procedure Calls](#remote-procedure-calls)
- [Database Integration Agreements](#database-integration-agreements)
- [External Relations](#external-relations)
  - [Non-M Software Distributed with Mental Health Assistant 3 (MHA3)](#non-m-software-distributed-with-mental-health-assistant-3-mha3)
  - [MHA3 Server Options](#mha3-server-options)
  - [Remote Systems](#remote-systems)
- [Mental Health File Relationships](#mental-health-file-relationships)
- [Mental Health Mail Group File (#3.8) Entries](#mental-health-mail-group-file-38-entries)
- [Archiving](#archiving)
- [Package Security](#package-security)
  - [Security Keys (File \#19.1)](#security-keys-file-191)
- [Glossary](#glossary)
- [Abbreviations, Acronyms, and Descriptions](#abbreviations-acronyms-and-descriptions)
- [Appendix A](#appendix-a)
  - [Files Deleted by Mental Health Patch 60](#files-deleted-by-mental-health-patch-60)
  - [Options Deleted by Mental Health Patch 60](#options-deleted-by-mental-health-patch-60)
  - [Routines Deleted by Mental Health Patch 60](#routines-deleted-by-mental-health-patch-60)
- [Appendix B](#appendix-b)
  - [NCCC HL7 Message Specification](#nccc-hl7-message-specification)
    - [Conventions](#conventions)
    - [Network Connections](#network-connections)
    - [NCR Patient Registration Message: ADT^A28](#ncr-patient-registration-message-adta28)
    - [NCR Clozapine Dispense Message: RDE^O11](#ncr-clozapine-dispense-message-rdeo11)
The Mental Health Technical Manual V. 5.01 is designed as a reference manual to provide a technical description of the Mental Health package for the Department of Veterans Affairs Medical Center (VAMC) Information Resource Management Service (IRMS), Automated Data Processing Application Coordinators (ADPAC), and Clinical Coordinators. For more information regarding options and menus, please see the Mental Health User Manual V. 5.01.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health V. 5.01 package is designed to provide a means of rapidly gathering, storing, and reporting clinical information for patients receiving mental health treatment and /or assistance with vocational issues. The clinical information stored in the VistA database is readily accessible to clinical staff throughout the various Mental Health Treatment Service areas and other clinics in the Medical Center. It can also be sent to enterprise storage facilities such as the Austin Information Technology Center (AITC).

### Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software and documentation files are exported as part of Mental Health patch YS\*5.01\*150:

<table>
<caption>This table displays the exported files by file name and contents</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 45%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Contents</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS_501_150_IG.PDF</td>
<td><blockquote>
<p>YS_MHA3 Installation Guide</p>
</blockquote></td>
<td><blockquote>
<p>Binary</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YS_MHA3_UM.PDF</td>
<td><blockquote>
<p>YS_MHA3 User Manual</p>
</blockquote></td>
<td><blockquote>
<p>Binary</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YS_MHA3_TM.PDF</td>
<td><blockquote>
<p>YS_MHA3 Technical Manual /Security</p>
<p>Guide</p>
</blockquote></td>
<td><blockquote>
<p>Binary</p>
</blockquote></td>
</tr>
</tbody>
</table>

This table displays the exported files by file name and contents

The software files are available on the following OI Field Offices' \[ANONYMOUS.SOFTWARE\] directories. Use the following FTP address to connect to the first available FTP server: REDACTED

<table>
<caption>This table displays the offices by OI field office, FTP address, and directory</caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>OI FIELD OFFICE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FTP ADDRESS</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DIRECTORY</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

This table displays the offices by OI field office, FTP address, and directory

### VistA Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the Web sites listed below when you want to receive more background and technical information about the Mental Health package v 5.01, and to download this manual and related documentation.

Online Documentation for this product is available at: <u>http://www.va.gov/vdl/</u>. This website is the VistA Documentation Library (VDL), which has a listing of all the software manuals for VistA. Click on the Mental Health link, and it will take you to the Mental Health v 5.01 documentation.

### Screen Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing Mental Health package v 5.01, review this section to learn the many conventions used throughout this guide.

- Keyboard Responses: Keys provided in boldface, within the copy, help you quickly identify what to press on your keyboard to perform an action. For example, when you see enter in the copy, press this key on your keyboard.
- Screen Captures: Provide “shaded” examples of what you will see on your computer screen, and possible user responses. The computer dialogue appears in Courier font.
- Notes: Provided within the steps describe exceptions or special cases about the information presented. They reflect the experience of our staff, developers, and testers.
- Note: This *boxed* element highlights special details about the current topic.
- Other Names: File and field names, and Security keys provided in uppercase. For example, you may select a patient's name from the PATIENT file (#2).
- Menu Options: Provided in italics. For example, you may establish Electronic Signatures Codes using the Kernel Electronic Signature Code Edit \[XUSESIG\] option.

# Implementation & Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Minimum Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing Mental Health package v 5.01, make sure that your system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher).

<table>
<caption>This table displays the packages and versions by application name and minimum version needed. </caption>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Application Name</strong></th>
<th><blockquote>
<p><strong>Minimum Version Needed</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CPRS</td>
<td><blockquote>
<p>31 A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Clinical Reminders</td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RPC Broker</td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PIMS</td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td><blockquote>
<p>22.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Mailman</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

This table displays the packages and versions by application name and minimum version needed.

## Routines and Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Calculate and Show Checksum Values \[XTSUMBLD-CHECK\] menu option can be used as shown below to display a list of checksums for Mental Health package V. 5.01. The Mental Health routines are in the YS\* and YT\* namespaces.

Select Programmer Options Option: Calculate and Show Checksum Values

This option determines the current Old (CHECK^XTSUMBLD) or New

(CHECK1^XTSUMBLD) logic checksum of selected routine(s).

Select one of the following:

1.  Old
2.  New

New or Old Checksums: New// 2New New Checksum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1.  Any comment line with a single semi-colon is presumed to be followed by comments and only the line tag will be included.
2.  Line 2 will be excluded from the count.
3.  The total value of the routine is determined (excluding exceptions noted above) by multiplying the ASCII value of each character by its position on the line and position of the line in the routine being checked.

Select one of the following:

Package

Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: YS\*5.01\*150MENTAL HEALTH

YS150PST value = 9122642

YTQAPI2D value = 6639144

YTSACE value = 2551823

YTSBSL23 value = 3044905

YTSCMQ value = 2552097

YTSEAT26 value = 6312697

YTSFOCI value = 4656413

YTSMHRM value = 2499615

YTSNUDEC value = 13752134

YTSSIP30 value = 5052592

YTSSIPST value = 5906306

YTSSWEM value = 6610853

## Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain a brief description for all Mental Health routines, use the First Line Routine Print \[XU FIRST LINE PRINT\] menu option. Including the second line in the report will show which patches have made changes to the routine. This menu option is part of Programmer Options \[XUPROG\] on the Routine Tools \[XUPR-ROUTINE-TOOLS\] menu.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of the files exported with Mental Health package v. 5.01:

<table>
<caption>This table displays the exported files by file number, file name, and global</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 50%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Number</strong></th>
<th><blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Global</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>601</td>
<td><blockquote>
<p>MH Instrument</p>
</blockquote></td>
<td><blockquote>
<p>^YTT(601,</p>
</blockquote></td>
</tr>
<tr class="even">
<td>601.2</td>
<td><blockquote>
<p>PSYCH INSTRUMENT PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>^YTD(601.2,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>601.3</td>
<td>COPYRIGHT HOLDER</td>
<td>^YTT(601.3,</td>
</tr>
<tr class="even">
<td>601.4</td>
<td>INCOMPLETE PSYCH TEST PATIENT</td>
<td>^YTD(601.4,</td>
</tr>
<tr class="odd">
<td>601.6</td>
<td>MH MULTIPLE SCORING</td>
<td>^YTT(601.6,</td>
</tr>
<tr class="even">
<td>601.71</td>
<td>MH TESTS AND SURVEYS</td>
<td>^YTT(601.71,</td>
</tr>
<tr class="odd">
<td>601.72</td>
<td>MH QUESTIONS</td>
<td>^YTT(601.72,</td>
</tr>
<tr class="even">
<td>601.73</td>
<td>MH INTRODUCTIONS</td>
<td>^YTT(601.73,</td>
</tr>
<tr class="odd">
<td>601.74</td>
<td>MH RESPONSE TYPES</td>
<td>^YTT(601.74,</td>
</tr>
<tr class="even">
<td>601.75</td>
<td>MH CHOICES</td>
<td>^YTT(601.75,</td>
</tr>
<tr class="odd">
<td>601.751</td>
<td>MH CHOICETYPES</td>
<td>^YTT(601.751,</td>
</tr>
<tr class="even">
<td>601.76</td>
<td>MH INSTRUMENT CONTENT</td>
<td>^YTT(601.76,</td>
</tr>
<tr class="odd">
<td>601.77</td>
<td>MH BATTERIES</td>
<td>^YTT(601.77,</td>
</tr>
<tr class="even">
<td>601.78</td>
<td>MH BATTERY CONTENTS</td>
<td>^YTT(601.78,</td>
</tr>
<tr class="odd">
<td>601.781</td>
<td>MH BATTERY USERS</td>
<td>^YTT(601.781,</td>
</tr>
<tr class="even">
<td>601.79</td>
<td>MH SKIPPED QUESTIONS</td>
<td>^YTT(601.79,</td>
</tr>
<tr class="odd">
<td>601.81</td>
<td>MH SECTIONS</td>
<td>^YTT(601.81,</td>
</tr>
<tr class="even">
<td>601.82</td>
<td>MH RULES</td>
<td>^YTT(601.82,</td>
</tr>
<tr class="odd">
<td>601.83</td>
<td>MH INSTRUMENTRULES</td>
<td>^YTT(601.83,</td>
</tr>
<tr class="even">
<td>601.84</td>
<td>MH ADMINISTRATIONS</td>
<td>^YTT(601.84,</td>
</tr>
<tr class="odd">
<td>601.85</td>
<td>MH ANSWERS</td>
<td>^YTT(601.85,</td>
</tr>
<tr class="even">
<td>601.86</td>
<td>MH SCALEGROUPS</td>
<td>^YTT(601.86,</td>
</tr>
<tr class="odd">
<td>601.87</td>
<td>MH SCALES</td>
<td>^YTT(601.87,</td>
</tr>
<tr class="even">
<td>601.88</td>
<td>MH DISPLAY</td>
<td>^YTT(601.88,</td>
</tr>
<tr class="odd">
<td>601.89</td>
<td>MH CHOICEIDENTIFIERS</td>
<td>^YTT(601.89,</td>
</tr>
<tr class="even">
<td>601.91</td>
<td>MH SCORING KEYS</td>
<td>^YTT(601.91,</td>
</tr>
<tr class="odd">
<td>601.92</td>
<td>MH RESULTS</td>
<td>^YTT(601.92,</td>
</tr>
<tr class="even">
<td>601.93</td>
<td>MH REPORT</td>
<td>^YTT(601.93,</td>
</tr>
<tr class="odd">
<td>601.94</td>
<td>MH CR SCRATCH</td>
<td>^YTT(601.94,</td>
</tr>
<tr class="even">
<td>603.01</td>
<td>CLOZAPINE PATIENT LIST</td>
<td>^YSCL(603.01,</td>
</tr>
<tr class="odd">
<td>603.02</td>
<td>CLOZAPINE LAB TEST</td>
<td>^YSCL(603.02,</td>
</tr>
<tr class="even">
<td>603.03</td>
<td>CLOZAPINE PARAMETERS</td>
<td>^YSCL(603.03,</td>
</tr>
<tr class="odd">
<td>603.04</td>
<td>CLOZAPINE TESTS</td>
<td>^YSCL(603.04,</td>
</tr>
<tr class="even">
<td>603.05</td>
<td>CLOZAPINE HL7 TRANSMISSION</td>
<td>^YSCL(603.05,</td>
</tr>
<tr class="odd">
<td>604</td>
<td>ADDICTION SEVERITY INDEX</td>
<td>^YSTX(604,</td>
</tr>
<tr class="even">
<td>604.26</td>
<td>ASI PROGRAM TYPE</td>
<td>^YSTX(604.26,</td>
</tr>
<tr class="odd">
<td>604.3</td>
<td>ASI LEGAL CODE</td>
<td>^YSTX(604.3,</td>
</tr>
<tr class="even">
<td>604.4</td>
<td>ASI LIVING ARRANGEMENTS</td>
<td>^YSTX(604.4,</td>
</tr>
<tr class="odd">
<td>604.45</td>
<td>ASI PATIENT RATING SCALE</td>
<td>^YSTX(604.45,</td>
</tr>
<tr class="even">
<td>604.48</td>
<td>ASI ROUTE OF ADMINISTRATION</td>
<td>^YSTX(604.48,</td>
</tr>
<tr class="odd">
<td>604.5</td>
<td>ASI FAMILY HX CODES</td>
<td>^YSTX(604.5,</td>
</tr>
<tr class="even">
<td>604.55</td>
<td>ASI FOLLOW UP</td>
<td>^YSTX(604.55,</td>
</tr>
<tr class="odd">
<td>604.66</td>
<td>ASI QUICK FORM</td>
<td>^YSTX(604.66,</td>
</tr>
<tr class="even">
<td>604.68</td>
<td>ASI NARRATIVE</td>
<td>^YSTX(604.68,</td>
</tr>
<tr class="odd">
<td>604.77</td>
<td>ASI SUBSTANCE CODE</td>
<td>^YSTX(604.77,</td>
</tr>
<tr class="even">
<td>604.8</td>
<td>ASI PARAMETERS</td>
<td>^YSTX(604.8,</td>
</tr>
<tr class="odd">
<td>615.2</td>
<td>SECLUSION/RESTRAINT</td>
<td>^YS(615.2,</td>
</tr>
<tr class="even">
<td>615.5</td>
<td>S/R REASONS</td>
<td>^YSR(615.5,</td>
</tr>
<tr class="odd">
<td>615.6</td>
<td>S/R CATEGORY</td>
<td>^YSR(615.6,</td>
</tr>
<tr class="even">
<td>615.7</td>
<td>S/R RELEASE CRITERIA</td>
<td>^YSR(615.7,</td>
</tr>
<tr class="odd">
<td>615.8</td>
<td>S/R ALTERNATIVES</td>
<td>^YSR(615.8,</td>
</tr>
<tr class="even">
<td>615.9</td>
<td>S/R OBSERVATION CHECKLIST</td>
<td>^YSR(615.9,</td>
</tr>
<tr class="odd">
<td>627.7</td>
<td>DSM</td>
<td>^YSD(627.7,</td>
</tr>
<tr class="even">
<td>627.8</td>
<td>DIAGNOSTIC RESULTS MENTAL HEALTH</td>
<td>^YSD(627.8,</td>
</tr>
<tr class="odd">
<td>627.9</td>
<td>DSM MODIFIERS</td>
<td>^DIC(627.9,</td>
</tr>
</tbody>
</table>

This table displays the exported files by file number, file name, and global

## File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a complete description of each file and fields, use the List File Attributes \[DILIST\] option of the VA File Manager. See the list above for the file names and numbers.

## VA File Manager Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This list shows all Mental Health package files and their VA File Manager access codes:

YGO DD RD WR DEL LA

FILE NUMBER ACCESS ACCESS ACCESS ACCESS

ACCESS

-----------------------------------------------------------------------------

MH INSTRUMENT 601 @ Y y y y

PSYCH INSTRUMENT PATIENT 601.2. @ Y Y y Y

COPYRIGHT HOLDER 601.3. @ Y y y y

INCOMPLETE PSYCH TEST PATIENT 601.4. @ Y Y Y Y

MH MULTIPLE SCORING 601.6 @ @ @ @ @

MH TESTS AND SURVEYS 601.71 @ @ @ @ @

MH QUESTIONS 601.72 @ @ @ @ @

MH INTRODUCTIONS 601.73 @ @ @ @ @

MH RESPONSE TYPES 601.74 @ @ @ @ @

MH CHOICES 601.75 @ @ @ @ @

MH CHOICETYPES 601.751 @ @ @ @ @

MH INSTRUMENT CONTENT 601.76 @ @ @ @ @

MH BATTERIES 601.77 @ @ @ @ @

MH BATTERY CONTENTS 601.78 @ @ @ @ @

MH BATTERY USERS 601.781 @ @ @ @ @

MH SKIPPED QUESTIONS 601.79 @ @ @ @ @

MH SECTIONS 601.81 @ @ @ @ @

MH RULES 601.82 @ @ @ @ @

MH INSTRUMENTRULES 601.83 @ @ @ @ @

MH ADMINISTRATIONS 601.84 @ @ @ @ @

MH ANSWERS 601.85 @ @ @ @ @

MH SCALEGROUPS 601.86 @ @ @ @ @

MH SCALES 601.87 @ @ @ @ @

MH DISPLAY 601.88 @ @ @ @ @

MH CHOICEIDENTIFIERS 601.89 @ @ @ @ @

MH SCORING KEYS 601.91 @ @ @ @ @

MH RESULTS 601.92 @ @ @ @ @

MH REPORT 601.93 @ @ @ @ @

MH CR SCRATCH 601.94 @ @ @ @ @

CLOZAPINE PATIENT LIST 603.01 ----------------NONE--------------

CLOZAPINE LAB TEST 603.02 @ @ @ @ @

CLOZAPINE PARAMETERS 603.03 @ @ @ @ @

CLOZAPINE TESTS 603.04 ----------------NONE--------------

CLOZAPINE HL7 TRANSMISSION FILE 603.05 @ Y @ @ @

ADDICTION SEVERITY INDEX 604 ----------------NONE--------------

ASI PROGRAM TYPE 604.26 ----------------NONE--------------

ASI LEGAL CODE 604.3 ----------------NONE--------------

ASI LIVING ARRANGEMENTS 604.4 ----------------NONE--------------

ASI PATIENT RATING SCALE 604.45 ----------------NONE--------------

ASI ROUTE OF ADMINISTRATION 604.48 ----------------NONE--------------

ASI FAMILY HX CODES 604.5 ----------------NONE--------------

ASI FOLLOW UP 604.55 ----------------NONE--------------

ASI QUICK FORM 604.66 ----------------NONE--------------

ASI NARRATIVE 604.68 ----------------NONE--------------

ASI SUBSTANCE CODE 604.77 ----------------NONE--------------

ASI PARAMETERS 604.8 ----------------NONE--------------

SECLUSION/RESTRAINT 615.2. @ Y Y y Y

S/R REASONS 615.5. @ Y y y y

S/R CATEGORY 615.6. @ Y y y y

S/R RELEASE CRITERIA 615.7. @ Y y y y

S/R ALTERNATIVES 615.8. @ Y y y y

S/R OBSERVATION CHECKLIST 615.9. @ Y y y y

DSM 627.7 ----------------NONE--------------

DIAGNOSTIC RESULTS-MENTAL HEALTH 627.8. @ Y Y Y Y

DSM-III-R MODIFIERS 627.9. @ Y @ @ @

## Pointer Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Map Pointer Relations \[DI DDMAP\] option to create a visual representation of the file pointer relationships.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menu and options exported by the Mental Health package V. 5.01 are in the YS\* and YT\* namespaces. Individual options can be viewed by using the Kernel option XUINQUIRE (Inquire).

## Mental Health Menu Distributions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a display of the options in the Mental Health V. 5.01 package.

Mental Health \[YSUSER\] Menu

The Mental Health \[YSUSER\] menu is the Mental Health package primary menu. This menu contains two options.

After you select the Mental Health \[YSUSER\] menu, you will see a display similar to the one below. Assignment of privileges will determine what options are available for your use.

\*\* Mental Health version 5.01 \*\*

1 Clinical Record ...

6 Global Assessment of Functioning ...

Each of the options listed submenus that lead to other options and menus. These are described below.

> **NOTE:** Functionality within some options is controlled by security keys. See the Security Key section for a complete description of the keys.

## Transmission Options \[YSCL HL7 MAIN\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Clozapine HL7 Transmission Options, patient Clozapine pharmacy orders and Clozapine lab results are to be sent nightly to the National Clozapine Registry (NCR) via the scheduled Transmit Clozapine Rx HL7 Messages \[YSCL HL7 CLOZ TRANSMISSION\] option.

The Clozapine HL7 Transmission Options \[YSCL HL7 MAIN\] menu includes options that allow patient Clozapine HL7 pharmacy orders and Clozapine lab results to be manually sent or re-sent to the NCR database. Previously sent Clozapine HL7 messages may also be printed.

Options:

- Clozapine HL7 Messages Summary
- List of Clozapine Prescriptions
- Print HL7 Report by Date
- Queue Clozapine Rx HL7 Messages
- Retransmit Clozapine Rx HL7 Messages

## Clinical Record \[YSCLINRECORD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Record \[YSCLINRECORD\] menu includes options and menus that allow you to access and input patient data.

\*\*\* MENTAL HEALTH \*\*\*

CLINICAL RECORD

3 Diagnosis ...

13Seclusion/Restraint ...

Diagnosis \[YSDIAG\]

1.  Enter Diagnosis
2.  Print Diagnoses
3.  Print DXLS History

## Seclusion/Restraint \[YSSR SEC/RES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Seclusion/Restraint \[YSSR SEC/RES\] menu includes options for information regarding seclusion/restraint. If there are patients in the Seclusion /Restraint files, you will see the following heading above the menu.

The following patient(s) are currently listed as being in Seclusion/Restraint:

DATE & TIMETOTAL

PATIENT SSNINITIATEDORDERED BYTIME

================================================================================

YSPATIENT,ONExxxx\*JAN 21, 2012@14:42YSPROVIDER,ONE2400:7

\* Written order required.

1.  Entry of Patient to Seclusion/Restraint
2.  Release of Patient from Seclusion/Restraint
3.  Fifteen-Minute Check
4.  4 Seclusion/Restraint Report Utilities..

## Seclusion/Restraint Report Utilities \[YSSR REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Seclusion/Restraint Report Utilities \[YSSR REPORTS\] menu includes options to display Seclusion/Restraint information in various formats.

1.  MONTHLY..Monthly Report (VA Form 10-2683)
2.  PATIENT..S/R Mgmt Report by Patient Episode
3.  DATE.....S/R Mgmt Report by Date
4.  NURSING..S/R Mgmt Report by Nursing Shift
5.  REVIEW...S/R Mgmt Report of Review Actions

6 WARD.....S/R Mgmt Ward Report

## Global Assessment of Functioning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Global Assessment of Functioning \[YSGAF MAIN\] menu is the top menu to enter, graph and print GAF scores. These scores are equivalent to the DSM IV Axis 5 diagnosis.

1.  Enter GAF by Clinic Visit
2.  Print GAF's by Clinic/Date
3.  Single Patient GAF Entry
4.  Historical GAF listing
5.  Edit/mark errors on GAF

## MHS Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHS Manager \[YSMANAGER\] menu is exported with the Mental Health package; it is typically assigned to a user's secondary menu. This menu provides managerial utilities such as the Psychological Test Utilities that should be assigned only to individuals who are responsible for maintaining the Mental Health software.

\*\*\* MENTAL HEALTH \*\*\*

MHS MANAGER FUNCTIONS

2.  Mental Health System site parameters ...
3.  MHA2 Psych test utilities ...

5 Seclusion/Restraint Management Utilities ...

7 MHA3 Utilities ...

## Mental Health System Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health System site parameters \[YS SITE PARAMETERS\] menu includes options for use by the Mental Health Application Coordinator. Through it, site-specific files are maintained by the coordinator.

REASONS......Edit S/R Reasons File

CATEGORY.....Edit S/R Category File

RELEASE......Edit S/R Release Criteria File

ALTERNATIVES.Edit S/R Alternatives File

CHECKLIST....Edit S/R Checklist File

INSTRUMENT...Edit Instrument Restart Day Limit

## MHA2 Psych Test Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHA2 Psych test utilities \[YSUTIL\] menu includes options to access the psych testing utilities options. This is a legacy option and does not affect MHA3.

\*\*\* LEGACY Mental Health \*\*\*

MHA2 Utilities

2.  Audit test/interview data
3.  Check Psych Data Base
6.  Delete Patient Data
7.  Print test/interview items
8.  Delete incomplete tests/interviews

## Seclusion/Restraint Management Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Seclusion/Restraint Management Utilities \[YSSR MGT UTILITY\] menu contains options required for the management of the Seclusion/Restraint features.

MHS Manager Functions

1.  Review of Seclusion/Restraint Action
2.  Written Order Edit
3.  Edit Seclusion/Restraint Entry
4.  Delete Seclusion/Restraint Entry

## MHA3 Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHA3 Utilities \[YTQ MHA3 MENU\] menu includes options for MHA3 settings and utilities.

\*\*\* Mental Health \*\*\*

MHA3 Utilities

1.  Print Test Form
2.  Detailed Definition
3.  Delete Patient Data
4.  Stop/Re-Start Progress Notes for an Instrument
5.  Exempt Test
6.  Test Usage
7.  XML Output
8.  Instrument Exchange

# Menu Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options comprising the Mental Health package are arranged on menus according to functionality.

The Mental Health \[YSUSER\] option is used by most Mental Health package users. The MHS Manager \[YSMANAGER\] menu is for supervisors. Use the Menu Diagrams \[XQDIAGMENU\] option to create a visual representation of the menu structure.

# Mental Health Protocols (File \#101)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS GAFYS GAF A08 SERVERYS GAF A08 CLIENTYS GAF A08 CLENT

YS MHA A08 CLIENTYS MHA A08 CLIENT

YS MHA A08 EVENT

Used by List Manager for Exchange Utility --

YTXCHG BROWSE SPEC Browse Specification

YTXCHG CREATE ENTRY Create New Entry

YTXCHG DELETE ENTRY Delete Entry

YTXCHG DRYRUN Trial Install \<Dry Run\>

YTXCHG INSTALL Install Exchange Entry

YTXCHG LOAD HOST Load Host File

YTXCHG LOAD URL Load from URL

YTXCHG MAIN MENU Instrument Exchange Menu

YTXCHG REBUILD ENTRY Rebuild Entry

YTXCHG SAVE HOST Create Host File

# Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health V. 5.01 Remote Procedure Calls (RPC’S) are in the YS\* and YT\* namespaces. Use the FileMan Print functionality to find and display the entries in the REMOTE PROCEDURE file (#8994).

# Database Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view the details of a Database Integration Agreements (DBIA) use the VA Forum option “Inquire to an Integration Control Registration” to display the DBIAS where the Mental Health package is the custodial or the subscribing package.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Mental Health Assistant (MHA) is the graphical user interface (GUI) for the VistA Mental Health package. MHA was developed to create an effective and efficient tool for all clinicians and their patients to use for the administration and scoring of assessment instruments and interviews. Additionally, results are displayed in report and graphical formats. MHA supports mental health assessments (e.g., psychological testing, structured interviews, questionnaires, etc.) that are not available elsewhere in the Computerized Patient Record System (CPRS)/Veterans Information System and Technology Architecture (VistA).

To better meet the needs of clinicians and patients in different treatment programs, particularly in nontraditional settings, MHA can now be run in a standalone mode to administer instruments offline for later uploading to Vista. For detailed instructions and requirements installing and implementing the MHA Graphical User Interface (GUI) software application, see the MHA3 Installation Guide.

## Non-M Software Distributed with Mental Health Assistant 3 (MHA3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here are typical examples of the storage locations for the MHA3 files (executable, DLL and other supporting files) installed on a workstation:

C:\Program Files\Vista\YS\MHA3

YS_MHA.exe (From Patch YS\*5.01\*123)

YS_MHA.HLP (From Patch YS\*5.01\*85)

YS_MHA.JCF (From Patch YS\*5.01\*85)

Borlndmm.dll (From Patch YS\*5.01\*123) Uninst000.dat uninst000.exe

C:\Program Files\Vista\Common Files

YS_MHA_A.dll

YS_MHA_AUX.dll

MHA3 Patch YS\*5.01\*150 exports the following folders and files:

<table>
<caption>This table displays the folders and files by the file names, contents, and retrieval formats</caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 49%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FILE NAMES</strong></th>
<th><strong>CONTENTS</strong></th>
<th><blockquote>
<p><strong>RETRIEVAL FORMATS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS_501_150_IG.pdf</td>
<td><blockquote>
<p>Mental Health Assistant Version 3 (MHA3) Installation Guide Patch YS*5.01*150</p>
</blockquote></td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YS_MHA3_UM.pdf</td>
<td><blockquote>
<p>Mental Health Assistant Version 3 (MHA3) User Manual Patch YS*5.01*150</p>
</blockquote></td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YS_MHA3_TM.pdf</td>
<td><blockquote>
<p>Mental Health Assistant Version 3 (MHA3) Technical Manual Patch YS*5.01*150</p>
</blockquote></td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
</tbody>
</table>

This table displays the folders and files by the file names, contents, and retrieval formats

Mental Health Remote Procedure Context Option

The OPTION file (#19) entry “YS BROKER1 version 1.0.3.85~1.0.5.11~1.0.3.86” \[YS BROKER1\] provides the context necessary to interface the V*ist*A Mental Health Assistant Version 3 application to the VistA database via Remote Procedure Calls (RPC).

## MHA3 Server Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The server options being used in the Mental Health package V. 5.01:

Clozapine Data Server \[YSCLSERVER\]

DESCRIPTION: This is a server to allow the National Clozapine Coordinating Center (NCCC) in Dallas to authorize Clozapine registration numbers for use at individual sites.

ROUTINE: YSCLSERV SERVER ACTION: RUN IMMEDIATELY

Mental Health Test Usage Server \[YS TEST USAGE\]

DESCRIPTION: Used by the National Mental Health Strategic Healthcare Group to determine the annual psychological test usage by site. This option reports the number of each test by station within any given time period.

The MAILMAN message must be in FILEMAN date format 3031001^3040930

ROUTINE: YSTUSESERVER ACTION: RUN IMMEDIATELY

Server test usage MHA3 stats \[YTQTUSE\]

DESCRIPTION: \*\*\* MHA3 \*\*\* Used by the National Mental Health Strategic Healthcare Group to determine the annual psychological test usage by site. This option reports the number of each test by station within any given time period.

The MAILMAN message must be in FILEMAN date format 3031001^3040930

ROUTINE: YTQTUSESERVER ACTION: RUN IMMEDIATELY

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All Global Assessment of Functioning (GAF) scores entered through the Mental Health GAF form are dynamically sent to the National Patient Care Database (NPCD) at the Austin Information Technology Center (AITC).

Mental Health Entries in the HL LOGICAL LINK file (#870):

YS GAF-SND

LLP TYPE: MAILMAN

DEVICE TYPE: N

TIME STOPPED: MAR 16, 2011@15:49:59

SHUTDOWN LLP? YES

MESSAGE NUMBER: 1

STATUS: PENDING

NODE: YSCL-NCCC

LLP TYPE: TCP

QUEUE SIZE: 10

DESCRIPTION: This is the logical link for the National Clozapine Registry NCR). The NCR is maintained by the National Clozapine Coordinating Center NCCC).

Mental Health entries in the HL7 APPLICATION PARAMETER file (#771):

NAME: YS GAF

ACTIVE/INACTIVE: ACTIVE

MAIL GROUP: YS GAF TO NPCD

COUNTRY CODE: USA

NAME: YS MHA

ACTIVE/INACTIVE: ACTIVE

MAIL GROUP: YS MHA-MHNDB

COUNTRY CODE: USA

HL7 ENCODING CHARACTERS: ~^\\

HL7 FIELD SEPARATOR: \|

HL7 MESSAGE: ADT

PROCESSING ROUTINE: ACKMHA^YTQHL7

HL7 SEGMENT: PID

FIELDS USED IN THIS SEGMENT: 1,2

HL7 SEGMENT: MSH

FIELDS USED IN THIS SEGMENT: 1

HL7 SEGMENT: MSA

FIELDS USED IN THIS SEGMENT: 1,3,7,8,9,10

Mental Health entries in the HLO APPLICATION REGISTRY file (#779.2):

APPLICATION NAME: YSCL-REG-REC

HL7 MESSAGE TYPE: ADT

HL7 EVENT: A28

ACTION TAG: ACCEPTAR

ACTION ROUTINE: YSCLHLAD

HL7 VERSION: 2.5.1

MINIMUM RETENTION TIME: 10

HL7 MESSAGE TYPE: RDE

HL7 EVENT: O11

ACTION TAG: ACCEPTAR

ACTION ROUTINE: YSCLHLAD

HL7 VERSION: 2.5.1

MINIMUM RETENTION TIME: 10

Package File Link: MENTAL HEALTH

APPLICATION NAME: YSCL-REG-SEND

HL7 MESSAGE TYPE: ADT

HL7 EVENT: A28

ACTION TAG: ACCEPTAR

ACTION ROUTINE: YSCLHLAD

HL7 VERSION: 2.5.1

MINIMUM RETENTION TIME: 10

HL7 MESSAGE TYPE: RDE

HL7 EVENT: O11

ACTION TAG: ACCEPTAR

ACTION ROUTINE: YSCLHLAD

HL7 VERSION: 2.5.1

MINIMUM RETENTION TIME: 10

Package File Link: MENTAL HEALTH

# Mental Health File Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Files accessed by the Mental Health package V. 5.01:

<table>
<caption>This table displays the accessed files by the file number, file name, package, and agreement status</caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 31%" />
<col style="width: 21%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File #</strong></th>
<th><blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Agreement Status</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.5</td>
<td>FUNCTION file</td>
<td><blockquote>
<p>KERNEL</p>
</blockquote></td>
<td><blockquote>
<p>Supported reference</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>PATIENT file</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>Read Only, Supported reference &amp; DBIA #87</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3.1</td>
<td><blockquote>
<p>TITLE file</p>
</blockquote></td>
<td><blockquote>
<p>KERNEL</p>
</blockquote></td>
<td><blockquote>
<p>Pointed to by File #200, Read only Reference</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>INSTITUTION file</p>
</blockquote></td>
<td><blockquote>
<p>KERNEL</p>
</blockquote></td>
<td><blockquote>
<p>Supported reference, Read only</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>STATE file</p>
</blockquote></td>
<td><blockquote>
<p>KERNEL</p>
</blockquote></td>
<td><blockquote>
<p>Supported reference, Read only</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>ELIGIBILITY CODE</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #87</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>RELIGION</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="even">
<td>19.1</td>
<td><blockquote>
<p>SECURITY KEY</p>
</blockquote></td>
<td><blockquote>
<p>MENU DRIVER</p>
</blockquote></td>
<td><blockquote>
<p>Supported reference</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>22</td>
<td><blockquote>
<p>POW PERIOD</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="even">
<td>23</td>
<td><blockquote>
<p>BRANCH OF SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>24</td>
<td><blockquote>
<p>NON-VETERAN CLASS</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="even">
<td>25</td>
<td><blockquote>
<p>TYPE OF DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>31</td>
<td><blockquote>
<p>DISABILITY CONDITION</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="even">
<td>35</td>
<td><blockquote>
<p>OTHER FEDERAL AGENCY</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>36</td>
<td><blockquote>
<p>INSURANCE COMPANY</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="even">
<td>37</td>
<td><blockquote>
<p>DEPOSITION</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>41.1</td>
<td><blockquote>
<p>SCHEDULED ADMISSION</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA#87</p>
</blockquote></td>
</tr>
<tr class="even">
<td>41.9</td>
<td><blockquote>
<p>CENSUS file</p>
</blockquote></td>
<td><blockquote>
<p>SCHEDULING</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #47</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>42</td>
<td><blockquote>
<p>WARD LOCATION file</p>
</blockquote></td>
<td><blockquote>
<p>SCHEDULING</p>
</blockquote></td>
<td><blockquote>
<p>Support reference, Read only</p>
</blockquote></td>
</tr>
<tr class="even">
<td>42.4</td>
<td><blockquote>
<p>SPECIALITY file</p>
</blockquote></td>
<td><blockquote>
<p>REGISTRATION</p>
</blockquote></td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>44</p>
</blockquote></td>
<td><blockquote>
<p>HOSPITAL LOCATION</p>
</blockquote></td>
<td>SCHEDULING</td>
<td><blockquote>
<p>Support reference, Read only</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>45</p>
</blockquote></td>
<td><blockquote>
<p>PTF (Patient Treatment file)</p>
</blockquote></td>
<td>DRG GROUPER REGISTRATION</td>
<td><blockquote>
<p>DBIA #27 &amp; #87<br />
Support reference</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>45.7</p>
</blockquote></td>
<td><blockquote>
<p>TREATING SPECIALTY file</p>
</blockquote></td>
<td>REGISTRATION</td>
<td><blockquote>
<p>DBIA #277</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td><blockquote>
<p>DRUG file</p>
</blockquote></td>
<td>OUTPATIENT PHARMACY</td>
<td><blockquote>
<p>DBIA #221</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>52</p>
</blockquote></td>
<td><blockquote>
<p>PRESCRIPTION file</p>
</blockquote></td>
<td>OUTPATIENT PHARMAHCY</td>
<td><blockquote>
<p>DBIA #276</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>52.5</p>
</blockquote></td>
<td><blockquote>
<p>RX SUSPENSE file</p>
</blockquote></td>
<td>OUTPATIENT PHARMACY</td>
<td><blockquote>
<p>DBIA #276</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>55</p>
</blockquote></td>
<td><blockquote>
<p>PHARMACY PATIENT file</p>
</blockquote></td>
<td>OUTPATIENT PHARMACY</td>
<td><blockquote>
<p>DBIA #276<br />
DBIA #4480</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ICD DIAGNOSIS file</p>
</blockquote></td>
<td>DRG</td>
<td><blockquote>
<p>Support reference, Read only</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>80.1</p>
</blockquote></td>
<td><blockquote>
<p>ICD OPERATION / PROCEDURE</p>
</blockquote></td>
<td>DRG</td>
<td><blockquote>
<p>Support reference, Read only</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON file</p>
</blockquote></td>
<td>KERNEL</td>
<td><blockquote>
<p>Support reference</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>211.6</p>
</blockquote></td>
<td><blockquote>
<p>NURSTOUR of DUTY file</p>
</blockquote></td>
<td>NURSING</td>
<td><blockquote>
<p>DBIA #278</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>405</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT MOVEMENT</p>
</blockquote></td>
<td>PIMS</td>
<td><blockquote>
<p>Support reference</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>801.41</p>
</blockquote></td>
<td><blockquote>
<p>REMINDER DIALOG</p>
</blockquote></td>
<td>Clinical Reminders</td>
<td><blockquote>
<p>Supported reference</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>801.43</p>
</blockquote></td>
<td><blockquote>
<p>REMINDER FINDING ITEM PARAMETER</p>
</blockquote></td>
<td>Clinical Reminders</td>
<td><blockquote>
<p>Supported reference</p>
</blockquote></td>
</tr>
</tbody>
</table>

This table displays the accessed files by the file number, file name, package, and agreement status

# Mental Health Mail Group File (#3.8) Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS ASI PERFORMANCE MEASURES - Members of this mail group will be used to receive the ASI Case Finder Report.

YS GAF TO NPCD - This mail group is being used by Mental Health to transmit data to the National Patient Care Database via HL7.

REMOTE MEMBER: XXX@Q-NPT.MED.VA.GOV

YS GAF TRANSMISSION ACK - This mail group will receive a message when a GAF score is transmitted to the National Patient Care Database or an error in the transmission has occurred.

YS MHA-MHNDB - This group receives error messages from the HL7 system when problems arise, sending messages to the Mental Health National database.

YS PSYCHTEST - Used to notify clinicians when tests and interviews are administered to patients at the requests of someone other than the person administering the test.

YSCLHL7 LOGS – This Mail Group is used for the receipt of mail messages that are created to log the transmission of HL7 messages for Clozapine patients.

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data archiving capabilities are not currently available for the Mental Health package.

# Package Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security in this package is controlled almost exclusively by the menu option that is assigned to a person.

Deletion of entries in many Mental Health files is prohibited under ordinary conditions.

## Security Keys (File \#19.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Allocate the following security keys to appropriate site personnel:

Name DescriptionYSCL AUTHORIZED - The presence of this key designates an authorized Clozapine Provider.

YSD - Allows verification of ICD diagnoses. This is a clinical privilege. The chief of psychiatry will determine who may have this key.

YSP - Provides access to psychological test options. The Chief of

Psychology Service will determine who may have this key.

YSQ - Allows verification of DSM-III diagnoses. The Chiefs of

Clinical Services will determine who may have this key.

YSZ - Allows Mental Health technicians/aides to queue tests/interviews after completion.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary contains definition of terms and abbreviations that may not be familiar to all users. Basic terms, acronyms, and phrases that are used throughout the Vista environment are included.
<table>
<caption>This table displays the terms and abbreviations by the term and definition</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>@</td>
<td><blockquote>
<p>The at symbol (@) is used to delete an entry in a FileMan file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ADT</td>
<td><blockquote>
<p>ADMISSIONS DISCHARGES, and TRANSFERS (part of the PIMS package).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ABBREVIATED RESPONSE</td>
<td><blockquote>
<p>Data entry by typing only the first few characters for the desired response. This feature will not work unless the information is already stored in the computer.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>AXIS 4</td>
<td><blockquote>
<p>A numeric representation of the severity of psychological stressors.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>AXIS 5</td>
<td><blockquote>
<p>A numeric representation of the global assessment of functioning.<br />
AXIS 5 is a clinician’s overall judgment of a patient’s social/psychological and occupational functioning on a continuum of mental health-illness.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CRISIS NOTES</td>
<td><blockquote>
<p>A note containing patient information that displays automatically wherever the patient’s name is entered into the system.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>CROSS-</p>
<p>REFERENCE</p></td>
<td><blockquote>
<p>An index of file entries. For a description see the VA File Manager documentation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DEFAULT</td>
<td><blockquote>
<p>A response the considered the most probable answer to the prompt being displayed. A default is identified by two slash marks (//) immediately following the computer-displayed response. You may accept the default answer by pressing the ENTER (or RETURN) key. To change the default answer, type in your response.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DELETE</td>
<td><blockquote>
<p>The key on your keyboard that enables deletion of individual characters. Place the CURSOR immediately after the last character of the string of characters you wish to delete and press the DELETE or RUBOUT key.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DRG</td>
<td><blockquote>
<p>DIAGNOSIS RELATED GROUP is a prospective payment system, based on a complex set of criteria, which established a reimbursement fee determined by the primary diagnosis. Each diagnosis is assigned a DRG number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DUZ</td>
<td>A user identification number assigned by Vista. It is the IEN of the NEW PERSON file (#200).</td>
</tr>
<tr class="even">
<td>DX</td>
<td>Diagnosis.</td>
</tr>
<tr class="odd">
<td>DXLS</td>
<td>Diagnosis Length of Stay. The diagnosis most responsible for the patient’s length of stay during the current admission.</td>
</tr>
<tr class="even">
<td>ENTER</td>
<td>Press the RETURN or ENTER key to instruct the system to store the information you just entered.</td>
</tr>
<tr class="odd">
<td>FIELD</td>
<td>A FIELD is similar to questions on a questionnaire. It is a statement that requests information. Your response is the value entered into that field. For example, the prompt, “DOB” is a field in which you enter your birth date.</td>
</tr>
<tr class="even">
<td>GLOBAL VARIABLE</td>
<td>Usually referred to as a global. A disc-resident structure (e.g. ^YTT(601), used to store data in the VistA database.</td>
</tr>
<tr class="odd">
<td>HELP</td>
<td>Assistance displayed on your terminal screen. The HELP function displays menus and describes options. To obtain HELP, enter 1-4 question marks in response to a prompt. The level of help you receive increases with the number of question marks you enter.</td>
</tr>
<tr class="even">
<td>IEN</td>
<td>The INTERNAL ENTRY NUMBER of a record in a File Manager file.</td>
</tr>
<tr class="odd">
<td>KERNEL</td>
<td>The VA kernel is the software suite that integrates the operating system with other software applications such as Mental Health, Laboratory, and Pharmacy.</td>
</tr>
<tr class="even">
<td>LOS</td>
<td>Length of stay.</td>
</tr>
<tr class="odd">
<td>LEVEL</td>
<td>Patients are assigned a LEVEL, a scaled position. The definition of each level is up to the local station. For example, a level 1 patent may require staff supervision when involved in off-ward activities, whereas a level 2 patient may leave the ward when accompanied by a level 3 patient.</td>
</tr>
<tr class="even">
<td>MASTER<br />
TREATMENT<br />
PLAN</td>
<td>The comprehensive Treatment Plan for the TREATMENT of an individual patient during each hospitalization. The plan is reviewed at regular intervals and adjusted to accommodate the needs of the patient.</td>
</tr>
<tr class="odd">
<td>MH</td>
<td>Mental Health</td>
</tr>
<tr class="even">
<td>MENU</td>
<td>A list of options that may include submenus or options.</td>
</tr>
<tr class="odd">
<td>NOK</td>
<td>Next of kin.</td>
</tr>
<tr class="even">
<td>ONSET</td>
<td>The beginning of a symptom or disease.</td>
</tr>
<tr class="odd">
<td>OPTION NAME</td>
<td>The formal name of an option. By convention, it is displayed in brackets and is the .01 field of the OPTION file (#19).</td>
</tr>
<tr class="even">
<td>PATIENT MESSAGE</td>
<td>Information concerning a patient that is not part of the permanent clinical record. If a message has been entered for a patient, a notation indicating that a PATIENT MESSAGE exists is displayed every time the patient’s name is entered into the system. A Patient Message may be transferred to a Progress Note where, it becomes part of the permanent clinical record.</td>
</tr>
<tr class="odd">
<td>PRIMARY</td>
<td>The condition that is chiefly responsible for the DIAGNOSIS the patient’s treatment.</td>
</tr>
<tr class="even">
<td>PRIORITY CATEGORY</td>
<td>Codes used to denote the order in which a patient’s acceptance into a program or clinic is determined.</td>
</tr>
<tr class="odd">
<td>PROGRESS NOTES</td>
<td>A note containing information concerning a patient. There are numerous kinds of progress notes such as admission, discharge, pre-operative, social work, nursing, etc. A progress note is included in the patient’s permanent clinical record.</td>
</tr>
<tr class="even">
<td>PSYCHOSIS</td>
<td>Gross impairment in reality testing.</td>
</tr>
<tr class="odd">
<td>PROMPT</td>
<td>The system interacts with the user by issuing questions and statements called PROMPTS, and the user enters a response.</td>
</tr>
<tr class="even">
<td>SIGNATURE BLOCK</td>
<td>Used with electronic signatures. A SIGNATURE BLOCK indicates the author’s complete name and title.</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>Social Security Number.</td>
</tr>
<tr class="even">
<td>TEAM</td>
<td>An organizational sub-unit of a ward which is often composed of residents, medical students, psychologists, social workers, nurses, etc.</td>
</tr>
<tr class="odd">
<td>VA FileManager</td>
<td>The Database Management System (DBMS) used by Vista. It is often referred to as FileMan.</td>
</tr>
<tr class="even">
<td>VERIFY CODE</td>
<td>An additional security precaution used in conjunction with ACCESS CODE. Like the access code, it is also 6-11 digits in length and if entered incorrectly, the user is not allowed access to the computer. Both codes are invisible on the terminal screen to provide user-protection.</td>
</tr>
</tbody>
</table>
This table displays the terms and abbreviations by the term and definition

# Abbreviations, Acronyms, and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>This table displays abbreviations and acronyms by the abbreviation or acronym and the description</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Abbreviation or Acronym</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>API</p>
</blockquote></td>
<td><blockquote>
<p>Application Programmer Interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AITC</p>
</blockquote></td>
<td><blockquote>
<p>Austin Information Technology Center</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ARTS</p>
</blockquote></td>
<td><blockquote>
<p>Adverse Reaction Tracking</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DBMS</p>
</blockquote></td>
<td><blockquote>
<p>Database Management System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DFN</p>
</blockquote></td>
<td><blockquote>
<p>Internal entry number of a record in the PATIENT file (#2). DFN is the name of a local variable.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DVA</p>
</blockquote></td>
<td><blockquote>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FDA</p>
</blockquote></td>
<td><blockquote>
<p>Food and Drug Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GUI</p>
</blockquote></td>
<td><blockquote>
<p>Graphical User Interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HL7</p>
</blockquote></td>
<td><blockquote>
<p>Health Level 7 (a data-transmission protocol).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HSD&amp;D</p>
</blockquote></td>
<td><blockquote>
<p>Health System Design and Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td><blockquote>
<p>Integration Control Number, or national VA patient record number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td><blockquote>
<p>Internal Entry Number (of a record in a FileMan file).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IMG</p>
</blockquote></td>
<td><blockquote>
<p>Information Management Group</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IRM</p>
</blockquote></td>
<td><blockquote>
<p>Information Resource Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KIDS</p>
</blockquote></td>
<td><blockquote>
<p>Kernel Installation and Distribution System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>Alternate name for MUMPS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MHA</p>
</blockquote></td>
<td><blockquote>
<p>Mental Health Assistant</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MUMPS</p>
</blockquote></td>
<td><blockquote>
<p>Massachusetts General Hospital Utility Multiprogramming System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OINT</p>
</blockquote></td>
<td><blockquote>
<p>Office of Information National Training and Education Office</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PCE</p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Encounter</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PIMS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Information Management Systems</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PMO</p>
</blockquote></td>
<td><blockquote>
<p>Project Management Office</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PTF</p>
</blockquote></td>
<td><blockquote>
<p>Patient Treatment File</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>System Implementation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SPP</p>
</blockquote></td>
<td><blockquote>
<p>Suicide Prevention Project</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Department of Veteran Affairs</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VERA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Equitable Resource Allocation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VHA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
</tbody>
</table>

This table displays abbreviations and acronyms by the abbreviation or acronym and the description

# Appendix A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health package contains a number of software elements that were deprecated (marked as obsolescent) in 2004 or earlier. These software components are deleted or disabled in Mental Health Patch 60 (YS\*5.01\*60). The following is a description of those items which will become obsolete with the release of Patch 60.

The obsolete software may contain scoring algorithms that are no longer correct, outdated data structures, and code that doesn’t meet current VA software standards and conventions.

## Files Deleted by Mental Health Patch 60

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|  File Name           | File \# | Global Location |
|----------------------|---------|-----------------|
| MEDICAL RECORD       | 90      | ^MR(            |
| PT. TEXT             | 99      | ^PTX(           |
| CRISIS NOTE DISPLAY  | 600.7   | ^YSG("CNT",     |
| MH TEXT              | 605     | ^YTX(           |
| MH CLINICAL FILE     | 615     | ^YS(615,        |
| MH WAIT LIST         | 617     | ^YSG("WAIT",    |
| MENTAL HEALTH CENSUS | 618     | ^YSG("CEN",     |
| MENTAL HEALTH TEAM   | 618.2   | ^YSG("SUB",     |
| MENTAL HEALTH INPT   | 618.4   | ^YSG("INP",     |
| PROBLEM              | 620     | ^DIC(620,       |
| JOB BANK             | 624     | ^YSG("JOB",     |
| INDICATOR            | 625     | ^DIC(625,       |
| DSM3                 | 627     | ^DIC(627,       |
| DSM-III-R            | 627.5   | ^DIC(627.5,     |
| DSM CONVERSION       | 627.99  | ^YSD(627.99,    |
| YSEXPERT             | 628     | ^YS(628,        |

This table displays the deleted files by file name, file number, and global location

## Options Deleted by Mental Health Patch 60

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  YS SITE-FILE 16 - SIGNATURE....Edit Signature Block Title
2.  YS SITE-FILE 602 TEST LIM - INSTRUMENT...Edit Instrument Restart Day Limit
3.  YS SITE-FILE 602 WWU - WWU..........Edit Weighted Work Unit (WWU)
4.  YSADMTEST - Psychological tests/interviews (administer)
5.  YSAPROB - Add a new problem
6.  YSAS CASE FINDER - ASI Case Finder
7.  YSAS FOLLOWUP FINDER - ASI Followup Finder
8.  YSCENCAD - Cancel a MH Census Discharge
9.  YSCENCL - Custom List
10. YSCENCRISIS - Crisis notes and Messages
11. YSCENDAYHX - Previous Admissions by Date
12. YSCENDCDOC - Discharge Comments Entry
13. YSCENDIA - Active Diagnoses
14. YSCENED - Enter/Edit Current Inpatient Data
15. YSCENEDM - Enter/Edit MH Inpatient Data
16. YSCENFS - Census
17. YSCENGED - Group Data Entry/Edit
18. YSCENIL - Individual Patient List
19. YSCENLOS - Current Inpatient Days
20. YSCENMAIN - Inpatient Features
21. YSCENMEDS - Outpatient Medications
22. YSCENMGR - Inpatient Features management functions
23. YSCENNAM - Name Search
24. YSCENNEW - Recent Admissions
25. YSCENPAHX - Individual Data Look Up
26. YSCENPASS - Pass/Last Transfer List
27. YSCENPL - Patient Lists
28. YSCENPP - Patient Profile Data
29. YSCENREM - Graph of Patients Remaining
30. YSCENROT - Rotation of Teams31. YSCENSL - Short Patient List
32. YSCENSUBUP - Team Definition
33. YSCENTAH - Team Admissions Record
34. YSCENTCEN - Team Census
35. YSCENTESTING - Psychological Tests and Interviews
36. YSCENTMHX - Ward/Team History - LOS, DRG and DXLS
37. YSCENTPTE - Treatment Plan Tracking data entry
38. YSCENTPTP - Treatment Plan Tracking Report
39. YSCENUNITUP - Ward Definition
40. YSCENUNT - Group Data Lookup
41. YSCENWDM - Statistics
42. YSCENWL - Work List
43. YSCLERK - Clerk-entered tests
44. YSCOMMENT - Append comments to tests and interviews
45. YSCRISNOT - Crisis note
46. YSDECTREES-R - Decision Tree Shell
47. YSDIRTEST - Staff entry of tests/interviews
48. YSEPROB - Edit a problem
49. YSEXTESTS - Exempt psychological tests
50. YSFPROB - Formulate new problem list
51. YSGAF CASE FINDER - GAF Case Finder
52. YSHX1 - History - present illness
53. YSHXPAST - Past medical history
54. YSHXPASTR - Past medical history (results of pt. report)
55. YSINST RESTART LIMIT - Edit Instrument Restart Limit
56. YSIPROB - Inactivate an active problem
57. YSJOBINQ - Inquire to job bank
58. YSJOBKILL - Purge job bank
59. YSJOBLIST - Search job bank
60. YSJOBUPDATE - Update job bank
61. YSMANAGEMENT - General Management
62. YSMLST - List Tests & Interviews
63. YSMOVP - Move crisis notes and messages
64. YSPATMSG - Patient message
65. YSPATPROF - Profile of patient
66. YSPERSHX - Psychosocial history
67. YSPERSHXR - Psychosocial history (results of pt. report)
68. YSPHYEXAM - Physical exam
69. YSPLDX - DSM Diagnosis (Problem list)
70. YSPLPDX - ICD9 Diagnosis (Problem list)
71. YSPPROB - Print the problem list
72. YSPRINT - Tests and interviews (results)
73. YSPROBLIST - Problem list
74. YSPTINSTRU - Patient-administered Instruments
75. YSRAPROB - Reactivate an inactive problem
76. YSREVSYS - Review of systems
77. YSREVSYSR - Review of systems (results of pt. report)
78. YSRFPROB - Reformulate a problem79. YSRSPROB - Resolve a problem
80. YSTESTBAT - Test battery utility
81. YSVOCATIONAL - Vocational Rehabilitation
82. YSWAITCR - Create/edit wait lists
83. YSWAITE - Add patient to wait list
84. YSWAITEDI - Edit patient list data
85. YSWAITLST - Wait lists
86. YSWAITP - Print wait list
87. YSWAITREM - Remove patient from list
88. YSWAITSHUF - Move patient on list
89. YT SF36 HEALTH SURVEY - SF-36 Health Survey

## Routines Deleted by Mental Health Patch 60

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>YS03ENV</th>
<th>YS04ENV</th>
<th>YS04POST</th>
<th>YS05ENV</th>
<th>YS05POST</th>
<th>YS06ENV</th>
<th>YS23ENV</th>
<th>YS23POST</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS24ENV</td>
<td>YS24POST</td>
<td>YS26ENV</td>
<td>YS29ENV</td>
<td><blockquote>
<p>YS30ENV</p>
</blockquote></td>
<td><blockquote>
<p>YS30PRE</p>
</blockquote></td>
<td><blockquote>
<p>YS32ENV</p>
</blockquote></td>
<td><blockquote>
<p>YS33ENV</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YS37ENV</td>
<td>YS38ENV</td>
<td>YS38POST</td>
<td>YS39POST</td>
<td>YS42ENV</td>
<td><blockquote>
<p>YS43POST</p>
</blockquote></td>
<td><blockquote>
<p>YS501100</p>
</blockquote></td>
<td><blockquote>
<p>YS501P82</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YS501P83</td>
<td>YS85POST</td>
<td>YS85PRE</td>
<td>YS96POST</td>
<td>YS97POST</td>
<td>YSANTEG</td>
<td>YSAPOST</td>
<td>YSASCF</td>
</tr>
<tr class="even">
<td>YSCEN</td>
<td>YSCEN1</td>
<td><blockquote>
<p>YSCEN10</p>
</blockquote></td>
<td><blockquote>
<p>YSCEN13</p>
</blockquote></td>
<td><blockquote>
<p>YSCEN14</p>
</blockquote></td>
<td><blockquote>
<p>YSCEN2</p>
</blockquote></td>
<td><blockquote>
<p>YSCEN21</p>
</blockquote></td>
<td><blockquote>
<p>YSCEN22</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YSCEN23</td>
<td>YSCEN24</td>
<td>YSCEN26</td>
<td>YSCEN3</td>
<td>YSCEN31</td>
<td>YSCEN32</td>
<td>YSCEN33</td>
<td><blockquote>
<p>YSCEN34</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YSCEN35</td>
<td>YSCEN36</td>
<td>YSCEN37</td>
<td>YSCEN39</td>
<td>YSCEN4</td>
<td>YSCEN41</td>
<td>YSCEN5</td>
<td>YSCEN51</td>
</tr>
<tr class="odd">
<td>YSCEN52</td>
<td>YSCEN53</td>
<td>YSCEN54</td>
<td>YSCEN55</td>
<td>YSCEN56</td>
<td><blockquote>
<p>YSCEN6</p>
</blockquote></td>
<td><blockquote>
<p>YSCEN61</p>
</blockquote></td>
<td><blockquote>
<p>YSCEN7</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YSCEN8</td>
<td><blockquote>
<p>YSCEN81</p>
</blockquote></td>
<td><blockquote>
<p>YSCPAF</p>
</blockquote></td>
<td><blockquote>
<p>YSCPAG</p>
</blockquote></td>
<td><blockquote>
<p>YSCPAI</p>
</blockquote></td>
<td>YSCPAK</td>
<td>YSCPAL</td>
<td>YSCPAM</td>
</tr>
<tr class="odd">
<td>YSCPAQ</td>
<td>YSCUP</td>
<td><blockquote>
<p>YSCUP000</p>
</blockquote></td>
<td><blockquote>
<p>YSCUP001</p>
</blockquote></td>
<td><blockquote>
<p>YSCUP002</p>
</blockquote></td>
<td>YSCUP003</td>
<td>YSCUP004</td>
<td>YSD40030</td>
</tr>
<tr class="even">
<td>YSD40031</td>
<td>YSD40032</td>
<td>YSD40040</td>
<td>YSD40041</td>
<td>YSD40042</td>
<td>YSD40050</td>
<td>YSD40051</td>
<td><blockquote>
<p>YSD40052</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YSD40060</td>
<td>YSD40061</td>
<td>YSD40062</td>
<td><blockquote>
<p>YSD4C000</p>
</blockquote></td>
<td><blockquote>
<p>YSD4CK00</p>
</blockquote></td>
<td><blockquote>
<p>YSD4DSM</p>
</blockquote></td>
<td>YSD4E010</td>
<td>YSD4E020</td>
</tr>
<tr class="even">
<td>YSD4POS0</td>
<td>YSD4POST</td>
<td>YSD4PRE</td>
<td>YSD4PRE0</td>
<td><blockquote>
<p>YSD4UT01</p>
</blockquote></td>
<td><blockquote>
<p>YSDX0001</p>
</blockquote></td>
<td><blockquote>
<p>YSDX0002</p>
</blockquote></td>
<td>YSDXR000</td>
</tr>
<tr class="odd">
<td>YSDXR1</td>
<td>YSEMSG</td>
<td>YSESA</td>
<td>YSESD</td>
<td>YSESE</td>
<td>YSESED</td>
<td>YSESH</td>
<td>YSESL</td>
</tr>
<tr class="even">
<td>YSESLOG</td>
<td><blockquote>
<p>YSESM</p>
</blockquote></td>
<td><blockquote>
<p>YSESN</p>
</blockquote></td>
<td><blockquote>
<p>YSESP</p>
</blockquote></td>
<td><blockquote>
<p>YSESR</p>
</blockquote></td>
<td><blockquote>
<p>YSESUT</p>
</blockquote></td>
<td><blockquote>
<p>YSHELP</p>
</blockquote></td>
<td><blockquote>
<p>YSHX1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YSHX1R</td>
<td>YSJOB</td>
<td>YSJOBK</td>
<td>YSKFASI1</td>
<td>YSKFASI2</td>
<td>YSKFASIF</td>
<td><blockquote>
<p>YSKFASIM</p>
</blockquote></td>
<td><blockquote>
<p>YSMV</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YSMV1</td>
<td>YSNTEG</td>
<td>YSNTEG0</td>
<td>YSONIT</td>
<td>YSONIT1</td>
<td>YSONIT2</td>
<td>YSONIT3</td>
<td>YSPDR1</td>
</tr>
<tr class="odd">
<td>YSPDXR</td>
<td>YSPHY</td>
<td>YSPHY1</td>
<td>YSPHYR</td>
<td><blockquote>
<p>YSPP</p>
</blockquote></td>
<td><blockquote>
<p>YSPP1</p>
</blockquote></td>
<td><blockquote>
<p>YSPP1A</p>
</blockquote></td>
<td><blockquote>
<p>YSPP2</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YSPP3</td>
<td>YSPP4</td>
<td>YSPP5</td>
<td>YSPP6</td>
<td>YSPP7</td>
<td>YSPP8</td>
<td>YSPP9</td>
<td>YSPPJ</td>
</tr>
<tr class="odd">
<td>YSPRBR1</td>
<td>YSPRBR2</td>
<td><blockquote>
<p>YSPROB</p>
</blockquote></td>
<td><blockquote>
<p>YSPROB1</p>
</blockquote></td>
<td><blockquote>
<p>YSPROB2</p>
</blockquote></td>
<td><blockquote>
<p>YSPROB3</p>
</blockquote></td>
<td>YSPROB4</td>
<td>YSPROB5</td>
</tr>
<tr class="even">
<td>YSPROBR</td>
<td>YSPROBR1</td>
<td>YSPROSE</td>
<td>YSPTX</td>
<td>YSPTX1</td>
<td>YSPTXR</td>
<td>YSWX</td>
<td><blockquote>
<p>YSWX1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YSWZ</td>
<td>YSXRAA</td>
<td>YSXRAA1</td>
<td><blockquote>
<p>YSXRAA2</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAA3</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAA4</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAF</p>
</blockquote></td>
<td>YSXRAF1</td>
</tr>
<tr class="even">
<td>YSXRAF2</td>
<td>YSXRAF3</td>
<td>YSXRAF4</td>
<td>YSXRAF5</td>
<td><blockquote>
<p>YSXRAF6</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAG</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAG1</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAG2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YSXRAJ</td>
<td>YSXRAJ1</td>
<td>YSXRAJ2</td>
<td>YSXRAJ3</td>
<td>YSXRAJ4</td>
<td>YSXRAK1</td>
<td>YSXRAK10</td>
<td>YSXRAK11</td>
</tr>
<tr class="even">
<td>YSXRAK12</td>
<td>YSXRAK2</td>
<td>YSXRAK3</td>
<td>YSXRAK4</td>
<td>YSXRAK5</td>
<td><blockquote>
<p>YSXRAK6</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAK7</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAK8</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YSXRAK9</td>
<td>YSXRAQ</td>
<td>YSXRAQ1</td>
<td>YSXRAQ2</td>
<td>YSXRAQ3</td>
<td>YSXRAQ4</td>
<td><blockquote>
<p>YSXRAR</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAR1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YSXRAR2</td>
<td>YSXRAS</td>
<td>YSXRAS1</td>
<td>YSXRAS2</td>
<td>YSXRAT</td>
<td>YSXRAT1</td>
<td>YSXRAT2</td>
<td>YSXRAT3</td>
</tr>
<tr class="odd">
<td>YSXRAT4</td>
<td>YSXRAT5</td>
<td>YSXRAT6</td>
<td><blockquote>
<p>YSXRAU</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAU1</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAU2</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAV</p>
</blockquote></td>
<td><blockquote>
<p>YSXRAV1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YSXRAV2</td>
<td>YSXRAW1</td>
<td>YSXRAW2</td>
<td>YSXRAZ1</td>
<td>YSXRAZ2</td>
<td>YSXRAZ3</td>
<td>YSXRAZ4</td>
<td>YSXRAZ5</td>
</tr>
<tr class="odd">
<td>YSXRAZ6</td>
<td>YSXRBA</td>
<td>YSXRBA1</td>
<td>YSXRBA2</td>
<td>YSXRBA3</td>
<td>YSXRBA4</td>
<td>YSXRBA5</td>
<td>YSXRBA6</td>
</tr>
<tr class="even">
<td>YTEX</td>
<td>YTQQI001</td>
<td>YTQQI002</td>
<td>YTQQI003</td>
<td>YTQQI004</td>
<td><blockquote>
<p>YTQQI005</p>
</blockquote></td>
<td><blockquote>
<p>YTQQI006</p>
</blockquote></td>
<td><blockquote>
<p>YTQQI007</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTQQI008</td>
<td><blockquote>
<p>YTQQI009</p>
</blockquote></td>
<td><blockquote>
<p>YTQQI00A</p>
</blockquote></td>
<td><blockquote>
<p>YTQQI00B</p>
</blockquote></td>
<td><blockquote>
<p>YTQQI00C</p>
</blockquote></td>
<td>YTQQI00D</td>
<td>YTQQI00E</td>
<td>YTQQI00F</td>
</tr>
<tr class="even">
<td>YTQQI00G</td>
<td>YTQQI00H</td>
<td>YTQQI00I</td>
<td><blockquote>
<p>YTQQI00J</p>
</blockquote></td>
<td><blockquote>
<p>YTQQI00K</p>
</blockquote></td>
<td><blockquote>
<p>YTTB</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

These routines are deleted by KIDS during the patch installation.

# Appendix B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## NCCC HL7 Message Specification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This describes the data being moved through the HL7 interface.

### Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the conventions for HL7 messages.

#### HL7 Messages

HL7 messages shall follow the standard HL7 version 2.5.1 format documented in An Application Protocol for Electronic Data Exchange in Healthcare Environments.

#### Date/Time of Message Format

The format for MSH-7, Date/Time of Message, is YYYYMMDD\[HHMM\[SS\]\] \[+-ZZZZ\] where:

- YYYY is the 4-digit year, e.g., “2002”
- MM is the month number, ranging from “01” to “12”
- DD is the day number within the month, ranging from “01” to “31”
- HH is the hour from “00” to “23”.? MM is the minute from “00” to “59”
- SS is the second from “00” to “59”
- +-ZZZZ represents the time zone as a leading signed value time offset from Greenwich Mean Time of the form HHMM using the same convention for HH and MM as given above. For example, Eastern Standard Time (EST) is given as “–0500”

#### Message and Segment Boundaries

Message starts with American Standard Code for Information Interchange (ASCII) character 11<sub>10</sub>, vertical tab (VT).

Segment terminates with ASCII character 13<sub>10</sub>, carriage return (CR).

Message terminates with ASCII character 28<sub>10</sub>, file separator (FS), followed by ASCII character 13<sub>10,</sub> carriage return (CR).

The prototypical form is:

- \<VT\>segment\<CR\>segment\<CR\>\<FS\>\<CR\>

\<VT\> as the prefix and \<FS\>\<CR\> as the suffix are part of the HL7 Minimal Lower Layer Protocol, (MLLP).

#### Segment Tables

In the Segment tables that follow, missing sequence numbers indicate that the respective fields are empty in the segment. An empty field has no characters between its boundaries (start of the segment, field separators, and the end of the segment).

The Seq column contains the sequence number of the element.

The Name column gives the HL7 name for the element or sub-element. In those cases where HL7 does not supply a name, this document defines that name for use solely within the VistA and NCR interface.

Following the element name, data type information drawn from the HL7 2.5.1 standard *may* appear in the DT column.

The Len column contains the length of the element.

The Opt column value “R” indicates that the element requires a value and so the sender must place a non-empty value into this HL7 element. The value “O” marks those elements in which a value is optional. The value of optional elements may be empty. “RE” indicates conditional use and “NS” means not supported.

The Rep column contains “TRUE” if the element is repeatable and “FALSE” (or blank) if it isn’t.

The Fixed Value column contains “TRUE” if the value of this element will be fixed for every message of this type. (In this case the example value in the Ex Val column is the value.)

The Code Tbl column contains the relevant code table number.

The Example Value column contains an example value for this element.

The Implementation Notes column contains any relevant implementation notes.

#### Message Notations

A message notation presents the segment IDs in the correct order. Curly brackets ({}) surround one or more segments that are to be repeated one or more times. Square brackets (\[\]) surround optional segments. Using both kinds of brackets declares that the enclosed segments may appear zero or more times.

### Network Connections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA connects to the designated TCP port and IP domain, listed in section 5.1.1, using TCP/IP to send HL7 messages to the NCR InterSystems HealthShare Server on the Cloud Server.

The NCR HealthShare Server returns negative commit acknowledgments for incomplete HL7 messages that it receives to the TCP port on the destination VistA system using TCP/IP.

### NCR Patient Registration Message: ADT^A28

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ADT^A28 Registration message is triggered when the YSCL at the individual VAMC VistA system extracts Clozaril Rollup data to generate HL7 messages.

The ADT^A28 Message Type is constructed of the following HL7 segments in the order listed:

- MSH - Message Header
- EVN - Event Type
- PID - Patient Identification
- ROL - Role
- PV1 - Patient Visit
- OBX(1) – Observation/Result - Patient Clozapine Status
- OBX(2) – Observation/Result - WBC
- OBX(3) – Observation/Result - ANC
- OBX(4) – Observation/Result - Site DEA
- OBX(5) – Observation/Result – Site

The notation is: MSH, EVN, PID, ROL, PV1, OBX, OBX, OBX, OBX, OBX

#### NCR Patient Registration MSH Segment

Table: MSH Segment

<table style="width:100%;">
<caption>This table displays the Clozapine Registration MSH Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>MSH Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Field Separator</td>
<td>1</td>
<td>ST</td>
<td>1</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td></td>
<td>|</td>
<td></td>
</tr>
<tr class="even">
<td>Encoding Characters</td>
<td>2</td>
<td>ST</td>
<td>4</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td></td>
<td>^~\&amp;</td>
<td></td>
</tr>
<tr class="odd">
<td>Sending Application</td>
<td>3</td>
<td>HD</td>
<td>227</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0361</td>
<td> </td>
<td></td>
</tr>
<tr class="even">
<td>Namespace ID</td>
<td>1</td>
<td>IS</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0300</td>
<td>YSCL CLOZ REGISTRY</td>
<td>This is always “YSCL CLOZ REGISTRY”</td>
</tr>
<tr class="odd">
<td>Universal ID</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Universal ID Type</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td> </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Sending Facility</td>
<td>4</td>
<td>HD</td>
<td>227</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0362</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Namespace ID</td>
<td>1</td>
<td>IS</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0300</td>
<td>501 or 501GF</td>
<td>This is the site number of the sending site, e.g., 501 (parent facility) or 501GF (satellite facility)</td>
</tr>
<tr class="odd">
<td>Universal ID</td>
<td>2</td>
<td>ST</td>
<td>50</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>HL7.SMA.FO-ALBANY.MED.VA.GOV:5001</td>
<td>URL and port number of the sending facility HL7 server</td>
</tr>
<tr class="even">
<td>Universal ID Type</td>
<td>3</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0301</td>
<td>DNS</td>
<td></td>
</tr>
<tr class="odd">
<td>Receiving Application</td>
<td>5</td>
<td>HD</td>
<td>227</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0361</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Namespace ID</td>
<td>1</td>
<td>IS</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0300</td>
<td>NCR CLOZ REGISTRY</td>
<td>This is always “NCR CLOZ REGISTRY”</td>
</tr>
<tr class="odd">
<td>Universal ID</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Universal ID Type</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Receiving Facility</td>
<td>6</td>
<td>HD</td>
<td>227</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0362</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Namespace ID</td>
<td>1</td>
<td>IS</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0300</td>
<td>3000</td>
<td>Receiving facility identifier (TBD for HealthShare server - alphanumeric)</td>
</tr>
<tr class="odd">
<td>Universal ID</td>
<td>2</td>
<td>ST</td>
<td>50</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>devazrclzpv01.dev.dss.local:5001</td>
<td>URL and port number of the receiving facility HL7 server</td>
</tr>
<tr class="even">
<td>Universal ID Type</td>
<td>3</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0301</td>
<td>DNS</td>
<td></td>
</tr>
<tr class="odd">
<td>Date/Time of Message</td>
<td>7</td>
<td>TS</td>
<td>26</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Time</td>
<td>1</td>
<td>DTM</td>
<td>24</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>20170328134602-0500</td>
<td>Date/time the message was created in format YYYYMMDD[HHMM[SS]][+-ZZZZ]00</td>
</tr>
<tr class="odd">
<td>Degree of Precision</td>
<td>2</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Security</td>
<td>8</td>
<td>ST</td>
<td>40</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Message Type</td>
<td>9</td>
<td>MSG</td>
<td>15</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Message Code</td>
<td>1</td>
<td>ID</td>
<td>3</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0076</td>
<td>ADT</td>
<td>This is always “ADT”</td>
</tr>
<tr class="odd">
<td>Trigger Event</td>
<td>2</td>
<td>ID</td>
<td>3</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0003</td>
<td>A28</td>
<td>This is always “A28”</td>
</tr>
<tr class="even">
<td>Message Structure</td>
<td>3</td>
<td>ID</td>
<td>7</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0354</td>
<td>ADT_A05</td>
<td>This is always “ADT_A05”</td>
</tr>
<tr class="odd">
<td>Message Control ID</td>
<td>10</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td>12345</td>
<td>Assigned by the HL7 package on VistA by the</td>
</tr>
<tr class="even">
<td>Processing ID</td>
<td>11</td>
<td>PT</td>
<td>3</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Processing ID</td>
<td>1</td>
<td>ID</td>
<td>1</td>
<td>R</td>
<td></td>
<td></td>
<td>0103</td>
<td>P</td>
<td><p>“P” -Production</p>
<p>“T” - Test</p></td>
</tr>
<tr class="even">
<td>Processing Mode</td>
<td>2</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Version ID</td>
<td>12</td>
<td>VID</td>
<td>973</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Version ID</td>
<td>1</td>
<td>ID</td>
<td>5</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0104</td>
<td>2.5.1</td>
<td>This is always “2.5.1”</td>
</tr>
<tr class="odd">
<td>Internationalization Code</td>
<td>2</td>
<td>CE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>International Version ID</td>
<td>3</td>
<td>CE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Sequence Number</td>
<td>13</td>
<td>NM</td>
<td>15</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr class="even">
<td>Continuation Pointer</td>
<td>14</td>
<td>ST</td>
<td>180</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Accept Acknowledgment Type</td>
<td>15</td>
<td>ID</td>
<td>2</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td>0155</td>
<td>AL</td>
<td>This is always “AL”</td>
</tr>
<tr class="even">
<td>Application Acknowledgment Type</td>
<td>16</td>
<td>ID</td>
<td>2</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td>0155</td>
<td>AL</td>
<td>This is always “AL”</td>
</tr>
<tr class="odd">
<td>Country Code</td>
<td>17</td>
<td>ID</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Character Set</td>
<td>18</td>
<td>ID</td>
<td>16</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Principal Language of Message</td>
<td>19</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Character Set Handling Scheme</td>
<td>20</td>
<td>ID</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Message Profile Identifier</td>
<td>21</td>
<td>EI</td>
<td>427</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Registration MSH Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Patient Registration EVN Segment

Table: EVN Segment

<table style="width:100%;">
<caption>This table displays the Clozapine Registration EVN Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>EVN Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Event Type Code</td>
<td>1</td>
<td>ID</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Recorded Date/Time</td>
<td>2</td>
<td>TS</td>
<td>26</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Time</td>
<td>1</td>
<td>DTM</td>
<td>24</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>20170328134602-0500</td>
<td><p>YYYYMMDD[HHMM</p>
<p>[SS]][+-ZZZZ]</p></td>
</tr>
<tr class="even">
<td>Degree of Precision</td>
<td>2</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Date/Time Planned Event</td>
<td>3</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Event Reason Code</td>
<td>4</td>
<td>IS</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Operator ID</td>
<td>5</td>
<td>XCN</td>
<td>2930</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Event Occurred</td>
<td>6</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Event Facility</td>
<td>7</td>
<td>HD</td>
<td>241</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Registration EVN Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Patient Registration PID Segment

Table: PID Segment

<table style="width:100%;">
<caption>This table displays the Clozapine Registration PID Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>PID Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Set ID - PID</td>
<td>1</td>
<td>SI</td>
<td>4</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patient ID</td>
<td>2</td>
<td>CX</td>
<td>1913</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Patient Identifier List</td>
<td>3</td>
<td>CX</td>
<td>1912</td>
<td>R</td>
<td>True</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ID Number</td>
<td>1</td>
<td>ST</td>
<td>15</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td><p>VA12345<br />
or</p>
<p>111223344<br />
or</p>
<p>1000720100V271387<br />
or</p>
<p>100234567</p></td>
<td>The 1st instance is the patient's Clozaril authorization number (NCR's number – 2 letters followed by 5 numbers). The 2nd instance is the patient's SSN. The 3rd instance is the patient ICN. The 4th instance is the patient DFN</td>
</tr>
<tr class="odd">
<td>Check Digit</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Check Digit Scheme</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td> </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Assigning Authority</td>
<td>4</td>
<td>HD</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier Type Code</td>
<td>5</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0203</td>
<td>PN or SS</td>
<td>The 1st instance is "PN" - Patient's Clozaril authorization number. The 2nd instance is "SS" – Patient’s Social Security.</td>
</tr>
<tr class="odd">
<td>Assigning Facility</td>
<td>6</td>
<td>HD</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Effective Date</td>
<td>7</td>
<td>DT</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Expiration Date</td>
<td>8</td>
<td>DT</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Assigning Jurisdiction</td>
<td>9</td>
<td>CWE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Assigning Agency or Department</td>
<td>10</td>
<td>CWE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Patient ID - PID</td>
<td>4</td>
<td>CX</td>
<td>1913</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Patient Name</td>
<td>5</td>
<td>XPN</td>
<td>1044</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Family Name</td>
<td>1</td>
<td>FN</td>
<td>194</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Surname</td>
<td>1</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Doe</td>
<td>Last Name</td>
</tr>
<tr class="even">
<td>Own Surname Prefix</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Own Surname</td>
<td>3</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Surname Prefix from Partner/Spouse</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Surname from Partner/Spouse</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Given Name</td>
<td>2</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>John</td>
<td>First Name</td>
</tr>
<tr class="odd">
<td>Second and Further Given Names or Initials Thereof</td>
<td>3</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Suffix (e.g., JR or III)</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Prefix (e.g., DR)</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Degree (e.g., MD)</td>
<td>6</td>
<td>IS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Type Code</td>
<td>7</td>
<td>ID</td>
<td>1</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0200</td>
<td>L</td>
<td>This is always "L"</td>
</tr>
<tr class="even">
<td>Name Representation Code</td>
<td>8</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td> </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Context</td>
<td>9</td>
<td>CE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td> </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name Validity Range</td>
<td>10</td>
<td>DR</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Assembly Order</td>
<td>11</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Effective Date</td>
<td>12</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Expiration Date</td>
<td>13</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Professional Suffix</td>
<td>14</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Mother's Maiden Name</td>
<td>6</td>
<td>XPN</td>
<td>1044</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Date/Time of Birth</td>
<td>7</td>
<td>TS</td>
<td>26</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Time</td>
<td>1</td>
<td>DTM</td>
<td>24</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>19700101</td>
<td>YYYYMMDD</td>
</tr>
<tr class="even">
<td>Degree of Precision</td>
<td>2</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Administrative Sex</td>
<td>8</td>
<td>IS</td>
<td>1</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0001</td>
<td>F</td>
<td></td>
</tr>
<tr class="even">
<td>Patient Alias</td>
<td>9</td>
<td>XPN</td>
<td>1044</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Race</td>
<td>10</td>
<td>CE</td>
<td>478</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0005</td>
<td>2028-9</td>
<td></td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Asian</td>
<td>Race Identifier description</td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0396</td>
<td>HL70005</td>
<td>HL7 Defined Code where nnnn is the HL7 table number 0005. This is always “HL70005”.HL7000570005L7</td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patient Address</td>
<td>11</td>
<td>XAD</td>
<td>513</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr class="odd">
<td>Street Address</td>
<td>1</td>
<td>SAD</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Other Designation</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>City</td>
<td>3</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>State or Province</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Zip or Postal Code</td>
<td>5</td>
<td>ST</td>
<td>12</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>33408</td>
<td></td>
</tr>
<tr class="even">
<td>Country</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Address Type</td>
<td>7</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Other Geographic Designation</td>
<td>8</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>County/Parish Code</td>
<td>9</td>
<td>IS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Census Tract</td>
<td>10</td>
<td>IS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Address Representation Code</td>
<td>11</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Address Validity Range</td>
<td>12</td>
<td>DR</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Effective Date</td>
<td>13</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Expiration Date</td>
<td>14</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>County Code</td>
<td>12</td>
<td>IS</td>
<td>4</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Phone Number - Home</td>
<td>13</td>
<td>XTN</td>
<td>651</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Phone Number - Business</td>
<td>14</td>
<td>XTN</td>
<td>651</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Primary Language</td>
<td>15</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Marital Status</td>
<td>16</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Religion</td>
<td>17</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Patient Account Number</td>
<td>18</td>
<td>CX</td>
<td>1912</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>SSN Number - Patient</td>
<td>19</td>
<td>ST</td>
<td>16</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Driver's License Number - Patient</td>
<td>20</td>
<td>DLN</td>
<td>66</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Mother's Identifier</td>
<td>21</td>
<td>CX</td>
<td>1912</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Ethnic Group</td>
<td>22</td>
<td>CE</td>
<td>478</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0189</td>
<td>U</td>
<td></td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Unknown</td>
<td>Ethnic Identifier description</td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0396</td>
<td>HL70189</td>
<td>HL7 Defined Code where nnnn is the HL7 table number 0005. This is always “HL70189”.</td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Birth Place</td>
<td>23</td>
<td>ST</td>
<td>250</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Multiple Birth Indicator</td>
<td>24</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Birth Order</td>
<td>25</td>
<td>NM</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Citizenship</td>
<td>26</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Veterans Military Status</td>
<td>27</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Nationality</td>
<td>28</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patient Death Date and Time</td>
<td>29</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Patient Death Indicator</td>
<td>30</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identity Unknown Indicator</td>
<td>31</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Identity Reliability Code</td>
<td>32</td>
<td>IS</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Last Update Date/Time</td>
<td>33</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Last Update Facility</td>
<td>34</td>
<td>HD</td>
<td>241</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Species Code</td>
<td>35</td>
<td>CE</td>
<td>478</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Breed Code</td>
<td>36</td>
<td>CE</td>
<td>478</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Strain</td>
<td>37</td>
<td>ST</td>
<td>80</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Production Class Code</td>
<td>38</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Tribal Citizenship</td>
<td>39</td>
<td>CWE</td>
<td>705</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Registration PID Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Patient Registration ROL Segment

<table>
<caption>This table displays the Clozapine Registration ROL Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>ROL Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Role Instance ID</td>
<td>1</td>
<td>EI</td>
<td>424</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Action Code</td>
<td>2</td>
<td>ID</td>
<td>2</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0287</td>
<td>UP</td>
<td>This is always “UP”</td>
</tr>
<tr class="odd">
<td>Role-ROL</td>
<td>3</td>
<td>CE</td>
<td>478</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0443</td>
<td>PPRX PRPX</td>
<td>This is always “PRX”. Need to add “PRX” to table 0443</td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>30</td>
<td>R</td>
<td></td>
<td>True</td>
<td></td>
<td>Prescribing Physician</td>
<td>This is always “Prescribing Physician”</td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0396</td>
<td>HL70443</td>
<td>HL7 Defined Code where nnnn is the HL7 table number 0443. This is always “HL70443”.</td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Role Person</td>
<td>4</td>
<td>XCN</td>
<td>2930</td>
<td>R</td>
<td>True</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ID Number</td>
<td>1</td>
<td>ST</td>
<td>15</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>AR7071296</td>
<td><p>1st instance: This is the DEA number of the prescribing physician.</p>
<p>2nd instance: This is the NPI number of the prescribing physician.</p></td>
</tr>
<tr class="even">
<td>Family Name</td>
<td>2</td>
<td>FN</td>
<td>194</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Surname</td>
<td>1</td>
<td>ST</td>
<td>50</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Lastname</td>
<td>Last name of the prescribing physician</td>
</tr>
<tr class="even">
<td>Own Surname Prefix</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Own Surname</td>
<td>3</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Surname Prefix from Partner/Spouse</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Surname from Partner/Spouse</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Given Name</td>
<td>3</td>
<td>ST</td>
<td>30</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Firstname</td>
<td>First name of the prescribing physician</td>
</tr>
<tr class="odd">
<td>Second and Further Given Names or Initials Thereof</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Suffix (e.g., JR or III)</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Prefix (e.g., DR)</td>
<td>6</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Degree (e.g., MD)</td>
<td>7</td>
<td>IS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Source Table</td>
<td>8</td>
<td>IS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Assigning Authority</td>
<td>9</td>
<td>HD</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Type Code</td>
<td>10</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier Check Digit</td>
<td>11</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Check Digit Scheme</td>
<td>12</td>
<td>ID</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier Type Code</td>
<td>13</td>
<td>ID</td>
<td>3</td>
<td>R</td>
<td></td>
<td></td>
<td>0203</td>
<td>DEA</td>
<td><p>1st instance: This is "DEA". Need to add “DEA” to table 0203</p>
<p>2nd instance: This is "NPI".</p></td>
</tr>
<tr class="odd">
<td>Assigning Facility</td>
<td>14</td>
<td>HD</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name Representation Code</td>
<td>15</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Context</td>
<td>16</td>
<td>CE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name Validity Range</td>
<td>17</td>
<td>DR</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Assembly Order</td>
<td>18</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Effective Date</td>
<td>19</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Expiration Date</td>
<td>20</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Professional Suffix</td>
<td>21</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Assigning Jurisdiction</td>
<td>22</td>
<td>CWE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Assigning Agency or Department</td>
<td>23</td>
<td>CWE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Role Begin Date/Time</td>
<td>5</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Role End Date/Time</td>
<td>6</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Role Duration</td>
<td>7</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Role Action Reason</td>
<td>8</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Provider Type</td>
<td>9</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Organization Unit Type</td>
<td>10</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Office/Home Address/Birthplace</td>
<td>11</td>
<td>XAD</td>
<td>513</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Phone</td>
<td>12</td>
<td>XTN</td>
<td>651</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Registration ROL Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Patient Registration PV1 Segment

Table: PV1 Segment

<table style="width:100%;">
<caption>This table displays the Clozapine Registration PV1 Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>PV1 Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Set ID - PV1</td>
<td>1</td>
<td>SI</td>
<td>4</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patient Class</td>
<td>2</td>
<td>IS</td>
<td>1</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0004</td>
<td>O or I</td>
<td><p>“O” - Outpatient</p>
<p>“I” - Inpatient</p></td>
</tr>
<tr class="odd">
<td>Assigned Patient Location</td>
<td>3</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Admission Type</td>
<td>4</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Preadmit Number</td>
<td>5</td>
<td>CX</td>
<td>1912</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Prior Patient Location</td>
<td>6</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Attending Doctor</td>
<td>7</td>
<td>XCN</td>
<td>2930</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Referring Doctor</td>
<td>8</td>
<td>XCN</td>
<td>2930</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Consulting Doctor</td>
<td>9</td>
<td>XCN</td>
<td>2945</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Hospital Service</td>
<td>10</td>
<td>IS</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Temporary Location</td>
<td>11</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Preadmit Test Indicator</td>
<td>12</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Re-admission Indicator</td>
<td>13</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Admit Source</td>
<td>14</td>
<td>IS</td>
<td>6</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Ambulatory Status</td>
<td>15</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VIP Indicator</td>
<td>16</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Admitting Doctor</td>
<td>17</td>
<td>XCN</td>
<td>2930</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patient Type</td>
<td>18</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Visit Number</td>
<td>19</td>
<td>CX</td>
<td>1912</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Financial Class</td>
<td>20</td>
<td>FC</td>
<td>50</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Charge Price Indicator</td>
<td>21</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Courtesy Code</td>
<td>22</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Credit Rating</td>
<td>23</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Contract Code</td>
<td>24</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Contract Effective Date</td>
<td>25</td>
<td>DT</td>
<td>8</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Contract Amount</td>
<td>26</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Contract Period</td>
<td>27</td>
<td>NM</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Interest Code</td>
<td>28</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Transfer to Bad Debt Code</td>
<td>29</td>
<td>IS</td>
<td>4</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Transfer to Bad Debt Date</td>
<td>30</td>
<td>DT</td>
<td>8</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Bad Debt Agency Code</td>
<td>31</td>
<td>IS</td>
<td>10</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bad Debt Transfer Amount</td>
<td>32</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Bad Debt Recovery Amount</td>
<td>33</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Delete Account Indicator</td>
<td>34</td>
<td>IS</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Delete Account Date</td>
<td>35</td>
<td>DT</td>
<td>8</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Discharge Disposition</td>
<td>36</td>
<td>IS</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Discharged to Location</td>
<td>37</td>
<td>DLD</td>
<td>47</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Diet Type</td>
<td>38</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Servicing Facility</td>
<td>39</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bed Status</td>
<td>40</td>
<td>IS</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Account Status</td>
<td>41</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Pending Location</td>
<td>42</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Prior Temporary Location</td>
<td>43</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Admit Date/Time</td>
<td>44</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Discharge Date/Time</td>
<td>45</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Current Patient Balance</td>
<td>46</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Total Charges</td>
<td>47</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Total Adjustments</td>
<td>48</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Total Payments</td>
<td>49</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Visit ID</td>
<td>50</td>
<td>CX</td>
<td>1912</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Visit Indicator</td>
<td>51</td>
<td>IS</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Other Healthcare Provider</td>
<td>52</td>
<td>XCN</td>
<td>2945</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Registration PV1 Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Patient Registration OBX(1) Segment

Table: OBX(1) Segment

<table style="width:100%;">
<caption>This table displays the Clozapine Registration OBX(1) Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>OBX(1) Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Set ID - OBX</td>
<td>1</td>
<td>SI</td>
<td>4</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td></td>
<td>1</td>
<td>This is always “1” to indicate the 1<sup>st</sup> instance of the OBX segment</td>
</tr>
<tr class="even">
<td>Value Type</td>
<td>2</td>
<td>ID</td>
<td>2</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td>0125</td>
<td>CE</td>
<td>This is always “CE” in the 1<sup>st</sup> instance of the OBX segment</td>
</tr>
<tr class="odd">
<td>Observation Identifier</td>
<td>3</td>
<td>CE</td>
<td>478</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td></td>
<td>PTSTAT</td>
<td>This is always “PTSTAT” in the 1<sup>st</sup> OBX instance</td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Observation Sub-ID</td>
<td>4</td>
<td>ST</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Observation Value</td>
<td>5</td>
<td>CE</td>
<td>99999</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>1</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td> A or D</td>
<td>Patient status:<br />
“A” – Active<br />
“D” - Discontinued</td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Units</td>
<td>6</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>References Range</td>
<td>7</td>
<td>ST</td>
<td>60</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Abnormal Flags</td>
<td>8</td>
<td>IS</td>
<td>5</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Probability</td>
<td>9</td>
<td>NM</td>
<td>5</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Nature of Abnormal Test</td>
<td>10</td>
<td>ID</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Observation Result Status</td>
<td>11</td>
<td>ID</td>
<td>1</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td>0085</td>
<td>F</td>
<td>This is always “F”</td>
</tr>
<tr class="even">
<td>Effective Date of Reference Range Values</td>
<td>12</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>User Defined Access Checks</td>
<td>13</td>
<td>ST</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Date/Time of the Observation</td>
<td>14</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Producer's Reference</td>
<td>15</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Responsible Observer</td>
<td>16</td>
<td>XCN</td>
<td>2930</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Observation Method</td>
<td>17</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Equipment Instance Identifier</td>
<td>18</td>
<td>EI</td>
<td>427</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Date/Time of the Analysis</td>
<td>19</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Reserved for harmonization with V2.6</td>
<td>20</td>
<td>varies</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Reserved for harmonization with V2.6</td>
<td>21</td>
<td>varies</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Reserved for harmonization with V2.6</td>
<td>22</td>
<td>varies</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Performing Organization Name</td>
<td>23</td>
<td>XON</td>
<td>567</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Performing Organization Address</td>
<td>24</td>
<td>XAD</td>
<td>631</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Performing Organization Medical Director</td>
<td>25</td>
<td>XCN</td>
<td>3002</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Registration OBX(1) Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Patient Registration OBX(2) Segment

Table: OBX(2) Segment

<table style="width:100%;">
<caption>This table displays the Clozapine Registration OBX(2) Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>OBX(2) Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Set ID - OBX</td>
<td>1</td>
<td>SI</td>
<td>4</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td></td>
<td>2</td>
<td>This is always “2” to indicate the 2nd instance of the OBX segment</td>
</tr>
<tr class="even">
<td>Value Type</td>
<td>2</td>
<td>ID</td>
<td>2</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td>0125</td>
<td>CE</td>
<td>This is always “CE” in the 2nd instance of the OBX segment</td>
</tr>
<tr class="odd">
<td>Observation Identifier</td>
<td>3</td>
<td>CE</td>
<td>478</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td> </td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td></td>
<td>PTSTAT</td>
<td>This is always “Dispense Frequency” in the 2nd OBX instance</td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Observation Sub-ID</td>
<td>4</td>
<td>ST</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Observation Value</td>
<td>5</td>
<td>CE</td>
<td>99999</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>1</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>7 Days</td>
<td>Dispense Frequency:<br />
7 Days, 14 Days, or 28 Days.</td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Units</td>
<td>6</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>References Range</td>
<td>7</td>
<td>ST</td>
<td>60</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Abnormal Flags</td>
<td>8</td>
<td>IS</td>
<td>5</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Probability</td>
<td>9</td>
<td>NM</td>
<td>5</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Nature of Abnormal Test</td>
<td>10</td>
<td>ID</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Observation Result Status</td>
<td>11</td>
<td>ID</td>
<td>1</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td>0085</td>
<td>F</td>
<td>This is always “F”</td>
</tr>
<tr class="even">
<td>Effective Date of Reference Range Values</td>
<td>12</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>User Defined Access Checks</td>
<td>13</td>
<td>ST</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Date/Time of the Observation</td>
<td>14</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Producer's Reference</td>
<td>15</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Responsible Observer</td>
<td>16</td>
<td>XCN</td>
<td>2930</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Observation Method</td>
<td>17</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Equipment Instance Identifier</td>
<td>18</td>
<td>EI</td>
<td>427</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Date/Time of the Analysis</td>
<td>19</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Reserved for harmonization with V2.6</td>
<td>20</td>
<td>varies</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Reserved for harmonization with V2.6</td>
<td>21</td>
<td>varies</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Reserved for harmonization with V2.6</td>
<td>22</td>
<td>varies</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Performing Organization Name</td>
<td>23</td>
<td>XON</td>
<td>567</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Performing Organization Address</td>
<td>24</td>
<td>XAD</td>
<td>631</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Performing Organization Medical Director</td>
<td>25</td>
<td>XCN</td>
<td>3002</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Registration OBX(2) Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Patient Registration OBX(3) Segment

Table: OBX(3) Segment

| OBX(3) Field Name                        | Seq | DT     | Len  | Opt | Rep   | Fixed Value | Code Tbl | Example Value        | Implementation Notes                                                                                     |
|------------------------------------------|-----|--------|------|-----|-------|-------------|----------|----------------------|----------------------------------------------------------------------------------------------------------|
| Set ID - OBX                             | 1   | SI     | 4    | R   | False | True        |          | 3                    | This is always “3” to indicate the 3rd OBX instance                                                      |
| Value Type                               | 2   | ID     | 2    | R   | False |             | 0125     | CE                   | This is always “CE” in the 3rd OBX instance                                                              |
| Observation Identifier                   | 3   | CE     | 478  | R   | False |             |          |                      |                                                                                                          |
| Identifier                               | 1   | ST     | 0    | NS  |       |             |          |                      |                                                                                                          |
| Text                                     | 2   | ST     | 20   | R   |       | True        |          | WBC                  | This is always “WBC” in the 3rd OBX instance                                                             |
| Name of Coding System                    | 3   | ID     | 0    | NS  |       |             |          |                      |                                                                                                          |
| Alternate Identifier                     | 4   | ST     | 0    | NS  |       |             |          |                      |                                                                                                          |
| Alternate Text                           | 5   | ST     | 0    | NS  |       |             |          |                      |                                                                                                          |
| Name of Alternate Coding System          | 6   | ID     | 0    | NS  |       |             |          |                      |                                                                                                          |
| Observation Sub-ID                       | 4   | ST     | 20   | NS  |       |             |          |                      |                                                                                                          |
| Observation Value                        | 5   | NM     | 20   | R   | False |             |          | 7800                 | The White Blood Count result in the format expected by the manufacturer of the drug (whole number)       |
| Units                                    | 6   | CE     | 483  | NS  |       |             |          |                      |                                                                                                          |
| References Range                         | 7   | ST     | 60   | NS  |       |             |          |                      |                                                                                                          |
| Abnormal Flags                           | 8   | IS     | 5    | NS  |       |             |          |                      |                                                                                                          |
| Probability                              | 9   | NM     | 5    | NS  |       |             |          |                      |                                                                                                          |
| Nature of Abnormal Test                  | 10  | ID     | 2    | NS  |       |             |          |                      |                                                                                                          |
| Observation Result Status                | 11  | ID     | 1    | R   | False | True        | 0085     | F                    | This is always “F”                                                                                       |
| Effective Date of Reference Range Values | 12  | TS     | 26   | NS  |       |             |          |                      |                                                                                                          |
| User Defined Access Checks               | 13  | ST     | 20   | NS  |       |             |          |                      |                                                                                                          |
| Date/Time of the Observation             | 14  | TS     | 26   | R   | False |             |          |                      |                                                                                                          |
| Time                                     | 1   | DTM    | 24   | R   |       |             |          |  20170328134602-0500 | Date and time of blood sample collection for the WBC Test in the format YYYYMMDD\[HHMM\[SS\]\]\[+-ZZZZ\] |
| Degree of Precision                      | 2   | ID     | 0    | NS  |       |             |          |                      |                                                                                                          |
| Producer's Reference                     | 15  | CE     | 483  | NS  |       |             |          |                      |                                                                                                          |
| Responsible Observer                     | 16  | XCN    | 2930 | NS  |       |             |          |                      |                                                                                                          |
| Observation Method                       | 17  | CE     | 483  | NS  |       |             |          |                      |                                                                                                          |
| Equipment Instance Identifier            | 18  | EI     | 427  | NS  |       |             |          |                      |                                                                                                          |
| Date/Time of the Analysis                | 19  | TS     | 26   | NS  |       |             |          |                      |                                                                                                          |
| Reserved for harmonization with V2.6     | 20  | varies | 1    | NS  |       |             |          |                      |                                                                                                          |
| Reserved for harmonization with V2.6     | 21  | varies | 1    | NS  |       |             |          |                      |                                                                                                          |
| Reserved for harmonization with V2.6     | 22  | varies | 1    | NS  |       |             |          |                      |                                                                                                          |
| Performing Organization Name             | 23  | XON    | 567  | NS  |       |             |          |                      |                                                                                                          |
| Performing Organization Address          | 24  | XAD    | 631  | NS  |       |             |          |                      |                                                                                                          |
| Performing Organization Medical Director | 25  | XCN    | 3002 | NS  |       |             |          |                      |                                                                                                          |

This table displays the Clozapine Registration OBX(3) Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Patient Registration OBX(4) Segment

Table: OBX(4) Segment

| OBX(4) Field Name                        | Seq | DT     | Len  | Opt | Rep   | Fixed Value | Code Tbl | Example Value       | Implementation Notes                                                                              |
|------------------------------------------|-----|--------|------|-----|-------|-------------|----------|---------------------|---------------------------------------------------------------------------------------------------|
| Set ID - OBX                             | 1   | SI     | 4    | R   | False | True        |          | 4                   | This is always “4” to indicate the 4th OBX instance                                               |
| Value Type                               | 2   | ID     | 2    | R   | False | True        | 0125     | CE                  | This is always “CE” in the 4th OBX instance                                                       |
| Observation Identifier                   | 3   | CE     | 478  | R   | False |             |          |                     |                                                                                                   |
| Identifier                               | 1   | ST     | 0    | NS  |       |             |          |                     |                                                                                                   |
| Text                                     | 2   | ST     | 20   | R   |       | True        |          | ANC                 | This is always “ANC” in the 4th OBX instance                                                      |
| Name of Coding System                    | 3   | ID     | 0    | NS  |       |             |          |                     |                                                                                                   |
| Alternate Identifier                     | 4   | ST     | 0    | NS  |       |             |          |                     |                                                                                                   |
| Alternate Text                           | 5   | ST     | 0    | NS  |       |             |          |                     |                                                                                                   |
| Name of Alternate Coding System          | 6   | ID     | 0    | NS  |       |             |          |                     |                                                                                                   |
| Observation Sub-ID                       | 4   | ST     | 20   | NS  |       |             |          |                     |                                                                                                   |
| Observation Value                        | 5   | NM     | 20   | R   | False |             |          | 300                 | ANC test result                                                                                   |
| Units                                    | 6   | CE     | 483  | NS  |       |             |          |                     |                                                                                                   |
| References Range                         | 7   | ST     | 60   | NS  |       |             |          |                     |                                                                                                   |
| Abnormal Flags                           | 8   | IS     | 5    | NS  |       |             |          |                     |                                                                                                   |
| Probability                              | 9   | NM     | 5    | NS  |       |             |          |                     |                                                                                                   |
| Nature of Abnormal Test                  | 10  | ID     | 2    | NS  |       |             |          |                     |                                                                                                   |
| Observation Result Status                | 11  | ID     | 1    | R   | False | True        | 0085     | F                   | This is always “F”                                                                                |
| Effective Date of Reference Range Values | 12  | TS     | 26   | NS  |       |             |          |                     |                                                                                                   |
| User Defined Access Checks               | 13  | ST     | 20   | NS  |       |             |          |                     |                                                                                                   |
| Date/Time of the Observation             | 14  | TS     | 26   | R   | False |             |          |                     |                                                                                                   |
| Time                                     | 1   | DTM    | 24   | R   |       |             |          | 20170328134602-0500 | Date of the blood sample collection for the ANC test in the format YYYYMMDD\[HHMM\[SS\]\]\[+-ZZZZ |
| Degree of Precision                      | 2   | ID     | 0    | NS  |       |             |          |                     |                                                                                                   |
| Producer's Reference                     | 15  | CE     | 483  | NS  |       |             |          |                     |                                                                                                   |
| Responsible Observer                     | 16  | XCN    | 2930 | NS  |       |             |          |                     |                                                                                                   |
| Observation Method                       | 17  | CE     | 483  | NS  |       |             |          |                     |                                                                                                   |
| Equipment Instance Identifier            | 18  | EI     | 427  | NS  |       |             |          |                     |                                                                                                   |
| Date/Time of the Analysis                | 19  | TS     | 26   | NS  |       |             |          |                     |                                                                                                   |
| Reserved for harmonization with V2.6     | 20  | varies | 1    | NS  |       |             |          |                     |                                                                                                   |
| Reserved for harmonization with V2.6     | 21  | varies | 1    | NS  |       |             |          |                     |                                                                                                   |
| Reserved for harmonization with V2.6     | 22  | varies | 1    | NS  |       |             |          |                     |                                                                                                   |
| Performing Organization Name             | 23  | XON    | 567  | NS  |       |             |          |                     |                                                                                                   |
| Performing Organization Address          | 24  | XAD    | 631  | NS  |       |             |          |                     |                                                                                                   |
| Performing Organization Medical Director | 25  | XCN    | 3002 | NS  |       |             |          |                     |                                                                                                   |

This table displays the Clozapine Registration OBX(4) Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Patient Registration OBX(5) Segment

Table: OBX(5) Segment

| OBX(5) Field Name                        | Seq | DT     | Len  | Opt | Rep   | Fixed Value | Code Tbl | Example Value       | Implementation Notes                                                                                                          |
|------------------------------------------|-----|--------|------|-----|-------|-------------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Set ID - OBX                             | 1   | SI     | 4    | R   | False | True        |          | 5                   | This is always “5” to indicate the 5<sup>th</sup> OBX instance                                                                |
| Value Type                               | 2   | ID     | 2    | R   | False | True        | 0125     | CE                  | This is always “CE” in the 5<sup>th</sup> OBX instance                                                                        |
| Observation Identifier                   | 3   | CE     | 478  | R   | False |             |          |                     |                                                                                                                               |
| Identifier                               | 1   | ST     | 0    | NS  |       |             |          |                     |                                                                                                                               |
| Text                                     | 2   | ST     | 199  | R   |       |             |          | Facility DEA number | DEA number type description: "Facility DEA number" or "Clinic DEA number" or Pharmacy DEA number" or "Pharmacist DEA number". |
| Name of Coding System                    | 3   | ID     | 0    | NS  |       |             |          |                     |                                                                                                                               |
| Alternate Identifier                     | 4   | ST     | 0    | NS  |       |             |          |                     |                                                                                                                               |
| Alternate Text                           | 5   | ST     | 0    | NS  |       |             |          |                     |                                                                                                                               |
| Name of Alternate Coding System          | 6   | ID     | 0    | NS  |       |             |          |                     |                                                                                                                               |
| Observation Sub-ID                       | 4   | ST     | 20   | NS  |       |             |          |                     |                                                                                                                               |
| Observation Value                        | 5   | ST     | 50   | R   | False |             |          | AG9698296           | This is a DEA number (in the format 2 letters and 7 numbers)                                                                  |
| Units                                    | 6   | CE     | 483  | NS  |       |             |          |                     |                                                                                                                               |
| References Range                         | 7   | ST     | 60   | NS  |       |             |          |                     |                                                                                                                               |
| Abnormal Flags                           | 8   | IS     | 5    | NS  |       |             |          |                     |                                                                                                                               |
| Probability                              | 9   | NM     | 5    | NS  |       |             |          |                     |                                                                                                                               |
| Nature of Abnormal Test                  | 10  | ID     | 2    | NS  |       |             |          |                     |                                                                                                                               |
| Observation Result Status                | 11  | ID     | 1    | R   | False | True        | 0085     | F                   | This is always “F”                                                                                                            |
| Effective Date of Reference Range Values | 12  | TS     | 26   | NS  |       |             |          |                     |                                                                                                                               |
| User Defined Access Checks               | 13  | ST     | 20   | NS  |       |             |          |                     |                                                                                                                               |
| Date/Time of the Observation             | 14  | TS     | 26   | NS  |       |             |          |                     |                                                                                                                               |
| Producer's Reference                     | 15  | CE     | 483  | NS  |       |             |          |                     |                                                                                                                               |
| Responsible Observer                     | 16  | XCN    | 2930 | NS  |       |             |          |                     |                                                                                                                               |
| Observation Method                       | 17  | CE     | 483  | NS  |       |             |          |                     |                                                                                                                               |
| Equipment Instance Identifier            | 18  | EI     | 427  | NS  |       |             |          |                     |                                                                                                                               |
| Date/Time of the Analysis                | 19  | TS     | 26   | NS  |       |             |          |                     |                                                                                                                               |
| Reserved for harmonization with V2.6     | 20  | varies | 1    | NS  |       |             |          |                     |                                                                                                                               |
| Reserved for harmonization with V2.6     | 21  | varies | 1    | NS  |       |             |          |                     |                                                                                                                               |
| Reserved for harmonization with V2.6     | 22  | varies | 1    | NS  |       |             |          |                     |                                                                                                                               |
| Performing Organization Name             | 23  | XON    | 567  | NS  |       |             |          |                     |                                                                                                                               |
| Performing Organization Address          | 24  | XAD    | 631  | NS  |       |             |          |                     |                                                                                                                               |
| Performing Organization Medical Director | 25  | XCN    | 3002 | NS  |       |             |          |                     |                                                                                                                               |

This table displays the Clozapine Registration OBX(5) Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Patient Registration OBX(6) Segment

Table: OBX(6) Segment

| OBX(6) Field Name                        | Seq | DT     | Len  | Opt | Rep   | Fixed Value | Code Tbl | Example Value              | Implementation Notes                                                                                                                                   |
|------------------------------------------|-----|--------|------|-----|-------|-------------|----------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set ID - OBX                             | 1   | SI     | 4    | R   | False | True        |          | 6                          | This is always “6” to indicate the 6<sup>th</sup> OBX instance                                                                                         |
| Value Type                               | 2   | ID     | 2    | R   | False | True        | 0125     | CE                         | This is always “CE” in the 6<sup>th</sup> OBX instance                                                                                                 |
| Observation Identifier                   | 3   | CE     | 478  | R   | False |             |          |                            |                                                                                                                                                        |
| Identifier                               | 1   | ST     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Text                                     | 2   | ST     | 20   | R   |       | True        |          | SITELOC                    | This is always “SITELOC” in the 6<sup>th</sup> OBX instance                                                                                            |
| Name of Coding System                    | 3   | ID     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Alternate Identifier                     | 4   | ST     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Alternate Text                           | 5   | ST     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Name of Alternate Coding System          | 6   | ID     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Observation Sub-ID                       | 4   | ST     | 20   | NS  |       |             |          |                            |                                                                                                                                                        |
| Observation Value                        | 5   | ST     | 50   | R   | False |             |          | 22                         | Pointer to QUIC SORT DATA FILE (#736), that is the pointer to the Hospital Location (file \#44) which is associated with the Ward Location (file \#42) |
| Units                                    | 6   | CE     | 483  | NS  |       |             |          |                            |                                                                                                                                                        |
| References Range                         | 7   | ST     | 60   | NS  |       |             |          |                            |                                                                                                                                                        |
| Abnormal Flags                           | 8   | IS     | 5    | NS  |       |             |          |                            |                                                                                                                                                        |
| Probability                              | 9   | NM     | 5    | NS  |       |             |          |                            |                                                                                                                                                        |
| Nature of Abnormal Test                  | 10  | ID     | 2    | NS  |       |             |          |                            |                                                                                                                                                        |
| Observation Result Status                | 11  | ID     | 1    | R   | False | True        | 0085     | F                          | This is always “F”                                                                                                                                     |
| Effective Date of Reference Range Values | 12  | TS     | 26   | NS  |       |             |          |                            |                                                                                                                                                        |
| User Defined Access Checks               | 13  | ST     | 20   | NS  |       |             |          |                            |                                                                                                                                                        |
| Date/Time of the Observation             | 14  | TS     | 26   | NS  |       |             |          |                            |                                                                                                                                                        |
| Producer's Reference                     | 15  | CE     | 483  | NS  |       |             |          |                            |                                                                                                                                                        |
| Responsible Observer                     | 16  | XCN    | 2930 | NS  |       |             |          |                            |                                                                                                                                                        |
| Observation Method                       | 17  | CE     | 483  | NS  |       |             |          |                            |                                                                                                                                                        |
| Equipment Instance Identifier            | 18  | EI     | 427  | NS  |       |             |          |                            |                                                                                                                                                        |
| Date/Time of the Analysis                | 19  | TS     | 26   | NS  |       |             |          |                            |                                                                                                                                                        |
| Reserved for harmonization with V2.6     | 20  | varies | 1    | NS  |       |             |          |                            |                                                                                                                                                        |
| Reserved for harmonization with V2.6     | 21  | varies | 1    | NS  |       |             |          |                            |                                                                                                                                                        |
| Reserved for harmonization with V2.6     | 22  | VARIES | 567  | NS  |       |             |          |                            |                                                                                                                                                        |
| Performing Organization Name             | 23  | XON    | 179  | R   | False |             |          |                            |                                                                                                                                                        |
| Organization Name                        | 1   | ST     | 50   | R   |       |             |          | VAMC Name                  | Site Name                                                                                                                                              |
| Organization Name Type Code              | 2   | IS     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| ID Number                                | 3   | NM     | 0    | B   |       |             |          |                            |                                                                                                                                                        |
| Check Digit                              | 4   | NM     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Check Digit Scheme                       | 5   | ID     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Assigning Authority                      | 6   | HD     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Identifier Type Code                     | 7   | ID     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Assigning Facility                       | 8   | HD     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Name Representation Code                 | 9   | ID     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Organization Identifier                  | 10  | ST     | 20   | R   |       |             |          | 402                        | Site Number                                                                                                                                            |
| Performing Organization Address          | 24  | XAD    | 631  | R   | False |             |          |                            |                                                                                                                                                        |
| Street Address                           | 1   | SAD    | 134  | R   |       |             |          |                            |                                                                                                                                                        |
| Street or Mailing Address                | 1   | ST     | 120  | R   |       |             |          | 123 Main St.               | The 1st Line of the street address of the VAMC where patient has been treated                                                                          |
| Street Name                              | 2   | ST     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Dwelling Number                          | 3   | ST     | 12   | O   |       |             |          |                            |                                                                                                                                                        |
| Other Designation                        | 2   | ST     | 120  | RE  |       |             |          | 2nd line of street address | The 2nd Line of the street address of the VAMC where patient has been treated, if available                                                            |
| City                                     | 3   | ST     | 50   | R   |       | 1           |          | North Palm Beach address   | City where the VAMC is located                                                                                                                         |
| State or Province                        | 4   | ST     | 50   | R   |       | 1           |          | FL                         | VACM state                                                                                                                                             |
| Zip or Postal Code                       | 5   | ST     | 12   | R   |       | 1           |          | 33408                      | VAMC zip code                                                                                                                                          |
| Country                                  | 6   | ID     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Address Type                             | 7   | ID     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Other Geographic Designation             | 8   | ST     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| County/Parish Code                       | 9   | IS     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Census Tract                             | 10  | IS     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Address Representation Code              | 11  | ID     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Address Validity Range                   | 12  | DR     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Effective Date                           | 13  | TS     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Expiration Date                          | 14  | TS     | 0    | NS  |       |             |          |                            |                                                                                                                                                        |
| Performing Organization Medical Director | 25  | XCN    | 3002 | NS  |       |             |          |                            |                                                                                                                                                        |

This table displays the Clozapine Registration OBX(6) Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

### NCR Clozapine Dispense Message: RDE^O11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RDE^O11 Clozapine Dispense message is triggered when the YSCL at the individual VAMC VistA system extracts Clozaril Rollup data to generate HL7 messages.

The RDE^O11 Message Type is constructed of the following HL7 segments in the order as listed:

- MSH – Message Header
- PID – Patient Identification
- PV1 – Patient Visit
- ORC – Common Order
- RXE – Pharmacy/Treatment Encoded Order
- TQ1 – Timing/Quantity
- RXR – Pharmacy/Treatment Route
- PV1 – Patient Visit

The notation is: MSH, PID, PV1, ORC, RXE, {TQ1}, RXR

#### NCR Clozapine Dispense MSH Segment

Table: MSH Segment

<table style="width:100%;">
<caption>This table displays the Clozapine Dispense MSH Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>MSH Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Field Separator</td>
<td>1</td>
<td>ST</td>
<td>1</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td></td>
<td>|</td>
<td></td>
</tr>
<tr class="even">
<td>Encoding Characters</td>
<td>2</td>
<td>ST</td>
<td>4</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td></td>
<td>^~\&amp;</td>
<td></td>
</tr>
<tr class="odd">
<td>Sending Application</td>
<td>3</td>
<td>HD</td>
<td>227</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0361</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Namespace ID</td>
<td>1</td>
<td>IS</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0300</td>
<td>YSCL CLOZ REGISTRY</td>
<td>This is always “YSCL CLOZ REGISTRY”</td>
</tr>
<tr class="odd">
<td>Universal ID</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Universal ID Type</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Sending Facility</td>
<td>4</td>
<td>HD</td>
<td>227</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0362</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Namespace ID</td>
<td>1</td>
<td>IS</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0300</td>
<td>501 or 501GF</td>
<td>This is the site number of the sending site, e.g., 501 (parent facility) or 501GF (satellite facility)</td>
</tr>
<tr class="odd">
<td>Universal ID</td>
<td>2</td>
<td>ST</td>
<td>50</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td><p>HL7.SMA.FO-</p>
<p>ALBANY.MED.VA.GOV:5001</p></td>
<td>URL and port number of the sending facility HL7 server</td>
</tr>
<tr class="even">
<td>Universal ID Type</td>
<td>3</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0301</td>
<td>DNS</td>
<td></td>
</tr>
<tr class="odd">
<td>Receiving Application</td>
<td>5</td>
<td>HD</td>
<td>227</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0361</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Namespace ID</td>
<td>1</td>
<td>IS</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0300</td>
<td>NCR CLOZ REGISTRY</td>
<td>This is always “NCR CLOZ REGISTRY”</td>
</tr>
<tr class="odd">
<td>Universal ID</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Universal ID Type</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Receiving Facility</td>
<td>6</td>
<td>HD</td>
<td>227</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0362</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Namespace ID</td>
<td>1</td>
<td>IS</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0300</td>
<td>3000</td>
<td>Receiving facility identifier (TBD for HealthShare server - alphanumeric)</td>
</tr>
<tr class="odd">
<td>Universal ID</td>
<td>2</td>
<td>ST</td>
<td>50</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>devazrclzpv01.dev.dss.local:5001</td>
<td>URL and port number of the receiving facility HL7 server</td>
</tr>
<tr class="even">
<td>Universal ID Type</td>
<td>3</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0301</td>
<td>DNS</td>
<td></td>
</tr>
<tr class="odd">
<td>Date/Time of Message</td>
<td>7</td>
<td>TS</td>
<td>26</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Time</td>
<td>1</td>
<td>DTM</td>
<td>24</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>20170328134602-0500</td>
<td>Date/time the message was created in format YYYYMMDD[HHMM[SS]][+-ZZZZ]00</td>
</tr>
<tr class="odd">
<td>Degree of Precision</td>
<td>2</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Security</td>
<td>8</td>
<td>ST</td>
<td>40</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Message Type</td>
<td>9</td>
<td>MSG</td>
<td>15</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Message Code</td>
<td>1</td>
<td>ID</td>
<td>3</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0076</td>
<td>ADT</td>
<td>This is always “RDE”</td>
</tr>
<tr class="odd">
<td>Trigger Event</td>
<td>2</td>
<td>ID</td>
<td>3</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0003</td>
<td>A28</td>
<td>This is always “O11”</td>
</tr>
<tr class="even">
<td>Message Structure</td>
<td>3</td>
<td>ID</td>
<td>7</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0354</td>
<td>ADT_A05</td>
<td>This is always “RDE_O11”</td>
</tr>
<tr class="odd">
<td>Message Control ID</td>
<td>10</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td>12354</td>
<td>Generated by the HL7 module in VistA</td>
</tr>
<tr class="even">
<td>Processing ID</td>
<td>11</td>
<td>PT</td>
<td>3</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Processing ID</td>
<td>1</td>
<td>ID</td>
<td>1</td>
<td>R</td>
<td></td>
<td></td>
<td>0103</td>
<td>P</td>
<td><p>“P” -Production</p>
<p>“T” - Test</p></td>
</tr>
<tr class="even">
<td>Processing Mode</td>
<td>2</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Version ID</td>
<td>12</td>
<td>VID</td>
<td>973</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Version ID</td>
<td>1</td>
<td>ID</td>
<td>5</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0104</td>
<td>2.5.1</td>
<td>This is always “2.5.1”</td>
</tr>
<tr class="odd">
<td>Internationalization Code</td>
<td>2</td>
<td>CE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>International Version ID</td>
<td>3</td>
<td>CE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Sequence Number</td>
<td>13</td>
<td>NM</td>
<td>15</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Continuation Pointer</td>
<td>14</td>
<td>ST</td>
<td>180</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Accept Acknowledgment Type</td>
<td>15</td>
<td>ID</td>
<td>2</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td>0155</td>
<td>AL</td>
<td>This is always “AL”</td>
</tr>
<tr class="even">
<td>Application Acknowledgment Type</td>
<td>16</td>
<td>ID</td>
<td>2</td>
<td>R</td>
<td>False</td>
<td>True</td>
<td>0155</td>
<td>AL</td>
<td>This is always “AL”</td>
</tr>
<tr class="odd">
<td>Country Code</td>
<td>17</td>
<td>ID</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Character Set</td>
<td>18</td>
<td>ID</td>
<td>16</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Principal Language of Message</td>
<td>19</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Character Set Handling Scheme</td>
<td>20</td>
<td>ID</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Message Profile Identifier</td>
<td>21</td>
<td>EI</td>
<td>427</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Dispense MSH Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Clozapine Dispense PID Segment

Table: PID Segment

<table style="width:100%;">
<caption>This table displays the Clozapine Dispense PID Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>PID Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Set ID - PID</td>
<td>1</td>
<td>SI</td>
<td>4</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patient ID</td>
<td>2</td>
<td>CX</td>
<td>1913</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Patient Identifier List</td>
<td>3</td>
<td>CX</td>
<td>1912</td>
<td>R</td>
<td>True</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ID Number</td>
<td>1</td>
<td>ST</td>
<td>15</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td><p>VA12345<br />
or</p>
<p>111223344<br />
or</p>
<p>1000720100V271387<br />
or</p>
<p>100234567</p></td>
<td>The 1st instance is the patient's Clozaril authorization number (NCR's number – 2 letters followed by 5 numbers). The 2nd instance is the patient's SSN. The 3<sup>rd</sup> instance is the patient ICN. The 4<sup>th</sup> instance is the patient DFN</td>
</tr>
<tr class="odd">
<td>Check Digit</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Check Digit Scheme</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Assigning Authority</td>
<td>4</td>
<td>HD</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier Type Code</td>
<td>5</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0203</td>
<td>PN or SS</td>
<td>The 1<sup>st</sup> instance is "PN" - Patient's Clozaril authorization number. The 2<sup>nd</sup> instance is "SS" – Patient’s Social Security.</td>
</tr>
<tr class="odd">
<td>Assigning Facility</td>
<td>6</td>
<td>HD</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Effective Date</td>
<td>7</td>
<td>DT</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Expiration Date</td>
<td>8</td>
<td>DT</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Assigning Jurisdiction</td>
<td>9</td>
<td>CWE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Assigning Agency or Department</td>
<td>10</td>
<td>CWE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Patient ID - PID</td>
<td>4</td>
<td>CX</td>
<td>1913</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Patient Name</td>
<td>5</td>
<td>XPN</td>
<td>1044</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Family Name</td>
<td>1</td>
<td>FN</td>
<td>194</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Surname</td>
<td>1</td>
<td>ST</td>
<td>50</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Doe</td>
<td>Last Name</td>
</tr>
<tr class="even">
<td>Own Surname Prefix</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Own Surname</td>
<td>3</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Surname Prefix from Partner/Spouse</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Surname from Partner/Spouse</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Given Name</td>
<td>2</td>
<td>ST</td>
<td>50</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>John</td>
<td>First Name</td>
</tr>
<tr class="odd">
<td>Second and Further Given Names or Initials Thereof</td>
<td>3</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Suffix (e.g., JR or III)</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Prefix (e.g., DR)</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Degree (e.g., MD)</td>
<td>6</td>
<td>IS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Type Code</td>
<td>7</td>
<td>ID</td>
<td>1</td>
<td>R</td>
<td></td>
<td></td>
<td>0200</td>
<td>L</td>
<td>This is always "L"</td>
</tr>
<tr class="even">
<td>Name Representation Code</td>
<td>8</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Context</td>
<td>9</td>
<td>CE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name Validity Range</td>
<td>10</td>
<td>DR</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Assembly Order</td>
<td>11</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Effective Date</td>
<td>12</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Expiration Date</td>
<td>13</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Professional Suffix</td>
<td>14</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Mother's Maiden Name</td>
<td>6</td>
<td>XPN</td>
<td>1044</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Date/Time of Birth</td>
<td>7</td>
<td>TS</td>
<td>26</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Time</td>
<td>1</td>
<td>DTM</td>
<td>24</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>19700101</td>
<td>YYYYMMDD</td>
</tr>
<tr class="even">
<td>Degree of Precision</td>
<td>2</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Administrative Sex</td>
<td>8</td>
<td>IS</td>
<td>1</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0001</td>
<td>M</td>
<td></td>
</tr>
<tr class="even">
<td>Patient Alias</td>
<td>9</td>
<td>XPN</td>
<td>1044</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Race</td>
<td>10</td>
<td>CE</td>
<td>478</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0005</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0005</td>
<td>2028-9</td>
<td></td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Asian</td>
<td>Race Identifier description</td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0396</td>
<td>HL70005</td>
<td>HL7 Defined Code where nnnn is the HL7 table number 0005. This is always “HL70005”.</td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patient Address</td>
<td>11</td>
<td>XAD</td>
<td>513</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Street Address</td>
<td>1</td>
<td>SAD</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Other Designation</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>City</td>
<td>3</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>State or Province</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Zip or Postal Code</td>
<td>5</td>
<td>ST</td>
<td>12</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>33408</td>
<td></td>
</tr>
<tr class="even">
<td>Country</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Address Type</td>
<td>7</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Other Geographic Designation</td>
<td>8</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>County/Parish Code</td>
<td>9</td>
<td>IS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Census Tract</td>
<td>10</td>
<td>IS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Address Representation Code</td>
<td>11</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Address Validity Range</td>
<td>12</td>
<td>DR</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Effective Date</td>
<td>13</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Expiration Date</td>
<td>14</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>County Code</td>
<td>12</td>
<td>IS</td>
<td>4</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Phone Number - Home</td>
<td>13</td>
<td>XTN</td>
<td>651</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Phone Number - Business</td>
<td>14</td>
<td>XTN</td>
<td>651</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Primary Language</td>
<td>15</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Marital Status</td>
<td>16</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td>False</td>
<td></td>
<td></td>
<td>3.4.2.16</td>
<td></td>
</tr>
<tr class="even">
<td>Religion</td>
<td>17</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Patient Account Number</td>
<td>18</td>
<td>CX</td>
<td>1912</td>
<td>NS</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>SSN Number - Patient</td>
<td>19</td>
<td>ST</td>
<td>16</td>
<td>NS</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Driver's License Number - Patient</td>
<td>20</td>
<td>DLN</td>
<td>66</td>
<td>NS</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Mother's Identifier</td>
<td>21</td>
<td>CX</td>
<td>1912</td>
<td>NS</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Ethnic Group</td>
<td>22</td>
<td>CE</td>
<td>478</td>
<td>RE</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td>0189</td>
<td>U</td>
<td></td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Unknown</td>
<td>Ethnic Identifier description</td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True</td>
<td>0396</td>
<td>HL70189</td>
<td>HL7 Defined Code where nnnn is the HL7 table number 0005. This is always “HL70189”.</td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Birth Place</td>
<td>23</td>
<td>ST</td>
<td>250</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Multiple Birth Indicator</td>
<td>24</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Birth Order</td>
<td>25</td>
<td>NM</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Citizenship</td>
<td>26</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Veterans Military Status</td>
<td>27</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Nationality</td>
<td>28</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patient Death Date and Time</td>
<td>29</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Patient Death Indicator</td>
<td>30</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identity Unknown Indicator</td>
<td>31</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Identity Reliability Code</td>
<td>32</td>
<td>IS</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Last Update Date/Time</td>
<td>33</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Last Update Facility</td>
<td>34</td>
<td>HD</td>
<td>241</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Species Code</td>
<td>35</td>
<td>CE</td>
<td>478</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Breed Code</td>
<td>36</td>
<td>CE</td>
<td>478</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Strain</td>
<td>37</td>
<td>ST</td>
<td>80</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Production Class Code</td>
<td>38</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Tribal Citizenship</td>
<td>39</td>
<td>CWE</td>
<td>705</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Dispense PID Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Clozapine Dispense PV1 Segment

Table: PV1 Segment

<table style="width:100%;">
<caption>This table displays the Clozapine Dispense PV1 Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>PV1 Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Set ID - PV1</td>
<td>1</td>
<td>SI</td>
<td>4</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patient Class</td>
<td>2</td>
<td>IS</td>
<td>1</td>
<td>R</td>
<td>False</td>
<td></td>
<td>0004</td>
<td>O or I</td>
<td><p>“O” - Outpatient</p>
<p>“I” - Inpatient</p></td>
</tr>
<tr class="odd">
<td>Assigned Patient Location</td>
<td>3</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Admission Type</td>
<td>4</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Preadmit Number</td>
<td>5</td>
<td>CX</td>
<td>1912</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Prior Patient Location</td>
<td>6</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Attending Doctor</td>
<td>7</td>
<td>XCN</td>
<td>2930</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Referring Doctor</td>
<td>8</td>
<td>XCN</td>
<td>2930</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Consulting Doctor</td>
<td>9</td>
<td>XCN</td>
<td>2945</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Hospital Service</td>
<td>10</td>
<td>IS</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Temporary Location</td>
<td>11</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Preadmit Test Indicator</td>
<td>12</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Re-admission Indicator</td>
<td>13</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Admit Source</td>
<td>14</td>
<td>IS</td>
<td>6</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Ambulatory Status</td>
<td>15</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VIP Indicator</td>
<td>16</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Admitting Doctor</td>
<td>17</td>
<td>XCN</td>
<td>2930</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Patient Type</td>
<td>18</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Visit Number</td>
<td>19</td>
<td>CX</td>
<td>1912</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Financial Class</td>
<td>20</td>
<td>FC</td>
<td>50</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Charge Price Indicator</td>
<td>21</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Courtesy Code</td>
<td>22</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Credit Rating</td>
<td>23</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Contract Code</td>
<td>24</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Contract Effective Date</td>
<td>25</td>
<td>DT</td>
<td>8</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Contract Amount</td>
<td>26</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Contract Period</td>
<td>27</td>
<td>NM</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Interest Code</td>
<td>28</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Transfer to Bad Debt Code</td>
<td>29</td>
<td>IS</td>
<td>4</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Transfer to Bad Debt Date</td>
<td>30</td>
<td>DT</td>
<td>8</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Bad Debt Agency Code</td>
<td>31</td>
<td>IS</td>
<td>10</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bad Debt Transfer Amount</td>
<td>32</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Bad Debt Recovery Amount</td>
<td>33</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Delete Account Indicator</td>
<td>34</td>
<td>IS</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Delete Account Date</td>
<td>35</td>
<td>DT</td>
<td>8</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Discharge Disposition</td>
<td>36</td>
<td>IS</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Discharged to Location</td>
<td>37</td>
<td>DLD</td>
<td>47</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Diet Type</td>
<td>38</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Servicing Facility</td>
<td>39</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Bed Status</td>
<td>40</td>
<td>IS</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Account Status</td>
<td>41</td>
<td>IS</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Pending Location</td>
<td>42</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Prior Temporary Location</td>
<td>43</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Admit Date/Time</td>
<td>44</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Discharge Date/Time</td>
<td>45</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Current Patient Balance</td>
<td>46</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Total Charges</td>
<td>47</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Total Adjustments</td>
<td>48</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Total Payments</td>
<td>49</td>
<td>NM</td>
<td>12</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Visit ID</td>
<td>50</td>
<td>CX</td>
<td>1912</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Visit Indicator</td>
<td>51</td>
<td>IS</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Other Healthcare Provider</td>
<td>52</td>
<td>XCN</td>
<td>2945</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Dispense PV1 Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Clozapine Dispense ORC Segment

Table: ORC Segment

| ORC Field Name                                     | Seq | DT  | Len  | Opt | Rep   | Fixed Value | Code Tbl | Example Value | Implementation Notes                                 |
|----------------------------------------------------|-----|-----|------|-----|-------|-------------|----------|---------------|------------------------------------------------------|
| Order Control                                      | 1   | ID  | 2    | R   | False | True        | 0119     | RE            | This is always “RE”                                  |
| Placer Order Number                                | 2   | EI  | 424  | NS  |       |             |          |               |                                                      |
| Filler Order Number                                | 3   | EI  | 424  | NS  |       |             |          |               |                                                      |
| Placer Group Number                                | 4   | EI  | 427  | NS  |       |             |          |               |                                                      |
| Order Status                                       | 5   | ID  | 2    | NS  |       |             |          |               |                                                      |
| Response Flag                                      | 6   | ID  | 1    | NS  |       |             |          |               |                                                      |
| Quantity/Timing                                    | 7   | TQ  | 1778 | NS  |       |             |          |               |                                                      |
| Parent                                             | 8   | EIP | 855  | NS  |       |             |          |               |                                                      |
| Date/Time of Transaction                           | 9   | TS  | 26   | R   | False |             |          |               |                                                      |
| Time                                               | 1   | DTM | 24   | R   |       |             |          | 20170328      | Date prescribed YYYYMMDD                             |
| Degree of Precision                                | 2   | ID  | 0    | NS  |       |             |          |               |                                                      |
| Entered By                                         | 10  | XCN | 2930 | NS  |       |             |          |               |                                                      |
| Verified By                                        | 11  | XCN | 2930 | NS  |       |             |          |               |                                                      |
| Ordering Provider                                  | 12  | XCN | 2930 | R   | False |             |          |               |                                                      |
| ID Number                                          | 1   | ST  | 20   | R   |       |             |          | 1235319599    | This is the NPI number of the prescribing physician. |
| Family Name                                        | 2   | FN  | 194  | R   |       |             |          |               |                                                      |
| Surname                                            | 1   | ST  | 50   | R   |       |             |          | Lastname      | Last name of the prescribing physician               |
| Own Surname Prefix                                 | 2   | ST  | 0    | NS  |       |             |          |               |                                                      |
| Own Surname                                        | 3   | ST  | 0    | NS  |       |             |          |               |                                                      |
| Surname Prefix from Partner/Spouse                 | 4   | ST  | 0    | NS  |       |             |          |               |                                                      |
| Surname from Partner/Spouse                        | 5   | ST  | 0    | NS  |       |             |          |               |                                                      |
| Given Name                                         | 3   | ST  | 30   | R   |       |             |          | Firstname     | First name of the prescribing physician              |
| Second and Further Given Names or Initials Thereof | 4   | ST  | 0    | NS  |       |             |          |               |                                                      |
| Suffix (e.g., JR or III)                           | 5   | ST  | 0    | NS  |       |             |          |               |                                                      |
| Prefix (e.g., DR)                                  | 6   | ST  | 0    | NS  |       |             |          |               |                                                      |
| Degree (e.g., MD)                                  | 7   | IS  | 0    | NS  |       |             |          |               |                                                      |
| Source Table                                       | 8   | IS  | 0    | NS  |       |             |          |               |                                                      |
| Assigning Authority                                | 9   | HD  | 0    | NS  |       |             |          |               |                                                      |
| Name Type Code                                     | 10  | ID  | 0    | NS  |       |             |          |               |                                                      |
| Identifier Check Digit                             | 11  | ST  | 0    | NS  |       |             |          |               |                                                      |
| Check Digit Scheme                                 | 12  | ID  | 0    |     |       |             |          |               |                                                      |
| Identifier Type Code                               | 13  | ID  | 3    | R   |       | True        | 0203     | NPI           | This is always "NPI"                                 |
| Assigning Facility                                 | 14  | HD  | 0    | NS  |       |             |          |               |                                                      |
| Name Representation Code                           | 15  | ID  | 0    | NS  |       |             |          |               |                                                      |
| Name Context                                       | 16  | CE  | 0    | NS  |       |             |          |               |                                                      |
| Name Validity Range                                | 17  | DR  | 0    | NS  |       |             |          |               |                                                      |
| Name Assembly Order                                | 18  | ID  | 0    | NS  |       |             |          |               |                                                      |
| Effective Date                                     | 19  | TS  | 0    | NS  |       |             |          |               |                                                      |
| Expiration Date                                    | 20  | TS  | 0    | NS  |       |             |          |               |                                                      |
| Professional Suffix                                | 21  | ST  | 0    | NS  |       |             |          |               |                                                      |
| Assigning Jurisdiction                             | 22  | CWE | 0    | NS  |       |             |          |               |                                                      |
| Assigning Agency or Department                     | 23  | CWE | 0    | NS  |       |             |          |               |                                                      |
| Enterer's Location                                 | 13  | PL  | 1230 | NS  |       |             |          |               |                                                      |
| Call Back Phone Number                             | 14  | XTN | 651  | NS  |       |             |          |               |                                                      |
| Order Effective Date/Time                          | 15  | TS  | 26   | NS  |       |             |          |               |                                                      |
| Order Control Code Reason                          | 16  | CE  | 483  | NS  |       |             |          |               |                                                      |
| Entering Organization                              | 17  | CE  | 483  | NS  |       |             |          |               |                                                      |
| Entering Device                                    | 18  | CE  | 483  | NS  |       |             |          |               |                                                      |
| Action By                                          | 19  | XCN | 2930 | NS  |       |             |          |               |                                                      |
| Advanced Beneficiary Notice Code                   | 20  | CE  | 483  | NS  |       |             |          |               |                                                      |
| Ordering Facility Name                             | 21  | XON | 563  | NS  |       |             |          |               |                                                      |
| Ordering Facility Address                          | 22  | XAD | 513  | NS  |       |             |          |               |                                                      |
| Ordering Facility Phone Number                     | 23  | XTN | 651  | NS  |       |             |          |               |                                                      |
| Ordering Provider Address                          | 24  | XAD | 513  | NS  |       |             |          |               |                                                      |
| Order Status Modifier                              | 25  | CWE | 705  | NS  |       |             |          |               |                                                      |
| Advanced Beneficiary Notice Override Reason        | 26  | CWE | 697  | NS  |       |             |          |               |                                                      |
| Filler's Expected Availability Date/Time           | 27  | TS  | 26   | NS  |       |             |          |               |                                                      |
| Confidentiality Code                               | 28  | CWE | 705  | NS  |       |             |          |               |                                                      |
| Order Type                                         | 29  | CWE | 705  | NS  |       |             |          |               |                                                      |
| Enterer Authorization Mode                         | 30  | CNE | 697  | NS  |       |             |          |               |                                                      |
| Parent Universal Service Identifier                | 31  | CWE | 705  | NS  |       |             |          |               |                                                      |

This table displays the Clozapine Dispense ORC Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Clozapine Dispense RXE Segment

Table: RXE Segment

<table>
<caption>This table displays the Clozapine Dispense RXE Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>RXE Field Name</th>
<th>Seq</th>
<th>DT</th>
<th>Len</th>
<th>Opt</th>
<th>Rep</th>
<th>Fixed Value</th>
<th>Code Tbl</th>
<th>Example Value</th>
<th>Implementation Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Quantity/Timing</td>
<td>1</td>
<td>TQ</td>
<td>1778</td>
<td>NS</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Give Code</td>
<td>2</td>
<td>CE</td>
<td>478</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>64725-1260</td>
<td>NDC Number</td>
</tr>
<tr class="odd">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>199</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Clozaril</td>
<td>Drug Name</td>
</tr>
<tr class="even">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>20</td>
<td>R</td>
<td></td>
<td>True T</td>
<td>0396</td>
<td>NDC</td>
<td>This is always “NDC”</td>
</tr>
<tr class="odd">
<td>Give Amount - Minimum</td>
<td>3</td>
<td>NM</td>
<td>20</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td>100</td>
<td></td>
</tr>
<tr class="even">
<td>Give Amount - Maximum</td>
<td>4</td>
<td>NM</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Give Units</td>
<td>5</td>
<td>CE</td>
<td>478</td>
<td>R</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>MG</td>
<td></td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Give Dosage Form</td>
<td>6</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Provider's Administration Instructions</td>
<td>7</td>
<td>CE</td>
<td>483</td>
<td>RE</td>
<td>False</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>0</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>91</td>
<td></td>
</tr>
<tr class="odd">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Deliver-To Location</td>
<td>8</td>
<td>LA1</td>
<td>790</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Substitution Status</td>
<td>9</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Dispense Amount</td>
<td>10</td>
<td>NM</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Dispense Units</td>
<td>11</td>
<td>CE</td>
<td>478</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Number of Refills</td>
<td>12</td>
<td>NM</td>
<td>3</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Ordering Provider's DEA Number</td>
<td>13</td>
<td>XCN</td>
<td>2930</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Pharmacist/Treatment Supplier's Verifier ID</td>
<td>14</td>
<td>XCN</td>
<td>2930</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Only if REX.7 is populated</td>
</tr>
<tr class="odd">
<td>ID Number</td>
<td>1</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>AR7071296</td>
<td><p>The 1st instance is the DEA number of</p>
<p>the prescriber who approved the</p>
<p>denial/override.</p>
<p>The 2nd instance is this prescriber's</p>
<p>DUZ number from file 200.</p></td>
</tr>
<tr class="even">
<td>Family Name</td>
<td>2</td>
<td>FN</td>
<td>194</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Surname</td>
<td>1</td>
<td>ST</td>
<td>50</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Lastname</td>
<td><p>Last name of the prescriber who approved the</p>
<p>denial/override.</p></td>
</tr>
<tr class="even">
<td>Own Surname Prefix</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Own Surname</td>
<td>3</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Surname Prefix from Partner/Spouse</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Surname from Partner/Spouse</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Given Name</td>
<td>3</td>
<td>ST</td>
<td>30</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>Firstname</td>
<td>First name of prescriber who approved the denial/override.</td>
</tr>
<tr class="odd">
<td>Second and Further Given Names or Initials Thereof</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Suffix (e.g., JR or III)</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Prefix (e.g., DR)</td>
<td>6</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Degree (e.g., MD)</td>
<td>7</td>
<td>IS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Source Table</td>
<td>8</td>
<td>IS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Assigning Authority</td>
<td>9</td>
<td>HD</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Type Code</td>
<td>10</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier Check Digit</td>
<td>11</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Check Digit Scheme</td>
<td>12</td>
<td>ID</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Identifier Type Code</td>
<td>13</td>
<td>ID</td>
<td>3</td>
<td>R</td>
<td></td>
<td></td>
<td>0203</td>
<td>DEA</td>
<td>The 1st instance is "DEA", the 2nd instance is "PN".</td>
</tr>
<tr class="odd">
<td>Assigning Facility</td>
<td>14</td>
<td>HD</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name Representation Code</td>
<td>15</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Context</td>
<td>16</td>
<td>CE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name Validity Range</td>
<td>17</td>
<td>DR</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name Assembly Order</td>
<td>18</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Effective Date</td>
<td>19</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Expiration Date</td>
<td>20</td>
<td>TS</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Professional Suffix</td>
<td>21</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Assigning Jurisdiction</td>
<td>22</td>
<td>CWE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Assigning Agency or Department</td>
<td>23</td>
<td>CWE</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Prescription Number</td>
<td>15</td>
<td>ST</td>
<td>20</td>
<td>C</td>
<td></td>
<td></td>
<td></td>
<td>13519100</td>
<td><p>If patient type in PV1.2 is "I" (Inpatient), then it is an order number.</p>
<p>If patient type in PV1.2 is "O"</p>
<p>(Outpatient), it is a prescription number.</p></td>
</tr>
<tr class="even">
<td>Number of Refills Remaining</td>
<td>16</td>
<td>NM</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Number of Refills/Doses Dispensed</td>
<td>17</td>
<td>NM</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>D/T of Most Recent Refill or Dose Dispensed</td>
<td>18</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Total Daily Dose</td>
<td>19</td>
<td>CQ</td>
<td>499</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Needs Human Review</td>
<td>20</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Pharmacy/Treatment Supplier's Special Dispensing Instructions</td>
<td>21</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Give Per (Time Unit)</td>
<td>22</td>
<td>ST</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Give Rate Amount</td>
<td>23</td>
<td>ST</td>
<td>6</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Give Rate Units</td>
<td>24</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Give Strength</td>
<td>25</td>
<td>NM</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Give Strength Units</td>
<td>26</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Give Indication</td>
<td>27</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Dispense Package Size</td>
<td>28</td>
<td>NM</td>
<td>20</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Dispense Package Size Unit</td>
<td>29</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Dispense Package Method</td>
<td>30</td>
<td>ID</td>
<td>2</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Supplementary Code</td>
<td>31</td>
<td>CE</td>
<td>483</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Original Order Date/Time</td>
<td>32</td>
<td>TS</td>
<td>26</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Give Drug Strength Volume</td>
<td>33</td>
<td>NM</td>
<td>5</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Give Drug Strength Volume Units</td>
<td>34</td>
<td>CWE</td>
<td>705</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Controlled Substance Schedule</td>
<td>35</td>
<td>CWE</td>
<td>705</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Formulary Status</td>
<td>36</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Pharmaceutical Substance Alternative</td>
<td>37</td>
<td>CWE</td>
<td>705</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Pharmacy of Most Recent Fill</td>
<td>38</td>
<td>CWE</td>
<td>705</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Initial Dispense Amount</td>
<td>39</td>
<td>NM</td>
<td>250</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Dispensing Pharmacy</td>
<td>40</td>
<td>CWE</td>
<td>705</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Identifier</td>
<td>1</td>
<td>ST</td>
<td>20</td>
<td>R</td>
<td></td>
<td></td>
<td></td>
<td>1234567</td>
<td>This is pharmacy number NCPDP</td>
</tr>
<tr class="even">
<td>Text</td>
<td>2</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Name of Coding System</td>
<td>3</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Identifier</td>
<td>4</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Alternate Text</td>
<td>5</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Name of Alternate Coding System</td>
<td>6</td>
<td>ID</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Coding System Version</td>
<td>7</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Alternate Coding System Version ID</td>
<td>8</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Original Text</td>
<td>9</td>
<td>ST</td>
<td>0</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Dispensing Pharmacy Address</td>
<td>41</td>
<td>XAD</td>
<td>513</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Deliver-to Patient Location</td>
<td>42</td>
<td>PL</td>
<td>1230</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Deliver-to Address</td>
<td>43</td>
<td>XAD</td>
<td>513</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Pharmacy Order Type</td>
<td>44</td>
<td>ID</td>
<td>1</td>
<td>NS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

This table displays the Clozapine Dispense RXE Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Clozapine Dispense TQ1 Segment

Table: TQ1 Segment

| TQ1 Field Name                  | Seq | DT  | Len | Opt | Rep   | Fixed Value | Code Tbl | Example Value | Implementation Notes                                                           |
|---------------------------------|-----|-----|-----|-----|-------|-------------|----------|---------------|--------------------------------------------------------------------------------|
| Set ID - TQ1                    | 1   | SI  | 4   | R   | False |             |          | 1             | This is consecutive numbers 1, 2, 3, etc. to indicate the order of repetitions |
| Quantity                        | 2   | CQ  | 500 | R   | False |             |          |               |                                                                                |
| Quantity                        | 1   | NM  | 16  | R   |       |             |          | 100           | This is drug dosage amount                                                     |
| Units                           | 2   | CE  | 483 | R   |       |             |          |               |                                                                                |
| Identifier                      | 1   | ST  | 20  | R   |       |             |          | MG            | This is drug dosage units                                                      |
| Text                            | 2   | ST  | 0   | NS  |       |             |          |               |                                                                                |
| Name of Coding System           | 3   | ID  | 0   | NS  |       |             |          |               |                                                                                |
| Alternate Identifier            | 4   | ST  | 0   | NS  |       |             |          |               |                                                                                |
| Alternate Text                  | 5   | ST  | 0   | NS  |       |             |          |               |                                                                                |
| Name of Alternate Coding System | 6   | ID  | 0   | NS  |       |             |          |               |                                                                                |
| Repeat Pattern                  | 3   | RPT | 984 | NS  |       |             |          |               |                                                                                |
| Explicit Time                   | 4   | TM  | 20  | NS  |       |             |          |               |                                                                                |
| Relative Time and Units         | 5   | CQ  | 500 | NS  |       |             |          |               |                                                                                |
| Service Duration                | 6   | CQ  | 500 | NS  |       |             |          |               |                                                                                |
| Start date/time                 | 7   | TS  | 26  | NS  |       |             |          |               |                                                                                |
| End date/time                   | 8   | TS  | 26  | NS  |       |             |          |               |                                                                                |
| Priority                        | 9   | CWE | 705 | NS  |       |             |          |               |                                                                                |
| Condition text                  | 10  | TX  | 250 | NS  |       |             |          |               |                                                                                |
| Text instruction                | 11  | TX  | 250 | NS  |       |             |          |               |                                                                                |
| Conjunction                     | 12  | ID  | 10  | NS  |       |             |          |               |                                                                                |
| Occurrence duration             | 13  | CQ  | 500 | NS  |       |             |          |               |                                                                                |
| Total occurrence's              | 14  | NM  | 10  | NS  |       |             |          |               |                                                                                |

This table displays the Clozapine Dispense TQ1 Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value

#### NCR Clozapine Dispense RXR Segment

Table: RXR Segment

| RXR Field Name               | Seq | DT  | Len | Opt | Rep   | Fixed Value | Code Tbl | Example Value | Implementation Notes          |
|------------------------------|-----|-----|-----|-----|-------|-------------|----------|---------------|-------------------------------|
| Route                        | 1   | CE  | 478 | R   | False |             |          |               |                               |
| Identifier                   | 1   | ST  | 20  | R   |       | True        | 0162     | PO            | This is always “PO” for oral. |
| Text                         | 2   | ST  | 199 | R   |       | True        |          | ORAL          | This is always “ORAL”         |
| Name of Coding System        | 3   | ID  | 20  | R   |       | True        | 0396     | HL70162       | This is always “HL70162”      |
| Alternate Identifier         | 4   | ST  | 0   | NS  |       |             |          |               |                               |
| Alternate Text               | 5   | ST  | 0   | NS  |       |             |          |               |                               |
| Alternate Coding System Name | 6   | ID  | 0   | NS  |       |             |          |               |                               |
| Administration Site          | 2   | CWE | 705 | NS  |       |             |          |               |                               |
| Administration Device        | 3   | CE  | 483 | NS  |       |             |          |               |                               |
| Administration Method        | 4   | CWE | 705 | NS  |       |             |          |               |                               |
| Routing Instruction          | 5   | CE  | 483 | NS  |       |             |          |               |                               |
| Administration Site Modifier | 6   | CWE | 705 | NS  |       |             |          |               |                               |

This table displays the Clozapine Dispense RXR Segment by Name, Seq, DT, Opt, Rep, Fixed Value, Code Tbl, and Example Value