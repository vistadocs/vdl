---
title: Accounts Receivable Version 4.5 User Manual - Cross Servicing Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Cross Servicing Menu
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
menu_options: 7
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - cross
  - servicing
  - class
  - debtor
  - debt
  - bill
  - span
  - table
  - contents
  - referred
page_count: 0
word_count: 30062
section_count: 51
table_count: 20
figure_count: 8
appendix_count: 6
has_toc: False
is_stub: False
pub_date: January 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_ar_cs_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_ar_cs_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

---
title: |
  <span id="_Hlk169268571" class="anchor"></span>Veterans’ Health Administration (VHA) Finance Integrated Billing (IB) and Accounts Receivable (AR)

  <span id="_Hlk169268572" class="anchor"></span>Cross-Servicing User Manual
---

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/001.png)

January 2025

Revision History

<table>
<caption><p><span id="_Toc169093103" class="anchor"></span>Table A‑1: Cross-Servicing Record Types &amp; Action Codes</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 56%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01/2025</td>
<td>1.7</td>
<td><p>Updated for patch PRCA*4.5*412.</p>
<p>Creates a new report, Multiple Referral Programs Report [PRCAC MULT REF RPT], that identifies any bills that may be referred for debt collection to multiple debt referral programs.</p></td>
<td>IBAR Team</td>
</tr>
<tr class="even">
<td>06/2024</td>
<td>1.6</td>
<td><p>Updated for patch PRCA*4.5*433.</p>
<p>Adds the Accounts Receivable Category field to the following Cross-Servicing reports:</p>
<ul>
<li><blockquote>
<p>Cross-Servicing Bill Report [RCTCSP BILL REPORT]</p>
</blockquote></li>
<li><blockquote>
<p>Cross-Servicing Re-Referred Bills Report [RCTCSP REREFER BILL REPORT]</p>
</blockquote></li>
<li><blockquote>
<p>Cross-Servicing Recall Report [RCTCSP RECALL REPORT]</p>
</blockquote></li>
<li><blockquote>
<p>Cross-Servicing Stop Reactivate Report [RCTCSP STOP REACTIVATE REPORT]</p>
</blockquote></li>
<li><blockquote>
<p>Debt Referral Reject Report [RCTCSP REJECT REPORT]</p>
</blockquote></li>
<li><blockquote>
<p>Print Cross-Servicing Report [RCTCSP REPORT]</p>
</blockquote></li>
</ul></td>
<td>HMDM Team</td>
</tr>
<tr class="odd">
<td>12/2019</td>
<td>1.5</td>
<td><p>Updated for patch PRCA*4.5*350.</p>
<p>Remove duplicate sections.</p>
<p>This patch adds the capability for a User to re-refer to Cross-Servicing returned or recalled bills, adds new displays to screens denoting when a bill has been re-referred, and a report to show all bills that have been re-referred. It also provides the Users the ability to stop or reactivate Cross-Servicing for a single Debtor or for an entire site and report on the stop/reactivate.</p></td>
<td>SE RCM Team</td>
</tr>
<tr class="even">
<td>08/29/2018</td>
<td>1.4</td>
<td><p>Updated for patch PRCA*4.5*340.</p>
<p>This patch deletes two columns from the Cross-Servicing Reconciliation Report. It replaces last 4 of the SSN with Patient ID. It corrects a minor problem with device handling.</p></td>
<td>HAPE Team</td>
</tr>
<tr class="odd">
<td>05/25/2018</td>
<td>1.3</td>
<td><p>Updated for patch PRCA*4.5*315:</p>
<p>This patch adds two new reports: Cross-Servicing Stop Reactivate Report &amp; Treasury Cross-Servicing IAI Report pages 35 – 37. Updated report options to support CSV format.</p>
<p>Updated screenshots for the Cross-Servicing Recall, Reconciliation reports. A historical “y” indicator is added to the full/brief account profile for CS bills that are recalled by the batch process or returned from Treasury. Updated option names for the recall/reactivate debtor &amp; recall/reactivate bills. Added new option - TCSP reconciliation worklist – to manage bills returned from Treasury page 46. Cross-servicing no longer blocks manual increase adjustments for CS bills and allows manual increase adjustments to the 5B record. A new set of cross-servicing transactions have been added to display an audit trail for detailing events (transactions) that have occurred on healthcare debts referred for debt collection.</p></td>
<td>HAPE Team</td>
</tr>
<tr class="even">
<td>9/21/2017</td>
<td>1.2</td>
<td><p>Updated for patch PRCA*4.5*327:</p>
<p>This patch adds the addition of two new notifications, the Failed Debtor Action &amp; the Batch Completion, to the TCSP mail group. See page 66.</p></td>
<td>HPS Admin Team</td>
</tr>
<tr class="odd">
<td>7/13/2017</td>
<td>1.1</td>
<td><p>Updated for patch PRCA*4.5*325:</p>
<p>This patch converts all scripts for handling Treasury Cross Service Project (TCSP) exceptions between Vista and Treasury to user option with improved controls. These scripts were provided to sites by the TCSP developers to handle mismatched Vista debtor/bills with the Treasury status for the same debtor/bills. See the following sections: 4.4 (TCSP Flag Control), fig. 21 – 26, glossary sections R &amp; T.</p></td>
<td>HPS Admin Team</td>
</tr>
<tr class="even">
<td>10/04/2016</td>
<td>1.0</td>
<td>Initial publication</td>
<td>HPES Team</td>
</tr>
<tr class="odd">
<td>9/28/2016</td>
<td>0.10</td>
<td>Information for updates included in test version T81; see the following sections: 2.5 (heading text), 2.5 #6, 2.6 #4, 3, 5.1, 5.2.2, 8.3.3 (paragraphs &amp; note).</td>
<td>HPES Team</td>
</tr>
<tr class="even">
<td>3/18/2016</td>
<td>0.09</td>
<td>Added Enhancement Requests/updated content</td>
<td>HPES Team</td>
</tr>
<tr class="odd">
<td>11/18/2015</td>
<td>0.08</td>
<td>Added Activation Dates for test sites to Section 2.5. Modified Letter 3 language in Section 2.5</td>
<td>HPES Team</td>
</tr>
<tr class="even">
<td>07/17/2015</td>
<td>0.07</td>
<td>Draft to be used during IOC Testing ONLY; general formatting review; verified all links in the References section.</td>
<td>HPES Team</td>
</tr>
<tr class="odd">
<td>06/02/2015</td>
<td>0.06</td>
<td><p>Added Section 8.4 for all blocked options on Cross-Serviced debt; added Section 9.2 for removing the stop on the bill placed for the reject on the Recall Debtor option.</p>
<p>Updated screenshots for the 5BU AIO IAI transmissions due to code change.</p></td>
<td>HPES Team</td>
</tr>
<tr class="even">
<td>05/11/2015</td>
<td>0.05</td>
<td><p>Draft to be used during second round of UFT (May 15 – May 29, 2015) ONLY.</p>
<p>Updated Production File Transfer graphic to include the DPN file transfer on Tuesdays.</p>
<p>Updated screenshots for DPN; added a sample DPN Letter (Section 7).</p>
<p>Added additional information on the DPN Rejects to Section 7.1.</p>
<p>Added additional text to Section 4.2.1 on the various record types that can be transmitted in the Update File.</p>
<p>Updated screenshots for 5B “ABAL” and AIO”. Also, added the following text: The signed principal amount is the amount by which the transaction amount changes the principal, not the amount of the principal. There should be no positive amounts in these fields because Cross-Servicing will not allow increase adjustments.</p>
<p>Added description of fields in the Cross-Servicing file section.</p>
<p>Modifications to Section 5.2.2 due to Enhancement Request # 159105 (VistA To Produce a 5B Record Transaction Back to Treasury [AITC/DMC] after a Treasury 170 Offset Type That Is An OVERPAYMENT Has Been Processed By VistA.</p></td>
<td>HPES Team</td>
</tr>
<tr class="odd">
<td>02/09/2015</td>
<td>0.04</td>
<td><p>Updated screenshots for 5B “ABAL and “AIO” Transmissions RTC# 145340; added verbiage indicating that end users should not use the Suspend an AR Bill option on Cross-Serviced debt (Appendix D). Added the following note to Section 2.6: “<em>Bills that are placed in a Suspended status continue to age and gather interest and administrative charges in VistA</em>.” (refers to bills not referred to CS).</p>
<p>Draft to be used during UFT (Phase 1) Testing ONLY</p></td>
<td>HPES Team</td>
</tr>
<tr class="even">
<td>02/06/2015</td>
<td>0.03</td>
<td>Draft to be used during UFT (Phase 1) Testing ONLY</td>
<td>HPES Team</td>
</tr>
<tr class="odd">
<td>01/14/2015</td>
<td>0.02</td>
<td>Second draft for review</td>
<td>HPES Team</td>
</tr>
<tr class="even">
<td>12/18/2014</td>
<td>0.01</td>
<td>Draft for use during Pre-UFT Smoke Test (UFT Phase 0) ONLY</td>
<td>HPES Team</td>
</tr>
</tbody>
</table>

<span id="_Toc169093103" class="anchor"></span>Table A‑1: Cross-Servicing Record Types & Action Codes

Table of Contents

[4.1.2 Cross-Servicing Re-Referred Bills Report [27](#cross-servicing-re-referred-bills-report)](\l)

[4.1.3 Cross-Servicing Recall Report [28](#cross-servicing-recall-report)](\l)

[5.3.1 Recall Debt [91](#recall-debt)](\l)

[5.3.2 Recall Debtor [92](#recall-debtor)](\l)

List of Figures

[Figure 40: TCSP Reconciliation Worklist - View Insurance [59](#_Toc25567366)](\l)

[Figure 41: TCSP Reconciliation Worklist – View Insurance – View Policy Info [59](#_Toc25567367)](\l)

[Figure 84: Transmission Message: Manual Decrease Adjustment - ABAL [89](#_Toc25567410)](\l)

[Figure 85: Bulletin: Manual Decrease Adjustment – ABAL [89](#_Toc25567411)](\l)

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [References](#references)
  - [Questions](#questions)
  - [Program Coordination](#program-coordination)
- [What is Cross-Servicing?](#what-is-cross-servicing)
  - [Cross-Servicing & Treasury Offset Program](#cross-servicing-treasury-offset-program)
  - [Cross-Servicing High-Level Process Flow](#cross-servicing-high-level-process-flow)
  - [Integrated Agency Interface (IAI)](#integrated-agency-interface-iai)
  - [Type of Debts Referred to Cross-Servicing](#type-of-debts-referred-to-cross-servicing)
  - [Rules for Initially Sending a Debt to Cross-Servicing](#rules-for-initially-sending-a-debt-to-cross-servicing)
  - [Debts Not Sent to Cross-Servicing](#debts-not-sent-to-cross-servicing)
  - [Cross-Servicing Fees](#cross-servicing-fees)
- [Cross-Servicing Fields & Messages](#cross-servicing-fields-messages)
  - [Debt Referred to Cross-Servicing](#debt-referred-to-cross-servicing)
    - [Brief Account Profile Screen](#brief-account-profile-screen)
    - [Full Account Profile Screen](#full-account-profile-screen)
    - [Account Profile – Agent Cashiers Menu](#account-profile-agent-cashiers-menu)
    - [Bill Profile](#bill-profile)
    - [Profile of Accounts Receivable](#profile-of-accounts-receivable)
  - [Debt / Debtor Recalled from Cross-Servicing](#debt-debtor-recalled-from-cross-servicing)
    - [Brief Account Profile Screen](#brief-account-profile-screen-1)
    - [Full Account Profile Screen](#full-account-profile-screen-1)
    - [Bill Profile](#bill-profile-1)
    - [Profile of Accounts Receivable](#profile-of-accounts-receivable-1)
  - [Debt Rejected by Cross-Servicing](#debt-rejected-by-cross-servicing)
    - [Brief Account Profile Screen](#brief-account-profile-screen-2)
    - [Full Account Profile Screen](#full-account-profile-screen-2)
    - [Bill Profile](#bill-profile-2)
    - [Profile of Accounts Receivable](#profile-of-accounts-receivable-2)
- [Cross-Servicing Options](#cross-servicing-options)
  - [Report Options](#report-options)
    - [Cross-Servicing Bill Report](#cross-servicing-bill-report)
    - [Cross-Servicing Re-Referred Bills Report](#cross-servicing-re-referred-bills-report)
    - [Cross-Servicing Recall Report](#cross-servicing-recall-report)
    - [Cross-Servicing Stop Reactivate Report](#cross-servicing-stop-reactivate-report)
    - [Debt Referral Reject Report](#debt-referral-reject-report)
    - [List IAI Error Codes](#list-iai-error-codes)
    - [Print Cross-Servicing Report](#print-cross-servicing-report)
    - [Reconciliation Report – Cross-Servicing](#reconciliation-report-cross-servicing)
    - [Treasury Cross-Servicing IAI Report](#treasury-cross-servicing-iai-report)
    - [Multiple Referral Programs Report](#multiple-referral-programs-report)
  - [Recall/Reactivate TCSP Referrals](#recallreactivate-tcsp-referrals)
    - [Recall TCSP Referral for a Bill](#recall-tcsp-referral-for-a-bill)
    - [Debtor Recall TCSP Referral](#debtor-recall-tcsp-referral)
    - [Reactivate Referral After Recall](#reactivate-referral-after-recall)
  - [Refer Returned CS Bill](#refer-returned-cs-bill)
    - [First Time Re-referral](#first-time-re-referral)
    - [Update a Re-referral](#update-a-re-referral)
    - [Cancel a Re-referral](#cancel-a-re-referral)
  - [Stop/Reactivate TCSP Referral](#stopreactivate-tcsp-referral)
    - [Stop/Reactivate TCSP Referral for a Bill](#stopreactivate-tcsp-referral-for-a-bill)
    - [Reactivate TCSP Referral for a Bill (Remove ‘Stop’ Flag)](#reactivate-tcsp-referral-for-a-bill-remove-stop-flag)
    - [Stop/Reactivate TCSP Referral for a Debtor](#stopreactivate-tcsp-referral-for-a-debtor)
    - [Reactivate TCSP Referral for a Debtor](#reactivate-tcsp-referral-for-a-debtor)
  - [TCSP Flag Control](#tcsp-flag-control)
    - [Set Cross-Service Flag on Bill](#set-cross-service-flag-on-bill)
    - [Clear Cross-Service Flag on Bill](#clear-cross-service-flag-on-bill)
    - [Clear Cross-Service Flag on Debtor (and all Bills)](#clear-cross-service-flag-on-debtor-and-all-bills)
    - [Set Cross-Service Flag on Debtor](#set-cross-service-flag-on-debtor)
    - [Fully Re-establish Debtor/Bill as Cross-Serviced](#fully-re-establish-debtorbill-as-cross-serviced)
  - [Reconciliation List Manager Option](#reconciliation-list-manager-option)
    - [Reconciliation List Manager](#reconciliation-list-manager)
    - [TCSP Reconciliation Worklist – Account Profile](#tcsp-reconciliation-worklist-account-profile)
- [Cross-Servicing Batch Jobs](#cross-servicing-batch-jobs)
  - [Referral Batch Job](#referral-batch-job)
    - [Add New Debt Referral](#add-new-debt-referral)
    - [New Debt for Existing Debtor](#new-debt-for-existing-debtor)
  - [Update Batch Job](#update-batch-job)
    - [Updates to Debtor’s Patient File](#updates-to-debtors-patient-file)
    - [Adjustments](#adjustments)
  - [Recall Batch Job](#recall-batch-job)
    - [Recall Debt](#recall-debt)
    - [Recall Debtor](#recall-debtor)
- [Debts / Debtors Returned by Treasury for Reconciliation](#debts-debtors-returned-by-treasury-for-reconciliation)
- [Due Process Notification Letter](#due-process-notification-letter)
  - [Due Process Notification Rejects](#due-process-notification-rejects)
- [Collections: Payment Processing](#collections-payment-processing)
  - [What is Lockbox?](#what-is-lockbox)
  - [No Manual Payments on Cross-Serviced Bills](#no-manual-payments-on-cross-serviced-bills)
  - [Lockbox Payment Types](#lockbox-payment-types)
    - [DMC Offset (168)](#dmc-offset-168)
    - [TOP Payments (169)](#top-payments-169)
    - [Treasury Payments (170)](#treasury-payments-170)
  - [Other Blocked Options on Cross-Serviced Bills](#other-blocked-options-on-cross-serviced-bills)
    - [Set Up Repayment Plan](#set-up-repayment-plan)
    - [Administrative Cost Adjustment](#administrative-cost-adjustment)
    - [Fiscal Officer Terminated](#fiscal-officer-terminated)
    - [Compromise Termination](#compromise-termination)
    - [Suspend an AR Bill](#suspend-an-ar-bill)
    - [Partial /Full Waiver](#partial-full-waiver)
- [Cross-Servicing Rejects](#cross-servicing-rejects)
  - [Recall Debtor Rejects](#recall-debtor-rejects)
  - [Reject Messages](#reject-messages)
  - [ZZ Error Code](#zz-error-code)
- [Additional VistA Information](#additional-vista-information)
  - [Cross-Servicing Mail Group](#cross-servicing-mail-group)
  - [Cross-Servicing File Transfer Schedule](#cross-servicing-file-transfer-schedule)
  - [Cross-Servicing Files & Fields](#cross-servicing-files-fields)
- [Appendix A. Cross-Servicing Record Types & Action Codes](#appendix-a-cross-servicing-record-types-action-codes)
- [Appendix B. Cross-Servicing IAI Error Codes](#appendix-b-cross-servicing-iai-error-codes)
- [Appendix C. Patient Statement Updates for Cross-Servicing](#appendix-c-patient-statement-updates-for-cross-servicing)
- [Appendix D. Acronyms](#appendix-d-acronyms)
- [Appendix E. Glossary](#appendix-e-glossary)
  - [A](#a)
  - [B](#b)
  - [C](#c)
  - [D](#d)
  - [F](#f)
  - [G](#g)
  - [I](#i)
  - [M](#m)
  - [P](#p)
  - [R](#r)
  - [S](#s)
  - [T](#t)
  - [U](#u)
  - [V](#v)
  - [W](#w)
- [Appendix F. References](#appendix-f-references)
The Department of Treasury (Treasury) Cross-Servicing program is the Department of Veterans Affairs’ (VA) next phase in the implementation of the Debt Collection Improvement Act (DCIA) of 1996. In 1996, 31 U.S.C 3716, Administrative Offset, was amended by DCIA, which initiated the requirement for VA to transfer any debt delinquent more than 180 days to Treasury for administrative offset or collection. With this amendment, VA implemented the Treasury Offset Program (TOP), which provided Consolidated Patient Account Centers (CPAC) Accounts Receivable (AR) staff members with an automated method of referring delinquent debt to Treasury. With the passing of the Digital Accountability and Transparency Act of 2014 (DATA Act), VA must now refer delinquent debt to Treasury after 120 days.
The Cross-Servicing functionality, developed as part of the Cross-Servicing program, was delivered and integrated under the Veterans Health Information Systems and Technology Architecture (VistA) AR 4.5 patch, PRCA\*4.5\*301. This new functionality will allow the Veterans Health Administration (VHA) to refer debt that has been delinquent 120 days or more to Treasury for administrative offset or collection.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this manual is to assist end users with the VistA Cross-Servicing AR 4.5 functionality, providing step-by-step examples that describe the options used for generating Cross-Servicing Reports, stopping or recalling Cross-Servicing referred debt and debtors, and how to locate the fields and text displays that reference Cross-Servicing referrals, recalls, and rejects.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended users of the Cross-Servicing functionality are the AR Supervisors and the Veteran Services Department technicians who handle First Party AR function for the CPACs.

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For references were used in the development of the Cross-Servicing program and in the development of this manual, see *Appendix F. References*.

## Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please direct all questions on the Cross-Servicing functionality and business processes to REDACTED.

## Program Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cross-Servicing is a joint effort between VistA AR, the Austin Information Technology Center (AITC), the Debt Management Center (DMC), and Treasury. For more information on each organization, please reference the following links:

- Veterans Health Administration (VHA) Chief Business Office (CBO): REDACTED
- Austin Information Technology Center (AITC)
- [Department of Veterans Affairs (VA) Debt Management Center (DMC)](http://www.va.gov/debtman/)
- [Consolidated Patient Account Center (CPAC)](http://www.va.gov/CBO/cbo/cpac.asp)
- [U.S. Department of the Treasury, Bureau of the Fiscal Service](https://www.fiscal.treasury.gov/dms/)

# What is Cross-Servicing?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a brief overview of how the VistA AR 4.5 Cross-Servicing functionality integrates with AITC, DMC, and Treasury.

## Cross-Servicing & Treasury Offset Program

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Treasury Cross-Servicing program is a mandatory, government-wide, delinquent, debt‑matching, and payment-offset system. It is a cost-effective means by which VA and all Federal program agencies recover delinquent debts through Treasury debt collection efforts, Administrative Wage Garnishment, referral to Private Collection Agencies, and offsetting Federal payments due the delinquent debtor. At the implementation of the Cross-Servicing program, all new, legally enforceable, non-tax, First Party debt owed to VHA that is over 120 days will be referred to Cross-Servicing. First party debt, previously processed by Treasury Offset Program (TOP), will remain in TOP. As with TOP, Cross-Servicing is a collaborative effort among VistA AR, AITC, DMC, and Treasury.

1.  At the implementation of the Cross-Servicing program, new, First Party debt that has been delinquent 120 days or more will be processed by Cross-Servicing.  
    Once a debt has been referred to Cross-Servicing, VHA can no longer service the debt.  
    First Party debt, previously processed by TOP, will remain in TOP. Any updates transmitted on a TOP account will continue to be updated in TOP, not Cross-Servicing.

## Cross-Servicing High-Level Process Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following provides a high-level overview of the Cross-Servicing process and functionality:

1.  After the DMC referral process, those debtors without VA benefits to offset are subject to the Cross-Servicing Program.
2.  AR sends new bill referrals, re-referral of previously recalled or returned bills, updates, and/or recalls of previously referred bills to AITC every Tuesday. Updates include, but are not limited to, such things as change in the debtor’s address or change in name.
3.  AITC sends a MailMan confirmation message to each VAMC when their transmission is received at AITC.
4.  AITC compiles file information from all VAMCs into Treasury’s Integrated Agency Interface (IAI) File Format (refer to *Section 2.3Integrated Agency Interface (IAI)*) and forwards to DMC.
5.  DMC validates header and footer information and forwards the file on to Treasury Cross‑Servicing. If the validation fails, DMC will reject the entire file and send it back to AITC for repair and re-transmission. However, the DMC check is now at the bill level rather than at the account level.
6.  If there are errors within the file that Treasury receives, an Unprocessable File from Treasury is sent electronically to DMC and forwarded on to AITC.
7.  AITC transmits the Cross-Servicing Unprocessable Files to each VAMC via MailMan. Reject messages and subsequent Unprocessable Files may originate from AITC or Treasury. Reject bulletins are generated containing the bill number and the error code(s) (refer to *Section 9Cross-Servicing Rejects*).
8.  If the Cross-Servicing Referral file rejects, the AR system will delete all of the Cross‑Servicing referral information for the debt in VistA. The reject information will display on the profile screens (refer to *Section 3.3Debt Rejected by Cross-Servicing*) and in the Debt Referral Reject Report (refer to *Section4.1.5)*.
9.  The AR staff must correct the cause of the error. Once corrected, the account will follow the appropriate processing sequence. Depending on the status of the account, this may include referral to Cross-Servicing with the next weekly transmission.
10. Upon implementation of Cross-Servicing, a one-time only process will generate an initial Due Process Notification (DPN) file that identifies bills that comply with all of the Cross-Servicing criteria, but are less than \$25.
11. On a weekly basis, the Initial DPN File will be checked by VistA for any bills that had previously been identified as less than \$25 and have now increased (due to fees and charges) to \$25 or more.
12. VistA will send this file to AITC for the purpose of printing the DPN Letters to the debtors of record.
13. AITC will process through each record and determine if the record is valid and can generate a Printed Letter, or determine if it is in error and is to be returned to VistA, identifying the two digit IAI error code(s). A DPN reject bulletin is generated listing the bills that were rejected with the associated error code (refer to *Section 7.1Due Process Notification Rejects*).
14. VistA receives the DPN Letter Printed & Error File from AITC and logs the Date Letter Printed or Errors found. (Note: This Date Letter Printed is used to calculate a 60-day waiting period before the Debt Referral for this bill can be made through the Referral process.)
15. Once a week, Treasury will send collections from Cross-Servicing to DMC.
16. DMC converts the VHA payments from the IAI Collection File to the Cross-Servicing Lockbox format.
17. AITC receives the Collections File and parses by VAMC.
18. VistA receives and processes the updates identified in the Collection File.

<span id="_Hlk169269034" class="anchor"></span>Figure 1: Cross-Servicing Scope of Integration and Process Flow

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/002.png)

## Integrated Agency Interface (IAI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Treasury’s Integrated Agency Interface (IAI) file format[^1] provides VA with a single file format for submitting multiple record types to Cross-Servicing via the FedDebt system.

For Cross-Servicing, IAI is used to: (1) Refer initial debt / debtor(s), (2) Re-refer returned or recalled debt, (3) Process financial updates (payments and adjustments), (4) Modify debt / debtor information, (5) Recall a debt / debtor, (6) Receive an Unprocessable Report from Treasury, and (7) Receive the Reconciliation File from Treasury.

Treasury’s Debt Management Services (DMS) processes IAI batch files daily and provides a comprehensive Unprocessable report to notify VHA that (a) its files have been processed, (b) whether any errors occurred and (c) what those errors are. DMS transmits reports to VA no later than the day after the file processing is complete. VHA receives an IAI Collection File each time DMS transmits an Intra-governmental Payments and Collections (IPAC) transfer for Cross-Servicing collections. This IAI Collection File includes all payment transactions for the specified collection period (refer to *Section 8Collections: Payment Processing*).

## Type of Debts Referred to Cross-Servicing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following AR Categories indicate First Party bills to be referred to Cross-Servicing:

> 1 – Hospital Care (NSC)

> 2 – Outpatient Care (NSC)

> 3 – Nursing Home Care (NSC)

> 24 – C (Means Test)

> 29 – Rx Co-payment / SC Vet

> 30 – Rx Co-payment / NSC Vet

> 31 – Nursing Home Care Per Diem

> 32 – Hospital Care Per Diem

> 40 – Adult Day Health Care

> 41 – Domiciliary

> 42 – Geriatric Evaluation – Institution

> 43 – Geriatric Evaluation – Non-institution

> 44 – Nursing Home Care – LTC

> 45 – Respite Care – Institution

> 46 – Respite Care – Non-institution

## Rules for Initially Sending a Debt to Cross-Servicing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the following criteria must be true for a debt to be referred to Cross-Servicing:

1.  The bill must be delinquent 120 days or more. (Note: This equates to 150 days old or older based on the date value in the “LETTER1” field (#61) in the Accounts Receivable file (#430)).
2.  As debts become eligible for Cross-Servicing, they are referred during the next weekly Cross-Servicing batch cycle transmission according to the following station locations and date specifications:
- If the LETTER1 (file \# 430, 61) is no earlier than February 1, 2015 for stations \#598 (Little Rock, AR), \#528 (Upstate NY-VISN 2), and \#517 (Beckley, WV).
- If the LETTER1 (file \# 430, 61) is no earlier than August 1, 2015 for all other stations.
3.  The Debtor Type must be a First Party bill.
4.  The bill status must be *Active*.
5.  The Site Deletion Referral Flag for a debtor must be set to ‘blank’ or ‘NO’ in the AR Debtor File (#340).
6.  The DMC Referral Flag must be removed from the bill. *DATE SENT TO DMC* field (file \#430, 121) must be Null and *DMC Debt Valid* field (file \#430,125) must be Yes.
7.  An individual bill must be equal to or greater than \$25.00.
8.  If the *Letter3* field under *Collection Follow up Date* on the profile screen does not have a date, the debt will not be referred to Cross-Servicing. VistA generates the ‘TCSP QUALIFIED/NO 3RD LETTER SENT ON MM/DD/YY’ bulletin when there is eligible debt for Cross-Servicing and a third collection letter has not been sent. Technicians should review the debtor’s account to determine why the third letter has not been sent.

<span id="_Hlk169269080" class="anchor"></span>Figure 2: Bulletin: TCSP Qualified/No 3rd Letter Sent

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/003.png)

## Debts Not Sent to Cross-Servicing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If <u>any</u> of the following criteria is true, the bill will NOT be referred to Cross-Servicing:

1.  Debts where the Debtor has included VA debts in their bankruptcy petition and has provided proof of bankruptcy.
2.  Debts where the debtor’s date of death is recorded in VistA.
3.  Debt that is in litigation and has been referred to the Department of Justice (DOJ). The software checks to see if the flag is set to “DOJ”. It will not refer a particular bill that is referred to DOJ; however, it can refer other bills by the same debtor that are not flagged as being referred to DOJ.
4.  Debt that is in *Offset* status at DMC. DATE SENT TO DMC (#121) would be populated.
5.  Debt that has a DMC Debt Valid (#125) field of “No” or “Pending” in the ACCOUNTS RECEIVABLE (#430) file.
6.  Debt that is on a repayment plan in VistA.
7.  Debt that is in *Suspended* status in the AR system (this includes, but is not limited to, the following: waiver, disputes, bankruptcy).
2.  Bills that are placed in a *Suspended* status continue to age and gather interest and administrative charges in VistA. If a bill has been suspended and is <u>un</u>suspended on or after Day 120 of the delinquency (and meets all of the other Cross-Servicing criteria), it will be referred to Cross-Servicing in the next weekly transmission.
8.  The Debtor is an entity or institution (a non-individual).
9.  The Debt is less than \$25.00.
10. A third collection letter has not been sent.
11. Debtor has a Stop flag set.
12. Site has a Stop flag set.

## Cross-Servicing Fees

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The debtor is responsible for paying any and all of the Cross-Servicing offset processing fee(s) from Treasury. Treasury will automatically withhold the offset fee prior to sending the money to VHA. VHA will receive the net amount of the offset. In addition, if a debtor has more than one offset processed on a given day, there will be a fee associated with each offset.

For debt that is continuing to be collected through TOP, the flat fee remains in effect. For all debt referred to Cross-Servicing, Treasury applies an offset fee. Additional fees may be applied if debt is collected through Administrative Wage Garnishment (AWG) or a Private Collection Agency (PCA).

For all questions related to debt that has been referred to Cross-Servicing, please refer the debtor to a Treasury Customer Service Representative at (888) 826-3127.

# Cross-Servicing Fields & Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides an overview of the various messages, symbols, and fields that indicate whether or not a bill has been referred to Cross-Servicing, recalled from Cross-Servicing, or rejected (by AITC, DMC, or Treasury).

The AR profile screens will display the following Cross-Servicing information (click the links below to be taken to the appropriate sub-section):

- [Debt Referred to Cross-Servicing](\l)
- [Debt / Debtor Recalled from Cross-Servicing](#debt-debtor-recalled-from-cross-servicing)
- [Debt Rejected by Cross-Servicing](#debt-rejected-by-cross-servicing)

The following sub-sections outline the location of the Cross-Servicing information on the AR screens.

## Debt Referred to Cross-Servicing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the text, fields, and symbols that display on the various AR screens when a debt has been <u>referred</u> or re-referred to Cross-Servicing.

### Brief Account Profile Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Brief Account Profile screen, a user is able to identify the bills on a debtor’s account that have been referred or re-referred to Cross-Servicing by the following displays:

If a debtor is referred to Cross-Servicing, the following text displays in the header of the screen: “x Debt Referred to Cross-Servicing” and “Total CS Debt” (Figure 3).

If a debtor is referred to Cross-Servicing and has at least one re-referred bill, the following text displays in the header of the screen: “x Debt Re-Referred to Cross-Servicing” (Figure 3), and “Total CS Debt” (Figure 4).

In the list of bills that display on a debtor’s account profile, an “x” will display before the Station Number in the *Bill \#* column for bills that are at Cross-Servicing.

A historical "y" indicator will be displayed if a Cross-Serviced bill has been recalled or returned from Treasury.<span id="_Ref394920653" class="anchor"></span>

Figure 3: Brief Account Profile (when accessed via a Debtor Name) –  
Debt Referred to Cross-Servicing

> ====================== A c c o u n t P r o f i l e ======================

> LLLLL,WWWWW (nnn-nn-nnnn) Statement Day: 24

> Statement Account \#: 442-000000-7172659-LLLLL Last Statement: 01/24/2018

> 7204 ANY RD Activity as of: 01/20/2018

> ANY CITY, ZZ 00000 Amount Owed: 3095.88

> Phone \#: 4444444444 RX Copay Exempt: NO

> CV Status: NO

> \*\* Account forwarded to TOP: 01/14/2008 Total TOP Amount: 0.00

> <span class="mark">x Debt Re-Referred to Cross-Servicing Total CS Debt: 1290.04</span>

> \# Bill \# Est Type Paid Prin Int Adm Balance

> ------------------------------- ACTIVE (3015.88) ------------------------------

> 1 442-K605CYA 06/29/2016 RX CO-P 97.53 2.03 0.00 20.93 22.96

> 2 y442-K605M3F 07/26/2016 RX CO-P 0.00 54.00 0.24 0.00 54.24

> 3 y%442-K605ZAF 08/29/2016 OUTPATI 0.00 15.00 0.24 0.00 15.24

> 4 y442-K702Q34 09/28/2016 RX CO-P 0.00 27.00 0.08 0.00 27.08

> 5 442-K702V5K 10/12/2016 OUTPATI 0.00 15.00 0.15 0.00 15.15

> 6 y%442-K7031JS 10/25/2016 OUTPATI 0.00 60.00 0.23 0.00 60.23

> 7 y442-K70335L 10/26/2016 RX CO-P 0.00 108.00 0.35 0.00 108.35

> 8 %442-K70378E 11/03/2016 REIMBUR 0.00 25.85 0.00 0.00 25.85

> Select 1-8 or return to continue:

<span id="_Hlk169269148" class="anchor"></span>Figure 4: Brief Account Profile (when accessed via a bill number) –  
Debt Re-Referred to Cross-Servicing

> ====================== A c c o u n t P r o f i l e ======================

> LLLLL,WWWWW (nnn-nn-nnnn) Statement Day: 24

> Statement Account \#: 442-000000-7172659-LLLLL Last Statement: 01/24/2018

> 0000 Any road Activity as of: 01/20/2018

> ANY CITY, ZZ 00000 Amount Owed: 3068.80

> Phone \#: 4444444444 RX Copay Exempt: NO

> CV Status: NO

> \*\* Account forwarded to TOP: 01/14/2008 Total TOP Amount: 0.00

> <span class="mark">x Debt Re-Referred to Cross-Servicing</span> Total CS Debt: 1344.28

> <span class="mark">CS Re-Referred Date: MAY 10, 2019</span>

> Bill \#: x442-K605M3F

> Bill \# Tr \# Type Date Amount

> -------------------------------------------------------------------------------

> Original Amount 07/26/2016 0.00

> 1 8749416 INCREASE ADJUSTMENT 07/26/2016 27.00

> 2 8749417 INCREASE ADJUSTMENT 07/26/2016 27.00

> 3 8886710 INTEREST/ADM. CHARGE 10/21/2016 0.09

> 4 8946740 INTEREST/ADM. CHARGE 11/21/2016 0.05

> 5 9013751 INTEREST/ADM. CHARGE 12/21/2016 0.05

> Select 1-5 or 'P' to Print or return to continue:

1.  Once the bill has been selected from the Brief Account Profile screen, the user is directed to the subscreen for that bill. If the bill has been referred to Cross-Servicing, the *CS Referred Date* will display on the sub-screen for that bill below “x Debt Referred to Cross-Servicing” (Figure 5).
2.  If the bill has been re-referred to Cross-Servicing, the *CS Re-Referred Date* will display on the sub-screen for that bill below “x Debt Re-Referred to Cross-Servicing” (Figure 4).
3.  <span id="_Hlk169269177" class="anchor"></span>The Total CS Debt in the below figures refers to the total amount of debt referred to Cross-Servicing. All transactions performed on the bill will display including any non-financial cross-servicing audit transactions (marked with “CS”). These transactions provide non-financial information and comments relevant to cross-servicing events that are not otherwise documented in the system.

Figure 5: Brief Account Profile – Bill Subscreen – CS Referred Date

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/004.png)

<span id="_Hlk169269181" class="anchor"></span>Figure 6: Brief Account Profile – Bill Subscreen – CS Re-Referred Date

> ====================== A c c o u n t P r o f i l e ======================

> LLLLL,WWWWW (nnn-nn-nnnn) Statement Day: 24

> Statement Account \#: 000-000000-717XX59-XXXX Last Statement: 01/24/2018

> 7204 ANY RD Activity as of: 01/20/2018

> ANY CITY, ZZ 00000 Amount Owed: 3095.88

> Phone \#: 4444444444 RX Copay Exempt: NO

> CV Status: NO

> \*\* Account forwarded to TOP: 01/14/2008 Total TOP Amount: 0.00

> <span class="mark">x Debt Re-Referred to Cross-Servicing Total CS Debt: 1290.04</span>

> <span class="mark">CS Re-Referred Date: APR 16, 2019</span>

> Bill \#: x442-K803GI0

> Bill \# Tr \# Type Date Amount

> -------------------------------------------------------------------------------

> Original Amount 11/21/2017 0.00

> 1 9574659 INCREASE ADJUSTMENT 11/21/2017 1288.00

> 2 9666586 INTEREST/ADM. CHARGE 01/21/2018 2.04

> 3 9686995 CS DEBTOR NEW BILL 04/16/2019 0.00

> 4 9686996 CS RECALL PLACED 04/16/2019 0.00

> 5 9686997 CS BILL RECALL 04/16/2019 0.00

> Select 1-5 or 'P' to Print or return to continue:

### Full Account Profile Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Full Account Profile screen, a user is able to identify which bills on a debtor’s account have been referred or re-referred to Cross-Servicing by the same displays as the Brief Account Profile screen (refer to *Section 3.1.1Brief Account Profile Screen*). After a REJECT, the “x” indicator is removed from the bill on the Full Account Profile Screen, Brief Account Profile Screen, and any other screen as appropriate.

### Account Profile – Agent Cashiers Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Account Profile(AP) screen, accessed from the Agent Cashiers Menu, if a debtor is referred to Cross-Servicing, *Debt Referred to Cross-Servicing* and *Total CS Debt* will display immediately after the *TOTAL BALANCE OWED FOR ALL BILLS DISPLAYED* line of the profile indicating that debtor has been forwarded to Cross-Servicing (Figure 7). If a debtor has one or more bills re-referred to Cross-Servicing, Debt Re-Referred to Cross-Servicing and Total CS Debt will display immediately after the TOTAL BALANCE OWED FOR ALL BILLS DISPLAYED line of the profile indicating that one or more debt has been forwarded to Cross-Servicing (Figure 7).

4.  The Total CS Debt amount refers to the total amount of debt that has been referred-re-referred to Cross-Servicing, not the total balance owed for all bills.

<span id="_Hlk169269214" class="anchor"></span>Figure 7: Account Profile (AP) – Debt Referred to Cross-Servicing

> <u>Account Profile Apr 24, 2019@13:52:01 Page: 2 of 2</u>

> Account: XXXXX,WWWWWW ZZZZZZZ(nnnnnnnnn) DOB: JUN 22, 19XX

> Addr: 4708 ANY ROAD, ANY CITY, ZZ 00000 Phone: 0000000000

> RX Copay Exempt: NO

> ACCOUNT BALANCE: 717.95 Pending Payments: 0.00

> <u>+ BillNum CareDate Stat Bill Type Principal Interest Admin</u>

> 15 xK703IJP 11/28/16 ACTI RX CO-PAYMENT/NSC VE 112.00 0.36 0.00

> 16 xK702Y79 10/19/16 ACTI RX CO-PAYMENT/NSC VE 32.00 0.14 0.00

> 17 xK60674W 09/16/16 ACTI RX CO-PAYMENT/NSC VE 56.00 0.19 0.00

> 18 K605T1G 08/10/16 ACTI RX CO-PAYMENT/NSC VE 8.00 0.16 0.00

> 19 K605FF4 07/07/16 ACTI RX CO-PAYMENT/NSC VE 2.81 0.00 20.93

> --------- -------- --------

> TOTAL BALANCE OWED FOR ALL BILLS DISPLAYED 694.81 2.21 20.93

> \*\* Account forwarded to TOP: 07/12/2010 Total TOP Amount: 0.00

> <span class="mark">Debt Referred to Cross-Servicing Total CS Debt: 453.48</span>

<span id="_Hlk169269233" class="anchor"></span>Figure 8: Account Profile (AP) – Debt Re-Referred to Cross-Servicing

> <u>Account Profile Apr 24, 2019@13:45:12 Page: 3 of 3</u>

> Account: LLLLL,WWWWW(nnnnnnnnn) DOB: AUG 15, 19XX

> Addr: 7204 ANY RD, ANY CITY, ZZ 00000 Phone: 4444444444

> RX Copay Exempt: NO

> ACCOUNT BALANCE: 3095.88 Pending Payments: 0.00

> <u>+ BillNum CareDate Stat Bill Type Principal Interest Admin</u>

> --------- -------- --------

> TOTAL BALANCE OWED FOR ALL BILLS DISPLAYED 3067.53 7.42 20.93

> \*\* Account forwarded to TOP: 01/14/2008 Total TOP Amount: 0.00

> <span class="mark">Debt Re-Referred to Cross-Servicing Total CS Debt: 1290.04</span>

### Bill Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Bill Profile (BP) screen, the *Debt Referred to Cross-Servicing* text displays *before the listing of the charges* on the bill. For bills that have been re-referred, *Debt Re-Referred to Cross-Servicing* displays *before the listing of the charges* on the bill.

<span id="_Hlk169269248" class="anchor"></span>Figure 9: Bill Profile (BP) – Debt Referred to Cross-Servicing

> <u>Bill Profile Apr 24, 2019@14:04:45 Page: 2 of 3</u>

> \*\*\*\*\* ACCOUNTS RECEIVABLE BILL PROFILE FOR 442-K60674W \*\*\*\*\*

> <u>+</u>

> <u>Bill Balances Billed Paid</u>

> Principal: 56.00 0.00 Original Amt: 0.00

> Interest: 0.19 0.00

> <u>Administrative: 0.00 0.00</u>

> Current: 56.19 0.00

> <u>Accounting Data</u> <u>Fiscal Year</u> <u>Approp Code</u> <u>Amount</u>

> 16 528701 56.00

> Rev Srce Code: 8CZZ

> <u>Collection Follow up Data</u>

> Letter1: SEP 24, 2016

> Letter2: OCT 24, 2016

> Letter3: NOV 24, 2016

> Letter4: JAN 24, 2018

> <span class="mark">Debt Referred to Cross-Servicing CS Referred Date: FEB 14, 2017</span>

> \+ \|% EEOB \| Enter ?? for more actions\|

> BT Bill Transactions NB Select New Bill EA Exit Action

> Select Action: Next Screen//

<span id="_Hlk169269270" class="anchor"></span>Figure 10: Bill Profile (BP) – Debt Re-Referred to Cross-Servicing

> <u>Bill Profile Apr 24, 2019@14:10:50 Page: 2 of 3</u>

> \*\*\*\*\* ACCOUNTS RECEIVABLE BILL PROFILE FOR 442-K803GI0 \*\*\*\*\*

> <u>+</u>

> <u>Bill Balances Billed Paid</u>

> Principal: 1288.00 0.00 Original Amt: 0.00

> Interest: 2.04 0.00

> <u>Administrative: 0.00 0.00</u>

> Current: 1290.04 0.00

> <u>Accounting Data</u> <u>Fiscal Year</u> <u>Approp Code</u> <u>Amount</u>

> 18 528703 1288.00

> Rev Srce Code: 88ZZ

> <u>Collection Follow up Data</u>

> Letter1: NOV 24, 2017

> Letter2: DEC 24, 2017

> Letter3: JAN 24, 2018

> Letter4:

> <span class="mark">Debt Re-Referred to Cross-Servicing CS Re-Referred Date: APR 16, 2019</span>

> \+ \|% EEOB \| Enter ?? for more actions\|

> BT Bill Transactions NB Select New Bill EA Exit Action

> Select Action: Next Screen//

### Profile of Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Profile of Accounts Receivable screen, *Debt Referred to Cross-Servicing* will display in the header if the Debtor has ever been referred to Cross-Servicing (Figure 11).

<span id="_Hlk169269297" class="anchor"></span>Figure 11: Profile of Accounts Receivable – Debt Referred to Cross-Servicing

> APR 24,2019 14:14 ACCOUNTS RECEIVABLE PROFILE

> ===========================================================================

> NAME: PAYER,TEST TEST BILL \#: 442-K803U29

> 4708 ANY ROAD SOC.SEC.NO.: nnn-nn-nnnn

> APT ABC

> ANY CITY, ZZ 00000 DATE OF BIRTH: 00/00/0000

> PHONE NO.: 0000000000 DATE POSTED: DEC 27, 2017 16:46:07

> \*\*\*\*Debtor's Account Forwarded To TOP\*\*\*\*

> <span class="mark">\*\*\*\*Debt Referred to Cross-Servicing\*\*\*\*</span>

> CURRENT STATUS: ACTIVE CATEGORY: RX CO-PAYMENT/NSC VET

> CP: DATE BILL PREPARED: DEC 27,2017

> INTEREST EFFECTIVE RATE DATE: JAN 1,2017 ANNUAL INTEREST RATE: .01

> ADMIN EFFECTIVE RATE DATE: JAN 1,2017 MONTHLY ADMIN RATE: 1.9

> ORIGINAL AMOUNT: 0.00

> FISCAL YEAR APPROP. CODE PAT REFERENCE \# AMOUNT

> ----------- ------------ --------------- ------

> 18 528701 54.00

> DC/DOJ REF.DATE:

If the selected bill has been referred to Cross-Servicing, the *CS Referred Date* will display below the *CURRENT* balance of the bill and above the *TRANSACTIONS* (Figure 12).

<span id="_Hlk169269320" class="anchor"></span>Figure 12: Profile of Accounts Receivable – CS Referred Date

> BALANCES PAID

> LETTER1/ICD: 01/24/2018

> PRINCIPAL: 54.00 0.00 LETTER2:

> INTEREST: 0.00 0.00 LETTER3:

> ADMINISTRATIVE: 0.00 0.00 IRS LETTER:

> DC/DOJ REF.DATE:

> CURRENT: 54.00 0.00

> <span class="mark">CS Referred Date:</span> <span class="mark">FEB 14, 2017</span>

> TRANSACTIONS:

> 9638083 1 INCREASE ADJUSTMENT 12/27/17 8.00

> 9646216 2 INCREASE ADJUSTMENT 01/08/18 15.00

> 9646217 3 INCREASE ADJUSTMENT 01/08/18 16.00

> 9649430 4 INCREASE ADJUSTMENT 01/09/18 15.00

*Debt Re-Referred to Cross-Servicing* will display in the header when one or more bills have been re-referred to Cross-Servicing (Figure 13).

<span id="_Hlk169269340" class="anchor"></span>Figure 13: Profile of Accounts Receivable – Debt Re-Referred to Cross-Servicing

> APR 24,2019 14:41 MEANS TEST ACCOUNTS RECEIVABLE PROFILE

> ===========================================================================

> NAME: PAYER,TEST BILL \#: 442-K803GI0

> 7204 ANY SOC.SEC.NO.: 000-XX-XXXX

> ANY CITY, ZZ 00000 DATE OF BIRTH: 08/15/19XX

> PHONE NO.: 4444444444 DATE POSTED: NOV 21, 2017 01:08:57

> \*\*\*\*Debtor's Account Forwarded To TOP\*\*\*\*

> <span class="mark">\*\*\*\*Debt Re-Referred to Cross-Servicing\*\*\*\*</span>

> CURRENT STATUS: ACTIVE CATEGORY: C (MEANS TEST)

> CARE: HOSPITAL CARE (NSC)

> CP: FUND (APPROPRIATION): 528703

> DATE BILL PREPARED: NOV 21,2017

> INTEREST EFFECTIVE RATE DATE: JAN 1,2017 ANNUAL INTEREST RATE: .01

> ADMIN EFFECTIVE RATE DATE: JAN 1,2017 MONTHLY ADMIN RATE: 1.9

> ORIGINAL AMOUNT: 0.00

> FISCAL YEAR APPROP. CODE PAT REFERENCE \# AMOUNT

> ----------- ------------ --------------- ------

> 18 528703 1288.00

> ENTER '^' TO HALT:

If the selected bill has been re-referred to Cross-Servicing, the *CS Re-Referred Date* will display below the *CURRENT* balance of the bill and above the *TRANSACTIONS* (Figure 14).

<span id="_Hlk169269364" class="anchor"></span>Figure 14: Profile of Accounts Receivable – CS Re-Referred Date

> BALANCES PAID

> LETTER1/ICD: 11/24/2017

> PRINCIPAL: 1288.00 0.00 LETTER2: 12/24/2017

> INTEREST: 2.04 0.00 LETTER3: 01/24/2018

> ADMINISTRATIVE: 0.00 0.00 IRS LETTER:

> DC/DOJ REF.DATE:

> CURRENT: 1290.04 0.00

> <span class="mark">CS Re-Referred Date: APR 16, 2019</span>

> TRANSACTIONS:

> 9574659 1 INCREASE ADJUSTMENT 11/21/17 1288.00

> 9666586 INTEREST/ADM. CHARGE 01/21/18 2.04

> 9686995 CS DEBTOR NEW BILL 04/16/19 0.00

> 9686996 CS RECALL PLACED 04/16/19 0.00

> 9686997 CS BILL RECALL 04/16/19 0.00

> 9687012 CS RE-REFER BILL REQUEST 04/16/19 0.00

> 9687027 CS DEBTOR RE-REFER BILL 04/16/19 0.00

All transactions performed on the bill will display including any non-financial cross-servicing audit transactions (marked with “CS”). These transactions provide non-financial information and comments relevant to cross-servicing events that are not otherwise documented in the system.

<span id="_Hlk169269384" class="anchor"></span>Figure 15: Profile of Accounts Receivable – “CS” Transactions Display

> TRANSACTIONS:

> 5600148 1 INCREASE ADJUSTMENT 08/25/16 8.00

> 5600149 2 DECREASE ADJUSTMENT 10/17/16 -8.00

> \*5601851 <span class="mark">CS</span> RECALL PLACED 09/25/17 0.00

> 5601859 <span class="mark">CS</span> INCREASE ADJ 09/25/17 10.00

> \*5601860 <span class="mark">CS</span> INC ADJ TR REV?N 09/25/17 0.00

> 5601861 ADMIN.COST CHARGE 09/25/17 3.30

> \*5601862 <span class="mark">CS</span> ADMIN ADJ TR REV?N 09/25/17 0.00

> ENTER '^' TO HALT:

## Debt / Debtor Recalled from Cross-Servicing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the text and fields that display on the various AR screens when a debt has been <u>recalled</u> from Cross-Servicing.

### Brief Account Profile Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Brief Account Profile screen, a user is able to identify the bills that have been either automatically recalled from Cross-Servicing (due to the debt balance dropping below \$25 and where there has been no activity in 365 days or more) or manually recalled from Cross-Servicing. Note that VistA automatically applies the Recall Reason, “Agency is Forgiving Debt”, to all of the automatically recalled bills.

Once a bill or debtor has been recalled, the Cross-Servicing referred information is deleted from the bill, as described below:

- In the list of bills that display on a debtor’s account profile, the “x” will be replaced by “y” before the Station Number in the *Bill \#* column.

Also, the *CS Recall Reason* and *CS Recall Date* will display on Page 2 of the Brief Account Profile screen above the Bill \# (Figure 16).

All transactions performed on the bill will display including any non-financial cross-servicing audit transactions (marked with “CS”). Recalls placed and processed recall transactions will display.

<span id="_Hlk169269406" class="anchor"></span>Figure 16: Brief Account Profile – CS Recall Reason & CS Recall Date

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/005.png)

### Full Account Profile Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Full Account Profile screen, a user is able to identify which bills on a debtor’s account have been recalled from Cross-Servicing by the same displays as the Brief Account Profile screen (refer to the previous section).

### Bill Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Bill Profile (BP) screen, the *CS Recall Reason and CS Recall Date* displays on Page 2 after the *Collection Follow up Data* on the bill.

<span id="_Hlk169269414" class="anchor"></span>Figure 17: Bill Profile (BP) – Debt Recalled from Cross-Servicing

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/006.png)

### Profile of Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Profile of Accounts Receivable screen, the *CS Recall Reason* and *CS Recall Date* will display in the header when a bill or debtor has been recalled from Cross-Servicing.

All transactions performed on the bill will display including any non-financial cross-servicing audit transactions (marked with “CS”). Recalls placed and processed recall transactions will display.

<span id="_Hlk169269420" class="anchor"></span>Figure 18: Profile of Accounts Receivable – Debtor Recalled from Cross-Servicing

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/007.png)

## Debt Rejected by Cross-Servicing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a debt is rejected by Cross-Servicing, the referral information is deleted from the debt (refer to *Section 9Cross-Servicing Rejects*). VistA maintains a historical record of the rejects by adding the reject code, reject reason, reject date, and reject source to the various profile screens.

5.  The reject code, reason, date, and source remain on the screen even after the error is corrected.

This section describes the fields that display on the various AR screens when a debt has been <u>rejected</u> by Cross-Servicing.

### Brief Account Profile Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a debt has been rejected, the Cross-Servicing referred information is deleted from the debt. The following information will display below the header on the Brief Account Profile screen: “Last CS REJECT CODE:” and “Last CS REJECT DATE:” with the last recorded Reject Date and Reject Code.

<span id="_Hlk169269433" class="anchor"></span>Figure 19: Brief Account Profile – Debt Rejected by Cross-Servicing

> ====================== A c c o u n t P r o f i l e ======================

> DDDDDDD,SSSS LLL (nnn-nn-nnnn) Statement Day: 24

> Statement Account \#: 442-000000-7183766-DDDDD Last Statement: 01/24/2018

> PO BOX 000 Activity as of: 01/20/2018

> ANY CITY, ZZ 00000 Amount Owed: 559.87

> Phone \#: 0000000000 RX Copay Exempt: NO

> CV Status: NO

> \*\* Account forwarded to TOP: 09/08/2008 Total TOP Amount: 419.43

> x Debt Referred to Cross-Servicing Total CS Debt: 27.12

> Bill \#: 442-K7048F2 <span class="mark">Last CS REJECT CODE: 7C Last CS REJECT DATE: 12/19/2017</span>

> Bill \# Tr \# Type Date Amount

> -------------------------------------------------------------------------------

> Original Amount 02/03/2017 0.00

> 1 9100544 INCREASE ADJUSTMENT 02/03/2017 9.00

> 2 9104272 INCREASE ADJUSTMENT 02/06/2017 27.00

> 3 9235533 INTEREST/ADM. CHARGE 04/21/2017 0.06

> 4 9283341 INTEREST/ADM. CHARGE 05/21/2017 0.03

> 5 9331872 INTEREST/ADM. CHARGE 06/21/2017 0.03

> 6 9379460 INTEREST/ADM. CHARGE 07/21/2017 0.03

### Full Account Profile Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Full Account Profile screen, a user is able to identify which bills on a debtor’s account have been rejected by Cross-Servicing by the same displays as the Brief Account Profile screen (refer to the previous section). The “x” indicator is removed from the bill.

### Bill Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Bill Profile (BP) screen, the reject information displays after the *Collection Follow up Data* on the bill (Figure 20).

<span id="_Hlk169269461" class="anchor"></span>Figure 20: Bill Profile (BP) – Debt Rejected by Cross-Servicing

> <u>Bill Profile May 01, 2019@12:19:57 Page: 2 of 8</u>

> \*\*\*\*\* ACCOUNTS RECEIVABLE BILL PROFILE FOR 442-K7048F2 \*\*\*\*\*

> <u>+</u>

> <u>Bill Balances Billed Paid</u>

> Principal: 36.00 0.00 Original Amt: 0.00

> Interest: 0.30 0.00

> <u>Administrative: 0.00 0.00</u>

> Current: 36.30 0.00

> <u>Accounting Data</u> <u>Fiscal Year</u> <u>Approp Code</u> <u>Amount</u>

> 17 528701 36.00

> Rev Srce Code: 8CZZ

> <u>Collection Follow up Data</u>

> Letter1: FEB 24, 2017

> Letter2: MAR 24, 2017

> Letter3: APR 24, 2017

> Letter4: JAN 24, 2018

> \+ \|% EEOB \| Enter ?? for more actions\|

> BT Bill Transactions NB Select New Bill EA Exit Action

> Select Action: Next Screen//

> Bill Profile May 01, 2019@11:42:52 Page: 3 of 8

> \*\*\*\*\* ACCOUNTS RECEIVABLE BILL PROFILE FOR 442-K7048F2 \*\*\*\*\*

> \+

> <span class="mark">CS Reject Data</span>

> CS REJECTS:DATE: JUL 06, 2017 CODE(s): 3E SOURCE: T

> DATE: JUL 13, 2017 CODE(s): 3E SOURCE: T

> DATE: JUL 20, 2017 CODE(s): 3E SOURCE: T

> DATE: JUL 31, 2017 CODE(s): 3E SOURCE: T

> DATE: AUG 03, 2017 CODE(s): 3E SOURCE: T

> DATE: AUG 10, 2017 CODE(s): 3E SOURCE: T

> DATE: AUG 17, 2017 CODE(s): 3E SOURCE: T

> DATE: AUG 24, 2017 CODE(s): 3E SOURCE: T

> DATE: AUG 31, 2017 CODE(s): 3E SOURCE: T

> DATE: SEP 18, 2017 CODE(s): 3E SOURCE: T

> DATE: SEP 21, 2017 CODE(s): 3E SOURCE: T

> DATE: SEP 28, 2017 CODE(s): 3E SOURCE: T

> DATE: OCT 05, 2017 CODE(s): 3E SOURCE: T

> DATE: OCT 12, 2017 CODE(s): 3E SOURCE: T

> DATE: OCT 19, 2017 CODE(s): 3E SOURCE: T

> DATE: OCT 26, 2017 CODE(s): 3E SOURCE: T

> \+ \|% EEOB \| Enter ?? for more actions\|

> BT Bill Transactions NB Select New Bill EA Exit Action

> Select Action: Next Screen//

> Bill Profile May 01, 2019@11:45:20 Page: 4 of 8

> \*\*\*\*\* ACCOUNTS RECEIVABLE BILL PROFILE FOR 442-K7048F2 \*\*\*\*\*

> \+

> DATE: DEC 19, 2017 CODE(s): 7C SOURCE: T

> CS REJECT DATE: JUL 06, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: JUL 13, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: JUL 20, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: JUL 31, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> \+ \|% EEOB \| Enter ?? for more actions\|

> BT Bill Transactions NB Select New Bill EA Exit Action

> Select Action: Next Screen//

### Profile of Accounts Receivable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Profile of Accounts Receivable screen, the reject information displays below the header.

<span id="_Hlk169269529" class="anchor"></span>Figure 21: Profile of Accounts Receivable – Debt Rejected by Cross-Servicing

> MAY 1,2019 12:00 ACCOUNTS RECEIVABLE PROFILE

> ===========================================================================

> NAME: PAYER,TEST LLLLL BILL \#: 442-K7048F2

> PO BOX 000 SOC.SEC.NO.: 000-00-0000

> ANY CITY, ZZ 00000 DATE OF BIRTH: mm/dd/yyyy

> PHONE NO.: 0000000000 DATE POSTED: FEB 03, 2017 01:05:35

> \*\*\*\*Debtor's Account Forwarded To TOP\*\*\*\*

> \*\*\*\*Debt Referred to Cross-Servicing\*\*\*\*

> CS REJECTS: DATE: JUL 06, 2017 CODE(s): 3E SOURCE: T

> DATE: JUL 13, 2017 CODE(s): 3E SOURCE: T

> DATE: JUL 20, 2017 CODE(s): 3E SOURCE: T

> DATE: JUL 31, 2017 CODE(s): 3E SOURCE: T

> DATE: AUG 03, 2017 CODE(s): 3E SOURCE: T

> DATE: AUG 10, 2017 CODE(s): 3E SOURCE: T

> DATE: AUG 17, 2017 CODE(s): 3E SOURCE: T

> DATE: AUG 24, 2017 CODE(s): 3E SOURCE: T

> DATE: AUG 31, 2017 CODE(s): 3E SOURCE: T

> DATE: SEP 18, 2017 CODE(s): 3E SOURCE: T

> DATE: SEP 21, 2017 CODE(s): 3E SOURCE: T

> DATE: SEP 28, 2017 CODE(s): 3E SOURCE: T

> DATE: OCT 05, 2017 CODE(s): 3E SOURCE: T

> DATE: OCT 12, 2017 CODE(s): 3E SOURCE: T

> DATE: OCT 19, 2017 CODE(s): 3E SOURCE: T

> DATE: OCT 26, 2017 CODE(s): 3E SOURCE: T

> DATE: DEC 19, 2017 CODE(s): 7C SOURCE: T

> CS REJECT DATE: JUL 06, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: JUL 13, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: JUL 20, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: JUL 31, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: AUG 03, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: AUG 10, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: AUG 17, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: AUG 24, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: AUG 31, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: SEP 18, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: SEP 21, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: SEP 28, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: OCT 05, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: OCT 12, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: OCT 19, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: OCT 26, 2017 REJECT SOURCE: T

> REJECT REASON1: 3E Agency Debtor ID~Agency Debtor ID is Required.

> CS REJECT DATE: DEC 19, 2017 REJECT SOURCE: T

> REJECT REASON1: 7C Agency Debtor ID~Debtor not found for agency debtor Id

> CURRENT STATUS: ACTIVE CATEGORY: RX CO-PAYMENT/NSC VET

> CP: DATE BILL PREPARED: FEB 3,2017

> INTEREST EFFECTIVE RATE DATE: JAN 1,2017 ANNUAL INTEREST RATE: .01

> ADMIN EFFECTIVE RATE DATE: JAN 1,2017 MONTHLY ADMIN RATE: 1.9

> ORIGINAL AMOUNT: 0.00

> FISCAL YEAR APPROP. CODE PAT REFERENCE \# AMOUNT

> ----------- ------------ --------------- ------

> 17 528701 36.00

> ENTER '^' TO HALT:

# Cross-Servicing Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of VistA options that users can utilize related to Cross-Servicing activities, including nine reports, the ability to recall a bill or debtor and to place a stop on a bill. Each option is listed below. All of the options are accessed from the Cross-Servicing Menu \[RCTCSP MENU\]. For each option, detailed VistA steps are provided in this section.

- <u>Bill Recall/Reactivate TCSP Referral</u> \[<u>RCTCSP RECALLB\]:</u> Recall a bill from being referred to Cross-Servicing or reactivate a bill (remove the recall flag) that has been recalled (<u>before the Recall Batch Job runs</u>).
- <u>Cross-Servicing Bill Report</u> \[<u>RCTCSP BILL REPORT\]:</u> For a selected debtor, all bills that have been referred to Cross-Servicing and the date that each bill was referred.
- <u>Cross-Servicing Re-Referred Bills Report \[RCTCSP REREFER BILL REPORT\]:</u> Provides a list of all bills that have been re-referred to Cross-Servicing.
- <u>Cross-Servicing Recall Report</u> \[RCTCSP RECALL REPORT\]<u>:</u> Bills that have been recalled from Cross-Servicing and the date each bill was recalled.
- <u>Cross-Servicing Stop Reactivate Report \[RCTCSP STOP REACTIVATE REPORT\]:</u> The Cross-Servicing Stop Reactivate Report lets the User run the report either for Bills or for Debtors. If Bill Level is selected, the report lists the bills that have been stopped from Cross-Servicing, or Reactivated, or Both. If Debtor Level is selected, the report lists the debtors that have been stopped from Cross-Servicing, or Reactivated, or Both. For both varieties the user may select a range of Debtors or all Debtors, and a range of dates or all dates. Excel CSV output is also supported. At the Bill Level, the user may also specify Divisions.
- <u>Debt Referral Reject Report</u> \[RCTCSP REJECT REPORT\]<u>:</u> Rejected bills from the Unprocessable files from AITC, DMC, and Treasury, and the date, error code, and reason(s) the bill was rejected.
- <u>Debtor Recall/Reactivate TCSP Referral</u> \[<u>RCTCSP RECALLD\]</u>: Recalls all bills referred to Cross-Servicing at the same time for the selected debtor.
- <u>List IAI Error Codes</u> \[<u>RCTCSP IAI ERROR CODES LIST\]:</u> Reference list of the Cross-Servicing error codes, the field name / action, the record type, and error message.
- <u>Print Cross-Servicing Report</u> \[RCTCSP REPORT\]<u>:</u> Current balance of all bills referred to Cross-Servicing and the date the bills were referred. This report provides the option to sort by bill number, debtor name, or the referral date.
- <u>Reconciliation Report - Cross-Servicing \[RCTCSP RECONCIL REPORT\]:</u> Bills / debtors that have been returned by Treasury for reconciliation.
- <u>Reconciliation List Manager \[RCTCSP RECONCILIATION WORKLIST\]:</u> List Manager for VistA AR Cross-servicing reconciliation. This option is used to work debts that are returned from Treasury.
- <u>Refer Returned CS Bill \[RCTCSP REREFER BILL\]:</u> Refer a returned or recalled bill for Cross-Servicing.
- <u>Stop/Reactivate TCSP Referral \[RCTCSP STOP\]:</u> Stop a bill or a Debtor in VistA from being referred to Cross-Servicing or updates on the bill from being transmitted; also, use this functionality to remove the ‘Stop’ flag (reactivate).
- <u>TCSP Flag Control \[RCDP TCSP FLAG CONTROL\]:</u> The options included in this menu are used to correct the bill or debtor data attributes (or flags) as needed because of a variance in the bill or debtor data between the VistA system and the Treasury system. This menu option was introduced with Accounts Receivable patch, PRCA\*4.5\*325. This menu option is locked with security key RCDP TCSP FLAG.

This option will allow TCSP flag control to the following options:

1.  Set cross-service flag on BILL
2.  Clear cross-service flag on BILL
3.  Clear cross-service flag on DEBTOR (AND ALL BILLS)
4.  Set cross-service flag on DEBTOR
5.  Fully re-establish debtor/bill as cross-serviced
- <u>Treasury Cross-Servicing IAI Report \[RCTCSP IAI REPORT\]:</u> This report displays a record of current VHA bills at Treasury. It is a tool that can be used to identify bills erroneously listed in a referral status in VistA when reconciled with the Print Cross-Servicing Report.
- <u>Multiple Referral Programs Report \[PRCAC MULT REF REPORT\]:</u> This report identifies any bills that may be referred for debt collection to multiple debt referral programs.
6.  Refer to Section 3 Cross-Servicing Fields & Messages for a description of the various screens where Cross-Servicing referrals, recalls, and reject information displays.

## Report Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This sub-section describes the seven Cross-Servicing reports accessed from the Cross-Servicing Menu.

### Cross-Servicing Bill Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cross-Servicing Bill Report lists all of the bills that have been referred or re-referred to Cross-Servicing for a debtor. The report lists the bill number (*BILL NO.*), status code (*ST*), the AR Category, the original amount of the bill (*ORIG AMT*), the current amount of the bill (*CURR AMT*), the principle (*PRIN*), interest (*INT*), administrative fees (*ADMIN*), court fees (*COURT*), and the date the bill was referred to Cross-Servicing (*CS REF DATE*). Additionally, the header of the report contains the total amount of all debt referred to Cross-Servicing for the debtor (*CURRENT CS DEBT*).

1.  At the Select Cross-Servicing Menu Option: prompt, enter the option: Cross-Servicing Bill Report.
13. Enter the debtor’s name at the Select AR Debtor: prompt.
14. Choose a Date Range From and Date Range To.
15. Finally, a prompt displays asking to CAPTURE report data to an Excel document?? NO//

> The default is (N)o.

> If (Y)es is entered, the following message displays:

> To capture as an Excel format, it is recommended that you queue this report to a spool device with margins of 256 and page length of 99999 (e.g., spoolname;256;99999). This should help avoid wrapping problems.

> Another method would be to set up your terminal to capture the detail report data. On some terminals, this can be done by invoking 'Logging' or clicking on the 'Tools' menu above, then click on 'Capture Incoming Data' to save to Desktop. To avoid undesired wrapping of the data saved to the file, change the DISPLAY screen width size to 132 and you can enter '0;256;99999' at the 'DEVICE:' prompt.

7.  To avoid undesired wrapping of the data saved to the file, enter '0;256;999' at the DEVICE: prompt.
16. To queue the report to a MailMan message, at the DEVICE prompt enter the letter ‘Q’:

> DEVICE: QUEUE TO PRINT ON

> DEVICE: HFS FILE =\> MESSAGE

> Subject: \[Enter message subject\]

> Select one of the following:

> M Me

> P Postmaster

> From whom: Me//

> Send mail to: CSUSER,ONE // CSUSER,ONE (default will display here)

> Select basket to send to: IN//

> And Send to:

> Requested Start Time: NOW// (Enter time to run report. NOW is the default)

> Report compilation has started with task# 999999.

17. Otherwise, press \[Enter\] to view the complete report.
18. The list of bills for the debtor will display in ascending order by bill number (Figure 22).

<span id="_Hlk169269682" class="anchor"></span>Figure 22: Cross-Servicing Bill Report

> PAGE 1 CROSS-SERVICING BILL REPORT 06/03/24

> ------------------------------------------------------------------------------------------------

> DEBTOR: TEST,TEST J SSN: XXXX CURRENT CS DEBT: 210.33

> ------------------------------------------------------------------------------------------------

> BILL NO. ST AR CAT ORIG AMT CURR AMT PRIN INT ADMIN COURT CS REF DT

> ----------- -- ---------- -------- -------- --------- --------- --------- --------- ---------

> 442-K002Y17 A RX CO-PAYM 36.06 36.06 36.00 0.06 0.00 0.00 03/22/22

> 442-K003FT1 A RX CO-PAYM 65.10 65.10 65.00 0.10 0.00 0.00 03/29/22

> 442-K003J40 A RX CO-PAYM 59.09 59.09 59.00 0.09 0.00 0.00 09/12/23

> 442-K003R66 A C (MEANS T 50.08 50.08 50.00 0.08 0.00 0.00 09/12/23

> END OF REPORT...PRESS RETURN TO CONTINUE

### Cross-Servicing Re-Referred Bills Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cross-Servicing Re-Referred Bills Report lists bills that have been re-referred to Cross-Servicing. The user is prompted to enter a date range for the re-referrals. The report includes the bill number (*Bill#),* the AR Category, the debtor’s name (*Debtor Name*), the debtor’s full social security number (*SSN*), the date of the re-referral (*Re-Refer Date*), the original referral amount (*Orig Amt*), the current amount (*Curr Amt*), the dollar amount difference between the original referral amount and the current amount if any (*Diff Amt*), the reason for the re-referral (Reason), and the user (*USER ID*). The USER ID is the name of person who made the re-referral.

1.  At the Select Cross-Servicing Menu Option: prompt, enter: Cross-Servicing Re-Referred Bills Report.
2.  Enter a Begin Date and an End Date or take the system defaults.
3.  A prompt displays asking Do you want to capture report data for an Excel document? NO//
4.  The default is (N)o.
5.  If (N)o is selected or entered, the system displays:

> It is recommended that you Queue this report to a device that is 132 characters wide.

> DEVICE: HOME//

6.  If (Y)es is entered, the following message displays:

> To capture as an Excel format, it is recommended that you queue this report to a spool device with margins of 256 and page length of 99999 (e.g., spoolname;256;99999). This should help avoid wrapping problems.

> Another method would be to set up your terminal to capture the detail report data. On some terminals, this can be done by invoking 'Logging' or clicking on the 'Tools' menu above, then click on 'Capture Incoming Data' to save to Desktop. To avoid undesired wrapping of the data saved to the file, change the DISPLAY screen width size to 132 and you can enter '0;256;99999' at the 'DEVICE:' prompt.

> DEVICE: HOME//

<span id="_Hlk169269714" class="anchor"></span>Figure 23: Cross-Servicing Re-Referred Bills Report

Cross-Servicing Re-Referred Bills Report -- Run Date: 03 Jun 2024 11:06 am -- Page 1

Re-Referred Dates from 01 Jan 2016 to 03 Jun 2024

Bill \# AR Cat Debtor Name PT ID Re-Refer Dt Orig Amt Curr Amt Diff Amt Reason User ID

===============================================================================================================

442-K003AK1 RX CO-PAY AAA,DDDDD E Axxxx 04/23/24 \$72.82 \$72.82 Recall Error JONES, B

END OF REPORT...PRESS RETURN TO CONTINUE

### Cross-Servicing Recall Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cross-Servicing Recall Report lists the bills that have been recalled from Cross-Servicing. The user has the option of sorting the report by bill number or debtor name. The report includes the bill number (*BILL NO.),* the AR Category, the debtor’s name (*DEBTOR*), the Pt ID (first initial last name, last four of *SSN*), the amount recalled from Cross-Servicing (*RECL AMT*), the date of the recall (*RECL DATE*), the reason for the recall (*RECALL RSN*) and user (USER ID). The USER ID is the name of person who placed the recall or POSTMASTER after the batch process has run.

1.  At the Select Cross-Servicing Menu Option: prompt, enter: Cross-Servicing Recall Report.
19. Choose to sort the report by bill number or debtor’s name by entering 1 \[Bill Number\] or 2 \[Debtor Name\] at the Select one of the following: prompt.
20. Choose a Date Range From and Date Range To.
21. A prompt displays asking to CAPTURE report data to an Excel document?? NO//

> The default is (N)o.

> If (Y)es is entered, the following message displays:

> To capture as an Excel format, it is recommended that you queue this report to a spool device with margins of 256 and page length of 99999 (e.g., spoolname;256;99999). This should help avoid wrapping problems.

> Another method would be to set up your terminal to capture the detail report data. On some terminals, this can be done by invoking 'Logging' or clicking on the 'Tools' menu above, then click on 'Capture Incoming Data' to save to Desktop. To avoid undesired wrapping of the data saved to the file, change the DISPLAY screen width size to 132 and you can enter '0;256;99999' at the 'DEVICE:' prompt.

8.  To avoid undesired wrapping of the data saved to the file, enter '0;256;999' at the 'DEVICE:' prompt.
22.  To queue the report to a MailMan message, at the DEVICE prompt enter the letter ‘Q’:

> DEVICE: QUEUE TO PRINT ON

> DEVICE: HFS FILE =\> MESSAGE

> Subject: \[Enter message subject\]

> Select one of the following:

> M Me

> P Postmaster

> From whom: Me//

> Send mail to: CSUSER,ONE // CSUSER,ONE (default will display here)

> Select basket to send to: IN//

> And Send to:

> Requested Start Time: NOW// (Enter time to run report. NOW is the default)

> Report compilation has started with task# 999999.

23. Otherwise, press \[Enter\] to view the complete report.
24. The list of bills recalled from Cross-Servicing at the time of the report output will display according to the sort option selected (Figure 24).
9.  Once a debt has been manually flagged in VistA for recall from Cross-Servicing, the bill number, debtor’s name, patient ID, user ID and recall reason will display in the Recall Report, however, the recall amount and recall date will not display until after the Recall Batch Job has processed (the User ID in this case will be POSTMASTER).

<span id="_Hlk169269757" class="anchor"></span>Figure 24: Cross-Servicing Recall Report (Sorted by Bill Number)

PAGE 1 CROSS-SERVICING RECALL REPORT (SORTED BY BILL NUMBER) 06/03/24

------------------------------------------------------------------------------------------

BILL NO. AR CAT DEBTOR Pt ID RECL AMT RECL DT RECALL RSN USER ID

---------- ---------- ---------------- ----- --------- -------- ---------- -------

442-K002X43 C (MEANS T ALBBBBBBBB,AAAAA A5584 157.84 02/14/23 05-DEBTOR POSTMASTER

442-K002Y6T RX CO-PAYM ALDDDDD,BBBBBB K A0201 29.05 11/15/22 06-DEBTOR POSTMASTER

442-K002YJE CHOICE OPT ADDDD,AAAAAA LLL A7364 30.05 11/29/22 05-DEBTOR POSTMASTER

442-K002ZAR RX CO-PAYM PPPPPPP,ADDDDD P P6099 29.05 11/01/22 05-DEBTOR POSTMASTER

442-K00301Y RX CO-PAYM AGGGGGGG,CCCCC L A1073 37.15 01/31/23 03-BANKRUP POSTMASTER

442-K00302M RX CO-PAYM KKKKKKKKKKK,DDDD K5822 61.10 11/01/22 05-DEBTOR POSTMASTER

442-K00307U RX CO-PAYM GGGG,SHHHHHH CCC G6405 41.65 11/01/22 05-DEBTOR POSTMASTER

442-K0030EG RX CO-PAYM LLLLLLLL,SSSS AN L3910 28.04 11/01/22 05-DEBTOR POSTMASTER

442-K0030WT RX CO-PAYM KGGGGGG,VVVVV K4702 26.04 11/01/22 05-DEBTOR POSTMASTER

442-K0030XB C (MEANS T AKKK,ARRRR MMMMM A4185 50.08 11/08/22 06-DEBTOR POSTMASTER

442-K0031DI RX CO-PAYM DLLLLL,RURRR AA D2221 89.35 11/15/22 03-BANKRUP POSTMASTER

442-K00330S RX CO-PAYM ALBBBBBBBB,AAAAA A5584 28.28 02/21/23 05-DEBTOR POSTMASTER

442-K0035MJ C (MEANS T GGGGGG,EEE DDDD G0945 50.08 02/07/23 03-BANKRUP POSTMASTER

442-K0036E8 C (MEANS T AKKK,MMMMMM DDD A0060 30.05 02/14/23 03-BANKRUP POSTMASTER

442-K0037LJ C (MEANS T ALBBBBBBBB,AAAAA A5584 100.16 02/14/23 05-DEBTOR POSTMASTER

442-K00383W C (MEANS T ACCCCCC,III TRRR A3221 103.36 04/16/24 08-AGENCY POSTMASTER

442-K0038EX RX CO-PAYM ABBBB,VVVVV EEEE A3055 45.07 11/15/22 08-AGENCY POSTMASTER

442-K00394J RX CO-PAYM PPPPPP,GGGGG BBB P1938 83.13 11/01/22 05-DEBTOR POSTMASTER

Type \<Enter\> to continue or '^' to exit:

### Cross-Servicing Stop Reactivate Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cross-Servicing Stop Reactivate Report\[RCTCSP STOP REACTIVATE REPORT\] allows the User to run the report for 1) a list of bills that have been stopped from Cross-Servicing, or Reactivated, or Both, or 2) a list of debtors that have been stopped from Cross-Servicing, or Reactivated, or Both.. The user may select a range of Debtors or all Debtors, and a range of dates or all dates. At the Bill level, the User may specify Divisions. The report default is the Debtor level.

EXAMPLE at Debtor level:

1.  From the Cross-Servicing Menu, enter: Cross-Servicing Stop Reactivate Report.
25. Select one of the following:

> C Currently Flagged

> R Reactivated

> B Both

> Run the Report for: B// oth

26. Select one of the following:

B Bill Level

D Debtor Level

Run the Report for: Debtor// Level

27. Start with Debtor: FIRST//

> Go to Debtor: LAST//

28. Select one of the following:

> A All Dates

> R Date Range

Include All Dates or Select by Date Range: Date Range//

> Date Entered From: 010117 (JAN 01, 2017)

> Date Entered To: T// 123117 (DEC 31, 2017)

29. A prompt displays asking Do you want to capture the output in Excel format? NO//

> The default is (N)o.

> If (N)o is entered, the following message displays:

> It is recommended that you Queue this report to a device that is 132 characters wide.

> If (Y)es is entered, the following message displays:

> To capture as an Excel format, it is recommended that you queue this report to a spool device with margins of 256 and page length of 99999 (e.g., spoolname;256;99999). This should help avoid wrapping problems.

> Another method would be to set up your terminal to capture the detail report data. On some terminals, this can be done by invoking 'Logging' or clicking on the 'Tools' menu above, then click on 'Capture Incoming Data' to save to Desktop. To avoid undesired wrapping of the data saved to the file, change the DISPLAY screen width size to 132 and you can enter '0;256;99999' at the 'DEVICE:' prompt.

30. To queue the report to a MailMan message, at the DEVICE prompt enter the letter ‘Q’:

> DEVICE: QUEUE TO PRINT ON

> DEVICE: HFS FILE =\> MESSAGE

> Subject: \[Enter message subject\]

> Select one of the following:

> M Me

> P Postmaster

> From whom: Me//

> Send mail to: CSUSER,ONE // CSUSER,ONE (default will display here)

> Select basket to send to: IN//

> And Send to:

> Requested Start Time: NOW// (enter time to run report), NOW is the default.

Otherwise, press \[Enter\] at the DEVICE prompt.

<span id="_Hlk169269831" class="anchor"></span>Figure 25: Cross-Servicing Stop Reactivate Report – Debtor Level

Date Range: All Cross-Servicing Stop Reactivate Report at Debtor Level Page: 1

Debtor Range: First:Last Currently Flagged, Reactivated, or Both: Both May 22, 2019@15:30

---------------------------------------------------------------------------------------------------------------

Debtor Name Pt ID SSN S/R Date Reason User

---------------------------------------------------------------------------------------------------------------AAA,DDDDD D ANNNN nnnnnnnnn S 04/15/19@0926 Other BBBBB,JJJJJJ N

AKKKK,MMMMM ANNNN nnnnnnnnn S 05/10/19@0834 Other BBBBB,JJJJJJ N

AKKKK,MMMMM ANNNN nnnnnnnnn R 05/10/19@0907 BBBBB,JJJJJJ N

AKKKK,MMMMM ANNNN nnnnnnnnn S 05/10/19@0948 Treasury Error BBBBB,JJJJJJ N

AKKKK,MMMMM ANNNN nnnnnnnnn R 05/12/19@2144 KKKKKKKK,CCCCCCCC

AKKKK,MMMMM ANNNN nnnnnnnnn S 05/12/19@2150 Other KKKKKKKK,CCCCCCCC

AKKKK,MMMMM ANNNN nnnnnnnnn R 05/12/19@2155 KKKKKKKK,CCCCCCCC

AKKKK,MMMMM ANNNN nnnnnnnnn S 05/12/19@2201 DMC Eligible KKKKKKKK,CCCCCCCC

AKKKK,MMMMM ANNNN nnnnnnnnn R 05/12/19@2239 KKKKKKKK,CCCCCCCC

ARRRR,WWWWWWW ZZZZZZZ ANNNN nnnnnnnnn S 04/24/19@1653 Other KKKKKKKK,CCCCCCCC

ARRRR,WWWWWWW ZZZZZZZ ANNNN nnnnnnnnn R 04/24/19@1706 KKKKKKKK,CCCCCCCC

ARRRR,WWWWWWW ZZZZZZZ ANNNN nnnnnnnnn S 04/24/19@2015 Treasury Error KKKKKKKK,CCCCCCCC

ARRRR,WWWWWWW ZZZZZZZ ANNNN nnnnnnnnn R 04/24/19@2017 KKKKKKKK,CCCCCCCC

ARRRR,WWWWWWW ZZZZZZZ ANNNN nnnnnnnnn S 04/26/19@1441 DMC Eligible FFFFFFFFFFF,AAAAA D

ARRRR,WWWWWWW ZZZZZZZ ANNNN nnnnnnnnn R 04/26/19@1445 FFFFFFFFFFF,AAAAA D

BBBBB,VVVVV EEEEEE ANNNN nnnnnnnnn S 04/01/19@2058 DMC Eligible KKKKKKKK,CCCCCCCC

BBBBB,VVVVV EEEEEE ANNNN nnnnnnnnn R 04/01/19@2100 KKKKKKKK,CCCCCCCC

BBBBB,VVVVV EEEEEE ANNNN nnnnnnnnn S 04/02/19@0744 Bankruptcy KKKKKKKK,CCCCCCCC

Type \<Enter\> to continue or '^' to exit:

EXAMPLE at Bill level:

1.  From the Cross-Servicing Menu, enter: Cross-Servicing Stop Reactivate Report.
31. Select one of the following:

> C Currently Flagged

> R Reactivated

> B Both

> Run the Report for: B// oth

32. Select one of the following:

B Bill Level

D Debtor Level

Run the Report for: Debtor// Bill Level

33. Start with Debtor: FIRST//

> Go to Debtor: LAST//

34. Select one of the following:

> A All Dates

> R Date Range

Include All Dates or Select by Date Range: Date Range//

> Date Entered From: 010117 (JAN 01, 2017)

> Date Entered To: T// 060324 (JUN 03, 2024)

35. Select one of the following:

> A All

> D Division

> Run the Report for: All// d Division

> Select MEDICAL CENTER DIVISION NAME: ??

> Choose from:

> 1 CHEYENNE VAMROC 442

> 2 CASPER 442GA

> 3 FORT COLLINS 442GC

> 4 GREELEY 442GD

> 5 SIDNEY 442GB

> 6 CHEYENNE MOC 442HK

> 7 IDES - F.E. WARREN AFB 442MA

> 8 RAWLINS 442QA

> 9 TORRINGTON 442QB

> 10 CHEYENNE VA DOMICILIARY 442BU

> Select MEDICAL CENTER DIVISION NAME: 1 CHEYENNE VAMROC 442

> Select MEDICAL CENTER DIVISION NAME: 4 GREELEY 442GD

> Select MEDICAL CENTER DIVISION NAME: 6 CHEYENNE MOC 442HK

> Select MEDICAL CENTER DIVISION NAME: \<ENTER\>

36. A prompt displays asking “Do you want to capture the output in Excel format? NO//

> The default is (N)o.

> If (N)o is entered, the following message displays:

> It is recommended that you Queue this report to a device that is 132 characters wide.

> If (Y)es is entered, the following message displays:

> To capture as an Excel format, it is recommended that you queue this report to a spool device with margins of 256 and page length of 99999 (e.g., spoolname;256;99999). This should help avoid wrapping problems.

> Another method would be to set up your terminal to capture the detail report data. On some terminals, this can be done by invoking 'Logging' or clicking on the 'Tools' menu above, then click on 'Capture Incoming Data' to save to Desktop. To avoid undesired wrapping of the data saved to the file, change the DISPLAY screen width size to 132 and you can enter '0;256;99999' at the 'DEVICE:' prompt.

<span id="_Hlk169269912" class="anchor"></span>Figure 26: Cross-Servicing Stop Reactivate Report – Bill Level

> Compiling Cross-Servicing Stop Reactivate Report. Please wait ...

> Date Range: 01/01/14 - 06/03/24 Cross-Servicing Stop Reactivate Report by Bill Page: 1

> Division(s): All Currently Flagged, Reactivated, or Both: Both Jun 03, 2024@11:53

> Debtor Range: ALL

> ------------------------------------------------------------------------------------------------------------------------------------

> Debtor Name Division Pt ID Bill# AR CAT Status Letter1 StopDate Reason CS STOP User

> ------------------------------------------------------------------------------------------------------------------------------------

> ALLLLL,ADDDDD LLLLL 442 A9699 442-K0038Y6 RX CO-PAYM ACTIVE 11/24/19 01/01/24 BANKRUPTC ADD GGGGGGGGG,P

> ARRRRRRR,CCCCCCC SSSSSSS 442 A7809 442-K705E3S RX CO-PAYM COLLECTED/C 06/24/17 08/09/18 REJECTED DEL MMMMMMMMM,N

> ARRRRRRR,CCCCCCC SSSSSSS 442 A7809 442-K705E3S RX CO-PAYM COLLECTED/C 06/24/17 08/09/18 REJECTED DEL MMMMMMMMM,N

> ARRRRRRR,CCCCCCC SSSSSSS 442 A7809 442-K705E3S RX CO-PAYM COLLECTED/C 06/24/17 08/09/18 REJECTED DEL GGGGG,FFFFFF

> BBBBB,NNN RRRRRRR 442 B0852 442-K703HBK RX CO-PAYM COLLECTED/C 12/24/16 04/01/19 OTHER DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K7048PX RX CO-PAYM COLLECTED/C 02/24/17 05/01/19 OTHER DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K704J39 RX CO-PAYM COLLECTED/C 03/24/17 06/03/19 OTHER DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K704WXA RX CO-PAYM ACTIVE 04/24/17 07/01/19 OTHER DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K705C7D RX CO-PAYM ACTIVE 06/24/17 07/25/19 OTHER DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K705PNC RX CO-PAYM COLLECTED/C 07/24/17 03/20/19 OTHER DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K803BPQ RX CO-PAYM COLLECTED/C 11/24/17 08/01/19 OTHER DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K803PXT RX CO-PAYM COLLECTED/C 12/24/17 09/03/19 OTHER DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K803R04 C (MEANS T COLLECTED/C 12/24/17 DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K803T46 C (MEANS T ACTIVE 01/24/18 09/03/19 OTHER DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K8047NC C (MEANS T COLLECTED/C 02/24/18 10/01/19 OTHER DEL NNNNN,IIIIII

> BBBBB,NNN RRRRRRR 442 B0852 442-K804GSD C (MEANS T ACTIVE 03/24/18 DEL NNNNN,IIIIII

> Type \<Enter\> to continue or '^' to exit:

### Debt Referral Reject Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Debt Referral Reject Report lists the rejected bills by Debtor Name from the Unprocessable Files from AITC, DMC, and Treasury (where applicable). The report includes the bill number (*BILL \#*), the AR Category, the debtor’s name (*DEBTOR*), SSN, the record type (*TYP*), action code (*ACTNCD*), reject date (*REJECT DATE*), the source of the reject (*SRC*), and the error codes (*ERROR CODES*).

For the detailed report, the reject reasons associated with the error codes will also display.

1.  From the Cross-Servicing Menu, enter: Debt Referral Reject Report.
37. Enter the date range of the report at the following prompt:

> FROM: T-7//

> TO: T//

> Dates can be in MMDDYYYY (10272014) or MMM DD, YYYY (OCT 27, 2014) format.

> Note that the default date range is a one-week timeframe from the day the report is being run.

38. At the Group Error Codes: Brief or Detail: (B/D):B// prompt, choose between Brief and Detail. Note that the default is Brief. The descriptions of each are below:
- If (B)rief, all error codes for a bill will be concatenated into one string and displayed with a single bill without error descriptions. One line per bill with a sum of all of the error codes.
- If (D)etail, each error code will be accompanied by an error description. Thus, there may be multiple lines per bill.
39. Select how to sort the report at the Sort by:1// prompt, choosing one of the following. (The default is by Bill Number.)

> 1 Bill Number

> 2 Debtor Name

> 3 CS Reject Date

40. Once the primary sort is selected, an Include Only: AITC, DMC, TREASURY or 'ALL': (A/D/T/ALL): ALL// prompt displays for a secondary sort of the reject source. Choose from the following:

> (A)ITC: Rejects from AITC

> (D)MC: Rejects from DMC

> (T)reasury: Rejects from Treasury

> (ALL): Rejects from all sources (Default)

41. Next, choose the sort order of the report (A)scending or (D)escending. Note that the default is (A)scending.
42. If the Detail option is selected, the Excel prompt will not display. If the Brief option is selected, a prompt displays asking to CAPTURE report data to an Excel document?? NO//

> The default is (N)o.

> If (Y)es is entered, the following message displays:

> To capture as an Excel format, it is recommended that you queue this report to a spool device with margins of 256 and page length of 99999 (e.g., spoolname;256;99999). This should help avoid wrapping problems.

> Another method would be to set up your terminal to capture the detail report data. On some terminals, this can be done by invoking 'Logging' or clicking on the 'Tools' menu above, then click on 'Capture Incoming Data' to save to Desktop. To avoid undesired wrapping of the data saved to the file, change the DISPLAY screen width size to 132 and you can enter '0;256;99999' at the 'DEVICE:' prompt.

10. To avoid undesired wrapping of the data saved to the file, enter '0;256;999' at the 'DEVICE:' prompt.
43. To queue the report to a MailMan message, at the DEVICE prompt, enter the letter ‘Q’:

> DEVICE: QUEUE TO PRINT ON

> DEVICE: HFS FILE =\> MESSAGE

> Subject: \[Enter message subject\]

> Select one of the following:

> M Me

> P Postmaster

> From whom: Me//

> Send mail to: CSUSER,ONE // CSUSER,ONE (default will display here)

> Select basket to send to: IN//

> And Send to:

> Requested Start Time: NOW// (Enter time to run report. NOW is the default)

> Report compilation has started with task# 999999.

44. The report will display based on the selected parameters in the previous steps (refer to the figures below for samples of the Debt Referral Reject Report).

<span id="_Toc25567353" class="anchor"></span>Figure 27: Debt Referral Reject Report (Brief – Treasury - Sorted by Bill Number)

PAGE 1 DEBT REFERRAL REJECT REPORT (SORTED BY BILL NO. \<ASC\>) 06/03/24

---------------------------------------------------------------------------------------

BILL NO. AR CAT DEBTOR Pt ID TYP ACTNCD REJECT DATE SRC ERR CODES

----------- ---------- ------------------- ----- --- ------ ----------- --- ---------

442-K604KH5 RX CO-PAYM BBBBBBBBBB,SSS L XXXX 1 A 02/13/18 T 7C

442-K604KH5 RX CO-PAYM BBBBBBBBBB,SSS L XXXX 2 B 02/13/18 T 7C

442-K604KH5 RX CO-PAYM BBBBBBBBBB,SSS L XXXX 3 A 02/13/18 T 7C

442-K605I5L RX CO-PAYM MMMMMMMM,SHHHHHH TH XXXX 2 B 08/10/17 T 3E

442-K605I5L RX CO-PAYM MMMMMMMM,SHHHHHH TH XXXX 2 B 08/17/17 T 3E

442-K605I5L RX CO-PAYM MMMMMMMM,SHHHHHH TH XXXX 2 B 08/31/17 T 3E

442-K605I5L RX CO-PAYM MMMMMMMM,SHHHHHH TH XXXX 2 B 09/18/17 T 3E

442-K605I5L RX CO-PAYM MMMMMMMM,SHHHHHH TH XXXX 2 B 09/28/17 T 3E

442-K605KPJ C (MEANS T KLLLLL,BBBBBB L XXXX 1 A 02/13/18 T 7C

442-K605KPJ C (MEANS T KLLLLL,BBBBBB L XXXX 2 B 02/13/18 T 7C

442-K605KPJ C (MEANS T KLLLLL,BBBBBB L XXXX 3 A 02/13/18 T 7C

442-K605XUY RX CO-PAYM PPPPIN,BLLLLL BRRRR XXXX 2C A 12/19/17 T 3K

442-K605XUY RX CO-PAYM PPPPIN,BLLLLL BRRRR XXXX 2C A 12/19/17 T 3K

442-K60609L RX CO-PAYM LMMMMM,TTTTTTT XXXX 2C A 12/19/17 T 3K

442-K60609L RX CO-PAYM LMMMMM,TTTTTTT XXXX 2C A 12/19/17 T 3K

442-K6068KN C (MEANS T SPPPP,HHHH PPPP XXXX 2C A 12/19/17 T 3K

Type \<Enter\> to continue or '^' to exit:

### List IAI Error Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To accompany the Debt Referral Reject Report, the Cross-Servicing Menu also contains the List IAI Error Codes option. Selecting this option lists the various error codes that will display in the Debt Referral Reject Report. In addition to the error codes, the list contains the field name / action, record type, and error message.

To queue the report to a MailMan message, enter the letter ‘Q’ at the DEVICE prompt:

DEVICE: QUEUE TO PRINT ON

DEVICE: HFS FILE =\> MESSAGE

Subject: \[Enter message subject\]

Select one of the following:

M Me

P Postmaster

From whom: Me//

Send mail to: CSUSER,ONE // CSUSER,ONE (default will display here)

Select basket to send to: IN//

And Send to:

Requested Start Time: NOW// (Enter time to run report. NOW is the default)

Report compilation has started with task# 999999.

Otherwise, press \[Enter\] at the DEVICE prompt.

Refer to *Appendix B. Cross-Servicing IAI Error Codes* for a complete list of the error codes.

<span id="_Toc25567354" class="anchor"></span>Figure 28: List of IAI Error Codes (Codes 10 – 17)

TCS IAI ERROR CODES LIST MAY 24, 2019@11:04 PAGE 1

RECORD

CD FIELD NAME/ACTION TYPE ERROR MESSAGE

10 Debtor TIN 2 Debtor already in debtor table.

11 Debtor TIN 2 This is a Joint & Several debt.

12 Debtor TIN 2 If Debtor TIN is provided, a valid TIN

Type must be Entered.

13 Debtor TIN 2,2C,4,6 Debtor TIN must be Numeric.

14 Referred Debt 1 Delinquent amount not numeric or amount \<

Balance \$25 limit.

15 Referred Debt 1 For adjust action, amount cannot be zero.

Balance

16 Referred Debt 1 Cannot decrease a debt with existing

Balance current balance of zero.

17 Referred Debt 1 For refund record, there is no offset

Balance payment found for the offset year / date,

or year / date is invalid.

### Print Cross-Servicing Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Cross-Servicing Report provides the current balance of all bills referred and re-referred to Cross-Servicing. The report output contains the bill number (*BILL NO.*), the AR Category, the debtor’s name (*DEBTOR*), the SSN, the original amount of the bill (*ORIG AMT*), the date the bill was referred to Cross-Servicing (*CS REF DT*), and the current amount of the bill (*CURR DEBT*).

1.  At the Select Cross-Servicing Menu Option: prompt, enter: Print Cross-Servicing Report.
45. Select to sort the report by bill number, debtor name, or the date the bill was referred to Cross-Servicing by entering 1 \[Bill Number\], 2 \[Debtor Name\], or 3 \[CS Referred Date\] at the Select one of the following: prompt.
46. Choose a Date Range From and Date Range To.
47. To queue the report to a MailMan message, at the DEVICE prompt enter the letter ‘Q’:

DEVICE: QUEUE TO PRINT ON

DEVICE: HFS FILE =\> MESSAGE

Subject: \[Enter message subject\]

Select one of the following:

M Me

P Postmaster

From whom: Me//

Send mail to: CSUSER,ONE // CSUSER,ONE (default will display here)

Select basket to send to: IN//

And Send to:

Requested Start Time: NOW// (Enter time to run report. NOW is the default)

Report compilation has started with task# 999999.

48. Otherwise, press \[Enter\] to view the complete report.
49. A list of all bills referred to Cross-Servicing at the time the report was run will display according to the sort option selected.

<span id="_Toc25567355" class="anchor"></span>Figure 29: Print Cross-Servicing Report (Sorted by Bill Number)

PAGE 1 BILLS AT CROSS-SERVICING (SORTED BY BILL NO.) 06/03/24

----------------------------------------------------------------------------------------

BILL NO. AR CAT DEBTOR Pt ID ORIG AMT CS REF DATE CURR AMT

---- --- ------ ------ ----- -------- ----------- --------

442-K505Y74 RX CO-PAYM THHHHHHHHH,AAAAAA J T4980 122.09 05/11/21 122.09

442-K505YYB C (MEANS T KKKKK,WWWWWW OOOOO K3815 47.03 05/11/21 47.03

442-K505YZZ RX CO-PAYM MAAAAA,BTTTTT KYY M5932 28.09 06/15/21 28.07

442-K505ZBL C (MEANS T MHHHHHH,RRRR M8257 31.52 05/11/21 31.52

442-K505ZG1 RX CO-PAYM SHRRRRR,TTTTT JJJJ S5414 47.03 05/11/21 47.03

442-K5060MG C (MEANS T CRRRRRRRRL,GGGGGGG C2226 52.04 05/11/21 52.04

442-K5060S5 RX CO-PAYM FFFFF,WWWWW NNN F4379 33.52 05/11/21 33.52

442-K50613B RX CO-PAYM ODDD,DDDDD RRRRRRR O6927 37.53 05/11/21 37.53

442-K50617H RX CO-PAYM CIIIIII,HRRRRRRR VI C0367 206.64 05/11/21 206.64

442-K5062GD RX CO-PAYM PPPPPP,NNNNN JJJJJJ P4320 28.02 05/11/21 28.02

442-K5063R1 RX CO-PAYM TTTTTT,NNNN MMMM T7782 28.02 05/11/21 28.02

Type \<Enter\> to continue or '^' to exit:

### Reconciliation Report – Cross-Servicing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reconciliation Report - Cross-Servicing \[RCTCSP RECONCIL REPORT\] lists all of the debt that has been returned from Cross-Servicing by Treasury for reconciliation. The report columns include the debtor’s name (DEBTOR), bill number (BILL NO.), patient ID (Pt ID) and the returned and recall effective date. The report also includes the return reason description and any required supporting information required (refer to the following sub-sections).

1.  From the Cross-Servicing Menu, enter: Reconciliation Report.
50. Enter the date range of the report at the following prompt:

> FROM: T-30//

> TO: T//

> Dates can be in MMDDYYYY (10272014) or MMM DD, YYYY (OCT 27, 2014) format.

> Note that the default date range is a one-month timeframe from the day the report is being run.

51. A prompt displays asking to CAPTURE report data to an Excel document? NO//

> The default is (N)o.

> If (Y)es is entered, the following message displays:

> To capture as an Excel format, it is recommended that you queue this report to a spool device with margins of 256 and page length of 99999 (e.g., spoolname;256;99999). This should help avoid wrapping problems.

> Another method would be to set up your terminal to capture the detail report data. On some terminals, this can be done by invoking 'Logging' or clicking on the 'Tools' menu above, then click on 'Capture Incoming Data' to save to Desktop. To avoid undesired wrapping of the data saved to the file, change the DISPLAY screen width size to 132 and you can enter '0;256;99999' at the 'DEVICE:' prompt.

11. To avoid undesired wrapping of the data saved to the file, enter '0;256;999' at the 'DEVICE:' prompt.
52. To queue the report to a MailMan message, at the DEVICE prompt enter the letter Q:

DEVICE: QUEUE TO PRINT ON

DEVICE: HFS FILE =\> MESSAGE

Subject: \[Enter message subject\]

Select one of the following:

M Me

P Postmaster

From whom: Me//

Send mail to: CSUSER,ONE // CSUSER,ONE (default will display here)

Select basket to send to: IN//

And Send to:

Requested Start Time: NOW// (Enter time to run report. NOW is the default)

Report compilation has started with task# 999999.

53. Otherwise, press \[Enter\] to view the complete report.
54. The Reconciliation Report will display.

<span id="_Toc25567356" class="anchor"></span>Figure 30: Print Reconciliation Report

PAGE 1 RECONCILIATION REPORT 05/24/19

-----------------------------------------------------------------------------

DEBTOR BILL NO. Pt ID Amount Recall Date

Refer Eff. Dt Return

---------------- ----------- ----- -------- -------- --------

ABBBBB,TTTT 442-K6068QS nnnnn 0.00 04/22/17

PAID IN FULL (OUTSIDE OF A PAYMENT AGREEMENT)

ALLLLLLL,AAAAAAA 442-K703UL2 nnnnn 0.00 10/14/17

SATISFIED PA - PAID IN FULL OR COMPROMISED

Compromise, Please write this bill off by the manual process

Amount (not collected): 0.00

ALRRRRR,BBBBBB M 442-K703ERX nnnnn 0.00 07/20/17

SYSTEM COMPROMISED (BALANCE BELOW \$25)

BAAAAAAAAA,RRRR 442-K605YP8 nnnnn 0.00 04/25/17

RECALLED

#### Compromise Offer

If the Return Reason Code = ‘P’ and the Compromise Indicator = ‘Y’ is sent in the Reconciliation IAI file, then a Compromise Amount will also be included to identify the amount that is not collected. The Reconciliation Report will display the Return Reason Code as ‘Satisfied PA – Paid in Full or Compromised’, a secondary note stating ‘Compromise, Please write this bill off by the manual process’, and the compromise amount that has not been collected and is to be written off manually.

#### Bankruptcy

If the Return Reason Code = ‘B’ is sent, then the Bankruptcy Date will also be included. The Reconciliation Report will display the Return Reason Code as ‘Administrative Resolution Approved for Bankruptcy’ and the Bankruptcy Date.

#### Death

If the Return Reason Code = ‘D’ is sent, then the Date of Death will be included. The Reconciliation Report will display the Return Reason Code as ‘Administrative Resolution Approved for Death’ and the Date of Death.

#### Other Returned Reasons

The following Return Reason Codes may also be returned in the Reconciliation file from Treasury.

> Z Uncollectable

> W Administrative Resolution Approved for Inability to Pay

> E Administrative Resolution Approved for Entity out of Business

> T CA Agrees – Complaint – Stop Collection Activity

> Y CA Agrees – Debt amount is incorrect – Stop Collection Activity

> C CA Agrees – Congressional Dispute – Stop Collection Activity

> M CA Agrees – Miscellaneous Dispute – Stop Collection Activity

> G CA Agrees – Wrong Debtor – Stop Collection Activity

> V CA Agrees – Previously Paid – Stop Collection Activity

> H CA Agrees – Previously Resolved – Stop Collection Activity

> X Dispute Timer Expired

> F Paid in Full (Outside of a Payment Agreement)

> S System Compromised (balance below \$25)

> R Recalled (Note: Once a bill is recalled from Cross-Servicing, it cannot be re-referred.)

> A Manually Returned to Agency

> N Proof of Debt documentation not provided – Stop Collection Activity

> Q Proof of Debt Timer Expired

### Treasury Cross-Servicing IAI Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Treasury Cross-Servicing IAI Report \[RCTCSP IAI REPORT\] displays a record of current VHA bills at Treasury. It is a tool that can be used to identify bills erroneously

listed in a referral status in VistA when reconciled with the Print Cross-Servicing Report.

1.  Select Cross-Servicing Menu \<TEST ACCOUNT\> Option: TREASury Cross-Servicing IAI Report.

> Select one of the following:

> 1 06/03/17

> 2 05/30/17

> Print IAI report date?: 1// 06/03/17

> CAPTURE Report data to an Excel Document? NO//

55. To queue the report to a MailMan message, enter the letter ‘Q’ at the DEVICE prompt:

> DEVICE: QUEUE TO PRINT ON

> DEVICE: HFS FILE =\> MESSAGE

> Subject: \[Enter message subject\]

> Select one of the following:

> M Me

> P Postmaster

> From whom: Me//

> Send mail to: CSUSER,ONE // CSUSER,ONE (default will display here)

> Select basket to send to: IN//

> And Send to:

> Requested Start Time: NOW// (Enter time to run report. NOW is the default)

> Report compilation has started with task# 999999.

> Otherwise, press \[Enter\] at the DEVICE prompt.

<span id="_Toc25567357" class="anchor"></span>Figure 31: Treasury Cross-Servicing IAI Report

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/008.png)

### Multiple Referral Programs Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Multiple Referral Programs Report \[PRCAC MULT REF RPT\], identifies any bills that may be referred for debt collection to multiple debt referral programs. It is a tool that can be used to determine if a bill or debtor has been referred to other programs.

1.  At the Select Cross-Servicing Menu Option: prompt, enter: Multiple Referral ProgramsReport.
2.  To capture as an Excel format, it is recommended that you queue this report to a spool device with margins of 256 and page length of 99999 (e.g., spoolname;256;99999). This should help avoid wrapping problems.
3.  Another method would be to set up your terminal to capture the detail report data. On some terminals, this can be done by invoking Logging or clicking on the Tools menu above, then click on Capture Incoming Data to save to the Desktop. To avoid undesired wrapping of the data saved to the file, change the DISPLAY screen width size to 132 and you can enter 0;256;99999 at the 'DEVICE: prompt.
4.  To avoid undesired wrapping of the data saved to the file, enter 0;256;999 at the DEVICE: prompt.
5.  To queue the report to a MailMan message, at the DEVICE prompt enter the letter Q:
6.  The report will print to the location selected.

## Recall/Reactivate TCSP Referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Recall/Reactivate TCSP Referral options are used to recall a debt or debtor (all debt for the debtor) from Cross-Servicing. Once a bill is recalled from Cross-Servicing, the bill can be RE-REFERRED if it is still recalled, is in an Active status, and has no conditions that will prevent it from being re-referred (e.g. Debtor now deceased, etc.).

Table 4‑1 provides the scenarios for when the recall debt / debtor functionality should be used for debt referred to Cross-Servicing, the recall reason, and the action in VistA.

The following sub-sections outline the steps for recalling a debt / debtor from Cross-Servicing.

<span id="_Ref10208984" class="anchor"></span>Table 4‑1: Recall Scenarios for Cross-Serviced Debt

| Scenario                                                                                                                                                                                                                                         | Recall Reason To Use                              | VistA Action                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Bankruptcy                                                                                                                                                                                                                                       | 03 – Bankruptcy with Automatic Stay               | Cancel Copayment (Suspend Copayment)                                                                                            |
| Debtor Deceased                                                                                                                                                                                                                                  | 06 – Debtor is Deceased                           | Termination of debt when reclamation requirements are met                                                                       |
| Debtor Disabled / Inability to Pay                                                                                                                                                                                                               | 05 – Debtor is Disabled with the Inability to Pay | Termination of debt or write-off when it’s deemed that further collection activity will not be successful or not cost effective |
| Hardship / Waiver determined in favor of debtor                                                                                                                                                                                                  | 07 – Agency is Forgiving Debt                     | Cancel Copayment (Waive Debt)                                                                                                   |
| If DMC sets up an offset of VA benefits after a debt has been referred to Cross-Servicing, and the Veteran requests to be removed from the Cross-Servicing process, and VA can collect the full debt within three years through internal offset. | 08 – Agency can collect through internal offset   | Enter DMC LESSER AMOUNT                                                                                                         |
| Other                                                                                                                                                                                                                                            | 01 – Debt Referred in Error                       | Add Debtor Comment Explanation                                                                                                  |
| Service-Connected Determination or Adjudication                                                                                                                                                                                                  | 01 – Debt Referred in Error                       | Reset Pharmacy or Cancel Copayment                                                                                              |

<span id="_Toc169093104" class="anchor"></span>Table B‑1: Cross-Servicing IAI Error Codes

### Recall TCSP Referral for a Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a week, VistA automatically recalls bills that are less than \$25 and have had no payment activity in 365 days or more or have been Cancelled. When bills are automatically recalled, the Recall Reason of “07 - Agency is Forgiving Debt” is automatically added as the Recall Reason.

In addition to the automatic recalls, the Cross-Servicing functionality allows for the manual recall of bills referred to Cross-Servicing. Manual recalls are performed using the Bill Recall/Reactivate TCSP Referral \[RCTCSP RECALLB\] option. This option is a toggle that flags the bill to be recalled the next time the Recall Batch Job runs. Once the Recall Batch Job runs, the Cross-Servicing referred information on the profile screens for that bill is deleted. Where required, <u>and before the Recall Batch Job runs</u>, use the option again to delete the “recall flag”.

12. Once a bill is manually recalled, VistA automatically calculates and applies all administrative fees and interest to the recalled bill from the CS Referred Date to the CS Recall Date. This does NOT apply to those bills that have been automatically recalled due to no payment activity in 365 days or more and if a bill is less than \$25.

The steps below outline the prompts for manually recalling a bill from Cross-Servicing:

1.  From the Cross-Servicing Menu, enter: BILL RECALL/REACTIVATE TCSP REFERRAL or RCTCSP RECALLB.
56. Enter the bill number at the ACCOUNTS RECEIVABLE BILL NO. prompt.
57. The following confirmation message will display: Are you sure you want to set this bill to be recalled from Cross-Servicing?
58. Enter: Y for “Yes”.
59. The next step is to enter the reason for the recall at the TCSP Recall Reason prompt. The available reasons for recalling a bill include the following:

> 01 DEBT REFERRED IN ERROR

> 07 AGENCY IS FORGIVING DEBT

> 08 AGENCY CAN COLLECT THROUGH INTERNAL OFFSET

60. After you have entered the reason for recall, the following confirmation displays: Setting this bill for Recall from Cross-Servicing is complete.
61. Using this functionality flags the bill to be recalled from Cross-Servicing when the next Recall Batch Job runs.
62. When the Recall Batch Job runs, a confirmation message will be transmitted through MailMan with the Subject line: CS RECALLS SENT ON \[MM/DD/YYYY\]
63. Once the batch process is complete, the Cross-Servicing-referred information for this bill will be deleted from the profile screens. Also, the Recall Reason and Recall Date will display on the following screens (refer to *Section 3 Cross-Servicing Fields & Messages* for the location of the Recall Reason and Recall Date on the following screens):
    - Full Account Profile (bill sub-screen for the recalled bill)
    - Brief Account Profile (bill sub-screen for the recalled bill)
    - Profile of Accounts Receivable
    - Bill Profile
    - Account Profile (from Agent Cashiers Menu)
13. Recalling all of the bills referred to Cross-Servicing (for a given debtor) also recalls the debtor. The informational display, “x Debt Referred to Cross-Servicing” and the “Total CS Debt” on the above screens will remain on the debtor’s account until all of the bills are recalled from Cross-Servicing.

### Debtor Recall TCSP Referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Debtor Recall/Reactivate TCSP Referral \[RCTCSP RECALLD\] option to recall a debtor from being referred to Cross-Servicing. By recalling a debtor, all debt on a debtor’s account that has been referred to Cross-Servicing is recalled. Future debts for that same Debtor meeting the Cross-Servicing criteria will be Cross-Serviced.

The steps below outline the prompts for recalling a Cross-Servicing referral for a debtor:

1.  From the Cross-Servicing Menu, enter: DEBTOR RECALL/REACTIVATE TCSP REFERRAL or RCTCSP RECALLD.
64. Enter the debtor’s name at the Select AR Debtor prompt.
65. The following confirmation message will display: Are you sure you want to recall this debtor and bills from Cross-Servicing?
66. Enter: Y for “Yes”.
67. The next step is to enter the reason for the recall at the TCSP Recall Reason prompt. The available reasons include the following:

> 03 BANKRUPTCY WITH AUTOMATIC STAY

> 05 DEBTOR IS DISABLED WITH INABILITY TO PAY

> 06 DEBTOR IS DECEASED

68. After you have entered the reason for recall, the following confirmation displays: Setting this debtor for Recall from Cross-Servicing is complete.
69. Using this functionality flags the debtor to be recalled from Cross-Servicing when the next Recall Batch Job runs.
70. When the recall batch process is run, a confirmation message will be transmitted through MailMan with the Subject line: CS RECALLS SENT ON \[MM/DD/YYYY\]
71. Once the batch process is complete, the Cross-Servicing referred information will be deleted on all bills for this debtor. The Recall Reason and Recall Date will display on the following screens (refer to *Section 3.2 Debt / Debtor Recalled from Cross-Servicing*) for the location of the Recall Reason and Recall Date on the various screens):

> a\. Full Account Profile (bill sub-screen for the recalled bill)

> b\. Brief Account Profile (bill sub-screen for the recalled bill)

> c\. Profile of Accounts Receivable

> d\. Bill Profile

> e\. Account Profile (from Agent Cashiers Menu)

### Reactivate Referral After Recall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the recall flag has been set and the Recall Batch Job has NOT run, the recall flag can be removed by completing the steps in the following sub-sections.

#### Reactivate Bill (Remove Recall Flag)

1.  Enter the option name: Bill Recall/Reactivate TCSP Referral
72. Press \[Enter\].
73. Enter the Bill Number at the Select ACCOUNTS RECEIVABLE BILL NO.: prompt.
74. The following message will display if the bill has been set for recall:

    This bill has already been set for recall from Cross-Servicing.Do you wish to delete the Cross-Servicing Recall for this bill? NO//
75. Enter: YES
76. The following message will display if the recall flag was removed successfully:

    Recall from Cross-Servicing has been deleted for this bill.
77. If the Recall Flag has been set on a bill and the Recall Batch Job <u>HAS</u> run, a message displays indicating that Recall Reactivation is not available.

> Not Available for Reactivation. The Recall Request Has Already Been Processed.

#### Reactivate Debtor (Remove Recall Flag)

1.  Enter the option name: Debtor Recall/Reactivate TCSP Referral
2.  Press \[Enter\].
3.  Enter the Debtor’s Name or SSN.
78. The following message will display if the debtor (and all Cross-Serviced bills) has been set for recall:

    This debtor has already been set for recall from Cross-Servicing.Do you wish to delete the Cross-Servicing Recall for this debtor? NO//
79. Enter: YES
80. The following message will display if the recall flag was removed successfully:

    Recall from Cross-Servicing has been deleted for this debtor.
81. If the Recall Flag has been set for the debtor and the Recall Batch Job <u>HAS</u> run, a message displays indicating that Recall Reactivation is not available, as indicated in the previous sub-section.

## Refer Returned CS Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Refer Returned CS Bill option allows a User to re-refer a Cross-Serviced bill that has been recalled or returned from Treasury and is in a current “Active” state. If the bill has been re-referred, and the batch job has not run yet, then the re-referral may be cancelled.

### First Time Re-referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Cross-Servicing Menu, select the option, Refer Returned CS Bill.
2.  At the Enter Bill Number for re-referral: prompt, enter the bill number to be re- referred to Cross-Servicing.
3.  The system will display the bill information to help identify the correct bill, including the debtor’s name, the status of the bill, and the debt amount.
4.  The system prompts the User to select a reason for the re-referral.

> Select one of the following:

> R Recall in error

> T Treasury reversal

> D Defaulted RPP

> O Other

> Select Reason for this re-referral:

> If “Other” is selected as the re-referral reason, the User is *required* to enter a 30 character, alpha-numeric description for the “Other” reason.

> Enter "Other" description:

82. The system then prompts:

> Are you sure you want to Re-refer this bill for Cross-Servicing? YES//

83. Press \<ENTER\> and the system displays the message:

> Bill is set to be re-referred to Cross-Servicing in the next weekly transmission

### Update a Re-referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the re-referral has not been processed by the weekly batch job yet, the re-referral may be updated.

1.  From the Cross-Servicing Menu, select the option, Refer Returned CS Bill.
2.  At the Enter Bill Number for re-referral: prompt, enter the bill number to be re- referred to Cross-Servicing.
3.  The system will display the bill information to help identify the correct bill, including the debtor’s name, the status of the bill, and the debt amount.
4.  The system then displays a message informing the User a re-referral was already made for this bill along with the name of the User who made the re-referral, the date the re-referral was requested, and the re-referral reason:

> Re-Referral has already been requested

> By MLTMKDSFK,JKLESDS on 05/20/2019 Reason: Defaulted RPP

84. The system prompts the User: Do you want to Cancel this Re-Referral? NO//

> \<Press ENTER\>

85. The system prompts: Do you want to Update this Re-Referral? NO//

> Enter \<YES\>

86. The system prompts the User to select a reason for the re-referral:

> Select one of the following:

> R Recall in error

> T Treasury reversal

> D Defaulted RPP

> O Other

> Select Reason for this re-referral:

87. If “Other” is selected as the re-referral reason, the User is required to enter a 30 character, alpha-numeric description for the “Other” reason.

> Enter "Other" description: then press \<ENTER\>

88. The system then prompts:

> Are you sure you want to Re-refer this bill for Cross-Servicing? YES//

> Press \<ENTER\>

89. The system displays the message:

> Bill is set to be re-referred to Cross-Servicing in the next weekly transmission

> Press \<ENTER\> to continue:

### Cancel a Re-referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Cross-Servicing Menu, select the option, Refer Returned CS Bill.
2.  At the Enter Bill Number for re-referral: prompt, enter the bill number to be re- referred to Cross-Servicing.
3.  The system will display the bill information to help identify the correct bill, including the debtor’s name, the status of the bill, and the debt amount.
4.  The system then displays a message informing the User a re-referral was already made for this bill along with the name of the User who made the re-referral, the date the re-referral was requested, and the re-referral reason:

> Re-Referral has already been requested

> By MLTMKDSFK,JKLESDS on 05/20/2019 Reason: Defaulted RPP

90. The system prompts the User: Do you want to Cancel this Re-Referral? NO//

> \<ENTER YES\>

91. The system displays a cancellation confirmation message:

> \*\*\* Re-Referral has been cancelled for this bill \*\*\*

## Stop/Reactivate TCSP Referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Stop/Reactivate TCSP Referral\[<u>RCTCSP STOP\]</u> option allows a User to 1) stop a bill (Stop/Reactivate TCSP Referral for a Bill) or 2) stop a Debtor (Stop/Reactivate TCSP Referral for a Debtor) from being referred to Cross-Servicing, and also to stop updates from being transmitted on the Cross-Serviced bill or Debtor (e.g., changes to debtor’s address, phone number, etc.). This ‘Stop’ toggle indicates to VistA to not send Cross-Servicing records to Treasury regarding this bill or Debtor. Once the stop is set, the option can be run again to delete the ‘Stop’ flag. Removing the stop allows this bill or Debtor to be processed again as a referral to Cross-Servicing and to allow updates to be sent on the bill / debtor’s account.

### Stop/Reactivate TCSP Referral for a Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Stop/Reactivate TCSP Referral for a Bill functionality is used to stop Cross-Servicing referral for a bill. Below are various reasons for stopping a Cross-Servicing referral and when these reasons should be used:

1.  Bankruptcy: Debtor has included VA in their bankruptcy petition and has provided proof of bankruptcy.
14. Review the date on the debtor’s account for the bankruptcy petition. Only bills that originated after the bankruptcy date can be marked with a stop reason of “Bankruptcy”.
92. Waiver: VA has granted waiver on outstanding bills not yet referred to Cross-Servicing. Or a waiver was received in a timely manner, and a decision has not yet been made.
93. Other: Stop the referral in order to research and verify the status of the referrals. (Stop the referral while awaiting bankruptcy paperwork, granting of waiver, etc.)
94. Rejected by Cross-Servicing: Reason automatically added to all debt rejected by Cross-Servicing from any source (Treasury, DMC, or AITC).

If Bankruptcy, Waiver, or Other is selected as the Stop Cross-Servicing Referral Reason, the user is required to enter an effective date. Below are the steps for setting the ‘Stop’ flag on a Cross-Servicing referral for a bill:

1.  From the Cross-Servicing Menu, select the option, Stop/Reactivate TCSP Referral. At the Enter Response: prompt, enter B.
95. At the Select ACCOUNTS RECEIVABLE BILL NO.: prompt, enter the bill number to be stopped from being referred to Cross-Servicing.
96. The system will display the bill information to help identify the correct bill, including the debtor’s name, the status of the bill, and the debt amount.
97. Additionally, the system will indicate whether or not the stop flag is set: Stop flag for Cross-Servicing Referral set? : NO
98. At the Are You Sure You Want To Stop the Cross-Servicing Referral for this bill?: prompt, type Y or YES and press the \[Enter\] key.
99. At the Enter Stop Cross-Servicing Reason: prompt, the following reasons are available. Enter the reason code and press the \[Enter\] key.

> B BANKRUPTCY

> W WAIVER

> O OTHER (If Other is entered, you will be prompted to enter a comment at the Stop Reason Comment prompt.)

> R REJECTED BY CROSS-SERVICING (automatically applied to debt rejected by Cross-Servicing)

100. At the Enter Effective Date: prompt, enter the effective date in MM/DD/YYYY format (if appropriate) or enter “T” (for Today) and press \[Enter\].
101. A Stop Cross-Servicing Referral complete message will display when the stop is completed.
15. Timing is critical. A request to stop a Cross-Servicing referral may NOT be honored because the referral has already occurred.

### Reactivate TCSP Referral for a Bill (Remove ‘Stop’ Flag)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Stop/Reactivate TCSP Referral for a Bill functionality is also used to reactivate a Cross-Servicing referral for a bill that was previously stopped (remove the ‘Stop’ flag) (refer to the steps below):

1.  From the Cross-Servicing Menu, enter the option: Stop/Reactivate TCSP Referral. Then, at the Enter Response: prompt, enter B.
2.  At the Select ACCOUNTS RECEIVABLE BILL NO.: prompt, enter the bill number to be re-referred to Cross-Servicing.
3.  The system will display the bill information to help identify the correct bill, including the debtor’s name, the status of the bill, and the debt amount.
4.  The following sample message will display (if the bill was previously stopped), with the effective date and reason entered at the time of the stop:

> Referral to Cross-Servicing has already been stopped for this bill

> Stop Cross-Servicing referral effective date: DEC 18, 2014

> Stop Cross-Servicing referral reason: WAIVER

> Do you wish to re-institute Cross-Servicing Referral for this bill? NO//

5.  Type Y or YES and press the \[Enter\] key.
6.  If the reactivate was successful, the following message will display: Bill is now eligible to be Referred to Cross-Servicing.
7.  Updates may continue on the bill and/or will be referred to Cross-Servicing in the next weekly transmission.

### Stop/Reactivate TCSP Referral for a Debtor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Stop/Reactivate TCSP Referral for a Debtor functionality is used to stop Cross-Servicing referral for a Debtor. Below are various reasons for stopping a Cross-Servicing referral and when these reasons should be used:

> DMC Eligible: VA has internal offset available through the VA Debt Management Center.

> High risk veteran: Veteran account is flagged for potential of self-harm.  Veteran case is under review for financial assistance.

> Bankruptcy: Veteran has included VA in court accepted bankruptcy petition for debt relief and proof of bankruptcy filing is available in court records.

> Treasury Error: Account has been referred to Treasury in error, or collection of bill with Treasury is not correct.

> Other: Stop the referral in order to research and verify the status of the referrals. (Stop the referral while awaiting bankruptcy paperwork, granting of waiver, WH inquiry, Congressional request, Director request while investigation is going on, bill dispute, etc.).

If Other is selected as the Stop Cross-Servicing Referral Reason, the user is required to enter an Other stop reason comment (free text, alpha numeric, 100 character limit).

Below are the steps for setting the Stop flag on a Cross-Servicing referral:

1.  From the Cross-Servicing Menu, select the option, Stop/Reactivate TCSP Referral .At the Enter Response: prompt, enter D.
102. At the Select AR DEBTOR: prompt, enter the Debtor name to be stopped from being referred to Cross-Servicing.
103. The system displays the Debtor’s name, SSN, and bill information for Active or Open bills (e.g. AR Status and debt amounts).
104. If the Stop Flag is “R” or Null (e.g. debtor is Reactivated or Active), the system displays:

> Are You Sure You Want To Stop Cross-Servicing Referral for this Debtor?

> Enter Yes or No: NO//

105. Type Y or YES and press the \[Enter\] key.
106. At the Enter Required Stop Reason: prompt, the following reasons are available. Enter the reason code and press the \[Enter\] key.

> D DMC Eligible

> H High risk veteran

> B Bankruptcy

> T Treasury Error

> O Other (If Other is entered, you will be prompted

> to enter a comment at the Stop Reason

> Comment prompt.)

107. A Stop Cross-Servicing Referral Complete message will display when the stop is completed.
108. If the Stop Flag is set to “S” (a.k.a. Stop), the system displays the following sample message indicating that this debtor is already ‘stopped’:

> Referral to Cross-Servicing has already been stopped for this debtor

> Stop Cross-Servicing referral effective date: MMM DD,YYYY@hh:mm:ss

> Stop Cross-Servicing referral reason: stop reason

> Cross-Servicing referral stopped by : BBBBB,JJJJJJJJ

> Are You Sure You Want To Reactivate Cross-Servicing Referral for this Debtor?

> Enter Yes or No: NO//

109. Type N or NO and press the Enter key to go back to the main menu.

### Reactivate TCSP Referral for a Debtor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Stop/Reactivate TCSP Referral for a Debtor functionality is also used to reactivate a Cross-Servicing referral for a Debtor that was previously stopped (remove the ‘Stop’ flag) (refer to the steps below for setting the ‘Stop’ flag on a Cross-Servicing referral:

1.  From the Cross-Servicing Menu, select the option, Stop/Reactivate TCSP Referral. At the Enter Response: prompt, enter D.
110. At the Select AR DEBTOR: prompt, enter the Debtor name to be reactivated.
111. The system displays the Debtor’s name, SSN, and bill information for Active or Open bills (e.g. AR Status and debt amounts).
112. If the Stop Flag is set to S (a.k.a. Stop), the system displays the following sample message indicating that this debtor is already stopped:

> Referral to Cross-Servicing has already been stopped for this debtor

> Stop Cross-Servicing referral effective date: MMM DD,YYYY@hh:mm:ss

> Stop Cross-Servicing referral reason: stop reason

> Cross-Servicing referral stopped by : BBBBB,JJJJJJJJ

> Are You Sure You Want To Reactivate Cross-Servicing Referral for this Debtor?

> Enter Yes or No: NO//

113. Type Y or YES and press the Enter key.
114. A message will display when the reactivation is completed.

> Reactivate Cross-Servicing Referral complete

> All eligible bills for this Debtor are now to be Referred to Cross-Servicing

> \*\*\* End of Reactivate Cross-Servicing Referral \*\*\*

## TCSP Flag Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TCSP Flag Control \[RCDP TCSP FLAG CONTROL\] The options included in this menu are used to correct the bill or debtor data attributes (or flags) as needed because of a variance in the bill or debtor data between the VistA system and the Treasury system. Note that this option is only seen by and accessible to those users assigned to <u>RCDP TCSP FLAG.</u>

<span id="_Toc25567358" class="anchor"></span>Figure 32: TCSP Flag Control Menu option

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/009.png)

### Set Cross-Service Flag on Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Set Cross-Service Flag on Bill functionality is used to set a bill as Cross-Serviced in the system and on the Bill Profile screens.

<span id="_Toc25567359" class="anchor"></span>Figure 33: Set Cross-Service Flag on Bill

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/010.png)

### Clear Cross-Service Flag on Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clear Cross-Service Flag on Bill functionality is used to clear a bill from being Cross- Serviced in the system and on the Bill Profile screens.

<span id="_Toc25567360" class="anchor"></span>Figure 34: Clear Cross-Service Flag on Bill

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/011.png)

### Clear Cross-Service Flag on Debtor (and all Bills)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clear Cross-Service Flag on Debtor (and all Bills) functionality is used to clear a Debtor and all of their bills from being Cross-Serviced in the system and on the Bill Profile screens.

<span id="_Toc25567361" class="anchor"></span>Figure 35: Clear Cross-Service Flag on Debtor (and all bills)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/012.png)

### Set Cross-Service Flag on Debtor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Set Cross-Service Flag on Debtor functionality is used to set a Debtor as Cross-Serviced in the system and on the Bill Profile screens.

<span id="_Toc25567362" class="anchor"></span>Figure 36: Set Cross-Service Flag on Debtor

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/013.png)

### Fully Re-establish Debtor/Bill as Cross-Serviced

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fully Re-Establish Debtor/Bill as Cross-Serviced functionality is used to re-set a debtor and his/her bill as Cross-Serviced in the system and on the Bill Profile screens.

<span id="_Toc25567363" class="anchor"></span>Figure 37: Fully Re-establish Debtor/Bill as Cross-Serviced

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/014.png)

## Reconciliation List Manager Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reconciliation List Manager \[RCTCSP RECONCILIATIONWORKLIST\] functionality is used to manage bills that have been returned by Treasury from Cross-Servicing for reconciliation. From the list manager screens, the user is able to view an expanded version of the selected patient’s cross-serviced bill, insurance data, view and manage the patient’s account, print statement, and remove bills from the worklist.

1.  At the Select Type of Report: prompt, enter RECONCILIATION LIST MANAGER or RCTCSP RECONCILIATION WORKLIST.
115. Choose the type of report:

> 1 Bankruptcy

> 2 Deaths

> 3 Uncollectible

> 4 Payment in Full

> 5 Satisfied PA

> 6 Compromise

> 7 All Returns

> Enter a list or range of numbers (1-7):

> This response must be a list or range, e.g., 1,3,5 or 2-4,8.

116. Select one of the following:

> A All Divisions

> S Selected Divisions

> Select(A)ll or (S)elected Division(s) : All//

> Enter 'A' to not filter by Division.

> Enter 'S' to view entries for selected Division(s).

117. Select one of the following:

> 1 List Manager

> 2 Excel Format

> List Manager or Excel Format: 1//

> The default is (1).

> If (2) is entered, the following message displays:

> To capture as an Excel format, it is recommended that you queue this report to a spool device with margins of 256 and page length of 99999 (e.g., spoolname;256;99999). This should help avoid wrapping problems.

> Another method would be to set up your terminal to capture the detail report data. On some terminals, this can be done by invoking 'Logging' or clicking on the 'Tools' menu above, then click on 'Capture Incoming Data' to save to Desktop. To avoid undesired wrapping of the data saved to the file, change the DISPLAY screen width size to 132 and you can enter '0;256;99999' at the 'DEVICE:' prompt.

16. To avoid undesired wrapping of the data saved to the file, enter 0;256;999 at the DEVICE: prompt.

### Reconciliation List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reconciliation List Manager main screen displays the patient’s name, patient ID (last name first initial, last 4 of the SSN), bill number, balance, and return reason code. Note that the “y” indicates each bill has been returned from Treasury.

<span id="_Toc25567364" class="anchor"></span>Figure 38: TCSP Reconciliation Worklist – Main Screen

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/015.png)

<span id="_Toc25567365" class="anchor"></span>Figure 39: TCSP Reconciliation Worklist - Expand Patient

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/016.png)

<span id="_Toc25567366" class="anchor"></span>Figure 40: TCSP Reconciliation Worklist - View Insurance

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/017.png)

<span id="_Toc25567367" class="anchor"></span>Figure 41: TCSP Reconciliation Worklist – View Insurance – View Policy Info

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/018.png)

<span id="_Toc25567368" class="anchor"></span>Figure 42: TCSP Reconciliation Worklist – View Insurance – Annual Benefits

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/019.png)

<span id="_Toc25567369" class="anchor"></span>Figure 43: TCSP Reconciliation Worklist – View Insurance – Benefits Used

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/020.png)

<span id="_Toc25567370" class="anchor"></span>Figure 44: TCSP Reconciliation Worklist – View Insurance – Change Patient

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/021.png)

<span id="_Toc25567371" class="anchor"></span>Figure 45: TCSP Reconciliation Worklist – View Insurance – Expand Benefits

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/022.png)

<span id="_Toc25567372" class="anchor"></span>Figure 46: TCSP Reconciliation Worklist: Patient Inquiry

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/023.png)

<span id="_Toc25567373" class="anchor"></span>Figure 47: TCSP Reconciliation Worklist: Print Statement

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/024.png)

<span id="_Toc25567374" class="anchor"></span>Figure 48: TCSP Reconciliation Worklist: Remove From Worklist

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/025.png)

### TCSP Reconciliation Worklist – Account Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Account Profile screen of the Reconciliation List Manager, the user can perform the following actions on individual or multiple bills for an account: view, stop or delete stop TCSP referral, suspend, re-establish, view transactions, terminate fiscal, select status to view, recall or delete recall flags for a debtor, increase or decrease adjustments or cancel/add/edit bills.

<span id="_Toc25567375" class="anchor"></span>Figure 49: TCSP Reconciliation Worklist – Account Profile

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/026.png)

<span id="_Toc25567376" class="anchor"></span>Figure 50: TCSP Reconciliation Worklist – Account Profile – Bill Profile (Page 1 of 3)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/027.png)

<span id="_Toc25567377" class="anchor"></span>Figure 51: TCSP Reconciliation Worklist – Account Profile – Bill Profile (Page 2 of 3)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/028.png)

<span id="_Toc25567378" class="anchor"></span>Figure 52: TCSP Reconciliation Worklist – Account Profile – Bill Profile (Page 3 of 3)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/029.png)

<span id="_Toc25567379" class="anchor"></span>Figure 53: TCSP Reconciliation Worklist – Account Profile – Stop TCSP (Page 1 of 2)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/030.png)

Figure 54: TCSP Reconciliation Worklist – Account Profile – Stop TCSP (Page 2 of 2)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/031.png)

<span id="_Toc25567380" class="anchor"></span>Figure 55: TCSP Reconciliation Worklist – Account Profile – Delete TCSP Stop

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/032.png)

<span id="_Toc25567381" class="anchor"></span>Figure 56: TCSP Reconciliation Worklist – Account Profile – Suspend Bill

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/033.png)

<span id="_Toc25567382" class="anchor"></span>Figure 57: TCSP Reconciliation Worklist – Account Profile – Re-Establish Bill

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/034.png)

<span id="_Toc25567383" class="anchor"></span>Figure 58: TCSP Reconciliation Worklist – Account Profile – Recall Bill

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/035.png)

<span id="_Toc25567384" class="anchor"></span>Figure 59: TCSP Reconciliation Worklist – Account Profile – Delete Bill Recall

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/036.png)

<span id="_Toc25567385" class="anchor"></span>Figure 60: TCSP Reconciliation Worklist – Account Profile – Term Fiscal (Page 1 of 2)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/037.png)

Figure 61: TCSP Reconciliation Worklist – Account Profile – Term Fiscal (Page 2 of 2)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/038.png)

<span id="_Toc25567386" class="anchor"></span>Figure 62: TCSP Reconciliation Worklist – Account Profile – Select Status

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/039.png)

<span id="_Toc25567387" class="anchor"></span>Figure 63: TCSP Reconciliation Worklist – Account Profile – Recall Debtor

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/040.png)

<span id="_Toc25567388" class="anchor"></span>Figure 64: TCSP Reconciliation Worklist – Account Profile – Increase Adj

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/041.png)

<span id="_Toc25567389" class="anchor"></span>Figure 65: TCSP Reconciliation Worklist – Account Profile – Select New Acct (1 of 2)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/042.png)

Figure 66: TCSP Reconciliation Worklist – Account Profile – Select New Acct (2 of 2)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/043.png)

<span id="_Toc25567390" class="anchor"></span>Figure 67: Account Profile: Cancel/Edit/Add

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/044.png)

<span id="_Toc25567391" class="anchor"></span>Figure 68: Account Profile: Cancel/Edit/Add – Add A Charge

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/045.png)

<span id="_Toc25567392" class="anchor"></span>Figure 69: Account Profile: Cancel/Edit/Add – Cancel A Charge

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/046.png)

<span id="_Toc25567393" class="anchor"></span>Figure 70: Account Profile: Cancel/Edit/Add – Cancel A Charge (cont’d.)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/047.png)

<span id="_Toc25567394" class="anchor"></span>Figure 71: Account Profile: Cancel/Edit/Add – Change Patient

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/048.png)

<span id="_Toc25567395" class="anchor"></span>Figure 72: Account Profile: Cancel/Add/Edit Charges – Change Date Range

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/049.png)

<span id="_Toc25567396" class="anchor"></span>Figure 73: Account Profile: Cancel/Add/Edit Charges – Pass A Charge:

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/050.png)

<span id="_Toc25567397" class="anchor"></span>Figure 74: Account Profile: Cancel/Edit/Add Charges – Update Events

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/051.png)

<span id="_Toc25567398" class="anchor"></span>Figure 75: Account Profile: Decrease Adjustment

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/052.png)

# Cross-Servicing Batch Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRCA Nightly Process is a set of AR routines scheduled to run at the same time every night. These routines update all actions completed through the VistA AR software and initiate all weekly Cross-Servicing messages transmitted to AITC. Cross-Servicing Weekly Messages are transmitted every Tuesday at 1:00 AM ET to AITC and the local VistA mail groups (G.TCSP).

The Cross-Servicing routines that run as part of the PRCA Nightly Process update the following Cross-Servicing actions. These actions are described in more detail in this section.

- [Referral Batch Job](#referral-batch-job): Transmits new debt to Cross-Servicing that meets all of the required criteria.
- [Update Batch Job](#update-batch-job): For those debtors referred to Cross-Servicing, transmits updates to the name (e.g., marriage, etc.), mailing address, phone number, Tax Identification Number (TIN) (Social Security Number \[SSN\]), and date of birth. Additionally, the Update File contains decrease adjustments.
- [Recall Batch Job](#_Recall_Batch_Job): Recalls all debts and debtors that have been flagged in VistA for recall from Cross-Servicing.

<span id="_Toc25567399" class="anchor"></span>Figure 76: Referral, Update & Recall Files Transfer Schedule for Cross-Servicing

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/053.png)

## Referral Batch Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cross-Servicing Referral batch job runs weekly on Tuesday. For a debt to be automatically referred to Cross-Servicing, the following criteria must be true:

- The bill must be delinquent 120 days or more.
- The Debtor Type must be a First Party bill.
- The bill status must be Active.
- The Site Deletion Referral Flag for a debtor must be set to blank or NO in the AR Debtor File (#340).
- The DMC Referral Flag must be removed from the bill. *DATE SENT TO DMC* (File 430,121) must be Null and *DMC Debt Valid* (File 430,125) must be No or Pending.
- An individual bill must be equal to or greater than \$25.00.
- The *Letter3* field is populated with a Collection Follow-up Date.

When the Cross-Servicing Referral batch job runs, VistA generates bulletins (MailMan messages), which lists all of the new debt / debtors referred to Cross-Servicing. The bulletins are described in the following sub-sections.

### Add New Debt Referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For new debt being referred to Cross-Servicing, where a debtor has NOT been previously referred, the “CS Add Referral” bulletin is generated, which includes the Bill Number, SSN (*TIN*) of the debtor, the action code (*TYPE*), “A”, which refers to “Add New Debt” (refer to *Appendix A. Cross-Servicing Record Types & Action Codes*), and the amount of the debt referred to Cross-Servicing (*AMOUNT*) (Figure 77). Cross-Servicing referred text will also display on the various AR profile and bill screens (refer to *Section 3 Cross-Servicing Fields & Messages*). The new debt and debtor are included in the Referral File.

<span id="_Ref398281290" class="anchor"></span>Figure 77: Bulletin: ‘CS Add Referral’ (New Cross-Servicing Referral Debt)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/054.png)

For all newly referred debt, where a debtor has NOT been previously referred, additional transmission messages will also be generated, along with the CS ADD REFERRAL bulletin. Using Bill \# 631-K001CDK from the above figure, the following figures represent example transmission messages that are also generated.

<span id="_Toc25567401" class="anchor"></span>Figure 78: Record Type 1 – Action Code A – Add New Debt

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/055.png)

<span id="_Toc25567402" class="anchor"></span>Figure 79: Record Type 2 – Action Code A – Add New Debtor

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/056.png)

<span id="_Toc25567403" class="anchor"></span>Figure 80: Record Type 2A – Action Code A – Add New Individual Debtor

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/057.png)

<span id="_Toc25567404" class="anchor"></span>Figure 81: Record Type 2C – Action Code A – Add New Debtor Contact Information

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/058.png)

<span id="_Toc25567405" class="anchor"></span>Figure 82: Record Type 3 – Action Code A – Add Case Information

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/059.png)

### New Debt for Existing Debtor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For new debt being referred, or returned or recalled debt that is being re-referred, to Cross-Servicing, where a debtor has been previously referred to Cross-Servicing, VistA generates the “CS Add Referral” bulletin, as in Figure 77, and a “CS Existing Debtor” bulletin (Figure 83), which includes the Bill Number, SSN (*TIN*) of the debtor, and the action code (*TYPE*), “B” (for Add New Debt to Existing Debtor) (refer to *Appendix A. Cross-Servicing Record Types & Action Codes*).

<span id="_Ref409684828" class="anchor"></span>Figure 83: Bulletin: 'CS Existing Debtor' (New Debt for Existing Debtor)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/060.png)

The bill will be marked as referred or re-referred to Cross-Servicing in the various account profile screens (refer to *Section 3 Cross-Servicing Fields & Messages*). The new debt is included in the Referral File.

Using Bill \#442-K601WD2 from Figure 83, Figure 84 illustrates the IAI record types, action codes, and data that are transmitted to Treasury when new debt is added to a previously referred debtor. This transmission message is generated by VistA, along with the ‘CS Add Referral’ and ‘CS Existing Debtor’ bulletins.

<span id="_Ref409685113" class="anchor"></span>Figure 84: Transmission Message: Add Debt to Existing Debtor

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/061.png)

## Update Batch Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Update batch job is scheduled to run weekly on Tuesday after the Referral batch job, transmitting updates to the debtor’s patient file and decrease adjustments on the debtor’s account.

### Updates to Debtor’s Patient File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA automatically identifies updates to the debtor’s name, SSN (TIN), address, date of birth, and gender since the last weekly run, and includes those updates in the Update File.

Depending on what data is updated, the transmitted record type could be 2, 2A, or 2C, with an Action Code of “U”. The debtor’s name and SSN is on Record Type 2 (see the figures below). If the change is gender or date of birth, that data is on Record Type 2A, so the update is for 2A. If the change is for address, which is on Record Type 2C, the update is for Record Type 2C, with the additional condition that the Action Code is A. When updates are transmitted, an update bulletin and a transmission message are generated. (*Refer to Appendix A. Cross-Servicing Record Types & Action Codes.*)

<span id="_Ref398283324" class="anchor"></span>Figure 85: Bulletin: ‘CS Updates’ (Updates to Debtor’s Patient File)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/062.png)<span id="_Recall_Batch_Job" class="anchor"></span>

Figure 86: Transmission Message: ‘CS Updates’ (Updates to Debtor’s Patient File)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/063.png)

### Adjustments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additionally, the Update File may include decrease or increase adjustments to the debtor’s account. Once a bill has been referred to Cross-Servicing, VistA will continue to allow the following decrease/increase adjustments:

1.  DMC offsets.
118. Adjustments that occur when one or more charges under a bill number are canceled.
119. Manual decreases or increases for third party payments via the claims-matching process.

Both manual and automatic decrease adjustments, increase adjustments, and administrative cost adjustments will produce individual, IAI, 5B records with the “Trans Type” field name (position 66-74) in the 5B record as follows:

1.  Trans Type = “AIO” (Agency Internal Offset) for automatic decreases via Lockbox.
120. Trans Type = “ABAL” (Agency Balance Adjustment) for manual decreases (via VistA).

A 5B record type will be generated by VistA when the Offset Type begins with “168” (DMC / C&P Originated), when an Overpayment is applied to other Cross-Serviced bills not in Treasury’s Collection File, or a manual decrease adjustment (via VistA AR’s adjustment feature) is applied to a bill (refer to the following figures). If there are any 5B transactions that take the balance of the bill to zero putting the bill into a collected/closed status, then the bill will no longer be flagged as being Cross-Serviced. The 5B record for increase and administrative cost adjustments will be generated when the user confirms that the adjustment is not a Treasury reversal.

As required by the IAI specifications, the 5B records will include the Signed Principal Amount, Signed Interest Amount, Signed Admin Cost Amount, and Signed Penalty Amount (includes the Marshall Fee and Court Costs amounts in VistA). Note that the Signed Principal Amount is the amount by which the transaction amount changes the principal, not the amount of the principal.

<span id="_Toc25567410" class="anchor"></span>Figure 87: Transmission Message: Manual Decrease Adjustment - ABAL

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/064.png)

<span id="_Toc25567411" class="anchor"></span>Figure 88: Bulletin: Manual Decrease Adjustment – ABAL

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/065.png)

<span id="_Toc25567412" class="anchor"></span>Figure 89: Transmission Message: Automatic Decrease Adjustment – AIO

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/066.png)

<span id="_Toc25567413" class="anchor"></span>Figure 90: Bulletin: Automatic Decrease Adjustment – AIO

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/067.png)

## Recall Batch Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Recall batch job is scheduled to run weekly after the Update batch job. This batch job recalls all debt and debtors that have been flagged to be recalled from Cross-Servicing.

### Recall Debt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA generates the “CS Recalls’ bulletin containing the bill number, SSN (*TIN*) and the action code (*TYPE*), “L” for recall (refer to *Appendix A. Cross-Servicing Record Types & Action Codes*) (Figure 91). Along with the bulletin, IAI-formatted transmissions for Record Type 1 will be transmitted. The Record Type 1 transmission includes the bill number and the debt recall reason \# (“01” in Figure 92).

<span id="_Ref398283737" class="anchor"></span>Figure 91: Bulletin: ‘CS Recalls Sent’ (Debt Recall)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/068.png)

<span id="_Ref408490018" class="anchor"></span>Figure 92: Transmission Message: Cross-Servicing Recalls (Debt Recall)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/069.png)

17. When all bills on a debtor’s account are recalled, a Type 2 record will also be transmitted with an Action Code of “L” (Figure 94).

### Recall Debtor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a debtor is recalled, all debt that is currently referred to Cross-Servicing will be recalled. The bulletin in the below figure illustrates the recall of a debtor, who has just one bill referred to Cross-Servicing.

<span id="_Toc25567416" class="anchor"></span>Figure 93: Bulletin: ‘CS Recalls Sent’ (Debtor Recall)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/070.png)

A Record Type 2 with an Action Code of “L” is transmitted for each recalled bill. Using the bill in the above figure (#500-K400009), Figure 94 illustrates the transmission for this particular recalled bill with a Recall Debtor Reason of “3” for “Bankruptcy with Automatic Stay”.

<span id="_Ref408492126" class="anchor"></span>Figure 94: Transmission Message: Cross-Servicing Recalls (Debtor Recall)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/071.png)

# Debts / Debtors Returned by Treasury for Reconciliation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following the referral of a debt to Cross-Servicing, there are various reasons why a debt may be returned by Treasury for reconciliation, including, but not limited to, the following: (1) Compromise Offer, (2) Uncollectable, (3) Administrative Resolution Approved for Bankruptcy, and (4) Administrative Resolution Approved for Death. These returned debts are sent from Treasury to VistA in the form of a Reconciliation File on the first day of every month. A bulletin is generated in MailMan listing those debts returned. The bulletin contains the debtor’s name, bill number, returned date, closed date, and return reason (Figure 95). Another Cross-Servicing option that can be used to manage returned debt by Treasury for reconciliation is the Print Reconciliation Report.

When a debt / debtor is returned by Treasury, VistA automatically places a ‘Stop’ on the debt, with a Stop reason of ‘Other’ and a comment of ‘By Reconciliation’. The effective date of the stop referral is also added to the debt. Additionally, the ‘Debt Referred to Cross-Servicing’ flag is removed from the debt (the “x”). Note that the message “Debt Referred to Cross-Servicing” and “Total CS Debt” will remain on the debtor’s account until <u>all debt</u> on the debtor’s account is no longer referred to Cross-Servicing. Refer to the following table for sample reconciliation scenarios and the action to take in VistA. For all other scenarios, please follow the business rules implemented for debts / debtors returned by Treasury for reconciliation.

<span id="_Toc169093091" class="anchor"></span>Table 6‑1: Reconciliation Scenarios & VistA Actions

| Reconciliation Scenario | VistA Action                                          |
|-----------------------------|-----------------------------------------------------------|
| Compromise Offer            | Cancel Copayment (Waive Debt)                             |
| Uncollectable               | Cancel Copayment (Waive Debt)                             |
| Bankruptcy                  | Cancel Copayment (Suspend Copayment)                      |
| Debtor Deceased             | Termination of Debt when Reclamation Requirements are Met |

<span id="_Toc169093105" class="anchor"></span>Table D‑1: Acronyms

<span id="_Ref400530333" class="anchor"></span>Figure 95: Bulletin: CS Qualified / Returned Debts

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/072.png)

# Due Process Notification Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon implementation of Cross-Servicing, a one-time-only process will generate an Initial Due Process Notification (DPN) File that identifies bills that comply with all of the Cross-Servicing rules, but are less than \$25. On a weekly basis, the Initial DPN File will be checked by VistA for any bills that had been identified previously as less than \$25 and have increased (due to fees and charges) to \$25 or more. VistA will send this file (Figure 96) to AITC on Tuesdays. AITC will process through each record and determine if the record is valid. AITC will then generate a printed DPN letter (

Figure 99), or determine if it is in error and is to be returned to VistA, identifying the two digit IAI error code(s) (see *Section 7.1 Due Process Notification Rejects*).

VistA receives the DPN Letter Printed & Error IAI File from AITC and logs the date the letter was printed or errors found. When AITC successfully prints the letter, AITC will send an IAI-formatted type file back to VistA with the ‘Date Letter Sent from AITC’. VistA displays this information in a MailMan bulletin (Figure 97).

After a 60-day wait period, the debt / bill associated with the DPN process will be processed by VistA according to the standard, Cross-Servicing, referral criteria.

<span id="_Ref408918350" class="anchor"></span>Figure 96: Bulletins: Due Process Notification (DPN)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/073.png)

<span id="_Ref419109215" class="anchor"></span>Figure 97: Bulletin: Due Process Notification Letter Print Date

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/074.png)

## Due Process Notification Rejects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AITC will process through each DPN record and determine if the record(s) are valid and can generate a printed letter or determine if the record is in error and is to be returned to VistA. This reject file identifies the errors with the corresponding error codes (refer to *Appendix B. Cross-Servicing IAI Error Codes*).

18. Error code, “37”, is transmitted back by AITC for any issues with a debtor’s address related to the DPN transmission, including a blank Address Line 1, Address Line 2, City, State, and Foreign Code.

The Unprocessable / Reject File for DPN, transmitted from AITC, will generate the DPN Unprocessable Reject Bulletin (Figure 98) in MailMan notifying end users that there is an error, and that a correction needs to take place in order for the DPN processing data to be sent in a future Cross-Servicing batch run.

<span id="_Ref419107946" class="anchor"></span>Figure 98: Bulletin: Due Process Notification Reject Records

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/075.png)<span id="_Ref419108684" class="anchor"></span>

Figure 99: Sample Due Process Notification Letter

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/076.png)

# Collections: Payment Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a brief overview on the payments and offsets on debt referred to Cross-Servicing. All payments and offsets on Cross-Serviced debt will be transmitted to VistA via AITC’s Lockbox application. No other payments other than those specified below will be allowed for Cross-Serviced bills.

## What is Lockbox?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AITC’s Lockbox application is a centralized, collection point for processing and depositing large volumes of payments and deposits.

For more information on the Lockbox process, refer to *Lockbox Training Guide*.

## No Manual Payments on Cross-Serviced Bills

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a bill is referred to Cross-Servicing, no <u>manual</u> payments can be applied to the bill. If a debtor’s account has bills referred to Cross-Servicing, VistA will apply any manual payments posted to a <u>debtor’s account</u> to the oldest bill that is <u>not</u> Cross-Serviced. Any overpayments on a debtor’s account (where all Non-Cross-Serviced bills are paid off) will NOT be applied to a Cross-Serviced bill and will be placed in a suspense fund. If a user attempts to post a manual payment by Bill Number to a Cross-Serviced bill, the following message will display:

<span id="_Toc25567423" class="anchor"></span>Figure 100: Bill Referred to Cross-Servicing - No Manual Payments Allowed

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/077.png)

## Lockbox Payment Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For payments / DMC offsets transmitted to VistA via Lockbox, the first three numbers of the deposit ticket \# will indicate the type of offset / payment, as indicated in the table below.

<span id="_Toc169093092" class="anchor"></span>Table 8‑1: Offset / Payment Types

<table>
<caption>Offset / Payment Types</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 27%" />
<col style="width: 26%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
&#10;</blockquote></th>
<th><blockquote>
<p><strong>DMC (C&amp;P) Offset</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TOP Payments</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Treasury (Cross-Servicing) Payments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Deposit Ticket Number begins with (1<sup>st</sup> 3 digits)</p>
</blockquote></td>
<td><blockquote>
<p>168</p>
</blockquote></td>
<td><blockquote>
<p>169</p>
</blockquote></td>
<td><blockquote>
<p>170</p>
</blockquote></td>
</tr>
</tbody>
</table>

Offset / Payment Types

### DMC Offset (168)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DMC Agency Internal Offsets occur around the 25th day of each month, although it varies a few days from month-to-month. When VistA receives an offset from DMC, it <u>applies the payment to the oldest bill in VistA first, no matter if it is a TOP or Cross-Serviced bill</u>. If the oldest bill is a bill that has been referred to Cross-Servicing, then an IAI record type 5B (Financial Adjustment) is created and sent to Treasury (refer to *Section 5.2.2 Adjustments*).

DMC does not store and will not transmit a Bill Number in the 168 Collections File, as C&P offset is at the account level, not the bill level. The following is the format of the file received by VistA. The file contains the: SSN of debtor, payment amount, deposit number, date of deposit, and a payment type of “2”.

<span id="_Toc25567424" class="anchor"></span>Figure 101: Lockbox Payment Transmission Content - DMC Collections File (168)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/078.png)

Using the example above, for the deposit number of “16822631”, a search on this deposit using the Deposit Processing screen from the Agent Cashiers Menu, will display a screen that looks like the below figure. The *Deposit Date* will match the deposit date in the Collections File of “12222014”. The *Payment Type* will be *Administrative Offset*, with total number of records listed under *Count*. For example, the seven records in the above figure, matches the total count on the Deposit Processing screen. If you add the dollar amounts in each of the seven records above, this amount is in the *Total Paid* column.

<span id="_Toc25567425" class="anchor"></span>Figure 102: Deposit Processing (168)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/079.png)

A search on the Receipt \# (using “A14122200” in the above figure), displays a Receipt Profile screen listing the seven records and the payment amount from each record in the Collections File (Figure 103).

<span id="_Ref408484913" class="anchor"></span>Figure 103: Receipt Profile (168)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/080.png)

Using Transaction \#1 in the above figure, the Transaction Profile screen will display the Transaction Date (*TransDate*) and Transaction Amount (*Trans Amt*) from the Collections File, as well as the Receipt Number. If only partial payment is received, the *Type* will read “PAYMENT (IN PART)”. If full payment is received, the *Type* will read “PAYMENT (IN FULL)”.

<span id="_Toc25567427" class="anchor"></span>Figure 104: Transaction Profile (168)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/081.png)

### TOP Payments (169)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For debt referred to TOP, the automatic payment process has not changed with the implementation of Cross-Servicing. DMC will continue to send the payments to AITC via the Lockbox Collections File, which triggers an update in VistA. VistA then sends an Update File to AITC where the files are bundled and transmitted to Treasury.

For payments received via a TOP (169) Collections File, payments will be applied to the <u>oldest bill on those debts previously referred to TOP</u>. The “Payment Type” description will be “TOP Payment”. A TOP payment will NOT be applied to a bill that has been referred to Cross-Servicing.

<span id="_Toc25567428" class="anchor"></span>Figure 105: Lockbox Payment Transmission Content – TOP Collections File (169)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/082.png)

<span id="_Toc25567429" class="anchor"></span>Figure 106: Deposit Processing Screen (169)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/083.png)

<span id="_Toc25567430" class="anchor"></span>Figure 107: Receipt Profile Screen (169)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/084.png)

### Treasury Payments (170)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For debt referred to Cross-Servicing, VistA will receive automatic payments from Treasury via Lockbox. Every Monday, Treasury transmits a Collections File to DMC containing payments on all Cross-Serviced debt. Following receipt of the file, DMC converts the file to a Lockbox format before transmitting to AITC. AITC then transmits the file to VistA where payments are applied automatically by Bill Number (Figure 108). Note that VistA will not generate a 5B record when a payment originates from Treasury (170) unless there is money left over from the payment which can be applied to other Cross Serviced bills. Take note that a 170 offset payment that is applied to the Cross-Serviced bill for which it was explicitly meant to be applied, if the bill is paid off taking the balance to zero and applying a collected/closed status to the bill, then the bill will no longer be flagged as being Cross-Serviced. Notifications will be transmitted via MailMan when the Treasury Collections File is received by VistA (Figure 109).

19. VistA will apply any overpayments on a Cross-Serviced bill to other Cross-Serviced bills (where applicable) on a debtor’s account, starting with the oldest, Cross-Serviced bill first. Any remaining balance will first be applied to other bills, starting with the oldest, then, if there are still monies left over, this amount will be placed in suspense, to be reviewed by the Accounting staff to determine whether those funds will be refunded to the debtor or applied to additional Cross-Serviced bills. Funds will be distributed within 60 days of receipt; however, the Veteran may request the refund sooner

<span id="_Ref409686083" class="anchor"></span>Figure 108: Lockbox Payment Transmission Content – Treasury Collections File (170)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/085.png)

The following figures illustrate the various components of payment processing using the example 170 Collections File in Figure 108. When the 170 Collections File is processed by VistA, a bulletin is generated indicating that the payment processing is complete, with the Deposit \# from the original collections file (i.e., 17002631) and a VistA-generated Receipt \# (i.e., P14120300). Also, the total amount of all payments received is included (Figure 109).

<span id="_Ref409687892" class="anchor"></span>Figure 109: Bulletin: Auto Payment Processing Completed (170)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/086.png)

On the Deposit Processing screen, the *Payment Type* will be “Private Collection Agency” (Figure 110), showing the number of payments under *Count* and the total dollar amount under *Total Paid*.

<span id="_Ref409688437" class="anchor"></span>Figure 110: Deposit Processing Screen (170)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/087.png)

Referring back to Figure 108, the highlighted payment of \$507.07 for the debtor (TCSISTINE, TSTEY NHIEKP) is reflected on the Receipt Profile screen with the same *Receipt \#*, *Deposit \#*, and *Type of Payment*.

<span id="_Toc25567434" class="anchor"></span>Figure 111: Receipt Profile Screen (170)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/088.png)

Finally, on the Transaction Profile screen, using the same Bill \# and payment highlighted in Figure 108 (631-K101BSG for a payment of \$507.07), the following figure illustrates that the payment was applied (In Full) to the Cross-Serviced Bill from the 170 Collections File.

<span id="_Toc25567435" class="anchor"></span>Figure 112: Transaction Profile Screen (170)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/089.png)

## Other Blocked Options on Cross-Serviced Bills

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options described in this sub-section are now blocked on all bills referred to Cross-Servicing. Note that once a bill is referred to Cross-Servicing, VHA can no longer service the debt.

### Set Up Repayment Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all bills referred to Cross-Servicing, the Set Up Repayment Plan\[PRCAC SET REPAYMENT\] option cannot be performed. A repayment plan must be set up by Treasury and not implemented by VHA in VistA. The following message will display if a user attempts to set up a repayment plan on a Cross-Serviced bill.

<span id="_Toc25567436" class="anchor"></span>Figure 113: Repayment Plan Option Blocked on Cross-Serviced Bills

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/090.png)

### Administrative Cost Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Administrative Cost Adjustment\[PRCAF ADJ ADMIN\] option is blocked on all bills referred to Cross-Servicing. The following message will display if a user performs this option on a Cross-Serviced bill.

<span id="_Toc25567437" class="anchor"></span>Figure 114: Administrative Cost Adjustment Option Blocked on Cross-Serviced Bills

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/091.png)

### Fiscal Officer Terminated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before a user can perform the Fiscal Offer Terminated \[PRCAC TR TERM-FISCAL\] option on a Cross-Serviced bill, the bill must be first recalled from Cross-Servicing. Use the Recall/Reactivate TCSP Referral for a Bill option on the Cross-Servicing Menu to recall the bill from Treasury.

The following message will display if a user attempts this option on a Cross-Serviced bill:

<span id="_Ref421010114" class="anchor"></span>Figure 115: Fiscal Officer Terminated Option Blocked on Cross-Serviced Bills

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/092.png)

### Compromise Termination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As with the above option, the bill must be recalled from Cross-Servicing before performing the Compromise Termination \[PRCAC TR TERM-COMPROMISE\] option on a Cross-Serviced bill. The same message will display as in Figure 115.

### Suspend an AR Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all bills referred to Cross-Servicing, the Suspend an AR Bill\[PRCAC TR SUSPENDED\] option cannot be performed until the bill is recalled from Cross-Servicing. A message will display indicating that the recall process must utilized prior to suspending the bill.

### Partial /Full Waiver

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Partial Waiver \[PRCAC WAIVED PART\] and Full Waiver\[PRCAC WAIVED FULL\] options will also be blocked on Cross-Serviced bills until the bill is recalled from Cross-Servicing.

# Cross-Servicing Rejects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a debt has been rejected by Cross-Servicing, the debt will no longer be considered referred to Cross-Servicing. Reject messages can come from Treasury, DMC or AITC. These messages / files are sent to the VAMC via MailMan on a weekly basis (where applicable).

If a bill that has been referred by Cross-Servicing is rejected by any source, a bulletin (MailMan message) will display in the user’s MailMan inbox. A ‘Stop’ flag is automatically set on the bill with a reason of “Rejected by Cross-Servicing”. Additionally, the Reject Code, Reason, and Date will display on the profile screens (see *Section 3.3 Debt Rejected by Cross-Servicing*). The “x” indicator is removed from the bill on the Full Account Profile screen.

VistA prevents the re-referral of any rejected bills until the ‘Stop’ flag is removed. For all bills rejected, the technician is required to research and correct the error(s), and then remove the ‘Stop’ flag from the bill, where applicable (see *Section 0*). When correcting an error, follow the business rules implemented for Cross-Servicing. The Cross-Servicing functionality provides the following two options for manually working these rejects, which are found on the main Cross-Servicing Menu:

- Debt Referral Reject Report (refer to *Section 4.1.5*)
- List IAI Error Codes (refer to *Appendix B. Cross-Servicing IAI Error Codes*).

Once the error is corrected and the ‘Stop’ flag is removed, the account will follow the appropriate processing sequence. Depending on the status of the account, this may include referral to Cross-Servicing with the next weekly transmission. Note that the reject information will remain on the profile screen even after the error has been corrected.

## Recall Debtor Rejects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a reject on debtor recalls using the *Recall TCSP Referral for a Debtor* option, note that a stop is placed on the first Cross-Serviced bill available for that debtor. After the error(s) is corrected, the stop will need to be removed from the debt in order for the recall debtor retransmission to occur. Utilize the *Debt Referral Reject Report* to locate the Bill No. on the rejected debtor recall (Type=“2”; Action Code=“L”) where the ‘Stop’ needs to be removed for a sample report of a reject on a debtor recall).

<span id="_Toc25567439" class="anchor"></span>Figure 116: Sample Debt Referral Reject Report (Rejects on a Debtor Recall)

PAGE 1 DEBT REFERRAL REJECT REPORT (SORTED BY BILL NO. \<ASC\>) 06/03/24

---------------------------------------------------------------------------------------

BILL NO. AR CAT DEBTOR Pt ID TYP ACTNCD REJECT DATE SRC ERR CODES

----------- ---------- ------------------- ----- --- ------ ----------- --- ---------

442-K604KH5 RX CO-PAYM DEBTOR,ONE L XXXX 2 L 02/13/18 T 7C

## Reject Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users must belong to the G.TCSP mail group to receive reject messages. The subject of the CS Reject message will identify the source of the reject. The body of the reject bulletin will include the Debtor’s name (*NAME*), SSN, Bill Number, Record Type (*TYPE*), Action Code (*ACTN*), and all of the Error Codes associated with the referral (Figure 117 and Figure 118).

20. For additional information on Error Codes, refer to *Appendix B. Cross-Servicing IAI Error Codes*. For information on Cross-Servicing Record Types and Action Codes, reference *Appendix A. Cross-Servicing Record Types & Action Codes*.

## ZZ Error Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ‘ZZ’ Error Code has been introduced as a ‘catch-all’ for errors that do not match up to the list of errors already defined by Treasury. A ‘ZZ’ error code does not indicate what the error is, meaning it will require manual intervention to review the record in VistA in order to locate and correct the error. The definition of Error Code ‘ZZ’ is “Manual Intervention Required”.

<span id="_Ref403122622" class="anchor"></span>Figure 117: Bulletin: Cross-Servicing Rejects (AITC)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/093.png)<span id="_Ref409598185" class="anchor"></span>

Figure 118: Bulletin: Cross-Servicing Rejects (Treasury)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/094.png)

# Additional VistA Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the mail group used for Cross-Servicing, the file transfer schedule for Cross-Servicing, and the Cross-Servicing fields (with file names) stored in VistA.

## Cross-Servicing Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is one mail group specifically for receiving Cross-Servicing messages – G.TCSP. This mail group must have members who are active VistA users.

The G.TCSP mail group will also receive notifications when the batch run is completed and when a corrupted debtor record is found during the batch run. This functionality was created with Accounts Receivable patch, PRCA\*4.5\*327.

Below are illustrations of how the Failed Debtor Action & Batch Completion notifications.

<span id="_Toc25567442" class="anchor"></span>Figure 119: Failed Debtor Action Notice & Batch Completion Notice

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/095.png)

The Failed Debtor Action notice will be sent when a corrupt debtor record has been found during the batch run.

<span id="_Toc25567443" class="anchor"></span>Figure 120: Failed Debtor Action Notice

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/096.png)

The Batch Completion notice will be sent once the batch run and transmission has been completed.

<span id="_Toc25567444" class="anchor"></span>Figure 121: Batch Completion Notice

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/097.png)

## Cross-Servicing File Transfer Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 122 illustrates the high-level, file transfer schedule between VHA, AITC, DMC, and Treasury for Cross-Servicing. The following files are referenced: Referral, Update, Recall, Collections, Due Process Notification, and Unprocessable.

<span id="_Ref408903923" class="anchor"></span>Figure 122: Cross-Servicing File Transfer Schedule

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/098.png)

## Cross-Servicing Files & Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cross-Servicing information is stored in the VistA files listed in this section. The following tables list the number, name, and description of each Cross-Servicing field.

<span id="_Ref393715017" class="anchor"></span>Table 10‑1: Cross-Servicing Fields in AR Debtor File (#340)

| Field Number | Field Name               | Description                                                                     |
|------------------|------------------------------|-------------------------------------------------------------------------------------|
| 7.02             | TCSP RECALL FLAG             | Flag set when debts or debtor recalled from Cross-Servicing.                        |
| 7.03             | TCSP RECALL DATE             | Date the debtor is recalled from Cross-Servicing.                                   |
| 7.04             | TCSP RECALL REASON           | Reason for recalling the debtor.                                                    |
| 7.05             | DATE DEBTOR REFERRED TO TCSP | Date the debtor is recalled from Cross-Servicing.                                   |
| 8                | TCSP REFERRAL STOP FLAG      | Multiple leading to subfile 340.08 containing stop/reactivate flags for this debtor |
| 340.08,.01       | TCSP REFERRAL STOP FLAG      | S for Stop or R for Reactivate for this debtor                                      |
| 340.08,.02       | TCSP REFERRAL DATE           | Date when this stop/reactivate flag was set                                         |
| 340.08,.03       | USER MAKING CHANGE           | User who performed this stop or reactivate                                          |
| 340.08,.04       | TCSP REFERRAL STOP REASON    | Reason why stop was placed                                                          |
| 340.08,.05       | TCSP REFERRAL STOP COMMENT   | If reason is O (OTHER), free text explanation of what it is for                     |

Cross Servicing Fields in AR Debtor File (#340)

<span id="_Toc169093094" class="anchor"></span>Table 10‑2: Cross-Servicing Fields in AR Site Parameter File (#342)

| Field Number | Field Name             | Description                                                                                                          |
|------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 100              | CROSS-SERVICING START DATE | Used to automatically calculate when the DPN processing and weekly transmissions of the DPN file to AITC will be halted. |
| 40               | TCSP REFERRAL STOP FLAG    | Multiple leading to subfile 342.02 containing stop/reactivate flags for site                                             |
| 342.02,.01       | TCSP REFERRAL STOP FLAG    | S for Stop or R for Reactivate                                                                                           |
| 342.02,.02       | TCSP REFERRAL STOP DATE    | Date when site was stopped or reactivated                                                                                |
| 342.02,.03       | USER MAKING CHANGE         | User who stopped or reactivated site                                                                                     |
| 342.02,.04       | TCSP REFERRAL COMMENT      | Comment on why stop or reactivate was done (field currently inactive)                                                    |

Cross Servicing Fields in AR Debtor File (#340)

<span id="_Toc169093095" class="anchor"></span>Table 10‑3: Cross-Servicing Fields in TCS IAI Error Codes File (#348.5)

| Field Number | Field Name    | Description                               |
|------------------|-------------------|-----------------------------------------------|
| 0.01             | ERROR CODE ID     | Error code ID in the IAI error code file.     |
| 1                | FIELD NAME/ACTION | Field name/action in the IAI error code file. |
| 2                | RECORD TYPE       | Record type in the IAI error code file.       |
| 3                | ERROR MESSAGE     | Error message in the IAI error code file.     |

Cross Servicing Fields in TCS IAI Error Codes File (#348.5)

<span id="_Toc169093096" class="anchor"></span>Table 10‑4: Cross-Servicing Fields in TCS IAI Action Code File (#348.6)

| Field Number | Field Name     | Description                                             |
|------------------|--------------------|-------------------------------------------------------------|
| 0.01             | ACTION CODE        | Action code in the IAI action code file.                    |
| 1                | ACTION DESCRIPTION | Description of the action code in the IAI action code file. |
| 2                | RECORD TYPE        | Record type in the IAI action code file.                    |

Cross Servicing Fields in TCS IAI Action Code File (#348.6)

<span id="_Toc169093097" class="anchor"></span>Table 10‑5: Cross-Servicing Fields in TCS IAI Record Types File (#348.7)

| Field Number | Field Name          | Description                                         |
|------------------|-------------------------|---------------------------------------------------------|
| 0.01             | RECORD TYPE ID          | Record Type ID of the IAI Record Type in transmission.  |
| 1                | RECORD TYPE DESCRIPTION | Description of the Record Type in the IAI transmission. |
| 2                | DATA TYPE               | Type of data in the IAI transmission.                   |

Cross Servicing Fields in TCS IAI Record Types File (#348.7)

<span id="_Toc169093098" class="anchor"></span>Table 10‑6: Cross-Servicing Fields in Accounts Receivable File (#430)

| Field Number | Field Name                          | Description                                                                                                                                                                                                              |
|------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 151              | DATE BILL REFERRED TO TCSP              | Date the bill was first referred to Cross-Servicing.                                                                                                                                                                         |
| 152              | TCSP RECALL FLAG                        | Set whenever a ‘Recall CS Referral” is entered by the user through the Recall menu options.                                                                                                                                  |
| 153              | TCSP RECALL EFF. DATE                   | Contains a date, for which bills generated after, are eligible for Cross-Servicing referral.                                                                                                                                 |
| 154              | TCSP RECALL REASON                      | Contains a code detailing the reason the referral to Cross-Servicing was recalled.                                                                                                                                           |
| 155              | RECALL AMOUNT                           | The dollar amount of the debt recalled from Cross-Servicing.                                                                                                                                                                 |
| 156              | ORIGINAL DATE REFERRED TO TCSP          | The original date that the debt was referred to Cross-Servicing. This field is set only once. It is not deleted or reset with subsequent actions on the debt. This field should not be used for aging or other computations. |
| 157              | STOP TCSP REFERRAL FLAG                 | Set whenever a 'Stop CS Referral' is entered by the user through the menu option.                                                                                                                                            |
| 158              | STOP TCSP REFERRAL EFF. DATE            | Contains a date, for which bills generated after, are eligible for Cross-Servicing referral.                                                                                                                                 |
| 159              | STOP TCSP REFERRAL REASON               | Contains a code detailing the reason the referral to Cross-Servicing was stopped.                                                                                                                                            |
| 159.1            | STOP TCSP REFERRAL COMMENT              | Comment field used to support the reason that a stop flag has been set for a debt. A comment is required in the case of 'Other' as a reason code.                                                                            |
| 159.2            | TCSP CASE RECALL FLAG                   | Flag that marks this case for recall record creation from Cross-Servicing when the AR nightly background job is run.                                                                                                         |
| 159.3            | TCSP CASE RECALL EFF DATE               | Date that the recall flag is set for a case.                                                                                                                                                                                 |
| 159.4            | TCSP CASE RECALL REASON                 | Reason that the case is being recalled from Cross-Servicing.                                                                                                                                                                 |
| 159.5            | TCSP GENDER                             | Gender of debtor referred to Cross-Servicing                                                                                                                                                                                 |
| 159.9            | TCSP RE-REFERRAL                        | Re-Referral requests and performs                                                                                                                                                                                            |
| 161              | ORIGINAL TCSP TIN                       | SSN sent to Cross-Servicing on the original referral document.                                                                                                                                                               |
| 162              | ORIGINAL TCSP DEBTOR NAME               | Name as sent on the original Cross-Servicing referral document.                                                                                                                                                              |
| 163              | TCSP DELINQUENCY DATE                   | Date that the bill became active. The debt is referred to Cross-Servicing when the debt is 150 days old counted from the delinquency date.                                                                                   |
| 164              | TCSP DEBTOR ADDRESS, LINE 1             | First line of the current debtor address transmitted to Cross-Servicing.                                                                                                                                                     |
| 165              | TCSP DEBTOR ADDRESS, LINE 2             | Second line of the current debtor address transmitted to Cross-Servicing.                                                                                                                                                    |
| 166              | TCSP DEBTOR ADDRESS, CITY               | City included in the debtor address transmitted to Cross-Servicing.                                                                                                                                                          |
| 167              | TCSP DEBTOR ADDRESS, STATE              | State included in the debtor address transmitted to Cross-Servicing.                                                                                                                                                         |
| 168              | TCSP DEBTOR ZIP CODE                    | Zip code included in the debtor address transmitted to Cross-Servicing.                                                                                                                                                      |
| 169              | ORIGINAL TCSP AMOUNT                    | Original amount referred to Cross-Servicing.                                                                                                                                                                                 |
| 169.1            | CURRENT TCSP AMOUNT                     | Current debt amount at Cross-Servicing.                                                                                                                                                                                      |
| 169.2            | TCSP DEBTOR PHONE                       | Residence phone number from the Patient file (#2).                                                                                                                                                                           |
| 169.3            | TCSP COUNTRY CODE                       | The country code from the Patient file (#2).                                                                                                                                                                                 |
| 169.4            | TCSP DOB                                | The patient date of birth.                                                                                                                                                                                                   |
| 171              | CS ADJ TRANS NUMBER (multiple 430.0171) | Transaction number in the AR Transaction file (#433) for transactions to be included in a 5B record to be sent to Cross-Servicing.                                                                                           |
| 430.0171, .01    | CS ADJ TRANS NUMBER                     | Transaction number in the AR Transaction file (#433) for transactions to be included in a 5B record to be sent to Cross-Servicing.                                                                                           |
| 430.0171, 1      | SEND TCSP RECORD 5B                     | Flag that marks this transaction to be sent to Cross-Servicing in a 5B record when the AR nightly background job is run.                                                                                                     |
| 173              | DUE PROCESS NOTIFICATION FLAG           | Date that a bill is flagged for Due Process Notification (DPN)                                                                                                                                                               |
| 174              | DUE PROCESS REQUEST DATE                | Date that the due process request is set                                                                                                                                                                                     |
| 175              | DUE PROCESS LETTER PRINT DATE           | Print date of the due process letter.                                                                                                                                                                                        |
| 176              | DUE PROCESS REFERRAL DATE               | Date that the bill is referred for due processing.                                                                                                                                                                           |
| 177              | DUE PROCESS ERROR DATE                  | Date that the bill is rejected for due process.                                                                                                                                                                              |
| 178              | DUE PROCESS ERROR CODES                 | Error codes related to the bill being rejected for due process.                                                                                                                                                              |
| 191              | SEND TCSP RECORD 1                      | Flag set by the unprocessable file to request that a record 1 be sent for this debt.                                                                                                                                         |
| 192              | SEND TCSP RECORD 2                      | Flag set by the unprocessable file to request that a record 2 be sent for this debt.                                                                                                                                         |
| 193              | SEND TCSP RECORD 2A                     | Flag set by the unprocessable file to request that a record 2A be sent for this debt.                                                                                                                                        |
| 194              | SEND TCSP RECORD 2C                     | Flag set by the unprocessable file to request that a record 2C be sent for this debt.                                                                                                                                        |
| 199.2            | STOP INTEREST ADMIN CALC                | Flag to stop interest and admin calculation for debts referred to Cross-Servicing.                                                                                                                                           |
| 301              | RETURNED DATE                           | Returned date field on the reconciliation file for records returned by Treasury from Cross-Servicing.                                                                                                                        |
| 302              | RETURN REASON CODE                      | Returned reason code field on the reconciliation file for records returned by Treasury from Cross-Servicing.                                                                                                                 |
| 303              | COMPROMISED INDICATOR                   | Compromise indicator field on the reconciliation file for records returned by Treasury from Cross-Servicing.                                                                                                                 |
| 304              | COMPROMISE AMOUNT                       | Compromise amount field on the reconciliation file for records returned by Treasury from Cross-Servicing.                                                                                                                    |
| 305              | CLOSED DATE                             | Closed date field on the reconciliation file for records returned by Treasury from Cross-Servicing.                                                                                                                          |
| 306              | BANKRUPTCY DATE                         | Bankruptcy date field on the reconciliation file for records returned by Treasury from Cross-Servicing.                                                                                                                      |
| 307              | DATE OF DEATH                           | Date of death field on the reconciliation file for records returned by Treasury from Cross-Servicing.                                                                                                                        |
| 308              | DATE OF DISSOLUTION                     | Date of dissolution field on the reconciliation file for records returned by Treasury from Cross-Servicing.                                                                                                                  |
| 309              | REMOVED FROM RECONCILIATION?            | This field determines whether or not the bill will display on the Cross-Servicing Reconciliation Worklist. Users have the ability to manually remove debtors/bills from the worklist and this field is used in that action.  |
| 310              | REC ORIGINAL TCSP AMOUNT                | This is the original amount referred to Cross-Servicing. It is saved and stored separately from field 169 (see above) for reporting purposes.                                                                                |
| 311              | REC CURRENT TCSP AMOUNT                 | This is the current debt amount at Cross-Servicing. It is saved and stored separately from field 169.1 (see above) for reporting purposes.                                                                                   |
| 312              | REC TCSP RECALL EFF. DATE               | This is the date that the recall flag is set for the debt. It is saved and stored separately from field 153 (see above) for reporting purposes.                                                                              |
| 313              | TCSP AGENCY DEBT ID LAST 2              | This is last 2 characters to be used in formatting Agency Debt ID field in IAI file for re-referrals                                                                                                                         |

Cross Servicing Fields in Accounts Receivable File (#430)

<span id="_Toc169093099" class="anchor"></span>Table 10‑7: Cross-Servicing Fields in Subfile CS Decrease Adj Trans Number  
(sub file of AR \#430) (#430.0171)

| Field Number | Field Name               | Description                                                |
|------------------|------------------------------|----------------------------------------------------------------|
| .01              | CS DECREASE ADJ TRANS NUMBER | Transaction number for the Cross-Servicing decrease adjustment |

Cross Servicing Fields in TCS IAI Record Types File (#348.7)

<span id="_Toc169093100" class="anchor"></span>Table 10‑8: Cross-Servicing Fields in Reject Date (sub-file of AR \#430) (#430.0172)

| Field Number | Field Name     | Description                                            |
|------------------|--------------------|------------------------------------------------------------|
| .01              | REJECT DATE        | Date that a Cross-Servicing referral / update was rejected |
| 1                | REJECT SOURCE      | Source of the reject (AITC, DMC, Treasury)                 |
| 2                | REJECT REASON1     | Reject Reason 1                                            |
| 3                | REJECT REASON2     | Reject Reason 2                                            |
| 4                | REJECT REASON3     | Reject Reason 3                                            |
| 5                | REJECT REASON4     | Reject Reason 4                                            |
| 6                | REJECT REASON5     | Reject Reason 5                                            |
| 7                | REJECT REASON6     | Reject Reason 6                                            |
| 8                | REJECT REASON7     | Reject Reason 7                                            |
| 9                | REJECT REASON8     | Reject Reason 8                                            |
| 10               | REJECT REASON9     | Reject Reason 9                                            |
| 11               | RECORD TYPE        | Record type of the reject                                  |
| 12               | RECORD ACTION CODE | Action code of reject                                      |
| 13               | REJECT BATCH ID    | Batch ID \# of the reject                                  |
| 14               | REJECT MM MSG NO.  | MailMan Message \# of the reject                           |

Cross Servicing Fields in Reject Date (sub-file of AR \#430) (#430.0172)

<span id="_Toc169093101" class="anchor"></span>Table 10‑9: Cross-Servicing Fields in TCSP RE-REFFERALS (sub file of AR \#430) (#430.03)

| Field Number | Field Name           | Description                                                                                                           |
|------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------|
| .01              | TCSP RE-REFERRAL         | 0=Re-Referral Requested, 1=Re-Referred                                                                                    |
| .02              | TCSP RE-REFERRAL DATE    | Date when re-referral was requested or performed                                                                          |
| .03              | TCSP RE-REFERRAL USER    | User requesting Re-Referral. When re-referral is performed, same user as made the request will be in the performed record |
| .04              | TCSP RE-REFERRAL REASON  | R=Recall In Error, T=Treasury Reversal, D=Defaulted RPP, O=Other                                                          |
| .05              | TCSP RE-REFERRAL COMMENT | If reason is O=Other, then comment explaining the reason.                                                                 |

Cross Servicing Fields in AR Return Reason Code File (#430.5)

<span id="_Toc169093102" class="anchor"></span>Table 10‑10: Cross-Servicing Fields in AR Return Reason Code File (#430.5)

| Field Number | Field Name | Description                             |
|------------------|----------------|---------------------------------------------|
| .01              | CODE           | Code \# in the return reason code file.     |
| .1               | DESCRIPTION    | Description in the return reason code file. |
| 2                | CATEGORY       | Category in the return reason code file.    |

Cross Servicing Fields in AR Return Reason Code File (#430.5)

# Appendix A. Cross-Servicing Record Types & Action Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the record types and action codes used for Cross-Servicing from Treasury’s IAI File Format specification (refer to *Appendix F. References*).

| Record Type                                               | Action Code | Description                       |
|---------------------------------------------------------------|-----------------|---------------------------------------|
| H – Header Record                                         | \-              | \-                                    |
| 1 – Debt Record                                           | A               | Add New Debt                          |
|                                                               | U               | Update Debt                           |
|                                                               | L               | Debt Recall                           |
|                                                               |                 |                                       |
| 2 – Debtor Record                                         | A               | Add new Debtor                        |
|                                                               | U               | Update Debtor, Update Debtor TIN      |
|                                                               | L               | Debtor Recall                         |
|                                                               | B               | Add New Debt to Existing Debtor       |
|                                                               |                 |                                       |
| 2A – Individual Debtor Record                             | A               | Add New Individual Debtor             |
|                                                               | U               | Update Individual Debtor              |
|                                                               |                 |                                       |
| 2C – Debtor Contact Information                           | A               | Add new Debtor Contact Info           |
|                                                               |                 |                                       |
| 3 – Case Record                                           | A               | Add Case Info                         |
|                                                               |                 |                                       |
| 5B - Creditor Agency Financial Transactions (Adjustments) | U               | CA Financial Transaction (Adjustment) |
|                                                               |                 |                                       |
| Z – Trailer Record                                        | \-              | \-                                    |

Cross-Servicing Record Types & Action CodesCross-Servicing Record Types & Action Codes

# Appendix B. Cross-Servicing IAI Error Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The below table is a list of the IAI error codes for Cross-Servicing. For all errors that cannot be fixed locally, please log a Remedy ticket.

<table>
<caption>Cross-Servicing IAI Error CodesCross-Servicing IAI Error Codes</caption>
<colgroup>
<col style="width: 4%" />
<col style="width: 25%" />
<col style="width: 19%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Field Name / Action</strong></th>
<th><strong>Record Type(s)</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01</td>
<td>FAST Code/ ALC/ Station</td>
<td>1,2,2A,2B,2C,2D,2E,3,4,5A,5B,6</td>
<td>Cannot be blank or is invalid.</td>
</tr>
<tr class="even">
<td>02</td>
<td>ALC</td>
<td>1,2,2A,2B,2C,2D,2E,3,4,5A,5B,6</td>
<td>ALC of input record does not Match file ALC.</td>
</tr>
<tr class="odd">
<td>03</td>
<td>DMS Processing Code</td>
<td>1,2,2A,2B,2C,2D,2E,3,4,5A,5B,6</td>
<td>DMS Processing Code cannot be blank or is invalid.</td>
</tr>
<tr class="even">
<td>04</td>
<td>Agency Debt ID</td>
<td>1,2,2A,2B,2C,2D,2E,3,4,5A,5B,6</td>
<td>Invalid agency debt id or agency debt id not specified.</td>
</tr>
<tr class="odd">
<td>05</td>
<td>Debt Type</td>
<td>1</td>
<td>Debt Type does not exist in Agency Profile or invalid Debt Type code.</td>
</tr>
<tr class="even">
<td>06</td>
<td>Debt Type</td>
<td>1</td>
<td>Cannot reset debt type.</td>
</tr>
<tr class="odd">
<td>07</td>
<td>Debtor TIN</td>
<td>2, 2C,4,6</td>
<td>Invalid TIN number or TIN not specified.</td>
</tr>
<tr class="even">
<td>08</td>
<td>Debtor TIN</td>
<td>1,2, 2A, 2B, 2C, 2D, 2E, 3, 4, 5A, 5B, 6</td>
<td>Cannot reset TIN, change TIN, or TIN does not match existing debt number.</td>
</tr>
<tr class="odd">
<td>09</td>
<td>Debtor TIN</td>
<td>2</td>
<td>Invalid TIN for a RT 2 Action Code Add record.</td>
</tr>
<tr class="even">
<td>10</td>
<td>Debtor TIN</td>
<td>2</td>
<td>Debtor already in debtor table.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>Debtor TIN</td>
<td>2</td>
<td>This is a Joint &amp; Several debt.</td>
</tr>
<tr class="even">
<td>12</td>
<td>Debtor TIN</td>
<td>2</td>
<td>If Debtor TIN is provided, a valid TIN Type must be Entered.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>Debtor TIN</td>
<td>2, 2C, 4, 6</td>
<td>Debtor TIN must be Numeric.</td>
</tr>
<tr class="even">
<td>14</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>Delinquent amount not numeric or amount &lt; $25 limit.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>For adjust action, amount cannot be zero.</td>
</tr>
<tr class="even">
<td>16</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>Cannot decrease a debt with existing current balance of zero.</td>
</tr>
<tr class="odd">
<td>17</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>For refund record, there is no offset payment found for the offset year / date, or year / date is invalid.</td>
</tr>
<tr class="even">
<td>18</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>Refund record amount in excess of offset.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>For refund reversal record, there is no offset payment found for the offset year / date, or year / date is invalid.</td>
</tr>
<tr class="even">
<td>20</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>Amount of refund reversal record exceeds amount of previous refund.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>Referred Debt Balance must be Equal to the Sum of Initial Principal, Initial Interest, Initial Admin Costs, and Initial Penalty.</td>
</tr>
<tr class="even">
<td>22</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>Referred Debt Balance must be Numeric.</td>
</tr>
<tr class="odd">
<td>23</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>Referred Debt Balance is Required.</td>
</tr>
<tr class="even">
<td>24</td>
<td>Debt Judgment</td>
<td>2</td>
<td>Invalid Judgment Debt value.</td>
</tr>
<tr class="odd">
<td>25</td>
<td>Delinquency Date</td>
<td>1</td>
<td>Invalid date for Delinquent Date, not numeric or not specified.</td>
</tr>
<tr class="even">
<td>26</td>
<td>Delinquency Date</td>
<td>1</td>
<td>Cannot reset Delinquent Date.</td>
</tr>
<tr class="odd">
<td>27</td>
<td>Delinquency Date</td>
<td>1</td>
<td>Delinquent date cannot be &gt; (later than) processing date.</td>
</tr>
<tr class="even">
<td>28</td>
<td>Delinquency Date</td>
<td>1</td>
<td>Date error (incorrect format) when adding or updating debt record.</td>
</tr>
<tr class="odd">
<td>29</td>
<td>Delinquency Date</td>
<td>1</td>
<td>Date error when updating Debt record.</td>
</tr>
<tr class="even">
<td>30</td>
<td>Delinquency Date</td>
<td>1</td>
<td>Date Delinquency Began is more than 10 years prior to current date</td>
</tr>
<tr class="odd">
<td>31</td>
<td>Individual or Business</td>
<td>2</td>
<td>Invalid Individual/Business Indicator or not specified.</td>
</tr>
<tr class="even">
<td>32</td>
<td>Individual or Business</td>
<td>2</td>
<td>Cannot reset Business/individual indicator.</td>
</tr>
<tr class="odd">
<td>33</td>
<td>Debtor Name Last or Business</td>
<td>2</td>
<td>Debtor Last Name/Business cannot be blank.</td>
</tr>
<tr class="even">
<td>35</td>
<td>Debtor Name Last or Business</td>
<td>2</td>
<td>Only present when changing last name.</td>
</tr>
<tr class="odd">
<td>36</td>
<td><p>Debtor Name Last or Business</p>
<p>Debtor Name First</p>
<p>Debtor Name Middle</p></td>
<td>2</td>
<td>The debtor is not in Debtor table.</td>
</tr>
<tr class="even">
<td>37</td>
<td>Contact Address 1</td>
<td>2C</td>
<td>Contact address line 1 cannot be blank.</td>
</tr>
<tr class="odd">
<td>38</td>
<td>Contact Address 1</td>
<td>2C</td>
<td>Cannot reset Contact address line 1.</td>
</tr>
<tr class="even">
<td>39</td>
<td>Contact City</td>
<td>2C</td>
<td>Contact city cannot be blank.</td>
</tr>
<tr class="odd">
<td>40</td>
<td>Contact City</td>
<td>2C</td>
<td>Cannot reset Contact city.</td>
</tr>
<tr class="even">
<td>41</td>
<td>Contact Country Name, Contact State</td>
<td>2C</td>
<td>Invalid contact state code or cannot be blank unless country code field is completed and not ‘US’.</td>
</tr>
<tr class="odd">
<td>42</td>
<td>Contact Country Name, Contact State</td>
<td>2C</td>
<td>If Country Code is xx (completed and not ‘US’ on debt record or this update record), State Code must be blank.</td>
</tr>
<tr class="even">
<td>43</td>
<td>Contact State</td>
<td>2C</td>
<td>Contact state code can only be reset when country code field is completed.</td>
</tr>
<tr class="odd">
<td>44</td>
<td>Contact Country Name</td>
<td>2C</td>
<td>Invalid Contact Country Code or code is not valid since state code is completed on debt record or this update record and country code is not ‘US’.</td>
</tr>
<tr class="even">
<td>45</td>
<td>Contact Country Name</td>
<td>2C</td>
<td>Invalid Contact Country Code or code is not valid since state code is completed and country code is not ‘US’.</td>
</tr>
<tr class="odd">
<td>46</td>
<td>Contact Country Name</td>
<td>2C</td>
<td>If Contact Country Code is xx (completed and not ‘US’), Alias State Code must be blank.</td>
</tr>
<tr class="even">
<td>47</td>
<td>Contact Zip Code</td>
<td>2C</td>
<td>The first 5 characters of zip code must be numeric if ‘US’ address or cannot be blank. If country code field is completed and not ‘US’ and state code field is blank, the first five characters must be completed or zeros.</td>
</tr>
<tr class="odd">
<td>48</td>
<td>Contact Zip Code</td>
<td>2C</td>
<td>Cannot reset contact Zip Code unless country code field is completed and not ‘US’.</td>
</tr>
<tr class="even">
<td>49</td>
<td>Debt Origination Date</td>
<td>1</td>
<td>Invalid date for Date Debt Originally Opened, not numeric or not specified.</td>
</tr>
<tr class="odd">
<td>50</td>
<td>Debt Origination Date</td>
<td>1</td>
<td>Date error (incorrect format) when adding or updating date Debt Originally Opened information.</td>
</tr>
<tr class="even">
<td>57</td>
<td>Debtor Alias Last or Business Name</td>
<td>4</td>
<td>Alias Last name cannot be blank.</td>
</tr>
<tr class="odd">
<td>58</td>
<td>Debtor Alias Last or Business Name</td>
<td>4</td>
<td>Cannot reset Alias last name.</td>
</tr>
<tr class="even">
<td>59</td>
<td>Record Type, Action Code</td>
<td>1,2,2A,2B,2C,2D, 2E,3,4,5A, 5B,6</td>
<td>Invalid record type/record action.</td>
</tr>
<tr class="odd">
<td>60</td>
<td>Record Type</td>
<td></td>
<td>Invalid record type for Add Action.</td>
</tr>
<tr class="even">
<td>61</td>
<td>Record Type</td>
<td></td>
<td>Invalid record type for Update Action.</td>
</tr>
<tr class="odd">
<td>62</td>
<td>Record Type</td>
<td>2, 2A,2B,2C,2D,2E,3,4</td>
<td>Invalid record type for Delete Action.</td>
</tr>
<tr class="even">
<td>63</td>
<td>Record Type</td>
<td>2,2A,2B,2C,2D,2E,3,4,6</td>
<td>Invalid record type for Adjust Action.</td>
</tr>
<tr class="odd">
<td>64</td>
<td>Entire Record Type 1</td>
<td>1</td>
<td>Duplicate Debt record found in database for ‘Add’.</td>
</tr>
<tr class="even">
<td>65</td>
<td>Entire Record Type 1</td>
<td>1</td>
<td>General error occurred when adding or updating debt record. Base debt record not found</td>
</tr>
<tr class="odd">
<td>66</td>
<td>Entire Record Type 2</td>
<td>2</td>
<td>Debt record not found for adding debtor information.</td>
</tr>
<tr class="even">
<td>67</td>
<td>Entire Record Type 4</td>
<td>4</td>
<td>Duplicate Debt Alias found in database for ‘Add’.</td>
</tr>
<tr class="odd">
<td>68</td>
<td>Entire Record Type 4</td>
<td>4</td>
<td>General error occurred when adding or updating debt record. Base debt record not found.</td>
</tr>
<tr class="even">
<td>69</td>
<td>Entire Record Types 1,2,2A,2B,2C,2D,2E,3,4,5A,5B,6</td>
<td>1,2,2A,2B,2C,2D,2E,3,4,5A,5B,6</td>
<td>Debt record not found in database for update. Missing contact data for debtor</td>
</tr>
<tr class="odd">
<td>70</td>
<td>Entire Record Type 4</td>
<td>4</td>
<td>Debt Alias record not found in database for update.</td>
</tr>
<tr class="even">
<td>76</td>
<td>Original Amt of Debt</td>
<td>1</td>
<td>Original Amount not numeric or amount &lt; $25 limit or not specified.</td>
</tr>
<tr class="odd">
<td>85</td>
<td>Debtor Name Middle</td>
<td>2</td>
<td>Middle initial not allowed for business debts.</td>
</tr>
<tr class="even">
<td>88</td>
<td>Bypass Indicators</td>
<td>6</td>
<td>Bypass code is invalid or does not exist.</td>
</tr>
<tr class="odd">
<td>89</td>
<td>Bypass Indicators</td>
<td>6</td>
<td>Bypass code already in place for this debt.</td>
</tr>
<tr class="even">
<td>90</td>
<td>Bypass Indicators</td>
<td>6</td>
<td>Bypass code not found for this debt.</td>
</tr>
<tr class="odd">
<td>91</td>
<td>Bypass Indicators</td>
<td>6</td>
<td>Bypass code indicator is full, cannot add another bypass.</td>
</tr>
<tr class="even">
<td>92</td>
<td>Bypass Indicators</td>
<td>6</td>
<td>Default debt load bypass indicator exceed limit of 10.</td>
</tr>
<tr class="odd">
<td>93</td>
<td>Bypass Indicators</td>
<td>6</td>
<td>Similar or duplicate Bypass Indicator already exists for this debt.</td>
</tr>
<tr class="even">
<td>1I</td>
<td>Individual/Joint Several Indicator</td>
<td>1</td>
<td>Individual/Joint Several status indicator is invalid.</td>
</tr>
<tr class="odd">
<td>1J</td>
<td>Individual/Joint Several Indicator</td>
<td>1</td>
<td>Cannot reset to a regular debt.</td>
</tr>
<tr class="even">
<td>1K</td>
<td>Individual/Joint Several Indicator</td>
<td>1</td>
<td>This is the last debtor for this debt.</td>
</tr>
<tr class="odd">
<td>1L</td>
<td>Individual/Joint Several Indicator</td>
<td>1</td>
<td>Cannot add Debtor to non-active Joint &amp; Several Debt.</td>
</tr>
<tr class="even">
<td>1M</td>
<td>Individual/Joint Several Indicator</td>
<td>1</td>
<td>Individual/Joint Several Ind is Required.</td>
</tr>
<tr class="odd">
<td>1N</td>
<td>Admin Debt Class</td>
<td>1</td>
<td>Admin Debt Class is Required if Debt Type = “A”.</td>
</tr>
<tr class="even">
<td>1O</td>
<td>Admin Debt Class</td>
<td>1</td>
<td>Admin Debt Class must be Null if Debt Type = “L”.</td>
</tr>
<tr class="odd">
<td>1P</td>
<td>Admin Debt Class</td>
<td>1</td>
<td>Invalid Admin Debt Classification Code.</td>
</tr>
<tr class="even">
<td>1Q</td>
<td>Consumer or Commercial</td>
<td>1</td>
<td>Invalid Consumer/Commercial Code.</td>
</tr>
<tr class="odd">
<td>1R</td>
<td>Consumer or Commercial</td>
<td>1</td>
<td>Consumer/Commercial is Required.</td>
</tr>
<tr class="even">
<td>1S</td>
<td>Initial Principal</td>
<td>1</td>
<td>Initial Principal must be Numeric.</td>
</tr>
<tr class="odd">
<td>1T</td>
<td>Initial Interest</td>
<td>1</td>
<td>Initial Interest must be Numeric.</td>
</tr>
<tr class="even">
<td>1U</td>
<td>Initial Admin Costs</td>
<td>1</td>
<td>Initial Admin Costs must be Numeric.</td>
</tr>
<tr class="odd">
<td>1V</td>
<td>Initial Penalty</td>
<td>1</td>
<td>Initial Penalty must be Numeric.</td>
</tr>
<tr class="even">
<td>1W</td>
<td><p>Initial Principal</p>
<p>Initial Interest</p>
<p>Initial Admin Costs</p>
<p>Initial Penalty</p></td>
<td>1</td>
<td>One of these Referred Balance Components is Required.</td>
</tr>
<tr class="odd">
<td>1X</td>
<td>Initial Interest Type</td>
<td>1</td>
<td>Interest code is not allowed when agency program indicates FedDebt will not accrue interest</td>
</tr>
<tr class="even">
<td>1Y</td>
<td>Interest Rate</td>
<td>1</td>
<td>Interest Rate is required if Initial Int Type = “A” / “F”.</td>
</tr>
<tr class="odd">
<td>1Z</td>
<td>Interest Rate</td>
<td>1</td>
<td>Interest rate is not allowed when agency program indicates FedDebt will not accrue interest</td>
</tr>
<tr class="even">
<td>2A</td>
<td>Interest Rate</td>
<td>1</td>
<td>Interest Rate must be Null if Initial Int Type = “C”.</td>
</tr>
<tr class="odd">
<td>2B</td>
<td>Interest Rate</td>
<td>1</td>
<td>Interest Rate must be Between 0.00 And 100.00.</td>
</tr>
<tr class="even">
<td>2C</td>
<td>Interest Rate</td>
<td>1</td>
<td>Interest Rate must be Numeric.</td>
</tr>
<tr class="odd">
<td>2D</td>
<td>Penalty Rate</td>
<td>1</td>
<td>Penalty Rate is Required if Penalty is Accrued.</td>
</tr>
<tr class="even">
<td>2E</td>
<td>Penalty Rate</td>
<td>1</td>
<td>Penalty Rate must be Null if Penalty is not Accrued.</td>
</tr>
<tr class="odd">
<td>2F</td>
<td>Penalty Rate</td>
<td>1</td>
<td>Penalty Rate must be Between 0.00 And 100.00</td>
</tr>
<tr class="even">
<td>2G</td>
<td>Penalty Rate</td>
<td>1</td>
<td>Penalty Rate must be Numeric.</td>
</tr>
<tr class="odd">
<td>2H</td>
<td>Last Interest Calc Date</td>
<td>1</td>
<td>Date is Required if Interest Rate is Entered or profile indicates required</td>
</tr>
<tr class="even">
<td>2I</td>
<td>Last Interest Calc Date</td>
<td>1</td>
<td>Last Interest Calc Date must be Null if Interest Rate is Not Entered.</td>
</tr>
<tr class="odd">
<td>2J</td>
<td>Last Interest Calc Date</td>
<td>1</td>
<td>Last Interest Calc Date must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="even">
<td>2K</td>
<td>Last Interest Calc Date</td>
<td>1</td>
<td>Last Interest Calc Date must be less than or equal to the System Date.</td>
</tr>
<tr class="odd">
<td>2L</td>
<td>Last Penalty Calc Date</td>
<td>1</td>
<td>Date is Required if Pen Rate is Entered or profile indicates required</td>
</tr>
<tr class="even">
<td>2M</td>
<td>Last Penalty Calc Date</td>
<td>1</td>
<td>Last Penalty Calc Date must be Null if Penalty Rate is Not Entered.</td>
</tr>
<tr class="odd">
<td>2N</td>
<td>Last Penalty Calc Date</td>
<td>1</td>
<td>Last Penalty Calc Date must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="even">
<td>2O</td>
<td>Last Penalty Calc Date</td>
<td>1</td>
<td>Last Penalty Calc Date must be less than or equal to the System Date.</td>
</tr>
<tr class="odd">
<td>2P</td>
<td>Last PMT Amt Prior to Ref</td>
<td>1</td>
<td>Last PMT Amt Prior to Ref must be Numeric.</td>
</tr>
<tr class="even">
<td>2Q</td>
<td>Last PMT Date Prior to Ref</td>
<td>1</td>
<td>Last PMT Date Prior to Ref must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="odd">
<td>2R</td>
<td>Last PMT Date Prior to Ref</td>
<td>1</td>
<td>Last PMT Date Prior to Ref must be less than or equal to the System Date.</td>
</tr>
<tr class="even">
<td>2T</td>
<td>SOL Expiration Date</td>
<td>1</td>
<td>SOL Expiration Date must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="odd">
<td>2U</td>
<td>Guarantor Exists</td>
<td>1</td>
<td>Invalid ‘Guarantor Exists’ Code.</td>
</tr>
<tr class="even">
<td>2V</td>
<td>Foreclosure Indicator</td>
<td>1</td>
<td>Invalid Foreclosure Indicator Code.</td>
</tr>
<tr class="odd">
<td>2X</td>
<td>Written Off</td>
<td>1</td>
<td>Invalid Written Off Code.</td>
</tr>
<tr class="even">
<td>2Y</td>
<td>Debtor TIN Type</td>
<td>2</td>
<td>If Debtor TIN Type is provided, a valid TIN must be Entered.</td>
</tr>
<tr class="odd">
<td>2Z</td>
<td>Debtor TIN Type</td>
<td>2</td>
<td>Invalid Debtor TIN Type Code.</td>
</tr>
<tr class="even">
<td>3A</td>
<td>Debtor Generation</td>
<td>2A</td>
<td>Invalid Debtor Generation Code.</td>
</tr>
<tr class="odd">
<td>3B</td>
<td>Debtor Gender</td>
<td>2A</td>
<td>Invalid Debtor Gender Code.</td>
</tr>
<tr class="even">
<td>3C</td>
<td>Date of Birth</td>
<td>2A</td>
<td>Date of Birth must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="odd">
<td>3D</td>
<td>Date of Birth</td>
<td>2A</td>
<td>Date of Birth must be less than the System Date.</td>
</tr>
<tr class="even">
<td>3E</td>
<td>Agency Debtor ID</td>
<td>2,2A, 2B, 2C, 2D,2E,3, 4, 5A,5B, 6</td>
<td>Agency Debtor ID is Required.</td>
</tr>
<tr class="odd">
<td>3F</td>
<td>Judgment Date</td>
<td>1</td>
<td>Judgment Date must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="even">
<td>3G</td>
<td>Relationship to Primary</td>
<td>3</td>
<td>Invalid Relationship to Primary Code.</td>
</tr>
<tr class="odd">
<td>3H</td>
<td>Relationship to Primary</td>
<td>3</td>
<td>Relationship to Primary is Required.</td>
</tr>
<tr class="even">
<td>3I</td>
<td>Contact Type to Rcv DL</td>
<td>3</td>
<td>Invalid Contact Type to Receive Demand Letter Code.</td>
</tr>
<tr class="odd">
<td>3J</td>
<td>Contact Type to Rcv DL</td>
<td>3</td>
<td>Contact Type to Receive Demand Letter is Required.</td>
</tr>
<tr class="even">
<td>3K</td>
<td>Contact Type</td>
<td>2C</td>
<td>Invalid Contact Type Code.</td>
</tr>
<tr class="odd">
<td>3L</td>
<td>Contact Type</td>
<td>2C</td>
<td>Contact Type is missing - see Error Code 3K.</td>
</tr>
<tr class="even">
<td>3M</td>
<td>Contact Free Form Name</td>
<td>2C</td>
<td>Contact Free Form Name cannot be blank.</td>
</tr>
<tr class="odd">
<td>3N</td>
<td>Contact Title</td>
<td>2C</td>
<td>Invalid Contact Title</td>
</tr>
<tr class="even">
<td>3O</td>
<td>Contact Primary Name</td>
<td>2C</td>
<td>Contact Primary Name cannot be blank</td>
</tr>
<tr class="odd">
<td>3P</td>
<td>Contact Phone Type</td>
<td>2C</td>
<td>Invalid Contact Phone Type Code.</td>
</tr>
<tr class="even">
<td>3Q</td>
<td>Contact Phone</td>
<td>2C</td>
<td>Contact Phone must be Numeric.</td>
</tr>
<tr class="odd">
<td>3R</td>
<td>Contact Phone Ext</td>
<td>2C</td>
<td>Contact Phone Ext must be Numeric.</td>
</tr>
<tr class="even">
<td>3S</td>
<td>Contact Primary Phone</td>
<td>2C</td>
<td>Invalid Contact Primary Phone Code.</td>
</tr>
<tr class="odd">
<td>3T</td>
<td>Contact Primary Address</td>
<td>2C</td>
<td>Invalid Contact Primary Address code</td>
</tr>
<tr class="even">
<td>3U</td>
<td>Contact Email Address</td>
<td>2C</td>
<td>Invalid Contact Email Address</td>
</tr>
<tr class="odd">
<td>3V</td>
<td>Contact Primary Email Address</td>
<td>2C</td>
<td>Invalid Contact Primary Email Code.</td>
</tr>
<tr class="even">
<td>3W</td>
<td>Salary</td>
<td>2E</td>
<td>Salary must be Numeric.</td>
</tr>
<tr class="odd">
<td>3X</td>
<td>Salary Cycle</td>
<td>2E</td>
<td>Invalid Salary Cycle Code.</td>
</tr>
<tr class="even">
<td>3Y</td>
<td>Salary Gross or Net</td>
<td>2E</td>
<td>Invalid Salary Gross or Net Code.</td>
</tr>
<tr class="odd">
<td>3Z</td>
<td>Fed Civilian Employee</td>
<td>2A</td>
<td>Invalid Fed Civilian Employee Code.</td>
</tr>
<tr class="even">
<td>4A</td>
<td>Fed Military Employee</td>
<td>2A</td>
<td>Invalid Fed Military Employee Code.</td>
</tr>
<tr class="odd">
<td>4B</td>
<td>Last Debtor Contact Date</td>
<td>3</td>
<td>Last Debtor Contact Date must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="even">
<td>4C</td>
<td>Last Debtor Contact Date</td>
<td>3</td>
<td>Last Debtor Contact Date must be less than or equal to the System Date.</td>
</tr>
<tr class="odd">
<td>4G</td>
<td>Business Debtor Type</td>
<td>2B</td>
<td>Invalid Business Debtor Type Code.</td>
</tr>
<tr class="even">
<td>4H</td>
<td>Business Type</td>
<td>2B</td>
<td>Invalid Business Type Code.</td>
</tr>
<tr class="odd">
<td>4I</td>
<td>Date of Incorporation</td>
<td>2B</td>
<td>Date of Incorporation must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="even">
<td>4J</td>
<td>State of Incorporation</td>
<td>2B</td>
<td>Invalid State of Incorporation Code.</td>
</tr>
<tr class="odd">
<td>4K</td>
<td>Federal Contractor Indicator</td>
<td>2B</td>
<td>Invalid Federal Contractor Indicator Code.</td>
</tr>
<tr class="even">
<td>4L</td>
<td>Date of Dissolution</td>
<td>2B</td>
<td>Date of Dissolution must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="odd">
<td>4M</td>
<td>Property Type</td>
<td>2D</td>
<td>Invalid Property Type Code.</td>
</tr>
<tr class="even">
<td>4N</td>
<td>Date Reported to CB</td>
<td>3</td>
<td>Date Reported to CB must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="odd">
<td>4O</td>
<td>Debtor Alias Type</td>
<td>4</td>
<td>Invalid Debtor Alias Type Code.</td>
</tr>
<tr class="even">
<td>4P</td>
<td>Debtor Alias First Name</td>
<td>4</td>
<td>Debtor Alias First Name cannot be blank.</td>
</tr>
<tr class="odd">
<td>4Q</td>
<td>Debtor Alias Generation</td>
<td>4</td>
<td>Invalid Debtor Alias Generation Code.</td>
</tr>
<tr class="even">
<td>4R</td>
<td>Financial Transaction Type</td>
<td>5A,5B</td>
<td>Invalid Financial Transaction Type Code.</td>
</tr>
<tr class="odd">
<td>4S</td>
<td>Financial Transaction Type</td>
<td>5A,5B</td>
<td>Financial Transaction Type is Required.</td>
</tr>
<tr class="even">
<td>4T</td>
<td>Trans Type</td>
<td>5A,5B</td>
<td>Invalid Trans Type Code.</td>
</tr>
<tr class="odd">
<td>4U</td>
<td>Trans Type</td>
<td>5A,5B</td>
<td>Trans Type is Required.</td>
</tr>
<tr class="even">
<td>4V</td>
<td>Identification Date</td>
<td>5A,5B</td>
<td>Identification Date must be a Valid Date in YYYYMMDD Format.</td>
</tr>
<tr class="odd">
<td>4W</td>
<td>Identification Date</td>
<td>5A,5B</td>
<td>Identification Date must be less than or equal to the System Date.</td>
</tr>
<tr class="even">
<td>4X</td>
<td>Identification Date</td>
<td>5A,5B</td>
<td>Identification Date is Required.</td>
</tr>
<tr class="odd">
<td>4Y</td>
<td>Agency Trans ID</td>
<td>5A,5B</td>
<td>Agency Trans ID is Required.</td>
</tr>
<tr class="even">
<td>5A</td>
<td>Agency Trans ID</td>
<td>5A,5B</td>
<td>Agency Trans ID must be Unique; Agency Trans ID already exists within FedDebt.</td>
</tr>
<tr class="odd">
<td>5B</td>
<td>Trans Amount</td>
<td>5A,5B</td>
<td>Trans Amount must be greater than Zero.</td>
</tr>
<tr class="even">
<td>5C</td>
<td>Trans Amount</td>
<td>5A,5B</td>
<td>Trans Amount must be Numeric.</td>
</tr>
<tr class="odd">
<td>5D</td>
<td>Trans Amount</td>
<td>5A,5B</td>
<td>Trans Amount is Required.</td>
</tr>
<tr class="even">
<td>5E</td>
<td>SIGNED Principal Amount</td>
<td>5B</td>
<td>If Financial Type Code = L, the value of the adjustment cannot reduce the Principal Amount below zero.</td>
</tr>
<tr class="odd">
<td>5F</td>
<td>SIGNED Penalty Amount</td>
<td>5B</td>
<td>If Financial Type Code = L, the value of the adjustment cannot reduce the Penalty Amount below zero.</td>
</tr>
<tr class="even">
<td>5G</td>
<td><p>SIGNED Principal Amount</p>
<p>SIGNED Interest Amount</p>
<p>SIGNED Admin Cost Amount</p>
<p>SIGNED Penalty Amount</p></td>
<td>5B</td>
<td>If Financial Type Code = L, one of these debt balance components is required.</td>
</tr>
<tr class="odd">
<td>5H</td>
<td>Financial Instrument Type</td>
<td>5A</td>
<td>Invalid Financial Instrument Type Code.</td>
</tr>
<tr class="even">
<td>5I</td>
<td>Financial Instrument Type</td>
<td>5A</td>
<td>Financial Instrument Type is Required.</td>
</tr>
<tr class="odd">
<td>5J</td>
<td>Financial Instrument Num</td>
<td>5A</td>
<td>Financial Instrument Num is Required.</td>
</tr>
<tr class="even">
<td>5K</td>
<td>SIGNED Interest Amount</td>
<td>5B</td>
<td>If Financial Type Code = L, the value of the adjustment cannot reduce the Interest Amount below zero.</td>
</tr>
<tr class="odd">
<td>5N</td>
<td>Credit Card Authorization Number</td>
<td>5A</td>
<td>Credit Card Authorization Number is Required if Financial Instrument Type Code = C.</td>
</tr>
<tr class="even">
<td>5O</td>
<td>Credit Card Authorization Number</td>
<td>5A</td>
<td>Credit Card Authorization Number must be Null if Financial Instrument Type Code &lt;&gt; C.</td>
</tr>
<tr class="odd">
<td>5P</td>
<td>SIGNED Admin Cost Amount</td>
<td>5B</td>
<td>If Financial Type Code = L, the value of the adjustment cannot reduce the Admin Cost Amount below zero.</td>
</tr>
<tr class="even">
<td>5Q</td>
<td>Agency Debt ID and Agency Debtor ID</td>
<td>5A</td>
<td>Payment or Reversal is Unidentified</td>
</tr>
<tr class="odd">
<td>5R</td>
<td>Agency Debt ID</td>
<td>5B</td>
<td>Cannot increase adjustment in PA</td>
</tr>
<tr class="even">
<td>5S</td>
<td>Agency Debt ID</td>
<td>5B</td>
<td>Cannot process an adjustment for a closed case</td>
</tr>
<tr class="odd">
<td>5T</td>
<td>Recall Request Reason for Debt</td>
<td>1</td>
<td>Invalid Recall Request Reason for Debt Code.</td>
</tr>
<tr class="even">
<td>5U</td>
<td>Recall Request Reason for Debtor</td>
<td>2</td>
<td>Invalid Recall Request Reason for Debtor Code.</td>
</tr>
<tr class="odd">
<td>5V</td>
<td>Recall Request Reason for Case</td>
<td>3</td>
<td>Invalid Recall Request Reason for Case Code.</td>
</tr>
<tr class="even">
<td>5W</td>
<td>Trans Sequence Number</td>
<td>5A,5B</td>
<td>Transaction’s Sequence Number duplicates another transaction’s number in the same file.</td>
</tr>
<tr class="odd">
<td>5X</td>
<td>Trans Sequence Number</td>
<td>5A,5B</td>
<td>Transaction’s Sequence Number is Required.</td>
</tr>
<tr class="even">
<td>5Y</td>
<td>Judgment/Non Judgment</td>
<td>1</td>
<td>Invalid Judgment Debt value.</td>
</tr>
<tr class="odd">
<td>5Z</td>
<td>Health Insurance Claim</td>
<td>1</td>
<td>Invalid Health Insurance Claim Code</td>
</tr>
<tr class="even">
<td>6A</td>
<td>Debtor Last Name Update Reason</td>
<td>2</td>
<td>Invalid Debtor Last Name Update Reason code</td>
</tr>
<tr class="odd">
<td>6B</td>
<td>DUNS Num</td>
<td>2B</td>
<td>Invalid DUNS Num code</td>
</tr>
<tr class="even">
<td>6C</td>
<td>Employer Name</td>
<td>2E</td>
<td>Employer Name cannot be blank</td>
</tr>
<tr class="odd">
<td>6D</td>
<td>Employer EIN</td>
<td>2E</td>
<td>Employer EIN cannot be blank</td>
</tr>
<tr class="even">
<td>6E</td>
<td>Agency Match Original Trans ID</td>
<td>5A, 5B</td>
<td>Agency Match Original Trans ID does not match Agency Trans ID of the Original Payment</td>
</tr>
<tr class="odd">
<td>6F</td>
<td>SIGNED Trans Amt of Original Payment</td>
<td>5A</td>
<td>Trans Amt of Original Payment does not match corresponding payment</td>
</tr>
<tr class="even">
<td>6G</td>
<td>Transaction Amt of Original Adjustment</td>
<td>5B</td>
<td>Trans Amt of Original Adjustment does not match corresponding adjustment</td>
</tr>
<tr class="odd">
<td>6H</td>
<td>Transaction Amt of Original Offset</td>
<td>5B</td>
<td>Trans Amt of Original Adjustment does not match corresponding TOP offset</td>
</tr>
<tr class="even">
<td>6I</td>
<td>Debtor Name First</td>
<td>2</td>
<td>Debtor First Name cannot be blank for individual debtor.</td>
</tr>
<tr class="odd">
<td>6J</td>
<td>Property Description</td>
<td>2D</td>
<td>Property Description cannot be blank if adding a property.</td>
</tr>
<tr class="even">
<td>6K</td>
<td>Override Action</td>
<td>6</td>
<td>Override Action cannot be blank.</td>
</tr>
<tr class="odd">
<td>6L</td>
<td>Referring a debt</td>
<td>1,2,2C,3</td>
<td>Must include all required record types in order to save debt.</td>
</tr>
<tr class="even">
<td>6M</td>
<td>Referred Debt Balance</td>
<td>1</td>
<td>Debt Balance must be greater or equal to referral threshold</td>
</tr>
<tr class="odd">
<td>6N</td>
<td>Processing a debt</td>
<td>3</td>
<td>Only one case allowed when individual liability</td>
</tr>
<tr class="even">
<td>6O</td>
<td>Processing a debt</td>
<td>2</td>
<td>At least one debtor must be assigned to the debt</td>
</tr>
<tr class="odd">
<td>6P</td>
<td>Processing a debt</td>
<td>3</td>
<td>Debt cannot have more than 26 cases assigned</td>
</tr>
<tr class="even">
<td>6Q</td>
<td>Processing a debt</td>
<td>2</td>
<td>Only one debtor allowed when individual liability</td>
</tr>
<tr class="odd">
<td>6R</td>
<td>Processing a debt</td>
<td>1</td>
<td>At least one case must be assigned to the debt</td>
</tr>
<tr class="even">
<td>6S</td>
<td>FAST Code/ ALC/ Station</td>
<td>1,2,2A,2B,2C,2D,2E,3,4,5A,5B,6</td>
<td>The agency program profile is inactive</td>
</tr>
<tr class="odd">
<td>6T</td>
<td>FAST Code/ ALC/ Station</td>
<td>1,2,2A,2B,2C,2D,2E,3,4,5A,5B,6</td>
<td>The agency program certification has expired</td>
</tr>
<tr class="even">
<td>6U</td>
<td><p>Agency Debt ID</p>
<p>Agency Debtor ID</p></td>
<td>1, 2, 2A, 2B, 2C, 2D, 2E, 3, 4, 5A, 5B, 6</td>
<td>Debt/Debtor Agency Code Conflict</td>
</tr>
<tr class="odd">
<td>6V</td>
<td><p>Agency Debt ID</p>
<p>Agency Debtor ID</p></td>
<td>1, 2, 2A, 2B, 2C, 2D, 2E, 3, 4, 5A, 5B, 6</td>
<td>Debt/Debtor Bureau Code Conflict</td>
</tr>
<tr class="even">
<td>6W</td>
<td>Agency Debt ID</td>
<td>1</td>
<td>Debt already exists</td>
</tr>
<tr class="odd">
<td>6X</td>
<td>Agency Debtor ID</td>
<td>2</td>
<td>Duplicate debtor for this debt</td>
</tr>
<tr class="even">
<td>6Y</td>
<td>Agency Debtor ID</td>
<td>2</td>
<td>New debtors may only be added to JOS debts</td>
</tr>
<tr class="odd">
<td>6Z</td>
<td>Agency Debtor ID</td>
<td>2</td>
<td>A debtor already exists with this key</td>
</tr>
<tr class="even">
<td>7A</td>
<td>Agency Debtor ID</td>
<td>2A</td>
<td>Debtor is not an individual debtor</td>
</tr>
<tr class="odd">
<td>7B</td>
<td>Agency Debtor ID</td>
<td>2B</td>
<td>Debtor is not a business debtor</td>
</tr>
<tr class="even">
<td>7C</td>
<td>Agency Debtor ID</td>
<td>2</td>
<td>Debtor not found for agency debtor Id</td>
</tr>
<tr class="odd">
<td>7D</td>
<td>Individual or Business</td>
<td>2</td>
<td>Consumer debt type may not have business debtors</td>
</tr>
<tr class="even">
<td>7E</td>
<td>Debtor TIN Type</td>
<td>2</td>
<td>Consumer debt may not have debtors with TIN type of EIN</td>
</tr>
<tr class="odd">
<td>7F</td>
<td>Debtor TIN</td>
<td>2</td>
<td>TIN cannot be blank due to debtor in TOP. Mark TIN invalid.</td>
</tr>
<tr class="even">
<td>7G</td>
<td>Individual/Joint Several Indicator</td>
<td>1</td>
<td>New debtors may only be added to JOS debts</td>
</tr>
<tr class="odd">
<td>7H</td>
<td>Relationship to Primary</td>
<td>3</td>
<td>The Relationship to Primary must not be null</td>
</tr>
<tr class="even">
<td>7I</td>
<td>Relationship to Primary</td>
<td>3</td>
<td>There can only be one primary debtor for this debt</td>
</tr>
<tr class="odd">
<td>7J</td>
<td>Relationship to Primary</td>
<td>3</td>
<td>There must be a primary debtor for this debt</td>
</tr>
<tr class="even">
<td>7K</td>
<td>Admin Debt Class</td>
<td>1</td>
<td>Admin Debt Class is not allowed for loan debt type</td>
</tr>
<tr class="odd">
<td>7L</td>
<td>Penalty Rate</td>
<td>1</td>
<td>Penalty rate exceeds system threshold</td>
</tr>
<tr class="even">
<td>7M</td>
<td>Penalty Rate</td>
<td>1</td>
<td>Not allowed when agency program indicates no accrual</td>
</tr>
<tr class="odd">
<td>7N</td>
<td>Contact Type to Rcv DL</td>
<td>3</td>
<td>Primary and Valid address required for contact to receive Demand Letter. When adding new IAI debt the SLFIND/SLFBUS contact primary name indicator must equal “Y”.</td>
</tr>
<tr class="even">
<td>7O</td>
<td>Agency Debtor ID</td>
<td>2, 3, 4</td>
<td>Agency Debtor ID does not match agency records</td>
</tr>
<tr class="odd">
<td>7R</td>
<td>Cannot add debtors to non J&amp;S debt</td>
<td>2</td>
<td>Cannot add debtors to non Joint &amp; Several debt.</td>
</tr>
<tr class="even">
<td>7T</td>
<td>Override already exists</td>
<td>6</td>
<td>Override already exists</td>
</tr>
<tr class="odd">
<td>7U</td>
<td>Update fields cannot be blank</td>
<td>1</td>
<td>Update fields cannot be blank.</td>
</tr>
<tr class="even">
<td>7V</td>
<td>The debt/debtor has no case data</td>
<td>3</td>
<td>Debt/Debtor has no Case Data – Record Type 3 is Required</td>
</tr>
<tr class="odd">
<td>7W</td>
<td>Individual Liability Debt May Only Have One Record Type 3</td>
<td>3</td>
<td>Individual Liability Debt May Only Have One Record Type 3</td>
</tr>
<tr class="even">
<td>7X</td>
<td>Invalid Guarantor Exists</td>
<td>1</td>
<td>Invalid Guarantor Exists</td>
</tr>
<tr class="odd">
<td>7Y</td>
<td>Individual Debt Liability Invalid</td>
<td>3</td>
<td>Individual Debt Liability is invalid.</td>
</tr>
<tr class="even">
<td>7Z</td>
<td>Liability Is Not 100%</td>
<td>3</td>
<td>Liability for debt does not equal 100%</td>
</tr>
<tr class="odd">
<td>8A</td>
<td>Invalid Agency Code – Verify Station Field</td>
<td>1,2,2A,2B,2C,2D,2E,3,4,6</td>
<td>Invalid Agency Code – Verify Station Field</td>
</tr>
<tr class="even">
<td>8B</td>
<td>Invalid Bureau Code – Verify Station Field</td>
<td>1,2,2A,2B,2C,2D,2E,3,4, 6</td>
<td>Invalid Bureau Code – Verify Station Field</td>
</tr>
<tr class="odd">
<td>8C</td>
<td>Invalid Office Code – Verify Station Field</td>
<td>1,2,2A,2B,2C,2D,2E,3,4, 6</td>
<td>Invalid Office Code – Verify Station Field</td>
</tr>
<tr class="even">
<td>8D</td>
<td>Invalid Program Code – Verify Station Field</td>
<td>1, 2, 2A, 2B, 2C, 2D, 2E, 3, 4, 6</td>
<td>Invalid Program Code – Verify Station Field</td>
</tr>
<tr class="odd">
<td>9A</td>
<td>Batch Control ID is Invalid</td>
<td>Header Record</td>
<td>Batch Control ID is invalid</td>
</tr>
<tr class="even">
<td>9B</td>
<td>Invalid Beneficiary Name</td>
<td>1</td>
<td>Beneficiary Name is Invalid</td>
</tr>
<tr class="odd">
<td>9C</td>
<td>Invalid Payment Agreement Terms</td>
<td>1</td>
<td>Payment Agreement Terms is Invalid</td>
</tr>
<tr class="even">
<td>9D</td>
<td>Invalid Job Title</td>
<td>2E</td>
<td>Job Title is Invalid</td>
</tr>
<tr class="odd">
<td>9E</td>
<td>Adjustment Information Only</td>
<td>5A</td>
<td>Full amount of adjustment could not be applied to the debt. Cannot reduce below zero.</td>
</tr>
<tr class="even">
<td>9G</td>
<td>Action Code</td>
<td><p>5A</p>
<p>5B</p></td>
<td>Invalid Action Code (Syntax Validation)</td>
</tr>
<tr class="odd">
<td>9H</td>
<td>Debtor Closed due to Entity Out of Business</td>
<td>1, 2, 2A, 2B, 2C, 2D, 2E, 3, 4, 6</td>
<td>Debtor Closed due to Entity Out of Business</td>
</tr>
<tr class="even">
<td>9I</td>
<td>Debtor Closed due to Death</td>
<td>1, 2, 2A, 2B, 2C, 2D, 2E, 3, 4, 6</td>
<td>Debtor Closed due to Death</td>
</tr>
<tr class="odd">
<td>9J</td>
<td>Transaction’s Sequence Number should be between 1 and 999,999</td>
<td>5A, 5B</td>
<td>Transactions’ Sequence Number should be between 1 and 999,999</td>
</tr>
<tr class="even">
<td>9K</td>
<td>Trans Amt does not match the sum of components</td>
<td>5B</td>
<td>Trans Amt does not match the sum of components</td>
</tr>
<tr class="odd">
<td>9L</td>
<td>Trans ID has to be 15 chars long</td>
<td>5A, 5B</td>
<td>Trans ID has to be 15 chars long</td>
</tr>
<tr class="even">
<td>9M</td>
<td>Cannot adjust the current case balance below ZERO</td>
<td>5B</td>
<td>Cannot adjust the current case balance below ZERO</td>
</tr>
<tr class="odd">
<td>ZZ</td>
<td>Manual intervention required</td>
<td>H,1,2,2A, 2B,2C,2D, 2E,3,4,5A, 5B,6</td>
<td>A Non-Disclosed error was detected which requires manual intervention to discern the type of error that was encountered.</td>
</tr>
</tbody>
</table>

Cross-Servicing IAI Error CodesCross-Servicing IAI Error Codes

# Appendix C. Patient Statement Updates for Cross-Servicing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When debt on a debtor’s account has been referred to Cross-Servicing, the debt will no longer be included on the debtor’s Patient Statement. Also, the debt amount referred to Cross-Servicing will not be included in the total balance due. Additionally, the “Notice of Rights and Responsibilities” section has been updated to include information on the Cross-Servicing Program.

<span id="_Toc25567446" class="anchor"></span>Figure 123: Notice of Rights and Responsibilities (Page 1)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/099.png)

<span id="_Toc25567447" class="anchor"></span>Figure 124: Notice of Rights and Responsibilities (Page 2)

![](accounts-receivable-version-4-5-user-manual-cross-servicing-menu/100.png)

# Appendix D. Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym  | Definition                                                      |
|----------|-----------------------------------------------------------------|
| ABAL     | Agency Balance Adjustment                                       |
| AIO      | Agency Internal Offset                                          |
| AITC     | Austin Information Technology Center                            |
| AWG      | Administrative Wage Garnishment                                 |
| AR       | Accounts Receivable                                             |
| C&P      | Compensation & Pension                                          |
| CCPC     | Consolidated Co-Payment Processing Center                       |
| CPAC     | Consolidated Patient Account Center                             |
| CS       | Cross-Servicing                                                 |
| DATA Act | Digital Accountability and Transparency Act of 2014             |
| DCIA     | Debt Collection Improvement Act                                 |
| DMC      | Debt Management Center                                          |
| DMS      | Debt Management Services                                        |
| DOJ      | Department of Justice                                           |
| DPN      | Due Process Notification                                        |
| IAI      | Integrated Agency Interface                                     |
| IPAC     | Intra-governmental Payments and Collections                     |
| PCA      | Private Collection Agency                                       |
| SSN      | Social Security Number                                          |
| TCSP     | Treasury Cross-Servicing Program                                |
| TIN      | Tax Identification Number                                       |
| TOP      | Treasury Offset Program                                         |
| VA       | Department of Veterans Affairs                                  |
| VAMC     | VA Medical Center                                               |
| VistA    | Veterans Health Information Systems and Technology Architecture |
| VHA      | Veterans Health Administration                                  |

Acronyms

# Appendix E. Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AR – *See Accounts Receivable.*Account – A record established for a debtor in the AR Debtor file (#340). The account can contain multiple bills for an individual debtor.

Account Profile – A screen display or printout showing an activity summary for an entire account. This profile shows if debt on a debtor’s account has been referred to Cross-Servicing with the message, “Debt Referred to Cross-Servicing”.

Accounts Receivable (AR) – (1) In the broadest sense, debts owed to VA are referred as Accounts Receivable. (2) Synonymous with the abbreviation ‘AR’. (3) In this document, AR also refers to VA’s automated system designed to process first party debt.

Accounts Receivable Section – The staff responsible, as a group, for the establishment and maintenance of debtor account records.

Active Bill – Bills that are in an “Active” status are available for collection. Bills must be in an “Active” status in order to be referred to Cross-Servicing.

Address Unknown – This field is set in the AR Debtor file (#340) to indicate that the site has not been able to obtain a correct address for the debtor. If this field is set to YES, the debtor’s account will NOT be forwarded to Cross-Servicing.

Adjustment – A transaction that makes an administrative change to the principal balance of a bill or an account.

Admin Charge – An administrative charge incurred during the debt collection process and added to an account's principal balance. Fees for locator searches, marshal fees, and court costs are administrative charges.

Administrative Offset – To withhold money that is either payable by the Government to, or held by the Government for, a person or entity to satisfy a debt the person or entity owes the Government.

Administrative Wage Garnishment(AWG) – Under Federal law, a Federal agency may, without first obtaining a court order, order an employer to withhold up to 15 percent of a debtor’s wages for payment to the Federal agency to satisfy a delinquent non-tax debt.

Austin Information Technology Center (AITC) – VA’s data center site located in Austin, Texas. The AITC receives the transmission files for referred debts and updates to existing referrals from the VistA AR system on a scheduled basis. The AITC compiles this information and forwards it to DMC. The AITC also transmits both confirmation and reject messages to the AR system at each VAMC via MailMan.

AWG – *See Administrative Wage Garnishment*.

## B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bill – A receivable.

Bulletin – Electronic mail messages that are automatically delivered by MailMan under certain conditions. For example, a bulletin can be set up to fire when database changes occur, such as adding a record to the file of users.

Bureau of the Fiscal Service – Bureau of the Treasury Department formed from the con­solidation of the Financial Management Service and the Bureau of the Public Debt.

## C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCPC *– Refer to Consolidated Copayment Processing Center*.

Consolidated Copayment Processing Center– Each month, patient-billing information is transmitted to the Consolidated Copayment Processing Center (CCPC) system located at AITC. The CCPC prints and mails billing statements to patients.

Consolidated Patient Account Centers – A congressionally mandated program that enhanced billing and collections activities within VHA through the consolidation of traditional revenue program functions into regionalized centers of excellence. There are seven regional consolidated centers around the country: (1) Mid-Atlantic - Asheville, NC; (2) Mid-South - Smyrna, TN; (3) North Central - Middleton, WI; (4) Florida\Caribbean - Orlando, FL; (5) North East - Lebanon, PA; (6) Central Plains - Leavenworth, KS; and (7) West - Las Vegas, NV.

CPAC – *Refer to Consolidated Patient Account Centers.*Creditor Agency – An agency which is owed money, requests Treasury’s services in collecting the debt, and includes its own delinquent debtor records in Treasury’s system for offset. Creditor agencies receive monies that have been offset on their behalf from payments due delinquent debtors.

CS – *Refer to Cross-Servicing*.

Cross-Servicing – The Cross-Servicing functionality, developed as part of the Cross-Servicing program, was delivered and integrated under the VistA AR 4.5 patch, PRCA\*4.5\*301. This new functionality will allow VHA to refer a debt that has been delinquent 120 days or more to Treasury for collection.

## D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATA Act of 2014 – *Refer to Digital Accountability and Transparency Act of 2014.*Debt – An amount of money that has been determined by an appropriate Federal official to be owed to the United States (U.S.) from any person, organization, or entity other than another Federal agency. Included as debts are amounts due the U.S. from fees, duties, leases, rents, royalties, services, sales of real or personal property, overpayments, fines, penalties, damages, taxes, interest, forfeitures, loans, and other sources.

Debt Collection – This is the official name given to the process of sending out bills and collecting payments.

Debt Management Center (DMC) – The nationwide debt collection operation for VA located at the St. Paul VA Regional Office and Insurance Center.

Debt Management Services (DMS) – As part of the U.S. Department of the Treasury’s Bureau of the Fiscal Service, DMS works with Federal government agencies to provide a comprehensive debt management program. DMS also provides debt collection services to the states.

Debtor – A patient, person, vendor, insurance company, or institution that owes VA money.

Default – A suggested response provided by the system.

Delinquent – The failure of the debtor to pay an obligation or debt when due.

Digital Accountability and Transparency Act of 2014 (DATA Act) – Requires VA to notify Treasury of any legally enforceable, non-tax debt owed to VA that is over 120 days delinquent so that Treasury can offset such debt administratively.

DMC – *See Debt Management Center.*DMS – *See Debt Management Services.*Due Process – In the context of debt collection, the legal rights of a debtor to be informed of the adverse action and to challenge the propriety of the creditor agency’s decision (e.g., to obtain review within the agency of the indebtedness, etc.).

## F

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FedDebt – A system that supports the Federal government’s delinquent, debt collection programs, by providing Debt Management Services (DMS) with a single platform for its business applications, a single entry portal for its business applications, online access for creditor agencies via a web-based customer interface, and a single database for reporting.

FMS – *See Treasury Financial Management Service.*

## G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

G.TCSP – Mail group that receives all bulletins and transmission messages related to Cross-Servicing.

## I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IAI – *See Integrated Agency Interface.*Integrated Agency Interface – The Integrated Agency Interface (IAI) was developed to provide agencies with a single file format to submit multiple record types to FedDebt. IAI can: (1) refer initial debts, (2) recall debts, (3) process collections, reversals, and make adjustments, and (4) modify debt and / or debtor information.

Interest – Amount charged to an account being paid on a repayment plan for carrying the account or on delinquent accounts.

## M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mail Groups – List of e-mail recipients who can all be addressed at once by reference to a mail group name defined in VistA. Cross-Servicing messages are sent to the G.TCSP mail group.

## P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Statement of Account – The monthly statement for patient type debtors, reflecting all activity (both charges and payments) recorded for that patient since his last statement was printed. Debt referred to Cross-Servicing will not display on the patient statement, nor will the amount of the Cross-Serviced debt be included in the Total Debt due.

PCA– *See Private Collection Agency.*PRCA Nightly Process – Set of AR routines scheduled to run at the same time every night. These routines update all actions completed through the AR VistA software. In addition, this set of routines includes those that create, record, and transmit all Cross-Servicing Messages to AITC. Cross-Servicing information is sent to AITC and the local VistA mail groups: Cross-Servicing (G.TCSP).

Private Collection Agency (PCA) – Private sector companies with expertise in the area of debt collection, to assist the government in its debt collection efforts. Once Treasury has exhausted efforts to collect the debts internally, the debts are sent to the PCAs for collection activity. The activities of the PCAs are monitored by the personnel of the Receivables Management and Debt Services Division of Debt Management Services (DMS).

Profile of Accounts Receivable – Accounts Receivable option displays information on debtor accounts. This profile shows if debt on a debtor’s account has been referred to Cross-Servicing with the message, “Debt Referred to Cross-Servicing”.

## R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RCDP TCSP FLAG - This security key allows users that are assigned to edit the TCSP flag on Debtor and/or Bill. This Security Key, RCDP TCSP FLAG, should ONLY be allocated by CPAC IT and given ONLY to Veteran Services Supervisors and/or Veteran Services Leads (One, Two or Three). Security key introduced with routine, RCDPCSA, in Accounts Receivable patch, PRCA\*4.5\*325.

Reconciliation – Following the referral of a debt to Cross-Servicing, there are various reasons why a debt may be returned by Treasury for Reconciliation, including, but not limited to, the following: (1) Compromise Offer, (2) Uncollectable, (3) Administrative Resolution Approved for Bankruptcy, and (4) Administrative Resolution Approved for Death. These returned debts are sent from Treasury to VistA in the form of a Reconciliation File on the first day of every month.

## S

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Stop/Reactivate TCSP Referral Option – A menu option provided to stop a debt or Debtor from being referred to Cross-Servicing. This option also is used to remove the ‘Stop’ flag.

## T

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Tasked Job – A job, usually a printout, which has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.

Taxpayer Identification Number (TIN) – A nine-digit unique identifier assigned to all individuals and businesses that file tax returns in the United States. For individuals, the *Social Security Number (SSN)* serves as the TIN; for businesses, organizations, and non-profit entities the *Employer Identification Number (EIN)* assigned by IRS, serves as the TIN.

TCSP – Department of Treasury Cross-Servicing Program

TCSP Flag Control – This option is used to correct debtor/bill for Treasury Cross Service as seen when viewing the same debtor/bill on the Treasury System or from the monthly TCSP reconciliation report. Note that this option is only seen by and accessible to those users assigned to security key, RCDP TCSP FLAG. This option will allow TCSP flag control to the following options:

> 1\) Set cross-service flag on BILL

> 2\) Clear cross-service flag on BILL

> 3\) Clear cross-service flag on DEBTOR (AND ALL BILLS)

> 4\) Set cross-service flag on DEBTOR

> 5\) Fully re-establish debtor/bill as cross-serviced

TIN – *See Taxpayer Identification Number.*TOP – *See Treasury Offset Program.*Total CS Debt – The total amount of debt referred to Cross-Servicing.

Transaction – Any action that affects a bill or an account. All transactions are numbered sequentially and can be examined individually.

Transaction Number – A number assigned by the computer for an activity against a debt (such as increase adjustment, decrease adjustment, payment, etc.)

Transaction Profile – A screen display or printout that shows a summary of a single transaction.

Treasury Offset Program (TOP) – Mandatory government wide delinquent debt matching and payment offset system. Debts that cannot be collected by the DMC must be forwarded to this collection program where delinquent debts may be recovered by offset of income tax refunds; Federal salary pay, including military pay; Federal retirement, including military retirement pay; Federal benefit payments; and other Federal payments. NOTE: The Cross-Servicing Program will be used in replace of TOP for all new, First Party debts.

## U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Update – An addition, deletion, or change to a debtor’s record.

Update File – Each Tuesday, AR software reviews accounts currently referred to Cross-Servicing and sends updates for Cross-Servicing name, address changes, and decrease adjustments.

## V

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA – Veterans Health Information Systems and Technology Architecture. The VA-developed computer system that supports day-to-day operations at local VA health care facilities.

## W

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Waiver – Decision that conditions exist which, under the applicable statutes and regulations, preclude recovery by VA of the outstanding debt, including interest and other late payment charges. An example of a situation when a Veteran may request a waiver is for undue financial hardship.

# Appendix F. References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  [31 USC § 3716 - Administrative offset](http://www.gpo.gov/fdsys/granule/USCODE-2010-title31/USCODE-2010-title31-subtitleIII-chap37-subchapII-sec3716/content-detail.html)
2.  Austin Information Technology Center (AITC). *Lockbox to AR Transmission Layout*.
3.  Bureau of the Fiscal Services – [Debt Management and Cross-Servicing](https://fiscal.treasury.gov/dms)
4.  Bureau of the Fiscal Services – [Guides, Policies, and Instructions](https://fiscal.treasury.gov/dms/legal-authorities/guide-policy-instructions.html)
5.  Bureau of the Fiscal Services – [Legal Authorities Quick Reference Chart](https://fiscal.treasury.gov/dms/legal-authorities/code-of-federal-regulations.html)
6.  Bureau of the Fiscal Services – [Public Laws, Statutes, Regulations & Guidance Managing Federal Receivables](https://fiscal.treasury.gov/dms/legal-authorities/public-laws.html)
7.  [Debt Collection Improvement Act (DCIA) of 1996](https://fiscal.treasury.gov/dms/about/about-dcia.html)
8.  [Digital Accountability and Transparency Act (DATA Act)](http://www.gpo.gov/fdsys/pkg/PLAW-113publ101/html/PLAW-113publ101.htm)
9.  [FedDebt Q & A Site](https://fiscal.treasury.gov/dms/faqs/for-the-general-public.html)
10. [Treasury Financial Manual](http://www.fms.treas.gov/tfm/vol1/v1p4c400.pdf)
11. U.S. Department of Treasury. Debt Management Services. Financial Management Service. *Integrated Agency Interface File Format For Cross-Servicing*.

[^1]: U.S. Department of Treasury. Debt Management Services. Financial Management Service. Integrated Agency Interface File Format For Cross-Servicing.