---
title: QUASAR Version 3 Technical Manual (Updated ACKQ*3*21)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: (Updated ACKQ*3*21)
app_code: ACKQ
app_name: Quality Audiology and Speech Analysis and Reporting (QUASAR)
section: CLI
app_status: active
pkg_ns: ACKQ
patch_ver: 3
patch_id: ACKQ*3
group_key: "ACKQ:ACKQ:3"
file_numbers: 
  - 2
  - 200
  - 8930
security_keys: []
menu_options: 1
description: "Quality: Audiology and Speech Analysis and Reporting (QUASAR) is a VISTA software package written for the Audiology and Speech Pathology Service. QUASAR is used to enter, edit, and retrieve data for each episode of care. It provides transmission of visit data to the Patient Care Encounter (PCE) prog"
audience: 
keywords: 
  - table
  - contents
  - class
  - quasar
  - strong
  - package
  - style
  - width
  - ackq
  - intentionally
page_count: 0
word_count: 2093
section_count: 3
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2000
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=97"
---

---
title: |
  <span id="_Toc390185170" class="anchor"></span>Quality Audiology and Speech Analysis and Reporting (QUASAR)

  <span id="_Toc390185171" class="anchor"></span>Technical Manual
---

![](quasar-version-3-technical-manual-updated-ackq-3-21/001.png)

February 2000

Office of Information and Technology (OIT)

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Implementation](#implementation)
    - [Implementation Checklist (Virgin Installations Only)](#implementation-checklist-virgin-installations-only)
    - [Implementation Checklist (Installations over V. 2.0)](#implementation-checklist-installations-over-v-20)
    - [Menu Option Assignment](#menu-option-assignment)
    - [Key Assignment](#key-assignment)
  - [Maintenance](#maintenance)
    - [File Maintenance](#file-maintenance)
    - [Resource Requirements](#resource-requirements)
- [Files](#files)
- [Routines](#routines)
- [# # This page intentionally left blank for double-sided printing.](#this-page-intentionally-left-blank-for-double-sided-printing)
- [Exported Options](#exported-options)
- [Archiving and Purging](#archiving-and-purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
- [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [# This page intentionally left blank for double-sided printing.](#this-page-intentionally-left-blank-for-double-sided-printing-1)
- [Package Security](#package-security)
- [# # This page intentionally left blank for double-sided printing.](#this-page-intentionally-left-blank-for-double-sided-printing-2)
- [Glossary](#glossary)
<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 49%" />
<col style="width: 8%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Page</strong></th>
<th><strong>Author/Manager</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>August 2014</td>
<td><p>ACKQ*3*21</p>
<ul>
<li><p>Added Note about CDR and Audiometric obsolescence.</p></li>
<li><p>Updated File Security.</p></li>
<li><p>Changed “ICD-9 CM” references to “ICD CM”.</p></li>
<li><p>Added clickable links to Table of Contents.</p></li>
</ul></td>
<td><p>iii,</p>
<p><a href="#ICDnote">7-8</a>,</p>
<p><a href="#p21_18">18</a></p>
<p><a href="#ICDp21">21</a></p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>November 2010</td>
<td><p>ACKQ*3*17</p>
<ul>
<li><p>Changes to Staff (Enter/Edit) [ACKQAS CLINICIAN ENTRY] option to synchronize the A&amp;SP STAFF (#509850.3) file names with the NEW PERSON (#200) file names.</p></li>
</ul></td>
<td>7</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>February 2000</td>
<td>QUASAR 3.0: original version</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
*This page intentionally left blank for double-sided printing.*
Table of Contents
*This page intentionally left blank for double-sided printing.*
Quality: Audiology and Speech Analysis and Reporting  
(QUASAR) V 3.0

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Quality: Audiology and Speech Analysis and Reporting (QUASAR) is a VISTA software package written for the Audiology and Speech Pathology Service. QUASAR is used to enter, edit, and retrieve data for each episode of care. It provides transmission of visit data to the Patient Care Encounter (PCE) program in order to incorporate QUASAR Visit Data in ACRP Workload Reporting. It produces a variety of reports useful to local managers, medical center management, and central planners. QUASAR also contains a VA FileMan function that permits users to generate customized reports using data from QUASAR's A&SP Clinic Visit file (#509850.6) or A&SP Patient file (#509850.2). QUASAR produces an automated Cost Distribution RCS 10-0141 Report (CDR) and has an option for generating and processing audiology compensation and pension examinations through an agreement with the Automated Medical Information Exchange (AMIE) package.

*This page intentionally left blank for double-sided printing.*

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Implementation Checklist (Virgin Installations Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign menu options to users.

> Make sure all A&SP clinics are in the VISTA Hospital Location file (# 44) and that each is associated with a Division.

> Assign the ACKQ ADHOC key to those users who will be designing reports using the Tailor-Made A&SP Reports option.

> Add appropriate A&SP staff to the USR Class Membership file \# 8930.3 and assign a User Class to each. After staff is added to the USR Class Membership file, add the same A&SP staff to the A&SP Staff file \#509850.3. Also ensure that each A&SP staff member has an appropriate Person Class entry within the New Person file \#200.

> Define site parameters using the A&SP Site Parameters option.

> (Optional) Use the Update Files per CO Directive to add diagnoses to the A&SP Diagnostic Condition file and procedures to the A&SP Procedure Code file.

> (Optional) Apply local cost amounts to each procedure using the Enter Cost Information Procedure option. You may use locally developed cost data, DSS product costs, community fees, insurance reasonable rates, or Medicare reasonable rates.

### Implementation Checklist (Installations over V. 2.0)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Define site parameters using the A&SP Site Parameters option.

> Make sure each entry in the A&SP Staff file \#509850.3 also has an appropriate Person Class entry within the New Person file \#200.

> (Optional) Use the Update Files per CO Directive to make any required changes to the A&SP Diagnostic Condition file and the A&SP Procedure Code file.

> (Optional) Apply local cost amounts to each procedure using the Enter Cost Information Procedure option.

### Menu Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### A&SP Supervisor Menu

> The A&SP Supervisor Menu \[ACKQAS SUPER\] option is assigned to supervisory personnel. It is the main menu and contains options for setting up and maintaining the QUASAR package, entering clinic visit data, generating management reports, and adequating Compensation and Pension (C&P) exams.

#### Audiology & Speech Visit Tracking System

> The Audiology & Speech Visit Tracking System \[ACKQAS MASTER\] menu option is assigned to personnel who will be entering clinic visit data and generating reports.

#### A&SP Reports

> The A&SP Reports \[ACKQAS REPORTS\] menu contains only report options. This menu can be assigned to users who may not enter or modify any of the data, but need to be able to see the data generated by these reports.

### Key Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Give the ACKQ ADHOC key to all users who will be creating/designing reports using the option Tailor-Made A&SP Reports. This option uses VA FileMan to sort and print data from the A&SP Clinic Visit (#509850.6) and A&SP Patient (#509850.2) files.

## Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### File Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Maintenance of the files is through the Set Up/Maintenance menu. For use of this menu, please refer to the QUASAR user manual.

### Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The total size of the ACKQ\* routines is approximately 360 K bytes. The package namespace is ACKQ.

> The CDR ACCOUNT (#509850), A&SP DIAGNOSTIC CONDITION (#509850.1), and A&SP PROCEDURE CODE (#509850.4) files are static, and require approximately 17, 5, and 9 K bytes respectively. The A&SP STAFF file (#509850.3) is reasonably static and requires about 1 K. The A&SP PROCEDURE MODIFIER file (#509850.5) is reasonably static and requires about 1 K. There are three dynamic files. A&SP PATIENT file (#509850.2) requires approximately .5 K per Audiology and Speech Pathology clinic patient. The A&SP CLINIC VISIT file (#509850.6) requires approximately .75 K per clinic visit. Using clinic workload data from the Chief, Audiology & Speech Pathology Service, some idea of file size and rate of growth can be calculated.

*This page intentionally left blank for double-sided printing.*

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 28%" />
<col style="width: 44%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p id="file" class="heading"><u>File #</u></p></td>
<td><p id="name" class="heading">Name</p></td>
<td><p id="contents" class="heading">Contents</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>509850</td>
<td>CDR Account</td>
<td><p>Contains all of the cost accounts used to calculate and print the Cost Distribution Report for Audiology and Speech Pathology. Each patient visit contains a pointer to one of these accounts for distribution of workload to appropriate cost accounts.</p>
<p><span id="ICDnote" class="anchor"></span>NOTE: CDR and audiometric fields in QUASAR are obsolete. CDR is no longer used and the audiometric functionality was replaced by GUI QUASAR (audiometric module).</p></td>
</tr>
<tr class="even">
<td>509850.1</td>
<td>A&amp;SP Diagnostic Condition</td>
<td>Contains pointers to a small subset of ICD CM codes which pertain to Audiology and Speech Pathology. Entries in this file are pointed to by the Diagnostic Code field in the A&amp;SP Clinic Visit file.</td>
</tr>
<tr class="odd">
<td>509850.2</td>
<td>A&amp;SP Patient</td>
<td>Contains identifying, demographic, and other clinical information for all patients seen in the Audiology and Speech Pathology clinics. The entries in this file are pointers to the Patient file #2.</td>
</tr>
<tr class="even">
<td>509850.3</td>
<td>A&amp;SP Staff</td>
<td>Entries in this file point to the New Person file #200. Staff members must be present in the USR Class Membership file # 8930.3 before they can be added to the A&amp;SP Staff file.  Staff members must also have an appropriate Person Class entry within the New Person file #200 otherwise their STATUS in the A&amp;SP Staff file (#509850.3) will default to STUDENT.</td>
</tr>
<tr class="odd">
<td>509850.4</td>
<td>A&amp;SP Procedure Code</td>
<td>Contains pointers to a small subset of CPT-4 codes which pertain to Audiology and Speech Pathology. Entries in this file are pointed to by the Procedure Code field in the A&amp;SP Clinic Visit file. Before using the QUASAR package, the supervisor should enter cost data for each procedure code in the A&amp;SP Procedure Code file if the site wants to take advantage of the procedure cost functionality.</td>
</tr>
<tr class="even">
<td>509850.5</td>
<td>A&amp;SP Procedure Modifier</td>
<td>Contains a list of the CPT and HCPCS modifiers that are appropriate to Audiology and Speech Pathology. This file restricts the selection of Modifiers when entering CPT procedures with the New Clinic Visits and Edit an Existing Visit options.</td>
</tr>
<tr class="odd">
<td>509850.6</td>
<td>A&amp;SP Clinic Visit</td>
<td>Contains all data specific to each patient encounter. This includes the patient, the providers and students involved, the diagnostic and procedure codes, the date and time of the visit, and the CDR cost account.</td>
</tr>
<tr class="even">
<td>509850.7</td>
<td>A&amp;SP Workload</td>
<td>Contains each month's capitation statistics. Data in this file are used to compile statistics which includes a display of total and unique visits by zip code, procedure, and disease codes for any specified month.</td>
</tr>
<tr class="odd">
<td>509850.8</td>
<td>A&amp;SP Site Parameters</td>
<td>Contains site specific data used by the QUASAR package. There should be only one site entry in this file and at least one division defined.</td>
</tr>
</tbody>
</table>

Data in all QUASAR files should not be altered through the use of VA FileMan; input should take place only through the QUASAR menu options.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

QUASAR routines are namespaced ACKQ. To obtain a list of the routines use the First Line Routine Print option to obtain a list of the routines exported with the package.

Select Routine Tools Option: First Line Routine Print

PRINTS FIRST LINES

routine(s) ? \> ACKQ\*

searching directory ...

routine(s) ? \> \<RET\>

(A)lpha, (D)ate ,(P)atched, OR (S)ize ORDER: A// \<RET\>

Include line 2? NO// \<RET\>

DEVICE: HOME// (Enter a device)

# # # *This page intentionally left blank for double-sided printing.*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

QUASAR options are namespaced ACKQ.

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At present, the QUASAR package does not provide for the archiving or purging of its data.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The QUASAR routines have not been designed to be called outside of the package.

*This page intentionally left blank for double-sided printing.*

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package was created using Kernel V. 8.0 and VA FileMan V. 21. The QUASAR V. 3.0 package requires the following external packages and files:

> <u>Name</u> <u>Minimum Version Needed</u>

> Kernel 8.0

> VA FileMan 21.0

> MailMan 7.1

> PIMS 5.3

> Automated Med Info Exchange 2.7

> PCE Patient Care Encounter 1.0

> QUASAR also uses the following files:

> New Person file \#200

> ICD Diagnosis file \#80

> CPT Procedure file \#81

> CPT Modifier file \#81.3

> USR Class Membership file \#8930.3

> DSS Unit file \#724

######## Integration Agreements

Integration agreements for QUASAR are listed on the Data Base Administrator (DBA) menu on FORUM. Use the Integration Agreements Menu option to obtain up-to-date information.

Active QUASAR Subscribing Agreements

> Select Integration Agreements Menu Option: SUBscriber Package Menu

> 1 Print ACTIVE by Subscribing Package

> 2 Print ALL by Subscribing Package

> Select Subscriber Package Menu Option: 1 Print ACTIVE by Subscribing Package

> START WITH SUBSCRIBING PACKAGE: FIRST// QUASAR

> GO TO SUBSCRIBING PACKAGE: LAST// QUASAR

> DEVICE: (Enter a device)

> Active QUASAR Custodial Agreements

> Select Integration Agreements Menu Option: 8 Custodial Package Menu

> 1 ACTIVE by Custodial Package

> 2 Print ALL by Custodial Package

> 3 Supported References Print All

> Select Custodial Package Menu Option: 1 ACTIVE by Custodial Package

> Select PACKAGE NAME: QUASAR ACKQ

> DEVICE: HOME// (Enter a device)

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the QUASAR package options can function independently. All menus can stand alone.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no QUASAR package-wide variables.

# # *This page intentionally left blank for double-sided printing.*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Package Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1. Security Management.

> Data in all QUASAR files should not be altered through the use of VA FileMan; input should take place only through the QUASAR menu options. Per VHA Directive 10-93-142, all QUASAR file definitions should not be modified.

> The QUASAR package uses the Current Procedural Terminology (CPT) coding system which is an American Medical Association (AMA) copyrighted product. Its use is governed by the terms of the agreement between the Department of Veterans Affairs and the AMA.

> No additional licenses are necessary to run the software.

> Confidentiality of staff and patient data and the monitoring of this confidentiality is no different than with any other paper reference.

2. Security Features:

> a\. Mail Groups and Alerts.

> There are no mail groups or alerts for the users of this package.

> b\. Remote Systems.

> The application does not transmit data to any remote system/facility database.

> c\. Archiving/Purging.

> Refer to <u>Archiving and Purging</u>, in this manual.

> d\. Contingency Planning.

> It is the responsibility of the using service to develop a local contingency plan to be used in the event of application problems.

> e\. Interfacing.

> No specialized (non VA) interfaces are used or required by the application.

> f\. Electronic Signatures.

> QUASAR has an option for generating and processing audiology compensation and pension examinations through an agreement with the Automated Medical Information Exchange (AMIE) package. If this functionality is used at your facility, A&SP staff involved must enter an electronic signature. An electronic signature can be established using the *Edit Electronic Signature Code* option in the *User’s Toolbox* menu.

> g\. Menus.

There are no options of special note for the Information Security Officers (ISO's) to view.

> h\. Security Keys.

> There is one locked option on the QUASAR menu. The *Tailor-Made A&SP Reports* option is locked with the ACKQ ADHOC security key. Allocation of this key is at the discretion of the IRM chief.

> i\. File Security

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p id="number" class="heading"><u>Number</u></p></td>
<td><strong><u>Name</u></strong></td>
<td><strong><u>Global Name</u></strong></td>
<td><strong><u>DD</u></strong></td>
<td><strong><u>RD</u></strong></td>
<td><strong><u>WR</u></strong></td>
<td><strong><u>DEL</u></strong></td>
<td><strong><u>LAY</u></strong></td>
<td><strong><u>AUDIT</u></strong></td>
</tr>
<tr class="even">
<td></td>
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
<td>509850</td>
<td>CDR Account</td>
<td>^ACKQ(509850,</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>509850.1</td>
<td>A&amp;SP Diagnostic Condition</td>
<td>^ACKQ(<span id="p21_18" class="anchor"></span>509850.1,</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>509850.2</td>
<td>A&amp;SP Patient</td>
<td>^ACKQ(509850.2,</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>509850.3</td>
<td>A&amp;SP Staff</td>
<td>^ACKQ(509850.3,</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>509850.4</td>
<td>A&amp;SP Procedure Code</td>
<td>^ACKQ(509850.4,</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>509850.5</td>
<td>A&amp;SP Procedure Modifier</td>
<td>^ACKQ(509850.5,</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>509850.6</td>
<td>A&amp;SP Clinic Visit</td>
<td>^ACKQ(509850.6,</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>509850.7</td>
<td>A&amp;SP Workload</td>
<td>^ACKQ(509850.7,</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>509850.8</td>
<td>A&amp;SP Site Parameters</td>
<td>^ACKQ(509850.8,</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

> j\. References.

There are no special reference materials for this package.

> k\. Official Policies.

> Per VHA Directive 10-93-142 regarding security of software that reports data to an external data base, the QUASAR routines may not be modified.

> According to the same directive, the QUASAR Data Dictionaries may not be modified. The file descriptions of these files are so noted. QUASAR files may only be updated through distributed options.

# # # *This page intentionally left blank for double-sided printing.*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                |                                                                           |
|------------------------------------------------|---------------------------------------------------------------------------|
| A&SP                                           | Audiology and Speech Pathology.                                           |
| CDR                                            | Cost Distribution Report.                                                 |
| C&P                                            | Compensation and Pension.                                                 |
| CPT Codes                                      | Codes listed in the *Physicians Current Procedural Terminology Handbook.* |
| DSS                                            | Decision Support System.                                                  |
| HCFA                                           | Health Care Financing Administration.                                     |
| HCPCS                                          | HCFA Common Procedure Coding System.                                      |
| <span id="ICDp21" class="anchor"></span>ICD CM | International Classification of Diseases with Clinical Modifications.     |
| PCE                                            | Patient Care Encounter.                                                   |
| QUASAR                                         | Quality: Audiology and Speech Analysis and Reporting.                     |
| VACO                                           | Veterans Affairs Central Office.                                          |
| VARO                                           | Veterans Affairs Regional Office.                                         |
| VHA                                            | Veterans Health Administration.                                           |
| VISTA                                          | Veterans Health Information System and Technology Architecture.           |
*This page intentionally left blank for double-sided printing.*
