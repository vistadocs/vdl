---
title: IFCAP Version 5.1 Control Point Clerk User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Control Point Clerk User's Guide
app_code: PRC
app_name: IFCAP
section: FIN
app_status: active
pkg_ns: PRC
patch_ver: 5.1
patch_id: PRC*5.1
group_key: "PRC:PRC:5.1"
file_numbers: []
security_keys: []
menu_options: 3
description: 
audience: 
keywords: 
  - control
  - request
  - point
  - table
  - contents
  - number
  - transaction
  - report
  - ifcap
  - prompt
page_count: 0
word_count: 43282
section_count: 86
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1cp_clerk.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1cp_clerk.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP)Version 5.1Control Point ClerkUser’s Guide

![](ifcap-version-5-1-control-point-clerk-user-s-guide/001.png)

March 2026Department of Veterans AffairsOffice of Information and Technology (OI&T)Management, Enrollment, and Financial Systems

Revision History

Initiated on 12/29/04

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 49%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description (Patch # if applicable)</strong></th>
<th><strong>Author(s)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>March 2026</td>
<td>12.0</td>
<td><p>Updates based on patch PRC*5.1*257.</p>
<p>This manual has been updated to comply with the VA OIT-mandated user guide template.</p></td>
<td><p>Technical Writer,</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="even">
<td><p>May</p>
<p>2016</p></td>
<td>11.0</td>
<td><p>Updates based on patch PRC*5.1*184.</p>
<p>• Corrected Adjustment instructions. See pages <a href="#PRC_184_A">80</a> and <a href="#PRC_184_B">117</a>.</p></td>
<td><p>Technical Writer, Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>January 2014</td>
<td><blockquote>
<p>10.0</p>
</blockquote></td>
<td><blockquote>
<p>Patch PRC*5.1*174 (IFCAP/eCMS Interface)</p>
</blockquote>
<p>1.6.6 – replaced “If the contracting staff…” with “If the <strong>eCMS</strong> contracting staff…”</p>
<p>1.6.7– replaced ‘an eCMS user may decide – with the eCMS contracting staff ‘–with ‘<strong>the eCMS contracting staff may determine that the 2237.</strong>’</p>
<p>Replaced ‘then the 2237 is returned to IFCAP automatically via another HL7 message’ with ‘<strong>then generate a cancellation of the 2237 in IFCAP automatically via another HL7 message.’</strong></p>
<p>2.4.5. –replaced ‘prompt, enter the name or the number of the service that will use the item. Enter the date required. Enter the priority of the request’ with ‘prompt, you must enter the name or the number of the service that will use the item.’</p>
<p>Added new <strong>Note:</strong> The Requesting Service field is mandatory in IFCAP. It is also a required field for the eCMS interface. If the Accountable Officer attempts to send a 2237 to eCMS and this field is blank, the 2237 will generate a transmission error. The Accountable Officer will have to return the 2237 to the CP user for edit and re-approval.</p>
<p>Updated top of screen display with “If User attempts to pass this field without entering a value – the software will prompt them for a response.</p>
<p>REQUESTING SERVICE: ??</p>
<p>Select the name of the Service that submitted this request.”</p>
<p>2.5.1- replaced ‘This might keep A&amp;MM staff from…’ with ‘This might keep Logistics staff from…’</p>
<p>2.5.4 –new sentence above screen display stating, “The Classification of Request field is not mandatory.”</p>
<p>Added <strong>Note:</strong> Requesting Service is an IFCAP-required field, and the 2237 cannot go forward to the electronic Contract Management System (eCMS), <strong>unless this field is populated</strong></p>
<p>Updated top of screen display with “If User attempts to pass this field without entering a value – they will be prompted to fill in this field.</p>
<p>REQUESTING SERVICE: ??</p>
<p>Select the name of the Service that submitted this request.”</p>
<p>2.5.7 - Added new <strong>Note:</strong> The Line Item <u>DESCRIPTION</u> is now a required field in the 2237. If the User attempts to leave the DESCRIPTION field blank, the User is prompted to fill in the field.</p>
<p>2.6.4 – After the REQUESTING SERVICE: ?? prompt, the “Select the name or number of the Service that submitted this request” displays.</p>
<p>Replaced the “Note: Although Requesting Service is not an IFCAP-required field, if the 2237 is intended to go forward to the electronic Contract Management System (eCMS), this field must be populated.” With “<strong>Note:</strong> Requesting Service is an IFCAP-required field. The 2237 cannot go forward to the electronic Contract Management System (eCMS), unless this field is populated.”</p>
<p>2.6.7. – Updated the next three lines after the Description: prompt, ‘If User does not enter any text, the User will be prompted to enter some text. Item DESCRIPTION is required! User must enter some text.’</p>
<p>2.6.9. – Added a note to screen display, “<strong>Note:</strong> Control Point Clerk is not permitted to set the 2237 to YES – Ready for Approval if any Required field is not populated.”</p>
<p>2.7.5 – Updated “<strong>Note</strong>: Although Requesting Service is not an IFCAP - required field, if the 2237 is intended to go forward to the electronic Contract Management System (eCMS), this field must be populated.” With “<strong>Note</strong>: Requesting Service is now an IFCAP-required field; the 2237 is not permitted to go forward to the electronic Contract Management System (eCMS), if this field is not populated.”</p>
<p>3.2 – Updated heading “3.2 Converting Item Requests to Permanent Transactions” with “<strong>3.2</strong> <strong>Converting Temporary Requests to Permanent Transactions</strong>”</p>
<p>3.2.1 - Added new “<strong>Note:</strong> The fields Requesting Service and Line-Item DESCRIPTION are not required fields in a Temporary Request. This will mean the Control Point Clerk may encounter missing required fields when converting a temporary request to a 2237 transaction. The Clerk will be advised of the missing field(s) and be allowed to edit the new 2237 and populate the required fields. If they choose not to edit the fields at that time the 2237 will not be complete and the Clerk will not be able to set the Approval flag to YES. The Clerk will have to Edit the 2237 and populate the missing fields.”</p>
<p>3.2.3 – new Request Review screen display</p>
<p>3.2.4 – REQUESTING SERVICE: <strong>CP</strong> User must Populate this field as it is required on a 2237<strong>.</strong></p>
<p>3.2.5 – reworded first paragraph</p>
<p>- added a note to screen caption, “Note: User cannot set the Request to “Ready for Approval? //YES" if the Requesting Service or any Item DESCRIPTION field is not populated.”</p>
<p>7.4. – updated heading “7.4 Canceling Transactions with Permanent Number” with “7.4 Change Existing Transaction Number (of a 2237)”</p>
<p>7.4.1 – added first sentence “Use this option to change the transaction number of an existing 2237 transaction.”</p>
<p>7.4.1 - added NOTE: If the 2237 you are changing has eCMS Identifiers -- immediately upon completing the process, you must manually notify the eCMS Contracting Officer of the changed 2237 number. Advise them of the cancelled original 2237# and the new 2237#. This will ensure that the Contracting Officer cancels the old 2237 in the eCMS system and will enable the Contracting Officer to link the new 2237 to the existing Award plan documents when it is Approved and sent forward to eCMS.</p>
<p>7.5 – replace heading “7.5 Supplementary Options in the Requestor's Menu with “7.5 Canceling Transactions with Permanent Number”</p>
<p>7.5.2 – added to second Note,</p>
<p>‘…Control Point Activity file (#410)’ at the end of the sentence</p>
<p>- updated screen capture by adding Comments: prompt, to describe the reason this transaction was cancelled</p>
<p>7.13.2 – updated screen display and also replaced ‘Sent to eCMS’ with ‘Accepted by eCMS’</p>
<p>7.13.3- updated screen display</p>
<p>7.13.4 – “<strong>Note:</strong> The Requesting Service field is a required field on a 2237.” Updated screen display</p>
<p>7.13.5 – the paragraph was divided into three smaller paragraphs. A sentence was added at the end of paragraph two –“If you are not selecting an Item from the Item Master File, you will be prompted to fill in the Item Description.” A note was inserted below paragraph two - “<strong>Note:</strong> Item Description is now a Required Field. You must enter the text.” Updated screen display.</p>
<p>7.13.6 – updated text description and screen display. Added a</p>
<p><strong>“Note:</strong> The User will not be able to set the Ready for Approval Flag to YES if either the Requesting Service field or a Line-Item Description field is not populated if a Required field is not populated, the User will see a warning message and be prompted to Edit the 2237 again. “</p>
<p>7.28 – replaced part of the note “…able to view data related to 2237 transactions returned from eCMS which are related to the Control Point(s) on which you are identified as a Control Point Clerk or Official.” With “…to view data about the 2237 transactions related to the Control Point(s) on which you are identified as a Control Point Clerk or Official”</p>
<p>7.28.1 – added Transaction Report - eCMS/IFCAP to the Process a Request Menu Option screen display</p>
<p>7.28.2 – added new paragraphs one and three to this section. Added <strong>“</strong>Select Process a Request Menu &lt;TEST ACCOUNT&gt; Option: Transaction Report - eCMS/IFCAP to the top of the screen display.”</p></td>
<td><p>Subject Matter Expert, Developer, Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>9/25/2013</td>
<td>8.0</td>
<td><p>Updates based on patch PRC*5.1*171.</p>
<p>• Removed option <strong>Enter/Edit Control Point Users</strong> from menus. See pages 141, 142, &amp; 143.</p></td>
<td><p>Subject Matter Expert, Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>9/25/12</td>
<td></td>
<td><p>Updates based on feedback from the testing team:</p>
<p>• Page 14, 1.6.5 Returning a 2237 from eCMS to the Accountable Officer: Deleted “A new Status, “To IFCAP Ordering Officer,” is placed on the 2237 and an IFCAP Purchasing Agent may include the 2237 in a Purchase Order or if appropriate, a Requisition Clerk can include the 2237 in a Requisition.”</p>
<p>• Page 16, 1.6.6 Returning a 2237 from eCMS to the Control Point Level: (in Note: box), Corrected status from not “Returned to Service by eCMS (P&amp;C)”, no status transaction type is changed to “Cancelled.”</p>
<p>• Added comment about making the determination to cancel in conjunction with the FCP user. The eCMS user absolutely should not make this decision unilaterally. “After communicating with the FCP User an eCMS user may decide…”</p>
<p>• Page 22, 2.4.5 Requestor Information: added statement about Requesting Service being mandatory field for transmission to eCMS (Bring this NOTE: outside of the screen capture, this does not appear on IFCAP screen.</p>
<p>• Pg 26, 2.5.4 Classification and Sort Group, same as 2.4.5.</p>
<p>• Pg 31/32, 2.6.4 Updated Classification and Sort Group, same as 2.4.5. No “Note” in screen capture, but no reference to mandatory for eCMS.</p>
<p>• Pg 38, 2.7.5 Classification and Sort Group, same as 2.4.5.</p>
<p>• Pg 105, 7.27.2 Note boxes are repetitive already mentioned in 7.27</p>
<p>• Pg 105, 7.27 Added a statement that this report only lists transactions that have been returned by eCMS.</p>
<p>• Pg 149, 9.2.1 MailMan Error Messages – Updated eCMS Interface Check 1st &amp; 2nd sentence.</p>
<p>• Pg 149, 9.2.1 MailMan Error Messages – eCMS Interface, changed last sentence to: “The CP user will need to edit the 2237 to populate the Requesting Service field and reapprove the 2237.</p>
<p>• Fixed “Note” box format consistency see Note in 1.6.6 (pg. 15) &amp; 2.7.6 and Note in 2.5.5 (pg. 27) &amp; 2.6.5 (Pg 32), 2.6.7</p>
<p>9.2.1 MailMan Error Messages – eCMS Interface</p>
<p>• The Accountable Officer sends all 2237s that will be processed by Contracting staff to the electronic Contract Management System (eCMS) in Austin. The IFCAP application will reject any 2237 forwarded to eCMS with no Requesting Service (Requesting Service field is blank (null)). The field is now mandatory in IFCAP, the field is required for 2237s being sent to eCMS. The Accountable Officer will receive a MailMan message advising that the 2237 must be Returned to the Service for editing by the Control Point User. The CP user will then need to edit the 2237 populate the Requesting Service field and reapprove the 2237. The Accountable Officer will then be able to process the 2237 and send it to eCMS.</p></td>
<td><p>Subject Matter Expert, Project Manager,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>9/3/12</td>
<td>7.0</td>
<td><p>Patch PRC*5.1*167 Updates to:</p>
<p>Add new Option to Sections 2.4.3, 3.2.1, 3.3.1.3.3.3, 4.2.1, 5,2,1,7.4.2,7.7.1,7.8.1, 7.9.1, 7.10.1, 7.11.1, 7.12.1, 7.12.6, 7.13.1, 7.13.3, 7.14.1, 7.14.3, 7.16.1, 7.17.1, 7.18.1, 7.19.1, 7.20.1, 7.21.1, 7.22.1, 7.23.1, 7.24.1, 7.25.1, 7.26.1, 7.26.2, 8.1.</p>
<p>Updated Screen captures in Sections:</p>
<p>2.4.5, 2.7.5, 2.7.2, 7.2.1, 7.2.2, 7.3.3, 7.4.1, 7.27, 7.27.1, 7.27.2, 7.36.2, 7.41.3, 9.2</p>
<p>Added to Glossary: AITC, eCMS, OA&amp;L, VUP – updated text for VRQ.</p>
<p>Added new section 1.6.4</p></td>
<td><p>Subject Matter Expert, Project Manager,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>8/28/12</td>
<td>6.0</td>
<td><p>Patch PRC*5.1*167 Updates to:</p>
<ol type="1">
<li><p>Revised Body Text style to Calibri 11 single 6 pt after.</p></li>
<li><p>Revised paragraph formatting; changed all content text from Normal to Body Text.</p></li>
<li><p>Revised Heading 1, Heading 2-2, and Heading 3-3 for consistency with body text and other IFCAP manuals (i.e. Accountable Officer UG).</p></li>
<li><p>Changed task headings to gerund format where applicable.</p></li>
</ol></td>
<td><p>Project Manager,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>10/2011</td>
<td>5.0</td>
<td>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358. See pages <a href="#PRC_158_A">33</a>, <a href="#PRC_158_B">34-35</a>, <a href="#reviewing-the-1358">39-40</a>, <a href="#setup-parameters-13">76-77</a>, <a href="#display-or-print-1358">85-86</a>, <a href="#setup-parameters-21">90-91</a>, <a href="#glossary">131</a>.</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="odd">
<td>01/05/11</td>
<td>4.0</td>
<td><p>Updated to address changes in support of the Segregation of Duties Patch [PRC*5.1*148 See: 2.8, 7.16.3, 7.16.5, 7.16.7, 7.16.8, 7.17.4, 7.24.3 &amp; 7.25.2</p>
<p>Includes Removal of Obligation Data option .</p></td>
<td><p>Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>02/03/06</td>
<td>3.0</td>
<td>Added New option, Print Obligated 1358s, per patch PRC*5.1*79.</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="odd">
<td>12/29/04</td>
<td>2.0</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>12/29/04</td>
<td>1.0</td>
<td>Pdf file checked for accessibility to readers with disabilities.</td>
<td>Department of Veterans Affairs</td>
</tr>
</tbody>
</table>

Preface

This manual is designed to provide you, the Control Point Clerk, with the information necessary to create requests, reconcile your control point balance, and generate reports that will assist you in managing your control point funds using the Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) package. The IFCAP package automated certain functions in Acquisition and Materials Management (A&MM), Fiscal Service, and in all of the services that request supplies and services on Veterans Affairs (VA) Form 90-2237. The goal of IFCAP is to integrate these three areas and allow users to share procurement information. IFCAP has the following components or “modules.”

> FUNDS DISTRIBUTION allows Fiscal Service to establish Fund Control Points, and track funding for budget purposes.

> CONTROL POINT ACTIVITY automates the preparation of requests, the electronic transmission of requests to A&MM and Fiscal services and the bookkeeping processes within a service.

> PROCUREMENT allows A&MM to transfer IFCAP-generated requests onto purchase orders and requisitions, process receiving documents in the warehouse, and create and transmit code sheets to Austin.

> ACCOUNTING automates the creation of code sheets, handles the processing of certified invoices, and facilitates the electronic transmission of code sheets and receiving documents to the Financial Management System (FMS) located in Austin, Texas. In addition, IFCAP transfers obligation information back to the Control Point and updates the Control Point balance automatically.

> INVENTORY permits services to maintain their own on-line inventory and establish an average stock level, record the distribution of goods to secondary location(s), and automatically generate IFCAP requests for replenishment purposes. Secondary locations may maintain their own inventory if they wish.

> RFQ enables the Purchasing Agent (PA) to create a Request for Quotation (RFQ), evaluate bids, award the order, and generate the purchase order. Using IFCAP and the Electronic Data Interchange (EDI) functionality that currently exists in Austin, the PA can electronically send the RFQ to one or many vendors and receive the bids electronically

> PURCHASE CARD permits users at Service level and in A&MM to generate purchase orders against assigned credit card(s). Charges are passed electronically from the Austin Credit Card System (CCS) to IFCAP, and users reconcile payments with IFCAP Purchase Orders. The assigned Approving Official then approves reconciled orders. The local IFCAP Purchase Card Registration file is maintained by the station designated Purchase Card Coordinator. Reconciled orders are then approved by assigned Approving Officials. There are many reports that provide data on the status of the purchase card orders and timeliness of the reconciliation and approval processes.

> DELIVERY ORDERS permits users to generate purchase orders for contract items at the Service-level. Using switches that are site configurable, orders can bypass Fiscal and be obligated at time of signing by Service-level staff.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [The Role of the Control Point Clerk](#the-role-of-the-control-point-clerk)
  - [How to Use This Manual](#how-to-use-this-manual)
  - [Reference Numbering System](#reference-numbering-system)
  - [Package Management and Security Measures](#package-management-and-security-measures)
  - [Package Operation](#package-operation)
  - [Features](#features)
    - [Cost Centers](#cost-centers)
    - [Sub allowance/Fund Control Point Reconciliation](#sub-allowancefund-control-point-reconciliation)
    - [Rollover of Funds from Previous Quarters](#rollover-of-funds-from-previous-quarters)
    - [eCMS Interface to IFCAP (2237 Processing)](#ecms-interface-to-ifcap-2237-processing)
    - [Returning a 2237 from eCMS to the Accountable Officer](#returning-a-2237-from-ecms-to-the-accountable-officer)
    - [Returning a 2237 from eCMS to the Control Point Level](#returning-a-2237-from-ecms-to-the-control-point-level)
    - [Cancelling a 2237 in eCMS & IFCAP](#cancelling-a-2237-in-ecms-ifcap)
- [How To Create Requests](#how-to-create-requests)
  - [Introduction](#introduction-1)
  - [Which 2237 Request Form Should You Use?](#which-2237-request-form-should-you-use)
  - [How to Consult the Item Master File](#how-to-consult-the-item-master-file)
    - [Introduction](#introduction-2)
    - [Menu Path](#menu-path)
    - [Setup Parameters](#setup-parameters)
    - [Item Information](#item-information)
    - [Order Type](#order-type)
  - [Creating Repetitive (PR Card) Order 2237 Requests](#creating-repetitive-pr-card-order-2237-requests)
    - [Introduction](#introduction-3)
    - [Setup Parameters](#setup-parameters-1)
    - [Menu Navigation](#menu-navigation)
    - [Classification and Sort Groups](#classification-and-sort-groups)
    - [Requestor Information](#requestor-information)
    - [Special Remarks](#special-remarks)
    - [Selecting a Vendor](#selecting-a-vendor)
    - [Item Selection](#item-selection)
    - [Item History](#item-history)
    - [Delivery Schedules](#delivery-schedules)
  - [Creating Non-Repetitive Order 2237 Requests](#creating-non-repetitive-order-2237-requests)
    - [Introduction](#introduction-4)
    - [Menu Navigation](#menu-navigation-1)
    - [Form Type](#form-type)
    - [Classification and Sort Groups](#classification-and-sort-groups-1)
    - [Priority of Order](#priority-of-order)
    - [Vendor Selection](#vendor-selection)
    - [Item Information](#item-information-1)
    - [Stock Number](#stock-number)
    - [Delivery Schedules](#delivery-schedules-1)
  - [Creating Repetitive and Non-Repetitive Order 2237 Requests](#creating-repetitive-and-non-repetitive-order-2237-requests)
    - [Introduction](#introduction-5)
    - [Setup Parameters](#setup-parameters-2)
    - [Form Type](#form-type-1)
    - [Classification and Sort Groups](#classification-and-sort-groups-2)
    - [Priority of Order](#priority-of-order-1)
    - [Vendor Selection](#vendor-selection-1)
    - [Item Information](#item-information-2)
    - [Stock Number](#stock-number-1)
    - [Delivery Schedules](#delivery-schedules-2)
  - [Creating Issue Book/Interval Issue Requests](#creating-issue-bookinterval-issue-requests)
    - [Introduction](#introduction-6)
    - [Setup Parameters](#setup-parameters-3)
    - [Classification Group](#classification-group)
    - [Sort Group](#sort-group)
    - [Priority](#priority)
    - [Cost Center](#cost-center)
    - [Additional Items](#additional-items)
  - [Creating 1358 Order Requests](#creating-1358-order-requests)
    - [Introduction](#introduction-7)
    - [Menu Navigation](#menu-navigation-2)
    - [Classification and Sort Groups](#classification-and-sort-groups-3)
    - [Requestor](#requestor)
    - [BOC](#boc)
    - [Vendor Information](#vendor-information)
    - [Service Start and End Dates/Purpose of 1358](#service-start-and-end-datespurpose-of-1358)
    - [New Process Flow for 1358s](#new-process-flow-for-1358s)
- [Turning Temporary Requests into Transactions](#turning-temporary-requests-into-transactions)
  - [Introduction](#introduction-8)
  - [Converting Temporary Requests to Permanent Transactions](#converting-temporary-requests-to-permanent-transactions)
    - [Menu Navigation](#menu-navigation-3)
    - [Setup Parameters](#setup-parameters-4)
    - [Request Review](#request-review)
    - [Edit Request](#edit-request)
    - [Request Review](#request-review-1)
  - [Converting Temporary 1358 Transactions to Permanent Transactions](#converting-temporary-1358-transactions-to-permanent-transactions)
    - [Menu Navigation](#menu-navigation-4)
    - [Enter Temporary Number](#enter-temporary-number)
    - [Conversion to Permanent Number](#conversion-to-permanent-number)
- [Monitoring Request Status](#monitoring-request-status)
  - [Introduction](#introduction-9)
  - [Monitoring Request Status](#monitoring-request-status-1)
    - [When You Know the Purchase Order Number?](#when-you-know-the-purchase-order-number)
    - [When You Don’t Know the Purchase Order Number, but know the Vendor?](#when-you-dont-know-the-purchase-order-number-but-know-the-vendor)
    - [When You Don’t Know the Purchase Order Number or Vendor, But Have the First Line Item?](#when-you-dont-know-the-purchase-order-number-or-vendor-but-have-the-first-line-item)
  - [Monitoring the Status of 1358’s](#monitoring-the-status-of-1358s)
    - [Menu Navigation](#menu-navigation-5)
    - [Entering Obligation Number](#entering-obligation-number)
    - [Reviewing the 1358](#reviewing-the-1358)
  - [# Adjusting Control Point Balances](#adjusting-control-point-balances)
  - [Introduction](#introduction-10)
    - [Menu Navigation](#menu-navigation-6)
    - [Setup Parameters](#setup-parameters-5)
    - [Adjustment Information](#adjustment-information)
- [Handling System Down or Life-Threatening Emergencies](#handling-system-down-or-life-threatening-emergencies)
- [Other IFCAP Functions](#other-ifcap-functions)
  - [Supplementary Options in the Process a Request Menu](#supplementary-options-in-the-process-a-request-menu)
  - [Editing a 2237 (Service)](#editing-a-2237-service)
    - [Setup Parameters](#setup-parameters-6)
    - [Entering Transaction Numbers](#entering-transaction-numbers)
    - [Form Type](#form-type-2)
    - [Control Point Balances](#control-point-balances)
  - [Printing and Displaying Request Forms](#printing-and-displaying-request-forms)
    - [Menu Navigation](#menu-navigation-7)
    - [Last Page Print](#last-page-print)
    - [Interpreting the Request Form](#interpreting-the-request-form)
  - [Change Existing Transaction Number (of a 2237)](#change-existing-transaction-number-of-a-2237)
    - [Menu Navigation](#menu-navigation-8)
  - [Canceling Transactions with Permanent Number](#canceling-transactions-with-permanent-number)
    - [Setup Parameters](#setup-parameters-7)
    - [Canceling Transactions](#canceling-transactions)
  - [Supplementary Options in the Requestor's Menu](#supplementary-options-in-the-requestors-menu)
  - [Supplementary Options in the Repetitive Item List Menu](#supplementary-options-in-the-repetitive-item-list-menu)
  - [New Repetitive Item List (Enter)](#new-repetitive-item-list-enter)
    - [Menu Navigation](#menu-navigation-9)
    - [Setup Parameters](#setup-parameters-8)
    - [Item Selection](#item-selection-1)
    - [Item Information](#item-information-3)
  - [Editing the Repetitive Item List Entry](#editing-the-repetitive-item-list-entry)
    - [Menu Navigation](#menu-navigation-10)
    - [Select Repetitive List](#select-repetitive-list)
    - [Adds Items](#adds-items)
  - [Print/Display Repetitive Item List Entry](#printdisplay-repetitive-item-list-entry)
    - [Menu Navigation](#menu-navigation-11)
    - [Enter Repetitive List](#enter-repetitive-list)
    - [Review List](#review-list)
  - [Generate Requests From Repetitive Item List Entry](#generate-requests-from-repetitive-item-list-entry)
    - [Menu Navigation](#menu-navigation-12)
    - [Select List Entry](#select-list-entry)
    - [Generate Requests](#generate-requests)
    - [Display Balances](#display-balances)
  - [Delete Repetitive Item List Entry](#delete-repetitive-item-list-entry)
    - [Menu Navigation](#menu-navigation-13)
    - [Enter Repetitive List](#enter-repetitive-list-1)
    - [Delete List](#delete-list)
  - [Copy a Transaction](#copy-a-transaction)
    - [Menu Navigation](#menu-navigation-14)
    - [Setup Parameters](#setup-parameters-9)
    - [Review Request](#review-request)
    - [Additional Information](#additional-information)
    - [Special Remarks](#special-remarks-1)
    - [Add Items](#add-items)
  - [Item Display](#item-display)
    - [Menu Navigation](#menu-navigation-15)
    - [Enter Item Number](#enter-item-number)
    - [Display Data](#display-data)
  - [Vendor Display](#vendor-display)
    - [Menu Navigation](#menu-navigation-16)
    - [Vendor Selection](#vendor-selection-2)
    - [Display Vendor Information](#display-vendor-information)
  - [Supplementary Options in the 1358 Request Menu](#supplementary-options-in-the-1358-request-menu)
  - [New 1358 Request](#new-1358-request)
    - [Menu Navigation](#menu-navigation-17)
    - [Setup Parameters](#setup-parameters-10)
    - [Authority & Sub-Authority Fields](#authority-sub-authority-fields)
    - [Classification and Sort Groups](#classification-and-sort-groups-4)
    - [Requestor & Cost Center Data](#requestor-cost-center-data)
    - [BOC Data](#boc-data)
    - [Vendor & Contract Information](#vendor-contract-information)
    - [Service Start & End Dates/Purpose Field](#service-start-end-datespurpose-field)
  - [Increase/Decrease Adjustment](#increasedecrease-adjustment)
    - [Menu Navigation](#menu-navigation-18)
    - [Setup Parameters](#setup-parameters-11)
    - [Classification and Sort Group](#classification-and-sort-group)
    - [BOC, Sub-Control Point and Purpose](#boc-sub-control-point-and-purpose)
  - [Edit 1358 Request](#edit-1358-request)
    - [Menu Navigation](#menu-navigation-19)
    - [Setup Parameters](#setup-parameters-12)
    - [Authority & Sub-Authority](#authority-sub-authority)
    - [Classification and Sort Groups](#classification-and-sort-groups-5)
  - [Create/Edit Authorization](#createedit-authorization)
    - [Menu Navigation](#menu-navigation-20)
    - [Setup Parameters](#setup-parameters-13)
    - [Display 1358 Balances](#display-1358-balances)
  - [Daily Activity Enter/Edit](#daily-activity-enteredit)
    - [Menu Navigation](#menu-navigation-21)
    - [Setup Parameters](#setup-parameters-14)
    - [Select Authorization](#select-authorization)
  - [Recalculate 1358 Balance](#recalculate-1358-balance)
    - [Menu Navigation](#menu-navigation-22)
    - [Setup Parameters](#setup-parameters-15)
  - [Display 1358 Balance](#display-1358-balance)
    - [Menu Navigation](#menu-navigation-23)
    - [Setup Parameters](#setup-parameters-16)
  - [List Open 1358s](#list-open-1358s)
    - [Menu Navigation](#menu-navigation-24)
    - [Setup Parameters](#setup-parameters-17)
  - [Print 1358](#print-1358)
    - [Menu Navigation](#menu-navigation-25)
    - [Setup Parameters](#setup-parameters-18)
    - [Display or Print 1358](#display-or-print-1358)
  - [Print Obligated 1358s](#print-obligated-1358s)
    - [Menu Navigation](#menu-navigation-26)
    - [Display or Print Obligated 1358s](#display-or-print-obligated-1358s)
  - [Outstanding Approved Requests Report](#outstanding-approved-requests-report)
    - [Menu Navigation](#menu-navigation-27)
    - [Setup Parameters](#setup-parameters-19)
  - [Transaction Report – eCMS/IFCAP](#transaction-report-ecmsifcap)
    - [Menu Navigation](#menu-navigation-28)
    - [Setup Parameters](#setup-parameters-20)
  - [Status of Requests Reports Menu: Supplementary Options](#status-of-requests-reports-menu-supplementary-options)
  - [Print/Display Request Form](#printdisplay-request-form)
    - [Menu Navigation](#menu-navigation-29)
    - [Setup Parameters](#setup-parameters-21)
  - [Status of All Obligation Transactions](#status-of-all-obligation-transactions)
    - [Menu Navigation](#menu-navigation-30)
    - [Display Data](#display-data-1)
  - [PO with Associated Transactions](#po-with-associated-transactions)
    - [Menu Navigation](#menu-navigation-31)
    - [Setup Parameters](#setup-parameters-22)
    - [Print Report](#print-report)
  - [Requests Ready for Approval List](#requests-ready-for-approval-list)
    - [Menu Navigation](#menu-navigation-32)
    - [Listing](#listing)
  - [Supplementary Options in the Display Control Point Activity Menu](#supplementary-options-in-the-display-control-point-activity-menu)
    - [Purchase Order Status](#purchase-order-status)
    - [Menu Navigation](#menu-navigation-33)
    - [Status Listing](#status-listing)
  - [Temporary Transaction Listing](#temporary-transaction-listing)
    - [Menu Navigation](#menu-navigation-34)
    - [Listing](#listing-1)
  - [Transaction Status Report](#transaction-status-report)
    - [Menu Navigation](#menu-navigation-35)
    - [Listing](#listing-2)
  - [Running Balances](#running-balances)
    - [Menu Navigation](#menu-navigation-36)
    - [Listing](#listing-3)
  - [Item History](#item-history-1)
    - [Menu Navigation](#menu-navigation-37)
    - [Listing](#listing-4)
  - [PPM Status of Transactions Report](#ppm-status-of-transactions-report)
    - [Menu Navigation](#menu-navigation-38)
    - [Listing](#listing-5)
  - [Supplementary Options in the Funds Control Menu](#supplementary-options-in-the-funds-control-menu)
  - [Enter FCP Adjustment Data](#enter-fcp-adjustment-data)
    - [Menu Navigation](#menu-navigation-39)
    - [Sort Group](#sort-group-1)
    - [BOC](#boc-1)
    - [Amount](#amount)
  - [Assign Ceiling to Sub-Control Points](#assign-ceiling-to-sub-control-points)
    - [Menu Navigation](#menu-navigation-40)
    - [Select Transaction](#select-transaction)
    - [Enter Sub-Control Point](#enter-sub-control-point)
  - [Recalculate Fund Control Point Balance](#recalculate-fund-control-point-balance)
    - [Menu Navigation](#menu-navigation-41)
  - [Supplementary Options in the Funds Control Reports Menu](#supplementary-options-in-the-funds-control-reports-menu)
  - [Quarterly Report](#quarterly-report)
    - [Menu Navigation](#menu-navigation-42)
    - [Display Report](#display-report)
  - [Ceiling Report](#ceiling-report)
    - [Menu Navigation](#menu-navigation-43)
    - [Display Ceiling Report](#display-ceiling-report)
  - [Audit Transaction List](#audit-transaction-list)
    - [Menu Navigation](#menu-navigation-44)
    - [Setup Parameters](#setup-parameters-23)
  - [Sort Group Report](#sort-group-report)
    - [Menu Navigation](#menu-navigation-45)
    - [Setup Parameters](#setup-parameters-24)
  - [Classification of Request Report](#classification-of-request-report)
    - [Menu Navigation](#menu-navigation-46)
    - [Setup Parameters](#setup-parameters-25)
  - [Cost Center Totals](#cost-center-totals)
    - [Menu Navigation](#menu-navigation-47)
    - [Setup Parameters](#setup-parameters-26)
    - [Print Report](#print-report-1)
  - [BOC Totals](#boc-totals)
    - [Menu Navigation](#menu-navigation-48)
    - [Setup Parameters](#setup-parameters-27)
  - [Sub-Control Point Report](#sub-control-point-report)
    - [Menu Navigation](#menu-navigation-49)
    - [Print Report](#print-report-2)
  - [Reconciliation of PO/Sub-CP Dollar Amounts](#reconciliation-of-posub-cp-dollar-amounts)
    - [Menu Navigation](#menu-navigation-50)
    - [Setup Parameters](#setup-parameters-28)
  - [BOC Detail Totals](#boc-detail-totals)
    - [Menu Navigation](#menu-navigation-51)
    - [Setup Parameters](#setup-parameters-29)
  - [FMS Transaction Data](#fms-transaction-data)
    - [Menu Navigation](#menu-navigation-52)
    - [Setup Parameters](#setup-parameters-30)
  - [Correct Sub-Control Point Amounts](#correct-sub-control-point-amounts)
    - [Menu Navigation](#menu-navigation-53)
    - [Select Transaction](#select-transaction-1)
  - [Supplementary Options in the Record Date Received by Service Menu](#supplementary-options-in-the-record-date-received-by-service-menu)
    - [Single Transaction](#single-transaction)
    - [Menu Navigation](#menu-navigation-54)
    - [Select Transaction](#select-transaction-2)
  - [All Transactions with Final Partials](#all-transactions-with-final-partials)
    - [Menu Navigation](#menu-navigation-55)
    - [Setup Parameters](#setup-parameters-31)
  - [Record Receipt of Multiple Delivery Schedule Items](#record-receipt-of-multiple-delivery-schedule-items)
    - [Menu Navigation](#menu-navigation-56)
    - [Classification and Sort Groups](#classification-and-sort-groups-6)
  - [Multiple Delivery Schedule List](#multiple-delivery-schedule-list)
    - [Menu Navigation](#menu-navigation-57)
    - [Listing](#listing-6)
- [# Menu Outline](#menu-outline)
  - [Option Listing](#option-listing)
- [Error Messages and Their Resolution](#error-messages-and-their-resolution)
  - [Use Errors](#use-errors)
  - [System Errors](#system-errors)
    - [MailMan Error Messages – eCMS Interface](#mailman-error-messages-ecms-interface)
- [GLOSSARY](#glossary)
- [INDEX](#index)

## The Role of the Control Point Clerk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control Point Clerks create requests, turn requests into formal transactions, and maintain Control Point funds records. These activities include creating 2237 and 1358 transactions, creating issue book requests, and creating and funding Sub-control Points.

## How to Use This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual explains how to perform the role of the Control Point Clerk by dividing that role into small, manageable tasks. The authors of this manual have listed these tasks in successive order so that each instruction builds on the functionality and information from the previous instructions. This will allow new Control Point Clerks to use this manual as a tutorial by following the instructions from beginning to end. Experienced Control Point Clerks can use this manual as a reference tool by using the index and table of contents.

## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses a special paragraph numbering system to allow users to understand how the sections of the manual relate to each other. For example, this paragraph is section 1.3. This means that this paragraph is the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections 1.3.1 and 1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third subsection of Chapter 1. All clear? Actually, this means that users are able to divide their reading into manageable lessons and concentrate on one section and all of its subsections. For example, section 1.3.5.4 and all of its subsections would make a coherent lesson.

## Package Management and Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP only allows the person who entered the temporary request (the requestor) to view the status of that request. This is a security measure that prevents users from altering the requests of others. Due to the nature of the information being processed by IFCAP, special attention has been paid to limiting usage by authorized individuals. Individuals in the system who have authority to approve actions, at whatever level, have an electronic signature code. This code is required before the documents pass on to a new level for processing or review. Like the access and verify codes used when gaining access to the system, the electronic signature code will not be visible on the terminal screen. These codes are also encrypted so that even when viewed in the user file by those with the highest levels of access, they are unreadable. Electronic signature codes are required by IFCAP at every level that currently requires a signature on paper.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP automates fiscal, budgetary, inventory, billing and payment activities. To accomplish all of these tasks, IFCAP consists of several functional components, each responsible for a similar set of tasks:

Funds Distribution (Fiscal Component)

Funds Control (Control Point Component)

Processing Requests (Control Point Component)

- Purchase Orders/Requisitions (A&MM Component)
- Accounting (Fiscal Component)
- Receiving (A&MM Component)
- Inventory (A&MM/Control Point Component)

As a Control Point Clerk, you may create and edit requests assigned to a Control Point you are authorized to use. To use a Control Point, the Control Point Official for that Control Point has to give you access. If your user access is limited to the Control Point Clerk level, IFCAP will require the Control Point Official to approve all transactions that you create before transmitting them to Personal Property Management (2237 forms and Issue Book requests) or Accounting (1358 forms). This is because the Control Point Official is responsible for approving all expenditure on the Control Point.

Different kinds of IFCAP users have different menus. The instructions in this manual only use the options that you have as a Control Point Clerk. If you do not know what to enter at an IFCAP prompt, enter 1, 2 or three question marks and IFCAP will list your available options or explain the prompt. The more question marks you enter at the prompt, the more information IFCAP will provide.

The options you use on IFCAP have been divided into groups based upon the type of work you do. When you select these options, IFCAP will ask you a series of questions. If you do not understand the question or are unsure of how to respond, enter a question mark (?) and the computer will explain the question, or allow you to choose from a list of responses.

This is the main menu for the Control Point Clerk.

| Menu Option                          | Description                                                                           |
|------------------------------------------|---------------------------------------------------------------------------------------|
| Process a Request Menu               | This menu contains options for processing transaction requests.                       |
| Display Control Point Activity Menu  | This menu displays request/transaction information.                                   |
| Funds Control Menu                   | This menu contains options used to balance the Control Point.                         |
| Status of Requests Report Menu       | This menu contains options to generate reports of the requests for the Control Point. |
| Record Date Received by Service Menu | This menu allows you to record the receipt of items ordered on IFCAP transactions.    |

## Features 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Cost Centers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In IFCAP 5.1, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP does not use a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'

### Sub allowance/Fund Control Point Reconciliation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The report FMS Transaction Data shows transactions affecting the Fund Control Point balance, but it is for review only. The FMS system passes Fund Control Point adjustments to IFCAP on a daily basis. These adjustments arise from FMS accounting activity that does not originate in IFCAP. A late receipt of goods, for example, could result in an interest expense. The IFCAP system would have no record of this type of charge to the Fund Control Point and would have to rely on FMS to provide adjustment data. The adjustments are returned in an FMS document, Sub allowance Reconciliation, which automatically updates Fund Control Point balances.

### Rollover of Funds from Previous Quarters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Budget Analyst for your Control Points might use IFCAP to designate your Control Point to receive rollover funds from a previous quarter. IFCAP allows Budget Analysts to designate Control Points to transmit and receive remaining funds at the end of each quarter.

### eCMS Interface to IFCAP (2237 Processing)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of October 2012, the process to obtain bids and award contracts occurs within the electronic Contract Management System (eCMS). With the implementation of an interface between IFCAP and eCMS, the 2237s created by control point users may be sent automatically to eCMS at the time the Accountable Officer e-signs and processes the 2237, and then determines it should go to Purchasing & Contracting. A new Status, “*Sent to eCMS (P&C),”* will be placed onto the 2237. The 2237 data will be transmitted in an HL7 message to eCMS. If the Accountable Officer decides to send the 2237 to eCMS, then IFCAP will store certain information about that transaction in a new IFCAP/ECMS TRANSACTION FILE \[414.06\].

### Returning a 2237 from eCMS to the Accountable Officer 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the staff decides that a 2237 should be returned to the Accountable Officer, the 2237 is returned to IFCAP automatically via another HL7 message. The 2237 is then available to the Accountable Officer to complete the processing of the 2237 within IFCAP. Using the “Process a Request in PPM” option, a status, “To IFCAP Ordering Officer,” may then be placed on the 2237 and an IFCAP Purchasing Agent may include the 2237 in a Purchase Order. Alternatively, if appropriate, the status, “Assigned to PPM,” may be placed on the 2237 and a Requisition Clerk can include the 2237 in a Requisition.

The Users listed on a 2237 as the Accountable Officer and the Initiator will receive a VistA MailMan message if eCMS returns that 2237 to the Accountable Officer. The phone number and e-mail address of the eCMS Contact will be included in the MailMan message.

Subj: 2237 RETURNED TO ACCOUNTABLE OFFICER 999-12-4-223-0014 \[#403094\]

08/13/12@13:53 10 lines

From: IFCAP/ECMS INTERFACE In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

STATION 999 SUBSTATION 999HS

eCMS Date/Time Returned to AO Aug 13, 2012@12:53:21

999-12-4-223-0014

ECMS, Test

Ecms.test@va.gov

123-456-0001

Returned to the Accountable Officer Level in IFCAP

Not eligible for contracting process in eCMS. Handle in IFCAP.

Enter message action (in IN basket): Ignore//

### Returning a 2237 from eCMS to the Control Point Level 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** If the eCMS contracting staff decides that a 2237 should be returned to the Control Point level, the 2237 is returned to IFCAP automatically via another HL7 message. The Control Point users are required to edit the 2237 and reapprove it. The Accountable Officer will then be able to process it again and send it back to eCMS.

The Users listed on the 2237 as the Accountable Officer, Control Point Official and Initiator will receive a VistA MailMan message if eCMS returns a 2237 to the Control Point level. The pphone number and e-mail address of the eCMS Contact will be included in the MailMan message.

Subj: 2237 RETURNED TO CONTROL POINT FOR 999-12-4-333-0080 \[#403100\]

08/13/12@16:00 10 lines

From: IFCAP/ECMS INTERFACE In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

STATION 999

eCMS Date/Time Returned to CP Aug 13, 2012@15:00:35

999-12-4-333-0080

TEST,ECMS

ecms.test@va.gov

123-456-0900

Returned to the Control Point Level in IFCAP

Delete line item 14 and modify line item 10 to be Qty 24 pr.

Enter message action (in IN basket): Ignore//

### Cancelling a 2237 in eCMS & IFCAP 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After communicating with the FCP User, the eCMS contracting staff may determine that the 2237 should be Cancelled; the eCMS User will then generate a Cancellation of the 2237 in IFCAP automatically via another HL7 message. The 2237 will have the status of Canceled and the existing IFCAP background processes will update the Running Balance to reflect the entry as CANCELLED and the amount will be set to zero. If due-ins were established when the 2237 was Approved, they will be reversed.

The Users listed on a 2237 as the Accountable Officer, Control Point Official, and Initiator will receive a VistA MailMan message if eCMS cancels a 2237. The phone number and e-mail address of the eCMS Contact will be included in the MailMan message.

Subj: 2237 CANCEL FROM eCMS FOR 2237 999-12-3-110-0021 \[#403586\] 08/28/12@14:51 10 lines

From: IFCAP/ECMS INTERFACE In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

STATION 999

eCMS Date/Time Canceled Aug 28, 2012@13:50:53

999-12-3-110-0021

ECMS, Test

ecms.test@va.gov

456-789-0123

Cancelled the PR and IFCAP 2237 will be cancelled.

Enter message action (in IN basket): Ignore//

# How To Create Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To determine what type of request to make, follow the instructions in the section below. Turn to the section on the form they indicate and create that form.

## Which 2237 Request Form Should You Use?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To choose the correct type of request form, you need to determine whether the item you want is on record in IFCAP as an item that someone has already purchased using IFCAP. If so, you are in luck, because that means that there is less information you will need to complete about the item to make your request. You determine whether there is a record for the item by consulting the Item Master File. If you are requesting a monthly estimated service, skip to the section on creating a 1358 order request.

## How to Consult the Item Master File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP has a file of most of the items that people at your facility have purchased. This file is called the Item Master File. You need to consult this file to determine what kind of request to make. If you still do not know what vendor to select for your request after reading this section, contact the Acquisition section (Purchasing) in Acquisition and Material Management (A&MM). Using the Item History option on the Requestor menu you can see a listing of the last 5 orders placed for an item or look at the orders for an item placed within a specific date range.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Requestor's Menu Option: ITEM History

Select STATION NUMBER: 999//

Select CONTROL POINT: 110 NAME .01 0160A1 10 0100 010042116

Select one of the following:

L Last 5 Purchase Orders

D Date Range

Select ITEM HISTORY Viewing Method: L// Date Range

Select ITEM MASTER NUMBER: 309 ??

Select ITEM MASTER NUMBER: CONTR

1 CONTRACT ITEM 3094 CONTRACT ITEM

2 CONTRACT ITEM W/ DUPACO 707 CONTRACT ITEM W/ DUPACO

3 CONTROL, QCS NORMAL ASSAY 18 CONTROL, QCS NORMAL ASSAY

CHOOSE 1-3: 1 3094 CONTRACT ITEM

### Setup Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number and then a Control Point. At the Select Item Master Number: prompt, enter the Item Master number for the item, the name of the item, a stock number, or some other feature of the item that IFCAP can search. IFCAP will search the Item Master File for all item descriptions that have the information you enter at this prompt and ask you to choose one if there are several matches. You can also type three question marks at this prompt and read the entire item master list. If IFCAP does not find a match, you have to create either a Non-Repetitive Order or a Repetitive and Non-Repetitive Order. Skip to the sections on these two request types and create one of those requests instead.

Select STATION NUMBER: 999//

Select CONTROL POINT: 110 NAME .01 0160A1 10 0100 010042116

Select one of the following:

L Last 5 Purchase Orders

D Date Range

Select ITEM HISTORY Viewing Method: L// Date Range

Select ITEM MASTER NUMBER: 309 ??

Select ITEM MASTER NUMBER: CONTR

1 CONTRACT ITEM 3094 CONTRACT ITEM

2 CONTRACT ITEM W/ DUPACO 707 CONTRACT ITEM W/ DUPACO

3 CONTROL, QCS NORMAL ASSAY 18 CONTROL, QCS NORMAL ASSAY

CHOOSE 1-3: 1 3094 CONTRACT ITEM

DATE ORDERED (BEGIN RANGE) : T-30// T-600

DATE ORDERED (END RANGE) : T//

DEVICE: UCX/TELNET Right Margin: 80//

Item History

JUN 28, 2000@16:00 Page 1

Site: 999 Control Point: 110 NAME .01

Item Number: 3094 Description: CONTRACT ITEM

Qty. Unit

Prev. of Quantity

Date Ordered PO Number Recd. Purch. Unit Cost Total Cost Ordered

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

JUN 6,2000 999-U00042 0 EA 1.10 13.20 12

VENDOR: IFVENDOR2,ONE

JUN 6,2000 999-U00041 0 EA 2.66 31.92 12

VENDOR: IFVENDOR2,ONE

MAR 21,2000 999-U00033 0 EA 2.66 31.92 12

VENDOR: IFVENDOR2,ONE

MAR 21,2000 999-P08005 0 EA 3.56 42.72 12

VENDOR: IFVENDOR2,ONE

MAR 7,2000 999-U00032 0 EA 2.66 31.92 12

VENDOR: IFVENDOR2,ONE

Item History

JUN 28, 2000@16:00 Page 2

Site: 999 Control Point: 110 NAME .01

Item Number: 3094 Description: CONTRACT ITEM

Qty. Unit

Prev. of Quantity

Date Ordered PO Number Recd. Purch. Unit Cost Total Cost Ordered

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FEB 10,2000 999-U00016 0 EA 2.66 26.60 10

VENDOR: IFVENDOR2,ONE

FEB 10,2000 999-U00015 0 EA 2.66 5.32 2

VENDOR: IFVENDOR2,ONE

FEB 4,2000 999-U00005 0 EA 2.66 5.32 2

VENDOR: IFVENDOR2,ONE

FEB 4,2000 999-U00003 0 EA 2.66 2660.00 1000

VENDOR: IFVENDOR2,ONE

### Item Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you select an item, IFCAP will display information for the item. Look at the VENDOR: field. Is "WAREHOUSE" one of the vendors listed for the item? If so, this means that this item is a "Posted Stock" item, or an item stocked at the warehouse for the control point. If one of the vendors is "WAREHOUSE", you have to create an Issue Book/Interval Issue Request for this item. Skip down to the section on Issue Book/Interval Issue Requests.

Select STATION NUMBER: 999//

Select CONTROL POINT: 110 NAME .01 0160A1 10 0100 010042116

Select one of the following:

L Last 5 Purchase Orders

D Date Range

Select ITEM HISTORY Viewing Method: Last 5 Purchase Orders

Select ITEM MASTER NUMBER: CONTR

1 CONTRACT ITEM 3094 CONTRACT ITEM

2 CONTRACT ITEM W/ DUPACO 707 CONTRACT ITEM W/ DUPACO

3 CONTROL, QCS NORMAL ASSAY 18 CONTROL, QCS NORMAL ASSAY

CHOOSE 1-3: 1 3094 CONTRACT ITEM

ITEM HISTORY

JUN 28, 2000@16:00 Site: 999 Control point: 110 NAME .01

Item Number: 3094 Description: CONTRACT ITEM

Quantity

Previously Unit of Quantity

Date Ordered PO Number Received Purchase Unit Cost Total Cost Ordered

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

JUN 06, 2000 999-U00042 0 EA 1.10 13.20 12

Vendor: IFVENDOR2,ONE

JUN 06, 2000 999-U00041 0 EA 2.66 31.92 12

Vendor: IFVENDOR2,ONE

MAY 01, 2000 999-P05178 0 EA 2.66 31.92 12

Vendor: IFVENDOR2,ONE

APR 04, 2000 999-U00035 0 EA 2.66 31.92 12

Vendor: IFVENDOR2,ONE

MAR 21, 2000 999-U00034 0 EA 2.66 31.92 12

Vendor: IFVENDOR2,ONE

### Order Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If IFCAP does not list "WAREHOUSE" as one of the vendors, you can create either a Repetitive order or a Repetitive and Non-Repetitive Order.

## Creating Repetitive (PR Card) Order 2237 Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If EVERY item in your request is in the Item Master File, you can create a Repetitive Order request. You can also create a Repetitive and Non-Repetitive Order request, even if you found matches for all of your items on the Item Master File.

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the New 2237 option on the Process a Request Menu to enter a Station number, Fiscal Year, Quarter and Control Point. If the Control Point selected is attached to more than one Inventory Point, the user will be asked to select the Inventory Point that will be attached to the order. The user can simply press the \<enter\> key at the prompt and no Inventory Point will be attached to the order

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Control Point Clerk's Menu Option: PROCess a Request Menu

New 2237 (Service) Request

Edit a 2237 (Service)

Copy a Transaction

1358 Request Menu

Print/Display Request Form

Change Existing Transaction Number

Repetitive Item List Menu

Cancel Transaction with Permanent Number

Requestor's Menu

Item Display

Vendor Display

Outstanding Approved Requests Report

Transaction Report - eCMS/IFCAP

Select Process a Request Menu Option: NEW 2237 (Service) Request

Select FISCAL YEAR: 00//

Select QUARTER: 3//

Select CONTROL POINT: 060 FISCAL SVC 0160A1 10 0100 010042100

1\) 999-IFUSER,ONE

2\) 999-LAB PRIMARY

Select INVENTORY POINT: (1-2): 2 999-LAB PRIMARY

This transaction is assigned transaction number: 999-00-3-060-0031

The form types 1358 and NO FORM are no longer used within this option

FORM TYPE: ???

Choose from:

2 NON-REPETITIVE (2237) ORDER

3 REPETITIVE (PR CARD) ORDER

4 REPETITIVE AND NON-REP ORDER

5 ISSUE BOOK/INTERVAL ISSUE

FORM TYPE: 3 REPETITIVE (PR CARD) ORDER

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group. Press the Enter key at the Date of Request: prompt if you want to accept the default of today's date.

CLASSIFICATION OF REQUEST: ???

This Classification of Request field allows you to classify and/or categorize all transactions (requests) for supplies, services, etc.

This is the previous 'Type of Request" field.

CHOOSE FROM:

TEST CLASS

CLASSIFICATION OF REQUEST:

SORT GROUP: ???

This Sort Group field may be used to group together all transactions (requests) that relate to a specific project, work order, investigator, food group, doctor, etc.

This is the previous 'Project Number' field.

Enter one of the following:

S.EntryName to select a Sort Group

To see the entries in any particular file, type \<Prefix.?\>

If you simply enter a name then the system will search each of the above files for the name you have entered. If a match is found the system will ask you if it is the entry that you desire.

However, if you know the file the entry should be in, then you can speed processing by using the following syntax to select and entry:

\<Prefix\>.\<entry name\>

or

\<Message\>.\<entry name\>

or

\<File Name\>.\<entry name\>

Also, you do NOT need to enter the entire file name or message

to direct the look up. Using the first few characters will suffice.

SORT GROUP:

DATE OF REQUEST: APR 18,1995// (APR 18, 1995)

### Requestor Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter your name at the Requestor: prompt. If you do not enter a name at the Requestor: prompt, your name will be entered into that field automatically by the IFCAP software.

At the Requesting Service: prompt, you must enter the name or the number of the service that will use the item.

REQUESTOR: IFUSER,TWO

> **NOTE:** The Requesting Service field is mandatory in IFCAP. It is also a required field for the eCMS interface. If the Accountable Officer attempts to send a 2237 to eCMS and this field is blank, the 2237 will generate a transmission error. The Accountable Officer will have to return the 2237 to the CP user for edit and re-approval.

If User attempts to pass this field without entering a value – they will be prompted to fill in this field

REQUESTING SERVICE: ??

Select the name of the Service that submitted this request.

REQUESTING SERVICE: LabORATORY 113

DATE REQUIRED: T+12 (APR 30, 1994)

PRIORITY OF REQUEST: ST// ???

This is the urgency or priority for this request.

CHOOSE FROM:

EM EMERGENCY

SP SPECIAL

ST STANDARD

### Special Remarks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Special Remarks: prompt, enter any special handling information about the item, such as whether the item needs refrigeration, special handling, or if a VA employee has to go to the vendor to get the item. The Purchasing Agent can transfer these remarks to the purchase order that the vendor receives. Enter the cost center at the Cost Center: prompt if this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses. Cost centers allow Fiscal staff to create total expense records for a section or service.

> **NOTE:** In IFCAP V. 5.1, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.

SPECIAL REMARKS:

1\>These are special remarks.

2\>

EDIT Option:

COST CENTER: ??

Select the appropriate cost center for this request

ANSWER WITH COST CENTER

CHOOSE FROM:

805600 Office of Director for Operations

820300 LAB

COST CENTER: 820300 LAB

### Selecting a Vendor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Vendor: prompt, enter the name of the vendor, or the first few letters of the name of the vendor's name. You can type three question marks (???) at the prompt to list all the vendors in the system. If you do not know which vendor has the item you want, follow the instructions in section 3.4, “How to Consult the Item Master File”. Press the Enter key at the vendor address prompts. Press the Enter key at the Line Item Number: prompt.

VENDOR ADDRESS1: 3900 HAPPY LANE//

VENDOR ADDRESS2: SUITE 200//

VENDOR ADDRESS3:

VENDOR CITY: ANYCITY//

VENDOR STATE: DISTRICT OF COLUMBIA//

VENDOR ZIP CODE: 88888//

VENDOR CONTACT: IFVENDOR,ONE//

VENDOR PHONE NO.: 555 555-5555//

Select LINE ITEM NUMBER: 1

LINE ITEM NUMBER: 1//

### Item Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Item Master File No.: prompt, enter the number of the item you are requesting.

ITEM MASTER FILE NO.: ???

ANSWER WITH ITEM MASTER NUMBER, OR SHORT DESCRIPTION, OR

VENDOR STOCK \#, OR NDC, OR NSN

DO YOU WANT THE ENTIRE ITEM MASTER LIST? y (YES)

CHOOSE FROM:

10 TEST ITEM \#10

11 ETHER U/P: 1/BT

211 METHANOL U/P: 1/BT

ITEM MASTER FILE NO.: 11 ETHER U/P: 1/BT 210

### Item History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the “Would you like to see the procurement history for this item?:” prompt, enter Y if you want to know the date, vendor, quantity ordered, item price or total purchase price of this item the last five times it was requested. Enter a budget object code (BOC). Budget object codes are defined and describe what type of item or service you are requesting. Enter a quantity. This quantity represents numbers of units, so if you order one unit that has forty items per unit (say, syringes per box), then you are going to receive 40 syringes.

Would you like to see the procurement history for this item? NO// y (YES)

A history for this item does not yet exist.

> **NOTE:** This item has a packaging multiple/unit of purchase of 1/BT

BOC: ???

Major budget object code classifications are:

10 thru 13 - Personal Services and Benefits

21 - Travel and Transportation of Persons

22 - Transportation of Things

23 - Rent, Communications, and Utilities

24 - Printing and Reproduction

25 - Other Services

26 - Supplies and Materials

31 thru 33 - Acquisition of Capital Assets

ANSWER WITH BUDGET OBJECT CODE

CHOOSE FROM:

2343 ADP Equipment Rental

2632 Other Medical and Dental Supplies

BOC: 2632 Other Medical and Dental Supplies

QUANTITY: 1

QTY BEG BAL: 1

### Delivery Schedules 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the “Select Delivery Schedule:” prompt, press the Enter key if you want all the items on your request delivered at once. If you select a delivery schedule, you are notifying the vendor that you want them to deliver different amounts of the items on different days. For example, if you want to order 100 cases of computer paper, but do not want all of it delivered at once, you can “stagger” the delivery by entering 1 at the Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date, enter 2 at the next Select Delivery Schedule: prompt and enter a date and the amount you would like delivered on that date, etc. Make sure that the total number of items among all the delivery dates equals the total number of items you are ordering.

At the Select Line Item Number: prompt, enter “2” if you want another item on this request. Otherwise, hit the Enter key. Enter the location you want the item to be delivered at the Deliver to/Location: prompt. At the Justification: prompt, enter your name and telephone number and information about how the item will be used. This will help the Personal Property Management Accountable Officer. The PPM Accountable Officer will adjust your request to save money, solicit another vendor or purchase a similar item if there is a problem with the vendor or item you specified. Explaining how you plan to use the item will help the VA acquire the item faster and cheaper. Enter your name at the Originator of Request: prompt. Add comments if you like. Enter N at the Would You Like To Edit Another Request?: prompt to return to the Requestor's Menu.

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

COMMITTED (ESTIMATED) COST: 5// 100 \$ 100.00

DATE COMMITTED: T+12 (JUL 11, 2000)

TRANSACTION BEG BAL: 100.00

Select SUB-CONTROL POINT: DELIVER TO/LOCATION: Fiscal Office (02)

JUSTIFICATION:

1\>We're out of ether.

2\>

EDIT Option:

ORIGINATOR OF REQUEST: IFUSER,TWO

COMMENTS:

1\>

Would you like to review this request? No// (No)

Current Control Point balance: \$1007426.00

Estimated cost of this request: \$100.00

Is this request ready for approval? Yes// N (No)

Would you like to edit another request? YES// n (NO)

## Creating Non-Repetitive Order 2237 Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If none of the items are in the Item Master File, you can use a Non-Repetitive Order request. You can also create a Repetitive and Non-Repetitive Order request, even if you did not find matches for any of your items on the Item Master File. This might keep Logistics staff from rejecting your request if you mistakenly listed an item as Non-Repetitive that in fact was in the Item Master File.

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the New 2237 (Service) request option on the Process a Request Menu to enter a Station number, Fiscal Year, Quarter and Control Point. If the Control Point selected is attached to more than one Inventory Point, the user will be asked to select the Inventory Point that will be attached to the order. The user can simply press the \<enter\> key at the prompt and no Inventory Point will be attached to the order.

Select Process a Request Menu Option: NEW 2237 (Service) Request

Select STATION NUMBER: 999ANYCITY,DC

Select FISCAL YEAR: 94//

Select QUARTER: 3//

Select CONTROL POINT:

1\) 999-IFUSER,ONE

2\) 999-LAB PRIMARY

Select INVENTORY POINT: (1-2): 1 999-IFINV,ONE

### Form Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system will assign a transaction number to this request. At the Form Type: prompt, enter Non-Repetitive Order.

Select CONTROL POINT: 060 FISCAL SVC 0160A1 10 0100 010042100

This transaction is assigned transaction number: 999-00-3-060-0033

The form types 1358 and NO FORM are no longer used within this option

FORM TYPE: ??

Choose from:

2 NON-REPETITIVE (2237) ORDER

3 REPETITIVE (PR CARD) ORDER

4 REPETITIVE AND NON-REP ORDER

5 ISSUE BOOK/INTERVAL ISSUE

FORM TYPE: 2 NON-REPETITIVE (2237) ORDER

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group. Press the Enter key at the Date of Request: prompt to select today's date. Enter your name at the Requestor: prompt.

The Classification of Request field is not mandatory.

CLASSIFICATION OF REQUEST:

SORT GROUP:

DATE OF REQUEST: 2940418// (APR 18, 1994)

REQUESTOR: IFUSER,TWO

> **NOTE:** Requesting Service is an IFCAP-required field, and the 2237 cannot go forward to the electronic Contract Management System (eCMS), unless this field is populated.

If the User attempts to pass this field without entering a value, the software

will prompt again for a response.

REQUESTING SERVICE: ??

Select the name of the Service that submitted this request.

REQUESTING SERVICE: LabORATORY 113

### Priority of Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date required and the priority of the request. Priorities are based on the days remaining before the delivery date requested for the item. The priority categories in IFCAP, ranging from shortest to longest delivery time remaining, are “Emergency”, “Special” and “Standard”. Different stations assign different time durations to these categories. Check with your Fiscal office to determine the durations at your station for these categories. At the Special Remarks: prompt, explain how the service will use the item, names of other items that would fulfill the same need, and any other information that would help the Purchasing Agent fulfill your request. Purchasing Agents sometimes change orders to fulfill the service’s need faster, find a better item or change the vendor for a better price. Explaining the use of the item will make these tasks easier to accomplish. Enter the cost center at the Cost Center: prompt if this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses. Cost centers allow Fiscal staff to create total expense records for a section or service.

> **NOTE:** In IFCAP V. 5.1, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.

DATE REQUIRED: T+12 (APR 30, 1994)

PRIORITY OF REQUEST: ST// ???

This is the urgency or priority for this request.

CHOOSE FROM:

EM EMERGENCY

SP SPECIAL

ST STANDARD

PRIORITY OF REQUEST: ST// STANDARD

SPECIAL REMARKS:

1\>These are special remarks.

2\>

EDIT Option:

COST CENTER: ???

ANSWER WITH COST CENTER

CHOOSE FROM:

805600 Office of Director for Operations

820100 Medical Service

COST CENTER: 820100 Medical Service

### Vendor Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Vendor: prompt, enter the name of the vendor that supplies the item you are requesting. If your vendor is not in the vendor file, IFCAP will ask you to confirm the vendor name. Enter the information for the new vendor. Enter 1 at the Line Item Number: prompt.

VENDOR: IF VENDOR,TWO//

VENDOR ADDRESS1: 12605 ANYSTREET Rd.

VENDOR ADDRESS2:

VENDOR CITY: MYTOWN

VENDOR STATE: MD MARYLAND

VENDOR ZIP CODE: 22222-2222

VENDOR CONTACT: IFVENDOR,THREE

VENDOR PHONE NO.: (555)- 555-5555

Select LINE ITEM NUMBER: 1

LINE ITEM NUMBER: 1//

### Item Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Description: prompt, define the item as thoroughly as you can. Since you are creating a non-repetitive order, the item you are requesting is not in the Item Master File. This means that the Purchasing Agent will have to make a “best guess” of exactly what kind of item you need, based on the information you provide in this field. Describe what the service plans to do with the item and any special features of the item (for example, does it have to be flexible or blue or heat-resistant or non-toxic). At the Unit of Purchase: prompt, enter the measuring standard for the item. For example, if you order 1 unit and select LB (pound) as unit of purchase, your request will list one pound of the item.

> **NOTE:** The Line Item <u>DESCRIPTION</u> is now a required field in the 2237. If the User attempts to leave the DESCRIPTION field blank, the User is prompted to fill in the field.

Item Description:

1\>

Item DESCRIPTION is required!

DESCRIPTION:

Enter some text

EDIT Option:

QUANTITY: 400

UNIT OF PURCHASE: ???

This is the unit of measurement for items being procured.

e.g., each, dozen, box, bottle, case, pound (lb.), square ft., etc.

CHOOSE FROM:

AM AMPOULE

AT ASSORTMENT

AY ASSEMBLY

LB POUND

UNIT OF PURCHASE: BX BOX

> **NOTE:** Many users accidentally order too much or too little quantity by choosing the wrong unit of purchase. For example, a carboy of disinfectant is much greater than a gallon of disinfectant. Double-check the printout of your request to make sure that the quantity and the unit of purchase are correct.

### Stock Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the stock number for the item. Enter the estimated cost per unit. The cost per unit will depend on the item and how many items are in a unit. If the item is ordered at one unit per item, the cost per unit is the cost per item. If the vendor sells the item by the case, the cost per unit is the cost per case, etc. Enter a budget object code (BOC). Budget object codes are defined in VHA Handbook 4671.2

STOCK NUMBER: 094104

EST. ITEM (UNIT) COST: 20

BOC: ???

Major budget object code classifications are:

10 thru 13 - Personal Services and Benefits

21 - Travel and Transportation of Persons

22 - Transportation of Things

23 - Rent, Communications, and Utilities

24 - Printing and Reproduction

25 - Other Services

26 - Supplies and Materials

31 thru 33 - Acquisition of Capital Assets

ANSWER WITH BUDGET OBJECT CODE

BOC: Operating Supplies and Materials

QTY BEG BAL: 400

### Delivery Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select Delivery Schedule: prompt, press the Enter key if you want all the items on your request delivered at once. If you select a delivery schedule, you are notifying the vendor that you want them to deliver different amounts of the items on different days. For example, if you want to order 100 cases of computer paper, but do not want all of it delivered at once, you can “stagger” the delivery by entering 1 at the Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date, enter 2 at the next Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date, etc. Make sure that the total number of items among all the delivery dates equals the total number of items you are ordering.

Enter a 2 at the Select Line Number: prompt if you want to add another item to your request. Otherwise, press the Enter key.

Enter the estimated shipping and/or handling costs in dollars. Enter where you want the warehouse to deliver the item at the Deliver To/Location: prompt. At the Justification: prompt, explain why the service or item is needed by the service. Enter your name and telephone number. Enter your name at the Originator Of Request: prompt. Add comments if you like. Enter N at the Would You Like To Enter Another Request?: prompt to return to the Requestor's Menu.

Select DELIVERY SCHEDULE: ???

This field is the Delivery Schedule of the Order file, \#400.8.

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

COMMITTED (ESTIMATED) COST: 16000//

DATE COMMITTED: TODAY// (JUN 29, 2000)

TRANSACTION BEG BAL: 16000.00

Select SUB-CONTROL POINT:

EST. SHIPPING AND/OR HANDLING: 40

DELIVER TO/LOCATION: Bldg.40

JUSTIFICATION:

1\>Roofing material for homeless veteran's shelter

2\>

EDIT Option:

REQUESTOR:

ORIGINATOR OF REQUEST:

COMMENTS:

1\>

Would you like to review this request? No// (No)

Current Control Point balance: \$1007426.00

Estimated cost of this request: \$16000.00

Is this request ready for approval? Yes// (Yes)

Would you like to enter another request? YES// n (NO)

## Creating Repetitive and Non-Repetitive Order 2237 Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If one or more, but not all the items on your request are on the Item Master File, you can create a Repetitive and Non-Repetitive Order Request. This is a versatile form type, because it allows other IFCAP users to "split" your request into multiple orders. Also, it is easier for Personal Property Management staff to correct a Repetitive and Non-Repetitive Order if you mistakenly list an item as non-repetitive that in fact is on the Item Master File, or if IFCAP fails to match an item to the Item Master File because you've misspelled or misnamed the item.

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station Number, a Fiscal Year, and a quarter. Enter a Control Point. If the Control Point selected is attached to more than one Inventory Point, the user will be asked to select the Inventory Point that will be attached to the order. The user can simply press the \<enter\> key at the prompt and no Inventory Point will be attached to the order

Select Process a Request Menu Option: New 2237 (Service) Request

Select STATION NUMBER: 999 ANYCITY,DC

Select FISCAL YEAR: 94//

Select QUARTER: 3//

CONTROL POINT

### Form Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system will generate a transaction number. At the Form Type: prompt, enter Repetitive And Non-Rep Order.

Select CONTROL POINT: 060 FISCAL SVC// 0160A1 10 0100 010042100

1\) 999-IFUSER,ONE

2\) 999-LAB PRIMARY

Select INVENTORY POINT: (1-2): 1 999-IFUSER,ONE

This transaction is assigned transaction number: 999-00-3-060-0034

The form types 1358 and NO FORM are no longer used within this option

FORM TYPE: ???

Choose from:

2 NON-REPETITIVE (2237) ORDER

3 REPETITIVE (PR CARD) ORDER

4 REPETITIVE AND NON-REP ORDER

5 ISSUE BOOK/INTERVAL ISSUE

FORM TYPE: 4 REPETITIVE AND NON-REP ORDER

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group. Press the Enter key at the Date of Request: prompt. Enter your name at the Requestor: prompt. Enter the service that will use the item or service at the Requesting Service: prompt.

CLASSIFICATION OF REQUEST: ???

This Classification of Request field allows you

to classify and/or categorize all transactions

(requests) for supplies, services, etc.

This is the previous 'Type of Request" field.

CHOOSE FROM:

SHOES

TEST CLASS

This is the name used to identify the type of request. File \#410.2

is pointed to by the Classification of Request field (#8) of the

Control Point Activity file, \#410.

CLASSIFICATION OF REQUEST: TEST CLASS

SORT GROUP:

DATE OF REQUEST: 2940418// (APR 18, 1994)

REQUESTOR: IFUSER,TWO

REQUESTING SERVICE: ??

Select the name or number of the Service that submitted this request.

This is the name of the service that submitted this request.

REQUESTING SERVICE: 11C AMBULATORY CARE

> NOTE: Requesting Service is an IFCAP-required field. The 2237 cannot go forward to the electronic Contract Management System (eCMS), unless this field is populated.

### Priority of Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date required and the priority of the request. Priorities are based on the days remaining before the delivery date requested for the item. The priority categories in IFCAP, ranging from shortest to longest delivery time remaining, are “Emergency”, “Special” and “Standard”. Different stations assign different time durations to these categories. Check with your Fiscal office to determine the durations at your station for these categories. At the Special Remarks: prompt, explain how the service will use the item, names of other items that would fulfill the same need, and any other information that would help the Purchasing Agent fulfill your request. Purchasing Agents sometimes change orders to fulfill the service’s need faster, find a better item or change the vendor for a better price. Explaining the use of the item will make these tasks easier to accomplish. Enter the cost center at the Cost Center: prompt if this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses. Cost centers allow Fiscal staff to create total expense records for a section or service.

> **NOTE:** In IFCAP V. 5.1, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.

DATE REQUIRED: // T+15 (OCT 08, 1994)

PRIORITY: ST// STANDARD PRIORITY

SPECIAL REMARKS:

1\>These are special remarks.

2\>

EDIT Option:

COST CENTER: ???

ANSWER WITH COST CENTER

CHOOSE FROM:

805600 Office of Director for Operations

820300 LAB

COST CENTER: 820300 LAB

### Vendor Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Vendor: prompt, enter the name of the vendor that supplies the item you are requesting. If your vendor is not in the vendor file, IFCAP will ask you to confirm the vendor name. Enter the information for the new vendor. Enter 1 at the Line Item Number: prompt.

> **NOTE:** Make sure that the vendor information you provide is correct. Incorrect vendor information will delay payment to the vendor.

VENDOR: IF VENDOR,TWO//

VENDOR ADDRESS1: 12605 ANYSTREET Rd.

VENDOR ADDRESS2:

VENDOR CITY: MYTOWN

VENDOR STATE: MD MARYLAND

VENDOR ZIP CODE: 66666-4444

VENDOR CONTACT: IF VENDOR,THREE

VENDOR PHONE NO.: (555) 555-5555

Select LINE ITEM NUMBER: 1

LINE ITEM NUMBER: 1//

ITEM MASTER FILE NO.:

### Item Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Description: prompt, define the item as thoroughly as you can. If the item is not in the Item Master File, the Purchasing Agent is going to make a “best guess” of exactly what kind of item you need. This guesswork will be based on the information you provide in this field. Describe what the service plans to do with the item and any special features of the item (for example, does it have to be flexible or blue or heat-resistant or non-toxic). At the Unit of Purchase: prompt, enter the measuring standard for the item. For example, if you order one unit and select LB (pound) as unit of purchase, your request will list one pound of the item.

DESCRIPTION:

If User does not enter any text, the User will be prompted to enter some text.

Item DESCRIPTION is required!

User must enter some text

EDIT Option:

BOC: 2660 Operating Supplies and Materials

QUANTITY: 400

UNIT OF PURCHASE: ???

This is the unit of measurement for items being procured.

e.g., each, dozen, box, bottle, case, pound (lb.), square ft., etc.

CHOOSE FROM:

AM AMPOULE

AT ASSORTMENT

AY ASSEMBLY

LB POUND

UNIT OF PURCHASE: LB POUND

> **NOTE:** Many users accidentally order too much or too little quantity by choosing the wrong unit of purchase. For example, a carboy of disinfectant is much greater than a gallon of disinfectant. Double-check the printout of your request to make sure that the quantity and the unit of purchase are correct.

### Stock Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the stock number for the item. Enter the estimated cost per unit. The cost per unit will depend on the item and how many items are in a unit. If the item is ordered as one unit per item, the cost per unit is the cost per item. If the vendor sells the item by the case, the cost per unit is the cost per case, etc. Enter a budget object code (BOC). Budget object codes are defined in VHA Handbook 4671. 2.

STOCK NUMBER: 094104

EST. ITEM (UNIT) COST: 20

### Delivery Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select Delivery Schedule: prompt, press the Enter key if you want all the items on your request delivered at once. If you select a delivery schedule, you are notifying the vendor that you want them to deliver different amounts of the items on different days. For example, if you want to order 100 cases of computer paper, but do not want all of it delivered at once, you can “stagger” the delivery by entering 1 at the Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date, and enter a 2 at the next Select Delivery Schedule: prompt. Enter a date and the amount you would like delivered on that date, etc. Make sure that the total number of items among all the delivery dates equals the total number of items you are ordering.

Enter a 2 at the Select Line Number: prompt if you want to add another item to your request. Otherwise, press the Enter key.

Enter the estimated shipping and/or handling costs in dollars. Enter where you want the warehouse to deliver the item at the Deliver To/Location: prompt. At the Justification: prompt, enter your name and telephone number and explain why the service or item is needed by the service. Enter your name at the Originator of Request: prompt. Add comments if you like. Enter N at the Would You Like To Enter Another Request?: prompt to return to the Requestor's Menu.

Select DELIVERY SCHEDULE: ???

This field is the Delivery Schedule of the Order file, \#400.8.

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

COMMITTED (ESTIMATED) COST: 400//

TRANSACTION BEG BAL: 400.00

Select SUB-CONTROL POINT:

DELIVER TO/LOCATION: Bldg.40

JUSTIFICATION:

1\>Testing material

2\>

EDIT Option: REQUESTOR:

ORIGINATOR OF REQUEST:

COMMENTS:

1\>

Would you like to review this request? No// (No)

Current Control Point balance: \$1007426.00

Estimated cost of this request: \$400.00

> **NOTE:** Control Point Clerk is not permitted to set the 2237 to YES – Ready for Approval if any Required field is not populated.

Is this request ready for approval? Yes// (Yes)

Would you like to enter another request? YES// n (NO)

## Creating Issue Book/Interval Issue Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Issue Book/Interval Issue Request is for "posted stock" items, or items that the warehouse keeps in stock. You must use an Issue Book/Interval Issue request for posted stock items. You must not use an Issue Book/Interval Issue request for any items that are not posted stock. If you need some items that are posted stock and some items that are not posted stock, create an Issue Book/Interval Issue Request for the posted stock items. Use one of the other forms for the other items. The Government makes certain procurement guarantees to vendors in exchange for discounts on posted stock. Obtaining posted stock items from any source other than the warehouse is a potential violation of those guarantees. If you request a posted stock item on any request other than an Issue Book/Interval Issue request, the computer will reject your request.

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station Number. Enter the Fiscal Year, Fiscal Quarter, and the Control Point. If the Control Point selected is attached to more than one Inventory Point, the user will be asked to select the Inventory Point that will be attached to the order. The user can simply press the \<enter\> key at the prompt and no Inventory Point will be attached to the order.

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

Select Process a Request Menu Option: New 2237 (Service) Request

Select STATION NUMBER: 999ANYCITY,DC

Select FISCAL YEAR: 94//

Select QUARTER: 3//

Select CONTROL POINT: 101 ISC2 A2222 10 0100 01AA20100

1\) 999-IFUSER,ONE

2\) 999-LAB PRIMARY

Select INVENTORY POINT: (1-2): 1 999-IFINV,ONE

### Classification Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system will assign a transaction number to this request.

> **NOTE:** Write this number down. You will need it to determine the status of your request.

At the Interval Issue?: prompt, enter “Y” if this is an item that you do not normally order. Enter “N” if this is an item you order on a regular basis. If you normally enter this item on an issue book order, but need the item before the next scheduled posted stock delivery, enter "Y". This prompt does NOT allow you to create a recurring order: it merely allows you to explain how you use the item.

At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define.

This transaction is assigned transaction number: 999-00-3-060-0035

The form types 1358 and NO FORM are no longer used within this option

FORM TYPE: ???

Choose from:

2 NON-REPETITIVE (2237) ORDER

3 REPETITIVE (PR CARD) ORDER

4 REPETITIVE AND NON-REP ORDER

5 ISSUE BOOK/INTERVAL ISSUE

FORM TYPE: 5 ISSUE BOOK/INTERVAL ISSUE

Issue Book Requests will automatically be ordered from IFVENDOR2,FIVE

INTERVAL ISSUE?: ???

This allows the user to specify (by entering Yes/No) whether the request for items in the Warehouse is an Interval Issue i.e., items requested between scheduled posted stock delivery, rather than a regularly scheduled Issue Book order.

CHOOSE FROM:

1 YES

0 NO

INTERVAL ISSUE?: 1 YES

CLASSIFICATION OF REQUEST: ???

This Classification of Request field allows you to classify and/or categorize all transactions (requests) for supplies, services, etc.

This is the previous 'Type of Request" field.

CHOOSE FROM:

TEST CLASS

CLASSIFICATION OF REQUEST:

### Sort Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group. Press the Enter key at the Date of Request: prompt to accept the default date of today. Enter your name at the Requestor: prompt.

SORT GROUP: ???

This Sort Group field may be used to group together all transactions (requests) that relate to a specific project, work order, investigator, food group, doctor, etc.

This is the previous 'Project Number' field.

Enter one of the following:

S.EntryName to select a Sort Group

To see the entries in any particular file, type \<Prefix.?\>

If you simply enter a name then the system will search each of the above files for the name you have entered. If a match is found the system will ask you if it is the entry that you desire.

However, if you know the file the entry should be in, then you can speed processing by using the following syntax to select and entry:

\<Prefix\>.\<entry name\>

or

\<Message\>.\<entry name\>

or

\<File Name\>.\<entry name\>

Also, you do NOT need to enter the entire file name or message to direct the look up. Using the first few characters will suffice.

SORT GROUP:

DATE OF REQUEST: TODAY// (APR 18, 1994)

REQUESTOR: IFVENDOR,TWO

### Priority 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Requesting Service: prompt, enter the name of the service that will use the item. Enter the date that the service will require the item. Enter the priority that you want to assign to the request. Enter any special remarks about the item that might help the Requirements Analyst fulfill your request or adjust inventory levels to accommodate the needs of your service (for example, refrigeration required, must be picked up from vendor, etc.)

REQUESTING SERVICE: ???

This is the name of the service that submitted this request.

*NOTE:* Requesting Service is now an IFCAP-required field; the 2237 is not permitted to go forward to the electronic Contract Management System (eCMS), if this field is not populated.

CHOOSE FROM:

A&MM 90

AMBULATORY CARE 11C

ANESTHESIOLOGY 123

AUDIOLOGY AND SPEECH PATHOLOGY 126

BLIND REHABILITATION 122

REQUESTING SERVICE: AUDIOLOGY AND SPEECH PATHOLOGY 126

DATE REQUIRED: T+20 (MAY 08, 1994)

PRIORITY OF REQUEST: ST// ???

This is the urgency or priority for this request.

CHOOSE FROM:

EM EMERGENCY

SP SPECIAL

ST STANDARD

PRIORITY OF REQUEST: ST// STANDARD

SPECIAL REMARKS:

1\>

### Cost Center 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the cost center at the Cost Center: prompt. Cost centers allow Fiscal staff to create total expense records for a section or service. At the Select Line Item Number: prompt, Enter 1 for the first item on the request. Remember, you can only request issue items on an issue book request. At the Item Master File No.: prompt, enter the item name or number. You can also type three question marks (???) to see a list of the items you can request on an issue book request. Enter a budget object code (BOC).Budget object codes are defined in VHA Handbook 4671.2.

> **NOTE:** In IFCAP V. 5.1, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.

COST CENTER: 805600 Office of Director for

Select LINE ITEM NUMBER: ???

This is the item number for this request.

Select LINE ITEM NUMBER: 1

LINE ITEM NUMBER: 1//

ITEM MASTER FILE NO.: ???

ANSWER WITH ITEM MASTER NUMBER, OR SHORT DESCRIPTION, OR

VENDOR STOCK \#, OR NDC, OR NSN

DO YOU WANT THE ENTIRE ITEM MASTER LIST? Y (YES)

CHOOSE FROM:

8 ITEM \#8 U/P: 12/CL

37 PEN U/P: 1/EA

39 RULER U/P: 1/EA

40 PAINT U/P: 1/EA

45 TESTING V5 U/P: 2/EA

ITEM MASTER FILE NO.: 39RULER U/P: 1/EA 39

> **NOTE:** This item has a minimum order quantity of 1

> **NOTE:** This item has a packaging multiple/unit of purchase of 1/EA

QUANTITY: 1

BOC: 2670 Maintenance Supplies and Materials

### Additional Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter 2 at the Select Line Item Number: prompt if you want to add another item to your request. Otherwise, press the Enter key. Remember, you can only request issue items on an issue book request. Enter where you want the warehouse to deliver the item at the Deliver To/Location: prompt. At the Justification: prompt, enter your name and telephone number and explain why the service or item is needed by the service. Enter your name at the Originator of Request: prompt. Add comments if you like. Enter N at the “Would You Like To Enter Another Request?:” prompt to return to the Requestor's Menu.

Select LINE ITEM NUMBER: ???

Select DELIVERY SCHEDULE: ???

This field is the Delivery Schedule of the Order file, \#400.8.

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

COMMITTED (ESTIMATED) COST: 3.22//

DATE COMMITTED: T (JUN 29, 2000)

TRANSACTION BEG BAL: 100.00

Select SUB-CONTROL POINT:

EST. SHIPPING AND/OR HANDLING: 40

DELIVER TO/LOCATION: Bldg.40

JUSTIFICATION:

1\>Roofing material for homeless veteran's shelter

2\>

EDIT Option:

ORIGINATOR OF REQUEST:

COMMENTS:

1\>

Would you like to review this request? No// (No)

Current Control Point balance: \$1007426.00

Estimated cost of this request: \$100.00

Is this request ready for approval? Yes// (Yes)

Would you like to enter another request? YES// N (NO)

## Creating 1358 Order Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use a 1358 Order request to budget money for ongoing service expenses, such as the utility bill, copier repair, rent, or postage. A 1358 Order allows the Control Point to "obligate funds," or establish a budget for ongoing services, so there will be money to pay the vendor when the monthly or quarterly statement is due.

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select New 1358 Request from the Control Point Clerk’s Menu. Enter a station number, fiscal year, quarter, Control Point, Authority and if required a Sub-Authority. IFCAP will assign a transaction number to your request. Write this number down. You will need this number to determine the status of your request.

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358's with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: NEW 1358 Request

Select FISCAL YEAR: 00//

Select QUARTER: 3//

Select CONTROL POINT: 060 FISCAL SVC 0160A1 10 0100 010042100

Select AUTHORITY OF REQUEST: 2 FEE BASIS User may enter ?? to see the list of 23 choices.

SUB AUTHORITY: ?? If the Authority selected requires a Sub-Authority the User will be prompted to enter a value.

Select the Sub-Authority for this 1358 Obligation.

You can only select active sub-authorities that relate to the main one.

Choose from:

A FEE MEDICAL/DENTAL (PRE-AUTHORIZED)

B FEE MEDICAL/DENTAL (NOT PRE-AUTHORIZED)

C HOMEMAKER/HOME HEALTH AID

D NON-VA HOSPITALIZATION (PRE-AUTHORIZED)

E NON-VA HOSPITALIZATION (NOT PRE-AUTHORIZED)

F NON-CONTRACT EMERGENCY TRAVEL

SUB AUTHORITY: C HOMEMAKER/HOME HEALTH AID

This transaction is assigned Transaction number: 999-00-3-060-0036

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group.

CLASSIFICATION OF REQUEST: ???

This Classification of Request field allows you to classify and/or categorize all transactions (requests) for supplies, services, etc.

This is the previous 'Type of Request" field.

CHOOSE FROM:

This is the name used to identify the type of request. File \#410.2 is pointed to by the Classification of Request field (#8) of the Control Point Activity file, \#410.

CLASSIFICATION OF REQUEST:

SORT GROUP: ???

This Sort Group field may be used to group together all transactions (requests) that relate to a specific project, work order, investigator, food group, doctor, etc.

This is the previous 'Project Number' field.

Enter one of the following:

S.EntryName to select a Sort Group

W.EntryName to select a Work Order

To see the entries in any particular file, type \<Prefix.?\>

If you simply enter a name then the system will search each of the above files for the name you have entered. If a match is found the system will ask you if it is the entry that you desire.

However, if you know the file the entry should be in, then you can speed processing by using the following syntax to select and entry:

\<Prefix\>.\<entry name\>

or

\<Message\>.\<entry name\>

or

\<File Name\>.\<entry name\>

Also, you do NOT need to enter the entire file name or message to direct the look up. Using the first few characters will suffice.

SORT GROUP:

### Requestor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Per implementation of Segregation of Duties within the 1358 options, the User is no longer asked to Enter the name of an individual at the Requestor: prompt. Your name is automatically entered as the Requestor.

Press the Enter key at the Date of Request: prompt to accept the default date of today.

Enter the date that you want to commit funds to your request at the Date Committed: prompt, or press the Enter key to accept the default of the first date of the current month.

Enter the total cost in dollars for the services at the Committed (Estimated) Cost: prompt.

Enter the cost center at the Cost Center: prompt. Cost centers allow Fiscal staff to create total expense records for a section or service.

> **NOTE:** In IFCAP V. 5.1, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.

DATE OF REQUEST: OCT 15,2010// (OCT 15, 2010)

DATE COMMITTED: 10/01/10// (OCT 01, 2010)

COMMITTED (ESTIMATED) COST: 1000 \$ 1000.00

COST CENTER: 842100 Fiscal

### BOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a budget object code (BOC) at the BOC1: prompt. Enter the amount of the item you want to attribute to the budget object code at the BOC1 Amount: prompt. You may also enter a Sub-control Point if you like.

BOC1: 2580 Miscellaneous Contractual Services by Individuals, Institute and Organize

Select SUB-CONTROL POINT:

### Vendor Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Authority you selected requires a Vendor entry, IFCAP will require you to enter a vendor for the request. If a Vendor is not required, you may leave this field blank. If the Authority you selected also requires a Vendor Contract \#, IFCAP will prompt you to enter a valid Contract \# for the Vendor you entered.

Do you want to enter a vendor for this 1358 request? NO// Y (YES)

VENDOR: IF VENDOR,FOUR 512-555-5555 NO. 7

SPECIAL FACTORS:

ORDERING ADDRESS: 4 SAMPLE ST

ANYTOWN, TX 77777

OK? YES// (YES)

VENDOR CONTRACT NUMBER: ???

ANSWER WITH CONTRACT /BOA NUMBER

CHOOSE FROM:

D339347 -- EXP. DATE: 12-12-10

TK-333333-94 -- EXP. DATE: 12-12-11 10% 25 DAYS

VENDOR CONTRACT NUMBER: TK-333333-94 -- EXP. DATE: 12-12-11 10% 25 DAYS

### Service Start and End Dates/Purpose of 1358

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the appropriate Service Start Date for the 1358. Enter the appropriate Service End Date for the 1358.

At the Purpose: prompt, explain the purpose of the order. This field is now required.

You may enter a name at the Originator Of Request: prompt.

Add comments if you like. Enter N at the Would You Like To Enter Another Request?: prompt to return to the Requestor's Menu.

SERVICE START DATE: 100110

SERVICE END DATE: 103110

PURPOSE:

1\> electric bill for july

2\>

EDIT Option:

ORIGINATOR OF REQUEST: IFUSER,FIVE

COMMENTS:

1\>

Would you like to review this request? No// (No)

Current Control Point balance: \$1007426.00

Estimated cost of this request: \$1000.00

Is this request ready for approval? Yes// (Yes)

Do you want to enter another NEW request? NO//

### New Process Flow for 1358s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![Figure 1 - New 1358 Process Flow](ifcap-version-5-1-control-point-clerk-user-s-guide/002.png)

*Figure 1 - New 1358 Process Flow*

# Turning Temporary Requests into Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No request can go forward for approval without first becoming a transaction. See the Control Point Requestor manual for options located on the Requestor menu.

## Converting Temporary Requests to Permanent Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you log onto the Control Point Clerk menu, IFCAP will tell you which Control Points have new requests. From the Control Point Clerk’s Menu, select Process a Request Menu. Select Change Existing Transaction Number. The requests will have a form type assigned. Read the following sections to turn these requests into transactions.

> **NOTE:** The fields Requesting Service and Line Item DESCRIPTION are not required fields in a Temporary Request. This will mean the Control Point Clerk may encounter missing required fields when converting a temporary request to a 2237 transaction. The Clerk will be advised of the missing field(s) and be allowed to edit the new 2237 and populate the required fields. If the Clerk chooses not to edit the fields at that time the 2237 will not be complete and the Clerk will not be able to set the Approval flag to YES. The Clerk will have to Edit the 2237 and populate the missing fields.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Change Existing Transaction Number

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number and a Control Point. Enter the <u>temporary transaction</u> number of the request you wish to forward to the Control Point Official for approval. If you do not know the number of the request, enter two question marks at the prompt and IFCAP will list the available transactions.

Select Process a Request Menu \<TEST ACCOUNT\> Option: change Existing Transaction

Number

Select STATION NUMBER: 999

Select CONTROL POINT: 1555 IFCP1 CP OFFICIAL 0160A1 10 0100 010022600

Select the existing transaction number to be replaced

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: IFC0720 IFC0720 OBL AVENDOR:

### Request Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you if you would like to review the request, and will allow you to enter new information for the transaction. IFCAP will then assign a permanent transaction number to the transaction. This is the number you will use for future reference to this request.

Would you like to review this request? No// (No)

Enter the information for the new transaction number.

Select STATION NUMBER: 999//

Select FISCAL YEAR: 13//

Select QUARTER: 4//

Select CONTROL POINT: 1555 IFCAP1 CP OFFICIAL 0160A1 10 0100 010022600

0160A1 10 0100 010022600

Transaction 'IFC0720' has been replaced by 999-13-4-1555-0039

WARNING - Transaction 999-13-4-1555-0039 is missing required data!

\>\>\> Line Item \#1 Description is missing.

The request needs to be edited prior to approval.

The form type for this transaction is REPETITIVE AND NON-REP ORDER

### Edit Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will allow you to edit the features of the request, including the quantity of the items, and the vendor. Make sure that the item or service is available from the vendor, that the Control Point has sufficient funds to cover the request, and that the information about the items or services on the request is correct.

Would you like to edit this request? NO// Y (YES)

FORM TYPE: REPETITIVE AND NON-REP ORDER//

CLASSIFICATION OF REQUEST:

SORT GROUP:

DATE OF REQUEST:

REQUESTING SERVICE: CP User must Populate this field as it is required on a 2237.

DATE REQUIRED: JUN 29,1994//

PRIORITY OF REQUEST: EMERGENCY//

SPECIAL REMARKS:

1\>

COST CENTER: 844100 Supply//

VENDOR: IFVENDOR,FOUR //

Select LINE ITEM NUMBER: 1//

LINE ITEM NUMBER: 1//

ITEM MASTER FILE NO.: 200//

BOC: 1091 Federal,Summer Employment Replace

QUANTITY: 1//

INTERMEDIATE PRODUCT CODE:

QTY BEG BAL: 1

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

COMMITTED (ESTIMATED) COST: 3//

TRANSACTION BEG BAL: 3.00

Select SUB-CONTROL POINT:

DELIVER TO/LOCATION:

JUSTIFICATION:

1\>

REQUESTOR: IFREQUESTOR,TWO//

COMMENTS:

1\>

### Request Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will allow you to review the request again, to make sure that all the information on the request is correct.

> **NOTE:** If any Required field is not populated, the User will be advised of the missing data and prompted to Edit the 2237.

IFCAP will then list the cost of the request, and the uncommitted balance available for purchases. IFCAP will not allow you to transmit the request to the Control Point Official for approval if any Required field in not populated. You can enter another request at the Select Control Point Activity Transaction Number: prompt or press the Enter key to return to the Process a Request Menu.

Would you like to review this request? NO// (NO)

Current Control Point balance: \$0.00

Estimated cost of this request: \$3.00

Total uncommitted balance from current and prior quarters: \$4734.20

Is this request ready for approval? NO// Y (YES)

> **NOTE:** User cannot set the Request to “Ready for Approval?//YES" if the Requesting Service or any Item DESCRIPTION field is not populated.

Would you like to replace another transaction number? NO// (NO)

Select Process a Request Menu Option:

## Converting Temporary 1358 Transactions to Permanent Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Control Point Clerk’s Menu, select Process a Request Menu. From the Process a Request Menu, select Change Existing Transaction Number. Enter a control Point.

Control Point Clerk's Menu

Process a Request Menu ...

Display Control Point Activity Menu ...

Funds Control Menu ...

Status of Requests Reports Menu ...

Record Date Received by Service Menu ...

Record Receipt of Multiple Delivery Schedule Items

Multiple Delivery Schedule List

Select Control Point Clerk's Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Change Existing Transaction Number

Select CONTROL POINT: 101 LAB TESTING 101

### Enter Temporary Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the temporary transaction number that the requestor assigned to the request at the Select Control Point Activity Transaction Number: prompt. If you decide to review the request, IFCAP will display the request and allow you to edit the Fiscal Year, Fiscal Quarter, and Control Point.

<span id="PRC_158_A" class="anchor"></span>Select the existing transaction number to be replaced

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: WER513 WER513 OBL

Would you like to review this request? NO// Y (YES)

DEVICE: HOME// LAT RIGHT MARGIN: 80//

MCG0727 JUL 27, 2011@12:31:09 PAGE 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Originator of Request: PRCUSER,NINE

Requestor: \|Date Requested: \|Obligation No.:

MCGAUGH, MAVIS \|JUL 27, 2011 \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Vendor: \|Contract Number:

\|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Name and Title Approving Off.: \|Signature: \|Date Signed:

\| \|

\| \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FUND CERTIFICATION: The supplies and services listed on this request are

properly chargeable to the following allotments, the available balances of

which are sufficient to cover the cost thereof, and funds have been obligated.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press return to continue, "^" to exit:

MCG0727 PAGE 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Appropriation & Acct. Symbols: \|Obligated By: \|Date Obligated:

999-3610160-081-828100-2580 010028100 \| \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORITY:

SERVICE START DATE: SERVICE END DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Purpose:

MONTHLY COSTS

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press return to continue, "^" to exit

MCG0727 PAGE 3

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Daily Record entries have not yet been entered for this request.

The total committed cost of this request is \$1000.00

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

VA FORM 4-1358a-ADP (NOV 1987)

Enter the information for the new transaction number

Select FISCAL YEAR: 94//

Select QUARTER: 3//

Select CONTROL POINT: 101 LAB TESTING 101//

### Conversion to Permanent Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will assign a transaction number to the request, making the request a transaction. IFCAP will ask you if you want to edit the transaction. IFCAP will ask you for a cost center, a budget object code (BOC), and a sub-control point. Budget object codes are in the left column of MP-4 Part V, Appendix B-1. At the Select Sub-Control Point: prompt, you can associate this purchase with a category of purchases that you can define. This allows you to group similar purchases together. IFCAP will ask you if you want to assign a vendor to the transaction.

> **NOTE:** Sometimes, you will want to leave the vendor field blank on a 1358 in case you want to change vendors or use multiple vendors.

<span id="PRC_158_B" class="anchor"></span>If you assign a vendor, IFCAP will ask you for a contract number. Explain the purpose of the 1358. Add comments if you like. If you make a mistake, answer Y at the Would you like to review this request?: prompt. If the 1358 is ready for approval, answer Y at the Is this request ready for approval?: prompt. The 1358 is now ready for approval by the Control Point Official. Press the Enter key at the Would you like to replace another transaction number? prompt to return to the Process a Request Menu.

Would you like to review this request? No// Y (Yes)

DEVICE: HOME// 0;80;9999 TELNET

MCG0727 JUL 27, 2011@12:34:40 PAGE 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Originator of Request: PRCUSER,NINE

Requestor: \|Date Requested: \|Obligation No.:

MCGAUGH,MAVIS \|JUL 27, 2011 \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Vendor: \|Contract Number:

\|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Name and Title Approving Off.: \|Signature: \|Date Signed:

\| \|

\| \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FUND CERTIFICATION: The supplies and services listed on this request are

properly chargeable to the following allotments, the available balances of

which are sufficient to cover the cost thereof, and funds have been obligated.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press return to continue, "^" to exit:

MCG0727 PAGE 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Appropriation & Acct. Symbols: \|Obligated By: \|Date Obligated:

999-3610160-081-828100-2580 010028100 \| \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORITY:

SERVICE START DATE: SERVICE END DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Purpose:

MONTHLY COSTS

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Daily Record entries have not yet been entered for this request.

The total committed cost of this request is \$1000.00

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

VA FORM 4-1358a-ADP (NOV 1987)

Enter the information for the new transaction number

Select STATION NUMBER: 999//

Select FISCAL YEAR: 11//

Select QUARTER: 4//

Select CONTROL POINT: 081 SPD SEEMA 0160A1 10 0100 010028100

0160A1 10 0100 010028100

Transaction 'MCG0727' has been replaced by 999-11-4-081-0006

Use the 1358 edit option if you wish to edit this request

Would you like to replace another transaction number? NO// (NO)

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

Select Process a Request Menu Option:

# Monitoring Request Status 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a Control Point Clerk, employees who request goods and services from your control point often need to know the status of their request. This chapter explains how to determine the status of a request, and what stage of accounting or procurement it has reached.

## Monitoring Request Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When You Know the Purchase Order Number?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Control Point Clerk’s Menu, select Display Control Point Activity Menu. From the Display Control Point Activity Menu, select Purchase Order Status. Enter the station number and the Control Point. Enter the purchase order number at the Select Purchase Order Number: prompt. You can type three question marks (???) to list all the purchase orders for the control point.

Select IFCAP MENU Option: Control Point Clerk’s Menu

Process a Request Menu ...

Display Control Point Activity Menu ...

Funds Control Menu ...

Status of Requests Reports Menu ...

Record Date Received by Service Menu

Record Receipt of Multiple Delivery Schedule Items

Multiple Delivery Schedule List

Select Control Point Clerk's Menu Option: Display Control Point Activity Menu

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

CP Entered, Not Approved Requests

Select Display Control Point Activity Menu Option: Purchase Order Status

Select STATION NUMBER: 999// ANYCITY,DC

Select CONTROL POINT: 101 TESTING 101

Select PURCHASE ORDER NUMBER: ???

CHOOSE FROM:

999-A40016 12-02-93 ST Pending Fiscal Action

FCP: 101 \$ 78.12

999-A40017 12-02-93 ST Pending Fiscal Action

FCP: 101 \$ 90

999-A40018 12-02-93 ST Complete Order Received (Amended)

FCP: 101 \$ 30

999-A40019 12-02-93 ST Complete Order Received

FCP: 101 \$ 30

999-A40020 12-02-93 ST Partial Order Received

FCP: 101 \$ 15

999-A40021 12-02-93 ST Pending Fiscal Action

FCP: 101 \$ 44.56

Select PURCHASE ORDER NUMBER: A40017 999-A40017 12-02-93 ST Pending Fiscal Action

FCP: 101 \$ 90

### When You Don’t Know the Purchase Order Number, but know the Vendor?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Control Point Clerk’s menu, select Display Control Point Activity Menu. Transaction Status Report. Enter the vendor name at the Select Control Point Activity Transaction Number: prompt. This report will list the vendor, the transaction number (station-fy-qtr-cp-transaction number), and the purchase order number. Choose a transaction number from the list of transactions for the vendor. Read the A&MM Status on the Obligation Transaction Status Display.

Select Control Point Clerk's Menu Option: Display Control Point Activity Menu

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

CP Entered, Not Approved Requests

Select Display Control Point Activity Menu Option: Transaction Status Report

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: 999-12-3-333

1 999-12-3-333-0015 CEIL FROM 12-2

2 999-12-3-333-0017 ADJ QTRADJ

3 999-12-3-333-0018 OBL IFVENDOR TWO C21255

REPAIR WATER HEATER in BLD 3

4 999-12-3-333-0019 OBL IFVENDOR THREE

CARTRIDGE,BLACK, A-2270DW PRINTER

Sent to eCMS

5 999-12-3-333-0020 OBL IFVENDOR ONE A23156

BATTERY,ALK,AAA, 1.5V, HEAVY DUTY

CHOOSE 1-5: 5 999-12-3-333-0020

DEVICE: HOME// LAT RIGHT MARGIN: 80//

OBLIGATION TRANSACTION STATUS DISPLAY JUN 7,2012@13:13:11

Transaction Number: 999-12-3-333-0020 Transaction Type: OBLIGATION

A&MM Status: Pending Accountable Officer Sig.

Temporary Trans. Number:

Form Type: REPETITIVE AND NON-REP ORDER

Date of Request: JUN 14,2012 Date Required: JUN 24,2012

Est. Delivery Date: Date Received:

Vendor: IFVENDOR ONE P.O. Vendor:

Committed (Estimated) Cost: \$7.00 Date Committed: JUN 14,2012

Obligated (Actual) Cost: \$0.00 Date Obligated:

Purchase Order/Obligation No.: Accounting Data: 3620160

FMS \$ Amount: \$0.00 FMS Date:

FMS Transaction Code:

Return to Service Comments:

2237 Returned by eCMS Line \#3 needs to be edited as the unit of …

Comments: Item has incorrect unit of measure.

Would you like to review the item information for this request? No// y (Yes)

OBLIGATION TRANSACTION STATUS DISPLAY - ITEM INFORMATION

Transaction Number: 999-12-3-333-0020 Transaction Type: OBLIGATION

-------------------------------------------------------------------------------

STOCK NUMBER ITEM DESCRIPTION QUANTITY U/I UNIT COST

------------------------------------------------------------------------------

ST00Q98 \|1 ITEM ID NO. 14 BATTERY, ALKALINE, \| \| \|

\|AAA SIZE, 1.5 VOLTS \| 2\| PG\| 3.50

Enter information for another report or an up-arrow to return to the menu.

Select STATION NUMBER: 999//

### When You Don’t Know the Purchase Order Number or Vendor, But Have the First Line Item?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go back to the Control Point Clerk’s Menu. Select Status of Requests Reports Menu from the Control Point Clerk’s Menu. Select Status of all Obligation Transactions. This will show you the vendor and the status of all obligation numbers. It’ll also list the date required and the estimated delivery date. Record the Purchase Order number from this report. Enter a caret (^) at the Select Fiscal Year: prompt to return to the Status of Requests Reports Menu.

Select Status of Requests Reports Menu Option: status of All Obligation Transactions

Select STATION NUMBER: 999//

Select FISCAL YEAR: 12//

Select QUARTER: 4// 3

Select CONTROL POINT: 333

Select CONTROL POINT: 333 TEST CNTRL POINT 0160A1 10 11 010024200

DEVICE: 0;80;9999 DECWINDOWS

STATUS OF OBLIGATION TRANSACTIONS CP: 333 TEST CNTRL POINT FY: 12

JUN 7,2012 13:30 PAGE 1

PRIORITY DATE

OF DATE RECEIVED

TRANS \# REQUEST SIGNED REQUIRED DELIVERED BY SVC

VENDOR STATUS

OBLIGATION# SORT GROUP

FIRST LINE ITEM DESCRIPTION

COMMENTS

------------------------------------------------------------------------------

12-3-0019 STANDARD 06/14/12

IFVENDOR THIRTEEN Returned to Service by eCMS(P&C)

CARTRIDGE,BLACK, AT-2270DW

Please expedite

12-3-0020 STANDARD 06/14/12 06/24/12

IFVENDOR FIVE Pending Accountable Officer Sig.

BATTERY,ALK,AAA,1.5V, HEAVY DUTY

Needed immediately if not sooner.

12-3-0021 STANDARD 06/24/12

IFVENDOR NINE Returned to Service by P&C

BATTERY,ALK,AAA,1.9V, HEAVY DUTY

Needed for emergency flashlights.

12-3-0023 STANDARD 06/15/12 06/30/12

IFVENDOR FOUR Pending Accountable Officer Sig.

BATTERY,ALK,AAA,1.12V, HEAVY DUTY

Need for emergency kits.

12-3-0024 STANDARD 06/29/12

IFVENDOR THREE Returned to Service by eCMS (P&C)

PAPER,8-1/2X11 INCH,WHITE,PHOTOCO

For copier in Director’s Office.

12-3-0031 STANDARD 06/28/12 07/01/12

IFVENDOR THREE To IFCAP Ordering Official

CABLE,NETWORK,25 FT,CAT6

We really need this for a meeting on July 1st.

## Monitoring the Status of 1358’s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the 1358 Request Menu, select the Print 1358 option

.

Select Control Point Clerk's Menu Option: Process a Request Menu

Select Process a Request Menu Option: 1358 Request Menu

Select 1358 Request Menu Option: Print 1358

### Entering Obligation Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Control Point. Enter the obligation number of the 1358. If you do not know the obligation number, enter three question marks and IFCAP will list the available 1358s.

Select 1358 Request Menu Option: PRINt 1358

Select STATION NUMBER: 999

Select CONTROL POINT: 110 NAME .01 0160A1 10 0100 010042116

Select OBLIGATION NUMBER: C85026 999-98-2-110-0110 OBL IFVENDOR2,THREE C85026

Would you like to print the Description field for each 1358 Daily Record entry? No// Y(Yes)

Would you like to print the daily records for each authorization? NO// YES

Would you like to print descriptions for each detailed daily record? NO// YES

DEVICE: HOME// UCX/TELNET Right Margin: 80//

### Reviewing the 1358

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Print 1358 you may display the 1358 and review the Authorization and Order Record. It will list all the entries and their cost for the quarter.

Select 1358 Request Menu Option: Print 1358

Select STATION NUMBER: 999//

Select CONTROL POINT: 045 FISCAL// 110 NAME .01 0160A1 10 0100 010042116

Select OBLIGATION NUMBER: C05026 999-10-4-110-0051 OBL C05026

Would you like to print the Description field for each 1358 Daily Record entry?

No// Y (Yes)

Would you like to print the daily records for each authorization? NO// YES

Would you like to print descriptions for each detailed daily record? NO// YES

DEVICE: HOME// 0;80;9999 TELNET

999-11-4-081-0003 JUL 27, 2011@12:42:05 PAGE 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:FEE BASIS

FEE MEDICAL/DENTAL (NOT PRE-AUTHORIZED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Originator of Request:

Requestor: \|Date Requested: \|Obligation No.:

CP CLERK, ONE \|JUL 07, 2011 \| 999-C15096

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Vendor: \|Contract Number:

\|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Name and Title Approving Off.: \|Signature: \|Date Signed:

OFFICIAL CP \|/ES/OFFICIAL CP \|JUL 07, 2011@15:3

2:39

FCP OFFICIAL \| \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FUND CERTIFICATION: The supplies and services listed on this request are

properly chargeable to the following allotments, the available balances of

which are sufficient to cover the cost thereof, and funds have been obligated.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press return to continue, "^" to exit:

999-11-4-081-0003 999-C15096 PAGE 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:FEE BASIS

FEE MEDICAL/DENTAL (NOT PRE-AUTHORIZED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Appropriation & Acct. Symbols: \|Obligated By: \|Date Obligated:

999-3610160-081-828100-2580 010028100 \|/ES/TECH ACCT \|JUL 19, 2011

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORITY: 2 SUB: B

SERVICE START DATE: 07/01/11 SERVICE END DATE: 07/31/11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Purpose:

MONTHLY COSTS

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press return to continue, "^" to exit:

999-11-4-081-0003 999-C15096 PAGE 3

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:FEE BASIS

FEE MEDICAL/DENTAL (NOT PRE-AUTHORIZED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ESTIMATED OBLIGATION RECAP

DATE REF# CPA#AMOUNT BALANCE

07/19 0001 999-11-4-081-0003 \$ 10000.00\$ 10000.00

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORIZATION & ORDER RECORD LIQUIDATION RECORD

AUTH. AUTH. CUMULATIVE UNLIQ

DATE SEQ# REFERENCE AMOUNT BALANCE AUTH. AMT. LIQUID BAL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TOTALS \$ 0.00 \$ 0.00 \$ 0.00 \$ 10000.00

VA FORM 4-1358a-ADP (NOV 1987)

## # Adjusting Control Point Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP V. 5.1 automates most of the reconciling that Control Point Clerks have had to perform manually. You will still have to adjust 1358 expenses and adjust your supply Fund Control Point balances at the end of the fiscal year.5.2 Adjusting 1358 Expenses

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Process a Request Menu ...

Display Control Point Activity Menu ...

Funds Control Menu ...

Status of Requests Reports Menu ...

Record Date Received by Service Menu ...

Select Control Point Clerk's Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List Open 1358s

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: Increase/Decrease Adjustment

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a fiscal year, fiscal quarter and a control point. Enter the number of the obligation you want to adjust at the Select Obligation Number: prompt. If you do not know the number, enter as many of the first characters that you remember or enter three question marks, and IFCAP will list the available obligations. IFCAP will display the amount of the obligation you selected and assign a transaction number to the adjustment you are creating. At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Enter your name at the Requestor: prompt. Enter today's date at the Date of Request: prompt. Enter the cost center at the Cost Center: prompt . Cost centers allow Fiscal staff to create total expense records for a section or service.

Select FISCAL YEAR: 95//

Select QUARTER: 2//

Select CONTROL POINT: 101 LAB

Select OBLIGATION NUMBER: ???

CHOOSE FROM:

Choose from:

B45003 999-11-1-110-0007 OBL AMSCO1 INTERNATIONAL B45003

C05003 999-10-4-110-0039 OBL RACHEL C05003

C05004 999-10-4-110-0043 OBL RACHEL C05004

C05005 999-10-4-110-0044 OBL RACHEL C05005

C05026 999-10-4-110-0051 OBL C05026

C15002 999-11-1-110-0013 OBL RACHEL C15002

C15003 999-11-1-110-0009 OBL C15003

C95118 999-09-4-110-0026 OBL C95118

C95119 999-09-4-110-0028 OBL C95119

C05026 999-10-4-110-0051 OBL C05026

Select OBLIGATION NUMBER: c05026 999-10-4-110-0051 OBL C05026

Note that one of the previous documents has not been processed in FMS. The adjustment to this 1358 cannot be obligated until the previous document has been processed in FMS.

FMS Document: SO-999C05026 -999065

Status: TRANSMITTED

Do you wish to create the adjustment to this 1358? YES//

Original Obligation Amount: \$ 1,284.00 Service Balance: \$ 448.50

Fiscal's 1358 Balance: \$ 1,284.00

This transaction is assigned transaction number: 999-11-1-110-0026

CLASSIFICATION OF REQUEST:

SORT GROUP:

DATE OF REQUEST: 101510// (OCT 15, 2010)

COST CENTER: 842100//

### Adjustment Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="PRC_184_A" class="anchor"></span>Enter today’s date at the Date Obligated Adjusted: prompt. Enter the amount that you want to adjust the obligation at the Adjustment \$Amount prompt. Type the number without any symbols to add money to the obligation. Type a minus symbol in front of the amount to subtract money from the obligation. At the BOC1: prompt, enter the budget object code classification for this item. Budget object codes are defined in VHA Handbook 4671.2. If you do not know the BOC for this item, enter three question marks and IFCAP will list the available budget object codes. At the BOC1 Amount: prompt. Hit the Enter key.

Enter a Sub-Control Point if you want to assign this receipt to a defined subcategory of the Control Point. The Purpose: prompt, is now a required field. Enter the purpose of the 1358 adjustment. Add comments if you like. You may review the request to make sure that the information on the request is correct. Confirm that the adjustment is ready for approval. You may enter another adjustment or return to the 1358 Request Menu.

DATE OBL ADJUSTED: T (OCT 15, 2010)

ADJUSTMENT \$ AMOUNT: 475 \$ 475.00

BOC1: 2580 Miscellaneous Contractual Replace

BOC1 \$ AMOUNT: 475// \$ 475.00

TRANSACTION BEG BAL: 410.00

Select SUB-CONTROL POINT:

PURPOSE:

1\>Additonal Monthly Costs for October 2010

2\>

EDIT Option:

COMMENTS:

1\>

2\>

EDIT Option:

Would you like to review this request? NO//

Is this request ready for approval? YES// (YES)

Enter another increase/decrease adjustment? NO//

# Handling System Down or Life-Threatening Emergencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In some facilities, Purchasing Agents prepare for system crashes by creating a set of purchase order numbers to use when the system crashes. Ask your Purchasing Agent if he or she does this. If so, call him or her when the system crashes and ask for one of the “emergency” purchase order numbers. When the system is functioning, create your requests in IFCAP using this purchase order number and enter in the Comments: field of the request that this order was requested during a system failure and that the order has already been ordered and obligated using the emergency purchase order number.

Comments: // System Failure reconciliation -- DO NOT ORDER -- DO NOT OBLIGATE

If you do not clearly explain that this order has already been filled, the Purchasing Agent will order it again and your control point will be charged for the purchase.

# Other IFCAP Functions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Supplementary Options in the Process a Request Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the options available to you in IFCAP that were not mentioned in the previous chapters. Each section of this chapter defines the purpose of the option, the menu path to reach the option in the menus, what information to enter at the prompts, and how to interpret the output that the option creates.

## Editing a 2237 (Service)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select Edit a 2237 (Service) from the Process a Request Menu.

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number. Enter a Control Point. If you do not know the Control Point, enter two question marks at the Select Control Point: prompt and IFCAP will list the available Control Points. If the Control Point is attached to more than one Inventory Point, enter the Inventory Point at the prompt or simply hit \<enter\> and no Inventory Point will be attached to the order.

Select STATION NUMBER: 999ANYCITY,DC

Select CONTROL POINT: 101 ??

Select CONTROL POINT: ??

CHOOSE FROM:

22 022 MISC OFFICE SUPPLIES

40 040 BUILDING MANAGEMENT

73 073 ENGINEERING

112 112 SURGICAL SERVICE

114 114 RADIOLOGY SERVICE

121 121 LAB TESTING 121

333 333 TEST CONTRL POINT

Select CONTROL POINT: 333 TEST CONTRL POINT

### Entering Transaction Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a transaction number. If you do not know the transaction number, enter three question marks at the Select Control Point Activity Transaction Number: prompt and IFCAP will list the available transactions. You can also enter the vendor name, or as much of the beginning of the transaction number as you can remember. For example, if you enter 999-95-4, IFCAP will list all the transactions for Control Point 999 for fiscal year 1995 and fiscal quarter 4. Reducing the search in one of these ways will greatly reduce your search time.

Attempting lookup in transaction file.

Attempting lookup using 333 TEST CNTRL POINT

1 333 TEST CNTRL POINT 999-12-3-333-0075 OBL IFVENDOR TWO

BATTERY,ALK,AAA,1.5V, HEAVY DUTY

Sent to eCMS

2 333 TEST CNTRL POINT 999-12-4-333-0074 OBL IFVENDOR FOUR

GAUZE PETRO 1X36IN WHT

To IFCAP Ordering Official

3 333 TEST CNTRL POINT 999-12-4-333-0073 OBL IFVENDOR NINE

FLOOR FINISH

### Form Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will show the default form type and list the prompts required to create that form type. Read the sections of this guide on creating these form types for descriptions of the prompts.

### Control Point Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list the current Control Point balance, the estimated cost (incorporating the change to the balance that you just made), and the total uncommitted balance from current and prior quarters for that Control Point. IFCAP will allow you to forward the request to the Control Point Official. Enter N at the Would You Like To Edit Another Request?: prompt to return to the Process a Request Menu.

Current Control Point balance: \$0.00

Estimated cost of this request: \$44.00

Total uncommitted balance from current and prior quarters: \$4734.20

Sure you want to approve this request? NO// Y (YES)

Would you like to edit another request? YES// n (NO)

Select Process a Request Menu Option:

## Printing and Displaying Request Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to print or display a request.

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu. Select Print/Display Request Form from the Process a Request Menu. Enter the transaction number of the request at the Select Transaction: prompt .or enter the Obligation Number.

Select Process a Request Menu Option: print/Display Request Form

Select STATION NUMBER: 999//

Select CONTROL POINT: 110 NAME .01// 0160A1 10 0100 010042116

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: A00011

Searching for a Sort Group, (pointed-to by SORT GROUP)

Searching for a Work Order, (pointed-to by SORT GROUP)

999-00-1-110-0015 OBL IFVENDOR2,THREE A00011 999-00-1-110-0014

DOLLS

### Last Page Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter Yes at the Print Last Page of 2237?: prompt if you want to see who has approved the request for purchase (the “Administrative Action” column) or who has certified receipt of the purchase (the “Receipt Action” column). Otherwise, enter No at this prompt.

Print last page of 2237? YES//

DEVICE: HOME// LAT RIGHT MARGIN: 80//

### Interpreting the Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The request form lists the information you provided in the Enter/Edit a Request options in a style that represents a manual VA 2237 form. The form lists each item with description and unit cost, and a total cost for the request. It also lists where the item(s) should be delivered. If you printed the last page of the 2237, the form will list signature and date columns for officers and clerks to sign at various stages of approval and receipt. Enter another transaction at the Select Transaction: number or press the Enter key to return to the Requestor’s Menu.

> **NOTE:** If the 2237 has been sent to and accepted by eCMS for processing, there will be Identifiers that will indicate that this occurred. The text “Accepted by eCMS” will appear to the right of the Priority in the Header on Page 1. The eCMS Line Item ID will appear beneath the Item description.

PRIORITY: STANDARD Accepted by eCMS

JUL 10, 2000@10:57:49 999-00-1-110-0015

--------------------------------------------------------------------------------

REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES

--------------------------------------------------------------------------------

TO: A&MM Officer Requesting Office

FISCAL (04)

----------------------- --------------------------------------------------------

Action Requested Date Prepared Date Required

Delivery OCT 25, 1999 OCT 25, 1999

----------------------- --------------------- ----------------------------------

ITEM NO. DESCRIPTION QUANTITY UNIT ESTIMATED

OR STOCK NO.

ST

--------------------------------------------------------------------------------

Put item info below in here

TN-420 1 CARTRIDGE,PRINTER AT-2270DW

PRINTER PART# TN-420

eCMS Item Line ID 12365 2 EA 44.9500

TOTAL COST: \$89.90

--------------------------------------------------------------------------------

VENDOR INFORMATION: NO: 12345 FAX: 555-555-5555/DEF

VENDOR: IFVENDOR,FOUR CONTACT: IFUSER,ONE

8 SAMPLE ST : 111-555-5555

ANYTOWN,MA 00001

--------------------------------------------------------------------------------

Ref. Voucher Number:

Press return to continue, up-arrow (^) to exit:

999-00-1-110-0015

--------------------------------------------------------------------------------

REQUEST, TURN-IN, AND RECEIPT FOR PROPERTY OR SERVICES

--------------------------------------------------------------------------------

DELIVER TO: BD3

--------------------------------------------------------------------------------

JUSTIFICATION OF NEED OR TURN-IN

TEST

--------------------------------------------------------------------------------

Originator of Request:

Signature of Initiator Signature of Approving Official Date

/ES/IFUSER,TEN

IFUSER,TEN IFUSER, TEN

IFVENDOR,FOUR IFVENDOR, FOUR OCT 25, 2011

------------------------------------ -------------------------------------------

Appropriation and Accounting Symbols

999-3600160-333-842100-2660-010042116

--------------------------------------------------------------------------------

Press return to continue:

## Change Existing Transaction Number (of a 2237)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to change the transaction number of an existing 2237 transaction.

> **NOTE:** If the 2237 you are changing has eCMS Identifiers -- immediately upon completing the process, you must manually notify the eCMS Contracting Officer of the changed 2237 number. Advise the Contracting Officer of the cancelled original 2237# and the new 2237#. This will ensure that the Contracting Officer cancels the old 2237 in the eCMS system and will enable the Contracting Officer to link the new 2237 to the existing Award plan documents when it is Approved and sent forward to eCMS.

Select Process a Request Menu from the Control Point Clerk’s Menu. Select Change Existing Transaction from the Process a Request Menu. Enter a Station number and a Control Point number. Enter the transaction you want to change at the Select Transaction Number: prompt, or enter three question marks and IFCAP will display the available transactions.

At the Select CONTROL POINT ACTIVITY TRANSACTION NUMBER prompt enter 2237 number you wish to change. You will be given an opportunity to review the 2237 If you enter Yes at that prompt.

Select STATION NUMBER: 999//

Select CONTROL POINT: 110 SUPPLIES .01// 0160A1 10 0100 010042116

Select the existing transaction number to be replaced

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: 0076 999-13-4-110-0076 OBL

STAPLES, INC.

Would you like to review this request? No// (No)

Enter the information for the new transaction number

Select STATION NUMBER: 999//

Select FISCAL YEAR: 13// 14

Select QUARTER: 4// 1

Select CONTROL POINT: 110 SUPPLIES .01// 0160A1 10 0100 010042116

0160A1 10 0100 010042116

Old transaction 999-13-4-110-0076 is now cancelled.

> **NOTE:** the original transaction is cancelled and the new transaction is checked to ensure that all Required fields are populated

Transaction '999-13-4-110-0076' has been replaced by 999-14-1-110-0001

WARNING - Transaction 999-14-1-110-0001 is missing required data!

\>\>\> Line Item \#1 Description is missing.

The request needs to be edited prior to approval.

The form type for this transaction is REPETITIVE AND NON-REP ORDER

CLASSIFICATION OF REQUEST:

SORT GROUP:

You will be permitted to change the Date of Request, Requesting Service, Date Required, Priority of Request as appropriate.

DATE OF REQUEST: JUN 3,2013// T AUG 5,2013

REQUESTING SERVICE: DENTAL//

DATE REQUIRED: JUL 1,2013// 100313 OCT 3,2013

PRIORITY OF REQUEST: STANDARD//

SPECIAL REMARKS:

1\>

COST CENTER: 842100 Fiscal

VENDOR: VENDORONE, INC.//

Select LINE ITEM NUMBER: 2//

LINE ITEM NUMBER: 2//

ITEM MASTER FILE NO.: 22//

BOC: 2631 Drugs, Medicines and Chem Replace

QUANTITY: 3//

QTY BEG BAL: 3

Select DELIVERY SCHEDULE:

> **NOTE:** Item Description is a REQUIRED field. You will have to enter text for that item.

Select LINE ITEM NUMBER: 1

LINE ITEM NUMBER: 1//

ITEM MASTER FILE NO.:

DESCRIPTION:

1\>

Item DESCRIPTION is required!

DESCRIPTION:

1\>DRAPES,LINEN 80 X 102 - 4 PANELS

2\>

EDIT Option:

BOC: 2660 Operating Supplies and Ma Replace

QUANTITY: 3//

UNIT OF PURCHASE: PR// SETS??

Select the appropriate unit of purchase for this item

UNIT OF PURCHASE: PR// SET SE SET

STOCK NUMBER:

EST. ITEM (UNIT) COST: 45.55//

QTY BEG BAL: 3

Select DELIVERY SCHEDULE:

Select LINE ITEM NUMBER:

COMMITTED (ESTIMATED) COST: 166.5//

TRANSACTION BEG BAL: 166.50

Select SUB-CONTROL POINT:

DELIVER TO/LOCATION: BLDG33,RM12//

JUSTIFICATION:

1\>Needed for training sessions with nursing students.

EDIT Option:

REQUESTOR: GREENE,LYFORD K//

ORIGINATOR OF REQUEST:

COMMENTS:

1\>

Would you like to review this request? No// (No)

Current Control Point balance: \$20606769.49

Estimated cost of this request: \$166.50

> **NOTE:** You will not be prompted to set this request to YES if there is a Required field that is not populated.

Is this request ready for approval? Yes//

Would you like to replace another transaction number? No// (No)

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

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select Process a Request Menu \<TEST ACCOUNT\> Option:

## Canceling Transactions with Permanent Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu. Select Cancel Transaction with Permanent Number from the Process a Request Menu. Enter a Station number and a Control Point number. Enter the transaction you want to delete at the Select Transaction Number: prompt, or enter three question marks and IFCAP will display the available transactions.

> **NOTE:** When you cancel a transaction that began as a temporary request, print and mail a copy of the request to the requestor, since canceling the request removes it from the system. This will save time for the requestor.

Select Process a Request Menu Option: Cancel Transaction with Permanent Number

Select Process a Request Menu Option: Cancel Transaction with Permanent Number

Select STATION NUMBER: 999

Select CONTROL POINT: 333 LYFE'S TEST CNTRL POINT 0160X1 10 11 815

Select TRANSACTION: ??

Attempting lookup in transaction file.

Attempting lookup using 333 (CONTROL POINT)

1 333 TEST CNTRL POINT 999-12-4-333-0092 OBL BEST BUY INC.

DRIVE,FLASH,16 Gb

Accepted by eCMS

2 333 TEST CNTRL POINT 999-12-4-333-0089 OBL STAPLES, INC.

BATTERY,ALK,AAA,1.5V, HEAVY DUTY

3 333 TEST CNTRL POINT 999-12-4-333-0083 OBL OFFICE DEPOT

NOTES,3X3 INCH,POST-IT,ASSORTED COLORS

Accepted by eCMS

4 333 TEST CNTRL POINT 999-12-4-333-0082 OBL STAPLES, INC.

CHALK,BOARD,ASSORTED COLORS,6/PKG

5 333 TEST CNTRL POINT 999-12-4-333-0078 OBL STAPLES, INC.

### Canceling Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** When doing a ?? lookup of 2237 transactions, some of the 2237s may show the text “Accepted by eCMS.” DO NOTcancel any transaction showing that text from within IFCAP. Now that an interface exists between IFCAP and the electronic Contract Management System, the cancellation of a 2237 that has been “Accepted by eCMS” *must be initiated by a User from within the electronic Contract Management System*.

> **NOTE:** When an IFCAP User cancels a 2237, the Name of the User and the Date/Time of the cancellation are now stored in the 2237 record in the Control Point Activity file (#410).

IFCAP will ask you to confirm that you want to cancel the transaction, and ask you to enter comments that explain why you have cancelled the transaction. At the Would you like to cancel another transaction?: prompt, answer Y to cancel another transaction or press the Enter key to return to the Process a Request Menu.

Are you sure you want to cancel this transaction? NO// Y (YES)

Please enter comments describing the reason this transaction was cancelled

COMMENTS:

2\>Item no longer needed.

3\>

EDIT Option:

Would you like to cancel another transaction? NO// (NO)

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

Select Process a Request Menu Option:

## Supplementary Options in the Requestor's Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Requestor’s Menu options are described in the IFCAP Requestor User’s Guide.7.6 Supplementary Options in the Repetitive Item List Menu.

## Supplementary Options in the Repetitive Item List Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Repetitive Item List (Enter)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Control Point Clerk's Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Repetitive Item List Menu

New Repetitive Item List (Enter)

Edit Repetitive Item List Entry

Delete Repetitive Item List Entry

Print/Display Repetitive Item List Entry

Generate Requests From Repetitive Item List Entry

Select Repetitive Item List Menu Option: New Repetitive Item List (Enter

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, a fiscal year and a fiscal quarter. Enter a Control Point. If you do not know the name of the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points. Enter a cost center. Cost centers allow Fiscal staff to create total expense records for a section or service.

Select STATION NUMBER: 999 ANYCITY,DC

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 022 IFVENDOR2,FOUR

Select COST CENTER: 804909 ??

Select COST CENTER: ??

844100 844100 Supply

Select COST CENTER: 844100 Supply

### Item Selection 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter an item number or name at the Select Item: prompt. If you do not know the name or the number of the item, enter three question marks at the prompt and IFCAP will list the available items.

Select ITEM: ????

This is a pointer to an item in the Item file, \#441. This file is

composed of items specified by Supply Service as being purchased

repetitively. This file maintains a full description of the item,

related stock numbers, vendors, contract numbers, and a procurement

history.

CHOOSE FROM:

1 BANDAGE-CAST-6INX5YD

2 CAP-SAFETY-BOTTLE-50S

3 PLASMA-USP 5%

4 TOMATOES CANNED

5 SUGAR

6 CEREAL-SHREDDED-WHEAT-BISQUIT

7 DIETARY SUPPLEMENT

8 PROMETHAZINE INJ 25MG 1ML

9 BATTERY-RECHARGEABLE-9 VOLT

10 PHENYTON SODIUM CAPS 100MG

11 TUBE,TRACH,STERILE,9MM ID

12 SUGAR-REFINED

13 THEOPHYLLINE-TABS-200MG

14 CEREAL-WHEAT

15 LITHIUM-CAP-300MG-100S-UD

16 ENEMA-ADMINISTRATION-SET-DISP

17 NEOSTIGMINE-METHYSULFATE-INJECTION.

18 BEANS, PINTO, CANNED, \#10

19 EGGNOG

20 CORN-CANNED-#10

21 TOWEL-PAPER-140SQIN

Select ITEM: 20 CORN-CANNED-#10

### Item Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you select an item, IFCAP will display what unit of sale the vendor uses to sell the item and if you have to buy the item by a specific multiple. In the example below, the unit is per can, but the item must be ordered in multiples of six, so the user would enter a multiple of six at the Quantity: prompt. Many repetitive items will have a mandatory source of the warehouse, meaning that the warehouse supplies this item. If the item you want is not a warehouse item, you must enter the vendor name after you enter the item number. If you do not know who the vendor should be for that item, press the Enter key at the vendor prompt and IFCAP will list the available vendors for the item. You can add another repetitive item at the Select Item: prompt or press the Enter key to stop adding items. IFCAP will determine the cost of the items. At the Would You Like To Create Another Repetitive Item List Entry?: prompt, answer Y to add another item or N to return to the Repetitive Item List Menu.

This item has a mandatory source (vendor) of WAREHOUSE

> **NOTE:** This item must be ordered in multiples of 6

> **NOTE:** This item has a packaging multiple/unit of purchase of 1/CAN

QUANTITY: 12

Select ITEM:

Let me total the cost for this Repetitive Item List entry (#999-94-4-022-844100-

0001\)

Total number of items: 1 Total cost (all items): \$30.00

Would you like to create another repetitive item list entry? NO// (NO)

## Editing the Repetitive Item List Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select Repetitive Item List Menu from the Process a Request Menu.

Select Edit Repetitive Item List Entry from the Repetitive Item List Menu.

Select Control Point Clerk's Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Repetitive Item List Menu

New Repetitive Item List (Enter)

Edit Repetitive Item List Entry

Delete Repetitive Item List Entry

Print/Display Repetitive Item List Entry

Generate Requests From Repetitive Item List Entry

Select Repetitive Item List Menu Option: Edit Repetitive Item List Entry

### Select Repetitive List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a repetitive item list. If you do not know the list number, enter three question marks at the Select Repetitive Item List: prompt and IFCAP will display the available item lists.

Select REPETITIVE ITEM LIST \#: ???

CHOOSE FROM:

002-93-4-073-632500-0002 09-15-93 \# OF ITEMS: 1TOTAL COST: 48.00

002-94-1-073-632500-0001 10-20-93 \# OF ITEMS: 1TOTAL COST: 48.00

002-94-1-7001-600000-0014 12-02-93 \# OF ITEMS: 3TOTAL COST: 2053.42

002-94-1-7001-600000-0015 12-14-93 \# OF ITEMS: 5TOTAL COST: 953514.73

Select REPETITIVE ITEM LIST \#: 632500

1 632500 002-93-4-073-632500-0002 09-15-93 \# OF ITEMS: 1 TOTAL COST: 48.00

2 632500 002-94-1-073-632500-0001 10-20-93 \# OF ITEMS: 1 TOTAL COST: 48.00

CHOOSE 1-2: 1 002-93-4-073-632500-0002

Select ITEM: 5// ???

This is a pointer to an item in the Item file, \#441. This file is

composed of items specified by Supply Service as being purchased

repetitively. This file maintains a full description of the item,

related stock numbers, vendors, contract numbers, and a procurement

history.

CHOOSE FROM:

1 BANDAGE-CAST-6INX5YD

2 CAP-SAFETY-BOTTLE-50S

3 PLASMA-USP 5%

4 TOMATOES CANNED

5 LIGHT BULBS

6 CEREAL-SHREDDED-WHEAT-BISQUIT

Select ITEM: 5// 5 LIGHT BULBS

...OK? YES// (YES)

LIGHT BULBS

### Adds Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change the item again if you like. Enter a quantity. You can add another item or delete items at the Select Item: prompt, or press the Enter key if you are through adding items. IFCAP will list the cost for the items on the list. To return to the Repetitive Item List Menu, press the Enter key at the Would you like to edit another repetitive item list entry?: prompt.

ITEM: 65//

QUANTITY: 48//

Select ITEM:

Let me total the cost for this Repetitive Item List entry (#002-93-4-073-632500-

0002\)

Total number of items: 1 Total cost (all items): \$48.00

Would you like to edit another repetitive item list entry? NO// (NO)

New Repetitive Item List (Enter)

Edit Repetitive Item List Entry

Delete Repetitive Item List Entry

Print/Display Repetitive Item List Entry

Generate Requests From Repetitive Item List Entry

Select Repetitive Item List Menu Option:

## Print/Display Repetitive Item List Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select Repetitive Item List Menu from the Process a Request Menu.

Select Print/Display Repetitive Item List Entry from the Repetitive Item List Menu.

Select Control Point Clerk's Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Repetitive Item List Menu

New Repetitive Item List (Enter)

Edit Repetitive Item List Entry

Delete Repetitive Item List Entry

Print/Display Repetitive Item List Entry

Generate Requests From Repetitive Item List Entry

Select Repetitive Item List Menu Option: Print/Display Repetitive Item List Entry

### Enter Repetitive List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a repetitive item list number or name. If you do not know the number or name, enter three question marks and IFCAP will list the available repetitive items.

Select REPETITIVE ITEM LIST \#: 1 ??

Select REPETITIVE ITEM LIST \#: ??

CHOOSE FROM:

002-93-4-073-632500-0002 09-15-93 \# OF ITEMS: 1TOTAL COST: 48.00

002-94-1-073-632500-0001 10-20-93 \# OF ITEMS: 1TOTAL COST: 48.00

002-94-1-7001-600000-0014 12-02-93 \# OF ITEMS: 3TOTAL COST: 2053.42

002-94-1-7001-600000-0015 12-14-93 \# OF ITEMS: 5TOTAL COST: 953514.73

002-94-2-7001-600000-0001 03-30-94 \# OF ITEMS: 2TOTAL COST: 1621.72

999-94-4-022-844100-0001 07-08-94 \# OF ITEMS: 1TOTAL COST: 30.00

Select REPETITIVE ITEM LIST \#: 0015 ??

Select REPETITIVE ITEM LIST \#: 073 ??

Select REPETITIVE ITEM LIST \#: 632570 ??

Select REPETITIVE ITEM LIST \#: 002

1 002-93-4-073-632500-0002 09-15-93 \# OF ITEMS: 1TOTAL COST:

48.00

2 002-94-1-073-632500-0001 10-20-93 \# OF ITEMS: 1TOTAL COST:

48.00

3 002-94-1-7001-600000-0014 12-02-93 \# OF ITEMS: 3TOTAL COST:

2053.42

4 002-94-1-7001-600000-0015 12-14-93 \# OF ITEMS: 5TOTAL COST:

953514.73

5 002-94-2-7001-600000-0001 03-30-94 \# OF ITEMS: 2TOTAL COST:

1621.72

CHOOSE 1-5: 2

DEVICE: HOME// LAT RIGHT MARGIN: 80//

### Review List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list each item on the list, the quantity, the unit cost, and the Unit of Purchase (U/P), listed separately by each vendor that supplies the item. After printing or displaying the item list entry, IFCAP will return to the repetitive Item List Menu.

REPETITIVE ITEM LIST \#: 002-94-1-073-632500-0001DATE: JUL 8,1994@16:42:39 PAGE

1

ITEM NO. SHORT DESCRIPTION QUANTITY UNIT COST U/P

--------------------------------------------------------------------------------

VENDOR: WAREHOUSE

65 LIGHT BULBS 48 1.00 EA

TOTAL \# OF ITEMS: 1 TOTAL COST: 48.00

--------------------------------------------------------------------------------

TOTAL \# OF ITEMS (ALL VENDORS): 1 TOTAL COST (ALL VENDORS): 48.00

New Repetitive Item List (Enter)

Edit Repetitive Item List Entry

Delete Repetitive Item List Entry

Print/Display Repetitive Item List Entry

Generate Requests From Repetitive Item List Entry

Select Repetitive Item List Menu Option:

## Generate Requests From Repetitive Item List Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select Repetitive Item List Menu from the Process a Request Menu.

Select Generate Requests From Repetitive Item List Entry from the Repetitive Item List Menu.

Select Control Point Clerk's Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Repetitive Item List Menu

New Repetitive Item List (Enter)

Edit Repetitive Item List Entry

Delete Repetitive Item List Entry

Print/Display Repetitive Item List Entry

Generate Requests From Repetitive Item List Entry

Select Repetitive Item List Menu Option: Generate Requests From Repetitive Item List Entry

### Select List Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will warn you that this option generates requests with permanent transaction numbers from entries in the repetitive item list file. IFCAP will ask you to confirm that you want to proceed, then will ask you for the repetitive item list number. If you do not know the repetitive item list number, enter three question marks at the Select Repetitive Item List Entry Number: prompt and IFCAP will list the available item numbers.

This option generates requests with permanent transaction numbers from

entries in the repetitive item list file.

Are you sure you are ready to proceed? NO// Y (YES)

Select REPETITIVE ITEM LIST ENTRY NUMBER: ??

CHOOSE FROM:

002-93-4-073-632500-0002 09-15-93 \# OF ITEMS: 1TOTAL COST: 48.00

002-94-1-073-632500-0001 10-20-93 \# OF ITEMS: 1TOTAL COST: 48.00

002-94-1-7001-600000-0014 12-02-93 \# OF ITEMS: 3TOTAL COST: 2053.42

002-94-1-7001-600000-0015 12-14-93 \# OF ITEMS: 5TOTAL COST: 953514.73

002-94-2-7001-600000-0001 03-30-94 \# OF ITEMS: 2TOTAL COST: 1621.72

999-94-4-022-844100-0001 07-08-94 \# OF ITEMS: 1TOTAL COST: 30.00

Select REPETITIVE ITEM LIST ENTRY NUMBER: 999-94-4-022-844100-000107-0

8-94 \# OF ITEMS: 1TOTAL COST: 30.00

### Generate Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you if you want to generate requests using the current quarter or the quarter that the repetitive item list was generated. IFCAP will generate a request, display the transaction number it has assigned to the request, and list the vendor. IFCAP will ask you if you want to edit the item information for the request.

You may use either the current quarter or the repetitive item

list quarter to generate requests.

Use repetitive item list quarter? YES// (YES)

DEVICE: HOME// LAT RIGHT MARGIN: 80//

GENERATE REQUESTS FROM REPETITIVE ITEM LIST FILEDATE: JUL 8,1994@16:43

Requests Generated From Repetitive Item List Entry \# 999-94-4-022-844100-0001

--------------------------------------------------------------------------------

A request with Transaction Number 999-94-4-022-0010 has been generated.

The vendor for this request is WAREHOUSE

Now entering items for this request.

Do you wish to edit this request? NO// (NO)

### Display Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the Control Point Balance, the cost of the request it generated, and the available funds from current and prior quarters. IFCAP will allow you to transmit the request for approval. IFCAP will list the total number of the requests it generated, and the total cost for all the requests. You can reuse the list to make another request, or press the Enter key to return to the Repetitive Item List Menu.

Current Control Point balance: \$0.00

Estimated cost of this request: \$30.00

Total uncommitted balance from current and prior quarters: \$4734.20

Is this request ready for approval? NO// (NO) Finished building request.

This request contains 1 item. The total cost for this request is \$30.00

--------------------------------------------------------------------------------

Total no. of requests generated: 1 Total no. of items (all requests): 1

Total committed (estimated) cost (all requests) : \$30.00

Do you wish to re-use this list ? NO// (NO)

New Repetitive Item List (Enter)

Edit Repetitive Item List Entry

Delete Repetitive Item List Entry

Print/Display Repetitive Item List Entry

Generate Requests From Repetitive Item List Entry

Select Repetitive Item List Menu Option:

## Delete Repetitive Item List Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select Repetitive Item List Menu from the Process a Request Menu.

Select Delete Repetitive Item List Entry from the Repetitive Item List Menu.

Select Control Point Clerk's Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Repetitive Item List Menu

New Repetitive Item List (Enter)

Edit Repetitive Item List Entry

Delete Repetitive Item List Entry

Print/Display Repetitive Item List Entry

Generate Requests From Repetitive Item List Entry

Select Repetitive Item List Menu Option: Delete Repetitive Item List Entry

### Enter Repetitive List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a repetitive item list number. If you do not know the number, enter two question marks at the prompt and IFCAP will list the available item lists.

Select REPETITIVE ITEM LIST \#: ??

CHOOSE FROM:

002-93-4-073-632500-0002 09-15-93 \# OF ITEMS: 1TOTAL COST: 48.00

002-94-1-073-632500-0001 10-20-93 \# OF ITEMS: 1TOTAL COST: 48.00

002-94-1-7001-600000-0014 12-02-93 \# OF ITEMS: 3TOTAL COST: 2053.42

002-94-1-7001-600000-0015 12-14-93 \# OF ITEMS: 5TOTAL COST: 953514.73

002-94-2-7001-600000-0001 03-30-94 \# OF ITEMS: 2TOTAL COST: 1621.72

Select REPETITIVE ITEM LIST \#: 002

1 002-93-4-073-632500-0002 09-15-93 \# OF ITEMS: 1TOTAL COST: 48.00

2 002-94-1-073-632500-0001 10-20-93 \# OF ITEMS: 1TOTAL COST: 48.00

3 002-94-1-7001-600000-0014 12-02-93 \# OF ITEMS: 3TOTAL COST: 2053.42

4 002-94-1-7001-600000-0015 12-14-93 \# OF ITEMS: 5TOTAL COST: 953514.73

5 002-94-2-7001-600000-0001 03-30-94 \# OF ITEMS: 2TOTAL COST: 1621.72

CHOOSE 1-5: 5

### Delete List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you to confirm that you want to delete the item list, and ask if you want to delete another. If not, IFCAP will return to the Repetitive Item List Menu.

Are you sure you want to delete this Repetitive Item List entry? NO// y (YES)

Okay It's deleted.

Would you like to delete another Repetitive Item List entry? NO// (NO)

New Repetitive Item List (Enter)

Edit Repetitive Item List Entry

Delete Repetitive Item List Entry

Print/Display Repetitive Item List Entry

Generate Requests From Repetitive Item List Entry

Select Repetitive Item List Menu Option:

## Copy a Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select Copy a Transaction from the Process a Request Menu.

Select Control Point Clerk's Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Copy a Transaction

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number and a Control Point. Enter the transaction number. If you do not know the transaction number, enter three question marks at the prompt and IFCAP will list the available transactions.

Select STATION NUMBER: 999ANYCITY,DC

Select CONTROL POINT: 022

Select the Transaction to be copied: ??

Attempting lookup in transaction file.

Attempting lookup using 022 (CONTROL POINT)

1 022 SUPPLIES 999-13-3-022-0003 OBL VENDORONE

COTTON SHEETS

2 022 SUPPLIES 999-13-3-022-0004 OBL VENDORTHREE

GAUZE,ABSORBENT,.5IN X5YDS

Accepted by eCMS

CHOOSE 1-2:1

TYPE '^' TO STOP, OR

CHOOSE 1-5: 1 999-13-2-022-0003

### Review Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you if you would like to review the request, and ask you to enter new information about the transaction. IFCAP will allow you to enter a new Station number, fiscal year, quarter, and Control Point for the transaction.

Would you like to proceed with copying this request? Yes//

Now enter the information for the new transaction number.

Select STATION NUMBER: 999//ANYCITY,DC

Select FISCAL YEAR: 13//

Select QUARTER: 4//

Select CONTROL POINT: 834 MISC OFFICE SUPPLIES//

### Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will assign a transaction number to the request and prompt you for a form type. Based on which form type you select, IFCAP will prompt you for additional information about the purpose of your request and the source of funds. Read the sections in this guide on creating this form type for explanations of these prompts. Enter “T” for today as the date of the request. Enter your name as the Requestor.

Enter the Service that you are creating the request for at the Requesting Service: prompt.

> **NOTE:** The Requesting Service field is a required field on a 2237.

Enter the date that the goods or services are required. Assign a priority to the request. The priority categories in IFCAP, ranging from shortest to longest delivery time remaining, are “Emergency,” “Special,” and “Standard”. Different stations assign different time durations to these categories. Check with your Fiscal office to determine the durations at your station for these categories.

This transaction is assigned transaction number: 999-13-4-834-0054

THE form type for this request is: REPETITIVE & NON-REPETITIVE

Transaction data is being copied...

CLASSIFICATION OF REQUEST:

SORT GROUP:

DATE OF REQUEST: AUG 5, 2013// (AUG 5, 2013)

REQUESTING SERVICE: LABORATORY

DATE REQUIRED: T+3 (JUL 11, 1994)

PRIORITY OF REQUEST: ST// STANDARD

### Special Remarks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Special Remarks: prompt, explain how the service will use the item, names of other items that would fulfill the same need, and any other information that would help the Purchasing Agent fulfill your request. Purchasing Agents sometimes change orders to fulfill the service’s need faster, find a better item or change the vendor for a better price. Explaining the use of the item will make these tasks easier to accomplish. Enter a cost center. Cost center numbers are listed in the left column of MP-4 Part V, Appendix B-1.

Cost centers allow Fiscal staff to create total expense records for a section or service. Enter 1 at the Select Line Item Number: prompt for the first item on the request. At the Item Master File No.: prompt, enter the item name or number. You can also type three question marks (???) to see a list of the items you can request. If you are not selecting an Item from the Item Master File, you will be prompted to fill in the Item Description.

> **NOTE:** Item Description is now a Required Field. You must enter the text.

Enter how many units of purchase (not number of items) at the Quantity: prompt. At the BOC: prompt, enter the budget object code classification for this item. Budget object codes are defined in MP-4 Part V, Appendix B-2. If you do not know the BOC for this item, enter three question marks and IFCAP will list the available budget object codes. At the Intermediate Product Code: prompt, enter the Intermediate Product Code if there is one. The Intermediate Product Code is a stock number that vendors sometimes use.

SPECIAL REMARKS:

1\>

COST CENTER: 820100 Medical

VENDOR: VENDORTHREE//

Select LINE ITEM NUMBER: 2//

LINE ITEM NUMBER: 2//

ITEM MASTER FILE NO.: 20//

BOC: 2610 Provisions//

QUANTITY: 12//

QTY. BEG. BAL. 20

Select DELIVERY SCHEDULE:

### Add Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter another item number at the Select Line Item Number: prompt if you want to add another item to your request or Edit a different Line Item Number.

Select LINE ITEM NUMBER:

COMMITTED (ESTIMATED) COST: 198.88//

TRANSACTION BEG BAL: 198.88

Select SUB-CONTROL POINT:

DELIVER TO/LOCATION: BLDG 33, Rm 8

At the Justification: prompt, explain why the service or item is needed by the service. Add comments if you like. IFCAP will ask you if you want to review the request again, and will display the current balance of the Control Point, the cost of the request, and the money available to the Control Point from current and prior quarters. IFCAP will ask you if you want to send the request to the Control Point Official for approval.

> **NOTE:** The User will not be able to set the Ready for Approval Flag to YES if either the Requesting Service field or a Line Item Description field is not populated. If a Required field is not populated, the User will see a warning message and be prompted to Edit the 2237 again.

You can copy another request, or ENTER NO at the prompt to return to the Process a Request Menu.

JUSTIFICATION:

1\>

REQUESTOR: IFCAPUSERONE//

ORIGINATOR OF 2237:

COMMENTS:

1\>

Would you like to review this request? NO// (NO)

Current Control Point balance: \$93,500.00

Estimated cost of this request: \$198.88

Is this request ready for approval? YES//

Would you like to copy another request? YES// NO

## Item Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select Item Display from the Process a Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Item Display

### Enter Item Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter an item master number at the prompt. If you do not know the item master number, enter the name of the item. If you do not know the name of the item, type three question marks at the prompt and IFCAP will list the available items.

Select ITEM MASTER NUMBER: ???

CHOOSE FROM:

1 BANDAGE-CAST-6INX5YD

2 CAP-SAFETY-BOTTLE-50S

3 PLASMA-USP 5%

4 TOMATOES CANNED

5 SUGAR

6 CEREAL-SHREDDED-WHEAT-BISQUIT

7 DIETARY SUPPLEMENT

8 PROMETHAZINE INJ 25MG 1ML

9 BATTERY-RECHARGEABLE-9 VOLT

10 PHENYTON SODIUM CAPS 100MG

11 TUBE,TRACH,STERILE,9MM ID

12 SUGAR-REFINED

13 THEOPHYLLINE-TABS-200MG

14 CEREAL-WHEAT

15 LITHIUM-CAP-300MG-100S-UD

16 ENEMA-ADMINISTRATION-SET-DISP

17 NEOSTIGMINE-METHYSULFATE-INJECTION.

18 BEANS, PINTO, CANNED, \#10

19 EGGNOG

20 CORN-CANNED-#10

21 TOWEL-PAPER-140SQIN

Select ITEM MASTER NUMBER: 4TOMATOES CANNED

NUMBER: 4 SHORT DESCRIPTION: TOMATOES CANNED

### Display Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display a series of descriptions of the item, including vendor information, units of purchase, and purchase orders that procured the item. You can either enter another item master number or press the Enter key to return to the Process a Request Menu.

FSC: 8940

LAST VENDOR ORDERED: IFVENDOR1,FIVE

NSN: 8940-00-851-7063 MANDATORY SOURCE: IFVENDOR2,FIVE

DATE ITEM CREATED: JAN 25, 1993 BOC: 2610 Provisions

CREATED BY: IFUSER1,TWOINC: 02183

DESCRIPTION: TOMATOES CANNED WHOLE OR LARGE PIECES DIETETIC NO. 303

VENDOR: IFVENDOR2,FIVE UNIT COST: 1.888

DATE OF UNIT PRICE: JAN 25, 1993 UNIT OF PURCHASE: CS

PACKAGING MULTIPLE: 6 MAXIMUM ORDER QTY: 6

UNIT CONVERSION FACTOR: 3 REQUIRED ORDER MULTIPLE: 6

VENDOR: IFVENDOR1,FIVE UNIT COST: 1.01

DATE OF UNIT PRICE: DEC 2, 1993 UNIT OF PURCHASE: CN

PACKAGING MULTIPLE: 1 UNIT CONVERSION FACTOR: 1

VENDOR: IFVENDOR1,SIXUNIT COST: 1.889

DATE OF UNIT PRICE: JAN 25, 1993 UNIT OF PURCHASE: CN

PACKAGING MULTIPLE: 6 MAXIMUM ORDER QTY: 6

UNIT CONVERSION FACTOR: 1 REQUIRED ORDER MULTIPLE: 6

MINIMUM ORDER QTY: 1

VENDOR: \*\*IFVENDOR1,SEVEN UNIT COST: .89

DATE OF UNIT PRICE: MAR 9, 1993 UNIT OF PURCHASE: CN

PACKAGING MULTIPLE: 1

NSN VERIFIED: DEC 2, 1993 FOOD GROUP: Fruits, Vegetables

SKU: CN

FCP: 002033

PURCHASE ORDER: 002-B40006

LONG NAME (c): SITE: 002 FCP: 033 PHARMACY

FCP: 0027001

PURCHASE ORDER: 002-G38095

PURCHASE ORDER: 002-G30004

PURCHASE ORDER: 002-G38043

LONG NAME (c): SITE: 002 FCP: 7001 SUPPLY FUND

Select ITEM MASTER NUMBER:

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

Select Process a Request Menu Option:

## Vendor Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select Vendor Display from the Process a request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Vendor Display

### Vendor Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a vendor name. If you do not know the vendor name, enter the first few characters of the name. If you do not know the first few characters of the name, enter three question marks at the prompt and IFCAP will list the available vendors.

Select VENDOR NAME: IFVENDOR,FOUR 000-456-7890 NO. 741

SPECIAL FACTORS:

ORDERING ADDRESS: 6877 MAIN ST

ANYTOWN, AK 00001

OK? YES// (YES)

DEVICE: LAT RIGHT MARGIN: 80//

### Display Vendor Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list a comprehensive set of descriptions of the vendor, including address, socioeconomic and business category information, payment information, and contract information. After the list, you can enter another vendor, or press the Enter key at the prompt to return to the Process a Request Menu.

VENDOR LIST JUL 8,1994 16:52 PAGE 1

--------------------------------------------------------------------------------

NUMBER: 741NAME: IFVENDOR,FOUR

ORDERING ADDRESS1: 6877 MAIN ST ORDERING CITY: ANYTOWN

ORDERING STATE: ALASKA ORDERING ZIP CODE: 00001

VA P&C contact phone number: 123-555-5555

SOCIOECONOMIC GROUP (FPDS): OO NONE OF THE ABOVE

BUSINESS TYPE (FPDS): SMALL IS A SF129 ON FILE?: NOT APPLICABLE

FMS VENDOR CODE: 000222444 TAX ID/SSN: 000222444

SSN/TAX ID INDICATOR: SOCIAL SECURITY NUMBER

PAYMENT HOLD INDICATOR: NO 1099 VENDOR INDICATOR: YES

PENDING FLAG: CONFIRMATION OF APPROVAL

CENTRAL REMIT: NO VENDOR TYPE: COMMERCIAL

MTI ACTION: CHANGE

CONTRACT NUMBER: 2432424 EXPIRATION DATE: AUG 4, 1994

BEGINING DATE: APR 16, 1994

PAYMENT PHONE NO.: 409-555-5555 PAYMENT ADDRESS1: 1453 KINWOOD LANE

PAYMENT ADDRESS2: SUITE 100 PAYMENT CITY: BALTIMORE

PAYMENT STATE: MARYLAND PAYMENT ZIP CODE: 21210\\

DATE VENDOR CREATED: JUL 1, 1994 CREATED BY: POSTMASTER

Select VENDOR NAME:

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

Select Process a Request Menu Option:

## Supplementary Options in the 1358 Request Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New 1358 Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select 1358 Request Menu from the Process a Request Menu.

Select New 1358 Request from the 1358 Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List Open 1358s

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: New 1358 Request

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number, fiscal year, fiscal quarter, and Control Point. IFCAP will assign a transaction number to your request. Write this number down. You will need this number to determine the status of your request.

Select STATION NUMBER: 999ANYCITY,DC

Select FISCAL YEAR: 94//

Select QUARTER: 3//

Select CONTROL POINT: 101

1 101 LAB TESTING 101

2 1011 BUDGET RETEST

3 1012 BUDGET RETEST

CHOOSE 1-3: 1

### Authority & Sub-Authority Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Authority field is mandatory on all 1358s. The Sub-Authority is conditionally mandatory based upon the Authority selected by the User.

Enter “??” at the Authority prompt to display the list of 23 Authorities the User may select from. Depending upon the Authority entered, the User may be prompted to enter a Sub-Authority. Enter “??” at the Sub-Authority prompt to display the list of Sub-Authorities that are applicable to the Authority selected.

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

Select AUTHORITY OF REQUEST: 3 STANDARDIZED OBLIGATIONS

Select SUB-AUTHORITY OF REQUEST: ??

Choose from:

A FEDERAL TELECOMMUNICATIONS SERVICES

B COLLEGE OF AMERICAN PATHOLOGY

C CONVENIENCE CHECK FEES

D DENVER ACQUISITION AND LOGISTICS CENTER SERVICES AND SUPPLIES

E EMERGENCY CARE BENEFICIARY TRAVEL, INCLUDING MILEAGE

F FEE BASIS PURCHASE CARD

G FEDERAL EMPLOYEES COMPENSATION PROGRAM

H SHPS

I STANDARD LEVEL USER CHARGES/GSA

J TRANSIT BENEFITS

K FRANCHISE FUND: SECURITY AND INVESTIGATIONS CENTER

L FRANCHISE FUND: LAW ENFORCEMENT TRAINING CENTER

M FRANCHISE FUND: FINANCIAL SERVICES CENTER

N FRANCHISE FUND: DEBT MANAGEMENT CENTER

O FRANCHISE FUND: CORPORATE DATA CENTER OPERATIONS

P FRANCHISE FUND: RECORDS CENTER AND VAULT

Select SUB-AUTHORITY OF REQUEST: e EMERGENCY CARE BENEFICIARY TRAVEL, INCLDING MILEAGE

This transaction is assigned Transaction number: 999-10-4-110-0062

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group.

CLASSIFICATION OF REQUEST: ???

This Classification of Request field allows you

to classify and/or categorize all transactions

(requests) for supplies, services, etc.

This is the previous 'Type of Request" field.

CLASSIFICATION OF REQUEST:

SORT GROUP: ???

This Sort Group field may be used to group together all

transactions (requests) that relate to a specific project,

work order, investigator, food group, doctor, etc.

This is the previous 'Project Number' field.

Enter one of the following:

S.EntryName to select a Sort Group

W.EntryName to select a Work Order

To see the entries in any particular file, type \<Prefix.?\>

If you simply enter a name then the system will search each of

the above files for the name you have entered. If a match is

found the system will ask you if it is the entry that you desire.

However, if you know the file the entry should be in, then you can

speed processing by using the following syntax to select and entry:

\<Prefix\>.\<entry name\>

or

\<Message\>.\<entry name\>

or

\<File Name\>.\<entry name\>

Also, you do NOT need to enter the entire file name or message

to direct the look up. Using the first few characters will suffice.

SORT GROUP:

### Requestor & Cost Center Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Per the implementation of Segregation of Duties within the 1358 options, the User is no longer asked to Enter the name of an individual at the Requestor: prompt. Your name is automatically entered as the Requestor.

Press the Enter key at the Date of Request: prompt to accept the default of today's date. Enter the date that you want to commit funds to your request at the Date Committed: prompt.

Enter the total cost for the 1358 in dollars at the Committed (Estimated) Cost: prompt.

Enter the cost center assigned to the section or service that requested the 1358 at the Cost Center: prompt. Cost centers allow Fiscal staff to create total expense records for a section or service.

DATE OF REQUEST: JUN 29,1994// (JUN 29, 1994)

DATE COMMITTED: 06/01/94// (JUN 01, 1994)

COMMITTED (ESTIMATED) COST: ???

This is the estimated amount of the committed cost of

the requested item(s).

COMMITTED (ESTIMATED) COST: 414 \$ 414.00

COST CENTER: ???

ANSWER WITH COST CENTER

CHOOSE FROM:

800100 Office of Chief Medical Director

810800 Career Development Program

820111 LAB TEST CC

840211 LAB TEST BOC

844111 LAB TEST BOC

850111 LAB TEST BOC

870021 Operating Equipment - Additions

COST CENTER: 800100 Office of Chief Medical

### BOC Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the budget object code classification for the item at the BOC1: prompt. Enter the amount of the item you want to attribute to the budget object code at the BOC1 Amount: prompt. You may also enter a Sub-control Point if you like.

BOC1: ???

Major budget object code classifications are:

10 thru 13 - Personal Services and Benefits

21 - Travel and Transportation of Persons

22 - Transportation of Things

23 - Rent, Communications, and Utilities

24 - Printing and Reproduction

25 - Other Services

26 - Supplies and Materials

31 thru 33 - Acquisition of Capital Assets

ANSWER WITH BUDGET OBJECT CODE

DO YOU WANT THE ENTIRE 62-ENTRY BUDGET OBJECT CODE LIST? Y (YES)

CHOOSE FROM:

1081 Physicians-Full Time

1090 Administrative and Clerical Personnel Not Otherwise Classified

1092 Stay-In-School Program Part-Time Employment of Needy Students

1093 Subsistence & Temp Exp, Real Estate Costs & Misc Exp-PL 89-516

1095 Employee Salary Continuation

1096 Computer Sys Analyst, Programmers, Keypunch & Computer Opr's

BOC1: 1095 Employee Salary Continuation

BOC1 \$ AMOUNT: 40.00 \$ 40.00

Select SUB-CONTROL POINT:

### Vendor & Contract Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Per the changes to IFCAP to implement Segregation of Duties during 1358 processing, IFCAP may or may not require the User to enter a Vendor on the 1358. The Vendor is conditionally mandatory based on the Authority that is selected. The Contract number is also conditionally mandatory based on the Authority selected.

Do you want to enter a vendor for this 1358 request? NO// Y (YES)

VENDOR: IFVENDOR,FOUR 512-555-5555 NO. 7

SPECIAL FACTORS:

ORDERING ADDRESS: 4 SAMPLE ST

ANYTOWN, TX 75434

OK? YES// (YES)

VENDOR CONTRACT NUMBER: ???

Select the appropriate contract number applicable to this request.

ANSWER WITH CONTRACT NUMBER

CHOOSE FROM:

D339347 -- EXP. DATE: 12-12-99

TK-987433-94 -- EXP. DATE: 01-31-98 10% 25 DAYS

VENDOR CONTRACT NUMBER: TK-987433-94-- EXP. DATE: 01-31-98 1

0% 25 DAYS

### Service Start & End Dates/Purpose Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Per the implementation of the Segregation of Duties within the 1358 process, the User is required to enter the appropriate Service Start and End Date for the 1358. The Purpose field is now mandatory and the User is to put in text that is appropriate for the 1358 being created. You may enter the name of the User that requested this 1358 at the Originator prompt.

Add comments if you’d like.

Enter Y at the Is This Request Ready For Approval?: prompt to submit the request to the Control Point Official for approval, or enter N to edit and submit the request later. You can enter another request if you like, or enter N at the Would You Like To Enter Another NEW Request?: prompt to return to the 1358 Request Menu.

SERVICE START DATE: 090110 (SEP 01, 2010)

SERVICE END DATE: 093010 (SEP 30, 2010)

PURPOSE:

1\>For Monthly Costs

2\>

EDIT Option:

ORIGINATOR OF REQUEST:

COMMENTS:

1\>

Current Control Point balance: \$3193125.53

Estimated cost of this request: \$434.00

Is this request ready for approval? YES//

Would you like to enter another NEW request? YES// n (NO)

Select 1358 Request Menu Option:

## Increase/Decrease Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select 1358 Request Menu from the Process a Request Menu.

Select Increase/Decrease Adjustment from the 1358 Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: Increase/Decrease Adjustment

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, fiscal year and fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks and IFCAP will display the available Control Points. At the Select Obligation Number: prompt, enter the purchase order number or obligation number of the 1358 you wish to decrease or increase. The obligation number is the number that Fiscal Service assigns to the 1358. IFCAP will display the transaction number assigned to the adjustment.

Select STATION NUMBER: 002MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 022 IFVENDOR2,FOUR

Select OBLIGATION NUMBER: ???

CHOOSE FROM:

C30032 OBL C30032

C30033 OBL C30033

C30034 OBL C30034

Select OBLIGATION NUMBER: C30032 002-93-2-022-0001 OBL C30032

Original Obligation Amount: \$ 1,000.00 Service Balance: \$ 100.00

Fiscal's 1358 Balance: \$ 1,000.00

This transaction is assigned transaction number: 002-94-4-022-0007

### Classification and Sort Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="PRC_184_B" class="anchor"></span>The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group.

Per the implementation of Segregation of Duties within the 1358 process, you will no longer be prompted to enter a Name at a Requestor prompt. Your name is automatically entered as the Requestor.

The Date of Request field will have a default date that you can change if appropriate.

The Cost Center will have the default value entered onto the original 1358 as the default value. Cost centers allow Fiscal staff to create total expense records for a section or service.

Enter the date that the obligation is being adjusted.

Enter the amount that you want to adjust the obligation at the Adjustment \$Amount prompt. Type the number without any symbols to add money to the obligation. Type a minus symbol in front of the amount to subtract money from the obligation.

CLASSIFICATION OF REQUEST:

SORT GROUP:

DATE OF REQUEST: JUL 8,1994// (JUL 08, 1994)

COST CENTER: 844100 Supply//

DATE OBL ADJUSTED:

ADJUSTMENT \$ AMOUNT: 400 \$ 400.00

### BOC, Sub-Control Point and Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the budget object code classification for the item at the BOC1: prompt. Enter the amount of the item you want to attribute to the budget object code at the BOC1 Amount: prompt. At the Select Sub-Control Point: prompt, you can associate this purchase with a category of purchases that you can define. This allows you to group similar purchases together.

Per the implementation of Segregation of Duties within the 1358 process, the Purpose field is mandatory and you must enter text indicating the reason for the adjustment.

Add comments if you like. IFCAP will let you review the request. IFCAP will list the current Control Point balance, the estimated cost of the adjustment, and the total uncommitted balance from current and prior quarters. IFCAP will allow you to transmit the adjustment to the Control Point Official for approval.

Enter N at the Enter another increase/decrease adjustment?: prompt to return to the 1358 Request Menu.

BOC1: 2580 Miscellaneous Contractural Replace

BOC1 \$ AMOUNT: 400// \$ 400.00

TRANSACTION BEG BAL: 400.00

Select SUB-CONTROL POINT:

PURPOSE:

1\> Monthly Costs for July

COMMENTS:

1\>

Would you like to review this request? NO// (NO)

Current Control Point balance: \$0.00

Estimated cost of this request: \$400.00

Total uncommitted balance from current and prior quarters: \$4734.20

Is this request ready for approval? NO// (NO)

Enter another increase/decrease adjustment? NO//

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option:

## Edit 1358 Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select 1358 Request Menu from the Process a Request Menu.

Select Edit 1358 Request from the 1358 Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: Edit 1358 Request

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number and a Control Point. Enter the transaction number of the 1358 at the Select Control Point Activity Transaction Number: prompt. If you do not know the transaction number, enter three question marks and IFCAP will list the available transactions.

Select STATION NUMBER:

Select CONTROL POINT: 101 ??

Select CONTROL POINT: 022 IFVENDOR2,FOUR

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ???

Attempting lookup in transaction file.

Attempting lookup using 022 IFVENDOR2,FOUR (CONTROL POINT)

1 022 IFVENDOR2,FOUR002-94-4-022-0007 ADJ C30032

2 022 IFVENDOR2,FOUR002-94-1-022-0002 ADJ C30101

3 022 IFVENDOR2,FOUR002-94-1-022-0001 OBL C30101

4 022 IFVENDOR2,FOUR002-93-4-022-0016 OBL

5 022 IFVENDOR2,FOUR002-93-4-022-0015 OBL

TYPE '^' TO STOP, OR

CHOOSE 1-5: 2 002-94-1-022-0002

### Authority & Sub-Authority 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Authority field is mandatory and the Authority entered when the transaction was created will be shown as a default. You may change this value if it is not appropriate for the 1358.

If you Edit the Authority value and select an Authority that requires a Sub-Authority, you will be required to enter a Sub-Authority value. You may ?? both fields to see the list of possible choices.

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group.

Per the implementation of the Segregation of Duties within the 1358 options, the User is no longer asked to Enter the name of an individual at the Requestor: prompt. Your name is automatically entered as the Requestor.

You may Enter a date in the Date of Request field or accept the default date.

Committed field will have a default value that you can accept or change.

Enter the cost of the 1358 at the Committed (Estimated) Cost: prompt.

Enter the budget object code classification for the 1358 at the BOC1: prompt. If you do not know the budget object code, enter three question marks at the prompt and IFCAP will display the available budget object codes.

At the Select Sub-Control Point: prompt, you can associate this purchase with a category of purchases that you can define. This allows you to group similar purchases together.

If a Vendor was entered when the 1358 was initially created, the Vendor name will be shown as a default and you may accept it or change it. If a Contract Number was entered originally it will be the default value and may be accepted. If a Contract Number is required per the Authority entered on the 1358, you must enter a Contract Number.

Purpose: is now a mandatory prompt and the text entered originally will be shown as a default. Enter the name of the User that requested the creation of the 1358 transaction at the Originator of Request: prompt.

If the system displays a Date Received: prompt, enter the date that the service was completed. Add comments if you like.

Enter N at the Would You Like To Review This Request?: prompt to return to the 1358 Request Menu.

CLASSIFICATION OF REQUEST:

SORT GROUP:

DATE OF REQUEST:

DATE COMMITTED: AUG 1,1994//

COMMITTED (ESTIMATED) COST: 20.25//

COST CENTER: 844100 Supply//

BOC1: 2660 Operating Supplies and Ma Replace

BOC1 \$ AMOUNT: 20.25//

TRANSACTION BEG BAL: 20.25

Select SUB-CONTROL POINT:

VENDOR: IFVENDOR,SIX

VENDOR CONTRACT NUMBER:

SERVICE START DATE: 080194//

SERVICE END DATE: 083194//

PURPOSE:

l\>TO TEST SECURITY SYSTEM

EDIT Option:

ORIGINATOR OF REQUEST: IFUSER,THREE //

COMMENTS:

1\>

Would you like to review this request? NO// (NO)

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option:

## Create/Edit Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select 1358 Request Menu from the Process a Request Menu.

Select Create/Edit Authorization from the 1358 Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Transaction Report – eCMS/IFCAP

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: Create/Edit Authorization

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number and a Control Point. Enter an obligation number. If you do not know the obligation number, type three question marks and IFCAP will list the available obligations. The obligation number is the number assigned to the transaction by Fiscal Service. Enter the recipient of the funds and any additional information that would aid in the processing of this transaction at the Reference: prompt (e.g., patient ICN, date of services). Add comments if you like. At the Would you like to EDIT or CREATE an Authorization: prompt, enter “E” to edit an authorization or “C” to create an authorization, or press the Enter key to return to the 1358 Request Menu. An authorization is a unique number that IFCAP uses to record individual charges against a 1358.

Select STATION NUMBER: 002MYTOWN, PA

Select CONTROL POINT: 022 IFVENDOR2,FOUR

Select OBLIGATION NUMBER: ?

ANSWER WITH CONTROL POINT ACTIVITY PURCHASE ORDER/OBLIGATION NO

DO YOU WANT THE ENTIRE CONTROL POINT ACTIVITY LIST? Y (YES)

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

Would you like to EDIT or CREATE an Authorization: CreATE

This entry has been assigned transaction number: 0003.

Obligation amount: \$ 500.00Fiscal balance: \$ 500.00

Service balance: \$ 500.00

AUTHORIZATION AMOUNT: (.01-999999999.99): 200

REFERENCE:

COMMENTS:

Would you like to EDIT or CREATE an Authorization: N

If you want to EDIT an existing authorization type 'E'

If you want to CREATE a NEW authorization type 'C'

OR press \<RETURN\>

Would you like to EDIT or CREATE an Authorization:

Select OBLIGATION NUMBER:

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option:

Select 1358 Request Menu Option: display 1358 Balance

Select STATION NUMBER: 999

Select CONTROL POINT: 081 SPD SEEMA 0160A1 10 0100 010028100

Select OBLIGATION NUMBER: c15093 999-C15093 07-07-11 1358 Obligated - 1358

FCP: 081 \$ 1000.00

999-C15093 OBLIGATION BALANCES

OBLIGATION AMOUNT: \$ 1,000.00 SERVICE BALANCE: \$ 1,000.00

LIQUIDATION BALANCE: \$ 1,000.00 TOTAL LIQUIDATIONS: \$0.00

AUTHORIZATION BALANCE(S):

AUTHORIZATION TOTAL: \$0.00

### Display 1358 Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will assign a transaction number to the entry, and display the obligation amount, the fiscal balance, and the service balance. The fiscal balance is the dollar amount Fiscal Service shows is still available to the Control Point after the entry has been obligated by Fiscal Service. The fiscal balance is what the Accounting Technician will read to determine if the Control Point has sufficient funds to meet the obligation. The service balance is what you have committed, the dollar amount left in the Control Point minus the non-obligated committed funds. Enter the recipient of the funds and any additional information that would aid in the processing of this transaction at the Reference: prompt (e.g., patient name, patient Social Security Number, or Vendor). Add comments if you like. At the Would you like to EDIT or CREATE an Authorization: prompt, enter “E” to edit an authorization or “C” to create an authorization, or press the Enter key to return to the 1358 Request Menu. An authorization is a unique number that IFCAP uses to record individual charges against a 1358.

This entry has been assigned transaction number: 0003.

Obligation amount: \$ 500.00Fiscal balance: \$ 500.00

Service balance: \$ 500.00

AUTHORIZATION AMOUNT: (.01-999999999.99): 200

REFERENCE:

COMMENTS:

Would you like to EDIT or CREATE an Authorization: N

If you want to EDIT an existing authorization type 'E'

If you want to CREATE a NEW authorization type 'C'

OR press \<RETURN\>

Would you like to EDIT or CREATE an Authorization:

Select OBLIGATION NUMBER:

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option:

## Daily Activity Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select 1358 Request Menu from the Process a Request Menu.

Select Daily Activity Enter/Edit from the 1358 Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: Daily Activity Enter/Edit

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, a Control Point, and an obligation number. If you do not know the obligation number, enter three question marks at the prompt and IFCAP will list the available obligations. At the Select Action: prompt, enter 1 to create a new bill activity, enter 2 to edit an existing bill activity, or enter 3 to quit and return to the 1358 Request Menu.

Select STATION NUMBER: 002MYTOWN, PA

Select CONTROL POINT: 022 IFVENDOR2,FOUR

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

1 Create a NEW bill activity

2 Edit existing bill activity

3 QUIT

Select ACTION: (1-3): 1

### Select Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter an authorization. An authorization is a unique number that IFCAP uses to record individual charges against a 1358. If you do not know the authorization, enter three question marks and IFCAP will list the available authorizations. IFCAP will list the amount of the authorization and the current balance of the authorization. IFCAP will also list any daily records of transactions posted against the authorization.

> **NOTE:** You must deduct the dollar amount for each invoice you receive from the balance of the 1358. If you mark the 1358 as complete, you will no longer be able to edit or access that 1358.

IFCAP will assign a number to the daily activity entry. Enter N at the Is this the final daily activity?: prompt to create another entry. Enter the amount of the activity at the Daily Activity Amount: prompt. Do not exceed the authorization balance. You may enter a vendor invoice number, a reference, and a description if you like. If the amount of the daily activity that you create is equal to the authorization balance, IFCAP will ask you to confirm that you want to clear the balance on the authorization and mark it as complete. IFCAP will then return to the 1358 Request Menu.

Select AUTHORIZATION: ???

CHOOSE FROM:

311 002-C30033-0003

Select AUTHORIZATION: 311 002-C30033-0003

Excuse me, This may take a few moments...

Authorization amount : \$ 200.00

Authorization balance: \$ 200.00

Daily Records:

This DAILY ACTIVITY ENTRY has been assigned: 002-C30033-0003-1

Is this the final daily activity? NO// YES

Daily Activity AMOUNT: (.01-999999999.99): 200

VENDOR INVOICE NUMBER:

REFERENCE:

DESCRIPTION:

This will zero out the balance on this authorization

and mark this authorization as complete.

Do you want to continue? YES

REFERENCE:

COMMENTS:

Authorization balance has been reduced to ZERO, and this authorization has

been marked as complete.

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option:

## Recalculate 1358 Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select 1358 Request Menu from the Process a Request Menu.

Select Recalculate 1358 Balance from the 1358 Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: Recalculate 1358 Balance

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, a Control Point, and an obligation number. If you do not know the obligation number, enter three question marks and IFCAP will list the available obligation numbers. Once you enter an obligation number, IFCAP will list the Fund Control Point that funds it and the current balance, and will return to the 1358 Request Menu.

Select STATION NUMBER: 002MYTOWN, PA

Select CONTROL POINT: 039 ANYSITE ISC

Select OBLIGATION NUMBER: 002-C40004 -- 1358 Obligated - 1358

FCP: 039 \$ 5.00

002-C40004 OBLIGATION BALANCES

OBLIGATION AMOUNT: \$ 5.00 SERVICE BALANCE: \$ 0.90

LIQUIDATION BALANCE: \$ 5.00TOTAL LIQUIDATIONS: \$ 0.00

AUTHORIZATION BALANCE(S):

002-C40004-0003 AMOUNT: \$2.00 BALANCE: \$0.00 PYMT: \$2.00

002-C40004-0004 AMOUNT: \$2.10 BALANCE: \$0.00 PYMT: \$2.10

\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_

\$4.10 \$0.00 \$4.10

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option:

## Display 1358 Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select 1358 Request Menu from the Process a Request Menu.

Select Display 1358 Balance from the 1358 Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Recalculate 1358 Balance

Select 1358 Request Menu Option: Display 1358 Balance

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, a Control Point, and an obligation number. If you do not know the obligation number, enter three question marks and IFCAP will list the available obligation numbers. Once you enter an obligation number, IFCAP will list the Fund Control Point that funds it and the current balance, and will return to the 1358 Request Menu.

Select STATION NUMBER: 002MYTOWN, PA

Select CONTROL POINT: 039 ANYSITE ISC

Select OBLIGATION NUMBER: 002-C40004 -- 1358 Obligated - 1358

FCP: 039 \$ 5.00

002-C40004 OBLIGATION BALANCES

OBLIGATION AMOUNT: \$ 5.00 SERVICE BALANCE: \$ 0.90

LIQUIDATION BALANCE: \$ 5.00TOTAL LIQUIDATIONS: \$ 0.00

AUTHORIZATION BALANCE(S):

002-C40004-0003 AMOUNT: \$2.00 BALANCE: \$0.00 PYMT: \$2.00

002-C40004-0004 AMOUNT: \$2.10 BALANCE: \$0.00 PYMT: \$2.10

\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_

\$4.10 \$0.00 \$4.10

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option:

## List Open 1358s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select 1358 Request Menu from the Process a Request Menu.

Select List Open 1358s from the 1358 Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: List Open 1358s

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, fiscal year and fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks and IFCAP will list the available Control Points.

IFCAP will print or display an “Open 1358 Daily Record,” listing each authorization, the balance remaining on the authorization, and the reference. After printing or displaying the record, IFCAP will return to the 1358 Request Menu.

Select STATION NUMBER: 002MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 022 IFVENDOR2,FOUR

DEVICE: LAT RIGHT MARGIN: 80//

OPEN 1358 DAILY RECORDS JUL 8,1994 17:29 PAGE 1

AUTHORIZATION

AUTHORIZATION \# BALANCE REFERENCE

--------------------------------------------------------------------------------

002-C30032-0002 0.00 FED EX

002-C30032-0003500.00 UPS

002-C30034-0002 0.00 FED EX

002-C30035-000225.00 FED EX

002-C30036-0002 0.00 FED EX

002-C30036-0003500.00 UPS

002-C30093-0002500.00 FED EX

002-C30097-0005 2.50 TRAINING ENTRY

002-C30097-000620.00 ENTERY 2

002-C30101-0002 0.11 ELECTRIC

002-C30101-000350.00 WATER

002-C30101-0004100.00 FUEL

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option:

## Print 1358

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select 1358 Request Menu from the Process a Request Menu.

Select Print 1358 from the 1358 Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: Print 1358

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number and a control point. Enter an obligation number. If you do not know the obligation number, enter three question marks and IFCAP will list the available obligations. You may also create a report that includes what the requestor entered in the ‘Description’ category, and print the daily records for each authorization.

Select STATION NUMBER: 002//MYTOWN, PA

Select CONTROL POINT: 022 MISC OFFICE SUPPLIES//

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

Would you like to print the Description field for each 1358 Daily Record entry? NO// (NO)

Would you like to print the daily records for each authorization? NO//

DEVICE: HOME// LAT RIGHT MARGIN: 80//

### Display or Print 1358

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will print each 1358 for the obligation number you selected, with the transaction number of each 1358 on the upper-left hand corner of the 1358. Enter a caret (^) at the Select Station Number: prompt to return to the 1358 Request Menu.

400-11-3-041-0067 JUL 27, 2011@13:13:29 PAGE 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:NURSING HOME/ADULT DAYCARE

NURSING HOME

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Originator of Request:

Requestor: \|Date Requested: \|Obligation No.:

CPCLERK,TWO \|APR 26, 2011 \| 400-C15090

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Vendor: \|Contract Number:

COMMUNITY HOSPITAL HOME CARE \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Name and Title Approving Off.: \|Signature:\|Date Signed:

CP OFFICIAL,ONE \|/ES/CPOFFICIAL,ONE \|APR 28, 2011@09:3

1:56

\|\|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FUND CERTIFICATION: The supplies and services listed on this request are

properly chargeable to the following allotments, the available balances of

which are sufficient to cover the cost thereof, and funds have been obligated.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press return to continue, "^" to exit:

400-11-3-041-0067 400-C15090 PAGE 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:NURSING HOME/ADULT DAYCARE

NURSING HOME

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Appropriation & Acct. Symbols: \|Obligated By: \|Date Obligated:

400-3610160-041-824100-2580 010044100 \|/ES/CP OFFICIAL TESTER\|MAY 13, 2011

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORITY: 1 SUB: A

SERVICE START DATE: 04/01/11 SERVICE END DATE: 04/30/11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Purpose:

APRIL HOSPITAL CARE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press return to continue, "^" to exit:

400-11-3-041-0067 400-C15090 PAGE 3

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:NURSING HOME/ADULT DAYCARE

NURSING HOME

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ESTIMATED OBLIGATION RECAP

DATE REF# CPA#AMOUNT BALANCE

05/13 0001 400-11-3-041-0067 \$ 100.00\$ 100.00

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORIZATION & ORDER RECORD LIQUIDATION RECORD

AUTH. AUTH. CUMULATIVE UNLIQ

DATE SEQ# REFERENCE AMOUNT BALANCE AUTH. AMT. LIQUID BAL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TOTALS \$ 0.00 \$ 0.00 \$ 0.00 \$ 100.00

VA FORM 4-1358a-ADP (NOV 1987)

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Recalculate 1358 Balance

Select 1358 Request Menu Option:

## Print Obligated 1358s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select 1358 Request Menu from the Process a Request Menu.

Select Print Obligated 1358s from the 1358 Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: 1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List 1358’s with Open Authorizations

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Select 1358 Request Menu Option: Print Obligated 1358s

### Display or Print Obligated 1358s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a date range and device to obtain a list of obligated 1358s with a dollar value of \$0 and higher. Your previous entries for the START and GO TO P.O. DATES will appear as the defaults.

The report includes information such as Obligation. \#, date and amount; Service Start and End dates, Authority/Sub-Authority, Requestor; and vendor and contract information, if it was entered when the 1358s were created.

This option should be printed at 132 columns.

\* Previous selection: P.O. DATE from Oct 1,2005 to Oct 31,2005@24:00

START WITH P.O. DATE: Oct 1,2005// (OCT 01, 2005)

GO TO P.O. DATE: Oct 31,2005// (OCT 31, 2005)

DEVICE: HOME// LAT RIGHT MARGIN: 80// 132

PROCUREMENT & ACCOUNTING TRANSACTIONS LIST (OBLIGATED 1358s) FEB 6,2006 13:13 PAGE 1

BUSINESS

PURCHASE VENDOR CONTRACT TYPE SOCIOECONOMIC TOTAL

ORDER NUMBER P.O. DATE VENDOR NUMBER(FPDS) GROUP (FPDS AMOUNT REQUESTOR

SERVICE START DATE SERVICE END DATE

AUTHORITY

SUB-AUTHORITY

-------------------------------------------------------------------------------

999-B05029 SEP 16,2010 1000 USER,NAME299

09/16/10 09/26/10

2 FEE BASIS

A FEE MEDICAL/DENTAL (PRE-AUTHORIZED)

999-C15094 SEP 17,2010 A EXAMPLE MD400 USER,NUAME33

09/17/10 09/17/4 LIMITED OPEN TRAVEL AUTHORITY

## Outstanding Approved Requests Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Process a Request Menu from the Control Point Clerk’s Menu.

Select Outstanding Approved Requests Report from the Process a Request Menu.

Select Control Point Clerk’s Menu Option: Process a Request Menu

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

Select Process a Request Menu Option: Outstanding Approved Requests Report

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station Number, a fiscal year and a fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks and IFCAP will list the available Control Points. IFCAP will list each outstanding request for the Control Point you select. Type a caret (^) at the Select Station Number: prompt to return to the Process a Request Menu.

Select STATION NUMBER: 002//MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 022 MISC OFFICE SUPPLIES//

DEVICE: HOME// LAT RIGHT MARGIN: 80//

OUTSTANDING APPROVED REQUEST REPORT - CP 022 JUL 8,1994@17:34:10 PAGE 1

TRANSACTION NUMBER TRANSACTION STATUSVENDOR

DATE SIGNED EST. DEL. DATE PO \# DATE OBL. DATE REQ.

--------------------------------------------------------------------------------

999-088-400101-94-3 OBL IFVENDOR,FOUR

04-09-94 05-02-94 999-088-94-3 04-09-94 05-04-94

------------------

End of processing

Select STATION NUMBER: 002//^

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

Select Process a Request Menu Option:

## Transaction Report – eCMS/IFCAP 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is based on data in the IFCAP/ECMS TRANSACTION file (#414.06). As 2237s are sent to and from eCMS via HL7 messages, certain information about each transaction is stored in this file. This report lists transactions that have been sent to eCMS, returned by eCMS, or cancelled by eCMS.

> **NOTE:** You will only be able to view data about the 2237 transactions related to the Control Point(s) on which you are identified as a Control Point Clerk or Official.

### Menu Navigation

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

The selection criteria for the report to be generated include: Single 2237, Single eCMS Contact, Date Range, Single Station, Sub-station (if applicable, and YES response to Single Station prompt), Single Fund Control Point, and up to four distinct Event Types.

The report is based on data in the new IFCAP/ECMS TRANSACTION file (#414.06). As 2237s are sent to and from eCMS via HL7 messages, certain information about each transaction is stored within this file.

The User is able to generate a report for a Single 2237. User must be a Clerk or Official on the Control Point selected for the 2237.

Select Process a Request Menu \<TEST ACCOUNT\> Option: transaction Report - eCMS/I

FCAP

Select a single 2237 TRANSACTION NUMBER? NO// y YES

Select a 2237: 999-13-4

1 999-13-4-110-0060

2 999-13-4-914-0009

CHOOSE 1-2: 2 999-13-4-914-0009

The single 2237, 999-13-4-914-0009, has been selected for printing.

DEVICE: HOME// 0;80;999 DECWINDOWS

JUL 21, 2013@03:27 eCMS/IFCAP TRANSACTION LOG REPORT p. 1

eCMS 2237: 999-13-4-914-0009

IFCAP Reference Message Event Event Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

999-13-4-914-0009 2237 SENT JUN 26, 2013@16:51:22

ACKNOWLEDGED: JUN 26, 2013@16:52:23

999-13-4-914-0009 RETURN TO CONTROL POINT JUN 26, 2013@17:10:54

ACKNOWLEDGED: JUN 26, 2013@17:10:55

eCMS CONTACT: XXXXX@va.gov PHONE: 501-257-1038

RETURN/CANCEL DATE: JUN 26, 2013@16:10:28

REASON: Returned to the Control Point Level in IFCAP

999-13-4-914-0009 2237 CANCELLED BY ECMS JUN 26, 2013@17:41:29

ACKNOWLEDGED: JUN 26, 2013@17:41:30

eCMS CONTACT: XXXXX@va.gov PHONE: 501-257-1038

RETURN/CANCEL DATE: JUN 26, 2013@16:41:10

REASON: Cancel the PR and Return to IFCAP

END OF REPORT

The User can generate a report for 2237s Sent from eCMS either by all possible eCMS Contacts (user accepts default value of NO), or a specific individual (user says YES.) In the latter (YES) scenario, a list of possible eCMS Contact choices is displayed, from which the User selects one. This is shown in the following screen capture.

Select Process a Request Menu \<TEST ACCOUNT\> Option: Transaction Report - eCMS/I

FCAP

Select a single 2237 TRANSACTION NUMBER? NO//

Select a single eCMS Contact? NO// y YES

1 eCMS USER1 USER1.eCMS@va.gov

2 eCMS USER2 USER2.eCMS@va.gov

3 USER FOUR FOUR.USER@va.gov

4 USER7 eCMS eCMS.USER7@va.gov

Select one of the above eCMS Contacts: 3

Select one of the above eCMS Contacts: FOUR USER

Select ALL DATES: (JUN 06, 2012 - JUL 21, 2013)? NO// y YES

Select a single STATION NUMBER? NO//

Select a single FUND CONTROL POINT? NO//

TRANSACTION EVENTS:

1 Sent to eCMS (includes resent 2237s)

2 Returned to Accountable Officer

3 Returned to Control Point

4 Cancelled within eCMS

Select one or more of the above events: 1-4// 2-4

Display event ERROR TEXT? NO//

All eCMS 2237s matching your selections below will be displayed:

eCMS Contact: FOUR.USER@va.gov

All dates: (JUN 06, 2012 - JUL 21, 2013)

All Stations and Substations

All Fund Control Points

Event Types selected are:

2 = Returned to Accountable Officer

3 = Returned to Control Point

4 = Cancelled within eCMS

A note will display for any errors, but not the full text.

DEVICE: HOME//

JUL 21, 2013@03:39 eCMS/IFCAP TRANSACTION LOG REPORT p. 1

eCMS 2237: ALL eCMS Contact: Anne.Klein@va.gov Station: ALL

Report Date Range: JUN 06, 2012 - JUL 21, 2013 Control Point: ALL

Events: Returned to AO, Returned to CP, Cancelled within eCMS

IFCAP Reference Message Event Event Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

001-12-4-060-0017 RETURN TO CONTROL POINT JUL 20, 2012@16:47:59

SUBSTATION: 001ACKNOWLEDGED: JUL 20, 2012@16:48

eCMS CONTACT: Four.User@va.gov PHONE: 202-632-0000 ext 257

RETURN/CANCEL DATE: JUL 20, 2012@16:16:25

REASON: Requires line edit

This RETURN TO CONTROL POINT has ACKNOWLEDGMENT ERROR TEXT.

001-12-4-145-0024 RETURN TO ACCOUNTABLE OFFICER JUL 18, 2012@17:02:59

SUBSTATION: 001A4 ACKNOWLEDGED: JUL 18, 2012@17:03

eCMS CONTACT: Four.User@va.gov PHONE: 202-632-0000 ext 257

RETURN/CANCEL DATE: JUL 18, 2012@14:16:23

REASON: Need to redirect

This RETURN TO ACCOUNTABLE OFFICER has ACKNOWLEDGMENT ERROR TEXT.

A Control Point User may generate a report for 2237 transaction records from one specific Control Point or a specific Date Range or Station. Note: The Control Point User is only permitted to view data related to Control Points on which that CP User is a Clerk or an Official.

## Status of Requests Reports Menu: Supplementary Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Print/Display Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Status of Requests Reports Menu from the Control Point Clerk’s Menu.

Select Print/Display Request Form from the Status of Requests Reports Menu.

Enter a Station Number and a Control Point. Enter a transaction number. If you do not know the transaction number, enter three question marks at the prompt and IFCAP will display the available transactions.

Select Control Point Clerk’s Menu Option: Status of Requests Reports Menu

Print/Display Request Form

Status of All Obligation Transactions

Requests Ready for Approval List

PO with Associated Transactions

Select Status of Requests Reports Menu Option: Print/Display Request Form

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list every request for the Control Point you select. Type a caret (^) at the Select Station Number: prompt to return to the Status of Requests Reports Menu.

Select STATION NUMBER: 999

Select CONTROL POINT: 081 SPD SEEMA 0160A1 10 0100 010028100

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: C15

1 C15093 999-11-4-081-0002 OBL C15093

2 C15096 999-11-4-081-0003 OBL C15096

CHOOSE 1-2:2

EVICE: HOME// TELNET Right Margin: 80//

999-11-4-081-0003 JUL 27, 2011@13:23:34 PAGE 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:FEE BASIS

FEE MEDICAL/DENTAL (NOT PRE-AUTHORIZED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Originator of Request:

Requestor: \|Date Requested: \|Obligation No.:

CP CLERK,TWO \|JUL 07, 2011 \| 999-C15096

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Vendor: \|Contract Number:

\|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Name and Title Approving Off.:\|Signature: \|Date Signed:

OFFICIAL CP\|/ES/OFFICIAL CP \|JUL 07, 2011@15:32:39

FCP OFFICIAL \| \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FUND CERTIFICATION: The supplies and services listed on this request are

properly chargeable to the following allotments, the available balances of

which are sufficient to cover the cost thereof, and funds have been obligated.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press return to continue, "^" to exit:

999-11-4-081-0003 999-C15096 PAGE 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:FEE BASIS

FEE MEDICAL/DENTAL (NOT PRE-AUTHORIZED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Appropriation & Acct. Symbols: \|Obligated By: \|Date Obligated:

999-3610160-081-828100-2580 010028100 \|/ES/TECH ACCT \|JUL 19, 2011

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORITY: 2 SUB: B

SERVICE START DATE: 07/01/11 SERVICE END DATE: 07/31/11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Purpose:

MONTHLY COSTS

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press return to continue, "^" to exit:

999-11-4-081-0003 999-C15096 PAGE 3

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE:FEE BASIS

FEE MEDICAL/DENTAL (NOT PRE-AUTHORIZED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ESTIMATED OBLIGATION RECAP

DATE REF# CPA#AMOUNT BALANCE

07/19 0001 999-11-4-081-0003 \$ 10000.00\$ 10000.00

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORIZATION & ORDER RECORD LIQUIDATION RECORD

AUTH. AUTH. CUMULATIVE UNLIQ

DATE SEQ# REFERENCE AMOUNT BALANCE AUTH. AMT. LIQUID BAL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TOTALS \$ 0.00 \$ 0.00 \$ 0.00 \$ 10000.00

VA FORM 4-1358a-ADP (NOV 1987)

Enter information for another report or an uparrow to return to the menu.

Select STATION NUMBER: 002// ^

Print/Display Request Form

Status of All Obligation Transactions

Requests Ready for Approval List

PO with Associated Transactions

Select Status of Requests Reports Menu Option:

## Status of All Obligation Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Status of Requests Reports Menu from the Control Point Clerk’s Menu.

Select Status of all Obligation Transactions from the Status of Requests Reports Menu.

Enter a Station number, fiscal year and fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points.

Select Control Point Clerk’s Menu Option: Status of Requests Reports Menu

Print/Display Request Form

Status of All Obligation Transactions

Requests Ready for Approval List

PO with Associated Transactions

Select Status of Requests Reports Menu Option: Status of All Obligation Transactions

Select STATION NUMBER: 002//MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 121 LAB TESTING 121//

DEVICE: LAT RIGHT MARGIN: 80//

### Display Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list each transaction number, the vendor assigned to the transaction, and the description that the requestor entered for the item. Type a caret (^) at the Select Station Number: prompt to return to the Status of Requests Reports Menu.

STATUS OF OBLIGATION TRANSACTIONS CP: 101 LAB TESTING 101 FY: 94

JUL 14,1994 09:33 PAGE 1

PRIORITY

OF DATE DATE DATE DATE

TRANS \# REQUEST SIGNED REQUIRED DELIVERED RECEIVED

VENDORSTATUS

OBLIGATION# SORT GROUP

FIRST LINE ITEM DESCRIPTION

COMMENTS

--------------------------------------------------------------------------------

94-4-0213 STANDARD 05/27/94

IFVENDOR,SEVEN

ITEM \#4

94-4-0214 STANDARD 05/27/94

IFVENDOR,SEVEN

ITEM \#4

STATUS OF OBLIGATION TRANSACTIONS CP: 101 LAB TESTING 101 FY: 94

JUL 14,1994 09:33 PAGE 2

PRIORITY

OF DATE DATE DATE DATE

TRANS \# REQUEST SIGNED REQUIRED DELIVERED RECEIVED

VENDORSTATUS

OBLIGATION# SORT GROUP

FIRST LINE ITEM DESCRIPTION

COMMENTS

--------------------------------------------------------------------------------

Select STATION NUMBER: 999// ^

Print/Display Request Form

Status of All Obligation Transactions

Requests Ready for Approval List

PO with Associated Transactions

Select Status of Requests Reports Menu Option:

## PO with Associated Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Status of Requests Reports Menu from the Control Point Clerk’s Menu.

Select PO with Associated Transactions from the Status of Requests Reports Menu.

Select Control Point Clerk’s Menu Option: Status of Requests Reports Menu

Print/Display Request Form

Status of All Obligation Transactions

Requests Ready for Approval List

PO with Associated Transactions

Select Status of Requests Reports Menu Option: PO with Associated Transactions

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station Number and a Control Point. Enter a purchase order number or obligation number. The obligation number is the number that Fiscal Service assigns to the 1358. If you do not know the number, enter three question marks and IFCAP will list the available purchase orders and obligations. Choose whether you want the comments for each purchase order and obligation to appear on the report.

Select STATION NUMBER: 999//ANYCITY,DC

Select CONTROL POINT: 040 BUILDING MANAGEMENT// ???

Select PURCHASE ORDER/OBLIGATION NO: ???

Attempting lookup in transaction file.

Attempting lookup using 040 BUILDING MANAGEMENT (CONTROL POINT)

1 040 BUILDING MANAGEMENT 002-93-2-040-0009 OBL C30092

2 040 BUILDING MANAGEMENT 002-93-2-040-0006 OBL C30065

3 040 BUILDING MANAGEMENT 002-93-2-040-0005 OBL C30064

4 040 BUILDING MANAGEMENT 002-93-2-040-0004 OBL C30063

5 040 BUILDING MANAGEMENT 002-93-2-040-0003 OBL C30062

TYPE '^' TO STOP, OR

CHOOSE 1-5: 1 002-93-2-040-0009

Would you like to include 'Comments'? YES// n (NO)

DEVICE: LAT RIGHT MARGIN: 80//

### Print Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will print an ‘Obligation Status Report,’ which lists each purchase order and obligation, its amount, the vendor assigned (if any), and the status of the purchase or obligation. Read Chapter 4 to learn more about determining the status of a request. Type a caret (^) at the Select Station Number: prompt to return to the Status of Requests Reports Menu.

OBLIGATION STATUS REPORT JUL 8,1994 17:44 PAGE 1

TRANSACTION NUMBER TYPE \$ AMOUNT VENDOR

STATUS

COMMENTS

--------------------------------------------------------------------------------

PURCHASE ORDER/OBLIGATION NO: C30092

002-93-2-040-0009 OBLIGATION 500.00 Obligated - 1358

Needed by Dietetics -----------

TOTAL 500.00

Select STATION NUMBER: 002// ^

Print/Display Request Form

Status of All Obligation Transactions

Requests Ready for Approval List

PO with Associated Transactions

Select Status of Requests Reports Menu Option:

## Requests Ready for Approval List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Status of Requests Reports Menu from the Control Point Clerk’s Menu.

Select Requests Ready for Approval List from the Status of Requests Reports Menu.

Enter a Control Point.

Select Control Point Clerk's Menu Option: Status of Requests Reports Menu.

Print/Display Request Form

Status of All Obligation Transactions

Requests Ready for Approval List

PO with Associated Transactions

Select Status of Requests Reports Menu Option: Requests Ready for Approval List

Select CONTROL POINT: 101 LAB TESTING 101

DEVICE: LAT RIGHT MARGIN: 80//

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list each permanent request that has not been approved by a Control Point Official, its transaction number, form type, vendor (if there is one) and description. Type a caret (^) at the Select Control Point: prompt to return to the Control Point Clerk’s Menu.

REQUESTS TO BE APPROVED LISTJUL 8,1994 17:49 PAGE 1

TRANSACTION NUMBER TYPE FORM TYPE

REQUESTOR REQUESTED REQUIRED

EST COST

VENDOR FIRST ITEM DESCRIPTION

--------------------------------------------------------------------------------

999-94-4-101-0318 ADJ 1358 ORDER FORM

JUL 7,1994

LONG LASTING TELEPHONE LINES

999-94-3-101-0156 OBL NON-REPETITIVE (2237) ORDER

IFUSER,TWO APR 18,1994 MAY 8,1994

8000.00

IFVENDOR,TWO Roofing Material

Press return to continue or uparrow to exit:

Select CONTROL POINT: 101 LAB TESTING 101// ^

Requests Ready for Approval List

Process a Request Menu ...

Display Control Point Activity Menu ...

Funds Control Menu ...

Status of Requests Reports Menu ...

Record Date Received by Service Menu ...

Select Control Point Clerk’s Menu Option:

## Supplementary Options in the Display Control Point Activity Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purchase Order Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Display Control Point Activity Menu from the Control Point Clerk’s Menu.

Select Purchase Order Status from the Display Control Point Activity Menu.

Enter a Control Point and a purchase order number. If you do not know the purchase order number, you can enter the vendor name, method of processing, Fund Control Point, inventory distribution point, or requisition number, and IFCAP will list all of the purchase orders under the criterion you select. If you do not know any of this information, enter three question marks at the prompt and IFCAP will list the available purchase orders.

Select Control Point Clerk’s Menu Option: Display Control Point Activity MenuPurchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option: Purchase Order Status

Select CONTROL POINT: 101 LAB TESTING 101//

Select PURCHASE ORDER NUMBER: ???

CHOOSE FROM:

999-A40001 11-10-93 CI Ordered and Obligated (Amended) FCP: 101 \$ 300.00

999-A40002 11-17-93 ST Complete Order Received But Not Ob FCP: 101 \$ 76.10

999-A40003 11-22-93 ST Complete Order Received But Not Ob FCP: 101 \$ 12.30

999-A40004 11-22-93 ST Complete Order Received But Not Ob FCP: 101 \$ 10.00

999-A40005 11-24-93 ST Partial Order Received (Amended) FCP: 101 \$ 33.00

999-A40006 11-24-93 ST Complete Order Received FCP: 101 \$ 12.30

999-A40007 11-24-93 ST Complete Order Received FCP: 101 \$ 25.00

999-A40008 12-01-93 ST Cancelled Order FCP: 101 \$ 0.00

999-A40009 12-01-93 ST Partial Order Received (Amended) FCP: 101 \$ 20.00

999-A40010 12-02-93 ST Partial Order Received FCP: 101 \$ 30.00

999-A40011 12-02-93 ST Ordered and Obligated FCP: 101 \$ 60.00

Select PURCHASE ORDER NUMBER: A40004 999-A40004 11-22-93 ST Complete Order Received But Not Ob

FCP: 101 \$ 10.00

### Status Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list the status of the purchase order you select and its Fund Control Point. You may look at a short display of the purchase order, or review the entire purchase order. Enter a caret (^) at the Select Control Point: prompt to return to the Display Control Point Activity Menu.

Purchase Order Status: Complete Order Received But Not Oblig.

Would you like the purchase order display? NO// (NO)

Would you like to review the entire purchase order? NO// (NO)

Enter information for another report or an uparrow to return to the menu.

Select CONTROL POINT: 101 LAB TESTING 101// ^

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option:

## Temporary Transaction Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Display Control Point Activity Menu from the Control Point Clerk’s Menu.

Select Temporary Transaction Listing from the Display Control Point Activity Menu.

Enter a Control Point. If you do not know the Control Point, enter three question marks and IFCAP will list the available Control Points. IFCAP will list all of the temporary transactions for the Control Point, or will list transactions created on or after a date that you specify at the Start With Date of Request: prompt.

Select Control Point Clerk’s Menu Option: Display Control Point Activity Menu

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option: Temporary Transaction Listing

Select CONTROL POINT: 101 LAB TESTING 101//

START WITH DATE OF REQUEST: FIRST//

DEVICE: LAT RIGHT MARGIN: 80//

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will generate a list of each temporary transaction, the date it was created, the requestor that created it, the vendor (if any) the first item on the request, and the amount of the transaction. After generating the list, IFCAP will return to the Display Control Point Activity Menu.

TEMPORARY TRANSACTION LISTING - CONTROL POINT 101 LAB TESTING 101

JUL 8,1994 17:54 PAGE 1

TEMPORARYDATE OF FIRST LINE ITEM COMM.

TRANSACTION \# REQUEST REQUESTOR VENDOR DESCRIPTION COST

--------------------------------------------------------------------------------

CONTROL POINT: 101 LAB TESTING 101

WER246 APR 19,1994 IFUSER,SIX IFVENDOR,FOUR 40.00

SIFUS627 JUN 27,1994 IFUSER,SEVEN 99999.27

MCG JUN27 JUN 27,1994 IFUSER,SEVEN IFVENDOR,FOUR 23.45

KMB601 JUN 27,1994IFVENDOR,SEVEN 10.00

KIMBIE2 JUN 30,1994 IFUSER,EIGHT IFVENDOR,SEVEN 10.00

USER90 JUN 30,199410.00

KMN5 JUL 5,1994 IFUSER,NINE IFVENDOR2,SIX ITEM \#11 48.00

KMBZ2 JUL 6,1994 IFUSER,EIGHT IFVENDOR,SEVEN ITEM \#25 12.23

KMN7 JUL 14,1994 IFUSER,EIGHT IFVENDOR,SEVEN ITEM \#17 23.84

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option:

## Transaction Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Display Control Point Activity Menu from the Control Point Clerk’s Menu.

Select Transaction Status Report from the Display Control Point Activity Menu.

Enter a transaction number. If you do not know the transaction number, enter three question numbers and IFCAP will list the available transactions.

Select Control Point Clerk’s Menu Option: Display Control Point Activity Menu

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option: Transaction Status Report

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ???

Attempting lookup in transaction file.

Attempting lookup using 101 LAB TESTING 101 (CONTROL POINT)

1 101 LAB TESTING 101 999-94-4-101-0325 OBL IFVENDOR2,FIVE TEST ITEM \#17

2 101 LAB TESTING 101 999-94-4-101-0324 OBL IFVENDOR2,FIVE TEST ITEM \#17

3 101 LAB TESTING 101 999-94-4-101-0323 ADJ C45003

4 101 LAB TESTING 101 999-94-4-101-0322 ADJ C45003

5 101 LAB TESTING 101 999-94-4-101-0321 ADJ C45040

TYPE '^' TO STOP, OR

CHOOSE 1-5: 3 999-94-4-101-0323

DEVICE: HOME// LAT RIGHT MARGIN: 80//

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list the type of transaction, the vendor (if any), the purchase order number, the amount of the adjustment used to fund the transaction(Adjustment Amount), and other classification data for the transaction. Enter a caret (^) at the Select Control Point Activity Transaction Number: prompt to return to the Display Control Point Activity Menu.

ADJUSTMENT TRANSACTION STATUS DISPLAYJUL 8,1994@17:56:16

Transaction Number: 999-94-4-101-0323 Transaction Type: ADJUSTMENT

Vendor:

Purchase Order/Obligation No.: C45003 Adjustment \$ Amount: \$100.00

Date Obl.Adjusted: Accounting Data: 3640151.001 3040/21-25

FMS \$ Amount: \$0.00 FMS Date:

FMS Transaction Code:

Sort Group:Classification of Request:

Enter information for another report or an uparrow to return to the menu.

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ^

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option:

OBLIGATION TRANSACTION STATUS DISPLAYJUL 21,2013@03:01:12

Transaction Number: 001-13-3-110-0010 Transaction Type: OBLIGATION

A&MM Status: Sent to eCMS (P&C)

Temporary Trans. Number:

Form Type: REPETITIVE (PR CARD) ORDER

Date of Request: APR 29,2013 Date Required: MAY 9,2013

Est. Delivery Date: Date Received:

Vendor: BAXTER HEALTHCARE CORPORATION P.O. Vendor:

Committed (Estimated) Cost: \$100.00 Date Committed: APR 29,2013

Obligated (Actual) Cost: \$0.00 Date Obligated:

Purchase Order/Obligation No.: Accounting Data: 3630160

FMS \$ Amount: \$0.00 FMS Date:

FMS Transaction Code:

Return to Service Comments:

Comments:

Transaction Number: 001-13-3-110-0010 Transaction Type: OBLIGATION

Requestor: IFCP1 Form Type: REPETITIVE (PR CARD) ORDER

Requestor's Title: Requesting Service: REHAB MEDICINE

Approving Official: IFCPO3 Inventory Dist. Point:

Appr. Official's Title: GRANDMA Cost Center: 820300 Psychiatry

Date Signed (Approved): APR 29,2013

Justification: want this stuff right away! needed on the wards.

Deliver To/Location: bdlkej33

Classification of Request:

Sort Group:

Would you like to review the item information for this request? No//

## Running Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Display Control Point Activity Menu from the Control Point Clerk’s Menu.

Select Running Balances from the Display Control Point Activity Menu.

Enter a fiscal year, fiscal quarter, and a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points. Enter Y at the Would you like a summary report (bottom line balances only)?: prompt to see the current balance for the Control Point. Enter Y to see all of the line items that cause this balance.

Select Control Point Clerk’s Menu Option: Display Control Point Activity Menu

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option: Running Balances

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 101 LAB TESTING 101//

Summary Balances Report Only? No// Y (Yes)

DEVICE: HOME// UCX/TELNET Right Margin: 80//

STATION: 999 FUND CONTROL POINT: 060 FISCAL SVC

FISCAL YEAR: 00 QTR: 3

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list the total amount of funds available to the Control Point Official (Control Point Official's Balance), how much of that money has not been obligated for a purchase, and how much has been committed to pay for a purchase. You may create another running balances report or return to the Control Point Activity Menu.

Select STATION NUMBER: 999//

Select FISCAL YEAR: 12//

Select QUARTER: 1// 4

Select CONTROL POINT: 110 MONEY BAG 0160A1 10 0100 010042116

Summary Balances Report Only? No// (No)

DEVICE: HOME// DECWINDOWS

CONTROL POINT BALANCE - 999-12-4-110- MAVIS AUG 07, 2012@16:32:04 PAGE 1

FISCAL

FYQSeq# TXN OBL \#AP/OB DT COMM \$AMT CP \$BAL OBL \$AMT UNOBL \$BAL

--------------------------------------------------------------------------------

1240012 CEI 999FC0607 04/02/12 1000000.00 998362.60 1000000.00 1000000.00

1230013 OBL 05/08/12 147.60 998215.00 0.00\*1000000.00

1230014 OBL 04/11/12 40.80 998174.20 0.00\*1000000.00

1230015 OBL 05/08/12 455.80 997718.40 0.00\*1000000.00

1230016 OBL 05/14/12 20.00 997698.40 0.00\*1000000.00

1230017 OBL 0.00\* 997698.40 0.00\*1000000.00

1230018 OBL 0.00\* 997698.40 0.00\*1000000.00

1230019 OBL 0.00\* 997698.40 0.00\*1000000.00

1230020 OBL 0.00\* 997698.40 0.00\*1000000.00

1230021 OBL 05/17/12 396.00 997302.40 0.00\*1000000.00

1230022 OBL 05/18/12 2962.55 994339.85 0.00\*1000000.00

Press return to continue, up-arrow (^) to exit:

CONTROL POINT BALANCE - 999-12-4-110- MAVIS AUG 07, 2012@16:32:04 PAGE 2

FISCAL

FYQSeq# TXN OBL \#AP/OB DT COMM \$AMT CP \$BAL OBL \$AMT UNOBL \$BAL

--------------------------------------------------------------------------------

1230023 OBL 05/25/12 120283.90 874055.95 0.00\*1000000.00

1240024 OBL22.40\* 874055.95 0.00\*1000000.00

1230025 OBL 06/12/12 301.84 873754.11 0.00\*1000000.00

1230026 OBL 1245.00\* 873754.11 0.00\*1000000.00

1230027 OBL 0.00\* 873754.11 0.00\*1000000.00

1230028 OBL129.60\* 873754.11 0.00\*1000000.00

1230029 OBL 06/14/12 78.20 873675.91 0.00\*1000000.00

1230030 OBL 06/21/12 390.55 873285.36 0.00\*1000000.00

1230031 OBL 0.00\* 873285.36 0.00\*1000000.00

1230032 OBL 06/22/12 39990.11 836405.25 0.00\*1000000.00

1230033 OBL 06/22/12 3308.70 833096.55 0.00\*1000000.00

1240035 CEI 999FC0607 06/22/12 10000000.0010833096.5510000000.0011000000.00

1240039 CEI FROM 12-3 10575000.0021408096.5510575000.0021575000.00

CONTROL POINT BALANCE - 999-12-4-110AUG 07, 2012@16:32:04 PAGE 3

FISCAL

FYQSeq# TXN OBL \#AP/OB DT COMM \$AMT CP \$BAL OBL \$AMT UNOBL \$BAL

--------------------------------------------------------------------------------

1240041 ADJ QTRADJ 0.00 21408096.55 21575000.00

1240042 OBL 07/11/12 36.00 21408060.55 0.00\*21575000.00

1240043 OBL B20004 07/27/12 310.00 21407750.55 310.00 21575000.00

1240044 OBL 0.00\*21407750.55 0.00\*21265000.00

Press return to continue, up-arrow (^) to exit:

CONTROL POINT BALANCE - 999-12-4-110- MAVIS AUG 07, 2012@16:32:04 PAGE 4

FISCAL

FYQSeq# TXN OBL \#AP/OB DT COMM \$AMT CP \$BAL OBL \$AMT UNOBL \$BAL

--------------------------------------------------------------------------------

FMS transaction total for this quarter: \$0.00

================================================================================

Balance Summary1st Quarter 2nd Quarter 3rd Quarter 4th Quarter

Actual CP Bal: 0.00 0.00 0.00 21407750.55

Actual Fiscal Bal: 0.00 0.00 0.00 21265000.00

Tot Commit, not Obl: 0.00 0.00 0.00 142750.55

SECTION 1 CODES \# - cancelled order \* - order not obligated or signed

@ - purchase card order for reconciliation

& - reconciled order with final charge - ready for approval

R - total reconciled charges

SECTION 2 CODES

@ - purchase card CC transaction is not reconciled

The symbols '\*','@', and '&' indicate incomplete items.

Please take the necessary steps to clear these items.

Would you like to run another running balances report? No//

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

CP Entered, Not Approved Requests

Select Display Control Point Activity Menu Option:

## Item History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Display Control Point Activity Menu from the Control Point Clerk’s Menu.

Select Item History from the Display Control Point Activity Menu.

Enter a Control Point. Enter the name or item master number of the item you want to review. If you do not know the name or item master number of the item, enter three question marks at the prompt and IFCAP will list the available items.

Select Control Point Clerk’s Menu Option: Display Control Point Activity Menu

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option: Item History

Select CONTROL POINT: 101 LAB TESTING 101//

Select one of the following:

LLast 5 Purchase Orders

DDate Range

Select ITEM HISTORY Viewing Method: L// ast 5 Purchase Orders

Select ITEM MASTER NUMBER: ???

CHOOSE FROM:

102 102 PEN SET

103 103 TRASH CAN

104 104 NAILS

105 105 LADDER

106 106 SURGICAL GLOVES

107 107 NEEDLES

108 108 THERMOMETERS

Select ITEM MASTER NUMBER: 103TRASH CAN

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list the last five purchase orders in the system that included this item. You may look at another Item History, or return to the Display Control Point Activity Menu.

ITEM HISTORY

Item Number: 103Description: TRASH CAN

Quantity

Previously Unit of Quantity

Date Ordered PO Number Received Purchase Unit Cost Total Cost Ordered

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MAY 31,1994 999-B400541 EA 9.00 90.00 10

Vendor: IFVENDOR,EIGHT

MAY 3,1994 999-A40680 EA 10.00 20.002

Vendor: IFVENDOR,NINE

MAY 2,1994 999-A40674 EA 10.00 20.002

Vendor: IFVENDOR,NINE

Would you like to look at another Item History? NO// (NO)

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option:

## PPM Status of Transactions Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Display Control Point Activity Menu from the Control Point Clerk’s Menu.

Select PPM Status of Transactions Report from the Display Control Point Activity Menu.

Enter a fiscal year, a fiscal quarter, and a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points.

Select Control Point Clerk’s Menu Option: Display Control Point Activity Menu

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option: PPM Status of Transactions Report

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT:// ???

CHOOSE FROM:

11 011 CONSULTANT & ATTENDING

33 033 337 Basil Pharmacy Test

101 101 LAB TESTING 101

Select CONTROL POINT: // 101 LAB TESTING 101

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will print a ‘PPM Transaction Status Report’, listing each transaction, whether funds have been obligated for the transaction, the cost of the transaction, the date the items or services are required, the date that funds were obligated for the transaction, the requestor, the originator of the request (the permanent transaction), and the status of the request. Enter a caret (^) at the Select Fiscal Year: prompt to return to the Display Control Point Activity Menu.

PPM TRANSACTION STATUS REPORT - CP 101 OCT 11,1994@10:00:35 PAGE 1

PO/OBL# COMM. OBLIG.

2237# (EST) COST (ACT) COST DATE REQ. DATE OBL.

REQUESTOR ORIGINATOR OF REQUEST

STATUS

-------------------------------------------------------------------------------

999-94-4-101-0326 \$23.84JUL 20,1994

Pending Accountable Officer Sig.

999-94-4-101-0328 \$23.84JUL 20,1994

Pending Accountable Officer Sig.

999-94-4-101-0342 \$541.79JUL 13,1994

IFUSER,TWOIFVENDOR,TWO

Pending Accountable Officer Sig.

999-94-4-101-0409 \$4.049AUG 15,1994 SEP 26,1994

IFUSER,TWOIFVENDOR,TWO

Assigned to PPM Clerk

999-94-4-101-0457 \$100 SEP 22,1994

IFUSER,THREE

Pending Accountable Officer Sig.

END OF REPORT

Select FISCAL YEAR: 95// ^

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Select Display Control Point Activity Menu Option:

## Supplementary Options in the Funds Control Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Enter FCP Adjustment Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Enter FCP Adjustment Data from the Funds Control Menu.

Enter a Station Number, a fiscal year and a fiscal quarter. Enter a Control Point. If you do not know the control point, enter three question marks and IFCAP will list the available Control Points. IFCAP will assign a transaction number to the adjustment.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Enter FCP Adjustment Data

Select STATION NUMBER: 002MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 022 IFVENDOR2,FOUR

This transaction is assigned transaction number: 002-94-4-022-0008

### Sort Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter an obligation number for the transaction. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Make sure that you include all applicable purchases in the sort group and exclude all purchases that do not belong to the sort group. Enter today’s date at the Date Obligation Adjusted: prompt. Enter the adjustment dollar amount for this obligation transaction at the Adjustment \$Amount: prompt. Enter the cost center at the Cost Center: prompt if this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses. Cost centers allow Fiscal staff to create total expense records for a section or service.

OBLIGATION NUMBER: C40021

SORT GROUP:

DATE OBL ADJUSTED:

ADJUSTMENT \$ AMOUNT: ??

Enter the adjustment dollar amount (from -9999999.99 to 9999999.99) for

this obligation transaction

ADJUSTMENT \$ AMOUNT: 40 \$ 40.00

COST CENTER: 870021 Operating Equipment

### BOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the budget object code classification for the item at the BOC1: prompt. If you do not know the budget object code, enter three question marks at the prompt and IFCAP will display the available budget object codes.

BOC1: ???

Select the appropriate budget object code for this request.

Major budget object code classifications are:

10 thru 13 - Personal Services and Benefits

21 - Travel and Transportation of Persons

22 - Transportation of Things

23 - Rent, Communications, and Utilities

24 - Printing and Reproduction

25 - Other Services

26 - Supplies and Materials

31 thru 33 - Acquisition of Capital Assets

ANSWER WITH BOC

DO YOU WANT THE ENTIRE 27-ENTRY BOC LIST? Y (YES)

CHOOSE FROM:

2220 Other Shipments

2299 LAB TEST BOC

2343 ADP Equipment Rental

2520 Repair of Furniture and Equipment

2535 Interior Decorating Services

2540 Laundry and Drycleaning Services

2543 Maintenance and Repair Services

BOC1: 2540 Laundry and Drycleaning S

### Amount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the amount of the item you want to attribute to the budget object code at the BOC1 Amount: prompt. Enter a second BOC at the BOC2: prompt if you like. Select a Sub-Control Point if you like. Add comments if you like. You may enter another adjustment transaction or return to the Funds Control Menu.

BOC1 \$ AMOUNT: ??

Type a Dollar Amount between -9999999.99 and 9999999.99, 2 Decimal Digits

BOC1 \$ AMOUNT: 40. \$ 40.00

BOC2:

BOC2 \$ AMOUNT:

TRANSACTION BEG BAL: 40.00

Select SUB-CONTROL POINT:

COMMENTS:

1\>

Would you like to enter another Adjustment transaction? YES// n (NO)

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option:

## Assign Ceiling to Sub-Control Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Assign Ceiling to Sub-Control Points from the Funds Control Menu.

Enter the Control Point. If you do not know the Control Point, enter three question marks and IFCAP will list the available Control Points.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Assign Ceiling to Sub-Control Points

Select CONTROL POINT: ??

CHOOSE FROM:

11 011 CONSULTANT & ATTENDING

33 033 337 Basil Pharmacy Test

101 101 LAB TESTING 101

Select CONTROL POINT: 101 LAB TESTING 101

### Select Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a ceiling transaction number. If you do not know the ceiling transaction number, enter three question marks and IFCAP will list the available ceiling transaction numbers. IFCAP will list the balance of the transaction you selected.

Select CEILING TRANSACTION NUMBER: ???

Attempting lookup in transaction file.

Attempting lookup using 101 LAB TESTING 101 (CONTROL POINT)

1 101 LAB TESTING 101 999-94-4-101-0285 CEIL 999FC0139 This is a multiple transaction for a widget.

2 101 LAB TESTING 101 999-94-3-101-0284 CEIL 999FC0138 This is a multiple transaction for a widget.

3 101 LAB TESTING 101 999-94-2-101-0283 CEIL This is a multiple transaction for a widget.

4 101 LAB TESTING 101 999-94-1-101-0282 CEIL This is a multiple transaction for a widget.

5 101 LAB TESTING 101 999-94-4-101-0258 CEIL FC0135 Test

TYPE '^' TO STOP, OR

CHOOSE 1-5: 1 999-94-4-101-0285

TRANSACTION BEG BAL: 533.00

### Enter Sub-Control Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter one or more Sub-Control Points if you like. Enter the amount of the ceiling at the \$Amount: prompt. IFCAP will deduct the ceiling amount you enter from the transaction amount and ask if you want to assign it to another Sub-Control Point. You may also assign a ceiling to Sub-Control Points from another ceiling transaction. After completing the ceiling assignment, IFCAP will return to the IFCAP Menu.

Select SUB-CONTROL POINT: 1 ??

Select SUB-CONTROL POINT: ???

This is an additional sub-control point. IFCAP

allows more than one sub-control point on each transaction

to get a quantity discount.

CHOOSE FROM:

100

KARENS

SHOES

TEST

This is the name of the sub-control point.

Select SUB-CONTROL POINT: 100

ARE YOU ADDING '100' AS A NEW SUB-CONTROL POINT (THE 1ST FOR THIS CONTROL POIN

T ACTIVITY)? Y

(YES)

\$ AMOUNT: 230 RUNNING TOTAL: 230.00 BAL: 303.00

Select SUB-CONTROL POINT:

The transaction \$ amount is \$ 533.00.

You still have \$ 303.00 available that could be assigned to your

sub-control points. Do you want to re-edit your entries? YES// (YES)

TRANSACTION BEG BAL: 533.00

Select SUB-CONTROL POINT: 100// Shoes

ARE YOU ADDING 'SHOES' AS A NEW SUB-CONTROL POINT (THE 2ND FOR THIS CONTROL PO

INT ACTIVITY)? Y

(YES)

\$ AMOUNT: 303 RUNNING TOTAL: 533.00 BAL: 0.00

Select SUB-CONTROL POINT:

Would you like to assign ceiling to sub-control points from another ceiling transaction? NO// (NO)

Select IFCAP MENU Option: Control Point Clerk’s Menu ...

Select Control Point Clerk’s Menu Funds Control Menu ...

## Recalculate Fund Control Point Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Recalculate Fund Control Point Balance from the Funds Control Menu.

Enter a fiscal year, a fiscal quarter and a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will display the available Control Points. IFCAP will display ‘DONE’ after the Control Point name when it has finished recalculating the balance and return to the Funds Control Menu.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Recalculate Fund Control Point Balance

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 101 LAB TESTING 101

Submit RECALCULATE CONTROL POINT BALANCES to the TASK MANAGER? YES//

Requested Start Time: NOW// (JUN 19, 2000@10:50:47)

RECALCULATE CONTROL POINT BALANCES HAS TASK NUMBER 229629

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option:

## Supplementary Options in the Funds Control Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Quarterly Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk's Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select Quarterly Report from the Funds Control Reports Menu.

Enter a fiscal year, fiscal quarter and a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will display the available Control Points.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: Quarterly Report

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 101 LAB TESTING 101//

DEVICE: LAT RIGHT MARGIN: 80//

### Display Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the ‘Control Point Quarterly Report’, which lists the transaction, the type, the cost, and the Control Point Balance. At the end of the report, IFCAP will list the total amount of committed, unobligated money for the Control Point and the total uncommitted balance for the Control Point from current and prior quarters. Enter a caret (^) at the Select Fiscal Year: prompt to return to the Funds Control Reports Menu.

QUARTERLY REPORT - 999-00-3-060- FISCAL JUN 19, 2000@10:58:19 PAGE: 1

TRANS \$ OBL/CEIL DATE DATE DATE

SEQ# TYPE PO/OBL# AMOUNT \$ AMOUNT REQ. OBL. REC'D.

CONTROL POINT UNCOMMITTED UNOBLIGATED

REQUEST TOTAL BALANCE BALANCE

VENDOR FIRST LINE DESCRIPTION

COMMENT

--------------------------------------------------------------------------------

0007 CEI 10000.00 10000.00 DEC 27, 1999

0.00 10000.00 10000.00

Initial seeding of funds

0011 CEI1000000.001000000.00 DEC 27, 1999

0.00 1010000.00 1010000.00

0013 CAN 0.00#

0.00 1010000.00 1010000.00

Transaction 999-00-3-060-0013 replaced by trans. 999-00-3-060-0015

QUARTERLY REPORT - 999-00-3-060- FISCAL JUN 19, 2000@10:58:19 PAGE: 2

TRANS \$ OBL/CEIL DATE DATE DATE

SEQ# TYPE PO/OBL# AMOUNT \$ AMOUNT REQ. OBL. REC'D.

CONTROL POINT UNCOMMITTED UNOBLIGATED

REQUEST TOTAL BALANCE BALANCE

VENDOR FIRST LINE DESCRIPTION

COMMENT

--------------------------------------------------------------------------------

0014 OBL 414.00\*

-414.00 1010000.00 1010000.00

Pepsi

0015 OBL 30.00\* JUN 11, 2000

-444.00 1010000.00 1010000.00

IFVENDOR1,EIGHTFCP, QCS NORMAL ASSAY

0016 ISS 17.70\* JUN 12, 2000

-461.70 1010000.00 1010000.00

IFVENDOR2,FIVE TAPE-ADHESIVE SURGICAL, 2INX10YD

QUARTERLY REPORT - 999-00-3-060- FISCAL JUN 19, 2000@10:58:19 PAGE: 3

TRANS \$ OBL/CEIL DATE DATE DATE

SEQ# TYPE PO/OBL# AMOUNT \$ AMOUNT REQ. OBL. REC'D.

CONTROL POINT UNCOMMITTED UNOBLIGATED

REQUEST TOTAL BALANCE BALANCE

VENDOR FIRST LINE DESCRIPTION

COMMENT

--------------------------------------------------------------------------------

0030 ADJ C40021 40.00 40.00

-4869.85 1007426.00 1009046.00

================================================================================

PO transaction (no 2237) total for this quarter: \$0.00

================================================================================

FMS transaction total for this quarter: \$0.00

================================================================================

Total Request Amount: -\$4869.85

Control Point Official's Balance: \$1007426.00

Fiscal's Unobligated Balance: \$1009046.00

Would you like to run another quarterly balance report? No//

## Ceiling Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select Ceiling Report from the Funds Control Reports Menu.

Enter a fiscal year, fiscal quarter and a Control Point.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: Ceiling Report

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 101 LAB TESTING 101

DEVICE: LAT RIGHT MARGIN: 80//

### Display Ceiling Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will create a ‘Ceiling Report’, listing the transaction number, ceiling amount, the date the funds were allocated, and comments. IFCAP will list the total ceiling amount and the total uncommitted balance from current and prior quarters at the bottom of the report. Enter a caret (^) at the Select Fiscal Year: prompt to return to the Funds Control Reports Menu.

CEILING REPORT - CP: 101 LAB TESTING 101 JUL 8,1994 18:24 PAGE 1

TRANS \# PAT \#

CEILING \$ DATE

AMOUNT ALLOCATED

COMMENTS

--------------------------------------------------------------------------------

94-4-0004 500000.00 NOV 17,1993

94-4-0043 -20.00 JAN 13,1994

94-4-0047 25000.00 FEB 1,1994

94-4-0150 1000.04 APR 15,1994

94-4-0253 FC0135 40.00 MAY 27,1994 Training program

94-4-0258 FC0135 23412.00 JUN 6,1994 Test

94-4-0285 999FC0139533.00 JUN 8,1994

This is a multiple transaction for a widget.

-----------

TOTAL 549965.04

Total uncommitted balance from current and prior quarters: \$1280869.77

Select FISCAL YEAR: 94// ^

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option:

## Audit Transaction List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select Audit Transaction List from the Funds Control Reports Menu.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: Audit Transaction List

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a fiscal year, a fiscal quarter and a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will display the available Control Points. Enter the last date of transactions that you want to audit at the Date: prompt. IFCAP will display the total uncommitted balance from current and prior quarters. Enter a caret (^) at the Select Fiscal Year: prompt to return to the Funds Control Reports Menu.

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 101 LAB TESTING 101

Enter the cutoff date for this reconciliation report

DATE: T-20 (JUN 24, 1994)

Cutoff date must be greater than first day of the quarter you selected.

Enter the cutoff date for this reconciliation report

DATE: T (JUL 14, 1994)

DEVICE: LAT RIGHT MARGIN: 80//

Total uncommitted balance from current and prior quarters: \$1271262.23

Select FISCAL YEAR: 94// ^

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option:

## Sort Group Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select Sort Group Report from the Funds Control Reports Menu.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: Sort Group Report

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, fiscal year, and fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points. You may list all of the sort groups on the report, or you can begin the report with a sort group that you specify. The Sort Group Report will list every transaction for the Control Point and fiscal quarter that you specify, listed by transaction, purchase order or obligation number, request type, vendor name, committed funds and obligated funds. After printing the report, IFCAP will return to the Funds Control Reports Menu.

Select STATION NUMBER: 002 MYTOWN

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 039 ANYSITE ISC

START WITH SORT GROUP: FIRST//

DEVICE: LAT RIGHT MARGIN: 80//

SORT GROUP REPORT - CP: 039 ANYSITE ISC AUG 18,1994 10:43 PAGE 1

TRANSACTION NUMBER PO/OBL# TYPE VENDOR COMM \$ OBL \$

COMMENTS

002-94-4-12341234 C94124 OBL IFVENDOR,FOUR 4.002.00

002-94-4-92138403 C94127 OBL IFVENDOR1,NINE45.00 45.00

TOTAL 45.00 45.00

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: Sort Group Report

## Classification of Request Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select Classification of Request Report from the Funds Control Reports Menu.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: Classification of Request Report

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, a fiscal year and a fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points. After printing the report, IFCAP will return to the Funds Control Reports Menu.

Select STATION NUMBER: 002MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 022 IFVENDOR2,FOUR

START WITH CLASSIFICATION OF REQUEST: FIRST// ???

This Classification of Request field allows you

to classify and/or categorize all transactions

(requests) for supplies, services, etc.

This is the previous 'Type of Request" field.

TEST01

This is the name used to identify the type of request. File \#410.2

is pointed to by the Classification of Request field (#8) of the

Control Point Activity file, \#410.

START WITH CLASSIFICATION OF REQUEST: FIRST//

DEVICE: LAT RIGHT MARGIN: 80//

----------- -----------

CLASSIFICATION OF REQUEST REPORT - 022 MISC OFFICE SUPPLIES

JUL 8,1994 21:54 PAGE 1

OBL# TRANS# TYPE VENDOR COMM \$ OBL \$

COMMENTS

--------------------------------------------------------------------------------

A43050 2902 OBL IFVENDOR,TEN494.62 494.62

A43057 2907 OBL IFVENDOR,TEN 3720.16 3308.65

A43067 2910 OBL IFVENDOR,TEN420.12 420.12

A43072 2924 OBL IFVENDOR,TEN566.04 326.04

---------- ---------

TOTAL 4549.43 4549.43

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option:

## Cost Center Totals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select Cost Center Totals from the Funds Control Reports Menu.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: Cost Center Totals

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a Station number, fiscal year, and fiscal quarter. Enter the cost center at the Select Cost Center Name: prompt if this purchase is assigned to a section or service that has a cost center defined in IFCAP for their expenses. Cost centers allow Fiscal staff to create total expense records for a section or service.

Select STATION NUMBER: 002//MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select COST CENTER NAME: ???

CHOOSE FROM:

100000100000 General Admin-Central Off Staff (Excl of Oper Depts) - Summary of Accts

110100110100 Office of the Secretary

110200110200 Off of Assoc Deputy Admstr for Congressional & Intergovt'l Affairs

110300110300 Board of Contract Appeals

110500110500 Board of Veterans Appeals

111600111600 Office of Public and Consumer Affairs

120000120000 Office of the General Counsel

Select COST CENTER NAME: 111600 Office of Public and Co

DEVICE: HOME// LAT RIGHT MARGIN: 80//

### Print Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will print a ‘Cost Center Totals Report’, listing each transaction for the cost center. Enter a caret (^) at the Select Station Number: prompt to return to the Funds Control Reports Menu.

COST CENTER TOTALS REPORT JUL 8,1994@21:57:22 PAGE 1

STATION 002, 4TH QUARTER, FY94

--------------------------------------------------------------------------------

COST CENTER: 822400 Pharmacy

CONTROL POINT: 040 OFC&MISC SUP 90

----------------------------------

CONTROL POINT: 100 PHARMACY SVC 119

-----------------------------------

TOTALS FOR ALL CONTROL POINTS

----------------------------

TOTAL COMMITTED (ESTIMATED) COST: 826042.81

TOTAL OBLIGATED (ACTUAL) COST: 725194.04

TOTAL (BEST ESTIMATE) COST: 740985.77

Enter information for another report or an uparrow to return to the menu.

Select STATION NUMBER: 002// ^

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option:

## BOC Totals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select BOC Totals from the Funds Control Reports Menu.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: BOC Totals

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, fiscal year, and fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points. IFCAP will print a ‘Budget Object Code Totals Report’, listing the budget object code totals for the Control Point you specified. Enter a caret (^) at the Select Station Number: prompt to return to the Funds Control Reports Menu.

Select STATION NUMBER: 603//MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 022 MISC OFFICE SUPPLIES//

DEVICE: HOME// LAT RIGHT MARGIN: 80//

BUDGET OBJECT CODE TOTALS REPORT JUL 8,1994@21:59:53 PAGE 1

STATION 002, 4TH QUARTER, FY94 ,CONTROL POINT 022 MISC OFFICE SUPPLIES

--------------------------------------------------------------------------------

BUDGET OBJECT CODE TOTALS

-----------------

2580 Miscellaneous Contractual Services by Individuals, Inst 175.00

2631 Chemical suplies 4007.74

2632 Other Medical and Dental Supplies 21851.70

2660 Operating Supplies and Materials 1307.40

-------------------------------------

TOTAL OBLIGATED (ACTUAL) COST: 27761.84

TOTAL OBLIGATED (ESTIMATED) COST: 27696.69

Enter information for another report or an uparrow to return to the menu.

Select STATION NUMBER: 002//^

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option:

## Sub-Control Point Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select Sub-Control Point Report from the Funds Control Reports Menu.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: Sub-Control Point Report

### Print Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may print the report for an entire fiscal year, or for a quarter that you specify. Enter a Station number, a fiscal year, and a fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points. You may list all of the Sub-Control Points, or you may begin the report at a Sub-Control Point that you specify. IFCAP will list all of the Sub-Control Point expenditures for the Control Point by fiscal quarter, transaction number and type, vendor name, item description, amount, and SCP amount (amount spent by that Sub-Control Point) for that quarter. After printing the report, IFCAP will return to the Funds Control Reports Menu.

Would you like the report printed for a full Fiscal Year? YES// (YES)

Select STATION NUMBER: 603//MYTOWN, PA

Select FISCAL YEAR: 94//

Select CONTROL POINT: 022 MISC OFFICE SUPPLIES//

START WITH SUB-CONTROL POINT: FIRST//

DEVICE: LAT RIGHT MARGIN: 80//

---------

SUB-CONTROL POINT EXPENDITURES - 022 MISC OFFICE SUPPLIES

JUL 8,1994 22:04 PAGE 1

FY-Q

FIRST LINE

TRANS \# TYPE PO/OBL# VENDOR ITEM DESC. \$ AMOUNT SCP AMT

--------------------------------------------------------------------------------

94-4

0327 OBL C54141 IFVENDOR,FOUR PROJECTOR 5000.00 -5000.00

0327 ADJ C54277 IFVENDOR1,TEN REAGENT-ST -2962.70 2962.70

0327 CEI6755.00 6755.00

---------

TOTAL 4717.70

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option:

## Reconciliation of PO/Sub-CP Dollar Amounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select Reconciliation of PO/Sub-CP Dollar Amounts from the Funds Control Reports Menu.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: Reconciliation of PO/Sub-CP Dollar Amounts

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, fiscal year, and fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points. IFCAP will list the reconciliation’s for the Control Point that you specified and return to the Funds Control Reports Menu.

Select STATION NUMBER: 002MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 022 IFVENDOR2,FOUR

DEVICE: LAT RIGHT MARGIN: 80//

PO/SCP \$ RECONCILIATION 22-94-4 JUL 9,1994 08:59 PAGE 1

SEQ \# TYPE REQUESTED RECEIVED PO \#

VENDOR

COM \$ OBL \$ ADJ \$

SCP \$ AMOUNT ITEM DESC

--------------------------------------------------------------------------------

STATUS: Obligated - 1358

0007 ADJ JUL 8,1994 C30032

400.00 400.00

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option:

## BOC Detail Totals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select BOC Detail Totals from the Funds Control Reports Menu.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Men

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: BOC Detail Totals

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, fiscal year and fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points. IFCAP will print a ‘Budget Object Code Detail Totals’ report, listing each budget object code by its transactions and transaction cost. IFCAP will provide a total for all budget object codes, and list the total uncommitted balance for the Control Point from current and prior quarters. After printing the report, IFCAP will return to the Funds Control Reports Menu.

This report displays item costs from 2237 orders, sorted

by budget object code.

Select STATION NUMBER: 002//MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 022 MISC OFFICE SUPPLIES//

DEVICE: LAT RIGHT MARGIN: 80//

BUDGET OBJECT CODE DETAIL TOTALS JUL 9,1994 09:01 PAGE 1

LINE

ITEM

TRANSACTION NUMBER NUMBER DESCRIPTION

EST. ITEM

QUANTITY (UNIT) COST TOTAL

BOC: 1007 Computer Systems

WER1234 1

1.00 449.00 449.00

----------

SUBTOTAL 449.00

BOC: 1081 Physicians-Full T

002-94-3-101-0002 2 NONE AGAIN

1.000.00 0.00

----------

SUBTOTAL 0.00

BOC: 1091 Federal,Summer Em

999-94-4-022-0002 1 LIGHT BULBS

1.003.00 3.00

----------

SUBTOTAL 3.00

TOTAL 634844.92

Total uncommitted balance from current and prior quarters: \$4734.20

End of report

Press RETURN to continue...

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option:

## FMS Transaction Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Funds Control Reports Menu from the Funds Control Menu.

Select FMS Transaction Data from the Funds Control Reports Menu.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option: FMS Transaction Data

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station number, a fiscal year and a fiscal quarter. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points. After printing the report, IFCAP will return to the Funds Control Reports Menu.

This report will generate a listing of FMS transactions

You may create the report for all entries,

or for selected year and/or quarter.

Enter fiscal year in the format '92'.

Select STATION NUMBER: 002//MYTOWN, PA

Select FISCAL YEAR: 94//

Select QUARTER: 4//

Select CONTROL POINT: 022 MISC OFFICE SUPPLIES//

DEVICE: HOME// LAT RIGHT MARGIN: 80//

FMS transaction total for this quarter: \$12.50

===============================================================================-

End of report

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Select Funds Control Reports Menu Option:

## Correct Sub-Control Point Amounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Funds Control Menu from the Control Point Clerk’s Menu.

Select Correct Sub-Control Point Amounts from the Funds Control Menu.

Enter a Station number and a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points.

Select Control Point Clerk’s Menu Option: Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option: Correct Sub-Control Point Amounts

Select STATION NUMBER: 999//ANYCITY,DC

Select CONTROL POINT: 121 LAB TESTING 121// ???

CHOOSE FROM:

22 022 MISC OFFICE SUPPLIES

40 040 BUILDING MANAGEMENT

73 073 ENGINEERING

112 112 SURGICAL SERVICE

114 114 RADIOLOGY SERVICE

121 121 LAB TESTING 121

170 170 REHAB. MEDICINE

7001 7001 SUPPLY FUND

Select CONTROL POINT: 121 LAB TESTING 121// 022 IFVENDOR2,FOUR

### Select Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a transaction number. If you do not know the transaction number, enter three question marks and IFCAP will list the available transactions. Enter additional Sub-Control Points to the Control Point if you like. At the \$ Amount: prompt, enter the amount that you would like to assign to this Sub-Control Point from the Control Point. Enter a caret (^) at the Select Station Number: prompt to return to the Funds Control Menu.

Select TRANSACTION NUMBER: ???

Attempting lookup in transaction file.

Attempting lookup using 999-94-4-022 (STA \# - FY - QTR - FCP)

1 999-94-4-022-0002 OBL IFVENDOR,FOUR LIGHT BULBS

2 999-94-4-022-0003 OBL IFVENDOR1,ONE

3 999-94-4-022-0004 OBL IFVENDOR2,FIVE

4 999-94-4-022-0005 OBL

5 999-94-4-022-0006 OBL

TYPE '^' TO STOP, OR

CHOOSE 1-5: 1

TRANSACTION BEG BAL: 3.00

Select SUB-CONTROL POINT: ???

This is an additional sub-control point. IFCAP allows more than one sub-control point on each transaction to get a quantity discount.

This is the name of the sub-control point.

Select SUB-CONTROL POINT: Reserve

ARE YOU ADDING 'Reserve' AS A NEW SUB-CONTROL POINT? Y (YES)

ARE YOU ADDING 'Reserve' AS A NEW SUB-CONTROL POINT (THE 1ST FOR THIS CONTROL

POINT ACTIVITY)? Y

(YES)

\$ AMOUNT: 2 RUNNING TOTAL: 2.00 BAL: 1.00

Select SUB-CONTROL POINT:

Select STATION NUMBER: ^

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu ...

Select Funds Control Menu Option:

## Supplementary Options in the Record Date Received by Service Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Single Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Record Date Received by Service Menu from the Control Point Clerk’s Menu.

Select Single Transaction from the Record Date Received by Service Menu.

Enter a Station Number. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points.

Select Control Point Clerk’s Menu Option: Record Date Received by Service Menu

Single Transaction

All Transactions with Final Partials

Select Record Date Received by Service Menu Option: Single Transaction

Select STATION NUMBER: 999//ANY CITY,DC

Select CONTROL POINT: 022 MISC OFFICE SUPPLIES//

### Select Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a transaction number. If you do not know the transaction number, enter three question marks and IFCAP will list the available transactions. Enter the date that the requestor received the goods or services at the Date Received: prompt. Press the Enter key at the Select Transaction or P.O. Number: prompt to return to the Record Date Received by Service Menu.

Select TRANSACTION or P.O. NUMBER: ???

Attempting lookup in transaction file.

Attempting lookup using 022 IFVENDOR2,FOUR (CONTROL POINT)

1022 IFVENDOR2,FOUR999-94-4-022-0011 OBL IFVENDOR2,FIVE CORN-CANNED-#10

2 022 IFVENDOR2,FOUR999-94-4-022-0010 OBL IFVENDOR2,FIVE CORN-CANNED-#10

3 022 IFVENDOR2,FOUR999-94-4-022-0008 OBL IFVENDOR,FOUR

4 022 IFVENDOR2,FOUR999-94-4-022-0009 OBL IFVENDOR1,ONE

This is where the "Description" goes.

5 022 IFVENDOR2,FOUR999-94-4-022-0006 OBL

TYPE '^' TO STOP, OR

CHOOSE 1-5: 1 999-94-4-022-0011

999-94-4-022-0011 P.O.:

DATE RECEIVED: T (JUL 09, 1994)

Select TRANSACTION or P.O. NUMBER:

Single Transaction

All Transactions with Final Partials

Select Record Date Received by Service Menu Option:

## All Transactions with Final Partials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Record Date Received by Service Menu from the Control Point Clerk’s Menu.

Select All Transactions with Final Partials from the Record Date Received by Service Menu.

Select Control Point Clerk’s Menu Option: Record Date Received by Service Menu

Single Transaction

All Transactions with Final Partials

Select Record Date Received by Service Menu Option: All Transactions with Final Partials

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station Number. Enter a Control Point. If you do not know the Control Point, enter three question marks at the prompt and IFCAP will list the available Control Points. IFCAP will record all the transactions in the Control Point as received and display \*\*\*LAST TRANSACTION\*\*\* when IFCAP is finished processing the changes. IFCAP will return to the Record Date Received by Service Menu.

Select STATION NUMBER: 999ANYCITY,DC

Select CONTROL POINT: 022 IFVENDOR2,FOUR

\*\*\*LAST TRANSACTION\*\*\*

Single Transaction

All Transactions with Final Partials

Select Record Date Received by Service Menu Option:

## Record Receipt of Multiple Delivery Schedule Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Record Receipt of Multiple Delivery Schedule Items from the Control Point Clerk's Menu. Enter a Control Point and a transaction number. If you do not know the transaction number, enter as much of the number as you can remember or enter three question marks, and IFCAP will list the available transaction numbers.

Process a Request Menu ...

Display Control Point Activity Menu ...

Funds Control Menu ...

Status of Requests Reports Menu ...

Record Date Received by Service Menu ...

Record Receipt of Multiple Delivery Schedule Items

Multiple Delivery Schedule List

Select Control Point Clerk's Menu Option: Record Receipt of Multiple Delivery Schedule Items

Select CONTROL POINT: 110 LAB TESTING 110

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ???

Attempting lookup in transaction file.

Attempting lookup using 110 LAB TESTING 110 (CONTROL POINT)

1 110 LAB TESTING 110 999-95-4-110-0055 CEIL Some description.

2 110 LAB TESTING 110 999-95-3-110-0054 CEIL Some description.

3 110 LAB TESTING 110 999-95-2-110-0053 CEIL 999FC0162 Some description.

4 110 LAB TESTING 110 999-95-1-110-0052 CEIL

Some description.

TYPE '^' TO STOP, OR

CHOOSE 1-5: 3

### Classification and Sort Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Classification of Request: prompt, create a classification name for the request if you like, or press the Enter key to skip this prompt. The Classification of Request: prompt allows you to create reports that group requests by categories that YOU define. Enter a sort group at the Sort Group: prompt if this purchase is assigned to a project, office, or some other category for which a sort group has been created. If this purchase does not belong to a sort group, just press the Enter key. Sort groups are used to generate expense reports for projects and offices. Enter today's date at the Date Received: prompt. Enter comments if you like. You may review the request if you like. You may enter another request or return to the Control Point Clerk's Menu.

CLASSIFICATION OF REQUEST: ABC

SORT GROUP:

TRANSACTION BEG BAL: 99999.00

Select SUB-CONTROL POINT:

DATE RECEIVED: T (JAN 09, 1995)

COMMENTS:

1\>Some description.

EDIT Option:

Would you like to review this request? NO// (NO)

Would you like to edit another request? YES// n (NO)

Process a Request Menu ...

Display Control Point Activity Menu ...

Funds Control Menu ...

Status of Requests Reports Menu ...

Record Date Received by Service Menu ...

Record Receipt of Multiple Delivery Schedule Items

Multiple Delivery Schedule List

Select Control Point Clerk's Menu Option:

## Multiple Delivery Schedule List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Multiple Delivery Schedule List from the Control Point Clerk's Menu. Enter a Control Point. Enter a transaction number. If you do not know the transaction number, enter as much of the number as you can remember, or enter three question marks, and IFCAP will list the available transactions. Enter an output device.

Process a Request Menu ...

Display Control Point Activity Menu ...

Funds Control Menu ...

Status of Requests Reports Menu ...

Record Date Received by Service Menu ...

Record Receipt of Multiple Delivery Schedule Items

Multiple Delivery Schedule List

Select Control Point Clerk's Menu Option: Multiple Delivery Schedule List

Select CONTROL POINT: 101 LAB TESTING 101//

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ???

Attempting lookup in transaction file.

Attempting lookup using 101 LAB TESTING 101 (CONTROL POINT)

1 101 LAB TESTING 101 999-94-4-101-0632 OBL IFVENDOR1,TWO

2 101 LAB TESTING 101 999-94-4-101-0403 OBL IFVENDOR1,THREE A41021 TEST ITEM \#13

3 101 LAB TESTING 101 KMN7 OBL IFVENDOR,SEVENTEST ITEM \#17

4 101 LAB TESTING 101 999-94-3-101-0159 OBL IFVENDOR,NINE A40579 TEST ITEM \#11

CHOOSE 1-4: 3 KMN7

DEVICE: ;;9999 LAT RIGHT MARGIN: 80//

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will print or display the 'Multiple Delivery Schedule List,' listing the transaction number, the item name, the schedule number, the quantity, the date received, and the delivery location. After printing or displaying the list, IFCAP will return to the Control Point Clerk's Menu.

MULTIPLE DELIVERY SCHEDULE LIST JAN 9,1995 09:04 PAGE 1

TRANS# ITEM# PR# ITEM QTY

SCH# QTY DATE DEL QTY DATE REC SCP LOCATION

--------------------------------------------------------------------------------

KMN7 \#1 17 1.00

TEST ITEM \#17

1 1 07/14/94 HERE

Process a Request Menu ...

Display Control Point Activity Menu ...

Funds Control Menu ...

Status of Requests Reports Menu ...

Record Date Received by Service Menu ...

Record Receipt of Multiple Delivery Schedule Items

Multiple Delivery Schedule List

Select Control Point Clerk's Menu Option:

# # Menu Outline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Option Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the options assigned to Control Point Clerks in the default IFCAP configuration. You may have some options that are not listed here, because you have additional responsibilities beyond the typical responsibilities of a Control Point Clerk. You may not have all of the options listed below. Main menu options are flush left. Subordinate options are spaced to the right. For example, if you wanted to use the “Copy a Transaction” option, you would select “Control Point Clerk's Menu”, then “Process a Request Menu”, then “Copy a Transaction”. To add any of the options listed below to your menus, contact your local Information Resources Management (IRM) service.

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

Control Point Clerk's Menu

Process a Request Menu

New 2237 (Service) Request

Edit a 2237 (Service)

Copy a Transaction

1358 Request Menu

New 1358 Request

Increase/Decrease Adjustment

Edit 1358 Request

Create/Edit Authorization

Daily Activity Enter/Edit

Display 1358 Balance

List Open 1358s

Print 1358

Print Obligated 1358s

Recalculate 1358 Balance

Print/Display Request Form

Change Existing Transaction Number

Repetitive Item List Menu

New Repetitive Item List (Enter)

Edit Repetitive Item List Entry

Delete Repetitive Item List Entry

Print/Display Repetitive Item List Entry

Generate Requests From Repetitive Item List Entry

Cancel Transaction with Permanent Number

Requestor's Menu

Enter a Request (Section)

Edit a Request (Section)

Delete a Request (Section)

New 1358 Request (Section)

Edit 1358 Request (Section)

Request Status Report (Section)

Print/Display Request Form (Section)

Copy a Transaction (Section)

Item History

Item Display

Vendor Display

Outstanding Approved Requests Report

Transaction Report - eCMS/IFCAP

Display Control Point Activity Menu

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

Funds Control Menu

Enter FCP Adjustment Data

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

Recalculate Fund Control Point Balance

Funds Control Reports Menu

Quarterly Report

Ceiling Report

Audit Transaction List

Sort Group Report

Classification of Request Report

Cost Center Totals

BOC Totals

Sub-Control Point Report

Reconciliation of PO/Sub-CP Dollar Amounts

BOC Detail Totals

FMS Transaction Data

Status of Requests Reports Menu

Print/Display Request Form

Status of All Obligation Transactions

Requests Ready for Approval List

PO with Associated Transactions

Record Date Received by Service Menu

Single Transaction

All Transactions with Final Partials

Record Receipt of Multiple Delivery Schedule Items

Multiple Delivery Schedule List

# Error Messages and Their Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Use Errors 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you use IFCAP to request goods and services, you will receive errors. Some errors are use errors. Use errors mean that IFCAP has determined that the information you have entered in the system is either incomplete or inconsistent, and look like this:

Select TRANSACTION: 10195

Incorrect format - please re-enter number

Select TRANSACTION:

This guide and the online option descriptions should help you with these errors.

## System Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System errors occur when IFCAP fails to function properly. IFCAP is written in a programming language called Digital Standard MUMPS. When errors occur, IFCAP will display the error code. Record the error code and notify your OIT staff.

RECORDING THAT AN ERROR OCCURRED ---

X2^PRCST212:1, %DSM-E-UNDEF, undefined variable PRCSTDT, -DSM-I-ECODE,

MUMPS error code: M6

Sorry 'bout that

### MailMan Error Messages – eCMS Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accountable Officer sends all 2237s that will be processed by Contracting staff to the electronic Contract Management System (eCMS) in Austin. The IFCAP application will reject any 2237 forwarded to eCMS with no Requesting Service (Requesting Service is blank (null)). The field is required for 2237s being sent to eCMS. The Accountable Officer will receive a MailMan message advising that the 2237 must be Returned to the Service for editing by the Control Point User. The CP user will need to edit the 2237 to populate the Requesting Service field and reapprove the 2237. The Accountable Officer will then be able to process the 2237 and send it to eCMS.

Example of this Error Message:

Subj: TRANSMISSION FAILURE FOR 2237 999-12-4-911-0022 \[#402930\] 08/07/12@11:59

8 lines

From: IFCAP TO ECMS INTERFACE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Return 2237 to Control Point for edit and re-approval!

STATION 999

2237 Transmission to eCMS failed Aug 07, 2012@11:59:46

999-12-4-911-0022

An error occurred when transmitting the 2237 transaction to eCMS.

Error: Field REQUESTING SERVICE is missing

Option: Process a Request in PPM

Enter message action (in IN basket): Ignore//

# GLOSSARY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term                    | Definition                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1358                    | VA Form 1358, Estimated Obligation or Change in Obligation.                                                                                                                                                                                                                                                                                                                                                                    |
| 2138                    | VA Form 90-2138, Order for Supplies or Services.                                                                                                                                                                                                                                                                                                                                                                               |
| 2139                    | VA Form 90-2139, Order for Supplies or Services (Continuation). This is a continuation sheet for the 2138 form.                                                                                                                                                                                                                                                                                                                |
| 2237                    | VA Form 90-2237, Request, Turn-in and Receipt for Property or Services.                                                                                                                                                                                                                                                                                                                                                        |
| A&MM                    | Acquisition and Material Management Service.                                                                                                                                                                                                                                                                                                                                                                                   |
| AACS                    | Automated Allotment Control System--Central computer system developed by VHA to disburse funding from VACO to field stations.                                                                                                                                                                                                                                                                                                  |
| Accounting Technician   | Fiscal employee responsible for obligation and payment of received goods and services.                                                                                                                                                                                                                                                                                                                                         |
| Activity Code           | The last two digits of the AACS number. It is defined by each station.                                                                                                                                                                                                                                                                                                                                                         |
| Allowance table         | Reference table in FMS that provides financial information at the level immediately above the AACS, or sub-allowance level.                                                                                                                                                                                                                                                                                                    |
| AMIS                    | Automated Management Information System.                                                                                                                                                                                                                                                                                                                                                                                       |
| AITC                    | Austin Information Technology Center hosts many different VA systems.                                                                                                                                                                                                                                                                                                                                                          |
| Authorization           | A charge to an obligated 1358. Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.                                                                                                                                                                                                         |
| Authorization Balance   | The amount of money remaining that can be authorized against the 1358. The service balance minus total authorizations.                                                                                                                                                                                                                                                                                                         |
| Budget Analyst          | Fiscal employee responsible for distributing and transferring funds.                                                                                                                                                                                                                                                                                                                                                           |
| Budget Object Code      | Fiscal accounting element that tells what kind of item or service is being procured. Budget object codes replace sub accounts in IFCAP 5.1. Budget object codes are listed in the left column of MP4 Part V, Appendix B-1.                                                                                                                                                                                                     |
| Ceiling Transactions    | Funding distributed from Fiscal Service to IFCAP Control Points for spending.                                                                                                                                                                                                                                                                                                                                                  |
| Control Point           | Financial element, existing ONLY in IFCAP that corresponds to the ACCS number in FMS.                                                                                                                                                                                                                                                                                                                                          |
| Control Point Requestor | The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. The users can only view or edit their own requests. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&MM.                                                                                                                                    |
| Cost Center             | “Subsection” of a Fund Control Point. Cost centers allow fiscal staff to create total expense reports for a section or service, and allow requestors to assign requests to that section or service. Cost centers are listed in the left column of MP-4 Part V, Appendix B-1.                                                                                                                                                   |
| Date Committed          | The date that you want IFCAP to commit funds to the purchase.                                                                                                                                                                                                                                                                                                                                                                  |
| Deficiency              | When a budget has obligated and expended more than it was funded (see MP-4, Part V Section C).                                                                                                                                                                                                                                                                                                                                 |
| eCMS                    | Electronic Contract Management System (eCMS) located at the Austin Information Technology Center (AITC).                                                                                                                                                                                                                                                                                                                       |
| Fiscal Balance          | The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidation submitted against the obligation.                                                                                                                                                                                                                                         |
| Fiscal Quarter          | The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.                                                                                                                                                                                                                                                                                                                        |
| Fiscal Year             | Twelve-month period from October 1 to September 30.                                                                                                                                                                                                                                                                                                                                                                            |
| FMS                     | Financial Management System, which has replaced CALM as the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides for flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting. |
| FOB                     | Freight on Board. An FOB of "Destination" means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of "Origin" means that shipping charges are due to the shipper, and must be paid when the shipper arrives at the warehouse with the item.                                                                          |
| FTEE                    | Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned an FTEE of 0.5, as would a full-time employee that worked for half of a year.                                                                                                                                 |
| Fund Control Point      | CALM accounting element that is not used by FMS.                                                                                                                                                                                                                                                                                                                                                                               |
| Justification           | A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source.                                                                                                                                                                                                                                         |
| ISMS                    | Integrated Supply Management System.                                                                                                                                                                                                                                                                                                                                                                                           |
| Liquidation             | The amount of money on the invoice from the vendor for the authorization. They are processed through payment/invoice tracking.                                                                                                                                                                                                                                                                                                 |
| OA&L                    | Office of Acquisitions and Logistics.                                                                                                                                                                                                                                                                                                                                                                                          |
| Obligation Number       | The C prefix number that Fiscal Service assigns to the 1358.                                                                                                                                                                                                                                                                                                                                                                   |
| Organization Code       | Accounting element functionally comparable to Cost Center, but used to organize purchases by the budget that funded them, not the purposes for spending the funds.                                                                                                                                                                                                                                                             |
| PAID                    | Paid Accounting Integrated Data.                                                                                                                                                                                                                                                                                                                                                                                               |
| Partial Date            | The date that a warehouse clerk created a receiving report for a shipment.                                                                                                                                                                                                                                                                                                                                                     |
| Program Code            | Accounting element that identifies the VA initiative or program that the purchase will support.                                                                                                                                                                                                                                                                                                                                |
| Purchase Order          | A government document authorizing the purchase of the goods or services at the terms indicated.                                                                                                                                                                                                                                                                                                                                |
| Purchasing Agents       | A&MM employees legally empowered to purchase goods and services from commercial vendors.                                                                                                                                                                                                                                                                                                                                       |
| Receiving Report        | Report that Warehouse Clerk creates to record that the warehouse has received an item.                                                                                                                                                                                                                                                                                                                                         |
| Requestor               | See “Control Point Requestor.”                                                                                                                                                                                                                                                                                                                                                                                                 |
| Requisition             | An order from a Government vendor.                                                                                                                                                                                                                                                                                                                                                                                             |
| Service Balance         | The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorizations created by the service.                                                                                                                                                                                                                |
| SF-18                   | Request for Quotation.                                                                                                                                                                                                                                                                                                                                                                                                         |
| SF-30                   | Amendment of Solicitation/Modification of Contract.                                                                                                                                                                                                                                                                                                                                                                            |
| Sort Order              | The order in which the budget categories will appear on the budget distribution reports.                                                                                                                                                                                                                                                                                                                                       |
| Sub-cost Center         | A subcategory of Cost Center. In IFCAP 5.1, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.                                                          |
| Sub-control Point       | A specific budget within a Control Point, defined by a Control Point user.                                                                                                                                                                                                                                                                                                                                                     |
| TDA                     | Transfer of Disbursing Authority. A sequential number Central Office assigns to each funding it gives to your station. The first funding they give you in the fiscal year is TDA number 1, the second funding they give you is TDA number 2, etc.                                                                                                                                                                              |
| Total Authorizations    | The total amount of the authorizations created for the 1358 obligation.                                                                                                                                                                                                                                                                                                                                                        |
| Total Liquidations      | The total amount of the liquidation against the 1358 obligation.                                                                                                                                                                                                                                                                                                                                                               |
| Transaction Number      | The number of the transaction that funded a Control Point (See Budget Analyst User's Guide)                                                                                                                                                                                                                                                                                                                                    |
| Vendor file             | An IFCAP file of vendors solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. File 440 contains information about the vendors solicited by your station. The debtor's address may be drawn from this file, but is maintained separately. If the desired vendor is not in the file, contact A&MM Service to have it added.               |
| VRQ                     | FMS Vendor Request document. When users in IFCAP create a new Vendor record or edit an existing record a VRQ message is sent to the FMS system at the AITC.                                                                                                                                                                                                                                                                    |
| VUP                     | Vendor Update document. FMS responds to a VRQ by sending a VUP message back to IFCAP. The VUP contains the FMS vendor information ( i.e. Address data, FMS Code and Alternate-Address-Indicator), ensuring that the information in the IFCAP vendor file matches the information in the FMS vendor table.                                                                                                                      |

# INDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1358 1
1358 Balance 99, 102, 104
2237 1, 2, 57, 59
A&MM i, 2, 7, 46
Accounting Technician 99
Audit Transaction List 143
BOC Detail Totals 154, 155
BOC Totals 150
Budget Object Code (BOC) 14, 20, 25, 30, 34, 42, 79, 88, 92, 95, 135, 136, 150, 154, 155
Cancel Transaction with Permanent Number i, 65
Ceiling Report 142
Change Existing Transaction Number 37, 40
Classification of Request Report 146
Copy a Transaction 77
Cost Center Totals 149
Create/Edit Authorization 96
Daily Activity Enter/Edit 100
Date Committed 34, 88, 95
Delete Repetitive Item List Entry 75
Display 1358 Balance 104
Edit 1358 Request 93
Edit a 2237 (Service) 57
Edit Repetitive Item List Entry 69
Enter FCP Adjustment Data 134
Fiscal Quarter 27, 41
Fiscal Year 21, 27, 41, 48, 133, 140, 142, 144
FMS 13, 18, 23, 30, 34, 157
FMS Transaction Data 3, 157
Generate Requests From Repetitive Item List Entry 73
Increase/Decrease Adjustment 90
Item Display 80
Item History 131, 132
Justification 15, 20, 25, 30, 80
List Open 1358s 106
Multiple Delivery Schedule List 163
New 1358 Request 31, 84
New Repetitive Item List (Enter) 67
Obligation Number 91
Outstanding Approved Requests Report 112
PO with Associated Transactions 120
PPM Status of Transactions Report 132
Print 1358 49, 107
Print Obligated 1358s 111
Print/Display Repetitive Item List Entry 71
Print/Display Request Form 58, 59, 117
Purchase Order 2, 45, 46, 48, 123
Purchase Order Status 45, 123
Quarterly Report 140
Recalculate 1358 Balance 102
Recalculate Fund Control Point Balance 138
Record Date Received by Service Menu 3, 159, 160, 161
Record Receipt of Multiple Delivery Schedule Items 161
Requests Ready for Approval List 122
Running Balances 128
Single Transaction 160
Sort Group Report 145
Status of All Obligation Transactions 119
Temporary Transaction Listing 124, 125
Transaction Number 37, 39, 40, 41, 46, 57, 61, 65
Transaction Status Report 46, 126, 133
Vendor Display 83
