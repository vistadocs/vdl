---
title: PXRM*2*32 Mental Health Clinical Reminder Dialog Templates Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Mental Health Clinical Reminder Dialog Templates
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*32
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document describes the installation and setup for the national release of Mental Health Clinical Reminder (MHCR) Dialog Templates, Patch PXRM\2.0\32. Clinicians will use these templates to document mental health treatment using specified Evidence Based Psychotherapy (EBP) protocols, as reques
audience: 
keywords: 
  - table
  - contents
  - blockquote
  - templates
  - installation
  - template
  - strong
  - cprs
  - class
  - pxrm
page_count: 0
word_count: 1890
section_count: 15
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_32_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_32_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> Department of Veterans Affairs

# Office of Information & Technology (OIT) Product Development 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Office of Information & Technology (OIT) Product Development](#office-of-information-technology-oit-product-development)
  - [Patch PXRM\2.0\32](#patch-pxrm2032)
    - [November 2014](#november-2014)
- [Introduction](#introduction)
  - [Target audience](#target-audience)
  - [MHCR dialog titles for Patch PXRM\2.0\32](#mhcr-dialog-titles-for-patch-pxrm2032)
  - [Project references](#project-references)
  - [Acronyms and definitions](#acronyms-and-definitions)
  - [Section 508 compliance](#section-508-compliance)
- [Pre-Installation](#pre-installation)
  - [Installation system notes and requirements](#installation-system-notes-and-requirements)
  - [Software retrieval](#software-retrieval)
  - [Security management](#security-management)
  - [Backup routines](#backup-routines)
  - [Backout plan (optional)](#backout-plan-optional)
    - [To remove the Reminder Exchange Entries from VistA](#to-remove-the-reminder-exchange-entries-from-vista)
    - [To delete the templates from VistA](#to-delete-the-templates-from-vista)
- [Installing KIDS](#installing-kids)
  - [Installation](#installation)
  - [KIDS Utilities Options (Optional)](#kids-utilities-options-optional)
  - [CPRS Template Installation](#cprs-template-installation)
    - [Setting the User Class](#setting-the-user-class)
    - [Preparing the templates](#preparing-the-templates)
    - [Adding the templates to the CPRS template drawer](#adding-the-templates-to-the-cprs-template-drawer)
    - [Verifying that the templates are properly installed](#verifying-that-the-templates-are-properly-installed)
- [Appendix - Example of an installation](#appendix-example-of-an-installation)
> Mental Health Clinical Reminder Dialog Templates
![](pxrm-2-32-mental-health-clinical-reminder-dialog-templates-installation-guide/001.png)
> Installation Guide

## Patch PXRM\*2.0\*32

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### November 2014

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 1.3

> Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 42%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>August 2014</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>Backup instructions added</p>
</blockquote></td>
<td>Information Innovators Inc.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>August 2013</p>
</blockquote></td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>Increment 3 – Patch PXRM*2.0*32</p>
</blockquote></td>
<td>Information Innovators Inc.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>January 2013</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Increments 1 &amp; 2 – Patch PXRM*2.0*29</p>
</blockquote></td>
<td>Information Innovators Inc.</td>
</tr>
</tbody>
</table>

> Contents

1.  [Introduction 1](#introduction)
    1.  [Target audience 1](#target-audience)
    2.  [MHCR dialog titles for Patch PXRM\*2.0\*32 1](#mhcr-dialog-titles-for-patch-pxrm2.032)
    3.  [Project references 3](#project-references)
    4.  [Acronyms and definitions 3](#acronyms-and-definitions)
    5.  [Section 508 compliance 4](#section-508-compliance)
2.  [Pre-Installation 4](#pre-installation)
    1.  [Installation system notes and requirements 4](#installation-system-notes-and-requirements)
    2.  [Software retrieval 4](#software-retrieval)
    3.  [Security management 5](#security-management)
    4.  [Backup routines 5](#backup-routines)
    5.  [Backout plan (optional) 6](#backout-plan-optional)
        1.  [To remove the Reminder Exchange Entries from VistA 6](#to-remove-the-reminder-exchange-entries-from-vista)
        2.  [To delete the templates from VistA 6](#to-delete-the-templates-from-vista)
3.  [Installing KIDS 6](#installing-kids)
    1.  [Installation 7](#installation)
    2.  [KIDS Utilities Options (Optional) 7](#kids-utilities-options-optional)
    3.  [CPRS Template Installation 9](#cprs-template-installation)
        1.  [Setting the User Class 10](#setting-the-user-class)
        2.  [Preparing the templates 10](#preparing-the-templates)
        3.  [Adding the templates to the CPRS template drawer 13](#adding-the-templates-to-the-cprs-template-drawer)
        4.  [Verifying that the templates are properly installed 16](#verifying-that-the-templates-are-properly-installed)

[Appendix - Example of an installation 18](#appendix---example-of-an-installation)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes the installation and setup for the national release of Mental Health Clinical Reminder (MHCR) Dialog Templates, Patch PXRM\*2.0\*32. Clinicians will use these templates to document mental health treatment using specified Evidence Based Psychotherapy (EBP) protocols, as requested by Mental Health Services (MHS).

> Patch PXRM\*2.0\*32 contains reminder dialog templates in support of five EBP protocols. The templates will be accessed by mental health clinicians documenting therapy sessions through the CPRS Shared Template Drawer. There is no reminder definition, so no reminder logic is being used.

## Target audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The intended user is familiar with the VistA computing environment (Kernel Installation and Distribution System \[KIDS\]).

## MHCR dialog titles for Patch PXRM\*2.0\*32

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On the next page, a table lists the MHCR dialog titles for Patch PXRM\*2.0\*32 and the associated mandated template names for the configuration of these templates in the Shared Template drawer.. This step is required to facilitate clinician recognition of the correct templates, and this naming convention will be used in national provider training. The national EBP training programs have created clinician training materials based on the this naming convention, therefore the names, the order of those names, and the names of their enclosing folders should be followed – see note on page 14 (section 3.3.3).

| Reminder Dialog Title                           | Mandated Template Drawer Name |
|-----------------------------------------------------|-----------------------------------|
| IPT - Interpersonal Psychotherapy for Depression    |                                   |
| VA-MH IPT 1 DEPRESSION                              | IPT 1 Depression Initial          |
| VA-MH IPT 2 DEPRESSION                              | IPT 2 Depression Intermediate     |
| VA-MH IPT 3 DEPRESSION                              | IPT 3 Depression Termination      |
| VA-MH IPT 4 DEPRESSION MAINT                        | IPT 4 Depression Maintenance      |
| VA-MH IPT EARLY TERMINATION                         | IPT Early Termination             |
| CBT-I - Cognitive Behavioral Therapy for Insomnia\* |                                   |
| VA-MH CBT-I 1 EVALUATION SESSION                    | CBT-I: 1 Evaluation Session       |
| VA-MH CBT-I 2 INITIAL TREATMENT PHASE               | CBT-I: 2 Initial Treatment Phase  |
| VA-MH CBT-I 3 MIDDLE TREATMENT PHASE                | CBT-I: 3 Middle Treatment Phase   |
| VA-MH CBT-I 4 FINAL SESSION                         | CBT-I: 4 Final Session            |
| VA-MH CBT-I EARLY TERMINATION                       | CBT-I: Early Termination          |
| BFT - Behavioral Family Therapy                     |                                   |
| VA-MH BFT 1 ORIENTATION                             | BFT 1 Orientation Session         |
| VA-MH BFT 2 EDUCATION SESSION                       | BFT 2 Education Session           |
| VA-MH BFT 3 COMMUNICATION SESSION                   | BFT 3 Communication Session       |
| VA-MH BFT 4 PROBLEM-SOLVING SESSION                 | BFT 4 Problem-Solving Session     |
| VA-MH BFT 5 FINAL SESSION                           | BFT 5 Final Session               |
| VA-MH BFT 6 EARLY TERMINATION                       | BFT Early Termination             |
| SST - Social Skills Training                        |                                   |
| VA-MH SST 1 INITIAL                                 | SST 1 Initial                     |
| VA-MH SST 2 GROUP VISIT                             | SST 2 Group Visit                 |
| VA-MH SST 3 FINAL VISIT                             | SST 3 Final Visit                 |
| VA-MH SST EARLY TERMINATION                         | SST Early Termination             |
| IBCT - Integrative Behavioral Couple Therapy        |                                   |
| VA-MH IBCT 1 INITIAL                                | IBCT 1 Initial                    |
| VA-MH IBCT 2 INDIVIDUAL                             | IBCT 2 Individual                 |
| VA-MH IBCT 3 NON VETERAN                            | IBCT 3 Non Veteran                |
| VA-MH IBCT 4 FEEDBACK                               | IBCT 4 Feedback                   |
| VA-MH IBCT 5 THERAPY                                | IBCT 5 Therapy                    |
| VA-MH IBCT 6 TERMINATION                            | IBCT 6 Termination                |
| VA-MH IBCT EARLY TERMINATION                        | IBCT Early Termination            |

> \*NOTE: The semicolon is needed on the CBT-I template names so that the I is not confused with a 1 (e.g. CBT-I: 1 Evaluation Session vs. CBT-I 1 Evaluation Session)

## Project references

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Manuals &amp; Guides</strong></th>
<th><strong>Documentation File name/ Web address</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Clinical Reminders User Manual</p>
</blockquote></td>
<td>PXRM_2_20_UM.PDF</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Clinical Reminders Manager’s Manual</p>
</blockquote></td>
<td>PXRM_2_MM.PDF</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPRS Technical Manual</p>
</blockquote></td>
<td><a href="http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprslmtm.pdf">http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprslmtm.pdf</a></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPRS User Guide: GUI Version</p>
</blockquote></td>
<td><a href="http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprsguium.pdf">http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprsguium.pdf</a></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Health Summary Technical Manual</p>
</blockquote></td>
<td><a href="http://www.va.gov/vdl/documents/Clinical/CPRS-Health_Summary/hsum2_7_tm.pdf">http://www.va.gov/vdl/documents/Clinical/CPRS-Health_Summary/hsum2_7_tm.pdf</a></td>
</tr>
<tr class="even">
<td><p><strong>V</strong><em>ist</em><strong>A</strong> MHA 3 Installation Guide</p>
<p>PATCH YS*5.01*105</p></td>
<td><a href="http://www.va.gov/vdl/application.asp?appid=78">http://www.va.gov/vdl/application.asp?appid=78</a></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 31%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Web Sites</strong></p>
</blockquote></th>
<th><strong>URL</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>National Clinical Reminders site</p>
</blockquote></td>
<td><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></td>
<td>Contains manuals, PowerPoint presentations, and other information about Clinical Reminders.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>National Clinical Reminders Committee</p>
</blockquote></td>
<td><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/ncrc</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>public/default.aspx</u></a></td>
<td>This committee directs the development of new and revised national reminders.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistA Documentation Library</p>
</blockquote></td>
<td><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></td>
<td>Contains manuals for Clinical Reminders and CPRS.</td>
</tr>
</tbody>
</table>

## Acronyms and definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronyms | Definition                                                      |
|----------|-----------------------------------------------------------------|
| ASU      | Authorization/Subscription Utility                              |
| CAC      | Clinical Application Coordinator                                |
| Clin4    | National Customer Support team that supports Clinical Reminders |
| CPRS     | Computerized Patient Record System                              |
| GMTS     | Health Summary namespace (also HSUM)                            |
| GUI      | Graphic User Interface                                          |
| ICD-9    | International Classification of Diseases, 9th Edition           |
| MHCR     | Mental Health Clinical Reminder                                 |

| MHS      | Mental Health Services (previously OMHS)   |
|----------|--------------------------------------------|
| MHTC     | Mental Health Treatment Coordinator        |
| OHI      | Office of Health Information               |
| OI       | Office of Information                      |
| OIT/OI&T | Office of Information Technology           |
| OMHS     | Office of Mental Health Services (now MHS) |
| PTM      | Patch Tracker Message                      |
| PXRM     | Clinical Reminder Package Namespace        |

## Section 508 compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Veterans Health Administration (VHA) fully supports Section 508 of *The Rehabilitation Act* and is committed to equal access for all users. The MHCR dialog templates project was evaluated according to parameters. Because the templates are a minor addition to VistA CPRS and use VistA tools, Section 508 compliance was determined to be N/A.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation system notes and requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VistA Operating System

> Mental Health Clinical Reminders Dialog Templates – PXRM\*2.0\*32 patch, as well as CPRS, and MHA currently run on the standard hardware platforms used by the Department of Veterans Affairs Health Care System facilities. These systems consist of standard or upgraded Alpha AXP clusters, and run either Cache-VMS or Cache-NT and the Open M product.

#### MHCR Software Application Installation Time

> MHCR Patch PXRM\*2.0\*32 installation time takes approximately 10-15 minutes during off peak hours.

#### Users on the System

> Users may remain on the system. However, the installation should be done during off- peak hours.

#### Kernel Installation and Distribution System (KIDS)

> PXRM\*2.0\*32 is created using the Kernel Installation and Distribution System (KIDS). For further instructions on using KIDS, please refer to the Kernel V.8.0 Systems Manual.

#### Namespace

> Mental Health Clinical Reminder Patch PXRM\*2.0\*32 namespace is PXRM.

## Software retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Your site will receive the Mental Health Clinical Reminders Dialog Template files as part of patch PXRM\*2.0\*32 via a host file. The preferred method is to FTP the files from:

> download.vista.med.va.gov

> This location automatically transmits files from the first available FTP Server to the appropriate directory on your system. (See the order listed below under the FTP Address column). If you prefer, you can retrieve the software *directly* from one of the FTP Servers listed below, under the FTP Address column.

| OI Field Office | FTP Address                           | Directory                             |
|---------------------|-------------------------------------------|-------------------------------------------|
| Albany (NY)         | <span class="mark"><u>REDACTED</u></span> | <span class="mark"><u>REDACTED</u></span> |
| Hines (IL)          | <span class="mark"><u>REDACTED</u></span> | <span class="mark"><u>REDACTED</u></span> |
| Salt Lake City (UT) | <span class="mark"><u>REDACTED</u></span> | <span class="mark"><u>REDACTED</u></span> |

## Security management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no unique legal requirements pertaining

## Backup routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No routines are being installed by this content-only patch; however, we recommend performing a backup of the transport global before installing the VistA MHCR Dialog Templates Patch PXRM\*2.0\*32.

> The option called Backup a Transport Global \[XPD BACKUP\] creates a MailMan message that backs up all current routines on your system that would be replaced by a KIDS patch. This option is under the Installation menu of the KIDS menu. It works on a patch that has been loaded on your system, but not installed.

> Example

## Backout plan (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### To remove the Reminder Exchange Entries from VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the Reminder Exchange Menu Option.
2.  Select the Exchange File entries that were installed by this patch. Example: CPT 1 Initial

> Warning: There is no confirmation question prior to the delete function in step 3.

3.  Select the number that matches the entry you want to remove; this will select the option: DFE Delete Exchange File Entry.

> The Exchange File Entry is deleted.

### To delete the templates from VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to back out of the existing MHCR Dialog Templates, you must delete the templates that were added during installation.

4.  Open CPRS and select any patient, then click the Options tab and select Edit Shared Templates…

> The Template Editor screen opens.

5.  Click Action, then select Delete.
6.  Select the MHCR dialog templates list, then select the name of a template to be deleted.

> A confirmation message appears.

7.  Click Yes to confirm your delete.
8.  Repeat steps 3-4 for all templates that were added during installation. Backout is complete.

# Installing KIDS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users MAY remain on the system, but installation should be done at off peak hours when use is low. The estimated installation time is 10-15 minutes.

1.  Use the ‘LOAD A DISTRIBUTION’ option on the PackMan menu. The Host File name is: PXRM_2_0_32.KID
2.  Answer YES to the question: “Want to Continue with Load? YES//” The patch has now been loaded into a Transport global on your system.
3.  Use the KIDS option to install the Transport Global.
4.  On the KIDS menu, under the ‘Installation’ menu, use the following options to print, compare, verify, and back up the transport global:
    - Print Transport Global
    - Compare Transport Global to Current System
    - Verify Checksums in Transport Global
    - Backup a Transport Global
5.  From the ‘Installation Menu’ of the KIDS menu, run the option ‘Install Package(s)’, and then select the package ‘PXRM\*2.0\*32’ and proceed with the install.
6.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install’? NO// ‘
7.  Answer THE FOLLOWING according to your site's policy.
8.  When prompted 'Want KIDS to INHIBIT LOGONs during the install?” NO //’,respond NO
9.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For an example of loading a distribution, see the [<u>appendix</u>](#appendix---example-of-an-installation).

## KIDS Utilities Options (Optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Utilities Option: Build File Print

> Select BUILD NAME: PXRM\*2.0\*32 CLINICAL REMINDERS CLINICAL REMINDERS RECORD SYSTEM

> DEVICE: HOME// TELNET

#### Print Results of the Installation Process

> Select Kernel Installation & Distribution System Option: UTilities

> Build File Print Install File Print Edit Install Status

> Convert Loaded Package for Redistribution Display Patches for a Package

> Purge Build or Install Files Rollup Patches into a Build Update Routine File

> Verify a Build

> Verify Package Integrity

> EXAMPLE: Install File Print

> Select Utilities Option: INstall File Print

> Select INSTALL NAME: PXRM\*2.0\*32

> PXRM\*2.0\*32 Install Completed 10/30/13@19:26:15

> =\> PXRM\*2.0\*32 ;Created on Oct 15, 2013@13:18:44 DEVICE: HOME// \<ENTER\> or Select another print device name

> PACKAGE: PXRM\*2.0\*32 Nov 07, 2013 8:50 pm PAGE 1

> COMPLETED ELAPSED

> STATUS: Install Completed DATE LOADED: OCT 30,2013@19:18:12 INSTALLED BY: PROGRAMMER,ONE

> NATIONAL PACKAGE: CLINICAL REMINDERS

> (Example: Install File Print continued)

> INSTALL STARTED: OCT 30,2013@19:24:24 19:26:15 0:01:51

> ROUTINES: 19:24:24

> PRE-INIT CHECK POINTS:

> XPD PREINSTALL STARTED 19:24:24 XPD PREINSTALL COMPLETED 19:24:24

> FILES:

> REMINDER EXCHANGE 19:24:24

> POST-INIT CHECK POINTS:

> XPD POSTINSTALL STARTED 19:26:15 0:01:51

> XPD POSTINSTALL COMPLETED 19:26:15

> INSTALL QUESTION PROMPT ANSWER

> XPI1 Want KIDS to INHIBIT LOGONs during the install NO

> XPZ1 Want to DISABLE Scheduled Options, Menu Options, and Protocols NO MESSAGES:

> Install Started for PXRM\*2.0\*32: Oct 30, 2013@19:24:24

> Build Distribution Date: Oct 15, 2013

> Installing Routines:

> Oct 30, 2013@19:24:24

> Running Pre-Install Routine: PRE^PXRMP32I

> DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries:

> Oct 30, 2013@19:24:24

> Installing Data:

> Oct 30, 2013@19:24:24

> Running Post-Install Routine: POST^PXRMP32I ENABLE options.

> ENABLE protocols.

> There are 1 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry VA-MH EBP DIALOGS INCREMENT 3

> Updating Routine file...

> Updating KIDS files...

> PXRM\*2.0\*32 Installed. Oct 30, 2013@19:26:15

## CPRS Template Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following section details how you will use the TIU menu option "CPRS REMINDER CONFIGURATION" to prepare the newly installed dialog templates for use. This sets the access level for the templates to be made available for use in the Progress Note template drawer.

> Typically, the Clinical Application Coordinator (CAC) is designated to modify the Shared Templates folder, although this may not be the case at your facility.

### Setting the User Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before you can edit the Shared Templates, you must set the User Class.

1.  Select CPRS Configuration (IRM) Option.

#### Select General Parameter Tools Menu Option.

2.  Select Edit Parameter Values.
3.  Select PARAMETER DEFINITION NAME: TIU FIELD EDITOR CLASSES, then set the parameter values. Normally the Clinical Coordinator User Class is set at a SYSTEM Level.

### Preparing the templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  ![](pxrm-2-32-mental-health-clinical-reminder-dialog-templates-installation-guide/002.png)Select CPRS Reminder Configuration (located on the Reminder Managers Menu).

#### Reminder Managers Menu

> The CPRS Reminder Configuration menu opens.

2.  Select TIU Template Reminder Dialog Parameter. This allows you to enter the MHCR dialog templates to be accessed via the Shared template functionality as standalone templates, or as templates linked to TIU titles.

#### CPRS Reminder Configuration Menu

3.  The example below reflects a selection at the “SYSTEM” level. This level is recommended for ALL CPRS user access. Depending on the organization at your individual facility, determine whether to set the dialogs or reminders to the User, Service, Division or SYSTEM Levels access.
4.  Enter selection: 5 System VISTA.TEST.ORG

> Setting Reminder Dialogs allows as Templates for System: VISTA.TEST.ORG Select Display Sequence: ? \<ENTER\> to display the list of available templates for

> editing. The listing below contains reminder dialogs from previous release with names similar to the reminder dialogs being released with this patch.

> Display Sequence Value

> ---------------- -----

> 1 VA-MH ACT FOR DEPRESSION 3 CLOSING PHASE

> 5 VA-MH ACT FOR DEPRESSION 2 ACTION PHASE

> 10 VA-MH ACT FOR DEPRESSION 1 BEGINNING PHASE

> 15 VA-MH ACT FOR DEPRESSION EARLY TERMINATION

> 20 VA-MH CBT-D 3 FINAL PHASE

> 25 VA-MH CBT-D 2 MIDDLE PHASE

> 30 VA-MH CBT-D 1 INITIAL PHASE

> 35 VA-MH CBT-D EARLY TERMINATION

> 40 VA-MH CPT 12 FINAL

> 45 VA-MH CPT 7 PROBLEMATIC THINKING

> 50 VA-MH CPT 6 CHALLENGING QUESTIONS

> 55 VA-MH CPT 11 ESTEEM

> 60 VA-MH CPT 9 TRUST

> 65 VA-MH CPT 10 POWER CONTROL

> 70 VA-MH CPT 8 SAFETY

> 75 VA-MH CPT 5 REWRITE EVENT

> 80 VA-MH CPT 4 TRAUMA EVENT SESSION

> 85 VA-MH CPT 3 ABC SHEET

> 90 VA-MH CPT 1 INDIVIDUAL INITIAL

> 95 VA-MH CPT EARLY TERMINATION

> 100 VA-MH CPT 2 MEANING SESSION

> 105 VA-MH PEI 6 EARLY TERMINATION

> 110 VA-MH PEI 3RD SESSION

> 115 VA-MH PEI 2ND SESSION

> 120 VA-MH PEI 1 INITIAL

> 125 VA-MH PEI 5 FINAL SESSION

> 130 VA-MH PEI 4 IMAGINAL SESSIONS

> 135 VA-MH IPT 1 DEPRESSION

> 140 VA-MH IPT 2 DEPRESSION

> 145 VA-MH IPT 3 DEPRESSION

> 150 VA-MH IPT 4 DEPRESSION MAINTENANCE

> 155 VA-MH IPT EARLY TERMINATION

> 160 VA-MH CBT-I 1 EVALUATION SESSION

> 165 VA-MH CBT-I 2 INITIAL TREATMENT PHASE

> 170 VA-MH CBT-I 3 MIDDLE TREATMENT PHASE

175. VA-MH CBT-I 4 FINAL SESSION
176. VA-MH CBT-I EARLY TERMINATION

> 180 VA-MH BFT 1: ORIENTATION SESSION

> 185 VA-MH BFT 2: EDUCATION SESSION

> 190 VA-MH BFT 3: COMMUNICATION SESSION

> 195 VA-MH BFT 4: PROBLEM-SOLVING SESSION

> 200 VA-MH BFT 5: FINAL SESSION

> 205 VA-MH BFT 6: EARLY TERMINATION

> 210 VA-MH SST 1 INITIAL

> 215 VA-MH SST 2 GROUP VISIT

> 220 VA-MH SST 3 FINAL VISIT

> 225 VA-MH SST EARLY TERMINATION

> 230 VA-MH IBCT 1 INITIAL

> 235 VA-MH IBCT 2 INDIVIDUAL

> 240 VA-MH IBCT 3 NON VETERAN

> 245 VA-MH IBCT 4 FEEDBACK

> 250 VA-MH IBCT 5 THERAPY

> 255 VA-MH IBCT 6 TERMINATION

> 260 VA-MH IBCT EARLY TERMINATION

5.  Select Display Sequence: 1 \<ENTER\> ( Select the entry to edit by the number associated with the Dialog title)
6.  Select Display Sequence: Enter additional Display Sequence

> --OR--

> \<ENTER\> if no more entries to edit.

### Adding the templates to the CPRS template drawer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  ![](pxrm-2-32-mental-health-clinical-reminder-dialog-templates-installation-guide/003.png)Open CPRS and select any patient, then click Options and select Create New Shared Template…

#### CPRS Options menu

> The Template Editor screen opens, showing a Shared Template Properties section with an editable Name field, a Template Type list, and an Active check box.

> ![](pxrm-2-32-mental-health-clinical-reminder-dialog-templates-installation-guide/004.png)

#### Shared Template Properties section of Template Editor screen

2.  Type the name of a new template (notice that the template name appears on the left side of the screen, in the list of Shared Templates). Make sure that the Active check box is checked. Below is a list of mandated template drawer names for the Evidence-Based Psychotherapy (EBP) Reminder Dialogs.

> Note: Each EBP training program will educate their staff trainees and MH providers on the use of these EBP templates, and uniform naming will assist staff in knowing how to complete certain fields in specific reminder dialogs. Mental Health Services (VACO) *<u>mandates</u>* that the following names be used when adding these reminder dialogs to the local CPRS template drawer:

> Behavioral Family Therapy - BFT

- BFT 1 Orientation
- BFT 2 Education
- BFT 3 Communication
- BFT 4 Problem-Solving
- BFT 5 Final Session
- BFT Early Term

> Cognitive Behavioral Therapy for Insomnia - CBT-I \*

- CBT-I: 1 Evaluation
- CBT-I: 2 Initial
- CBT-I: 3 Middle
- CBT-I: 4 Final Session
- CBT-I: Early Term

> *\*Please place a colon (:) following CBT-I so that the capital I does not visually join with its following numbers; otherwise, the template appears to be named (for example) CBT-11 Evaluation versus CBT-I: 1 Evaluation.*

> Integrative Behavioral Couple Therapy - IBCT

- IBCT 1 Initial
- IBCT 2 Individual
- IBCT 3 Non-Veteran
- IBCT 4 Feedback
- IBCT 5 Therapy
- IBCT 6 Termination
- IBCT Early Term

> Interpersonal Psychotherapy for Depression - IPT

- IPT-D 1 Initial
- IPT-D 2 Intermediate
- IPT-D 3 Termination
- IPT-D 4 Maintenance
- IPT-D Early Term

> Social Skills Training - SST

- SST 1 Initial
- SST 2 Group Visit
- SST 3 Final Visit
- SST Early Term
3.  ![](pxrm-2-32-mental-health-clinical-reminder-dialog-templates-installation-guide/005.png)Click the Template Type list, then select Reminder Dialog.

#### Shared Template Properties section with arrow pointing to the selection in the Template Type list

> The reminder dialog template names appear below the Template Type field as shown in the screen shot below step 4.

4.  Verify the selections, then click Apply.

> ![](pxrm-2-32-mental-health-clinical-reminder-dialog-templates-installation-guide/006.png)

#### Reminder Dialog section with arrow pointing to template names, and another arrow pointing to the Apply button

### Verifying that the templates are properly installed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Open CPRS and select any patient, then click Notes, then click Templates. The Shared Templates icon displays.
2.  Expand the Shared Templates drawer.
3.  Verify that the expanded list of Shared Templates lists the Patch PXRM\*2.0\*32 protocols and their templates as shown below.

> Note: The example may also show template titles from the previous increment.

> ![](pxrm-2-32-mental-health-clinical-reminder-dialog-templates-installation-guide/007.png)

#### Expanded list of templates

> See the MHCR PXRM\*2.0\*32 Dialog Templates User Guide (PXRM_2_0_32_UG.PDF) for specific instructions on accessing and using the individual dialog templates included in this patch.

# Appendix - Example of an installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The steps are provided as prompts on your screen. User response is in Bold characters. Select Kernel Installation & Distribution System Option: Installation \<Enter\>

1.  *Load a Distribution*
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation Option: 1 \<Enter\> Load a Distribution Enter a Host File: \<your directory\>\\PXRM_2_0_32.KID

> KIDS Distribution saved on Oct 30, 2013@19:18:12

> Comment: PXRM\*2.0\*32

> This Distribution contains Transport Globals for the following Package(s): PXRM\*2.0\*32

> Distribution OK!

> Want to Continue with Load? YES// \<Enter\>

> Loading Distribution...

> PXRM\*2.0\*32

> Use INSTALL NAME: PXRM\*2.0\*32 to install this Distribution.

> Select INSTALL NAME: PXRM\*2.0\*32\<Enter\>

> Loaded from Distribution 10/30/13@19:18:12

> =\> PXRM\*2.0\*32;Created on Oct 15, 2013@13:18:44

> This Distribution was loaded on Oct 30, 2013@19:18:12 with header of PXRM\*2.0\*32;Created on Oct 15, 2013@13:18:44

> It consisted of the following Install(s): PXRM\*2.0\*32

> Checking Install for Package PXRM\*2.0\*32

> Install Questions for PXRM\*2.0\*32

> Incoming Files:

> 811.8 REMINDER EXCHANGE (including data)

> Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO// \<Enter\>

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// \<Enter\>

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// \<Enter\>

> Install Started for PXRM\*2.0\*32: Oct 30, 2013@19:24:24

> Build Distribution Date: Oct 15, 2013

> Installing Routines:

> Oct 30, 2013@19:24:24

> Running Pre-Install Routine: PRE^PXRMP32I

> DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries: Oct 30, 2013@19:24:24

> Installing Data:

> Oct 30, 2013@19:24:24

> Running Post-Install Routine: POST^PXRMP32I

> PXRM\*2.0\*32

> ENABLE options.

> ENABLE protocols.

> There are 1 Reminder Exchange entries to be installed.

> 1\. Installing Reminder Exchange entry VA-MH EBP DIALOGS INCREMENT 3

> Updating Routine file...

> Updating KIDS files...

> PXRM\*2.0\*32 Installed. Oct 30, 2013@19:26:15

> Install Message Sent

> 100% \| 25 50 75 \|

> Complete \[ \]

> Install Completed