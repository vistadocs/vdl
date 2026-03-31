---
title: IFCAP Version 5.1 Control Point Official User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Control Point Official User's Guide
app_code: PRC
app_name: IFCAP
section: FIN
app_status: active
pkg_ns: PRC
patch_ver: 5.1
patch_id: PRC*5.1
group_key: "PRC:PRC:5.1"
file_numbers: 
  - 410
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - strong
  - control
  - class
  - point
  - table
  - request
  - transaction
  - number
  - ifcap
  - span
page_count: 0
word_count: 52775
section_count: 36
table_count: 29
figure_count: 1
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1cp_official.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1cp_official.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

Integrated Funds Distribution Control Point Activity, Accounting and Procurement (IFCAP)Version 5.1Control Point OfficialUser’s Guide

![](ifcap-version-5-1-control-point-official-user-s-guide/001.png)

March 2026Department of Veterans AffairsOffice of Information and Technology (OI&T)Management, Enrollment, and Financial Systems

Revision History

Initiated 12/29/04

<table>
<caption><p><span id="_Toc166316025" class="anchor"></span>Table 1: Icons Used in Boxed Notes</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 49%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>March 2026</td>
<td>9.4</td>
<td><p>Updates based on patch PRC*5.1*257.</p>
<p>This manual has been updated to comply with the VA OIT mandated user guide template.</p></td>
<td><p>Project Manager, Technical Writer</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="even">
<td>September 2025</td>
<td>9.3</td>
<td><p>Patch PRC*5.1*247</p>
<p>Removed PRCHL GUI Logistics Data Query Tool</p></td>
<td><p>Project Manager, Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td><p>August</p>
<p>2018</p></td>
<td>9.2</td>
<td>Patch XU*8.0*679. Added note regarding Electronic Signature Block restrictions. Page <a href="#XU_80_679"><u>19</u></a>.</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td><p>May</p>
<p>2016</p></td>
<td>9.1</td>
<td>Patch PRC*5.1*184. Corrected ADJUSTMENT $ AMOUNT wording. Page 9-93.</td>
<td><p>Project Manager, Technical Writer, Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td><p>January</p>
<p>2014</p></td>
<td>9.0</td>
<td><p>Patch PRC*5.1*174 (IFCAP/eCMS Interface)</p>
<ul>
<li><p>3.3.3 – updated “Table 3-2 Menu Option / Security List” with Transaction Report – eCMS/IFCAP menu option.</p></li>
<li><p>4.1 – Figure 4-1 removed Enter/Edit Control Point User option.</p></li>
<li><p>4.1 – removed Enter/Edit Control Point User option description text.</p></li>
<li><p>5.2.2 – added a “Note: …the Control Point Clerk may encounter missing required fields when converting a temporary request to a 2237 transaction. The Clerk will be advised of the missing field(s) and be allowed to edit the new 2237 and populate the required fields…”</p></li>
<li><p>5.2.3 – updated “Figure 5.3 with “If the 2237 has any required fields that are not populated – the User will not be prompted to set the Ready for approval flag to YES. All required fields must be populated before the 2237 can be moved to the Official for Approval.”</p></li>
<li><p>6.1.1 – updated Setup Parameters</p></li>
<li><p>6.1.2 – updated screen capture</p></li>
<li><p>6.1.3 – updated screen capture</p></li>
<li><p>6.1.4 – updated screen capture</p></li>
<li><p>6.1.5 – deleted 6.1.5 Record Type Help Text and replaced with 6.1.5 Report Example</p></li>
<li><p>8.2.3 – updated/added Status and Node Assignments</p></li>
<li><p>9.3.1.2 – replaced “Sent to eCMS” with “Accepted by eCMS”</p></li>
<li><p>9.3.3.2 – replaced “Sent to eCMS” with “Accepted by eCMS”</p></li>
<li><p>9.4.1.3- changed Note text to identify as required field.</p></li>
<li><p>9.4.1.5 – added “NOTE: Description is now a Required field on all 2237s.” An item description is now required.</p></li>
<li><p>9.4.1.8 – added “NOTE: You will not be prompted to set this request to YES if there is a Required field that is not populated.”</p></li>
<li><p>9.4.3.1 – changed sentence from “Use this option to print or display a request.” to “Use this option to print or display a 2237 or a temporary request.”</p></li>
<li><p>9.4.3.2 – replaced “Sent to eCMS” with “Accepted by eCMS”</p></li>
<li><p>9.4.4 – replaced “Use this option to correct the fiscal year or fiscal quarter of the order…” with “Use this option to correct the fiscal year or fiscal quarter of the 2237…”</p></li>
<li><p>9.4.4.2 – replace “IFCAP will change the transaction number and show you the new transaction number. IFCAP will give you another chance to edit the request, and show… with “IFCAP will create a duplicate 2237 with a new transaction number - Cancel the original 2237 transaction - and give you the chance to edit the new 2237 request. If there are Required fields that are not populated – you will be prompted to enter the required data. You will be shown… After “You will be shown the current Control Point balance, the estimated cost of the request, and the total uncommitted balance from current and prior quarters.” Add the following sentence: “If any of the required fields are not populated FCAP will not ask if the 2237 is ready for Approval.”</p></li>
<li><p>9.4.4.2 – Figure 9.63 - Edit Data: Updated screen capture to show the original transaction cancelled and the new transaction checked to ensure that all Required fields are populated.”</p></li>
<li><p>9.4.5.1- replaced Sent to eCMS with Accepted by eCMS</p></li>
<li><p>9.4.5.2 –added “NOTE: When an IFCAP User cancels a 2237, the Name of the User and the Date/Time of the cancellation are now stored in the 2237 record in the Control Point Activity file (#410).”</p></li>
<li><p>9.4.8.2 –new screen capture and replaced “Sent to eCMS” with “Accepted by eCMS”.</p></li>
<li><p>9.4.8.3 – replaced fiscal year prompt “Select FISCAL YEAR: 94//”with “Select FISCAL YEAR: 13//”</p></li>
<li><p>9.4.8.4 - replace “The form type for this request is ISSUE BOOK/INTERVAL ISSUE//” with “The form type for this request is: REPETITIVE &amp; NON-REPETITIVE”. Added note about new Required field.</p></li>
<li><p>9.4.8.5 – added “NOTE: If any of the Required fields are not populated, you will not be able to set the request to YES ready for Control Point Official approval.” Also added new screen capture for special remarks.</p></li>
<li><p>9.4.8.5 – Added note re. required fields.</p></li>
</ul></td>
<td><p>Project Manager, Technical Writer, Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>September 2013</td>
<td>8.0</td>
<td>Patch PRC*5.1*171. Removed Chapter 5, renumbered subsequent chapters. Removed option Enter/Edit Control Point Users from menus.</td>
<td><p>Project Manager, Technical Writer, Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>September 2012</td>
<td>7.0</td>
<td><p>Patch PRC*5.1*167 (eCMS Interface to IFCAP) updates:</p>
<ul>
<li><p>Updated menu options and commands in chapters 7 and 13.</p></li>
<li><p>Conducted general editorial review.</p></li>
<li><p>Chapter 7 – Pg 7-1 Added a statement that this report only lists transactions that have been returned by eCMS.</p></li>
<li><p>10.4.5.1 – pg. 10-55, updated second Note: box – warns CP Official to not cancel transaction that has been sent to eCMS. Control Point Official may not be able to cancel any transactions after it has been sent to Supply &amp; Fiscal (Signed/approved by FCP Official) unless it is returned to the FCP.</p></li>
<li><p>13.1 – pg. 13-1, Deleted “A new Status, “To IFCAP Ordering Officer,” is placed on the 2237 and an IFCAP Purchasing Agent may include the 2237 in a Purchase Order or if appropriate, a Requisition Clerk can include the 2237 in a Requisition.”</p></li>
<li><p>13.3 – Pg 13-2, Added comment about making the determination to cancel in conjunction with the FCP user. The eCMS user absolutely should not make this decision unilaterally. Added “After communicating with the FCP User an eCMS user may decide…”</p></li>
</ul></td>
<td><p>Project Manager, Technical Writer, Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>October 2011</td>
<td>6.0</td>
<td>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358. See pages <a href="#select-temporary-1358-transaction">6-3</a>, <a href="#PRC_158_B">9-27</a>, <a href="#display-4">9-84</a>, <a href="#PRC_158_1">13-1</a>.</td>
<td><p>Project Manager, Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>01/05/11</td>
<td>5.0</td>
<td>Addresses changes made in support of Segregation of Duties patch PRC*5.1*148 See: 9.5.1.3, 9.5.1.7. Removed references to the Obligation Data option.</td>
<td><p>Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>3/05/2008</td>
<td>4.0</td>
<td>Added documentation about new menu option PRCHPM CS PURGE ALL</td>
<td><p>SQA Analyst</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>05/31/07</td>
<td>3.0</td>
<td>Added information covering the use of the Logistics Data Query Tool (LDQT), per patch PRC*5.1*103.</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>02/06/06</td>
<td>2.0</td>
<td>Added New option, Print Obligated 1358s, per patch PRC*5.1*79.</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="odd">
<td>12/29/04</td>
<td>1.1</td>
<td>PDF file checked for accessibility to readers with disabilities.</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>12/29/04</td>
<td>1.0</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td>Department of Veterans Affairs</td>
</tr>
</tbody>
</table>

<span id="_Toc166316025" class="anchor"></span>Table 1: Icons Used in Boxed Notes

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Introduction](#introduction)
  - [The Role of the Control Point Official](#the-role-of-the-control-point-official)
  - [How to Use This Guide](#how-to-use-this-guide)
    - [Hypertext and Hyperlinks](#hypertext-and-hyperlinks)
    - [Procedure Steps](#procedure-steps)
    - [Typographical Conventions](#typographical-conventions)
  - [FileMan Date Conventions](#fileman-date-conventions)
- [The Role of the Control Point Official](#the-role-of-the-control-point-official-1)
  - [Control Point Official Responsibilities](#control-point-official-responsibilities)
  - [References](#references)
    - [The IFCAP Monograph](#the-ifcap-monograph)
    - [The IFCAP User’s Guide Series](#the-ifcap-users-guide-series)
    - [Other Documentation](#other-documentation)
- [System Security](#system-security)
  - [Security Levels](#security-levels)
  - [System Access](#system-access)
  - [Menu and Security Keys](#menu-and-security-keys)
    - [Menus](#menus)
    - [Security Keys](#security-keys)
    - [Security Keys/Mail Groups](#security-keysmail-groups)
  - [Electronic Signature Codes](#electronic-signature-codes)
    - [Changing Your Electronic Signature Code](#changing-your-electronic-signature-code)
- [Operation](#operation)
  - [IFCAP Control Point Official Menu](#ifcap-control-point-official-menu)
  - [Using IFCAP Files](#using-ifcap-files)
  - [The Financial Management System](#the-financial-management-system)
    - [Sub-Allowance Reconciliation](#sub-allowance-reconciliation)
    - [Rollover of Funds from Previous Quarters](#rollover-of-funds-from-previous-quarters)
    - [Amendment Processing](#amendment-processing)
  - [Introduction](#introduction-1)
  - [Convert a Temporary 2237 Request](#convert-a-temporary-2237-request)
    - [Menu Path](#menu-path)
    - [Select Temporary 2237 Transaction](#select-temporary-2237-transaction)
    - [Edit Data on the 2237 Transaction](#edit-data-on-the-2237-transaction)
  - [Change a Temporary 1358 Transaction](#change-a-temporary-1358-transaction)
    - [Select Temporary 1358 Transaction](#select-temporary-1358-transaction)
    - [Edit Data on the 1358 Transaction](#edit-data-on-the-1358-transaction)
  - [Reject a Request](#reject-a-request)
    - [Menu Path](#menu-path-1)
    - [Select Transaction Number](#select-transaction-number)
    - [Notify the Requestor](#notify-the-requestor)
  - [Approve a 2237 Request](#approve-a-2237-request)
    - [Menu Path](#menu-path-2)
    - [Select a Transaction](#select-a-transaction)
  - [Approve a 1358 Request](#approve-a-1358-request)
    - [Menu Path](#menu-path-3)
    - [Select a 1358 Transaction](#select-a-1358-transaction)
- [Transaction Report - IFCAP/eCMS](#transaction-report-ifcapecms)
  - [Menu Navigation](#menu-navigation)
    - [Setup Parameters](#setup-parameters)
    - [Date Range Help Text](#date-range-help-text)
    - [Station Number Help Text](#station-number-help-text)
    - [Fund Control Point Help Text](#fund-control-point-help-text)
    - [Report Example](#report-example)
- [# How to Monitor Your Control Point Balance](#how-to-monitor-your-control-point-balance)
  - [Introduction](#introduction-2)
  - [Monitor the Balance of Your Control Point](#monitor-the-balance-of-your-control-point)
    - [Setup Parameters](#setup-parameters-1)
    - [Setting Report Parameters](#setting-report-parameters)
    - [Transaction Listing](#transaction-listing)
    - [FMS Transaction Listing](#fms-transaction-listing)
- [How to Determine the Status of a Request](#how-to-determine-the-status-of-a-request)
  - [Introduction](#introduction-3)
  - [Determine the Status of a Transaction](#determine-the-status-of-a-transaction)
    - [Menu Path](#menu-path-4)
    - [Display](#display)
    - [Status](#status)
- [Supplemental Control Point Official Options](#supplemental-control-point-official-options)
  - [Introduction](#introduction-4)
  - [Options in the Funds Control Menu](#options-in-the-funds-control-menu)
    - [Enter FCP Adjustment Data](#enter-fcp-adjustment-data)
    - [Assigning Ceiling to Sub-Control Points](#assigning-ceiling-to-sub-control-points)
    - [Recalculate Fund Control Point Balance](#recalculate-fund-control-point-balance)
    - [Options in the Funds Control Reports Menu](#options-in-the-funds-control-reports-menu)
    - [Correct Sub-Control Point Amounts](#correct-sub-control-point-amounts)
  - [Options in the Status of Requests Reports Menu](#options-in-the-status-of-requests-reports-menu)
    - [Print/Display Request Form](#printdisplay-request-form)
    - [Status of All Obligation Transactions](#status-of-all-obligation-transactions)
    - [PO with Associated Transactions](#po-with-associated-transactions)
    - [Requests Ready for Approval List](#requests-ready-for-approval-list)
  - [Options in the Process a Request Menu](#options-in-the-process-a-request-menu)
    - [New 2237 (Service) Request](#new-2237-service-request)
    - [Edit a 2237 (Service)](#edit-a-2237-service)
    - [Print/Display Request Form](#printdisplay-request-form-1)
    - [Change Existing Transaction Number](#change-existing-transaction-number)
    - [Cancel Transaction with Permanent Number](#cancel-transaction-with-permanent-number)
    - [Options in the Requestor's Menu](#options-in-the-requestors-menu)
    - [Options in the Repetitive Item List Menu](#options-in-the-repetitive-item-list-menu)
    - [Copy a Transaction](#copy-a-transaction)
    - [Item Display](#item-display)
    - [Vendor Display](#vendor-display)
    - [Outstanding Approved Requests Report](#outstanding-approved-requests-report)
  - [Options in the 1358 Request Menu](#options-in-the-1358-request-menu)
    - [New 1358 Request](#new-1358-request)
    - [Increase/Decrease Adjustment](#increasedecrease-adjustment)
    - [Edit 1358 Request](#edit-1358-request)
    - [Create/Edit Authorization](#createedit-authorization)
    - [Daily Activity Enter/Edit](#daily-activity-enteredit)
    - [Recalculate 1358 Balance](#recalculate-1358-balance)
    - [Display 1358 Balance](#display-1358-balance)
    - [List 1358's with Open Authorizations](#list-1358s-with-open-authorizations)
    - [Print 1358](#print-1358)
    - [Obligated 1358s](#obligated-1358s)
  - [Options on the Display Control Point Activity Menu](#options-on-the-display-control-point-activity-menu)
    - [Purchase Order Status](#purchase-order-status)
    - [Temporary Transaction Listing](#temporary-transaction-listing)
    - [Transaction Status Report](#transaction-status-report)
    - [Running Balances](#running-balances)
    - [Item History](#item-history)
    - [PPM Status of Transactions Report](#ppm-status-of-transactions-report)
  - [Options in the Record Date Received by Service Menu](#options-in-the-record-date-received-by-service-menu)
    - [Single Transaction](#single-transaction)
    - [All Transactions with Final Partials](#all-transactions-with-final-partials)
- [Menu Listing](#menu-listing)
- [IFCAP/eCMS Interface (2237 Processing)](#ifcapecms-interface-2237-processing)
  - [Returned to Accountable Officer from eCMS](#returned-to-accountable-officer-from-ecms)
    - [MailMan Message – 2237 Returned to AO](#mailman-message-2237-returned-to-ao)
  - [Returned to Control Point Users](#returned-to-control-point-users)
    - [MailMan Message: Return 2237 to Control Point](#mailman-message-return-2237-to-control-point)
  - [Cancelled in IFCAP by eCMS](#cancelled-in-ifcap-by-ecms)
    - [MailMan Message: Cancel 2237](#mailman-message-cancel-2237)
- [Error Messages and Their Resolution](#error-messages-and-their-resolution)
  - [User Errors](#user-errors)
  - [System Errors](#system-errors)
- [Glossary](#glossary)
- [Index](#index)
This guide is designed to provide you, the Control Point Official, with the information necessary to perform your job. The IFCAP package automated certain functions in Acquisition and Materiel Management (A&MM), Fiscal Service, and in all of the services that request supplies and services on Veterans Affairs (VA) Form 90-2237. The goal of IFCAP is to integrate these three areas and allow users to share procurement information. IFCAP has the following components or “modules.”
- FUNDS DISTRIBUTION allows Fiscal Service to establish Fund Control Points and track funding for budget purposes.
- CONTROL POINT ACTIVITY automates the preparation of requests, the electronic transmission of requests to A&MM and Fiscal services, and the bookkeeping processes within a service.
- PROCUREMENT allows A&MM to transfer IFCAP-generated requests onto purchase orders and requisitions, process receiving documents in the warehouse, and create and transmit code sheets to Austin.
- ACCOUNTING automates the creation of code sheets, handles the processing of certified invoices, and facilitates the electronic transmission of code sheets and receiving documents to the Financial Management System (FMS) located in Austin, Texas. In addition, IFCAP transfers obligation information back to the Control Point and updates the Control Point balance automatically.
- INVENTORY permits services to maintain their own on-line inventory and establish an average stock level, record the distribution of goods to secondary location(s), and automatically generate IFCAP requests for replenishment purposes. Secondary locations may maintain their own inventory.
- RFQ enables the Purchasing Agent (PA) to create a Request for Quotation (RFQ), evaluate bids, award the order, and generate the purchase order. Using IFCAP and the Electronic Data Interchange (EDI) functionality in Austin, the PA can electronically send the RFQ to one or more vendors and receive their bids electronically
- PURCHASE CARD permits users at the Service-level and in A&MM to generate purchase orders against assigned credit card(s). Charges are passed electronically from the Austin Credit Card System (CCS) to IFCAP, and users reconcile payments with IFCAP Purchase Orders. The assigned Approving Official then approves reconciled orders. The local IFCAP Purchase Card Registration file is maintained by the station designated Purchase Card Coordinator. Reconciled orders are then approved by assigned Approving Officials. There are many reports that provide data on the status of the purchase card orders and timeliness of the reconciliation and approval processes.
- DELIVERY ORDERS permits users to generate purchase orders for contract items at the Service-level. Using switches that are site configurable, orders can pass Fiscal and be obligated at time of signing by Service-level staff.
Table of Contents
Tables:
Figures:

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The Role of the Control Point Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You have been selected as an Integrated Funds Distribution, Control Point Activity, Accounting, and Procurement (IFCAP) Control Point Official. You probably have many questions about your new role and are eager for information. The *Control Point Official User’s Guide* will provide you with guidance and training for your new responsibilities.

Control Point Officials approve requests, reconcile the financial records of their Control Point, and authorize users to be Requestors, Control Point Clerks, or Control Point Officials for the Control Point. As Control Point Requestors create requests, Control Point Clerks turn their requests into transactions, which the Control Point Official rejects or approves and sends to Personal Property Management (PPM) or Fiscal Service, who orders the goods or services, and obligates (sets aside) money for the purchase.

This guide will teach you how to use IFCAP to approve and reject requests, monitor the balance of your Control Point and determine the status of a request.

## How to Use This Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide explains how to perform the role of the Control Point Official by dividing that role into small, manageable tasks. The authors of this guide have listed these tasks in successive order so that each instruction builds on the functionality and information from the previous instructions. This will allow new Control Point Officials to use this guide as a tutorial by following the instructions from beginning to end. Experienced Control Point Officials can use this guide as a reference tool by using the index and table of contents.

Before you plunge into learning about your job as Control Point Official, please take a few moments to familiarize yourself with how this guide is put together.

<table>
<caption><p><span id="_Toc166316026" class="anchor"></span>Table 2: IFCAP User’s Guides</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th>STEP 1.</th>
<th>Read all of 1. It explains how to interpret the graphics and typestyles used in this guide.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>STEP 2.</td>
<td><p>If this is your first exposure to using VistA, you should become familiar with terminology and functions that are used throughout VistA applications. There are several manuals and guides that provide a foundation for use of <em>Kernel</em>, <em>FileMan</em>, and <em>MailMan</em> (<em>see</em> Glossary). These documents replace the old <em>DHCP User’s Guide to Computing</em>, which is obsolete. You will find these at:</p>
<p><em>Kernel:</em> <a href="http://www.va.gov/vdl/application.asp?appid=10">http://www.va.gov/vdl/application.asp?appid=10</a></p>
<p><em>FileMan:</em> <a href="http://www.va.gov/vdl/application.asp?appid=5">http://www.va.gov/vdl/application.asp?appid=5</a></p>
<p><em>MailMan:</em> <a href="http://www.va.gov/vdl/application.asp?appid=15">http://www.va.gov/vdl/application.asp?appid=15</a></p></td>
</tr>
<tr class="even">
<td>STEP 3.</td>
<td>Read the remainder of this guide.</td>
</tr>
</tbody>
</table>

<span id="_Toc166316026" class="anchor"></span>Table 2: IFCAP User’s Guides

### Hypertext and Hyperlinks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document contains “hypertext” that provides links to other parts of this document or to other related documents. Hypertext is a computer-based text retrieval system that enables you to access particular locations in electronic documents by clicking on hyperlinks in those documents. If you are viewing this document on your computer screen (as opposed to reading a printed copy), you will find certain hyperlinked words or phrases.

- An internal or “cross-reference” hyperlink allows you to “jump” to another part of this document. Typically, these hyperlinks will be imbedded in sentences like “See the IFCAP Glossary in 12.” Although such internal cross-references may not be shown in blue, if you move your mouse over such phrases, a pop-up box will display the link, like this:

![](ifcap-version-5-1-control-point-official-user-s-guide/002.png)

> If you have the Web toolbar enabled in your copy of Word, just click the back ![](ifcap-version-5-1-control-point-official-user-s-guide/003.png) icon on the toolbar to return to where you jumped from.

- Another kind of internal hyperlink uses “bookmarks” to direct you to other locations in this document. These are normally presented in a blue font. Again, click the back ![](ifcap-version-5-1-control-point-official-user-s-guide/004.png) icon on the toolbar to return to the point where you jumped from.

Links to web pages or Internet sites should open in your web browser (typically *Internet Explorer*®). Use the browser’s “back” button to return to this document. Since *Internet Explorer* and *Word* are both Microsoft products, do *not* close the browser window, since this may (under certain circumstances) also close this document.

- Links to some external documents (for example, other Word documents) may (depending on your system settings) open in Word. Such links are also usually presented in a blue font. For example, note the shortcut graphic with blue hyperlink to the other online documents shown in the boxed note below. Use the back ![](ifcap-version-5-1-control-point-official-user-s-guide/005.png) icon to return to where you jumped from.

In either case, you may click (or, depending on your computer’s operating system or software version, you may have to hold down the \<Ctrl\> key while clicking) on the link to see the other document or move to the specified place in this document.

### Procedure Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Procedures that you perform in an exact order will list the steps involved. Look for Step numbers as in the following samples:

| STEP 1. | Select the FMS Exception option.                                                                                          |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| STEP 2. | Enter the latest date that you want to retain entries. IFCAP will delete all entries recorded before that retention date. |

<span id="_Toc166316027" class="anchor"></span>Table 3: Other IFCAP Documentation

> There are also paragraphs that simply discuss a process. In these instances, you do not need to perform any process discussed using a particular order.

### Typographical Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide uses a few conventions to help identify, clarify, or emphasize information.

- Type: The word “type” is used in this guide to mean straightforward typing at your terminal keyboard.
- Keys: In this guide, computer keys that you press, but which do not result in words appearing on your screen, are represented inside \<angle brackets\> using the r_ansi font (examples: \<Ctrl\>+\<S\>, \<Enter\>).
- \<Enter\>: The term \<Enter\> is used to indicate that you must send whatever you have been typing on your keyboard to the computer. When you have completed typing your response, you send it to the computer by pressing the return or enter key once.
- Emphasis: Italic text (such as *must* or *not*) is used to emphasize or draw your attention to a situation or process to perform. Pay close attention to statements containing italic text.
- Program and Utility Names: Names of software programs and utilities appear in bold type (like FileMan).
- Menus, Options, File and Field Names: Names of menus, menu options, files, and similar items are shown in the r_ansi font (as in “Select the FMS Exception option”).
- Alert Icons: Whenever you need to be aware of something important or informative, the Guide will display a boxed note with an icon to alert you; icons are shown in Error! Not a valid bookmark self-reference.. Look for these icons in the left and right margins of the document.

<table>
<caption><p><span id="_Toc166316028" class="anchor"></span>Table 4: Security Key / Mail Group</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th>Icon</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-control-point-official-user-s-guide/006.png)</td>
<td><strong>Warning</strong>: Something that could adversely affect your use of the Query Tool or of the material available in the IFCAP databases.</td>
</tr>
<tr class="even">
<td>![](ifcap-version-5-1-control-point-official-user-s-guide/007.png)</td>
<td><strong>Tip</strong>: Advice on how to more easily navigate or use the Guide or the software.</td>
</tr>
<tr class="odd">
<td>![](ifcap-version-5-1-control-point-official-user-s-guide/008.png)</td>
<td><strong>Information</strong>: or <strong>Note:</strong> Additional information that might be helpful to you or something you need to know about, but which is not critical to understanding or use of the software.</td>
</tr>
<tr class="even">
<td>![](ifcap-version-5-1-control-point-official-user-s-guide/009.png)</td>
<td><strong>Technical Note:</strong> Information primarily of interest to software developers, IRM or Enterprise VistA Support (EVS) personnel. Most users can usually safely ignore such notes.</td>
</tr>
<tr class="odd">
<td><p>![](ifcap-version-5-1-control-point-official-user-s-guide/010.png)</p>
<p>![](ifcap-version-5-1-control-point-official-user-s-guide/011.png)</p></td>
<td><strong>Question:</strong> A question that might come to your mind (hopefully, followed by an <strong>Answer</strong>!)</td>
</tr>
</tbody>
</table>

<span id="_Toc166316028" class="anchor"></span>Table 4: Security Key / Mail Group

## FileMan Date Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout the guide, *FileMan* date conventions have been used. A date-valued response can be entered into FileMan in a variety of ways. The following is a typical help prompt for a date field:

<table>
<caption><p><span id="_Ref153165504" class="anchor"></span>Table 5: Menu Option / Security Key List</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Examples of Valid Dates:</strong></p>
<p><strong>JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057</strong></p>
<p><strong>T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.</strong></p>
<p><strong>T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.</strong></p>
<p><strong>If the year is omitted, the computer uses CURRENT YEAR. Two digit year</strong></p>
<p><strong>assumes no more than 20 years in the future, or 80 years in the past.</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref153165504" class="anchor"></span>Table 5: Menu Option / Security Key List

|                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-control-point-official-user-s-guide/012.png) | *<u>NOTE:</u>* If you do not specify the year when you enter a date, IFCAP will assume that you are referring to the current calendar year. This could cause some confusion around the fiscal year turnover period when you are more likely to be entering dates for next year (when the current Fiscal Year is the same as the next Calendar Year). | ![](ifcap-version-5-1-control-point-official-user-s-guide/013.png) |

<span id="_Ref222296145" class="anchor"></span>Table 6: Status and Node Assignment

# The Role of the Control Point Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Control Point Official Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a Control Point Official, you may create, edit and approve requests assigned to a Control Point you are authorized to use. To use a Control Point, the Control Point Official for that Control Point has to provide access. If a user’s access is limited to the Control Point Requestor or Control Point Clerk level, IFCAP will require the Control Point Official to approve all transactions that user creates before transmitting them to Personal Property Management (2237s and Issue Book requests) or Accounting (1358s). This is because the Control Point Official is responsible for approving all expenditure for the Control Point location.

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The IFCAP Monograph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To get an overview of what IFCAP is all about, you might want to take a look at the IFCAP Monograph. It’s available via a separate link near the top of the VDL page (just above the table which lists the other documents) or via this link:
> <https://www.va.gov/vdl/application.asp?appid=239>

### The IFCAP User’s Guide Series

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The series of IFCAP User’s Guides was designed to follow the functions which IFCAP provides and the “roles” which users play at various times within IFCAP. Consequently, these guides are known as “role-based” guides. The person performing a given role may or may not actually hold the position title indicated in the guide – but within IFCAP, that person carries out the duties associated with the role that is being performed.
Error! Not a valid bookmark self-reference. lists the documentation you may need when performing Application Coordinator functions. The listed documents are available online at the Vista Document Library (VDL):
<http://www.va.gov/vdl/application.asp?appid=42>
<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Guide Name</strong></th>
<th><strong>Description and Use</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Accounting Technician User’s Guide</td>
<td>Provides the information needed to process an obligation, receiving report or amendment using IFCAP. In addition, it shows how to create or edit FMS documents that will be transmitted to FMS. All Accounting Technicians at your facility should be given a copy of the <em>Accounting Technician Manual</em>.</td>
</tr>
<tr class="even">
<td>Application Coordinator User’s Guide</td>
<td>Provides guidance to Application Coordinators when implementing IFCAP at a facility. This guide also contains information on options permitting Application Coordinators to enter the station address, common PAT numbering series, and the proper printer locations used by all IFCAP users.</td>
</tr>
<tr class="odd">
<td>Budget Analyst User’s Guide</td>
<td>This guide is used by the Budget Analyst, generally a person in Fiscal Service. It describes how to enter Ceiling Transactions that fund all Control Points. The Fiscal employee responsible for processing Transfers of Disbursing Authority (TDAs) and assigning ceilings to Control Points should be given a copy of the <em>Budget Analyst User’s Guide</em>.</td>
</tr>
<tr class="even">
<td>Control Point Clerk User’s Guide</td>
<td>This guide is used by those individuals who are responsible for creating requests (2237s, 1358s, etc.) that will be approved by their Control Point Official. The Control Point Clerks at your facility should be given a copy of the <em>Control Point Clerk User’s Guide</em> and the <em>Control Point Requestor User’s Guide</em>.</td>
</tr>
<tr class="odd">
<td>Control Point Official User’s Guide</td>
<td>This guide should be given to those individuals responsible for the management of Fund Control Point money. These users have been designated as the authority to approve requests for goods and services. There may be more than one Control Point Official for a Funds Control Point. This guide briefly covers those options used exclusively by the Control Point Official, including Approve Requests and Enter/Edit Control Point Users. In most cases, the Control Point Official is only concerned with approving requests. The other options that make up the Control Point Official’s menu are discussed in the Control Point Clerk’s guide. The Control Point Officials at your facility should be given a copy of the <em>Control Point Official User’s Guide</em>, the <em>Control Point Clerk User’s Guide</em>, and the <em>Control Point Requestor User’s Guide</em>.</td>
</tr>
<tr class="even">
<td>Control Point Requestor User’s Guide</td>
<td>This guide is used by those individuals that create temporary requests (2237s, 1358s, etc.) but do not have access to the Control Point balance. The Requestors at your facility should be given a copy of the <em>Control Point Requestor User’s Guide</em>.</td>
</tr>
<tr class="odd">
<td>Delivery Order User’s Guide</td>
<td>This guide contains the functionality to permit Service level staff to generate orders for contracted items and depending on switch settings at the site to obligate them without passing them through Fiscal service. A copy of this guide should be provided to those staff members who are going to place orders for contract items.</td>
</tr>
<tr class="even">
<td>Generic Inventory User’s Guide</td>
<td><p>This guide describes the full functionality of the IFCAP Inventory system, which includes a warehouse; primary inventories that may or may not maintain a perpetual inventory; and secondary inventories (created by a primary), also maintaining perpetual inventory. The options also are included to control a dependent inventory point from the warehouse (Issue Book Processing option) or from the primary inventory (Stock Item Distribution Menu). While the warehouse, primary and secondary inventory are separate parts of the inventory system, the menu options for controlling stock in all three are identical in most respects. The differences lie in the stock request, stock distribution, and management functions.</p>
<p><em>See also</em> the <em>Point of Use Manual</em> (<a href="http://www.va.gov/vdl/application.asp?appid=42">http://www.va.gov/vdl/application.asp?appid=42</a>).</p></td>
</tr>
<tr class="odd">
<td>PPM Accountable Officer User’s Guide</td>
<td>This guide describes the options that may be used by the Accountable Officer, Requisition Clerk, Warehouse staff and other PPM employees.</td>
</tr>
<tr class="even">
<td>Purchase Card User’s Guide</td>
<td>This guide contains full functionality to enable the site Card Coordinator to maintain the Registration file for Purchase Cards. It also contains the functionality for Service level and A&amp;MM staff to create purchase card orders which will be charged against assigned credit cards and reconciled against the charges received from the Austin Credit Card System (CCS). It also contains functionality for designated Approving Officials to approve a reconciliation done by a cardholder. All staff placing orders using government credit cards and their designated approving officials should be given a copy of this guide. A copy of the Purchase Card Coordinator’s part of the guide should be given to the person designated as the site Purchase Card Coordinator.</td>
</tr>
<tr class="odd">
<td>Purchasing Agent User’s Guide</td>
<td>This guide describes the options used to create, edit and display a Purchase Order, a Vendor, or an Item purchased on a repetitive basis. It contains the options that enable the Purchasing Agent (PA) to generate and process Requests for Quotation. In addition, the guide provides information concerning the printing of various management reports. The PAs at your facility should be given a copy of the <em>Purchasing Agent User’s Guide</em>.</td>
</tr>
<tr class="even">
<td>Requirements Analyst User’s Guide</td>
<td>This guide provides guidance for options used by the Requirements Analyst under the Personal Property Management (PPM) section of the Acquisition and Materiel Management (A&amp;MM). Service. These options are used to process requests and requisitions for Supply Fund and to create code sheets.</td>
</tr>
<tr class="odd">
<td>Requisition Clerk User’s Guide</td>
<td>This guide provides guidance for options used by Personal Property Management (PPM) personnel who process requisitions and Integrated Supply Management System (ISMS) / General Services Administration (GSA) / Defense Logistics Agency (DLA) code sheets.</td>
</tr>
<tr class="even">
<td>Voucher Audit Clerk User’s Guide</td>
<td>This guide explains how to use the options in the Payment/Invoice Tracking Menu of the IFCAP System to build and maintain an invoice tracking system. The Voucher Audit Clerk inspects invoices, maintains invoice records, and records and/or edits payment information.</td>
</tr>
<tr class="odd">
<td>Warehouse Clerk User’s Guide</td>
<td>This guide describes the process of receiving goods on the IFCAP system. All warehouse staff at your facility should be given a copy of the Warehouse Guide.</td>
</tr>
</tbody>
</table>

### Other Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Other documentation is available. These documents are listed in Error! Not a valid bookmark self-reference..
<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Manual or Guide Name</strong></th>
<th><strong>Description and Use</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Point of Use Manual</td>
<td><p>This guide describes the set up and functionality related to interfacing the inventory in a Secondary Inventory Point such as on a ward with an automated supply station.</p>
<p>It supplements—but does not replace— the <em>Generic Inventory User’s Guide</em>. It’s useful to programmers, site managers, and IRM technical staff setting up or maintaining the point of use interface. It is also useful to all Acquisition &amp; Materiel Management (A&amp;MM) personnel utilizing GIP.</p></td>
</tr>
<tr class="even">
<td>DynaMed-IFCAP Implementation Guide</td>
<td>Describes the interface between <em>DynaMed</em>® (a commercial, off-the-shelf software package) and IFCAP. As of Oct. 2010, at Bay Pines VAMC <em>only,</em> <em>DynaMed</em> is used to control inventory.</td>
</tr>
<tr class="odd">
<td>Package Security Guide</td>
<td>Specifies parameters controlling the release of sensitive information related to IFCAP.</td>
</tr>
<tr class="even">
<td>Release Notes and Installation Guide</td>
<td>Provides information on how to install the latest version of IFCAP at a site.</td>
</tr>
<tr class="odd">
<td>Technical Manual</td>
<td>Provides technical information about the IFCAP package, including information to assist programmers, site managers, and Information Resources Management (IRM) technical personnel to operate, maintain, and troubleshoot IFCAP software.</td>
</tr>
<tr class="even">
<td>DHCP User’s Guide to Computing (obsolete)</td>
<td><p>There are several manuals and guides that provide a foundation for use of <em>Kernel</em>, <em>FileMan</em>, and <em>MailMan</em> (<em>see</em> Glossary). These documents replace the old <em>DHCP User’s Guide to Computing</em>, which is obsolete. You will find these at:</p>
<p><em>Kernel:</em> <a href="http://www.va.gov/vdl/application.asp?appid=10">http://www.va.gov/vdl/application.asp?appid=10</a></p>
<p><em>FileMan:</em> <a href="http://www.va.gov/vdl/application.asp?appid=5">http://www.va.gov/vdl/application.asp?appid=5</a></p>
<p><em>MailMan:</em> <a href="http://www.va.gov/vdl/application.asp?appid=15">http://www.va.gov/vdl/application.asp?appid=15</a></p></td>
</tr>
</tbody>
</table>

# System Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP operates with three distinct levels of security:

- System Access
- Menu and Security Keys
- Electronic Signature Codes

This chapter of the guide discusses these three levels.

IFCAP has levels of security for all users. For instance, many of the areas require that a user gain access via a security key (assigned by an Application Coordinator, Site Manager, or IRM, depending on protocol). Your electronic signature code is one of the measures used to authenticate approval.

## System Access 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The same system of access currently in operation for all VistA applications at your medical center applies to IFCAP. The Site Manager or Application Coordinator must assign an access code to a user. Additionally, a verify code must be assigned or entered by the user. The access and verify code pair afford access to the VistA system. If the user fails to enter the proper set of codes in two or three attempts (the number of attempts is determined by the site), the terminal will lock and further efforts will not be allowed.

As a security measure, the system periodically requires verify codes be changed as defined by system site parameters. The verify code may also be changed at any time by the user, (i.e., when an access or verify code may have been compromised).

Since access and verify codes cannot be viewed on the screen and are encrypted, these codes are safeguarded against exposure and possible use by unauthorized personnel.

## Menu and Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After a user enters the proper access and verify codes, IFCAP will display a menu. The menu presents *only* those options that a user has been assigned (security keys are the method by which a user may access certain options).

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP uses standard menus to organize the various IFCAP options around the activities of specific job-related positions. For instance, only Control Point Officials will have the Approve Requests option on their standard job-related menu if they have been given the PRCSCPO security key.

The Site Manager has the authority to alter these standard menus, or this authority may be delegated to an Application Coordinator.

Specialized menus are created using the *Menu Manager*. Use of this menu is *not* discussed in this guide. If authority for assigning additional menu options has been delegated to you, your Site Manager will instruct you in how to create new menus.

A single user should *not* have all IFCAP menus. It is inappropriate, for example, that a Control Point Official should have the Funds Distribution option that enters Ceiling Transactions. Restricting access to menus applies to Application Coordinators as well as management. No user is capable of assigning themselves additional menu options. Only those menus options required to accomplish their duties are assigned.

|                                                                                                                                                        |                                                                                                                                                                             |                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-control-point-official-user-s-guide/014.png) | *<u>TIP:</u>* Use the IFCAP standardized menus for an initial period for users to become familiar with available options. Evaluate the need for customized menus later. | ![](ifcap-version-5-1-control-point-official-user-s-guide/015.png) |

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some IFCAP menus and options are restricted through the implementation of a “lock.” Only those users who hold the appropriate security key for the locked option (such as supervisors and their designated staff) are granted access to that option. Users that do *not* hold the appropriate key will not see the option on their menus. In addition, the system verifies that the user holds the proper security key before permitting the user access to a restricted option.

### Security Keys/Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security keys can be associated with mail groups, menu options and users.

IFCAP transmits data to the Austin Automation Center (AAC). Transmitting data to AAC may require (for each type of document), several domains, security keys, and mail groups.

The mail group members will be the recipients of MSC Confirmation Messages coming from the AAC verifying the receipt of transmissions from your facility.

<table style="width:100%;">
<colgroup>
<col style="width: 31%" />
<col style="width: 21%" />
<col style="width: 30%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Domain Name</th>
<th>Purpose</th>
<th>Security Key</th>
<th>Mail group</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Redacted <strong>(<em>not in use)</em></strong></td>
<td>CALM</td>
<td>N/A</td>
<td>CLM</td>
</tr>
<tr class="even">
<td>Redacted</td>
<td>Code Sheets</td>
<td>N/A</td>
<td>CLI</td>
</tr>
<tr class="odd">
<td>Redacted</td>
<td><p>Receiving</p>
<p>Reports</p></td>
<td>PRCFA TRANSMIT</td>
<td>CLM</td>
</tr>
<tr class="even">
<td>Redacted</td>
<td>DLA</td>
<td>PRCHPM CS TRANSMIT</td>
<td>DLA</td>
</tr>
<tr class="odd">
<td>Redacted</td>
<td>Sends EDI orders to AAC</td>
<td>XMQ-EDP</td>
<td>EDP</td>
</tr>
<tr class="even">
<td>Redacted</td>
<td>ISMS</td>
<td>N/A</td>
<td>ISM</td>
</tr>
<tr class="odd">
<td>Redacted</td>
<td>Log</td>
<td>PRCHPM CS TRANSMIT</td>
<td>LOG</td>
</tr>
<tr class="even">
<td>Redacted</td>
<td>Vendor</td>
<td>PRCFA TRANSMIT</td>
<td>MDY</td>
</tr>
<tr class="odd">
<td>Redacted</td>
<td>ISMS</td>
<td>N/A</td>
<td>OGR</td>
</tr>
<tr class="even">
<td>Redacted</td>
<td></td>
<td>N/A</td>
<td>PRC</td>
</tr>
</tbody>
</table>

A list of the standardized menu options and their associated security keys is in Table 3.2.

Names of individuals working with IFCAP must appear in the New Person (#200) file. The Site Manager usually performs this task, or it may be assigned to the Application Coordinator.

In either case, a list of IFCAP users should be compiled to include the menu(s) assigned (*e.g.*, PRCSCP OFFICIAL for Control Point Officials).

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>Assigned Position or IFCAP Role</th>
<th>External Name</th>
<th>Internal Name</th>
<th>Associated Security Key(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Service Chief or designated Control Point Official</td>
<td>Control Point Official’s Menu</td>
<td>PRCSCP OFFICIAL</td>
<td>PRCSCPO</td>
</tr>
<tr class="even">
<td>Control Point Clerk</td>
<td>Control Point Clerk’s Menu</td>
<td>PRCSCP CLERK</td>
<td></td>
</tr>
<tr class="odd">
<td>Person who requests goods but doesn’t have access to Control Point Records</td>
<td>Requestor‘s Menu</td>
<td>PRCSREQUESTOR</td>
<td></td>
</tr>
<tr class="even">
<td>Chief, Personal Property Management or designee/Accountable Officer</td>
<td>Accountable Officer Menu</td>
<td>PRCHUSER PPM</td>
<td><p>PRCHADVOUCHER</p>
<p>PRCH TRANSACTION COMPLETE</p>
<p>PRCHPM CS PURGE CODE SHEETS</p>
<p>PRCHPM CS PURGE ALL</p>
<p>PRCHPM CS TRANSMIT</p>
<p>PRCPW MGRKEY</p>
<p>PRCPW ADJAPPR</p>
<p>PRCNPPM</p></td>
</tr>
<tr class="odd">
<td>PPM Clerk or person responsible for creating requisitions and LOG I code sheets</td>
<td>Requisition Clerk Menu</td>
<td>PRCHPM REQUISITION CLK MENU</td>
<td><p>PRCHADVOUCHER</p>
<p>PRCHPM CS PURGE CODE SHEETS</p>
<p>PRCHPM CS PURGE ALL</p>
<p>PRCHPM CS TRANSMIT</p>
<p>PRCH TRANSACTION COMPLETE</p></td>
</tr>
<tr class="even">
<td>Chief, Purchasing and Contracting or designee</td>
<td>Purchasing Agent Menu</td>
<td>PRCHUSER PA</td>
<td><p>PRCHADVOUCHER</p>
<p>PRCHASSIGN</p>
<p>PRCHIMP</p>
<p>PRCHRPT</p>
<p>PRCH TRANSACTION COMPLETE</p></td>
</tr>
<tr class="odd">
<td>Purchasing Agent</td>
<td>Purchasing Agent Menu</td>
<td>PRCHUSER PA</td>
<td><p>PRCHADVOUCHER</p>
<p>PRCHIMP</p>
<p>PRCHRPT</p>
<p>PRCH TRANSACTION COMPLETE</p></td>
</tr>
<tr class="even">
<td>Chief, Warehouse or designee</td>
<td>Warehouse Menu</td>
<td>PRCHUSER WHSE</td>
<td>PRCHRECDEL</td>
</tr>
<tr class="odd">
<td>Warehouse Worker</td>
<td>Warehouse Menu</td>
<td>PRCHUSER WHSE</td>
<td></td>
</tr>
<tr class="even">
<td>Fiscal Application Coordinator</td>
<td>Fund Distribution &amp; Accounting Menu</td>
<td>PRCF MASTER</td>
<td><p>PRCFA SUPERVISOR</p>
<p>PRCFA PURGE CODE SHEETS</p>
<p>PRCFA TRANSMIT</p>
<p>PRCF CC/SA MISMATCH OVERRIDE</p>
<p>PRCFA VENDOR EDIT</p></td>
</tr>
<tr class="odd">
<td>Budget Analyst</td>
<td>Fund Distribution Program Menu</td>
<td>PRCB MASTER</td>
<td><p>PRCF CC/SA MISMATCH OVERRIDE</p>
<p>PRCFA SUPERVISOR</p></td>
</tr>
<tr class="even">
<td>Chief, Accounting or designee</td>
<td>Accounting Technician Menu</td>
<td>PRCFA ACCTG TECH</td>
<td><p>PRCFA SUPERVISOR</p>
<p>PRCFA PURGE CODE SHEETS</p>
<p>PRCFA TRANSMIT</p>
<p>PRCFA VENDOR EDIT</p>
<p>PRCHPM CS PURGE CODE SHEETS</p>
<p>PRCHPM CS PURGE ALL</p>
<p>PRCHPM CS TRANSMIT</p>
<p>PRCF CC/SA MISMATCH OVERRIDE</p>
<p>PRCASVC</p></td>
</tr>
<tr class="odd">
<td>Accounting Technician</td>
<td>Accounting Technician Menu</td>
<td>PRCFA ACTTG TECH</td>
<td><p>PRCFA VENDOR EDIT</p>
<p>PRCHPM CS PURGE CODE SHEETS</p>
<p>PRCHPM CS PURGE ALL</p>
<p>PRCHPM CS TRANSMIT</p>
<p>PRCF CC/SA MISMATCH OVERRIDE</p>
<p>PRCASVC</p></td>
</tr>
<tr class="even">
<td>Item File Managers</td>
<td>Item File Edit</td>
<td>PRCHPC ITEM EDIT</td>
<td>PRCHITEM MASTER</td>
</tr>
<tr class="odd">
<td>Fiscal Staff</td>
<td>Transaction Report – eCMS/IFCAP</td>
<td>PRCHJ TRANS REPORT3</td>
<td>PRCHJFIS</td>
</tr>
<tr class="even">
<td>Voucher Auditor</td>
<td>Payment /Invoice Tracking Menu</td>
<td>PRCFD PAYMENTS MENU</td>
<td>PRCFA VENDOR EDIT</td>
</tr>
<tr class="odd">
<td>Person in A&amp;MM responsible for Warehouse Inventory</td>
<td>Warehouse Inventory</td>
<td>PRCPW MAIN MENU</td>
<td><p>PRCPW MGRKEY</p>
<p>PRCPW ADJAPPR</p>
<p>PRCNWHSE*</p></td>
</tr>
<tr class="even">
<td>Person in Primary Inventory Point responsible for maintaining Inventory</td>
<td>Primary – General Inventory/Distribution Menu</td>
<td>PRCP MAIN MENU</td>
<td>PRCP MGRKEY*</td>
</tr>
<tr class="odd">
<td>Person on the ward/clinic responsible for maintaining Inventory</td>
<td>Secondary – General Inventory/ Distribution Menu</td>
<td>PRCP2 MAIN MENU</td>
<td><p>PRCP2 MGRKEY</p>
<p>PRCPSSQOH*</p></td>
</tr>
<tr class="even">
<td>A&amp;MM and Fiscal Application Coordinators</td>
<td>IFCAP Application Coordinator Menu</td>
<td>PRCHUSER COORDINATOR</td>
<td>PRCFA SUPERVISOR</td>
</tr>
<tr class="odd">
<td>A&amp;MM/Logistics Application Coordinators</td>
<td>IFCAP Application Coordinator Menu</td>
<td>PRCHUSER COORDINATOR</td>
<td><p>PRCPAQOH*</p>
<p>PRCPODI</p>
<p>PRCHPM CS PURGE CODE SHEETS</p>
<p>PRCHPM CS PURGE ALL</p>
<p>PRCHPM CS TRANSMIT</p></td>
</tr>
<tr class="even">
<td>Application Coordinator and Inventory Point Managers</td>
<td>Barcode Manager Menu</td>
<td>PRCT MGR</td>
<td></td>
</tr>
<tr class="odd">
<td>Service Personnel responsible for performing Inventory</td>
<td>Barcode User</td>
<td>PRCT BARCODE USER</td>
<td></td>
</tr>
<tr class="even">
<td>Service Personnel responsible for performing Inventory</td>
<td>Labels</td>
<td>PRCT LABELS</td>
<td></td>
</tr>
<tr class="odd">
<td>IRM Service Personnel</td>
<td>Barcode Programmer</td>
<td>PRCT PROGRAMMER</td>
<td>PRCT MGR</td>
</tr>
<tr class="even">
<td>Station Purchase Card Coordinator</td>
<td>Purchase Card Coordinator</td>
<td>PRCH CARD COORDINATOR MENU</td>
<td></td>
</tr>
<tr class="odd">
<td>Service personnel ordering using a Credit Card</td>
<td>Purchase Card Menu</td>
<td>PRCH PURCHASE CARD MENU</td>
<td></td>
</tr>
<tr class="even">
<td>Service personnel designated as Credit Card approving officials</td>
<td>Approving Official Menu</td>
<td>PRCH APPROVE</td>
<td>PRCH AR</td>
</tr>
<tr class="odd">
<td>Service Control Point personnel ordering contract items</td>
<td>Delivery Orders Menu</td>
<td>PRCH DELIVERY ORDER MENU</td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><p>* Manager Only</p>
<p> If on-site automated supply stations are interfaced to GIP.</p></td>
</tr>
</tbody>
</table>

|                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-control-point-official-user-s-guide/016.png) | *<u>TIP:</u>* If your site is using the file access provisions of Kernel, ensure users have access to needed files. Contact your Site Manager or IRM for assistance. | ![](ifcap-version-5-1-control-point-official-user-s-guide/017.png) |

As mentioned previously, certain menus require the user to have a security key in order to access available options. IFCAP looks to see if the user is an A&MM employee and position held. All A&MM employees *must* be identified using the Add/Edit Supply Personnel option of the IFCAP Application Coordinator Menu.

## Electronic Signature Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The final level of security in IFCAP involves the use of electronic signatures. The electronic signature code is not visible to the screen and is encrypted rendering them unreadable even when viewed in the user file by those with the highest levels of access. This signature code enables the system to limit to authorized individuals only, the ability to review or electronically pass a document to the next level of processing.

Electronic signature codes are required by IFCAP at every level a signature would be required on paper. Therefore, electronic signature codes are assigned to:

- Budget Analysts for distributing funds to control points
- Control Point Officials for approving requests
- Purchasing Agents for processing purchase orders
- Accounting Technicians for obligation of documents and authorizing payments
- Warehouse workers for receiving purchases
- Purchase Card holders for processing credit card orders
- Delivery Order users to process delivery orders against existing contracts

### Changing Your Electronic Signature Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When necessary, you may edit your electronic signature code via the menu option Electronic Signature Code Edit.

| STEP 1. | From any IFCAP Menu (Error! Not a valid bookmark self-reference.), select User’s Toolbox |
|---------|----------------------------------------------------------------------------------------------|
| STEP 2. | From the User’s Toolbox menu, select Edit Electronic Signature Code.                         |

<span id="_Toc166316032" class="anchor"></span>Figure 1: Sample IFCAP Menu Option User’s Toolbox Screen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select IFCAP MENU Option: User’s Toolbox</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Display User Characteristics</p>
<p>Edit Electronic Signature code</p>
<p>Edit User Characteristics</p>
<p>Menu Templates …</p>
<p>Spooler Menu …</p>
<p>TaskMan User</p>
<p>User Help</p>
<p>Select User’s Toolbox Option: electronic Signature code Edit</p>
<p>This option is designed to permit you to enter or change your Initials,</p>
<p>Signature Block Information, Office Phone number, and Voice and</p>
<p>Digital Pagers numbers.</p>
<p>In addition, you are permitted to enter a new Electronic Signature Code</p>
<p>or to change an existing code.</p>
<p>INITIAL: IO//</p>
<p>SIGNATURE BLOCK PRINTED NAME: IFUSER,ONE//</p>
<p>SIGNATURE BLOCK TITLE:</p>
<p>OFFICE PHONE:</p>
<p>VOICE PAGER:</p>
<p>DIGITAL PAGER:</p>
<p>Enter your Current Signature Code: SIGNATURE VERIFIED</p>
<p>Your typing will not show.</p>
<p>ENTER NEW SIGNATURE CODE:</p>
<p>RE-ENTER SIGNATURE CODE FOR VERIFICATION:</p>
<p>DONE</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 86%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-control-point-official-user-s-guide/018.png)</td>
<td><p><em><strong><u>NOTES</u></strong>:</em></p>
<ul>
<li><p>Your electronic signature is legal authorization to release government funds.</p></li>
<li><p><span id="XU_80_679" class="anchor"></span>If the SIGNATURE BLOCK PRINTED NAME and SIGNATURE BLOCK TITLE fields are disabled at your site, contact your supervisor to request entry of your name and title.</p></li>
</ul></td>
<td>![](ifcap-version-5-1-control-point-official-user-s-guide/019.png)</td>
</tr>
</tbody>
</table>

| STEP 3. | At the INITIAL: prompt, enter your initials.                                                                               |
|---------|----------------------------------------------------------------------------------------------------------------------------|
| STEP 4. | At the SIGNATURE BLOCK PRINTED NAME: prompt, enter your name, as you want it printed on forms that require your signature. |
| STEP 5. | At the SIGNATURE BLOCK TITLE: prompt, enter your job title, as you want it printed on forms that require your signature.   |
| STEP 6. | At the appropriate prompts, enter your OFFICE PHONE number, your VOICE PAGER number, and your DIGITAL PAGER number.        |
| STEP 7. | Finally, at the ENTER NEW SIGNATURE CODE: prompt, enter your signature code; re-enter the same code when prompted.         |

# Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## IFCAP Control Point Official Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section presents the Control Point Official options in the IFCAP Control Point Official Menu (Error! Not a valid bookmark self-reference.).

Different kinds of IFCAP users have different menus. If the menus in this guide include options that you don’t see on your screen, don’t panic! The instructions in this guide only use the options that you have as a Control Point Official. If you have additional responsibilities, please consult the appropriate role-based user guide.

The options you use in IFCAP are divided into groups based upon the type of work you do. When you select these options, IFCAP will ask you a series of questions.

<span id="_Toc222496802" class="anchor"></span>Figure 2: Sample Control Point Official Main Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Requests Ready for Approval List</p>
<p>Process a Request Menu</p>
<p>Display Control Point Activity Menu</p>
<p>Funds Control Menu</p>
<p>Status of Requests Reports Menu</p>
<p>Record Date Received by Service Menu</p>
<p>Approved Requests</p>
<p>Record Receipt of Multiple Delivery Schedule Items</p>
<p>Multiple Delivery Schedule List</p></td>
</tr>
</tbody>
</table>

- OPTION: Requests Ready for Approval List– lists requests pending your approval
- OPTION: Process a Request Menu– allows you to process transaction requests
- OPTION: Display Control Point Activity Menu– displays request/transaction information
- OPTION: Funds Control Menu– balance the Control Point
- OPTION: Status of Requests Reports Menu– lets you generate reports on the requests for the Control Point
- OPTION: Record Date Received by Service Menu– lets you report receipt of items ordered on IFCAP transactions
- OPTION: Approve Requests– allows you to review the order, edit the order, and forward the order to Supply
- OPTION: Record Receipt of Multiple Delivery Schedule Items – lets you record the receipt of items that are received in multiple deliveries
- OPTION: Multiple Delivery Schedule List– lets you generate a list of transactions having items with multiple delivery dates or receiving locations

## Using IFCAP Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information entered into IFCAP is stored in files. These files allow users to access and share information quickly and easily. A good example of shared data is the information in the Vendor (#440) file. A&MM is responsible for entering and maintaining vendor data. The Control Points access this information when a user enters a request or when Purchasing and Contracting users create a quotation for bid or a purchase order. Fiscal Service uses the Vendor (#440) file to enter and store billing information.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 86%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-control-point-official-user-s-guide/020.png)</td>
<td><p><strong><em><u>TIP:</u></em></strong> When at a menu prompt enter:</p>
<ul>
<li><p>All or part of the option name, then &lt;Enter&gt;</p></li>
</ul>
<ul>
<li><p>?? (to see more options at the menu prompt)</p></li>
<li><p>??? (to see brief descriptions)</p></li>
<li><p>? OPTION (to see Help text)</p></li>
</ul>
<p>When the system responds with a question of offers a prompt, and you do not understand the question or are unsure of how to respond, enter one (?) or two (??) question marks. The system will give you an explanation of the information needed or allow you to choose from a list of responses.</p></td>
<td>![](ifcap-version-5-1-control-point-official-user-s-guide/021.png)</td>
</tr>
</tbody>
</table>

The remainder of this guide discusses tasks you may perform as a Control Point Official.

## The Financial Management System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP exchanges data with the Financial Management System (FMS). FMS uses the “sub-cost center” to track costs. While IFCAP itself does not use the sub-cost center, IFCAP does send to FMS the last two digits of the cost center, if anything other than “00,” as the sub-cost center.

### Sub-Allowance Reconciliation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IFCAP FMS Transaction Data report shows all transactions affecting the Fund Control Point balance, but it is for review only. The FMS system passes Fund Control Point adjustments to IFCAP on a daily basis. These adjustments arise from FMS accounting activity that originates outside of IFCAP. For example, a late receipt of goods could result in an interest expense. The IFCAP system would have no record of this type of charge to the Fund Control Point and thus relies on FMS to provide adjustment data. The adjustments are returned to an FMS document, Sub allowance Reconciliation, which automatically updates balances in the Fund Control Point.

### Rollover of Funds from Previous Quarters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Budget Analyst for your Control Points might designate your Control Point to receive rollover funds from previous quarters. IFCAP allows Budget Analysts to designate Control Points to transmit and receive remaining funds at the end of each quarter. This means that even if you are not allowed to overcommit funds for your Control Point, you still might have enough funds from the quarterly rollover to cover your expenses.

### Amendment Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Amendments will automatically adjust FCP balances.

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Approving and rejecting requests and monitoring the balance of the Control Point are the most common activities of the Control Point Official. This chapter explains the procedure for approving or rejecting standard requests and purchase card requests.

## Convert a Temporary 2237 Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Control Point official may want to convert a temporary 2237 transaction into a permanent transaction. The first step is to Change the Temporary request number to a Permanent transaction number.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222496803" class="anchor"></span>Figure 3: Approve a Temporary 2237 Request Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select Control Point Official's Menu Option: Process a Request Menu</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p><strong>Select Process a Request Menu Option: Change Existing Transaction Number</strong></p>
<p>Select CONTROL POINT: 101 ISC2// A2222 10 0100 01AA20100</p></td>
</tr>
</tbody>
</table>

### Select Temporary 2237 Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: prompt, enter the temporary 2237 transaction number that the requestor assigned to the request. You may review the request to make sure that you’ve chosen the correct one.

| ![](ifcap-version-5-1-control-point-official-user-s-guide/022.png) | *<u>NOTE:</u>* The fields Requesting Service and Line-Item DESCRIPTION are not required fields in a Temporary Request. This will mean the Control Point Clerk may encounter missing required fields when converting a temporary request to a 2237 transaction. The Clerk will be advised of the missing field(s) and be allowed to edit the new 2237 and populate the required fields. If they choose not to edit the fields at that time, the 2237 will not be complete and the Clerk will not be able to set the Approval flag to YES. The Clerk will have to Edit the 2237 and populate the missing fields. | ![](ifcap-version-5-1-control-point-official-user-s-guide/023.png) |
|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc222496804" class="anchor"></span>Figure 4: Select Transaction to be Approved

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select the existing transaction number to be replaced</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: THX-1138 THX-1138 OBL IFVENDOR1,TWO Furry things with green hair</p>
<p>Would you like to review this request? No// Y (Yes)</p>
<p>Print administrative certification page of 2237? Yes// (Yes)</p>
<p>DEVICE: HOME// LAT RIGHT MARGIN: 80//</p>
<p>PRIORITY: STANDARD</p>
<p>MAR 28,1994@15:39:42 THX-1138</p>
<p>----------------------------------------------------------</p>
<p>REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES</p>
<p>-------------------------------------------</p>
<p>TO: A&amp;MM Officer Requesting Office</p>
<p>INFORMATION SYSTEMS CENTER (162-2)----------------------- ---------------------------------------</p>
<p>Action Requested</p>
<p>Date Prepared Date Required Delivery</p>
<p>MAR 28,1994 APR 1,1994----------------------- --------------------- -----------</p>
<p>ITEM NO. DESCRIPTION QUANTITY UNIT ESTIMATED</p>
<p>OR STOCK NO. UNIT COST----------------------</p>
<p>011 1 Furry things with green hair 10 CB 9.4000</p>
<p>TOTAL COST: $94.00</p>
<p>------------------------------------------------------------------</p>
<p>VENDOR INFORMATION:VENDOR: IFVENDOR1,TWO</p>
<p>CONTACT: IFUSER2,NINE 4 HIGH ST</p>
<p>PHONE: 111 555-5555 AUSTIN,MN 99999</p>
<p>LOG Voucher Number: THX-1138</p>
<p>----------------------------------------------------------------------------------------------------------</p>
<p>SPECIAL REMARKS: This is a standard remark.</p>
<p>------------------------------------------------------------------------------------------</p>
<p>JUSTIFICATION OF NEED OR TURN-IN</p>
<p>Items needed for computer section for daily use.</p>
<p>-----------------------------------------------------------------</p>
<p>Signature of Initiator Signature of Approving Official Date</p>
<p>IFUSER3,SIX</p>
<p>Publications Analyst</p>
<p>-----------------------------------------------------------------</p>
<p>Appropriation and Accounting Symbols</p>
<p>999-3640151-101-805600-1091</p>
<p>-----------------------------------------------------------------</p>
<p>MULTIPLE DELIVERY DISTRIBUTION LIST PAGE: 1 ITEM PR# DESCRIPTION QTY DATE QTY SCP LOCATION 1 Furry thin 10 04-01-94 NONENONE</p></td>
</tr>
</tbody>
</table>

### Edit Data on the 2237 Transaction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will allow you to change the Fiscal Year, Fiscal Quarter, and Control Point for the transaction. IFCAP will then replace the temporary transaction number (earlier assigned to the request by the requestor) with a new, permanent transaction number. This new number will refer to the transaction for the rest of its history. IFCAP will give you *one more chance* to edit the request before asking if you want to transmit the 2237 request to A&MM/Fiscal Service. If you choose to submit the request, IFCAP will ask for your signature code.

Answer “Y” at the “Would you like to replace another transaction number?” prompt if you want to approve another temporary request. If not, press \<Enter\> to return to the Control Point Official’s Menu.

<span id="_Toc222496805" class="anchor"></span>Figure 5: Enter New Transaction Data

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Enter the information for the new 2237 transaction number</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select FISCAL YEAR: 94//</p>
<p>Select QUARTER: 2//</p>
<p>Select CONTROL POINT: 101 ISC2// A2222 10 0100 01AA20100 A2222 10 0100 01AA20100</p>
<p>Old transaction THX-1138 is now cancelled.</p>
<p>Transaction 'THX-1138' has been replaced by transaction 999-94-2-101-0134</p>
<p>Would you like to review this request? No// (No)</p>
<p>Current Control Point balance: $-13456.86</p>
<p>Estimated cost of this request: $500.00</p>
<p>Total uncommitted balance from current and prior quarters: -$13456.86</p>
<p>If the 2237 has any required fields that are not populated – the User will not be prompted to set the Ready for approval flag to YES. All required fields must be populated before the 2237 can be moved to the Official for Approval.</p>
<p>Is this request ready for approval? Yes// (Yes)</p>
<p><strong>Is this request ready for transmission to A&amp;MM/Fiscal? No// Y (Yes)</strong></p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p>
<p>Would you like to replace another transaction number? No// (No)</p></td>
</tr>
</tbody>
</table>

## Change a Temporary 1358 Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Select Temporary 1358 Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: prompt, enter the temporary transaction number for the 1358 form that the requestor assigned to the request. You may review the request to make sure that you’ve chosen the correct one.

<span id="_Toc222496806" class="anchor"></span>Figure 6: Select Transaction to be Changed

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select the existing transaction number to be replaced</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Process a Request Menu Option: Change Existing Transaction Number [PRCSANTN]</p>
<p>MCG-0727 JUL 27, 2011@16:22:15 PAGE 1</p>
<p>________________________________________________________________________________</p>
<p>1358 OBLIGATION OR CHANGE</p>
<p>________________________________________________________________________________</p>
<p>Originator of Request: TESTER, CP OFFICIAL</p>
<p>Requestor: |Date Requested: |Obligation No.:</p>
<p>TESTER, CP OFFICIAL |JUL 27, 2011, |</p>
<p>________________________________________________________________________________</p>
<p>Vendor: |Contract Number:</p>
<p>________________________________________________________________________________</p>
<p>Name and Title Approving Off.: |Signature: |Date Signed:</p>
<p>________________________________________________________________________________</p>
<p>FUND CERTIFICATION: The supplies and services listed on this request are</p>
<p>properly chargeable to the following allotments, the available balances of</p>
<p>which are sufficient to cover the cost thereof, and funds have been obligated.</p>
<p>________________________________________________________________________________</p>
<p>Press ‘return’ to continue, "^" to exit:</p>
<p>MCG-0727 PAGE 2</p>
<p>________________________________________________________________________________</p>
<p>1358 OBLIGATION OR CHANGE</p>
<p>________________________________________________________________________________</p>
<p>Appropriation &amp; Acct. Symbols: |Obligated By: |Date Obligated:</p>
<p>442-3610160-041-820300-2584 010044100 | |</p>
<p>________________________________________________________________________________</p>
<p>AUTHORITY:</p>
<p>SERVICE START DATE: SERVICE END DATE:</p>
<p>________________________________________________________________________________</p>
<p>Purpose:</p>
<p>MONTHLY COSTS</p>
<p>________________________________________________________________________________</p>
<p>Daily Record entries have not yet been entered for this request.</p>
<p>The total committed cost of this request is $1000.00</p>
<p>________________________________________________________________________________</p>
<p>VA FORM 4-1358a-ADP (NOV 1987)</p>
<p>Press ‘return’ to continue, "^" to exit:</p>
<p>Do you want to enter another new request? NO//</p></td>
</tr>
</tbody>
</table>

### Edit Data on the 1358 Transaction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will allow you to change the Fiscal Year, Fiscal Quarter, and Control Point for the transaction. IFCAP will then replace the temporary transaction number (earlier assigned to the request by the requestor) with a new, permanent transaction number. This new number will refer to the transaction for the rest of its history. IFCAP will assign you as the CP Clerk (Requestor) for the new 1358 transaction per the Segregation of Duties functionality. You will be given *one more chance* to edit the request before you are asked if the transaction is *Ready for Approval.* Another CP Official will have to Approve the 1358 and transmit the request to Fiscal for obligation.

Answer Y at the Would you like to replace another transaction number? if you want to approve another temporary request. If not, press \<Enter\> to return to the Control Point Official’s Menu.

<span id="_Toc222496807" class="anchor"></span>Figure 7: Enter New 1358 Transaction Data

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Enter the information for the new 2237 transaction number</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select STATION NUMBER: 999//</p>
<p>Select FISCAL YEAR: 10//</p>
<p>Select QUARTER: 4//</p>
<p>Select CONTROL POINT: 110 Stuff .01// 0160A1 10 0100 010042116</p>
<p><strong>WARNING: The system will assign you as the CP Clerk (Requestor) of this 1358.</strong></p>
<p><strong>You will be unable to approve a 1358 on which you are the REQUESTOR due to</strong></p>
<p><strong>segregation of duties.</strong></p>
<p>Do you want to proceed (Y/N)? NO// YES</p>
<p>0160A1 10 0100 010042116</p>
<p>Transaction 'IFUSER1' has been replaced by 999-10-4-110-0056</p>
<p><strong>Use the 1358 edit option if you wish to edit this request.</strong></p></td>
</tr>
</tbody>
</table>

## Reject a Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222496808" class="anchor"></span>Figure 8: Cancel Transaction Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Approve Requests</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Requests Ready for Approval List</p>
<p>Process a Request Menu ...</p>
<p>Display Control Point Activity Menu ...</p>
<p>Funds Control Menu ...</p>
<p>Status of Requests Reports Menu ...</p>
<p>Record Date Received by Service Menu ...</p>
<p>Enter/Edit Control Point Users</p>
<p>Record Receipt of Multiple Delivery Schedule Items</p>
<p>Multiple Delivery Schedule List</p>
<p>Select Control Point Official's Menu Option: Process a Request Menu</p>
<p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: Cancel Transaction with Permanent Number</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>

### Select Transaction Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a Control Point. Enter the permanent transaction number the Control Point Clerk assigned to the request. If you don’t know the number, type three question marks (???) at the Select TRANSACTION: prompt to have IFCAP display the available requests. IFCAP will ask you to verify that you want to cancel the request and ask you to explain why you’re canceling the request. At the Would you like to cancel another transaction? prompt, answer Y if you want to cancel another request. If not, press \<Enter\> to return to the Process a Request menu.

| ![](ifcap-version-5-1-control-point-official-user-s-guide/024.png) | *<u>NOTE:</u>* Per the existing Business Rules: Do not use this option to cancel any 2237 that contains eCMS Identifiers. Notify the Contracting Officer in eCMS that you want the 2237 cancelled. The cancellation process will be initiated from within eCMS to ensure that the two systems remain synchronized. | ![](ifcap-version-5-1-control-point-official-user-s-guide/025.png) |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc222496809" class="anchor"></span>Figure 9: Select Transaction Number Screen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select CONTROL POINT: 101 LAB TESTING 101</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select TRANSACTION : ???</p>
<p>Attempting lookup in transaction file.</p>
<p>Attempting lookup using 101 LAB TESTING 101 (CONTROL POINT)</p>
<p>1 101 LAB TESTING 101 999-94-3-101-0166 OBL GENERIC GENERAL STOR</p>
<p>2 101 LAB TESTING 101 999-94-3-101-0164 CANC</p>
<p>TEST FOR IFUSER2,FIVE</p>
<p>3 101 LAB TESTING 101 999-94-3-101-0163 CANC</p>
<p>TEST FOR IFUSER2,FIVE</p>
<p>4 101 LAB TESTING 101 999-94-3-101-0162</p>
<p>5 101 LAB TESTING 101 999-94-3-101-0161</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: 4 999-94-3-101-0162</p>
<p>Cancel this transaction? No// Y (Yes)</p>
<p>Enter comments for this cancellation</p>
<p>COMMENTS:</p>
<p>1&gt;Project cancelled</p>
<p>2&gt;</p>
<p>EDIT Option:</p>
<p>Would you like to cancel another transaction? No// (No)</p></td>
</tr>
</tbody>
</table>

### Notify the Requestor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notify the Requestor that you’ve cancelled the request and why. Don’t let the Requestor anticipate the arrival of items that are never coming because you’ve cancelled the request.

## Approve a 2237 Request 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Control Point Clerk will create transactions and then pass them to the Official for signature.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222496810" class="anchor"></span>Figure 10: Approving a Request Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select Control Point Official's Menu Option:</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Approve Requests</p>
<p>Requests Ready for Approval List</p>
<p>Process a Request Menu ...</p>
<p>Display Control Point Activity Menu ...</p>
<p>Funds Control Menu ...</p>
<p>Status of Requests Reports Menu ...</p>
<p>Record Date Received by Service Menu ...</p>
<p>Enter/Edit Control Point Users</p>
<p>Record Receipt of Multiple Delivery Schedule Items</p>
<p>Multiple Delivery Schedule List</p>
<p>Select Control Point Official's Menu Option: Approve Requests</p></td>
</tr>
</tbody>
</table>

### Select a Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222496811" class="anchor"></span>Figure 11: Approving a Request

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select Control Point Official's Menu Option: Approve Requests</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Please wait while I check your control points...</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p>
<p>Loop thru all control points? Yes// (Yes)</p>
<p>Loop thru all transactions for CP 60? Yes// (Yes)</p>
<p>CP TRANSACTION NUMBER: 100-01-1-060-0021</p>
<p>TEMPORARY TRANSACTION:</p>
<p>TRANSACTION TYPE: OBLIGATION</p>
<p>FORM TYPE: REPETITIVE AND NON-REP ORDER</p>
<p>REQUESTOR: IFUSER3,FIVE</p>
<p>DATE OF REQUEST: NOV 14,2000</p>
<p>DATE REQUIRED: NOV 18,2000</p>
<p>COMMITTED (ESTIMATED) COST: 25.20</p>
<p>VENDOR: IFCAPVENDFOR1,FIVE</p>
<p>ITEM #1 DESCRIPTION: WIDGETS</p>
<p>Current Control Point balance: $299660.97</p>
<p>Estimated cost of this request: $25.20</p>
<p>Requests need to be reviewed prior to approval.</p>
<p>Have you reviewed this request? Y (Yes)</p>
<p>Is this request ready for approval? Yes// (Yes)</p>
<p>Is this request ready for transmission to A&amp;MM/Fiscal? No// Y (Yes)</p>
<p>incrementing due-ins in inventory point: SPD</p>
<p>*END OF PROCESSING*</p></td>
</tr>
</tbody>
</table>

## Approve a 1358 Request 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Control Point Clerk will create transactions and then pass them to the Official for signature.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222496812" class="anchor"></span>Figure 12: Approve a 1358 Request Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select Control Point Official's Menu Option:</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Approve Requests</p>
<p>Requests Ready for Approval List</p>
<p>Process a Request Menu ...</p>
<p>Display Control Point Activity Menu ...</p>
<p>Funds Control Menu ...</p>
<p>Status of Requests Reports Menu ...</p>
<p>Record Date Received by Service Menu ...</p>
<p>Enter/Edit Control Point Users</p>
<p>Record Receipt of Multiple Delivery Schedule Items</p>
<p>Multiple Delivery Schedule List</p>
<p>Select Control Point Official's Menu Option: Approve Requests</p></td>
</tr>
</tbody>
</table>

### Select a 1358 Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222496813" class="anchor"></span>Figure 13: Approving Requests

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select Control Point Official's Menu Option: Approve Requests</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Please wait while I check your control points...</p>
<p>Select STATION NUMBER: 999</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p>
<p>Loop through all control points? Yes// N (No)</p>
<p>_____________________________________________________</p>
<p>Select CONTROL POINT: 110</p>
<p>___________________________________________________</p>
<p>Loop through all transactions for CP 110? Yes// (Yes)</p>
<p>CP TRANSACTION NUMBER: 999-11-1-110-0009</p>
<p>TEMPORARY TRANSACTION:</p>
<p>TRANSACTION TYPE: OBLIGATION</p>
<p>FORM TYPE: 1358 ORDER</p>
<p>REQUESTOR: IFUSER 77</p>
<p>DATE OF REQUEST: OCT 4,2010</p>
<p>DATE REQUIRED:</p>
<p>COMMITTED (ESTIMATED) COST: 19999.00</p>
<p>VENDOR:</p>
<p>ITEM #1 DESCRIPTION: Item Description not available</p>
<p>Current Control Point balance: $999556.00</p>
<p>Estimated cost of this request: $19999.00</p>
<p>Requests need to be reviewed prior to approval.</p>
<p>Have you reviewed this request? N (YES)</p>
<p>Is this request ready for approval? Yes// (Yes)</p>
<p>Is this request ready for transmission to A&amp;MM/Fiscal? No// y (Yes</p></td>
</tr>
</tbody>
</table>

| ![](ifcap-version-5-1-control-point-official-user-s-guide/026.png) | *<u>NOTE:</u>* If the CP Official attempts to Appove a 1358 on which they are listed as the CP Clerk (Requestor), they will be prevented from completing the Approval process and will see this Warning message: You are the CP Clerk (Requestor) on this 1358 transaction. Per Segregation of Duties, the CP Clerk (Requestor) is not permitted to Approve the 1358. | ![](ifcap-version-5-1-control-point-official-user-s-guide/027.png) |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

# Transaction Report - IFCAP/eCMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of October 2012, there is an interface between IFCAP and the electronic Contract Management System (eCMS) in Austin. 2237s are sent to eCMS via HL7 messages. This option enables users to generate reports based on data in the new IFCAP/ECMS TRANSACTION File \[414.06\]. As 2237s are sent to eCMS via HL7 messages, certain information about the transaction is stored in the file.

| ![](ifcap-version-5-1-control-point-official-user-s-guide/028.png) | *<u>Note:</u>* You will only be able to view data related to the Control Point(s) on which you are identified as a Control Point Clerk or Official. | ![](ifcap-version-5-1-control-point-official-user-s-guide/029.png) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

## Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu option on Control Point Clerk’s Menu.

Select Transaction Report – eCMS/IFCAP

Select Process a Request Menu Option: ?

New 2237 (Service) Request

Edit a 2237 (Service)

Copy a Transaction

1358 Request Menu ...

Print/Display Request Form

Change Existing Transaction Number

Repetitive Item List Menu ...

Cancel Transaction with Permanent Number

Requestor's Menu ...

Item Display

Vendor Display

Outstanding Approved Requests Report

Transaction Report - eCMS/IFCAP

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a single 2237 or all, or a single eCMS Contact, or all.

Select All dates or accept default NO and then Enter Start and End dates.

Select a single Station, Sub-station (if applicable), or All stations.

Select a single Control Point, or ALL then select the Event Type of Report to be generated.

The report is based on data in the new IFCAP/ECMS TRANSACTION file \[414.06\]. As 2237s are sent to eCMS via HL7 messages, certain information about the transaction is stored within this file. This report also lists transactions that have been returned by eCMS.

| ![](ifcap-version-5-1-control-point-official-user-s-guide/030.png) | *<u>NOTE:</u>* Users can view only those transactions related to the Control Point(s) on which they are identified as the Control Point Clerk or Official. | ![](ifcap-version-5-1-control-point-official-user-s-guide/031.png) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

### Date Range Help Text 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu \<TEST ACCOUNT\> Option: Transaction Report - eCMS/IFCAP

Select a single 2237 TRANSACTION NUMBER? NO//

Select a single eCMS Contact? NO//

Select ALL DATES: (JUN 06, 2012 - AUG 08, 2013)? NO//

Starting date: TODAY// T-39 (JUN 30, 2013)

Ending date: TODAY// (AUG 08, 2013)

Examples of Valid Dates:

JAN 20, 1957, or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses CURRENT YEAR. Two-digit year

assumes no more than 20 years in the future, or 80 years in the past.

### Station Number Help Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a single STATION NUMBER? NO// YES

Select Station: ??

Choose from:

001 ANYTOWN, SD

009 NATIONAL CEMETERY

Do you want to see the records for ALL the substations of 001? YES//NO

Select one of the following:

1 001 MEDICAL CENTER EAST

2 001A4 MEDICAL CENTER WEST

SUBSTATION: 2 001A4 MEDICAL CENTER WEST

### Fund Control Point Help Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a single FUND CONTROL POINT? NO/yes

Fund Control Point: ??

Choose from:

223

Fund Control Point: 223

TRANSACTION EVENTS:

1 Sent to eCMS (includes re-sent 2237s)

2 Returned to Accountable Officer

3 Returned to Control Point

4 Cancelled within eCMS

Select one or more of the above events: 1-4// ??

This response must be a list or range, e.g., 1,3 or 1-2,4.

TRANSACTION EVENTS:

1 Sent to eCMS (includes re-sent 2237s)

2 Returned to Accountable Officer

3 Returned to Control Point

4 Cancelled within eCMS

Select one or more of the above events: 1-4// 1,2,3

Display event ERROR TEXT. NO//

All eCMS 2237s matching your selections below will be displayed:

All eCMS Contacts

Dates: (JUN 30, 2013 - AUG 08, 2013)

Station: 001, records for substation 001HS

Fund Control Point: 223

Event Types selected are:

1 = Sent to eCMS (includes re-sent 2237s)

2 = Returned to Accountable Officer

3 = Returned to Control Point

A note will display any errors, but not the full text.

### Report Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AUG 08, 2013@10:21 eCMS/IFCAP TRANSACTION LOG REPORT p. 1

eCMS 2237: ALL eCMS Contact: ALL Station: 662

Report Date Range: JUN 24, 2013 - AUG 08, 2013, Control Point: ALL

Events: Sent to eCMS, returned to AO, Returned to CP, Cancelled within eCMS

IFCAP Reference Message Event Event Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

001-13-3-223-0016 2237 SENT JUN 24, 2013@15:46:43

SUBSTATION: 001A4 ACKNOWLEDGED: JUN 24, 2013@15:47:41

001-13-3-223-0017 2237 SENT JUN 24, 2013@15:43:52

SUBSTATION: 001A4 ACKNOWLEDGED: JUN 24, 2013@15:44:40

001-13-3-223-0018 2237 SENT JUN 26, 2013@16:02:19

SUBSTATION: 001A4 ACKNOWLEDGED: JUN 26, 2013@16:03:56

001-13-3-223-0021 RETURNED TO ACCOUNTABLE OFFICER JUN 26, 2013@16:19:41

SUBSTATION: 001A4 ACKNOWLEDGED: JUN 26, 2013@16:19:43

eCMS CONTACT: XXXXX@va.gov PHONE: 800-200-1000

RETURN/CANCEL DATE: JUN 26, 2013@15:19:18

REASON/COMMENT: Process within IFCAP as Imprest Fund Order {ECMS, CONTACT1}

001-13-4-223-0018 2237 SENT JUN 26, 2013@12:05:49

SUBSTATION: 001A4 ACKNOWLEDGED: JUN 26, 2013@12:07:12

001-13-4-223-0019 RETURNED TO CONTROL POINT JUN 26, 2013@12:54:08

SUBSTATION: 001A4 ACKNOWLEDGED: JUN 26, 2013@12:54:09

eCMS CONTACT: XXXXX@va.gov PHONE: 88-200-1000

RETURN/CANCEL DATE: JUN 26, 2013@11:53:45

REASON/COMMENT: Edit Item 1 Quantity {ECMS, CONTACT1}

001-13-4-223-0020 2237 SENT JUL 25, 2013@19:06:48

SUBSTATION: 001A4 ACKNOWLEDGED: JUL 26, 2013@17:41:16

001-14-1-223-0001 2237 SENT JUN 24, 2013@15:11:35

SUBSTATION: 001a4 ACKNOWLEDGED: (Pending)

This 2237 SENT has ERROR TEXT.

END OF REPORT

# # How to Monitor Your Control Point Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Approving and rejecting requests and monitoring the Control Point balance are the most common Control Point activities of the Control Point Official.

## Monitor the Balance of Your Control Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Control Point Official Menu, select Display Control Point Activity Menu. From that menu, select Running Balances. Enter a Fiscal Year, a Fiscal Quarter, and a Control Point.

<span id="_Toc222496814" class="anchor"></span>Figure 14: Control Point Balance Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Approve Requests</strong></p>
<p><strong>Requests Ready for Approval List</strong></p>
<p><strong>Process a Request Menu ...</strong></p>
<p><strong>Display Control Point Activity Menu ...</strong></p>
<p><strong>Funds Control Menu ...</strong></p>
<p><strong>Status of Requests Reports Menu ...</strong></p>
<p><strong>Record Date Received by Service Menu ...</strong></p>
<p><strong>Enter/Edit Control Point Users</strong></p>
<p><strong>Record Receipt of Multiple Delivery Schedule Items</strong></p>
<p><strong>Multiple Delivery Schedule List</strong></p>
<p><strong>Select Control Point Official's Menu Option: Display Control Point Activity Menu</strong></p>
<p><strong>Purchase Order Status</strong></p>
<p><strong>Transaction Status Report</strong></p>
<p><strong>Running Balances</strong></p>
<p><strong>Temporary Transaction Listing</strong></p>
<p><strong>Item History</strong></p>
<p><strong>PPM Status of Transactions Report</strong></p>
<p><strong>CP Entered, Not Approved Requests</strong></p>
<p><strong>Select Display Control Point Activity Menu Option: Running Balances</strong></p>
<p><strong>Select FISCAL YEAR: 00//</strong></p>
<p><strong>Select QUARTER: 3//</strong></p>
<p><strong>Select CONTROL POINT: 101 LAB TESTING 101//</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Setting Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you if you want to see a summary report (which lists only the balances and totals for the Control Point) or the entire report (which also lists the transactions and their costs). To see the entire report, answer “N”.

<span id="_Toc222496815" class="anchor"></span>Figure 15: Control Point Balance Report Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Summary Balances Report Only? No// (No)</strong></p>
<p><strong>DEVICE: HOME// LAT RIGHT MARGIN: 80//</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Transaction Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report has three sections. The first section lists each transaction type (TXN), including funding and expense transactions. This section also lists the obligation number (OBL \#), the committed cost (COMM \$AMT), the Control Point balance (CP \$BAL), the obligation/ceiling amount (OBL \$AMT) and the un-obligated balance (UNOBL \$BAL). The obligation number is the number that Fiscal Service assigns to the 1358 form.

The numbers in the COMM \$AMT column are estimated costs for the requests. Costs with an asterisk (\*) are transactions that you haven’t approved. Those with an “at” sign (@) are awaiting reconciliation. Those with a pound sign (#) are cancelled.

The numbers in the OBL \#AMT column are the amounts that the Accounting Technician in Fiscal has obligated for request. Blank values and values with an asterisk represent transactions that the Accounting Technician hasn’t approved.

<span id="_Toc222496816" class="anchor"></span>Figure 16: Transaction Listing (Section 1)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>CONTROL POINT BALANCE - 999-94-4-110- Stuff OCT 13,1994@13:38:58 PAGE 1</strong></p>
<p><strong>FISCAL</strong></p>
<p><strong>FYQSeq# TXN OBL # AP/OB DT COMM $AMT CP $BAL OBL $AMT UNOBL $BAL</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>0010003 CAN 0.00# 0.00 0.00# 0.00</strong></p>
<p><strong>0030007 CEI 12/27/99 10000.00 10000.00 10000.00 10000.00</strong></p>
<p><strong>0030011 CEI 12/27/99 1000000.00 1010000.00 1000000.00 1010000.00</strong></p>
<p><strong>0030017 OBL P91001 04/12/00 70.50@9999029.50 1010000.00</strong></p>
<p><strong>0030018 ADJ P91001-1 04/13/00 0.00 9999029.50 0.00 1010000.00</strong></p>
<p><strong>0030019 OBL B70001 04/14/00 3.35@9999026.15 1010000.00</strong></p>
<p><strong>0030020 ADJ B70001-1 04/14/00 0.00 9999026.15 0.00 1010000.00</strong></p>
<p><strong>0030021 ADJ P91001-2 04/14/00 0.00 9999026.15 0.00 1010000.00</strong></p>
<p><strong>0030022 ADJ P91001-3 04/17/00 0.00 9999026.15 0.00 1010000.00</strong></p>
<p><strong>0030023 ADJ P91001-4 04/17/00 0.00 9999026.15 0.00 1010000.00</strong></p>
<p><strong>0030025 CEI FROM 00-2 2030000.00 3039926.15 2030000.00 3040000.00</strong></p>
<p><strong>0030027 ADJ QTRADJ 0.00 3039926.15 3040000.00</strong></p>
<p><strong>0030028 ISS 0.00#3039926.15 0.00#3040000.00</strong></p>
<p><strong>Press return to continue, uparrow (^) to exit:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### FMS Transaction Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second section of the report lists the FMS transactions by the transaction number, date and time, the transaction amount, and their effect on the uncommitted and unobligated balances of the Control Point. FMS transactions are transactions of funds, not purchases.

The bottom of the report will list the total discrepancy between the committed fund transactions and the actual fund transactions (FMS transaction total). The report will also list the total amount of fund transactions you have committed but the Accounting Technician in Fiscal is not obligated.

If you want to run another running balance report, answer “Y” at the Would you like to run another running balance report? prompt. If not, press \<Enter\> to return to the Display Control Point Activity menu.

<span id="_Toc222496817" class="anchor"></span>Figure 17: Transaction Listing (Sections 2 and 3)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>CONTROL POINT BALANCE - 999-00-3-060- FISCAL OCT 13, 1994@17:40:04 PAGE 2</strong></p>
<p><strong>FISCAL</strong></p>
<p><strong>FYQSeq# TXN OBL # AP/OB DT COMM $AMT CP $BAL OBL $AMT UNOBL $BAL</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>FMS transaction total for this quarter: $0.00</strong></p>
<p><strong>================================================================================</strong></p>
<p><strong>Balance Summary 1st Quarter 2nd Quarter 3rd Quarter 4th Quarter</strong></p>
<p><strong>Actual CP Bal: 0.00 0.00 3039926.15 1010000.00</strong></p>
<p><strong>Actual Fiscal Bal: 0.00 0.00 3040000.00 1010000.00</strong></p>
<p><strong>Tot Commit, not Obl: 0.00 0.00 73.85 0.00</strong></p>
<p><strong>SECTION 1 CODES # - cancelled order * - order not obligated or signed</strong></p>
<p><strong>@ - purchase card order for reconciliation</strong></p>
<p><strong>&amp; - reconciled order with final charge - ready for approval</strong></p>
<p><strong>R - total reconciled charges</strong></p>
<p><strong>SECTION 2 CODES</strong></p>
<p><strong>@ - purchase card CC transaction is not reconciled</strong></p>
<p><strong>The symbols '*','@', and '&amp;' indicate incomplete items.</strong></p>
<p><strong>Please take the necessary steps to clear these items.</strong></p>
<p><strong>Would you like to run another running balances report? No// (No)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# How to Determine the Status of a Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter is adapted from the Control Point Requestor User’s Guide.

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP requests pass through several stages: the processing stage, where requests are created and approved for spending; the accounting stage, where a deduction and an order are created and associated to the request; the inventory stage, where the order is filled; and the payment stage, where the funds are deducted and the vendor is paid. IFCAP will tell you at what stage your request is.

## Determine the Status of a Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222496818" class="anchor"></span>Figure 18 :Sample Status of Requests Reports Menu Screen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Approve Requests</strong></p>
<p><strong>Requests Ready for Approval List</strong></p>
<p><strong>Process a Request Menu ...</strong></p>
<p><strong>Display Control Point Activity Menu ...</strong></p>
<p><strong>Funds Control Menu ...</strong></p>
<p><strong>Status of Requests Reports Menu ...</strong></p>
<p><strong>Record Date Received by Service Menu ...</strong></p>
<p><strong>Enter/Edit Control Point Users</strong></p>
<p><strong>Record Receipt of Multiple Delivery Schedule Items</strong></p>
<p><strong>Multiple Delivery Schedule List</strong></p>
<p><strong>Select Control Point Official's Menu Option: status of Requests Reports Menu</strong></p>
<p><strong>Print/Display Request Form</strong></p>
<p><strong>Status of All Obligation Transactions</strong></p>
<p><strong>Requests Ready for Approval List</strong></p>
<p><strong>PO with Associated Transactions</strong></p>
<p><strong>Select Status of Requests Reports Menu Option: status of All Obligation Transactions</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Display 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display a transaction report. Look at the STATUS field. See ![](ifcap-version-5-1-control-point-official-user-s-guide/032.png)

Figure 21: IFCAP Process Flowchart (Part 2) for information on how to use this status to determine who you need to contact to follow up on the transaction.

<span id="_Toc222496819" class="anchor"></span>Figure 19: Status of Requests Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER: 999</strong></p>
<p><strong>Select FISCAL YEAR: 00//</strong></p>
<p><strong>Select QUARTER: 4// 3</strong></p>
<p><strong>Select CONTROL POINT: 110 Stuff .01 0160A1 10 0100 010042116</strong></p>
<p><strong>DEVICE: UCX/TELNET Right Margin: 80//</strong></p>
<p><strong>STATUS OF OBLIGATION TRANSACTIONS CP: 110 Stuff .01 FY: 00</strong></p>
<p><strong>JUL 12,2000 18:08 PAGE 1</strong></p>
<p><strong>PRIORITY DATE</strong></p>
<p><strong>OF DATE DATE DATE RECEIVED</strong></p>
<p><strong>TRANS # REQUEST SIGNED REQUIRED DELIVERED BY SVC</strong></p>
<p><strong>VENDOR STATUS</strong></p>
<p><strong>OBLIGATION# SORT GROUP</strong></p>
<p><strong>FIRST LINE ITEM DESCRIPTION</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>00-3-0093 STANDARD 05/04/00</strong></p>
<p><strong>IFUSER2,SIX</strong></p>
<p><strong>WIDGETS</strong></p>
<p><strong>00-3-0094 STANDARD 04/04/00 05/04/00</strong></p>
<p><strong>SUPPLY WAREHOUSE Assigned to IFUSER3,SEVEN</strong></p>
<p><strong>CATS</strong></p>
<p><strong>STATUS OF OBLIGATION TRANSACTIONS CP: 110 Stuff .01 FY: 00</strong></p>
<p><strong>JUL 12,2000 18:08 PAGE 2</strong></p>
<p><strong>PRIORITY DATE</strong></p>
<p><strong>OF DATE DATE DATE RECEIVED</strong></p>
<p><strong>TRANS # REQUEST SIGNED REQUIRED DELIVERED BY SVC</strong></p>
<p><strong>VENDOR STATUS</strong></p>
<p><strong>OBLIGATION# SORT GROUP</strong></p>
<p><strong>FIRST LINE ITEM DESCRIPTION</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p>
<p><strong>00-3-0095 STANDARD 06/29/00 05/04/00</strong></p>
<p><strong>IFUSER2,SIX Pending Accountable Officer Sig.</strong></p>
<p><strong>WIDGETS</strong></p>
<p><strong>00-3-0096 STANDARD 06/29/00 05/04/00</strong></p>
<p><strong>SUPPLY WAREHOUSE Pending Accountable Officer Sig.</strong></p>
<p><strong>CATS</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Find the status in Table 6: Status and Node Assignment below. The “node numbers” in the table (like “*17*”) represent nodes in the flowcharts (Figure 20: IFCAP Process Flowchart (Part 1) and Figure 21: IFCAP Process Flowchart (Part 2)) on the pages following the table. Contact the representative at that node. In the example above, the status for the WIDGETS is Pending Accountable Officer Sig.

According to the table, this means that the transaction may be at node ![](ifcap-version-5-1-control-point-official-user-s-guide/033.png) ![](ifcap-version-5-1-control-point-official-user-s-guide/034.png) or ![](ifcap-version-5-1-control-point-official-user-s-guide/035.png). In this example, you will contact the Personal Property Management Accountable Officer if you have specific questions about the status of your request.

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>If the Status of Request, Transaction, or Purchase Order is…</th>
<th>Then the request is pending action at node number…</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Assigned to PPM Clerk</td>
<td><em><strong>17</strong></em></td>
</tr>
<tr class="even">
<td>Assigned to Purchasing Agent</td>
<td><em><strong>19</strong></em></td>
</tr>
<tr class="odd">
<td>Awaiting Payment</td>
<td><em><strong>38</strong></em> through <em><strong>43</strong></em>, depending on order</td>
</tr>
<tr class="even">
<td>Cancelled – 1358</td>
<td><em><strong>6</strong></em> Rejected. Start from scratch.</td>
</tr>
<tr class="odd">
<td>Cancelled Order</td>
<td><em><strong>19</strong></em> IFCAP Ordering Officer cancelled the IFCAP 2237 request that was never sent to eCMS.</td>
</tr>
<tr class="even">
<td>Cancelled Order</td>
<td><em><strong>19</strong></em> Contracting Officer in eCMS cancelled the 2237 that was sent to eCMS for processing.</td>
</tr>
<tr class="odd">
<td>Complete Order Received</td>
<td><em><strong>36</strong></em> or <em><strong>37</strong></em></td>
</tr>
<tr class="even">
<td>Complete Order Received (Amended)</td>
<td>Same as above, just that the Purchasing Agent has amended the Purchase Order.</td>
</tr>
<tr class="odd">
<td>Complete Order Received but Not Obligated</td>
<td><p>Past <em><strong>32, 33</strong></em>, but <em><strong>23</strong></em> or <em><strong>24</strong></em> has been skipped.</p>
<p>Talk to the Accounting Technician.</p></td>
</tr>
<tr class="even">
<td>Forward to Imprest Funds Agent</td>
<td><em><strong>19</strong></em></td>
</tr>
<tr class="odd">
<td>Held for Review in Personal Prop.</td>
<td><em><strong>17</strong></em></td>
</tr>
<tr class="even">
<td>Held in P&amp;C Pending Return of Quotations</td>
<td><em><strong>19</strong></em></td>
</tr>
<tr class="odd">
<td>Issue Pending Delivery from Warehouse</td>
<td><em><strong>29, 33</strong></em>, or ![](ifcap-version-5-1-control-point-official-user-s-guide/036.png).</td>
</tr>
<tr class="even">
<td>Issue Request Pending Fiscal Action</td>
<td>This status is not used. Currently, Fiscal Service does not process Issue Book orders.</td>
</tr>
<tr class="odd">
<td>Obligated - 1358</td>
<td><em><strong>20</strong></em></td>
</tr>
<tr class="even">
<td>Obligated - Awaiting Invoice</td>
<td><em><strong>27</strong></em></td>
</tr>
<tr class="odd">
<td>Order Not Completely Prepared</td>
<td><em><strong>19</strong></em> The IFCAP Ordering Officer (Purchasing Agent) has assigned a Purchase Order number to it but has not transmitted it to the Accounting Technician yet.</td>
</tr>
<tr class="even">
<td>Ordered (No Fiscal Action Required)</td>
<td><em><strong>30</strong></em> This status means that funds are not obligated for this type of Purchase Order, so it skipped node 23.</td>
</tr>
<tr class="odd">
<td>Ordered and Obligated</td>
<td><em><strong>28</strong></em> or <em><strong>30</strong></em>. Talk to the vendor.</td>
</tr>
<tr class="even">
<td>Ordered and Obligated (Amended)</td>
<td>Same as above, just that the Purchasing Agent amended the Purchase Order.</td>
</tr>
<tr class="odd">
<td>Partial Issue Delivered</td>
<td><em><strong>29</strong></em> or ![](ifcap-version-5-1-control-point-official-user-s-guide/037.png).</td>
</tr>
<tr class="even">
<td>Partial Order Received</td>
<td><em><strong>36, 37, 38, 39, 41</strong></em>or ![](ifcap-version-5-1-control-point-official-user-s-guide/038.png). Talk to the Accounting Technician if you want to know if they’ve sent the payment order.</td>
</tr>
<tr class="odd">
<td>Partial Order Received (Amended)</td>
<td>Same as above, just that the Purchasing Agent amended the Purchase Order.</td>
</tr>
<tr class="even">
<td>Partial Received (No Fiscal Action Req)</td>
<td>Same as Partial Order Received, except that this status means that, because no fiscal action is required, this Purchase Order will skip either <em><strong>38</strong></em> or <em><strong>39</strong></em>.</td>
</tr>
<tr class="odd">
<td>Partial Received but Not Obligated</td>
<td>Same as Partial Order Received, except that this status means that funds are not obligated for this type of Purchase Order, so it skipped node <em><strong>23</strong></em>.</td>
</tr>
<tr class="even">
<td>Pending Accountable Officer Signature</td>
<td><em><strong>14, 15,18</strong></em></td>
</tr>
<tr class="odd">
<td>Pending CP Official’s Signature</td>
<td><em><strong>7,9,11</strong></em></td>
</tr>
<tr class="even">
<td>Pending Completion by CP Clerk</td>
<td><em><strong>4, 6, 8</strong></em></td>
</tr>
<tr class="odd">
<td>Pending Completion by Requestor</td>
<td><em><strong>5</strong></em></td>
</tr>
<tr class="even">
<td>Pending Contracting Officers Signature</td>
<td><em><strong>19</strong></em></td>
</tr>
<tr class="odd">
<td>Pending Fiscal Action</td>
<td><em><strong>12, 23, 24</strong></em></td>
</tr>
<tr class="even">
<td>Pending PPM Clerk Signature</td>
<td><em><strong>17, 18</strong></em></td>
</tr>
<tr class="odd">
<td>Request Clarification by Service for P&amp;C</td>
<td><em><strong>19</strong></em></td>
</tr>
<tr class="even">
<td>Returned to Accountable Officer by eCMS (P&amp;C)</td>
<td>2237 has been sent back to the AO from eCMS to be processed entirely within IFCAP. Current Status: Pending Accountable Officer Signature.</td>
</tr>
<tr class="odd">
<td>Returned to Service by eCMS (P&amp;C)</td>
<td>2237 has been sent back to the Service from eCMS for Edit and Re-approval Currently at <em><strong>4.</strong></em> Ask the Contracting Officer why it was returned if the explanation is not in the Return to Service Comments: line on the request.</td>
</tr>
<tr class="even">
<td>Returned to Service by PPM</td>
<td>Died at <em><strong>14</strong></em> or <em><strong>17</strong></em>; currently at <em><strong>4</strong></em>. Ask the PPM Accountable Officer and PPM Requisition Clerk which one of them killed it and why, if the explanation is not in the Return to Service Comments: line on the request.</td>
</tr>
<tr class="odd">
<td>Returned to Supply (Pending Signature)</td>
<td>Died at <em><strong>23</strong></em>; currently at <em><strong>19.</strong></em> The Accounting Technician returned the Purchase Order, usually because the Control Point does not have enough money to cover the Purchase Order.</td>
</tr>
<tr class="even">
<td>Sent to eCMS (P&amp;C)</td>
<td>2237 data have been transmitted to eCMS for order &amp; award processing.</td>
</tr>
<tr class="odd">
<td>Sent to Purchasing and Contracting</td>
<td><em><strong>19</strong></em></td>
</tr>
<tr class="even">
<td>Transaction Complete</td>
<td><p>Certified Purchase Orders: your request could be at <em><strong>30, 34, 37, 39, 42</strong></em> or ![](ifcap-version-5-1-control-point-official-user-s-guide/039.png).</p>
<p>All other requests: <em><strong>41, 42, 43</strong></em>, or ![](ifcap-version-5-1-control-point-official-user-s-guide/040.png).</p></td>
</tr>
<tr class="odd">
<td>Transaction Complete (Amended)</td>
<td>Same as above, just that the IFCAP Ordering Officer (Purchasing Agent) amended the Purchase Order.</td>
</tr>
</tbody>
</table>

According to the table, this means that the transaction may be at node *14,15*, or *18*. In this example, you will contact the Personal Property Management Accountable Officer if you have specific questions about the status of your request.

<span id="_Ref222296746" class="anchor"></span>Figure 20: IFCAP Process Flowchart (Part 1)

<span id="_Ref222296787" class="anchor"></span>![](ifcap-version-5-1-control-point-official-user-s-guide/041.png)

Figure 21: IFCAP Process Flowchart (Part 2)

![](ifcap-version-5-1-control-point-official-user-s-guide/042.png)

# Supplemental Control Point Official Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the options available to you in IFCAP that weren’t mentioned in the previous chapters. Each section of this chapter defines the purpose of the option, the menu path to reach the option in the menus, what information to enter at the prompts, and how to interpret the output that the option creates.

## Options in the Funds Control Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enter FCP Adjustment Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Setup Parameters

Enter a FISCAL YEAR: and a fiscal QUARTER: at the prompts. Enter a CONTROL POINT. If you do not know the Control Point, enter three question marks (???) and IFCAP will list the available Control Points. IFCAP will assign a transaction number to the adjustment.

<span id="_Toc222496822" class="anchor"></span>Figure 22: FCP Adjustment Data Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option: Enter FCP Adjustment Data</strong></p>
<p><strong>Select FISCAL YEAR: 94//</strong></p>
<p><strong>Select QUARTER: 4//</strong></p>
<p><strong>Select CONTROL POINT: 022 IFVENDOR,THREE</strong></p>
<p><strong>This transaction is assigned transaction number: 002-94-4-022-0008</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Enter Reference Number

- At the OBLIGATION NUMBER: prompt, enter a reference number for the transaction. The obligation number may be used. If you do not know the obligation number, enter three question marks and IFCAP will list the available obligation numbers.
- If this purchase is assigned to a project, office, or some other category for which a Sort Group has been created, enter that Sort Group at the SORT GROUP: prompt.
- If this purchase doesn’t belong to a Sort Group, just press \<Enter\>. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the Sort Group and exclude all purchases that don’t belong to the Sort Group.
- At the DATE OBL ADJUSTED: prompt, enter today’s date.
- At the ADJUSTMENT \$ AMOUNT: prompt enter the adjustment dollar amount for this obligation transaction.
- If this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses, enter that cost center at the COST CENTER: prompt. Cost centers allow Fiscal staff to create total expense records for a section or service.

<span id="_Ref222296340" class="anchor"></span>Figure 23: Enter Reference Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>OBLIGATION NUMBER: ???</strong></p>
<p><strong>Enter the 6 character purchase order/obligation/reference number for this</strong></p>
<p><strong>transaction</strong></p>
<p><strong>??</strong></p>
<p><strong>OBLIGATION NUMBER: C40021</strong></p>
<p><strong>SORT GROUP:</strong></p>
<p><strong>DATE OBL ADJUSTED:</strong></p>
<p><strong>ADJUSTMENT $ AMOUNT: ??</strong></p>
<p><strong>This is the adjustment dollar amount for this obligation</strong></p>
<p><strong>transaction.</strong></p>
<p><strong>ADJUSTMENT $ AMOUNT: 40 $ 40.00</strong></p>
<p><strong>COST CENTER: 870021 Operating Equipment</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Budget Object Code

At the BOC1: prompt, enter the Budget Object Code (BOC) classification for the item. If you do not know the budget object code, enter three question marks (???) at the prompt and IFCAP will display the available budget object codes.

<span id="_Toc222496824" class="anchor"></span>Figure 24: Enter Budget Object Code

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>BOC1: ???</strong></p>
<p><strong>Select the appropriate budget object code for this request.</strong></p>
<p><strong>Major budget object code classifications are:</strong></p>
<p><strong>10 thru 13 - Personal Services and Benefits</strong></p>
<p><strong>21 - Travel and Transportation of Persons</strong></p>
<p><strong>22 - Transportation of Things</strong></p>
<p><strong>23 - Rent, Communications, and Utilities</strong></p>
<p><strong>24 - Printing and Reproduction</strong></p>
<p><strong>25 - Other Services</strong></p>
<p><strong>26 - Supplies and Materials</strong></p>
<p><strong>31 thru 33 - Acquisition of Capital Assets</strong></p>
<p><strong>Answer with BOC</strong></p>
<p><strong>Do you want the entire 27-Entry BOC List? Y (Yes)</strong></p>
<p><strong>Choose from:</strong></p>
<p><strong>2220 Other Shipments</strong></p>
<p><strong>2299 LAB TEST BOC</strong></p>
<p><strong>2343 ADP Equipment Rental</strong></p>
<p><strong>2520 Repair of Furniture and Equipment</strong></p>
<p><strong>2535 Interior Decorating Services</strong></p>
<p><strong>2540 Laundry and Drycleaning Services</strong></p>
<p><strong>2543 Maintenance and Repair Services</strong></p>
<p><strong>BOC1: 2540 Laundry and Drycleaning S</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Enter Amount

- At the BOC1 \$ AMOUNT: prompt, enter the amount of the item you want to attribute to the budget object code. Enter a second BOC at the BOC2: prompt if you like.
- If you like, Select SUB-CONTROL POINT.
- Add COMMENTS: if you wish. You may enter another adjustment transaction or return to the Funds Control Menu.

<span id="_Toc222496825" class="anchor"></span>Figure 25: Enter Budget Object Code Amount

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>BOC1 $ AMOUNT: ?? This is the dollar amount applied to the budget object code.</strong></p>
<p><strong>BOC1 $ AMOUNT: 40. $ 40.00</strong></p>
<p><strong>BOC2:</strong></p>
<p><strong>BOC2 $ AMOUNT:</strong></p>
<p><strong>TRANSACTION BEG BAL: 40.00</strong></p>
<p><strong>Select SUB-CONTROL POINT:</strong></p>
<p><strong>COMMENTS:</strong></p>
<p><strong>1&gt;</strong></p>
<p><strong>Would you like to enter another Adjustment transaction? YES// n (NO)</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Assigning Ceiling to Sub-Control Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Setup Parameters

Enter the CONTROL POINT. If you do not know the Control Point, enter three question marks (???) and IFCAP will list the available Control Points.

<span id="_Toc222496826" class="anchor"></span>Figure 26: Sub-Control Point Ceiling Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option: Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Select CONTROL POINT: ??</strong></p>
<p><strong>CHOOSE FROM:</strong></p>
<p><strong>11 011 CONSULTANT &amp; ATTENDING</strong></p>
<p><strong>33 033 337 Pharmacy Test</strong></p>
<p><strong>101 101 LAB TESTING 101</strong></p>
<p><strong>Select CONTROL POINT: 101 LAB TESTING 101</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Select Ceiling Transaction

Enter the CEILING TRANSACTION NUMBER. If you do not know the ceiling transaction number, enter three question marks (???) and IFCAP will list the available ceiling transaction numbers. IFCAP will list the balance of the transaction you selected.

<span id="_Toc222496827" class="anchor"></span>Figure 27: Select Ceiling Transaction

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select CEILING TRANSACTION NUMBER: ???</strong></p>
<p><strong>Attempting lookup in transaction file.</strong></p>
<p><strong>Attempting lookup using 101 LAB TESTING 101 (CONTROL POINT)</strong></p>
<p><strong>1 101 LAB TESTING 101 999-94-4-101-0285 CEIL 999FC0139 This is a multiple transaction for a widget.</strong></p>
<p><strong>2 101 LAB TESTING 101 999-94-3-101-0284 CEIL 999FC0138 This is a multiple transaction for a widget.</strong></p>
<p><strong>3 101 LAB TESTING 101 999-94-2-101-0283 CEIL This is a multiple transaction for a widget.</strong></p>
<p><strong>4 101 LAB TESTING 101 999-94-1-101-0282 CEIL This is a multiple transaction for a widget.</strong></p>
<p><strong>5 101 LAB TESTING 101 999-94-4-101-0258 CEIL FC0135 Test</strong></p>
<p><strong>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</strong></p>
<p><strong>CHOOSE 1-5: 1 999-94-4-101-0285</strong></p>
<p><strong>TRANSACTION BEG BAL: 533.00</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Enter Sub-Control Point

Enter one or more Sub-Control Points if you like. At the \$ AMOUNT: prompt, enter the amount of the ceiling. IFCAP will deduct the ceiling amount you enter from the transaction amount and ask if you want to assign it to another Sub-Control Point. You may also assign a ceiling to Sub-Control Points from another ceiling transaction. After completing the ceiling assignment, IFCAP will return to the Funds Control Menu.

<span id="_Toc222496828" class="anchor"></span>Figure 28: Enter Sub-Control Point

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select SUB-CONTROL POINT: 1 ??</strong></p>
<p><strong>Select SUB-CONTROL POINT: ???</strong></p>
<p><strong>This is an additional sub-control point. IFCAP</strong></p>
<p><strong>allows more than one sub-control point on each transaction</strong></p>
<p><strong>to get a quantity discount.</strong></p>
<p><strong>CHOOSE FROM:</strong></p>
<p><strong>100</strong></p>
<p><strong>IFUSER2,FIVE</strong></p>
<p><strong>SHOES</strong></p>
<p><strong>TEST</strong></p>
<p><strong>This is the name of the sub-control point.</strong></p>
<p><strong>Select SUB-CONTROL POINT: 100</strong></p>
<p><strong>ARE YOU ADDING '100' AS A NEW SUB-CONTROL POINT (THE 1ST FOR THIS CONTROL POIN</strong></p>
<p><strong>T ACTIVITY)? Y</strong></p>
<p><strong>(Yes)</strong></p>
<p><strong>$ AMOUNT: 230 RUNNING TOTAL: 230.00 BAL: 303.00</strong></p>
<p><strong>Select SUB-CONTROL POINT:</strong></p>
<p><strong>The transaction $ amount is $ 533.00.</strong></p>
<p><strong>You still have $ 303.00 available that could be assigned to your</strong></p>
<p><strong>sub-control points. Do you want to re-edit your entries? Yes// (Yes)</strong></p>
<p><strong>TRANSACTION BEG BAL: 533.00</strong></p>
<p><strong>Select SUB-CONTROL POINT: 100// Shoes</strong></p>
<p><strong>ARE YOU ADDING 'SHOES' AS A NEW SUB-CONTROL POINT (THE 2ND FOR THIS CONTROL PO</strong></p>
<p><strong>INT ACTIVITY)? Y</strong></p>
<p><strong>(Yes)</strong></p>
<p><strong>$ AMOUNT: 303 RUNNING TOTAL: 533.00 BAL: 0.00</strong></p>
<p><strong>Select SUB-CONTROL POINT:</strong></p>
<p><strong>Would you like to assign ceiling to sub-control points from another ceiling transaction? No// (No)</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Recalculate Fund Control Point Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option recalculates the Fund Control Point balance that the Control Point Official sees when approving a request. This option should only be used if the Fund Control Point balance differs from the running balance.

From the Control Point Official’s Menu, select Funds Control Menu.

From the Funds Control Menu, select Recalculate Fund Control Point Balance.

Enter a fiscal year, a fiscal quarter and a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will display the available Control Points. IFCAP will send a mail message to the Control Point Official when it has finished recalculating the balance.

<span id="_Toc222496829" class="anchor"></span>Figure 29: Recalculate Fund Control Point Balance

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option: Recalculate Fund Control Point Balance</strong></p>
<p><strong>Select FISCAL YEAR: 94//</strong></p>
<p><strong>Select QUARTER: 4//</strong></p>
<p><strong>Select CONTROL POINT: 101 LAB TESTING 101</strong></p>
<p><strong>Submit RECALCULATE CONTROL POINT BALANCES to the TASK MANAGER? YES//</strong></p>
<p><strong>Requested Start Time: NOW// (JUN 21, 2000@16:54:06)</strong></p>
<p><strong>RECALCULATE CONTROL POINT BALANCES HAS TASK NUMBER 211610</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Options in the Funds Control Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Quarterly Report

#### Report Parameters

Enter a FISCAL YEAR, fiscal QUARTER and a CONTROL POINT when prompted. Enter an output device.

<span id="_Toc222496830" class="anchor"></span>Figure 30: Control Point Quarterly Report Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option: Funds Control Reports Menu</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option: Quarterly Report</strong></p>
<p><strong>Select FISCAL YEAR: 94//</strong></p>
<p><strong>Select QUARTER: 4//</strong></p>
<p><strong>Select CONTROL POINT: 101 LAB TESTING 101//</strong></p>
<p><strong>...OK? Yes// (Yes)</strong></p>
<p><strong>DEVICE: LAT RIGHT MARGIN: 80//</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Display

IFCAP will display the *Control Point Quarterly Report,* which lists the transaction, the type, the cost, and the Control Point Balance. At the end of the report, IFCAP will list the total amount of committed, un-obligated money for the Control Point and the total uncommitted balance for the Control Point from current and prior quarters. At the Would You Like to Run Another Quarterly Balance Report? prompt, press \<Enter\> to return to the Funds Control Reports Menu.

<span id="_Toc222496831" class="anchor"></span>Figure 31: Control Point Quarterly Report Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>QUARTERLY REPORT - 999-97-2-120- DIET FEB 28, 1997@14:24:41 PAGE: 1</strong></p>
<p><strong>TRANS $ OBL/CEIL DATE DATE DATE</strong></p>
<p><strong>SEQ# TYPE PO/OBL# AMOUNT $ AMOUNT REQ. OBL. REC'D.</strong></p>
<p><strong>CONTROL POINT UNCOMMITTED UNOBLIGATED</strong></p>
<p><strong>REQUEST TOTAL BALANCE BALANCE</strong></p>
<p><strong>VENDOR FIRST LINE DESCRIPTION</strong></p>
<p><strong>COMMENT</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>0002 OBL 10.00 100.00 FEB 25, 1997</strong></p>
<p><strong>10.00 90.00 90.00</strong></p>
<p><strong>GENERAL MEDICAL</strong></p>
<p><strong>=============================================================================</strong></p>
<p><strong>QUARTERLY REPORT 999-97-2-120- DIET FEB 28, 1997@14:24:41 PAGE: 2</strong></p>
<p><strong>__________PO TRANSACTIONS WITHOUT 2237____________</strong></p>
<p><strong>PO/ PO OBLIGATED CONTROL PT. UNCOMMITTED UNOBLIGATED</strong></p>
<p><strong>OBL# DATE AMOUNT REQ TOT BALANCE BALANCE</strong></p>
<p><strong>=============================================================================</strong></p>
<p><strong>999-B70004 FEB 25, 1997 10.00 20.00 80.00 80.00</strong></p>
<p><strong>PO transaction (no 2237) total for this quarter: $10.00</strong></p>
<p><strong>=============================================================================</strong></p>
<p><strong>FMS transaction total for this quarter: $0.00</strong></p>
<p><strong>=============================================================================</strong></p>
<p><strong>Total Request Amount: $20.00</strong></p>
<p><strong>Control Point Official's Balance: $80.00</strong></p>
<p><strong>Fiscal's Unobligated Balance: $80.00</strong></p>
<p><strong>Would you like to run another quarterly balance report? No// (No)</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Ceiling Report

#### Report Parameters

Enter a FISCAL YEAR:, fiscal QUARTER: and a CONTROL POINT: when prompted.

<span id="_Toc222496832" class="anchor"></span>Figure 32: Sample Quarterly Report Parameters Screen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option: Funds Control Reports Menu</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option: Ceiling Report</strong></p>
<p><strong>Select FISCAL YEAR: 94//</strong></p>
<p><strong>Select QUARTER: 4//</strong></p>
<p><strong>Select CONTROL POINT: 101 LAB TESTING 101</strong></p>
<p><strong>DEVICE: LAT RIGHT MARGIN: 80//</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Display

IFCAP will create a *Ceiling Report* which lists the transaction number, ceiling amount, the date the funds were allocated, and comments.

At the Select Fiscal Year: prompt, enter a caret (^) to return to the Funds Control Reports Menu.

<span id="_Toc222496833" class="anchor"></span>Figure 33: Sample Ceiling Report Screen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>CEILING REPORT - CP: 101 LAB TESTING 101 JUL 8,1994 18:24 PAGE 1</strong></p>
<p><strong>TRANS # PAT #</strong></p>
<p><strong>CEILING $ DATE</strong></p>
<p><strong>AMOUNT ALLOCATED</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>94-4-0004 500000.00 NOV 17,1993</strong></p>
<p><strong>94-4-0043 -20.00 JAN 13,1994</strong></p>
<p><strong>94-4-0047 25000.00 FEB 1,1994</strong></p>
<p><strong>94-4-0150 1000.04 APR 15,1994</strong></p>
<p><strong>94-4-0253 FC0135 40.00 MAY 27,1994 Training program</strong></p>
<p><strong>94-4-0258 FC0135 23412.00 JUN 6,1994 Test</strong></p>
<p><strong>94-4-0285 999FC0139 533.00 JUN 8,1994</strong></p>
<p><strong>This is a multiple transaction for a widget.</strong></p>
<p><strong>-----------</strong></p>
<p><strong>TOTAL 549965.04</strong></p>
<p><strong>Select FISCAL YEAR: 94// ^</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Audit Transaction List

#### Menu Path

From the Control Point Official’s Menu Option list, select Funds Control Menu.

<span id="_Toc222496834" class="anchor"></span>Figure 34: Audit Transaction List Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option: Funds Control Reports Menu</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option: Audit Transaction List</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Audit Transaction List Report Parameters

Enter a FISCAL YEAR:, a fiscal QUARTER: and a CONTROL POINT: at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

At the DATE: prompt, enter the last date for transactions that you want to audit. IFCAP will display the *820 Reconciliation Report*, listing the transaction number, the obligation number, and the FMS amount of the reconciliation. Enter a (^) caret at the Select Station Number: Select Fiscal Year: prompt to return to the Funds Control Reports Menu.

<span id="_Toc222496835" class="anchor"></span>Figure 35: Audit Transaction List Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER: 999 ANYCITY,ANYSTATE</strong></p>
<p><strong>Select FISCAL YEAR: 94//</strong></p>
<p><strong>Select QUARTER: 4//</strong></p>
<p><strong>Select CONTROL POINT: 101 LAB TESTING 101</strong></p>
<p><strong>...OK? Yes// (Yes)</strong></p>
<p><strong>Enter the cutoff date for this reconciliation report</strong></p>
<p><strong>DATE: T (FEB 14, 1997)</strong></p>
<p><strong>DEVICE: LAT RIGHT MARGIN: 80//</strong></p>
<p><strong>820 RECONCILIATION REPORT FEB 28, 1997 14:44 PAGE 1</strong></p>
<p><strong>CEILING $</strong></p>
<p><strong>TRANS # FMS CODE FMS DATE PO/OBL# TYPE AMOUNT</strong></p>
<p><strong>FMS</strong></p>
<p><strong>$AMT</strong></p>
<p><strong>OBL. COST</strong></p>
<p><strong>UNOBL CP UNOBL</strong></p>
<p><strong>BALANCE BALANCE</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>999-96-4-101-1647 07/26/96 C60038WR ADJ</strong></p>
<p><strong>210.00</strong></p>
<p><strong>210.00</strong></p>
<p><strong>-210.00 -210.00</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Sort Group Report

#### Menu Path

<span id="_Toc222496836" class="anchor"></span>Figure 36: Sort Group Report Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option: Funds Control Reports Menu</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option: Sort Group Report</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Sort Group Report Parameters

Enter a FISCAL YEAR, a fiscal QUARTER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

Enter the first SORT GROUP: you want to include on the report, or press \<Enter\> to include all Sort Groups. Enter an output device.

<span id="_Toc222496837" class="anchor"></span>Figure 37: Sort Group Report Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select FISCAL YEAR: 95//</strong></p>
<p><strong>Select QUARTER: 1//</strong></p>
<p><strong>Select CONTROL POINT: 101 LAB TESTING 101</strong></p>
<p><strong>...OK? Yes// (Yes)</strong></p>
<p><strong>START WITH SORT GROUP: FIRST//</strong></p>
<p><strong>DEVICE: LAT RIGHT MARGIN: 80//</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Sort Group Report Display

IFCAP will print or display a *Sort Group Report*, listing the transactions in each Sort Group, their purchase order or obligation number, the request type, the vendor, and the committed and obligated amounts. After printing or displaying the report, IFCAP will return to the Funds Control Reports Menu.

<span id="_Toc222496838" class="anchor"></span>Figure 38: Sort Group Report Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>SORT GROUP REPORT - CP: 101 LAB TESTING 101 DEC 30,1994 09:59 PAGE 1</strong></p>
<p><strong>TRANSACTION NUMBER PO/OBL# TYPE VENDOR COMM $ OBL $</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>SORT GROUP: TEST SORT</strong></p>
<p><strong>999-95-1-101-0083 A50031 OBL GENERIC GENERAL 10.00</strong></p>
<p><strong>999-95-1-101-0084 C50044 OBL CENTRAL BUSINES 60.00</strong></p>
<p><strong>----------- -----------</strong></p>
<p><strong>SUBTOTAL 70.00 0.00</strong></p>
<p><strong>----------- -----------</strong></p>
<p><strong>TOTAL 70.00 0.00</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Classification of Request Report

Amendments will automatically adjust FCP balances. The *Classification of Request Report* and *Sort Group Report* will accurately reflect cost amendments.

#### Classification of Request Report Menu Path

<span id="_Toc222496839" class="anchor"></span>Figure 39: Sort Group Report Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option: Funds Control Reports Menu</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option: Classification of Request Report</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Classification of Request Report Parameters

Enter a STATION NUMBER, a FISCAL YEAR, a fiscal QUARTER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

IFCAP will print the *Classification of Request Report*, listing each transaction by the classification that the Requestor entered at the START WITH CLASSIFICATION OF REQUEST: prompt. After printing the report, IFCAP will return to the Funds Control Reports Menu.

<span id="_Toc222496840" class="anchor"></span>Figure 40: Classification of Request Report Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER: 002 ANYTOWN, PA</strong></p>
<p><strong>Select FISCAL YEAR: 94//</strong></p>
<p><strong>Select QUARTER: 4//</strong></p>
<p><strong>Select CONTROL POINT: 022 IFVENDOR,THREE</strong></p>
<p><strong>...OK? Yes// (Yes)</strong></p>
<p><strong>START WITH CLASSIFICATION OF REQUEST: FIRST//</strong></p>
<p><strong>DEVICE: LAT RIGHT MARGIN: 80//</strong></p>
<p><strong>----------- -----------</strong></p>
<p><strong>CLASSIFICATION OF REQUEST REPORT - 101 LAB TESTING 101</strong></p>
<p><strong>OCT 12,1994 12:36 PAGE 1</strong></p>
<p><strong>OBL# TRANS# TYPE VENDOR COMM $ OBL $</strong></p>
<p><strong>COMMENTS</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>CLASSIFICATION OF REQUEST: Endurance test of capacitor</strong></p>
<p><strong>A50002 0006 OBL CENTRAL BUSINE 120.00 120.00</strong></p>
<p><strong>TESTING</strong></p>
<p><strong>----------- -----------</strong></p>
<p><strong>SUBTOTAL 120.00 120.00</strong></p>
<p><strong>CLASSIFICATION OF REQUEST: Vandalism repair</strong></p>
<p><strong>C50003 0003 OBL CENTRAL BUSINE 69.00 124.00</strong></p>
<p><strong>REPAIRS</strong></p>
<p><strong>----------- -----------</strong></p>
<p><strong>SUBTOTAL 69.00 124.00</strong></p>
<p><strong>----------- -----------</strong></p>
<p><strong>TOTAL 189.00 244.00</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Cost Center Totals

#### Cost Center Totals Menu Path

<span id="_Toc222496841" class="anchor"></span>Figure 41: Cost Center Totals Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option: Funds Control Reports Menu</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option: Cost Center Totals</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Cost Center Totals Report Parameters

Enter a STATION NUMBER, a FISCAL YEAR, a fiscal QUARTER and a CONTROL POINT at the appropriate prompts.

If this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses, at the COST CENTER NAME: prompt, enter the COST CENTER. Cost centers allow Fiscal staff to create total expense records for a section or service.

If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

<span id="_Toc222496842" class="anchor"></span>Figure 42: Cost Center Totals Report Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER: 002// ANYTOWN, PA</strong></p>
<p><strong>Select FISCAL YEAR: 94//</strong></p>
<p><strong>Select QUARTER: 4//</strong></p>
<p><strong>Select COST CENTER NAME: ???</strong></p>
<p><strong>CHOOSE FROM:</strong></p>
<p><strong>100000 100000 General Admin-Central Off Staff (Excl of Oper Depts) - Summary of Accts</strong></p>
<p><strong>110100 110100 Office of the Secretary</strong></p>
<p><strong>110200 110200 Off of Assoc Deputy Admstr for Congressional &amp; Intergovt'l Affairs</strong></p>
<p><strong>110300 110300 Board of Contract Appeals</strong></p>
<p><strong>110500 110500 Board of Veterans Appeals</strong></p>
<p><strong>111600 111600 Office of Public and Consumer Affairs</strong></p>
<p><strong>120000 120000 Office of the General Counsel</strong></p>
<p><strong>Select COST CENTER NAME: 111600 Office of Public and Co</strong></p>
<p><strong>DEVICE: HOME// LAT RIGHT MARGIN: 80//</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Cost Center Totals Report Display

IFCAP will print a *Cost Center Totals Report*, listing each transaction for the cost center. Enter a caret (^) at the “Select Station Number:” prompt to return to the Funds Control Reports Menu.

<span id="_Toc222496843" class="anchor"></span>Figure 43:Cost Center Totals Report Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>COST CENTER TOTALS REPORT JUL 8,1994@21:57:22 PAGE 1</strong></p>
<p><strong>STATION 002, 4TH QUARTER, FY94</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>COST CENTER: 822400 Pharmacy</strong></p>
<p><strong>CONTROL POINT: 040 OFC&amp;MISC SUP 90</strong></p>
<p><strong>----------------------------------</strong></p>
<p><strong>CONTROL POINT: 100 PHARMACY SVC 119</strong></p>
<p><strong>-----------------------------------</strong></p>
<p><strong>TOTALS FOR ALL CONTROL POINTS</strong></p>
<p><strong>----------------------------</strong></p>
<p><strong>TOTAL COMMITTED (ESTIMATED) COST: 826042.81</strong></p>
<p><strong>TOTAL OBLIGATED (ACTUAL) COST: 725194.04</strong></p>
<p><strong>TOTAL (BEST ESTIMATE) COST: 740985.77</strong></p>
<p><strong>Enter information for another report or an uparrow to return to the menu.</strong></p>
<p><strong>Select STATION NUMBER: 002// ^</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### BOC Totals

#### Menu Path

<span id="_Toc222496844" class="anchor"></span>Figure 44: BOC Totals Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></p>
<p><strong>Enter FCP Adjustment Data</strong></p>
<p><strong>Assign Ceiling to Sub-Control Points</strong></p>
<p><strong>Correct Sub-Control Point Amounts</strong></p>
<p><strong>Recalculate Fund Control Point Balance</strong></p>
<p><strong>Funds Control Reports Menu ...</strong></p>
<p><strong>Select Funds Control Menu Option: Funds Control Reports Menu</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option: BOC Totals</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### BOC Totals Report Parameters and Display

Enter a STATION NUMBER, a FISCAL YEAR, a fiscal QUARTER and a CONTROL POINT at the appropriate prompts.

If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

IFCAP will print a *Budget Object Code Totals Report*, listing the budget object code totals for the Control Point you specified. Enter a caret (^) at the “Select Station Number:” prompt to return to the Funds Control Reports Menu.

<span id="_Toc222496845" class="anchor"></span>Figure 45: BOC Totals Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select STATION NUMBER: 002// ANYTOWN, PA</strong></p>
<p><strong>Select FISCAL YEAR: 94//</strong></p>
<p><strong>Select QUARTER: 4//</strong></p>
<p><strong>Select CONTROL POINT: 022 IFVENDOR,THREE//</strong></p>
<p><strong>DEVICE: HOME// LAT RIGHT MARGIN: 80//</strong></p>
<p><strong>BUDGET OBJECT CODE TOTALS REPORT JUL 8,1994@21:59:53 PAGE 1</strong></p>
<p><strong>STATION 002, 4TH QUARTER, FY94 ,CONTROL POINT 022 IFVENDOR,THREE</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>BUDGET OBJECT CODE TOTALS</strong></p>
<p><strong>-----------------</strong></p>
<p><strong>2580 Miscellaneous Contractual Services by Individuals, Inst 175.00</strong></p>
<p><strong>2631 Chemical suplies 4427.74</strong></p>
<p><strong>2632 Other Medical and Dental Supplies 21851.70</strong></p>
<p><strong>2660 Operating Supplies and Materials 1307.40</strong></p>
<p><strong>-------------------------------------</strong></p>
<p><strong>TOTAL OBLIGATED (ACTUAL) COST: 27761.84</strong></p>
<p><strong>TOTAL OBLIGATED (ESTIMATED) COST: 27696.69</strong></p>
<p><strong>Enter information for another report or an uparrow to return to the menu.</strong></p>
<p><strong>Select STATION NUMBER: 002//^</strong></p>
<p><strong>Quarterly Report</strong></p>
<p><strong>Ceiling Report</strong></p>
<p><strong>Audit Transaction List</strong></p>
<p><strong>Sort Group Report</strong></p>
<p><strong>Classification of Request Report</strong></p>
<p><strong>Cost Center Totals</strong></p>
<p><strong>BOC Totals</strong></p>
<p><strong>Sub-Control Point Report</strong></p>
<p><strong>Reconciliation of PO/Sub-CP Dollar Amounts</strong></p>
<p><strong>BOC Detail Totals</strong></p>
<p><strong>FMS Transaction Data</strong></p>
<p><strong>Select Funds Control Reports Menu Option:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Sub-Control Point Report

#### Menu Path 

<span id="_Toc222496846" class="anchor"></span>Figure 46: Sub-Control Point Report Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enter FCP Adjustment Data</p>
<p>Assign Ceiling to Sub-Control Points</p>
<p>Correct Sub-Control Point Amounts</p>
<p>Recalculate Fund Control Point Balance</p>
<p>Funds Control Reports Menu ...</p>
<p>Select Funds Control Menu Option: Funds Control Reports Menu</p>
<p>Quarterly Report</p>
<p>Ceiling Report</p>
<p>Audit Transaction List</p>
<p>Sort Group Report</p>
<p>Classification of Request Report</p>
<p>Cost Center Totals</p>
<p>BOC Totals</p>
<p>Sub-Control Point Report</p>
<p>Reconciliation of PO/Sub-CP Dollar Amounts</p>
<p>BOC Detail Totals</p>
<p>FMS Transaction Data</p>
<p>Select Funds Control Reports Menu Option: Sub-Control Point Report</p></td>
</tr>
</tbody>
</table>

#### Sub-Control Point Report Print

You may print the report for an entire fiscal year, or for a quarter that you specify.

Enter a STATION NUMBER, a FISCAL YEAR, a fiscal QUARTER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

You may list all of the Sub-Control Points, or you may begin the report at a Sub-Control Point that you specify. IFCAP will list all of the Sub-Control Point expenditures for the Control Point by fiscal quarter, TRANS (transaction) \# (number) and TYPE, VENDOR name, the FIRST LINE of the ITEM DESCR (description), \$ AMOUNT, and SCP AMT (amount spent by that Sub-Control Point) for that quarter. After printing the report, IFCAP will return to the Funds Control Reports Menu.

<span id="_Toc222496847" class="anchor"></span>Figure 47: Sub-Control Point Report Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Would you like the report printed for a full Fiscal Year? YES// (YES)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select STATION NUMBER: 002// ANYTOWN, PA</p>
<p>Select FISCAL YEAR: 94//</p>
<p>Select CONTROL POINT: 022 IFVENDOR,THREE//</p>
<p>START WITH SUB-CONTROL POINT: FIRST//</p>
<p>DEVICE: LAT RIGHT MARGIN: 80//</p>
<p>---------</p>
<p>SUB-CONTROL POINT EXPENDITURES - 022 IFVENDOR</p>
<p>JUL 8,1994 22:04 PAGE 1</p>
<p>FY-Q</p>
<p>FIRST LINE</p>
<p>TRANS # TYPE PO/OBL# VENDOR ITEM DESC. $ AMOUNT SCP AMT</p>
<p>-----------------------------------------------------------------------------</p>
<p>94-4</p>
<p>0327 OBL C54141 IFVENDOR1,TWO PROJECTOR 5000.00 -5000.00</p>
<p>0327 ADJ C54277 IFVENDOR2,ONE REAGENT-ST -2962.70 2962.70</p>
<p>0327 CEI 6755.00 6755.00</p>
<p>---------</p>
<p>TOTAL 4717.70</p>
<p>Quarterly Report</p>
<p>Ceiling Report</p>
<p>Audit Transaction List</p>
<p>Sort Group Report</p>
<p>Classification of Request Report</p>
<p>Cost Center Totals</p>
<p>BOC Totals</p>
<p>Sub-Control Point Report</p>
<p>Reconciliation of PO/Sub-CP Dollar Amounts</p>
<p>BOC Detail Totals</p>
<p>FMS Transaction Data</p>
<p>Select Funds Control Reports Menu Option:</p></td>
</tr>
</tbody>
</table>

#### Reconciliation of PO/Sub-CP Dollar Amounts

#### Reconciliation of PO/Sub-CP Dollar Amounts Menu Path

<span id="_Toc222496848" class="anchor"></span>Figure 48: Reconciliation of PO/Sub-CP Dollar Amounts Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enter FCP Adjustment Data</p>
<p>Assign Ceiling to Sub-Control Points</p>
<p>Correct Sub-Control Point Amounts</p>
<p>Recalculate Fund Control Point Balance</p>
<p>Funds Control Reports Menu ...</p>
<p>Select Funds Control Menu Option: Funds Control Reports Menu</p>
<p>Quarterly Report</p>
<p>Ceiling Report</p>
<p>Audit Transaction List</p>
<p>Sort Group Report</p>
<p>Classification of Request Report</p>
<p>Cost Center Totals</p>
<p>BOC Totals</p>
<p>Sub-Control Point Report</p>
<p>Reconciliation of PO/Sub-CP Dollar Amounts</p>
<p>BOC Detail Totals</p>
<p>FMS Transaction Data</p>
<p>Select Funds Control Reports Menu Option: Reconciliation of PO/Sub-CP Dollar Amounts</p></td>
</tr>
</tbody>
</table>

#### Reconciliation of PO/Sub-CP Dollar Amounts Report Parameters

Enter a STATION NUMBER, a FISCAL YEAR, a fiscal QUARTER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

IFCAP will list the reconciliations for the Control Point that you specified and return you to the Funds Control Reports Menu.

<span id="_Toc222496849" class="anchor"></span>Figure 49:. Reconciliation of PO/Sub-CP Dollar Amounts Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select STATION NUMBER: 002 ANYTOWN, PA</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select FISCAL YEAR: 94//</p>
<p>Select QUARTER: 4//</p>
<p>Select CONTROL POINT: 022 IFVENDOR</p>
<p>...OK? Yes// (Yes)</p>
<p>DEVICE: LAT RIGHT MARGIN: 80//</p>
<p>PO/SCP $ RECONCILIATION 22-94-4 JUL 9,1994 08:59 PAGE 1</p>
<p>SEQ # TYPE REQUESTED RECEIVED PO #</p>
<p>VENDOR</p>
<p>COM $ OBL $ ADJ $</p>
<p>SCP $ AMOUNT ITEM DESC</p>
<p>-----------------------------------------------------------------------------</p>
<p>STATUS: Obligated - 1358</p>
<p>0007 ADJ JUL 8,1994 C30032</p>
<p>400.00 400.00</p>
<p>Quarterly Report</p>
<p>Ceiling Report</p>
<p>Audit Transaction List</p>
<p>Sort Group Report</p>
<p>Classification of Request Report</p>
<p>Cost Center Totals</p>
<p>BOC Totals</p>
<p>Sub-Control Point Report</p>
<p>Reconciliation of PO/Sub-CP Dollar Amounts</p>
<p>BOC Detail Totals</p>
<p>FMS Transaction Data</p>
<p>Select Funds Control Reports Menu Option:</p></td>
</tr>
</tbody>
</table>

#### BOC Detail Totals

#### BOC Detail Totals Menu Path

<span id="_Toc222496850" class="anchor"></span>Figure 50: BOC Detail Totals Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enter FCP Adjustment Data</p>
<p>Assign Ceiling to Sub-Control Points</p>
<p>Correct Sub-Control Point Amounts</p>
<p>Recalculate Fund Control Point Balance</p>
<p>Funds Control Reports Menu ...</p>
<p>Select Funds Control Menu Option: Funds Control Reports Menu</p>
<p>Quarterly Report</p>
<p>Ceiling Report</p>
<p>Audit Transaction List</p>
<p>Sort Group Report</p>
<p>Classification of Request Report</p>
<p>Cost Center Totals</p>
<p>BOC Totals</p>
<p>Sub-Control Point Report</p>
<p>Reconciliation of PO/Sub-CP Dollar Amounts</p>
<p>BOC Detail Totals</p>
<p>FMS Transaction Data</p>
<p>Select Funds Control Reports Menu Option: BOC Detail Totals</p></td>
</tr>
</tbody>
</table>

#### BOC Detail Totals Report Parameters and Display

Enter a STATION NUMBER, a FISCAL YEAR, a fiscal QUARTER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

IFCAP will print the *Budget Object Code Detail Totals* report, listing each budget object code by its transactions and transaction cost. IFCAP will provide a total for all budget object codes. After printing the report, IFCAP will return to the Funds Control Reports Menu.

<span id="_Toc222496851" class="anchor"></span>Figure 51: BOC Detail Totals Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select STATION NUMBER: 002// ANYTOWN, PA</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>This report displays item costs from 2237 orders, sorted</p>
<p>by budget object code.</p>
<p>Select FISCAL YEAR: 94//</p>
<p>Select QUARTER: 4//</p>
<p>Select CONTROL POINT: 022 IFVENDOR //</p>
<p>DEVICE: LAT RIGHT MARGIN: 80//</p>
<p>BUDGET OBJECT CODE DETAIL TOTALS JUL 9,1994 09:01 PAGE 1</p>
<p>LINE</p>
<p>ITEM</p>
<p>TRANSACTION NUMBER NUMBER DESCRIPTION</p>
<p>EST. ITEM</p>
<p>QUANTITY (UNIT) COST TOTAL</p>
<p>-----------------------------------------------------------------------------</p>
<p>BOC: 1007 Computer Systems</p>
<p>WER1234 1</p>
<p>1.00 449.00 449.00</p>
<p>----------</p>
<p>SUBTOTAL 449.00</p>
<p>BOC: 1081 Physicians-Full T</p>
<p>002-94-3-101-0002 2 NONE AGAIN</p>
<p>1.00 0.00 0.00</p>
<p>----------</p>
<p>SUBTOTAL 0.00</p>
<p>BOC: 1091 Federal,Summer Em</p>
<p>999-94-4-022-0002 1 LIGHT BULBS</p>
<p>1.00 3.00 3.00</p>
<p>----------</p>
<p>SUBTOTAL 3.00</p>
<p>----------</p>
<p>TOTAL 634844.92</p>
<p>End of report</p>
<p>Quarterly Report</p>
<p>Ceiling Report</p>
<p>Audit Transaction List</p>
<p>Sort Group Report</p>
<p>Classification of Request Report</p>
<p>Cost Center Totals</p>
<p>BOC Totals</p>
<p>Sub-Control Point Report</p>
<p>Reconciliation of PO/Sub-CP Dollar Amounts</p>
<p>BOC Detail Totals</p>
<p>FMS Transaction Data</p>
<p>Select Funds Control Reports Menu Option:</p></td>
</tr>
</tbody>
</table>

#### FMS Transaction Data

#### FMS Transaction Data Menu Path

<span id="_Toc222496852" class="anchor"></span>Figure 52: FMS Transaction Data Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enter FCP Adjustment Data</p>
<p>Assign Ceiling to Sub-Control Points</p>
<p>Correct Sub-Control Point Amounts</p>
<p>Recalculate Fund Control Point Balance</p>
<p>Funds Control Reports Menu ...</p>
<p>Select Funds Control Menu Option: Funds Control Reports Menu</p>
<p>Quarterly Report</p>
<p>Ceiling Report</p>
<p>Audit Transaction List</p>
<p>Sort Group Report</p>
<p>Classification of Request Report</p>
<p>Cost Center Totals</p>
<p>BOC Totals</p>
<p>Sub-Control Point Report</p>
<p>Reconciliation of PO/Sub-CP Dollar Amounts</p>
<p>BOC Detail Totals</p>
<p>FMS Transaction Data</p>
<p>Select Funds Control Reports Menu Option: FMS Transaction Data</p></td>
</tr>
</tbody>
</table>

#### FMS Transaction Data Report Parameters

Enter a STATION NUMBER, a FISCAL YEAR, a fiscal QUARTER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

IFCAP will print the *FMS Transactions Report*, listing each transmission by date, reference number, FMS transmission code, the amount of the transaction, and the balances of the affected Control Point. After printing the report, IFCAP will return to the Funds Control Reports Menu.

<span id="_Toc222496853" class="anchor"></span>Figure 53: FMS Transaction Data Report Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>This report will generate a listing of FMS transactions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>You may create the report for all entries,</p>
<p>or for selected year and/or quarter.</p>
<p>Enter fiscal year in the format '92'.</p>
<p>Select FISCAL YEAR: 95// 94</p>
<p>Select QUARTER: 4// 4</p>
<p>Select CONTROL POINT: 110 Stuff .01 110//</p>
<p>DEVICE: HOME// LAT RIGHT MARGIN: 80//</p>
<p>Control Point Balance - 999-94-4-11 Stuff .01 OCT 12,1994@14:29:13 PAGE 1</p>
<p>FMS Transactions</p>
<p>TRANSMISSION TRANS TRANSACTION UNOBLIG</p>
<p>DATE REFERENCE # CODE $ AMOUNT CP BALANCE BALANCE</p>
<p>=============================================================================</p>
<p>SEP 16,1994 438LG2000 SO 12.50 -25.00 -25.00</p>
<p>FMS transaction total for this quarter: $12.50</p>
<p>=============================================================================</p>
<p>End of report</p>
<p>Quarterly Report</p>
<p>Ceiling Report</p>
<p>Audit Transaction List</p>
<p>Sort Group Report</p>
<p>Classification of Request Report</p>
<p>Cost Center Totals</p>
<p>BOC Totals</p>
<p>Sub-Control Point Report</p>
<p>Reconciliation of PO/Sub-CP Dollar Amounts</p>
<p>BOC Detail Totals</p>
<p>FMS Transaction Data</p>
<p>Select Funds Control Reports Menu Option:</p></td>
</tr>
</tbody>
</table>

### Correct Sub-Control Point Amounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Correct Sub-Control Point Amounts Parameters

Enter a STATION NUMBER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

<span id="_Toc222496854" class="anchor"></span>Figure 54:. Correct Sub-Control Point Amounts Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>From the Control Point Official’s Menu, select option: Funds Control Menu</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enter FCP Adjustment Data</p>
<p>Assign Ceiling to Sub-Control Points</p>
<p>Correct Sub-Control Point Amounts</p>
<p>Recalculate Fund Control Point Balance</p>
<p>Funds Control Reports Menu ...</p>
<p>Select Funds Control Menu Option: Correct Sub-Control Point Amounts</p>
<p>Select STATION NUMBER: 999// ANYCITY,ANYSTATE</p>
<p>Select CONTROL POINT: 121 LAB TESTING 121// ???</p>
<p>CHOOSE FROM:</p>
<p>22 022 IFVENDOR,THREE</p>
<p>40 040 BUILDING MANAGEMENT</p>
<p>73 073 ENGINEERING</p>
<p>112 112 SURGICAL SERVICE</p>
<p>114 114 RADIOLOGY SERVICE</p>
<p>121 121 LAB TESTING 121</p>
<p>170 170 REHAB. MEDICINE</p>
<p>7001 7001 SUPPLY FUND</p>
<p>Select CONTROL POINT: 121 LAB TESTING 121// 022 IFVENDOR,THREE</p></td>
</tr>
</tbody>
</table>

#### Select Transaction Number

Enter a TRANSACTION NUMBER and a CONTROL POINT at the appropriate prompts. If you do not know the Transaction Number, enter three question marks (???) at the prompt and IFCAP will display the available transactions.

Enter additional SUB-CONTROL POINT to the Control Point if you like. Enter a caret (^) at the Select STATION NUMBER: prompt to return to the Funds Control Menu.

<span id="_Toc222496855" class="anchor"></span>Figure 55: Correct Sub-Control Point Amounts (Select Transaction Number)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select TRANSACTION NUMBER: ???</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Attempting lookup in transaction file.</p>
<p>Attempting lookup using 999-94-4-022 (STA # - FY - QTR - FCP)</p>
<p>1 999-94-4-022-0002 OBL IFVENDOR,TWO LIGHT BULBS</p>
<p>2 999-94-4-022-0003 OBL IFVENDOR,ONE</p>
<p>3 999-94-4-022-0004 OBL WAREHOUSE</p>
<p>4 999-94-4-022-0005 OBL</p>
<p>5 999-94-4-022-0006 OBL</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: 1</p>
<p>TRANSACTION BEG BAL: 3.00</p>
<p>Select SUB-CONTROL POINT: ???</p>
<p>This is an additional sub-control point. IFCAP</p>
<p>allows more than one sub-control point on each transaction</p>
<p>to get a quantity discount.</p>
<p>This is the name of the sub-control point.</p>
<p>Select SUB-CONTROL POINT: Reserve</p>
<p>ARE YOU ADDING 'Reserve' AS A NEW SUB-CONTROL POINT? No//Y (Yes)</p>
<p>ARE YOU ADDING 'Reserve' AS A NEW SUB-CONTROL POINT (THE 1ST FOR THIS CONTROL</p>
<p>POINT ACTIVITY)? Y</p>
<p>(Yes)</p>
<p>$ AMOUNT: 2 RUNNING TOTAL: 2.00 BAL: 1.00</p>
<p>Select SUB-CONTROL POINT:</p>
<p>Select STATION NUMBER: ^</p>
<p>Enter FCP Adjustment Data</p>
<p>Assign Ceiling to Sub-Control Points</p>
<p>Correct Sub-Control Point Amounts</p>
<p>Recalculate Fund Control Point Balance</p>
<p>Funds Control Reports Menu ...</p>
<p>Select Funds Control Menu Option:</p></td>
</tr>
</tbody>
</table>

## Options in the Status of Requests Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Print/Display Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Print/Display Request Form Menu Path

<span id="_Toc222496856" class="anchor"></span>Figure 56: Print/Display Request Form Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>From the Control Point Official’s Menu, select option: Status of Requests Reports Menu</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Print/Display Request Form</p>
<p>Status of All Obligation Transactions</p>
<p>Requests Ready for Approval List</p>
<p>PO with Associated Transactions</p>
<p>Select Status of Requests Reports Menu Option: Print/Display Request Form</p></td>
</tr>
</tbody>
</table>

#### Print/Display Request Form Setup Parameters

Enter a CONTROL POINT. If you do not know the Control Point, enter three question marks (???) and IFCAP will list the available Control Points.

Enter a TRANSACTION NUMBER. If you do not know the transaction number, enter three question marks (???) at the prompt and IFCAP will display the available transactions.

<span id="_Toc222496857" class="anchor"></span>Figure 57: Print/Display Request Form Setup Parameters

Select STATION NUMBER: 900//

Select CONTROL POINT: 300 TUITION RESERVE ACCT// 0160A1 10 0100 010024243

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: A2

1 A20004 900-12-4-300-0017 OBL COMPANY HEALTHCARE A20004

RESERVOIR, DRUG,250ML

Accepted by eCMS

2 A22002 900-12-4-300-0021 OBL BURROWS COMPANY A22002

CATH, URETH, NELATON,12FR

CHOOSE 1-2: 1 900-12-4-300-0017 OBL COMPANY HEALTHCARE A20004

RESERVOIR, DRUG,250ML

Accepted by eCMS

Print administrative certification page of 2237? Yes// N (No)

DEVICE: HOME// DECWINDOWS

<span id="PRC_158_B" class="anchor"></span>Print/Display Request Form Display

IFCAP will list every request for the Control Point you select. Type a caret (^) at the Select STATION NUMBER: prompt to return to the Status of Requests Reports Menu.

<span id="_Toc222496858" class="anchor"></span>Figure 58: Print/Display Request Form Setup Parameters

PRIORITY: STANDARD Accepted by eCMS

SEP 18, 2012@16:42:42 900-12-4-300-0017

-------------------------------------------------------------------------------

REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES

-------------------------------------------------------------------------------

TO: A&MM Officer Requesting Office

FISCAL/ACCOUNTING (04)

-------------------------------------------------------------------------------

Action Requested Date Prepared Date Required

Delivery AUG 30, 2012, SEP 11, 2012

-------------------------------------------------------------------------------

ITEM NO. DESCRIPTION QUANTITY UNIT ESTIMATED

OR STOCK NO. UNIT COST

-------------------------------------------------------------------------------

21250000 1 ITEM ID NO. 13686 250ML DRUG

RESERVOIR 10/CS

PKG: 10 per CS 2 CS 68.0000

eCMS Item Line ID 110496

G3449 2 GOGGLES, SUNSHADES, PLASTIC 16 EA 12.5600

eCMS Item Line ID 110497

SDJ3 3 HAIR PINS, PLASTIC, LONG 24 PG 18.4000

eCMS Item Line ID 110498

4 SOCKS, WHITE, COTTON, NO-SEAM, CREW

LENGTH 36 PR 19.3400

eCMS Item Line ID 110499

TOTAL COST: \$1474.80

-------------------------------------------------------------------------------

VENDOR INFORMATION: NO: 6399

VENDOR: HEFTY HEALTHCARE CONTACT: MISS HELPFUL EXT 221

C/O MY MEDSYSTEM DIVISION PHONE: 800-008-1234

24 EAST STREET ACCT. \#: 1234

ANYTOWN, PA 99999

-------------------------------------------------------------------------------

Ref. Voucher Number:

SPECIAL REMARKS: NEED THIS VERY SOON!

DELIVER TO: WHSE 5

-------------------------------------------------------------------------------

Press ‘return’ to continue, up arrow (^) to exit:

900-12-4-300-0017

-------------------------------------------------------------------------------

REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES

-------------------------------------------------------------------------------

JUSTIFICATION OF NEED OR TURN-IN

THESE ARE NEEDED FOR NURSING HOME ITEMS ARE REQUIRED FOR DIABETIC CARE

-------------------------------------------------------------------------------

Originator of Request: IFCAPUSER, THREE

Signature of Initiator Signature of Approving Official Date

/ES/ONE IFCAPUSER DTN

TWO IFCAPUSER DTN ONE IFCAPUSER DTN

USER’S ALIAS 3 AUG 31, 2012

-------------------------------------------------------------------------------

Appropriation and Accounting Symbols

900-3620160-300-824200-2660-A20004 010024243

-------------------------------------------------------------------------------

900-12-4-300-0017

REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES

MULTIPLE DELIVERY DISTRIBUTION LIST PAGE: 1

ITEM PR# DESCRIPTION QTY DATE QTY SCP LOCATION

1 13686 RESERVOIRS, 2

09-25-12 1 \*\*NONE\*\* CPC12

10-03-12 1 \*\*NONE\*\* CPC14

Press ‘return’ to continue:

Enter information for another report or an up arrow to return to the menu.

### Status of All Obligation Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Status of All Obligation Transactions Menu Path

<span id="_Toc222496859" class="anchor"></span>Figure 59: Status of All Obligation Transactions Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>From the Control Point Official’s Menu, select option: Status of Requests Reports Menu</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Print/Display Request Form</p>
<p>Status of All Obligation Transactions</p>
<p>Requests Ready for Approval List</p>
<p>PO with Associated Transactions</p>
<p>Select Status of Requests Reports Menu Option: Status of All Obligation Transactions</p></td>
</tr>
</tbody>
</table>

#### Status of All Obligation Transactions Setup Parameters

Enter a STATION NUMBER, a FISCAL YEAR, a fiscal QUARTER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

<span id="_Toc222496860" class="anchor"></span>Figure 60: Status of All Obligation Transactions Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select STATION NUMBER: 442// CHEYENNE, WY</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select FISCAL YEAR: 12//</p>
<p>Select QUARTER: 4//</p>
<p>Select CONTROL POINT: 300 ALL OTHER ITEMS //</p>
<p>...OK? Yes// (Yes)</p>
<p>DEVICE: LAT RIGHT MARGIN: 80//</p></td>
</tr>
</tbody>
</table>

#### Status of All Obligation Transactions Display

IFCAP will list each transaction number, the vendor assigned to the transaction, and the description that the requestor entered for the item. Type a caret (^) at the Select STATION NUMBER: prompt to return to the Status of Requests Reports Menu.

<span id="_Toc222496861" class="anchor"></span>Figure 61: Status of All Obligation Transactions Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>STATUS OF OBLIGATION TRANSACTIONS CP: 300 ALL OTHER ITEMS FY: 12</p>
<p>SEP 18,2012 17:03 PAGE 2</p>
<p>PRIORITY DATE</p>
<p>OF DATE DATE DATE RECEIVED</p>
<p>TRANS # REQUEST SIGNED REQUIRED DELIVERED BY SVC</p>
<p>VENDOR STATUS</p>
<p>OBLIGATION# SORT GROUP</p>
<p>FIRST LINE-ITEM DESCRIPTION</p>
<p>COMMENTS</p>
<p>-----------------------------------------------------------------------------</p>
<p>12-4-0015 STANDARD 08/30/12 09/10/12</p>
<p>COMPANY FOODS, INC. Sent to eCMS (P&amp;C)</p>
<p>CHEESE, PARMESAN, GRATED, IND PKG,1/</p>
<p>12-4-0016 09/11/12</p>
<p>12-4-0017 STANDARD 08/31/12 09/11/12 09/17/12</p>
<p>COMPANY HEALTHCARE Ordered and Obligated</p>
<p>A20004 RESERVOIR, DRUG,250ML</p>
<p>-----------------------------------------------------------------------------</p>
<p>Select STATION NUMBER: 442// ^</p>
<p>Print/Display Request Form</p>
<p>Status of All Obligation Transactions</p>
<p>Requests Ready for Approval List</p>
<p>PO with Associated Transactions</p>
<p>Select Status of Requests Reports Menu Option:</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>

### PO with Associated Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PO with Associated Transactions Menu Path

<span id="_Toc222496862" class="anchor"></span>Figure 62: PO with Associated Transactions Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>From the Control Point Official’s Menu, select option: Status of Requests Reports Menu</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Print/Display Request Form</p>
<p>Status of All Obligation Transactions</p>
<p>Requests Ready for Approval List</p>
<p>PO with Associated Transactions</p>
<p>Select Status of Requests Reports Menu Option: PO with Associated Transactions</p></td>
</tr>
</tbody>
</table>

#### PO with Associated Transaction Setup Parameters

Enter a STATION NUMBER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

At the Select PURCHASE ORDER/OBLIGATION NO: prompt, enter the purchase order number or obligation number of the 1358 you wish to decrease or increase. The obligation number is the number that Fiscal Service assigns to the 1358 form. If you do not know the number, enter three question marks (???) and IFCAP will list the available purchase orders and obligations.

At the Would you like to include 'Comments'? prompt, choose whether you want the comments for each purchase order and obligation to appear in the report.

<span id="_Toc222496863" class="anchor"></span>Figure 63: PO with Associated Transactions Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select STATION NUMBER: 999// ANYCITY,ANYSTATE</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select CONTROL POINT: 040 BUILDING MANAGEMENT//</p>
<p>Select PURCHASE ORDER/OBLIGATION NO: ???</p>
<p>Attempting lookup in transaction file.</p>
<p>Attempting lookup using 040 BUILDING MANAGEMENT (CONTROL POINT)</p>
<p>1 040 BUILDING MANAGEMENT 002-93-2-040-0009 OBL C30092</p>
<p>2 040 BUILDING MANAGEMENT 002-93-2-040-0006 OBL C30065</p>
<p>3 040 BUILDING MANAGEMENT 002-93-2-040-0005 OBL C30064</p>
<p>4 040 BUILDING MANAGEMENT 002-93-2-040-0004 OBL C30063</p>
<p>5 040 BUILDING MANAGEMENT 002-93-2-040-0003 OBL C30062</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: 1 002-93-2-040-0009 OBL C30092</p>
<p>Select Status of Requests Reports Menu Option: PO with Associated Transactions</p>
<p>Select STATION NUMBER: 900//</p>
<p>Select CONTROL POINT: 3832 B-127 RENOVATION PFSS// 4537 SUPPLY FUND ECMS 4537</p>
<p>B 90 0161 016144100</p>
<p>Select PURCHASE ORDER/OBLIGATION NO: G2</p>
<p>1 G25000 900-12-4-4537-0002 OBL MEDLINE INDUSTRIES, G25000</p>
<p>STOCKING-ANTI-EMBOLISM-KNEE-MED</p>
<p>Accepted by eCMS</p>
<p>2 G26001 900-12-4-4537-0003 OBL BURROWS COMPANY G26001</p>
<p>RUBBER MATS FOR ELEVATOR IN WARD 4</p>
<p>CHOOSE 1-2:1</p>
<p>Would you like to include 'Comments'? YES// N (NO)</p>
<p>DEVICE: LAT RIGHT MARGIN: 80//</p></td>
</tr>
</tbody>
</table>

#### PO with Associated Transactions Display

IFCAP will print an *Obligation Status Report*, which lists each purchase order and obligation, its amount, the vendor assigned (if any), and the status of the purchase or obligation. Read 7 to learn more about determining the status of a request.

At the Select STATION NUMBER: prompt, type a caret (^) to return to the Status of Requests Reports Menu.

<span id="_Toc222496864" class="anchor"></span>Figure 64: PO with Associated Transactions Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>OBLIGATION STATUS REPORT JUL 8,1994 17:44 PAGE 1</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TRANSACTION NUMBER TYPE $ AMOUNT VENDOR</p>
<p>STATUS</p>
<p>COMMENTS</p>
<p>-------------------------------------------------------------------------------</p>
<p>PURCHASE ORDER/OBLIGATION NO: G25000</p>
<p>900-12-4-4537-0002 OBLIGATION 1621.83 MEDLINE INDUSTRIES, INC</p>
<p>Ordered (No Fiscal Action Required)</p>
<p>-----------</p>
<p>TOTAL 1621.83</p>
<p>Select CONTROL POINT: 040 BUILDING MANAGEMENT// ^</p>
<p>Print/Display Request Form</p>
<p>Status of All Obligation Transactions</p>
<p>Requests Ready for Approval List</p>
<p>PO with Associated Transactions</p>
<p>Select Status of Requests Reports Menu Option:</p></td>
</tr>
</tbody>
</table>

### Requests Ready for Approval List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Requests Ready for Approval Menu Path

<span id="_Toc222496865" class="anchor"></span>Figure 65: Requests Ready for Approval Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>From the Control Point Official’s Menu, select option: Status of Requests Reports Menu</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Print/Display Request Form</p>
<p>Status of All Obligation Transactions</p>
<p>Requests Ready for Approval List</p>
<p>PO with Associated Transactions</p>
<p>Select Status of Requests Reports Menu Option: Requests Ready for Approval List</p></td>
</tr>
</tbody>
</table>

#### Requests Ready for Approval Parameters and Display

IFCAP will list each permanent request that has not been approved by a Control Point Official, its transaction number, form type, vendor (if there is one) and description. Type a caret (^) at the “Select CONTROL POINT:” prompt to return to the Control Point Official’s Menu.

<span id="_Toc222496866" class="anchor"></span>Figure 66: Requests Ready for Approval Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select CONTROL POINT: 101 LAB TESTING 101</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>...OK? Yes// (Yes)</p>
<p>DEVICE: LAT RIGHT MARGIN: 80//</p>
<p>REQUESTS TO BE APPROVED LIST JUL 8,1994 17:49 PAGE 1</p>
<p>TRANSACTION NUMBER TYPE FORM TYPE</p>
<p>REQUESTOR REQUESTED REQUIRED</p>
<p>EST COST</p>
<p>VENDOR FIRST ITEM DESCRIPTION</p>
<p>--------------------------------------------------------------------------------</p>
<p>999-94-4-101-0318 ADJ 1358 ORDER FORM</p>
<p>JUL 7,1994</p>
<p>LONG LASTING TELEPHONE LINES</p>
<p>999-94-3-101-0156 OBL NON-REPETITIVE (2237) ORDER</p>
<p>IFUSER2,THREE APR 18,1994 MAY 8,1994</p>
<p>8000.00</p>
<p>IFVENDOR1,NINE</p>
<p>Press return to continue or uparrow to exit:</p>
<p>Select CONTROL POINT: 101 LAB TESTING 101// ^</p>
<p>Approve Requests</p>
<p>Requests Ready for Approval List</p>
<p>Process a Request Menu ...</p>
<p>Display Control Point Activity Menu ...</p>
<p>Funds Control Menu ...</p>
<p>Status of Requests Reports Menu ...</p>
<p>Record Date Received by Service Menu ...</p>
<p>From the Control Point Official’s Menu, select option:</p></td>
</tr>
</tbody>
</table>

## Options in the Process a Request Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New 2237 (Service) Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New 2237 (Service) Request Setup Parameters

Enter a STATION NUMBER, a FISCAL YEAR, a fiscal QUARTER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

<span id="_Toc222496867" class="anchor"></span>Figure 67: New 2237 (Service) Request Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select STATION NUMBER: 999// ANYCITY, ANYSTATE</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select FISCAL YEAR: 94//</p>
<p>Select QUARTER: 4//</p>
<p>Select CONTROL POINT: 022 IFVENDOR //</p>
<p>...OK? Yes// (Yes)</p></td>
</tr>
</tbody>
</table>

#### Transaction Number Assignment

IFCAP will assign a transaction number to your request. Enter a form type (available types are REPETITIVE; NON-REPETITIVE; REPETITIVE AND NON-REP ORDER; and ISSUE BOOK REQUEST).

At the CLASSIFICATION OF REQUEST: prompt, you may create a classification name for the request if you like or just press \<Enter\> to skip this prompt. The CLASSIFICATION OF REQUEST: prompt allows you to create reports that group requests by categories that *you* define.

<span id="_Toc222496868" class="anchor"></span>Figure 8-68. Transaction Number Assignment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>This transaction is assigned transaction number: 999-94-4-022-0005</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The form types 1358 and NO FORM are no longer used within this option</p>
<p>FORM TYPE: REPETITIVE AND NON-REP ORDER//</p>
<p>CLASSIFICATION OF REQUEST:</p></td>
</tr>
</tbody>
</table>

#### Sort Group Entry

If there’s a Sort Group assigned to the item, enter the sort group at the Sort Group: prompt.

At the DATE OF REQUEST: prompt, press \<Enter\>.

At the REQUESTING SERVICE: prompt, enter the Service that will use the item. If you do not know the name of the service, enter three question marks and IFCAP will list the available Services.

| ![](ifcap-version-5-1-control-point-official-user-s-guide/043.png) | *<u>NOTE:</u>* This is a required field in IFCAP | ![](ifcap-version-5-1-control-point-official-user-s-guide/044.png)![](ifcap-version-5-1-control-point-official-user-s-guide/045.png) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

At the DATE REQUIRED: prompt, enter the Date that you need the item.

At the PRIORITY OF REQUEST: prompt, enter the priority of the request. Priorities are based on the days remaining before the delivery date requested for the item. The priority categories in IFCAP, ranging from shortest to longest delivery time remaining, are “Emergency,” “Special,” and “Standard.” Different stations assign different time frames to these categories. Check with your Fiscal office to determine the time frames at your station for each category.

At the SPECIAL REMARKS: prompt, explain how the service will use the item, names of other items that would fulfill the same need, and any other information that would help the Purchasing Agent fulfill your request. Purchasing Agents sometimes change orders to fulfill the service’s need faster, find a better item, or change the vendor for a better price. Explaining the use of the item will make these tasks easier to accomplish.

<span id="_Toc222496869" class="anchor"></span>Figure 69: Transaction Number Assignment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SORT GROUP:</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DATE OF REQUEST: TODAY// (JUL 08, 1994)</p>
<p>REQUESTING SERVICE:</p>
<p>DATE REQUIRED: T+15 (JUL 23, 1994)</p>
<p>PRIORITY OF REQUEST: ST// STANDARD</p>
<p>SPECIAL REMARKS:</p>
<p>1&gt;This is where the "Special Remarks" go.</p>
<p>2&gt;</p>
<p>EDIT Option:</p></td>
</tr>
</tbody>
</table>

#### Cost Center and Vendor Assignment

IFCAP will ask you for a COST CENTER: and a vendor. Cost centers allow Fiscal staff to create total expense records for a section or service. If you do not know the name of the vendor, enter two question marks (??) and IFCAP will list the available vendors.

<span id="_Toc222496870" class="anchor"></span>Figure 70: Cost Center and Vendor Assignment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>COST CENTER: ??</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select the appropriate cost center for this request</p>
<p>ANSWER WITH COST CENTER:</p>
<p>844100 Supply</p>
<p>COST CENTER: 844100 Supply</p></td>
</tr>
<tr class="even">
<td><p>VENDOR: ??</p>
<p>Enter the name of the vendor for the items ordered on this request (1 to</p>
<p>36 characters)</p>
<p>ANSWER WITH VENDOR NUMBER, OR SYNONYM, OR FMS VENDOR CODE</p>
<p>DO YOU WANT THE ENTIRE VENDOR LIST? Y (Yes)</p>
<p>CHOOSE FROM:</p>
<p>1 TEAM 3 CLOCKWORKS 800-CALLME1 NO. 1</p>
<p>SPECIAL FACTORS:</p>
<p>ORDERING ADDRESS: 123 ANY POST AVEREET</p>
<p>MYTOWN, PA 99990</p>
<p>2 IFVENDOR,ONE. 800-BANDAGES NO. 2</p>
<p>SPECIAL FACTORS:</p>
<p>ORDERING ADDRESS: 123 ANY STREET</p>
<p>ANYTOWN, MN 99990</p>
<p>3 IFVENDOR,EIGHT 2453 NO. 3</p>
<p>ORDERING ADDRESS: 123 ANY AVE</p>
<p>ANYCITY, NY 99990</p>
<p>For 1358 requests, additional information concerning vendors may be entered</p>
<p>in the Purpose field.</p>
<p>VENDOR: 2 IFVENDOR,ONE. 800-BANDAGES NO. 2</p>
<p>SPECIAL FACTORS:</p>
<p>ORDERING ADDRESS: 123 ANY STREET</p>
<p>ANYTOWN, MN 99990</p>
<p>...OK? Yes// (Yes)</p></td>
</tr>
</tbody>
</table>

#### Enter Item

At the Select LINE ITEM NUMBER: prompt for the first item on the request, enter “1.”

At the Item Master File No.: prompt, enter the item name or number. You can also type three question marks (???) to see a list of the items you can request.

At the DESCRIPTION: prompt, define the item as thoroughly as you can. If the item isn’t in the Item Master File, the Purchasing Agent is going to make a “best guess” about just what kind of item you need, based on the information you provide in this field. Describe what the service plans to do with the item, and any special features of the item (*e.g.*, does it have to be flexible, or blue, or heat-resistant, or non-toxic?).

| ![](ifcap-version-5-1-control-point-official-user-s-guide/046.png) | *<u>NOTE:</u>* The Description field is now a required field | ![](ifcap-version-5-1-control-point-official-user-s-guide/047.png) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

At the BOC: prompt, enter the budget object code classification for this item. If you do not know the BOC, enter three question marks (???) and IFCAP will list the available BOCs.

<span id="_Toc222496871" class="anchor"></span>Figure 71: Cost Center and Vendor Assignment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select LINE ITEM NUMBER: 1</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>LINE ITEM NUMBER: 1//</p>
<p>ITEM MASTER FILE NO.:</p>
<p><strong>NOTE:</strong> Description is now a Required field on all 2237s</p>
<p>DESCRIPTION:</p>
<ol type="1">
<li><p>If you leave this field blank the following prompt appears</p></li>
</ol>
<p>Item DESCRIPTION is required!</p>
<p>DESCRIPTION: (you will be prompted again for a description)</p>
<p>1&gt;DRAPES, LINEN 80 X 102 - 4 PANELS</p>
<p>2&gt;</p>
<p>EDIT Option:</p>
<p>BOC: ???</p>
<p>Major budget object code classifications are:</p>
<p>10 thru 13 - Personal Services and Benefits</p>
<p>21 - Travel and Transportation of Persons</p>
<p>22 - Transportation of Things</p>
<p>23 - Rent, Communications, and Utilities</p>
<p>24 - Printing and Reproduction</p>
<p>25 - Other Services</p>
<p>26 - Supplies and Materials</p>
<p>31 thru 33 - Acquisition of Capital Assets</p>
<p>ANSWER WITH BOC</p>
<p>DO YOU WANT THE ENTIRE 29-ENTRY BOC LIST? Y (Yes)</p>
<p>CHOOSE FROM:</p>
<p>1050 Trainees-Administrative Training Program</p>
<p>1090 Administrative and Clerical Personnel Not Otherwise Classified</p>
<p>1091 Federal,Summer Employment Program for Youth-Summer Aids</p>
<p>1092 Stay-In-School Program Part-Time Employment of Needy Students</p>
<p>1093 Subsistence &amp; Temp Exp, Real Estate Costs &amp; Misc Exp-PL 89-516</p>
<p>1095 Employee Salary Continuation</p>
<p>1098 Wage Rate Employees</p>
<p>2101 Permanent Duty Travel</p>
<p>2102 Round Trip Tvl Between Old and New Sta To Seek Perm Res Quarters</p>
<p>2103 Employee Training Travel</p>
<p>2104 Employee Program Travel</p>
<p>2121 Local Transportation of Employees</p>
<p>2220 Other Shipments</p>
<p>2230 Shipment of Household Goods &amp; Personal Effects</p>
<p>2330 Real Property Rentals</p>
<p>2341 Equipment Rental</p>
<p>2350 Motion-Picture Film Rentals</p>
<p>2423 Forms and Form Letters</p>
<p>2424 Other Printing and Reproduction</p>
<p>2520 Repair of Furniture and Equipment</p>
<p>2530 Storage of Household Goods</p>
<p>BOC: 2220 Other Shipments</p></td>
</tr>
</tbody>
</table>

#### Enter Quantity, Unit of Purchase, and Identifying Numbers

At the QUANTITY: prompt, enter the number of units that you want, based on how the vendor sells the item. For example, if the vendor sells units by the case, and you want 4 cases, you will enter 4 at the QUANTITY: prompt.

Enter the UNIT OF PURCHASE. If the vendor sells units by the case, you will enter CS for case at this prompt. If you don’t know the correct abbreviation for the unit of purchase, enter two question marks (??) at the prompt and IFCAP will list the abbreviations.

At the STOCK NUMBER: prompt, enter the stock number of the item.

At the INTERMEDIATE PRODUCT CODE: prompt, enter the Intermediate Product Code if there is one. The Intermediate Product Code is a stock number that vendors sometimes use.

<span id="_Toc222496872" class="anchor"></span>Figure 72: Enter Quantity, Unit of Purchase, and Identifying Numbers

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>QUANTITY: 1</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>UNIT OF PURCHASE: CS CASE</p>
<p>STOCK NUMBER: ??</p>
<p>This is the item Federal Supply Service (FSS) Number; or National Stock</p>
<p>Number (NSN); or any other stock number; or the manufacturer model</p>
<p>number.</p>
<p>STOCK NUMBER: 28934750283</p>
<p>EST. ITEM (UNIT) COST: 440/00??</p>
<p>Enter the unit cost for this item (a dollar amount between 0 and 9999999)</p>
<p>or N/C for no charge. Commas are not allowed.</p>
<p>EST. ITEM (UNIT) COST: 440.00</p>
<p>QTY BEG BAL: 1</p></td>
</tr>
</tbody>
</table>

#### Select Delivery Schedules

At the SELECT DELIVERY SCHEDULE: prompt, press \<Enter\> if you want all of the items on your request to be delivered at the same time. If you select a delivery schedule, you are notifying the vendor that you want them to deliver different amounts of the items on different days. For example, if you want to order 100 cases of computer paper, but do not want all of it delivered at once, you can “stagger” the delivery by entering 1 at the SELECT DELIVERY SCHEDULE: prompt. Enter a date and the amount you would like to be delivered on that date, enter 2 at the next SELECT DELIVERY SCHEDULE: prompt and enter a date and the amount you would like to be delivered on that date, etc. Make sure that the total number of items among all of the delivery dates equals the total number of items you are ordering.

At the COMMITTED (ESTIMATED) COST: prompt, enter the total cost (in dollars) for the item.

At the SELECT SUB-CONTROL POINT: prompt, you can associate this purchase with a category of purchases that you can define. This allows you to group similar purchases together.

At the DELIVER TO/LOCATION: prompt, enter where you want the warehouse to deliver the item, including room and building number if you can. At the JUSTIFICATION: prompt, explain why the service or item is needed by the service. Enter the name of the individual printed on the request form as the initiator of the request at the REQUESTOR: prompt. Enter your name at the ORIGINATOR OF REQUEST: prompt. Add comments if you like.

<span id="_Toc222496873" class="anchor"></span>Figure 73: Enter Quantity

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select DELIVERY SCHEDULE:</strong></th>
<th><strong>See explanatory text above for choices</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>Select LINE ITEM NUMBER:</p>
<p>COMMITTED (ESTIMATED) COST: 440//</p>
<p>TRANSACTION BEG BAL: 440.00</p>
<p>Select SUB-CONTROL POINT:</p>
<p>DELIVER TO/LOCATION:</p>
<p>JUSTIFICATION:</p>
<p>1&gt;This is where the "Justification" goes.</p>
<p>2&gt;</p>
<p>EDIT Option:</p>
<p>REQUESTOR: IFUSER2,THREE</p>
<p>ORIGINATOR OF REQUEST: IFUSER</p>
<p>COMMENTS:</p>
<p>1&gt;This is where the "Comments" go.</p>
<p>2&gt;</p>
<p>EDIT Option:</p></td>
</tr>
</tbody>
</table>

#### Review Request

IFCAP will ask you if you would like to review the request. IFCAP will display the Control Point balance, your estimate of the cost of the request, and the total uncommitted balance for the Control Point. IFCAP will allow you to transmit the request for approval by the Control Point Official. You can enter another request, or press \<Enter\> at the Would You Like To Enter Another Request? prompt to return to the Process a Request Menu.

<span id="_Toc222496874" class="anchor"></span>Figure 74: Review Request

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Would you like to review this request? NO// (No)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Current Control Point balance: $0.00</p>
<p>Estimated cost of this request: $440.00</p>
<p>NOTE: You will not be prompted to set the 2237 Approval Flag to YES, if there is a Required field that is not populated.</p>
<p>Is this request ready for approval? YES// Y (Yes)</p>
<p>Is this request ready for transmission to A&amp;MM/Fiscal? No// N (No)</p>
<p>Would you like to enter another request? YES// N (No)</p>
<p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Select Process a Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### Edit a 2237 (Service)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Edit a 2237 Setup Parameters

Enter a STATION NUMBER and a CONTROL POINT at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points.

<span id="_Toc222496875" class="anchor"></span>Figure 75: Edit a 2237 Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select STATION NUMBER: 999 ANYCITY,ANYSTATE</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select CONTROL POINT: 101 ??</p>
<p>Select CONTROL POINT: ??</p>
<p>CHOOSE FROM:</p>
<p>22 022 IFVENDOR,THREE</p>
<p>40 040 BUILDING MANAGEMENT</p>
<p>73 073 ENGINEERING</p>
<p>112 112 SURGICAL SERVICE</p>
<p>114 114 RADIOLOGY SERVICE</p>
<p>121 121 LAB TESTING 121</p>
<p>170 170 REHAB. MEDICINE</p>
<p>7001 7001 SUPPLY FUND</p>
<p>Select CONTROL POINT: 022 IFVENDOR,THREE</p></td>
</tr>
</tbody>
</table>

#### Enter Transaction Number

At the Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: prompt, enter a transaction number. If you do not know the transaction number, enter three question marks (???) at the prompt and IFCAP will list the available transactions.

<span id="_Toc222496876" class="anchor"></span>Figure 76: Edit a 2237 (Enter Transaction Number)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ???</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Attempting lookup in transaction file.</p>
<p>Attempting lookup using 022 IFVENDOR (CONTROL POINT)</p>
<p>1 022 IFVENDOR,THREE 999-94-4-022-0007 OBL IFVENDOR,ONE</p>
<p>This is where the "Description" goes.</p>
<p>2 022 IFVENDOR 999-94-4-022-0006 OBL</p>
<p>3 022 IFVENDOR 999-94-4-022-0005 OBL</p>
<p>4 022 IFVENDOR 999-94-4-022-0004 OBL IFVENDOR,EIGHT</p>
<p>5 022 IFVENDOR 999-94-4-022-0003</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: 5 999-94-4-022-0003</p></td>
</tr>
</tbody>
</table>

#### Enter Classification of Request and Sort Group

At the CLASSIFICATION OF REQUEST: prompt, you may create a classification name for the request if you like or just press \<Enter\> to skip this prompt. The CLASSIFICATION OF REQUEST: prompt allows you to create reports that group requests by categories that *you* define.

If there’s a Sort Group assigned to the item, enter it at the SORT GROUP: prompt. IFCAP will ask you for a cost center and a vendor. Cost center numbers are listed in the left column of MP-4 Part V, Appendix B-1. Cost centers allow Fiscal staff to create total expense records for a section or service. If you do not know the name of the vendor, enter two question marks (??) and IFCAP will list the available vendors.

<span id="_Toc222496877" class="anchor"></span>Figure 77: Enter Classification of Request and Sort Group

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>The form type for this transaction is REPETITIVE AND NON-REP ORDER</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CLASSIFICATION OF REQUEST:</p>
<p>SORT GROUP:</p>
<p>DATE OF REQUEST: JUL 08, 1994//</p>
<p>REQUESTING SERVICE:</p>
<p>DATE REQUIRED: JUL 23, 1994//</p>
<p>PRIORITY OF REQUEST: STANDARD//</p>
<p>SPECIAL REMARKS:</p>
<p>1&gt;This is where the "Special Remarks" go.</p>
<p>2&gt;</p>
<p>EDIT Option:</p>
<p>COST CENTER: 844100 Supply// VENDOR: IFVENDOR,ONE. Replace</p></td>
</tr>
</tbody>
</table>

#### Enter Cost

At the COMMITTED (ESTIMATED) COST: prompt, enter the total cost (in dollars) for the item.

At the Select SUB-CONTROL POINT: prompt, you can associate this purchase with a category of purchases that you can define. This allows you to group similar purchases together.

You can change the DATE COMMITTED, add COMMENTS if you like, change the EST. ITEM (UNIT) COST, cost of the item and the date obligated, and change the Purchase Order number.

At the DELIVER TO/LOCATION: prompt, enter where you want the warehouse to deliver the item, including room and building number if you can.

At the JUSTIFICATION: prompt, explain why the service or item is needed by the service. Add COMMENTS if you like.

<span id="_Toc222496878" class="anchor"></span>Figure 78: Enter Cost

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select LINE ITEM NUMBER: 1//</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>LINE ITEM NUMBER: 1//</p>
<p>ITEM MASTER FILE NO.:</p>
<p>DESCRIPTION:</p>
<p>1&gt;</p>
<p>EDIT Option:</p>
<p>BOC: 2220 Other Shipments//</p>
<p>QUANTITY: 1//</p>
<p>UNIT OF PURCHASE: CS//</p>
<p>STOCK NUMBER: 28934750283//</p>
<p>EST. ITEM (UNIT) COST: 440.00//</p>
<p>QTY BEG BAL: 1</p>
<p>Select DELIVERY SCHEDULE:</p>
<p>Select LINE ITEM NUMBER:</p>
<p>COMMITTED (ESTIMATED) COST: 42 $ 42.00</p>
<p>DATE COMMITTED: JUL 8,1994// (JUL 08, 1994)</p>
<p>TRANSACTION BEG BAL: 42.00</p>
<p>Select SUB-CONTROL POINT:</p>
<p>DELIVER TO/LOCATION:</p>
<p>JUSTIFICATION:</p>
<p>1&gt;This is where the "Justification" goes.</p>
<p>2&gt;</p>
<p>EDIT Option:</p>
<p>REQUESTOR: IFUSER2,THREE</p>
<p>ORIGINATOR OF REQUEST: IFUSER</p>
<p>COMMENTS:</p>
<p>1&gt;</p></td>
</tr>
</tbody>
</table>

You may enter a new estimated delivery date. If the service has received the item, you can enter the date it was received at the Date Received: prompt. At the Select Sub-Control Point: prompt, you can associate this purchase with a category of purchases that you can define. This allows you to group similar purchases together. Add COMMENTS if you like. IFCAP will list the current Control Point balance, the estimated cost (incorporating any change you just made), and the total uncommitted balance from current and prior quarters for that Control Point. IFCAP will allow you to forward the request to the Control Point Official. You can either edit another request, or press \<Enter\> to return to the Process a Request Menu.

<span id="_Toc222496879" class="anchor"></span>Figure 79: Forward Request for Approval

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Would you like to review this request? No// (No)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Current Control Point balance: $0.00</p>
<p>Estimated cost of this request: $42.00</p>
<p>Is this request ready for approval? Yes// (Yes)</p>
<p>Is this request ready for transmission to A&amp;MM/Fiscal? No// (No)</p>
<p>Would you like to edit another request? Yes// N (No)</p>
<p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Select Process a Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### Print/Display Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Use this option to print or display a 2237 or a temporary request.

#### Select Transaction 

At the Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: prompt, enter the temporary transaction number assigned to the request. If you don’t know the number, enter two questions marks (??) and IFCAP will list the available numbers.

<span id="_Toc222496880" class="anchor"></span>Figure 80: Select Transaction

Select CONTROL POINT: 397 multi yr 0160B1 10 0100 010020132

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ??

Attempting lookup in transaction file.

Attempting lookup using 397 (CONTROL POINT)

1 397 multi yr 561-13-1-397-0002 OBL ANYCOMPANY CONTRACT IT C30000

REPAIR OF ALL WATER FOUNTAINS IN THE MAIN BUILDING.

2 397 multi yr 561-13-1-397-0001 OBL EXAMPLE HEALTH (\$250 A30000

CONTAINER, SHARPS, BIOHAZARD, HORIZ DROP OPENING,2GAL, RED

Accepted by eCMS

3 397 multi yr 561-12-4-397-0003 OBL GREAT STUFF FOR ALL

BALLOONS, WEATHER, HIGH-ALTITUDE

Accepted by eCMS

4 397 multi yr 561-12-4-397-0002 OBL AMSCO

CHOOSE 1-4: 2

#### Print Last Page

At the Print administrative certification page of 2237? prompt, enter Yes if you want to see who has approved the request for purchase (the “Administrative Action” column) or who has certified receipt of the purchase (the “Receipt Action” column). Otherwise, enter No at this prompt.

<span id="_Toc222496881" class="anchor"></span>Figure 81: Print Last Page

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Print administrative certification page of 2237? Yes// (Yes)</strong></p>
<p><strong>DEVICE: HOME// LAT RIGHT MARGIN: 80//</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Interpreting the Request Form

The request form lists the information you provided in the Enter/Edit a Request options in a style that replicates a printed VA 2237 form. The form lists each item with description and unit cost, and a total cost for the request. It also lists where the item(s) should be delivered. If you printed the last page of the 2237, the form would list signature and date columns for officers and clerks to sign at various stages of approval and receipt. Enter another transaction at the Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: prompt, or press \<Enter\> to return to the Requestor’s Menu.

<span id="_Toc222496882" class="anchor"></span>Figure 82: Interpreting the Request Form

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>PRIORITY: STANDARD</strong></p>
<p><strong>JUN 29,1994@14:55:47 WER1234</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>TO: A&amp;MM Officer Requesting Office</strong></p>
<p><strong>SUPPLY (90)</strong></p>
<p><strong>----------------------- -----------------------------------------------------</strong></p>
<p><strong>Action Requested Date Prepared Date Required</strong></p>
<p><strong>Delivery JUN 29,1994 JUL 1,1994</strong></p>
<p><strong>----------------------- --------------------- -------------------------------</strong></p>
<p><strong>ITEM NO. DESCRIPTION QUANTITY UNIT ESTIMATED</strong></p>
<p><strong>OR STOCK NO. UNIT COST</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>BR-549 *NO DESCRIPTION* 1 449.0000</strong></p>
<p><strong>2 CELERY-FRESH-STALK LB 1.0000</strong></p>
<p><strong>TOTAL COST: $449.00</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>WER1234</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>VENDOR INFORMATION:</strong></p>
<p><strong>VENDOR: IFVENDOR1,TEN CONTACT: IFVENDOR,TEN</strong></p>
<p><strong>123 ANY POST AVEREET PHONE: 800-555-5555</strong></p>
<p><strong>MYTOWN,PA 99990</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>Ref. Voucher Number:</strong></p>
<p><strong>DELIVER TO: Bldg. 1, Office of the Bursar</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>JUSTIFICATION OF NEED OR TURN-IN</strong></p>
<p><strong>I need it!</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>Signature of Initiator Signature of Approving Official Date</strong></p>
<p><strong>IFUSER3,SIX</strong></p>
<p><strong>------------------------------------ ----------------------------------------</strong></p>
<p><strong>WER1234</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>Appropriation and Accounting Symbols</strong></p>
<p><strong>002-3640160.001.01-112-802700-0</strong></p>
<p><strong>-----------------------------------------------------------------------------</strong></p>
<p><strong>Press return to continue:</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enter information for another report or an uparrow to return to the menu.</p>
<p>Select CONTROL POINT: 022 IFVENDOR,THREE// ^</p></td>
</tr>
</tbody>
</table>

### Change Existing Transaction Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to correct the fiscal year or fiscal quarter of the 2237 form or change a temporary transaction number into a permanent transaction number. If you change a permanent transaction number, <u>this option automatically cancels the old transaction number.</u>

| ![](ifcap-version-5-1-control-point-official-user-s-guide/048.png) | *<u>NOTE:</u>* If you change the transaction number of a <u>2237 containing eCMS identifiers</u>, you must manually notify the eCMS Contracting Officer of the cancellation of the original 2237# and provide the newly assigned 2237#. This will enable the Contracting Officer to mark the original 2237 as Cancelled in eCMS and to associate the new 2237 transaction with any existing Plan/Award documentation upon its Approval and subsequent transmission to eCMS. | ![](ifcap-version-5-1-control-point-official-user-s-guide/049.png) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

#### Setup Parameters

Enter a CONTROL POINT and the TRANSACTION NUMBER you wish to change. If you do not know the transaction number, enter three question marks (???) at the Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: prompt and IFCAP will list the available transactions.

<span id="_Toc222496883" class="anchor"></span>Figure 83: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select Process a Request Menu Option: Change Existing Transaction Number</strong></p>
<p><strong>Select CONTROL POINT: 022 IFVENDOR,THREE</strong></p>
<p><strong>Select the existing transaction number to be replaced</strong></p>
<p><strong>Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ???</strong></p>
<p><strong>Attempting lookup in transaction file.</strong></p>
<p><strong>Attempting lookup using 022 IFVENDOR,THREE (CONTROL POINT)</strong></p>
<p><strong>1 022 IFVENDOR 999-94-4-022-0008 OBL IFVENDOR,TWO</strong></p>
<p><strong>2 022 IFVENDOR 999-94-4-022-0007 OBL IFVENDOR,ONE</strong></p>
<p><strong>This is where the "Description" goes.</strong></p>
<p><strong>3 022 IFVENDOR 999-94-4-022-0006 OBL</strong></p>
<p><strong>4 022 IFVENDOR 999-94-4-022-0005 OBL</strong></p>
<p><strong>5 022 IFVENDOR 999-94-4-022-0004 OBL IFVENDOR,EIGHT</strong></p>
<p><strong>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CHOOSE 1-5: 2 999-94-4-022-0007 OBL IFVENDOR,ONE</td>
</tr>
</tbody>
</table>

#### Edit Data 

IFCAP will let you review the request and change the Station number, fiscal year, fiscal quarter, and Control Point. IFCAP will create a duplicate 2237 with a new transaction number - Cancel the original 2237 transaction - and give you the chance to edit the new 2237 request. If there are Required fields that are not populated – you will be prompted to enter the required data. You will be shown the current Control Point balance, the estimated cost of the request, and the total uncommitted balance from current and prior quarters. If any of the Required fields are not populated, IFCAP will not ask if the 2237 is Ready for Approval. You can change to another transaction number by answering Yes at the Would you like to replace another transaction number? prompt, or press \<Enter\> to return to the Process a Request Menu.

<span id="_Toc222496884" class="anchor"></span>Figure 84: Edit Data

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 999//</p>
<p>Select FISCAL YEAR: 13// 14</p>
<p>Select QUARTER: 4// 1</p>
<p>Select CONTROL POINT: 110 SUPPLIES .01// 0160A1 10 0100 010042116</p>
<p>0160A1 10 0100 010042116</p>
<p>Old transaction 999-13-4-110-0076 is now cancelled.</p>
<p>NOTE: The original transaction is cancelled, and the new transaction is checked to ensure that all Required fields are populated.</p>
<p>Transaction '999-13-4-110-0076' has been replaced by 999-14-1-110-0001</p>
<p>WARNING - Transaction ‘999-14-1-110-0001’ is missing required data!</p>
<p>&gt;&gt;&gt; Line Item #1 Description is missing.</p>
<p>The request needs to be edited prior to approval.</p>
<p>The form type for this transaction is REPETITIVE AND NON-REP ORDER</p>
<p>CLASSIFICATION OF REQUEST:</p>
<p>SORT GROUP:</p>
<p>You will be permitted to change the Date of Request, Requesting Service, Date Required, and Priority of Request as appropriate.</p>
<p>DATE OF REQUEST: JUN 3,2013// T AUG 5,2013</p>
<p>REQUESTING SERVICE: DENTAL//</p>
<p>DATE REQUIRED: JUL 1,2013// 100313 OCT 3,2013</p>
<p>PRIORITY OF REQUEST: STANDARD//</p>
<p>SPECIAL REMARKS:</p>
<p>1&gt;</p>
<p>COST CENTER: 842100 Fiscal</p>
<p>VENDOR: VENDORONE, INC.//</p>
<p>Select LINE-ITEM NUMBER: 2//</p>
<p>LINE-ITEM NUMBER: 2//</p>
<p>ITEM MASTER FILE NO.: 22//</p>
<p>BOC: 2631 Drugs, Medicines and Chem Replace</p>
<p>QUANTITY: 3//</p>
<p>QTY BEG BAL: 3</p>
<p>Select DELIVERY SCHEDULE:</p>
<p>NOTE: Item Description is a REQUIRED field. You will have to enter text for that item.</p>
<p>Select LINE-ITEM NUMBER: 1</p>
<p>LINE-ITEM NUMBER: 1//</p>
<p>ITEM MASTER FILE NO.:</p>
<p>DESCRIPTION:</p>
<p>1&gt;</p>
<p>Item DESCRIPTION is required!</p>
<p>DESCRIPTION:</p>
<p>1&gt;DRAPES, LINEN 80 X 102 - 4 PANELS</p>
<p>2&gt;</p>
<p>EDIT Option:</p>
<p>BOC: 2660 Operating Supplies and Ma Replace</p>
<p>QUANTITY: 3//</p>
<p>UNIT OF PURCHASE: PR// SETS??</p>
<p>Select the appropriate unit of purchase for this item</p>
<p>UNIT OF PURCHASE: PR// SET SE SET</p>
<p>STOCK NUMBER:</p>
<p>EST. ITEM (UNIT) COST: 45.55//</p>
<p>QTY BEG BAL: 3</p>
<p>Select DELIVERY SCHEDULE:</p>
<p>Select LINE-ITEM NUMBER:</p>
<p>COMMITTED (ESTIMATED) COST: 166.5//</p>
<p>TRANSACTION BEG BAL: 166.50</p>
<p>Select SUB-CONTROL POINT:</p>
<p>DELIVER TO/LOCATION: BLDG33, RM12//</p>
<p>JUSTIFICATION:</p>
<p>1&gt;Needed for training sessions with nursing students.</p>
<p>EDIT Option:</p>
<p>REQUESTOR: Smith, John//</p>
<p>ORIGINATOR OF REQUEST:</p>
<p>COMMENTS:</p>
<p>1&gt;</p>
<p>Would you like to review this request? No// (No)</p>
<p>Current Control Point balance: $20606769.49</p>
<p>Estimated cost of this request: $166.50</p>
<p>NOTE: You will not be prompted to set this request to YES if there is a Required field that is not populated.</p>
<p>Is this request ready for approval? Yes//</p>
<p>Would you like to replace another transaction number? No// (No)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
</tbody>
</table>

### Cancel Transaction with Permanent Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Setup Parameters

Enter the STATION NUMBER and the CONTROL POINT number. At the Select TRANSACTION NUMBER: prompt, enter the transaction you want to delete, or enter three question marks (???) to have IFCAP will display the available transactions.

|                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-control-point-official-user-s-guide/050.png)![](ifcap-version-5-1-control-point-official-user-s-guide/051.png) | *<u>NOTE:</u>* When you reject a request, print and mail a copy of the request to the requestor, since rejecting the request removes it from the system. This will save time for the Requestor.                                                                                                                                 | ![](ifcap-version-5-1-control-point-official-user-s-guide/052.png)![](ifcap-version-5-1-control-point-official-user-s-guide/053.png) |
|                                                                                                                                                                                                                                                                                                | *<u>NOTE:</u>* Now that an interface exists between IFCAP and the electronic Contract Management System, do not cancel any 2237 that has been sent to eCMS, as those 2237s are controlled by eCMS. That type of 2237 is easily identified by the text Accepted by eCMS that will appear below the transaction in a display list |                                                                                                                                                                                                                                                                                                    |

<span id="_Toc222496885" class="anchor"></span>Figure 85: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Process a Request Menu Option: Cancel Transaction with Permanent Number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select STATION NUMBER: 999 ANYCITY,ANYSTATE</p>
<p>Select CONTROL POINT: 022 IFVENDOR</p>
<p>Select TRANSACTION NUMBER: ???</p>
<p>Attempting lookup in transaction file.</p>
<p>Attempting lookup using 022 IFVENDOR (CONTROL POINT) Select STATION NUMBER: 999 ANYCITY,ANYSTATE</p>
<p>Select CONTROL POINT: 022 IFVENDOR</p>
<p>Select TRANSACTION NUMBER: ???</p>
<p>Attempting lookup in transaction file.</p>
<p>Attempting lookup using 022 IFVENDOR (CONTROL POINT)</p></td>
</tr>
<tr class="even">
<td><p>::::::</p>
<p>3 022 IFVENDOR 999-12-4-022-0009 OBL IFVENDOR,ONE</p>
<p>BATTERY, ALK, AAA,1.5V, HEAVY DUTY</p>
<p>Accepted by eCMS</p>
<p>4 022 IFVENDOR 999-12-4-022-0006 OBL</p>
<p>CUSHION, CHAIR</p>
<p>5 022 IFVENDOR 999-12-4-022-0005 OBL</p>
<p>HEPARIN 1000U/ML 30 ML</p>
<p>Accepted by eCMS</p></td>
</tr>
<tr class="odd">
<td><p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: 1 999-12-4-022-0006</p></td>
</tr>
</tbody>
</table>

#### Cancel the Transaction

IFCAP will ask you to confirm that you want to cancel the transaction and ask you to enter comments that explain why you have cancelled the transaction. At the Would you like to cancel another transaction?: prompt, answer YES to edit another transaction, or press \<Enter\> to return to the Process a Request Menu.

<span id="_Toc222496886" class="anchor"></span>Figure 86: Cancel the Transaction

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Cancel this transaction? No// Y (Yes)</p>
<p>Enter comments for this cancellation</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>COMMENTS:</p>
<p>1&gt;Transaction no. 999-12-4-022-0006 was cancelled.</p>
<p>EDIT Option: add lines</p>
<p>2&gt;Item no longer needed.</p>
<p>3&gt;</p>
<p>EDIT Option:</p>
<p>Would you like to cancel another transaction? NO// (NO)</p></td>
</tr>
<tr class="even">
<td><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option:</p></td>
</tr>
</tbody>
</table>

| ![](ifcap-version-5-1-control-point-official-user-s-guide/054.png) | *<u>NOTE:</u>* When an IFCAP User cancels 2237, the Name of the User and the Date/Time of the cancellation are now stored in the 2237 record in the Control Point Activity file (#410). | ![](ifcap-version-5-1-control-point-official-user-s-guide/055.png) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

### Options in the Requestor's Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Requestor’s Menu options are described in the IFCAP *Control Point Requestor User’s Guide*, available online at the Vista Document Library (VDL):

<http://www.va.gov/vdl/application.asp?appid=42>.

### Options in the Repetitive Item List Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Repetitive Item List (Enter)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496887" class="anchor"></span>Figure 87: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: Repetitive Item List Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Select Repetitive Item List Menu Option: New Repetitive Item List (Enter)</p></td>
</tr>
</tbody>
</table>

#### Setup Parameters

Enter a STATION NUMBER, a FISCAL YEAR and a FISCAL QUARTER. Enter a CONTROL POINT. If you do not know the name Of the Control Point, enter three question marks (???) at the prompt and IFCAP will list the available Control Points. Enter a COST CENTER. Cost center numbers are listed in the left column of MP-4 Part V, Appendix B-1. Cost centers allow Fiscal staff to create total expense records for a section or service.

<span id="_Toc222496888" class="anchor"></span>Figure 88: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 999 ANYCITY,ANYSTATE</p>
<p>Select FISCAL YEAR: 94//</p>
<p>Select QUARTER: 4//</p>
<p>Select CONTROL POINT: 022 IFVENDOR</p>
<p>...OK? Yes// (Yes)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select COST CENTER: ??</p>
<p>844100 844100 Supply</p></td>
</tr>
<tr class="even">
<td>Select COST CENTER: 844100 Supply</td>
</tr>
</tbody>
</table>

#### Select Item

Enter an item number or name at the Select ITEM: prompt. If you do not know the name or the number of the item, enter three question marks (???) at the prompt and IFCAP will list the available items.

<span id="_Toc222496889" class="anchor"></span>Figure 89: Select Item

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select ITEM: ???</strong></p>
<p><strong>This is a pointer to an item in the Item file, #441. This file is</strong></p>
<p><strong>composed of items specified by Supply Service as being purchased</strong></p>
<p><strong>repetitively. This file maintains a full description of the item,</strong></p>
<p><strong>related stock numbers, vendors, contract numbers, and a procurement</strong></p>
<p><strong>history.</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>1 BANDAGE-CAST-6INX5YD</p>
<p>2 CAP-SAFETY-BOTTLE-50S</p>
<p>3 PLASMA-USP 5%</p>
<p>4 TOMATOES CANNED</p>
<p>5 SUGAR</p>
<p>6 CEREAL-SHREDDED-WHEAT-BISQUIT</p>
<p>7 DIETARY SUPPLEMENT</p>
<p>8 PROMETHAZINE INJ 25MG 1ML</p>
<p>9 BATTERY-RECHARGEABLE-9 VOLT</p>
<p>10 PHENYTON SODIUM CAPS 100MG</p>
<p>11 TUBE,TRACH,STERILE,9MM ID</p>
<p>12 SUGAR-REFINED</p>
<p>13 THEOPHYLLINE-TABS-200MG</p>
<p>14 CEREAL-WHEAT</p>
<p>15 LITHIUM-CAP-300MG-100S-UD</p>
<p>16 ENEMA-ADMINISTRATION-SET-DISP</p>
<p>17 NEOSTIGMINE-METHYSULFATE-INJECTION.</p>
<p>18 BEANS, PINTO, CANNED, #10</p>
<p>19 EGGNOG</p>
<p>20 CORN-CANNED-#10</p>
<p>21 TOWEL-PAPER-140SQIN</p></td>
</tr>
<tr class="even">
<td>Select ITEM: 20 CORN-CANNED-#10</td>
</tr>
</tbody>
</table>

#### Item Information

After you select an item, IFCAP will display the unit of sale the vendor uses to sell the item and whether or not you have to buy the item in specific multiples. In the example below, the unit is per can, but the item must be ordered in multiples of six, so you would enter a multiple of six at the QUANTITY: prompt. At the Select ITEM: prompt, you may add another repetitive item, or press \<Enter\> to stop adding items. IFCAP will determine the cost of the items. At the “Would You Like To Create Another Repetitive Item List Entry?” prompt, answer “Y” to add another item or N to return to the Repetitive Item List Menu.

<span id="_Toc222496890" class="anchor"></span>Figure 90: Item Information

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>This item has a mandatory source (vendor) of IFVENDOR, EIGHT</p>
<p>NOTE: This item must be ordered in multiples of 6</p>
<p>NOTE: This item has a packaging multiple/unit of purchase of 1/CAN</p>
<p>QUANTITY: 12</p>
<p>Select ITEM:</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Let me total the cost for this Repetitive Item List entry (#999-94-4-022-844100-</p>
<p>0001)</p>
<p>Total number of items: 1 Total cost (all items): $30.00</p>
<p>Would you like to create another repetitive item list entry? No// (No)</p></td>
</tr>
<tr class="even">
<td><p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests from Repetitive Item List Entry</p>
<p>Select Repetitive Item List Menu Option:</p></td>
</tr>
</tbody>
</table>

#### Edit Repetitive Item List Entry

#### Menu Path

From the Control Point Official’s Menu, select option: Process a Request Menu

<span id="_Toc222496891" class="anchor"></span>Figure 91: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: Repetitive Item List Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Select Repetitive Item List Menu Option: Edit Repetitive Item List Entry</p></td>
</tr>
</tbody>
</table>

#### Select Repetitive Item List (RIL)

Select a repetitive item list. If you do not know the list number, enter three question marks at the Select Repetitive Item List: prompt and IFCAP will display the available item lists.

<span id="_Toc222496892" class="anchor"></span>Figure 92: Select RIL

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select REPETITIVE ITEM LIST #: ???</strong></p>
<p><strong>CHOOSE FROM:</strong></p>
<p><strong>002-93-4-073-632500-0002 09-15-93 # OF ITEMS: 1TOTAL COST: 48.00</strong></p>
<p><strong>002-94-1-073-632500-0001 10-20-93 # OF ITEMS: 1TOTAL COST: 48.00</strong></p>
<p><strong>002-94-1-7001-600000-0014 12-02-93 # OF ITEMS: 3TOTAL COST: 2053.42</strong></p>
<p><strong>002-94-1-7001-600000-0015 12-14-93 # OF ITEMS: 5TOTAL COST: 953514.73</strong></p>
<p><strong>Select REPETITIVE ITEM LIST #: 632500</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1 632500 002-93-4-073-632500-0002 09-15-93 # OF ITEMS: 1TOTAL C</p>
<p>OST: 48.00</p>
<p>2 632500 002-94-1-073-632500-0001 10-20-93 # OF ITEMS: 1TOTAL C</p>
<p>OST: 48.00</p>
<p>CHOOSE 1-2: 1 002-93-4-073-632500-0002</p></td>
</tr>
<tr class="even">
<td><p>Select ITEM: 5// ???</p>
<p>This is a pointer to an item in the Item file, #441. This file is</p>
<p>composed of items specified by Supply Service as being purchased</p>
<p>repetitively. This file maintains a full description of the item,</p>
<p>related stock numbers, vendors, contract numbers, and a procurement</p>
<p>history.</p></td>
</tr>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>1 BANDAGE-CAST-6INX5YD</p>
<p>2 CAP-SAFETY-BOTTLE-50S</p>
<p>3 PLASMA-USP 5%</p>
<p>4 TOMATOES CANNED</p>
<p>5 LIGHT BULBS</p>
<p>6 CEREAL-SHREDDED-WHEAT-BISQUIT</p>
<p>Select ITEM: 5// 5 LIGHT BULBS</p>
<p>...OK? Yes// (Yes)</p>
<p>LIGHT BULBS</p></td>
</tr>
</tbody>
</table>

#### Edit Item

You can change the item again if you like. Enter a QUANTITY. You can add another item at the Select ITEM: prompt, or press \<Enter\> if you are through adding items. IFCAP will list the cost for the items on the list. To return to the Repetitive Item List Menu, press \<Enter\> at the Would you like to edit another repetitive item list entry? prompt.

<span id="_Toc222496893" class="anchor"></span>Figure 93: Edit Item

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>VENDOR: ???</strong></p>
<p><strong>Select the name of the vendor from whom you wish to order this item.</strong></p>
<p><strong>Answer with VENDOR</strong></p>
<p><strong>Choose from:</strong></p>
<p><strong>IFVENDOR,FOUR U/P: EA PH:800 555-5555 NO: 65</strong></p>
<p><strong>ORD ADD:500 PINNACLE COURT FMS:IFCAPVEDOR,FOUR</strong></p>
<p><strong>A CITY, ST 99999 CODE:00080003304 FAX:</strong></p>
<p><strong>IFVENDOR,FIVE U/P: EA PH:800 555-5555 NO: 268</strong></p>
<p><strong>ORD ADD:HOPSON ROAD AT LEADBETTER FMS:IFVENDOR,SIX</strong></p>
<p><strong>ANYTOWN, PA 99999-0424 CODE:54061902001 FAX:</strong></p>
<p><strong>IFVENDOR,SEVEN U/P: EA PH:703 555-5555 NO: 281</strong></p>
<p><strong>ORD ADD:19 FRANKLIN ROAD FMS:IFVENDOR,SEVEN</strong></p>
<p><strong>ANYTOWN, VA 00001 CODE:000131232 FAX:</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>VENDOR: IFVENDOR,FOUR PH:800 555-5555 NO: 65</p>
<p>ORD ADD:500 PINNACLE COURT FMS:IFVENDOR,FOUR</p>
<p>A CITY, ST 99999 CODE:00080003304 FAX:</p>
<p>...OK? Yes// (Yes)</p></td>
</tr>
<tr class="even">
<td><p>U/P: EA</p>
<p>NOTE: This item has a packaging multiple/unit of purchase of 12/EACH</p>
<p>QUANTITY: 12</p>
<p>Select ITEM:</p></td>
</tr>
<tr class="odd">
<td><p>Let me total the cost for this Repetitive Item List entry (#002-93-4-073-632500-</p>
<p>0002)</p>
<p>Total number of items: 1 Total cost (all items): $48.00</p>
<p>Would you like to edit another repetitive item list entry? No// (No)</p></td>
</tr>
<tr class="even">
<td><p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Select Repetitive Item List Menu Option:</p></td>
</tr>
</tbody>
</table>

#### Print/Display Repetitive Item List Entry

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496894" class="anchor"></span>Figure 94: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: Repetitive Item List Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Select Repetitive Item List Menu Option: Print/Display Repetitive Item List Entry</p></td>
</tr>
</tbody>
</table>

#### Enter RIL Number

At the Select REPETITIVE ITEM LIST \#: prompt, enter a Repetitive Item List (RIL) number or name. If you do not know the number or name, enter three question marks (???) and IFCAP will list the available RILs.

<span id="_Toc222496895" class="anchor"></span>Figure 95: Enter RIL Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select REPETITIVE ITEM LIST #: ???</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>002-93-4-073-632500-0002 09-15-93 # OF ITEMS: 1TOTAL COST: 48.00</p>
<p>002-94-1-073-632500-0001 10-20-93 # OF ITEMS: 1TOTAL COST: 48.00</p>
<p>002-94-1-7001-600000-0014 12-02-93 # OF ITEMS: 3TOTAL COST: 2053.42</p>
<p>002-94-1-7001-600000-0015 12-14-93 # OF ITEMS: 5TOTAL COST: 953514.73</p>
<p>002-94-2-7001-600000-0001 03-30-94 # OF ITEMS: 2TOTAL COST: 1621.72</p>
<p>999-94-4-022-844100-0001 07-08-94 # OF ITEMS: 1TOTAL COST: 30.00</p>
<p>Select REPETITIVE ITEM LIST #: 002</p></td>
</tr>
<tr class="even">
<td><p>1 002-93-4-073-632500-0002 09-15-93 # OF ITEMS: 1TOTAL COST:</p>
<p>48.00</p>
<p>2 002-94-1-073-632500-0001 10-20-93 # OF ITEMS: 1TOTAL COST:</p>
<p>48.00</p>
<p>3 002-94-1-7001-600000-0014 12-02-93 # OF ITEMS: 3TOTAL COST:</p>
<p>2053.42</p>
<p>4 002-94-1-7001-600000-0015 12-14-93 # OF ITEMS: 5TOTAL COST:</p>
<p>953514.73</p>
<p>5 002-94-2-7001-600000-0001 03-30-94 # OF ITEMS: 2TOTAL COST:</p>
<p>1621.72</p></td>
</tr>
<tr class="odd">
<td>CHOOSE 1-5: 2</td>
</tr>
<tr class="even">
<td>DEVICE: HOME// LAT RIGHT MARGIN: 80//</td>
</tr>
</tbody>
</table>

#### Item Listing

IFCAP will list each item on the list, the quantity, the unit cost, and the unit of purchase (U/P), listed separately by each vendor that supplies the item. After printing or displaying the item list entry, IFCAP will return to the Repetitive Item List Menu.

<span id="_Toc222496896" class="anchor"></span>Figure 96: Enter RIL Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>REPETITIVE ITEM LIST #: 002-94-1-073-632500-0001DATE: JUL 8,1994@16:42:39 PAGE 1</strong></p>
<p><strong>ITEM NO. SHORT DESCRIPTION QUANTITY UNIT COST U/P</strong></p>
<p><strong>--------------------------------------------------------------------------------</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>VENDOR: IFVENDOR,EIGHT</p>
<p>65 LIGHT BULBS 48 1.00 EA</p>
<p>TOTAL # OF ITEMS: 1 TOTAL COST: 48.00</p>
<p>--------------------------------------------------------------------------------</p>
<p>Press return to continue, uparrow (^) to exit:</p></td>
</tr>
<tr class="even">
<td>TOTAL # OF ITEMS (ALL VENDORS): 1 TOTAL COST (ALL VENDORS): 48.00</td>
</tr>
<tr class="odd">
<td><p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p></td>
</tr>
<tr class="even">
<td>Select Repetitive Item List Menu Option:</td>
</tr>
</tbody>
</table>

#### Generate Requests from Repetitive Item List Entry

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496897" class="anchor"></span>Figure 97: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: Repetitive Item List Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Select Repetitive Item List Menu Option: Generate Requests From Repetitive Item List Entry</p></td>
</tr>
</tbody>
</table>

#### Enter RIL

IFCAP will warn you that this option generates requests with permanent transaction numbers from entries in the RIL file. IFCAP will ask you to confirm that you want to proceed, then will ask you for the RIL number. If you do not know the RIL number, enter three question marks (???) at the Select REPETITIVE ITEM LIST ENTRY NUMBER: prompt and IFCAP will list the available RILs.

<span id="_Toc222496898" class="anchor"></span>Figure 98: Enter RIL

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>This option generates requests with permanent transaction numbers from</strong></p>
<p><strong>entries in the repetitive item list file.</strong></p>
<p><strong>Are you sure you are ready to proceed? NO// Y (YES)</strong></p>
<p><strong>Select REPETITIVE ITEM LIST ENTRY NUMBER: ???</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>002-93-4-073-632500-0002 09-15-93 # OF ITEMS: 1TOTAL COST: 48.00</p>
<p>002-94-1-073-632500-0001 10-20-93 # OF ITEMS: 1TOTAL COST: 48.00</p>
<p>002-94-1-7001-600000-0014 12-02-93 # OF ITEMS: 3TOTAL COST: 2053.42</p>
<p>002-94-1-7001-600000-0015 12-14-93 # OF ITEMS: 5TOTAL COST: 953514.73</p>
<p>002-94-2-7001-600000-0001 03-30-94 # OF ITEMS: 2TOTAL COST: 1621.72</p>
<p>999-94-4-022-844100-0001 07-08-94 # OF ITEMS: 1TOTAL COST: 30.00</p>
<p>Select REPETITIVE ITEM LIST ENTRY NUMBER: 999-94-4-022-844100-0001 07-0</p></td>
</tr>
<tr class="even">
<td><p>8-94 # OF ITEMS: 1TOTAL COST: 30.00</p>
<p>Select FISCAL YEAR: 94//</p></td>
</tr>
</tbody>
</table>

#### Generate Request 

IFCAP will ask you if you want to generate requests using the current quarter or the quarter that the repetitive item list was generated. IFCAP will generate a request, display the transaction number it has assigned to the request, and list the vendor. IFCAP will ask you if you want to edit the item information for the request.

<span id="_Toc222496899" class="anchor"></span>Figure 99: Generate Request

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>You may use either the current quarter or the repetitive item</strong></p>
<p><strong>list quarter to generate requests.</strong></p>
<p><strong>Use repetitive item list quarter? Yes// (Yes)</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DEVICE: HOME// LAT RIGHT MARGIN: 80//</td>
</tr>
<tr class="even">
<td><p>GENERATE REQUESTS FROM REPETITIVE ITEM LIST FILEDATE: JUL 8,1994@16:43</p>
<p>Requests Generated From Repetitive Item List Entry # 999-94-4-022-844100-0001</p>
<p>--------------------------------------------------------------------------------</p>
<p>A request with Transaction Number 999-94-4-022-0010 has been generated.</p>
<p>The vendor for this request is IFVENDOR,EIGHT</p>
<p>Now entering items for this request.</p>
<p>Do you wish to edit this request? No// (No)</p></td>
</tr>
</tbody>
</table>

#### Display 

IFCAP will display the Control Point Balance, the cost of the request it just generated, and the available funds from current and prior quarters. IFCAP will allow you to transmit the request for approval. IFCAP will list the total number of the requests it generated, and the total cost for all of the requests. You can reuse the list to make another request, or press \<Enter\> to return to the Repetitive Item List Menu.

<span id="_Toc222496900" class="anchor"></span>Figure 100: Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Current Control Point balance: $0.00</strong></p>
<p><strong>Estimated cost of this request: $30.00</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Is this request ready for approval? Yes// (Yes)</p>
<p>Is this request ready for transmission to A&amp;MM/Fiscal? No// Y (Yes)</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p></td>
</tr>
<tr class="even">
<td><p>incrementing due-ins in inventory point: NEWONE</p>
<p>Finished building request.</p>
<p>This request contains 3 items. The total cost for this request is $177.00</p>
<p>-----------------------------------------------------------------------------</p>
<p>Total no. of requests generated: 1 Total no. of items (all requests): 3</p>
<p>Total committed (estimated) cost (all requests) : $177.00</p>
<p>Do you wish to re-use this list ? No// (No)</p></td>
</tr>
<tr class="odd">
<td><p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Select Repetitive Item List Menu Option:</p></td>
</tr>
</tbody>
</table>

#### Delete Repetitive Item List Entry

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496901" class="anchor"></span>Figure 101: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: Repetitive Item List Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Select Repetitive Item List Menu Option: Delete Repetitive Item List Entry</p></td>
</tr>
</tbody>
</table>

#### Enter RIL

Enter an RIL number. If you do not know the number, enter three question marks (???) at the Select REPETITIVE ITEM LIST \#: prompt and IFCAP will list the available RILs.

<span id="_Toc222496902" class="anchor"></span>Figure 102: Enter RIL

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select REPETITIVE ITEM LIST #: ???</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>002-93-4-073-632500-0002 09-15-93 # OF ITEMS: 1TOTAL COST: 48.00</p>
<p>002-94-1-073-632500-0001 10-20-93 # OF ITEMS: 1TOTAL COST: 48.00</p>
<p>002-94-1-7001-600000-0014 12-02-93 # OF ITEMS: 3TOTAL COST: 2053.42</p>
<p>002-94-1-7001-600000-0015 12-14-93 # OF ITEMS: 5TOTAL COST: 953514.73</p>
<p>002-94-2-7001-600000-0001 03-30-94 # OF ITEMS: 2TOTAL COST: 1621.72</p>
<p>Select REPETITIVE ITEM LIST #: 002</p></td>
</tr>
<tr class="even">
<td><p>1 002-93-4-073-632500-0002 09-15-93 # OF ITEMS: 1TOTAL COST: 48.00</p>
<p>2 002-94-1-073-632500-0001 10-20-93 # OF ITEMS: 1TOTAL COST: 48.00</p>
<p>3 002-94-1-7001-600000-0014 12-02-93 # OF ITEMS: 3TOTAL COST: 2053.42</p>
<p>4 002-94-1-7001-600000-0015 12-14-93 # OF ITEMS: 5TOTAL COST: 953514.73</p>
<p>5 002-94-2-7001-600000-0001 03-30-94 # OF ITEMS: 2TOTAL COST: 1621.72</p>
<p>CHOOSE 1-5: 5</p></td>
</tr>
</tbody>
</table>

#### Delete Item List

IFCAP will ask you to confirm that you want to delete the item list, and ask if you want to delete another. If you respond NO, IFCAP will return to the Repetitive Item List Menu.

<span id="_Toc222496903" class="anchor"></span>Figure 103: Delete Item List

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Are you sure you want to delete this Repetitive Item List entry? No// Y (Yes)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Okay.....It's deleted.</p>
<p>Would you like to delete another Repetitive Item List entry? No// (No)</p></td>
</tr>
<tr class="even">
<td><p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Select Repetitive Item List Menu Option:</p></td>
</tr>
</tbody>
</table>

### Copy a Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496904" class="anchor"></span>Figure 104: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: Copy a Transaction</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Setup Parameters

Enter a STATION NUMBER and a CONTROL POINT. At the Select the Transaction to be copied: prompt, enter the number of the transaction to be copied. If you do not know the transaction number, enter three question marks (???) at the prompt to have IFCAP will list the available transactions.

<span id="_Toc222496905" class="anchor"></span>Figure 105: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 999 ANYCITY,ANYSTATE</p>
<p>Select CONTROL POINT: 022 IFVENDOR</p>
<p>...OK? Yes// (Yes)</p>
<p>Select the Transaction to be copied: ???</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Attempting lookup in transaction file.</p>
<p>Attempting lookup using 022 IFVENDOR (CONTROL POINT)</p>
<p>1 022 IFVENDOR 999-94-4-022-0010 OBL IFVENDOR,EIGHT CORN-CANNED-#10</p>
<p>2 022 IFVENDOR 999-94-4-022-0007 CANC</p>
<p>Transaction no. 999-13-4-022-0007 was replaced by trans. no. 999-13-4-022-0009</p>
<p>3 022 SUPPLIES 999-13-4-022-0008 OBL IFVENDOR,TWO</p>
<p>4 022 SUPPLIES 999-13-4-022-0009 OBL IFVENDOR,ONE</p>
<p>This is where the "Description" goes.</p>
<p>5 022 SUPPLIES 999-13-4-022-0006 OBL</p>
<p>Heparin</p>
<p>Accepted by eCMS</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p></td>
</tr>
<tr class="even">
<td>CHOOSE 1-5: 1 999-94-4-022-0010</td>
</tr>
<tr class="odd">
<td></td>
</tr>
</tbody>
</table>

#### Review Request

IFCAP will ask you if you would like to review the request, and ask you to enter new information about the transaction. IFCAP will allow you to enter a new Station number, fiscal year, quarter, and Control Point for the transaction.

<span id="_Toc222496906" class="anchor"></span>Figure 106: Review Request

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Would you like to review this request? No// (No)</p>
<p>Would you like to proceed ? Yes// (Yes)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Now enter the information for the new transaction number.</td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>Select STATION NUMBER: 999// ANYCITY,ANYSTATE</p>
<p>Select FISCAL YEAR: 13//</p>
<p>Select QUARTER: 4//</p>
<p>Select CONTROL POINT: 022 IFVENDOR//</p></td>
</tr>
</tbody>
</table>

#### Assign Transaction Number

IFCAP will assign a transaction number to the request. Based on the transaction you select, IFCAP will prompt you for additional information about the purpose of your request and the source of funds.

Enter “T” for today as the date of the request. Enter your name as the REQUESTOR. Enter the Service for which you are creating the request at the REQUESTING SERVICE: prompt. Enter the date that the goods or services are required.

Assign a priority to the request. The priority categories in IFCAP, ranging from shortest to longest delivery time remaining, are “Emergency”, “Special” and “Standard.” Different stations assign different time durations to these categories. Check with your Fiscal office to determine the durations at your station for these categories.

<span id="_Toc222496907" class="anchor"></span>Figure 107: Assign Transaction Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The form type for this request is: REPETITIVE &amp; NON-REPETITIVE</p>
<p>Transaction data is being copied...</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CLASSIFICATION OF REQUEST:</p>
<p>SORT GROUP:</p>
<p>DATE OF REQUEST: TODAY// (JUL 08, 2013)</p>
<p>REQUESTOR: IFUSER2,THREE</p>
<p>REQUESTING SERVICE: NOTE: This is now a Required field – if it is not populated you will be prompted to enter the appropriate Service.</p>
<p>DATE REQUIRED: T+3 (AUG 11, 2013)</p>
<p>PRIORITY OF REQUEST: ST// STANDARD</p></td>
</tr>
</tbody>
</table>

#### Special Remarks

At the SPECIAL REMARKS: prompt, explain how the service will use the item, names of other items that would fulfill the same need, and any other information that would help the Purchasing Agent fulfill your request. Purchasing Agents sometimes change orders to fulfill the service’s need faster, find a better item or obtain a better price. Explaining the use of the item will make these tasks easier to accomplish.

Enter a COST CENTER. Using Cost Centers allow Fiscal staff to create total expense records for a section or service.

At the Select Line-Item Number: prompt, enter “1” for the first item on the request.

At the ITEM MASTER FILE NO.: prompt, enter the item name or number. You can also type three question marks (???) to see a list of the items you can request.

Enter how many units of purchase (not number of items) at the QUANTITY: prompt.

At the BOC: prompt, enter the budget object code classification for this item. If you do not know the BOC for this item, enter three question marks and IFCAP will list the available BOCs.

At the INTERMEDIATE PRODUCT CODE: prompt, enter the Intermediate Product Code if there is one. The Intermediate Product Code is a stock number that vendors sometimes use.

If you want to add another item to your request, enter “2” at the Select Line-Item Number: prompt.

IFCAP will display the estimated cost of your request. At the DATE COMMITTED: prompt, enter the date that you want IFCAP to commit funds to the purchase. At the Select SUB-CONTROL POINT: prompt, you can associate this purchase with a category of purchases that you can define. This allows you to group similar purchases together.

Enter where you want the warehouse to deliver the item at the DELIVER TO/LOCATION: prompt, including room and building number if you can.

At the JUSTIFICATION: prompt, explain why the service or item is needed by the service. Add COMMENTS if you like. IFCAP will ask you if you want to review the request again and will display the current balance of the Control Point, the cost of the request, and the money available to the Control Point from current and prior quarters. IFCAP will ask you if you want to send the request to the Control Point Official for approval.

| ![](ifcap-version-5-1-control-point-official-user-s-guide/056.png) | *<u>NOTE:</u>* If any of the Required fields are not populated, you will not be able to set the request to YES ready for Control Point Official approval. | ![](ifcap-version-5-1-control-point-official-user-s-guide/057.png) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

You can copy another request, or press \<Enter\> at the prompt to return to the Process a Request Menu.

<span id="_Toc222496908" class="anchor"></span>Figure 108: Special Remarks

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SPECIAL REMARKS:</p>
<p>1&gt;</p>
<p>COST CENTER: 844100 Supply//</p>
<p>Select LINE ITEM NUMBER: 1//</p>
<p>LINE ITEM NUMBER: 1//</p>
<p>ITEM MASTER FILE NO.: //</p>
<p>DESCRIPTION:</p>
<p>This is now a Required field. You must enter text.</p>
<p>Edit Option:</p>
<p>QUANTITY: 12//</p>
<p>BOC: 2610 Provisions//</p>
<p>Select LINE ITEM NUMBER:</p>
<p>COMMITTED (ESTIMATED) COST: 30//</p>
<p>DATE COMMITTED:</p>
<p>TRANSACTION BEG BAL: 30.00</p>
<p>Select SUB-CONTROL POINT:</p>
<p>DELIVER TO/LOCATION: Bldg. 20</p>
<p>JUSTIFICATION:</p>
<p>1&gt;</p>
<p>ORIGINATOR OF 2237: IFUSER2,THREE</p>
<p>COMMENTS:</p>
<p>1&gt;</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Would you like to review this request? Yes// (Yes)</p>
<p>Current Control Point balance: $0.00</p>
<p>Estimated cost of this request: $30.00</p>
<p>Total uncommitted balance from current and prior quarters: $4734.20</p>
<p>Is this request ready for approval? No// (No)</p>
<p>NOTE: User will not be asked this question if the Required fields are not populated. User will have to Edit the 2237 and populate all required fields before User will be permitted to Approve the 2237 and send it forward to A&amp;MM/FISCAL.</p>
<p>Would you like to copy another request? Yes// N (No)</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### Item Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496909" class="anchor"></span>Figure 109: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Select Process a Request Menu Option: Item Display</td>
</tr>
</tbody>
</table>

#### Enter Item Number

At the Select ITEM MASTER NUMBER: prompt, enter an item master number. If you do not know the item master number, type three question marks (???) and IFCAP will list the available items.

<span id="_Toc222496910" class="anchor"></span>Figure 110: Enter Item Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select ITEM MASTER NUMBER: ???</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>1 BANDAGE-CAST-6INX5YD</p>
<p>2 CAP-SAFETY-BOTTLE-50S</p>
<p>3 PLASMA-USP 5%</p>
<p>4 TOMATOES CANNED</p>
<p>5 SUGAR</p>
<p>6 CEREAL-SHREDDED-WHEAT-BISQUIT</p>
<p>7 DIETARY SUPPLEMENT</p>
<p>8 PROMETHAZINE INJ 25MG 1ML</p>
<p>9 BATTERY-RECHARGEABLE-9 VOLT</p>
<p>10 PHENYTON SODIUM CAPS 100MG</p>
<p>11 TUBE,TRACH,STERILE,9MM ID</p>
<p>12 SUGAR-REFINED</p>
<p>13 THEOPHYLLINE-TABS-200MG</p>
<p>14 CEREAL-WHEAT</p>
<p>15 LITHIUM-CAP-300MG-100S-UD</p>
<p>16 ENEMA-ADMINISTRATION-SET-DISP</p>
<p>17 NEOSTIGMINE-METHYSULFATE-INJECTION.</p>
<p>18 BEANS, PINTO, CANNED, #10</p>
<p>19 EGGNOG</p>
<p>20 CORN-CANNED-#10</p>
<p>21 TOWEL-PAPER-140SQIN</p></td>
</tr>
<tr class="even">
<td>Select ITEM MASTER NUMBER: 4 TOMATOES CANNED</td>
</tr>
<tr class="odd">
<td>NUMBER: 4 SHORT DESCRIPTION: TOMATOES CANNED</td>
</tr>
</tbody>
</table>

#### Item Information

IFCAP will display a series of descriptions of the item, including vendor information, units of purchase, and purchase orders that procured the item. You can either enter another item master number or press \<Enter\> to return to the Process a Request Menu.

<span id="_Toc222496911" class="anchor"></span>Figure 111: Item Information

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>FSC: 8940</p>
<p>LAST VENDOR ORDERED: IFVENDOR,NINE</p>
<p>NSN: 8940-00-851-7063 MANDATORY SOURCE: IFVENDOR,EIGHT</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DATE ITEM CREATED: JAN 25, 1993 BOC: 2610 Provisions</p>
<p>CREATED BY: IFUSER2,EIGHT INC: 02183</p>
<p>DESCRIPTION: TOMATOES CANNED WHOLE OR LARGE PIECES DIETETIC NO. 303</p>
<p>VENDOR: IFVENDOR,EIGHT UNIT COST: 1.888</p>
<p>DATE OF UNIT PRICE: JAN 25, 1993 UNIT OF PURCHASE: CS</p>
<p>PACKAGING MULTIPLE: 6 MAXIMUM ORDER QTY: 6</p>
<p>UNIT CONVERSION FACTOR: 3 REQUIRED ORDER MULTIPLE: 6</p></td>
</tr>
<tr class="even">
<td><p>VENDOR: IFVENDOR,NINE UNIT COST: 1.01</p>
<p>DATE OF UNIT PRICE: DEC 2, 1993 UNIT OF PURCHASE: CN</p>
<p>PACKAGING MULTIPLE: 1 UNIT CONVERSION FACTOR: 1</p></td>
</tr>
<tr class="odd">
<td><p>VENDOR: IFVENDOR,TEN UNIT COST: 1.889</p>
<p>DATE OF UNIT PRICE: JAN 25, 1993 UNIT OF PURCHASE: CN</p>
<p>PACKAGING MULTIPLE: 6 MAXIMUM ORDER QTY: 6</p>
<p>UNIT CONVERSION FACTOR: 1 REQUIRED ORDER MULTIPLE: 6</p>
<p>MINIMUM ORDER QTY: 1</p></td>
</tr>
<tr class="even">
<td><p>VENDOR: IFVENDOR1,ONE UNIT COST: .89</p>
<p>DATE OF UNIT PRICE: MAR 9, 1993 UNIT OF PURCHASE: CN</p>
<p>PACKAGING MULTIPLE: 1</p></td>
</tr>
<tr class="odd">
<td><p>NSN VERIFIED: DEC 2, 1993 FOOD GROUP: Fruits, Vegetables</p>
<p>SKU: CN</p>
<p>FCP: 002033</p></td>
</tr>
<tr class="even">
<td><p>PURCHASE ORDER: 002-B40006</p>
<p>LONG NAME (c): SITE: 002 FCP: 033 PHARMACY</p>
<p>FCP: 0027001</p>
<p>PURCHASE ORDER: 002-G38095</p>
<p>PURCHASE ORDER: 002-G30004</p>
<p>PURCHASE ORDER: 002-G38043</p>
<p>LONG NAME (c): SITE: 002 FCP: 7001 SUPPLY FUND</p></td>
</tr>
<tr class="odd">
<td>Enter RETURN to continue or '^' to exit:</td>
</tr>
<tr class="even">
<td>Select ITEM MASTER NUMBER:</td>
</tr>
<tr class="odd">
<td><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### Vendor Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496912" class="anchor"></span>Figure 112: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Select Process a Request Menu Option: Vendor Display</td>
</tr>
</tbody>
</table>

#### Enter Vendor

At the Select VENDOR NAME: prompt, enter a vendor name. If you do not know the vendor’s name, enter three question marks (???) at the prompt and IFCAP will list the available vendors.

<span id="_Toc222496913" class="anchor"></span>Figure 113: Enter Vendor

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select VENDOR NAME: IFVENDOR,TWO 000-456-7890 NO. 741</p>
<p>SPECIAL FACTORS:</p>
<p>ORDERING ADDRESS: 6877 POST AVE</p>
<p>ANYTOWN, AK 11111</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>...OK? Yes// (Yes)</td>
</tr>
<tr class="even">
<td>DEVICE: LAT RIGHT MARGIN: 80//</td>
</tr>
</tbody>
</table>

#### Vendor Information

IFCAP will list a comprehensive set of descriptions of the vendor, including address, socioeconomic and business category information, payment information, and contract information. After the list, you can enter another vendor, or press \<Enter\> at the prompt to return to the Process a Request Menu.

<span id="_Toc222496914" class="anchor"></span>Figure 114: Vendor Information

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VENDOR LIST JUL 8,1994 16:52 PAGE 1</p>
<p>-----------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NUMBER: 741 NAME: IFVENDOR,TWO</p>
<p>ORDERING ADDRESS1: 6877 POST AVE ORDERING CITY: ANYTOWN</p>
<p>ORDERING STATE: ALASKA ORDERING ZIP CODE: 11111</p>
<p>VA P&amp;C contact number: 000-555-5555</p>
<p>SOCIOECONOMIC GROUP (FPDS): OO NONE OF THE ABOVE</p>
<p>BUSINESS TYPE (FPDS): SMALL IS A SF129 ON FILE?: NOT APPLICABLE</p>
<p>FMS VENDOR CODE: 000222444 TAX ID/SSN: 000222444</p>
<p>SSN/TAX ID INDICATOR: SOCIAL SECURITY NUMBER</p>
<p>PAYMENT HOLD INDICATOR: NO 1099 VENDOR INDICATOR: YES</p>
<p>PENDING FLAG: CONFIRMATION OF APPROVAL</p>
<p>CENTRAL REMIT: NO VENDOR TYPE: COMMERCIAL</p>
<p>MTI ACTION: CHANGE</p>
<p>CONTRACT NUMBER: 2432424 EXPIRATION DATE: AUG 4, 1994</p>
<p>BEGINING DATE: APR 16, 1994</p>
<p>PAYMENT NO.: 409-555-5555 PAYMENT ADDRESS1: 1453 KINWOOD LANE</p>
<p>PAYMENT ADDRESS2: SUITE 100 PAYMENT CITY: BALTIMORE</p>
<p>PAYMENT STATE: MARYLAND PAYMENT ZIP CODE: 21210\</p>
<p>DATE VENDOR CREATED: JUL 1, 1994 CREATED BY: POSTMASTER</p></td>
</tr>
<tr class="even">
<td>Select VENDOR NAME:</td>
</tr>
<tr class="odd">
<td><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### Outstanding Approved Requests Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496915" class="anchor"></span>Figure 115: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: Outstanding Approved Requests Report</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Setup Parameters and Display

Enter a STATION NUMBER, FISCAL YEAR and FISCAL QUARTER. Enter a CONTROL POINT. If you do not know the Control Point, enter three question marks and IFCAP will display the available Control Points. IFCAP will list each outstanding request for the Control Point you select. Type a caret (^) at the “Select STATION NUMBER:” prompt to return to the Process a Request Menu.

<span id="_Toc222496916" class="anchor"></span>Figure 116: Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 002// ANYTOWN, PA</p>
<p>Select FISCAL YEAR: 94//</p>
<p>Select QUARTER: 4//</p>
<p>Select CONTROL POINT: 022 IFVENDOR,THREE/</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Processing entries...</td>
</tr>
<tr class="even">
<td>DEVICE: HOME// LAT RIGHT MARGIN: 80//</td>
</tr>
<tr class="odd">
<td><p>OUTSTANDING APPROVED REQUEST REPORT - CP 022 JUL 8,1994@17:34:10 PAGE 1</p>
<p>TRANSACTION NUMBER TRANSACTION STATUS VENDOR</p>
<p>DATE SIGNED EST. DEL. DATE PO # DATE OBL. DATE REQ.</p>
<p>-----------------------------------------------------------------------------</p>
<p>999-088-400101-94-3 OBL IFVENDOR1,TWO</p>
<p>04-09-94 05-02-94 999-088-94-3 04-09-94 05-04-94</p>
<p>------------------</p>
<p>End of processing</p>
<p>Select STATION NUMBER: 002//^</p></td>
</tr>
<tr class="even">
<td><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option:</p></td>
</tr>
</tbody>
</table>

## Options in the 1358 Request Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New 1358 Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496917" class="anchor"></span>Figure 117: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: 1358 Request Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option: New 1358 Request</p></td>
</tr>
</tbody>
</table>

#### Setup Parameters

Enter a STATION NUMBER, FISCAL YEAR and FISCAL QUARTER. Select a Control Point.

<span id="_Toc222496918" class="anchor"></span>Figure 118: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select</strong> STATION NUMBER: 999 ANYCITY,ANYSTATE</p>
<p>Select FISCAL YEAR: 11//</p>
<p>Select QUARTER: 1//</p>
<p>Select CONTROL POINT: 110</p>
<p>1 110 Stuff .01</p>
<p>2 1011 BUDGET RETEST</p>
<p>3 1012 BUDGET RETEST</p>
<p>Select CONTROL POINT: 1</p>
<p>...OK? Yes// (Yes)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Authority & Sub-Authority Fields

Enter an Authority. Depending on the Authority selected the User may be prompted for a Sub-Authority. Users must enter a value to continue the process.

IFCAP will assign a Transaction number to your request. Write this number down; you will need it to determine the status of your request.

Select AUTHORITY OF REQUEST: ??

Choose from:

1 NURSING HOME/ADULT DAYCARE

2 FEE BASIS

3 STANDARDIZED OBLIGATIONS

4 LIMITED OPEN TRAVEL AUTHORITY

5 RESEARCH STUDIES

6 INTER-LIBRARY LOAN PROGRAM

7 AFFILIATED AGREEMENTS FOR INTERNS/RESIDENTS

8 TORT CLAIMS/EEO SETTLEMENTS/OIG CONFIDENTIAL SERVICES

9 VOLUNTEER MEAL TICKETS

10 INCENTIVE THERAPY/COMPENSATED WORK THERAPY

11 BENEFICIARY TRAVEL

12 HOME IMPROVEMENT STRUCTURAL ALTERATIONS

13 OUTER BURIAL RECEPTACLES

14 VBA LEASE AGREEMENT OVERTIME CHARGES

15 HOME OXYGEN BILLS

16 PROSTHETICS

17 PHARMACY AND SUBSISTENCE PRIME VENDOR

18 REGULATED UTILITIES

19 TUITION REIMBURSEMENT TO VA EMPLOYEES

20 NON-PROCUREMENT OBLIGATIONS

21 HEALTH ADMIN CARE PROGRAMS

22 SPECIAL ADAPTIVE HOUSING INSPECTIONS

23 STATE APPROVING AGENCY

Select AUTHORITY OF REQUEST: 2 FEE BASIS

Select SUB-AUTHORITY OF REQUEST: ??

Choose from:

A FEE MEDICAL/DENTAL (PRE-AUTHORIZED)

B FEE MEDICAL/DENTAL (NOT PRE-AUTHORIZED)

C HOMEMAKER/HOME HEALTH AID

D NON-VA HOSPITALIZATION (PRE-AUTHORIZED)

E NON-VA HOSPITALIZATION (NOT PRE-AUTHORIZED)

F NON-CONTRACT EMERGENCY TRAVEL

Select SUB-AUTHORITY OF REQUEST: d NON-VA HOSPITALIZATION (PRE-AUTHORIZED)

This transaction is assigned Transaction number: 999-11-1-110-0010

#### Classification and Sort Groups

At the CLASSIFICATION OF REQUEST: prompt, you may create reports that group requests by categories that *you* define.

At the SORT GROUP: prompt, enter a Sort Group *if* this purchase is assigned to a project, office, or some other category for which a Sort Group has been created. If this purchase doesn’t belong to a Sort Group, just press \<Enter\>. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the Sort Group and exclude all purchases that don’t belong to the Sort Group.

<span id="_Toc222496919" class="anchor"></span>Figure 119: Classification and Sort Groups

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CLASSIFICATION OF REQUEST: ???</p>
<p>This Classification of Request field allows you</p>
<p>to classify and/or categorize all transactions</p>
<p>(requests) for supplies, services, etc.</p>
<p>This is the previous 'Type of Request" field.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHOOSE FROM: ???</p>
<p>This is the name used to identify the type of request. File #410.2</p>
<p>is pointed to by the Classification of Request field (#8) of the</p>
<p>Control Point Activity file, #410.</p>
<p>CLASSIFICATION OF REQUEST:</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>SORT GROUP: ???</p>
<p>This Sort Group field may be used to group together all</p>
<p>transactions (requests) that relate to a specific project,</p>
<p>work order, investigator, food group, doctor, etc.</p>
<p>This is the previous 'Project Number' field.</p>
<p>Enter one of the following:</p>
<p>S.EntryName to select a Sort Group</p>
<p>W.EntryName to select a Work Order</p>
<p>To see the entries in any particular file, type &lt;Prefix.?&gt;</p>
<p>If you simply enter a name then the system will search each of</p>
<p>the above files for the name you have entered. If a match is</p>
<p>found the system will ask you if it is the entry that you desire.</p>
<p>However, if you know the file the entry should be in, then you can</p>
<p>speed processing by using the following syntax to select and entry:</p>
<p>&lt;Prefix&gt;.&lt;entry name&gt;</p>
<p>or</p>
<p>&lt;Message&gt;.&lt;entry name&gt;</p>
<p>or</p>
<p>&lt;File Name&gt;.&lt;entry name&gt;</p>
<p>Also, you do NOT need to enter the entire file name or message</p>
<p>to direct the look up. Using the first few characters will suffice.</p>
<p>SORT GROUP:</p></td>
</tr>
</tbody>
</table>

#### Requestor and Cost Information

| ![](ifcap-version-5-1-control-point-official-user-s-guide/058.png) | *<u>NOTE:</u>* Per implementation of Segregation of Duties within the 1358 options, the User is no longer asked to Enter the name of an individual at the Requestor: prompt. Your name is automatically entered as the Requestor. | ![](ifcap-version-5-1-control-point-official-user-s-guide/059.png) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

Press \<Enter\> at the Date of Request: prompt.

At the DATE COMMITTED: prompt, enter the date that you want to commit funds to your request.

At the COMMITTED (ESTIMATED) COST: prompt, enter the total cost (in dollars) for the item.

At the COST CENTER: prompt, enter the cost center *if* this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses. Cost centers allow Fiscal staff to create total expense records for a section or service.

<span id="_Toc222496920" class="anchor"></span>Figure 120: Cost Information

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>DATE OF REQUEST: OCT 4,2010// (OCT 04, 2010)</p>
<p>DATE COMMITTED: 10/01/10// (OCT 01, 2010)</p>
<p>TYPE A NUMBER BETWEEN 0 AND 9999999</p>
<p>COMMITTED (ESTIMATED) COST: 585 $ 585.00</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>This is the estimated amount of the committed cost of</p>
<p>the requested item(s).</p></td>
</tr>
<tr class="even">
<td>COST CENTER: 820100 Medical Service</td>
</tr>
</tbody>
</table>

#### Budget Object Code

At the BOC1: prompt, enter the BOC for this item. If you do not know the BOC for this item, enter three question marks (???) and IFCAP will list the available BOCs.

At the BOC1 Amount: prompt, enter the amount of the item you want to attribute to the BOC.

You may also enter a SUB-CONTROL POINT if you like.

<span id="_Toc222496921" class="anchor"></span>Figure 121: Budget Object Code

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>BOC1: ?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>CHOOSE FROM:</p>
<p>1081 Physicians-Full Time</p>
<p>1090 Administrative and Clerical Personnel Not Otherwise Classified</p>
<p>1092 Stay-In-School Program Part-Time Employment of Needy Students</p>
<p>1093 Subsistence &amp; Temp Exp, Real Estate Costs &amp; Misc Exp-PL 89-516</p>
<p>1095 Employee Salary Continuation</p>
<p>1096 Computer Sys Analyst, Programmers, Keypunch &amp; Computer Opr's</p>
<p>BOC1: 2580 Miscellaneous Contractual Services by Individuals, Institu and Organiz</p>
<p>TRANSACTION BEG BAL: 585</p></td>
</tr>
<tr class="odd">
<td>Select SUB-CONTROL POINT:</td>
</tr>
</tbody>
</table>

#### Enter Vendor

If the Authority selected requires that a Vendor be entered on the 1358 the User will not be permitted to proceed until a valid Vendor is entered.

If the Authority selected does not require a Vendor, the User will be able to pass the field.

At the “Do you want to enter a vendor for this 1358 request?” prompt, IFCAP is asking you if you want to enter a vendor for the request. You may or may not, depending on whether there is a single vendor or there are multiple vendors for the service. If there is only one vendor, you may enter the vendor’s name at the prompt. If there are multiple vendors, leave this field blank.

The VENDOR CONTRACT NUMBER: prompt is now conditionally mandatory based on the Authority selected. Enter the appropriate, active contract number for the order, if the Contract \# is required. If it is not the User can pass the field and leave it blank.

As shown below, you may enter three question marks (???) to see a list of numbers.

<span id="_Toc222496922" class="anchor"></span>Figure 122: Enter Vendor

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Do you want to enter a vendor for this 1358 request? No//</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>VENDOR CONTRACT NUMBER: ???</p>
<p>Select the appropriate contract number applicable to this request.</p></td>
</tr>
</tbody>
</table>

#### Service Start and End Dates and Purpose

The Service Start Date, Service End Date, and the Purpose field are mandatory fields.

Enter the appropriate Service Start Date for the Period of Service covered by the 1358.

Enter the appropriate Service End Date for the Period of Service covered by the 1358.

Enter text to explain the PURPOSE of the order.

Add COMMENTS if you like. You can enter another 1358 request if you like, or press \<Enter\> to return to the 1358 Request Menu.

<span id="_Toc222496923" class="anchor"></span>Figure 123: Enter Vendor Address, Contact Information, and Purpose

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SERVICE START DATE: 100110 OCT 1, 2010</p>
<p>SERVICE END DATE: 103110 OCT 31, 2010</p>
<p>PURPOSE:</p>
<p>1&gt;Monthly HHA Costs</p>
<p>2&gt;</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EDIT Option:</td>
</tr>
<tr class="even">
<td><p>ORIGINATOR OF REQUEST: IFUSER2,TWO</p>
<p>COMMENTS:</p>
<p>1&gt;</p>
<p>Would you like to review this request? No// N (No)</p></td>
</tr>
<tr class="odd">
<td><p>Current Control Point balance: $0.00</p>
<p>Estimated cost of this request: $441.00</p>
<p>Is this request ready for approval? Yes// (Yes)</p>
<p>Is this request ready for transmission to A&amp;MM/Fiscal? No// (No)</p>
<p>Do you want to enter another NEW request? NO//</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### Increase/Decrease Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496924" class="anchor"></span>Figure 124: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: 1358 Request Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option: Increase/Decrease Adjustment</p></td>
</tr>
</tbody>
</table>

#### Setup Parameters

Enter a STATION NUMBER, FISCAL YEAR and FISCAL QUARTER. Enter a CONTROL POINT. If you do not know the Control Point, enter three question marks and IFCAP will display the available Control Points. Enter an OBLIGATION NUMBER (this is number that Fiscal Service assigns to the 1358 form). IFCAP will display the number assigned to the adjustment transaction.

<span id="_Toc222496925" class="anchor"></span>Figure 125: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 002 ANYTOWN, PA</p>
<p>Select FISCAL YEAR: 94//</p>
<p>Select QUARTER: 4//</p>
<p>Select CONTROL POINT: 022 IFVENDOR,THREE</p>
<p>...OK? Yes// (Yes)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select OBLIGATION NUMBER: ???</p>
<p>CHOOSE FROM:</p>
<p>C30032 OBL C30032</p>
<p>C30033 OBL C30033</p>
<p>C30034 OBL C30034</p>
<p>Select OBLIGATION NUMBER: C30032 002-93-2-022-0001 OBL C30032</p></td>
</tr>
<tr class="even">
<td><p>Original Obligation Amount: $ 1,000.00 Service Balance: $ 100.00</p>
<p>Fiscal's 1358 Balance: $ 1,000.00</p>
<p>This transaction is assigned transaction number: 002-94-4-022-0007</p></td>
</tr>
</tbody>
</table>

#### Classification and Sort Groups

At the Classification of Request: prompt, you may create reports that group requests by categories that *you* define.

At the SORT GROUP: prompt, enter a Sort Group *if* this purchase is assigned to a project, office, or some other category for which a Sort Group has been created. If this purchase doesn’t belong to a Sort Group, just press \<Enter\>. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the Sort Group and exclude all purchases that don’t belong to the Sort Group.

Enter your name as the REQUESTOR. Enter “T” for today as the date of the request.

At the COST CENTER: prompt, enter a Cost Center *if* this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses. Cost centers allow Fiscal staff to create total expense records for a section or service.

At the DATE OBL ADJUSTED: prompt, enter the date that the obligation was adjusted.

At the ADJUSTMENT \$ AMOUNT: prompt, enter the amount by which you want to adjust the obligation. Type the number without any symbols to add money to the obligation. Type a minus symbol in front of the amount to subtract money from the obligation.

<span id="_Toc222496926" class="anchor"></span>Figure 126: Classification and Sort Groups

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>CLASSIFICATION OF REQUEST:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SORT GROUP:</td>
</tr>
<tr class="even">
<td>REQUESTOR: IFUSER2,THREE</td>
</tr>
<tr class="odd">
<td>DATE OF REQUEST: JUL 8,1994// (JUL 08, 1994)</td>
</tr>
<tr class="even">
<td><p>COST CENTER: 844100 Supply//</p>
<p>DATE OBL ADJUSTED:</p>
<p>ADJUSTMENT $ AMOUNT: 400 $ 400.00</p></td>
</tr>
</tbody>
</table>

#### Budget Object Code

At the BOC1: prompt, enter the BOC for this item. If you do not know the BOC for this item, enter three question marks (???) and IFCAP will list the available BOCs.

At the BOC1 Amount: prompt, enter the amount of the item you want to attribute to the BOC.

Enter the amount of the item you want to attribute to the budget object code at the BOC1 Amount: prompt.

At the Select SUB-CONTROL POINT: prompt, you may enter a sub-control point if you like in order to associate this purchase with a category of purchases that *you* define. This allows you to group similar purchases together.

Enter the PURPOSE for the adjustment. Add COMMENTS if you like.

IFCAP will let you review the request. IFCAP will list the current Control Point balance, the estimated cost of the adjustment, and the total uncommitted balance from current and prior quarters.

IFCAP will also allow you to transmit the adjustment to the Control Point Clerk for approval. At the Enter another increase/decrease adjustment?: prompt, enter “NO” to return to the 1358 Request Menu.

<span id="_Toc222496927" class="anchor"></span>Figure 127: Budget Object Code

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>BOC1: 2660 Operating Supplies and Ma Replace</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>BOC1 $ AMOUNT: 400// $ 400.00</p>
<p>TRANSACTION BEG BAL: 400.00</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Select SUB-CONTROL POINT:</td>
</tr>
<tr class="odd">
<td><p>PURPOSE:</p>
<p>1&gt;</p>
<p>COMMENTS:</p>
<p>1&gt;</p>
<p>Would you like to review this request? NO// (NO)</p></td>
</tr>
<tr class="even">
<td><p>Current Control Point balance: $0.00</p>
<p>Estimated cost of this request: $400.00</p>
<p>Is this request ready for approval? Yes//N (No)</p>
<p>Enter another increase/decrease adjustment? NO//</p></td>
</tr>
<tr class="odd">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### Edit 1358 Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496928" class="anchor"></span>Figure 128: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: 1358 Request Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>y</p>
<p>Select 1358 Request Menu Option: Edit 1358 Request</p></td>
</tr>
</tbody>
</table>

#### Setup Parameters

Enter a STATION NUMBER and a CONTROL POINT.

At the Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: prompt, enter the transaction number of the 1358 form. If you do not know the transaction number, enter three question marks (???) and IFCAP will list the available transactions.

| ![](ifcap-version-5-1-control-point-official-user-s-guide/060.png) | *<u>NOTE:</u>* Per the implementation of Segregation of Duties, you will be advised that continuation of the process will result in your becoming the Requestor for the 1358. Another Control Point Official will have to Approve the 1358. | ![](ifcap-version-5-1-control-point-official-user-s-guide/061.png) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

At the AUTHORITY: prompt. You may accept the default value or change the value if that is appropriate.

If the SUB-AUTHORITY: prompt appears, you may accept the default value or change the value if that is appropriate.

<span id="_Toc222496929" class="anchor"></span>Figure 129: Setup Parameters

Select 1358 Request Menu Option: Edit 1358 Request

Select STATION NUMBER: 999

Select CONTROL POINT: 110 STUFF .01 0160A1 10 0100 010042116

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER:??

Attempting lookup using 110 (CONTROL POINT)

…………………………………………………………………………………

7 110 STUFF .01 999-11-1-110-0016 OBL

8 110 STUFF .01 999-11-1-110-0015 OBL

9 110 STUFF .01 999-11-1-110-0014 OBL

10 110 STUFF .01 999-11-1-110-0013 OBL IFVENDOR ONE C15002

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-10: 7 999-11-1-110-0016 OBL

> **WARNING:** The system will assign you as the CP Clerk (Requestor) of this 1358.

You will be unable to approve a 1358 on which you are the REQUESTOR due to

segregation of duties.

Do you want to proceed (Y/N)? NO// y YES

AUTHORITY: 2//

SUB-AUTHORITY: D//

#### Classification and Sort Group 

At the CLASSIFICATION OF REQUEST: prompt, you may create reports that group requests by categories that *you* define.

At the SORT GROUP: prompt, enter a Sort Group *if* this purchase is assigned to a project, office, or some other category for which a Sort Group has been created. If this purchase doesn’t belong to a Sort Group, just press \<Enter\>. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the Sort Group and exclude all purchases that don’t belong to the Sort Group.

The DATE OF REQUEST and DATE COMMITTED fields will appear with default values.

The COST CENTER data will be displayed for review.

Per the AUTHORITY that was selected, a VENDOR may have been required. The Vendor name will appear as a default value. If CONTRACT NUMBER was required, that will also appear as a default value.

At the Select SUB-CONTROL POINT: prompt, you may associate this purchase with a category of purchases that *you* define. This allows you to group similar purchases together.

SERVICE START and END DATES will appear as default values.

The PURPOSE field will appear with the default value.

IF the ORIGINATOR OF REQUEST field was populated, it will appear as a default value.

Add COMMENTS if you like.

At the “Would You Like to Review This Request?” prompt, enter “NO” to return to the 1358 Request Menu.

At the: IS THIS REQUEST READY FOR APPROVAL? Yes//prompt, enter “YES” if you wish to permit the 1358 form to be Approved.

<span id="_Toc222496930" class="anchor"></span>Figure 130: Classification and Sort Groups

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>DATE OF REQUEST: JUN 29, 1994//</p>
<p>DATE COMMITTED: JUN 1,1994//</p></td>
</tr>
<tr class="even">
<td><p>COMMITTED (ESTIMATED) COST: 441//</p>
<p>COST CENTER: 844100 Supply</p>
<p>BOC1: 2580 Miscellaneous Contractual replace</p></td>
</tr>
<tr class="odd">
<td><p>TRANSACTION BEG BAL: 414.00</p>
<p>Select SUB-CONTROL POINT:</p></td>
</tr>
<tr class="even">
<td><p>VENDOR: IFVENDOR1,TWO//</p>
<p>VENDOR CONTRACT NUMBER: TK-987433-94//</p>
<p>SERVICE START DATE: Jun 1, 1994//</p>
<p>SERVICE END DATE: Jun 30, 1994//</p>
<p>PURPOSE:</p>
<p>1&gt; Monthly costs for June</p>
<p>ORIGINATOR OF REQUEST: IFUSER2,TWO//</p>
<p>COMMENTS:</p>
<p>1&gt;</p></td>
</tr>
<tr class="odd">
<td>Would you like to review this request? No// (No)</td>
</tr>
<tr class="even">
<td><p>Current Control Point balance: $0.00</p>
<p>Estimated cost of this request: $441.00</p>
<p>Is this request ready for approval? Yes// (Yes)</p>
<p>You are the CP Clerk (Requestor) on this 1358 transaction. Per Segregation</p>
<p>of Duties, the CP Clerk (Requestor) is not permitted to Approve the 1358.</p>
<p>Do you want to edit another request? NO//</p></td>
</tr>
</tbody>
</table>

### Create/Edit Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496931" class="anchor"></span>Figure 131: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: 1358 Request Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option: Create/Edit Authorization</p></td>
</tr>
</tbody>
</table>

#### Setup Parameters

Enter a STATION NUMBER and a CONTROL POINT.

Enter an OBLIGATION NUMBER (this is the number that Fiscal Service assigns to the 1358 form). If you do not know the obligation number, type three question marks (???) and IFCAP will list the available obligations.

<span id="_Toc222496932" class="anchor"></span>Figure 132: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 002 ANYTOWN, PA</p>
<p>Select CONTROL POINT: 022 IFVENDOR,THREE</p>
<p>Select OBLIGATION NUMBER: ?</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Answer with CONTROL POINT ACTIVITY PURCHASE ORDER/OBLIGATION NO</p>
<p>Do you want the entire CONTROL POINT ACTIVITY LIST? Y (Yes)</p>
<p>Choose from:</p>
<p>C30032 OBL C30032</p>
<p>C30033 OBL C30033</p>
<p>C30034 OBL C30034</p>
<p>C30035 OBL C30035</p>
<p>C30036 OBL C30036</p>
<p>C30037 OBL C30037</p>
<p>C30093 OBL C30093</p>
<p>C30097 OBL C30097</p>
<p>C30100 OBL C30100</p>
<p>C30101 OBL C30101</p>
<p>Select OBLIGATION NUMBER: C30033 002-93-2-022-0002 OBL C30033</p></td>
</tr>
<tr class="even">
<td>Would you like to EDIT or CREATE an Authorization: CREATE</td>
</tr>
</tbody>
</table>

#### Display Balances

IFCAP will assign a transaction number to the entry, and display the obligation amount, the fiscal balance, and the service balance.

- The fiscal balance is the dollar amount Fiscal Service shows is still available to the Control Point after Fiscal Service has obligated the entry. The fiscal balance is what the Accounting Technician will read to determine if the Control Point has sufficient funds to meet the obligation.
- The service balance is what you have committed, the dollar amount left in the Control Point minus the non-obligated committed funds.

At the “REFERENCE:” prompt, enter the recipient of the funds and any additional information that would aid in the processing of this transaction (e.g., patient name, patient Social Security Number, or Vendor).

Add COMMENTS if you like.

At the Would You Like to Edit or Create an Authorization: prompt, enter “E” to edit an authorization; “C” to create an authorization; or press \<Enter\> to return to the 1358 Request Menu.

<span id="_Toc222496933" class="anchor"></span>Figure 133: Display Balances

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>This entry has been assigned transaction number: 0003.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Obligation amount: $ 500.00 Fiscal balance: $ 500.00</p>
<p>Service balance: $ 500.00</p>
<p>AUTHORIZATION AMOUNT: (.01-999999999.99): 200</p>
<p>REFERENCE:</p>
<p>COMMENTS:</p>
<p>Would you like to EDIT or CREATE an Authorization: N</p></td>
</tr>
<tr class="even">
<td><p>If you want to EDIT an existing authorization type 'E'</p>
<p>If you want to CREATE a NEW authorization type 'C'</p>
<p>OR press &lt;RETURN&gt;</p>
<p>Would you like to EDIT or CREATE an Authorization:</p></td>
</tr>
<tr class="odd">
<td>Select OBLIGATION NUMBER:</td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### Daily Activity Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496934" class="anchor"></span>Figure 134: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: 1358 Request Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option: Daily Activity Enter/Edit</p></td>
</tr>
</tbody>
</table>

#### Setup Parameters

Enter a STATION NUMBER and a CONTROL POINT.

Enter an OBLIGATION NUMBER (this is the number that Fiscal Service assigns to 1358). If you do not know the obligation number, type three question marks (???) and IFCAP will list the available obligations.

At the Select ACTION: prompt, enter 1 to create a new bill activity, 2 to edit an existing bill activity; or 3 to quit and return to the 1358 Request Menu.

<span id="_Toc222496935" class="anchor"></span>Figure 135: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 002 ANYTOWN, PA</p>
<p>Select CONTROL POINT: 022 IFVENDOR,THREE</p>
<p>Select OBLIGATION NUMBER: ???</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>C30032 OBL C30032</p>
<p>C30033 OBL C30033</p>
<p>C30034 OBL C30034</p>
<p>C30035 OBL C30035</p>
<p>C30036 OBL C30036</p>
<p>C30037 OBL C30037</p>
<p>C30093 OBL C30093</p>
<p>C30097 OBL C30097</p>
<p>C30100 OBL C30100</p>
<p>C30101 OBL C30101</p>
<p>Select OBLIGATION NUMBER: C30033 002-93-2-022-0002 OBL C30033</p></td>
</tr>
<tr class="even">
<td><p>1 Create a NEW bill activity</p>
<p>2 Edit existing bill activity</p>
<p>3 QUIT</p>
<p>Select ACTION: (1-3): 1</p></td>
</tr>
</tbody>
</table>

#### Enter Authorization

Enter an AUTHORIZATION (this is a unique number that IFCAP uses to record individual charges against 1358). If you do not know the authorization, enter three question marks (???) to have IFCAP list the available authorizations.

IFCAP will list the amount of authorization and the current balance of the authorization. IFCAP will also list any daily records of transactions posted against the authorization.

|                                                                                                                                                   |                                                                                                                                                                                                       |                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifcap-version-5-1-control-point-official-user-s-guide/062.png) | *<u>NOTE:</u>* You must deduct the dollar amount for each invoice you receive from the balance of 1358. If you mark the 1358 as complete, you will no longer be able to edit or access that 1358. | ![](ifcap-version-5-1-control-point-official-user-s-guide/063.png) |

IFCAP will assign a number to the daily activity entry.

At the Is this the final daily activity?: prompt, enter “NO” to create another entry.

At the Daily Activity Amount: prompt, enter the amount of the activity. Do not exceed the authorization balance.

You may enter a VENDOR INVOICE NUMBER, a REFERENCE, and a DESCRIPTION if you like.

If the amount of the daily activity that you create is equal to the authorization balance, IFCAP will ask you to confirm that you want to clear the balance on the authorization and mark it as complete. IFCAP will then return to the 1358 Request Menu.

<span id="_Toc222496936" class="anchor"></span>Figure 136: Enter Authorization and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select AUTHORIZATION: ???</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>311 002-C30033-0003</p>
<p>Select AUTHORIZATION: 311 002-C30033-0003</p></td>
</tr>
<tr class="even">
<td>...Excuse me, This may take a few moments...</td>
</tr>
<tr class="odd">
<td><p>Authorization amount : $ 200.00</p>
<p>Authorization balance: $ 200.00</p>
<p>Daily Records:</p></td>
</tr>
<tr class="even">
<td><p>This DAILY ACTIVITY ENTRY has been assigned: 002-C30033-0003-1</p>
<p>Is this the final daily activity? NO// YES</p></td>
</tr>
<tr class="odd">
<td>Daily Activity AMOUNT: (.01-999999999.99): 200</td>
</tr>
<tr class="even">
<td><p>VENDOR INVOICE NUMBER:</p>
<p>REFERENCE:</p>
<p>DESCRIPTION:</p>
<p>This will zero out the balance on this authorization</p>
<p>and mark this authorization as complete</p>
<p>Do you want to continue? YES</p>
<p>REFERENCE:</p>
<p>COMMENTS:</p>
<p>Authorization balance has been reduced to ZERO, and this authorization has</p>
<p>been marked as complete.</p></td>
</tr>
<tr class="odd">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### Recalculate 1358 Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496937" class="anchor"></span>Figure 137: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: 1358 Request Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option: Recalculate 1358 Balance</p></td>
</tr>
</tbody>
</table>

#### Setup Parameters and Display

Enter a STATION NUMBER and a CONTROL POINT.

Enter an OBLIGATION NUMBER (this is the number that Fiscal Service assigns to the 1358 form). If you do not know the obligation number, type three question marks (???) and IFCAP will list the available obligations.

Once you enter an obligation number, IFCAP will list the Fund Control Point that funds it and the current balance and will return to the 1358 Request Menu.

<span id="_Toc222496938" class="anchor"></span>Figure 138: Setup Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 002 ANYTOWN, PA</p>
<p>Select CONTROL POINT: 022 IFVENDOR</p>
<p>Select OBLIGATION NUMBER: ???</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>99999681 999-C45008 -- 1358 Obligated - 1358 FCP: 102 $ 100.00</p>
<p>99999696 999-C45007 -- 1358 Obligated - 1358 FCP: 102 $ 1000.00</p>
<p>99999710 999-C45006 -- 1358 Obligated - 1358 FCP: 101 $ 10000.00</p>
<p>99999720 999-C45901 -- 1358 Obligated - 1358 FCP: 102 $ 10000.00</p>
<p>99999730 999-C45005 -- 1358 Obligated - 1358 FCP: 101 $ 25000.00</p>
<p>99999731 999-C45004 -- 1358 Obligated - 1358 FCP: 103 $ 100000.00</p>
<p>99999732 999-C45003 -- 1358 Obligated - 1358 FCP: 201 $ 13500.00</p>
<p>99999736 999-C45002 -- 1358 Obligated - 1358 FCP: 9988 $ 100000.00</p>
<p>99999762 999-C45001 -- 1358 Obligated - 1358 FCP: 101 $ 10000.00</p>
<p>99999773 999-C00001 -- 1358 Obligated - 1358 FCP: 102 $ 25000.00</p>
<p>99999802 002-C40003 -- 1358 Obligated - 1358 FCP: 019 $ 200.00</p>
<p>Select OBLIGATION NUMBER: 99999696 999-C45007 -- 1358 Obligated - 1358</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>FCP: 102 $ 1000.00</p>
<p>...OK? Yes// (Yes)</p></td>
</tr>
</tbody>
</table>

### Display 1358 Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496939" class="anchor"></span>Figure 139: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: 1358 Request Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358s with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option: Display 1358 Balance</p></td>
</tr>
</tbody>
</table>

#### Setup Parameters and Display

Enter a STATION NUMBER and a CONTROL POINT.

Enter an OBLIGATION NUMBER (this is the number that Fiscal Service assigns to the 1358 form). If you do not know the obligation number, type three question marks (???) and IFCAP will list the available obligations.

Once you enter an obligation number, IFCAP will list the Fund Control Point that funds it and the current balance and will return to the 1358 Request Menu.

<span id="_Toc222496940" class="anchor"></span>Figure 140: Setup Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 002 ANYTOWN, PA</p>
<p>Select CONTROL POINT: 022 IFVENDOR</p>
<p>Select OBLIGATION NUMBER: ???</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>99999681 999-C45008 -- 1358 Obligated - 1358 FCP: 102 $ 100.00</p>
<p>99999696 999-C45007 -- 1358 Obligated - 1358 FCP: 102 $ 1000.00</p>
<p>99999710 999-C45006 -- 1358 Obligated - 1358 FCP: 101 $ 10000.00</p>
<p>99999720 999-C45901 -- 1358 Obligated - 1358 FCP: 102 $ 10000.00</p>
<p>99999730 999-C45005 -- 1358 Obligated - 1358 FCP: 101 $ 25000.00</p>
<p>99999731 999-C45004 -- 1358 Obligated - 1358 FCP: 103 $ 100000.00</p>
<p>99999732 999-C45003 -- 1358 Obligated - 1358 FCP: 201 $ 13500.00</p>
<p>99999736 999-C45002 -- 1358 Obligated - 1358 FCP: 9988 $ 100000.00</p>
<p>99999762 999-C45001 -- 1358 Obligated - 1358 FCP: 101 $ 10000.00</p>
<p>99999773 999-C00001 -- 1358 Obligated - 1358 FCP: 102 $ 25000.00</p>
<p>99999802 002-C40003 -- 1358 Obligated - 1358 FCP: 019 $ 200.00</p>
<p>Select OBLIGATION NUMBER: 99999696 999-C45007 -- 1358 Obligated - 1358</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>FCP: 102 $ 1000.00</p>
<p>...OK? Yes// (Yes)</p></td>
</tr>
<tr class="even">
<td><p>999-C45007 OBLIGATION BALANCES</p>
<p>OBLIGATION AMOUNT: $ 1000.00 SERVICE BALANCE: $ 0.00</p>
<p>LIQUIDATION BALANCE: $ 1000.00 TOTAL LIQUIDATIONS: $ 0.00</p>
<p>AUTHORIZATION BALANCE(S):</p>
<p>999-C45007-0002 AMOUNT: $ 1000.00 BALANCE: $ 0.00</p>
<p>AUTHORIZATION TOTAL: $ 1000.00</p></td>
</tr>
<tr class="odd">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### List 1358's with Open Authorizations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496941" class="anchor"></span>Figure 141: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: 1358 Request Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option: List 1358's with Open Authorizations</p></td>
</tr>
</tbody>
</table>

#### Setup Parameters and Display

Enter a STATION NUMBER, FISCAL YEAR and FISCAL QUARTER.

Enter a CONTROL POINT. If you do not know the Control Point, enter three question marks (???) and IFCAP will list the available Control Points.

IFCAP will print or display the *Open 1358 Daily Record*, listing each authorization, the balance remaining on the authorization, and the reference. After printing or displaying the record, IFCAP will return to the 1358 Request Menu.

<span id="_Toc222496942" class="anchor"></span>Figure 142: Setup Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 002 ANYTOWN, PA</p>
<p>Select FISCAL YEAR: 94//</p>
<p>Select QUARTER: 4//</p>
<p>Select CONTROL POINT: 022 IFVENDOR</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DEVICE: LAT RIGHT MARGIN: 80//</td>
</tr>
<tr class="even">
<td><p>OPEN 1358 DAILY RECORDS JUL 8,1994 17:29 PAGE 1</p>
<p>AUTHORIZATION</p>
<p>AUTHORIZATION # BALANCE REFERENCE</p>
<p>--------------------------------------------------------------------------------</p>
<p>002-C30032-0002 0.00 IFVENDOR1,SIX</p>
<p>002-C30032-0003 500.00 IFVENDOR1,SEVEN</p>
<p>002-C30034-0002 0.00 IFVENDOR1,SIX</p>
<p>002-C30035-0002 25.00 IFVENDOR1,SIX</p>
<p>002-C30036-0002 0.00 IFVENDOR1,SIX</p>
<p>002-C30036-0003 500.00 IFVENDOR1,SEVEN</p>
<p>002-C30093-0002 500.00 IFVENDOR1,SIX</p>
<p>002-C30097-0005 2.50 TRAINING ENTRY</p>
<p>002-C30097-0006 20.00 ENTERY 2</p>
<p>002-C30101-0002 0.11 ELECTRIC</p>
<p>002-C30101-0003 50.00 WATER</p>
<p>002-C30101-0004 100.00 FUEL</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option:</p></td>
</tr>
</tbody>
</table>

### Print 1358

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496943" class="anchor"></span>Figure 143: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: 1358 Request Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option: Print 1358</p></td>
</tr>
</tbody>
</table>

#### Setup Parameters

Enter the STATION NUMBER and a CONTROL POINT number. Enter an OBLIGATION NUMBER (this is number that Fiscal Service assigns to the 1358 form). If you do not know the obligation number, enter three question marks (???) to have IFCAP list the available obligations. You may also create a report that includes what the requestor entered in the DESCRIPTION field, and/or print the daily records for each authorization.

<span id="_Toc222496944" class="anchor"></span>Figure 144: Setup Parameters

Select STATION NUMBER: 002// ANYTOWN, PA

Select CONTROL POINT: 022 IFVENDOR //

Select OBLIGATION NUMBER: ???

CHOOSE FROM:

C30032 OBL C30032

C30033 OBL C30033

C30034 OBL C30034

C30035 OBL C30035

C30036 OBL C30036

C30037 OBL C30037

C30093 OBL C30093

C30097 OBL C30097

C30100 OBL C30100

C30101 OBL C30101

Select OBLIGATION NUMBER: C30033 002-93-2-022-0002 OBL C30033

Would you like to print the Description field for each 1358 Daily Record entry? No// (No)

Would you like to print the daily records for each authorization? No//

DEVICE: HOME// LAT RIGHT MARGIN: 80//

#### Display

IFCAP will print each 1358 for the obligation number you selected, with the transaction number of each 1358 on the upper-left hand corner of the 1358 form. Enter a caret (^) at the “Select STATION NUMBER:” prompt to return to the 1358 Request Menu.

<span id="_Toc222496945" class="anchor"></span>Figure 145: Display Example

Select STATION NUMBER: 999//

Select CONTROL POINT: 110 STUFF .01//

Select OBLIGATION NUMBER:C15002

Would you like to print the Description field for each 1358 Daily Record entry?

No// (No)

Would you like to print the daily records for each authorization? NO//

DEVICE: HOME// TELNET Right Margin: 80//

999-11-1-110-0013 OCT 15, 2010@16:12:38 PAGE 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:

COLLEGE OF SIMPLE PATHOLOGY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Originator of Request:

Requestor: \|Date Requested: \|Obligation No.:

IFUSER,SEVEN \|OCT 05, 2010 \| 999-C15002

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Vendor: \|Contract Number:

A VENDOR NAME \|GS-98-99827F

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Name and Title Approving Off.: \|Signature: \|Date Signed:

IFUSER,THREE \|/ES/IFUSER THREE \|OCT 05, 2010@14:49:30

SERVICE CHIEF \| \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FUND CERTIFICATION: The supplies and services listed on this request are

properly chargeable to the following allotments, the available balances of

which are sufficient to cover the cost thereof, and funds have been obligated.

Press return to continue, "^" to exit:

999-11-1-110-0013 999-C15002 PAGE 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358OBLIGATION OR CHANGE: STANDARDIZED OBLIGATIONS

COLLEGE OF SIMPLE PATHOLOGY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Appropriation & Acct. Symbols: \|Obligated By: \|Date Obligated:

999-3610160-110-842100-2580 010042116 \|/ES/IFACCT TECH2 \|OCT 05, 2010

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORITY: 3 SUB: B

SERVICE START DATE: 10/01/10 SERVICE END DATE: 10/31/10

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Purpose:

MONTHLY COSTS FOR OCT.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Purpose: SERVICE START DATE: 10/01/10 SERVICE END DATE: 10/31/10

MONTHLY COSTS FOR OCT.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ESTIMATED OBLIGATION RECAP

DATE REF# CPA# AMOUNT BALANCE

10/05 0001 999-11-1-110-0013 \$ 556.00 \$ 556.00

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORIZATION & ORDER RECORD LIQUIDATION RECORD

AUTH. AUTH. CUMULATIVE UNLIQ

DATE SEQ# REFERENCE AMOUNT BALANCE AUTH. AMT. LIQUID BAL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TOTALS \$ 0.00 \$ 0.00 \$ 0.00 \$ 556.00

VA FORM 4-1358a-ADP (NOV 1987)

|     |
|-----|

### Obligated 1358s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Process a Request Menu.

<span id="_Toc222496946" class="anchor"></span>Figure 146: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu ...</p>
<p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu ...</p>
<p>Cancel Transaction with Permanent Number</p>
<p>Requestor's Menu ...</p>
<p>Item Display</p>
<p>Vendor Display</p>
<p>Outstanding Approved Requests Report</p>
<p>Transaction Report – eCMS/IFCAP</p>
<p>Select Process a Request Menu Option: 1358 Request Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p>
<p>Select 1358 Request Menu Option: Print Obligated 1358s</p></td>
</tr>
</tbody>
</table>

#### Parameters and Display

Enter a date range and device to obtain a list of purchase orders from obligated 1358s with a dollar value of \$0 and higher. Your previous entries for the START and GO TO P.O. DATES will appear as the defaults.

The report includes information such as P.O. \#, date and amount; requestor; and vendor and contract information, if it was entered when the 1358s were created.

This option should be printed at 132 columns.

<span id="_Toc222496947" class="anchor"></span>Figure 147: Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>* Previous selection: P.O. DATE from Oct 1,2005 to Oct 31,2005@24:00</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>START WITH P.O. DATE: Oct 1,2005// (OCT 01, 2005)</p>
<p>GO TO P.O. DATE: Oct 31,2005// (OCT 31, 2005)</p>
<p>DEVICE: HOME// LAT RIGHT MARGIN: 80// 132</p></td>
</tr>
<tr class="even">
<td><p>PROCUREMENT &amp; ACCOUNTING TRANSACTIONS LIST (OBLIGATED 1358s) FEB 6,2006 13:13 PAGE 1</p>
<p>BUSINESS</p>
<p>PURCHASE VENDOR CONTRACT TYPE SOCIOECONOMIC TOTAL</p>
<p>ORDER NUMBER P.O. DATE VENDOR NUMBER (FPDS) GROUP (FPDS) AMOUNT REQUESTOR</p>
<p>SERVICE START DATE SERVICE END DATE</p>
<p>AUTHORITY</p>
<p>SUB-AUTHORITY</p>
<p>---------------------------------------------------------------------------------------------------------------</p>
<p>442-G67001 OCT 3,2005 IFVENDOR THREE LARGE OO 987 IFREQUESTOR,ONE</p>
<p>442-C66002 OCT 19,2005 IFVENDOR THREE V797P-2003 LARGE OO 2000 IFREQUESTOR,TWO</p>
<p>999-C15004 OCT 12,2010 SAMPLE COMPANY BUSINESS SY 797P-22233 LARGE OO 500 IFREQUESTOR,ONE</p>
<p>10/01/10 10/30/10</p>
<p>18 REGULATED UTILITIES</p>
<p>999-C00024 OCT 14,2010 SIMPLE MEDICAL/SURGITEK SMALL OO 77.77 TEST,CPCCLR</p>
<p>10/14/10 11/13/10</p>
<p>3 STANDARDIZED OBLIGATIONS</p>
<p>D DENVER ACQUISITION AND LOGISTICS CENTER SERVICES AND SUPPLIES</p></td>
</tr>
</tbody>
</table>

## Options on the Display Control Point Activity Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purchase Order Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official Menu, select Display Control Point Activity Menu.

<span id="_Toc222496948" class="anchor"></span>Figure 148: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option: Purchase Order Status</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Setup Parameters

Enter a CONTROL POINT and a PURCHASE ORDER NUMBER. If you do not know the purchase order number, enter three question marks (???) at the prompt and IFCAP will list the available purchase orders.

<span id="_Toc222496949" class="anchor"></span>Figure 149: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Select CONTROL POINT: 101 LAB TESTING 101//</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select PURCHASE ORDER NUMBER: ???</td>
</tr>
<tr class="even">
<td><p>CHOOSE FROM:</p>
<p>999-A40001 11-10-93 CI Ordered and Obligated (Amended) FCP: 101 $ 300.00</p>
<p>999-A40002 11-17-93 ST Complete Order Received But Not Ob FCP: 101 $ 76.10</p>
<p>999-A40003 11-22-93 ST Complete Order Received But Not Ob FCP: 101 $ 12.30</p>
<p>999-A40004 11-22-93 ST Complete Order Received But Not Ob FCP: 101 $ 10.00</p>
<p>999-A40005 11-24-93 ST Partial Order Received (Amended) FCP: 101 $ 33.00</p>
<p>999-A40006 11-24-93 ST Complete Order Received FCP: 101 $ 12.30</p>
<p>999-A40007 11-24-93 ST Complete Order Received FCP: 101 $ 25.00</p>
<p>999-A40008 12-01-93 ST Cancelled Order FCP: 101 $ 0.00</p>
<p>999-A40009 12-01-93 ST Partial Order Received (Amended) FCP: 101 $ 20.00</p>
<p>999-A40010 12-02-93 ST Partial Order Received FCP: 101 $ 30.00</p>
<p>999-A40011 12-02-93 ST Ordered and Obligated FCP: 101 $ 60.00</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Select PURCHASE ORDER NUMBER: A40004 999-A40004 11-22-93 ST Complete Order Received But Not Ob</p>
<p>FCP: 101 $ 10.00</p></td>
</tr>
</tbody>
</table>

#### Status Display

IFCAP will list the status of the purchase order you select and the corresponding Fund Control Point. You may look at a short display of the purchase order or review the entire purchase order. Enter a caret (^) at the Select Control Point: prompt to return to the Display Control Point Activity Menu.

<span id="_Toc222496950" class="anchor"></span>Figure 150: Status Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Purchase Order Status: Complete Order Received But Not Oblig.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Would you like the purchase order display? No// (No)</td>
</tr>
<tr class="even">
<td>Would you like to review the entire purchase order? No// (No)</td>
</tr>
<tr class="odd">
<td>Enter information for another report or an uparrow to return to the menu.</td>
</tr>
<tr class="even">
<td><p>Select CONTROL POINT: 101 LAB TESTING 101// ^</p>
<p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option:</p></td>
</tr>
</tbody>
</table>

### Temporary Transaction Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official Menu, select Display Control Point Activity Menu.

<span id="_Toc222496951" class="anchor"></span>Figure 151: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option: Temporary Transaction Listing</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Setup Parameters

Enter a CONTROL POINT. If you do not know the Control Point, enter three question marks (???) and IFCAP will list the available Control Points.

IFCAP will list all of the temporary transactions for the Control Point or will only list transactions that were created on or after a date that you specify at the START WITH DATE OF REQUEST: prompt.

<span id="_Toc222496952" class="anchor"></span>Figure 152: Set Parameters

| Select CONTROL POINT: 101 LAB TESTING 101// |
|---------------------------------------------|
| START WITH DATE OF REQUEST: FIRST//         |
| DEVICE: LAT RIGHT MARGIN: 80//              |

#### Display

IFCAP will generate a list of each temporary transaction, the date it was created, the requestor that created it, the vendor (if any) the first item on the request, and the amount of the transaction. After generating the list, IFCAP will return to the Display Control Point Activity Menu.

<span id="_Toc222496953" class="anchor"></span>Figure 153: Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>TEMPORARY TRANSACTION LISTING - CONTROL POINT 101 LAB TESTING 101</p>
<p>JUL 8,1994 17:54 PAGE 1</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TEMPORARY DATE OF FIRST LINE ITEM COMM.</p>
<p>TRANSACTION # REQUEST REQUESTOR VENDOR DESCRIPTION COST</p>
<p>-----------------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>CONTROL POINT: 101 LAB TESTING 101</p>
<p>WER246 APR 19,1994 IFUSER3,ONE IFVENDOR1,TWO 40.00</p>
<p>MAVIS627 JUN 27,1994 IFUSER3,TWO 99999.27</p>
<p>MCGJUN27 JUN 27,1994 IFUSER3,TWO IFVENDOR1,TWO 23.45</p>
<p>KMB601 JUN 27,1994 IFVENDOR2,ONE 10.00</p>
<p>KLIMBIE2 JUN 30,1994 IFUSER3,THREE IFVENDOR2,ONE 10.00</p>
<p>IFUSER2,FIVE90 JUN 30,1994 10.00</p>
<p>KMN5 JUL 5,1994 IFUSER3,FOUR IFCENTRAL TEST ITEM #11 48.00</p>
<p>KMBZ2 JUL 6,1994 IFUSER3,THREE IFVENDOR2,ONE TEST ITEM #25 12.23</p>
<p>KMN7 JUL 14,1994 IFUSER3,THREE IFVENDOR2,ONE TEST ITEM #17 23.84</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option:</p></td>
</tr>
</tbody>
</table>

### Transaction Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official Menu, select Display Control Point Activity Menu.

<span id="_Toc222496954" class="anchor"></span>Figure 154: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option: Transaction Status Report</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Setup Parameters

<span id="_Toc222496955" class="anchor"></span>Figure 155: Set Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>...OK? Yes// (Yes)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ???</td>
</tr>
<tr class="even">
<td><p>Attempting lookup in transaction file.</p>
<p>Attempting lookup using 101 LAB TESTING 101 (CONTROL POINT)</p></td>
</tr>
<tr class="odd">
<td><p>1 101 LAB TESTING 101 999-94-4-101-0325 OBL SUPPLY IFVENDOR,EIGHT TEST ITEM #17</p>
<p>2 101 LAB TESTING 101 999-94-4-101-0324 OBL SUPPLY IFVENDOR,EIGHT TEST ITEM #17</p>
<p>3 101 LAB TESTING 101 999-94-4-101-0323 ADJ C45003</p>
<p>4 101 LAB TESTING 101 999-94-4-101-0322 ADJ C45003</p>
<p>5 101 LAB TESTING 101 999-94-4-101-0321 ADJ C45040</p></td>
</tr>
<tr class="even">
<td><p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: 3 999-94-4-101-0323</p></td>
</tr>
<tr class="odd">
<td>DEVICE: HOME// LAT RIGHT MARGIN: 80//</td>
</tr>
</tbody>
</table>

#### Display

IFCAP will list the type of transaction, the vendor (if any), the purchase order number, the amount of the adjustment used to fund the transaction (Adjustment Amount), and other classification data for the transaction. Enter a caret (^) at the “Select Control Point Activity Transaction Number:” prompt to return to the Display Control Point Activity Menu.

<span id="_Toc222496956" class="anchor"></span>Figure 156: Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ADJUSTMENT TRANSACTION STATUS DISPLAY JUL 8,1994@17:56:16</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Transaction Number: 999-94-4-101-0323 Transaction Type: ADJUSTMENT</td>
</tr>
<tr class="even">
<td><p>Vendor:</p>
<p>Purchase Order/Obligation No.: C45003 Adjustment $ Amount: $100.00</p>
<p>Date Obl.Adjusted: Accounting Data: 3640151.001 3040/21-25</p>
<p>FMS $ Amount: $0.00 FMS Date:</p>
<p>FMS Transaction Code:</p>
<p>Sort Group: Classification of Request:</p></td>
</tr>
<tr class="odd">
<td><p>Enter information for another report or an uparrow to return to the menu.</p>
<p>OBLIGATION TRANSACTION STATUS DISPLAY AUG 6,2013@23:55:39</p>
<p>Transaction Number: 999-13-3-110-0029 Transaction Type: OBLIGATION</p>
<p>A&amp;MM Status: Returned to Service by eCMS (P&amp;C)</p>
<p>Temporary Trans. Number:</p>
<p>Form Type: REPETITIVE AND NON-REP ORDER</p>
<p>Date of Request: APR 1,2013 Date Required: APR 11,2013</p>
<p>Est. Delivery Date: Date Received:</p>
<p>Vendor: IFVENDOR1, INC. P.O. Vendor:</p>
<p>Committed (Estimated) Cost: $39.98 Date Committed: APR 1,2013</p>
<p>Obligated (Actual) Cost: $0.00 Date Obligated:</p>
<p>Purchase Order/Obligation No.: Accounting Data: 3630160</p>
<p>FMS $ Amount: $0.00 FMS Date:</p>
<p>FMS Transaction Code:</p>
<p>Return to Service Comments: This 2237 needs price adjustment.</p>
<p>Comments:</p>
<p>OBLIGATION TRANSACTION STATUS DISPLAY AUG 6,2013@23:58:16</p>
<p>Transaction Number: 999-13-3-110-0029 Transaction Type: OBLIGATION</p>
<p>Originator of Request: CPUSER, ONE</p>
<p>Requestor: REQUESTOR, TWO Form Type: REPETITIVE AND NON-REP ORDER</p>
<p>Requestor's Title: THE BOSS Requesting Service: IRMGMT (IRM)</p>
<p>Approving Official: Inventory Dist. Point: GIP2 PRIMARY</p>
<p>Appr. Official's Title: Cost Center: 842100 Fiscal</p>
<p>Date Signed (Approved):</p>
<p>Justification: THE ITEMS ARE REQUIRED.</p>
<p>Deliver To/Location: COMPUTER ROOM</p>
<p>Classification of Request:</p>
<p>Sort Group:</p>
<p>Return to Service Comments:</p>
<p>This 2237 needs price adjustment.</p>
<p>Would you like to review the item information for this request? No//</p></td>
</tr>
</tbody>
</table>

### Running Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official Menu, select Display Control Point Activity Menu.

<span id="_Toc222496957" class="anchor"></span>Figure 157: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option: Running Balances</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Setup Parameters

Enter a FISCAL YEAR: and a fiscal QUARTER: at the prompts. Enter a CONTROL POINT. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will list the available Control Points.

Enter YES at the Would you like a summary report (bottom line balances only)?: prompt to see only the current balance for the Control Point; enter NO to see all of the line items that cause this balance.

<span id="_Toc222496958" class="anchor"></span>Figure 158: Set Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select FISCAL YEAR: 94//</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select QUARTER: 4//</td>
</tr>
<tr class="even">
<td>Select CONTROL POINT: 101 LAB TESTING 101//</td>
</tr>
<tr class="odd">
<td><p>Summary Balances Report Only? No// Y (Yes)</p>
<p>DEVICE: HOME// LAT RIGHT MARGIN: 80//</p></td>
</tr>
<tr class="even">
<td><p>STATION: 999 FUND CONTROL POINT: 101 LAB TESTING 101</p>
<p>FISCAL YEAR: 94 QTR: 3</p></td>
</tr>
<tr class="odd">
<td>Press return to continue, uparrow (^) to exit:</td>
</tr>
</tbody>
</table>

#### Display Balances

IFCAP will list the total amount of funds available to the Control Point Official (Control Point Official's Balance), how much of that money has not been obligated for a purchase, and how much has been committed to pay for a purchase. You may create another running balance report or return to the Control Point Activity Menu.

<span id="_Toc222496959" class="anchor"></span>Figure 159: Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Control Point Balance - 999-94-4-110- LAB OCT 13,1994@13:39:10 PAGE 1</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FISCAL</p>
<p>FYQSeq# TXN OBL # AP/OB DT COMM $AMT CP $BAL OBL $AMT UNOBL $BAL</p>
<p>-----------------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>SEP 16,1994 438LG2000 SO 12.50 221953.38 227073.40</p>
<p>FMS transaction total for this quarter: $12.50</p>
<p>=============================================================================</p></td>
</tr>
<tr class="odd">
<td><p>Balance Summary 1st Quarter 2nd Quarter 3rd Quarter 4th Quarter</p>
<p>Actual CP Bal: 0.00 100209.96 0.00 0.00</p>
<p>Actual Fiscal Bal: 0.00 101001.00 0.00 0.00</p>
<p>Tot Commit, not Obl: 0.00 791.04 0.00 0.00</p></td>
</tr>
<tr class="even">
<td><p>SECTION 1 CODES # - cancelled order * - order not obligated or signed</p>
<p>@ - purchase card order for reconciliation</p>
<p>&amp; - reconciled order ready for approval</p>
<p>SECTION 2 CODES</p>
<p>@ - purchase card CC transaction is not reconciled</p>
<p>The symbols '*','@', and '&amp;' indicate incomplete items.</p>
<p>Please take the necessary steps to clear these items.</p></td>
</tr>
<tr class="odd">
<td>Would you like to run another running balances report? No// (No)</td>
</tr>
<tr class="even">
<td><p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option:</p></td>
</tr>
</tbody>
</table>

### Item History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Item History option allows you to review the purchase history of an item before creating a new request.

#### Menu Path

From the Control Point Official Menu, select Display Control Point Activity Menu.

<span id="_Toc222496960" class="anchor"></span>Figure 160: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option: Item History</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Setup Parameters

Enter a CONTROL POINT. Enter the name or item master number of the item you want to review. If you do not know the name or item master number of the item, enter three question marks (???) at the prompt and IFCAP will list the available items.

<span id="_Toc222496961" class="anchor"></span>Figure 161: Set Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select CONTROL POINT: 101 LAB TESTING 101//</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select one of the following:</p>
<p>L Last 5 Purchase Orders</p>
<p>D Date Range</p>
<p>Select ITEM HISTORY Viewing Method: L// ast 5 Purchase Orders</p></td>
</tr>
<tr class="even">
<td>Select ITEM MASTER NUMBER: ???</td>
</tr>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>102 102 PEN SET</p>
<p>103 103 TRASH CAN</p>
<p>104 104 NAILS</p>
<p>105 105 LADDER</p>
<p>106 106 SURGICAL GLOVES</p>
<p>107 107 NEEDLES</p>
<p>108 108 THERMOMETERS</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td>Select ITEM MASTER NUMBER: 103 TRASH CAN</td>
</tr>
</tbody>
</table>

#### Display

IFCAP will list the last five purchase orders in the system that includes this item. You may look at another Item History, or return to the Display Control Point Activity Menu.

<span id="_Toc222496962" class="anchor"></span>Figure 162: Display Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ITEM HISTORY</p>
<p>Item Number: 103 Description: TRASH CAN</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Quantity</p>
<p>Previously Unit of Quantity</p>
<p>Date Ordered PO Number Received Purchase Unit Cost Total Cost Ordered</p>
<p>-----------------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>MAY 31,1994 999-B40054 1 EA 9.00 90.00 10</p>
<p>Vendor: IFVENDOR1,THREE</p>
<p>MAY 3,1994 999-A40680 EA 10.00 20.00 2</p>
<p>Vendor: IFVENDOR1,FOUR</p>
<p>MAY 2,1994 999-A40674 EA 10.00 20.00 2</p>
<p>Vendor: IFVENDOR1,FOUR</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Would you like to look at another Item History? No// (No)</td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option:</p></td>
</tr>
</tbody>
</table>

### PPM Status of Transactions Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official Menu, select Display Control Point Activity Menu.

<span id="_Toc222496963" class="anchor"></span>Figure 163: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option: PPM Status of Transactions Repor</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Setup Parameters

Enter a FISCAL YEAR: and a fiscal QUARTER: at the prompts. Enter a CONTROL POINT. If you do not know the Control Point, enter three question marks (???) and IFCAP will list the available Control Points.

<span id="_Toc222496964" class="anchor"></span>Figure 164: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select FISCAL YEAR: 94//</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select QUARTER: 4//</td>
</tr>
<tr class="even">
<td>Select CONTROL POINT:// ???</td>
</tr>
<tr class="odd">
<td><p>CHOOSE FROM:</p>
<p>11 011 CONSULTANT &amp; ATTENDING</p>
<p>33 033 337 Pharmacy Test</p>
<p>101 101 LAB TESTING 101</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td>Select CONTROL POINT: // 101 LAB TESTING 101</td>
</tr>
</tbody>
</table>

#### Display

IFCAP will display the *PPM Transaction Status Report,* listing each transaction, whether funds have been obligated for the transaction, the cost of the transaction, the date the items or services are required, and the date that funds were obligated for the transaction. After printing the report, IFCAP will return to the Display Control Point Activity Menu.

<span id="_Toc222496965" class="anchor"></span>Figure 165: Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PPM TRANSACTION STATUS REPORT - CP 101 JUL 8,1994@18:03:37 PAGE 1</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PO/OBL# COMM. OBLIG.</p>
<p>2237# (EST) COST (ACT) COST DATE REQ. DATE OBL.</p>
<p>STATUS</p>
<p>-----------------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>999-011-C41344-000035 OBL 440.00 June 16,1994 June 01, 1994</p>
<p>END OF REPORT</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p>
<p>Select Display Control Point Activity Menu Option:</p></td>
</tr>
</tbody>
</table>

## Options in the Record Date Received by Service Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Single Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Record Date Received by Service Menu.

#### Setup Parameters

Enter the Station Number. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points.

<span id="_Toc222496966" class="anchor"></span>Figure 166: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Single Transaction</p>
<p>All Transactions with Final Partials</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select Record Date Received by Service Menu Option: Single Transaction</td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>Select STATION NUMBER: 999// ANYCITY,ANYSTATE</p>
<p>Select CONTROL POINT: 022 IFVENDOR //</p></td>
</tr>
</tbody>
</table>

#### Select Transaction Number

Enter a transaction number. If you do not know the transaction number, enter three question marks and IFCAP will list the available transactions. Enter the date that the requestor received the goods or services at the Date Received: prompt. Press \<Enter\> at the Select Transaction or P.O. Number: prompt to return to the Record Date Received by Service Menu.

<span id="_Toc222496967" class="anchor"></span>Figure 167: Select Transaction Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select TRANSACTION or P.O. NUMBER: ???</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Attempting lookup in transaction file.</p>
<p>Attempting lookup using 022 IFVENDOR (CONTROL POINT)</p>
<p>1 022 IFVENDOR,THREE 999-94-4-022-0011 OBL IFVENDOR,EIGHT CORN-CANNED-#10</p>
<p>2 022 IFVENDOR,THREE 999-94-4-022-0010 OBL IFVENDOR,EIGHT CORN-CANNED-#10</p>
<p>3 022 IFVENDOR,THREE 999-94-4-022-0008 OBL IFVENDOR,TWO</p>
<p>4 022 IFVENDOR,THREE 999-94-4-022-0009 OBL IFVENDOR,ONE</p>
<p>This is where the "Description" goes.</p>
<p>5 022 IFVENDOR,THREE 999-94-4-022-0006 OBL</p></td>
</tr>
<tr class="even">
<td><p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p>
<p>CHOOSE 1-5: 1 999-94-4-022-0011</p></td>
</tr>
<tr class="odd">
<td><p>999-94-4-022-0011 P.O.:</p>
<p>DATE RECEIVED: T (JUL 09, 1994)</p></td>
</tr>
<tr class="even">
<td><p>Select TRANSACTION or P.O. NUMBER:</p>
<p>Single Transaction</p>
<p>All Transactions with Final Partials</p>
<p>Select Record Date Received by Service Menu Option:</p></td>
</tr>
</tbody>
</table>

### All Transactions with Final Partials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Control Point Official’s Menu, select Record Date Received by Service Menu.

<span id="_Toc222496968" class="anchor"></span>Figure 168: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Single Transaction</p>
<p>All Transactions with Final Partials</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Select Record Date Received by Service Menu Option: All Transactions with Final Partials</td>
</tr>
</tbody>
</table>

#### Setup Parameters

Enter a STATION NUMBER: and a CONTROL POINT: at the appropriate prompts. If you do not know the Control Point, enter three question marks (???) at the prompt and IFCAP will display the available Control Points. IFCAP will record all the transactions in the Control Point as received and display \*\*\*LAST TRANSACTION\*\*\* when IFCAP is finished processing the changes. IFCAP will return to the Record Date Received by Service Menu.

<span id="_Toc222496969" class="anchor"></span>Figure 169: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER: 999// ANYCITY,ANYSTATE</p>
<p>Select CONTROL POINT: 022 IFVENDOR //</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>......</p>
<p>999-00-3-060-0040 P.O.: 123456</p>
<p>DATE RECEIVED: T (JUL 09, 1994)</p>
<p>..........</p>
<p>999-00-3-060-0017 P.O.: P91001 PURCHASE CARD P.O.DATE: JUL 09, 1994</p>
<p>DATE RECEIVED:</p>
<p>...................</p>
<p>*LAST TRANSACTION*</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>Single Transaction</p>
<p>All Transactions with Final Partials</p>
<p>Select Record Date Received by Service Menu Option:</p></td>
</tr>
</tbody>
</table>

# Menu Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the options assigned to Control Point Clerks in the default IFCAP configuration. You may have some options that are not listed here, because you have additional responsibilities beyond the typical responsibilities of a Control Point Clerk. You may not have all of the options listed below. Main menu options are flush left. Subordinate options are spaced to the right. For example, if you wanted to use the “Copy a Transaction” option, you would select “Control Point Official's Menu,” then “Process a Request Menu,” then “Copy a Transaction.” To add any of the options listed below to your menus, contact your local Information Resources Management (IRM) service.

<span id="_Toc222496970" class="anchor"></span>Figure 170: Control Point Official’s Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Control Point Official's Menu</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Approve Requests</p>
<p>Requests Ready for Approval List</p>
<p>Process a Request Menu</p>
<p>New 2237 (Service) Request</p>
<p>Edit a 2237 (Service)</p>
<p>Copy a Transaction</p>
<p>1358 Request Menu</p>
<p>New 1358 Request</p>
<p>Increase/Decrease Adjustment</p>
<p>Edit 1358 Request</p>
<p>Create/Edit Authorization</p>
<p>Daily Activity Enter/Edit</p>
<p>Display 1358 Balance</p>
<p>List 1358's with Open Authorizations</p>
<p>Print 1358</p>
<p>Print Obligated 1358s</p>
<p>Recalculate 1358 Balance</p></td>
</tr>
<tr class="even">
<td><p>Print/Display Request Form</p>
<p>Change Existing Transaction Number</p>
<p>Repetitive Item List Menu</p>
<p>New Repetitive Item List (Enter)</p>
<p>Edit Repetitive Item List Entry</p>
<p>Delete Repetitive Item List Entry</p>
<p>Print/Display Repetitive Item List Entry</p>
<p>Generate Requests From Repetitive Item List Entry</p>
<p>Cancel Transaction with Permanent Number</p></td>
</tr>
<tr class="odd">
<td><p>Display Control Point Activity Menu</p>
<p>Purchase Order Status</p>
<p>Transaction Status Report</p>
<p>Running Balances</p>
<p>Temporary Transaction Listing</p>
<p>Item History</p>
<p>PPM Status of Transactions Report</p>
<p>CP Entered, Not Approved Requests</p></td>
</tr>
<tr class="even">
<td><p>Funds Control Menu</p>
<p>Enter FCP Adjustment Data</p>
<p>Assign Ceiling to Sub-Control Points</p>
<p>Correct Sub-Control Point Amounts</p>
<p>Recalculate Fund Control Point Balance</p>
<p>Funds Control Reports Menu</p>
<p>Quarterly Report</p>
<p>Ceiling Report</p>
<p>Audit Transaction List</p>
<p>Sort Group Report</p>
<p>Classification of Request Report</p>
<p>Cost Center Totals</p>
<p>BOC Totals</p>
<p>Sub-Control Point Report</p>
<p>Reconciliation of PO/Sub-CP Dollar Amounts</p>
<p>BOC Detail Totals</p>
<p>FMS Transaction Data</p></td>
</tr>
<tr class="odd">
<td><p>Status of Requests Reports Menu</p>
<p>Print/Display Request Form</p>
<p>Status of All Obligation Transactions</p>
<p>Requests Ready for Approval List</p>
<p>PO with Associated Transactions</p>
<p>Record Date Received by Service Menu</p>
<p>Single Transaction</p>
<p>All Transactions with Final Partials</p>
<p>Enter/Edit Control Point Users</p>
<p>Record Receipt of Multiple Delivery Schedule Items</p>
<p>Multiple Delivery Schedule List</p></td>
</tr>
</tbody>
</table>

# IFCAP/eCMS Interface (2237 Processing)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The process of obtaining bids and awarding a contract occurs within the electronic Contract Management System (eCMS). With the implementation of an interface between IFCAP and eCMS in October 2012, 2237s, created by control point, users may be sent automatically to eCMS when the Accountable Officer processes, e-signs, and determines the 2237 should go to Purchasing & Contracting. A new Status, “Sent to eCMS (P&C),” will be placed on the 2237.

The 2237 data will be transmitted in an HL7 message to eCMS. If the Accountable Officer decides to send the 2237 forms to eCMS, then IFCAP will store certain information about that transaction in a new IFCAP/ECMS TRANSACTION FILE \[414.06\].

## Returned to Accountable Officer from eCMS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the contracting staff decide that a 2237 should be returned to the Accountable Officer, the 2237 is returned to IFCAP automatically via another HL7 message. The 2237 is then available to the Accountable Officer to complete the processing of the 2237 within IFCAP.

The Users listed on a 2237 as the Accountable Officer and the Initiator will receive a VistA MailMan message if eCMS returns that 2237 to the Accountable Officer. The phone number and e-mail address of the eCMS Contact will be included in the MailMan message.

### MailMan Message – 2237 Returned to AO 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: 2237 RETURNED TO ACCOUNTABLE OFFICER 001-12-4-223-0014 \[#403094\]08/13/12@13:53 10 lines

From: IFCAP/ECMS INTERFACE In 'IN' basket. Page 1 \*New\*

------------------------------------------------------------------------------

STATION 001 SUBSTATION 001HS

eCMS Date/Time Returned to AO Aug 13, 2012@12:53:21

001-12-4-223-0014

ECMS, Test

Ecms.test@va.gov

123-456-0001

Returned to the Accountable Officer Level in IFCAP

Not eligible for contracting process in eCMS. Handle in IFCAP.

Enter message action (in IN basket): Ignore//

## Returned to Control Point Users 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the eCMS contracting staff decide that a 2237 should be returned to the Control Point level, the 2237 is returned to IFCAP automatically via another HL7 message. A new Status, “Returned to Service by eCMS (P&C),” is placed on the 2237 and the Control Point users *are required to edit the 2237 and reapprove it.* The Accountable Officer will then be able to process it again and send it back to eCMS.

The users listed on the 2237 as the Accountable Officer, Control Point Official, and Initiator will receive a VistA MailMan message if eCMS returns a 2237 to the Control Point level. The phone number and e-mail address of the eCMS Contact will be included in the MailMan message.

### MailMan Message: Return 2237 to Control Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: 2237 RETURNED TO CONTROL POINT FOR 999-12-4-333-0080 \[#403100\]

08/13/12@16:00 10 lines

From: IFCAP/ECMS INTERFACE In 'IN' basket. Page 1 \*New\*

------------------------------------------------------------------------------

STATION 999

eCMS Date/Time Returned to CP Aug 13, 2012@15:00:35

999-12-4-333-0080

TEST, ECMS

ecms.test@va.gov

123-456-0900

Returned to the Control Point Level in IFCAP

Delete line item 14 and modify line item 10 to be Qty 24 pr.

Enter message action (in IN basket): Ignore//

## Cancelled in IFCAP by eCMS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After communicating with the FCP User, an eCMS user – and the eCMS contracting staff – may decide that a 2237 should be cancelled. In this case, the cancelled 2237 is returned to IFCAP automatically via another HL7 message. The 2237 status will be marked as cancelled and the existing IFCAP background processes will update the Running Balance to reflect the entry as CAN (Cancelled) and the amount will be set to zero. If due ins were established when the 2237 was approved, they will be reversed.

The users listed on a 2237 as the Accountable Officer, Control Point Official and Initiator will receive a VistA MailMan message if eCMS cancels a 2237. The phone number and e-mail address of the eCMS Contact will be included in the MailMan message.

### MailMan Message: Cancel 2237

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: 2237 CANCEL FROM eCMS FOR 2237 999-12-3-110-0021 \[#403586\] 08/28/12@14:51 10 lines

From: IFCAP/ECMS INTERFACE In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

STATION 999

eCMS Date/Time Canceled Aug 28, 2012@13:50:53

999-12-3-110-0021

ECMS, Test

ecms.test@va.gov

456-789-0123

Cancelled the 2237. Not to be ordered with this 2237.

Enter message action (in IN basket): Ignore//

# Error Messages and Their Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## User Errors 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you use IFCAP to request goods and services, you will receive errors. Some errors are use errors. *User errors* indicate that IFCAP has determined that the information you have entered in the system is either incomplete or inconsistent. Such messages look like this:

<span id="_Toc222496971" class="anchor"></span>Figure 171: Sample User Error Message

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Select TRANSACTION: 10195</strong></p>
<p><strong>Incorrect format - please re-enter number</strong></p>
<p><strong>Select TRANSACTION:</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

This guide and the online option descriptions should help you with these errors.

## System Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*System errors* occur when IFCAP fails to function properly. When these errors occur, IFCAP will display the error code. Record the error code and notify your IRM service.

<span id="_Toc222496972" class="anchor"></span>Figure 172: Sample System Error Message

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>RECORDING THAT AN ERROR OCCURRED ---</strong></p>
<p><strong>X2^PRCST212:1, %DSM-E-UNDEF, undefined variable PRCSTDT, -DSM-I-ECODE,</strong></p>
<p><strong>MUMPS error code: M6</strong></p>
<p><strong>Sorry 'bout that</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary defines terms in this guide that users might find unfamiliar.
| Term                                           | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1358                                       | VA Form 1358, Estimated Obligation or Change in Obligation.                                                                                                                                                                                                                                                                                                                                                     |
| 2138                                       | VA Form 90-2138, Order for Supplies or Services. First page of a VA Purchase Order.                                                                                                                                                                                                                                                                                                                             |
| 2139                                       | VA Form 90-2139, Order for Supplies or Services (Continuation). This is a continuation sheet for the 2138 form.                                                                                                                                                                                                                                                                                                 |
| 2237                                       | VA Form 90-2237, Request, Turn-in and Receipt for Property or Services. Used to request goods and services.                                                                                                                                                                                                                                                                                                     |
| A&MM                                       | Acquisition and Materiel Management Service.                                                                                                                                                                                                                                                                                                                                                                    |
| AACS                                       | Automated Allotment Control System--Central computer system developed by VHA to disburse funding from VACO to field stations.                                                                                                                                                                                                                                                                                   |
| Accounting Technician                      | Fiscal employee responsible for obligation and payment of received goods and services. Accounting Technicians process accounting transactions and transmit them to FMS.                                                                                                                                                                                                                                         |
| Activity Code                              | The last two digits of the AACS number. It is defined by each station.                                                                                                                                                                                                                                                                                                                                          |
| Security Officer                           | The individual at your station who’s responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing file access.                                                                                                                                                                                                           |
| Agent Cashier                              | The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.                                                                                                                                                                                                                                                               |
| AITC                                       | The Austin Information Technology Center, located in Austin, Texas.                                                                                                                                                                                                                                                                                                                                             |
| ALD Code                                   | Appropriation Limitation Department. A set of Fiscal codes that identifies the appropriation used for funding.                                                                                                                                                                                                                                                                                                  |
| Allowance table                            | Reference table in FMS that provides financial information at the level immediately above the AACS, or sub-allowance level.                                                                                                                                                                                                                                                                                     |
| Amendment                                  | A document that changes the information contained in a specified Purchase Order. Amendments are processed by the Purchasing & Contracting section of A&MM and obligated by Fiscal Service.                                                                                                                                                                                                                      |
| Application Coordinator                    | The individuals responsible for the implementation, training and troubleshooting of a software package within a service. IFCAP requires there to be an Application Coordinator designated for Fiscal Service, Supply Service, and Control Points (Requesting Services).                                                                                                                                         |
| Approve Requests                           | The use of an electronic signature by a Control Point Official to approve a 2237, 1358 or other request form and transmit said request to Supply/Fiscal.                                                                                                                                                                                                                                                        |
| Approving Official                         | An official in Purchasing and Contracting or Acquisition & Materiel Management Service that approves orders for payment and inspects orders and reconciliations to ensure that they are correct and complete.                                                                                                                                                                                                   |
| Authorization                              | A charge to 1358 form with obligated funds. Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you submit expenses from more than one vendor are covered by a single 1358.                                                                                                                                                                |
| Authorization Balance                      | The amount of money remaining that can be authorized against 1358. The service balance minus total authorizations.                                                                                                                                                                                                                                                                                              |
| Batch Number                               | A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number.                                                                                                                                                                                                                                                     |
| Breakout Code                              | A set of A&MM codes which identifies a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.).                                                                                                                                                                                                                                                     |
| Budget Analyst                             | Fiscal employee responsible for distributing and transferring funds.                                                                                                                                                                                                                                                                                                                                            |
| Budget Object Code                         | Fiscal accounting element that tells what kind of item or service is being procured.                                                                                                                                                                                                                                                                                                                            |
| Budget Sort Category                       | Used by Fiscal Service to identify the allocation of funds throughout their facility.                                                                                                                                                                                                                                                                                                                           |
| Ceiling Transactions                       | Funding distributed from Fiscal Service to IFCAP Control Points for spending. The Budget Analyst initiates these transactions using the Funds Distribution options.                                                                                                                                                                                                                                             |
| Classification of Request                  | An identifier a Control Point can assign to track requests that fall into a category, e.g., Memberships, Replacement Parts, Food Group III.                                                                                                                                                                                                                                                                     |
| Common Numbering Series                    | This is a pre-set series of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinators establish the Common Numbering Series used by each facility.                                     |
| Control Point                              | Financial element existing ONLY in IFCAP, which corresponds to the ACCS number in FMS. Also, the division of monies into a specified service, activity or purpose from an appropriation.                                                                                                                                                                                                                        |
| Control Point Clerk                        | The user within the service who’s designated to input requests (2237s) and maintain the Control Point records for a Service.                                                                                                                                                                                                                                                                                    |
| Control Point Official                     | The individual authorized to expend government funds for ordering supplies and services for their Control Point(s). This person has all of the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.                                                                                                                                               |
| Control Point Official's Balance           | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.                                                                                                                                                                                   |
| Control Point Requestor                    | The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. This level of user is only able to view and edit their requests. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&MM.                                                                                                        |
| Cost Center                                | “Subsection” of a Fund Control Point. Cost centers allow fiscal staff to create total expense reports for a section or service and allow requestors to assign requests to that section or service. Cost centers are listed in the left column of MP-4 Part V, Appendix B-1.                                                                                                                                     |
| Date Committed                             | The date that you want IFCAP to commit funds to the purchase.                                                                                                                                                                                                                                                                                                                                                   |
| Default                                    | A suggested response that is provided by the system.                                                                                                                                                                                                                                                                                                                                                            |
| Deficiency                                 | When a budget has obligated and expended more than it was funded (see MP-4, Part V, Section C).                                                                                                                                                                                                                                                                                                                 |
| Delinquent Delivery Listing                | A listing of all the Purchase Orders that have not had all the items received by the Warehouse on IFCAP. It is used to contact the vendor for updated delivery information.                                                                                                                                                                                                                                     |
| Delivery Order                             | An order for an item that the VA purchases through an established contract with a vendor who supplies the items.                                                                                                                                                                                                                                                                                                |
| Direct Delivery Patient                    | A patient who has been designated to have goods delivered directly to him/her from the vendor.                                                                                                                                                                                                                                                                                                                  |
| Discount Item                              | This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.                                                                                                                                                                                                                                                     |
| eCMS                                       | The VA’s electronic Contract Management System located in Austin, Texas.                                                                                                                                                                                                                                                                                                                                        |
| EDI Vendor                                 | A vendor with whom the VA has negotiated an arrangement to accept and fill orders electronically.                                                                                                                                                                                                                                                                                                               |
| Electronic Data Interchange (EDI)          | Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.                                                                                                                                                                                                                                                                             |
| Electronic Signature                       | The electronic signature code replaces the written signature on all IFCAP documents used within your facility. Documents going off station will require a written signature as well.                                                                                                                                                                                                                            |
| Expenditure Request                        | A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).                                                                                                                                                                                                                                                                                        |
| FCP                                        | Fund Control Point (see Control Point).                                                                                                                                                                                                                                                                                                                                                                         |
| Federal Tax ID                             | A unique number that identifies your station to the Internal Revenue Service.                                                                                                                                                                                                                                                                                                                                   |
| Fiscal Balance                             | The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by all liquidations submitted against the obligation.                                                                                                                                                                                                                         |
| Fiscal Quarter                             | The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.                                                                                                                                                                                                                                                                                                         |
| Fiscal Year                                | Twelve-month period from October 1 to September 30.                                                                                                                                                                                                                                                                                                                                                             |
| FMS                                        | Financial Management System is the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.               |
| FOB                                        | Freight on Board. An FOB of “Destination” means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of “Origin” means that shipping charges are due to the shipper and must be paid when the shipper arrives at the warehouse with the item.                                                            |
| FPDS                                       | Federal Procurement Data System.                                                                                                                                                                                                                                                                                                                                                                                |
| FTEE                                       | Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned as an FTEE of 0.5, as would a full-time employee that worked for half of a year.                                                                                                               |
| Fund Control Point                         | An accounting element that is not used by FMS.                                                                                                                                                                                                                                                                                                                                                                  |
| Funds Control                              | A group of Control Point options that allow the Control Point Clerk and/or Official to maintain and reconcile their funds.                                                                                                                                                                                                                                                                                      |
| Funds Distribution                         | A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.                                                                                                                                                                                                                                                               |
| GBL                                        | Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of \$250.00.                                                                                                                                                                                                                                                                                                    |
| GL                                         | General Ledger.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Identification Number                      | A computer-generated number assigned to a code sheet.                                                                                                                                                                                                                                                                                                                                                           |
| Imprest Funds                              | Monies used for cash or 3rd party draft purchases at a VA facility.                                                                                                                                                                                                                                                                                                                                             |
| Integrated Supply Management System (ISMS) | ISMS is the system that replaced LOG I for Expendable Inventory.                                                                                                                                                                                                                                                                                                                                                |
| ISMS                                       | Integrated Supply Management System.                                                                                                                                                                                                                                                                                                                                                                            |
| Item File                                  | A listing of items specified by A&MMS as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history.                                                                                                                                                                                                          |
| Item History                               | Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.                                                                                                                                                                                                                                                              |
| Item Master Number                         | A computer-generated number used to identify an item in the Item File.                                                                                                                                                                                                                                                                                                                                          |
| Justification                              | A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source.                                                                                                                                                                                                                          |
| Liquidation                                | The amount of money on the invoice from the vendor for the authorization. They are processed through payment/invoice tracking.                                                                                                                                                                                                                                                                                  |
| LOG I                                      | LOG I is the name of the Logistics A&MM computer located at the Austin Data Processing Center. This system continues to support the Consolidated Memorandum of Receipt.                                                                                                                                                                                                                                         |
| Mandatory Source                           | A Federal Agency that sells supplies and services to the VA. VA Supply Depot, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.                                                                                                                                                                                                                                                       |
| MSC Confirmation Message                   | A MailMan message generated by the Austin Message Switching Center that assigns an FMS number to an IFCAP transmission of Code Sheets.                                                                                                                                                                                                                                                                          |
| Obligation                                 | The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of a Purchase Order.                                                                                                                                                                                                                                                                                                     |
| Obligation (Actual) Amount                 | The actual dollar figure that has been obligated by Fiscal Service for a Purchase Order. The Control Point's records are updated with actual cost automatically when Fiscal obligates the document on IFCAP.                                                                                                                                                                                                    |
| Obligation Number                          | The C prefix number that Fiscal Service assigns to 1358.                                                                                                                                                                                                                                                                                                                                                        |
| Organization Code                          | Accounting element is functionally comparable to Cost Center but used to organize purchases by the budget that funded them, not for the purpose of spending the funds.                                                                                                                                                                                                                                          |
| Outstanding 2237                           | A&MM report that lists all the IFCAP generated 2237s pending action in A&MM.                                                                                                                                                                                                                                                                                                                                    |
| PAID                                       | Paid Accounting Integrated Data.                                                                                                                                                                                                                                                                                                                                                                                |
| Partial                                    | A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.                                                                                                                                                                                                                                                                                            |
| Partial Date                               | The date that a warehouse clerk created a receiving report for a shipment.                                                                                                                                                                                                                                                                                                                                      |
| PAT Number                                 | Pending Accounting Transaction number - the primary FMS reference number.                                                                                                                                                                                                                                                                                                                                       |
| Personal Property Management               | A section of A&MM Service who is responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process all requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support.                                      |
| PPM                                        | Personal Property Management, now referred to at most sites as Acquisition and Materiel Management Service.                                                                                                                                                                                                                                                                                                     |
| Procurement Request Cards                  | VA Form 10-7142. Used to order items repetitively.                                                                                                                                                                                                                                                                                                                                                              |
| Program Code                               | Accounting element that identifies the VA initiative or program that the purchase will support.                                                                                                                                                                                                                                                                                                                 |
| Prompt Payment Terms                       | The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).                                                                                                                                                                                            |
| Purchase Card                              | A card, similar to a credit card, which Purchase Card Users use to make purchases. Purchase Cards are not credit cards but debit cards that spend money out of a deposited balance of VA funds.                                                                                                                                                                                                                 |
| Purchase Card Coordinator                  | A person authorized by a VA station to monitor and resolve delinquent purchase card orders, help VA services record, edit and approve purchase card orders in a timely manner, assign purchase cards to IFCAP users, and monitor the purchase card expenses of VAMC services.                                                                                                                                   |
| Purchase Card Orders                       | Orders funded by a purchase card.                                                                                                                                                                                                                                                                                                                                                                               |
| Purchase Card User                         | A person who uses a purchase card. Purchase Card Users are responsible for reporting their purchase card orders in IFCAP.                                                                                                                                                                                                                                                                                       |
| Purchase History Add (PHA)                 | Information about purchase orders which is automatically sent to Austin for archiving. This same transaction is also used to send a PO for EDI processing.                                                                                                                                                                                                                                                      |
| Purchase Order                             | A government document authorizing the purchase of the goods or services at the terms indicated.                                                                                                                                                                                                                                                                                                                 |
| Purchase Order Acknowledgment              | Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).                                                                                                                                                                                                                                                                                          |
| Purchase Order Status                      | The status of completion of a purchase order (e.g., Pending Contracting Officer's Signature, Pending Fiscal Action, Partial Order Received, etc.).                                                                                                                                                                                                                                                              |
| Purchasing Agents                          | A&MM employees who are legally empowered to create purchase orders to obtain goods and services from commercial vendors.                                                                                                                                                                                                                                                                                        |
| Quarterly Report                           | A Control Point listing of all transactions (Ceilings, Obligations, Adjustments) made to Control Point's Funds.                                                                                                                                                                                                                                                                                                 |
| Quotation for Bid                          | Standard Form 18. Used by Purchasing Agents to obtain written bids from vendors.                                                                                                                                                                                                                                                                                                                                |
| Receiving Report                           | Report that Warehouse Clerk creates to record that the warehouse has received an item.                                                                                                                                                                                                                                                                                                                          |
| Receiving Report                           | The VA document used to indicate the quantity and dollar value of the goods being received.                                                                                                                                                                                                                                                                                                                     |
| Reconciliation                             | Comparing two records of a purchase to validate IFCAP records and the records of other systems that share data with IFCAP. For example, Purchase Card Users compare purchase card orders with the 820 Sub allowance Reconciliation from FMS.                                                                                                                                                                    |
| Reference Number                           | Also known as the Transaction Number. The computer-generated number that identifies a request. It is comprised of the: Station Number - Fiscal Year - Quarter - Control Point - 4-digit Sequence Number.                                                                                                                                                                                                        |
| Repetitive (PR Card) Number                | See Item Master Number.                                                                                                                                                                                                                                                                                                                                                                                         |
| Repetitive Item List                       | A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate requests from the list.                                                                                                                                                                                                               |
| Requestor                                  | See “Control Point Requestor.”                                                                                                                                                                                                                                                                                                                                                                                  |
| Requisition                                | An order from a government vendor.                                                                                                                                                                                                                                                                                                                                                                              |
| Running Balance                            | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.                                                                                                                                                                                  |
| Section Request                            | A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.                                                                                                                                                                                                                                        |
| Service Balance                            | The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorization created by the service.                                                                                                                                                                                                  |
| SF-18                                      | Request for Quotation.                                                                                                                                                                                                                                                                                                                                                                                          |
| SF-30                                      | Amendment of Solicitation/Modification of Contract.                                                                                                                                                                                                                                                                                                                                                             |
| Short Description                          | A phrase that describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).                                                                                                                                                                                                        |
| Site Parameters                            | Information (such as Station Number, Cashier's address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter file.                                                                                                                                                                                                                                                 |
| Sort Group                                 | An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.                                                                                                                                                                                                                                                           |
| Sort Order                                 | The order in which the budget categories will appear on the budget distribution reports.                                                                                                                                                                                                                                                                                                                        |
| Special Remarks                            | A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.                                                                                                                                                                                                                                   |
| Stacked Documents                          | The POs, RRs, and 358s that are sent electronically to Fiscal and stored in a file rather than being printed immediately.                                                                                                                                                                                                                                                                                       |
| Status of Funds                            | Fiscal’s on-line status report of the monies available to a Control Point. FMS updates this information automatically.                                                                                                                                                                                                                                                                                          |
| Sub-control Point                          | A specific budget within a Control Point, defined by a Control Point user.                                                                                                                                                                                                                                                                                                                                      |
| Sub-cost Center                            | A subcategory of Cost Center. IFCAP will not use a 'sub-cost center' field but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.                                                                                                                                                                                 |
| Tasked Job                                 | A job, usually a printout, which has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.                                                                                                                                                                                                                                                   |
| TDA                                        | See “Transfer of Disbursing Authority.”                                                                                                                                                                                                                                                                                                                                                                         |
| Total Authorizations                       | The total amount of the authorizations created for the 1358 obligation.                                                                                                                                                                                                                                                                                                                                         |
| Total Liquidations                         | The total amount of the liquidation against the 1358 obligation.                                                                                                                                                                                                                                                                                                                                                |
| Transaction Number                         | The number of the transaction that funds a Control Point (See Budget Analyst User's Guide). It consists of the Station Number - Fiscal Year - Quarter - Control Point - Sequence Number.                                                                                                                                                                                                                        |
| Transmission Number                        | A sequential number given to a data string when it is transmitted to the Austin DPC; used for tracking message traffic.                                                                                                                                                                                                                                                                                         |
| Type Code                                  | A set of A&MM codes that provides information concerning the vendor’s size and type of competition sought on a purchase order.                                                                                                                                                                                                                                                                                  |
| Vendor file                                | An IFCAP file of vendors solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. File 440 contains information about the vendors requested by your station. The debtor's address may be drawn from this file but is maintained separately. If the desired vendor is not in the file, contact A&MM Service to have it added. |
| Vendor ID Number                           | The ID number that is assigned to a vendor by FMS.                                                                                                                                                                                                                                                                                                                                                              |
| VRQ                                        | FMS Vendor Request document. When users send vendor information to FMS, FMS sends a VRQ document to IFCAP with the vendor information, ensuring that the information in the IFCAP vendor file matches the information in the FMS vendor table.                                                                                                                                                                  |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<Alt\> 1-3
2237 2-1, 8-47
A&MM 3-7, 4-2, 4-5
Accounting Technician 3-6, 6-2, 6-3, 8-86
Add/Edit Supply Personnel 3-8
Amendment Processing 4-3
Approve Requests 3-2
Audit Transaction List 8-11
Barcode Manager Menu 3-7
BOC Detail Totals 8-24
BOC Totals 8-20
Budget Analyst 3-5
Budget Object Code 8-24
Budget Object Code (BOC) 8-3, 8-20, 8-39, 8-66, 8-76, 8-81
Cancel Transaction with Permanent Number 8-52
Ceiling Report 8-10, 8-11
Ceiling Transactions 3-2
Change Existing Transaction Number 8-48
Classification of Request Report 8-15
click 1-3
Control Point 3-2, 3-3, 3-4, 3-7, 4-2
Cost Center Totals 8-18, 8-19
Date Committed 8-66, 8-76
Delete Repetitive Item List Entry 8-62
documents available 1-2
Edit a 2237 (Service) 8-43
Edit Repetitive Item List Entry 8-56
Electronic Signature 3-8
Enter FCP Adjustment Data 8-1
figures
list of xiii
Financial Management System 4-2
Fiscal Quarter 4-5, 4-7, 6-1
Fiscal Year 4-5, 4-7, 6-1
FMS 4-2, 6-3, 8-26, 8-27
Fund Control Point adjustments sent to IFCAP 4-2
Suballowance Reconciliation 4-3
sub-cost center 4-2
FMS Transaction Data 8-26
Generate Requests From Repetitive Item List Entry 8-60
hyperlink
internal 1-2
hyperlinks 1-2
icon
Information 1-4
Technical Note 1-4
Tip 1-4, 3-2, 3-8, 3-10, 4-2
Warnings 1-4
icons for boxed notes 1-4
IFCAP 1-4
Increase/Decrease Adjustment 8-79
ISMS 2-4, 3-3
Item Display 8-68
Item History 8-105
Justification 8-42, 8-67
Manual 1-4
New 2237 (Service) Request 8-37
New Repetitive Item List (Enter) 8-54
operating system 1-3
PO with Associated Transactions 8-33
Print 1358 8-94
Print/Display Repetitive Item List Entry 8-58
Print/Display Request Form 8-30, 8-46
Purchase Order 2-3, 4-2, 8-45
Purchasing Agents 2-3
Quarterly Report 8-7, 8-8
Query Tool 1-4
Recalculate Fund Control Point Balance 8-6
Record Date Received by Service Menu 8-108
Requestor 3-4
Requests Ready for Approval List 8-35
rollover funds 4-3
Running Balances 6-1
Site Parameters 3-1
Sort Group Report 8-15
Status of All Obligation Transactions 8-32
System Access 3-1
tables
list of xiii
Tranaction Number 4-4
Transaction Data report 4-2
Transaction Number 4-6, 4-8, 8-43, 8-48, 8-82, 8-102
Vendor file 4-2
