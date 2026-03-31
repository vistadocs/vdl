---
title: PXRM*2*27 Homelessness Screening & Lipid Statin Rx CVD/DM Reminders Installation Guide)
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Homelessness Screening & Lipid Statin Rx CVD/DM Reminders )
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*27
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 2
description: ![](pxrm-2-27-homelessness-screening-lipid-statin-rx-cvd-dm-reminders-installation-g/001.png)
audience: 
keywords: 
  - contents
  - table
  - reminder
  - dialog
  - install
  - finding
  - homelessness
  - homeless
  - element
  - management
page_count: 0
word_count: 8528
section_count: 15
table_count: 7
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: October 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_27_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_27_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-27-homelessness-screening-lipid-statin-rx-cvd-dm-reminders-installation-g/001.png)

Homelessness Screening

&

Lipid Statin Rx CVD/DM Reminders

PXRM\*2.0\*27

INSTALLATION and SETUP GUIDE

October 2012

Product Development

Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Pre-Installation](#pre-installation)
  - [Required Software for PXRM\2\27](#required-software-for-pxrm227)
  - [## Related Documentation](#related-documentation)
    - [Web Sites](#web-sites)
  - [# Installation](#installation)
  - [This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes](#this-patch-can-be-installed-with-users-on-the-system-but-it-should-be-done-during-non-peak-hours-estimated-installation-time-10-15-minutes)
  - [Retrieve the host file from one of the following locations (with the ASCII file type):](#retrieve-the-host-file-from-one-of-the-following-locations-with-the-ascii-file-type)
  - [Install the patch first in a training or test account.](#install-the-patch-first-in-a-training-or-test-account)
  - [Load the distribution.](#load-the-distribution)
  - [## Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
  - [## Install the build.](#install-the-build)
  - [## Install File Print](#install-file-print)
  - [## Build File Print](#build-file-print)
  - [Post-installation routines](#post-installation-routines)
- [Post-Install Set-up Instructions](#post-install-set-up-instructions)
- [After the installation of patch PXRM\2.0\27, do the following steps to set up the VA-Homelessness Screening reminder](#after-the-installation-of-patch-pxrm2027-do-the-following-steps-to-set-up-the-va-homelessness-screening-reminder)
- [CF Reminder Computed Finding Management ...](#cf-reminder-computed-finding-management)
- [RM Reminder Definition Management ...](#rm-reminder-definition-management)
- [SM Reminder Sponsor Management ...](#sm-reminder-sponsor-management)
- [TXM Reminder Taxonomy Management ...](#txm-reminder-taxonomy-management)
- [TRM Reminder Term Management ...](#trm-reminder-term-management)
- [LM Reminder Location List Management ...](#lm-reminder-location-list-management)
- [RX Reminder Exchange](#rx-reminder-exchange)
- [RT Reminder Test](#rt-reminder-test)
- [OS Other Supporting Menus ...](#os-other-supporting-menus)
- [INFO Reminder Information Only Menu ...](#info-reminder-information-only-menu)
- [DM Reminder Dialog Management ...](#dm-reminder-dialog-management)
- [CP CPRS Reminder Configuration ...](#cp-cprs-reminder-configuration)
- [RP Reminder Reports ...](#rp-reminder-reports)
- [MST Reminders MST Synchronization Management ...](#mst-reminders-mst-synchronization-management)
- [PL Reminder Patient List Menu ...](#pl-reminder-patient-list-menu)
- [PAR Reminder Parameters ...](#par-reminder-parameters)
- [ROI Reminder Orderable Item Group Menu ...](#roi-reminder-orderable-item-group-menu)
- [XM Reminder Extract Menu ...](#xm-reminder-extract-menu)
- [GEC GEC Referral Report](#gec-gec-referral-report)
- [Select Reminder Managers Menu Option: DM Reminder Dialog Management](#select-reminder-managers-menu-option-dm-reminder-dialog-management)
- [# DP Dialog Parameters ...](#dp-dialog-parameters)
- [DI Reminder Dialogs](#di-reminder-dialogs)
- [DR Dialog Reports ...](#dr-dialog-reports)
- [IA Inactive Codes Mail Message](#ia-inactive-codes-mail-message)
- [# Select Reminder Dialog Management Option: DI Reminder Dialogs](#select-reminder-dialog-management-option-di-reminder-dialogs)
- [<u>Dialog Edit List Sep 13, 2012@11:58:41 Page: 3 of 7</u>](#udialog-edit-list-sep-13-2012115841-page-3-of-7u)
- [REMINDER DIALOG NAME: VA-HOMELESSNESS SCREENING \[NATIONAL\] \LIMITED EDIT\](#reminder-dialog-name-va-homelessness-screening-national-limited-edit)
- [<u>+Item Seq. Dialog Summary</u>](#uitem-seq-dialog-summaryu)
- [5.5.5.5.5.5.7 Element: BLANK SPACE1](#5555557-element-blank-space1)
- [# 5.5.5.5.5.5.10 Group: VA-GP HOMELESS - REFER TO SOCIAL WORK](#55555510-group-va-gp-homeless-refer-to-social-work)
- [# 5.5.5.5.5.5.10.5 Element: VA-OI SOCIAL WORK REFERRAL Edit](#555555105-element-va-oi-social-work-referral-edit)
- [# 5.5.5.5.5.5.10.10 Element: VA-HF HOMELESS DECLINES REFERRAL TO SOC](#5555551010-element-va-hf-homeless-declines-referral-to-soc)
- [# 5.5.5.5.5.5.12 Element: BLANK SPACE1](#55555512-element-blank-space1)
- [# 5.5.5.5.5.5.15 Element: TXTZ VA-HOMELESSNESS BEST WAY TO REACH](#55555515-element-txtz-va-homelessness-best-way-to-reach)
- [# 5.5.5.5.5.5.20 Element: VA-TXTZ HOMELESSNESS - DONE WITH SCREEN](#55555520-element-va-txtz-homelessness-done-with-screen)
- [# 5.5.5.5.5.5.25 Element: BLANK SPACE1](#55555525-element-blank-space1)
- [ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print](#add-add-elementgroup-ds-dialog-summary-inq-inquiryprint)
- [CO Copy Dialog DO Dialog Overview QU Quit](#co-copy-dialog-do-dialog-overview-qu-quit)
- [DD Detailed Display DT Dialog Text](#dd-detailed-display-dt-dialog-text)
- [DP Progress Note Text ED Edit/Delete Dialog](#dp-progress-note-text-ed-editdelete-dialog)
- [Select Item: Next Screen//18 Enter Item \#](#select-item-next-screen18-enter-item)
- [# Current dialog element/group name: VA-OI SOCIAL WORK REFERRAL](#current-dialog-elementgroup-name-va-oi-social-work-referral)
- [Used by: VA-GP HOMELESS - REFER TO SOCIAL WORK (Dialog Group)](#used-by-va-gp-homeless-refer-to-social-work-dialog-group)
- [<u>Dialog Edit List Sep 13, 2012@12:12:30 Page: 5 of 7</u>](#udialog-edit-list-sep-13-2012121230-page-5-of-7u)
- [REMINDER DIALOG NAME: VA-HOMELESSNESS SCREENING \[NATIONAL\] \LIMITED EDIT\](#reminder-dialog-name-va-homelessness-screening-national-limited-edit-1)
- [<u>+Item Seq. Dialog Summary</u>](#uitem-seq-dialog-summaryu-1)
- [5.5.5.10.5.25 Element: HF VA-HOMELESS INSTITUTION](#55510525-element-hf-va-homeless-institution)
- [# 5.5.5.10.5.30 Element: HF VA-HOMELESS SHELTER](#55510530-element-hf-va-homeless-shelter)
- [# 5.5.5.10.5.35 Element: HF VA-HOMELESS STREET](#55510535-element-hf-va-homeless-street)
- [# 5.5.5.10.5.40 Element: HF VA-HOMELESS OTHER](#55510540-element-hf-va-homeless-other)
- [# 5.5.5.10.7 Element: BLANK SPACE1](#555107-element-blank-space1)
- [# 5.5.5.10.10 Group: VA-GP HOMELESS - REFER TO HOMELESS PROGRAM?](#5551010-group-va-gp-homeless-refer-to-homeless-program)
- [# 5.5.5.10.10.5 Element: VA-OI HOMELESS REFERRAL Now edit this](#55510105-element-va-oi-homeless-referral-now-edit-this)
- [# 5.5.5.10.10.10 Element: VA-HF HOMELESS DECLINES REFERRAL](#555101010-element-va-hf-homeless-declines-referral)
- [ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print](#add-add-elementgroup-ds-dialog-summary-inq-inquiryprint-1)
- [CO Copy Dialog DO Dialog Overview QU Quit](#co-copy-dialog-do-dialog-overview-qu-quit-1)
- [DD Detailed Display DT Dialog Text](#dd-detailed-display-dt-dialog-text-1)
- [DP Progress Note Text ED Edit/Delete Dialog](#dp-progress-note-text-ed-editdelete-dialog-1)
- [Select Item: Next Screen// 37 Select by Item \#](#select-item-next-screen-37-select-by-item)
- [Current dialog element/group name: VA-OI HOMELESS REFERRAL](#current-dialog-elementgroup-name-va-oi-homeless-referral)
- [Used by: VA-GP HOMELESS - REFER TO HOMELESS PROGRAM? (Dialog Group)](#used-by-va-gp-homeless-refer-to-homeless-program-dialog-group)
- [# FINDING ITEM: REFERRED TO HOMELESS PROGRAM// Leave this alone!](#finding-item-referred-to-homeless-program-leave-this-alone)
- [Select ADDITIONAL FINDINGS: Q.NAME OF HOMELESS SERVICES CONSULT Q.O. Enter](#select-additional-findings-qname-of-homeless-services-consult-qo-enter)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [DO NOT QUEUE THE INSTALL!!](#do-not-queue-the-install)
- [Select Installation Option: INstall Package(s)](#select-installation-option-install-packages)
- [Select INSTALL NAME:    PXRM\2.0\27    9/12/12@15:07:40](#select-install-name-pxrm2027-91212150740)
- [=\> PXRM\2.0\27  ;Created on Sep 07, 2012@11:11:52](#pxrm2027-created-on-sep-07-2012111152)
- [# This Distribution was loaded on Sep 12, 2012@15:07:40 with header of](#this-distribution-was-loaded-on-sep-12-2012150740-with-header-of)
- [PXRM\2.0\27  ;Created on Sep 07, 2012@11:11:52](#pxrm2027-created-on-sep-07-2012111152-1)
- [It consisted of the following Install(s):](#it-consisted-of-the-following-installs)
- [PXRM\2.0\27](#pxrm2027)
- [Checking Install for Package PXRM\2.0\27](#checking-install-for-package-pxrm2027)
- [# Install Questions for PXRM\2.0\27](#install-questions-for-pxrm2027)
- [# Incoming Files:](#incoming-files)
- [# # REMINDER EXCHANGE  (including data)](#reminder-exchange-including-data)
- [Note:  You already have the 'REMINDER EXCHANGE' File.](#note-you-already-have-the-reminder-exchange-file)
- [I will OVERWRITE your data with mine.](#i-will-overwrite-your-data-with-mine)
- [# # Want KIDS to INHIBIT LOGONs during the install? NO//](#want-kids-to-inhibit-logons-during-the-install-no)
- [Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//](#want-to-disable-scheduled-options-menu-options-and-protocols-no)
- [# Enter the Device you want to print the Install messages.](#enter-the-device-you-want-to-print-the-install-messages)
- [You can queue the install by enter a 'Q' at the device prompt.](#you-can-queue-the-install-by-enter-a-q-at-the-device-prompt)
- [Enter a '^' to abort the install.](#enter-a-to-abort-the-install)
- [# DEVICE: HOME//   SSH VIRTUAL TERMINAL](#device-home-ssh-virtual-terminal)
- [# # # Install Started for PXRM\2.0\27 :](#install-started-for-pxrm2027)
- [Sep 12, 2012@15:08:45](#sep-12-2012150845)
- [# Build Distribution Date: Sep 07, 2012](#build-distribution-date-sep-07-2012)
- [# Installing Routines:](#installing-routines)
- [Sep 12, 2012@15:08:45](#sep-12-2012150845-1)
- [# Running Pre-Install Routine: PRE^PXRMP27I](#running-pre-install-routine-prepxrmp27i)
- [# DISABLE options.](#disable-options)
- [# DISABLE protocols.](#disable-protocols)
- [# Installing Data Dictionaries:](#installing-data-dictionaries)
- [Sep 12, 2012@15:08:45](#sep-12-2012150845-2)
- [# Installing Data:](#installing-data)
- [Sep 12, 2012@15:08:47](#sep-12-2012150847)
- [# Running Post-Install Routine: POST^PXRMP27I](#running-post-install-routine-postpxrmp27i)
- [# ENABLE options.](#enable-options)
- [# ENABLE protocols.](#enable-protocols)
- [# There are 3 Reminder Exchange entries to be installed.](#there-are-3-reminder-exchange-entries-to-be-installed)
- [Installing Reminder Exchange entry VA-HOMELESSNESS SCREENING](#installing-reminder-exchange-entry-va-homelessness-screening)
- [Installing Reminder Exchange entry VA-LIPID STATIN RX CVD/DM (VER1.0)](#installing-reminder-exchange-entry-va-lipid-statin-rx-cvddm-ver10)
- [Installing Reminder Exchange entry VA-LIPID STATIN RX CVD/DM DIALOG](#installing-reminder-exchange-entry-va-lipid-statin-rx-cvddm-dialog)
- [Finding LT.LDL CHOLESTEROL does not exist, what do you want to do?](#finding-ltldl-cholesterol-does-not-exist-what-do-you-want-to-do)
- [# Select one of the following:](#select-one-of-the-following)
- [# # D         Delete](#d-delete)
- [P         Replace with an existing entry](#p-replace-with-an-existing-entry)
- [Q         Quit the install](#q-quit-the-install)
- [# Enter response: P  Replace with an existing entry](#enter-response-p-replace-with-an-existing-entry)
- [Select LABORATORY TEST NAME: LDL](#select-laboratory-test-name-ldl)
- [LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!](#lipid-profile-is-a-lab-panel-it-cannot-be-used-as-a-reminder-finding)
- [Contact your Lab ADPAC for help](#contact-your-lab-adpac-for-help)
- [LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!](#lipid-profile-is-a-lab-panel-it-cannot-be-used-as-a-reminder-finding-1)
- [Contact your Lab ADPAC for help](#contact-your-lab-adpac-for-help-1)
- [LDL (CALC.)](#ldl-calc)
- [LDL DIRECT](#ldl-direct)
- [CHOOSE 1-2: 1  LDL (CALC.)](#choose-1-2-1-ldl-calc)
- [Selection item L.CHOLESTEROL HDL does not exist, what do you want to do?](#selection-item-lcholesterol-hdl-does-not-exist-what-do-you-want-to-do)
- [# Select one of the following:](#select-one-of-the-following-1)
- [# # D         Delete](#d-delete-1)
- [P         Replace with an existing entry](#p-replace-with-an-existing-entry-1)
- [Q         Quit the install](#q-quit-the-install-1)
- [# Enter response: P  Replace with an existing entry](#enter-response-p-replace-with-an-existing-entry-1)
- [Select LABORATORY TEST NAME: HDL](#select-laboratory-test-name-hdl)
- [HDL CHOLESTEROL](#hdl-cholesterol)
- [HDL-REF..](#hdl-ref)
- [CHOOSE 1-2: 1  HDL CHOLESTEROL](#choose-1-2-1-hdl-cholesterol)
- [Selection item L.LDL CHOLESTEROL does not exist, what do you want to do?](#selection-item-lldl-cholesterol-does-not-exist-what-do-you-want-to-do)
- [# Select one of the following:](#select-one-of-the-following-2)
- [# # D         Delete](#d-delete-2)
- [P         Replace with an existing entry](#p-replace-with-an-existing-entry-2)
- [Q         Quit the install](#q-quit-the-install-2)
- [# Enter response: P  Replace with an existing entry](#enter-response-p-replace-with-an-existing-entry-2)
- [Select LABORATORY TEST NAME: LDL](#select-laboratory-test-name-ldl-1)
- [LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!](#lipid-profile-is-a-lab-panel-it-cannot-be-used-as-a-reminder-finding-2)
- [Contact your Lab ADPAC for help](#contact-your-lab-adpac-for-help-2)
- [LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!](#lipid-profile-is-a-lab-panel-it-cannot-be-used-as-a-reminder-finding-3)
- [Contact your Lab ADPAC for help](#contact-your-lab-adpac-for-help-3)
- [LDL (CALC.)](#ldl-calc-1)
- [LDL DIRECT](#ldl-direct-1)
- [CHOOSE 1-2: 1  LDL (CALC.)](#choose-1-2-1-ldl-calc-1)
- [Selection item L.LDL CHOLESTEROL does not exist, what do you want to do?](#selection-item-lldl-cholesterol-does-not-exist-what-do-you-want-to-do-1)
- [# Select one of the following:](#select-one-of-the-following-3)
- [# # D         Delete](#d-delete-3)
- [P         Replace with an existing entry](#p-replace-with-an-existing-entry-3)
- [Q         Quit the install](#q-quit-the-install-3)
- [# PXRM\2.0\27](#pxrm2027-1)
- [Enter response: P  Replace with an existing entry](#enter-response-p-replace-with-an-existing-entry-3)
- [Select LABORATORY TEST NAME: LDL](#select-laboratory-test-name-ldl-2)
- [LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!](#lipid-profile-is-a-lab-panel-it-cannot-be-used-as-a-reminder-finding-4)
- [Contact your Lab ADPAC for help](#contact-your-lab-adpac-for-help-4)
- [LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!](#lipid-profile-is-a-lab-panel-it-cannot-be-used-as-a-reminder-finding-5)
- [Contact your Lab ADPAC for help](#contact-your-lab-adpac-for-help-5)
- [LDL (CALC.)](#ldl-calc-2)
- [LDL DIRECT](#ldl-direct-2)
- [CHOOSE 1-2: 1  LDL (CALC.)](#choose-1-2-1-ldl-calc-2)
- [# Updating Routine file...](#updating-routine-file)
- [# Updating KIDS files...](#updating-kids-files)
- [# PXRM\2.0\27 Installed.](#pxrm2027-installed)
- [Sep 12, 2012@15:10:51](#sep-12-2012151051)
- [# Install Message sent \#53288961](#install-message-sent-53288961)
- [100%                 25             50             75               ](#100-25-50-75)
- [Complete  ](#complete)
- [# # Install Completed](#install-completed)
- [Acronyms](#acronyms)
Patch PXRM\*2.0\*27 is the first patch to the Clinical Reminder package that uses the recently-approved expedited patch process. The patch releases two (2) new National VHA reminders to the field, without any changes to routines, data dictionaries, or other package functions – “content” only. The two (2) reminders are the VA-HOMELESSNESS SCREENING and VA-LIPID STATIN RX CVD/DM reminders.
VA- HOMELESSNESS SCREENING reminder:
The President of The United States and The Secretary of the Department of Veterans Affairs have made it a priority (T-21 initiative) to eliminate homelessness in our Veteran population. Ideally, none of our nation’s heroes would be homeless or at risk of becoming homeless, but sadly, studies show that more than 6% of our Veterans and/or families of Veterans, nationwide, are in this situation.
The objectives of the VA-Homelessness Screening clinical reminder are to: (a) identify Veterans and their families who are at imminent risk of homelessness or who have very recently become homeless; (b) ensure that those who are at-risk or who are currently homeless are referred for appropriate assistance; and (c) update documentation in the medical record regarding the current living situation for these at-risk Veterans. It is anticipated that this new screening reminder will help to identify Veterans who might not otherwise seek assistance or who may not be aware of homeless programs offered by VHA.
The Homelessness Screening reminder consists of two questions:
1.  For the past 60 days have you been living in stable housing that you own, rent or stay in as part of a household?
2.  Are you worried or concerned that in the next 60 days you may NOT have stable housing that you own, rent or stay in as part of a household?            
The second question only displays if the Veteran indicates that his/her current living situation is stable. If the answer to the first question is “no,” the Veteran is then asked about his/her current living arrangement and asked about referral for homeless services.
If the answer to the second question is “yes,” indicating at-risk for homelessness, the Veteran is again asked about the current living situation and about a referral to homeless services. Efforts should be made to ensure that Veterans who screen positive are not just *offered* assistance, but are *referred* to local homelessness programs for assistance with their living situation. The VA-HOMELESSNESS SCREENING reminder is a NATIONALLY-MANDATED reminder – similar to the VA-TBI and VA-IRAQ&AFGHAN POST DEPLOYMENT screening reminders. It *MUST* be placed on the Cover Sheet at all facilities and is intended to be completed by any staff person. Sites can choose to display this reminder for all staff or for select staff. However, any staff person who performs the screen must have a mechanism for referring the Veteran for further services if warranted. Medical centers may need to create policies or standard operating procedures that allow administrative and/or non-licensed clinical support staff to place to a CPRS consult if electronic consults are required.
All Veterans are eligible for screening, although the reminder will not trigger if a Veteran has had a visit *in the last 6 months* to a clinic associated with any of the stop codes indicative of homelessness services - 504, 507, 508, 511, 522, 528, 529, 530, 590, 591, or 592. Otherwise, the reminder is due annually. If a Veteran screens positive (currently homeless or in imminent danger of homelessness), the reminder will be due every six months until the Veteran is seen in a clinic associated with one of the stop codes listed above, or subsequently screens negative. Once a Veteran has screened negative for homelessness three (3) consecutive times, the frequency changes to every two years.
Veterans answering that they currently reside in Long Term Care facilities need only be screened every two years. If the Veteran indicates that he is already receiving homeless services or is unable to answer the screening questions, the reminder is resolved for 6 months. If the Veteran declines to answer the screening questions, the reminder is resolved for one year.
If specific note titles are utilized to document homelessness services at a given VA facility outside of a clinic associated with the stop codes listed above, there is an option built into the reminder to allow resolution of the reminder on this basis. In order to take advantage of this option, the local CAC or CR Manager will need to *map NEW TIU Document Titles* created for this purpose (homelessness services) to the Reminder Term, “VA-HOMELESSNESS - ALREADY RECEIVING SERVICES.” That is done by editing one of the computed findings, “VA-PROGRESS NOTE,” and entering the title *exclusively* used for homelessness services, into the “COMPUTED FINDING PARAMETER” field for one of those findings. Three (3) of the VA-Progress Note computed findings (blank – no title) have been entered into the Reminder Term for this purpose. See post-install instructions for specific details.
The reminder dialog contains a link to the VA National Homelessness Program Office website that contains educational and other materials related to VHA homelessness programs. Sites may wish to provide a local or VISN link to specific patient hand-outs relating to local or VISN homeless programs.
VA-LIPID STATIN RX CVD/DM (VER1.0) reminder (Print name: Assess Statin Use - Lipids (CVD/DM))
Recent analyses of cardiovascular prevention studies, as well as the growing appreciation of the downsides of aggressive lipid treatment with high dose statins or non-statin cholesterol-lowering medications, have raised concerns about performance measures for lipid management based solely on achieving a target value of Low Density Lipoprotein Cholesterol (LDL-C) (Hayward and Krumholz, 2012).   
The use of statin drugs can provide significant patient benefit even if LDL-C values remain above 100.  Professional societies now recommend that the adequacy of lipid management be judged by the appropriateness of the therapy and not solely by LDL value (ACCF/AHA/AMA-PCPI, 2011).  Performance measures that recognize appropriate clinical prescribing provide a better balance of patient benefit and risk and may reduce complications of overzealous drug therapy (e.g., muscle breakdown).
This national clinical reminder has been created to address the concerns outlined above and to support updated VHA Performance Measures for FY 12 and FY 13 (ihd18hns and dmg25hs) that assess LDL-C values in patients with cardiovascular disease or with diabetes mellitus or whether the patient is on at least a moderate dose of a statin medication. The reminder replaces previous national lipid reminders that were based on threshold LDL-C values. It was created by the VHA National Clinical Reminders Committee with input from multiple national VA experts on lipid management, diabetes mellitus, ischemic heart disease, and quality measurement. The reminder is intended to be used by providers with prescribing privileges.
The eligible cohort for the reminder includes patients ages 18-75 with ICD-9 codes indicating any type of cardiovascular disease or diabetes (based on EPRP diagnostic criteria), as well as patients on specific medications utilized in the management of diabetes. More specifically, the reminder includes patients who meet the following criteria:
1.  CVD: any diagnosis of CVD in the past 2 years that is more recent than any entry of incorrect diagnosis of CVD and age 18-75.
2.  Diabetes: 2 diagnoses in the past 2 years, or a problem list entry, or a prescription of medication for diabetes that was active in the previous 9 months and the diagnosis or prescription is more recent than any entry of an incorrect diagnosis and age 18-75.
At this time, the reminder triggers for patients ages 18-75 based on current EPRP criteria. However, it is anticipated that these age ranges may be modified in the future, particularly for patients with diabetes mellitus.
The reminder evaluates whether there is an LDL-C value in the past two years and whether that value is below 100. If not, the reminder evaluates whether the patient has an active prescription for at least a moderate dose statin as defined below:
- atorvastatin  10 mg/day or higher
- fluvastatin 80 mg/day or higher
- lovastatin 40 mg/day or higher
- pravastatin 40 mg/day or higher
- rosuvastatin 5 mg/day or higher
- simvastatin 20 mg/day or higher  
Patients are excluded from the reminder cohort if they have documentation of limited life expectancy or of specific types of terminal cancers.
The reminder can also be resolved for varying times if any of the following are documented:
1.  Contraindication to statin use (either temporary – off for one year; or permanent – resolves permanently)
2.  Documentation of moderate dose statin use (e.g. non-VA medication) – resolves for one year
3.  Documentation that the patient is on the highest tolerated dose of a statin – resolves for one year
4.  Documentation that the patient has had an adverse drug reaction to all available statins – resolves for one year)
5.  Documentation that the patient has had an adverse drug reaction to all available statins and there is an allergy/ADR documented in the allergy package of CPRS – resolves permanently
6.  Non-adherence to statin therapy – resolves for 2 months
7.  Outside LDL-C value \< 100 – resolves for one year from date of LDL-C
8.  Dosage adjustment – resolves for 2 months
9.  Patient declination – resolves for 2 months
10. Order for LDL-C – resolves if order date is within the past 14 days or the next two months and is reactivated two months after lab start date
11. Incorrect diagnosis of CVD or DM – resolves until a new code is entered
Sites that have created risk calculators for CVD may choose to include patients with a CHD 10-year risk \>20% in the eligible cohort by mapping their local health factors to the CHD RISK\>20% reminder term.
The reminder provides a list of moderate dose statins for provider reference, allows the provider to view the most recent lipid panel results, and includes information regarding current guidance on lipid management. It is recommended that sites continue to utilize local or national reminders for annual LDL-C assessment as long as this continues to be a performance measure. This reminder will not trigger if there is no LDL-C value documented in the past two years, even if a patient meets disease criteria and is not on a moderate dose statin. The reminder evaluates for an LDL-C within the last two years (as opposed to the past year) in order to focus attention on statin therapy, since this is the most important intervention, and treating to goal is now felt to be less critical.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Software for PXRM\*2\*27

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
| Installation and Setup Guide | PXRM_2_0_27_IG.PDF          |
| Release Notes                | PXRM_2_0_27_RN.PDF          |

### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                       |                                                           |                                                                                            |
|---------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Site                              | URL                                                   | Description                                                                            |
| National Clinical Reminders site      | <http://vista.med.va.gov/reminders>                       | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | <http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx> | This committee directs the development of new and revised national reminders               |
| VistA Document Library                | <http://www.va.gov/vdl/>                                  | Contains manuals for Clinical Reminders and                                                |

## # Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*The installation needs to be done by a person with DUZ(0) set to "@."*NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.

## Retrieve the host file from one of the following locations (with the ASCII file type): 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Albany <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Salt Lake City <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

1.  This installation will prompt the installer for a few replacement lab tests. We experienced a problem with an install into a test account where the account had a lab panel named LDL CHOLESTEROL. Although most sites will not have this issue, it is important that you check your LABORATORY TEST file (file 60) to ensure that you DO NOT have a lab panel test named “LDL CHOLESTEROL.” If you do have a lab panel test named “LDL CHOLESTEROL,” do not install the patch and enter a national remedy ticket. Product support staff will help you get the patch installed.

## Install the patch first in a training or test account. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name.KID at the Host File prompt.

Example

> Select Installation Option: LOAD a Distribution

> Enter a Host File: PXRM_2_0_27.KID

> KIDS Distribution saved on

From the Installation menu, you may elect to use the following options:

## ## Backup a Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

## Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

## Verify Checksums in Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (<span class="mark">REDACTED</span>) to report the problem.

> Select INSTALL NAME: PXRM\*2.0\*27

> Want each Routine Listed with Checksums: Yes// YES

> DEVICE: HOME// VIRTUAL TELNET

## ## Install the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*27 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: PXRM\*2.0\*27

Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE:DO NOT QUEUE THE INSTALLATION, because this installation asks questions requiring responses and queuing will stop the installation. A Reminders Manager or CAC should be present to respond to these.

> Installation Example

> See [Appendix A](\l).

## ## Install File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

> Select Utilities Option: Install File Print

> Select INSTALL NAME: PXRM\*2.0\*27

## ## Build File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print

> Select BUILD NAME: PXRM\*2.0\*27

> DEVICE: HOME//

## Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After successful installation, the following init routines may be deleted:

> PXRMP27E

> PXRMP27I

# Post-Install Set-up Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post-install setup will only take a few minutes, but getting together with your local Homelessness Staff may take a while. Do NOT DELAY – talk to them immediately.

Be sure to speak with the Homelessness Program staff locally, to determine:

- *WhatConsult Service* they wish to use locally for Homelessness referrals – it is a mandate that a consult is used
- *What URL address* will be used locally for hand-outs to homeless Veterans
- If the Homelessness Program locally uses a clinic with any of the following Stop codes: *504, 507, 508, 511, 522, 528, 529, 530, 590, 591, or 592.*

> If they use clinics with stop codes <u>OTHER than those listed</u>, you will need to set up Progress Note Titles for them to use, or determine those used currently EXCLUSIVELY for documenting Homelessness Services. These stop codes must be entered in the Resolution Logic, by following the instructions below in [step 3](#step3).VA-HOMELESSNESS SCREENING Reminder:

# After the installation of patch PXRM\*2.0\*27, do the following steps to set up the VA-Homelessness Screening reminder 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See details under each section below this list:

1.  Edit the Dialog and add separate quick orders for Social Work Consult and Homelessness Consult as Additional Finding Items in two different dialog elements.
2.  Edit the url in the Template Field, “*HOMELESSNESS EDUCATIONAL MATERIALS.”*
3.  Determine if Progress Note Titles will be used to resolve the reminder and if so, enter NEW TIU title into Reminder Term that will be used *exclusively* for this purpose.
4.  Place the reminder on the Cover Sheet in CPRS for all users in MH and Primary Care (“SYSTEM”).

Detailed steps:

1.  Edit the two (2) Dialog Elements for REFERRALS to Homelessness and Social Work Services, and add appropriate Consult Q.O. as Additional Finding Item to each:

> Edit the dialog and edit the elements:

> (Responses to Prompts are *BOLD* and in *ITALICS*)

# CF Reminder Computed Finding Management ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# RM Reminder Definition Management ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# SM Reminder Sponsor Management ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# TXM Reminder Taxonomy Management ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# TRM Reminder Term Management ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LM Reminder Location List Management ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# RX Reminder Exchange

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# RT Reminder Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# OS Other Supporting Menus ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# INFO Reminder Information Only Menu ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DM Reminder Dialog Management ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# CP CPRS Reminder Configuration ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# RP Reminder Reports ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# MST Reminders MST Synchronization Management ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# PL Reminder Patient List Menu ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# PAR Reminder Parameters ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ROI Reminder Orderable Item Group Menu ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# XM Reminder Extract Menu ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# GEC GEC Referral Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select Reminder Managers Menu Option: *DM* Reminder Dialog Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # DP Dialog Parameters ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DI Reminder Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DR Dialog Reports ...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# IA Inactive Codes Mail Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Select Reminder Dialog Management Option: *DI* Reminder Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Dialog List Jul 23, 2012@13:13:40 Page: 1 of 9</u>

> REMINDER VIEW (ALL REMINDERS BY NAME) Must Change View

> <u>Item Reminder Name Linked Dialog Name & Dialog Status</u>

> 1 ACUTE MYOCARDIAL INFARCTION

> 2 AGP TEST AGP TEST ALL DIALOG

> 3 CHEST XRAY

> 4 CHOLESTEROL SCREEN (M)

> 5 CRITICAL DRUG

> 6 DEPRESSION SCREEN

> 7 MAMMOGRAM

> 8 MAMMOGRAMS

> 9 MAMMOGRAPHY

> 10 OEF/OIF COHORT

> 11 PAP SMEAR

> 12 PATCH 11 LOCATION LIST

> 13 PPD

> + Enter ?? for more actions \>\>\>

> AR All reminders LR Linked Reminders QU Quit

> *CV Change View* RN Name/Print Name

> Select Item: Next Screen// *CV* Change View

> Select one of the following:

> D Reminder Dialogs Select “D”

> E Dialog Elements

> F Forced Values

> G Dialog Groups

> P Additional Prompts

> R Reminders

> RG Result Group (Mental Health)

> RE Result Element (Mental Health)

> TYPE OF VIEW: R// *D* Reminder Dialogs

> *This is an Example – your list will be different!*

> <u>Dialog List Jul 23, 2012@13:13:41 Page: 1 of 5</u>

> DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)

> <u>Item Reminder Dialog Name Source Reminder Status</u>

> 1 AGP TEST ALL DIALOG \*NONE\* Linked

> 2 AWAT PACK TEST \*NONE\*

> 3 CCHT (2 DATA OBJECTS ONLY) \*NONE\* Disabled

> 4 DALFAMPRIDINE INITIATION-EFFICACY EVAL \*NONE\*

> 5 NCEHC LIFE SUSTAINING TREATMENT PLAN \*NONE\*

> 6 PVC TEST \*NONE\*

> 7 VA-AAA SCREENING \*NONE\* Linked

> 8 VA-AIMS VA-ANTIPSYCHOTIC MED SIDE Linked

> 9 VA-ALCOHOL F/U POS AUDIT-C \*NONE\* Linked

> 10 VA-ALCOHOL USE SCREENING (AUDIT-C) \*NONE\* Linked

> 11 VA-DEPRESSION ASSESSMENT VA-POS DEPRESSION SCREEN Disabled

> 12 VA-DEPRESSION SCREEN VA-DEPRESSION SCREENING Linked

> 13 VA-DIAB RETINOPATHY SURVEILLANCE NOTE \*NONE\*

> 14 VA-DIAB TELERETINAL IMAGING READER CONS \*NONE\* Linked

> 15 VA-ECOE EDUCATION TPL \*NONE\*

> 16 VA-ECOE FOLLOW-UP NOTE \*NONE\*

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

> AD Add Reminder Dialog PT List/Print All QU Quit

> CV Change View RN Name/Print Name

> Select Item: Next Screen// *Hit Return (enter) several times until found on your screen.*

> <u>Dialog List Jul 23, 2012@13:21:44 Page: 2 of 5</u>

> <u>DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)</u>

> <u>+Item Reminder Dialog Name Source Reminder Status</u>

> 17 VA-ECOE INITIAL NOTE \*NONE\*

> 18 VA-ECOE QUALITY OF LIFE TPL \*NONE\*

> 19 VA-EMBEDDED FRAGMENTS RISK EVALUATION \*NONE\* Linked

> 20 VA-EMBEDDED FRAGMENTS SCREENING \*NONE\* Linked

> 21 VA-GEC REFERRAL CARE COORDINATION VA-GEC REFERRAL CARE COOR Linked

> 22 VA-GEC REFERRAL CARE RECOMMENDATION VA-GEC REFERRAL CARE RECO Linked

> 23 VA-GEC REFERRAL NURSING ASSESSMENT VA-GEC REFERRAL NURSING A Linked

> 24 VA-GEC REFERRAL SOCIAL SERVICES VA-GEC REFERRAL SOCIAL SE Linked

> 25 VA-HOMELESSNESS SCREENING VA-HOMELESSNESS SCREENING Linked

> 26 VA-HT ASSESSMENT TREATMENT PLAN TEMPLAT \*NONE\*

> 27 VA-HT CAREGIVER ASSESSMENT TEMPLATE \*NONE\*

> 28 VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER RISK ASSE Linked

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

> ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print

> CO Copy Dialog DO Dialog Overview QU Quit

> DD Detailed Display DT Dialog Text

> DP Progress Note Text ED Edit/Delete Dialog

> Select Item: Next Screen// 25Select the dialog by Item \#. Mine is 25. Yours will be a different \# - depending on how many you have on your system

> <u>Dialog Edit List Jul 23, 2012@13:31:48 Page: 1 of 7</u>

> REMINDER DIALOG NAME: VA-HOMELESSNESS SCREENING \[NATIONAL\] \*LIMITED EDIT\*

> <u>Item Seq. Dialog Summary</u>

> 1 5 Group: VA-GP HOMELESSNESS REMINDER

> 2 5.5 Group: VA-GP HOMELESSNESS SCREEN

> 3 5.5.5 Group: VA-GP HOMELESS LAST 60 DAYS - STABLE HOUSING?

> 4 5.5.5.5 Group: VA-GP HOMELESS - STABLE HOUSING

> 5 5.5.5.5.5 Group: VA-GP HOMELESS WORRIED NEXT 60 DAYS

> 6 5.5.5.5.5.5 Group: VA-GP HOMELESS - AT RISK NEAR FUTURE - RECENT H

> 7 5.5.5.5.5.5.5 Group: VA-GP HOMELESS - AT RISK - WHERE HAVE YOU LI

> 8 5.5.5.5.5.5.5.5 Element: HF VA-HOMELESS HOUSE NO SUBSIDY

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

> ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print

> CO Copy Dialog DO Dialog Overview QU Quit

> DD Detailed Display DT Dialog Text

> DP Progress Note Text ED Edit/Delete Dialog

> Select Item: Next Screen// *Now hit Return (Enter) twice (X2) to see the first OI Element where you will enter an Additional Finding Item*

# <u>Dialog Edit List Sep 13, 2012@11:58:41 Page: 3 of 7</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# REMINDER DIALOG NAME: VA-HOMELESSNESS SCREENING \[NATIONAL\] \*LIMITED EDIT\*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>+Item Seq. Dialog Summary</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# 5.5.5.5.5.5.7 Element: BLANK SPACE1 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.5.5.5.10 Group: VA-GP HOMELESS - REFER TO SOCIAL WORK 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.5.5.5.10.5 Element: VA-OI SOCIAL WORK REFERRAL Edit 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.5.5.5.10.10 Element: VA-HF HOMELESS DECLINES REFERRAL TO SOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.5.5.5.12 Element: BLANK SPACE1 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.5.5.5.15 Element: TXTZ VA-HOMELESSNESS BEST WAY TO REACH 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.5.5.5.20 Element: VA-TXTZ HOMELESSNESS - DONE WITH SCREEN 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.5.5.5.25 Element: BLANK SPACE1 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

# ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# CO Copy Dialog DO Dialog Overview QU Quit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DD Detailed Display DT Dialog Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DP Progress Note Text ED Edit/Delete Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select Item: Next Screen//18 Enter Item \# 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Current dialog element/group name: VA-OI SOCIAL WORK REFERRAL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Used by: VA-GP HOMELESS - REFER TO SOCIAL WORK (Dialog Group)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> FINDING ITEM: REFERRED TO SOCIAL WORK// *Leave that alone!*

> Additional findings: none

> Select ADDITIONAL FINDING: *Here, type, “Q.name of your Quick Order” for Social Work Referral Consult*

> When you enter that QO, and hit enter, you’ll be brought back to the list of Items in the dialog.

> <u>Dialog Edit List Jul 23, 2012@13:36:49 Page: 3 of 7</u>

> REMINDER DIALOG NAME: VA-HOMELESSNESS SCREENING \[NATIONAL\] \*LIMITED EDIT\*

> <u>+Item Seq. Dialog Summary</u>

> 16 5.5.5.5.5.5.7 Element: BLANK SPACE1

> 17 5.5.5.5.5.5.10 Group: VA-GP HOMELESS - REFER TO HOMELESS PROGRAM?

> 18 5.5.5.5.5.5.10.5 Element: VA-OI HOMELESS REFERRAL

> 19 5.5.5.5.5.5.10.10 Element: VA-HF HOMELESS DECLINES REFERRAL

> 20 5.5.5.5.5.5.12 Element: BLANK SPACE1

> 21 5.5.5.5.5.5.15 Element: TXTZ VA-HOMELESSNESS BEST WAY TO REACH

> 22 5.5.5.5.5.5.20 Element: VA-TXTZ HOMELESSNESS - DONE WITH SCREEN

> 23 5.5.5.5.5.5.25 Element: BLANK SPACE1

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

> ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print

> CO Copy Dialog DO Dialog Overview QU Quit

> DD Detailed Display DT Dialog Text

> DP Progress Note Text ED Edit/Delete Dialog

> Select Item: Next Screen// Hit enter twice (X2)

# <u>Dialog Edit List Sep 13, 2012@12:12:30 Page: 5 of 7</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# REMINDER DIALOG NAME: VA-HOMELESSNESS SCREENING \[NATIONAL\] \*LIMITED EDIT\*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>+Item Seq. Dialog Summary</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# 5.5.5.10.5.25 Element: HF VA-HOMELESS INSTITUTION 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.10.5.30 Element: HF VA-HOMELESS SHELTER 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.10.5.35 Element: HF VA-HOMELESS STREET 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.10.5.40 Element: HF VA-HOMELESS OTHER 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.10.7 Element: BLANK SPACE1 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.10.10 Group: VA-GP HOMELESS - REFER TO HOMELESS PROGRAM? 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.10.10.5 Element: VA-OI HOMELESS REFERRAL Now edit this 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 5.5.5.10.10.10 Element: VA-HF HOMELESS DECLINES REFERRAL 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

# ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# CO Copy Dialog DO Dialog Overview QU Quit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DD Detailed Display DT Dialog Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DP Progress Note Text ED Edit/Delete Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select Item: Next Screen// 37 Select by Item \# 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Current dialog element/group name: VA-OI HOMELESS REFERRAL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Used by: VA-GP HOMELESS - REFER TO HOMELESS PROGRAM? (Dialog Group)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # FINDING ITEM: REFERRED TO HOMELESS PROGRAM// Leave this alone!

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select ADDITIONAL FINDINGS: Q.NAME OF HOMELESS SERVICES CONSULT Q.O. Enter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2.  Edit the Template Field for the url to Homelessness Assistance information:*If your site wants to change that url from the VA National Homelessness Web Site, to a local or VISN site, you’ll need to do this. If no local or VISN site is to be used, skip this step.*
- *Sign into CPRS GUI*,
- *Select any patie*nt,
- *Select the NOTES tab*
- *Click on Options (top of screen)*
- *Select “Edit Template Fields”, from drop down list*
- *In the window that APPEARS, type, “HOMELESSNESS* and edit the Template Field, named, “*HOMELESSNESS EDUCATIONAL MATERIALS*”, and *change the address* to a local Educational Materials url address. *Apply* & *Ok*.

> ![](pxrm-2-27-homelessness-screening-lipid-statin-rx-cvd-dm-reminders-installation-g/002.png)

Your site may opt to change the url to point to a local or VISN site with Education Materials/List of services, or to leave as is – pointing to the National Homelessness site.

3.  <span id="step3" class="anchor"></span>Determine if Progress Note Titles will be used to resolve the reminder

> \*\*\*Homelessness clinic staff may not be aware of what stop code is associated with their clinic. Check with DSS staff as to what stop code is used for that clinic\*\*\*

> (Important for Clinics that do NOT use any of the following Stop codes: *504, 507, 508, 511, 522, 528, 529, 530, 590, 591, or 592*).

> If clinics with other stop codes are used for homelessness services, you *<u>MUST</u>* determine the Note Titles they are currently using or will use (*<u>EXCLUSIVELY for Homelessness Services</u>*) – *do NOT use titles used for anything other than Homelessness Services*, and enter the title(s) into the resolution logic of the reminder – all setup to do so – just edit current Reminder Term Findings as shown below:

CF Reminder Computed Finding Management ...

*RM Reminder Definition Management ...*

SM Reminder Sponsor Management ...

TXM Reminder Taxonomy Management ...

TRM Reminder Term Management ...

LM Reminder Location List Management ...

RX Reminder Exchange

RT Reminder Test

OS Other Supporting Menus ...

INFO Reminder Information Only Menu ...

DM Reminder Dialog Management ...

CP CPRS Reminder Configuration ...

RP Reminder Reports ...

MST Reminders MST Synchronization Management ...

PL Reminder Patient List Menu ...

PAR Reminder Parameters ...

ROI Reminder Orderable Item Group Menu ...

XM Reminder Extract Menu ...

GEC GEC Referral Report

Select Reminder Managers Menu Option: *RM Reminder Definition Management*

RL List Reminder Definitions

RI Inquire about Reminder Definition

*RE Add/Edit Reminder Definition*

RC Copy Reminder Definition

RA Activate/Inactivate Reminders

RH Reminder Edit History

ICS Integrity Check Selected

ICA Integrity Check All

Select Reminder Definition Management Option: *RE Add/Edit ReminderDefinition*

Select Reminder Definition: VA-HOMELESS

1 VA-HOMELESSNESS FREQUENCY 2Y NATIONAL

*2 VA-HOMELESSNESS SCREENING NATIONAL*

CHOOSE 1-2: *2 VA-HOMELESSNESS SCREENING NATIONAL*

You will see a list of the Reminder Terms – there is only 1! Select it, and edit as shown below:

*RT VA-HOMLESSNESS - ALREADY RECEIVING SERVICES Finding \# 1*

Select FINDING: *\`1 VA-HOMLESSNESS - ALREADY RECEIVING SERVICES*

You will be asked,

“Do you want to edit mapped findings for VA-HOMLESSNESS - ALREADY RECEIVING SERVICES : N// Y YES Say YES!

To enter titles to exclude the Veteran from screening, simply edit one of the CF VA-PROGRESS NOTE Findings, and enter the EXACT Title in the "COMPUTED FINDING PARAMETER" field. If in the unlikely event that more than three (3) PN titles are in use locally for this purpose, enter that CF again as another finding, by typing "CF.VA-PROGRESS NOTE" (IN QUOTES), at the Finding: prompt.

Reminder Term Findings:

CF VA-PROGRESS NOTE

HF ALREADY RECEIVING ASSIST WITH HOUSING

RL VA-HOMELESSNESS STOP CODES

Choose from:

CF VA-PROGRESS NOTE Finding \# 3

CF VA-PROGRESS NOTE Finding \# 4

CF VA-PROGRESS NOTE Finding \# 5

HF ALREADY RECEIVING ASSIST WITH HOUSING Finding \# 2

RL VA-HOMELESSNESS STOP CODES Finding \# 1

Select Finding: *\`3 VA-PROGRESS NOTE Enter \`# of first CF*

Select FINDING: CF.VA

Searching for a REMINDER COMPUTED FINDING, (pointed-to by FINDING ITEM)

VA-PROGRESS NOTE NATIONAL

...OK? Yes// (Yes)

1 VA-PROGRESS NOTE

2 VA-PROGRESS NOTE

3 VA-PROGRESS NOTE

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 VA-PROGRESS NOTE

Computed Finding Description:

This computed finding will return multiple instances of a progress

note based on the exact title of the TIU DOCUMENT DEFINTION or the

internal entry number (IEN) of the TIU DOCUMENT DEFINTION. If the

IEN is used, it should be preceded by the "\`" character. The note

title or IEN is specified in the COMPUTED FINDING PARAMETER field.

If you want to search for notes with a certain status, then append

"^status" to the title. Status can be any of the following:

1 = UNDICTATED

2 = UNTRANSCRIBED

3 = UNRELEASED

4 = UNVERIFIED

5 = UNSIGNED

6 = UNCOSIGNED

7 = COMPLETED

8 = AMENDED

9 = PURGED

10 = TEST

11 = ACTIVE

13 = INACTIVE

14 = DELETED

15 = RETRACTED

If status is not specified, then the default is to search for notes with a status of COMPLETED.

For example, if the COMPUTED FINDING PARAMETER field contains: ADMITTING HISTORY & PHYSICAL^5, the search would be for notes with the exact title of "ADMITTING HISTORY & PHYSICAL" and a status of "UNSIGNED."

If the IEN were used, then the COMPUTED FINDING PARAMETER filed would be: \`1091^5

> **NOTE:** The specified TIU DOCUMENT DEFINITION must have a TYPE of "DOC"; if it doesn’t, the computed finding will always be false.

The values returned by this computed finding that can be used in the Condition are V=note title, V("TITLE")=note title and V("AUTH")=author of note.

Additional data for use in the Condition can be obtained by appending "^1" after the status; for example:

ADMITTING HISTORY & PHYSICAL^5^1

ADMITTING HISTORY & PHYSICAL^^1

(In the second example, since the status is blank, it would default to notes with a status of COMPLETED.)

The additional data are:

V("DISPLAY NAME")=Display name of TIU title.

V("EPISODE BEGIN DATE/TIME")=String\_":"\_EPISODE BEGIN DATE/TIME, where String is "Adm" for ward locations and "Visit" for all other location types. Date/time is in MM/DD/YY format.

V("EPISODE END DATE/TIME")=String\_" "\_EPISODE END DATE/TIME, where string is null if no date/time or "Dis: " if date/time exists. Date/time is in MM/DD/YY format

V("HOSPITAL LOCATION")=External format of HOSPITAL LOCATION from TIU

DOCUMENT file

V("NUMBER OF IMAGES")=Number of images associated with TIU DOCUMENT

entry

V("REQUESTING PACKAGE")=REQUESTING PACKAGE REFERENCE field from TIU

DOCUMENT file (internal format)

V("SUBJECT")=SUBJECT (OPTIONAL description) field from TIU DOCUMENT file (note that characters are limited to ensure returned string is not longer than 255 characters).

Editing Finding Number: 3

FINDING ITEM: VA-PROGRESS NOTE//

BEGINNING DATE/TIME:

ENDING DATE/TIME:

OCCURRENCE COUNT:

COMPUTED FINDING PARAMETER: HOMELESS PROGRAM ASSESSMENT NOTE^7 *Enter the first Local Progress Note Title that will be used for documenting Homelessness Services (<u>exclusively used for such</u>)*

CONDITION:

CONDITION CASE SENSITIVE:

USE STATUS/COND IN SEARCH:

Choose from:

CF VA-PROGRESS NOTE Finding \# 3

*CF VA-PROGRESS NOTE Finding \# 4*

CF VA-PROGRESS NOTE Finding \# 5

HF ALREADY RECEIVING ASSIST WITH HOUSING Finding \# 2

RL VA-HOMELESSNESS STOP CODES Finding \# 1

Select Finding: *Now edit the next CF (if more than one title will be used)To document Homelessness Services – doing the same Enter the title inthe COMPUTED FINDING PARAMETER: field*Repeat a third time – editing the next CF for a 3<sup>rd</sup> Title.

If more than three titles will be used to document Homelessness Services provided in clinics where the Stop code is different than the ones mentioned above, you may enter more titles, by entering more instances of the Computed Finding called, “VA-HOMELESSNESS”.

While still editing the Reminder Term, enter a 4<sup>th</sup> iteration of the Computed Finding by following what is shown below:

CF VA-PROGRESS NOTE Finding \# 3

CF VA-PROGRESS NOTE Finding \# 4

CF VA-PROGRESS NOTE Finding \# 5

HF ALREADY RECEIVING ASSIST WITH HOUSING Finding \# 2

RL VA-HOMELESSNESS STOP CODES Finding \# 1

Select Finding: *"CF.VA-PROGRESS NOTE" Type using Quotation Marks!*

Searching for a REMINDER COMPUTED FINDING, (pointed-to by FINDING ITEM)

VA-PROGRESS NOTE NATIONAL

...OK? *Yes// (Yes)*

Are you adding 'VA-PROGRESS NOTE' as a new FINDINGS (the 6TH for this REMINDER

TERM)? No// *Say Yes, then enter 4<sup>th</sup> title in COMPUTED FINDING PARAMETER: field.*A fifth title would be entered the same way. Hopefully you won’t need that many!

4.  Place the Clinical Reminder on the Cover Sheet for ALL Primary Care and Mental Health Clinics (SYSTEM).  
VA-LIPID STATIN RX CVD/DM \[Assess Statin Use – Lipids (CVD/DM)\] Post-Installation Instructions

1.  Verify that the reminder and the dialog have been installed on your system.

> Reminder: VA-LIPID STATIN RX CVD/DM (VER1.0)  
> Dialog: VA-LIPID STATIN RX CVD/DM

2.  Map any local items to reminder terms
1.  Existing national reminder terms: the following terms already exist on each VistA system and should have already been mapped. Verify that your local findings are appropriately included in these terms. If the prior mapping was incomplete or has not been maintained, then this reminder will not work correctly.

> VA-LDL

> VA-LIFE EXPECTANCY \<6 MONTHS

> VA-LIPID PROFILE ORDERABLE

> VA-ORDER LIPID PROFILE HEALTH FACTOR

> VA-OUTSIDE LDL 100-119

> VA-OUTSIDE LDL 120-129

> VA-OUTSIDE LDL \<100

> VA-OUTSIDE LDL \>129

2.  New Reminder terms requiring mapping: the following reminder terms are imported with this reminder installation but need to be mapped by the local reminder coordinator.  
      
    VA-STATIN HIGH DOSE  
    VA-STATIN MODERATE DOSE  
      
    The correct mapping of these 2 terms to drug findings (DR) is critical to allow the reminder to assess the doses of statins that are in use. Use only drug findings – do NOT use generic drugs or drug classes.  
      
    VA-STATIN HIGH DOSE: include all drug findings that have a dose of statin that even if split in half would still be a moderate dose.  
      
    ATORVASTATIN CALCIUM 20MG TAB

> ATORVASTATIN CALCIUM 40MG TAB

> ATORVASTATIN CALCIUM 80MG TAB

> EZETIMIBE 10MG/SIMVASTATIN 40MG TAB

> EZETIMIBE 10MG/SIMVASTATIN 80MG TAB

> PRAVASTATIN NA 80MG TAB

> ROSUVASTATIN CA 10MG TAB

> ROSUVASTATIN CA 20MG TAB

> ROSUVASTATIN CA 40MG TAB

> SIMVASTATIN 40MG TAB

> SIMVASTATIN 80MG TAB

> VA-STATIN MODERATE DOSE: only include doses that if split would no longer be considered a moderate dose.  

> ATORVASTATIN CALCIUM 10MG TAB

> EZETIMIBE 10MG/SIMVASTATIN 20MG TAB

> FLUVASTATIN NA 80MG SA TAB

> LOVASTATIN 40MG TAB

> PRAVASTATIN NA 40MG TAB

> ROSUVASTATIN CA 5MG TAB

> SIMVASTATIN 20MG TAB

3.  Reminder terms that might benefit from local review: The following reminder terms are exported with the reminder. Most of these already have a mapped finding that is entered through the dialog and therefore will work without any additional mapping. If there are local findings that have been in use in the past that fit into these terms, then mapping locally may be appropriate. The CHD risk terms are exported empty for those few sites that have been using a risk calculator to record this information.  
      
    VA-CHD RISK \<=20%

> VA-CHD RISK \>20%

> VA-DIABETES DX INCORRECT

> VA-IHD/ASVD DX INCORRECT

> VA-STATIN ADD/ADJUST

> VA-STATIN ON HIGHEST TOLERATED DOSE

> VA-STATIN TEMPORARY CONTRAIND

> VA-LDL NON-ADHERENCE WITH RX

3.  Dialog Elements
1.  Display of Lipid Panel results: The dialog element VA-LDL DISPLAY PRIOR RESULTS contains a health summary object that is meant to display any recent lipid panel results. The health summary object is \|LIPID PANEL RESULTS\|. Verify that the correct information is being displayed in the dialog. Update the health summary object if this is not complete.
2.  Ordering Statin medication: A local dialog group is included in the dialog that allows sites to add a quick order, a menu or additional dialog elements for ordering statins. It is exported with PSO OERR  
    NAME: GP LDL STATIN ORDERS NOT ON STATIN Replace

> DISABLE:

> CLASS: LOCAL//

> SPONSOR:

> REVIEW DATE:

> RESOLUTION TYPE: ORDERED//

> ORDERABLE ITEM:

> Finding item: Q PSO OERR  
> FINDING ITEM: PSO OERR//  

> 3. Recording outside LDL: A local dialog group is included in the dialog that allows sites to customize the way that outside results are recorded. CPT codes are included as additional findings and any changes that local sites make to this group should incorporate these CPT codes in their local elements.

> GP LIPID OUTSIDE LEVELS LOCAL  

> 4. Ordering Lipid profile: The group VA-IHD LIPID ORDER GROUP contains 2 options for ordering an LDL. Enter any local quick orders or menus that would be useful for the lipid profile and for the direct LDL. If your site has restrictions on ordering one of these items, insert a generic order with that information as the dialog finding.

> VA-IHD FASTING LIPID ORDERED  
> VA-IHD DIRECT LDL ORDERED

> The element VA-HF LDL ORDER 2 MONTHS is for ordering a future lipid profile in ~ 2 months for patients who have had an adjustment. Enter any local menu or quick order for this item if appropriate.  

> 5. Incorrect diagnoses: if you have local health factors that you use for entering incorrect diagnoses, then you may want to ADD them as additional findings in these dialog elements.

> VA-DX INCORRECT DIABETES

> FINDING ITEM: INCORRECT DIABETES DIAGNOSIS//

> Select ADDITIONAL FINDINGS: HF.INCORRECT DX OF DM  

> D. Activate Reminder: Turn the reminder on for the pilot users and testers using the assignment options in CPRS. After verification that it is working correctly, then assign it to the appropriate users.

# Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DO NOT QUEUE THE INSTALL!!

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # .

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select Installation Option: INstall Package(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select INSTALL NAME:    PXRM\*2.0\*27    9/12/12@15:07:40

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# =\> PXRM\*2.0\*27  ;Created on Sep 07, 2012@11:11:52

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # This Distribution was loaded on Sep 12, 2012@15:07:40 with header of 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# PXRM\*2.0\*27  ;Created on Sep 07, 2012@11:11:52

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# It consisted of the following Install(s):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# PXRM\*2.0\*27

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Checking Install for Package PXRM\*2.0\*27

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Questions for PXRM\*2.0\*27

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Incoming Files:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # REMINDER EXCHANGE  (including data)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Note:  You already have the 'REMINDER EXCHANGE' File.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# I will OVERWRITE your data with mine.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Want KIDS to INHIBIT LOGONs during the install? NO// 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Enter the Device you want to print the Install messages.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# You can queue the install by enter a 'Q' at the device prompt.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Enter a '^' to abort the install.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # DEVICE: HOME//   SSH VIRTUAL TERMINAL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # # Install Started for PXRM\*2.0\*27 : 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Sep 12, 2012@15:08:45

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Build Distribution Date: Sep 07, 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Sep 12, 2012@15:08:45

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Pre-Install Routine: PRE^PXRMP27I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # DISABLE options.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # DISABLE protocols.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Data Dictionaries: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Sep 12, 2012@15:08:45

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Data: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Sep 12, 2012@15:08:47

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Post-Install Routine: POST^PXRMP27I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # ENABLE options.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # ENABLE protocols.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # There are 3 Reminder Exchange entries to be installed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry VA-HOMELESSNESS SCREENING               

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry VA-LIPID STATIN RX CVD/DM (VER1.0)      

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry VA-LIPID STATIN RX CVD/DM DIALOG        

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Finding LT.LDL CHOLESTEROL does not exist, what do you want to do?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Select one of the following:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # D         Delete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# P         Replace with an existing entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Q         Quit the install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Enter response: P  Replace with an existing entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select LABORATORY TEST NAME: LDL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Contact your Lab ADPAC for help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Contact your Lab ADPAC for help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LDL (CALC.)  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LDL DIRECT  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# CHOOSE 1-2: 1  LDL (CALC.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Selection item L.CHOLESTEROL HDL does not exist, what do you want to do?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Select one of the following:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # D         Delete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# P         Replace with an existing entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Q         Quit the install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Enter response: P  Replace with an existing entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select LABORATORY TEST NAME: HDL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# HDL CHOLESTEROL  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# HDL-REF..  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# CHOOSE 1-2: 1  HDL CHOLESTEROL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Selection item L.LDL CHOLESTEROL does not exist, what do you want to do?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Select one of the following:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # D         Delete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# P         Replace with an existing entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Q         Quit the install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Enter response: P  Replace with an existing entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select LABORATORY TEST NAME: LDL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Contact your Lab ADPAC for help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Contact your Lab ADPAC for help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LDL (CALC.)  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LDL DIRECT  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# CHOOSE 1-2: 1  LDL (CALC.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Selection item L.LDL CHOLESTEROL does not exist, what do you want to do?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Select one of the following:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # D         Delete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# P         Replace with an existing entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Q         Quit the install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # PXRM\*2.0\*27                                   

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Enter response: P  Replace with an existing entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select LABORATORY TEST NAME: LDL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Contact your Lab ADPAC for help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LIPID PROFILE is a lab panel, it cannot be used as a reminder finding!

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Contact your Lab ADPAC for help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LDL (CALC.)  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# LDL DIRECT  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# CHOOSE 1-2: 1  LDL (CALC.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating Routine file...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating KIDS files...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # PXRM\*2.0\*27 Installed. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Sep 12, 2012@15:10:51

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Message sent \#53288961

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# 100%                 25             50             75               

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Complete  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Install Completed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Acronyms

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
