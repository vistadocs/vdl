---
title: Accounts Receivable Version 4.5 ePayments User Manual (EDI Lockbox)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: ePayments  (EDI Lockbox)
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5
group_key: "PRCA:PRCA:4.5"
file_numbers: []
security_keys: []
menu_options: 12
description: 
audience: 
keywords: 
  - report
  - auto
  - total
  - table
  - number
  - contents
  - amount
  - date
  - receipt
  - payment
page_count: 0
word_count: 59685
section_count: 75
table_count: 11
figure_count: 1
appendix_count: 5
has_toc: False
is_stub: False
pub_date: December 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/ePayments_edi_lockbox_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/ePayments_edi_lockbox_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>ePayments

  (Electronic Data Interchange \[EDI\] Lockbox)

  <span id="_Toc311740987" class="anchor"></span>User Manual
---

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/001.png)

December 2025

Office of Information and Technology

Revision History

| Date           | Revision | Description                                                                           | Project Manager                            | Technical Writer                           |
|----------------|----------|---------------------------------------------------------------------------------------|--------------------------------------------|--------------------------------------------|
| December 2025  | 25.0     | ePayments Patch updates for PRCA\*4.5\*450                                            | VHA HF DSO MCCF ePayments Development Team | VHA HF DSO MCCF ePayments Development Team |
| August 2025    | 24.0     | ePayments Patch updates for PRCA\*4.5\*446                                            | VHA HF DSO MCCF ePayments Development Team | VHA HF DSO MCCF ePayments Development Team |
| May 2025       | 23.0     | ePayments Patch updates for PRCA\*4.5\*439                                            | MCCF EDI TAS ePayments Development Team    | MCCF EDI TAS ePayments Development Team    |
| October 2024   | 22.0     | ePayments Patch updates for PRCA\*4.5\*432                                            | MCCF EDI TAS ePayments Development Team    | MCCF EDI TAS ePayments Development Team    |
| June 2024      | 21.0     | ePayments Patch updates for PRCA\*4.5\*436                                            | MCCF EDI TAS ePayments Development Team    | MCCF EDI TAS ePayments Development Team    |
| April 2024     | 20.0     | ePayments Patch updates for PRCA\*4.5\*424                                            | MCCF EDI TAS ePayments Development Team    | MCCF EDI TAS ePayments Development Team    |
| November 2023  | 19.0     | ePayments Patch updates for PRCA\*4.5\*409                                            | MCCF EDI TAS ePayments Development Team    | MCCF EDI TAS ePayments Development Team    |
| January 2023   | 18.0     | ePayments Patch updates for PRCA\*4.5\*371                                            | MCCF EDI TAS ePayments Development Team    | MCCF EDI TAS ePayments Development Team    |
| July 2022      | 17.0     | ePayments Patch updates for PRCA\*4.5\*367                                            | MCCF EDI TAS ePayments Development Team    | MCCF EDI TAS ePayments Development Team    |
| March 2022     | 16.0     | ePayments Patch updates for PRCA\*4.5\*380                                            | MCCF EDI TAS ePayments Development Team    | MCCF EDI TAS ePayments Development Team    |
| November 2021  | 15.0     | ePayments Patch updates for PRCA\*4.5\*349                                            | MCCF EDI TAS ePayments Development Team    | MCCF EDI TAS ePayments Development Team    |
| June 2021      | 14.0     | ePayments Patch updates for PRCA\*4.5\*375                                            | MCCF EDI TAS ePayments Development Team    | MCCF EDI TAS ePayments Development Team    |
| October 2020   | 13.0     | ePayments Patch updates for PRCA\*4.5\*345                                            | REDACTED                                   | REDACTED                                   |
| March 2019     | 12.0     | ePayments Patch updates for PRCA\*4.5\*332                                            | REDACTED                                   | REDACTED                                   |
| November 2018  | 11.0     | ePayments Patch updates for PRCA\*4.5\*326                                            | REDACTED                                   | REDACTED                                   |
| June 2018      | 10.0     | ePayments Patch updates for PRCA\*4.5\*321                                            | REDACTED                                   | REDACTED                                   |
| October 2017   | 9.0      | ePayments Patch updates for PRCA\*4.5\*318                                            | REDACTED                                   | REDACTED                                   |
| March 2017     | 8.0      | ePayments Patch updates for PRCA\*4.5\*317                                            | REDACTED                                   | REDACTED                                   |
| August 2016    | 7.0      | ePayments Patch updates for PRCA\*4.5\*316                                            | REDACTED                                   | REDACTED                                   |
| May 2016       | 6.0      | Comprehensive updates throughout in accordance with PRCA\*4.5\*303 and PRCA\*4.5\*304 | REDACTED                                   | REDACTED                                   |
| March 2015     | 5.0      | ePayments Patch updates: PRCA\*4.5\*298                                               | REDACTED                                   | REDACTED                                   |
| July 2012      | 4.0      | Changes for deposit ticket number patch PRCA\*4.5\*283 (page 56).                     | REDACTED                                   | REDACTED                                   |
| April 2012     | 3.0      | Patch updates: PRCA\*4.5\*284                                                         | REDACTED                                   | REDACTED                                   |
| January 2012   | 2.0      | ePayments II updates - patches IB\*2.0\*451 and PRCA\*4.5\*276                        | REDACTED                                   | REDACTED                                   |
| September 2011 | 1.0      | Initial Release                                                                       | REDACTED                                   | REDACTED                                   |

<span id="_Toc183424285" class="anchor"></span>Table 1: Terms

Table of Contents

List of Figures

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Business Uses](#business-uses)
  - [Timeframes](#timeframes)
  - [Patches](#patches)
    - [AR Patch PRCA\4.5\284](#ar-patch-prca45284)
    - [AR Patch PRCA\4.5\303](#ar-patch-prca45303)
    - [AR Patch PRCA\4.5\304](#ar-patch-prca45304)
    - [AR Patch PRCA\4.5\316](#ar-patch-prca45316)
    - [AR Patch PRCA\4.5\317](#ar-patch-prca45317)
    - [AR Patch PRCA\4.5\318](#ar-patch-prca45318)
    - [AR Patch PRCA\4.5\321](#ar-patch-prca45321)
    - [AR Patch PRCA\4.5\326](#ar-patch-prca45326)
    - [AR Patch PRCA\4.5\332](#ar-patch-prca45332)
    - [AR Patch PRCA\4.5\345](#ar-patch-prca45345)
    - [AR Patch PRCA\4.5\375](#ar-patch-prca45375)
    - [AR Patch PRCA\4.5\349](#ar-patch-prca45349)
    - [AR Patch PRCA\4.5\380](#ar-patch-prca45380)
    - [AR Patch PRCA\4.5\367](#ar-patch-prca45367)
    - [AR Patch PRCA\4.5\371](#ar-patch-prca45371)
    - [AR Patch PRCA\4.5\409](#ar-patch-prca45409)
    - [AR Patch PRCA\4.5\424](#ar-patch-prca45424)
    - [AR Patch PRCA\4.5\436](#ar-patch-prca45436)
    - [AR Patch PRCA\4.5\432](#ar-patch-prca45432)
    - [AR Patch PRCA\4.5\439](#ar-patch-prca45439)
    - [AR Patch PRCA\4.5\446](#ar-patch-prca45446)
    - [AR Patch PRCA\4.5\450](#ar-patch-prca45450)
  - [New Terminology](#new-terminology)
  - [Process Flow](#process-flow)
  - [Process Flow, OGC Exception](#process-flow-ogc-exception)
- [Getting Started with ePayments](#getting-started-with-epayments)
  - [Menus and Screens](#menus-and-screens)
    - [ERA List – Worklist Screen](#era-list-worklist-screen)
    - [ERA Worklist / Scratchpad Screen](#era-worklist-scratchpad-screen)
    - [ERA / 835 Screens for ePayments](#era-835-screens-for-epayments)
    - [Action Option: RX ECME Information](#action-option-rx-ecme-information)
    - [Action Option: AR Account Profile](#action-option-ar-account-profile)
    - [Action Option: CM Comment History](#action-option-cm-comment-history)
    - [Action Option: PE Print EEOB](#action-option-pe-print-eeob)
    - [Action Option: CI Go to Claim Screen](#action-option-ci-go-to-claim-screen)
    - [Action Option: BC Bill Charges](#action-option-bc-bill-charges)
    - [Action Option: IR Insurance Reviews](#action-option-ir-insurance-reviews)
    - [Action Option: AD Additional 835 Data](#action-option-ad-additional-835-data)
    - [Action Option: VP Policy Benefits](#action-option-vp-policy-benefits)
    - [Action Option: EL Patient Eligibility](#action-option-el-patient-eligibility)
    - [Action Option: RP Receipt Profile](#action-option-rp-receipt-profile)
    - [Action Option: EX Exit](#action-option-ex-exit)
  - [Parameters](#parameters)
    - [Parameters Report – EDI Lockbox (ePayments) Parameters Report](#parameters-report-edi-lockbox-epayments-parameters-report)
    - [Parameters Report – EDI Lockbox (ePayments) Parameters Audit Report](#parameters-report-edi-lockbox-epayments-parameters-audit-report)
    - [Parameters Report – EDI Lockbox Exclusion Audit Report](#parameters-report-edi-lockbox-exclusion-audit-report)
  - [Mail Groups](#mail-groups)
  - [How to Read an ERA / 835](#how-to-read-an-era-835)
  - [Workload Notifications](#workload-notifications)
    - [Unmatched ERAs \> 30 Days](#unmatched-eras-30-days)
    - [PAPER Matched / Not Posted ERAs \> 30 Days](#paper-matched-not-posted-eras-30-days)
    - [EFT Matched / Not Posted ERAs \> 30 Days Bulletin](#eft-matched-not-posted-eras-30-days-bulletin)
    - [Unmatched EFTs \> 14 Days](#unmatched-efts-14-days)
    - [Suspense Entry Bulletin](#suspense-entry-bulletin)
- [Payments Processing](#payments-processing)
  - [Check Email](#check-email)
  - [Exception Processing](#exception-processing)
    - [Transmission Exceptions](#transmission-exceptions)
    - [Data Exceptions](#data-exceptions)
    - [Non-Released Prescriptions](#non-released-prescriptions)
  - [Working the EEOB Scratchpad](#working-the-eeob-scratchpad)
    - [ERA List – Worklist Actions](#era-list-worklist-actions)
    - [Worklist Actions](#worklist-actions)
    - [Change View](#change-view)
    - [Research Menu Actions](#research-menu-actions)
    - [Example of Processing a Paper Check and ERA](#example-of-processing-a-paper-check-and-era)
    - [Example of Processing a Matched ERA and EFT](#example-of-processing-a-matched-era-and-eft)
  - [Auto-Posting Claims](#auto-posting-claims)
    - [Medical Auto-Posting Candidates](#medical-auto-posting-candidates)
    - [Medical Auto-Posting Create and Process Receipt](#medical-auto-posting-create-and-process-receipt)
    - [Medical Auto-Posting Receipts](#medical-auto-posting-receipts)
    - [Pharmacy Auto Posting Receipts](#pharmacy-auto-posting-receipts)
    - [EEOB Worklist](#eeob-worklist)
    - [Ignore Payment Retraction Pairs](#ignore-payment-retraction-pairs)
    - [Status Change](#status-change)
    - [AR Display](#ar-display)
  - [Working the APAR List](#working-the-apar-list)
    - [APAR – Actions](#apar-actions)
    - [APAR Scratchpad – Actions](#apar-scratchpad-actions)
  - [Auto-Decrease of Medical Claims](#auto-decrease-of-medical-claims)
    - [Decrease Adjustment Warning Messages](#decrease-adjustment-warning-messages)
  - [Auto-Decrease of Pharmacy Claims](#auto-decrease-of-pharmacy-claims)
- [The EFT Has Been Accepted by FMS](#the-eft-has-been-accepted-by-fms)
  - [FMS](#fms)
  - [Three Day EFT Cycle](#three-day-eft-cycle)
  - [EFT Deposits](#eft-deposits)
- [NPI (National Provider Identifier)](#npi-national-provider-identifier)
- [Additional Functionality](#additional-functionality)
  - [Auto–Audit](#autoaudit)
    - [Update Rate Types for Auto-Audit](#update-rate-types-for-auto-audit)
    - [Process Open Bills / Paper Claims](#process-open-bills-paper-claims)
    - [Validate Bill Data and Status](#validate-bill-data-and-status)
    - [Process AR Entry](#process-ar-entry)
    - [Required Security Key](#required-security-key)
  - [Automatic Match EFTs to ERAs Acronym: MA](#automatic-match-efts-to-eras-acronym-ma)
  - [EFT Manual Match Acronym: MM](#eft-manual-match-acronym-mm)
  - [Mark Ø-Balance EFT Matched Acronym: ZB](#mark-ø-balance-eft-matched-acronym-zb)
  - [Unmatch an ERA Acronym: UN](#unmatch-an-era-acronym-un)
  - [Update ERA Posted using Paper EOB Acronym: UP](#update-era-posted-using-paper-eob-acronym-up)
  - [Remove ERA from Active Worklist Acronym: REM](#remove-era-from-active-worklist-acronym-rem)
  - [EEOB Move / Copy / Remove Acronym: MCR](#eeob-move-copy-remove-acronym-mcr)
  - [Remove Duplicate EFT Deposits Acronym: REFT](#remove-duplicate-eft-deposits-acronym-reft)
  - [EEOB Indicator](#eeob-indicator)
  - [Receipt Processing](#receipt-processing)
  - [Unposted EFT Override Acronym: OEFT](#unposted-eft-override-acronym-oeft)
  - [Identify Payers Acronym: IDP](#identify-payers-acronym-idp)
  - [Remove Unbalanced Deposit Flag: UBD](#remove-unbalanced-deposit-flag-ubd)
- [EDI Lockbox (ePayments) Reports Menu Acronym: REP](#edi-lockbox-epayments-reports-menu-acronym-rep)
  - [EFT Daily Activity Report Acronym: DA](#eft-daily-activity-report-acronym-da)
    - [When to Run this Report](#when-to-run-this-report)
    - [How to Run this Report](#how-to-run-this-report)
  - [EFT Unmatched Aging Report Acronym: EFT](#eft-unmatched-aging-report-acronym-eft)
    - [When to Run this Report](#when-to-run-this-report-1)
    - [How to Run this Report](#how-to-run-this-report-1)
  - [ERA Unmatched Aging Report Acronym: ERA](#era-unmatched-aging-report-acronym-era)
    - [When to Run this Report](#when-to-run-this-report-2)
    - [How to Run this Report](#how-to-run-this-report-2)
  - [Pending EFT Override Report Acronym: PEO](#pending-eft-override-report-acronym-peo)
    - [When to Run this Report](#when-to-run-this-report-3)
    - [How to Run this Report](#how-to-run-this-report-3)
  - [EFT / ERA Trending Report Acronym: ETR](#eft-era-trending-report-acronym-etr)
    - [When to Run this Report](#when-to-run-this-report-4)
    - [How to Run this Report](#how-to-run-this-report-4)
  - [Unapplied EFT Deposits Report Acronym: UN](#unapplied-eft-deposits-report-acronym-un)
    - [When to Run this Report](#when-to-run-this-report-5)
    - [How to Run this Report](#how-to-run-this-report-5)
  - [Active Bills with EEOB Report Acronym: AB](#active-bills-with-eeob-report-acronym-ab)
    - [When to Run this Report](#when-to-run-this-report-6)
    - [How to Run this Report](#how-to-run-this-report-6)
  - [Auto Decrease Adjustment Report Acronym: AD](#auto-decrease-adjustment-report-acronym-ad)
    - [When to Run this Report](#when-to-run-this-report-7)
  - [Auto-Post Report Acronym: AP](#auto-post-report-acronym-ap)
    - [When to Run this Report](#when-to-run-this-report-8)
    - [How to Run this Report](#how-to-run-this-report-7)
  - [Auto-Posted Receipt Report Acronym: APR](#auto-posted-receipt-report-acronym-apr)
    - [When to Run this Report](#when-to-run-this-report-9)
    - [How to Run this Report](#how-to-run-this-report-8)
  - [Auto Parameter History Report Acronym: APH](#auto-parameter-history-report-acronym-aph)
    - [When to Run this Report](#when-to-run-this-report-10)
    - [How to Run this Report](#how-to-run-this-report-9)
  - [CARC Data Report Acronym: CR](#carc-data-report-acronym-cr)
    - [When to Run this Report](#when-to-run-this-report-11)
    - [How to Run this Report](#how-to-run-this-report-10)
  - [Duplicate EFT Audit Report Acronym: DUPR](#duplicate-eft-audit-report-acronym-dupr)
    - [When to Run this Report](#when-to-run-this-report-12)
    - [How to Run this Report](#how-to-run-this-report-11)
  - [ERA Auto-Post Status Audit Report Acronym: EAPA](#era-auto-post-status-audit-report-acronym-eapa)
    - [When to Run this Report](#when-to-run-this-report-13)
    - [How to Run this Report](#how-to-run-this-report-12)
  - [EFT Transaction Audit Report Acronym: ETA](#eft-transaction-audit-report-acronym-eta)
    - [When to Run this Report](#when-to-run-this-report-14)
    - [How to Run this Report](#how-to-run-this-report-13)
  - [First Party COPAY Auto-Decrease Report Acronym: FAD](#first-party-copay-auto-decrease-report-acronym-fad)
    - [When to Run this Report](#when-to-run-this-report-15)
    - [How to Run this Report](#how-to-run-this-report-14)
  - [First Party COPAY Manual vs Auto-Decrease Report Acronym: FAM](#first-party-copay-manual-vs-auto-decrease-report-acronym-fam)
    - [When to Run this Report](#when-to-run-this-report-16)
    - [How to Run this Report](#how-to-run-this-report-15)
  - [EEOB Move / Copy / Remove Audit Report Acronym: MCR](#eeob-move-copy-remove-audit-report-acronym-mcr)
    - [When to Run this Report](#when-to-run-this-report-17)
    - [How to Run this Report](#how-to-run-this-report-16)
  - [EEOBs Marked for Auto-Post Audit Report Acronym: EMA](#eeobs-marked-for-auto-post-audit-report-acronym-ema)
    - [When to Run this Report](#when-to-run-this-report-18)
    - [How to Run this Report](#how-to-run-this-report-17)
  - [Provider Level Adjustments (PLB) Report Acronym: PLB](#provider-level-adjustments-plb-report-acronym-plb)
    - [When to Run this Report](#when-to-run-this-report-19)
    - [How to Run this Report](#how-to-run-this-report-18)
  - [ERAs Posted with Paper EOB Audit Report Acronym: POSR](#eras-posted-with-paper-eob-audit-report-acronym-posr)
    - [When to Run this Report](#when-to-run-this-report-20)
    - [How to Run this Report](#how-to-run-this-report-19)
  - [Payer Implementation Report Acronym: PX](#payer-implementation-report-acronym-px)
    - [When to Run this Report](#when-to-run-this-report-21)
    - [How to Run this Report](#how-to-run-this-report-20)
  - [CARC / RARC Quick Search Acronym: QS](#carc-rarc-quick-search-acronym-qs)
    - [When to Run this Report](#when-to-run-this-report-22)
  - [Remove ERA from Active Worklist Audit Report Acronym: REMR](#remove-era-from-active-worklist-audit-report-acronym-remr)
    - [When to Run this Report](#when-to-run-this-report-23)
    - [How to Run this Report](#how-to-run-this-report-21)
  - [Link Payment Tracking Report Acronym: SR](#link-payment-tracking-report-acronym-sr)
    - [When to Run this Report](#when-to-run-this-report-24)
  - [CARC / RARC Table Data Report Acronym: TB](#carc-rarc-table-data-report-acronym-tb)
    - [When to Run this Report](#when-to-run-this-report-25)
    - [How to Run this Report](#how-to-run-this-report-22)
  - [View / Print ERA Acronym: VP](#view-print-era-acronym-vp)
    - [When to Run this Report](#when-to-run-this-report-26)
    - [How to Run this Report](#how-to-run-this-report-23)
  - [EFT Deposit Reconciliation Report Acronym: DEP](#eft-deposit-reconciliation-report-acronym-dep)
  - [EFT Unlock Lockout Override Report Acronym: EUO](#eft-unlock-lockout-override-report-acronym-euo)
    - [When to Run this Report](#when-to-run-this-report-27)
    - [How to Run this Report](#how-to-run-this-report-24)
  - [ERA Status Change Audit Report Acronym: ESC](#era-status-change-audit-report-acronym-esc)
    - [When to Run this Report](#when-to-run-this-report-28)
    - [How to Run this Report](#how-to-run-this-report-25)
  - [Manual Audit Report for Bills: MAR](#manual-audit-report-for-bills-mar)
    - [When to Run this Report](#when-to-run-this-report-29)
    - [How to Run this Report](#how-to-run-this-report-26)
- [National Reports for ePayments Data](#national-reports-for-epayments-data)
  - [EDI VOLUME STATISTICS Report](#edi-volume-statistics-report)
  - [ERA / EFT TRENDING Report](#era-eft-trending-report)
  - [EDI Diagnostic Measures Extracts Menu](#edi-diagnostic-measures-extracts-menu)
    - [Report Results Imported into Excel](#report-results-imported-into-excel)
    - [Downloading Reports to Excel](#downloading-reports-to-excel)
    - [Report Results Displayed in List Manager](#report-results-displayed-in-list-manager)
    - [Display Report in List Manager Format](#display-report-in-list-manager-format)
- [Enhancements to Non-EDI Lockbox Menus](#enhancements-to-non-edi-lockbox-menus)
  - [Agent Cashier Menu](#agent-cashier-menu)
    - [Extended Check / Trace / Credit Card Search Acronym: EX](#extended-check-trace-credit-card-search-acronym-ex)
    - [Link Payment Acronym: LP](#link-payment-acronym-lp)
    - [Link Payment to Multiple Claims](#link-payment-to-multiple-claims)
    - [Deposit Processing Acronym: DP](#deposit-processing-acronym-dp)
    - [Receipt# Lookup for Pharmacy Claims](#receipt-lookup-for-pharmacy-claims)
    - [Edit a Receipt](#edit-a-receipt)
    - [Auto-Posted Receipt Report Acronym: APR](#auto-posted-receipt-report-acronym-apr-1)
- [Security Keys](#security-keys)
  - [New or Modified Security Keys](#new-or-modified-security-keys)
    - [RCDPE REMOVE DUPLICATES](#rcdpe-remove-duplicates)
    - [RCDPE MARK ERA](#rcdpe-mark-era)
    - [PRCADJ](#prcadj)
    - [RCDPE AGED PMT](#rcdpe-aged-pmt)
    - [RCDPE ERA EXCEPT](#rcdpe-era-except)
    - [RCDPE AUTO DEC](#rcdpe-auto-dec)
    - [RCDPE REMOVE EEOB](#rcdpe-remove-eeob)
    - [RCDPEAR](#rcdpear)
    - [RCDPEPP](#rcdpepp)
    - [PRCFA SUPERVISOR](#prcfa-supervisor)
    - [RCDPE PAYER IDENTIFY](#rcdpe-payer-identify)
- [Appendix A – Helpful Links](#appendix-a-helpful-links)
- [Appendix B – Claim Level Adjustment Codes](#appendix-b-claim-level-adjustment-codes)
  - [Claim Adjustment Group Code](#claim-adjustment-group-code)
- [Appendix C – Provider Level Adjustment Codes](#appendix-c-provider-level-adjustment-codes)
  - [Provider Level Adjustment Reason Code](#provider-level-adjustment-reason-code)
- [Appendix D – Terms and Definitions](#appendix-d-terms-and-definitions)
- [Appendix E – 3rd Party EDI Lockbox Bulletins](#appendix-e-3rd-party-edi-lockbox-bulletins)
- [Solving ePayment Problems](#solving-epayment-problems)
  - [How to Remove Aged EFTs from the EFT Unmatched Aging Report](#how-to-remove-aged-efts-from-the-eft-unmatched-aging-report)

## Business Uses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Insurance Portability and Accountability Act of 1996 (HIPAA) or Public Law 101-191 requires healthcare plans and providers who conduct transactions electronically to comply with rules of standardization. HIPAA has several purposes but defines standards through rules and compliance of transactions and code sets. National standards allow for compatible formats between providers and third-party payers. Pittsburgh National Corporation and Provident National Corporation (PNC) Bank in Pennsylvania functions as the Department of Veterans Affairs (VA) 3rd Party Lockbox bank and will accept those standard transactions from payers on behalf of VA. The bank makes a daily deposit of third-party payments to US Treasury. They will also transmit deposit information in the form of an Electronic Funds Transfer (EFT) and data about the payment in the form of an Electronic Remittance Advice (ERA) to the Austin Financial Services Center (FSC). The Austin FSC will accept those transactions from the bank and translate those files into a Veterans Health Information System and Technology Architecture (VistA) readable format. The FSC will then forward those files to the appropriate VistA Accounts Receivable (AR) package by way of Mailman messages. In addition, the FSC will also transmit the ERA and EFT data files to Explanation of Benefits (EOB) Payment Healthcare Remittance Advice (EPHRA).

VistA, therefore, was enhanced to allow receipt processing and posting of electronic remittance data sent by payers. Additionally, VistA and Financial Management System (FMS) were enhanced to accommodate receipt and processing of third-party electronic payment data.

The ePayments software will supplement the current accounts receivable process by eliminating some data entry and automating the process of entering payments on a field service receipt. The software will now create an electronic receipt that replaces the paper field service receipt for payments received via the ePayments software.

## Timeframes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePayments software was released to sites on October 10, 2003, with an installation compliance deadline of October 16, 2003. The payer community is working to make transactions HIPAA compliant. Once payers are ready to transmit, they will work with our Lockbox Bank to enroll in the VA ePayments program. After enrolling, each payer will go through a rigorous transaction testing process with our Lockbox bank and any Clearinghouse that may be integrated. Testing ensures that the payer’s 835 EFT and ERA transmissions:

1.  Conform to acceptable HIPAA and X12 transaction standards.
2.  Can be received and forwarded by internal VA processing and messaging systems.

The entire payer community was not expected to be ready to transmit immediately following the HIPAA deadline of October 16, 2003. Payer implementation is expected to be staggered but initially covered the payers with the highest Veterans Health Administration (VHA) claim submission volume across each Veterans Integrated Service Network (VISN). Sites should expect to continue with paper processing as the electronic payers are brought online.

Since releasing the ePayments system, VHA has been honored by National Automated Clearinghouse Association (NACHA), the Electronic Payments Association, for its success in implementing a nationwide electronic health care remittance and payment processing system that complies with the electronic transaction standards of the HIPAA. PNC Bank in Pittsburgh, Pennsylvania serves as VHA’s Lockbox Bank and has partnered with VHA to enroll payers in this new, electronic business process. VHA’s experience with payers has been positive regarding the payer’s capability to produce and transmit ERAs. However, less than one percent of VHA’s active payers are producing and transmitting an EFT. While VHA’s primary goal is to enroll its payer community for ERA, VHA believes that additional benefits of HIPAA will be realized through both ERA and EFT processing. Because HIPAA regulations specify that payers comply with a request for ERA in response to a provider’s claim, payers’ business organizations may not be focused on the development of EFT.

## Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### AR Patch PRCA\*4.5\*284

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Rename existing option – Mark ERA Return to Payer.

Per request from the Chief Business Office (CBO), the existing Mark ERA Returned to Payer option, which is located on the Electronic Data Interchange (EDI) Lockbox parent menu, has been renamed to <u>Remove ERA from Active Worklist</u>. To accurately reflect the renamed option, the help text associated with the option has been updated to reflect the removal of an ERA off the ERA Worklist. The basic functionality of the option remains intact as it will continue to provide the capability to remove an unmatched ERA off the ERA Worklist.

2.  Rename existing option – Mark ERA Return to Payer Audit report.

The existing Mark ERAs Returned to Payer Audit Report, which is located on the EDI Lockbox Reports Menu, has been renamed to <u>Remove ERA from Active Worklist Audit Report</u>.

3.  Change default answer in prompt - Update ERA Posted Using Paper EOB.
4.  When an automatic update is performed on an ERA, the default response has been changed from "YES" to "NO." This modification helps prevent accidental updates. An example of the prompt is below:

“Link to update Remittance entry \# XXXXX with receipt ERA14332? NO//“

### AR Patch PRCA\*4.5\*303

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Implement new 835 Claim Adjustment Reason Code (CARC) Data Report option to the EDI Lockbox (ePayments) Reports Menu to display payers and the CARC codes returned on the 835 transactions.
2.  Implement new Third Party Joint Inquiry (TPJI) Screen Display redesign for ePayments. The new action option 'EP ERA/835" shall display only data associated with the 835 transaction.
3.  Implement new TPJI Action Option redesign for ePayments.
4.  Implement CARC / Remittance Advice Remark Code (RARC) Data Transfer from FSC.
5.  Implement Report Enhancements. The EDI Lockbox (ePayments) Reports Menu includes a new report entitled "Provider Level Adjustments (PLB) Report to display ERA data with PLB data details.
6.  Modification to the Scratchpad to process Efficiency Enhancements.
7.  Change EDI Lockbox to EDI Lockbox (ePayments).

### AR Patch PRCA\*4.5\*304

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Implement Auto-Auditing for Paper Bills.
8.  Enhance Insurance Payment Trend Report.
9.  Implement ability to Track Dollars through Suspense.
10. Implement National Reports for ePayments Data.
11. Implement Standardized Deposit Tickets.
12. Implement Receipt# Enhancements.
13. Implement Site Parameters for Pharmacy / Medical.
14. Implement Auto-Posting for Pharmacy / Medical.
15. Implement Auto-Decrease for Medical Claims.
16. Fix errors and enhancements to Auto-Post Awaiting Resolution (APAR).
17. Implement Auto-Post Checks for Pharmacy Claims.
18. Enhance Exception Error message and filtering.

### AR Patch PRCA\*4.5\*316

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updates the VistA upload process of CARC / RARC data sent by FSC.

### AR Patch PRCA\*4.5\*317

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Adds the Unapplied EFT Deposits Report back on the EDI Lockbox (ePayments) Reports Menu.
19. Updates the ERA Worklist option and the Auto-Post Awaiting Resolution option to ask users if they want to use a preferred view, when appropriate.

### AR Patch PRCA\*4.5\*318

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Updates the logic associated with auto-posting.
20. Adds new report Auto-Posted Receipt Report on the EDI Lockbox (ePayments) Reports Menu.
21. Updates the Auto-Decrease Adjustment report to include CARC details.
22. Locks several actions within the ERA Worklist (including Scratchpad) and the Auto-Post Awaiting Resolution worklist (including Scratchpad) with one of two new security keys.
23. Updates EFT Daily Activity Report to include CR and TR numbers and allows for up to 60 characters for the payer’s name.
24. Removes security key lock from the EDI Diagnostic Measures Reports menu.
25. With a security key, locks several options within the EDI Diagnostic Measures Extracts Menu.
26. Updates the EFT Unmatched Aging Report and the Unapplied EFT Deposits report.
27. Updates the logic associated with putting money to suspense.
28. Updates the auto-post site parameters logic.

### AR Patch PRCA\*4.5\*321

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The ‘Move ERA to Suspense’ option has been disabled and is no longer accessible from the EDI Lockbox menu.
29. The ‘Refresh Scratch Pad’ action has been removed from the APAR Scratchpad.
30. Receipt comments are now required when part of an account balance is split to suspense. A standardized set of comments have been added for the user to choose from along with a free form text comment field.
31. If a receipt line comment has been added, the scratchpad screens in APAR and ERA Worklists will display the username and a timestamp.
32. The automatic update of Electronic Explanation Of Benefits (EEOB) information to reflect the split / edit of claims will occur at receipt creation in the PRCA nightly auto-post job (for APAR) or at receipt creation in the ERA Worklist.
33. Updates to the Daily Activity Report including: a prompt to filter for EFTs with debits, a debit flag added to EFTs, removed matched payment amounts posted from totals, displays the station number instead of division and various page breaks for ease of use.
34. Updates to Receipt Processing including new help text when creating new receipts, ability to change the type of payment on receipts with preexisting lines, and the ability to change the EFT number in certain cases.
35. Eliminated an error when running the EFT Transaction Audit Report.
36. Update to the Link Payment Account action that now allows the user to move EEOBs to claims with payments linked from suspense.
37. Updates to payer name selection and display: payer names longer than 30 characters can be selected, names containing ":", "," or "-" can be selected, names with 60 characters display correctly.
38. Updated the Auto-Posted Receipt Report to ensure the correct dates displayed in the report fall within the range selected at the prompt.
39. Enabled VistA to use the start date and Electronic Claims Management Engine (ECME) \# to identify the correct claim \# and populate the ERA.
40. Exceptions for pharmacy claims now display correctly and in sequence.
41. Updated the APAR worklist to allow greater flexibility to sort and display data.
42. Updated receipt headers to show EFT / ERA numbers and totals.
43. Claims in Claim Status Awaiting Resolution (CSA) status cannot be manually or auto-audited.
44. The List of Receipts report now displays in list manager format.
45. Manually matched ERAs with CHK payment types can be marked for auto-post.
46. Medical, Pharmacy and Tricare Payers can now be indicated, along with access to view, in a list, and preferred types edited when appropriate.
47. EFT / ERA Trending Report added to EDI Lockbox reports menu.
48. The Decrease Adjustment function now alerts users if there are pending payments and displays the payment that is pending.
49. Updated the ERA worklist to allow greater flexibility to sort and display data.
50. The RCDPE AUDIT mail group now allows end users to self-enroll and a specific day of the week can be set for when the bulletins are sent.
51. Number of days of unposted medical and pharmacy EFTs to prevent posting have been changed to 60 and 365 respectively.

### AR Patch PRCA\*4.5\*326

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Adds notifications for changes to auto-post, auto-decrease, payer, and CARC site parameters.
52. Adds the ability to see who manually marked an ERA for auto-post in the Auto-Posted Receipt Report, Receipt Profile, List of Receipts Report, and Transaction Profile.
53. Adds 'matched date’ to the ERA Worklist and Daily Activity Report.
54. Adds a unique EFT identifier to the following reports: Daily Activity Report, EFT Unmatched Report, Unapplied EFT Report, EFT Audit Report, and Manual Match Report.
55. Adds display of ‘Percent Collected on Claims’ to the ‘Claim Level Pay Status’ section of the EP Report (ERA / 835 Action).
56. Updates display language in the Link Payment Report.
57. Adds ability to filter by receipt number on Link Payment Report.
58. Allows user to generate Auto-Post Report by payer Tax ID Number (TIN).
59. Restricts unbalanced ERAs to be auto-post candidates.
60. Renames the Payer Exclusion Report to the Payer Implementation Report.
61. Modified the 'Distribute Adj Amts' action on the ERA Worklist to allow for negative distributions to claim lines that do not have a valid claim.
62. Adds FMS Document Status to bill / claim profile screens and reports.
63. Provides fix to Pharmacy Data Exception Filter on the 3rd Party Exceptions Worklist Scratch Pad.
64. Provides fix to error in the ERA Worklist Manual Match Action.
65. Adds an ERA Partial Post Indicator.
66. Rewrites auto-posting logic to determine if the ERA is matched to an EFT.
67. Changes prompt wording of Worklist Delete.
68. Removes auto-decrease limit and adds new maximum parameter.
69. Adds the ability to auto-decrease zero or no-pays.
70. Adds the ability to view all ERA verify lines information on EEOBs.
71. Adds the capability to filter all 3rd Party EDI Lockbox reports and options by Tricare / Civilian Health and Medical Program of the Department of Veterans Affairs (ChampVA).
72. Adds Administrative Cost Adjustment option to allow adjustment to balance and for it to be recognized.
73. Adds fee claims to Auto-Audit (5287.13) Rate type = Fee.
74. Allows Accounts Management (AM )Clerk access to the Admin Cost Adjustment option.
75. Fixes duplicate EFT deposits in the Audit Report.

### AR Patch PRCA\*4.5\*332

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Adds report that shows all EFTs creating the EFT lock up.
76. Adds report for who marked EEOBs for auto-post.
77. Adds a List Manager report (worklist) showing all ERAs that were marked as duplicates.
78. Adds a historical report for all auto-activity and parameter changes.
79. Modifies the Active Bills with EEOB Report.
80. Expands the user initials on the List of Receipts Report.
81. Modifies the data displayed on the ERA / EFT Trending Report.
82. Modifies ERA Worklist Manual Match Action.
83. Adds Number of days (age) of unposted Tricare EFTs to prevent posting.
84. Adds ability to look up check, credit card, or trace numbers without identifying type of number.
85. Corrects 835 message errors for claims not electronically billed.
86. Adds the ability to auto-audit Tricare claims.
87. Corrects attachment of correct EEOBs to payments that have been posted to suspense.
88. Adds trace \# to the Receipt Profile.
89. Creates sub-menus for the EDI Lockbox Reports.
90. Allows users to view and print ERAs in List Manager.
91. Removes security key RCDPEAR from the Administrative Cost Adjustment option.

### AR Patch PRCA\*4.5\*345

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Removes Transfer Language reference from the EDI Lockbox 3rd Party Exceptions (EXC) data transmissions worklist.
92. Adds deposit number to the detail lines in the Auto-Post Report.
93. Adds new site parameter questions to allow pharmacy claims with payments to be auto-decreased by the Nightly AR Process, and modifies reports Auto-Parameter History Report, EDI Lockbox Parameters Report, EDI Lockbox Exclusion Report Audit Report, and EDI Lockbox Parameters Audit Report.
94. Adds ability to auto-decrease first party claims when payments have been posted to the corresponding third-party claim by adding a new site parameter to the AR SITE PARAMETER File and creating new reports 1st Party Auto-Decrease Adjustment Report and First Party COPAY Manual vs Auto-Decrease Report.
95. Fixes an issue with TRICARE EFT lockouts that were preventing medical EFT Lockouts from being processed if TRICARE ERAs aged beyond the NUMBER OF DAYS (AGE) OF UNPOSTED TRICARE EFTS TO PREVENT POSTING site parameter setting.
96. Keeps and displays the patient’s name received on the EEOB and displayed under ‘Free Text’. If a split/edit is processed on the claim payment, both the original patient’s name and the split / edit patient name will display in following screens: TPJI EP option, View / Print ERA, and View / Print EEOB.

### AR Patch PRCA\*4.5\*375

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Receipt transactions for a debit (negative) type EFT will be marked with a new debit flag. These transactions will be subtracted from the calculated receipt total, which may result in a negative receipt total.
97. When an EFT is removed from the system using the menu option. Remove Duplicate EFT Deposits, \[RCDPE REMOVE DUP DEPOSITS\], the new field REMOVAL TYPE \[.2\] will be entered, after the removal reason text. The user must enter one of two codes from the set:
- D – DUPLICATE EFT
- M – MILLENIUM EFT

The new field will show on the Duplicate EFT Deposits Audit report \[RCDPE EFT AUDIT REPORT\].

### AR Patch PRCA\*4.5\*349

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ability to auto-decrease TRICARE claims with and without payments. New site parameter questions were added to allow TRICARE claims with and without payments to be auto-decreased by the Nightly AR Process. This resulted in changes to the following areas:
1.  New site parameter questions were added to the EDI Lockbox Parameters \[RCDPE EDI LOCKBOX PARAMETERS\] option.
2.  The Auto-Parameter History Report \[RCDPE AUTO PARAM HIST REPORT\] was modified to include changes to TRICARE auto-decrease parameters.
3.  The EDI Lockbox Parameters Report \[RCDPE SITE PARAMETER REPORT\] was modified to include TRICARE auto-decrease parameters.
4.  The EDI Lockbox Exclusion Report Audit Report \[\[RCDPE EXCLUSION AUDIT REPORT\] was modified to include changes to payer exclusions for TRICARE claims with and without payments.
5.  The EDI Lockbox Parameters Audit Report \[RCDPE PARAMETER AUDIT REPORT\] was modified to include changes to site parameters for TRICARE claims with and without payments.
6.  The Nightly AR Process was modified to auto-decrease TRICARE claims with and without payments that meet site parameter criteria.
98. The amount column on the List of Receipts \[RCDP LIST OF RECEIPTS REPORT\] report was modified to accurate reflect the amount of the receipts when more than one receipt is created for an ERA.
99. The Review Line \[RCDPE APAR EEOB REVIEW\] protocol action was removed from the Research menu of actions in the Auto-Post Awaiting Resolution \[RCDPE APAR\] (APAR) worklist.
100. The worklist header for the ERA Worklist \[RCDPE EDI LOCKBOX WORKLIST\] (WL) was modified to ensure that the entire payer name / TIN is accurately displayed.
101. The EFT/ERA TRENDING Report \[RCDPE EFT-ERA TRENDING REPORT\] (ETR) was modified to display a separate section for auto-posted ERAs.
102. A new filter was added to the EFT/ERA TRENDING Report \[RCDPE EFT-ERA TRENDING REPORT\] (ETR) to allow for the display of only closed claims.
103. A new report, EFT Unlock Lockout Override \[RCDPE EFT UNLOCK OVERRIDE REP\] was added to the Audit Reports \[RCDPE EDI LOCKBOX AUDIT RPRTS\] (AUDR) sub-menu of EDI LOCKBOX REPORTS Menu \[RCDPE EDI LOCKBOX REPORTS MENU\].
104. Allows the user to display a list of EFT Lockout overrides including the override comment, override type, user who performed the override, and the date the override was performed for a specified date range.
105. The Site Parameter Edit \[PRCA SITE PARAMETER\] and the EDI Lockbox Parameters Report \[RCDPE SITE PARAMETER REPORT\] options were modified to allow selection by a specified list of categories, if desired.
106. The Site Parameter Edit \[PRCA SITE PARAMETER\] option was modified to filter the payer exclusion lists for Auto-Posting and Auto-Decreasing Medical, Pharmacy and TRICARE claims by the type of payer (Medical, Pharmacy or TRICARE).
107. The Search List action in the ERA Worklist \[RCDPE EDI LOCKBOX WORKLIST\] (WL) was modified such that if a user performed a search on an empty worklist, no error occurred.
108. Look at Receipt \[RCDPE EOB WL RECEIPT VIEW\] in the ERA Worklist scratchpad was modified to only display the create receipt \[RCDPE EOB WORKLIST RECEIPT\] action for users who have the RCDPEPP security key.
109. Display of auto-decrease CARCs are now sorted in numerical order by CARC code in the EDI Lockbox Parameters \[RCDPE EDI LOCKBOX PARAMETERS\] option and the EDI Lockbox Parameters Report \[RCDPE SITE PARAMETER REPORT\] option.
110. A previous enhancement prevented claims with reject error messages from being audited. This has been amended so that claims with rejects will be allowed to be audited if review has been completed in the Claims Status Awaiting Resolution \[IBCE CLAIMS STATUS AWAITING\] option.
111. A new filter by rate type has been added to the Audit an Electronic Bill \[PRCAA AUDIT\] option. When looping through bills one or more rate types may be selected to limit the bills presented for audit.
112. The TPJI "ERA/835" screen was modified to fix a problem with users being kicked out of the system when an EOB contained a RARC code that was not on file.
113. A bug fix was made to allow pharmacy claims that have an ECME numbers with less than 12 characters to be correctly identified when receiving a pharmacy 835 Electronic Remittance Advice (ERA) file.
114. Email messages will now be sent to a standard outlook email group when 835 transmission errors occur.

### AR Patch PRCA\*4.5\*380

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Added the ability to receive Electronic Fund Transfers (EFTs) from FSC for the same Deposit Number and Deposit Date more than once a day. Prior to the enhancement, if ePayments received EFTs from FSC for a deposit number and deposit date already on file, the EFTs initially received were overwritten by those just received.
115. Added the ability to receive EFTS from FSC for the same Deposit Number and Deposit Date on subsequent days. Prior to the enhancement, if ePayments received EFTs from FSC for a Deposit Number and Deposit Date that had already created a Cash Receipt (CR) deposit, it was logged as an error.
116. Enhanced the EFT Audit Report to show a summary of all the EFTs received from FSC for a specified Deposit Number and Deposit Date.

### AR Patch PRCA\*4.5\*367

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  A new receipt type ('TDA Receipt') for processing ChampVA payments was added.
1.  Receipts of this type will not have a deposit number and will not be sent to FMS because ChampVA monies are deposited into FMS via TDA.
117. Fixed an existing performance issue that was causing a long delay when an Electronic Remittance Advice (ERA) was selected from the ERA Worklist to be worked. Prior to working an ERA, the system first checks to see if any aged ERAs or Electronic Fund Transfers (EFTs) need to be worked on first. Prior to the fix the system was checking all ERAs and EFTs since patch PRCA\*4.5\*298 was installed at the site (2015). Now the system will only check for aged ERAs or EFTs for the last three years.

### AR Patch PRCA\*4.5\*371

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  An option has been added to the Unapplied EFT Deposits Report \[RCDPE UNAPPLIED EFT DEP REPORT\] to allow a user to choose "Grand Totals" only. This will print the total amount of unapplied deposits in their VistA system (known as the 8NZZ account).
118. To allow quick access to recently changed electronic remittance advice (ERA) and electronic funds transfer (EFT) data, several date/time fields, indexes, and cross references were added to Vista to facilitate reporting in future releases.

     New date/time fields were added to the top-level ELECTRONIC REMITTANCE ADVICE file (#344.4, 9) and EDI THIRD PARTY EFT DETAIL file (#344.31, 9). Whole file cross references ('MCCF') were created for each file. To allow Vista access to only changed detail lines within an ERA, a date/time field was added to the ERA DETAIL sub-file (#344.41, 9.02), along with an associated sub-file cross reference ('MCCF'). Updates to the \#344.41 sub-file will in-turn update the whole file 'MCCF' cross references. A date/time field was also added to the AR BATCH PAYMENT file (#344, 9) to track receipt data changes.

     Additionally, MUMPS record type cross references were created to update the MCCF date/time fields in the \#344.4, \#344.41, \#344.31, and \#344 files if any of the report data fields within these files change.
119. Widened the Selection Number column of the Identify Payers \[RCDPE PAYER IDENTIFY\] menu option of the EDI Lockbox (ePayments) \[RCDPE EDI LOCBOX MENU\] so it can accurately show selection numbers for payers when the total number of payers is in the thousands.
120. The EFT Transaction Audit Report \[RCDPE EFT TRANSACTION AUD REP\] (ETA) on the Audit Reports \[RCDPE EDI LOCKBOX AUDIT RPRTS\] sub-menu of the EDI Lockbox (ePayments) Reports menu \[RCDPE EDI LOCKBOX REPORTS MENU\] was modified. This report can be run in either summary or detail mode. When run in detail mode, the user can choose an EFT to display by either Deposit Number, Deposit Date, Receipt Number, or Trace Number. Prior to this enhancement the report was exited after the EFT was displayed. Now the user will be returned to the Deposit Number, Deposit Date, Receipt Number, or Trace Number prompt so that they can select another EFT.
121. The ERA Unmatched Aging Report \[RCDPE ERA AGING REPORT\] (ERA) was modified to remove all Electronic Explanation of Benefits (EEOB) detail lines from being displayed so that unmatched Electronic Remittance Advice (ERAs) can be researched more easily.
122. Modified the Remove ERA from Active Worklist Audit Report \[RCDPE REMOVED ERA AUDIT\] (REMR) to include a column for Trace number.
123. Modified Receipt Processing \[RCDP RECEIPT PROCESSING\] (RP) to prevent blank spaces in a receipt number when either creating a new receipt or using the Edit Receipt action when editing an existing receipt.
124. Fixed an issue that resulted in one Electronic Fund Transfer (EFT) being matched to multiple receipts. The issued occurred when the user enters the Receipt Processing \[RCDP RECEIPT PROCESSING\] (RP) menu option to edit an open receipt with a payment type of EDI LOCKBOX and performs the following steps:
1.  The user selects the Edit Receipt action and switches the EFT attached to the receipt.
7.  The user selects a different receipt to edit without exiting all the way back to the menu option prompt.
8.  When the second receipt, having no deposit number, is processed, the following occurs:
    - The EFT from the first receipt is associated with the second receipt.
    - The EFT that was associated with the second receipt is unmatched.
125. Fixed an issue that caused the system to erroneously prompt the user for a deposit number when a receipt with a payment type of EDI LOCKBOX was processed in Receipt Processing \[RCDP RECEIPT PROCESSING\] (RP) using the Process Receipt action.
126. Fixed an issue for CHAMPVA receipts that was preventing users from entering a receipt total that was greater than 99999.99 dollars.

### AR Patch PRCA\*4.5\*409

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The ability to automatically remove all data exceptions for an ERA when the ERA is removed from the worklist was added to the Remove ERA from Active Worklist \[RCDPE REMOVE ERA FROM WORKLIST\] (REM) option.
127. The display of data exceptions using the EDI Lockbox 3rd Party Exceptions \[RCDPE EXCEPTION PROCESSING\] (EXC) option was modified to allow for up to 17 character claim numbers.
128. To allow quick access to recently changed electronic remittance advice (ERA) and electronic funds transfer (EFT) data, several date/time fields, indexes, and cross references were added to VistA to facilitate reporting in future releases.
129. The View/Print ERA \[RCDPE VIEW/PRINT ERA\] (VP) option was modified to allow for ERAs with provider line balances (PLBs) but no claim data to be displayed properly.
130. Enhanced the Receipt Processing \[RCDP RECEIPT PROCESSING\] (RP) option to allow for ECME or Prescription number lookup when adding a new payment to a receipt. Previously, ECME or Prescription number lookup was only allowed for EDI LOCKBOX receipt types.
131. Enhanced the Receipt Processing \[RCDP RECEIPT PROCESSING\] (RP) option to allow for a new AR EVENT TYPE file (#341.1) OGC-CHK to checks sent by the Office of General Council (OGC).
132. Modified the ERA Unmatched Aging Report (ERA) to optional display adjustment/code information.
133. Fixed a bug in the EFT Transaction Audit Report \[RCDPE EFT TRANSACTION AUD REP\] (ETA) option that prevented the user from up-arrowing out of the deposit number selection when running the report in summary mode by deposit number.

### AR Patch PRCA\*4.5\*424

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Auto-Posting of ERAs has been enhanced to allow for the auto-posting of ERAs where the total amount paid is 0 (zero). This includes the following enhancements:
    1.  An additional site Parameter was added to the EDI Lockbox Parameters \[RCDPE EDI LOCKBOX PARAMETERS\] to allow for the enabling/disabling of Zero Pay ERAs.
    2.  The EDI Lockbox Parameters Report \[RCDPE SITE PARAMETER REPORT\] was modified to show the value of the newly added parameter.
    3.  The EDI Lockbox Parameters Audit Report \[RCDPE PARAMETER AUDIT REPORT\] was modified to include the audit trail for the newly added parameter.
    4.  The auto-posting process was modified to auto-post zero pay ERAs if the newly added site parameter is set to 'YES'.
    5.  When auto-posting of zero pay ERAs is enabled, a background job will be initiated. This background job auto-posts eligible historical zero payment ERAs.
5.  Enhancements were made to the EFT Transaction Audit Report \[RCDPE EFT TRANSACTION AUD REP\] as follows:
1.  The ability to search by FMS document number was added to the detail report.
2.  For Debit EFTs, the total on amount of the EFT will now show as negative.
6.  When looking at data exceptions in the EDI Lockbox 3rd Party Exceptions \[RCDPE EXCEPTION PROCESSING\] option, the date of service has been added to the display.
7.  A bug was fixed, whereby matching of the ECME Number to a pharmacy claim would fail if the transaction contained no service line data.
8.  The ERA Worklist \[RCDPE EDI LOCKBOX WORKLIST\] will now allow filtering of the list for auto-posted, zero payment ERAs.
9.  Reversed a change from a previous patch that prevented processing of check type receipts with no deposit ticket.

### AR Patch PRCA\*4.5\*436

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enhanced the Receipt Processing \[RCDP RECEIPT PROCESSING\] (RP) option to allow for a new AR EVENT TYPE file (#341.1) OGC-EFT to process EFTs generated for the Office of General Council (OGC).

### AR Patch PRCA\*4.5\*432

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Update the following with a CHAMPVA filter selection. If payer type selection was previously displayed in a heading, include CHAMPVA that heading.
- 835 CARC Data Report \[RCDPE CARC CODE PAYER REPORT\]
- Active Bills With EEOB Report \[RCDPE ACTIVE WITH EEOB REPORT\]
- Auto-Decrease Adjustment Report \[RCDPE AUTO-DECREASE REPORT\]
- Auto-Post Awaiting Resolution \[RCDPE APAR\]
- Auto-Post Report \[RCDPE AUTO-POST REPORT\]
- Auto-Posted Receipt Report \[RCDPE AUTO-POSTED REPORT \[RCDPE AUTO-POST RECEIPT REPORT\]
- Duplicate EFT Deposits Audit Report \[RCDPE EFT AUDIT REPORT\]
- EDI Lockbox 3rd Party Exceptions \[RCDPE EXCEPTION PROCESSING\]
- EEOB Move/Copy/Remove Audit Report \[RCDPE EEOB MOVE/COPY/RMOVE RPT\]
- EEOBs Marked for Auto-Post Audit Report \[RCDPE MARKED AUTO-POST REPORT\]
- EFT Daily Activity Report \[RCDPE EDI LOCKBOX ACT REPORT\]
- EFT Unmatched Aging Report \[RCDPE EFT AGING REPORT\]
- EFT/ERA TRENDING Report \[RCDPE EFT-ERA TRENDING REPORT\]
- ERA Status Change Audit Report \[RCDPE ERA STATUS CHNG AUD REP\]
- ERA Unmatched Aging Report \[RCDPE ERA AGING REPORT\]
- ERA Worklist \[RCDPE EDI LOCKBOX WORKLIST\]
- ERAs Posted with Paper EOB Audit Report \[RCDPE ERA W/PAPER EOB REPORT\]
- Identify Payers \[RCDPE PAYER IDENTIFY\]
- Payer Implementation Report \[RCDPE PAYER EXCLUSION NAME TIN\]
- Provider Level Adjustments (PLB) Report \[RCDPE PROVIDER LVL ADJ REPORT\]
- Remove ERA from Active Worklist Audit Report \[RCDPE REMOVED ERA AUDIT\]
- Unapplied EFT Deposits Report \[RCDPE UNAPPLIED EFT DEP REPORT\]
134. Modify Identify Payers \[RCDPE PAYER IDENTIFY\] to allow CHAMPVA identification.
1.  Allow the user to select CHAMPVA as a filter.
2.  Display a new column for the CHAMPVA flag.
3.  Action to Edit Flags will allow the user to the CHAMPVA flag.
4.  A new action called Flag CHAMPVA will CHAMPVA flag edits.
5.  Action Filter incudes CHAMPVA as a filter choice.
6.  Help text includes reference to CHAMPVA.
135. Add a negative sign on the following reports to indicate an EFT debit amount.
- Duplicate EFT Deposits Audit Report \[RCDPE EFT AUDIT REPORT\]
- EFT Unmatched Aging Report \[RCDPE EFT AGING REPORT\]
136. Remove the word “Debit” from EFT Daily Activity Report \[RCDPE EDI LOCKBOX ACT REPORT\] and display a negative sign in front of the EFT debit amount.
137. Increase the maximum character display in option Receipt Processing \[RCDP RECEIPT PROCESSING\]. Display a maximum of 11 characters, without commas, for the processed amount and payment amount. Previously the maximum was 8 and 7 respectively.
138. Auto-posting was modified to exclude CHAMPVA zero-payment ERAs.

### AR Patch PRCA\*4.5\*439

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Add Excel format to options:
- EFT Daily Activity Report \[RCDPE EDI LOCKBOX ACT REPORT\]
- Identify Payers \[RCDPE PAYER IDENTIFY\]
2.  List deposits for selection when running the detail format of EFT Transaction Audit Report \[RCDPE EFT TRANSACTION AUD REP\] by deposit number.
3.  Enhance alignment for EFTs displayed for selection on EFT Transaction Audit Report \[RCDPE EFT TRANSACTION AUD REP\].
4.  Identify Unbalanced Deposits via:
- EFT Transaction Audit Report \[RCDPE EFT TRANSACTION AUD REP\]
- EFT Daily Activity Report \[RCDPE EDI LOCKBOX ACT REPORT\]
- Outlook email sent by Nightly Process when a deposit is unbalanced.
5.  Stop sending Suspense Bulletins through MailMan.
6.  Add filter selection to the heading on Data Exceptions screen of option EDI Lockbox 3rd Party Exceptions \[RCDPE EXCEPTION PROCESSING\].
7.  Remove requirement of security key RCDPEPP on ERA Worklist \[RCDPE EDI LOCKBOX WORKLIST\] for the following:
- Verify Action
- Refresh Scratchpad Action
8.  Old version of ERA Status Change Audit Report is renamed to ERA Auto-Post Status Audit Report \[RCDPE ERA MATCH POST AUDIT RPT\].
9.  Show an Auto-Post Audit and Matching Audit on:
- View/Print ERA \[RCDPE VIEW/PRINT ERA\]
- ERA Status Change Audit Report \[RCDPE ERA MATCH POST AUDIT RPT\]

### AR Patch PRCA\*4.5\*446

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enhance EFT/ERA Trending Report \[RCDPE EFT-ERA TRENDING REPORT\].
1.  Add new filter for Payment EEOBs, Unmatched EEOBs, Zero Payment EEOBs, or All
9.  Add new filter to allow users to sort by payer or sort by amount of payment
2.  Include new report Manual Audit Report for Bills \[RCDPE MANUAL AUD REP\].
1.  Report on manually audited bills for third party electronic payment
3.  Add a final validation when processing a receipt to verify EFTs are available to post.
4.  Add a new option Remove Unbalanced Deposit Flag \[RCDPE UNBAL DEPSOSIT FLAG\] to the EDI Lockbox Menu, locked with security key RCDPE AUTO DEC.
5.  Remove Sum of EFT Amounts: line from the Summary of the EFT Transaction Audit Report.
6.  Add STMT FROM DATE and STMT TO DATE to VP View/Print ERA \[RCDPE VIEW/PRINT ERA\] option.

### AR Patch PRCA\*4.5\*450

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Add ability to auto-decrease first party claims when payments have been manually posted to the corresponding third-party claims.
2.  Expand auto-decrease to include inpatient charges and pharmacy charges when decreasing first party claims using the corresponding third-party.
3.  Add new site parameters to the AR SITE PARAMTER file to enable auto-decrease of manually posted first party copay claims.

## New Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table of terms contains vocabulary that are be referenced throughout this document to describe the ePayments process.

| Term         | Description                                                                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CARC         | Claim Adjustment Reason Code.                                                                                                                                       |
| EFT          | Electronic Funds Transfer: the electronic form of what is currently sent as a paper check.                                                                          |
| ERA          | Electronic Remittance Advice; the equivalent to a stack of paper Explanation of Benefits (EOB) statements for many patients from one payer.                         |
| EEOB         | Electronic Explanation of Benefits; one line item within an ERA.                                                                                                    |
| RARC         | Remittance Advice Remark Code                                                                                                                                       |
| Trace Number | A number assigned by the insurance company to identify which EFT payment is associated with what ERA; used to re-associate electronic remittance payment with data. |

<span id="_Toc183424286" class="anchor"></span>Table 2: ERA Work List

## Process Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following figure depicts a high-level description of the ePayments process. See the next section for one exception involving transactions that flow through website pay.gov, a program of the U.S. Department of the Treasury used to facilitate payment to U.S. Federal Government Agencies.

<span id="_Toc183424267" class="anchor"></span>Figure 1: ePayments High Level Process Flow

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/002.png)

The data flow process functions as follows:

- Electronic claims are sent to the payer, and the Clearinghouse sends a message to VistA Integrated Billing (IB), indicating that the claim passed all Clearinghouse validity edits and was forwarded to the payer. The message initiates the auto-audit functionality that automatically audits the claim and sets it up as a receivable in VistA.
- The payer adjudicates the claim and determines payment. The payment may be sent electronically to PNC Bank as an EFT or the payer may mail a paper check.
- PNC Bank sends:
- EFT dollars directly to the U.S. Treasury
- EFT 835 transactions, containing daily total deposit information by payer to the FSC
- ERA 835 transactions, containing electronic EOBs (EEOBs) to the FSC
- The FSC passes EFT and ERA information on to each Veterans Affairs Medical Center (VAMC) in flat file format via VistA Mailman messages. These messages are sent to the MLB mail group.
- Additionally, the FSC transmits the EFT and ERA flat file information to the EPHRA database.
- The FSC also transmits unrouteable EEOB data to EPHRA. Unrouteable EEOB data does not contain the appropriate Tax ID information to allow the FSC to route it to the proper VistA AR system. FSC 224-Unit staff monitors EPHRA for unrouteable EEOB data and use other data identifiers, such as the bill number, to determine appropriate routing and transmit to the correct VistA AR system.
1.  EFT data received by VistA initiates an automatic Credit Receipt (CR) document for each payment received within the deposit, and puts the payment information into a separate appropriation fund that tracks payments not yet posted as part of the A/R nightly processing job. The Revenue Source Code (RSC) 8NZZ was created specifically for third-party EFTs.

<span id="_Ref69289254" class="anchor"></span>Figure 2: ePayments Nightly Process

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/003.png)

2.  VistA runs a nightly process (see [⁠Figure 2: ePayments Nightly Process⁠](#_Ref69289254)) that matches ERAs to EFT files using the Trace Number and Insurance Company ID.
1.  If the system finds a match, it verifies the amount matches. If the amount matches, the ERA and EFT detail records are automatically marked as “matched.”
2.  If the amount does not match, the ERA record, and the EFT detail record are marked as “matched with errors.”
3.  If the system is not able to match an ERA with an EFT detail record, it is marked as “unmatched.” This scenario will call for a match to a paper check or is a zero-payment.
3.  When the ERA is received in VistA, it attempts to associate EEOBs with bills in the AR package and stores the details associated with the payer’s adjudication decisions in Integrated Billing’s EEOB file. This EEOB data is available for display under the BILL CHARGES action in THIRD PARTY JOINT INQUIRY.
1.  If any EEOBs cannot be associated with bills in VistA, a message will be sent to the RCDPE PAYMENTS EXCEPTIONS mail group. This message indicates that there is a problem with the bill number such as belongs to another site or the numbers were transposed.
4.  If NONE of the EEOBs included in the ERA can be associated with a bill in VistA, a message will be sent to the RCDPE PAYMENT EXCEPTIONS mail group indicating there were no valid bills on the ERA for the site. This ERA is then rejected and is not stored at the site. Contact the ePayments Point of Contact (POC) for assistance if needed.
4.  Members of the RCDPE Payments mail group receive the nightly processing bulletins.
5.  Members of the RCDPE Payment Exceptions mail group will receive all bulletins for exception conditions or processing issues generated by the EDI Lockbox (ePayments) message processor. An ePayments exception occurs when an EDI Lockbox (ePayments) message cannot be automatically or completely filed into the VistA AR and IB systems. When this occurs, an exception record is created in Exception Processing. To address the transmission issues, the user will access the Exception Processing function.
6.  A nightly auto-posting job evaluates the unposted ERAs to determine if an ERA is an auto-post candidate. If the ERA is not an auto-post candidate, the ERA must be worked by a user from the ERA Worklist Scratch Pad.
    - If the ERA is an auto-post candidate, the system will process the receipt if all criteria are met.
    - If the system is unable to create a receipt for an individual EEOB, the EEOBs must be worked by a user from the Auto-Posting Awaiting Resolution (APAR) list.
7.  The user reviews all unposted ERAs and creates the ERA Worklist Scratch Pad entries to make the necessary adjustments to balance the total of the EEOB with the total on the check or EFT. To use the worklist, ERAs with an unmatched status require matching to a paper check or marked as a zero pay.
8.  Once the adjustments are made in the Worklist, the Receipt can be created automatically through a Worklist function. The receipt and any total balancing adjustments can be created manually.
9.  The receipt can then be processed as normal through PR Process Receipt option.
10. For EFTs related to ERAs: After the receipt is processed and closed in VistA, the FMS transactions will be initiated. This means that a Transfer (TR) Document is generated to FMS to transfer the monies from the new Medical Care Collection Fund (MCCF) RSC 528704/8NZZ to the appropriate MCCF collection accounts under 5287. This TR document will also transfer any monies needing to be posted to the station suspense account or other accounts, due to non-MCCF billing / payments.
11. For ERAs related to paper checks: A CR document is generated to process the monies into FMS. This is the same processing as for current non-EDI receipts.
12. If the ERA receipt is not created using the Worklist, the ERA reference must be manually entered using the EDIT RECEIPT action in Receipt Profile. If the ERA is also associated with an EFT, the EFT reference must also be manually added using this action. This is extremely important because the receipt associated with an EFT will generate the appropriate TR documents to move the money out of 8NZZ and into the proper Fund / RSC, whereas a receipt without an EFT referenced will generate a CR document and will expect the dollars on the receipt to be deposited by the site.

## Process Flow, OGC Exception

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[⁠Figure 3⁠](#_Ref173925199) depicts a high-level description of the ePayments process for transactions originating with Office of General Counsel (OGC) settlements that flow through website pay.gov, a program of the U.S. Department of the Treasury.

<span id="_Ref173925199" class="anchor"></span>Figure 3: ePayments High Level Process Flow for OGC Payments

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/004.png)

The data flow process functions as follows:

- Office of General Counsel negotiates a monetary settlement that is due to the VA.
- The client’s law firm submits payment through website pay.gov, which is used to facilitate payment to U.S. Federal Government Agencies.
- Funds are processed via the Collections Information Repository (CIR).
- EFT dollars directly to the U.S. Treasury.
- EFT 835 transactions, containing daily total deposit information by payer to the FSC.
2.  ERA 835 transactions, containing electronic EOBs (EEOBs) are NOT transmitted.
- ERA 835 transactions, containing electronic EOBs (EEOBs) to the FSC.
- The FSC passes EFT information on to each Veterans Affairs Medical Center (VAMC) in flat file format via VistA Mailman messages. These messages are sent to the MLB mail group.
- Additionally, the FSC transmits the EFT flat file information to the EPHRA database.
1.  EFT data received by VistA initiates an automatic Credit Receipt (CR) document for each payment received within the deposit, and puts the payment information into a separate appropriation fund that tracks payments not yet posted as part of the A/R nightly processing job. The Revenue Source Code (RSC) 8NZZ was created specifically for third-party EFTs.
13. Members of the RCDPE Payments mail group receive the nightly processing bulletins.
14. Members of the RCDPE Payment Exceptions mail group will receive all bulletins for exception conditions or processing issues generated by the EDI Lockbox (ePayments) message processor. An ePayments exception occurs when an EDI Lockbox (ePayments) message cannot be automatically or completely filed into the VistA AR and IB systems. When this occurs, an exception record is created in Exception Processing. To address the transmission issues, the user will access the Exception Processing function.
15. The receipt can be processed using the EDIT RECEIPT action in Receipt Profile.
16. After the receipt is processed and closed in VistA, the FMS transactions will be initiated. This means that a Transfer (TR) Document is generated to FMS to transfer the monies from the new Medical Care Collection Fund (MCCF) RSC 528704/8NZZ to the appropriate MCCF collection accounts under 5287. This TR document will also transfer any monies needing to be posted to the station suspense account or other accounts, due to non-MCCF billing / payments.

# Getting Started with ePayments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menus and Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ERA List – Worklist Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new list manager screen, the ERA List – Worklist screen has been added to display the selection of ERAs to be worked.

There are features that give the capability to search a greater range of records, with dialogue issued at intermittent periods during the ERA Worklist record search to indicate that the system is still gathering records for the ERA Worklist. To exit the ERA Worklist option the user enters the cancel search character (“^”).

The user-defined sort selections are displayed in the header information on this screen. The following information is available in the body of the ERA List – Worklist screen:

1.  Sequence \#
139. ERA \#
140. Trace \#
141. Payer Name
142. Match Status & Date
143. ERA Paid Date
144. Total Amount Paid
145. Date Received

ERA List - Worklist Dec 09, 2011@15:20:15 Page: 1 of 136

DATE RANGE : NONE SELECTED MED/PHARM/TRIC/CHAMPVA: ALL

MATCH STATUS: NOT MATCHED AUTOP: ALL AUTO-POSTING: BOTH

POST STATUS : UNPOSTED PAYERS: ALL PAYERS PAYMENT TYPE: BOTH

\# ERA \# TRACE#

PAYER NAME/MATCH STATUS & DATE ERA PAID DT TOT AMT PAID DT REC'D

1 -XXXXXX XXXXXX \##

11/9/11 277.10 11/9/11

WOODMEN OF THE WORLD ASSURED L APPROX \# EEOBs: 3

UNMATCHED (CHECK PAYMENT EXPECTED)

2 - XXXXXX XXXXXX

11/10/11 155.95 11/10/11

MERITAIN HEALTH APPROX \# EEOBs: 1

UNMATCHED (CHECK PAYMENT EXPECTED)

3 - XXXXXX XXXXXX

11/10/11 270.62 11/10/11

XXXXXXXX XXXXXX APPROX \# EEOBs: 1

UNMATCHED (CHECK PAYMENT EXPECTED)

\+ \|'-' No scratchpad\|'x' EXC \|'A' autopost complete

Select ERA View/Print ERA Admin Cost Adj

Sort List Change View Exit

Mark for Auto Post ERA Manual Match

Select Action: Next Screen//

The List Manager ERA Worklist main page allows the user to perform the following actions:

1.  Select ERA
2.  Sort List
3.  Mark for Auto Post (requires the RCDPEPP security key)
4.  View / Print ERA
5.  Change View
6.  ERA Manual Match
7.  EXIT

### ERA Worklist / Scratchpad Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERA Worklist / Scratchpad is a new option that has been created for the ePayments system. It allows the user to select an ERA and view the detailed EEOB records associated with the ERA.

The following information is available from the ERA Worklist / Scratchpad:

For the entire ERA:

1.  ERA Entry \#
2.  Payer Name / ID
3.  Total Amt Paid
4.  Paper Check \# or EFT Trace \#
5.  Total amount to be posted to the receipt

ERA Worklist/Scratch Pad Jul 21, 2010@12:17:58 Page: 1 of 1

ERA Entry \#: XX Total Amount Paid: 123.45 Payment Order: ZERO-PAYMENTS FIRST Disp Auto-Posted ERAs: UNPOSTED EEOBS ONLY EFT \#/TRACE \#: XXX.X/ XXXXXXXXXXXXX BANKERS LINE AND CASUALTY COMPANY/ XXXXXXXXXXXXX

1 EEOB Seq \# On ERA: 1 Net Payment Amt: 123.45

1.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One A/XXXXX

Claim Bal: 0.00 Billed Amt: 0.00 Amt To Post: 123.45

Svc Dt: 6/1/00 COB: NO Rx Copay: UNKNOWN Means Tst: ??

Payment Amt: 123.45 Total Adjustments: 0.00 Net: 123.45

Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

Distribute Adj Amts Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen//

For the EEOB detail:

1.  Bill number
146. Patient Priority Status (CAT C)
147. Rx Copay exempt status
148. Date of service
149. Billed amount
150. Claim balance (current balance)
151. Patient last name
152. Last 4 digits of the patient’s Social Security Number (SSN)
153. Paid amount (amt to post)
154. COB status
155. Line item number from the ERA
156. ERA level and Claim level Adjustment totals
157. Comment Date and Time (stamp)
158. (Comment) User Name

ERA Worklist/Scratch Pad Jul 21, 2010@12:17:58 Page: 1 of 1

ERA Entry \#: XXXXXXXXXX Total Amt Pd: 123.45 Current View:

Payer Name/ID: IBinsurance Company One/XXXXXXXX NO SORT ORDER

PAPER CHECK \#: XXXX ALL EEOBs

... 1 EEOB Seq \# On ERA: 1 Net Payment Amt: 123.45

1.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One A/XXXX

Claim Bal: 0.00 Billed Amt: 0.00 Amt To Post: 123.45

Svc Dt: 6/1/00 COB: NO Rx Copay: UNKNOWN Means Tst: ??

Payment Amt: 123.45 Total Adjustments: 0.00 Net: 123.45.

Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

Distribute Adj Amts Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen//

The List Manager ERA Worklist Scratchpad allows the user to perform the following actions:

1.  Split / Edit A Line
159. Distribute Adj Amts
160. Refresh Scratch Pad
161. Research Menu
162. Look At Receipt
163. Review Line
164. Verify
165. Change View
166. Mark for Auto Post (requires the RCDPEPP security key)
167. View / Print an ERA
168. Receipt Processing (requires the RCDPEPP security key)
169. Exit

ERA Worklist/Scratch Pad Jul 21, 2010@12:17:58 Page: 1 of 1

ERA Entry \#: XXXXXXXXXX Total Amt Pd: 123.45 Current View:

Payer Name/ID: IBinsurance Company One/XXXXXXXX NO SORT ORDER

PAPER CHECK \#: XXXX ALL EEOBs

1 EEOB Seq \# On ERA: 1 Net Payment Amt: 123.45

1.001 Claim \#: KXXXXXX Patient/Last 4: Ibpatient,One A/XXXX

Claim Bal: 0.00 Billed Amt: 0.00 Amt To Post: 123.45

Svc Dt: 6/1/00 COB: NO Rx Copay: UNKNOWN Means Tst: ??

Payment Amt: 123.45 Total Adjustments: 0.00 Net: 123.45

..................Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

Distribute Adj Amts Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen//

The expanded Look At Receipt action (previously named PREVIEW RECEIPT) will yield the Preview / Create Receipt screens, and allows the following actions to be performed:

1.  Select option LOOK AT RECEIPT.
170. CREATE RECEIPT (allows a link to the RECEIPT PROCESSING function if the receipt is created without errors).

ERA WORKLIST PREVIEW RECEIPT Jul 21, 2010@08:43:02 Page: 1 of 1

ERA Entry \#: XXXXXXXXXX Total Amt Pd: 20.59

Payer Name/ID: IBinsurance Company One/XXXXXXXX

PAPER CHECK \#: XXXX

LINE \# ACCOUNT AMOUNT

PAYMENTS (LINES FOR RECEIPT):

1.001 XXX-KXXXXXX 20.59

Enter ?? for more actions

Print Receipt Preview Create Receipt Exit

Select Action: Quit//

The new Verify option provides functionality needed to identify and mark unverified EEOBs:

1.  MANUAL MARK AS VERIFIED
171. REPORT OF UNVERIFIED WITH DISCREPANCIES

VERIFY EEOBs:

1 MANUAL MARK AS VERIFIED

2 REPORT OF UNVERIFIED WITH DISCREPANCIES

3 QUIT AND RETURN TO WORKLIST

Select Action: QUIT//

The Research Menu is accessible through the list manager ERA Worklist screen and it allows the following actions to be performed:

1.  Full Acct Prof
172. Admin Cost Adj (requires the RCDPEAR security key)
173. TPJI (Third Party Joint Inquiry)
174. Bill Comment Log
175. Reestablish Bill (requires the RCDPEAR security key)
176. View / Print EEOB
177. Scratchpad Menu / Exit

ERA Worklist Research Aug 10, 2004@11:01:33 Page: 1 of 2

ERA Entry \#: 5 Total Amt Pd: 509.61 Current View:

Payer Name/ID: IBinsurance Company One/XXXXXXXXXX NO SORT ORDER

PAPER CHECK \#: XXXXX-XXXXXXXX ALL EEOBs

1 (V) EEOB Seq \# On ERA: 1 Net Payment Amt: 0.00

1.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One A/XXXX

Claim Bal: 0.00 Billed Amt: 19.47 Amt to Post: 0.00

Svc Dt: 1/27/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: ??

Payment Amt: 0.00 Total Adjustments: 0.00 Net: 0.00

2 (V) EEOB Seq \# On ERA: 3 Net Payment Amt: 509.61

2.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,Two A/XXXX

Claim Bal: 509.61 Billed Amt: 559.61 Amt To Post: 509.61

Svc Dt: 2/4/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: NO

Payment Amt: 590.61 Total Adjustments: 0.00 Net: 509.61

\+ Enter ?? for more actions

Full Acct Prof Bill Comment Log Scratch Pad Menu/Exit

Admin Cost Adj Re establish Bill

TPJI View/Print EEOB

Select Action: Next Screen/

The Receipt Processing option allows the user to jump to “RP Receipt Processing” with a pre-populated Receipt number and return to the Scratchpad. This action requires the RCDPEPP security key.

ERA Worklist/Scratch Pad Sep 17, 2015@15:30:24 Page: 1 of 2

ERA Entry \#: XXXXX Total Amt Pd: 8501.13 Current View:

Payer Name/ID: AETNA/XXXXXXXXXXX NO SORT ORDER

EFT \#/TRACE \#: XXXXX/XXXXXXXXXXXXXXX ALL EEOBS

\*\*\* RECEIPT(S) ALREADY CREATED \*\*\* (XXXXXXXXXX-XXXXXXXXXX)

Auto-Post Status: Complete Auto-Post Date: Aug 03, 2015

1 EEOB Seq \# On ERA: 1 Net Payment Amt: 7000.58

1.001 Claim \#: XXXXXXX Patient/Last 4: XX-XXXXXX,XXXX/XXXX

Claim Bal: 0.00 Billed Amt: 7000.58 Amt To Post: 7000.58

Svc Dt: 12/9/14 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 7000.58 Total Adjustments: 0.00 Net: 7000.58

Receipt: EXXXXXXXXX

2 (V)EEOB Seq \# On ERA: 2 Net Payment Amt: 1500.55

2.001 Claim \#: XXXXXXX Patient/Last 4: XX-XXXXXX,XXXX /XXXX

Claim Bal: 0.00 Billed Amt: 1500.55 Amt To Post: 1500.55

Svc Dt: 1/21/15 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

\+ Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

Distribute Adj Amts Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen// rp Receipt Processing

Select one of the following:

1 XXXXXXXXXX

2 XXXXXXXXXX

Select Receipt: 1

### ERA / 835 Screens for ePayments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERA / 835 screens are accessible from the main TPJI screen, by choosing the action option “EP ERA / 835.” The ERA / 835 screen will display ERA level summary data based on the claim# selected and displayed on the previous Main TPJI Screen, EOB / Claim level data and Claim level adjustments, and EEOB / Claim Line level data and adjustments.

3.  For pharmacy claims, the ECME#, Date of Service, Rx / Fill / Release Status shall be displayed. For medical claims, these data elements will be blank.

The following ePayments actions can be performed from the ERA / 835 Screen:

RX ECME Information CI Go to Claim Screen VP Policy Benefits

AR Account Profile BC Bill Charges EL Patient Eligibility

CM Comment History IR Insurance Reviews RP Receipt Profile

PE Print EEOB AD Additional 835 Data EX Exit

### Action Option: RX ECME Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to view ECME Claim Information. The user can select “EX Exit” to return to the TPJI Main screen or the user can select the action option “VER View ePharmacy Rx” to view detailed prescription data.

### Action Option: AR Account Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to view payment transaction details including the ERA#, TRACE#, Payer ID, and Receipt# that was used for posting the payment.

### Action Option: CM Comment History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to view Accounts Receivables comments for the claims account.

### Action Option: PE Print EEOB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to print EEOBs. The user may select either a single EEOB or all EEOBs for a claim.

When the user successfully selects an EEOB(s) for printing, the system prints the EOB / Claim level data, and Claim level adjustments, EOB / Claim Line level data, and Claim Line level adjustments for each EEOB selected for printing then returns the user to the ERA / 835 screen.

### Action Option: CI Go to Claim Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to return to the Claim Information screen.

### Action Option: BC Bill Charges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to view a bill’s charge information as it would print on the bill.

### Action Option: IR Insurance Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to view all insurance reviews for the episodes of care on a bill.

### Action Option: AD Additional 835 Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to view additional information found in the 835 at the EOB level. if sent by the payer. The additional 835 data is not mandated by HIPAA so additional information is sent at a payer’s discretion.

1.  Claim Code / Status

> 1 = Processed as Primary

> 2 = Processed as Secondary

> 3 = Processed as Tertiary

> 4 = Denied

> 19 = Processed as Primary, Forwarded to Additional Payer(s)

> 20 = Processed as Secondary, Forwarded to Additional Payer(s)

> 21 = Processed as Tertiary, Forwarded to Additional Payer(s)

> 22 = Reversal of Previous Payment

> 23 = Not Our Claim, Forwarded to Additional Payer(s)

> 25 = Predetermination Pricing Only - No Payment

178. Corrected Priority Payer Type

> AD = Blue Cross Blue Shield Association Plan Code

> FI = Federal Taxpayer’s Identification Number

> NI = National Association of Insurance Commissioners (NAIC) Identification

> PI = Payer Identification

> PP = Pharmacy Processor Number

> XV = Centers for Medicare and Medicaid Services PlanID

### Action Option: VP Policy Benefits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to view patient insurance policy data.

### Action Option: EL Patient Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to view current information on the patient’s eligibility for care and service connection status.

### Action Option: RP Receipt Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to view a bill and any of its associated transactions.

### Action Option: EX Exit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to return to the <u>TPJI Main Screen</u>.

4.  All the menus are described in detail in Section [⁠3⁠](#payments-processing) [⁠Payments Processing⁠](#payments-processing).

## Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menu option to edit parameters requires the user to hold security key RCDPE AUTO DEC. The following parameters are part of the ePayments software:

- Aging Payments

This parameter allows the user to select the specified number of days that will elapse before an unmatched payment (for an EFT detail line) will be reported. This parameter will be used when the report is run as part of the nightly processing. At installation, the Report Aging Payments site parameter will default to five days.

- Aging ERA

This parameter allows the user to select the specified number of days that will elapse before an unmatched ERA will be reported. This parameter will be used when the job is run as part of the nightly processing. At installation, the Report Aging ERA site parameter will default to seven days.

- Medical Claims Auto-Posting

This parameter allows the user to enable or disable auto-posting of third-party medical claims. At installation, the medical claims auto-posting site parameter will default to yes, which enables auto-posting.

- Medical Claims Auto-Posting Exclusion

This parameter allows the user to exclude specific payers from auto-posting of third-party medical claims by selecting the payer name or payer ID. At the time of installation, no payers are excluded from auto-posting. This parameter will only display if auto-posting of third-party medical claims is enabled.

The Payer prompt acts as a toggle. If a payer is selected, the payer will be added to the exclusion list if the payer is not already there or removed from the exclusion list if the payer is already there. A comment is required.

- Medical Claims with Payments Auto-Decrease

This parameter allows the user to enable or disable auto-decrease of third-party medical claims with payments. At installation, the medical claims auto-posting site parameter will default to no, which disables auto-decrease. This parameter will only display if auto-posting of third-party medical claims is enabled.

- Medical Claims with No Payments Auto-Decrease

This parameter allows the user to enable or disable auto-decrease of third-party medical claims with no payments. At installation, the medical claims auto-posting site parameter will default to no, which disables auto-decrease. This parameter will only display if auto-posting of third-party medical claims is enabled.

- Medical Claims Auto-Decrease Amount

This parameter allows the user to specify the maximum claim dollar amount of an automatic decrease adjustment that is made for a third-party medical claim. At installation, the amount is not populated, and the value is required to enable auto-decrease of third-party medical claims. This parameter will only display if auto-decrease of third-party medical claims is enabled.

- Medical Claims Auto-Decrease by CARC

This parameter allows the user to specify an individual CARC code to include in the auto-decreasing of third-party medical claims. The user must select the actual CARC by code to include auto-decreasing medical claims. Once validated and selected, the user must enter a maximum dollar amount that can be auto-decreased for the entered CARC. The maximum claim dollar amount displays with an initial default value of null, and a required response from 1 to 99999 dollars with the default amount being set to 5000. The dollar amount is represented without cents. This parameter will only display if auto-decrease of third-party medical claims is enabled.

- Medical Claims Auto-Decrease by CARC Amount

This parameter allows the user to specify the maximum claim dollar amount of an automatic decrease adjustment by CARC code that is made for a third-party medical claim. At installation, the amount is not populated and a value between 1 to 1500 dollars is required to enable auto-decrease of third-party medical claims by CARC. This parameter will only display if auto-decrease of third-party medical claims is enabled.

- Medical Claims Auto-Decrease Timeframe

This parameter allows the user to specify the number of days to wait before an automatic decrease adjustment is made for a third-party medical claim. The number of days is the time to wait after auto-posting completes. At installation, the timeframe is not populated, and the value is required to enable auto-decrease of third-party medical claims. This parameter will only display if auto-decrease of third-party medical claims is enabled.

- Medical Claims Auto-Decrease Exclusion

This parameter allows the user to exclude specific payers from auto-decrease of third-party medical claims by selecting the payer name or payer ID. At the time of installation, no payers are excluded from auto-decrease. This parameter will only display if auto-decrease of third-party medical claims is enabled.

The Payer prompt acts as a toggle. If a payer is selected, the payer will be added to the exclusion list if the payer is not already there or removed from the exclusion list if the payer is already there. A comment is required.

- Pharmacy Claims Auto-Posting

This parameter allows the user to enable or disable auto-posting of third-party pharmacy claims. At installation, the pharmacy claims auto-posting site parameter will default to NO.

- Pharmacy Claims Auto-Posting Exclusion

This parameter allows the user to exclude specific payers from auto-posting of third-party pharmacy claims by selecting the payer name or payer ID. At the time of installation, no payers are excluded from auto-posting. This parameter will only display if auto-posting of third-party pharmacy claims is enabled.

The Payer prompt acts as a toggle. If a payer is selected, the payer will be added to the exclusion list if the payer is not already there or removed from the exclusion list if the payer is already there. A comment is required.

- Pharmacy Claims Auto-Decrease

This parameter allows the user to enable or disable auto-decrease of third-party pharmacy claims. At installation, the pharmacy claims auto-decrease site parameter will default to no, which disables auto-decrease. This parameter will only display if auto-posting of third-party pharmacy claims is enabled.

- Pharmacy Claims Auto-Decrease Amount

This parameter allows the user to specify the maximum claim dollar amount of an automatic decrease adjustment that is made for a third-party pharmacy claim. At installation, the amount is not populated, and the value is required to enable auto-decrease of third-party pharmacy claims. This parameter will only display if auto-decrease of third-party pharmacy claims is enabled.

- Pharmacy Claims Auto-Decrease by CARC

This parameter allows the user to specify an individual CARC code to include in the auto-decreasing of third-party pharmacy claims. The user must select the actual CARC by code to include auto-decreasing pharmacy claims. Once validated and selected, the user must enter a maximum dollar amount that can be auto-decreased for the entered CARC. The maximum claim dollar amount displays with an initial default value of null, and a required response from 1 to 99999 dollars with the default amount being set to 5000. The dollar amount is represented without cents. This parameter will only display if auto-decrease of third-party pharmacy claims is enabled.

- Pharmacy Claims Auto-Decrease by CARC Amount

This parameter allows the user to specify the maximum claim dollar amount of an automatic decrease adjustment by CARC code that is made for a third-party pharmacy claim. At installation, the amount is not populated, and a value between 1 to 1500 dollars is required to enable auto-decrease of third-party pharmacy claims by CARC. This parameter will only display if auto-decrease of third-party pharmacy claims is enabled.

- Pharmacy Claims Auto-Decrease Timeframe

This parameter allows the user to specify the number of days to wait before an automatic decrease adjustment is made for a third-party pharmacy claim. after auto posting of a pharmacy payment. At installation, the timeframe is not populated, and the value is required to enable auto-decrease of third-party pharmacy claims. This parameter will only display if auto-decrease of third-party pharmacy claims is enabled.

- Pharmacy Claims Auto-Decrease Exclusion

This parameter allows the user to exclude specific payers from auto-decrease of third-party pharmacy claims by selecting the payer name or payer ID. At the time of installation, no payers are excluded from auto-decrease. This parameter will only display if auto-decrease of third-party pharmacy claims is enabled. The Payer prompt acts as a toggle. If a payer is selected, the payer will be added to the exclusion list if the payer is not already there or removed from the exclusion list if the payer is already there. A comment is required.

- Pharmacy Claims with Payments Auto-Decrease

This parameter allows the user to enable or disable auto-decrease of third-party pharmacy claims with payments. At installation, the third-party pharmacy claims auto-posting site parameter will default to no, which disables auto-decrease. This parameter will only display if auto-posting of third-party pharmacy claims with payments is enabled.

- Medical Claims Posting Prevention

This parameter allows the user to set the number of calendar days beyond which unposted medical payments (EFTs) will trigger an error message that prevents the user from posting newer medical EFTs. This parameter is used in the ERA Worklist when a user selects an ERA. At the time of installation, the value will be set to five (5) days if the current value is over the new parameter max of seven (7) days, otherwise it will remain the same. The value cannot be deleted, and valid entries are in the range of zero (0) days to seven (7) days.

- Pharmacy Claims Posting Prevention

This parameter allows the user to set the number of calendar days beyond which unposted pharmacy payments (EFTs) will trigger an error message that prevents the user from posting newer pharmacy EFTs. This parameter is used in the ERA Worklist when a user selects an ERA. At the time of installation, the value will be set to 365 days if the current value is over the new parameter max of 99 days, otherwise it will remain the same. The value cannot be deleted, and valid entries are in the range of 21 days to 99 days.

- Tricare Claims Posting Prevention

This parameter allows the user to set the number of calendar days beyond which unposted Tricare payments (EFTs) will trigger an error message that prevents the user from posting newer Tricare EFTs. This parameter is used in the ERA Worklist when a user selects an ERA. At the time of installation, the value will be set to 30 days if the current value is over the new parameter max of 60 days, otherwise it will remain the same. The value cannot be deleted, and valid entries are in the range of 14 days to 60 days.

- Tricare Claims Auto-Posting

This parameter allows the user to enable or disable auto-posting of third-party Tricare claims. At installation, the Tricare claims auto-posting site parameter will default to NO.

- Tricare Claims Auto-Decrease

This parameter allows the user to enable or disable auto-decrease of third-party Tricare claims. At installation, the Tricare claims auto-decrease site parameter will default to NO, which disables auto-decrease. This parameter will only display if auto-posting of third-party Tricare claims is enabled.

- Tricare Claims Auto-Decrease Amount

This parameter allows the user to specify the maximum claim dollar amount of an automatic decrease adjustment that is made for a third-party Tricare claim. At installation, the amount is not populated, and the value is required to enable auto-decrease of third-party Tricare claims. This parameter will only display if auto-decrease of third-party Tricare claims is enabled.

- Tricare Claims Auto-Decrease by CARC

This parameter allows the user to specify an individual CARC code to include in the auto-decreasing of third-party Tricare claims. Once validated and selected, the user must enter a maximum dollar amount that can be auto-decreased for the entered CARC. The maximum claim dollar amount displays with an initial default value of null and a required response from 1 to 99999 dollars. The dollar amount is represented without cents. This parameter will only display if auto-decrease of third-party Tricare claims is enabled.

- Tricare Claims Auto-Decrease by CARC Amount

This parameter allows the user to specify the maximum dollar amount of an automatic decrease adjustment by CARC code for a third-party Tricare claim. At installation, the amount is not populated and a value between 1 to 7000 dollars is required to enable auto-decrease of third-party Tricare claims by CARC. This parameter will only display if auto-decrease of third-party Tricare claims is enabled.

- Tricare Claims Auto-Decrease Timeframe

This parameter allows the user to specify the number of days to wait before an automatic decrease adjustment is made for a third-party Tricare claim after auto posting of a Tricare payment. At installation, the timeframe is not populated, and the value is required to enable auto-decrease of third-party Tricare claims. This parameter will only display if auto-decrease of third-party Tricare claims is enabled.

- Tricare Claims with Payments Auto-Decrease

This parameter allows the user to enable or disable auto-decrease of third-party Tricare claims with payments. At installation, the third-party Tricare claims auto-posting site parameter will default to NO, which disables auto-decrease. This parameter will only display if auto-posting of third-party Tricare claims with payments is enabled.

- Auto Audit for Medical, Pharmacy, and Tricare Bills

Three parameters exist to allow the user to enable or disable automatic auditing of paper and / or electronic medical, pharmacy, or Tricare bills. At installation, the auto audit site parameter will default to no, which disables auto auditing for Medical, Pharmacy, and Tricare claims.

- Add Suspense

The parameter allows the user to limit the number of days an entry can remain in Suspense. The parameter default is initially set at 45 days. The user can edit the parameter within the range of 1-120 days.

- Zero Payment Amount ERA Auto-Post

  The parameter allows the user to enable or disable auto-posting of zero payment amount ERAs. At installation, the parameter will default to no, which is disabled.

EDI Lockbox Parameters Screen

EDI Lockbox Parameters

Update AR Site Parameters

Select one of the following:

AA Auto-Audit Site Parameters

AD Auto-Decrease Parameters

AP Auto-Post Parameters

FP First Party Parameters

GN General EDI Lockbox Site Parameters

LK EFT Lock-Out Parameters

AL All

Enter response:

\### Auto-Audit Site Parameters \###

ENABLE AUTO-AUDIT FOR MEDICAL PAPER BILLS (Y/N): No// NO

ENABLE AUTO-AUDIT FOR PHARMACY PAPER BILLS (Y/N): No// NO

ENABLE AUTO-AUDIT FOR MEDICAL ELECTRONIC BILLS (Y/N): No// NO

ENABLE AUTO-AUDIT FOR PHARMACY ELECTRONIC BILLS (Y/N): No// NO

ENABLE AUTO-AUDIT FOR TRICARE BILLS (Y/N): Yes// YES

\### Auto-Decrease Parameters \###

\*\*\* Medical Auto-Decrease Parameters \*\*\*

ENABLE AUTO-DECREASE OF MEDICAL CLAIMS WITH PAYMENTS (Y/N): Yes// YES

MAXIMUM DOLLAR AMOUNT TO AUTO-DECREASE PER MEDICAL CLAIM: 900//

AUTO-DECREASE MEDICAL CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

=========================================================================

11 The diagnosis is inconsistent with the procedure. ... 217

20 This injury/illness is covered by the liability ca ... 1

22 This care may be covered by another payer per coor ... 670

23 The impact of prior payer(s) adjudication includin ... 10

24 Charges are covered under a capitation agreement/m ... 15

25 Payment denied. Your Stop loss deductible has not ... 19 (I)

33 Insured has no dependent coverage. 19

50 These are non-covered services because this is not ... 77

56 Procedure/treatment has not been deemed "proven to ... 19

CARC:

NUMBER OF DAYS TO WAIT BEFORE MEDICAL AUTO-DECREASE (0-7): 5//

ENABLE AUTO-DECREASE OF MEDICAL CLAIMS WITH NO PAYMENTS (Y/N): Yes// YES

AUTO-DECREASE NO-PAY MEDICAL CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

=========================================================================

20 This injury/illness is covered by the liability ca ... 222

22 This care may be covered by another payer per coor ... 10

23 The impact of prior payer(s) adjudication includin ... 19

24 Charges are covered under a capitation agreement/m ... 16

25 Payment denied. Your Stop loss deductible has not ... 25 (I)

35 Lifetime benefit maximum has been reached. 40

46 This (these) service(s) is (are) not covered. 19 (I)

CARC:

NUMBER OF DAYS TO WAIT BEFORE MEDICAL NO PAY AUTO-DECREASE (0-45): 0//

\*\* Additional Payers excluded from Medical Auto-Decrease:

LOYAL AM/CONT GEN/UNTD TEACHER/GRT AMER/PROV AMER/CENTRL RES XXXXXXXXXX

PRINCIPAL FINANCIAL GROUP XXXXXXXXXX

PACIFICARE OF ARIZONA XXXXXXXXXX

CONSECO LIFE INSURANCE COMPANY XXXXXXXXXX

KENTUCKY PHYSICIANS PLAN \# XXXXXXXXXX

TRUSTEES OF HEALTH ACCESS INSURANCE XXXXXXXXXX

All payers excluded from Auto-Posting are also excluded from Auto-Decrease.

Select a Payer to add or remove from the exclusion list.

Payer:

\*\* Additional Payers excluded from Medical Auto-Decrease:

LOYAL AM/CONT GEN/UNTD TEACHER/GRT AMER/PROV AMER/CENTRL RES XXXXXXXXXX

PRINCIPAL FINANCIAL GROUP XXXXXXXXXX

PACIFICARE OF ARIZONA XXXXXXXXXX

CONSECO LIFE INSURANCE COMPANY XXXXXXXXXX

KENTUCKY PHYSICIANS PLAN XXXXXXXXXX

TRUSTEES OF HEALTH ACCESS INSURANCE XXXXXXXXXX

All payers excluded from Auto-Posting are also excluded from Auto-Decrease.

\*\*\* Pharmacy Auto-Decrease Parameters \*\*\*

ENABLE AUTO-DECREASE OF PHARMACY CLAIMS WITH PAYMENTS (Y/N): Yes// YES

MAXIMUM DOLLAR AMOUNT TO AUTO-DECREASE PER PHARMACY CLAIM: 100//

AUTO-DECREASE PHARMACY CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

=========================================================================

22 This care may be covered by another payer per coor ... 10

23 The impact of prior payer(s) adjudication includin ... 100

33 Insured has no dependent coverage. 50

46 This (these) service(s) is (are) not covered. 22 (I)

CARC:

\*\* Additional Payers excluded from Pharmacy Auto-Decrease

GERBER LIFE INS XXXXXXXXXX

PRINCIPAL FINANCIAL GROUP XXXXXXXXXX

Select a Payer to add or remove from the exclusion list.

Payer:

\*\* Additional Payers excluded from Pharmacy Auto-Decrease

GERBER LIFE INS XXXXXXXXXX

PRINCIPAL FINANCIAL GROUP XXXXXXXXXX

NUMBER OF DAYS TO WAIT BEFORE PHARMACY AUTO-DECREASE (0-7): 0//

\### Auto-Post Parameters \###

\*\*\* Medical Auto-Post Parameters \*\*\*

ENABLE AUTO-POSTING OF MEDICAL CLAIMS (Y/N): Yes// YES

Payers excluded from Medical Auto-Posting:

MUTUAL OF OMAHA XXXXXXXXXX

GERBER LIFE INS XXXXXXXXXX

AETNA AMERICAN CONTINENTAL INSURANCE COMPANY XXXXXXXXXX

JOHN ALDEN LIFE COMPANY XXXXXXXXXX

HARTFORD LIFE & ACCIDENT INS XXXXXXXXXX

PRINCIPAL LIFE INSURANCE CO XXXXXXXXXX

UNITED HEALTHCARE SERVICES INC AND XXXXXXXXXX

Select a Payer to add or remove from the exclusion list.

Payer:

Payers excluded from Medical Auto-Posting:

MUTUAL OF OMAHA XXXXXXXXXX

GERBER LIFE INS XXXXXXXXXX

AETNA AMERICAN CONTINENTAL INSURANCE COMPANY XXXXXXXXXX

JOHN ALDEN LIFE COMPANY XXXXXXXXXX

HARTFORD LIFE & ACCIDENT INS XXXXXXXXXX

PRINCIPAL LIFE INSURANCE CO XXXXXXXXXX

UNITED HEALTHCARE SERVICES INC AND XXXXXXXXXXX

\*\*\* Pharmacy Auto-Post Parameters \*\*\*

ENABLE AUTO-POSTING OF PHARMACY CLAIMS (Y/N): Yes// YES

Payers excluded from Pharmacy Auto-Posting

HARTFORD LIFE & ACCIDENT INS XXXXXXXXXX

AETNA -CONTINENTAL LIFE INSURANCE COMPANY OF BRENTWOOD XXXXXXXXXX

CIGNA BEHAVIORAL HEALTH XXXXXXXXXX

PACIFICARE OF ARIZONA XXXXXXXXXX

BANK ONE CORPORATION XXXXXXXXXX

Select a Payer to add or remove from the exclusion list.

Payer:

Payers excluded from Pharmacy Auto-Posting

HARTFORD LIFE & ACCIDENT INS XXXXXXXXXX

AETNA -CONTINENTAL LIFE INSURANCE COMPANY OF BRENTWOOD XXXXXXXXXX

CIGNA BEHAVIORAL HEALTH XXXXXXXXXX

PACIFICARE OF ARIZONA XXXXXXXXXX

BANK ONE CORPORATION \# XXXXXXXXXX

\### First Party Parameters \###

FIRST PARTY PARAMETERS FOR AUTO-POSTED CLAIMS (AUTO-POST)

AUTO-DECREASE FIRST PARTY COPAY CLAIMS (AUTO-POST): YES//

Charge types enabled for 1st party auto-decrease (AUTO-POST)

All Inpatient, Outpatient and Pharmacy, except “CANCEL” charges.

DAYS TO WAIT BEFORE FIRST PARTY AUTO-DECREASE (AUTO-POST): 0//

FIRST PARTY PARAMETERS FOR MANUALLY POSTED CLAIMS (MANUAL)

AUTO-DECREASE FIRST PARTY COPAY CLAIMS (MANUAL): YES//

Charge types enabled for 1st party auto-decrease (MANUAL)

DG FEE SERVICE (OPT) NEW

DG OPT COPAY NEW

CC (OPT) NEW

\### General EDI Lockbox Site Parameters \###

NUMBER OF DAYS EFT UNMATCHED: 5//

NUMBER OF DAYS ERA UNMATCHED: 4//

\#DAYS ENTRY CAN REMAIN IN SUSP: 3//

SELECT DAY TO SEND WORKLOAD NOTIFICATION: SATURDAY// SATURDAY

\### ZERO PAYMENT Auto-Post Parameters \###

ENABLE AUTO-POSTING OF ZERO PAYMENT AMOUNT ERAs (Y/N): No// NO

\### EFT Lock-Out Parameters \###

NUMBER OF DAYS EFT UNMATCHED: 5//

NUMBER OF DAYS ERA UNMATCHED: 7//

\#DAYS ENTRY CAN REMAIN IN SUSP: 45//

### Parameters Report – EDI Lockbox (ePayments) Parameters Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Lockbox Parameters Report provides a listing of all parameters with current settings. The report can be run on-demand on an as-needed basis to view or print parameter settings.

#### When to Run this Report

Review the EDI Lockbox (ePayments) Parameters Report on an as-needed basis to view or print changes to settings. The report can be run on-demand.

#### How to Run this Report

To run the EDI Lockbox (ePayments) Parameters Report, select EDI Lockbox Parameters Report, and then choose Medical, Pharmacy, Tricare, or All.

The EDI Lockbox (ePayments) Parameters Report follows:

EDI Lockbox Parameters Report

(M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EDI Lockbox Parameters Report - ALL Page: 1

Run Date: Nov 20, 2018@11:29:09 Site: CHEYENNE VAMC

Categories: General EDI Lockbox Site, Auto-Audit Site, Auto-Decrease, EFT Lock-Out, First Party

------------------------------------------------------------------------------

\### General EDI Lockbox Site Parameters \###

NUMBER OF DAYS EFT UNMATCHED: 5

NUMBER OF DAYS ERA UNMATCHED: 7

\#DAYS ENTRY CAN REMAIN IN SUSP: 45

DAY FOR WORKLOAD NOTIFICATIONS: SATURDAY

\### Auto-Audit Site Parameters \###

ENABLE AUTO-AUDIT MEDICAL PAPER BILLS: Yes

ENABLE AUTO-AUDIT RX PAPER BILLS: Yes

ENABLE AUTO-AUDIT MEDICAL EDI BILLS: Yes

ENABLE AUTO-AUDIT RX EDI BILLS: Yes

ENABLE AUTO-AUDIT TRICARE BILLS: Yes

\### Auto-Decrease Parameters \###

\*\*\* Medical Auto-Decrease\*\*\*

ENABLE AUTO-DECREASE OF MEDICAL CLAIMS WITH PAYMENTS: Yes

MAXIMUM DOLLAR AMOUNT TO AUTO-DECREASE PER MEDICAL CLAIM: \$7000

AUTO-DECREASE MEDICAL CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

----------------------------------------------------------------------

2 Coinsurance Amount 1

4 The procedure code is inconsistent with the modifi .. 1

5 The procedure code/bill type is inconsistent with .. 1

3 Co-payment Amount 10

10 The diagnosis is inconsistent with the patient"s g .. 250

42 Charges exceed our fee schedule or maximum allowab .. 1 (I)

43 Gramm-Rudman reduction. 100 (I)

NUMBER OF DAYS TO WAIT BEFORE MEDICAL AUTO-DECREASE: 5

ENABLE AUTO-DECREASE OF NO-PAY MEDICAL CLAIMS: Yes

AUTO-DECREASE NO-PAY MEDICAL CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

----------------------------------------------------------------------

1 Deductible Amount 1

2 Coinsurance Amount 1

3 Co-payment Amount 15

4 The procedure code is inconsistent with the modifi .. 1

42 Charges exceed our fee schedule or maximum allowab .. 1 (I)

43 Gramm-Rudman reduction. 100 (I)

45 Charge exceeds fee schedule/maximum allowable or c .. 7000

NUMBER OF DAYS TO WAIT BEFORE MEDICAL NO PAY AUTO-DECREASE: 1

All payers excluded from Auto-Posting are excluded from Auto-Decrease.

Additional Excluded Payer Comment

AETNA-CONTINENTAL LIFE INSURANCE C enter comment

ANHEUSER-BUSCH enter comment

UNITED HEALTH CARE enter comment

\*\*\* Pharmacy Auto-Decrease\*\*\*

ENABLE AUTO-DECREASE OF PHARMACY CLAIMS WITH PAYMENTS: Yes

MAXIMUM DOLLAR AMOUNT TO AUTO-DECREASE PER PHARMACY CLAIM: \$7000

AUTO-DECREASE PHARMACY CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

----------------------------------------------------------------------

2 Coinsurance Amount 1

4 The procedure code is inconsistent with the modifi .. 1

5 The procedure code/bill type is inconsistent with .. 1

3 Co-payment Amount 10

10 The diagnosis is inconsistent with the patient"s g .. 250

42 Charges exceed our fee schedule or maximum allowab .. 1 (I)

43 Gramm-Rudman reduction. 100 (I)

NUMBER OF DAYS TO WAIT BEFORE PHARMACY AUTO-DECREASE: 5

ENABLE AUTO-DECREASE OF TRICARE CLAIMS WITH PAYMENTS: Yes

MAXIMUM DOLLAR AMOUNT TO AUTO-DECREASE PER TRICARE CLAIM: \$7000

AUTO-DECREASE TRICARE CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

----------------------------------------------------------------------

2 Coinsurance Amount 1

4 The procedure code is inconsistent with the modifi .. 1

5 The procedure code/bill type is inconsistent with .. 1

3 Co-payment Amount 10

10 The diagnosis is inconsistent with the patient"s g .. 250

42 Charges exceed our fee schedule or maximum allowab .. 1 (I)

43 Gramm-Rudman reduction. 100 (I)

NUMBER OF DAYS TO WAIT BEFORE TRICARE AUTO-DECREASE: 5

ENABLE AUTO-DECREASE OF NO PAY TRICARE CLAIMS: Yes

AUTO-DECREASE NO PAY TRICARE CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

----------------------------------------------------------------------

2 Coinsurance Amount 1

4 The procedure code is inconsistent with the modifi .. 1

5 The procedure code/bill type is inconsistent with .. 1

3 Co-payment Amount 10

10 The diagnosis is inconsistent with the patient"s g .. 250

42 Charges exceed our fee schedule or maximum allowab .. 1 (I)

43 Gramm-Rudman reduction. 100 (I)

\*\*\* ZERO PAYMENT AMOUNT ERA Auto-Post Parameters \*\*\*

ENABLE AUTO-POSTING OF ZERO PAYMENT AMOUNT ERAs: No

\### EFT Lock-Out Parameters \###

NUMBER OF DAYS TO WAIT BEFORE TRICARE NO PAY AUTO-DECREASE: 5

ENABLE AUTO-POSTING OF PHARMACY CLAIMS: No

NUMBER OF DAYS (AGE) OF UNPOSTED MEDICAL EFTS TO PREVENT POSTING: 30

NUMBER OF DAYS (AGE) OF UNPOSTED PHARMACY EFTS TO PREVENT POSTING: 99

NUMBER OF DAYS (AGE) OF UNPOSTED MEDICAL TRICARE TO PREVENT POSTING: 14

\### First Party Parameters \###

AUTO-DECREASE FIRST PARTY COPAY CLAIMS (AUTO-POST): YES

DAYS TO WAIT BEFORE FIRST PARTY AUTO-DECREASE (AUTO-POST): 0

AUTO-DECREASE FIRST PARTY COPAY CLAIMS (MANUAL): YES

\*\*\*\*\* END OF REPORT \*\*\*\*\*

### Parameters Report – EDI Lockbox (ePayments) Parameters Audit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Lockbox (ePayments) Parameters Audit Report provides an audit of changes to parameter questions. The information on the report contains the date and time a parameter was edited, the old value, the new value, and the user who completed the edit.

#### When to Run this Report

Review the EDI Lockbox (ePayments) Parameters Audit Report on an as-needed basis to view or print changes to settings. The report can be run on-demand.

#### How to Run this Report

To run the EDI Lockbox (ePayments) Parameters Audit Report, enter a start and end date, and select a division. The resulting report will contain parameters that have been changed within the date range. The report can also be exported to Excel.

The EDI Lockbox (ePayments) Parameters Audit Report follows:

EDI Lockbox Parameters Audit Report

(M)edical, (P)harmacy,(T)ricare or A(ll): A// ll

Report start date: t-10 (NOV 10, 2018)

Report end date: Nov 20, 2018// t (NOV 20, 2018)

Export the report to Microsoft Excel? (Y/N): NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EDI Lockbox Parameter Audit Report Page: 1

RUN DATE: 11/20/2018@11:19:48

DATE RANGE: 11/10/2018 - 11/20/2018

REPORT TYPE: All M/P/T

LOCKBOX PARAMETER UPDATES

-------------------------- Values

Parameter Date/Time Edited Old New User

===============================================================================

AUTO-AUDIT MEDICAL PAPER BILLS 11/13/18@10:13:04 Yes No PATIENT,ONE

AUTO-AUDIT RX PAPER BILLS 11/13/18@10:13:05 Yes No PATIENT,ONE

AUTO-AUDIT MEDICAL EDI BILLS 11/13/18@10:13:07 Yes No PATIENT,ONE

AUTO-AUDIT RX EDI BILLS 11/13/18@10:13:09 Yes No PATIENT,ONE

AUTO-POST RX CLAIMS ENABLED 11/15/18@11:03:40 No Yes PATIENT,ONE

TRICARE EFT POST PREVENT DAYS 11/15/18@11:18:49 14 30 PATIENT,ONE

TRICARE EFT POST PREVENT DAYS 11/15/18@11:19:14 30 14 PATIENT,ONE

AUTO-POST RX CLAIMS ENABLED 11/15/18@11:19:30 Yes No PATIENT,ONE

AUTO-POST MED CLAIMS ENABLED 11/15/18@11:55:51 Yes No PATIENT,ONE

AUTO-POST MED CLAIMS ENABLED 11/16/18@12:20:44 No Yes PATIENT,ONE

AUTO-DECREASE MED NOPAY ENABLED 11/16/18@12:21:01 No Yes PATIENT,ONE

AUTO-DECREASE MED AMT DEFAULT 11/16/18@13:48:25 250 7000 PATIENT,ONE

CARC AUTO DECREASE NO-PAY (45) 11/16/18@13:51:17 No Yes PATIENT,ONE

AUTO-DECREASE TRI ENABLED 11/16/18@12:21:01 No Yes PATIENT,ONE

AUTO-DECREASE TRI AMT DEFAULT 11/16/18@13:48:25 250 7000 PATIENT,ONE

CARC AUTO DECREASE TRI (45) 11/16/18@13:51:17 No Yes PATIENT,ONE

AUTO-DECREASE TRI NOPAY ENABLED 11/16/18@12:21:01 No Yes PATIENT,ONE

CARC AUTO DECREASE TRI NOPAY (45)11/16/18@13:51:17 No Yes PATIENT,ONE

AUTO-POST ZERO PAY ENABLED 11/16/18@14:52:02 0 1 PATIENT,ONE

\*\*\*\*\* END OF REPORT \*\*\*\*\*

### Parameters Report – EDI Lockbox Exclusion Audit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Lockbox Exclusion Audit Report provides an audit of changes to excluded payers. The information on the report contains the date and time a payer was added or removed from the exclusion list, the user who completed the edit, and a comment.

#### When to Run this Report

Review the EDI Lockbox Exclusion Audit Report on an as-needed basis to view or print changes to payer exclusions. The report can be run on-demand.

#### How to Run this Report

To run the EDI Lockbox Exclusion Audit Report, enter a start date, end date, and select a division. The resulting report will contain payer exclusions that have been changed within the date range. The report can also be exported to Excel.

EDI Lockbox Exclusion Audit Report

(M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

Report start date: t-100 (AUG 28, 2018)

Report end date: Dec 06, 2018// t (DEC 06, 2018)

Export the report to Microsoft Excel? (Y/N): NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EDI Lockbox Exclusion Audit Report Page: 1

DIVISIONS: ALL

RUN DATE: 12/6/2018@07:41:38

DATE RANGE: 8/28/2018 - 12/6/2018

REPORT TYPE: ALL

MEDICAL AUTO-POSTING PAYER EXCLUSION LIST

-----------------------------------------

Change Payer Date/Time Edited User

===============================================================================

No Auto-post Exclusions to Display

MEDICAL AUTO-DECREASE PAYER EXCLUSION LIST

------------------------------------------

Change Payer Date/Time Edited User

===============================================================================

Added UNITED HEALTH CARE XXXXXXXXXX 8/29/18@08:50:50 PATIENT,ONE

Comment: testing

Added AETNA -CONTINENTAL LIFE INSURA 9/20/18@09:05:40 PATIENT,ONE

Comment: testing

PHARMACY AUTO-POSTING PAYER EXCLUSION LIST

------------------------------------------

Change Payer Date/Time Edited User

===============================================================================

Added AETNA XXXXXXXXXX 8/29/18@08:51:06 PATIENT,ONE

Comment: testing

PHARMACY AUTO-DECREASE PAYER EXCLUSION LIST

------------------------------------------

Change Payer Date/Time Edited User

===============================================================================

Added UNITED HEALTH CARE XXXXXXXXXX 8/29/18@08:50:50 PATIENT,ONE

Comment: testing

Added AETNA -CONTINENTAL LIFE INSURA 9/20/18@09:05:40 PATIENT,ONE

Comment: testing

TRICARE AUTO-POSTING PAYER EXCLUSION LIST

-----------------------------------------

Change Payer Date/Time Edited User

===============================================================================

No Auto-post Exclusions to Display

TRICARE AUTO-DECREASE PAYER EXCLUSION LIST

------------------------------------------

Change Payer Date/Time Edited User

===============================================================================

Added UNITED HEALTH CARE XXXXXXXXXX 8/9/18@08:50:50 PATIENT,ONE

Comment: testing

Added AETNA -CONTINENTAL LIFE INSURA 9/20/18@09:05:40 PATIENT,ONE

Comment: testing

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Seven mail groups are associated with EDI Lockbox. The names of these mail groups are:

- RCDPE PAYMENTS: This group will receive all reports and bulletins generated by the nightly processing job and from all other EDI Lockbox jobs, except for those resulting from exceptions found when storing the EDI Lockbox transmission records.
- RCDPE PAYMENTS EXCEPTIONS: This group will receive all bulletins for exception conditions generated by the receipt of all EDI Lockbox electronic messages. Exceptions occur when the software cannot identify a bill number in the site’s VistA system. This group also receives error bulletins generated by the receipt and processing of the CARC / RARC date from the FSC.
- RCDPE PAYMENTS MGMT: This group previously received the bulletin that is sent when an EEOB transferred out of the site is accepted by another site. Transfer functionality is no longer available.
- RCDPE AUDIT: This group will systematically notify management of critical outstanding workload related to aged ERAs and EFTs. This includes:
- Unmatched ERAs greater than 30 days.
- Matched / not posted ERAs greater than 30 days.
- EFTs greater than 14 days.

The AR application will flag the above-mentioned bulletins as high priority. These bulletins can be scheduled weekly, biweekly, or monthly, and the specific day of the week can be set in the EDI Lockbox parameters. All bulletins will be scheduled for the same cycle. End users can self-enroll in this mail group.

- RCDPE MOVE COPY: This mail group previously received bulletins sent by the AR nightly process. The bulletins are no longer sent.
- MLB: This mail group receives all transmission messages relating to EDI Lockbox. These messages contain the detailed transmission data.

It is a local decision as to who will be members of these mail groups. It is recommended, at a minimum, that the MCCF Supervisor or Lead AR be included. Important: The electronic data is sent to VistA through these mail man messages. If no one is assigned to these mail groups, the electronic data will not be stored in VistA. These messages also help with trouble shooting, and problem solving. Appendix E contains a list of the bulletins and recommendations on how to handle each message.

- CARC_RARC_DATA: This mail group receives all transmission messages related to CARC / RARC data sent by the FSC. These messages contain the detailed transmission data that automatically updates CARC / RARC data in VistA.

It is a local decision as to who will be members of this mail group. It is recommended, at a minimum, that the local Install Release Manager (IRM) be included. Important: These messages may help with trouble shooting, and problem solving that may be needed; any error messages will be sent as an error bulletin to RCDPE PAYMENTS EXCEPTIONS group containing all errors discovered in the entire message.

## How to Read an ERA / 835

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 835 is a transaction set created by HIPAA standards. The transaction format defines what data should be included in the Electronic Remittance Advice (ERA) for use in the world of Electronic Data Interchange (EDI). The technical term ‘835’ is used in the healthcare industry when referring to an ERA – Electronic Remittance Advice. ERAs, or 835’s can be found in the ePayments software in the worklist, view / print options, or under Billed Charges (BC) in the TPJI menu. ERAs are sent in a standard format as defined by HIPAA and include standard Claim adjustment reason codes (CARC’s).

EDI LOCKBOX EEOB DETAIL FROM WORKLIST 7/22/10 Page: 1

ERA NUMBER: XXXXXXXXXX ERA DATE: Jul 21, 2010

INS COMPANY: IBinsurance Company One/ XXXXXXXXX

ERA TRACE \#: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

================================================================================

The example above shows the user the ERA number, trace number and date, and payer information.

This is on page one (1) of the ERA.

EDI LOCKBOX EEOB DETAIL FROM WORKLIST 10/12/18 Page: 1

ERA NUMBER: 93324 ERA DATE: Oct 02, 2018

INS COMPANY: AETNA/ XXXXXXXXXX

ERA TRACE \#: XXXXXXXXXXXXX

================================================================================

CLAIM \#: XXX-XXXXXX

ORIGINAL PATIENT NAME: PATIENT,ONE

EOB GENERAL INFORMATION:

Type : NORMAL EOB EOB Paid DT : 10/02/18

Entry Dt/Tm :10/02/18 7:11 am Claim Status : PROCESSED

Entry Dt/Tm :10/02/18 7:11 am Review Status: ACCEPTED-COMPLETE EOB

Entered By : Insurance Seq: SECONDARY

Last Edited : 10/02/18 7:12 am Last Edit By : POSTMASTER

Patient Name: CASE,ONE Pt. Relation : PATIENT

Insured ID : XXXXXXXXXX

Claim Rec'd Date :

Other Subscriber Name:

Also included on page one is the:

- Bill Number
- Patient Name
- ID Number
- Claim Status
- Patient Relationship

The user sees the Payer Information including payer name, payer ID number, and the payers Internal Control Number (ICN) and any other claim level contact information on page two (2).

The claim level contact information can also be viewed from: Claim Information \> Comment History option available under TPJI. TPJI is available through many menu paths, such as EDI Lockbox \> ERA Worklist \> Select ERA \> Research Menu \> TPJI.

EDI LOCKBOX EEOB DETAIL FROM WORKLIST 7/22/10 Page: 3

ERA NUMBER: XXXXXXXXXX ERA DATE: Jul 21, 2010

INS COMPANY: IBinsurance Company One/XXXXXXXXX

ERA TRACE \#: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

================================================================================

CLAIM LEVEL PAY STATUS:

Tot Submitted Chrg: 102.95 Covered Amt : 0.00

Payer Paid Amt : 20.59 Patient Resp. Amt : 0.00

CLAIM LEVEL ADJUSTMENTS:

NONE

MEDICARE INFORMATION:

NONE

LINE LEVEL ADJUSTMENTS:

\# SV DT REVCD PROC MOD UNITS BILLED DEDUCT COINS ALLOW PYMT

1 06/01/10 510 99213 1 102.95 0.00 0.00 102.95 20.59

ADJ: CO 23 Payment adjusted because charges have been paid by another payer.

ADJ AMT: 82.36

The top of page three (3) shows the user the submitted charges, covered amount, and amount paid in the Claim Level Pay status section of the ERA.

EDI LOCKBOX EEOB DETAIL FROM WORKLIST 7/22/10 Page: 3

ERA NUMBER: XXXXXXXXXX ERA DATE: Jul 21, 2010

INS COMPANY: IBinsurance Company One/XXXXXXXXX

ERA TRACE \#: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

================================================================================

CLAIM LEVEL PAY STATUS:

Tot Submitted Chrg: 102.95 Covered Amt : 0.00

Payer Paid Amt : 20.59 Patient Resp. Amt : 0.00

CLAIM LEVEL ADJUSTMENTS:

NONE

MEDICARE INFORMATION:

NONE

LINE LEVEL ADJUSTMENTS:

\# SV DT REVCD PROC MOD UNITS BILLED DEDUCT COINS ALLOW PYMT

1 06/01/10 510 XXXXX 1 102.95 0.00 0.00 102.95 20.59

ADJ: CO 23 Payment adjusted because charges have been paid by another payer.

ADJ AMT: 82.36

Enter RETURN to continue or '^' to exit:

At the bottom of page three (3), the user can see the Claim Adjudication details that include the HIPAA standardized justification codes. Adjudication details can be continued on page four (4) depending on the number of procedures included on the claim to the payer.

## Workload Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AR application systematically notifies management of critical outstanding workload related to aged ERAs and EFTs. There are four (4) workload notifications. They are the Unmatched ERA’s \> 30 days, the Paper Matched / Not Posted ERAs \> 30 days, the EFT Matched / Not Posted ERAs \>30 days, and the Unmatched EFTs \> 14 days. The notifications are sent to a mail group, RCPDE Audit, and can be queued for weekly, bi-weekly, or monthly notifications. All the notifications will be flagged as high priority.

### Unmatched ERAs \> 30 Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A warning bulletin is sent to the RCDPE AUDIT Mail Group for unmatched ERAs greater than 30 days.

Subj: EDI LBOX-STA# 442-ACTION REQ-Unmatched ERAs \> 30 days \[XXXXX\]

11/17/11@11:20 142 lines

From: POSTMASTER In 'IN' basket Page 1 Priority!

-------------------------------------------------------------------------------

The listed ERAs were received more than 30 days ago and have not yet been

matched.

Total \# of ERAs - 134

Total Dollar Amount - \$53,638.41

ERA# PAYER NAME FILE DATE AMOUNT PAID

XX AETNA 4/21/04 \$0.00

XXX UNITED HEALTH CARE 6/10/04 \$749.61

XXXXX GREAT-WEST LIFE 2/22/07 \$320.94

XXXXX MUTUAL OF OMAHA COMPANIES 2/22/07 \$9.76

XXXXX MAIL HANDLERS BENEFIT PLAN 2/22/07 \$29.25

XXXXX NALC HBP 2/22/07 \$463.67

XXXXX NALC HBP 2/22/07 \$12.21

XXXXX GREAT-WEST LIFE 2/23/07 \$489.92

XXXXX GREAT-WEST LIFE 2/23/07 \$65.37

XXXXX GREAT-WEST LIFE 2/23/07 \$65.37

XXXXX MUTUAL OF OMAHA COMPANIES 2/23/07 \$4.66

Subj: EDI LBOX-STA# 442-ACTION REQ-Unmatched ERAs \> 30 days \[XXXXXXX\]

11/17/11@11:20 142 lines

From: POSTMASTER In 'IN' basket Page 1 Priority!

-------------------------------------------------------------------------------

The listed ERAs were received more than 30 days ago and have not yet been

matched.

Total \# of ERAs - 134

Total Dollar Amount - \$53,638.41

ERA# PAYER NAME FILE DATE AMOUNT PAID

XX AETNA 4/21/04 \$0.00

XXX UNITED HEALTH CARE 6/10/04 \$749.61

XXXXX GREAT-WEST LIFE 2/22/07 \$320.94

XXXXX MUTUAL OF OMAHA COMPANIES 2/22/07 \$9.76

XXXXX MAIL HANDLERS BENEFIT PLAN 2/22/07 \$29.25

XXXXX NALC HBP 2/22/07 \$463.67

XXXXX NALC HBP 2/22/07 \$12.21

XXXXX GREAT-WEST LIFE 2/23/07 \$489.92

XXXXX GREAT-WEST LIFE 2/23/07 \$65.37

XXXXX GREAT-WEST LIFE 2/23/07 \$65.37

XXXXX MUTUAL OF OMAHA COMPANIES 2/23/07 \$4.66

Subj: EDI LBOX-STA# 442-ACTION REQ-Matched/Not Posted ERAs \> 30 days \[XXXXXXX\]

11/17/11@11:20 58 lines

From: POSTMASTER In 'IN' basket Page 1 Priority!

-------------------------------------------------------------------------------

The listed ERAs were received more than 30 days ago and have been matched but

have not been posted

Total \# of ERAs - 50

Total Dollar Amount - \$75,710,095,295.75

ERA# PAYER NAME FILE DATE AMOUNT PAID

XXXXX BCBS of WY and Affiliated Companies 9/28/10 \$1,077.86

XXXXX SF MUTUAL 3/2/07 \$75.48

XXXXX BCBS of WY and Affiliated Companies 9/28/10 \$1,077.86

XXXXX BCBS of WY and Affiliated Companies 9/28/10 \$1,077.86

XXXXX UNITED HEALTH CARE 2/12/07 \$715.99

XXXXX MAIL HANDLERS BENEFIT PLAN 2/16/07 \$129.26

XXXXX MAIL HANDLERS BENEFIT PLAN 2/16/07 \$123.48

XXXXX MAIL HANDLERS BENEFIT PLAN 2/16/07 \$18.53

XXXXX GREAT-WEST LIFE 2/20/07 \$8.32

XXXXX MAIL HANDLERS BENEFIT PLAN 2/20/07 \$285.60

XXXXX MAIL HANDLERS BENEFIT PLAN 2/20/07 \$160.00

### PAPER Matched / Not Posted ERAs \> 30 Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A warning bulletin is sent to the RCDPE AUDIT mail group for Paper Checks Matched / Not Posted that are matched to ERAs \>30 days but not yet posted.

From: POSTMASTER@XXXXX.MED.VA.GOV

Sent: Thursday, July 31, 2014 6:01 AM

To: "G.RCDPE AUDIT"@XXXXX.MED.VA.GOV

Subject: EDI LBOX-STA# 504-ACTION REQ-PAPER:Matched/Not Posted ERA\>30 days

Importance: High

The listed ERAs were received more than 30 days ago and have been matched but  
have not been posted

Total \# of ERAs - “MATCHED TO PAPER CHECK” - 4

Total Dollar Amount - \$2,076.49

ERA# PAYER NAME FILE DATE AMOUNT PAID

XXXXX CONNECTICUT GENERAL LIFE INSURANCE 4/4/12 \$2.04

XXXXX WOODMEN OF THE WORLD ASSURED LIFE A 4/19/12 \$1,831.22

XXXXX THRIVENT FINANCIAL FOR LUTHERANS 5/7/12 \$102.20

XXXXX NALC HBP 5/18/12 \$141.03

\*\* END OF REPORT \*\*

### EFT Matched / Not Posted ERAs \> 30 Days Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A warning bulletin is sent to the RCDPE AUDIT mail group for EFT Matched / EFTs that are matched to an ERA \>30 days but not yet posted.

From: POSTMASTER@XXXXX.MED.VA.GOV

Sent: Thursday, July 31, 2014 6:01 AM

To: "G.RCDPE AUDIT"@XXXXX.MED.VA.GOV

Subject: EDI LBOX-STA# 504-ACTION REQ-EFT:Matched/Not Posted ERA\>30 days

Importance: High

The listed ERAs were received more than 30 days ago and have been matched but  
have not been posted

Total \# of ERAs - “MATCHED TO EFT” - 5

Total Dollar Amount - \$2,041.91

ERA# PAYER NAME FILE DATE AMOUNT PAID XXXXX OUTREACH HEALTH CARE SERVICES 5/31/12 \$1,227.73

XXXXX ValueOptions, Inc . 7/11/12 \$144.68

XXXXX ROYAL NEIGHBORS OF AMERICA 8/2/12 \$33.70

XXXXX TLPEXTON 8/6/12 \$8.99

XXXXX NALC HBP 8/10/12 \$626.81

\*\* END OF REPORT \*\*

### Unmatched EFTs \> 14 Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A warning bulletin is sent to the RCDPE AUDIT Mail Group for unmatched EFTs greater than 14 days.

From: POSTMASTER@XXXXX.MED.VA.GOV

Sent: Thursday, July 31, 2014 6:01 AM

To: "G.RCDPE AUDIT"@XXXXX.MED.VA.GOV

Subject: EDI LBOX-STA# 623-ACTION REQ-EFTs \> 14 days  
Importance: High

The following EFTs were received more than 14 days ago and have not yet been matched – or have been matched but not posted.

Total \# of EFTs - 4

Total Dollar Amount - \$87.99

DEPOSIT# PAYER NAME/TRACE# EFT DATE DEPOSIT AMT

XXXXXXXXX BCBS OKFEPDENTAL/ XXXXXXXXXXXXXX 4/11/14 \$32.00

XXXXXXXXX BCBS OKFEPDENTAL/ XXXXXXXXXXXXXX 5/17/14 \$8.00

XXXXXXXXX BCBS OKFEPDENTAL/ XXXXXXXXXXXXXX 6/3/14 \$32.00

XXXXXXXXX COMMUNITYCARE XX/XXXXXXX 7/11/14 \$15.99

\*\* END OF REPORT \*\*

### Suspense Entry Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A warning bulletin was previously sent to the RCDPE AUDIT Mail Group for Suspense Entries overdue for processing. This bulletin was removed with patch PRCA\*4.5\*439.

# Payments Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Daily activities related to processing ePayments are included in this section of the User’s Guide. It is organized by how the daily workflow should be processed – starting with checking e-mail and processing exceptions before proceeding to the ERA Worklist activities.

## Check Email

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 3rd Party EDI Lockbox software makes extensive use of e-mail bulletins to alert users about actions taken during the nightly processing of EFTs and ERAs received from payers. Check e-mail for these notifications first thing in the morning to help plan the workday. If a bulletin is received that states an ERA was rejected because no valid EEOBs were found for the site, contact the ePayments POC for assistance to ensure that no data is lost.

Starting with the Clerk’s AR Menu, the user must navigate through two screens to access the functionality that is contained in the ERA Worklist / Scratchpad:

Audit/Set up a New Accounts Receivable ...

New Bill Forms Print ...

Profile of Accounts Receivable

Update Accounts Receivable ...

Adjustment to Accounts Receivable ...

Report Menu for Accounts Receivable ...

Follow-up Letter Menu ...

Establish/Edit Old Bills ...

Transaction Profile

TPJI Third Party Joint Inquiry

Account Management ...

Agent Cashier Menu ...

EDI Lockbox ...

FMS Utilities Menu ...

Refund Review and Approve

Select Clerk's AR Menu Option:

Select Clerk's AR Menu Option: edi Lockbox (ePayments)

EXC EDI Lockbox 3rd Party Exceptions

WL ERA Worklist

APAR Auto-Post Awaiting Resolution

MA Automatic Match EFTs to ERAs

MCR EEOB Move/Copy/Remove

MM EFT Manual Match

OEFT Unposted EFT Override

DUP Duplicate ERA Worklist

REFT Remove Duplicate EFT Deposits

REM Remove ERA from Active Worklist

REP EDI Lockbox Reports Menu ...

UN Unmatch An ERA

UP Update ERA Posted Using Paper EOB

ZB Mark 0-Balance EFT Matched

IDP Identify Payers

UBD Remove Unbalanced Deposit Flag

Select EDI Lockbox (ePayments) Option:

## Exception Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before starting to process anything on the ERA Worklist, check for exceptions by using the option EXC EDI Lockbox 3rd Party Exceptions located on the EDI Lockbox (ePayments) Menu. Any ERA or EEOB that cannot be automatically and completely matched into both the VistA AR and IB packages will end up on the Exception Report. This includes ERAs with recognized errors that prevent a clean update to automatically occur.

Records can be viewed, and various options are provided to reconcile the exceptions and move these to the ERA Worklist for processing. An ERA cannot be processed in the ERA Worklist if an exception exists on the ERA.

5.  The ERA Worklist will display “x” in front of the ERA number to indicate an exception exists.

ERA List - Worklist Dec 12, 2014@14:18:37 Page: 4 of 7

SELECTED MATCH STATUS: BOTH POST STATUS : BOTH

DATE RANGE: 11/22/14-12/12/14 AUTO-POSTING : BOTH

ALL PAYERS PHARMACY/MEDICAL: BOTH

\# ERA \# Trace#

\+ PAYER NAME/MATCH STATUS & DATE ERA PAID DT TOT AMT PAID DT REC'D

11 XXXXX XXXXXXXXXX

12/10/14 0.00 12/10/14

AETNA APPROX \# EEOBs: 2

UNMATCHED N/A

Details for processing the exceptions are included below.

There are two types of exceptions explained below:

1.  Transmission Exceptions
2.  Data Exceptions
6.  Exceptions should be worked daily and before the scratchpad is created for the ERA.

### Transmission Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Transmission Exceptions occur when there was a problem storing ERA EEOB data.

Here are three examples of when a transmission error may occur:

1.  All sequences for an ERA that was sent in multiple messages were not received at the site.

For example, AR cannot process these until ALL messages in the batch are received. The exception list contains only four (4) of five (5) messages. The user should wait for the fifth message. If the message is not received in 24 hours, contact EPS at REDACTED to enter a remedy ticket and request a re-transmission.

2.  An ERA transmission did not fully complete the permanent update process on a previous date, and remains in the file, partially processed. How is this corrected? Enter a remedy ticket, as this is the result of a system problem. Once the problem has been resolved, use File Message to process the ERA. However, if the problem is severe and cannot be resolved, the user will be instructed to use DELETE MESSAGE to permanently remove the message from the list.
3.  An ERA cannot identify any claims on the transmission as valid at the user station. In Version one (1), this information was sent to the sites via e-mail messages. The information contained in the e-mail messages is now stored under the Transmission Exceptions until filed and corrected / saved or deleted.

EEOB TRANSMISSION EXCEPTIONS Jul 01, 2010@10:41:30 Page: 1 of 1

ERA/EEOB MESSAGES WITH EXCEPTION CONDITIONS

\# Message ID Msg Typ Date Received Mail Msg \#

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1 XXXXXXX ERA MAR 05, 2007@18:41 XXXXXXX

EXCEPTION: NO VALID CLAIMS

Payer Name: IBinsurance Company One

Payer ID: XXXXXXXXXX

Trace \#: XXXXXXXXXXX

Date Paid: 03/02/2007 Total Amt Paid: 22.39

\*XXXKXXXXXXX

Enter ?? for more actions

View/Print Message Delete Message Exit

File Message TPJI

Select Action: Quit//

#### Processing Actions for Transmission Exceptions

Enter ?? for more actions

View/Print Message Delete Message Exit

File Message TPJI

Select Action: Quit//

List Manager options are used to complete the transmission exceptions. Each option is explained in detail below.

- View / Print Message – Used to print or view the formatted version of the message and optionally includes the actual text (raw data) received in the message.
- File Message – Used to attempt to re-file a message. This could be used if the message was not completely stored in the permanent ELECTRONIC REMITTANCE ADVICE file. When the user selects a message to re-file, the system checks the content of the message and tries to automatically file the data in VistA.
- If successful, the exception is removed. A bulletin is sent to the RCDPE PAYMENTS mail group reporting the attempt to re-file the message.
- If this action is used with a NO VALID CLAIMS transmission, the exception will be moved to the data transmissions screen where the claim numbers can be edited and the EEOBs filed in IB.
- Delete Message – Used to remove the message from the exception list if the message cannot be re-filed into VistA automatically. This action removes the message permanently from the exception list and sends a bulletin to the RCDPE PAYMENTS Mail Group containing the text of the message received.

  The Delete Message action cannot be used if the ERA has a payment method of Automatic Clearing House (ACH). An error message will display.
7.  The Delete Message action is locked with the security key, RCDPE ERA EXCEPT.
- TPJI (Third Party Joint Inquiry) – This is a link to TPJI in case further analysis of the site’s receivables is required.

### Data Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data Exceptions may be filtered to view medical claims, pharmacy claims, CHAMPVA claims, or all, and by all payers or a range of payers.

DO YOU WANT TO SEE (T)RANSMISSION OR (D)ATA EXCEPTIONS?: T// DATA

(C)HAMPVA, (M)EDICAL, (P)HARMACY, OR (A)LL?: A// ALL

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: ALL//

A Data Exception occurs when AR cannot match the claim number on the EEOB with a claim number in AR.

An example of a Data Exception is provided below:

- An EEOB has encountered an error such as a typo or transposed bill number, the action called Edit Claim \# can be used to correct this error.

Sample Data Exception Report

LOCKBOX EEOB DATA EXCEPTIONS Oct 13, 2010@15:38:12 Page: 1 of 1

EEOB DETAIL DATA WITH EXCEPTION CONDITIONS

<span class="mark">INSURANCE CO.: ALL CHAMPVA/MEDICAL/PHARM/TRICARE: ALL</span>

\# Trace \# EOB Date

Insurance Co Name/ID Service Date

1 XXXXXXXX XX/XX/XX

IBinsurance Company One/XXXXXXXXX XX/XX/XX

Seq \#: 49 Bill: \*XXX-XXXXXXX Pt: IBpatient,One A Pd: 1.82

ECME \#: XXXXXXXXXXXX Release Date:

Comment: Pharmacy comment about prescription

\*\*Exception: VALID BILL NOT FOUND

Enter ?? for more actions

View/Print Message Edit Claim \# Exit

File EEOB in IB TPJI

Remove Exception Pharmacy Claim Comment

Select Action: Quit//

#### Processing Actions for Data Exceptions

Enter ?? for more actions

View/Print Message Edit Claim \# Exit

File EEOB in IB TPJI

Remove Exception Pharmacy Claim Comment

Select Action: Quit//

List Manager options are used to complete the data exceptions. Each option is explained in detail below.

- View / Print Message - Used to print or view the exception message and any detail on file for it.
- File EEOB in IB - Used to attempt to re-file the EEOB data detail in IB (Integrated Billing) if an exception occurred during a previous update attempt.
- Remove Exception - Used if there is no electronic way to resolve the exception condition. This action marks the ERA or EEOB detail record, so it no longer appears as an exception. A bulletin will be sent to report this action to the RCDPE PAYMENTS mail group. If an exception is removed, the EEOB will appear in the worklist as ‘not found in AR.’
- Edit Claim \# - Used to update the claim number to reflect the correct claim number to file in the EEOB. TPJI can be used to view the claim detail before changing the claim number. The system will also accept an entry that is not a valid claim number, which will cause money to go to suspense.

Select Action: Next Screen// ED Edit Claim \#

Select EDI LBox EEOB Data Exception(s): (96-99): 97

Selection \#: 97 XXXXXXX

Select A/R Bill this EEOB is actually paying on: SUSPENSE

THIS CLAIM WAS NOT FOUND IN YOUR AR. DO YOU WANT TO CONTINUE?: NO// YES

EEOB Filed.

PRESS RETURN TO CONTINUE

8.  \#1: The Edit Claim \# function REMOVES the old claim number from the ERA Worklist and REPLACES it with the new one. If this change is made in the Worklist, the original number remains on the EEOB and the new number also references the EEOB. It is cleaner to do it here than the Worklist if the error is simply that the wrong bill \# was reported paid.
9.  \#2: Once a data exception has been resolved, the system will re-evaluate the ERA to determine if it can be marked for Auto-Post. A message will display if the ERA was successfully Marked for Auto-Post, or the reason it was not successfully marked.
- TPJI (Third Party Joint Inquiry) – This is a link to TPJI in case further analysis of the site’s receivables is required.
- Pharmacy Claim Comment – Used to enter a one line comment for a non-released prescription. Only the most recent comment is stored and displayed.

### Non-Released Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An ERA for a non-released prescription automatically goes to the exception list because a bill is not created for a prescription until the prescription is released. VistA runs a nightly job to evaluate the ERAs that are on the exception list due to non-released prescriptions. If the prescription has been recently released, a bill exists, and the ERA has no more exception conditions, the nightly job removes the ERA from the exception list. Processing of the ERA continues as normal.

## Working the EEOB Scratchpad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB Scratchpad is a list of Electronic EOB (EEOB) detail records that were included on a selected electronic remittance advice (ERA). It allows for the creation of a receipt that will post each payment contained in each EEOB against the site's A/R, and send to FMS. To accomplish this, some manipulation of the payment data may be necessary. The EEOB Scratchpad contains the tools for performing these manipulations (i.e., distribute adjustments, split / edit a payment, etc.).

10. Negative Claim Balance rule is enforced. When adjusting, the claim balance cannot be less than zero dollars (collected / closed status).

Once the Work List (WL) ERA Worklist option above has been selected, the process begins with at least one question that determines the ERA(s) that is (are) available to be processed. If the user has not saved a preferred view, the questions associated with the Change View action will be asked.

11. See the section on the Change View action for details.

There is one question that will always display, regardless of the preferred view. The prompt asks if one wants to work with a date range selection:

- Date Range Selection:
- ALL
- RANGE

The initial list of the ERAs selected will then be presented:

Sample ERA List – Worklist (list manager worklist)

ERA List - Worklist Jul 22, 2010@17:37:06 Page: 1 of 3

SELECTED: MATCH STATUS: BOTH POST STATUS : UNPOSTED

DATE RANGE : NONE SELECTED AUTO-POSTED : BOTH

ALL PAYERS PHARMACY/MEDICAL: BOTH

\# ERA \# TRACE#

PAYER NAME/MATCH STATUS & DATE ERA PAID DT TOT AMT PAID DT REC'D

1 1 XXXXX

10/29/02 20.00 10/29/02

IBinsurance Company One APPROX \# EEOBs: 1

CHK MATCHED 7/21/2010 EFT RECEIPT STATUS: NOT ENTERED

2 XXXXXXXXXX TEST123

6/8/10 3456.78 6/8/10

IBinsurance Company Two APPROX \# EEOBs: 1

CHK MATCHED 7/21/2010 (CHECK PAYMENT CHOSEN)

3 XXXXXXXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

7/21/10 123.45 7/21/10

IBinsurance Company Three APPROX \# EEOBs: 1

CHK MATCHED 7/21/2010 (CHECK PAYMENT CHOSEN)

\+ \|'-' No scratchpad\|'x' EXC \|'A' autopost complete

Select ERA View/Print ERA Admin Cost Adj

Sort List Change View

Mark for Auto Post ERA Manual Match Exit

Select Action: Next Screen//

### ERA List – Worklist Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several List Managers options available on the ERA Worklist screen that provide greater capability to manage records at the ERA level.

| Action         | Description                                                                                                                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select ERA     | Used to select a specific ERA.                                                                                                                                                                                                         |
| Sort List      | Allows the user to sort the ERA worklist by multiple criteria; amount paid, payer name, ERA paid date, or date ERA received. Sorting the worklist by these criteria does not change the list of the individual EEOB’s within each ERA. |
| View/Print ERA | Used to display / print the summary ERA information.                                                                                                                                                                                   |
| Change View    | Used to customize the information displayed on the ERA worklist.                                                                                                                                                                       |
| Admin Cost Adj | Used to make Administrative Cost Adjustments to a claim.                                                                                                                                                                               |

<span id="_Toc183424287" class="anchor"></span>Table 3: Scratch Pad

#### Sort List

To work more efficiently with ERAs, the user can select two different sort levels to identify the ERAs to be worked on first:

- First Level Sort: Amount Paid, Payer Name, ERA Paid Date, Date ERA Received.
- Second Level Sort: None, or any of the data elements listed in the First Level Sort (cannot use the same sort twice).

#### View / Print ERA

The View / Print ERA action is used to display and print the summary ERA information. If a data exception exists for the selected ERA, a warning message will display. The user must press enter to continue.

Select \#: (6-9): 9

> **WARNING:** Fix Transmission Exceptions first and then Data Exceptions

with the EXE EDI Lockbox 3rd Party Exceptions option which is located

on the EDI Lockbox (ePayments) Main Menu.

PRESS ENTER TO CONTINUE

The View / Print ERA action displays an AUTO-POST STATUS of UNPOSTED, PARTIAL, or COMPLETE at the ERA summary level and EEOB detail level.

#### Change View

The Change View action is used to customize the information displayed on the ERA worklist. After answering the questions, the system gives the user the option to “SAVE” the selections as a “preferred view.” If the user saves a preferred view, they will be prompted if they want to use that view in the future.

The answers are used to filter the worklist display to limit the entries that are included.

The following options are available as filters:

Select Action: Next Screen// C Change View

SELECT PARAMETERS FOR DISPLAYING THE LIST OF ERAs

(Z)ERO, (P)AYMENT, or (B)OTH: B//

ERA posting status: (U)NPOSTED, (P)OSTED, or (B)OTH: U//

DISPLAY (A)UTO-POSTING, (N)ON AUTO-POSTING, OR (B)OTH: B// OTH

(M)ARKED, (P)ARTIAL, (C)OMPLETE OR (A)LL: A// LL

ERA-EFT MATCH STATUS: (N)OT MATCHED, (M)ATCHED, or (B)OTH: B//

(M)EDICAL, (P)HARMACY, (T)RICARE, (C)HAMPVA or (A)LL: A//

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: A// LL

DO YOU WANT TO SAVE THIS AS YOUR PREFERRED VIEW (Y/N)? NO//

Select Parameters for Displaying the List of ERAs:

- Zero – Show only zero-dollar ERAs
- Payment – Show only ERAs with payments
- Both – Show both zero dollar and ERAs with payments

ERA Posting Status:

- UNPOSTED – ERA / Receipt has not been posted to FMS
- POSTED – ERA / Receipt has been posted to FMS

Auto-Posting Qualification:

- AUTO-POSTING – ERA meets criteria for auto-posting
- NON AUTO-POSTING – ERA does not meet criteria for auto-posting
- BOTH – All ERAs, regardless of criteria for auto-posting

Partial Posted and Marked for Auto-Post Status:

- Select MARKED to only see ERAs currently marked for auto-post
- Select PARTIAL to only see ERAs with a partial auto-post status
- Select COMPLETE to only see ERAs with a complete auto-post status
- Select ALL to see ERAs with any auto-post status

ERA-EFT Match Status:

- NOT MATCHED – ERA has not been matched with an EFT (automatically by nightly job) or ERA has not been matched with a paper check by user or ERA has not been matched with a Ø -payment by the user.
- MATCHED - ERA was matched with an EFT (automatically by nightly job) or ERA was matched with a paper check by user) or ERA was matched with a Ø-payment by user.
- BOTH – list both Not Matched and Matched ERAs.

Claim Type:

- MEDICAL – ERAs for Third Party Medical Claims
- PHARMACY – ERAs for Pharmacy Claims
- TRICARE – ERAs for Tricare Claims
- CHAMPVA – ERAs for CHAMPVA Claims
- All – ERAS for Third Party Medical Claims, Pharmacy Claims, Tricare Claims and CHAMPVA Claims

Payer Range Selection:

- ALL
- RANGE

#### Select ERA

The Select ERA action allows the user to select a specific ERA by number. If a user selects an ERA with one or more exceptions, the software will alert the user by displaying a warning that access is denied until all exceptions for that ERA are resolved.

Users now have the option to go to exceptions from the worklist.

ACCESS DENIED Scratchpad creation is not allowed when Exceptions exist. Fix Transmission Exceptions first and then Data Exceptions via the EXC EDI Lockbox 3rd Party Exceptions option which is located on the EDI Lockbox Main Menu.

Do you want to begin clearing Exceptions for this ERA (Y/N)? Y//

If the user selects Y, the user “jumps” to the exceptions list to begin clearing exceptions following the existing process. The user will return to the Worklist if the user opts to exit the exceptions process, or enters "N" to the original prompt, and does NOT want to begin clearing Exceptions.

If the user selects an ERA that does not have a scratch pad, three options display:

| Option            | Description                                                  |
|-------------------|--------------------------------------------------------------|
| Create Scratchpad | Used to create a scratchpad.                                 |
| View ERA Details  | Used to View / Print ERA; a scratchpad is not created.       |
| Exit              | Used to return to the worklist; a scratchpad is not created. |

<span id="_Toc183424288" class="anchor"></span>Table 4: EOB Line Item

The user will automatically be prompted to select the display order for payment information before continuing to the scratchpad screen.

Once the ERA is selected, if the payer has indicated a PAYMENT METHOD CODE on the ERA, it will be displayed here. This can be used as a guide as to how the payer has decided to send the payment for this ERA to the site.

Some examples are:

- CHK - indicates a paper check should be expected.
- NON - indicates an Ø-payment.
- ACH - indicates an EFT should be expected.
- FWT - indicates a federal wire transfer.

If the PAYMENT METHOD CODE indicates NON or CHK, and is a zero-payment ERA, respond YES to the next prompt to mark the ERA as MATCH-Ø-PAYMENT.

If matching a paper check with an ERA, enter the check \# and date of the check.

Sample ERA Worklist / Scratch Pad

ERA Worklist/Scratch Pad Jul 21, 2010@12:17:58 Page: 1 of 1

ERA Entry \#: XXXXXXXXXX Total Amt Pd: 123.45 Current View:

Payer Name/ID: IBinsurance Company One/XXXXXXXX NO SORT ORDER

PAPER CHECK \#: XXXX ALL EEOBs

1 EEOB Seq \# On ERA: X Net Payment Amt: 123.45

1.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One A/XXXX

Claim Bal: 0.00 Billed Amt: 0.00 Amt To Post: 123.45

Svc Dt: 6/1/00 COB: NO Rx Copay: UNKNOWN Means Tst: ??

Payment Amt: 123.45 Total Adjustments: 0.00 Net: 123.45

ECME \#: XXXXXXXXXXXX

Rx/Fill/Release Status: XXXXXXX/1/Released

DOS: 1/4/13

Enter ?? for more action

Split/Edit A Line Look At Receipt Mark for Auto Post

Distribute Adj Amts Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen//

The header of the ERA Worklist / Scratch Pad screen contains:

- The ERA Entry \#.
- The Name and ID number of the Payer.
- The Total Amount being Paid on the ERA (this will equal the dollar amount of the Electronic Funds Transfer or Paper Check received from the Payer).
- The EFT Trace \# or the number from the Paper.

Each EEOB line item equates to a line item on a paper EOB form. The advantage is that the information on the ERA Worklist / Scratch Pad will always be in the same location, regardless of Payer. HIPAA mandates standardization of the electronic transmissions.

<table>
<caption><p><span id="_Toc183424289" class="anchor"></span>Table 5: EFT</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EEOB Seq # on ERA</td>
<td><p>This shows the line item order as the payer sent it.</p>
<p>Remember, the Worklist can be sorted with Zero Payments First or Zero Payments Last, so the sequence number may not match the line item list on the far left of the screen.</p></td>
</tr>
<tr class="even">
<td>Net Payment Amt</td>
<td>The payment amount plus or minus the adjustment amount will equal the net payment amount for this claim number.</td>
</tr>
<tr class="odd">
<td>Claim #</td>
<td>The claims number associated with this payment. This may or may not be the correct claim number. Research each claim carefully to see the amount being paid is appropriate for the claim in AR. Test sites have identified Payer errors (typos) that could result in a payment being applied to the wrong claim if not corrected by using the Split / Edit A Line action. If the line item is marked (V), the system has already done a verification match between bill number and the patient’s name, date of service, and original billed amount.</td>
</tr>
<tr class="even">
<td>Patient/Last 4</td>
<td>The patient’s name and last four digits of the SSN. Used to help identify this payment is for the correct Claim.</td>
</tr>
<tr class="odd">
<td>Claim Balance</td>
<td>Current balance from AR.</td>
</tr>
<tr class="even">
<td>Billed Amt</td>
<td>Original billed amount from AR.</td>
</tr>
<tr class="odd">
<td>Amount to Post</td>
<td>The payment amount plus or minus the adjustment amount will equal the amount to post for this claim number.</td>
</tr>
<tr class="even">
<td>Service Date</td>
<td>Beginning Service Date for this Claim</td>
</tr>
<tr class="odd">
<td>COB</td>
<td>Coordination of Benefits information that indicates whether a secondary payer has been identified for this claim.</td>
</tr>
<tr class="even">
<td>Rx Copay</td>
<td>Current Rx Copay status of the patient.</td>
</tr>
<tr class="odd">
<td>Means Test</td>
<td>Indicates if this patient may be responsible for Means Test co-payments.</td>
</tr>
<tr class="even">
<td>Payment Amt</td>
<td>Amount of money paid for this claim on this ERA.</td>
</tr>
<tr class="odd">
<td>Total Adjustments</td>
<td>Net total of all adjustments for this line item.</td>
</tr>
<tr class="even">
<td>Net</td>
<td>The payment amount plus or minus the adjustment amount.</td>
</tr>
<tr class="odd">
<td>ECME #</td>
<td>ECME number generated when the NCPDP claim is submitted for a pharmacy prescription. This field only displays for a pharmacy claim.</td>
</tr>
<tr class="even">
<td>Rx/Fill/Release Status</td>
<td>The prescription number fill number and release status (released, non-released). This field only displays for a pharmacy claim.</td>
</tr>
<tr class="odd">
<td>DOS</td>
<td>The date of service submitted on the NCPDP claim. This field only displays for a pharmacy claim.</td>
</tr>
</tbody>
</table>

<span id="_Toc183424289" class="anchor"></span>Table 5: EFT

If there are unposted payments (EFTs), the system may block access to the scratchpad. Based on the age of the oldest EFT, the system may generate a warning message, an error message, or no message.

| Type of Claim | Age of oldest EFT                                                   | Result                                                             |
|---------------|---------------------------------------------------------------------|--------------------------------------------------------------------|
| Medical       | Less than or equal to 14 calendar days.                             | No warning message or error message displays.                      |
| Medical       | More than 14 calendar days.                                         | A warning message displays. The user must press enter to continue. |
| Medical       | More than the number of calendar days specified in site parameters. | An error message displays. The user is not allowed to continue.    |
| Pharmacy      | Less than or equal to 21 calendar days.                             | No warning message or error message displays.                      |
| Pharmacy      | More than 21 calendar days.                                         | A warning message displays. The user must press enter to continue. |
| Pharmacy      | More than the number of calendar days specified in site parameters. | An error message displays. The user is not allowed to continue.    |

<span id="_Toc183424290" class="anchor"></span>Table 6: Worklist Actions

The warning messages and error messages display the trace numbers of the older EFTs to allow the users to research and resolve the problem. If a posting override exists, the warning messages and error messages are suppressed.

12. See the section on posting overrides for more information.

### Worklist Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several actions available on the ERA Worklist / Scratchpad that can assist a user to ensure that the correct payment is being applied to the correct claim.

<table>
<caption><p><span id="_Toc183424291" class="anchor"></span>Table 7: Research Menu</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Split/Edit a Line</td>
<td><p>Used to split a payment or adjustment between two or more bills (if the payer has combined payments) or to correct the claim # associated with a payment (if the payer has reported the payment for the wrong bill).</p>
<p>The automatic update of EEOB information to reflect the split / edit of claims will occur at receipt creation in the PRCA nightly auto-post job (for APAR) or at receipt creation in the ERA Worklist.</p>
<ol start="13">
<li><p>This action is not available for an auto-posted ERA.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Distribute Adj Amt</td>
<td><p>Used to balance the receipt total to be posted with the total amount deposited if the payer sends a takeback within the ERA.</p>
<ol start="14">
<li><p>This action now allows adjustments to lines marked as ‘Claim not found in AR.’</p></li>
<li><p>This action is not available for an auto-posted ERA.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Refresh Scratch Pad</td>
<td><p>Restores the scratch pad record to the original lines extracted from the ERA. All previous actions (splits / edits / comments) that were performed will be deleted and must be re-entered.</p>
<ol start="16">
<li><p>This action is not available for an auto-posted ERA.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Research Menu</td>
<td>Link to all the necessary AR functions / processes such as TPJI, needed to process ERAs. These can each still be accessed through regular AR menu options.</td>
</tr>
<tr class="odd">
<td>Look at Receipt</td>
<td><p>Compiles the payments in the ERA Worklist / Scratch Pad and displays the lines that will be entered on a receipt.</p>
<ol start="17">
<li><p>This action is not available for unposted EEOBs that are part of an auto-posted ERA. For auto-posted ERAs, only one receipt displays at once.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Review Line</td>
<td>Allows addition of comments or used as a bookmark on a specific line within an ERA in case processing was interrupted, thereby allowing the user to more easily resume where the user left off. This option must be turned ‘on’ each time the user enters the ERA to enter or view comments.</td>
</tr>
<tr class="odd">
<td>Verify</td>
<td><p>Provides the functionality to identify and manually mark EEOBs as verified.</p>
<ol start="18">
<li><p>This action is not available for an auto-posted ERA.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Change View</td>
<td>Used to customize the information displayed on the ERA worklist.</td>
</tr>
<tr class="odd">
<td>Mark for Auto Post</td>
<td><p>Option used to indicate the ERA is ready for the software to auto post the ERA during the next nightly process.</p>
<p>This is locked with the security key “RCDPEPP.”</p></td>
</tr>
<tr class="even">
<td>View/Print ERA</td>
<td>Used to view / print the entire formatted ERA, with or without the EEOB detail, and with or without Auto-Post and Match Status audit information.</td>
</tr>
<tr class="odd">
<td>Receipt Processing</td>
<td><p>Option that allows the user to process a receipt.</p>
<p>This is locked with the security key “RCDPEPP.”</p></td>
</tr>
<tr class="even">
<td>EXIT</td>
<td>Option that allows the user to exit the ERA Worklist / Scratchpad.</td>
</tr>
</tbody>
</table>

<span id="_Toc183424291" class="anchor"></span>Table 7: Research Menu

19. The system is modified to remove case sensitivity when comparing Trace \#s while manually matching an ERA / EFT.

#### Split / Edit a Line

Sometimes Payers combine payments for two or more claims onto one claim. This action is used to split the payment to the appropriate claim. It can also be used to correct an incorrect claim number.

ERA Worklist/Scratch Pad Oct 07, 2003@16:55:39 Page: 2 of 3

ERA Entry \#: XX Total Amt Pd: 1165.99 Current View:

Payer Name/ID: Aetna/US Healthcare/XXXXXXXXXX NO SORT ORDER

PAPER CHECK \#: XXXXX-XXXXXXXX ALL EEOBs

\+

3 EEOB Seq \# On ERA: X Net Payment Amt: 812.00

3.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/XXXX

Claim Bal: 14850.54 Billed Amt: 14850.54 Amt To Post: 812.00

Svc Dt: 12/12/02 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 812.00 Total Adjustments: 0.00 Net: 812.00

4 EEOB Seq \# On ERA: X Net Payment Amt: 343.99

4.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/XXXX

Claim Bal: 100.00 Billed Amt: 100.00 Amt To Post: 343.99

Svc Dt: 1/22/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 343.99 Total Adjustments: 0.00 Net: 343.99

Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

View/Print EEOB Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen//

This example shows how to Split / Edit Line item \#4 to post the payment correctly. This action takes place after reviewing the EEOB detailed data to confirm how the payment should be applied.

Select Action: Next Screen// Split/Edit A Line

SELECT THE ENTRY THAT HAS A LINE YOU NEED TO SPLIT/EDIT

Select EEOB Line: (3-4): 4

4.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/XXXX

Claim Bal: 100.00 Billed Amt: 1719.92 Amt To Post: 343.99

Svc Dt: 1/22/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 343.99 Total Adjustments: 0.00 Net: 343.99

CLAIM \#: KXXXXXX// \>\>Current claim balance is: 100.00

PAYMENT AMOUNT TO APPLY TO THIS CLAIM: 343.99// 100.00

RECEIPT LINE COMMENT: SPLIT PAYMENT REMAINDER APPLIED TO KXXXXXX

CLAIM \#: KXXXXXX \>\>Current claim balance is: 2341.39

PAYMENT AMOUNT TO APPLY TO THIS CLAIM: 243.99// \<RET\>

RECEIPT LINE COMMENT: SPLIT PAYMENT - ORIG APPLIED TO KXXXXXX

Apply the correct payment amount to the correct claim number(s) until all the funds are applied.

Claim \# Payment Amount Adjustment Amt Net Amount

1 KXXXXXX 100.00 0.00 100.00

SPLIT PAYMENT REMAINDER APPLIED TO KXXXXXX

2 KXXXXXX 243.99 0.00 243.99

SPLIT PAYMENT - ORIG APPLIED TO KXXXXXX

============== ============== ===========

TOTALS: 343.99 0.00 343.99

Enter ?? for more actions…………………………………………………………………………………………………………

File New Lines Edit Lines Split Exit

Select Action:Quit// File New Lines

Edit Line Split if the information is not correct. File the new lines to save this information. *Exiting without filing will mean all changes are discarded.*

4 EEOB Seq \# On ERA: 4 Net Payment Amt: 343.99

4.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/ XXXX

Claim Bal: 100.00 Billed Amt: 1719.92 Amt To Post: 100.00

Svc Dt: 1/22/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 100.00 Total Adjustments: 0.00 Net: 100.00

Receipt Comment: SPLIT PAYMENT REMAINDER APPLIED TO KXXXXXX

4.002 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/XXXX

Claim Bal: 2341.39 Billed Amt: 2341.39 Amt To Post: 243.99

Svc Dt: 1/22/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 243.99 Total Adjustments: 0.00 Net: 243.99

Receipt Comment: SPLIT PAYMENT - ORIG APPLIED TO KXXXXXX

Sub lines are created for each EEOB line item to allow the payment amounts to be split and distributed as necessary. The sub lines are numbered in increments of .001. In this example, the sub-lines are numbered 4.001 and 4.002.

Reason text (i.e., Comment) is mandatory when leaving a portion of the payment in suspense.

COMMENT: ??

Enter a code from the list.

Select one of the following:

1 Collected/Closed

2 Cancelled

3 Returned refund

4 Overpayment

5 Inactive bill

6 Duplicate payment

7 Policy termed

8 Service connected

9 Other

The scratchpad screen displays the following if a receipt line comment has been added.

2.002 Claim \#: SUPENSE Patient/Last 4: ??

\*\*\*CLAIM NOT FOUND IN YOUR AR \*\*\*

Payment Amt: 160.00 Total Adjustments: 0.00 Net: 160.00

Receipt: XXXXXXXXXX

Receipt Comment: OVERPAYMENT

Added By: EMPLOYEE,ONE

Date/Time Added: July 20 2017@10:00:00

#### Distribute Adj Amt

There are circumstances where payers determine they have ‘overpaid’ a VA facility on a claim. There are two ways that Payers process transactions to recoup overpayments:

- Process a retraction of funds on a subsequent payment (take back).
- Issue a negative payment adjustment (clipped payment).

Here are two examples showing how a ‘clipped payment’ and a ‘take back’ will appear on an ERA.

- Example One: Take Back

VA billed Payer \$200.00 for care. Payer issued a payment for \$160.00 (80% of the billed amount). A Payer review shows policy should have paid at 60% so the actual payment should have been \$120.00.

3 EEOB Seq \# On ERA: 3 Net Payment Amt: -40.00

3.001 Claim \#: KXXXXXX Patient/Last 4: VA Patient One/XXXX

Claim Bal: 0.00 Billed Amt: 200.00 Amt To Post: -40.00

Svc Dt: 12/12/02 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 120.00 Total Adjustments: -160.00 Net: -40.00

In this example, the Payer sent an EEOB with both the new payment amount (\$120.00) and the retraction of the incorrect payment (-\$160.00). This resulted in the Net Payment amount of a negative number (-\$40.00) being recorded on this EEOB. Use the action called Distribute Adj Amts on the ERA Worklist to decrease the payments received on one or more of the other claims within the ERA.

20. See the Distributed Adjustments section of this guide for instructions on how to perform this action.
- Example Two: Clipped Payment

Payer determines an overpayment of \$14.00 was made to VA. Rather than process a negative transaction adjustment on as specific VA claim, they process a non-specific retraction.

1 EEOB Seq \# On ERA: ADJ1 Net Payment Amt: -14.00

1.001\*\*\*ADJUSTMENT AT ERA LEVEL

Payment Amt: 0.00 Total Adjustments: -14.00 Net: -14.00

ADJUSTMENTS:

1\. Non-specific retraction (ref# SXXXX): -14.00

The EEOB line shows an adjustment at an ERA level. This is because the Payer did not provide a VA claim number. The Payment Amount will show as \$0.00 and the adjustment amount -\$14.00. The net payment amount is -\$14.00.

The Ref \# is provided by the Payer as a way for both the user and the payer to identify and track this transaction.

The Adjustment comments show this is a non-specific retraction with no reference to a claim number. Again, use the action called Distribute Adj Amts on the ERA Worklist to decrease the payments received on one or more of the other claims within the ERA.

Sometimes Payers will process non-specific payments to VA.

2 EEOB Seq \# On ERA: ADJ2 Net Payment Amt: 24.00

2.001\*\*\*ADJUSTMENT AT ERA LEVEL

Payment Amt: 0.00 Total Adjustments: 24.00 Net: 24.00

ADJUSTMENTS:

1\. Non-specific payment (ref# AXXXX): 24.00

ERA level adjustments do not reference individual claims. The payment amount = Ø, the total adjustments is a positive number (\$24.00) and with a net payment for the amount adjusted (negative for a retraction / positive for an additional payment).

The Ref \# is provided by the Payer as a way for both the user and the payer to identify and track this transaction. This non-specific payment will be placed in the facility’s suspense account when the receipt is processed for this ERA.

Use the *Distribute Adj Amt* action to resolve takebacks and clipped payments.

Select Action: Next Screen// Distribute Adj Amts

SELECT A LINE THAT NEEDS AN ADJUSTMENT AMOUNT DISTRIBUTED: 1.001// \<RET\>

LINE \#: 1.001 AMOUNTS NEEDED TO DISTRIBUTE: -14.00

SELECT A LINE TO DISTRIBUTE THE ADJUSTMENT AMOUNT TO: ?

THE FOLLOWING LINE(S) HAVE A NET PAYMENT THAT CAN BE USED TO OFFSET THE

NEGATIVE NET PAYMENT FOR LINE 1.001 (-14.00):

3.001 812.00 On hold exists

4.001 243.99

2.001 24.00

SELECT A LINE TO DISTRIBUTE THE ADJUSTMENT AMOUNT TO:

In this example, line item 1.001 has a negative amount that needs to be distributed to a payment. Entering a question mark displays the lines on the ERA that have a positive payment that can be used to offset the negative net payment.

SELECT A LINE TO DISTRIBUTE THE ADJUSTMENT AMOUNT TO: 4.001

LINE \#: 4.001 LINE BALANCE: 243.99

ADJUSTMENT AMOUNT TO DISTRIBUTE: 14.00// \<RET\>

DECREASE ADJ COMMENT (1-60 CHARACTERS):

\> RETRACTED FOR ERA ADJ \#1 Ref: SXXXX

Replace \<RET\>

An adjustment amount can be distributed against several lines if necessary. The user does not have to perform an adjustment for the take back amount. A DECREASE ADJUSTMENT will be automatically performed for the decreased amount when the user processes the receipt for posting if the Worklist is used to create the receipt. A standard comment will be used will be used when the DECREASE ADJUSTMENT is sent unless a new comment is entered. (It is up to each station to determine if the default comment is used or a more detailed comment needs to be entered by the user).

Distribute Adj Amts – Warning Message

SELECT A LINE THAT NEEDS AN ADJUSTMENT AMOUNT DISTRIBUTED: 4.001//

LINE \#: 4.001 AMOUNT NEEDED TO DISTRIBUTE: -6.55

SELECT A LINE TO DISTRIBUTE THE ADJUSTMENT AMOUNT TO: 7

THIS IS NOT AN ACTIVE BILL !

CANNOT PERFORM DISTRIBUTION TO THIS CLAIM

An adjustment cannot be made against a line within the ERA that represents a closed claim (claim balance equals zero dollars). A warning message will be generated if these types of lines are selected and the user will be forced to select another line.

1 EEOB Seq \# On ERA: ADJ1 Net Payment Amt: 0.00

1.001\*\*\*ADJUSTMENT AT ERA LEVEL

Payment Amt: 0.00 Total Adjustments: 0.00 Net: 0.00

ADJUSTMENTS:

1\. Non-specific retraction (ref# SXXXX): -14.00

2\. Adjustment distribution to balance receipt: 14.00

RETRACTED FUNDS DEDUCTED FROM OTHER PAYMENT ON THIS ERA

4.001 Claim \#: KXXXXXX Patient/Last 4: VA Patient One/1234

Claim Bal: 2341.39 Billed Amt: 2341.39 Amt To Post: 229.99

Svc Dt: 1/22/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 243.99 Total Adjustments: -14.00 Net: 229.99

ADJUSTMENTS:

1\. Distributed adj dec for retraction SXXXX: -14

RETRACTED FOR ERA ADJ \#1 Ref: S1234

An adjustment record is then displayed attached to BOTH lines selected, indicating the action that was taken. The negative net payment line will have its net amount automatically increased by the amount selected and show a Net Payment Amount of zero. The line with the positive net payment data will be automatically decreased by this same amount to balance the amount of the deposit / check with the amount being posted. The Total Adjustments field shows the amount adjusted, while the Amount to Post and Net show the new payment amount.

#### View / Print EEOB and View / Print ERA

These Worklist actions are used to display / print the detail received from a Payer. Where the View / Print EEOB will only show the information for one line on the ERA, the View / Print ERA will show detailed information on each EEOB line for the entire ERA. Displayed below is a sample of the EEOB information sent by Payers.

ePayments ERA/EEOB Data Oct 15, 2018@07:13:22 Page: 1 of 3\_\_\_\_

%KXXXXXX CASE,ONE KXXXX DOB: REDACTED Subsc ID: XXXXXXXXX

Svc Date: 05/24/2007 Orig Amt: 67.27 ERA#: XXXXX

\*\* ERA SUMMARY DATA \*\*

ERA#: XXXXX TRACE#: XXXXXXXXXX

ERA DATE (PAYER): OCT 06, 2007 TOTAL AMT PD: 53.82

PAYER NAME/TIN: GREAT-WEST LIFE/XXXXXXXXXX

FILE DATE/TIME: OCT 09, 2007@18:24:08

EFT MATCH STATUS: MATCHED TO PAPER CHECK

ERA TYPE: ERA INDIVIDUAL EOB COUNT: 1

MAIL MESSAGE: XXXXXXX CHECK#: XXXXXXXXXX

DETAIL POST STATUS: POSTED EXPECTED PAYMENT METHOD CODE: CHK

\*\*\*\*\*\*\*\*\*\* ERA LEVEL ADJUSTMENTS \*\*\*\*\*\*\*\*\*\*

-- NONE --

\*\*\*\*\*\*\*\*\*\* EOB/835 INFORMATION (1 of 1) \*\*\*\*\*\*\*\*\*\*

Original Patient Name: PATIENT,ONE

EOB Type: NORMAL EOB EOB Paid Date: OCT 06, 2007

Svc From Date: 05/24/07 Svc to Date:

ICN: XXXXXXXXXX

Payer Name/TIN: GWH-CIGNA/XXXXXXXXXX

ERA \#: XXXXX Auto-Post Status:

Trace \#: XXXXXXXXXX

ECME \#: DOS: Rx/Fill/Release Status:

--------------------------------------------------------------------------------

CLAIM LEVEL PAY STATUS:

Total Submitted Charges : 67.27 Payer Covered Amount : 0.00

The example below shows the EEOB move / copy history.

EDI LOCKBOX EEOB DETAIL FROM WORKLIST 2/6/17 Page: 2

ERA NUMBER: XXX ERA DATE: Feb 06, 2017

INS COMPANY: TJB INSURANCE CO./ XXXXXXXXX

ERA TRACE \#: XXXXXXXXXXXXXXX

Payer Name : EPHARM INSURANCE

Payer Id : XXXXXXXXXXX

ICN : XXXXXXXXXXX

MOVE/COPY HISTORY

Date/Time of EEOB Copy: FEB 03, 2017@10:27:18

Copy of EEOB performed by: EMPLOYEE,ONE

Copy Justification Comments:

JUSTIFICATION

Other Claims: KXXXXXX

\*\*A/R CORRECTED PAYMENT DATA:

TOTAL AMT PD: 1200.00

\[suspense\]NO BILL 1000.00

xxx-K500009 200.00

#### Review Line

This worklist action is used to enter comments for an EEOB or as a bookmark when an EEOB was last worked on, so that the process be more easily resumed after an interruption. This option now remains active for the user, even if the user leaves the worklist. Additionally, each user comment entered is identified by the user, and the date / time that it was entered or edited. This will allow the user to edit the user’s own comments. Individual user preference determines whether this option is consistently on or off.

Select Action: Next Screen// re

1 Refresh Scratch Pad

2 Research Menu

3 Review Line

CHOOSE 1-3: 3 Review Line

REVIEW DATA DISPLAY IS CURRENTLY TURNED ON  
DO YOU WANT TO TURN IT OFF?: NO//

Select EEOB Line: (1-2): 1

REVIEW DATE/TIME: 8/12/04@13:13:18

COMMENT:

1\>this is a test

2\>

EDIT Option:

REVIEWED?: y YES

#### Verify

The system has been enhanced to automatically mark EEOBs as verified based on the first five digits of the patient’s last name, the claim number, the original bill amount, and the date of service. If all the criteria match in the EEOB and in the AR package, the system will place a (V) next to the EEOB to indicate that all the criteria was automatically verified.

For non-auto-post ERAs, where the system indicator has not been automatically updated, this worklist action is manually used to mark EEOBs as verified. In addition, for both auto-post and non-auto-post ERAs, the user can display / print the list of bills that were not automatically verified or contain discrepancies between the EEOB, and the bill record in VistA. The report will include data from the original bill (i.e., patient full name, date of service, last 4 digits of patient’s SSN, billed amount, and bill number) as well as data from the EEOB (i.e., patient full name, date of service, billed amount, and bill number).

21. All the data shown on the worklist for the EEOB is taken from the claim in VistA. The user must use the report below to identify the discrepancies for unverified EEOBs.

Sample of Autopost ERA Lines Discrepancies Report Output

EDI LBOX WORKLIST - AUTOPOST ERA LINES DISCREPANCIES REPORT 3/30/18 Page: 1

ERA \#: XXXXX TRACE \#: XXXXXXXXXXXXX

PAYER: AETNA ERA DT: 2/1/18

PATIENT NAME SUBMITTED AMT SVC DATE(S)

\* preceding data = data has discrepancy

================================================================================

EEOB Sequence \#(s) on the ERA:1 KXXXXXXX Unverified

VistA:\*Last, First Middle 186.66 7/10/00 – 7/10/00

ERA:\*Last, First Middle 186.66 7/10/00 – 7/10/00

### Change View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action is used to customize the information displayed on the ERA worklist scratchpad. After answering the questions, the system gives the user the option to “SAVE” the selections as a “preferred view.” If the user saves a preferred view, they will be prompted if they want to use that view in the future.

The answers are used to filter the scratchpad display to limit the entries that are included.

The following options are available as filters.

Select Action: Quit// c Change View

ORDER OF PAYMENT: N// O ORDER

DISPLAY FOR AUTO-POSTED ERAS: (U)NPOSTED EEOBs, (P)OSTED EEOBs, OR (A)LL: U// NP

OSTED

DO YOU WANT TO SAVE THIS AS YOUR PREFERRED VIEW (Y/N)? NO/

Order of Payment:

- N = NO ORDER – Does not list payments with respect to zero-payments.
- F = ZERO-PAYMENTS FIRST – Display all zero-payments first.
- L = ZERO-PAYMENTS LAST – Display all zero-payments last.

Auto-Posting Qualification:

- U = UNPOSTED – Only display unposted EEOBs.
- P = POSTED – Only display posted EEOBs.
- A = ALL – Display all EEOBS, both posted and unposted.

### Research Menu Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Research Menu provides access to functionality necessary to process ERAs. It can be accessed from the ERA Worklist / Scratch Pad to facilitate business process. Links to the following existing AR functions are available.

<table>
<caption><p><span id="_Toc183424292" class="anchor"></span>Table 8: EOBs</p></caption>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Full Account Profile</td>
<td>This option will display a full account profile of all bills for a debtor regardless of the status of the bill.</td>
</tr>
<tr class="even">
<td>TPJI</td>
<td>Comment History will display contact information if provided</td>
</tr>
<tr class="odd">
<td>Bill Comment Log</td>
<td>Allows user to document any necessary and pertinent information on a third-party bill.</td>
</tr>
<tr class="even">
<td>Re-establish Bill</td>
<td><p>Provides the capability to re-establish a bill for the specific site.</p>
<p>This is locked with the security key “RCDPEAR.”</p></td>
</tr>
<tr class="odd">
<td>View/Print EEOB</td>
<td>Used to display / print the detail received on the ERA for a selected line.</td>
</tr>
<tr class="even">
<td>Review Line</td>
<td>Bookmarks a specific line within an ERA in case processing was interrupted, thereby allowing the user to more easily resume where the user left off.</td>
</tr>
</tbody>
</table>

<span id="_Toc183424292" class="anchor"></span>Table 8: EOBs

#### Comment History Screen of TPJI

The Comments History screen of the Third-Party Joint Inquiry option displays contact data that will include payer name, and can include phone number, fax number, email address, and website address. Contact data that comes in from an ERA or MRA transaction will be distinguishable from manually entered comments by use of the program generated text, “ERA Payer Contact Information”.

Refer to example below:

Comment History Jul 07, 2011@18:27:38 Page: 1 of 1

KXXXXXX REDACTED C1547 DOB: XX/XX/XX Subsc ID: XXXXXXXXXX

AR Status: COLLECTED/CLOSED Orig Amt: 4.49 Balance Due: 0.00

XXXXXXX 01/17/07 2A FOLLOW-UP DT:

XXXXXXX 07/07/11 ERA Payer Contact Information FOLLOW-UP DT:

Payer Name: UNITEDHEALTHCARE

Contact Name: TEST PAYER 1

Phone Number: XXX-XXX-XXXX

Payer Name: MEDICARE (WNR)

Contact Name: MEDICARE TEST PAYER

Phone Number: XXX-XXX-XXXX

Email Address: REDACTED

XXXXXXX 10/04/19 999-XXXXXXX OFFSET \$50.00 FOLLOW-UP DT:

1ST PARTY BILL# 442-XXXXXXX COMPUTERIZED OFFSET \$50.00

FOR CLAIMS MATCHING DOS: 8/11/14 POSTMASTER

Enter ?? for more actions

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis AD Add Comment VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit

Select Action: Quit//

The Trace number and ERA number will display on the Bill Charges screen of TPJI for non-MRA ERAs. Refer to example below:

Bill Charges Nov 27, 2011@20:47:24 Page: 1 of 2

%KXXXXXX PATIENT1,REDACTED XXXXX DOB: REDACTED Subsc ID: SUBSC ID XXXXXX

03/11/02 - 03/11/02 ADMIT THRU DISCHARGE Orig Amt: 177.72

GX XXXXXXXXX

03 11 02 03 11 02 22 99213 123 17772 1 XXXXXXXXXX X

\>\> EOB/MRA Information (1 OF 1) l

EOB Type: NORMAL EOB l

ICN: XXXXXXXXXXXXX Patient Resp Amount: 128.92

Payer Name: AETNA US HEALTHCARE Total Allowed Amount: 0.00

EOB Date: Jan 07, 2004 Total Submitted Charges: 177.72

Svc From Dt: Svc To Dt:

Reported Payment Amt: 48.80

ERA \#: XX Auto-Post Status: Partial

Trace \#: XXXXXXXXXXXXXXX X

\+ \|% EEOB \| Enter ?? for more actions\|l

PR Bill Procedures CM Comment History AB Annual Benefits

CI Go to Claim Screen IR Insurance Reviews EL Patient Eligibility

HS Health Summary EX Exit

ED EDI Status AL Go to Active List

VI Insurance Company

Select Action: Next Screen//

### Example of Processing a Paper Check and ERA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAMC received a paper check from IBinsurance Company One, a payer who sends Electronic Remittance Advices (ERAs). Begin by selecting the ERA Worklist option.

Select EDI Lockbox (ePayments) Option: WL ERA Worklist

SELECT PARAMETERS FOR SELECTING AN ERA

ERA POSTING STATUS: UNPOSTED//

ERA-EFT MATCH STATUS: BOTH// NOT MATCHED

LIMIT THE SELECTION TO A DATE RANGE WHEN THE ERA WAS RECEIVED?: NO//

Select ELECTRONIC REMITTANCE ADVICE ENTRY: XXXXX-XXXXXXXX X XXXXX-XXXXXXXX 03-06-03 509.61 IBinsurance Company One UNMATCHED

The paper check (XXXXX-XXXXXXXX) matches the ERA Trace \# and the check amount received from the Payer.

No Worklist currently exists for this ERA.

Create one now.

NO WORKLIST SCRATCH PAD ENTRY EXISTS FOR THIS ERA

DO YOU WANT TO CREATE ONE NOW?: NO// YES

NO PAYMENT METHOD CODE REPORTED

THIS ERA DOES NOT HAVE A MATCHING EFT

ENTER THE NUMBER OF THE PAPER CHECK YOU RECEIVED FOR THIS ERA: XXXXX-XXXXXXXX// \<RET\>

DATE OF CHECK: 3/6/03// \<RET\> (MAR 06, 2003)

CHECK BANK/ROUTING \#: XXXXXX IBinsurance Company One

ERA \#6 (TRACE \#:XXXXX-XXXXXXXX) MATCHED TO PAPER CHECK XXXXX-XXXXXXXX

IS THIS CORRECT?: YES// \<RET\>

ORDER OF PAYMENTS: NO ORDER// L ZERO-PAYMENTS LAST

- Verify the paper check number is correct. The date on the check should match the date listed in VistA. If it does not match, correct the VistA date to match the paper check.
- Enter the Check Bank / Routing number as station policy dictates. Again, verify the information is correct.
- Select the order of the Payments. In this case, select L to sort the zero payment EEOBs to the bottom of the Worklist.

ERA Worklist/Scratch Pad Sep 11, 2010@13:24:20 Page: 1 of 2

ERA Entry \#: 5 Total Amt Pd: 509.61 Current View:

Payer Name/ID: IBinsurance Company One/XXXXXXXXXX NO SORT ORDER

PAPER CHECK \#: XXXXX-XXXXXXXX ALL EEOBs

1 EEOB Seq \# On ERA: 3 Net Payment Amt: 509.61

1.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/XXXX

Claim Bal: 559.61 Billed Amt: 559.61 Amt To Post: 509.61

Svc Dt: 2/4/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: NO

Payment Amt: 509.61 Total Adjustments: 0.00 Net: 509.61

2 EEOB Seq \# On ERA: 1 Net Payment Amt: 0.00

2.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/XXXX

Claim Bal: 0.00 Billed Amt: 19.47 Amt To Post: 0.00

Svc Dt: 1/27/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: ??

Payment Amt: 0.00 Total Adjustments: 0.00 Net: 0.00

\+ Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

View/Print EEOB Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen// EOB View/Print EEOB

#### Process EEOB Line Items

- To process line item \#1, select the Research Menu action to access Third Party Joint Inquiry (TPJI) to confirm this payment is correct for this claim.
- The IB application is enhanced to display the Trace Number and ERA Number on the TPJI screen when viewing the EEOB.

Select Action: Next Screen// BC Bill Charges

DO YOU WANT ALL EEOB DETAILS?: NO// YES

\>\> EOB/MRA Information (1 OF 1)

EOB Type: NORMAL EOB

ICN: XXXXXXXXXXXX Patient Resp Amount: 50.00

Payer Name: IBinsurance Company One Total Allowed Amount: 0.00

EOB Date: Mar 06, 2003 Total Submitted Charges: 559.61

Reported Payment Amt: 509.61

Bill \#: XXX-KXXXXXX

Adjustment Group Code: XX

Adjustment Reason Code: 3

Adjustment Amount: 50.00

Quantity: 0

Reason Code Text: Co-payment Amount

The user can view the EEOB details without going back to the worklist by selecting Bill Charges (BC) from within TPJI to view the EEOB Details for this claim. Scrolling down to the bottom of the EEOB information shows the Payer adjusted this payment by \$50.00 for the patient’s insurance co-payment amount.

#### Create Receipt

After all the EEOB lines have been reviewed, verified as correct, and adjusted appropriately, it is time to create the receipt for these payments. Select Look at Receipt from the ERA Worklist / Scratch Pad screen.

ERA WORKLIST PREVIEW RECEIPT Oct 07, 2003@15:09:36 Page: 1 of 1

ERA Entry \#: 6 Total Amt Pd: 509.61

Payer Name/ID: IBinsurance Company One/XXXXXXXXXX

PAPER CHECK \#: XXXXX-XXXXXXXX

LINE \# ACCOUNT AMOUNT

PAYMENTS (LINES FOR RECEIPT):

2.001 XXX-KXXXXXX 509.61

ZERO DOLLAR PAYMENTS:

1.001 XXX-KXXXXXX 0.00

3.001 XXX-KXXXXXX 0.00

Enter ?? for more actions………………………………………………………………………………………………………….

Print Receipt Preview Create Receipt Exit

Select Action: Quit//

The preview screen is divided into two sections. The top contains the line items, and payment information. The bottom section lists all the zero-dollar payments. Zero-dollar payments can be worked using AR options in the research menu from within the Worklist.

The Create Receipt action will create the receipt for lines on the ERA that contain payments, and those lines used to offset any negative payments on this ERA. The ERA Worklist can no longer be used to adjust any of the line items once the receipt is created.

THIS ACTION WILL CREATE THE RECEIPT FOR THIS ERA . ONCE THE RECEIPT IS

CREATED HERE, NO MORE AUTOMATIC ADJUSTMENTS MAY BE MADE FOR THIS ERA.

ARE YOU SURE YOU ARE READY TO CREATE THIS RECEIPT?: NO// YES

Select AR DEPOSIT TICKET \#: XXXXXX 03-10-03 IBpatient,One A

\$0.00 OPEN

ARE YOU SURE YOU WANT TO USE THIS DEPOSIT?: NO// YES

RECEIPT EXXXXXXXX HAS BEEN CREATED FOR THIS ERA

DO YOU WANT TO GO TO RECEIPT PROCESSING NOW? YES// \<RET\>

Processing receipts for paper checks requires entry of an AR Deposit Ticket \#. Contact the Agent Cashier for this number. The system will automatically generate a receipt number for this payment. All 3<sup>rd</sup> Party EDI Lockbox receipts will begin with the letter ‘E.’

22. It is important to note that every ERA is assigned its own receipt number. If four ERAs are processed on a given day, then there will be four ‘E’ receipts – one for each ERA. The system assigns the electronic receipt number based on the date and the last two digits are a combination of numbers or letters.

In the example below, the receipt was created on October 7, 2003, and was the first batch created for that day (00).

Receipt History

Receipt Profile Oct 07, 2003@15:14:52 Page: 1 of 1

Receipt \#: EXXXXXXXX Type of Payment: CHECK/MO PAYMENT

Deposit \#: XXXXXX ERA \#: 6 Receipt Status: OPEN

ERA \#: XXXXXXXXXX ERA TTL: xxxxxx.xx FMS Document: NOT SENT

EFT \#: XXXXXXXXXX EFT TTL: xxxxxx.xx FMS Doc Status: NOT ENTERED

\# Account Pay Date By Pay Amt Proc Amt

1 XXX-KXXXXXX 10/07/03 EG 509.61 0.00

-------- --------

TOTAL DOLLARS FOR RECEIPT 509.61 0.00

Opened By: IBclerk,One Date/Time Opened: Oct 7, 2003

Last Edit By: Date/Time Last Edit:

Processed By: Date/Time Processed:

Enter ?? for more actions………………………………………………………………………………………………………….

NP New Payment AP Account Profile PR Process Receipt

EP Edit Payment RR Reprint Receipt 21 (215 Report)

CP Cancel Payment WL Worklist (ERA) EA Exit Action

MP Move Payment CU Customize CR Entered Online

ER Edit Receipt

Select Action: Quit//

The Receipt Profile screen is the same screen used when the option Receipt Processing is selected. All the payment line items automatically transfer to this screen. No additional data entry is required to input these claim numbers and payment amounts. Process this receipt as normal to complete processing a Paper Check and ERA.

The following condition must be met before the receipt can be fully processed to FMS:

- The total on the receipt must be equal to the total reported on the ERA.

When the above condition is met, select the PROCESS RECEIPT action. The system will:

- Generate the decrease adjustment for any distributed adjustments made to the payments on the Worklist.
- Add any related bill comments to the Bill record in AR.

If the receipt passes the normal edits for posting, the system will post payments to the AR and then generate and transmit the appropriate CR document to FMS for these payments.

### Example of Processing a Matched ERA and EFT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAMC received an Electronic Funds Transfer (EFT) from IBinsurance Company One, a payer who sends both EFTS and ERAs.

Begin by selecting the ERA Worklist option.

Select EDI Lockbox (ePayments) Option: WL ERA Worklist

DO YOU WANT A (L)IST OF ERAs OR A (S)PECIFIC ONE?: LIST//

LIMIT THE SELECTION TO A DATE RANGE WHEN THE ERA WAS RECEIVED?: NO//

The EFT payment was automatically matched with the ERA during the AR nightly job. The user can select a specific payer by selecting Range, or can view all payers by selecting All. All is the default selection.

Select ELECTRONIC REMITTANCE ADVICE ENTRY: 25 XXXXX-XXXXXXXX 03-10-03 79.55 IBinsurance Company One MATCHED

NO WORKLIST SCRATCH PAD ENTRY EXISTS FOR THIS ERA

(C)reate scratchpad, (V)iew ERA details or (E)xit:

NO PAYMENT METHOD CODE REPORTED

ORDER OF PAYMENTS: NO ORDER//

In this example, the user selected ERA \#25 after viewing the worklist. The EFT Trace \# XXXXX-XXXXXXXX was received from the Payer.

23. No check information is required. The EFT payment was already deposited into US Treasury, account MCCR RSC 528704/8NZZ for the VA.

If no scratchpad entry currently exists for this ERA, create one now.

ERA Worklist/Scratch Pad Oct 07, 2003@15:52:17 Page: 1 of 2

ERA Entry \#: 25 Total Amt Pd: 79.55 Current View:

Payer Name/ID: IBinsurance Company One/XXXXXXXXXX NO SORT ORDER

EFT \#/TRACE \#: X/XXXXX-XXXXXXXX ALL EEOBs

1 EEOB Seq \# On ERA: 1 Net Payment Amt: 47.26

1.001 Claim \#: KXXXXXX Patient/Last 4:IBpatient,One/XXXX

Claim Bal: 236.31 Billed Amt: 236.31 Amt To Post: 47.26

Svc Dt: 1/15/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: NO

Payment Amt: 47.26 Total Adjustments: 0.00 Net: 47.26

2 EEOB Seq \# On ERA: X Net Payment Amt: 32.29

2.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/XXXX

Claim Bal: 161.46 Billed Amt: 161.46 Amt To Post: 32.29

Svc Dt: 7/26/02 COB: NO Rx Copay: NON-EXEMPT Means Tst: NO

Payment Amt: 32.29 Total Adjustments: 0.00 Net: 32.29

Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

View/Print EEOB Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Quit//

The header of the ERA Worklist / Scratch Pad screen shows the EFT \# / Trace \# instead of the number from the paper check.

Processing of an EFT / ERA is no different than processing an ERA and Paper Check. Perform the necessary reviews and processing for each claim.

#### Create Receipt

After all the EEOB lines have been reviewed and processed, it is time to create the receipt for these payments. Select Look AT Receipt from the ERA Worklist / Scratch Pad screen.

ERA WORKLIST PREVIEW RECEIPT Oct 07, 2003@16:20:17 Page: 1 of 1

ERA Entry \#: XX Total Amt Pd: 79.55

EFT \#/TRACE \#: X/XXXXX-XXXXXXXX

Payer Name/ID: IBinsurance Company One/XXXXXXXXXX

LINE \# ACCOUNT AMOUNT

PAYMENTS (LINES FOR RECEIPT):

1.001 XXX-KXXXXXX 47.26

2.001 XXX-KXXXXXX 32.29

ZERO DOLLAR PAYMENTS:

3.001 XXX-KXXXXXX 0.00

Enter ?? for more actions

Print Receipt Preview Create Receipt Exit

Select Action: Quit//

The ‘look at’ screen is divided into two sections. The top contains the line items, and payment information. The bottom section lists all the zero-dollar payments. Zero-dollar payments can be “worked” using AR options or from within the Worklist.

The Create Receipt action will create the receipt for the lines on the ERA that contain payments, and those lines used to distribute negative payments on this ERA. The ERA Worklist can no longer be used to adjust any of the line items once the receipt is created.

THIS ACTION WILL CREATE THE RECEIPT FOR THIS ERA . ONCE THE RECEIPT IS

CREATED HERE, NO MORE AUTOMATIC ADJUSTMENTS MAY BE MADE FOR THIS ERA.

ARE YOU SURE YOU ARE READY TO CREATE THIS RECEIPT?: NO// YES

RECEIPT EXXXXXXXX HAS BEEN CREATED FOR THIS ERA

DO YOU WANT TO GO TO RECEIPT PROCESSING NOW? YES//

Processing receipts for EFTs does not require or allow the entry of an AR Deposit Ticket \#. Remember, the EFT payment was already deposited into US Treasury for the VA. As with the receipt for a paper check, the system will automatically generate a receipt number for this payment. All 3rd Party EDI Lockbox receipts will begin with the letter ‘E.’

24. It is important to note that every ERA is assigned its own receipt number. If four ERAs are processed on a given day, then there will be four ‘E’ receipts – one for each ERA.

ER Edit Receipt

Receipt Profile Oct 07, 2003@16:24:41 Page: 1 of 1

Receipt \#: EXXXXXXXX Type of Payment: EDI LOCKBOX

EFT Detail \#: 3 VETERAN ERA \#: XX Receipt Status: OPEN

ERA \#: xxxxxxxxxx ERA TTL: xxxxxx.xx FMS Document: NOT SENT

EFT \#: xxxxxxxxxx EFT TTL: xxxxxx.xx FMS Doc Status: NOT ENTERED

\# Account Pay Date By Pay Amt Proc Amt

1 XXX-KXXXXXX 10/07/03 EG 47.26 0.00

2 XXX-KXXXXXX 10/07/03 EG 32.29 0.00

-------- --------

TOTAL DOLLARS FOR RECEIPT 79.55 0.00

Receipt History

Opened By: IBclerk,One Date/Time Opened: MAR 10, 2003

Last Edit By: Date/Time Last Edit:

Processed By: Date/Time Processed:

Enter ?? for more actions………………………………………………………………………………………………………… .

NP New Payment AP Account Profile PR Process Receipt

EP Edit Payment RR Reprint Receipt 21 (215 Report)

CP Cancel Payment WL Worklist (ERA) EA Exit Action

MP Move Payment CU Customize CR Entered Online

ER Edit Receipt

Select Action: Quit// QUIT

The Receipt Profile screen is the same screen the user would see for Receipt Processing. Instead of a Deposit Ticket \#, the EFT Detail and ERA \# will display. The Type of Payment indicates EDI LOCKBOX. All the payment line items automatically transfer to this screen.

No additional data entry is required to input these claim numbers and payment amounts. Process the receipt as normal.

The following conditions must be met before the receipt can be fully processed to FMS:

- An ERA receipt cannot be processed if the EFT receipt for the EFT related to this ERA has not yet been recorded in FMS, and confirmed as ACCEPTED in VistA. Wait until the FMS document for the EFT deposit has reached this status in VistA before processing the ERA related to the EFT.
- If there is an error on the EFT where the checksum was determined to be invalid, the receipt cannot be processed until the EDI Lockbox checksum exception is cleared on the EFT transmission.
- If the total of the receipt is different from the total reported on the EFT, the receipt cannot be processed.
- A receipt for an ERA related to an EFT cannot have a deposit associated with it.

When the above conditions have been met, and the user selects PROCESS RECEIPT, the system will:

- Generate the decrease adjustments for any distributed adjustments made to the payments in the Worklist and add any related bill comments to the bills.
- If the receipt passes the normal edits for posting, it will post the payments to the A/R and will generate and transmit the appropriate TR document to FMS for EFT payments. The TR documents will transfer the payment amounts from the Fund 528704, Revenue Source Code 8NZZ account (where it was placed by the CR and generated when the EFT was recorded) into the correct General Ledger accounts for the claims on the ERA. A CR document is created and recorded in FMS for receipts that are processed using a paper check.

#### How to Process an EFT using a Paper EOB (when the ERA is Not Received)

It is important to process an EFT even if the ERA is unavailable. By processing the EFT, the funds are appropriately transferred to the appropriate revenue source codes, and the third-party payments are applied to the proper outstanding accounts receivables.

1.  Create a receipt using the receipt number of the EFT. A letter or number will need to be added to the end of the receipt. This process will create a good audit trail of the EFT. The EFT receipt number can be located by accessing the EFT Daily Activity Report (see Reports section).
179. Enter EDI LOCKBOX for the receipt payment type.
180. Select the corresponding EFT (To see a complete listing of EFTs, enter ‘??’).

Do not enter a deposit ticket. The Funds have already been deposited into the appropriate fund.

<span id="_Toc183424270" class="anchor"></span>Figure 4: Funds Receipt

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/005.png)

181. Manually enter each payment.
182. Complete the receipt processing function according to local policy.
25. The EFT will be removed from the EFT Unmatched Aging Report with this process; however, the Unapplied EFT Deposits Report will still display this EFT (A future enhancement will correct this issue).

## Auto-Posting Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA runs a nightly job to automatically post third-party medical claims by creating, and processing receipts. The system attempts to create and process receipts for claims that are candidates for auto-posting based on auto posting parameters.

### Medical Auto-Posting Candidates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A third-party medical claim is a candidate for auto-posting if the following conditions are met:

- Auto-posting is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The EEOB payer is not excluded from auto-posting in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The ERA does not have an exception.
- The ERA does not contain interest.
- The ERA does not contain an adjustment.
- The EFT and ERA are matched.
- The ERA total amount equals the sum of all EEOBs listed on the ERA.
- The EFT and ERA total amounts must balance.
- The EFT has been accepted by FMS.
- The ERA negative payments all have a matching positive payment (+/- pairs).

### Medical Auto-Posting Create and Process Receipt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the nightly job runs, a receipt is created and processed if the following conditions are met:

- The EEOB detail has been verified against the bill detail.
- The claim balance covers the payment to be posted for all EEOBs.
- The claim status is open for all EEOBs.
- The claim has not been referred to regional council or general council.

If all EEOB auto-posting conditions to create, and process a receipt are not met, the system sends that EEOB to the Auto-Posting Awaiting Resolution list. Once a user corrects the condition that prevented receipt processing, the EEOB can be reprocessed by the next nightly job. For more details, refer to the section on Auto-Posting Awaiting Resolution.

The claim has not been terminated as a write off, indicated by a “WO” claim status.

### Medical Auto-Posting Receipts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system creates a receipt for all EEOBs that can be auto-posted, even if all EEOBs in an ERA cannot be posted at the same time.

The following examples illustrate possible auto-posting situations.

1.  Example of a Partially Posted ERA:
- Scenario:

The ERA contains a hundred EEOBs and the ERA is an auto-posting candidate.

Seventy of the EEOBs meet the conditions to create and process a receipt.

The nightly auto-posting job runs.

- Auto-Posting Day \#1:

A receipt is created and processed for seventy EEOBs. The receipt number is EXXXXXXA.

Thirty EEOBs do not have a receipt and the EEOBs are on the Auto-Posting Awaiting Resolution list.

The ERA is partially posted.

26. The receipt number contains an alphabetic character at the end.
- Auto-Posting Day \#2:

A user resolved the issues on twenty of the EEOBs.

The nightly auto-posting job runs.

A receipt is created and processed for twenty EEOBs. The receipt number is EXXXXXXXXB.

Ten EEOBs do not have a receipt and the EEOBs are on the Auto-Posting Awaiting Resolution list.

The ERA is partially posted.

27. The receipt number contains an alphabetic character at the end, incrementing to the next letter of the alphabet.
- Auto-Posting Day \#3:

A user resolved the issues on the remaining ten EEOBs.

The nightly auto-posting job runs.

A receipt is created and processed for ten EEOBs. The receipt number is EXXXXXXXXC.

The ERA is completely posted.

None of the EEOBs for this ERA are on the Auto-Posting Awaiting Resolution list.

28. The receipt number contains an alphabetic character at the end, incrementing to the next letter of the alphabet.
183. Example of a Completely posted ERA. The ERA is partially posted.
- Scenario:

> The ERA contains a hundred EEOBs and the ERA is an auto-posting candidate.

> All the EEOBs meet the conditions to create and process a receipt.

> The nightly auto-posting job runs.

- Auto-Posting Day \#1:

> A receipt is created and processed for all EEOBs. The receipt number is EXXXXXXX.

> The ERA is completely posted.

> None of the EEOBs for this ERA are on the Auto-Posting Awaiting Resolution list.

29. The receipt number does not contain an alphabetic character at the end.

#### Pharmacy Auto Posting Candidates

The system auto-posts for pharmacy claims when the following conditions are met:

- Auto-posting for pharmacy claims is enabled in the EDI LOCKBOX PARAMETERS.
- The EEOB payer is not excluded from pharmacy auto-posting in the EDI LOCKBOX PARAMETERS.
- The Electronic Remittance Advice (ERA) does not have an exception.
- The ERA does not contain interest.
- The ERA does not contain an ERA level adjustment.
- The EFT and ERA are matched.
- The EFT has been accepted by Financial Management System (FMS).
- The ERA negative payments all have a matching positive payment (+/- pairs).

#### Pharmacy Auto Posting Create and Process Receipt

When the nightly job runs, a receipt is created and processed if the following conditions are met:

- The EEOB detail has been verified against the bill detail.
- The claim balance covers the payment to be posted for all EEOBs.
- The claim status is open for all EEOBs.
- The claim has not been referred to regional council or general council.

If all EEOB auto-posting conditions to create, and process a receipt are not met, the system sends that EEOB to the Auto-Posting Awaiting Resolution list. Once a user corrects the condition that prevented receipt processing, the EEOB can be reprocessed by the next nightly job. For more details, refer to the section on Auto-Posting Awaiting Resolution.

### Pharmacy Auto Posting Receipts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system creates a receipt for all EEOBs that can be auto-posted, even if all EEOBs in an ERA cannot be posted at the same time.

- If all EEOBs in an ERA can be posted, the receipt number will contain “E” followed by numeric characters.
- If only some of the EEOBs in an ERA can be posted, the receipt number will have an alphabetic character on the end, starting with “A,” and proceeding in order until all EEOBs have been posted. The base number stays the same.
1.  Example of Completed Posted Pharmacy ERA Scenario:

The ERA contains ten EEOBs and the ERA is an auto posting candidate. All the EEOBs meet the conditions to create and process a receipt.

The nightly auto-posting job runs.

- Auto-Posting Day \#1:

A receipt is created and processed for all EEOBs. The receipt number is EXXXXXXXX.

The ERA is completely posted.

None of the EEOBs for this ERA are on the Auto-Posting Awaiting Resolution list.

30. The receipt number does not contain an alphabetic character at the end.
184. Example of a Partially Posted ERA:
- Scenario:

The ERA contains a ten EEOBs and the ERA is an auto-posting candidate.

Seven of the EEOBs meet the conditions to create and process a receipt.

The nightly auto-posting job runs.

- Auto-Posting Day \#1:

A receipt is created and processed for seventy EEOBs. The receipt number is EXXXXXXXXA.

Three EEOBs do not have a receipt and the EEOBs are on the Auto-Posting Awaiting Resolution list.

The ERA is partially posted.

31. The receipt number contains an alphabetic character at the end.
- Auto-Posting Day \#2:

A user resolved the issues on two of the EEOBs.

The nightly auto-posting job runs.

A receipt is created and processed for twenty EEOBs. The receipt number is EXXXXXXXXB.

One EEOB does not have a receipt and the EEOBs are on the Auto-Posting Awaiting Resolution list.

The ERA is partially posted.

32. The receipt number contains an alphabetic character at the end, incrementing to the next letter of the alphabet.
- Auto-Posting Day \#3:

A user resolved the issues on the remaining one EEOB.

The nightly auto-posting job runs.

A receipt is created and processed for one EEOB. The receipt number is EXXXXXXXC.

The ERA is completely posted.

None of the EEOBs for this ERA are on the Auto-Posting Awaiting Resolution list.

33. The receipt number contains an alphabetic character at the end, incrementing to the next letter of the alphabet.

### EEOB Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST option displays an "A" indicator before the ERA number if auto-posting is complete for that ERA. The indicator is displayed for both medical and pharmacy auto posted ERAs.

\# ERA \# TRACE#

PAYER NAME/MATCH STATUS ERA PAID DT TOT AMT PAID DT REC'D

1 XXXXX XXXXXXXXX

3/31/05 7.46 3/31/05

THE COMMUNITY HOSPITAL APPROX \# EEOBs: 1

### Ignore Payment Retraction Pairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system ignores payment retraction pairs for medical and pharmacy claims when the following conditions are met, without regard to case sensitivity:

- Payment / Retraction pair is in the same ERA.
- The first 5 characters of the patient's last names match.
- The dates of service match.
- The bill numbers or claim numbers match.
- The social security numbers or patient ID’s match.
- The amounts billed sum to zero, such as +5 and -5.

### Status Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system makes the following status changes when a medical or pharmacy claim is successfully auto-posted:

- Claim Status – Collected / Closed or Open (with residual balance).
- Receipt Status – Closed.
- Detail Post Status – Posted, Not Posted or Partial.
34. Detail Post Status becomes Posted when all lines have been posted. Detail Post Status becomes Partial if some lines have been posted but not all.

### AR Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays the auto-posted transactions within Accounts Receivable in the same manner as a manually posted transaction. Specifically, Auto-Posted payments display on the TPJI – AR Account Profile and VT Transaction Profile screens.

## Working the APAR List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Auto-Posting Awaiting Resolution list displays EEOB detail records that require user intervention before the nightly auto-posting job can post. The APAR screen contains the actions that enable research, resolution, and the ability to mark the EEOB for auto-posting. Once an entry is marked for auto-post, the entry is removed from the APAR display.

Once the APAR option has been selected, the initial list of EEOBs is presented.

| Field    | Description                                                                                                                                                                                                         |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERA \#   | The number that the VistA system has assigned to designate an ERA. It is shown on the ERA List Worklist), after accessing the WL Worklist menu option. Each ERA is in numerical order as it is accepted into Vista. |
| Claim \# | Claim used to bill the insurance company.                                                                                                                                                                           |
| Posted   | The total amount posted to the claim.                                                                                                                                                                               |
| Post Dt  | The date the amount was posted.                                                                                                                                                                                     |
| Unposted | The balance remaining.                                                                                                                                                                                              |

<span id="_Toc183424293" class="anchor"></span>Table 9: APAR Options

Use preferred view N// O

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: A// LL

(C)HAMPVA,(M)EDICAL, (P)HARMACY, or (A)LL: ALL//

Sort By PAYER (N)AME, APAR (R)EASON, (P)OSTED, (U)NPOSTED,: UNPOSTED// ??

Enter ‘PAYER NAME’ to sort by payer name.

Enter ‘APAR REASON’ to sort by the reason code.

Enter ‘POSTED’ to sort by the posted amount.

Enter ‘UNPOSTED’ to sort by the unposted amount.

Select one of the following:

N PAYER

R REASON

P POSTED

U UNPOSTED

Sort By PAYER (N)AME, APAR (R)EASON, (P)OSTED, (U)POSTED, APAR (R)EASON: UNPOSTED//

Sort By (H)IGHEST TO LOWEST or (L)OWEST TO HIGHEST: HIGHEST TO LOWEST// ??

Enter ‘HIGHEST TO LOWEST’ to sort amounts in decreasing order.

Enter ‘LOWEST TO HIGHEST’ to sort amounts in increasing order.

Select one of the following:

1 HIGHEST TO LOWEST

2 LOWEST TO HIGHEST

Sort By (H)IGHEST TO LOWEST or (L)OWEST TO HIGHEST: HIGHEST TO LOWEST//

AUTOPOST - AWAIT RESOLUTION Feb 14, 2017@02:43:35 Page: 1 of 1

Current View: MEDICAL CLAIMS for ALL PAYERS

Sorted By: Posted – Highest to Lowest

ERA \#.Seq Claim \# Posted Post Dt Unposted

Payer Name/ID

APAR Reason

1 43416.1 KXXXXXX 0.00 1/23/17 2169.44

AETNA/10XXXXXXXX

CLAIM ALREADY COMPLETED/CLOSED

2 43417.1 KXXXXXX 0.00 1/23/17 594.33

AETNA/10XXXXXXXX

3 43419.1 KXX XXXX 0.00 1/23/17 487.76

CIGNA BEHAVIORAL HEALTH, INC./10XXXXXXXX

### APAR – Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several List Managers options available on the APAR screen that provides greater capability to manage EEOB records.

| Field          | Description                                                   |
|----------------|---------------------------------------------------------------|
| Select EEOB    | Used to select a specific EEOB.                               |
| View/Print ERA | Used to display / print the summary ERA information.          |
| Change View    | Used to customize the information displayed on the APAR list. |

<span id="_Toc183424294" class="anchor"></span>Table 10: EEOB Line

#### View / Print ERA

The View / Print ERA action is used to display and print the summary ERA information.

#### Change View

The Change View action is used to customize the information displayed on the APAR list. After answering the question, the system gives the user the option to “SAVE” the selection as a “preferred view.” The answer is used to filter the display to limit the entries that are included.

If the user saves a preferred view, they will be prompted if they want to use that view in the future.

The following option is available as a filter.

Select Action: Next Screen// C Change View

(C)HAMPVA, (M)EDICAL, (P)HARMACY, OR (A)LL: ALL//

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: A//

DO YOU WANT TO SAVE THIS AS YOUR PREFERRED VIEW (Y/N)? NO//

Payer Range Selection:

ALL

RANGE

The screen header will indicate the Current View selected as follows:

AUTO-POST - AWAIT RESOLUTION Nov 19, 2013@21:37:21 Page: 1 of 2

Current View: MEDICAL + PHARMACY CLAIMS for ALL PAYERS

ERA#.Seq Claim# Posted Amt Post Date Un-posted Bal

\_\_\_\_ \_Payer Name/ID\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1 87705.1 KXXXXXX 3000.41 11/1/13 127.44

ANTHEM BCBS OF WISCONSIN/XXXXXXXXXX

2 87705.2 KXXXXXX 3000.41 11/1/13 127.44

ANTHEM BCBS OF WISCONSIN/XXXXXXXXXX

Enter ?? for more actions

Select EEOB View/Print ERA

Change View Exit

Select Action: Next Screen//

#### Select EEOB

The Select EEOB action allows the user to select a specific EEOB by number. After selection, the APAR scratchpad is displayed.

APAR - EEOB ITEM - SCRATCHPAD Jul 21, 2014@15:34:59 Page: 1 of 1

ERA Entry \#: XXXX Total Amt Pd: 50.00

Posted Amt: 0.00 Unposted balance: 50.00

Payer Name/ID: ONE INSURANCE COMPANY/XXXXXXXX

EFT \#/TRACE \#: XXX/XXXXXXXXXX

Posted Receipt \#(s):

EEOB: ERA Seq \# 1 Net Payment Amt: 50.00

1.001 Claim \#: KXXXXXX Patient/Last 4: PATIENT,ONE/XXXX

Claim Bal: 51051.58 Billed Amt: 51051.58 Amt To Post: 50.00

Svc Dt: 4/23/14 COB: NO Rx Copay: UNKNOWN Means Tst: ??

Payment Amt: 50.00 Total Adjustments: 0.00 Net: 50.00

APAR Reason: FIELD VERIFICATION FAILED

Enter ?? for more actions

Split/Edit a Line EOB View/Print EEOB Review Line

Mark for Auto Post ERA View/Print ERA Verify

Claim Comment Research Menu EXIT

Select Action: Quit//

The header of the APAR Scratchpad screen contains:

- The ERA Entry \#.
- The Total Amount being Paid on the ERA (this will equal the dollar amount of the Electronic Funds Transfer).
- The Posted Amount; the Unposted balance.
- The Name and ID number of the Payer; the EFT Trace \#.
- The base number for the Posted Receipt(s) numbers.

Each EEOB line item equates to a line item on a paper EOB form. HIPAA mandates standardization of the electronic transmissions.

| Field                  | Description                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EEOB Seq \# on ERA     | This shows the line item order as the payer sent it. Remember, the Worklist can be sorted with Zero Payments First or Zero Payments Last, so the sequence number may not match the line item list on the far left of the screen.                                                                                                                                            |
| Net Payment Amt        | The payment amount plus or minus the adjustment amount will equal the net payment amount for this claim number.                                                                                                                                                                                                                                                             |
| Claim \#               | The claim number associated with this payment. This may or may not be the correct claim number. Research each claim carefully verify if the amount being paid is appropriate for the claim in AR. If the line item is marked (V), the system has already done a verification match between bill number and the patient’s name, date of service, and original billed amount. |
| Patient/Last 4         | The patient’s name and last four digits from the SSN. Used to help identify this payment is for the correct Claim.                                                                                                                                                                                                                                                          |
| Claim Balance          | Current balance from AR.                                                                                                                                                                                                                                                                                                                                                    |
| Billed Amt             | Original billed amount from AR.                                                                                                                                                                                                                                                                                                                                             |
| Amount to Post         | The payment amount plus or minus the adjustment amount will equal the amount to post for this claim number.                                                                                                                                                                                                                                                                 |
| Service Date           | Beginning Service Date for this Claim.                                                                                                                                                                                                                                                                                                                                      |
| COB                    | Coordination of Benefits information that indicates whether a secondary payer has been identified for this claim.                                                                                                                                                                                                                                                           |
| Rx Copay               | Current Rx Copay status of the patient.                                                                                                                                                                                                                                                                                                                                     |
| Means Test             | Indicates if this patient may be responsible for Means Test co-payments.                                                                                                                                                                                                                                                                                                    |
| Payment Amt            | Amount of money paid for this claim on this ERA.                                                                                                                                                                                                                                                                                                                            |
| Total Adjustments      | Net total of all adjustments for this line item.                                                                                                                                                                                                                                                                                                                            |
| Net                    | The payment amount plus or minus the adjustment amount.                                                                                                                                                                                                                                                                                                                     |
| ECME \#                | ECME number generated when the NCPDP claim is submitted for a pharmacy prescription. This field only displays for a pharmacy claim.                                                                                                                                                                                                                                         |
| Rx/Fill/Release Status | The prescription number fill number and release status (released, non-released). This field only displays for a pharmacy claim.                                                                                                                                                                                                                                             |
| DOS                    | The date of service submitted on the NCPDP claim. This field only displays for a pharmacy claim.                                                                                                                                                                                                                                                                            |
| APAR Reason            | The reason the EEOB is on the APAR list.                                                                                                                                                                                                                                                                                                                                    |

<span id="_Toc183424295" class="anchor"></span>Table 11: APAR Scratchpad

### APAR Scratchpad – Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several actions available on the APAR Scratchpad that can assist a user to ensure that the correct payment is being applied to the correct claim. Except for the Mark for Auto-Post action, the actions behave the same as the actions on the ERA Worklist Scratchpad. Refer to the ERA Worklist Scratchpad section for more details on functionality.

<table>
<caption><p><span id="_Toc183424296" class="anchor"></span>Table 12: Key</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Split/Edit a Line</td>
<td>Used to split a payment or adjustment between two or more bills (if the payer has combined payments), or to correct the claim # associated with a payment (if the payer has reported the payment for the wrong bill). Option can also be used to put payment into suspense. This is locked with the security key “RCDPEPP.”</td>
</tr>
<tr class="even">
<td>Mark for Auto-Post</td>
<td><p>This action checks the EEOB for auto-posting criteria. If all criteria are met, the EEOB is successfully marked for auto-post, which means the EEOB will be removed from the APAR display and reprocessed by the nightly auto-post job. Verification (V) is not required before marking an EEOB for auto-posting.</p>
<p>This is locked with the security key “RCDPEPP.”</p></td>
</tr>
<tr class="odd">
<td>Claim Comment</td>
<td>Used to enter a one line comment for ANY exception on the APAR List.</td>
</tr>
<tr class="even">
<td>View/Print EEOB</td>
<td>Used to display / print the detail received on the ERA for a selected line (EEOB).</td>
</tr>
<tr class="odd">
<td>View/Print ERA</td>
<td>Used to view / print posting for claims with the entire formatted ERA, with or without the EEOB detail, and with or without Auto-Post and Match Status audit information.</td>
</tr>
<tr class="even">
<td>Research Menu</td>
<td>Link to all the necessary AR functions / processes such as TPJI, needed to process ERAs. These can each still be accessed through regular AR menu options.</td>
</tr>
<tr class="odd">
<td>Review Line</td>
<td>Allows addition of comments or used as a bookmark on a specific line within an ERA in case processing was interrupted, thereby allowing the user to more easily resume where the user left off. This option must be turned ‘on’ each time the user enters the ERA to enter or view comments.</td>
</tr>
<tr class="even">
<td>Verify</td>
<td>Provides the functionality to identify and manually mark EEOBs as verified.</td>
</tr>
</tbody>
</table>

<span id="_Toc183424296" class="anchor"></span>Table 12: Key

#### Action Option: Split / Edit a Line

Sometimes Payers combine payments for two or more claims into one claim. This action is used to split the payment to the appropriate claim, and to put a payment into suspense. It can also be used to correct an incorrect claim number.

This action requires the RCDPEPP security key.

APAR - EEOB ITEM - SCRATCHPAD Jun 29, 2016@11:49:03 Page: 1 of 1

ERA Entry \#: XXXXX Total Amt Pd: 2555.25

Posted Amt: 0.00 Un-posted balance: 2555.25

Payer Name/ID: AETNA/XXXXXXXXXX

Posted Receipt \#(s):

EEOB: ERA Seq \# 1 Net Payment Amt: 2555.25

1.001 Claim \#: KXXXXXX Patient/Last 4: REDACTED/XXXX

Claim Bal: 0.00 Billed Amt: 2555.25 Amt To Post: 2555.25

Svc Dt: 11/3/15 COB: NO Rx Copay: NON-EXEMPT Means Tst: REQ

Payment Amt: 2555.25 Total Adjustments: 0.00 Net: 2555.25

APAR Reason: FIELD VERIFICATION FAILED

Enter ?? for more actions

Split/Edit a Line EOB View/Print EEOB Review Line

Mark for Auto Post ERA View/Print ERA Verify

Claim Comment Research Menu EXIT

Select Action: Quit//SPLIT

This example shows how to Split / Edit Line item \#4 to post the payment correctly. This action takes place after reviewing the EEOB detailed data to confirm how the payment should be applied.

1.001 Claim \#: KXXXXXX Patient/Last 4: REDACTED /XXXX

Claim Bal: 0.00 Billed Amt: 2555.25 Amt To Post: 2555.25

Svc Dt: 11/3/15 COB: NO Rx Copay: NON-EXEMPT Means Tst: REQ

Payment Amt: 2555.25 Total Adjustments: 0.00 Net: 2555.25

APAR Reason: FIELD VERIFICATION FAILED

CLAIM \#: KXXXXXX// \>\>Current claim balance is: 0.00

PAYMENT AMOUNT TO APPLY TO THIS CLAIM: 2555.25// 2000

RECEIPT LINE COMMENT: comment for claim KXXXXXX

CLAIM \#: kXXXXXX \>\>Current claim balance is: 3444.75

PAYMENT AMOUNT TO APPLY TO THIS CLAIM: 555.25// 500

RECEIPT LINE COMMENT: comment for claim KXXXXXX

CLAIM \#: kXXXXXX \>\>Current claim balance is: 0.00

PAYMENT AMOUNT TO APPLY TO THIS CLAIM: 55.25//

RECEIPT LINE COMMENT: comment for claim KXXXXXX

Apply the correct payment amount to the correct claim number(s) until all the funds are applied.

EEOB WORKLIST SPLIT LINE Jun 29, 2016@12:04:13 Page: 1 of 1

1.001 Claim \#: KXXXXXX Patient/Last 4: REDACTED /XXXX

Claim Bal: 0.00 Billed Amt: 2555.25 Amt To Post: 2555.25

Svc Dt: 11/3/15 COB: NO Rx Copay: NON-EXEMPT Means Tst: REQ

Payment Amt: 2555.25 Total Adjustments: 0.00 Net: 2555.25

APAR Reason: FIELD VERIFICATION FAILED

Claim \# Payment Amount Adjustment Amt Net Amount

1 KXXXXXX 2000.00 0.00 2000.00

comment for claim KXXXXXX

2 kXXXXXX 500.00 0.00 500.00

comment for claim KXXXXXX

3 Kxxxxxx 55.25 0.00 55.25

comment for claim KXXXXXX

============== ============== ==============

TOTALS: 2555.25 0.00 2555.25

Enter ?? for more actions

File New Lines Edit Lines Split Exit

Select Action:Quit//

At this point, the user should FILE NEW LINES to process the split.

Edit Line Split if the information is not correct. File the new lines to save this information. *Exiting without filing will mean all changes are discarded.*

Reason text (i.e., Comment) is mandatory when leaving a portion of the payment in suspense.

COMMENT: ??

Enter a code from the list.

Select one of the following:

Collected/Closed

2 Cancelled

3 Returned refund

4 Overpayment

5 Inactive bill

6 Duplicate payment

7 Policy termed

8 Service connected

9 Other

The scratchpad screen displays the following if a receipt line comment has been added.

2.002 Claim \#: SUPENSE Patient/Last 4: ??

\*\*\*CLAIM NOT FOUND IN YOUR AR \*\*\*

Payment Amt: 160.00 Total Adjustments: 0.00 Net: 160.00

Receipt: EXXXXXXXXXXXX Receipt Comment: OVERPAYMENT

Added By: EMPLOYEE,ONE

Date/Time Added: July 20 2017@10:00:00

#### Action Option: Mark for Auto-Post

The ListManager screen contains the action of Mark for Auto-Post that will check the EEOB for auto-posting criteria, and mark the EEOB for auto-posting if all criteria are met. This action requires the RCDPEPP security key.

#### Action Option: Claim Comment

The ListManager screen includes a “Claim Comment” option to allow the user to enter a one line comment for ANY exception on the APAR List.

\+ Enter ?? for more actions

Split/Edit a Line EOB View/Print EEOB t Review Line

Mark for Auto Post ERA View/Print ERA Verify

Claim Comment Research EXIT

Select Action: Quit//Claim

Select EDI LBox EEOB Data Exception(s): (1-4): 2

Selection \#: 2 KXXXXXX

Comment: This is where the Claim Comment will appear and may wrap to the next line. A comment can be entered for ANY claim and is tied to an ERA Seq line#.

35. Once successfully entered, the Claim Comment displays as indicated in the APAR screen display and on the ERA Worklist / Scratch Pad as well as on the View / Print ERA display – on the individual EEOB. If the EEOB has no comment, nothing will display.

#### Action Option: MARK FOR AUTO-POST

When the user selects the new “Mark for Auto Post” Action Option, the system re-evaluates the selected ERA to determine if the ERA can be marked as an Auto-Post CANDIDATE. The system displays a message to the user indicating whether the ERA was successfully Marked as an Auto-Post CANDIDATE – or – the reason why the check failed. This action requires the RCDPEPP security key.

- If the system determines that the <u>ERA IS an Auto-Post CANDIDATE</u>, the following success message is displayed:

ERA List - Worklist Nov 30, 2015@12:31:17 Page: 1 of 22

SELECTED MATCH STATUS: BOTH POST STATUS : BOTH

DATE RANGE: 2/12/15-2/12/15 AUTO-POSTING : BOTH

ALL PAYERS PHARMACY/MEDICAL: BOTH

\# ERA \# Trace#

PAYER NAME/MATCH STATUS & DATE ERA PAID DT TOT AMT PAID DT REC’D

1 4 XXXXXXXXXXX

2/12/15 485.27 2/12/15

EPHARM INSURANCE APPROX \# EEOBs: 1

EFT MATCHED 2/12/15 EFT RECEIPT STATUS: NOT ENTERED

\|’-‘ No scratchpad\|’x’ EXC \|’A’ autopost complete

Select ERA View/Print ERA Admin Cost Adj

Sort List Change View Exit

Mark for Auto Post ERA Manual Match

Select Action: Quit// MAR Mark for Auto Post

ERA has been successfully Marked as an Auto-Post CANDIDATE

Enter RETURN to continue or ‘^’ to exit:

36. If the ERA is deemed an Auto-Post CANDIDATE, the ERA enters the Auto-Post pipeline to be processed with other CANDIDATES during the next nightly process.
- If the system determines that the <u>ERA IS NOT an Auto-Post CANDIDATE</u>, ONE of the error message reasons is displayed:

ERA was NOT Marked as an Auto-Post CANDIDATE – Already marked for Auto-Posting

ERA was NOT Marked as an Auto-Post CANDIDATE – Already partially Auto-Posted

ERA was NOT Marked as an Auto-Post CANDIDATE – Already completely Auto-Posted

ERA was NOT Marked as an Auto-Post CANDIDATE – ERA not matched

ERA was NOT Marked as an Auto-Post CANDIDATE – Zero value ERA

ERA was NOT Marked as an Auto-Post CANDIDATE – Medical auto-posting off

ERA was NOT Marked as an Auto-Post CANDIDATE – Pharmacy auto-posting off

ERA was NOT Marked as an Auto-Post CANDIDATE – Medical payer excluded

ERA was NOT Marked as an Auto-Post CANDIDATE – Pharmacy payer excluded

ERA was NOT Marked as an Auto-Post CANDIDATE – Invalid Bill Number Exception(s)

ERA was NOT Marked as an Auto-Post CANDIDATE – ERA level Adjustment(s)

ERA was NOT Marked as an Auto-Post CANDIDATE – ERA has a receipt

ERA was NOT Marked as an Auto-Post CANDIDATE – Unable to create scratchpad

ERA was NOT Marked as an Auto-Post CANDIDATE – Claim Level Adjustments w/o payment

ERA was NOT Marked as an Auto-Post CANDIDATE – +/- pairs do not balance

## Auto-Decrease of Medical Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA runs a nightly job to automatically perform a decrease adjustment to a third-party medical claim under certain conditions. The automatic decrease is made with a contractual decrease adjustment amount that brings the claim balance to zero.

An automatic decrease will only occur if the EEOB has been auto-posted. Refer to the section on Parameters for details on the settings that affect auto-decrease of medical claims.

The following conditions must be met:

- Auto-posting of third-party medical claims is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The payer is not excluded from auto-posting of third-party medical claims in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] and the EEOB is auto-posted.
- Auto-decrease of third-party medical claims is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The payer is not excluded from auto-decrease of third-party medical claims in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The number of days since the EEOB was posted is equal to or greater than the number of days specified in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The residual balance on the EEOB is equal to or less than the dollar amount maximum specified in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The claim has not been referred to regional council or general council.

### Decrease Adjustment Warning Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option DECREASE ADJUSTMENT \[PRCAC TR DECREASE\] displays a warning message if there are pending payments for the selected claim. Additionally, the user can receive a “Marked for Auto-Post warning if they try to make a decrease adjustment on a bill that has at least one associated EEOB marked for auto-post.

Select Adjustment to an AR record \<TEST ACCOUNT\> Option: Decrease Adjustment

Select (B)ILL or (E)CME#: B// ILL NUMBER

Select BILL: KXXXXXX

1 KXXXXXX 552-KXXXXXX RX CO-PAYMENT/N 10/01/03 XXXX,XXXX COLLECTED

2 KXXXXXX 405-KXXXXXX REIMBURS.HEALTH 05/15/14 EXPRESS SC ACTIVE

CHOOSE 1-2: 2 405-KXXXXXX REIMBURS.HEALTH 05/15/14 EXPRESS SC ACTIVE

Principal Balance: 51051.58 FY: 14 Principal Balance: 51051.58

Interest Balance: 0.00

Admin Balance: 0.00

-----------

TOTAL Balance: 51051.58

Checking the bill's balance ... IN Balance!

Marked for Auto-Post. Are you sure? (Y/N) NO// NO

Exiting bill adjustment.

Select (B)ILL or (E)CME#: B// ILL NUMBER

1 KXXXXXX 552-KXXXXXX RX CO-PAYMENT/N 10/01/03 XXXXX,XXXX COLLECTED

2 KXXXXXX 405-KXXXXXX REIMBURS.HEALTH 05/15/14 EXPRESS SC ACTIVE

CHOOSE 1-2: 2 405-KXXXXXX REIMBURS.HEALTH 05/15/14 EXPRESS SC ACTIVE

Principal Balance: 51051.58 FY: 14 Principal Balance: 51051.58

Interest Balance: 0.00

Admin Balance: 0.00

-----------

TOTAL Balance: 51051.58

Checking the bill's balance ... IN Balance!

Warning – Pending Payments of \$XXXX.XX exist

Rcpt: XXXXXXXXX \$XX.XX No Trace Number

Rcpt: XXXXXXXXX \$XXX.XX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Rcpt: XXXXXXXXX \$XXX.XX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

ERA: XXXXX \$XX.XX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Marked for Auto-Post. Are you sure? (Y/N) NO// YES

Enter the DECREASE Adjustment AMOUNT, from .01 to 51051.58.

DECREASE PRINCIPAL BALANCE BY: 1.00

Is this a CONTRACT adjustment ? YES//

If you process the transaction, the bill will look like:

Current Principal Balance: 51051.58

NEW DECREASE Adjustment: -1.00

-----------

NEW Principal Balance: 51050.58

Are you sure you want to enter this DECREASE adjustment ? YES//

Adjustment Transaction: XXXXXXX has been added.

Enter a comment for the DECREASE Adjustment:

COMMENTS:

No existing text

Edit? NO//

## Auto-Decrease of Pharmacy Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA runs a nightly job to automatically perform a decrease adjustment to a third-party pharmacy claim under certain conditions. The automatic decrease is made with a contractual decrease adjustment amount that brings the claim balance to zero.

An automatic decrease will only occur if the EEOB has been auto-posted. Refer to the section on Parameters for details on the settings that affect auto-decrease of pharmacy claims.

The following conditions must be met:

- Auto-posting of third-party pharmacy claims is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The payer is not excluded from auto-posting of third-party pharmacy claims in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] and the EEOB is auto-posted.
- Auto-decrease of third-party pharmacy claims is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The payer is not excluded from auto-decrease of third-party pharmacy claims in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The number of days since the EEOB was posted is equal to or greater than the number of days specified in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The residual balance on the EEOB is equal to or less than the dollar amount maximum specified in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The claim has not been referred to regional council or general council.

# The EFT Has Been Accepted by FMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## FMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Financial Management System (FMS) is an interactive system to manage central payment services to federal government agencies, including the VHA financial data. Deposits to FMS are transmitted during the nightly process as individual deposits, and are relayed through the DMI / mailman system. The EFT information is transferred into VistA from Financial Services Center (FSC). Although paper checks are also deposited through FMS by a daily deposit ticket at each medical center, EFTs are also deposited via a deposit ticket. Deposit tickets are assigned for EFTs by PNC bank (they assign the 6-digit number, and the FSC makes it a 9-digit number by adding a “569” prefix).

## Three Day EFT Cycle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The diagram below demonstrates a high-level overview of the ePay / FMS process. Upon adjudication at the payer level, the payer transmits 835 information to the respective banking partner. In turn, this banking partner transmits the information to PNC Bank, the banking partner of the VA. PNC bank sends the EFT information to US Treasury for deposit, and to FSC to be translated into VistA language and for processing to the sites. In addition to sending the data to each individual VistA system, FSC also sends the information to EPHRA for storing, and reference of the data as needed. Each VistA system interacts with FMS through the nightly process, notifying the financial system of funds that have been processed for each medical center.

A complete cycle takes three business days to complete.

<span id="_Toc183424271" class="anchor"></span>Figure 5: EFT 3-Day Cycle Part \#1

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/006.png)

The three-day cycle detailed:

- Day 1 – EFT populates VistA with a system generated electronic (e) receipt, and transmits to FMS with a CR document during the nightly process. This shows in the VistA system as ‘NA’ when viewing the worklist. Deposit can be viewed by looking at Receipt profile, List of receipts, or deposit processing.

<span id="_Toc183424272" class="anchor"></span>Figure 6: EFT 3-Day Cycle Part \#2

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/007.png)

- Day 2 – FMS accepts deposit, and sends message back to VistA during nightly process. The money is deposited into 528704/8NZZ. This shows in the VistA system as ‘transmitted’ when viewing the worklist.

<span id="_Toc183424273" class="anchor"></span>Figure 7: EFT 3-Day Cycle Part \#3

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/008.png)

- Day 3 – EFT is ready to be processed with ERA or paper EOB, and transmit back to FMS. This shows in the VistA system as ‘accepted’ when viewing the worklist.

<span id="_Toc183424274" class="anchor"></span>Figure 8: EFT 3-Day Cycle Part \#4

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/009.png)

The screen capture below demonstrates how the three-day cycle shows on the worklist in the VistA system. This information can also be viewed on the EFT Daily Activity Report, and the EFT unmatched aging report.

<span id="_Toc183424275" class="anchor"></span>Figure 9: VistA Worklist

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/010.png)

When an e-receipt is processed to FMS, a TR document (Transfer Document) is created. The TR document transmits during the nightly process. The TR document does not transmit money to FMS, but transfers funds from 528704/8NZZ to the appropriate MCCF appropriation of 528704. The TR document number can be viewed in the VistA system under the Receipt Processing Option.<span id="_Toc269910937" class="anchor"></span>

Figure 10: Transfer Document

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/011.png)

## EFT Deposits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view a copy of the CR code sheet on the CRLT table, enter the transaction code (CR), and the CR number. This screen shows the Fund and RSC the money dropped into in FMS.

For this example, the CR number is XXXXXXXXXX:

ACTION: N TABLEID: CRLT USERID: XXXX SLK

\*\*\* CASH RECEIPTS LINE INQUIRY SCREEN \*\*\*

KEY IS TRANS CODE, CR NUMBER, LINE

TRANS CODE: CR CR NUMBER: XXXXXXXXXX

01-

LINE: 001 BFYS: 04 FUND: XXXXXX

STATION/SAT: XXX FCP/PRJ: JOB NO:

COST CTR/SUB: BOC/SUB: REPT CATG:

REV SRCE/SUB: XXXXXX CLSD BFYS: CLSD FUND:

GL ACCOUNT: TRANS TYPE: 23 TRAVEL TYPE:

VENDOR/PROVIDER: MCCFVALUE UNAPPLIED DEPOSIT NO:

AMOUNT: 1,480.00 CHECK NUMBER:

REF TC: REF DOC NO: REF LINE:

ADV: ADVANCE NO: ADV IND:

AGREEMENT NO: ACTION OUT:

DESCRIPTION:

View the General Ledger Detail Balance (GLDB) table to see all deposits into the GL ACCT and RSC for approximately two months. For this table, select the FY, BFY, FUND, GL ACCT, AD/OF, STN, and RSC.

ACTION: R TABLEID: GLDB USERID: S570 SLK

\*\*\* GENERAL LEDGER DETAIL BALANCE INQUIRY SCREEN \*\*\*

FY BFY FUND GL ACCT AD/OF STN COST CTR FCP/PRJ BOC/REV SRCE TYPE

-- ----- ------ ------- ---- ------- -------- --------- ------------ ----

04 04 XXXXXX XXXX XXX XXXX 01

TRANS ID DATE FM REF DOCUMENT VENDOR VENDOR INV \# AMT

---------- ------ -- ------------- ------- ----------------- ----------

XXXXXXXXXX 01 MCCFVALUE

1,480.00

XXXXXXXXXXXX XXXXXX 01 MCCFVALUE

428.34

XXXXXXXXXXXX XXXXXX 01 MCCFVALUE

37.64

XXXXXXXXXXXX XXXXXX MCCFVALUE

1,084.95

37. All transfers in from CR Documents will show up under GL ACCT 1029. All transfers, from the TR documents will show up on this table under the GL ACCT 1030.

| Field        | Description           |
|--------------|-----------------------|
| FY           | Fiscal Year           |
| BFY          | Budget Fiscal Year    |
| FUND         | Fund                  |
| GL ACCT      | General Ledger Acct   |
| AD/OF        | Administrative Office |
| STN          | Station               |
| BOC/REV SRCE | Revenue Source Code   |

<span id="_Toc183424297" class="anchor"></span>Table 13: Code Definition

# NPI (National Provider Identifier)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The facility and providers NPI can be found within the ERA by viewing the ERA details. This was an added function by Patch.

EDI LOCKBOX WORKLIST - ERA DETAIL 10/10/03 Page: 2

==============================================================================

PATIENT: IBpatient,One A/XXXX CLAIM \#: XXX-KXXXXXX

\*\*EOB PROVIDER(S)/NPI CLAIM PROVIDER(S)/NPI\*\*

--------------------- -----------------------

BILLING: /XXXXXXXXXX XXXXXXXX VAMC/XXXXXXXXXX

RENDERING: Ibclerk,One/XXXXXXXXXX

EOB GENERAL INFORMATION:

Type : NORMAL EOB EOB Paid DT : 02/07/07

Entry Dt/Tm :02/09/07 4:32 pm Claim Status : PROCESSED

Entry Dt/Tm :02/09/07 4:32 pm Review Status: ACCEPTED-COMPLETE EOB

Entered By : Insurance Seq: PRIMARY

Last Edited : 02/09/07 6:50 pm Last Edit By : POSTMASTER

Patient Name: IBpatient,One A Pt. Relation : PATIENT

Insured Name: IBpatient,One A Insured ID : XXXXXXXXX

Claim Rec'd Date :

Other Subscriber Name: XXXXX,XXXX X

Enter RETURN to continue or '^' to exit:

# Additional Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Auto–Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New functionality is included with the 3<sup>rd</sup> Party EDI Lockbox patch. It allows EDI claims to automatically be audited, and assigned an active status. Integrated Billing was modified to update AR whenever an EDI electronic status message is received for a bill that corresponds to one of these statuses:

- A3 = CLAIM SENT FOR ALL PAYER ROUTING
- AC = CLAIM FORWARDED TO PRINT CENTER
- A7 = CLAIM SENT TO PAYER, NO FURTHER UPDATES TO FOLLOW
- A8 = CLAIM SENT TO PAYER
- AA = CLAIM RECEIVED, PRINTED AND MAILED BY PRINT CENTER
- 2P = CLAIM ACCEPTED BY CLEARINGHOUSE- NO FURTHER UPDATES TO FOLLOW
- 10 = Claim sent to Payer
- 11 = Claim sent to Payer

The auto-audit function must be made active by using the Update Rate Types For Auto-audit option located in the Supervisor’s AR Menu. Once the rate type is selected, answer YES to the prompt AUTO-AUDIT? Then enter the appropriate Bill Resulting From reason must be selected. This reason will be assigned to every EDI claim for this rate type that is auto-audited by the system. To turn off auto-audit for a rate type, select the option, enter the rate type, and answer NO to the prompt AUTO-AUDIT? This deletes the Bill Resulting From field from for the rate type selected, and from this point on, no more bills with this rate type will be auto-audited.

38. Any claims that have claim rejects on the Claims Status Awaiting Resolution (CSA) worklist will not be auto-audited.

### Update Rate Types for Auto-Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To activate auto-audit for EDI claims within a particular rate type, proceed with the following selections:

Select Supervisor's AR Menu Option: Update Rate Types For Auto-audit

Select RATE TYPE NAME: ??

Choose from:

1 CRIME VICTIM Who's Responsible: INSURER

2 DENTAL Who's Responsible: PATIENT

3 HUMANITARIAN Who's Responsible: PATIENT

4 INTERAGENCY Who's Responsible: INSURER

5 MEANS TEST Who's Responsible: PATIENT

6 MEDICARE ESRD Who's Responsible: OTHER (INSTITUTION)

7 NO FAULT INS . Who's Responsible: INSURER

8 REIMBURSABLE INS . Who's Responsible: INSURER

9 SHARING AGREEMENT Who's Responsible: OTHER (INSTITUTION)

10 TORT FEASOR Who's Responsible: INSURER

11 WORKERS' COMP . Who's Responsible: INSURER

12 CHAMPVA REIMB.INS . Who's Responsible: INSURER

Select RATE TYPE NAME: REIMBURSABLE INS . Who's Responsible: INSURER

AUTO-AUDIT?: NO// YES

BILL RESULTING FROM: HI HEALTH INSURANCE 3RD PARTY BILLING

...OK? Yes// \<RET\>

### Process Open Bills / Paper Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system, as part of the current nightly processing, automatically runs through open bills / paper claims with a status of NEW BILL in AR File \#430.

39. A “Paper Claim” is identified by looking at the “Force To Print?”

    Parameter:

    MEDICAL Paper Claim = “FORCE LOCAL PRINT”

    PHARMACY Paper Claim = “NOT APPLICABLE – NOT TRANSMITTABLE”

### Validate Bill Data and Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system identifies which bills have bill type = “Reimbursable”, “NEW BILL” status, and have been created / completed in the billing package and signed off by a biller (i.e., which bills have all the necessary information within patient info, insurance company, subscriber info, codes). Specifically, the data elements that must be present include Patient Internal Entry Number (IEN), Debtor, Subscriber IEN, Group Name, and Group Number.

### Process AR Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If all the necessary information is in the AR file \#430, the process updates the AR entry to contain the Category of REIMBURSABLE INSURANCE, HI (HEALTH INSURANCE 3RD PARTY BILLING) in the ‘Bill Resulting From’ field.

For records updated during this process, the system updates the status to ACTIVE in AR File \#430.

### Required Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system utilizes the security key RCDPE AUTO DEC that is NOT automatically assigned to any user.

## Automatic Match EFTs to ERAs Acronym: MA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option manually starts the routine that runs as part of the normal nightly processing. Only select this option if the user needs to initiate the process of matching the 3rd Party Lockbox EFT records that have not yet been matched to the electronic ERAs currently on file. The process must be queued and only one of these processes can be running at any given time.

## EFT Manual Match Acronym: MM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to manually match an EFT detail record with an ERA record, and will mark the two records as matched. Use this option *only* if the automatic matching function is not able to make the match.

The EFT and ERA selected must both be unmatched, and the ERA must not be associated with a receipt. This action may be necessary if the Trace Numbers or Insurance Company IDs do not match on the two records, but the payer has confirmed they are indeed supposed to be matched. To make matching easier, the system allows a partial match on trace number, and leading zeroes are ignored. A date range filter can narrow the options for selection. This option allows the user to manually have the ERA re-evaluated for Auto-Posting to determine if the ERA can be marked for auto-post.

Select EDI Lockbox (ePayments) \<TEST ACCOUNT\> Option: EFT Manual Match

THIS OPTION WILL ALLOW YOU TO MANUALLY MATCH AN EFT DETAIL RECORD

WITH AN ERA RECORD.

Select by date Range? (Y/N) NO//

SELECT THE UNMATCHED EFT TO MATCH TO AN ERA: XXXX TTXXXXXXX 09-15-2015

EFT TRANSACTION: XXXX PAYER NAME: AETNA

PAYER ID: XXXXXXXXXX TRACE \#: XXXXXXXXXXXXX

TAX ID CORRECTION: NO CHANGE AMOUNT OF PAYMENT: 2202.50

MATCH STATUS: UNMATCHED RECEIPT \#: EXXXXXXXX

EFT RECORDED AT SITE: YES DATE CLAIMS PAID: SEP 15, 2015

DATE RECEIVED: SEP 15, 2015 TRANSACTION \#: 1

DEPOSIT NUMBER: TXXXXXX DEPOSIT DATE: SEP 25, 2018

ARE YOU SURE THIS IS THE EFT YOU WANT TO MATCH?: YES//

SELECT THE UNMATCHED ERA TO MATCH TO EFT \#XXXX: XXXXX XXXXXXXXXXXXX 09-15-15

2202.50 AETNA UNMATCHED

ENTRY: XXXXX TRACE NUMBER: XXXXXXXXXXXXX

INSURANCE CO ID: XXXXXXXXXX ERA DATE: SEP 15, 2015

TOTAL AMOUNT PAID: 2202.50 PAYMENT FROM: AETNA

FILE DATE/TIME: SEP 15, 2015@12:31:42

EFT MATCH STATUS: UNMATCHED ERA TYPE: ERA

INDIVIDUAL EOB COUNT: 1 MAIL MESSAGE: XXXXXX

ERA DETAIL POST STATUS: NOT POSTED EXPECTED PAYMENT METHOD CODE: ACH

ARE YOU SURE THIS IS THE CORRECT ERA TO MATCH TO?: YES//

EFT \#XXXX WAS SUCCESSFULLY MATCHED TO ERA \#XXXXX

Do you wish to mark this entry for Auto Posting (Y/N)?

If the system determines that the ERA is NOT an auto-post candidate, one of the following error messages is displayed:

ERA was NOT Marked as an Auto-Post CANDIDATE – Already marked for Auto-Posting

ERA was NOT Marked as an Auto-Post CANDIDATE – Already partially Auto-Posted

ERA was NOT Marked as an Auto-Post CANDIDATE – Already completely Auto-Posted

ERA was NOT Marked as an Auto-Post CANDIDATE – ERA not matched

ERA was NOT Marked as an Auto-Post CANDIDATE – Zero value ERA

ERA was NOT Marked as an Auto-Post CANDIDATE – Medical auto-posting off

ERA was NOT Marked as an Auto-Post CANDIDATE – Pharmacy auto-posting off

ERA was NOT Marked as an Auto-Post CANDIDATE – Medical payer excluded

ERA was NOT Marked as an Auto-Post CANDIDATE – Pharmacy payer excluded

ERA was NOT Marked as an Auto-Post CANDIDATE – Invalid Bill Number Exception(s)

ERA was NOT Marked as an Auto-Post CANDIDATE – ERA level Adjustment(s)

ERA was NOT Marked as an Auto-Post CANDIDATE – ERA has a receipt

ERA was NOT Marked as an Auto-Post CANDIDATE – Unable to create scratchpad

ERA was NOT Marked as an Auto-Post CANDIDATE – Claim Level Adjustments w/o payment

ERA was NOT Marked as an Auto-Post CANDIDATE – +/- pairs do not balance

## Mark Ø-Balance EFT Matched Acronym: ZB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There may be times when an EFT is received with a zero payment and has a paper EEOB associated with it. This option allows the user to select an EFT detail record and mark it as matched to a paper EEOB. This removes it from the EFT UNMATCHED AGING REPORT.

## Unmatch an ERA Acronym: UN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an ERA has been marked with a match status in error, this option allows it to be marked as unmatched again. Only select an ERA that was previously marked as matched and that has had no receipt created for it yet. If the Scratchpad entry has been created, it will need to be deleted before the unmatch can occur. If the ERA was matched to an EFT, the EFT will be remarked as unmatched, and returned to the EFT Unmatched Aging Report.

## Update ERA Posted using Paper EOB Acronym: UP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When Payers first come on-line with the 3<sup>rd</sup> Party EDI Lockbox functions it is possible for a facility to receive both EEOB data and paper EOBs at the same time. As a result, there may be times when the EOB data gets posted from the paper EOB to AR and FMS without referencing the ERA. In this situation, the ERA will indicate it is unposted. Use this option to mark the ERA as POSTED. It requires entering the receipt \# used to post the paper EOB information.

The existing functionality of the Update ERA Posted Using Paper EOB option is extended to include an automatic system search of an existing receipt when associating payments to the ERA. The automatic search for receipts to post requires the user to enter an ERA number to be updated to initiate automatic system search for associated receipt. The AR application will collect only those receipts that have an FMS DOC STATUS of “ACCEPTED BY FMS” as indicated in the following options:

- Receipt Processing \[RCDP RECEIPT PROCESSING\]
- List Of Receipts Report \[RCDP LIST OF RECEIPTS REPORT\]
1.  System will display specific payment details associated with the ERA for validation by the user prior to updating the ERA.
- Patient Name / Last 4 of SSN
- Bill Number
- Check number
- Trace number
- Date of Service
- AR Transaction Amount
- Receipt Number
- Date of Receipt
185. A new audit report will display or print data to identify usage of the Update ERA Posted to EOB option.

ERAs Posted with Paper EOB - Audit Report Page: 1

Run Date: 11/27/11@21:05:06

DIVISIONS: ALL

Date Range: 8/19/11 - 11/27/11 (DATE ERA UPDATED)

Date/Time User Who EFT Match Status

ERA \# Receipt \# ERA Updated Updated Detail Post Status

===============================================================================

XXXXX XXXXXXX 9/12/11@14:03:33 User, One MATCHED TO PAPER CHECK

MANUALLY POSTED

XXXXX XXXXXXXX 10/10/11@16:31:09 User, Two MATCHED TO PAPER CHECK

MANUALLY POSTED

XXXXX XXXXXXXXX 10/14/11@13:23:52 User, One MATCHED TO PAPER CHECK

MANUALLY POSTED

XXXXX XXXXXXXX 10/14/11@14:29:30 User, One MATCHED TO PAPER CHECK

MANUALLY POSTED

XXXXX XXXXXXXX 10/14/11@14:40:26 User, One MATCHED TO PAPER CHECK

The option now includes the capability of an automatic system search of an existing receipt when associating payments to the ERA.

Select EDI Lockbox Option: up Update ERA Posted Using Paper EOB

Select one of the following:

M Manually select receipt to post

A Automatic search for receipt to post

Select type of receipt to ERA link: M// a Automatic search for receipt to post

Select ELECTRONIC REMITTANCE ADVICE ENTRY: XXXXX XXXXXXXXXX 02-20-07 398.07

GREAT-WEST LIFE UNMATCHED

PATIENT: Patient,Test X/XXXX

Bill number: KXXXXXX

Check \#: XXXXXXX

Trace \#: XXXXXXXXXXXXXXX

DOS: Nov 21, 2006

AR Transaction amount: 8

## Remove ERA from Active Worklist Acronym: REM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to remove an unmatched ERA from the active Worklist. Use this option only if the deposit has not been made. The Remove ERA from Active Worklist option should always be used cautiously.

Here are some common scenarios: the user received a duplicate ERA; the ERA doesn’t belong to the station, the Update an ERA Posted using a paper EOB is not feasible or there is no other way to process the ERA (i.e., Receipts are purged from system). This marks the POSTED status of the ERA as NOT POSTED-REMOVED; and the EFT MATCH STATUS of the ERA is updated to REMOVED FROM WORKLIST.

This option has been enhanced to require the user to have the security key RCDPE MARK ERA and requires that a comment is entered that will represent the reason the ERA was removed from the Worklist.

If user tries to use the Remove ERA from Active Worklist option without having the RCDPE MARK ERA security key assigned, the user will receive the following error message (refer to sample screen shot below):

EXC EDI Lockbox 3rd Party Exceptions

WL ERA Worklist

APAR Auto-Post Awaiting Resolution

MA Automatic Match EFTs to ERAs

MCR EEOB Move/Copy/Remove

MM EFT Manual Match

OEFT Unposted EFT Override

DUP Duplicate ERA Worklist

REFT Remove Duplicate EFT Deposits

REM Remove ERA from Active Worklist

REP EDI Lockbox (ePayments) Reports Menu ...

UN Unmatch An ERA

UP Update ERA Posted Using Paper EOB

ZB Mark 0-Balance EFT Matched

IDP Identify Payers

UBD Remove Unbalanced Deposit Flag

Select EDI Lockbox Option: REM Remove ERA from Active Worklist

SORRY, YOU ARE NOT AUTHORIZED TO USE THIS OPTION

This option is locked with RCDPE MARK ERA key.

Enter RETURN to continue or '^' to exit:

## EEOB Move / Copy / Remove Acronym: MCR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB Move / Copy / Remove option was added to the EDI Lockbox Menu that provides the capability to move or copy an EEOB to the correct patient account to ensure Protected Health Information (PHI) is not compromised.

This option has the following features:

- Ability to select an EEOB and move or copy it to the appropriate claim(s) or remove it from the claim.
- The move, copy, or removal of an EEOB is captured and can be viewed with a new audit report.

The remove option is locked with security key RCDPE REMOVE EEOB to restrict usage of removing EEOBs from claims.

An example of the MOVE function:

Select EDI Lockbox Option: mcr EEOB Move/Copy/Remove

Select one of the following:

M Move EEOB to different claim

C Copy EEOB to multiple claims

R Remove EEOB from claim

Select action: M// ove EEOB to different claim

Select EXPLANATION OF BENEFIT (EEOB) to MOVE: KXXXXXX ARPatient,One

12-01-03 Inpatient REIMBURSABLE INS PRNT/TX

AETNA US HEALTHCARE (PRIMARY)

Select A/R Bill to MOVE to: KXXXXXX XXX-KXXXXXX REIMBURS.HEALTH INS 01

-12-04 AETNA US HEALTHCARE COLLECTED/CLOSED \$0.00

Move EEOB from claim KXXXXXX to claim KXXXXXX ? YES//

Enter JUSTIFICATION COMMENT: Moving EEOB to correct claim number

EEOB Update Complete

40. For audit purposes, a justification is required to move an EEOB.

An example of the COPY function:

Select EDI Lockbox Option: mcr EEOB Move/Copy/Remove

Select one of the following:

M Move EEOB to different claim

C Copy EEOB to multiple claims

R Remove EEOB from claim

Select action: M// c Copy EEOB to multiple claims

Select EXPLANATION OF BENEFIT (EEOB) to COPY: KXXXXXX User,Test

07-24-03 Outpatient REIMBURSABLE INS PRNT/TX

AETNA US HEALTHCARE (PRIMARY)

Select A/R Bill to COPY to: KXXXXXX XXX-KXXXXXX REIMBURS.HEALTH INS 07

-18-03 AETNA US HEALTHCARE COLLECTED/CLOSED \$0.00

Select another A/R Bill to COPY to: KXXXXXX XXX-KXXXXXX REIMBURS.HEALTH INS

07-18-03 AETNA US HEALTHCARE COLLECTED/CLOSED  \$0.00

Select another A/R Bill to COPY to:

Copy EEOB from claim K to clXXXXXXaim(s) KXXXXXX, KXXXXXX ? YES//

Enter JUSTIFICATION COMMENT: Copying EEOB information to additional claim KXXXXXX.

EEOB Update Complete

41. A justification comment is required to copy an EEOB to another claim.

An example of the REMOVE function:

Select EDI Lockbox Option: mcr EEOB Move/Copy/Remove

Select one of the following:

M Move EEOB to different claim

C Copy EEOB to multiple claims

R Remove EEOB from claim

Select action: M// R  Remove EEOB from claim

Select EXPLANATION OF BENEFIT (EEOB) to REMOVE: KXXXXXX User,Test

07-24-03 Outpatient REIMBURSABLE INS PRNT/TX

AETNA US HEALTHCARE (PRIMARY)

Are you sure you want to remove EEOB from claim KXXXXXX (Y/N)?? YES//

Enter JUSTIFICATION COMMENT: Removing EEOB information for test.

EEOB Update Complete

42. A justification comment is required to remove an EEOB. Also, the remove action is locked with security key RCDPE REMOVE EEOB.

## Remove Duplicate EFT Deposits Acronym: REFT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remove Duplicate EFT Deposits option was added to the EDI Lockbox Menu that provides the capability to remove a duplicate EFT from the EFT Unmatched Aging report.

EFTs marked as duplicates are displayed on the EFT Daily Activity report with a new display field that indicates the justification for the removal and the user that removed the EFT.

Select EDI Lockbox (ePayments) \<TEST ACCOUNT\> Option: REFT Remove Duplicate EFT

Deposits

> **WARNING:** Removing an EFT is \*\*NOT\*\* reversible.

Use this option only if you are sure you want to remove this EFT.

Please be aware that once an EFT is removed - it cannot be restored.

Are you sure you want to continue? NO// YES

This will mark EFT \# XXXX.X as removed.

Are you sure you want to continue? NO// YES

EFT REMOVAL REASON: FOR TESTING PURPOSES Replace

REMOVAL TYPE: ?

Please enter 'D' for Duplicate EFT or 'M' for Millenium EFT

Choose from:

D DUPLICATE EFT

M MILLENIUM EFT

REMOVAL TYPE: D DUPLICATE EFT

EFT \# XXXX.X has been marked as removed.

Press return to continue:

EDI LOCKBOX EFT DAILY ACTIVITY DETAIL REPORT Page: 1

RUN DATE: 11/30/16@11:12:12

DIVISIONS: ALL

PAYERS: ALL

DATE RANGE: 1/1/00 - 11/30/16 (Date Deposit Added)

DEP \# DEPOSIT DT DATE PD DEP AMOUNT FMS DEPOSIT STAT

EFT \# MATCHED DT PAYMENT AMOUNT ERA MATCH STATUS

EFT PAYER TRACE \# CR \#

PAYMENT FROM

TR \#

DEP RECEIPT \# DEP RECEIPT STATUS

===============================================================================

DATE EFT DEPOSIT RECEIVED: 1/14/04

XXXXXX 1/7/04 1/7/04 136.49 NO FMS DOC

1 1/7/04 10.80 MATCHED/ERA \#XX

XXXXXXXXXXXXXXX XXXXXXXXXX

AETNA LIFE INS/ XXXXXXXXXX

XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX , XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX

E16 XXXXXB QUEUED

The Duplicate EFT Audit Report was created to list all the EFT deposits that were removed from the EFT Unmatched Aging Report also referred to as the EFT Worklist. This report is found in the EDI Lockbox (ePayments) Reports Menu.

The new option is locked with a new security key RCDPE REMOVE DUPLICATES to restrict usage of removing EFTs from the EFT Unmatched Aging Report. Appropriate personnel, such as: managers, supervisors and leads should be assigned this security key.

EXC EDI Lockbox 3rd Party Exceptions

WL ERA Worklist

APAR Auto-Post Awaiting Resolution

MA Automatic Match EFTs to ERAs

MCR EEOB Move/Copy/Remove

MM EFT Manual Match

OEFT Unposted EFT Override

DUP Duplicate ERA Worklist

REFT Remove Duplicate EFT Deposits

REM Remove ERA from Active Worklist

REP EDI Lockbox (ePayments) Reports Menu ...

UN Unmatch An ERA

UP Update ERA Posted Using Paper EOB

ZB Mark 0-Balance EFT Matched

IDP Identify Payers

UBD Remove Unbalanced Deposit Flag

Select EDI Lockbox Option: reft Remove Duplicate EFT Deposits

SORRY, YOU ARE NOT AUTHORIZED TO USE THIS OPTION

The removed EFT will no longer display on the EFT Unmatched Aging Report.

EFT UNMATCHED AGING REPORT Page: 1

RUN DATE: 11/27/11@15:27:12

PAYERS: ALL

DATE RANGE: 11/27/11 - 11/27/11 (DATE EFT FILED)

AGED

DAYS TRACE \#

DEPOSIT FROM/ID DEP DATE

FILE DATE DEPOSIT AMOUNT DEP#/EFT# DEPOSIT POST STATUS

=============================================================================

TOTALS:

NUMBER AGED ELECTRONIC EFT MESSAGES FOUND: 0

AMOUNT AGED ELECTRONIC EFT MESSAGES FOUND: \$0.00

=============================================================================

\*\*\* END OF REPORT \*\*\*

## EEOB Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reports and screens display an EEOB indicator, the “%” character, next to the third-party accounts claim number when an EEOB has been received in the system for the claim.

- Brief Account Profile \[PRCAY ACCOUNT PROFILE\]
- Full Account Profile \[PRCAY FULL ACCOUNT PROFILE\]
- List All Bills \[PRCA LIST ALL BILLS\]
- Bill Profile \[RCDP BILL PROFILE\]
- Bill Transactions \[RCDP BILL TRANSACTIONS\]
- Claims Matching Report \[RCDP CLAIMS MATCH\]
- List all Bills for a Patient \[IB LIST ALL BILLS FOR PAT\]
- Insurance Payment Trend Report \[IB OUTPUT TREND REPORT\]
- BILL CHARGES screen of Third-Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]
- Third Party Active Bills screen of Third-Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]
- Third Party Inactive Bills screen of Third-Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]
- Third party Follow-Up Report \[IBJD FOLLOW-UP THIRD PARTY\]

The following reports and screens display the EEOB indicator next to the first party claim number when a match can be made to an associated third-party claim that has received an EEOB.

- Brief Account Profile \[PRCAY ACCOUNT PROFILE\]
- Full Account Profile \[PRCAY FULL ACCOUNT PROFILE\]
- First Party Follow-Up Report \[IBJD FOLLOW-UP FIRST PARTY\]
- List all Bills for a Patient \[IB LIST ALL BILLS FOR PAT\]
- List All Bills \[PRCA LIST ALL BILLS\]
- Bill Profile \[RCDP BILL PROFILE\]
- Bill Transactions \[RCDP BILL TRANSACTIONS\]

An example of the EEOB indicator, the “%” character, appearing before a claim number.

XXX-XXXXXX 03/01/11 XRAY CORP ACTIVE 127 62.00

%XXX-XXXXXX 03/01/11 PRUDENTIAL ACTIVE 127 55.00

%XXX-XXXXXX 01/06/11 AETNA NEW BILL -31 -31.00

## Receipt Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RECEIPT PROCESSING option generates a new warning message that will alert the user that the receipt cannot be processed when a claim on the ERA Worklist would result in a negative balance if the decrease adjustment were allowed against the claim.

Receipt Processing – Warning Message:

Receipt Profile May 15, 2017@15:57:59 Page: 1 of 1

Receipt \#: EXXXXXXXX Type of Payment: CHECK/MO PAYMENT

Deposit \#: Receipt Status: OPEN

ERA \#: XXXXXXXXXX ERA TTL: XXXXXX.XX FMS Document: NOTSENT

EFT \#: XXXXXXXXXX EFT TTL: XXXXXX.XX FMS Doc Status: NOT ENTERED

\# Account Pay Date Open By Edit By Pay Amt Proc Amt

1 442-K405IET 05/15/17 CM 4.38 0.00

-------- --------

TOTAL DOLLARS FOR RECEIPT 4.38 0.00

\+ Enter ?? for more actions

NP New Payment AP Account Profile PR Process Receipt

EP Edit Payment RR Reprint Receipt 21 (215 Report)

CP Cancel Payment WL Worklist (ERA) EA Exit Action

MP Move Payment CU Customize CR Entered Online

ER Edit Receipt

Select Action: Next Screen// PR Process Receipt

This option will process the payments for the receipt updating the AR

Package and generate the transfer receipt document to FMS. Any decrease

adjustments entered via the EDI Lockbox Worklist will also be generated.

Once a receipt has been processed, the receipt status will change to closed

and no further processing of the receipt can occur. If the FMS transfer

receipt document rejects, you can use this same option to reprocess the

receipt.

Generating automatic decrease adjustments from EDI Lbox Worklist

ARE YOU SURE YOU WANT TO CONTINUE?: YES// YES

Could not perform automatic decrease adj from ERA Worklist for

bill \# 442-KXXXXXX for amount of -6.55

> **WARNING:** Receipt cannot be processed.

Processing this receipt will cause this bill to have a negative balance

which is outside the scope of VA Accounting regulations.

Correct the error and reprocess this receipt .

43. This new message is generated only when the decrease adjustment would have caused a negative claim balance.

## Unposted EFT Override Acronym: OEFT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Unposted EFT Override option displays current warning messages or error messages for third party medical claims and pharmacy claims. A user can select either Medical or Pharmacy claims to file an override. A comment must be entered to explain why the override is occurring. An override allows unrestricted scratchpad creation for the day the override is filed.

44. The Unposted EFT Override option is locked with the security key, RCDPE AGED PMT.

The menu option to override unposted EFT posting prevention requires the user to hold security key RCDPE AUTO DEC.

## Identify Payers Acronym: IDP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Identify Payers option allows all users to see a list of all payer names and if they have been identified as Tricare, Pharmacy, or CHAMPVA only payers. The report can also be exported to Excel.

If the user has the RCDPE PAYER IDENTIFY security key they can set the Tricare, Pharmacy, and CHAMPVA indicators for payers.

Prompts:

Select EDI Lockbox (ePayments) \<TEST ACCOUNT\> Option: IDP Identify Payers

Filter by Date Added? NO//

Select payers to show. (A)ll, (P)harmacy, (T)ricare, (C)HAMPVA, (M)edical: A// ll

Payer List

Payer Pharmacy/Tricare/CHAMPVA Oct 10, 2017@13:04:57 Page: 1 of 16

Current Filter: ALL Payers

\# PAYER TIN Rx TR CV

1 AETNA XXXXXXXXXX Y

2 AETNA -CONTINENTAL LIFE INSURANCE COMPANY OF BRENTWOOD XXXXXXXXXX Y

3 AETNA AMERICAN CONTINENTAL INSURANCE COMPANY XXXXXXXXXX

4 AETNA GENWORTH LIFE AND ANNUITY INSURANCE XXXXXXXXXX

5 ALLEGIANCE BENEFIT PLAN MANAGEMENT XXXXXXXXXX Y

6 ALTIUS HEALTH PLANS A COVENTRY HEALTH CARE PLAN XXXXXXXXXX

7 AMERICAN FAMILY LIFE ASSURANCE COMPANY XXXXXXXXXX

8 AMERICAN FAMILY MUTUAL INSURANCE XXXXXXXXXX Y Y

9 AMERICAN NAT'L INS CO OF TEXAS XXXXXXXXXX

\+ Enter ?? for more actions \>\>\>

ED Edit Flags PH Flag Pharmacy CV Flag CHAMPVA

FI Filter TR Flag Tricare Q Quit

Select Action:Next Screen//

The Edit Flags, Flag Pharmacy, Flag Tricare, and Flag CHAMPVA actions will only be accessible to those with the RCDPE PAYER IDENTIFY security key.

## Remove Unbalanced Deposit Flag: UBD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remove Unbalanced Deposit Flag option allows users to remove an unbalanced flag from a deposit. To see a list of all unbalanced EDI Lockbox deposits, enter a question mark.

45. The Remove Unbalanced Deposit Flag option is locked with the security key, RCDPE AUTO DEC.

Prompts:

Select EDI LOCKBOX DEPOSIT NUMBER: ?

Answer with EDI LOCKBOX DEPOSIT NUMBER, or DEPOSIT NUMBER

Do you want the entire Unbalanced EDI LOCKBOX DEPOSIT List? Y (Yes)

Choose from:

T551598 03-21-2025 \$99.99

Select EDI LOCKBOX DEPOSIT NUMBER: T551598 2936 T551598 03-21-2025

UNBALANCED FLAG: YES// ?

Choose from:

1 YES

0 NO

UNBALANCED FLAG: YES// @

SURE YOU WANT TO DELETE? Y (Yes)

Select EDI LOCKBOX DEPOSIT NUMBER:

# EDI Lockbox (ePayments) Reports Menu Acronym: REP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Lockbox (ePayments) Reports Menu lists the available EDI Lockbox Reports.

EXC EDI Lockbox 3rd Party Exceptions

WL ERA Worklist

APAR Auto-Post Awaiting Resolution

MA Automatic Match EFTs to ERAs

MCR EEOB Move/Copy/Remove

MM EFT Manual Match

OEFT Unposted EFT Override

DUP Duplicate ERA Worklist

REFT Remove Duplicate EFT Deposits

REM Remove ERA from Active Worklist

REP EDI Lockbox (ePayments) Reports Menu

UN Unmatch An ERA

UP Update ERA Posted Using Paper EOB

ZB Mark 0-Balance EFT Matched

IDP Identify Payers

UBD Remove Unbalanced Deposit Flag

Select EDI Lockbox (ePayments) Option:

The sub-menus for the EDI Lockbox Reports are listed here and display after REP is entered above.

WORK Workload Reports ...

ADJR Adjustment Code Reports ...

RESR Additional Research Reports ...

AUDR Audit Reports ...

VP View/Print ERA

Select EDI Lockbox (ePayments) Reports Menu Option:

The sub-menu ‘WORK’ for the EDI Lockbox Reports lists the following Workload Reports:

DA EFT Daily Activity Report

EFT EFT Unmatched Aging Report

ERA ERA Unmatched Aging Report

PEO Pending EFT Override Report

UN Unapplied EFT Deposits Report

Select Workload Reports \<TEST ACCOUNT\> Option:

The sub-menu ‘ADJR’ for the EDI Lockbox Reports lists the following Adjustment Code Reports:

CR 835 CARC Data Report

PLB Provider Level Adjustments (PLB) Report

QS CARC/RARC Quick Search

TB CARC/RARC Table Data Report

Select Adjustment Code Reports \<TEST ACCOUNT\> Option:

The sub-menu ‘RESR’ for the EDI Lockbox Reports lists the following Additional Research Reports:

ETR EFT/ERA TRENDING Report

AB Active Bills With EEOB Report

NEO Negative ERA Line Report

Select Additional Research Reports \<TEST ACCOUNT\> Option:

The sub-menu ‘AUDR’ for the EDI Lockbox Reports lists the following Audit Reports:

AD Auto-Decrease Adjustment Report

FAD First Party COPAY Auto-Decrease Report

FAM First Party COPAY Manual vs Auto-Decrease Report

AP Auto-Post Report

APR Auto-Posted Receipt Report

APH Auto Parameter History Report

DUPR Duplicate EFT Deposits Audit Report

EAPA ERA Auto-Post Status Audit Report

ETA EFT Transaction Audit Report

EUO EFT Unlock Lockout Override Report

MCR EEOB Move/Copy/Remove Audit Report

EMA EEOBs Marked for Auto-Post Audit Report

POSR ERAs Posted with Paper EOB Audit Report

PX Payer Implementation Report

REMR Remove ERA from Active Worklist Audit Report

ESC ERA Status Change Audit Report

Select Audit Reports \<TEST ACCOUNT\> Option:

The sub-menu ‘VP’ for the EDI Lockbox Reports contains only the View / Print ERA option.

## EFT Daily Activity Report Acronym: DA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Summary EFT Daily Activity Report provides total data on all EFT deposits. The report can be run on-demand with detail by date or just the summary data for the date range. Detail format provides a detailed list of all EFT deposits received within the selected date range and the corresponding EFT payments from the payers comprising each deposit.

The following information appears on the EFT Daily Activity Statement.

- Deposit Ticket Information – including deposit number, date received, trace \#, which payment was from, CR document number, and TR document number(s).
- EFT’s that have been matched to an ERA.
- Accepted EFT’s represent total dollars posted to FUND 52870404 / Revenue Source Code 8NZZ.
- A minus sign to indicate if an EFT is a debit received by the payer, resulting in a debit voucher.
- The word UNBALANCED displays to indicate an unbalanced deposit.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the EFT Daily Activity Report on an as-needed basis to monitor electronic funds deposited to the US Treasury that are associated with the site.

When reviewed monthly, the user can ensure all deposits are in an ‘accepted’ status or in an appropriate ‘transmitted’ status. ALL deposits in a ‘rejected’ status must be corrected, to process the payments OR get collection credit for the funds.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the EFT Daily Activity Report in detail, proceed through the following steps:

Select EDI Lockbox (ePayments) Reports Menu Option - DA EFT Daily Activity Report

Select division: ALL//

(S)UMMARY OR (D)ETAIL?: D// DETAIL AND TOTALS

START DATE: 3/1/2017 (MAR 01, 2017)

END DATE: MAR 01, 2017// T (APR 14, 2017)

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//

Show EFTs with debits only? NO// YES

(B)alanced deposits, (U)nbalanced deposits or (A)LL?: All//

Export the report to Microsoft Excel? (Y/N): NO//

DISPLAY IN LISTMANAGER FORMAT (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

EDI LOCKBOX EFT DAILY ACTIVITY DETAIL REPORT Page: 1

RUN DATE: 04/30/17@16:56:14

DIVISIONS: ALL

PAYERS: SELECTED MED/PHARMACY/TRICARE/CHAMPVA:TRICARE

DATE RANGE: 03/01/17 - 03/01/17 (DATE DEPOSIT ADDED) DEBIT ONLY EFTs: NO

DEPOSITS: ALL

DEP \# DEPOSIT DT DEP AMOUNT FMS DEPOSIT STAT

EFT \# DATE PD PAYMENT AMOUNT ERA MATCH STATUS & DATE

EFT PAYER TRACE \# CR \#

PAYMENT FROM

TR \#

DEP RECEIPT \# DEP RECEIPT STATUS

===============================================================================

DATE EFT DEPOSIT RECEIVED: 03/01/17

TXXXXXX 03/01/17 UNBALANCED 75.00 ACCEPTED

2846.1 10/02/24 76.36 MATCHED/ERA \#XXXXX 03/01/17

ABCXXXXXXXXXX CR-XXXXXXXXXX

FEDERAL EMPLOYEES HEALTH BENEFIT A COVENTRY HEALTH CARE PLAN/XXXXXXXXXX

TR-XXXXXXXXXX

EXXXXXXXX ACCEPTED

To run the EFT Daily Activity Report in summary, proceed through the following steps:

Select division: ALL//

(S)UMMARY OR (D)ETAIL?: D// SUMMARY TOTALS ONLY

START DATE: 3/1/2017 (MAR 01, 2017)

END DATE: MAR 1,2017// (MAR 01, 2017)

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EDI LOCKBOX EFT DAILY ACTIVITY SUMMARY REPORT Page: 1

RUN DATE: 04/30/17@17:10:48

DIVISIONS: ALL

PAYERS: SELECTED MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

DATE RANGE: 03/01/17 - 03/01/17 (Date Deposit Added) DEBIT ONLY EFTs: NO

===============================================================================

\*\*TOTALS FOR DATE: 03/01/17 \# OF DEPOSIT TICKETS RECEIVED: 1

TOTAL AMOUNT OF DEPOSITS RECEIVED: \$737.58

DEPOSIT AMOUNTS SENT TO FMS:

ACCEPTED: \$737.58

QUEUED: \$0.00

ERROR/REJECT: \$0.00

NOT IN FMS: \$0.00

DEBIT VOUCHERS: \$0

\# EFT DEBIT VOUCHERS: 0

\# EFT PAYMENT RECORDS: 1

\# EFT PAYMENTS MATCHED: 1

\*\*\*\* TOTALS FOR DATE RANGE: \# OF DEPOSIT TICKETS RECEIVED: 1

TOTAL AMOUNT OF DEPOSITS RECEIVED: \$737.58

DEPOSIT AMOUNTS SENT TO FMS:

ACCEPTED: \$737.58

QUEUED: \$0.00

ERROR/REJECT: \$0.00

NOT IN FMS: \$0.00

DEBIT VOUCHERS: \$0

\# EFT DEBIT VOUCHERS: 0

\# EFT PAYMENT RECORDS: 1

\# EFT PAYMENTS MATCHED: 1

\*\*\*\*\* END OF REPORT \*\*\*\*\*

Enter RETURN to continue or '^' to exit:

## EFT Unmatched Aging Report Acronym: EFT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EFT Unmatched Aging Report contains a list of all Electronic Funds Transfer (EFT) records that have not been successfully matched to ERAs or to paper EOBs within the user-specified number of days. Within EDI Lockbox Site Parameters, each site can set the number of days an EFT should wait before appearing on this report. The default parameter is set at 5 days.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the EFT Unmatched Aging Report on a regular basis, as determined by the site, to monitor outstanding electronic funds requiring a match to an ERA or even a paper EEOB.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the summary EFT Unmatched Aging Report, proceed with the following selections.

Select EDI Lockbox Reports Menu Option: EFT EFT Unmatched Aging Report

Start date: T-1000 (AUG 07, 2014)

End date: AUG 7,2014// T (MAY 03, 2017)

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//SPECIFIC

Select Insurance Company Name: TRICARE WEST XXXXXXXXXX

Export the report to Microsoft Excel? (Y/N): NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

EFT UNMATCHED AGING REPORT Page: 1

RUN DATE: 5/3/17@15:21:37

PAYERS: SELECTED MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

DATE RANGE: 8/7/14 - 5/3/17 (DATE EFT FILED)

AGED

DAYS TRACE \# DEP DATE

DEPOSIT FROM/ID

FILE DATE DEPOSIT AMOUNT DEP#/EFT# DEPOSIT POST STATUS

================================================================================

Totals:

Number Aged Electronic EFT Messages Found: 1

Amount Aged Electronic EFT Messages Found: \$66.76

================================================================================

637 XXXXXXXX 3/18/15

FEDERAL EMPLOYEES HEALTH BENEFIT A COVENTRY HEALTH CARE PLAN/XXXXXXXXXX

8/5/15 66.76 XXXXXXXXX/2101.2 Posted to 8NZZ 8/6/15

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## ERA Unmatched Aging Report Acronym: ERA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces the ERA aging report containing a list of all Electronic Remittance Advice (ERA) records that have not been successfully matched to electronic EFTs within the user-specified number of days. Within EDI Lockbox Site Parameters, each site can set the number of days an ERA should wait before appearing on this report. An indicator of “x” displays before the Aged Days if an exception exists for the ERA.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the ERA Unmatched Aging Report on a regular basis, as determined by the site, to monitor outstanding electronic remittance advices requiring a match to an EFT or paper check.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the summary ERA Unmatched Aging Report, proceed with the following selections:

Select EDI Lockbox Reports Menu Option: ERA ERA Unmatched Aging Report

Select division: ALL//

START DATE: 1/1/2005 (JAN 01, 2005)

END DATE: JAN 1,2005// T (SEP 20, 2011)

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: A// LL

RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//

Include Zero payment amounts? (Y/N): YES//

Display Adjustment/Code Information? (Y/N): NO//

Export the report to Microsoft Excel? (Y/N): NO// EXPORT THE REPORT TO Microsoft Excel (Y/N): ? NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

ERA UNMATCHED AGING REPORT Page: 1

RUN DATE/TIME: 9/20/11@14:44:15

DIVISIONS: ALL

PAYERS: SELECTED MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

DATE RANGE: 1/1/05 - 9/20/11 (ERA FILE DATE)

AGED

DAYS TRACE \#

PAYMENT FROM/ID ERA DATE

FILE DATE AMOUNT PAID ERA \#

===============================================================================

TOTALS:

NUMBER AGED ELECTRONIC ERA MESSAGES FOUND: 155

AMOUNT AGED ELECTRONIC ERA MESSAGES FOUND: \$55,599.63

===============================================================================

1672 XXXXXXXXXX

FIRST HEALTH/XXXXXXXXXX 2/17/07

2/21/07 10.56 14102

x1672 XXXXXXXXXX

MAIL HANDLERS BENEFIT PLAN/XXXXXXXXXX 2/17/07

2/21/07 18.53 14106

Enter RETURN to continue or '^' to exit:

## Pending EFT Override Report Acronym: PEO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces the Pending EFT Override Report containing all EFTs creating the EFT locks up, including an automatic list when the EFT locks up override option was used and includes the EFT override comments.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the Pending EFT Override Report whenever locked reports are encountered to help troubleshoot and resolve locked reports.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the summary Pending EFT Override Report proceed with the following selections:

Select Workload Reports Option: PEO Pending EFT Override Report

Medical Override not active for today's date

Aged EFT days before Medical posting prevented = 30

List the report in Microsoft Excel format? NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

Pending EFT Override Report - Page 1 Run Date: Dec 07, 2018@09:06:08

Sorted by Aged Days, Comment: testing

Medical Override Date: OCT 31, 2018@07:04:46 User: USER,ONE

Number of Days (Age) of Unposted EFTs to prevent posting: 30

EFT Trace#

ERA Match Status EFT Received Aged Amount

===============================================================================

Total Number of Unposted EFTs: 68

Total Amount of Unposted EFTs: \$251,726.33

===============================================================================

XXXX.X XXXXXXXXXXX

XXXXX MATCHED Jul 29, 2015 1227 \$16,582.33

XXXX.XX XXXXXXXXXX

XXXXX MATCHED Aug 05, 2015 1220 \$1,514.70

XXXX.XX XXXXXXXX

None PAPER EOB MATCH Aug 05, 2015 1220 \$66.76

XXXX.X XXXXXXXXXXXXX

XXXXX MATCHED Aug 06, 2015 1219 \$131.57

Press ENTER to continue, '^' to exit:

## EFT / ERA Trending Report Acronym: ETR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERA / EFT TRENDING Report is used to display metrics on \#ERAs, \#EEOBs (Payment EEOBs, Unmatched EEOBs, Zero Payment EEOBs), \#EFTs with \#days between ERA and EFT transactions. The report can be run for ALL payers or selected payer(s).

The prompt for “SORT BY (P)AYER or (A)MOUNT OF PAYMENT” will only display if the MAIN report is selected.

This report can also be found under the EDI Diagnostics Measures Reports menu.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run this report on an as-needed basis.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the ERA/EFT TRENDING Report, proceed with the following selections:

Prompts:

EFT/ERA TRENDING Report

Select division: ALL//

(A)UTO-POSTED, (M)MANUALLY POSTED, (B)OTH: BOTH// ?

Enter 'A' to include only auto-posted entries

'M' to include only manually posted entries

'B' to include both

Select one of the following:

A AUTO-POSTED

M MANUALLY POSTED

B BOTH

(A)UTO-POSTED, (M)ANUALLY POSTED, (B)OTH: BOTH//

(P)AYMENT EEOBs, (U)NMATCHED EEOBs, (Z)ERO PAYMENT EEOBs or (A)LL: ALL//

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

Select Insurance Companies by NAME or TIN: TIN//

RUN REPORT FOR (A)LL OR (S)PECIFIC INSURANCE COMPANIES?: ALL//

Select RATE TYPE NAME: 8 REIMBURSABLE INS. Who's Responsible: INSURER

Include (A)LL Claims or only (C)LOSED Claims: ALL//

Print (M)AIN Report, (S)UMMARY by Payer or (G)RAND TOTALS ONLY: G// MAIN

SORT BY (P)AYER or (A)MOUNT OF PAYMENT: PAYER//

Start with DATE: 12/24/24 (DEC 24, 2024)

Go to DATE: 1/23/25// (JAN 23, 2025)

Export the report to Microsoft Excel? (Y/N): NO//

Main Report with Header and Sub-header:

EFT/ERA TRENDING REPORT PAGE 1

ALL DIVISIONS ALL TINS MEDICAL/PHARMACY/TRICARE/CHAMPVA: ALL MANUAL/AUTOPOST: BOTH Claims: ALL

DATE RANGE: 12/24/24 - 1/23/25 RUN DATE: 1/23/25@12:05:54 PAYMENT/UNMATCHED/ZERO PAY: ALL

PAYER NAME/TIN

-----------------------------------------------------------------------------------------------------------------------------------

UNITED HEALTH CARE/1113283886

-----------------------------------------------------------------------------------------------------------------------------------

CLAIM# DOS AMT BILLED AMT PAID BILLED ERA/EOB REC'D EFT/PMT REC'D POSTED TRACE \# AUTOPOST/MANUAL

ETRANS TYPE ERA# \#EEOBS EFT# \#DAYS:(BILL/ERA) \#DAYS:(ERA/EFT) \#DAYS:(ERA+EFT/POSTED) TOTAL \#DAYS(BILL/POSTED)

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - AUTOPOST \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

K70000N 8/5/06 684.99 684.99 11/13/06 1/10/25 1/10/25 1/10/25 6721540081 AUTOPOST

ERA/EFT 93010 1 36294 6633 0 0 6633

K70001A 7/27/06 32.83 32.83 9/27/06 12/30/24 12/30/24 12/30/24 6720430187 AUTOPOST

ERA/EFT 93007 1 36291 6669 0 0 6669

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* UNMATCHED ERA - UNPOSTED \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

K70002B 8/5/06 684.99 0.00 11/13/06 1/10/25 1/10/25 N/A 6721540081 UNPOSTED

ERA/EFT 93010 1 N/A 6633 N/A N/A N/A

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ZERO PAYMENTS \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

K70007D 8/5/06 684.99 0.00 11/13/06 1/10/25 1/10/25 N/A 6721540089 UNPOSTED

ERA/EFT 93010 1 36297 6633 0 N/A N/A

-----------------------------------------------------------------------------------------------------------------------------------

EFT/ERA TRENDING REPORT PAGE 2

ALL DIVISIONS ALL TINS MEDICAL/PHARMACY/TRICARE/CHAMPVA: ALL MANUAL/AUTOPOST: BOTH Claims: ALL

DATE RANGE: 12/24/24 - 1/23/25 RUN DATE: 1/23/25@12:05:54 PAYMENT/UNMATCHED/ZERO PAY: ALL

-----------------------------------------------------------------------------------------------------------------------------------

GRAND TOTALS ALL PAYERS

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - AUTOPOST \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* UNMATCHED E0B - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 00.00

TOTAL AMOUNT PAID 00.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 6633

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 00.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ZERO PAYMENTS - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 4

TOTAL AMOUNT BILLED 50.00

TOTAL AMOUNT PAID 0

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 20

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 1

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 0

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\* END OF REPORT \*\*\*\*\*Report Totals (Summary):

EFT/ERA TRENDING REPORT PAGE 1

ALL DIVISIONS ALL TINS MEDICAL/PHARMACY/TRICARE/CHAMPVA: ALL MANUAL/AUTOPOST: BOTH Claims: ALL

DATE RANGE: 12/24/24 - 1/23/25 RUN DATE: 1/23/25@12:05:54 PAYMENT/UNMATCHED/ZERO PAY: ALL

------------------------------------------------------------------------------------

PAYER NAME/TIN

UNITED HEALTH CARE/1113283886

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - AUTOPOST \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* UNMATCHED E0B - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 50.00

TOTAL AMOUNT PAID 50.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/EOB 20

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 1

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 50.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ZERO PAYMENTS - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 4

TOTAL AMOUNT BILLED 50.00

TOTAL AMOUNT PAID 0

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 20

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 1

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 0

------------------------------------------------------------------------------------

GRAND TOTALS ALL PAYERS

------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - AUTOPOST \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* UNMATCHED E0B - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 50.00

TOTAL AMOUNT PAID 50.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/EOB 20

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 1

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 50.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ZERO PAYMENTS - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 4

TOTAL AMOUNT BILLED 50.00

TOTAL AMOUNT PAID 0

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 20

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 1

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 0

------------------------------------------------------------------------------------

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## Unapplied EFT Deposits Report Acronym: UN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces a list of EFT deposits that have EFT detail records whose funds have not been applied to bills in A/R. These funds remain in FUND 5287.4, RSC 8NZZ. Only those EFTs that have either not been matched to an ERA or have been matched to an ERA, but the payment receipt has not been posted to FMS, will appear on this report.

EFTs posted using a paper EOB will continue to show on this report. This will be updated with a future enhancement.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user will run the Unapplied EFT Deposits Report on a regular basis, as determined by the facility, to monitor funds outstanding in FUND 5287.4, REVENUE SOURCE CODE 8NZZ.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the Unapplied EFT Deposits Report, proceed with the following selections:

Unapplied EFT Deposits Report Page: 2

Run Date: 12/12/16@16:42:39 MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

Date Range: 7/28/89 - 12/12/16 (Deposit Date)

TOTAL NUMBER OF UNAPPLIED DEPOSITS: 13

TOTAL AMOUNT OF UNAPPLIED DEPOSITS: \$8,274.78

DEPOSIT#/EFT# DEPOSIT DATE TOT AMT OF DEPOSIT TOT AMT UNPOSTED

PAYER/ID

TRACE \# PAYMENT AMT RECEIPT \#

ERA MATCHED FMS DOC \#/STATUS

=============================================================================

XXXXXX 3/4/11 1345.68 1345.68

FEDERAL EMPLOYEES HEALTH BENEFIT A COVENTRY HEALTH CARE PLAN/ XXXXXXXXXX

XXXXXXXXXX/XXXX.X 880.98 E XXXXXXXX

MATCHED TO ERA \#: XXXXX TR- XXXXXXXXXX - TRANSMITTED

Press enter to continue, '^' to exit:

To run the Unapplied EFT Deposits Report in Grand Totals mode, proceed with the following selections:

(D)ETAIL REPORT or (G)RAND TOTAL?: D// GRAND TOTAL

DEVICE: HOME// HOME (TERMINAL) Right Margin: 80//

Unapplied EFT Deposits Report Page: 2

Run Date: 12/12/16@16:42:39 MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

Date Range: 7/28/89 - 12/12/16 (Deposit Date)

TOTAL NUMBER OF UNAPPLIED DEPOSITS: 13

TOTAL AMOUNT OF UNAPPLIED DEPOSITS: \$8,274.78

Press enter to continue, '^' to exit:

## Active Bills with EEOB Report Acronym: AB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was created to enable one to manage ACTIVE third-party insurance claims that have an EDI Lockbox EEOB, but have a balance remaining. All active bills that have EEOBs associated, and have a balance \>0, will be displayed, sorted by insurance company.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run this report on a routine basis, as determined by the site, to identify any payments that have been posted to accounts without any contractual adjustments and analysis having been performed. This report is a very useful tool for keeping Account Receivables from becoming aged.

The ERA Unmatched Aging report should be current before working this report.

46. It is recommended that the report is queued, since it will take a while to print.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the Active Bills with an EEOB \> 0 report, proceed with the following steps:

Select EDI Lockbox Reports Menu Option: AB  Active Bills With EEOB Report

Select division: ALL//

(CHAMPVA),(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/ \<=new prompt/Default=ALL

RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//

RUN REPORT FOR (P)AYMENT EEOBs or (Z)ERO PAYMENT EEOBs or (A)LL: ALL//

WITHIN INS CO, SORT BY (P)ATIENT NAME OR (L)AST 4 OF SSN?: PATIENT NAME//

SORT PATIENT NAME (F)IRST TO LAST OR (L)AST TO FIRST?: FIRST TO LAST//

START DATE (RECEIVED): t-30 (DEC 03, 2014)

END DATE (RECEIVED): DEC 3,2014// t (JAN 02, 2015

Export the report to Microsoft Excel? (Y/N): NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// VIRTUAL TELNET Right Margin: 80//

EDI LOCKBOX ACTIVE BILLS W/EEOB REPORT Page: 1

RUN DATE: 1/2/15@08:39:45

DIVISIONS: ALL

PAYERS: SELECTED MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

DATE RANGE: 12/03/14 - 01/02/15 PAYMENT TYPE:TRICARE

PATIENT NAME SSN BILL#

INS CO NAME BALANCE AMT BILLED AMT PAID

TRACE# DT REC'D DT POST

================================================================================

XXXXXXXXXXXXXXXXXX XXXX 626KXXXXXX

AETNA\* 14.53 14.53 0.00

XXXXXXXXXXXXXXX 9/16/13 9/25/13

XXXXXXXXXXXXXXXXXXX XXXX 626KXXXXXX

AETNA\* 53.66 53.66 0.00

XXXXXXXXXXXXXXX 7/9/14 7/14/14

XXXXXXXXXXXXXXXXXXX XXXX 626KXXXXXX

AETNA\* 46.31 46.31 0.00

XXXXXXXXXXXXXXX 7/21/14 8/5/14

## Auto Decrease Adjustment Report Acronym: AD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was created to monitor EEOBs that have been automatically decreased to a zero balance by the system.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run this report on a routine basis, as determined by the site, to identify any EEOB with a contractual decrease adjustment performed automatically by the system.

## Auto-Post Report Acronym: AP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was created to monitor EEOBs that have been automatically processed by the nightly job to create and process a receipt. This report has filter questions for Medical, Pharmacy, TRICARE, CHAMPVA, or ALL claim types and allows the user to filter and sort by Insurance Company Name or TIN.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run this report on a routine basis, as determined by the site, to identify any EEOB that has a processed receipt resulting from the nightly auto-posting job.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the Auto-Posted Report proceed through the following steps:

Auto-Post Report (Detail):

EDI LOCKBOX AUTO-POST REPORT - DETAIL Print Date: 11/26/18@13:21:03 Page: 1

DIVISIONS: ALL

CLAIM TYPE: ALL SORTED BY: PAYER TIN

TINS : ALL

AUTOPOST POSTING RESULTS FOR DATE RANGE: 08/18/18 - 11/26/18

=================================================================================================

PATIENT NAME/SSN ERA# DT REC'D DT POST BILL# AMT BILLED AMT PAID BALANCE %COLL

=================================================================================================

DIVISION: ANYTOWN VAMROC/XXX

-----------------------------------------------------------------------------------------------------------------------------------

PAYER: XXXXXXXXXX/AETNA

-----------------------------------------------------------------------------------------------------------------------------------

PATIENT,NUMBER ONEONE/XXXX XXXXX 09/18/18 09/18/18 KXXXXXX 14.84 568.01 46.83 3827.56%

DEP#:XXXXXXXXX EFT#:XXXXXX.XX RECEIPT#: EXXXXXXXXXXX TRACE#:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Auto-Post Report (Summary):

EDI LOCKBOX AUTO-POST REPORT - SUMMARY Print Date: 11/26/18@08:20:07 Page: 1

DIVISIONS: ALL

CLAIM TYPE: ALL SORTED BY: PAYER TIN

TINS : ALL

AUTOPOST POSTING RESULTS FOR DATE RANGE: 08/18/18 - 11/26/18

=====================================================================================================================

PATIENT NAME/SSN ERA# DT REC'D DT POST BILL# AMT BILLED AMT PAID BALANCE %COLL

=====================================================================================================================

DIVISION: GREELEY/442GD

-----------------------------------------------------------------------------------------------------------------------------------

SUBTOTALS FOR PAYER: XXXXXXXXXX/AETNA GENWORTH LIFE AND ANNUITY INSURANCE 605.19 4022.26 653956.45 664.63%

COUNT 3 3 3

MEAN 201.73 1340.75 217985.48

## Auto-Posted Receipt Report Acronym: APR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review this report on a regular basis, as determined by the site, to display all auto-posted receipts to ensure payments are posted to patient’s 3rd party claims.

If payments are 'hung up' and not processed timely, veterans’ copayments are not credited in a timely fashion.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the Auto-Posted Receipt Report proceed through the following steps:

Select EDI Lockbox Reports Menu Option - APR AUTO-POSTED RECEIPT REPORT

Select division: ALL//

(A)uto-Post Date or (E)RA Date Received? (A/E): A//

START DATE: 3/1/2017 (MAR 01, 2017)

END DATE: MAR 01, 2017// T (MAY 01, 2017)

Select ERAs to be Displayed: Both// ??

Enter 1 to only display Posted Receipts.

Enter 2 to only display ERAs with missing receipts.

Enter 3 to display all receipts.

Select one of the following:

1 Posted/Completed Receipts

2 Missing Receipts

3 Both

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

Run Report for (A)LL, (S)PECIFIC, or (R)ANGE of Insurance Companies?: ALL//

Sort by (D)ate or (M)issing Receipts: D//

Display in List Manager format? (Y/N): NO//

Export the report to Microsoft Excel? NO//

DEVICE: HOME//

AUTO-POSTED RECEIPT REPORT May 01, 2017@13:08:17 Page: 1

FILTERS: All Divs; Selected Payers;TRICARE Auto-Post Date 03/01/17-05/01/17

ERA: All Receipts SORT: Auto-Post Date

DATE DATE

RECEIVED POSTED RECEIPT USER AMOUNT FMS DOC

--------------------------------------------------------------------------------

Payer: AETNA

ERA: XXXXX ERA Total: 737.58

Receipt Total: 737.58

Trace \#: XXXXXXXXXXXXX

03/01/17 03/01/17 EXXXXXXXX 737.58 TR-XXXXXXXXXX

ERA: XXXXX ERA Total: 371.72 \* Missing Receipts \*

Receipt Total: 177.72

Trace \#: XXXXXXXXXXXXX

03/17/17 \* Missing \* POST 194.00

03/17/17 03/17/17 EXXXXXXXXX POST 177.72 TR-XXXXXXXXXX

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## Auto Parameter History Report Acronym: APH

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Auto Parameter History Report shows the Date / Time, User, Parameter, Old Value, and New Value of any Auto-Activity Parameter changes. Use this report to identify the historical changes and / or trends related to any Auto-Activity Parameter. The report can be filtered by Start / End Date.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the Auto Parameter History Report, proceed through the following steps:

Auto Parameter History Report

Start Date: T// t-10 (NOV 10, 2018)

End Date: T// t (NOV 20, 2018)

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

Auto Parameter History Report Page: 1

RUN DATE: 11/20/18@11:43:25

DATE RANGE: 11/10/18 - 11/20/18

Date/Time Edited User Values

Parameter Old New

================================================================================

11/13/18@09:56:37 PATIENT,ONE

TRICARE FLAG (TRICARE WEST) NO YES

11/15/18@11:04:21 PATIENT,ONE

AUTO-POST RX CLAIMS ENABLED NO YES

11/15/18@11:18:49 PATIENT,ONE

TRICARE EFT POST PREVENT DAYS 14 30

11/15/18@11:19:14 PATIENT,ONE

TRICARE EFT POST PREVENT DAYS 30 14

11/15/18@11:19:31 PATIENT,ONE

AUTO-POST RX CLAIMS ENABLED YES NO

11/16/18@12:51:02 PATIENT,ONE

AUTO-POST RX CLAIMS ENABLED NO YES

AUTO-DECREASE RX CLAIMS ENABLED NO YES

AUTO-DECREASE RX AMT DEFAULT 250.00 7,000.00

Press enter to continue, '^' to exit:

Auto Parameter History Report Page: 2

RUN DATE: 11/20/18@11:43:25

DATE RANGE: 11/10/18 - 11/20/18

Date/Time Edited User Values

Parameter Old New

================================================================================

11/16/18@12:51:02 PATIENT,ONE

AUTO-POST TRICARE CLAIMS ENABLED NO YES

AUTO-DECREASE TRICARE CLAIMS ENABLED NO YES

AUTO-DECREASE TRICARE AMT DEFAULT 250.00 7,000.00

11/16/18@12:51:02 PATIENT,ONE

AUTO-POST NOPAY TRICARE CLAIMS ENABLED NO YES

AUTO-DECREASE NOPAY TRICARE CLAIMS ENABLED NO YES

AUTO-DECREASE NOPAY TRICARE AMT DEFAULT 250.00 7,000.00

11/16/18@13:51:24 PATIENT,ONE

AUTO-DECREASE AMT DEFAULT 250.00 7,000.00

CARC AUTO DECREASE NO-PAY (45) NO YES

CARC DECREASE AMOUNT NO-PAY (45) 1.00 7,000.00

Press enter to continue, '^' to exit:

## CARC Data Report Acronym: CR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run this report on a routine basis, as determined by the site, to determine any CARC codes returned on 835 forms by payers.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the 8335 CARC Data report, proceed with the following steps:

Select EDI Lockbox Reports Menu Option: CR 835 CARC Data Report

Select Division: ALL//

(S)UMMARY or (D)ETAIL FORMAT: SUMMARY// *\<=Defaults to SUMMARY*

SELECT (C)ARC, (R)ANGE of CARCs or (A)LL: ALL//

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: A// LL

Run Report for (A)LL,(S)PECIFIC,or (R)ANGE of Insurance Companies?: ALL//SPECIFIC

Select Insurance Company NAME: TRICARE WEST XXXXXXXXXX

SORT BY (C)ARC or (P)AYER?: CARC// *\<=Defaults to CARC*

START DATE: T//090115

END DATE: T//091615

DEVICE: HOME// UCX/TELNET Right Margin: 80//

## Duplicate EFT Audit Report Acronym: DUPR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the Duplicate EFT Audit Report on a regular basis, as determined by the site, to monitor usage of the Remove Duplicate EFT Deposits option.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the Duplicate EFT Audit report, proceed with the following selections:

Select EDI Lockbox Reports Menu Option: dupr Duplicate EFT Deposits Audit Report START DATE: t-60 (NOV 06, 2020)

END DATE: JAN 05,2021// t (JAN 05, 2021)

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: A// LL

EXPORT THE REPORT TO Microsoft Excel (Y/N): ? NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

Duplicate EFT Deposits - Audit Report Page: 1

RUN DATE: 1/5/21@13:40:20 CHAMPVA/MEDICAL/PHARM/TRICARE: ALL

Date Range: 11/06/20 - 01/05/21 (DATE EFT REMOVAL)

Deposit#/EFT# Trace \#

Payer Name Date/Time User Who

Amount Removed Removed Removal Type

================================================================================

TXXXXXX/XXXX.X XXXXXXXXXXXXX

THE MEGA LIFE AND HEALTH INSURANCE XXXXXXXXXXXXXXXXXXXXXXXXX DUPLICATE EFT

194.00 11/24/20@09:12:49 ARClerk,One

Justification Comments: OK

TXXXXXX/XXXX.X XXXXXXXXXXXXX

AETNA -CONTINENTAL LIFE INSURANCE COMPANY OF BRENTWOOD MILLENIUM EFT

186.66 11/24/20@14:43:37 ARClerk,One

Justification Comments: DUPLICATE EFT

Total number of duplicates removed: 2

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## ERA Auto-Post Status Audit Report Acronym: EAPA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run this report on a routine basis, as determined by the site, to display a detailed audit trail listing of ERA AUTO POST STATUS changes.

The report allows the user to run an audit for a single ERA or ALL ERAs for a date range. Report will be sorted by ERA then by date / time. Specific data elements shall include Date / Time, User, ERA#, STATUS (old / new) and Reason text.

The Reason text will be a summary of the “process” that caused the ERA Status to be changed along with the “outcome” of the change.

Example Reason text messages are listed below with some of these messaged displayed in the report mockup.

Auto Matching: Marked as Auto-Post Candidate

Auto Posting: Removed from Auto Posting-Unable to create scratchpad

Auto Posting: Removed from Auto Posting-ERA level Adjustment(s)

Auto Posting: Removed from Auto Posting-+/- pairs do not balance

Auto Posting: Removed from Auto Posting-Unable to create receipt

Auto Posting: Removed from Auto Posting-Error in receipt processing

Auto Posting: ERA posted successfully

Auto Posting: Some of the ERA lines went to APAR

Auto Posting: Previously processed ERA posting attempt

Exceptions: Marked as Auto-Post Candidate

Exceptions: Not Marked as Auto-Post Candidate-\<Reasons listed in section 2.9.1.2\>

Worklist: Marked as Auto-Post Candidate

Worklist: Not Marked as Auto-Post Candidate-\<Reasons listed in section 2.9.1.2\>

Manual Match: Marked as Auto-Post Candidate

Manual Match: Not Marked as Auto-Post Candidate-\<Reasons listed in section 2.9.1.2\>

Unmatch: Removed as Auto-Post Candidate

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the ERA Auto-Post Status Audit report, proceed with the following steps:

Select EDI Lockbox (ePayments) Reports Menu \<TEST ACCOUNT\> Option: ERA Auto-Post Status Audit Report

SELECT (S)ingle ERA or (A)LL: ALL//

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: A// LL

START DATE: T// (DEC 03, 2015)

END DATE: T// (DEC 03, 2015)

DEVICE: HOME// HOME (CRT) Right Margin: 80//

The ERA Status Change Audit report will display as follows:

EDI Lockbox ERA Status Change Audit Report Page: 1

RUN DATE: DEC 03, 2015@14:39:45 MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

DATE RANGE: 12/03/2015 - 12/03/2015

ERA# Date/Time Edited Status (Old/New) User

Reason Text

--------------------------------------------------------------------------------

XXXXX 12/03/15@01:54:13 NULL UNPOSTED POSTMASTER

Auto Matching: Marked as Auto-Post Candidate

XXXXX 12/03/15@01:55:18 NULL NULL POSTMASTER

Auto Posting: Removed from Auto Posting-ERA level Adjustment(s)

XXXXX 12/03/15@01:56:22 UNPOSTED PARTIAL POSTMASTER

Auto Posting: Some of the ERA lines went to APAR

XXXXX 12/03/15@01:58:16 UNPOSTED COMPLETE POSTMASTER

Auto Posting: ERA posted successfully

XXXXX 12/03/15@01:59:44 PARTIAL COMPLETE POSTMASTER

Auto Posting: ERA posted successfully

XXXXX 12/03/15@12:10:12 NULL NULL REDACTED

Exceptions: Not Marked as Auto-Post Candidate-ERA not matched

XXXXX 12/03/15@12:22:47 NULL NULL REDACTED

Exceptions: Not Marked as Auto-Post Candidate-Invalid Bill Number Exception(s)

XXXXX 12/03/15@12:31:22 NULL UNPOSTED REDACTED

Exceptions: Marked as Auto-Post Candidate

XXXXX 12/03/15@12:40:47 NULL UNPOSTED REDACTED Worklist: Marked as Auto-Post Candidate

XXXXX 12/03/15@13:11:33 COMPLETE COMPLETE REDACTED

Worklist: Not Marked as Auto-Post Candidate-Already completely Auto-Posted

XXXXX 12/03/15@13:44:44 NULL UNPOSTED REDACTED

Manual Match: Marked as Auto-Post Candidate

XXXXX 12/03/15@13:55:55 NULL NULL REDACTED

Manual Match: Not Marked as Auto-Post Candidate-+/- pairs do not balance

XXXXX 12/03/15@14:12:22 UNPOSTED NULL REDACTED Unmatch: Removed as Auto-Post Candidate

## EFT Transaction Audit Report Acronym: ETA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run this report on a routine basis, as determined by the site, to list all actions taken place for a single EFT.

For example: If a user matched the EFT to a paper EOB, the report would list the date, user, and deposit ticket number. If another user unmatched / matched the EFT to an ERA, this data would also be displayed on the report. This report also identifies which EFTs are ready to lock up the system.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EFT Transaction Audit Report allows the user to generate SUMMARY or DETAIL EFT Data as described below. If the report is run summary mode, the user is then asked if they want to sort the EFTs by date or by deposit number. If deposit number is chosen, all the EFTs for the selected deposit number and deposit date will be shown even if they were received on multiple days. This report also identifies deposits that are not in balance.

To run the EFT Transaction Audit report, proceed with the following steps:

Summary Report By Date:

Select EDI Lockbox (ePayments) Reports Menu \<TEST ACCOUNT\> Option: EFT Transact

ion Audit Report

(S)ummary or (D)etail Report format? SUMMARY// Summary Information Only

(E)FTs by Date or (D)eposit? DEPOSIT// EFTS by Date

Start Date: T// 090115 (SEP 01, 2015)

End Date: T// (SEP 17, 2015)

Do you want to capture report data for an Excel document? NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EFT TRANSACTION AUDIT REPORT - SUMMARY Page: 1

RUN DATE: 9/17/15@11:21:24

DATE RANGE: 9/1/15 - 9/17/15 (DATE DEPOSIT ADDED)

EFT# DATE RECVD DEPOSIT# EFT TOTAL AMT DATE MATCHED DATE POSTED

TRACE \#

PAYER NAME/ID

--------------------------------------------------------------------------------

\*\*XXXX.X 09/01/15 TXXXXXXXX 2727.50 09/01/15 09/01/15

XXXXXXXXXXXXXX

AETNA/XXXXXXXXXXX

\*XXXX.X 09/08/15 TXXXXXXXX 9000.00 09/09/15 09/08/15

XXXXXXXXXXXXXX

AETNA/XXXXXXXXXXX

\*XXXX.X 09/15/15 TXXXXXXXX 2202.50 09/15/15 09/15/15

XXXXXXXXXXXXXX

AETNA/XXXXXXXXXXX

XXXX.X 09/15/15 TXXXXXXXX 2202.50 \<No History\> 09/15/15

XXXXXXXXXXXXXX

AETNA/XXXXXXXXXXX

XXXX.X 09/15/15 TXXXXXXXX 2202.50 \<No History\> 09/15/15

XXXXXXXXXXXXXX

AETNA/XXXXXXXXXXX

Enter RETURN to continue or '^' to exit:

Summary Report sorted by Deposit Number:

(S)ummary or (D)etail Report format? SUMMARY// Summary Information Only

(E)FTs by Date or (D)eposit? DEPOSIT// Deposit Number

Enter Deposit Number: XXXXXXXXXX

Select Deposit:

1 XXXXXXXXXX on: 09/01/2021 \*\*UNBALANCED\*\*

2 XXXXXXXXXX on: 06/18/2015

CHOOSE 1 - 2: 1

Do you want to capture report data for an Excel document? NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EFT TRANSACTION AUDIT REPORT - SUMMARY Page: 1

RUN DATE: 9/30/21@06:45:20

DEPOSIT \#: XXXXXXXXX Deposit Date 9/1/21 \*\*UNBALANCED\*\*

EFT# DEPOSIT# DEPOSIT DATE DATE RECEIVED EFT TOTAL AMT

TRACE \#

PAYER NAME/ID

--------------------------------------------------------------------------------

XXXX.X XXXXXXXXX 09/01/21 09/15/21 536.21

XXXXXXXXXX

ANTHEM BLUE NH5F/XXXXXXXXXX

XXXX.X XXXXXXXXX 09/01/21 09/15/21 4502.38

XXXXXXXXXXXXXXX

CIGNA/ XXXXXXXXXX

XXXX.X XXXXXXXXX 09/01/21 09/15/21 736.95

XXXXXXXXXXXXXXX

CIGNA/ XXXXXXXXXX

XXXX XXXXXXXXX 09/01/21 09/16/21 353.77

XXXXXXXXX

EXPRESS SCRIPTS/XXXXXXXXXX

XXXX XXXXXXXXX 09/01/21 09/16/21 120.32

XXXXXXXXX

EXPRESS SCRIPTS/ XXXXXXXXXX

XXXX XXXXXXXXX 09/01/21 09/16/21 1187.99

XXXXXXXXX

EXPRESS SCRIPTS/XXXXXXXXXX

Total for Deposit \#: XXXXXXXX Deposit Date: 09/01/2021 7437.62

Detail Report

The user had the ability to look up a single EFT by Deposit#, Deposit Date, Receipt# or Trace#.

Search for EFT# by:

1.  Deposit (N)umber
186. Deposit (D)ate
187. (R)eceipt#
188. (T)race#
189. (F)MS Document Number

Search for EFT# by://

All selection options include logic to assist the user in selecting a single EFT as follows:

1.  Deposit (N)umber:

If the user chooses to find a SINGLE EFT by Deposit#, the selection list displays as follows:

Deposit \#: 655855 Deposit Date: 08/14/10

1\. XXXX.X AETNA LIFE INS 175.59

XXXXXXXXXXXXX

2\. XXXX.X AETNA LIFE INS 139.61

XXXXXXXXXXXXX

CHOOSE 1-2: 1

190. Deposit (D)ate:

Once the <u>DEPOSIT</u> is selected, the system displays all EFTs on that Deposit for the user to select a SINGLE EFT.

Select DEPOSIT DATE: T// 032410 (MAR 24, 2010)

Select single EFT:

1\. 819 AETNA LIFE INS XXXXXXXXXXXXXXXXX 144.61 XXXXXX 03/24/10

2\. 819 AETNA LIFE INS XXXXXXXXXXXXXXXXX 87.20 XXXXXX 03/24/10

3\. 819 AETNA LIFE INS XXXXXXXXXXXXXXXXX 88.00 XXXXXX 03/24/10

4\. 819 UNITEDHEALTHCARE XXXXXXXXXXX 3545.01 XXXXXX 03/24/10

5\. 819 UNITEDHEALTHCARE XXXXXXXXXXX 20.88 XXXXXX 03/24/10

191. (R)eceipt#:

If the user chooses to find a SINGLE EFT by Receipt#, the selection list will display as follows:

Select RECEIPT: eXXXXX

1 EXXXXXXXX by: ARUSER,ONE on: 04/01/10 EDI LOCKBOX CLOSED

2 EXXXXXXXX by: ARUSER,TWO on: 04/02/10 EDI LOCKBOX CLOSED

3 EXXXXXXXX by: ARUSER,TWO on: 04/02/10 EDI LOCKBOX CLOSED

4 EXXXXXXXX by: ARUSER,TWO on: 04/02/10 EDI LOCKBOX CLOSED

5 EXXXXXXXX by: ARUSER,TWO on: 04/02/10 EDI LOCKBOX CLOSED

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1

Once the <u>RECEIPT</u> is selected, the system displays all EFTs on that Receipt for the user to select a SINGLE EFT. This display is as follows:

Select RECEIPT: eXXXXXXXX

Select single EFT:

1\. 824 SF MUTUAL XXXXXXXXXXXXXXXX 2.14 XXXXXX 04/01/10

2\. 824 SF MUTUAL XXXXXXXXXXXXXXXX 8.59 XXXXXX 04/01/10

3\. 824 UNITEDHEALTHCARE XXXXXXXXXXX 0.02 XXXXXX 04/01/10

192. (T)race#:

Once the Trace# is entered, if there is only ONE EFT that matches the entered Trace#, the EFT Audit Report will display for the selected SINGLE EFT. If there are multiple EFTs that match the entered Trace#, the user is given the following display to select a SINGLE EFT for the Audit Report.

Select TRACE: ABC6369

1 XXXXXXXXXXXXXX XXXX AETNA 385.40 05/20/15

2 XXXXXXXXXXXXXX XXXX AETNA 385.40 05/20/15

3 XXXXXXXXXXXXXX XXXX AETNA 550.55 05/20/15

4 XXXXXXXXXXXXXX XXXX AETNA 1345.01 05/20/15

5 XXXXXXXXXXXXXX XXXX AETNA 2202.50 05/20/15

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5:

Once a single EFT is selected, the EFT Transaction Audit Report displays the entire EFT history.

193. (F)MS Document Number:

     Once the FMS Document Number is entered, if there is only ONE EFT that matches the entered document number, the EFT Audit Report will display for the selected SINGLE EFT. If there are multiple EFTs that match the entered document number, the user is given the following display to select a SINGLE EFT for the Audit Report.

Select FMS DOCUMENT NUMBER: CR-XXXXXXXXXX EXXXXXXXDby: PATIENT,ONE on: 11/09/10 EDI LOCKBOX CLOSED

Select single EFT:

1\. XXX.1 SF MUTUAL XXXXXXXXXXXXXXX 16.80 XXXXXX 11/09/10

2\. XXX.2 SF MUTUAL XXXXXXXXXXXXXXX 16.80 XXXXXX 11/09/10

3\. XXX.3 SF MUTUAL XXXXXXXXXXXXXXX 14.53 XXXXXX 11/09/10

Select item from list:

Once a single EFT is selected, the EFT Transaction Audit Report displays the entire EFT history.

194. Once the selected EFT is displayed, the system returns to the selection prompt to allow the user to select another EFT by Deposit \#, Deposit Date, Receipt \# or Trace \#.

## First Party COPAY Auto-Decrease Report Acronym: FAD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was created to display the Auto-Decrease Adjustments for First Party claims with residual balances for which decrease adjustments have been automatically applied by the nightly process.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

47. Run this report on an “as needed” basis.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the First Party Auto-Decrease Adjustment Report, proceed through the following steps, selecting either All Patients or a Single Patient:

First Party COPAY Auto-Decrease Report (ALL PATIENTS):

Select division: ALL//

Select (P)ATIENT or (A)LL?: ALL//

Sort by (C)LAIM \# or PATIENT (N)AME?: CLAIM//

Sort CLAIM (F)IRST TO LAST or (L)AST TO FIRST?: FIRST TO LAST//

Start Date: 1/10 (JAN 10, 2019)

End Date: JAN 10,2019// T (JAN 15, 2019)

Display in List Manager format? (Y/N): NO//

Export the report to Microsoft Excel? NO//

DEVICE: HOME// HOME (TERMINAL) Right Margin: 80//

First Party COPAY Auto-Decrease Report Page: 1

Run Date: 01/15/19@07:43:03

Divisions: ALL

Date Range: 01/10/19 - 01/15/19 (Date Decrease Applied)

Sorted By: Claim - First to Last

Copay Decrease

Patient Name/SSN Amt Amt Bill \# 3rd Party Date

--------------------------------------------------------------------------------

PATIENT, ONE TWO/XXXX 50.00 23.88 NNN-KXXXXX 442-KXXXXX 01/10/19

CLIENT, THREE FOUR/XXXX 50.00 50.00 NNN-KXXXXX 442-KXXXXX 01/10/19

\*\*Totals for Date: 01/10/19 \# of Decrease Adjustments: 2

Total Amount of Decrease Adjustments: \$73.88

\*\*\*\* Totals for Date Range: \# of Decrease Adjustments: 2

Total Amount of Decrease Adjustments: \$73.88

\*\*\*\*\* END OF REPORT \*\*\*\*\*First Party COPAY Auto-Decrease Report (SINGLE PATIENT):

Select division: ALL//

Select (P)ATIENT or (A)LL?: ALL// PATIENT

Select Patient: USER

1 USER,ONE T \*SENSITIVE\* \*SENSITIVE\* NO TRICARE

2 USER,ONE U \*SENSITIVE\* \*SENSITIVE\* NO EMPLOYEE

3 USER,TWO A \*SENSITIVE\* \*SENSITIVE\* NO TRICARE C

4 USER,TWO B \*SENSITIVE\* \*SENSITIVE\* NO ACTIVE DUTY C

5 USER,TWO C \*SENSITIVE\* \*SENSITIVE\* NO NSC VETERAN C

6 USER,THREE A \*SENSITIVE\* \*SENSITIVE\* YES SC VETERAN CD

7 USER,THREE B \*SENSITIVE\* \*SENSITIVE\* NO NSC VETERAN CD

8 USER,THREE C \*SENSITIVE\* \*SENSITIVE\* NO NSC VETERAN C

9 USER,THREE D \*SENSITIVE\* \*SENSITIVE\* NO ACTIVE DUTY C

10 USER,THREE E \*SENSITIVE\* \*SENSITIVE\* YES SC VETERAN CD

Press \<Enter\> to see more, '^' to exit this list, OR

CHOOSE 1-10: 8 USER,THREE C \*SENSITIVE\* \*SENSITIVE\* NO NSC VETERAN C

Sort by (C)LAIM \# or PATIENT (N)AME?: CLAIM//

Sort CLAIM (F)IRST TO LAST or (L)AST TO FIRST?: FIRST TO LAST//

Start Date: 1/10 (JAN 10, 2019)

End Date: JAN 10,2019// T (JAN 15, 2019)

Display in List Manager format? (Y/N): NO//

Export the report to Microsoft Excel? NO//

DEVICE: HOME// HOME (TERMINAL) Right Margin: 80//

First Party COPAY Auto-Decrease Report Page: 1

Run Date: 01/15/19@07:43:41

Divisions: ALL

Date Range: 01/10/19 - 01/15/19 (Date Decrease Applied)

Sorted By: Claim - First to Last

Copay Decrease

Patient Name/SSN Amt Amt Bill \# 3rd Party Date

--------------------------------------------------------------------------------

USER,THREE C XXXX 50.00 23.88 442-KXXXXX 442-KXXXXX 01/10/19

\*\*Totals for Date: 01/10/19 \# of Decrease Adjustments: 1

Total Amount of Decrease Adjustments: \$23.88

\*\*\*\* Totals for Date Range: \# of Decrease Adjustments: 1

Total Amount of Decrease Adjustments: \$23.88

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## First Party COPAY Manual vs Auto-Decrease Report Acronym: FAM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was created to show the number of first party claims auto-released from hold versus the total auto-decreased. There are both summary and detail views.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run this report on an “as needed” basis.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the First Party COPAY Manual vs Auto-Decrease Report, proceed through the following steps, selecting either Summary or Detail Format:

First Party COPAY Manual vs Auto-Decrease Report Prompts:

Select division: ALL//

Display (S)UMMARY or (D)ETAIL Format?: DETAIL//

Sort CLAIM (F)IRST TO LAST or (L)AST TO FIRST?: FIRST TO LAST//

Include first party bills where the latest decrease falls within the following

date range:

Start Date: 1/10 (JAN 10, 2019)

End Date: JAN 10,2019// T (JAN 15, 2019)

Display in List Manager format? (Y/N): NO//

Export the report to Microsoft Excel? NO//

DEVICE: HOME// HOME (TERMINAL) Right Margin: 80//

First Party COPAY Manual vs Auto-Decrease Report Detail:

First Party COPAY Release Report Page: 1

Run Date: 02/28/19@14:13:20

Divisions: ALL

Date Range: 11/20/18 - 02/28/19 (Date of Latest Decrease)

Sorted By: Claim - First to Last Display: DETAIL

3rd Party Copay Auto-Decr Manual Decr Total Decr

COPAY Bill \# Bill \# Date Amt Amt Amt Amt RH

--------------------------------------------------------------------------------------

442-KXXXXXX 442-KXXXXXX 02/12/19 15.00 6.75 0.00 6.75 \*

442-KXXXXXX 02/12/19 15.00 15.00 15.00

\*\*Totals for Date 02/12/19: 30.00 6.75 15.00 21.75 1

Percent for Date 02/12/19: 22.50% 50.00% 72.50% 50%

\*\*\*\* Totals for Date Range: 30.00 6.75 15.00 21.75

Percent for Date Range: 22.50% 50.00% 72.50%

\*\*\*\*\* END OF REPORT \*\*\*\*\*

Type \<Enter\> to continue or '^' to exit:

First Party COPAY Manual vs Auto-Decrease Report Summary

First Party COPAY Release Report Page: 1

Run Date: 02/28/19@14:13:20

Divisions: ALL

Date Range: 11/20/18 - 02/28/19 (Date of Latest Decrease)

Sorted By: Claim - First to Last Display: SUMMARY

Copay Auto-Decr Manual Decr Total Decr

Amt Amt Amt Amt RH

-------------------------------------------------------------------------------------

\*\*Totals for Date 02/12/19: 30.00 6.75 15.00 21.75 1

Percent for Date 02/12/19: 22.50% 50.00% 72.50% 50%

\*\*\*\* Totals for Date Range: 30.00 6.75 15.00 21.75

Percent for Date Range: 22.50% 50.00% 72.50%

\*\*\*\*\* END OF REPORT \*\*\*\*\*

Type \<Enter\> to continue or '^' to exit:

## EEOB Move / Copy / Remove Audit Report Acronym: MCR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the EEOB Move / Copy / Remove Audit Report on a regular basis, as determined by the site, to monitor EEOBs moved or copied from one claim to another

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the report EEOB Move / Copy / Remove Audit Report, proceed with the following selections:

Select division: ALL//

START DATE: 05/28/14 (MAY 28, 2014)

END DATE: MAY 28, 2014// T (FEB 21, 2017)

Move/Copy/Remove or All (M/C/R/A): All//

Select division: ALL//

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: A// LL

Export the report to Microsoft Excel? NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

EEOB Move/Copy/Remove - Audit Report Page: 1

Run Date/Time: 2/21/17@14:18:42

Divisions: ALL

Date Range: 05/28/14 - 02/21/17 (Date EEOB was Moved/Copied/Removed)

MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

Action(s) Selected: ALL

Orig Bill# Trace \#

Moved/Copied/ Total Amt User Who Moved/

ERA \# Date/Time Removed Paid Copied/Removed

================================================================================

XXXXXXXXXX XXXXXXXX

XXXXX 7/31/14@07:26:16 MOVED \$163.00 Patient, One

New Bill: KXXXXXX Other Bill Number(s): NONE

Justification Comments: EEOB moved from Claim KXXXXXX

Automatically by AUTOPOST

XXXXXXXXXX XXXXXXXX

XXXXX 6/6/14@08:27:15 REMOVED \$1122.41 Patient, One

New Bill: KXXXXXX Other Bill Number(s): NONE

Justification Comments: EEOB removed from claim KXXXXXX

Automatically by AUTOPOST

XXXXXXXXXX XXXXXXXXX

XXXXX 2/2/15@07:37:50 COPIED \$48.15 Patient, Two

New Bill: KXXXXXX Other Bill Number(s): KXXXXXX

Justification Comments: EEOB from claim KXXXXXX copied to claim(s)

KXXXXXX, KXXXXXX by automatically by AUTOPOST

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## EEOBs Marked for Auto-Post Audit Report Acronym: EMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the EEOBs Marked for Auto-Post Audit Report to determine the user who marked an EEOB for auto-post. Lines included in the report are based on filter criteria selected at run time by the end user.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the EEOBs Marked for Auto-Post Audit Report, proceed with the following selections:

Select Audit Reports Option: EMA EEOBs Marked for Auto-Post Audit Report

Select division: ALL//

Start Date: T-10 (NOV 27, 2018)

End Date: NOV 27,2018// T (DEC 07, 2018)

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//

Run Report for (S)pecific or (A)ll Users: A// ll

Sort by Insurance Company (N)ame or (U)ser: N// ame

Display in List Manager format? (Y/N): NO//

Export the report to Microsoft Excel? NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EEOBs Marked for Auto-Post Audit Report Dec 07, 2018@09:25:16 Page: 1

Divs : All

M/P/T/C: All - All Payers Auto-Post Date: 11/27/18-12/07/18

Users: All Sort: Payer Name

ERA \# Claim \# Trace \#

--------------------------------------------------------------------------------

Auto-Post Date: 12/04/18

Payer: XXXXXXXXXX/AETNA -CONTINENTAL LIFE INSURANCE COMPANY OF BRENTWOOD

User: USER,ONE

XXXXX.X XXXXXXXXXX OU XXXXXXXXXXXXX

XXXXX.X XXXXXXXXXX OU XXXXXXXXXXXXX

XXXXX.X XXXXXXXXXX OU XXXXXXXXXXXXX

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## Provider Level Adjustments (PLB) Report Acronym: PLB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run the PLB Report regularly, as determined by the site, to extract report data, as well as view and manage refund requests, for all PLB adjustment codes (FB, WO, 72, IR, J1, L6, CS, WU, etc.).

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the PLB Report, proceed with the following selections:

Select EDI Lockbox Reports Menu Option: PL Provider Level Adjustments (PLB) Report

Select Division: ALL//

(S)UMMARY or (D)ETAIL FORMAT: SUMMARY// *\<=Defaults to SUMMARY*

SELECT (C)ODE, (R)ANGE of CODEs or (A)LL: ALL//

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

Select Insurance Company by NAME or TIN:TIN//NAME

RUN REPORT FOR (A)LL,(S)SPECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?:ALL//SPECIFIC

Select Insurance Company NAME: TRICARE WEST XXXXXXXXXX

SORT BY (C)ODE or (P)AYER?: CODE// *\<=Defaults to CODE*

START DATE: 08/10/15

END DATE: 8/17/15

DEVICE: HOME// UCX/TELNET Right Margin: 80//

PLB Report – Summary:

EDI LOCKBOX 835 PROVIDER LEVEL ADJUSTMENT (PLB) REPORT - SUMMARY Page: 1

SORT by PLB CODES REPORT RUN DATE: Sep 17, 2015@10:16:15

DIVISION: ALL Codes: ALL

835 PAYERS: ALL 835 PAYER TINs: SELECTED MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

EOB PAID DATE RANGE: 08/10/15 - 08/17/15

===============================================================================

GRAND TOTALS FOR ALL PLB CODES & PAYERS ON REPORT

TOTAL \#ERAs: 5 ADJ: -5% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: \$ -960.55 AMT BILLED: \$ 21154.95 AMT PAID: \$ 19895.76

===============================================================================

ADJ CODE: 50 \# ERAs: 1 ADJ: -1% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -50.00 AMT BILLED: 6102.20 AMT PAID: 6064.70

ADJ CODE TEXT: Late Charge

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/XXXXXXXXXXX

\#ERAs: 1 ADJ: -1% \[ADJ: -50.00/ BILLED: 6102.20\] PAID: 6064.70

-------------------------------------------------------------------------------

ADJ CODE: 51 \# ERAs: 1 ADJ: 0% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -15.00 AMT BILLED: 6102.20 AMT PAID: 6067.20

ADJ CODE TEXT: Interest Penalty Charge

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/XXXXXXXXXXX

\#ERAs: 1 ADJ: 0% \[ADJ: -15.00/ BILLED: 6102.20\] PAID: 6067.20

-------------------------------------------------------------------------------

ADJ CODE: J1 \# ERAs: 2 ADJ: -1% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -101.55 AMT BILLED: 7450.00 AMT PAID: 7013.31

ADJ CODE TEXT: Nonreimbursable

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/XXXXXXXXXXX

\#ERAs: 2 ADJ: -1% \[ADJ: -101.55/ BILLED: 7450.00\] PAID: 7013.31

-------------------------------------------------------------------------------

ADJ CODE: WO \# ERAs: 1 ADJ: -33% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -500.00 AMT BILLED: 1500.55 AMT PAID: 750.55

ADJ CODE TEXT: Overpayment Recovery

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/XXXXXXXXXXX

\#ERAs: 1 ADJ: -33% \[ADJ: -500.00/ BILLED: 1500.55\] PAID: 750.55

-------------------------------------------------------------------------------

ADJ CODE: WU \# ERAs: 2 ADJ: -7% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -294.00 AMT BILLED: 3950.55 AMT PAID: 2955.85

ADJ CODE TEXT: Unspecified Recovery

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/XXXXXXXXXXX

\#ERAs: 2 ADJ: -7% \[ADJ: -294.00/ BILLED: 3950.55\] PAID: 2955.85

-------------------------------------------------------------------------------

PLB Report – Detailed:

EDI LOCKBOX 835 PROVIDER LEVEL ADJUSTMENT (PLB) REPORT - DETAIL Page: 1

SORT by PLB CODES REPORT RUN DATE: Sep 17, 2015@10:18:20

DIVISION: ALL Codes: ALL

835 PAYERS: ALL 835 PAYER TINs: SELECTED MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

EOB PAID DATE RANGE: 08/10/15 - 08/17/15

===============================================================================

GRAND TOTALS FOR ALL PLB CODES & PAYERS ON REPORT

TOTAL \#ERAs: 5 ADJ: -5% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: \$ -960.55 AMT BILLED: \$ 21154.95 AMT PAID: \$ 19895.76

===============================================================================

ADJ CODE: 50 \# ERAs: 1 ADJ: -1% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -50.00 AMT BILLED: 6102.20 AMT PAID: 6064.70

ADJ CODE TEXT: Late Charge

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/XXXXXXXXXXXX

\#ERAs: 1 ADJ: -1% \[ADJ: -50.00/ BILLED: 6102.20\] PAID: 6064.70

-----------------------------------------------------------------------------

\#ERA DATE %ADJ ADJUST BILLED PAID CHECK#

TRACE#

REFERENCE#

XXXXX 08/14/15 0 -50.00 6102.20 6064.70

XXXXXXXXXXXXXX

PATIENT CHECK BOUNCED

-------------------------------------------------------------------------------

ADJ CODE: 51 \# ERAs: 1 ADJ: 0% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -15.00 AMT BILLED: 6102.20 AMT PAID: 6067.20

ADJ CODE TEXT: Interest Penalty Charge

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/XXXXXXXXXXX

\#ERAs: 1 ADJ: 0% \[ADJ: -15.00/ BILLED: 6102.20\] PAID: 6067.20

-----------------------------------------------------------------------------

\#ERA DATE %ADJ ADJUST BILLED PAID CHECK#

TRACE#

REFERENCE#

XXXXX 08/17/15 0 -15.00 6102.20 6067.20

XXXXXXXXXXXXXX

INTEREST CHARGE

-------------------------------------------------------------------------------

ADJ CODE: J1 \# ERAs: 2 ADJ: -1% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -101.55 AMT BILLED: 7450.00 AMT PAID: 7013.31

ADJ CODE TEXT: Nonreimbursable

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/XXXXXXXXXXX

\#ERAs: 2 ADJ: -1% \[ADJ: -101.55/ BILLED: 7450.00\] PAID: 7013.31

-----------------------------------------------------------------------------

\#ERA DATE %ADJ ADJUST BILLED PAID CHECK#

TRACE#

REFERENCE#

XXXXX 08/10/15 0 -55.00 2450.00 2205.30

XXXXXXXXXXXXXX

notes here on J1 PLB Adjustment - TW

XXXXX 08/10/15 0 -46.55 5000.00 4808.01

XXXXXXXXXXXXXX

TW entered comments for J1 PLB adjustment

-------------------------------------------------------------------------------

ADJ CODE: WO \# ERAs: 1 ADJ: -33% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -500.00 AMT BILLED: 1500.55 AMT PAID: 750.55

ADJ CODE TEXT: Overpayment Recovery

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/XXXXXXXXXXX

\#ERAs: 1 ADJ: -33% \[ADJ: -500.00/ BILLED: 1500.55\] PAID: 750.55

-----------------------------------------------------------------------------

\#ERA DATE %ADJ ADJUST BILLED PAID CHECK#

TRACE#

REFERENCE#

XXXXX 08/10/15 -33 -500.00 1500.55 750.55

XXXXXXXXXXXXXX

User entered comments here.... TW

-------------------------------------------------------------------------------

ADJ CODE: WU \# ERAs: 2 ADJ: -7% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -294.00 AMT BILLED: 3950.55 AMT PAID: 2955.85

ADJ CODE TEXT: Unspecified Recovery

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/XXXXXXXXXXX

\#ERAs: 2 ADJ: -7% \[ADJ: -294.00/ BILLED: 3950.55\] PAID: 2955.85

-----------------------------------------------------------------------------

\#ERA DATE %ADJ ADJUST BILLED PAID CHECK#

TRACE#

REFERENCE#

XXXXX 08/10/15 -17 -250.00 1500.55 750.55

XXXXXXXXXXXXXX

wu comments --- TW

XXXXX 08/10/15 0 -44.00 2450.00 2205.30

XXXXXXXXXXXXXX

user comment entered here - TW

-------------------------------------------------------------------------------

## ERAs Posted with Paper EOB Audit Report Acronym: POSR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the ERAs Posted with Paper EOB Audit Report on a regular basis, as determined by the site, to identify usage of the Update ERA Posted to EOB option.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the ERAs Posted with Paper EOB Audit Report, proceed with the following selections:

Select EDI Lockbox Reports Menu Option: ERAs Posted with Paper EOB Audit Report

Select division: ALL//

START DATE: 1/1/2011 (JAN 01, 2011)

END DATE: JAN 1,2011// T (SEP 20, 2011)

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: A// LL

Export the report to Microsoft Excel? NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

ERAs Posted with Paper EOB - Audit Report Page: 1

Run Date: 9/20/11@16:04:34

DIVISIONS: ALL

Date Range: 1/1/11 - 9/20/11 (DATE ERA UPDATED)

MEDICAL/PHARMACY/TRICARE/CHAMPVA:TRICARE

Date/Time User Who EFT Match Status

ERA \# Receipt \# ERA Updated Updated Detail Post Status

===============================================================================

XXXXX XXXXXXX 7/27/11@16:19:11 User,Five MATCHED TO PAPER CHECK

MANUALLY POSTED

XXXXX XXXXXXXXX 7/29/11@17:50:43 User,Four MATCHED TO PAPER CHECK

MANUALLY POSTED

XXXXX XXXXXXX 9/12/11@14:03:33 User,Four MATCHED TO PAPER CHECK

MANUALLY POSTED

XXXXX XXXXXXXX 9/16/11@07:31:28 User,One MATCHED TO PAPER CHECK

MANUALLY POSTED

\*\*\*\*\*\*\*\* END OF REPORT \*\*\*\*\*\*\*\*

## Payer Implementation Report Acronym: PX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review this report on a regular basis, as determined by the site, to identify all payers that have been associated with ERAs in the system. This report will show all payers, regardless of whether the payer is, or is not, excluded from auto-posting or auto-decreasing.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run this report, select an output device.

To run the report, proceed with the following selections:

Select EDI Lockbox Reports Menu \<TEST ACCOUNT\> Option: PX Payer Implementation Report

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

DEVICE: HOME// UCX/TELNET Right Margin: 80//

PAYER IMPLEMENTATION REPORT Page: 1

RUN DATE: 6/10/14@08:15:01 MEDICAL/PHARMACY/TRICARE/CHAMPVA: ALL

PAYER ID PAYER NAME DATE ADDED

================================================================================

XXXXXXXXXXX INSURANCE PAYER NAME 1 02/03/04

XXXXXXXXXXX INSURANCE PAYER NAME 2 09/01/10

XXXXXXXXXXX INSURANCE PAYER NAME 3 09/29/10

Press enter to continue, '^' to exit:

## CARC / RARC Quick Search Acronym: QS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run the CARC / RARC Quick Search regularly, as determined by the site, to display all data associated with the entered code.

The CARC / RARC Quick Search displays as follows:

EDI LOCKBOX CARC/RARC QUICK SEARCH Page: 1

REPORT RUN DATE: Sep 17, 2015@10:04:11

CODE START DATE STOP DATE DATE MODIFIED CARC/RARC LAST VISTA UPDATE

CODE DESCRIPTION

===============================================================================

9 01/01/95 09/20/09 CARC 09/10/15

The diagnosis is inconsistent with the patient"s age. Note: Refer to the  
835 Healthcare Policy Identification Segment (loop 2110 Service Payment  
Information REF), if present.

## Remove ERA from Active Worklist Audit Report Acronym: REMR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review this report on a regular basis, as determined by the site, to identify all ERAs that have been removed from the Worklist.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the report, proceed with the following selections:

Remove ERA from Active Worklist Audit Report

Select Start Date: (W/R/B): Both Dates

START DATE: T-100 (OCT 19, 2011)

END DATE: OCT 19,2011// T (JAN 27, 2012)

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: A// LL

Select division: ALL//

EXPORT THE REPORT TO Microsoft Excel (Y/N): ? NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

ERAs Removed from Active Worklist - Audit Report Page 6

Run Date/Time: 1/27/12@10:39:49

DATE RANGE: 10/19/11 - 1/27/12 (Received & Removed)

DIVISIONS: ALL

MEDICAL/PHARMACY/TRICARE/CHAMPVA: TRICARE

ERA# Trace \#/Payer Name

Date/Time Date ERA Total Amt User Who

Removed Received Paid Removed

================================================================================

XXXXX 005640947/PRINCIPAL FINANCIAL GROUP

1/19/12@12:04:04 2/26/07 34.85 User,One

Removed Reason: ERA does not belong; check returned to payer

XXXXX BANKERS LIFE & CASUALTY

1/18/12@14:35:41 2/26/07 4.66 User,Four

Removed Reason: check was returned to payer before deposited

XXXXX 3388003139/BANKERS LIFE & CASUALTY

1/27/12@10:11:46 2/26/07 14.07 User,Four

Removed Reason: ERA belongs to another site; check returned to payer

\*\*\*\*\*\*\*\* END OF REPORT \*\*\*\*\*\*\*\*

## Link Payment Tracking Report Acronym: SR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review this report on a regular basis, as determined by the site, to identify all entries going in and out of Suspense including information on where the payment was dispersed by the user via the Link Payment option.

The LINK PAYMENT TRACKING REPORT displays as follows:

LINK PAYMENT TRACKING REPORT NOV 20, 2017@15:59:29 PAGE 1

FOR THE DATE RANGE: RECEIPT#: EXXXXXXXX

RECEIPT# TRANS# DATE AMOUNT CLAIM USER DISPOSITION

REASON CLAIMS

--------------------------------------------------------------------------------

EXXXXXXXX 11/20/17 38.92 PH In Suspense

Multi-Trans Split

KXXXXXX \$15.00

KXXXXXX \$23.92

EXXXXXXXX 1 11/20/17 15.00 KXXXXXX PH Paid

EXXXXXXXX 2 11/20/17 23.92 KXXXXXX PH Paid

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## CARC / RARC Table Data Report Acronym: TB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review this report on a regular basis, as determined by the site, to display all CARC / RARC data that has been transferred from FSC, stored in VistA and available for use.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the report, proceed with the following selections:

Select EDI Lockbox Reports Menu Option: TB CARC/RARC Table Data Report

SELECT (N)O CARCS OR (A)LL CARCS: ALL// *\<=Defaults to ALL*

SELECT (N)O RARCS OR (A)LL RARCS: ALL// *\<=Defaults to ALL*

Include (A)ctive codes, (I)nactive codes or (B)OTH?: ACTIVE//*\<=Default ACTIVE*

REPORT DATE: T// *\<=Defaults to T (today)*

DEVICE: HOME// UCX/TELNET Right Margin: 80//

## View / Print ERA Acronym: VP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to select an ERA and print or view its contents.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used on an “as needed” basis.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the View / Print Report proceed with the following selections:

Select EDI Lockbox Reports Menu Option: VP View/Print ERA

Select ELECTRONIC REMITTANCE ADVICE ENTRY: XXXXXXTN 03-10-03 704.03

IBinsurance Company One MATCHED

DO YOU WANT TO INCLUDE EXPANDED EEOB DETAIL?: NO// YES \<RET\>

Display Auto-Post and Match Status Audit Information?: NO// YES \<RET\>

Display in List Manager format? (Y/N): YES//

View/Print ERA - Expanded Detail EDI LOCKBOX WORKLIST - ERA DETAIL 8/7/19 Page: 1

================================================================================

\*\*ERA SUMMARY DATA\*\*

ENTRY: XXXXX TRACE NUMBER: TP XXXXXXXXXXXXX

INSURANCE CO ID: XXXXXXXXXX ERA DATE: NOV 09, 2018

TOTAL AMOUNT PAID: 1878.97

PAYMENT FROM: AETNA -CONTINENTAL LIFE INSURANCE COMPANY OF BRENTWOOD

FILE DATE/TIME: NOV 09, 2018@09:48:50 RECEIPT: XXXXXXXXX

EFT MATCH STATUS: MATCHED TO PAPER CHECK

ERA TYPE: ERA INDIVIDUAL EOB COUNT: 1

MAIL MESSAGE: XXXXXX CHECK \#: TP XXXXXXXXXXXXX

ERA DETAIL POST STATUS: NOT POSTED EXPECTED PAYMENT METHOD CODE: CHK

DATE CHECK MATCHED: NOV 09, 2018 CHECK MATCHED USER: REDACTED

\*\*EEOB DETAIL DATA\*\*

SEQUENCE \#: 1 EOB DETAIL: KXXXXXX

AMOUNT PAID: 1878.97 INSURANCE COMPANY ON BILL: BCBS XX\*

FREE TEXT PATIENT NAME: PATIENT, F A

ORIGINAL PATIENT NAME: CLERK, A B

BILLING PROVIDER NPI: XXXXXXXXXX RECEIPT:

BILL REFERENCE NUMBER: 442-KXXXXXX

Type \<Enter\> to continue or '^' to exit:

EDI LOCKBOX WORKLIST - ERA DETAIL 8/7/19 Page: 2

================================================================================

PATIENT: PATIENT, F A /XXXX CLAIM \#: XXX-KXXXXXX

STMT FROM DATE: JUN 02, 2014 STMT TO DATE: JUN 02, 2014

\*\*EOB PROVIDER(S)/NPI CLAIM PROVIDER(S)/NPI\*\*

--------------------- -----------------------

ATTENDING: DOE, JOHN /XXXXXXXXXX

BILLING: /XXXXXXXXXX XYZ VAMC/XXXXXXXXXX

RENDERING:

\*\*EXCEPTION RESOLUTION LOG DATA\*\*

EOB GENERAL INFORMATION:

Type : NORMAL EOB EOB Paid DT : 11/09/18

Entry Dt/Tm :11/09/18 9:48 am Claim Status : PROCESSED

Entry Dt/Tm :11/09/18 9:48 am Review Status: ACCEPTED-COMPLETE EOB

Entered By : Insurance Seq: SECONDARY

Last Edited : 11/09/18 9:48 am Last Edit By : POSTMASTER

Patient Name: PATIENT, F A Pt. Relation : PATIENT

Insured ID : SUBSC ID XXXXXXX

Type \<Enter\> to continue or '^' to exit:

EDI LOCKBOX WORKLIST - ERA DETAIL 8/7/19 Page: 3

================================================================================

Claim Rec'd Date :

Other Subscriber Name:

PAYER INFORMATION:

Payer Name : BCBS XX\*

Payer Id : XXXXXXXXXX

ICN : XXXXXXXXXXX

CLAIM LEVEL PAY STATUS:

Tot Submitted Chrg: 1878.97 Covered Amt : 1878.97

Payer Paid Amt : 1878.97 Patient Resp. Amt : 0.00

CLAIM LEVEL ADJUSTMENTS:

NONE

MEDICARE INFORMATION:

NONE

LINE LEVEL ADJUSTMENTS:

\# SV DT REVCD PROC MOD UNITS BILLED DEDUCT COINS ALLOW PYMT

Type \<Enter\> to continue or '^' to exit:

EDI LOCKBOX WORKLIST - ERA DETAIL 8/7/19 Page: 4

================================================================================

1 06/02/14 XXX XXXXX 1 300.66 0.00 0.00 0.00 300.66

\# SV DT REVCD PROC MOD UNITS BILLED DEDUCT COINS ALLOW PYMT

2 06/02/14 XXX XXXXX XX 1 1442.60 0.00 0.00 0.00 1442.60

\# SV DT REVCD PROC MOD UNITS BILLED DEDUCT COINS ALLOW PYMT

3 06/02/14 XXX XXXXX 1 135.71 0.00 0.00 0.00 135.71

Type \<Enter\> to continue or '^' to exit:

\*\*AUTO POST STATUS\*\*

10/01/18@12:13:31 NULL UNPOSTED POSTMASTER

Auto Matching: Marked as Auto-Post Candidate

10/01/18@12:13:57 UNPOSTED COMPLETE POSTMASTER

Auto Posting: ERA posted successfully

\*\*MATCH STATUS\*\*

05/28/14@11:17:14 NULL UNMATCHED POSTMASTER

06/01/14@10:33:24 UNMATCHED PAPER CHK FAWCETT,CINDY N

## EFT Deposit Reconciliation Report Acronym: DEP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EFT Deposit Reconciliation Report has been removed from the EDI Lockbox Reports Menu tree.

## EFT Unlock Lockout Override Report Acronym: EUO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used on an “as needed” basis.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the report, proceed with the following steps:

(M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

Start Date: t-10 (MAR 19, 2019)

End Date: MAR 19,2019//

Export the report to Microsoft Excel? NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// HOME (TERMINAL) Right Margin: 80//

EFT Unlock Lockout Override Report Page: 1

Date Range: 03/03/19 – o4/01/19 Run Date: 03/29/19@07:43:03

Medical/Pharmacy/TRICARE: ALL

Date User Comment Type \# Days

------------------------------------------------------------------------------

03/19/19 REDACTED IS IS THE COMMENT M 30

03/20/19 REDACTED THIS IS ANOTHER OVERRIDE COMMENT P 30

Total \# of Medical Overrides: 1

Total \# of Pharmacy Overrides: 1

Total \# of TRICARE Overrides: 0

Total \# of EFT Overrides: 2

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## ERA Status Change Audit Report Acronym: ESC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run this report on a routine basis, as determined by the site, to display a detailed audit trail listing of ERA AUTO POST STATUS changes.

The report allows the user to run an audit for a single ERA or ALL ERAs for a date range. Report will be sorted by ERA then by date / time. Specific data elements shall include Date / Time, User, ERA#, STATUS (old / new) and Reason text.

The Reason text will be a summary of the “process” that caused the ERA Status to be changed along with the “outcome” of the change.

Example Reason text messages are listed below with some of these messaged displayed in the report mockup.

Auto Matching: Marked as Auto-Post Candidate

Auto Posting: Removed from Auto Posting-Unable to create scratchpad

Auto Posting: Removed from Auto Posting-ERA level Adjustment(s)

Auto Posting: Removed from Auto Posting-+/- pairs do not balance

Auto Posting: Removed from Auto Posting-Unable to create receipt

Auto Posting: Removed from Auto Posting-Error in receipt processing

Auto Posting: ERA posted successfully

Auto Posting: Some of the ERA lines went to APAR

Auto Posting: Previously processed ERA posting attempt

Exceptions: Marked as Auto-Post Candidate

Exceptions: Not Marked as Auto-Post Candidate-\<Reasons listed in section 2.9.1.2\>

Worklist: Marked as Auto-Post Candidate

Worklist: Not Marked as Auto-Post Candidate-\<Reasons listed in section 2.9.1.2\>

Manual Match: Marked as Auto-Post Candidate

Manual Match: Not Marked as Auto-Post Candidate-\<Reasons listed in section 2.9.1.2\>

Unmatch: Removed as Auto-Post Candidate

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the ERA Status Change Audit report, proceed with the following steps:

Select EDI Lockbox (ePayments) Reports Menu \<TEST ACCOUNT\> Option: ERA Status C

hange Audit Report

SELECT (S)ingle ERA or (A)LL: ALL//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

The ERA Status Change Audit report will display as follows:

ERA STATUS AND AUDIT INFORMATION 11/25/24 Page: 1

================================================================================

\*\*ERA SUMMARY DATA\*\*

ENTRY: XXXXX TRACE NUMBER: XXXXXXXXXXXXX

INSURANCE CO ID: XXXXXXXXXX ERA DATE: JUL 12, 2014

TOTAL AMOUNT PAID: 115.17 PAYMENT FROM: INSURANCE HEALTH CARE

FILE DATE/TIME: JUL 12, 2014@11:04:56 EFT MATCH STATUS: MATCHED TO TDA

ERA TYPE: ERA INDIVIDUAL EOB COUNT: 1

MAIL MESSAGE: XXXXXX ERA DETAIL POST STATUS: NOT POSTED

EXPECTED PAYMENT METHOD CODE: CHK DATE CHECK MATCHED: JUL 12, 2014

CHECK MATCHED USER: LASTNAME,USER A

MCCF DATE/TIME: JUL 12, 2014@11:06:43

Date/Time Edited Status (Old/New)

User

Reason Text

--------------------------------------------------------------------------------

\*\*AUTO POST STATUS\*\*

10/01/14@12:13:31 NULL UNPOSTED POSTMASTER

Auto Matching: Marked as Auto-Post Candidate

10/01/14@12:13:57 UNPOSTED COMPLETE POSTMASTER

Auto Posting: ERA posted successfully

\*\*MATCH STATUS\*\*

07/12/24@11:04:56 NULL UNMATCHED POSTMASTER

07/12/24@11:06:43 UNMATCHED MATCH TDA LASTNAME,USER A

Type \<Enter\> to continue or '^' to exit:

## Manual Audit Report for Bills: MAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Manual Audit for Bills Report provides total number of claims that have been manually audited. The report can be run on-demand with detail by date or just the summary data for the date range. Detail format provides a detailed list of all claims received within the selected date range and the corresponding payer/TIN, rate type, user’s name, and comment for each claim.

### When to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the Manual Audit Report for Bills on an as-needed basis to see the number of claims that have been manually audited for the date range.

### How to Run this Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the Manual Audit Report for Bills in detail, proceed through the following steps:

Select EDI Lockbox (ePayments) Reports Menu Option - MAR Manual Audit Report for Bills

(S)ummary or (D)etail Report format? SUMMARY// D Detail Report

Start Date: 2/16/2025 (FEB 16, 2025)

End Date: MAR 18, 2025// T (MAR 18, 2025)

Export the report to Microsoft Excel? (Y/N): NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

MANUAL AUDIT REPORT - DETAIL MAR 18, 2025@08:58:09 PAGE: 1

MANUAL AUDIT DATE RANGE: 02/16/25 - 03/18/25

DATE BILL RATE TYPE USER

PAYER/TIN

COMMENTS

--------------------------------------------------------------------------------

02/18/25 442-K80001T 8 REIMBURSABLE INS. LASTNAME, USER A

MEDICARE (WNR) / 1752784278

02/20/25 442-K503JER 8 REIMBURSABLE INS. LASTNAME, USER B

BCBS WY\* /

02/26/25 442-K70000Z 8 REIMBURSABLE INS. LASTNAME, USER C

GWH-CIGNA / 1900080705

THIS IS A TEST

02/26/25 442-K70001G 8 REIMBURSABLE INS. LASTNAME, USER D

UP RAILROAD EMPLOYEES HEALTH / 1113283886

\*\*\*\*\* END OF REPORT \*\*\*\*\*

Enter RETURN to continue or '^' to exit:

To run the Daily Audit Report for Bills in summary, proceed through the following steps:

Select EDI Lockbox (ePayments) Reports Menu Option - MAR Manual Audit Report for Bills

(S)ummary or (D)etail Report format? SUMMARY// D Detail Report

Start Date: 2/16/2025 (FEB 16, 2025)

End Date: MAR 18, 2025// T (MAR 18, 2025)

DEVICE: HOME// TELNET TERMINAL

MANUAL AUDIT REPORT - SUMMARY MAR 18, 2025@08:59:30 PAGE: 1

MANUAL AUDIT DATE RANGE: 02/16/25 - 03/18/25

MANUAL AUTO

DATE \# BILLS \# BILLS

--------------------------------------------------------------------------------

02/18/25 1 0

02/20/25 1 0

02/26/25 2 0

Total: 4 0

Percentage of Manually Audited Bills: 100%

\*\*\*\*\* END OF REPORT \*\*\*\*\*

Enter RETURN to continue or '^' to exit:

# National Reports for ePayments Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Diagnostic Measures Reports menu is located under the Finance AR Manager Menu:

Clerk's AR Menu ...

Supervisor's AR Menu ...

EDI Diagnostic Measures Reports…

Select Finance AR Manager Menu Option:

There are 2 EDI Diagnostic Measure reports plus the Extracts submenu to choose from:

VS EDI VOLUME STATISTICS Report

TD ERA/EFT TRENDING Report

EX EDI Diagnostic Measures Extracts Menu…

Select EDI Diagnostic Measures Reports Option:

## EDI VOLUME STATISTICS Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI VOLUME STATISTICS Report to display metrics on \#837s / NCPDP claims and 835s with \#days between the claim and payment transactions. The report can be run for ALL payers or selected payer(s).

Select EDI Reports Option: VS EDI VOLUME STATISTICS Report

Select Division: ALL//

SELECT (A)LL PAYERS, RANGE of PAYER NAMES: ALL//

(S)UMMARY by Payer or (G)RAND TOTALS ONLY; G//

Start with DATE:

Go to DATE:

DEVICE: HOME// UCX/TELNET Right Margin: 80//

EDI VOLUME STATISTICS REPORT Page: 1

ALL DIVISIONS PAYERS:AETNA-1 – AETNA-2

DATE RANGE: 01/01/14 – 01/31/15 RUN DATE: 02/07/15@15:30:14

-------------------------------------------------------------------------------------

PAYER NAME: AETNA-1 INSURANCE

-------------------------------------------------------------------------------------

NUMBER OF 837s TRANSMITTED TO MEDICAL PAYERS 12345

NUMBER OF NCPDP CLAIMS TRANSMITTED TO PHARMACY PBMs 54321

NUMBER OF 835s RECEIVED FROM MEDICAL PAYERS 10000

NUMBER OF 835s RECEIVED FROM PHARMACY PBMs 1323

NUMBER OF 837 WITH CORRESPONDING 835 (MRA Excluded) 2921

NUMBER OF NCPDP CLAIM WITH CORRESPONDING 835 610

AVG \#DAYS BETWEEN 837 TRANSMIT AND 835 RECEIVED 9.0

AVG \#DAYS BETWEEN NCPDP CLAIM TRANSMIT AND 835 RCVD 14.5

-------------------------------------------------------------------------------------

PAYER NAME: AETNA-2 INSURANCE

-------------------------------------------------------------------------------------

NUMBER OF 837s TRANSMITTED TO MEDICAL PAYERS 100

NUMBER OF NCPDP CLAIMS TRANSMITTED TO PHARMACY PBMs 100

NUMBER OF 835s RECEIVED FROM MEDICAL PAYERS 100

NUMBER OF 835s RECEIVED FROM PHARMACY PBMs 100

NUMBER OF 837 WITH CORRESPONDING 835 (MRA Excluded) 100

NUMBER OF NCPDP CLAIM WITH CORRESPONDING 835 100

AVG \#DAYS BETWEEN 837 TRANSMIT AND 835 RECEIVED 9.0

AVG \#DAYS BETWEEN NCPDP CLAIM TRANSMIT AND 835 RCVD 14.5

-------------------------------------------------------------------------------------

GRAND TOTAL ALL PAYERS

-------------------------------------------------------------------------------------

NUMBER OF 837s TRANSMITTED TO MEDICAL PAYERS 12445

NUMBER OF NCPDP CLAIMS TRANSMITTED TO PHARMACY PBMs 54421

NUMBER OF 835s RECEIVED FROM MEDICAL PAYERS 10100

NUMBER OF 835s RECEIVED FROM PHARMACY PBMs 1423

NUMBER OF 837 WITH CORRESPONDING 835 (MRA Excluded) 3021

NUMBER OF NCPDP CLAIM WITH CORRESPONDING 835 710

AVG \#DAYS BETWEEN 837 TRANSMIT AND 835 RECEIVED 9.0

AVG \#DAYS BETWEEN NCPDP CLAIM TRANSMIT AND 835 RCVD 14.5

Enter RETURN to continue or '^' to exit:

## ERA / EFT TRENDING Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERA / EFT TRENDING Report is used to display metrics on \#ERAs, \#EEOBs (Payment EEOBs, Unmatched EEOBs, Zero Payment EEOBs), \#EFTs with \#days between ERA and EFT transactions. The report can be run for ALL payers or selected payer(s).

The prompt for “SORT BY (P)AYER or (A)MOUNT OF PAYMENT” will only display if the MAIN report is selected.

Prompts:

EFT/ERA TRENDING Report

Select division: ALL//

(A)UTO-POSTED, (M)MANUALLY POSTED, (B)OTH: BOTH// ?

Enter 'A' to include only auto-posted entries

'M' to include only manually posted entries

'B' to include both

Select one of the following:

A AUTO-POSTED

M MANUALLY POSTED

B BOTH

(A)UTO-POSTED, (M)ANUALLY POSTED, (B)OTH: BOTH//

(P)AYMENT EEOBs, (U)NMATCHED EEOBs, (Z)ERO PAYMENT EEOBs or (A)LL: ALL//

(C)HAMPVA, (M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

Select Insurance Companies by NAME or TIN: TIN//

RUN REPORT FOR (A)LL OR (S)PECIFIC INSURANCE COMPANIES?: ALL//

Select RATE TYPE NAME: 8 REIMBURSABLE INS. Who's Responsible: INSURER

Include (A)LL Claims or only (C)LOSED Claims: ALL//

Print (M)AIN Report, (S)UMMARY by Payer or (G)RAND TOTALS ONLY: G// MAIN

SORT BY (P)AYER or (A)MOUNT OF PAYMENT: PAYER//

Start with DATE: 12/24/24 (DEC 24, 2024)

Go to DATE: 1/23/25// (JAN 23, 2025)

Export the report to Microsoft Excel? (Y/N): NO//

Main Report with Header and Sub-header:

EFT/ERA TRENDING REPORT PAGE 1

ALL DIVISIONS ALL TINS MEDICAL/PHARMACY/TRICARE/CHAMPVA: ALL MANUAL/AUTOPOST: BOTH Claims: ALL

DATE RANGE: 12/24/24 - 1/23/25 RUN DATE: 1/23/25@12:05:54 PAYMENT/UNMATCHED/ZERO PAY: ALL

PAYER NAME/TIN

-----------------------------------------------------------------------------------------------------------------------------------

UNITED HEALTH CARE/1113283886

-----------------------------------------------------------------------------------------------------------------------------------

CLAIM# DOS AMT BILLED AMT PAID BILLED ERA/EOB REC'D EFT/PMT REC'D POSTED TRACE \# AUTOPOST/MANUAL

ETRANS TYPE ERA# \#EEOBS EFT# \#DAYS:(BILL/ERA) \#DAYS:(ERA/EFT) \#DAYS:(ERA+EFT/POSTED) TOTAL \#DAYS(BILL/POSTED)

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - AUTOPOST \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

K70000N 8/5/06 684.99 684.99 11/13/06 1/10/25 1/10/25 1/10/25 6721540081 AUTOPOST

ERA/EFT 93010 1 36294 6633 0 0 6633

K70001A 7/27/06 32.83 32.83 9/27/06 12/30/24 12/30/24 12/30/24 6720430187 AUTOPOST

ERA/EFT 93007 1 36291 6669 0 0 6669

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* UNMATCHED ERA - UNPOSTED \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

K70002B 8/5/06 684.99 0.00 11/13/06 1/10/25 1/10/25 N/A 6721540081 UNPOSTED

ERA/EFT 93010 1 N/A 6633 N/A N/A N/A

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ZERO PAYMENTS \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

K70007D 8/5/06 684.99 0.00 11/13/06 1/10/25 1/10/25 N/A 6721540089 UNPOSTED

ERA/EFT 93010 1 36297 6633 0 N/A N/A

-----------------------------------------------------------------------------------------------------------------------------------

EFT/ERA TRENDING REPORT PAGE 2

ALL DIVISIONS ALL TINS MEDICAL/PHARMACY/TRICARE/CHAMPVA: ALL MANUAL/AUTOPOST: BOTH Claims: ALL

DATE RANGE: 12/24/24 - 1/23/25 RUN DATE: 1/23/25@12:05:54 PAYMENT/UNMATCHED/ZERO PAY: ALL

-----------------------------------------------------------------------------------------------------------------------------------

GRAND TOTALS ALL PAYERS

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - AUTOPOST \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* UNMATCHED E0B - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 00.00

TOTAL AMOUNT PAID 00.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 6633

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 00.00

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ZERO PAYMENTS - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-----------------------------------------------------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 4

TOTAL AMOUNT BILLED 50.00

TOTAL AMOUNT PAID 0

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 20

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 1

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 0

-----------------------------------------------------------------------------------------------------------------------------------

\*\*\*\*\* END OF REPORT \*\*\*\*\*Report Totals (Summary):

EFT/ERA TRENDING REPORT PAGE 1

ALL DIVISIONS ALL TINS MEDICAL/PHARMACY/TRICARE/CHAMPVA: ALL MANUAL/AUTOPOST: BOTH Claims: ALL

DATE RANGE: 12/24/24 - 1/23/25 RUN DATE: 1/23/25@12:05:54 PAYMENT/UNMATCHED/ZERO PAY: ALL

------------------------------------------------------------------------------------

PAYER NAME/TIN

UNITED HEALTH CARE/1113283886

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - AUTOPOST \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* UNMATCHED E0B - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 50.00

TOTAL AMOUNT PAID 50.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/EOB 20

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 1

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 50.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ZERO PAYMENTS - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 4

TOTAL AMOUNT BILLED 50.00

TOTAL AMOUNT PAID 0

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 20

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 1

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 0

------------------------------------------------------------------------------------

GRAND TOTALS ALL PAYERS

------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - AUTOPOST \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - MANUAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 717.82

TOTAL AMOUNT PAID 717.82

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6651

AVG \#DAYS BETWEEN ERA/EFT 0

AVG \#DAYS BETWEEN ERA+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 6651

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 717.82

TOTAL DIFFERENCE BETWEEN ERAs (PAID) - EFTs (COLLECTED): 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO A PAPER CHECK - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/ERA 0

AVG \#DAYS BETWEEN ERA/CHK 0

AVG \#DAYS BETWEEN ERA+CHK REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO AN EFT - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 0

TOTAL AMOUNT BILLED 0.00

TOTAL AMOUNT PAID 0.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 0

AVG \#DAYS BETWEEN EOB/EFT 0

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED 0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* UNMATCHED E0B - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 50.00

TOTAL AMOUNT PAID 50.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/EOB 20

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 1

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 50.00

------------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ZERO PAYMENTS - TOTAL \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 4

TOTAL AMOUNT BILLED 50.00

TOTAL AMOUNT PAID 0

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 20

AVG \#DAYS BETWEEN EOB/EFT N/A

AVG \#DAYS BETWEEN EOB+EFT REC'D/PMT POSTED N/A

AVG \#DAYS BETWEEN BILLED/PMT POSTED N/A

TOTAL NUMBER OF ERAs 1

TOTAL NUMBER OF EEOBs 2

TOTAL NUMBER OF EFTs N/A

TOTAL AMOUNT COLLECTED 0

------------------------------------------------------------------------------------

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## EDI Diagnostic Measures Extracts Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only option listed on the EDI Diagnostic Measures Extract Menu that is not locked with the security key ‘PRCFA SUPERVISOR’ is View / Print Extracted Reports.

DE Disable-Enable DM Background Job/Reports

VP View/Print Extracted Reports

MN Manually Start DM Extract

TR Manually Transmit DM Extract

Select EDI Diagnostic Measures Extracts Menu Option:

### Report Results Imported into Excel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Except for the Daily Activity Report and the 835 CARC Data Report Filters, the software has been modified to allow the user to export the report from VistA to a text file to be imported into Microsoft Excel.

### Downloading Reports to Excel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose report to print to Excel and enter ‘0;256;999’ at the device prompt.
195. Capture report into a text file.

Select EDI Lockbox Reports Menu Option: MCR EEOB Move/Copy/Remove Audit Report

START DATE: 010106 (JAN 01, 2006)

END DATE: JAN 1,2006// t (AUG 29, 2011)

Move/Copy/Remove or All (M/C/R/A): All//

Select division: ALL//

Export the report to Microsoft Excel? NO// y YES

Before continuing, please set up your terminal to capture the

report data as this report may take a while to run.

To avoid undesired wrapping of the data saved to the

file, please enter '0;256;999' at the 'DEVICE:' prompt.

It may be necessary to set up the terminal display width

to 256 characters which can be performed by selecting the

Display option located within the 'Setup' menu on the

tool bar of the terminal emulation software (e.g. KEA,

Reflections or Smarterm).

DEVICE: HOME// 0;256;999

196. Once the user has captured the report data onto a text file, open an Excel document.
197. Select the Data tab.
198. Choose From Text button located in the Get External Data group.

<span id="_Toc183424277" class="anchor"></span>Figure 11: Data Tab

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/012.png)

The dialogue box will pop up that will allow the user to browse for the text file to cut and past the data from the VistA session.

48. Using a text file with word wrap “off” is recommended.
199. Select the import button once the text file has been selected.
200. The Text Import Wizard box comes up. Select delimited radio button and select Next.

<span id="_Toc183424278" class="anchor"></span>Figure 12: Text Import Wizard Part \#1

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/013.png)

201. Select Other from the list of delimiter choices and enter the “^” character in the space provided.
202. Select Next.

<span id="_Toc183424279" class="anchor"></span>Figure 13: Text Import Wizard Part \#2

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/014.png)

203. Select General from the list of data formats.
204. Select Finish.

<span id="_Toc183424280" class="anchor"></span>Figure 14: Text Import Wizard Part \#3

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/015.png)

205. Accept the Existing Worksheet default. Select Ok.

<span id="_Toc183424281" class="anchor"></span>Figure 15: Accept Worksheet

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/016.png)

<span id="_Toc183424282" class="anchor"></span>Figure 16: Worksheet

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/017.png)

### Report Results Displayed in List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Except for the View / Print ERA Report, the software has been modified to allow the user to view the report in a List Manager format.

### Display Report in List Manager Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose to display the report in a List Manager format.

Select OPTION NAME: EFT UNMATCHED AGING REPORT RCDPE EFT AGING REPORT

EFT Unmatched Aging Report

EFT Unmatched Aging Report

EFT Unmatched Aging

Start date: T-10 (MAY 31, 2014)

End date: MAY 31,2014// T (JUN 10, 2014)

RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//

Export the report to Microsoft Excel? (Y/N): NO//

Display in List Manager format? (Y/N): NO// YES

206. The report displays in a List Manager format with default actions.

Enter ?? for more actions

Select Action:Quit//??

The following actions are also available:

\+ Next Screen \< Shift View to Left PS Print Screen

\- Previous Screen FS First Screen PL Print List

UP Up a Line LS Last Screen SL Search List

DN Down a Line GO Go to Page ADPL Auto Display(On/Off)

\> Shift View to Right RD Re Display Screen Q Quit

Enter RETURN to continue or '^' to exit:

# Enhancements to Non-EDI Lockbox Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Agent Cashier Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Extended Check / Trace / Credit Card Search Acronym: EX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AR option allows a user to perform a check search - either by Check, Credit Card, Trace \#, or All. This has been specifically tailored for electronic funds processing. Searches can be made based on Exact Match or Contains (Partial Match):

Select Agent Cashier Menu Option: Extended Check/Trace/Credit Card Search

Extended AR BATCH PAYMENT file search.

Search for Check, Credit Card, Trace \#, or All: All//

Enter the check, credit card, or trace number to Search for

in All types: 123

Type of Match: Contains//

Start with RECEIPT Opened Date: DEC 01, 2018//T-1000 (MAR 12, 2016)

End with RECEIPT Opened Date: DEC 07, 2018//T (DEC 07, 2018)

\*\*\* Selected date range from MAR 12, 2016 to DEC 07, 2018 \*\*\*

DEVICE: HOME// HOME (CRT)

Extended Check \#/Trace \#/Credit Card Search Dec 07, 2018@12:27:21 Page: 1

For the Date Range: Mar 12, 2016 to Dec 07, 2018

Searching for: ALL TYPES CONTAINING "123"

Receipt Open Date Trans Account Amount

Any \#

================================================================================

XXXXXXX 05/09/18 1 REDACTED \$ 25.00

XXXXXXX (Check \#)

XXXXXXX 05/08/18 1 REDACTED \$ 0.01

XXXXX (Check \#)

XXXXXXX 05/08/18 2 REDACTED \$ 0.02

XXXXX (Check \#)

EXXXXXXXX 02/22/18 2 REDACTED \$ 10.00

XXXXX (Check \#)

EXXXXXXXX 11/30/17 1 XXX-XXXXXX \$ 40.00

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (Trace \#)

EXXXXXXXXX 08/01/17 1 - \$ 13.87

XXXXXXXXXXXX (Trace \#)

EXXXXXXXX 03/09/17 1 XXX-KXXXXXX \$ 196.43

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (Trace \#)

Total records found: 7

### Link Payment Acronym: LP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc183424283" class="anchor"></span>Figure 17: Link Payment

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/018.png)

Notice the new search options, S1 and S2, under Link Payment.

<span id="_Toc183424284" class="anchor"></span>Figure 18: Search Options

![](accounts-receivable-version-4-5-epayments-user-manual-edi-lockbox/019.png)

### Link Payment to Multiple Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following screen is displayed when the user accesses the Link Payment for further processing of suspense entries.

Link Payments To Accounts Jul 31, 2014@13:11:05 Page: 1 of 129

Transactions for ALL Unapplied Payments

Receipt Tran Unapplied Dep Stat Pay Date Type Ck/Tr/Cd# Amt Paid

1 XXXXXXXX 44 XXXXXXXXXXXX CLOS 03/08/13 CHEC XXXXXXXX 963.20

AcctLU: CRdoc: CR-XXXXXXXXXX ACCEPT

2 XXXXXXXX 45 XXXXXXXXXXXX CLOS 03/08/13 CHEC XXXXXXXX 666.00

AcctLU: CRdoc: CR-XXXXXXXXXX ACCEPT

3 XXXXXXXX 46 XXXXXXXXXXXX CLOS 03/08/13 CHEC XXXXXXXX 473.62

AcctLU: CRdoc: CR-XXXXXXXXXX ACCEPT

4 XXXXXXXX 47 XXXXXXXXXXXX CLOS 03/08/13 CHEC XXXXXXXX 138.60

AcctLU: CRdoc: CR-XXXXXXXXXX ACCEPT

5 XXXXXXXX 48 XXXXXXXXXXXX CLOS 03/08/13 CHEC XXXXXXXX 54.49

AcctLU: CRdoc: CR-XXXXXXXXXX ACCEPT

6 XXXXXXXX 94 XXXXXXXXXXXX CLOS 04/04/13 CHEC XXXXX 1421.71

AcctLU: CRdoc: CR-XXXXXXXXXX ACCEPT

7 XXXXXXXX 96 XXXXXXXXXXXX CLOS 04/04/13 CHEC XXXXX 3444.37

AcctLU: CRdoc: CR-XXXXXXXXXX ACCEPT

8 XXXXXXXX 11 XXXXXXXXXXXX CLOS 04/11/13 CHEC XXXXXXXX 112.08

\+ Enter ?? for more actions

S1 Search Check/Trace# CS Clear Suspense AP Account Profile

S2 Search Credit Card SR Suspense Report RP Receipt Profile

LP Link Payment SP Show Payment EA Exit Action

The user can disperse the payment to a single or multiple claims.

Additional notes:

- The user is required to disperse the ENTIRE payment between multiple claims, or nothing is linked, and the ENTIRE payment remains in Suspense with no audit records generated. When linking / dispersing payment dollars, the ENTIRE payment must be accounted for or the ENTIRE payment remains in Suspense.
- The software prevents the user from posting dollars to a bill that causes the balance to go below zero. If attempted, the user will receive an error message as in the example below.

BILL NUMBER: kXXXXXX TW-RX PAYER 1 ACTIVE \$567.79

Amount to apply to Account: (0.01-20666.66): 2000

The requested payment is greater than then amount owed please try again.

Amount to apply to Account: (0.01-20666.66):

- The user is required to enter a Reason text (i.e., Comment) when leaving a portion of the payment in SUSPENSE.

COMMENT: ??

Enter a code from the list.

Select one of the following:

1 Collected/Closed

2 Cancelled

3 Returned refund

4 Overpayment

5 Inactive bill

6 Duplicate payment

7 Policy termed

8 Service connected

9 Other

The system automatically captures / stores a Final Disposition as Paid or In Suspense as the user links payments via Link Payment. This disposition will be displayed in the new Link Payment Tracking Report.

The user may choose to restore the removed suspense EEOB to active status and move EEOB detail to the correct claim.

After payment (bill) selection the user will be asked if the payment has an EEOB.

If the response is YES, the following detail will be displayed for the EEOB:

- Claim Number
- Trace Number
- Total Amount Paid
- Removed By
- Justification Comment

Users will be prompted to confirm this is the correct EEOB for this payment. On filing, the EEOB will be moved to the correct claim (if the payment claim number is different from the claim on the EEOB) and the EEOB removed status will be cleared.

When using the Link Payment functionality, the user must know the Account Number and the Amounts to be processed. The Link Payment functionality does NOT allow the user to search for account information.

### Deposit Processing Acronym: DP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Select Deposit prompt allows the user to Select an existing Deposit for review, create a NEW Deposit or Exit.

If there are multiple deposits within the same Deposit ticket# for different dates, the system displays a list of ALL matching Deposit tickets with the Deposit Dates so that the user can select one.

The display and prompt are written as follows when there are multiple dates for a single Deposit ticket#:

Select Deposit: AXXXXXX

1 AXXXXXX by: ARUSER,ONE on: 01/05/12 Amt: \$ 888.00 CLOSED

2 AXXXXXX by: ARUSER,TWO on: 12/06/14 Amt: \$ 725.00 OPEN

Enter the line# to view an existing deposit or (N) to create a NEW deposit or e(X)it: //

The user can create a NEW Deposit ticket \# or view an existing one. The user can only add to the Deposit for Today. Confirm / close the Deposit when appropriate.

49. The user will be able to add a NEW Deposit (with the same Deposit Ticket#) only if the existing Deposit Ticket(s) are on a different date(s) with status = CONFIRMED.

Example Scenarios:

- If the user selects a line#, the selected Deposit displays and follows the existing process for displaying / editing information.
- If the user selects NEW and the Deposit ticket number to be created already exists for today (i.e., Deposit Date), the following error message displays:
- ERROR: Deposit Ticket# already exists for today – Please select the appropriate line \# to modify the existing Deposit or e(X)it to enter a different Deposit Ticket#.”
- If the user selects NEW and the Deposit ticket number to be created does NOT already exist for today (i.e., Deposit Date) AND the previous deposit equals CONFIRMED, the system prompts the user for confirmation before creating a New Deposit:

Add Deposit Ticket# A999999 for today (Y/N)? NO// \<=default=NO

- If the user enters Y, the Deposit Ticket will be created - following existing process for creating the Deposit.
- If the user enters N, the user will return to the “Select Deposit:” prompt.
- If the user selects e(X)it, the system will return to the “Select Deposit:” prompt.

### Receipt# Lookup for Pharmacy Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Lockbox Receipt functionality allows the user to enter ECME# or RX# to get the claim# returned. (i.e., the user must enter ECME# or Rx# in Receipt when posting payments).

- Within ePayments: the lookup is available after the user creates the receipt.
- Outside of ePayments: the lookup is available in Receipt processing: Action Option: New Payment.

### Edit a Receipt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AR option to edit a receipt has been expanded to allow the user to edit the type of payment. This has been specifically tailored for electronic funds processing. The user can change the type of payment to CHECK/MO PAYMENT if the receipt status is open and the current value is EDI LOCKBOX and vice versa. The user can also change the type of payment to CHAMPVA if the receipt status is open, the current value is EDI LOCKBOX, and the first three characters of the trace number are TDA and vice versa.

The user can also change the type of payment from CHECK/MO PAYMENT to EDI LOCKBOX on receipts that have preexisting lines and add / attach a new EFT to the receipt if the user has the RCDPEAR key. The system then marks the EFT as unmatched if appropriate. The RCDPEAR key will allow the user to change the EFT number on receipts when the TYPE OF PAYMENT equals “EDI LOCKBOX.”

### Auto-Posted Receipt Report Acronym: APR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The APR option allows the user to display all auto-posted receipts to ensure payments are posted to patients’ third party claims. Refer to the EDI LOCKBOX (EPAYMENTS) REPORTS MENU section within this document for more information.

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A unique entry in the Security Key file (^DIC(19.1,) that may prevent access to a specific Option by including the key as part of the options’ entry in the Option file (^DIC (19,). Only users entered in the Holder field of the Security Key file may access the option.

## New or Modified Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RCDPE REMOVE DUPLICATES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New security key RCDPE REMOVE DUPLICATES is utilized to restrict usage of the Remove Duplicate EFT Deposits option.

50. See Section 6.10 and 6.13 for further information on this security key.

### RCDPE MARK ERA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new security key restricts usage of the Remove ERA from Active Worklist option.

51. See Section 6.8 for further information on this security key.

### PRCADJ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing security key PRCADJ has been modified to lock the Adjust (Inc / Dec) action of the ERA Worklist Research Menu to restrict its usage. This key should only be given to supervisory personnel.

52. See Section 3.3.3.1 for further information on this security key.

### RCDPE AGED PMT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New security key RCDPE AGED PMT is utilized to restrict usage of the Unposted EFT Override option.

### RCDPE ERA EXCEPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New security key RCDPE ERA EXCEPT is utilized to restrict usage of the Delete Message action from the EDI Lockbox 3rd Party Transmission Exceptions.

53. See Section 3.2.1.1 for further information on this security key.

### RCDPE AUTO DEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New security key RCDPE AUTO DEC is utilized to restrict usage of all options on the EDI Lockbox Parameters menu.

54. See Section 2.2 for further information on this security key.

### RCDPE REMOVE EEOB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New security key RCDPE REMOVE EEOB is utilized to restrict usage of the Remove option on the new EEOB Move / Copy / Remove option.

55. See Section 6.9 for further information on this security key.

### RCDPEAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security key RCDPEAR is utilized to restrict usage of the Admin Cost Adj and Re-establish Bill actions on both the ERA Worklist Scratch Pad Research Menu and the Auto-Post Awaiting Resolution (APAR) Scratch Pad Research Menu.

56. See Sections 2.1.2 and 3.5 respectively for further information on this security key.

Security key RCDPEAR is utilized when editing a receipt to change the TYPE OF PAYMENT from CHECK/MO PAYMENT to EDI LOCKBOX on receipts that have preexisting lines and allow a clerk to add / attach a new EFT to the receipt. It will also allow clerks to change the EFT number on receipts when the TYPE OF PAYMENT equals EDI LOCKBOX.

### RCDPEPP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security key RCDPEPP is utilized to restrict usage of the Mark for Auto Post, and Receipt Processing actions on the ERA Worklist and ERA Worklist Scratch Pad. Also, the security key RCDPEPP is utilized to restrict the usage of the Split / Edit a Line and Mark for Auto Post actions on the Auto-Post Awaiting Resolution (APAR) Scratch Pad.

57. See Sections 2.1.1, 2.1.2, and 3.5 respectively for further information on this security key.

### PRCFA SUPERVISOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing security key PRCFA SUPERVISOR has been removed as a lock for the option EDI Diagnostic Measures Reports menu that is located under the Finance AR Manager Menu.

The following options have been modified to be locked with the existing PRCFA SUPERVISOR security key:

- Disable-Enable DM Background Job / Reports
- Manually Start DM Extract
- Manually Transmit DM Extract

### RCDPE PAYER IDENTIFY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security key RCDPE IDENTIFY allows users to identify payers as being Tricare only, Pharmacy only, CHAMPVA only, all, or none. This functionality is accessed when choosing the Identify Payers option on the EDI Lockbox menu.

# Appendix A – Helpful Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistaU – Vista University has online training and documentation for a number of Training Initiatives including ePayments.

REDACTED

Revenue Guide - Provides a uniform and standard set of educational and reference materials for the benefit of Revenue Cycle staff and management.

REDACTED

Washington Publishing – Provider of services, publications and products to entities that develop or consume Electronic Data Interchange Standard Transaction.

REDACTED

ePay Rapid Response Team – email group including POC’s, ePay team, FSC, and EPS. Provides responses to questions from the field.

REDACTED

TMS VA Talent Management System (Formerly LMS – VA Learning Management System)

REDACTED

# Appendix B – Claim Level Adjustment Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Claim Adjustment Group Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Code identifying the general category of payment adjustment 1100.

| Code | Definition                 | Description                                                                                                                                                                                                                                     |
|------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CO   | Contractual Obligations    | Used when a joint payer / payee contractual agreement or a regulatory requirement resulted in an adjustment.                                                                                                                                    |
| CR   | Correction and Reversals   | Used for corrections and reversals to PRIOR claims                                                                                                                                                                                              |
| OA   | Other adjustments          |                                                                                                                                                                                                                                                 |
| PI   | Payer Initiated Reductions | Used when, in the opinion of the payer, the adjustment is not the responsibility of the patient, but there is no supporting contract between the provider and the payer (i.e., medical review or professional review organization adjustments). |
| PR   | Patient Responsibility     |                                                                                                                                                                                                                                                 |

<span id="_Toc183424298" class="anchor"></span>Table 14: Code and Definition

# Appendix C – Provider Level Adjustment Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Provider Level Adjustment Reason Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Code indicating reason for debit or credit memo or adjustment to invoice, debit or credit memo, or payment.

<table>
<caption><p><span id="_Toc30513948" class="anchor"></span>Table 15: Terms</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 33%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Definition</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>50</td>
<td>Late Charge</td>
<td>Code for the Late Claim Filing Penalty or Medicare Late Cost Report Penalty. PLB03-2 identifies the Medicare Late Cost Report Penalty with a code value of LR.</td>
</tr>
<tr class="even">
<td>51</td>
<td>Interest Penalty Charge</td>
<td>Code for the interest assessment for late filing. Medicare Part A provides code “IP” in PLB03-2.</td>
</tr>
<tr class="odd">
<td>72</td>
<td>Authorized Return</td>
<td><p>Monetary amount is the provider refund adjustment.</p>
<ul>
<li><blockquote>
<p>This adjustment acknowledges a refund received from a provider for previous overpayment. PLB03-2 should always contain an identifying reference number when the value is used.</p>
</blockquote></li>
<li><blockquote>
<p>PLB04 should contain a negative value.</p>
</blockquote></li>
<li><blockquote>
<p>This adjustment should always be offset by some other PLB adjustment referring to the original refund request or reason.</p>
</blockquote></li>
<li><blockquote>
<p>For balancing purposes, the amount related to this adjustment reason code must be directly offset. Medicare A will provide code “PR” in PLB03-2.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>90</td>
<td>Early Payment Allowance</td>
<td></td>
</tr>
<tr class="odd">
<td>AM</td>
<td>Applied to Borrower’s Account</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information. Use this monetary amount for the loan repayment amount.</td>
</tr>
<tr class="even">
<td>AP</td>
<td>Acceleration of Benefits</td>
<td><p>Code to reflect accelerated payment amounts or withholdings.</p>
<p>Withholding or payment identification is indicated by the sign of the amount in PLB04.</p>
<ul>
<li><blockquote>
<p>A positive value represents a withholding.</p>
</blockquote></li>
<li><blockquote>
<p>A negative value represents a payment. Medicare Part A will provide code “AP” for accelerated payment amounts and code “AW” for accelerated payment withholdings in PLB03-2.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>B2</td>
<td>Rebate</td>
<td>Code for the refund adjustment. Medicare Part A will provide code “RF” in PLB03-2.</td>
</tr>
<tr class="even">
<td>B3</td>
<td>Recovery Allowance</td>
<td><p>Medicare uses code to represent the check received from the provider for overpayments generated by payments from other payers.</p>
<p>This code differs from the provider refund adjustment identified with code 72. Part A or Part B trust fund for Medicare use is identified in PLB03-2.</p>
<ul>
<li><blockquote>
<p>“RA” is used for Medicare A.</p>
</blockquote></li>
<li><blockquote>
<p>“RB” is used for Medicare Part B.</p>
</blockquote></li>
</ul>
<p>PLB04 should contain a NEGATIVE value.</p>
<p>This adjustment should always be offset by some other PLB adjustment referring to the original refund request or reason. For balancing purposes, the amount related to this adjustment reason code must be directly offset.</p></td>
</tr>
<tr class="odd">
<td>BD</td>
<td>Bad Debt Adjustment</td>
<td>Code for the bad debt pass-through. Medicare Part A will provide code “BD” in PLB03-2.</td>
</tr>
<tr class="even">
<td>BN</td>
<td>Bonus</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</td>
</tr>
<tr class="odd">
<td>C5</td>
<td>Temporary Allowance</td>
<td>Tentative adjustment. Medicare Part A will provide code “TS” in PLB03-2.</td>
</tr>
<tr class="even">
<td>CR</td>
<td>Capitation Interest</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</td>
</tr>
<tr class="odd">
<td>CS</td>
<td>Adjustment</td>
<td><p>Provide supporting identification information in PLB03-2.</p>
<ul>
<li><blockquote>
<p>Medicare Part A will provide code “CA” for Manual Claim Adjustment, “AA” for Receivable Today.</p>
</blockquote></li>
<li><blockquote>
<p>Medicare Part A and Part B will provide code “RI” for Reissued Check Amount in PLB03-2.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>CT</td>
<td>Capitation Payment</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</td>
</tr>
<tr class="odd">
<td>CV</td>
<td>Capital Passthru</td>
<td>Medicare Part A will provide code “CP” in PLB03-2.</td>
</tr>
<tr class="even">
<td>CW</td>
<td>Certified Registered Nurse Anesthetist Passthru</td>
<td>Medicare Part A will provide code “CR” in PLB03-2.</td>
</tr>
<tr class="odd">
<td>DM</td>
<td>Direct Medical Education Passthru</td>
<td>Medicare Part A will provide code “DM” in PLB03-2.</td>
</tr>
<tr class="even">
<td>E3</td>
<td>Withholding</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information. Medicare Part A will provide code “CW” in PLB03-2.</td>
</tr>
<tr class="odd">
<td>FB</td>
<td>Forwarding Balance</td>
<td><p>Monetary amount for the balance forward. A negative value in PLB04 represents a balance moving forward to a future payment advice.</p>
<ul>
<li><blockquote>
<p>A positive value represents a balance being applied from a previous payment advice. A reference number should be supplied in PLB03-2 for tracking purposes.</p>
</blockquote></li>
<li><blockquote>
<p>Medicare Part A will provide code “BF” for negative values and “CO” for positive values in PLB03-2.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>FC</td>
<td>Fund Allocation</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information. The specific fund should be identified in PLB03-2.</td>
</tr>
<tr class="odd">
<td>GO</td>
<td>Graduate Medical Education Passthru</td>
<td>Medicare Part A will provide code “GM” in PLB03-2.</td>
</tr>
<tr class="even">
<td>IP</td>
<td>Incentive Premium Payment</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</td>
</tr>
<tr class="odd">
<td>IR</td>
<td>Internal Revenue Service Withholding</td>
<td></td>
</tr>
<tr class="even">
<td>IS</td>
<td>Interim Settlement</td>
<td>Number for the interim rate lump sum adjustment. Medicare Part A will provide code “IR” in PLB03-2.</td>
</tr>
<tr class="odd">
<td>J1</td>
<td>Nonreimbursable</td>
<td>Offset claim or service level data that reflects what could be paid if not for demonstration program or other limitation that prevents issuance of payment.</td>
</tr>
<tr class="even">
<td>L3</td>
<td>Penalty</td>
<td><p>Number for the capitation-related penalty, penalty withholding, or penalty release adjustment. Withholding or release is identified by the sign in PLB04. See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</p>
<p>Medicare Part A will provide code “PW” for Penalty Withhold, “RS” for Penalty Release, and “SW” for Settlement Withhold Amount in PLB03-2.</p></td>
</tr>
<tr class="odd">
<td>L6</td>
<td>Interest Owed</td>
<td>Monetary amount for the interest paid on claims in this 835. Support the amounts related to this adjustment by 2-062 AMT amounts, where AMT01 is “I.” Medicare Part A will provide code “IN” in PLB03-2.</td>
</tr>
<tr class="even">
<td>LE</td>
<td>Levy</td>
<td>IRS Levy</td>
</tr>
<tr class="odd">
<td>LS</td>
<td>Lump Sum</td>
<td><p>Disproportionate share adjustment, indirect medical education pass-through, non-physician pass-through, pass-through lump sum adjustment, or another pass-through amount. The specific type of lump sum adjustment must be identified in PLB03-2. Medicare Part A will provide code:</p>
<ul>
<li><blockquote>
<p>“DS” for Disproportionate Share Adjustment,</p>
</blockquote></li>
<li><blockquote>
<p>“IM” for Indirect Medical Education Passthrough</p>
</blockquote></li>
<li><blockquote>
<p>“NP” for Non-physician Passthrough</p>
</blockquote></li>
<li><blockquote>
<p>“PS” for Passthrough Lump Sum</p>
</blockquote></li>
<li><blockquote>
<p>“PO” for Other Passthrough in PLB03-2.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>OA</td>
<td>Organ Acquisition Passthru</td>
<td>Medicare Part A will provide code “KA” in PLB03-2.</td>
</tr>
<tr class="odd">
<td>OB</td>
<td>Offset for Affiliated Providers</td>
<td><p>Part A or Part B trust fund identification for the source of the offset is in PLB03-2.</p>
<ul>
<li><blockquote>
<p>Use “OA” for the Part A trust fund.</p>
</blockquote></li>
<li><blockquote>
<p>Use “OB” for the Part B trust fund in PLB03-2.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>PI</td>
<td>Periodic Interim Payment</td>
<td><p>Monetary amount for the PIP lump sum, PIP payment, or adjustment after PIP. The sign of the amount in PLB04 determines whether this is a payment (negative) or adjustment (positive).</p>
<p>Medicare Part A will provide code:</p>
<ul>
<li><blockquote>
<p>“PL” for PIP Lump Sum</p>
</blockquote></li>
<li><blockquote>
<p>“PP” for PIP Payment</p>
</blockquote></li>
<li><blockquote>
<p>“PA” for Adjustment After PIP in PLB03-2.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>PL</td>
<td>Payment Final</td>
<td>Number for the final settlement. Medicare Part A will provide code “FS” in PLB03-2.</td>
</tr>
<tr class="even">
<td>RA</td>
<td>Retro-activity Adjustment</td>
<td>See 2.2.10, Capitation and Related Payments and Adjustments, for additional information. Medicare Part A will provide code “TR” in PLB03-2.</td>
</tr>
<tr class="odd">
<td>RE</td>
<td>Return on Equity</td>
<td>Medicare Part A will provide code “RE” in PLB03-2.</td>
</tr>
<tr class="even">
<td>SL</td>
<td>Student Loan Repayment</td>
<td></td>
</tr>
<tr class="odd">
<td>TL</td>
<td>Third Party Liability</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</td>
</tr>
<tr class="even">
<td>WO</td>
<td>Overpayment Recovery</td>
<td><p>Use for the recovery of previous overpayment. An identifying number should be provided in PLB03-2.</p>
<p>See the notes on codes 72 and B3 for additional information about balancing against a provider refund. Medicare Part A will provide code “OR” in PLB03-2.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc30513948" class="anchor"></span>Table 15: Terms

# Appendix D – Terms and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides definitions and explanations for terms and acronyms relevant to the content presented within this document. For additional terms and acronyms, you can include references to other VA acronym and glossary repositories (e.g., VA Acronym Lookup and OIT Master Glossary).

| Term                                 | Definitions                                                                                                                                                                                                                                                                                   |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 835                                  | HIPAA standard terminology for an electronic health care claim payment or remittance advice.                                                                                                                                                                                                  |
| ACH                                  | Automatic Clearing House                                                                                                                                                                                                                                                                      |
| AR                                   | Accounts Receivable: The financial computer system used by the Department of Veterans Affairs Medical Centers.                                                                                                                                                                                |
| AITC                                 | Austin Information Technology Center (AITC) located in Austin, Texas; responsible for maintaining the hardware that supports the Lockbox system, including FSC servers, the Mailman routing system, and EPHRA database.                                                                       |
| AM                                   | Account Management                                                                                                                                                                                                                                                                            |
| APAR List                            | Auto-Post Awaiting Resolution list of EEOBs that were processed by the auto posting nightly job, but the system was unable to create and process a receipt.                                                                                                                                   |
| Austin Information Technology Center | Repository for databases located in Austin, Texas. (formerly Austin Automation Center)                                                                                                                                                                                                        |
| Auto-Decrease                        | VistA runs a nightly job to automatically make a decrease adjustment to a third-party medical, pharmacy or Tricare claims with payments that meet auto-decrease criteria. The automatic decrease is made with a contractual decrease adjustment amount that brings the claim balance to zero. |
| Auto-Post                            | VistA runs a nightly job to automatically post third party medical claims by creating and processing receipts for EEOBs that meet auto-posting criteria.                                                                                                                                      |
| BC                                   | Billed Charges                                                                                                                                                                                                                                                                                |
| CARC                                 | Claim Adjustment Reason Code                                                                                                                                                                                                                                                                  |
| CBO                                  | Chief Business Office                                                                                                                                                                                                                                                                         |
| CHAMPVA                              | Civilian Health and Medical Program of the Department of Veterans Affairs                                                                                                                                                                                                                     |
| CR                                   | Credit Receipt                                                                                                                                                                                                                                                                                |
| CR Document                          | Credit document; credits funds to site via FMS.                                                                                                                                                                                                                                               |
| CSA                                  | Claim Status Awaiting Resolution                                                                                                                                                                                                                                                              |
| Data Dictionary                      | The structure of a file, table, or any group of related information as defined for and by VA FileMan.                                                                                                                                                                                         |
| ECME                                 | Electronic Claims Management Engine                                                                                                                                                                                                                                                           |
| EDI                                  | Electronic Data Interchange                                                                                                                                                                                                                                                                   |
| EEOB                                 | Electronic Explanation Of Benefits                                                                                                                                                                                                                                                            |
| EFT                                  | Electronic Funds Transfer: the electronic form of what is currently sent as a paper check.                                                                                                                                                                                                    |
| Electronic Remittance Advice         | An electronic record transmitted to the sites with EEOB detail information included. An Electronic Remittance Advice can consist of one or more EEOBs from one payer.                                                                                                                         |
| EOB                                  | Explanation Of Benefits                                                                                                                                                                                                                                                                       |
| EPHRA                                | EEOB and Payment Healthcare Resolution Application; Web-based archival repository and research tool; allows user to search for missing EEOBs that are not received due to incorrect routing information; allows Austin FSC 224-unit staff to route unrouteable EEOB data.                     |
| ERA                                  | Electronic Remittance Advice; the equivalent to a stack of paper Explanation of Benefits (EOB) statements for many patients from one payer.                                                                                                                                                   |
| EXC                                  | EDI Lockbox 3rd Party Exceptions                                                                                                                                                                                                                                                              |
| Explanation Of Benefits              | A document from a payer that details the amount of payment on a claim and if not paid in full, the reasons for it.                                                                                                                                                                            |
| Financial Management System          | The financial computer system used by the Department of Veterans Affairs.                                                                                                                                                                                                                     |
| FMS                                  | Financial Management System. FMS interacts with VistA to manage VHA financial data.                                                                                                                                                                                                           |
| FSC                                  | Financial Services Center; located in Austin, Texas; FSC runs GENTRAN translator software on FSC servers; FSC servers parse incoming EFT and ERA data and routes data to the appropriate VistA AR system based on Provider Tax ID information within each transaction.                        |
| GENTRAN                              | Software used to translate incoming 835 data into VistA readable flat file data; software is loaded onto FSC server.                                                                                                                                                                          |
| GLDB                                 | General Ledger Detail Balance                                                                                                                                                                                                                                                                 |
| HIPAA                                | Health Insurance Portability and Accountability Act of 1996                                                                                                                                                                                                                                   |
| IB                                   | Integrated Billing Package                                                                                                                                                                                                                                                                    |
| ICN                                  | Internal control number. This number is sent by the payer, and is unique to each payer; it identifies the claim in the payer’s system. It is given by AR to the payer customer service representative to help locate the information in the payer’s system.                                   |
| IEN                                  | VA Internal Entry Number.                                                                                                                                                                                                                                                                     |
| Implementation Manager               | The person or group whose function is to field questions and solve problems for the sites that are data or process related to transmissions from EDI Lockbox.                                                                                                                                 |
| Insurance Company ID                 | ID associating each transaction with the payer; typically, the payer’s tax ID number and is not related to any other Payer ID stored in VistA for other purposes.                                                                                                                             |
| Integration Agreement                | Programming agreements made between two VistA packages enabling the sharing / management of data and or functions.                                                                                                                                                                            |
| List Manager Screen                  | A graphical user interface program used by VistA to present data to the users. From the List Manager Screen, the user can select options programmed and set up for the data displayed.                                                                                                        |
| Mail Group                           | A VA MailMan structure that defines a subset of VA MailMan users. A Mail Group is used to communicate with a group of users. The Mail Group user subset can easily be modified without having to change software logic.                                                                       |
| MailMan Message                      | The messaging system used to communicate between the users of the VistA software. MailMan messages will be used to process automatic payments and to communicate between the Accounts Receivable software and the users.                                                                      |
| Matched                              | An ERA that has been associated with an EFT, a paper check, or a zero-dollar payment.                                                                                                                                                                                                         |
| MCCF                                 | Medical Care Collection Fund                                                                                                                                                                                                                                                                  |
| MLB                                  | This mail group receives all transmission messages relating to EDI Lockbox. These messages contain the detailed transmission data.                                                                                                                                                            |
| NACHA                                | National Automated Clearinghouse Association                                                                                                                                                                                                                                                  |
| NAIC                                 | National Association of Insurance Commissioners                                                                                                                                                                                                                                               |
| Not matched                          | An ERA that has not yet been associated with an EFT, a paper check, or a zero-dollar payment; user will always select unmatched when searching for an ERA that should match the paper check received.                                                                                         |
| NPI                                  | National Provider Identifier                                                                                                                                                                                                                                                                  |
| Option                               | A unique method defined in the Option file (^DIC(19,). Options are usually defined as part of a user driven menu system but may be invoked as extensions of other options or VA MailMan messages.                                                                                             |
| PD                                   | Product Development                                                                                                                                                                                                                                                                           |
| PHI                                  | Protected Health Information                                                                                                                                                                                                                                                                  |
| PLB                                  | Provider Level Adjustments                                                                                                                                                                                                                                                                    |
| PNC                                  | Pittsburgh National Corporation and Provident National Corporation                                                                                                                                                                                                                            |
| POC                                  | Point of Contact. The ePay network includes an ePay POC per VISN.                                                                                                                                                                                                                             |
| Posted ERA                           | Indicates the AR processing is complete.                                                                                                                                                                                                                                                      |
| RARC                                 | Remittance Advice Remark Code                                                                                                                                                                                                                                                                 |
| Related SRS Module                   | The numeric and title of the functionality requested in the SRS, which the SDD is implementing.                                                                                                                                                                                               |
| Routines                             | A unique identifiable containment of software pertinent to a computer system function. The routines contain the programming logic to implement the functionality for the EDI Lockbox Project.                                                                                                 |
| RSC                                  | Revenue Source Code                                                                                                                                                                                                                                                                           |
| Scratchpad                           | VistA screen containing ERA \#, name and ID of payer, amount paid, and the trace number. The scratchpad also contains list manager options that conveniently store frequently used AR / ePay options in one centralized location.                                                             |
| Security Key                         | A unique entry in the Security Key file (^DIC(19.1,) that may prevent access to a specific Option by including the key as part of the options’ entry in the Option file (^DIC(19,). Only users entered in the Holder field of the Security Key file may access the option.                    |
| Sequence Number                      | A sequential number assigned in VistA to each incoming ERA.                                                                                                                                                                                                                                   |
| Software Requirements Specifications | Document that outlines the functionality requirements for a project.                                                                                                                                                                                                                          |
| SSN                                  | Social Security Number                                                                                                                                                                                                                                                                        |
| TIN                                  | Tax ID Number                                                                                                                                                                                                                                                                                 |
| TPJI                                 | Third Party Joint Inquiry                                                                                                                                                                                                                                                                     |
| TR Document                          | Transfer document; transfers funds to appropriate revenue source code.                                                                                                                                                                                                                        |
| Trace Number                         | A number assigned by the insurance company to identify which EFT payment is associated with what ERA; used to re-associate electronic remittance payment with data.                                                                                                                           |
| Transaction and code sets            | Standard for Electronic transactions set forth by HIPAA. Compliance is mandatory for payers, providers, clearinghouses, or anyone who receives or submits electronic health information.                                                                                                      |
| Unposted ERA                         | Indicates the AR processing is not complete; an unposted ERA needs to be processed, closed, and posted, just like a paper EOB that must be verified and / or adjusted before closing.                                                                                                         |
| VA                                   | Department of Veterans Affairs                                                                                                                                                                                                                                                                |
| VAMC                                 | Veterans Affairs Medical Center                                                                                                                                                                                                                                                               |
| VHA                                  | Veterans Health Administration                                                                                                                                                                                                                                                                |
| VISN                                 | Veterans Integrated Service Network                                                                                                                                                                                                                                                           |
| VistA                                | Veterans Health Information System and Technology Architecture                                                                                                                                                                                                                                |
| VistaU                               | Vista University has online training and documentation for several Training Initiatives including ePayments.                                                                                                                                                                                  |
| WL                                   | Work List: A listing of all ERA information sent from payers. It can be viewed by posted or unposted ERA’s, specific payers, and matched or not matched ERA’s.                                                                                                                                |

<span id="_Toc183424300" class="anchor"></span>Table 16: Subject of Bulletin / When it’s Generated / How to Resolve

# Appendix E – 3rd Party EDI Lockbox Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3<sup>rd</sup> Party EDI Lockbox Bulletins

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 42%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>Subject</th>
<th>Generate</th>
<th>Resolve</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ERRONEOUS TAX ID ON ERA</td>
<td><p>Message sent when the payer sends an ERA to the EDI Lockbox bank and they do not include a valid V.A. tax id on the transmission.</p>
<p>To correctly route the data to the proper site, the tax id number must be corrected before the data is transmitted to the site by either EPHRA or the EDI Lockbox group in Austin.</p>
<p>If this occurs, this bulletin is received by the site to alert that the payer has either omitted or has an erroneous tax id for the site.</p></td>
<td>What to do: Contact the insurance company and provide the correct tax id for the site.</td>
</tr>
<tr class="even">
<td>EDI LOCKBOX SERVER OPTION ERROR</td>
<td><p>Message sent when the EDI Lockbox system receives a message where:</p>
<ul>
<li><blockquote>
<p>Message code is invalid for EDI Lockbox.</p>
</blockquote></li>
<li><blockquote>
<p>This message has no ending $ or 99 record.</p>
</blockquote></li>
<li><blockquote>
<p>Message file problem - no message stored.</p>
</blockquote></li>
<li><blockquote>
<p>Message file problem - message partially stored.</p>
</blockquote></li>
<li><blockquote>
<p>Invalid mail group designated for EDI Lockbox errors.</p>
</blockquote></li>
<li><blockquote>
<p>Message header error – the format of the header record on an EFT or ERA was not correct.</p>
</blockquote></li>
</ul></td>
<td>What to do: For all situations, contact the IRM as there may be mailman or server problems or EVS if there are software errors.</td>
</tr>
<tr class="odd">
<td>EDI LBOX ALERT - ERA/EFT NOT FROM AUSTIN</td>
<td>Message sent when an ERA or EFT is received by the EDI Lockbox system and the message did not come from Austin.</td>
<td>What to do: Contact the IRM to report this breach of security.</td>
</tr>
<tr class="even">
<td>EDI LBOX - EEOB FROM &lt;site name&gt; FOR &lt;payer name&gt;</td>
<td>Message sent when an EEOB is transferred into the site from another site that received it in error.</td>
<td>What to do: In EDI Lockbox Data Exception Processing, find the EEOB and accept it (via file EEOB) or delete it if it does not belong to the user.</td>
</tr>
<tr class="odd">
<td>TOTALS MISMATCH ON EFT-ERA MATCH</td>
<td>Message sent when an EFT and an ERA are matched with the same trace number and insurance company id number, but the totals indicated on the two records do not match.</td>
<td>What to do: Contact the payer to determine why this has occurred.</td>
</tr>
<tr class="even">
<td>DUPLICATE EFT DEPOSIT RECORD RECEIVED</td>
<td>DUPLICATE EFT DEPOSIT RECORD RECEIVED.</td>
<td>What to do: Report this to the IRM and the implementation manager to determine why it happened.</td>
</tr>
<tr class="odd">
<td>EXCEPTIONS EFT DEPOSIT AND MATCH EFTs TO ERAs &lt;date&gt;</td>
<td><p>Message sent when exceptions are encountered when the system attempts to post EFT deposits or to match EFTs with ERAs.</p>
<p>A Nightly via the EDI Lockbox nightly job that creates and processes the deposit for any EFTs received and not yet posted and that attempts to match unmatched ERA records to unmatched EFT records. If no exceptions are found, this is stated in the bulletin.</p>
<p>Exception conditions include:</p>
<ol type="1">
<li><blockquote>
<p>The nightly job to post EFT deposits and match EFTs to ERAs could not be run because another match process was already running.</p>
</blockquote></li>
<li><blockquote>
<p>An invalid checksum value was found for an EFT on file and the EFT deposit was not sent to FMS.</p>
</blockquote></li>
<li><blockquote>
<p>A deposit or a receipt could not be added for an EFT. The EFT deposit was not sent to FMS.</p>
</blockquote></li>
</ol></td>
<td><p>What to do:</p>
<p>Only one process to match ERAs to EFTs may be running at any given time.</p>
<ul>
<li><blockquote>
<p>If happening on the manual process, try again later.</p>
</blockquote></li>
<li><blockquote>
<p>If on the nightly job or the problem persists, show the bulletin to the IRM as they can research the problem.</p>
</blockquote></li>
</ul>
<p>This indicates the EFT record was modified since it was stored in VistA. IRM should be notified of the problem and the EFT will need to be retransmitted to the site from Austin (the existing record will be overwritten with the retransmitted data.</p>
<p>This indicates a data problem with the record or a software problem. Ask Austin to retransmit. If the problem persists, contact the IRM and / or EVS.</p></td>
</tr>
<tr class="even">
<td>EDI LOCKBOX TOTALS RECORD EXCEPTION</td>
<td><p>Message sent when the EDI Lockbox server stores an ERA record in different parts. Each EEOB within the ERA is stored in IB in the EXPLANATION OF BENEFITS file.</p>
<p>All the detail pertaining to payment made regarding the claim is stored here. The ERA total amount paid and all detail not pertaining to an individual claim is stored in A/R. This exception is received when the ERA totals record cannot be stored in A/R.</p></td>
<td>What to do: Contact EVS.</td>
</tr>
<tr class="odd">
<td>AR LOCKBOX ERA UNMATCHED AGING REPORT FOR &lt;date&gt;</td>
<td>When received: Produced by the nightly EDI Lockbox job. It contains an ERA UNMATCHED AGING summary report.</td>
<td>What to do: This is FYI only. No action is needed.</td>
</tr>
<tr class="even">
<td>AUTO DAILY ACTIVITY SUMMARY REPORT - &lt;date&gt;</td>
<td>When received: Produced by the nightly EDI Lockbox job. It contains a daily activity report indicating the matches made and the EFT deposits created / posted to FMS.</td>
<td>What to do: This is FYI only. No action is needed.</td>
</tr>
<tr class="odd">
<td>INVALID EFT DEPOSIT NUMBER</td>
<td>When received: When the EDI Lockbox server receives an EFT whose deposit number does not start with a 469 or HAC.</td>
<td>What to do: Contact the implementation manager.</td>
</tr>
<tr class="even">
<td>ELECTRONIC EDI LOCKBOX MESSAGE DELETED</td>
<td>When received: Any time a user uses the delete message action within EDI Lockbox transmission exception processing to delete an exception message.</td>
<td>What to do: FYI – the user might want to follow up to be sure the deletion was justified.</td>
</tr>
<tr class="odd">
<td>ELECTRONIC EEOB DETAIL EXCEPTION REMOVED</td>
<td>Any time a user uses the delete message action within EDI Lockbox data exception processing to delete an exception message.</td>
<td>What to do: FYI – the user might want to follow up to be sure the exception removal was justified.</td>
</tr>
<tr class="even">
<td>LOCKBOX EEOB DETAIL RE-FILE ATTEMPTED TO IB</td>
<td>When received: When an attempt is made to re-file an EEOB that could not be stored in IB due to a data exception by using the FILE EEOB in IB action in EDI Lockbox Data Exception Processing.</td>
<td>What to do: FYI only. No action required.</td>
</tr>
<tr class="odd">
<td>Unmatched ERAs &gt; 30 days</td>
<td>The listed ERAs were received more than 30 days ago and have not yet been matched.</td>
<td>What to do: Review the ERAs and expedite processing.</td>
</tr>
<tr class="even">
<td>Matched/Not Posted ERAs &gt; 30 days</td>
<td>The listed ERAs were received more than 30 days ago and have been matched but have not been posted</td>
<td>What to do: Review the ERAs and expedite processing.</td>
</tr>
<tr class="odd">
<td>EFTs greater than 14 days</td>
<td>The listed EFTs were received more than 14 days ago.</td>
<td>What to do: Review the EFTs and expedite processing.</td>
</tr>
<tr class="even">
<td>EDI CARC_RARC SERVER OPTION ERROR</td>
<td>When received: Any time an error is found while processing CARC &amp; RARC data from FSC.</td>
<td>What to do: Review the type of errors report and expedite processing with FSC and local IRM.</td>
</tr>
</tbody>
</table>

# Solving ePayment Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to Remove Aged EFTs from the EFT Unmatched Aging Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM can use the following process to change the status of an EFT to “PAPER EOB MATCH”, which will allow the EFT to fall off the aged EFT report. A complete trace number(s) is needed to complete the process.

Due to database integrity issue, IRM may elect not to do this workaround.

VA FileMan Version 22.0

1 Enter or Edit File Entries

2 Print File Entries

3 Search File Entries

5 Inquire to File Entries

8 Data Dictionary Utilities ...

Select VA FileMan Option: ENTER or Edit File Entries.

INPUT TO WHAT FILE: (file needed).

EDIT WHICH FIELD: ALL// ??

Choose from:

.01 EFT TRANSACTION

.02 PAYER NAME

.03 PAYER ID

.04 TRACE \#

.05 PROVIDER TAX ID SENT

.06 TAX ID CORRECTION

.07 AMOUNT OF PAYMENT

.08 MATCH STATUS

.09 RECEIPT \#

.1 ERA RECORD

.11 EFT RECORDED AT SITE

.12 DATE CLAIMS PAID

.13 DATE RECEIVED

.14 TRANSACTION \#

.15 ACH TRACE \#

2 ERROR MESSAGES (word-processing)

EDIT WHICH FIELD: ALL// .08 MATCH STATUS.

THEN EDIT FIELD:

Select EDI THIRD PARTY EFT DETAIL EFT TRANSACTION: \<enter trace number\>

MATCH STATUS: UNMATCHED// ?

Enter the status to indicate if the payment has been matched to an ERA.

Choose from:

-1 MATCHED WITH ERRORS

0 UNMATCHED

1 MATCHED

2 PAPER EOB MATCH

MATCH STATUS: MATCHED// 2 PAPER EOB MATCH