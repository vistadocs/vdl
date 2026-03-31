---
title: PXRM*2*15  National TBI/Polytrauma Rehabilitation Dialog Install and Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: patch
doc_subject: National TBI/Polytrauma Rehabilitation Dialog Install and
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*15
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: > The National Defense and Authorization Act (NDAA) calls for VA Medical Centers to use standardized documentation that outlines the plan of rehabilitation care and community reintegration for patients who have experienced a Traumatic Brain Injury (TBI). To meet the needs of the NDAA, Patient Care S
audience: 
keywords: 
  - table
  - contents
  - blockquote
  - class
  - installation
  - install
  - style
  - width
  - transport
  - global
page_count: 0
word_count: 2449
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: March 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_15_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_15_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-15-national-tbi-polytrauma-rehabilitation-dialog-install-and-setup-guide/001.png)

# Clinical Reminders


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Clinical Reminders](#clinical-reminders)
  - [Contents](#contents)
  - [Introduction](#introduction)
    - [PXRM\2.0\15 Patch Description](#pxrm2015-patch-description)
    - [TIU\1\246 description](#tiu1246-description)
    - [Environment Check ROUTINE: TIUE246](#environment-check-routine-tiue246)
    - [Pre- and post-install routine: TIUP246](#pre-and-post-install-routine-tiup246)
    - [Web Sites](#web-sites)
  - [Pre-Installation](#pre-installation)
    - [Required Software](#required-software)
    - [Estimated Installation Time](#estimated-installation-time)
- [Installation](#installation)
    - [NOTE: Before proceeding with installation of this patch, make sure a CAC is present or has been consulted about the Document Class under Progress Notes in which the new TBI/POLYTRAUMA REHABILITATION/REINTEGRATION](#note-before-proceeding-with-installation-of-this-patch-make-sure-a-cac-is-present-or-has-been-consulted-about-the-document-class-under-progress-notes-in-which-the-new-tbipolytrauma-rehabilitationreintegration)
    - [Retrieve the PXRM\2.0\15 build](#retrieve-the-pxrm2015-build)
    - [Install the build first in a training or test account.](#install-the-build-first-in-a-training-or-test-account)
    - [Load the distribution.](#load-the-distribution)
    - [Example](#example)
    - [Backup a Transport Global](#backup-a-transport-global)
    - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
    - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
    - [Print Transport Global (optional)](#print-transport-global-optional)
    - [Install the build.](#install-the-build)
    - [Installation Example](#installation-example)
    - [Install File Print](#install-file-print)
    - [Build File Print](#build-file-print)
    - [Post-installation routines](#post-installation-routines)
    - [Deletion of init routines](#deletion-of-init-routines)
- [Setup](#setup)
    - [Steps to assign a reminder dialog to a TIU Template.](#steps-to-assign-a-reminder-dialog-to-a-tiu-template)
  - [Appendix A: Installation Example](#appendix-a-installation-example)
  - [Appendix B: Reminder Dialog](#appendix-b-reminder-dialog)
  - [Appendix C: FAQ](#appendix-c-faq)
    - [Q: What is meant by Current Problems (physical, mental, spiritually, etc.…)](#q-what-is-meant-by-current-problems-physical-mental-spiritually-etc)
    - [Q: Who is supposed to be the managing physician if the patient is seen by multiple specialists, such as MH, TBI, primary care, and what if the patient is being discharged from the hospital.](#q-who-is-supposed-to-be-the-managing-physician-if-the-patient-is-seen-by-multiple-specialists-such-as-mh-tbi-primary-care-and-what-if-the-patient-is-being-discharged-from-the-hospital)
    - [Q: Who is the Military Case Manager if the patient is discharged from the military? Does the document need to be sent to the military if the patient is a veteran? This raises the question: why are these fields required?](#q-who-is-the-military-case-manager-if-the-patient-is-discharged-from-the-military-does-the-document-need-to-be-sent-to-the-military-if-the-patient-is-a-veteran-this-raises-the-question-why-are-these-fields-required)
    - [Q: What is the date of review if the patient is being discharged from the hospital? This raises the question: why is this field required?](#q-what-is-the-date-of-review-if-the-patient-is-being-discharged-from-the-hospital-this-raises-the-question-why-is-this-field-required)
    - [Q: Is the Discharge Plan of Care for being discharged from the hospital or from the program?](#q-is-the-discharge-plan-of-care-for-being-discharged-from-the-hospital-or-from-the-program)
> Patches PXRM\*2\*15 and TIU\*1\*246
> National TBI/Polytrauma Rehabilitation Dialog
> INSTALLATION & SETUP GUIDE
> March 2009
> Office of Information and Technology Department of Veterans Affairs

## Contents 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  [Retrieve the PXRM\*2.0\*15 build 4](#installation)
2.  [Install the build first in a training or test account. 4](#installation)
3.  [Load the distribution. 4](#installation)
    1.  [Backup a Transport Global 4](#installation)
    2.  [Compare Transport Global to Current System 4](#installation)
    3.  [Verify Checksums in Transport Global 5](#verify-checksums-in-transport-global)
    4.  [Print Transport Global (optional) 5](#verify-checksums-in-transport-global)
4.  [Install the build. 5](#verify-checksums-in-transport-global)
5.  [Install File Print 6](#installation-example)
6.  [Build File Print 6](#installation-example)
7.  [Post-installation routines 6](#installation-example)
8.  [Deletion of init routines 6](#installation-example)
> ii Clinical Reminder Setup Guide March 2009

## Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Defense and Authorization Act (NDAA) calls for VA Medical Centers to use standardized documentation that outlines the plan of rehabilitation care and community reintegration for patients who have experienced a Traumatic Brain Injury (TBI). To meet the needs of the NDAA, Patient Care Services (PCS) supports the development of a standardized progress note title and associated documentation method for TBI Rehabilitation Care and Community Reintegration for use in the Computerized Patient Record System or in Veterans Health Information Systems & Technology Architecture (VistA) Order Entry/Results Reporting (OE/RR).

> Ultimately, the addition of a standardized note title and documentation will ensure all patients receive the same level of care. It will also allow for national monitoring of the program as standardized data can be rolled up and extracted to those individuals who monitor the program directly.

> This project consists of patch numbers PXRM\*2.0\*15 and TIU\*1\*246.

### PXRM\*2.0\*15 Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Reminder patch installs the Reminder Dialog VA-TBI/POLYTRAUMA REHAB/ REINTEGRATION PLAN OF CARE on your local system. The dialog will be used by Rehab clinicians to document the interdisciplinary treatment plan of care. The clinician will document the Type of Plan: an Initial plan, Interim Plan, or Discharge plan. The Type of Plan will be stored as a PCE Health Factor. In a future patch, the type of plan will be used to trigger a reminder for a follow-up review of the plan.

> The remainder of the reminder dialog contains required topics that one clinician will use to collect word processing responses to meet requirements specified by the Office of Rehabilitation Services at VACO and the Secretary’s office.

### TIU\*1\*246 description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch deploys the TBI/POLYTRAUMA DOCUMENTS / TBI/POLYTRAUMA REHABILITATION/REINTEGRATION PLAN OF CARE Document Class/Title Pair in support of NSR \#20080818. It maps the newly introduced TBI/POLYTRAUMA REHABILITATION/REINTEGRATION PLAN OF CARE National Title to the TBI

> TREATMENT PLAN NOTE Enterprise Standard Title, and if possible, activates the new title. It will optionally allow the site to attach the new TBI/POLYTRAUMA REHABILITATION/ REINTEGRATION PLAN OF CARE National Title to a local document class at the Clinical Application Coordinator's discretion.

### Environment Check ROUTINE: TIUE246

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Prior to installation, the routine checks to see whether the user is a member of the Clinical Application Coordinator (CAC) User Class. If not, it will prompt the user to affirm that they either have a CAC present with them, or have consulted a CAC, in order to offer an informed

> <span id="_bookmark1" class="anchor"></span>decision as to which Document Class the new Title should be assigned to (with the new National TBI/POLYTRAUMA DOCUMENTS as default). It will also detect the case where the installation is complete, and if necessary, allow the site to move the Title to a different Document Class, cleaning up any residue in the process.

### Pre- and post-install routine: TIUP246

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before the installation, it cleans out any prior instances of the REMINDERS EXCHANGE FILE ENTRY that deploys the TBI/POLYTRAUMA DOCUMENTS / TBI/POLYTRAUMA

> REHABILITATION/REINTEGRATION PLAN OF CARE Document Class / Title Pair. Following installation, the routine installs the new TIU DOCUMENT DEFINITION entries into file 8925.1, maps the new TBI/POLYTRAUMA REHABILITATION/REINTEGRATION

> PLAN OF CARE Title to the TREATMENT PLAN NOTE Enterprise Standard Title, activates the new title, and attaches the new Document Class to the PROGRESS NOTES class.

### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 36%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site</strong></th>
<th><strong>URL</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>National Clinical Reminders site</td>
<td><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></td>
<td><p>Contains manuals, PowerPoint presentations, and other information about</p>
<p>Clinical Reminders</p></td>
</tr>
<tr class="even">
<td>VistA Document Library</td>
<td><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></td>
<td><p>Contains manuals for Clinical Reminders</p>
<p>and</p></td>
</tr>
</tbody>
</table>

> This patch can be loaded with users on the system. Installation will take less than 2 minutes. Installation should be coordinated with the person who manages Clinical Reminders at your site and be scheduled during a time of lower system usage.

## Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual describes how to install and set up Clinical Reminders patch PXRM\*2\*15 and Text Integration Utilities patch, TIU\*1\*246.

> Before proceeding with installation of this patch, you need to either have a CAC present with you, or have consulted the CAC as to the Document Class under Progress Notes in which the new TBI/POLYTRAUMA REHABILITATION/REINTEGRATION PLAN OF CARE Title

> should be placed..

### Required Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Package/Patch</strong></th>
<th><strong>Namespace</strong></th>
<th><strong>Version</strong></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinical Reminders</td>
<td><blockquote>
<p>PXRM</p>
</blockquote></td>
<td>2.0</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>Health Summary</td>
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td>2.7</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>HL</td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>Kernel</td>
<td><blockquote>
<p>XU</p>
</blockquote></td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td><blockquote>
<p>XM</p>
</blockquote></td>
<td><blockquote>
<p>7.1</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Mental Health YS*5.01*85</td>
<td>YS</td>
<td><blockquote>
<p>5.01</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Text Integration Utilities (TIU)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td>DI</td>
<td>22</td>
<td>Fully patched</td>
</tr>
</tbody>
</table>

### Estimated Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Installation</p>
</blockquote></th>
<th><blockquote>
<p>About 2 minutes</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Setup after installation by the Reminder</p>
<p>Manager or CAC to address local implementation</p>
</blockquote></td>
<td><blockquote>
<p>Approximately 20 minutes (depending partly</p>
<p>on the experience level of the manager or CAC)</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This build can be installed with users on the system, but it should be done during non-peak hours.

### NOTE: Before proceeding with installation of this patch, make sure a CAC is present or has been consulted about the Document Class under Progress Notes in which the new TBI/POLYTRAUMA REHABILITATION/REINTEGRATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PLAN OF CARE Title should be placed.

> *The installation needs to be done by a person with DUZ(0) set to "@."*

### Retrieve the PXRM\*2.0\*15 build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use ftp to access the build, the name of the host file is PXRM_2_0_15.KID, from one of the following locations:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Albany</p>
</blockquote></th>
<th><mark>REDACTED</mark></th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

### Install the build first in a training or test account.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

### Load the distribution.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and PXRM_2_0_15.KID at the Host File prompt.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu, you may elect to use the following options:

### Backup a Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

### Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

### Verify Checksums in Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.

> Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

### Print Transport Global (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view the components of the KIDS build.

### Install the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*15 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE: DO NOT QUEUE THE INSTALLATION, because this installation may ask questions requiring responses and queuing will stop the installation. The most common are replacements for finding items or quick orders during the installation of Reminder Exchange file entries.

> NOTE: If you need to reinstall the build, you should answer No to the prompt “Is this acceptable” when you see this message:

### Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See <u>[Appendi](#appendix-a-installation-example)x A</u>.

### Install File Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process.

### Build File Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

### Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TIUP246

> This is the pre- and post-install routine for patch TIU\*1\*246. Before the installation, it cleans out any prior instances of the REMINDERS EXCHANGE FILE ENTRY that deploys the TBI/POLYTRAUMA DOCUMENTS / TBI/POLYTRAUMA INDIVIDUALIZED REHABILITATION/REINTEGRATION PLAN OF CARE

> Document Class /Title Pair. After installation, the routine installs the new TIU DOCUMENT DEFINITION entries into file 8925.1, maps the new TBI/POLYTRAUMA INDIVIDUALIZED REHABILITATION/REINTEGRATION PLAN OF CARE Title to

> the TREATMENT PLAN NOTE Enterprise Standard Title, activates the new title, and attaches the new Document Class to the PROGRESS NOTES class.

> PXRMP15I

> This is the pre- and post-install routine for patch PXRM\*2.0\*15. Before the installation, it cleans out any prior instances of the REMINDERS EXCHANGE FILE ENTRY that deploy the VA-TBI/POLYTRAUMA REHAB/REINTEGRATION PLAN OF CARE

> reminder dialog. Following installation, it invokes the Reminders Exchange Utility's Silent Installer to install the new VA-TBI/POLYTRAUMA REHAB/REINTEGRATION PLAN OF CARE reminder dialog.

### Deletion of init routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After everything has been successfully installed you may delete the init routines.

# Setup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VA-TBI/POLYTRAUMA REHAB/REINTEGRATION PLAN OF CARE reminder dialogs

> needs to be attached to the National Note TBI/POLYTRAUMA REHABILITATION/ REINTEGRATION PLAN OF CARE. This is done by assigning the reminder to a TIU Template, then attaching the template to the note title.

### Steps to assign a reminder dialog to a TIU Template.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Set the dialog to be used in a TIU Template. This is done by using the TIU Template Reminder Dialog Parameter under the CPRS Reminder Configuration option. Example is below.

> Select OPTION NAME: PXRM MANAGERS MENU Reminder Managers Menu

> Select Reminder Managers Menu Option: CP CPRS Reminder Configuration

> Select CPRS Reminder Configuration Option: TIU TIU Template Reminder Dialog Parameter

> Reminder Dialogs allows as Templates may be set for the following:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 14%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>1</th>
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
<td>3</td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>SRV</td>
<td><blockquote>
<p>[choose from SERVICE/SECTION]</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td>DIV</td>
<td><blockquote>
<p>[choose from INSTITUTION]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td>SYS</td>
<td><blockquote>
<p>[CPRS27.FO-SLC.MED.VA.GOV]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter selection: 5 System CPRS27.FO-SLC.MED.VA.GOV Select Display Sequence: 2

> Are you adding 2 as a new Display Sequence? Yes// YES

> Display Sequence: 2// 2

> Clinical Reminder Dialog: VA-TBI/POLYTRAUMA REHAB/REINTEGRATION PLAN OF CARE reminder dialog NATIONAL

> ...OK? Yes// \<Enter\> (Yes)

> Select Display Sequence: \<Enter\>

> CA Add/Edit Reminder Categories CL CPRS Lookup Categories

> CS CPRS Cover Sheet Reminder List MH Mental Health Dialogs Active PN Progress Note Headers

> RA Reminder GUI Resolution Active

> TIU TIU Template Reminder Dialog Parameter DL Default Outside Location

> PT Position Reminder Text at Cursor NP New Reminder Parameters

> GEC GEC Status Check Active WH WH Print Now Active

2.  ![](pxrm-2-15-national-tbi-polytrauma-rehabilitation-dialog-install-and-setup-guide/002.png)In CPRS, create the new template and assign the reminder dialog to it. This is done by accessing the template editor from the Notes Tab in CPRS Options\|Create New Template.
6.  ![](pxrm-2-15-national-tbi-polytrauma-rehabilitation-dialog-install-and-setup-guide/003.png)In the template editor, click on the Document Titles category in the Shared Templates window pane.
7.  Make sure Edit Shared Templates checkbox is “checked.”
8.  ![](pxrm-2-15-national-tbi-polytrauma-rehabilitation-dialog-install-and-setup-guide/004.png)Click on the template created in Step 3 in the Personal Templates window panes.
9.  Click on the arrow pointing to the left to move the new template under the Document Title category.
10. Click OK.

> ![](pxrm-2-15-national-tbi-polytrauma-rehabilitation-dialog-install-and-setup-guide/005.png)

> ![](pxrm-2-15-national-tbi-polytrauma-rehabilitation-dialog-install-and-setup-guide/006.png)

13. Test the template by selecting the TBI/POLYTRAUMA REHABILITATION/ REINTEGRATION PLAN OF CARE when writing a new note.
    - In the CPRS GUI, open the NOTES tab.
    - Click on New Note.
    - When the Progress Note Properties box opens, type TBI in the Title box.
    - ![](pxrm-2-15-national-tbi-polytrauma-rehabilitation-dialog-install-and-setup-guide/007.png)The TBI dialog template is displayed; click on it and click OK.
- The dialog opens up. Select the Plan of Care Type: Initial, Interim, or Discharge.

> NOTE: It’s okay to answer “No” to the statement, “Plan Has Been Communicated to Military.”

![](pxrm-2-15-national-tbi-polytrauma-rehabilitation-dialog-install-and-setup-guide/008.png)

![](pxrm-2-15-national-tbi-polytrauma-rehabilitation-dialog-install-and-setup-guide/009.png)

- Ensure that selecting a Plan of Care Type creates one of the following Health Factors for the visit: TBI/POLYTRAUMA INITIAL PLAN OF CARE, TBI/POLYTRAUMA INTERIM PLAN OF CARE, TBI/POLYTRAUMA DISCHARGE PLAN OF CARE.
- Ensure the progress note text generated by the reminder dialog is appropriate.

## Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Loaded from Distribution 2/3/09@16:18:16

> =\> PXRM\*2.0\*15 and TIU\*1.0\*246 ;Created on Feb 03, 2009@16:11:21

> This Distribution was loaded on Feb 03, 2009@16:18:16 with header of PXRM\*2.0\*15 and TIU\*1.0\*246 ;Created on Feb 03, 2009@16:11:21

> It consisted of the following Install(s): PXRM\*2.0\*15 TIU\*1.0\*246

> Checking Install for Package PXRM\*2.0\*15 Install Questions for PXRM\*2.0\*15

> Incoming Files:

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Checking Install for Package TIU\*1.0\*246

> Will first run the Environment Check Routine, TIUE246

> You are not known to the system to be a Clinical Application Coordinator (CAC).

> Before proceeding with installation of this patch, you need to either have a CAC present with you, or have consulted the CAC as to the Document Class under Progress Notes in which the new TBI/POLYTRAUMA REHABILITATION/REINTEGRATION PLAN OF CARE Title should be placed.

> Are You Prepared to Continue? NO// YES

> Install Questions for TIU\*1.0\*246

> Incoming Files:

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> To be selectable, the new TBI/POLYTRAUMA REHABILITATION/REINTEGRATION PLAN OF CARE title must be added to an appropriate Document Class. If you don't specify a local Document Class, the title will be associated with a new National one called TBI/POLYTRAUMA DOCUMENTS.

> ...

> Select Document Class for TBI/POLYTRAUMA: \<== select local Document class or press Enter

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// HOME

> Install Started for PXRM\*2.0\*15 :

> Feb 03, 2009@16:19:32

> Build Distribution Date: Feb 03, 2009

> Installing Routines:

> Feb 03, 2009@16:19:32

> Running Pre-Install Routine: PRE^PXRMP15I

> Installing Data Dictionaries:

> Feb 03, 2009@16:19:32

> Installing Data:

> Feb 03, 2009@16:19:32

> Running Post-Install Routine: POST^PXRMP15I

> Installing reminder VA-TBI/POLYTRAUMA REHAB/REINTEGRATION PLAN OF CARE

> Updating Routine file... Updating KIDS files...

> PXRM\*2.0\*15 Installed.

> Feb 03, 2009@16:19:41

> Not a production UCI

> NO Install Message sent

> TIU\*1.0\*246

> Install Started for TIU\*1.0\*246 :

> Feb 03, 2009@16:19:41

> Build Distribution Date: Feb 03, 2009

> Installing Routines:

> Feb 03, 2009@16:19:41

> Running Pre-Install Routine: PRE^TIUP246

> Installing Data Dictionaries:

> Feb 03, 2009@16:19:41

> Installing Data:

> Feb 03, 2009@16:19:41

> Running Post-Install Routine: POST^TIUP246

> Installing Reminder Exchange entry TIU\*1\*246 2009

> Updating Routine file...

> Updating KIDS files...

> TIU\*1.0\*246 Installed.

> Feb 03, 2009@16:19:41

> Not a production UCI NO Install Message sent Install Completed

## Appendix B: Reminder Dialog 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> REMINDER DIALOG INQUIRY Jan 15, 2009 3:27:58 pm Page 1

> NUMBER: 1538

> DIALOG NAME: VA-TBI/POLYTRAUMA REHAB/REINTEGRATION PLAN OF CARE

> Type: reminder dialog

> Associated reminder:

> Class: NATIONAL

> Sponsor: Office of Rehabilitation Services in VACO Review Date:

> Edit History:

> Edit Date: JAN 15,2009 14:45 Edit By: CRUSER, FIFTEEN

> Edit Comments: Exchange Install

> DIALOG COMPONENTS:

> Seq. Dialog

> 1 Element: VA-TBI/POLY TEXT

> Text: The sections included in the TBI/Polytrauma Rehabilitation and Reintegration Plan of Care are mandated as per the National Defense and Authorization Act of FY '08, Section 1702, paragraph 1710C. Content areas cannot be replaced based on prior local templates in order to maintain compliance with the language of the NDAA.

3.  Group: VA-TBI/POLY PLAN OF CARE TYPE Text: \[BOX, SUPPRESS, SHOW, ONE ONLY\] Resolution: DONE AT ENCOUNTER
    1.  Element: VA-TBI/POLY INITIAL PLAN Text: Initial Plan of Care

> Finding: TBI/POLYTRAUMA INITIAL PLAN OF CARE \[660172\] (HEALTH FACTOR)

> Resolution: DONE AT ENCOUNTER

> 3.5 Element: VA-TBI/POLY INTERIM PLAN Text: Interim Plan of Care

> Finding: TBI/POLYTRAUMA INTERIM PLAN OF CARE \[660177\] (HEALTH FACTOR)

> Resolution: DONE AT ENCOUNTER

> 3.10 Element: VA-TBI/POLY DISCHARGE PLAN Text: Discharge Plan of Care

> Finding: TBI/POLYTRAUMA DISCHARGE PLAN OF CARE \[660178\] (HEALTH FACTOR)

> Resolution: DONE AT ENCOUNTER

5.  Group: VA-TBI/POLY PLAN OF CARE QUESTIONS

> Text: Please answer all of the following questions. \[BOX, SUPPRESS, SHOW, NO SELECTION\]

1.  Element: VA-TBI/POLY MILITARY STATUS

> Text: Patient's current Military Status: {FLD:TBI/POLY MILITARY STATUS}

> 5.3 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.5 Element: VA-TBI/POLY HISTORY OF INJURIES

> Text: Brief History of injuries: {FLD:TBI/POLY INJURIES INFO}

> {FLD:TBI/POLY WORD PROCESSING}

> 5.8 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.10 Element: VA-TBI/POLY PROBLEMS Text: Current problems:

> {FLD:TBI/POLY WORD PROCESSING}

> 5.12 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.15 Element: VA-TBI/POLY PATIENT GOALS Text: Patient and Family Goals:

> {FLD:TBI/POLY WORD PROCESSING}

> 5.17 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.20 Element: VA-TBI/POLY IDT EVALUATIONS

> Text: Summary of Interdisciplinary Treatment (IDT) evaluations:

> {FLD:TBI/POLY IDT INFO}

> {FLD:TBI/POLY WORD PROCESSING}

> 5.22 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.25 Element: VA-TBI/POLY CONSULTS

> Text: Consults requested and/or follow-up on consults:

> {FLD:TBI/POLY WORD PROCESSING}

> 5.28 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.30 Element: VA-TBI/POLY IDT GOALS

> Text: Interdisciplinary Treatment Goals:

> {FLD:TBI/POLY WORD PROCESSING}

> 5.32 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> INFO}

> 5.35 Element: VA-TBI/POLY REHAB AND REINTEGRATION PLAN

> Text: Rehabilitation and Reintegration Plan: {FLD:TBI/POLY REHAB

> {FLD:TBI/POLY WORD PROCESSING}

> 5.37 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.40 Element: VA-TBI/POLY IDT CONF DATE

> Text: Date of IDT conference with patient and family to review plan:

> {FLD:TBI/POLY DATE}

> Written copy provided: {FLD:TBI/POLY YESNO}

> 5.43 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.45 Element: VA-TBI/POLY FAMILY ED AND SUPPORT NEEDS Text: Family education and support needs:

> {FLD:TBI/POLY WORD PROCESSING}

> 5.50 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.55 Element: VA-TBI/POLY CURRENT LIVING ARRANGEMENTS Text: Current location/living arrangements:

> {FLD:TBI/POLY WORD PROCESSING}

> 5.60 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.65 Element: VA-TBI/POLY VOCATIONAL STATUS

> Text: Current Vocational Status: {FLD:TBI/POLY VOCATIONAL INFO}

> {FLD:TBI/POLY VOCATIONAL STATUS}

> {FLD:TBI/POLY WORD PROCESSING}

> 5.75 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.80 Element: VA-TBI/POLY VOCATIONAL REHAB PLAN

> Text: Vocational Rehabilitation Plan: {FLD:TBI/POLY VOCATIONAL REHAB INFO}

> {FLD:TBI/POLY WORD PROCESSING}

> 5.85 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.90 Element: VA-TBI/POLY PHYSICIAN MANAGING IDT PLAN

> Text: Physician responsible for managing the treatment plan:

> {FLD:TBI/POLY CONTACT INFO}

> {FLD:TBI/POLY WORD PROCESSING}

> 5.95 Element: VA-TEXT BLANK LINE PN TEXT ONLY Text:

> 5.100 Element: VA-TBI/POLY CASE MANAGER

> Text: Polytrauma/TBI Case Manager responsible for monitoring implementation: {FLD:TBI/POLY CONTACT INFO}

> {FLD:TBI/POLY WORD PROCESSING}

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>5.105</th>
<th><blockquote>
<p>Element: VA-TEXT BLANK LINE PN TEXT ONLY</p>
<p>Text:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5.110</td>
<td><blockquote>
<p>Element: VA-TBI/POLY MILITARY CASE MANAGER</p>
<p>Text: Military Case Manager: {FLD:TBI/POLY CONTACT INFO}</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>{FLD:TBI/POLY WORD PROCESSING}</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5.115</td>
<td><blockquote>
<p>Element: VA-TEXT BLANK LINE PN TEXT ONLY</p>
<p>Text:</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5.120</td>
<td><blockquote>
<p>Element: VA-TBI/POLY PLAN COMM TO MILITARY</p>
<p>Text: Plan has been communicated to military: {FLD:TBI/POLY YESNO}</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5.125</td>
<td><blockquote>
<p>Element: VA-TEXT BLANK LINE PN TEXT ONLY</p>
<p>Text:</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5.130</td>
<td><blockquote>
<p>Element: VA-TBI/POLY OTHER CARE COORD INFO</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>5.135</th>
<th><blockquote>
<p>Element: VA-TEXT BLANK LINE PN TEXT ONLY</p>
<p>Text:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5.140</td>
<td><blockquote>
<p>Element: VA-TBI/POLY NEXT REVIEW DATE</p>
<p>Text: Date care plan will be reviewed {FLD:TBI/POLY DATE}</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5.145</td>
<td><blockquote>
<p>Element: VA-TEXT BLANK LINE PN TEXT ONLY</p>
<p>Text:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5.150</td>
<td><blockquote>
<p>Element: VA-TBI/POLY ADDITIONAL INFO</p>
<p>Text: Additional Information: {FLD:TBI/POLY ADD INFO}</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix C: FAQ 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Q: What is meant by Current Problems (physical, mental, spiritually, etc.…)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A: The purpose of the template is to document the Rehabilitation and Reintegration plan of care. Community reintegration refers to the resumption of age, gender, and culturally appropriate roles in the family, community and workplace. Community reintegration should emphasize a multidisciplinary approach, which also includes peers and family, in the attempt to close the gap between treatment activities and functional competence in the individual’s natural environment. The primary focus of community reintegration should be on what the individual with polytrauma and TBI needs to achieve for returning to home, community, work, or school. That being said, the current problems section of the template should be used to address any barriers the patient is facing, which are limiting their ability to successfully resume the roles mentioned above. There is intentional flexibility to allow the treatment team to document the primary problems for each individual patient, but this could refer to physical, mental, spiritual problems, or even be broken down further into memory, balance, strength, cognition, etc., problems.

### Q: Who is supposed to be the managing physician if the patient is seen by multiple specialists, such as MH, TBI, primary care, and what if the patient is being discharged from the hospital.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A: The managing physician should be the physiatrist on the Polytrauma/TBI Interdisciplinary Team.

### Q: Who is the Military Case Manager if the patient is discharged from the military? Does the document need to be sent to the military if the patient is a veteran? This raises the question: why are these fields required?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A: This would not be applicable if the patient has been discharged from the military. The law says VA is to assume case management roles if they are discharged.

### Q: What is the date of review if the patient is being discharged from the hospital? This raises the question: why is this field required?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A: The template is to document the Rehabilitation and Reintegration plan of care for a patient as s/he transitions back into the community. It is not an inpatient-specific tool, but rather a tool for the IDT to document their plan as patients resume their roles or ‘reintegrates’ back into the community.

### Q: Is the Discharge Plan of Care for being discharged from the hospital or from the program?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A: This can be either, depending upon the overall plan for the patient. If the IDT feels an inpatient does not have future issues to be addressed related to their rehabilitation and

> reintegration back into the community, it may take place at the time of DC from the hospital. In many cases, these individuals may continue to require services as they resume their roles in the community, and the Discharge plan of care would then be utilized when they are ultimately DC’d from the IDT program while an outpatient.