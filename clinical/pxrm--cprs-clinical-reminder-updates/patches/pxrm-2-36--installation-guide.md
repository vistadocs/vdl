---
title: PXRM*2*36 Pneumococcal Reminders & Women's Health Taxonomy Update Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Pneumococcal Reminders & Women's Health Taxonomy Update
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*36
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](pxrm-2-36-pneumococcal-reminders-women-s-health-taxonomy-update-installation-gui/001.png)
audience: 
keywords: 
  - contents
  - table
  - install
  - ppsv
  - pneumoc
  - installation
  - pxrm
  - reminder
  - pneumococcal
  - risk
page_count: 0
word_count: 3127
section_count: 14
table_count: 7
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: February 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_36_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_36_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-36-pneumococcal-reminders-women-s-health-taxonomy-update-installation-gui/001.png)

Pneumococcal Reminders and Women’s Health Taxonomy update

PXRM\*2.0\*36

INSTALLATION and SETUP GUIDE

February 2014

Product Development

Contents

[Pre-Installation](#_Toc9233976) 8

[Required Software for PXRM\*2\*36](#required-software-for-pxrm236) 8

[Estimated Installation Time: 10-15 minutes 8](#this-patch-can-be-installed-with-users-on-the-system-but-it-should-be-done-during-non-peak-hours.-estimated-installation-time-10-15-minutes)

[Installation](#installation) 9

[1. Retrieve the host file containing from one of the following locations](#retrieve-the-host-file-from-one-of-the-following-locations-with-the-ascii-file-type) 9

[2. Install the build first in a training or test account.](#install-the-patch-first-in-a-training-or-test-account.) 9

[3. Load the distribution.](#load-the-distribution.) 9

[4. Backup a Transport Global](#backup-a-transport-global) 10

[a. Compare Transport Global to Current System](#compare-transport-global-to-current-system) 10

[5. Install the build.](#install-the-build.) 10

[6. Install File Print](#section-4) 10

[7. Build File Print 1](#build-file-print)1

[8. Post-installation routines 1](#post-installation-routines)1

[Post-Install Set-up Instructions 1](#post-install-set-up-instructions)2

Appendix A: Installation Example 15

[Acronyms 1](#pxrm2.036-install-completed-acronyms)7

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Pre-Installation](#pre-installation)
  - [Required Software for PXRM\2\36](#required-software-for-pxrm236)
  - [## Related Documentation](#related-documentation)
    - [Web Sites](#web-sites)
  - [1\. Rename any local health factors to prevent duplicates](#1-rename-any-local-health-factors-to-prevent-duplicates)
- [Installation](#installation)
  - [This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes](#this-patch-can-be-installed-with-users-on-the-system-but-it-should-be-done-during-non-peak-hours-estimated-installation-time-10-15-minutes)
  - [Retrieve the host file from one of the following locations (with the ASCII file type):](#retrieve-the-host-file-from-one-of-the-following-locations-with-the-ascii-file-type)
  - [Install the patch first in a training or test account.](#install-the-patch-first-in-a-training-or-test-account)
  - [Load the distribution.](#load-the-distribution)
  - [## Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Install the build.](#install-the-build)
  - [## Install File Print](#install-file-print)
  - [## Build File Print](#build-file-print)
  - [Post-installation routines](#post-installation-routines)
- [Post-Install Set-up Instructions](#post-install-set-up-instructions)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)](#select-installation-test-account-option-6-install-packages)
- [Select INSTALL NAME: pxrm\2.0\36 11/15/13@08:50:05](#select-install-name-pxrm2036-111513085005)
- [=\> Pneumoccocal vaccine update ;Created on Nov 14, 2013@14:24:03](#pneumoccocal-vaccine-update-created-on-nov-14-2013142403)
- [# This Distribution was loaded on Nov 15, 2013@08:50:05 with header of](#this-distribution-was-loaded-on-nov-15-2013085005-with-header-of)
- [Pneumoccocal vaccine update ;Created on Nov 14, 2013@14:24:03](#pneumoccocal-vaccine-update-created-on-nov-14-2013142403-1)
- [It consisted of the following Install(s):](#it-consisted-of-the-following-installs)
- [PXRM\2.0\36](#pxrm2036)
- [Checking Install for Package PXRM\2.0\36](#checking-install-for-package-pxrm2036)
- [Will first run the Environment Check Routine, PXRMP36I](#will-first-run-the-environment-check-routine-pxrmp36i)
- [The environment check was successful, this build can be installed.](#the-environment-check-was-successful-this-build-can-be-installed)
- [Install Questions for PXRM\2.0\36](#install-questions-for-pxrm2036)
- [Incoming Files:](#incoming-files)
- [# REMINDER EXCHANGE (including data)](#reminder-exchange-including-data)
- [Note: You already have the 'REMINDER EXCHANGE' File.](#note-you-already-have-the-reminder-exchange-file)
- [I will OVERWRITE your data with mine.](#i-will-overwrite-your-data-with-mine)
- [Want KIDS to INHIBIT LOGONs during the install? NO//](#want-kids-to-inhibit-logons-during-the-install-no)
- [Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//](#want-to-disable-scheduled-options-menu-options-and-protocols-no)
- [Enter the Device you want to print the Install messages.](#enter-the-device-you-want-to-print-the-install-messages)
- [You can queue the install by enter a 'Q' at the device prompt.](#you-can-queue-the-install-by-enter-a-q-at-the-device-prompt)
- [Enter a '^' to abort the install.](#enter-a-to-abort-the-install)
- [DEVICE: HOME// TELNET PORT](#device-home-telnet-port)
- [Install Started for PXRM\2.0\36 :](#install-started-for-pxrm2036)
- [Nov 15, 2013@08:51:31](#nov-15-2013085131)
- [Build Distribution Date: Nov 14, 2013](#build-distribution-date-nov-14-2013)
- [Installing Routines:](#installing-routines)
- [Nov 15, 2013@08:51:31](#nov-15-2013085131-1)
- [Running Pre-Install Routine: PRE^PXRMP36I](#running-pre-install-routine-prepxrmp36i)
- [DISABLE options.](#disable-options)
- [DISABLE protocols.](#disable-protocols)
- [Checking for entries that need renamed.](#checking-for-entries-that-need-renamed)
- [Installing Data Dictionaries:](#installing-data-dictionaries)
- [Nov 15, 2013@08:51:31](#nov-15-2013085131-2)
- [Installing Data:](#installing-data)
- [Nov 15, 2013@08:51:32](#nov-15-2013085132)
- [Running Post-Install Routine: POST^PXRMP36I](#running-post-install-routine-postpxrmp36i)
- [ENABLE options.](#enable-options)
- [ENABLE protocols.](#enable-protocols)
- [There are 3 Reminder Exchange entries to be installed.](#there-are-3-reminder-exchange-entries-to-be-installed)
- [Installing Reminder Exchange entry VA-PNEUMOCOCCAL REMINDERS](#installing-reminder-exchange-entry-va-pneumococcal-reminders)
- [Installing Reminder Exchange entry PATCH 36 WH TAXONOMIES (5)](#installing-reminder-exchange-entry-patch-36-wh-taxonomies-5)
- [Installing Reminder Exchange entry VA-PATCH 36 POST COMPONENTS](#installing-reminder-exchange-entry-va-patch-36-post-components)
- [Updating Routine file...](#updating-routine-file)
- [Updating KIDS files...](#updating-kids-files)
- [PXRM\2.0\36 Installed.](#pxrm2036-installed)
- [Nov 15, 2013@08:52:33](#nov-15-2013085233)
- [Not a production UCI](#not-a-production-uci)
- [PXRM\2.0\36 Install Completed Acronyms](#pxrm2036-install-completed-acronyms)
Description:
Pneumococcal vaccine-naïve persons. ACIP recommends that adults aged \>=19
years with immunocompromising conditions, functional or anatomic asplenia,
CSF leaks, or cochlear implants, and who have not previously received PCV13
or PPSV23, should receive a dose of PCV13 first, followed by a dose of
PPSV23 at least 8 weeks later (Table). Subsequent doses of PPSV23 should
follow current PPSV23 recommendations for adults at high risk.
Specifically, a second PPSV23 dose is recommended 5 years after the first
PPSV23 dose for persons aged 19-64 years with functional or anatomic
asplenia and for persons with immunocompromising conditions. Additionally,
those who received PPSV23 before age 65 years for any indication should
receive another dose of the vaccine at age 65 years, or later if at least 5
years have elapsed since their previous PPSV23 dose.
Previous vaccination with PPSV23. Adults aged \>=19 years with
immunocompromising conditions, functional or anatomic asplenia, CSF leaks,
or cochlear implants, who previously have received \>=1 doses of PPSV23
should be given a PCV13 dose \>=1 year after the last PPSV23 dose was
received. For those who require additional doses of PPSV23, the first such
dose should be given no sooner than 8 weeks after PCV13 and at least 5
years after the most recent dose of PPSV23.
This patch does the following during installation:
1.  Installation Routine:  
    Rename PNEUMOVAX to PNEUMOVAX POLYSACCHARIDE PPSV23 (does not change the short name that displays in CPRS or on Health Summary).  
    Rename the reminder term VA-HIGH RISK FOR PNEUMOCOCCAL DZ to VA-PNEUMOC DZ RISK – HIGH
2.  Reminders:  
    LONG TERM STEROID USE (LOCAL)
VA-BL PNEUMOC RISK IMMUNOCOMPROMISED
VA-PNEUMOCOCCAL IMMUNIZATION PPSV23
VA-PNEUMOCOCCAL IMMUNIZATION PCV13
VA-MHV PNEUMOVAX
VA-BL PNEUMOC RECENT CHEMO/IMMUNOSUPPRESSION
VA-OB PNEUMOCOCCAL PRIOR VACCINATIONS
VA-OB PNEUMOCOCCAL PPSV23 INDICATIONS
VA-OB ZOSTER VACCINE DATE
VA-OB PNEUMOCOCCAL PCV13 INDICATIONS
3.  Dialogs  
    VA-PNEUMOCOCCAL IMMUNIZATION PPSV23 PNEUMOVAX  
    VA-PNEUMOCOCCAL IMMUNIZATION PCV13 PREVNAR
4.  Taxonomies  
    VA-PNEUMOC DZ RISK - HIGHEST/NOT IMMUNO COMP  
    VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED  
    VA-PNEUMOC DZ RISK - HIGH  
    VA-PNEUMOC DZ RISK - CHEMOTHERAPY (includes drug classes and drugs)
VA-CERVICAL CA/ABNORMAL PAP  
VA-MASTECTOMY  
VA-CERVICAL CANCER SCREEN  
VA-WH HYSTERECTOMY W/CERVIX REMOVED  
VA-WH PAP SMEAR SCREEN CODES
5.  Immunization: PNEUMOCOCCAL CONJUGATE PCV13  
    No mnemonic is being sent out
6.  Terms  
    STEROIDS - PNEUMOCOCCAL DZ RISK ( LOCAL)  
    VA-PNEUMOC DZ RISK - CHEMO/IMMUNOSUPP DRUGS  
    VA-PNEUMOC DZ RISK - CHEMOTHERAPY  
    VA-PNEUMOC DZ RISK - HIGH  
    VA-PNEUMOC DZ RISK - HIGHEST/NOT IMMUNO COMP  
    VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED  
    VA-PNEUMOC DZ RISK - LONG TERM STEROIDS  
    VA-PNEUMOC PCV13 CONTRAINDICATION  
    VA-PNEUMOC PCV13 DEFERRALS  
    VA-PNEUMOC PCV13 DX INCORRECT  
    VA-PNEUMOC PCV13 IMMUNIZATION  
    VA-PNEUMOC PCV13 ORDER SUPPRESSION  
    VA-PNEUMOC PCV13 ORDERS  
    VA-PNEUMOC PPSV23 CONTRAINDICATIONS  
    VA-PNEUMOC PPSV23 DEFERRALS  
    VA-PNEUMOC PPSV23 IMMUNIZATION  
    VA-PNEUMOC PPSV23 INCORRECT DIAGNOSIS  
    VA-PNEUMOC PPSV23 ORDER SUPPRESSION  
    VA-PNEUMOC PPSV23 ORDERS
How the reminders work:
1.  Only see one reminder at a time – never both
2.  Counts the number of PPSV23 doses given either by counting doses recorded or looking for a ‘SERIES’ marked as booster, 2, 3 or 4.
3.  If the PCV13 immunization is needed, then the PPSV23 is NA.
4.  If PCV13 is given, contraindicated or not indicated, then the PPSV23 reminder is applicable unless
    1.  PCV13 was given in the past 8 weeks or
    2.  The patient has already received PPSV23 and is not yet due again, or
    3.  Has a contraindication/allergy recorded.
5.  The PPSV23 reminder takes into account:
    1.  Diagnoses that would require a 2<sup>nd</sup> dose after 5 years
    2.  Age so that a dose is given after age 65
6.  If PPSV23 has been given in the past year and the patient should get PCV13, the PCV13 reminder will not come due until one year after the most recent PPSV23
7.  Logic for PPSV23:
> <span id="_Toc9233976" class="anchor"></span>Taxonomies that are used in the logic:
- IC: immunocompromised (HIV, renal failure, nephrotic syndrome, splenic dysfx, etc.
- Highest Risk= HstR: cochlear implant, CSF leak
- High Risk=HR - Other Diagnoses: (cardiac, pulmonary, smoking, liver disease)
- Chemo=CH : taxonomy and drugs
- LTS=Long term steroids
> Included in the COHORT if:
1.  (IC or HstR or CH or LTS) and either already got PCV13 but not in the past 8 weeks or has contraindication to PCV13
2.  Other dx or age\>64 and not IC/HstR/CH/LTS or has contraindication to PCV13
> Baseline frequencies
> 1\. \>65 99Y
> 2\. IC 5Y
> 3\. HstR 99Y
> 4\. HR 99Y
> 5\. LTS 5Y
> 6\. CH 5Y
> Function Findings 1,2,3,8 Frequency Rank
> 1 \<age 65 and 2 or more doses\*: 99Y 1
> 2 \>age 64 and 1 dose after age 64: 99Y 1
> 3 no dose \>64, IC/CH/LTS and no 2nd dose 5Y 2
> 8 \>age 64, IC/CH/LTS, has PCV13, no dose\>64 5Y 2
> \*2 doses are counted only if given more than 1460 days apart (4Y) or one
> is marked as a booster dose.
> For IC/CH/LTS: FF 1,2,3,8
> FF3 above can be explained this way - Patient is IC and has had a dose
> before age 65, needs a second dose 5 years later. FF(3) is true and the
> reminder is due 5Y after the recorded dose.
> If that second dose is given, then FF(1) takes over and the reminder is
> resolved (99Y).
> If the patient turns 65, then FF(8) is true and the reminder is due again
> 5Y after the last dose. Once that dose after age 65 is given, then FF(2)
> takes over and the reminder is resolved (99Y).
> Function Findings 2,4,6 Frequency Rank
> 2 \>age 64 and 1 dose after age 64: 99Y 1
> 4 \>age 64,dosed \<65, no dose\>64, not IC/CH 5Y 2
> 6 (HR or Other dx) not IC/CH and \<age 65: 99Y 3
> For <span class="mark">not</span> IC/CH/LTS: FF 6,4
> Baseline dose due for HR and HstR, FF6 sets for patients \<age 65 who are
> not IC/CH/LTS. Once they turn 65, then FF4 is applicable and the reminder
> is due 5 years after the prior dose. Once a dose is given after age 65,
> then FF2 is applicable and any dose after age 65 will resolve.
Resolution: PPSV23 or deferral or an order
> Function Findings 5, 7, 10, 16, 17, 18, 19, 20
> FF5 provides a message about the need for an additional dose after age 65
> if the patient's most recent dose was prior to age 65 for non-IC/CH/LTS
> patients.
> FF7 provides a message about the need for an additional dose after age 65
> for IC/CH/LTS patients who have already gotten PCV13.
> FF10 assesses the last 2 doses of pneumococcal vaccine to be sure that they
> were more than 4 years apart
> FF16, 17, 18 and 19 look at finding 16 and evaluate to see if it is an ICD
> code, an outpatient drug or a non-intravitreal administration of a
> chemotherapy drug.
> FF20 provides a message if PCV13 is needed. This is just in case someone
> looks at this reminder to see why it is NOT due.
> Long Term steroids is set up in a local reminder term and a local reminder in order to allow sites to modify this option. This was done since there is not a clear consensus on how to best identify these patients or to define long term steroid use and pharmacy practices in how the day’s supply is recorded may vary.
> Map local dosage formulations to the reminder term: STEROIDS - PNEUMOCOCCAL DZ RISK (see post install instructions).
> Once those are mapped, a reminder LONG TERM STEROID USE evaluates the recent fills of steroid to identify patients with long term use. This reminder defines long term use as:  
> a. any fill that is marked with a day’s supply of \>70 days  
> b. or 3 recent fills each with a day’s supply of \>21 days.
> The CDC Guidance on the amount of steroid use that causes a level of immunosuppression sufficient to warrant pneumococcal immunization is two weeks on every-day dosing of corticosteroids of at least 20 mg/day or 2 mg/kg/day. However, higher thresholds were chosen for these reminders because there were many false positives included in the reminder cohort logic when looking for shorter durations or fewer fills. Patients who received one or 2 recent tapers of steroids that were of short duration (7-14 days) were identified and included incorrectly in the cohort if only one fill was used because even though the patient got only a limited duration of steroid, the day’s supply was marked as 30 days.
> Local sites can modify this reminder or map some other entry to the term that is used in the pneumococcal reminder logic if needed. This reminder is used in the term: VA-PNEUMOC DZ RISK - LONG TERM STEROIDS.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Software for PXRM\*2\*36

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                          |               |             |               |
|--------------------------|---------------|-------------|---------------|
| Package/Patch        | Namespace | Version | Comments  |
| Clinical Reminders       | PXRM          | 2.0         | Fully patched |
| Health Summary           | GMTS          | 2.7         | Fully patched |
| Kernel                   | XU            | 8.0         | Fully patched |
| NATIONAL DRUG FILE       | PSN           | 4.0         | Fully patched |
| Pharmacy Data Management | PSS           | 1.0         | Fully patched |
| Outpatient Pharmacy      | PSO           | 7.0         | Fully patched |
| VA FileMan               | DI            | 22          | Fully patched |

## ## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                              |                             |
|------------------------------|-----------------------------|
| Documentation            | Documentation File name |
| Installation and Setup Guide | PXRM_2_0_36_IG.PDF          |

### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                       |                                                           |                                                                                            |
|---------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Site                              | URL                                                   | Description                                                                            |
| National Clinical Reminders site      | <http://vista.med.va.gov/reminders>                       | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | <http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx> | This committee directs the development of new and revised national reminders               |
| VistA Document Library                | <http://www.va.gov/vdl/>                                  | Contains manuals for Clinical Reminders and                                                |

## 1\. Rename any local health factors to prevent duplicates  
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These are the names of the HFs being exported with this patch

PNEUMOCOCCAL PCV13 DX INCORRECT

PNEUMOCOCCAL PCV13 VACCINE CONTRAIND

PNEUMOCOCCAL PCV13 VACCINE PRECAUTION

REFUSED PNEUMOC VACCINE PCV13

PNEUMOCOCCAL PPSV23 DX INCORRECT

PNEUMOCOCCAL PPSV23 VACCINE CONTRAIND

PNEUMOCOCCAL PPSV23 VACCINE PRECAUTION

REFUSED PNEUMOC VACCINE PPSV23

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*The installation needs to be done by a person with DUZ(0) set to "@."*NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.

## Retrieve the host file from one of the following locations (with the ASCII file type): 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Albany <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Salt Lake City <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

## Install the patch first in a training or test account. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name.KID at the Host File prompt.

Example

> Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

> Enter a Host File:

> KIDS Distribution saved on Oct 01, 2013@13:29:56

> Comment: Pneumococcal vaccine update

> Loading Distribution...

> Build PXRM\*2.0\*36 has an Environmental Check Routine

> <span class="mark">Want to RUN the Environment Check Routine? YES// YES</span>

> PXRM\*2.0\*36

> Will first run the Environment Check Routine, PXRMP36I

> The environment check was successful, this build can be installed.

> Use INSTALL NAME: PXRM\*2.0\*36 to install this Distribution.

From the Installation menu, you may elect to use the following options:

## ## Backup a Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

## Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

## Install the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*36 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: PXRM\*2.0\*36

Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE:DO NOT QUEUE THE INSTALLATION, because this installation asks questions requiring responses and queuing will stop the installation. A Reminders Manager or CAC should be present to respond to these.

> Installation Example

> See [Appendix A](\l).

## ## Install File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

> Select Utilities Option: Install File Print

> Select INSTALL NAME: PXRM\*2.0\*36

## ## Build File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print

> Select BUILD NAME: PXRM\*2.0\*36

> DEVICE: HOME//

## Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After successful installation, the following init routines may be deleted:

> PXRMP36E

> PXRMP36I

# Post-Install Set-up Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Mapping drug dose findings for steroids  
    Map to this term: STEROIDS - PNEUMOCOCCAL DZ RISK

Description:

Include any drug/dose that indicates a high enough steroid dose that when

given over a period of weeks/months would cause immunosuppression to a

degree that put the patient at risk for pneumococcal disease.

Example: to include steroids at a dose equivalent to 5mg of prednisone,

include at least the following.

DR.PREDNISONE 10MG TAB DR.PREDNISONE 20MG TAB

DR.PREDNISONE 50MG TAB DR.DEXAMETHASONE 2MG TAB

DR.DEXAMETHASONE 4MG TAB DR.DEXAMETHASONE 1MG TAB

DR.DEXAMETHASONE 1.5MG TAB DR.DEXAMETHASONE 0.75MG TAB

DR.PREDNISONE 5MG TAB

2.  Map your local pneumovax PPSV23 immunization types to:  
    VA-PNEUMOC PPSV23 IMMUNIZATION

Map your local Prevnar immunization types to:

VA-PNEUMOC PCV13 IMMUNIZATION

3.  Map your local orderable items for immunizations if you want the active/pending order to resolve the reminder: (optional)

VA-PNEUMOC PCV13 ORDERS  
VA-PNEUMOC PPSV23 ORDERS

4.  Map any CURRENT SMOKER health factors to:  
    VA-PNEUMOC DZ RISK – HIGH  
    Add a begin date to these health factors so that the reminder looks back only a moderate amount of time for an entry. E.g. T-1Y
5.  Map immunizations for Zoster to the term:  
    VA-ZOSTER IMMUNIZATION  
    Set BEGINNING DATE/TIME to T-28D
6.  Consider mapping the lab test eGFR into the reminder term VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED.  
    A condition should be set on this lab test. The VHA Clinical Guidance Statement includes those with Chronic Kidney Disease (CKD) of stages III-V in this cohort. We recommend that an eGFR of \<40 rather than \<60 be used since transient decreases of eGFR \<60 may occur with acute illness or use of contrast dye and not be indicative actual CKD stage III or higher.

I +V\<40!(V\["\<")&'(V="\>60")  
Set the field USE STATUS/COND IN SEARCH to YES.

7.  The order option in the dialog can be suppressed for specific user classes or for everyone using the reminder terms:  
    VA-PNEUMOC PCV13 ORDER SUPPRESSION  
    VA-PNEUMOC PPSV23 ORDER SUPPRESSION
1)  To suppress for specific user classes, in the above Terms configure the VA-ASU USER CLASS computed finding and DELETE the VA-AGE finding. NOTE: If the Age finding is not deleted, the user class settings will not work.

> VA-ASU USER CLASS

> Enter the user class in the Computed Finding Parameter field that should NOT see the option to order the pneumococcal vaccines.

> If more than one user class is needed, add additional findings of the CF

> VA-ASU USER CLASS for each one as needed.

2)  To suppress for EVERYONE, in the above TERMS DELETE the VA-ASU USER CLASS finding and edit the VA-AGE computed finding.

> VA-AGE

> To suppress the order from being seen by ANYONE, delete the Condition within the VA-AGE computed finding.

8.  If the order option is available, please attach an order dialog or an order menu to the finding items.  
    OI PNEUMOC PCV13 OUTPT SHORT  
    OI PNEUMOC PPSV23 OUTPT
9.  2 Template fields are used for Lot \#s and expiration dates. They are exported as EDIT BOXES, for free text entry. Sites may choose to change the TYPE to a COMBO box and then populate the template fields with local lot \#s and expiration dates.  
      
    IM PCV13 LOT# EXP DATE  
    IM PPSV23 LOT# EXP DATE

Changing the type is done in CPRS under Template Editor on the Notes Tab.

![](pxrm-2-36-pneumococcal-reminders-women-s-health-taxonomy-update-installation-gui/002.png)

# Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select INSTALL NAME: pxrm\*2.0\*36 11/15/13@08:50:05

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# =\> Pneumoccocal vaccine update ;Created on Nov 14, 2013@14:24:03

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # This Distribution was loaded on Nov 15, 2013@08:50:05 with header of 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Pneumoccocal vaccine update ;Created on Nov 14, 2013@14:24:03

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# It consisted of the following Install(s):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# PXRM\*2.0\*36

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Checking Install for Package PXRM\*2.0\*36

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Will first run the Environment Check Routine, PXRMP36I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# The environment check was successful, this build can be installed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Install Questions for PXRM\*2.0\*36

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Incoming Files:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # REMINDER EXCHANGE (including data)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Note: You already have the 'REMINDER EXCHANGE' File.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# I will OVERWRITE your data with mine.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Want KIDS to INHIBIT LOGONs during the install? NO// 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Enter the Device you want to print the Install messages.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# You can queue the install by enter a 'Q' at the device prompt.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Enter a '^' to abort the install.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DEVICE: HOME// TELNET PORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Install Started for PXRM\*2.0\*36 : 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Nov 15, 2013@08:51:31

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Build Distribution Date: Nov 14, 2013

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Nov 15, 2013@08:51:31

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Running Pre-Install Routine: PRE^PXRMP36I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DISABLE options.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DISABLE protocols.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Checking for entries that need renamed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Data Dictionaries: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Nov 15, 2013@08:51:31

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Data: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Nov 15, 2013@08:51:32

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Running Post-Install Routine: POST^PXRMP36I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ENABLE options.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ENABLE protocols.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# There are 3 Reminder Exchange entries to be installed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry VA-PNEUMOCOCCAL REMINDERS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry PATCH 36 WH TAXONOMIES (5) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry VA-PATCH 36 POST COMPONENTS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Updating Routine file...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Updating KIDS files...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# PXRM\*2.0\*36 Installed. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Nov 15, 2013@08:52:33

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Not a production UCI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# PXRM\*2.0\*36 Install Completed Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OIT Master Glossary is available at <http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm>

| Term       | Definition                                                      |
|------------|-----------------------------------------------------------------|
| ASU        | Authorization/Subscription Utility                              |
| Clin4      | National Customer Support team that supports Clinical Reminders |
| CPRS       | Computerized Patient Record System                              |
| DBA        | Database Administration                                         |
| DG         | Registration and Enrollment Package namespace                   |
| ESM        | Enterprise Systems Management (ESM)                             |
| FIM        | Functional Independence Measure                                 |
| GMTS       | Health Summary namespace (also HSUM)                            |
| GUI        | Graphic User Interface                                          |
| HRMH/HRMHP | High Risk Mental Health Patient                                 |
| IAB        | Initial Assessment & Briefing                                   |
| ICD-10     | International Classification of Diseases, 10th Edition          |
| ICR        | Internal Control Number                                         |
| IOC        | Initial Operating Capabilities                                  |
| LSSD       | Last Service Separation Date                                    |
| MH         | Mental Health                                                   |
| MHTC       | Mental Health Treatment Coordinator                             |
| OHI        | Office of Health Information                                    |
| OI         | Office of Information                                           |
| OIF/OEF    | Operation Iraqi Freedom/Operation Enduring Freedom              |
| OIT/OI&T   | Office of Information Technology                                |
| OMHS       | Office of Mental Health Services                                |
| ORR        | Operational Readiness Review                                    |
| PCS        | Patient Care Services                                           |
| PD         | Product Development                                             |
| PIMS       | Patient Information Management System                           |
| PMAS       | Program Management Accountability System                        |
| PTM        | Patch Tracker Message                                           |
| PXRM       | Clinical Reminder Package namespace                             |
| RSD        | Requirements Specification Document                             |
| SD         | Scheduling Package Namespace                                    |
| SQA        | Software Quality Assurance                                      |
| USR        | ASU package namespace                                           |
| VA         | Department of Veteran Affairs                                   |
| VHA        | Veterans Health Administration                                  |
| VISN       | Veterans Integrated Service Network                             |
| VistA      | Veterans Health Information System and Technology Architecture  |