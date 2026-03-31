---
title: IFCAP Version 5.1 Purchase Card User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Purchase Card User's Guide
app_code: PRC
app_name: IFCAP
section: FIN
app_status: active
pkg_ns: PRC
patch_ver: 5.1
patch_id: PRC*5.1
group_key: "PRC:PRC:5.1"
file_numbers: 
  - 440
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - strong
  - card
  - purchase
  - table
  - order
  - contents
  - report
  - date
  - colgroup
  - tbody
page_count: 0
word_count: 44181
section_count: 70
table_count: 13
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1purchase_card.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1purchase_card.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

Integrated Funds Distribution, Control Point Activity, Accounting and Procurement  
(IFCAP) Version 5.1

Purchase Card  
User's Guide

![](ifcap-version-5-1-purchase-card-user-s-guide/001.png)

September 2025

Department of Veterans Affairs (VA)Office of Information and Technology (OIT)

Revision History

Initiated on 12/29/04

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 51%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Revision</td>
<td>Description</td>
<td>Author(s)</td>
</tr>
<tr class="even">
<td>September 2025</td>
<td>7.0</td>
<td>The PRCHL GUI Logistics Data Query Tool option has been marked Out of Order with patch PRC*5.1*247</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>May 2025</td>
<td>6.0</td>
<td>Patch PRC*5.1*238: FPDS Questions Removal</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>October 2011</td>
<td>5.0</td>
<td>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358. See page <a href="#glossary">11-1</a>.</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>11/05/08</td>
<td>4.0</td>
<td>US Bank purchase card activation, per patch PRC*5.1*125.</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>05/31/07</td>
<td>3.0</td>
<td>Added information covering the use of the Logistics Data Query Tool (LDQT), per patch PRC*5.1*103.</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>02/08/06</td>
<td>2.0</td>
<td>Updated to reflect changes included in patch PRC*5.1*79 (FPDS ICAR for VistA).</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>12/29/04</td>
<td>1.1</td>
<td>PDF file checked for accessibility to readers with disabilities.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/29/04</td>
<td>1.0</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Introduction](#introduction)
  - [The Role of the Purchase Card User](#the-role-of-the-purchase-card-user)
  - [Reference Numbering System](#reference-numbering-system)
  - [Legal Requirements and Security Measures](#legal-requirements-and-security-measures)
  - [Package Operation](#package-operation)
  - [FMS-ET VENDOR FIELDS](#fms-et-vendor-fields)
- [Record Card Purchases in IFCAP](#record-card-purchases-in-ifcap)
  - [Introduction](#introduction-1)
  - [Determine What Kind of Purchase Card Order to Enter](#determine-what-kind-of-purchase-card-order-to-enter)
  - [Enter a Simplified Purchase Card Order](#enter-a-simplified-purchase-card-order)
    - [Introduction](#introduction-2)
    - [Menu Path](#menu-path)
    - [Prompts](#prompts)
  - [New Detailed Purchase Card Order](#new-detailed-purchase-card-order)
    - [Introduction](#introduction-3)
    - [Menu Path](#menu-path-1)
    - [Prompts](#prompts-1)
  - [Editing Purchase Card Orders](#editing-purchase-card-orders)
    - [Edit, Amend, or Adjust Purchase Card Orders](#edit-amend-or-adjust-purchase-card-orders)
    - [Editing a Simplified Purchase Card Order](#editing-a-simplified-purchase-card-order)
    - [Editing a Detailed Purchase Card Order](#editing-a-detailed-purchase-card-order)
- [Create and Convert Orders](#create-and-convert-orders)
  - [Introduction](#introduction-4)
  - [Create a PC order from a RIL](#create-a-pc-order-from-a-ril)
    - [Menu Path](#menu-path-2)
    - [Prompts](#prompts-2)
  - [Convert Temporary 2237 to PC Request](#convert-temporary-2237-to-pc-request)
    - [Menu Path](#menu-path-3)
    - [Prompts](#prompts-3)
- [Convert PC Orders to Other Document Types](#convert-pc-orders-to-other-document-types)
  - [Introduction](#introduction-5)
  - [Convert a PC order to a 2237](#convert-a-pc-order-to-a-2237)
    - [Menu Path](#menu-path-4)
    - [Display of Option](#display-of-option)
  - [Convert a 2237 to a Delivery Order](#convert-a-2237-to-a-delivery-order)
    - [Menu Path](#menu-path-5)
    - [Display the Option](#display-the-option)
- [# Record Receipt of a PC Order](#record-receipt-of-a-pc-order)
  - [Introduction](#introduction-6)
  - [Menu Path](#menu-path-6)
  - [Prompts](#prompts-4)
- [Reconcile Payment Authorizations from FMS](#reconcile-payment-authorizations-from-fms)
  - [Introduction](#introduction-7)
    - [The Purchase Card Reconciliation Process](#the-purchase-card-reconciliation-process)
    - [Data Sharing for Reconciliation](#data-sharing-for-reconciliation)
  - [Menu Path](#menu-path-7)
  - [Automatic Reconciliations](#automatic-reconciliations)
    - [Auto Charge Selection](#auto-charge-selection)
    - [Manual Charge Selection](#manual-charge-selection)
    - [Reconcile by Purchase Card Order](#reconcile-by-purchase-card-order)
  - [ET-FMS Document Display](#et-fms-document-display)
    - [Introduction](#introduction-8)
    - [Menu Path](#menu-path-8)
    - [Prompts](#prompts-5)
  - [Edit/Remove Reconciliation](#editremove-reconciliation)
    - [Introduction](#introduction-9)
    - [Menu Path](#menu-path-9)
    - [Prompts](#prompts-6)
  - [Daily Purchase Card Charges Statement](#daily-purchase-card-charges-statement)
    - [Introduction](#introduction-10)
    - [Menu Path](#menu-path-10)
    - [Prompts](#prompts-7)
- [Approving Official Options](#approving-official-options)
  - [Approve Reconciliation](#approve-reconciliation)
    - [Introduction](#introduction-11)
    - [Menu Path](#menu-path-11)
    - [Prompts](#prompts-8)
  - [Reports](#reports)
    - [Introduction](#introduction-12)
    - [Menu Path](#menu-path-12)
    - [Unreconciled Austin Payments – Official](#unreconciled-austin-payments-official)
    - [Unreconciled Purchase Card Transactions – Official](#unreconciled-purchase-card-transactions-official)
    - [Card Holder Daily Charge Statement](#card-holder-daily-charge-statement)
    - [Delinquent PC Listing – Official](#delinquent-pc-listing-official)
    - [Disputed Purchase Card Orders – Official](#disputed-purchase-card-orders-official)
    - [History of Purchase Card Transactions – Official](#history-of-purchase-card-transactions-official)
    - [Incomplete Purchase Card Orders – Official](#incomplete-purchase-card-orders-official)
    - [Official Charges Audit](#official-charges-audit)
    - [Purchase Card Orders Ready for Approval](#purchase-card-orders-ready-for-approval)
    - [Reconciled Purchase Card Transactions – Official](#reconciled-purchase-card-transactions-official)
- [Purchase Card Coordinator Options](#purchase-card-coordinator-options)
  - [Introduction](#introduction-13)
  - [Austin Audit Information](#austin-audit-information)
    - [Introduction](#introduction-14)
    - [Menu Path](#menu-path-13)
    - [Prompts](#prompts-9)
  - [Charge Card Reg. Exception](#charge-card-reg-exception)
    - [Introduction](#introduction-15)
    - [Menu Path](#menu-path-14)
    - [Prompts](#prompts-10)
  - [Coordinator Approving Official Charge Audit](#coordinator-approving-official-charge-audit)
    - [Introduction](#introduction-16)
    - [Menu Path](#menu-path-15)
    - [Prompts](#prompts-11)
  - [Daily Charge Transmission Log](#daily-charge-transmission-log)
    - [Introduction](#introduction-17)
    - [Menu Path](#menu-path-16)
    - [Prompts](#prompts-12)
  - [Delinquent Approvals](#delinquent-approvals)
    - [Introduction](#introduction-18)
    - [Menu Path](#menu-path-17)
    - [Prompts](#prompts-13)
  - [Delinquent PC Listing](#delinquent-pc-listing)
    - [Introduction](#introduction-19)
    - [Menu Path](#menu-path-18)
    - [Prompts](#prompts-14)
  - [Delinquent Reconciliations](#delinquent-reconciliations)
    - [Introduction](#introduction-20)
    - [Menu Path](#menu-path-19)
    - [Prompts](#prompts-15)
  - [Fiscal Daily Review](#fiscal-daily-review)
    - [Introduction](#introduction-21)
    - [Menu Path](#menu-path-20)
    - [Prompts](#prompts-16)
  - [History of Purchase Card Transactions](#history-of-purchase-card-transactions)
    - [Introduction](#introduction-22)
    - [Menu Path](#menu-path-21)
    - [Prompts](#prompts-17)
  - [IMPAC Account Information](#impac-account-information)
    - [1ntroduction](#1ntroduction)
    - [Menu Path](#menu-path-22)
    - [Prompts](#prompts-18)
  - [Inactivate Expired Charge Cards](#inactivate-expired-charge-cards)
    - [Introduction](#introduction-23)
    - [Menu Path](#menu-path-23)
    - [Prompts](#prompts-19)
  - [Incomplete Purchase Card Orders Report](#incomplete-purchase-card-orders-report)
    - [Introduction](#introduction-24)
    - [Menu Path](#menu-path-24)
    - [Prompts](#prompts-20)
  - [Print Unregistered Credit Card Charges](#print-unregistered-credit-card-charges)
    - [Introduction](#introduction-25)
    - [Menu Path](#menu-path-25)
    - [Prompts](#prompts-21)
  - [Purchase Card exceptions/replacements](#purchase-card-exceptionsreplacements)
    - [Introduction](#introduction-26)
    - [Menu Path](#menu-path-26)
    - [Prompts](#prompts-22)
  - [Purchase Card Information List](#purchase-card-information-list)
    - [Introduction](#introduction-27)
    - [Menu Path](#menu-path-27)
    - [Prompts](#prompts-23)
  - [Purchase Card Registration](#purchase-card-registration)
    - [Introduction](#introduction-28)
    - [Menu Path](#menu-path-28)
    - [Prompts](#prompts-24)
  - [Purchase Card Statistics](#purchase-card-statistics)
    - [Introduction](#introduction-29)
    - [Menu Path](#menu-path-29)
    - [Prompts](#prompts-25)
  - [Purchase Card Timely Commitment Report](#purchase-card-timely-commitment-report)
    - [Introduction](#introduction-30)
    - [Menu Path](#menu-path-30)
    - [Prompts](#prompts-26)
  - [Reconciled Purchase Card Transactions](#reconciled-purchase-card-transactions)
    - [Introduction](#introduction-31)
    - [Menu Path](#menu-path-31)
    - [Prompts](#prompts-27)
  - [Retrieve Unregistered Credit Card Charges](#retrieve-unregistered-credit-card-charges)
    - [Introduction](#introduction-32)
    - [Menu Path](#menu-path-32)
    - [Prompts](#prompts-28)
  - [Summary Report of Unpaid PC Transactions](#summary-report-of-unpaid-pc-transactions)
    - [Introduction](#introduction-33)
    - [Menu Path](#menu-path-33)
    - [Prompts](#prompts-29)
  - [Unapproved Reconciliations](#unapproved-reconciliations)
    - [Introduction](#introduction-34)
    - [Menu Path](#menu-path-34)
    - [Prompts](#prompts-30)
  - [Unreconciled Austin Payment Transactions](#unreconciled-austin-payment-transactions)
    - [Introduction](#introduction-35)
    - [Menu Path](#menu-path-35)
    - [Prompts](#prompts-31)
  - [Unreconciled Purchase Card Transactions](#unreconciled-purchase-card-transactions)
    - [Introduction](#introduction-36)
    - [Menu Path](#menu-path-36)
    - [Prompts](#prompts-32)
- [Supplemental Purchase Card Options](#supplemental-purchase-card-options)
  - [Introduction](#introduction-37)
  - [Amendment to Purchase Card Order](#amendment-to-purchase-card-order)
    - [Introduction](#introduction-38)
    - [Amendment types](#amendment-types)
    - [Order Status after Amendment](#order-status-after-amendment)
    - [Menu Path](#menu-path-37)
    - [Prompts](#prompts-33)
  - [Adjustment Voucher to Purchase Card Order](#adjustment-voucher-to-purchase-card-order)
    - [Introduction](#introduction-39)
    - [Menu Path](#menu-path-38)
    - [Prompts](#prompts-34)
  - [Purchase Card Reports Menu](#purchase-card-reports-menu)
    - [Introduction](#introduction-40)
  - [Unreconciled Austin Payments-Buyer](#unreconciled-austin-payments-buyer)
    - [Introduction](#introduction-41)
    - [Menu Path](#menu-path-39)
    - [Prompts](#prompts-35)
    - [Introduction](#introduction-42)
    - [Menu Path](#menu-path-40)
    - [Prompts](#prompts-36)
  - [BOC Report for OA&MM/Fiscal](#boc-report-for-oammfiscal)
    - [Introduction](#introduction-43)
    - [Menu Path](#menu-path-41)
    - [Prompts](#prompts-37)
  - [Delinquent PC Listing – Buyer](#delinquent-pc-listing-buyer)
    - [Introduction](#introduction-44)
    - [Menu Path](#menu-path-42)
    - [Prompts](#prompts-38)
  - [Disputed Purchase Card Orders – Buyer](#disputed-purchase-card-orders-buyer)
    - [Introduction](#introduction-45)
    - [Menu Path](#menu-path-43)
    - [Prompts](#prompts-39)
  - [Final Charge YES - Reconciled Orders – Buyer](#final-charge-yes-reconciled-orders-buyer)
    - [Introduction](#introduction-46)
    - [Menu Path](#menu-path-44)
    - [Prompts](#prompts-40)
  - [History of Purchase Card Transactions – Buyer](#history-of-purchase-card-transactions-buyer)
    - [Introduction](#introduction-47)
    - [Menu Path](#menu-path-45)
    - [Prompts](#prompts-41)
  - [Incomplete Purchase card Orders – Buyer](#incomplete-purchase-card-orders-buyer)
    - [Introduction](#introduction-48)
    - [Menu Path](#menu-path-46)
    - [Prompts](#prompts-42)
  - [Reconciled Purchase Card Transactions – Buyer](#reconciled-purchase-card-transactions-buyer)
    - [Introduction](#introduction-49)
    - [Menu Path](#menu-path-47)
    - [Prompts](#prompts-43)
  - [Cancel an Incomplete PC Order](#cancel-an-incomplete-pc-order)
    - [Introduction](#introduction-50)
    - [Menu Path](#menu-path-48)
    - [Prompts](#prompts-44)
  - [Purchase Card Display/Print Menu](#purchase-card-displayprint-menu)
    - [Introduction](#introduction-51)
    - [Menu Path](#menu-path-49)
  - [Inquire-Purchase Card Information](#inquire-purchase-card-information)
    - [Introduction](#introduction-52)
    - [Menu Path](#menu-path-50)
    - [Prompts](#prompts-45)
  - [Purchase Card Transaction Status](#purchase-card-transaction-status)
    - [Introduction](#introduction-53)
    - [Menu Path](#menu-path-51)
    - [Prompts](#prompts-46)
  - [Reprint Purchase Card Order](#reprint-purchase-card-order)
    - [Introduction](#introduction-54)
    - [Menu Path](#menu-path-52)
    - [Prompts](#prompts-47)
- [The Logistics Data Query Tool](#the-logistics-data-query-tool)
- [Glossary](#glossary)
- [Index](#index)
This manual is designed to provide you with the information necessary to use the Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) system to report, record, and amend Purchase Card purchases. The IFCAP package has automated certain functions in Acquisition and Materiel Management Services (A&MM), Fiscal Service, and all of the services that request supplies and services.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The Role of the Purchase Card User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purchase Card Users use Purchase Cards to pay for goods and services and use IFCAP to report these purchases. Purchase Card Users also review the payments that the Credit Card Vendor makes to the Purchase Card account. After the Purchase Card User matches the payment to the Purchase Card order (Reconciliation), the Approving Official approves the Reconciliation.

This manual will teach you how to use IFCAP (Integrated Funds Distribution, Control Point Activity, Accounting and Procurement) to record purchases, edit Purchase Card orders, report receipt of goods and services bought with a Purchase Card, review an FMS payment report, approve payments Reconciled (Approving Officials only,) create reports. The manual will also show users how to convert a Purchase Card order into a Delivery Order or into a VA Form 2237 for completion as a Purchase Order and/or delivery order

This manual explains how to perform the role of the Purchase Card User by dividing that role into small, manageable tasks. The authors of this manual have listed these tasks in successive order so that each instruction builds on the functionality and information from the previous instructions. This will allow new Purchase Card Users to use this manual as a tutorial by following the instructions from beginning to end. Experienced Purchase Card Users can use this manual as a reference tool by using the index and table of contents.

## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses a special paragraph numbering system to allow users to understand how the sections of the manual relate to each other. For example, this paragraph is section 1.3. This means that this paragraph is the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections 1.3.1 and 1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third subsection of Chapter 1. All clear? Actually, all this means is that users that want to divide their reading into manageable lessons can concentrate on one section and all of its subsections, e.g., section 1.3.5 and all of its subsections would make a coherent lesson.

## Legal Requirements and Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP allows only the person who enters an order or their approved surrogate to edit that order. This is a security measure that prevents users from altering the requests of others. Due to the nature of the information being processed by IFCAP, special attention has been paid to limiting usage to authorized individuals. Individuals in the system who have authority to approve actions, at whatever level, have an electronic signature code. This code is required before the documents pass to a new level for processing or review. Like the access and verify codes used when gaining access to the system, the electronic signature code will not be visible on the terminal screen. These codes are also encrypted so that even when viewed in the user file by those with the highest levels of access, they are unreadable. Electronic signature codes are required by IFCAP at every level that currently requires a signature on paper. To designate IFCAP Purchase Card Users, the IFCAP Purchase Card Coordinator will use the Purchase Card Registration option.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP automates fiscal, budgetary, inventory, billing and payment activities. To accomplish all of these tasks, IFCAP consists of several functional components, each responsible for a similar set of tasks:

- Funds Distribution (Fiscal Component)
- Funds Control (Control Point Component)
- Processing Requests (Control Point Component)
- Purchase Orders/Requisitions (A&MM Component)
- Accounting (Fiscal Component)
- Receiving (A&MM Component)
- Inventory (A&MM/Control Point Component)

As a Purchase Card User, you are affecting Control Point balances. Different kinds of IFCAP users have different menus. If the menus in this manual don’t include options that you see on your screen, don’t panic! The instructions in this manual only use the options that you have as a Purchase Card User. If you don’t know what to enter at an IFCAP prompt, enter one, two or three question marks and IFCAP will list your available options or explain the prompt. The more question marks you enter at the prompt, the more information IFCAP will provide.

The options you use on IFCAP have been divided into groups based upon the type of work you do. When you select these options, IFCAP will ask you a series of questions. If you do not understand the question or are unsure of how to respond, enter a question mark (?) and the computer will explain the question, or allow you to choose from a list of responses.

## FMS-ET VENDOR FIELDS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must populate the field FMS-ET Vendor Code using the Site Parameters option before your site can use the Purchase Card Reconciliation process. A second field is the FMS-ET Alternate Address Indicator. Currently the FMS-ET Alternate Address Indicator is to be left blank.

# Record Card Purchases in IFCAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To ensure that balances are accurate for the Control Point which funds purchases made via your Purchase Card, all such purchases must be recorded in IFCAP.

## Determine What Kind of Purchase Card Order to Enter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to record the purchase of goods or services that will be delivered after purchase, create a *detailed* Purchase Card order (see 2.4 below). You should also create a detailed Purchase Card order if you need to enter information about specific items being tracked in an inventory point. Otherwise, create a *simplified* Purchase Card order (see 2.3 below).

|                                                                                                                      |                                                                       |                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-purchase-card-user-s-guide/002.png) | *Note:* No procurement history is collected on Simplified Orders. | ![](ifcap-version-5-1-purchase-card-user-s-guide/003.png) |

## Enter a Simplified Purchase Card Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option allows you to log enough information about the purchase that you can easily reconcile it with the payment from CitiBank. In the background, IFCAP will create the appropriate CONTROL POINT ACTIVITY (#410) and PROCUREMENT & ACCOUNTING TRANSACTIONS (#442) file entries. IFCAP will populate many of the fields in this option with values from the Purchase Card Information file. This option also allows you to edit these fields and enter other details about the purchase.

This option may not be used to enter purchases where the cost exceeds \$2500. For orders over \$2500, you *must* use the New Detailed Purchase Card Order option (see 2.4 below).

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Purchase Card Menu, select the New Detailed Purchase Card Order option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Purchase Card Reports Menu ...</p>
<p>Approving Official Menu ...</p>
<p>Process Purchase Card Menu ...</p>
<p>Purchase Card Display/Print Menu ...</p>
<p>Reconciliation Menu ...</p>
<p>Select Purchase Card Menu Option: Process Purchase Card Menu</p>
<p>New Simplified Purchase Card Order</p>
<p>Edit Simplified Purchase Card Order</p>
<p>New Detailed Purchase Card Order</p>
<p>Edit Detailed Purchase Card Order</p>
<p>Amendment To Purchase Card Order</p>
<p>Adjustment Voucher To Purchase Card Order</p>
<p>Receive Purchase Card Order</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Create P/C Order From Repetitive Item List</p>
<p>Convert P/C Order To 2237 Request</p>
<p>Convert P/C Order to a Delivery Order</p>
<p>Cancel An Incomplete PC Order</p>
<p>Convert Temporary 2237 to PC Request</p>
<p>Select Process Purchase Card Menu Option: New Simplified Purchase Card Order</p></td>
</tr>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number if prompted. Usually, the primary station number will be the default. Press \<Enter\> to accept the default, or type in the required station number and then press \<Enter\>.

Enter the purchase order number series. This is a common number series already defined for use on Purchase Card orders at your station. IFCAP will generate the next available purchase order number and prompt you, “Are you adding ‘\[PO \#\]’ as a new Purchase Order Number?”

Enter the substation. If the facility has been integrated with another facility you may be prompted for a Substation. Enter the appropriate Substation number. If your station is not integrated, this prompt will not appear.

At the Purchase Card Name: prompt, if you have more than one Purchase Card, enter the Purchase Card name you are using to purchase the items or services.

At the P.O. Date: prompt, enter the date of the new purchase order.

At the PCDO Vendor: prompt, enter the vendor for the Purchase Card order. If you wish to use a vendor that is *not* in the Vendor File, enter the word SIMPLIFIED at the prompt. At the FREE TEXT Vendor: prompt, enter the name of the vendor you wish to use.

At the FCP: prompt, enter the Fund Control Point for the order. IFCAP will use the information associated with the Purchase Card as the default value for this prompt. Make sure that you change the value if it is different from the default.

At the ???: prompt, enter the cost center for the order. Cost centers allow Fiscal staff to create total expense records for a section or service. IFCAP will supply a default value for this prompt based on the information associated with the Purchase Card. Make sure that you change the value if it is different from the default.

At the Classification of Request: prompt, create a classification name for the request if you like, or press \<Enter\> to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define.

At the Purchase Cost: prompt, enter the cost of the purchase. If the cost exceeds \$2500.00, the following message will appear, and you will not be allowed to proceed. The message “COST CANNOT EXCEED \$2500.00 - YOU MUST USE DETAILED PURCHASE CARD!!” will appear.

At the ???: prompt, enter a description of the purchase.

At the BOC: prompt, enter the Budget Object Code for the purchase. If you do not know the BOC, enter two question marks at the prompt and IFCAP will display the available BOCs. IFCAP will supply a default value for this prompt based on the information associated with the Purchase Card. Make sure that you change the value if it is different from the default.

At the ???: prompt, enter comments if you like.

if this purchase is assigned to a project, office, or some other category for which a sort group has been created, at the Sort Group: prompt, enter a sort group. If this purchase does not belong to a sort group, just press \<Enter\>. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group.

At the Select Sub-Control Point: prompt, you can associate this purchase with a category of purchases defined by the Fund Control Point. This allows you to group similar purchases together.

At the \$Amount: prompt, enter the amount that you want to charge the Sub-Control Point.

You may review the Purchase Card order if you like. IFCAP will display the new Purchase Card order to your screen.

You will now be prompted for your Electronic Signature Code.

You may print the Purchase Card order using the output device you specified.

|                                                                                                                        |                                                                                                                                                                         |                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-purchase-card-user-s-guide/004.png) | *Note:* If the order is over \$2500.00 or is on a contract, you *cannot* use the Simplified Purchase Card option. You *must* use the Detailed Purchase Card option! | ![](ifcap-version-5-1-purchase-card-user-s-guide/005.png) |

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><p>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</p>
<p>ENTER A NEW PURCHASE ORDER NUMBER OR A COMMON NUMBERING SERIES</p>
<p>PURCHASE ORDER: p05 999-P05 PC AUTHORIZED BUYER</p>
<p>Are you adding '999-P05125' as a new Purchase Order number ? y (YES)</p>
<p>PURCHASE CARD NAME: IFVENDOR,ONE IFVENDOR,ONE</p>
<p>P.O. DATE: TODAY// (FEB 06, 2006)</p>
<p>PCDO VENDOR: IFVENDOR5,TEN IFVENDOR5,TEN PH: NO: 41360</p>
<p>ORD ADD: IFVENDOR5,TEN FMS:</p>
<p>CODE: FAX:</p>
<p>Business Type Undefined</p>
<p>...OK? Yes// (Yes)</p>
<p>FREE TEXT VENDOR: IFVENDOR,TWO</p>
<p>FCP: 911 PROSTHETICS// 0160A1 10 01AE 01AE27200</p>
<p>COST CENTER: 827200// Prosthetic Activity</p>
<p>CLASSIFICATION OF REQUEST:</p>
<p>PURCHASE COST: 2501.</p>
<p>COST CANNOT EXCEED $2500.00 - YOU MUST USE DETAILED PURCHASE CARD!!</p>
<p>PURCHASE COST: 2501.// 2500.</p>
<p>DESCRIPTION:</p>
<p>1&gt;PROSTHETIC LEFT LEG</p>
<p>2&gt;</p>
<p>EDIT Option:</p>
<p>BOC: 2692 Prosthetic Supplies Replace</p>
<p>2692 Prosthetic Supplies</p>
<p>COMMENTS:</p>
<p>1&gt; Example of Simplified Order</p>
<p>SORT GROUP:</p>
<p>Select SUB-CONTROL POINT:</p>
<p>Review Purchase Card Order ? YES// (YES)</p>
<p>PC ORDER: 999-P05125 STATUS: Order Not Completely Prepared</p>
<p>M.O.P.: PURCHASE CARD LAST PARTIAL RECD.:</p>
<p>REQUESTING SERVICE:</p>
<p>VENDOR: IFVENDOR,TWO SHIP TO: IFVENDOR5,TEN</p>
<p>V.A. Medical Center</p>
<p>670 SOMEWHERE Street, NW</p>
<p>ANYCITY, NM 99999</p>
<p>________________________________________________________________________________</p>
<p>FOB POINT: |PROPOSAL: |AUTHORITY:</p>
<p>COST CENTER: 82OO00 | |</p>
<p>TYPE: | |BUYER:</p>
<p>DELIVER ON/BEFORE |CONTRACT: | IFBUYER,ONE</p>
<p>DISCOUNT TERM: | |DATE: 2/6/2006</p>
<p>APP: 3600160-911 | |</p>
<p>| |TOTAL: 2500.00</p>
<p>--------------------------------------------------------------------------------</p>
<p>ENTER '^' TO HALT:</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>--------------------------------------------------------------------------------</p>
<p>&gt;PROSTHETIC LEFT LEG 2500.00</p>
<p>BOC: 2692</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p>
<p>Print Purchase Card Order ? YES// (YES)</p>
<p>Cost of this request: $2500.00</p>
<p>Current Control Point Balance: $2098973.54</p></td>
</tr>
<tr class="even">
<td>QUEUE ON DEVICE: S</td>
<td>Enter your printer selection here</td>
</tr>
</tbody>
</table>

## New Detailed Purchase Card Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to record the purchase of goods or services that will be delivered after purchase, or you are tracking items in an inventory point create a detailed Purchase Card order. You should also create a detailed Purchase Card order if you need to enter information about specific items on the order. Note: Use of the Detailed Purchase Card Order updates the Procurement History File in Austin. Otherwise, create a simplified Purchase Card order.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Purchase Card Menu, select Process Purchase Card Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select Purchase Card Menu Option: Process Purchase Card Menu</p>
<p>New Simplified Purchase Card Order</p>
<p>Edit Simplified Purchase Card Order</p>
<p>New Detailed Purchase Card Order</p>
<p>Edit Detailed Purchase Card Order</p>
<p>Amendment To Purchase Card Order</p>
<p>Adjustment Voucher To Purchase Card Order</p>
<p>Receive Purchase Card Order</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Create P/C Order From Repetitive Item List</p>
<p>Convert P/C Order To 2237 Request</p>
<p>Convert P/C Order to a Delivery Order</p>
<p>Cancel An Incomplete PC Order</p>
<p>Convert Temporary 2237 to PC Request</p>
<p>Select Process Purchase Card Menu Option: New Detailed Purchase Card Order</p></td>
</tr>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a station number if prompted.
2.  Enter the purchase order number series. This will be a common number series already defined for use on Purchase card orders at your station. IFCAP will generate the next available purchase order number and prompt you, ‘Are you adding (PO \#) as a new Purchase Order Number?
3.  Enter a substation, if applicable.
4.  If you have more than one Purchase Card, enter the Purchase Card name you are using to purchase the items or services at the Purchase Card Name: prompt. The option is “case-sensitive”.
5.  Enter the date of the order at the P.O. Date: prompt.
6.  Enter N at the Estimated Order?: Answer Y if the quantity is estimated or the due to the service an exact price cannot be given at the time of the order.
7.  Enter the Source Code.
8.  Enter the vendor for the Purchase Card order at the PCDO Vendor: prompt
9.  Enter the Fund Control Point for the order at the FCP: prompt. IFCAP will use the information associated with the Purchase Card as the default value for this prompt. Make sure that you change the value if it is different from the default.
10. Enter the Cost Center. Cost centers allow Fiscal staff to create total expense records for a section or service. IFCAP will use the information associated with the Purchase Card as the default value for this prompt. Make sure that you change the value if it is different from the default.
11. Enter the Requesting Service. Enter the service that has requested the goods being ordered.
12. At the Classification of Request: prompt, create a classification name for the request if you like, or press \<Enter\> to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define.
13. Enter Y at the Receiving Required?: prompt if this Purchase Card order is for goods or services that have not yet been received, and you wish to record the receipt as part of the record. You will then be offered the Delivery Location: prompt. Enter the building, floor and/or room number the items are to be delivered to
14. Enter O for origin at the F.O.B. (Freight On Board) Point: prompt if additional freight charges are due to the carrier at the time of delivery. Enter D for destination if no additional freight charges are due at time of delivery.
15. Enter the date that the purchase is due at the Delivery Date: prompt.
16. Enter the name of the vendor representative that quoted the purchase price at the Proposal: prompt, and the date of the quote or a quote number if they are available (for example, 'telephone quote IFVENDOR,ONE quote \#001 dated 3-10-95'). Enter the estimated shipping and handling charges.
17. If shipping and handling charges are entered you will have to enter a Shipping BOC as well.
18. Enter the line item number of the item you want to add to the Purchase Card order at the Select Line Item Number: prompt.
19. Enter the Item Master File number of the item if there is an Item Master File number associated with the item. If there is none, hit “ENTER”
20. Enter a description of the first item order at the Description: prompt. If you used an Item Master Number the description information will appear automatically.
21. Enter the quantity of the item to be ordered at the “Quantity”: prompt.
22. At the “Unit Of Purchase”: prompt, enter the unit used to buy the item, such as box, each, pound, etc.
23. Enter the unit cost of the item, not including delivery, at the Actual Unit Cost: prompt.
24. Enter the number of units per shipping package at the Packaging Multiple: prompt.
25. Enter the factor that you use to convert the packaging multiple to the unit of purchase at the Unit Conversion Factor: prompt.
26. At the Vendor Stock Number: prompt, enter the stock number supplied by the vendor for the item.
27. Enter the Federal Supply Classification (FSC) for an item, or the Product Service Code (PSC) for a service. IFCAP might display some additional prompts based on your entry.
28. At the Contract/BOA \#: prompt, enter a contract number if the purchase price and vendor is established by a purchasing contract with that vendor.
29. Enter the Budget Object Code classification for the item at the BOC: prompt. If you do not know the Budget Object Code, enter two question marks at the prompt and IFCAP will display the available Budget Object Codes.
30. Repeat steps 17 through 28 for each line item that you want to add.
31. Enter comments if you like.
32. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press \<Enter\>. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group.
33. Enter a Sub-Control Point if you are using that feature.
34. You may review the Purchase Card order if you like.
35. Enter your electronic signature code.
36. You may send the Purchase Card order to a printer if you like. IFCAP will display the cost of the request and the current Control Point balance.
37. Enter another purchase order number at the Purchase Order: prompt, or press \<Enter\> to return to the Purchase Card Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select Process Purchase Card Menu Option: NEW DETailed Purchase Card Order</p>
<p>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</p>
<p>ENTER A NEW PURCHASE ORDER NUMBER OR A COMMON NUMBERING SERIES</p>
<p>PURCHASE ORDER: 4E 999-4E PC AUTHORIZED BUYER</p>
<p>Are you adding '999-4E0296' as a new Purchase Order number ? Y (YES)</p>
<p>PURCHASE CARD NAME: EXNAME</p>
<p>P.O. DATE: JUN 28,2005// (JUN 28, 2005)</p>
<p>ESTIMATED ORDER?: N// NO</p>
<p>PCDO VENDOR: SAMPLE INTERNATIONAL SAMPLE INTERNATIONAL EDIPH:800 333-8828NO: 4</p>
<p>0179</p>
<p>ORD ADD:2424 WEST 23RD STREET FMS:AMER STERILIZER CO</p>
<p>VA CODE:250320960 FAX:</p>
<p>...OK? Yes// (Yes)</p>
<p>SOURCE CODE: B// 6 Fed.Supply Sched.or OGA Contracts</p>
<p>FCP: 256 MULTI-YEAR ONE Replace 0160B1 10 01EA 01EA44175</p>
<p>Enter a year in the following sequence of years.</p>
<p>...1998 2000 2002 2004 2006 2008 2010 ...</p>
<p>First Year of the Multi-Appropriation (36_/_0160): 2004//</p>
<p>COST CENTER: 805300// Medical Research Service</p>
<p>REQUESTING SERVICE: ENGINEERING</p>
<p>CLASSIFICATION OF REQUEST: SUPPLIES</p>
<p>RECEIVING REQUIRED?: N NO</p>
<p>F.O.B. POINT: DESTINATION// DESTINATION</p>
<p>DELIVERY DATE: JUL 8,2005// (JUL 08, 2005)</p>
<p>PROPOSAL: N/A//</p>
<p>EST. SHIPPING AND/OR HANDLING:</p>
<p>Select LINE ITEM NUMBER: 1</p>
<p>LINE ITEM NUMBER: 1//</p>
<p>ITEM MASTER FILE NO.: 14 BATTERY,ALK,AAA,1.5V NIF#12923 ..</p>
<p>DESCRIPTION:</p>
<p>BATTERY, ALKALINE, AAA SIZE, 1.5 VOLTS</p>
<p>Edit? NO//</p>
<p>QUANTITY: 12</p>
<p>UNIT OF PURCHASE: EA//</p>
<p>ACTUAL UNIT COST: $3.5000//</p>
<p>PACKAGING MULTIPLE: 12//</p>
<p>UNIT CONVERSION FACTOR: 1//</p>
<p>VENDOR STOCK NUMBER:</p>
<p>FSC/PSC: 6135//</p>
<p>CONTRACT/BOA #: 1234567//</p>
<p>BOC: 2660 Operating Supplies and Materials</p>
<p>2660 Operating Supplies and Materials</p>
<p>Select LINE ITEM NUMBER:</p>
<p>COMMENTS:</p>
<p>No existing text</p>
<p>Edit? NO//</p>
<p>SORT GROUP:</p>
<p>Select SUB-CONTROL POINT:</p>
<p>BUSINESS TYPE: 1 SMALL</p>
<p>ITEM: 1, AMOUNT: 42</p>
<p>Review Purchase Card Order ? YES// (YES)</p>
<p>PC ORDER: 999-4E0296 STATUS: Order Not Completely Prepared</p>
<p>M.O.P.: PURCHASE CARD LAST PARTIAL RECD.:</p>
<p>REQUESTING SERVICE: ENGINEERING</p>
<p>VENDOR: IFVENDOR ONE SHIP TO:</p>
<p>2424 WEST 23RD STREET V.A. Medical Center</p>
<p>VA</p>
<p>800 333-8828</p>
<p>ACCT # 883198</p>
<p>FMS Vendor Code: 250320960</p>
<p>*EDI ORDER* DO NOT MAIL</p>
<p>___________________________________________________________________</p>
<p>FOB POINT: DESTINATION |PROPOSAL: N/A |AUTHORITY:</p>
<p>COST CENTER: 805300 | |</p>
<p>TYPE: DELIVERY ORDER | |BUYER:</p>
<p>DELIVER ON/BEFORE 7/8/2005 |CONTRACT: | IFCAP USER ONE</p>
<p>DISCOUNT TERM: | 1234567 |DATE: 6/28/2005</p>
<p>APP: 364/50160-256 | |</p>
<p>| |TOTAL: 42.00</p>
<p>--------------------------------------------------------------------------------</p>
<p>ENTER '^' TO HALT:</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>--------------------------------------------------------------------------------</p>
<p>1 BATTERY, ALKALINE, AAA SIZE, 12 EA 3.50 42.00</p>
<p>1.5 VOLTS</p>
<p>NSN: 6135-01-296-1859</p>
<p>Items per EA: 12</p>
<p>BOC: 2660 CONTRACT: 1234567</p>
<p>END OF DISPLAY--PRESS RETURN OR ENTER '^' TO HALT:</p>
<p>* TAKE NOTE *</p>
<p>This order will not be sent via EDI.</p>
<p>To place a Purchase Card order via EDI please use the Purchasing Agent Menu.</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p>
<p>Print Purchase Card Order ? YES// n (NO)</p>
<p>Cost of this request: $42.00</p>
<p>Current Control Point Balance: $4497370.26</p>
<p>...now generating the PHA transaction</p></td>
</tr>
</tbody>
</table>

## Editing Purchase Card Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit, Amend, or Adjust Purchase Card Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three ways to change Purchase Card orders:

- Editing a Purchase Card order is changing the order *before* you certify the Purchase Card order with your electronic signature code.
- Amending a Purchase Card order is changing a Purchase Card order *after* you have certified the purchase order with your electronic signature code and prior to receipt of items/services. To amend a Purchase Card order, see section 9.2, Amendment to Purchase Card Order.
- Adjusting a Purchase Card order is decreasing the quantity received on a receiving report for a Purchase Card order. To adjust a Purchase Card order receiving report, see section 9.3, Adjustment Voucher to Purchase Card Order.

> **NOTE:** The options Amendment to Purchase Card Orders and Adjustment to purchase Card orders are explained in Chapter 9 as part of the Supplemental Purchase Card Options.

### Editing a Simplified Purchase Card Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Editing a Purchase Card order will allow you to change the order before you certify it with your electronic signature code. All previously entered data will appear as default data.

#### Menu Path

From the Purchase Card Menu, select Process Purchase Card Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select Purchase Card Menu Option: Process Purchase Card Menu</p>
<p>New Simplified Purchase Card Order</p>
<p>Edit Simplified Purchase Card Order</p>
<p>New Detailed Purchase Card Order</p>
<p>Edit Detailed Purchase Card Order</p>
<p>Amendment To Purchase Card Order</p>
<p>Adjustment Voucher To Purchase Card Order</p>
<p>Receive Purchase Card Order</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Create P/C Order From Repetitive Item List</p>
<p>Convert P/C Order To 2237 Request</p>
<p>Convert P/C Order to a Delivery Order</p>
<p>Cancel An Incomplete PC Order</p>
<p>Convert Temporary 2237 to PC Request</p>
<p>Select Process Purchase Card Menu Option: Edit Simplified Purchase Card Order</p></td>
</tr>
</tbody>
</table>

#### Prompts

Enter a station number if prompted. Enter the number of the purchase order or requisition associated with the Purchase Card order at the P.O./REQ.NO.: prompt. If your station has substations, IFCAP will prompt you for the substation for which you are ordering the items. You can enter a question mark at the Substation: prompt to see a list of available substations. Enter the Purchase Card name.

Enter the date of the order at the P.O. Date: prompt. Enter TODAY or a future date only.

Enter the vendor for the Purchase Card order at the PCDO Vendor: prompt. IFCAP will look for the Vendor in the Vendor File (440). If you are using a new vendor you may enter the word SIMPLIFIED at the vendor prompt: and then IFCAP will offer you the PCDO Vendor:: prompt again. You may enter a new vendor now.

Enter the Fund Control Point for the purchase at the FCP: prompt.

Enter the Cost Center. Cost centers allow Fiscal staff to create total expense records for a section or service.

At the Classification of Request: prompt, create a classification name for the request if you like, or press \<Enter\> to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define.

Enter the cost of the purchase at the Purchase Cost: prompt.

Edit the description of the purchase at the Description: prompt.

Enter the Budget Object Code classification for the item at the BOC: prompt. If you do not know the Budget Object Code, enter two question marks at the prompt and IFCAP will display the available Budget Object Codes.

Enter comments if you want to.

Enter a Sub-Control Point if you like.

If you enter Y at the Review Purchase Card Order?: prompt, IFCAP will display the Purchase Card order to your screen.

Enter your electronic signature code. You may print the Purchase Card order if you like. IFCAP will display the cost of the request and the current balance of the Control Point that will fund the Purchase Card order.

Enter the output device for the Purchase Card order. Enter another purchase order number or requisition number at the P.O./Req. No.: prompt, or press \<Enter\> to return to the Process Purchase Card Menu.

|                                                                                                                        |                                                                                                                                                                         |                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-purchase-card-user-s-guide/006.png) | *Note:* If the order is over \$2500.00 or is on a contract, you *cannot* use the Simplified Purchase Card option. You *must* use the Detailed Purchase Card option! | ![](ifcap-version-5-1-purchase-card-user-s-guide/007.png) |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</p>
<p>P.O./REQ.NO.:999-P05125 999-P05125 02-06-06 PC Order Not Completely Prepared</p>
<p>FCP: 911 $ 2500.00</p>
<p>PURCHASE CARD NAME: IFVENDOR,ONE// IFVENDOR,ONE</p>
<p>P.O. DATE: FEB 06, 2006// (FEB 06,2006)</p>
<p>PCDO VENDOR: IFVENDOR5,TEN IFVENDOR5,TEN PH: NO: 41360</p>
<p>ORD ADD: IFVENDOR5,TEN FMS:</p>
<p>CODE: FAX:</p>
<p>Business Type Undefined</p>
<p>...OK? Yes// (Yes)</p>
<p>FREE TEXT VENDOR: IFVENDOR,TWO//</p>
<p>FCP: 911 PROSTHETICS// Replace</p>
<p>COST CENTER: 827200//</p>
<p>CLASSIFICATION OF REQUEST:</p>
<p>PURCHASE COST: 2500//</p>
<p>DESCRIPTION:</p>
<p>PROSTHETIC LEFT LEG</p>
<p>Edit? NO//</p>
<p>BOC: 2692 Prosthetic Supplies Replace</p>
<p>2692 Prosthetic Supplies</p>
<p>COMMENTS:</p>
<p>Example of Simplified Order Replace</p>
<p>SORT GROUP:</p>
<p>Select SUB-CONTROL POINT:</p>
<p>Review Purchase Card Order ? YES// (YES)</p>
<p>PC ORDER: 999-P05125 STATUS: Order Not Completely Prepared</p>
<p>M.O.P.: PURCHASE CARD LAST PARTIAL RECD.:</p>
<p>REQUESTING SERVICE:</p>
<p>VENDOR: IFVENDOR,TWO SHIP TO: IFVENDOR5,TEN</p>
<p>V.A. Medical Center</p>
<p>670 SOMEWHERE Street, NW</p>
<p>ANYCITY, NM 99999</p>
<p>________________________________________________________________________________</p>
<p>FOB POINT: |PROPOSAL: |AUTHORITY:</p>
<p>COST CENTER: 82OO00 | |</p>
<p>TYPE: | |BUYER:</p>
<p>DELIVER ON/BEFORE |CONTRACT: | IFBUYER,ONE</p>
<p>DISCOUNT TERM: | |DATE: 2/6/2006</p>
<p>APP: 3600160-911 | |</p>
<p>| |TOTAL: 2500.00</p>
<p>--------------------------------------------------------------------------------</p>
<p>ENTER '^' TO HALT:</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>--------------------------------------------------------------------------------</p>
<p>&gt;PROSTHETIC LEFT LEG 2500.00</p>
<p>BOC: 2692</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p>
<p>Print Purchase Card Order ? YES// No</p>
<p>Cost of this request: $2500.00</p>
<p>Current Control Point Balance: $2098973.54</p></td>
</tr>
</tbody>
</table>

### Editing a Detailed Purchase Card Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Editing a Purchase Card order is changing the order before you certify the Purchase Card order with your electronic signature code. All previously entered data will appear as default values.

#### Menu Path

From the Purchase Card Menu, select Process Purchase Card Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select Purchase Card Menu Option: Process Purchase Card Menu</p>
<p>New Simplified Purchase Card Order</p>
<p>Edit Simplified Purchase Card Order</p>
<p>New Detailed Purchase Card Order</p>
<p>Edit Detailed Purchase Card Order</p>
<p>Amendment To Purchase Card Order</p>
<p>Adjustment Voucher To Purchase Card Order</p>
<p>Receive Purchase Card Order</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Create P/C Order From Repetitive Item List</p>
<p>Convert P/C Order To 2237 Request</p>
<p>Convert P/C Order to a Delivery Order</p>
<p>Cancel An Incomplete PC Order</p>
<p>Convert Temporary 2237 to PC Request</p>
<p>Select Process Purchase Card Menu Option: Edit Detailed Purchase Card Order</p></td>
</tr>
</tbody>
</table>

#### Prompts

|                                                                                                                      |                                                                                                                                      |                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-purchase-card-user-s-guide/008.png) | *Note:* Previously entered data will appear as a default value. Do you want this note remarks have been entered with both edits? | ![](ifcap-version-5-1-purchase-card-user-s-guide/009.png) |

1.  Enter a station number if prompted.
2.  Enter the number of the purchase order or requisition associated with the Purchase Card order at the P.O./REQ.NO.: prompt.
3.  You can enter a question mark at the Substation: prompt to see a list of available substations. (Only appears if site has invoked the sub-station functionality)
4.  Enter the Purchase Card name.
5.  Enter the date of the order at the P.O. Date: prompt.
6.  Enter N at the Estimated Order?: Answer Y if the quantity is estimated or due to the service an exact price cannot be given at the time of the order.
7.  Enter the vendor for the Purchase Card order at the PCDO Vendor: prompt.
8.  Enter the Fund Control Point for the purchase at the FCP: prompt.
9.  Enter the Cost Center. Cost centers allow Fiscal staff to create total expense records for a section or service.
10. Enter the service requesting the order at the Request for Service: prompt.
11. At the Classification of Request: prompt, enter a classification name for the request if you like, or press \<Enter\> to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define.
12. Enter Y at the Receiving Required?: prompt if this Purchase Card order is for goods or services that have not yet been received. Enter the Delivery Location at the Delivery Location: prompt,
13. Enter where you want the VENDOR to deliver the purchase at the Ship To: prompt.
14. Enter O for origin at the F.O.B. (Freight On Board) Point: prompt if additional freight charges are due to the carrier at the time of delivery.
15. Enter the date that the purchase is due at the Delivery Date: prompt.
16. \#17 should go in her per the caption??
17. Enter the estimated shipping and handling charges.
18. Enter the name of the vendor representative that quoted the purchase price at the Proposal: prompt, and the date of the quote or a quote number if they are available (for example, 'telephone quote IFVENDOR,FOUR quote \#001 dated 3-10-95').
19. Enter the line item number of the item you want to edit or add to the Purchase Card order at the Select Line Item Number: prompt.
20. Enter the Item Master File number of the item.
21. Enter a description of the item at the Description: prompt if you didn’t enter an Item Master File number.
22. Enter the number of units of purchase received at the Quantity: prompt.
23. At the Unit Of Purchase: prompt, enter the unit used to buy the item, such as box, each, pound, etc.
24. Enter the unit cost of the item, not including delivery, at the Actual Unit Cost: prompt.
25. Enter the number of units per shipping package at the Packaging Multiple: prompt.
26. Enter the factor that you use to convert the packaging multiple to the unit of purchase at the Unit Conversion Factor: prompt.
27. At the Vendor Stock Number: prompt, enter the stock number supplied by the vendor for the item.
28. Enter the Federal Supply Classification (FSC) for an item, or the Product Service Code (PSC) for a service. IFCAP might display some additional prompts based on your entry.
29. At the Contract: prompt, enter a contract number if the purchase price and vendor is established by a purchasing contract with that vendor.
30. Enter the Budget Object Code classification for the item at the BOC: prompt. If you do not know the Budget Object Code, enter two question marks at the prompt and IFCAP will display the available Budget Object Codes.
31. Repeat steps 18 through 28 for each item you want to edit.
32. Add comments if you like.
33. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press \<Enter\>. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group.
34. At the Select Sub-Control Point: prompt, you can associate this purchase with a category of purchases defined for the Fund Control Point. This allows you to group similar purchases together.
35. If you enter Y at the Review Purchase Card Order?: prompt, IFCAP will display the Purchase Card order to your screen.
36. Enter your electronic signature code.
37. You may print the Purchase Card order if you like. IFCAP will display the cost of the request and the balance of the Control Point that will fund the request. Other messages related to Inventory point due-ins and PHA transactions may appear.
38. Enter the output device for the Purchase Card order at the Queue On Device: prompt. IFCAP will print or display the Purchase Card order on the output device you selected.
39. Enter another purchase order number at the Purchase Order: prompt, or press \<Enter\> to return to the Process Purchase Card

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>P.O./REQ.NO.: 999-4E0300 999-4E0300 02-06-06 PC Order Not Completely Prepar</p>
<p>ed FCP: 256 $ 42.00</p>
<p>PURCHASE CARD NAME: EXNAME// EXNAME</p>
<p>P.O. DATE: JUN 28,2005//</p>
<p>ESTIMATED ORDER?: N//</p>
<p>PCDO VENDOR: SAMPLE INTERNATIONAL//</p>
<p>SOURCE CODE: B//</p>
<p>FCP: 256 MULTI-YEAR ONE Replace</p>
<p>COST CENTER: 805300//</p>
<p>REQUESTING SERVICE: ENGINEERING//</p>
<p>CLASSIFICATION OF REQUEST: SUPPLIES//</p>
<p>RECEIVING REQUIRED?: N//</p>
<p>F.O.B. POINT: DESTINATION//</p>
<p>DELIVERY DATE: JUL 8,2005//</p>
<p>PROPOSAL: N/A//</p>
<p>EST. SHIPPING AND/OR HANDLING:</p>
<p>Select LINE ITEM NUMBER: 1//</p>
<p>LINE ITEM NUMBER: 1//</p>
<p>ITEM MASTER FILE NO.: 14// ..</p>
<p>DESCRIPTION:</p>
<p>BATTERY, ALKALINE, AAA SIZE, 1.5 VOLTS</p>
<p>Edit? NO//</p>
<p>QUANTITY: 12//</p>
<p>UNIT OF PURCHASE: EA//</p>
<p>ACTUAL UNIT COST: $3.5000//</p>
<p>PACKAGING MULTIPLE: 12//</p>
<p>UNIT CONVERSION FACTOR: 1//</p>
<p>VENDOR STOCK NUMBER:</p>
<p>FSC/PSC: 6135//</p>
<p>CONTRACT/BOA #: 1234567//</p>
<p>BOC: 2660 Operating Supplies and Materials Replace</p>
<p>Select LINE ITEM NUMBER:</p>
<p>COMMENTS:</p>
<p>No existing text</p>
<p>Edit? NO//</p>
<p>SORT GROUP:</p>
<p>Select SUB-CONTROL POINT:</p>
<p>BUSINESS TYPE: 1 SMALL</p>
<p>ITEM: 1, AMOUNT: 42</p>
<p>Review Purchase Card Order ? YES// (YES)</p>
<p>PC ORDER: 999-4E0296 STATUS: Order Not Completely Prepared</p>
<p>M.O.P.: PURCHASE CARD LAST PARTIAL RECD.:</p>
<p>REQUESTING SERVICE: ENGINEERING</p>
<p>VENDOR: IFVENDOR ONE SHIP TO:</p>
<p>2424 WEST 23RD STREET V.A. Medical Center</p>
<p>VA</p>
<p>800 333-8828</p>
<p>ACCT # 883198</p>
<p>FMS Vendor Code: 250320960</p>
<p>*EDI ORDER* DO NOT MAIL</p>
<p>___________________________________________________________________</p>
<p>FOB POINT: DESTINATION |PROPOSAL: N/A |AUTHORITY:</p>
<p>COST CENTER: 805300 | |</p>
<p>TYPE: DELIVERY ORDER | |BUYER:</p>
<p>DELIVER ON/BEFORE 7/8/2005 |CONTRACT: | IFCAP USER ONE</p>
<p>DISCOUNT TERM: | 1234567 |DATE: 6/28/2005</p>
<p>APP: 364/50160-256 | |</p>
<p>| |TOTAL: 42.00</p>
<p>--------------------------------------------------------------------------------</p>
<p>ENTER '^' TO HALT:</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>--------------------------------------------------------------------------------</p>
<p>1 BATTERY, ALKALINE, AAA SIZE, 12 EA 3.50 42.00</p>
<p>1.5 VOLTS</p>
<p>NSN: 6135-01-296-1859</p>
<p>Items per EA: 12</p>
<p>BOC: 2660 CONTRACT: 1234567</p>
<p>END OF DISPLAY--PRESS RETURN OR ENTER '^' TO HALT:</p>
<p>* TAKE NOTE *</p>
<p>This order will not be sent via EDI.</p>
<p>To place a Purchase Card order via EDI please use the Purchasing Agent Menu.</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p>
<p>Print Purchase Card Order ? YES// n (NO)</p>
<p>Cost of this request: $42.00</p>
<p>Current Control Point Balance: $4497370.26</p>
<p>...now generating the PHA transaction</p></td>
</tr>
</tbody>
</table>

# Create and Convert Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purchase Card orders may be generated from other IFCAP documents. For example, you may convert a *Repetitive Item List* (RIL) or *Temporary Transaction* into a Purchase Card order. A Purchase Card order may be converted back into a 2237 or Delivery Order if it is determined a Purchase Card order is not appropriate.

## Create a PC order from a RIL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user may create a Purchase Card order from an existing RIL.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select Purchase Card Menu Option: PROCess Purchase Card Menu</p>
<p>SPO New Simplified Purchase Card Order</p>
<p>ES Edit Simplified Purchase Card Order</p>
<p>DPO New Detailed Purchase Card Order</p>
<p>EDO Edit Detailed Purchase Card Order</p>
<p>Amendment To Purchase Card Order</p>
<p>Adjustment Voucher To Purchase Card Order</p>
<p>Receive Purchase Card Order</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Create P/C Order From Repetitive Item List</p>
<p>Convert P/C Order To 2237 Request</p>
<p>Convert P/C Order to a Delivery Order</p>
<p>Cancel An Incomplete PC Order</p>
<p>Convert Temporary 2237 to PC Request</p>
<p>Select Process Purchase Card Menu Option: CREATE P/C Order From Repetitive Item List</p></td>
</tr>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                      |                                                                     |                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-purchase-card-user-s-guide/010.png) | *Note:* Data entered on the RIL will appear as a default value. | ![](ifcap-version-5-1-purchase-card-user-s-guide/011.png) |

1.  Select a RIL. If you don’t know the RIL number, enter a question mark (?) to generate a list of RILs. All the information on the RIL will be displayed as a default value during the edit of the Purchase Card order. You may change these default data values if necessary.
2.  Enter the common number series that is used for Purchase Card orders at the P.O./REQ.NO.: prompt.
3.  Enter the Purchase Card name.
4.  Enter the date of the order at the P.O. Date: prompt.
5.  Enter N at the Estimated Order?: Answer Y if the quantity is estimated or due to the service an exact price cannot be given at the time of the order.
6.  Enter the vendor for the Purchase Card order at the PCDO Vendor: prompt.
7.  Enter the Fund Control Point for the purchase at the FCP: prompt.
8.  Enter the Cost Center. Cost centers allow Fiscal staff to create total expense records for a section or service.
9.  Enter the service requesting the order at the Request for Service: prompt.
10. At the Classification of Request: prompt, enter a classification name for the request if you like, or press \<Enter\> to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define.
11. Enter Y at the Receiving Required?: prompt if this Purchase Card order is for goods or services that have not yet been received. Enter the Delivery Location at the Delivery Location: prompt.
12. Enter where you want the VENDOR to deliver the purchase at the Ship To: prompt.
13. Enter O for origin at the F.O.B. (Freight On Board) Point: prompt if additional freight charges are due to the carrier at the time of delivery.
14. Enter the date that the purchase is due at the Delivery Date: prompt.
15. Enter the name of the vendor representative that quoted the purchase price at the Proposal: prompt, and the date of the quote or a quote number is they are available.
16. Enter the estimated shipping and handling charges
17. Enter the line item number of the item you want to edit or add to the Purchase Card order at the Select Line Item Number: prompt.
18. Enter the Item Master File number of the item.
19. Enter a description of the item at the Description: prompt if you didn’t enter an Item Master File number.
20. Enter the number of units of purchase received at the Quantity: prompt.
21. At the Unit Of Purchase: prompt, enter the unit used to buy the item, such as box, each, pound, etc.
22. Enter the unit cost of the item, not including delivery, at the Actual Unit Cost: prompt.
23. Enter the number of units per shipping package at the Packaging Multiple: prompt.
24. Enter the factor that you use to convert the packaging multiple to the unit of purchase at the Unit Conversion Factor: prompt.
25. At the Vendor Stock Number: prompt, enter the stock number supplied by the vendor for the item.
26. Enter the Federal Supply Classification (FSC) for an item, or the Product Service Code (PSC) for a service. IFCAP might display some additional prompts based on your entry.
27. At the Contract: prompt, enter a contract number if the purchase price and vendor is established by a purchasing contract with that vendor.
28. Enter the Budget Object Code classification for the item at the BOC: prompt. If you do not know the Budget Object Code, enter two question marks at the prompt and IFCAP will display the available Budget Object Codes.
29. Repeat steps 18 through 28 for each item you want to edit.
30. Add comments if you like.
31. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press \<Enter\>.
32. At the Select Sub-Control Point: prompt, you can associate this purchase with a category of purchases defined for the Fund Control Point. This allows you to group similar purchases together.
33. Enter another purchase order number at the Purchase Order: prompt, or press \<Enter\> to return to the Process Purchase Card Menu, Select Process Purchase Card Menu Option: EDIT Detailed Purchase Card Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select Process Purchase Card Menu Option: CREATE P/C Order From Repetitive Item List</p>
<p>Select REPETITIVE ITEM LIST ENTRY NUMBER: ?</p>
<p>Answer with REPETITIVE ITEM LIST ENTRY NUMBER</p>
<p>Do you want the entire REPETITIVE ITEM LIST List? Y (Yes)</p>
<p>Choose from:</p>
<p>999-00-3-911-827200-0001 04-06-00 # OF ITEMS: 1 TOTAL COST: 4.40</p>
<p>999-00-3-111-824200-0001 04-13-00 # OF ITEMS: 6 TOTAL COST: 3885.26</p>
<p>^</p>
<p>Select REPETITIVE ITEM LIST ENTRY NUMBER: 999-00-3-111-824200-0001 04-13-00</p>
<p># OF ITEMS: 6TOTAL COST: 3885.26</p>
<p>This repetitive item list has the following vendors:</p>
<p>IFVENDOR,SIX</p>
<p>IFVENDOR,SEVEN</p>
<p>IFVENDOR,THREE</p>
<p>ENTER A NEW PURCHASE ORDER NUMBER OR A COMMON NUMBERING SERIES</p>
<p>PURCHASE ORDER: P05 999-P05 PC AUTHORIZED BUYER</p>
<p>Are you adding '999-P05173' as a new Purchase Order number ? Y (YES)</p>
<p>Edit request 999-P05173? Yes// (Yes)</p>
<p>PURCHASE CARD NAME: IFVENDOR,EIGHT IFVENDOR,EIGHT</p>
<p>P.O. DATE: APR 26,2000//</p>
<p>ESTIMATED ORDER?: N// Y YES</p>
<p>PCDO VENDOR: IFVENDOR,SIX//</p>
<p>FCP: 111 REHAB //</p>
<p>COST CENTER: 824444//</p>
<p>REQUESTING SERVICE: IFVENDOR,EIGHT</p>
<p>CLASSIFICATION OF REQUEST:</p>
<p>RECEIVING REQUIRED?: Y YES</p>
<p>DELIVERY LOCATION: BDL3//</p>
<p>SHIP TO: ANYCITY VAMC//</p>
<p>F.O.B. POINT: DESTINATION// DESTINATION</p>
<p>DELIVERY DATE: TODAY+10// (MAY 06, 2000)</p>
<p>PROPOSAL: N/A//</p>
<p>EST. SHIPPING AND/OR HANDLING:</p>
<p>Select LINE ITEM NUMBER: 1//</p>
<p>LINE ITEM NUMBER: 1//</p>
<p>ITEM MASTER FILE NO.: 171// ..</p>
<p>DESCRIPTION:</p>
<p>1&gt; PENCILS</p>
<p>EDIT Option:</p>
<p>QUANTITY: 2//</p>
<p>UNIT OF PURCHASE: CS//</p>
<p>ACTUAL UNIT COST: $12.0000//</p>
<p>PACKAGING MULTIPLE: 144//</p>
<p>UNIT CONVERSION FACTOR: 144//</p>
<p>VENDOR STOCK NUMBER:</p>
<p>FSC/PSC: 7510//</p>
<p>CONTRACT/BOA #:</p>
<p>BOC: 2620 Office Supplies Replace</p>
<p>Select LINE ITEM NUMBER:</p>
<p>COMMENTS:</p>
<p>1&gt;</p>
<p>SORT GROUP:</p>
<p>Select SUB-CONTROL POINT:</p></td>
</tr>
</tbody>
</table>

34. If you enter Y at the Review Purchase Card Order?: prompt, IFCAP will display the Purchase Card order to your screen.
35. Enter your electronic signature code.
36. You may print the Purchase Card order if you like. IFCAP will display the cost of the request and the balance of the Control Point that will fund the request. Other messages related to Inventory point due-ins and PHA transactions may appear.
37. Enter the output device for the Purchase Card order at the Queue On Device: prompt. IFCAP will print or display the Purchase Card order on the output device you selected.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Review Purchase Card Order ? YES// (YES)</p>
<p>PC ORDER: 999-P05173 STATUS: Order Not Completely Prepared</p>
<p>M.O.P.: PURCHASE CARD LAST PARTIAL RECD.:</p>
<p>REQUESTING SERVICE: IFVENDOR,EIGHT</p>
<p>VENDOR: IFVENDOR,SIX SHIP TO: ANYCITY VAMC</p>
<p>1000 S BOULEVARD V.A. Medical Center</p>
<p>SUITE 1000 670 SOMEWHERE Street, NW</p>
<p>ROOM 100, POD 12 ANYCITY, NM 99999</p>
<p>ANYTOWN, GA 00001</p>
<p>555-333-8838</p>
<p>FMS Vendor Code: 93086711305</p>
<p>DELIVERY LOCATION: BDL3</p>
<p>________________________________________________________________________________</p>
<p>FOB POINT: DESTINATION |PROPOSAL: N/A |AUTHORITY:</p>
<p>COST CENTER: 830000 | |</p>
<p>TYPE: | |BUYER:</p>
<p>DELIVER ON/BEFORE 5/6/2000 |CONTRACT: | IFBUYER,TWO</p>
<p>IFBUYER,TWO</p>
<p>DISCOUNT TERM: | |DATE: 4/26/2000</p>
<p>APP: 3600160-911 | |ESTIMATED</p>
<p>| |TOTAL: 24.00</p>
<p>----------------------------------------------------------------------------</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>--------------------------------------------------------------------------------</p>
<p>1 PENCILS 2 CS 12.00 24.00</p>
<p>NSN: 7510-01-432-4333</p>
<p>Items per CS: 144</p>
<p>BOC: 2620</p>
<p>* ESTIMATED PURCHASE ORDER *</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p>
<p>Print Purchase Card Order ? YES// (YES)</p>
<p>Cost of this request: $24.00</p>
<p>Current Control Point Balance: $1499759.20</p>
<p>incrementing due-ins in inventory point: SPD</p>
<p>...now generating the PHA transaction</p>
<p>...checking on due-ins at inventory point(s)...</p>
<p>QUEUE ON DEVICE: SFCS6$PRT-10/6/UP SF CIOFO</p>
<p>Requested Start Time: NOW// (APR 26, 2000@13:16:32)</p>
<p>Request 999-P05173 has been created.</p>
<p>The vendor for this request is: IFVENDOR,SIX</p>
<p>Total cost of request: $24.00</p>
<p>Total items on Purchase Card request: 1</p></td>
</tr>
</tbody>
</table>

## Convert Temporary 2237 to PC Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select Purchase Card Menu Option: Process Purchase Card Menu</p>
<p>SPO New Simplified Purchase Card Order</p>
<p>ES Edit Simplified Purchase Card Order</p>
<p>DPO New Detailed Purchase Card Order</p>
<p>EDO Edit Detailed Purchase Card Order</p>
<p>Amendment To Purchase Card Order</p>
<p>Adjustment Voucher To Purchase Card Order</p>
<p>Receive Purchase Card Order</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Create P/C Order From Repetitive Item List</p>
<p>Convert P/C Order To 2237 Request</p>
<p>Convert P/C Order to a Delivery Order</p>
<p>Cancel An Incomplete PC Order</p>
<p>Convert Temporary 2237 to PC Request</p>
<p>Select Purchase Card Menu Option: Convert Temporary 2237 to PC Request</p></td>
</tr>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter the station number if prompted.
2.  Enter an appropriate control Point. Enter a “?” to see a list of choices.
3.  If the control point has more than one Inventory Point attached to it, the user will be asked to select the appropriate Inventory Point for the order. If no Inventory Point is appropriate hit \<Enter\> key.
4.  Select the Temporary transaction you wish to convert.
5.  The user may display the temporary request for review by answering Yes at the “Would you like to review this request?: prompt.
6.  Enter NO at the Print administrative certification page of 2237?: prompt. (NOTE: the user is not given an opportunity to enter any administrative certifications on the 2237).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select STATION NUMBER: 999</p>
<p>Select CONTROL POINT: 036 SUPPLY SPD 1060</p>
<p>1) 999-SPD</p>
<p>2) 999-IFCAPTWO</p>
<p>3) 999-IFCAPTHREE</p>
<p>Select INVENTORY POINT: (1-3): 1 999-SPD</p>
<p>Select the existing transaction number to be converted</p>
<p>Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: IFVENDOR,onespd</p>
<p>OBL IFVENDOR,THREE</p>
<p>WIDGETS</p>
<p>Would you like to review this request? No// Y</p>
<p>Print administrative certification page of 2237? Yes// N (No)</p>
<p>DEVICE: HOME// UCX/TELNET Right Margin: 80//</p></td>
</tr>
<tr class="even">
<td><p>MAY 01, 2000@14:01:07 IFVENDOR,ONESPD</p>
<p>----------------------------------------------------------------------</p>
<p>REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES</p>
<p>----------------------------------------------------------------------</p>
<p>TO: A&amp;MM Officer Requesting Office</p>
<p>ACQUISITION &amp; MATERIAL MGMT (90)</p>
<p>----------------------- ----------------------------------------------</p>
<p>Action Requested Date Prepared Date Required</p>
<p>Delivery MAY 01, 2000 MAY 05, 2000</p>
<p>----------------------- --------------------- -----------------------</p>
<p>ITEM NO. DESCRIPTION QUANTITY UNIT ESTIMATED</p>
<p>OR STOCK NO. UNIT COST</p>
<p>----------------------------------------------------------------------</p>
<p>8766 1 ITEM ID NO. 12001 WOODEN</p>
<p>WIDGETS-PINE-PAINTED</p>
<p>(NSN: 7510-87-228-2816) PKG: 1 per EA</p>
<p>(CONTRACT # GS-98-99827F, EXPIRATION</p>
<p>DATE: SEP 30,2009) 12 EA 2.3000</p>
<p>TOTAL COST: $27.60</p>
<p>----------------------------------------------------------------------</p>
<p>Press return to continue, uparrow (^) to exit:</p>
<p>IFVENDOR,ONESPD</p>
<p>-----------------------------------------------------------------------</p>
<p>REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES</p>
<p>----------------------------------------------------------------------</p>
<p>VENDOR INFORMATION: NO: 41369 FAX: 555-222-3711/DEF</p>
<p>VENDOR: IFVENDOR,THREE CONTACT: IFBUYER,THREE</p>
<p>777 EXAMPLE RD PHONE: 555-666-2625</p>
<p>ANYTOWN,MA 00001</p>
<p>---------------------------------------------------------------------</p>
<p>Ref. Voucher Number:</p>
<p>DELIVER TO: BDL2</p>
<p>--------------------------------------------------------------------</p>
<p>JUSTIFICATION OF NEED OR TURN-IN</p>
<p>Needed for stock</p>
<p>---------------------------------------------------------------------</p>
<p>Originator of Request: IFBUYER,TWO</p>
<p>Signature of Initiator Signature of Approving Official Date</p>
<p>IFBUYER,TWO</p>
<p>IFBUYER,FOUR</p>
<p>------------------------------------ --------------------------------</p>
<p>Press return to continue, uparrow (^) to exit:</p>
<p>IFVENDOR,ONESPD</p>
<p>-----------------------------------------------------------------------</p>
<p>REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES</p>
<p>----------------------------------------------------------------------</p>
<p>Appropriation and Accounting Symbols</p>
<p>999-3601060-036-828100-2660</p>
<p>----------------------------------------------------------------------</p>
<p>Press return to continue:</p></td>
</tr>
</tbody>
</table>

7.  Enter the information for the new transaction number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select STATION NUMBER: 999//</p>
<p>Select FISCAL YEAR: 00//</p>
<p>Select QUARTER: 3//</p>
<p>Select CONTROL POINT: 036 SUPPLY SPD 1060 1060</p>
<p>Transaction 'IFVENDOR,ONESPD' has been replaced by 999-00-3-036-0027</p></td>
</tr>
</tbody>
</table>

8.  Build the Purchase Card Order by entering an appropriate common number series for the Purchase Card order.
9.  Enter Yes at the Edit Request: prompt. This will enable you to edit the various fields on the Purchase Card order. This process is the same as the EDIT process shown earlier. See Edit a Detailed Purchase Card Order.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>ENTER A NEW PURCHASE ORDER NUMBER OR A COMMON NUMBERING SERIES</p>
<p>PURCHASE ORDER: P05 999-P05 PC AUTHORIZED BUYER</p>
<p>Are you adding '999-P05176' as a new Purchase Order number ? Y (YES) 1060</p>
<p>Edit request 999-P05176? Yes// (Yes)</p>
<p>PURCHASE CARD NAME: IFVENDOR,THREE IFVENDOR,THREE</p>
<p>P.O. DATE: MAY 1,2000//</p>
<p>ESTIMATED ORDER?: N// NO</p>
<p>PCDO VENDOR: IFVENDOR,THREE //</p>
<p>FCP: 036 SUPPLY SPD//</p>
<p>COST CENTER: 820000//</p>
<p>REQUESTING SERVICE: SURGERY</p>
<p>CLASSIFICATION OF REQUEST:</p>
<p>RECEIVING REQUIRED?: Y YES</p>
<p>DELIVERY LOCATION: BLD8//</p>
<p>SHIP TO: ANYCITY VAMC//</p>
<p>F.O.B. POINT: DESTINATION// DESTINATION</p>
<p>DELIVERY DATE: TODAY+10// (MAY 11, 2000)</p>
<p>PROPOSAL: N/A// IFBUYER,FIVE 555-777-9889</p>
<p>EST. SHIPPING AND/OR HANDLING:</p>
<p>Select LINE ITEM NUMBER: 1//</p>
<p>LINE ITEM NUMBER: 1//</p>
<p>ITEM MASTER FILE NO.: 12001// ..</p>
<p>DESCRIPTION:</p>
<p>1&gt; WOODEN WIDGETS-PINE-PAINTED</p>
<p>EDIT Option:</p>
<p>Minimum Order Qty.: 1</p>
<p>Maximum Order Qty.: 100</p>
<p>QUANTITY: 12//</p>
<p>UNIT OF PURCHASE: EA//</p>
<p>ACTUAL UNIT COST: $2.3000//</p>
<p>PACKAGING MULTIPLE: 1//</p>
<p>UNIT CONVERSION FACTOR: 1//</p>
<p>VENDOR STOCK NUMBER: 8766//</p>
<p>FSC/PSC: 2310//</p>
<p>CONTRACT/BOA #: GS-98-99827F//</p>
<p>BOC: 2660 Operating Supplies and Ma Replace</p>
<p>Select LINE ITEM NUMBER:</p>
<p>COMMENTS:</p>
<p>1&gt;</p>
<p>1) 999-SPD</p>
<p>2) 999-IFCAPTWO</p>
<p>3) 999-IFCAPTHREE</p>
<p>Select INVENTORY POINT: (1-3): 1 999-SPD</p>
<p>SORT GROUP:</p>
<p>Select SUB-CONTROL POINT:</p></td>
</tr>
</tbody>
</table>

10. The Purchase Card Order May be Displayed

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Review Purchase Card Order ? YES// (YES)</p>
<p>PC ORDER: 999-P05176 STATUS: Order Not Completely Prepared</p>
<p>M.O.P.: PURCHASE CARD LAST PARTIAL RECD.:</p>
<p>REQUESTING SERVICE: SURGERY</p>
<p>VENDOR: IFVENDOR,THREE SHIP TO: ANYCITY VAMC</p>
<p>777 EXAMPLE RD V.A. Medical Center</p>
<p>ANYTOWN, MA 01111 670 SOMEWHERE Street, NW</p>
<p>555-222-2625 ANYCITY, NM 99999</p>
<p>FMS Vendor Code: 98722987301</p>
<p>DELIVERY LOCATION: BLD8</p>
<p>_____________________________________________________________________</p>
<p>FOB POINT: DESTINATION |PROPOSAL: IFBUYER,FIVE |AUTHORITY:</p>
<p>COST CENTER: 820000 | 555-777-9889 |</p>
<p>TYPE: | |BUYER:</p>
<p>DELIVER ON/BEFORE 5/11/2000 |CONTRACT: | IFBUYER,TWO</p>
<p>IFBUYER,TWO</p>
<p>DISCOUNT TERM: | GS-98-99827F |DATE: 5/1/2000</p>
<p>APP: 3601060-036 | |</p>
<p>| |TOTAL: 27.60</p>
<p>----------------------------------------------------------------------</p>
<p>ENTER '^' TO HALT:</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>-----------------------------------------------------------------------</p>
<p>1 WOODEN WIDGETS-PINE-PAINTED 12 EA 2.30 27.60</p>
<p>STK#: 8766</p>
<p>NSN: 7510-87-228-2816</p>
<p>Items per EA: 1</p>
<p>BOC: 2660 CONTRACT: GS-98-99827F</p>
<p>END OF DISPLAY--PRESS RETURN OR ENTER '^' TO HALT:</p></td>
</tr>
</tbody>
</table>

11. The user must enter their Electronic Signature Code to complete the order.
12. The order may be directed to a printer.
13. A series of messages will display on the screen as the system completes the document.
14. If you elected to print the document you will be asked for a DEVICE and a starting time.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Enter ELECTRONIC SIGNATURE CODE: Thank you.</strong></p>
<p><strong>Print Purchase Card Order ? YES// (YES)</strong></p>
<p><strong>Cost of this request: $27.60</strong></p>
<p><strong>Current Control Point Balance: $1019972.40</strong></p>
<p><strong>incrementing due-ins in inventory point: SPD</strong></p>
<p><strong>...now generating the PHA transaction</strong></p>
<p><strong>...checking on due-ins at inventory point(s)...</strong></p>
<p><strong>QUEUE ON DEVICE: ISC A103-10/6/UP RECEPTIONIST LASER PRINTER [Out of Service]</strong></p>
<p><strong>QUEUE ON DEVICE: &lt;ENTER A DEVICE&gt;</strong></p>
<p><strong>Requested Start Time: NOW// (MAY 01, 2000@14:03:29)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Convert PC Orders to Other Document Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purchase Card module permits a user to convert an Unsigned Purchase Card order to a 2237 or a delivery order which can then be processed utilizing the appropriate menu options for 2237’s and delivery orders.

## Convert a PC order to a 2237

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow the user to convert the “unsigned” Purchase Card order back into a 2237. This might be necessary if the Vendor will not accept a credit card, or the user has exceeded their Single or Monthly Purchase Limit. The use of this option will eliminate the need to reenter all the order data.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>SPO New Simplified Purchase Card Order</strong></p>
<p><strong>ES Edit Simplified Purchase Card Order</strong></p>
<p><strong>DPO New Detailed Purchase Card Order</strong></p>
<p><strong>EDO Edit Detailed Purchase Card Order</strong></p>
<p><strong>Amendment To Purchase Card Order</strong></p>
<p><strong>Adjustment Voucher To Purchase Card Order</strong></p>
<p><strong>Receive Purchase Card Order</strong></p>
<p><strong>Item Display</strong></p>
<p><strong>Vendor Display</strong></p>
<p><strong>Create P/C Order From Repetitive Item List</strong></p>
<p><strong>REQ Convert P/C Order To 2237 Request</strong></p>
<p><strong>DEL Convert P/C Order to a Delivery Order</strong></p>
<p><strong>Cancel An Incomplete PC Order</strong></p>
<p><strong>TEMP Convert Temporary 2237 to PC Request</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select Process Purchase Card Menu Option: DEL Convert P/C Order to 2237 Request</td>
</tr>
</tbody>
</table>

### Display of Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Process Purchase Card Menu Option: REQ Convert P/C Order To 2237 Request</strong></p>
<p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>P.O./REQ. NO.: P05177 999-P05177 05-01-00 PC Order Not Completely Prepared</strong></p>
<p><strong>FCP: 110 $ 4.50 $ 4.50 $ 4.50</strong></p>
<p><strong>Use transaction 999-00-3-110-0106 to access this record from your fund control point.</strong></p>
<p><strong>Conversion completed.</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** Use the Control Point options to edit and complete the 2237.

## Convert a 2237 to a Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow the user to convert the “unsigned” Purchase Card order into a Delivery Order. This might be necessary if the Vendor will not accept a credit card, or the user has exceeded their Single or Monthly Purchase Limit and the items you are ordering are under contract. The use of this option will eliminate the need to reenter all the order data.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>SPO New Simplified Purchase Card Order</strong></p>
<p><strong>ES Edit Simplified Purchase Card Order</strong></p>
<p><strong>DPO New Detailed Purchase Card Order</strong></p>
<p><strong>EDO Edit Detailed Purchase Card Order</strong></p>
<p><strong>Amendment To Purchase Card Order</strong></p>
<p><strong>Adjustment Voucher To Purchase Card Order</strong></p>
<p><strong>Receive Purchase Card Order</strong></p>
<p><strong>Item Display</strong></p>
<p><strong>Vendor Display</strong></p>
<p><strong>Create P/C Order From Repetitive Item List</strong></p>
<p><strong>REQ Convert P/C Order To 2237 Request</strong></p>
<p><strong>DEL Convert P/C Order to a Delivery Order</strong></p>
<p><strong>Cancel An Incomplete PC Order</strong></p>
<p><strong>TEMP Convert Temporary 2237 to PC Request</strong></p>
<p><strong>Select Process Purchase Card Menu Option: DEL Convert P/C Order to a Delivery Order</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Display the Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>Select PURCHASE CARD ORDER NUMBER: P05178 999-P05178 05-01-00 PC Order Not Completely Prepared</strong></p>
<p><strong>FCP: 110 $ 31.92</strong></p>
<p><strong>ENTER A NEW DELIVERY ORDER NUMBER OR A COMMON NUMBERING SERIES</strong></p>
<p><strong>DELIVERY ORDER: U0 999-U0 DO AUTHORIZED BUYER</strong></p>
<p><strong>Are you adding '999-U00037' as a new Purchase Order number ? Y (YES)</strong></p>
<p><strong>This Purchase Card order has now been converted to a delivery order.</strong></p>
<p><strong>The Purchase Card Order No: P05178 has been converted to Delivery Order No: U00037</strong></p>
<p><strong>This delivery order must be edited.</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** Use the Delivery Orders module to edit and complete the order.

# # Record Receipt of a PC Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “Receive Purchase Card Order” option allows individuals with Purchase Card authority to receive goods within their area. The option is similar to the current Warehouse Receiving option but is limited to PURCHASE CARD orders that the user has set up for DIRECT delivery. The warehouse staff will record the receipt of items delivered to them using existing options in the Warehouse Menu. The Receive Purchase Card Order option also allows the user to update the due-ins in the Inventory Package thus eliminating the need to receive twice (once in the Purchase Card program and once in the Inventory Program). If the order is received in the warehouse, the warehouse will utilize their Warehouse Receiving option to receive the goods; however, there would still be a need for the authorized buyer to receive the goods into the Inventory Package. It will not be necessary for the approving official to "sign off" at the receiving process. The approving official will "approve" through the reconciliation process. There will be the capability to process partials on Purchase Card orders. If a partial is processed, the status will be updated to Partial Order Received. If the order is received as complete, the status of the order will be updated to Complete Order Received. There will be no receiving document printed in Fiscal and no FMS document created and transmitted to Austin.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process Purchase Card Menu from the Purchase Card Menu.

Select Receive Purchase Card Order from the Process Purchase Card Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Menu Option: Process Purchase Card Menu</strong></p>
<p><strong>New Simplified Purchase Card Order</strong></p>
<p><strong>Edit Simplified Purchase Card Order</strong></p>
<p><strong>New Detailed Purchase Card Order</strong></p>
<p><strong>Edit Detailed Purchase Card Order</strong></p>
<p><strong>Amendment To Purchase Card Order</strong></p>
<p><strong>Adjustment Voucher To Purchase Card Order</strong></p>
<p><strong>Receive Purchase Card Order</strong></p>
<p><strong>Item Display</strong></p>
<p><strong>Vendor Display</strong></p>
<p><strong>Create P/C Order From Repetitive Item List</strong></p>
<p><strong>Convert P/C Order To 2237 Request</strong></p>
<p><strong>Convert P/C Order to a Delivery Order</strong></p>
<p><strong>Cancel An Incomplete PC Order</strong></p>
<p><strong>Select Process Purchase Card Menu Option: Receive Purchase Card Order</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a Purchase Card order number.
2.  You can review the Purchase Card order if you like.
3.  Enter the date you received the goods at the Date Received: prompt.
4.  Enter the line item number for the items at the Line Item: prompt.
5.  Enter the quantity that you are receiving.
6.  Repeat steps 4 and 5 to enter additional line items.
7.  IFCAP will display the receiving report.
8.  You can approve the Receiving Report by entering a Yes at the prompt and by then entering your electronic signature code. If the item is part of the Inventory Point attached to the order, the GIP Receipt screen will open and the item may be received into the Inventory.
9.  If you choose to print an additional copy of the receiving report enter a device at the prompt.
10. Enter another Purchase Card order at the Purchase Card Order: prompt, or press \<Enter\> to return to the Process Purchase Card Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>PURCHASE ORDER: 658-P65138 07-31-96 PC Ordered (No Fiscal Action Required</strong></p>
<p><strong>FCP: 036 $ 565.60 IFVENDOR,NINE</strong></p>
<p><strong>I N V E N T O R Y version 5.0</strong></p>
<p><strong>(658) Primary Inventory Point: SPD IFBUYER,SIX</strong></p>
<p><strong>PA/PPM/AUTHORIZED BUYER: IFBUYER,SIX</strong></p>
<p><strong>REVIEW PURCHASE ORDER? NO// (NO)</strong></p>
<p><strong>DATE RECEIVED: TODAY// (OCT 03, 1996)</strong></p>
<p><strong>LINE ITEM: 1</strong></p>
<p><strong>Item: 1 1 CUTTER WIRE KIRSCHNER</strong></p>
<p><strong>STK#: 56-2507 NSN:</strong></p>
<p><strong>CUTTER WIRE KIRSCHNER</strong></p>
<p><strong>UNIT OF PRCH: EA QTY ORDERED: 3 PREVIOUSLY RECEIVED: 0</strong></p>
<p><strong>QTY BEING RECEIVED: 2 AMOUNT: 246.40</strong></p>
<p><strong>LINE ITEM:</strong></p>
<p><strong>PURCHASE ORDER: 658-P65138 STATUS: Ordered (No Fiscal Action Required)</strong></p>
<p><strong>PROCESSING: PURCHASE CARD PARTIAL: 1 10/3/96</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>UNIT QTY TOTAL</strong></p>
<p><strong>ITEM DESCRIPTION QTY UNIT COST REC COST</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>1 CUTTER WIRE KIRSCHNER 3 EA 123.20 2 246.40</strong></p>
<p><strong>Total Amount: 246.40</strong></p>
<p><strong>Approve this receiving report ? YES// (YES)</strong></p>
<p><strong>Enter ELECTRONIC SIGNATURE CODE: Thank you.</strong></p>
<p><strong>DC Distribution Cost EE E/E Inventory Item RO Receive Order</strong></p>
<p><strong>Purchase Order Receipt Oct 03, 1996 11:15:11 Page: 1 of 1</strong></p>
<p><strong>INVENTORY: 658-SPD PO: 658-P65138 VENDOR: IFVENDOR,NINE#623</strong></p>
<p><strong>PARTIAL: 1 DATE: OCT 03, 1996 LINECNT: 1 TOTAL AMT: 246.4</strong></p>
<p><strong>LINE DESCRIPTION IM# POQTY CONV RECQTY AVGCOST UNITCOST TOTCOST</strong></p>
<p><strong>1 CUTTER-WIRE-KIRSCH 11965 2 1 2 0.00 123.20 246.40</strong></p>
<p><strong>Enter ?? for more actions</strong></p>
<p><strong>DC Distribution Cost EE E/E Inventory Item RO Receive Order</strong></p>
<p><strong>Select Item(s): Quit// QUIT</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Reconcile Payment Authorizations from FMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The Purchase Card Reconciliation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CitiBank transmits Purchase Card order transactions to the Credit Card System (CCS) at the Austin Finance Center (AFC). This computer updates its database and sends the payment transactions to FMS. The AFC system also transmits purchase date, amount and vendor information to IFCAP in a transaction called a CC document. FMS records the payment transactions and formats the transactions into F16 Transactions that FMS sends to IFCAP. IFCAP processes the F16 entry and posts it to the FMS transaction portion of the Running Balance. IFCAP stores the CC transactions from the CCS system in the Reconciliation File. Purchase Card Users reconcile the transaction records in the Reconciliation File with the Purchase Card orders they entered in IFCAP. If the accounting data differs, IFCAP will create an Expenditure Transfer (ET) document and transmit it to FMS to correct FMS Control Point records. IFCAP will also correct its own Control Point Records. IFCAP is presumed to have the correct set of accounting data.

> **NOTE:** You must reconcile your transaction records in a timely manner. When you go to your Purchase Card menu and you have payment documents to reconcile, a bulletin will appear stating “You have (number) transaction(s) to reconcile (date range).” The number states how many payment documents you have to reconcile and the date range states the range you will print in the Daily Purchase Card Charges Statement.

### Data Sharing for Reconciliation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reconciliation data will be transmitted from CitiBank into the Credit Card System (CCS) in Austin. This information includes: RETAIL ID; PURCHASE DATE; PURCHASE CARD NUMBER; DOLLAR AMOUNT and VENDOR NAME. The CCS database will create what is known as a CC# which begins with C. The next three digits are the station number, the next digit is the last digit of the calendar year, the next three digits are the Julian date, and the remaining digits are a sequential number. (Example: C61202630001) The CCS database will transmit this information to the FMS system, which will, in turn, generate an F16 document back to IFCAP. The CitiBank system will also send Credit Card Registration data through the CCS system to IFCAP. This data will update the Purchase Card Information File (440.5) in IFCAP.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Reconciliation Menu from the Purchase Card Menu. Select Reconciliation from the Reconciliation Menu. Select Reconciliation from the Purchase Card Menu. Enter a station number. At the Select Number: prompt, enter 1 for Auto if you want IFCAP to generate a list of all pending Oracle records for you to reconcile. Enter 2 for Manual if you want to choose specific Purchase Cards and payment documents. Enter 3 to reconcile by Purchase Card Order number.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Reports Menu ...</strong></p>
<p><strong>Approving Official Menu ...</strong></p>
<p><strong>Process Purchase Card Menu ...</strong></p>
<p><strong>Purchase Card Display/Print Menu ...</strong></p>
<p><strong>Reconciliation Menu ...</strong></p>
<p><strong>Select Purchase Card Menu Option: REConciliation Menu</strong></p>
<p><strong>Reconciliation</strong></p>
<p><strong>Edit/Remove Reconciliation</strong></p>
<p><strong>ET-FMS Document Display</strong></p>
<p><strong>Daily Purchase Card Charges Statement</strong></p>
<p><strong>You have PENDING ALERTS</strong></p>
<p><strong>Enter "VA VIEW ALERTS to review alerts</strong></p>
<p><strong>Select Reconciliation Menu Option: REConciliation</strong></p>
<p><strong>Select STATION NUMBER: 999</strong></p>
<p><strong>Select one of the following:</strong></p>
<p><strong>1 Auto Charge Selection</strong></p>
<p><strong>2 Manual Charge Selection</strong></p>
<p><strong>3 Reconcile by Purchase Card Order #</strong></p>
<p><strong>Select Number: 1 Auto Charge Selection</strong></p>
<p><strong>Reconcile for your own Purchase Card orders?</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Automatic Reconciliations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto Charge Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are an Approving Official for the service, IFCAP will ask you if you want to reconcile for your own Purchase Card orders. If you do, enter Yes. If you are the Approving Official for another Cardholder and you want to Reconcile orders for that person, enter No. You will then be asked to enter a Cardholder’s name. IFCAP will display the first payment document. The entry will show the Vendor Name, Purchase Date and Amount and *may* include the Purchase Order Number. If a match is found, the user will be prompted with the order and default of YES. If it is not the correct order, answer N and IFCAP will continue the matching process.

IFCAP will then begin a matching process. IFCAP will attempt to find an existing purchase order with the same <u>Credit Card Number</u> and <u>Purchase Order \#</u> that is on the payment entry. If no match is found, IFCAP will then search for a match using the <u>Credit Card Number</u> and the <u>Amount</u> of the Purchase Card Order.

If a dollar Range has been defined in File 411 the matching process will look for Amounts, which fall within the Range specified.

If no match is found, IFCAP will then do the matching process again using any other Credit Card that is assigned to the CARDHOLDER.

If IFCAP finds potential matches, IFCAP will display a list of possible Purchase Card orders.

Enter the sequence number associated with the Purchase Card order you want to reconcile or enter ND to see the *next payment document*. IFCAP will display the next payment document

Select DO at the Action Code: prompt to display the purchase order.

Enter DC at the Action Code: prompt to display any previously reconciled charges for this order.

Enter RS at the Action Code: prompt to reselect the purchase document and start the matching process over.

Enter RD at the Action Code: prompt to Redisplay Data.

Enter RC at the Action Code: prompt to Reconcile the payment with the selected Purchase Card order.

If the Purchase Order is a Simplified Order or a Detailed Order and the Receiving Required response was N, the Complete Order Received?: prompt will appear. Enter Y if the item(s) you are receiving are the last of the outstanding items for the order.

Enter Y at the Final Payment: prompt ONLY if you do not expect any more payments or credits to the Purchase Card order you selected.

If you indicate all the merchandise is received but you indicate the payment is NOT the Final you will receive this prompt: Are You Going To Dispute This Charge?: Enter Yes or NO as applicable.

If there is a difference between the accounting elements on the Purchase Card Order in IFCAP and the accounting elements on the payment charge an Expenditure Transfer (ET) document will be created automatically and sent to FMS in Austin. (IFCAP is presumed to have the correct set of accounting elements.)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Reports Menu ...</strong></p>
<p><strong>Approving Official Menu ...</strong></p>
<p><strong>Process Purchase Card Menu ...</strong></p>
<p><strong>Purchase Card Display/Print Menu ...</strong></p>
<p><strong>Reconciliation Menu ...</strong></p>
<p><strong>You are reconciling this credit card CHARGE:</strong></p>
<p><strong>Reconcile Doc: C65544433300001 Purchase Date: APR 29, 1996</strong></p>
<p><strong>Vendor Name: 6NPDB-HRSA P.O.#: 999-P75202</strong></p>
<p><strong>TXN REF: A2430128612106121054270 $Amount: 2.00</strong></p>
<p><strong>------------------------------------------------------------------------------</strong></p>
<p><strong>to this IFCAP Purchase Card order:</strong></p>
<p><strong>IFCAP Order FCP: 221 SUPPLY 4537B (REV) Purchase Date: JAN 26, 1998</strong></p>
<p><strong>Vendor Name: IFVENDOR,TEN P.O.#: 999-P85050</strong></p>
<p><strong>STATUS: Ordered (No Fiscal Action Required) $Amount: 2.00</strong></p>
<p><strong>Total Reconciled Charges: 0.00</strong></p>
<p><strong>---------------------------------------------------------------------------</strong></p>
<p><strong>The CC-credit card # and Purchase Card order card # are different.</strong></p>
<p><strong>____________________________________________________________________________</strong></p>
<p><strong>Action Code: RC: Reconcile DO: Display Order ND: Next Document</strong></p>
<p><strong>RS: Reselect RD: Redisplay Data DC: Display Charges</strong></p>
<p><strong>Action: rc</strong></p>
<p><strong>COMPLETE ORDER RECEIVED: NO// y YES</strong></p>
<p><strong>WARNING: If a credit or additional charge is expected against this order number do NOT respond YES.</strong></p>
<p><strong>FINAL CHARGE: NO// y YES</strong></p>
<p><strong>COMMENTS:</strong></p>
<p><strong>1&gt;</strong></p>
<p><strong>EDIT Option:</strong></p>
<p><strong>Generating ET-document to FMS...</strong></p>
<p><strong>AUTO reconciliation ends.</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Manual Charge Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are an Approving Official for the service, IFCAP will ask you if you want to reconcile for your own Purchase Card orders. If you do, enter Yes. If you are the Approving Official for another Cardholder and you want to Reconcile orders for that person, enter No. You will then be asked to enter a Cardholder’s name. IFCAP will display the first payment document.

IFCAP will display a listing of any Unreconciled payment charges for the cardholder selected. User can select the payment charge to be reconciled.

IFCAP will attempt to find an existing Purchase Card Order with the same Credit Card Number and Amount.

If a dollar Range has been defined in File 411 the matching process will look for Amounts, which fall within the Range, specified.

If no match is found, IFCAP will list any open Purchase Card order, which has the same Credit Card number.

User can select the Purchase Card order they wish to reconcile to the payment charge.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>You are reconciling this credit card CHARGE:</strong></p>
<p><strong>Reconcile Doc: C62255544411100 Purchase Date: APR 26, 1996</strong></p>
<p><strong>Vendor Name: IFVENDOR1,ONE P.O.#:</strong></p>
<p><strong>TXN REF: Y2407105611978000001842 $Amount: 150.20</strong></p>
<p><strong>------------------------------------------------------------------------------</strong></p>
<p><strong>to this IFCAP Purchase Card order:</strong></p>
<p><strong>IFCAP Order FCP: 221 SUPPLY 4537B (REV) Purchase Date: APR 28, 1997</strong></p>
<p><strong>Vendor Name: IFVENDOR1,TWO P.O.#: 999-P65024</strong></p>
<p><strong>STATUS: Ordered (No Fiscal Action Required) $Amount: 667.14</strong></p>
<p><strong>Total Reconciled Charges: 0.00</strong></p>
<p><strong>------------------------------------------------------------------------------</strong></p>
<p><strong>WARNING: The CC-charge amount and Purchase Card order amount are different.</strong></p>
<p><strong>_____________________________________________________________________________</strong></p>
<p><strong>Action Code: RC: Reconcile DO: Display Order ND: Next Document</strong></p>
<p><strong>RS: Reselect RD: Redisplay Data DC: Display Charges</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  Select DO at the Action Code: prompt to display the purchase order.
2.  Enter DC at the Action Code: prompt to display any previously reconciled charges for this order.
3.  Enter RS at the Action Code: prompt to reselect the purchase document. Enter RD at the Action Code: prompt to Redisplay Data.
4.  Enter RC at the Action Code: prompt to Reconcile the payment with the selected Purchase Card order.
5.  Enter Y at the Complete Order Received?: prompt if the item(s) you are receiving are the last of the outstanding items for the order.
6.  Enter Y at the Final Payment: prompt ONLY if you do not expect any more payments to the Purchase Card order you selected.
7.  Enter Y or N at the Are You Going To Dispute This Charge?: prompt. If you indicate all the merchandise is received but you indicate the payment is NOT the Final you will receive this prompt.
8.  If there is a difference between the accounting elements on the Purchase Card Order in IFCAP and the accounting elements on the payment charge an Expenditure Transfer (ET) document will be created automatically and sent to FMS in Austin. (IFCAP is presumed to have the correct set of accounting elements)
9.  If there are other Purchase Card orders to be reconciled IFCAP will display the list again. User may enter “^” to exit the option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>WARNING: The CC-charge amount and Purchase Card order amount are different.</strong></p>
<p><strong>You are reconciling this credit card CHARGE:</strong></p>
<p><strong>Reconcile Doc: C62255544411100 Purchase Date: APR 26, 1996</strong></p>
<p><strong>Vendor Name: IFVENDOR1,ONE P.O.#:</strong></p>
<p><strong>TXN REF: Y2407105611978000001842 $Amount: 150.20</strong></p>
<p><strong>------------------------------------------------------------------------------</strong></p>
<p><strong>to this IFCAP Purchase Card order:</strong></p>
<p><strong>IFCAP Order FCP: 221 SUPPLY 4537B (REV) Purchase Date: APR 28, 1997</strong></p>
<p><strong>Vendor Name: IFVENDOR1,TWO P.O.#: 999-P65024</strong></p>
<p><strong>STATUS: Ordered (No Fiscal Action Required) $Amount: 667.14</strong></p>
<p><strong>Total Reconciled Charges: 0.00</strong></p>
<p><strong>______________________________________________________________________________</strong></p>
<p><strong>Action Code: RC: Reconcile DO: Display Order ND: Next Document</strong></p>
<p><strong>RS: Reselect RD: Redisplay Data DC: Display Charges</strong></p>
<p><strong>Action: rc</strong></p>
<p><strong>COMPLETE ORDER RECEIVED: YES// n NO</strong></p>
<p><strong>WARNING: If a credit or additional charge is expected against this order number</strong></p>
<p><strong>do NOT respond YES.</strong></p>
<p><strong>FINAL CHARGE: NO//</strong></p>
<p><strong>Are you going to dispute this charge amount?: NO// NO</strong></p>
<p><strong>COMMENTS:</strong></p>
<p><strong>1&gt;</strong></p>
<p><strong>EDIT Option:</strong></p>
<p><strong>Manual Select by Listing Unreconciled C-payment document:</strong></p>
<p><strong>1 04-26-96 $667.14 ~ IFVENDOR1,THREE</strong></p>
<p><strong>2 04-26-96 $330.00 ~ IFVENDOR1,FOUR</strong></p>
<p><strong>3 04-30-96 $116.96 ~ IFVENDOR1,FIVE</strong></p>
<p><strong>4 04-30-96 $ 0.45 ~ IFVENDOR1,SIX</strong></p>
<p><strong>5 04-30-96 $608.96 ~ IFVENDOR1,SEVEN</strong></p>
<p><strong>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</strong></p>
<p><strong>CHOOSE 1-5:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Reconcile by Purchase Card Order 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If no match is found, IFCAP will then look for any Unreconciled charge that has the same Credit Card Number as that on the order selected.

If no match is found, the User may select another Purchase Card Order.

Enter the first characters of the Purchase Card order. IFCAP will list the outstanding Purchase Card order numbers that begin with the characters you entered.

Select a Purchase Card order number or enter a caret (^) to return to the Action Code: prompt.

Enter RS at the Action Code: prompt to reselect the charges.

Enter DC at the Action Code: prompt to display any previously reconciled charges on this order.

Enter RD at the Action Code: prompt to redisplay data. IFCAP will redisplay the purchase document and vendor name, and potential Purchase Card order matches with the purchase document.

Enter NP at the Action Code: prompt to select a new document.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Number: 3 Reconcile by Purchase Card Order #</strong></p>
<p><strong>Select Purchase Card Order #: p0</strong></p>
<p><strong>1 P00002 999-P00 999-P00002 02-11-00 PC Ordered (No Fiscal Action Required</strong></p>
<p><strong>FCP: 110 9.00 IFVENDOR,SIX</strong></p>
<p><strong>2 P00003 999-P00 999-P00003 04-13-00 PC Ordered (No Fiscal Action Required</strong></p>
<p><strong>FCP: 060 10.00 IFVENDOR,THREE</strong></p>
<p><strong>3 P05004 999-P05 999-P05004 09-23-99 PC Ordered (No Fiscal Action Required</strong></p>
<p><strong>FCP: 060 2.00 IFVENDOR1,EIGHT</strong></p>
<p><strong>4 P05005 999-P05 999-P05005 09-23-99 PC Ordered (No Fiscal Action Required</strong></p>
<p><strong>FCP: 300 10.80 IFVENDOR,SIX</strong></p>
<p><strong>5 P05006 999-P05 999-P05006 10-20-99 PC Complete Order Received</strong></p>
<p><strong>FCP: 990 30.00 IFVENDOR1,NINE</strong></p>
<p><strong>CHOOSE 1-5: 1 999 999-P00002 02-11-00 PC Ordered (No Fiscal Action Required</strong></p>
<p><strong>FCP: 110 9.00 IFVENDOR,SIX</strong></p>
<p><strong>You are reconciling this PURCHASE CARD ORDER:</strong></p>
<p><strong>IFCAP Order FCP: 110 IFBUYER,ONE .01 Purchase Date: FEB 11, 2000</strong></p>
<p><strong>Vendor Name: IFVENDOR,SIX P.O.#: 999-P00002</strong></p>
<p><strong>STATUS: Ordered (No Fiscal Action Required) $Amount: 9.00</strong></p>
<p><strong>Total Reconciled Charges: 0.00</strong></p>
<p><strong>---------------------------------------------------------------------------</strong></p>
<p><strong>The system is attempting to locate credit card charge...</strong></p>
<p><strong>Matching Card XXXX2345, Vendor's Purchase Order #:</strong></p>
<p><strong>Not Found</strong></p>
<p><strong>Matching Card XXXX2345, $Amount within Range 5%:</strong></p>
<p><strong>Not Found</strong></p>
<p><strong>Listing All Credit Card Charges with Matched Card XXXX2345:</strong></p>
<p><strong>Not Found</strong></p>
<p><strong>No Credit Card Charges Selected!</strong></p>
<p><strong>________________________________________________________________________</strong></p>
<p><strong>Action Code: RS: Reselect Charges RD: Redisplay Data</strong></p>
<p><strong>NP: Next Purchase Order DC: Display Charges</strong></p>
<p><strong>Action:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## ET-FMS Document Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays Electronic Transfer (ET) documents. Control point users can use this option to identify the Purchase Card order number associated with the ET documents listed on their running balance.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p> <strong>Select Purchase Card Menu Option: reconciliation Menu</strong></p>
<p><strong>Reconciliation</strong></p>
<p><strong>Edit/Remove Reconciliation</strong></p>
<p><strong>ET-FMS Document Display</strong></p>
<p><strong>Daily Purchase Card Charges Statement</strong></p>
<p><strong>Select Reconciliation Menu Option: ET-FMS Document Display</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a station number. IFCAP will display the types of transactions you can see.
2.  Enter the transaction type ET.
3.  At the FMS ET Document ID: prompt, enter the document identifier code for the document, or enter two question marks to see a list of available documents. IFCAP will display the document you selected, listing expense and fund information about the document.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>Select one of the following:</strong></p>
<p><strong>ET Expenditure Transfer</strong></p>
<p><strong>Select Transaction Type: ET Expenditure Transfer</strong></p>
<p><strong>FMS ET Document ID: ??</strong></p>
<p><strong>Choose from:</strong></p>
<p><strong>ET-999FADG0006</strong></p>
<p><strong>ET-999FADG1139</strong></p>
<p><strong>ET-999FADG1140</strong></p>
<p><strong>ET-999JJJP1379</strong></p>
<p><strong>FMS ET Document ID: ET-999JJJP1379</strong></p>
<p><strong>FMS Document: ET-999JJJP1379</strong></p>
<p><strong>Description: Auto ET Document</strong></p>
<p><strong>Status: TRANSMITTED</strong></p>
<p><strong>Created: OCT 14, 1999@09:04:52</strong></p>
<p><strong>Description Line #504 Line #4</strong></p>
<p><strong>BBFY: 99 99</strong></p>
<p><strong>BBEY:</strong></p>
<p><strong>FUND: 0160A1 0160A1</strong></p>
<p><strong>STATION: 999 999</strong></p>
<p><strong>SUB STATION:</strong></p>
<p><strong>COST CENTER: 840200 870000</strong></p>
<p><strong>SUB COST CENTER: 00 00</strong></p>
<p><strong>FCP/PRJ: 0100201B1 0100201B1</strong></p>
<p><strong>BOC: 2660 2660</strong></p>
<p><strong>JOB NO:</strong></p>
<p><strong>LINE AMOUNT: 1.50 1.50</strong></p>
<p><strong>LINE ACTION: D I</strong></p>
<p><strong>PURCHASE CARD ORDER: 999-P9535</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Edit/Remove Reconciliation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sometimes, users will inadvertently reconcile a Purchase Card order to the wrong payment document or answer the Complete Order Received or Final Payment questions incorrectly. Use the Remove Reconciliation option to remove the reconciliation so that you can reconcile the Purchase Card order with the correct payment document. Use the Edit Reconciliation option to correct the answer to the Complete Order Received or Final Payment questions.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Menu Option: REConciliation Menu</strong></p>
<p><strong>Reconciliation</strong></p>
<p><strong>Edit/Remove Reconciliation</strong></p>
<p><strong>ET-FMS Document Display</strong></p>
<p><strong>Daily Purchase Card Charges Statement</strong></p>
<p><strong>Select Reconciliation Menu Option: Edit/Remove Reconciliation</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a station number if prompted.
2.  Enter Y at the Edit/Remove Reconciliation For Your Own Purchase Card Orders?: prompt if you want to edit or remove your own reconciliation, otherwise, enter N. Enter the Purchase Credit Card or holder of the Purchase Card associated with the reconciliation you want to edit or remove.
3.  Enter a reconciled Purchase Card order at the Select Reconciled/Disputed C-Document/Purchase Card Order: prompt.
4.  Enter ED at the Action: prompt to edit the reconciliation, or RM at the Action: prompt to remove the reconciliation.
5.  If you do not want to change any data, but want to view the document enter DD at the Action: prompt.
6.  If you edit the reconciliation, IFCAP will allow you to declare whether the complete order has been received (if receiving was not required on the purchase order) and whether the VA has made the final payment to the vendor for this purchase.
7.  Enter comments if you like.
8.  If you remove the reconciliation an ET document will be generated to FMS and a status of order prompt will appear with the new status. Check the status of the order to ensure that IFCAP is setting it correctly.
9.  Enter another reconciled Purchase Card order at the Select Reconciled/Disputed C-Document/Purchase Card Order: prompt, or press \<Enter\> to return to the Reconciliation Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER: 999 ANYCITY,NM</strong></p>
<p><strong>Edit/Remove Reconciliation for your own Purchase Card orders? YES</strong></p>
<p><strong>Select Reconciled/Disputed C-Document/Purchase Card Order: C-99903110001001</strong></p>
<p><strong>C-99903110001001 11-15-99 $12.50 IFVENDOR,THREE</strong></p>
<p><strong> WARNING </strong></p>
<p><strong>This charge is reconciled. If you 'Edit' it, another approval will be needed.</strong></p>
<p><strong>If you 'Remove' the reconciliation, you must reconcile the charge and your</strong></p>
<p><strong>Approving Official will have to approve it again.</strong></p>
<p><strong>Use the action code DD (Display Document) if no change is desired.</strong></p>
<p><strong>Do you want to continue? NO// YES</strong></p>
<p><strong>_______________________________________________________________________________</strong></p>
<p><strong>Action Code: ED: Edit DO: Display Order ND: Next Document</strong></p>
<p><strong>RM: Remove DD: Display Document</strong></p>
<p><strong>Action: RM</strong></p>
<p><strong>COMMENTS:</strong></p>
<p><strong>1&gt;TST</strong></p>
<p><strong>EDIT Option:</strong></p>
<p><strong>Generating ET-document to FMS...</strong></p>
<p><strong>AFTER Removing Change P.O. Status to: Ordered (No Fiscal Action Required)//</strong></p>
<p><strong>22</strong></p>
<p><strong>Select Reconciled/Disputed C-Document/Purchase Card Order:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Daily Purchase Card Charges Statement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is an option to print your daily Purchase Card charges sent from the Austin financial center.

> **NOTE:** You must reconcile your transaction records in a timely manner. When you go to your Purchase Card menu and you have payment documents to reconcile, a bulletin will appear stating “You have (number) transaction(s) to reconcile (date range).” The number states how many payment documents you have to reconcile and the date range states the range you will print in the Daily Purchase Card Charges Statement.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Menu Option: REConciliation Menu</strong></p>
<p><strong>Reconciliation</strong></p>
<p><strong>Edit/Remove Reconciliation</strong></p>
<p><strong>ET-FMS Document Display</strong></p>
<p><strong>Daily Purchase Card Charges Statement</strong></p>
<p><strong>Select Reconciliation Menu Option: Edit/Remove Reconciliation</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter the date you wish to begin the report.
2.  Enter the date you wish to end the report.
3.  Enter a printer name if you wish a hard copy printout of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Reconciliation Menu Option: Daily Purchase Card Charges Statement</strong></p>
<p><strong>For Credit Card Charge Statement Beginning Date: 06/04/00// 111499</strong></p>
<p><strong>For Credit Card Charge Statement Ending Date: 11/14/99// 111699</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>E-Charge Statement for IFBUYER,TWO Statement Date: 11/14/99 -</strong></p>
<p><strong>11/16/99</strong></p>
<p><strong>JUN 6,2000 11:12 PAGE 1</strong></p>
<p><strong>Charge Id PO Date Vendor</strong></p>
<p><strong>P.O. # TXN Ref Charge $AMT</strong></p>
<p><strong>IFCAP P.O. # TXN DATE STATUS</strong></p>
<p><strong>---------------------------------------------------------------------------</strong></p>
<p><strong>STATEMENT DATE: NOV 15,1999</strong></p>
<p><strong>CHARGE DATA for CREDIT CARD #: XXXXXXXXXXXX7625</strong></p>
<p><strong>C-99903110002001 NOV 15,1999</strong></p>
<p><strong>99903110002 32.45</strong></p>
<p><strong>999-P05026 NOV 16,1999 RECONCILED</strong></p>
<p><strong>---------------</strong></p>
<p><strong>SUBTOTAL 32.45</strong></p>
<p><strong>---------------</strong></p>
<p><strong>TOTAL 32.45</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Approving Official Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Approve Reconciliation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Approving Officials use this option to electronically approve the reconciliation. This affords the Approving Official the opportunity to ensure that the reconciliation is correct and complete. The Approve Reconciliation option is controlled with the Security Key PRCH AR.

This new option prompts the Approving Official to loop through all cardholders for whom they have approving authority. The Approving Official will be able to approve a single entry or a range of entries. Once the Approving Official enters their electronic signature, IFCAP will update the status of the order to "Transaction Complete," or to "Transaction Complete (Amended)" if an amendment has been processed on the order.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Menu Option: APProving Official Menu</strong></p>
<p><strong>You have 1 order(s) to approve for FCP,USER.</strong></p>
<p><strong>You have 44 order(s) to approve for IFBUYER1,THREE.</strong></p>
<p><strong>Unreconciled Austin Payments - Official</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Official</strong></p>
<p><strong>Approve Reconciliation</strong></p>
<p><strong>Card Holder Daily Charge Statement</strong></p>
<p><strong>Delinquent PC Listing - Official</strong></p>
<p><strong>Disputed Purchase Card Orders - Official</strong></p>
<p><strong>History of Purchase Card Transactions - Official</strong></p>
<p><strong>Incomplete Purchase Card Orders - Official</strong></p>
<p><strong>Official Charges Audit</strong></p>
<p><strong>Purchase Card Orders Ready for Approval</strong></p>
<p><strong>Reconciled Purchase Card Transactions - Official</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Approve Reconciliation from the Approving Official Menu.
2.  If you are a multi-station site, IFCAP will ask you to enter a station number.
3.  IFCAP will ask if you want to approve reconciliations for all users or for a single specific user. If you select Single Purchase Card User, you can enter two question marks at the Select Purchase Card Order User: prompt and IFCAP will display the valid user names.
4.  Enter the name of a cardholder. If that cardholder has any Unapproved Reconciliations they will be displayed on the screen.
5.  Enter SL at the Action: prompt to select a Purchase Card order for review.
6.  Enter DO at the Action: prompt to display the order.
7.  Enter DC at the Action: prompt to display any previously reconciled charges.
8.  Enter RL at the Action: prompt to Re list the Reconciled orders.
9.  Enter NU at the Action: prompt to view orders for a different user.
10. Enter AP at the Action: prompt to approve the reconciliation.
11. Enter your electronic signature. IFCAP will continue to display Purchase Card orders for each user.
12. Continue to select and approve reconciliations. When you have finished scrolling through the Purchase Card users, IFCAP will return to the Approving Official Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Approving Official Menu Option: Approve Reconciliation</strong></p>
<p><strong>Select one of the following:</strong></p>
<p><strong>1 All Purchase Card Users</strong></p>
<p><strong>2 Single Purchase Card User</strong></p>
<p><strong>Select Number: 1 All Purchase Card Users</strong></p>
<p><strong>Start approving Purchase Card orders for IFBUYER,SEVEN</strong></p>
<p><strong>Compiling user's reconciled purchase orders...</strong></p>
<p><strong>Seq# IFCAP PO # Vendor $Amount Credit Card Vendor $Amount</strong></p>
<p><strong>1 656-P60260 IFVENDOR2,ONE 35.00 STC DINER 35.00</strong></p>
<p><strong>_______________________________________________________________________</strong></p>
<p><strong>Action Code: SL: Select DO: Display Order NU: Next User</strong></p>
<p><strong>AP: Approve RL: Relist Reconciled Orders DC Display Charges</strong></p>
<p><strong>Action: SL</strong></p>
<p><strong>Select Sequence #'s to approve (1-1): 1</strong></p>
<p><strong>__________________________________________________________________</strong></p>
<p><strong>Action Code: SL: Select DO: Display Order NU: Next User</strong></p>
<p><strong>AP: Approve RL: Relist Reconciled Orders DC Display Charges</strong></p>
<p><strong>Action: AP Enter ELECTRONIC SIGNATURE Thank you.</strong></p>
<p><strong>Start approving Purchase Card orders for IFBUYER,EIGHT</strong></p>
<p><strong>Compiling user's reconciled purchase orders...</strong></p>
<p><strong>Seq# IFCAP PO # Vendor $Amount Credit Card Vendor $Amount</strong></p>
<p><strong>1 999-P95502 IFVENDOR,SIX 48.00 IFVENDOR,SIX 48.00</strong></p>
<p><strong>______________________________________________________________________________</strong></p>
<p><strong>Action Code: SL: Select DO: Display Order NU: Next User</strong></p>
<p><strong>AP: Approve RL: Relist Reconciled Orders DC Display Charges</strong></p>
<p><strong>Action: SL</strong></p>
<p><strong>Select Sequence #'s to approve (1-1): 1</strong></p>
<p><strong>__________________________________________________________________________</strong></p>
<p><strong>Action Code: SL: Select DO: Display Order NU: Next User</strong></p>
<p><strong>AP: Approve RL: Relist Reconciled Orders DC Display Charges</strong></p>
<p><strong>Action: AP</strong></p>
<p><strong>Enter ELECTRONIC SIGNATURE CODE: Thank you.</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Approving Official menu provides many different reports that will enable the Approving Official to confirm the correctness of the Reconciliation process. There are reports that identify unreconciled orders, unreconciled payments, incomplete orders, disputed orders and delinquent orders. Reports can be run for all the cardholders the Approving Official is responsible for.

Some reports may be run for a specific cardholder, and some are run for all cardholders. A sample of each report follows.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Menu Option: APProving Official Menu</strong></p>
<p><strong>You have 1 order(s) to approve for FCP,USER.</strong></p>
<p><strong>You have 44 order(s) to approve for IFVENDOR2,TEN.</strong></p>
<p><strong>Unreconciled Austin Payments - Official</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Official</strong></p>
<p><strong>Approve Reconciliation</strong></p>
<p><strong>Card Holder Daily Charge Statement</strong></p>
<p><strong>Delinquent PC Listing - Official</strong></p>
<p><strong>Disputed Purchase Card Orders - Official</strong></p>
<p><strong>History of Purchase Card Transactions - Official</strong></p>
<p><strong>Incomplete Purchase Card Orders - Official</strong></p>
<p><strong>Official Charges Audit</strong></p>
<p><strong>Purchase Card Orders Ready for Approval</strong></p>
<p><strong>Reconciled Purchase Card Transactions - Official</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Unreconciled Austin Payments – Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will display unreconciled payment transactions for the approving official's cards. The Official will enter their name, select a cardholder or accept the default of first for all cardholders they are an official for and enter a printer device.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select NEW PERSON NAME: IFCAPCARDHOLDER,ONE IFCAPCARDHOLDER,ONE LKG COMP</strong></p>
<p><strong>UTER SYSTEMS ANALYST</strong></p>
<p><strong>START WITH CARD HOLDER: FIRST//</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>UNRECONCILED AUSTIN PAYMENTS - OFFICIAL JUN 2,2000 16:46 PAGE 1</strong></p>
<p><strong>TRANSACTION</strong></p>
<p><strong>CARD HOLDER DATE AMOUNT</strong></p>
<p><strong>MERCHANT NAME ORACLE DOCUMENT ID</strong></p>
<p><strong>------------------------------------------------------------------------</strong></p>
<p><strong>IFBUYER,NINE 430.00</strong></p>
<p><strong>IFVENDOR2,TWO C99982520012001</strong></p>
<p><strong>IFBUYER,TEN SEP 1,1998 125.99</strong></p>
<p><strong>IFVENDOR2,THREE C99982520001001</strong></p>
<p><strong>-------------</strong></p>
<p><strong>SUBTOTAL 555.99</strong></p>
<p><strong>SUBCOUNT 2</strong></p>
<p><strong>SUBMEAN 278.00</strong></p>
<p><strong>IFBUYER,TWO NOV 16,1999 12.50</strong></p>
<p><strong>IFVENDOR,THREE C-99903110001001</strong></p>
<p><strong>-------------</strong></p>
<p><strong>SUBTOTAL 12.50</strong></p>
<p><strong>SUBCOUNT 1</strong></p>
<p><strong>SUBMEAN 12.5</strong></p>
<p><strong>IFBUYER1,ONE MAY 28,1996 2.00</strong></p>
<p><strong>IFVENDOR2,FOUR C65861470001001</strong></p>
<p><strong>IFBUYER1,ONE MAY 28,1996 94.00</strong></p>
<p><strong>IFVENDOR2,FIVE C65861470001002</strong></p>
<p><strong>IFBUYER1,ONE MAY 28,1996 2.00</strong></p>
<p><strong>IFVENDOR2,SIX C65861470001003</strong></p>
<p><strong>-------------</strong></p>
<p><strong>SUBTOTAL 98.00</strong></p>
<p><strong>SUBCOUNT 3</strong></p>
<p><strong>SUBMEAN 32.67</strong></p>
<p><strong>-------------</strong></p>
<p><strong>TOTAL 666.49</strong></p>
<p><strong>COUNT 6</strong></p>
<p><strong>MEAN 111.08</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Unreconciled Purchase Card Transactions – Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will display all unreconciled Purchase Card orders for cards controlled by the official. The official will enter a station number, beginning and ending dates and a printer device.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>Enter beginning date: 010100 JAN 1,2000</strong></p>
<p><strong>Enter ending date: t JUN 2,2000</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>UNRECONCILED PURCHASE CARD ORDERS JUN 02, 2000@16:50:06 PAGE 1</strong></p>
<p><strong>P.O. DATE ORDER # $AMT TYPE(S/D)</strong></p>
<p><strong>VENDOR DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>---------------------------------------------------------------------------</strong></p>
<p><strong>BUYER: IFBUYER1,TWO</strong></p>
<p><strong>MAR 02, 2000 999-P05104 144.00</strong></p>
<p><strong>IFVENDOR,SIX SHAVING KIT, SURGICAL PREPARATION.</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>BUYER SUBTOTAL - $144.00</strong></p>
<p><strong>BUYER: IFBUYER1,THREE</strong></p>
<p><strong>FEB 11, 2000 999-B90086 15.00</strong></p>
<p><strong>GSA ADHESIVE TIES, SURGICAL, WHITE, 7-</strong></p>
<p><strong>Complete Order Received</strong></p>
<p><strong>TEST</strong></p>
<p><strong>FEB 11, 2000 999-P85792 2.40</strong></p>
<p><strong>IFVENDOR,SIX COVER ARMBOARD 9 INCH</strong></p>
<p><strong>Complete Order Received</strong></p>
<p><strong>Testing receiving and code sheets generation, 2/11/00.</strong></p>
<p><strong>MAR 01, 2000 999-P85809 15.00</strong></p>
<p><strong>IFVENDOR,SIX COVER ARMBOARD 9 INCH</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>MAR 01, 2000 999-P85807 2.40</strong></p>
<p><strong>IFVENDOR,SIX COVER ARMBOARD 9 INCH</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>MAR 29, 2000 999-P85864 6.00 SIMPLIFIED</strong></p>
<p><strong>IFVENDOR,SIX TEST, 3/29/00</strong></p>
<p><strong>Ordered (No Fiscal Action)-Amended</strong></p>
<p><strong>APR 07, 2000 999-P85867 1.00 SIMPLIFIED</strong></p>
<p><strong>IFVENDOR,SIX TESTING AFTER CONVERSION OF FILE 20</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>APR 13, 2000 999-A99064 12.85</strong></p>
<p><strong>IFVENDOR,SIX NEEDLE JAMSHIDI BONE MARROW 11GA X</strong></p>
<p><strong>Complete Order Received (Amended)</strong></p>
<p><strong>TESTING FOR PRC*5*244, 4/13/00.</strong></p>
<p><strong>APR 14, 2000 999-P85873 78.50 DETAILED</strong></p>
<p><strong>IFVENDOR2,TEN BANDAGE CAST PLASTER OF PARIS IMPR</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>BUYER: IFBUYER1,THREE</strong></p>
<p><strong>TESTING</strong></p>
<p><strong>BUYER SUBTOTAL - $267.55</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Card Holder Daily Charge Statement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints the cardholder's daily charge statement. The official will define the beginning and ending statement date, select a cardholder, and enter a printer device.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>For Credit Card Charge Statement Beginning Date: 05/31/00// 010100</strong></p>
<p><strong>For Credit Card Charge Statement Ending Date: 01/01/00// t</strong></p>
<p><strong>Select Purchase Card Holder: buye IFBUYER1,THREE CR COMPUTER</strong></p>
<p><strong>SYSTEMS ANALYST</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>E-Charge Statement for IFBUYER1,THREE Statement Date: 01/01/00 - 06/02/00</strong></p>
<p><strong>JUN 2,2000 16:54 PAGE 1</strong></p>
<p><strong>Charge Id PO Date Vendor</strong></p>
<p><strong>P.O. # TXN Ref Charge $AMT</strong></p>
<p><strong>IFCAP P.O. # TXN DATE STATUS</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>STATEMENT DATE: MAR 10,2000</strong></p>
<p><strong>CHARGE DATA for CREDIT CARD #: XXXXXXXXXXXX0001</strong></p>
<p><strong>C-999000P85846 MAR 10,2000 IFVENDOR,SIX</strong></p>
<p><strong>134567890 10.00</strong></p>
<p><strong>999-P85846 MAR 10,2000 RECONCILED</strong></p>
<p><strong>---------------</strong></p>
<p><strong>SUBTOTAL 10.00</strong></p>
<p><strong>STATEMENT DATE: APR 18,2000</strong></p>
<p><strong>CHARGE DATA for CREDIT CARD #: XXXXXXXXXXXX0001</strong></p>
<p><strong>C-9990002P95080 NOV 20,1998 IFVENDOR2,SEVEN</strong></p>
<p><strong>134567890 8.20</strong></p>
<p><strong>999-P95080 NOV 20,1998 RECONCILED</strong></p>
<p><strong>---------------</strong></p>
<p><strong>SUBTOTAL 8.20</strong></p>
<p><strong>---------------</strong></p>
<p><strong>TOTAL 18.20</strong></p>
<p><strong>7.2.6 Delinquent PC Listing - Official</strong></p>
<p><strong>7.2.6 Delinquent PC Listing - Official</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Delinquent PC Listing – Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will display delinquent orders (items not yet received) for all Purchase Card orders (that are detailed orders and receiving required is Yes) for which the user is the approving official.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Please enter a device for printing this report</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>DELINQUENT PURCHASE CARD LISTING PAGE 1</strong></p>
<p><strong>PURCHASE CARD NAME PO # STATUS DELIVERY DATE</strong></p>
<p><strong>VENDOR VENDOR PHONE</strong></p>
<p><strong>DELIVERY DATE LINE ITEM OUTSTANDING QTY ORDERED QTY OUTSTANDING</strong></p>
<p><strong>AMOUNT OUTSTANDING ITEM DESCRIPTION</strong></p>
<p><strong>BUYER: IFBUYER,TWO</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>110CR P85157 Partial Order Received MAR 18, 1998</strong></p>
<p><strong>IFVENDOR,THREE 555-222-2625</strong></p>
<p><strong>JUL 01, 1999 1 12 6</strong></p>
<p><strong>20.40 STUFF</strong></p>
<p><strong>PURCHASE CARD SUBTOTAL: 20.40</strong></p>
<p><strong>IFVENDOR,ONE P05099 Partial Order Received FEB 22, 2000</strong></p>
<p><strong>IFVENDOR,THREE 555-222-2625</strong></p>
<p><strong>FEB 22, 2000 1 12 8</strong></p>
<p><strong>25.60 DOGS-LARGE-FURRY</strong></p>
<p><strong>PURCHASE CARD SUBTOTAL: 46.00</strong></p>
<p><strong>SUPPLY1 B90090 Complete Order Received (Amended) MAR 13, 2000</strong></p>
<p><strong>GSA 555 777 4046</strong></p>
<p><strong>MAR 13, 2000 1 12 1</strong></p>
<p><strong>1.25 COVER ARMBOARD 9 INCH</strong></p>
<p><strong>MAR 13, 2000 2 12 1</strong></p>
<p><strong>4.50 BATTERY AAA ALKALINE 1.5 VOLTS</strong></p>
<p><strong>PURCHASE CARD SUBTOTAL: 5.75</strong></p>
<p><strong>PC#EDIT P95345 Partial Order Received MAY 27, 1999</strong></p>
<p><strong>IFVENDOR,SIX 555-333-4444</strong></p>
<p><strong>OCT 06, 1999 1 12 6</strong></p>
<p><strong>6.00 ADHESIVE TIES, SURGICAL, WHITE, 7-1/4 I</strong></p>
<p><strong>PURCHASE CARD SUBTOTAL: 11.75</strong></p>
<p><strong>SUPPLY1 P95301 Ordered (No Fiscal Action Required) MAR 09, 1999</strong></p>
<p><strong>IFVENDOR,SIX 555-333-8838</strong></p>
<p><strong>MAR 16, 1999 1 12 10</strong></p>
<p><strong>120.00 SHAVING KIT, SURGICAL PREPARATION. DISP</strong></p>
<p><strong>MAR 16, 1999 2 12 8</strong></p>
<p><strong>0.80 COVER ARMBOARD 9 INCH</strong></p>
<p><strong>PURCHASE CARD SUBTOTAL: 132.55</strong></p>
<p><strong>SUPPLY229 P95403 Partial Order Received JUL 15, 1999</strong></p>
<p><strong>IFVENDOR2,EIGHT</strong></p>
<p><strong>JUL 15, 1999 1 12 6</strong></p>
<p><strong>7.50 COVER ARMBOARD 9 INCH</strong></p>
<p><strong>JUL 15, 1999 2 12 5</strong></p>
<p><strong>18.00 REAGENT, IRON BINDING</strong></p>
<p><strong>JUL 15, 1999 3 24 6</strong></p>
<p><strong>11.10 PASTA PERFECT, ROTINI &amp; SPINACH, ROTINI</strong></p>
<p><strong>PURCHASE CARD SUBTOTAL: 169.15</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Disputed Purchase Card Orders – Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of disputed Purchase Card orders. The official will enter a station number and printer device.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>DISPUTED PURCHASE CARD ORDERS JUN 02, 2000@17:06:03 PAGE 1</strong></p>
<p><strong>PC NAME P.O. DATE $AMT PC ORDER # VENDOR</strong></p>
<p><strong>DATE RECONCILED DESCRIPTION</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>---------------------------------------------------------------------------</strong></p>
<p><strong>BUYER: IFBUYER,ONE</strong></p>
<p><strong>PROS MAY 19, 1998 29.90 999-P85308 SAMPSON</strong></p>
<p><strong>JUL 02, 1998 Prosthetic Order</strong></p>
<p><strong>TESTING</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### History of Purchase Card Transactions – Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will display Purchase Card data within a date range selected by the official. The report can display PAID orders, Unpaid orders or Both types of orders in the same report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Enter beginning date: 010100 JAN 1,2000</strong></p>
<p><strong>Enter ending date: T JUN 2,2000</strong></p>
<p><strong>Select one of the following:</strong></p>
<p><strong>P Paid</strong></p>
<p><strong>U Unpaid</strong></p>
<p><strong>B Both</strong></p>
<p><strong>STATUS: Both</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>HISTORY OF PURCHASE CARD TRANSACTIONS REPORT - ALL PAGE: 1</strong></p>
<p><strong>FCP PC NUMBER PURCHASE DATE BUYER VENDOR</strong></p>
<p><strong>AMOUNT COST CENTER BUDGET OBJECT CODE</strong></p>
<p><strong>FIRST LINE ITEM DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>--------------------------------------------------------------------------</strong></p>
<p><strong>036 P05176 MAY 01, 2000 IFBUYER,ONE IFVENDOR,THREE</strong></p>
<p><strong>27.60 828100 2660 Operating Supplies and Ma</strong></p>
<p><strong>WOODEN WIDGETS-PINE-PAINTED</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>CONTROL POINT 36 SUBTOTAL: 27.60</strong></p>
<p><strong>060 B90093 MAY 03, 2000 SUPPLY,USER GSA</strong></p>
<p><strong>2.00 820300 2632 Other Medical and Dental Supplies</strong></p>
<p><strong>SHAVING KIT, SURGICAL PREPARATION. DISPOSABLE. CONSISTS OF</strong></p>
<p><strong>Complete Order Received (Amended)</strong></p>
<p><strong>060 P05174 MAY 01, 2000 IFBUYER,ONE IFVENDOR,THREE</strong></p>
<p><strong>0.00 842100 2660 Operating Supplies and Ma</strong></p>
<p><strong>WOODEN WIDGETS-PINE-PAINTED</strong></p>
<p><strong>Order Not Completely Prepared</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Incomplete Purchase Card Orders – Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a report of incomplete Purchase Card orders for the approving official. The official will enter a station number, fiscal year and printer device.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER: 999//</strong></p>
<p><strong>Select FISCAL YEAR: 00//</strong></p>
<p><strong>Please select a device for printing this report.</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>INCOMPLETE PURCHASE CARD ORDERS REPORT PAGE 1</strong></p>
<p><strong>PURCHASE CARD ORDER PO DATE SUPPLY STATUS</strong></p>
<p><strong>BUYER DATE PO ASSIGNED</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>999-P05174 MAY 01, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER,ONE DVMMAY 01, 2000@12:20</strong></p>
<p><strong>999-P05166 APR 13, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER,ONE DVMAPR 13, 2000@12:16</strong></p>
<p><strong>999-P05128 MAR 21, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER,ONE DVMMAR 21, 2000@12:43</strong></p>
<p><strong>999-P05127 MAR 21, 2000 Order Not Completely Prepared</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Official Charges Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a report to list approving official charge audit data. The official will define the statement date and enter a printer device.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>START WITH STATEMENT DATE: FIRST//</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>IFCAP APPROVING OFFICIAL CHARGE AUDIT JUN 2,2000 17:14 PAGE 1</strong></p>
<p><strong>CARD# PURCH DT ORACLE ID # IFCAP P/O # MERCHANT NAME AMOUNT</strong></p>
<p><strong>----------------------------------------------------------------------------</strong></p>
<p><strong>STATEMENT DATE: MAY 26,1996</strong></p>
<p><strong>APPROVING OFFICIAL: IFBUYER1,THREE</strong></p>
<p><strong>CARD HOLDER: FCP,USER</strong></p>
<p><strong>1000 04/26/96 C99961470011001 IFVENDOR2,NINE 46.20</strong></p>
<p><strong>1000 04/26/96 C99961470011002 IFVENDOR3,TEN 629.65</strong></p>
<p><strong>1000 04/26/96 C99961470011003 IFVENDOR3,ONE 793.50</strong></p>
<p><strong>STATEMENT DATE: MAR 4,1998</strong></p>
<p><strong>APPROVING OFFICIAL: IFBUYER1,THREE</strong></p>
<p><strong>CARD HOLDER: SUPPLY,USER</strong></p>
<p><strong>0002 03/04/98 C-999-8037004 999-P85127 9.00</strong></p>
<p><strong>0002 03/04/98 C-999-8037005 999-P85126 15.00</strong></p>
<p><strong>0002 03/04/98 C-999-8037006 999-P85125 1100.00</strong></p>
<p><strong>0002 03/04/98 C-999-8037007 999-P85124 10.20</strong></p>
<p><strong>--------</strong></p>
<p><strong>SUBTOTAL 1134.20</strong></p>
<p><strong>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; want to remove this</strong></p>
<p><strong>TOTAL 55482.1</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Purchase Card Orders Ready for Approval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists Purchase Card orders that are ready for approval. The user will enter a station and printer device.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>PURCHASE CARD ORDERS READY FOR APPROVAL PAGE 6</strong></p>
<p><strong>PC DATE DATE RECONCILED PC NUMBER $AMT</strong></p>
<p><strong>VENDOR DESCRIPTION</strong></p>
<p><strong>--------------------------------------------------------------------------</strong></p>
<p><strong>BUYER: IFBUYER1,FOUR</strong></p>
<p><strong>JAN 06, 2000 JAN 06, 2000 A99029 129</strong></p>
<p><strong>IFVENDOR,SIX BATTERY AAA ALKALINE 1.5 VOLTS</strong></p>
<p><strong>JAN 18, 2000 JAN 18, 2000 P85615 15</strong></p>
<p><strong>IFVENDOR2,SEVEN COVER ARMBOARD 9 INCH</strong></p>
<p><strong>FEB 23, 2000 FEB 23, 2000 P85804 6</strong></p>
<p><strong>IFVENDOR,SIX COVER ARMBOARD 9 INCH</strong></p>
<p><strong>MAR 07, 2000 MAR 07, 2000 P85830 1.2</strong></p>
<p><strong>IFVENDOR3,TWO TESTING</strong></p>
<p><strong>MAR 07, 2000 MAR 07, 2000 P85829 27</strong></p>
<p><strong>IFVENDOR2,SEVEN COVER ARMBOARD 9 INCH</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Reconciled Purchase Card Transactions – Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will afford the Approving Official an opportunity to review Reconciliations that have been processed. The user will enter the station number, date range, and device to display or print the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>Enter beginning date: 010100 JAN 1,2000</strong></p>
<p><strong>Enter ending date: t JUN 2,2000</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>RECONCILED PURCHASE CARD ORDERS JUN 02, 2000@17:30:57 PAGE 1</strong></p>
<p><strong>P.O. DATE DATE RECONCILED ORDER # $AMT TYPE(S/D)</strong></p>
<p><strong>VENDOR DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>DOC-REF # RECONCILED $AMT RECONCILE VENDOR FINAL CHARGE</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>BUYER: IFBUYER1,FIVE</strong></p>
<p><strong>MAR 09, 2000 MAR 09, 2000 999-P85834 12.12 DETAILED</strong></p>
<p><strong>IFVENDOR,SIX BATTERY AAA ALKALINE 1.5 VOLTS</strong></p>
<p><strong>Reconciled - Amended</strong></p>
<p><strong>C-999000P85834 6.12 IFVENDOR,SIX NO</strong></p>
<p><strong>C-9990002P85834 6.00 IFVENDOR,SIX YES</strong></p>
<p><strong>RECONCILED SUBTOTAL - $12.12</strong></p>
<p><strong>BUYER SUBTOTAL - $12.12</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Purchase Card Coordinator Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purchase Card Coordinator's Menu is a stand-alone menu that must be assigned to the Purchase Card Coordinator at your facility. It has a set of options that allow the Purchase Card Coordinator to add, change or delete information about Purchase Card Users and monitor the use of Purchase Cards at their facility. The option names and descriptions are listed below.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Austin Audit Information</strong></td>
<td>This option is used to link Oracle ID numbers to Purchase Card numbers, to be used with random sample audits performed by Austin.</td>
</tr>
<tr class="even">
<td><strong>Charge Card Reg. Exception</strong></td>
<td>This report will list any Charge Card Registration entries passed to IFCAP but not activated in File #440.5</td>
</tr>
<tr class="odd">
<td><strong>Coordinator Approving Official Charge Audit</strong></td>
<td><p>This report provides an audit list of</p>
<p>Charges by selected date and approving official.</p></td>
</tr>
<tr class="even">
<td><strong>Daily Charge Transmission Log</strong></td>
<td>This report will list the charge transmissions received in IFCAP for a selected date. The entries identify the number of records sent from Austin and the number posted to IFCAP.</td>
</tr>
<tr class="odd">
<td><strong>Delinquent Approvals</strong></td>
<td>This report will list Purchase Card orders, which were approved more than 14 days after being reconciled.</td>
</tr>
<tr class="even">
<td><strong>Delinquent PC Listing</strong></td>
<td>This option creates a report of delinquent Purchase Card orders.</td>
</tr>
<tr class="odd">
<td><strong>Delinquent Reconciliations</strong></td>
<td>This report will list transactions that were reconciled more than 5 days after being received in File 440.6.</td>
</tr>
<tr class="even">
<td><strong>Fiscal Daily Review</strong></td>
<td>This option creates a report showing buyer, vendor, and status information for Purchase Card orders within a selected date range.</td>
</tr>
<tr class="odd">
<td><strong>History of Purchase Card Transactions</strong></td>
<td>This option creates a report of Purchase Card orders sorted by unpaid, paid or both status, for a selected date range.</td>
</tr>
<tr class="even">
<td><strong>IMPAC Account Information</strong></td>
<td>This option is used to generate a report of card information sent from the credit card vendor. User may display Active, Inactive or Both types of entries.</td>
</tr>
<tr class="odd">
<td><strong>Inactivate Expired Charge Cards</strong></td>
<td>This option is used to inactivate the expired charge cards before the default date of TODAY.</td>
</tr>
<tr class="even">
<td><strong>Incomplete Purchase Card Orders Report</strong></td>
<td>This option creates a report of incomplete Purchase Card orders.</td>
</tr>
<tr class="odd">
<td><strong>Print Unregistered Credit Card Charges</strong></td>
<td>This report will list all charges in File #440.6 that have no corresponding credit card entry in File #440.5</td>
</tr>
<tr class="even">
<td><strong>Purchase Card exceptions/replacements</strong></td>
<td>This option will allow users to print exceptions/replacements reports previously run through the Fileman print option.</td>
</tr>
<tr class="odd">
<td><strong>Purchase Card Information List</strong></td>
<td>This option will display card holder, Purchase Card name, approving official, alternate approving official, and surrogate(s) for entries in the Purchase Card Information file (#440.5).</td>
</tr>
<tr class="even">
<td><strong>Purchase Card Registration</strong></td>
<td>This option is used to assign Purchase Cards to the users on the IFCAP system.</td>
</tr>
<tr class="odd">
<td><strong>Purchase Card Statistics</strong></td>
<td>This option creates a report of totals for each Purchase Card and each control point, and the percentage of Purchase Card orders for each control point.</td>
</tr>
<tr class="even">
<td><strong>Purchase Card Timely Commitment Report</strong></td>
<td>This option is used to track the days between initial entry into IFCAP, signing of order and reconciliation.</td>
</tr>
<tr class="odd">
<td><strong>Reconciled Purchase Card Transactions</strong></td>
<td>This option creates a report of reconciled Purchase Card orders sorted by user and card number.</td>
</tr>
<tr class="even">
<td><strong>Retrieve Unregistered Credit Card Charges</strong></td>
<td>After the credit card information has been entered into File #440.5 for an unregistered charge, this option will fill-in the cardholder information on the unregistered charges in File # 440.6. These charges will be then be ready for reconciliation.</td>
</tr>
<tr class="odd">
<td><strong>Summary Report of Unpaid PC Transactions</strong></td>
<td>This option creates a report showing the unpaid Purchase Card order total for each control point.</td>
</tr>
<tr class="even">
<td><strong>Unapproved Reconciliations</strong></td>
<td>This option generates a report of unreconciled Purchase Card data, sorted by approving official, control point, and cardholder.</td>
</tr>
<tr class="odd">
<td><strong>Unreconciled Austin Payment Transactions</strong></td>
<td>This option is used to print Oracle transaction data from unreconciled transactions.</td>
</tr>
<tr class="even">
<td><strong>Unreconciled Purchase Card Transactions</strong></td>
<td>This option creates a report of unreconciled Purchase Card orders.</td>
</tr>
</tbody>
</table>

## Austin Audit Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to link payment transaction numbers to Purchase Cardholders and Purchase Card orders, to be used with random sample audits performed by Austin.

### Menu Path 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Austin Audit Information</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter the Payment Document ID you wish to start with or accept the default.
2.  Enter a device if you wish to print the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: austin Audit Information</strong></p>
<p><strong>START WITH ORACLE DOCUMENT ID: FIRST//</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>AUSTIN AUDIT INFORMATION MAY 11,2000 17:46 PAGE 1</strong></p>
<p><strong>ORACLE DOCUMENT ID PO NUMBER DATE STATUS</strong></p>
<p><strong>AMOUNT FUND ACC CODE COST CENTER BOC</strong></p>
<p><strong>MERCHANT NAME CARD HOLDER</strong></p>
<p><strong>VENDOR NAME</strong></p>
<p><strong>--------------------------------------------------------------------------</strong></p>
<p><strong>999-000P95039 999-P95039 OCT 28,1998 RECONCILED</strong></p>
<p><strong>35.00 0160B1 364840 211200 2631</strong></p>
<p><strong>IFVENDOR,SIX IFBUYER1,FOUR</strong></p>
<p><strong>IFVENDOR,SIX</strong></p>
<p><strong>999-001P95039 999-P95039 OCT 28,1998 RECONCILED</strong></p>
<p><strong>42.50 0160B1 364840 211200 2631</strong></p>
<p><strong>IFVENDOR,SIX IFBUYER1,FOUR</strong></p>
<p><strong>IFVENDOR,SIX</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Charge Card Reg. Exception

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will list any Charge Card Registration entries passed to IFCAP but not activated in File \#440.5

### Menu Path 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Charge Card Reg. Exception</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a device if you want a printout of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: charge card reg. Exception</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>Charge Card Reg. Exception List MAY 11,2000 17:58 PAGE 1</strong></p>
<p><strong>Charge Card # Exp. Date Replaced Card #</strong></p>
<p><strong>Card Holder IFCAP CARD HOLDER FCP #</strong></p>
<p><strong>Station S.P. Limit M.P. Limit</strong></p>
<p><strong>Fund Code ACC Code Cost Center BOC</strong></p>
<p><strong>--------------------------------------------------------------------------</strong></p>
<p><strong>666877* 19991231</strong></p>
<p><strong>IFBUYER1,SIX</strong></p>
<p><strong>999 7500 35000</strong></p>
<p><strong>0160B1 5942 856100 2660</strong></p>
<p><strong>669997* 19991231</strong></p>
<p><strong>IFBUYER1,SIX</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Coordinator Approving Official Charge Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides an audit list of Charges by selected date and approving official.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Coordinator Approving Official Charge Audit</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the statement Date you want to run the report for.

Enter a Device if you wish to print the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: coordinator Approving Official Charge Audit</strong></p>
<p><strong>* Previous selection: STATEMENT DATE not null</strong></p>
<p><strong>START WITH STATEMENT DATE: FIRST//</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>IFCAP APPROVING OFFICIAL CHARGE AUDIT MAY 11,2000 18:04 PAGE 1</strong></p>
<p><strong>CARD# PURCH DT ORACLE ID # IFCAP P/O # MERCHANT NAME AMOUNT</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>STATEMENT DATE: FEB 25,1999</strong></p>
<p><strong>APPROVING OFFICIAL: IFBUYER1,THREE</strong></p>
<p><strong>CARD HOLDER: SUPPLY,USER</strong></p>
<p><strong>0004 02/25/99 C-999000P95265 999-P95265 IFVENDOR3,TWO 1.25</strong></p>
<p><strong>0003 02/25/99 C-999000P95274 IFVENDOR3,THREE 3.75</strong></p>
<p><strong>0003 02/25/99 C-999000P95270 999-P95270 IFVENDOR3,THREE 139.20</strong></p>
<p><strong>0003 02/25/99 C-999000P95269 IFVENDOR3,FOUR 41.40</strong></p>
<p><strong>0003 02/25/99 C-999000P95268 999-P95268 IFVENDOR3,FIVE 3.00</strong></p>
<p><strong>0003 02/25/99 C-999000P95267 999-P95267 IFVENDOR2,SEVEN 2.50</strong></p>
<p><strong>0003 02/25/99 C-999000P95266 IFVENDOR,SIX 1.10</strong></p>
<p><strong>0004 02/25/99 C-999000P95275 999-P95275 IFVENDOR2,SEVEN 29.95</strong></p>
<p><strong>0004 02/25/99 C-999000P95273 IFVENDOR2,SEVEN 9.50</strong></p>
<p><strong>0004 02/25/99 C-999000P95272 999-P95272 IFVENDOR3,FIVE 25.95</strong></p>
<p><strong>0004 02/25/99 C-999000P95271 IFVENDOR2,SEVEN 5.75</strong></p>
<p><strong>--------</strong></p>
<p><strong>SUBTOTAL 263.35</strong></p>
<p><strong>--------</strong></p>
<p><strong>SUBTOTAL 263.35</strong></p>
<p><strong>-------</strong></p>
<p><strong>SUBTOTAL 263.35</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Daily Charge Transmission Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will list the charge transmissions received in IFCAP for a selected date. The report will identify how many records were sent from Austin and how many were posted to IFCAP File \#440.6 and the time of posting.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Daily Charge Transmission Log</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the transmission date you want to check.

Enter a printer device if you want to print a copy of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: daily Charge Transmission Log</strong></p>
<p><strong>START WITH LOG DATE: FIRST//</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>IFCAP DAILY CREDIT CARD CHARGE TRANSMISSION LOG</strong></p>
<p><strong>MAY 12,2000 17:51 PAGE 1</strong></p>
<p><strong>AFC IFCAP</strong></p>
<p><strong>TOT TOT</strong></p>
<p><strong>LOG DT AFC FILE REC REC POSTING BEG POSTING END</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>11/19/97 NEW 368 11/19/97@2:28 PM 11/19/97@2:29 PM</strong></p>
<p><strong>AFC FILE #AAAAA 400 368 11/19/97@3:00 PM 11/19/97@3:00 PM</strong></p>
<p><strong>09/08/98 NEW 2 09/08/98@3:40 PM 09/08/98@3:40 PM</strong></p>
<p><strong>NEW 2 09/08/98@4:35 PM 09/08/98@4:35 PM</strong></p>
<p><strong>NEW 09/08/98@4:48 PM @0:00 AM</strong></p>
<p><strong>NEW 2 09/08/98@4:49 PM 09/08/98@4:49 PM</strong></p>
<p><strong>NEW 2 09/08/98@4:55 PM 09/08/98@4:55 PM</strong></p>
<p><strong>09/09/98 NEW 56 09/09/98@3:02 PM 09/09/98@3:02 PM</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Delinquent Approvals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will list Purchase Card orders that were approved more than 14 days after being reconciled. The report will list any orders with an untimely approval interval.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Delinquent Approvals</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you wish to look at a report for one cardholder,

1.  Enter a Name at the START WITH CARD HOLDER: prompt.
2.  Enter a Name at the GO TO CARD HOLDER: prompt.

If you wish to gather data on more than one cardholder, enter the Names in a range (i.e. Start With...Axxx and Go To… Mxxx).

3.  Enter a Date at the START WITH APPROVAL DATE : prompt
4.  Enter a Date at the GO TO APPROVAL DATE: prompt
5.  Enter a printer at the device prompt.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>START WITH CARD HOLDER: fcp FCP,USER</strong></p>
<p><strong>GO TO CARD HOLDER: mcgaugh IFBUYER,TWO BUY COMPUTER SPECIALIST</strong></p>
<p><strong>START WITH APPROVAL DATE: 010199 JAN 1,1999</strong></p>
<p><strong>Enter the last date for which you want to see records.</strong></p>
<p><strong>GO TO APPROVAL DATE: t MAY 12,2000</strong></p>
<p><strong>This report should be queued. It may be very large and</strong></p>
<p><strong>take a long time to generate to the printer. We suggest you</strong></p>
<p><strong>run it during off hours.</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>DELINQUENT APPROVALS EXCEPTION LISTING MAY 12, 2000@18:03:51 PAGE: 1</strong></p>
<p><strong>PURCHASE FINAL RECONCILE APPROVAL RECON TO</strong></p>
<p><strong>ORDER DATE DATE APPR INTER CARD OFFICIAL</strong></p>
<p><strong>----------------------------------------------------------------------------</strong></p>
<p><strong>CARD HOLDER: IFBUYER,NINE</strong></p>
<p><strong>999-P95304 MAR 20, 1999 APR 14, 1999 17 IFBUYER1,SEVEN</strong></p>
<p><strong>CARD HOLDER: IFBUYER1,TWO</strong></p>
<p><strong>999-P95502 AUG 20, 1999 MAY 05, 2000 185 IFBUYER,ONE</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Delinquent PC Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of delinquent Purchase Card orders. A delinquent Purchase Card order has items or services not completely received by the requested delivery date.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Delinquent PC Listing</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a printer selection at the device prompt.

This report will list each delinquent order for each Purchase Card, and compute a total for each Purchase Card.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Please enter a device for printing this report</strong></p>
<p><strong>EVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>DELINQUENT PURCHASE CARD LISTING PAGE 1</strong></p>
<p><strong>PURCHASE CARD NAME PO # STATUS DELIVERY DATE</strong></p>
<p><strong>VENDOR VENDOR PHONE</strong></p>
<p><strong>DELIVERY DATE LINE ITEM OUTSTANDING QTY ORDERED QTY OUTSTANDING</strong></p>
<p><strong>AMOUNT OUTSTANDING ITEM DESCRIPTION</strong></p>
<p><strong>BUYER: IFBUYER1,EIGHT</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>IFBUYER1,EIGHT P85556 Partial Order Received NOV 30, 1998</strong></p>
<p><strong>IFVENDOR,SIX 555-333-4444</strong></p>
<p><strong>NOV 30, 1998 1 12 2</strong></p>
<p><strong>0.20 BEANS, ITALIAN, GREEN, FROZEN, FG 3 FG</strong></p>
<p><strong>PURCHASE CARD SUBTOTAL: 0.20</strong></p>
<p><strong>Press return to continue, '^' to exit:</strong></p>
<p><strong>DELINQUENT PURCHASE CARD LISTING PAGE 2</strong></p>
<p><strong>PURCHASE CARD NAME PO # STATUS DELIVERY DATE</strong></p>
<p><strong>VENDOR VENDOR PHONE</strong></p>
<p><strong>DELIVERY DATE LINE ITEM OUTSTANDING QTY ORDERED QTY OUTSTANDING</strong></p>
<p><strong>AMOUNT OUTSTANDING ITEM DESCRIPTION</strong></p>
<p><strong>BUYER: IFBUYER1,NINE</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>IFBUYER1,NINE FISCAL P75164 Partial Order Received AUG 25, 1997</strong></p>
<p><strong> IFVENDOR3,SIX 555 777 0681</strong></p>
<p><strong>AUG 25, 1997 1 10 5</strong></p>
<p><strong>5.00 Special ITEM</strong></p>
<p><strong>PURCHASE CARD SUBTOTAL: 5.00</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Delinquent Reconciliations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will list transactions that were reconciled more than 5 days after being received in File 440.6. This report may be run for 1 cardholder or ALL cardholders, for one transaction date or a range of transaction dates and for one station or several.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>select Purchase Card Coordinator's Menu Option: Delinquent Reconciliations</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a specific cardholder’s name at the START WITH CARD HOLDER: prompt or accept the default to see all cardholders.
2.  Enter a specific date at the START WITH TRANSACTION DATE: prompt or accept the default to see all dates.
3.  Enter a specific station number at the START WITH STATION NUMBER: prompt or accept the default to see all stations.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: Delinquent Reconciliations</strong></p>
<p><strong>* Previous selection: CARD HOLDER not null</strong></p>
<p><strong>START WITH CARD HOLDER: FIRST//</strong></p>
<p><strong>* Previous selection: TRANSACTION DATE not null</strong></p>
<p><strong>START WITH TRANSACTION DATE: FIRST// 010100 (JAN 01, 2000)</strong></p>
<p><strong>GO TO TRANSACTION DATE: LAST//</strong></p>
<p><strong>* Previous selection: STATION NUMBER not null</strong></p>
<p><strong>START WITH STATION NUMBER: FIRST//</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>DELINQUENT RECONCILIATIONS EXCEPTION LISTING MAY 12,2000 18:19 PAGE 1</strong></p>
<p><strong>PAYMENT</strong></p>
<p><strong>CHARGE DATE TO</strong></p>
<p><strong>PURCHASE TRANSACTION RECEIPT RECONCILE RECONCILE</strong></p>
<p><strong>ORDER DATE DATE DATE CARD HOLDER TIMESPAN</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>999-A00032 01/06/00 01/06/00 03/10/00 IFBUYER1,FOUR 45</strong></p>
<p><strong>999-A99029 01/06/00 01/06/00 03/09/00 IFBUYER1,FOUR 44</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Fiscal Daily Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report showing buyer, vendor, and status information for Purchase Card orders within a selected date range.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Fiscal Daily Review</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the earliest date for which you want to see transactions at the Enter Beginning Date: prompt.

Enter the last date for which you want to see transactions at the Enter Ending Date: prompt.

You can include delivery orders in the report if you like.

Enter an output device. IFCAP will display the 'Fiscal Daily Review Report' on the output device you selected.

IFCAP will display the transaction in each Control Point, and list subtotals for each Control Point. After printing or displaying the report, IFCAP will return to the Purchase Card Coordinator's Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Enter beginning date: t-90 JUN 24,1996</strong></p>
<p><strong>Enter ending date: t SEP 22,1996</strong></p>
<p><strong>Do you want to see delivery orders? y YES</strong></p>
<p><strong>DEVICE: LASERDP RIGHT MARGIN: 80// 132</strong></p>
<p><strong>FISCAL DAILY REVIEW REPORT PAGE: 1</strong></p>
<p><strong>PURCHASE DATE BUYER VENDOR AMOUNT</strong></p>
<p><strong>STATUS TRANSACTION PO NUMBER</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>DATE: SEP 22, 1996 CONTROL POINT: 101</strong></p>
<p><strong>SEP 20, 1996 IFBUYER1,EIGHT IFVENDOR3,SEVEN 0.00</strong></p>
<p><strong>Ordered and Obligated 999-A61271</strong></p>
<p><strong>SEP 19, 1996 IFVENDOR3,SEVEN 4.40</strong></p>
<p><strong>Pending Contracting Offic 999-A61266</strong></p>
<p><strong>SEP 19, 1996 IFVENDOR3,SEVEN 0.00</strong></p>
<p><strong>Pending Contracting Offic 999-A61265</strong></p>
<p><strong>SEP 19, 1996 IFVENDOR3,SEVEN 0.00</strong></p>
<p><strong>Pending Contracting Offic 999-A61262</strong></p>
<p><strong>SEP 19, 1996 IFBUYER1,EIGHT IFVENDOR3,SEVEN 2.50</strong></p>
<p><strong>Ordered and Obligated 999-A61258</strong></p>
<p><strong>SEP 18, 1996 IFBUYER1,EIGHT IFVENDOR3,EIGHT 13.00</strong></p>
<p><strong>Ordered and Obligated 999-A61254</strong></p>
<p><strong>SEP 17, 1996 IFVENDOR3,SEVEN 29.40</strong></p>
<p><strong>Pending Contracting Offic 999-A61252</strong></p>
<p><strong>SEP 16, 1996 IFBUYER1,NINE IFVENDOR3,SEVEN 4.40</strong></p>
<p><strong>Pending Contracting Offic 999-A61249</strong></p>
<p><strong>SEP 13, 1996 IFVENDOR3,SEVEN 29.40</strong></p>
<p><strong>Pending Contracting Offic 999-A61244</strong></p>
<p><strong>CONTROL POINT 101 SUBTOTAL: 83.10</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## History of Purchase Card Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of Purchase Card orders sorted by the status of unpaid, paid or both, for a selected date range.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select History of Purchase Card Transactions from the Purchase Card Coordinator's Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option History of Purchase Card Transactions</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the earliest date for which you want to see transactions at the Enter Beginning Date: prompt.

Enter the last date for which you want to see transactions at the Enter Ending Date: prompt.

At the Status: prompt, enter P to limit the report to transactions that have been paid, or U to limit the report to transactions that have not been paid. Enter B to print the report with all transactions regardless of status.

Enter an output device. IFCAP will print or display the 'History Of Purchase Card Transactions Report', listing each transaction in the date range and status you selected. IFCAP sorts the report by Control Point, and lists a subtotal for each Control Point and a total for all Control Points. After printing or displaying the report, IFCAP will return to the Purchase Card Coordinator's Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Enter beginning date: t-6 SEP 16,1996</strong></p>
<p><strong>Enter ending date: t SEP 22,1996</strong></p>
<p><strong>Select one of the following:</strong></p>
<p><strong>P Paid</strong></p>
<p><strong>U Unpaid</strong></p>
<p><strong>B Both</strong></p>
<p><strong>STATUS: Both</strong></p>
<p><strong>DEVICE: LASERDP RIGHT MARGIN: 80//</strong></p>
<p><strong>HISTORY OF PURCHASE CARD TRANSACTIONS REPORT - PAID PAGE: 1</strong></p>
<p><strong>FCP PC NUMBER PURCHASE DATE BUYER VENDOR</strong></p>
<p><strong>AMOUNT COST CENTER BUDGET OBJECT CODE</strong></p>
<p><strong>FIRST LINE ITEM DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>060 P85845 MAR 10, 2000 IFBUYER1,FOUR IFVENDOR,SIX</strong></p>
<p><strong>120.12 822100 2692 Prosthetic Supplies</strong></p>
<p><strong>BATTERY AAA ALKALINE 1.5 VOLTS</strong></p>
<p><strong>Reconciled - Amended</strong></p>
<p><strong>060 B90088 MAR 10, 2000 IFBUYER1,FOUR IFVENDOR3,FIVE</strong></p>
<p><strong>54.00 822100 2631 Drugs, Medicines and Chemical Suppl</strong></p>
<p><strong>2X2 LITER CONDITIONER, 1X2 LITER BUFFER ASTRA</strong></p>
<p><strong>Reconciled</strong></p>
<p><strong>:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::</strong></p>
<p><strong>CONTROL POINT 255 SUBTOTAL: 217.44</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## IMPAC Account Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### 1ntroduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of account information stored in File 440.5 sorted by Approving Official and cardholder. The data can be selected for Active or Inactive cards or all cards.

### Menu Path 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: imPAC Account Information</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter A at the TYPE: prompt to see information on Active cards.

Enter I at the TYPE: prompt to see information on Inactive cards.

Enter B at the TYPE: prompt to see information on all cards.

Enter a printer name if you wish to have a hard copy of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: imPAC Account Information</strong></p>
<p><strong>Please select the type of Purchase Cards you wish to display:</strong></p>
<p><strong>Select one of the following:</strong></p>
<p><strong>A Active</strong></p>
<p><strong>I Inactive</strong></p>
<p><strong>B Both</strong></p>
<p><strong>TYPE: b Both</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>IMPAC ACCOUNT INFORMATION MAY 26,2000 14:10 PAGE 1</strong></p>
<p><strong>CARD HOLDER</strong></p>
<p><strong>SERVICE/SECTION MAIL CODE PHONE</strong></p>
<p><strong>SINGLE MONTHLY</strong></p>
<p><strong>PURCHASE PURCHASE</strong></p>
<p><strong>INACTIVE LIMIT LIMIT</strong></p>
<p><strong>FUND CONTROL POINT COST CENTER BUDGET OBJECT CODE</strong></p>
<p><strong>-------------------------------------------------------------------------</strong></p>
<p><strong>APPROVING OFFICIAL: IFBUYER2,TEN</strong></p>
<p><strong>PURCHASE CARD NUMBER: 6666777788889999</strong></p>
<p><strong>IFVENDOR3,NINE INFORMATION SYSTEMS CENTER 192-2 555-777-9961</strong></p>
<p><strong>NO 2000.00 10000.00</strong></p>
<p><strong>100 OPERATING EQUIPMENT</strong></p>
<p><strong>APPROVING OFFICIAL: IFBUYER2,ONE</strong></p>
<p><strong>PURCHASE CARD NUMBER: 2123436666666666</strong></p>
<p><strong>IFVENDOR4,TEN INFORMATION SYSTEMS CENTER 4273807</strong></p>
<p><strong>1200.00 12000.00</strong></p>
<p><strong>060 FISCAL SVC 842100 2121 Local Transport</strong></p>
<p><strong>PURCHASE CARD NUMBER: 7773331234567891</strong></p>
<p><strong>IFVENDOR4,ONE INFORMATION SYSTEMS CENTER 555-444-3700 3723</strong></p>
<p><strong>YES 2000.00 24000.00</strong></p>
<p><strong>120 DIET SUBSISTENCE 824300 2210 Shipment of Bod</strong></p>
<p><strong>PURCHASE CARD NUMBER: 8999999999999997</strong></p>
<p><strong>IFVENDOR4,ONE INFORMATION SYSTEMS CENTER 555-444-3700 3723</strong></p>
<p><strong>8499.99 14999.99</strong></p>
<p><strong>120 DIET SUBSISTENCE 824300 2210</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Inactivate Expired Charge Cards

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will identify and inactivate any cards that have an expiration date greater than date report is run.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Inactivate Expired Charge Cards</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter Yes at the Ready to Inactivate prompt, if you wish to automatically inactivate any cards with an expiration date that is older than the date you run the option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: inactivate Expired Charge Cards</strong></p>
<p><strong>Ready to inactivate expired charge cards before 05/26/00? NO// y YES</strong></p>
<p><strong>IFCAP INACTIVATE EXPIRED CHARGE CARDS BEFORE 05/26/00 SCHEDULED WITH TASK #184606</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Incomplete Purchase Card Orders Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of incomplete Purchase Card orders. Orders created by users (card holder or surrogate) but not approved for release from the service.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option:Incomplete Purchase Card Orders Report</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number if prompted.

Enter the fiscal year for the report.

Enter an output device for the report. IFCAP will print or display the 'Incomplete Purchase Card Orders Report' on the output device you selected. The report will list each incomplete Purchase Card order number, the date the order was created, the status of the order, the buyer of the order, and the date that the order was assigned to the buyer.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 658// SALEM, VA</strong></p>
<p><strong>Select FISCAL YEAR ('^' to EXIT): 00//</strong></p>
<p><strong>Please select a device for printing this report.</strong></p>
<p><strong>DEVICE: LAT RIGHT MARGIN: 80//</strong></p>
<p><strong>999-P05174 MAY 01, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER,TWO DVMMAY 01, 2000@12:20</strong></p>
<p><strong>999-P05170 APR 19, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER2,TWO APR 19, 2000@15:08</strong></p>
<p><strong>999-P05166 APR 13, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER,TWO DVMAPR 13, 2000@12:16</strong></p>
<p><strong>999-P05162 APR 05, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER2,TWO APR 05, 2000@07:18</strong></p>
<p><strong>999-P05159 APR 04, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER,NINE APR 04, 2000@17:48</strong></p>
<p><strong>999-P05142 MAR 23, 2000 Pending Contracting Officers Signature</strong></p>
<p><strong>IFBUYER2,TWO MAR 23, 2000@14:31</strong></p>
<p><strong>999-P05136 MAR 21, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER2,TWO MAR 21, 2000@17:13</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Print Unregistered Credit Card Charges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will identify any charge entry in File 440.6 that does not have a corresponding credit card entry in File 440.5.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Print Unregistered Credit Card Charges</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a printer name if you would like a hard copy of this report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: print Unregistered Credit Card C</strong></p>
<p><strong>harges</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>Unregistered Credit Card Charges MAY 26,2000 14:42 PAGE 1</strong></p>
<p><strong>Credit Card # PO Date Vendor</strong></p>
<p><strong>P.O. # TXN Ref Charge $AMT</strong></p>
<p><strong>Charge Id TXN DATE STATUS</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>4716360000143798 MAY 17,1996 IFVENDOR4,TWO</strong></p>
<p><strong>~ A2433500614338714233732 220.99</strong></p>
<p><strong>C65861470005001 MAY 28,1996 NONE</strong></p>
<p><strong>4716360000143822 MAY 20,1996 IFVENDOR4,THREE</strong></p>
<p><strong>~ N2460600614204000041742 249.61</strong></p>
<p><strong>C65861470006001 MAY 28,1996 NONE</strong></p>
<p><strong>4716360000144499 APR 30,1996 IFVENDOR4,FOUR</strong></p>
<p><strong>~ A55122001285 104.72</strong></p>
<p><strong>C65861470007001 MAY 28,1996 NONE</strong></p>
<p><strong>4716360000144754 MAY 21,1996 1SALEM OFF SUPPLY INC</strong></p>
<p><strong>~ A2433500614438714436905 29.10</strong></p>
<p><strong>C65861470008001 MAY 28,1996 NONE</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Purchase Card exceptions/replacements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow users to print exceptions/replacements reports previously run through the Fileman print option.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Purchase Card exceptions/replacements</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  For the report - ALL Citibank cards with No US Bank replacement \#
2.  For the report - Active Citibank cards with No US Bank replacement \#
3.  For the report - Inactive Citibank cards with US Bank replacement \#

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: CCEX Purchase Card exceptions/</strong></p>
<p><strong>replacements</strong></p>
<p><strong>Select STATION NUMBER ('^' TO EXIT): 552// DAYTON</strong></p>
<p><strong>Select one of the following:</strong></p>
<p><strong>1 ALL Citibank cards with No US Bank replacement #</strong></p>
<p><strong>2 Active Citibank cards with No US Bank replacement #</strong></p>
<p><strong>3 Inactive Citibank cards with US Bank replacement #</strong></p>
<p><strong>Type of Report://</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Purchase Card Information List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report can be run for a range of cardholders or all cardholders. It will list the cardholder, the card name, Approving and Alternate Approving Officials, and surrogates.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Purchase Card Information List</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a cardholder - Last Name, First Name at the prompt START WITH CARD HOLDER: FIRST// if you wish to run the report for only certain cardholders.

Accept the default value of FIRST and LAST if you wish to run the report for ALL cardholders.

Enter a printer name if you want a hard copy of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: Purchase Card Information List</strong></p>
<p><strong>START WITH CARD HOLDER: FIRST// IFBUYER,NINE</strong></p>
<p><strong>GO TO CARD HOLDER: LAST// IFBUYER1,TWO</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>PURCHASE CARD INFORMATION LIST MAY 26,2000 14:50 PAGE 1</strong></p>
<p><strong>CARD HOLDER PC CARD NAME APP OFFICIAL ALT OFFICIAL</strong></p>
<p><strong>SURROGATE USER</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>IFBUYER,NINE BUY VOL SVC IFBUYER2,FOUR IFBUYER2,FIVE</strong></p>
<p><strong>IFBUYER,NINE</strong></p>
<p><strong>IFBUYER2,THREE</strong></p>
<p><strong>IFBUYER1,TWO IFBUYER1,TWO IFBUYER1,THREE IFBUYER1,EIGHT</strong></p>
<p><strong>IFBUYER1,TWO</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Purchase Card Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 'Purchase Card Registration' option is designed for the exclusive use of the Purchase Card Coordinator. Purchase Card Users will have the capability to display their own information from this file but will not be able to view data on other Purchase Card users. There will be times when either the Approving Official is not available or the Approving Official must complete the reconciliation process for his/her user. In those instances, another (Alternate) Approving Official would be required to approve a reconciliation done by the Approving Official.

The posting of card registration information to File 440.5 is expected to be done automatically based on transmission of the data from the credit card Vendor to Austin and then to IFCAP. In the event of a problem with the timely transmission of data, the coordinator will be able to enter data manually if necessary.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Purchase Card Registration</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number if prompted.

Enter the Purchase Card number. The Purchase Card number is the account number on the Purchase Card.

Enter the name of the Purchase Card Holder or enter a question mark to see a list of all the users in the New Person File.

Enter a name for the Purchase Card.

Enter the expiration date of the card.

Enter Yes if you wish to Inactivate the card.

Enter the Fund Control Point that will fund the Purchase Card. Cardholder must have at a minimum, Requestor level access in the Fund Control Point.

Enter the Cost Center. Cost centers allow Fiscal staff to create total expense records for a section or service.

Enter the Budget Object Code for the Purchase Card or enter a question mark to see a list of the available Budget Object Codes for the Cost Center.

Enter the maximum amount per purchase at the Single Purchase Limit: prompt.

Enter the maximum total expense per monthly statement at the Monthly Purchase Limit: prompt.

At the Delivery Location: prompt, enter the location of delivery.

Enter the Approving Official that will approve a reconciliation for the new Purchase Card at the Approving Official: prompt or enter a question mark to see a list of the valid Approving Officials. IFCAP will not allow you to enter the Purchase Card User as the Approving Official for the same card. Approving Official must have, at a minimum, Requestor Level access to the Fund Control Point.

Enter the Alternate Approving Official that will approve a reconciliation for the new Purchase Card at the Alternate Approving Official: prompt or enter a question mark to see a list of the valid Alternate Approving Officials. Alternate Approving Official must have, at a minimum, Requestor Level access to the Fund Control Point.

Enter the Purchase Card User Surrogate that can enter or edit Purchase Card orders for the Purchase Card User at the Purchase Card User Surrogate: prompt. A surrogate will not be allowed to reconcile Purchase Card orders. Surrogate must have, at a minimum, Requestor Level access to the Fund Control Point.

Enter the Replaced Card: *number*. This ensures a link between the new card and the replaced card for charge reconciliation crossovers on old orders against replaced cards when charges come through under the new card number. This 'REPLACED CARD' number MUST be a valid card number, inactive, not used as a replacement card for another card and match the new card for the following fields: CARD HOLDER, STATION NUMBER, FUND CONTROL POINT, COST CENTER and BUDGET OBJECT CODE.

Enter Y at the Would you like to register another Purchase Card?: prompt to enter another Purchase Card number for the Purchase Card User, or press \<Enter\> to return to the Purchase Card Coordinator's Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>Select PURCHASE CARD INFORMATION PURCHASE CARD NUMBER: 4486760000843213</strong></p>
<p><strong>Are you adding '4486760000843213' as</strong></p>
<p><strong>a new PURCHASE CARD INFORMATION? No// Y (Yes)</strong></p>
<p><strong>PURCHASE CARD INFORMATION CARD HOLDER: IFBUYER,TWO IBT</strong></p>
<p><strong>COMPUTER SPECIALIST</strong></p>
<p><strong>PURCHASE CARD INFORMATION PURCHASE CARD NAME: IFVENDOR4,FIVE</strong></p>
<p><strong>PURCHASE CARD NUMBER: 4486760000843213// (No Editing)</strong></p>
<p><strong>EXPIRATION DATE: 01012005 (JAN 01, 2005)</strong></p>
<p><strong>INACTIVATE CARD?:</strong></p>
<p><strong>CARD HOLDER: IFBUYER,TWO//</strong></p>
<p><strong>COMMERCIAL PHONE: 555-777-6357//</strong></p>
<p><strong>FUND CONTROL POINT: 060 Fiscal Service 0160A1 10 0100 010042100</strong></p>
<p><strong>COST CENTER: 842100 Fiscal test for tampa</strong></p>
<p><strong>BUDGET OBJECT CODE: 2660 Operating Supplies and Materials</strong></p>
<p><strong>PC USER SINGLE PURCHASE LIMIT: 1000</strong></p>
<p><strong>MONTHLY PURCHASE LIMIT: 10000</strong></p>
<p><strong>DELIVERY LOCATION: BDL3 RM5</strong></p>
<p><strong>APPROVING OFFICIAL: IFBUYER,NINE IBN COMPUTER SYSTEMS ANALYST</strong></p>
<p><strong>ALTERNATE APPROVING OFFICIAL: IFCABUYER</strong></p>
<p><strong>1 IFBUYER2,SIX IBS PROGRAM ANALYST</strong></p>
<p><strong>2 IFBUYER1,THREE IBT COMPUTER SYSTEMS ANALYST</strong></p>
<p><strong>CHOOSE 1-2: 2 IFBUYER1,THREE IBT COMPUTER SYSTEMS ANALYST</strong></p>
<p><strong>PURCHASE CARD NAME: IFVENDOR4,FIVE //</strong></p>
<p><strong>Select SURROGATE USER: IFBUYER2,SEVEN IB COMPUTER SYSTEMS ANALYS</strong></p>
<p><strong>T</strong></p>
<p><strong>Are you adding 'IFBUYER2,SEVEN' as a new SURROGATE USER? No// Y (Yes)</strong></p>
<p><strong>Select SURROGATE USER:</strong></p>
<p><strong>Replaced Card: 1234567890123456</strong></p>
<p><strong>Would you like to register another Purchase Card? No// (No)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Purchase Card Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of totals for each Purchase Card and each control point, and the percentage of Purchase Card orders for each control point. You can select a date range for the report. The report will generate statistics for all Purchase Card orders for the station for the date range you selected, sorted by Control Point. The report also shows the average dollar cost per card in the Control Point, and the average number of line items on each card. It also shows the percentage of Purchase Card orders for all orders for each Control Point.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Purchase Card Statistics</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number if prompted.

Enter the first date for the report at the Enter Beginning Date: prompt.

Enter the last date for the report at the Enter Ending Date: prompt.

Enter an output device. IFCAP will print or display the 'Purchase Card Statistics Report' on the output device you selected. After printing or displaying the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>Enter beginning date: 010100 JAN 1,2000</strong></p>
<p><strong>Enter ending date: t MAY 26,2000</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>PURCHASE CARD STATISTICS REPORT MAY 26, 2000@18:04:01 PAGE: 1</strong></p>
<p><strong>PURCHASE CARD NAME PO # LINE ITEMS AMOUNT DATE PLACED</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>::::::::::::::::::::::::::::::::::::::::::</strong></p>
<p><strong>FCP: 60 BUYER: IFBUYER2,EIGHT</strong></p>
<p><strong>060 Fiscal Service P05117 2 25.00 MAR 03, 2000</strong></p>
<p><strong>AVERAGE DOLLAR COST FOR CARD: $25.00</strong></p>
<p><strong>AVERAGE LINE COUNT FOR CARD: 2.00</strong></p>
<p><strong>:::::::::::::::::::::::::::::::::::::</strong></p>
<p><strong>FCP: 4537 BUYER: IFBUYER1,FIVE</strong></p>
<p><strong>300 IFVENDOR4,SIX P95032 2 26.40 FEB 23, 2000</strong></p>
<p><strong>AVERAGE DOLLAR COST FOR CARD: $26.40</strong></p>
<p><strong>AVERAGE LINE COUNT FOR CARD: 2.00</strong></p>
<p><strong>:::::::::::::::::::::::::::::::</strong></p>
<p><strong>% OF PC ORDERS FOR CP 7101: 100.000</strong></p>
<p><strong>PC ORDER COUNT: 5 TOTAL ORDER COUNT: 5</strong></p>
<p><strong>PC SUBTOTAL: 1028.00</strong></p>
<p><strong>STATION GRAND TOTAL: 14426.31</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Purchase Card Timely Commitment Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report lists the time elapsed from order creation through reconciliation.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Purchase Card Timely Commitment Report</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a specific cardholder’s name at both the START WITH Purchase Card Holder: prompt and the GO TO PURCHASE CARD HOLDER: prompt if you wish to view data for a specific cardholder. Accept the default values of FIRST and LAST if you wish to view data for all cardholders.

You may enter a specific date if you wish to view data for a specific time frame or accept the default value of FIRST to view data for all dates.

Enter a printer name if you wish to print a hard copy of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: PURCHASE CARD Timely Commitment</strong></p>
<p><strong>Report</strong></p>
<p><strong>* Previous selection: PURCHASE CARD HOLDER not null</strong></p>
<p><strong>START WITH PURCHASE CARD HOLDER: FIRST// IFBUYER,SIX</strong></p>
<p><strong>GO TO PURCHASE CARD HOLDER: LAST// IFBUYER1,TWO</strong></p>
<p><strong>* Previous selection: VALIDATION DATE/TIME not null</strong></p>
<p><strong>START WITH VALIDATION DATE/TIME: FIRST//</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>PURCHASE CARD TIMELY COMMITMENT REPORT MAY 30,2000 10:25 PAGE 1</strong></p>
<p><strong>INCEPTION COMMITMENT</strong></p>
<p><strong>PURCHASE PURCHASE TO TO</strong></p>
<p><strong>ORDER ORDER DATE DATE COMMITMENT RECONCILE</strong></p>
<p><strong>NUMBER DATE SIGNED RECONCILED (DAYS) (DAYS)</strong></p>
<p><strong>CARD HOLDER</strong></p>
<p><strong>---------------------------------------------------------------------------</strong></p>
<p><strong>999-P05306 05/18/00 05/18/00 0</strong></p>
<p><strong>IFBUYER1,EIGHT</strong></p>
<p><strong>999-P05316 05/20/00 05/20/00 0</strong></p>
<p><strong>IFBUYER1,EIGHT</strong></p>
<p><strong>999-P05319 05/20/00 05/20/00 05/20/00 0 0</strong></p>
<p><strong>IFBUYER1,EIGHT</strong></p>
<p><strong>999-P05321 05/20/00 05/20/00 0</strong></p>
<p><strong>IFBUYER1,EIGHT</strong></p>
<p><strong>999-P05345 06/08/00 06/08/00 06/12/00 0 4</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Reconciled Purchase Card Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of reconciled Purchase Card orders. The report is sorted by card holder and displays the Vendor, status of the order, charge reference number, Amount reconciled, charge Vendor and if amount reconciled was identified as the Final Charge.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Reconciled Purchase Card Transactions</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number if prompted.

Enter the first date that you want IFCAP to use for the report at the Enter Beginning Date: prompt.

Enter the last date that you want IFCAP to use for the report at the Enter Ending Date: prompt.

Enter an output device. IFCAP will display or print the 'Reconciled Purchase Card Orders' report, using the output device you selected. The report lists each reconciled Purchase Card order, sorted by buyer.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>Enter beginning date: 120199 DEC 1,1999</strong></p>
<p><strong>Enter ending date: 013000 JAN 30,2000</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>RECONCILED PURCHASE CARD ORDERS MAY 30, 2000@10:39:28 PAGE 1</strong></p>
<p><strong>P.O. DATE DATE RECONCILED ORDER # $AMT TYPE(S/D)</strong></p>
<p><strong>VENDOR DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>DOC-REF # RECONCILED $AMT RECONCILE VENDOR FINAL CHARGE</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>BUYER: IFBUYER1,FOUR</strong></p>
<p><strong>JAN 27, 2000 JAN 27, 2000 999-P85707 9.00 DETAILED</strong></p>
<p><strong>IFVENDOR,SIX COVER ARMBOARD 9 INCH</strong></p>
<p><strong>Reconciled</strong></p>
<p><strong>C-999000P85707 9.00 IFVENDOR,SIX YES</strong></p>
<p><strong>RECONCILED SUBTOTAL - $9.00</strong></p>
<p><strong>JAN 27, 2000 JAN 27, 2000 999-P85706 1.00 SIMPLIFIED</strong></p>
<p><strong>IFVENDOR3,TWO TESTING PRCH1A3, 1/27/00</strong></p>
<p><strong>Reconciled</strong></p>
<p><strong>C-999000P85706 1.00 SIMPLIFIED YES</strong></p>
<p><strong>RECONCILED SUBTOTAL - $1.00</strong></p>
<p><strong>JAN 14, 1999 DEC 17, 1999 999-P95193 59.94</strong></p>
<p><strong>IFVENDOR,SIX WHITE AND RED MARBLES.</strong></p>
<p><strong>Reconciled - Amended</strong></p>
<p><strong>C-999000P95193 58.74 IFVENDOR,SIX YES</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Retrieve Unregistered Credit Card Charges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will enable the user to identify any charges that exist in File 440.6, but do not have a corresponding credit card entry in File 440.5. This option is used with the option Charge Card Reg. Exception. After correcting exception entries, this option will link the entry in 440.6 to the Cardholder.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Retrieve Unregistered Credit Card Charges</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Accept the default value if you are ready to retrieve any unregistered Purchase Card charges.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Ready to Retrieve Unregistered Purchase Card Charges? YES//</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Summary Report of Unpaid PC Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report showing the unpaid Purchase Card order total for each control point.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Summary Report of Unpaid PC Transactions</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a printer name if you want a hard copy of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: summary Report of Unpaid PC Tran</strong></p>
<p><strong>sactions</strong></p>
<p><strong>Please select a device for display/print of this report.</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>UNPAID PURCHASE CARD TRANSACTION BY FCP - SUMMARY PAGE 1</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>CONTROL POINT: 20 TOTAL: $11237.00</strong></p>
<p><strong>CONTROL POINT: 36 TOTAL: $90.50</strong></p>
<p><strong>CONTROL POINT: 40 TOTAL: $337.76</strong></p>
<p><strong>CONTROL POINT: 45 TOTAL: $700.78</strong></p>
<p><strong>CONTROL POINT: 60 TOTAL: $51576.69</strong></p>
<p><strong>CONTROL POINT: 76 TOTAL: $2595.20</strong></p>
<p><strong>CONTROL POINT: 86 TOTAL: $267.45</strong></p>
<p><strong>CONTROL POINT: 88 TOTAL: $1004.27</strong></p>
<p><strong>CONTROL POINT: 100 TOTAL: $1612.25</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Unapproved Reconciliations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a report of reconciled Purchase Card orders that have not been approved by an official, sorted by approving official, control point, and cardholder.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Unapproved Reconciliations</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date you wish to begin displaying data for.

Enter the date the ending date for the data you wish to display.

You may display data for a specific approving official by entering NO at the Do you want to include all officials in this report: prompt. A yes will generate the report for ALL the approving officials.

Enter a printer name if you want to print a hard copy of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Enter beginning date: 070199 JUL 1,1999</strong></p>
<p><strong>Enter ending date: 093099 SEP 30,1999</strong></p>
<p><strong>Do you want to include all officials in this report? NO</strong></p>
<p><strong>Select NEW PERSON NAME: IFCAPB</strong></p>
<p><strong>1 IFBUYER2,SIX AR PROGRAM ANALYST</strong></p>
<p><strong>2 IFBUYER1,THREE CR COMPUTER SYSTEMS ANALYST</strong></p>
<p><strong>CHOOSE 1-2: 2 IFBUYER1,THREE CR COMPUTER SYSTEMS ANALYST</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>UNAPPROVED RECONCILIATION REPORT MAY 30, 2000 PAGE: 1</strong></p>
<p><strong>PURCHASE DATE PC ORDER # CARDHOLDER FCP AMOUNT</strong></p>
<p><strong>DATE RECONCILED</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>APPROVING OFFICIAL: IFBUYER1,THREE</strong></p>
<p><strong>SEP 30, 1999 662-P90003 IFBUYER1,FIVE 045 IFVENDOR4,SEVEN 25.50</strong></p>
<p><strong>SEP 30, 1999</strong></p>
<p><strong>JUL 29, 1999 662-P99001 IFBUYER1,FIVE 045 IFVENDOR4,SEVEN 35.40</strong></p>
<p><strong>JUL 29, 1999</strong></p>
<p><strong>JUL 27, 1999 999-P90015 IFBUYER1,FOUR 255 IFVENDOR4,EIGHT 17.40</strong></p>
<p><strong>DEC 22, 1999</strong></p>
<p><strong>JUL 12, 1999 999-P95393 IFBUYER1,FOUR 255 IFVENDOR4,EIGHT 21.00</strong></p>
<p><strong>JUL 12, 1999</strong></p>
<p><strong>UNAPPROVED RECONCILIATION REPORT MAY 30, 2000 PAGE: 2</strong></p>
<p><strong>PURCHASE DATE PC ORDER # CARDHOLDER FCP AMOUNT</strong></p>
<p><strong>DATE RECONCILED</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>APPROVING OFFICIAL: IFBUYER1,THREE</strong></p>
<p><strong>SEP 20, 1999 999-B90042 IFBUYER1,FOUR 300 IFVENDOR4,SIX 12.00</strong></p>
<p><strong>OCT 06, 1999</strong></p>
<p><strong>JUL 28, 1999 999-B90013 IFBUYER1,FOUR 300 IFVENDOR4,SIX 69.00</strong></p>
<p><strong>DEC 23, 1999</strong></p>
<p><strong>SEP 30, 1999 662-G90003 IFBUYER1,FIVE 4537 IFVENDOR4,NINE 52.50</strong></p>
<p><strong>SEP 30, 1999</strong></p>
<p><strong>SEP 29, 1999 662-G90001 IFBUYER1,FIVE 4537 IFVENDOR4,NINE 57.00</strong></p>
<p><strong>SEP 29, 1999</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Unreconciled Austin Payment Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print payment transaction data that have not been reconciled to a Purchase Card order.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Unreconciled Austin Payment Transactions</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you want to see the data for ALL cardholders accept the default of FIRST at the START WITH CARD HOLDER: FIRST// prompt.

If you want to see data for a specific cardholder, enter the cardholder’s name at the START WITH CARD HOLDER: FIRST// prompt.

Enter the name of the last cardholder you want to see data for at the GO TO CARD HOLDER: LAST// prompt.

Enter an output device. IFCAP will print or display the 'UNRECONCILED AUSTIN PAYMENT TRANSACTIONS' report on the output device you selected.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Coordinator's Menu Option: Unreconciled Austin Payment Transactions</strong></p>
<p><strong>START WITH CARD HOLDER: FIRST// IFBUYER1,FOUR</strong></p>
<p><strong>GO TO CARD HOLDER: LAST// IFBUYER1,FOUR</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>UNRECONCILED AUSTIN PAYMENT TRANSACTIONS MAY 30,2000 11:47 PAGE 1</strong></p>
<p><strong>TRANSACTION</strong></p>
<p><strong>CARD HOLDER DATE AMOUNT</strong></p>
<p><strong>MERCHANT NAME ORACLE DOCUMENT ID</strong></p>
<p><strong>------------------------------------------------------------------------------</strong></p>
<p><strong>IFBUYER1,FOUR OCT 28,1999 25.20</strong></p>
<p><strong>IFVENDOR2,SEVEN C-9990000P95669</strong></p>
<p><strong>IFBUYER1,FOUR OCT 28,1999 2.00</strong></p>
<p><strong>IFVENDOR5,TEN C-9990000P95670</strong></p>
<p><strong>IFBUYER1,FOUR OCT 28,1999 10.00</strong></p>
<p><strong>IFVENDOR5,ONE C-9990000P95671</strong></p>
<p><strong>:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;</strong></p>
<p><strong>TOTAL 98345.80 37.50</strong></p>
<p><strong>COUNT 248 3</strong></p>
<p><strong>MEAN 396.56 12.50</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Unreconciled Purchase Card Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of Purchase Card orders that have not been reconciled to a charge.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Registration</strong></p>
<p><strong>Purchase Card exceptions/replacements</strong></p>
<p><strong>Charge Card Reg. Exception</strong></p>
<p><strong>Inactivate Expired Charge Cards</strong></p>
<p><strong>Austin Audit Information</strong></p>
<p><strong>Coordinator Approving Official Charge Audit</strong></p>
<p><strong>Daily Charge Transmission Log</strong></p>
<p><strong>Delinquent Approvals</strong></p>
<p><strong>Delinquent PC Listing</strong></p>
<p><strong>Delinquent Reconciliations</strong></p>
<p><strong>Fiscal Daily Review</strong></p>
<p><strong>History of Purchase Card Transactions</strong></p>
<p><strong>IMPAC Account Information</strong></p>
<p><strong>Incomplete Purchase Card Orders Report</strong></p>
<p><strong>Print Unregistered Credit Card Charges</strong></p>
<p><strong>Purchase Card Information List</strong></p>
<p><strong>Purchase Card Statistics</strong></p>
<p><strong>Purchase Card Timely Commitment Report</strong></p>
<p><strong>Reconciled Purchase Card Transactions</strong></p>
<p><strong>Retrieve Unregistered Credit Card Charges</strong></p>
<p><strong>Summary Report of Unpaid PC Transactions</strong></p>
<p><strong>Unapproved Reconciliations</strong></p>
<p><strong>Unreconciled Austin Payment Transactions</strong></p>
<p><strong>Unreconciled Purchase Card Transactions</strong></p>
<p><strong>Select Purchase Card Coordinator's Menu Option: Unreconciled Purchase Card Transactions</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number if prompted.

Enter the earliest date that you want IFCAP to use for the report at the Enter Beginning Date: prompt.

Enter the last date that you want IFCAP to use for the report at the Enter Ending Date: prompt.

Enter an output device. IFCAP will display or print the 'Unreconciled Purchase Card Orders' report on the output device you selected. The report lists the P.O. Date, order number, amount, order type, vendor, description of first line item, status, comments and buyer of each unreconciled Purchase Card order, sorted by buyer.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>Enter beginning date: 100199 OCT 1,1999</strong></p>
<p><strong>Enter ending date: t MAY 30,2000</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>UNRECONCILED PURCHASE CARD ORDERS MAY 30, 2000@12:02:32 PAGE 1</strong></p>
<p><strong>P.O. DATE ORDER # $AMT TYPE(S/D)</strong></p>
<p><strong>VENDOR DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>BUYER: IFBUYER,NINE</strong></p>
<p><strong>DEC 06, 1999 999-P05029 48.00 DETAILED</strong></p>
<p><strong>IFVENDOR2,TEN Diaper, large</strong></p>
<p><strong>Complete Order Received</strong></p>
<p><strong>Just testing</strong></p>
<p><strong>APR 04, 2000 999-P05160 165.00 DETAILED</strong></p>
<p><strong>IFVENDOR5,TWO NEEDLE JAMSHIDI BONE MARROW 11GA X</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>Test Detailed Purchase Card Order</strong></p>
<p><strong>BUYER SUBTOTAL - $213.00</strong></p>
<p><strong>UNRECONCILED PURCHASE CARD ORDERS MAY 30, 2000@12:02:32 PAGE 2</strong></p>
<p><strong>P.O. DATE ORDER # $AMT TYPE(S/D)</strong></p>
<p><strong>VENDOR DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>BUYER: IFBUYER1,TWO</strong></p>
<p><strong>NOV 15, 1999 999-P05011 12.00 SIMPLIFIED</strong></p>
<p><strong>IFVENDOR,SIX TEST</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>NOV 19, 1999 999-P05027 144.00</strong></p>
<p><strong>IFVENDOR,SIX SHAVING KIT, SURGICAL PREPARATION.</strong></p>
<p><strong>Paid (Not Received)</strong></p>
<p><strong>NOV 19, 1999 999-P90022 144.00</strong></p>
<p><strong>IFVENDOR,SIX SHAVING KIT, SURGICAL PREPARATION.</strong></p>
<p><strong>Paid (Not Received)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Supplemental Purchase Card Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter explains several options from the IFCAP Purchase Card Menu that were not explained in the previous chapters.

## Amendment to Purchase Card Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to make changes to a Purchase Card order after the Purchase Card User has authorized the order with their electronic signature code.

### Amendment types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There will be times when it will be necessary to amend a Purchase Card order. Purchase card order amendments will be allowed for the following:

- LINE ITEM ADD: This amendment adds a line item to the Purchase Card order. Purchase Card Users can only add line items on Detailed Purchase Card Orders.
- LINE ITEM DELETE: This amendment deletes a line item to the Purchase Card order. Purchase Card Users can only delete line items on Detailed Purchase Card Orders.
- LINE ITEM EDIT: This amendment edits a line item on the Purchase Card order. Purchase Card Users can only edit line items on Detailed Purchase Card Orders.
- FCP CHANGE (Limited to authorized buyer information/list.) This amendment changes the Fund Control Point on a Purchase Card order.
- VENDOR CHANGE: This amendment changes the vendor on a Purchase Card order.
- CANCEL P/C ORDER: This amendment cancels a Purchase Card order.
- F.O.B. EDIT: This amendment changes the Freight On Board charges from Origin to Destination or vice versa. Purchase Card Users can only change Freight on Board charges on Detailed Purchase Card Orders.

### Order Status after Amendment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon approval of the amendment, IFCAP will permit the user to select the appropriate status for the document. Status selection offered will depend on what the status was, when the user started the amendment. The following is a partial list of possible choices:

- Cancelled Order
- Complete Order Received (Amended)
- Ordered (No Fiscal Action)-Amended
- Partial Order Received (Amended)
- Partial Payment (Not Received) - Amended
- Transaction Complete (Amended)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Reports Menu ...</strong></p>
<p><strong>Approving Official Menu ...</strong></p>
<p><strong>Process Purchase Card Menu ...</strong></p>
<p><strong>Purchase Card Display/Print Menu ...</strong></p>
<p><strong>Reconciliation Menu ...</strong></p>
<p><strong>Select Purchase Card Menu Option: Process Purchase Card Menu</strong></p>
<p><strong>New Simplified Purchase Card Order</strong></p>
<p><strong>Edit Simplified Purchase Card Order</strong></p>
<p><strong>New Detailed Purchase Card Order</strong></p>
<p><strong>Edit Detailed Purchase Card Order</strong></p>
<p><strong>Amendment To Purchase Card Order</strong></p>
<p><strong>Adjustment Voucher To Purchase Card Order</strong></p>
<p><strong>Receive Purchase Card Order</strong></p>
<p><strong>Item Display</strong></p>
<p><strong>Vendor Display</strong></p>
<p><strong>Create P/C Order From Repetitive Item List</strong></p>
<p><strong>Convert P/C Order To 2237 Request</strong></p>
<p><strong>Convert P/C Order to a Delivery Order</strong></p>
<p><strong>Cancel An Incomplete PC Order</strong></p>
<p><strong>Convert Temporary 2237 to PC Request</strong></p>
<p><strong>Select Process Purchase Card Menu Option: Amendment To Purchase Card Order</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a station number if prompted.
2.  Enter a Purchase Card order number or enter two question marks to see a list of available purchase orders. If there is an amendment pending for the purchase order, IFCAP will ask you if you want to edit it. If no amendment is pending IFCAP will assign an amendment number for this transaction.
3.  At the Effective Date: prompt, enter the date that the amendment will take effect, or press \<Enter\> to accept the default of today's date.
4.  At the Authority: prompt, enter the authority by which you amend the Purchase Card order. If you do not know the applicable authorization, enter two question marks and IFCAP will list the available authority categories. Press \<Enter\> to accept the default value of “D”. If you are canceling the order, change the value to “E”.
5.  Enter comments about the amendment if you like at the Type Comments: prompt.
6.  At the Contractor Required To Sign?: prompt, enter Y if the contractor has to sign the amendment showing that they accept the terms of the amendment.
7.  IFCAP will display a list of the amendment types you can create. At the Type Of Amendment Number: prompt, enter the number corresponding to the type of amendment you want to create.
8.  IFCAP will display the edit prompt(s) that correspond to the amendment type you selected.
9.  If you would like to amend the Purchase Card order in another way, enter another amendment type at the Select Type Of Amendment Number: prompt.
10. You may enter the new status of the Purchase Card order at the Amendment/Adjustment Status: prompt or enter a question mark to see a list of valid status.
11. Enter a justification for the amendment. You may review the amendment if you like.
12. If you entered Y at the Review Amendment?: prompt, IFCAP will display the amendment on the screen.
13. If you are satisfied with the amendment, enter Y at the Approve and print Amendment number (#)?: prompt.
14. Enter your electronic signature code.
15. At the Queue On Device: prompt, enter the output device for the amendment. IFCAP will print the amendment on the output device you selected.
16. Enter another station number if prompted, to amend another Purchase Card order, or enter a caret (^) to return to the Process Purchase Card Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>PURCHASE ORDER: ??</strong></p>
<p><strong>^</strong></p>
<p><strong>PURCHASE ORDER: P0501</strong></p>
<p><strong>1 P05011 999-P05011 11-15-99 PC Ordered (No Fiscal Action Required</strong></p>
<p><strong>FCP: 060 $ 12.00</strong></p>
<p><strong>2 P05012 999-P05012 11-15-99 PC Order Not Completely Prepared</strong></p>
<p><strong>FCP: 060 $ 15.00</strong></p>
<p><strong>3 P05013 999-P05013 11-15-99 PC Order Not Completely Prepared</strong></p>
<p><strong>FCP: 060 $ 0.00</strong></p>
<p><strong>4 P05014 999-P05014 11-15-99 PC Order Not Completely Prepared</strong></p>
<p><strong>FCP: 060 $ 12.00</strong></p>
<p><strong>5 P05015 999-P05015 11-15-99 PC Order Not Completely Prepared</strong></p>
<p><strong>FCP: 060 $ 12.00</strong></p>
<p><strong>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</strong></p>
<p><strong>CHOOSE 1-5: 1 999-P05011 11-15-99 PC Ordered (No Fiscal Action Required</strong></p>
<p><strong>FCP: 060 $ 12.00</strong></p>
<p><strong>Amendment Number: 1</strong></p>
<p><strong>...copying Purchase Order into work file...</strong></p>
<p><strong>...EXCUSE ME, HOLD ON...</strong></p>
<p><strong>EFFECTIVE DATE: TODAY// (JUN 01, 2000)</strong></p>
<p><strong>AUTHORITY: D// OTHER (specify type of modification and authority)</strong></p>
<p><strong>TYPE COMMENTS:</strong></p>
<p><strong>CONTRACTOR REQUIRED TO SIGN?: NO// NO</strong></p>
<p><strong>Select one of the following:</strong></p>
<p><strong>1 F.C.P. Edit</strong></p>
<p><strong>2 Change VENDOR</strong></p>
<p><strong>3 AUTHORITY Edit</strong></p>
<p><strong>4 LINE ITEM Edit</strong></p>
<p><strong>Select TYPE OF AMENDMENT NUMBER: 4 LINE ITEM Edit</strong></p>
<p><strong>...HMMM, JUST A MOMENT PLEASE...</strong></p>
<p><strong>Select ITEM: 1 TEST</strong></p>
<p><strong>ITEM MASTER FILE NO.:</strong></p>
<p><strong>DESCRIPTION:</strong></p>
<p><strong>1&gt;TEST</strong></p>
<p><strong>EDIT Option:</strong></p>
<p><strong>QUANTITY: 1// 2</strong></p>
<p><strong>UNIT OF PURCHASE: EA//</strong></p>
<p><strong>ACTUAL UNIT COST: $12.0000// 11.50</strong></p>
<p><strong>PACKAGING MULTIPLE: 1//</strong></p>
<p><strong>UNIT CONVERSION FACTOR: 1//</strong></p>
<p><strong>VENDOR STOCK NUMBER:</strong></p>
<p><strong>FSC/PSC: 9999//</strong></p>
<p><strong>CONTRACT/BOA #:</strong></p>
<p><strong>BOC: 2660 Operating Supplies and Materials Replace</strong></p>
<p><strong>Select one of the following:</strong></p>
<p><strong>1 F.C.P. Edit</strong></p>
<p><strong>2 Change VENDOR</strong></p>
<p><strong>3 AUTHORITY Edit</strong></p>
<p><strong>4 LINE ITEM Edit</strong></p>
<p><strong>Select TYPE OF AMENDMENT NUMBER:</strong></p>
<p><strong>AMENDMENT/ADJUSTMENT STATUS: Ordered (No Fiscal Action)-Amended</strong></p>
<p><strong>// 23</strong></p>
<p><strong>JUSTIFICATION: tst</strong></p>
<p><strong>Review Amendment ? YES// (YES)</strong></p>
<p><strong>2. MOD. NO.: | 3. EFFECTIVE DATE: | 4. REQUISITION/P.O. REQ. NO.:</strong></p>
<p><strong>1 | 6/1/2000 | 999-00-1-060-0053/P05011</strong></p>
<p><strong>_______________________________________________________________________________</strong></p>
<p><strong>8. NAME AND ADDRESS OF CONTRACTOR | 10A. MODIFICATION OF CONTRACT/ORDER</strong></p>
<p><strong>IFVENDOR,SIX | NO. 999-P05011</strong></p>
<p><strong>1000 S BOULEVARD |______________________________________</strong></p>
<p><strong>SUITE 100 | 10B. DATED (See Item 13) 11/15/1999</strong></p>
<p><strong>ROOM 100, POD 12 |</strong></p>
<p><strong>ANYTOWN, GA 00001 |</strong></p>
<p><strong>_______________________________________________________________________________</strong></p>
<p><strong>12. ACCOUNTING AND APPROPRIATION DATA (If required)</strong></p>
<p><strong>Increase 3600160-060 $ 11.00 TOTAL AMOUNT: $ 23.00</strong></p>
<p><strong>_______________________________________________________________________________</strong></p>
<p><strong>D. OTHER (specify type of modification and authority)</strong></p>
<p><strong>_______________________________________________________________________________</strong></p>
<p><strong>IMPORTANT: Contractor is not required to sign this document and return</strong></p>
<p><strong>copies to the issuing office.</strong></p>
<p><strong>14. DESCRIPTION OF MODIFICATION (organized by UCF section heading,</strong></p>
<p><strong>including contract subject matter where feasible.)</strong></p>
<p><strong>_______________________________________________________________________________</strong></p>
<p><strong>Currently:</strong></p>
<p><strong>Item No. 1 Item Master File No. BOC: 2660</strong></p>
<p><strong>TEST</strong></p>
<p><strong>Items per EA: 1 NSN:</strong></p>
<p><strong>1 EA at $ 12.0000 = $ 12.00</strong></p>
<p><strong>Will now be AMENDED to read:</strong></p>
<p><strong>Item No. 1 Item Master File No. BOC: 2660</strong></p>
<p><strong>TEST</strong></p>
<p><strong>Items per EA: 1 NSN:</strong></p>
<p><strong>2 EA $ 11.5000 = $ 23.00</strong></p>
<p><strong>*ADDED THROUGH AMENDMENT*</strong></p>
<p><strong>Authority Edit is OTHER (specify type of modification and authority)</strong></p>
<p><strong>Except as provided herein, all terms and conditions of the document referenced</strong></p>
<p><strong>in Item 10A, as heretofore changed, remains unchanged and in full force and</strong></p>
<p><strong>effect.</strong></p>
<p><strong>_______________________________________________________________________________</strong></p>
<p><strong>JUSTIFICATION: tst</strong></p>
<p><strong>_______________________________________________________________________________</strong></p>
<p><strong>CONTRACTING OFFICER: IFBUYER,TWO</strong></p>
<p><strong>ENTER '^' TO HALT:</strong></p>
<p><strong>Approve Amendment number 1: ? NO// y (YES)</strong></p>
<p><strong>Enter ELECTRONIC SIGNATURE CODE: Thank you.</strong></p>
<p><strong>...copying amendment information back to Purchase Order file...</strong></p>
<p><strong>...EXCUSE ME, JUST A MOMENT PLEASE...</strong></p>
<p><strong>...checking on due-ins at inventory point(s)...</strong></p>
<p><strong>...now creating entry in File 410 for the amendment...</strong></p>
<p><strong>SEND TO SUPPLY</strong></p>
<p><strong>QUEUE ON DEVICE: UCX/TELNET</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Adjustment Voucher to Purchase Card Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to decrease the quantity received on a receiving report for a Purchase Card order. This option will follow the prompts of the current Adjustment Voucher option. This new option will be available to all Purchase Card Users. Depending upon where the order is in the system, the system will update the status to one of the following:

- Complete Order Received (Amended)
- Ordered (No Fiscal Action Required) - Amended
- Paid (No Receipt) - Amended
- Paid (Partial Receipt) - Amended
- Paid (Complete Order Received) - Amended
- Partial Payment (No Receipt) - Amended
- Partial Payment (Partial Rec) - Amended
- Partial Payment (Complete Rec) - Amended
- Transaction Complete (Amended)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process Purchase Card Menu from the Purchase Card Menu.

Select Adjustment Voucher to Purchase Card Order from the Process Purchase Card Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Reports Menu ...</strong></p>
<p><strong>Approving Official Menu ...</strong></p>
<p><strong>Process Purchase Card Menu ...</strong></p>
<p><strong>Purchase Card Display/Print Menu ...</strong></p>
<p><strong>Reconciliation Menu ...</strong></p>
<p><strong>Select Purchase Card Menu Option: Process Purchase Card Menu</strong></p>
<p><strong>New Simplified Purchase Card Order</strong></p>
<p><strong>Edit Simplified Purchase Card Order</strong></p>
<p><strong>New Detailed Purchase Card Order</strong></p>
<p><strong>Edit Detailed Purchase Card Order</strong></p>
<p><strong>Amendment To Purchase Card Order</strong></p>
<p><strong>Adjustment Voucher To Purchase Card Order</strong></p>
<p><strong>Receive Purchase Card Order</strong></p>
<p><strong>Item Display</strong></p>
<p><strong>Vendor Display</strong></p>
<p><strong>Create P/C Order From Repetitive Item List</strong></p>
<p><strong>Convert P/C Order To 2237 Request</strong></p>
<p><strong>Convert P/C Order to a Delivery Order</strong></p>
<p><strong>Cancel An Incomplete PC Order</strong></p>
<p><strong>Select Process Purchase Card Menu Option: Adjustment Voucher to Purchase Card Order</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a station number if prompted.
2.  Enter the Purchase Card order you wish to adjust at the Purchase Order: prompt, or enter two question marks to see a list of available purchase orders.
3.  IFCAP will display the Adjustment number it is working on. You will be prompted ‘Do you wish to continue? Yes//’. Accept the default of Yes to continue with the adjustment voucher.
4.  At the Effective Date: prompt, enter the date that the adjustment will take effect.
5.  You may enter the new status of the Purchase Card order at the Amendment/Adjustment Status: prompt or enter a question mark to see a list of valid status.
6.  Enter the date of the receiving report you wish to adjust at the Select Partial Date: prompt.
7.  If you do not know the report date, enter three question marks and IFCAP will list the available dates.
8.  Enter the sequence number of the item you want to adjust (e.g., 1 for the first item on the purchase order) at the Select Item: prompt.
9.  Enter the new quantity at the QTY Being Received: prompt. This value has to be smaller than the quantity on the receiving report.
10. Press Enter at the Select Item: prompt when you are through entering items for adjustment. You may review the adjustment if you like. IFCAP will display the adjustment voucher.
11. You may also edit the description of the adjustment.
12. Confirm that you want to approve the adjustment by entering Y at the Approve And Print (In Fiscal And Supply) Adjustment No. (#)?: prompt.
13. Enter your electronic signature.
14. Enter an output device for the adjustment voucher. IFCAP will print or display the adjustment voucher on the output device you selected.
15. You may enter another purchase order at the Purchase Order: prompt, or press \<Enter\> to return to the Process Purchase Card Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 658// SALEM, VA</strong></p>
<p><strong>PURCHASE ORDER: 658-P65138 07-31-96 PC Partial Order Received (Amended)</strong></p>
<p><strong>FCP: 036 $ 574.96 IFVENDOR,NINE</strong></p>
<p><strong>Adjustment number: 2</strong></p>
<p><strong>Do you wish to continue? YES// (YES)</strong></p>
<p><strong>EFFECTIVE DATE: t (OCT 03, 1996)</strong></p>
<p><strong>AMENDMENT/ADJUSTMENT STATUS: ?</strong></p>
<p><strong>Enter the status the purchase will have after it is amended.</strong></p>
<p><strong>Answer with PURCHASE ORDER STATUS NAME, or SUPPLY STATUS ORDER</strong></p>
<p><strong>Do you want the entire PURCHASE ORDER STATUS List? y (Yes)</strong></p>
<p><strong>Choose from:</strong></p>
<p><strong>Complete Order Received (Amended) 31</strong></p>
<p><strong>Ordered (No Fiscal Action)-Amended 23</strong></p>
<p><strong>Partial Order Received (Amended) 26</strong></p>
<p><strong>Transaction Complete (Amended) 41</strong></p>
<p><strong>AMENDMENT/ADJUSTMENT STATUS: 26 Partial Order Received (Amended) 26</strong></p>
<p><strong>Select PARTIAL DATE: t OCT 03, 1996</strong></p>
<p><strong>...HMMM, HOLD ON...</strong></p>
<p><strong>Select ITEM: 1</strong></p>
<p><strong>QTY BEING RECEIVED: 2// 1</strong></p>
<p><strong>Select ITEM:</strong></p>
<p><strong>Review Adjustment ? YES// (YES)</strong></p>
<p><strong>ADJUSTMENT VOUCHER 10/3/96</strong></p>
<p><strong>_______________________________________________________________________________</strong></p>
<p><strong>Adjustment Voucher for Purchase Order 658-P65138</strong></p>
<p><strong>Item No. 1 CUTTER WIRE KIRSCHNER</strong></p>
<p><strong>Items per EA: 1 STK#: 56-2507</strong></p>
<p><strong>3 EA at $ 123.20 = $ 369.60</strong></p>
<p><strong>ORIGINALLY QTY RECEIVED = 2 ,COST = $ 246.4</strong></p>
<p><strong>will now read: QTY RECEIVED=1, COST=$123.2</strong></p>
<p><strong>Vendor: IFVENDOR,NINE</strong></p>
<p><strong>APPROPRIATION: 3660160</strong></p>
<p><strong>This Receiving Report will now read:</strong></p>
<p><strong>Total Amount: 123.2</strong></p>
<p><strong>CONTRACTING OFFICER: IFBUYER,SIX</strong></p>
<p><strong>Edit Description ? NO// (NO)</strong></p>
<p><strong>Approve and print Adjustment no.: 2? NO// y (YES)</strong></p>
<p><strong>Enter ELECTRONIC SIGNATURE CODE: Thank you.</strong></p>
<p><strong>...HMMM, LET ME THINK ABOUT THAT A MOMENT...</strong></p>
<p><strong>...please wait while I update the due-ins at the inventory points...</strong></p>
<p><strong>SEND TO SUPPLY</strong></p>
<p><strong>QUEUE ON DEVICE: ;80;999 TELNET</strong></p>
<p><strong>SUBJECT: ADJUSTMENT VOUCHER</strong></p>
<p><strong>Adjustment Voucher for Purchase Order 658-P65138</strong></p>
<p><strong>Item No. 1 CUTTER WIRE KIRSCHNER</strong></p>
<p><strong>Items per EA: 1 STK#: 56-2507</strong></p>
<p><strong>3 EA at $ 123.20 = $ 369.60</strong></p>
<p><strong>ORIGINALLY QTY RECEIVED = 2 ,COST = $ 246.4</strong></p>
<p><strong>will now read: QTY RECEIVED=1, COST=$123.2</strong></p>
<p><strong>Vendor: IFVENDOR,NINE</strong></p>
<p><strong>APPROPRIATION: 3660160</strong></p>
<p><strong>This Receiving Report will now read:</strong></p>
<p><strong>Total Amount: 123.2</strong></p>
<p><strong>______________________________________________________________________________________</strong></p>
<p><strong>Approve subject to final action on R/S on items indicated. | DATE |</strong></p>
<p><strong>P.O. NO.</strong></p>
<p><strong>_________________________________________________________________| |</strong></p>
<p><strong>SIGNATURE OF CONTRACTING OFFICER | |</strong></p>
<p><strong>| |</strong></p>
<p><strong>/ES/ IFBUYER,SIX 10/3/96 | 10/3/96 |</strong></p>
<p><strong>_________________________________________________________________|___________|________</strong></p>
<p><strong>PURCHASE ORDER:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Purchase Card Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains Purchase Card reports for a single buyer. Reports available in the Purchase Card Reports Menu include the following options:

- Unreconciled Austin Payments - Buyer
- Unreconciled Purchase Card Transactions - Buyer
- BOC Report for OA&MM/Fiscal.
- Delinquent PC Listing - Buyer
- Disputed Purchase Card Orders - Buyer
- Final Charge YES - Reconciled Orders - Buyer
- History of Purchase Card Transactions - Buyer
- Incomplete Purchase card Orders - Buyer
- Reconciled Purchase Card Transactions - Buyer

## Unreconciled Austin Payments-Buyer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will display charge transactions that have not been reconciled by the cardholder

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>BOC Report for OA&amp;MM/Fiscal</strong></p>
<p><strong>Delinquent PC Listing - Buyer</strong></p>
<p><strong>Disputed Purchase Card Orders - Buyer</strong></p>
<p><strong>Final Charge YES - Reconciled Orders - Buyer</strong></p>
<p><strong>History of Purchase Card Transactions - Buyer</strong></p>
<p><strong>Incomplete Purchase card Orders - Buyer</strong></p>
<p><strong>Reconciled Purchase Card Transactions – Buyer</strong></p>
<p><strong>Select Purchase Card Reports Menu Option: Unreconciled Austin Payments - Buyer</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Accept the default of First and Last.
2.  Enter a Printer name if you want a hard copy printout of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Reports Menu Option: UNR</strong></p>
<p><strong>1 Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>2 Unreconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>CHOOSE 1-2: 1 Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>START WITH CARD HOLDER: FIRST//</strong></p>
<p><strong>DEVICE: HOME// UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>UNRECONCILED AUSTIN PAYMENTS - BUYER JUN 1,2000 18:03 PAGE 1</strong></p>
<p><strong>TRANSACTION</strong></p>
<p><strong>CARD HOLDER DATE AMOUNT</strong></p>
<p><strong>MERCHANT NAME ORACLE DOCUMENT ID</strong></p>
<p><strong>-----------------------------------------------------------------------</strong></p>
<p><strong>IFBUYER,ONE MAY 28,1996 200.00</strong></p>
<p><strong>6NPDB-HRSA C99961470001003</strong></p>
<p><strong>-------------</strong></p>
<p><strong>SUBTOTAL 200.00</strong></p>
<p><strong>SUBCOUNT 1</strong></p>
<p><strong>SUBMEAN 200.00</strong></p>
<p><strong>-------------</strong></p>
<p><strong>TOTAL 200.00</strong></p>
<p><strong>COUNT 1</strong></p>
<p><strong>MEAN 200.00</strong></p>
<p><strong>Unreconciled Purchase Card Transactions – Buyer</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will display purchase orders not reconciled to a credit card charge by the cardholder.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>BOC Report for OA&amp;MM/Fiscal</strong></p>
<p><strong>Delinquent PC Listing - Buyer</strong></p>
<p><strong>Disputed Purchase Card Orders - Buyer</strong></p>
<p><strong>Final Charge YES - Reconciled Orders - Buyer</strong></p>
<p><strong>History of Purchase Card Transactions - Buyer</strong></p>
<p><strong>Incomplete Purchase card Orders - Buyer</strong></p>
<p><strong>Reconciled Purchase Card Transactions – Buyer</strong></p>
<p><strong>Select Purchase Card Reports Menu Option: Unreconciled Purchase Card Transactions - Buyer</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter station number if prompted.

Enter beginning date for report.

Enter ending date for report.

Enter a printer name if you want a hard copy printout of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Reports Menu Option: PTB Unreconciled Purchase Card Transa</strong></p>
<p><strong>ctions - Buyer</strong></p>
<p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>Enter beginning date: 010100 JAN 1,2000</strong></p>
<p><strong>Enter ending date: T JUN 2,2000</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>UNRECONCILED PURCHASE CARD ORDERS JUN 02, 2000@12:32:56 PAGE 1</strong></p>
<p><strong>P.O. DATE ORDER # $AMT TYPE(S/D)</strong></p>
<p><strong>VENDOR DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>BUYER: MCGAUGH,MAVIS</strong></p>
<p><strong>JAN 11, 2000 999-P05034 27.60 DETAILED</strong></p>
<p><strong>DAN'S TESTING #2 ALTER THE TEXT</strong></p>
<p><strong>Ordered (No Fiscal Action)-Amended</strong></p>
<p><strong>FEB 08, 2000 999-P05080 12.00 DETAILED</strong></p>
<p><strong>AMSCO INTERNATIONAL BATTERY, NONRECHARGEABLE. 1.5 VOLT</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>DO THESE WIPE OUT MY COMMENTS</strong></p>
<p><strong>FEB 08, 2000 999-P05079 12.00 DETAILED</strong></p>
<p><strong>AMSCO INTERNATIONAL BATTERY, NONRECHARGEABLE. 1.5 VOLT</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## BOC Report for OA&MM/Fiscal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will allow users to specify a date and name range to print any Purchase Card transactions that include BOC numbers 2696 to 2699. It is used by OA&MM/Fiscal to perform Supply Funds reconciliation. NOTE: This option is usually assigned to the Purchase Card Coordinator and /or Fiscal Staff. It may not be on your menu.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>BOC Report for OA&amp;MM/Fiscal</strong></p>
<p><strong>Delinquent PC Listing - Buyer</strong></p>
<p><strong>Disputed Purchase Card Orders - Buyer</strong></p>
<p><strong>Final Charge YES - Reconciled Orders - Buyer</strong></p>
<p><strong>History of Purchase Card Transactions - Buyer</strong></p>
<p><strong>Incomplete Purchase card Orders - Buyer</strong></p>
<p><strong>Reconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>Select Purchase Card Reports Menu Option: BOC Report for OA&amp;MM/Fiscal</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a specific cardholder name or accept the default to get ALL cardholders.
2.  Enter a printer name if you wish a hard copy printout of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Reports Menu Option: BOC Report for OA&amp;MM/Fiscal</strong></p>
<p><strong>* Previous selection: CARD HOLDER from greene,lyford to gribschaw,stephen</strong></p>
<p><strong>START WITH CARD HOLDER: FIRST//</strong></p>
<p><strong>* Previous selection: TRANSACTION DATE not null</strong></p>
<p><strong>START WITH TRANSACTION DATE: FIRST//</strong></p>
<p><strong>DEVICE: HOME// UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>PURCHASE CARD/SUPPLY FUND DOC ID RECONCILIATION</strong></p>
<p><strong>JUN 2,2000 12:37 PAGE 1</strong></p>
<p><strong>TRANSACTION</strong></p>
<p><strong>BOC DATE ORACLE DOCUMENT ID PURCHASE ORDER</strong></p>
<p><strong>COMMITTED</strong></p>
<p><strong>AMOUNT AMOUNT MERCHANT NAME</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>CARD HOLDER: MONTOYA,INDIGO</strong></p>
<p><strong>2696 MAR 3,1999 C-662000P95005 662-P95005</strong></p>
<p><strong>1.50 1.50 IFVENDOR5,TEN</strong></p>
<p><strong>2696 MAR 3,1999 C-662000P95006 662-P95006</strong></p>
<p><strong>2.50 2.50 IFVENDOR,SIX</strong></p>
<p><strong>2696 APR 16,1999 C-662000P95014 662-P95014</strong></p>
<p><strong>3.00 3.00 IFVENDOR,SIX</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Delinquent PC Listing – Buyer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will display the cardholder’s Purchase Card orders with items only partially received after requested delivery date.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>BOC Report for OA&amp;MM/Fiscal</strong></p>
<p><strong>Delinquent PC Listing - Buyer</strong></p>
<p><strong>Disputed Purchase Card Orders - Buyer</strong></p>
<p><strong>Final Charge YES - Reconciled Orders - Buyer</strong></p>
<p><strong>History of Purchase Card Transactions - Buyer</strong></p>
<p><strong>Incomplete Purchase card Orders - Buyer</strong></p>
<p><strong>Reconciled Purchase Card Transactions – Buyer</strong></p>
<p><strong>Select Purchase Card Reports Menu Option: Delinquent PC Listing - Buyer</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a device for printing this report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Reports Menu Option: delinquent PC Listing - Buyer</strong></p>
<p><strong>Please enter a device for printing this report</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>DELINQUENT PURCHASE CARD LISTING PAGE 1</strong></p>
<p><strong>PURCHASE CARD NAME PO # STATUS DELIVERY DATE</strong></p>
<p><strong>VENDOR VENDOR PHONE</strong></p>
<p><strong>DELIVERY DATE LINE ITEM OUTSTANDING QTY ORDERED QTY OUTSTANDING</strong></p>
<p><strong>AMOUNT OUTSTANDING ITEM DESCRIPTION</strong></p>
<p><strong>BUYER: IFBUYER,TWO</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>110CR P85157 Partial Order Received MAR 18, 1998</strong></p>
<p><strong>IFVENDOR,THREE 555-222-2625</strong></p>
<p><strong>JUL 01, 1999 1 12 6</strong></p>
<p><strong>20.40 STUFF</strong></p>
<p><strong>PURCHASE CARD SUBTOTAL: 20.40</strong></p>
<p><strong>SEPT TEST P75149 Partial Order Received AUG 09, 1997</strong></p>
<p><strong>IFVENDOR5,THREE 555 555 6462</strong></p>
<p><strong>JAN 13, 1998 1 12 6</strong></p>
<p><strong>5.94 GOGGLES INFECTION CONTROL DISPOSABLE</strong></p>
<p><strong>PURCHASE CARD SUBTOTAL: 26.34</strong></p>
<p><strong>IFVENDOR,THREE P05092 Partial Order Received FEB 11, 2000</strong></p>
<p><strong>IFVENDOR,SIX 555-333-8838</strong></p>
<p><strong>Press return to continue, '^' to exit:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Disputed Purchase Card Orders – Buyer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of Purchase Card orders placed in dispute status for a single cardholder.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>BOC Report for OA&amp;MM/Fiscal</strong></p>
<p><strong>Delinquent PC Listing - Buyer</strong></p>
<p><strong>Disputed Purchase Card Orders - Buyer</strong></p>
<p><strong>Final Charge YES - Reconciled Orders - Buyer</strong></p>
<p><strong>History of Purchase Card Transactions - Buyer</strong></p>
<p><strong>Incomplete Purchase card Orders - Buyer</strong></p>
<p><strong>Reconciled Purchase Card Transactions – Buyer</strong></p>
<p><strong>Select Purchase Card Reports Menu Option: Disputed Purchase Card Orders - Buyer</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter station number if prompted.

Enter printer name if want a hard copy of the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>DISPUTED PURCHASE CARD ORDERS JUN 02, 2000@13:05:51 PAGE 1</strong></p>
<p><strong>PC NAME P.O. DATE $AMT PC ORDER # VENDOR</strong></p>
<p><strong>DATE RECONCILED DESCRIPTION</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>BUYER: IFBUYER,TWO</strong></p>
<p><strong>PROS MAY 19, 1998 29.90 999-P85308 IFVENDOR5,FOUR</strong></p>
<p><strong>JUL 02, 1998 Prosthetic Order</strong></p>
<p><strong>TESTING</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Final Charge YES - Reconciled Orders – Buyer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report lists all reconciled orders that have been marked as Final Change YES for the selected date range and Card Name (File 440.6, field 44).

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>BOC Report for OA&amp;MM/Fiscal</strong></p>
<p><strong>Delinquent PC Listing - Buyer</strong></p>
<p><strong>Disputed Purchase Card Orders - Buyer</strong></p>
<p><strong>Final Charge YES - Reconciled Orders - Buyer</strong></p>
<p><strong>History of Purchase Card Transactions - Buyer</strong></p>
<p><strong>Incomplete Purchase card Orders - Buyer</strong></p>
<p><strong>Reconciled Purchase Card Transactions – Buyer</strong></p>
<p><strong>Select Purchase Card Reports Menu Option: Final Charge YES - Reconciled Orders - Buyer</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the name of your Purchase Card.

Enter a reconciliation date for the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Purchase Card Reports Menu Option: final Charge YES - Reconciled Orders - Buyer</strong></p>
<p><strong>Enter Purchase Card Name: IVO IFVENDOR,ONE</strong></p>
<p><strong>* Previous selection: RECONCILE DATE not null</strong></p>
<p><strong>START WITH RECONCILE DATE: FIRST//</strong></p>
<p><strong>DEVICE: HOME// UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>FINAL CHARGE RECONCILED ORDERS - BUYER JUN 2,2000 13:13 PAGE 1</strong></p>
<p><strong>P.O. NUMBER</strong></p>
<p><strong>ORACLE CHARGE DATE</strong></p>
<p><strong>P.O. AMOUNT AMOUNT RECONCILED</strong></p>
<p><strong>-------------------------------------------------------------------------</strong></p>
<p><strong>999-P05026 32.45 32.45 NOV 17,1999</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## History of Purchase Card Transactions – Buyer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will display Purchase Card data on cards held by the cardholder within the date range selected by the buyer.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>BOC Report for OA&amp;MM/Fiscal</strong></p>
<p><strong>Delinquent PC Listing - Buyer</strong></p>
<p><strong>Disputed Purchase Card Orders - Buyer</strong></p>
<p><strong>Final Charge YES - Reconciled Orders - Buyer</strong></p>
<p><strong>History of Purchase Card Transactions - Buyer</strong></p>
<p><strong>Incomplete Purchase card Orders - Buyer</strong></p>
<p><strong>Reconciled Purchase Card Transactions – Buyer</strong></p>
<p><strong>Select Purchase Card Reports Menu Option: History of Purchase Card Transactions - Buyer</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter the beginning date for the report.
2.  Enter the ending date for the report.
3.  Enter a status: P for Paid orders, U for Unpaid orders and B for both types of orders.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Enter beginning date: 010100 JAN 1,2000</strong></p>
<p><strong>Enter ending date: t JUN 2,2000</strong></p>
<p><strong>Select one of the following:</strong></p>
<p><strong>P Paid</strong></p>
<p><strong>U Unpaid</strong></p>
<p><strong>B Both</strong></p>
<p><strong>STATUS: b Both</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>HISTORY OF PURCHASE CARD TRANSACTIONS REPORT - ALL PAGE: 1</strong></p>
<p><strong>FCP PC NUMBER PURCHASE DATE BUYER VENDOR</strong></p>
<p><strong>AMOUNT COST CENTER BUDGET OBJECT CODE</strong></p>
<p><strong>FIRST LINE ITEM DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>036 P05176 MAY 01, 2000 IFBUYER,ONE IFVENDOR5,FIVE</strong></p>
<p><strong>27.60 828100 2660 Operating Supplies and Ma</strong></p>
<p><strong>WOODEN WIDGETS-PINE-PAINTED</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>CONTROL POINT 36 SUBTOTAL: 27.60</strong></p>
<p><strong>060 P05174 MAY 01, 2000 IFBUYER,ONE IFVENDOR5,FIVE</strong></p>
<p><strong>0.00 842100 2660 Operating Supplies and Ma</strong></p>
<p><strong>WOODEN WIDGETS-PINE-PAINTED</strong></p>
<p><strong>Order Not Completely Prepared</strong></p>
<p><strong>060 P00003 APR 13, 2000 IFBUYER,ONE IFVENDOR5,FIVE</strong></p>
<p><strong>10.00 842100 2660 Operating Supplies and Materials</strong></p>
<p><strong>STUFF</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>HISTORY OF PURCHASE CARD TRANSACTIONS REPORT - ALL PAGE: 2</strong></p>
<p><strong>FCP PC NUMBER PURCHASE DATE BUYER VENDOR</strong></p>
<p><strong>AMOUNT COST CENTER BUDGET OBJECT CODE</strong></p>
<p><strong>FIRST LINE ITEM DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>110 A00059 APR 13, 2000 IFBUYER,ONE IFVENDOR5,FIVE</strong></p>
<p><strong>14.40 842100 2660 Operating Supplies and Materials</strong></p>
<p><strong>TESTING</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p>
<p><strong>110 P05158 APR 04, 2000 IFBUYER,ONE IFVENDOR5,FIVE</strong></p>
<p><strong>27.60 842100 2660 Operating Supplies and Materials</strong></p>
<p><strong>WOODEN WIDGETS-PINE-PAINTED</strong></p>
<p><strong>Ordered (No Fiscal Action Required)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Incomplete Purchase card Orders – Buyer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a report of Purchase Card orders entered but not signed for the cardholder.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>BOC Report for OA&amp;MM/Fiscal</strong></p>
<p><strong>Delinquent PC Listing - Buyer</strong></p>
<p><strong>Disputed Purchase Card Orders - Buyer</strong></p>
<p><strong>Final Charge YES - Reconciled Orders - Buyer</strong></p>
<p><strong>History of Purchase Card Transactions - Buyer</strong></p>
<p><strong>Incomplete Purchase card Orders - Buyer</strong></p>
<p><strong>Reconciled Purchase Card Transactions – Buyer</strong></p>
<p><strong>Select Purchase Card Reports Menu Option: History of Purchase Card Transactions - Buyer</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter a station number if prompted.
2.  Select a fiscal year.
3.  Select a device for printing the report.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER: 999</strong></p>
<p><strong>Select FISCAL YEAR: 00//</strong></p>
<p><strong>Please select a device for printing this report.</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>INCOMPLETE PURCHASE CARD ORDERS REPORT PAGE 1</strong></p>
<p><strong>PURCHASE CARD ORDER PO DATE SUPPLY STATUS</strong></p>
<p><strong>BUYER DATE PO ASSIGNED</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>999-P05174 MAY 01, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER,ONE DVMMAY 01, 2000@12:20</strong></p>
<p><strong>999-P05166 APR 13, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER,ONE DVMAPR 13, 2000@12:16</strong></p>
<p><strong>999-P05128 MAR 21, 2000 Order Not Completely Prepared</strong></p>
<p><strong>IFBUYER,ONE DVMMAR 21, 2000@12:43</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Reconciled Purchase Card Transactions – Buyer 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reconciled Purchase Card Transactions - Buyer report will list all Purchase Card orders reconciled by the Purchase Card holder, sorted by Purchase Card User, card number (although the card number will not display on the report), and date, beginning with the oldest order. Cardholder access to Purchase Card order data will be limited to their own orders.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Unreconciled Austin Payments - Buyer</strong></p>
<p><strong>Unreconciled Purchase Card Transactions - Buyer</strong></p>
<p><strong>BOC Report for OA&amp;MM/Fiscal</strong></p>
<p><strong>Delinquent PC Listing - Buyer</strong></p>
<p><strong>Disputed Purchase Card Orders - Buyer</strong></p>
<p><strong>Final Charge YES - Reconciled Orders - Buyer</strong></p>
<p><strong>History of Purchase Card Transactions - Buyer</strong></p>
<p><strong>Incomplete Purchase card Orders - Buyer</strong></p>
<p><strong>Reconciled Purchase Card Transactions – Buyer</strong></p>
<p><strong>Select Purchase Card Reports Menu Option: Reconciled Purchase Card Transactions – Buyer</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number if prompted.

Enter the first date that you want IFCAP to use for the report at the Enter Beginning Date: prompt.

Enter the last date that you want IFCAP to use for the report at the Enter Ending Date: prompt.

Enter an output device. IFCAP will print the 'Reconciled Purchase Card Orders’ report on the output device you selected. The report will list each reconciled order, purchase order date, date reconciled, order \#, the amount of the order, the vendor, description of line item 1, status, comments, charge document reference \#, amount reconciled, whether reconciled amount was the Final Charge, and the buyer of the order.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, NM</strong></p>
<p><strong>Enter beginning date: 060100 JUN 1,2000</strong></p>
<p><strong>Enter ending date: T JUN 2,2000</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>RECONCILED PURCHASE CARD ORDERS JUN 02, 2000@13:41:04 PAGE 1</strong></p>
<p><strong>P.O. DATE DATE RECONCILED ORDER # $AMT TYPE(S/D)</strong></p>
<p><strong>VENDOR DESCRIPTION</strong></p>
<p><strong>STATUS</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>DOC-REF # RECONCILED $AMT RECONCILE VENDOR FINAL CHARGE</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>BUYER: IFBUYER2,NINE</strong></p>
<p><strong>APR 28, 1997 JUN 02, 2000 999-P65024 667.14 SIMPLIFIED</strong></p>
<p><strong>IFVENDOR1,TWO SDFS</strong></p>
<p><strong>Reconciled</strong></p>
<p><strong>SFSF</strong></p>
<p><strong>C99961470012001 150.20 IFVENDOR1,ONE NO</strong></p>
<p><strong>C99961470012006 667.14 IFVENDOR1,THREE YES</strong></p>
<p><strong>RECONCILED SUBTOTAL - $817.34</strong></p>
<p><strong>BUYER SUBTOTAL - $667.14</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Cancel an Incomplete PC Order 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to cancel an incomplete Purchase Card order, not certified with an electronic signature. To cancel a COMPLETE purchase order, you must create an amendment to the Purchase Card order.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process Purchase Card Menu from the Purchase Card Menu.

Select Cancel An Incomplete PC Order from the Process Purchase Card Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Reports Menu ...</strong></p>
<p><strong>Approving Official Menu ...</strong></p>
<p><strong>Process Purchase Card Menu ...</strong></p>
<p><strong>Purchase Card Display/Print Menu ...</strong></p>
<p><strong>Reconciliation Menu ...</strong></p>
<p><strong>Select Purchase Card Menu Option: Process Purchase Card Menu</strong></p>
<p><strong>New Simplified Purchase Card Order</strong></p>
<p><strong>Edit Simplified Purchase Card Order</strong></p>
<p><strong>New Detailed Purchase Card Order</strong></p>
<p><strong>Edit Detailed Purchase Card Order</strong></p>
<p><strong>Amendment To Purchase Card Order</strong></p>
<p><strong>Adjustment Voucher To Purchase Card Order</strong></p>
<p><strong>Receive Purchase Card Order</strong></p>
<p><strong>Item Display</strong></p>
<p><strong>Vendor Display</strong></p>
<p><strong>Create P/C Order From Repetitive Item List</strong></p>
<p><strong>Convert P/C Order To 2237 Request</strong></p>
<p><strong>Convert P/C Order to a Delivery Order</strong></p>
<p><strong>Cancel An Incomplete PC Order</strong></p>
<p><strong>Select Process Purchase Card Menu Option: Cancel an Incomplete PC Order</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Purchase Card order number or enter two question marks to see a list of available Purchase Card orders.

IFCAP will ask you to confirm that you want to cancel the order. Enter Y to cancel the order. IFCAP will return to the Process Purchase Card Menu.

|     |
|-----|

## Purchase Card Display/Print Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options for printing and displaying information related to the Purchase Card Orders.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select PURCHASE CARD ORDER NUMBER: 658-P65210 08-15-96 PC Order Not Completely Prepared</strong></p>
<p><strong>FCP: 091 $ 2.00 IFVENDOR5,SIX</strong></p>
<p><strong>Are sure you want to cancel this order? NO// y (YES)</strong></p>
<p><strong>New Simplified Purchase Card Order</strong></p>
<p><strong>Edit Simplified Purchase Card Order</strong></p>
<p><strong>New Detailed Purchase Card Order</strong></p>
<p><strong>Edit Detailed Purchase Card Order</strong></p>
<p><strong>Amendment To Purchase Card Order</strong></p>
<p><strong>Adjustment Voucher To Purchase Card Order</strong></p>
<p><strong>Receive Purchase Card Order</strong></p>
<p><strong>Item Display</strong></p>
<p><strong>Vendor Display</strong></p>
<p><strong>Create P/C Order From Repetitive Item List</strong></p>
<p><strong>Convert P/C Order To 2237 Request</strong></p>
<p><strong>Convert P/C Order to a Delivery Order</strong></p>
<p><strong>Cancel An Incomplete PC Order</strong></p>
<p><strong>Select Purchase Card Menu Option: Purchase Card Display/Print Menu</strong></p>
<p><strong>Inquire-Purchase Card Information</strong></p>
<p><strong>Purchase Card Transaction Statu</strong></p>
<p><strong>Item History</strong></p>
<p><strong>Reprint Purchase Card Order</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Inquire-Purchase Card Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows users to make an inquiry about Purchase Card information and to add or delete surrogate users on their specific cards.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Reports Menu ...</strong></p>
<p><strong>Approving Official Menu ...</strong></p>
<p><strong>Process Purchase Card Menu ...</strong></p>
<p><strong>Purchase Card Display/Print Menu ...</strong></p>
<p><strong>Reconciliation Menu ...</strong></p>
<p><strong>Select Purchase Card Menu Option: Purchase Card Display/Print Menu</strong></p>
<p><strong>Inquire-Purchase Card Information</strong></p>
<p><strong>Purchase Card Transaction Status</strong></p>
<p><strong>Item History</strong></p>
<p><strong>Reprint Purchase Card Order</strong></p>
<p><strong>Select Purchase Card Display/Print Menu Option: Inquire-Purchase Card Information</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Purchase Card number or enter two question marks to see a list of Purchase Card numbers that you are authorized to use.

After you make your selection, IFCAP will display information about the Purchase Card, including budgetary information, spending limits, and IFCAP users associated with the card in various ways.

Enter Y at the Would You Like To Add/Delete A Surrogate?: prompt to authorize a new user of the Purchase Card or to delete a user from the card.

Enter the user's name at the Select Surrogate User: prompt. Enter the last name of the user first. You do not have to enter the @ sign before the name to delete a user; when you enter a name, IFCAP adds the name if the name isn't associated with the card, and deletes the name if the name is associated with the card.

Enter another user at the Would You Like To Add/Delete Another Surrogate?: prompt, or press \<Enter\> to return to the Purchase Card Display/Print Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select PURCHASE CARD INFORMATION PURCHASE CARD NUMBER: 4716360112121212</strong></p>
<p><strong>PURCHASE CARD NUMBER: 4716360112121212 FUND CONTROL POINT: 173 PROSTHETICS</strong></p>
<p><strong>COST CENTER: 827200</strong></p>
<p><strong>BUDGET OBJECT CODE: 1031 Other Health Technicians and Aides not Previously Identified</strong></p>
<p><strong>PC USER SINGLE PURCHASE LIMIT: 1000 MONTHLY PURCHASE LIMIT: 10000</strong></p>
<p><strong>CARD HOLDER: IFBUYER3,TEN</strong></p>
<p><strong>SURROGATE USER: IFBUYER3,TEN</strong></p>
<p><strong>STATION NUMBER: 658</strong></p>
<p><strong>Would you like to add/delete a surrogate? NO// y (YES)</strong></p>
<p><strong>Select SURROGATE USER: IFBUYER3,ONE IRM PROGRAMMER/ANALYST</strong></p>
<p><strong>Are you adding 'IFBUYER3,ONE' as a new SURROGATE USER? y (Yes)</strong></p>
<p><strong>Would you like to add/delete another surrogate? NO// (NO)</strong></p>
<p><strong>Inquire-Purchase Card Information</strong></p>
<p><strong>Purchase Card Transaction Status</strong></p>
<p><strong>Item History</strong></p>
<p><strong>Reprint Purchase Card Order</strong></p>
<p><strong>Select Purchase Card Display/Print Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Purchase Card Transaction Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report that displays limited data including the status for a Purchase Card order.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Reports Menu ...</strong></p>
<p><strong>Approving Official Menu ...</strong></p>
<p><strong>Process Purchase Card Menu ...</strong></p>
<p><strong>Purchase Card Display/Print Menu ...</strong></p>
<p><strong>Reconciliation Menu ...</strong></p>
<p><strong>Select Purchase Card Menu Option: Purchase Card Display/Print Menu</strong></p>
<p><strong>Inquire-Purchase Card Information</strong></p>
<p><strong>Purchase Card Transaction Status</strong></p>
<p><strong>Item History</strong></p>
<p><strong>Reprint Purchase Card Order</strong></p>
<p><strong>Select Purchase Card Display/Print Menu Option: Purchase Card Transaction Status</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number if prompted.

Enter a Purchase Card order number at the P.O./REQ. NO.: prompt. IFCAP will display the order, including item and budget information. You may also print the report if you like.

Enter another station number at the Station Number: prompt or enter a caret (^) to return to the Purchase Card Display/Print Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 658// SALEM, VA</strong></p>
<p><strong>P.O./REQ. NO.: 658-A62633 10-04-96 PC Complete Order Received</strong></p>
<p><strong>FCP: 036 $ 7.25 PERMA TYPE</strong></p>
<p><strong>Transaction Number: 658-P65027 FCP: 074 M&amp;O</strong></p>
<p><strong>Transaction Status: Transaction Complete</strong></p>
<p><strong>Date of Request: AUG 07, 1996 Date Required: SEP 06, 1996</strong></p>
<p><strong>Vendor: IFVENDOR5,SEVEN</strong></p>
<p><strong>Committed (Estimated) Cost: 2631.00 Date Committed: SEP 06, 1996</strong></p>
<p><strong>Purchase Card Amount: 2631.00 Date Signed: AUG 07, 1996@12:24:36</strong></p>
<p><strong>Transaction Amount: 2631.00 Accounting Data: 3660160</strong></p>
<p><strong>Originator of Request: IFBUYER3,TWO</strong></p>
<p><strong>Requesting Service: ENGINEERING</strong></p>
<p><strong>Delivery Location: AC SHOP</strong></p>
<p><strong>Sort Group:</strong></p>
<p><strong>Transaction date: AUG 14, 1996 Credit card ref.#: C55566660004005</strong></p>
<p><strong>Amount: 2631.00</strong></p>
<p><strong>Do you wish to print this report? Yes// NO</strong></p>
<p><strong>Inquire-Purchase Card Information</strong></p>
<p><strong>Purchase Card Transaction Status</strong></p>
<p><strong>Item History</strong></p>
<p><strong>Reprint Purchase Card Order</strong></p>
<p><strong>Select Purchase Card Display/Print Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Reprint Purchase Card Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow the cardholder to reprint Purchase Card orders.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purchase Card Reports Menu ...</strong></p>
<p><strong>Approving Official Menu ...</strong></p>
<p><strong>Process Purchase Card Menu ...</strong></p>
<p><strong>Purchase Card Display/Print Menu ...</strong></p>
<p><strong>Reconciliation Menu ...</strong></p>
<p><strong>Select Purchase Card Menu Option: Purchase Card Display/Print Menu</strong></p>
<p><strong>Inquire-Purchase Card Information</strong></p>
<p><strong>Purchase Card Transaction Status</strong></p>
<p><strong>Item History</strong></p>
<p><strong>Reprint Purchase Card Order</strong></p>
<p><strong>Select Purchase Card Display/Print Menu Option: Reprint Purchase Card Order</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number if prompted.

Enter a Purchase Card order at the P.O./Req.No.: prompt.

Enter an output device for the Purchase Card order.

You can enter another Purchase Card order at the P.O./Req.No.: prompt, or press \<Enter\> to return to the Purchase Card Display/Print Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER ('^' TO EXIT): 658// SALEM, VA</strong></p>
<p><strong>P.O./REQ.NO.: 658-P65058 658-P65058 04-22-96 PC Transaction Complete</strong></p>
<p><strong>FCP: 060 $ 829.00 IFVENDOR5,EIGHT</strong></p>
<p><strong>Print on what Device: LASERDJ//</strong></p>
<p><strong>P.O./REQ.NO.:</strong></p>
<p><strong>Inquire-Purchase Card Information</strong></p>
<p><strong>Purchase Card Transaction Status</strong></p>
<p><strong>Item History</strong></p>
<p><strong>Reprint Purchase Card Order</strong></p>
<p><strong>Select PUrchase Card Display/Print Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

  

# The Logistics Data Query Tool 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Logistics Data Query Tool is designed to assist Chief Logistics Officers; Materiel Managers; Purchasing Agents; and members of the Facility Logistics Staff (including Inventory Managers; Supply, Processing, and Distribution (SPD) Technicians; Management Analysts; Warehouse Clerks; or Supply System Analysts). The Query Tool can be used to quickly access, analyze and verify IFCAP and Prosthetics procurement data and display it using a graphical user interface to the VistA data. You can sign-on to VistA, find data, view the data, or easily move the data into a Microsoft® Excel® spreadsheet.

The Query Tool is a Windows software application that acts as a “front-end” to enable you to more easily find, display, and export VistA data. The Query Tool is an alternative to the VA FileMan utility program which has traditionally been used to look directly at the MUMPS globals (files) which store VistA data. The Query Tool enables you to…

- Search for data and display data by a range of dates
- Sort and rearrange the view of the data; display the data in a custom view
- Export the data into a Microsoft Excel spreadsheet file

Information on what the Query Tool can do for you can be found in the Logistics Data Query Tool User Manual XE "Logistics Data Query Tool.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 86%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-purchase-card-user-s-guide/012.png)</td>
<td><p>The Logistics Data Query Tool User Manual is available online at…</p>
<p>![](ifcap-version-5-1-purchase-card-user-s-guide/013.png) <a href="http://www.va.gov/vdl/application.asp?appid=42">http://www.va.gov/vdl/application.asp?appid=42</a>.</p></td>
<td>![](ifcap-version-5-1-purchase-card-user-s-guide/014.png)</td>
</tr>
</tbody>
</table>

\*\<u>NOTE</u>*: The PRCHL LOGISTICS DATA TOOL \[PRCHL GUI\] option has been marked Out of Order with patch PRC\*5.1\*247.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary defines terms in this manual that users might find unfamiliar.
| Term                                           | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1358                                       | VA Form 1358, Estimated Obligation or Change in Obligation.                                                                                                                                                                                                                                                                                                                                                     |
| 2138                                       | VA Form 90-2138, Order for Supplies or Services. First page of a VA Purchase Order.                                                                                                                                                                                                                                                                                                                             |
| 2139                                       | VA Form 90-2139, Order for Supplies or Services (Continuation). This is a continuation sheet for the 2138 form.                                                                                                                                                                                                                                                                                                 |
| 2237                                       | VA Form 90-2237, Request, Turn-in and Receipt for Property or Services. Used to request goods and services.                                                                                                                                                                                                                                                                                                     |
| A&MM                                       | Acquisition and Materiel Management Service.                                                                                                                                                                                                                                                                                                                                                                    |
| Accounting Technician                      | Fiscal employee responsible for obligation of and payment for goods and services. Accounting Technicians process accounting transactions and transmit them to FMS.                                                                                                                                                                                                                                              |
| ADP Security Officer                       | The individual at your station who is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing file access.                                                                                                                                                                                                          |
| Agent Cashier                              | The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.                                                                                                                                                                                                                                                               |
| Allowance table                            | Reference table in FMS that provides financial information at the level immediately above the sub-allowance level.                                                                                                                                                                                                                                                                                              |
| Amendment                                  | A document that changes the information contained in a specified Order.                                                                                                                                                                                                                                                                                                                                         |
| Approve Requests                           | The use of an electronic signature by a Control Point Official to approve a 2237, 1358 or other request form and transmit said request to A&MM/Fiscal.                                                                                                                                                                                                                                                          |
| Authorization                              | A charge to an obligated 1358. Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.                                                                                                                                                                                          |
| Authorization Balance                      | The amount of money remaining that can be authorized against the 1358. The service balance minus total authorizations.                                                                                                                                                                                                                                                                                          |
| Batch Number                               | A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number.                                                                                                                                                                                                                                                     |
| Breakout Code                              | A set of A&MM codes which identifies a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.).                                                                                                                                                                                                                                                     |
| Budget Analyst                             | Fiscal employee responsible for distributing and transferring funds.                                                                                                                                                                                                                                                                                                                                            |
| Budget Object Code                         | Fiscal accounting element that tells what kind of item or service is being procured~~.~~ Budget object codes are listed in the VA Handbook 4671.2                                                                                                                                                                                                                                                               |
| Budget Sort Category                       | Used by Fiscal Service to identify the allocation of funds throughout their facility.                                                                                                                                                                                                                                                                                                                           |
| Ceiling Transactions                       | Funding distributed from Fiscal Service to IFCAP Control Points for spending. The Budget Analyst initiates these transactions using the Funds Distribution options.                                                                                                                                                                                                                                             |
| Classification of Request                  | An identifier a Control Point can assign to track requests that fall into a category, e.g., Memberships, Replacement Parts, and Food Group III.                                                                                                                                                                                                                                                                 |
| Common Numbering Series                    | This is a pre-set series of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinator establishes the Common Numbering Series used by each facility.                                    |
| Control Point                              | Financial element, existing ONLY in IFCAP that corresponds to the ACC~~S~~ number in FMS. Also, the division of monies to a specified service, activity or purpose from an appropriation.                                                                                                                                                                                                                       |
| Control Point Clerk                        | The user within the service who is designated to input requests and maintain the Control Point records for a Service.                                                                                                                                                                                                                                                                                           |
| Control Point Official                     | The individual authorized to expend government funds for ordering of supplies and services for their Control Point(s). This person has all of the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.                                                                                                                                            |
| Control Point Official's Balance           | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.                                                                                                                                                                                   |
| Control Point Requestor                    | The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. This user can only view or edit their own requests. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&MM/Fiscal.                                                                                                              |
| Cost Center                                | “Subsection” of a Fund Control Point. Cost centers allow fiscal staff to create total expense reports for a section or service, and allow requestors to assign requests to that section or service. Cost centers are listed in the VA Handbook 4671.1.                                                                                                                                                          |
| Date Committed                             | The date that you want IFCAP to commit funds to the purchase.                                                                                                                                                                                                                                                                                                                                                   |
| Default                                    | A suggested response that is provided by the system.                                                                                                                                                                                                                                                                                                                                                            |
| Deficiency                                 | When a budget has obligated and expended more than it was funded (see MP-4, Part V, Section C).                                                                                                                                                                                                                                                                                                                 |
| Delinquent Delivery Listing                | A listing of all the Purchase Orders that have not had all the items received by the Warehouse on IFCAP. It is used to contact the vendor for updated delivery information.                                                                                                                                                                                                                                     |
| Direct Delivery Patient                    | A patient who has been designated to have goods delivered directly to him/her from the vendor.                                                                                                                                                                                                                                                                                                                  |
| Discount Item                              | This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.                                                                                                                                                                                                                                                     |
| EDI Vendor                                 | A vendor with whom the VA has negotiated an arrangement to accept and fill orders electronically.                                                                                                                                                                                                                                                                                                               |
| Electronic Data Interchange (EDI)          | Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.                                                                                                                                                                                                                                                                             |
| Electronic Signature                       | The electronic signature code replaces the written signature on all IFCAP documents used within your facility. Documents going off-station will require a written signature as well.                                                                                                                                                                                                                            |
| Expenditure Request                        | A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).                                                                                                                                                                                                                                                                                        |
| FCP                                        | Fund Control Point (see Control Point).                                                                                                                                                                                                                                                                                                                                                                         |
| Federal Tax ID                             | A unique number that identifies your station to the Internal Revenue Service.                                                                                                                                                                                                                                                                                                                                   |
| Fiscal Balance                             | The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidations submitted against the obligation.                                                                                                                                                                                                                         |
| Fiscal Quarter                             | The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.                                                                                                                                                                                                                                                                                                         |
| Fiscal Year                                | Twelve-month period from October 1 to September 30.                                                                                                                                                                                                                                                                                                                                                             |
| FMS                                        | Financial Management System, the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides for flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.             |
| FOB                                        | Freight on Board. An FOB of "Destination" means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of "Origin" means that shipping charges are due to the shipper and must be paid when the shipper arrives at the warehouse with the item.                                                            |
| FPDS                                       | Federal Procurement Data System.                                                                                                                                                                                                                                                                                                                                                                                |
| FTEE                                       | Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned an FTEE of 0.5, as would a full-time employee that worked for half of a year.                                                                                                                  |
| Fund Control Point                         | See Control Point                                                                                                                                                                                                                                                                                                                                                                                               |
| Funds Control                              | A group of Control Point options that allow the Control Point Clerk and/or Official to maintain and reconcile their funds.                                                                                                                                                                                                                                                                                      |
| Funds Distribution                         | A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.                                                                                                                                                                                                                                                               |
| GBL                                        | Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of \$250.00.                                                                                                                                                                                                                                                                                                    |
| GL                                         | General Ledger.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Imprest Funds                              | Monies used for cash or 3rd party draft purchases at a VA facility.                                                                                                                                                                                                                                                                                                                                             |
| Integrated Supply Management System (ISMS) | ISMS is the system that replaced LOG I for Expendable Inventory. IFCAP sends PHA and PHM transactions to this system.                                                                                                                                                                                                                                                                                           |
| ISMS                                       | Integrated Supply Management System.                                                                                                                                                                                                                                                                                                                                                                            |
| Item File                                  | A listing of items specified by A&MMS as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history.                                                                                                                                                                                                          |
| Item History                               | Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.                                                                                                                                                                                                                                                              |
| Item Master Number                         | A computer generated number used to identify an item in the Item File.                                                                                                                                                                                                                                                                                                                                          |
| Justification                              | A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source.                                                                                                                                                                                                                          |
| Liquidation                                | The amount of money to be paid a vendor. The payment will be posted on the 1358 document and will reduce the Fiscal Balance. They are processed through payment/invoice tracking.                                                                                                                                                                                                                               |
| LOG I                                      | LOG I is the name of the Logistics A&MM computer located at the Austin Data Processing Center. This system continues to support the Consolidated Memorandum of Receipt.                                                                                                                                                                                                                                         |
| Mandatory Source                           | A Federal Agency that sells supplies and services to the VA. VA Supply Depot, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.                                                                                                                                                                                                                                                       |
| MSC Confirmation Message                   | A MailMan message generated by the Austin Message Switching Center that assigns an FMS number to an IFCAP transmission of documents.                                                                                                                                                                                                                                                                            |
| Obligation                                 | The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of an Order.                                                                                                                                                                                                                                                                                                             |
| Obligation (Actual) Amount                 | The actual dollar figure obligated by Fiscal Service for a Purchase Order. The Control Point's records are updated with actual cost automatically when Fiscal obligates the document in IFCAP.                                                                                                                                                                                                                  |
| Obligation Data                            | A Control Point option that allows the Control Point Clerk to enter data not recorded by IFCAP.                                                                                                                                                                                                                                                                                                                 |
| Organization Code                          | Accounting element functionally comparable to Cost Center but used to organize purchases by the budget that funded them, not the purposes for spending the funds.                                                                                                                                                                                                                                               |
| Outstanding 2237                           | A&MM report that lists all the IFCAP generated 2237s pending action in A&MM.                                                                                                                                                                                                                                                                                                                                    |
| PAID                                       | Personnel Accounting Integrated Data.                                                                                                                                                                                                                                                                                                                                                                           |
| Partial                                    | A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.                                                                                                                                                                                                                                                                                            |
| Partial Date                               | The date that a warehouse clerk created a receiving report for a shipment.                                                                                                                                                                                                                                                                                                                                      |
| PAT Number                                 | Pending Accounting Transaction number - the primary FMS reference number.                                                                                                                                                                                                                                                                                                                                       |
| Personal Property Management               | A section of A&MM Service responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process all requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support.                                             |
| PPM                                        | Personal Property Management.                                                                                                                                                                                                                                                                                                                                                                                   |
| Program Code                               | Accounting element that identifies the VA initiative or program that the purchase will support.                                                                                                                                                                                                                                                                                                                 |
| Prompt Payment Terms                       | The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).                                                                                                                                                                                            |
| Purchase History Add (PHA)                 | Procurement History Add transaction. This updates the Procurement History file in Austin when orders are obligated in IFCAP. This same transaction is also used to send a PO for EDI processing.                                                                                                                                                                                                                |
| Purchase History Mod (PHM)                 | Procurement History Modification. This updates the Procurement History file in Austin when orders are amended.                                                                                                                                                                                                                                                                                                  |
| Purchase Order                             | A government document authorizing the purchase of ~~the~~ goods or services at the terms indicated.                                                                                                                                                                                                                                                                                                             |
| Purchase Order Acknowledgment              | Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).                                                                                                                                                                                                                                                                                          |
| Purchase Order Status                      | The status of completion of a purchase order (e.g., Pending Contracting Officer's Signature, Pending Fiscal Action, Partial Order Received, etc.).                                                                                                                                                                                                                                                              |
| Purchasing Agents                          | A&MM employees legally empowered to create purchase orders to obtain goods and services from commercial vendors.                                                                                                                                                                                                                                                                                                |
| Quarterly Report                           | A Control Point listing of all transactions (Ceilings, Obligations, and Adjustments) made to a Control Point's Funds.                                                                                                                                                                                                                                                                                           |
| Quotation for Bid                          | Standard Form 18. Used by Purchasing Agents to obtain written/electronic bids from vendors.                                                                                                                                                                                                                                                                                                                     |
| Receiving Report                           | Report that Warehouse Clerk creates to record that the warehouse has received an item. The VA document used to indicate the quantity and dollar value of the goods being received.                                                                                                                                                                                                                              |
| Reference Number                           | Also known as the Transaction Number. The computer generated number that identifies a request. It is comprised of the Station Number-Fiscal Year-Quarter -Control Point - 4 digit Sequence Number.                                                                                                                                                                                                              |
| Repetitive Item List                       | A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate requests from the list.                                                                                                                                                                                                               |
| Requestor                                  | See “Control Point Requestor.”                                                                                                                                                                                                                                                                                                                                                                                  |
| Requisition                                | The order form used to buy from a Government vendor.                                                                                                                                                                                                                                                                                                                                                            |
| Running Balance                            | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.                                                                                                                                                                                  |
| Section Request                            | A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.                                                                                                                                                                                                                                        |
| Service Balance                            | The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorizations created by the service.                                                                                                                                                                                                 |
| SF-18                                      | Request for Quotation.                                                                                                                                                                                                                                                                                                                                                                                          |
| SF-30                                      | Amendment of Solicitation/Modification of Contract.                                                                                                                                                                                                                                                                                                                                                             |
| Short Description                          | A phrase that describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).                                                                                                                                                                                                        |
| Site Parameters                            | Information (such as Station Number, Cashier's address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter file.                                                                                                                                                                                                                                                 |
| Sort Group                                 | An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.                                                                                                                                                                                                                                                           |
| Sort Order                                 | The order in which the budget categories will appear on the budget distribution reports.                                                                                                                                                                                                                                                                                                                        |
| Special Remarks                            | A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.                                                                                                                                                                                                                                   |
| Stacked Documents                          | The POs, RRs & 1358s that are sent electronically to Fiscal and stored in a file rather than being printed immediately.                                                                                                                                                                                                                                                                                         |
| Status of Funds                            | Fiscal's on-line status report of the monies available to a Control Point. FMS updates this information automatically.                                                                                                                                                                                                                                                                                          |
| Sub-control Point                          | A specific budget within a Control Point, defined by a Control Point user.                                                                                                                                                                                                                                                                                                                                      |
| Sub-cost Center                            | A subcategory of Cost Center. In IFCAP 5.0, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.                                            |
| Tasked Job                                 | A job, usually a printout that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.                                                                                                                                                                                                                                                     |
| TDA                                        | See "Transfer of Disbursing Authority."                                                                                                                                                                                                                                                                                                                                                                         |
| Total Authorizations                       | The total amount of the authorizations created for the 1358 obligation.                                                                                                                                                                                                                                                                                                                                         |
| Total Liquidations                         | The total amount of the liquidation against the 1358 obligation.                                                                                                                                                                                                                                                                                                                                                |
| Transaction Number                         | The number of the transaction that funded a Control Point (See Budget Analyst User's Guide). It consists of the Station Number - Fiscal Year - Quarter - Control Point - Sequence Number.                                                                                                                                                                                                                       |
| Transmission Number                        | A sequential number given to a data string when it is transmitted to the AAC; used for tracking message traffic.                                                                                                                                                                                                                                                                                                |
| Type Code                                  | A set of A&MM codes that provides information concerning the vendor size and type of competition sought on a purchase order.                                                                                                                                                                                                                                                                                    |
| Vendor file                                | An IFCAP file of vendors solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. File 440 contains information about the vendors solicited by your station. The debtor's address may be drawn from this file but is maintained separately. If the desired vendor is not in the file, contact A&MM Service to have it added. |
| Vendor ID Number                           | The ID number assigned to a vendor by FMS.                                                                                                                                                                                                                                                                                                                                                                      |
| VRQ                                        | FMS Vendor Request document. When users send vendor information to FMS, FMS sends a VRQ document to IFCAP with the vendor information, ensuring that the information in the IFCAP vendor file matches the information in the FMS vendor table.                                                                                                                                                                  |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2237, 1-1
Adjusting Purchase Card Orders, 2-10
Amending Purchase Card Orders, 2-10
Authorizations, 1-1
Cost Center, 2-2
Create a Detailed Purchase Card Order, 2-1
Delivery Orders, 1-1
Detailed Purchase Card Order, 2-4
Detailed purchase card orders, 2-1
Editing a Detailed Purchase Card Order, 2-13
Editing a Simplified Purchase Card Order, 2-10
Editing Purchase Card Orders, 2-10
FMS/ET Vendor Code, 1-2
Logistics Data Query Tool, 10-1
Chief Logistics Officer, 10-1
Excel, 10-1
export data, 10-1
Facility Logistics Staff, 10-1
FileMan alternative, 10-1
graphical user interface, 10-1
Inventory Managers, 10-1
Management Analysts, 10-1
Materiel Managers, 10-1
procurement data, 10-1
Prosthetics data, 10-1
Purchasing Agents, 10-1
SPD Technicians, 10-1
Supply System Analysts, 10-1
User Manual
online, 10-1
Warehouse Clerks, 10-1
New Purchase Order, 2-2
PAID, 1-1
Purchase Card Order, 2-16, 3-4
Purchase Order, 2-2, 2-5, 2-7, 2-10, 2-11, 2-12, 2-14, 2-16, 3-1, 3-3
Receipt of item, 5-4
Receiving reports, 2-10, 5-5
Reconciliation, 6-1
Reconciliations, 5-4
Reference Numbering System, 1-1
Requisition, 2-11, 2-14
Simplified purchase card orders, 2-1, 2-4
Simplified Purchase Card Orders, 2-1
