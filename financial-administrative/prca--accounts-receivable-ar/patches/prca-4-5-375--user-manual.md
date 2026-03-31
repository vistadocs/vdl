---
title: PRCA*4.5*375 Accounts Receivable ePayments User Manual (EDI) Lockbox
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Accounts Receivable ePayments  (EDI) Lockbox
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: archive
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5*375
group_key: "PRCA:PRCA:4.5"
file_numbers: []
security_keys: []
menu_options: 15
description: 
audience: 
keywords: 
  - report
  - auto
  - table
  - contents
  - date
  - payment
  - receipt
  - claim
  - eeob
  - payer
page_count: 0
word_count: 44466
section_count: 79
table_count: 26
figure_count: 0
appendix_count: 5
has_toc: False
is_stub: False
pub_date: May 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)_Archive/epayments_edi_lockbox_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)_Archive/epayments_edi_lockbox_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=244"
---

ePayments User Manual

(EDI Lockbox)

User Manual

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/001.png)

May 2021

Veterans Affairs

Product Development (PD)

*(This page included for two-sided copying.)*Revision History

|                |              |                                                                                       |                                         |                                         |
|----------------|--------------|---------------------------------------------------------------------------------------|-----------------------------------------|-----------------------------------------|
| Date       | Revision | Description                                                                       | Project Manager                     | Technical Writer                    |
| May 2021       | 14.0         | ePayments Patch updates for PRCA\*4.5\*375                                            | MCCF EDI TAS ePayments Development Team | MCCF EDI TAS ePayments Development Team |
| October 2020   | 13.0         | ePayments Patch updates for PRCA\*4.5\*345                                            | REDACTED                                | REDACTED                                |
| March 2019     | 12.0         | ePayments Patch updates for PRCA\*4.5\*332                                            | REDACTED                                | REDACTED                                |
| November 2018  | 11.0         | ePayments Patch updates for PRCA\*4.5\*326                                            | REDACTED                                | REDACTED                                |
| June 2018      | 10.0         | ePayments Patch updates for PRCA\*4.5\*321                                            | REDACTED                                | REDACTED                                |
| October 2017   | 9.0          | ePayments Patch updates for PRCA\*4.5\*318                                            | REDACTED                                | REDACTED                                |
| March 2017     | 8.0          | ePayments Patch updates for PRCA\*4.5\*317                                            | REDACTED                                | REDACTED                                |
| August 2016    | 7.0          | ePayments Patch updates for PRCA\*4.5\*316                                            | REDACTED                                | REDACTED                                |
| May 2016       | 6.0          | Comprehensive updates throughout in accordance with PRCA\*4.5\*303 and PRCA\*4.5\*304 | REDACTED                                | REDACTED                                |
| March 2015     | 5.0          | ePayments Patch updates: PRCA\*4.5\*298                                               | REDACTED                                | REDACTED                                |
| July 2012      | 4.0          | Changes for deposit ticket number patch PRCA\*4.5\*283 (page 56).                     | REDACTED                                | REDACTED                                |
| April 2012     | 3.0          | Patch updates: PRCA\*4.5\*284                                                         | REDACTED                                | REDACTED                                |
| January 2012   | 2.0          | ePayments II updates - patches IB\*2.0\*451 and PRCA\*4.5\*276                        | REDACTED                                | REDACTED                                |
| September 2011 | 1.0          | Initial Release                                                                       | REDACTED                                | REDACTED                                |

<u>  
</u>*(This page included for two-sided copying.)*Table of Contents

*  
(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Business Uses’](#business-uses)
  - [Timeframes](#timeframes)
  - [Patches](#patches)
    - [AR Patch PRCA\4.5\284](#ar-patch-prca45284)
    - [AR Patch PRCA \4.5\303](#ar-patch-prca-45303)
    - [### AR Patch PRCA\4.5\304](#ar-patch-prca45304)
    - [AR Patch PRCA\4.5\316](#ar-patch-prca45316)
    - [AR Patch PRCA\4.5\317](#ar-patch-prca45317)
    - [AR Patch PRCA\4.5\318](#ar-patch-prca45318)
    - [AR Patch PRCA\4.5\321](#ar-patch-prca45321)
    - [AR Patch PRCA\4.5\326](#ar-patch-prca45326)
    - [AR Patch PRCA\4.5\332](#ar-patch-prca45332)
    - [AR Patch PRCA\4.5\345](#ar-patch-prca45345)
    - [AR Patch PRCA\4.5\375](#ar-patch-prca45375)
  - [New Terminology](#new-terminology)
  - [Process Flow](#process-flow)
- [Getting Started with ePayments](#getting-started-with-epayments)
  - [Menus and Screens](#menus-and-screens)
  - [ERA List – Worklist screen](#era-list-worklist-screen)
  - [ERA Worklist/Scratchpad screen](#era-worklistscratchpad-screen)
  - [ERA/835 Screens for ePayments](#era835-screens-for-epayments)
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
  - [Mail groups](#mail-groups)
  - [How to read an ERA/835](#how-to-read-an-era835)
  - [Workload Notifications](#workload-notifications)
    - [Unmatched ERAs \> 30 days](#unmatched-eras-30-days)
    - [PAPER Matched/Not Posted ERAs \> 30 Days](#paper-matchednot-posted-eras-30-days)
    - [EFT Matched/Not Posted ERAs \> 30 days Bulletin](#eft-matchednot-posted-eras-30-days-bulletin)
    - [Unmatched EFTs \> 14 days](#unmatched-efts-14-days)
    - [Suspense Entry Bulletin](#suspense-entry-bulletin)
- [Payments Processing](#payments-processing)
  - [Check Email](#check-email)
  - [Exception Processing](#exception-processing)
    - [Transmission Exceptions](#transmission-exceptions)
    - [Data Exceptions](#data-exceptions)
    - [Non-Released Prescriptions](#non-released-prescriptions)
  - [Working the EEOB Scratchpad](#working-the-eeob-scratchpad)
    - [ERA List - Worklist Actions](#era-list-worklist-actions)
    - [Worklist Actions](#worklist-actions)
    - [### Change View](#change-view)
    - [Research Menu Actions](#research-menu-actions)
    - [Example of processing a Paper Check and ERA](#example-of-processing-a-paper-check-and-era)
    - [Example of processing a matched ERA and EFT](#example-of-processing-a-matched-era-and-eft)
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
    - [APAR - Actions](#apar-actions)
    - [APAR Scratchpad - Actions](#apar-scratchpad-actions)
  - [Auto-Decrease of Medical Claims](#auto-decrease-of-medical-claims)
  - [Auto-Decrease of Pharmacy Claims](#auto-decrease-of-pharmacy-claims)
  - [# The EFT has been accepted by FMS](#the-eft-has-been-accepted-by-fms)
  - [FMS](#fms)
  - [Three Day EFT Cycle](#three-day-eft-cycle)
  - [EFT Deposits](#eft-deposits)
- [NPI](#npi)
- [Additional Functionality](#additional-functionality)
  - [Auto–Audit](#autoaudit)
    - [Update Rate Types for Auto-audit](#update-rate-types-for-auto-audit)
    - [Process Open Bills/Paper Claims](#process-open-billspaper-claims)
    - [Validate Bill Data and Status](#validate-bill-data-and-status)
    - [Process AR entry](#process-ar-entry)
    - [Required Security Key](#required-security-key)
  - [Automatic Match EFTs to ERAs Acronym: MA](#automatic-match-efts-to-eras-acronym-ma)
  - [EFT Manual Match Acronym: MM](#eft-manual-match-acronym-mm)
  - [Mark Ø-Balance EFT Matched Acronym: ZB](#mark-ø-balance-eft-matched-acronym-zb)
  - [Unmatch an ERA Acronym: UN](#unmatch-an-era-acronym-un)
  - [Update ERA Posted using Paper EOB Acronym: UP](#update-era-posted-using-paper-eob-acronym-up)
  - [Remove ERA from Active Worklist Acronym: REM](#remove-era-from-active-worklist-acronym-rem)
  - [EEOB Move/Copy/Remove Acronym: MCR](#eeob-movecopyremove-acronym-mcr)
  - [Remove Duplicate EFT Deposits Acronym: REFT](#remove-duplicate-eft-deposits-acronym-reft)
  - [EEOB Indicator](#eeob-indicator)
  - [Receipt Processing](#receipt-processing)
  - [Unposted EFT Override Acronym: OEFT](#unposted-eft-override-acronym-oeft)
  - [Identify Payers Acronym: IDP](#identify-payers-acronym-idp)
- [EDI Lockbox (ePayments) Reports Menu Acronym: REP](#edi-lockbox-epayments-reports-menu-acronym-rep)
  - [EFT Daily Activity Report Acronym: DA](#eft-daily-activity-report-acronym-da)
  - [EFT Unmatched Aging Report Acronym: EFT](#eft-unmatched-aging-report-acronym-eft)
  - [ERA Unmatched Aging Report Acronym: ERA](#era-unmatched-aging-report-acronym-era)
  - [Pending EFT Override Report Acronym: PEO](#pending-eft-override-report-acronym-peo)
  - [EFT/ERA Trending Report Acronym: ETR](#eftera-trending-report-acronym-etr)
  - [Unapplied EFT Deposits Report Acronym: UN](#unapplied-eft-deposits-report-acronym-un)
  - [## Active Bills with EEOB Report Acronym: AB](#active-bills-with-eeob-report-acronym-ab)
  - [Auto Decrease Adjustment Report Acronym: AD](#auto-decrease-adjustment-report-acronym-ad)
  - [Auto-Post Report Acronym: AP](#auto-post-report-acronym-ap)
  - [Auto-Posted Receipt Report Acronym: APR](#auto-posted-receipt-report-acronym-apr)
  - [Auto Parameter History Report Acronym: APH](#auto-parameter-history-report-acronym-aph)
  - [CARC Data Report Acronym: CR](#carc-data-report-acronym-cr)
  - [Duplicate EFT Audit report Acronym: DUPR](#duplicate-eft-audit-report-acronym-dupr)
  - [ERA Status Change Audit Report Acronym: ESC](#era-status-change-audit-report-acronym-esc)
  - [EFT Transaction Audit Report Acronym: ETA](#eft-transaction-audit-report-acronym-eta)
  - [First Party COPAY Auto-Decrease Report Acronym: FAD](#first-party-copay-auto-decrease-report-acronym-fad)
  - [First Party COPAY Manual vs Auto-Decrease Report Acronym: FAM](#first-party-copay-manual-vs-auto-decrease-report-acronym-fam)
  - [EEOB Move/Copy/Remove Audit Report Acronym: MCR](#eeob-movecopyremove-audit-report-acronym-mcr)
  - [EEOBs Marked for Auto-Post Audit Report Acronym: EMA](#eeobs-marked-for-auto-post-audit-report-acronym-ema)
  - [Provider Level Adjustments (PLB) Report Acronym: PLB](#provider-level-adjustments-plb-report-acronym-plb)
  - [ERAs Posted with Paper EOB Audit Report Acronym: POSR](#eras-posted-with-paper-eob-audit-report-acronym-posr)
  - [Payer Implementation Report Acronym: PX](#payer-implementation-report-acronym-px)
  - [CARC/RARC Quick Search Acronym: QS](#carcrarc-quick-search-acronym-qs)
  - [Remove ERA from Active Worklist Audit Report Acronym: REMR](#remove-era-from-active-worklist-audit-report-acronym-remr)
  - [Link Payment Tracking Report Acronym:SR](#link-payment-tracking-report-acronymsr)
  - [CARC/RARC Table Data Report Acronym: TB](#carcrarc-table-data-report-acronym-tb)
  - [View/Print ERA Acronym: VP](#viewprint-era-acronym-vp)
  - [EFT Deposit Reconciliation Report Acronym: DEP](#eft-deposit-reconciliation-report-acronym-dep)
- [National Reports for ePayments Data](#national-reports-for-epayments-data)
  - [EDI VOLUME STATISTICS Report](#edi-volume-statistics-report)
  - [ERA/EFT TRENDING Report](#eraeft-trending-report)
  - [EDI Diagnostic Measures Extracts Menu](#edi-diagnostic-measures-extracts-menu)
  - [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
- [Enhancements to non-EDI Lockbox Menus](#enhancements-to-non-edi-lockbox-menus)
  - [Agent Cashier Menu](#agent-cashier-menu)
    - [Extended Check/Trace/Credit Card Search Acronym: EX](#extended-checktracecredit-card-search-acronym-ex)
    - [Link Payment Acronym: LP](#link-payment-acronym-lp)
    - [Link Payment to Multiple Claims](#link-payment-to-multiple-claims)
    - [Deposit Processing Acronym: DP](#deposit-processing-acronym-dp)
    - [### Receipt# Lookup for Pharmacy Claims](#receipt-lookup-for-pharmacy-claims)
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
- [APPENDIX A – Helpful Links](#appendix-a-helpful-links)
- [APPENDIX B – Claim Level Adjustment Codes](#appendix-b-claim-level-adjustment-codes)
  - [CLAIM ADJUSTMENT GROUP CODE](#claim-adjustment-group-code)
  - [# APPENDIX C – Provider Level Adjustment Codes](#appendix-c-provider-level-adjustment-codes)
  - [PROVIDER LEVEL ADJUSTMENT](#provider-level-adjustment)
    - [Provider Level Adjustment Reason Code](#provider-level-adjustment-reason-code)
- [APPENDIX D - Definitions](#appendix-d-definitions)
- [APPENDIX E – 3<sup>rd</sup> Party EDI Lockbox Bulletins](#appendix-e-3suprdsup-party-edi-lockbox-bulletins)
- [Solving ePayment Problems](#solving-epayment-problems)
  - [How to Remove Aged EFT’s from the EFT Unmatched Aging Report](#how-to-remove-aged-efts-from-the-eft-unmatched-aging-report)

## Business Uses’

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Insurance Portability and Accountability Act of 1996 (HIPAA) or Public Law 101-191 requires healthcare plans and providers who conduct transactions electronically to comply with rules of standardization. HIPAA has several purposes but defines standards through rules and compliance of transactions and code sets. National standards allow for compatible formats between providers and third party payers. PNC Bank in Pennsylvania functions as the VA 3rd Party Lockbox bank and will accept those standard transactions from payers on behalf of VA. The bank makes a daily deposit of 3rd party payments to US Treasury. They will also transmit deposit information in the form of an Electronic Funds Transfer (EFT) and data about the payment in the form of an Electronic Remittance Advice (ERA) to the Austin Financial Services Center (FSC). The Austin FSC will accept those transactions from the bank and translate those files into a VistA readable format. The FSC will then forward those files to the appropriate VistA AR package by way of Mailman messages. In addition, the FSC will also transmit the ERA and EFT data files to Explanation of Benefits (EOB) Payment Healthcare Remittance Advice (EPHRA).

VistA, therefore, was enhanced to allow receipt processing and posting of electronic remittance data sent by payers. Additionally, VistA and FMS were enhanced to accommodate receipt and processing of 3rd party electronic payment data.

The ePayments software will supplement the current accounts receivable process by eliminating some data entry and automating the process of entering payments on a field service receipt. The software will now create an electronic receipt that replaces the paper field service receipt for payments received via the ePayments software.

## Timeframes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePayments software was released to sites on October 10, 2003 with an installation compliance deadline of October 16, 2003. The payer community is working to make their transactions HIPAA compliant. Once payers are ready to transmit, they will work with our Lockbox Bank to enroll in the VA ePayments program. After enrolling, each payer will go through a rigorous transaction testing process with our Lockbox bank and any Clearinghouse that may be integrated. Testing ensures that the payer’s 835 EFT and ERA transmissions:

1.  Conform to acceptable HIPAA and X12 transaction standards and
2.  Can be received and forwarded by internal VA processing and messaging systems.

The entire payer community was not expected to be ready to transmit immediately following the HIPAA deadline of October 16, 2003. Payer implementation is expected to be staggered but initially covered the payers with the highest VHA claim submission volume across each VISN. Sites should expect to continue with paper processing as the electronic payers are brought on line.

Since releasing the ePayments system, VHA has been honored by NACHA, the Electronic Payments Association, for its success in implementing a nationwide electronic health care remittance and payment processing system that complies with the electronic transaction standards of the HIPAA.[^1] PNC Bank in Pittsburgh, Pennsylvania serves as VHA’s lockbox bank and has partnered with VHA to enroll payers in this new, electronic business process. VHA’s experience with payers has been positive with regard to the payer’s capability to produce and transmit ERAs. However, less than one percent of VHA’s active payers are producing and transmitting an EFT. While VHA’s primary goal is to enroll its payer community for ERA, VHA believes that additional benefits of HIPAA will be realized through both ERA and EFT processing. Because HIPAA regulations specify that payers comply with a request for ERA in response to a provider’s claim, payers’ business organizations may not be focused on the development of EFT.

## Patches 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### AR Patch PRCA\*4.5\*284

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Rename existing option – Mark ERA Return to Payer

> Per request from the Chief Business Office (CBO), the existing Mark ERA Returned to Payer option, which is located on the EDI Lockbox parent menu, has been renamed to <u>Remove ERA from Active Worklist</u>. To accurately reflect the renamed option, the help text associated with the option has been updated to reflect the removal of an ERA off the ERA Worklist. The basic functionality of the option remains intact as it will continue to provide the capability to remove an unmatched ERA off the ERA Worklist.

2.  Rename existing option – Mark ERA Return to Payer Audit report

> The existing Mark ERAs Returned to Payer Audit Report, which is located on the EDI Lockbox Reports Menu, has been renamed to <u>Remove ERA from Active Worklist Audit Report.</u>

3.  Change default answer in prompt - Update ERA Posted Using Paper EOB

> When an automatic update is performed on an ERA, the default response has been changed from "YES" to "NO". This modification helps prevent accidental updates. An example of the prompt is below:

“Link to update Remittance entry \# 14332 with receipt ERA14332? NO// “

### AR Patch PRCA \*4.5\*303

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Implement new 835 CARC Data Report option to the EDI Lockbox (ePayments) Reports Menu to display payers and the CARC codes returned on the 835 transactions.

2\. Implement new TPJI Screen Display redesign for ePayments. The new action option 'EP ERA/835" shall display only data associated with the 835 transaction.

3\. Implement new TPJI Action Option redesign for ePayments.

4\. Implement CARC/RARC Data Transfer from FSC.

5\. Implement Report Enhancements. The EDI Lockbox (ePayments) Reports Menu includes a new report entitled "Provider Level Adjustments (PLB) Report to display ERA data with PLB data details.

6\. Modification to the Scratchpad to process Efficiency Enhancements.

7\. Change EDI Lockbox to EDI Lockbox (ePayments).

### ### AR Patch PRCA\*4.5\*304

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Implement Auto-Auditing for Paper Bills
2.  Enhance Insurance Payment Trend Report
3.  Implement ability to Track Dollars through Suspense
4.  Implement National Reports for ePayments Data
5.  Implement Standardized Deposit Tickets
6.  Implement Receipt# Enhancements
7.  Implement Site Parameters for Pharmacy/Medical
8.  Implement Auto-Posting for Pharmacy/Medical
9.  Implement Auto-Decrease for Medical Claims
10. Fix errors and enhancements to APAR
11. Implement Auto-Post Checks for Pharmacy Claims
12. Enhance Exception Error message and filtering

### AR Patch PRCA\*4.5\*316

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Updates the VistA upload process of CARC/RARC data sent by FSC.

### AR Patch PRCA\*4.5\*317

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Adds the Unapplied EFT Deposits Report back on the EDI Lockbox (ePayments) Reports Menu.
2.  Updates the ERA Worklist option and the Auto-Post Awaiting Resolution option to ask users if they want to use their preferred view, when appropriate.

### AR Patch PRCA\*4.5\*318

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Updates the logic associated with auto-posting.
2.  Adds new report Auto-Posted Receipt Report on the EDI Lockbox (ePayments) Reports Menu.
3.  Updates the Auto-Decrease Adjustment report to include CARC details.
4.  Locks several actions within the ERA Worklist (including Scratchpad) and the Auto-Post Awaiting Resolution worklist (including Scratchpad) with one of two new security keys.
5.  Updates EFT Daily Activity Report to include CR and TR numbers and allows for up to 60 characters for the payer name.
6.  Removes security key lock from the EDI Diagnostic Measures Reports menu.
7.  With a security key, locks several options within the EDI Diagnostic Measures Extracts Menu.
8.  Updates the EFT Unmatched Aging Report and the Unapplied EFT Deposits report.
9.  Updates the logic associated with putting money to suspense.
10. Updates the auto-post site parameters logic.

### AR Patch PRCA\*4.5\*321 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The ‘Move ERA to Suspense’ option has been disabled and is no longer accessible from the EDI Lockbox menu
2.  The ‘Refresh Scratch Pad’ action has been removed from the APAR Scratchpad
3.  Receipt comments are now required when part of an account balance is split to suspense. A standardized set of comments have been added for the user to choose from along with a free form text comment field.
4.  If a receipt line comment has been added, the scratchpad screens in APAR and ERA Worklists will display the user name and a timestamp.
5.  The automatic update of EEOB information to reflect the split/edit of claims will occur at receipt creation in the PRCA nightly auto-post job (for APAR) or at receipt creation in the ERA Worklist.
6.  Updates to the Daily Activity Report including: a prompt to filter for EFTs with debits, a debit flag added to EFTs, removed matched payment amounts posted from totals, displays the station number instead of division and various page breaks for ease of use.
7.  Updates to Receipt Processing including: new help text when creating new receipts, ability to change the type of payment on receipts with preexisting lines and the ability to change the EFT number in certain cases.
8.  Eliminated an error when running the EFT Transaction Audit Report
9.  Update to the Link Payment Account action that now allows the user to move EEOBs to claims with payments linked from suspense
10. Updates to payer name selection and display: payer names longer than 30 characters can be selected, names containing ":", "," or "-" can be selected, names with 60 characters display correctly
11. Updated the Auto-Posted Receipt Report to ensure the correct dates displayed in the report fall within the range selected at the prompt
12. Enabled VistA to use the start date and ECME \# to identify the correct claim \# and populate the ERA
13. Exceptions for pharmacy claims now display correctly and in sequence
14. Updated the APAR worklist to allow greater flexibility to sort and display data
15. Updated receipt headers to show EFT/ERA numbers and totals
16. Claims in CSA status cannot be manually or auto-audited
17. The List of Receipts report now displays in list manager format
18. Manually matched ERAs with CHK payment types can be marked for auto-post
19. Medical, Pharmacy and Tricare Payers can now be indicated, along with access to view in a list and their types edited when appropriate.
20. EFT/ERA Trending Report added to EDI Lockbox reports menu
21. The Decrease Adjustment function now alerts users if there are pending payments and displays the payment that is pending.
22. Updated the ERA worklist to allow greater flexibility to sort and display data
23. The RCDPE AUDIT mail group now allows end users to self-enroll and a specific day of the week can be set for when the bulletins are sent
24. Number of days of unposted medical and pharmacy EFTs to prevent posting have been changed to 60 and 365 respectively

### AR Patch PRCA\*4.5\*326 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Adds notifications for changes to auto-post, auto-decrease, payer, and CARC site parameters
2.  Adds the ability to see who manually marked an ERA for auto-post in the Auto-Posted Receipt Report, Receipt Profile, List of Receipts Report, and Transaction Profile.
3.  Adds 'matched date’ to the ERA Worklist and Daily Activity Report.
4.  Adds a unique EFT identifier to the following reports: Daily Activity Report, EFT Unmatched Report, Unapplied EFT Report, EFT Audit Report, and Manual Match Report.
5.  Adds display of ‘Percent Collected on Claims’ to the ‘Claim Level Pay Status’ section of the EP Report (ERA/835 Action).
6.  Updates display language in the Link Payment Report
7.  Adds ability to filter by receipt number on Link Payment Report
8.  Allows user to generate Auto-Post Report by payer TIN
9.  Restricts unbalanced ERAs to be auto-post candidates
10. Renames the Payer Exclusion Report to the Payer Implementation Report
11. Modified the 'Distribute Adj Amts' action on the ERA Worklist to allow for negative distributions to claim lines which do not have a valid claim
12. Adds FMS Document Status to bill/claim profile screens and reports
13. Provides fix to Pharmacy Data Exception Filter on the 3rd Party Exceptions Worklist Scratch Pad
14. Provides fix to error in the ERA Worklist Manual Match Action
15. Adds an ERA Partial Post Indicator
16. Rewrites auto-posting logic to determine if the ERA is actually matched to an EFT
17. Changes prompt wording of Worklist Delete
18. Removes auto-decrease limit and adds new maximum parameter
19. Adds the ability to auto-decrease zero or no-pays
20. Adds the ability to view all ERA verify lines information on EEOBs
21. Adds the capability to filter all 3rd Party EDI Lockbox reports and options by Tricare/ChampVA
22. Adds Administrative Cost Adjustment option to allow adjustment to balance and for it to be recognized
23. Adds fee claims to Auto-Audit (5287.13) Rate type = Fee
24. Allows AM Clerk access to the Admin Cost Adjustment option
25. Fixes duplicate EFT deposits in the Audit Report

### AR Patch PRCA\*4.5\*332 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Adds report that shows all EFTs creating the EFT lock up
2.  Adds report for who marked EEOBs for auto-post
3.  Adds a List Manager report (worklist) showing all ERAs that were marked as duplicates
4.  Adds a historical report for all auto-activity and parameter changes
5.  Modifies the Active Bills with EEOB report
6.  Expands the user initials on the List of Receipts Report
7.  Modifies the data displayed on the ERA/EFT Trending Report
8.  Modifies ERA Worklist Manual Match Action
9.  Adds Number of days (age) of unposted Tricare EFTs to prevent posting
10. Adds ability to look up check, credit card, or trace numbers without identifying type of number
11. Corrects 835 message errors for claims not electronically billed
12. Adds the ability to auto-audit Tricare claims
13. Corrects attachment of correct EEOBs to payments that have been posted to suspense
14. Adds trace \# to the Receipt Profile
15. Creates sub-menus for the EDI Lockbox Reports
16. Allows users to view and print ERAs in List Manager
17. Removes security key RCDPEAR from the Administrative Cost Adjustment option

### AR Patch PRCA\*4.5\*345

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Removes Transfer Language reference from the EDI Lockbox 3rd Party Exceptions (EXC) data transmissions worklist
2.  Adds deposit number to the detail lines in the Auto-Post Report
3.  Adds new site parameter questions to allow pharmacy claims with payments to be auto-decreased by the Nightly AR Process, and modifies reports Auto-Parameter History Report, EDI Lockbox Parameters Report, EDI Lockbox Exclusion Report Audit Report and EDI Lockbox Parameters Audit Report
4.  Adds ability to auto-decrease first party claims when payments have been posted to the corresponding 3rd party claim by adding a new site parameter to the AR SITE PARAMETER File and creating new reports 1st Party Auto-Decrease Adjustment Report and First Party COPAY Manual vs Auto-Decrease Report
5.  Fixes an issue with TRICARE EFT lock-outs which was preventing medical EFT Lock-outs from being processed if TRICARE ERAs aged beyond the NUMBER OF DAYS (AGE) OF UNPOSTED TRICARE EFTS TO PREVENT POSTING site parameter setting.
6.  Keeps and displays the patient name received on the EEOB and displayed under ‘Free Text’. If a split/edit is processed on the claim payment, both the original patient name and the split/edit patient name will display in following screens: TPJI EP option, View/Print ERA and View/Print EEOB

### AR Patch PRCA\*4.5\*375

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Receipt transactions for a debit (negative) type EFT will be marked with

a new debit flag. These transactions will be subtracted from the

calculated receipt total, which may result in a negative receipt total. Debit vouchers will transmit negative dollars to FMS.

2.  When an EFT is removed from the system using the menu option

Remove Duplicate EFT Deposits, \[RCDPE REMOVE DUP DEPOSITS\], the

new field REMOVAL TYPE \[.2\] will be entered, after the removal reason

text. The user must enter one of two codes from the set:

D DUPLICATE EFT

M MILLENIUM EFT

The new field will show on the Duplicate EFT Deposits Audit report

\[RCDPE EFT AUDIT REPORT\].

## New Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table of terms contains vocabulary that are be referenced throughout this document to describe the ePayments process.

| CARC         | Claim Adjustment Reason Code                                                                                                                                       |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EFT          | Electronic Funds Transfer; the electronic form of what is currently sent as a paper check                                                                          |
| ERA          | Electronic Remittance Advice; the equivalent to a stack of paper Explanation of Benefits (EOB) statements for many patients from one payer                         |
| EEOB         | Electronic Explanation of Benefits; one line item within an ERA                                                                                                    |
| RARC         | Remittance Advice Remark Code                                                                                                                                      |
| Trace Number | A number assigned by the insurance company to identify which EFT payment is associated with what ERA; used to re-associate electronic remittance payment with data |

## Process Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following figure depicts a high level description of the ePayments process.

![Figure 1 - ePayments High Level Process Flow](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/002.png)

*Figure 1 - ePayments High Level Process Flow*

The data flow process functions as follows:

Electronic claims are sent to the payer and the Clearinghouse sends a message to VistA Integrated Billing (IB), indicating that the claim passed all Clearinghouse validity edits and was forwarded to the payer. The message initiates the auto-audit functionality that automatically audits the claim and sets it up as a receivable in VistA.

The payer adjudicates the claim and determines payment. The payment may be sent electronically to PNC Bank as an EFT or the payer may mail a paper check.

PNC Bank sends:

EFT dollars directly to the U.S. Treasury,

EFT 835 transactions, containing daily total deposit information by payer to the FSC, and

ERA 835 transactions, containing electronic EOBs (EEOBs) to the FSC.

The FSC passes EFT and ERA information on to each VAMC in flat file format via VistA Mailman messages. These messages are sent to the MLB mail group.

Additionally, the FSC transmits the EFT and ERA flat file information to the EPHRA database

The FSC also transmits unrouteable EEOB data to EPHRA. Unrouteable EEOB data does not contain the appropriate Tax ID information to allow the FSC to route it to the proper VistA AR system. FSC 224-Unit staff monitors EPHRA for unrouteable EEOB data and use other data identifiers, such as the bill number, to determine appropriate routing and transmit to the correct VistA AR system.

1.  EFT data received by VistA initiates an automatic Credit Receipt (CR) document for each payment received within the deposit and puts the payment information into a separate appropriation fund that tracks payments not yet posted as part of the A/R nightly processing job. The Revenue Source Code (RSC) 8NZZ was created specifically for 3<sup>rd</sup> Party EFTs. (See Error! Reference source not found.)

![Figure 2 - ePayments Nightly Process](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/003.png)

*Figure 2 - ePayments Nightly Process*

2.  VistA runs a nightly process (see Figure 2 - ePayments Nightly Process) that matches ERAs to EFT files using the Trace Number and Insurance Company ID.
    1.  If the system finds a match, it then verifies the amount matches. If the amount matches, the ERA and EFT detail records are automatically marked as “matched.”
    2.  If the amount does not match, the ERA record and the EFT detail record are marked as “matched with errors.”
    3.  If the system is not able to match an ERA with an EFT detail record, it is marked as “unmatched.” It is most likely that this scenario will call for a match to a paper check or is a zero-payment.
3.  When the ERA is received in VistA, it attempts to associate EEOBs with bills in the AR package and stores the details associated with the payer’s adjudication decisions in Integrated Billing’s EEOB file. This EEOB data is available for display under the BILL CHARGES action in THIRD PARTY JOINT INQUIRY.
    1.  If any EEOBs cannot be associated with bills in VistA, a message will be sent to the RCDPE PAYMENTS EXCEPTIONS mail group. This message indicates that there is a problem with the bill number such as belongs to another site or the numbers were transposed.
    2.  If NONE of the EEOBs included in the ERA can be associated with a bill in VistA, a message will be sent to the RCDPE PAYMENT EXCEPTIONS mail group indicating there were no valid bills on the ERA for the site. This ERA is then rejected and is not stored at the site. Contact your ePayments POC for assistance if needed.
4.  Members of the RCDPE Payments mail group receive the nightly processing bulletins.
5.  Members of the RCDPE Payment Exceptions mail group will receive all bulletins for exception conditions or processing issues generated by the EDI Lockbox (ePayments) message processor. Generally, an ePayments exception occurs when an EDI Lockbox (ePayments) message cannot be automatically or completely filed into the VistA AR and IB systems. When this occurs, an exception record is created in Exception Processing. In order to address the transmission issues, you will access the Exception Processing function.
6.  A nightly auto-posting job evaluates the unposted ERAs to determine if an ERA is an auto-post candidate. If the ERA is not an auto-post candidate, the ERA must be worked by a user from the ERA Worklist Scratch Pad. If the ERA is an auto-post candidate, the system will process the receipt if all criteria are met. If the system is unable to create a receipt for an individual EEOB, the EEOBs must be worked by a user from the Auto-Posting Awaiting Resolution (APAR) list.
7.  The user reviews all unposted ERAs and creates the ERA Worklist Scratch Pad entries to make the necessary adjustments to balance the total of the EEOB with the total on the check or EFT. In order to use the worklist, ERAs with an unmatched status require matching to a paper check or marked as a zero pay.
8.  Once the adjustments are made in the Worklist, the Receipt can be created automatically through a Worklist function. The receipt and any total balancing adjustments can be created manually.
9.  The receipt can then be processed as normal through PR Process Receipt option.
10. For EFTs related to ERAs:  
    After the receipt is processed and closed in VistA, the FMS transactions will be initiated. This means that a transfer (TR) document is generated to FMS to transfer the monies from the new MCCF RSC 528704/8NZZ to the appropriate MCCF collection accounts under 5287. This TR document will also transfer any monies needing to be posted to the station suspense account or other accounts, due to non-MCCF billing/payments.
11. For ERAs related to paper checks:  
    A CR document is generated to process the monies into FMS. This is the same processing as for current non-EDI receipts.
12. If the ERA receipt is not created using the Worklist, then the ERA reference must be manually entered using the EDIT RECEIPT action in Receipt Profile. If the ERA is also associated with an EFT, the EFT reference must also be manually added using this action. This is extremely important because the receipt associated with an EFT will generate the appropriate TR documents to move the money out of 8NZZ and into the proper Fund/RSC whereas a receipt without an EFT referenced will generate a CR document and will expect the dollars on the receipt to be deposited by your site.

# Getting Started with ePayments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menus and Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ERA List – Worklist screen 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new list manager screen, the ERA List – Worklist screen has been added in order to display the selection of ERAs to be worked.

There are features that give the capability to search a greater range of records, with dialogue issued at intermittent periods during the ERA Worklist record search to indicate that the system is still gathering records for the ERA Worklist. To exit the ERA Worklist option the user enters the cancel search character (“^”).

The user-defined sort selections are displayed in the header information on this screen. The following information is available in the body of the ERA List – Worklist screen:

1.  Sequence \#
2.  ERA \#
3.  Trace \#
4.  Payer Name
5.  Match Status & Date
6.  ERA Paid Date
7.  Total Amount Paid
8.  Date Received

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ERA List - Worklist Dec 09, 2011@15:20:15 Page: 1 of 136</p>
<p>DATE RANGE : NONE SELECTED MEDICAL/PHARM/TRIC: ALL</p>
<p>MATCH STATUS: NOT MATCHED AUTOP: ALL AUTO-POSTING: BOTH</p>
<p>POST STATUS : UNPOSTED PAYERS: ALL PAYERS PAYMENT TYPE: BOTH</p>
<p># ERA # TRACE#</p>
<p><u>PAYER NAME/MATCH STATUS &amp; DATE ERA PAID DT TOT AMT PAID DT REC'D</u></p>
<p>1 -112137 00698105</p>
<p>11/9/11 277.10 11/9/11</p>
<p>WOODMEN OF THE WORLD ASSURED L APPROX # EEOBs: 3</p>
<p>UNMATCHED (CHECK PAYMENT EXPECTED)</p>
<p>2 -112200 377746</p>
<p>11/10/11 155.95 11/10/11</p>
<p>MERITAIN HEALTH APPROX # EEOBs: 1</p>
<p>UNMATCHED (CHECK PAYMENT EXPECTED)</p>
<p>3 -112201 385045</p>
<p>11/10/11 270.62 11/10/11</p>
<p>MERITAIN HEALTH APPROX # EEOBs: 1</p>
<p>UNMATCHED (CHECK PAYMENT EXPECTED)</p>
<p>+ |'-' No scratchpad|'x' EXC |'A' autopost complete</p>
<p>Select ERA View/Print ERA Admin Cost Adj</p>
<p>Sort List Change View Exit</p>
<p>Mark for Auto Post ERA Manual Match</p>
<p>Select Action: Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The list manager ERA Worklist main page allows the user to perform the following actions:

1.  Select ERA
2.  Sort List
3.  Mark for Auto Post (requires the RCDPEPP security key)
4.  View/Print ERA
5.  Change View
6.  ERA Manual Match
7.  EXIT

## ERA Worklist/Scratchpad screen 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>ERA List - Worklist Dec 09, 2011@15:20:15 Page: 1 of 136</u>
- SELECTED: MATCH STATUS: BOTH POST STATUS: UNPOSTED
- DATE RANGE : 1/1/11-12/9/11
- ALL PAYERS
- \# ERA \# TRACE#
- <u>PAYER NAME/MATCH STATUS ERA PAID DT TOT AMT PAID DT REC'D</u>
- 1 -112137 00698105
- 11/9/11 277.10 11/9/11
- WOODMEN OF THE WORLD ASSURED L APPROX \# EEOBs: 3
- UNMATCHED (CHECK PAYMENT EXPECTED)
- 
- 2 -112200 377746
- 11/10/11 155.95 11/10/11
- MERITAIN HEALTH APPROX \# EEOBs: 1
- UNMATCHED (CHECK PAYMENT EXPECTED)
- 
- 3 -112201 385045
- 11/10/11 270.62 11/10/11
- MERITAIN HEALTH APPROX \# EEOBs: 1
- UNMATCHED (CHECK PAYMENT EXPECTED)
- \+ '-' Before the ERA \# indicates no scratchpad entry
- Select ERA View/Print ERA Exit
- Sort List Hide/Display Batch

  The ERA Worklist/Scratchpad is a new option that has been created for the ePayments system. It allows the user to select an ERA and view the detailed EEOB records associated with the ERA.

  The following information is available from the ERA Worklist/Scratchpad:

For the entire ERA:

1.  ERA Entry \#
2.  Payer Name/ID
3.  Total Amt Paid
4.  Paper Check \# or EFT Trace \#
5.  Total amount to be posted to the receipt

<u>ERA Worklist/Scratch Pad Jul 21, 2010@12:17:58 Page: 1 of 1</u>

ERA Entry \#: 9876543210 Total Amt Pd: 123.45 Current View:

Payer Name/ID: IBinsurance Company One/55555555 NO SORT ORDER

PAPER CHECK \#: 1003 ALL EEOBs

<u>.</u>

1 EEOB Seq \# On ERA: 1 Net Payment Amt: 123.45

1.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One A/5555

Claim Bal: 0.00 Billed Amt: 0.00 Amt To Post: 123.45

Svc Dt: 6/1/00 COB: NO Rx Copay: UNKNOWN Means Tst: ??

Payment Amt: 123.45 Total Adjustments: 0.00 Net: 123.45

..............................................................................

Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

Distribute Adj Amts Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen//

For the EEOB detail:

1.  Bill number
2.  Patient Priority Status (CAT C)
3.  Rx Copay exempt status
4.  Date of service
5.  Billed amount
6.  Claim balance (current balance)
7.  Patient last name
8.  Last 4 digits of the patient’s SSN
9.  Paid amount (amt to post)
10. COB status
11. Line item number from the ERA
12. ERA level and Claim level Adjustment totals
13. Comment Date and Time (stamp)
14. (Comment) User Name

ERA Worklist/Scratch Pad Jul 21, 2010@12:17:58 Page: 1 of 1

ERA Entry \#: 9876543210 Total Amt Pd: 123.45 Current View:

Payer Name/ID: IBinsurance Company One/55555555 NO SORT ORDER

PAPER CHECK \#: 1003 ALL EEOBs

... 1 EEOB Seq \# On ERA: 1 Net Payment Amt: 123.45

1.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One A/5555

Claim Bal: 0.00 Billed Amt: 0.00 Amt To Post: 123.45

Svc Dt: 6/1/00 COB: NO Rx Copay: UNKNOWN Means Tst: ??

Payment Amt: 123.45 Total Adjustments: 0.00 Net: 123.45 ...........................................................................

Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

Distribute Adj Amts Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen//

The list manager ERA Worklist Scratchpad allows the user to perform the following actions:

1.  Split/Edit A Line
2.  Distribute Adj Amts
3.  Refresh Scratch Pad (requires the RCDPEPP security key)
4.  Research Menu
5.  Look At Receipt (requires the RCDPEPP security key)
6.  Review Line
7.  Verify (requires the RCDPEPP security key)
8.  Change View
9.  Mark for Auto Post (requires the RCDPEPP security key)
10. View/Print an ERA
11. Receipt Processing (requires the RCDPEPP security key)
12. Exit

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ERA Worklist/Scratch Pad Jul 21, 2010@12:17:58 Page: 1 of 1</p>
<p>ERA Entry #: 9876543210 Total Amt Pd: 123.45 Current View:</p>
<p>Payer Name/ID: IBinsurance Company One/55555555 NO SORT ORDER</p>
<p>PAPER CHECK #: 1003 ALL EEOBs</p>
<p>1 EEOB Seq # On ERA: 1 Net Payment Amt: 123.45</p>
<p>1.001 Claim #: KXXXXXX Patient/Last 4: IBpatient,One A/5555</p>
<p>Claim Bal: 0.00 Billed Amt: 0.00 Amt To Post: 123.45</p>
<p>Svc Dt: 6/1/00 COB: NO Rx Copay: UNKNOWN Means Tst: ??</p>
<p>Payment Amt: 123.45 Total Adjustments: 0.00 Net: 123.45</p>
<p>..............................................................................</p>
<p>Enter ?? for more actions</p>
<p>Split/Edit A Line Look At Receipt Mark for Auto Post</p>
<p>Distribute Adj Amts Review Line ERA View/Print ERA</p>
<p>Refresh Scratch Pad Verify RP Receipt Processing</p>
<p>Research Menu Change View EXIT</p>
<p>Select Action: Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The expanded Look At Receipt action (previously named PREVIEW RECEIPT) will yield the Preview/Create Receipt screens, and allows the following actions to be performed. This action requires the RCDPEPP security key:

> 1\. Select option LOOK AT RECEIPT

> 2\. CREATE RECEIPT (which will allow a link to the RECEIPT PROCESSING function if the receipt is created without errors)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ERA WORKLIST PREVIEW RECEIPT Jul 21, 2010@08:43:02 Page: 1 of 1</p>
<p>ERA Entry #: 9876543210 Total Amt Pd: 20.59</p>
<p>Payer Name/ID: IBinsurance Company One/55555555</p>
<p>PAPER CHECK #: 1003</p>
<p>LINE # ACCOUNT AMOUNT .</p>
<p>PAYMENTS (LINES FOR RECEIPT):</p>
<p>1.001 XXX-KXXXXXX 20.59</p>
<p>Enter ?? for more actions</p>
<p>Print Receipt Preview Create Receipt Exit</p>
<p>Select Action: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The new Verify option provides functionality needed to identify and mark unverified EEOBs. This action requires the RCDPEPP security key:

1\. MANUAL MARK AS VERIFIED

2\. REPORT OF UNVERIFIED WITH DISCREPANCIES

VERIFY EEOBs:

1 MANUAL MARK AS VERIFIED

2 REPORT OF UNVERIFIED WITH DISCREPANCIES

3 QUIT AND RETURN TO WORKLIST

Select Action: QUIT//

The Research Menu is accessible through the list manager ERA Worklist screen and it allows the following actions to be performed:

1.  Full Acct Prof
2.  Admin Cost Adj (requires the RCDPEAR security key)
3.  TPJI (Third Party Joint Inquiry)
4.  Bill Comment Log
5.  Re establish Bill (requires the RCDPEAR security key)
6.  View/Print EEOB
7.  Review Line
8.  Scratchpad Menu/Exit

ERA Worklist Research Aug 10, 2004@11:01:33 Page: 1 of 2

ERA Entry \#: 5 Total Amt Pd: 509.61 Current View:

Payer Name/ID: IBinsurance Company One/5555555555 NO SORT ORDER

PAPER CHECK \#: 55555-55555555 ALL EEOBs

.

1 (V) EEOB Seq \# On ERA: 1 Net Payment Amt: 0.00

1.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One A/5555

Claim Bal: 0.00 Billed Amt: 19.47 Amt to Post: 0.00

Svc Dt: 1/27/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: ??

Payment Amt: 0.00 Total Adjustments: 0.00 Net: 0.00

....................................................................................

2 (V) EEOB Seq \# On ERA: 3 Net Payment Amt: 509.61

2.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,Two A/4444

Claim Bal: 509.61 Billed Amt: 559.61 Amt To Post: 509.61

Svc Dt: 2/4/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: NO

Payment Amt: 590.61 Total Adjustments: 0.00 Net: 509.61

....................................................................................

\+ Enter ?? for more actions

Full Acct Prof Bill Comment Log Review Line

Admin Cost Adj Re establish Bill Scratch Pad Menu/Exit

TPJI View/Print EEOB

Select Action: Next Screen/

Receipt Processing option allows you to jump to “RP Receipt Processing” with a pre-populated Receipt number and return to the Scratchpad. This action requires the RCDPEPP security key.

ERA Worklist/Scratch Pad Sep 17, 2015@15:30:24 Page: 1 of 2

ERA Entry \#: 43530 Total Amt Pd: 8501.13 Current View:

Payer Name/ID: AETNA/10660X33492 NO SORT ORDER

EFT \#/TRACE \#: 1135/ABC637X6748X787 ALL EEOBS

\*\*\* RECEIPT(S) ALREADY CREATED \*\*\* (E15080304A-E15080304B)

Auto-Post Status: Complete Auto-Post Date: Aug 03, 2015

1 EEOB Seq \# On ERA: 1 Net Payment Amt: 7000.58

1.001 Claim \#: K502VMQ Patient/Last 4: XX-XXXXXX,XXXX/2215

Claim Bal: 0.00 Billed Amt: 7000.58 Amt To Post: 7000.58

Svc Dt: 12/9/14 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 7000.58 Total Adjustments: 0.00 Net: 7000.58

Receipt: E15080304B

..............................................................................

2 (V)EEOB Seq \# On ERA: 2 Net Payment Amt: 1500.55

2.001 Claim \#: K502VQR Patient/Last 4: XX-XXXXXX,XXXX /2215

Claim Bal: 0.00 Billed Amt: 1500.55 Amt To Post: 1500.55

Svc Dt: 1/21/15 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

\+ Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

Distribute Adj Amts Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen// rp Receipt Processing

Select one of the following:

1 E15080304A

2 E15080304B

Select Receipt: 1

## ERA/835 Screens for ePayments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERA/835 screens are accessible from the main TPJI screen, by choosing the action option “EP ERA/835”. The ERA/835 screen will display ERA level summary data based on the claim# selected and displayed on the previous Main TPJI Screen, EOB/Claim level data and Claim level adjustments; and EEOB/Claim Line level data and adjustments.

> **NOTE:** For pharmacy claims, the ECME#, Date of Service, Rx/Fill/Release Status shall be displayed. For medical claims, these data elements will be blank.

The following ePayments actions can be performed from the ERA/835 Screen:

RX ECME Information CI Go to Claim Screen VP Policy Benefits

AR Account Profile BC Bill Charges EL Patient Eligibility

CM Comment History IR Insurance Reviews RP Receipt Profile

PE Print EEOB AD Additional 835 Data EX Exit

### Action Option: RX ECME Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view ECME Claim Information. You can select “EX Exit” to return to the TPJI Main screen or you can select the action option “VER View ePharmacy Rx” to view detailed prescription data.

### Action Option: AR Account Profile 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view payment transaction details including the ERA#, TRACE#, Payer ID and Receipt# that was used for posting the payment.

### Action Option: CM Comment History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view Accounts Receivables comments for the claims account.

### Action Option: PE Print EEOB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to print EEOBs. You may select either a single EEOB or all EEOBs for a claim.

When the user successfully selects an EEOB(s) for printing, the system prints the EOB/Claim level data and Claim level adjustments and EOB/Claim Line level data and Claim Line level adjustments for each EEOB selected for printing then returns the user to the ERA/835 screen.

### Action Option: CI Go to Claim Screen 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to return to the Claim Information screen.

### Action Option: BC Bill Charges 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view a bill’s charge information as it would print on the bill.

### Action Option: IR Insurance Reviews 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view all insurance reviews for the episodes of care on a bill.

### Action Option: AD Additional 835 Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view additional information found in the 835 at the EOB level. if sent by the payer. The additional 835 data is not mandated by HIPAA so additional information is sent at a payer’s discretion.

1.  Claim Code/Status

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

2.  Corrected Priority Payer Type

> AD = Blue Cross Blue Shield Association Plan Code

> FI = Federal Taxpayer’s Identification Number

> NI = National Association of Insurance Commissioners (NAIC) Identification

> PI = Payer Identification

> PP = Pharmacy Processor Number

> XV = Centers for Medicare and Medicaid Services PlanID

### Action Option: VP Policy Benefits 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view patient insurance policy data.

### Action Option: EL Patient Eligibility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view current information on the patient’s eligibility for care and service connection status.

### Action Option: RP Receipt Profile 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to view a bill and any of its associated transactions.

### Action Option: EX Exit 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to return to the <u>TPJI Main Screen</u>.

*All of the menus are described in detail in Section* 3 *Payments Processing.*

## Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menu option to edit parameters requires the user to hold security key RCDPE AUTO DEC. The following parameters are part of the ePayments software:

Aging Payments  
This parameter allows the user to select the specified number of days that will elapse before an unmatched payment (for an EFT detail line) will be reported. This parameter will be used when the report is run as part of the nightly processing. At installation, the Report Aging Payments site parameter will default to five days.

Aging ERA

This parameter allows the user to select the specified number of days that will elapse before an unmatched ERA will be reported. This parameter will be used when the job is run as part of the nightly processing. At installation, the Report Aging ERA site parameter will default to seven days.

Medical Claims Auto-Posting

This parameter allows the user to enable or disable auto-posting of third party medical claims. At installation, the medical claims auto-posting site parameter will default to yes, which enables auto-posting.

Medical Claims Auto-Posting Exclusion

This parameter allows the user to exclude specific payers from auto-posting of third party medical claims by selecting the payer name or payer ID. At the time of installation, no payers are excluded from auto-posting. This parameter will only display if auto-posting of third party medical claims is enabled.

The Payer prompt acts as a toggle. If a payer is selected, the payer will be added to the exclusion list if the payer is not already there or removed from the exclusion list if the payer is already there. A comment is required.

Medical Claims with Payments Auto-Decrease

This parameter allows the user to enable or disable auto-decrease of third party medical claims with payments. At installation, the medical claims auto-posting site parameter will default to no, which disables auto-decrease. This parameter will only display if auto-posting of third party medical claims is enabled.

Medical Claims with No Payments Auto-Decrease

This parameter allows the user to enable or disable auto-decrease of third party medical claims with no payments. At installation, the medical claims auto-posting site parameter will default to no, which disables auto-decrease. This parameter will only display if auto-posting of third party medical claims is enabled.

Medical Claims Auto-Decrease Amount

This parameter allows the user to specify the maximum claim dollar amount of an automatic decrease adjustment that is made for a third party medical claim. At installation, the amount is not populated and the value is required to enable auto-decrease of third party medical claims. This parameter will only display if auto-decrease of third party medical claims is enabled.

Medical Claims Auto-Decrease by CARC

This parameter allows the user to specify an individual CARC code to include in the auto-decreasing of third party medical claims. The user must select the actual CARC by code to include auto-decreasing medical claims. Once validated and selected, the user must enter a maximum dollar amount that can be auto-decreased for the entered CARC. The maximum claim dollar amount displays with an initial default value of null and a required response from 1 to 99999 dollars with the default amount being set to 5000. The dollar amount is represented without cents. This parameter will only display if auto-decrease of third party medical claims is enabled.

Medical Claims Auto-Decrease by CARC Amount

This parameter allows the user to specify the maximum claim dollar amount of an automatic decrease adjustment by CARC code that is made for a third party medical claim. At installation, the amount is not populated and a value between 1 to 1500 dollars is required to enable auto-decrease of third party medical claims by CARC. This parameter will only display if auto-decrease of third party medical claims is enabled.

Medical Claims Auto-Decrease Timeframe

This parameter allows the user to specify the number of days to wait before an automatic decrease adjustment is made for a third party medical claim. The number of days is the time to wait after auto-posting completes. At installation, the timeframe is not populated and the value is required to enable auto-decrease of third party medical claims. This parameter will only display if auto-decrease of third party medical claims is enabled.

Medical Claims Auto-Decrease Exclusion

This parameter allows the user to exclude specific payers from auto-decrease of third party medical claims by selecting the payer name or payer ID. At the time of installation, no payers are excluded from auto-decrease. This parameter will only display if auto-decrease of third party medical claims is enabled.

The Payer prompt acts as a toggle. If a payer is selected, the payer will be added to the exclusion list if the payer is not already there or removed from the exclusion list if the payer is already there. A comment is required.

Pharmacy Claims Auto-Posting

This parameter allows the user to enable or disable auto-posting of third-party pharmacy claims. At installation, the pharmacy claims auto-posting site parameter will default to NO

Pharmacy Claims Auto-Posting Exclusion

This parameter allows the user to exclude specific payers from auto-posting of third-party pharmacy claims by selecting the payer name or payer ID. At the time of installation, no payers are excluded from auto-posting. This parameter will only display if auto-posting of third-party pharmacy claims is enabled.

The Payer prompt acts as a toggle. If a payer is selected, the payer will be added to the exclusion list if the payer is not already there or removed from the exclusion list if the payer is already there. A comment is required.

Pharmacy Claims Auto-Decrease

This parameter allows the user to enable or disable auto-decrease of third-party pharmacy claims. At installation, the pharmacy claims auto-decrease site parameter will default to no, which disables auto-decrease. This parameter will only display if auto-posting of third-party pharmacy claims is enabled.

Pharmacy Claims Auto-Decrease Amount

This parameter allows the user to specify the maximum claim dollar amount of an automatic decrease adjustment that is made for a third-party pharmacy claim. At installation, the amount is not populated and the value is required to enable auto-decrease of third-party pharmacy claims. This parameter will only display if auto-decrease of third-party pharmacy claims is enabled.

Pharmacy Claims Auto-Decrease by CARC

This parameter allows the user to specify an individual CARC code to include in the auto-decreasing of third-party pharmacy claims. The user must select the actual CARC by code to include auto-decreasing pharmacy claims. Once validated and selected, the user must enter a maximum dollar amount that can be auto-decreased for the entered CARC. The maximum claim dollar amount displays with an initial default value of null and a required response from 1 to 99999 dollars with the default amount being set to 5000. The dollar amount is represented without cents. This parameter will only display if auto-decrease of third-party pharmacy claims is enabled.

Pharmacy Claims Auto-Decrease by CARC Amount

This parameter allows the user to specify the maximum claim dollar amount of an automatic decrease adjustment by CARC code that is made for a third-party pharmacy claim. At installation, the amount is not populated and a value between 1 to 1500 dollars is required to enable auto-decrease of third-party pharmacy claims by CARC. This parameter will only display if auto-decrease of third-party pharmacy claims is enabled.

Pharmacy Claims Auto-Decrease Timeframe

This parameter allows the user to specify the number of days to wait before an automatic decrease adjustment is made for a third-party pharmacy claim. after auto posting of a pharmacy payment. At installation, the timeframe is not populated and the value is required to enable auto-decrease of third-party pharmacy claims. This parameter will only display if auto-decrease of third-party pharmacy claims is enabled.

Pharmacy Claims Auto-Decrease Exclusion

This parameter allows the user to exclude specific payers from auto-decrease of third-party pharmacy claims by selecting the payer name or payer ID. At the time of installation, no payers are excluded from auto-decrease. This parameter will only display if auto-decrease of third-party pharmacy claims is enabled. The Payer prompt acts as a toggle. If a payer is selected, the payer will be added to the exclusion list if the payer is not already there or removed from the exclusion list if the payer is already there. A comment is required.

Pharmacy Claims with Payments Auto-Decrease

This parameter allows the user to enable or disable auto-decrease of third-party pharmacy claims with payments. At installation, the third-party pharmacy claims auto-posting site parameter will default to no, which disables auto-decrease. This parameter will only display if auto-posting of third-party pharmacy claims with payments is enabled.

Medical Claims Posting Prevention

This parameter allows the user to set the number of calendar days beyond which unposted medical payments (EFTs) will trigger an error message that prevents the user from posting newer medical EFTs. This parameter is used in the ERA Worklist when a user selects an ERA. At the time of installation, the value will be set to 5 days if the current value is over the new parameter max of 7 days, otherwise it will remain the same. The value cannot be deleted and valid entries are in the range of 0 days to 7 days.

Pharmacy Claims Posting Prevention

This parameter allows the user to set the number of calendar days beyond which unposted pharmacy payments (EFTs) will trigger an error message that prevents the user from posting newer pharmacy EFTs. This parameter is used in the ERA Worklist when a user selects an ERA. At the time of installation, the value will be set to 365 days if the current value is over the new parameter max of 99 days, otherwise it will remain the same. The value cannot be deleted and valid entries are in the range of 21 days to 99 days.

Tricare Claims Posting Prevention

This parameter allows the user to set the number of calendar days beyond which unposted Tricare payments (EFTs) will trigger an error message that prevents the user from posting newer Tricare EFTs. This parameter is used in the ERA Worklist when a user selects an ERA. At the time of installation, the value will be set to 30 days if the current value is over the new parameter max of 60 days, otherwise it will remain the same. The value cannot be deleted and valid entries are in the range of 14 days to 60 days.

Auto Audit for Medical, Pharmacy, and Tricare Bills

Three parameters exist to allow the user to enable or disable automatic auditing of paper and/or electronic medical, pharmacy, or Tricare bills. At installation, the auto audit site parameter will default to no, which disables auto auditing for Medical, Pharmacy, and Tricare claims.

Add Suspense

The parameter allows the user to limit the number of days an entry can remain in Suspense. The parameter default is initially set at 45 days. The user can to edit the parameter within the range of 1-120 days.

## Parameters Report – EDI Lockbox (ePayments) Parameters Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Lockbox Parameters Report provides a listing of all parameters with current settings. The report can be run on-demand on an as-needed basis to view or print parameter settings.

#### When to run this report

Review the EDI Lockbox (ePayments) Parameters Report on an as-needed basis to view or print changes to settings. The report can be run on-demand.

#### How to run this report

To run the EDI Lockbox (ePayments) Parameters Report, select EDI Lockbox Parameters Report and then choose Medical, Pharmacy or Both.

The EDI Lockbox (ePayments) Parameters Report follows:

EDI Lockbox Parameters Report

(M)EDICAL, (P)HARMACY, OR (B)OTH: BOTH//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EDI Lockbox Parameters Report - ALL Page: 1

Run Date: Nov 20, 2018@11:29:09 Site: CHEYENNE VAMC

------------------------------------------------------------------------------

NUMBER OF DAYS EFT UNMATCHED: 5

NUMBER OF DAYS ERA UNMATCHED: 7

\#DAYS ENTRY CAN REMAIN IN SUSP: 45

ENABLE AUTO-AUDIT MEDICAL PAPER BILLS: No

ENABLE AUTO-AUDIT RX PAPER BILLS: No

ENABLE AUTO-AUDIT MEDICAL EDI BILLS: No

ENABLE AUTO-AUDIT RX EDI BILLS: No

DAY FOR WORKLOAD NOTIFICATIONS: SATURDAY

ENABLE AUTO-POSTING OF MEDICAL CLAIMS: Yes

Excluded Payer Comment

AETNA test

ANHEUSER-BUSCH a comment

BCBS CO & NV HMO TEST

FOREIGN SERVICE BENEFIT PLAN TESTING

MAIL HANDLERS BENEFIT PLAN testing

TRICARE TDEFIC TESTING

Press enter to continue, '^' to exit:

EDI Lockbox Parameters Report - ALL Page: 2

Run Date: Nov 20, 2018@11:29:09 Site: CHEYENNE VAMC

------------------------------------------------------------------------------

ENABLE AUTO-DECREASE OF MEDICAL CLAIMS WITH PAYMENTS: Yes

MAXIMUM DOLLAR AMOUNT TO AUTO-DECREASE PER MEDICAL CLAIM: \$7000

AUTO-DECREASE MEDICAL CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

----------------------------------------------------------------------

2 Coinsurance Amount 1

42 Charges exceed our fee schedule or maximum allowab .. 1 (I)

4 The procedure code is inconsistent with the modifi .. 1

5 The procedure code/bill type is inconsistent with .. 1

3 Co-payment Amount 10

43 Gramm-Rudman reduction. 100 (I)

10 The diagnosis is inconsistent with the patient"s g .. 250

NUMBER OF DAYS TO WAIT BEFORE MEDICAL AUTO-DECREASE: 5

ENABLE AUTO-DECREASE OF NO-PAY MEDICAL CLAIMS: Yes

Press enter to continue, '^' to exit:

EDI Lockbox Parameters Report - ALL Page: 3

Run Date: Nov 20, 2018@11:29:09 Site: CHEYENNE VAMC

------------------------------------------------------------------------------

AUTO-DECREASE NO-PAY MEDICAL CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

----------------------------------------------------------------------

45 Charge exceeds fee schedule/maximum allowable or c .. 7000

1 Deductible Amount 1

2 Coinsurance Amount 1

42 Charges exceed our fee schedule or maximum allowab .. 1 (I)

4 The procedure code is inconsistent with the modifi .. 1

3 Co-payment Amount 15

43 Gramm-Rudman reduction. 100 (I)

NUMBER OF DAYS TO WAIT BEFORE MEDICAL NO PAY AUTO-DECREASE: 1

All payers excluded from Auto-Posting are excluded from Auto-Decrease.

Additional Excluded Payer Comment

AETNA -CONTINENTAL LIFE INSURANCE C testing

ANHEUSER-BUSCH a commetn

UNITED HEALTH CARE testing

Press enter to continue, '^' to exit:

EDI Lockbox Parameters Report - ALL Page: 4

Run Date: Nov 20, 2018@11:29:09 Site: CHEYENNE VAMC

------------------------------------------------------------------------------

ENABLE AUTO-DECREASE OF PHARMACY CLAIMS WITH PAYMENTS: Yes

MAXIMUM DOLLAR AMOUNT TO AUTO-DECREASE PER PHARMACY CLAIM: \$7000

AUTO-DECREASE PHARMACY CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:

CARC Description Max. Amt

----------------------------------------------------------------------

2 Coinsurance Amount 1

42 Charges exceed our fee schedule or maximum allowab .. 1 (I)

4 The procedure code is inconsistent with the modifi .. 1

5 The procedure code/bill type is inconsistent with .. 1

3 Co-payment Amount 10

43 Gramm-Rudman reduction. 100 (I)

10 The diagnosis is inconsistent with the patient"s g .. 250

NUMBER OF DAYS TO WAIT BEFORE PHARMACY AUTO-DECREASE: 5

Press enter to continue, '^' to exit:

ENABLE AUTO-POSTING OF PHARMACY CLAIMS: No

NUMBER OF DAYS (AGE) OF UNPOSTED MEDICAL EFTS TO PREVENT POSTING: 30

NUMBER OF DAYS (AGE) OF UNPOSTED PHARMACY EFTS TO PREVENT POSTING: 99

NUMBER OF DAYS (AGE) OF UNPOSTED MEDICAL TRICARE TO PREVENT POSTING: 14

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## Parameters Report – EDI Lockbox (ePayments) Parameters Audit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Lockbox (ePayments) Parameters Audit Report provides an audit of changes to parameter questions. The information on the report contains the date and time a parameter was edited, the old value, the new value and the user who completed the edit.

#### When to run this report

Review the EDI Lockbox (ePayments) Parameters Audit Report on an as-needed basis to view or print changes to settings. The report can be run on-demand.

#### How to run this report

To run the EDI Lockbox (ePayments) Parameters Audit Report, enter a start date and end date and select a division. The resulting report will contain parameters that have been changed within the date range. The report can also be exported to Excel.

The EDI Lockbox (ePayments) Parameters Audit Report follows:

EDI Lockbox Parameters Audit Report

(M)EDICAL, (P)HARMACY, OR (B)OTH: BOTH//

Report start date: t-10 (NOV 10, 2018)

Report end date: Nov 20, 2018// t (NOV 20, 2018)

Export the report to Microsoft Excel? (Y/N): NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EDI Lockbox Parameter Audit Report Page: 1

RUN DATE: 11/20/2018@11:19:48

DATE RANGE: 11/10/2018 - 11/20/2018

REPORT TYPE: All M/P

LOCKBOX PARAMETER UPDATES

-------------------------- Values

Parameter Date/Time Edited Old New User

===============================================================================

AUTO-AUDIT MEDICAL PAPER BILLS 11/13/18@10:13:04 Yes No USER,ONE

AUTO-AUDIT RX PAPER BILLS 11/13/18@10:13:05 Yes No USER,ONE

AUTO-AUDIT MEDICAL EDI BILLS 11/13/18@10:13:07 Yes No USER,ONE

AUTO-AUDIT RX EDI BILLS 11/13/18@10:13:09 Yes No USER,ONE

AUTO-POST RX CLAIMS ENABLED 11/15/18@11:03:40 No Yes USER,ONE

TRICARE EFT POST PREVENT DAYS 11/15/18@11:18:49 14 30 USER,ONE

TRICARE EFT POST PREVENT DAYS 11/15/18@11:19:14 30 14 USER,ONE

AUTO-POST RX CLAIMS ENABLED 11/15/18@11:19:30 Yes No USER,ONE

AUTO-POST MED CLAIMS ENABLED 11/15/18@11:55:51 Yes No USER,ONE

AUTO-POST MED CLAIMS ENABLED 11/16/18@12:20:44 No Yes USER,ONE

AUTO-DECREASE MED NOPAY ENABLED 11/16/18@12:21:01 No Yes USER,ONE

AUTO-DECREASE MED AMT DEFAULT 11/16/18@13:48:25 250 7000 USER,ONE

CARC AUTO DECREASE NO-PAY (45) 11/16/18@13:51:17 No Yes USER,ONE

AUTO-DECREASE RX ENABLED 11/16/18@12:21:01 No Yes USER,ONE

AUTO-DECREASE RX AMT DEFAULT 11/16/18@13:48:25 250 7000 USER,ONE

CARC AUTO DECREASE RX (45) 11/16/18@13:51:17 No Yes USER,ONE

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## Parameters Report – EDI Lockbox Exclusion Audit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Lockbox Exclusion Audit Report provides an audit of changes to excluded payers. The information on the report contains the date and time a payer was added or removed from the exclusion list, the user who completed the edit and a comment.

#### When to run this report

Review the EDI Lockbox Exclusion Audit Report on an as-needed basis to view or print changes to payer exclusions. The report can be run on-demand.

#### How to run this report

To run the EDI Lockbox Exclusion Audit Report, enter a start date and end date and select a division. The resulting report will contain payer exclusions that have been changed within the date range. The report can also be exported to Excel.

EDI Lockbox Exclusion Audit Report

M)EDICAL, (P)HARMACY, OR (B)OTH: BOTH//

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

Added UNITED HEALTH CARE 1362739571 8/29/18@08:50:50 USER,ONE

Comment: testing

Added AETNA -CONTINENTAL LIFE INSURA 9/20/18@09:05:40 USER,ONE

Comment: testing

Press enter to continue, '^' to exit:

EDI Lockbox Exclusion Audit Report Page: 2

DIVISIONS: ALL

RUN DATE: 12/6/2018@07:41:38

DATE RANGE: 8/28/2018 - 12/6/2018

REPORT TYPE: ALL

PHARMACY AUTO-POSTING PAYER EXCLUSION LIST

------------------------------------------

Change Payer Date/Time Edited User

===============================================================================

Added AETNA 1066033492 8/29/18@08:51:06 USER,ONE

Comment: testing

PHARMACY AUTO-DECREASE PAYER EXCLUSION LIST

------------------------------------------

Change Payer Date/Time Edited User

===============================================================================

Added UNITED HEALTH CARE 1362739571 8/29/18@08:50:50 USER,ONE

Comment: testing

Added AETNA -CONTINENTAL LIFE INSURA 9/20/18@09:05:40 USER,ONE

Comment: testing

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## Mail groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Seven mail groups are associated with EDI Lockbox. The names of these mail groups are:

RCDPE PAYMENTS: This group will receive all reports and bulletins generated by the nightly processing job and from all other EDI Lockbox jobs, except for those resulting from exceptions found when storing the EDI Lockbox transmission records.

RCDPE PAYMENTS EXCEPTIONS: This group will receive all bulletins for exception conditions generated by the receipt of all EDI Lockbox electronic messages. Exceptions occur when the software cannot identify a bill number in the site’s VistA system. This group also receives error bulletins generated by the receipt and processing of the CARC/RARC date from the FSC.

RCDPE PAYMENTS MGMT: This group previously received the bulletin that is sent when an EEOB transferred out of the site is accepted by another site. Transfer functionality is no longer available.

RCDPE AUDIT: This group will systematically notify management of critical outstanding workload related to aged ERAs and EFTs. This includes

- Unmatched ERAs greater than 30 days
- Matched/not posted ERAs greater than 30 days
- EFTs greater than 14 days

The AR application will flag the above-mentioned bulletins as high priority. These bulletins can be scheduled weekly, biweekly or monthly and the specific day of the week can be set in the EDI Lockbox parameters. All bulletins will be scheduled for the same cycle. End users can self-enroll in this mail group.

RCDPE MOVE COPY: This mail group previously received bulletins sent by the AR nightly process. The bulletins are no longer sent.

MLB: This mail group receives all transmission messages relating to EDI Lockbox. These messages contain the detailed transmission data.

> It is a local decision as to who will be members of these mail groups. It is recommended at a minimum that the MCCF Supervisor or Lead AR be included. Important: The electronic data is sent to VistA thru these mail man messages. If no one is assigned to these mail groups, the electronic data will not be stored in VistA. These messages also help with trouble shooting and problem solving. Appendix E contains a list of the bulletins and recommendations on how to handle each message.

CARC_RARC_DATA: This mail group receives all transmission messages related to CARC/RARC data sent by the FSC. These messages contain the detailed transmission data that automatically updates CARC/RARC data in VistA.

> It is a local decision as to who will be members of this mail group. It is recommended at a minimum that the local IRM be included. Important: These messages may help with trouble shooting and problem solving that may be needed; any error messages will be sent as an error bulletin to RCDPE PAYMENTS EXCEPTIONS group containing all errors discovered in the entire message.

## How to read an ERA/835 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 835 is a transaction set created by HIPAA standards. The transaction format defines what data should be included in the Electronic Remittance Advice (ERA) for use in the world of Electronic Data Interchange (EDI). ‘835’ is the technical term used in the healthcare industry when referring to an ERA – Electronic Remittance Advice. ERAs or 835’s can be found in the ePayments software in the worklist, view/print options, or under Billed Charges (BC) in the TPJI menu. ERA’s are sent in a standard format as defined by HIPAA and include standard Claim adjustment reason codes (CARC’s).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>EDI LOCKBOX EEOB DETAIL FROM WORKLIST 7/22/10 Page: 1</p>
<p>ERA NUMBER: 9876543210 ERA DATE: Jul 21, 2010</p>
<p>INS COMPANY: IBinsurance Company One/555555555</p>
<p>ERA TRACE #: 123456789012345678901234567890123456789</p>
<p>================================================================================</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The example above shows the user the ERA number, trace number and date, and payer information. This is on page 1 of the ERA.

EDI LOCKBOX EEOB DETAIL FROM WORKLIST 10/12/18 Page: 1

ERA NUMBER: 93324 ERA DATE: Oct 02, 2018

INS COMPANY: AETNA/1066033492

ERA TRACE \#: ABC6492325843

================================================================================

CLAIM \#: 442-K505S5I

ORIGINAL PATIENT NAME: PATIENT,ONE

EOB GENERAL INFORMATION:

Type : NORMAL EOB EOB Paid DT : 10/02/18

Entry Dt/Tm :10/02/18 7:11 am Claim Status : PROCESSED

Entry Dt/Tm :10/02/18 7:11 am Review Status: ACCEPTED-COMPLETE EOB

Entered By : Insurance Seq: SECONDARY

Last Edited : 10/02/18 7:12 am Last Edit By : POSTMASTER

Patient Name: CASE,ONE Pt. Relation : PATIENT

Insured ID : 1000880268

Claim Rec'd Date :

Other Subscriber Name:

Also included on page 1 are the bill number, patient name, ID number, claim status, and patient relationship.

The User sees the Payer Information including payer name, payer ID number, and the payers Internal Control Number (ICN) and any other claim level contact information on page 2. The claim level contact information can also be viewed from the Claim Information -\> Comment History option available under TPJI. TPJI is available through many menu paths, such as EDI Lockbox -\> ERA Worklist -\> Select ERA -\> Research Menu -\> TPJI.

EDI LOCKBOX EEOB DETAIL FROM WORKLIST 7/22/10 Page: 3

ERA NUMBER: 9876543210 ERA DATE: Jul 21, 2010

INS COMPANY: IBinsurance Company One/555555555

ERA TRACE \#: 1234567890123456789012345678901234567890123456789

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

The top of page 3 shows the user the submitted charges, covered amount, and amount paid in the Claim Level Pay status section of the ERA.

EDI LOCKBOX EEOB DETAIL FROM WORKLIST 7/22/10 Page: 3

ERA NUMBER: 9876543210 ERA DATE: Jul 21, 2010

INS COMPANY: IBinsurance Company One/555555555

ERA TRACE \#: 1234567890123456789012345678901234567890123456789

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

Enter RETURN to continue or '^' to exit:

At the bottom of page 3, the user can see the Claim Adjudication details which include the HIPAA standardized justification codes. Adjudication details can be continued on page 4 depending on the number of procedures included on the claim to the payer.

## Workload Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AR application systematically notifies management of critical outstanding workload related to aged ERAs and EFTs. There are 4workload notifications. They are the Unmatched ERA’s \> 30 days, the Paper Matched/Not Posted ERAs \> 30 days, the EFT Matched/Not Posted ERAs \>30 days, and the Unmatched EFTs \> 14 days. The notifications are sent to a mail group, RCPDE Audit, and can be queued for weekly, bi-weekly, or monthly notifications. All the notifications will be flagged as high priority.

### Unmatched ERAs \> 30 days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A warning bulletin is sent to the RCDPE AUDIT Mail Group for unmatched ERAs greater than 30 days.

### PAPER Matched/Not Posted ERAs \> 30 Days 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A warning bulletin is sent to the RCDPE AUDIT mail group for Paper Checks Matched/Not Posted that are matched to ERAs \>30 days but not yet posted.

From: POSTMASTER@XXXXX.MED.VA.GOV

Sent: Thursday, July 31, 2014 6:01 AM  
To: "G.RCDPE AUDIT"@XXXXX.MED.VA.GOV  
Subject: EDI LBOX-STA# 504-ACTION REQ-PAPER:Matched/Not Posted ERA\>30 days

Importance: High

The listed ERAs were received more than 30 days ago and have been matched but  
have not been posted  
   
Total \# of ERAs - “MATCHED TO PAPER CHECK” - 4  
Total Dollar Amount - \$2,076.49  
   
ERA#        PAYER NAME                                FILE DATE    AMOUNT PAID  
78596       CONNECTICUT GENERAL LIFE INSURANCE           4/4/12          \$2.04  
79195       WOODMEN OF THE WORLD ASSURED LIFE A         4/19/12      \$1,831.22  
79917       THRIVENT FINANCIAL FOR LUTHERANS             5/7/12        \$102.20  
80484       NALC HBP                                    5/18/12        \$141.03  
\*\* END OF REPORT \*\*

### EFT Matched/Not Posted ERAs \> 30 days Bulletin 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A warning bulletin is sent to the RCDPE AUDIT mail group for EFT Matched/EFTs that are matched to an ERA \>30 days but not yet posted.

From: POSTMASTER@XXXXX.MED.VA.GOV  
Sent: Thursday, July 31, 2014 6:01 AM  
To: "G.RCDPE AUDIT"@XXXXX.MED.VA.GOV  
Subject: EDI LBOX-STA# 504-ACTION REQ-EFT:Matched/Not Posted ERA\>30 days

Importance: High

The listed ERAs were received more than 30 days ago and have been matched but  
have not been posted  
   
Total \# of ERAs - “MATCHED TO EFT” - 5  
Total Dollar Amount - \$2,041.91

ERA#        PAYER NAME                                FILE DATE    AMOUNT PAID 80933       OUTREACH HEALTH CARE SERVICES               5/31/12      \$1,227.73  
82352       ValueOptions, Inc.                          7/11/12        \$144.68  
83339       ROYAL NEIGHBORS OF AMERICA                   8/2/12         \$33.70  
83496       TLPEXTON                                     8/6/12          \$8.99  
83667       NALC HBP                                    8/10/12        \$626.81

\*\* END OF REPORT \*\*

### Unmatched EFTs \> 14 days

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

5694XX617 BCBS OKFEPDENTAL/F14098E000X186X 4/11/14 \$32.00

5694XX621 BCBS OKFEPDENTAL/F14104E000X244X 5/17/14 \$8.00

5694XX675 BCBS OKFEPDENTAL/F14181E000X986X 6/3/14 \$32.00

5694XX680 COMMUNITYCARE LI/5200088 7/11/14 \$15.99

\*\* END OF REPORT \*\*

### Suspense Entry Bulletin 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A warning bulletin is sent to the RCDPE AUDIT Mail Group for Suspense Entries overdue for processing. The suspense parameter determines when an entry is overdue and captured on the Suspense Entry Bulletin.

From: POSTMASTER@xxxxxx \[mailto:POSTMASTER@xxxxxxxxx\]  
Sent: Thursday, July 31, 2014 6:01 AM  
To: "G.RCDPE AUDIT"@xxxxxxxxx  
Subject: EDI LBOX-STA# 623-SUSPENSE ENTRIES OVERDUE FOR PROCESSING  
Importance: High

The following entries have been in Suspense past the \#days allowed by the site parameter – which is currently set at 45 days.

Total \# of Overdue Entries in Suspense - 3

Total Dollar Amount Overdue in Suspense - \$21446.47

SUSP DATE \#DAYS USER RECEIPT# AMOUNT DISP REASON

03/11/14 145 AB 7080793I \$5500.00 PENDING NO BILL \# OR EOB

04/15/14 112 RT 7354664R \$15788.25 PENDING NO BILL \# OR EOB

05/12/14 75 PR L1407020 \$158.22 PENDING NO BILL \# OR EOB

\*\* END OF REPORT \*\*

# Payments Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Daily activities related to processing ePayments are included in this section of the User’s Guide. It is organized by how the daily workflow should be processed – starting with checking e-mail and processing exceptions before proceeding to the ERA Worklist activities.

## Check Email

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 3<sup>rd</sup> Party EDI Lockbox software makes extensive use of e-mail bulletins to alert users about actions taken during the nightly processing of EFTs and ERAs received from payers. Check e-mail for these notifications first thing in the morning to help plan the workday. If you receive a bulletin that states an ERA was rejected because no valid EEOBs were found for your site, you should contact your ePayments POC for assistance to ensure that no data is lost.

Starting with the Clerk’s AR Menu, the user must navigate through two screens in order to access the functionality that is contained in the ERA Worklist/Scratchpad:

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

REFT Remove Duplicate EFT Deposits

REM Remove ERA from Active Worklist

REP EDI Lockbox Reports Menu ...

UN Unmatch An ERA

UP Update ERA Posted Using Paper EOB

ZB Mark 0-Balance EFT Matched

Select EDI Lockbox (ePayments) Option:

## Exception Processing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before starting to process anything on your ERA Worklist, check for exceptions by using the option EXC EDI Lockbox 3rd Party Exceptions located on the EDI Lockbox (ePayments) Menu. Any ERA or EEOB that cannot be automatically and completely matched into both the VistA AR and IB packages will end up on the Exception Report. This includes ERAs with recognized errors that prevent a clean update to automatically occur. Records can be viewed and various options are provided to reconcile the exceptions and move them to the ERA Worklist for processing. An ERA cannot be processed in the ERA Worklist if an exception exists on the ERA. The ERA Worklist will display “x” in front of the ERA number to indicate an exception exists.

<u>ERA List - Worklist Dec 12, 2014@14:18:37 Page: 4 of 7</u>

SELECTED MATCH STATUS: BOTH POST STATUS : BOTH

DATE RANGE: 11/22/14-12/12/14 AUTO-POSTING : BOTH

ALL PAYERS PHARMACY/MEDICAL: BOTH

\# ERA \# Trace#

<u>+ PAYER NAME/MATCH STATUS & DATE ERA PAID DT TOT AMT PAID DT REC'D</u>

11 x5545 6353169460

12/10/14 0.00 12/10/14

AETNA APPROX \# EEOBs: 2

UNMATCHED N/A

Details for processing the exceptions are included below.

There are two types of exceptions, Transmission Exceptions and Data Exceptions, explained below.

*Exceptions should be worked daily and before the scratchpad is created for the ERA.*

### Transmission Exceptions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Transmission Exceptions occur when there was a problem storing ERA EEOB data. Here are three examples of when a transmission error may occur:

1.  All sequences for an ERA that was sent in multiple messages were not received at the site.

> For example, AR cannot process these until ALL of the messages in the batch are received. The exception list contains only 4 of 5 messages. You should wait for the 5th message. If the message is not received in 24 hours, contact EPS at 1-888-596-4357 to enter a remedy ticket and request a re-transmission.

2.  An ERA transmission did not fully complete the permanent update process on a previous date and remains in the file, partially processed. How is this corrected? Enter a remedy ticket, as this is probably the result of a system problem. Once the problem has been resolved, use File Message to process the ERA. Or, if the problem is severe and cannot be resolved, you will be instructed to use DELETE MESSAGE to permanently remove the message from the list.
3.  An ERA cannot identify any claims on the transmission as valid at your station. In Version 1, this information was sent to the sites via e-mail messages. The information contained in the e-mail messages is now stored under the Transmission Exceptions until filed and corrected/saved or deleted.

<u>EEOB TRANSMISSION EXCEPTIONS Jul 01, 2010@10:41:30 Page: 1 of 1</u>

ERA/EEOB MESSAGES WITH EXCEPTION CONDITIONS

\# Message ID Msg Typ Date Received Mail Msg \#

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1 XXXXXXX ERA MAR 05, 2007@18:41 XXXXXXX

EXCEPTION: NO VALID CLAIMS

Payer Name: IBinsurance Company One

Payer ID: 5555555555

Trace \#: XXXXXXXXXXX

Date Paid: 03/02/2007 Total Amt Paid: 22.39

\*XXXKXXXXXXX

Enter ?? for more actions

View/Print Message Delete Message Exit

File Message TPJI

Select Action: Quit//

Figure 3a - Sample Transmission Exception Report

#### Processing Actions for Transmission Exceptions 

Enter ?? for more actions

View/Print Message Delete Message Exit

File Message TPJI

Select Action: Quit//

List Manager options are used to complete the transmission exceptions. Each option is explained in detail below.

- *View/Print Message* – Used to print or view the formatted version of the message and optionally includes the actual text (raw data) received in the message.
- *File Message* – Used to attempt to re-file a message. This could be used if the message was not completely stored in the permanent ELECTRONIC REMITTANCE ADVICE file. When the user selects a message to re-file, the system checks the content of the message and tries to automatically file the data in VistA. If successful, the exception is removed. A bulletin is sent to the RCDPE PAYMENTS mail group reporting the attempt to re-file the message.

> If this action is used with a NO VALID CLAIMS transmission, the exception will be moved to the data transmissions screen where the claim numbers can be edited and the EEOBs filed in IB.

- *Delete Message* – Used to remove the message from the exception list if the message cannot be re-filed into VistA automatically. This action removes the message permanently from the exception list and sends a bulletin to the RCDPE PAYMENTS Mail Group containing the text of the message received.

> The Delete Message action cannot be used if the ERA has a payment method of Automatic Clearing House (ACH). An error message will display.

> Note: The Delete Message action is locked with the security key, RCDPE ERA EXCEPT.

- *TPJI (Third Party Joint Inquiry) –* This is a link to TPJI in case further analysis of the site’s receivables is required.

### Data Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data Exceptions may be filtered to view Medical claims, Pharmacy claims or both and by all payers or a range of payers.

<u>DO YOU WANT TO SEE (T)RANSMISSION OR (D)ATA EXCEPTIONS?: T// DATA</u>

<u>INCLUDE EXCEPTIONS FOR (M)EDICAL, (P)HARMACY, OR (B)OTH?: B// OTH</u>

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: ALL//

A Data Exception occurs when AR cannot match the claim number on the EEOB with a claim number in AR. Here is an example of a Data Exception:

- An EEOB has encountered an error such as a typo or transposed bill number, the action called Edit Claim \# can be used to correct this error.

<u>LOCKBOX EEOB DATA EXCEPTIONS Oct 13, 2010@15:38:12 Page: 1 of 1</u>

EEOB DETAIL DATA WITH EXCEPTION CONDITIONS

\# Trace \# EOB Date

<u>Insurance Co Name/ID .</u>

1 XXXXXXXX XX/XX/XX

IBinsurance Company One/555555555

Seq \#: 49 Bill: \*442-XXXXXXX Pt: IBpatient,One A Pd: 1.82

ECME \#: XXXXXXXXXXXX Release Date:

Comment: Pharmacy comment about prescription

\*\*Exception: VALID BILL NOT FOUND

Enter ?? for more actions

View/Print Message Edit Claim \# Exit

File EEOB in IB TPJI

Remove Exception Pharmacy Claim Comment

Select Action: Quit//

Figure 3b - Sample Data Exception Report

#### Processing Actions for Data Exceptions

Enter ?? for more actions

View/Print Message Edit Claim \# Exit

File EEOB in IB TPJI

Remove Exception Pharmacy Claim Comment

Select Action: Quit//

List Manager options are used to complete the data exceptions. Each option is explained in detail below.

- *View/Print Message* - Used to print or view the exception message and any detail on file for it.
- *File EEOB in IB* - Used to attempt to re-file the EEOB data detail in IB (Integrated Billing) if an exception occurred during a previous update attempt.
- *Remove Exception* - Used if there is no electronic way to resolve the exception condition. This action marks the ERA or EEOB detail record so it no longer appears as an exception. A bulletin will be sent to report this action to the RCDPE PAYMENTS mail group. If an exception is removed, the EEOB will appear in the worklist as ‘not found in AR’
- *Edit Claim \#* - Used to update the claim number to reflect the correct claim number you want to file in the EEOB. TPJI can be used to view the claim detail before changing the claim number. The system will also accept an entry that is not a valid claim number, which will cause money to go to suspense.

> Select Action: Next Screen// ED   Edit Claim \# 

> Select EDI LBox EEOB Data Exception(s):  (96-99): 97

> Selection \#: 97     4343434

> Select A/R Bill this EEOB is actually paying on: SUSPENSE

>    THIS CLAIM WAS NOT FOUND IN YOUR AR.  DO YOU WANT TO CONTINUE?: NO// YES

> EEOB Filed.

> PRESS RETURN TO CONTINUE

> *Note \#1*: The Edit Claim \# function actually REMOVES the old claim number from the ERA Worklist and REPLACES it with the new one. If this change is made in the Worklist, the original number remains on the EEOB and the new number also references the EEOB. It is cleaner to do it here than the Worklist if the error is simply that the wrong bill \# was reported paid.

> *Note \#2*: Once a data exception has been resolved, the system will re-evaluate the ERA to determine if it can be marked for Auto-Post. A message will display if the ERA was successfully Marked for Auto-Post, or the reason it was not successfully marked.

- *TPJI (Third Party Joint Inquiry) –* This is a link to TPJI in case further analysis of the site’s receivables is required.
- *Pharmacy Claim Comment –* Used to enter a one line comment for a non-released prescription. Only the most recent comment is stored and displayed.

### Non-Released Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An ERA for a non-released prescription automatically goes to the exception list because a bill is not created for a prescription until the prescription is released. VistA runs a nightly job to evaluate the ERAs that are on the exception list due to non-released prescriptions. If the prescription has been recently released, a bill exists, and the ERA has no more exception conditions, the nightly job removes the ERA from the exception list. Processing of the ERA continues as normal.

## Working the EEOB Scratchpad 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB Scratchpad is a list of electronic EOB (EEOB) detail records that were included on a selected electronic remittance advice (ERA). It allows for the creation of a receipt that will post each payment contained in each EEOB against the site's A/R and send to FMS. To accomplish this, some manipulation of the payment data may be necessary. The EEOB Scratchpad contains the tools for performing these manipulations (i.e. distribute adjustments, split/edit a payment, etc.).

> **NOTE:** Negative Claim Balance rule is enforced. When making adjustments the claim balance cannot be less than zero dollars (collected/closed status).

Once the WL ERA Worklist option above has been selected, the process begins with at least one question that determines the ERA (ERAs) that is (are) available to be processed. If the user has not saved a preferred view, the questions associated with the Change View action will be asked. See the section on the Change View action for details.

There is one question that will always display, regardless of the preferred view. The prompt asks if one wants to work with a date range selection:

Date Range Selection:

- ALL
- RANGE

The initial list of the ERAs selected will then be presented:

<u>ERA List - Worklist Jul 22, 2010@17:37:06 Page: 1 of 3</u>

SELECTED: MATCH STATUS: BOTH POST STATUS : UNPOSTED

DATE RANGE : NONE SELECTED AUTO-POSTED : BOTH

ALL PAYERS PHARMACY/MEDICAL: BOTH

\# ERA \# TRACE#

<u>PAYER NAME/MATCH STATUS & DATE ERA PAID DT TOT AMT PAID DT REC'D</u>

1 1 12345

10/29/02 20.00 10/29/02

IBinsurance Company One APPROX \# EEOBs: 1

CHK MATCHED 7/21/2010 EFT RECEIPT STATUS: NOT ENTERED

2 1234567891 TEST123

6/8/10 3456.78 6/8/10

IBinsurance Company Two APPROX \# EEOBs: 1

CHK MATCHED 7/21/2010 (CHECK PAYMENT CHOSEN)

3 9876543210 01234567890123456789012345678901234567890123456789

7/21/10 123.45 7/21/10

IBinsurance Company Three APPROX \# EEOBs: 1

CHK MATCHED 7/21/2010 (CHECK PAYMENT CHOSEN)

\+ \|'-' No scratchpad\|'x' EXC \|'A' autopost complete

Select ERA View/Print ERA Admin Cost Adj

Sort List Change View

Mark for Auto Post ERA Manual Match Exit

Select Action: Next Screen//

Figure 4 - Sample ERA List – Worklist (list manager worklist)

### ERA List - Worklist Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of list manager options available on the ERA Worklist screen that provides greater capability to manage records at the ERA level.

|                |                                                                                                                                                                                                                                        |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select ERA     | Used to select a specific ERA.                                                                                                                                                                                                         |
| Sort List      | Allows the user to sort the ERA worklist by multiple criteria; amount paid, payer name, ERA paid date, or date ERA received. Sorting the worklist by these criteria does not change the list of the individual EEOB’s within each ERA. |
| View/Print ERA | Used to display/print the summary ERA information.                                                                                                                                                                                     |
| Change View    | Used to customize the information displayed on the ERA worklist.                                                                                                                                                                       |
| Admin Cost Adj | Used to make Administrative Cost Adjustments to a claim.                                                                                                                                                                               |

#### Sort List

In order to work more efficiently with ERAs, the user can choose selections from two different sort levels in order to identify the ERAs to be worked on first:

- First Level Sort: Amount Paid, Payer Name, ERA Paid Date, Date ERA Received
- Second Level Sort: None, or any of the data elements listed in the First Level Sort (cannot use the same sort twice)

#### View/Print ERA

The View/Print ERA action is used to display and print the summary ERA information. If a data exception exists for the selected ERA, a warning message will display. The user must press enter to continue.

Select \#: (6-9): 9

> **WARNING:** Fix Transmission Exceptions first and then Data Exceptions

with the EXE EDI Lockbox 3rd Party Exceptions option which is located

on the EDI Lockbox (ePayments) Main Menu.

PRESS ENTER TO CONTINUE

The View/Print ERA action displays an AUTO-POST STATUS of UNPOSTED, PARTIAL or COMPLETE, at the ERA summary level and EEOB detail level.

#### Change View

The Change View action is used to customize the information displayed on the ERA worklist. After answering the questions, the system gives the user the option to “SAVE” the selections as a “preferred view”. If the user saves a preferred view they will be prompted if they want to use that view in the future.

The answers are used to filter the worklist display to limit the entries that are included.

The following options are available as filters.

Select Action: Next Screen// C Change View

SELECT PARAMETERS FOR DISPLAYING THE LIST OF ERAs

(Z)ERO, (P)AYMENT, or (B)OTH: B//

ERA posting status: (U)NPOSTED, (P)OSTED, or (B)OTH: U//

DISPLAY (A)UTO-POSTING, (N)ON AUTO-POSTING, OR (B)OTH: B// OTH

(M)ARKED, (P)ARTIAL, (C)OMPLETE OR (A)LL: A// LL

ERA-EFT MATCH STATUS: (N)OT MATCHED, (M)ATCHED, or (B)OTH: B//

(M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: A//

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: A// LL

DO YOU WANT TO SAVE THIS AS YOUR PREFERRED VIEW (Y/N)? NO//

> Select Parameters for Displaying the List of ERAs:

- Zero – Show only zero dollar ERAs
- Payment – Show only ERAs with payments
- Both – Show both zero dollar and ERAs with payments

> ERA Posting Status:

- UNPOSTED – ERA/Receipt has not been posted to FMS
- POSTED - ERA/Receipt has been posted to FMS

> Auto-Posting Qualification

- AUTO-POSTING – ERA meets criteria for auto-posting
- NON AUTO-POSTING – ERA does not meet criteria for auto-posting
- BOTH – All ERAs, regardless of criteria for auto-posting

> Partial Posted and Marked for Auto-Post Status:

- Select MARKED to only see ERAs currently marked for auto-post
- Select PARTIAL to only see ERAs with a partial auto-post status
- Select COMPLETE to only see ERAs with a complete auto-post status
- Select ALL to see ERAs with any auto-post status

> ERA-EFT Match Status:

- NOT MATCHED – ERA has not been matched with an EFT (automatically by nightly job) – or – ERA has not been matched with a paper check by user - or - ERA has not been matched with a Ø -payment by the user
- MATCHED - ERA was matched with an EFT (automatically by nightly job) – or – ERA was matched with a paper check by user) – or – ERA was matched with a Ø-payment by user
- BOTH – list both Not Matched and Matched ERAs

> Claim Type:

- MEDICAL – ERAs for Third Party Medical Claims
- PHARMACY – ERAs for Pharmacy Claims
- TRICARE – ERAs for Tricare Claims
- All – ERAS for Third Party Medical Claims, Pharmacy Claims and Tricare Claims

> Payer Range Selection:

- ALL
- RANGE

#### Select ERA

The Select ERA action allows the user to select a specific ERA by number

If a user selects an ERA with one or more exceptions, the software will alert the user by displaying a warning that access is denied until all exceptions for that particular ERA are resolved. Users now have the option to go to exceptions from the worklist.

> ACCESS DENIED: Scratchpad creation is not allowed when Exceptions exist. Fix Transmission Exceptions first and then Data Exceptions via the EXC EDI Lockbox 3rd Party Exceptions option which is located on the EDI Lockbox Main Menu.

> <u>Do you want to begin clearing Exceptions for this ERA (Y/N)? Y//</u>

If the user selects Y, the user “jumps” to the exceptions list to begin clearing exceptions following the existing process. The user is returned to the Worklist if the user selects to exit the exceptions process or if the user enters "N" to the original prompt and does NOT want to begin clearing Exceptions.

If the user selects an ERA that does not have a scratch pad, three options display.

|                   |                                                              |
|-------------------|--------------------------------------------------------------|
| Option        | Description                                              |
| Create Scratchpad | Used to create a scratchpad.                                 |
| View ERA Details  | Used to View/Print ERA; a scratchpad is not created.         |
| Exit              | Used to return to the worklist; a scratchpad is not created. |

The user will be automatically prompted to select the display order for payment information before continuing to the scratchpad screen.

Once the ERA is selected, if the payer has indicated a PAYMENT METHOD CODE on the ERA, it will be displayed here. This can be used as a guide as to how the payer has decided to send the payment for this ERA to the site. Some examples are: CHK indicates a paper check should be expected; NON-indicates an Ø-payment; ACH indicates an EFT should be expected; FWT indicates a federal wire transfer.

If the PAYMENT METHOD CODE indicates NON or CHK and is a zero-payment ERA, respond YES to the next prompt to mark the ERA as MATCH-Ø-PAYMENT.

If matching a paper check with an ERA, enter the check \# and date of the check.

<u>ERA Worklist/Scratch Pad Jul 21, 2010@12:17:58 Page: 1 of 1</u>

ERA Entry \#: 9876543210 Total Amt Pd: 123.45 Current View:

Payer Name/ID: IBinsurance Company One/55555555 NO SORT ORDER

PAPER CHECK \#: 1003 ALL EEOBs

1 EEOB Seq \# On ERA: 1 Net Payment Amt: 123.45

1.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One A/5555

Claim Bal: 0.00 Billed Amt: 0.00 Amt To Post: 123.45

Svc Dt: 6/1/00 COB: NO Rx Copay: UNKNOWN Means Tst: ??

Payment Amt: 123.45 Total Adjustments: 0.00 Net: 123.45

ECME \#: XXXXXXXXXXXX

Rx/Fill/Release Status: XXXXXXX/1/Released

DOS: 1/4/13

..............................................................................

 

 

 

 

Enter ?? for more action

Split/Edit A Line Look At Receipt Mark for Auto Post

Distribute Adj Amts Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen//

Figure 5 - Sample ERA Worklist/Scratch Pad

The header of the ERA Worklist/Scratch Pad screen contains the ERA Entry \#; the Name and ID number of the Payer; the Total Amount being Paid on the ERA (this will equal the dollar amount of the Electronic Funds Transfer or Paper Check received from the Payer; and the EFT Trace \# or the number from the Paper.

Each EEOB line item equates to a line item on a paper EOB form. The advantage is that the information on the ERA Worklist/Scratch Pad will always be in the same location, regardless of Payer. HIPAA mandates standardization of the electronic transmissions.

| Field               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EEOB Seq \# on ERA:     | This shows the line item order as the payer sent it. Remember, the Worklist can be sorted with Zero Payments First or Zero Payments Last, so the sequence number may not match the line item list on the far left of the screen.                                                                                                                                                                                                                                                                                                                                        |
| Net Payment Amt:        | The payment amount plus or minus the adjustment amount will equal the net payment amount for this claim number.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Claim \#:               | The claims number associated with this payment. This may or may not be the correct claim number. Research each claim carefully to see the amount being paid is appropriate for the claim in AR. Test sites have identified Payer errors (typos) that could result in a payment being applied to the wrong claim if not corrected by using the Split/Edit A Line action. If the line item is marked (V), the system has already done a verification match between bill number and the patient name, last four of the social, date of service and original billed amount. |
| Patient/Last 4:         | The patient’s name and last four digits from their SSN. Used to help identify this payment is for the correct Claim.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Claim Balance:          | Current balance from AR.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Billed Amt:             | Original billed amount from AR.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Amount to Post:         | The payment amount plus or minus the adjustment amount will equal the amount to post for this claim number.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Service Date:           | Beginning Service Date for this Claim                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| COB:                    | Coordination of Benefits information that indicates whether a secondary payer has been identified for this claim.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Rx Copay:               | Current Rx Copay status of the patient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Means Test:             | Indicates if this patient may be responsible for Means Test co-payments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Payment Amt:            | Amount of money paid for this claim on this ERA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Total Adjustments:      | Net total of all adjustments for this line item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Net:                    | The payment amount plus or minus the adjustment amount.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ECME \#:                | ECME number generated when the NCPDP claim is submitted for a pharmacy prescription. This field only displays for a pharmacy claim.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Rx/Fill/Release Status: | The prescription number, fill number and release status (released, non-released). This field only displays for a pharmacy claim.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DOS:                    | The date of service submitted on the NCPDP claim. This field only displays for a pharmacy claim.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

If there are unposted payments (EFTs), the system may block access to the scratchpad. Based on the age of the oldest EFT, the system may generate a warning message, an error message, or no message.

|                   |                                                                    |                                                                    |
|-------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| Type of Claim | Age of oldest EFT                                              | Result                                                         |
| Medical           | Less than or equal to 14 calendar days                             | No warning message or error message displays.                      |
| Medical           | More than 14 calendar days                                         | A warning message displays. The user must press enter to continue. |
| Medical           | More than the number of calendar days specified in site parameters | An error message displays. The user is not allowed to continue.    |
| Pharmacy          | Less than or equal to 21 calendar days                             | No warning message or error message displays.                      |
| Pharmacy          | More than 21 calendar days                                         | A warning message displays. The user must press enter to continue. |
| Pharmacy          | More than the number of calendar days specified in site parameters | An error message displays. The user is not allowed to continue.    |

The warning messages and error messages display the trace numbers of the older EFTs to allow the users to research and resolve the problem. If a posting override exists, the warning messages and error messages are suppressed. See the section on posting overrides for more information.

### Worklist Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of actions available on the ERA Worklist/Scratchpad that can assist a user to ensure that the correct payment is being applied to the correct claim.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Action</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Split/Edit a Line</td>
<td><p>Used to split a payment or adjustment between two or more bills (if the payer has combined payments) or to correct the claim # associated with a payment (if the payer has reported the payment for the wrong bill).</p>
<p>The automatic update of EEOB information to reflect the split/edit of claims will occur at receipt creation in the PRCA nightly auto-post job (for APAR) or at receipt creation in the ERA Worklist.</p>
<p>Note: This action is not available for an auto-posted ERA.</p></td>
</tr>
<tr class="odd">
<td>Distribute Adj Amt</td>
<td><p>Used to balance the receipt total to be posted with the total amount deposited if the payer sends a takeback within the ERA.</p>
<p>Note: This action now allows adjustments to lines marked as ‘Claim not found in AR’.</p>
<p>Note: This action is not available for an auto-posted ERA.</p></td>
</tr>
<tr class="even">
<td>Refresh Scratch Pad</td>
<td><p>Restores the scratch pad record to the original lines extracted from the ERA. All previous actions (splits/ edits/ comments) that were performed will be deleted and must be re-entered.</p>
<p>Note: This action is not available for an auto-posted ERA.</p>
<p>This is locked with the security key “RCDPEPP”.</p></td>
</tr>
<tr class="odd">
<td>Research Menu</td>
<td>Link to all the necessary AR functions/ processes such as TPJI, needed to process ERAs. These can each still be accessed through regular AR menu options.</td>
</tr>
<tr class="even">
<td>Look at Receipt</td>
<td><p>Compiles the payments in the ERA Worklist/Scratch Pad and displays the lines that will be entered on a receipt.</p>
<p>Note: This action is not available for unposted EEOBs that are part of an auto-posted ERA. For auto-posted ERAs, only one receipt displays at once.</p>
<p>This is locked with the security key “RCDPEPP”.</p></td>
</tr>
<tr class="odd">
<td>Review Line</td>
<td>Allows addition of comments or used as a bookmark on a specific line within an ERA in case processing was interrupted, thereby allowing the user to more easily resume where he/she left off. This option must be turned ‘on’ each time the user enters the ERA to enter or view comments.</td>
</tr>
<tr class="even">
<td>Verify</td>
<td><p>Provides the functionality to identify and manually mark EEOBs as verified.</p>
<p>Note: This action is not available for an auto-posted ERA.</p>
<p>This is locked with the security key “RCDPEPP”.</p></td>
</tr>
<tr class="odd">
<td>Change View</td>
<td>Used to customize the information displayed on the ERA worklist.</td>
</tr>
<tr class="even">
<td>Mark for Auto Post</td>
<td><p>Option used to indicate the ERA is ready for the software to auto post the ERA during the next nightly process.</p>
<p>This is locked with the security key “RCDPEPP”.</p></td>
</tr>
<tr class="odd">
<td>View/Print ERA</td>
<td>Used to view/print the entire formatted ERA, with or without the EEOB detail.</td>
</tr>
<tr class="even">
<td>Receipt Processing</td>
<td><p>Option that allows the user to process a receipt.</p>
<p>This is locked with the security key “RCDPEPP”.</p></td>
</tr>
<tr class="odd">
<td>EXIT</td>
<td></td>
</tr>
</tbody>
</table>

> **NOTE:** The system is modified to remove case sensitivity when comparing Trace \#s while manually matching an ERA/EFT.

#### Split/Edit a Line 

Sometimes Payers combine payments for two or more claims onto one claim. This action is used to split the payment to the appropriate claim. It can also be used to correct an incorrect claim number.

<u>ERA Worklist/Scratch Pad Oct 07, 2003@16:55:39 Page: 2 of 3</u>

ERA Entry \#: 21 Total Amt Pd: 1165.99 Current View:

Payer Name/ID: Aetna/US Healthcare/1953402799 NO SORT ORDER

PAPER CHECK \#: 05507-93746289 ALL EEOBs

\+

3 EEOB Seq \# On ERA: 3 Net Payment Amt: 812.00

3.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/1234

Claim Bal: 14850.54 Billed Amt: 14850.54 Amt To Post: 812.00

Svc Dt: 12/12/02 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 812.00 Total Adjustments: 0.00 Net: 812.00

............................................................................

4 EEOB Seq \# On ERA: 4 Net Payment Amt: 343.99

4.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/1234

Claim Bal: 100.00 Billed Amt: 100.00 Amt To Post: 343.99

Svc Dt: 1/22/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 343.99 Total Adjustments: 0.00 Net: 343.99

...........................................................................

Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

View/Print EEOB Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen//

This example shows how to Split/Edit Line item \#4 to post the payment correctly. This action takes place after reviewing the EEOB detailed data to confirm how the payment should be applied.

Select Action: Next Screen// Split/Edit A Line

SELECT THE ENTRY THAT HAS A LINE YOU NEED TO SPLIT/EDIT

Select EEOB Line: (3-4): 4

4.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/1234

Claim Bal: 100.00 Billed Amt: 1719.92 Amt To Post: 343.99

Svc Dt: 1/22/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 343.99 Total Adjustments: 0.00 Net: 343.99

.............................................................................

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

Enter ?? for more actions………………………………………………………………………………………………………….

File New Lines Edit Lines Split Exit

Select Action:Quit// File New Lines

Edit Line Split if the information is not correct. File the new lines to save this information. *Exiting without filing will mean all changes are discarded.*

4 EEOB Seq \# On ERA: 4 Net Payment Amt: 343.99

4.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/1234

Claim Bal: 100.00 Billed Amt: 1719.92 Amt To Post: 100.00

Svc Dt: 1/22/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 100.00 Total Adjustments: 0.00 Net: 100.00

Receipt Comment: SPLIT PAYMENT REMAINDER APPLIED TO KXXXXXX

..............................................................................

4.002 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/1234

Claim Bal: 2341.39 Billed Amt: 2341.39 Amt To Post: 243.99

Svc Dt: 1/22/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 243.99 Total Adjustments: 0.00 Net: 243.99

Receipt Comment: SPLIT PAYMENT - ORIG APPLIED TO KXXXXXX

Sub lines are created for each EEOB line item to allow the payment amounts to be split and distributed as necessary. The sub lines are numbered in increments of .001. In this example, the sub-lines are numbered 4.001 and 4.002.

Reason text (i.e. Comment) is mandatory when leaving a portion of the payment in suspense.

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

The scratchpad screen displays the following if a receipt line comment has been added

2.002 Claim \#: SUPENSE Patient/Last 4: ??

\*\*\*CLAIM NOT FOUND IN YOUR AR \*\*\*

Payment Amt: 160.00 Total Adjustments: 0.00 Net: 160.00

Receipt: E1702150EB

Receipt Comment: OVERPAYMENT

Added By: EMPLOYEE,ONE

Date/Time Added: July 20 2017@10:00:00

#### Distribute Adj Amt 

There are circumstances where payers determine they have ‘overpaid’ a VA facility on a claim. There are two possible ways Payers process transactions to recoup overpayments:

- Process a retraction of funds on a subsequent payment (take back)
- Issue a negative payment adjustment (clipped payment)

Here are two examples showing how a ‘clipped payment’ and a ‘take back’ will appear on an ERA.

*Example One:* Take back

VA billed Payer \$200.00 for care. Payer issued a payment for \$160.00 (80% of the billed amount). A Payer review shows policy should have paid at 60% so the actual payment should have been \$120.00.

3 EEOB Seq \# On ERA: 3 Net Payment Amt: -40.00

3.001 Claim \#: KXXXXXX Patient/Last 4: VA Patient One/1234

Claim Bal: 0.00 Billed Amt: 200.00 Amt To Post: -40.00

Svc Dt: 12/12/02 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 120.00 Total Adjustments: -160.00 Net: -40.00

In this example, the Payer sent an EEOB with both the new payment amount (\$120.00) and the retraction of the incorrect payment (-\$160.00). This resulted in the Net Payment amount of a negative number (-\$40.00) being recorded on this EEOB. Use the action called Distribute Adj Amts on the ERA Worklist to decrease the payments received on one or more of the other claims within the ERA. See the Distributed Adjustments section of this guide for instructions on how to perform this action.

*Example Two:* Clipped Payment

Payer determines an overpayment of \$14.00 was made to VA. Rather than process a negative transaction adjustment on as specific VA claim, they process a non-specific retraction.

1 EEOB Seq \# On ERA: ADJ1 Net Payment Amt: -14.00

1.001\*\*\*ADJUSTMENT AT ERA LEVEL

Payment Amt: 0.00 Total Adjustments: -14.00 Net: -14.00

ADJUSTMENTS:

1\. Non-specific retraction (ref# S1234): -14.00

The EEOB line shows an adjustment at an ERA level. This is because the Payer did not provide a VA claim number. The Payment Amount will show as \$0.00 and the adjustment amount -\$14.00. The net payment amount is -\$14.00. The Ref \# is provided by the Payer as a way for both you and the payer to identify and track this transaction. The Adjustment comments show this is a non-specific retraction with no reference to a claim number. Again, use the action called Distribute Adj Amts on the ERA Worklist to decrease the payments received on one or more of the other claims within the ERA. .

Sometimes Payers will process non-specific payments to VA.

2 EEOB Seq \# On ERA: ADJ2 Net Payment Amt: 24.00

2.001\*\*\*ADJUSTMENT AT ERA LEVEL

Payment Amt: 0.00 Total Adjustments: 24.00 Net: 24.00

ADJUSTMENTS:

1\. Non-specific payment (ref# A1234): 24.00

ERA level adjustments do not reference individual claims. The payment amount = Ø, the total adjustments is a positive number (\$24.00) and with a net payment for the amount adjusted (negative for a retraction/positive for an additional payment). The Ref \# is provided by the Payer as a way for both you and the payer to identify and track this transaction. This non-specific payment will be placed in your facility’s suspense account when the receipt is processed for this ERA.

Use the *Distribute Adj Amt* action to resolve take-backs and clipped payments.

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

\> RETRACTED FOR ERA ADJ \#1 Ref: S1234

Replace \<RET\>

An adjustment amount can be distributed against several lines if necessary. The user does not have to perform an adjustment for the take back amount. A DECREASE ADJUSTMENT will be automatically performed for the decreased amount when the user processes the receipt for posting if the Worklist is used to create the receipt. A standard comment will be used will be used when the DECREASE ADJUSTMENT is sent unless a new comment is entered. (It is up to each station to determine if the default comment is used or a more detailed comment needs to be entered by the user.)

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

1\. Non-specific retraction (ref# S1234): -14.00

2\. Adjustment distribution to balance receipt: 14.00

RETRACTED FUNDS DEDUCTED FROM OTHER PAYMENT ON THIS ERA

...........................................................................

4.001 Claim \#: KXXXXXX Patient/Last 4: VA Patient One/1234

Claim Bal: 2341.39 Billed Amt: 2341.39 Amt To Post: 229.99

Svc Dt: 1/22/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: YES

Payment Amt: 243.99 Total Adjustments: -14.00 Net: 229.99

ADJUSTMENTS:

1\. Distributed adj dec for retraction S1234: -14

RETRACTED FOR ERA ADJ \#1 Ref: S1234

An adjustment record is then displayed attached to BOTH lines selected, indicating the action that was taken. The negative net payment line will have its net amount automatically increased by the amount selected and show a Net Payment Amount of zero. The line with the positive net payment data will be automatically decreased by this same amount to balance the amount of the deposit/check with the amount being posted. The Total Adjustments field shows the amount adjusted, while the Amount to Post and Net show the new payment amount.

#### View/Print EEOB and View/Print ERA 

These Worklist actions are used to display/print the detail received from a Payer. Where the View/Print EEOB will only show the information for one line on the ERA, the View/Print ERA will show detailed information on each and every EEOB line for the entire ERA. Here is a sample of the EEOB information sent by Payers.

<u>ePayments ERA/EEOB Data Oct 15, 2018@07:13:22 Page: 1 of 3\_\_\_\_</u>

%K8000Y0 CASE,ONE K4520 DOB: 10/16/1964 Subsc ID: 553304520

Svc Date: 05/24/2007 Orig Amt: 67.27 ERA#: 18024

\*\* ERA SUMMARY DATA \*\*

ERA#: 18024 TRACE#: 0044912703

ERA DATE (PAYER): OCT 06, 2007 TOTAL AMT PD: 53.82

PAYER NAME/TIN: GREAT-WEST LIFE/1840467907

FILE DATE/TIME: OCT 09, 2007@18:24:08

EFT MATCH STATUS: MATCHED TO PAPER CHECK

ERA TYPE: ERA INDIVIDUAL EOB COUNT: 1

MAIL MESSAGE: 9890147 CHECK#: 0044912703

DETAIL POST STATUS: POSTED EXPECTED PAYMENT METHOD CODE: CHK

\*\*\*\*\*\*\*\*\*\* ERA LEVEL ADJUSTMENTS \*\*\*\*\*\*\*\*\*\*

-- NONE --

\*\*\*\*\*\*\*\*\*\* EOB/835 INFORMATION (1 of 1) \*\*\*\*\*\*\*\*\*\*

Original Patient Name: PATIENT,ONE

EOB Type: NORMAL EOB EOB Paid Date: OCT 06, 2007

Svc From Date: 05/24/07 Svc to Date:

ICN: 7272118305

Payer Name/TIN: GWH-CIGNA/1840467907

ERA \#: 18024 Auto-Post Status:

Trace \#: 0044912703

ECME \#: DOS: Rx/Fill/Release Status:

--------------------------------------------------------------------------------

CLAIM LEVEL PAY STATUS:

Total Submitted Charges : 67.27 Payer Covered Amount : 0.00

The example below shows the EEOB move/copy history

EDI LOCKBOX EEOB DETAIL FROM WORKLIST 2/6/17 Page: 2

ERA NUMBER: 147 ERA DATE: Feb 06, 2017

INS COMPANY: TJB INSURANCE CO./xxxxxxxxx

ERA TRACE \#: xxxxxxxxxxxxxxx

Payer Name : EPHARM INSURANCE

Payer Id : xxxxxxxxxxx

ICN : xxxxxxxxxxx

MOVE/COPY HISTORY

Date/Time of EEOB Copy: FEB 03, 2017@10:27:18

Copy of EEOB performed by: EMPLOYEE,ONE

Copy Justification Comments:

JUSTIFICATION

Other Claims: K50000E

\*\*A/R CORRECTED PAYMENT DATA:

TOTAL AMT PD: 1200.00

\[suspense\]NO BILL 1000.00

xxx-K500009 200.00

#### Review Line 

This worklist action is used to enter comments for an EEOB or as a bookmark when an EEOB was last worked on, so that the process be more easily resumed after an interruption. This option now remains active for the user, even if he/she leaves the worklist. Additionally, each user comment that has been entered is identified by the user and the date/time that it was entered or edited. This will allow the user to edit his/her own comments. Individual user preference determines whether this option is consistently on or off.

Select Action: Next Screen// re  
     1   Refresh Scratch Pad  
     2   Research Menu  
     3   Review Line  
CHOOSE 1-3: 3   Review Line 

 

REVIEW DATA DISPLAY IS CURRENTLY TURNED ON  
DO YOU WANT TO TURN IT OFF?: NO//

 

Select EEOB Line:  (1-2): 1

 

REVIEW DATE/TIME: <8/12/04@13:13:18>  
COMMENT:  
  1\>this is a test  
  2\>  
EDIT Option:  
REVIEWED?: y  YES

#### #### Verify

The system has been enhanced to automatically mark EEOBs as verified based on the first five digits of the patient’s last name, the patient’s last four of their social security number, the claim number, the original bill amount, and the date of service. If all the criteria matches in the EEOB and in the AR package, the system will place a (V) next to the EEOB to indicate that all the criteria was automatically verified. For non auto-post ERAs, where the system indicator has not been automatically updated, this worklist action is manually used to mark EEOBs as verified. In addition, for both auto-post and non auto-post ERAs, the user can display/print the list of bills that were not automatically verified or contain discrepancies between the EEOB and the bill record in VistA. The report will include data from the original bill (i.e. patient full name, date of service, last 4 digits of patient’s SSN, billed amount, and bill number) as well as data from the EEOB (i.e. patient full name, date of service, billed amount and bill number). Note that all the data shown on the worklist for the EEOB is taken from the claim in VistA. You must use the report below to identify the discrepancies for unverified EEOBs. This action requires the RCDPEPP security key.

<u>Autopost ERA Lines Discrepancy Report</u>

EDI LBOX WORKLIST - AUTOPOST ERA LINES DISCREPANCIES REPORT 3/30/18 Page: 1

ERA \#: 92599 TRACE \#: ABC6467843571

PAYER: AETNA ERA DT: 2/1/18

PATIENT NAME SUBMITTED AMT SVC DATE(S)

\* preceding data = data has discrepancy

================================================================================

EEOB Sequence \#(s) on the ERA:1 K1000000 Unverified

VistA:\*Last, First Middle 186.66 7/10/00 – 7/10/00

ERA:\*Last, First Middle 186.66 7/10/00 – 7/10/00

Figure 8 - Sample of Autopost ERA Lines Discrepancies Report Output

### ### Change View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action is used to customize the information displayed on the ERA worklist scratchpad. After answering the questions, the system gives the user the option to “SAVE” the selections as a “preferred view”. If the user saves a preferred view they will be prompted if they want to use that view in the future.

The answers are used to filter the scratchpad display to limit the entries that are included.

The following options are available as filters.

Select Action: Quit// c Change View

ORDER OF PAYMENT: N// O ORDER

DISPLAY FOR AUTO-POSTED ERAS: (U)NPOSTED EEOBs, (P)OSTED EEOBs, OR (A)LL: U// NP

OSTED

DO YOU WANT TO SAVE THIS AS YOUR PREFERRED VIEW (Y/N)? NO/

> Order of Payment:

- N NO ORDER – Does not list payments with respect to zero-payments
- F ZERO-PAYMENTS FIRST – Display all zero-payments first
- L ZERO-PAYMENTS LAST – Display all zero-payments last

> Auto-Posting Qualification

- U UNPOSTED – Only display unposted EEOBs
- P POSTED – Only display posted EEOBs
- A ALL – Display all EEOBS, both posted and unposted

### Research Menu Actions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Research Menu provides access to functionality necessary to process ERAs. It can be accessed from the ERA Worklist/Scratch Pad to facilitate business process. Links to the following existing AR functions are available.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Action</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Full Account Profile</td>
<td>This option will display a full account profile of all bills for a debtor regardless of the status of the bill.</td>
</tr>
<tr class="odd">
<td>TPJI</td>
<td>Comment History will display contact information if provided</td>
</tr>
<tr class="even">
<td>Bill Comment Log</td>
<td>Allows user to document any necessary and pertinent information on a 3<sup>rd</sup> party bill.</td>
</tr>
<tr class="odd">
<td>Re-establish Bill</td>
<td><p>Provides the capability to re-establish a bill for the specific site.</p>
<p>This is locked with the security key “RCDPEAR”.</p></td>
</tr>
<tr class="even">
<td>View/Print EEOB</td>
<td>Used to display/print the detail received on the ERA for a selected line.</td>
</tr>
<tr class="odd">
<td>Review Line</td>
<td>Bookmarks a specific line within an ERA in case processing was interrupted, thereby allowing the user to more easily resume where he/she left off.</td>
</tr>
</tbody>
</table>

#### Comment History Screen of TPJI

The Comments History screen of the Third Party Joint Inquiry option displays contact data which will include payer name and can include phone number, fax number, email address, and website address. Contact data that comes in from an ERA or MRA transaction will be distinguishable from manually entered comments by use of the program generated text, “ERA Payer Contact Information”. Refer to example below:

Comment History Jul 07, 2011@18:27:38 Page: 1 of 1

K700CM9 CAGGIANO,GARTH JR C1547 DOB: 04/29/39 Subsc ID: 520372456

AR Status: COLLECTED/CLOSED Orig Amt: 4.49 Balance Due: 0.00

3551940 01/17/07 2A FOLLOW-UP DT:

3649412 07/07/11 ERA Payer Contact Information FOLLOW-UP DT:

Payer Name: UNITEDHEALTHCARE

Contact Name: TEST PAYER 1

Phone Number: 800-909-1212

Payer Name: MEDICARE (WNR)

Contact Name: MEDICARE TEST PAYER

Phone Number: 888-998-1212

Email Address: EMAIL1@YAHOO.COM

Enter ?? for more actions

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis AD Add Comment VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit

Select Action: Quit//

The Trace number and ERA number will display on the Bill Charges screen of TPJI for non-MRA ERAs. Refer to example below:

<u>Bill Charges Nov 27, 2011@20:47:24 Page: 1 of 2</u>

%K4004JU PATIENT1,ELI R Z9854 DOB: 12/08/44 Subsc ID: SUBSC ID 587893

03/11/02 - 03/11/02 ADMIT THRU DISCHARGE Orig Amt: 177.72

G2 830148494

03 11 02 03 11 02 22 99213 123 17772 1 1790708568

\>\> EOB/MRA Information (1 OF 1)

EOB Type: NORMAL EOB

ICN: EP253MC4S0000 Patient Resp Amount: 128.92

Payer Name: AETNA US HEALTHCARE Total Allowed Amount: 0.00

EOB Date: Jan 07, 2004 Total Submitted Charges: 177.72

Svc From Dt: Svc To Dt:

Reported Payment Amt: 48.80

ERA \#: 12 Auto-Post Status: Partial

Trace \#: 804001620000025

\+ \|% EEOB \| Enter ?? for more actions\|

PR Bill Procedures CM Comment History AB Annual Benefits

CI Go to Claim Screen IR Insurance Reviews EL Patient Eligibility

HS Health Summary EX Exit

ED EDI Status AL Go to Active List

VI Insurance Company

Select Action: Next Screen//

### Example of processing a Paper Check and ERA 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAMC received a paper check from IBinsurance Company One, a payer who sends Electronic Remittance Advices (ERAs). Begin by selecting the ERA Worklist option.

Select EDI Lockbox (ePayments) Option: WL ERA Worklist

SELECT PARAMETERS FOR SELECTING AN ERA

ERA POSTING STATUS: UNPOSTED//

ERA-EFT MATCH STATUS: BOTH// NOT MATCHED

LIMIT THE SELECTION TO A DATE RANGE WHEN THE ERA WAS RECEIVED?: NO//

Select ELECTRONIC REMITTANCE ADVICE ENTRY: 55555-55555555 6 55555-55555555 03-06-03 509.61 IBinsurance Company One UNMATCHED

The paper check (55555-55555555) matches the ERA Trace \# and the check amount received from the Payer.

No Worklist currently exists for this ERA. Create one now.

NO WORKLIST SCRATCH PAD ENTRY EXISTS FOR THIS ERA

DO YOU WANT TO CREATE ONE NOW?: NO// YES

NO PAYMENT METHOD CODE REPORTED

THIS ERA DOES NOT HAVE A MATCHING EFT

ENTER THE NUMBER OF THE PAPER CHECK YOU RECEIVED FOR THIS ERA: 55555-55555555// \<RET\>

DATE OF CHECK: 3/6/03// \<RET\> (MAR 06, 2003)

CHECK BANK/ROUTING \#: 123456 IBinsurance Company One

ERA \#6 (TRACE \#:55555-55555555) MATCHED TO PAPER CHECK 55555-55555555

IS THIS CORRECT?: YES// \<RET\>

ORDER OF PAYMENTS: NO ORDER// L ZERO-PAYMENTS LAST

Verify the paper check number is correct. The date on the check should match the date listed in VistA. If it does not match, correct the VistA date to match the paper check. Enter the Check Bank/ Routing number as station policy dictates. Again, verify the information is correct. Select the order of the Payments. In this case, select L to sort the zero payment EEOBs to the bottom of the Worklist.

ERA Worklist/Scratch Pad Sep 11, 2010@13:24:20 Page: 1 of 2

ERA Entry \#: 5 Total Amt Pd: 509.61 Current View:

Payer Name/ID: IBinsurance Company One/5555555555 NO SORT ORDER

PAPER CHECK \#: 55555-55555555 ALL EEOBs

1 EEOB Seq \# On ERA: 3 Net Payment Amt: 509.61

1.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/1234

Claim Bal: 559.61 Billed Amt: 559.61 Amt To Post: 509.61

Svc Dt: 2/4/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: NO

Payment Amt: 509.61 Total Adjustments: 0.00 Net: 509.61

...........................................................................

2 EEOB Seq \# On ERA: 1 Net Payment Amt: 0.00

2.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/1234

Claim Bal: 0.00 Billed Amt: 19.47 Amt To Post: 0.00

Svc Dt: 1/27/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: ??

Payment Amt: 0.00 Total Adjustments: 0.00 Net: 0.00

...........................................................................

\+ Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

View/Print EEOB Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Next Screen// EOB View/Print EEOB

#### Process EEOB Line Items 

- In order to process line item \#1, select the Research Menu action to access Third Party Joint Inquiry (TPJI) to confirm this payment is correct for this claim.
- The IB application is enhanced to display the Trace Number and ERA Number on the TPJI screen when viewing the EEOB.

Select Action: Next Screen// BC Bill Charges

DO YOU WANT ALL EEOB DETAILS?: NO// YES

\>\> EOB/MRA Information (1 OF 1)

EOB Type: NORMAL EOB

ICN: XXXXXXXXXXXX Patient Resp Amount: 50.00

Payer Name: IBinsurance Company One Total Allowed Amount: 0.00

EOB Date: Mar 06, 2003 Total Submitted Charges: 559.61

Reported Payment Amt: 509.61

.

.

.

Bill \#: XXX-KXXXXXX

Adjustment Group Code: PR

Adjustment Reason Code: 3

Adjustment Amount: 50.00

Quantity: 0

Reason Code Text: Co-payment Amount

The user can view the EEOB details without going back to the worklist by selecting Bill Charges (BC) from within TPJI to view the EEOB Details for this claim. Scrolling down to the bottom of the EEOB information shows the Payer adjusted this payment by \$50.00 for the patient’s insurance co-payment amount.

#### Create Receipt 

After all of the EEOB lines have been reviewed, verified as correct and adjusted appropriately, it is time to create the receipt for these payments. Select Look at Receipt from the ERA Worklist/Scratch Pad screen.

<u>ERA WORKLIST PREVIEW RECEIPT Oct 07, 2003@15:09:36 Page: 1 of 1</u>

ERA Entry \#: 6 Total Amt Pd: 509.61

Payer Name/ID: IBinsurance Company One/5555555555

PAPER CHECK \#: 55555-55555555

<u>LINE \# ACCOUNT AMOUNT .</u>

PAYMENTS (LINES FOR RECEIPT):

2.001 XXX-KXXXXXX 509.61

ZERO DOLLAR PAYMENTS:

1.001 XXX-KXXXXXX 0.00

3.001 XXX-KXXXXXX 0.00

Enter ?? for more actions………………………………………………………………………………………………………….

Print Receipt Preview Create Receipt Exit

Select Action: Quit//

The preview screen is divided into two sections. The top contains the line items and payment information. The bottom section lists all of the zero-dollar payments. Zero-dollar payments can be worked using AR options in the research menu from within the Worklist.

The Create Receipt action will create the receipt for lines on the ERA that contain payments and those lines used to offset any negative payments on this ERA. The ERA Worklist can no longer be used to adjust any of the line items once the receipt is created.

THIS ACTION WILL CREATE THE RECEIPT FOR THIS ERA. ONCE THE RECEIPT IS

CREATED HERE, NO MORE AUTOMATIC ADJUSTMENTS MAY BE MADE FOR THIS ERA.

ARE YOU SURE YOU ARE READY TO CREATE THIS RECEIPT?: NO// YES

Select AR DEPOSIT TICKET \#: 123456 03-10-03 IBpatient,One A

\$0.00 OPEN

ARE YOU SURE YOU WANT TO USE THIS DEPOSIT?: NO// YES

RECEIPT EXXXXXXXX HAS BEEN CREATED FOR THIS ERA

DO YOU WANT TO GO TO RECEIPT PROCESSING NOW? YES// \<RET\>

Processing receipts for paper checks require the entry of an AR Deposit Ticket \#. Contact the Agent Cashier for this number. The system will automatically generate a receipt number for this payment. All 3<sup>rd</sup> Party EDI Lockbox receipts will begin with the letter ‘E’. It is important to note that every ERA is assigned its own receipt number. If four ERAs are processed on a given day, then there will be four ‘E’ receipts – one for each ERA. The system assigns the electronic receipt number based on the date and the last two digits are a combination of numbers or letters. In the example below, the receipt was created on October 7, 2003 and was the first batch created for that day (00).

Receipt Profile Oct 07, 2003@15:14:52 Page: 1 of 1

Receipt \#: EXXXXXXXX Type of Payment: CHECK/MO PAYMENT

Deposit \#: XXXXXX ERA \#: 6 Receipt Status: OPEN

ERA \#: xxxxxxxxxx ERA TTL: xxxxxx.xx FMS Document: NOT SENT

EFT \#: xxxxxxxxxx EFT TTL: xxxxxx.xx FMS Doc Status: NOT ENTERED

\# Account Pay Date By Pay Amt Proc Amt

1 XXX-KXXXXXX 10/07/03 EG 509.61 0.00

-------- --------

TOTAL DOLLARS FOR RECEIPT 509.61 0.00

Receipt History

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

The Receipt Profile screen is the same screen used when the option Receipt Processing is selected. All of the payment line items automatically transfer to this screen. No additional data entry is required to input these claim numbers and payment amounts. Process this receipt as normal to complete processing a Paper Check and ERA. The following condition must be met before the receipt can be fully processed to FMS:

> The total on the receipt must be equal to the total reported on the ERA.

> When the above condition is met, select the PROCESS RECEIPT action. The system will:

1)  Generate the decrease adjustment for any distributed adjustments made to the payments on the Worklist AND add any related bill comments to the Bill record in AR.
2)  If the receipt passes the normal edits for posting, the system will post payments to your AR and then generate and transmit the appropriate CR document to FMS for these payments.

### Example of processing a matched ERA and EFT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAMC received an Electronic Funds Transfer (EFT) from IBinsurance Company One, a payer who sends both EFTS and ERAs. Begin by selecting the ERA Worklist option.

Select EDI Lockbox (ePayments) Option: WL ERA Worklist

DO YOU WANT A (L)IST OF ERAs OR A (S)PECIFIC ONE?: LIST//

LIMIT THE SELECTION TO A DATE RANGE WHEN THE ERA WAS RECEIVED?: NO//

The EFT payment was automatically matched with the ERA during the AR nightly job. The user can select a specific payer by selecting Range or can view all payers by selecting All. All is the default selection.

Select ELECTRONIC REMITTANCE ADVICE ENTRY: 25 55555-55555555 03-10-03 79.55 IBinsurance Company One MATCHED

NO WORKLIST SCRATCH PAD ENTRY EXISTS FOR THIS ERA

(C)reate scratchpad, (V)iew ERA details or (E)xit:

NO PAYMENT METHOD CODE REPORTED

ORDER OF PAYMENTS: NO ORDER//

In this example the user selected ERA \#25 after viewing the worklist. The EFT Trace \# 55555-55555555 was received from the Payer. Note that no check information is required. The EFT payment was already deposited into US Treasury, account MCCR RSC 528704/8NZZ for the VA.

If no scratchpad entry currently exists for this ERA, create one now.

<u>ERA Worklist/Scratch Pad Oct 07, 2003@15:52:17 Page: 1 of 2</u>

ERA Entry \#: 25 Total Amt Pd: 79.55 Current View:

Payer Name/ID: IBinsurance Company One/5555555555 NO SORT ORDER

EFT \#/TRACE \#: 3/55555-55555555 ALL EEOBs

<u>.</u>

1 EEOB Seq \# On ERA: 1 Net Payment Amt: 47.26

1.001 Claim \#: KXXXXXX Patient/Last 4:IBpatient,One/0000

Claim Bal: 236.31 Billed Amt: 236.31 Amt To Post: 47.26

Svc Dt: 1/15/03 COB: NO Rx Copay: NON-EXEMPT Means Tst: NO

Payment Amt: 47.26 Total Adjustments: 0.00 Net: 47.26

...........................................................................

2 EEOB Seq \# On ERA: 2 Net Payment Amt: 32.29

2.001 Claim \#: KXXXXXX Patient/Last 4: IBpatient,One/0000

Claim Bal: 161.46 Billed Amt: 161.46 Amt To Post: 32.29

Svc Dt: 7/26/02 COB: NO Rx Copay: NON-EXEMPT Means Tst: NO

Payment Amt: 32.29 Total Adjustments: 0.00 Net: 32.29

...........................................................................

Enter ?? for more actions

Split/Edit A Line Look At Receipt Mark for Auto Post

View/Print EEOB Review Line ERA View/Print ERA

Refresh Scratch Pad Verify RP Receipt Processing

Research Menu Change View EXIT

Select Action: Quit//

The header of the ERA Worklist/Scratch Pad screen shows the EFT \#/Trace \# instead of the number from the paper check.

Processing of an EFT/ERA is no different than processing an ERA and Paper Check. Perform the necessary reviews and processing for each claim.

#### Create Receipt 

After all of the EEOB lines have been reviewed and processed, it is time to create the receipt for these payments. Select Look AT Receipt from the ERA Worklist/Scratch Pad screen.

<u>ERA WORKLIST PREVIEW RECEIPT Oct 07, 2003@16:20:17 Page: 1 of 1</u>

ERA Entry \#: 25 Total Amt Pd: 79.55

EFT \#/TRACE \#: 3/55555-55555555

Payer Name/ID: IBinsurance Company One/5555555555

<u>LINE \# ACCOUNT AMOUNT .</u>

PAYMENTS (LINES FOR RECEIPT):

1.001 XXX-KXXXXXX 47.26

2.001 XXX-KXXXXXX 32.29

ZERO DOLLAR PAYMENTS:

3.001 XXX-KXXXXXX 0.00

Enter ?? for more actions

Print Receipt Preview Create Receipt Exit

Select Action: Quit//

The ‘look at’ screen is divided into two sections. The top contains the line items and payment information. The bottom section lists all of the zero-dollar payments. Zero-dollar payments can be “worked” using AR options or from within the Worklist.

The Create Receipt action will create the receipt for the lines on the ERA that contain payments and those lines used to distribute negative payments on this ERA. The ERA Worklist can no longer be used to adjust any of the line items once the receipt is created.

THIS ACTION WILL CREATE THE RECEIPT FOR THIS ERA. ONCE THE RECEIPT IS

CREATED HERE, NO MORE AUTOMATIC ADJUSTMENTS MAY BE MADE FOR THIS ERA.

ARE YOU SURE YOU ARE READY TO CREATE THIS RECEIPT?: NO// YES

RECEIPT E03100701 HAS BEEN CREATED FOR THIS ERA

DO YOU WANT TO GO TO RECEIPT PROCESSING NOW? YES//

Processing receipts for EFTs does not require or allow the entry of an AR Deposit Ticket \#. Remember, The EFT payment was already deposited into US Treasury for the VA. As with the receipt for a paper check, the system will automatically generate a receipt number for this payment. All 3rd Party EDI Lockbox receipts will begin with the letter ‘E’. It is important to note that every ERA is assigned its own receipt number. If four ERAs are processed on a given day, then there will be four ‘E’ receipts – one for each ERA.

ER Edit Receipt

Receipt Profile Oct 07, 2003@16:24:41 Page: 1 of 1

Receipt \#: E03100701 Type of Payment: EDI LOCKBOXEFT Detail \#: 3 VETERAN ERA \#: 25 Receipt Status: OPEN

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

Enter ?? for more actions………………………………………………………………………………………………………….

NP New Payment AP Account Profile PR Process Receipt

EP Edit Payment RR Reprint Receipt 21 (215 Report)

CP Cancel Payment WL Worklist (ERA) EA Exit Action

MP Move Payment CU Customize CR Entered Online

ER Edit Receipt

Select Action: Quit// QUIT

The Receipt Profile screen is the same screen as you would see for Receipt Processing. Instead of a Deposit Ticket \#, the EFT Detail and ERA \# will display. The Type of Payment indicates EDI LOCKBOX. All of the payment line items automatically transfer to this screen. No additional data entry is required to input these claim numbers and payment amounts. Process the receipt as normal. The following conditions must be met before the receipt can be fully processed to FMS:

1.  An ERA receipt cannot be processed if the EFT receipt for the EFT related to this ERA has not yet been recorded in FMS and confirmed as ACCEPTED in VistA. Wait until the FMS document for the EFT deposit has reached this status in VistA before processing the ERA related to the EFT.
2.  If there is an error on the EFT where the checksum was determined to be invalid, the receipt cannot be processed until the EDI Lockbox checksum exception is cleared on the EFT transmission
3.  If the total of the receipt is not the same as the total reported on the EFT, the receipt cannot be processed.
4.  A receipt for an ERA related to an EFT cannot have a deposit associated with it.

When the above conditions have been met, and you select PROCESS RECEIPT, the system will:

1.  Generate the decrease adjustments for any distributed adjustments made to the payments in the Worklist and add any related bill comments to the bills.
2.  If the receipt passes the normal edits for posting, it will post the payments to your A/R and will generate and transmit the appropriate TR document to FMS for EFT payments. The TR documents will transfer the payment amounts from the Fund 528704, Revenue Source Code 8NZZ account (where it was placed by the CR generated when the EFT was recorded) into the correct General Ledger accounts for the claims on the ERA. A CR document is created and recorded in FMS for receipts that are processed using a paper check.

#### How to Process an EFT using a Paper EOB (when the ERA is not received)

It is important to process an EFT even if the ERA is unavailable. By processing the EFT, the funds are appropriately transferred to the appropriate revenue source codes and the third party payments are applied to the proper outstanding accounts receivables.

Create a receipt using the receipt number of the EFT. A letter or number will need to be added to the end of the receipt. This process will create a good audit trail of the EFT. The EFT receipt number can be located by accessing the EFT Daily Activity Report (see Reports section).

Enter EDI LOCKBOX for the receipt payment type.

Select the corresponding EFT. (To see a complete listing of EFTs, enter ‘??’)

Do not enter a deposit ticket. The Funds have already been deposited into the appropriate fund.

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/004.png)

Manually enter each payment.

Complete the receipt processing function according to local policy.

\*NOTE – The EFT will be removed from the EFT Unmatched Aging Report with this process; however, the Unapplied EFT Deposits Report will still display this EFT. (A future enhancement will correct this issue)

## Auto-Posting Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA runs a nightly job to automatically post third party medical claims by creating and processing receipts. The system attempts to create and process receipts for claims that are candidates for auto-posting based on auto posting parameters.

### Medical Auto-Posting Candidates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A third party medical claim is a candidate for auto-posting if the following conditions are met:

- Auto-posting is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\]
- The EEOB payer is not excluded from auto-posting in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\]
- The ERA does not have an exception
- The ERA does not contain interest
- The ERA does not contain an adjustment
- The EFT and ERA are matched
- The ERA total amount equals the sum of all EEOBs listed on the ERA
- The EFT and ERA total amounts must balance
- The EFT has been accepted by FMS
- The ERA negative payments all have a matching positive payment (+/- pairs)

### Medical Auto-Posting Create and Process Receipt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the nightly job runs, a receipt is created and processed if the following conditions are met:

- The EEOB detail has been verified against the bill detail
- The claim balance covers the payment to be posted for all EEOBs
- The claim status is open for all EEOBs
- The claim has not been referred to regional council or general council

If all auto-posting conditions to create and process a receipt are not met for an EEOB, the system sends that EEOB to the Auto-Posting Awaiting Resolution list. Once a user corrects the condition that prevented receipt processing, the EEOB can be reprocessed by the next nightly job. For more details, refer to the section on Auto-Posting Awaiting Resolution.

The claim has not been terminated as a write off, indicated by a “WO” claim status

### Medical Auto-Posting Receipts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system creates a receipt for all EEOBs that can be auto-posted, even if all EEOBs in an ERA cannot be posted at the same time.

The following examples illustrate possible auto-posting situations.

1.  Example of a Partially Posted ERA

> Scenario:

> The ERA contains a hundred EEOBs and the ERA is an auto-posting candidate.

> Seventy of the EEOBs meet the conditions to create and process a receipt.

> The nightly auto-posting job runs.

> Auto-Posting Day \#1:

> A receipt is created and processed for seventy EEOBs. The receipt number is E14101306A.

> Thirty EEOBs do not have a receipt and the EEOBs are on the Auto-Posting Awaiting Resolution list.

> The ERA is partially posted.

> Note: The receipt number contains an alphabetic character at the end.

> Auto-Posting Day \#2:

> A user resolved the issues on twenty of the EEOBs.

> The nightly auto-posting job runs.

> A receipt is created and processed for twenty EEOBs. The receipt number is E14101306B.

> Ten EEOBs do not have a receipt and the EEOBs are on the Auto-Posting Awaiting Resolution list.

> The ERA is partially posted.

> Note: The receipt number contains an alphabetic character at the end, incrementing to the next letter of the alphabet.

> Auto-Posting Day \#3:

> A user resolved the issues on the remaining ten EEOBs.

> The nightly auto-posting job runs.

> A receipt is created and processed for ten EEOBs. The receipt number is E1410306C.

> The ERA is completely posted.

> None of the EEOBs for this ERA are on the Auto-Posting Awaiting Resolution list.

> Note: The receipt number contains an alphabetic character at the end, incrementing to the next letter of the alphabet.

2.  Example of a Completely posted ERAThe ERA is partially posted.The ERA is partially posted.

> Scenario:

> The ERA contains a hundred EEOBs and the ERA is an auto-posting candidate.

> All of the EEOBs meet the conditions to create and process a receipt.

> The nightly auto-posting job runs.

> Auto-Posting Day \#1:

> A receipt is created and processed for all EEOBs. The receipt number is E14101305.

> The ERA is completely posted.

> None of the EEOBs for this ERA are on the Auto-Posting Awaiting Resolution list.

> Note: The receipt number does not contain an alphabetic character at the end.

Pharmacy Auto Posting Candidates:

The system auto-posts for pharmacy claims when the following conditions are met:

- Auto-posting for pharmacy claims is enabled in the EDI LOCKBOX PARAMETERS
- The EEOB payer is not excluded from pharmacy auto-posting in the EDI LOCKBOX PARAMETERS
- The Electronic Remittance Advice (ERA) does not have an exception
- The ERA does not contain interest
- The ERA does not contain an ERA level adjustment
- The EFT and ERA are matched
- The EFT has been accepted by Financial Management System (FMS)
- The ERA negative payments all have a matching positive payment (+/- pairs)

Pharmacy Auto Posting Create and Process ReceiptWhen the nightly job runs, a receipt is created and processed if the following conditions are met:

- The EEOB detail has been verified against the bill detail
- The claim balance covers the payment to be posted for all EEOBs
- The claim status is open for all EEOBs
- The claim has not been referred to regional council or general council

If all auto-posting conditions to create and process a receipt are not met for an EEOB, the system sends that EEOB to the Auto-Posting Awaiting Resolution list. Once a user corrects the condition that prevented receipt processing, the EEOB can be reprocessed by the next nightly job. For more details, refer to the section on Auto-Posting Awaiting Resolution.

### Pharmacy Auto Posting Receipts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system creates a receipt for all EEOBs that can be auto-posted, even if all EEOBs in an ERA cannot be posted at the same time.

If all EEOBs in an ERA can be posted, the receipt number will contain “E” followed by numeric characters.

If only some of the EEOBs in an ERA can be posted, the receipt number will have an alphabetic character on the end, starting with “A” and proceeding in order until all EEOBs have been posted. The base number stays the same.

> 1. Example of Completed Posted Pharmacy ERA Scenario:

> The ERA contains ten EEOBs and the ERA is an auto posting candidate. All of the EEOBs meet the conditions to create and process a receipt.

> The nightly auto-posting job runs.

Auto-Posting Day \#1:

> A receipt is created and processed for all EEOBs. The receipt number is E14101308.

> The ERA is completely posted.

> None of the EEOBs for this ERA are on the Auto-Posting Awaiting Resolution list.

> Note: The receipt number does not contain an alphabetic character at the end.

1.  Example of a Partially Posted ERA

> Scenario:

> The ERA contains a ten EEOBs and the ERA is an auto-posting candidate.

> Seven of the EEOBs meet the conditions to create and process a receipt.

> The nightly auto-posting job runs.

> Auto-Posting Day \#1:

> A receipt is created and processed for seventy EEOBs. The receipt number is E14101309A.

> Three EEOBs do not have a receipt and the EEOBs are on the Auto-Posting Awaiting Resolution list.

> The ERA is partially posted.

> Note: The receipt number contains an alphabetic character at the end.

> Auto-Posting Day \#2:

> A user resolved the issues on two of the EEOBs.

> The nightly auto-posting job runs.

> A receipt is created and processed for twenty EEOBs. The receipt number is E14101309B.

> One EEOB does not have a receipt and the EEOBs are on the Auto-Posting Awaiting Resolution list.

> The ERA is partially posted.

> Note: The receipt number contains an alphabetic character at the end, incrementing to the next letter of the alphabet.

> Auto-Posting Day \#3:

> A user resolved the issues on the remaining one EEOB.

> The nightly auto-posting job runs.

> A receipt is created and processed for one EEOB. The receipt number is E1410309C.

> The ERA is completely posted.

> None of the EEOBs for this ERA are on the Auto-Posting Awaiting Resolution list.

> Note: The receipt number contains an alphabetic character at the end, incrementing to the next letter of the alphabet.

### EEOB Worklist 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB WORKLIST option displays an "A" indicator before the ERA number if auto-posting is complete for that ERA. The indicator is displayed for both medical and pharmacy auto posted ERAs.

\# ERA \# TRACE#

<u>PAYER NAME/MATCH STATUS ERA PAID DT TOT AMT PAID DT REC'D</u>

1 A4667 000032974

3/31/05 7.46 3/31/05

THE COMMUNITY HOSPITAL APPROX \# EEOBs: 1

### Ignore Payment Retraction Pairs 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system ignores payment retraction pairs for medical and pharmacy claims when the following conditions are met, without regard to case sensitivity:

- Payment/Retraction pair is in the same ERA
- The first 5 characters of the patient's last names match
- The dates of service match
- The bill numbers or claim numbers match
- The social security numbers or patient IDs match
- The amounts billed sum to zero, such as +5 and -5

### Status Change 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system makes the following status changes when a medical or pharmacy claim is successfully auto-posted:

- Claim Status – Collected/Closed or Open (with residual balance)
- Receipt Status – Closed
- Detail Post Status – Posted, Not Posted or Partial

> **NOTE:** Detail Post Status becomes Posted when all lines have been posted. Detail Post Status becomes Partial if some lines have been posted but not all.

### AR Display 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system displays the auto-posted transactions within Accounts Receivable in the same manner as a manually posted transaction. Specifically, Auto-Posted payments display on the TPJI – AR Account Profile and VT Transaction Profile screens.

## Working the APAR List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Auto-Posting Awaiting Resolution list displays EEOB detail records that require user intervention before the nightly auto-posting job can post. The APAR screen contains the actions that enable research, resolution and the ability to mark the EEOB for auto-posting. Once an entry is marked for auto-post, the entry is removed from the APAR display.

Once the APAR option has been selected, the initial list of EEOBs are presented.

| Field | Description                                                                                                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERA \#:   | The number that the VistA system has assigned to designate an ERA. It is shown on the ERA List – Worklist), after accessing the WL Worklist menu option. Each ERA is in numerical order as it is accepted into Vista. |
| Claim \#: | Claim used to bill the insurance company                                                                                                                                                                              |
| Posted    | The total amount posted to the claim                                                                                                                                                                                  |
| Post Dt   | The date the amount was posted                                                                                                                                                                                        |
| Unposted  | The balance remaining                                                                                                                                                                                                 |

Use preferred view N// O

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: A// LL

(M)EDICAL, (P)HARMACY, or (B)OTH: BOTH//

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

1 43416.1 K100000 0.00 1/23/17 2169.44

AETNA/10XXXXXXXX

CLAIM ALREADY COMPLETED/CLOSED

2 43417.1 K100001 0.00 1/23/17 594.33

AETNA/10XXXXXXXX

3 43419.1 K100002 0.00 1/23/17 487.76

CIGNA BEHAVIORAL HEALTH, INC./10XXXXXXXX

### APAR - Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of list manager options available on the APAR screen that provides greater capability to manage EEOB records.

|                |                                                               |
|----------------|---------------------------------------------------------------|
| Select EEOB    | Used to select a specific EEOB.                               |
| View/Print ERA | Used to display/print the summary ERA information.            |
| Change View    | Used to customize the information displayed on the APAR list. |

#### View/Print ERA

The View/Print ERA action is used to display and print the summary ERA information.

#### Change View

The Change View action is used to customize the information displayed on the APAR list. After answering the question, the system gives the user the option to “SAVE” the selection as a “preferred view”. The answer is used to filter the display to limit the entries that are included.

If the user saves a preferred view they will be prompted if they want to use that view in the future.

The following option is available as a filter.

Select Action: Next Screen// C Change View

(M)EDICAL, (P)HARMACY, OR (B)OTH: BOTH//

(A)LL PAYERS, (R)ANGE OF PAYER NAMES: A//

DO YOU WANT TO SAVE THIS AS YOUR PREFERRED VIEW (Y/N)? NO//

Payer Range Selection:

ALL

RANGE

The screen header will indicate the Current View selected as follows:

<u>AUTO-POST - AWAIT RESOLUTION Nov 19, 2013@21:37:21 Page: 1 of 2</u>

Current View: MEDICAL + PHARMACY CLAIMS for ALL PAYERS

ERA#.Seq Claim# Posted Amt Post Date Un-posted Bal

<u>\_\_\_\_ \_Payer Name/ID\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>1 87705.1 K307YUC 3000.41 11/1/13 127.44

ANTHEM BCBS OF WISCONSIN/139XX38065

2 87705.2 K307740 3000.41 11/1/13 127.44

ANTHEM BCBS OF WISCONSIN/139XX38065

          Enter ?? for more actions                                            

    Select EEOB               View/Print ERA

    Change View               Exit

Select Action: Next Screen//

#### Select EEOB

The Select EEOB action allows the user to select a specific EEOB by number. After selection, the APAR scratchpad is displayed.

APAR - EEOB ITEM - SCRATCHPAD Jul 21, 2014@15:34:59 Page: 1 of 1

ERA Entry \#: 5177 Total Amt Pd: 50.00

Posted Amt: 0.00 Unposted balance: 50.00

Payer Name/ID: ONE INSURANCE COMPANY/11111111

EFT \#/TRACE \#: 177/1234123456

Posted Receipt \#(s):

EEOB: ERA Seq \# 1 Net Payment Amt: 50.00

1.001 Claim \#: K4000FM Patient/Last 4: PATIENT,ONE/1234

Claim Bal: 51051.58 Billed Amt: 51051.58 Amt To Post: 50.00

Svc Dt: 4/23/14 COB: NO Rx Copay: UNKNOWN Means Tst: ??

Payment Amt: 50.00 Total Adjustments: 0.00 Net: 50.00

APAR Reason: FIELD VERIFICATION FAILED

..............................................................................

Enter ?? for more actions

Split/Edit a Line EOB View/Print EEOB Review Line

Mark for Auto Post ERA View/Print ERA Verify

Claim Comment Research Menu EXIT

Select Action: Quit//

The header of the APAR Scratchpad screen contains the ERA Entry \#; the Total Amount being Paid on the ERA (this will equal the dollar amount of the Electronic Funds Transfer ); the Posted Amount; the Unposted balance; the Name and ID number of the Payer; the EFT Trace \#; and the base number for the Posted Receipt(s) numbers.

Each EEOB line item equates to a line item on a paper EOB form. HIPAA mandates standardization of the electronic transmissions.

| Field               | Description                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EEOB Seq \# on ERA:     | This shows the line item order as the payer sent it. Remember, the Worklist can be sorted with Zero Payments First or Zero Payments Last, so the sequence number may not match the line item list on the far left of the screen.                                                                                                                                                                  |
| Net Payment Amt:        | The payment amount plus or minus the adjustment amount will equal the net payment amount for this claim number.                                                                                                                                                                                                                                                                                   |
| Claim \#:               | The claim number associated with this payment. This may or may not be the correct claim number. Research each claim carefully verify if the amount being paid is appropriate for the claim in AR. If the line item is marked (V), the system has already done a verification match between bill number and the patient name, last four of the social, date of service and original billed amount. |
| Patient/Last 4:         | The patient’s name and last four digits from their SSN. Used to help identify this payment is for the correct Claim.                                                                                                                                                                                                                                                                              |
| Claim Balance:          | Current balance from AR.                                                                                                                                                                                                                                                                                                                                                                          |
| Billed Amt:             | Original billed amount from AR.                                                                                                                                                                                                                                                                                                                                                                   |
| Amount to Post:         | The payment amount plus or minus the adjustment amount will equal the amount to post for this claim number.                                                                                                                                                                                                                                                                                       |
| Service Date:           | Beginning Service Date for this Claim                                                                                                                                                                                                                                                                                                                                                             |
| COB:                    | Coordination of Benefits information that indicates whether a secondary payer has been identified for this claim.                                                                                                                                                                                                                                                                                 |
| Rx Copay:               | Current Rx Copay status of the patient                                                                                                                                                                                                                                                                                                                                                            |
| Means Test:             | Indicates if this patient may be responsible for Means Test co-payments                                                                                                                                                                                                                                                                                                                           |
| Payment Amt:            | Amount of money paid for this claim on this ERA.                                                                                                                                                                                                                                                                                                                                                  |
| Total Adjustments:      | Net total of all adjustments for this line item.                                                                                                                                                                                                                                                                                                                                                  |
| Net:                    | The payment amount plus or minus the adjustment amount.                                                                                                                                                                                                                                                                                                                                           |
| ECME \#:                | ECME number generated when the NCPDP claim is submitted for a pharmacy prescription. This field only displays for a pharmacy claim.                                                                                                                                                                                                                                                               |
| Rx/Fill/Release Status: | The prescription number, fill number and release status (released, non-released). This field only displays for a pharmacy claim.                                                                                                                                                                                                                                                                  |
| DOS:                    | The date of service submitted on the NCPDP claim. This field only displays for a pharmacy claim.                                                                                                                                                                                                                                                                                                  |
| APAR Reason:            | The reason the EEOB is on the APAR list                                                                                                                                                                                                                                                                                                                                                           |

### APAR Scratchpad - Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of actions available on the APAR Scratchpad that can assist a user to ensure that the correct payment is being applied to the correct claim. With the exception of the Mark for Auto-Post action, the actions behave the same as the actions on the ERA Worklist Scratchpad. Refer to the ERA Worklist Scratchpad section for more details on functionality.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Action</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Split/Edit a Line</td>
<td><p>Used to split a payment or adjustment between two or more bills (if the payer has combined payments) or to correct the claim # associated with a payment (if the payer has reported the payment for the wrong bill). Option can also be used to put payment into suspense.</p>
<p>This is locked with the security key “RCDPEPP”.</p></td>
</tr>
<tr class="odd">
<td>Mark for Auto-Post</td>
<td><p>This action checks the EEOB for auto-posting criteria. If all criteria are met, the EEOB is successfully marked for auto-post which means the EEOB will be removed from the APAR display and reprocessed by the nightly auto-post job. Verification (V) is not required before marking an EEOB for auto-posting.</p>
<p>This is locked with the security key “RCDPEPP”.</p></td>
</tr>
<tr class="even">
<td>Claim Comment</td>
<td>Used to enter a one line comment for ANY exception on the APAR List.</td>
</tr>
<tr class="odd">
<td>View/Print EEOB</td>
<td>Used to display/print the detail received on the ERA for a selected line (EEOB).</td>
</tr>
<tr class="even">
<td>View/Print ERA</td>
<td>Used to view/print posting for claims with the entire formatted ERA, with or without the EEOB detail.</td>
</tr>
<tr class="odd">
<td>Research Menu</td>
<td>Link to all the necessary AR functions/ processes such as TPJI, needed to process ERAs. These can each still be accessed through regular AR menu options.</td>
</tr>
<tr class="even">
<td>Review Line</td>
<td>Allows addition of comments or used as a bookmark on a specific line within an ERA in case processing was interrupted, thereby allowing the user to more easily resume where he/she left off. This option must be turned ‘on’ each time the user enters the ERA to enter or view comments.</td>
</tr>
<tr class="odd">
<td>Verify</td>
<td><p>Provides the functionality to identify and manually mark EEOBs as verified.</p>
<p>This is locked with the security key “RCDPEPP”.</p></td>
</tr>
</tbody>
</table>

#### Action Option: Split/Edit a Line

Sometimes Payers combine payments for two or more claims onto one claim. This action is used to split the payment to the appropriate claim and to put a payment into suspense. It can also be used to correct an incorrect claim number. This action requires the RCDPEPP security key.

> <u>APAR - EEOB ITEM - SCRATCHPAD Jun 29, 2016@11:49:03         Page:    1 of    1</u>

> ERA Entry \#: 43622             Total Amt Pd: 2555.25

> Posted Amt: 0.00               Un-posted balance: 2555.25

> Payer Name/ID: AETNA/1066033492

> Posted Receipt \#(s):

>     EEOB: ERA Seq \# 1   Net Payment Amt: 2555.25                               

>        1.001 Claim \#: K602VMV Patient/Last 4: TW-WOMACK,JOHNNY/2222            

>          Claim Bal: 0.00   Billed Amt: 2555.25   Amt To Post: 2555.25          

>          Svc Dt: 11/3/15  COB: NO   Rx Copay: NON-EXEMPT  Means Tst: REQ       

>          Payment Amt: 2555.25   Total Adjustments: 0.00  Net: 2555.25          

>        APAR Reason: FIELD VERIFICATION FAILED                                  

> .............................................................................. 

>           Enter ?? for more actions                                            

>     Split/Edit a Line     EOB View/Print EEOB           Review Line

>     Mark for Auto Post    ERA View/Print ERA            Verify

>     Claim Comment        Research Menu             EXIT

> Select Action: Quit//SPLIT

This example shows how to Split/Edit Line item \#4 to post the payment correctly. This action takes place after reviewing the EEOB detailed data to confirm how the payment should be applied.

>        1.001 Claim \#: K602VMV Patient/Last 4: TW-WOMACK,JOHNNY/2222

>          Claim Bal: 0.00   Billed Amt: 2555.25   Amt To Post: 2555.25

>          Svc Dt: 11/3/15  COB: NO   Rx Copay: NON-EXEMPT  Means Tst: REQ

>          Payment Amt: 2555.25   Total Adjustments: 0.00  Net: 2555.25

>        APAR Reason: FIELD VERIFICATION FAILED

> ..............................................................................

> CLAIM \#: K602VMV//   \>\>Current claim balance is: 0.00

> PAYMENT AMOUNT TO APPLY TO THIS CLAIM: 2555.25// 2000

> RECEIPT LINE COMMENT: comment for claim K602vmv

> CLAIM \#: k602vmu  \>\>Current claim balance is: 3444.75

> PAYMENT AMOUNT TO APPLY TO THIS CLAIM: 555.25// 500

> RECEIPT LINE COMMENT: comment for claim K602vmu

> CLAIM \#: k602vmy  \>\>Current claim balance is: 0.00

> PAYMENT AMOUNT TO APPLY TO THIS CLAIM: 55.25//

> RECEIPT LINE COMMENT: comment for claim K602vmy

Apply the correct payment amount to the correct claim number(s) until all the funds are applied.

> <u>EEOB WORKLIST SPLIT LINE      Jun 29, 2016@12:04:13         Page:    1 of    1</u>

>        1.001 Claim \#: K602VMV Patient/Last 4: TW-WOMACK,JOHNNY/2222

>          Claim Bal: 0.00   Billed Amt: 2555.25   Amt To Post: 2555.25

>          Svc Dt: 11/3/15  COB: NO   Rx Copay: NON-EXEMPT  Means Tst: REQ

>          Payment Amt: 2555.25   Total Adjustments: 0.00  Net: 2555.25

>        APAR Reason: FIELD VERIFICATION FAILED

> ..............................................................................

> <u>    Claim \#                    Payment Amount   Adjustment Amt   Net Amount    </u>

> 1   K602VMV                            2000.00             0.00          2000.00

>           comment for claim K602vmv                                            

> 2   k602vmu                             500.00             0.00           500.00

>           comment for claim K602vmu                                            

> 3   k602vmy                              55.25             0.00            55.25

>           comment for claim K602vmy                                            

>                                 ==============   ==============   ==============

>     TOTALS:                            2555.25             0.00          2555.25

>           Enter ?? for more actions                                            

>   File New Lines            Edit Lines Split          Exit

> Select Action:Quit//

At this point the user should FILE NEW LINES to process the split.

Edit Line Split if the information is not correct. File the new lines to save this information. *Exiting without filing will mean all changes are discarded.*

Reason text (i.e. Comment) is mandatory when leaving a portion of the payment in suspense.

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

The scratchpad screen displays the following if a receipt line comment has been added

2.002 Claim \#: SUPENSE Patient/Last 4: ??

\*\*\*CLAIM NOT FOUND IN YOUR AR \*\*\*

Payment Amt: 160.00 Total Adjustments: 0.00 Net: 160.00

Receipt: E1702150EB

Receipt Comment: OVERPAYMENT

Added By: EMPLOYEE,ONE

Date/Time Added: July 20 2017@10:00:00

#### Action Option: Mark for Auto-Post

The ListManager screen contains the action of Mark for Auto-Post that will check the EEOB for auto-posting criteria and mark the EEOB for auto-posting if all criteria are met. This action requires the RCDPEPP security key.

#### Action Option: Claim Comment 

The ListManager screen includes a “Claim Comment” option to allow you to enter a one line comment for ANY exception on the APAR List.

\+ Enter ?? for more actions

Split/Edit a Line EOB View/Print EEOB t Review Line

Mark for Auto Post ERA View/Print ERA Verify

Claim Comment Research EXIT

Select Action: Quit//<u>Claim</u>

Select EDI LBox EEOB Data Exception(s): (1-4): <u>2</u>

Selection \#: <u>2 K777777</u>

Comment: This is where the Claim Comment will appear and may wrap to the next line. A comment can be entered for ANY claim and is tied to an ERA Seq line#.

<u>NOTE</u>: Once successfully entered, the Claim Comment displays as indicated in the APAR screen display and on the ERA Worklist/Scratch Pad as well as on the View/Print ERA display – on the individual EEOB. If the EEOB has no comment, nothing will display.

#### Action Option: MARK FOR AUTO-POST 

When you select the new “Mark for Auto Post” Action Option, the system re-evaluates the selected ERA to determine if the ERA can be marked as an Auto-Post CANDIDATE. The system displays a message to the user indicating whether the ERA was successfully Marked as an Auto-Post CANDIDATE – or – the reason why the check failed. This action requires the RCDPEPP security key.

- If the system determines that the <u>ERA IS an Auto-Post CANDIDATE</u>, the following success message is displayed:

> ERA List - Worklist Nov 30, 2015@12:31:17 Page: 1 of 22

> SELECTED MATCH STATUS: BOTH POST STATUS : BOTH

>            DATE RANGE: 2/12/15-2/12/15   AUTO-POSTING    : BOTH

>           ALL PAYERS                     PHARMACY/MEDICAL: BOTH

> \#       ERA \#            Trace#

> <u>            PAYER NAME/MATCH STATUS & DATE  ERA PAID DT  TOT AMT PAID   DT REC’D</u>

> 1       4           63595X56923                                                 

>                                          2/12/15           485.27       2/12/15

>             EPHARM INSURANCE                APPROX \# EEOBs: 1                  

>             EFT MATCHED          2/12/15  EFT RECEIPT STATUS: NOT ENTERED    

>           \|’-‘ No scratchpad\|’x’ EXC \|’A’ autopost complete                    

>     Select ERA                View/Print ERA            Admin Cost Adj

>     Sort List                 Change View Exit

>     Mark for Auto Post        ERA Manual Match

> Select Action: Quit// MAR   Mark for Auto Post 

> ERA has been successfully Marked as an Auto-Post CANDIDATE

> Enter RETURN to continue or ‘^’ to exit:

> NOTE: If the ERA is deemed an Auto-Post CANDIDATE, the ERA enters the Auto-Post pipeline to be processed with other CANDIDATES during the next nightly process.

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

VistA runs a nightly job to automatically perform a decrease adjustment to a third party medical claim under certain conditions. The automatic decrease is made with a contractual decrease adjustment amount that brings the claim balance to zero.

An automatic decrease will only occur if the EEOB has been auto-posted. Refer to the section on Parameters for details on the settings that affect auto-decrease of medical claims.

The following conditions must be met:

- Auto-posting of third party medical claims is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The payer is not excluded from auto-posting of third party medical claims in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\] and the EEOB is auto-posted.
- Auto-decrease of third party medical claims is enabled in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The payer is not excluded from auto-decrease of third party medical claims in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The number of days since the EEOB was posted is equal to or greater than the number of days specified in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The residual balance on the EEOB is equal to or less than the dollar amount maximum specified in the EDI LOCKBOX PARAMETERS \[RCDPE EDI LOCKBOX PARAMETERS\].
- The claim has not been referred to regional council or general council.

#### Decrease Adjustment Warning Messages 

The option DECREASE ADJUSTMENT \[PRCAC TR DECREASE\] displays a warning message if there are pending payments for the selected claim. Additionally, the user can receive a “Marked for Auto-Post warning if they try to make a decrease adjustment on a bill that has at least one associated EEOB marked for auto-post.

> Select Adjustment to an AR record \<TEST ACCOUNT\> Option: Decrease Adjustment

> Select (B)ILL or (E)CME#: B// ILL NUMBER

> Select BILL: Kxxxxxx

>      1   Kxxxxxx  552-Kxxxxxx RX CO-PAYMENT/N  10/01/03  xxxx,xxxx    COLLECTED

>      2   Kxxxxxx  405-Kxxxxxx REIMBURS.HEALTH  05/15/14  EXPRESS SC   ACTIVE

> CHOOSE 1-2: 2  405-Kxxxxxx REIMBURS.HEALTH  05/15/14  EXPRESS SC      ACTIVE

>         Principal Balance:    51051.58  FY: 14  Principal Balance: 51051.58

>          Interest Balance:        0.00

>             Admin Balance:        0.00

>                            -----------

>             TOTAL Balance:    51051.58

> Checking the bill's balance ... IN Balance!

> <u>Marked for Auto-Post. Are you sure? (Y/N) NO// NO</u>

> Exiting bill adjustment.

> Select (B)ILL or (E)CME#: B// ILL NUMBER

>      1   Kxxxxxx  552-Kxxxxxx RX CO-PAYMENT/N  10/01/03  xxxxx,xxxx    COLLECTED

>      2   Kxxxxxx  405-Kxxxxxx REIMBURS.HEALTH  05/15/14  EXPRESS SC   ACTIVE

> CHOOSE 1-2: 2  405-Kxxxxxx REIMBURS.HEALTH  05/15/14  EXPRESS SC      ACTIVE

>         Principal Balance:    51051.58  FY: 14  Principal Balance: 51051.58

>          Interest Balance:        0.00

>             Admin Balance:        0.00

>                            -----------

>             TOTAL Balance:    51051.58

> Checking the bill's balance ... IN Balance!

> Warning – Pending Payments of \$XXXX.XX exist

> Rcpt: XXXXXXXXX \$XX.XX No Trace Number

> Rcpt: XXXXXXXXX \$XXX.XX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

> Rcpt: XXXXXXXXX \$XXX.XX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

> ERA: XXXXX \$XX.XX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

> <u>Marked for Auto-Post. Are you sure? (Y/N) NO// YES</u>

> Enter the DECREASE Adjustment AMOUNT, from .01 to 51051.58.

>   DECREASE PRINCIPAL BALANCE BY: 1.00

>   Is this a CONTRACT adjustment ? YES//

> If you process the transaction, the bill will look like:

> Current Principal Balance:    51051.58

>   NEW DECREASE Adjustment:       -1.00

>                            -----------

>     NEW Principal Balance:    51050.58

> Are you sure you want to enter this DECREASE adjustment ? YES//

>   Adjustment Transaction: 8770898 has been added.

> Enter a comment for the DECREASE Adjustment:

> COMMENTS:

>   No existing text

>   Edit? NO//

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

## # The EFT has been accepted by FMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## FMS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Financial Management System (FMS) is an interactive system to manage central payment services to federal government agencies including the VHA financial data. Deposits to FMS are transmitted during the nightly process as individual deposits and are relayed through the DMI/mailman system. The EFT information is transferred into VistA from Financial Services Center (FSC). Although paper checks are also deposited through FMS by a daily deposit ticket at each medical center, EFT’s are also deposited via a deposit ticket. Deposit tickets are assigned for EFT’s by PNC bank (they assign the 6-digit number, and the FSC makes it a 9-digit number by adding a “569” prefix).

## Three Day EFT Cycle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The diagram below demonstrates a high level overview of the ePay/FMS process. Upon adjudication at the payer level, the payer transmits 835 information to their respective banking partner. In turn, this banking partner transmits the information to PNC Bank, the banking partner of the VA. PNC bank sends the EFT information to US Treasury for deposit and to FSC to be translated into VistA language and for processing to the sites. In addition to sending the data to each individual VistA system, FSC also sends the information to EPHRA for storing and reference of the data as needed. Each VistA system interacts with FMS through the nightly process, notifying the financial system of funds that have been processed for each medical center. A complete cycle takes three business days to complete.

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/005.png)

The three day cycle detailed:

- Day 1 – EFT populates VistA with a system generated electronic (e) receipt and transmits to FMS with a CR document during the nightly process. This shows in the VistA system as ‘NA’ when viewing the worklist. Deposit can be viewed by looking at Receipt profile, List of receipts, or deposit processing.

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/006.png)

- Day 2 – FMS accepts deposit and sends message back to VistA during nightly process. The money is deposited into 528704/8NZZ. This shows in the VistA system as ‘transmitted’ when viewing the worklist.

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/007.png)

- Day 3 – EFT is ready to be processed with ERA or paper EOB and transmit back to FMS. This shows in the VistA system as ‘accepted’ when viewing the worklist.

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/008.png)

The screen capture below demonstrates how the three day cycle shows on your worklist in your VistA system. This information can also be viewed on the EFT Daily Activity Report and the EFT unmatched aging report:

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/009.png)When an e-receipt is processed to FMS, a TR document (transfer document) is created. The TR document transmits during the nightly process. The TR document does not transmit money to FMS, but rather transfers funds from 528704/8NZZ to the appropriate MCCF appropriation of 528704. The TR document number can be viewed in the VistA system under the Receipt Processing Option.

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/010.png)

## EFT Deposits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view a copy of the CR code sheet on the CRLT table, enter the transaction code (CR) and the CR number. This screen shows the Fund and RSC the money dropped into in FMS. For this example, the CR number is 555K4A000C:

ACTION: N TABLEID: CRLT USERID: S555 SLK

\*\*\* CASH RECEIPTS LINE INQUIRY SCREEN \*\*\*

KEY IS TRANS CODE, CR NUMBER, LINE

TRANS CODE: CR CR NUMBER: 555K4A000C

01-

LINE: 001 BFYS: 04 FUND: 528704

STATION/SAT: 555 FCP/PRJ: JOB NO:

COST CTR/SUB: BOC/SUB: REPT CATG:

REV SRCE/SUB: 8NZZ CLSD BFYS: CLSD FUND:

GL ACCOUNT: TRANS TYPE: 23 TRAVEL TYPE:

VENDOR/PROVIDER: MCCFVALUE UNAPPLIED DEPOSIT NO:

AMOUNT: 1,480.00 CHECK NUMBER:

REF TC: REF DOC NO: REF LINE:

ADV: ADVANCE NO: ADV IND:

AGREEMENT NO: ACTION OUT:

DESCRIPTION:

View the GLDB table to see all deposits into the GL ACCT and RSC for approximately 2 months. For this table, select the FY, BFY, FUND, GL ACCT, AD/OF, STN, and RSC.

ACTION: R TABLEID: GLDB USERID: S570 SLK

\*\*\* GENERAL LEDGER DETAIL BALANCE INQUIRY SCREEN \*\*\*

FY BFY FUND GL ACCT AD/OF STN COST CTR FCP/PRJ BOC/REV SRCE TYPE

-- ----- ------ ------- ---- ------- -------- --------- ------------ ----

04 04 528704 1029 10 570 8NZZ 01

TRANS ID DATE FM REF DOCUMENT VENDOR VENDOR INV \# AMT

---------- ------ -- ------------- ------- ----------------- ----------

CR555K4A000C 031003 01 MCCFVALUE

1,480.00

CR555K4A000H 031004 01 MCCFVALUE

428.34

CR555K4A000Q 031007 01 MCCFVALUE

37.64

CR555K4A0001 031002 01 MCCFVALUE

1,084.95

All transfers in from CR Documents will show up under GL ACCT 1029. All transfers, from the TR documents will show up on this table under the GL ACCT 1030.

Key:

|              |                       |
|--------------|-----------------------|
| FY           | Fiscal Year           |
| BFY          | Budget Fiscal Year    |
| FUND         | Fund                  |
| GL ACCT      | General Ledger Acct   |
| AD/OF        | Administrative Office |
| STN          | Station               |
| BOC/REV SRCE | Revenue Source Code   |

*(This page included for two-sided copying.)*

# NPI 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The facility and providers NPI can be found within the ERA by viewing the ERA details. This was an added function by Patch.

EDI LOCKBOX WORKLIST - ERA DETAIL 10/10/03 Page: 2

==============================================================================

PATIENT: IBpatient,One A/5555 CLAIM \#: XXX-KXXXXXX

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

*(This page included for two-sided copying.)*

# Additional Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Auto–Audit 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New functionality is included with the 3<sup>rd</sup> Party EDI Lockbox patch. It allows EDI claims to automatically be audited and assigned an active status. Integrated Billing was modified to update AR whenever an EDI electronic status message is received for a bill that corresponds to one of these statuses:

> A3 CLAIM SENT FOR ALL PAYER ROUTING

> AC CLAIM FORWARDED TO PRINT CENTER

> A7 CLAIM SENT TO PAYER, NO FURTHER UPDATES TO FOLLOW

> A8 CLAIM SENT TO PAYER

> AA CLAIM RECEIVED, PRINTED AND MAILED BY PRINT CENTER

> 2P CLAIM ACCEPTED BY CLEARINGHOUSE- NO FURTHER UPDATES TO

FOLLOW

> 10 Claim sent to Payer

> 11 Claim sent to Payer

The auto-audit function must be made active by using the Update Rate Types For Auto-audit option located in the Supervisor’s AR Menu. Once the rate type is selected, answer YES to the prompt AUTO-AUDIT? Then enter the appropriate Bill Resulting From reason must be selected. This reason will be assigned to every EDI claim for this rate type that is auto-audited by the system. To turn off auto-audit for a rate type, select the option, enter the rate type and answer NO to the prompt AUTO-AUDIT?. This deletes the Bill Resulting From field from for the rate type selected and from that point on, no more bills having that rate type will be auto-audited. NOTE: Any claims that have claim rejects on the Claims Status Awaiting Resolution (CSA) worklist will not be auto-audited.

### Update Rate Types for Auto-audit 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To activate auto-audit for EDI claims within a particular rate type proceed with the following selections:

Select Supervisor's AR Menu Option: Update Rate Types For Auto-audit

Select RATE TYPE NAME: ??

Choose from:

1 CRIME VICTIM Who's Responsible: INSURER

2 DENTAL Who's Responsible: PATIENT

3 HUMANITARIAN Who's Responsible: PATIENT

4 INTERAGENCY Who's Responsible: INSURER

5 MEANS TEST Who's Responsible: PATIENT

6 MEDICARE ESRD Who's Responsible: OTHER (INSTITUTION)

7 NO FAULT INS. Who's Responsible: INSURER

8 REIMBURSABLE INS. Who's Responsible: INSURER

9 SHARING AGREEMENT Who's Responsible: OTHER (INSTITUTION)

10 TORT FEASOR Who's Responsible: INSURER

11 WORKERS' COMP. Who's Responsible: INSURER

12 CHAMPVA REIMB.INS. Who's Responsible: INSURER

.

Select RATE TYPE NAME: REIMBURSABLE INS. Who's Responsible: INSURER

AUTO-AUDIT?: NO// YES

BILL RESULTING FROM: HI HEALTH INSURANCE 3RD PARTY BILLING...OK? Yes// \<RET\>

### Process Open Bills/Paper Claims 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system, as part of the current nightly processing, automatically runs through open bills/paper claims with a status of NEW BILL in AR File \#430.

NOTES: A “Paper Claim” is identified by looking at the “Force To Print?” Parameter:

- MEDICAL Paper Claim = “FORCE LOCAL PRINT”
- PHARMACY Paper Claim = “NOT APPLICABLE – NOT TRANSMITTABLE”

### Validate Bill Data and Status 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system identifies which bills have bill type = “Reimbursable”, “NEW BILL” status, and have been created/completed in the billing package and signed off by a biller (i.e. which bills have all of the necessary information within patient info, insurance company, subscriber info, codes). Specifically, the data elements that must be present include Patient IEN, Debtor, Subscriber IEN, Group Name and Group Number.

### Process AR entry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If all of the necessary information is in the AR file \#430, the process updates the AR entry to contain the Category of REIMBURSABLE INSURANCE, HI (HEALTH INSURANCE 3RD PARTY BILLING) in the ‘Bill Resulting From’ field.

- For records updated during this process, the system updates the status to ACTIVE in AR File \#430.

### Required Security Key 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system utilizes the security key RCDPE AUTO DEC which is NOT automatically assigned to any user.

## Automatic Match EFTs to ERAs Acronym: MA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option manually starts the routine that runs as part of the normal nightly processing. Only select this option if you need to initiate the process of matching the 3rd Party Lockbox EFT records that have not yet been matched to the electronic ERAs currently on file. The process must be queued and only one of these processes can be running at any given time.

## EFT Manual Match Acronym: MM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to manually match an EFT detail record and an ERA record and will mark the 2 records as matched. Use this option *only* if the automatic matching function is not able to make the match. The EFT and ERA selected must both be unmatched and the ERA must not be associated with a receipt. This action may be necessary if the Trace Numbers or Insurance Company IDs do not match on the 2 records, but the payer has confirmed they are indeed supposed to be matched. To make matching easier, the system allows a partial match on trace number and leading zeroes are ignored. A date range filter can narrow the options for selection.

This option allows you to manually have the ERA re-evaluated for Auto-Posting to determine if the ERA can be marked for auto-post.

Select EDI Lockbox (ePayments) \<TEST ACCOUNT\> Option: EFT Manual Match

THIS OPTION WILL ALLOW YOU TO MANUALLY MATCH AN EFT DETAIL RECORD

WITH AN ERA RECORD.

Select by date Range? (Y/N) NO//

SELECT THE UNMATCHED EFT TO MATCH TO AN ERA: 1176 TT8104351 09-15-2015

EFT TRANSACTION: 1176 PAYER NAME: AETNA

PAYER ID: 1066033492 TRACE \#: ABC6381043449

TAX ID CORRECTION: NO CHANGE AMOUNT OF PAYMENT: 2202.50

MATCH STATUS: UNMATCHED RECEIPT \#: E15091502

EFT RECORDED AT SITE: YES DATE CLAIMS PAID: SEP 15, 2015

DATE RECEIVED: SEP 15, 2015 TRANSACTION \#: 1

DEPOSIT NUMBER: T649697 DEPOSIT DATE: SEP 25, 2018

ARE YOU SURE THIS IS THE EFT YOU WANT TO MATCH?: YES//

SELECT THE UNMATCHED ERA TO MATCH TO EFT \#3055: 43563 ABC6381045098 09-15-15

2202.50 AETNA UNMATCHED

ENTRY: 43563 TRACE NUMBER: ABC6381043449

INSURANCE CO ID: 1066014321 ERA DATE: SEP 15, 2015

TOTAL AMOUNT PAID: 2202.50 PAYMENT FROM: AETNA

FILE DATE/TIME: SEP 15, 2015@12:31:42

EFT MATCH STATUS: UNMATCHED ERA TYPE: ERA

INDIVIDUAL EOB COUNT: 1 MAIL MESSAGE: 218296

ERA DETAIL POST STATUS: NOT POSTED EXPECTED PAYMENT METHOD CODE: ACH

ARE YOU SURE THIS IS THE CORRECT ERA TO MATCH TO?: YES//

EFT \#3055 WAS SUCCESSFULLY MATCHED TO ERA \#43563

Do you wish to mark this entry for Auto Posting (Y/N)?

If the system determines that the ERA is NOT an auto-post candidate, one of the following error messages is displayed:

> ERA was NOT Marked as an Auto-Post CANDIDATE – Already marked for Auto-Posting

>     ERA was NOT Marked as an Auto-Post CANDIDATE – Already partially Auto-Posted

>     ERA was NOT Marked as an Auto-Post CANDIDATE – Already completely Auto-Posted

>     ERA was NOT Marked as an Auto-Post CANDIDATE – ERA not matched

>     ERA was NOT Marked as an Auto-Post CANDIDATE – Zero value ERA

>     ERA was NOT Marked as an Auto-Post CANDIDATE – Medical auto-posting off

>     ERA was NOT Marked as an Auto-Post CANDIDATE – Pharmacy auto-posting off

>     ERA was NOT Marked as an Auto-Post CANDIDATE – Medical payer excluded

>     ERA was NOT Marked as an Auto-Post CANDIDATE – Pharmacy payer excluded

>     ERA was NOT Marked as an Auto-Post CANDIDATE – Invalid Bill Number Exception(s)

>     ERA was NOT Marked as an Auto-Post CANDIDATE – ERA level Adjustment(s)

>     ERA was NOT Marked as an Auto-Post CANDIDATE – ERA has a receipt

>        ERA was NOT Marked as an Auto-Post CANDIDATE – Unable to create scratchpad 

>     ERA was NOT Marked as an Auto-Post CANDIDATE – Claim Level Adjustments w/o payment

>     ERA was NOT Marked as an Auto-Post CANDIDATE – +/- pairs do not balance

## Mark Ø-Balance EFT Matched Acronym: ZB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There may be times when an EFT is received with a zero payment and has a paper EEOB associated with it. This option allows the user to select an EFT detail record and mark it as matched to a paper EEOB. This removes it from the EFT UNMATCHED AGING REPORT.

## Unmatch an ERA Acronym: UN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an ERA has been marked with a match status in error, this option allows it to be marked as unmatched again. Only select an ERA that was previously marked as matched and that has had no receipt created for it yet. If the Scratchpad entry has been created, it will need to be deleted before the unmatch can occur. If the ERA was matched to an EFT, the EFT will be remarked as unmatched, and returned to the EFT Unmatched Aging Report.

## Update ERA Posted using Paper EOB Acronym: UP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When Payers first come on-line with the 3<sup>rd</sup> Party EDI Lockbox functions it is possible for a facility to receive both EEOB data and paper EOBs at the same time. As a result, there may be times when the EOB data gets posted from the paper EOB to AR and FMS without referencing the ERA. In this situation, the ERA will indicate it is unposted. Use this option to mark the ERA as POSTED. It requires entering the receipt \# used to post the paper EOB information.

- The existing functionality of the Update ERA Posted Using Paper EOB option is extended to include an automatic system search of an existing receipt when associating payments to the ERA. The automatic search for receipts to post requires the user to enter an ERA number to be updated to initiate automatic system search for associated receipt. The AR application will collect only those receipts that have an FMS DOC STATUS of “ACCEPTED BY FMS” as indicated in the following options:
- Receipt Processing \[RCDP RECEIPT PROCESSING\]
- List Of Receipts Report \[RCDP LIST OF RECEIPTS REPORT\]
1.  System will display specific payment details associated with the ERA for validation by the user prior to updating the ERA
- Patient Name/Last 4 of SSN
- Bill Number
- Check number
- Trace number
- Date of Service
- AR Transaction Amount
- Receipt Number
- Date of Receipt
2.  A new audit report will display or print data to identify usage of the Update ERA Posted to EOB option.

ERAs Posted with Paper EOB - Audit Report Page: 1

Run Date: 11/27/11@21:05:06

DIVISIONS: ALL

Date Range: 8/19/11 - 11/27/11 (DATE ERA UPDATED)

Date/Time User Who EFT Match Status

ERA \# Receipt \# ERA Updated Updated Detail Post Status

===============================================================================

14201 2362006 9/12/11@14:03:33 User, One MATCHED TO PAPER CHECK

MANUALLY POSTED

13877 13398756 10/10/11@16:31:09 User, Two MATCHED TO PAPER CHECK

MANUALLY POSTED

14150 E06111505 10/14/11@13:23:52 User, One MATCHED TO PAPER CHECK

MANUALLY POSTED

14151 13805055 10/14/11@14:29:30 User, One MATCHED TO PAPER CHECK

MANUALLY POSTED

14232 13805672 10/14/11@14:40:26 User, One MATCHED TO PAPER CHECK

The option now includes the capability of an automatic system search of an existing receipt when associating payments to the ERA.

## Remove ERA from Active Worklist Acronym: REM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to remove an unmatched ERA from the active Worklist. Use this option *only* if the deposit has not been made. The Remove ERA from Active Worklist option should always be used <u>cautiously</u>. Here are some common scenarios: you have received a duplicate ERA; the ERA doesn’t belong to your station, the Update an ERA Posted using a paper EOB is not feasible or there is no other way to process the ERA (i.e. Receipts are purged from system). This marks the POSTED status of the ERA as NOT POSTED-REMOVED; and the EFT MATCH STATUS of the ERA is updated to REMOVED FROM WORKLIST.

This option has been enhanced to require the user to have the security key RCDPE MARK ERA and requires that a comment is entered that will represent the reason the ERA was removed from the Worklist.

- If user tries to use the Remove ERA from Active Worklist option without having the RCDPE MARK ERA security key assign to them will get the following error message (refer to sample screen shot below):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EXC EDI Lockbox 3rd Party Exceptions</p>
<p>WL ERA Worklist</p>
<p>APAR Auto-Post Awaiting Resolution</p>
<p>MA Automatic Match EFTs to ERAs</p>
<p>MCR EEOB Move/Copy/Remove</p>
<p>MM EFT Manual Match</p>
<p>OEFT Unposted EFT Override</p>
<p>REFT Remove Duplicate EFT Deposits</p>
<p>REM Remove ERA from Active Worklist</p>
<p>REP EDI Lockbox (ePayments) Reports Menu ...</p>
<p>UN Unmatch An ERA</p>
<p>UP Update ERA Posted Using Paper EOB</p>
<p>ZB Mark 0-Balance EFT Matched</p>
</blockquote>
<p><strong> </strong></p>
<p><strong>Select EDI Lockbox Option: REM  Remove ERA from Active Worklist</strong></p>
<p><strong>SORRY, YOU ARE NOT AUTHORIZED TO USE THIS OPTION</strong></p>
<p>This option is locked with RCDPE MARK ERA key.</p>
<p><strong> </strong></p>
<p><strong>Enter RETURN to continue or '^' to exit:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## EEOB Move/Copy/Remove Acronym: MCR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EEOB Move/Copy/Remove option was added to the EDI Lockbox Menu which provides the capability to move or copy an EEOB to the correct patient account to ensure PHI is not compromised. This option has the following features:

- Ability to select an EEOB and move or copy it to the appropriate claim(s) or remove it from the claim
- The move, copy, or removal of an EEOB is captured and can be viewed with a new audit report

The remove option is locked with security key RCDPE REMOVE EEOB to restrict usage of removing EEOBs from claims.

Example of MOVE function

Select EDI Lockbox Option: mcr  EEOB Move/Copy/Remove

 

     Select one of the following:

 

          M         Move EEOB to different claim

          C         Copy EEOB to multiple claims

          R         Remove EEOB from claim

 

Select action: M// ove EEOB to different claim

 

Select EXPLANATION OF BENEFIT (EEOB) to MOVE: K400M44       ARPatient,One

    12-01-03     Inpatient     REIMBURSABLE INS.     PRNT/TX     

AETNA US HEALTHCARE (PRIMARY)

 

Select A/R Bill to MOVE to: K400M42  442-K400M42     REIMBURS.HEALTH INS.     01

-12-04    AETNA US HEALTHCARE     COLLECTED/CLOSED  \$0.00

 

Move EEOB from claim K400M44 to claim K400M42 ? YES//

 Enter JUSTIFICATION COMMENT: Moving EEOB to correct claim number

 EEOB Update Complete

> **NOTE:** For audit purposes, a justification is required to move an EEOB

Example of COPY function

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select EDI Lockbox Option: mcr  EEOB Move/Copy/Remove</strong></p>
<p><strong>      Select one of the following:</strong></p>
<p><strong>          M         Move EEOB to different claim</strong></p>
<p><strong>          C         Copy EEOB to multiple claims</strong></p>
<p><strong>R         Remove EEOB from claim</strong></p>
<p><strong> </strong></p>
<p><strong>Select action: M// c  Copy EEOB to multiple claims</strong></p>
<p><strong> </strong></p>
<p><strong>Select EXPLANATION OF BENEFIT (EEOB) to COPY: K301XF4       User,Test    </strong></p>
<p><strong>07-24-03     Outpatient     REIMBURSABLE INS.     PRNT/TX     </strong></p>
<p><strong>AETNA US HEALTHCARE (PRIMARY)</strong></p>
<p><strong> Select A/R Bill to COPY to: K301SHC  442-K301SHC     REIMBURS.HEALTH INS.     07</strong></p>
<p><strong>-18-03    AETNA US HEALTHCARE     COLLECTED/CLOSED  $0.00</strong></p>
<p><strong>Select another A/R Bill to COPY to: K301SI9  442-K301SI9     REIMBURS.HEALTH INS</strong></p>
<p><strong>.     07-18-03    AETNA US HEALTHCARE     COLLECTED/CLOSED  $0.00</strong></p>
<p><strong>Select another A/R Bill to COPY to:</strong></p>
<p><strong> </strong></p>
<p><strong>Copy EEOB from claim K301XF4 to claim(s) K301SHC, K301SI9 ? YES//</strong></p>
<p><strong> Enter JUSTIFICATION COMMENT: Copying EEOB information to additional claim K123456.</strong></p>
<p><strong> EEOB Update Complete</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** A justification comment is required to copy an EEOB to another claim.

Example of REMOVE function

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select EDI Lockbox Option: mcr  EEOB Move/Copy/Remove</strong></p>
<p><strong>      Select one of the following:</strong></p>
<p><strong>          M         Move EEOB to different claim</strong></p>
<p><strong>          C         Copy EEOB to multiple claims</strong></p>
<p>R         <strong>Remove EEOB from claim</strong></p>
<p><strong> </strong></p>
<p><strong>Select action: M// R  Remove EEOB from claim</strong></p>
<p><strong> </strong></p>
<p><strong>Select EXPLANATION OF BENEFIT (EEOB) to REMOVE: K301XF4       User,Test    </strong></p>
<p><strong>07-24-03     Outpatient     REIMBURSABLE INS.     PRNT/TX     </strong></p>
<p><strong>AETNA US HEALTHCARE (PRIMARY)</strong></p>
<p><strong> </strong></p>
<p><strong>Are you sure you want to remove EEOB from claim K301XF4 (Y/N)?? YES//</strong></p>
<p><strong> Enter JUSTIFICATION COMMENT: Removing EEOB information for test.</strong></p>
<p><strong> EEOB Update Complete</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

*Note: A justification comment is required to remove an EEOB. Also, the remove action is locked with security key RCDPE REMOVE EEOB.*

## Remove Duplicate EFT Deposits Acronym: REFT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remove Duplicate EFT Deposits option was added to the EDI Lockbox Menu which provides the capability to remove a duplicate EFT from the EFT Unmatched Aging report.

<span id="_Toc61610504" class="anchor"></span>EFTs marked as duplicates are displayed on the EFT Daily Activity report with a new display field that indicates the justification for the removal and the user that removed the EFT.

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

469082 1/7/04 1/7/04 136.49 NO FMS DOC

1 1/7/04 10.80 MATCHED/ERA \#10

803365450000024 1234567890

AETNA LIFE INS/1066033492

1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890, 1234567890

E16xxxxxB QUEUED

1 1/7/04 125.69 MATCHED/ERA \#12

The Duplicate EFT Audit Report was created to list all the EFT deposits that were removed from the EFT Unmatched Aging Report also referred to as the EFT Worklist. This report is found in the EDI Lockbox (ePayments) Reports Menu.

The new option is locked with a new security key RCDPE REMOVE DUPLICATES to restrict usage of removing EFTs from the EFT Unmatched Aging Report. Appropriate personnel, such as: managers, supervisors and leads should be assigned this security key.

EXC EDI Lockbox 3rd Party Exceptions

WL ERA Worklist

APAR Auto-Post Awaiting Resolution

MA Automatic Match EFTs to ERAs

MCR EEOB Move/Copy/Remove

MM EFT Manual Match

OEFT Unposted EFT Override

REFT Remove Duplicate EFT Deposits

REM Remove ERA from Active Worklist

REP EDI Lockbox (ePayments) Reports Menu ...

UN Unmatch An ERA

UP Update ERA Posted Using Paper EOB

ZB Mark 0-Balance EFT Matched

Select EDI Lockbox Option: reft Remove Duplicate EFT Deposits

SORRY, YOU ARE NOT AUTHORIZED TO USE THIS OPTION

The removed EFT will no longer display on the EFT Unmatched Aging Report

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

The following reports and screens display an EEOB indicator, the “%” character, next to the third party accounts claim number when an EEOB has been received in the system for the claim.

- Brief Account Profile    \[PRCAY ACCOUNT PROFILE\]     
- Full Account Profile     \[PRCAY FULL ACCOUNT PROFILE\]      
- List All Bills     \[PRCA LIST ALL BILLS\]   
- Bill Profile \[RCDP BILL PROFILE\]
- Bill Transactions \[RCDP BILL TRANSACTIONS\]
- Claims Matching Report \[RCDP CLAIMS MATCH\]
- List all Bills for a Patient   \[IB LIST ALL BILLS FOR PAT\]
- Insurance Payment Trend Report \[IB OUTPUT TREND REPORT\]
- BILL CHARGES screen of Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]
- Third Party Active Bills screen of Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]
- Third Party Inactive Bills screen of Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]
- Third party Follow-Up Report \[IBJD FOLLOW-UP THIRD PARTY\]

The following reports and screens display the EEOB indicator next to the first party claim number when a match can be made to an associated third party claim that has received an EEOB.

- Brief Account Profile    \[PRCAY ACCOUNT PROFILE\]     
- Full Account Profile     \[PRCAY FULL ACCOUNT PROFILE\]    
- First Party Follow-Up Report   \[IBJD FOLLOW-UP FIRST PARTY\]   
- List all Bills for a Patient   \[IB LIST ALL BILLS FOR PAT\]
- List All Bills     \[PRCA LIST ALL BILLS\]   
- Bill Profile \[RCDP BILL PROFILE\]
- Bill Transactions\[RCDP BILL TRANSACTIONS\]

Example of the EEOB indicator, the “%” character, appearing before a claim number

## Receipt Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RECEIPT PROCESSING option generates a new warning message that will alert the user that the receipt cannot be processed when a claim on the ERA Worklist would result in a negative balance if the decrease adjustment is allowed against the claim.

Receipt Processing – Warning Message

Receipt Profile May 15, 2017@15:57:59 Page: 1 of 1

Receipt \#: E17051500 Type of Payment: CHECK/MO PAYMENT

Deposit \#: Receipt Status: OPEN

ERA \#: xxxxxxxxxx ERA TTL: xxxxxx.xx FMS Document: NOTSENT

EFT \#: xxxxxxxxxx EFT TTL: xxxxxx.xx FMS Doc Status: NOT ENTERED

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

Generating automatic decrease adjustments from EDI Lbox Worklist ...

ARE YOU SURE YOU WANT TO CONTINUE?: YES// YES

Could not perform automatic decrease adj from ERA Worklist for

bill \# 442-K700WEI for amount of -6.55

> **WARNING:** Receipt cannot be processed.

Processing this receipt will cause this bill to have a negative balance

which is outside the scope of VA Accounting regulations.

Correct the error and reprocess this receipt.

## Unposted EFT Override Acronym: OEFT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Unposted EFT Override option displays current warning messages or error messages for third party medical claims and pharmacy claims. A user can select either Medical or Pharmacy claims to file an override. A comment must be entered to explain why the override is occurring. An override allows unrestricted scratchpad creation for the day the override is filed.

> Note: The Unposted EFT Override option is locked with the security key, RCDPE AGED PMT.

The menu option to override unposted EFT posting prevention requires the user to hold security key RCDPE AUTO DEC.

## Identify Payers Acronym: IDP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Identify Payers option allows all users to see a list of all payer names and if they have been identified as Tricare and/or Pharmacy only payers.

If the user has the RCDPE PAYER IDENTIFY security key they are allowed to set the Tricare and Pharmacy indicators for payers.

Prompts

Select EDI Lockbox (ePayments) \<TEST ACCOUNT\> Option: IDP Identify Payers

Filter by Date Added? NO//

Select payers to show. (A)ll, (P)harmacy, (T)ricare, (M)edical: A// ll

Payer List

Payer Pharmacy/Tricare Oct 10, 2017@13:04:57 Page: 1 of 16

Current Filter: ALL Payers

\# PAYER TIN Rx TR

1 AETNA 10XXXXXX92 Y

2 AETNA -CONTINENTAL LIFE INSURANCE COMPANY OF BRENTWOOD 16XXXXXX09

3 AETNA AMERICAN CONTINENTAL INSURANCE COMPANY 12XXXXXX54

4 AETNA GENWORTH LIFE AND ANNUITY INSURANCE 12XXXXXX54

5 ALLEGIANCE BENEFIT PLAN MANAGEMENT 18XXXXXX50 Y

6 ALTIUS HEALTH PLANS A COVENTRY HEALTH CARE PLAN 18XXXXXX31

7 AMERICAN FAMILY LIFE ASSURANCE COMPANY 15XXXXXX85

8 AMERICAN FAMILY MUTUAL INSURANCE 13XXXXXX10 Y Y

9 AMERICAN NAT'L INS CO OF TEXAS 17XXXXXX94

\+ Enter ?? for more actions \>\>\>

ED Edit Flags PH Flag Pharmacy Q Quit

FI Filter TR Flag Tricare

Select Action:Next Screen//

The Edit Flags, Flag Pharmacy and Flag Tricare actions will only be accessible to those with the RCDPE PAYER IDENTIFY security key.

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

Select EDI Lockbox (ePayments) Option:

The sub-menus for the EDI Lockbox Reports are listed here and display after you type REP above.

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

Select Additional Research Reports \<TEST ACCOUNT\> Option:

The sub-menu ‘AUDR’ for the EDI Lockbox Reports lists the following Audit Reports:

AD Auto-Decrease Adjustment Report

FAD First Party COPAY Auto-Decrease Report

FAM First Party COPAY Manual vs Auto-Decrease Report

AP Auto-Post Report

APR Auto-Posted Receipt Report

APH Auto Parameter History Report

DUPR Duplicate EFT Deposits Audit Report

ESC ERA Status Change Audit Report

ETA EFT Transaction Audit Report

MCR EEOB Move/Copy/Remove Audit Report

EMA EEOBs Marked for Auto-Post Audit Report

POSR ERAs Posted with Paper EOB Audit Report

PX Payer Implementation Report

REMR Remove ERA from Active Worklist Audit Report

Select Audit Reports \<TEST ACCOUNT\> Option:

The sub-menu ‘VP’ for the EDI Lockbox Reports contains only the View/Print ERA option.

## EFT Daily Activity Report Acronym: DA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Summary EFT Daily Activity Report provides total data on all EFT deposits. The report can be run on-demand with detail by date or just the summary data for the date range. Detail format provides a detailed list of all EFT deposits received within the selected date range and the corresponding EFT payments from the payers comprising each deposit. The following information appears on the EFT Daily Activity Statement.

- Deposit Ticket Information – including deposit number, date received, trace \#, which payment was from, CR document number, and TR document number(s)
- EFT’s that have been matched to an ERA
- Accepted EFT’s represent total dollars posted to FUND 52870404/Revenue Source Code 8NZZ.
- A flag to indicate if an EFT is a debit received by the payer, resulting in a debit voucher

When to run this report

Review the EFT Daily Activity Report on an as-needed basis to monitor electronic funds deposited to the US Treasury that are associated with your site.

Reviewing at least monthly you can ensure all deposits are in an ‘accepted’ status or in an appropriate ‘transmitted’ status. ALL deposits in a ‘rejected’ status must be corrected, in order to process the payments OR get collection credit for the funds.

How to run this report

To run the EFT Daily Activity Report in detail, proceed through the following steps:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select EDI Lockbox (ePayments) Reports Menu Option - DA EFT Daily Activity Report</p>
<p>Select division: ALL//</p>
<p>(S)UMMARY OR (D)ETAIL?: D// DETAIL AND TOTALS</p>
<p>START DATE: 3/1/2017 (MAR 01, 2017)</p>
<p>END DATE: MAR 01, 2017// T (APR 14, 2017)</p>
<p>(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/</p>
<p>RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//</p>
<p>Show EFTs with debits only? NO// YES</p>
<p>DISPLAY IN LISTMANAGER FORMAT (Y/N): NO//</p>
<p>DEVICE: HOME// TELNET TERMINAL</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>EDI LOCKBOX EFT DAILY ACTIVITY DETAIL REPORT Page: 1</p>
<p>RUN DATE: 04/30/17@16:56:14</p>
<p>DIVISIONS: ALL</p>
<p>PAYERS: SELECTED MEDICAL/PHARMACY/TRICARE:TRICARE</p>
<p>DATE RANGE: 03/01/17 - 03/01/17 (DATE DEPOSIT ADDED) DEBIT ONLY EFTs: NO</p>
<p>DEP # DEPOSIT DT DATE PD DEP AMOUNT FMS DEPOSIT STAT</p>
<p>EFT # MATCHED DT PAYMENT AMOUNT ERA MATCH STATUS</p>
<p>EFT PAYER TRACE # CR #</p>
<p>PAYMENT FROM</p>
<p>TR #</p>
<p>DEBIT DEP RECEIPT # DEP RECEIPT STATUS</p>
<p>===============================================================================</p>
<p>DATE EFT DEPOSIT RECEIVED: 03/01/17</p>
<p>T331543 03/01/17 03/01/17 737.58 ACCEPTED</p>
<p>2100.01 03/01/17 737.58 MATCHED/ERA #92594</p>
<p>ABC6434331449 CR-442K5A0A64</p>
<p>FEDERAL EMPLOYEES HEALTH BENEFIT A COVENTRY HEALTH CARE PLAN/1066033492</p>
<p>TR-442K5A0A65</p>
<p>E17030100 ACCEPTED</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

To run the EFT Daily Activity Report in summary, proceed through the following steps:

Select division: ALL//

(S)UMMARY OR (D)ETAIL?: D// SUMMARY TOTALS ONLY

START DATE: 3/1/2017 (MAR 01, 2017)

END DATE: MAR 1,2017// (MAR 01, 2017)

(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/

RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EDI LOCKBOX EFT DAILY ACTIVITY SUMMARY REPORT Page: 1

RUN DATE: 04/30/17@17:10:48

DIVISIONS: ALL

PAYERS: SELECTED MEDICAL/PHARMACY/TRICARE:TRICARE

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

When to run this report

Review the EFT Unmatched Aging Report on a regular basis, as determined by your site, to monitor outstanding electronic funds requiring a match to an ERA or even a paper EEOB.

How to run this report

To run the summary EFT Unmatched Aging Report, proceed with the following selections.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select EDI Lockbox Reports Menu Option: EFT EFT Unmatched Aging Report</p>
<p>Start date: T-1000 (AUG 07, 2014)</p>
<p>End date: AUG 7,2014// T (MAY 03, 2017)</p>
<p>(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/</p>
<p>RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//SPECIFIC</p>
<p>Select Insurance Company Name: TRICARE WEST 1860813402</p>
<p>Export the report to Microsoft Excel? (Y/N): NO//</p>
<p>Display in List Manager format? (Y/N): NO//</p>
<p>DEVICE: HOME// TELNET TERMINAL</p>
<p>EFT UNMATCHED AGING REPORT Page: 1</p>
<p>RUN DATE: 5/3/17@15:21:37</p>
<p>PAYERS: SELECTED MEDICAL/PHARMACY/TRICARE:TRICARE DATE RANGE: 8/7/14 - 5/3/17 (DATE EFT FILED)</p>
<p>AGED</p>
<p>DAYS TRACE # DEP DATE</p>
<p>DEPOSIT FROM/ID</p>
<p>FILE DATE DEPOSIT AMOUNT DEP#/EFT# DEPOSIT POST STATUS</p>
<p>================================================================================</p>
<p>Totals:</p>
<p>Number Aged Electronic EFT Messages Found: 1</p>
<p>Amount Aged Electronic EFT Messages Found: $66.76</p>
<p>================================================================================</p>
<p>637 68127436 3/18/15</p>
<p>FEDERAL EMPLOYEES HEALTH BENEFIT A COVENTRY HEALTH CARE PLAN/1470246511</p>
<p>8/5/15 66.76 569469949/2101.2 Posted to 8NZZ 8/6/15</p>
<p>* END OF REPORT *</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## ERA Unmatched Aging Report Acronym: ERA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces the ERA aging report containing a list of all Electronic Remittance Advice (ERA) records that have not been successfully matched to electronic EFTs within the user-specified number of days. Within EDI Lockbox Site Parameters, each site can set the number of days an ERA should wait before appearing on this report. An indicator of “x” displays before the Aged Days if an exception exists for the ERA.

When to run this report

Review the ERA Unmatched Aging Report on a regular basis, as determined by your site, to monitor outstanding electronic remittance advices requiring a match to an EFT or paper check.

How to run this report

To run the summary ERA Unmatched Aging Report proceed with the following selections:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select EDI Lockbox Reports Menu Option: ERA ERA Unmatched Aging Report</p>
<p>Select division: ALL//</p>
<p>START DATE: 1/1/2005 (JAN 01, 2005)</p>
<p>END DATE: JAN 1,2005// T (SEP 20, 2011)</p>
<p>(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/</p>
<p>RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//</p>
<p>Include Zero payment amounts? (Y/N): YES//</p>
<p>Export the report to Microsoft Excel? (Y/N): NO// EXPORT THE REPORT TO Microsoft Excel (Y/N): ? NO//</p>
<p>Display in List Manager format? (Y/N): NO//</p>
<p>DEVICE: HOME// TELNET TERMINAL</p>
<p>ERA UNMATCHED AGING REPORT Page: 1</p>
<p>RUN DATE/TIME: 9/20/11@14:44:15</p>
<p>DIVISIONS: ALL</p>
<p>PAYERS: SELECTED MEDICAL/PHARMACY/TRICARE:TRICAREDATE RANGE: 1/1/05 - 9/20/11 (ERA FILE DATE)</p>
<p>AGED</p>
<p>DAYS TRACE #</p>
<p>PAYMENT FROM/ID ERA DATE</p>
<p>FILE DATE AMOUNT PAID EEOB CNT ERA #</p>
<p>===============================================================================</p>
<p>TOTALS:</p>
<p>NUMBER AGED ELECTRONIC ERA MESSAGES FOUND: 155</p>
<p>AMOUNT AGED ELECTRONIC ERA MESSAGES FOUND: $55,599.63</p>
<p>===============================================================================</p>
<p>1672 0003214829</p>
<p>FIRST HEALTH/1364072377 2/17/07</p>
<p>2/21/07 10.56 1 14102</p>
<p>EEOB Seq #: 1 EEOB on file for K700XL8 10.56</p>
<p>x1672 2013140051</p>
<p>MAIL HANDLERS BENEFIT PLAN/1382242132 2/17/07</p>
<p>2/21/07 18.53 1 14106</p>
<p>Enter RETURN to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Pending EFT Override Report Acronym: PEO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces the Pending EFT Override Report containing all EFTs creating the EFT lock up, including an automatic list when the EFT lock up override option was used and includes the EFT override comments.

When to run this report

Review the Pending EFT Override Report whenever locked reports are encountered to help troubleshoot and resolve locked reports.

How to run this report

To run the summary Pending EFT Override Report proceed with the following selections:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Workload Reports Option: PEO Pending EFT Override Report</p>
<p>Medical Override not active for today's date</p>
<p>Aged EFT days before Medical posting prevented = 30</p>
<p>List the report in Microsoft Excel format? NO//</p>
<p>DEVICE: HOME// HOME (CRT) Right Margin: 80//</p>
<p>Pending EFT Override Report - Page 1 Run Date: Dec 07, 2018@09:06:08</p>
<p>Sorted by Aged Days, Comment: testing</p>
<p>Medical Override Date: OCT 31, 2018@07:04:46 User: USER,ONE</p>
<p>Number of Days (Age) of Unposted EFTs to prevent posting: 30</p>
<p>EFT Trace#</p>
<p>ERA Match Status EFT Received Aged Amount</p>
<p>===============================================================================</p>
<p>Total Number of Unposted EFTs: 68</p>
<p>Total Amount of Unposted EFTs: $251,726.33</p>
<p>===============================================================================</p>
<p>2089.7 1QG06355544</p>
<p>92116 MATCHED Jul 29, 2015 1227 $16,582.33</p>
<p>2094.13 9165357725</p>
<p>92492 MATCHED Aug 05, 2015 1220 $1,514.70</p>
<p>2094.24 68127436</p>
<p>None PAPER EOB MATCH Aug 05, 2015 1220 $66.76</p>
<p>2095.3 5640317212WR5</p>
<p>92434 MATCHED Aug 06, 2015 1219 $131.57</p>
<p>Press ENTER to continue, '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## EFT/ERA Trending Report Acronym: ETR 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERA/EFT TRENDING Report is used to display metrics on \#ERAs, \#EEOBs, \#EFTs with \#days between ERA and EFT transactions. The report can be run for ALL payers or selected payer(s).

This report can also be found under the EDI Diagnostics Measures Reports menu.

## Unapplied EFT Deposits Report Acronym: UN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces a list of EFT deposits that have EFT detail records whose funds have not been applied to bills in A/R. These funds remain in FUND 5287.4, RSC 8NZZ. Only those EFTs that have either not been matched to an ERA or have been matched to an ERA, but the payment receipt has not been posted to FMS, will appear on this report

EFT’s posted using a paper EOB will continue to show on this report. This will be updated with a future enhancement.

When to run this report

You will run the Unapplied EFT Deposits Report on a regular basis, as determined by your facility, to monitor funds outstanding in FUND 5287.4, REVENUE SOURCE CODE 8NZZ.

How to run this report

To run the Unapplied EFT Deposits Report proceed with the following selections:

Unapplied EFT Deposits Report Page: 2

Run Date: 12/12/16@16:42:39 MEDICAL/PHARMACY/TRICARE:TRICARE

Date Range: 7/28/89 - 12/12/16 (Deposit Date)

TOTAL NUMBER OF UNAPPLIED DEPOSITS: 13

TOTAL AMOUNT OF UNAPPLIED DEPOSITS: \$8,274.78

DEPOSIT#/EFT# DEPOSIT DATE TOT AMT OF DEPOSIT TOT AMT UNPOSTED

PAYER/ID

TRACE \# PAYMENT AMT RECEIPT \#

ERA MATCHED FMS DOC \#/STATUS

=============================================================================

569836 3/4/11 1345.68 1345.68

FEDERAL EMPLOYEES HEALTH BENEFIT A COVENTRY HEALTH CARE PLAN/1362739571

1044620067/2119.1 880.98 E11030800

MATCHED TO ERA \#: 43349 TR-442K1A03DK - TRANSMITTED

Press enter to continue, '^' to exit:

## ## Active Bills with EEOB Report Acronym: AB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was created in order to enable one to manage ACTIVE third party insurance claims that have an EDI Lockbox EEOB, but have a balance remaining. All active bills that have EEOBs associated with them and also have a balance \>0 will be displayed, sorted by insurance company.

When to run this report

Run this report on a routine basis, as determined by your site, in order to identify any payments that have been posted to accounts without any contractual adjustments and analysis having been performed. This report is a <u>very</u> useful tool for keeping Account Receivables from becoming aged.

The ERA Unmatched Aging report should be current before working this report.

*<span class="smallcaps">Note</span>: It is recommended that the report is queued, since it will take a while to print.*

How to run this report

To run the Active Bills with an EEOB \> 0 report, proceed with the following steps:

Select EDI Lockbox Reports Menu Option: AB  Active Bills With EEOB Report

Select division: ALL//

(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/ \<=new prompt/Default=ALL

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

PAYERS: SELECTED MEDICAL/PHARMACY/TRICARE:TRICARE

DATE RANGE: 12/03/14 - 01/02/15 PAYMENT TYPE:TRICARE

PATIENT NAME SSN BILL#

INS CO NAME BALANCE AMT BILLED AMT PAID

TRACE# DT REC'D DT POST

================================================================================

XXXXXXXXXXXXXXXXXX 2335 626KXXXXXX

AETNA\* 14.53 14.53 0.00

8132X65800XX230 9/16/13 9/25/13

XXXXXXXXXXXXXXXXXXX 9633 626KXXXXXX

AETNA\* 53.66 53.66 0.00

8141X55200XX932 7/9/14 7/14/14

XXXXXXXXXXXXXXXXXXX 9633 626KXXXXXX

AETNA\* 46.31 46.31 0.00

8141X95800XX893 7/21/14 8/5/14

## Auto Decrease Adjustment Report Acronym: AD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was created to monitor EEOBs that have been automatically decreased to a zero balance by the system.

When to run this report

Run this report on a routine basis, as determined by your site, in order to identify any EEOB with a contractual decrease adjustment performed automatically by the system.

## Auto-Post Report Acronym: AP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was created to monitor EEOBs that have been automatically processed by the nightly job to create and process a receipt. This report has filter questions for Medical, Pharmacy, TRICARE or ALL claim types and allows the user to filter and sort by Insurance Company Name or TIN.

When to run this report

Run this report on a routine basis, as determined by your site, in order to identify any EEOB that has a processed receipt resulting from the nightly auto-posting job.

How to run this report

To run the Auto-Posted Report proceed through the following steps:

Auto-Post Report (Detail)

EDI LOCKBOX AUTO-POST REPORT - DETAIL Print Date: 11/26/18@13:21:03 Page: 1

DIVISIONS: ALL

CLAIM TYPE: ALL SORTED BY: PAYER TIN

TINS : ALL

AUTOPOST POSTING RESULTS FOR DATE RANGE: 08/18/18 - 11/26/18

=====================================================================================================================

PATIENT NAME/SSN ERA# DT REC'D DT POST BILL# AMT BILLED AMT PAID BALANCE %COLL

=====================================================================================================================

DIVISION: CHEYENNE VAMROC/442

-----------------------------------------------------------------------------------------------------------------------------------

PAYER: 1066033492/AETNA

-----------------------------------------------------------------------------------------------------------------------------------

PATIENT,NUMBER ONEONE/4064 93313 09/18/18 09/18/18 K505XHQ 14.84 568.01 46.83 3827.56%

DEP#:123456789 EFT#:002212.99 RECEIPT#: E18092104999 TRACE#:ABC45678901234567890123456789012345678901234567890

Auto-Post Report (Summary)

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

SUBTOTALS FOR PAYER: 1202901054/AETNA GENWORTH LIFE AND ANNUITY INSURANCE 605.19 4022.26 653956.45 664.63%

COUNT 3 3 3

MEAN 201.73 1340.75 217985.48

## Auto-Posted Receipt Report Acronym: APR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Review this report on a regular basis, as determined by your site, to display all auto-posted receipts to ensure payments are posted to patient’s 3rd party claims.

If payments are 'hung up' and not processed timely, veterans’ copayments are not credited in a timely fashion.

How to run this report

To run the Auto-Posted Receipt Report proceed through the following steps:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select EDI Lockbox Reports Menu Option - APR AUTO-POSTED RECEIPT REPORT</p>
<p>Select division: ALL//</p>
<p>(A)uto-Post Date or (E)RA Date Received? (A/E): A//</p>
<p>START DATE: 3/1/2017 (MAR 01, 2017)</p>
<p>END DATE: MAR 01, 2017// T (MAY 01, 2017)</p>
<p>Select ERAs to be Displayed: Both// ??</p>
<p>Enter 1 to only display Posted Receipts.</p>
<p>Enter 2 to only display ERAs with missing receipts.</p>
<p>Enter 3 to display all receipts.</p>
<p>Select one of the following:</p>
<p>1 Posted/Completed Receipts</p>
<p>2 Missing Receipts</p>
<p>3 Both</p>
<p>(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/</p>
<p>Run Report for (A)LL, (S)PECIFIC, or (R)ANGE of Insurance Companies?: ALL//</p>
<p>Sort by (D)ate or (M)issing Receipts: D//</p>
<p>Display in List Manager format? (Y/N): NO//</p>
<p>Export the report to Microsoft Excel? NO//</p>
<p>DEVICE: HOME//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>AUTO-POSTED RECEIPT REPORT May 01, 2017@13:08:17 Page: 1</p>
<p>FILTERS: All Divs; Selected Payers;TRICARE Auto-Post Date 03/01/17-05/01/17</p>
<p>ERA: All Receipts SORT: Auto-Post Date</p>
<p>DATE DATE</p>
<p>RECEIVED POSTED RECEIPT USER AMOUNT FMS DOC</p>
<p>--------------------------------------------------------------------------------</p>
<p>Payer: AETNA</p>
<p>ERA: 92594 ERA Total: 737.58</p>
<p>Receipt Total: 737.58</p>
<p>Trace #: ABC6434331449</p>
<p>03/01/17 03/01/17 E17030101 737.58 TR-442K5A0A65</p>
<p>ERA: 92595 ERA Total: 371.72 * Missing Receipts *</p>
<p>Receipt Total: 177.72</p>
<p>Trace #: ABC6435956395</p>
<p>03/17/17 * Missing * POST 194.00</p>
<p>03/17/17 03/17/17 E17031701A POST 177.72 TR-442K5A0A67</p>
<p>* END OF REPORT *</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Auto Parameter History Report Acronym: APH

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

The Auto Parameter History Report shows the Date/Time, User, Parameter, Old Value, and New Value of any Auto-Activity Parameter changes. Use this report to identify the historical changes and/or trends related to any Auto-Activity Parameter. The report can be filtered by Start/End Date.

How to run this report

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

11/13/18@09:56:37 USER,ONE

TRICARE FLAG (TRICARE WEST) NO YES

11/15/18@11:04:21 USER,ONE

AUTO-POST RX CLAIMS ENABLED NO YES

11/15/18@11:18:49 USER,ONE

TRICARE EFT POST PREVENT DAYS 14 30

11/15/18@11:19:14 USER,ONE

TRICARE EFT POST PREVENT DAYS 30 14

11/15/18@11:19:31 USER,ONE

AUTO-POST RX CLAIMS ENABLED YES NO

11/16/18@12:51:02 USER,ONE

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

11/16/18@13:51:24 USER,ONE

AUTO-DECREASE AMT DEFAULT 250.00 7,000.00

CARC AUTO DECREASE NO-PAY (45) NO YES

CARC DECREASE AMOUNT NO-PAY (45) 1.00 7,000.00

Press enter to continue, '^' to exit:

## CARC Data Report Acronym: CR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Run this report on a routine basis, as determined by your site, in order to determine any CARC codes returned on 835 forms by payers.

How to run this report

To run the 8335 CARC Data report, proceed with the following steps:

Select EDI Lockbox Reports Menu Option: CR 835 CARC Data Report

Select Division: ALL//

(S)UMMARY or (D)ETAIL FORMAT: SUMMARY// *\<=Defaults to SUMMARY*

SELECT (C)ARC, (R)ANGE of CARCs or (A)LL: ALL//

(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/

Run Report for (A)LL,(S)PECIFIC,or (R)ANGE of Insurance Companies?: ALL//SPECIFIC

Select Insurance Company NAME: TRICARE WEST 1860813402

SORT BY (C)ARC or (P)AYER?: CARC// *\<=Defaults to CARC*

START DATE: T//090115

END DATE: T//091615

DEVICE: HOME// UCX/TELNET Right Margin: 80//

## Duplicate EFT Audit report Acronym: DUPR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Review the Duplicate EFT Audit Report on a regular basis, as determined by your site, to monitor usage of the Remove Duplicate EFT Deposits option.

How to run this report

To run the Duplicate EFT Audit report, proceed with the following selections:

## ERA Status Change Audit Report Acronym: ESC 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Run this report on a routine basis, as determined by your site, in order to display a detailed audit trail listing of ERA AUTO POST STATUS changes.

The report allows you to run an audit for a single ERA or ALL ERAs for a date range. Report will be sorted by ERA then by date/time. Specific data elements shall include: Date/Time, User, ERA#, STATUS (old/new) and Reason text.

The Reason text will be a summary of the “process” that caused the ERA Status to be changed along with the “outcome” of the change. Example Reason text messages are listed below with some of these messaged displayed in the report mockup.

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

How to run this report

To run the ERA Status Change Audit report, proceed with the following steps:

Select EDI Lockbox (ePayments) Reports Menu \<TEST ACCOUNT\> Option: ERA Status C

hange Audit Report

SELECT (S)ingle ERA or (A)LL: ALL//

(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/

START DATE: T// (DEC 03, 2015)

END DATE: T// (DEC 03, 2015)

DEVICE: HOME// HOME (CRT) Right Margin: 80//

The ERA Status Change Audit report will display as follows:

EDI Lockbox ERA Status Change Audit Report Page: 1

RUN DATE: DEC 03, 2015@14:39:45 MEDICAL/PHARMACY/TRICARE:TRICARE

DATE RANGE: 12/03/2015 - 12/03/2015

ERA# Date/Time Edited Status (Old/New) User

Reason Text

--------------------------------------------------------------------------------

43522 12/03/15@01:54:13 NULL UNPOSTED POSTMASTER

Auto Matching: Marked as Auto-Post Candidate

43566 12/03/15@01:55:18 NULL NULL POSTMASTER

Auto Posting: Removed from Auto Posting-ERA level Adjustment(s)

44448 12/03/15@01:56:22 UNPOSTED PARTIAL POSTMASTER

Auto Posting: Some of the ERA lines went to APAR

44467 12/03/15@01:58:16 UNPOSTED COMPLETE POSTMASTER

Auto Posting: ERA posted successfully

44699 12/03/15@01:59:44 PARTIAL COMPLETE POSTMASTER

Auto Posting: ERA posted successfully

46777 12/03/15@12:10:12 NULL NULL SMITH,JOE

Exceptions: Not Marked as Auto-Post Candidate-ERA not matched

46784 12/03/15@12:22:47 NULL NULL SMITH,JOE

Exceptions: Not Marked as Auto-Post Candidate-Invalid Bill Number Exception(s)

46799 12/03/15@12:31:22 NULL UNPOSTED SMITH,JOE

Exceptions: Marked as Auto-Post Candidate

47786 12/03/15@12:40:47 NULL UNPOSTED SMITH,JOE

Worklist: Marked as Auto-Post Candidate

48422 12/03/15@13:11:33 COMPLETE COMPLETE SMITH,JOE

Worklist: Not Marked as Auto-Post Candidate-Already completely Auto-Posted

48687 12/03/15@13:44:44 NULL UNPOSTED SMITH,JOE

Manual Match: Marked as Auto-Post Candidate

48696 12/03/15@13:55:55 NULL NULL SMITH,JOE

Manual Match: Not Marked as Auto-Post Candidate-+/- pairs do not balance

48777 12/03/15@14:12:22 UNPOSTED NULL SMITH,JOE

Unmatch: Removed as Auto-Post Candidate

## EFT Transaction Audit Report Acronym: ETA 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Run this report on a routine basis, as determined by your site, in order to list all actions taken place for a single EFT.

For example: If a user matched the EFT to a paper EOB, the report would list the date, user and deposit ticket number. If another user unmatched/matched the EFT to an ERA, this data would also be displayed on the report. This report also *identifies which EFTs are ready to lock up the system.*

How to run this report

To run the EFT Transaction Audit report, proceed with the following steps:

The EFT Transaction Audit Report allows the user to generate SUMMARY or DETAIL EFT Data as described below.

Summary Report

Select EDI Lockbox (ePayments) Reports Menu \<TEST ACCOUNT\> Option: EFT Transact

ion Audit Report

(S)ummary or (D)etail Report format? SUMMARY// Summary Information Only

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

\*\*3052.1 09/01/15 TT7964771 2727.50 09/01/15 09/01/15

ABC637964X7703

AETNA/10660X33492

\*3053.1 09/08/15 TT8035484 9000.00 09/09/15 09/08/15

ABC638035X4846

AETNA/10660X33492

\*3054.1 09/15/15 TT8104218 2202.50 09/15/15 09/15/15

ABC638104X2181

AETNA/10660X33492

3055.1 09/15/15 TT8104351 2202.50 \<No History\> 09/15/15

ABC638104X3449

AETNA/10660X33492

3056.1 09/15/15 TT8104351 2202.50 \<No History\> 09/15/15

ABC638104X3480

AETNA/10660X33492

Enter RETURN to continue or '^' to exit:

Detail Report

You have the ability to look up a single EFT by Deposit#, Deposit Date, Receipt# or Trace#.

Search for EFT# by:

1.  Deposit (N)umber
2.  Deposit (D)ate
3.  (R)eceipt#
4.  (T)race#

Search for EFT# by://

All selection options include logic to assist you to select a single EFT as follows:

1)  <u>Deposit (N)umber:</u>

If the you choose to find a SINGLE EFT by Deposit#, the selection list displays as follows:

Select DEPOSIT: 569601

1 569601 by: ARUSER,ONE on: 03/31/10 amt: \$ 148.17 CONFIRMED

2 569601 by: ARUSER,TWO on: 08/21/15 amt: \$ 0.00 OPEN

3 569601 by: ARUSER,TWO on: 09/02/15 amt: \$ 0.00 OPEN

CHOOSE 1-3: 1

2)  <u>Deposit (D)ate:</u>

Once the <u>DEPOSIT</u> is selected, the system displays all EFTs on that Deposit for the user to select a SINGLE EFT.

Select DEPOSIT DATE: T// 032410 (MAR 24, 2010)

Select single EFT:

1\. 819 AETNA LIFE INS 8100X775500X01276 144.61 569597 03/24/10

2\. 819 AETNA LIFE INS 8100X773700X01185 87.20 569597 03/24/10

3\. 819 AETNA LIFE INS 8100X775400X01163 88.00 569597 03/24/10

4\. 819 UNITEDHEALTHCARE 10319X01081 3545.01 569597 03/24/10

5\. 819 UNITEDHEALTHCARE 10319X01083 20.88 569597 03/24/10

3)  <u>(R)eceipt#:</u>

If you choose to find a SINGLE EFT by Receipt#, the selection list will display as follows:

Select RECEIPT: e10040

1 E10040101 by: ARUSER,ONE on: 04/01/10 EDI LOCKBOX CLOSED

2 E10040200 by: ARUSER,TWO on: 04/02/10 EDI LOCKBOX CLOSED

3 E10040201 by: ARUSER,TWO on: 04/02/10 EDI LOCKBOX CLOSED

4 E10040202 by: ARUSER,TWO on: 04/02/10 EDI LOCKBOX CLOSED

5 E10040203 by: ARUSER,TWO on: 04/02/10 EDI LOCKBOX CLOSED

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1

Once the <u>RECEIPT</u> is selected, the system displays all EFTs on that Receipt for you to select a SINGLE EFT. This display is as follows:

Select RECEIPT: e10040101

Select single EFT:

1\. 824 SF MUTUAL 12051X8936GH0330 2.14 569603 04/01/10

2\. 824 SF MUTUAL 12051X8937GH0330 8.59 569603 04/01/10

3\. 824 UNITEDHEALTHCARE 10321X87875 0.02 569603 04/01/10

4)  <u>(T)race#:</u>

Once the Trace# is entered, if there is only ONE EFT that matches the entered Trace#, the EFT Audit Report will display for the selected SINGLE EFT. If there are multiple EFTs that match the entered Trace#, you are given the following display to select a SINGLE EFT for the Audit Report.

Select TRACE: ABC6369

1 ABC63692X49313 1052 AETNA 385.40 05/20/15

2 ABC63692X49473 1053 AETNA 385.40 05/20/15

3 ABC63692X51402 1054 AETNA 550.55 05/20/15

4 ABC63692X52144 1055 AETNA 1345.01 05/20/15

5 ABC63692X53837 1056 AETNA 2202.50 05/20/15

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5:

Once a single EFT is selected, the EFT Transaction Audit Report displays the entire EFT history.

## First Party COPAY Auto-Decrease Report Acronym: FAD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was created to display the Auto-Decrease Adjustments for First Party claims with residual balances for which decrease adjustments have been automatically applied by the nightly process.

When to run this report

Run this report on an “as needed” basis.

How to run this report

To run the First Party Auto-Decrease Adjustment Report, proceed through the following steps, selecting either All Patients or a Single Patient:

First Party COPAY Auto-Decrease Report (ALL PATIENTS)

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

PATIENT, ONE TWO/6332 50.00 23.88 NNN-K900I9 442-K5060D 01/10/19

CLIENT, THREE FOUR/2529 50.00 50.00 NNN-K900TZ 442-K50603 01/10/19

\*\*Totals for Date: 01/10/19 \# of Decrease Adjustments: 2

Total Amount of Decrease Adjustments: \$73.88

\*\*\*\* Totals for Date Range: \# of Decrease Adjustments: 2

Total Amount of Decrease Adjustments: \$73.88

\*\*\*\*\* END OF REPORT \*\*\*\*\*First Party COPAY Auto-Decrease Report (SINGLE PATIENT)

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

USER,THREE C 6332 50.00 23.88 442-K900I9 442-K5060D 01/10/19

\*\*Totals for Date: 01/10/19 \# of Decrease Adjustments: 1

Total Amount of Decrease Adjustments: \$23.88

\*\*\*\* Totals for Date Range: \# of Decrease Adjustments: 1

Total Amount of Decrease Adjustments: \$23.88

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## First Party COPAY Manual vs Auto-Decrease Report Acronym: FAM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was created to show the number of first party claims auto-released from hold versus the total auto-decreased. There are both summary and detail views.

When to run this report

Run this report on an “as needed” basis.

How to run this report

To run the First Party COPAY Manual vs Auto-Decrease Report, proceed through the following steps, selecting either Summary or Detail Format:

First Party COPAY Manual vs Auto-Decrease Report Prompts

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

First Party COPAY Manual vs Auto-Decrease Report Detail

First Party COPAY Release Report Page: 1

Run Date: 02/28/19@14:13:20

Divisions: ALL

Date Range: 11/20/18 - 02/28/19 (Date of Latest Decrease)

Sorted By: Claim - First to Last Display: DETAIL

3rd Party Copay Auto-Decr Manual Decr Total Decr

COPAY Bill \# Bill \# Date Amt Amt Amt Amt RH

--------------------------------------------------------------------------------------

442-K4042I9 442-K405BLE 02/12/19 15.00 6.75 0.00 6.75 \*

442-K405TBF 02/12/19 15.00 15.00 15.00

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

--------------------------------------------------------------------------------------

\*\*Totals for Date 02/12/19: 30.00 6.75 15.00 21.75 1

Percent for Date 02/12/19: 22.50% 50.00% 72.50% 50%

\*\*\*\* Totals for Date Range: 30.00 6.75 15.00 21.75

Percent for Date Range: 22.50% 50.00% 72.50%

\*\*\*\*\* END OF REPORT \*\*\*\*\*

Type \<Enter\> to continue or '^' to exit:

## EEOB Move/Copy/Remove Audit Report Acronym: MCR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Review the EEOB Move/Copy/Remove Audit Report on a regular basis, as determined by your site, to monitor EEOBs moved or copied from one claim to another

How to run this report

To run the report EEOB Move/Copy/Remove Audit Report, proceed with the following selections:

Select division: ALL//

START DATE: 05/28/14 (MAY 28, 2014)

END DATE: MAY 28, 2014// T (FEB 21, 2017)

Move/Copy/Remove or All (M/C/R/A): All//

Select division: ALL//

(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/

Export the report to Microsoft Excel? NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

EEOB Move/Copy/Remove - Audit Report Page: 1

Run Date/Time: 2/21/17@14:18:42

Divisions: ALL

Date Range: 05/28/14 - 02/21/17 (Date EEOB was Moved/Copied/Removed)

MEDICAL/PHARMACY/TRICARE:TRICARE

Action(s) Selected: ALL

Orig Bill# Trace \#

Moved/Copied/ Total Amt User Who Moved/

ERA \# Date/Time Removed Paid Copied/Removed

================================================================================

999K222ZZZ 00629417

78862 7/31/14@07:26:16 MOVED \$163.00 Patient, One

New Bill: KZZZ123 Other Bill Number(s): NONE

Justification Comments: EEOB moved from Claim K222ZZZ

Automatically by AUTOPOST

999K999BBB 02164161

77032 6/6/14@08:27:15 REMOVED \$1122.41 Patient, One

New Bill: K999ABC Other Bill Number(s): NONE

Justification Comments: EEOB removed from claim K999BBB

Automatically by AUTOPOST

999K222XXX 1157381779

85552 2/2/15@07:37:50 COPIED \$48.15 Patient, Two

New Bill: K111ZZZ Other Bill Number(s): K111AAA

Justification Comments: EEOB from claim K222XXX copied to claim(s)

K000XXX, K999YYY by automatically by AUTOPOST

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## EEOBs Marked for Auto-Post Audit Report Acronym: EMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Review the EEOBs Marked for Auto-Post Audit Report to determine the user who marked an EEOB for auto-post. Lines included in the report are based on filter criteria selected at run time by the end user.

How to run this report

To run the EEOBs Marked for Auto-Post Audit Report, proceed with the following selections:

Select Audit Reports Option: EMA EEOBs Marked for Auto-Post Audi

t Report

Select division: ALL//

Start Date: T-10 (NOV 27, 2018)

End Date: NOV 27,2018// T (DEC 07, 2018)

(M)EDICAL, (P)HARMACY, (T)RICARE or (A)LL: ALL//

RUN REPORT FOR (A)LL, (S)PECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?: ALL//

Run Report for (S)pecific or (A)ll Users: A// ll

Sort by Insurance Company (N)ame or (U)ser: N// ame

Display in List Manager format? (Y/N): NO//

Export the report to Microsoft Excel? NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

EEOBs Marked for Auto-Post Audit Report Dec 07, 2018@09:25:16 Page: 1

Divs : All

M/P/T: All - All Payers Auto-Post Date: 11/27/18-12/07/18

Users: All Sort: Payer Name

ERA \# Claim \# Trace \#

--------------------------------------------------------------------------------

Auto-Post Date: 12/04/18

Payer: 1621181209/AETNA -CONTINENTAL LIFE INSURANCE COMPANY OF BRENTWOOD

User: USER,ONE

92747.1 442K4059Z9 OU ABC6498633710

92747.2 442K4059WK OU ABC6498633710

92748.1 442K405AG0 OU ABC6498635583

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## Provider Level Adjustments (PLB) Report Acronym: PLB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Run the PLB Report regularly, as determined by your site, to extract report data, as well as view and manage refund requests, for all PLB adjustment codes (FB, WO, 72, IR, J1, L6, CS, WU, etc.)

How to run this report

To run the PLB Report, proceed with the following selections:

Select EDI Lockbox Reports Menu Option: PL Provider Level Adjustments (PLB) Report

Select Division: ALL//

(S)UMMARY or (D)ETAIL FORMAT: SUMMARY// *\<=Defaults to SUMMARY*

SELECT (C)ODE, (R)ANGE of CODEs or (A)LL: ALL//

(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/

Select Insurance Company by NAME or TIN:TIN//NAME

RUN REPORT FOR (A)LL,(S)SPECIFIC, OR (R)ANGE OF INSURANCE COMPANIES?:ALL//SPECIFIC

Select Insurance Company NAME: TRICARE WEST 8169029303

SORT BY (C)ODE or (P)AYER?: CODE// *\<=Defaults to CODE*

START DATE: 08/10/15

END DATE: 8/17/15

DEVICE: HOME// UCX/TELNET Right Margin: 80//

PLB Report – Summary:

EDI LOCKBOX 835 PROVIDER LEVEL ADJUSTMENT (PLB) REPORT - SUMMARY Page: 1

SORT by PLB CODES REPORT RUN DATE: Sep 17, 2015@10:16:15

DIVISION: ALL Codes: ALL

835 PAYERS: ALL 835 PAYER TINs: SELECTED MEDICAL/PHARMACY/TRICARE:TRICARE

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

PAYER NAME/TIN: AETNA/10660X33492

\#ERAs: 1 ADJ: -1% \[ADJ: -50.00/ BILLED: 6102.20\] PAID: 6064.70

-------------------------------------------------------------------------------

ADJ CODE: 51 \# ERAs: 1 ADJ: 0% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -15.00 AMT BILLED: 6102.20 AMT PAID: 6067.20

ADJ CODE TEXT: Interest Penalty Charge

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/10660X33492

\#ERAs: 1 ADJ: 0% \[ADJ: -15.00/ BILLED: 6102.20\] PAID: 6067.20

-------------------------------------------------------------------------------

ADJ CODE: J1 \# ERAs: 2 ADJ: -1% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -101.55 AMT BILLED: 7450.00 AMT PAID: 7013.31

ADJ CODE TEXT: Nonreimbursable

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/10660X33492

\#ERAs: 2 ADJ: -1% \[ADJ: -101.55/ BILLED: 7450.00\] PAID: 7013.31

-------------------------------------------------------------------------------

ADJ CODE: WO \# ERAs: 1 ADJ: -33% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -500.00 AMT BILLED: 1500.55 AMT PAID: 750.55

ADJ CODE TEXT: Overpayment Recovery

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/10660X33492

\#ERAs: 1 ADJ: -33% \[ADJ: -500.00/ BILLED: 1500.55\] PAID: 750.55

-------------------------------------------------------------------------------

ADJ CODE: WU \# ERAs: 2 ADJ: -7% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -294.00 AMT BILLED: 3950.55 AMT PAID: 2955.85

ADJ CODE TEXT: Unspecified Recovery

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/10660X33492

\#ERAs: 2 ADJ: -7% \[ADJ: -294.00/ BILLED: 3950.55\] PAID: 2955.85

-------------------------------------------------------------------------------

PLB Report – Detailed:

EDI LOCKBOX 835 PROVIDER LEVEL ADJUSTMENT (PLB) REPORT - DETAIL Page: 1

SORT by PLB CODES REPORT RUN DATE: Sep 17, 2015@10:18:20

DIVISION: ALL Codes: ALL

835 PAYERS: ALL 835 PAYER TINs: SELECTED MEDICAL/PHARMACY/TRICARE:TRICARE

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

PAYER NAME/TIN: AETNA/10660X33492

\#ERAs: 1 ADJ: -1% \[ADJ: -50.00/ BILLED: 6102.20\] PAID: 6064.70

-----------------------------------------------------------------------------

\#ERA DATE %ADJ ADJUST BILLED PAID CHECK#

TRACE#

REFERENCE#

43551 08/14/15 0 -50.00 6102.20 6064.70

ABC63778X42734

PATIENT CHECK BOUNCED

-------------------------------------------------------------------------------

ADJ CODE: 51 \# ERAs: 1 ADJ: 0% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -15.00 AMT BILLED: 6102.20 AMT PAID: 6067.20

ADJ CODE TEXT: Interest Penalty Charge

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/10660X33492

\#ERAs: 1 ADJ: 0% \[ADJ: -15.00/ BILLED: 6102.20\] PAID: 6067.20

-----------------------------------------------------------------------------

\#ERA DATE %ADJ ADJUST BILLED PAID CHECK#

TRACE#

REFERENCE#

43552 08/17/15 0 -15.00 6102.20 6067.20

ABC63781X39044

INTEREST CHARGE

-------------------------------------------------------------------------------

ADJ CODE: J1 \# ERAs: 2 ADJ: -1% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -101.55 AMT BILLED: 7450.00 AMT PAID: 7013.31

ADJ CODE TEXT: Nonreimbursable

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/10660X33492

\#ERAs: 2 ADJ: -1% \[ADJ: -101.55/ BILLED: 7450.00\] PAID: 7013.31

-----------------------------------------------------------------------------

\#ERA DATE %ADJ ADJUST BILLED PAID CHECK#

TRACE#

REFERENCE#

43543 08/10/15 0 -55.00 2450.00 2205.30

ABC637746X7154

notes here on J1 PLB Adjustment - TW

43544 08/10/15 0 -46.55 5000.00 4808.01

ABC637746X7490

TW entered comments for J1 PLB adjustment

-------------------------------------------------------------------------------

ADJ CODE: WO \# ERAs: 1 ADJ: -33% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -500.00 AMT BILLED: 1500.55 AMT PAID: 750.55

ADJ CODE TEXT: Overpayment Recovery

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/10660X33492

\#ERAs: 1 ADJ: -33% \[ADJ: -500.00/ BILLED: 1500.55\] PAID: 750.55

-----------------------------------------------------------------------------

\#ERA DATE %ADJ ADJUST BILLED PAID CHECK#

TRACE#

REFERENCE#

43540 08/10/15 -33 -500.00 1500.55 750.55

ABC637746X5961

User entered comments here.... TW

-------------------------------------------------------------------------------

ADJ CODE: WU \# ERAs: 2 ADJ: -7% \[TOT AMT ADJUSTED / TOT AMT BILLED\]

AMT ADJUST: -294.00 AMT BILLED: 3950.55 AMT PAID: 2955.85

ADJ CODE TEXT: Unspecified Recovery

-------------------------------------------------------------------------------

PAYER NAME/TIN: AETNA/10660X33492

\#ERAs: 2 ADJ: -7% \[ADJ: -294.00/ BILLED: 3950.55\] PAID: 2955.85

-----------------------------------------------------------------------------

\#ERA DATE %ADJ ADJUST BILLED PAID CHECK#

TRACE#

REFERENCE#

43540 08/10/15 -17 -250.00 1500.55 750.55

ABC637746X5961

wu comments --- TW

43543 08/10/15 0 -44.00 2450.00 2205.30

ABC637746X7154

user comment entered here - TW

-------------------------------------------------------------------------------

## ERAs Posted with Paper EOB Audit Report Acronym: POSR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Review the ERAs Posted with Paper EOB Audit Report on a regular basis, as determined by your site, to identify usage of the Update ERA Posted to EOB option.

How to run this report

To run the ERAs Posted with Paper EOB Audit Report, proceed with the following selections:

Select EDI Lockbox Reports Menu Option: ERAs Posted with Paper EOB Audit Report

Select division: ALL//

START DATE: 1/1/2011 (JAN 01, 2011)

END DATE: JAN 1,2011// T (SEP 20, 2011)

(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/

Export the report to Microsoft Excel? NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

ERAs Posted with Paper EOB - Audit Report Page: 1

Run Date: 9/20/11@16:04:34

DIVISIONS: ALL

Date Range: 1/1/11 - 9/20/11 (DATE ERA UPDATED)

MEDICAL/PHARMACY/TRICARE:TRICARE

Date/Time User Who EFT Match Status

ERA \# Receipt \# ERA Updated Updated Detail Post Status

===============================================================================

14083 1012006 7/27/11@16:19:11 User,Five MATCHED TO PAPER CHECK

MANUALLY POSTED

14094 E11020100 7/29/11@17:50:43 User,Four MATCHED TO PAPER CHECK

MANUALLY POSTED

14201 2362006 9/12/11@14:03:33 User,Four MATCHED TO PAPER CHECK

MANUALLY POSTED

14124 13804836 9/16/11@07:31:28 User,One MATCHED TO PAPER CHECK

MANUALLY POSTED

\*\*\*\*\*\*\*\* END OF REPORT \*\*\*\*\*\*\*\*

## Payer Implementation Report Acronym: PX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Review this report on a regular basis, as determined by your site, to identify all payers that have been associated with ERAs in the system. This report will show all payers, regardless of whether the payer is, or is not, excluded from auto-posting or auto-decreasing.

How to run this report

To run this report, select an output device.

Select EDI Lockbox Reports Menu \<TEST ACCOUNT\> Option: PX Payer Implementation Report

DEVICE: HOME// UCX/TELNET Right Margin: 80//

PAYER IMPLEMENTATION REPORT Page: 1

RUN DATE: 6/10/14@08:15:01

PAYER ID PAYER NAME DATE ADDED

================================================================================

12345678999 INSURANCE PAYER NAME 1 02/03/04

12345678988 INSURANCE PAYER NAME 2 09/01/10

12345678977 INSURANCE PAYER NAME 3 09/29/10

Press enter to continue, '^' to exit:

To run the report, proceed with the following selections:

## CARC/RARC Quick Search Acronym: QS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Run the CARC/RARC Quick Search regularly, as determined by your site, to display all data associated with the entered code.

The CARC/RARC Quick Search displays as follows:

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

When to run this report

Review this report on a regular basis, as determined by your site, to identify all ERAs that have been removed from the Worklist.

How to run this report

To run the report, proceed with the following selections:

Remove ERA from Active Worklist Audit Report

Select Start Date: (W/R/B): Both Dates

START DATE: T-100 (OCT 19, 2011)

END DATE: OCT 19,2011// T (JAN 27, 2012)

(M)EDICAL,(P)HARMACY,(T)RICARE,(A)LL: ALL/

Select division: ALL//

EXPORT THE REPORT TO Microsoft Excel (Y/N): ? NO//

Display in List Manager format? (Y/N): NO//

DEVICE: HOME// TELNET TERMINAL

ERAs Removed from Active Worklist - Audit Report Page 6

Run Date/Time: 1/27/12@10:39:49

DATE RANGE: 10/19/11 - 1/27/12 (Received & Removed)

DIVISIONS: ALL

MEDICAL/PHARMACY/TRICARE: TRICARE

ERA# Payer Name

Date/Time Date ERA Total Amt User Who

Removed Received Paid Removed

================================================================================

14215 PRINCIPAL FINANCIAL GROUP

1/19/12@12:04:04 2/26/07 34.85 User,One

Removed Reason: ERA does not belong; check returned to payer

14241 BANKERS LIFE & CASUALTY

1/18/12@14:35:41 2/26/07 4.66 User,Four

Removed Reason: check was returned to payer before deposited

14244 BANKERS LIFE & CASUALTY

1/27/12@10:11:46 2/26/07 14.07 User,Four

Removed Reason: ERA belongs to another site; check returned to payer

\*\*\*\*\*\*\*\* END OF REPORT \*\*\*\*\*\*\*\*

## Link Payment Tracking Report Acronym:SR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Review this report on a regular basis, as determined by your site, to identify all entries going in and out of Suspense including information on where the payment was dispersed by the user via the Link Payment option.

The LINK PAYMENT TRACKING REPORT displays as follows:

LINK PAYMENT TRACKING REPORT NOV 20, 2017@15:59:29 PAGE 1

FOR THE DATE RANGE: RECEIPT#: E17112005

RECEIPT# TRANS# DATE AMOUNT CLAIM USER DISPOSITION

REASON CLAIMS

--------------------------------------------------------------------------------

E17112005 11/20/17 38.92 PH In Suspense

Multi-Trans Split

K100015 \$15.00

K100007 \$23.92

E17112005 1 11/20/17 15.00 K100015 PH Paid

E17112005 2 11/20/17 23.92 K100007 PH Paid

\*\*\*\*\* END OF REPORT \*\*\*\*\*

## CARC/RARC Table Data Report Acronym: TB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When to run this report

Review this report on a regular basis, as determined by your site, to display all CARC/RARC data that has been transferred from FSC, stored in VistA and available for use.

How to run this report

To run the report, proceed with the following selections:

Select EDI Lockbox Reports Menu Option: TB CARC/RARC Table Data Report

SELECT (N)O CARCS OR (A)LL CARCS: ALL// *\<=Defaults to ALL*

SELECT (N)O RARCS OR (A)LL RARCS: ALL// *\<=Defaults to ALL*

Include (A)ctive codes, (I)nactive codes or (B)OTH?: ACTIVE//*\<=Default ACTIVE*

REPORT DATE: T// *\<=Defaults to T (today)*

DEVICE: HOME// UCX/TELNET Right Margin: 80//

## View/Print ERA Acronym: VP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to select an ERA and print or view its contents.

When to run this report

This option is used on an “as needed” basis.

How to run this report

To run the View/Print Report proceed with the following selections:

Select EDI Lockbox Reports Menu Option: VP View/Print ERA

Select ELECTRONIC REMITTANCE ADVICE ENTRY: 123456TN 03-10-03 704.03

IBinsurance Company One MATCHED

DO YOU WANT TO INCLUDE EXPANDED EEOB DETAIL?: NO// YES \<RET\>

Display in List Manager format? (Y/N): YES//

View/Print ERA - Expanded Detail EDI LOCKBOX WORKLIST - ERA DETAIL 8/7/19 Page: 1

================================================================================

\*\*ERA SUMMARY DATA\*\*

ENTRY: 92737 TRACE NUMBER: TP ABC6496135298

INSURANCE CO ID: 1621181209 ERA DATE: NOV 09, 2018

TOTAL AMOUNT PAID: 1878.97

PAYMENT FROM: AETNA -CONTINENTAL LIFE INSURANCE COMPANY OF BRENTWOOD

FILE DATE/TIME: NOV 09, 2018@09:48:50 RECEIPT: E18110903

EFT MATCH STATUS: MATCHED TO PAPER CHECK

ERA TYPE: ERA INDIVIDUAL EOB COUNT: 1

MAIL MESSAGE: 309660 CHECK \#: TP ABC6496135298

ERA DETAIL POST STATUS: NOT POSTED EXPECTED PAYMENT METHOD CODE: CHK

DATE CHECK MATCHED: NOV 09, 2018 CHECK MATCHED USER: PICKENS,TANYA

\*\*EEOB DETAIL DATA\*\*

SEQUENCE \#: 1 EOB DETAIL: K40581F

AMOUNT PAID: 1878.97 INSURANCE COMPANY ON BILL: BCBS WY\*

FREE TEXT PATIENT NAME: PATIENT, F A

ORIGINAL PATIENT NAME: CLERK, A B

BILLING PROVIDER NPI: 1164471991 RECEIPT:

BILL REFERENCE NUMBER: 442-K40581F

Type \<Enter\> to continue or '^' to exit:

EDI LOCKBOX WORKLIST - ERA DETAIL 8/7/19 Page: 2

================================================================================

PATIENT: PATIENT, F A /8101 CLAIM \#: 442-K40581F

\*\*EOB PROVIDER(S)/NPI CLAIM PROVIDER(S)/NPI\*\*

--------------------- -----------------------

ATTENDING: DOE, JOHN /1518050301

BILLING: /1164471991 XYZ VAMC/1164471991

RENDERING:

\*\*EXCEPTION RESOLUTION LOG DATA\*\*

EOB GENERAL INFORMATION:

Type : NORMAL EOB EOB Paid DT : 11/09/18

Entry Dt/Tm :11/09/18 9:48 am Claim Status : PROCESSED

Entry Dt/Tm :11/09/18 9:48 am Review Status: ACCEPTED-COMPLETE EOB

Entered By : Insurance Seq: SECONDARY

Last Edited : 11/09/18 9:48 am Last Edit By : POSTMASTER

Patient Name: PATIENT, F A Pt. Relation : PATIENT

Insured ID : SUBSC ID 1947268

Type \<Enter\> to continue or '^' to exit:

EDI LOCKBOX WORKLIST - ERA DETAIL 8/7/19 Page: 3

================================================================================

Claim Rec'd Date :

Other Subscriber Name:

PAYER INFORMATION:

Payer Name : BCBS WY\*

Payer Id : 1621181209

ICN : 14705500441

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

1 06/02/14 324 71020 1 300.66 0.00 0.00 0.00 300.66

\# SV DT REVCD PROC MOD UNITS BILLED DEDUCT COINS ALLOW PYMT

2 06/02/14 450 99284 25 1 1442.60 0.00 0.00 0.00 1442.60

\# SV DT REVCD PROC MOD UNITS BILLED DEDUCT COINS ALLOW PYMT

3 06/02/14 730 93005 1 135.71 0.00 0.00 0.00 135.71

Type \<Enter\> to continue or '^' to exit:

## EFT Deposit Reconciliation Report Acronym: DEP 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EFT Deposit Reconciliation Report has been removed from the EDI Lockbox Reports Menu tree.

# National Reports for ePayments Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Diagnostic Measures Reports menu is located under the Finance AR Manager Menu:

Clerk's AR Menu ...

Supervisor's AR Menu ...

<span class="mark">EDI Diagnostic Measures Reports…</span>

Select Finance AR Manager Menu Option:

There are 2 EDI Diagnostic Measure reports plus the Extracts submenu to choose from:

VS EDI VOLUME STATISTICS Report

TD ERA/EFT TRENDING Report

EX EDI Diagnostic Measures Extracts Menu…

Select EDI Diagnostic Measures Reports Option:

## EDI VOLUME STATISTICS Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI VOLUME STATISTICS Report to display metrics on \#837s/NCPDP claims and 835s with \#days between the claim and payment transactions. The report can be run for ALL payers or selected payer(s).

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

--------------------------------------------------------------------------------------

PAYER NAME: AETNA-1 INSURANCE

--------------------------------------------------------------------------------------

NUMBER OF 837s TRANSMITTED TO MEDICAL PAYERS 12345

NUMBER OF NCPDP CLAIMS TRANSMITTED TO PHARMACY PBMs 54321

NUMBER OF 835s RECEIVED FROM MEDICAL PAYERS 10000

NUMBER OF 835s RECEIVED FROM PHARMACY PBMs 1323

NUMBER OF 837 WITH CORRESPONDING 835 (MRA Excluded) 2921

NUMBER OF NCPDP CLAIM WITH CORRESPONDING 835 610

AVG \#DAYS BETWEEN 837 TRANSMIT AND 835 RECEIVED 9.0

AVG \#DAYS BETWEEN NCPDP CLAIM TRANSMIT AND 835 RCVD 14.5

--------------------------------------------------------------------------------------

PAYER NAME: AETNA-2 INSURANCE

--------------------------------------------------------------------------------------

NUMBER OF 837s TRANSMITTED TO MEDICAL PAYERS 100

NUMBER OF NCPDP CLAIMS TRANSMITTED TO PHARMACY PBMs 100

NUMBER OF 835s RECEIVED FROM MEDICAL PAYERS 100

NUMBER OF 835s RECEIVED FROM PHARMACY PBMs 100

NUMBER OF 837 WITH CORRESPONDING 835 (MRA Excluded) 100

NUMBER OF NCPDP CLAIM WITH CORRESPONDING 835 100

AVG \#DAYS BETWEEN 837 TRANSMIT AND 835 RECEIVED 9.0

AVG \#DAYS BETWEEN NCPDP CLAIM TRANSMIT AND 835 RCVD 14.5

--------------------------------------------------------------------------------------

GRAND TOTAL ALL PAYERS

--------------------------------------------------------------------------------------

NUMBER OF 837s TRANSMITTED TO MEDICAL PAYERS 12445

NUMBER OF NCPDP CLAIMS TRANSMITTED TO PHARMACY PBMs 54421

NUMBER OF 835s RECEIVED FROM MEDICAL PAYERS 10100

NUMBER OF 835s RECEIVED FROM PHARMACY PBMs 1423

NUMBER OF 837 WITH CORRESPONDING 835 (MRA Excluded) 3021

NUMBER OF NCPDP CLAIM WITH CORRESPONDING 835 710

AVG \#DAYS BETWEEN 837 TRANSMIT AND 835 RECEIVED 9.0

AVG \#DAYS BETWEEN NCPDP CLAIM TRANSMIT AND 835 RCVD 14.5

Enter RETURN to continue or '^' to exit:

## ERA/EFT TRENDING Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERA/EFT TRENDING Report to display metrics on \#ERAs, \#EEOBs, \#EFTs with \#days between ERA and EFT transactions. The report can be run for ALL payers or selected payer(s).

Select Division: ALL//

SELECT (A)LL PAYERS, (R)ANGE of PAYER NAMES: ALL//

SELECT (A)LL PAYER TINs, (R)ANGE of PAYER TINs: ALL//

Select RATE TYPE NAME: 8 REIMBURSABLE INS. Who's Responsible: INSURER

Print (M)AIN Report, (S)UMMARY by Payer or (G)RAND TOTALS ONLY: GRAND// \<=default

Start with DATE:

Go to DATE:

EXPORT THE REPORT TO Microsoft Excel (Y/N): ? NO// \<= MAIN Report format only

DEVICE: HOME// UCX/TELNET Right Margin: 80//

ERA/EFT TRENDING Report Page: 1

ALL DIVISIONS ALL PAYERS ALL PAYER TINs

DATE RANGE: 01/01/14 – 01/31/15 RUN DATE: 02/07/15@15:30:14

-------------------------------------------------------------------------------- \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO an EFT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

--------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 4

TOTAL AMOUNT BILLED 2212.50

TOTAL AMOUNT PAID 2212.50

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 6.5

AVG \#DAYS BETWEEN ERA/EFT 1.8

AVG \#DAYS BETWEEN ERA+EFT REC’D/PMT POSTED 4.5

AVG \#DAYS BETWEEN BILLED/PMT POSTED 13.0

TOTAL NUMBER OF ERAs 2

TOTAL NUMBER OF EEOBs 214

TOTAL NUMBER OF EFTs 2

TOTAL AMOUNT COLLECTED 2112.50

TOTAL DIFFERENCE BETWEEN ERAs (PAID) – EFTs (COLLECTED): 100.00

-------------------------------------------------------------------------------- \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO a PAPER CHECK \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

--------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 3

TOTAL AMOUNT BILLED 4190.00

TOTAL AMOUNT PAID 4190.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%

AVG \#DAYS BETWEEN BILLED/ERA 5.3

AVG \#DAYS BETWEEN ERA/CHK 6.3

AVG \#DAYS BETWEEN ERA+CHK REC’D/PMT POSTED 5.7

AVG \#DAYS BETWEEN BILLED/PMT POSTED 17.0

TOTAL NUMBER OF ERAs 3

TOTAL NUMBER OF EEOBs 147

TOTAL NUMBER OF EFTs 0

TOTAL AMOUNT COLLECTED 0.0

-------------------------------------------------------------------------------- \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO an EFT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

--------------------------------------------------------------------------------

TOTAL NUMBER OF CLAIMS 2

TOTAL AMOUNT BILLED 90.00

TOTAL AMOUNT PAID 90.00

PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 0%

AVG \#DAYS BETWEEN BILLED/EOB 16.0

AVG \#DAYS BETWEEN EOB/EFT -3.0

AVG \#DAYS BETWEEN EOB+EFT REC’D/PMT POSTED 4.0

AVG \#DAYS BETWEEN BILLED/PMT POSTED 20.0

TOTAL NUMBER OF ERAs 0

TOTAL NUMBER OF EEOBs 0

TOTAL NUMBER OF EFTs 1

TOTAL AMOUNT COLLECTED 90.00

ERA/EFT Trending Report by PAYER /TIN displays as follows:

ERA/EFT TRENDING Report Page: 1ALL DIVISIONS PAYERS:AETNA-1 – AETNA-2 ALL PAYER TINsDATE RANGE: 01/01/14 – 01/31/15 RUN DATE: 02/07/15@15:30:14-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------PAYER NAME/TIN: AETNA-1 INSURANCE/9999X99966X99-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO an EFT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------CLAIM# DOS AMT BILLED AMT PAID BILLED ERA/EOB REC’D EFT/PMT REC’D POSTED TRACE# AUTOPOST/MANUALETRANS TYPE ERA# \#EEOBs EFT# \#DAYS:(BILL/ERA) \#DAYS:(ERA/EFT) \#DAYS:(ERA+EFT REC’D/PMT POSTED) TOTAL \#DAYS(BILLED/PMT POSTED)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------K999991 01/15/15 1200.00 1200.00 01/30/15 02/04/15 02/07/15 02/10/15 123xxx7890 AUTOPOSTERA/EFT 123456 20 555001 5 3 3 11K999992 01/15/15 300.00 300.00 01/30/15 02/04/15 02/07/15 02/17/15 123xxx7890 MANUALERA/EFT 123456 66 555001 5 3 10 18K999994 01/15/15 200.00 200.00 01/30/15 02/06/15 02/05/15 02/10/15 123xxx7890 AUTOPOSTERA/EFT 123458 51 555000 7 -1 4 11K999997 01/15/15 512.50 512.50 01/30/15 02/08/15 02/10/15 02/11/15 123xxx7890 AUTOPOSTERA/EFT 123458 77 555000 9 2 1 12----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO a PAPER CHECK \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------CLAIM# DOS AMT BILLED AMT PAID BILLED ERA/EOB REC’D EFT/PMT REC’D POSTED TRACE# AUTOPOST/MANUALETRANS TYPE ERA# \#EEOBs EFT# \#DAYS:(BILL/ERA) \#DAYS:(ERA/EFT) \#DAYS:(ERA+EFT REC’D/PMT POSTED) TOTAL \#DAYS(BILLED/PMT POSTED)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------K999993 01/15/15 550.00 550.00 01/30/15 02/04/15 02/10/15 02/13/15 123xxx7890 AUTOPOSTERA/PAPER 123500 81 N/A 5 6 3 14K999995 01/15/15 3340.00 3340.00 01/30/15 02/03/15 02/11/15 02/21/15 123xxx7890 MANUALERA/PAPER 123501 22 N/A 4 8 10 22K999996 01/15/15 300.00 300.00 01/30/15 02/05/15 02/10/15 02/14/15 123xxx7890 AUTOPOSTERA/PAPER 123504 44 N/A 6 5 4 15----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO an EFT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------CLAIM# DOS AMT BILLED AMT PAID BILLED ERA/EOB REC’D EFT/PMT REC’D POSTED TRACE# AUTOPOST/MANUALETRANS TYPE ERA# \#EEOBs EFT# \#DAYS:(BILL/ERA) \#DAYS:(ERA/EFT) \#DAYS:(ERA+EFT REC’D/PMT POSTED) TOTAL \#DAYS(BILLED/PMT POSTED)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------K999998 01/15/15 30.00 30.00 01/30/15 02/15/15 02/12/15 02/22/15 123xxx7890 MANUALPAPER/EFT N/A N/A 55700 16 -3 7 23K999999 01/15/15 60.00 60.00 01/30/15 02/15/15 02/12/15 02/16/15 123xxx7890 AUTOPOSTPAPER/EFT N/A N/A 55700 16 -3 1 17-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------PAYER NAME/TIN: AETNA-1 INSURANCE/9999X99966X99-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO an EFT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------TOTAL NUMBER OF CLAIMS 4TOTAL AMOUNT BILLED 2212.50TOTAL AMOUNT PAID 2212.50PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%AVG \#DAYS BETWEEN BILLED/ERA 6.5AVG \#DAYS BETWEEN ERA/EFT 1.8AVG \#DAYS BETWEEN ERA+EFT REC’D/PMT POSTED 4.5AVG \#DAYS BETWEEN BILLED/PMT POSTED 13.0TOTAL NUMBER OF ERAs 2TOTAL NUMBER OF EEOBs 214TOTAL NUMBER OF EFTs 2TOTAL AMOUNT COLLECTED 2212.50TOTAL DIFFERENCE BETWEEN ERAs (PAID) – EFTs (COLLECTED): 100.00----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO a PAPER CHECK \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------TOTAL NUMBER OF CLAIMS 3TOTAL AMOUNT BILLED 4190.00TOTAL AMOUNT PAID 4190.00PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%AVG \#DAYS BETWEEN BILLED/ERA 5.3AVG \#DAYS BETWEEN ERA/CHK 6.3AVG \#DAYS BETWEEN ERA+CHK REC’D/PMT POSTED 5.7AVG \#DAYS BETWEEN BILLED/PMT POSTED 17.0TOTAL NUMBER OF ERAs 3TOTAL NUMBER OF EEOBs 147TOTAL NUMBER OF EFTs 0TOTAL AMOUNT COLLECTED 0.00----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO an EFT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------TOTAL NUMBER OF CLAIMS 2TOTAL AMOUNT BILLED 90.00TOTAL AMOUNT PAID 90.00PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%AVG \#DAYS BETWEEN BILLED/EOB 16.0AVG \#DAYS BETWEEN EOB/EFT -3.0AVG \#DAYS BETWEEN EOB+EFT REC’D/PMT POSTED 4.0AVG \#DAYS BETWEEN BILLED/PMT POSTED 20.0TOTAL NUMBER OF ERAs 0TOTAL NUMBER OF EEOBs 0TOTAL NUMBER OF EFTs 1TOTAL AMOUNT COLLECTED 90.00-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------PAYER NAME/TIN: AETNA-2 INSURANCE/9999X99966X88-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO an EFT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------Claim line items here…..----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO a PAPER CHECK \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------Claim line items listed here…----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO an EFT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------Claim line items listed here…-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------PAYER NAME/TIN: AETNA-2 INSURANCE/9999X99966X88-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------TOTALS BY CATEGORY listed here…..---------------------------------------------------------------------------------Etc…..Etc…..-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------GRAND TOTALS ALL PAYERS--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO an EFT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------TOTAL NUMBER OF CLAIMS 4TOTAL AMOUNT BILLED 2212.50TOTAL AMOUNT PAID 2212.50PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%AVG \#DAYS BETWEEN BILLED/ERA 6.5AVG \#DAYS BETWEEN ERA/EFT 1.8AVG \#DAYS BETWEEN ERA+EFT REC’D/PMT POSTED 4.5AVG \#DAYS BETWEEN BILLED/PMT POSTED 13.0TOTAL NUMBER OF ERAs 2TOTAL NUMBER OF EEOBs 214TOTAL NUMBER OF EFTs 2TOTAL AMOUNT COLLECTED 2212.50TOTAL DIFFERENCE BETWEEN ERAs (PAID) – EFTs (COLLECTED): 100.00----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ERA MATCHED TO a PAPER CHECK \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------TOTAL NUMBER OF CLAIMS 3TOTAL AMOUNT BILLED 4190.00TOTAL AMOUNT PAID 4190.00PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%AVG \#DAYS BETWEEN BILLED/ERA 5.3AVG \#DAYS BETWEEN ERA/CHK 6.3AVG \#DAYS BETWEEN ERA+CHK REC’D/PMT POSTED 5.7AVG \#DAYS BETWEEN BILLED/PMT POSTED 17.0TOTAL NUMBER OF ERAs 3TOTAL NUMBER OF EEOBs 147TOTAL NUMBER OF EFTs 0TOTAL AMOUNT COLLECTED 0.00----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PAPER EOB MATCHED TO an EFT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------TOTAL NUMBER OF CLAIMS 2TOTAL AMOUNT BILLED 90.00TOTAL AMOUNT PAID 90.00PERCENTAGE AMOUNT PAID: (%Total Paid/Billed) 100%AVG \#DAYS BETWEEN BILLED/EOB 16.0AVG \#DAYS BETWEEN EOB/EFT -3.0AVG \#DAYS BETWEEN EOB+EFT REC’D/PMT POSTED 4.0AVG \#DAYS BETWEEN BILLED/PMT POSTED 20.0TOTAL NUMBER OF ERAs 0TOTAL NUMBER OF EEOBs 0TOTAL NUMBER OF EFTs 1TOTAL AMOUNT COLLECTED 90.00

## EDI Diagnostic Measures Extracts Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only option listed on the EDI Diagnostic Measures Extract Menu that is not locked with the security key ‘PRCFA SUPERVISOR’ is View/Print Extracted Reports.

DE Disable-Enable DM Background Job/Reports

VP View/Print Extracted Reports

MN Manually Start DM Extract

TR Manually Transmit DM Extract

Select EDI Diagnostic Measures Extracts Menu Option:

Report Results imported into Excel

With the exception of the Daily Activity Report and the 835 CARC Data Report Filters, the software has been modified to allow the user to export the report from VistA to a text file in order to be imported into Microsoft Excel.

Downloading Reports to Excel

1\. Choose report to print to Excel and enter ‘0;256;999’ at the device prompt. Capture report into a text file.

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

1.  Once you have captured the report data onto a text file, open an Excel document, click on Data tab, choose 'From Text' button located in the 'Get External Data' group

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/011.png)

2.  The dialogue box will come up that will allow you to browse for the text file for which you cut and pasted the data from the VistA session.   Note:  Using a text file with word wrap “off” is recommended.
3.  Click on the import button once you select the text file.
4.  The Text Import Wizard box comes up.  Select ‘delimited’ radio button and click Next.

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/012.png)

5.  Select ‘Other’ from the list of delimiter choices and enter the “^” character in the space provided.   Click ‘next’.

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/013.png)

6.  Select ‘General’ from the list of data formats.  Click ‘finish’.

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/014.png)

7.  Accept the Existing Worksheet default.  Click ‘Ok’.

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/015.png)

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/016.png)

Report Results displayed in List Manager

With the exception of the View/Print ERA Report, the software has been modified to allow the user to view the report in a List Manager format.

Display Report in List Manager Format

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

2.  The report displays in a List Manager format with default actions.

Enter ?? for more actions

Select Action:Quit//??

The following actions are also available:

\+ Next Screen \< Shift View to Left PS Print Screen

\- Previous Screen FS First Screen PL Print List

UP Up a Line LS Last Screen SL Search List

DN Down a Line GO Go to Page ADPL Auto Display(On/Off)

\> Shift View to Right RD Re Display Screen Q Quit

Enter RETURN to continue or '^' to exit:

## *(This page included for two-sided copying.)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Enhancements to non-EDI Lockbox Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Agent Cashier Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Extended Check/Trace/Credit Card Search Acronym: EX

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

1234567 05/09/18 1 SCHIELE,GONZALO L \$ 25.00

1234567 (Check \#)

1010101 05/08/18 1 RYON,GLENNA ELRICH \$ 0.01

12345 (Check \#)

1010101 05/08/18 2 RYON,GLENNA ELRICH \$ 0.02

12345 (Check \#)

E18022200 02/22/18 2 SCHIELE,GONZALO L \$ 10.00

12345 (Check \#)

E17113006 11/30/17 1 442-3M0178 \$ 40.00

12345678901234567890123456789012345678901234567890 (Trace \#)

E17072800b 08/01/17 1 - \$ 13.87

LJC123456789 (Trace \#)

E17030901 03/09/17 1 442-K404UYB \$ 196.43

TPABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890123456789012 (Trace \#)

Total records found: 7

### Link Payment Acronym: LP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/017.png)

Notice the new search options, S1 and S2, under Link Payment:

![](prca-4-5-375-accounts-receivable-epayments-user-manual-edi-lockbox/018.png)

### Link Payment to Multiple Claims 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following screen is displayed when you access Link Payment for further processing of suspense entries.

<u>Link Payments To Accounts Jul 31, 2014@13:11:05 Page: 1 of 129</u>

Transactions for ALL Unapplied Payments

<u>Receipt Tran Unapplied Dep Stat Pay Date Type Ck/Tr/Cd# Amt Paid</u>

1 7080793I 44 7080793I0044 CLOS 03/08/13 CHEC 48363065 963.20

AcctLU: CRdoc: CR-626K3A08CF ACCEPT

2 7080793I 45 7080793I0045 CLOS 03/08/13 CHEC 48363066 666.00

AcctLU: CRdoc: CR-626K3A08CF ACCEPT

3 7080793I 46 7080793I0046 CLOS 03/08/13 CHEC 48363067 473.62

AcctLU: CRdoc: CR-626K3A08CF ACCEPT

4 7080793I 47 7080793I0047 CLOS 03/08/13 CHEC 48363068 138.60

AcctLU: CRdoc: CR-626K3A08CF ACCEPT

5 7080793I 48 7080793I0048 CLOS 03/08/13 CHEC 48363069 54.49

AcctLU: CRdoc: CR-626K3A08CF ACCEPT

6 7081260I 94 7081260I0094 CLOS 04/04/13 CHEC 44234 1421.71

AcctLU: CRdoc: CR-626K3A09U6 ACCEPT

7 7081260I 96 7081260I0096 CLOS 04/04/13 CHEC 44234 3444.37

AcctLU: CRdoc: CR-626K3A09U6 ACCEPT

8 7081407I 11 7081407I0011 CLOS 04/11/13 CHEC 40112515 112.08

\+ Enter ?? for more actions

S1 Search Check/Trace# CS Clear Suspense AP Account Profile

S2 Search Credit Card SR Suspense Report RP Receipt Profile

LP Link Payment SP Show Payment EA Exit Action

You are able to disperse the payment to a single or multiple claims. Additional notes:

- You are required to disperse the ENTIRE payment between multiple claims or nothing is linked and the ENTIRE payment remains in Suspense with no audit records generated. Ultimately, when linking/dispersing payment dollars, the ENTIRE payment must be accounted for or the ENTIRE payment remains in Suspense.
- The software prevents the user from posting dollars to a bill that causes the balance to go below zero. If you try to do so you will receive an error message as in the example below.

> BILL NUMBER: k602vts  TW-RX PAYER 1   ACTIVE   \$567.79

> Amount to apply to Account:  (0.01-20666.66): 2000

> The requested payment is greater than then amount owed please try again.

> Amount to apply to Account:  (0.01-20666.66):

- You are required to enter a Reason text (i.e. Comment) when leaving a portion of the payment in SUSPENSE.

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

The system automatically captures/stores a Final Disposition as Paid or In Suspense as you link payments via Link Payment. This disposition will be displayed in the new Link Payment Tracking Report.

The user may choose to restore the removed suspense EEOB to active status and move EEOB detail to the correct claim.

After payment (bill) selection the user will be asked if the payment has an EEOB.

If the response is YES the following detail will be displayed for the EEOB:

\- Claim Number

\- Trace Number

\- Total Amount Paid

\- Removed By

\- Justification Comment

Users will be prompted to confirm this is the correct EEOB for this payment. On filing, the EEOB will be moved to the correct claim (if the payment claim number is different from the claim on the EEOB) and the EEOB removed status will be cleared.

When using the Link Payment functionality, you must already know the Account Number and the Amounts to be processed. The Link Payment functionality does NOT allow you to search for account information.

### Deposit Processing Acronym: DP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Select Deposit prompt allows you to Select an existing Deposit for review, create a NEW Deposit or Exit.

If there are multiple deposits within the same Deposit ticket# for different dates, the system displays a list of ALL matching Deposit tickets with the Deposit Dates so that you can select one.

The display and prompt are written as follows when there are multiple dates for a single Deposit ticket#:

> Select Deposit: A999999

> 1 A999999 by: ARUSER,ONE on: 01/05/12 Amt: \$ 888.00 CLOSED

> 2 A999999 by: ARUSER,TWO on: 12/06/14 Amt: \$ 725.00 OPEN

> Enter the line# to view an existing deposit or (N) to create a NEW deposit or e(X)it: //

You can create a NEW Deposit ticket \# or view an existing one. You can only add to the Deposit for Today. You will confirm/close the Deposit when appropriate.

> **NOTE:** The user will be able to add a NEW Deposit (with the same Deposit Ticket#) only if the existing Deposit Ticket(s) are on a different date(s) with status = CONFIRMED.

Example Scenarios:

- If the user selects a line#, the selected Deposit displays and follows the existing process for displaying/editing information.
- If the user selects NEW and the Deposit ticket number to be created already exists for today (i.e. Deposit Date), the following error message displays:

> ERROR: Deposit Ticket# already exists for today – Please select the appropriate line \# to modify the existing Deposit or e(X)it to enter a different Deposit Ticket#”.

- If the user selects NEW and the Deposit ticket number to be created does NOT already exist for today (i.e. Deposit Date) AND the previous deposit equals CONFIRMED, the system prompts the user for confirmation before creating a New Deposit:

Add Deposit Ticket# A999999 for today (Y/N)? NO// \<=default=NO

- If the user enters Y, the Deposit Ticket will be created - following existing process for creating the Deposit.
- If the user enters N, the user will return to the “Select Deposit:” prompt.
- If the user selects e(X)it, the system will return to the “Select Deposit:” prompt.

### ### Receipt# Lookup for Pharmacy Claims 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI Lockbox Receipt functionality allows you to enter ECME# or RX# to get the claim# returned. (i.e. you must enter ECME# or Rx# in Receipt when posting payments).

- Within ePayments: the lookup is available after the user creates the receipt.
- Outside of ePayments: the lookup is available in Receipt processing: Action Option: New Payment.

### Edit a Receipt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AR option to edit a receipt has been expanded to allow you to edit the type of payment. This has been specifically tailored for electronic funds processing. You can change the type of payment to CHECK/MO PAYMENT if the receipt status is open and the current value is EDI LOCKBOX and vice versa. You can also change the type of payment from CHECK/MO PAYMENT to EDI LOCKBOX on receipts that have preexisting lines and add/attach a new EFT to the receipt if you have the RCDPEAR key. The system then marks the EFT as unmatched if appropriate. The RCDPEAR key will allow you to change the EFT number on receipts when the TYPE OF PAYMENT equals “EDI LOCKBOX.”

### Auto-Posted Receipt Report Acronym: APR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The APR option allows you to display all auto-posted receipts to ensure payments are posted to patients’ 3rd party claims. Refer to the EDI LOCKBOX (EPAYMENTS) REPORTS MENU section within this document for more information.

*(This page included for two-sided copying.)*

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A unique entry in the Security Key file (^DIC(19.1,) which may prevent access to a specific Option by including the key as part of the options’ entry in the Option file (^DIC (19,). Only users entered in the Holder field of the Security Key file may access the option.

## New or Modified Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RCDPE REMOVE DUPLICATES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New security key RCDPE REMOVE DUPLICATES is utilized to restrict usage of the Remove Duplicate EFT Deposits option. (See Section 6.10 and 6.13 for further information on this security key)

### RCDPE MARK ERA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new security key restricts usage of the Remove ERA from Active Worklist option. (See Section 6.8 for further information on this security key)

### PRCADJ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing security key PRCADJ has been modified to lock the Adjust (Inc/Dec) action of the ERA Worklist Research Menu to restrict its usage. This key should only be given to supervisory personnel. (See Section 3.3.3.1 for further information on this security key)

### RCDPE AGED PMT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New security key RCDPE AGED PMT is utilized to restrict usage of the Unposted EFT Override option. (See Section 6.14 for further information on this security key)

### RCDPE ERA EXCEPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New security key RCDPE ERA EXCEPT is utilized to restrict usage of the Delete Message action from the EDI Lockbox 3rd Party Transmission Exceptions. (See Section 3.2.1.1 for further information on this security key)

### RCDPE AUTO DEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New security key RCDPE AUTO DEC is utilized to restrict usage of all options on the EDI Lockbox Parameters menu. (See Section 2.2 for further information on this security key)

### RCDPE REMOVE EEOB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New security key RCDPE REMOVE EEOB is utilized to restrict usage of the Remove option on the new EEOB Move/Copy/Remove option. (See Section 6.9 for further information on this security key)

### RCDPEAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security key RCDPEAR is utilized to restrict usage of the Admin Cost Adj and Re-establish Bill actions on both the ERA Worklist Scratch Pad Research Menu and the Auto-Post Awaiting Resolution (APAR) Scratch Pad Research Menu. (See Sections 2.1.2 and 3.5 respectively for further information on this security key)

Security key RCDPEAR is utilized when editing a receipt to change the TYPE OF PAYMENT from CHECK/MO PAYMENT to EDI LOCKBOX on receipts that have preexisting lines and allow a clerk to add/attach a new EFT to the receipt. It will also allow clerks to change the EFT number on receipts when the TYPE OF PAYMENT equals EDI LOCKBOX.

### RCDPEPP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security key RCDPEPP is utilized to restrict usage of the Mark for Auto Post, Refresh Scratch Pad, Look at Receipt, Verify, and Receipt Processing actions on the ERA Worklist and ERA Worklist Scratch Pad. Also, the security key RCDPEPP is utilized to restrict the usage of the Split/Edit a Line, Mark for Auto Post and Verify actions on the Auto-Post Awaiting Resolution (APAR) Scratch Pad. (See Sections 2.1.1 / 2.1.2 and 3.5 respectively for further information on this security key.)

### PRCFA SUPERVISOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing security key PRCFA SUPERVISOR has been removed as a lock for the option EDI Diagnostic Measures Reports menu which is located under the Finance AR Manager Menu. The following options have been modified to be locked with the existing PRCFA SUPERVISOR security key:

- Disable-Enable DM Background Job/Reports
- Manually Start DM Extract
- Manually Transmit DM Extract

### RCDPE PAYER IDENTIFY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security key RCDPE IDENTIFY allows users to identify payers as being Tricare only, Pharmacy only, both or none. This functionality is accessed when choosing the Identify Payers option on the EDI Lockbox menu.

*(This page included for two-sided copying.)*

# APPENDIX A – Helpful Links 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistaU – Vista University has online training and documentation for a number of Training Initiatives including ePayments

REDACTEDRevenue Guide - Provides a uniform and standard set of educational and reference materials for the benefit of Revenue Cycle staff and management.

REDACTEDWashington Publishing – Provider of services, publications and products to entities that develop or consume Electronic Data Interchange Standard Transaction

[http://www.wpc-edi.com/custom_html/claimadjustment.htm](http://www.wpc-edi.com/custom_html/claimadjustment.htm)

ePay Rapid Response Team – email group including POC’s, ePay team, FSC, and EPS. Provides responses to questions from the field

[VHAePaymentsRRT@va.gov](mailto:VHAePaymentsRRT@va.gov)

TMS VA Talent Management System (Formerly LMS – VA Learning Management System)

[https://www.tms.va.gov/plateau/user/login.jsp](https://www.tms.va.gov/plateau/user/login.jsp)

*(This page included for two-sided copying.)*

# APPENDIX B – Claim Level Adjustment Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CLAIM ADJUSTMENT GROUP CODE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Code identifying the general category of payment adjustment 1100.

CODE DEFINITION

| Code | Definition             | Description                                                                                                                                                                                                                                 |
|----------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CO   | Contractual Obligations    | Used when a joint payer/payee contractual agreement or a regulatory requirement resulted in an adjustment.                                                                                                                                      |
| CR   | Correction and Reversals   | Used for corrections and reversals to PRIOR claims                                                                                                                                                                                              |
| OA   | Other adjustments          |                                                                                                                                                                                                                                                 |
| PI   | Payer Initiated Reductions | Used when, in the opinion of the payer, the adjustment is not the responsibility of the patient, but there is no supporting contract between the provider and the payer (i.e., medical review or professional review organization adjustments). |
| PR   | Patient Responsibility     |                                                                                                                                                                                                                                                 |

*(This page included for two-sided copying.)*

## # APPENDIX C – Provider Level Adjustment Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PROVIDER LEVEL ADJUSTMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Provider Level Adjustment Reason Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Code indicating reason for debit or credit memo or adjustment to invoice, debit or credit memo, or payment

CODE and DEFINITION

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 22%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Code</strong></th>
<th><strong>Definition</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>50</strong></td>
<td>Late Charge</td>
<td>Code for the Late Claim Filing Penalty or Medicare Late Cost Report Penalty. PLB03-2 identifies the Medicare Late Cost Report Penalty with a code value of LR.</td>
</tr>
<tr class="even">
<td><strong>51</strong></td>
<td>Interest Penalty Charge</td>
<td>Code for the interest assessment for late filing. Medicare Part A provides code “IP” in PLB03-2.</td>
</tr>
<tr class="odd">
<td><strong>72</strong></td>
<td>Authorized Return</td>
<td>Monetary amount is the provider refund adjustment. This adjustment acknowledges a refund received from a provider for previous overpayment. PLB03-2 should always contain an identifying reference number when the value is used. PLB04 should contain a negative value. This adjustment should always be offset by some other PLB adjustment referring to the original refund request or reason. For balancing purposes, the amount related to this adjustment reason code must be directly offset. Medicare A will provide code “PR” in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>90</strong></td>
<td>Early Payment Allowance</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>AM</strong></td>
<td>Applied to Borrower’s Account</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information. Use this monetary amount for the loan repayment amount.</td>
</tr>
<tr class="even">
<td><strong>AP</strong></td>
<td>Acceleration of Benefits</td>
<td>Code to reflect accelerated payment amounts or withholdings. Withholding or payment identification is indicated by the sign of the amount in PLB04. A positive value represents a withholding. A negative value represents a payment. Medicare Part A will provide code “AP” for accelerated payment amounts and code “AW” for accelerated payment withholdings in PLB03-2.</td>
</tr>
<tr class="odd">
<td><strong>B2</strong></td>
<td>Rebate</td>
<td>Code for the refund adjustment. Medicare Part A will provide code “RF” in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>B3</strong></td>
<td>Recovery Allowance</td>
<td>Code is used by Medicare to represent the check received from the provider for overpayments generated by payments from other payers. This code differs from the provider refund adjustment identified with code 72. Part A or Part B trust fund for Medicare use is identified in PLB03-2. “RA” is used for Medicare A. “RB” is used for Medicare Part B. PLB04 should contain a NEGATIVE value. This adjustment should always be offset by some other PLB adjustment referring to the original refund request or reason. For balancing purposes, the amount related to this adjustment reason code must be directly offset.</td>
</tr>
<tr class="odd">
<td><strong>BD</strong></td>
<td>Bad Debt Adjustment</td>
<td>Code for the bad debt pass-through. Medicare Part A will provide code “BD” in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>BN</strong></td>
<td>Bonus</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</td>
</tr>
<tr class="odd">
<td><strong>C5</strong></td>
<td>Temporary Allowance</td>
<td>Tentative adjustment. Medicare Part A will provide code “TS” in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>CR</strong></td>
<td>Capitation Interest</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</td>
</tr>
<tr class="odd">
<td><strong>CS</strong></td>
<td>Adjustment</td>
<td>Provide supporting identification information in PLB03-2. Medicare Part A will provide code “CA” for Manual Claim Adjustment, “AA” for Receivable Today. Medicare Part A and Part B will provide code “RI” for Reissued Check Amount in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>CT</strong></td>
<td>Capitation Payment</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</td>
</tr>
<tr class="odd">
<td><strong>CV</strong></td>
<td>Capital Passthru</td>
<td>Medicare Part A will provide code “CP” in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>CW</strong></td>
<td>Certified Registered Nurse Anesthetist Passthru</td>
<td>Medicare Part A will provide code “CR” in PLB03-2.</td>
</tr>
<tr class="odd">
<td><strong>DM</strong></td>
<td>Direct Medical Education Passthru</td>
<td>Medicare Part A will provide code “DM” in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>E3</strong></td>
<td>Withholding</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information. Medicare Part A will provide code “CW” in PLB03-2.</td>
</tr>
<tr class="odd">
<td><strong>FB</strong></td>
<td>Forwarding Balance</td>
<td>Monetary amount for the balance forward. A negative value in PLB04 represents a balance moving forward to a future payment advice. A positive value represents a balance being applied from a previous payment advice. A reference number should be supplied in PLB03-2 for tracking purposes. Medicare Part A will provide code “BF” for negative values and “CO” for positive values in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>FC</strong></td>
<td>Fund Allocation</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information. The specific fund should be identified in PLB03-2.</td>
</tr>
<tr class="odd">
<td><strong>GO</strong></td>
<td>Graduate Medical Education Passthru</td>
<td>Medicare Part A will provide code “GM” in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>IP</strong></td>
<td>Incentive Premium Payment</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</td>
</tr>
<tr class="odd">
<td><strong>IR</strong></td>
<td>Internal Revenue Service Withholding</td>
<td></td>
</tr>
<tr class="even">
<td><strong>IS</strong></td>
<td>Interim Settlement</td>
<td>Number for the interim rate lump sum adjustment. Medicare Part A will provide code “IR” in PLB03-2.</td>
</tr>
<tr class="odd">
<td><strong>J1</strong></td>
<td>Nonreimbursable</td>
<td>Offset claim or service level data that reflects what could be paid if not for demonstration program or other limitation that prevents issuance of payment.</td>
</tr>
<tr class="even">
<td><strong>L3</strong></td>
<td>Penalty</td>
<td>Number for the capitation-related penalty, penalty withholding, or penalty release adjustment. Withholding or release is identified by the sign in PLB04. See 2.2.10, Capitation and Related Payments or Adjustments, for additional information. Medicare Part A will provide code “PW” for Penalty Withhold, “RS” for Penalty Release, and “SW” for Settlement Withhold Amount in PLB03-2.</td>
</tr>
<tr class="odd">
<td><strong>L6</strong></td>
<td>Interest Owed</td>
<td>Monetary amount for the interest paid on claims in this 835. Support the amounts related to this adjustment by 2-062 AMT amounts, where AMT01 is “I.”Medicare Part A will provide code “IN” in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>LE</strong></td>
<td>Levy</td>
<td>IRS Levy</td>
</tr>
<tr class="odd">
<td><strong>LS</strong></td>
<td>Lump Sum</td>
<td><p>Disproportionate share adjustment, indirect medical education pass-through, non-physician pass-through, pass-through lump sum adjustment, or other pass-through amount. The specific type of lump sum adjustment must be identified in PLB03-2. Medicare Part A will provide code:</p>
<blockquote>
<p>“DS” for Disproportionate Share Adjustment,</p>
<p>“IM” for Indirect Medical Education Passthrough</p>
<p>“NP” for Non-physician Passthrough</p>
<p>“PS” for Passthrough Lump Sum</p>
<p>“PO” for Other Passthrough in PLB03-2.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OA</strong></td>
<td>Organ Acquisition Passthru</td>
<td>Medicare Part A will provide code “KA” in PLB03-2.</td>
</tr>
<tr class="odd">
<td><strong>OB</strong></td>
<td>Offset for Affiliated Providers</td>
<td>Part A or Part B trust fund identification for the source of the offset is in PLB03-2. Use “OA” for the Part A trust fund and “OB” for the Part B trust fund in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>PI</strong></td>
<td>Periodic Interim Payment</td>
<td><p>Monetary amount for the PIP lump sum, PIP payment, or adjustment after PIP. The sign of the amount in PLB04 determines whether this is a payment (negative) or adjustment (positive). Medicare Part A will provide code:</p>
<blockquote>
<p>“PL” for PIP Lump Sum</p>
<p>“PP” for PIP Payment</p>
<p>“PA” for Adjustment After PIP in PLB03-2.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PL</strong></td>
<td>Payment Final</td>
<td>Number for the final settlement. Medicare Part A will provide code “FS” in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>RA</strong></td>
<td>Retro-activity Adjustment</td>
<td>See 2.2.10, Capitation and Related Payments and Adjustments, for additional information. Medicare Part A will provide code “TR” in PLB03-2.</td>
</tr>
<tr class="odd">
<td><strong>RE</strong></td>
<td>Return on Equity</td>
<td>Medicare Part A will provide code “RE” in PLB03-2.</td>
</tr>
<tr class="even">
<td><strong>SL</strong></td>
<td>Student Loan Repayment</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>TL</strong></td>
<td>Third Party Liability</td>
<td>See 2.2.10, Capitation and Related Payments or Adjustments, for additional information.</td>
</tr>
<tr class="even">
<td><strong>WO</strong></td>
<td>Overpayment Recovery</td>
<td>Use for the recovery of previous overpayment. An identifying number should be provided in PLB03-2. See the notes on codes 72 and B3 for additional information about balancing against a provider refund. Medicare Part A will provide code “OR” in PLB03-2.</td>
</tr>
</tbody>
</table>

*(This page included for two-sided copying.)*

# APPENDIX D - Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term                                                                 | Definition                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Austin Information Technology Center (formerly Austin Automation Center) | Repository for databases located in Austin, Texas.                                                                                                                                                                                                                                         |
| Accounts Receivable                                                      | The financial computer system used by the Department of Veterans Affairs Medical Centers.                                                                                                                                                                                                  |
| Financial Management System                                              | The financial computer system used by the Department of Veterans Affairs.                                                                                                                                                                                                                  |
| Software Requirements Specifications                                     | Document that outlines the functionality requirements for a project.                                                                                                                                                                                                                       |
| Routines                                                                 | A unique identifiable containment of software pertinent to a computer system function. The routines contain the programming logic to implement the functionality for the EDI Lockbox Project.                                                                                              |
| Data Dictionary                                                          | The structure of a file, table or any group of related information as defined for and by VA FileMan.                                                                                                                                                                                       |
| MailMan Message                                                          | The messaging system used to communicate between the users of the VISTA software. MailMan messages will be used to process automatic payments and to communicate between the Accounts Receivable software and the users.                                                                   |
| Related SRS Module                                                       | The numeric and title of the functionality requested in the SRS, which the SDD is implementing.                                                                                                                                                                                            |
| Mail Group                                                               | A VA MailMan structure that defines a subset of VA MailMan users. A Mail Group is used to communicate with a group of users. The Mail Group user subset can easily be modified without having to change software logic.                                                                    |
| Security Key                                                             | A unique entry in the Security Key file (^DIC(19.1,) which may prevent access to a specific Option by including the key as part of the options’ entry in the Option file (^DIC(19,). Only users entered in the Holder field of the Security Key file may access the option.                |
| Option                                                                   | A unique method defined in the Option file (^DIC(19,). Options are usually defined as part of a user driven menu system but may be invoked as extensions of other options or VA MailMan messages.                                                                                          |
| List Manager Screen                                                      | A graphical user interface program used by VISTA to present data to the users. From the List Manager Screen, the user can select options programmed and set up for the data displayed.                                                                                                     |
| Integration Agreement                                                    | Programming agreements made between two VISTA packages enabling the sharing/management of data and or functions.                                                                                                                                                                           |
| Implementation Manager                                                   | The person or group whose function is to field questions and solve problems for the sites that are data or process related to transmissions from EDI Lockbox.                                                                                                                              |
| ERA                                                                      | Electronic Remittance Advice                                                                                                                                                                                                                                                               |
| Electronic Remittance Advice                                             | An electronic record transmitted to the sites with EEOB detail information included. An Electronic Remittance Advice can consist of one or more EEOBs from one payer.                                                                                                                      |
| EOB                                                                      | Explanation Of Benefits                                                                                                                                                                                                                                                                    |
| EEOB                                                                     | Electronic Explanation Of Benefits                                                                                                                                                                                                                                                         |
| Explanation Of Benefits                                                  | A document from a payer that details the amount of payment on a claim and if not paid in full, the reasons for it.                                                                                                                                                                         |
| Insurance Company ID                                                     | ID associating each transaction with the payer; typically the payer’s tax ID number and is not related to any other Payer ID stored in VistA for other purposes.                                                                                                                           |
| FSC                                                                      | Financial Services Center; located in Austin, Texas; FSC runs GENTRAN translator software on FSC servers; FSC servers parse incoming EFT and ERA data and routes data to the appropriate VistA AR system based on Provider Tax ID information within each transaction                      |
| GENTRAN                                                                  | Software used to translate incoming 835 data into VistA readable flat file data; software is loaded onto FSC server                                                                                                                                                                        |
| AITC                                                                     | Austin Information Technology Center (AITC) located in Austin, Texas; responsible for maintaining the hardware that supports the Lockbox system, including FSC servers, the Mailman routing system, and EPHRA database                                                                     |
| EPHRA                                                                    | EEOB and Payment Healthcare Resolution Application; Web-based archival repository and research tool; allows user to search for missing EEOBs that are not received due to incorrect routing information; allows Austin FSC 224-unit staff to route unroutable EEOB data                    |
| Posted ERA                                                               | Indicates the AR processing is complete                                                                                                                                                                                                                                                    |
| Unposted ERA                                                             | Indicates the AR processing is not complete; an unposted ERA needs to be processed, closed, and posted, just like a paper EOB that must be verified and/or adjusted before closing                                                                                                         |
| Matched                                                                  | An ERA that has been associated with an EFT, a paper check, or a zero dollar payment                                                                                                                                                                                                       |
| Not matched                                                              | An ERA that has not yet been associated with an EFT, a paper check, or a zero dollar payment; user will always select unmatched when searching for an ERA that should match the paper check received                                                                                       |
| Worklist                                                                 | A listing of all ERA information sent from payers. It can be viewed by posted or unposted ERA’s, specific payers, and matched or not matched ERA’s.                                                                                                                                        |
| Sequence number                                                          | A sequential number assigned in VistA to each incoming ERA                                                                                                                                                                                                                                 |
| ICN                                                                      | Internal control number. This number is sent by the payer and is unique to each payer and identifies the claim in the payers system. It can be given by AR to the customer service representative at the payer to help locate the information in the payer’s system.                       |
| Transaction and code sets                                                | Standard for Electronic transactions set forth by HIPAA. Compliance is mandatory for payers, providers, clearinghouses or anyone who receives or submits electronic health information.                                                                                                    |
| 835                                                                      | HIPAA standard terminology for an electronic health care claim payment or remittance advice                                                                                                                                                                                                |
| Scratchpad                                                               | VistA screen containing ERA \#, name and ID of payer, amount paid, and the trace number. The scratchpad also contains list manager options that conveniently store frequently used AR/ePay options in one centralized location.                                                            |
| FMS                                                                      | Financial Management System. FMS interacts with VistA to manage VHA financial data.                                                                                                                                                                                                        |
| CR document                                                              | Credit document; credits funds to site via FMS                                                                                                                                                                                                                                             |
| TR document                                                              | Transfer document; transfers funds to appropriate revenue source code                                                                                                                                                                                                                      |
| IB                                                                       | Integrated Billing Package                                                                                                                                                                                                                                                                 |
| POC                                                                      | Point of Contact. The ePay network includes an ePay POC per VISN.                                                                                                                                                                                                                          |
| VistaU                                                                   | Vista University has online training and documentation for a number of Training Initiatives including ePayments.                                                                                                                                                                           |
| Auto-Post                                                                | VistA runs a nightly job to automatically post third party medical claims by creating and processing receipts for EEOBs that meet auto-posting criteria.                                                                                                                                   |
| APAR List                                                                | Auto-Post Awaiting Resolution list of EEOBs that were processed by the auto posting nightly job, but the system was unable to create and process a receipt.                                                                                                                                |
| Auto-Decrease                                                            | VistA runs a nightly job to automatically make a decrease adjustment to a third-party medical claim or pharmacy claims with payments that meet auto-decrease criteria. The automatic decrease is made with a contractual decrease adjustment amount that brings the claim balance to zero. |

*(This page included for two-sided copying.)*

# APPENDIX E – 3<sup>rd</sup> Party EDI Lockbox Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3<sup>rd</sup> Party EDI Lockbox BulletinsSubject of Bulletin / When it’s generated/ How to resolve

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ERRONEOUS TAX ID ON ERA</td>
<td></td>
</tr>
<tr class="even">
<td>Message sent when the payer sends an ERA to the EDI Lockbox bank and they do not include a valid V.A. tax id on the transmission. In order to correctly route the data to the proper site, the tax id number must be corrected before the data is transmitted to the site by either EPHRA or the EDI Lockbox group in Austin. If this occurs, this bulletin is received by the site to alert them that the payer has either omitted or has an erroneous tax id for the site.</td>
<td>What to do: Contact the insurance company and provide them with the correct tax id for the site.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>EDI LOCKBOX SERVER OPTION ERROR</strong></td>
</tr>
<tr class="even">
<td><p>Message sent when the EDI Lockbox system receives a message where:</p>
<ol type="1">
<li><p>Message code is invalid for EDI Lockbox</p></li>
<li><p>This message has no ending $ or 99 record.</p></li>
<li><p>Message file problem - no message stored.</p></li>
<li><p>Message file problem - message partially stored.</p></li>
<li><p>Invalid mail group designated for EDI Lockbox errors</p></li>
<li><p>Message header error – the format of the header record on an EFT or ERA was not correct.</p></li>
</ol></td>
<td>What to do: For all situations, contact your IRM as there may be mailman or server problems or EVS if there are software errors.</td>
</tr>
</tbody>
</table>

|                                                                                                                                                                             |                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| EDI LBOX ALERT - ERA/EFT NOT FROM AUSTIN                                                                                                                                |                                                                                                                                                       |
| Message sent when an ERA or EFT is received by the EDI Lockbox system and the message did not come from Austin.                                                             | What to do: Contact your IRM to report this possible breach of security                                                                               |
| EDI LBOX - EEOB FROM \<site name\> FOR \<payer name\>                                                                                                                   |                                                                                                                                                       |
| Message sent when an EEOB is transferred into your site from another site that received it in error.                                                                        | What to do: In EDI Lockbox Data Exception Processing, find the EEOB and accept it as yours (via file EEOB) or delete it if it does not belong to you. |
| TOTALS MISMATCH ON EFT-ERA MATCH                                                                                                                                        |                                                                                                                                                       |
| Message sent when an EFT and an ERA are matched with the same trace number and insurance company id number, but the totals indicated on the 2 records do not match.         | What to do: Contact the payer to determine why this has occurred.                                                                                     |
| DUPLICATE EFT DEPOSIT RECORD RECEIVED                                                                                                                                   |                                                                                                                                                       |
| Message sent when the EDI Lockbox server receives an EFT message and VistA already has a deposit and receipt posted to FMS for the deposit ticket \# referenced by the EFT. | What to do: Report this to your IRM and the implementation manager to determine why it happened.                                                      |

Subject of Bulletin / When it’s generated/ How to resolve

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>EXCEPTIONS EFT DEPOSIT AND MATCH EFTs TO ERAs &lt;date&gt;</strong></td>
</tr>
<tr class="even">
<td>Message sent when exceptions are encountered when the system attempts to post EFT deposits or to match EFTs with ERAs.</td>
<td></td>
</tr>
<tr class="odd">
<td><p>A. Nightly via the EDI Lockbox nightly job that creates and processes the deposit for any EFTs received and not yet posted and that attempts to match unmatched ERA records to unmatched EFT records. If no exceptions are found, this is stated in the bulletin.</p>
<p>Exception conditions include:</p>
<ol type="1">
<li><p>The nightly job to post EFT deposits and match EFTs to ERAs could not be run because another match process was already running.</p></li>
<li><p>An invalid checksum value was found for an EFT on file and the EFT deposit was not sent to FMS.</p></li>
<li><p>A deposit or a receipt could not be added for an EFT. The EFT deposit was not sent to FMS.</p></li>
</ol></td>
<td><p>What to do:</p>
<ol type="1">
<li><p>Only 1 process to match ERAs to EFTs may be running at any given time. If happening on the manual process, try again later. If on the nightly job or the problem persists, show the bulletin to your IRM as they can research the problem.</p></li>
<li><p>This indicates the EFT record was modified since it was stored in VistA. IRM should be notified of the problem and the EFT will need to be retransmitted to the site from Austin (the existing record will be overwritten with the retransmitted data</p></li>
<li><p>This indicates a data problem with the record or a software problem. Ask Austin to retransmit. If the problem persists, contact your IRM and/or EVS</p></li>
</ol></td>
</tr>
<tr class="even">
<td colspan="2">EDI LOCKBOX TOTALS RECORD EXCEPTION</td>
</tr>
<tr class="odd">
<td>Message sent when the EDI Lockbox server stores an ERA record in different parts. Each EEOB within the ERA is stored in IB in the EXPLANATION OF BENEFITS file. All the detail pertaining to payment made regarding the claim is stored here. The ERA total amount paid and all detail not pertaining to an individual claim is stored in A/R. This exception is received when the ERA totals record cannot be stored in A/R.</td>
<td>What to do: Contact EVS.</td>
</tr>
<tr class="even">
<td colspan="2">AR LOCKBOX ERA UNMATCHED AGING REPORT FOR &lt;date&gt;</td>
</tr>
<tr class="odd">
<td>When received: Produced by the nightly EDI Lockbox job. It contains an ERA UNMATCHED AGING summary report.</td>
<td>What to do: This is FYI only. No action is needed.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>AR LOCKBOX EFT UNMATCHED AGING REPORT FOR &lt;date&gt;</strong></td>
</tr>
<tr class="odd">
<td>When received: Produced by the nightly EDI Lockbox job. It contains an EFT UNMATCHED AGING summary report.</td>
<td>What to do: This is FYI only. No action is needed.</td>
</tr>
</tbody>
</table>

  
Subject of Bulletin / When it’s generated/ How to resolve

|                                                                                                                                                                                                |                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| AUTO DAILY ACTIVITY SUMMARY REPORT - \<date\>                                                                                                                                                  |                                                                                               |
| When received: Produced by the nightly EDI Lockbox job. It contains a daily activity report indicating the matches made and the EFT deposits created/posted to FMS.                            | What to do: This is FYI only. No action is needed.                                            |
| INVALID EFT DEPOSIT NUMBER                                                                                                                                                                 |                                                                                               |
| When received: When the EDI Lockbox server receives an EFT whose deposit number does not start with a 469 or HAC.                                                                              | What to do: Contact the implementation manager.                                               |
| ELECTRONIC EDI LOCKBOX MESSAGE DELETED                                                                                                                                                         |                                                                                               |
| When received: Any time a user uses the delete message action within EDI Lockbox transmission exception processing to delete an exception message.                                             | What to do: FYI – you might want to follow up to be sure the deletion was justified.          |
| ELECTRONIC EEOB DETAIL EXCEPTION REMOVED                                                                                                                                                       |                                                                                               |
| Any time a user uses the delete message action within EDI Lockbox data exception processing to delete an exception message.                                                                    | What to do: FYI – you might want to follow up to be sure the exception removal was justified. |
| LOCKBOX EEOB DETAIL RE-FILE ATTEMPTED TO IB                                                                                                                                                |                                                                                               |
| When received: When an attempt is made to re-file an EEOB that could not be stored in IB due to a data exception by using the FILE EEOB in IB action in EDI Lockbox Data Exception Processing. | What to do: FYI only. No action required.                                                     |

|                                                                                                    |                                                      |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------|
| Unmatched ERAs \> 30 days                                                                          |                                                      |
| The listed ERAs were received more than 30 days ago and have not yet been matched.                 | What to do: Review the ERAs and expedite processing. |
| Matched/Not Posted ERAs \> 30 days                                                                 |                                                      |
| The listed ERAs were received more than 30 days ago and have been matched but have not been posted | What to do: Review the ERAs and expedite processing. |
| EFTs greater than 14 days                                                                          |                                                      |
| The listed EFTs were received more than 14 days ago                                                | What to do: Review the EFTs and expedite processing. |

|                                                                                      |                                                                                              |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| EDI CARC_RARC SERVER OPTION ERROR                                                    |                                                                                              |
| When received: Any time an error is found while processing CARC & RARC data from FSC | What to do: Review the type of errors report and expedite processing with FSC and local IRM. |

# Solving ePayment Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to Remove Aged EFT’s from the EFT Unmatched Aging Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM can use the following process to change the status of an EFT to “PAPER EOB MATCH”, which will allow the EFT to fall off the aged EFT report. A complete trace number(s) is needed in order to complete the process.

Due to database integrity issue, IRM may elect not to do this workaround.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VA FileMan Version 22.0</p>
<p>1 Enter or Edit File Entries</p>
<p>2 Print File Entries</p>
<p>3 Search File Entries</p>
<p>5 Inquire to File Entries</p>
<p>8 Data Dictionary Utilities ...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select VA FileMan Option: ENTER or Edit File Entries

INPUT TO WHAT FILE: (file needed)

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

EDIT WHICH FIELD: ALL// .08 MATCH STATUS

THEN EDIT FIELD:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select EDI THIRD PARTY EFT DETAIL EFT TRANSACTION: &lt;enter trace number&gt;</p>
<p>MATCH STATUS: UNMATCHED// ?</p>
<p>Enter the status to indicate if the payment has been matched to an ERA.</p>
<p>Choose from:</p>
<p>-1 MATCHED WITH ERRORS</p>
<p>0 UNMATCHED</p>
<p>1 MATCHED</p>
<p><strong>2 PAPER EOB MATCH</strong></p>
<p>MATCH STATUS: MATCHED// 2 PAPER EOB MATCH</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

[^1]: