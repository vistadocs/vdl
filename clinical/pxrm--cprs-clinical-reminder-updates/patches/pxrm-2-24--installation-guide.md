---
title: PXRM*2*24 High Risk Mental Health Patient-National Reminder and Flag Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: High Risk Mental Health Patient-National Reminder and Flag
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*24
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 1
description: ![](pxrm-2-24-high-risk-mental-health-patient-national-reminder-and-flag-installatio/001.png)
audience: 
keywords: 
  - table
  - contents
  - install
  - risk
  - high
  - routine
  - installing
  - calculated
  - patient
  - flag
page_count: 0
word_count: 15485
section_count: 16
table_count: 18
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: April 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_24_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_24_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-24-high-risk-mental-health-patient-national-reminder-and-flag-installatio/001.png)

High Risk Mental Health Patient –

National Reminder and Flag

<u>Patches</u>DG\*5.3\*849GMTS\*2.7\*104OR\*3.0\*348PXRM\*2\*24SD\*5.3\*588 TIU\*1.0\*265

INSTALLATION and SETUP GUIDE

April 2013*Revised May 9, 2013*

Office of Information and Technology (OIT)

Product Development

Contents

> [a. Backup a Transport Global [13](#backup-a-transport-global)](#backup-a-transport-global)

> [b. Compare Transport Global to Current System [14](#compare-transport-global-to-current-system)](#compare-transport-global-to-current-system)

> [c. Verify Checksums in Transport Global [14](#verify-checksums-in-transport-global)](#verify-checksums-in-transport-global)

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
  - [OR\3\348](#or3348)
  - [Related Web Sites](#related-web-sites)
- [Pre-Installation](#pre-installation)
  - [## Required Software for PXRM\2\24](#required-software-for-pxrm224)
  - [Required Software for DG\5.3\836](#required-software-for-dg53836)
  - [Estimated Installation Time: 10-15 minutes](#estimated-installation-time-10-15-minutes)
  - [# Installation](#installation)
    - [## Retrieve the host file containing the multi-package build, HIGH RISK MH 2.0.](#retrieve-the-host-file-containing-the-multi-package-build-high-risk-mh-20)
  - [Install the build first in a training or test account.](#install-the-build-first-in-a-training-or-test-account)
  - [Load the distribution.](#load-the-distribution)
  - [## Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
  - [## Install the build.](#install-the-build)
- [NOTE: We recommend that you do not queue the install.](#note-we-recommend-that-you-do-not-queue-the-install)
  - [Install File Print](#install-file-print)
  - [## Build File Print](#build-file-print)
  - [Post-installation routines](#post-installation-routines)
- [Post-Install Set-up Instructions](#post-install-set-up-instructions)
- [Select OPTION NAME: USR](#select-option-name-usr)
- [USR BUSINESS RULE MANAGEMENT       Manage Business Rules     action](#usr-business-rule-management-manage-business-rules-action)
- [USR CLASS DEFINITION       User Class Definition     action](#usr-class-definition-user-class-definition-action)
- [USR CLASS MANAGEMENT MENU       User Class Management     menu](#usr-class-management-menu-user-class-management-menu)
- [USR INITIALIZE MEMBERSHIP    Initialize Membership of User Classes action](#usr-initialize-membership-initialize-membership-of-user-classes-action)
- [USR LIST MEMBERSHIP BY CLASS       List Membership by Class     action](#usr-list-membership-by-class-list-membership-by-class-action)
- [Press \<RETURN\> to see more, '^' to exit this list, OR](#press-return-to-see-more-to-exit-this-list-or)
- [CHOOSE 1-5: 2  USR CLASS DEFINITION     User Class Definition     action](#choose-1-5-2-usr-class-definition-user-class-definition-action)
- [User Class Definition](#user-class-definition)
- [# Select User Class Status: ACTIVE//    Active](#select-user-class-status-active-active)
- [Start With Class: FIRST//](#start-with-class-first)
- [Go To Class: LAST//](#go-to-class-last)
- [Searching for the User Classes..................................................](#searching-for-the-user-classes)
- [# <u>User Classes                  Oct 30, 2012@09:04:33          Page:    9 of   42</u>](#uuser-classes-oct-30-2012090433-page-9-of-42u)
- [ACTIVE USER CLASSES                    622 Classes](#active-user-classes-622-classes)
- [<u>+     Class Name                                         Abbrev                </u>](#u-class-name-abbrev-u)
- [DERMATOLOGIST: CLINICAL & LABORATORY                DERM](#dermatologist-clinical-laboratory-derm)
- [DERMATOLOGY FELLOW                                  DERM](#dermatology-fellow-derm)
- [DERMATOPATHOLOGIST                                  DERMP](#dermatopathologist-dermp)
- [DETECTIVE                                           DET](#detective-det)
- [DEVELOPER                                           DEV](#developer-dev)
- [<span class="mark">126  DGPF PATIENT RECORD FLAGS MGR</span>                       PRFM](#span-classmark126-dgpf-patient-record-flags-mgrspan-prfm)
- [DIABETES STUDY NURSE                                DSRN](#diabetes-study-nurse-dsrn)
- [DIALYSIS TECHNICIAN                                 DIALTEC](#dialysis-technician-dialtec)
- [DIETETIC INTERN                                     DI](#dietetic-intern-di)
- [DIETETIC TECHNICIAN STUDENT                         DTS](#dietetic-technician-student-dts)
- [+         + Next Screen  - Prev Screen  ?? More Actions](#next-screen-prev-screen-more-actions)
- [Find                      Expand/Collapse Class     Change View](#find-expandcollapse-class-change-view)
- [Create a Class            List Members              Quit](#create-a-class-list-members-quit)
- [Edit User Class](#edit-user-class)
- [Select Action: Next Screen// 126](#select-action-next-screen-126)
- [Listing Members of \#126](#listing-members-of-126)
- [# <u>User Class Members            Oct 30, 2012@09:05:11          Page:    1 of    1</u>](#uuser-class-members-oct-30-2012090511-page-1-of-1u)
- [DGPF PATIENT RECORD FLAGS MGRs                5 Members](#dgpf-patient-record-flags-mgrs-5-members)
- [<u>     Member                                                 Effective  Expires </u>](#u-member-effective-expires-u)
- [MHPROVIDER,THREE](#mhproviderthree)
- [MHPROVIDER,TWELVE 10/18/11](#mhprovidertwelve-101811)
- [MHPROVIDER,TEN](#mhproviderten)
- [MHPROVIDER,TWO 10/18/11](#mhprovidertwo-101811)
- [WHPROVIDER,THIRTEEN](#whproviderthirteen)
- [(?SBPN) missing SIGNATURE BLOCK PRINTED NAME                       \>\>\>](#sbpn-missing-signature-block-printed-name)
- [Add                       Remove                    Change View](#add-remove-change-view)
- [Edit                      Schedule Changes          Quit](#edit-schedule-changes-quit)
- [Select Action: Quit// AD   Add](#select-action-quit-ad-add)
- [Select MEMBER: MHCOORDINATOR, TWO       TM          CAC MD](#select-member-mhcoordinator-two-tm-cac-md)
- [MEMBER: MHCOORDINATOR, TWO       //](#member-mhcoordinator-two)
- [EFFECTIVE DATE: NOW  (OCT 30, 2012)](#effective-date-now-oct-30-2012)
- [EXPIRATION DATE:](#expiration-date)
- [Back-Out Plan for Production Environment](#back-out-plan-for-production-environment)
- [Appendix A: Installation Examples](#appendix-a-installation-examples)
- [# First-Time Install](#first-time-install)
- [# NOTE: We recommend that you not queue the install.](#note-we-recommend-that-you-not-queue-the-install)
- [Select Installation \<TEST ACCOUNT\> Option: Load a Distribution](#select-installation-test-account-option-load-a-distribution)
- [# # Installation after Previous Install](#installation-after-previous-install)
- [# # Select Installation \<TEST ACCOUNT\> Option: Install Package(s)](#select-installation-test-account-option-install-packages)
- [Select INSTALL NAME: HIGH RISK MH 2.0 12/10/12@11:06:05](#select-install-name-high-risk-mh-20-121012110605)
- [=\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34](#high-risk-mental-health-phase-2-created-on-dec-07-2012101634)
- [# This Distribution was loaded on Dec 10, 2012@11:06:05 with header of](#this-distribution-was-loaded-on-dec-10-2012110605-with-header-of)
- [High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34](#high-risk-mental-health-phase-2-created-on-dec-07-2012101634-1)
- [It consisted of the following Install(s):](#it-consisted-of-the-following-installs)
- [HIGH RISK MH 2.0 TIU\1.0\265 DG\5.3\849 SD\5.3\588 GMTS\2.7\104](#high-risk-mh-20-tiu10265-dg53849-sd53588-gmts27104)
- [OR\3.0\348 PXRM\2.0\24](#or30348-pxrm2024)
- [Checking Install for Package HIGH RISK MH 2.0](#checking-install-for-package-high-risk-mh-20)
- [# Install Questions for HIGH RISK MH 2.0](#install-questions-for-high-risk-mh-20)
- [# # Checking Install for Package TIU\1.0\265](#checking-install-for-package-tiu10265)
- [# Install Questions for TIU\1.0\265](#install-questions-for-tiu10265)
- [# # Checking Install for Package DG\5.3\849](#checking-install-for-package-dg53849)
- [# Install Questions for DG\5.3\849](#install-questions-for-dg53849)
- [# # Incoming Mail Groups:](#incoming-mail-groups)
- [# Enter the Coordinator for Mail Group 'DGPF CLINICAL HR FLAG REVIEW': CRDEVELOPER,ONE](#enter-the-coordinator-for-mail-group-dgpf-clinical-hr-flag-review-crdeveloperone)
- [OC OI&T STAFF](#oc-oit-staff)
- [# Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<Enter\>](#want-kids-to-rebuild-menu-trees-upon-completion-of-install-no-enter)
- [# Checking Install for Package SD\5.3\588](#checking-install-for-package-sd53588)
- [# Install Questions for SD\5.3\588](#install-questions-for-sd53588)
- [# # Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<Enter\>](#want-kids-to-rebuild-menu-trees-upon-completion-of-install-no-enter-1)
- [# Checking Install for Package GMTS\2.7\104](#checking-install-for-package-gmts27104)
- [Will first run the Environment Check Routine, GMTSY104](#will-first-run-the-environment-check-routine-gmtsy104)
- [# # CHECKING RECENT ADDITIONS TO HEALTH SUMMARY COMPONENT FILE](#checking-recent-additions-to-health-summary-component-file)
- [# Medication Worksheet (Tool \#2): OK](#medication-worksheet-tool-2-ok)
- [# MAS CONTACTS: OK](#mas-contacts-ok)
- [# MAS MH CLINIC VISITS FUTURE: OK](#mas-mh-clinic-visits-future-ok)
- [# MH HIGH RISK PRF HX: OK](#mh-high-risk-prf-hx-ok)
- [# MH TREATMENT COORDINATOR: OK](#mh-treatment-coordinator-ok)
- [# Install Questions for GMTS\2.7\104](#install-questions-for-gmts27104)
- [# # Checking Install for Package OR\3.0\348](#checking-install-for-package-or30348)
- [# Install Questions for OR\3.0\348](#install-questions-for-or30348)
- [# Incoming Files:](#incoming-files)
- [# # OE/RR NOTIFICATIONS](#oerr-notifications)
- [Note: You already have the 'OE/RR NOTIFICATIONS' File.](#note-you-already-have-the-oerr-notifications-file)
- [# Checking Install for Package PXRM\2.0\24](#checking-install-for-package-pxrm2024)
- [# Install Questions for PXRM\2.0\24](#install-questions-for-pxrm2024)
- [# Incoming Files:](#incoming-files-1)
- [# # REMINDER COMPUTED FINDINGS (including data)](#reminder-computed-findings-including-data)
- [Note: You already have the 'REMINDER COMPUTED FINDINGS' File.](#note-you-already-have-the-reminder-computed-findings-file)
- [I will REPLACE your data with mine.](#i-will-replace-your-data-with-mine)
- [# # REMINDER EXCHANGE (including data)](#reminder-exchange-including-data)
- [Note: You already have the 'REMINDER EXCHANGE' File.](#note-you-already-have-the-reminder-exchange-file)
- [I will OVERWRITE your data with mine.](#i-will-overwrite-your-data-with-mine)
- [# # Want KIDS to INHIBIT LOGONs during the install? NO// \<Enter\>](#want-kids-to-inhibit-logons-during-the-install-no-enter)
- [Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// \<Enter\>](#want-to-disable-scheduled-options-menu-options-and-protocols-no-enter)
- [# Enter the Device you want to print the Install messages.](#enter-the-device-you-want-to-print-the-install-messages)
- [You can queue the install by enter a 'Q' at the device prompt.](#you-can-queue-the-install-by-enter-a-q-at-the-device-prompt)
- [Enter a '^' to abort the install.](#enter-a-to-abort-the-install)
- [# DEVICE: HOME// \<Enter\> SSH VIRTUAL TEMINAL Do not queue the install](#device-home-enter-ssh-virtual-teminal-do-not-queue-the-install)
- [# Install Started for HIGH RISK MH 2.0 :](#install-started-for-high-risk-mh-20)
- [Dec 10, 2012@11:07:14](#dec-10-2012110714)
- [# Build Distribution Date: Dec 07, 2012](#build-distribution-date-dec-07-2012)
- [# Installing Routines:](#installing-routines)
- [Dec 10, 2012@11:07:14](#dec-10-2012110714-1)
- [# Running Pre-Install Routine: MPBPRE^PXRMP24I](#running-pre-install-routine-mpbprepxrmp24i)
- [# Install Started for TIU\1.0\265 :](#install-started-for-tiu10265)
- [Dec 10, 2012@11:07:14](#dec-10-2012110714-2)
- [# Build Distribution Date: Dec 07, 2012](#build-distribution-date-dec-07-2012-1)
- [# Installing Routines:](#installing-routines-1)
- [Dec 10, 2012@11:07:14](#dec-10-2012110714-3)
- [# Installing PACKAGE COMPONENTS:](#installing-package-components)
- [# Installing PARAMETER DEFINITION](#installing-parameter-definition)
- [Dec 10, 2012@11:07:14](#dec-10-2012110714-4)
- [# Running Post-Install Routine: ^TIUPS265](#running-post-install-routine-tiups265)
- [# Title Created: PATIENT RECORD FLAG CATEGORY I - HIGH RISK FOR SUICIDE](#title-created-patient-record-flag-category-i-high-risk-for-suicide)
- [# Title attached to Document Class PATIENT RECORD FLAG CAT I](#title-attached-to-document-class-patient-record-flag-cat-i)
- [# Updating Routine file...](#updating-routine-file)
- [# Updating KIDS files...](#updating-kids-files)
- [# TIU\1.0\265 Installed.](#tiu10265-installed)
- [Dec 10, 2012@11:07:16](#dec-10-2012110716)
- [# Not a production UCI](#not-a-production-uci)
- [# NO Install Message sent](#no-install-message-sent)
- [# Install Started for DG\5.3\849 :](#install-started-for-dg53849)
- [Dec 10, 2012@11:07:16](#dec-10-2012110716-1)
- [# Build Distribution Date: Dec 07, 2012](#build-distribution-date-dec-07-2012-2)
- [# Installing Routines:](#installing-routines-2)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717)
- [# Installing PACKAGE COMPONENTS:](#installing-package-components-1)
- [# Installing MAIL GROUP](#installing-mail-group)
- [# Installing OPTION](#installing-option)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-1)
- [# Running Post-Install Routine: ^DG53849P](#running-post-install-routine-dg53849p)
- [The 'HIGH RISK FOR SUICIDE' PRF is already entered in the PRF NATIONAL](#the-high-risk-for-suicide-prf-is-already-entered-in-the-prf-national)
- [FLAG file, no further processing of the new national PRF field entry.](#flag-file-no-further-processing-of-the-new-national-prf-field-entry)
- [# Updating Routine file...](#updating-routine-file-1)
- [# Updating KIDS files...](#updating-kids-files-1)
- [# DG\5.3\849 Installed.](#dg53849-installed)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-2)
- [# Not a production UCI](#not-a-production-uci-1)
- [# NO Install Message sent](#no-install-message-sent-1)
- [# Install Started for SD\5.3\588 :](#install-started-for-sd53588)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-3)
- [# Build Distribution Date: Dec 07, 2012](#build-distribution-date-dec-07-2012-3)
- [# Installing Routines:](#installing-routines-3)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-4)
- [# Installing PACKAGE COMPONENTS:](#installing-package-components-2)
- [# Installing OPTION](#installing-option-1)
- [# Installing PARAMETER DEFINITION](#installing-parameter-definition-1)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-5)
- [# Running Post-Install Routine: ^SD53588P](#running-post-install-routine-sd53588p)
- [# Updating Parameters File...](#updating-parameters-file)
- [# SDMH PROACTIVE DAYS](#sdmh-proactive-days)
- [# 89895006^Duplicate instance not allowed.](#89895006duplicate-instance-not-allowed)
- [# SDMH NO SHOW DAYS](#sdmh-no-show-days)
- [# 89895006^Duplicate instance not allowed.](#89895006duplicate-instance-not-allowed-1)
- [# Updating Routine file...](#updating-routine-file-2)
- [# Updating KIDS files...](#updating-kids-files-2)
- [# SD\5.3\588 Installed.](#sd53588-installed)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-6)
- [# Not a production UCI](#not-a-production-uci-2)
- [# NO Install Message sent](#no-install-message-sent-2)
- [# Install Started for GMTS\2.7\104 :](#install-started-for-gmts27104)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-7)
- [# Build Distribution Date: Dec 07, 2012](#build-distribution-date-dec-07-2012-4)
- [# Installing Routines:](#installing-routines-4)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-8)
- [# Running Post-Install Routine: POST^GMTSY104](#running-post-install-routine-postgmtsy104)
- [# Updating description for Health Summary Component MH HIGH RISK FOR SUICIDE](#updating-description-for-health-summary-component-mh-high-risk-for-suicide)
- [# Update Successful](#update-successful)
- [# Updating Routine file...](#updating-routine-file-3)
- [# Updating KIDS files...](#updating-kids-files-3)
- [# GMTS\2.7\104 Installed.](#gmts27104-installed)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-9)
- [# Not a production UCI](#not-a-production-uci-3)
- [# NO Install Message sent](#no-install-message-sent-3)
- [# Install Started for OR\3.0\348 :](#install-started-for-or30348)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-10)
- [# Build Distribution Date: Dec 07, 2012](#build-distribution-date-dec-07-2012-5)
- [# Installing Routines:](#installing-routines-5)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-11)
- [# Installing Data Dictionaries:](#installing-data-dictionaries)
- [Dec 10, 2012@11:07:17](#dec-10-2012110717-12)
- [# Installing PACKAGE COMPONENTS:](#installing-package-components-3)
- [# Installing PARAMETER DEFINITION](#installing-parameter-definition-2)
- [Dec 10, 2012@11:07:18](#dec-10-2012110718)
- [# Running Post-Install Routine: POST^ORY348](#running-post-install-routine-postory348)
- [# Updating Routine file...](#updating-routine-file-4)
- [# Updating KIDS files...](#updating-kids-files-4)
- [# OR\3.0\348 Installed.](#or30348-installed)
- [Dec 10, 2012@11:07:18](#dec-10-2012110718-1)
- [# Not a production UCI](#not-a-production-uci-4)
- [# NO Install Message sent](#no-install-message-sent-4)
- [# Install Started for PXRM\2.0\24 :](#install-started-for-pxrm2024)
- [Dec 10, 2012@11:07:18](#dec-10-2012110718-2)
- [# Build Distribution Date: Dec 07, 2012](#build-distribution-date-dec-07-2012-6)
- [# Installing Routines:](#installing-routines-6)
- [Dec 10, 2012@11:07:18](#dec-10-2012110718-3)
- [# Running Pre-Install Routine: PRE^PXRMP24I](#running-pre-install-routine-prepxrmp24i)
- [# DISABLE options.](#disable-options)
- [# DISABLE protocols.](#disable-protocols)
- [# Installing Data Dictionaries:](#installing-data-dictionaries-1)
- [Dec 10, 2012@11:07:19](#dec-10-2012110719)
- [# Installing Data:](#installing-data)
- [Dec 10, 2012@11:07:19](#dec-10-2012110719-1)
- [# Running Post-Install Routine: POST^PXRMP24I](#running-post-install-routine-postpxrmp24i)
- [# ENABLE options.](#enable-options)
- [# ENABLE protocols.](#enable-protocols)
- [# There are 5 Reminder Exchange entries to be installed.](#there-are-5-reminder-exchange-entries-to-be-installed)
- [Installing Reminder Exchange entry VA-MH NO SHOW APPT CLINICS LL](#installing-reminder-exchange-entry-va-mh-no-show-appt-clinics-ll)
- [Installing Reminder Exchange entry VA-MHTC APPT STOP CODES AND EXCLUSION](#installing-reminder-exchange-entry-va-mhtc-appt-stop-codes-and-exclusion)
- [STOP](#stop)
- [Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW FOLLOW-UP](#installing-reminder-exchange-entry-va-mh-high-risk-no-show-follow-up)
- [Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW ADHOC RPT](#installing-reminder-exchange-entry-va-mh-high-risk-no-show-adhoc-rpt)
- [Installing Reminder Exchange entry VA-MHTC NEEDS ASSIGNMENT](#installing-reminder-exchange-entry-va-mhtc-needs-assignment)
- [# Renaming/inactivating health factors and terms that are no longer used.](#renaminginactivating-health-factors-and-terms-that-are-no-longer-used)
- [# Updating Routine file...](#updating-routine-file-5)
- [# Updating KIDS files...](#updating-kids-files-5)
- [# PXRM\2.0\24 Installed.](#pxrm2024-installed)
- [Dec 10, 2012@11:07:31](#dec-10-2012110731)
- [# Not a production UCI](#not-a-production-uci-5)
- [# NO Install Message sent](#no-install-message-sent-5)
- [# Running Post-Install Routine: POST^GMTSY104](#running-post-install-routine-postgmtsy104-1)
- [# Updating description for Health Summary Component MH HIGH RISK FOR SUICIDE](#updating-description-for-health-summary-component-mh-high-risk-for-suicide-1)
- [# Update Successful](#update-successful-1)
- [# Updating Routine file...](#updating-routine-file-6)
- [# Updating KIDS files...](#updating-kids-files-6)
- [# HIGH RISK MH 2.0 Installed.](#high-risk-mh-20-installed)
- [Dec 10, 2012@11:07:31](#dec-10-2012110731-1)
- [# No link to PACKAGE file](#no-link-to-package-file)
- [# # # Install Completed](#install-completed)
- [# # # # # # # # Appendix B: Instructions for Recreating/ Re-pointing Site-defined Notifications](#appendix-b-instructions-for-recreating-re-pointing-site-defined-notifications)
- [Acronyms](#acronyms)
The purpose of the High Risk Mental Health Patient- Reminder and Flag (HRMHP) project is to support Mental Health (MH) professionals in the tracking of veterans with the High Risk for Suicide Patient Record Flag (PRF) who have missed Mental Health (MH) Clinic appointments due to a no-show.
This is the second release (Phase 2) of the (HRMHP) project. It includes six patches, which will be installed as a combined build, HIGH RISK MH 2.0. This Installation Guide describes installing and setting up Phase 2.
This installation contains a post-implementation step (related to DG\*5.3\*849), which first requires all sites to have the bundle installed on their VistA system.
- The Implementation Manager will monitor sites that are installing and will contact sites to complete the install to meet the install requirement within 30 days.
- After all sites have installed, the Implementation manager will inform the HRMHP Phase 2 Project Manager.
- The Project Manager will contact the Office of Mental Health Services (OMHS) to indicate that all VistA systems have the HRMHP software installed.
- The OMHS, which has regular calls with Suicide Prevention Coordinators (SPCs) across the VA, will guide SPCs through a post-installation step.
POST-RELEASE NOTE:
This build was put on hold due to a CLINIC STOP name being changed by Patch SD\*5.3\*601 after the last version of the High Risk MH build was completed. This caused an error upon installing a reminder location list which contained that renamed CLINIC STOP.  A new build was created for distribution but unfortunately, the PXRM\*2.0\*24 patch could not be put back under development in order to update the patch description of the checksum for this routine. The checksum for routine PXRMP24E will be reflected incorrectly in the patch description. 
If your site had already installed the High Risk MH build into your test account, you will see the following after installing the updated build.
Routine Name: PXRMP24E
    Before:       2321342  After:  <span class="mark">B2321909</span>  \*\*24\*\*
If you have not installed the build into your test or production account, you will see the following after installing the updated build.
Routine Name: PXRMP24E
    Before:       n/a   After:  <span class="mark">B2321909</span>  \*\*24\*\*
Again, the patch description information for this routine will be incorrect.
DG\*5.3\*849
This build installs a new national Patient Record Flag (PRF) for suicide prevention: HIGH RISK FOR SUICIDE. Clinically, the Category I PRF for high risk for suicide will not be available to the site until the install is completed. Furthermore, we recommend that the Category I HIGH RISK FOR SUICIDE PRF should not be assigned to a patient until the post-installation step is completed by an SPC on each VistA System. Until then, all of the high risk patients will continue to have the local Category II PRFs on their record that clinicians are accustomed to working with.
This build also installs a new option, Convert Local HRMH PRF to National \[DGPF LOCAL TO NATIONAL CONVERT\], which will allow an SPC to auto-generate new national PRFs for suicide prevention from local, active, suicide prevention Category II PRFs. This option can be run in either Report-only or in Processing mode – but the Processing mode must not be run until OMHS informs the SPCs that it is OK to run.
 IMPORTANT DEPLOYMENT NOTE: SPC staff should NOT run the Processing mode of the DGPF LOCAL TO NATIONAL CONVERT option (Process Local-to-National option) until 30 days after the national release date and sites have received approval from the Office of Mental Health Services (OMHS). This will help to minimize transmission error messages among sites with shared patients. These error messages occur when one of these sites has installed and runs the conversion, but another site that also sees the same patient(s) has not installed this newly released software patch(s). SPC staff may run the Report Only mode of the option after installing the package, to get a preliminary report of local PRFs that will be converted.DG\*5.3\*849 post-installation steps on every VistA system:
- For each VistA system, OMHS will task an SPC to complete the post-install step that will automatically convert the Category II flag to the Category I flag (Process mode of DGPF LOCAL TO NATIONAL CONVERT option).
- After all sites have installed HRMHP Phase 2 patches, the Office of Mental Health Services (OMHS) will announce on their SPC conference calls and via Outlook that the Process Mode of the DGPF LOCAL TO NATIONAL CONVERT option can now be run by the assigned SPC for the VistA system.
- The assigned SPC will be responsible for ensuring that the Report-Only mode has already been run and resolved any patient issues found before running the Process mode.
- The SPC will be responsible for regularly monitoring the PRF TRANSMISSION MANAGEMENT option to ensure that there are no transmission errors between their system and other systems due to the Process mode.
- Any issues should be dealt with between the SPCs at each site. For example, if two sites treating the same patient had the Category II flag, than the PRF TRANSMISSION MANAGEMENT option will inform them of the situation, and the SPCs will figure out which site should be the owner and use the Patient Record Flag Management option to assign/change the ownership.
- The SPC will be responsible for reporting back to the OMHS when the process mode is completed.
TIU\*1.0\*265
This Text Integration Utility patch installs a new title in the TIU DOCUMENT DEFINITION: PATIENT RECORD FLAG CATEGORY I – HIGH RISK FOR SUICIDE. This title will be used with the new Patient Record Flag. The patch installation links the title to the existing document class, PATIENT RECORD FLAG CAT I.
This patch also provides one fix to TUI\*1\*260 in routine ^TIULO1. A formatting error was discovered in the MH MISSED APPOINTMENTS 10D TIU object. This is the object that will display on the High Risk MH No-Show Follow-up reminder dialog whenever a patient has missed a mental health appointment within the last 10 days.
SD\*5.3\*588
This build contains two new proactive reports that list appointments for High Risk for Suicide patients who have appointments for the day. The SD MH PROACTIVE BGJ REPORT is a background job that will run in the background and send a mail message to the members of the SD MH NO SHOW NOTIFICATION mail group. This reportwill be kicked off by the Scheduling nightly background job (SDAM BACKGROUND JOB) that should already be scheduled to run nightly on your system. It is the same background job that calls the SD MH NO SHOW NIGHTLY BGJ.
> **NOTE:** DO NOT schedule the options:
SD MH NO SHOW NIGHTLY BGJ
SD MH PROACTIVE BGJ REPORT
Scheduling’s Nightly Background Job generates these reports.
An ad hoc report option, High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\], generates a *proactive* report that can be run by the users. This report is more flexible and allows users to refine the report to their specifications. This report will list, by divisions, all patients with PRF High Risk for Suicide who have appointments in mental health clinics today. Totals will list the number of unique patients by division. The patients are listed alphabetically by division and by date/time of the appointment.
This build also allows the SD MH NO SHOW AD HOC REPORT, SD MH NO SHOW NIGHTLY BGJ, SD MH PROACTIVE AD HOC REPORT and SD MH PROACTIVE BGJ REPORT to look for PRF activity from the new national Category I Patient Record Flag, HIGH RISK FOR SUICIDE, as well as from local Patient Record Flags.
SD\*5.3\*588 contains a post-installation routine that will add two new parameters to the PARAMETERS (#8989.5) file, with associated parameter definitions added to the PARAMETER DEFINITION (#8989.51) file. The new parameter SDMH PROACTIVE DAYS stores a value that will list future appointments for the number of days stored in the parameter, for each patient on the report. This parameter is checked when Nightly SD MH PROACTIVE BGJ REPORT is run. The second new parameter is SDMH NO SHOW DAYS which also stores a value that will list future appointments for the number of days stored in the parameter, for each patient on the SD MH NO SHOW NIGHTLY BGJ Report.
The default value of 30 days will be populated by the post-init for both parameters. Sites may change the number of days stored in the parameter, by using the General Parameter Tools option, selecting the Edit Parameter Values option, and entering SDMH PROACTIVE DAYS or SDMH NO SHOW DAYS. Once changed, the reports will reflect the change by displaying the new number of days of future appointments on the report.
> Changes to the SD MH NO SHOW AD HOC REPORT:
1.  The report displays The Mental Health Treatment Coordinator (MHTC) name and the name of the care team that the MHTC is assigned to in parentheses.
2.  The report displays the results of the no-show patient contact.
> Changes to the SD MH NO SHOW AD HOC REPORT and SD MH NO SHOW NIGHTLY BGJ:
1.  The provider name is now displayed directly under the NO Show Appointment information to keep everything connected.
PXRM\*2.0\*24 - MH HIGH RISK PHASE 2NOTE: In this document you will see references to both PXRM\*2\*24 and PXRM\*2.0\*24. The difference is that PXRM\*2\*24 is the name of the patch and PXRM\*2.0\*24 is the name of the build.
This Clinical Reminders patch includes an updated reminder definition (VA-MH HIGH RISK NO-SHOW FOLLOW-UP), two new reminder definitions, (VA-MH HIGH RISK NO-SHOW ADHOC RPT and VA-MHTC NEEDS ASSIGNMENT), a new computed finding (VA-PCMM MHTC), and a new dialog that will display the Mental Health Treatment Coordinator (MHTC)..
The MH HIGH RISK NO-SHOW ADHOC RPT reminder determines whether Mental Health (MH) professionals have followed up during the week following a No-Show MH appointment for a patient with an active High Risk for Suicide Patient Record Flag. This reminder is called from a Scheduling report for each No-Show MH appointment.
A new reminder titled VA-MHTC NEEDS ASSIGNMENT is available and can be used from CPRS on the Cover Sheet’s Reminders Due section when the patient is a candidate for MHTC assignment. The reminder looks for three MH appointments within a specific period of time, and then checks to see if the MHTC is defined for the patients. The reminder will be due when no MHTC is currently assigned to the patient. A Reminders Due Report can be run weekly to get a list of patients who have not yet been assigned an MHTC. MHTC NEEDS ASSIGNMENT uses a new Reminder Location List called VA-MHTC APPT STOP CODES LL in the Computed Finding: VA-Appointments for a Patient. The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services. The new VA-PCMM MHTC Computed Finding can be used in Reminder Definitions to get the MHTC assigned to a patient.
A new term, The VA-MH HIGH RISK FOR SUICIDE PRF was added, to be used in the Reminder Definitions in the High Risk for Suicide Patient – Reminder & Flag project. The following description was added to the VA-HIGH RISK FOR SUICIDE PRF Reminder Term:
> This reminder looks for the national category I HIGH RISK FOR SUICIDE patient record flag and the local category II patient record flag used at your site. 
This term is distributed to look for the local name HIGH RISK FOR SUICIDE, which is the first mapped finding in the Mapped Findings. The Computed Finding Parameter of HIGH RISK FOR SUICIDE^L means use the local patient record flag called HIGH RISK FOR SUICIDE.  If your site uses a different category II patient record flag name, then the computed finding parameter for the first mapped finding should be changed.  For example, if your site uses SUICIDE RISK as the name of the category II patient record flag, then the Computed Finding Parameter should be changed to SUICIDE RISK^L.
*Do not change the second mapped finding with the Computed Finding Parameter of HIGH RISK FOR SUICIDE^N.*GMTS\*2.7\*104
This patch will modify two entries in the Health Summary Component file (142.1): MH HIGH RISK PRF HX and MH TREATMENT COORDINATOR.
These components are used in the VA-MH HIGH RISK PATIENT and REMOTE MH
HIGH RISK PATIENT Health Summaries, and are also available for use in the Health Summary Adhoc Report. Additionally, the VA-MH HIGH RISK PATIENT Health Summary is also embedded in the VA-MH HIGH RISK NO SHOW FOLLOW-UP Reminder Dialog released in Phase I of this project.
The MH HIGH RISK PRF HX component now includes the assignment history for the newly created Category I Patient Record Flag (HIGH RISK FOR SUICIDE). The assignment history in Health Summary will display both Category II (local) and Category I (national) assignments for High Risk for Suicide until all local entries have been converted to the national flag.
The MH TREATMENT COORDINATOR component will now be fully functional and display the mental health treatment team, mental health treatment coordinator (MHTC), and the MHTC contact information.

## OR\*3\*348

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds a new provider recipient, Primary Care Management Module (PCMM) Mental Health Treatment Coordinator (MHTC), to the existing ORB PROVIDER RECIPIENTS parameter. It will be added as a “C” code to the existing “PATOMERS” values:

> P (Primary Provider): deliver notification to the patient's Primary Provider.

> A (Attending Physician): deliver notification to the patient's Attending Physician.

T (Patient Care Team): deliver notification to the patient's OE/RR Teams (personal patient and team lists are evaluated for potential recipients) and to devices on an OE/RR team).

> O (Ordering Provider): deliver notification to the provider who placed the order which trigger the notification.

> M (PCMM Team): deliver notification to users/providers linked to the patient via PCMM Team Position assignments.

> E (Entering User): deliver notification to the user/provider who entered the order's most recent activity.

> R (PCMM Primary Care Practitioner): deliver notification to the patient's PCMM Primary Care Practitioner.

> S (PCMM Associate Provider): deliver notification to the patient's PCMM Associate Provider.

> C (PCMM Mental Health Treatment Coordinator): deliver notification to the patient's PCMM Mental Health Treatment Coordinator.

With this enhancement, MHTCs can now specify to be default provider recipients of certain pertinent notifications, such as for Admissions, Discharge, and Deceased Patient, to name a few.

The following parameters in the PARAMETERS DEFINITION file \#8989.51 will also be updated accordingly to reflect these changes:

- ORB PROVIDER RECIPIENTS
- ORB OI EXPIRING - INPT PR
- ORB OI EXPIRING - OUTPT PR
- ORB OI ORDERED - INPT PR
- ORB OI ORDERED - OUTPT PR
- ORB OI RESULTS - INPT PR
- ORB OI RESULTS - OUTPT PR

A new notification is also being released with this patch: SUICIDE ATTEMPTED/ COMPLETED. This informational notification is triggered by Clinical Reminders when a MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in PCE. It is exported with package parameter values set as follows:

. ORB ARCHIVE PERIOD - 30

. ORB DELETE MECHANISM - Individual Recipient

. ORB FORWARD BACKUP REVIEWER - No

. ORB FORWARD SUPERVISOR - No

. ORB FORWARD SURROGATES - No

. ORB PROCESSING FLAG - Disabled

. ORB PROVIDER RECIPIENTS - MHTC and PCMM Team (CM)

. ORB URGENCY - High

\*\*\*Important Note\*\*\*Notifications are processed by IEN (internal entry number) from the OE/RR NOTIFICATIONS File \#100.9. Any site-defined notifications run the risk of being over-written by new notifications that are nationally released, especially those within the number range 1-9999, which is reserved for national release. Specifically, for this project, IEN \#77 is being added. If you have a locally defined notification with the IEN of 77, you will need to renumber it before this patch is installed. See [Appendix B](#appendix-b-instructions-for-recreating-re-pointing-site-defined-notifications) for instructions on how to recreate or re-point site-defined notifications occupying a national number space.

A validation routine is also added to the input transform of the NUMBER field (#.001) of the OE/RR Notifications File \#100.9. This validation routine will prohibit new national notification entries by the site and validate the correct local notification number scheme \<your site's station number\>\<incremental notification number 01-99\>.

Related DocumentationClinical Reminders PXRM\*2\*24 Documentation

|                              |                  |
|------------------------------|------------------|
| Manual                   | File name    |
| Installation and Setup Guide | PXRM_2_24_IG.PDF |
| Release Notes                | PXRM_2_24_RN.PDF |
| User Manual                  | PXRM_2_UM.PDF    |
| Manager’s Manual             | PXRM_2_MM.PDF    |

Health Summary GMTS\*2.7\*104 Documentation

|                  |                     |
|------------------|---------------------|
| Manual       | File name       |
| User Manual      | HSUM_2_7_104_UM.PDF |
| Technical Manual | HSUM_2_7_104_TM.PDF |

TIU\*1\*265 Documentation

|                                    |               |
|------------------------------------|---------------|
| Manual                         | File name |
| Clinical Coordinator & User Manual | TIUUM.PDF     |
| Technical Manual                   | TIUTM.PDF     |

Scheduling SD\*5.3\*588 and Registration DG\*5.3\*849 Documentation

|                                                     |                         |
|-----------------------------------------------------|-------------------------|
| Manual                                          | File name           |
| PIMS Technical Manual (contains SD and DG updates)  | PIMSTM.PDF              |
| Scheduling User Manual – Outputs Menu               | PIMsSchOutput.pdf       |
| Scheduling User Manual - Menus, Intro & Orientation | PIMsSchIntro.pdf        |
| Patient Record Flag User Guide                      | PatRecFlagUG.pdf        |
| SDDG Install Review Guide                           | SDDG_Install_Review.pdf |

CPRS OR\*2.0\*348 Documentation

| Manual                         | File Name |
|------------------------------------|---------------|
| CPRS User Guide: GUI Version       | CPRSGUIUM.PDF |
| CPRS Technical Manual: GUI Version | CPRSGUITM.PDF |
| CPRS Technical Manual              | CPRSLMTM.PDF  |

## Related Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                       |                                                           |                                                                           |
|---------------------------------------|-----------------------------------------------------------|---------------------------------------------------------------------------|
| SITE                              | URL                                                   | DESCRIPTION                                                           |
| National Clinical Reminders site      | <http://vista.med.va.gov/reminders>                       | Contains manuals, presentations, and information about Clinical Reminders |
| National Clinical Reminders Committee | <http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx> | This GROUP directs the development of new and revised national reminders  |
| VistA Document Library                | <http://www.va.gov/vdl/>                                  | Contains manuals for Clinical Reminders and related applications.         |

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We recommend that the team members who will be responsible for implementing this project coordinate with each other before installing the patches, to determine the first three pre-install steps. This team could include MH coordinators, Suicide Prevention Coordinators, Clinical Application Coordinators (CACs), Reminders Managers, and IRM staff.

1.  Make sure that the regular Scheduling Background Job \[SDAM BACKGROUND JOB\] has been scheduled, so that the High Risk MH No-Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\] will be sent to appropriate staff.

> **NOTE:** your site should not *specifically* schedule the SD MH NO SHOW NIGHTLY BGJ. It should be running automatically at the time when the SDAM BACKGROUND JOB runs each night to process the appointments.

Example

> <u>Option Name</u>: SDAM BACKGROUND JOB

> Menu Text: Appointment Status Update (Backg TASK ID: 3940982

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> QUEUED TO RUN AT WHAT TIME: AUG 30,2012@00:15

> DEVICE FOR QUEUED JOB OUTPUT:

> QUEUED TO RUN ON VOLUME SET:

> RESCHEDULING FREQUENCY: 1D

> TASK PARAMETERS:

> SPECIAL QUEUEING: STARTUP

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2.  Determine the name of the Mail Group Owner for the new Mail Group DGPF CLINICAL HR FLAG REVIEW. Note: The new DGPF CLINICAL HR FLAG REVIEW mail group will also be used to send a message to its members when the patient’s flag needs to be reviewed following existing PRF review processes (continue/inactivate/delete). During the DG\*5.3\*849 install, the installer will be asked to enter a name for the Mail Group Owner. *We recommend that a CAC and/or an MH/SPC representative be present during the install, to answer this question.* This prompt appears during the installation:

> Enter the Coordinator for Mail Group 'DGPF CLINICAL HR FLAG REVIEW'

> The owner assigned will be responsible for entering the names of Suicide Prevention Coordinators (SPCs) and/or other MH professionals into the Mail Group. Sites can decide who this owner should be – an IRM staff member, a CAC, or one of the MH-SPC team. Check to see if there’s a Mail Group expert at your site. NOTE: Self enrollment is not allowed for this mail group.

> This should be the Suicide Prevention Coordinator (or designee). This name should be available to the IRM staff prior to installing the patch.

3.  After the patch is installed, IRM will need to attach the new DGPF LOCAL TO NATIONAL CONVERT option to the appropriate menu for the Suicide Prevention Coordinator (or designee). The Suicide Prevention Coordinator (or designee) will need to populate the DGPF CLINICAL HR FLAG REVIEW mail group with members as needed. This mail group will receive the reports and any error messages generated by the local-to-national PRF processing and will also receive messages when a patient’s PRF needs to be reviewed.
4.  Have the local Suicide Prevention Coordinator evaluate your local PRF entries and make any changes for the PRF conversion of local Category II flags to national Category I flags. This should be done using the Report Only action in the DGPF LOCAL TO NATIONAL CONVERT option. As part of the post-patch processing, this patch installs a new national flag data entry (HIGH RISK FOR SUICIDE) into the PRF NATIONAL FLAG file (#26.15). 

> Basic requirements of auto-creating national PRF entries

- Local flag MUST BE currently active
- Local flag information will be pulled into the new National flag at creation.
- Various comments are updated to reflect auto-created information.
- If there is an issue with generating a National flag:

> \- No National flag is created

> \- Local flag remains intact

> \- Error report will be generated

5.  If you have locally defined notifications, you may need to re-number them before this patch is installed. A new notification is being released with this patch: SUICIDE ATTEMPTED/ COMPLETED. This informational notification is triggered by Clinical Reminders when a MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in PCE. Notifications are processed by IEN (internal entry number) from the OE/RR NOTIFICATIONS File \#100.9. Any site-defined notifications run the risk of being overwritten by new notifications that are nationally released, especially those within the number range 1-9999, which is reserved for national release. Specifically, for this project, IEN \#77 is being added. If you have a locally defined notification with the IEN of 77, you will need to renumber it before this patch is installed. See [Appendix B](#appendix-b-instructions-for-recreating-re-pointing-site-defined-notifications) for instructions for recreating or re-pointing site-defined notifications.
6.  The Reminder Definitions in this project look for the national category I HIGH RISK FOR SUICIDE patient record flag and the local category II patient record flag used at your site. The new term, VA-MH HIGH RISK FOR SUICIDE PRF, used in these reminders, looks for the local name HIGH RISK FOR SUICIDE, which is the first mapped finding in the Mapped Findings. The Computed Finding Parameter of HIGH RISK FOR SUICIDE^L means use the local patient record flag called HIGH RISK FOR SUICIDE.  If your site uses a different category II patient record flag name, then the Computed Finding Parameter for the first mapped finding should be changed. For example, if your site uses SUICIDE RISK as the name of the category II patient record flag, then the computed finding parameter should be changed to SUICIDE RISK^L.

> Do not change the second mapped finding with the Computed Finding Parameter of HIGH RISK FOR SUICIDE^N.

## ## Required Software for PXRM\*2\*24

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package/Patch</strong></td>
<td><strong>Namespace</strong></td>
<td><strong>Version</strong></td>
<td><strong>Comments</strong></td>
</tr>
<tr class="even">
<td><p>Clinical Reminders</p>
<p>PXRM*2*18</p>
<p>PXRM*2*22</p></td>
<td>PXRM</td>
<td>2.0</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td><p>GEN. MED. REC. – VITALS</p>
<p>GMRV*5*25</p></td>
<td>GMRV</td>
<td>5.0</td>
<td></td>
</tr>
<tr class="even">
<td>Health Summary</td>
<td>GMTS</td>
<td>2.7</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>HL</td>
<td>1.6</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>Kernel</td>
<td>XU</td>
<td>8.0</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td><p>Kernel Toolkit</p>
<p>XT*7.3*111</p></td>
<td>XT</td>
<td>7.3</td>
<td></td>
</tr>
<tr class="even">
<td>MailMan</td>
<td>XM</td>
<td>7.1</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td><p>Mental Health Assistant (MHA)</p>
<p>YS*5.01*103 + MH dlls</p></td>
<td>YS</td>
<td>5.01</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td><p>NATIONAL DRUG FILE</p>
<p>PSN*4.0*176</p></td>
<td>PSN</td>
<td>4.0</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>Order Entry/Results Reporting</td>
<td>OR</td>
<td>3.0</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td><p>Pharmacy Data Management</p>
<p>PSS*1.0*133</p></td>
<td>PSS</td>
<td>1.0</td>
<td></td>
</tr>
<tr class="odd">
<td><p>Outpatient Pharmacy</p>
<p>PSO*7.0*299</p></td>
<td>PSO</td>
<td>7.0</td>
<td></td>
</tr>
<tr class="even">
<td><p>Primary Care Management Module (PCMM)</p>
<p>SD*5.3*575</p></td>
<td>SD</td>
<td>5.3</td>
<td></td>
</tr>
<tr class="odd">
<td><p>RADIOLOGY/NUCLEAR MEDICINE</p>
<p>RA*5*56</p></td>
<td>RA</td>
<td>5.0</td>
<td></td>
</tr>
<tr class="even">
<td><p>Registration</p>
<p>DG*5.3*836</p></td>
<td>DG</td>
<td>5.3</td>
<td></td>
</tr>
<tr class="odd">
<td><p>Scheduling</p>
<p>SD*5.3*583</p></td>
<td>SD</td>
<td>5.3</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td>DI</td>
<td>22</td>
<td>Fully patched</td>
</tr>
</tbody>
</table>

## Required Software for DG\*5.3\*836

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package/Patch</strong></td>
<td><strong>Namespace</strong></td>
<td><strong>Version</strong></td>
<td><strong>Comments</strong></td>
</tr>
<tr class="even">
<td>Registration/Enrollment</td>
<td>DG</td>
<td>5.3</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td><p>Patient Record Flags Phase III</p>
<p>DG*5.3*650</p></td>
<td>DG</td>
<td>5.3</td>
<td></td>
</tr>
</tbody>
</table>

Required Software for SD\*5.3\*578 

|                   |               |             |               |
|-------------------|---------------|-------------|---------------|
| Package/Patch | Namespace | Version | Comments  |
| Scheduling        | SD            | 5.0         | Fully patched |

Required Software for GMTS\*2.7\*99 

|                   |               |             |               |
|-------------------|---------------|-------------|---------------|
| Package/Patch | Namespace | Version | Comments  |
| Health Summary    | GMTS          | 2.7         | Fully patched |

Required Software for TIU\*1\*260 

|                            |               |             |               |
|----------------------------|---------------|-------------|---------------|
| Package/Patch          | Namespace | Version | Comments  |
| Text Integration Utilities | TIU           | 1.0         | Fully patched |

Required Software for OR\*3\*348 

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package/Patch</strong></td>
<td><strong>Namespace</strong></td>
<td><strong>Version</strong></td>
<td><strong>Comments</strong></td>
</tr>
<tr class="even">
<td>Primary Care Management Module (PCMM)</td>
<td>SD</td>
<td>5.3</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td><p>Order Entry/Results Reporting</p>
<p>OR*3*243</p>
<p>OR*3*280</p>
<p>OR*3*296</p></td>
<td>OR</td>
<td>3.0</td>
<td></td>
</tr>
</tbody>
</table>

## Estimated Installation Time: 10-15 minutes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## # Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual describes how to install the combined build that includes builds DG\*5.3\*849, SD\*5.3\*588, GMTS\*2.7\*104, TIU\*1.0\*265, OR\*3.0\*348, and PXRM\*2.0\*24.

This build can be installed with users on the system, but it should be done during non-peak hours.

*The installation needs to be done by a person with DUZ(0) set to "@."*NOTE: We recommend having a Clinical Reminders Manager or Clinical Applications Coordinator (CAC) present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.

### ## Retrieve the host file containing the multi-package build, HIGH RISK MH 2.0. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use ftp to access the build (the name of the host file is HIGH_RISK_MH_2_0 .KID) from one of the following locations (with the ASCII file type):

> Albany <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Salt Lake City <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

## Install the build first in a training or test account. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and HIGH_RISK_MH_2.0.KID at the Host File prompt.

Example

> Select Installation Option: LOAD a Distribution

> Enter a Host File: HIGH_RISK_MH_2.0.KID

> KIDS Distribution saved on FEB 29: HIGH_RISK_MH_2_0.KID

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

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: utilities

Select Utilities \<TEST ACCOUNT\> Option: Verify Package Integrity

Select BUILD NAME: HIGH RISK MH 2.0

CHOOSE 1-2: 2 HIGH RISK MH 2.0 (Multi-Package)

TIU\*1.0\*265

DG\*5.3\*849

SD\*5.3\*588

GMTS\*2.7\*104

OR\*3.0\*348

PXRM\*2.0\*24

Want each Routine Listed with Checksums: Yes// YES

DEVICE: HOME// ;;999 HOME

PACKAGE: HIGH RISK MH 2.0 Dec 11, 2012 2:04 pm PAGE 1

----------------------------------------------------------------------------- 0 Routine checked, 0 failed.

PACKAGE: TIU\*1.0\*265 Dec 11, 2012 2:04 pm PAGE 1

-----------------------------------------------------------------------------

TIULO1 Calculated 21084404

1 Routine checked, 0 failed.

PACKAGE: DG\*5.3\*849 Dec 11, 2012 2:04 pm PAGE 1

-----------------------------------------------------------------------------

DG53849P Calculated 7093789

DGPFCNR Calculated 62901548

DGPFCNV Calculated 95099109

3 Routines checked, 0 failed.

PACKAGE: SD\*5.3\*588 Dec 11, 2012 2:04 pm PAGE 1

-----------------------------------------------------------------------------

SD53588P Calculated 6953359

SDAMQ Calculated 9860749

SDMHAD Calculated 116008938

SDMHAD1 Calculated 108729141

SDMHAP Calculated 89393379

SDMHAP1 Calculated 16336515

SDMHNS Calculated 22141437

SDMHNS1 Calculated 101585316

SDMHPRO Calculated 15994772

SDMHPRO1 Calculated 19699190

10 Routines checked, 0 failed.

PACKAGE: GMTS\*2.7\*104 Dec 11, 2012 2:04 pm PAGE 1

-----------------------------------------------------------------------------

GMTSMHRF Calculated 7698174

GMTSMHTC Calculated 7727408

GMTSY104 Calculated 9611824

3 Routines checked, 0 failed.

PACKAGE: OR\*3.0\*348 Dec 11, 2012 2:04 pm PAGE 1

-----------------------------------------------------------------------------

ORB3 Calculated 97635419

ORB3SPEC Calculated 93913902

ORBINPTR Calculated 1813250

ORBPRCHK Calculated 32589157

ORY348 Calculated 13557254

5 Routines checked, 0 failed.

> **NOTE:** See the NOTE at the beginning of this manual (page 1). The checksum for routine PXRMP24E will be reflected incorrectly in the patch description, because of a new emergency build. 

If your site already installed the High Risk MH build into your test account, you will see the following after installing the updated build.

Routine Name: PXRMP24E

    Before:       2321342  After:  <span class="mark">B2321909</span>  \*\*24\*\*

If you have not installed the build into your test or production account, you will see the following after installing the updated build.

Routine Name: PXRMP24E

    Before:       n/a   After:  <span class="mark">B2321909</span>  \*\*24\*\*

PACKAGE: PXRM\*2.0\*24 Dec 11, 2012 2:04 pm PAGE 1

-----------------------------------------------------------------------------

PXRM Calculated 37992293

PXRMCDEF Calculated 2284758

PXRMDATE Calculated 69746461

PXRMDEDT Calculated 86390747

PXRMDEV Calculated 78211075

PXRMDUTL Calculated 9494253

PXRMEXFI Calculated 53496841

PXRMEXIC Calculated 80167234

PXRMEXID Calculated 65987316

PXRMEXIU Calculated 66069083

PXRMEXLM Calculated 46743705

PXRMEXPS Calculated 192149462

PXRMEXSI Calculated 40410891

PXRMFF Calculated 65126590

PXRMICHK Calculated 132138736

PXRMLOCF Calculated 95753792

PXRMLPOE Calculated 14864405

PXRMMSER Calculated 106782052

PXRMNTFY Calculated 3662059

<span class="mark">PXRMP24E Calculated 2321342</span>

PXRMPCMM Calculated 11797305

PXRMPDEM Calculated 65842415

PXRMPINF Calculated 8130614

PXRMRDI Calculated 38535019

PXRMSCR Calculated 88295

PXRMTAX Calculated 65791721

PXRMUTIL Calculated 113964494

PXRMVSIT Calculated 10650656

PXRMXQUE Calculated 12328074

29 Routines checked, 0 failed.

## ## Install the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build HIGH RISK MH 2.0 .KID and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: HIGH RISK MH 2.0

Answer "NO" to the following prompt: Want KIDS to INHIBIT LOGONs during install? NO// NO

# NOTE: We recommend that you do not queue the install.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation Example

> See [Appendix A](\l).

## Install File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

> Select Utilities Option: Install File Print

> Select INSTALL NAME: HIGH RISK MH 2.0

## ## Build File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print

> Select BUILD NAME: HIGH RISK MH 2.0

> DEVICE: HOME//

## Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- As part of the post-patch processing, DG\*5.3\*849 installs a new national flag data entry into the PRF NATIONAL FLAG file (#26.15). This data entry is the HIGH RISK FOR SUICIDE national flag. Once it’s been established that the flag has been correctly installed into the file, the post-install routine should be deleted.
- GMTS\*2.7\*104 contains a routine (GMTSY104) that will perform an environment check and update the DESCRIPTION field of the HEALTH SUMMARY COMPONENT file (142.1) entry for MH HIGH RISK PRF HX (post-install). GMTSY104 can be deleted after successful installation.
- TIU\*1.0\*265 consists of one post-install routine that will install the new title into the TIU DOCUMENT DEFINITION file (#8925.1). A message will be written to screen and also captured in the install log as to whether or not the title was successfully created. If a title already exists with the same name, it will be overwritten by the new title.
- The routine TIUPS265 contains the POST-install actions for this patch.

> This routine may be deleted from the system if storage space is a concern. Local IT staff should consider keeping a copy of TIUPS265 as it may prove useful in the event of any unexpected issues with this patch.

- OR\*3.0\*348 contains one post-install routine (ORY348) that will install the new SUICIDE ATTEMPTED/COMPLETED notification and its associated package parameter values as mentioned under the OR\*3.0\*348 section of the Introduction. ORY348 can be deleted after successful installation.
- SD\*5.3\*588 contains one post-install routine (SD53588P) that adds two new parameters to the PARAMETERS (#8989.5) file with associated parameter definitions added to the PARAMETER DEFINITION (#8989.51) file. The new parameter SDMH PROACTIVE DAYS stores a value that will list for future appointments the number of days stored in the parameter, for each patient on the High Risk MH Proactive Adhoc Report and High Risk MH Proactive Nightly Report. This parameter is checked when the SD MH PROACTIVE BGJ REPORT is run. The second new parameter is SDMH NO SHOW DAYS which also stores a value that will list for future appointments the number of days stored in the parameter, for each patient on the SD MH NO SHOW NIGHTLY BGJ Report. The default value of 30 days will be populated by the post-install routine for both parameters. Sites may change the number of days stored in the parameter, within the range of 1 to 30, SD53588P can be deleted after the install.

# Post-Install Set-up Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The person(s) responsible for making the assignment is listed in parentheses after the step.

1.  Assign SPCs to the User Class DGPF PATIENT RECORD FLAGS MGR. *(CAC)*
    1.  To write a PRF note for a category I flag, the user must belong to the DGPF PATIENT RECORD FLAG MGR user class. Each site will be responsible for populating this user class.
    2.  The new HIGH RISK FOR SUICIDE title is in the existing Document Class PATIENT RECORD FLAG CAT I, and the existing business rule applies to that Document Class, so the rule applies to the new title automatically.

Business Rule:

An UNTRANSCRIBED (DOCUMENT CLASS) PATIENT RECORD FLAG CAT I may

BE ENTERED by a DGPF PATIENT RECORD FLAGS MGR

 DESCRIPTION: This rule limits note entry to persons specially trained to

assign and document the assignment of Category I Patient Record Flags.

Sites must not alter, delete, or override this rule. Rule created by patch USR\*1\*24.

Example of USR CLASS MANAGEMENT for current Category I TIU Standard Note Title:

# Select OPTION NAME: USR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# USR BUSINESS RULE MANAGEMENT       Manage Business Rules     action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# USR CLASS DEFINITION       User Class Definition     action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# USR CLASS MANAGEMENT MENU       User Class Management     menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# USR INITIALIZE MEMBERSHIP    Initialize Membership of User Classes action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# USR LIST MEMBERSHIP BY CLASS       List Membership by Class     action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Press \<RETURN\> to see more, '^' to exit this list, OR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# CHOOSE 1-5: 2  USR CLASS DEFINITION     User Class Definition     action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# User Class Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Select User Class Status: ACTIVE//    Active  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Start With Class: FIRST// 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Go To Class: LAST// 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Searching for the User Classes..................................................

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # <u>User Classes                  Oct 30, 2012@09:04:33          Page:    9 of   42</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ACTIVE USER CLASSES                    622 Classes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>+     Class Name                                         Abbrev                </u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DERMATOLOGIST: CLINICAL & LABORATORY                DERM                   

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DERMATOLOGY FELLOW                                  DERM                   

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DERMATOPATHOLOGIST                                  DERMP                  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DETECTIVE                                           DET                    

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DEVELOPER                                           DEV                    

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <span class="mark">126  DGPF PATIENT RECORD FLAGS MGR</span>                       PRFM                   

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DIABETES STUDY NURSE                                DSRN                   

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DIALYSIS TECHNICIAN                                 DIALTEC                

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DIETETIC INTERN                                     DI                     

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DIETETIC TECHNICIAN STUDENT                         DTS                    

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# +         + Next Screen  - Prev Screen  ?? More Actions                         

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Find                      Expand/Collapse Class     Change View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Create a Class            List Members              Quit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Edit User Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select Action: Next Screen// 126     

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Listing Members of \#126

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # <u>User Class Members            Oct 30, 2012@09:05:11          Page:    1 of    1</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DGPF PATIENT RECORD FLAGS MGRs                5 Members

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>     Member                                                 Effective  Expires </u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# MHPROVIDER,THREE                                                       

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# MHPROVIDER,TWELVE 10/18/11            

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# MHPROVIDER,TEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# MHPROVIDER,TWO 10/18/11            

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# WHPROVIDER,THIRTEEN                                                        

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# (?SBPN) missing SIGNATURE BLOCK PRINTED NAME                       \>\>\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Add                       Remove                    Change View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Edit                      Schedule Changes          Quit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select Action: Quit// AD   Add  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select MEMBER: MHCOORDINATOR, TWO       TM          CAC MD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# MEMBER: MHCOORDINATOR, TWO       // 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# EFFECTIVE DATE: NOW  (OCT 30, 2012)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# EXPIRATION DATE: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Assign Mental Health Treatment Coordinators in the Patient Care Management Module (PCMM). See the [PCMM MHTC User Manual](http://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/pcmmmhtcug.pdf) for instructions. *(MH PCMM Coordinator)*
2.  Assign MHTCs to appropriate patients. See the PCMM MHTC User Manual for an example. *(MH PCMM Coordinator*). A new reminder called VA-MHTC NEEDS ASSIGNMENT can help Mental Health staff identify patients that need an MHTC to be assigned.
3.  Attach the new DGPF LOCAL TO NATIONAL CONVERT option to the appropriate menu for the Suicide Prevention Coordinator (and/or Mental Health designee). This should be the SPC or MH designee that will be running the report-only and processing steps in the DGPF LOCAL TO NATIONAL CONVERT option.  When the Process Local to National step is run, all new automatically created Category I HIGH RISK FOR SUICIDE PRFs will include this individual’s name in each patient’s PRF activity narrative. It is better to use a Mental Health person. *(IRM)*
4.  Attach the existing DGPF TRANSMISSION MGMT option to the appropriate menu for the Suicide Prevention Coordinator (or designee) to track HIGH RISK FOR SUICIDE assignments that could not be updated at one of the patient’s other Treating Facilities. *(IRM)*
5.  Add Suicide Prevention Coordinators names to the DGPF CLINICAL HR FLAG REVIEW Mail group. *(Mail group owner)*

> The Mail Group Owner of the DGPF CLINICAL HR FLAG REVIEW Mail Group (as entered during the installation process) will need to add these names after the multi-package build is installed. The Mail Group members added to this Mail Group will receive the reports in a MailMan Message. This can include all facility SPCs if you’re an integrated site.

> NOTE: The DGPF CLINICAL HR FLAG REVIEW Mail Group is not used to document PRF Transmission Errors. It is also used to let Mail Group members know the patient’s PRF is due for a review.

> Example:

> \>D ^XUP

> Setting up programmer environment

> This is a TEST account.

> Select OPTION NAME: XMMGR

> Manage Mailman menu

> Check MailMan Files for Errors

> Create a Mailbox for a user

> Disk Space Management ...

> Group/Distribution Management ...

> Local Delivery Management ...

> MailMan Site Parameters

> Network Management ...

> New Features for Managing MailMan

> Select Manage Mailman Option: Group/Distribution Management ... \[XMMGR-GROUP-MAINTENANCE\]

> Select Group/Distribution Management Option: Mail Group Coordinator's Edit \[XMMGR-MAIL-GRP-COORDINATOR\]

> This option allows a mail group coordinator to edit the mail groups that

> he or she is the coordinator of (and no others). It does not allow edit

> of remote recipients.

> Select MAIL GROUP NAME: DGPF CLINICAL HR FLAG REVIEW

> Select MEMBER: MHUSER,TWO

> Are you adding 'MHUSER,TWO' as a new MEMBER (the 1ST for this MAIL GROUP)? No// YES

> Select MEMBER: MHUSER,THREE

6.  Select the Convert Local HRMH PRF to National option. Select Report Only. The actual conversion (P option) should only be run after notification from the national Office of Mental Health Services (30 days after the package release), to minimize transmission error messages among sites with shared patients. These errors occur when one of these sites has installed and runs the conversion, but another site that sees the same patient hasn’t installed the software. *(SPC)*

> When run in the report mode, reports will be generated and sent via MailMan to the new DGPF CLINICAL HR FLAG REVIEW mail group, showing which local PRFs can be processed, which ones may have potential errors needing to be corrected first, and which ones may need to be processed manually.

> Select OPTION NAME: DGPF LOCAL TO NATIONAL CONVERT Convert Local HRMH PRF to National action

> Convert Local HRMH PRF to National

> This option can be run in a report only mode which will provide a report

> of what actions the local-to-national processing will perform. Enter 'R'

> to run the Report Only mode, or 'P' to begin the local-to-national PRF

> processing.

> Select one of the following:

> R Report Only

> P Process Local-to-National

> Select which mode to run: R//Report Only

> ...SORRY, JUST A MOMENT PLEASE...

> \>\> Results have been sent to the 'DGPF CLINICAL HR FLAG' mail group

> Subj: Pre-report National Flag Create 8/1/12@15:42 \[#64240\] 08/01/12@15:42

> 44 lines

> From: HRMH PRF GENERATE JOB In 'IN' basket. Page 1 Priority!

> -----------------------------------------------------------------------------

> Pre-scan summary from Local to National flag processing job

> Run date: Aug 01, 2012@15:42:06

> Started by: MHPROVIDER,SIX

> -----------------------------------------------------------------------------

> Summary of PRF Processing:

> Total active Cat II flag assignments: 12

> Cat I flags created: 5

> Potential errors Found: 5

> Cat II flags requiring manual action: 0

> Found active Cat I and Cat II flags: 2

> =============================================================================

> Processing Results:

> Invalid DFN's or Patient File errors

> -----------------------------------------------------------------------------

> No DFN errors were found

> Patients with Local ICN (National ICN Required)

> Name Local ICN

> -----------------------------------------------------------------------------

> AWHPATIENT,FEMALEFIFTEEN (0015) 6600000145V816164

> CRPATIENT,ONE (2222) 6600000120V652113

> MHPATIENT,TWO (0011) 6600000105V932329

> National Flag assigned and Local still active

> Name CMOR Owning Site

> -----------------------------------------------------------------------------

> CRPATIENT,TWO (4444) SALT LAKE CITY OIFO SALT LAKE CITY HCS

> Patients flagged for manual processing

> Name CMOR Description

> -----------------------------------------------------------------------------

> No records needing manual intervention found

> Other Errors which may have prevented conversion

> Name Description

> -----------------------------------------------------------------------------

> No other errors found

7.  Allocate the DGPF TRANSMISSIONS key to SPCs on your VistA system. At a minimum, it should be provided to the same SPC who runs the convert option. The SPCs will be using this key for access to the DGPF TRANSMISSION MGMT menu option. *(IRM)*

DGPF TRANSMISSIONS key description

> NAME: DGPF TRANSMISSIONS

>   DESCRIPTIVE NAME: Patient Record Flag Trans

> DESCRIPTION:   This key should only be given to those individuals who may

> perform patient record flag functions related to the sharing/transmission of

> Category I PRF assignments with other treating facilities.  These functions

> include the following:

>   - Transmission error processing. 

>   - Retransmission of patient assignments. 

>   - Transmission of a query to a selected treating facility. 

8.  Add the DGPF TRANSMISSION MGMT menu option to the same users as above. (This option will only be assigned to a few staff at your site – it should be provided to the same SPC who runs the convert option). The Record Flag Transmission Errors option on this menu will be used by sites that have multi-treating facilities and will be sharing Category I PRF assignment information. *(IRM)*Record Flag Transmission Errors option description

> DGPF TRANSMISSION MGMT     Record Flag Transmission Mgmt     menu

>    TE     Record Flag Transmission Errors

> DESCRIPTION:   This option provides a List Manager user interface that can be

> used to review and manage Rejected Status ("RJ") HL7 transmission messages

> that are received from Treating Facilities of the patient when trying to share Category I PRF Assignment information.  The following actions are provided

> within this option. 

>   - Sort List display by patient name alphabetically or date/time received

>   - View Message details of the patient's rejected HL7 message record

>   - Retransmit all of the patient's PRF Assignment and History records to

>     the site that the rejection message occurred at.

>    MQ     Record Flag Manual Query

9.  Add users to the DGPF HL7 TRANSMISSION ERRORS Mail Group. These should be the same users who were given the DGPF Transmissions Security Key and access to the DGPF Transmission MGMT option. Recipients will receive any error messages generated by the local-to-national PRF processing. Messages sent to the user will need to be checked for the reject reason of “Record Flag is already assigned to patient,” so that they can coordinate with the other site that is also owner of the Cat I HIGH RISK FOR SUICIDE record.

> CHOOSE 1-5: 4  DGPF HL7 TRANSMISSION ERRORS

> MAIL GROUP NAME: DGPF HL7 TRANSMISSION ERRORS  Replace

> Select MEMBER: MHUSER, ONE

>   MEMBER: MHUSER, ONE // \<Enter\>

>   TYPE:

> Select MEMBER:

> DESCRIPTION:

> This mail group is used to notify Patient Record Flag administrators of

> transmission errors that occur during the processing of HL7 messages.

> Scenarios that can cause the transmission errors:

> 1\) Assigning the new Category I HIGH RISK FOR SUICIDE flag to a patient BEFORE all sites have installed the patch bundle, or

> 2\) Running the Convert option BEFORE all sites have installed the patch bundle.

> In either case, the PRF assignments will not be lost to the other sites because the assignment is waiting to be re-transmitted to sites.

> For example, if site A runs the convert process step prior to others installing the software, each Category II flag for suicide risk will be converted to the Category I flag on the Site A system using the review date and ownership facility from the source Category II flag. For each Category I created, the patient’s treating facilities of record will be sent an update using the existing PRF Transmission management system where normal protocol can be used to resolve issues between sites.

> If site B does not have the bundle installed, then site A receives a transmission error back in the PRF transmission management option that informs the SPC that the Category I flag could not be updated at the site.

> The SPC will coordinate with Site B so that when Site B completes its install, the SPC at Site A could manually reprocess the transmission to Site B. which would update Site B with the Category I.

> If site B had the Category II PRF active, it would remain active until the site B SPC runs the conversion on the site B system.

> Waiting the 30 days relieves the SPCs of having to coordinate with each unique patient/ site combination that receives a transmission error.

10. The HIGH RISK FOR SUICIDE national flag uses a new Text Integration Utility (TIU) Progress Note (PN) title that is installed by patch TIU\*1.0\*265; Patient Record Flag CATEGORY I - HIGH RISK FOR SUICIDE.  If, for some reason, this Progress Note Title is not available, the HIGH RISK FOR SUICIDE national flag will not be installed. In this case, you will need to manually install it, by running the post-install routine from the programmer prompt (\>D EN^DG53849P).
11. If your site is using the Reminder dialog template, SUICIDE HIGH RISK PRF DOCUMENTATION, make the following changes:
    1.  Change Category II to Category I.
    2.  The CACs will need to temporarily assign themselves the ASU User class of DGPF PATIENT RECORD FLAGS MGR. This user class allows the CAC to see the Patient Record Flag Category I –High Risk for Suicide title and attach the reminder dialog if desired.

> It is not required to use health factors with the Category I PRF—the national PRF data is extractable.  However, if you want to link the existing template that captures health factors to the new TIU note title, you can do this.

12. Enable the new informational notification released with this patch, SUICIDE ATTEMPTED/ COMPLETED, which is triggered by Clinical Reminders when an MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in PCE. IRM will need to enable this at the System level.
    1.  Assign SPC users as recipients to this notification. Note: MHTC should already be set up as a default recipient type for Suicide Attempted/Completed.
    2.  Add ‘C’ (MHTC) to the default recipient list for other notification types (Admission, Discharge, …) as deemed necessary.
    3.  Other Notification Types enabled on your system that are identified as appropriate to notify the patient’s assigned MHTC. (e.g., Admission, Discharge, ….) will need to be manually defined as needed.

> NOTE: An ORB PROVIDER RECIPIENT parameter value of “CM” is exported with the Suicide behavior notification. Therefore, the suicide behavior notification will be sent to the MHTC and PCMM Mental Health team if any are set up and configured at the site. Directions on how to set those up should be contained in a setup manual created by the sister project, Principal Mental Health Provider. See the Primary Care Management Module (PCMM) – Mental Health Treatment Coordinator (MHTC) User Manual (pcmmmhtcug.pdf) for more information.

Set of codes indicating default provider recipients of a notification by their title or relationship to the patient. 

> Notifications can be set up with any or all of the following codes:

   P (Primary Provider): deliver notification to the patient's Primary Provider. 

   A (Attending Physician): deliver notification to the patient's Attending Physician.

   T (Patient Care Team): deliver notification to the patient's OE/RR Teams (personal patient and team lists are evaluated for potential recipients) and to devices on an OE/RR team).

   O (Ordering Provider): deliver notification to the provider who placed the order which trigger the notification.

   M (PCMM Team): deliver notification to users/providers linked to the patient via PCMM Team Position assignments.

   E (Entering User): deliver notification to the user/provider who entered the order's most recent activity.

   R (PCMM Primary Care Practitioner): deliver notification to the patient's PCMM Primary Care Practitioner.

   S (PCMM Associate Provider): deliver notification to the patient's PCMM Associate Provider.

   C (PCMM Mental Health Treatment Coordinator): deliver notification to the patient's PCMM Mental Health Treatment Coordinator.
4.  Once all the set-up is done, you can verify this via the following menu:

> Notification Mgmt Menu     menu

>    1      Enable/Disable Notifications

>    2      Erase Notifications

>    3      Set Urgency for Notifications (GUI)

>    4      Set Deletion Parameters for Notifications

>    5      Set Default Recipient(s) for Notifications

>    6      Set Default Recipient Device(s) for Notifications

>    7      Set Provider Recipients for Notifications

>    8      Flag Orderable Item(s) to Send Notifications

>    9      Archive(delete) after \<x\> Days

>    10     Forward Notifications ...

>    11     Set Delays for Unverified Orders ...

>    13     Send Flagged Orders Bulletin

>    14     Determine Recipients for a Notification

>    15     Display Patient Alerts and Alert Recipients

>    16     Enable or Disable Notification System

>    17     Display the Notifications a User Can Receive

> Select Notification Mgmt Menu Option: 14  Determine Recipients for a Notification

> PATIENT (req'd): MHPATIENT,ONE        5-5-55    555121255   

>  YES     SC VETERAN      

>  Enrollment Priority: GROUP 1    Category: IN PROCESS    End Date:

> NOTIFICATION (req'd): SUICIDE ATTEMPTED/COMPLETED 

> Processing, please stand by...

> DEVICE: HOME// ;;9999  HOME

>                     DETERMINE NOTIFICATION RECIPIENTS REPORT          Page:   1

> Processing notification: SUICIDE ATTEMPTED/COMPLETED

>             for patient: MHPATIENT,ONE

> Default recipient users and teams:

>    SBCUSER,ONE: ON because

>      Default Recipient (USER) parameter set to Yes.

>    SBCUSER,TWO: ON because

>      Default Recipient (USER) parameter set to Yes.

> Recipients determined by Provider Recipient parameter:

> PCMM Team Position Assignments:

> PCMM Mental Health Treatment Coordinator:

>    MHTCUSER,ONE: ON because

>      User MHTCUSER,ONE is Enabled.

>            - End of Report -

13. Check the DG Parameter Definition setup for the PRF FOR SUCIDE PREVENTION. If your site has a different name for this PRF, you’ll need to go into the Parameter Tools option (XPAR MENU TOOLS) to change this. NOTE: You may need programmer access to use this option, depending on how your site has assigned menus and options.

> LV List Values for a Selected Parameter

> LE List Values for a Selected Entity

> LP List Values for a Selected Package

> LT List Values for a Selected Template

> EP Edit Parameter Values

> ET Edit Parameter Values with Template

> EK Edit Parameter Definition Keyword

> Select General Parameter Tools Option: EP Edit Parameter Values

> --- Edit Parameter Values ---

> Select PARAMETER DEFINITION NAME: PRF FOR SUICIDE PREVENTION DGPF SUICIDE FLAG

> PRF for Suicide Prevention

> ------------ Setting DGPF SUICIDE FLAG for Package: REGISTRATION ------------

> Value: HIGH RISK FOR SUICIDE Replace

15. If desired, change the number of days for future appointments that will appear on the SD MH NO SHOW NIGHTLY BGJ Report and the SD MH PROACTIVE BGJ REPORT.

    These can be changed in the new parameters SDMH PROACTIVE DAYS and SDMH NO SHOW DAYS. The default value is 30 days for both parameters. The SD NO SHOW NOTIFICATION mail group that was installed with the previous patch SD\*5.3\*578 will receive the SD MH PROACTIVE BGJ REPORT.

> *Example:*

> Select General Parameter Tools Option: EP Edit Parameter Values

> --- Edit Parameter Values ---

> Select PARAMETER DEFINITION NAME: SDMH PROACTIVE DAYS Proactive Report Future Days Displayed

> ------------ Setting SDMH PROACTIVE DAYS for Package: SCHEDULING ------------

> 30: 30// ??

> Enter the number of days from 1 to 30 to list future appointments for on

> the nightly Proactive Report.

> 30: 30// 15

> --------------------------------------------------------------------------

> Select PARAMETER DEFINITION NAME: SDMH NO SHOW DAYS No Show Report Future Days Displayed

> ------------- Setting SDMH NO SHOW DAYS for Package: SCHEDULING -------------

> 30: 30// 10

> -------------------------------------------------------------------------------

> Select PARAMETER DEFINITION NAME: \<Enter\>

16. IRM staff will need to attach the High Risk MH Proactive Adhoc Report \[SD MH PROACTIVE AD HOC REPORT\] and High Risk MH Proactive Nightly Report \[SD MH PROACTIVE BGJ REPORT\] menu options to an appropriate menu for the Suicide Prevention Coordinator, or to a menu at the local suicide prevention staff’s discretion.
17. Use the same name entered in the Parameter Definition to complete an update to the reminder term. For the reminder definition VA-MH HIGH RISK NO-SHOW FOLLOW-UP, the term VA-MH HIGH RISK FOR SUICIDE PRF needs to be reviewed, and if the local Suicide flag name is not HIGH RISK FOR SUICIDE, the term needs to be updated to the local name.

>   ---- Begin: VA-MH HIGH RISK FOR SUICIDE PRF (FI(2)=RT(811)) --------------

>                   Finding Type: REMINDER TERM

>    Use in Patient Cohort Logic: AND

>            Beginning Date/Time: FIEVAL(1,1,"DATE")

>               Ending Date/Time: FIEVAL(1,1,"DATE")+1D

>               Occurrence Count: 2

> REMINDER DEFINITION INQUIRY                     Jul 19, 2012 7:56:47 am  Page 5

> -------------------------------------------------------------------------------

>                     Mapped Findings: CF.VA-PATIENT RECORD FLAG         

>                                      INFORMATION                       

>          Computed Finding Parameter: HIGH RISK FOR SUICIDE^L

>                     Mapped Findings: CF.VA-PATIENT RECORD FLAG         

>                                      INFORMATION                       

>          Computed Finding Parameter: HIGH RISK FOR SUICIDE^N

>   ---- End: VA-MH HIGH RISK FOR SUICIDE PRF --------------------------------

18. Set up a Reminders Due report template for SPCs.

> A new reminder called VA-MHTC NEEDS ASSIGNMENT is available that can be used from CPRS to evaluate and display on the Cover Sheet’s Reminders Due section when the patient is a candidate for MHTC assignment. In order to be an MHTC candidate, the patient must have had three completed MH appointments within the past year, and not have an MHTC assigned to the patient.

- The reminder definition uses the new VA-PCMM MHTC computed finding.
- There is no reminder dialog related to this reminder.
- Uses Reminder Term VA-MH APPTS FOR MHTC ASSIGNMENT, which uses a new Reminder Location List called VA-MHTC APPT STOP CODES LL in the Computed Finding VA-Appointments for a Patient. 
- The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services.
- This reminder can also be used from Reminder Reporting options/Reminders Due Report. Reminder CACs can create a Reminders Due Report (User) template for an SPC user to get the list of patients who are scheduled for a MH appointment next week and are candidates for MHTC. MHTCs, SPCs, or other MH Professionals should work with their Reminders Manager or Reminders CAC to set up the Reminders Due report criteria in a template, based on report criteria for SPC users. The report criteria should specify facility (or facilities), stop codes (e.g., 502) or hospital locations (selected Mental Health locations), future appointments or completed visits, and the VA-MHTC NEEDS ASSIGNMENT reminder.
19. Ensure that the new health summary types have been added to the CPRS Reports tab display. (This should’ve been done as part of the installation and setup of Phase 1 of the HRMHP project, which was released in March 2012.) 

> Follow your facility’s rules and conventions for adding these health summary types.

1.  VA-MH HIGH RISK PATIENT - This Type contains the four Health Summary Components mentioned above, and is the basis for creating the VA-MH HIGH RISK PATIENT (TIU) Health Summary Object.
2.  REMOTE MH HIGH RISK PATIENT - This Type contains the same components as the VA-MH HIGH RISK PATIENT and allows viewing the aforementioned information from remote sites.

> Sequencing new Health Summary types is done in the GUI Parameters option.

> Example: Sequencing new Health Summary types in Parameters option

> Select CPRS Manager Menu Option: PE  CPRS Configuration (Clin Coord)

> Select CPRS Configuration (Clin Coord) Option: GP GUI Parameters

> Select GUI Parameters Option: HS  GUI Health Summary Types

> Allowable Health Summary Types may be set for the following:

>      2   User          USR    \[choose from NEW PERSON\]

>      3   Division      DIV    \[choose from INSTITUTION\]

>      4   System        SYS    \[TEST.FO-SLC.MED.VA.GOV\]

>      5   Service       SVC    \[choose from SERVICE/SECTION\]

> Enter selection: 4  System   xxx.MED.VA.GOV

> \- Setting Allowable Health Summary Types  for System: PUGET-SOUND.MED.VA.GOV -

> Sequence: 20//

> Health Summary: VA-HIGH RISK MH PATIENT

> Sequence: 21//                (your sequence numbers will be different)

> Health Summary: REMOTE MH HIGH RISK PATIENT

20. When notified by the Office of Mental Health Services, run the Convert Local HRMHP PRF to National option - Process mode.

> When the Convert Local HRMHP PRF to National option is run in the processing mode, the actual processing and auto-creation of the national PRFs from the local PRFs will take place and messages will be sent out to summarize the process results. The local PRF for the patient will be inactivated. Note: Category I PRFs that are auto-created from this option will not have a Progress Note related to them.

> The Process Mode can be re-run as needed if a patient had an error that is resolved. Each time the process mode is run the active local PRFs that are found will be processed.

> Select OPTION NAME: DGPF LOCAL TO NATIONAL CONVERT Convert Local HRMH PRF to National action

> This option can be run in a report only mode which will provide a report

> of what actions the local-to-national processing will perform. Enter 'R'

> to run the Report Only mode, or 'P' to begin the local-to-national PRF

> processing.

> Select one of the following:

> R Report Only

> P Process Local-to-National

> Select which mode to run: R// P Process Local-to-National

> ...SORRY, JUST A MOMENT PLEASE...

> \>\> Results have been sent to the 'DGPF CLINICAL HR FLAG' mail group

> The process to generate the new national (category I) PRFs from the local (category II) PRFs consists of determining whether a national PRF can be created from existing, active, local PRFs for suicide prevention.

> Basic requirements of auto-creating national PRF entries

> Local flag MUST BE currently active

> Local flag information will be pulled into the new National flag at creation.

> Various comments are updated to reflect auto-created information.

> If there is an issue with generating a National flag:

> No National flag is created

> Local flag remains intact

> Error report will be generated

If there is any issue with generating a national PRF, either an error message will be logged, or the record will be reported as needing manual action by the suicide prevention coordinator (SPC).

If a new national PRF can be created, the information from the local PRF will be used in creating the new national PRF with a generated activity narrative using the name of the SPC running the process mode..

This national PRF entry was auto-created on \<DT\>, by the 'Convert Local HRMH PRF to National' option, run by \<USER\>. The fields are based on the local PRF \<FLAG\> which was inactivated by the auto conversion.

Upon successful creation of the new national PRF, the local PRF will be inactivated with a comment indicating that a new national PRF has been created and the existing HL7 messaging functionality will be used to transmit the national PRF information to other known treating facilities, as is currently done when a National PRF is entered through the Patient Record Flag assignment menu.

See the PRF User Manual for more information about the Patient Record Flag options and the PRF Transmission key (DGPF TRANSMISSIONS KEY).

Ownership of Category I flag determined at assignment and when Process Mode is run:

The first site that runs the Process mode that creates a Category I flag for a particular patient becomes the Owning site for that Category I flag. Each Category I flag assignment to a specific patient’s record is owned by a single facility. The facility that placed the Category I flag on the patient’s record would normally own and maintain the flag. The site that owns the Category I flag is the only site that can:

- Review whether to remove or continue the flag
- Edit the flag
- Inactivate the flag
- Reactivate the flag
- Mark the flag as entered in error
- Change ownership of the flag
- Enter a Patient Record Flag Category I progress note for the flag

However, ownership of a Category I flag assignment can be transferred. If a patient received the majority of care at a different VA facility than the one that assigned the flag, the site giving the majority of care could request that ownership of the flag be transferred to that site. The owning site could then change the ownership to the second site through the PRF software in List Manager.

Example of a transmission error logged at the site that originated the Category I flag (“owner” site) for a patient

In this example, a transmission error was created when the first site processed the auto-created flag but one of the patient’s treating facility sites had not installed the patch bundle. The “Assignment Transmitted To” will be the site that could not be updated because the Category I flag has not been installed on the VistA system at the transmitted to site.

> <u>TRANSMISSION ERROR DETAILS    Jul 30, 2012@14:02:35          Page:</u>

> Patient: ZZTEST,VADOD FOR (000009242)                DOB: 09/11/59

>     ICN: 1017279300V523655

> <u>                                                                  </u>

>          Error Received D/T: 07/30/12@13:58:19                    

>          Message Control ID: 612453468834                         

>                   Flag Name: HIGH RISK FOR SUICIDE                

>                  Owner Site: MARTINEZ OPC/CREC                    

>   Assignment Transmitted To: NORTHPORT VAMC                       

> Assignment Transmission D/T: 07/30/12@13:58:15                    

> Rejection Reason(s):                                              

> --------------------                                              

> 1\. Record flag is invalid                                         

In this case, the Category I flag did not update at the Transmitted To site. The only site that knows about the issue via the transmission error is the site that ran the Process Mode. The Transmitted To site does not receive an error message.

The DGPF Transmission Management options should be visited regularly by SPCs to guide them on which sites need manual transmission of a patient’s Category I flag to update another site, and which site needs to be coordinated with to determine ownership of the Category I flag.

# Back-Out Plan for Production Environment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HRMHP project, Phase II, contains a bundle with six VistA patches: DG\*5.3\*849, SD\*5.3\*588, TIU\*1.0\*265, PXRM\*2.0\*24, GMTS\*2.7\*104, and OR\*3\*348.

Sites are encouraged to create a back-up of all routines as a KIDS pre-install step when installing the Phase II bundle. This back-up of routines will cover restoration of routines from all packages if a back-out is necessary.

> **NOTE:** The efficiency of the Back-Out Plan diminishes over time. At some point the VistA recovery process will need to be implemented.

File content changes in these builds:

- DG\*5.3\*849: Adds a new Category I Patient Record Flag, HIGH RISK FOR SUICIDE.
- Also adds a new conversion option that one or two people will be accessing on local systems. The options can be removed from these users’ option menus if a back-out is needed.

> The PRF conversion process must be manually initiated from the new option. It will not be initiated when the bundle is installed, which puts each site in control of when the new conversion options are run. If the conversion option is run before a back-out becomes necessary, the Patient Record Flag (PRF) conversion process is not reversible, but a local Category II High Risk for Suicide PRF flag that was de-activated for a patient can be manually reactivated with the Local Category II flag, and the national Category I HIGH RISK FOR SUICIDE PRF can be de-activated for a patient.

- SD\*5.3\*588: Adds new SD options to help proactively follow-up with patients before the MH appointment occurs. These options can be removed from SPC/MH Professional users’ menus. A new nightly protocol is added that is run by the SD Background Job protocol event. The nightly protocol can be removed from the SD Background Job’s protocol event if a back-out is needed.
- TIU\*1.0\*265: Updates a national note title. The existence of the new entry in the TIU file will not cause a problem if a back-out is necessary.
- PXRM\*2.0\*24: Updates an existing reminder and dialog and adds new one. The HRMHP Phase I released bundle contains post-install Reminder Exchange entries that can be used to install over the existing reminder and dialog if a back-out is needed. The new reminder can be removed from all cover sheet reminder parameter lists if a back-out is needed.
- GMTS\*2.7\*104: Updates the description for a health summary component, to reflect the local Cat II and national Cat I PRF history that is displayed for High Risk for Suicide. No back-out required.
- OR\*3\*348: Updates a provider recipient parameter to include a new provider recipient (MHTC) for notification parameter setup. Adds a new notification type that is distributed with a disabled status, with instructions to enable in the post install. If a back-out is needed, the notification type can be disabled, and all notification types that have default provider recipients that include “C” should remove the “C” from the default provider recipients.

See patch descriptions for exact names of file content changed. Reverse the post-install steps described in the install and set-up instructions, to remove access to new Options, Mail Groups, the Security Key, and Clinical Reminders.

Other than the steps outlined above for back-out, any additional back-out coding is not feasible and could cause more issues that it resolves. Back-out restoration from selective de-journaling is not possible. De-journaling from backups would negatively impact other applications and their valid data.

The HRMHP development staff is available to support sites with the back-out steps above, if needed.

# Appendix A: Installation Examples 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # First-Time Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # NOTE: We recommend that you not queue the install.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select Installation \<TEST ACCOUNT\> Option: Load a Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Host File: USER\$:\[ANONYMOUS\]HIGH_RISK_MH_2_0_T9.KID

KIDS Distribution saved on Dec 07, 2012@10:16:34

Comment: High Risk Mental Health phase 2

This Distribution contains Transport Globals for the following Package(s):

HIGH RISK MH 2.0

TIU\*1.0\*265

DG\*5.3\*849

SD\*5.3\*588

GMTS\*2.7\*104

OR\*3.0\*348

PXRM\*2.0\*24

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

HIGH RISK MH 2.0

TIU\*1.0\*265

DG\*5.3\*849

SD\*5.3\*588

Build GMTS\*2.7\*104 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES//

GMTS\*2.7\*104

Will first run the Environment Check Routine, GMTSY104

CHECKING RECENT ADDITIONS TO HEALTH SUMMARY COMPONENT FILE

Medication Worksheet (Tool \#2): OK

MAS CONTACTS: OK

MAS MH CLINIC VISITS FUTURE: OK

MH HIGH RISK PRF HX: OK

MH TREATMENT COORDINATOR: OK

OR\*3.0\*348

PXRM\*2.0\*24

Use INSTALL NAME: HIGH RISK MH 2.0 to install this Distribution.

Select Installation \<TEST ACCOUNT\> Option: BACKup a Transport Global

Select INSTALL NAME: HIGH RISK MH 2.0 2/25/13@14:36:41

=\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

This Distribution was loaded on Feb 25, 2013@14:36:41 with header of

High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

It consisted of the following Install(s):

HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

OR\*3.0\*348 PXRM\*2.0\*24

Subject: Backup of HIGH RISK MH 2.0 install on Feb 25, 2013

Replace

Loading Routines for HIGH RISK MH 2.0.

Routine PXRMP24I is not on the disk..

Loading Routines for TIU\*1.0\*265.

Routine TIUPS265 is not on the disk..

Loading Routines for DG\*5.3\*849

Routine DG53849P is not on the disk..

Routine DGPFCNR is not on the disk..

Routine DGPFCNV is not on the disk..

Loading Routines for SD\*5.3\*588

Routine SD53588P is not on the disk.....

Routine SDMHAP is not on the disk..

Routine SDMHAP1 is not on the disk....

Routine SDMHPRO is not on the disk..

Routine SDMHPRO1 is not on the disk..

Loading Routines for GMTS\*2.7\*104...

Loading Routines for OR\*3.0\*348..

Routine ORBINPTR is not on the disk...

Routine ORY348 is not on the disk..

Loading Routines for PXRM\*2.0\*24.....

Routine PXRMDUTL is not on the disk..............

Routine PXRMNTFY is not on the disk..

Routine PXRMP24E is not on the disk..

Routine PXRMP24I is not on the disk......

Routine PXRMSCR is not on the disk......

Send mail to: CRUSER, SIX// CRUSER, SIX

Select basket to send to: IN// PATCH TEST

And Send to:

Select Installation \<TEST ACCOUNT\> Option: COMPARE Transport Global to Current System

Select INSTALL NAME: HIGH RISK MH 2.0 2/25/13@14:36:41

=\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

This Distribution was loaded on Feb 25, 2013@14:36:41 with header of

High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

It consisted of the following Install(s):

HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

OR\*3.0\*348 PXRM\*2.0\*24

Select one of the following:

1 Full Comparison

2 Second line of Routines only

3 Routines only

4 Old style Routine compare

Type of Compare: 1 Full Comparison

DEVICE: HOME// P

1 P-LAB-MESSAGE-HFS HFS FILE

2 P-MESSAGE-HFS (VXD) HFS FILE =\> MESSAGE

3 P-RESMON IRM

4 PACS1\$PRT COMPRESSED RADIOLOGY

5 PACS1\$PRT LANDSCAPE RADIOLOGY

6 PACS1\$PRT STANDARD RADIOLOGY

7 PACS2\$PRT COMPRESSED A208E

8 PACS2\$PRT STANDARD A208E

9 PBOWES BRWCALL BRW MAIL ROOM

10 PBOWES BRWPREAPPT BRW MAIL ROOM

Type '^' to Stop, or

Choose 1-10\> 2 P-MESSAGE-HFS (VXD) HFS FILE =\> MESSAGE

Subject: HIGH RISK MH 2.0 COMPARE

Select one of the following:

M Me

P Postmaster

From whom: Me//

Send mail to: CRUSER, SIX // CRUSER, SIX

Select basket to send to: IN// PATCH TEST

And Send to:

Moving to MailMan message...

.............................................................................

.............................................................................

....................

Finished moving.

Sending \[8150\]...

Sent

Select Installation \<TEST ACCOUNT\> Option: VERify Checksums in Transport Global

Select INSTALL NAME: HIGH RISK MH 2.0 2/25/13@14:36:41

=\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

This Distribution was loaded on Feb 25, 2013@14:36:41 with header of

High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

It consisted of the following Install(s):

HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

OR\*3.0\*348 PXRM\*2.0\*24

Want each Routine Listed with Checksums: Yes// YES

DEVICE: HOME// SSH

PACKAGE: HIGH RISK MH 2.0 Feb 25, 2013 2:38 pm PAGE 1

--------------------------------------------------------------------------

GMTSY104 Calculated 9611824

PXRMP24I Calculated 14301202

2 Routines checked, 0 failed.

PACKAGE: TIU\*1.0\*265 Feb 25, 2013 2:38 pm PAGE 1

--------------------------------------------------------------------------

TIULO1 Calculated 21084404

TIUPS265 Calculated 9608303

2 Routines checked, 0 failed.

PACKAGE: DG\*5.3\*849 Feb 25, 2013 2:38 pm PAGE 1

--------------------------------------------------------------------------

DG53849P Calculated 7093789

DGPFCNR Calculated 62901548

DGPFCNV Calculated 95099109

3 Routines checked, 0 failed.

PACKAGE: SD\*5.3\*588 Feb 25, 2013 2:38 pm PAGE

--------------------------------------------------------------------------

SD53588P Calculated 6953359

SDAMQ Calculated 9860749

SDMHAD Calculated 116008938

SDMHAD1 Calculated 108729141

SDMHAP Calculated 89393379

SDMHAP1 Calculated 16336515

SDMHNS Calculated 22141437

SDMHNS1 Calculated 101585316

SDMHPRO Calculated 15994772

SDMHPRO1 Calculated 19699190

10 Routines checked, 0 failed.

PACKAGE: GMTS\*2.7\*104 Feb 25, 2013 2:38 pm PAGE 1

--------------------------------------------------------------------------

GMTSMHRF Calculated 7698174

GMTSMHTC Calculated 7727408

GMTSY104 Calculated 9611824

3 Routines checked, 0 failed.

PACKAGE: OR\*3.0\*348 Feb 25, 2013 2:38 pm PAGE 1

--------------------------------------------------------------------------

ORB3 Calculated 97635419

ORB3SPEC Calculated 93913902

ORBINPTR Calculated 1813250

ORBPRCHK Calculated 32589157

ORY348 Calculated 13557254

5 Routines checked, 0 failed.

PACKAGE: PXRM\*2.0\*24 Feb 25, 2013 2:38 pm PAGE 1

--------------------------------------------------------------------------

PXRM Calculated 37992293

PXRMCDEF Calculated 2284758

PXRMDATE Calculated 69746461

PXRMDEDT Calculated 86390747

PXRMDEV Calculated 78211075

PXRMDUTL Calculated 9494253

PXRMEXFI Calculated 53496841

PXRMEXIC Calculated 80167234

PXRMEXID Calculated 65987316

PXRMEXIU Calculated 66069083

PXRMEXLM Calculated 46743705

PXRMEXPS Calculated 192149462

PXRMEXSI Calculated 40410891

PXRMFF Calculated 65126590

PXRMICHK Calculated 132138736

PXRMLOCF Calculated 95753792

PXRMLPOE Calculated 14864405

PXRMMSER Calculated 106782052

PXRMNTFY Calculated 3662059

PXRMP24E Calculated 2321342

PXRMP24I Calculated 14301202

PXRMPCMM Calculated 11797305

PXRMPDEM Calculated 65842415

PXRMPINF Calculated 8130614

PXRMRDI Calculated 38535019

PXRMSCR Calculated 88295

PXRMTAX Calculated 65791721

PXRMUTIL Calculated 113964494

PXRMVSIT Calculated 10650656

PXRMXQUE Calculated 12328074

30 Routines checked, 0 failed.

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INstallation

Select Installation \<TEST ACCOUNT\> Option: PRINT Transport Global

Select INSTALL NAME: HIGH RISK MH 2.0 2/25/13@14:36:41

=\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

This Distribution was loaded on Feb 25, 2013@14:36:41 with header of

High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

It consisted of the following Install(s):

HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

OR\*3.0\*348 PXRM\*2.0\*24

Select Installation \<TEST ACCOUNT\> Option: INstall Package(s)

Select INSTALL NAME: HIGH RISK MH 2.0 2/25/13@14:36:41

=\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

This Distribution was loaded on Feb 25, 2013@14:36:41 with header of

High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

It consisted of the following Install(s):

HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

OR\*3.0\*348 PXRM\*2.0\*24

Checking Install for Package HIGH RISK MH 2.0

Install Questions for HIGH RISK MH 2.0

Checking Install for Package TIU\*1.0\*265

Install Questions for TIU\*1.0\*265

Checking Install for Package DG\*5.3\*849

Install Questions for DG\*5.3\*849

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'DGPF CLINICAL HR FLAG REVIEW': CARTER,DAVI

D

L DC 11CI CLINICAL APPLICATIONS COORD

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package SD\*5.3\*588

Install Questions for SD\*5.3\*588

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package GMTS\*2.7\*104

Will first run the Environment Check Routine, GMTSY104

CHECKING RECENT ADDITIONS TO HEALTH SUMMARY COMPONENT FILE

Medication Worksheet (Tool \#2): OK

MAS CONTACTS: OK

MAS MH CLINIC VISITS FUTURE: OK

MH HIGH RISK PRF HX: OK

MH TREATMENT COORDINATOR: OK

Install Questions for GMTS\*2.7\*104

Checking Install for Package OR\*3.0\*348

Install Questions for OR\*3.0\*348

Incoming Files:

100.9 OE/RR NOTIFICATIONS

> **NOTE:** You already have the 'OE/RR NOTIFICATIONS' File.

Checking Install for Package PXRM\*2.0\*24

Install Questions for PXRM\*2.0\*24

Incoming Files:

811.4 REMINDER COMPUTED FINDINGS (including data)

> **NOTE:** You already have the 'REMINDER COMPUTED FINDINGS' File.

I will REPLACE your data with mine.

811.8 REMINDER EXCHANGE (including data)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// 0;80;99999 SSH

Install Started for HIGH RISK MH 2.0 :

Feb 25, 2013@14:47:35

Build Distribution Date: Dec 07, 2012

Installing Routines:

Feb 25, 2013@14:47:35

Running Pre-Install Routine: MPBPRE^PXRMP24I

Install Started for TIU\*1.0\*265 :

Feb 25, 2013@14:47:35

Build Distribution Date: Dec 07, 2012

Installing Routines:

Feb 25, 2013@14:47:35

Installing PACKAGE COMPONENTS:

Installing PARAMETER DEFINITION

Feb 25, 2013@14:47:36

Running Post-Install Routine: ^TIUPS265

Title Created: PATIENT RECORD FLAG CATEGORY I - HIGH RISK FOR SUICIDE

Title attached to Document Class PATIENT RECORD FLAG CAT I

Updating Routine file...

Updating KIDS files...

TIU\*1.0\*265 Installed.

Feb 25, 2013@14:47:36

Not a production UCI

NO Install Message sent

Install Started for DG\*5.3\*849 :

Feb 25, 2013@14:47:36

Build Distribution Date: Dec 07, 2012

Installing Routines:

Feb 25, 2013@14:47:36

Installing PACKAGE COMPONENTS:

Installing MAIL GROUP

Installing OPTION

Feb 25, 2013@14:47:36

Running Post-Install Routine: ^DG53849P

Installing new national PRF entry

Installation of new national PRF entry complete

Updating Routine file...

Updating KIDS files...

DG\*5.3\*849 Installed.

Feb 25, 2013@14:47:36

Not a production UCI

NO Install Message sent

Install Started for SD\*5.3\*588 :

Feb 25, 2013@14:47:36

Build Distribution Date: Dec 07, 2012

Installing Routines:

Feb 25, 2013@14:47:36

Installing PACKAGE COMPONENTS:

Installing OPTION

Installing PARAMETER DEFINITION

Feb 25, 2013@14:47:36

Running Post-Install Routine: ^SD53588P

Updating Parameters File...

SDMH PROACTIVE DAYS

89895006^Duplicate instance not allowed.

SDMH NO SHOW DAYS

89895006^Duplicate instance not allowed.

Updating Routine file...

Updating KIDS files...

SD\*5.3\*588 Installed.

Feb 25, 2013@14:47:36

Not a production UCI

NO Install Message sent

Install Started for GMTS\*2.7\*104 :

Feb 25, 2013@14:47:36

Build Distribution Date: Dec 07, 2012

Installing Routines:

Feb 25, 2013@14:47:36

Running Post-Install Routine: POST^GMTSY104

Updating description for Health Summary Component MH HIGH RISK FOR SUICIDE

Update Successful

Updating Routine file...

Updating KIDS files...

GMTS\*2.7\*104 Installed.

Feb 25, 2013@14:47:37

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*348 :

Feb 25, 2013@14:47:37

Build Distribution Date: Dec 07, 2012

Installing Routines:

Feb 25, 2013@14:47:37

Installing Data Dictionaries:

Feb 25, 2013@14:47:37

Installing PACKAGE COMPONENTS:

Installing PARAMETER DEFINITION

Feb 25, 2013@14:47:37

Running Post-Install Routine: POST^ORY348

Updating Routine file...

Updating KIDS files...

OR\*3.0\*348 Installed.

Feb 25, 2013@14:47:37

Not a production UCI

NO Install Message sent

Install Started for PXRM\*2.0\*24 :

Feb 25, 2013@14:47:37

Build Distribution Date: Dec 07, 2012

Installing Routines:

Feb 25, 2013@14:47:38

Running Pre-Install Routine: PRE^PXRMP24I

DISABLE options.

DISABLE protocols.

Installing Data Dictionaries:

Feb 25, 2013@14:47:38

Installing Data:

Feb 25, 2013@14:47:38

Running Post-Install Routine: POST^PXRMP24I

ENABLE options.

ENABLE protocols.

There are 5 Reminder Exchange entries to be installed.

1\. Installing Reminder Exchange entry VA-MH NO SHOW APPT CLINICS LL

2\. Installing Reminder Exchange entry VA-MHTC APPT STOP CODES AND EXCLUSION

STOP

3\. Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW FOLLOW-UP

4\. Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW ADHOC RPT

5\. Installing Reminder Exchange entry VA-MHTC NEEDS ASSIGNMENT

Renaming/inactivating health factors and terms that are no longer used.

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*24 Installed.

Feb 25, 2013@14:47:59

Not a production UCI

NO Install Message sent

Running Post-Install Routine: POST^GMTSY104

Updating description for Health Summary Component MH HIGH RISK FOR SUICIDE

Update Successful

Updating Routine file...

Updating KIDS files...

HIGH RISK MH 2.0 Installed.

Feb 25, 2013@14:47:59

No link to PACKAGE file

PXRM\*2.0\*24

Install Completed

# # # Installation after Previous Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Select Installation \<TEST ACCOUNT\> Option: Install Package(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select INSTALL NAME: HIGH RISK MH 2.0 12/10/12@11:06:05

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# =\> High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # This Distribution was loaded on Dec 10, 2012@11:06:05 with header of 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# High Risk Mental Health phase 2 ;Created on Dec 07, 2012@10:16:34

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# It consisted of the following Install(s):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# HIGH RISK MH 2.0 TIU\*1.0\*265 DG\*5.3\*849 SD\*5.3\*588 GMTS\*2.7\*104

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# OR\*3.0\*348 PXRM\*2.0\*24

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Checking Install for Package HIGH RISK MH 2.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Questions for HIGH RISK MH 2.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Checking Install for Package TIU\*1.0\*265

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Questions for TIU\*1.0\*265

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Checking Install for Package DG\*5.3\*849

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Questions for DG\*5.3\*849

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Incoming Mail Groups:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Enter the Coordinator for Mail Group 'DGPF CLINICAL HR FLAG REVIEW': CRDEVELOPER,ONE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# OC OI&T STAFF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<Enter\> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Checking Install for Package SD\*5.3\*588

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Questions for SD\*5.3\*588

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<Enter\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Checking Install for Package GMTS\*2.7\*104

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Will first run the Environment Check Routine, GMTSY104

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # CHECKING RECENT ADDITIONS TO HEALTH SUMMARY COMPONENT FILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Medication Worksheet (Tool \#2): OK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # MAS CONTACTS: OK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # MAS MH CLINIC VISITS FUTURE: OK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # MH HIGH RISK PRF HX: OK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # MH TREATMENT COORDINATOR: OK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Questions for GMTS\*2.7\*104

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Checking Install for Package OR\*3.0\*348

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Questions for OR\*3.0\*348

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Incoming Files:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # OE/RR NOTIFICATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Note: You already have the 'OE/RR NOTIFICATIONS' File.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Checking Install for Package PXRM\*2.0\*24

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Questions for PXRM\*2.0\*24

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Incoming Files:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # REMINDER COMPUTED FINDINGS (including data)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Note: You already have the 'REMINDER COMPUTED FINDINGS' File.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# I will REPLACE your data with mine.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # REMINDER EXCHANGE (including data)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Note: You already have the 'REMINDER EXCHANGE' File.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# I will OVERWRITE your data with mine.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Want KIDS to INHIBIT LOGONs during the install? NO// \<Enter\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// \<Enter\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Enter the Device you want to print the Install messages.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# You can queue the install by enter a 'Q' at the device prompt.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Enter a '^' to abort the install.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # DEVICE: HOME// \<Enter\> SSH VIRTUAL TEMINAL Do not queue the install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# --------------------------------------------------------------------------------

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Started for HIGH RISK MH 2.0 : 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:14

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Build Distribution Date: Dec 07, 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:14

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Pre-Install Routine: MPBPRE^PXRMP24I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Started for TIU\*1.0\*265 : 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:14

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Build Distribution Date: Dec 07, 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:14

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing PACKAGE COMPONENTS: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing PARAMETER DEFINITION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:14

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Post-Install Routine: ^TIUPS265

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Title Created: PATIENT RECORD FLAG CATEGORY I - HIGH RISK FOR SUICIDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Title attached to Document Class PATIENT RECORD FLAG CAT I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating Routine file...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating KIDS files...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # TIU\*1.0\*265 Installed. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:16

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Not a production UCI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # NO Install Message sent 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Started for DG\*5.3\*849 : 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:16

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Build Distribution Date: Dec 07, 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing PACKAGE COMPONENTS: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing MAIL GROUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing OPTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Post-Install Routine: ^DG53849P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# The 'HIGH RISK FOR SUICIDE' PRF is already entered in the PRF NATIONAL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# FLAG file, no further processing of the new national PRF field entry.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating Routine file...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating KIDS files...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # DG\*5.3\*849 Installed. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Not a production UCI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # NO Install Message sent 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Started for SD\*5.3\*588 : 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Build Distribution Date: Dec 07, 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing PACKAGE COMPONENTS: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing OPTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing PARAMETER DEFINITION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Post-Install Routine: ^SD53588P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating Parameters File...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # SDMH PROACTIVE DAYS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 89895006^Duplicate instance not allowed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # SDMH NO SHOW DAYS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # 89895006^Duplicate instance not allowed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating Routine file...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating KIDS files...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # SD\*5.3\*588 Installed. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Not a production UCI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # NO Install Message sent 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Started for GMTS\*2.7\*104 : 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Build Distribution Date: Dec 07, 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Post-Install Routine: POST^GMTSY104

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating description for Health Summary Component MH HIGH RISK FOR SUICIDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Update Successful 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating Routine file...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating KIDS files...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # GMTS\*2.7\*104 Installed. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Not a production UCI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # NO Install Message sent 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Started for OR\*3.0\*348 : 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Build Distribution Date: Dec 07, 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Data Dictionaries: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing PACKAGE COMPONENTS: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing PARAMETER DEFINITION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:18

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Post-Install Routine: POST^ORY348

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating Routine file...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating KIDS files...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # OR\*3.0\*348 Installed. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:18

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Not a production UCI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # NO Install Message sent 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Started for PXRM\*2.0\*24 : 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:18

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Build Distribution Date: Dec 07, 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:18

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Pre-Install Routine: PRE^PXRMP24I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # DISABLE options.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # DISABLE protocols.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Data Dictionaries: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:19

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installing Data: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:19

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Post-Install Routine: POST^PXRMP24I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # ENABLE options.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # ENABLE protocols.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # There are 5 Reminder Exchange entries to be installed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry VA-MH NO SHOW APPT CLINICS LL 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry VA-MHTC APPT STOP CODES AND EXCLUSION 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# STOP 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW FOLLOW-UP 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW ADHOC RPT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installing Reminder Exchange entry VA-MHTC NEEDS ASSIGNMENT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Renaming/inactivating health factors and terms that are no longer used.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating Routine file...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating KIDS files...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # PXRM\*2.0\*24 Installed. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:31

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Not a production UCI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # NO Install Message sent 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Running Post-Install Routine: POST^GMTSY104

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating description for Health Summary Component MH HIGH RISK FOR SUICIDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Update Successful 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating Routine file...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating KIDS files...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # HIGH RISK MH 2.0 Installed. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Dec 10, 2012@11:07:31

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # No link to PACKAGE file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # # Install Completed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # # # # # # # Appendix B: Instructions for Recreating/ Re-pointing Site-defined Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To transfer a local notification outside the national number range (1-9999), FileMan’s Enter/Edit File Entries option should be used to create a new entry to transfer to. This will require the user to re-enter the data contained in the original notification entry in the new entry.

Please follow these steps for this transfer process:

For the purposes of this example, this will be the original notification entry that we will be transferring:

NUMBER: 77 NAME: LOCAL NOTIFICATION 1

PACKAGE ID: OR

MESSAGE TEXT: This is Local Notification Test 1.

MESSAGE TYPE: PACKAGE PROVIDES A VARIABLE MESSAGE

ACTION FLAG: RUN ROUTINE ENTRY POINT: INFODEL

ROUTINE NAME: ORB3FUP2 RELATED PACKAGE: OR

DESCRIPTION: Testing the transfer process of Local Notification 1.

1.  Create an entry in the OE/RR Notifications file \#100.9. This will be the new entry where the original entry information will be transferred to. This entry must have a unique, descriptive name and unique internal entry number. In addition, the internal entry number must be specific to your VAMC in the following format:

> \<your site station number\>\<incremental notification number 01-99\>

> For example, if your site is number 660, your first locally created notification would be 66001.

> Enter a slightly different name from the original entry; otherwise you will be editing the original entry name. The name can be edited later if you wish.

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: OE/RR NOTIFICATIONS//

EDIT WHICH FIELD: ALL//

Select OE/RR NOTIFICATIONS NAME: LOCAL NOTIFICATION TEST 1

Are you adding 'LOCAL NOTIFICATION TEST 1' as

a new OE/RR NOTIFICATIONS (the 57TH)? No// Y (Yes)

OE/RR NOTIFICATIONS NUMBER: 66001

21. Re-enter the following information from the original notification entry above. All "site-defined" notifications must be defined similarly to the following example:

NUMBER: \<site station number\>\<incremental number 01-99\>

NAME: \<unique site name\>

PACKAGE ID: OR MESSAGE TEXT: \<alert message text\>

MESSAGE TYPE: PACKAGE PROVIDES A VARIABLE MESSAGE

ACTION FLAG: RUN ROUTINE ENTRY POINT: INFODEL

ROUTINE NAME: ORB3FUP2

RELATED PACKAGE: OR

DESCRIPTION: \<description of the notification\>

> Site-defined notifications CANNOT have follow-up actions. (Notifications with follow-up actions must have follow-up action code written for both the ListManager and GUI interfaces. Currently, this requires the source code to the GUI which is not available.) Therefore, the entry point must be INFODEL and routine name ORB3FUP2.

MESSAGE TEXT: This is Local Notification Test 1.

MESSAGE TYPE: PKG PACKAGE PROVIDES A VARIABLE MESSAGE

ACTION FLAG: RUN RUN ROUTINE

ENTRY POINT: INFODEL

ROUTINE NAME: ORB3FUP2

NON-MENU TYPE OPTION ACTION:

RELATED PACKAGE: OR

DESCRIPTION: Testing the transfer process of Local Notification 1.

FOLLOW-UP TYPE:

22. Delete the original notification entry (IEN \#77) occupying the national numberspace. This will allow FileMan to provide the user the option to update any pointers pointing to the original entry.

Select OE/RR NOTIFICATIONS NAME: LOCAL NOTIFICATION 1

NAME: LOCAL NOTIFICATION 1 Replace @

SURE YOU WANT TO DELETE THE ENTIRE 'LOCAL NOTIFICATION 1' OE/RR NOTIFI

CATIONS? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'OE/RR LIST' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No//

Y (Yes)

23. Select option \#2 to redirect all pointers to point to the new record entry. Enter the name of the new record entry and exit out of the ENTER/EDIT option.

WHICH DO YOU WANT TO DO? --

1\) DELETE ALL SUCH POINTERS

2\) CHANGE ALL SUCH POINTERS TO POINT TO A DIFFERENT 'OE/RR

NOTIFICATIONS' ENTRY

CHOOSE 1) OR 2): 2

THEN PLEASE INDICATE WHICH ENTRY SHOULD BE POINTED TO

Select OE/RR NOTIFICATIONS NAME: LOCAL NOTIFICATION TEST 1

(RE-POINTING WILL OCCUR WHEN YOU LEAVE 'ENTER/EDIT' OPTION)

Select OE/RR NOTIFICATIONS NAME:

1)  This will generate a report of all the record entries whose pointers have been updated in the OE/RR LIST file \#100.21 and ORDER CHECK RULE file \#860.2. Of note, the notification pointers in file \#100.21 are obsolete and no longer in use, so that section of the report can be disregarded. If there are no records to print, then there are n o pointers in either of these files that point to the original entry.

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

DEVICE: HOME// ;;999 HOME

OE/RR LIST entries whose '\*NOTIFICATION SELECTION' pointers have been

changed

NOV 14,2012 14:01 PAGE 1

--------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

ORDER CHECK RULE entries whose 'NOTIFICATION' pointers have been changed

NOV 14,2012 14:01 PAGE 1

--------------------------------------------------------------------------

LOCAL NOTIFICATION ORDER CHECK 1 \*\*\*ACTIVE

5.  To verify that the pointers have updated correctly, you could perform a FileMan Print or Inquiry into the ORDER CHECK RULE file \#860.2 for those record entries that are printed out in the report above. For example:

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: ORDER CHECK RULE//

Select ORDER CHECK RULE NAME: LOCAL NOTIFICATION ORDER CHECK 1

\*\*\*ACTIVE

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// BOTH Computed Fields and Record

Number (IEN)

NUMBER: 39 NAME: LOCAL NOTIFICATION ORDER CHECK 1

LABEL: LOCAL NOTIFICATION 1

ELEMENT NAME: LOCAL NOTIFICATION 1

STATUS: ACTIVE

RELATION INDEX: 1 NOTIFICATION: LOCAL NOTIFICATION TEST 1

RELATION EXPRESSION: LOCAL NOTIFICATION 1

NOTIFICATION MESSAGE: This is Local Notification Test 1.

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OIT Master Glossary is available at <http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm>
| Term       | Definition                                                                                                                      |
|------------|---------------------------------------------------------------------------------------------------------------------------------|
| AIMS       | Abnormal Involuntary Movement Scale                                                                                             |
| AITC       | Austin Information Technology Center                                                                                            |
| API        | Application Programmer Interface.                                                                                               |
| ASU        | Authorization/Subscription Utility                                                                                              |
| Clin4      | National Customer Support team that supports Clinical Reminders                                                                 |
| CAC        | Clinical Applications Coordinator                                                                                               |
| CPRS       | Computerized Patient Record System                                                                                              |
| DBA        | Database Administration                                                                                                         |
| DG         | Registration and Enrollment Package namespace                                                                                   |
| ESM        | Enterprise Systems Management (ESM)                                                                                             |
| FIM        | Functional Independence Measure                                                                                                 |
| GEC        | Geriatric Extended Care                                                                                                         |
| GMTS       | Health Summary namespace (also HSUM)                                                                                            |
| GUI        | Graphic User Interface                                                                                                          |
| HRMH/HRMHP | High Risk Mental Health Patient                                                                                                 |
| IAB        | Initial Assessment & Briefing                                                                                                   |
| ICD-10     | International Classification of Diseases, 10th Edition                                                                          |
| ICR        | Internal Control Number                                                                                                         |
| IHD        | Ischemic Heart Disease                                                                                                          |
| IOC        | Initial Operating Capabilities                                                                                                  |
| LDL        | Low-density lipo-protein                                                                                                        |
| LSSD       | Last Service Separation Date                                                                                                    |
| MDD        | Major Depressive disorder                                                                                                       |
| MH         | Mental Health                                                                                                                   |
| MHTC       | Mental Health Treatment Coordinator                                                                                             |
| OHI        | Office of Health Information                                                                                                    |
| OI         | Office of Information                                                                                                           |
| OIF/OEF    | Operation Iraqi Freedom/Operation Enduring Freedom                                                                              |
| OIT/OI&T   | Office of Information Technology                                                                                                |
| OMHS       | Office of Mental Health Services                                                                                                |
| OQP        | Formerly Office of Quality and Performance, replaced by Office of Performance Measurement and Office of Quality, Safety & Value |
| OQSV       | Office of Quality, Safety & Value                                                                                               |
| ORR        | Operational Readiness Review                                                                                                    |
| PCE        | Patient Care Encounter                                                                                                          |
| PCS        | Patient Care Services                                                                                                           |
| PD         | Product Development                                                                                                             |
| PIMS       | Patient Information Management System                                                                                           |
| PMAS       | Program Management Accountability System                                                                                        |
| PTM        | Patch Tracker Message                                                                                                           |
| PXRM       | Clinical Reminder Package namespace                                                                                             |
| RSD        | Requirements Specification Document                                                                                             |
| SD         | Scheduling Package Namespace                                                                                                    |
| SQA        | Software Quality Assurance                                                                                                      |
| TIU        | Text Integration Utilities                                                                                                      |
| USR        | ASU package namespace                                                                                                           |
| VA         | Department of Veteran Affairs                                                                                                   |
| VHA        | Veterans Health Administration                                                                                                  |
| VISN       | Veterans Integrated Service Network                                                                                             |
| VistA      | Veterans Health Information System and Technology Architecture                                                                  |
