---
title: PXRM*2*6 Integration with New Mental Health Package Installation and Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: patch
doc_subject: Integration with New Mental Health Package Installation and
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*6
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - reminder
  - pxrm
  - contents
  - table
  - dialog
  - install
  - finding
  - health
  - result
  - installation
page_count: 0
word_count: 7485
section_count: 43
table_count: 6
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: December 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_6_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_6_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-6-integration-with-new-mental-health-package-installation-and-setup-guide/001.png)

INTEGRATION WITH NEW MENTAL HEALTH PACKAGEPatch PXRM\*2\*6

INSTALLATION & SETUP GUIDE

December 2007

Health Provider Systems

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Contents](#contents)
- [Introduction](#introduction)
  - [NOTE: In this document you will see references to both PXRM\2\6 and PXRM\2.0\6. The difference is that PXRM\2\6 is the name of the patch and PXRM\2.0\6 is the name of the build.](#note-in-this-document-you-will-see-references-to-both-pxrm26-and-pxrm206-the-difference-is-that-pxrm26-is-the-name-of-the-patch-and-pxrm206-is-the-name-of-the-build)
  - [Updates to National Reminders](#updates-to-national-reminders)
  - [VA-Depression Screening](#va-depression-screening)
  - [PHQ-2 & PHQ-9 in the dialog](#phq-2-phq-9-in-the-dialog)
  - [VA-Iraq & Afghan Post Deploy Screen](#va-iraq-afghan-post-deploy-screen)
  - [Use all MH tests (AUDC, PHQ-2, PC PTSD)](#use-all-mh-tests-audc-phq-2-pc-ptsd)
  - [Added more detailed branching logic](#added-more-detailed-branching-logic)
  - [VA-TBI Screening](#va-tbi-screening)
  - [Fixed selection problem; added done elsewhere](#fixed-selection-problem-added-done-elsewhere)
  - [VA-MHV Influenza Vaccine](#va-mhv-influenza-vaccine)
  - [Updated date for FY08](#updated-date-for-fy08)
  - [VA-PTSD SCREENING](#va-ptsd-screening)
  - [Uses PC PTSD](#uses-pc-ptsd)
  - [VA-ALCOHOL ABUSE SCREEN (AUDIT-C)](#va-alcohol-abuse-screen-audit-c)
  - [Uses AUDIT-C for all alcohol screens](#uses-audit-c-for-all-alcohol-screens)
  - [VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL](#va-alcohol-audit-c-positive-fu-eval)
  - [Provides a standard tool for education and counseling](#provides-a-standard-tool-for-education-and-counseling)
  - [Multiple branching logic reminders](#multiple-branching-logic-reminders)
  - [## Mental Health Modifications](#mental-health-modifications)
    - [See the Release Notes (PXRM26RN.PDF) for a detailed list of all the changes included in PXRM\2\6.NOTE: In order to use all of the dialog functionality available with MHA3 and PXRM\2\6, Version 27 of the CPRS GUI will need to be installed. This version isn’t scheduled for release until later in the year.](#see-the-release-notes-pxrm26rnpdf-for-a-detailed-list-of-all-the-changes-included-in-pxrm26note-in-order-to-use-all-of-the-dialog-functionality-available-with-mha3-and-pxrm26-version-27-of-the-cprs-gui-will-need-to-be-installed-this-version-isnt-scheduled-for-release-until-later-in-the-year)
  - [Version 27 adds the ability to use a Mental Health DLL when a MH test is invoked from a reminder dialog. YSMHA.DLL is included with YS\5.01\85 and must be installed in the folder \Program Files\vista\\ Common Files on all workstations.](#version-27-adds-the-ability-to-use-a-mental-health-dll-when-a-mh-test-is-invoked-from-a-reminder-dialog-ysmhadll-is-included-with-ys50185-and-must-be-installed-in-the-folder-program-filesvista-common-files-on-all-workstations)
  - [Clinical Reminders PXRM\2\6 Documentation](#clinical-reminders-pxrm26-documentation)
    - [Web Sites](#web-sites)
  - [# Pre-Installation](#pre-installation)
  - [Required Software](#required-software)
  - [## Estimated Installation Time](#estimated-installation-time)
  - [## ## Reminder Term Update Pre-installation Information](#reminder-term-update-pre-installation-information)
  - [Updated versions of the national terms that use MH findings are being distributed with this patch. Normally, terms are merged, to preserve site mappings, but in this case, we must overwrite so that MH SCALE values and Conditions are updated. Before installing the patch, check these terms, and if your site has mapped any additional findings, you will need to re-map them after the installation.](#updated-versions-of-the-national-terms-that-use-mh-findings-are-being-distributed-with-this-patch-normally-terms-are-merged-to-preserve-site-mappings-but-in-this-case-we-must-overwrite-so-that-mh-scale-values-and-conditions-are-updated-before-installing-the-patch-check-these-terms-and-if-your-site-has-mapped-any-additional-findings-you-will-need-to-re-map-them-after-the-installation)
  - [PHQ9 and BDI2 have been added to the depression screen terms.](#phq9-and-bdi2-have-been-added-to-the-depression-screen-terms)
  - [Reminder Dialog Conversion Pre-Installation information](#reminder-dialog-conversion-pre-installation-information)
  - [During the pre-init, all result groups will be scanned and a list of local result groups that need to be mapped to an MH Test and an MH Scale will be displayed. This change is needed to support new functionality in Reminder Dialogs that generate progress note text.](#during-the-pre-init-all-result-groups-will-be-scanned-and-a-list-of-local-result-groups-that-need-to-be-mapped-to-an-mh-test-and-an-mh-scale-will-be-displayed-this-change-is-needed-to-support-new-functionality-in-reminder-dialogs-that-generate-progress-note-text)
  - [## MHA3 Installation Tips](#mha3-installation-tips)
- [Installation](#installation)
  - [Retrieve the PXRM\2.0\6 and GMTS\2.7\77 build](#retrieve-the-pxrm206-and-gmts2777-build)
  - [Install the build first in a training or test account.](#install-the-build-first-in-a-training-or-test-account)
  - [Load the distribution.](#load-the-distribution)
  - [## Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
  - [Print Transport Global (optional)](#print-transport-global-optional)
  - [Install the build.](#install-the-build)
  - [Install File Print](#install-file-print)
  - [Build File Print](#build-file-print)
  - [Post-installation routine](#post-installation-routine)
  - [Deletion of init routines](#deletion-of-init-routines)
- [Setup and Maintenance](#setup-and-maintenance)
- [### Overview](#overview)
    - [Conversion of Findings in Definitions, Terms, and Dialogs](#conversion-of-findings-in-definitions-terms-and-dialogs)
    - [Conversion of MH SCALE in Definitions and Terms](#conversion-of-mh-scale-in-definitions-and-terms)
    - [Reminder Definition Descriptions](#reminder-definition-descriptions)
    - [- VA-DEPRESSION SCREENING](#va-depression-screening-1)
    - [Setup Steps](#setup-steps)
    - [Map Local Findings to National Terms](#map-local-findings-to-national-terms)
    - [### Edit Reminder Dialogs](#edit-reminder-dialogs)
    - [### To map a consult quick order for the VA-TBI SCREENING reminder dialog:](#to-map-a-consult-quick-order-for-the-va-tbi-screening-reminder-dialog)
    - [Verify that the dialogs function properly](#verify-that-the-dialogs-function-properly)
- [Appendix A: Example of Possible Installation Messages](#appendix-a-example-of-possible-installation-messages)
- [Appendix B: Installation Example](#appendix-b-installation-example)
- [Appendix C: MHA3 and CR 6 Install Checklist](#appendix-c-mha3-and-cr-6-install-checklist)
- [Appendix D: Cross-package Tips](#appendix-d-cross-package-tips)
> [a. Backup a Transport Global [6](#backup-a-transport-global)](#backup-a-transport-global)
> [b. Compare Transport Global to Current System [6](#compare-transport-global-to-current-system)](#compare-transport-global-to-current-system)
> [c. Verify Checksums in Transport Global [6](#verify-checksums-in-transport-global)](#verify-checksums-in-transport-global)
> [d. Print Transport Global (optional) [7](#print-transport-global-optional)](#print-transport-global-optional)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## NOTE: In this document you will see references to both PXRM\*2\*6 and PXRM\*2.0\*6. The difference is that PXRM\*2\*6 is the name of the patch and PXRM\*2.0\*6 is the name of the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PXRM\*2\*6 contains modifications to integrate the Clinical Reminders package with the new version of the Mental Package called MHA3. The Clinical Reminders package will support use of new mental health surveys, instruments, and forms for clinical collection, reminder evaluation, patient list building, and reporting. These modifications are distributed at the same time as YS\*5.01\*85.

This functionality is needed so that Clinical Reminders can be used to help sites meet the Performance Measure requirements related to a standardized set of Mental Health Instruments that will be available in the YS\*5.01\*85 patch. The standardized instruments are AUDC, BDI2, PHQ-2, PHQ9, and PC-PTSD.

## Updates to National Reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-Depression Screening

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PHQ-2 & PHQ-9 in the dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-Iraq & Afghan Post Deploy Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use all MH tests (AUDC, PHQ-2, PC PTSD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Added more detailed branching logic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-TBI Screening

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Fixed selection problem; added done elsewhere 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-MHV Influenza Vaccine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Updated date for FY08

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### #### New National Reminders

## VA-PTSD SCREENING 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Uses PC PTSD 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-ALCOHOL ABUSE SCREEN (AUDIT-C) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Uses AUDIT-C for all alcohol screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Provides a standard tool for education and counseling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Multiple branching logic reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Mental Health Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To aid sites in making the conversion of Clinical Reminders to use MHA3, the post-init converts all existing mental health findings to their MHA3 equivalent and MH SCALE values to the appropriate MHA3 scale. If the field MH SCALE is null, then the score for the first scale returned by MHA3 will be displayed in the Clinical Maintenance output.

> **NOTE:** No national reminder definitions use MH findings, but those national terms that use MH findings will have correct values set for MH SCALE, and where applicable, the condition will be updated also. These terms are redistributed in patch PXRM\*2\*6.

### See the Release Notes (PXRM_2_6_RN.PDF) for a detailed list of all the changes included in PXRM\*2\*6.NOTE: In order to use all of the dialog functionality available with MHA3 and PXRM\*2\*6, Version 27 of the CPRS GUI will need to be installed. This version isn’t scheduled for release until later in the year.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Version 27 adds the ability to use a Mental Health DLL when a MH test is invoked from a reminder dialog. YS_MHA.DLL is included with YS\*5.01\*85 and must be installed in the folder \Program Files\vista\\ Common Files on all workstations.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Additional dialog features available via CPRS 27 and MH DLL:
  - Result group messages
  - Require all items in a group
  - Improved MH test required functionality
- Improves progress note text over CPRS V26 for MH tests

## Clinical Reminders PXRM\*2\*6 Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                         |                             |
|-------------------------|-----------------------------|
| Documentation       | Documentation File name |
| Release Notes           | PXRM_2_6_RN.PDF             |
| Install and Setup Guide | PXRM_2_6_IG.PDF             |
| User Manual             | PXRM_2_6_UM.PDF             |
| Manager Manual          | PXRM_2_6_MM.PDF             |

### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                  |                                        |                                                                                            |
|----------------------------------|----------------------------------------|--------------------------------------------------------------------------------------------|
| Site                         | URL                                | Description                                                                            |
| National Clinical Reminders site | <http://vista.med.va.gov/reminders>    | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| VA Mental Health Home            | <http://vaww.mentalhealth.med.va.gov/> | Contains items of interest for all VA mental health clinicians                             |
| VistA Document Library           | <http://www.va.gov/vdl/>               | Contains manuals for Clinical Reminders and Mental Health YS\*5.01\*85                     |

## # Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual describes how to install and set up Clinical Reminders patch PXRM\*2\*6 - MH Integration, and GMTS\*2.7\*77 - Mental Health Components.

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

|                                                                                         |                                                                                               |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Setup before installation                                                               | Approximately 30 minutes                                                                      |
| Installation                                                                            | About 4 minutes                                                                               |
| Setup after installation by the Reminder Manager or CAC to address local implementation | Approximately one-four hours (depending partly on the experience level of the manager or CAC) |

## ## ## Reminder Term Update Pre-installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Updated versions of the national terms that use MH findings are being distributed with this patch. Normally, terms are merged, to preserve site mappings, but in this case, we must overwrite so that MH SCALE values and Conditions are updated. Before installing the patch, check these terms, and if your site has mapped any additional findings, you will need to re-map them after the installation.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The terms are:

VA-AIM EVALUATION NEGATIVE

VA-AIM EVALUATION POSITIVE

VA-DEPRESSION SCREEN NEGATIVE

VA-DEPRESSION SCREEN POSITIVE

## PHQ9 and BDI2 have been added to the depression screen terms.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Reminder Dialog Conversion Pre-Installation information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## During the pre-init, all result groups will be scanned and a list of local result groups that need to be mapped to an MH Test and an MH Scale will be displayed. This change is needed to support new functionality in Reminder Dialogs that generate progress note text.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:

Result Group: AGP AUDC RESULT ELEMENT needs to be mapped to an MH test and scale.

Result Group: AGP BPRS SCALE 210 RG needs to be mapped to an MH test and scale.

All the National Result Groups will be re-released with PXRM\*2\*6. These have been updated to use the correct MH Test and the MH Scale.

The following new result groups will be released with PXRM\*2\*6

PXRM BRADEN RESULT GROUP

PXRM MORSE FALL RESULT GROUP

PXRM PCL RESULT GROUP

PXRM PCLM RESULT GROUP

PXRM PHQ2 RESULT GROUP

PXRM PHQ9 RESULT GROUP

PXRM PTSD RESULT GROUP

Some sites have set up a local version of PXRM PTSD RESULT GROUP and the Result Elements associated with the Result Group. We recommend that all sites review their local Result Group and Result Elements, and rename any local result groups with the same names as the one listed above to a different name.

During the pre-init, ^XTMP("PXRM PATCH 6","PXRM DCONV") will be created to store the Result Group/Element for each element. The deletion date will be set to 30 days from the date of installation. The post-init will only move national Result Groups if the MH Test assigned to the Result Group matches the MH finding item assigned to the dialog element. The result groups will be stored as the first item in the new result group sequence multiple.

*Any Local Result Groups and National Result Groups that do not pass the above check will not be moved.* A list of these Result Groups and Elements will be given in a post-init MailMan message

Example of the message:

Result Group: AUDC RESULT GROUP TEST could not be moved for the following element AIMS TEST ELEMENT.

Manual Correction is needed.

Consult Order Dialogs

VA-ALCOHOL ABUSE SCREEN (AUDIT-C)

The reminder dialog group VA-GP ALC SCREEN POS REFERRAL is for referral to substance abuse treatment or to Mental Health. At the time of install, the Reminder Dialog will use the GMRCOR CONSULT as the consult orderable item for this dialog element. Sites should substitute a quick order or order menu for ordering consults to the substance abuse treatment or to Mental Health at your facility. If no such service is available yet, you may wish to leave the GMRCOR CONSULT in the dialog element until a consult becomes available.

If your site doesn’t have GMRCOR CONSULT installed, you will be prompted during the PXRM\*2.0\*6 installation to enter an orderable item. Do not queue the install and do not enter D or Q or this dialog will not be installed.

> ADDITIONAL FINDING entry Q. does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry

> Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry

> Select ORDER DIALOG NAME: GMRCOR CONSULT (or enter your own consult dialog name)

> **NOTE:** When the VA-TBI SCREENING Reminder was released (in PXRM\*2\*8), it included the generic consult dialog (GMRCOR CONSULT) as a finding item in the dialog. Most sites probably replaced the generic consult dialog with their own order dialog or order menu. When the TBI dialog is re-installed as part of PXRM\*2\*6, the consult is re-pointed back to the generic consult that was initially released with the consult. After installation, you will need to replace GMRCOR CONSULT with your own consult dialog. See the [Dialog Edit](#DIALOGEDIT) section for instructions.

## ## MHA3 Installation Tips

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Mental Health YS\*5.01\*85 Installation Guide for details about installing this patch.

See [Appendix C](#appendix-c-mha3-and-cr-6-install-checklist) and [Appendix D](#appd) for more tips related to MHA3.

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This build can be installed with users on the system, but it should be done during non-peak hours. NOTE: PXRM\*2.0\*10 must be installed before the PXRM\*2.0\*6 and GMTS\*2.7\*77 build.*The installation needs to be done by a person with DUZ(0) set to "@."*

## Retrieve the PXRM\*2.0\*6 and GMTS\*2.7\*77 build 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use ftp to access the build, the name of the host file is PXRM_2_0_6.KID, from one of the following locations:

> Albany <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Salt Lake City <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

## Install the build first in a training or test account. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and PXRM_2_0_6.KID at the Host File prompt.

Example

> Select Installation Option: LOAD a Distribution

> Enter a Host File: PXRM_2_0_6.KID

> KIDS Distribution saved on Aug 14, 2007@11:53:53

> Comment: PXRM\*2.0\*6, GMTS\*2.7\*77

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

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*6 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: PXRM\*2.0\*6

Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE:DO NOT QUEUE THE INSTALLATION, because this installation may ask questions requiring responses and queuing will stop the installation. The most common are replacements for finding items or quick orders during the installation of Reminder Exchange file entries. This installation will most likely ask for a replacement order dialog.

Installation Example

See <u>Appendix B</u>.

Setting up programmer environment

Terminal Type set to: C-VT220

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System menu

Select Kernel Installation & Distribution System Option: Installation

Select Installation Option: Install Package(s) \[XPD INSTALL BUILD\]

Select INSTALL NAME: PXRM\*2.0\*6

## Install File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process.

> Select Utilities Option: Install File Print

> Select INSTALL NAME: PXRM\*2.0\*6

## Build File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print

> Select BUILD NAME: PXRM\*2.0\*6 CLINICAL REMINDERS

> DEVICE: HOME//

## Post-installation routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The installation will place the following exchange file entries in the Reminder Exchange file \#811.8:

> PXRM RESULT GROUP UPDATE REMINDER

> PXRM\*2\*6 TAXONOMY UPDATES

> VA-GEC REFERRAL CARE RECOMMENDATION

> VA-GEC REFERRAL NURSING ASSESSMENT

> VA-MH TERM UPDATE

> VA-WH HYSTERECTOMY W/CERVIX REMOVED

> VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL

> VA-ALCOHOL USE SCREEN (AUDIT-C)

> VA-BL ALCOHOL SCREEN

> VA-BL ALCOHOL WITHIN SAFE LIMIT

> VA-BL DEPRESSION SCREEN

> VA-BL OEF/OIF FEVER

> VA-BL OEF/OIF GI SX

> VA-BL OEF/OIF OTHER SX

> VA-BL OEF/OIF SERVICE INFO ENTERED

> VA-BL OEF/OIF SKIN SX

> VA-BL PTSD SCREEN

> VA-DEPRESSION SCREENING

> VA-IRAQ & AFGHAN POST-DEPLOY SCREEN

> VA-MHV INFLUENZA VACCINE

> VA-PTSD SCREENING

> VA-TBI SCREENING

> The post-init will install all the components of these Exchange file entries on your system. After the installation has finished, if you discover that any of these components weren’t installed correctly, you can use the Reminder Exchange option on the Reminders Manager Menu to install them.

> NOTE: Revised dialog elements and result groups/elements are distributed with PXRM\*2.0\*6 in the Reminder Exchange entry PXRM RESULT GROUP UDPATE REMINDER.

> PXRM\*2\*6 TAXONOMY UPDATES contains updated versions of VA-TETANUS DIPHTHERIA and VA-WH HYSTERECTOMY W/CERVIX REMOVED.

## Deletion of init routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After everything has been successfully installed you may delete the following init routines: PXRMP6I, PXRMP6IC, PXRMP6ID, PXRMP6IE, PXRMP6IL, PXRMP6IM, and PXRMP6IS.

# Setup and Maintenance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Conversion of Findings in Definitions, Terms, and Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The post-init for PXRM\*2.0\*6 converts all existing MH findings to their MHA3 equivalent.

### Conversion of MH SCALE in Definitions and Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The post-init for PXRM\*2.0\*6 converts all existing MH SCALE values to the appropriate MHA3 scale.

### Reminder Definition Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following Reminder Definitions are re-distributed with PXRM\*2\*6:

- VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL
- VA-ALCOHOL USE SCREEN (AUDIT-C)
- VA-DEPRESSION SCREENING
- VA-IRAQ & AFGHAN POST-DEPLOY SCREEN
- VA-MHV INFLUENZA VACCINE
- VA-PTSD SCREENING
- VA-TBI SCREENING

### - VA-DEPRESSION SCREENING

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Screening for Depression using a standard tool should be done on a yearly basis. A positive PHQ-2 triggers the need for a PHQ-9.
- A PHQ-2 or a PHQ-9 is required on all patients unless there is a recent diagnosis of depression entered for an outpatient visit. Patients with a diagnosis of depression need additional f/u and treatment.
- This reminder requires entry of the PHQ-2 into the Mental Health package after 1/1/08. The PHQ-9 must be entered in the MH package to resolve this reminder when applicable.
- Health factors for refusal, acute illness, and for chronic cognitive impairment are included in this reminder.
- A PHQ-9 should be done for any positive PHQ-2.

> This screening reminder requires one of the following in order to be resolved:

> 1\. Negative PHQ-2

> 2\. Positive PHQ-2 plus a PHQ-9 done on the same day or later than the most recent positive PHQ-2

> 3\. Refusal

- Entry of chronic cognitive impairment makes this reminder not applicable.
- Entry of acute illness or a refusal resolves the reminder for 30 days.
- Reminder terms for health factors that represent prior depression screening using the PHQ-2 and PHQ-9 are included. The PHQ-2 has been the only accepted depression screening tool since 12/1/06. Map any local health factors for the PHQ-2 to these terms. Do not include any health factors for other depression screening tools.
- The reminder term VA-CHRONIC COGNITIVE IMPAIRMENT contains a health factor and also the BOMC from the MH package. Use this health factor with caution since it turns this reminder off permanently.
- VA-PTSD SCREENING
- PTSD screening due every 5 years for all patients. The reminder is set to also be due every year for the first 5 years after the last service separation date in the patient file. This facilitates repeated screening of patients after a recent period of military service.
- The reminder is not applicable to patients who have had a diagnosis of PTSD entered in the past 1 year.
- The reminder is resolved if the patient has had:
  1.  An entry of a health factor that indicates that all four PTSD questions were answered (PTSD SCREEN NEGATIVE or PTSD SCREEN POSITIVE)
  2.  Entry of individual health factors that indicated that all 4 questions were asked and answered.
      - VA-PTSD AVOIDANCE ALL
      - VA-PTSD DETACHMENT ALL
      - VA-PTSD NIGHTMARES ALL
      - VA-PTSD ON GUARD ALL
  3.  Entry of a health factor indicating that the patient declined/refused to answer the PTSD questions (resolves the reminder for 3 months).
  4.  Entry of a PC-PTSD screen in the Mental Health package.
  - This reminder is set up to require use of the Mental Health package after 1/1/08.
  - Entry of chronic cognitive impairment makes this reminder not applicable.
  - The reminder term VA-CHRONIC COGNITIVE IMPAIRMENT contains a health factor and also the BOMC (Blessed Orientation Memory Concentration) from the MH package. Use this health factor with caution since it turns this reminder off permanently.
  - The reminder term VA-LIFE EXPECTANCY \<6 MONTHS makes the reminder NA for 6 months.
- The computed finding VA-LAST SERVICE SEPARATION DATE is included in the reminder twice: once to affect the frequency of the reminder and then a second time to provide the information on the last service separation date in the clinical maintenance display.
- VA-ALCOHOL USE SCREEN (AUDIT-C)
- Alcohol Screen Due yearly for all patients.
- The AUDIT-C is needed on all patients on a yearly basis. A reminder term is included in this reminder VA-ALCOHOL USE SCREEN to represent entries of the AUDIT-C as health factors or exams or for health factors that represent NO ALCOHOL IN THE PAST YEAR. After 1/1/08, this term is not used to resolve the reminder and the AUDIT-C tool in the MH package must be used.
- The reminder term VA-CHRONIC COGNITIVE IMPAIRMENT contains a health factor and also the BOMC from the MH package. Use this health factor with caution since it turns this reminder off permanently.
- The reminder term VA-LIFE EXPECTANCY \<6 MONTHS makes the reminder NA for 6 months.
- The reminder term VA-REFUSED ALCOHOL SCREENING resolves the reminder for 3 months.
- VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL
- This reminder is due for patient's who have a Positive Alcohol Use Screen. It becomes due with an AUDIT-C score of 5 or more.
- The dialog includes assessment tools and documentation of advice, counseling and referral.
- The reminder term VA-ALCOHOL USE INFORMATION is used for display in clinical maintenance of previously entered information.
- The reminder resolves by documentation of direct alcohol related advice and education about alcohol related medical problems. Options for further assessment and referral are also included.
- The reminder dialog group VA-GP ALC SCREEN POS REFERRAL is for referral to substance abuse treatment or to Mental Health. Enter an order dialog for a consult service or an order menu into the finding item for this dialog group.
- This reminder is intended for use by providers. This reminder is triggered by the AUDIT-C score generated from the VA-ALCOHOL USE SCREEN (AUDIT-C) clinical reminder. The dialog uses branching logic and will display different screens depending on the AUDIT-C score. A score of 8 or more will display a screen geared towards patients with a higher risk of alcohol abuse or dependence. A score of less than 8 will display a screen to guide counseling and assessment for those with a lower risk of dependence. A score of 5 in a male with specific responses to the AUDIT-C questions will trigger the question “Does the patient drink above safe limits.”
- Reminder terms that are used for the branching logic are:

VA-BL AUDIT C POSITIVE (\>=5)

VA-BL AUDIT-C \>7

VA-BL AUDC 5 SAFE LIMITS

- VA-IRAQ & AFGHAN POST-DEPLOY SCREEN
- Revisions to this reminder include:
1.  Reminder term for chronic cognitive impairment is included and resolves the reminder.
2.  The reminder term for depression screening requires a PHQ-2 or PHQ9 after 12/1/06.
3.  The PC-PTSD, PHQ-2, and PHQ-9 from the Mental Health package are included in the reminder terms.
4.  The dialog is extensively modified to allow entry of the Mental Health instruments: PHQ-2, AUDI-C and PCPTSD.
5.  The dialog branching logic is improved using reminder terms. Each reminder term contains a reminder that determines the appropriate branching:
    1.  VA-BL ALCOHOL SCREEN
    2.  VA-BL DEPRESSION SCREENING
    3.  VA-BL OEF/OIF FEVER
    4.  VA-BL OEF/OIF GI SX
    5.  VA-BL OEF/OIF OTHER SX
    6.  VA-BL OEF/OIF SKIN SX
    7.  VA-BL PTSD SCREEN

> **NOTE:** The MH instrument BDI is being discontinued. The Beck Depression Inventory is an instrument in the Mental Health Assistant that has long been used for evaluating and monitoring depression.  For several years, MHA carried both the original version (BDI) and a newer, enhanced version (BDI2).  With the release of patch YS\*5.01\*85, the BDI will be inactivated, as the BDI2 is now the preferred version of this instrument. During the pre-init, any dialog elements using BDI will be changed to use BDI2.

### Setup Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Map Local Findings to National Terms 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following terms must be remapped, if previously mapped locally:

- VA-AIM EVALUATION NEGATIVE
- VA-AIM EVALUATION POSITIVE
- VA-DEPRESSION SCREEN NEGATIVE
- VA-DEPRESSION SCREEN POSITIVE

If desired, map local Health Factors or education topics to these terms:

- VA-CHRONIC COGNITIVE IMPAIRMENT
- VA-ALCOHOL USE INFORMATION
- VA-ALCOHOL USE SCREEN
- VA-LIFE EXPECTANCY \<6 MONTHS
- VA-REFUSED ALCOHOL SCREENING

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

> Several Dialog Elements will need to be remapped after patch 6 is installed:

- TEXT ALC LABS AND VS
  - Local element for BP and alcohol related labs
- VA-PDIQ POLYTRAUMA CONSULT
  - National element for TBI consult – needs to be updated after install
- VA-GP ALC SCREEN POS REFERRAL
  - National element for MH or SATP consult – needs to be updated after install

With PXRM\*2\*6, all result groups must be mapped to an MH test and scale. The Reminder Dialog Result Group Editor has been modified to allow the Reminder Manager to assign an MH test and scale to a result group. *Any local result groups will need this mapping completed before the result group can be used in CPRS.* Once the MH test and scale have been added to a result group, the result group can be added to a dialog element. For the result group to be used with a dialog element, the MH finding item in the element must match the MH test assigned to the result group.

Once you have mapped the local findings to the national terms, you can then decide if you want to continue to use your local findings as the data elements that are captured, or if you want to use the national findings that are already mapped to the national terms.

If you want to continue to use your local findings, then be sure to edit the reminder dialog by identifying the element that allows for that data element to be collected.  Change the finding item for that element to the local finding. The national reminders and dialogs can *only* be changed by changing the finding item in the nationally distributed elements to use your local finding item instead of the nationally distributed one.

<span id="DIALOGEDIT" class="anchor"></span>NOTE: This process is also used for replacing the generic dialog consult (GMRCOR CONSULT) with a local consult.

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

> c\. Use the Search List (SL) action to get to the MH dialog elements, then enter the name of the reminder.

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

### ### To map a consult quick order for the VA-TBI SCREENING reminder dialog:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Type the name of the dialog element, VA-TBI OI CONSULT FOR KNOWN TBI

> Select Item: Next Screen// SL SL

> Search for: VA-TBI OI CONSULT FOR KNOWN TBI

> ...searching for ' VA-TBI OI CONSULT FOR KNOWN TBI'............

2\. At the “Find Next” prompt, type No.

3 Type the item number next to the element.

4\. At the finding Item Prompt, enter Q. plus the name of the site-specific

Quick Order or order menu.

5\. Press Enter at the Additional Finding prompt.

### Verify that the dialogs function properly

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Test the MH Reminder dialogs in CPRS, using either the exported dialogs or your locally created dialogs. Using point-and-click reminder resolution processing through CPRS GUI, verify the following:

- Correct Progress Note text is posted
- Finding Item gets sent to PCE
- Reminder is satisfied

> Check the Clinical Maintenance component display in CPRS after testing dialogs to ensure that all the activities are tested are reflected in the clinical maintenance display.

> *Steps to test dialogs:*

1.  On the cover sheet, click on the Reminders icon.
2.  Click on reminders in the Reminders box to see details of a reminder
3.  Open the Notes tab and select New Note. Enter a title and visit information.
4.  Open the Reminders drawer and review the contents.
5.  Locate the Depression Screening reminder dialog and open it.
6.  In the dialog box, check relevant actions.
7.  Finish the reminder processing.
8.  Review the text added to the note to assure its correctness.
9.  Ensure that the reminder can be satisfied by the individual finding items that were mapped to the reminder terms.
10. Check the Clinical Maintenance component display in Health Summaries and CPRS after the reminder dialog is complete.

    ![](pxrm-2-6-integration-with-new-mental-health-package-installation-and-setup-guide/002.png)
11. Repeat steps 5-10 for the Depression Assessment, Iraq & Afghan Post-Deployment Screen and AIMS dialogs.

> **NOTE:** Remember to “refresh” the screen after completing a dialog, if you want to see the updated status immediately. This is especially critical if you’re doing the screening reminder and want to see the follow-up reminder become due because of positive results.

# Appendix A: Example of Possible Installation Messages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: Dialog elements converted from BDI to BDI2 \[#19680\] 08/16/07@10:44

2 lines

From: POSTMASTER (Sender: XXX,YY) In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Dialog Elements names that were converted.

No dialog elements were converted.

Subj: Dialog Results Groups that need to be mapped to a MH Test. \[#19681\]

08/16/07@10:44 4 lines

From: POSTMASTER (Sender: XXX,YY) In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Result Group: AGP AUDC RESULT ELEMENT needs to be mapped to an MH test and scale.

Result Group: AGP BPRS SCALE 210 RG needs to be mapped to an MH test and scale.

# Appendix B: Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation Option: Install Package(s)  
Select INSTALL NAME: PXRM\*2.0\*6       Loaded from Distribution  12/12/07 @10:56  
     =\> PXRM\*2.0\*6 and GMTS\*2.7\*77  ;Created on Dec 12, 2007@10:56  
   
This Distribution was loaded on 12/12/07 @10:56 with header of  
   PXRM\*2.0\*6 and GMTS\*2.7\*77  ;Created on Dec 12, 2007@10:56  
   It consisted of the following Install(s):  
     PXRM\*2.0\*6    GMTS\*2.7\*77  
Checking Install for Package PXRM\*2.0\*6  
Will first run the Environment Check Routine, PXRMP6IM  
   
   
Install Questions for PXRM\*2.0\*6  
   
Incoming Files:  
   
   
   800       CLINICAL REMINDER PARAMETERS  
> **NOTE:** You already have the 'CLINICAL REMINDER PARAMETERS' File.  
   
   
   801.41    REMINDER DIALOG  
> **NOTE:** You already have the 'REMINDER DIALOG' File.  
   
   
   810.1     REMINDER REPORT TEMPLATE  
> **NOTE:** You already have the 'REMINDER REPORT TEMPLATE' File.  
   
   
   810.2     REMINDER EXTRACT DEFINITION  
> **NOTE:** You already have the 'REMINDER EXTRACT DEFINITION' File.  
   
   
   810.4     REMINDER LIST RULE  (including data)  
> **NOTE:** You already have the 'REMINDER LIST RULE' File.  
I will REPLACE your data with mine.  
   
   
   810.5     REMINDER PATIENT LIST  
> **NOTE:** You already have the 'REMINDER PATIENT LIST' File.  
   
   
   810.7     REMINDER EXTRACT COUNTING RULE  (Partial Definition)  
> **NOTE:** You already have the 'REMINDER EXTRACT COUNTING RULE' File.  
   
   
   810.8     REMINDER COUNTING GROUP  
> **NOTE:** You already have the 'REMINDER COUNTING GROUP' File.  
   
   
   811.5     REMINDER TERM  
> **NOTE:** You already have the 'REMINDER TERM' File.  
   
   
   811.8     REMINDER EXCHANGE  (including data)  
> **NOTE:** You already have the 'REMINDER EXCHANGE' File.  
I will OVERWRITE your data with mine.  
   
   
   811.9     REMINDER DEFINITION  
> **NOTE:** You already have the 'REMINDER DEFINITION' File.  
   
Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// NO  
   
Checking Install for Package GMTS\*2.7\*77  
   
Install Questions for GMTS\*2.7\*77  
   
Incoming Files:  
   
   
   142       HEALTH SUMMARY TYPE  (Partial Definition)  
> **NOTE:** You already have the 'HEALTH SUMMARY TYPE' File.  
   
   
Want KIDS to INHIBIT LOGONs during the install? NO// NO  
   
Enter the Device you want to print the Install messages.  
You can queue the install by enter a 'Q' at the device prompt.  
Enter a '^' to abort the install.  
   
DEVICE: HOME//   REMOTE  
   
   
   
 Install Started for PXRM\*2.0\*6 :

12/12/07 @10:59  
   
Build Distribution Date: Dec 04, 2007  
   
 Installing Routines:  
              12/12/07 @10:59  
   
 Running Pre-Install Routine: PRE^PXRMP6I  
   
DISABLE options.  
   
DISABLE protocols.  
Removing old data dictionaries.  
 Deleting data dictionary for file \# 800  
 Deleting data dictionary for file \# 801.41  
 Deleting data dictionary for file \# 810.1  
 Deleting data dictionary for file \# 810.2  
 Deleting data dictionary for file \# 810.4  
 Deleting data dictionary for file \# 810.5  
 Deleting data dictionary for file \# 810.8  
 Deleting data dictionary for file \# 811.5  
 Deleting data dictionary for file \# 811.8  
 Deleting data dictionary for file \# 811.9  
Converting Dialog Elements from BDI to BDI2.  
See Mailman message for more details.  
   
 Installing Data Dictionaries:  
              12/12/07 @10:56  
   
 Installing Data:  
              12/12/07 @10:56  
   
 Installing PACKAGE COMPONENTS:  
   
 Installing PRINT TEMPLATE  
   
 Installing INPUT TEMPLATE  
   
 Installing PROTOCOL  
  Located in the PXRM (CLINICAL REMINDERS) namespace.  
   
 Installing LIST TEMPLATE  
   
 Installing OPTION  
              12/12/07 @10:56  
   
 Running Post-Install Routine: POST^PXRMP6I  
   
Changing MH pointers in reminder definition PA-ASI SCREEN INITIAL IEN=55  
Converting finding number 2  
   
Changing MH pointers in reminder definition PA-ASI SCREEN FOLLOWUP IEN=56  
Converting finding number 2  
Converting finding number 3  
Converting finding number 5  
   
Changing MH pointers in reminder definition PA-ASI IEN=640033  
Converting finding number 1  
   
Changing MH pointers in reminder definition PA-GAF IEN=640034  
Converting finding number 1  
   
Changing MH pointers in reminder definition PA-AIMS IEN=640035  
Converting finding number 1  
   
Changing MH pointers in reminder term VA-DEPRESSION SCREEN NEGATIVE IEN=82  
Converting finding number 4  
Converting finding number 6  
Converting finding number 5  
Converting finding number 2  
Converting finding number 3  
   
Changing MH pointers in reminder term VA-DEPRESSION SCREEN POSITIVE IEN=83  
Converting finding number 4  
Converting finding number 6  
Converting finding number 5  
Converting finding number 2  
Converting finding number 3  
   
Changing MH pointers in reminder term DOQ DEPRESSION SCREEN COMPLETED IEN=86  
Converting finding number 3  
Converting finding number 2  
Converting finding number 1  
Converting finding number 7  
Converting finding number 8  
   
Changing MH pointers in reminder term VA-DEPRESSION ASSESS COMPLETED IN MHC IEN=  
99  
Converting finding number 1  
Converting finding number 3  
Converting finding number 2  
   
Changing MH pointers in reminder term VA-AIM EVALUATION NEGATIVE IEN=113  
Converting finding number 2  
   
Changing MH pointers in reminder term VA-AIM EVALUATION POSITIVE IEN=114  
Converting finding number 2  
   
Changing MH pointers in reminder term VA-ALCOHOL USE SCREEN IEN=122  
Converting finding number 1  
Converting finding number 2  
Converting finding number 5  
   
Changing MH pointers in reminder term VA-ALCOHOL SCREEN PAST 6 MONTHS IEN=568021  
Converting finding number 1  
Converting finding number 5  
   
Changing MH pointers in reminder term VA-DEPRESSION SCREEN IN PAST 6 MONTHS IEN=  
568022  
Converting finding number 7  
Converting finding number 5  
Converting finding number 6  
Converting finding number 9  
Converting finding number 8  
   
Changing MH pointers in reminder dialog MH AUDC IEN=355  
   
Changing MH pointers in reminder dialog MH CAGE IEN=356  
   
Changing MH pointers in reminder dialog MH AUDC HHS IEN=358  
   
Changing MH pointers in reminder dialog VA-MH DOMG IEN=640  
   
Changing MH pointers in reminder dialog VA-MH DOM80 IEN=820  
   
Changing MH pointers in reminder dialog VA-MH AIMS IEN=847  
   
Changing MH pointers in reminder dialog VA-MH AUDC YES IEN=1175  
   
Changing MH pointers in reminder dialog PA-MH AUDC 2007 IEN=2993  
   
Changing MH pointers in reminder dialog PA-MH DOM80 IEN=3623  
   
Changing MH pointers in reminder dialog PA-MH DOMG IEN=3624  
   
Changing MH pointers in reminder dialog APA SA PERFORM AUDC IEN=512000359  
   
Changing MH pointers in reminder dialog MH AIMS IEN=640000260  
   
Changing MH pointers in reminder dialog MH GAF IEN=640000267  
   
Converting Conditions for MH findings in definitions and terms.  
811.5 - IEN=82 FI=5 COND=I V\<10  
I +V\<10  
   
811.5 - IEN=82 FI=4 COND=I V\<10  
I +V\<10  
   
811.5 - IEN=82 FI=2 COND=I V=0  
I +V=0  
   
811.5 - IEN=82 FI=3 COND=I V\<4  
I +V\<4  
   
811.5 - IEN=82 FI=6 COND=I V\<33  
I +V\<33  
   
811.5 - IEN=83 FI=5 COND=I V\>9  
I +V\>9  
   
811.5 - IEN=83 FI=4 COND=I V\>9  
I +V\>9  
   
811.5 - IEN=83 FI=2 COND=I V=1  
I +V=1  
   
811.5 - IEN=83 FI=3 COND=I V\>3  
I +V\>3  
   
811.5 - IEN=83 FI=6 COND=I V\>32  
I +V\>32  
   
811.5 - IEN=113 FI=2 COND=I V\<7  
I +V\<7  
   
811.5 - IEN=114 FI=2 COND=I V\>6  
I +V\>6  
   
   
Converting sequences from free text to numerical.  
   
Converting sequences in file \#810.2  
^PXRM(810.2,1,10,1,0) from 001 to 1  
  ^PXRM(810.2,1,10,1,10,1,0) from 001 to 1  
  ^PXRM(810.2,1,10,1,10,2,0) from 002 to 2  
^PXRM(810.2,1,10,2,0) from 002 to 2  
  ^PXRM(810.2,1,10,2,10,1,0) from 001 to 1  
  ^PXRM(810.2,1,10,2,10,2,0) from 002 to 2  
^PXRM(810.2,1,10,3,0) from 003 to 3  
  ^PXRM(810.2,1,10,3,10,1,0) from 001 to 1  
  ^PXRM(810.2,1,10,3,10,2,0) from 002 to 2  
^PXRM(810.2,1,10,4,0) from 004 to 4  
  ^PXRM(810.2,1,10,4,10,1,0) from 001 to 1  
  ^PXRM(810.2,1,10,4,10,2,0) from 002 to 2  
^PXRM(810.2,1,10,5,0) from 005 to 5  
  ^PXRM(810.2,1,10,5,10,1,0) from 001 to 1  
  ^PXRM(810.2,1,10,5,10,2,0) from 002 to 2  
^PXRM(810.2,5,10,1,0) from 001 to 1  
  ^PXRM(810.2,5,10,1,10,1,0) from 001 to 1  
  ^PXRM(810.2,5,10,1,10,2,0) from 002 to 2  
^PXRM(810.2,5,10,2,0) from 002 to 2  
  ^PXRM(810.2,5,10,2,10,1,0) from 001 to 1  
   
Converting sequences in file \#810.4  
^PXRM(810.4,6,30,3,0) from 001 to 1  
^PXRM(810.4,6,30,4,0) from 002 to 2  
^PXRM(810.4,6,30,5,0) from 003 to 3  
^PXRM(810.4,10,30,1,0) from 001 to 1  
^PXRM(810.4,10,30,2,0) from 002 to 2  
^PXRM(810.4,12,30,1,0) from 001 to 1  
^PXRM(810.4,12,30,2,0) from 002 to 2  
^PXRM(810.4,12,30,3,0) from 003 to 3  
^PXRM(810.4,14,30,5,0) from 001 to 1  
^PXRM(810.4,14,30,6,0) from 002 to 2  
^PXRM(810.4,14,30,7,0) from 003 to 3  
^PXRM(810.4,15,30,5,0) from 001 to 1  
^PXRM(810.4,15,30,6,0) from 002 to 2  
^PXRM(810.4,15,30,7,0) from 003 to 3  
^PXRM(810.4,19,30,1,0) from 001 to 1  
^PXRM(810.4,21,30,1,0) from 001 to 1  
^PXRM(810.4,24,30,1,0) from 001 to 1  
^PXRM(810.4,26,30,1,0) from 001 to 1  
   
Converting sequences in file \#810.7  
^PXRM(810.7,1,10,1,0) from 001 to 1  
^PXRM(810.7,1,10,2,0) from 002 to 2  
^PXRM(810.7,1,10,3,0) from 003 to 3  
^PXRM(810.7,2,10,1,0) from 001 to 1  
^PXRM(810.7,2,10,2,0) from 002 to 2  
^PXRM(810.7,2,10,3,0) from 003 to 3  
^PXRM(810.7,3,10,1,0) from 001 to 1  
^PXRM(810.7,3,10,2,0) from 002 to 2  
^PXRM(810.7,7,10,1,0) from 001 to 1  
^PXRM(810.7,7,10,2,0) from 002 to 2  
^PXRM(810.7,8,10,1,0) from 001 to 1  
^PXRM(810.7,8,10,2,0) from 002 to 2  
^PXRM(810.7,8,10,3,0) from 003 to 3  
^PXRM(810.7,9,10,1,0) from 001 to 1  
^PXRM(810.7,10,10,1,0) from 001 to 1  
   
Converting sequences in file \#810.8  
^PXRM(810.8,1,10,1,0) from 001 to 1  
^PXRM(810.8,1,10,2,0) from 002 to 2  
^PXRM(810.8,2,10,1,0) from 001 to 1  
^PXRM(810.8,2,10,2,0) from 002 to 2  
^PXRM(810.8,2,10,3,0) from 003 to 3  
^PXRM(810.8,2,10,4,0) from 004 to 4  
^PXRM(810.8,2,10,5,0) from 005 to 5  
^PXRM(810.8,2,10,6,0) from 006 to 6  
^PXRM(810.8,2,10,7,0) from 007 to 7  
^PXRM(810.8,2,10,8,0) from 009 to 9  
^PXRM(810.8,2,10,9,0) from 010 to 10  
^PXRM(810.8,2,10,10,0) from 008 to 8  
^PXRM(810.8,3,10,1,0) from 001 to 1  
^PXRM(810.8,4,10,1,0) from 001 to 1  
^PXRM(810.8,4,10,2,0) from 002 to 2  
^PXRM(810.8,4,10,3,0) from 003 to 3  
^PXRM(810.8,4,10,4,0) from 004 to 4  
^PXRM(810.8,4,10,5,0) from 005 to 5  
^PXRM(810.8,4,10,6,0) from 006 to 6  
^PXRM(810.8,4,10,7,0) from 007 to 7  
^PXRM(810.8,4,10,8,0) from 008 to 8  
^PXRM(810.8,5,10,1,0) from 001 to 1  
^PXRM(810.8,5,10,2,0) from 002 to 2  
^PXRM(810.8,7,10,1,0) from 001 to 1  
^PXRM(810.8,7,10,2,0) from 002 to 2  
^PXRM(810.8,7,10,3,0) from 003 to 3  
^PXRM(810.8,7,10,4,0) from 004 to 4  
^PXRM(810.8,7,10,5,0) from 005 to 5  
^PXRM(810.8,7,10,6,0) from 006 to 6  
^PXRM(810.8,7,10,7,0) from 007 to 7  
^PXRM(810.8,7,10,8,0) from 008 to 8  
^PXRM(810.8,11,10,1,0) from 001 to 1  
^PXRM(810.8,11,10,2,0) from 002 to 2  
^PXRM(810.8,11,10,3,0) from 003 to 3  
^PXRM(810.8,12,10,1,0) from 001 to 1  
^PXRM(810.8,12,10,2,0) from 002 to 2  
^PXRM(810.8,13,10,1,0) from 001 to 1  
^PXRM(810.8,14,10,1,0) from 001 to 1  
^PXRM(810.8,14,10,2,0) from 002 to 2  
^PXRM(810.8,14,10,3,0) from 003 to 3  
^PXRM(810.8,14,10,4,0) from 004 to 4  
^PXRM(810.8,14,10,5,0) from 005 to 5  
^PXRM(810.8,14,10,6,0) from 006 to 6  
^PXRM(810.8,14,10,7,0) from 007 to 7  
^PXRM(810.8,14,10,8,0) from 008 to 8  
^PXRM(810.8,14,10,9,0) from 009 to 9  
^PXRM(810.8,15,10,1,0) from 001 to 1  
^PXRM(810.8,15,10,2,0) from 002 to 2  
^PXRM(810.8,15,10,3,0) from 003 to 3  
^PXRM(810.8,15,10,4,0) from 004 to 4  
   
ENABLE options.  
   
ENABLE protocols.  
   
Installing reminder PXRM RESULT GROUP UPDATE REMINDER  
   
Installing reminder PXRM\*2\*6 TAXONOMY UPDATES  
   
Installing reminder VA-GEC REFERRAL CARE RECOMMENDATION  
   
FINDING entry Q.GMRCT GEC does not exist.  
   
     Select one of the following:  
   
   
          D         Delete (from the reminder/dialog)  
          P         Replace (in the reminder/dialog) with an existing entry  
          Q         Quit the install  
   
Enter response: P    Replace (in the reminder/dialog) with an existing entry  
  
Select ORDER DIALOG NAME: GMRCOR CONSULT

   
Installing reminder VA-GEC REFERRAL NURSING ASSESSMENT  
   
FINDING entry Q.GMRCT GEC does not exist.  
   
     Select one of the following:  
   
   
          D         Delete (from the reminder/dialog)  
          P         Replace (in the reminder/dialog) with an existing entry  
          Q         Quit the install  
   
Enter response: P    Replace (in the reminder/dialog) with an existing entry  
  
Select ORDER DIALOG NAME: GMRCOR CONSULT

    
Installing reminder VA-MH TERM UPDATE  
   
Installing reminder VA-WH HYSTERECTOMY W/CERVIX REMOVED  
   
Installing reminder VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL  
   
FINDING entry Q.ORZ GMENU CONSULTS SUBSTANCE ABUSE does not exist.  
   
     Select one of the following:  
           D         Delete (from the reminder/dialog)  
          P         Replace (in the reminder/dialog) with an existing entry  
          Q         Quit the install  
   
Enter response: P    Replace (in the reminder/dialog) with an existing entry  
  
Select ORDER DIALOG NAME: GMRCOR CONSULT

 

   
Installing reminder VA-ALCOHOL USE SCREEN (AUDIT-C)  
   
Installing reminder VA-BL ALCOHOL SCREEN  
   
Installing reminder VA-BL ALCOHOL WITHIN SAFE LIMIT  
   
Installing reminder VA-BL DEPRESSION SCREEN  
   
Installing reminder VA-BL OEF/OIF FEVER  
   
Installing reminder VA-BL OEF/OIF GI SX  
   
Installing reminder VA-BL OEF/OIF OTHER SX  
   
Installing reminder VA-BL OEF/OIF SERVICE INFO ENTERED  
   
Installing reminder VA-BL OEF/OIF SKIN SX  
   
Installing reminder VA-BL PTSD SCREEN  
   
Installing reminder VA-DEPRESSION SCREENING  
   
Installing reminder VA-IRAQ & AFGHAN POST-DEPLOY SCREEN  
  
Installing reminder VA-MHV INFLUENZA VACCINE  
   
Installing reminder VA-PTSD SCREENING  
   
Installing reminder VA-TBI SCREENING  
  
   
   
Rebuilding taxonomy expansions.  
   
 Working on taxonomy 29  
   
 Working on taxonomy 58  
Moving Result Group to new multiple location.  
See mailman message for any error.  
Removing transport reminder and dialog for Result Groups.  
   
 Updating Routine file...  
   
 Updating KIDS files...  
   
 PXRM\*2.0\*6 Installed.  
             Dec 12, 2007 @11:08  
   
 Install Message sent \#888  
   
 Install Started for GMTS\*2.7\*77 :  
              Dec 12, 2007 @11:08  
   
Build Distribution Date: Dec 04, 2007  
   
 Installing Routines:  
              Dec 12, 2007 @11:08  
   
 Installing Data Dictionaries:  
              Dec 12, 2007 @11:08  
   
 Running Post-Install Routine: POST^GMTSP77B  
   
 Filing "MHA ADMINISTRATION LIST" component in Health Summary  
   Successfully installed new component  
   
 Adding "MHA ADMINISTRATION LIST" component to the PDX package  
   Component successfully added  
   
   
 Filing "MHA SCORE" component in Health Summary  
   Successfully installed new component  
   
 Re-Indexing Health Summary Component file ................ \< done \>  
 Re-Indexing Health Summary Type file ..................... \< done \>  
   
                                  GMTS\*2.7\*77  
--------------------------------------------------------------------------------  
 Ad Hoc Summary  
   Gathering Ad Hoc Summary information.................... \< done \>  
   Purging old Ad Hoc Summary.............................. \< done \>  
   Rebuilding Ad Hoc Summary............................... \< done \>  
   
 Ad Hoc Health Summary successfully rebuilt  
   
 Setting time and occurrence limits for GMTS HS ADHOC OPTION component  
 MHA Score (Limits - 1 year and 10 occurrences)  
   
 Updating Routine file...  
   
 Updating KIDS files...  
   
 GMTS\*2.7\*77 Installed.  
               S Dec 12, 2007 @11:11  
   
 Install Message sent \#890  
--------------------------------------------------------------------------------  
          \[------------------------------------------------------------\]  
  100%    \|             25             50             75               \|  
Complete  \[------------------------------------------------------------\]  
   
   
Install Completed

# Appendix C: MHA3 and CR 6 Install Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** See the YS\*5.01\*85 Install Guide for detailed instructions on installing and setting up this application.

YS\*5.01\*85 Install Steps

1\. Using ftp, retrieve the YS\*5.01\*85 file from an Anonymous Software directory.

2\. Use the LOAD A DISTRIBUTION option on the KIDS menu to load the Host File, YS_501_85.KID.

3\. Use KIDS to install the Transport global, YS\*5.01\*85, and proceed with the install.

4\. Place the option YS BROKER1 \[YS BROKER1\] on the Mental Health users’ secondary menus, as well as the secondary menus of all users who currently have the OR CPRS GUI CHART option.

Post-Install Steps

1\. Create a TIU Document Definition, Mental Health Diagnostic Study Note, and add it to the TIU Document Definition hierarchy using the TIU option Create Document Definitions Note. The title can be entered under the site-appropriate Document Class.

2\. Run the YS50185_SETUP_1_0_3_36.exe file (i.e., double click on it). This starts the MHA3, installation process.

3\. If the optional SecureDesktop functionality is desired, repeat steps 1 and 2 for the file named YS50185_SD_SETUP.exe. (NOTE: Secure Desktop should only be loaded on computers where patient-administered assessments will be completed; this should not be pushed out silently to all machines on network—it has caused problems when attempted). Be sure to install YS50185_SETUP_1_0_3_36.exe prior to running YS50185_SD_SETUP.exe.

4\. Set up VistA MHA3 on CPRS GUI Tools Menu.

5\. A new MH entry to the HL7 APPLICATION PARAMETER file (#771) is created with this install – YS MHA. It is exported as Inactive and should be set to Active after install.

6\. Check the new MH entry to the HL LOGICAL LINK file (#870): YS MHAT.

7\. Place the YS_MHA dll in the Common Folder (same location as vitals dll).

PXRM\*2\*6Recommended Pre-installation steps (Reminder Managers or CACs)

1\. Print or capture inquiry output for reminder definitions and reminder terms with mental health findings. 

- The following terms will override current definitions, instead of merging during the install: 
  - VA-AIM EVALUATION NEGATIVE
  - VA-AIM EVALUATION POSITIVE
  - VA-DEPRESSION SCREEN NEGATIVE
  - VA-DEPRESSION SCREEN POSITIVE
- Keep track of local mapped findings to add them back into the reminder terms after the build is successfully installed. NOTE: PHQ9 and BDI2 have been added to the depression screen terms.

2\. Use Print List (PL) action to print or capture reminder dialog, dialog group, and dialog element definitions that use Mental Health finding items. 

Installation Steps (IRMS)

1\. Using ftp, retrieve the PXRM\*2.0\*6 and GMTS\*2.7\*77 build (host file name: PXRM_2_0_6.KID) from an Anonymous Software directory.

2\. Install the build first in a training or test account.

3\. Using the KIDS menu, load the distribution.

4\. Install the build.

> **NOTE:** DO NOT QUEUE THE INSTALLATION, because this installation may contain questions requiring a response, and queuing will stop the installation. See [Appendix B](#appendix-b-installation-example), installation example.

Post-Install (CAC/Reminders Managers)

1.  Compare “before install” reminder definition inquiries to post install reminder definition inquiries. The mental health finding should still be defined after the install conversion, but will point to a new MHA3 mental health test and survey file.
2.  Re-map any local terms that were overridden by the install, using Add New Terms on the Reminder Term Management menu. A post-install message is sent to notify you of terms that were overridden. If you mapped these terms previously, you’ll have to redo local mapping:
- VA-AIM EVALUATION NEGATIVE
- VA-AIM EVALUATION POSITIVE
- VA-DEPRESSION SCREEN NEGATIVE
- VA-DEPRESSION SCREEN POSITIVE
3.  Edit Reminder dialogs. Compare pre-install reminder dialog print lists to post install reminder dialog, dialog group and dialog element definitions that use a mental health finding.
    - Patch 6 installation overrides local Consult Order Dialogs for TBI and MH or SATP consults. These must be remapped.
    - With Patch 6, all result groups must be mapped to a MH test and scale. The Reminder Dialog Result Group Editor has been modified to allow the Reminder Manager to assign an MH test and scale to a result group. *Any local result groups will need this mapping completed before the result group can be used in CPRS.* Once the MH test and scale have been added to a result group, the result group can be added to a dialog element.

<span id="_Toc184710874" class="anchor"></span>

# Appendix D: Cross-package Tips

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Add YS BROKER1 to the secondary menus of anyone who will use Reminder dialogs.

(Use the Edit User Characteristics option.)

2\. Secure Desktop

The Secure Desktop feature is used when patients complete MH tests directly on the computer. The Secure Desktop needs to be installed on individual computers because it has a feature of locking down the PC and could be problematic if placed on a server. See the MHA3 install guide for instructions

3\. Speed Tab

Speed Tab is a feature that some users may prefer to enable them to increase data entry speed. Speed Tab is actually an automatic “Tab” key press that is triggered after the user makes a choice from a question with multiple choice answers. This saves the user from having to press the Tab key to move on to subsequent questions on the form. However, the Speed Tab option has no effect on Multiple-Line Text Boxes, Single-Line Text Boxes and Spin Boxes.

If set, you can use the keyboard to enter numbers of selection items, rather than clicking each button and hitting enter

4\. BOMC (and a few other tests)

Some tests, such as BOMC, won't work in a reminder dialog until CPRS V27. Given the need to document cognitive impairment in excluding patients from some of the MH performance measures, one option to address this may be to individually place the BOMC on the Tools Menu. Instructions for how to do this can be found in the MHA3 install guide.