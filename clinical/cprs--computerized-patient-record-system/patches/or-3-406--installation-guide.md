---
title: OR*3*406 ICD-10 PTF Modifications Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: ICD-10 PTF Modifications
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*406
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - table
  - contents
  - span
  - install
  - routine
  - installation
  - class
  - filed
  - mail
  - group
page_count: 0
word_count: 9017
section_count: 33
table_count: 16
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: September 2015
revision_count: 1
revision_newest: 9/2/2015
revision_oldest: 9/2/2015
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/icd_10_ptf_modifications_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/icd_10_ptf_modifications_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  ICD-10 Patient Treatment File (PTF) Modifications

  Admission, Discharge, Transfer (ADT) - DG\*5.3\*884

  Health Summary (HS) - GMTS\*2.7\*111

  Integrated Billing (IB) - IB\*2.0\*522

  Lab Anatomic Pathology (AP) and Emerging Pathogens Initiative (EPI) - LR\*5.2\*442

  Order Entry/Results Reporting (OE/RR) - OR\*3.0\*406

  Clinical Case Registries (CCR) - ROR\*1.5\*25

  Installation Guide
---

![](or-3-406-icd-10-ptf-modifications-installation-guide/001.png)

September 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Product Development (PD)

Revision History

| Date     | Version | Description                                                        | Author                                    |
|----------|---------|--------------------------------------------------------------------|-------------------------------------------|
| 9/2/2015 | 1.0     | Baseline document for ICD-10 PTF Modifications production release. | VA OI&T PD, ICD-10 PTF Modifications Team |

<span id="_Toc428787960" class="anchor"></span>Table 1: 401 Sub-File Fields From Which AO Cross-References Will Be Removed

Table of Contents

List of Figures

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Software Disclaimer](#software-disclaimer)
  - [Documentation Disclaimer](#documentation-disclaimer)
- [Pre-Installation Information](#pre-installation-information)
  - [Environment Check](#environment-check)
  - [Add Installer to Reminder Management Mail Group](#add-installer-to-reminder-management-mail-group)
  - [Pre-Installation Routine](#pre-installation-routine)
  - [Required Builds](#required-builds)
- [ICD-10 PTF Modifications Installation Instructions](#icd-10-ptf-modifications-installation-instructions)
  - [Warnings](#warnings)
    - [WARNING: Install During Non-Peak/Off-Hours With All Users Logged Off the System](#warning-install-during-non-peakoff-hours-with-all-users-logged-off-the-system)
    - [WARNING: Do Not Install While the PTF Background Job \[DG PTF BACKGROUND JOB\] Is Running](#warning-do-not-install-while-the-ptf-background-job-dg-ptf-background-job-is-running)
    - [WARNING: Do Not Install While IB Queue Means Test Compilation of Charges \[IB MT NIGHT COMP\] Is Running](#warning-do-not-install-while-ib-queue-means-test-compilation-of-charges-ib-mt-night-comp-is-running)
    - [WARNING: Do Not Install While Lab EPI Nightly Task \[LREPI NIGHTLY TASK\] Is Running](#warning-do-not-install-while-lab-epi-nightly-task-lrepi-nightly-task-is-running)
    - [WARNING: Do Not Install While CCR Nightly Task, Registry Update & Data Extraction \[ROR TASK\] Is Running](#warning-do-not-install-while-ccr-nightly-task-registry-update-data-extraction-ror-task-is-running)
    - [RECOMMENDATION: Do Not Install During System Backup](#recommendation-do-not-install-during-system-backup)
  - [Users Must Be Off the System](#users-must-be-off-the-system)
  - [Distribution](#distribution)
  - [Estimated Timing](#estimated-timing)
  - [File Retrieval](#file-retrieval)
    - [New and Updated Documentation](#new-and-updated-documentation)
    - [Software Files](#software-files)
  - [Environment](#environment)
  - [Load Software Distribution](#load-software-distribution)
  - [Run Installation Options for Multi-build](#run-installation-options-for-multi-build)
    - [Backup a Transport Global](#backup-a-transport-global)
    - [Compare Transport Global to Current System (Optional)](#compare-transport-global-to-current-system-optional)
    - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
  - [Install KIDS Multi-Build](#install-kids-multi-build)
- [Post Installation Information](#post-installation-information)
  - [DG\5.3\884 Post-Installation Routine](#dg53884-post-installation-routine)
    - [Rebuild Clinical Reminders Global Index ^PXRMINDX(45)](#rebuild-clinical-reminders-global-index-pxrmindx45)
    - [Recompile Input Templates Where Field DD Definition Changed](#recompile-input-templates-where-field-dd-definition-changed)
  - [OR\3.0\406 Post-Installation Routine](#or30406-post-installation-routine)
  - [ROR\1.5\25 Post-Installation Routine](#ror1525-post-installation-routine)
  - [Optional: Delete Post-Installation Routines](#optional-delete-post-installation-routines)
- [Install the Clinical Case Registries Graphical User Interface](#install-the-clinical-case-registries-graphical-user-interface)
  - [Background Information](#background-information)
  - [Uninstall Older CCR GUI Versions](#uninstall-older-ccr-gui-versions)
    - [First-Time Installation of CCR GUI](#first-time-installation-of-ccr-gui)
    - [Upgrade Existing CCR GUI](#upgrade-existing-ccr-gui)
    - [Instructions to Uninstall Previous CCR GUI Versions](#instructions-to-uninstall-previous-ccr-gui-versions)
  - [Install New CCR GUI](#install-new-ccr-gui)
  - [Continue Installing New CCR GUI on File Server](#continue-installing-new-ccr-gui-on-file-server)
  - [Configure CCR Desktop Application Parameters](#configure-ccr-desktop-application-parameters)
  - [CCR Command Line Switches](#ccr-command-line-switches)
- [Back-Out and Roll-Back Procedures](#back-out-and-roll-back-procedures)
  - [Back-Out Procedure](#back-out-procedure)
  - [Roll-Back Procedure](#roll-back-procedure)
  - [Locate Reminder Management Mail Group](#locate-reminder-management-mail-group)
  - [Add Installer to Reminder Management Mail Group](#add-installer-to-reminder-management-mail-group-1)
  - [Remove Installer From Reminder Management Mail Group](#remove-installer-from-reminder-management-mail-group)
  - [Clinical Reminders Mail Group Message – Index Rebuild Status (Example)](#clinical-reminders-mail-group-message-index-rebuild-status-example)
  - [Clinical Reminders Mail Group Message – Entries Could Not Be Indexed (Example)](#clinical-reminders-mail-group-message-entries-could-not-be-indexed-example)
Veterans Health Administration (VHA) software remediation for the International Classification of Diseases, Tenth Revision (ICD-10) enabled the transition to support the use of ICD-10 code sets. ICD-10 Clinical Modification (ICD-10-CM) will replace ICD-9-CM as the diagnostic coding system, and ICD-10 Procedure Coding System (ICD-10-PCS) will replace ICD-9-CM as the procedural coding system. The Patient Treatment File (PTF) Modifications project will increase the maximum allowable codes in the entry, display, lookup, view, print, storage, and transmission of the ICD-10 code sets in the VistA legacy and Health*<u>e</u>*Vet systems. Effective as of the ICD-10 activation date, VHA will be able to utilize the ICD-10 code sets to include the increased number of diagnosis and procedures which can be recorded in its day-to-day operations (e.g. entry, display, lookup, print, storage, internal and/or external transmission) for inpatient episodes of care with discharges on or after this date.
The ICD-10 PTF Modifications project supports the expansion of the number of ICD-10 Diagnosis, Present on Admission (POA) indicators, and Procedure and Surgical codes that may be contained in a patient treatment record. The user will now be able to enter up to 25 ICD-10 diagnosis codes with their associated POA indicators in each Movement (501) screen and in the Discharge (701) screen of a patient treatment record. The user will also be able to enter up to 25 ICD-10 procedure codes in each Surgical Episode (401) screen and in each Non-Operating Room (OR) Procedure (601) screen.
The ICD-10 PTF Modifications project is comprised of six patches, which are being released within a single Kernel Installation and Distribution System (KIDS) multi-package build (host file):
- Admission, Discharge, Transfer (ADT, also known as Registration), DG\*5.3\*884
- CPRS: Health Summary (HS), GMTS\*2.7\*111
- Integrated Billing (IB), IB\*2.0\*522
- Lab Service: Anatomic Pathology (AP) and Laboratory: Emerging Pathogens Initiative (EPI), LR\*5.2\*442
- CPRS: Order Entry/Results Reporting (OE/RR), OR\*3.0\*406
- Clinical Case Registries (CCR), ROR\*1.5\*25

## Software Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17, Section 105, of the United States Code, this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

## Documentation Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Environment Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 includes an environment check (ENV^DG884P) that will ensure the following requirements are satisfied prior to patch installation:

- Programmer access is required for installing this patch. Prior to installation, the installer must ensure the DUZ(0) node of the DUZ array is set to the "@" symbol.
- The ‘Q-PTI.VA.GOV’ entry is required in the DOMAIN (#4.2) file. Prior to installation, the installer should check the DOMAIN file to make certain this entry exists. If it does not, the user should follow the instructions in the XM\*999\*179 patch to create it. This patch installation will not run until this DOMAIN file entry exists.
- Several DRG-related files should have the correct number of nationally released entries. If they do not, a message is displayed to the patch installer to log a Remedy ticket. Also, a message is sent to a customer support mail group on FORUM. NOTE: This will NOT stop the patch from installing.

## Add Installer to Reminder Management Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 automatically queues a background job that will rebuild the Clinical Reminders Global Index, ^PXRMINDX (45), in the new format.  Reminder evaluation will be disabled while these indexes are rebuilding.

> **NOTE:** Estimated re-indexing time is 10 minutes to 3 hours. <u>All users must be logged off of the system</u> until the re-indexing background job has been completed. By taking this step, sites will prevent missed actions as a result of reminder functionality interruption due to re-indexing. This eliminates any risk to patient safety or data due to incomplete or missed clinical reminders.

The background job will generate one or two messages to the Clinical Reminders Management mail group.  One message will provide the status of the rebuild and specify if any entries could not be indexed or problems were encountered. If there were problems, another message will be sent with the details regarding the entries that could not be indexed. Because users must be logged off of the system until the re-indexing is complete, it is important for the installer to be added to the Clinical Reminders Management mail group in order to be notified of re-indexing status.

The messages are sent to the REMINDER MANAGEMENT MAILGROUP defined in the CLINICAL REMINDER PARAMETERS (#800) file entry. NOTE: This mail group name may not be the same on all VistA instances. See <u>APPENDIX A – Reminder Management Mail Group</u> for instructions on how to locate the name of this mail group and how to add and remove a user from this mail group.

## Pre-Installation Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 includes a pre-installation routine, PRE^DG884P, which will perform the following actions:

- Delete the "AO" cross-references from the following five OPERATION CODE fields in the 401 (#45.01) sub-file of the PTF (#45) file:

| Field Number | Field Name       |
|--------------|------------------|
| 8            | OPERATION CODE 1 |
| 9            | OPERATION CODE 2 |
| 10           | OPERATION CODE 3 |
| 11           | OPERATION CODE 4 |
| 12           | OPERATION CODE 5 |

<span id="_Toc428787961" class="anchor"></span>Table 2: DG\*5.3\*884 Required Builds

- Since it is possible for the installer to skip running the environment check routine, the pre-installation routine also checks for the existence of the Q-PTI.VA.GOV entry in the DOMAIN (#4.2) file. If it does not exist, this patch installation will stop until it is created.
- A new mail group is created in the MAIL GROUP (#3.8) file. The mail group name is PTI. The purpose of this new mail group is to accept confirmation messages from the Austin Information Technology Center (AITC). Currently, the existing PTT mail group handles this function, but it will become dormant. The members of the PTT mail group will be automatically added to the new PTI mail group. If the PTT mail group does not have any members, the installer will be automatically added as a new member to the new PTI mail group. In that case, the installer should find out which persons at the site should be added as members to the new PTI mail group. The MailMan package will not deliver messages to a mail group that does not have any members assigned to it.
- The PTF125 entry in the TRANSMISSION ROUTERS (#407.7) file is modified to send PTF record messages to the new Q-PTI.VA.GOV domain at the AITC. The existing Q-PTT.VA.GOV domain will no longer be used to send PTF record messages. If the PTF125 entry does not exist, it will be created. If, for any reason, the PTF125 entry cannot be created or modified, an error message will be displayed to the installer, and the patch installation will stop.
- Several DRG-related files are checked to ensure they have the correct number of nationally released entries. If they do not, a message is displayed to the patch installer to log a Remedy ticket. Also, a message is sent to a customer support mail group on FORUM. NOTE: This will NOT stop the patch from installing.

## Required Builds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following tables list the REQUIRED builds for this KIDS software distribution. KIDS will not allow the installation of this patch without their prior installation.

> **NOTE:** DG\*5.3\*884 is included in this KIDS distribution and is a required build for the subsequent builds in this KIDS distribution, GMTS\*2.7\*111, IB\*2.0\*522, LR\*5.2\*442, OR\*3.0\*406, and ROR\*1.5\*25.

The builds listed below are required prior to installing DG\*5.3\*884.

| Required Build | Required Build Subject                              | Required Build Release Date |
|----------------|-----------------------------------------------------|-----------------------------|
| DG\*5.3\*850   | ADT ICD-10 REMEDIATION                              | 8/5/2014                    |
| DG\*5.3\*862   | PTF ICD-10 CHANGES FOR CLINICAL REMINDERS           | 7/24/2014                   |
| DG\*5.3\*867   | DG NEWBORN CLAIMS ENHANCEMENT                       | 12/10/2013                  |
| DG\*5.3\*898   | PATCH FOR 601 DISCHARGE DATE                        | 10/14/2014                  |
| DG\*5.3\*905   | REGISTRATION PTF FIXES                              | 6/16/2015                   |
| XM\*999\*179   | NEW DOMAIN Q-PTI.VA.GOV ADDED TO DOMAIN (#4.2) FILE | 7/30/2015                   |

<span id="_Toc428787962" class="anchor"></span>Table 3: GMTS\*2.7\*111 Required Builds

The builds listed below are required prior to installing GMTS\*2.7\*111.

| Required Build | Required Build Subject                              | Required Build Release Date |
|----------------|-----------------------------------------------------|-----------------------------|
| DG\*5.3\*884   | ICD-10 PATIENT TREATMENT FILE MODIFICATIONS PROJECT | 9/2/2015                    |
| GMTS\*2.7\*101 | ICD-10 – Health Summary Updates                     | 8/29/2014                   |

<span id="_Toc428787963" class="anchor"></span>Table 4: IB\*2.0\*522 Required Builds

The builds listed below are required prior to installing IB\*2.0\*522.

| Required Build | Required Build Subject                              | Required Build Release Date |
|----------------|-----------------------------------------------------|-----------------------------|
| DG\*5.3\*884   | ICD-10 PATIENT TREATMENT FILE MODIFICATIONS PROJECT | 9/2/2015                    |
| IB\*2.0\*461   | IB ICD-10 CLASS 1 REMEDIATION                       | 10/22/2014                  |
| IB\*2.0\*479   | SITE PARAMETER DISPLAYS INCORRECTLY FOR IV SECTION  | 1/13/2014                   |
| IB\*2.0\*516   | EBILLING – CLAIMS COMPLIANCE                        | 5/12/2015                   |

<span id="_Toc428787964" class="anchor"></span>Table 5: LR\*5.2\*442 Required Builds

The builds listed below are required prior to installing LR\*5.2\*442.

| Required Build | Required Build Subject                                                 | Required Build Release Date |
|----------------|------------------------------------------------------------------------|-----------------------------|
| DG\*5.3\*884   | ICD-10 PATIENT TREATMENT FILE MODIFICATIONS PROJECT                    | 9/2/2015                    |
| LR\*5.2\*421   | EMERGING PATHOGENS INITIATIVE (EPI) ICD-10 CLASS I REMEDIATION PROJECT | 8/15/2014                   |
| LR\*5.2\*422   | ANATOMIC PATHOLOGY ICD-10 CLASS 1 REMEDIATION PROJECT                  | 8/15/2014                   |

<span id="_Toc428787965" class="anchor"></span>Table 6: OR\*3.0\*406 Required Builds

The builds listed below are required prior to installing OR\*3.0\*406.

| Required Build | Required Build Subject                              | Required Build Release Date |
|----------------|-----------------------------------------------------|-----------------------------|
| DG\*5.3\*884   | ICD-10 PATIENT TREATMENT FILE MODIFICATIONS PROJECT | 9/2/2015                    |

<span id="_Toc428787966" class="anchor"></span>Table 7: ROR\*1.5\*25 Required Builds

The builds listed below are required prior to installing ROR\*1.5\*25.

| Required Build | Required Build Subject                                                              | Required Build Release Date |
|----------------|-------------------------------------------------------------------------------------|-----------------------------|
| DG\*5.3\*884   | ICD-10 PATIENT TREATMENT FILE MODIFICATIONS PROJECT                                 | 9/2/2015                    |
| ROR\*1.5\*27   | MINOR CCR CHANGES (Updates to Support Enhanced ICD-10 PTF Procedures and Diagnoses) | 6/10/2015                   |

<span id="_Toc428787967" class="anchor"></span>Table 8: Anonymous Directories

# ICD-10 PTF Modifications Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](or-3-406-icd-10-ptf-modifications-installation-guide/002.png)

## Warnings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### WARNING: Install During Non-Peak/Off-Hours With All Users Logged Off the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please install this patch in your production accounts during non-peak/off-hours. The Clinical Reminders Global Index ^PXRMINDX (45) will be rebuilt for the PTF (#45) file, and reminder evaluation will be disabled while these indexes are rebuilding.

> **NOTE:** Estimated re-indexing time is 10 minutes to 3 hours. <u>All users must be logged off of the system</u> until the re-indexing background job has been completed. If you followed the instructions in Section 2.2 above (<u>Add Installer to Reminder Management Mail Group</u>), you will receive a MailMan message upon completion.By taking this step, sites will prevent missed actions as a result of reminder functionality interruption due to re-indexing. This eliminates any risk to patient safety or data due to incomplete or missed clinical reminders.

Notify the Health Information Management (HIM) Chief and Implementation Business Manager when the ICD-10 PTF Modifications software is scheduled to be installed.

### WARNING: Do Not Install While the PTF Background Job \[DG PTF BACKGROUND JOB\] Is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not install this patch while the PTF Background Job \[DG PTF BACKGROUND JOB\] option is running or during the time it is scheduled to run.

### WARNING: Do Not Install While IB Queue Means Test Compilation of Charges \[IB MT NIGHT COMP\] Is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not install this patch while the Queue Means Test Compilation of Charges \[IB MT NIGHT COMP\] option is running or during the time it is scheduled to run.

### WARNING: Do Not Install While Lab EPI Nightly Task \[LREPI NIGHTLY TASK\] Is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not install this patch while the Lab EPI Nightly Task \[LREPI NIGHTLY TASK\] option is running or during the time it is scheduled to run.

### WARNING: Do Not Install While CCR Nightly Task, Registry Update & Data Extraction \[ROR TASK\] Is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not install this patch while the CCR nightly task, Registry Update & Data Extraction \[ROR TASK\] option is running or during the time it is scheduled to run.

### RECOMMENDATION: Do Not Install During System Backup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended to schedule installation outside of the timeframe(s) during which a system backup is scheduled to run.

## Users Must Be Off the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software distribution should be loaded during non-peak/off-hours with all users logged off the system. Notify the Health Information Management (HIM) Chief and Implementation Business Manager when the ICD-10 PTF Modifications software is scheduled to be installed.

Additionally, the following options should be placed out of order to reduce the possibility of errors when the routines are updated:

- All options beginning with "DG PTF" (“DG\<space\>PTF”)
  - Place all options beginning with “DG PTF” out of order by entering "DG PTF\*"
- Enter/Edit Billing Information \[IB EDIT BILLING INFO\]

## Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software distribution contains six builds in a single KIDS multi-package host file. In addition, CCR patch ROR\*1.5\*25 includes a revised Graphical User Interface (GUI) application, which must be distributed to the appropriate workstations. After the patch is installed correctly and the GUI is updated, the version of the GUI will be 1.5.25. The GUI is distributed in a separate zip file (see Section 3.5.2, Software Files).

> **NOTE:** DG\*5.3\*884 is included in this KIDS distribution and is a required build for the subsequent builds in this KIDS distribution, GMTS\*2.7\*111, IB\*2.0\*522, LR\*5.2\*442, OR\*3.0\*406, and ROR\*1.5\*25 (see Section 2.3, Required Builds).

## Estimated Timing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The estimated installation time for this software distribution is less than 5 minutes during off-peak hours with all users logged off the system.

The background job to perform a rebuild of the Clinical Reminders Global Index, ^PXRMINDX(45), will be automatically queued during the DG\*5.3\*884 post-installation process. It will not impact the software installation time.

> **NOTE:** Post-installation estimated re-indexing time is 10 minutes to 3 hours. <u>All users must be logged off of the system</u> until the re-indexing background job has been completed. If you followed the instructions in Section 2.2 above (<u>Add Installer to Reminder Management Mail Group</u>), you will receive a MailMan message upon completion.By taking this step, sites will prevent missed actions as a result of reminder functionality interruption due to re-indexing. This eliminates any risk to patient safety or data due to incomplete or missed clinical reminders.

Notify the Health Information Management (HIM) Chief and Implementation Business Manager when the ICD-10 PTF Modifications software is scheduled to be installed.

## File Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the functionality introduced by the ICD-10 PTF Modifications project is available in the \[ANONYMOUS.SOFTWARE\] directories at the following Internet addresses:

| Preferred or Specific Server       | FTP Address                        |
|------------------------------------|------------------------------------|
| First available FTP server         | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

<span id="_Toc428787968" class="anchor"></span>Table 9: Updated Documents

### New and Updated Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of the documentation files related to the ICD-10 PTF Modifications project, which are available via the FTP sites listed above:

| File Name                                               | Document File Description                                                                               | New or Updated | FTP Protocol |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------|--------------|
| ICD_10_PTF_MODIFICATIONS_IG.PDF                         | ICD-10 PTF Installation Guide (all patches)                                                             | New            | Binary       |
| DG_5_3_884_RN.pdf                                       | Admission Discharge Transfer DG\*5.3\*884 Release Notes                                                 | New            | Binary       |
| pimstm.pdf                                              | Admission Discharge Transfer Technical Manual                                                           | Updated        | Binary       |
| ptf.pdf                                                 | Admission Discharge Transfer PTF Menu User Manual                                                       | Updated        | Binary       |
| pxrm_index_tm.pdf                                       | Clinical Reminders Index Technical Manual                                                               | Updated        | Binary       |
| ROR1_5_25RN.pdf (may be contained in ROR1_5P25DOC2.ZIP) | Clinical Case Registries ROR\*1.5\*25 Release Notes                                                     | New            | Binary       |
| ROR1_5_25TM.pdf (may be contained in ROR1_5P25DOC2.ZIP) | Clinical Case Registries Technical Manual                                                               | Updated        | Binary       |
| ROR1_5_25UM.pdf (may be contained in ROR1_5P25DOC1.ZIP) | Clinical Case Registries User Manual                                                                    | Updated        | Binary       |
| GMTS_2_7_111_RN.pdf                                     | CPRS: Health Summary GMTS\*2.7\*111 Release Notes                                                       | New            | Binary       |
| hsum_2_7_tm.pdf                                         | CPRS: Health Summary Technical Manual                                                                   | Updated        | Binary       |
| hsum_2_7_um.pdf                                         | CPRS: Health Summary User Manual                                                                        | Updated        | Binary       |
| OR_3_0_406_RN.pdf                                       | CPRS: Order Entry/Results Reporting OR\*3.0\*406 Release Notes                                          | New            | Binary       |
| IB_2_522_RN.pdf                                         | Integrated Billing IB\*2.0\*522 Release Notes                                                           | New            | Binary       |
| ib_2_0_tm.pdf                                           | Integrated Billing Technical Manual                                                                     | Updated        | Binary       |
| ib_2_0_um.pdf                                           | Integrated Billing (IB) User Guide                                                                      | Updated        | Binary       |
| LR_5_2_442_RN.pdf                                       | Laboratory: Anatomic Pathology and Laboratory: Emerging Pathogens Initiative LR\*5.2\*442 Release Notes | New            | Binary       |
| lab_epi_rollup_mod_tech_user_manual.pdf                 | Laboratory EPI Roll Up Modifications Technical and User Manual                                          | Updated        | Binary       |
| lab_epi_tech_user_guide.pdf                             | Laboratory EPI Technical and User Guide                                                                 | Updated        | Binary       |
| lab_epi_hepc_tech_user_guide.pdf                        | Laboratory Hepatitis C and EPI Technical and User Guide                                                 | Updated        | Binary       |
| lab_epi_searchextract_tm_ug.pdf                         | Laboratory Search/Extract Technical and User Guide                                                      | Updated        | Binary       |
| Lab_AP_LR_5_2_UG.pdf                                    | Laboratory Anatomic Pathology (AP) User Guide                                                           | Updated        | Binary       |

<span id="_Toc428787969" class="anchor"></span>Table 10: Software Files to Download

Upon software release, the updated manuals may also be retrieved from the VA Software Document Library (VDL) website at <http://www.va.gov/vdl/>.

### Software Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files are available for download:

<table>
<caption><p><span id="_Toc428787970" class="anchor"></span>Table 11: CCR Command Line Switches</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 43%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Host File</th>
<th>File Name</th>
<th>FTP Protocol</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KIDS Distribution</td>
<td><p>ICD_10_PTF_MODIFICATIONS.KID</p>
<p>The KID file contains 6 patches:</p>
<ul>
<li><p>DG*5.3*884</p></li>
<li><p>GMTS*2.7*111</p></li>
<li><p>IB*2.0*522</p></li>
<li><p>LR*5.2*442</p></li>
<li><p>ROR*1.5*25</p></li>
<li><p>OR*3.0*406</p></li>
</ul></td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>CCR Revised GUI for ROR*1.5*25</td>
<td><p>ROR1_5P25GUI.ZIP</p>
<p>The ZIP file contains CCRSetup.exe.</p></td>
<td>Binary</td>
</tr>
</tbody>
</table>

<span id="_Toc428787970" class="anchor"></span>Table 11: CCR Command Line Switches

## Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Programmer access is required for installing patch DG\*5.3\*884.

Patch DG\*5.3\*884 includes an environment check, ENV^DG884P, which will ensure the following requirements are satisfied prior to patch installation (see Section 2.1, Environment Check, above for more information):

- Verify that the DUZ(0) node of the DUZ array is set to the “@” symbol.
- Verify that the Q-PTI.VA.GOV entry exists in the DOMAIN (#4.2) file.
- Verify DRG-related files have the correct number of nationally released entries. NOTE: The patch may still be installed if this requirement is not met.

## Load Software Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the steps below to load the software distribution:

1.  Retrieve the file ICD_10_PTF_MODIFICATIONS.KID using one of the methods described above.
2.  From the Kernel Installation and Distribution System menu \[XPD MAIN\], select the Installation menu \[XPD INSTALLATION MENU\].
3.  From the Installation menu, select the LOAD A DISTRIBUTION option.
4.  When prompted for "Enter a Host File:", enter the full directory path where you saved the host file, ICD_10_PTF_MODIFICATIONS.KID (e.g., SYS\$SYSDEVICE:\[ANONYMOUS\]\_ICD_10_PTF_MODIFICATIONS.KID).
5.  When prompted for "OK to continue with Load? NO//", enter "YES".
6.  When prompted for "Want to RUN the Environment Check Routine? YES//", accept the default "YES" answer.
7.  Use “DG\*5.3\*884” as the INSTALL NAME to install this distribution.

Partial example of what will display (see APPENDIX B – Captured Install for a complete installation example):

Loading Distribution...

DG\*5.3\*884

GMTS\*2.7\*111

IB\*2.0\*522

LR\*5.2\*442

ROR\*1.5\*25

OR\*3.0\*406

Build DG\*5.3\*884 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES// YES

DG\*5.3\*884

Will first run the Environment Check Routine, DG884P

## Run Installation Options for Multi-build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Installation menu, you may select to use the following options:

> **NOTE:** When prompted for the INSTALL NAME, enter “DG\*5.3\*884”.

### Backup a Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will create a backup message of any routines exported with this patch. It will not back up any other changes such as DD's or templates.

### Compare Transport Global to Current System (Optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).

### Verify Checksums in Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow you to ensure the integrity of the routines that are in the transport global.

## Install KIDS Multi-Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is how to start the installation of this KIDS build. These procedures will need to be followed for ICD-10 PTF Modifications, “DG\*5.3\*884” multi-build.

1.  Choose the Install Package(s) option to start the install.
2.  When prompted for the "Select INSTALL NAME:", enter “DG\*5.3\*884”.
3.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", answer “YES”.
4.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//", accept the default “YES” answer.
5.  When prompted "Enter options you wish to mark as 'Out Of Order':", enter the following options:
    1.  Place all options beginning with “DG PTF” ("DG\<space\>PTF") out of order by entering "DG PTF\*".
    2.  Enter/Edit Billing Information \[IB EDIT BILLING INFO\]
6.  When prompted "Enter protocols you wish to mark as 'Out Of Order':", press the \<return\> or \<enter\> key.
7.  When prompted "Delay Install (Minutes): (0-60): 0//", enter an appropriate number of minutes to delay the installation in order to give users enough time to exit the disabled options before the installation starts.
8.  When prompted "Device: Home//", respond with the correct device.

# Post Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Post-installation instructions associated with this patch; all post-installation activities will occur automatically. However, action may be needed if bad data is encountered in PTF (see Section 4.1.1.1, Clinical Reminders Management Mail Group Messages, below).

## DG\*5.3\*884 Post-Installation Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 includes a post-installation routine, POST^DG884P, that will perform the actions below.

### Rebuild Clinical Reminders Global Index ^PXRMINDX(45)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 automatically queues a background job that will rebuild the Clinical Reminders Global Index, ^PXRMINDX (45), in the new format. Reminder evaluation will be disabled while these indexes are rebuilding.

> **NOTE:** Post-installation estimated re-indexing time is 10 minutes to 3 hours. <u>All users must be logged off of the system</u> until the re-indexing background job has been completed. If you followed the instructions in Section 2.2 above (<u>Add Installer to Reminder Management Mail Group</u>), you will receive a MailMan message upon completion.By taking this step, sites will prevent missed actions as a result of reminder functionality interruption due to re-indexing. This eliminates any risk to patient safety or data due to incomplete or missed clinical reminders.

#### Clinical Reminders Management Mail Group Messages

This job will generate one or two messages to the Clinical Reminders Management mail group. This is the mail group defined in the CLINICAL REMINDER PARAMETERS (#800) file entry.

- One message will provide the status of the rebuild, and specify if any entries could not be indexed or problems were encountered.
- If there were problems, another message will be sent with the details regarding the entries that could not be indexed. If bad data is encountered in PTF and you need assistance dealing with it, you may submit a support ticket.

### Recompile Input Templates Where Field DD Definition Changed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*884 will recompile all compiled input templates that contain specific fields where the Data Dictionary definition of these fields has changed and are being exported with this patch.

## OR\*3.0\*406 Post-Installation Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*406 includes a post-installation routine, POST^ORY406, to establish a default value at the PACKAGE level for the ORWRP TIME/OCC LIMITS INDV parameter. For more information on the default parameter value, please refer to the OR\*3.0\*406 Release Notes on the VDL: <http://www.va.gov/vdl/application.asp?appid=61>.

The following reports in the OE/RR REPORT (#101.24) file will have a value set:

1.  ORRPW ADT ADM DC
2.  ORRPW ADT DC DIAG
3.  ORRPW ADT EXP
4.  ORRPW ADT ICD PROC
5.  ORRPW ADT ICD SURG
6.  ORRPW DOD ADT EXP

## ROR\*1.5\*25 Post-Installation Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROR\*1.5\*25 post-installation routine, POST^RORP025, performs the following function:

- Adds new entries to the ROR METADATA file (#799.2) for the PTF ICD-10 Diagnosis fields. These entries are used to define selection rules for inclusion of patients in the CCR registries.

## Optional: Delete Post-Installation Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following pre/post-installation routines may be deleted from the system if the post-installation process has completed.

- DG884P
- ORY406
- RORP025

# Install the Clinical Case Registries Graphical User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Background Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current CCR Graphical User Interface ([GUI](#Glos_GUI)) provides access to both Hepatitis C and HIV registries.

It is strongly recommended that the CCR GUI be installed on a file server and the CCR application be made available to the CCR users via the Computerized Patient Record System (CPRS) Tool menu. Installing the CCR GUI on workstations is not recommended.

Access to the registries is controlled by the security keys within VistA.

For users who have access to a single registry, its window will be opened automatically by the GUI. Users who have access to both registries will be able to select a registry from a list.

The GUI supports the /NOCCOW command-line parameter that completely disables the CCOW functionality. It also supports the parameter /CCOW=PatientOnly, which disables only the Single Sign-On/User Context (SSO/UC) functionality.

## Uninstall Older CCR GUI Versions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### First-Time Installation of CCR GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There should not be any old software to be uninstalled. If you are unsure whether old software is present, use the uninstall instructions in Section 5.2.3, Instructions to Uninstall Previous CCR GUI Versions, below. If you are certain that no previous GUI software has been installed, you may skip down to section 5.3, Install New CCR GUI.

### Upgrade Existing CCR GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To eliminate any chance for errors, it is strongly recommended that any older versions be uninstalled using the instructions in Section 5.2.3, Instructions to Uninstall Previous CCR GUI Versions, below.

### Instructions to Uninstall Previous CCR GUI Versions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Windows 7 Start menu, select Control Panel, then Programs and Features (in previous versions of Windows, this was called Add or Remove Programs).

> The Uninstall or change a program dialog appears:

<span id="_Toc428787950" class="anchor"></span>Figure 1: Programs and Features, Uninstall or Change a Program

![](or-3-406-icd-10-ptf-modifications-installation-guide/003.png)

2.  Look for any entries that include Clinical Case Registries 1.5\* (or simply 1.5\*) on the program list. If neither of these appears on the program list, skip to Step 9 below.

> NOTE: Releases of the GUI up until 1/13/2010 were shown simply as “1.5.xx” on the program list; following installation of the 1/13/2010 version, it will correctly display on the list as “Clinical Case Registries 1.5.xx.”

3.  Select Clinical Case Registries from the list and click the Uninstall button.
4.  If prompted, click the Next button.
5.  You will likely see a pop-up, asking you to confirm removal:

<span id="_Toc428787951" class="anchor"></span>Figure 2: Clinical Case Registries Uninstall Pop-Up

![](or-3-406-icd-10-ptf-modifications-installation-guide/004.png)

> Confirm the uninstall action by clicking the Yes or OK button.

6.  Confirm deletion of read-only files by clicking the Yes button.
7.  Confirm deletion of shared files by clicking the Yes button.
8.  Wait until the Uninstall Wizard completes the removal and then click the Finish button.
9.  Look for Hepatitis C Local Registry on the Uninstall or change a program list. If this does not appear on the program list, skip to Step 13 below.
10. Select Hepatitis C Local Registry from the list and click the Uninstall button.
11. Confirm the uninstall action by clicking the Yes or OK button.
12. Wait until the Uninstall Wizard completes the removal and click the OK button.
13. Close the Programs and Features, Uninstall or change a program window.

## Install New CCR GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download (see Section 3.5, File Retrieval, above) and install the new GUI using the instructions below.

1.  Download and unzip the ROR1_5P25GUI.ZIP into a temporary directory.
2.  Open the temporary directory and run (double-click) CCRSetup.exe to begin the installation.
3.  Wait until the setup wizard prepares the setup procedure. A welcome message displays:

<span id="_Toc428787952" class="anchor"></span>Figure 3: CCR Setup Wizard Welcome Message

![](or-3-406-icd-10-ptf-modifications-installation-guide/005.png)

4.  Click Next to continue the installation.

> The Select Destination Location dialog displays:

<span id="_Toc428787953" class="anchor"></span>Figure 4: Select Destination Location Dialog Box

![](or-3-406-icd-10-ptf-modifications-installation-guide/006.png)

5.  Select the directory in which to install the CCR GUI. We recommend that you accept the default directory: C:\Program Files\VistA\Clinical Case Registries\\.

> To select a different location, click Browse… and select the desired directory.

6.  Click Next to continue the installation.

> The Select Start Menu Folder dialog displays:

<span id="_Toc428787954" class="anchor"></span>Figure 5: Select Start Menu Folder Dialog Box

> ![](or-3-406-icd-10-ptf-modifications-installation-guide/007.png)

7.  Select the Start Menu Folder. We recommend that you accept the default directory: Clinical Case Registries.

> To select a different location, click Browse… and select the directory.

8.  Click Next to continue the installation.

> The Select Additional Tasks dialog appears:

<span id="_Toc428787955" class="anchor"></span>Figure 6: Select Additional Tasks Dialog Box

> ![](or-3-406-icd-10-ptf-modifications-installation-guide/008.png)

9.  If you want a desktop icon, leave the checkbox checked; otherwise, clear the checkbox.
10. Click Next to continue the installation.

> The Ready to Install dialog displays:

<span id="_Toc428787956" class="anchor"></span>Figure 7: Ready to Install Dialog Box

![](or-3-406-icd-10-ptf-modifications-installation-guide/009.png)

11. Review the installation settings and click Install to proceed.

> The Wizard finishes the installation and a confirmation screen displays:

<span id="_Toc428787957" class="anchor"></span>Figure 8: CCR Finish Installation Message

![](or-3-406-icd-10-ptf-modifications-installation-guide/010.png)

12. Click Finish.

If you installed the CCR GUI on a file server (recommended), continue to Section 5.4, Continue Installing New CCR GUI on File Server, below.

If you installed the CCR GUI on user workstations (not recommended), skip down to Section 5.5, Configure CCR Desktop Application Parameters.

## Continue Installing New CCR GUI on File Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you installed the CCR GUI on a file server using the instructions in Section 5.3, Install New CCR GUI, then continue the installation using the instructions below.

> **NOTE:** If you have previously set up the CPRS Tools menu (as for a previous version of CCR), you should not have to perform this step and installation of the CCR GUI is completed.

13. Add the corresponding item to the CPRS Tool menu using the CPRS GUI Tool Menu Items \[ORW TOOL MENU ITEMS\] option.

> It is recommended that you add the item at “User” level.

> If you used the default directory for the installation, the “Name=Command” parameter should look like this:

Clinical Case Registries="C:\Program Files\VistA\Clinical Case Registries\ClinicalCaseRegistries.exe" /S="{*Server IP Address*}" /P={*RPC Broker Port*}

> Below is a typical configuration example:

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT320

Select OPTION NAME: ORW TOOL MENU ITEMS

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[HINES DEVELOPMENT\]

4 System SYS \[DEV.DEV.FO-HINES.MED.VA.GOV\]

9 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 1

Select NEW PERSON NAME: CCRUSER,ONE

------ Setting CPRS GUI Tools Menu for User: CCRUSER,ONE -------

Select Sequence: 10

Are you adding 10 as a new Sequence? Yes// \<RET\>

Sequence: 10// \<RET\>

Name=Command: Clinical Case Registries="C:\Program Files\VistA\Clinical Case Registries\ClinicalCaseRegistries.exe" /S="10.3.29.201" /P=9200

Select Sequence: \<RET\>

> For more details, please refer to the GUI Tool Menu Items section of the Computerized Patient Record System (CPRS) v1.0 Setup Guide on the VDL: <http://www.va.gov/vdl/application.asp?appid=61>.

> NOTE: You can also use other command-line parameters described in Section 5.6, CCR Command Line Switches, below to further customize the menu items (limit access to a single registry, disable CCOW, etc.).

## Configure CCR Desktop Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Follow these instructions <u>only</u> if you elected to install the GUI on user workstations (not recommended). If you installed the CCR GUI on a file server (recommended), skip this section.

There are two ways to configure the GUI for those users who are coordinators of both Hepatitis C and HIV registries:

1.  Single shortcut: This is the default. A single shortcut is created on the desktop. When the GUI is launched (or when File, Open is selected from the menu), the user selects the desired registry from the list.
2.  Separate shortcuts: Two separate shortcuts are created, one for the Hepatitis C registry and one for the HIV registry. A command-line switch in each shortcut allows access only to a single registry. As a result, the registry selection dialog box is not displayed, and the corresponding registry is opened automatically. This can be accomplished by adding the /R parameter after the executable name in the Target field of the shortcut.

> For example:

<span id="_Toc428787958" class="anchor"></span>Figure 9: Configuring CCR Desktop Parameters

![](or-3-406-icd-10-ptf-modifications-installation-guide/011.png)

> The Target field should read:

"C:\Program Files\VistA\Clinical Case Registries\ClinicalCaseRegistries.exe" /R="VA HEPC"

## CCR Command Line Switches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can get a list of command-line “switches” supported by the CCR GUI by running the application with the /? or /h parameter.

For example:

Start \| Run \| "C:\Program Files\VistA\Clinical Case Registries\ClinicalCaseRegistries. exe" /?

> **NOTE:** Notice the use of quotation marks around the “target” application name. These are required when using this method because the C:\Program Files\VistA directory is typically not in the *path* (the list of directories which the operating system searches for executable files).

<span id="_Toc428787959" class="anchor"></span>Figure 10: CCR Command Line Switches

![](or-3-406-icd-10-ptf-modifications-installation-guide/012.png)

<table>
<caption><p><span id="_Toc428787971" class="anchor"></span>Table 12: DG*5.3*884 Checksums</p></caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Switch</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>/?, -?, /h, -h</td>
<td>Show a list of command-line parameters.</td>
</tr>
<tr class="even">
<td>/debug, -debug</td>
<td>Run the application in debug mode.</td>
</tr>
<tr class="odd">
<td>/noccow, /ccow=off,<br />
-noccow, -ccow=off</td>
<td>Completely disable CCOW functionality.</td>
</tr>
<tr class="even">
<td>/patientonly, /ccow=patientonly,<br />
-patientonly,<br />
-ccow=patientonly</td>
<td>Disable user context functionality.</td>
</tr>
<tr class="odd">
<td>/port=, /p=, P=,<br />
-port=, -p=</td>
<td>Port number of the Remote Procedure Call Broker (RPC) listener.</td>
</tr>
<tr class="even">
<td>/registry=, /r=, R=,<br />
-registry=, -r=</td>
<td>Registry name.</td>
</tr>
<tr class="odd">
<td>/server=, /r=, S=,<br />
-server=, -s=</td>
<td>Server name or IP address of the RPC Broker listener.</td>
</tr>
</tbody>
</table>

<span id="_Toc428787971" class="anchor"></span>Table 12: DG\*5.3\*884 Checksums

# Back-Out and Roll-Back Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out and roll-back procedures for the ICD-10 PTF Modifications project are complex since the software distribution is comprised of six patches, which are being released within a single Kernel Installation and Distribution System (KIDS) multi-package build (i.e. host file). Registration/Admission Discharge Transfer (ADT) patch DG\*5.3\*884 makes significant changes to VistA software components such as routines, data dictionaries, cross-references, and input templates. In addition, Clinical Case Registries (CCR) patch ROR\*1.5\*25 includes a revised Graphical User Interface (GUI) application.

The general strategy for back-out and roll-back procedures is to first contact the VA Help Desk at 1-888-596-4357 for support or assistance. Based on the severity of the issue reported, it may be necessary for both the application sustainment team and the ICD-10 PTF Modifications project team to be involved in providing direct support and technical solutions for a site’s unique problem. This may also include issuance of an emergency patch to correct or remove software components and to perform restoration of data with a database clean-up process.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During installation, if the option to back up routines was run as directed in Section 3.8.1, Backup a Transport Global, then routines have the ability to be restored from the “backup” MailMan message that was generated. However, the KIDS installation process does not perform a save of other VistA components, such as data dictionary, cross-reference, and template changes, etc.

To uninstall the CCR GUI provided as a Windows application, please use the Programs and Features, Uninstall or change a program option of the Windows Control panel (see above Section 5.2.3, Instructions to Uninstall Previous CCR GUI Versions).

> **NOTE:** After the CCR client application is uninstalled, you may need to re-install the previous version of the client software.

Prior to attempting back-out of any ICD-10 PTF Modifications software components, please contact the VA Help Desk at 1-888-596-4357 for support or assistance.

## Roll-Back Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The roll-back procedures for the ICD-10 PTF Modifications are complicated due to the numerous data dictionary changes, global updates, and data transmissions from VistA to offsite data stores. Patch DG\*5.3\*884 and any installed dependent patch changes that follow patch DG\*5.3\*884 need to be taken out in reverse of the order in which these patches were installed; routines and data dictionary modifications and populated data must also be rolled back in reverse order.

Please contact the VA Help Desk at 1-888-596-4357 for support or assistance regarding roll-back procedures. Based on the severity of the issue reported, it may be necessary for both the application sustainment team and the ICD-10 PTF Modifications project team to be involved in providing direct support and technical solutions for a site’s unique problem.  This may also include issuance of an emergency patch to perform restoration of data with a database clean-up process.

1.  <span id="_bookmark53" class="anchor"></span>APPENDIX A – Reminder Management Mail Group

## Locate Reminder Management Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the FileMan option INQUIRE TO FILE ENTRIES, obtain the name of the REMINDER MANAGEMENT MAILGROUP defined in the CLINICAL REMINDERS PARAMETERS (#800) file entry.  NOTE: This mail group name may not be the same on all VistA instances.

Example:

ALBANYTST:DEVESS\>D P^DI

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES 

OUTPUT FROM WHAT FILE: CLINICAL REMINDER PARAMETERS//

         

Select CLINICAL REMINDER PARAMETERS SITE PARAMETERS: 1  

         ...OK? Yes//   (Yes)

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes//   (Yes)

Include COMPUTED fields:  (N/Y/R/B): NO//  - No record number (IEN), no Computed

Fields

SITE PARAMETERS: 1

URL: <http://www.oqp.med.va.gov/cpg/cpg.htm>

  WEB SITE TITLE: OQP Clinical Guidelines

DEFAULT REMINDER DISCLAIMER:   The following disease screening, immunization and patient education recommendations are offered as guidelines to assist in your practice.  These are only recommendations, not practice standards.  The appropriate utilization of these for your individual patient must be based on clinical judgment and the patient's current status. 

 FORMATTED DISCLAIMER:  

 The following disease screening, immunization and patient education

recommendations are offered as guidelines to assist in your practice.

These are only recommendations, not practice standards.  The appropriate utilization of these for your individual patient must be based on clinical judgment and the patient's current status.

  FULL SSN: NO

  <span class="mark">REMINDER MANAGEMENT MAILGROUP: PXRM Management</span>

  MAXIMUM NUMBER OF MH QUESTIONS: 35  MAXIMUM NUMBER OF INDEX ERRORS: 200

  INITIAL MST SYNCH COMP DATE: FEB 25, 2002@14:27:19

  INITIAL MST SYNCH UPDATE COUNT: 0

  DAILY MST SYNC COMP DATE: JUN 02, 2010@11:53:10

  DAILY MST SYNCH UPDATE COUNT: 0

  INITIAL MST SYNCH START DATE: FEB 25, 2002@14:27:19

## Add Installer to Reminder Management Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add yourself as a member of the mail group found in Step A.1 above. In this example, the name of the mail group is “PXRM Management.”

Example:

ALBANYTST:DEVESS\>D P^DI

VA FileMan 22.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: CLINICAL REMINDER PARAMETERS// MAIL GROUP

(315 entries)

EDIT WHICH FIELD: ALL//

Select MAIL GROUP NAME: PXRM Management <span class="mark">\<\<Enter mail group name found in REMINDER MANAGEMENT MAILGROUP (#3) field in CLINICAL REMINDER PARAMETERS file (#800) (name of mail group may vary at each site).</span>

NAME: PXRM Management//

Select MEMBER: DGTEST,PATONE// DGTEST,PATTWO<span class="mark">\<\<Enter your name as a member.</span>

Are you adding 'DGTEST,PATTWO' as a new MEMBER (the 9TH for this MAIL GROUP)?

No// <span class="mark">Y (Yes)</span>

TYPE:

Select MEMBER: ^

Select MAIL GROUP NAME:

## Remove Installer From Reminder Management Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the background job finishes rebuilding the Clinical Reminders Global Index and the results message(s) is received, remove yourself as a member of the mail group found in A.1 above. In this example, the name of the mail group is “PXRM Management.”

Example:

ALBANYTST:DEVESS\>D P^DI

VA FileMan 22.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: MAIL GROUP// MAIL GROUP (315 entries)

EDIT WHICH FIELD: ALL//

Select MAIL GROUP NAME: PXRM Management<span class="mark">\<\<Enter mail group name found in REMINDER MANAGEMENT MAILGROUP (#3) field in CLINICAL REMINDER PARAMETERS file (#800) (name of mail group may vary at each site).</span>

NAME: PXRM Management//

Select MEMBER: DGTEST,PATONE// DGTEST,PATTWO<span class="mark">\<\<Enter your name.</span>

...OK? Yes// (Yes)

MEMBER: DGTEST,PATTWO// @<span class="mark">\<\<Enter ‘@’ sign to delete member.</span>

SURE YOU WANT TO DELETE THE ENTIRE MEMBER? <span class="mark">Y (Yes)</span>

Select MEMBER: ^

Select MAIL GROUP NAME:

## Clinical Reminders Mail Group Message – Index Rebuild Status (Example)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: Index for global ^DGPT( successfully built \[#120\] 07/08/15@16:48 6 lines

From: DGUSER,TEST In 'IN' basket. Page 1 \*New\*

----------------------------------------------------------------------------------

Build of Clinical Reminders index for global ^DGPT( completed.

Build finished at 07/08/2015@16:48:41

2128929 entries were created.

Elapsed time: 0:05:29

1 errors were encountered.

Another MailMan message will contain the error information.

Enter message action (in IN basket): Ignore//

## Clinical Reminders Mail Group Message – Entries Could Not Be Indexed (Example)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: CLINICAL REMINDER INDEX BUILD ERROR(S) FOR GLOBAL ^DGPT( \[#121\] 07/08/15@16:48 1 line

From: DGUSER,TEST In 'IN' basket. Page 1 \*New\*

---------------------------------------------------------------------------------------------

GLOBAL: ^DGPT( ENTRY: 30212;S;2;0 has the invalid code -1^Invalid IEN for File

Enter message action (in IN basket): Ignore//

2.  <span id="Appendix_B" class="anchor"></span>APPENDIX B – Captured Install
3.  <span id="3.1_Load_Export_Global_^LEXM" class="anchor"></span>Load KIDS Distribution

Select OPTION NAME: Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System Option: Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: Load a Distribution

Enter a Host File: /home/cheyl146/ICD_10_PTF_MODIFICATIONS.KID

KIDS Distribution saved on Aug 20, 2015@17:16:54

Comment: DG\*5.3\*884,GMTS\*2.7\*111,IB\*2\*522,LR\*5.2\*442,ROR\*1.5\*25,OR\*3\*406

This Distribution contains Transport Globals for the following Package(s):

Build DG\*5.3\*884 has been loaded before, here is when:

DG\*5.3\*884 Install Completed

was loaded on Jul 22, 2015@09:02:42

OK to continue with Load? NO// YES

Build GMTS\*2.7\*111 has been loaded before, here is when:

GMTS\*2.7\*111 Install Completed

was loaded on Jul 22, 2015@09:02:44

OK to continue with Load? NO// YES

Build IB\*2.0\*522 has been loaded before, here is when:

IB\*2.0\*522 Install Completed

was loaded on Jul 22, 2015@09:02:44

OK to continue with Load? NO// YES

Build LR\*5.2\*442 has been loaded before, here is when:

LR\*5.2\*442 Install Completed

was loaded on Jul 22, 2015@09:02:44

OK to continue with Load? NO// YES

Build ROR\*1.5\*25 has been loaded before, here is when:

ROR\*1.5\*25 Install Completed

was loaded on Jul 22, 2015@09:02:44

OK to continue with Load? NO// YES

Build OR\*3.0\*406 has been loaded before, here is when:

OR\*3.0\*406 Install Completed

was loaded on Jul 22, 2015@09:02:44

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

Build DG\*5.3\*884 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES//

DG\*5.3\*884

Will first run the Environment Check Routine, DG884P

\>\>\> Check programmer variables...Successful

\>\>\> Checking number of entries in some DRG files...

No discrepancies found.

\>\>\> Checking for 'Q-PTI.VA.GOV entry in DOMAIN (#4.2)...Successful

GMTS\*2.7\*111

IB\*2.0\*522

LR\*5.2\*442

ROR\*1.5\*25

OR\*3.0\*406

Use INSTALL NAME: DG\*5.3\*884 to install this Distribution.

4.  <span id="_Toc428788036" class="anchor"></span>Captured Times

KIDS Distribution saved on Mar 17, 2015@17:45:21

This Distribution was loaded on Mar 17, 2015@17:52:33 with header of

DG\*5.3\*884,GMTS\*2.7\*111,IB\*2\*522,LR\*5.2\*442,ROR\*1.5\*25,OR\*3\*406

5.  <span id="3.3_Install_KIDS_Distribution" class="anchor"></span>Install KIDS Distribution

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: Install Package(s)

Select INSTALL NAME: DG\*5.3\*884 8/20/15@17:23

=\> DG\*5.3\*884,GMTS\*2.7\*111,IB\*2\*522,LR\*5.2\*442,ROR\*1.5\*25,OR\*3\*406 ;Crea

This Distribution was loaded on Aug 20, 2015@17:23 with header of

DG\*5.3\*884,GMTS\*2.7\*111,IB\*2\*522,LR\*5.2\*442,ROR\*1.5\*25,OR\*3\*406 ;Created on

Aug 20, 2015@17:16:54

It consisted of the following Install(s):

DG\*5.3\*884 GMTS\*2.7\*111 IB\*2.0\*522 LR\*5.2\*442 ROR\*1.5\*25

OR\*3.0\*406

Checking Install for Package DG\*5.3\*884

Will first run the Environment Check Routine, DG884P

\>\>\> Check programmer variables...Successful

\>\>\> Checking number of entries in some DRG files...

No discrepancies found.

\>\>\> Checking for 'Q-PTI.VA.GOV entry in DOMAIN (#4.2)...Successful

Install Questions for DG\*5.3\*884

Incoming Files:

45 PTF (Partial Definition)

> **NOTE:** You already have the 'PTF' File.

45.64 PTF AUSTIN ERROR CODES (including data)

> **NOTE:** You already have the 'PTF AUSTIN ERROR CODES' File.

I will OVERWRITE your data with mine.

Checking Install for Package GMTS\*2.7\*111

Install Questions for GMTS\*2.7\*111

Checking Install for Package IB\*2.0\*522

Install Questions for IB\*2.0\*522

Checking Install for Package LR\*5.2\*442

Install Questions for LR\*5.2\*442

Checking Install for Package ROR\*1.5\*25

Install Questions for ROR\*1.5\*25

Checking Install for Package OR\*3.0\*406

Install Questions for OR\*3.0\*406

Want KIDS to INHIBIT LOGONs during the install? NO// YES

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

Enter options you wish to mark as 'Out Of Order': DG PTF BACKGROUND JOB PT

F Background Job

Enter options you wish to mark as 'Out Of Order':

Enter protocols you wish to mark as 'Out Of Order':

Delay Install (Minutes): (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME (CRT)

--------------------------------------------------------------------------------

Install Started for DG\*5.3\*884 :

Aug 20, 2015@17:23:44

Build Distribution Date: Aug 20, 2015

Installing Routines:

Aug 20, 2015@17:23:45

Running Pre-Install Routine: PRE^DG884P

\>\>\> Start removal of PTF Operation Code "AO" cross-reference...

"AO" removal completed.

\>\>\> Checking number of entries in some DRG files...

No discrepancies found.

\>\>\> Creating new 'PTI' mail group...

> **WARNING:** Mail Group PTI already exists.

Since the mail group exists, no action is required.

\>\>\> Updating PTF125 entry in TRANSMISSION ROUTER (#407.7) file.

Setting TRANSMIT=NO for (existing) receiving user@Q-PTT.VA.GOV.

Creating new receiving user@Q-PTI.VA.GOV.

Installing Data Dictionaries: .

Aug 20, 2015@17:23:47

Installing Data:

Aug 20, 2015@17:23:47

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing REMOTE PROCEDURE

Aug 20, 2015@17:23:47

Running Post-Install Routine: POST^DG884P

\>\>\> Rebuild PTF portion of the Clinical Reminders Global Index...

The DG\*5.3\*884 patch has previously been installed.

Skipping another rebuild of the PTF portion of the index.

\>\>\> Re-compiling input templates...

Compiling DG701 Input Template of File 45..........

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED..

'DGPTX7' ROUTINE FILED...........

'DGPTX73' ROUTINE FILED.............

'DGPTX74' ROUTINE FILED..

'DGPTX75' ROUTINE FILED.

'DGPTX76' ROUTINE FILED.

Compiling DG701-10D Input Template of File 45..........

'DGX71' ROUTINE FILED..

'DGX7' ROUTINE FILED...........

'DGX72' ROUTINE FILED...........

'DGX73' ROUTINE FILED...........

'DGX74' ROUTINE FILED...........

'DGX75' ROUTINE FILED........

'DGX76' ROUTINE FILED.

'DGX77' ROUTINE FILED.

'DGX78' ROUTINE FILED.

Compiling DG401 Input Template of File 45..

'DGPTX4' ROUTINE FILED.............

'DGPTX41' ROUTINE FILED.

'DGPTX42' ROUTINE FILED.

Compiling DG401-10P Input Template of File 45..

'DGX4' ROUTINE FILED..............

'DGX41' ROUTINE FILED...........

'DGX43' ROUTINE FILED.

'DGX42' ROUTINE FILED..........

'DGX44' ROUTINE FILED.

'DGX45' ROUTINE FILED.

Compiling DG501F Input Template of File 45..

'DGX5F' ROUTINE FILED.............

'DGX5F1' ROUTINE FILED.................

'DGX5F2' ROUTINE FILED..........

'DGX5F3' ROUTINE FILED.

'DGX5F4' ROUTINE FILED.

Compiling DG501 Input Template of File 45..

'DGPTX5' ROUTINE FILED............

'DGPTX52' ROUTINE FILED..

'DGPTX51' ROUTINE FILED.....................

'DGPTX53' ROUTINE FILED....

'DGPTX54' ROUTINE FILED.

'DGPTX55' ROUTINE FILED.

Compiling DG501-10D Input Template of File 45..

'DGX5' ROUTINE FILED............

'DGX52' ROUTINE FILED..

'DGX51' ROUTINE FILED..........

'DGX54' ROUTINE FILED..

'DGX53' ROUTINE FILED...........

'DGX55' ROUTINE FILED...........

'DGX56' ROUTINE FILED...........

'DGX57' ROUTINE FILED.....................

'DGX58' ROUTINE FILED....

'DGX59' ROUTINE FILED.

'DGX510' ROUTINE FILED.

Compiling DG501F-10D Input Template of File 45..

'DGX5FD' ROUTINE FILED.............

'DGX5FD1' ROUTINE FILED..........

'DGX5FD3' ROUTINE FILED..

'DGX5FD2' ROUTINE FILED...........

'DGX5FD4' ROUTINE FILED...........

'DGX5FD5' ROUTINE FILED...........

'DGX5FD6' ROUTINE FILED.................

'DGX5FD7' ROUTINE FILED..........

'DGX5FD8' ROUTINE FILED.

'DGX5FD9' ROUTINE FILED.

Compiling DG601-10P Input Template of File 45..

'DGX6' ROUTINE FILED............

'DGX62' ROUTINE FILED.

'DGX61' ROUTINE FILED............

'DGX63' ROUTINE FILED.......

'DGX64' ROUTINE FILED.

'DGX65' ROUTINE FILED.

Re-compile completed.

Updating Routine file...

The following Routines were created during this install:

DGPTXX

DGPTXX1

DGPTXX10

DGPTXX11

DGPTXX12

DGPTXX13

DGPTXX14

DGPTXX15

DGPTXX16

DGPTXX2

DGPTXX3

DGPTXX4

DGPTXX5

DGPTXX6

DGPTXX7

DGPTXX8

DGPTXX9

DGX5

DGX51

DGX510

DGX52

DGX53

DGX54

DGX55

DGX56

DGX57

DGX58

DGX59

DGX7

DGX71

DGX72

DGX73

DGX74

DGX75

DGX76

DGX77

DGX78

DGX5FD

DGX5FD1

DGX5FD2

DGX5FD3

DGX5FD4

DGX5FD5

DGX5FD6

DGX5FD7

DGX5FD8

DGX5FD9

DGX4

DGX41

DGX42

DGX43

DGX44

DGX45

DGX6

DGX61

DGX62

DGX63

DGX64

DGX65

Updating KIDS files...

DG\*5.3\*884 Installed.

Aug 20, 2015@17:23:48

Not a production UCI

NO Install Message sent

Install Started for GMTS\*2.7\*111 :

Aug 20, 2015@17:23:48

Build Distribution Date: Aug 20, 2015

Installing Routines:

Aug 20, 2015@17:23:48

Updating Routine file...

Updating KIDS files...

GMTS\*2.7\*111 Installed.

Aug 20, 2015@17:23:48

Not a production UCI

NO Install Message sent

Install Started for IB\*2.0\*522 :

Aug 20, 2015@17:23:48

Build Distribution Date: Aug 20, 2015

Installing Routines:

Aug 20, 2015@17:23:48

Updating Routine file...

Updating KIDS files...

IB\*2.0\*522 Installed.

Aug 20, 2015@17:23:48

Not a production UCI

NO Install Message sent

Install Started for LR\*5.2\*442 :

Aug 20, 2015@17:23:48

Build Distribution Date: Aug 20, 2015

Installing Routines:

Aug 20, 2015@17:23:49

Updating Routine file...

Updating KIDS files...

LR\*5.2\*442 Installed.

Aug 20, 2015@17:23:49

Not a production UCI

NO Install Message sent

Install Started for ROR\*1.5\*25 :

Aug 20, 2015@17:23:49

Build Distribution Date: Aug 20, 2015

Installing Routines:

Aug 20, 2015@17:23:49

Running Post-Install Routine: POST^RORP025

POST INSTALL START

Update to ROR METADATA \<SUCCESSFUL\>

POST INSTALL COMPLETE

Updating Routine file...

Updating KIDS files...

ROR\*1.5\*25 Installed.

Aug 20, 2015@17:23:49

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*406 :

Aug 20, 2015@17:23:49

Build Distribution Date: Aug 20, 2015

Installing Routines:

Aug 20, 2015@17:23:49

Running Post-Install Routine: POST^ORY406

This patch will establish a default value at the PACKAGE level

for the ORWRP TIME/OCC LIMITS INDV parameter.

These reports in OE/RR REPORT (#101.24) are affected:

ORRPW ADT ADM DC

ORRPW ADT DC DIAG

ORRPW ADT EXP

ORRPW ADT ICD PROC

ORRPW ADT ICD SURG

ORRPW DOD ADT EXP

ORRPW ADT ADM DC complete.

ORRPW ADT DC DIAG complete.

ORRPW ADT EXP complete.

ORRPW ADT ICD PROC complete.

ORRPW ADT ICD SURG complete.

ORRPW DOD ADT EXP complete.

Updating Routine file...

Updating KIDS files...

OR\*3.0\*406 Installed.

Aug 20, 2015@17:23:49

Not a production UCI

Install Completed

6.  <span id="_Toc428788038" class="anchor"></span>Captured Times

Install Started for DG\*5.3\*884: Mar 17, 2015@17:53:11

OR\*3.0\*406 Installed: Mar 17, 2015@17:53:15

Install Completed.

7.  <span id="_bookmark59" class="anchor"></span>APPENDIX C – Checksums
8.  <span id="4.1_Multi-Package_Distribution_Routine_S" class="anchor"></span>DG\*5.3\*884 Checksums

The second line of each of these routines will look like:

;;5.3;Registration;\*\*\[PATCH LIST\]\*\*;Aug 13, 1993;Build 19

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

| Routine  | Checksums Before Patch | Checksums After Patch | Patch List (2<sup>nd</sup> Line)                                  |
|----------|------------------------|-----------------------|-------------------------------------------------------------------|
| DG884P   | N/A                    | 172982622             | 884                                                               |
| DGICDGT  | 93717009               | 98953906              | 850, 884                                                          |
| DGICP    | 26601934               | 28102080              | 850, 884                                                          |
| DGPT101  | 13245456               | 16555084              | 8,164,180,247,415,678,696,884                                     |
| DGPT101P | 4327695                | 14198290              | 164,678,664,884                                                   |
| DGPT401  | 8757458                | 22199810              | 164,729,884                                                       |
| DGPT501  | 11578445               | 15677318              | 64,164,529,729,884                                                |
| DGPT501P | 3510968                | 13121491              | 884                                                               |
| DGPT50DI | 7758522                | 12005227              | 510,850,884                                                       |
| DGPT50MS | 4605823                | 6178285               | 142,729,884                                                       |
| DGPT535  | 8073530                | 7151570               | 64,164,729,884                                                    |
| DGPT601  | 17005208               | 21745672              | 64,164,729,850,884                                                |
| DGPT60PR | 4857421                | 4921445               | 510,870,850,884                                                   |
| DGPT701  | 13785418               | 25074534              | 64,164,251,415,729,850,884                                        |
| DGPT701P | 2908139                | 17213050              | 164,415,884                                                       |
| DGPT702  | 2277722                | 12007365              | 884                                                               |
| DGPT70DI | 12136680               | 18406929              | 510,850,884                                                       |
| DGPT70DX | 3873659                | 4054092               | 510,850,884                                                       |
| DGPTAE   | 14522606               | 19185351              | 58,415,884                                                        |
| DGPTAE01 | 9393836                | 10894380              | 58,342,466,664,867,884                                            |
| DGPTAE02 | 19628803               | 26206444              | 8,22,39,114,176,251,247,270,446,418, 482,466,683,729,884          |
| DGPTAE03 | 10987387               | 8625430               | 8,52,164,850,884                                                  |
| DGPTAE04 | 9147597                | 12240703              | 510,744,870,850,884                                               |
| DGPTAEE  | 10892054               | 24445151              | 64,338,678,850,884                                                |
| DGPTAEE1 | 21575685               | 39125544              | 338,565,678,729,664,884                                           |
| DGPTAEE2 | 14351045               | 30765062              | 8,338,415,565,729,664,884                                         |
| DGPTC1   | 26112849               | 29467995              | 37,413,643,701,850,905,884                                        |
| DGPTC2   | 11527513               | 12393502              | 58,189,643,850,884                                                |
| DGPTDDCR | 88922399               | 172287843             | 478,862,884                                                       |
| DGPTDRG  | 50130642               | 52220100              | 60,441,510,559,599,606,669,729,850,884                            |
| DGPTF099 | 11108603               | 12766033              | 884                                                               |
| DGPTF09X | 7765866                | 8106091               | 58,884                                                            |
| DGPTF1   | 34378858               | 35051519              | 69,114,195,397,342,415,565,664,884                                |
| DGPTF2   | 17166598               | 26229374              | 37,342,643,861,850,884                                            |
| DGPTF4   | 30195949               | 30569279              | 114,115,397,510,517,478,683,775,850,884                           |
| DGPTF41  | 10056872               | 11239143              | 64,635,729,850,884                                                |
| DGPTF5   | 6981494                | 6998580               | 669,701,744,868,850,884                                           |
| DGPTFAPI | 6968721                | 6178065               | 309,510,850,884                                                   |
| DGPTFD   | 19169268               | 23594019              | 60,441,510,785,850,884                                            |
| DGPTFIC  | 52898785               | 57159054              | 510,559,599,669,704,744,832,850,884                               |
| DGPTFJC  | 63564376               | 64477474              | 158,510,517,590,636,635,701,729,785,850,884                       |
| DGPTFM   | 72739353               | 81427420              | 510,517,590,594,606,635,683,696,664,850,884                       |
| DGPTFM0  | 10244116               | 17632645              | 510,517,850,884                                                   |
| DGPTFM1  | 18916672               | 36433048              | 114,517,635,850,884                                               |
| DGPTFM4  | 31864138               | 35748755              | 114,195,397,510,565,775,664,759,850,884                           |
| DGPTFM5  | 13820382               | 15479197              | 510,606,850,884                                                   |
| DGPTFM6  | 28907671               | 36495035              | 164,510,729,850,898,884                                           |
| DGPTFM7  | 21219043               | 21631380              | 78,590,594,683,729,884                                            |
| DGPTFMO  | 32031244               | 42799242              | 195,397,510,590,594,606,683,729,664,850,884                       |
| DGPTFQWK | 21436549               | 26393553              | 517,594,635,729,850,884                                           |
| DGPTFTR  | 24216608               | 55260983              | 37,415,530,601,614,645,787,850,884                                |
| DGPTFTR3 | 13488826               | 13787675              | 568,884                                                           |
| DGPTFUT  | N/A                    | 38258055              | 884                                                               |
| DGPTFUT1 | N/A                    | 3593858               | 884                                                               |
| DGPTFVC1 | 39436670               | 42593524              | 52,58,79,114,164,400,342,466,415,493, 512,510,544,629,817,850,884 |
| DGPTFVC3 | 10783685               | 11851601              | 164,729,884                                                       |
| DGPTIC10 | 100685699              | 94542788              | 850,905,884                                                       |
| DGPTOD1  | 9627005                | 9059489               | 158,238,375,744,884                                               |
| DGPTODCM | 17786774               | 17949456              | 375,884                                                           |
| DGPTOLC2 | 25585897               | 35887229              | 164,510,559,599,729,850,884                                       |
| DGPTR0   | 26425804               | 26801939              | 114,247,338,342,510,524,565,678,729,664,850,884                   |
| DGPTR2   | 22938579               | 31431930              | 183,338,423,510,636,729,850,884                                   |
| DGPTR3   | 4042057                | 3570598               | 183,729,884                                                       |
| DGPTR4   | 20498105               | 21708537              | 338,423,415,510,565,645,729,664,850,884                           |
| DGPTRI0  | 26605957               | 27141499              | 850,884                                                           |
| DGPTRI1  | 37319384               | 45682125              | 850,884                                                           |
| DGPTRI2  | 26956533               | 35680960              | 850,884                                                           |
| DGPTRI3  | 26611263               | 26721345              | 850,884                                                           |
| DGPTRI4  | 32872225               | 69886418              | 850,884                                                           |
| DGPTRNU  | N/A                    | 55750657              | 884                                                               |
| DGPTRNU1 | N/A                    | 7245862               | 884                                                               |
| DGPTRPO  | 17649764               | 20840184              | 884                                                               |
| DGPTSCAN | 23143464               | 25305178              | 29,64,114,189,729,850,884                                         |
| DGPTSUDO | 23608581               | 31462240              | 441,510,478,785,850,884                                           |
| DGPTTS   | 17997399               | 24184788              | 26,61,164,510,850,884                                             |
| DGPTTS1  | 23805966               | 28870180              | 26,64,418,510,478,850,884                                         |
| DGPTTS2  | 14533867               | 22200737              | 549,478,884                                                       |

<span id="_Toc428787972" class="anchor"></span>Table 13: GMTS\*2.7\*111 Checksums

9.  <span id="_Toc428788041" class="anchor"></span>GMTS\*2.7\*111 Checksums

The second line of each of these routines will look like:

;;2.7;Health Summary;\*\*\[PATCH LIST\]\*\*;Oct 20, 1995;Build 4

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

| Routine  | Checksums Before Patch | Checksums After Patch | Patch List (2<sup>nd</sup> Line) |
|----------|------------------------|-----------------------|----------------------------------|
| GMTSDGA  | 11914941               | 16655517              | 28,49,71,101,111                 |
| GMTSDGC1 | 15467864               | 21632270              | 5,35,47,71,101,111               |
| GMTSDGC2 | 7198971                | 8062721               | 28,49,71,101,111                 |
| GMTSDGP  | 12132145               | 14004206              | 28,49,60,71,101,111              |
| GMTSPXU1 | 17119835               | 24643576              | 10,37,71,86,101,111              |

<span id="_Toc428787973" class="anchor"></span>Table 14: IB\*2.0\*522 Checksums

10. <span id="_Toc428788042" class="anchor"></span>IB\*2.0\*522 Checksums

The second line of each of these routines will look like:

;;2.0;INTEGRATED BILLING;\*\*\[PATCH LIST\]\*\*;21-MAR-94;Build 1

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

| Routine | Checksums Before Patch | Checksums After Patch | Patch List (2<sup>nd</sup> Line)                                     |
|---------|------------------------|-----------------------|----------------------------------------------------------------------|
| IBCD3   | 32514703               | 34628725              | 14,55,52,91,106,125,51,148,160,137, 210,245,260,405,384,516,522      |
| IBCD4   | 18076054               | 14091278              | 14,80,106,160,309,276,347,522                                        |
| IBCRBG  | 66489178               | 68718544              | 52,80,106,51,142,159,210,245,382,389,461,522                         |
| IBCSC4A | 32672806               | 26406207              | 106,228,339,479,522                                                  |
| IBCSC4B | 36503632               | 14226360              | 210,228,304,479,522                                                  |
| IBCSC4D | 75384760               | 76016238              | 55,62,91,106,124,51,210,403,400,461,516,522                          |
| IBCSC4E | 45259248               | 48958417              | 8,106,121,124,210,266,403,479,522                                    |
| IBCSC4F | 26386041               | 34285009              | 106,403,400,522                                                      |
| IBCU7   | 111564056              | 113207672             | 62,52,106,125,51,137,210,245,228,260,348,371,432,447,488,461,516,522 |

<span id="_Toc428787974" class="anchor"></span>Table 15: LR\*5.2\*442 Checksums

11. <span id="_Toc428788043" class="anchor"></span>LR\*5.2\*442 Checksums

The second line of each of these routines will look like:

;;5.2;LAB SERVICE;\*\*\[PATCH LIST\]\*\*;Sep 27, 1994;Build 1

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

| Routine  | Checksums Before Patch | Checksums After Patch | Patch List (2<sup>nd</sup> Line) |
|----------|------------------------|-----------------------|----------------------------------|
| LRAPQAT1 | 5116733                | 5639030               | 201,315,422,442                  |
| LREPI3   | 50368609               | 50657708              | 132,175,260,281,320,315,421,442  |
| LREPI5   | 7519412                | 9871956               | 281,315,421,442                  |

<span id="_Toc428787975" class="anchor"></span>Table 16: OR\*3.0\*406 Checksums

12. <span id="_Toc428788044" class="anchor"></span>OR\*3.0\*406 Checksums

The second line of each of these routines will look like:

;;3.0;ORDER ENTRY/RESULTS REPORTING;\*\*\[PATCH LIST\]\*\*;Dec 17, 1997;Build 1

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

| Routine | Checksums Before Patch | Checksums After Patch | Patch List (2<sup>nd</sup> Line) |
|---------|------------------------|-----------------------|----------------------------------|
| ORY406  | N/A                    | 6519234               | 406                              |

<span id="_Toc428787976" class="anchor"></span>Table 17: ROR\*1.5\*25 Checksums

13. <span id="_Toc428788045" class="anchor"></span>ROR\*1.5\*25 Checksums

The second line of each of these routines will look like:

;;1.5;CLINICAL CASE REGISTRIES;\*\*\[patch list\]\*\*;Feb 17, 2006;Build 17

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

| Routine  | Checksums Before Patch | Checksums After Patch | Patch List (2<sup>nd</sup> Line)    |
|----------|------------------------|-----------------------|-------------------------------------|
| RORHL081 | 53807054               | 53447433              | 19,25                               |
| RORP025  | N/A                    | 6132875               | 25                                  |
| RORUPD09 | 11144111               | 11230376              | 18,25                               |
| RORUTL11 | 4209534                | 4346474               | 13,14,15,17,18,20,19,21,22,24,27,25 |
| RORX013A | 78520195               | 79404657              | 1,13,19,21,25                       |
| RORX015A | 96662849               | 90387034              | 1,8,13,19,21,25                     |
| RORXU010 | 16438309               | 14122091              | 8,19,25                             |

<span id="_Toc414369012" class="anchor"></span>Table 18: Acronyms and Definitions

14. <span id="Appendix_D" class="anchor"></span>Appendix D – Acronyms and Definitions

<table>
<caption>Acronyms and DefinitionsAcronyms and Definitions</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADT</td>
<td>Registration, Enrollment, Eligibility, Admission, Discharge, and Transfer</td>
</tr>
<tr class="even">
<td>AITC</td>
<td>Austin Information Technology Center</td>
</tr>
<tr class="odd">
<td>AP</td>
<td>Anatomic Pathology</td>
</tr>
<tr class="even">
<td>CCOW</td>
<td><p>Clinical Context Object Workgroup:</p>
<p>CCOW is an HL7 standard protocol designed to enable disparate applications to synchronize in real-time, and at the user-interface level. It is vendor independent and allows applications to present information at the desktop and/or portal level in a unified way.</p>
<p>CCOW is the primary standard protocol in healthcare to facilitate a process called "Context Management." Context Management is the process of using particular "subjects" of interest (e.g., user, patient, clinical encounter, charge item, etc.) to 'virtually' link disparate applications so that the end-user sees them operate in a unified, cohesive way.</p>
<p>Context Management can be utilized for both CCOW and non-CCOW compliant applications. The CCOW standard exists to facilitate a more robust, and near "plug-and-play" interoperability across disparate applications.</p>
<p>Context Management is often combined with Single Sign-On applications in the healthcare environment, but the two are discrete functions. Single Sign On is the process that enables the secure access of disparate applications by a user through use of a single authenticated identifier and password.</p></td>
</tr>
<tr class="odd">
<td>CCR</td>
<td>Clinical Case Registries</td>
</tr>
<tr class="even">
<td>DG</td>
<td>Registration Namespace</td>
</tr>
<tr class="odd">
<td>EPI</td>
<td>Emerging Pathogens Initiative</td>
</tr>
<tr class="even">
<td>GMTS</td>
<td>Health Summary Namespace</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>Graphical User Interface</td>
</tr>
<tr class="even">
<td>HS</td>
<td>Health Summary</td>
</tr>
<tr class="odd">
<td>IB</td>
<td>Integrated Billing</td>
</tr>
<tr class="even">
<td>ICD-10</td>
<td>International Classification of Diseases, 10<sup>th</sup> Revision</td>
</tr>
<tr class="odd">
<td>KIDS</td>
<td>Kernel Installation and Distribution System</td>
</tr>
<tr class="even">
<td>LR</td>
<td>Lab Service (Laboratory) Namespace</td>
</tr>
<tr class="odd">
<td>OE/RR</td>
<td>Order Entry/Results Reporting</td>
</tr>
<tr class="even">
<td>OR</td>
<td>Order Entry/Results Reporting Namespace</td>
</tr>
<tr class="odd">
<td>POA</td>
<td>Present on Admission</td>
</tr>
<tr class="even">
<td>PTF</td>
<td>Patient Treatment File</td>
</tr>
<tr class="odd">
<td>ROR</td>
<td>Clinical Case Registries Namespace</td>
</tr>
<tr class="even">
<td>TBD</td>
<td>To Be Determined</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
<tr class="odd">
<td>VMP</td>
<td>VistA Maintenance Project</td>
</tr>
</tbody>
</table>

Acronyms and DefinitionsAcronyms and Definitions