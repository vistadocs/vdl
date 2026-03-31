---
title: Benefits Management Version 4 Technical Manual/Security Guide
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: PSU
app_name: "Pharmacy: Benefits Management"
section: CLI
app_status: active
pkg_ns: PSU
patch_ver: 4
patch_id: PSU*4
group_key: "PSU:PSU:4"
file_numbers: []
security_keys: []
menu_options: 3
description: 
audience: 
keywords: 
  - table
  - pharmacy
  - class
  - contents
  - patient
  - strong
  - drug
  - manual
  - options
  - management
page_count: 0
word_count: 3458
section_count: 6
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_tm_r0714.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_tm_r0714.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=91"
---

---
title: |
  <span id="_Toc495855387" class="anchor"></span>Pharmacy Benefits Management (PBM)

  Technical Manual/Security Guide
---

![](benefits-management-version-4-technical-manual-security-guide/001.png)

Software Version 4.0

June 2005

Office of Information and Technology (OI&T)

Product Development

|                      |
|----------------------|
| Revision History |

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Date</p>
</blockquote></td>
<td><strong>Revised Pages</strong></td>
<td><strong>Patch Number</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>7/2014</td>
<td>i, <a href="#p19_18">18</a></td>
<td>PSU*4*19</td>
<td><p>Added new API $$CSI^ICDEX() to Section 8.1, Integration Agreements (IAs).</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>07/2012</td>
<td>19</td>
<td>PSU*4*20</td>
<td><p>Updated only the Callable Routines section on this page.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/2006</td>
<td><p>iii,</p>
<p>5, 9, 11, 15,</p>
<p>17-19,</p>
<p>21</p></td>
<td>PSU*4*3</td>
<td><p>PBM Extract Enhancements #3 project. Updated Table of Contents. Added PBM Health Level 7 (HL7) Chemistry Lab messaging functionality to applicable sections.</p>
<p>Added routines PSULRHL1, PSULRHL2, and PSULRHL3 to Routines section. Added references to HLO package to External Relations and Internal Relations sections. Added list of DBIA’s to Section 8.1, Integration Agreements.</p>
<p>Added new Glossary entries for CMOP-NAT, HL7, and HLO.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>06/2005</td>
<td>All</td>
<td></td>
<td><p>Original Released PBM V. 4.0 Technical Manual</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

*(This page included for two-sided copying.)*

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Orientation](#orientation)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Resource Requirements](#resource-requirements)
  - [Implementation Requirements](#implementation-requirements)
  - [System Configuration](#system-configuration)
- [Files](#files)
- [Routines](#routines)
- [Exported Options](#exported-options)
  - [New Options](#new-options)
- [Archiving and Purging](#archiving-and-purging)
- [External Relations](#external-relations)
  - [Integration Agreements (IAs)](#integration-agreements-ias)
- [Callable Routines](#callable-routines)
- [Internal Relations](#internal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [Technical Assistance](#technical-assistance)
- [Software Product Security](#software-product-security)
- [Glossary](#glossary)
Pharmacy Benefits Management (PBM) Version 4.0 is a new enhanced version of the software and replaces PBM Version 3.0. In a series of three enhancements, new extracts and reports were created, existing extracts were modified, and some options were modified to increase the functionality of this software package. For more detail, refer to the *Pharmacy Benefits Management V. 4.0 Release Notes* document.
The software extracts medication dispensing data elements from the Outpatient Pharmacy, Inpatient Medications Intravenous (IV) and Unit Dose (UD), Automatic Replenishment/Ward Stock (AR/WS), Controlled Substances (CS) modules, Procurement information from Drug Accountability, Integrated Funds Control, Accounting and Procurement (IFCAP), and a limited amount of Laboratory data on a monthly basis.
The extracted data is electronically exported via MailMan to the PBM section at <span class="mark">REDACTED</span> Department of Veterans Affairs Medical Center (VAMC). MailMan messages are downloaded to text files onto the PBM network. These electronic messages are then passed through a translation process, which pulls text files into a database format and is checked for quality assurance and converts all local drug names to a common drug name and all local dispensing units to a common dispensing unit if possible. After translation, the information is added to the PBM national database.
Through an option placed on the pharmacy supervisor menu, the software makes data extraction reports available at local VAMCs and allows local management to use this data to project local drug usage and identify potential drug accountability problem areas. The PBM section is able to provide information on Local Facility, Veterans Integrated Service Network (VISN), and National product use on monthly, quarterly, and annual intervals. Pharmacy personnel at VAMCs and VISNs shall use this application to collect and report on pharmacy and patient statistics through user-executed options. Users of the database include the PBM, VAMCs, VISNs, and the research community.
PBM Version 4.0 extracts additional data elements and modifies current extracts to take advantage of enhancements made to the other Pharmacy modules since the release of previous versions (D&PPM V. 2.0) and PBM Version 3.0.
The enhancements included in PBM V.4.0 are documented in the Pharmacy Benefits Management Release Notes V. 4.0.
Related Manuals
*Pharmacy Benefits Management Release Notes V. 4.0Pharmacy Benefits Management Installation Guide V. 4.0Pharmacy Benefits Management User Manual V. 4.0(This page included for two-sided copying.)*

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within this documentation, several notations need to be outlined.

- Menu options will be italicized.

> Example: *Manual Pharmacy Statistics* indicates a menu option.

- Screen prompts will be denoted with quotation marks around them.

Example: “Select DRUG:” indicates a screen prompt.

- Responses in bold face indicate what the user is to type in.

> Example: Printing a MAR report by ward group G, by ward W or by patient P.

- Text centered between arrows represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed.

> Example: Press \<Tab\> to move the cursor to the next field.

> Press \<Enter\> to select the default.

- ![](benefits-management-version-4-technical-manual-security-guide/002.png)Note: Indicates especially important or helpful information.
- Some of the menu options have several letters that are capitalized. By entering in the letters and pressing \<Enter\>, the user can go directly to that menu option (the letters do not have to be entered as capital letters).

> Example: From the *Unit Dose Medications* option: the user can key INQ and proceed directly into the *INQuiries Menu* option.

- ?, ??, ??? One, two, or three question marks can be entered at any of the prompts for on-line help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions and three question marks will provide more detailed help, including a list of possible answers, if appropriate.
- ^ Caret (up arrow or a circumflex) and pressing \<Enter\> can be used to exit the current option.

*(This page included for two-sided copying.)*

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New PBM Health Level 7 (HL7) Chemistry Lab messaging to PBM functionality requires the use of HLO (HL7 Optimized), which requires port 5001 in live accounts and port 5026 in test accounts. If a site is unable to dedicate these ports, special arrangements must be made with the HLO team.

![](benefits-management-version-4-technical-manual-security-guide/003.png)Note: Considerable network traffic is generated by PBM HL7 messages.

## Implementation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the KIDS installation has completed, appropriate Pharmacy and Information Resource Management (IRM) personnel need to be added to the PSU PBM mail group. It is recommended that the Laboratory Information Manager (LIM) at each facility be added to the mail group to monitor data extracted from the Laboratory files.

![](benefits-management-version-4-technical-manual-security-guide/004.png)Note: It is recommended that the members of the PSU PBM mail group be limited due to the length and number of MailMan messages generated.

Schedule the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option to be executed on a monthly basis at a time when there will be the least amount of activity on the system. Please schedule the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option to run after the *Update AMIS Stats File* \[PSGW UPDATE AMIS STATS\] option has been executed.

For the remaining packages from which PBM extracts data, no statistical compilation options need to be executed before data extraction can be accomplished.

The DPPM.MED. <span class="mark">REDACTED</span> domain needs to exist at each facility for transmission.

![](benefits-management-version-4-technical-manual-security-guide/005.png)Note: Patch HL\*1.6\*126 is required for the PBM HL7 Chemistry Lab messaging functionality. For more information, see the patch description for project PSU\*4\*3

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no configurable site parameters involved in the implementation of this product.

*(This page included for two-sided copying.)*

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new PBM PATIENT DEMOGRAPHICS file (#59.9) was added to PBM V. 4.0 as a repository in which to temporarily store new or updated patient demographic data in real time until the data is compiled and transmitted on a monthly basis to the PBM national database. Only one demographics record per patient shall be retained in the file for a reporting period. The data is retained in this file for 75 days, after which time it is purged.

The PBM V. 4.0 software extracts data from the following files:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Extract</strong></th>
<th><strong>File Name/#</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IV</td>
<td><p>PATIENT (#2)</p>
<p>MEDICAL CENTER DIVISION (#40.8)</p>
<p>DRUG (#50)</p>
<p>VA PRODUCT (#50.68) <em>[Only if NDF V. 4.0 is installed.]</em></p>
<p>IV ADDITIVE (#52.6)</p>
<p>IV SOLUTIONS (#52.7)</p>
<p>PHARMACY PATIENT (#55)</p>
<p>PHARMACY PATIENT IV SUB-FILE (#55.01)</p>
<p>NEW PERSON (#200)</p></td>
</tr>
<tr class="even">
<td>UD</td>
<td><p>PATIENT (#2)</p>
<p>MEDICAL CENTER DIVISION (#40.8)</p>
<p>DRUG (#50)</p>
<p>VA PRODUCT (#50.68) <em>[Only if NDF V. 4.0 is installed.]</em></p>
<p>PHARMACY PATIENT (#55)</p>
<p>PHARMACY PATIENT UD SUBFILE (#55.06)</p>
<p>NEW PERSON (#200)</p></td>
</tr>
<tr class="odd">
<td>AR/WS Stats</td>
<td><p>MEDICAL CENTER DIVISION (#40.8)</p>
<p>DRUG (#50)</p>
<p>VA PRODUCT (#50.68)</p>
<p>AR/WS STATS (#58.5)</p>
<p>OUTPATIENT SITE (#59)</p></td>
</tr>
<tr class="even">
<td>Prescription</td>
<td><p>PATIENT (#2)</p>
<p>HOSPITAL LOCATION (#44)</p>
<p>DRUG (#50)</p>
<p>DRUG UNITS (#50.607)</p>
<p>VA PRODUCT (#50.68) <em>[Only if NDF V. 4.0 is installed.]</em></p>
<p>PRESCRIPTION (#52)</p>
<p>Rx PATIENT STATUS (#53)</p>
<p>OUTPATIENT SITE (#59)</p>
<p>NEW PERSON (#200)</p></td>
</tr>
<tr class="odd">
<td>Procurement</td>
<td><p>MEDICAL CENTER DIVISION (#40.8)</p>
<p>DRUG (#50)</p>
<p>ORDER UNIT (#51.5)</p>
<p>DRUG ACCOUNTABILITY ORDER (#58.811)</p>
<p>DRUG ACCOUNTABILITY TRANSACTION (#58.81)</p>
<p>OUTPATIENT SITE (#59)</p>
<p>PROCUREMENT &amp; ACCOUNTING TRANSACTIONS file (#442)</p></td>
</tr>
<tr class="even">
<td>Controlled Substances</td>
<td><p>PATIENT (#2)</p>
<p>MEDICAL CENTER DIVISION (#40.8)</p>
<p>DRUG (#50)</p>
<p>VA PRODUCT (#50.68)</p>
<p>DRUG ACCOUNTABILITY STATS (#58.8)</p>
<p>DRUG ACCOUNTABILITY TRANSACTION (#58.81)</p>
<p>OUTPATIENT SITE (#59)</p></td>
</tr>
<tr class="odd">
<td>Patient Demographics</td>
<td><p>PATIENT (#2)</p>
<p>INSTITUTION (#4)</p>
<p>PATIENT ENROLLMENT (#27.11)</p>
<p>PHARMACY PATIENT (#55)</p>
<p>NEW PERSON (#200)</p></td>
</tr>
<tr class="even">
<td>Outpatient Visits</td>
<td><p>PATIENT (#2)</p>
<p>INSTITUTION (#4)</p>
<p>ICD DIAGNOSIS (#80)</p>
<p>CPT file (#81)</p>
<p>VISIT (#9000010)</p>
<p>V POV (#9000010.07)</p>
<p>V CPT (#9000010.18)</p></td>
</tr>
<tr class="odd">
<td>Inpatient PTF Record</td>
<td><p>PATIENT (#2)</p>
<p>INSTITUTION (#4)</p>
<p>PTF (#45)</p>
<p>ICD DIAGNOSIS (#80)</p>
<p>ICD OPERATION/PROCEDURE (#80.1)</p></td>
</tr>
<tr class="even">
<td>Provider Data</td>
<td><p>PATIENT (#2)</p>
<p>PROVIDER CLASS (#7)</p>
<p>PRESCRIPTION (#52)</p>
<p>REFILL SUB-FILE (#52.1)</p>
<p>PARTIAL SUB-FILE (#52.2)</p>
<p>PHARMACY PATIENT IV ORDER SUB-FILE (#55.01)</p>
<p>PHARMACY PATIENT UD ORDER SUB-FILE (#55.06)</p>
<p>NEW PERSON (#200)</p>
<p>SERVICE/SECTION (#49)</p>
<p>PERSON CLASS (#8932.1)</p></td>
</tr>
<tr class="odd">
<td>Allergy/Adverse Event</td>
<td><p>PATIENT (#2)</p>
<p>INSTITUTION (#4)</p>
<p>SERVICE/SECTION (#49)</p>
<p>DRUG (#50)</p>
<p>DRUG INGREDIENTS (#50.416)</p>
<p>VA GENERIC (#50.6)</p>
<p>VA DRUG CLASS (#50.605)</p>
<p>PATIENT ALLERGIES (#120.8)</p>
<p>GMR ALLERGIES (#120.82)</p>
<p>ADVERSE REACTION REPORTING (#120.85)</p></td>
</tr>
<tr class="even">
<td>Vital/Immunization</td>
<td><p>PATIENT (#2)</p>
<p>INSTITUTION (#4)</p>
<p>GMRV VITAL MEASUREMENT (#120.5)</p>
<p>GMRV VITAL TYPE (#120.51)</p>
<p>GMRV VITAL QUALIFIER (#120.52)</p>
<p>V IMMUNIZATION (#9000010.11)</p>
<p>IMMUNIZATION (#9999999.14)</p></td>
</tr>
<tr class="odd">
<td>Laboratory</td>
<td><p>PATIENT (#2)</p>
<p>MEDICAL CENTER DIVISION (#40.8)</p>
<p>DRUG (#50)</p>
<p>PRESCRIPTION (#52)</p>
<p>PHARMACY PATIENT IV ORDER SUB-FILE (#55.01)</p>
<p>PHARMACY PATIENT UD ORDER SUB-FILE (#55.06)</p>
<p>OUTPATIENT SITE (#59)</p>
<p>LABORATORY TEST (#60)</p>
<p>LABORATORY TEST FILE SUB-FILE (#60.01)</p>
<p>LAB DATA (#63) (#63.04)</p></td>
</tr>
</tbody>
</table>

Data from the following files are pushed to PBM via event-driven HL7 messaging.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><strong>File Name/#</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Triggers</td>
<td>Data from these files are encapsulated in HL7 messages to PBM</td>
</tr>
<tr class="even">
<td>Verification of chemistry lab results.</td>
<td><p>PATIENT (#2)</p>
<p>LABORATORY TEST (#60)</p>
<p>LAB DATA (#63)</p>
<p>LAB LOINC (#95.3)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option</strong></th>
<th><strong>File Name/#</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>Map Pharmacy Locations</em> [PSU MAP PHARMACY LOCATIONS]</td>
<td><p>PHARMACY AOU STOCK (#58.1)</p>
<p>DRUG ACCOUNTABILITY STATS (#58.8)</p>
<p>MEDICAL CENTER DIVISION (#40.8)</p>
<p>OUTPATIENT SITE (#59)</p></td>
</tr>
<tr class="even">
<td><em>Automatic Pharmacy Statistics</em> [PSU PBM AUTO]</td>
<td><p>GENERIC INVENTORY (#445) <em>[PBM has current agreement.]</em></p>
<p>UNIT OF ISSUE (#420.5) <em>[PBM has current agreement.]</em></p>
<p>PROCUREMENT &amp; ACCOUNTING TRANSACTIONS file (#442)</p></td>
</tr>
<tr class="odd">
<td><em>Manual Pharmacy Statistics</em> [PSU PBM MANUAL]</td>
<td><p>GENERIC INVENTORY (#445) <em>[PBM has current agreement.]</em></p>
<p>UNIT OF ISSUE (#420.5) <em>[PBM has current agreement.]</em></p>
<p>PROCUREMENT &amp; ACCOUNTING TRANSACTIONS file (#442)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Reports</strong></th>
<th><strong>File Name/#</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Summary Reports</td>
<td>DRUG (#59)</td>
</tr>
<tr class="even">
<td>UD AMIS Summary Report</td>
<td><p>AMIS 334-341 (#42.6)</p>
<p>AMIS 345&amp;346 (#42.7)</p></td>
</tr>
<tr class="odd">
<td>AR/WS AMIS Summary Report</td>
<td>AR/WS STATS (#58.5)</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Mail Messages</strong></th>
<th><strong>File Name/#</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MailMan</td>
<td>MAILMAN SITE PARAMETERS (#4.3)</td>
</tr>
<tr class="even">
<td>HL7</td>
<td><p>PATIENT (#2)</p>
<p>LABORATORY TEST (#60)</p>
<p>LAB DATA (#63)</p>
<p>LAB LOINC (#95.3)</p></td>
</tr>
</tbody>
</table>

*(This page included for two-sided copying.)*

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of routines seen for PBM when the new routine set is loaded. The first line of each routine contains a brief description of the general function of the routine. Use the Kernel *First Line Routine Print* \[XU FIRST LINE PRINT\] option to print a list of just the first line of each routine.

| PSOORDER | PSUAA1   | PSUAA2  | PSUALERT | PSUAMC  | PSUAR0  | PSUAR1  | PSUAR2   |
|----------|----------|---------|----------|---------|---------|---------|----------|
| PSUAR3   | PSUAR4   | PSUAR5  | PSUAR6   | PSUAR7  | PSUCP   | PSUCP1  | PSUCP2   |
| PSUCP3   | PSUCS0   | PSUCS1  | PSUCS17  | PSUCS2  | PSUCS3  | PSUCS4  | PSUCS5   |
| PSUCSR0  | PSUCSR1  | PSUCSR2 | PSUDBQUE | PSUDEM0 | PSUDEM1 | PSUDEM2 | PSUDEM3  |
| PSUDEM4  | PSUDEM5  | PSUDEM6 | PSUDEM7  | PSUDEM8 | PSUDEM9 | PSUENV  | PSUHL    |
| PSULR0   | PSULR1   | PSULR2  | PSULR3   | PSULR4  | PSULR5  | PSULR6  | PSULRHL1 |
| PSULRHL2 | PSULRHL3 | PSUMAP0 | PSUMAPR  | PSUOP0  | PSUOP1  | PSUOP2  | PSUOP3   |
| PSUOP4   | PSUOP5   | PSUOP6  | PSUOP7   | PSUOP8  | PSUOPAM | PSUOPMD | PSUPR0   |
| PSUPR1   | PSUPR2   | PSUPR3  | PSUPR4   | PSUPR5  | PSUPR6  | PSURT1  | PSURT2   |
| PSURTQ   | PSUSUM1  | PSUSUM2 | PSUSUM3  | PSUSUM4 | PSUSUM5 | PSUSUM6 | PSUSUM7  |
| PSUTL    | PSUTL1   | PSUUD0  | PSUUD1   | PSUUD2  | PSUUD3  | PSUUD4  | PSUUD5   |
| PSUUD6   | PSUUD7   | PSUV0   | PSUV1    | PSUV10  | PSUV11  | PSUV12  | PSUV2    |
| PSUV3    | PSUV4    | PSUV5   | PSUV6    | PSUV7   | PSUV8   | PSUV9   | PSUVIT   |
| PSUVIT0  | PSUVIT1  | PSUVIT2 |          |         |         |         |          |

> 107 routines

![](benefits-management-version-4-technical-manual-security-guide/006.png) Note: Any PSU routine in the system that is not listed above for PBM 4.0 is no longer needed by the application and may be deleted.

> *(This page included for two-sided copying.)*

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Six options are exported with PBM version 4.0. These options are described in more detail in the *PBM User Manual V. 4.0*.

- *Automatic Pharmacy Statistics* \[PSU PBM AUTO\]
- *Manual Pharmacy Statistics* \[PSU PBM MANUAL\]
- *Pharmacy Background Job Check* \[PSU PBM JOB CHECK\]
- *Retransmit Patient Demographic Data* \[PSU RETRANSMIT PATIENT DATA\] – New option added in PBM V. 4.0
- *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] – New option added in PBM V. 4.0
- *PBM Manager Menu* \[PSU PBM MANAGER MENU\] – New option added in PBM V. 4.0

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following describes new options that are included in PBM V. 4.0.

*Retransmit Patient Demographic Data*\[PSU RETRANSMIT PATIENT DATA\]

The *Retransmit Patient Demographic Data* \[PSU RETRANSMIT PATIENT DATA\] option was created to retransmit patient demographic data stored in the new PBM file. When a user first enters the option, the software shall display the purpose of this option and the dates available for inclusion in the extract. Full months are available for monthly extract retransmissions, or a date range may be selected from the available dates. Modified patient data is available for the preceding 75 days.

*Map Pharmacy Locations*\[PSU MAP PHARMACY LOCATIONS\]

The *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] option was created to allow a user to map Area of Uses from the AR/WS Stats application, Narcotic Area of Uses from the CS application, and Pharmacy Locations from the Drug Accountability application to a specific Division or Outpatient Site.

*  
PBM Manager Menu*\[PSU PBM MANAGER MENU\]

This option was created to grant the user access to the following options:

- *Manual Pharmacy Statistics* \[PSU PBM MANUAL\]
- *Retransmit Patient Demographic Data* \[PSU RETRANSMIT PATIENT DATA\]
- *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\]

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data that is collected for the PBM extract is stored in the temporary globals (^XTMP and ^TMP). Data stored in the ^TMP global is deleted once the data is compiled and transmitted. The major portion of the data is stored in the ^XTMP global. A three (3)-day purge date is assigned. If a site does not regularly purge data in the ^XTMP global, the data will only be deleted the next time the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] or *ManualPharmacyStatistics* \[PSU PBM MANUAL\] options are run.

The PBM HL7 Lab messaging component stores PBM Chemistry Lab messages in the ^DIZ(9999 global on the CMOP-NAT server. A nightly job loads the PBM Chemistry Lab messages into a flat file and flags those messages as they are loaded, then purges the messages from the previous night’s job.

  
*(This page included for two-sided copying.)*

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PBM V. 4.0 relies (minimum) on the following external packages. This software is not included in this package and must be installed before this version of PBM is completely functional.

|                                                              |                            |
|--------------------------------------------------------------|----------------------------|
| Package                                                  | Minimum Version Needed |
| Adverse Reaction Tracking (ART)                              | 4.0                        |
| Auto Replenishment/Ward Stock (AR/WS)                        | 2.3                        |
| Controlled Substances (CS)                                   | 3.0                        |
| Drug Accountability                                          | 3.0                        |
| HLO (Health Level 7 Optimized)                               | 1.6                        |
| Inpatient Medications                                        | 5.0                        |
| Integrated Funds Control, Accounting and Procurement (IFCAP) | 5.1                        |
| Kernel                                                       | 8.0                        |
| Laboratory                                                   | 5.2                        |
| MailMan                                                      | 8.0                        |
| National Drug File (NDF)                                     | 4.0                        |
| Outpatient Pharmacy                                          | 7.0                        |
| Patient Care Encounter (PCE)                                 | 1.0                        |
| Patient Information Management System (PIMS)                 | 5.3                        |
| Pharmacy Data Management (PDM)                               | 1.0                        |
| VA FileMan                                                   | 22.0                       |
| Visit Tracking                                               | 2.0                        |

Verified Chemistry Lab results are pushed, rather than extracted, to PBM.

Verified Chemistry Lab results trigger the creation of an HL7 message containing data from the lab. These messages are sent to the CMOP-NAT sever, where a PBM process loads the data into flat files for export to an SQL database.

## Integration Agreements (IAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DBIA 3565 to subscribe to the LR7O ALL EVSEND RESULTS protocol

DBIA 998 to step through ^DPT(i,"LR" go get the IEN to file \#63

DBIA 91-A to step through ^LAB(60 to get the name of the test

DBIA 3630 to call the HL7 PID builder

DBIA 4727 to call EN^HLOCNRT

DBIA 3646 to call API: \$\$EMPL^DGSEC4

DBIA 4658 to call API: \$\$TSTRES^LRRPU

<span id="p19_18" class="anchor"></span>DBIA 5747 to call API: \$\$CSI^ICDEX()

PSU\*4\*3 has Integration Agreements (IAs) with the packages listed above. For complete information regarding the IAs, please refer to the *DBA MENU* \[DBA\] option on FORUM and then the *Integration AgreementsMenu* \[DBA IA ISC\] option.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Application Program Interfaces (APIs), callable routines, and entry points can be viewed by first choosing the DBA menu option on FORUM and then choosing the INTEGRATION CONTROL REGISTRATIONS (IAs) Menu option.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the options in this package can be invoked independently except for Laboratory, which is automatically run when the IV, UD, or Prescriptions extracts are run. The PBM HL7 messaging functionality is automatic and transparent to users. IRMs can monitor PBM messages using HLO monitoring utilities and by viewing the PSU SEND HL LOGICAL LINK.

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(Need Thom input)

PBM V. 4.0 contains several variables, such as PSUDIV, and all variables are stored in ^XTMP (PSUOPTS).

# Technical Assistance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If problems of a technical nature are encountered with this software package, please contact the <span class="mark">REDACTED</span>

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no security issues related to the Pharmacy Benefits Management software package.

*(This page included for two-sided copying.)*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Automatic Replenishment/ A method of drug distribution and inventory
> Ward Stock (AR/WS) management within a hospital. Drug products can be automatically inventoried and delivered to an Area of Use (AOU) or requested on demand.
> CMOP-NAT Consolidated Mail Outpatient Pharmacy’s national server. This server hosts PSUHL2 & PSUHL3, which are the PBM components to catch and process the PBM HL7 Chemistry Lab results sent from each site.
> Controlled Substance A drug that has been marked for tracking through the Controlled Substances package. It is usually narcotic.
> Dispensing Unit This field is used to indicate the pharmacy dispensing units when converting the unit per issue to the pharmacy dispensing units.
> Drug A substance used to treat illness or disease.
> HL7 Health Level Seven communication protocol.
> HLO HL7 Optimized (patch HL\*1.6\*126).
> Hyperalimentation (Hyperal) Long term feeding of a protein-carbohydrate solution. Electrolytes, fats, trace elements, and vitamins can be added. Since this solution generally provides all necessary nutrients, it is commonly referred to as Total Parenteral Nutrition (TPN). A hyperal is composed of many additives in two or more solutions. When the labels print, they show the individual electrolytes in the hyperal order.
> IFCAP Integrated Funds Distribution Control Point Activity, Accounting and Procurement. A VA software package that tracks procurement
> and payment.
> Invoice A bill for ordered goods. Each invoice is numbered. See entry for Order Number vs. Item Number.
> IV Additive A drug that is added to an IV solution for the purpose of parenteral administration. An additive can be an electrolyte, a vitamin, or other nutrient; or an antibiotic. Only electrolyte or multivitamin type additives can be entered as IV fluid additives in Computerized Patient Record System (CPRS).
> IV Solution Usually a Large Volume Parenteral (LVP), administered as a vehicle for additive(s) or for pharmacological effect of the solution itself. Infusion is generally continuous. An LVP or piggyback has only one solution (primary solution). A hyperal can have one or more solutions.
> MailMan An electronic mail, teleconferencing, and networking system.
> Order VA’s request for goods from the vendor.
> Order Number vs. An order number is a VA number by which
> Invoice Number to charge the ordered goods. The invoice number is the vendor’s number for billing the ordered goods. There can be many invoice numbers assigned to one order number because by law, certain drugs have to be placed on an invoice by itself. Also drugs can come from different distribution centers, which necessitates different invoice numbers.
> Outpatient Site An area within a facility that treats patients that are not admitted to the facility. If a facility has more than one Outpatient dispensing area, it is necessary to link each pharmacy location to the appropriate Outpatient site (area) for the collection of Outpatient dispensing data.
> PBM Pharmacy Benefits Management.
> Pharmacy Location An inventory location created to store a select group or all of non-controlled drugs and track their balance and activity.
> Prescription This term is now referred to throughout the software as medication orders.
> Prime Vendor A procurement system where each section orders pharmaceutical supplies directly from one primary vendor via computer link.
> Process Process is matching invoice data with data in VistA and validating the data. Matching is accomplished by comparing the line item data on the invoice with its entry in the DRUG file (#50). Validating is accomplished by confirming the quantity received vs. the quantity invoiced. Anyone holding the PSA ORDERS key can process the invoice.
> Provider The person who authorized an order. Only users identified as providers who are authorized to write medication orders may be selected.
> Reporting Period The period for the Start/Stop dates entered by the user for the PBM extract.
> Syringe Type of IV that uses a syringe rather than a bottle or bag. The method of infusion for a syringe-type IV may be continuous or intermittent.
> Unit A standard form of measure.
> Unit of Issue The packaging unit used at the inventory point to distribute the item.
> VistA Veterans Health Information Systems and Technology Architecture.
*(This page included for two-sided copying.)*
