---
title: PXRM*2*24 High Risk Mental Health Patient Phase 2 Installation & Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: patch
doc_subject: High Risk Mental Health Patient Phase 2 Installation &
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*24
group_key: "YS:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - class
  - table
  - contents
  - calculated
  - even
  - strong
  - style
  - width
  - colgroup
page_count: 0
word_count: 9693
section_count: 3
table_count: 1
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: April 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/pxrm_2_24_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/pxrm_2_24_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/001.png)

> High Risk Mental Health Patient – National Reminder and Flag

## Patches DG\*5.3\*849 GMTS\*2.7\*104 OR\*3.0\*348 PXRM\*2\*24 SD\*5.3\*588 TIU\*1.0\*265

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> INSTALLATION and SETUP GUIDE

## April 2013

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Revised May 9, 2013*

> Department of Veterans Affairs Office of Information and Technology (OIT)

> Product Development

> <u>Contents</u>

1.  [Retrieve the host file containing the multi-package build, HIGH RISK MH 2.0. 13](#1._Retrieve_the_host_file_containing_the)
2.  [Install the build first in a training or test account 13](#install-the-build-first-in-a-training-or-test-account.)
3.  [Load the distribution. 13](#load-the-distribution.)
    1.  [Backup a Transport Global 13](#backup-a-transport-global)
    2.  [Compare Transport Global to Current System 14](#compare-transport-global-to-current-system)
    3.  [Verify Checksums in Transport Global 14](#verify-checksums-in-transport-global)
4.  [Install the build. 16](#install-the-build.)
5.  [Install File Print 16](#install-file-print)
6.  [Build File Print 16](#build-file-print)
7.  [Post-installation routines 17](#post-installation-routines)

> May 2013 High Risk Mental Health Patient – National Reminder & Flag ii

> Installation and Setup Guide

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Patches DG\5.3\849 GMTS\2.7\104 OR\3.0\348 PXRM\2\24 SD\5.3\588 TIU\1.0\265](#patches-dg53849-gmts27104-or30348-pxrm224-sd53588-tiu10265)
  - [April 2013](#april-2013)
- [Introduction](#introduction)
    - [DG\5.3\849](#dg53849)
    - [ IMPORTANT DEPLOYMENT NOTE: SPC staff should NOT run the Processing mode of the DGPF LOCAL TO NATIONAL CONVERT option (Process Local-to- National option) until 30 days after the national release date and sites have received approval from the Office of Mental Health Services (OMHS). This will help to minimize transmission error messages among sites with shared patients. These error messages occur when one of these sites has installed and runs the conversion, but another site that also sees the same patient(s) has not installed this newly released software patch(s). SPC staff may run the Report Only mode of the option after installing the package, to get a preliminary report of local PRFs that will be converted.](#important-deployment-note-spc-staff-should-not-run-the-processing-mode-of-the-dgpf-local-to-national-convert-option-process-local-to-national-option-until-30-days-after-the-national-release-date-and-sites-have-received-approval-from-the-office-of-mental-health-services-omhs-this-will-help-to-minimize-transmission-error-messages-among-sites-with-shared-patients-these-error-messages-occur-when-one-of-these-sites-has-installed-and-runs-the-conversion-but-another-site-that-also-sees-the-same-patients-has-not-installed-this-newly-released-software-patchs-spc-staff-may-run-the-report-only-mode-of-the-option-after-installing-the-package-to-get-a-preliminary-report-of-local-prfs-that-will-be-converted)
    - [TIU\1.0\265](#tiu10265)
    - [SD\5.3\588](#sd53588)
    - [Changes to the SD MH NO SHOW AD HOC REPORT:](#changes-to-the-sd-mh-no-show-ad-hoc-report)
    - [Changes to the SD MH NO SHOW AD HOC REPORT and SD MH NO SHOW NIGHTLY BGJ:](#changes-to-the-sd-mh-no-show-ad-hoc-report-and-sd-mh-no-show-nightly-bgj)
    - [PXRM\2.0\24 - MH HIGH RISK PHASE 2](#pxrm2024-mh-high-risk-phase-2)
    - [GMTS\2.7\104](#gmts27104)
    - [OR\3\348](#or3348)
    - [\\\Important Note\\\](#important-note)
    - [Related Documentation](#related-documentation)
    - [Health Summary GMTS\2.7\104 Documentation](#health-summary-gmts27104-documentation)
    - [Scheduling SD\5.3\588 and Registration DG\5.3\849 Documentation](#scheduling-sd53588-and-registration-dg53849-documentation)
    - [Related Web Sites](#related-web-sites)
- [Pre-Installation](#pre-installation)
    - [We recommend that the team members who will be responsible for implementing this project coordinate with each other before installing the patches, to determine the first three pre-install steps. This team could include MH coordinators, Suicide Prevention Coordinators, Clinical Application Coordinators (CACs), Reminders Managers, and IRM staff.](#we-recommend-that-the-team-members-who-will-be-responsible-for-implementing-this-project-coordinate-with-each-other-before-installing-the-patches-to-determine-the-first-three-pre-install-steps-this-team-could-include-mh-coordinators-suicide-prevention-coordinators-clinical-application-coordinators-cacs-reminders-managers-and-irm-staff)
    - [Example](#example)
    - [renumber it before this patch is installed. See Appendix B for instructions for recreating or re-pointing site-defined notifications.](#renumber-it-before-this-patch-is-installed-see-appendix-b-for-instructions-for-recreating-or-re-pointing-site-defined-notifications)
    - [Required Software for PXRM\2\24](#required-software-for-pxrm224)
    - [Required Software for SD\5.3\578](#required-software-for-sd53578)
    - [Required Software for TIU\1\260](#required-software-for-tiu1260)
    - [Estimated Installation Time: 10-15 minutes](#estimated-installation-time-10-15-minutes)
- [Installation](#installation)
    - [Install the build first in a training or test account.](#install-the-build-first-in-a-training-or-test-account)
    - [Load the distribution.](#load-the-distribution)
    - [Example](#example-1)
    - [Backup a Transport Global](#backup-a-transport-global)
    - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
    - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
    - [Install the build.](#install-the-build)
    - [Installation Example](#installation-example)
    - [Install File Print](#install-file-print)
    - [Build File Print](#build-file-print)
    - [Post-installation routines](#post-installation-routines)
- [Post-Install Set-up Instructions](#post-install-set-up-instructions)
    - [Business Rule:](#business-rule)
    - [Example:](#example-2)
    - [Record Flag Transmission Errors option description](#record-flag-transmission-errors-option-description)
    - [Scenarios that can cause the transmission errors:](#scenarios-that-can-cause-the-transmission-errors)
    - [Set of codes indicating default provider recipients of a notification by their title or relationship to the patient.](#set-of-codes-indicating-default-provider-recipients-of-a-notification-by-their-title-or-relationship-to-the-patient)
    - [Set up a Reminders Due report template for SPCs.](#set-up-a-reminders-due-report-template-for-spcs)
    - [![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/026.png) The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services.](#pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide026png-the-new-reminder-location-list-is-consistent-with-the-national-list-of-mh-encounter-stop-codes-defined-for-sites-by-the-office-of-mental-health-services)
    - [Ensure that the new health summary types have been added to the CPRS Reports tab display. (This should’ve been done as part of the installation and setup of Phase 1 of the HRMHP project, which was released in March 2012.)](#ensure-that-the-new-health-summary-types-have-been-added-to-the-cprs-reports-tab-display-this-shouldve-been-done-as-part-of-the-installation-and-setup-of-phase-1-of-the-hrmhp-project-which-was-released-in-march-2012)
    - [When notified by the Office of Mental Health Services, run the Convert Local HRMHP PRF to National option - Process mode.](#when-notified-by-the-office-of-mental-health-services-run-the-convert-local-hrmhp-prf-to-national-option-process-mode)
    - [Ownership of Category I flag determined at assignment and when Process Mode is run:](#ownership-of-category-i-flag-determined-at-assignment-and-when-process-mode-is-run)
    - [Example of a transmission error logged at the site that originated the Category I flag (“owner” site) for a patient](#example-of-a-transmission-error-logged-at-the-site-that-originated-the-category-i-flag-owner-site-for-a-patient)
- [Back-Out Plan for Production Environment](#back-out-plan-for-production-environment)
- [Appendix A: Installation Examples](#appendix-a-installation-examples)
    - [First-Time Install](#first-time-install)
> The purpose of the High Risk Mental Health Patient- Reminder and Flag (HRMHP) project is to support Mental Health (MH) professionals in the tracking of veterans with the High Risk for Suicide Patient Record Flag (PRF) who have missed Mental Health (MH) Clinic appointments due to a no-show.
> This is the second release (Phase 2) of the (HRMHP) project. It includes six patches, which will be installed as a combined build, HIGH RISK MH 2.0. This Installation Guide describes installing and setting up Phase 2.
> This installation contains a post-implementation step (related to DG\*5.3\*849), which first requires all sites to have the bundle installed on their VistA system.
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/002.png) The Implementation Manager will monitor sites that are installing and will contact sites to complete the install to meet the install requirement within 30 days.
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/003.png) After all sites have installed, the Implementation manager will inform the HRMHP Phase 2 Project Manager.
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/004.png) The Project Manager will contact the Office of Mental Health Services (OMHS) to indicate that all VistA systems have the HRMHP software installed.
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/005.png) The OMHS, which has regular calls with Suicide Prevention Coordinators (SPCs) across the VA, will guide SPCs through a post-installation step.
> May 2013 High Risk Mental Health Patient – National Reminder & Flag 1
> Installation and Setup Guide

### DG\*5.3\*849

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This build installs a new national Patient Record Flag (PRF) for suicide prevention: HIGH RISK FOR SUICIDE. Clinically, the Category I PRF for high risk for suicide will not be available to the site until the install is completed. Furthermore, we recommend that the Category I HIGH RISK FOR SUICIDE PRF should not be assigned to a patient until the post-installation step is completed by an SPC on each VistA System. Until then, all of the high risk patients will continue to have the local Category II PRFs on their record that clinicians are accustomed to working with.
> This build also installs a new option, Convert Local HRMH PRF to National \[DGPF LOCAL TO NATIONAL CONVERT\], which will allow an SPC to auto-generate new national PRFs for suicide prevention from local, active, suicide prevention Category II PRFs. This option can be run in either Report-only or in Processing mode – but the Processing mode must not be run until OMHS informs the SPCs that it is OK to run.

###  IMPORTANT DEPLOYMENT NOTE: SPC staff should NOT run the Processing mode of the DGPF LOCAL TO NATIONAL CONVERT option (Process Local-to- National option) until 30 days after the national release date and sites have received approval from the Office of Mental Health Services (OMHS). This will help to minimize transmission error messages among sites with shared patients. These error messages occur when one of these sites has installed and runs the conversion, but another site that also sees the same patient(s) has not installed this newly released software patch(s). SPC staff may run the Report Only mode of the option after installing the package, to get a preliminary report of local PRFs that will be converted.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DG\*5.3\*849 post-installation steps on every VistA system:
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/006.png) For each VistA system, OMHS will task an SPC to complete the post-install step that will automatically convert the Category II flag to the Category I flag (Process mode of DGPF LOCAL TO NATIONAL CONVERT option).
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/007.png) After all sites have installed HRMHP Phase 2 patches, the Office of Mental Health Services (OMHS) will announce on their SPC conference calls and via Outlook that the Process Mode of the DGPF LOCAL TO NATIONAL CONVERT option can now be run by the assigned SPC for the VistA system.
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/008.png) The assigned SPC will be responsible for ensuring that the Report-Only mode has already been run and resolved any patient issues found before running the Process mode.
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/009.png) The SPC will be responsible for regularly monitoring the PRF TRANSMISSION MANAGEMENT option to ensure that there are no transmission errors between their system and other systems due to the Process mode.
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/010.png) Any issues should be dealt with between the SPCs at each site. For example, if two sites treating the same patient had the Category II flag, than the PRF TRANSMISSION MANAGEMENT option will inform them of the situation, and the
> SPCs will figure out which site should be the owner and use the Patient Record Flag Management option to assign/change the ownership.
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/011.png) The SPC will be responsible for reporting back to the OMHS when the process mode is completed.

### TIU\*1.0\*265

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This Text Integration Utility patch installs a new title in the TIU DOCUMENT DEFINITION: PATIENT RECORD FLAG CATEGORY I – HIGH RISK FOR SUICIDE.
> This title will be used with the new Patient Record Flag. The patch installation links the title to the existing document class, PATIENT RECORD FLAG CAT I.
> This patch also provides one fix to TUI\*1\*260 in routine ^TIULO1. A formatting error was discovered in the MH MISSED APPOINTMENTS 10D TIU object. This is the object that will display on the High Risk MH No-Show Follow-up reminder dialog whenever a patient has missed a mental health appointment within the last 10 days.

### SD\*5.3\*588

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This build contains two new proactive reports that list appointments for High Risk for Suicide patients who have appointments for the day. The SD MH PROACTIVE BGJ REPORT is a background job that will run in the background and send a mail message to the members of the SD MH NO SHOW NOTIFICATION mail group. This report will be kicked off by the Scheduling nightly background job (SDAM BACKGROUND JOB) that should already be scheduled to run nightly on your system. It is the same background job that calls the SD MH NO SHOW NIGHTLY BGJ.
> NOTE: DO NOT schedule the options:
> SD MH NO SHOW NIGHTLY BGJ SD MH PROACTIVE BGJ REPORT
> Scheduling’s Nightly Background Job generates these reports.
> An ad hoc report option, High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\], generates a *proactive* report that can be run by the users. This report is more flexible and allows users to refine the report to their specifications. This report will list, by divisions, all patients with PRF High Risk for Suicide who have appointments in mental health clinics today. Totals will list the number of unique patients by division. The patients are listed alphabetically by division and by date/time of the appointment.
> This build also allows the SD MH NO SHOW AD HOC REPORT, SD MH NO SHOW NIGHTLY BGJ, SD MH PROACTIVE AD HOC REPORT and SD MH PROACTIVE BGJ
> REPORT to look for PRF activity from the new national Category I Patient Record Flag, HIGH RISK FOR SUICIDE, as well as from local Patient Record Flags.
> SD\*5.3\*588 contains a post-installation routine that will add two new parameters to the PARAMETERS (#8989.5) file, with associated parameter definitions added to the PARAMETER DEFINITION (#8989.51) file. The new parameter SDMH PROACTIVE
> DAYS stores a value that will list future appointments for the number of days stored in the parameter, for each patient on the report. This parameter is checked when Nightly SD MH PROACTIVE BGJ REPORT is run. The second new parameter is SDMH NO SHOW DAYS which also stores a value that will list future appointments for the number of days stored in the parameter, for each patient on the SD MH NO SHOW NIGHTLY BGJ Report.
> The default value of 30 days will be populated by the post-init for both parameters. Sites may change the number of days stored in the parameter, by using the General Parameter Tools option, selecting the Edit Parameter Values option, and entering SDMH PROACTIVE DAYS or SDMH NO SHOW DAYS. Once changed, the reports will reflect the change by displaying the new number of days of future appointments on the report.

### Changes to the SD MH NO SHOW AD HOC REPORT:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The report displays The Mental Health Treatment Coordinator (MHTC) name and the name of the care team that the MHTC is assigned to in parentheses.
2.  The report displays the results of the no-show patient contact.

### Changes to the SD MH NO SHOW AD HOC REPORT and SD MH NO SHOW NIGHTLY BGJ:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. The provider name is now displayed directly under the NO Show Appointment information to keep everything connected.

### PXRM\*2.0\*24 - MH HIGH RISK PHASE 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This Clinical Reminders patch includes an updated reminder definition (VA-MH HIGH RISK NO-SHOW FOLLOW-UP), two new reminder definitions, (VA-MH HIGH RISK NO- SHOW ADHOC RPT and VA-MHTC NEEDS ASSIGNMENT), a new computed finding (VA-PCMM MHTC), and a new dialog that will display the Mental Health Treatment Coordinator (MHTC)..
> The MH HIGH RISK NO-SHOW ADHOC RPT reminder determines whether Mental Health (MH) professionals have followed up during the week following a No-Show MH appointment for a patient with an active High Risk for Suicide Patient Record Flag. This reminder is called from a Scheduling report for each No-Show MH appointment.
> A new reminder titled VA-MHTC NEEDS ASSIGNMENT is available and can be used from CPRS on the Cover Sheet’s Reminders Due section when the patient is a candidate for MHTC assignment. The reminder looks for three MH appointments within a specific period
> of time, and then checks to see if the MHTC is defined for the patients. The reminder will be due when no MHTC is currently assigned to the patient. A Reminders Due Report can be run weekly to get a list of patients who have not yet been assigned an MHTC. MHTC NEEDS ASSIGNMENT uses a new Reminder Location List called VA-MHTC APPT STOP CODES LL in the Computed Finding: VA-Appointments for a Patient. The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services. The new VA-PCMM MHTC Computed Finding can be used in Reminder Definitions to get the MHTC assigned to a patient.
> A new term, The VA-MH HIGH RISK FOR SUICIDE PRF was added, to be used in the Reminder Definitions in the High Risk for Suicide Patient – Reminder & Flag project. The following description was added to the VA-HIGH RISK FOR SUICIDE PRF Reminder Term:
> This reminder looks for the national category I HIGH RISK FOR SUICIDE patient record flag and the local category II patient record flag used at your site.
> This term is distributed to look for the local name HIGH RISK FOR SUICIDE, which is the first mapped finding in the Mapped Findings. The Computed Finding Parameter of HIGH RISK FOR SUICIDE^L means use the local patient record flag called HIGH RISK FOR SUICIDE. If your site uses a different category II patient record flag name, then the computed finding parameter for the first mapped finding should be changed. For example, if your site uses SUICIDE RISK as the name of the category II patient record flag, then the Computed Finding Parameter should be changed to SUICIDE RISK^L.
> *Do not change the second mapped finding with the Computed Finding Parameter of HIGH RISK FOR SUICIDE^N.*

### GMTS\*2.7\*104

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch will modify two entries in the Health Summary Component file (142.1): MH HIGH RISK PRF HX and MH TREATMENT COORDINATOR.
> These components are used in the VA-MH HIGH RISK PATIENT and REMOTE MH HIGH RISK PATIENT Health Summaries, and are also available for use in the Health Summary Adhoc Report. Additionally, the VA-MH HIGH RISK PATIENT Health Summary is also embedded in the VA-MH HIGH RISK NO SHOW FOLLOW-UP Reminder Dialog released in Phase I of this project.
> The MH HIGH RISK PRF HX component now includes the assignment history for the newly created Category I Patient Record Flag (HIGH RISK FOR SUICIDE). The assignment history in Health Summary will display both Category II (local) and Category I (national) assignments for High Risk for Suicide until all local entries have been converted to the national flag.
> The MH TREATMENT COORDINATOR component will now be fully functional and display the mental health treatment team, mental health treatment coordinator (MHTC), and the MHTC contact information.

### OR\*3\*348

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch adds a new provider recipient, Primary Care Management Module (PCMM) Mental Health Treatment Coordinator (MHTC), to the existing ORB PROVIDER RECIPIENTS parameter. It will be added as a “C” code to the existing “PATOMERS” values:
> P (Primary Provider): deliver notification to the patient's Primary Provider.
> A (Attending Physician): deliver notification to the patient's Attending Physician.
> T (Patient Care Team): deliver notification to the patient's OE/RR Teams (personal patient and team lists are evaluated for potential recipients) and to devices on an OE/RR team).
> O (Ordering Provider): deliver notification to the provider who placed the order which trigger the notification.
> M (PCMM Team): deliver notification to users/providers linked to the patient via PCMM Team Position assignments.
> E (Entering User): deliver notification to the user/provider who entered the order's most recent activity.
> R (PCMM Primary Care Practitioner): deliver notification to the patient's PCMM Primary Care Practitioner.
> S (PCMM Associate Provider): deliver notification to the patient's PCMM Associate Provider.
> C (PCMM Mental Health Treatment Coordinator): deliver notification to the patient's PCMM Mental Health Treatment Coordinator.
> With this enhancement, MHTCs can now specify to be default provider recipients of certain pertinent notifications, such as for Admissions, Discharge, and Deceased Patient, to name a few.
> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/012.png)![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/013.png)![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/014.png)![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/015.png)![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/016.png)![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/017.png)![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/018.png)The following parameters in the PARAMETERS DEFINITION file \#8989.51 will also be updated accordingly to reflect these changes:
> ORB PROVIDER RECIPIENTS ORB OI EXPIRING - INPT PR ORB OI EXPIRING - OUTPT PR ORB OI ORDERED - INPT PR ORB OI ORDERED - OUTPT PR ORB OI RESULTS - INPT PR ORB OI RESULTS - OUTPT PR
> A new notification is also being released with this patch: SUICIDE ATTEMPTED/ COMPLETED. This informational notification is triggered by Clinical Reminders when a
> MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in PCE. It is exported with package parameter values set as follows:
> . ORB ARCHIVE PERIOD - 30
> . ORB DELETE MECHANISM - Individual Recipient
> . ORB FORWARD BACKUP REVIEWER - No
> . ORB FORWARD SUPERVISOR - No
> . ORB FORWARD SURROGATES - No
> . ORB PROCESSING FLAG - Disabled
> . ORB PROVIDER RECIPIENTS - MHTC and PCMM Team (CM)
> . ORB URGENCY - High

### \*\*\*Important Note\*\*\*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Notifications are processed by IEN (internal entry number) from the OE/RR NOTIFICATIONS File \#100.9. Any site-defined notifications run the risk of being over- written by new notifications that are nationally released, especially those within the number range 1-9999, which is reserved for national release. If you have locally defined notifications, you may need to renumber them before this patch will install. Specifically, IEN \#77 is being added. See [Appendix B](#Appendix_B:_Instructions_for_Recreating/) for instructions on how to recreate or re-point site-defined notifications occupying a national number space.
> A validation routine is also added to the input transform of the NUMBER field (#.001) of the OE/RR Notifications File \#100.9. This validation routine will prohibit new national notification entries by the site and validate the correct local notification number scheme
> \<your site's station number\>\<incremental notification number 01-99\>.

### Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Clinical Reminders PXRM\*2\*24 Documentation
<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Manual</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Installation and Setup Guide</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_24_IG.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Release Notes</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_24_RN.PDF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>User Manual</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_UM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Manager’s Manual</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_MM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Health Summary GMTS\*2.7\*104 Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Manual</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>User Manual</p>
</blockquote></td>
<td><blockquote>
<p>HSUM_2_7_104_UM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Technical Manual</p>
</blockquote></td>
<td><blockquote>
<p>HSUM_2_7_104_TM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>
> TIU\*1\*265 Documentation
<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Manual</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Clinical Coordinator &amp; User Manual</p>
</blockquote></td>
<td><blockquote>
<p>TIUUM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Technical Manual</p>
</blockquote></td>
<td><blockquote>
<p>TIUTM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Scheduling SD\*5.3\*588 and Registration DG\*5.3\*849 Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Manual</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PIMS Technical Manual (contains SD and DG updates)</p>
</blockquote></td>
<td><blockquote>
<p>PIMSTM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Scheduling User Manual – Outputs Menu</p>
</blockquote></td>
<td><blockquote>
<p>PIMsSchOutput.pdf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Scheduling User Manual - Menus, Intro &amp; Orientation</p>
</blockquote></td>
<td><blockquote>
<p>PIMsSchIntro.pdf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient Record Flag User Guide</p>
</blockquote></td>
<td><blockquote>
<p>PatRecFlagUG.pdf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDDG Install Review Guide</p>
</blockquote></td>
<td><blockquote>
<p>SDDG_Install_Review.pdf</p>
</blockquote></td>
</tr>
</tbody>
</table>
> CPRS OR\*2.0\*348 Documentation
<table>
<colgroup>
<col style="width: 55%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Manual</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CPRS User Guide: GUI Version</p>
</blockquote></td>
<td><blockquote>
<p>CPRSGUIUM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPRS Technical Manual: GUI Version</p>
</blockquote></td>
<td><blockquote>
<p>CPRSGUITM.PDF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPRS Technical Manual</p>
</blockquote></td>
<td><blockquote>
<p>CPRSLMTM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Related Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 32%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SITE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>URL</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>National Clinical</p>
<p>Reminders site</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Contains manuals, presentations, and information about Clinical Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>National Clinical</p>
<p>Reminders Committee</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>This GROUP directs the development of new and revised national reminders</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistA Document Library</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Contains manuals for Clinical</p>
<p>Reminders and related applications.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### We recommend that the team members who will be responsible for implementing this project coordinate with each other before installing the patches, to determine the first three pre-install steps. This team could include MH coordinators, Suicide Prevention Coordinators, Clinical Application Coordinators (CACs), Reminders Managers, and IRM staff.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Make sure that the regular Scheduling Background Job \[SDAM BACKGROUND JOB\] has been scheduled, so that the High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] will be sent to appropriate staff.

> NOTE: your site should not *specifically* schedule the SD MH NO SHOW NIGHTLY BGJ. It should be running automatically at the time when the SDAM BACKGROUND JOB runs each night to process the appointments.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2.  Determine the name of the Mail Group Owner for the new Mail Group DGPF CLINICAL HR FLAG REVIEW. Note: The new DGPF CLINICAL HR FLAG REVIEW mail group will also be used to send a message to its members when the patient’s flag needs to be reviewed following existing PRF review processes

> (continue/inactivate/delete). During the DG\*5.3\*849 install, the installer will be asked to enter a name for the Mail Group Owner. *We recommend that a CAC and/or an MH/SPC representative be present during the install, to answer this question.* This prompt appears during the installation:

> The owner assigned will be responsible for entering the names of Suicide Prevention Coordinators (SPCs) and/or other MH professionals into the Mail Group. Sites can decide who this owner should be – an IRM staff member, a CAC, or one of the MH-SPC team. Check to see if there’s a Mail Group expert at your site. NOTE: Self enrollment is not allowed for this mail group.

> This should be the Suicide Prevention Coordinator (or designee). This name should be available to the IRM staff prior to installing the patch.

3.  After the patch is installed, IRM will need to attach the new DGPF LOCAL TO NATIONAL CONVERT option to the appropriate menu for the Suicide Prevention Coordinator (or designee). The Suicide Prevention Coordinator (or designee) will need to populate the DGPF CLINICAL HR FLAG REVIEW mail group with members as needed. This mail group will receive the reports and any error messages generated by the local-to-national PRF processing and will also receive messages when a patient’s PRF needs to be reviewed.
4.  Have the local Suicide Prevention Coordinator evaluate your local PRF entries and make any changes for the PRF conversion of local Category II flags to national Category I flags. This should be done using the Report Only action in the DGPF LOCAL TO NATIONAL CONVERT option. As part of the post-patch processing, this patch installs a new national flag data entry (HIGH RISK FOR SUICIDE) into the PRF NATIONAL FLAG file (#26.15).
5.  If you have locally defined notifications, you may need to re-number them before this patch is installed. A new notification is being released with this patch: SUICIDE ATTEMPTED/ COMPLETED. This informational notification is triggered by Clinical Reminders when a MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in PCE. Notifications are processed by IEN (internal entry number) from the OE/RR NOTIFICATIONS File \#100.9. Any site-defined notifications run the risk of being overwritten by new notifications that are nationally released, especially those within the number range 1-9999, which is reserved for national release. Specifically, for this project, IEN \#77 is being added. If you have a locally defined notification with the IEN of 77, you will need to

### renumber it before this patch is installed. See [Appendix B](#Appendix_B:_Instructions_for_Recreating/) for instructions for recreating or re-pointing site-defined notifications.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

6.  The Reminder Definitions in this project look for the national category I HIGH RISK FOR SUICIDE patient record flag and the local category II patient record flag used at your site. The new term, VA-MH HIGH RISK FOR SUICIDE PRF, used in these reminders, looks for the local name HIGH RISK FOR SUICIDE, which is the first mapped finding in the Mapped Findings. The Computed Finding Parameter of HIGH RISK FOR SUICIDE^L means use the local patient record flag called HIGH RISK FOR SUICIDE. If your site uses a different category II patient record flag name, then the Computed Finding Parameter for the first mapped finding should be changed. For example, if your site uses SUICIDE RISK as the name of the category II patient record flag, then the computed finding parameter should be changed to SUICIDE RISK^L.

> Do not change the second mapped finding with the Computed Finding Parameter of HIGH RISK FOR SUICIDE^N.

### Required Software for PXRM\*2\*24

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package/Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Clinical Reminders PXRM*2*18 PXRM*2*22</p>
</blockquote></td>
<td><blockquote>
<p>PXRM</p>
</blockquote></td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEN. MED. REC. – VITALS</p>
<p>GMRV*5*25</p>
</blockquote></td>
<td><blockquote>
<p>GMRV</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Health Summary</p>
</blockquote></td>
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td><blockquote>
<p>2.7</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HL7</p>
</blockquote></td>
<td><blockquote>
<p>HL</p>
</blockquote></td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Kernel</p>
</blockquote></td>
<td><blockquote>
<p>XU</p>
</blockquote></td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Kernel Toolkit</p>
<p>XT*7.3*111</p>
</blockquote></td>
<td><blockquote>
<p>XT</p>
</blockquote></td>
<td><blockquote>
<p>7.3</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MailMan</p>
</blockquote></td>
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
<td><blockquote>
<p>Mental Health Assistant (MHA)</p>
<p>YS*5.01*103 + MH dlls</p>
</blockquote></td>
<td><blockquote>
<p>YS</p>
</blockquote></td>
<td><blockquote>
<p>5.01</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NATIONAL DRUG FILE</p>
<p>PSN*4.0*176</p>
</blockquote></td>
<td><blockquote>
<p>PSN</p>
</blockquote></td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order Entry/Results Reporting</p>
</blockquote></td>
<td><blockquote>
<p>OR</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Pharmacy Data Management</p>
<p>PSS*1.0*133</p>
</blockquote></td>
<td><blockquote>
<p>PSS</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Outpatient Pharmacy</p>
<p>PSO*7.0*299</p>
</blockquote></td>
<td><blockquote>
<p>PSO</p>
</blockquote></td>
<td><blockquote>
<p>7.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Primary Care Management Module (PCMM)</p>
<p>SD*5.3*575</p>
</blockquote></td>
<td><blockquote>
<p>SD</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RADIOLOGY/NUCLEAR MEDICINE</p>
<p>RA*5*56</p>
</blockquote></td>
<td><blockquote>
<p>RA</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Registration</p>
</blockquote></td>
<td><blockquote>
<p>DG</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DG*5.3*836</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Scheduling</p>
<p>SD*5.3*583</p>
</blockquote></td>
<td><blockquote>
<p>SD</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA FileMan</p>
</blockquote></td>
<td><blockquote>
<p>DI</p>
</blockquote></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Required Software for DG\*5.3\*836

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package/Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Registration/Enrollment</p>
</blockquote></td>
<td><blockquote>
<p>DG</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient Record Flags Phase III</p>
<p>DG*5.3*650</p>
</blockquote></td>
<td><blockquote>
<p>DG</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

### Required Software for SD\*5.3\*578

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package/Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Scheduling</p>
</blockquote></td>
<td><blockquote>
<p>SD</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Required Software for GMTS\*2.7\*99

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package/Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Health Summary</p>
</blockquote></td>
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td><blockquote>
<p>2.7</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Required Software for TIU\*1\*260

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package/Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Text Integration Utilities</p>
</blockquote></td>
<td><blockquote>
<p>TIU</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Required Software for OR\*3\*348

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package/Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Primary Care Management Module</p>
<p>(PCMM)</p>
</blockquote></td>
<td><blockquote>
<p>SD</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order Entry/Results Reporting OR*3*243</p>
<p>OR*3*280 OR*3*296</p>
</blockquote></td>
<td><blockquote>
<p>OR</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

### Estimated Installation Time: 10-15 minutes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual describes how to install the combined build that includes builds DG\*5.3\*849, SD\*5.3\*588, GMTS\*2.7\*104, TIU\*1.0\*265, OR\*3.0\*348, and PXRM\*2.0\*24.

> This build can be installed with users on the system, but it should be done during non-peak hours.

> *The installation needs to be done by a person with DUZ(0) set to "@."*

> NOTE: We recommend having a Clinical Reminders Manager or Clinical Applications Coordinator (CAC) present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.

1.  <span id="1._Retrieve_the_host_file_containing_the" class="anchor"></span>Retrieve the host file containing the multi-package build, HIGH RISK MH 2.0. Use ftp to access the build (the name of the host file is HIGH_RISK_MH_2_0 .KID) from one of the following locations (with the ASCII file type):

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

### Install the build first in a training or test account.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

### Load the distribution.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and HIGH_RISK_MH_2.0.KID at the Host File prompt.

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

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 42%" />
<col style="width: 20%" />
<col style="width: 2%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PACKAGE:</p>
</blockquote></th>
<th><blockquote>
<p>SD*5.3*588</p>
</blockquote></th>
<th><blockquote>
<p>Dec 11, 2012 2:04 pm</p>
</blockquote></th>
<th>PAGE</th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SD53588P</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="4"><blockquote>
<p>6953359</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDAMQ</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="4"><blockquote>
<p>9860749</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDMHAD</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="4"><blockquote>
<p>116008938</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDMHAD1</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="4"><blockquote>
<p>108729141</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDMHAP</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="4"><blockquote>
<p>89393379</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDMHAP1</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="4"><blockquote>
<p>16336515</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDMHNS</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="4"><blockquote>
<p>22141437</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDMHNS1</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="4"><blockquote>
<p>101585316</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 45%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>GMTSMHRF Calculated</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>7698174</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>GMTSMHTC Calculated</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>7727408</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>GMTSY104 Calculated</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>9611824</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>3 Routines checked, 0 failed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PACKAGE:</p>
</blockquote></td>
<td><blockquote>
<p>OR*3.0*348</p>
</blockquote></td>
<td><blockquote>
<p>Dec 11, 2012 2:04 pm</p>
</blockquote></td>
<td><blockquote>
<p>PAGE 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORB3</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="2"><blockquote>
<p>97635419</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORB3SPEC</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="2"><blockquote>
<p>93913902</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORBINPTR</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="2"><blockquote>
<p>1813250</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORBPRCHK</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="2"><blockquote>
<p>32589157</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORY348</p>
</blockquote></td>
<td>Calculated</td>
<td colspan="2"><blockquote>
<p>13557254</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>PACKAGE: PXRM*2.0*24 Dec 11, 2012 2:04 pm PAGE 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PXRM</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>37992293</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRMCDEF</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>2284758</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRMDATE</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>69746461</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRMDEDT</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>86390747</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRMDEV</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>78211075</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRMDUTL</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>9494253</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRMEXFI</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>53496841</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRMEXIC</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>80167234</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRMEXID</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>65987316</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PXRMEXIU</p>
</blockquote></th>
<th>Calculated</th>
<th>66069083</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PXRMEXLM</p>
</blockquote></td>
<td>Calculated</td>
<td>46743705</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRMEXPS</p>
</blockquote></td>
<td>Calculated</td>
<td>192149462</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRMEXSI</p>
</blockquote></td>
<td>Calculated</td>
<td>40410891</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRMFF</p>
</blockquote></td>
<td>Calculated</td>
<td>65126590</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRMICHK</p>
</blockquote></td>
<td>Calculated</td>
<td>132138736</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRMLOCF</p>
</blockquote></td>
<td>Calculated</td>
<td>95753792</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRMLPOE</p>
</blockquote></td>
<td>Calculated</td>
<td>14864405</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRMMSER</p>
</blockquote></td>
<td>Calculated</td>
<td>106782052</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRMNTFY PXRMP24E</p>
</blockquote></td>
<td><blockquote>
<p>Calculated Calculated</p>
</blockquote></td>
<td><blockquote>
<p>3662059</p>
<p>2321342</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PXRMPCMM Calculated</p>
</blockquote></td>
<td>11797305</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PXRMPDEM Calculated</p>
</blockquote></td>
<td>65842415</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PXRMPINF Calculated</p>
</blockquote></td>
<td>8130614</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PXRMRDI Calculated</p>
</blockquote></td>
<td>38535019</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PXRMSCR Calculated</p>
</blockquote></td>
<td>88295</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PXRMTAX Calculated</p>
</blockquote></td>
<td>65791721</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PXRMUTIL Calculated</p>
</blockquote></td>
<td>113964494</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PXRMVSIT Calculated</p>
</blockquote></td>
<td>10650656</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PXRMXQUE Calculated</p>
</blockquote></td>
<td>12328074</td>
</tr>
</tbody>
</table>

### Install the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build HIGH RISK MH 2.0 .KID and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompt: Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE: We recommend that you do not queue the install.

### Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See [<u>Appendix A</u>](#appendix-a-installation-examples).

### Install File Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

### Build File Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

### Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/019.png) As part of the post-patch processing, DG\*5.3\*849 installs a new national flag data entry into the PRF NATIONAL FLAG file (#26.15). This data entry is the HIGH RISK FOR SUICIDE national flag. Once it’s been established that the flag has been correctly installed into the file, the post-install routine should be deleted.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/020.png) GMTS\*2.7\*104 contains a routine (GMTSY104) that will perform an environment check and update the DESCRIPTION field of the HEALTH SUMMARY COMPONENT file (142.1) entry for MH HIGH RISK PRF HX (post-install).

> GMTSY104 can be deleted after successful installation.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/021.png) TIU\*1.0\*265 consists of one post-install routine that will install the new title into the TIU DOCUMENT DEFINITION file (#8925.1). A message will be written to screen and also captured in the install log as to whether or not the title was successfully created. If a title already exists with the same name, it will be overwritten by the new title.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/022.png) The routine TIUPS265 contains the POST-install actions for this patch.

> This routine may be deleted from the system if storage space is a concern. Local IT staff should consider keeping a copy of TIUPS265 as it may prove useful in the event of any unexpected issues with this patch.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/023.png) OR\*3.0\*348 contains one post-install routine (ORY348) that will install the new SUICIDE ATTEMPTED/COMPLETED notification and its associated package parameter values as mentioned under the OR\*3.0\*348 section of the Introduction. ORY348 can be deleted after successful installation.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/024.png) SD\*5.3\*588 contains one post-install routine (SD53588P) that adds two new parameters to the PARAMETERS (#8989.5) file with associated parameter definitions added to the PARAMETER DEFINITION (#8989.51) file. The new parameter SDMH PROACTIVE DAYS stores a value that will list for future appointments the number of days stored in the parameter, for each patient on the High Risk MH Proactive Adhoc Report and High Risk MH Proactive Nightly Report. This parameter is checked when the SD MH PROACTIVE BGJ REPORT is run. The second new parameter is SDMH NO SHOW DAYS which also stores a value that will list for future appointments the number of days stored in the parameter, for each patient on the SD MH NO SHOW NIGHTLY BGJ Report. The default value of 30 days will be populated by the post-install routine for both parameters. Sites may

> change the number of days stored in the parameter, within the range of 1 to 30, SD53588P can be deleted after the install.

# Post-Install Set-up Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The person(s) responsible for making the assignment is listed in parentheses after the step.

1.  Assign SPCs to the User Class DGPF PATIENT RECORD FLAGS MGR. *(CAC)*
    1.  To write a PRF note for a category I flag, the user must belong to the DGPF PATIENT RECORD FLAG MGR user class. Each site will be responsible for populating this user class.
    2.  The new HIGH RISK FOR SUICIDE title is in the existing Document Class PATIENT RECORD FLAG CAT I, and the existing business rule applies to that Document Class, so the rule applies to the new title automatically.

### Business Rule:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example of USR CLASS MANAGEMENT for current Category I TIU Standard Note Title:

2.  Assign Mental Health Treatment Coordinators in the Patient Care Management Module (PCMM). See the [<u>PCMM MHTC User Manual</u>](http://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/pcmmmhtcug.pdf) for instructions. *(MH PCMM Coordinator)*
3.  Assign MHTCs to appropriate patients. See the PCMM MHTC User Manual for an example. *(MH PCMM Coordinator*). A new reminder called VA-MHTC NEEDS ASSIGNMENT can help Mental Health staff identify patients that need an MHTC to be assigned.
4.  Attach the new DGPF LOCAL TO NATIONAL CONVERT option to the appropriate menu for the Suicide Prevention Coordinator (and/or Mental Health designee). This should be the SPC or MH designee that will be running the report-only and processing steps in the DGPF LOCAL TO NATIONAL CONVERT option. When the Process Local to National step is run, all new automatically created Category I HIGH RISK FOR SUICIDE PRFs will include this individual’s name in each patient’s PRF activity narrative. It is better to use a Mental Health person. *(IRM)*
5.  Attach the existing DGPF TRANSMISSION MGMT option to the appropriate menu for the Suicide Prevention Coordinator (or designee) to track HIGH RISK FOR SUICIDE assignments that could not be updated at one of the patient’s other Treating Facilities. *(IRM)*
6.  Add Suicide Prevention Coordinators names to the DGPF CLINICAL HR FLAG REVIEW Mail group. *(Mail group owner)*

> The Mail Group Owner of the DGPF CLINICAL HR FLAG REVIEW Mail Group (as entered during the installation process) will need to add these names after the multi- package build is installed. The Mail Group members added to this Mail Group will receive the reports in a MailMan Message. This can include all facility SPCs if you’re an integrated site.

> NOTE: The DGPF CLINICAL HR FLAG REVIEW Mail Group is not used to document PRF Transmission Errors. It is also used to let Mail Group members know the patient’s PRF is due for a review.

### Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

7.  Select the Convert Local HRMH PRF to National option. Select Report Only. The actual conversion (P option) should only be run after notification from the national Office of Mental Health Services (30 days after the package release), to minimize transmission error messages among sites with shared patients. These errors occur when one of these sites has installed and runs the conversion, but another site that sees the same patient hasn’t installed the software. *(SPC)*

> When run in the report mode, reports will be generated and sent via MailMan to the new DGPF CLINICAL HR FLAG REVIEW mail group, showing which local PRFs can be processed, which ones may have potential errors needing to be corrected first, and which ones may need to be processed manually.

> Select OPTION NAME: DGPF LOCAL TO NATIONAL CONVERT Convert Local HRMH PRF

> to National action

> Convert Local HRMH PRF to National

> This option can be run in a report only mode which will provide a report of what actions the local-to-national processing will perform. Enter 'R' to run the Report Only mode, or 'P' to begin the local-to-national PRF processing.

> Select one of the following:

> R Report Only

> P Process Local-to-National

> Select which mode to run: R//Report Only

> ...SORRY, JUST A MOMENT PLEASE...

> \>\> Results have been sent to the 'DGPF CLINICAL HR FLAG' mail group

> Subj: Pre-report National Flag Create 8/1/12@15:42 \[#64240\] 08/01/12@15:42

> 44 lines

> From: HRMH PRF GENERATE JOB In 'IN' basket. Page 1 Priority!

> Pre-scan summary from Local to National flag processing job Run date: Aug 01, 2012@15:42:06

> Started by: MHPROVIDER,SIX

> Summary of PRF Processing:

<table>
<colgroup>
<col style="width: 90%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Total active Cat II flag assignments:</p>
</blockquote></th>
<th>12</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Cat I flags created:</p>
</blockquote></td>
<td>5</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Potential errors Found:</p>
</blockquote></td>
<td>5</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cat II flags requiring manual action:</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Found active Cat I and Cat II flags:</p>
</blockquote></td>
<td>2</td>
</tr>
</tbody>
</table>

> =============================================================================

> Processing Results:

> Invalid DFN's or Patient File errors

> No DFN errors were found

> Patients with Local ICN (National ICN Required) Name Local ICN

> AWHPATIENT,FEMALEFIFTEEN (0015) 6600000145V816164

> CRPATIENT,ONE (2222) 6600000120V652113

> MHPATIENT,TWO (0011) 6600000105V932329

> National Flag assigned and Local still active

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 34%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Name</p>
</blockquote></th>
<th><blockquote>
<p>CMOR</p>
</blockquote></th>
<th><blockquote>
<p>Owning Site</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CRPATIENT,TWO (4444)</p>
</blockquote></td>
<td><blockquote>
<p>SALT LAKE CITY OIFO</p>
</blockquote></td>
<td><blockquote>
<p>SALT LAKE CITY HCS</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Patients flagged for manual processing</p>
<p>Name CMOR Description</p>
<p>No records needing manual intervention found</p>
<p>Other Errors which may have prevented conversion Name Description</p>
<p>No other errors found</p>
</blockquote></td>
</tr>
</tbody>
</table>

8.  Allocate the DGPF TRANSMISSIONS key to SPCs on your VistA system. At a minimum, it should be provided to the same SPC who runs the convert option. The SPCs will be using this key for access to the DGPF TRANSMISSION MGMT menu option. *(IRM)*

> DGPF TRANSMISSIONS key description

9.  Add the DGPF TRANSMISSION MGMT menu option to the same users as above. (This option will only be assigned to a few staff at your site – it should be provided to the same SPC who runs the convert option). The Record Flag Transmission Errors option on this menu will be used by sites that have multi-treating facilities and will be sharing Category I PRF assignment information. *(IRM)*

### Record Flag Transmission Errors option description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

10. Add users to the DGPF HL7 TRANSMISSION ERRORS Mail Group. These should be the same users who were given the DGPF Transmissions Security Key and access to the DGPF Transmission MGMT option. Recipients will receive any error messages generated by the local-to-national PRF processing. Messages sent to the user will need to be checked for the reject reason of “Record Flag is already assigned to patient,” so that they can coordinate with the other site that is also owner of the Cat I HIGH RISK FOR SUICIDE record.

### Scenarios that can cause the transmission errors:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1)  Assigning the new Category I HIGH RISK FOR SUICIDE flag to a patient BEFORE all sites have installed the patch bundle, or
2)  Running the Convert option BEFORE all sites have installed the patch bundle.

> In either case, the PRF assignments will not be lost to the other sites because the assignment is waiting to be re-transmitted to sites.

> For example, if site A runs the convert process step prior to others installing the software, each Category II flag for suicide risk will be converted to the Category I flag on the Site A system using the review date and ownership facility from the source Category II flag. For each Category I created, the patient’s treating facilities of record will be sent an update using the existing PRF Transmission management system where normal protocol can be used to resolve issues between sites.

> If site B does not have the bundle installed, then site A receives a transmission error back in the PRF transmission management option that informs the SPC that the Category I flag could not be updated at the site.

> The SPC will coordinate with Site B so that when Site B completes its install, the SPC at Site A could manually reprocess the transmission to Site B. which would update Site B with the Category I.

> If site B had the Category II PRF active, it would remain active until the site B SPC runs the conversion on the site B system.

> Waiting the 30 days relieves the SPCs of having to coordinate with each unique patient/ site combination that receives a transmission error.

11. The HIGH RISK FOR SUICIDE national flag uses a new Text Integration Utility (TIU) Progress Note (PN) title that is installed by patch TIU\*1.0\*265; Patient Record Flag CATEGORY I - HIGH RISK FOR SUICIDE. If, for some reason, this Progress Note Title is not available, the HIGH RISK FOR SUICIDE national flag will not be installed. In this case, you will need to manually install it, by running the post-install routine from the programmer prompt (\>D EN^DG53849P).
12. If your site is using the Reminder dialog template, SUICIDE HIGH RISK PRF DOCUMENTATION, make the following changes:
    1.  Change Category II to Category I.
    2.  The CACs will need to temporarily assign themselves the ASU User class of DGPF PATIENT RECORD FLAGS MGR. This user class allows the CAC to see the Patient Record Flag Category I –High Risk for Suicide title and attach the reminder dialog if desired.

> It is not required to use health factors with the Category I PRF—the national PRF data is extractable. However, if you want to link the existing template that captures health factors to the new TIU note title, you can do this.

13. Enable the new informational notification released with this patch, SUICIDE ATTEMPTED/ COMPLETED, which is triggered by Clinical Reminders when an MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in PCE. IRM will need to enable this at the System level.
    1.  Assign SPC users as recipients to this notification. Note: MHTC should already be set up as a default recipient type for Suicide Attempted/Completed.
    2.  Add ‘C’ (MHTC) to the default recipient list for other notification types (Admission, Discharge, …) as deemed necessary.
    3.  Other Notification Types enabled on your system that are identified as appropriate to notify the patient’s assigned MHTC. (e.g., Admission, Discharge, ….) will need to be manually defined as needed.

> NOTE: An ORB PROVIDER RECIPIENT parameter value of “CM” is exported with the Suicide behavior notification. Therefore, the suicide behavior notification will be sent to the MHTC and PCMM Mental Health team if any are set up and configured at the site. Directions on how to set those up should be contained in a setup manual created by the sister project, Principal Mental Health Provider. See the Primary Care Management Module (PCMM) – Mental Health Treatment Coordinator (MHTC) User Manual (pcmmmhtcug.pdf) for more information.

### Set of codes indicating default provider recipients of a notification by their title or relationship to the patient.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Notifications can be set up with any or all of the following codes:

4.  Once all the set-up is done, you can verify this via the following menu:

> Notification Mgmt Menu menu

1.  Enable/Disable Notifications
2.  Erase Notifications
3.  Set Urgency for Notifications (GUI)
4.  Set Deletion Parameters for Notifications
5.  Set Default Recipient(s) for Notifications
6.  Set Default Recipient Device(s) for Notifications
7.  Set Provider Recipients for Notifications
8.  Flag Orderable Item(s) to Send Notifications
9.  Archive(delete) after \<x\> Days
10. Forward Notifications ...
11. Set Delays for Unverified Orders ...
13. Send Flagged Orders Bulletin
14. Determine Recipients for a Notification
15. Display Patient Alerts and Alert Recipients
16. Enable or Disable Notification System
17. Display the Notifications a User Can Receive

> Select Notification Mgmt Menu Option: 14 Determine Recipients for a Notification

> PATIENT (req'd): MHPATIENT,ONE 5-5-55 555121255

> YES SC VETERAN

> Enrollment Priority: GROUP 1 Category: IN PROCESS End Date:

> NOTIFICATION (req'd): SUICIDE ATTEMPTED/COMPLETED

> Processing, please stand by... DEVICE: HOME// ;;9999 HOME

> DETERMINE NOTIFICATION RECIPIENTS REPORT Page: 1

> Processing notification: SUICIDE ATTEMPTED/COMPLETED for patient: MHPATIENT,ONE

14. Check the DG Parameter Definition setup for the PRF FOR SUCIDE PREVENTION. If your site has a different name for this PRF, you’ll need to go into the Parameter Tools option (XPAR MENU TOOLS) to change this. NOTE: You may need programmer access to use this option, depending on how your site has assigned menus and options.
15. If desired, change the number of days for future appointments that will appear on the SD MH NO SHOW NIGHTLY BGJ Report and the SD MH PROACTIVE BGJ REPORT.

> These can be changed in the new parameters SDMH PROACTIVE DAYS and SDMH NO SHOW DAYS. The default value is 30 days for both parameters. The SD NO SHOW NOTIFICATION mail group that was installed with the previous patch SD\*5.3\*578 will receive the SD MH PROACTIVE BGJ REPORT.

> *Example:*

16. IRM staff will need to attach the High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] and High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] menu options to an appropriate menu for the Suicide Prevention Coordinator, or to a menu at the local suicide prevention staff’s discretion.
17. Use the same name entered in the Parameter Definition to complete an update to the reminder term. For the reminder definition VA-MH HIGH RISK NO-SHOW FOLLOW- UP, the term VA-MH HIGH RISK FOR SUICIDE PRF needs to be reviewed, and if the local Suicide flag name is not HIGH RISK FOR SUICIDE, the term needs to be updated to the local name.

### Set up a Reminders Due report template for SPCs.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A new reminder called VA-MHTC NEEDS ASSIGNMENT is available that can be used from CPRS to evaluate and display on the Cover Sheet’s Reminders Due section when the patient is a candidate for MHTC assignment. In order to be an MHTC candidate, the patient must have had three completed MH appointments within the past year, and not have an MHTC assigned to the patient.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/025.png)The reminder definition uses the new VA-PCMM MHTC computed finding. There is no reminder dialog related to this reminder.

> Uses Reminder Term VA-MH APPTS FOR MHTC ASSIGNMENT, which uses a new Reminder Location List called VA-MHTC APPT STOP CODES LL in the Computed Finding VA-Appointments for a Patient.

### ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/026.png) The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/027.png) This reminder can also be used from Reminder Reporting options/Reminders Due Report. Reminder CACs can create a Reminders Due Report (User) template for an SPC user to get the list of patients who are scheduled for a MH appointment next week and are candidates for MHTC. MHTCs, SPCs, or other MH Professionals should work with their Reminders Manager or Reminders CAC to set up the Reminders Due report criteria in a template, based on report criteria for SPC users. The report criteria should specify facility (or facilities), stop codes (e.g., 502) or hospital locations (selected Mental Health locations), future appointments or completed visits, and the VA-MHTC NEEDS ASSIGNMENT reminder.

### Ensure that the new health summary types have been added to the CPRS Reports tab display. (This should’ve been done as part of the installation and setup of Phase 1 of the HRMHP project, which was released in March 2012.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow your facility’s rules and conventions for adding these health summary types.

1.  VA-MH HIGH RISK PATIENT - This Type contains the four Health Summary Components mentioned above, and is the basis for creating the VA-MH HIGH RISK PATIENT (TIU) Health Summary Object.
2.  REMOTE MH HIGH RISK PATIENT - This Type contains the same components as the VA-MH HIGH RISK PATIENT and allows viewing the aforementioned information from remote sites.

> Sequencing new Health Summary types is done in the GUI Parameters option.

> Example: Sequencing new Health Summary types in Parameters option

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>Select CPRS Manager Menu Option: <strong>PE</strong> CPRS Configuration (Clin Coord) Select CPRS Configuration (Clin Coord) Option: <strong>GP</strong> GUI Parameters</p>
<p>Select GUI Parameters Option: <strong>HS</strong> GUI Health Summary Types Allowable Health Summary Types may be set for the following:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>User</p>
</blockquote></td>
<td>USR</td>
<td><blockquote>
<p>[choose from NEW PERSON]</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td>DIV</td>
<td><blockquote>
<p>[choose from INSTITUTION]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td>SYS</td>
<td><blockquote>
<p>[TEST.FO-SLC.MED.VA.GOV]</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>SVC</td>
<td><blockquote>
<p>[choose from SERVICE/SECTION]</p>
</blockquote></td>
</tr>
</tbody>
</table>

### When notified by the Office of Mental Health Services, run the Convert Local HRMHP PRF to National option - Process mode.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the Convert Local HRMHP PRF to National option is run in the processing mode, the actual processing and auto-creation of the national PRFs from the local PRFs will take place and messages will be sent out to summarize the process results. The local PRF for the patient will be inactivated. Note: Category I PRFs that are auto-created from this option will not have a Progress Note related to them.

> The Process Mode can be re-run as needed if a patient had an error that is resolved. Each time the process mode is run the active local PRFs that are found will be processed.

> The process to generate the new national (category I) PRFs from the local (category II) PRFs consists of determining whether a national PRF can be created from existing, active, local PRFs for suicide prevention.

> If there is any issue with generating a national PRF, either an error message will be logged, or the record will be reported as needing manual action by the suicide prevention coordinator (SPC).

> If a new national PRF can be created, the information from the local PRF will be used in creating the new national PRF with a generated activity narrative using the name of the SPC running the process mode..

> Upon successful creation of the new national PRF, the local PRF will be inactivated with a comment indicating that a new national PRF has been created and the existing HL7 messaging functionality will be used to transmit the national PRF information to other known treating facilities, as is currently done when a National PRF is entered through the Patient Record Flag assignment menu.

> See the PRF User Manual for more information about the Patient Record Flag options and the PRF Transmission key (DGPF TRANSMISSIONS KEY).

### Ownership of Category I flag determined at assignment and when Process Mode is run:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The first site that runs the Process mode that creates a Category I flag for a particular patient becomes the Owning site for that Category I flag. Each Category I flag assignment to a specific patient’s record is owned by a single facility. The facility that placed the Category I flag on the patient’s record would normally own and maintain the flag. The site that owns the Category I flag is the only site that can:

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/028.png)Review whether to remove or continue the flag Edit the flag

> Inactivate the flag Reactivate the flag

> Mark the flag as entered in error Change ownership of the flag

> Enter a Patient Record Flag Category I progress note for the flag

> However, ownership of a Category I flag assignment can be transferred. If a patient received the majority of care at a different VA facility than the one that assigned the flag, the site giving the majority of care could request that ownership of the flag be transferred to that site. The owning site could then change the ownership to the second site through the PRF software in List Manager.

### Example of a transmission error logged at the site that originated the Category I flag (“owner” site) for a patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this example, a transmission error was created when the first site processed the auto- created flag but one of the patient’s treating facility sites had not installed the patch bundle. The “Assignment Transmitted To” will be the site that could not be updated because the Category I flag has not been installed on the VistA system at the transmitted to site.

> In this case, the Category I flag did not update at the Transmitted To site. The only site that knows about the issue via the transmission error is the site that ran the Process Mode. The Transmitted To site does not receive an error message.

> The DGPF Transmission Management options should be visited regularly by SPCs to guide them on which sites need manual transmission of a patient’s Category I flag to update another site, and which site needs to be coordinated with to determine ownership of the Category I flag.

# Back-Out Plan for Production Environment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HRMHP project, Phase II, contains a bundle with six VistA patches: DG\*5.3\*849, SD\*5.3\*588, TIU\*1.0\*265, PXRM\*2.0\*24, GMTS\*2.7\*104, and OR\*3\*348.

> Sites are encouraged to create a back-up of all routines as a KIDS pre-install step when installing the Phase II bundle. This back-up of routines will cover restoration of routines from all packages if a back-out is necessary.

> NOTE: The efficiency of the Back-Out Plan diminishes over time. At some point the VistA recovery process will need to be implemented.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/029.png)![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/030.png)File content changes in these builds:

> DG\*5.3\*849: Adds a new Category I Patient Record Flag, HIGH RISK FOR SUICIDE.

> Also adds a new conversion option that one or two people will be accessing on local systems. The options can be removed from these users’ option menus if a back-out is needed.

> The PRF conversion process must be manually initiated from the new option. It will not be initiated when the bundle is installed, which puts each site in control of when the new conversion options are run. If the conversion option is run before a back-out becomes necessary, the Patient Record Flag (PRF) conversion process is not reversible, but a local Category II High Risk for Suicide PRF flag that was de-activated for a patient can be manually reactivated with the Local Category II flag, and the national Category I HIGH RISK FOR SUICIDE PRF can be de-activated for a patient.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/031.png) SD\*5.3\*588: Adds new SD options to help proactively follow-up with patients before the MH appointment occurs. These options can be removed from SPC/MH Professional users’ menus. A new nightly protocol is added that is run by the SD Background Job protocol event. The nightly protocol can be removed from the SD Background Job’s protocol event if a back-out is needed.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/032.png) TIU\*1.0\*265: Updates a national note title. The existence of the new entry in the TIU file will not cause a problem if a back-out is necessary.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/033.png) PXRM\*2.0\*24: Updates an existing reminder and dialog and adds new one. The HRMHP Phase I released bundle contains post-install Reminder Exchange entries that can be used to install over the existing reminder and dialog if a back-out is needed. The new reminder can be removed from all cover sheet reminder parameter lists if a back-out is needed.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/034.png) GMTS\*2.7\*104: Updates the description for a health summary component, to reflect the local Cat II and national Cat I PRF history that is displayed for High Risk for Suicide. No back-out required.

> ![](pxrm-2-24-high-risk-mental-health-patient-phase-2-installation-setup-guide/035.png) OR\*3\*348: Updates a provider recipient parameter to include a new provider recipient (MHTC) for notification parameter setup. Adds a new notification type that is distributed with a disabled status, with instructions to enable in the post install. If a back-out is needed, the notification type can be disabled, and all notification types that have default provider recipients that include “C” should remove the “C” from the default provider recipients.

> See patch descriptions for exact names of file content changed. Reverse the post-install steps described in the install and set-up instructions, to remove access to new Options, Mail Groups, the Security Key, and Clinical Reminders.

> Other than the steps outlined above for back-out, any additional back-out coding is not feasible and could cause more issues that it resolves. Back-out restoration from selective de- journaling is not possible. De-journaling from backups would negatively impact other applications and their valid data.

> The HRMHP development staff is available to support sites with the back-out steps above, if needed.

# Appendix A: Installation Examples 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### First-Time Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: We recommend that you not queue the install.

> Select Installation \<TEST ACCOUNT\> Option: Load a Distribution Enter a Host File: USER\$:\[ANONYMOUS\]HIGH_RISK_MH_2_0_T9.KID

> KIDS Distribution saved on Dec 07, 2012@10:16:34 Comment: High Risk Mental Health phase 2

> This Distribution contains Transport Globals for the following Package(s): HIGH RISK MH 2.0

> TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104 OR\*3.0\*348 PXRM\*2.0\*24

> Distribution OK!

> Want to Continue with Load? YES// Loading Distribution...

> HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588

> Build GMTS\*2.7\*104 has an Environmental Check Routine Want to RUN the Environment Check Routine? YES//

> GMTS\*2.7\*104

> Will first run the Environment Check Routine, GMTSY104

> CHECKING RECENT ADDITIONS TO HEALTH SUMMARY COMPONENT FILE

> Medication Worksheet (Tool \#2): OK MAS CONTACTS: OK

> MAS MH CLINIC VISITS FUTURE: OK MH HIGH RISK PRF HX: OK

> MH TREATMENT COORDINATOR: OK OR\*3.0\*348

> PXRM\*2.0\*24

> Use INSTALL NAME: HIGH RISK MH 2.0 to install this Distribution.

> Select Installation \<TEST ACCOUNT\> Option: BACKup a Transport Global Select INSTALL NAME: HIGH RISK MH 2.0 2/25/13@14:36:41

> =\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

> This Distribution was loaded on Feb 25, 2013@14:36:41 with header of High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34 It consisted of the following Install(s):

> HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

> OR\*3.0\*348 PXRM\*2.0\*24

> Subject: Backup of HIGH RISK MH 2.0 install on Feb 25, 2013 Replace

> Loading Routines for HIGH RISK MH 2.0. Routine PXRMP24I is not on the disk.. Loading Routines for TIU\*1.0\*265.

> Routine TIUPS265 is not on the disk.. Loading Routines for DG\*5.3\*849 Routine DG53849P is not on the disk.. Routine DGPFCNR is not on the disk.. Routine DGPFCNV is not on the disk.. Loading Routines for SD\*5.3\*588

> Routine SD53588P is not on the disk.....

> Routine SDMHAP is not on the disk.. Routine SDMHAP1 is not on the disk....

> Routine SDMHPRO is not on the disk.. Routine SDMHPRO1 is not on the disk.. Loading Routines for GMTS\*2.7\*104...

> Loading Routines for OR\*3.0\*348.. Routine ORBINPTR is not on the disk...

> Routine ORY348 is not on the disk.. Loading Routines for PXRM\*2.0\*24.....

> Routine PXRMDUTL is not on the disk..............

> Routine PXRMNTFY is not on the disk.. Routine PXRMP24E is not on the disk.. Routine PXRMP24I is not on the disk......

> Routine PXRMSCR is not on the disk......

> Send mail to: CRUSER, SIX// CRUSER, SIX Select basket to send to: IN// PATCH TEST And Send to:

> Select Installation \<TEST ACCOUNT\> Option: COMPARE Transport Global to Current System

> Select INSTALL NAME: HIGH RISK MH 2.0 2/25/13@14:36:41

> =\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

> This Distribution was loaded on Feb 25, 2013@14:36:41 with header of High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34 It consisted of the following Install(s):

> HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

> OR\*3.0\*348 PXRM\*2.0\*24

> Select one of the following:

1.  Full Comparison
2.  Second line of Routines only
3.  Routines only
4.  Old style Routine compare

> Type of Compare: 1 Full Comparison DEVICE: HOME// P

1.  P-LAB-MESSAGE-HFS HFS FILE
2.  P-MESSAGE-HFS (VXD) HFS FILE =\> MESSAGE
3.  P-RESMON IRM
4.  PACS1\$PRT COMPRESSED RADIOLOGY
5.  PACS1\$PRT LANDSCAPE RADIOLOGY
6.  PACS1\$PRT STANDARD RADIOLOGY
7.  PACS2\$PRT COMPRESSED A208E
8.  PACS2\$PRT STANDARD A208E
9.  PBOWES BRWCALL BRW MAIL ROOM
10. PBOWES BRWPREAPPT BRW MAIL ROOM Type '^' to Stop, or

> Choose 1-10\> 2 P-MESSAGE-HFS (VXD) HFS FILE =\> MESSAGE Subject: HIGH RISK MH 2.0 COMPARE

> Select one of the following:

> M Me

> P Postmaster

> From whom: Me//

> Send mail to: CRUSER, SIX // CRUSER, SIX Select basket to send to: IN// PATCH TEST And Send to:

> Moving to MailMan message...

> ..........................................................................

> ...

> ..........................................................................

> ...

> ....................

> Finished moving.

> Sending \[8150\]...

> Sent

> Select Installation \<TEST ACCOUNT\> Option: VERify Checksums in Transport Global

> Select INSTALL NAME: HIGH RISK MH 2.0 2/25/13@14:36:41

> =\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

> This Distribution was loaded on Feb 25, 2013@14:36:41 with header of High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34 It consisted of the following Install(s):

> HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

> OR\*3.0\*348 PXRM\*2.0\*24

> Want each Routine Listed with Checksums: Yes// YES DEVICE: HOME// SSH

> PACKAGE: HIGH RISK MH 2.0 Feb 25, 2013 2:38 pm PAGE 1

> GMTSY104 Calculated 9611824

> PXRMP24I Calculated 14301202

> 2 Routines checked, 0 failed.

> PACKAGE: TIU\*1.0\*265 Feb 25, 2013 2:38 pm PAGE 1

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 39%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>TIULO1</p>
</blockquote></th>
<th><blockquote>
<p>Calculated</p>
</blockquote></th>
<th>21084404</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TIUPS265</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>9608303</td>
</tr>
</tbody>
</table>

2.  Routines checked, 0 failed.

> PACKAGE: DG\*5.3\*849 Feb 25, 2013 2:38 pm PAGE 1

> DG53849P Calculated 7093789

> DGPFCNR Calculated 62901548

> DGPFCNV Calculated 95099109

3.  Routines checked, 0 failed.

> PACKAGE: SD\*5.3\*588 Feb 25, 2013 2:38 pm PAGE

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 37%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SD53588P</p>
</blockquote></th>
<th><blockquote>
<p>Calculated</p>
</blockquote></th>
<th>6953359</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SDAMQ</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>9860749</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDMHAD</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>116008938</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDMHAD1</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>108729141</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDMHAP</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>89393379</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDMHAP1</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>16336515</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDMHNS</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>22141437</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDMHNS1</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>101585316</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDMHPRO</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>15994772</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDMHPRO1</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>19699190</td>
</tr>
</tbody>
</table>

> 10 Routines checked, 0 failed.

> PACKAGE: GMTS\*2.7\*104 Feb 25, 2013 2:38 pm PAGE 1

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 40%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GMTSMHRF</p>
</blockquote></th>
<th><blockquote>
<p>Calculated</p>
</blockquote></th>
<th>7698174</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GMTSMHTC</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>7727408</td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMTSY104</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>9611824</td>
</tr>
</tbody>
</table>

> 3 Routines checked, 0 failed.

> PACKAGE: OR\*3.0\*348 Feb 25, 2013 2:38 pm PAGE 1

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>ORB3</th>
<th><blockquote>
<p>Calculated</p>
</blockquote></th>
<th><blockquote>
<p>97635419</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ORB3SPEC</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>93913902</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ORBINPTR</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>1813250</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ORBPRCHK</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>32589157</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ORY348</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td><blockquote>
<p>13557254</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 5 Routines checked, 0 failed.

> PACKAGE: PXRM\*2.0\*24 Feb 25, 2013 2:38 pm PAGE 1

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>PXRM</th>
<th><blockquote>
<p>Calculated</p>
</blockquote></th>
<th>37992293</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PXRMCDEF</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>2284758</td>
</tr>
<tr class="even">
<td>PXRMDATE</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>69746461</td>
</tr>
<tr class="odd">
<td>PXRMDEDT</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>86390747</td>
</tr>
<tr class="even">
<td>PXRMDEV</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>78211075</td>
</tr>
<tr class="odd">
<td>PXRMDUTL</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>9494253</td>
</tr>
<tr class="even">
<td>PXRMEXFI</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>53496841</td>
</tr>
<tr class="odd">
<td>PXRMEXIC</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>80167234</td>
</tr>
<tr class="even">
<td>PXRMEXID</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>65987316</td>
</tr>
<tr class="odd">
<td>PXRMEXIU</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>66069083</td>
</tr>
<tr class="even">
<td>PXRMEXLM</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>46743705</td>
</tr>
<tr class="odd">
<td>PXRMEXPS</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>192149462</td>
</tr>
<tr class="even">
<td>PXRMEXSI</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>40410891</td>
</tr>
<tr class="odd">
<td>PXRMFF</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>65126590</td>
</tr>
<tr class="even">
<td>PXRMICHK</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>132138736</td>
</tr>
<tr class="odd">
<td>PXRMLOCF</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>95753792</td>
</tr>
<tr class="even">
<td>PXRMLPOE</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>14864405</td>
</tr>
<tr class="odd">
<td>PXRMMSER</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>106782052</td>
</tr>
<tr class="even">
<td>PXRMNTFY</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>3662059</td>
</tr>
<tr class="odd">
<td>PXRMP24E</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>2321342</td>
</tr>
<tr class="even">
<td>PXRMP24I</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>14301202</td>
</tr>
<tr class="odd">
<td>PXRMPCMM</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>11797305</td>
</tr>
<tr class="even">
<td>PXRMPDEM</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>65842415</td>
</tr>
<tr class="odd">
<td>PXRMPINF</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>8130614</td>
</tr>
<tr class="even">
<td>PXRMRDI</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>38535019</td>
</tr>
<tr class="odd">
<td>PXRMSCR</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>88295</td>
</tr>
<tr class="even">
<td>PXRMTAX</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>65791721</td>
</tr>
<tr class="odd">
<td>PXRMUTIL</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>113964494</td>
</tr>
<tr class="even">
<td>PXRMVSIT</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>10650656</td>
</tr>
<tr class="odd">
<td>PXRMXQUE</td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>12328074</td>
</tr>
</tbody>
</table>

> 30 Routines checked, 0 failed.

> Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option:

> INstallation

> Select Installation \<TEST ACCOUNT\> Option: PRINT Transport Global Select INSTALL NAME: HIGH RISK MH 2.0 2/25/13@14:36:41

> =\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

> This Distribution was loaded on Feb 25, 2013@14:36:41 with header of High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34 It consisted of the following Install(s):

> HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

> OR\*3.0\*348 PXRM\*2.0\*24

> Select Installation \<TEST ACCOUNT\> Option: INstall Package(s) Select INSTALL NAME: HIGH RISK MH 2.0 2/25/13@14:36:41

> =\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

> This Distribution was loaded on Feb 25, 2013@14:36:41 with header of High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34 It consisted of the following Install(s):

> HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

> OR\*3.0\*348 PXRM\*2.0\*24

> Checking Install for Package HIGH RISK MH 2.0 Install Questions for HIGH RISK MH 2.0

> Checking Install for Package TIU\*1.0\*265 Install Questions for TIU\*1.0\*265

> Checking Install for Package DG\*5.3\*849 Install Questions for DG\*5.3\*849

> Incoming Mail Groups:

> Enter the Coordinator for Mail Group 'DGPF CLINICAL HR FLAG REVIEW': CARTER,DAVI

> D

> L DC 11CI CLINICAL APPLICATIONS COORD

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

> Checking Install for Package SD\*5.3\*588 Install Questions for SD\*5.3\*588

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// Checking Install for Package GMTS\*2.7\*104

> Will first run the Environment Check Routine, GMTSY104

> CHECKING RECENT ADDITIONS TO HEALTH SUMMARY COMPONENT FILE

> Medication Worksheet (Tool \#2): OK MAS CONTACTS: OK

> MAS MH CLINIC VISITS FUTURE: OK MH HIGH RISK PRF HX: OK

> MH TREATMENT COORDINATOR: OK

> Install Questions for GMTS\*2.7\*104

> Checking Install for Package OR\*3.0\*348 Install Questions for OR\*3.0\*348 Incoming Files:

> 100.9 OE/RR NOTIFICATIONS

> Note: You already have the 'OE/RR NOTIFICATIONS' File. Checking Install for Package PXRM\*2.0\*24

> Install Questions for PXRM\*2.0\*24 Incoming Files:

> 811.4 REMINDER COMPUTED FINDINGS (including data) Note: You already have the 'REMINDER COMPUTED FINDINGS' File. I will REPLACE your data with mine.

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// 0;80;99999 SSH

> Install Started for HIGH RISK MH 2.0 :

> Feb 25, 2013@14:47:35

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Feb 25, 2013@14:47:35

> Running Pre-Install Routine: MPBPRE^PXRMP24I Install Started for TIU\*1.0\*265 :

> Feb 25, 2013@14:47:35

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Feb 25, 2013@14:47:35

> Installing PACKAGE COMPONENTS:

> Installing PARAMETER DEFINITION

> Feb 25, 2013@14:47:36

> Running Post-Install Routine: ^TIUPS265

> Title Created: PATIENT RECORD FLAG CATEGORY I - HIGH RISK FOR SUICIDE

> Title attached to Document Class PATIENT RECORD FLAG CAT I Updating Routine file...

> Updating KIDS files...

> TIU\*1.0\*265 Installed.

> Feb 25, 2013@14:47:36

> Not a production UCI NO Install Message sent

> Install Started for DG\*5.3\*849 :

> Feb 25, 2013@14:47:36

> Build Distribution Date: Dec 07, 2012

> Installing Routines:

> Feb 25, 2013@14:47:36

> Installing PACKAGE COMPONENTS: Installing MAIL GROUP

> Installing OPTION

> Feb 25, 2013@14:47:36

> Running Post-Install Routine: ^DG53849P Installing new national PRF entry

> Installation of new national PRF entry complete Updating Routine file...

> Updating KIDS files...

> DG\*5.3\*849 Installed.

> Feb 25, 2013@14:47:36

> Not a production UCI NO Install Message sent

> Install Started for SD\*5.3\*588 :

> Feb 25, 2013@14:47:36

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Feb 25, 2013@14:47:36

> Installing PACKAGE COMPONENTS: Installing OPTION

> Installing PARAMETER DEFINITION

> Feb 25, 2013@14:47:36

> Running Post-Install Routine: ^SD53588P Updating Parameters File...

> SDMH PROACTIVE DAYS

> 89895006^Duplicate instance not allowed.

> SDMH NO SHOW DAYS

> 89895006^Duplicate instance not allowed.

> Updating Routine file... Updating KIDS files...

> SD\*5.3\*588 Installed.

> Feb 25, 2013@14:47:36

> Not a production UCI NO Install Message sent

> Install Started for GMTS\*2.7\*104 :

> Feb 25, 2013@14:47:36

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Feb 25, 2013@14:47:36

> Running Post-Install Routine: POST^GMTSY104

> Updating description for Health Summary Component MH HIGH RISK FOR SUICIDE Update Successful

> Updating Routine file... Updating KIDS files...

> GMTS\*2.7\*104 Installed.

> Feb 25, 2013@14:47:37

> Not a production UCI NO Install Message sent

> Install Started for OR\*3.0\*348 :

> Feb 25, 2013@14:47:37

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Feb 25, 2013@14:47:37

> Installing Data Dictionaries:

> Feb 25, 2013@14:47:37

> Installing PACKAGE COMPONENTS: Installing PARAMETER DEFINITION

> Feb 25, 2013@14:47:37

> Running Post-Install Routine: POST^ORY348

> Updating Routine file... Updating KIDS files...

> OR\*3.0\*348 Installed.

> Feb 25, 2013@14:47:37

> Not a production UCI NO Install Message sent

> Install Started for PXRM\*2.0\*24 :

> Feb 25, 2013@14:47:37

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Feb 25, 2013@14:47:38

> Running Pre-Install Routine: PRE^PXRMP24I DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries:

> Feb 25, 2013@14:47:38

> Installing Data:

> Feb 25, 2013@14:47:38

> Running Post-Install Routine: POST^PXRMP24I ENABLE options.

> ENABLE protocols.

> There are 5 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry VA-MH NO SHOW APPT CLINICS LL
2.  Installing Reminder Exchange entry VA-MHTC APPT STOP CODES AND EXCLUSION

> STOP

3.  Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW FOLLOW-UP
4.  Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW ADHOC RPT
5.  Installing Reminder Exchange entry VA-MHTC NEEDS ASSIGNMENT Renaming/inactivating health factors and terms that are no longer used.

> Updating Routine file... Updating KIDS files...

> PXRM\*2.0\*24 Installed.

> Feb 25, 2013@14:47:59

> Not a production UCI NO Install Message sent

> Running Post-Install Routine: POST^GMTSY104

> Updating description for Health Summary Component MH HIGH RISK FOR SUICIDE Update Successful

> Updating Routine file... Updating KIDS files...

> HIGH RISK MH 2.0 Installed.

> Feb 25, 2013@14:47:59

> No link to PACKAGE file PXRM\*2.0\*24

> Install Completed

> Installation after Previous Install

> Select Installation \<TEST ACCOUNT\> Option: Install Package(s) Select INSTALL NAME: HIGH RISK MH 2.0 12/10/12@11:06:05

> =\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

> This Distribution was loaded on Dec 10, 2012@11:06:05 with header of High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34 It consisted of the following Install(s):

> HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104 OR\*3.0\*348 PXRM\*2.0\*24

> Checking Install for Package HIGH RISK MH 2.0 Install Questions for HIGH RISK MH 2.0

> Checking Install for Package TIU\*1.0\*265 Install Questions for TIU\*1.0\*265

> Checking Install for Package DG\*5.3\*849 Install Questions for DG\*5.3\*849

> Incoming Mail Groups:

> Enter the Coordinator for Mail Group 'DGPF CLINICAL HR FLAG REVIEW': CRDEVELOPER,ONE OC OI&T STAFF

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<Enter\> Checking Install for Package SD\*5.3\*588

> Install Questions for SD\*5.3\*588

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<Enter\> Checking Install for Package GMTS\*2.7\*104

> Will first run the Environment Check Routine, GMTSY104

> CHECKING RECENT ADDITIONS TO HEALTH SUMMARY COMPONENT FILE

> Medication Worksheet (Tool \#2): OK MAS CONTACTS: OK

> MAS MH CLINIC VISITS FUTURE: OK MH HIGH RISK PRF HX: OK

> MH TREATMENT COORDINATOR: OK

> Install Questions for GMTS\*2.7\*104

> Checking Install for Package OR\*3.0\*348 Install Questions for OR\*3.0\*348 Incoming Files:

> 100.9 OE/RR NOTIFICATIONS

> Note: You already have the 'OE/RR NOTIFICATIONS' File. Checking Install for Package PXRM\*2.0\*24

> Install Questions for PXRM\*2.0\*24 Incoming Files:

> 811.4 REMINDER COMPUTED FINDINGS (including data) Note: You already have the 'REMINDER COMPUTED FINDINGS' File. I will REPLACE your data with mine.

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO// \<Enter\>

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// \<Enter\>

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// \<Enter\> SSH VIRTUAL TEMINAL Do not queue the install

> Install Started for HIGH RISK MH 2.0 :

> Dec 10, 2012@11:07:14

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Dec 10, 2012@11:07:14

> Running Pre-Install Routine: MPBPRE^PXRMP24I Install Started for TIU\*1.0\*265 :

> Dec 10, 2012@11:07:14

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Dec 10, 2012@11:07:14

> Installing PACKAGE COMPONENTS:

> Installing PARAMETER DEFINITION

> Dec 10, 2012@11:07:14

> Running Post-Install Routine: ^TIUPS265

> Title Created: PATIENT RECORD FLAG CATEGORY I - HIGH RISK FOR SUICIDE

> Title attached to Document Class PATIENT RECORD FLAG CAT I Updating Routine file...

> Updating KIDS files...

> TIU\*1.0\*265 Installed.

> Dec 10, 2012@11:07:16

> Not a production UCI NO Install Message sent

> Install Started for DG\*5.3\*849 :

> Dec 10, 2012@11:07:16

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Dec 10, 2012@11:07:17

> Installing PACKAGE COMPONENTS: Installing MAIL GROUP

> Installing OPTION

> Dec 10, 2012@11:07:17

> Running Post-Install Routine: ^DG53849P

> The 'HIGH RISK FOR SUICIDE' PRF is already entered in the PRF NATIONAL FLAG file, no further processing of the new national PRF field entry.

> Updating Routine file... Updating KIDS files...

> DG\*5.3\*849 Installed.

> Dec 10, 2012@11:07:17

> Not a production UCI NO Install Message sent

> Install Started for SD\*5.3\*588 :

> Dec 10, 2012@11:07:17

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Dec 10, 2012@11:07:17

> Installing PACKAGE COMPONENTS: Installing OPTION

> Installing PARAMETER DEFINITION

> Dec 10, 2012@11:07:17

> Running Post-Install Routine: ^SD53588P Updating Parameters File...

> SDMH PROACTIVE DAYS

> 89895006^Duplicate instance not allowed.

> SDMH NO SHOW DAYS

> 89895006^Duplicate instance not allowed.

> Updating Routine file... Updating KIDS files...

> SD\*5.3\*588 Installed.

> Dec 10, 2012@11:07:17

> Not a production UCI NO Install Message sent

> Install Started for GMTS\*2.7\*104 :

> Dec 10, 2012@11:07:17

> Build Distribution Date: Dec 07, 2012

> Installing Routines:

> Dec 10, 2012@11:07:17

> Running Post-Install Routine: POST^GMTSY104

> Updating description for Health Summary Component MH HIGH RISK FOR SUICIDE Update Successful

> Updating Routine file... Updating KIDS files...

> GMTS\*2.7\*104 Installed.

> Dec 10, 2012@11:07:17

> Not a production UCI NO Install Message sent

> Install Started for OR\*3.0\*348 :

> Dec 10, 2012@11:07:17

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Dec 10, 2012@11:07:17

> Installing Data Dictionaries:

> Dec 10, 2012@11:07:17

> Installing PACKAGE COMPONENTS: Installing PARAMETER DEFINITION

> Dec 10, 2012@11:07:18

> Running Post-Install Routine: POST^ORY348 Updating Routine file...

> Updating KIDS files...

> OR\*3.0\*348 Installed.

> Dec 10, 2012@11:07:18

> Not a production UCI NO Install Message sent

> Install Started for PXRM\*2.0\*24 :

> Dec 10, 2012@11:07:18

> Build Distribution Date: Dec 07, 2012 Installing Routines:

> Dec 10, 2012@11:07:18

> Running Pre-Install Routine: PRE^PXRMP24I

> DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries:

> Dec 10, 2012@11:07:19

> Installing Data:

> Dec 10, 2012@11:07:19

> Running Post-Install Routine: POST^PXRMP24I ENABLE options.

> ENABLE protocols.

> There are 5 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry VA-MH NO SHOW APPT CLINICS LL
2.  Installing Reminder Exchange entry VA-MHTC APPT STOP CODES AND EXCLUSION STOP
3.  Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW FOLLOW-UP
4.  Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW ADHOC RPT
5.  Installing Reminder Exchange entry VA-MHTC NEEDS ASSIGNMENT Renaming/inactivating health factors and terms that are no longer used.

> Updating Routine file... Updating KIDS files...

> PXRM\*2.0\*24 Installed.

> Dec 10, 2012@11:07:31

> Not a production UCI NO Install Message sent

> Running Post-Install Routine: POST^GMTSY104

> Updating description for Health Summary Component MH HIGH RISK FOR SUICIDE Update Successful

> Updating Routine file... Updating KIDS files...

> HIGH RISK MH 2.0 Installed.

> Dec 10, 2012@11:07:31

> No link to PACKAGE file

> Install Completed

> <span id="Appendix_B:_Instructions_for_Recreating/" class="anchor"></span>Appendix B: Instructions for Recreating/ Re-pointing Site- defined Notifications

> To transfer a local notification outside the national number range (1-9999), FileMan’s Enter/Edit File Entries option should be used to create a new entry to transfer to. This will require the user to re-enter the data contained in the original notification entry in the new entry.

> Please follow these steps for this transfer process:

> For the purposes of this example, this will be the original notification entry that we will be transferring:

1.  Create an entry in the OE/RR Notifications file \#100.9. This will be the new entry where the original entry information will be transferred to. This entry must have a unique, descriptive name and unique internal entry number. In addition, the internal entry number must be specific to your VAMC in the following format:

> \<your site station number\>\<incremental notification number 01-99\>

> For example, if your site is number 660, your first locally created notification would be 66001.

> Enter a slightly different name from the original entry; otherwise you will be editing the original entry name. The name can be edited later if you wish.

2.  Re-enter the following information from the original notification entry above. All "site- defined" notifications must be defined similarly to the following example:

> Site-defined notifications CANNOT have follow-up actions. (Notifications with follow- up actions must have follow-up action code written for both the ListManager and GUI interfaces. Currently, this requires the source code to the GUI which is not available.) Therefore, the entry point must be INFODEL and routine name ORB3FUP2.

3.  Delete the original notification entry (IEN \#77) occupying the national numberspace. This will allow FileMan to provide the user the option to update any pointers pointing to the original entry.
4.  Select option \#2 to redirect all pointers to point to the new record entry. Enter the name of the new record entry and exit out of the ENTER/EDIT option.

> a\) This will generate a report of all the record entries whose pointers have been updated in the OE/RR LIST file \#100.21 and ORDER CHECK RULE file \#860.2. Of note, the notification pointers in file \#100.21 are obsolete and no longer in use, so that section of

> the report can be disregarded. If there are no records to print, then there are no pointers in either of these files that point to the original entry.

5.  To verify that the pointers have updated correctly, you could perform a FileMan Print or Inquiry into the ORDER CHECK RULE file \#860.2 for those record entries that are printed out in the report above. For example:

> <span id="Acronyms" class="anchor"></span><u>Acronyms</u>

> The OIT Master Glossary is available at [<u>http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm</u>](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AIMS</p>
</blockquote></td>
<td><blockquote>
<p>Abnormal Involuntary Movement Scale</p>
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
<p>API</p>
</blockquote></td>
<td><blockquote>
<p>Application Programmer Interface.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ASU</p>
</blockquote></td>
<td><blockquote>
<p>Authorization/Subscription Utility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Clin4</p>
</blockquote></td>
<td><blockquote>
<p>National Customer Support team that supports Clinical Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CAC</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Applications Coordinator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DBA</p>
</blockquote></td>
<td><blockquote>
<p>Database Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DG</p>
</blockquote></td>
<td><blockquote>
<p>Registration and Enrollment Package namespace</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ESM</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Systems Management (ESM)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FIM</p>
</blockquote></td>
<td><blockquote>
<p>Functional Independence Measure</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>Geriatric Extended Care</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td><blockquote>
<p>Health Summary namespace (also HSUM)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GUI</p>
</blockquote></td>
<td><blockquote>
<p>Graphic User Interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HRMH/HRMHP</p>
</blockquote></td>
<td><blockquote>
<p>High Risk Mental Health Patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IAB</p>
</blockquote></td>
<td><blockquote>
<p>Initial Assessment &amp; Briefing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICD-10</p>
</blockquote></td>
<td><blockquote>
<p>International Classification of Diseases, 10th Edition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICR</p>
</blockquote></td>
<td><blockquote>
<p>Internal Control Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IHD</p>
</blockquote></td>
<td><blockquote>
<p>Ischemic Heart Disease</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IOC</p>
</blockquote></td>
<td><blockquote>
<p>Initial Operating Capabilities</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LDL</p>
</blockquote></td>
<td><blockquote>
<p>Low-density lipo-protein</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LSSD</p>
</blockquote></td>
<td><blockquote>
<p>Last Service Separation Date</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MDD</p>
</blockquote></td>
<td><blockquote>
<p>Major Depressive disorder</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MH</p>
</blockquote></td>
<td><blockquote>
<p>Mental Health</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MHTC</p>
</blockquote></td>
<td><blockquote>
<p>Mental Health Treatment Coordinator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OHI</p>
</blockquote></td>
<td><blockquote>
<p>Office of Health Information</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OI</p>
</blockquote></td>
<td><blockquote>
<p>Office of Information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OIF/OEF</p>
</blockquote></td>
<td><blockquote>
<p>Operation Iraqi Freedom/Operation Enduring Freedom</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OIT/OI&amp;T</p>
</blockquote></td>
<td><blockquote>
<p>Office of Information Technology</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OMHS</p>
</blockquote></td>
<td><blockquote>
<p>Office of Mental Health Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OQP</p>
</blockquote></td>
<td><blockquote>
<p>Formerly Office of Quality and Performance, replaced by Office of Performance Measurement and Office of Quality, Safety &amp; Value</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OQSV</p>
</blockquote></td>
<td><blockquote>
<p>Office of Quality, Safety &amp; Value</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORR</p>
</blockquote></td>
<td><blockquote>
<p>Operational Readiness Review</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PCE</p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Encounter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PCS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PD</p>
</blockquote></td>
<td><blockquote>
<p>Product Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PIMS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Information Management System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PMAS</p>
</blockquote></td>
<td><blockquote>
<p>Program Management Accountability System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PTM</p>
</blockquote></td>
<td><blockquote>
<p>Patch Tracker Message</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRM</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Reminder Package namespace</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RSD</p>
</blockquote></td>
<td><blockquote>
<p>Requirements Specification Document</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SD</p>
</blockquote></td>
<td><blockquote>
<p>Scheduling Package Namespace</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SQA</p>
</blockquote></td>
<td><blockquote>
<p>Software Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TIU</p>
</blockquote></td>
<td><blockquote>
<p>Text Integration Utilities</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>USR</p>
</blockquote></td>
<td><blockquote>
<p>ASU package namespace</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Department of Veteran Affairs</p>
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
<tr class="even">
<td><blockquote>
<p>VISN</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Integrated Service Network</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Information System and Technology Architecture</p>
</blockquote></td>
</tr>
</tbody>
</table>