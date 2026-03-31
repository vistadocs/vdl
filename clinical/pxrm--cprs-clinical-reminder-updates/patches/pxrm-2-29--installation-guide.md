---
title: PXRM*2*29 Mental Health Clinical Reminder Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Mental Health Clinical Reminder
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*29
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document describes the installation and setup for the national release of Mental Health Clinical Reminder (MHCR) Dialog Templates, patch PXRM\2.0\29. This patch is made up of Increments 1 and 2 of four increments. Clinicians will use these templates to document veteran patient treatment as re
audience: 
keywords: 
  - table
  - contents
  - templates
  - installation
  - blockquote
  - template
  - pxrm
  - reminder
  - cprs
  - class
page_count: 0
word_count: 2123
section_count: 15
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_29_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_29_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> Department of Veterans Affairs

# Office of Information & Technology (OIT) Product Development


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Office of Information & Technology (OIT) Product Development](#office-of-information-technology-oit-product-development)
    - [September 2014](#september-2014)
- [Introduction](#introduction)
  - [Target audience](#target-audience)
  - [Patch PXRM\2.0\29 entries](#patch-pxrm2029-entries)
  - [Full template titles for PXRM\2.0\29](#full-template-titles-for-pxrm2029)
  - [Project references](#project-references)
  - [Acronyms and definitions](#acronyms-and-definitions)
  - [Section 508 compliance](#section-508-compliance)
- [Pre-Installation](#pre-installation)
  - [Installation system notes and requirements](#installation-system-notes-and-requirements)
  - [Software retrieval](#software-retrieval)
  - [Security management](#security-management)
  - [Backup routines (optional)](#backup-routines-optional)
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
- [Appendix – Install Example](#appendix-install-example)
> Mental Health Clinical Reminder Dialog Templates
![](pxrm-2-29-mental-health-clinical-reminder-installation-guide/001.png)
> Installation Guide Patch PXRM\*2.0\*29

### September 2014

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 1.2
> Revision History
<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 43%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>August 2014</p>
</blockquote></td>
<td>1.2</td>
<td>Patch PXRM*2.0*29 (Increments 1 &amp; 2) Backup instructions added</td>
<td>Information Innovators Inc.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>August 2013</p>
</blockquote></td>
<td>1.1</td>
<td>Patch PXRM*2.0*29 (Increments 1 &amp; 2) revised</td>
<td>Information Innovators Inc.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>January 2013</p>
</blockquote></td>
<td>1.0</td>
<td>Patch PXRM*2.0*29 (Increments 1 &amp; 2)</td>
<td>Information Innovators Inc.</td>
</tr>
</tbody>
</table>
> Contents
1.  [Introduction 1](#introduction)
    1.  [Target audience 1](#target-audience)
    2.  [Patch PXRM\*2.0\*29 entries 1](#patch-pxrm2.029-entries)
    3.  [Full template titles for PXRM\*2.0\*29 1](#full-template-titles-for-pxrm2.029)
    4.  [Project references 2](#project-references)
    5.  [Acronyms and definitions 3](#acronyms-and-definitions)
    6.  [Section 508 compliance 3](#section-508-compliance)
2.  [Pre-Installation 3](#pre-installation)
    1.  [Installation system notes and requirements 3](#installation-system-notes-and-requirements)
    2.  [Software retrieval 4](#software-retrieval)
    3.  [Security management 4](#security-management)
    4.  [Backup routines (optional) 4](#backup-routines-optional)
    5.  [Backout plan (optional) 5](#backout-plan-optional)
        1.  [To remove the Reminder Exchange Entries from VistA 5](#to-remove-the-reminder-exchange-entries-from-vista)
        2.  [To delete the templates from VistA 5](#to-delete-the-templates-from-vista)
3.  [Installing KIDS 6](#installing-kids)
    1.  [Installation 6](#installation)
    2.  [KIDS Utilities Options (Optional) 6](#kids-utilities-options-optional)
    3.  [CPRS Template Installation 9](#cprs-template-installation)
        1.  [Setting the User Class 9](#setting-the-user-class)
        2.  [Preparing the templates 9](#preparing-the-templates)
        3.  [Adding the templates to the CPRS template drawer 12](#adding-the-templates-to-the-cprs-template-drawer)
        4.  [Verifying that the templates are properly installed 15](#verifying-that-the-templates-are-properly-installed)
[Appendix – Install Example 17](#appendix-install-example)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes the installation and setup for the national release of Mental Health Clinical Reminder (MHCR) Dialog Templates, patch PXRM\*2.0\*29. This patch is made up of Increments 1 and 2 of four increments. Clinicians will use these templates to document veteran patient treatment as requested by Mental Health Services (MHS, previously OMHS). The templates are components of Evidence Based Psychotherapy (EBP) protocols, designed for the treatment of mental health conditions. The EBP protocols included in this patch are listed in section 1.3.

> The patch PXRM\*2.0\*29 (Increments 1 and 2) comprises four protocols with 27 accompanying dialog templates (listed below) and associated Health Factors. The templates will be accessed through the CPRS Shared Template Drawer, but do not contain any cohort or resolution logic.

## Target audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The intended user is familiar with the VistA computing environment (Kernel Installation and Distribution System \[KIDS\]).

## Patch PXRM\*2.0\*29 entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch will create four Reminder Exchange entries:

- VA-MH CPT DIALOGS
- VA-MH PE DIALOGS
- VA-MH ACT DIALOGS
- VA-MH CBT-D DIALOGS

## Full template titles for PXRM\*2.0\*29

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Mandated template drawer names are listed in the installation procedure steps. To facilitate clinician recognition of the correct templates, those drawer names are abbreviated versions of the titles listed in full here. The national EBP training programs have created clinician training materials based on the mandated (abbreviated) template drawer names, therefore the names, the order of those names, and the names of their enclosing folders should be followed (see 3.3.3.2).

> CPT - Cognitive Processing Therapy

- VA-MH CPT 1 INITIAL
- VA-MH CPT 2 MEANING SESSION
- VA-MH CPT 3 ABC SHEET
- VA-MH CPT 4 TRAUMA EVENT SESSION
- VA-MH CPT 5 REWRITE EVENT
- VA-MH CPT 6 CHALLENGING QUESTIONS
- VA-MH CPT 7 PROBLEMATIC THINKING
- VA-MH CPT 8 SAFETY
- VA-MH CPT 9 TRUST
- VA-MH CPT 10 POWER CONTROL
- VA-MH CPT 11 ESTEEM
- VA-MH CPT 12 FINAL
- VA-MH CPT EARLY TERMINATION

> PEI - Prolonged Exposure

- VA-MH PEI 1 INITIAL
- VA-MH PEI 2nd SESSION
- VA-MH PEI 3rd SESSION
- VA-MH PEI 4 IMAGINAL SESSIONS
- VA-MH PEI 5 FINAL SESSION
- VA-MH PEI EARLY TERMINATION

> ACT-D - Acceptance and Commitment Therapy for Depression

- VA-MH ACT-D 1 BEGINNING PHASE
- VA-MH ACT-D 2 ACTION PHASE
- VA-MH ACT-D 3 CLOSING PHASE
- VA-MH ACT-D EARLY TERMINATION

> CBT-D - Cognitive Behavior Therapy for Depression

- VA-MH CBT-D 1 INITIAL PHASE
- VA-MH CBT-D 2 MIDDLE PHASE
- VA-MH CBT-D 3 FINAL PHASE
- VA-MH CBT-D EARLY TERMINATION

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
<td>PXRM_2_UM.PDF</td>
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
<td><a href="http://www.va.gov/vdl/documents/Clinical/CompPatient_Recrd_Sys_(CPRS)/cprsguium.pdf">http://www.va.gov/vdl/documents/Clinical/CompPatient_Recrd_Sys_(CPRS)/cprsguium.pdf</a></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Health Summary Technical Manual</p>
</blockquote></td>
<td><a href="http://www.va.gov/vdl/documents/Clinical/CPRS-Health_Summary/hsum2_7_tm.pdf">http://www.va.gov/vdl/documents/Clinical/CPRS-Health_Summary/hsum2_7_tm.pdf</a></td>
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
<p><strong>Web Site</strong></p>
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
<p>VistA Document Library</p>
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
| LEBPC    | Local Evidence-Based Psychotherapy Coordinators                 |
| MHCR     | Mental Health Clinical Reminder                                 |
| MHS      | Mental Health Services (previously OMHS)                        |
| MHTC     | Mental Health Treatment Coordinator                             |
| OHI      | Office of Health Information                                    |
| OI       | Office of Information                                           |
| OIT/OI&T | Office of Information Technology                                |
| OMHS     | Office of Mental Health Services (now MHS)                      |
| PTM      | Patch Tracker Message                                           |
| PXRM     | Clinical Reminder Package Namespace                             |

## Section 508 compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Veterans Health Administration (VHA) fully supports Section 508 of *The Rehabilitation Act* and is committed to equal access for all users. The MHCR dialog templates project was evaluated according to parameters. Because the templates are a minor addition to VistA CPRS and use VistA tools, Section 508 compliance was determined to be N/A.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation system notes and requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Coordinate the patch installation with Local Evidence-Based Psychotherapy Coordinators (LEBPC), Clinical Application Coordinators (CACs), Reminders Managers, and IT Staff.
2.  Make sure that Mental Health Assistant (MHA 3) is fully installed prior to installing patch PXRM\*2.0\*29.
3.  Back up the VistA system prior to the patch installation. If it becomes necessary to remove the patch and associated dialog templates, the system back-up can then be restored to the date and time prior to the installation.

#### VistA Operating System

> Mental Health Clinical Reminders Dialog Templates – PXRM\*2.0\*29 patch, as well as CPRS, and MHA3, currently run on the standard hardware platforms used by the Department of Veterans Affairs Health Care System facilities. These systems consist of standard or upgraded Alpha AXP clusters, and run either Cache-VMS or Cache-NT and the Open M product.

#### MHCR Software Application Installation Time

> MHCR Patch PXRM\*2.0\*29 installation time takes approximately 25 minutes during off-peak hours.

#### Users on the System

> Users may remain on the system. However, installation should be done during off-peak hours.

#### Kernel Installation and Distribution System (KIDS)

> PXRM\*2.0\*29 is created using the Kernel Installation and Distribution System (KIDS). For further instructions on using KIDS, please refer to the Kernel V.8.0 Systems Manual.

#### Namespace

> Mental Health Clinical Reminder Patch PXRM\*2.0\*29 namespace is PXRM.

## Software retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Your site will receive the Mental Health Clinical Reminders Dialog Template files as part of patch PXRM\*2.0\*29 via a host file. The preferred method is to FTP the files from:

#### download.vista.med.va.gov

> This location automatically transmits files from the first available FTP Server to the appropriate directory on your system. (See the order listed below under the FTP Address column). If you prefer, you can retrieve the software directly from one of the FTP Servers listed below.

| OI Field Office | FTP Address                           | Directory                             |
|---------------------|-------------------------------------------|-------------------------------------------|
| Albany (NY)         | <span class="mark"><u>REDACTED</u></span> | <span class="mark"><u>REDACTED</u></span> |
| Hines (IL)          | <span class="mark"><u>REDACTED</u></span> | <span class="mark"><u>REDACTED</u></span> |
| Salt Lake City (UT) | <span class="mark"><u>REDACTED</u></span> | <span class="mark"><u>REDACTED</u></span> |

## Security management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no unique legal requirements pertaining to Mental Health Assistant software applications, other than some of the psychological tests are copyrighted. Copyrighted tests can be used with permission from the copyright holders and must be consistent with contracts between VHA and copyright holders.

## Backup routines (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No routines are being installed by this content-only patch; however, we recommend performing a backup of the transport global before installing the VistA MHCR Dialog Templates Patch PXRM\*2.0\*29.

> The option called Backup a Transport Global \[XPD BACKUP\] creates a MailMan message that backs up all current routines on your system that would be replaced by a KIDS patch. This option is under the Installation menu of the KIDS menu. It works on a patch that has been loaded on your system, but not installed.

> Example of the option “Backup a Transport Global:”

## Backout plan (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### To remove the Reminder Exchange Entries from VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the Reminder Exchange Menu Option.
2.  Select the Exchange File entries that were installed by this patch. Example: CPT 1 Initial

> Warning: There is no confirmation question prior to the delete function in step 3.

3.  Select the number that matches the entry you want to remove; this will select the option:

> DFE Delete Exchange File Entry. The Exchange File Entry is deleted.

### To delete the templates from VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to back out of the existing MHCR Dialog Templates, you must delete the templates that were added during installation.

4.  Open CPRS and select any patient, then click the Options tab and select Edit Shared Templates…

> The Template Editor screen opens.

5.  Click Action, then select Delete.
6.  Select the MHCR dialog templates list, then select the name of a template to be deleted. A confirmation message appears.
7.  Click Yes to confirm your delete.

> Repeat steps 3-4 for all templates that were added during installation. Backout is complete.

# Installing KIDS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users may remain on the system, but installation should be done at off-peak hours when use is low. The estimated installation time is 25 minutes.

1.  Use the ‘LOAD A DISTRIBUTION’ option on the PackMan menu. The Host File name is: \<your directory\>PXRM_2_0_29.KID
2.  Answer YES to the question: “Want to Continue with Load? YES//” The patch has now been loaded into a Transport global on your system.
3.  Use the KIDS option to install the Transport Global.
4.  On the KIDS menu, under the ‘Installation’ menu, you may use the following options to print, compare, verify, and back up the transport global:
    - Print Transport Global
    - Compare Transport Global to Current System
    - Verify Checksums in Transport Global
    - Backup a Transport Global

> Example of the option “Backup a Transport Global”: See 2.4, Backup Routines.

5.  From the ‘Installation Menu’ option on the KIDS menu, run the option ‘Install Package(s)’, and then select the package name ‘PXRM\*2.0\*29’ and proceed with the install.
6.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install’?NO// ‘
7.  Answer THE FOLLOWING items 8 and 9according to your site's policy.
8.  When prompted 'Want KIDS to INHIBIT LOGONs during the install//', respond NO.
9.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols?YES//', respond NO

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the appendix for an example of *Loading a Distribution*.

## KIDS Utilities Options (Optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \>D ^XUP

> Setting up programmer environment Terminal Type set to: C-VT100

> Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System menu

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: UTilities

> Build File Print Install File Print

> Convert Loaded Package for Redistribution Display Patches for a Package

> Purge Build or Install Files Rollup Patches into a Build Update Routine File

> Verify a Build

> Verify Package Integrity

> Select Utilities Option: Build File Print

> Select BUILD NAME: PXRM\*2.0\*29 CLINICAL REMINDERS CLINICAL REMINDERS RECORD SYSTEM

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

> Select INSTALL NAME: PXRM\*2.0\*29

> PXRM\*2.0\*29 Install Completed 10/30/12@19:26:15

> =\> PXRM\*2.0\*29 ;Created on Oct 15, 2012@13:18:44 DEVICE: HOME// \<ENTER\> or Select another print device name

> PACKAGE: PXRM\*2.0\*29 Nov 07, 2012 8:50 pm PAGE 1

> COMPLETED ELAPSED

> STATUS: Install Completed DATE LOADED: OCT 30,2012@19:18:12 INSTALLED BY: PROGRAMMER,ONE

> NATIONAL PACKAGE: CLINICAL REMINDERS

> (Example: Install File Print continued)

> INSTALL STARTED: OCT 30,2012@19:24:24 19:26:15 0:01:51

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

> Install Started for PXRM\*2.0\*29: Oct 30, 2012@19:24:24

> Build Distribution Date: Oct 15, 2012 Installing Routines:

> Oct 30, 2012@19:24:24

> Running Pre-Install Routine: PRE^PXRMP29I DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries:

> Oct 30, 2012@19:24:24

> Installing Data:

> Oct 30, 2012@19:24:24

> Running Post-Install Routine: POST^PXRMP29I

## CPRS Template Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IMPORTANT: You must perform the installation in VistA, so that the templates will be available in CPRS under the Progress Note template drawer.

> Typically, the Clinical Application Coordinator (CAC) is designated to modify the Shared Templates folder, although this may not be the case at your facility.

### Setting the User Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You must set the User Class before you can edit the Shared Templates.

1.  Select CPRS Configuration (IRM) Option.

#### Select General Parameter Tools Menu Option.

2.  Select Edit Parameter Values.
3.  Select PARAMETER DEFINITION NAME: TIU FIELD EDITOR CLASSES, then set the parameter values. Normally the Clinical Coordinator User Class is set at a SYSTEM Level.

### Preparing the templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

4.  Select CPRS Reminder Configuration (located on the Reminder Managers Menu).

> ![](pxrm-2-29-mental-health-clinical-reminder-installation-guide/002.png)

#### Reminder Managers Menu

> The CPRS Reminder Configuration menu opens.

5.  Select TIU Template Reminder Dialog Parameter. This allows you to enter the MHCR dialog templates to be accessed via the Shared template functionality as standalone templates, or as templates linked to TIU titles.

#### CPRS Reminder Configuration Menu

6.  The example below reflects a selection at the “SYSTEM” level. This level is recommended for ALL CPRS user access. Depending on the organization at your individual facility, determine whether to set the dialogs or reminders to the User, Service, Division or SYSTEM Levels access.
7.  Enter selection: 5 System VISTA.TEST.ORG

> Setting Reminder Dialogs allows as Templates for System: VISTA.TEST.ORG Select Display Sequence: ? \<ENTER\> to display the list of available templates for editing.

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

8.  Select Display Sequence: 1 \<ENTER\> ( Select the entry to edit by the number associated with the Dialog title). Note: All 27 Reminder Dialogs will need to be added.
9.  Select Display Sequence: Enter additional Display Sequence

> --OR--

> \<ENTER\> if no more entries to edit.

### Adding the templates to the CPRS template drawer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

10. ![](pxrm-2-29-mental-health-clinical-reminder-installation-guide/003.png)Open CPRS and select any patient, then click Options and select Create New Shared Template…

#### CPRS Options menu

> The Template Editor screen opens, showing a Shared Template Properties section with an editable Name field, a Template Type list, and an Active check box:

> ![](pxrm-2-29-mental-health-clinical-reminder-installation-guide/004.png)

#### Shared Template Properties section of Template Editor screen

11. Type the name of a new template, and make sure that the Active check box is checked. The name appears on the list under Shared Templates (left pane).

> Note: Each EBP training program will educate their staff trainees and MH providers on the use of these EBP templates, so having similar naming will assist staff in knowing how to complete certain fields in specific reminder dialogs. Mental Health Services (VACO) mandates that the following names be used when adding these reminder dialogs to the local CPRS template drawer:

> CPT - Cognitive Processing Therapy

- VA-MH CPT 1 INITIAL
- VA-MH CPT 2 MEANING SESSION
- VA-MH CPT 3 ABC SHEET
- VA-MH CPT 4 TRAUMA EVENT SESSION
- VA-MH CPT 5 REWRITE EVENT
- VA-MH CPT 6 CHALLENGING QUESTIONS
- VA-MH CPT 7 PROBLEMATIC THINKING
- VA-MH CPT 8 SAFETY
- VA-MH CPT 9 TRUST
- VA-MH CPT 10 POWER CONTROL
- VA-MH CPT 11 ESTEEM
- VA-MH CPT 12 FINAL
- VA-MH CPT EARLY TERMINATION

> PEI - Prolonged Exposure

- VA-MH PEI 1 INITIAL
- VA-MH PEI 2nd SESSION
- VA-MH PEI 3rd SESSION
- VA-MH PEI 4 IMAGINAL SESSIONS
- VA-MH PEI 5 FINAL SESSION
- VA-MH PEI EARLY TERMINATION

> ACT-D - Acceptance and Commitment Therapy for Depression

- VA-MH ACT-D 1 BEGINNING PHASE
- VA-MH ACT-D 2 ACTION PHASE
- VA-MH ACT-D 3 CLOSING PHASE
- VA-MH ACT-D EARLY TERMINATION

> CBT-D - Cognitive Behavior Therapy for Depression

- VA-MH CBT-D 1 INITIAL PHASE
- VA-MH CBT-D 2 MIDDLE PHASE
- VA-MH CBT-D 3 FINAL PHASE
- VA-MH CBT-D EARLY TERMINATION
  1.  ![](pxrm-2-29-mental-health-clinical-reminder-installation-guide/005.png)Click the Template Type list, then select Reminder Dialog.

#### Shared Template Properties section with arrow pointing to the selection in the Template Type list

> The reminder dialog template names appear below the Template Type field as shown in the screen shot below step 4.

2.  ![](pxrm-2-29-mental-health-clinical-reminder-installation-guide/006.png)Verify the selection, then click Apply.

#### Reminder Dialog section with arrow pointing to Reminder Dialog names, and second arrow pointing to the Apply button

### Verifying that the templates are properly installed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3.  Open CPRS and select any patient, then click Notes, then click Templates. The Shared Templates icon displays.
4.  Expand the Shared Templates drawer.
5.  Verify that the expanded list of Shared Templates lists the Patch PXRM\*2.0\*29 protocols and their templates as shown below:

> ![](pxrm-2-29-mental-health-clinical-reminder-installation-guide/007.png)

#### Expanded list of templates

> See the MHCR PXRM\*2.0\*29 User Manual for specific instructions on the individual dialog templates included in this patch.

# Appendix – Install Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The steps are provided as prompts on your screen. User response is in bold typeface.

#### “LOADING A DISTRIBUTION”

> Select Kernel Installation & Distribution System Option: Installation \<Enter\>

1.  *Load a Distribution*
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation Option: 1 \<Enter\> Load a Distribution Enter a Host File: \<your directory\>PXRM_2_0_29.KID KIDS Distribution saved on Sep 20, 2012@09:07:30 Comment: PXRM\*2.0\*29

> This Distribution contains Transport Globals for the following Package(s): PXRM\*2.0\*29

> Distribution OK!

> Want to Continue with Load? YES// \<Enter\>

> Loading Distribution... PXRM\*2.0\*29

> Use INSTALL NAME: PXRM\*2.0\*29 to install this Distribution. Select Installation Option : INstall Package(s)

> Select INSTALL NAME: PXRM\*2.0\*29 \<Enter\>

> Loaded from Distribution 10/30/12@19:18:12

> =\> PXRM\*2.0\*29 ;Created on Oct 15, 2012@13:18:44

> This Distribution was loaded on Oct 30, 2012@19:18:12 with header of PXRM\*2.0\*29 ;Created on Oct 15, 2012@13:18:44

> It consisted of the following Install(s): PXRM\*2.0\*29

> Checking Install for Package PXRM\*2.0\*29 Install Questions for PXRM\*2.0\*29 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data)

> Note: You already have the 'REMINDER EXCHANGE' File.

> I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO// \<Enter\>

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// \<Enter\>

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// \<Enter\>

> Install Started for PXRM\*2.0\*29 :

> Oct 30, 2012@19:24:24

> Build Distribution Date: Oct 15, 2012 Installing Routines:

> Oct 30, 2012@19:24:24

> Running Pre-Install Routine: PRE^PXRMP29I DISABLE options.

> DISABLE protocols. Installing Data Dictionaries:

> Oct 30, 2012@19:24:24

> Installing Data:

> Oct 30, 2012@19:24:24

> Running Post-Install Routine: POST^PXRMP29I PXRM\*2.0\*29

> ENABLE options. ENABLE protocols.

> There are 4 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry VA-MH CPT MH DIALOGS
2.  Installing Reminder Exchange entry VA-MH PEI MH DIALOGS
3.  Installing Reminder Exchange entry VA-MH ACT DIALOGS
4.  Installing Reminder Exchange entry VA- MH CBT-D DIALOGS

> Updating Routine file... Updating KIDS files... PXRM\*2.0\*29 Installed. Oct 30, 2012@19:26:15

> Install Message Sent 100% \| 25 50 75 \|

> Complete \[ \] Install Completed

> \*\*End of Sample Installation\*\*