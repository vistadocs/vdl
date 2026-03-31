---
consolidated_title: "ar release notes/installation guide"
app_code: PRCA
doc_type: IG
master_source: "PRCA*4.5*298 AR Release Notes/Installation Guide"
master_pub_date: revision_count: 0
consolidated_from: 8 versions
prior_versions:
  - "PRCA*4.5*275 AR Release Notes/Installation Guide"
  - "PRCA*4.5*295 AR Release Notes/Installation Guide"
  - "PRCA*4.5*300 AR Release Notes/Installation Guide"
  - "PRCA*4.5*302 AR Release Notes/Installation Guide"
  - "PRCA*4.5*315 AR Release Notes/Installation Guide"
  - "PRCA*4.5*316 AR Release Notes/Installation Guide"
  - "PRCA*4.5*339 AR Release Notes/Installation Guide"
---

![](prca-4-5-298-ar-release-notes-installation-guide/001.png)

Electronic Data Interchange (EDI)New Standards and Operating Rules –VHA Provider-side Technical Compliance RequirementsVA118-1001-1018

ePayments

####### 

####### ACCOUNTS RECEIVABLE (PRCA)

####### RELEASE NOTES/ Installation Guide/ Rollback Plan

PRCA\*4.5\*298May 2015  
Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Documentation and Distribution](#documentation-and-distribution)
- [Patch Description and Installation Instructions](#patch-description-and-installation-instructions)
  - [Patch Description](#patch-description)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Installation Instructions](#installation-instructions)
- [Backout and Rollback Procedures](#backout-and-rollback-procedures)
  - [Overview of Backout and Rollback Procedures](#overview-of-backout-and-rollback-procedures)
  - [Backout Procedure](#backout-procedure)
  - [Rollback Procedure](#rollback-procedure)
- [Enhancements](#enhancements)
  - [System Feature: Site Parameters for Medical Auto-Post](#system-feature-site-parameters-for-medical-auto-post)
    - [Site Parameters for Medical Auto-Post – Parameter for Auto-posting Medical Claims](#site-parameters-for-medical-auto-post-parameter-for-auto-posting-medical-claims)
    - [Site Parameters for Medical Auto-Post – Notification of Edits for Parameter for Auto-posting Medical Claims](#site-parameters-for-medical-auto-post-notification-of-edits-for-parameter-for-auto-posting-medical-claims)
    - [Site Parameters for Medical Auto-Post – Parameter for Excluding Payers from Auto-posting of Medical Claims](#site-parameters-for-medical-auto-post-parameter-for-excluding-payers-from-auto-posting-of-medical-claims)
    - [Site Parameters for Medical Auto-Post – Default Parameter for Excluding Payers from Auto-posting of Medical Claims](#site-parameters-for-medical-auto-post-default-parameter-for-excluding-payers-from-auto-posting-of-medical-claims)
    - [Site Parameters for Medical Auto-Post – Comment for Excluding Payers from Auto-posting of Medical Claims](#site-parameters-for-medical-auto-post-comment-for-excluding-payers-from-auto-posting-of-medical-claims)
    - [Site Parameters for Medical Auto-Post – Security Key for Parameter for Auto-posting of Medical Claims](#site-parameters-for-medical-auto-post-security-key-for-parameter-for-auto-posting-of-medical-claims)
    - [Site Parameters for Medical Auto-Post – Audit for Auto-posting of Medical Claims](#site-parameters-for-medical-auto-post-audit-for-auto-posting-of-medical-claims)
  - [System Feature: Site Parameters for Medical Auto-Decrease](#system-feature-site-parameters-for-medical-auto-decrease)
    - [Site Parameters for Medical Auto-Decrease – Parameter for Auto-decrease of Medical Claims](#site-parameters-for-medical-auto-decrease-parameter-for-auto-decrease-of-medical-claims)
    - [Site Parameters for Medical Auto-Decrease – Parameter for Auto-decrease Timeframe of Medical Claims](#site-parameters-for-medical-auto-decrease-parameter-for-auto-decrease-timeframe-of-medical-claims)
    - [Site Parameters for Medical Auto-Decrease – Parameter for Auto-decrease Amount of Medical Claims](#site-parameters-for-medical-auto-decrease-parameter-for-auto-decrease-amount-of-medical-claims)
    - [Site Parameters for Medical Auto-Decrease – Parameter for Excluding Payers from Auto-decrease of Medical Claims](#site-parameters-for-medical-auto-decrease-parameter-for-excluding-payers-from-auto-decrease-of-medical-claims)
    - [Site Parameters for Medical Auto-Decrease – Default Parameter for Excluding Payers from Auto-decrease of Medical Claims](#site-parameters-for-medical-auto-decrease-default-parameter-for-excluding-payers-from-auto-decrease-of-medical-claims)
    - [Site Parameters for Medical Auto-Decrease – Comment for Excluding Payers from Auto-decrease of Medical Claims](#site-parameters-for-medical-auto-decrease-comment-for-excluding-payers-from-auto-decrease-of-medical-claims)
    - [Site Parameters for Medical Auto-Decrease - Security Key for Parameter for Auto-decrease of Medical Claims](#site-parameters-for-medical-auto-decrease-security-key-for-parameter-for-auto-decrease-of-medical-claims)
    - [Site Parameters for Medical Auto-Decrease - Audit for Auto-decrease of Medical Claims](#site-parameters-for-medical-auto-decrease-audit-for-auto-decrease-of-medical-claims)
    - [Site Parameters for Pharmacy Auto-Post - Parameter for Auto-posting Pharmacy Claims](#site-parameters-for-pharmacy-auto-post-parameter-for-auto-posting-pharmacy-claims)
  - [System Feature: Posting Prevention](#system-feature-posting-prevention)
    - [Posting Prevention - Posting Prevention for Medical Claims](#posting-prevention-posting-prevention-for-medical-claims)
    - [Posting Prevention - Posting Prevention for Pharmacy Claims](#posting-prevention-posting-prevention-for-pharmacy-claims)
  - [System Feature: Site Parameter Reporting - Report for Auto-processing](#system-feature-site-parameter-reporting-report-for-auto-processing)
    - [Site Parameter Reporting - Report for Auto-processing](#site-parameter-reporting-report-for-auto-processing)
    - [Site Parameter Reporting - Report for Auto-processing Audit](#site-parameter-reporting-report-for-auto-processing-audit)
    - [Site Parameter Reporting - Database for Payer](#site-parameter-reporting-database-for-payer)
    - [Site Parameter Reporting - Populate Database for Payer](#site-parameter-reporting-populate-database-for-payer)
    - [Site Parameter Reporting - Maintain Database for Payer](#site-parameter-reporting-maintain-database-for-payer)
    - [Site Parameter Reporting - Add Exclusion of all Payers for IOC](#site-parameter-reporting-add-exclusion-of-all-payers-for-ioc)
    - [Site Parameter Reporting - Remove Exclusion of all Payers for IOC](#site-parameter-reporting-remove-exclusion-of-all-payers-for-ioc)
    - [Site Parameter Reporting - Report for Payers](#site-parameter-reporting-report-for-payers)
  - [## System Feature: Transfer EEOB- Remove Transfer EEOB](#system-feature-transfer-eeob-remove-transfer-eeob)
    - [Transfer EEOB- Remove Transfer EEOB](#transfer-eeob-remove-transfer-eeob)
    - [Transfer EEOB - Remove EEOB Transfer Report](#transfer-eeob-remove-eeob-transfer-report)
  - [System Feature: Exception List- Security Key for Delete Message Action](#system-feature-exception-list-security-key-for-delete-message-action)
    - [Exception List- Security Key for Delete Message Action](#exception-list-security-key-for-delete-message-action)
    - [Exception List- Restrict Delete Message Action](#exception-list-restrict-delete-message-action)
    - [Exception List- Transfer Message](#exception-list-transfer-message)
    - [Exception List- Filter Question](#exception-list-filter-question)
    - [Exception List- Pharmacy Claim Comment Action](#exception-list-pharmacy-claim-comment-action)
    - [Exception List- Display Pharmacy Data](#exception-list-display-pharmacy-data)
    - [Exception List – Allow Suspense in Exceptions](#exception-list-allow-suspense-in-exceptions)
  - [## System Feature: Verification of EEOB Detail against Bill Detail](#system-feature-verification-of-eeob-detail-against-bill-detail)
    - [Verification of EEOB Detail against Bill Detail - Remove Case Sensitivity](#verification-of-eeob-detail-against-bill-detail-remove-case-sensitivity)
  - [System Feature: EEOB Worklist](#system-feature-eeob-worklist)
    - [EEOB Worklist - Remove Adjust (Inc/Dec) Action](#eeob-worklist-remove-adjust-incdec-action)
    - [EEOB Worklist - Exception Indicator](#eeob-worklist-exception-indicator)
    - [EEOB Worklist - Exception Error Message](#eeob-worklist-exception-error-message)
    - [EEOB Worklist – Warning for View/Print ERA](#eeob-worklist-warning-for-viewprint-era)
    - [EEOB Worklist - Posting Warning for Medical Claims](#eeob-worklist-posting-warning-for-medical-claims)
    - [EEOB Worklist - Posting Prevention for Medical Claims](#eeob-worklist-posting-prevention-for-medical-claims)
    - [EEOB Worklist - Posting Warning for Pharmacy Claims](#eeob-worklist-posting-warning-for-pharmacy-claims)
    - [EEOB Worklist - Posting Prevention for Pharmacy Claims](#eeob-worklist-posting-prevention-for-pharmacy-claims)
    - [EEOB Worklist - Rename the Option](#eeob-worklist-rename-the-option)
    - [EEOB Worklist - Split/Edit Action](#eeob-worklist-splitedit-action)
    - [EEOB Worklist - View/Print ERA Displays ECME Number](#eeob-worklist-viewprint-era-displays-ecme-number)
    - [EEOB Worklist - Remove Batch Question](#eeob-worklist-remove-batch-question)
    - [EEOB Worklist - Remove Hide/Display Batch Action](#eeob-worklist-remove-hidedisplay-batch-action)
    - [EEOB Worklist - User-Entered Pharmacy Comment](#eeob-worklist-user-entered-pharmacy-comment)
  - [System Feature: Unposted Payment Override](#system-feature-unposted-payment-override)
    - [Unposted Payment Override - New Option](#unposted-payment-override-new-option)
    - [Unposted Payment Override – New Option Text](#unposted-payment-override-new-option-text)
    - [Unposted Payment Override - Outlook Message](#unposted-payment-override-outlook-message)
  - [## System Feature: Select ERA Question](#system-feature-select-era-question)
    - [Select ERA Question- Select ERA Question](#select-era-question-select-era-question)
    - [Select ERA Question- Create Scratchpad](#select-era-question-create-scratchpad)
    - [Select ERA Question- View ERA Details](#select-era-question-view-era-details)
    - [Select ERA Question- Exit](#select-era-question-exit)
  - [System Feature: EEOB Worklist Filter](#system-feature-eeob-worklist-filter)
    - [EEOB Worklist Filter- Change View Action](#eeob-worklist-filter-change-view-action)
    - [EEOB Worklist Filter- Move Current Filter Questions](#eeob-worklist-filter-move-current-filter-questions)
    - [EEOB Worklist Filter- Auto-Posting, Non-Auto-Posting or Both](#eeob-worklist-filter-auto-posting-non-auto-posting-or-both)
    - [EEOB Worklist Filter- Medical, Pharmacy or Both](#eeob-worklist-filter-medical-pharmacy-or-both)
    - [EEOB Worklist Filter- Preferred View](#eeob-worklist-filter-preferred-view)
    - [EEOB Worklist Filter- Preferred View Initialization](#eeob-worklist-filter-preferred-view-initialization)
    - [EEOB Worklist Filter- Filter Displayed in Heading](#eeob-worklist-filter-filter-displayed-in-heading)
  - [## System Feature: ERA Unmatched Aging Report](#system-feature-era-unmatched-aging-report)
    - [ERA Unmatched Aging Report - Exception Indicator](#era-unmatched-aging-report-exception-indicator)
  - [## System Feature: Scratchpad Filter- Change View Action](#system-feature-scratchpad-filter-change-view-action)
    - [Scratchpad Filter- Change View Action](#scratchpad-filter-change-view-action)
    - [Scratchpad Filter- Order of Payments](#scratchpad-filter-order-of-payments)
    - [Scratchpad Filter- Unposted Lines or All Lines](#scratchpad-filter-unposted-lines-or-all-lines)
    - [Scratchpad Filter- Zero Payments Order](#scratchpad-filter-zero-payments-order)
    - [Scratchpad Filter- Preferred View](#scratchpad-filter-preferred-view)
    - [Scratchpad Filter- Preferred View Initialization](#scratchpad-filter-preferred-view-initialization)
    - [Scratchpad Filter- Filter Displayed in Heading](#scratchpad-filter-filter-displayed-in-heading)
  - [System Feature: Scratchpad](#system-feature-scratchpad)
    - [Scratchpad- Remove Batch Maintenance Action](#scratchpad-remove-batch-maintenance-action)
    - [Scratchpad- Remove Research Menu Actions](#scratchpad-remove-research-menu-actions)
    - [Scratchpad- Ignore Payment Retraction Pairs](#scratchpad-ignore-payment-retraction-pairs)
    - [Scratchpad- Pharmacy Fees](#scratchpad-pharmacy-fees)
    - [Scratchpad- EEOB Screen Display](#scratchpad-eeob-screen-display)
    - [Scratchpad- Display Auto-Posted ERA](#scratchpad-display-auto-posted-era)
    - [Scratchpad- Unavailable Actions for Auto-Posted ERA](#scratchpad-unavailable-actions-for-auto-posted-era)
    - [Scratchpad- Available Actions for Auto-Posted ERA](#scratchpad-available-actions-for-auto-posted-era)
    - [Scratchpad- Look at Receipt Action for Auto-Posted ERA](#scratchpad-look-at-receipt-action-for-auto-posted-era)
  - [System Feature: Auto-Decrease for Medical Claim](#system-feature-auto-decrease-for-medical-claim)
    - [Auto-Decrease for Medical Claim- Decrease Adjustment](#auto-decrease-for-medical-claim-decrease-adjustment)
    - [Auto-Decrease for Medical Claim- File for Medical Claim](#auto-decrease-for-medical-claim-file-for-medical-claim)
    - [Auto-Decrease for Medical Claim- Decrease Claim Amount](#auto-decrease-for-medical-claim-decrease-claim-amount)
    - [Auto-Decrease for Medical Claim- Auto-Decrease Report](#auto-decrease-for-medical-claim-auto-decrease-report)
  - [## System Feature: Auto-Posting Medical Claims](#system-feature-auto-posting-medical-claims)
    - [Auto-Posting Medical Claims- Auto-Posting Claims](#auto-posting-medical-claims-auto-posting-claims)
    - [Auto-Posting Medical Claims- Create and Process Receipt](#auto-posting-medical-claims-create-and-process-receipt)
    - [Auto-Posting Medical Claims- Auto-Posting Awaiting Resolution](#auto-posting-medical-claims-auto-posting-awaiting-resolution)
  - [System Feature: Auto-Posting](#system-feature-auto-posting)
    - [Auto-Posting - Run Nightly](#auto-posting-run-nightly)
    - [Auto-Posting - Receipt Creation](#auto-posting-receipt-creation)
    - [Auto-Posting - EEOB Worklist](#auto-posting-eeob-worklist)
    - [Auto-Posting - Ignore Payment Retraction Pairs](#auto-posting-ignore-payment-retraction-pairs)
    - [Auto-Posting - Status Change](#auto-posting-status-change)
    - [Auto-Posting - AR Display](#auto-posting-ar-display)
    - [Auto-Posting - FMS Data](#auto-posting-fms-data)
    - [Auto-Posting - Auto-Post Report](#auto-posting-auto-post-report)
  - [System Feature: Match to ECME Claim](#system-feature-match-to-ecme-claim)
    - [Match to ECME Claim- Match to ECME Claim for Correct Fill](#match-to-ecme-claim-match-to-ecme-claim-for-correct-fill)
  - [System Feature: Auto-Post Awaiting Resolution](#system-feature-auto-post-awaiting-resolution)
    - [Auto-Post Awaiting Resolution- Screen Display](#auto-post-awaiting-resolution-screen-display)
    - [Auto-Post Awaiting Resolution- Actions](#auto-post-awaiting-resolution-actions)
    - [Auto-Post Awaiting Resolution- All Payers or Range](#auto-post-awaiting-resolution-all-payers-or-range)
  - [System Feature: Auto-Post Awaiting Resolution EEOB](#system-feature-auto-post-awaiting-resolution-eeob)
    - [Auto-Post Awaiting Resolution EEOB- EEOB Screen Display](#auto-post-awaiting-resolution-eeob-eeob-screen-display)
    - [Auto-Post Awaiting Resolution EEOB- EEOB Screen Actions](#auto-post-awaiting-resolution-eeob-eeob-screen-actions)
    - [Auto-Post Awaiting Resolution EEOB- Mark for Auto-Post](#auto-post-awaiting-resolution-eeob-mark-for-auto-post)
  - [## System Feature: Auto-Post Awaiting Resolution View/Print ERA](#system-feature-auto-post-awaiting-resolution-viewprint-era)
    - [Auto-Post Awaiting Resolution View/Print ERA - Add Auto-Post Status](#auto-post-awaiting-resolution-viewprint-era-add-auto-post-status)
    - [Auto-Post Awaiting Resolution View/Print ERA - Detail Post Status](#auto-post-awaiting-resolution-viewprint-era-detail-post-status)
    - [Auto-Post Awaiting Resolution View/Print ERA – Add Auto-Post Date](#auto-post-awaiting-resolution-viewprint-era-add-auto-post-date)
    - [Auto-Post Awaiting Resolution View/Print ERA – Receipt](#auto-post-awaiting-resolution-viewprint-era-receipt)
  - [## System Feature: Auto-Post Awaiting Resolution Filter](#system-feature-auto-post-awaiting-resolution-filter)
    - [Auto-Post Awaiting Resolution Filter- Change View Action](#auto-post-awaiting-resolution-filter-change-view-action)
    - [Auto-Post Awaiting Resolution Filter- All Payers or Range](#auto-post-awaiting-resolution-filter-all-payers-or-range)
    - [Auto-Post Awaiting Resolution Filter- Preferred View](#auto-post-awaiting-resolution-filter-preferred-view)
    - [Auto-Post Awaiting Resolution Filter- Preferred View Initialization](#auto-post-awaiting-resolution-filter-preferred-view-initialization)
    - [Auto-Post Awaiting Resolution Filter- Filter Displayed in Heading](#auto-post-awaiting-resolution-filter-filter-displayed-in-heading)
  - [System Feature: Receipt Processing](#system-feature-receipt-processing)
    - [Receipt Processing- Change Type of Payment](#receipt-processing-change-type-of-payment)
    - [Receipt Processing- Un-match the EFT](#receipt-processing-un-match-the-eft)
  - [System Feature: Exception Bulletins- Remove Bulletins](#system-feature-exception-bulletins-remove-bulletins)
    - [Exception Bulletins- Remove Bulletins](#exception-bulletins-remove-bulletins)
  - [System Feature: TPJI Reports- Add Indicator for Rejects](#system-feature-tpji-reports-add-indicator-for-rejects)
    - [TPJI Reports- Add Auto-Post Status](#tpji-reports-add-auto-post-status)
  - [System Feature: Daily Activity Report](#system-feature-daily-activity-report)
    - [Daily Activity Report- Change the Name](#daily-activity-report-change-the-name)
  - [System Feature: Miscellaneous Reports](#system-feature-miscellaneous-reports)
    - [Miscellaneous Reports- Add a Date Range](#miscellaneous-reports-add-a-date-range)
    - [Miscellaneous Reports- Change to ListManager](#miscellaneous-reports-change-to-listmanager)
    - [Miscellaneous Reports - Add Filter for TRICARE and CHAMPVA](#miscellaneous-reports-add-filter-for-tricare-and-champva)
  - [System Feature: EEOB Move/Copy Option](#system-feature-eeob-movecopy-option)
    - [EEOB Move/Copy Option- Correct Payer Information](#eeob-movecopy-option-correct-payer-information)
    - [EEOB Move/Copy Option- Rename the Option](#eeob-movecopy-option-rename-the-option)
    - [EEOB Move/Copy Option- Require Security Key](#eeob-movecopy-option-require-security-key)
    - [EEOB Move/Copy Option- Remove Option](#eeob-movecopy-option-remove-option)
    - [EEOB Move/Copy Option- Audit Log](#eeob-movecopy-option-audit-log)
    - [EEOB Move/Copy Option- Reports](#eeob-movecopy-option-reports)
    - [EEOB Move/Copy Option- AR Comment=](#eeob-movecopy-option-ar-comment)
    - [EEOB Move/Copy Option- AR Comment History](#eeob-movecopy-option-ar-comment-history)
    - [EEOB Move/Copy Option- Add Filter Question](#eeob-movecopy-option-add-filter-question)
  - [System Feature: Add Security Keys](#system-feature-add-security-keys)
    - [Add Security Keys- Add Security Keys](#add-security-keys-add-security-keys)
  - [System Feature: Testing Tool](#system-feature-testing-tool)
    - [Testing Tool- Reset 837](#testing-tool-reset-837)
    - [Testing Tool- Reset ECME Bill](#testing-tool-reset-ecme-bill)
    - [Testing Tool- Manipulate Fields and Resend](#testing-tool-manipulate-fields-and-resend)
    - [Testing Tool- Process De-Identified data](#testing-tool-process-de-identified-data)
    - [Testing Tool- Not Available after National Release](#testing-tool-not-available-after-national-release)
  - [System Feature: Non- Released Prescriptions](#system-feature-non-released-prescriptions)
    - [Non- Released Prescriptions- EXC Exception List](#non-released-prescriptions-exc-exception-list)
    - [Non- Released Prescriptions – Process Released Prescriptions](#non-released-prescriptions-process-released-prescriptions)
  - [System Feature: Trace Number with 9s](#system-feature-trace-number-with-9s)
    - [Trace Number with 9s- Include EFTs](#trace-number-with-9s-include-efts)
  - [Sytem Feature: Active Bills with EEOB Report](#sytem-feature-active-bills-with-eeob-report)
    - [Active Bills with EEOB Report- EEOB Date Posted](#active-bills-with-eeob-report-eeob-date-posted)
  - [System Feature: Manual Match of ERA and EFT](#system-feature-manual-match-of-era-and-eft)
    - [Manual Match of ERA and EFT- Add Date Range](#manual-match-of-era-and-eft-add-date-range)
    - [Manual Match of ERA and EFT- Partial Match on Trace Number](#manual-match-of-era-and-eft-partial-match-on-trace-number)
  - [System Feature: Decrease Adjustment](#system-feature-decrease-adjustment)
    - [Decrease Adjustment - Warning Message if Mark for Auto-Post](#decrease-adjustment-warning-message-if-mark-for-auto-post)
  - [System Feature: EDI Lockbox Menu](#system-feature-edi-lockbox-menu)
    - [EDI Lockbox Menu- Order of Menu Options](#edi-lockbox-menu-order-of-menu-options)
  - [System Feature: Trace Number Matching](#system-feature-trace-number-matching)
    - [Trace Number Matching – Remove Case Sensitivity](#trace-number-matching-remove-case-sensitivity)
This patch has enhancements that extend the capabilities of the Veterans
Health Information Systems and Technology Architecture (VistA) electronic
payment (ePayments) system. Below is a list of all the applications involved
in this project along with their patch number:
APPLICATION/VERSION PATCH
---------------------------------------------------------------
INTEGRATED BILLING (IB) V. 2.0 IB\*2\*511
ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*17
ACCOUNTS RECEIVABLE (PRCA) V. 4.5 PRCA\*4.5\*298
The patches (IB\*2\*511, BPS\*1\*17 and PRCA\*4.5\*298) are being released in the
Kernel Installation and Distribution System (KIDS) multi-build distribution
BPS IB PRCA EPAYMENTS BUNDLE 1.0.

## Documentation and Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation Retrieval Instructions:

------------------------------------

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to FTP the files from

REDACTED

This transmits the files from the first available FTP server. Sites may

also elect to retrieve software directly from a specific server as

follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

The documentation will be in the form of Adobe Acrobat files.

Documentation can also be found on the VA Software Documentation Library

at: REDACTED

Title File Name FTP Mode

----------------------------------------------------------------------

AR Release Notes/Installation PRCA_4_5_P298_RN.PDF Binary

Guide (PRCA\*4.5\*298)

ePayments User Manual (EDI Lockbox) PRCA_4_5_UM_epayments_R0515.PDF

> Binary

AR Technical Manual/Security Guide PRCA_4_5_TM_R0515.PDF Binary

AR User Manual - Clerk's AR Menu

\- Part 1 PRCA_4_5_UM_CLERK_R0515.PDF Binary

AR User Manual - Agent Cashier PRCA_4_5_UM_AC_R0515.PDF Binary

*(This page included for two-sided copying.)*

# Patch Description and Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

=============================================================================

Run Date: MAY 19, 2015 Designation: PRCA\*4.5\*298

Package : ACCOUNTS RECEIVABLE Priority : MANDATORY

Version : 4.5 Status : RELEASED

=============================================================================

Associated patches:

(v)PRCA\*4.5\*208\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*220\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*222\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*241\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*249\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*253\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*261\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*262\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*269\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*271\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*276\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*283\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*284\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*293\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

(v)PRCA\*4.5\*296\<\<= must be installed BEFORE \`PRCA\*4.5\*298'

Subject: ePAYMENTS COMPLIANCE

Category: ROUTINE

DATA DICTIONARY

OTHER

PRINT TEMPLATE

ENHANCEMENT

Description:

===========

This patch has enhancements that extend the capabilities of the Veterans

Health Information Systems and Technology Architecture (VistA) electronic

payment (ePayments) system. Below is a list of all the applications

involved in this project along with their patch number:

APPLICATION/VERSION PATCH

---------------------------------------------------------------

ACCOUNTS RECEIVABLE (PRCA) V. 4.5 PRCA\*4.5\*298

INTEGRATED BILLING (IB) V. 2.0 IB\*2\*511

ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*17

The patches PRCA\*4.5\*298, IB\*2\*511, and BPS\*1\*17 are being released in the

Kernel Installation and Distribution System (KIDS) multi-build

distribution BPS IB PRCA EPAYMENTS BUNDLE 1.0.

The purpose of this software package is to increase automation of the

current ePayments processes in order to improve productivity of Accounts

Receivable (AR) staff and increase accuracy of the revenue operation.

These changes include:

1\. Increasing automation of third party payer medical claims processing

a\. Automatic Electronic Remittance Advice (ERA) posting (auto-posting)

for ERAs associated with Electronic Fund Transfers (EFTs)

b\. Automatic decrease (auto-decrease) adjustments

2\. Addressing issues with existing ePayments process for pharmacy claims

a\. Automatic matching of pharmacy 835 responses with the ECME claim

3\. Increasing automation of pharmacy claims processing

a\. Process standard National Council for Prescription Drug Programs

(NCPDP) pharmacy fees

b\. Manage non-released prescriptions

4\. Enabling a switch-back solution through implementation of parameter

questions

This specific patch contains the following functionality:

---------------------------------------------------------

1\. The ePayments Site Parameter Edit menu was modified.

a\. The existing EDI Lockbox Parameters option \[RCDPE EDI LOCKBOX

PARAMETERS\] is extended to allow maintenance of new parameter

values for the new automatic processing and posting prevention

functionality.

These parameters include:

\- Enable Auto-posting of Medical Claims for the site

\- Payers to be excluded from Auto-posting

\- Enable Auto-decrease of Medical Claims for the site

\- Payers to be excluded from Auto-decrease

\- Number of Days to wait before Auto-decrease is applied

\- Maximum Dollar Amount for which Auto-decrease is allowed

\- Number of Days Allowed for Un-Posted Medical EFTs

\- Number of Days Allowed for Un-Posted Pharmacy EFTs

b\. A new EDI Lockbox Parameter Report option \[RCDPE SITE PARAMETER

REPORT\] displays the parameter settings.

c\. A new EDI Lockbox Exclusion Audit Report option \[RCDPE EXCLUSION

AUDIT REPORT\] reports changes made to the excluded payer parameters

d\. A new EDI Lockbox Parameters Audit Report option \[RCDPE PARAMETER

AUDIT REPORT\] reports changes made to other parameters

2\. The Accounts Receivable Nightly Process Background Job \[PRCA NIGHTLY

PROCESS\] was modified to automatically create receipts for ERA if the

following criteria are met:

\- Enable Auto-posting of Medical Claims parameter is set to 'Yes'

\- The Payer for the ERA is not excluded from Auto-posting

\- ERA is matched to an EFT and the EFT receipt's status is

'Accepted By FMS'

\- ERA has no EXC exceptions and also contains no ERA level adjustments

3\. The Accounts Receivable Nightly Process Background Job was also

modified to automatically apply contract decrease adjustments to claims

which have been previously automatically posted if the following

criteria are met:

\- Enable Auto-posting parameter for medical claims is set to 'Yes'

\- Enable Auto-decrease parameter for medical claims is set to 'Yes'

\- The Payer for the claim is not excluded from Auto-decrease or

Auto-posting

\- The number of days since Auto-posting exceeds the value of the

Number of Days to Wait before Auto-decrease parameter

\- The claim balance does not exceed the value of the Maximum Dollar

Amount parameter

4\. The EDI Lockbox Reports Menu \[RCDPE EDI LOCKBOX REPORTS MENU\] was

modified to include new ad-hoc reports of Auto-posting and

Auto-decrease activity

\- A new Auto-post Report option \[RCDPE AUTO-POST REPORT\] displays

information on receipts created by Auto-Posting for selected

dates and payers

\- A new Auto-decrease Adjustment Report \[RCDPE AUTO-DECREASE

REPORT\] displays Information on claims Auto-decreased for

selected dates and payers

5\. The EDI Lockbox menu option \[RCDPE EDI LOCKBOX MENU\] was modified to

include a new Auto-Post Awaiting Resolution option \[RCDPE APAR\].

This option allows for claim lines rejected by the nightly Auto-posting

process to be reviewed and resubmitted for Auto-posting.

Claim lines can be rejected for the following reasons:

\- The claim has been referred to General Counsel

\- The payment (or other pending payments) would generate a negative

balance on the claim

\- The claim is no longer active

Note that the new Auto-Posting Awaiting Resolution option \[RCDPE APAR\]

is similar to the current EOB Worklist option \[RCDPE EDI LOCKBOX

WORKLIST\] except that a receipt cannot be created directly.

A 'Mark For Auto-Posting' action allows claims to be re-submitted to

Auto-Posting after review and correction.

6\. The Decrease Adjustment option \[PRCAC TR DECREASE\] was changed to

display a warning message if a user tries to make a decrease adjustment

on a bill that has at least one associated Electronic Explanation

of Benefit (EEOB) marked for auto-post.

7\. Exception processing options were modified:

a\) The EDI Lockbox 3rd Party Exceptions option \[RCDPE

EXCEPTION PROCESSING\] is modified

\- The action to 'Transfer EEOB' is removed from the Data Exceptions

screen

\- A new RCDPE ERA EXCEPT key is now required for use of the Delete

Message action

\- ERAs with payment method of Automated Clearing House can no longer

be deleted

\- A record selection filter for Medical, Pharmacy or Both claim types

is also added to the EEOB Data Exceptions List Manager screen

\- For pharmacy claims the EEOB Data Exceptions List Manager screen now

displays the ECME number and release date for pharmacy claims. If

the prescription is not released then entry and display

of a comment is allowed

\- Exceptions due to non-released prescriptions are now cleared

automatically from the data exceptions list by the AR Nightly Process

when prescriptions are released. The EEOB for the prescription are

then processed normally.

b\) The EEOB Transfer Reports option \[RCDPE EOB TRANSFER REPORTS\] was

removed from the EDI Lockbox Reports Menu \[RCDPE EDI LOCKBOX REPORTS

MENU\]

8\. The matching of ERA claim numbers to the VistA database was improved

for both pharmacy and medical claims.

9\. The EEOB Worklist option \[RCDPE EDI LOCKBOX WORKLIST\] was renamed

ERA Worklist and has a number of new functions:

\- The capability to view an ERA without creating a Scratchpad is added

\- On the Worklist screen an 'x' is displayed against any ERA which has

exceptions and a warning is displayed if the users attempts to work

the ERA before the exceptions are cleared

\- The Worklist screen displays a warning message if an ERA is selected

and there are other unposted EFT payments for medical claims more

than 14 days old or pharmacy claims older than the number of days

specified in the site parameters

\- The Worklist screen will prevent selection of an ERA when there are

other unposted EFT payments for medical claims more than 21 days old

or pharmacy claims older than the number of days specified in the

site parameters

\- Verification of ERA patient information against VistA claim

for the Scratchpad is no longer case sensitive

\- The Adjust (Inc/Dec) action on the Research Menu List Manager

screen was removed

\- The Split/Edit A Line action in the Scratchpad screen is modified to

transfer the correct payer name when editing EEOB with different

payer names

\- The ECME number for pharmacy claims is displayed on the Scratchpad

screen and on the View/Print ERA action

10\. A new Unposted EFT Override option \[RCDPE UNPOSTED EFT OVERRIDE\] was

added to the EDI Lockbox menu \[RCDPE EDI LOCKBOX MENU\]. This allows

users with the new RCDPE AGED PMT security key to override posting

prevention in the ERA Worklist. The reason for the override must be

entered as a comment.

11\. ERA selection criteria for the EEOB Worklist option \[RCDPE EDI LOCKBOX

WORKLIST\] can be saved as the preferred Worklist view for the user

and will be re-used each time the Worklist is entered. The preferred

view for the user may be changed by using the Change View (CV) action

in the ERA Worklist screen.

A new filter for Medical ERAs only, Pharmacy ERAs only or both was

added and also included in the preferred view.

12\. The Batch Maintenance actions was removed from the Scratchpad screen

in the EEOB Worklist option \[RCDPE EDI LOCKBOX WORKLIST\].

The Hide/Display Batch action is removed from the ERA List - Worklist

screen in the EEOB Worklist option \[RCDPE EDI LOCKBOX WORKLIST\].

13\. Scratchpad display criteria for the EEOB Worklist option \[RCDPE EDI

LOCKBOX WORKLIST\] can be saved as the preferred Scratchpad view for a

user and will be re-used each time the Scratchpad screen is entered.

The preferred view for the user may be changed by using the CV action.

A new filter for posted lines, un-posted lines or both was added and

also included in the preferred view. This is for Auto-Posted ERAs.

14\. For pharmacy claims the Release Date, ECME number and Date of Service

are displayed in the Scratchpad View EEOB action for the EEOB

Worklist option \[RCDPE EDI LOCKBOX WORKLIST\].

15\. The following actions were removed from the Research Menu screen in

the EEOB Worklist option \[RCDPE EDI LOCKBOX WORKLIST\]:

\- Release Hold

\- On Hold List

\- Claims Matching Report

16\. Changes were made to the reports in the EDI Lockbox Reports Menu

\[RCPDE EDI LOCKBOX REPORTS MENU\]

a\) To facilitate searching of report content List Manager

functionality was added to the existing reports:

\- Active Bills With EEOB Report \[RCDPE ACTIVE WITH EEOB REPORT\]

\- Daily Activity Report \[RCDPE EDI LOCKBOX ACT REPORT\]

\- ERA Unmatched Aging Report \[RCDPE ERA AGING REPORT\]

\- EFT Unmatched Aging Report \[RCDPE EFT AGING REPORT\]

\- Unapplied EFT Deposits Report \[RCDPE UNAPPLIED EFT DEP REPORT\]

\- Duplicate EFT Deposits Audit Report \[RCDPE EFT AUDIT REPORT\]

\- EEOB Move/Copy/Rmove Audit Report \[RCDPE EEOB MOVE/COPY/RMOVE RPT\]

\- ERAs Posted with Paper EOB Audit Report \[RCDPE ERA W/PAPER EOB

REPORT\]

\- Remove ERA from Active Worklist Audit Report \[RCDPE REMOVED ERA

AUDIT\]

b\) A filter to allow inclusion or exclusion of TRICARE and/or

CHAMPVA was added to the existing reports

\- Active Bills With EEOB Report \[RCDPE ACTIVE WITH EEOB REPORT\]

\- ERA Unmatched Aging Report \[RCDPE ERA AGING REPORT\]

\- EEOB Move/Copy/Rmove Audit Report \[RCDPE EEOB MOVE/COPY/RMOVE RPT\]

\- ERAs Posted with Paper EOB Audit Report \[RCDPE ERA W/PAPER EOB

REPORT\]

\- Remove ERA from Active Worklist Audit Report \[RCDPE REMOVED ERA

AUDIT\]

c\) The ERA Unmatched Aging Report now displays an 'x' indicator against

any ERA for which a Transmission or Data exception exists

d\) The Daily Activity Report option \[RCDPE EDI LOCKBOX ACT REPORT\] is

renamed EFT Daily Activity Report

e\) The following reports were corrected to include EFTs with all 9's

in the trace number:

\- Daily Activity Report (now renamed EFT Daily Activity Report)

\[RCDPE EDI LOCKBOX ACT REPORT\]

\- EFT Unmatched Aging Report \[RCDPE EFT AGING REPORT\]

\- Unapplied EFT Deposits Report \[RCDPE UNAPPLIED EFT DEP REPORT\]

f\) A date range selection prompt was added to the Active Bills with

EEOB Report \[RCDPE ACTIVE WITH EEOB REPORT\]

17\. The Receipt Processing option \[RCDP RECEIPT PROCESSING\] action 'ER

Edit Receipt' was modified to allow the user to change open receipts

with a payment type of 'EDI LOCKBOX' to payment type 'CHECK/MO

PAYMENT'. The user is prompted 'Are You Sure?' and the EFT is changed

to a match status of 'UNMATCHED'.

18\. The option Manual Match EFT - ERA \[RCDPE MANUAL MATCH EFT-ERA\] was

modified to allow selection of an unmatched EFT within a date range.

19\. The option to remove an EEOB is added to the EEOB Move/Copy option

\[RCDPE EEOB MOVE/COPY\] which was renamed EEOB Move/Copy/Remove

\[RCDPE EEOB MOVE/COPY/REMOVE\].

20\. The EEOB Move/Copy Audit Report \[RCDPE EEOB MOVE/COPY RPT\] was

renamed to EEOB Move/Copy/Remove Audit Report \[RCDPE EEOB

MOVE/COPY/RMOVE RPT\] and includes removed EEOBs.

21\. The following MailMan notifications were disabled:

\- EDI LBOX EEOB - EXCEPTIONS

\- EDI LBOX - NO VALID BILLS ON ERA

\- EDI LBOX - ERA HAS ADJ/TAKEBACKS

\- EDI LBOX ERA - DUPLICATE TRANSMISSION MSG

\- EEOB MOVE/COPY

Patch Components

================

The following is a list of field modifications included in this patch:

File Name (#) New/Modified/

Sub-File Name (#) Field Name (#) Deleted

------------------- ------------------- --------

AR BATCH PAYMENT (#344) Modified

EFT RECORD (#.17) Modified

ERA REFERENCE (#.18) Modified

EDI THIRD PARTY EFT DETAIL (#344.31) Modified

TRACE (#.04) Modified

DATE RECEIVED (#.13) Modified

ELECTRONIC REMITTANCE ADVICE (#344.4) Modified

TRACE NUMBER (#.02) Modified

PAYMENT FROM (#.06) Modified

ERA DETAIL POST STATUS (#.14) Modified

AUTO-POST DATE (#4.01) New

AUTO-POST STATUS (#4.02) New

LATEST AUTO-DECREASE DATE (#4.03) New

ERA DETAIL sub-file (#344.41) Modified

ECME \# (#.24) New

RECEIPT (#.25) New

AUTO-POST REJECTION REASON (#5) New

MARK FOR AUTO-POST (#6) New

AUTO-DECREASE INDICATOR (#7) New

AUTO-DECREASE AMOUNT (#8) New

AUTO-POST DATE (#9) New

PHARMACY CLAIM COMMENT (#9.01) New

AUTO-DECREASE DATE (#10) New

OTHER RECEIPT NUMBERS sub-file (#344.48) New

OTHER RECEIPT NUMBER (#.01) New

EDI LOCKBOX EOB WORKLIST (#344.49) Modified

OTHER RECEIPT NUMBERS sub-file (#344.494) New

OTHER RECEIPT NUMBER (#.01) New

RCDPE AUTO-PAY EXCLUSION (#344.6) New File

PAYER NAME (#.01)

PAYER ID (#.02)

DATE ADDED (#.03)

UPDATED BY (#.04)

DATE LAST UPDATED (#.05)

EXCLUDE MED CLAIMS POSTING (#.06)

EXCLUDE MED CLAIMS DECREASE (#.07)

AUTO-POST COMMENT (#1)

AUTO-DECREASE COMMENT (#2)

RCDPE PARAMETER (#344.61) New File

SITE (#.01)

AUTO-POST MED CLAIMS ENABLED (#.02)

AUTO-DECREASE MED ENABLED (#.03)

AUTO-DECREASE MED DAYS DEFAULT (#.04)

AUTO-DECREASE MED AMT DEFAULT (#.05)

MEDICAL EFT POST PREVENT DAYS (#.06)

PHARMACY EFT POST PREVENT DAYS (#.07)

LAST UPDATE PAYER EXCLUSIONS (#.08)

EFT CUTOFF field (#.09)

MEDICAL EFT OVERRIDE (#20)

PHARMACY EFT OVERRIDE (#21)

USER-MEDICAL OVERRIDE (#22)

USER-PHARMACY OVERRIDE (#23)

COMMENT-MEDICAL OVERRIDE (#24)

COMMENT-PHARMACY OVERRIDE (#25)

RCDPE PARAMETER AUDIT (#344.7) New File

TIMESTAMP (#.01)

MODIFIED IEN (#.02)

CHANGED BY (#.03)

CHANGED FIELD (#.04)

MODIFIED FILE (#.05)

NEW VALUE (#.06)

OLD VALUE (#.07)

COMMENT (#.08)

RC MESSAGE TEXT OBJECT FILE (#344.81) New File

NUMBER (#.001)

NAME (#.01)

CREATOR (#.02)

CREATED (#.03)

LAST UPDATED (#.04)

DESCRIPTION (#.05)

TYPE (#1.01)

OBJECT STATUS (#1.02)

OBJECT TEXT sub-file (#344.812)

OBJECT TEXT (#.01)

RC TESTING USER PREFERENCES (#344.82) New File

USER (#.01)

UPDATED (#.02)

PAYER ID DEFAULT (#1.01)

PAYMENT METHOD CODE (#1.02)

Forms Associated:

Form Name File \# New/Modified/Deleted

--------- ------ --------------------

N/A

Mail Groups Associated:

Mail Group Name New/Modified/Deleted

--------------- --------------------

N/A

Option Name Type Deleted

----------- ---- -------------

PRCA BIL AGENCY action Modified

PRCA CBO PARAMETERS run routine Modified

PRCA DEACTIVATE GROUP action Modified

PRCA NOTIFICATION action Modified

PARAMETERS

PRCA RC PARAMETERS run routine Modified

PRCA SITE PARAMETER menu Modified

PRCAF U ADMIN.RATE action Modified

RCDPE ACTIVE WITH EEOB run routine Modified

REPORT

RCDPE APAR run routine New

RCDPE AUTO-DECREASE run routine New

REPORT

RCDPE AUTO-POST REPORT run routine New

RCDPE EDI LOCKBOX ACT run routine Modified

REPORT

RCDPE EDI LOCKBOX MENU menu Modified

RCDPE EDI LOCKBOX run routine Modified

PARAMETERS

RCDPE EDI LOCKBOX menu Modified

REPORTS MENU

RCDPE EDI LOCKBOX run routine Modified

WORKLIST

RCDPE EEOB MOVE/COPY Delete

RCDPE EEOB MOVE/COPY Delete

REPORT

RCDPE EEOB run routine New

MOVE/COPY/REMOVE

RCDPE EEOB run routine New

MOVE/COPY/RMOVE RPT

RCDPE EFT AGING REPORT run routine Modified

RCDPE EFT AUDIT REPORT run routine Modified

RCDPE EOB TRANSFER run routine Modified

REPORTS

RCDPE ERA AGING REPORT run routine Modified

RCDPE ERA POSTED BY run routine Modified

PAPER EOB

RCDPE ERA W/PAPER EOB run routine Modified

REPORT

RCDPE EXCEPTION run routine Modified

PROCESSING

RCDPE EXCLUSION AUDIT run routine New

REPORT

RCDPE MANUAL MATCH run routine Modified

EFT-ERA

RCDPE MARK 0-BAL EFT run routine Modified

MATCHED

RCDPE MATCH EFT TO ERA run routine Modified

RCDPE MOVE ERA TO run routine Modified

SUSPENSE

RCDPE PARAMETER AUDIT run routine New

REPORT

RCDPE PAYER EXCLUSION run routine New

NAME TIN

RCDPE REMOVE DUP run routine Modified

DEPOSITS

RCDPE REMOVE ERA FROM run routine Modified

WORKLIST

RCDPE REMOVED ERA AUDIT run routine Modified

RCDPE SITE PARAMETER run routine New

REPORT

RCDPE UNAPPLIED EFT DEP run routine Modified

REPORT

RCDPE UNMATCH ERA run routine Modified

RCDPE UNPOSTED EFT run routine New

OVERRIDE

RCDPE VIEW/PRINT ERA run routine Modified

RCDPETT TOOL run routine New

Protocols Associated:

Protocol Name New/Modified/Deleted

------------- --------------------

RCDPE APAR CHANGE VIEW New

RCDPE APAR EEOB LIST MENU New

RCDPE APAR EEOB REFRESH New

RCDPE APAR EEOB REVIEW New

RCDPE APAR EEOB RESEARCH MENU New

RCDPE APAR RESEARCH New

RCDPE APAR SELECT EEOB New

RCDPE APAR SELECTED EEOB MENU New

RCDPE APAR SPLIT LINE New

RCDPE APAR VERIFY New

RCDPE APAR VIEW/PRINT EOB New

RCDPE APAR VIEW/PRINT ERA New

RCDPE EOB WL RECEIPT VIEW Modified

RCDPE EOB WL RESEARCH EXIT Modified

RCDPE EOB WL REVIEW Modified

RCDPE EOB WORKLIST ADMIN COST ADJ Modified

RCDPE EOB WORKLIST BILL COMMENT Modified

RCDPE EOB WORKLIST CHANGE VIEW New

RCDPE EOB WORKLIST DIST ADJ Modified

RCDPE EOB WORKLIST FULL ACCT PROF Modified

RCDPE EOB WORKLIST MENU Modified

RCDPE EOB WORKLIST REESTABLISH Modified

RCDPE EOB WORKLIST REFRESH Modified

RCDPE EOB WORKLIST RESEARCH Modified

RCDPE EOB WORKLIST RESEARCH MENU Modified

RCDPE EOB WORKLIST SPLIT LINE Modified

RCDPE EOB WORKLIST TPJI Modified

RCDPE EOB WORKLIST VERIFY Modified

RCDPE ERA LIST VIEW ERA Modified

RCDPE ERA WORKLIST CHANGE VIEW New

RCDPE MARK FOR AUTOPOST New

RCDPE VIEW/PRINT WORKLIST EOB Modified

RCDPE VIEW/PRINT WORKLIST ERA Modified

RCDPE WORKLIST ERA LIST MENU Modified

RCDPE WORKLIST ERA SELECT Modified

RCDPE WORKLIST ERA SORT Modified

RCDPEX DELETE MESSAGE Modified

RCDPEX EOB_SUM EXCEPTION MENU Modified

RCDPEX EOB_SUM REMOVE EXCEPT Modified

RCDPEX RX_COMMENT New

RCDPEX SUM_EDIT CLAIM Modified

RCDPEX SUM_FILE EXCEPTION Modified

RCDPEX SUM_VIEW/PRINT MESSAGE Modified

VALM QUIT Modified

Security Keys Associated:

Security Key Name New/Modified/Deleted

----------------- --------------------

RCDPE AGED PMT New

RCDPE AUTO DEC New

RCDPE ERA EXCEPT New

RCDPE REMOVE EEOB New

List Templates:

List Template Name New/Modified/Deleted

------------------ --------------------

RCDPE APAR EEOB LIST New

RCDPE AUTO EOB RECEIPT PREVIEW New

RCDPE APAR EOB RESEARCH New

RCDPE APAR SELECTED EEOB New

RCDPE EOB RESEARCH Modified

RCDPE EOB WORKLIST Modified

RCDPE MISC REPORTS New

Templates Associated:

Template Name Type File Name (Number) New/Modified/Deleted

------------- ---- ------------------ --------------------

N/A

Parameters Associated:

Parameter Name New/Modified/Deleted

------------------ --------------------

RCDPE APAR New

RCDPE EDI LOCKBOX WORKLIST New

RCDPE SCRATCHPAD New

Additional Information: N/A

New Service Requests (NSRs):

-------------------------------------------------------------

NSR - Request id: 20110503 Electronic Data Interchange (EDI) New

Standards and Operating Rules (Veterans Health Administration)

VHA Provider-Side TCRs 05/19/2011

http://vista.med.va.gov/nsrd/ViewITRequest.asp?RequestID=20110503

Patient Safety Issues (PSIs)

-----------------------------

N/A

Remedy Ticket(s) & Overview:

----------------------------

N/A

Test Sites:

-----------

VA Puget Sound Health Care System

VA Southern Nevada Healthcare System (VASNHS) - Las Vegas

New Mexico VA Health Care System - Albuquerque

Tuscaloosa VA Medical Center

Central Alabama Veterans Health Care System (CAVHCS)

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview

------------------------------

N/A

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

-------------------------

This patch should take less than 5 minutes to install.

DO NOT QUEUE the installation of this patch.

To avoid disruptions, these patches should be installed during non-peak

hours when there is minimal activity on the system. Avoid times when ERAs

and EFTs are being received from the Financial Services Center (FSC). Of

particular concern is the option below.

TaskMan tasks will be queued at installation to perform post-installation

activities. When these tasks are complete the installer will receive

informational MailMan messages. No additional installation tasks will be

needed.

1\. Accounts Receivable Nightly Process Background Job

\[PRCA NIGHTLY PROCESS\]

Do not install the patch when the AR Nightly Process Background job is

running. Wait for this job to finish or complete the installation

before this job starts.

Pre-Installation Instructions

-----------------------------

1\. OBTAIN PATCHES

--------------

Obtain the host file BPS_IB_PRCA_EPAYMENTS_BUNDLE_1_0.KID, which

contains the following 3 patches:

PRCA\*4.5\*298

IB\*2.0\*511

BPS\*1.0\*17

Sites can retrieve VistA software from the following FTP addresses.

The preferred method is to FTP the files from:

REDACTED

This will transmit the files from the first available FTP server.

Sites may also elect to retrieve software directly from a specific

server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

The BPS_IB_PRCA_EPAYMENTS_BUNDLE_1_0.KID host file is located in

the \[anonymous.software\] directory. Use ASCII Mode when downloading

the file.

2\. USE KIDS TO INSTALL

-------------------

Use the Kernel Installation & Distribution System Menu option

\[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INStallation

---

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option:

3\. LOAD TRANSPORT GLOBAL FOR MULTI-BUILD

-------------------------------------

From the Installation menu, select the Load a Distribution option.

When prompted for "Enter a Host File:", enter the full directory path

where you saved the host file BPS_IB_PRCA_EPAYMENTS_BUNDLE_1_0.KID

(e.g., SYS\$SYSDEVICE:\[ANONYMOUS\]BPS_IB_PRCA_EPAYMENTS_BUNDLE_1_0.KID).

When prompted for "OK to continue with Load? NO//", enter "YES."

The following will display:

Loading Distribution...

Build PRCA\*4.5\*298 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES//

PRCA\*4.5\*298

Will first run the Environment Check Routine, PRCA298E

Checking for prerequisite patches Sep 25, 2014@18:31:09

BPS\*1.0\*11 installed

IB\*2.0\*447 installed

IB\*2.0\*451 installed

IB\*2.0\*452 installed

IB\*2.0\*488 installed

PRCA\*4.5\*138 installed

PRCA\*4.5\*208 installed

PRCA\*4.5\*220 installed

PRCA\*4.5\*222 installed

PRCA\*4.5\*233 installed

PRCA\*4.5\*241 installed

PRCA\*4.5\*249 installed

PRCA\*4.5\*253 installed

PRCA\*4.5\*261 installed

PRCA\*4.5\*262 installed

PRCA\*4.5\*269 installed

PRCA\*4.5\*271 installed

PRCA\*4.5\*276 installed

PRCA\*4.5\*283 installed

PRCA\*4.5\*284 installed

PRCA\*4.5\*293 installed

PRCA\*4.5\*296 installed

All prerequisite patches found.

IB\*2.0\*511

BPS\*1.0\*17

Use INSTALL NAME: BPS IB PRCA EPAYMENTS BUNDLE 1.0 to install this

Distribution.

4\. OPTIONAL INSTALLATION OPTIONS FOR MULTI-BUILD

---------------------------------------------

From the Installation menu, you may select to use the following 3

KIDS options

(when prompted for the INSTALL NAME, enter BPS IB PRCA EPAYMENTS

BUNDLE 1.0):

5 Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as data dictionaries or templates.

4 Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, data dictionaries, templates, etc.).

2 Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

5\. INSTALL MULTI-BUILD

-------------------

This is the step to start the installation of this KIDS patch. This

will need to be run for the BPS IB PRCA EPAYMENTS BUNDLE 1.0.

a\. Choose the Install Package(s) option to start the patch install.

b\. When prompted for the "Select INSTALL NAME:",

enter BPS IB PRCA EPAYMENTS BUNDLE 1.0

c\. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of

Install? YES//", enter YES unless your system does this in a

nightly TaskMan process.

d\. When prompted "Want KIDS to INHIBIT LOGONs during the install?

YES//", enter NO.

e\. When prompted " Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//", enter NO.

g\. When prompted "Device: HOME//", respond with the correct device

but do not queue this install.

> **NOTE:** You may see this informational message during installation

of the multi-build:

Not a known package or a local namespace

This is because the name of the multi-build doesn't match a

namespace in the PACKAGE file (#9.4).

Post-Installation Instructions

------------------------------

For production environments only:

After the distribution is installed the REDACTED mail address

must be added to the RCDPE AUDIT Mail Group as a REMOTE MEMBER if it's

not already there. This can be done via the Mail Group Edit

\[XMEDITMG\]option.

This can be verified by a FileMan inquiry to the MAIL GROUP file (#3.8).

You should see this in the Mail Group:

NAME: RCDPE AUDIT TYPE: public

ALLOW SELF ENROLLMENT?: NO

...

REMOTE MEMBER: REDACTED

In the DOMAIN file (#4.2) the Q-NPS.VA.GOV domain must exist and the

field 'FLAGS' must have a value of 'S'.

For example:

NAME: Q-NPS.VA.GOV FLAGS: S

RELAY DOMAIN: REDACTED.GOV DHCP ROUTING INDICATOR: NPS

DISABLE TURN COMMAND: YES

Please consult the MailMan documentation for additional information on

creating and editing Mail Groups and Domains.

Routine Information:

====================

The second line of each of these routines now looks like:

;;4.5;Accounts Receivable;\*\*\[Patch List\]\*\*;Jan 21, 2014;Build 111

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: PRCA298E

Before: n/a After: B2741517 \*\*298\*\*

Routine Name: PRCAP298

Before: n/a After:B109719472 \*\*298\*\*

Routine Name: RCBEADJ

Before: B63961627 After: B66159160 \*\*169,172,204,173,208,233,298\*\*

Routine Name: RCDPAYER

Before: B25868382 After: B26142929 \*\*269,276,298\*\*

Routine Name: RCDPE8NZ

Before: B56342604 After:B102784792 \*\*173,212,208,269,276,283,293,298\*\*

Routine Name: RCDPEAA1

Before: n/a After: B60672744 \*\*298\*\*

Routine Name: RCDPEAA2

Before: n/a After: B95635325 \*\*298\*\*

Routine Name: RCDPEAA3

Before: n/a After: B72680990 \*\*298\*\*

Routine Name: RCDPEAC

Before: B83292786 After:B163795465 \*\*208,269,276,298\*\*

Routine Name: RCDPEAD

Before: n/a After: B15979535 \*\*298\*\*

Routine Name: RCDPEADP

Before: n/a After: B82856652 \*\*298\*\*

Routine Name: RCDPEAP

Before: n/a After:B192874498 \*\*298\*\*

Routine Name: RCDPEAP1

Before: n/a After: B28791355 \*\*298\*\*

Routine Name: RCDPEAPP

Before: n/a After:B144741985 \*\*298\*\*

Routine Name: RCDPEAR1

Before:B126108337 After:B225062601 \*\*173,269,276,284,293,298\*\*

Routine Name: RCDPEAR2

Before: B63768101 After: B99664049 \*\*173,269,276,284,283,293,298\*\*

Routine Name: RCDPEARL

Before: n/a After: B31596491 \*\*298\*\*

Routine Name: RCDPEDA1

Before: B24558059 After: B3534 \*\*173,269,276,284,283,298\*\*

Routine Name: RCDPEDAR

Before:B115536602 After:B196389465 \*\*173,276,284,283,298\*\*

Routine Name: RCDPEM

Before: B58755837 After: B61345619 \*\*173,255,269,276,283,298\*\*

Routine Name: RCDPEM0

Before: B51750344 After: B72082268 \*\*173,208,220,298\*\*

Routine Name: RCDPEM2

Before:B188791112 After:B206109836 \*\*173,208,276,284,293,298\*\*

Routine Name: RCDPEM3

Before:B110558911 After:B177381909 \*\*276,284,298\*\*

Routine Name: RCDPEM4

Before:B186253544 After:B226302840 \*\*276,284,298\*\*

Routine Name: RCDPEM41

Before: n/a After: B8625925 \*\*298\*\*

Routine Name: RCDPEM5

Before: B72301084 After: B85031915 \*\*173,208,276,298\*\*

Routine Name: RCDPEM6

Before: B40220654 After: B78693035 \*\*276,298\*\*

Routine Name: RCDPEM7

Before: B44597294 After: B44920512 \*\*276,298\*\*

Routine Name: RCDPEM8

Before: B32433593 After: B32922579 \*\*276,298\*\*

Routine Name: RCDPEMA

Before: n/a After: B22679834 \*\*298\*\*

Routine Name: RCDPESP

Before: n/a After:B100040879 \*\*298\*\*

Routine Name: RCDPESP1

Before: n/a After: B30021822 \*\*298\*\*

Routine Name: RCDPESP2

Before: n/a After: B90155274 \*\*298\*\*

Routine Name: RCDPESP3

Before: n/a After: B6781847 \*\*298\*\*

Routine Name: RCDPESP4

Before: n/a After: B23109774 \*\*298\*\*

Routine Name: RCDPESR1

Before: B50545484 After: B49930663 \*\*173,214,208,202,271,298\*\*

Routine Name: RCDPESR2

Before: B85277265 After: B84502503 \*\*173,216,208,230,252,264,269,

271,298\*\*

Routine Name: RCDPESR3

Before: B55776988 After: B51416516 \*\*173,214,208,255,269,283,298\*\*

Routine Name: RCDPESR4

Before: B77733360 After: B80329387 \*\*173,216,208,230,269,271,298\*\*

Routine Name: RCDPESR6

Before: B43409269 After: B45550757 \*\*173,214,208,230,252,269,271,298\*\*

Routine Name: RCDPETT

Before: n/a After: B81520347 \*\*298\*\*

Routine Name: RCDPETTE

Before: n/a After:B258211138 \*\*298\*\*

Routine Name: RCDPETTF

Before: n/a After: B80402649 \*\*298\*\*

Routine Name: RCDPETTM

Before: n/a After:B189296632 \*\*298\*\*

Routine Name: RCDPETTP

Before: n/a After: B4906426 \*\*298\*\*

Routine Name: RCDPETTQ

Before: n/a After: B30669370 \*\*298\*\*

Routine Name: RCDPETTU

Before: n/a After:B117602125 \*\*298\*\*

Routine Name: RCDPEUPO

Before: n/a After: B40462165 \*\*298\*\*

Routine Name: RCDPEV

Before: B37749611 After: B38492428 \*\*208,138,298\*\*

Routine Name: RCDPEV0

Before: B24403974 After: B24203052 \*\*208,261,298\*\*

Routine Name: RCDPEWL

Before: B44600003 After: B68499983 \*\*173,208,269,298\*\*

Routine Name: RCDPEWL0

Before: B83670852 After:B153865640 \*\*173,208,252,269,298\*\*

Routine Name: RCDPEWL1

Before: B53027767 After: B68166367 \*\*173,208,222,298\*\*

Routine Name: RCDPEWL2

Before: B84334841 After: B85809764 \*\*173,208,269,298\*\*

Routine Name: RCDPEWL4

Before: B48717166 After: B46490209 \*\*173,208,269,298\*\*

Routine Name: RCDPEWL6

Before: B83585540 After: B80720367 \*\*173,208,222,276,298\*\*

Routine Name: RCDPEWL7

Before: B93160515 After: B96884750 \*\*208,222,269,276,298\*\*

Routine Name: RCDPEWL8

Before: B78778752 After: B82558343 \*\*208,269,276,298\*\*

Routine Name: RCDPEWLA

Before: B49000254 After: B59960871 \*\*173,208,298\*\*

Routine Name: RCDPEWLB

Before: B46624897 After: B49175831 \*\*208,298\*\*

Routine Name: RCDPEWLP

Before: n/a After:B164916639 \*\*298\*\*

Routine Name: RCDPEX

Before: B76642906 After: B80310750 \*\*173,208,269,298\*\*

Routine Name: RCDPEX1

Before: B15098572 After: B18257259 \*\*173,262,298\*\*

Routine Name: RCDPEX2

Before: B15963944 After: B22431438 \*\*173,269,298\*\*

Routine Name: RCDPEX31

Before: B37980620 After: B40819762 \*\*173,208,298\*\*

Routine Name: RCDPEX32

Before: B30120865 After: B48567496 \*\*173,249,298\*\*

Routine Name: RCDPEX4

Before: n/a After: B11626090 \*\*298\*\*

Routine Name: RCDPURE1

Before: B57024051 After: B60661584 \*\*114,148,153,169,204,173,214,

217,296,298\*\*

Routine Name: RCDPUREC

Before: B76306195 After:B104492015 \*\*114,148,169,173,208,222,293,298\*\*

Routine Name: RCMSITE

Before: B7163985 After: B8419776 \*\*173,236,253,298\*\*

Routine list of preceding patches: 138, 220, 233, 249, 253, 261, 262, 271

293, 296

*(This page included for two-sided copying.)*

# Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview of Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not able to be a “one size fits all.” The general strategy for VistA rollback is to repair the code with a follow-up patch. The development team recommends that sites log a Remedy ticket if it is a nationally released patch; otherwise, the site should contact the product development team directly for specific solutions to their unique problems.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA Installation Procedure of the KIDS build, the installer hopefully backed up the modified routines by the use of the ‘Backup a Transport Global’ action.  The installer can restore the routines using the MailMan message that were saved prior to installing the patch.  The backout procedure for global, data dictionary and other VistA components is more complex and will require issuance of a follow-up patch to ensure all components are properly removed. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with restoration of the data.  This backout may need to include a database cleanup process.

Please contact the Product Support team for assistance if the installed patch that needs to be backed out contains anything at all besides routines before trying to backout the patch.  If the installed patch that needs to be backed out includes a pre or post install routine please contact the Product Support team before attempting the backout.

From the Kernel Installation and Distribution System Menu, select

the Installation Menu.  From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch \#.

    a. Backup a Transport Global - This option will create a backup

       message of any routines exported with this patch. It will not

       backup any other changes such as DD's or templates.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure for VistA patches is complicated and may require a follow-up patch to fully roll back to the pre-patch state. This is due to the possibility of Data Dictionary updates, Data updates, cross references, and transmissions from VistA to offsite data stores.

Please contact the Product Support team for assistance if needed.

*(This page included for two-sided copying.)*

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following features in VistA, Integrated Billing are affected by this effort:

## System Feature: Site Parameters for Medical Auto-Post

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Site Parameters for Medical Auto-Post – Parameter for Auto-posting Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] contains a parameter question to allow sites to enable or disable auto-posting of third party medical claims with an initial default value of enabled.

> NUMBER OF DAYS EFT UNMATCHED: 5//

> NUMBER OF DAYS ERA UNMATCHED: 7//

> ENABLE AUTO-POSTING OF MEDICAL CLAIMS (Y/N): Y//

The question for auto-posting of medical claims comes after the two existing parameter questions.

The system initializes YES and the first default for auto-posting should be YES. After the user answers the question, that new answer is used as the next default value.

### Site Parameters for Medical Auto-Post – Notification of Edits for Parameter for Auto-posting Medical Claims 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system sends an Outlook email to distribution group REDACTED if a site changes the parameter question to enable or disable auto-posting of third party medical claims.

### Site Parameters for Medical Auto-Post – Parameter for Excluding Payers from Auto-posting of Medical Claims 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If auto-posting of third party medical claims is enabled for the site the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] contains a parameter question to allow sites to exclude specific payers from auto-posting of third party medical claims by selecting payer name or payer ID.

If auto-posting of medical claims is set to NO, excluded payers are not displayed and PAYER is not prompted.

If auto-posting of medical claims is set to YES and there be no excluded payers, the system displays a message and prompted for PAYER.

> NUMBER OF DAYS EFT UNMATCHED: 5//

> NUMBER OF DAYS ERA UNMATCHED: 7//

> ENABLE AUTO-POSTING OF MEDICAL CLAIMS (Y/N): Y//

> NO EXCLUDED PAYERS

> Select a Payer to add or remove from the exclusion list.

> PAYER:

If auto-posting of medical claims is set to YES and there are excluded payers, the system displays excluded payers and prompts for PAYER.

The system allows the user to enter a partial name and display matches by showing the name and the ID.

> ENABLE AUTO-POSTING OF MEDICAL CLAIMS (Y/N): Y//

> EXCLUDED PAYERS:

> INSURANCE OF ARIZONA 4444

> INSURANCE OF KANSAS 2222

> Select a Payer to add or remove from the exclusion list.

> PAYER: INSURANCE OF A

> 1 INSURANCE OF ALABAMA 3333

> 2 INSURANCE OF ARIZONA 4444

> CHOOSE 1-2: 2 INSURANCE OF ARIZONA 4444

> COMMENT: Comment goes here. Enter justification for Arizona.

> Insurance of Arizona - 4444 has been added to the list of Excluded Payers.

> If auto-decrease is turned on, this payer will be excluded from auto-decrease too.

Treat the PAYER prompt as a toggle. If the user enters a payer that is already listed, remove the payer from the list. If the user enters a payer that is not listed, add the payer to the list.

> EXCLUDED PAYERS:

> INSURANCE OF ARIZONA 4444

> INSURANCE OF KANSAS 2222

> Select a Payer to add or remove from the exclusion list.

> PAYER: INSURANCE OF KANSAS 2222

> COMMENT: Comment goes here. Enter justification for Kansas.

> Insurance of Kansas - 2222 has been removed from the list of Excluded Payers.

> If auto-decrease is turned on, this payer will no longer be excluded from auto-decrease.

> Select a Payer to add or remove from the exclusion list.

> PAYER: INSURANCE OF ALABAMA 3333

> COMMENT: Comment goes here. Enter justification for Alabama.

> Insurance of Alabama - 3333 has been added to the list of Excluded Payers.

> If auto-decrease is turned on, this payer will be excluded from auto-decrease too.

> Select a Payer to add or remove from the exclusion list.

When the user presses enter without entering a payer, list the excluded payers a second time if there were any changes to the list.

> Select a Payer to add or remove from the exclusion list.

> PAYER:

> EXCLUDED PAYERS:

> INSURANCE OF ALABAMA 3333

> INSURANCE OF ARIZONA 4444

If the user turns on auto-posting, excludes payers and turns auto-posting off, then keep the excluded payers but do not display the excluded payers unless auto-posting is turned on again.

### Site Parameters for Medical Auto-Post – Default Parameter for Excluding Payers from Auto-posting of Medical Claims 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] neither requires excluded payers nor contains default excluded payers.

### Site Parameters for Medical Auto-Post – Comment for Excluding Payers from Auto-posting of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] contains a comment question that is required if a user adds or removes a payer exclusion from auto-posting of third party medical claims.

### Site Parameters for Medical Auto-Post – Security Key for Parameter for Auto-posting of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] requires a user to hold security key RCDPE AUTO DEC to edit any parameter question concerning auto-posting of third party medical claims. The key is required at the menu option level.

### Site Parameters for Medical Auto-Post – Audit for Auto-posting of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system captures and maintains an audit trail of the user name, user initials, date, time, previous value, new value, and/or addition or deletion of payer exclusions for each edit of a parameter associated with auto-posting of medical claims.

## System Feature: Site Parameters for Medical Auto-Decrease

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Site Parameters for Medical Auto-Decrease – Parameter for Auto-decrease of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If auto-posting of third party medical claims is enabled for the site, the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] contains a parameter question to allow sites to enable or disable auto-decrease of third party medical claims, with an initial default value of disabled.

NUMBER OF DAYS EFT UNMATCHED: 5//

NUMBER OF DAYS ERA UNMATCHED: 7//

ENABLE AUTO-POSTING OF MEDICAL CLAIMS (Y/N): Y//

NO CURRENTLY EXCLUDED PAYERS

Select a Payer to add or remove from the exclusion list.

PAYER:

ENABLE AUTO-DECREASE OF MEDICAL CLAIMS (Y/N): N//

The first default for auto-decrease should be NO. After the user answers the question, that new answer is used as the next default value.

The question only displays if auto-posting of third party medical claims is enabled.

### Site Parameters for Medical Auto-Decrease – Parameter for Auto-decrease Timeframe of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If auto-decrease of third party medical claims is enabled for the site, the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] contains a parameter question to allow sites to specify the number of days to wait before an automatic decrease adjustment is made for a third party medical claim, with an initial default value of null and a required response of 0 to 7 days.

The question only displays if auto-decrease of third party medical claims is enabled.

The number of days are the number of days that have elapsed since auto-posting completed.

### Site Parameters for Medical Auto-Decrease – Parameter for Auto-decrease Amount of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If auto-decrease of third party medical claims is enabled for the site, the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] contains a parameter question to allow sites to specify the maximum claim dollar amount of an automatic decrease adjustment that is made for a third party medical claim, with an initial default value of null and a required response from 1 to 1500 dollars.

The question only displays if auto-decrease of third party medical claims is enabled.

The dollar amount is represented without cents.

ENABLE AUTO-DECREASE OF MEDICAL CLAIMS (Y/N): Y//

NUMBER OF DAYS TO WAIT BEFORE AUTO-DECREASE (0-7):

MAXIMUM DOLLAR AMOUNT TO AUTO-DECREASE (1-1500):

### Site Parameters for Medical Auto-Decrease – Parameter for Excluding Payers from Auto-decrease of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If auto-decrease of third party medical claims is enabled for the site, the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] contains a parameter question to allow sites to exclude specific payers from auto-decrease of third party medical claims by selecting payer name or payer ID.

The auto-decrease exclusion of payers work the same way as the auto-post exclusion of payers. Reference 2.6.1.3.

### Site Parameters for Medical Auto-Decrease – Default Parameter for Excluding Payers from Auto-decrease of Medical Claims 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] does not require payers nor contain default payers for the parameter question to allow sites to exclude specific payers from auto-decrease of third party medical claims.

### Site Parameters for Medical Auto-Decrease – Comment for Excluding Payers from Auto-decrease of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] contains a comment question that is required if a user adds or removes a payer exclusion from auto-decrease of third party medical claims.

### Site Parameters for Medical Auto-Decrease - Security Key for Parameter for Auto-decrease of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] requires a user to hold security key RCDPE AUTO DEC to edit any parameter question concerning auto-decrease of third party medical claims. The key will be required at the menu option level.

### Site Parameters for Medical Auto-Decrease - Audit for Auto-decrease of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system captures and maintains an audit trail of the user name, date, time, previous value, new value, and/or addition or deletion of payer exclusions for each edit of a parameter associated with auto-decrease of medical claims.

### Site Parameters for Pharmacy Auto-Post - Parameter for Auto-posting Pharmacy Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] displays an informational parameter to show that auto-posting for Pharmacy claims is disabled. This line is informational and cannot be edited.

NUMBER OF DAYS EFT UNMATCHED: 5//

NUMBER OF DAYS ERA UNMATCHED: 7//

ENABLE AUTO-POSTING OF MEDICAL CLAIMS (Y/N): N//

ENABLE AUTO-DECREASE OF MEDICAL CLAIMS (Y/N): N//

ENABLE AUTO-POSTING OF PHARMACY CLAIMS (Y/N): N

The informational parameter for auto-posting of pharmacy claims come after the auto-decrease of medical claims parameter questions.

## System Feature: Posting Prevention 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Posting Prevention - Posting Prevention for Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] contains a parameter question to allow sites to set the number of calendar days beyond which unposted medical payments (EFTs) will prevent the user from posting newer medical EFTs without posting the older payments first.

A value of 21 will be filed with the patch installation. The user can reset the value to a number between 14 and 99, inclusive, but the user cannot delete the value.

NUMBER OF DAYS EFT UNMATCHED: 5//

NUMBER OF DAYS ERA UNMATCHED: 7//

ENABLE AUTO-POSTING OF MEDICAL CLAIMS (Y/N): N//

ENABLE AUTO-DECREASE OF MEDICAL CLAIMS (Y/N): N//

ENABLE AUTO-POSTING OF PHARMACY CLAIMS (Y/N): N

NUMBER OF DAYS (AGE) OF UNPOSTED MEDICAL EFTS TO PREVENT POSTING: 21//

### Posting Prevention - Posting Prevention for Pharmacy Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] contains a parameter question to allow sites to set the number of calendar days beyond which unposted pharmacy payments (EFTs) will prevent the user from posting newer pharmacy EFTs without posting the older payments first.

A value of 999 is filed with the patch installation. The user can reset the value to a number between 21 and 999, inclusive, but the user cannot delete the value.

NUMBER OF DAYS EFT UNMATCHED: 5//

NUMBER OF DAYS ERA UNMATCHED: 7//

ENABLE AUTO-POSTING OF MEDICAL CLAIMS (Y/N): N//

ENABLE AUTO-DECREASE OF MEDICAL CLAIMS (Y/N): N//

ENABLE AUTO-POSTING OF PHARMACY CLAIMS (Y/N): N

NUMBER OF DAYS (AGE) OF UNPOSTED MEDICAL EFTS TO PREVENT POSTING: 21//

NUMBER OF DAYS (AGE) OF UNPOSTED PHARMACY EFTS TO PREVENT POSTING: 30//

## System Feature: Site Parameter Reporting - Report for Auto-processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Site Parameter Reporting - Report for Auto-processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SITE PARAMETER EDIT \[RCDPE SITE PARAMETER\] menu contains a new option of EDI Lockbox Parameters Report \[RCDPE SITE PARAMETER REPORT\] to display or print the EDI Lockbox Parameters.

### Site Parameter Reporting - Report for Auto-processing Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SITE PARAMETER EDIT \[RCDPE SITE PARAMETER\] menu contains two new options of EDI Lockbox Parameters Audit Report \[RCDPE SITE PARAMETER AUDIT REPORT\] and EDI Lockbox Exclusion Audit Report \[RCDPE SITE EXCLUSION AUDIT REPORT\] to display or print the EDI Lockbox Parameters audit.

### Site Parameter Reporting - Database for Payer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system includes a database of payer names, payer IDs, and the date on which the payer was added to the database, stored in such a way that allows for user selection of a name or payer ID.

### Site Parameter Reporting - Populate Database for Payer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system populates entries into the database using information from the ERA table.

### Site Parameter Reporting - Maintain Database for Payer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system maintains the database in such a way that new payers in the file ELECTRONIC REMITTANCE ADVICE (344.4) are available for user selection.

### Site Parameter Reporting - Add Exclusion of all Payers for IOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all new parameter questions that exclude by payer, the system provides field test sites to start testing with all payers excluded, filing with a user name of POSTMASTER and a comment of "Auto Addition - Beginning of Field Test / IOC". This addition of all payer exclusions is not available to sites after national release.

### Site Parameter Reporting - Remove Exclusion of all Payers for IOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all new parameter questions that exclude by payer, the system provides field-test sites to remove all payer exclusions, filing with a user name of POSTMASTER and a comment of "Auto Deletion - End of Field Test / IOC". This removal of all payer exclusions is not available to sites after national release.

### Site Parameter Reporting - Report for Payers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX REPORTS MENU \[RCDPE EDI LOCKBOX REPORTS MENU\] contains a new option of PAYER EXCLUSION NAME / ID REPORT \[RCDPE PAYER EXCLUSION NAME ID\] to show the payers, with columns for payer name, payer ID, and the date on which the payer was added to the database.

Select EDI Lockbox Reports Menu Option: Payer Exclusion Name / ID Report

DEVICE: HOME// UCX/TELNET Right Margin: 80//

PAYER EXCLUSION NAME / ID REPORT Page: 1

RUN DATE: 11/27/13@18:47:14

PAYER ID PAYER NAME DATE ADDED

===============================================================================

111111 PAYER NAME ONE 11/27/13

222222 PAYER NAME TWO 11/27/13

333333 PAYER NAME THREE 11/27/13

444444 PAYER NAME FOUR 11/27/13

Enter RETURN to continue or '^' to exit:

## ## System Feature: Transfer EEOB- Remove Transfer EEOB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Transfer EEOB- Remove Transfer EEOB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX 3RD PARTY EXCEPTIONS \[RCDPE EXCEPTION PROCESSING\] ListManager screen for Data Exceptions no longer contains the action Transfer EEOB; although, the coding executed by the action remains on the system.

### Transfer EEOB - Remove EEOB Transfer Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX REPORTS MENU \[RCDPE EDI LOCKBOX REPORTS MENU\] no longer contains the option EEOB TRANSFER REPORTS \[RCDPE EOB TRANSFER REPORTS\]; although, the coding executed by the option remains on the system.

## System Feature: Exception List- Security Key for Delete Message Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Exception List- Security Key for Delete Message Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX 3RD PARTY EXCEPTIONS \[RCDPE EXCEPTION PROCESSING\] action of Delete Message requires a new security key; RCDPE ERA EXCEPT.

### Exception List- Restrict Delete Message Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX 3RD PARTY EXCEPTIONS \[RCDPE EXCEPTION PROCESSING\] action of Delete Message displays an error message and returns the user to the main screen under the following condition:

ERA has a payment method of Automatic Clearing House (ACH)

Select EDI LBox EEOB Transmission Exception: 2

Deletion is not allowed. The ERA has a payment method of ACH.

### Exception List- Transfer Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system no longer displays the transfer message for data exceptions.

<u>LOCKBOX EEOB DATA EXCEPTIONS  Nov 27, 2013@16:01:40          Page:    2 of    2</u>

                   EEOB DETAIL DATA WITH EXCEPTION CONDITIONS

  \#   Trace \#                                                          EOB Date

<u>+       Insurance Co Name/ID                                                   </u>

 7     999999995523333333                                               9/20/10 

        FEDERAL EMPLOYEES HEALTH /1382242132                                   

      Seq \#: 1    Bill: \*ECME1234566  Pt: PUBLIC,JOHN Q        Pd: 12.24       

          \*\*Exception: VALID BILL NOT FOUND (TRANSFER NEEDED IF NOT YOURS)     

### Exception List- Filter Question 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system has a filter question for medical or pharmacy before displaying the exceptions.

INCLUDE EXCEPTIONS FOR (M)EDICAL, (P)HARMACY, OR (B)OTH

### Exception List- Pharmacy Claim Comment Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX 3RD PARTY EXCEPTIONS \[RCDPE EXCEPTION PROCESSING\] screen for data exceptions contains an action for Pharmacy Claim Comment that allows a user to enter a one line comment for a non-released prescription.

<u>View/Print Message Transfer EEOB Pharmacy Claim Comment</u>

<u>File EEOB in IB Edit Claim \# Exit</u>

<u>Remove Exception TPJI</u>

<u>Select Action: Next Screen// ph Pharmacy Claim Comment</u>

<u>Select EDI LBox EEOB Data Exception(s): (1-4): 2</u>

<u>Selection \#: 2 7777777</u>

<u>Comment: This is a pharmacy comment for bill \#7777777 that will display on the screen.</u>

Only the most recent comment is stored and displayed.

### Exception List- Display Pharmacy Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX 3RD PARTY EXCEPTIONS \[RCDPE EXCEPTION PROCESSING\] screen for data exceptions displays the following for pharmacy claims: ECME number, release date, comment.

<u>LOCKBOX EEOB DATA EXCEPTIONS Dec 18, 2013@08:57:36 Page: 1 of 3</u>

<u>EEOB DETAIL DATA WITH EXCEPTION CONDITIONS</u>

<u>\# Trace \# EOB Date</u>

<u>--------Insurance Co Name/ID----------------------------------------------------</u>

<u>1 63025</u>

<u>AETNA/1234567890</u>

<u>Seq \#: 2 Bill: \*7777777 Pt: ARPATIENT,ONE Pd: 43.36</u>

ECME \#: 76523098 Release Date: 12/16/10

<u>Comment: Pharmacy comment goes here.</u>

<u>\*\*Exception: VALID BILL NOT FOUND (TRANSFER NEEDED IF NOT YOURS)</u>

### Exception List – Allow Suspense in Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX 3RD PARTY EXCEPTIONS \[RCDPE EXCEPTION PROCESSING\] screen for data exceptions shall allow an entry that is not a valid A/R Bill for the Edit Claim \# action.  The Edit Claim \# action currently removes the EEOB from the exception list and will continue to function that way.

>     View/Print Message        Edit Claim \#              Exit

>     File EEOB in IB           TPJI

>     Remove Exception          Pharmacy Claim Comment

> Select Action: Next Screen// ED   Edit Claim \# 

> Select EDI LBox EEOB Data Exception(s):  (96-99): 97

> Selection \#: 97     4343434

> Select A/R Bill this EEOB is actually paying on: SUSPENSE

>    THIS CLAIM WAS NOT FOUND IN YOUR AR.  DO YOU WANT TO CONTINUE?: NO// YES

> EEOB Filed.

> PRESS RETURN TO CONTINUE

## ## System Feature: Verification of EEOB Detail against Bill Detail 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Verification of EEOB Detail against Bill Detail - Remove Case Sensitivity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system automatically performs verification of the EEOB detail against the bill detail without regard to case sensitivity for the first five characters of the patient's last name, date of service, bill number or claim number, social security number or patient ID, and the amount billed.

## System Feature: EEOB Worklist 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EEOB Worklist - Remove Adjust (Inc/Dec) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] no longer contains the action Adjust (Inc/Dec) on the Research Menu ListManager screen; however, the coding executed by the action remains on the system.

### EEOB Worklist - Exception Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays an "x" indicator before the ERA number on the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] if any exception exists for the ERA.

There is no need to display "-" with the indicator for an exception. Once the exception is resolved, the indicator of “x” no longer displays and the “-“displays next to the ERA number to indicate that there is no scratchpad.

\# ERA \# TRACE#

<u>PAYER NAME/MATCH STATUS ERA PAID DT TOT AMT PAID DT REC'D</u>

1 x4667 000032974

3/31/05 7.46 3/31/05

THE COMMUNITY HOSPITAL APPROX \# EEOBs: 1

### EEOB Worklist - Exception Error Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a data exception exists for a medical ERA, the system denies a user access to select that medical ERA from the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] by displaying the following message, requiring the user to press enter to continue and return the user to the Worklist display:

ACCESS DENIED: Scratchpad creation is not allowed when Exceptions exist. Fix Transmission Exceptions first and then Data Exceptions via the EXC EDI Lockbox 3rd Party Exceptions option, located on the EDI Lockbox Main Menu.

Press enter to continue.

### EEOB Worklist – Warning for View/Print ERA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a data exception exists for a medical ERA, the system shall display a warning for action View/Print ERA on the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] by displaying the following message, requiring the user to press enter to continue before viewing and/or printing:

> WARNING: Fix Transmission Exceptions first and then Data Exceptions via the EXC EDI Lockbox 3rd Party Exceptions option, located on the EDI Lockbox Main Menu.

> Press enter to continue.

### EEOB Worklist - Posting Warning for Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are un-posted payments (EFTs) associated with third party medical claims more than 14 calendar days old, the system displays a warning message for action Select ERA on the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\], requiring the user to press enter to continue:

> **WARNING:** Unposted EFTs exist that are more than 14 days old. Post the older payments first. The EFTs may be matched or unmatched.

Trace#, Trace#, Trace#

Press enter to continue.

Unmatched EFTs, since they have not yet been matched with an ERA record, are handled as though they are associated with third party medical claims.

Does not consider EFTs that are older than two months prior to national release..

An EFT is no longer considered for posting prevention under either of the following conditions:

- The EFT is matched to an ERA with a detail post status of POSTED.
- The EFT is matched to a paper EOB and the status of the receipt is processed.

### EEOB Worklist - Posting Prevention for Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are un-posted payments (EFTs) associated with third party medical claims, aged more than the number of days specified in site parameters, the system displays an error message for action Select ERA on the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\], requiring the user to press enter:

ERROR: Unposted EFTs exist that are more than 21 days old. Scratchpad creation is not allowed for newer payments. Post older payments first. The EFTs may be matched or unmatched.

Trace#, Trace#, Trace#

Press enter to continue.

If the user has selected an ERA that is 14 days or older, the user can create the scratchpad.

If an override exists, the user can create the scratchpad.

If the user has selected an ERA that has been received within 14 days and there is no override, the user is returned to the ListManager screen.

Unmatched EFTs, since they have not yet been matched with an ERA record, are handled as though they are associated with third party medical claims.

Does not consider EFTs that are older than two months prior to national release.

An EFT is no longer considered for posting prevention under either of the following conditions:

- The EFT is matched to an ERA with a detail post status of POSTED.
- The EFT is matched to a paper EOB and the status of the receipt is processed.

### EEOB Worklist - Posting Warning for Pharmacy Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are un-posted payments (EFTs) associated with pharmacy claims more than 21 calendar days old, the system displays a warning message for action Select ERA on the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\], requiring the user to press enter to continue:

> **WARNING:** Unposted EFTs exist for pharmacy claims that are more than 21 days old. Post the older payments first.

Trace#, Trace#, Trace#

Press enter to continue.

Does not consider EFTs that are older than two months prior to national release.

An EFT is no longer considered for posting prevention under either of the following conditions:

- The EFT is matched to an ERA with a detail post status of POSTED.
- The EFT is matched to a paper EOB and the status of the receipt is processed.

### EEOB Worklist - Posting Prevention for Pharmacy Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are un-posted payments (EFTs) associated with pharmacy claims, aged more than the number of days specified in site parameters, the system displays an error message for action Select ERA on the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\], requiring the user to press enter to continue:

ERROR: Unposted EFTs exist for pharmacy claims that are more than 30 days old. Scratchpad creation is not allowed for newer payments. Post older payments first.

Trace#, Trace#, Trace#

Press enter to continue

If the user has selected an ERA that is 21 days or older, the user can create the scratchpad.

If an override exists, the user can create the scratchpad.

If the user has selected an ERA that is has been received within 21 days and there is no override, the user is returned to the ListManager screen.

Does not consider EFTs that are older than two months prior to national release.

An EFT is no longer considered for posting prevention under either of the following conditions:

- The EFT is matched to an ERA with a detail post status of POSTED.
- The EFT is matched to a paper EOB and the status of the receipt is processed.

### EEOB Worklist - Rename the Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] is renamed to ERA WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\].

### EEOB Worklist - Split/Edit Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system transfers the correct payer information when splitting or editing an EEOB with different payer names. The correct payer information matches the information sent with the ERA.

### EEOB Worklist - View/Print ERA Displays ECME Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays the ECME number for pharmacy claims for action View/Print ERA on the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\].

EDI LOCKBOX WORKLIST - ERA DETAIL                 1/30/14        Page: 1

========================================================================

  \*\*ERA SUMMARY DATA\*\*

TRACE NUMBER: B0055713489                INSURANCE CO ID: 1731128555

ERA DATE: FEB 01, 2011                   TOTAL AMOUNT PAID: 21.24

PAYMENT FROM: UNITED AMERICAN INSURANCE COMPANY

FILE DATE/TIME: FEB 02, 2011@18:18:56 

EFT MATCH STATUS: MATCHED TO PAPER CHECK

ERA TYPE: ERA                            INDIVIDUAL EOB COUNT: 1

MAIL MESSAGE: 3519245                    CHECK \#: B0055713489

DETAIL POST STATUS: NOT POSTED           EXPECTED PAYMENT METHOD CODE: CHK

  \*\*EEOB DETAIL DATA\*\*

SEQUENCE \#: 1                            EOB DETAIL: K100U6D

AMOUNT PAID: 21.24                     

INSURANCE COMPANY ON BILL: UNITED AMERICAN INS CO

FREE TEXT PATIENT NAME: xxxxxxx,xxxxxxx

PATIENT: xxxxxxxxxx,xxxxxxxx/XXXX           CLAIM \#: 442-K100U6D

ECME \#:  123456789121

                             

\*\*EOB PROVIDER(S)/NPI                  CLAIM PROVIDER(S)/NPI\*\*

Enter RETURN to continue or '^' to exit:

### EEOB Worklist - Remove Batch Question

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] action to Select ERA no longer allows the user to split the ERA into batches.

### EEOB Worklist - Remove Hide/Display Batch Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] no longer contains the action Hide/Display Batch; however, the coding executed by the action shall remain on the system.

### EEOB Worklist - User-Entered Pharmacy Comment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays the user-entered pharmacy comment for action View/Print ERA on the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\].

## System Feature: Unposted Payment Override 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Unposted Payment Override - New Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system contains new option UNPOSTED EFT OVERRIDE \[RCDPE UNPOSTED EFT OVERRIDE\] that is available to user who holds security key RCDPE AGED PMT.

### Unposted Payment Override – New Option Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

UNPOSTED EFT OVERRIDE \[RCDPE UNPOSTED EFT OVERRIDE\] shall display current error and/or warning messages, prompt the user to override for Medical or Pharmacy and require an override reason.

> Current Warning and/or Error messages for Unposted EFTs:

> WARNING: Unposted EFTs exist for pharmacy claims that are

> more than 21 days old.

> ERROR: Unposted EFTs exist for third party medical claims that are

> more than 21 days old. Scratchpad creation is not allowed for newer

> payments.

> An override will allow unrestricted scratchpad creation for one day.

> Do you want to continue (Y/N)?

> Override for (M)edical or (P)harmacy?

> Reason for Override:

> File comment, the user name and date/time stamp.

> The override is not payer specific.

### Unposted Payment Override - Outlook Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system sends an Outlook message when an override occurs, using distribution groups specified when the patch is installed into production.

Subject: EDI LBOX-STA# 500-Unposted EFTs Override  11/15/13@19:02

Current Warning and/or Error messages for Unposted EFTs:

> **WARNING:** Unposted EFTs exist for pharmacy claims that are

more than 21 days old.

ERROR: Unposted EFTs exist for third party medical claims that are

more than 21 days old. Scratchpad creation is not allowed for newer

payments.

Medical Override Details

User: Lastnm, Firstnm

Date/Time: 11/15/13@19:00

Reason for Override: Short staffed due to event XYZ

## ## System Feature: Select ERA Question

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Select ERA Question- Select ERA Question

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] action to Select ERA displays the following question, with no default, when a user selects an ERA that does not have a scratchpad:

NO WORKLIST SCRATCHPAD ENTRY EXISTS FOR THIS ERA

(C)REATE SCRATCHPAD, (V)IEW ERA DETAILS or (E)XIT:

### Select ERA Question- Create Scratchpad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The action to Select ERA creates a scratchpad using existing functionality, if the user selects CREATE SCRATCHPAD.

### Select ERA Question- View ERA Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The action to Select ERA executes the functionality for action VIEW/PRINT ERA, if the user selects VIEW ERA DETAILS and does not create a scratchpad.

### Select ERA Question- Exit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The action to Select ERA returns the user to the EEOB Worklist, if the user selects EXIT or presses enter without a selection or enters "^".

## System Feature: EEOB Worklist Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EEOB Worklist Filter- Change View Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] ListManager screen contains a new action, Change View, to filter the data displayed, based on the user's response to the Change View questions.

The Change View action is specific to a user.

### EEOB Worklist Filter- Move Current Filter Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action contains the following questions instead of prompting the user each time the worklist is accessed:

ERA POSTING STATUS: UNPOSTED//

ERA-EFT MATCH STATUS: BOTH//

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: ALL//

The question of “(L)ist or (S)pecific” is displayed each time a user accesses the worklist.

The question of “LIMIT THE SELECTION TO A DATE RANGE WHEN THE ERA WAS RECEIVED” is displayed each time a user accesses the worklist.

### EEOB Worklist Filter- Auto-Posting, Non-Auto-Posting or Both

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action contains a question for Auto-posting, Non-Auto-posting or Both:

DISPLAY (A)UTO-POSTING, (N)ON AUTO-POSTING, OR (B)OTH: B//

### EEOB Worklist Filter- Medical, Pharmacy or Both

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action contains a question for Medical, Pharmacy or Both:

(M)EDICAL, (P)HARMACY, OR (B)OTH: M//

### EEOB Worklist Filter- Preferred View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action contains a required question to save as a preferred view and store the answers to the Change View questions if the user answers "Y":

DO YOU WANT TO SAVE THIS AS YOUR PREFERRED VIEW (Y/N)?:

The preferred view is specific to a user.

### EEOB Worklist Filter- Preferred View Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user selects the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] option, the system executes the Change View action if the user does not have a preferred view.

### EEOB Worklist Filter- Filter Displayed in Heading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] ListManager screen displays a line at the top of the heading to indicate the Change View display selected by the user:

SELECTED: MATCH STATUS: BOTH POST STATUS: UNPOSTED

DATE RANGE : NONE SELECTED AUTO-POSTED & NON AUTO-POSTED

MEDICAL & PHARMACY CLAIMS

ALL PAYERS

## ## System Feature: ERA Unmatched Aging Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ERA Unmatched Aging Report - Exception Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays an "x" indicator before the AGED DAYS on the ERA UNMATCHED AGING REPORT \[RCDPE ERA AGING REPORT\] if an exception exists for the ERA.

AGED

DAYS TRACE \#

PAYMENT FROM/ID ERA DATE

FILE DATE AMOUNT PAID EEOB CNT ERA \#

===========================================================================

TOTALS:

NUMBER AGED ELECTRONIC ERA MESSAGES FOUND: 80

AMOUNT AGED ELECTRONIC ERA MESSAGES FOUND: \$69,971.16

===========================================================================

x3147 850392408

CONNECTICUT GENERAL LIFE INSURANCE/1060303370 4/5/05

4/8/05 58.69 3 4843

EEOB Seq \#: 1 EEOB on file for K502DDI 3.39

EEOB Seq \#: 2 EEOB on file for K502C5V 24.61

## ## System Feature: Scratchpad Filter- Change View Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scratchpad Filter- Change View Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad ListManager screen contains a new action, CV Change View, to filter the data displayed, based on the user's response to the Change View questions.

The Change View action is specific to a user.

### Scratchpad Filter- Order of Payments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action contains a question for Order of Payments instead of prompting the user each time the scratchpad is accessed:

ORDER OF PAYMENTS: NO ORDER//

### Scratchpad Filter- Unposted Lines or All Lines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action contains a question which only applies to auto-posted ERAs for display of un-posted EEOBs, posted EEOBs or all EEOBs:

DISPLAY FOR AUTO-POSTED ERAS: (U)NPOSTED EEOBS, (P)OSTED EEOBS, OR (A)LL : U//

### Scratchpad Filter- Zero Payments Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action contains a question to order zero payments:

ORDER OF PAYMENTS: ZERO-PAYMENTS FIRST// ?

Enter the code corresponding to the sort order the user last used when

accessing the worklist entry.

Choose from:

N        NO ORDER

F        ZERO-PAYMENTS FIRST

L        ZERO-PAYMENTS LAST

ORDER OF PAYMENTS: ZERO-PAYMENTS FIRST//

### Scratchpad Filter- Preferred View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action contains a required question to save as a preferred view and store the answers to the Change View questions if the user answers "Y":

DO YOU WANT TO SAVE THIS AS YOUR PREFERRED VIEW (Y/N)?:

### Scratchpad Filter- Preferred View Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user selects an ERA from the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\], the system executes the Change View action if the user does not have a preferred view.

### Scratchpad Filter- Filter Displayed in Heading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad ListManager screen displays a line at the top of the heading to indicate the Change View display selected by the user:

View: No order, auto-posing, un-posted lines, zero payments.

## System Feature: Scratchpad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scratchpad- Remove Batch Maintenance Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad ListManager screen no longer contains the action Batch Maintenance; however, the coding executed by the action shall remain on the system.

### Scratchpad- Remove Research Menu Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad ListManager screen for Research Menu no longer contains the actions Release Hold, On Hold List, and Claims Match Rpt; however, the coding executed by the actions remain on the system.

### Scratchpad- Ignore Payment Retraction Pairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad ignores payment retraction pairs for claims when the following conditions are met, without regard to case sensitivity:

- Payment/Retraction pair is in the same ERA
- The first 5 characters of the patient's last name match
- The dates of service match
- The bill numbers or claim numbers match
- The social security numbers or patient IDs match

The amounts billed sum to zero, such as +5 and -5.

The payment/retraction pairs are displayed in TPJI.

### Scratchpad- Pharmacy Fees

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad automatically process’s fees at a line level.

### Scratchpad- EEOB Screen Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For pharmacy claims, The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad ListManager screen displays ECME \#, prescription number, fill number, release status, and date of service.

<u>EEOB Worklist/Scratch Pad     Jan 14, 2014@20:17:44          Page:    1 of    1</u>

ERA Entry \#: 87705 Total Amt Pd: 3127.85

Payer Name/ID: ANTHEM BCBS OF WISCONSIN/1390138065

PAPER CHECK \#: 6952887

                                                                               

1       EEOB Seq \# On ERA: ADJ1   Net Payment Amt: -1.10                       

       1.001\*\*\*ADJUSTMENT AT ERA LEVEL                                          

         Payment Amt: 0.00   Total Adjustments: -1.10  Net: -1.10              

         ADJUSTMENTS:                                                          
           1.  Non-specific retraction (ref# LATE CHARGE ): -1.10              

.............................................................................. 

2       EEOB Seq \# On ERA: 1   Net Payment Amt: 12.24                          

       2.001 Claim \#: 000111 Patient/Last 4:                                   

         Claim Bal: 0.00   Billed Amt: 0.00   Amt To Post: 12.24               

         Svc Dt: 10/26/89  COB: NO   Rx Copay: NON-EXEMPT  Means Tst: ??       

         Payment Amt: 12.24   Total Adjustments: 0.00  Net: 12.24

        ECME \#:  76523098

Rx/Fill/Release Status: 1234567/1/Released

DOS: 1/4/13

              

### Scratchpad- Display Auto-Posted ERA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad ListManager screen and Worklist Research screen displays auto-posted ERAs with a receipt at the EEOB level and an Auto-Post Date at the ERA level that is only displayed when the ERA is completely posted.

### Scratchpad- Unavailable Actions for Auto-Posted ERA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad ListManager screen makes the following actions unavailable for auto-posted ERAs:

- Split/Edit a Line
- Distribute Adj Amts
- Refresh Scratch Pad
- Verify

### Scratchpad- Available Actions for Auto-Posted ERA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad ListManager screen makes the following actions available for auto-posted ERAs and will behave as non-auto posted ERAs that have receipts.

- Review Line
- EOB View/Print EEOB
- ERA View/Print ERA
- Exit

### Scratchpad- Look at Receipt Action for Auto-Posted ERA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] scratchpad ListManager screen makes available the action to Look at Receipt, with the following behavior:

- Receipt number displays at the EEOB level
- The user must select the receipt to view and only one receipt is displayed at one time
- The action is not available for un-posted EEOBs that are part of an auto-posted ERA

## System Feature: Auto-Decrease for Medical Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto-Decrease for Medical Claim- Decrease Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system has a background job that automatically makes a decrease adjustment to the claim for the EEOB of a medical claim if the following criteria are met:

- Auto-posting of third party medical claims is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\]
- The payer is not excluded from auto-posting of third party medical claims in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] and the EEOB is auto-posted
- Auto-decrease of third party medical claims is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\]
- The payer is not excluded from auto-decrease of third party medical claims in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\]
- The number of days since the EEOB was posted is equal to or greater than the number of days specified in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\]
- The residual balance on the EEOB is equal to or less than the dollar amount maximum specified in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\]
- The claim has not been referred to regional council or general council

### Auto-Decrease for Medical Claim- File for Medical Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system files a contractual decrease adjustment for a medical claim and record the following:

- User - Postmaster
- Comment - Auto-Decrease Adjustment, Medical
- Date/Time Stamp
- Transaction Type – Decrease Adjustment

### Auto-Decrease for Medical Claim- Decrease Claim Amount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system makes a contractual decrease adjustment with an adjustment amount that brings the claim balance to zero.

### Auto-Decrease for Medical Claim- Auto-Decrease Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX REPORTS MENU \[RCDPE EDI LOCKBOX REPORTS MENU\] contains a new option of AUTO-DECREASE ADJUSTMENT REPORT \[RCDPE AUTO DECREASE REPORT\] which shows automatic decrease adjustments that have been applied.

The user is able to sort and/or select an Excel format.

Select EDI Lockbox Reports Menu Option: DC Auto Decrease Adjustment Report

Select division: ALL//

SORT BY OR (C)LAIM \#, (P)AYER or PATIENT (N)AME?: CLAIM//PATIENT NAME

SORT PATIENT NAME (F)IRST TO LAST OR (L)AST TO FIRST?: FIRST TO LAST//

START DATE: t (NOV 27, 2013)

END DATE: NOV 27,2013// t (NOV 27, 2013)

EXPORT THE REPORT TO Microsoft Excel (Y/N): ? NO//

DEVICE: HOME// UCX/TELNET Right Margin: 80//

EDI LOCKBOX AUTO DECREASE ADJUSTMENT REPORT Page: 1

RUN DATE: 11/27/13@18:47:14

DIVISIONS: ALL

DATE RANGE: 11/27/13 - 11/27/13 (Date Decrease Applied)

CLAIM \# PATIENT NAME Payer DECREASE AMT DATE CARC

========================================================================

500-K111111 ARPATIENT, ONE Payer One 1.00 11/27/13 23

500-K222222 ARPATIENT, TWO Payer Two 1.77 11/27/13

500-K333333 ARPATIENT, THREE Payer Three 2.00 11/27/13 100

500-K444444 ARPATIENT, FOUR Payer Four .50 11/27/13 100

\*\*TOTALS FOR DATE: 11/27/13 \# OF DECREASE ADJUSTMENT: 4

TOTAL AMOUNT OF DECREASE ADJUSTMENTS: \$5.27

\*\*\*\* TOTALS FOR DATE RANGE: \# OF DECREASE ADJUSTMENT: 4

TOTAL AMOUNT OF DECREASE ADJUSTMENTS: \$5.27

Enter RETURN to continue or '^' to exit:

## ## System Feature: Auto-Posting Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto-Posting Medical Claims- Auto-Posting Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system auto-posts for medical claims when the following conditions are met:

- Auto-posting is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\]
- The EEOB payer is not excluded from auto-posting in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\]
- The Electronic Remittance Advice (ERA) does not have an exception
- The ERA does not contain interest
- The ERA does not contain an adjustment
- The Electronic Fund Transfer (EFT) and ERA are matched
- The EFT has been accepted by Financial Management System (FMS)
- The ERA negative payments all have a matching positive payment (+/- pairs)

### Auto-Posting Medical Claims- Create and Process Receipt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system creates a receipt and processes that receipt for medical claims when the following conditions are met:

- The ERA negative payments all have a matching positive payment (+/- pairs)
- The EEOB detail has been verified against bill detail
- The claim balance covers payment to be posted for all EEOBs
- The claim status is open for all EEOBs
- The claim has not been referred to regional council or general council
- The claim has not been terminated as a write off, indicated by a “WO” claim status

### Auto-Posting Medical Claims- Auto-Posting Awaiting Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system sends an EEOB line to the Auto-Post Awaiting Resolution list when the conditions are met for auto-posting but at least one condition is not met to create and process a receipt.

Stores the reason the EEOB line is sent to the Auto-Post Awaiting Resolution list.

## System Feature: Auto-Posting 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto-Posting - Run Nightly

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The auto-posting process runs nightly and processes receipts, including EEOBs that were previously on the Auto-Post Awaiting Resolution list but are now in a state that can be processed. Once processing completes, the receipts continue to show up on reports as if a user processed the receipts.

### Auto-Posting - Receipt Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system creates a receipt for all EEOBs that can be auto-posted, even if all EEOBs in an ERA cannot be posted at the same time.

If all EEOBs in an ERA can be posted, there is no change to the way the receipt number is generated.

If only some of the EEOBs in an ERA can be posted, the receipt number has an alphabetic character on the end, starting with “A” and proceeding in order until all EEOBs have been posted. The base number stays the same.

Example \#1

ERA has 10 lines

Auto-Posting Day \#1

All lines are posted and the receipt number is E1234.

Example \#2

ERA has 10 lines

Auto-Posting Day \#1

The first 3 lines are posted and the receipt number is E1234A.

Auto-Posting Day \#2

The next 2 lines are posted and the receipt number is E1234B.

Auto-Posting Day \#3

The remaining 5 lines are posted and the receipt number is E1234C.

### Auto-Posting - EEOB Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] displays an "A" indicator before the ERA number if auto-posting is complete for that ERA.

\# ERA \# TRACE#

<u>PAYER NAME/MATCH STATUS ERA PAID DT TOT AMT PAID DT REC'D</u>

1 A4667 000032974

3/31/05 7.46 3/31/05

THE COMMUNITY HOSPITAL APPROX \# EEOBs: 1

### Auto-Posting - Ignore Payment Retraction Pairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system ignores payment retraction pairs for medical claims when the following conditions are met, without regard to case sensitivity:

- Payment/Retraction pair is in the same ERA
- The first 5 characters of the patient's last names match
- The dates of service match
- The bill numbers or claim numbers match
- The social security numbers or patient IDs match
- The amounts billed sum to zero, such as +5 and -5

### Auto-Posting - Status Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system makes the following status changes when a medical claim is successfully auto-posted:

Claim Status - Collected/Closed or Open (with residual balance)

Receipt Status – Closed

Detail Post Status – Posted or Posted Incomplete

Detail Post Status becomes Posted when all lines have been posted. Detail Post Status becomes Posted Incomplete if some lines have been posted but not all.

### Auto-Posting - AR Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays the auto-posted transactions within Accounts Receivable in the same manner as a manually posted transaction.

### Auto-Posting - FMS Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system continues to build data transactions to send to FMS using the same data format and structure that was used prior to the auto-post enhancements.

### Auto-Posting - Auto-Post Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX REPORTS MENU \[RCDPE EDI LOCKBOX REPORTS MENU\] contains a new option of AUTO POST REPORT \[RCDPE AUTO POST REPORT\] to displayed information for auto-posted transactions.

## System Feature: Match to ECME Claim 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Match to ECME Claim- Match to ECME Claim for Correct Fill 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system matches the 835 to the correct ECME claim for the correct pharmacy fill.

## System Feature: Auto-Post Awaiting Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto-Post Awaiting Resolution- Screen Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AUTO-POST AWAITING RESOLUTION \[RCDPEAPAR\] option displays EEOB line items from one to many ERAs in a ListManager format, removing an EEOB line item after a receipt has been created and processed or marked for auto-post.

<u>AUTO-POST - AWAITING RESOLUTION Nov 19, 2013@21:37:21 Page: 1 of 2</u>

Filter: ALL PAYERS, MEDICAL

ERA#.Seq Claim# Post Amt Post Date Un-Post Bal

Payer Name/ID

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u> 1 87705.1 K307YUC 3000.41 11/1/13 127.44

ANTHEM BCBS OF WISCONSIN/1390138065

2 87705.2 K307740 3000.41 11/1/13 127.44

ANTHEM BCBS OF WISCONSIN/1390138065

3 87721.1 K301PVD 439.41 11/3/13 39.36

AETNA/1066033492

4 87789.1 K301PVV 2004.09 11/19/13 75.90

BLUE CROSS ANTHEM/106876219

Select EEOB View/Print ERA Exit

CV Change View

Select Action: Next Screen//

### Auto-Post Awaiting Resolution- Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the ListManager screen and behave like actions on the existing worklist:

- Select EEOB
- View/Print ERA
- CV Change View
- Verify
- Exit

### Auto-Post Awaiting Resolution- All Payers or Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AUTO-POST AWAITING RESOLUTION \[RCDPE AUTO-POST AWAITING RESOLUTION\] option displays a question to select payers before showing the ListManager screen:

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: ALL//

## System Feature: Auto-Post Awaiting Resolution EEOB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto-Post Awaiting Resolution EEOB- EEOB Screen Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays the EEOB detail when a user selects the Select EEOB action.

Only the unposted lines display.

The user returns to the Auto-Post Awaiting Resolution screen after exiting the EEOB display.

<u>AWAITING RESOLUTION – Selected EEOB - Scratch Pad Nov 19, 2013@21:37:21 Page: 1 of 2</u>

ERA Entry \#: 87705 Total Amt Pd: 3127.85

Posted Amt: 3000.41 Un-posted balance: 127.44

Payer Name/ID: ANTHEM BCBS OF WISCONSIN/1390138065

EFT \#/TRACE \#: 1737/CC13312873

POSTED RECEIPT \#(s): E123838

EEOB Seq \# On ERA: 7 Net Payment Amt: 69.17

6.001 Claim \#: K307YUC Patient/Last 4: TEST,PATIENT ONE/7017

Claim Bal: 69.17 Billed Amt: 69.17 Amt To Post: 69.17

Svc Dt: 1/4/13 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 69.17 Total Adjustments: 0.00 Net: 69.17

APAR Reason: Not Verified

\+ Enter ?? for more actions

Split/Edit A Line EOB View/Print EEOB

Mark for Auto-Post Review Line ERA View/Print ERA

Refresh Scratch Pad Exit

Research Menu

Select Action: QUIT//

### Auto-Post Awaiting Resolution EEOB- EEOB Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available from the ListManager screen and behave like actions on the existing worklist:

- Split/Edit A Line
- Mark for Auto-Post
- Refresh Scratch Pad
- Research Menu
- Review Line
- EOB View/Print EEOB
- ERA View/Print ERA
- Verify
- Exit

### Auto-Post Awaiting Resolution EEOB- Mark for Auto-Post

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ListManager screen contains a new action of Mark for Auto-Post that checks the EEOB for auto-posting criteria and marks the EEOB for auto-posting if all criteria are met.

The EEOB is removed from the Awaiting Resolution list once it is successfully marked for auto-posting.

If the EEOB cannot be successfully marked for auto-posting, it displays the reason the EEOB cannot be auto-posted.

Verification is not required before marking for auto-post.

\+ Enter ?? for more actions

Split/Edit a Line EOB View/Print EEOB Review Line

Mark for Auto Post ERA View/Print ERA Verify

Refresh Scratch Pad Research EXIT Select Action: QUIT// Mark for Auto-Post

87705.7 has been marked for auto-post and has been removed from the Awaiting Resolution List.

## ## System Feature: Auto-Post Awaiting Resolution View/Print ERA 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto-Post Awaiting Resolution View/Print ERA - Add Auto-Post Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View/Print ERA action displays an Auto-Post Status of Completed or Not Completed, at the ERA summary level.

### Auto-Post Awaiting Resolution View/Print ERA - Detail Post Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system contains a new value of POSTING INCOMPLETE for the Detail Post Status and changes the label to “ERA DETAIL POST STATUS”.

### Auto-Post Awaiting Resolution View/Print ERA – Add Auto-Post Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View/Print ERA action shall display an Auto-Post Date for a status of completed, at the ERA summary level.

> EDI LOCKBOX WORKLIST - ERA DETAIL 11/22/13 Page: 1

> ================================================================================

> \*\*ERA SUMMARY DATA\*\*

> TRACE NUMBER: 013710099903824 INSURANCE CO ID: 1391263473

> ERA DATE: JAN 02, 2013 TOTAL AMOUNT PAID: 25.34

> PAYMENT FROM: HUMANA INC

> FILE DATE/TIME: JAN 02, 2014@21:57:42 RECEIPT: E12345678

> EFT MATCH STATUS: MATCHED ERA TYPE: ERA

> AUTO-POST STATUS: NOT COMPLETED AUTO-POST DATE: JAN 02, 2014

> INDIVIDUAL EOB COUNT: 2 MAIL MESSAGE: 37176080

> ERA DETAIL POST STATUS: POSTING INCOMPLETE EXPECTED PAYMENT METHOD CODE: ACH

### Auto-Post Awaiting Resolution View/Print ERA – Receipt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View/Print ERA action displays the Receipt at the EEOB detail level, regardless of posting.

\*\*EEOB DETAIL DATA\*\*

SEQUENCE \#: 1 EOB DETAIL: K306RI9

RECEIPT: E12345678A

AMOUNT PAID: 15.42

INSURANCE COMPANY ON BILL: HUMANA/VA MEDICAL

FREE TEXT PATIENT NAME: XXXXXXXXXXX BILLING PROVIDER NPI: 1275583619

RENDERING/SERVICING PROV NPI: 1275583619

ENTITY TYPE QUALIFIER: NON-INDIVIDUAL

RENDERING/SERVICING PROV NAME: MADISON VAMC

PATIENT: XXXXXXX,XXXXXXX/3607 CLAIM \#: 607-K306RI9

\*\*EEOB DETAIL DATA\*\*

SEQUENCE \#: 2 EOB DETAIL: K306RIB

RECEIPT:

AMOUNT PAID: 9.92

INSURANCE COMPANY ON BILL: HUMANA/VA MEDICAL

FREE TEXT PATIENT NAME: XXXXXXX,XXXXXXX BILLING PROVIDER NPI: 1275583619

RENDERING/SERVICING PROV NPI: 1275583619

ENTITY TYPE QUALIFIER: NON-INDIVIDUAL

RENDERING/SERVICING PROV NAME: MADISON VAMC

PATIENT: XXXXXXX,XXXXXXX /3607 CLAIM \#: 607-K306RIB

## ## System Feature: Auto-Post Awaiting Resolution Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto-Post Awaiting Resolution Filter- Change View Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AUTO-POST AWAITING RESOLUTION \[RCDPE AUTO-POST AWAITING RESOLUTION\] ListManager screen contains a new action, CV Change View, to filter the data displayed, based on the user's response to the Change View questions.

The Change View action is specific to a user.

### Auto-Post Awaiting Resolution Filter- All Payers or Range 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action contains a question to select payers:

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: ALL//

### Auto-Post Awaiting Resolution Filter- Preferred View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action contains a required question to save as a preferred view and store the answers to the Change View questions if the user answers "Y":

DO YOU WANT TO SAVE THIS AS YOUR PREFERRED VIEW (Y/N)?:

### Auto-Post Awaiting Resolution Filter- Preferred View Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user selects the EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] option, the system executes the Change View action if the user does not have a preferred view.

### Auto-Post Awaiting Resolution Filter- Filter Displayed in Heading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] ListManager screen displays a line at the top of the heading to indicate the Change View display selected by the user:

Filter: ALL PAYERS

## System Feature: Receipt Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Receipt Processing- Change Type of Payment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RECEIPT PROCESSING \[RCDP RECEIPT PROCESSING\] action ER Edit Receipt allows the user to change the Type of Payment field and prompt "Are you sure", if the following conditions are met:

- Current value is EDI LOCKBOX
- New value is CHECK/MO PAYMENT

-OR-

- Current value is CHECK/MO PAYMENT
- New value is EDI LOCKBOX

### Receipt Processing- Un-match the EFT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user successfully changes the Type of Payment from EDI LOCKBOX to CHECK/MO PAYMENT, the system marks the EFT as unmatched.

## System Feature: Exception Bulletins- Remove Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Exception Bulletins- Remove Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system no longer sends exception bulletins for the following:

- EDI LBOX EEOB - EXCEPTIONS
- EDI LBOX - NO VALID BILLS ON ERA
- EDI LBOX - ERA HAS ADJ/TAKEBACKS
- EDI LBOX ERA - DUPLICATE TRANSMISSION MSG
- EDI LBOX-STA# 999-Move/Copy Transactions

## System Feature: TPJI Reports- Add Indicator for Rejects 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TPJI Reports- Add Auto-Post Status 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TPJI Bill Charges Screen displays a new field to show the Auto-Post Status after the ERA field, only if the ERA is an auto-post candidate.

## System Feature: Daily Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Daily Activity Report- Change the Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LOCKBOX REPORTS MENU \[RCDPE EDI LOCKBOX REPORTS MENU\] option DAILY ACTIVITY REPORT \[RCDPE EDI LOCKBOX ACT REPORT\] is renamed to EFT DAILY ACTIVITY REPORT \[RCDPE EDI LOCKBOX ACT REPORT\].

## System Feature: Miscellaneous Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Miscellaneous Reports- Add a Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ACTIVE BILLS WITH EEOB REPORTS \[RCDPE ACTIVE WITH EEOB REPORT\] prompts the user for a beginning and ending Received Date, used to limit the report output.

### Miscellaneous Reports- Change to ListManager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reports are displayed in a ListManager format with standard ListManager actions available for selection:

- ACTIVE BILLS WITH EEOB REPORTS \[RCDPE ACTIVE WITH EEOB REPORT\]
- DAILY ACTIVITY REPORT \[RCDPE EDI LOCKBOX ACT REPORT\]
- ERA UNMATCHED AGING REPORT \[RCDPE ERA AGING REPORT\]
- EFT UNMATCHED AGING REPORT \[RCDPE EFT AGING REPORT\]
- UNAPPLIED EFT DEPOSITS REPORT \[RCDPE UNAPPLIED EFT DEP REPORT\]
- DUPLICATE EFT DEPOSITS AUDIT REPORT \[RCDPE EFT AUDIT REPORT\]
- EEOB MOVE/COPY AUDIT REPORT \[RCDPE EEOB MOVE/COPY REPORT\]
- ERAS POSTED WITH PAPER EOB AUDIT \[RCDPE ERA W/PAPER EOB REPORT\]
- REMOVE ERA FROM ACTIVE WORKLIST \[RCDPE REMOVED ERA AUDIT\]

### Miscellaneous Reports - Add Filter for TRICARE and CHAMPVA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reports have filter questions to allow inclusion or exclusion of TRICARE and CHAMPVA:

- ACTIVE BILLS WITH EEOB REPORTS \[RCDPE ACTIVE WITH EEOB REPORT\]
- ERA UNMATCHED AGING REPORT \[RCDPE ERA AGING REPORT\]
- EEOB MOVE/COPY AUDIT REPORT \[RCDPE EEOB MOVE/COPY REPORT\]
- ERAS POSTED WITH PAPER EOB AUDIT \[RCDPE ERA W/PAPER EOB REPORT\]
- REMOVE ERA FROM ACTIVE WORKLIST \[RCDPE REMOVED ERA AUDIT\]
- The filter selection for TRICARE and CHAMPVA is displayed in the report headers, consistent with the current filter selection display.

## System Feature: EEOB Move/Copy Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EEOB Move/Copy Option- Correct Payer Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system transfers the correct payer information when moving or copying an EEOB from one patient to another.

### EEOB Move/Copy Option- Rename the Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB Move/Copy option is renamed to the EEOB Move/Copy/Remove option and prompts the user with an option to Remove EEOB from patient claim.

EXC    EDI Lockbox 3rd Party Exceptions

   MA     Automatic Match EFTs to ERAs

 MCR    EEOB Move/Copy/Remove

   MM     Manual Match EFT-ERA

   MO     Move ERA Total To Suspense

REFT   Remove Duplicate EFT Deposits

   REP    EDI Lockbox Reports Menu ...

   RET    Mark ERA Returned To Payer

   UN     Unmatch An ERA

   UP     Update ERA Posted Using Paper EOB

   WL     EEOB Worklist

   ZB     Mark 0-Balance EFT Matched

Select EDI Lockbox Option: MCR  EEOB Move/Copy/Remove

Select one of the following:

M     Move EEOB to different claim

C     Copy EEOB to multiple claims

R Remove EEOB from patient claim

Select action: R//emove EEOB from patient claim

### EEOB Move/Copy Option- Require Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remove option on the new EEOB Move/Copy/Remove option requires new security key RCDPE REMOVE EEOB.

### EEOB Move/Copy Option- Remove Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remove option on the new EEOB Move/Copy/Remove option displays the patient and claim information for verification, and requires the user to enter a free text justification comment, and prompt the user with a question of "Are you sure you want to remove EEOB from claim K#### (Y/N)?".

Select EXPLANATION OF BENEFIT (EEOB) to REMOVE: K400M44       ARPatient,One

    12-01-03     Inpatient     REIMBURSABLE INS.     PRNT/TX     

AETNA US HEALTHCARE (PRIMARY)

Enter JUSTIFICATION COMMENT: Sent to our facility by mistake. Not intended to pay this claim.

ARE YOU SURE YOU WANT TO REMOVE EEOB from claim K400M44 (Y/N)? Y

 

EEOB REMOVED

### EEOB Move/Copy Option- Audit Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remove option on the new EEOB Move/Copy/Remove option stores data in the audit log with the following information:

- Audit Log type of "R"
- Date/Time stamp
- User
- Original Bill Number
- Free Text Justification Comment

### EEOB Move/Copy Option- Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the remove option has been executed, the system no longer displays the removed EEOB information for the patient with whom the information was previously associated.

### EEOB Move/Copy Option- AR Comment=

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays a comment on the Bill Charges screen, similar to the comment that is displayed for Move/Copy.

<u>Bill Charges                  Nov 15, 2013@18:33:04          Page:    3 of    9</u>

%K700001   ARPATIENT,ONE   O7774         DOB: 01/23/36   Subsc ID: 657789      

 06/13/97 - 06/13/97        ADMIT THRU DISCHARGE         Orig Amt: 50.00

<u>+                                                                              </u>

    EOB Type: NORMAL EOB                                                        

         ICN:                              Patient Resp Amount: 0.00           

  Payer Name: INSURANCE LTD.              Total Allowed Amount: 0.00           

    EOB Date:                          Total Submitted Charges: 0.00           

 Svc From Dt:                                        Svc To Dt:                

                                          Reported Payment Amt: 0.00           

       ERA \#: 1007                                                              

     Trace \#: 8281206DA5                                                       

MOVE/COPY/REMOVE HISTORY

                                                              

Date/Time EEOB Removed: NOV 15, 2013@17:53:47

Remove of EEOB performed by: USER,AR 

Remove Justification Comments:                                                   

testing comment testing comment                                              

Original Claim Number: 92046A                                        

+         \|% EEOB \| Enter ?? for more actions\|                                 

PR  Bill Procedures       CM  Comment History       AB  Annual Benefits

CI  Go to Claim Screen    IR  Insurance Reviews     EL  Patient Eligibility

                          HS  Health Summary        EX  Exit

ED  EDI Status            AL  Go to Active List

                          VI  Insurance Company

Select Action: Next Screen//

### EEOB Move/Copy Option- AR Comment History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays a comment in AR Comment History, similar to the comment that is displayed for Move/Copy.

<u>Comment History               Nov 15, 2013@18:36:46          Page:    2 of    2</u>

%K700001   ARPATIENT,ONE   O7774         DOB: 01/23/36   Subsc ID: 657789      

AR Status: RETURNED FOR AMENDMENT   Orig Amt: 50.00      Balance Due: 50.00    

<u>+                                                                               </u>

4949        11/15/13   EEOB REMOVED BY XXX               FOLLOW-UP DT:          

                        testing comment testing comment    

4950        11/15/13   ERA Payer Contact Information   FOLLOW-UP DT:          

Payer Name: INSURANCE LTD.                        

                        Contact Name: FIRSTNM LASTNM                                

                        Phone Number: 2006649555                               

          \|% EEOB \| Enter ?? for more actions\|                                 

BC  Bill Charges          AR  Account Profile       VI  Insurance Company

DX  Bill Diagnosis       AD  Add Comment         VP  Policy

PR  Bill Procedures       IR  Insurance Reviews   AB  Annual Benefits

CI  Go to Claim Screen HS  Health Summary      EL  Patient Eligibility

AL  Go to Active List     EX  Exit

Select Action: Quit//

### EEOB Move/Copy Option- Add Filter Question

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For report MCR EEOB Move/Copy/Remove, the system displays a filter question of MOVE/COPY/REMOVE or ALL.

The user selection displays in the header, consistent with other filter question responses.

START DATE: T-2 (DEC 31, 2013)

END DATE: DEC 31,2013// T (JAN 02, 2014)

Select division: ALL//

MOVE/COPY/REMOVE or ALL (M/C/R/A): ALL//

Are you sure you want to select ALL divisions ? NO// YES

Export the report to Microsoft Excel? NO//

## System Feature: Add Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add Security Keys- Add Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system contains the following new security keys, none of which are automatically assigned to any user:

- RCDPE AGED PMT
- RCDPE ERA EXCEPT
- RCDPE AUTO DEC
- RCDPE REMOVE EEOB

## System Feature: Testing Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Testing Tool- Reset 837

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system has the ability to reset an 837 to allow an 835 to reprocess against that 837.

### Testing Tool- Reset ECME Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system has the ability to reset an ECME bill to allow an 835 to reprocess against the bill.

### Testing Tool- Manipulate Fields and Resend

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system has the ability to reprocess the ERA in VistA after manipulating the 5 fields on the ERA used for matching: the first 5 characters of the patient's last name, date of service, bill number or claim number, social security number or patient ID, and the amount paid.

### Testing Tool- Process De-Identified data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system has the ability to receive and process de-identified data.

### Testing Tool- Not Available after National Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The testing functionality is not available to sites after national release.

## System Feature: Non- Released Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Non- Released Prescriptions- EXC Exception List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system places an EEOB on the EXC Exception List if the EEOB pertains to a prescription that is non-released.

### Non- Released Prescriptions – Process Released Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system runs a nightly job removing exceptions from the EXC Exception List if the exception was triggered for non-released prescription which is newly released.

Once the EEOB is removed from the EXC Exception List, process continues as normal.

## System Feature: Trace Number with 9s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Trace Number with 9s- Include EFTs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system includes EFTs with trace number that is all 9’s and includes all payer names on the bulletin with a subject of “EDI LBOX-STA# NNN-ACTION REQ-EFTS\>14 days” and the following reports:

- Daily Activity Report
- EFT Unmatched Aging
- Unapplied EFT Deposits

If the payer name is null, the entry on the report shows with a name of \<NO PAYER NAME RECEIVED\>.

## Sytem Feature: Active Bills with EEOB Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Active Bills with EEOB Report- EEOB Date Posted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system references the EEOB date posted instead of the ERA date posted on report ACTIVE BILLS WITH EEOB REPORT \[RCDPE ACTIVE WITH EEOB REPORT\].

## System Feature: Manual Match of ERA and EFT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Manual Match of ERA and EFT- Add Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system prompts the user for a date range and filter the data based on the date range for the option MANUAL MATCH EFT-ERA \[RCDPE MANUAL MATCH EFT-ERA\].

### Manual Match of ERA and EFT- Partial Match on Trace Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system allows a partial match on trace number, ignoring leading zeroes.

## System Feature: Decrease Adjustment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Decrease Adjustment - Warning Message if Mark for Auto-Post

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option DECREASE ADJUSTMENT \[PRCAC TR DECREASE\] displays a warning message of “Marked for Auto-Post. Are you sure? (Y/N): N//” if a user tries to make a decrease adjustment on a bill that has at least one associated EEOB marked for auto-post.

## System Feature: EDI Lockbox Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EDI Lockbox Menu- Order of Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays options on the EDI LOCKBOX \[RCDPE EDI LOCKBOX MENU\] in the following order:

EXC EDI Lockbox 3rd Party Exceptions

WL ERA Worklist

APAR Auto-Post Awaiting Resolution

MA Automatic Match EFTs to ERAs

MC EEOB Move/Copy/Remove

MM Manual Match EFT-ERA

MO Move ERA Total To Suspense

REFT Remove Duplicate EFT Deposits

REM Remove ERA from Active Worklist

REP EDI Lockbox Reports Menu ...

UN Unmatch An ERA

UP Update ERA Posted Using Paper EOB

ZB Mark 0-Balance EFT Matched

## System Feature: Trace Number Matching

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Trace Number Matching – Remove Case Sensitivity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The matching of the ERA trace number to the EFT trace number shall be modified so that matches are case insensitive.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PRCA*4.5*316 AR Release Notes/Installation Guide

## ## ## Audit/Set up a New Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-316-ar-release-notes-installation-guide/002.png)

This menu contains options for auditing bills and establishing a new billing record in the Accounts Receivable file for an existing debtor. To add a new debtor, see the Set Up And Audit New Accounts Receivable option.

### Audit an Electronic Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays a new bill for review, allows the auditor to approve it, and if approved, continues the bill through AR processing.

The option asks if you wish to "Loop" through all New Bills. This feature facilitates the clerk's job eliminating the need to determine the new bills and enter it in for auditing. The computer will then display the information it has stored for each bill. After reviewing and/or editing the bill, you will be prompted for your Electronic Signature Code. If your Electronic Signature Code is entered correctly, you will see a message informing you that an FMS document has been created and sent and you can proceed to audit other bills or return to your menu.

Select Audit/Set up a New Accounts Receivable Option: AUDit an Electronic Bill

Do you want to loop thru 'NEW BILLS'? YES//

SITE: ALTOONA VAMC// PENNSYLVANIA 000

==========================================================================

BILL \#: 000-K400058 CATEGORY: VENDOR

DATE BILL PREPARED: MAY 26,1994

DEBTOR: ARDEBTOR, ONE

123 MAIN ST

ALTOONA, PA 16602 PHONE NO.:(814) 944-0000

BILL RESULTING FROM: OVERPAYMENT

APPROVED IN MED BY : ONE,TEST

Date Description Quantity Units Cost Total Cost

==========================================================================

(Since this is an overpayment no data is necessary here.)

==========================================================================

BILL \# : 000-K400058 DEBTOR : ARDEBTOR, ONE

FISCAL YEAR FUND (APPROPRIATION) ORIGINAL AMOUNT

94 0160A1 100.00

==========================================================================

\*\*\* REFUND \*\*\*

CONTROL POINT : 101

BUDGET OBJECT : 2699 COST CENTER : 870000

SUB : SUB : 21

==========================================================================

\*\*\* REIMBURSEMENT \*\*\*

REVENUE SOURCE : SUB :

IS THIS DATA CORRECT? NO// (NO)

Do you want to edit this information ? NO// Y (YES)

Will this bill be a REFUND or REIMBURSEMENT? REFUND//

CONTROL POINT: 101// 102

SAT STATION:

COST CENTER: 870000//

BOC (SUB ACCOUNT): 2699//

BILL RESULTING FROM: OVERPAYMENT//

==========================================================================

BILL \#: 000-K400058 CATEGORY: VENDOR

DATE BILL PREPARED: MAY 26,1994

DEBTOR: ARDEBTOR, ONE

123 MAIN ST

ALTOONA, PA 16602 PHONE NO.:(814) 555-0000

BILL RESULTING FROM: OVERPAYMENT

APPROVED IN MED BY : ONE,TEST

Date Description Quantity Units Cost Total Cost

==========================================================================

==========================================================================

BILL \# : 000-K400058 DEBTOR : ARDEBTOR, ONE

FISCAL YEAR FUND (APPROPRIATION) ORIGINAL AMOUNT

94 0160A1 100.00

==========================================================================

\*\*\* REFUND \*\*\*

CONTROL POINT : 102

BUDGET OBJECT : 2699 COST CENTER : 870000

SUB : SUB : 21

==========================================================================

\*\*\* REIMBURSEMENT \*\*\*

REVENUE SOURCE : SUB :

IS THIS DATA CORRECT? NO// Y (YES)

Do you want to write any comments for this bill ? NO// (NO)

Enter Electronic Signature Code: \<Signature\>

Building FMS Billing Document. Please hold...

FMS document, \# 5208, built and queued for transmission.

\*\*\* AUDITED AND RELEASED \*\*\*

### Set up and Audit New Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option establishes debtor accounts for AR bills that must be loaded into the system manually. It primarily sets up accounts that have not already been established via the electronic Billing Module of Accounts Receivable. If the debtor already has an account, use the Audit an Electronic Bill option to activate any subsequent bills. The paper bill you are working from should contain all of the information you need, facilitating data entry. Bills sent to you electronically already contain their account information, and you should use the option Audit an Electronic Bill to work with them. If you enter a number that has already been used, you will see a message telling you to choose another bill number.

If the bill you are working with has been sent to you electronically, you must use the Audit an Electronic Bill option to review it. If the bill has been entered into the system but is not complete, use the Edit an Incomplete Accounts Receivable option. If you are working with a Category C type transaction (Means Test), the computer will ask you for the type of care, debtor name, resulting from, date of charges, service, approving official, and finally, for any comments.

The debtor can be a patient, a vendor, an employee or ex-employee, another federal agency, or any other party responsible for paying the bill. When you make new entries, these entries must match entries in the other appropriate files. For example, patients you enter must exist in the Patient file, and vendors you enter must exist in the Vendor file. You may add a new debtor, provided the category of the AR entered does not require a patient or Third Party type debtor. These types of debtors cannot be entered here; they can only be entered in the MAS software. However, if the category does not require a patient or Third Party type debtor (the other debtor types are means test patient, other-person, vendor, and institution), you may add a new debtor.

### Amended Bill Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays an amended bill for auditing. This action requires an electronic signature to complete.

Once a bill has been returned to the billing service for amend-ment and is on a subsequent pass through the audit procedure, there are other actions that may need to be taken, depending on the nature of the amendment. Once the bill has been reactivated, the system reminds you of additional actions.

Select Audit/Set up a New Accounts Receivable Option: AMENDed Bill Audit

Select ACCOUNTS RECEIVABLE BILL NO.: K20177 000-K20177 MILITARY 09-27-93 ARpatient,one AMENDED BILL

=========================================================================

BILL NO.: 000-K20177 DEBTOR: ARpatient, one

ORIGINAL AMOUNT: \$600 CATEGORY: MILITARY

\<\<RETURNED\>\>

DATE: SEP 27,1994 BY: TWO,TEST

REASON:

SHOULD BE 60 QUANTITY

\<\<AMENDED\>\>

DATE: SEP 27,1994 AMENDED BY: TWO,TEST

AMENDED AMOUNT: \$20

COMMENTS:

ADDED ADDITIONAL \$20

=========================================================================

Is this correct ? NO//\<ret\> (NO)

Do you want to return this bill to the service again ? NO// YES (YES)

Are you sure you want to return this bill to the Service ? NO// Y (YES)

DATE RETURNED TO SERVICE: SEP 27,1994//\<ret\>

FISCAL COMMENTS (RETURN): SHOULD BE 60 QUANTITY

### Edit an Incomplete Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to edit Accounts Receivables that are in a status of Incomplete. The information displayed by this option depends on the category that has been assigned to the incomplete bill.

When you are satisfied that everything is correct, enter your signature code. It is important to emphasize the fact that you should be sure the entries are correct before you attach your electronic signature. To allow you to correct any errors discovered after using this option, the AR Supervisor must return the bill to you. Even if the bill is canceled, it must be re-entered with a new bill number since the system stores the complete bill history along with its number.

Select ACCOUNTS RECEIVABLE BILL NO.: 000-K400025 VENDOR 05-18-94

ARDEBTOR, ONE INCOMPLETE \$1.00

CATEGORY: VENDOR//

DEBTOR: ARDEBTOR, ONE//

BILL RESULTING FROM: OVERPAYMENT//

DATE BILL PREPARED: MAY 18,1994//

SERVICE: MEDICAL SERVICE//

APPROVING OFFICIAL (SERVICE): ONE,TEST//

BILL TYPE: REIMBURSEMENT//

FUND: 2431 1994 1994

SAT STATION: 12

Do you want to write any comments for this bill ? NO// (NO)

==========================================================================

BILL \#: 000-K400025 CATEGORY: VENDOR

DATE BILL PREPARED: MAY 18,1994

DEBTOR: ARDEBTOR, ONE

123 MAIN ST

ALTOONA, PA 16602 PHONE NO.:(814) 555-0000

BILL RESULTING FROM: OVERPAYMENT

APPROVED IN MED BY : TWO,TEST

Date Description Quantity Units Cost Total Cost

==========================================================================

BILL \# : 000-K400025 DEBTOR : ARDEBTOR, ONE

FISCAL YEAR FUND (APPROPRIATION) ORIGINAL AMOUNT

94 2431 200.00

==========================================================================

\*\*\* REFUND \*\*\*

CONTROL POINT :

BUDGET OBJECT : COST CENTER :

SUB : SUB :

==========================================================================

\*\*\* REIMBURSEMENT \*\*\*

REVENUE SOURCE :ARRV SUB :

IS THIS DATA CORRECT? NO// y (YES)

Enter Electronic Signature Code: \<Signature verified\>

Building FMS Billing Document. Please hold...

FMS document, \# 31, built and queued for transmission.

## New Bill Forms Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-316-ar-release-notes-installation-guide/003.png)

This menu contains options necessary for printing a copy of bill forms.

### Other Bill Form Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will print all the other bill forms which include the 1080 and 1081 bills. This option is for use with new bills only.

### Re-print 'Other' Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to print a second, or subsequent, copy of the 1080 and 1081 forms.

## Profile of Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a report about activities and events that have occurred against any account. You may view these accounts by entering the debtor name, bill number, or PAT number. If the debtor is a patient, you may enter the social security number. Use this option to obtain information for veteran or third party inquiries. Also, it can be used to accumulate information for submitting delinquent debts to District Counsel.

OCT 22,1994 16:11 ACCOUNTS RECEIVABLE PROFILE

=======================================================================

NAME: ARpatient,one BILL \#: 000-AA0014

101 WALT ROAD SOC.SEC.NO.: 000-11-1111

ORLANDO, FL 43434 DATE OF BIRTH: 03-04-34

PHONE NO.: DATE POSTED: AUG 31,1992 17:45:58

CURRENT STATUS: COLLECTED/CLOSED CATEGORY: RX CO-PAYMENT/NSC VET

GL \#: DATE BILL PREPARED: AUG 31,1992

INTEREST EFFECTIVE RATE DATE: JUL 1,1991 ANNUAL INTEREST RATE: .085

ADMIN EFFECTIVE RATE DATE: JUL 1,1991 MONTHLY ADMIN RATE: .91

ORIGINAL AMOUNT: 0.00

FISCAL YEAR APPROP. CODE PAT REFERENCE \# AMOUNT

---------- ------------ -------------- ------

92 0.00

BALANCES PAID LETTER1/ICD:

PRINCIPAL: 0.00 54.50 LETTER2:

INTEREST: 0.00 0.00 LETTER3:

ADMINISTRATIVE: 0.00 0.00 IRS LETTER:

DC/DOJ REF.DATE:

CURRENT: 0.00 54.50

TRANSACTIONS:

62 1 INCREASE ADJUSTMENT 08/31/92 50.00

63 2 INCREASE ADJUSTMENT 08/26/92 4.50

79 B2222222 PAYMENT (IN PART) 08/31/92 2.00

80 B2222222 PAYMENT (IN PART) 08/31/92 5.00

86 B3333333 PAYMENT (IN FULL) 09/03/92 47.00

BILL RESULTING FROM: UNEARNED MD/DD BONUS

Statement date: NOV 8,1994

OTHER BILLS:

000-AB0004 (PREP/REFU) 000-AA0015 (RX C/COLL) 000-AB0020 (PREP/CANC)

000-AB0029 (PREP/REFU) 000-AB0049 (PREP/REFU) 000-K20061 (VEND/PEND)

000-K20072 (CURR/BILL) 000-K20131 (RX C/COLL) 000-K20136 (EX-E/PEND)

000-K20188 (RX C/OPEN)

![](prca-4-5-316-ar-release-notes-installation-guide/004.png)

## Update Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options necessary to record new activity against a particular account.

### Locate Debtor Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option documents actions that fiscal personnel have taken to locate a debtor's address. Use this for proof of your attempts to collect debts from debtors who have no address.

BILL NO.: 000-K10092 DEBTOR: ARpatient,one

========================================================================

ABLE TO PAY: YES ABLE TO LOCATE: NO DMV LOCA. CHECK:

POSTAL LOC. DATE SENT: OCT 13,1994 POSTAL LOC. DATE REC'D:OCT 16,1994

IRS ABLE TO LOCATE: YES IRS LOC. DATE SENT: DEC 27,1992

IRS LOC. DATE REC'D: APR 6,1994 CREDIT REP. ABLE TO PAY: NO

CREDIT REPT. DATE SENT: SEP 23,1994 CREDIT REP. DATE REC'D:OCT 8,1994

PATIENT FOLDER REVIEWED: YES DATE FOLDER REVIEWED: OCT 22,1994

LETTER1: LETTER2: LETTER3:

=========================================================================

ABLE TO PAY: YES//\<ret\>

ABLE TO LOCATE: NO//\<ret\>

DMV LOCATION CHECK:\<ret\>

POSTAL LOC.DATE SENT: OCT 13,1994//\<ret\>

POSTAL LOC.DATE RECEIVED: OCT 16,1994//\<ret\>

IRS ABLE TO LOCATE: YES//\<ret\>

IRS LOC. DATE SENT: DEC 27,1992//\<ret\>

IRS LOC. DATE RECEIVED: APR 6,1994//\<ret\>

CREDIT REP. ABLE TO PAY: NO//\<ret\>

CREDIT REPT. DATE SENT: SEP 23,1994//\<ret\>

CREDIT REP. DATE RECEIVED: OCT 8,1994//\<ret\>

PATIENT FOLDER REVIEWED: YES//\<ret\>

DATE FOLDER REVIEWED: OCT 22,1994//\<ret\>

![](prca-4-5-316-ar-release-notes-installation-guide/005.png)

### DC/DOJ Action Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options necessary to control account activities that deal with the District Counsel or the Department of Justice.

#### Refer to DC/DOJ

Use this option if a determination has been made that an active account must be referred for collection to government authorities. The system uses the principal balance of the account to determine which type of referral has been made. The defaults are set so that balances between \$600 and \$1200 will be recorded as having been referred to the District Counsel. Accounts over \$1200 will be recorded as having been referred to the Department of Justice. The minimum/maximum referral amounts vary depending on which District Counsel office you work with. Check these defaults; your supervisor can change the amounts as required.

This option does not automatically pass information to the District Counsel or the Department of Justice. You are just recording account activity in the AR system.

Select DC/DOJ Action Menu Option: REFER to DC/DOJ

Select ACCOUNTS RECEIVABLE BILL NO.: AA0003 000-AA0003 C (MEANS TEST)

08-12-92 ARpatient,one ACTIVE \$500.00

IF THE PRINCIPAL BALANCE IS BETWEEN \$200 AND \$99999 THE REFERRAL WILL BE TO DC.

IF THE PRINCIPAL BALANCE IS GREATER THAN \$99999 THE REFERRAL WILL BE TO DOJ.

REFERRAL DATE: T (OCT 23, 1994)

PRINCIPAL BALANCE: 499.09//\<ret\>

INTEREST BALANCE:\<ret\>

ADMIN. BALANCE: .91//\<ret\>

MARSHAL FEE: 0//\<ret\>

COURT COST: 0//\<ret\>

=======================================================================

BILL \#: 000-AA0003 DATE: 10/23/93

TRANSACTION TYPE: REFER TO DC TOTAL AMOUNT: 500.00

PRIN.BAL. INT.BAL. ADMIN.BAL. MARSHAL FEE COURT COST

499.09 0.00 0.91 0.00 0.00

=======================================================================

IS THIS CORRECT ? NO// Y (YES)

#### Returned by DC/DOJ

This option reinstates an active account that was referred to District Counsel or Department of Justice. It records the date returned by DC/DOJ for the account that was referred. This option should be used for recording accounts that are returned by DC/DOJ because the debt has been cleared as a result of corrective award action, or accounts that are returned and will be cleared by appropriate write-off because of death, bankruptcy, etc.

Select DC/DOJ Action Menu Option: RETURNED by DC/DOJ

Select ACCOUNTS RECEIVABLE BILL NO.: AA0003 000-AA0003 C (MEANS TEST) 08-12-92 ARpatient,one ACTIVE \$500.00

DATE RETURNED: T (OCT 23, 1994)

PRIN. BAL. RETURNED: 499.09

INT. BAL. RETURNED:\<ret\>

ADMIN. BAL. RETURNED: .91

MARSHAL FEE RETURNED:\<ret\>

COURT COST RETURNED:\<ret\>

===================================================================

BILL \#: 000-AA0003 DATE: 10/23/93

TRANSACTION TYPE: RETURNED BY DC/DOJ TOTAL AMOUNT: 500.00

PRIN.BAL. INT.BAL. ADMIN.BAL. MARSHAL FEE COURT COST

499..09 0.00 0.91 0.00 0.00

===================================================================

IS THIS CORRECT ? NO// Y (YES)

#### Re-Refer to DC/DOJ

If it becomes necessary to refer an account to the District Counsel or the Department of Justice more than once, use this option to record that fact.

#### Debit Voucher (SF 5515)

This option makes a record of the Standard Form 5515 debit vouchers. Enter the information from the voucher. Use this option to apply a debit voucher transaction from the District Counsel or the Department of Justice.

#### Waived by DC/DOJ

This option records accounts that are waived in full as a result of a District Counsel or Department of Justice ruling. It maintains records of those accounts that have been waived. This information is used for the Debt Collection Reports. Use your source document to enter the data as requested. It changes the status of the account to Write-Off. If you have a case where the District Counsel or the Department of Justice has waived a portion of an account, see the Waive An Accounts Receivable option.

Select DC/DOJ Action Menu Option: WAIVEd by DC/DOJ

Select ACCOUNTS RECEIVABLE BILL NO.: AA0003 000-AA0003 C (MEANS TEST)

08-12-92 ARpatient,one ACTIVE \$500.00

Are you sure you want to record this as a Waiver ? NO// Y (YES)

WAIVED DATE: T (OCT 23, 1994)

COMMENTS:

1\>DC wouldn't let us have the money!!

#### Terminated by DC/DOJ

This option records those accounts that have been terminated by the District Counsel or the Department of Justice.

The data collected under this option is used for the Debt Collection Reports. Selecting this option changes the status of the account to Write-Off.

Select DC/DOJ Action Menu Option: TERMINATED by DC/DOJ

Select ACCOUNTS RECEIVABLE BILL NO.: K10092 000-K10092 TORT FEASOR

10-12-92 ARpatient,one ACTIVE \$2000.00

Are you sure you want to record this as a Termination ? NO// Y (YES)

TERMINATION DATE: T (OCT 23, 1994)

TERMINATION REASON: WAIVED

COMMENTS:

1\>They said we couldn't get the money!!

2\>\<ret\>

#### Compromised by DC/DOJ

This option records those accounts that have been compromised by the District Counsel or the Department of Justice. The data collected under this option is used for the Debt Collection Report. The account's status changes to Write-Off.

Select DC/DOJ Action Menu Option: COMPROMISED by DC/DOJ

Select ACCOUNTS RECEIVABLE BILL NO.: K10091 000-K10091 TORT FEASOR 10-13-92 ARpatient,one ACTIVE \$1000.00

Are you sure you want to record this as a Compromise? NO// Y (YES)

TERMINATION DATE: T (OCT 23, 1994)

TERMINATION REASON: COMPROMISED

COMMENTS:

1\>Documentation Purposes!

### repayment plan menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-316-ar-release-notes-installation-guide/006.png)

This menu contains options necessary to establish and manage repayment plans.

If the debt owed to VA is large enough to create a substantial financial burden, the debtor may request that they repay it in installments. It is also likely that an installment plan is the agreed upon settlement resulting from negotiations with the District Counsel or the Department of Justice. In either case, the set of options gives the AR clerk the tools to set up and keep track of repayment plans. They establish the plans, print statements, and apply interest charges. Payments under these plans are processed by the Agent Cashier payment entry options, but the statements are printed using this menu.

#### enter/edit Repayment Plan

This option establishes a single repayment plan for one or multiple bills for a debtor.

Before you set up a plan you will need to know the date the plan was established, the day of the month the payments will be due, and the agreed upon amount of each payment. If an account has multiple bills that are to be repaid, all bills can be consolidated in a single repayment plan. A debtor may make lump sum payments for all bills in the account. It is the user's responsibility to ensure that the correct credits are posted to the individual bills. Existing administrative costs are included in the principal balance at the time a plan is set up. Interest also carries over into the plan. Additional administrative costs can be added at any time using the Add an Administrative Cost option. There is no automatic notification if a debtor's payments become delinquent. In some cases, a delinquent payment means that interest must be added to the plan. See the Charge Int/Admin option.

Select DEBTOR NAME or BILL NUMBER: OLLAR,M

Searching for a PATIENT, (pointed-to by DEBTOR)

OLLAR,MAUDE LYNN \*SENSITIVE\* \*SENSITIVE\* YES SC VETERAN

CSHD

Enrollment Priority: GROUP 5 Category: ENROLLED End Date:

...OK? Yes// (Yes)

This Veteran does not have a Repayment Plan

List of Active Bills:

1 000-K902DWX RX CO-PAYMENT/SC VET 07-28-09 ACTIVE \$ 84.34

2 000-K902GB2 RX CO-PAYMENT/NSC VET 08-05-09 ACTIVE \$ 9.38

3 000-K902L7G RX CO-PAYMENT/SC VET 08-21-09 ACTIVE \$ 18.72

4 000-K902UCB RX CO-PAYMENT/SC VET 09-21-09 ACTIVE \$ 93.38

5 000-K0007CX RX CO-PAYMENT/SC VET 10-21-09 ACTIVE \$ 65.23

6 000-K000FFE RX CO-PAYMENT/SC VET 11-25-09 ACTIVE \$ 74.38

7 000-K000M92 RX CO-PAYMENT/SC VET 12-21-09 ACTIVE \$ 55.67

8 000-K2017HU RX CO-PAYMENT/NSC VET 02-07-12 ACTIVE \$ 24.78

Choose Bills to Add to Repayment Plan: : ALL//

Total amount chosen is \$ 425.88

Are you sure this is correct? YES//

Repayment Amount Due: 50

Number of Payments will be 9

Repayment Plan Date: T (JUN 25, 2017)

Day of Month Payment Due: 15

Due Date of First Payment: 7/15 (JUL 15, 2017)

The Repayment Plan has been established.

Type \<Enter\> to continue or '^' to exit:

Summary of Current Repayment Plan for AR Debtor: OLLAR,MAUDE LYNN

------------------------------------------------------------------

Monthly Repayment Amount: \$50.00 Day of Month Payment Due: 15

Number of Payments Remaining: 9 Due Date of First Payment: 07/15/17

Current Total Due: \$425.88 Last Payment Due: 03/15/18

Plan Date: 06-25-17 Next Payment Due: 07/15/17

Bills in Repayment Plan:

000-K902DWX\*\* RX CO-PAYMENT/SC VET 07-28-09 ACTIVE \$ 84.34

000-K902GB2\*\* RX CO-PAYMENT/NSC VET 08-05-09 ACTIVE \$ 9.38

000-K902L7G\*\* RX CO-PAYMENT/SC VET 08-21-09 ACTIVE \$ 18.72

000-K902UCB\*\* RX CO-PAYMENT/SC VET 09-21-09 ACTIVE \$ 93.38

000-K0007CX\*\* RX CO-PAYMENT/SC VET 10-21-09 ACTIVE \$ 65.23

000-K000FFE\*\* RX CO-PAYMENT/SC VET 11-25-09 ACTIVE \$ 74.38

000-K000M92\*\* RX CO-PAYMENT/SC VET 12-21-09 ACTIVE \$ 55.67

000-K2017HU\*\* RX CO-PAYMENT/NSC VET 02-07-12 ACTIVE \$ 24.78

\*\* Bill is currently in Repayment Plan

Do you wish to enter Debtor comments? YES//

Reference number assigned: 000-2130252-0

Date of Contact: JUN 25,2017//

Brief Comment: PAYMENT PLAN ESTABLISHED

Expanded Comment:

1\>Payment plan established.

2\>\$100/mon on the 15th of the month.

3\>Last payment due 3/15/2018.

4\>

EDIT Option:

Follow-up Date: 8/16 (AUG 16, 2017)

Is this OK? YES//

Select DEBTOR NAME or BILL NUMBER:

In cases where there is already a Repayment Plan in place for the selected debtor, the user will see the following prompt and the user may select the appropriate action. The View action is shown here in this screen shot.

Select DEBTOR NAME or BILL NUMBER: K70CYLW AAAHY,CLJB IHZWTHN CU

This Veteran has a Repayment Plan - (D)elete, (E)dit or (V)iew it? V// IEW

Summary of Current Repayment Plan for AR Debtor: AAAHY,CLJB IHZWTHN CU

------------------------------------------------------------------

Monthly Repayment Amount: \$5.00 Day of Month Payment Due: 28

Number of Payments Remaining: 5 Due Date of First Payment: 04/28/18

Current Total Due: \$20.00 Last Payment Due: 08/28/18

Plan Date: 03-07-18 Next Payment Due: 04/28/18

Bills in Repayment Plan:

558-K70CYLW\*\* RX CO-PAYMENT/SC VET 04-25-17 ACTIVE \$ 20.00

\*\* Bill is currently in Repayment Plan

Type \<Enter\> to continue or '^' to exit:

Payments Since Plan Date

None

Bills not in Repayment Plan:

#### Profile of Repayment Plan

This option displays an overview of account activity under a repayment plan. Use this option to keep track of the payments for debtors who have a repayment plan set up. The report lists the monthly payment due dates, whether or not the payment was received, whether or not a statement was sent to the debtor, and the date the statement was mailed.

BILL NO.: 000-K10091 DEBTOR: ARpatient,one

CURRENT BALANCE: 1000.00 REPAYMENT AMOUNT: 100.00

REPAYMENT SCHEDULE

-------------------------------------------------------------------------

DUE PAYMENT SEND PAYMENT DATE SENT PAYMENT

DATE RECEIVED STATEMENT STATEMENT

-------------------------------------------------------------------------

NOV 15,1994 NO

DEC 15,1994 NO

JAN 15,1994 NO

FEB 15,1994 NO

MAR 15,1994 NO

APR 15,1994 NO

MAY 15,1994 NO

JUN 15,1994 NO

JUL 15,1994 NO

AUG 15,1994 NO

-------------------------------------------------------------------------

#### Print a Payment Statement

This option prints the repayment plan statements allowing you to match them with the payment receipts and mail them to the customer. When the debtor makes a payment, the Agent Cashier issues a numbered receipt and records it in the account record. Repayment plans complicate the matter slightly because the clerk must use this separate option to print the required statement that is mailed to the debtor. One way to handle this extra piece of paper is to collect the debtor copies of the cashier receipts on a daily basis and use the Agent Cashier payment entry options to update the account records. You will not be able to print a statement until a payment has been recorded for the plan.

> **NOTE:** The system assumes that printing a copy to your monitor is the same as printing a hard copy. This is considered one copy; to print more than one copy of the payment, see the Reprint A Payment Statement option.

#### Reprint a Payment Statement

This option prints a second copy of a payment statement for a repayment plan. In order to reprint a statement, you must first identify the plan by entering the bill number. Then you need to enter the date the original statement was printed or displayed. The statement dates are shown by the Profile of Repayment option.

### Add an Administrative Cost

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to add to the outstanding balance of an account any administrative charges incurred during the debt collection process. The charges include:

- Internal Revenue Service locator charge
- Department of Motor Vehicles locator charge
- Marshal fees or Court Costs
- Credit report costs
- Consumer reporting agency costs

Select Update Accounts Receivable Option: add an Administrative Cost

Select ACCOUNTS RECEIVABLE BILL NO.: AA0008 000-AA0008 RX CO-PAYMENT/NSC VET 08-18-92 ARpatient,one ACTIVE \$80.99

ADMIN. COST CHARGE DATE: T (OCT 23, 1994)

IRS LOC.COST: 3.00

CREDIT REP.COST: 2.00

DMV LOC.COST: 1.00

CONSUMER REP.AGENCY COST: 5.00

MARSHAL FEE: .50

COURT COST: .50

======================================================================

BILL N0.: 000-AA0008 TRANSACTION DATE: OCT 23,1994

TYPE: ADMIN.COST CHARGE TOTAL TRANS. AMOUNT: 12.00

IRS LOC. COST: 3.00 CREDIT REP.COST: 2.00

DMV LOC.COST: 1.00 CONSUMER REP.AGENCY COST: 5.00

MARSHAL FEE: 0.50 COURT COST: 0.50

======================================================================

Is this correct? NO// Y (YES) \*\*\* DONE\*\*\*

### 3rd Party Information Data Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is provided for editing the Third Party information that is stored along with the bill.

At the time that a bill is entered into the system, either directly by a Billing Clerk or indirectly by another module such as MAS, information about the bill is copied from other files and stored in the Accounts Receivable file. This copied information is used for billing purposes only and can be changed as circumstances require. The files of origin are never changed. Quite often, the AR Clerk will receive the most current information about insurance coverage and debtor's address during the debt collection process.

> **NOTE:** Updating information here with the Edit Debtor's Address option does not alter the Patient file. You should notify MAS of important changes as they occur.

### Update 'Bill Resulting From' Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to edit the "Bill Resulting From" data that appears on all bills.

The "Bill Resulting From" Data is a short phrase used on the follow-up letters to indicate the cause of the bill. If the bill was initially set up with erroneous information, this option gives you a chance to make a correction before the letters are mailed. If you learn, during the course of collecting the debt that a change needs to be made you can use this option to make the correction and the Reprint The Follow-up Letters option to print new letters.

Select Update Accounts Receivable Option: UPDATE 'Bill Resulting From' Data

Select ACCOUNTS RECEIVABLE BILL NO.: AA0008 000-AA0008 RX CO-PAYMENT/NSC VET 08-18-92 ARpatient,one ACTIVE \$92.99

BILL RESULTING FROM: PHARMACY CO-PAYMENT// IMC INPATIENT MEDICAL CARE

...OK? YES//\<ret\> (YES)

### COWC Referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occasionally you will need to refer a veteran patient's bill to the Department of Veterans Benefits Committee on Waivers and Compromises. This option lets you record the date of referral and the amount being referred.

> **NOTE:** These options may be used to correct particular errors caused by incorrect posting of payments.

Select ACCOUNTS RECEIVABLE BILL NO.: AA0008 000-AA0008 RX CO-PAYMENT/NSC VET 08-18-92 ARpatient,one ACTIVE \$92.99#

This account has already been referred to the COWC !

BILL \#: AA0008 DATE REFERRED: 10/23/93 AMOUNT REFERRED: 10

REFERRAL DATE TO COWC: OCT 23,1994//\<ret\>

REFERRED AMOUNT TO COWC: 10// 90

![](prca-4-5-316-ar-release-notes-installation-guide/007.png)

## Adjustments to Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options necessary for applying adjustments to an account. These options affect the principal balance of a bill due to administrative actions. Adjustment to an AR regular adjustment to a bill can decrease or increase the principal balance. Use other appropriate options to process payments and include administrative charges and interest.

### Adjustment to an AR record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-316-ar-release-notes-installation-guide/008.png)

This menu contains options that adjust a debtor's account. These options affect the principal balance of a bill in response to administrative actions. This option is locked with the PRCADJ Security Key.

#### Decrease Adjustment

This option applies a credit transaction to an active bill causing the balance of the bill (and account) to decrease.

Use this option to manually apply decrease transactions to an active bill. A good example of an administrative action that requires an adjustment is a case where MAS has found it necessary to cancel a bill generated by the AR Package. It will be necessary to make a decrease adjustment to the bill, reducing the balance due to zero. The status of the bill will then automatically change to either cancellation or collected/closed.

Situations sometimes arise where a small amount reflecting interest or administrative charges is all that remains of the debt. This occurs because interest and administrative charges are liquidated first, before the payment is applied to the principal balance. A payment of \$100 toward a debt of \$100 plus \$5 interest leaves a principal balance of \$5. Administrative action may be taken to decrease this small balance to zero.

When the balance of a bill is decreased to zero, the status will be automatically changed to either Cancellation or Collected/ Closed. The following criteria determine the new status:

| Status       | Criteria                                          |
|------------------|-------------------------------------------------------|
| Collected/Closed | if the bill contains at least one payment transaction |
| Canceled         | if the bill contains no payment transactions          |

> **NOTE:** If the bill category is Reimbursable Health Insurance, you will be prompted to answer "Contractual Adjustment?: YES//". This decrease transaction will be flagged as Contractual Adjustment.

If the bill has at least one EEOB pending auto-post, you will be prompted to answer “Marked for Auto-Post. Are you sure?”

Select Adjustment to an AR record Option: Decrease Adjustment

Select ACCOUNTS RECEIVABLE BILL NO.: 000-K400025 VENDOR 05-18-94 ARDEBTOR, ONE ACTIVE \$200.00

\*\*\* Transaction \#135 assigned \*\*\*

ADJUSTMENT DATE: t (AUG 26, 1994)

ADJUSTMENT NUMBER: 1//

ADJUSTMENT AMOUNT: 12.00

COMMENTS:

Edit? NO//

==========================================================================

BILL NO.: 000-K400025 ADJUSTMENT AMOUNT: -12.00

ADJUSTMENT DATE: AUG 26,1994 ADJUSTMENT NO.: 1

FISCAL YEAR PAT REF NO. ADJ.AMOUNT PRIN.BAL.(ADJUSTED)

94 -12.00 188.00

Brief Comment: Follow-up Date:

Comments:

==========================================================================

Is this correct? NO// y (YES)

Creating FMS Modified Billing Document...

Document \#33 Created.

#### Increase Adjustment

Use this option to apply a debit transaction to an active bill causing the balance of the bill (and account) to increase.

Use this option to manually apply increase transactions to an active bill. An example of this type of adjustment is a case where an increase in the cost of materials to perform a laboratory test needs to be passed on to the debtor. This is not adjusted automatically, so apply an increase adjustment.

Select Adjustment to an AR record Option: INCREASE Adjustment

Select ACCOUNTS RECEIVABLE BILL NO.: 000-K400025 VENDOR 05-18-94 ARDEBTOR, ONE ACTIVE \$188.00

\*\*\* Transaction \#136 assigned \*\*\*

ADJUSTMENT DATE: t (AUG 26, 1994)

ADJUSTMENT NUMBER: 2//

ADJUSTMENT AMOUNT: 10

COMMENTS:

Edit? NO//

==========================================================================

BILL NO.: 000-K400025 ADJUSTMENT AMOUNT: 10.00

ADJUSTMENT DATE: AUG 26,1994 ADJUSTMENT NO.: 2

FISCAL YEAR PAT REF NO. ADJ.AMOUNT PRIN.BAL.(ADJUSTED)

94 10.00 198.00

Brief Comment: Follow-up Date:

Comments:

==========================================================================Is this correct? NO// y (YES)

Creating FMS Modified Billing Document...

Document \#34 Created.

### waive an accounts receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-316-ar-release-notes-installation-guide/009.png)

This menu contains options necessary for recording a debt waiver. All waivers are at the discretion of the Fiscal Officer. The waived bills will still be kept on file for six years with a status of Write-Off. These options refer to actions taken by the Fiscal Officer. To handle actions taken by District Counsel or Department of Justice, see the DC/DOJ Action menu.

#### Partial Waiver

This option applies a credit transaction to an active bill decreasing the balance by a partial amount. Waivers are logged and tracked within the AR system for the management. This type of transaction can occur at any time during the debt collection cycle. After the amount being waived is entered, the system gives you the opportunity to verify it before proceeding.

Select Waive an Accounts Receivable Option: PARTIAL Waiver

Select ACCOUNTS RECEIVABLE BILL NO.: AA0067 000-AA0067 RX CO-PAYMENT/SC VET 05-28-93 ARpatient,one ACTIVE \$5.69

WAIVED IN PART DATE: T (OCT 23, 1994)

WAIVED AMOUNT: 1.00

=========================================================================

BILL NO.: 000-AA0067 WAIVED AMOUNT: 1.00

WAIVED DATE: OCT 23,1994

FISCAL YEAR PAT REF NO. WAIVED AMOUNT PRIN.BAL.(WAIVED)

93 1.00 0.66

=========================================================================

Is this correct? NO// Y (YES)

#### Full Waiver

This option applies a credit transaction to an account decreasing the balance by the full amount. Waivers are logged and tracked within the AR system for the management.

A Full Waiver makes the bill inactive with a status of Write-off. In the unlikely event that a bill is waived in error, the supervisor will have to take action to re-establish it. You are asked if you are sure that this is the action you want to take, then you are asked for an optional comment.

Select Waive an Accounts Receivable Option: FULL Waiver

Select ACCOUNTS RECEIVABLE BILL NO.: 000-AA0067 RX CO-PAYMENT/SC VETb 05-28-93 ARpatient,one ACTIVE \$4.69

Are you sure you want to record this as a Waiver ? NO// Y (YES)

WAIVED DATE: T (OCT 23, 1994)

COMMENTS:

1\>Couldn't pay this.

2\>\<ret\>

EDIT Option:\<ret\>

### terminate an accounts receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-316-ar-release-notes-installation-guide/010.png)

This menu contains options necessary to stop the debt collection regardless of whether the debt has been paid.

> **NOTE:** A bill that has been waived in full may still require a termination action.

#### Fiscal Officer Terminated

This option terminates an entire bill for no further collection. Choosing this option to terminate a bill changes the bill's status to Write-Off.

This decision is made by the Fiscal Officer. If an entire account is being terminated, each bill must be processed individually. Double question marks will give you a list of the reasons for termination. A comment can be included to make the record more meaningful.

Select Terminate an Accounts Receivable Option: fiscal Officer Terminated

Select ACCOUNTS RECEIVABLE BILL NO.: AA0008 000-AA0008 RX CO-PAYMENT/NSC VET 08-18-92 ARpatient,one ACTIVE \$87.99

Are you sure you want to record this as a Termination ? NO// y (YES)

TERMINATION DATE: t (OCT 23, 1994)

TERMINATION REASON: WAIVED

COMMENTS:

1\>CAN'T PAY!!

2\>\<ret\>

EDIT Option:\<ret\>

#### Compromise Termination

This option terminates a portion of an active bill for no further collection. Choosing this option to terminate an active bill changes the bill's status to Write-Off.

This decision is made by the Fiscal Officer. If an entire account is being terminated, each bill must be processed individually. A comment can be included to make the record more meaningful.

### re-establish a bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option re-establishes an inactive bill changing its status back to Active. Valid bills to re-establish include bills with the following status:

Suspended

Cancellation

Collected/Closed

Write-Off

Options to apply this transaction to an account will prompt for a bill, an amount, and a comment. The amount prompt will only appear if the bill has no balance (\$0.00); however, if the bill had a previous balance, the system will automatically re-establish the bill for that amount. Finally, the comment will appear in the description column of the patient statement for the veteran to see.

For example, this supports documenting bankruptcy actions for veterans who have attempted to file bankruptcy. A "transaction" to re-establish an amount should be created, and a prompt for a comment about why this amount is being suspended. A comment like "Patient did not qualify for Bankruptcy" could be entered and would appear on the patient statement to describe why that amount was added to the statement balance.

Select Adjustment to Accounts Receivable Option: RE-Establish Bill

SITE: ALTOONA VAMC//\<ret\> PENNSYLVANIA 000

Select ACCOUNTS RECEIVABLE BILL NO.: AA0045 000-AA0045 RX CO-PAYMENT/NSC VET 01-27-93 ARpatient,one SUSPENDED \$268.25

Are you sure you wish to re-establish this bill? NO// Y (YES)

COMMENTS:

000-AA0045 is in the ACTIVE status for \$268.25

### suspend a bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option suspends a bill changing its current status to Suspended. The amount to suspend is added to the account balance.

Options to apply this transaction to an account will prompt for a "comment". This comment will appear in the description column of the patient statement. For example, this supports documenting bankruptcy actions for those veterans who have filed bankruptcy. A transaction to suspend an amount would be chosen, and a prompt for a comment about why this amount is being suspended. A comment like "Claimed Bankruptcy" is entered and appears on the patient statement to describe why that amount was subtracted from the statement balance.

Select Adjustment to Accounts Receivable Option: SUSPEND an AR bill

Select ACCOUNTS RECEIVABLE BILL NO.: AA0023 000-AA0023 C (MEANS TEST)

09-04-92 ARpatient,one ACTIVE \$75.50

Are you sure you want to record this as a Suspension ? NO// Y (YES)

SUSPENDED DATE: T (OCT 23, 1994)

COMMENTS:

1\>Suspending because we don't know if he really can claim bankruptcy

2\>yet.

3\>\<ret\>

EDIT Option:\<ret\>

## Report Menu for Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-316-ar-release-notes-installation-guide/011.png)

This menu contains report options for the Accounts Receivable Package. Reports formatted for 80 columns can be viewed on your CRT screen or sent to a printer. Reports designed for 132 columns should be printed. If you decide to send a report to a printer, you can queue the output; that is, you can release the report to the system which will send it to the printer along with other jobs in the queue.

![](prca-4-5-316-ar-release-notes-installation-guide/012.png)

### Accounts Receivable Status Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu provides options to display bill listings by status, category, or referrals.

#### DC Pending Referral AR Listing

This report displays a listing of bills that may need to be referred to the District Counsel for collection proceedings. Running this report on a weekly basis will alert you when bills have become past due.

#### DOJ Pending Referral Listing

This report shows a listing of bills that may need to be referred to the Department of Justice for collection proceedings. Running this report on a weekly basis alerts you when bills have become past due.

#### category listing for bills

This option displays a report of all bills within a given category. Valid categories include the following:

| Require Code Sheets to become an ACTIVE bill |                               |
|--------------------------------------------------|-------------------------------|
| Vendor                                           | Tort Feasor                   |
| Military                                         | Category C (Means Test)       |
| Medicare                                         | Emergency/Humanitarian        |
| InterAgency                                      | Crime of Personal Violence    |
| Ex-Employee                                      | Ineligible Hosp.              |
| Current Employee                                 | No-Fault Auto Accident        |
| Sharing Agreements                               | Federal Agency-Refund         |
| Rx Co-Payment                                    | Federal Agency-Reimburse      |
| Workman's Compensation                           | Reimbursable Health Insurance |
| Hospital Care Per Diem                           | Nursing Home Care Per Diem    |
| RX Co-Payment (NSC)                              | RX Co-Payment (SC)            |

Select Accounts Receivable Status Reports Option: CATEGory Listing for Bills

START WITH CATEGORY: FIRST//\<ret\>

START WITH CURRENT STATUS: FIRST//\<ret\>

DEVICE:\<ret\> VIRTUAL RIGHT MARGIN: 80//\<ret\>

AR CATEGORY/STATUS LIST OCT 23,1994 11:10 PAGE 1

PRINCIPAL CURRENT

BILL NO. DEBTOR CAT. STATUS BALANCE BALANCE

-------------------------------------------------------------------------

10000-AA008 ARpatient,one C A 249.00 265.00

000-AA0001 ARpatient,two PN CC 0.00 0.00

000-AA0003 ARpatient,three C WO 499.09 500.00

000-AA0006 ARpatient,four PS CC 0.00 0.00

000-AA0007 ARpatient,five PN OB 10.00 10.00

000-AA0008 ARpatient,six PN WO 75.99 87.99

000-AA0010 ARpatient,seven PS CN 0.00 0.00

000-AA0011 ARpatient,eight PS CC 20.00 20.00

000-AA0012 ARpatient,nine PS CC 0.00 0.00

000-AA0014 ARpatient,ten PN CC 0.00 0.00

000-AA0016 ARpatient,eleven PN A 50.00 50.00

TOTAL 904.58 932.99

COUNT 11 11

MEAN 60.27 62.20

MINIMUM 0.00

MAXIMUM 499.09

DEV. 137.68

#### Status Listing for Bills

This option lists all bills with a given status. This report will contain the bill's number, date, debtor, and balance. In addition, a summary will appear at the end of the report which will show the total number of bills with this status and the total balance of all bills with this status. To view this report, enter the status name at the system prompt

Select AR - Accounts Receivable Menu Option: STATUS Listing For Bills

List for STATUS: OPEN

DEVICE: HOME//\<ret\> VIRTUAL RIGHT MARGIN: 80//\<ret\>

Status: OPEN

Bill no. Date Prepared Category Debtor Balance

------------------------------------------------------------------------

000-AA0054 NOV 1,1992 RX CO-PAYMENT/N ARpatient,one 8.00

000-K10044 JUL 14,1994 PREPAYMENT ARpatient,two 7.00

000-K10056 OCT 1,1994 PREPAYMENT ARpatient,three 20.00

000-K20187 OCT 22,1994 RX CO-PAYMENT/S \*ARpatient,four 10.00

000-K20188 OCT 22,1994 RX CO-PAYMENT/N ARpatient,five 2.00

TOTAL: 47.00

COUNT: 5.00

MEAN: 9.40 \* -indicates that patient is deceased

#### Refunds to be approved by certifying official

This option allows the user to print all refunds which are pending approval by a certifying official. (See ‘Refund Review and Approve for more information.)

### Delinquent AR Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-316-ar-release-notes-installation-guide/013.png)

This menu contains report options which display accounts that have been in debt for the number of days specified. Since the date range is built into the print specifications, these reports can be set up by the IRM/Site Management Office to run on a recurring basis.

The reports show bills on an individual basis. An account can have multiple bills that are delinquent. Each one will show as a separate line entry. The column heading ICD refers to the Interest Computation Date for that bill. That is the date of the first follow-up letter.

#### 31-90 delinquent accounts

This option displays all delinquent bills that have been in debt anywhere between 31 and 90 days. Use this option to obtain debtors to follow-up for collection of these debts.

#### 91-180 days delinquent accounts

This option displays all delinquent bills that have been in debt anywhere between 91 and 180 days. Use this option to obtain debtors to follow-up for collection of these debts.

#### 181-365 days delinquent accounts

This option displays all delinquent bills that have been in debt anywhere between 181 and 365 days. Use this option to obtain debtors to follow-up for collection of these debts.

#### over 365 days delinquent accounts

This option displays all delinquent bills that have been in debt over 365 days. Use this option to obtain debtors to follow-up for collection of these debts.

#### print all delinquent accounts

This option displays all bills that are more than 30 days delinquent. Use this option to obtain debtors to follow-up for collection of these debts.

#### report of AR by last activity date 

This option displays a report of all bills that have had no activity before a given date. Typically, these are bills that have been unresolved. The "last activity date" is defined as the following:

> Last time a letter printed (LETTER1, LETTER2, LETTER3)

> Date bill was prepared

> Date status was last updated

> Date the last transaction was entered into the system or Transaction date

Report of AR Last Activity before 02/16/93 OCT 24,1994 22:12 PAGE 1

CURRENT CURRENT DATE OF LAST

BILL NO. STATUS DEBTOR BALANCE ACTIVITY

CATEGORY DATE BILL PREPARED

-------------------------------------------------------------------------

000-AA0079 ACTIVE ARpatient,one 100.00 JAN 12,1994

C (MEANS TES JAN 12,1994

000-AA0080 ACTIVE ARpatient,two 125.00 JAN 14,1994

C (MEANS TES JAN 12,1994

------------

SUBTOTAL 225

SUBCOUNT 2

SUBMEAN 112.50

![](prca-4-5-316-ar-release-notes-installation-guide/014.png)

### Management Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains report options that allow management to get an overview of the debt collection system in its entirety.

### From: PRCA*4.5*315 AR Release Notes/Installation Guide

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the HAPE FY16 Revenue Enhancements Accounts Receivable patch PRCA\*4.5\*315 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. Successful deployment and installation of this patch is dependent upon a fully functional and existing VistA system with functional links with FMS and with Central Fee at the Austin Information Technology Center (AITC).

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. The only constraints associated with the patch installation are the required patches as mentioned in the patch description and on the Forum National Patch Module (NPM).

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for 30 days starting with the National Release date and concluding with the National Compliance date by which time all 130 VistA production instances should have the patch installed.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the HAPE FY16 Revenue Enhancements Accounts Receivable patch PRCA\*4.5\*315 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for a VistA patch.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All 130 VistA production instances. The IOC test sites for this project were Durham (558) and Central Alabama HCS (619).

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None required other than prerequisite patch installation as described in the patch description and in the Forum NPM.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HAPE FY16 Revenue Enhancements Accounts Receivable patch PRCA\*4.5\*315 is a VistA patch and does not require any special or specific resources other than an existing and functional VistA system.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific hardware required other than that which already hosts the VistA system. This is a software enhancement that will not require additional hardware.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific software required other than that which already hosts the VistA system.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA patches are nationally released from the Forum National Patch Module (NPM) the patch is automatically sent to the targeted VistA systems nationwide. When VistA patches are installed at a site, a notification is sent back to the NPM to track which sites have and have not installed a patch. This is part of the standard VistA patch notifications and communications protocols.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the patch PRCA\*4.5\*315, which is tracked in the NPM in Forum, nationally to all VAMCs. Forum automatically tracks the patches as they are installed in the different VAMC production systems as described in the previous section. One can run a report in Forum to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run, to identify which sites have not installed the patch in their VistA production system as of that moment in time.

Therefore, this information does not need to be manually tracked in the chart below. The table is included below if manual tracking is desired and because it is part of the VIP document template.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. The only pre-installation and system requirements for deployment and installation of this patch are the prerequisite patches which need to be installed before this patch can be installed.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. There are three patches for this project and they must be installed in the following order:

1.  PRCA\*4.5\*315
2.  IB\*2\*568
3.  PSO\*7\*463

Sites should install patches into the test/mirror/pre-prod accounts before the production account as is the normal VistA patch installation standard convention.

When installing any VistA patch, sites should utilize the option “Backup a Transport Global” in order to create a backup message of any routines exported with this patch.

Post-installation checksums are found in the patch description and in Forum NPM.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install this VistA patch, the patch installer must be an active user on the VistA system and have access to the VistA menu option “Kernel Installation & Distribution System” \[XPD MAIN\] and have VistA security keys XUPROG and XUPROGMODE. Knowledge on how to install VistA patches using the items on this menu option is also a required skill.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

--------------------------

This process will install new and updated routines and other

components listed above. There is a post-install routine that will add

entries to a number of files.

The patch will be released in conjunction with an Integrated Billing

patch, IB\*2.0\*568, and an Outpatient Pharmacy patch, PSO\*7.0\*463.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NOTE \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

IF A USER IS ON THE SYSTEM AND USING THESE PROGRAMS

AN EDITED ERROR WILL OCCUR.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Installation will take less than 15 minutes.

Suggested time to install: non-peak requirement hours.

1\. Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation & Distribution System menu, select

the Installation menu.

4\. From this menu, you may select to use the following options

(when prompted for INSTALL NAME, enter PRCA\*4.5\*315):

a\. Verify Checksums in Transport Global - This option will

allow you to ensure the integrity of the routines that are

in the transport global.

b\. Print Transport Global - This option will allow you to

view the components of the KID build.

c\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of

this patch (routines, DD's, templates, etc.).

d\. Backup a Transport Global - This option will create a

backup message of any routines exported with this patch.

It will not backup any other changes such as DD's or

templates.

5\. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of

Install? YES//" respond YES

6\. When prompted "Want KID to INHIBIT LOGONs during the install?

NO//" respond NO.

7\. When prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//, enter 'NO'

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify completed installation by comparing the post-install routine checksums against the published checksums in the patch description and in Forum NPM.

Another verification method is to ensure that the build components as listed in the patch description have been correctly installed onto the target VistA system.

## Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out plan for VistA applications is complex and is not able to be a “one size fits all” strategy. The general strategy for VistA software back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch; otherwise, the site should contact the Enterprise Program Management Office (EPMO) directly for specific solutions to their unique problems.

Although it is unlikely due to care in collecting approved requirements, SQA/PBM review and multiple testing stages (Primary Developer, Secondary Developer, and Component Integration Testing) a back-out decision due to major issues with this patch could occur during site Mirror Testing, Site Production Testing or after National Release to the Field. The strategy would depend on during which of these stages the decision is made. If during Site Production Testing, unless the patch produces catastrophic problems, the normal VistA response would be for a new version of the test patch correcting defects to be produced, retested and upon successfully passing development team testing would be resubmitted to the site for testing. This project, however, has prepared a set of back-out patch instructions if necessary, as in the case that the project is canceled or the implemented design is found to be so wrong and detrimental to the site’s delivery of services to Veterans that the software must be removed. If the defects were not discovered until after national release but during the 30 days support period, a new patch will be entered into the National Patch Module on Forum and go through all the necessary milestone reviews etc. as an emergency patch. After 30 days, the VistA Maintenance Program would produce the new patch, either to correct the defective components or to back-out.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to determine if a wholesale back-out of the patch PRCA\*4.5\*315 is needed or if a better course of action is to correct through a new version of the patch (if prior to national release) or through a subsequent patch aimed at specific areas modified or affected by the original patch (after national release). A wholesale back-out of the patch will still require a new version (if prior to national release) or a subsequent patch (after national release). If the back-out is post-release of patch PRCA\*4.5\*315, this patch should be assigned status of “Entered in Error” in Forum’s NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is detailed in the User Stories in Rational Tools Management.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to back-out this VistA patch will be made by Health Product Support, CPAC Revenue System Management staff, and the Development Team. Criteria to be determined based on separate and unique factors and will be evaluated upon post-patch installation use of the product.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out authorization will be determined by a consensus consisting of the following individuals:

- Health Product Support Management
- Release Managers
- CPAC Revenue System Managers
- Development Team

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA Installation Procedure of the KIDS build, the installer can back up the modified routines using the ‘Backup a Transport Global’ action. The installer can restore the routines using the MailMan message that were saved prior to installing the patch. The back-out procedure for global, data dictionary and other VistA components is more complex and will require issuance of a follow-up patch to ensure all components are properly removed. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with restoration of the data. This back-out may need to include a database cleanup process.

Please contact the EPMO for assistance if the installed patch that needs to be backed out contains anything at all besides routines before trying to back-out the patch. If the installed patch that needs to be backed out includes a pre or post install routine, please contact the EPMO before attempting the back-out.

From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch \#.

    a. Backup a Transport Global - This option will create a backup

       message of any routines exported with this patch. It will not

       backup any other changes such as DD's or templates.

Locate the Transport Global Backup message which should have been created as a part of the patch installation and restore the software from that Packman message containing the pre-installation version of the routines. If this message was not created or cannot be found, then contact Health Product Support for help in generating a new Packman message from another source.

In addition to backing out and restoring the previous versions of the routines, the following software components will also need to be backed-out. The safest thing to do is to work with Health Product Support and the Development Team to create a separate build containing these non-routine software components from an environment in which this patch has not been installed.

- Input Template: PRCAE ADMIN associated with File# 433
- Parent Menu options “Repayment Plan Menu \[PRCAC REPAYMENT MENU\]” and “Cross-Servicing Menu” \[RCTCSP MENU\] and all of the child menu items on these parent menus.
- Security key PRCAF LATE CHARGES may be deleted upon a back-out
- List template \[RCDP ACCOUNT PROFILE\] and associated parent menu protocol \[RCDP ACCOUNT PROFILE MENU\] and all associated child action protocols should be rolled back to the previous version via a new patch build
- New List templates and associated new menu and action protocols may remain on the system without rolling them back without risk.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The success of the back-out can be verified by verifying checksums for the routines removed to validate that they reflect the nationally released checksums.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to determine if a wholesale rollback of the data associated with patch PRCA\*4.5\*315 is needed or if a better course of action is to correct the data through a new version of the patch (if prior to national release) or through a subsequent patch aimed at specific areas modified or affected by the original patch (after national release). A wholesale rollback of the data associated with this patch will still require a new version (if prior to national release) or a subsequent patch (after national release).

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to rollback the data associated with this VistA patch will be made by Health Product Support, CPAC Revenue System Management staff, and the Development Team. Criteria to be determined based on separate and unique factors and will be evaluated upon post-patch installation use of the product.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback risks include being able to restore the database to what it looked like before this patch was installed without introducing database corruption. For example, new AR categories are being added by this patch into the ACCOUNTS RECEIVABLE CATEGORY file (#430.2) and new revenue source codes are being added by this patch into the REVENUE SOURCE CODE file (#347.3). These are core AR dictionary files. If subsequent AR bills are created for one of the new AR categories and/or revenue source codes, and it is decided that a full rollback of this data is needed, then a decision needs to be made as to what to do with new bills with these new AR categories and/or revenue source codes.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback of the data associated with this patch will be determined by a consensus consisting of the following individuals:

- Health Product Support Management
- Release Managers
- CPAC Revenue System Managers
- Development Team

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that all of the above data components have been removed from the system as described in the previous section.

Template Revision History

| Date          | Version | Description                                                                                                                                                                                                                              | Author                                 |
|---------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| March 2016    | 2.2     | Changed the title from Installation, Back-Out, and Rollback Guide to Deployment and Installation Guide, with the understanding that Back-Out and Rollback belong with Installation.                                                      | VIP Team                               |
| February 2016 | 2.1     | Changed title from Installation, Back-Out, and Rollback Plan to Installation, Back-Out, and Rollback Guide as recommended by OI&T Documentation Standards Committee                                                                      | OI&T Documentation Standards Committee |
| December 2015 | 2.0     | The OI&T Documentation Standards Committee merged the existing *“Installation, Back-Out, Rollback Plan”* template with the content requirements in the OI&T End-user Documentation Standards for a more comprehensive Installation Plan. | OI&T Documentation Standards Committee |
| February 2015 | 1.0     | Initial Draft                                                                                                                                                                                                                            | Lifecycle and Release Management       |

### From: PRCA*4.5*339 AR Release Notes/Installation Guide

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for a VistA patch.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All 130 VistA production instances. The IOC test sites for this project were Durham (558) and Central Alabama HCS (619).

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None required other than prerequisite patch installation as described in the patch description and in the Forum NPM.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific hardware required other than that which already hosts the VistA system. This is a software enhancement that will not require additional hardware.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific software required other than that which already hosts the VistA system.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA patches are nationally released from the Forum National Patch Module (NPM) the patch is automatically sent to the targeted VistA systems nationwide. When VistA patches are installed at a site, a notification is sent back to the NPM to track which sites have and have not installed a patch. This is part of the standard VistA patch notifications and communications protocols.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the patch PRCA\*4.5\*339, which is tracked in the NPM in Forum, nationally to all VAMCs. Forum automatically tracks the patches as they are installed in the different VAMC production systems as described in the previous section. One can run a report in Forum to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run, to identify which sites have not installed the patch in their VistA production system as of that moment in time.

Therefore, this information does not need to be manually tracked in the chart below. The table is included below if manual tracking is desired and because it is part of the VIP document template.

Table 6: 3.3.4.1 Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is detailed in the User Stories in Rational Tools Management.

### From: PRCA*4.5*295 AR Release Notes/Installation Guide

## Documentation Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to FTP the files from REDACTED.

This transmits the files from the first available FTP server. Sites may

also elect to retrieve software directly from a specific server as follows:

Albany REDACTED

Hines REDACTED\>

Salt Lake City REDACTED

The documentation will be in the form of Adobe Acrobat files.

Documentation can also be found on the VA Software Documentation Library at:

REDACTED

Title File Name FTP Mode

----------------------------------------------------------------------

AR Release Notes/Installation PRCA_4_5_P295_RN.PDF Binary

Guide (PRCA\*4.5\*295)

*(This page included for two-sided copying.)*

## Functional Specifications for Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- For affected AR codes, the data that was transmitted in a manual transfer before the enhancement matches the format and content of the data that is transmitted in a manual transfer after the enhancement.
- For affected AR codes, the data is automatically transferred to FMS and the data format and content match the manual transfer format and content.

### Transfer to FMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Transfer to TRICARE Claims to FMS

The VistA system automatically transferred TRICARE claims to FMS for specific account receivable codes. Previously, this was a manual process.

### From: PRCA*4.5*300 AR Release Notes/Installation Guide

## System Feature: Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Data Dictionary – Bill Number Length – Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for the Bill No. field (.01 field) of the Accounts Receivable file (file 430) to store a 6-10 character claim number plus a 3 character station number and a hyphen.

### From: PRCA*4.5*302 AR Release Notes/Installation Guide

## System Feature: EDI Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EDI Transactions – Use HPID/OEID in EDI Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software provides the ability to transmit and receive HPID/OEID in all applicable EDI transactions.

<u>Note:</u> Certification of the HPID/OEID is a requirement of payers, not providers.

### From: PRCA*4.5*275 AR Release Notes/Installation Guide

## Hardware Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special hardware considerations.

## System Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special system considerations.

## Installation and Configuration Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IB\*2\*447 and PRCA\*4.5\*275 (E-claims5-5010) should be installed as a Multi-Build (Host-file) installation, using the KIDS Installation 6 (Install package) option. Please refer to the patch description for instructions on where to download the multi-patch host file. Please also note for Step 4b of the KIDS Patch Description, if you select option \#1 to run a Full Comparison you will get a system error: \<UNDEFINED\>S+1^DIQ ^IBA(364.6,2209,0) due to a known issue with the KIDS Full Compare option (see Remedy Ticket \# HD0000000449218). You can run any of the other 3 compare options without issue.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Security Key Changes for Patch PCRA\*4.5\*275
