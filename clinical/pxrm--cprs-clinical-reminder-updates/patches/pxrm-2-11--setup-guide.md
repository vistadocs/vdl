---
title: PXRM*2*11 National Reminder & Dialog Updates Install and Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: patch
doc_subject: National Reminder & Dialog Updates Install and
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*11
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - reminder
  - contents
  - class
  - installation
  - date
  - entry
  - service
  - finding
  - print
page_count: 0
word_count: 4474
section_count: 22
table_count: 5
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: October 2008
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_11_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_11_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-11-national-reminder-dialog-updates-install-and-setup-guide/001.png)

Clinical RemindersPatch PXRM\*2\*11National Reminder and Dialog Updates

INSTALLATION & SETUP GUIDE

October 2008

Health Provider Systems

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Contents](#contents)
- [Introduction](#introduction)
  - [Patch PXRM\2.0\11 includes the following modifications to the Clinical Reminders package:](#patch-pxrm2011-includes-the-following-modifications-to-the-clinical-reminders-package)
    - [Web Sites](#web-sites)
  - [# Pre-Installation](#pre-installation)
  - [Required Software](#required-software)
  - [## Estimated Installation Time](#estimated-installation-time)
  - [## Pre-Installation Steps](#pre-installation-steps)
  - [Do a reminder term inquiry and save for post-installation comparisons](#do-a-reminder-term-inquiry-and-save-for-post-installation-comparisons)
  - [> The following terms have changed and may need to be remapped, if previously mapped locally. The ones in bold will almost definitely need remapping. Please use the option, “Inquire about a reminder term” on these terms for post-installation comparison and remapping.](#the-following-terms-have-changed-and-may-need-to-be-remapped-if-previously-mapped-locally-the-ones-in-bold-will-almost-definitely-need-remapping-please-use-the-option-inquire-about-a-reminder-term-on-these-terms-for-post-installation-comparison-and-remapping)
  - [# Installation](#installation)
  - [Retrieve the PXRM\2.0\11 build](#retrieve-the-pxrm2011-build)
  - [Install the build first in a training or test account.](#install-the-build-first-in-a-training-or-test-account)
  - [Load the distribution.](#load-the-distribution)
  - [## Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
  - [Print Transport Global (optional)](#print-transport-global-optional)
  - [Install the build.](#install-the-build)
  - [Install File Print (optional)](#install-file-print-optional)
  - [Build File Print (optional)](#build-file-print-optional)
  - [Post-installation routine](#post-installation-routine)
  - [Deletion of init routines](#deletion-of-init-routines)
- [Setup and Maintenance](#setup-and-maintenance)
- [### Overview](#overview)
    - [Setup Steps](#setup-steps)
  - [Repeat the pre-installation reminder inquiry and compare the pre- and post-installation output.](#repeat-the-pre-installation-reminder-inquiry-and-compare-the-pre-and-post-installation-output)
    - [Map Local Findings to National Terms](#map-local-findings-to-national-terms)
    - [### Edit Reminder Dialogs](#edit-reminder-dialogs)
    - [### ### ### Mapping a consult quick order for the VA-TBI SCREENING reminder dialog:](#mapping-a-consult-quick-order-for-the-va-tbi-screening-reminder-dialog)
    - [Verify that the dialogs function properly](#verify-that-the-dialogs-function-properly)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [Appendix B: Setting up a TIU/HS Object for the](#appendix-b-setting-up-a-tiuhs-object-for-the)
- [AUDIT-C Test](#audit-c-test)
- [Appendix C: Computed Finding Descriptions](#appendix-c-computed-finding-descriptions)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch PXRM\*2.0\*11 includes the following modifications to the Clinical Reminders package:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Updates eleven reminder definitions (and their dialogs if there is one attached), based on changes required by the Office of Patient Care Services and problems reported in Remedy tickets. 
- Installs four new reminders.
- Installs 11 new or modified service-related computed findings.
- Updates URLs in six reminders.
- Modifies Location List exclusion functionality
- Modifies Reminder Test output
- Corrects several problems reported in Remedy tickets:

> 229723 Nat'l reminder component "PXRM AUDC RESULT has errors

> 233994 Discrepancy between VA-Iraq/Afghan Post Deploy reminder dialog and clinical maintenance display

> 242238 Duplicate text in AIMS test

> 239704 Display inconsistent for VA-IRAQ&AFGHANISTAN POST DEPLOYMENT

> 234380\. National OIF reminder is producing conflicting information in clinical maintenance vs the reminder dialog concerning section 4

> 238209 Functionality of I/A and TBI reminders

See the Setup section of this manual for instructions about mapping terms and dialogs.

### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                  |                                     |                                                                                            |
|----------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------|
| Site                         | URL                             | Description                                                                            |
| National Clinical Reminders site | <http://vista.med.va.gov/reminders> | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| VA Mental Health Home            | <http://vaww.mentalhealth.va.gov/>  | Contains items of interest for all VA mental health clinicians                             |
| VistA Document Library           | <http://www.va.gov/vdl/>            | Contains manuals for Clinical Reminders and Mental Health YS\*5.01\*85                     |

## # Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual describes how to install and set up Clinical Reminders patch PXRM\*2.0\*11.

## Required Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package/Patch</strong></td>
<td><strong>Namespace</strong></td>
<td><strong>Version</strong></td>
<td><strong>Comments</strong></td>
</tr>
<tr class="even">
<td>Clinical Reminders</td>
<td>PXRM</td>
<td>2.0</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>Health Summary</td>
<td>GMTS</td>
<td>2.7</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>HL7</td>
<td>HL</td>
<td>1.6</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td>XU</td>
<td>8.0</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>MailMan</td>
<td>XM</td>
<td>7.1</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td><p>Mental Health</p>
<p>YS*5.01*85</p></td>
<td>YS</td>
<td>5.01</td>
<td></td>
</tr>
<tr class="even">
<td><p>Pharmacy Data Management</p>
<p>PSS*1.0*112</p></td>
<td>PSS</td>
<td>1.0</td>
<td></td>
</tr>
<tr class="odd">
<td><p>Outpatient Pharmacy</p>
<p>PSO*7.0*245</p></td>
<td>PSO</td>
<td>7.0</td>
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

## ## Estimated Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                         |                                                                                         |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Setup before installation                                                               | Approximately 30 minutes                                                                |
| Installation                                                                            | About 5-10 minutes                                                                      |
| Setup after installation by the Reminder Manager or CAC to address local implementation | Approximately one hour (depending partly on the experience level of the manager or CAC) |

## ## Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1. Do a reminder definition inquiry on the following reminders and save for post-installation comparisons:

> VA-ALCOHOL AUDIT-C POSITIVE F/U

> VA-ALCOHOL USE SCREEN (AUDIT-C)

> VA-BL DEPRESSION SCREEN

> VA-BL PTSD SCREEN

> VA-BL OEF/OIF FEVER

> VA-BL OEF/OIF GI SX

> VA-BL OEF/OIF SKIN SX

> VA-DEPRESSION SCREENING

> VA-IRAQ & AFGHAN POST-DEPLOY SCREEN

> VA-MHV CERVICAL CANCER SCREEN

> VA-MHV COLORECTAL CANCER SCREEN

> VA-MHV DIABETES FOOT EXAM

> VA-MHV DIABETES RETINAL EXAM

> VA-MHV HYPERTENSION

> VA-MHV INFLUENZA VACCINE

> VA-MHV MAMMOGRAM SCREENING

> VA-MHV PNEUMOVAX

> VA-PTSD SCREENING

> VA-TBI SCREENING

## Do a reminder term inquiry and save for post-installation comparisons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## > The following terms have changed and may need to be remapped, if previously mapped locally. The ones in bold will almost definitely need remapping. Please use the option, “Inquire about a reminder term” on these terms for post-installation comparison and remapping.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA-COGNITIVE IMPAIRMENT

> VA-DEPRESSION SCREEN OEF/OIF

> VA-LDL

> VA-MHV BARIUM ENEMA

> VA-MHV COLONOSCOPY

> VA-MHV DIABETIC FOOT EXAM COMPLETE

> VA-MHV DIABETIC FOOT EXAM INSPECTION

> VA-MHV DIABETIC FOOT EXAM MONOFILAMENT

> VA-MHV DIABETIC FOOT EXAM PULSES

> VA-MHV HBA1C \<8.0

> VA-MHV HBA1C \>7.9

> VA-MHV HBA1C ALL RESULTS

> VA-MHV HDL – lab test and outside lab test

> VA-MHV INFLUENZA IMMUNIZATION

> VA-MHV LIPID PANEL ORDERABLE ITEMS

> VA-MHV OCCULT BLOOD PANEL

> VA-MHV OCCULT BLOOD SINGLE TEST

> VA-MHV OUTSIDE LDL

> VA-MHV OUTSIDE LDL\>99

> VA-MHV PNEUMOCOCCAL IMMUNIZATION

> VA-MHV SIGMOIDOSCOPY

> VA-MHV TOTAL CHOLESTEROL

> VA-MHV TRIGLYCERIDES

> VA-PTSD SCREEN

> VA-WH HYSTERECTOMY W/CERVIX REMOVED

> VA-WH MAMMOGRAM ORDER

> VA-WH MAMMOGRAM SCREEN DEFER

> VA-WH MAMMOGRAM SCREEN DONE

> VA-WH MAMMOGRAM SCREEN NOT INDICATED

> VA-WH PAP SMEAR DONE

> VA-WH PAP SMEAR OBTAINED

> VA-WH PAP SMEAR ORDER HEALTH FACTOR

> VA-WH PAP SMEAR SCREEN NOT INDICATED

3. Create an Audit-C TIU/HS Object for the VA-Alcohol Use Screen Reminder (see instructions in <u>[Appendix B](#appendix-b-setting-up-a-tiuhs-object-for-the).</u>4. The reminder dialog element VA-PDIQ POLYTRAUMA CONSULT, which is used to order a TBI consult, is overwritten in the install. You will need to re-enter the finding item for this element using the menu or quick order that you use to order a TBI consult.

## # Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This build can be installed with users on the system, but it should be done during non-peak hours.

*The installation needs to be done by a person with DUZ(0) set to "@."*

## Retrieve the PXRM\*2.0\*11 build 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use ftp to access the build – the name of the host file is PXRM_2_0_11.KID – from one of the following locations:

> Albany <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Salt Lake City <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

## Install the build first in a training or test account. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and PXRM_2_0_11.KID at the Host File prompt.

Example

> Select Installation Option: LOAD a Distribution

> Enter a Host File: PXRM_2_0_11.KID

> KIDS Distribution saved on June 14, 2008@11:53:53

> Comment: PXRM\*2.0\*11

From the Installation menu, you may elect to use the following options:

## ## Backup a Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

## Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

## Verify Checksums in Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

## Print Transport Global (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view the components of the KIDS build.

## Install the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*11 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: PXRM\*2.0\*11

Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE:DO NOT QUEUE THE INSTALLATION, because this installation may ask questions requiring responses and queuing will stop the installation. The most common are replacements for finding items or quick orders during the installation of Reminder Exchange file entries.

> The reminder dialog element VA-PDIQ POLYTRAUMA CONSULT, which is used to order a TBI consult, is overwritten in the install. You will need to re-enter the finding item for this element using the menu, order dialog, or quick order that you use to order a TBI consult.  
> Installation Example

See [Appendix A](#appendix-a-installation-example).

Setting up programmer environment

Terminal Type set to: C-VT220

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System menu

Select Kernel Installation & Distribution System Option: Installation

Select Installation Option: Install Package(s) \[XPD INSTALL BUILD\]

Select INSTALL NAME: PXRM\*2.0\*11

## Install File Print (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process.

> Select Utilities Option: Install File Print

> Select INSTALL NAME: PXRM\*2.0\*11

## Build File Print (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print

> Select BUILD NAME: PXRM\*2.0\*11 CLINICAL REMINDERS

> DEVICE: HOME//

## Post-installation routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The installation will place the following exchange file entries in the Reminder Exchange file \#811.8:

> PATCH 11 ITEMS

> VA-ALCOHOL AUDIT-C POSITIVE F/U

> VA-ALCOHOL USE SCREEN (AUDIT-C

> VA-BL DEPRESSION SCREEN

> VA-BL PTSD SCREEN

> VA-BL OEF/OIF EMBEDDED FRAGMENTS

> VA-BL OEF/OIF FEVER

> VA-BL OEF/OIF GI SX

> VA-BL OEF/OIF SKIN SX

> VA-CV ELIG W/HF FOR NO SERVICE

> VA-CV INELG W/HF FOR SERVICE

> VA-DEPRESSION SCREENING

> VA-IRAQ & AFGHAN POST-DEPLOY SCREEN

> VA-MHV CERVICAL CANCER SCREEN

> VA-MHV COLORECTAL CANCER SCREEN

> VA-MHV DIABETES FOOT EXAM

> VA-MHV DIABETES RETINAL EXAM

> VA-MHV HYPERTENSION

> VA-MHV INFLUENZA VACCINE

> VA-MHV MAMMOGRAM SCREENING

> VA-MHV PNEUMOVAX

> VA-OEF/OIF MONITOR REPORTING

> VA-PTSD SCREENING

> VA-TBI SCREENING

> The post-init will install all the components of these Exchange file entries on your system. After the installation has finished, if you discover that any of these components weren’t installed correctly, you can use the Reminder Exchange option on the Reminders Manager Menu to install them.

## Deletion of init routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After everything has been successfully installed you may delete the following init routines: PXRMP11I, PXRMP11E

# Setup and Maintenance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PXRM\*2.0\*11 includes the following additions and modifications:

- New and modified national reminder definitions and dialogs
  - New reminders to help clerks reconcile HEC data and self-reported VA-IRAQ/AFGHAN SERVICE health factor
  - New national reminder for the monitor
- New and modified computed findings
- Modified Location List exclusion functionality
- Modified Reminder Test output
- Fixes to My HealtheVet reminders function finding pointers

New Reminder Definitions

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>VA-BL OEF/OIF EMBEDDED FRAGMENTS</th>
<th>New reminder for branching logic in the new 4<sup>th</sup> question in the last section of the OEF/OIF reminder. Used for branching logic to indicate in the reminder dialog that an item is already completed or not needed.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>VA-CV ELIG W/HF FOR NO SERVICE</p>
<p>VA-CV INELG W/HF FOR SERVICE</p></td>
<td><p>These two reminders are designed to aid sites in identifying patients whose combat veteran eligibility data and data collected from the OEF/OIF Screening reminder are not in agreement.</p>
<p>Reminder patient list functionality can be used to identify patients needing reconciliation</p></td>
</tr>
<tr class="even">
<td>VA-OEF/OIF MONITOR REPORTING</td>
<td>New reminder for reporting this monitor. Excludes non-combat vets from the denominator; requires two visits after discharge separation.</td>
</tr>
</tbody>
</table>

> Modified national reminder definitions

- VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL
- VA-ALCOHOL USE SCREEN (AUDIT-C)
- VA-BL OEF/OIF FEVER
- VA-BL OEF/OIF GI SX
- VA-BL OEF/OIF SKIN SX
- VA-DEPRESSION SCREENING
- VA-IRAQ & AFGHANISTAN POST DEPLOYMENT SCREEN
- VA-MHV COLORECTAL CANCER SCREEN
- VA-MHV HYPERTENSION
- VA-MHV DIABETES RETINAL EXAM
- VA-PTSD SCREENING
- VA-TBI SCREENING

New and modified Service-related Computed Findings

- VA-AGENT ORANGE EXPOSURE 
- VA-COMBAT SERVICE 
- VA-COMBAT VET ELIGIBILITY 
- VA-LAST SERVICE SEPARATION DATE  (modified)
- VA-OEF SERVICE
- VA-OIF SERVICE
- VA-POW
- VA-PURPLE HEART 
- VA-SERVICE BRANCH 
- VA-UNKNOWN OEF/OIF SERVICE
- VA-VETERAN (modified)

Modified Location List exclusion functionality

- Exclusion location list can be defined once
- Any location lists can reference the pre-defined Exclusion location list

Modified My HealtheVet Reminders

- Updated URLs:

> VA-MHV CERVICAL CANCER SCREEN

> VA-MHV DIABETES FOOT EXAM

> VA-MHV DIABETES RETINAL EXAM

> VA-MHV HYPERTENSION

> VA-MHV INFLUENZA VACCINE

> VA-MHV MAMMOGRAM SCREENING

- VA-MHV COLORECTAL CANCER SCREEN

Added reminder term for barium enema

- VA-MHV DIABETES RETINAL EXAM

> Updated to use only prior exam as indication of frequency of exams instead of HbA1c level and use of insulin.

- VA-MHV HYPERTENSION

Converted findings to national reminder terms.

- VA-MHV INFLUENZA VACCINE

Updated the date to August 2008

- VA-MHV PNEUMOVAX

The reminder term VA-MHV HIGH RISK FOR PNEUMONIA was made national.

> Dialog Updates

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>VA-DEPRESSION SCREEN</th>
<th>PHQ-9 not required; MH test in dialog set to ‘2’ – required if opened; informational text for dialog edited to remove PHQ-9</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA-PTSD SCREENING</td>
<td><ul>
<li><p>MH test in dialog set to ‘2’ – required if opened</p></li>
<li><p>Added Acute Illness to dialog</p></li>
</ul></td>
</tr>
<tr class="even">
<td>VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN</td>
<td><ul>
<li><p>Added cognitive impairment</p></li>
<li><p>Added done elsewhere</p></li>
<li><p>Doesn’t ask the “Did you serve…? “ question if combat vet eligible</p></li>
<li><p>Substituted Q4D – asks about embedded fragments</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Setup Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Repeat the pre-installation reminder inquiry and compare the pre- and post-installation output. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following reminder definitions have been changed. These may require remapping.  The ones in red may require remapping as well as a check of the dialog for any orders that need to be re-linked. 

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Reminder</strong></th>
<th><strong>Change</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL</td>
<td>Fixed branching logic</td>
</tr>
<tr class="even">
<td>VA-ALCOHOL USE SCREEN (AUDIT-C)</td>
<td><p>Changes to dialog.</p>
<p>Removed date from term and moved to the health factor for “No alcohol in the past 1 year”</p></td>
</tr>
<tr class="odd">
<td>VA-BL OEF/OIF FEVER</td>
<td>Fixed logic</td>
</tr>
<tr class="even">
<td>VA-BL OEF/OIF GI SX</td>
<td>Fixed logic</td>
</tr>
<tr class="odd">
<td>VA-BL OEF/OIF SKIN SX</td>
<td>Fixed logic</td>
</tr>
<tr class="even">
<td>VA-DEPRESSION SCREENING</td>
<td>Changes to terms and dialog; verify/report any changes</td>
</tr>
<tr class="odd">
<td>VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN</td>
<td><p>Multiple changes:</p>
<ul>
<li><p>Added Combat Vet to logic</p></li>
<li><p>Excluded those who did not serve from denominator</p></li>
<li><p>Added cognitive impairment to exclusions</p></li>
<li><p>Added done elsewhere to resolutions</p></li>
<li><p>Updated dates of health factors for depression/PTSD to 10/1/08</p></li>
</ul></td>
</tr>
<tr class="even">
<td>VA-MHV COLORECTAL CANCER SCREEN</td>
<td>VA-MHV BARIUM ENEMA added</td>
</tr>
<tr class="odd">
<td>VA-MHV HYPERTENSION</td>
<td>Uses reminder terms</td>
</tr>
<tr class="even">
<td>VA-MHV DIABETES RETINAL EXAM</td>
<td>Frequency depends on no retinopathy only</td>
</tr>
<tr class="odd">
<td>VA-PTSD SCREENING</td>
<td><p>Added veteran status</p>
<p>Added Acute Illness to the dialog</p></td>
</tr>
<tr class="even">
<td>VA-TBI SCREENING</td>
<td>Two new Finding Items were added: VA-COMBAT VET and (FI10) VA-COGNITIVE IMPAIRMENT, and a change in the Cohort and Resolution logic</td>
</tr>
</tbody>
</table>

### Map Local Findings to National Terms 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following terms have changed and may need to be remapped, if previously mapped locally:

> The ones in bold will almost definitely need remapping.

| Term                                       | Mapping                                                                                                           |     |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----|
| VA-COGNITIVE IMPAIRMENT                        |                                                                                                                       |     |
| VA-DEPRESSION SCREEN OEF/OIF               |                                                                                                                       |     |
| VA-LDL                                     | All local lab tests for LDL                                                                                       |     |
| VA-MHV BARIUM ENEMA                        | Add outside BE                                                                                                    |     |
| VA-MHV COLONOSCOPY                         | Add outside colonoscopies or other HFs                                                                            |     |
| VA-MHV DIABETIC FOOT EXAM COMPLETE         | All 3 components completed                                                                                        |     |
| VA-MHV DIABETIC FOOT EXAM INSPECTION       | Local exams and/or HFs                                                                                            |     |
| VA-MHV DIABETIC FOOT EXAM MONOFILAMENT     | Local exams and/or HFs                                                                                            |     |
| VA-MHV DIABETIC FOOT EXAM PULSES           | Local exams and/or HFs                                                                                            |     |
| VA-MHV HBA1C \<8.0                         | Local labs with condition I +V\<8and outside HFs                                                                  |     |
| VA-MHV HBA1C \>7.9                         |                                                                                                                       |     |
| VA-MHV HBA1C ALL RESULTS                   |                                                                                                                       |     |
| VA-MHV HDL – lab test and outside lab test |                                                                                                                       |     |
| VA-MHV INFLUENZA IMMUNIZATION                  | Two national entries are included                                                                                     |     |
| VA-MHV LIPID PANEL ORDERABLE ITEMS         |                                                                                                                       |     |
| VA-MHV OCCULT BLOOD PANEL                  | Lab test for panel                                                                                                |     |
| VA-MHV OCCULT BLOOD SINGLE TEST            | Lab test for individual tests in the occult blood panel e.g. occult blood \#1, occult blood \#2, occult blood \#3 |     |
| VA-MHV OUTSIDE LDL                             | Local HFs for outside LDLs, national HFs are included                                                                 |     |
| VA-MHV OUTSIDE LDL\>99                         | Outside HFs, national HFs are included                                                                                |     |
| VA-MHV PNEUMOCOCCAL IMMUNIZATION               | National entry is included                                                                                            |     |
| VA-MHV SIGMOIDOSCOPY                       | Outside sigmoidoscopies or other HFs                                                                              |     |
| VA-MHV TOTAL CHOLESTEROL                   | Local labs and outside HFs                                                                                        |     |
| VA-MHV TRIGLYCERIDES                       | Local labs and outside HFs                                                                                        |     |
| VA-PTSD SCREEN                                 |                                                                                                                       |     |
| VA-WH HYSTERECTOMY W/CERVIX REMOVED            | Includes taxonomy and national HF                                                                                     |     |
| VA-WH MAMMOGRAM ORDER                          | Orderable item and HF included, add local HFs or orders                                                               |     |
| VA-WH MAMMOGRAM SCREEN DEFER                   | Two national HFs included                                                                                             |     |
| VA-WH MAMMOGRAM SCREEN DONE                    | Taxonomies and national HF included, add any local HFs                                                                |     |
| VA-WH MAMMOGRAM SCREEN NOT INDICATED           | Includes terminal cancer and limited life expectancy, add local HFs for limited life expectancy                       |     |
| VA-WH PAP SMEAR DONE                           | Includes taxonomy and national HF                                                                                     |     |
| VA-WH PAP SMEAR OBTAINED                       | Includes national taxonomy                                                                                            |     |
| VA-WH PAP SMEAR ORDER HEALTH FACTOR            | Already contains four national HFs                                                                                    |     |
| VA-WH PAP SMEAR SCREEN NOT INDICATED           | Limited life expectancy and terminal cancer taxonomy, add local HFs for limited life expectancy                       |     |

Example: Mapping a Local Health Factor Finding to the National Reminder Term

Select Reminder Term Management Option: te Add/Edit Reminder Term

Select Reminder Term: VA-ALCOHOL USE SCREEN NATIONAL

...OK? Yes// (Yes)

Select FINDING ITEM: 10-Question Audit

Searching for a MENTAL HEALTH INSTRUMENT, (pointed-to by FINDING ITEM)

Searching for a MENTAL HEALTH INSTRUMENT

TENS

...OK? Yes// (Yes)

Are you adding 'TENS' as a new FINDINGS (the 6TH for this REMINDER TERM)? No//

Y (Yes)

Editing Finding Number: 6 FINDING ITEM: 10-Question Audit

EFFECTIVE PERIOD:

USE INACTIVE PROBLEMS:

WITHIN CATEGORY RANK:

EFFECTIVE DATE:

MH SCALE:

CONDITION:

CONDITION CASE SENSITIVE:

RX TYPE:

Select FINDING ITEM:

### ### Edit Reminder Dialogs 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Several Dialog Elements may need to be remapped after patch 11 is installed. For example, the reminder dialog element VA-PDIQ POLYTRAUMA CONSULT, which is used to order a TBI consult, is overwritten in the install. You will need to re-enter the finding item for this element using the menu or quick order that you use to order a TBI consult. VA-GP ALC SCREEN POS REFERRAL and TBI OI CONSULT FOR KNOWN TBI are also overwritten.

> The objects in the element TXT ALC LABS & VS, in the VA-GP ALC AUDIT \>7 (added after Patch 6 was installed) will also need to be remapped.

> Check the dialogs for any orders that need to be re-linked for the following:

- VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL
- VA-ALCOHOL USE SCREEN (AUDIT-C)
- VA-BL DEPRESSION SCREENING 
- VA-IRAQ & AFGHAN POST-DEPLOY SCREEN
- VA-IRAQ/AFGHAN SERVICE
- VA-MHV HIGH RISK FOR PNEUMONIA
- VA-MHV INFLUENZA IMMUNIZATION
- VA-PTSD SCREENING

Steps to add or edit dialog elements:

> a\. Select Dialog management (DM) from the Reminders Manager Menu, then select Dialog (DI):

> Select Reminder Managers Menu Option: DM Reminder Dialog Management

> DP Dialog Parameters ...

> DI Reminder Dialogs

> Select Reminder Dialog Management Option: DI Reminder Dialogs

> <u>Dialog List Aug 30, 2007@09:55:38 Page: 1 of 8</u>

> REMINDER VIEW (ALL REMINDERS BY NAME)

> <u>Item Reminder Name Linked Dialog Name & Dialog Status</u>

> 1 AGETEST AGETEST Disabled

> 7 ALCOHOL USE SCREEN ALCOHOL USE SCREEN DIALOG

> 3 HIV HEPATITIS A SEROLOGIC TESTING HIV HEPATITIS A SEROLOGIC T

> 4 HYPERTENSION HYPERTENSION GROUP Disabled

> 5 Hypertension Screen (VHACHS) Hypertension Screen (local)

> + Enter ?? for more actions \>\>\>

> AR All reminders LR Linked Reminders QU Quit

> CV Change View RN Name/Print Name

> Select Item: Next Screen//

> b\. Use the Change View (CV) action to see the Dialog Elements view.

> Select Item: Next Screen// CV

> Select one of the following:

> D Reminder Dialogs

> E Dialog Elements

> F Forced Values

> G Dialog Groups

> P Additional Prompts

> R Reminders

> RG Result Group (Mental Health)

> RE Result Element (Mental Health)

> TYPE OF VIEW: R// E Dialog Elements

> <u>Dialog List Sep 04, 2007@10:36 Page: 1 of 120</u>

> DIALOG VIEW (DIALOG ELEMENTS)

> <u>Item Dialog Name Dialog type Status</u>

> 1 04 AUDIT-C Dialog Element

> 2 ABILITY FAIR (SLC) Dialog Element

> 3 ABILITY FAIR 1 Dialog Element

> 4 ABILITY GOOD Dialog Element

> 5 ABILITY POOR Dialog Element

> 6 ADD'L INFO Dialog Element

> 7 ADDITIONAL COMMENTS (PXRM COMMENT) Dialog Element

> 8 ADDITIONAL COMMENTS(2 LINES WP) Dialog Element

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

> AD Add CV Change View INQ Inquiry/Print

> CO Copy Dialog PT List/Print All QU Quit

> Select Item: Next Screen//

> c\. Use the Search List (SL) action to get to the dialog element you want the edit.

> Select Item: Next Screen// SL SL

> Search for: VA-HF DEP

> ...searching for 'VA-HF DEP'............

> e\. Make edits, as needed, by entering the dialog element number.

> Find Next 'VA-HF DEP'? Yes// NO

> <u>Dialog List Sep 04, 2007@10:25:40 Page: 77 of 120</u>

> DIALOG VIEW (DIALOG ELEMENTS)

> <u>+Item Dialog Name Dialog type Status</u>

> 1232 VA-HF DEP 2 QUESTION NEG Dialog Element

> 1233 VA-HF DEP 2 QUESTION POS Dialog Element

> 1234 VA-HF DEP ACUTE ILLNESS Dialog Element

> 1235 VA-HF DEP ACUTE MED CONDITION Dialog Element

> 1236 VA-HF DEP CHRONIC MED CONDITION Dialog Element

> 1237 VA-HF DEP REFERRAL TO MHC Dialog Element

> 1238 VA-HF DEP TO BE MANAGED IN PC Dialog Element

> 1239 VA-HF DEP TO BE MANAGED IN PC (2) Dialog Element

> 1240 VA-HF ETOH ADVISE NEGOTIATED LEVEL Dialog Element

> 1241 VA-HF ETOH ADVISE PT RESPONSE NO CHANGE Dialog Element

> 1242 VA-HF ETOH ADVISE PT RESPONSE WILL PLAN Dialog Element

> 1243 VA-HF ETOH DSM IV CONTINUED USE Dialog Element

> 1244 VA-HF ETOH DSM IV DRINKS LARGE AMT Dialog Element

> 1245 VA-HF ETOH DSM IV IMPAIRED CONTROL Dialog Element

> 1246 VA-HF ETOH DSM IV NEGLECT OTHER RESPONS Dialog Element

> 1247 VA-HF ETOH DSM IV TOLERANCE Dialog Element

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

> AD Add CV Change View INQ Inquiry/Print

> CO Copy Dialog PT List/Print All QU Quit

> Select Item: Next Screen// 1234

> Dialog Name: VA-HF DEP ACUTE ILLNESS

> Current dialog element/group name: VA-HF DEP ACUTE ILLNESS

> Used by: VA-GP DEP UNABLE TO SCREEN (Dialog Group)

> VA-GP PTSD UNABLE TO SCREEN (Dialog Group)

> FINDING ITEM: UNABLE TO SCREEN - ACUTE ILLNESS//

### ### ### ### Mapping a consult quick order for the VA-TBI SCREENING reminder dialog:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Type the name of the dialog element, VA-PDIQ POLYTRAUMA CONSULT <span class="mark">(or TBI OI CONSULT FOR KNOWN TBI?)</span>

> Select Item: Next Screen// SL SL

> Search for: VA-TBI OI CONSULT FOR KNOWN TBI

> ...searching for ' VA-TBI OI CONSULT FOR KNOWN TBI'............

2\. At the “Find Next” prompt, type No.

3\. Type the item number next to the element.

4\. At the finding Item Prompt, enter Q. plus the name of the site-specific Quick Order or order menu.

5\. Press Enter at the Additional Finding prompt.

### Verify that the dialogs function properly

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Test the reminder dialogs in CPRS, using either the exported dialogs or your locally created dialogs. Using point-and-click reminder resolution processing through CPRS GUI, verify the following:

- Correct Progress Note text is posted
- Finding Item gets sent to PCE
- Reminder is satisfied

> Check the Clinical Maintenance component display in CPRS after testing dialogs to ensure that all the activities are tested are reflected in the clinical maintenance display.

> *Steps to test dialogs:*

1.  On the cover sheet, click on the Reminders icon.
2.  Click on reminders in the Reminders box to see details of a reminder
3.  Open the Notes tab and select New Note. Enter a title and visit information.
4.  Open the Reminders drawer and review the contents.
5.  Locate the reminder dialog and open it.
6.  In the dialog box, check relevant actions.
7.  Finish the reminder processing.
8.  Review the text added to the note to assure its correctness.
9.  Ensure that the reminder can be satisfied by the individual finding items that were mapped to the reminder terms.
10. Check the Clinical Maintenance component display in Health Summaries and CPRS after the reminder dialog is complete.

    ![](pxrm-2-11-national-reminder-dialog-updates-install-and-setup-guide/002.png)
11. Repeat steps 5-10 for the Depression Assessment, Iraq & Afghan Post-Deployment Screen, and VA-PTSD SCREENING dialogs.

> **NOTE:** Remember to “refresh” the screen after completing a dialog, if you want to see the updated status immediately. This is especially critical if you’re doing the screening reminder and want to see the follow-up reminder become due because of positive results.

# Appendix A: Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation Option: INSTAll Package(s)

Select INSTALL NAME: PXRM\*2.0\*11 Loaded from Distribution 10/7/08@14:01:56

=\> PXRM\*2.0\*11 ;Created on Sept 26, 2008@11:08:46

It consisted of the following Install(s):

PXRM\*2.0\*11

Install Started for PXRM\*2.0\*11 :

Oct 07, 2008@05:47:49

Build Distribution Date: Sep 26, 2008

Installing Routines: Oct 07, 2008@05:47:49

Running Pre-Install Routine: PRE^PXRMP11I

DISABLE options.

DISABLE protocols.

Removing old data dictionaries.

Deleting data dictionary for file \# 810.9

Installing Data Dictionaries: Oct 07, 2008@05:47:50

Installing Data:

Oct 07, 2008@05:47:52

Running Post-Install Routine: POST^PXRMP11I

Rebuilding Function Finding internal data structures.

ENABLE options.

ENABLE protocols.

There are 25 Reminder Exchange entries to be installed.

Installing Reminder Exchange entry PATCH 11 LOCATION LIST

Installing Reminder Exchange entry VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL

Installing Reminder Exchange entry VA-ALCOHOL USE SCREEN (AUDIT-C)

Installing Reminder Exchange entry VA-BL OEF/OIF EMBEDDED FRAGMENTS

Installing Reminder Exchange entry VA-BL OEF/OIF FEVER

Installing Reminder Exchange entry VA-BL OEF/OIF GI SX

Installing Reminder Exchange entry VA-BL OEF/OIF SKIN SX

Installing Reminder Exchange entry VA-CV ELIG W/HF FOR NO SERVICE

Installing Reminder Exchange entry VA-CV INELG W/HF FOR SERVICE

Installing Reminder Exchange entry VA-DEPRESSION SCREENING

Installing Reminder Exchange entry VA-IRAQ & AFGHAN POST-DEPLOY SCREEN

Installing Reminder Exchange entry VA-MHV BMI \> 25.0

Installing Reminder Exchange entry VA-MHV CERVICAL CANCER SCREEN

Installing Reminder Exchange entry VA-MHV COLORECTAL CANCER SCREEN

Installing Reminder Exchange entry VA-MHV DIABETES FOOT EXAM

Installing Reminder Exchange entry VA-MHV DIABETES RETINAL EXAM

Installing Reminder Exchange entry VA-MHV HYPERTENSION

Installing Reminder Exchange entry VA-MHV INFLUENZA VACCINE

Installing Reminder Exchange entry VA-MHV LDL CONTROL

Installing Reminder Exchange entry VA-MHV MAMMOGRAM SCREENING

Finding RP.MAMMOGRAM UNILAT does not exist; input a replacement or ^ to quit the install.

Select RAD/NUC MED PROCEDURES NAME: MAMMOGRAPHY SCREENING (RAD Detailed) CPT:77057

Finding RP.MAMMOGRAM UNILAT does not exist; input a replacement or ^ to quit the install.

Select RAD/NUC MED PROCEDURES NAME: MAMMOGRAPHY SCREENING (RAD Detailed) CPT:77057

Installing Reminder Exchange entry VA-MHV PNEUMOVAX

Installing Reminder Exchange entry VA-OEF/OIF MONITOR REPORTING

Installing Reminder Exchange entry VA-PTSD SCREENING

Installing Reminder Exchange entry VA-TBI SCREENING

Installing Reminder Exchange entry PATCH 11 ITEMS

Removing PATCH 11 ITEMS transport reminder.

Removing PATCH 11 DIALOG transport dialog.

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*11 Installed.

Oct 07, 2008@05:51:35

Install Message sent \#xxxxxxxxxxxxxInstall Completed

# Appendix B: Setting up a TIU/HS Object for the 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# AUDIT-C Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before using the VA-Alcohol Use Screen reminder, a TIU/HS Object needs to be created to look for the last occurrence of an AUDIT-C test done on a patient. The TIU/HS Object must be named AUDIT-C for the object to work in the reminder dialog.

> **NOTE:** For some reason, Health summary doesn’t allow occurrence count or time period for MH tests, so you may need to enter these first, as follows:

The components MHAL and MHAS should have values of 'Y' for both fields \#2

\- TIME LIMITS APPLICABLE and \#4 - MAXIMUM OCCURRENCES APPLICABLE.

You can edit both those fields locally by doing the following:

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: HEALTH SUMMARY COMPONENT//

EDIT WHICH FIELD: ALL// MAXIMUM OCCURRENCES APPLICABLE

THEN EDIT FIELD:

Select HEALTH SUMMARY COMPONENT NAME: MH

1 MHA

2 MHA Administration List

3 MHA Score

4 MHV REMINDERS DETAIL DISPLAY

5 MHV REMINDERS SUMMARY DISPLAY

CHOOSE 1-5: 3 MHA Score

MAXIMUM OCCURRENCES APPLICABLE: Y yes

You can do this for both MHAL and MHAS components.

Create TIU/Health Summary Objects

To create the TIU/Object, use the menu option “Create TIU/Health Summary Objects” under the Manager Document Definition Menu on the TIU Maintenance Menu. An example of how to set this up is provided below. The bolded parts must be exact; the non-bolded parts are site preferences.

Select OPTION NAME: TIU IRM MAINTENANCE MENU TIU Maintenance Menu menu

1 TIU Parameters Menu ...

2 Document Definitions (Manager) ...

3 User Class Management ...

4 TIU Template Mgmt Functions ...

5 TIU Alert Tools

7 TIUHL7 Message Manager

Title Mapping Utilities ...

6 Active Title Cleanup Report

Select TIU Maintenance Menu Option: 2 Document Definitions (Manager)

--- Manager Document Definition Menu ---

1 Edit Document Definitions

2 Sort Document Definitions

3 Create Document Definitions

4 Create Objects

5 Create TIU/Health Summary Objects

Select Document Definitions (Manager) Option: 5 Create TIU/Health Summary Objects

TIU Health Summary Object

<u>Jul 30, 2008@12:13:19 Page: 1 of 1</u>

TIU Object Name Health Summary Type

1 BRADEN SCALE 30D VA-BRADEN SCALE 30D

2 PRESSURE ULCER VA-PRESSURE ULCER

3 PU INTERVENTIONS VA-PU INTERVENTIONS

4 TIU TPBN FUTURE APPTS TIU TPBN FUTURE APPTS

Create New TIU Object Find

Detailed Display/Edit TIU Object Detailed Display/Edit HS Object

Quit Select Action: Quit// CRE Create New TIU Object

--- Create TIU/Health Summary Object ---

Enter a New TIU OBJECT NAME: AUDIT-C this must be exact.

Object Name: AUDIT-C

Is this correct? YES// \<Enter\>

Use a pre-existing Health Summary Object? NO// \<Enter\>

Checking AUDIT-C (TIU) with Health Summary...

Creating Health Summary Object 'AUDIT-C (TIU)'

Select Health Summary Type: OB AUDC

Are you adding 'OB AUDC' as

a new HEALTH SUMMARY TYPE (the 181th)? No// YES

NAME: OB AUDC// \<Enter\>

TITLE: OB AUDC

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: \<Enter\>

SUPPRESS SENSITIVE PRINT DATA: \<Enter\>

LOCK: \<Enter\>

OWNER: // \<Enter\>

Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO

Select COMPONENT: MHAS MHA Score MHAS

SUMMARY ORDER: 5// 5

OCCURRENCE LIMIT: 1

HEADER NAME: MHA Score// \<Enter\>

No selection items chosen.

Select new items one at a time in the sequence you want them displayed.

You may select up to 99 items.

Select SELECTION ITEM: AUDC

Searching for a MH TESTS AND SURVEYS, (pointed-to by SELECTION ITEM)

Searching for a MH TESTS AND SURVEYS

1 AUDC

2 AUDCR

CHOOSE 1-2: 1 AUDC

Select SELECTION ITEM: \<Enter\>

Select COMPONENT: \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Please hold on while I resequence the summary order.

Do you want to overwrite the TIME LIMITS in the Health

Summary Type 'OB AUDC'? N//\<Enter\> O

Print standard Health Summary Header with the Object? N//\<Enter\> O

Partial Header:

Print Report Date? N// O

Print Confidentiality Banner? N// O

Print Report Header? N// O

Print the standard Component Header? Y// ES

Use report time/occurence limits? N// O

Underline Component Header? N// O

Add a Blank Line after the Component Header? N//\<Enter\> O

Print the date a patient was deceased? N//\<Enter\> O

Print a LABEL before the Health Summary Object? N//\<Enter\> O

Suppress Components without Data? N// \<Enter\>O

OBJECT DESCRIPTION:

No existing text

Edit? NO// \<Enter\>

Create a TIU Object named: AUDIT-C

Ok? YES// \<Enter\>

TIU Object created successfully.

Enter RETURN to continue...

# Appendix C: Computed Finding Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are new or modified computed findings distributed by PXRM\*2\*11:

NAME: VA-AGENT ORANGE EXPOSURE ROUTINE: PXRMMSER

ENTRY POINT: AORANGE PRINT NAME: VA-Agent Orange Exposure

TYPE: MULTIPLE

DESCRIPTION: This computed finding will be true if the patient has an agent

orange exposure registration date in the date range specified by Beginning

Date/Time and Ending Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

NAME: VA-COMBAT SERVICE ROUTINE: PXRMMSER

ENTRY POINT: COMBAT PRINT NAME: VA-Combat Service

TYPE: MULTIPLE

DESCRIPTION: This computed finding will be true if combat service is found

in the date range specified by Beginning Date/Time and Ending

Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

NAME: VA-COMBAT VET ELIGIBILITY ROUTINE: PXRMMSER

ENTRY POINT: CVELIG PRINT NAME: VA-Combat Vet Eligibility

TYPE: MULTIPLE

DESCRIPTION: This computed finding will be true if the patient qualifies as

a combat vet.

The possible values that can be used in a Condition are: "Eligible",

"Expired", and "Not eligible". An example is:

I V="Not eligible"

If the patient was eligible on the evaluation date then the Value for use in a Condition will be "Eligible". If the patient is not eligible and the

evaluation date is greater than the eligibility end date then the Value is

"Expired", otherwise the value is "Not eligible".

CLASS: NATIONAL

  
(*modified)* NAME: VA-LAST SERVICE SEPARATION DATE ROUTINE: PXRMMSER

ENTRY POINT: DISCHDT PRINT NAME: Veteran Last Separation Date

TYPE: SINGLE

DESCRIPTION: This is a single occurrence computed finding that returns the

most recent Service Separation Date for the veteran as a FileMan date. It can be used as the value in the Condition. For example: I V\>3030101.

The computed finding will be true if a separation date is found; otherwise it will be false. If the computed finding is true, the date of the finding will be the most recent Service Separation Date.

CLASS: NATIONAL SPONSOR: Office of Quality & Performance

NAME: VA-OEF SERVICE ROUTINE: PXRMMSER

ENTRY POINT: OEF PRINT NAME: VA-OEF Service

TYPE: MULTIPLE

DESCRIPTION: This multi-occurrence computed finding will search for periods

of OEF service in the date range specified by Beginning Date/Time and Ending

Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

NAME: VA-OIF SERVICE ROUTINE: PXRMMSER

ENTRY POINT: OIF PRINT NAME: VA-OIF Service

TYPE: MULTIPLE

DESCRIPTION: This multi-occurrence computed finding will search for periods

of OIF service in the date range specified by Beginning Date/Time and Ending

Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

NAME: VA-POW ROUTINE: PXRMMSER

ENTRY POINT: POW PRINT NAME: VA-POW

TYPE: MULTIPLE

DESCRIPTION: This computed finding will be true if the patient was a POW in

the date range specified by Beginning Date/Time and Ending Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

NAME: VA-PURPLE HEART ROUTINE: PXRMMSER

ENTRY POINT: PHEART PRINT NAME: VA-Purple Heart

TYPE: SINGLE

DESCRIPTION: This computed finding will be true if the patient is a Purple

Heart recipient.

There is no value for use in a Condition.

CLASS: NATIONAL

NAME: VA-SERVICE BRANCH ROUTINE: PXRMMSER

ENTRY POINT: SBRANCH PRINT NAME: VA-Service Branch

TYPE: MULTIPLE

DESCRIPTION: This computed finding will return service branch information

for a maximum of three service periods in the date range specified by

Beginning Date/Time and Ending Date/Time.

Subscripts that can be used in a Condition are:

"BRANCH"

"DISCHARGE TYPE"

"ENTRY DATE"

"SEPARATION DATE"

"SERVICE COMPONENT"

The default value is "DISCHARGE TYPE".

CLASS: NATIONAL

NAME: VA-UNKNOWN OEF/OIF SERVICE ROUTINE: PXRMMSER

ENTRY POINT: UNKOEIF PRINT NAME: VA-Unknown OEF/OIF Service

TYPE: MULTIPLE

DESCRIPTION: This multi-occurrence computed finding will search for periods of OEF/OIF service with an unknown location in the date range specified by Beginning Date/Time and Ending Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

(*modified)* NAME: VA-VETERAN ROUTINE: PXRMMSER

ENTRY POINT: VETERAN PRINT NAME: Patient is a Veteran

TYPE: SINGLE

DESCRIPTION: This single occurrence computed finding is true if the patient is a veteran and false otherwise.

There are no values that can be used in a Condition.

CLASS: NATIONAL