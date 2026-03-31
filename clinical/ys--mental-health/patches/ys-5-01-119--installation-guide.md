---
title: YS*5.01*119 Mental Health Assistant Phase 3 PCL-5 Update Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Mental Health Assistant Phase 3 PCL-5 Update Install Guide
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*119
group_key: "YS:YS:5.01"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - reminder
  - health
  - installation
  - install
  - build
  - pclc
  - pclm
  - mental
page_count: 0
word_count: 3519
section_count: 12
table_count: 1
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_pcl5_update.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_pcl5_update.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

> ![](ys-5-01-119-mental-health-assistant-phase-3-pcl-5-update-install-guide/001.png)

Mental Health PCL-5 UpdateYS_PCL5_UPDATEINSTALLATION GUIDEOctober 2016

### Product Development Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Contents</u>

[Introduction 3](#introduction)

[Installation 4](#_bookmark1)

1.  [Retrieve the host file from one of the following locations (with the ASCII file type) 4](#_bookmark2)
2.  [Install the patch first in a training or test account 4](#install-the-patch-first-in-a-training-or-test-account.)
3.  [Load the distribution. 4](#load-the-distribution.)
4.  [Backup a Transport Global 4](#backup-a-transport-global)
5.  [Compare Transport Global to Current System 4](#compare-transport-global-to-current-system)
6.  [Install the build. 5](#install-the-build.)
7.  [Install File Print (optional) 5](#install-file-print-optional)
8.  [Build File Print (optional) 5](#build-file-print-optional)
9.  [Post-installation routines 5](#post-installation-routines)

[Post-Install Set-up Instructions 6](#_bookmark11)

1.  [Find usages of PCLC and PCLM in locally developed Clinical Reminders 6](#find-usages-of-pclc-and-pclm-in-locally-developed-clinical-reminders.)
2.  [Find usages of PCLC and PCLM in Reminder Dialogs. 6](#find-usages-of-pclc-and-pclm-in-reminder-dialogs.)
3.  [Modify findings to use PCL-5. 6](#modify-findings-to-use-pcl-5.)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Product Development Department of Veterans Affairs](#product-development-department-of-veterans-affairs)
- [Introduction](#introduction)
    - [This patch releases the Posttraumatic Stress Disorder (PTSD) Checklist 5 (PCL-5) mental health instrument. This will make PCL-5 available for selection in MHA (Mental Health Assistant) application. The previous versions of PTSD checklists, PCL-C and PCL-M are inactivated with this patch. Nationally released Clinical Reminders and Reminder Dialogs that made use of PCL- C as a mental health finding are also updated to use PCL-5. These include:](#this-patch-releases-the-posttraumatic-stress-disorder-ptsd-checklist-5-pcl-5-mental-health-instrument-this-will-make-pcl-5-available-for-selection-in-mha-mental-health-assistant-application-the-previous-versions-of-ptsd-checklists-pcl-c-and-pcl-m-are-inactivated-with-this-patch-nationally-released-clinical-reminders-and-reminder-dialogs-that-made-use-of-pcl-c-as-a-mental-health-finding-are-also-updated-to-use-pcl-5-these-include)
    - [VA-PTSD REASSESSMENT (PCL)](#va-ptsd-reassessment-pcl)
    - [VA-MH CPT 1 INITIAL](#va-mh-cpt-1-initial)
    - [VA-MH CPT 2 MEANING SESSION VA-MH CPT 3 ABC SHEET](#va-mh-cpt-2-meaning-session-va-mh-cpt-3-abc-sheet)
    - [VA-MH CPT 4 TRAUMA EVENT SESSION VA-MH CPT 5 REWRITE EVENT](#va-mh-cpt-4-trauma-event-session-va-mh-cpt-5-rewrite-event)
    - [VA-MH CPT 6 CHALLENGING QUESTIONS VA-MH CPT 7 PROBLEMATIC THINKING VA-MH CPT 8 SAFETY](#va-mh-cpt-6-challenging-questions-va-mh-cpt-7-problematic-thinking-va-mh-cpt-8-safety)
    - [VA-MH CPT 9 TRUST](#va-mh-cpt-9-trust)
    - [VA-MH CPT 10 POWER CONTROL VA-MH CPT 11 ESTEEM](#va-mh-cpt-10-power-control-va-mh-cpt-11-esteem)
    - [VA-MH CPT 12 FINAL](#va-mh-cpt-12-final)
    - [VA-MH CPT EARLY TERMINATION VA-MH PEI 1 INITIAL](#va-mh-cpt-early-termination-va-mh-pei-1-initial)
    - [VA-MH PEI 2ND SESSION VA-MH PEI 3RD SESSION](#va-mh-pei-2nd-session-va-mh-pei-3rd-session)
    - [VA-MH PEI 4 IMAGINAL SESSIONS VA-MH PEI 5 FINAL SESSION](#va-mh-pei-4-imaginal-sessions-va-mh-pei-5-final-session)
    - [VA-MH PEI 6 EARLY TERMINATION VA-PTSD EVALUATION (PCL)](#va-mh-pei-6-early-termination-va-ptsd-evaluation-pcl)
    - [VA-PTSD SCREENING](#va-ptsd-screening)
    - [Additionally, the patch provides an interim solution for the problem where instruments with complex scoring algorithms display inaccurate scores in Clinical Reminders and Health Summary. A filter is added that will prevent selection of these instruments in Clinical Reminders and Health Summary until a VistA based scoring algorithm can be deployed.](#additionally-the-patch-provides-an-interim-solution-for-the-problem-where-instruments-with-complex-scoring-algorithms-display-inaccurate-scores-in-clinical-reminders-and-health-summary-a-filter-is-added-that-will-prevent-selection-of-these-instruments-in-clinical-reminders-and-health-summary-until-a-vista-based-scoring-algorithm-can-be-deployed)
    - [To include the changes to Mental Health, Clinical Reminders, and Health Summary, three patches are bundled together in a multi-package build:](#to-include-the-changes-to-mental-health-clinical-reminders-and-health-summary-three-patches-are-bundled-together-in-a-multi-package-build)
    - [YS\5.01\119 PCL-5 Update and Instrument Scoring PXRM\2.0\62 PCL-5 Mental Health Instrument Update GMTS\2.7\116 Correct List of Mental Health Instruments](#ys501119-pcl-5-update-and-instrument-scoring-pxrm2062-pcl-5-mental-health-instrument-update-gmts27116-correct-list-of-mental-health-instruments)
  - [Install the patch first in a training or test account.](#install-the-patch-first-in-a-training-or-test-account)
    - [Installing in a non-production environment will give you time to get familiar with new functionality. It will also allow you to see what changes might be necessary for locally developed clinical reminders and reminder dialogs (see post-installation).](#installing-in-a-non-production-environment-will-give-you-time-to-get-familiar-with-new-functionality-it-will-also-allow-you-to-see-what-changes-might-be-necessary-for-locally-developed-clinical-reminders-and-reminder-dialogs-see-post-installation)
  - [Load the distribution.](#load-the-distribution)
    - [Select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option, LOAD a Distribution. Enter your directory name.KID at the Host File prompt.](#select-the-kernel-installation-distribution-system-menu-xpd-main-then-the-installation-option-and-then-the-option-load-a-distribution-enter-your-directory-namekid-at-the-host-file-prompt)
    - [From the Installation menu, you may elect to use the following options:](#from-the-installation-menu-you-may-elect-to-use-the-following-options)
  - [Backup a Transport Global](#backup-a-transport-global)
    - [This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.](#this-option-will-create-a-backup-message-of-any-routines-exported-with-the-patch-it-will-not-back-up-any-other-changes-such-as-dds-or-templates)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
    - [This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).](#this-option-will-allow-you-to-view-all-changes-that-will-be-made-when-the-patch-is-installed-it-compares-all-components-of-the-patch-routines-dds-templates-etc)
  - [Install the build.](#install-the-build)
    - [From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build YSPCL5UPDATE and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.](#from-the-installation-menu-on-the-kernel-installation-and-distribution-system-kids-menu-run-the-option-install-packages-select-the-build-yspcl5update-and-proceed-with-the-install-if-you-have-problems-with-the-installation-log-a-remedy-ticket-andor-call-the-national-help-desk-to-report-the-problem)
    - [Answer "NO" to the following prompts:](#answer-no-to-the-following-prompts)
    - [Want KIDS to INHIBIT LOGONs during install? NO// NO](#want-kids-to-inhibit-logons-during-install-no-no)
    - [Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO](#want-to-disable-scheduled-options-menu-options-and-protocols-no-no)
    - [See <u>Appendix A</u>.](#see-uappendix-au)
  - [Install File Print (optional)](#install-file-print-optional)
    - [Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.](#use-the-kids-install-file-print-option-to-print-out-the-results-of-the-installation-process-you-can-select-the-multi-package-build-or-any-of-the-individual-builds-included-in-the-multi-package-build)
  - [Build File Print (optional)](#build-file-print-optional)
    - [Use the KIDS Build File Print option to print out the build components.](#use-the-kids-build-file-print-option-to-print-out-the-build-components)
  - [Post-installation routines](#post-installation-routines)
    - [After successful installation, the following init routines may be deleted:](#after-successful-installation-the-following-init-routines-may-be-deleted)
  - [Find usages of PCLC and PCLM in locally developed Clinical Reminders.](#find-usages-of-pclc-and-pclm-in-locally-developed-clinical-reminders)
    - [The installation of patch YS\5.01\119 will inactivate the PCLC and PCLM instruments. If either of these is used as a finding in locally developed clinical reminders, they will need to be changed to use PCL-5 as a finding instead. Use the “Finding Usage Report” option (PXRM FINDING USAGE REPORT) on the Reminder Reports menu to locate any usages of these inactivated instruments. See <u>Appendix B</u> for an example of running this report.](#the-installation-of-patch-ys501119-will-inactivate-the-pclc-and-pclm-instruments-if-either-of-these-is-used-as-a-finding-in-locally-developed-clinical-reminders-they-will-need-to-be-changed-to-use-pcl-5-as-a-finding-instead-use-the-finding-usage-report-option-pxrm-finding-usage-report-on-the-reminder-reports-menu-to-locate-any-usages-of-these-inactivated-instruments-see-uappendix-bu-for-an-example-of-running-this-report)
    - [The report may reveal some usages of PCLC and PCLM in nationally released reminder dialogs. These have already been corrected with replacement dialog elements.](#the-report-may-reveal-some-usages-of-pclc-and-pclm-in-nationally-released-reminder-dialogs-these-have-already-been-corrected-with-replacement-dialog-elements)
  - [Find usages of PCLC and PCLM in Reminder Dialogs.](#find-usages-of-pclc-and-pclm-in-reminder-dialogs)
    - [To find usages of PCLC and PCLM in reminder dialogs specifically, you may use the “Reminder Dialog Search Report” option (PXRM DIALOG SEARCH REPORT) on the Dialog Reports menu using the following steps:](#to-find-usages-of-pclc-and-pclm-in-reminder-dialogs-specifically-you-may-use-the-reminder-dialog-search-report-option-pxrm-dialog-search-report-on-the-dialog-reports-menu-using-the-following-steps)
    - [When prompted “Search for coding system?” answer NO.](#when-prompted-search-for-coding-system-answer-no)
    - [When prompted “Search for Finding Item(s) used in dialog component(s)?” answer YES. When prompted for a list, enter 5 - MENTAL HEALTH.](#when-prompted-search-for-finding-items-used-in-dialog-components-answer-yes-when-prompted-for-a-list-enter-5-mental-health)
    - [When prompted for ALL or SELECTED, answer SELECTED.](#when-prompted-for-all-or-selected-answer-selected)
    - [When prompted “Select MENTAL HEALTH:”, enter PCLC followed by PCLM. When prompted “Search for specific Reminder Dialog component(s)?” answer NO. When prompted “Search for Reminder Dialog by CPRS parameter(s)?” answer NO. When prompted “Display match criteria on the report?” answer YES.](#when-prompted-select-mental-health-enter-pclc-followed-by-pclm-when-prompted-search-for-specific-reminder-dialog-components-answer-no-when-prompted-search-for-reminder-dialog-by-cprs-parameters-answer-no-when-prompted-display-match-criteria-on-the-report-answer-yes)
    - [A list of dialogs that use PCLC or PCLM, if any, will be displayed. An example of this report is found in <u>Appendix C</u>.](#a-list-of-dialogs-that-use-pclc-or-pclm-if-any-will-be-displayed-an-example-of-this-report-is-found-in-uappendix-cu)
  - [Modify findings to use PCL-5.](#modify-findings-to-use-pcl-5)
    - [The reports may show some nationally released items. You only need to address the locally developed reminder definitions and reminder dialogs. Correct any locally defined reminders by changing the finding value from PCLC or PCLM to PCL-5.](#the-reports-may-show-some-nationally-released-items-you-only-need-to-address-the-locally-developed-reminder-definitions-and-reminder-dialogs-correct-any-locally-defined-reminders-by-changing-the-finding-value-from-pclc-or-pclm-to-pcl-5)
- [<u>Acronyms</u>](#uacronymsu)
    - [The OI&T Master Glossary is available at REDACTED](#the-oit-master-glossary-is-available-at-redacted)

### This patch releases the Posttraumatic Stress Disorder (PTSD) Checklist 5 (PCL-5) mental health instrument. This will make PCL-5 available for selection in MHA (Mental Health Assistant) application. The previous versions of PTSD checklists, PCL-C and PCL-M are inactivated with this patch. Nationally released Clinical Reminders and Reminder Dialogs that made use of PCL- C as a mental health finding are also updated to use PCL-5. These include:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Clinical Reminders

### VA-PTSD REASSESSMENT (PCL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Reminder Dialogs

### VA-MH CPT 1 INITIAL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-MH CPT 2 MEANING SESSION VA-MH CPT 3 ABC SHEET

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-MH CPT 4 TRAUMA EVENT SESSION VA-MH CPT 5 REWRITE EVENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-MH CPT 6 CHALLENGING QUESTIONS VA-MH CPT 7 PROBLEMATIC THINKING VA-MH CPT 8 SAFETY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-MH CPT 9 TRUST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-MH CPT 10 POWER CONTROL VA-MH CPT 11 ESTEEM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-MH CPT 12 FINAL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-MH CPT EARLY TERMINATION VA-MH PEI 1 INITIAL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-MH PEI 2ND SESSION VA-MH PEI 3RD SESSION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-MH PEI 4 IMAGINAL SESSIONS VA-MH PEI 5 FINAL SESSION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-MH PEI 6 EARLY TERMINATION VA-PTSD EVALUATION (PCL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-PTSD SCREENING

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Additionally, the patch provides an interim solution for the problem where instruments with complex scoring algorithms display inaccurate scores in Clinical Reminders and Health Summary. A filter is added that will prevent selection of these instruments in Clinical Reminders and Health Summary until a VistA based scoring algorithm can be deployed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### To include the changes to Mental Health, Clinical Reminders, and Health Summary, three patches are bundled together in a multi-package build:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### YS\*5.01\*119 PCL-5 Update and Instrument Scoring PXRM\*2.0\*62 PCL-5 Mental Health Instrument Update GMTS\*2.7\*116 Correct List of Mental Health Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark1" class="anchor"></span><u>Installation</u>

#### This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 5 minutes

1.  <span id="_bookmark2" class="anchor"></span>Retrieve the host file from one of the following locations using Secure File Transfer Protocol (SFTP). The file should be downloaded using the ASCII file type):

## Install the patch first in a training or test account.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Installing in a non-production environment will give you time to get familiar with new functionality. It will also allow you to see what changes might be necessary for locally developed clinical reminders and reminder dialogs (see post-installation).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Load the distribution.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option, LOAD a Distribution. Enter your directory name.KID at the Host File prompt.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example

### From the Installation menu, you may elect to use the following options:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Backup a Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Install the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build YS_PCL5_UPDATE and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Answer "NO" to the following prompts:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Want KIDS to INHIBIT LOGONs during install? NO// NO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation Example

### See [<u>Appendix A</u>](#_bookmark15).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Install File Print (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Build File Print (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Use the KIDS Build File Print option to print out the build components.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### After successful installation, the following init routines may be deleted:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PXRMP62E PXRMP62I

> <span id="_bookmark11" class="anchor"></span>Post-Install Set-up Instructions

## Find usages of PCLC and PCLM in locally developed Clinical Reminders.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The installation of patch YS\*5.01\*119 will inactivate the PCLC and PCLM instruments. If either of these is used as a finding in locally developed clinical reminders, they will need to be changed to use PCL-5 as a finding instead. Use the “Finding Usage Report” option (PXRM FINDING USAGE REPORT) on the Reminder Reports menu to locate any usages of these inactivated instruments. See [<u>Appendix B</u>](#_bookmark16) for an example of running this report.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The report may reveal some usages of PCLC and PCLM in nationally released reminder dialogs. These have already been corrected with replacement dialog elements.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Find usages of PCLC and PCLM in Reminder Dialogs.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### To find usages of PCLC and PCLM in reminder dialogs specifically, you may use the “Reminder Dialog Search Report” option (PXRM DIALOG SEARCH REPORT) on the Dialog Reports menu using the following steps:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When prompted “Search for coding system?” answer NO.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When prompted “Search for Finding Item(s) used in dialog component(s)?” answer YES. When prompted for a list, enter 5 - MENTAL HEALTH.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When prompted for ALL or SELECTED, answer SELECTED.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When prompted “Select MENTAL HEALTH:”, enter PCLC followed by PCLM. When prompted “Search for specific Reminder Dialog component(s)?” answer NO. When prompted “Search for Reminder Dialog by CPRS parameter(s)?” answer NO. When prompted “Display match criteria on the report?” answer YES.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### A list of dialogs that use PCLC or PCLM, if any, will be displayed. An example of this report is found in [<u>Appendix C</u>](#_bookmark18).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modify findings to use PCL-5.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The reports may show some nationally released items. You only need to address the locally developed reminder definitions and reminder dialogs. Correct any locally defined reminders by changing the finding value from PCLC or PCLM to PCL-5.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark15" class="anchor"></span><u>Appendix A: Installation Example</u>

> Select Kernel Installation & Distribution System \<INITIAL\> Option: INstallation

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> You have PENDING ALERTS

> Enter "VA to jump to VIEW ALERTS option

> Select Installation \<INITIAL\> Option: LOad a Distribution

> Enter a Host File: \<your directory\>YS_PCL5_UPDATE.KID

> KIDS Distribution saved on Jan 13, 2016@14:23:46

> Comment: PCL-5 Update Combined Build with YS\*5.01\*119, GMTS\*2.7\*116, PXRM\*2.0\*62

> This Distribution contains Transport Globals for the following Package(s): YS_PCL5_UPDATE 1.0

> YS\*5.01\*119 GMTS\*2.7\*116 PXRM\*2.0\*62

> Distribution OK!

> Want to Continue with Load? YES// YES

> Loading Distribution...

> YS_PCL5_UPDATE 1.0

> Build YS\*5.01\*119 has an Environmental Check Routine Want to RUN the Environment Check Routine? YES//

> YS\*5.01\*119

> Will first run the Environment Check Routine, YS119ENV

> GMTS\*2.7\*116 PXRM\*2.0\*62

> Use INSTALL NAME: YS_PCL5_UPDATE 1.0 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> You have PENDING ALERTS

> Enter "VA to jump to VIEW ALERTS option

> Select Installation \<INITIAL\> Option: Install Package(s)

> Select INSTALL NAME: YS_PCL5_UPDATE 1.0 1/13/16@17:16:28

> =\> PCL-5 Update Combined Build with YS\*5.01\*119, GMTS\*2.7\*116, PXRM\*2.0\*6

> This Distribution was loaded on Jan 13, 2016@17:16:28 with header of

> PCL-5 Update Combined Build with YS\*5.01\*119, GMTS\*2.7\*116, PXRM\*2.0\*62 ;Created on Jan 13, 2016@14:23:46

> It consisted of the following Install(s):

> YS_PCL5_UPDATE 1.0 YS\*5.01\*119 GMTS\*2.7\*116 PXRM\*2.0\*62

> Checking Install for Package YS_PCL5_UPDATE 1.0 Install Questions for YS_PCL5_UPDATE 1.0

> Checking Install for Package YS\*5.01\*119 Install Questions for YS\*5.01\*119 Incoming Files:

> 601.71 MH TESTS AND SURVEYS (including data) Note: You already have the 'MH TESTS AND SURVEYS' File. I will OVERWRITE your data with mine.

> Checking Install for Package GMTS\*2.7\*116 Install Questions for GMTS\*2.7\*116

> Checking Install for Package PXRM\*2.0\*62 Install Questions for PXRM\*2.0\*62 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

DEVICE: HOME// HOME PSEUDO-TERMINAL SLAVE

Install Started for YS_PCL5_UPDATE 1.0 :

> Jan 13, 2016@17:19:35

> Build Distribution Date: Jan 13, 2016 Installing Routines:.

> Jan 13, 2016@17:19:35

> Install Started for YS\*5.01\*119 :

> Jan 13, 2016@17:19:35

> Build Distribution Date: Jan 13, 2016 Installing Routines:...................

> Jan 13, 2016@17:19:35

> Installing Data Dictionaries: ..

> Jan 13, 2016@17:19:36

> Installing Data:

> Jan 13, 2016@17:19:36

> Running Post-Install Routine: POST^YS119PST. Updating Routine file......

> Updating KIDS files.......

> YS\*5.01\*119 Installed.

> Jan 13, 2016@17:19:36

> Not a production UCI NO Install Message sent

> Install Started for GMTS\*2.7\*116 :

> Jan 13, 2016@17:19:36

> Build Distribution Date: Jan 13, 2016 Installing Routines:..

> Jan 13, 2016@17:19:36

> Updating Routine file......

> Updating KIDS files.......

> GMTS\*2.7\*116 Installed.

> Jan 13, 2016@17:19:36

> Not a production UCI

> NO Install Message sent

> Install Started for PXRM\*2.0\*62 :

> Jan 13, 2016@17:19:36

> Build Distribution Date: Jan 13, 2016 Installing Routines:...

> Jan 13, 2016@17:19:36

> Running Pre-Install Routine: PRE^PXRMP62I. DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries: ..

> Jan 13, 2016@17:19:36

> Installing Data:

> Jan 13, 2016@17:19:36

> Running Post-Install Routine: POST^PXRMP62I. ENABLE options.

> ENABLE protocols.

> There are 1 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry PXRM\*2.0\*62 PCL-5 INSTRUMENT Updating Routine file......

> Updating KIDS files.......

> PXRM\*2.0\*62 Installed.

> Jan 13, 2016@17:19:40

> Not a production UCI NO Install Message sent

> Updating Routine file.....

> Updating KIDS files.....

> YS_PCL5_UPDATE 1.0 Installed.

> Jan 13, 2016@17:19:40

> No link to PACKAGE file

> <span id="_bookmark16" class="anchor"></span>NO Install Message sent

> <span id="_bookmark17" class="anchor"></span><u>Appendix B: Find Usage Example</u>

> Select Reminder Managers Menu \<INITIAL\> Option: RP Reminder Reports

> D Reminders Due Report

> DRU Reminders Due Report (User) DRT User Report Templates

> EPT Extract EPI Totals

> EPF Extract EPI List by Finding and SSN EQT Extract QUERI Totals

> GEC GEC Referral Report REV Review Date Report FUR Finding Usage Report

> You have PENDING ALERTS

> Enter "VA to jump to VIEW ALERTS option

> Select Reminder Reports \<INITIAL\> Option: FUR Finding Usage Report Clinical Reminders Usage Report

> Select from the following reminder findings (\* signifies standardized):

1.  \- DRUG
2.  \- EDUCATION TOPICS
3.  \- EXAM
4.  \- HEALTH FACTOR
5.  \- IMMUNIZATION
6.  \- LABORATORY TEST
7.  \- MENTAL HEALTH
8.  \- MH TESTS AND SURVEYS
9.  \- ORDER DIALOG
10. \- ORDERABLE ITEM
11. \- RADIOLOGY PROCEDURE
12. \- REMINDER COMPUTED FINDING
13. \- REMINDER DEFINITION
14. \- REMINDER LOCATION LIST
15. \- REMINDER TAXONOMY
16. \- REMINDER TERM
17. \- SKIN TEST
18. \- VA DRUG CLASS
19. \- VA GENERIC
20. \- VITAL MEASUREMENT
21. \- VITAL TYPE
22. \- WH NOTIFICATION PURPOSE

> Enter your list for the report: (1-22): 7

> Search for all or selected MENTAL HEALTHS?

> Select one of the following:

1.  ALL
2.  SELECTED

> Enter response: SELECTED// SELECTED Select MENTAL HEALTH: PCLC PCLC Select MENTAL HEALTH: PCLM PCLM Select MENTAL HEALTH:

> Browse or Print? B// Print

> DEVICE: HOME// HOME PSEUDO-TERMINAL SLAVE

> Clinical Reminders finding usage report.

> The following MH TESTS AND SURVEYS(s) are used as follows:

> ======================================================= MH TESTS AND SURVEYS - PCLC (IEN=40)

> Is used in the following Reminder Definition(s): EVALUATION OF + PTSD SCREEN (IEN=918)

> Finding number 3

> BL PCLC NEEDED (IEN=959)

> Finding number 3

> Is used in the following Reminder Dialog(s):

> Dialog result group PXRM PCLC RESULT GROUP (IEN=3594), used in the MH Test field

> Dialog element VA-MH PCLC (IEN=3595), used in the Finding Item field

> Dialog element VA-MH CPT PCLC (IEN=3772), used in the Finding Item field

> Is used in the following Reminder Term(s):

> VA-PTSD CHECKLIST (IEN=661)

> Finding number 1

> ======================================================= MH TESTS AND SURVEYS - PCLM (IEN=41)

> Is used in the following Reminder Definition(s):

> EVALUATION OF + PTSD SCREEN (IEN=918)

> Finding number 4

> BL PCLC NEEDED (IEN=959)

> Finding number 4

> <span id="_bookmark18" class="anchor"></span>Is used in the following Reminder Dialog(s):

> Dialog result group PXRM PCLM RESULT GROUP (IEN=3555), used in the MH Test field

> Dialog element VA-MH PCLM (IEN=3558), used in the Finding Item field

> <span id="_bookmark19" class="anchor"></span><u>Appendix C: Dialog Search Example</u>

> Select Reminder Dialog Management \<INITIAL\> Option: DR Dialog Reports

> OR Reminder Dialog Elements Orphan Report ER Empty Reminder Dialog Report

> ALL Check all active reminder dialog for invalid items SEA Reminder Dialog Search Report

> CH Check Reminder Dialog for invalid items

> You have PENDING ALERTS

> Enter "VA to jump to VIEW ALERTS option

> Select Dialog Reports \<INITIAL\> Option: SEA Reminder Dialog Search Report Search for coding system? N// NO O

> Search for Finding Item(s) used in dialog component(s)? N// YES

> Select from the following reminder findings (\* signifies standardized):

1.  \- EDUCATION TOPICS
2.  \- EXAM
3.  \- HEALTH FACTOR
4.  \- IMMUNIZATION
5.  \- MENTAL HEALTH
6.  \- ORDER DIALOG
7.  \- REMINDER TAXONOMY
8.  \- SKIN TEST
9.  \- VITAL TYPE
10. \- WH NOTIFICATION PURPOSE

> Enter your list for the report: (1-10): 5

> Search for all or selected MENTAL HEALTHS?

> Select one of the following:

1.  ALL
2.  SELECTED

> Enter response: SELECTED// SELECTED Select MENTAL HEALTH: PCLC PCLC Select MENTAL HEALTH: PCLM PCLM Select MENTAL HEALTH:

> Search for specific Reminder Dialog component(s)? N// NO O Search for Reminder Dialog by CPRS parameter(s)? N// NO O Display match criteria on the report? N// YES

> No parent dialogs found.

# <u>Acronyms</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The OI&T Master Glossary is available at REDACTED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term | Definition                                                 |
|----------|----------------------------------------------------------------|
| ASCII    | American Standard Code for Information Interchange             |
| CPT      | Cognitive Processing Therapy                                   |
| FTP      | File Transfer Protocol                                         |
| GMTS     | Health Summary namespace                                       |
| KIDS     | Kernel Installation and Distribution System                    |
| MH       | Mental Health namespace                                        |
| MHA      | Mental Health Assistant                                        |
| PCLC     | PTSD Checklist - Civilian                                      |
| PCLM     | PTSD Checklist - Military                                      |
| PCL-5    | PTSD Checklist (DSM-5)                                         |
| PE       | Prolonged Exposure Therapy                                     |
| PEI      | Prolonged Exposure Therapy (namespace)                         |
| PTSD     | Post-Traumatic Stress Disorder                                 |
| PXRM     | Clinical Reminders namespace                                   |
| VistA    | Veterans Health Information System and Technology Architecture |