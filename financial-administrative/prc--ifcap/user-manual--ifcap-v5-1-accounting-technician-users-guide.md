---
title: IFCAP Version.5.1 Accounting Technician User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Accounting Technician User's Guide
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
menu_options: 2
description: 
audience: 
keywords: 
  - class
  - table
  - contents
  - number
  - vendor
  - order
  - document
  - purchase
  - date
  - even
page_count: 0
word_count: 32222
section_count: 56
table_count: 17
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1accounting_tech.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1accounting_tech.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP)Version 5.1Accounting TechnicianUser’s Guide

![](ifcap-version-5-1-accounting-technician-user-s-guide/001.png)

March 2026Department of Veterans AffairsOffice of Information and Technology (OI&T)Management, Enrollment, and Financial Systems

Revision History

Initiated 12/29/04

<table>
<caption><p><span id="_Toc166316025" class="anchor"></span>Table 1: Icons Used in Boxed Notes</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 44%" />
<col style="width: 24%" />
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
<td>03/2026</td>
<td>15.0</td>
<td><p>Updates based on patch PRC*5.1*257.</p>
<blockquote>
<p>This manual has been updated to comply with the VA OIT-mandated user guide template.</p>
</blockquote></td>
<td><p>Technical Writer,</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="even">
<td>09/2025</td>
<td>14.0</td>
<td><blockquote>
<p>The PRCHL GUI Logistics Data Query Tool option has been marked Out of Order with patch PRC*5.1*247</p>
</blockquote></td>
<td><p>Technical Writer,</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="odd">
<td>9/2022</td>
<td>14.0</td>
<td><p>PRC*5.1*227:</p>
<ul>
<li><p>Updated Figure 10-3 in Section 10.4.1 with UEI field</p></li>
<li><p>Updated Figure 10-9 and Figure 10-10 in Section 10.10 with UEI field</p></li>
</ul></td>
<td><p>SQA Analyst,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>07/2021</td>
<td>13.0</td>
<td><blockquote>
<p>Patch PRC*5.1*223</p>
</blockquote>
<p>13-2 - Changed the option Queue Single Receiving Report for Transmission with the following message:</p>
<p>“&gt; Out of order: No longer available, partial filing non-compliant”</p></td>
<td><p>SQA Analyst,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>10/2019</td>
<td>12.0</td>
<td><blockquote>
<p>Reviewed document; made minor formatting changes</p>
</blockquote></td>
<td><p>PMO Program Analyst,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>10/2017</td>
<td>11.0</td>
<td><blockquote>
<p>Patch PRC*5.1*198 (NIF/IFCAP IMF Interface Enhancement)</p>
<p>Section 10.4 Vendor File Edit, added “In order to edit the VENDOR NAME and PAYMENT ADDRESS fields for a Medical/Surgical Prime (MSPV) Vendor (vendor numbers above 949,999), the Fiscal user must hold the PRCHVEN security key.”</p>
<p>Updated footers with current revision date.</p>
<p>Added “MSPV” to the Glossary</p>
</blockquote></td>
<td><p>IMF/IFCAP Developer, Functional Analyst, PMO Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>01/2014</td>
<td>10.0</td>
<td><blockquote>
<p>Patch PRC*5.1*174 (IFCAP/eCMS Interface)</p>
</blockquote>
<p>10.12 – Added the name of security key to the following sentence, “This option is available to Fiscal users who have the PRCHJFIS Security Key”</p>
<p>10.12 – Added new Transaction Report –eCMS/IFCAP option to Accounting Utilities Menu.</p>
<p>10.12.1 – Added “<strong>Note</strong>: At the DEVICE: HOME// prompt, the report can either be displayed to the screen or sent to a printer. The latter choice is appropriate when the report is long.”</p>
<p>13 – Added Transaction Report – eCMS/IFCAP to Menu Outline.</p></td>
<td><p>Project Manager</p>
<p>Subject matter Expert, Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>02/2013</td>
<td>9.0</td>
<td>Patch PRC*5.1*161 query user for if they wish to view the 1358 details. See pages 4-1, 4-2.</td>
<td><p>Project Manager, Tech Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>01/2013</td>
<td>8.0</td>
<td><p>As of Patch PRC*5.1*162, completion of a payment batch using the Finalize a Batch option in VistA Fee Basis will automatically generate a new transaction that is sent to Central Fee. This new transaction will replace all use of 994 code sheets in IFCAP.</p>
<p>The Fee Basis - IFCAP Code Sheet Menu [PRC FEE GECS MAIN MENU] and all associated options were removed from the Accounting Technician Menu [PRCFA ACCTG TECH] as this functionality is no longer necessary.</p></td>
<td><p>Project Manager, Subject Matter Expert</p>
<p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>09/2012</td>
<td>7.5</td>
<td>Patch PRC*5.1*167 Updates (eCMS Interface to IFCAP): added eCMS term to the Glossary</td>
<td><p>Project Manager, Technical Writer,</p>
<p>Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>10/2011</td>
<td>7.0</td>
<td>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358. See pages 3-1, 4-13, 13-1.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>08/2011</td>
<td>6.0</td>
<td>Remedy Ticket HD512314 make option lists complete. See page 8-7 to 8-8.</td>
<td><p>Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>07/2011</td>
<td>5.0</td>
<td>Patch PRC*5.1*153 – New message interface with Austin for 1358 Obligations see pp. 4-5, 4-10.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>01/05/2011</td>
<td>4.0</td>
<td>Changes to the manual based on implementation of the Segregation of Duties functionality, per patch PRC*5.1*148. Includes the removal of the Obligation Data option.</td>
<td><p>Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>05/31/07</td>
<td>3.0</td>
<td>Added information covering the use of the Logistics Data Query Tool (LDQT), per patch PRC*5.1*103.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>02/06/06</td>
<td>2.0</td>
<td>Added New option, Print Obligated 1358s, per patch PRC*5.1*79.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>12/29/04</td>
<td>1.1</td>
<td>PDF file checked for accessibility to readers with disabilities.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>12/29/04</td>
<td>1.0</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
</tbody>
</table>

<span id="_Toc166316025" class="anchor"></span>Table 1: Icons Used in Boxed Notes

########### Preface

This manual is designed to provide you, the Accounting Technician, with the information necessary to obligate purchase orders and 1358s, process receiving reports, amendments, and adjustment vouchers, make General Post Fund transactions, and track invoices for payment into the Financial Management System (FMS). The Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) package automates functions in Acquisition and Materiel Management (A&MM), Fiscal and for all VA Services that request supplies and services. The goal of IFCAP is to integrate these three areas and allow users to share procurement and financial information.

Table Of Contents

Figures

Tables

[Table 1: Icons Used in Boxed Notes [4](#_Toc166316025)](#_Toc166316025)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [The Role of the Accounting Technician](#the-role-of-the-accounting-technician)
  - [How to Use This Guide](#how-to-use-this-guide)
    - [Hypertext and Hyperlinks](#hypertext-and-hyperlinks)
    - [Procedure Steps](#procedure-steps)
    - [Typographical Conventions](#typographical-conventions)
  - [Package Management, Legal Requirements and Security Measures](#package-management-legal-requirements-and-security-measures)
  - [Package Operation](#package-operation)
  - [Funds Obligation Flowchart](#funds-obligation-flowchart)
- [Inspect Purchase Orders and Requisitions](#inspect-purchase-orders-and-requisitions)
  - [Introduction](#introduction-1)
  - [Purchase Order Number](#purchase-order-number)
  - [Invoice Address](#invoice-address)
  - [Cost Center](#cost-center)
  - [Fiscal Source Code](#fiscal-source-code)
  - [Budget Object Code](#budget-object-code)
- [Obligating and Amending Purchase Orders](#obligating-and-amending-purchase-orders)
  - [Introduction](#introduction-2)
  - [Is there Adequate Funding for the Purchase Order?](#is-there-adequate-funding-for-the-purchase-order)
  - [Obligating a Purchase Order](#obligating-a-purchase-order)
    - [Menu Path](#menu-path)
    - [Select Order Number](#select-order-number)
    - [Display Order Information](#display-order-information)
    - [Obligation Date](#obligation-date)
    - [Post Using Status of Funds Tracker](#post-using-status-of-funds-tracker)
    - [Enter Transaction Amount](#enter-transaction-amount)
  - [Amending a Purchase Order](#amending-a-purchase-order)
    - [Is There Adequate Funding for the Amendment?](#is-there-adequate-funding-for-the-amendment)
    - [Obligate an Amendment](#obligate-an-amendment)
- [Obligating and Adjusting 1358 Transactions](#obligating-and-adjusting-1358-transactions)
  - [Inspect the 1358 for Correctness](#inspect-the-1358-for-correctness)
  - [Is There Adequate Funding for the 1358?](#is-there-adequate-funding-for-the-1358)
  - [Obligate 1358](#obligate-1358)
    - [Menu Path](#menu-path-1)
    - [Enter Station Number](#enter-station-number)
    - [Review Balances](#review-balances)
    - [Enter Obligation Number](#enter-obligation-number)
    - [Enforcing Segregation of Duties on 1358s](#enforcing-segregation-of-duties-on-1358s)
- [Enforcing Segregation of Duties in Online Certification System for 1358 Obligation](#enforcing-segregation-of-duties-in-online-certification-system-for-1358-obligation)
  - [Adjustments to 1358s](#adjustments-to-1358s)
    - [Introduction](#introduction-3)
    - [Inspect the Adjustment for Correctness](#inspect-the-adjustment-for-correctness)
    - [Is There Adequate Funding for the Adjustment?](#is-there-adequate-funding-for-the-adjustment)
    - [Adjust the 1358](#adjust-the-1358)
    - [Enforcing Segregation of Duties on 1358 Adjustments](#enforcing-segregation-of-duties-on-1358-adjustments)
    - [Enforcing Segregation of Duties in Online Certification System for 1358 Adjustments](#enforcing-segregation-of-duties-in-online-certification-system-for-1358-adjustments)
  - [Display or Print Obligated 1358s](#display-or-print-obligated-1358s)
  - [Display/Print 1358](#displayprint-1358)
- [Review and Forward Receiving Reports for Payment](#review-and-forward-receiving-reports-for-payment)
  - [Introduction](#introduction-4)
  - [Dollar Amounts](#dollar-amounts)
    - [Menu Path](#menu-path-2)
    - [Review Order](#review-order)
    - [Review Receiving Report](#review-receiving-report)
- [Process 1358 Invoices for Payment](#process-1358-invoices-for-payment)
  - [Introduction](#introduction-5)
  - [Menu Path](#menu-path-3)
    - [Select Station Number](#select-station-number)
    - [Assign Liquidation Number](#assign-liquidation-number)
    - [Select Budget Object Code](#select-budget-object-code)
  - [Verifying Payment Transmission](#verifying-payment-transmission)
    - [Menu Path](#menu-path-4)
    - [Enter and Verify Transmission](#enter-and-verify-transmission)
- [Resolving Error Messages](#resolving-error-messages)
  - [FMS Error Processing](#fms-error-processing)
  - [Stack Status Report](#stack-status-report)
  - [FMS Inquiry Rejected Obligation Documents Menu](#fms-inquiry-rejected-obligation-documents-menu)
  - [Payment Error Processing](#payment-error-processing)
- [# Purchase Card Options](#purchase-card-options)
  - [Purchase Card Transaction Print Menu](#purchase-card-transaction-print-menu)
  - [Detailed Report of Unpaid PC Transactions by FCP](#detailed-report-of-unpaid-pc-transactions-by-fcp)
    - [Enter Parameters and Display](#enter-parameters-and-display)
  - [Fiscal Daily Review](#fiscal-daily-review)
    - [Enter Parameters and Display](#enter-parameters-and-display-1)
  - [History of Purchase Card Transactions](#history-of-purchase-card-transactions)
    - [Enter Parameters and Display](#enter-parameters-and-display-2)
  - [Reconciled Purchase Card Transactions](#reconciled-purchase-card-transactions)
    - [Enter Parameters and Display](#enter-parameters-and-display-3)
  - [Unreconciled Purchase Card Transactions](#unreconciled-purchase-card-transactions)
    - [Enter Parameters and Display](#enter-parameters-and-display-4)
  - [ET-FMS Document Display](#et-fms-document-display)
    - [Enter Parameters and Display](#enter-parameters-and-display-5)
  - [ET-FMS Document Rebuild](#et-fms-document-rebuild)
  - [Purchase Card Transaction Status](#purchase-card-transaction-status)
    - [Enter Parameters and Display](#enter-parameters-and-display-6)
  - [Monitor Reconciled Orders by Card Holder](#monitor-reconciled-orders-by-card-holder)
    - [Enter Parameters and Display](#enter-parameters-and-display-7)
  - [BOC Report for OA&MM/Fiscal](#boc-report-for-oammfiscal)
    - [Enter Parameters and Display](#enter-parameters-and-display-8)
- [Accounting Utilities](#accounting-utilities)
  - [Introduction](#introduction-6)
  - [Update Status of Funds Balances](#update-status-of-funds-balances)
    - [Enter Parameters and Display](#enter-parameters-and-display-9)
  - [Lookup Vendor ID Number](#lookup-vendor-id-number)
    - [Enter Parameters and Display](#enter-parameters-and-display-10)
  - [Vendor File Edit](#vendor-file-edit)
    - [Enter Parameters and Display](#enter-parameters-and-display-11)
  - [Edit BOC in Item File](#edit-boc-in-item-file)
    - [Enter Parameters and Display](#enter-parameters-and-display-12)
  - [Clear Program Lock](#clear-program-lock)
    - [Enter Parameters and Display](#enter-parameters-and-display-13)
  - [Undelivered Orders Reconciliation Report](#undelivered-orders-reconciliation-report)
    - [Enter Parameters and Display](#enter-parameters-and-display-14)
  - [Fiscal Pending Action](#fiscal-pending-action)
    - [Enter Parameters and Display](#enter-parameters-and-display-15)
  - [History - Code Sheet/Obligation (PAT) Number](#history-code-sheetobligation-pat-number)
    - [Enter Parameters and Display](#enter-parameters-and-display-16)
  - [Review Vendor Request](#review-vendor-request)
    - [Enter Parameters and Display](#enter-parameters-and-display-17)
  - [Setup Accounts Receivable Selected Vendor](#setup-accounts-receivable-selected-vendor)
    - [Enter Parameters and Display](#enter-parameters-and-display-18)
  - [Transaction Report – eCMS/IFCAP](#transaction-report-ecmsifcap)
    - [Enter Parameters and Display](#enter-parameters-and-display-19)
- [FMS Code Sheet Menu](#fms-code-sheet-menu)
  - [Introduction](#introduction-7)
  - [Menu Choices](#menu-choices)
    - [Transmission Records/Code Sheets](#transmission-recordscode-sheets)
    - [Enter Parameters and Display](#enter-parameters-and-display-20)
    - [Retransmit Stack File Document](#retransmit-stack-file-document)
    - [User Comments](#user-comments)
- [# The Logistics Data Query Tool](#the-logistics-data-query-tool)
- [Menu Outline](#menu-outline)
- [Glossary](#glossary)
- [Index](#index)

## The Role of the Accounting Technician

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As an Accounting Technician, you have an important role in the way the Department of Veterans Affairs manages its finances. Accounting Technicians control, coordinate and direct a variety of financial documents and reports and ensure their timely, accurate disposition. Accounting Technicians inspect purchase orders and requisitions, obligate and amend transactions of funds, and review and forward invoices and receiving reports for payment. Accounting Technicians rely on Control Point Officials and Purchasing Agents to provide accurate information about the obligations that the Accounting Technician charges to the Control Point. They also rely on the Warehouse Clerks to process receiving reports quickly and accurately, and the Purchasing Agents and Requisition Clerks to process amendments and adjustment vouchers quickly and accurately. Vendors rely on the Accounting Technician to make sure that the receiving reports are promptly transmitted for payment and that certified invoices are processed according to the Prompt Payment Act.

## How to Use This Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide explains how to perform the role of the Accounting Technician by dividing that role into small, manageable tasks. The authors of this guide have listed these tasks in successive order so that each instruction builds on the functionality and information from the previous instructions. This will allow new Accounting Technicians to use this guide as a tutorial by following the instructions from beginning to end. Experienced Accounting Technicians can use this guide as a reference tool by using the index and table of contents.

Before you plunge into learning about your job as Accounting Technician, please take a few moments to familiarize yourself with how this guide is put together.

1.  Read all of Section 1. It explains how to interpret the graphics and typestyles used in this guide.
2.  If this is your first exposure to using VistA, you should become familiar with terminology and functions that are used throughout VistA applications. There are several manuals and guides that provide a foundation for use of *Kernel*, *FileMan*, and *MailMan*. These documents replace the old *DHCP User’s Guide to Computing*, which is obsolete. You will find these at:

> *Kernel:* [VA Software Document Library – Kernel](https://www.va.gov/vdl/application.asp?appid=10)

> *FileMan:* [VA Software Document Library - FileMan](https://www.va.gov/vdl/application.asp?appid=5)

> *MailMan:* [VA Software Document Library - MailMan](https://www.va.gov/vdl/application.asp?appid=15)

3.  Read the remainder of this guide.

### Hypertext and Hyperlinks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document contains hypertext that provides links to other parts of this document or to other related documents. *Hypertext* is a computer-based text retrieval system that enables you to access particular locations in electronic documents by clicking on *hyperlinks* in those documents. If you are viewing this document on your computer screen (as opposed to reading a printed copy), you will find certain hyperlinked words or phrases.

- An internal or “cross-reference” hyperlink allows you to “jump” to another part of this document. Typically, these hyperlinks will be imbedded in sentences like “See the IFCAP Glossary in 14.” Although such internal cross-references may not be shown in blue, if you move your mouse over such phrases, a pop-up box will display the link, like this:

<span id="_Toc222493031" class="anchor"></span>Figure 1: Example of Internal Link

![](ifcap-version-5-1-accounting-technician-user-s-guide/002.png)

If you have the Web toolbar enabled in your copy of Word, just click the back ![](ifcap-version-5-1-accounting-technician-user-s-guide/003.png) icon on the toolbar to return to where you jumped from.

- Another kind of internal hyperlink uses “bookmarks” to direct you to other locations in this document. These are normally presented in a blue font. Again, click the back icon on the toolbar to return to the point where you jumped from.

Links to web pages or Internet sites should open in your web browser (typically *Internet Explorer*®). Use the browser’s “back” button to return to this document. Since *Internet Explorer* and *Word* are both Microsoft products, do *not* close the browser window, since this may (under certain circumstances) also close this document.

- Links to some external documents (for example, other Word documents) may (depending on your system settings) open in Word. Such links are also usually presented in a blue font. For example, note the shortcut graphic with blue hyperlink to the other online documents shown in the boxed note below. Use the back icon on the menu bar to return to where you jumped from.

In either case, you may click (or, depending on your computer’s operating system or software version, you may have to hold down the \<Ctrl\> key while clicking) on the link to see the other document or move to the specified place in this document.

### Procedure Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Procedures that you perform in an exact order will list the steps involved. Look for Step numbers as in the following samples:
1.  Select the FMS Exception option.
2.  Enter the latest date that you want to retain entries. IFCAP will delete all entries recorded before that retention date.
- There are also paragraphs that simply discuss a process. In these instances, you do not need to perform any process discussed using a particular order.

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
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Icon</strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](ifcap-version-5-1-accounting-technician-user-s-guide/004.png)</td>
<td><strong>Warning</strong>: Something that could adversely affect your use of the Query Tool or of the material available in the IFCAP databases.</td>
</tr>
<tr class="even">
<td>![](ifcap-version-5-1-accounting-technician-user-s-guide/005.png)</td>
<td><strong>Tip</strong>: Advice on how to more easily navigate or use the Guide or the software.</td>
</tr>
<tr class="odd">
<td>![](ifcap-version-5-1-accounting-technician-user-s-guide/006.png)</td>
<td><strong>Information</strong>: or <strong>Note:</strong> Additional information that might be helpful to you or something you need to know about, but which is not critical to understanding or use of the software.</td>
</tr>
<tr class="even">
<td>![](ifcap-version-5-1-accounting-technician-user-s-guide/007.png)</td>
<td><strong>Technical Note:</strong> Information primarily of interest to software developers, IRM or Enterprise VistA Support (EVS) personnel. Most users can usually safely ignore such notes.</td>
</tr>
<tr class="odd">
<td><p>![](ifcap-version-5-1-accounting-technician-user-s-guide/008.png)</p>
<p>![](ifcap-version-5-1-accounting-technician-user-s-guide/009.png)</p></td>
<td><strong>Question:</strong> A question that might come to your mind (hopefully, followed by an <strong>Answer</strong>!)</td>
</tr>
</tbody>
</table>

FileMan Date Conventions

Throughout the guide, *FileMan* date conventions have been used. A date-valued response can be entered in a variety of ways. The following is a typical help prompt for a date field:

Examples of Valid Dates:

JAN 20, 1957, or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses CURRENT YEAR. Two-digit year

assumes no more than 20 years in the future, or 80 years in the past.

> **NOTE:** If you do not specify the year when you enter a date, IFCAP will assume that you are referring to the current calendar year. This could cause some confusion around the fiscal year turnover period when you are more likely to be entering dates for next year (when the current Fiscal Year is the same as the next Calendar Year).

## Package Management, Legal Requirements and Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only authorized Control Point users are able to enter, edit, or view requests or any other information for a particular Control Point. This is a security measure that prevents users from altering the requests of others. Due to the nature of the information being processed by IFCAP, special attention has been paid to limiting usage to authorized individuals. Individuals in the system who have authority to approve actions, at whatever level, have an electronic signature code. This code is required before the documents pass on to a new level for processing or review. Like the access and verify codes used when gaining access to the system, the electronic signature code will not be visible on the terminal screen. These codes are also encrypted so that they are unreadable even when viewed in the user file by those with the highest levels of access. Electronic signature codes are required by IFCAP at every level that currently requires a signature on paper.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP automates fiscal, budgetary, procurement, inventory, invoice tracking and payment activities. To accomplish all of these tasks, IFCAP consists of several functional components, each responsible for a similar set of tasks:

- Funds Distribution (Fiscal Component)
- Funds Control (Control Point Component)
- Processing Requests (Control Point Component)
- Purchase Orders/Requisitions (A&MM Component)
- Accounting (Fiscal Component)
- Receiving (A&MM Component)
- Inventory (A&MM/Control Point Component)

Different kinds of IFCAP users have different menus. If the menus in this manual include options that you do not see on your screen, do not panic! The instructions in this manual only use the options that you have as an Accounting Technician. If you do not know what to enter at an IFCAP prompt, enter one, two, or three question marks and IFCAP will list your available options or explain the prompt. The more question marks you enter at the prompt, the more information IFCAP will provide.

The options you use on IFCAP have been divided into groups based upon the type of work you do. When you select these options, IFCAP will ask you a series of questions. If you do not understand the question or are unsure of how to respond, enter a question mark (?) and the computer will explain the question, or allow you to choose from a list of responses.

The main menu for the Accounting Technician contains these sub-menus:

- Accounting Utilities Menu - This menu allows you to edit vendor files, clear a program lock, and review undelivered orders and reports.
- Document Processing Menu - This menu allows you to correct errors, and inspect, forward, or return obligations, receiving reports, amendments, purchase orders, and service orders.
- FMSCode Sheet Menu - This menu allows you to create, edit, delete, and review manual code sheets, and determine the status of transmission stacks.
- Receiving Report Transmission Menu - This menu allows you to change the transmission date of a queued receiving report, retransmit a receiving report, and delete a report from the transmission queue.
- Reprint Menu - This menu allows you to print receiving reports, purchase orders, and service orders.

## Funds Obligation Flowchart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ifcap-version-5-1-accounting-technician-user-s-guide/010.png)![](ifcap-version-5-1-accounting-technician-user-s-guide/011.png)

# Inspect Purchase Orders and Requisitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter explains how to inspect purchase orders and requisitions before obligating funds for purchase from the Control Point.

## Purchase Order Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Does the purchase order number follow the correct numbering system? If it does not, return the purchase order or requisition to Acquisition and Material Management (A&MM). Call the contracting officer listed on the purchase order or requisition and advise that the purchase order number is incorrect.

## Invoice Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Does the address in IFCAP in the Mail Invoice To: field correspond to the method of payment? If not, return the purchase order or requisition to Acquisition and Material Management (A&MM). Call the contracting officer listed on the purchase order or requisition and inform them that the invoice address is incorrect. All certified purchase orders should list Fiscal Service in the Mail Invoice To: field.

## Cost Center

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Compare the cost center to the requesting service. The cost center should agree in some way or other to the function of the service, for example, 822400 would be a valid cost center for Pharmacy Service. If the Cost Center is wrong, you can change it by following these three steps:

1.  From the Accounting Technician Menu, select Document Processing Menu.
2.  From the Document Processing Menu, select Obligation Processing.
3.  Enter the purchase order number. When IFCAP asks if the information on the purchase order is correct, answer “N” and enter the correct cost center. At the Should the Cost Center or BOC Information Be Edited at This Time? prompt, answer “Y”. Change the cost center.

You may also return the purchase order or requisition to the Purchasing Agent. The Purchasing Agent can return it to the Control Point for correction. If the service continues to send purchase orders or requisitions with an incorrect cost center, ask the Budget Analyst to review the list of available cost centers for the Control Point.

## Fiscal Source Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Compare the fiscal source code to the vendor. The vendor should have the correct fiscal source code. If not, return the purchase order or requisition to Fiscal Service or A&MM. If the service continues to send purchase orders or requisitions with an incorrect source code, ask the Purchasing Agent in A&MM to change the source code for the vendor.

## Budget Object Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Compare the Budget Object Code (BOC) number on the purchase order or requisition to the transaction code descriptions in VA HANDBOOK 4671.2.

The BOC should match the budget object code descriptions. If not, you can change it by following these three steps:

1.  From the Accounting Technician Menu), select Document Processing Menu.
2.  From the Document Processing Menu, select Obligation Processing.
3.  Enter the purchase order number. When IFCAP asks if the information on the purchase order is correct, answer “N” and enter the correct BOC.

You may also return the purchase order or the requisition to A&MM Service for return to the service. If the service continues to send purchase orders or requisitions with an incorrect budget object code, ask the Budget Analyst to change the list of available budget object codes for the Control Point.

# Obligating and Amending Purchase Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purchase orders are orders to a vendor to deliver items. The 2138 has a receipt date and a single, private vendor. This is different from the 1358 Obligation forms, which are for services.

## Is there Adequate Funding for the Purchase Order?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control Points cannot process a request if the request exceeds the amount of their allotted funds. At the end of a fiscal year, some Control Points are given the authority to over-commit funds so that they can obtain bids or quotes for next year's purchases. You should receive a daily report from the Austin Finance Center called the *Status of Allowance Report*, listing the funds available for each Control Point. Check this document closely for availability of funds, especially at the end of the fiscal year.

## Obligating a Purchase Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Accounting Technician’s Menu, select Document Processing Menu. From the Document Processing Menu, select Obligation Processing.

<span id="_Toc222493032" class="anchor"></span>Figure 2: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Document Processing Menu ...</p>
<p>Accounting Utilities Menu ...</p>
<p>Reprint Menu ...</p>
<p>Receiving Report Transmission Menu ...</p>
<p>FMS Code Sheet Menu ...</p>
<p>IRS Offset Code Sheet Menu ...</p>
<p>Print Obligated 1358s</p>
<p>Purchase Card Transactions Print Menu ...</p>
<p>Select Accounting Technician Menu Option: Document Processing Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1358 Processing Menu ...</p>
<p>Amendment Processing</p>
<p>General Post Funds Requests Processing</p>
<p>Invoice Processing (ACCTG) Menu ...</p>
<p>Obligation Processing</p>
<p>Process Receiving Report</p>
<p>Return Purchase Order to Supply</p>
<p>Return PO Amendment to Supply</p>
<p>FMS Rejected Obligation Document Processing ...</p>
<p>Select Document Processing Menu Option: Obligation Processing</p></td>
</tr>
</tbody>
</table>

### Select Order Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a STATION NUMBER and a PURCHASE Order Number at the appropriate prompts. If you do not know the Purchase Order Point, enter three question marks (???) at the prompt and IFCAP will display the available orders.

<span id="_Toc222493033" class="anchor"></span>Figure 3: Select Order Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select Purchase Order Number: ???</td>
</tr>
<tr class="even">
<td><p>Choose from:</p>
<p>U00001 688-U00001 02-23-00 ST Pending Fiscal Action</p>
<p>FCP: 081 $ 106.20</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Select Purchase Order Number: UOOOO1 688-U00001 02-23-00 ST Pending Fiscal Action</p>
<p>FCP: 081 $ 106.20</p></td>
</tr>
</tbody>
</table>

### Display Order Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the purchase order and ask if the Control Point and cost center information are correct. If not, answer N to edit the information. Otherwise, enter “Y”. IFCAP will display the cost of the order and its effect on the uncommitted and un-obligated balances of the Control Point. IFCAP will also display the status of funds balance for the Control Point. The status of funds balance is the funds available to the Control Point at the time the purchase order is being obligated. If the un-obligated balance is greater than the net cost of the order, then you can obligate the order. Otherwise, return the order to the Purchasing Agent or Requisition Clerk.

<span id="_Toc222493034" class="anchor"></span>Figure 4: Display Order Information

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Obligation Processing</p>
<p>Purchase Order - 688-U00001</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>COST CENTER: 828100 CONTROL POINT: 081 SPD</p>
<p>BOC: 2660 AMOUNT: $ 106.20</p>
<p>Net Cost of Order: $ 106.20</p>
<p>Justification(s):</p>
<p>No Justification Information shown.</p>
<p>The information listed above is recorded on this Purchase Order.</p></td>
</tr>
<tr class="even">
<td>Is the above information correct? YES//</td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Net Cost of Order: $ 106.20</p>
<p>Control Point Balances</p>
<p>Uncommitted Balance: $ 299992.80</p>
<p>Unobligated Balance: $ 300000.00</p>
<p>Committed, Not Obligated: $ 7.20</p>
<p>OK to Continue? YES//</p>
<p>Would you like to review the entire Purchase Order? YES//</p></td>
</tr>
</tbody>
</table>

### Obligation Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date the purchase order is obligated at the Select Obligation Processing Date: prompt. This date determines the accounting period, fiscal quarter, etc., of the purchase order for FMS records. IFCAP will ask you if the purchase order is ready to transmit to FMS. The invoice will be paid when the invoice and the receiving report are in agreement. Payment occurs 23 to 30 days after the invoice was received or the goods were received, whichever is later.

<span id="_Toc222493035" class="anchor"></span>Figure 5: Obligation Date

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Obligation Processing Date: JAN 5,1994// (JAN 05, 1994)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>This Purchase Order Obligation will now generate the</p>
<p>Original Entry Miscellaneous Order (MO) Document. The MO Document</p>
<p>will be marked for transmission to FMS.</p></td>
</tr>
<tr class="even">
<td><p>Transmit this Document to FMS? YES//</p>
<p>The Electronic Signature must now be entered to generate the MO Document.</p></td>
</tr>
<tr class="odd">
<td>Enter ELECTRONIC SIGNATURE CODE: Thank you.</td>
</tr>
<tr class="even">
<td>...now generating the FMS Miscellaneous Order (MO) Document...</td>
</tr>
<tr class="odd">
<td>...EXCUSE ME, HOLD ON...</td>
</tr>
</tbody>
</table>

### Post Using Status of Funds Tracker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP may ask you if you want to post this purchase order to the *Fiscal Status of Funds Tracker*, a financial tracking option used at some facilities. If you see this prompt, enter a Control Point name. If you do not know the Control Point, enter three question marks (???) at the Select Control Point Name: prompt and IFCAP will display a list of the available Control Points.

If you do not see this prompt, it is ok. It means your site has opted not to use that functionality.

<span id="_Toc222493036" class="anchor"></span>Figure 6: Post Using Status of Funds Tracker

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Do you wish to post this information to the Fiscal Status of Funds</p>
<p>Tracker? NO//???</p>
<p>If you answer 'YES', you will be asked the information necessary to post</p>
<p>the code sheet to the Fiscal Status of Funds. A 'NO' or an '^' will</p>
<p>skip the bypass the posting.</p>
<p>Do you wish to post this information to the Fiscal Status of Funds</p>
<p>Tracker? NO// Y (YES)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>REMEMBER, DO NOT ENTER TRANSACTION FOR FUTURE QUARTERS!</td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>Select CONTROL POINT NAME: ???</p>
<p>CHOOSE FROM:</p>
<p>33 033 PHARMACY</p>
<p>40 040 BUILDING MANAGEMENT</p>
<p>44 044 FEE BASIS</p>
<p>68 068 REC M&amp;R</p>
<p>73 073 ENGINEERING</p>
<p>Select CONTROL POINT NAME: 033 PHARMACY</p></td>
</tr>
</tbody>
</table>

### Enter Transaction Amount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a TRANSACTION AMOUNT. Enter the amount as an increase if the transaction is a refund, rebate or some other transaction that returns obligated money to the Control Point; enter additional expenses as deductions.

IFCAP will show the effect of the transaction on the estimated balance and ask you if you want to post the transaction now or wait until later.

If this transaction affects additional Control Points, enter another Control Point at the Select Next Control Point Name: prompt. Otherwise, enter a caret (^) at the prompt. You can print the purchase order to the printer designated for Fiscal Service and Supply Service, or you can enter “N” at the Do You Wish To Queue The Purchase Order To Another Printer?: prompt and specify another printer. Enter another station number at the Select Station Number: prompt if you have another transaction to enter. Otherwise, enter a caret (^) at the prompt to return to the Document Processing menu.

<span id="_Toc222493037" class="anchor"></span>Figure 7: Enter Transaction Amount

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ENTER TRANSACTION AMOUNT: 48.01</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>(I)ncrease or (D)ecrease to balance? D//???</p>
<p>Enter a &lt;CR&gt; or 'D' to DECREASE the balance in the status, an 'I' to INCREASE</p>
<p>the balance, or an '^' to ABORT the option.</p>
<p>(I)ncrease or (D)ecrease to balance? D//</p></td>
</tr>
<tr class="even">
<td><p>THE OLD ESTIMATED BALANCE IS $0.00</p>
<p>THE NEW ESTIMATED BALANCE IS $-48.01</p>
<p>OK TO POST? YES// (YES)</p>
<p>POSTED</p></td>
</tr>
<tr class="odd">
<td><p>Select Next Control Point Name:</p>
<p>I'M CONFUSED ABOUT WHICH CONTROL POINT YOU WANT, TRY AGAIN.</p>
<p>USE AN '^' TO QUIT</p>
<p>Select CONTROL POINT NAME: ^</p>
<p>...HMMM, THIS MAY TAKE A FEW MOMENTS...</p>
<p>...now generating the PHA transaction...</p>
<p>Do you wish to queue the Purchase Order to another printer? NO//</p></td>
</tr>
<tr class="even">
<td>Select STATION NUMBER ('^' TO EXIT): 688//</td>
</tr>
</tbody>
</table>

## Amending a Purchase Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Is There Adequate Funding for the Amendment?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control Points cannot process an amendment if the amendment exceeds the amount of their allotted funds. At the end of a fiscal year some Control Points are given the authority to over commit funds so that they can obtain bids or quotes for next year's purchases. You should receive a daily report from the Austin Finance Center called the “Status of Funds Report,” listing the funds available for each Control Point. Check this document closely for availability of funds, especially at the close of a fiscal year. This information is also available on an FMS report called the *Object Class by Allowance Report*.

### Obligate an Amendment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Amendments add, delete, or adjust items on a purchase order before the item is received. Amendments are different from adjustments, which adjust the quantity of an item on a receiving report after it is processed by Fiscal Service.

#### Menu Path

From the Accounting Technician’s Menu, select Document Processing Menu. From the Document Processing Menu, select Obligation Processing.

<span id="_Toc222493038" class="anchor"></span>Figure 8: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Document Processing Menu ...</p>
<p>Accounting Utilities Menu ...</p>
<p>Reprint Menu ...</p>
<p>Receiving Report Transmission Menu ...</p>
<p>FMS Code Sheet Menu ...</p>
<p>IRS Offset Code Sheet Menu ...</p>
<p>Print Obligated 1358s</p>
<p>Purchase Card Transactions Print Menu ...</p>
<p>Select Accounting Technician Menu Option: Document Processing Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1358 Processing Menu ...</p>
<p>Amendment Processing</p>
<p>General Post Funds Requests Processing</p>
<p>Invoice Processing (ACCTG) Menu ...</p>
<p>Obligation Processing</p>
<p>Process Receiving Report</p>
<p>Return Purchase Order to Supply</p>
<p>Return PO Amendment to Supply</p>
<p>FMS Rejected Obligation Document Processing ...</p>
<p>Select Document Processing Menu Option: Obligation Processing</p></td>
</tr>
</tbody>
</table>

#### Enter Electronic Signature

Enter a STATION NUMBER, FISCAL YEAR, and your ELECTRONIC SIGNATURE CODE. Enter the Purchase Order Number. If you do not know the purchase order number, enter three question marks (???) to have IFCAP will list the available purchase orders. Enter an AMENDMENT. If you do not know the amendment number, enter three question marks (???) and IFCAP will list the available amendment numbers.

<span id="_Toc222493039" class="anchor"></span>Figure 9: Enter Electronic Signature

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select FISCAL YEAR ('^' to EXIT): 95//</td>
</tr>
<tr class="even">
<td>Enter ELECTRONIC SIGNATURE CODE: Thank you.</td>
</tr>
<tr class="odd">
<td><p>Select Purchase Order Number: 688-A40406 INVOICE/RECEIVING REPORT</p>
<p>Ordered and Obligated</p>
<p>Select AMENDMENT:?</p>
<p>Answer with AMENDMENT, or NUMBER:</p>
<p>1 1</p>
<p>Select AMENDMENT: 1</p></td>
</tr>
<tr class="even">
<td>...SORRY, JUST A MOMENT PLEASE...</td>
</tr>
</tbody>
</table>

#### Display Amendment

IFCAP will show the amendment, the contractor, and the requisition or purchase order affected by the amendment.

<span id="_Toc222493040" class="anchor"></span>Figure 10: Display Amendment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>2. MOD. NO.: | 3. EFFECTIVE DATE: | 4. REQUISITION/P.O. REQ. NO.:</p>
<p>1 | 3/30/94 | A40406</p>
<p>_______________________________________________________________________________</p>
<p>8. NAME AND ADDRESS OF CONTRACTOR | 10A. MODIFICATION OF CONTRACT/ORDER</p>
<p>CENTRAL BUSINESS SERVICES AND SUPPLY| NO.688-A40406</p>
<p>4000 RESERVOIR ROAD | CONTRACT # 1: 94-123A</p>
<p>SUITE 200 |--------------------------------------</p>
<p>WASHINGTON, DC 20008 | 10B. DATED (See Item 13) 3/17/94</p>
<p>-------------------------------------------------------------------------------</p>
<p>12. ACCOUNTING AND APPROPRIATION DATA (If required)</p>
<p>36 0869-2222</p>
<p>-------------------------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>D. OTHER (specify type of modification and authority)</p>
<p>-------------------------------------------------------------------------------</p>
<p>IMPORTANT: Contractor is not required to sign this document and return</p>
<p>copies to the issuing office.</p>
<p>14. DESCRIPTION OF MODIFICATION (organized by UCF section heading,</p>
<p>including contract subject matter where feasible.)</p>
<p>-------------------------------------------------------------------------------</p>
<p>Except as provided herein, all terms and conditions of the document referenced</p>
<p>in Item 10A, as heretofore changed, remains unchanged and in full force and</p>
<p>effect.</p>
<p>-------------------------------------------------------------------------------</p>
<p>JUSTIFICATION: TESTING AMENDMENT PROCESS</p>
<p>-------------------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td>CONTRACTING OFFICER: IFUSER, ONE</td>
</tr>
</tbody>
</table>

#### Approve and Obligate the Amendment

At the Are You Ready To Approve And Obligate This Amendment?: prompt, answer “Y” to approve and obligate the amendment. Verify that the Budget Object Code information is correct. You may also print the amendment.

Enter the date the purchase order is obligated at the Select Obligation Processing Date: prompt. Answer “Y” at the Transmit this Document to FMS? prompt. Enter your ELECTRONIC SIGNATURE CODE. Enter another purchase order number at the Select Purchase Order Number: prompt, or press \<Enter\> to return to the Document Processing Menu.

<span id="_Toc222493041" class="anchor"></span>Figure 11: Display Amendment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The information listed above is recorded on this Purchase Order amendment.</p>
<p>Are you ready to approve and obligate this amendment? YES//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Amendment Processing</p>
<p>The following information appears on the original and any previously amended</p>
<p>Purchase Order:</p>
<p>Purchase Order - 688-A40406</p>
<p>COST CENTER: 813400 CONTROL POINT: 2222 FMS TEST CON POINT</p>
<p>Net Cost of Order: $ 68.89</p>
<p>Amendment Processing</p>
<p>Net Cost of Order: $ 68.89</p>
<p>No Control Point balances are available at this time.</p></td>
</tr>
<tr class="even">
<td><p>Amendment Processing</p>
<p>The following information appears on the original and any previously amended</p>
<p>Purchase Order:</p></td>
</tr>
<tr class="odd">
<td><p>Purchase Order - 688-A40406</p>
<p>COST CENTER: 813400 CONTROL POINT: 2222 FMS TEST CON POINT</p>
<p>Net Cost of Order: $ 68.89</p>
<p>Amendment Processing</p>
<p>Net Cost of Order: $ 68.89</p>
<p>No Control Point balances are available at this time.</p>
<p>Amendment Processing</p></td>
</tr>
<tr class="even">
<td><p>The following information appears in the amended Purchase Order</p>
<p>as listed in the DESCRIPTION OF MODIFICATION:</p>
<p>Is the above BOC information correct? YES//</p>
<p>Would you like to print this amendment? YES// n NO</p>
<p>Select Obligation Processing Date: MAR 18,1995// (MAR 18, 1995)</p></td>
</tr>
<tr class="odd">
<td><p>This Purchase Order Amendment Obligation will now generate the</p>
<p>Modification Entry Miscellaneous Order (MO) Document. The MO Document</p>
<p>will be marked for transmission to FMS.</p></td>
</tr>
<tr class="even">
<td><p>Transmit this Document to FMS? YES//</p>
<p>The Electronic Signature must now be entered to generate the MO Document.</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p></td>
</tr>
<tr class="odd">
<td><p>...copying amendment information back to Purchase Order file...</p>
<p>...SORRY, LET ME THINK ABOUT THAT A MOMENT...</p>
<p>...now generating the FMS Miscellaneous Order (MO) Document...</p>
<p>...EXCUSE ME, HOLD ON...</p></td>
</tr>
<tr class="even">
<td>Select Purchase Order Number:</td>
</tr>
</tbody>
</table>

# Obligating and Adjusting 1358 Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Inspect the 1358 for Correctness

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Are the cost center and budget object code (BOC) appropriate for this purchase? Is the Purpose (justification) adequate? Is the Purpose sufficiently explained? If the cost center or budget object code is wrong, you can correct them during the obligation process. If the Purpose (justification) is incorrect or inappropriate, return the 1358 to the service.

## Is There Adequate Funding for the 1358?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control Points cannot process a 1358 if the 1358 exceeds the amount of their allotted funds. At the end of a fiscal year some Control Points are given the authority to over commit funds so that they can obtain bids or quotes for next year's purchases. You should receive a daily report from the Austin Finance Center called the “Status of Funds Report,” listing the funds available for each Control Point. Check this document closely for availability of funds, especially at the close of a fiscal year. This information is also available on an FMS report called the *Object Class by Allowance Report*.

## Obligate 1358

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the 1358 Processing Menu, select Obligate 1358.

<span id="_Toc222493042" class="anchor"></span>Figure 12: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Accounting Technician Menu Option: Document Processing Men</p>
<p>Select Document Processing Menu Option: 1358 Processing Menu</p>
<p>Obligate 1358</p>
<p>Adjust (Increase/Decrease) 1358</p>
<p>Liquidate 1358</p>
<p>1358 Print Menu ...</p>
<p>Close 1358</p>
<p>Recalculate 1358 Balances</p>
<p>Reopen a Closed 1358</p>
<p>Send 1358 back to Service without action</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select 1358 Processing Menu Option: Obligate 1358</td>
</tr>
</tbody>
</table>

### Enter Station Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a STATION NUMBER and a FISCAL YEAR. Enter the TRANSACTION NUMBER of the 1358 you wish to obligate. You will be able to view the Authority, Sub-authority, Service Start Date, and Service End Date on the screen.

You will be asked to review the 1358 request:

Would you like to review this request?? No// Y (Yes)

Responding “N” will continue with the 1358 Obligating. Responding “Y” will then display all the detailed information on the 1358 to ascertain full 1358 compliance prior to obligation. Once the display has completed you will be asked:

Would you like to continue obligating this 1358?? Yes// N (No)

Responding “N” will exit the Obligate 1358 option. Responding “Y” will allow continuation of the 1358 Obligate processing.

At the Will this 1358 Obligation Need To Be Accrued In FMS? prompt, enter “Y” if this obligation should be distributed among multiple accounting periods. Otherwise, enter “N”. Confirm that the information is correct.

Enter “N” at the Are these Auto Accrual values correct? prompt to edit the Cost Center or BOC. Otherwise, enter “Y”.

Enter “Y” at the Is the above information correct? prompt to continue.

<span id="_Toc222493043" class="anchor"></span>Figure 13: Setup Parameters

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 00//

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER:

1358 TRANSACTION - 688-11-1-110-0009

COST CENTER: 842100 AMOUNT: \$ 19999.00

BOC \#1: 2580 AMOUNT \#1: \$ 19999.00

AUTHORITY: 2 FEE BASIS

SUB: C HOMEMAKER/HOME HEALTH AID

SERVICE START DATE: Oct 01, 2010

SERVICE END DATE: Oct 31, 2010

MONTHLY HHA COSTS \<= this is the Purpose (Justification)

VENDOR: HOLDRENS INC

Would you like to review this request?? No// Y (Yes) Yes will display 1358

No will continue obligation

..

Would you like to continue obligating this 1358?? Yes// Y (Yes) Only seen if ‘Yes’ to review

Yes, I will continue obligation

No, I will exit obligation processing

Editing Auto Accrual information...

This 1358 Obligation appears to be for services.

Will this 1358 Obligation need to be accrued in FMS? YES//

CURRENT VALUES FOR AUTO ACCRUAL FOR 1358:

ENDING DATE FOR SERVICE: OCT 31, 2010

AUTO ACCRUAL FLAG: NO

Are these Auto Accrual values correct? YES//NO

CURRENT VALUES FOR AUTO ACCRUAL FOR 1358:

ENDING DATE FOR SERVICE: OCT 31, 2010//

AUTO ACCRUAL FLAG: NO// YES

CURRENT VALUES FOR AUTO ACCRUAL FOR 1358:

ENDING DATE FOR SERVICE: OCT 31, 2010

AUTO ACCRUAL FLAG: Yes

Are these Auto Accrual values correct? YES//

### Review Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Look at the unobligated balance of the Control Point. If the amount of the 1358 is less than the un-obligated balance, enter “Y” at the OK To Continue? prompt. Otherwise, enter N and return the 1358 to Fiscal Service.

<span id="_Toc222493044" class="anchor"></span>Figure 14: Review Balances

Uncommitted Balance: \$ 977607.00

Unobligated Balance: \$ 999004.00

Committed, Not Obligated: \$ 21397.00

to Continue? YES//

### Enter Obligation Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter an obligation number for 1358. Answer “Y” at the Transmit this document to FMS? prompt. Enter your ELECTRONIC SIGNATURE CODE. Enter a Station Number at the Select Station Number: prompt to obligate another 1358 or enter a caret (^) at the prompt to return to the 1358 Processing Menu.

<span id="_Toc222493045" class="anchor"></span>Figure 15: Enter Obligation Number

ENTER A NEW 1358 Obligation Number OR A COMMON NUMBERING SERIES

1358 Obligation Number: c15 688-C15 ACCOUNTING TECHNICIAN

Are you adding '688-C15003' as a new 1358 Obligation Number? y (Yes)

Select Obligation Processing Date: OCT 8,2010// (OCT 08, 2010)

This FMS document will be transmitted on 10/08/10 and will

affect the accounting period of October 2010. The Accounting

Period affected in FMS will be 0111.

Is this OK? YES//

This 1358 Obligation will now generate the

Original Entry Service (SO) Order Document. The SO Document

will be marked for transmission to FMS.

Transmit this Document to FMS? YES//

The Electronic Signature must now be entered to generate the SO Document.

Enter ELECTRONIC SIGNATURE CODE:

Sorry, but that's not your correct electronic signature code.

Enter ELECTRONIC SIGNATURE CODE: Thank you.

...now generating the FMS Service Order (SO) Document...

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

...updating 1358 Obligation balances...

...Excuse me, let me think about this for a moment...

...Control Point has been notified of this transaction...

### Enforcing Segregation of Duties on 1358s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you select a 1358 transaction for Obligation and you were a Requestor or Approver on that 1358 transaction, you will be advised of the Role you already performed on the transaction and will not be permitted to Obligate the 1358.

<span id="_Toc222493046" class="anchor"></span>Figure 16: Enforcing Segregation of Duties on 1358s

Select 1358 Processing Menu Option: Obligate 1358

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 11//

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER:688-11-1-110-0009

1358 TRANSACTION - 688-11-1-110-0009

COST CENTER: 842100 AMOUNT: \$ 19999.00

BOC \#1: 2580 AMOUNT \#1: \$ 19999.00

AUTHORITY: 2 FEE BASIS

SUB: C HOMEMAKER/HOME HEALTH AID

SERVICE START DATE: Oct 01, 2010

SERVICE END DATE: Oct 31, 2010

MONTHLY HHA COSTS

You are the Approver on this 1358 transaction.

Per Segregation of Duties, the Approver is not permitted to Obligate the 1358.

# Enforcing Segregation of Duties in Online Certification System for 1358 Obligation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An interface exists between the IFCAP application and the Online Certification System (OLCS) located at the Financial Services Center (FSC) in Austin, Texas. The interface will support the validation of the Certifier of Payment role in the OLCS.

The interface is a one-way data exchange of 1358 Obligation data from the IFCAP application to the OLCS using VistA MailMan messages. The mail messages support segregation of duties within OLCS by providing OLCS with the names of the requestor, approver, and obligator on every 1358 transaction as it is obligated in IFCAP. Segregation of duties prevents a user from functioning in more than one role on a 1358. The OLCS will verify that a certifier processing an invoice for a 1358 in OLCS is not the requestor, approver, or obligator on that 1358 in IFCAP.

IFCAP triggers a VistA MailMan message to the OLCS when a 1358 is obligated (i.e. Electronic Signature Code is entered). The exchange of 1358 Obligation data from the IFCAP to the Online Certification System will occur in the background and be transparent to IFCAP end-users.

<span id="_Toc222493047" class="anchor"></span>Figure 17: 1358 Obligation Exchange of Data to Online Certification System

ENTER A NEW 1358 Obligation Number OR A COMMON NUMBERING SERIES

1358 Obligation Number: c15 688-C15 ACCOUNTING TECHNICIAN

Are you adding '688-C15003' as a new 1358 Obligation Number? y (Yes)

Select Obligation Processing Date: OCT 8,2010// \<Enter\> (OCT 08, 2010)

This FMS document will be transmitted on 10/08/10 and will

affect the accounting period of October 2010. The Accounting

Period affected in FMS will be 0111.

Is this OK? YES// \<Enter\>

This 1358 Obligation will now generate the

Original Entry Service (SO) Order Document. The SO Document

will be marked for transmission to FMS.

Transmit this Document to FMS? YES// \<Enter\>

The Electronic Signature must now be entered to generate the SO Document.

Enter ELECTRONIC SIGNATURE CODE:

Sorry, but that's not your correct electronic signature code.

Enter ELECTRONIC SIGNATURE CODE: Thank you.

...now generating the FMS Service Order (SO) Document...

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

...updating 1358 Obligation balances...

...Excuse me, Let me think about this for a moment...

...Control Point has been notified of this transaction...

## Adjustments to 1358s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control Points may require changes to their obligated 1358 during the month. IFCAP links the 1358 adjustment to the original 1358 by the obligation number and increases or decreases the obligated total automatically.

### Inspect the Adjustment for Correctness

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Is the purpose of the adjustment sufficiently explained? Decreased adjustments should have a minus sign preceding the dollar amount; was the adjustment correctly entered as a decrease or an increase? If not, return the adjustment to the Control Point.

### Is There Adequate Funding for the Adjustment?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control Points cannot process an adjustment if the adjustment exceeds the amount of their allotted funds. At the end of a fiscal year some Control Points are given the authority to over commit funds so that they can obtain bids or quotes for next year's purchases. You should receive a daily report from the Austin Finance Center called the “Status of Allowance Report,” listing the funds available for each Control Point. Check this document closely for availability of funds, especially at the close of a fiscal year. This information is also available on an FMS report called the *Object Class by Allowance Report*.

### Adjust the 1358

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu Path

From the Accounting Technician’s Menu, select Document Processing Menu.

<span id="_Toc222493048" class="anchor"></span>Figure 18: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Technician Menu Option: Document Processing Menu</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select Document Processing Menu Option: 1358 Processing Menu</td>
</tr>
<tr class="even">
<td><p>Obligate 1358</p>
<p>Adjust (Increase/Decrease) 1358</p>
<p>Liquidate 1358</p>
<p>1358 Print Menu ...</p>
<p>Close 1358</p>
<p>Recalculate 1358 Balances</p>
<p>Reopen a Closed 1358</p>
<p>Send 1358 back to Service without action</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Select 1358 Processing Menu Option: Adjust (Increase/Decrease) 1358</td>
</tr>
</tbody>
</table>

#### Enter Station Number

Enter a station number and a fiscal year. Enter the transaction number for the adjustment. If you do not know the transaction number, enter three question marks (???) at the prompt and IFCAP will display the available transactions.

<span id="_Toc222493049" class="anchor"></span>Figure 19: Setup Parameters

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select FISCAL YEAR ('^' to EXIT): 11//</td>
</tr>
<tr class="even">
<td><p>Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: ???</p>
<p>1 C15001 688-10-4-110-0012 ADJ C15001</p>
<p>2 C15002 688-11-1-110-0022 ADJ LONG LASTING TELEPHO C15003</p>
<p>3 C15006 688-11-1-110-0036 ADJ LONG LASTING TELEPHO C15006</p>
<p>4 C15007 688-11-1-110-0037 ADJ LONG LASTING TELEPHO C15007</p>
<p>5 C15008 688-11-1-120-0045 ADJ C15148</p>
<p>TYPE '^' TO STOP, OR</p></td>
</tr>
<tr class="odd">
<td>CHOOSE 1-5: 5 Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: C15003 688-11-1-110-0022 ADJ C15003</td>
</tr>
<tr class="even">
<td>...retrieving 1358 information...</td>
</tr>
<tr class="odd">
<td>...SORRY, I'M WORKING AS FAST AS I CAN...</td>
</tr>
</tbody>
</table>

#### Review Balances

IFCAP will list the service balance, the fiscal balance, and the adjustment amount. The service balance is the balance on the 1358 after the Control Point Clerk enters authorizations. The fiscal balance is the balance on the 1358 after Fiscal Service enters payments (liquidations). IFCAP will also list the cost center and the budget object code for the original 1358 and for the adjustment, and the auto accrual values. Enter N at the Is the above information correct? prompt to edit the Cost Center or BOC. At the Will this 1358 Obligation Need to Be Accrued In FMS? prompt, enter “Y” if this obligation should be distributed among multiple accounting periods. Otherwise, enter N. Confirm that the information is correct.

<span id="_Toc222493050" class="anchor"></span>Figure 20: Review Balances

PROCESS 1358 ADJUSTMENT Obligation \#: 688-C15003

Service Balance: \$ 19,999.00

Fiscal Balance: \$ 19,999.00

Amount of Adjustment: \$ 777.00

ORIGINAL ADJUSTMENT

COST CENTER: 842100 842100

BOC \#1: 2580 2580

Editing Auto Accrual information...

CURRENT VALUES FOR AUTO ACCRUAL FOR 1358:

ENDING DATE FOR SERVICE: OCT 31, 2010

AUTO ACCRUAL FLAG: YES

Are these Auto Accrual values correct? YES//

Returning to Obligation processing...

The information listed above is recorded on this 1358 Obligation Adjustment.

Is the above information correct? YES//

#### Enter Electronic Signature

IFCAP will list the transaction number of the adjustment, the current amount obligated on the 1358, the total amount of authorizations for the 1358, the total liquidations (payments) for the 1358, the authorization balance (payments authorized by the Control Point), the liquidation balance (the balance on the 1358 after Fiscal Service enters payments), and the amount of the adjustment. enter “Y” at the OK to Continue? prompt. enter “Y” at the Transmit this Document to FMS? prompt. Enter your ELECTRONIC SIGNATURE CODE. IFCAP will compute the adjustment and record the adjustment. Enter a caret (^) at the “Select Station Number:” prompt to return to the 1358 Processing Menu.

### Enforcing Segregation of Duties on 1358 Adjustments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Per Segregation of Duties on 1358s, you will be advised if you already signed the 1358 transaction as a Requestor or Approver and you will not be permitted to Obligate the Adjustment.

<span id="_Toc222493051" class="anchor"></span>Figure 21: Segregation of Duties on Adjustments

Select 1358 Processing Menu Option: ADJust (Increase/Decrease) 1358

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select FISCAL YEAR ('^' to EXIT): 11//

Select CONTROL POINT ACTIVITY TRANSACTION NUMBER: C15002 688-11-1-110-0023 ADJ

IFVENDOR C15002

...retrieving 1358 information...

...HMMM, THIS MAY TAKE A FEW MOMENTS...

PROCESS 1358 ADJUSTMENT Obligation \#: 688-C15002

Service Balance: \$ 556.00

Fiscal Balance: \$ 556.00

Amount of Adjustment: \$ 111.00

ORIGINAL ADJUSTMENT

COST CENTER: 842100 842100

BOC \#1: 2580 2580

VENDOR: IFVENDOR

CONTRACT: GS-98-99827F

CONTRACT ENDING DATE: OCT 31, 2010

Editing Auto Accrual information...

CURRENT VALUES FOR AUTO ACCRUAL FOR 1358:

ENDING DATE FOR SERVICE: OCT 31, 2010

AUTO ACCRUAL FLAG: YES

Are these Auto Accrual values correct? YES//

Returning to Obligation processing...

The information listed above is recorded on this 1358 Obligation Adjustment.

Is the above information correct? YES//

Adjustment Transaction \# 688-11-1-110-0023 1358 \# 688-C15002

Current amount obligated on 1358: \$ 556.00

Total Authorizations: \$ 556.00 Total Liquidations: \$ 556.00

Authorization Balance: \$ 0.00 Liquidation Balance: \$ 0.00

Amount of Adjustment: 111.00

You are the Requestor on this 1358 transaction. Per Segregation of Duties, the Requestor is not permitted to Obligate the 1358.

No further processing is being taken on this 1358 adjustment obligation.

It has NOT been obligated.

### Enforcing Segregation of Duties in Online Certification System for 1358 Adjustments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An interface exists between the IFCAP application and the Online Certification System (OLCS) located at the Financial Services Center (FSC) in Austin, Texas. The interface will support the validation of the Certifier of Payment role in the OLCS.

The interface is a one-way data exchange of 1358 Obligation data from the IFCAP application to the OLCS using VistA MailMan messages. The mail messages support segregation of duties within OLCS by providing OLCS with the names of the requestor, approver, and obligator on every 1358 transaction as it is obligated in IFCAP. Segregation of duties prevents a user from functioning in more than one role on a 1358. The OLCS will verify that a certifier processing an invoice for a 1358 in OLCS is not the requestor, approver, or obligator on that 1358 in IFCAP.

IFCAP will trigger a VistA MailMan message to the OLCS when a 1358 increase/decrease adjustment is obligated (i.e. Electronic Signature Code is entered). The exchange of 1358 Obligation data from the IFCAP application to the Online Certification System will occur in the background and be transparent to IFCAP end-users.

<span id="_Toc222493052" class="anchor"></span>Figure 22: Validation of Certifier of Payment Role

Adjustment Transaction \# 688-11-1-110-0022 1358 \# 688-C15003

Current amount obligated on 1358: \$ 19,999.00

Total Authorizations: \$ 19,999.00 Total Liquidations: \$ 19,999.00

Authorization Balance: \$ 0.00 Liquidation Balance: \$ 0.00

Amount of Adjustment: 777.00

OK to Continue? YES//

Select Obligation Processing Date: OCT 8,2010/ (OCT 08, 2010)

This FMS document will be transmitted on 10/08/10 and will

affect the accounting period of October 2010. The Accounting

Period affected in FMS will be 0111.

Is this OK? YES//

This 1358 Obligation Adjustment will now generate the

Modification Entry Service (SO) Order Document. The SO Document

will be marked for transmission to FMS.

Transmit this Document to FMS? YES//

The Electronic Signature must now be entered to generate the SO Document.

Enter ELECTRONIC SIGNATURE CODE: Thank you.

...now generating the FMS Service Order (SO) Document...

...HMMM, I'M WORKING AS FAST AS I CAN...

...updating obligation balances.... please hold...

...adjustment completed...

## Display or Print Obligated 1358s

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a date range and device to obtain a list of obligated 1358s with a dollar value of \$0 and higher. Your previous entries for the START and GO TO P.O. DATES will appear as the defaults.

The report includes information such as P.O. \#, Authority, Sub-authority, Service Start and End Dates, Amount and Requestor; and Vendor and Contract information, if it was entered when the 1358s were created.

This option should be printed at 132 columns.

<span id="_Toc222493053" class="anchor"></span>Figure 23: Setup Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>* Previous selection: P.O. DATE from Oct 3, 2010, to Oct 9, 2010 @24:00</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>START WITH P.O. DATE: Oct 3,2010// (OCT 03, 2010)</td>
</tr>
<tr class="even">
<td>GO TO P.O. DATE: Oct 9,2010// (OCT 9, 2010)</td>
</tr>
<tr class="odd">
<td>DEVICE: HOME// LAT RIGHT MARGIN: 80// 132</td>
</tr>
<tr class="even">
<td>PROCUREMENT &amp; ACCOUNTING TRANSACTIONS LIST (OBLIGATED 1358s) FEB 6,2006 13:13 PAGE 1</td>
</tr>
<tr class="odd">
<td><p>BUSINESS</p>
<p>PURCHASE VENDOR</p>
<p>CONTRACT TYPE SOCIOECONOMIC TOTAL</p>
<p>ORDER NUMBER P.O. DATE VENDOR NUMBER</p>
<p>(FPDS) GROUP (FPDS) AMOUNT REQUESTOR</p>
<p>Service Start Date Service End Date</p>
<p>Authority</p>
<p>Sub-Authority</p>
<p>------------------------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>688-C05032 OCT 5,2010</p>
<p>1000 TEST, ABR</p>
<p>10/01/10 10/31/10</p>
<p>2 FEE BASIS</p>
<p>A FEE MEDICAL/DENTAL (PRE-AUTHORIZED)</p>
<p>688-C15001 OCT 5,2010 AMSCO1 INTERNATIONAL SMALL W S</p>
<p>HZ 8.44 IFREQUESTOR, FOUR</p>
<p>10/01/10 11/30/10</p>
<p>20 NON-PROCUREMENT OBLIGATIONS</p>
<p>E CEMETERY GRANTS AND STATE HOME PROGRAM</p>
<p>688-C15002 OCT 5,2010 IFVENDOR EIGHT GS-98-99827F SMALL</p>
<p>N 556 IFREQUESTOR, TWO</p>
<p>10/01/10 10/31/10</p>
<p>3 STANDARDIZED OBLIGATIONS</p>
<p>B COLLEGE OF AMERICAN PATHOLOGY</p></td>
</tr>
</tbody>
</table>

## Display/Print 1358

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may view a 1358 using the Display/Print 1358 option on the 1358 Print Menu.

You may select the brief version of the 1358 or the standard ‘full’ version of the 1358 form.

<span id="_Toc222493054" class="anchor"></span>Figure 24: Viewing a 1358 Using Display/Print 1358 Option on 1358 Print Menu

Select 1358 Print Menu Option: DISPLAY/PRINT 1358

Brief or Standard output? (B/S): B//

Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC

Select OBLIGATION NUMBER: C15003 688-C15003 10-08-10 1358 Obligated - 1358

FCP: 110 \$ 20776.00

SERVICE START DATE: 10/01/10 SERVICE END DATE: 10/31/10AUTHORITY: 2 FEE BASISSUB: C HOMEMAKER/HOME HEALTH AID

Do you wish to view the Authorization information? No// NO

DEVICE: TELNET

Obligation \#: 688-C15003

Total Authorization: \$ 0.00 Total Liquidation: \$ 0.00

\|AUTHORIZATION/ORDER REC\| LIQUIDATION RECORD

Date/Time Reference No\|Indiv/Daily Cumul \| Liq. Amt \| Unliq Bal.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

10/08/10 \| OBLIGATION \| \| \| 19999.00\| 19999.00

10/08/10 \| ADJUSTMENT \| \| \| 777.00\| 20776.00

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Do you wish to view another 1358? YES//No

Brief or Standard output? (B/S): B// s

Select OBLIGATION NUMBER: C05026 688-10-4-110-0051

Would you like to print the Description field for each 1358 Daily Record entry? No// y (Yes)

Would you like to print the daily records for each authorization? NO// Y YES

Would you like to print descriptions for each detailed daily record? NO// Y YES

DEVICE: HOME// TELNET Right Margin: 80//

688-10-4-110-0051 OCT 15, 2010@17:52:38 PAGE 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE: STANDARDIZED OBLIGATIONS

FEE BASIS PURCHASE CARD

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Originator of Request:

Requestor: \|Date Requested: \|Obligation No.:

IFUSER, TWO \|SEP 23,2010 \| 688-C05026

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Vendor: \|Contract Number:

\|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Name and Title Approving Off.: \|Signature: \|Date Signed:

IFUSER, FOUR \|/ES/IFUSER FOUR \|SEP 23, 2010@17:49:27

SERVICE CHIEF \| \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FUND CERTIFICATION: The supplies and services listed on this request are

properly chargeable to the following allotments, the available balances of

which are sufficient to cover the cost thereof, and funds have been obligated.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Appropriation & Acct. Symbols: \|Obligated By: \|Date Obligated:

688-3600160-110-842100-2580 010042116 \|/ES/USER ACCT TECH \|SEP 23, 2010

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

688-10-4-110-0051 688-C05026 PAGE 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1358 OBLIGATION OR CHANGE: STANDARDIZED OBLLIGATIONS

FEE BASIS PURCHASE CARD

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Appropriation & Acct. Symbols: \|Obligated By: \|Date Obligated:

688-3600160-110-842100-2580 010042116 \|/ES/USER ACCT TECH \|SEP 23, 2010

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORITY: 3 SUB: F

\_SERVICE START DATE: 09/01/10 SERVICE END DATE: 11/01/10

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Purpose:

MORE APPTS. FOR TWO MONTHS

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ESTIMATED OBLIGATION RECAP

DATE REF# CPA# AMOUNT BALANCE

09/23 0001 688-10-4-110-0051 \$ 456.00 \$ 456.00

09/27 0002 688-10-4-110-0058 \$ 828.00 \$ 1284.00

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AUTHORIZATION & ORDER RECORD LIQUIDATION RECORD

AUTH. AUTH. CUMULATIVE UNLIQ

DATE SEQ# REFERENCE AMOUNT BALANCE AUTH. AMT. LIQUID BAL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

10/15 0003 1ST WEEK COSTS \$ 235.50 \$ 0.00 \$ 235.50 \$ 0.00

10/15 0003-1

2 PTS \$ 235.50

10/15 0004 2ND WEEKS COSTS \$ 275.00 \$ 93.25 \$ 510.50 \$ 0.00

10/15 0004-1

1 PT VISIT \$ 181.75

10/15 0005 3RD WEEKS COSTS \$ 325.00 \$ 325.00 \$ 835.50 \$ 0.00

TOTALS \$835.50 \$418.25 \$835.50 \$1284.00

VA FORM 4-1358a-ADP (NOV 1987)

# Review and Forward Receiving Reports for Payment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter explains how to make sure that the information on the received order report is correct.

## Dollar Amounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Compare the dollar amounts on the receiving report to the purchase order. To view the IFCAP record of the purchase order, follow the steps in this section.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Accounting Technician Menu, select Document Processing Menu.

From the Document Processing Menu, select Process Receiving Report.

Enter a STATION NUMBER and a FISCAL YEAR.

At the Select PURCHASE ORDER NUMBER: prompt, enter the PAT number for the receiving report. If you do not know the PAT number, enter three question marks (???) at the prompt and IFCAP will display the available transactions.

<span id="_Toc222493055" class="anchor"></span>Figure 25: Setup Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p> 1358 Processing Menu ...</p>
<p>Amendment Processing</p>
<p>General Post Funds Requests Processing</p>
<p>Invoice Processing (ACCTG) Menu ...</p>
<p>Obligation Processing</p>
<p>Process Receiving Report</p>
<p>Return Purchase Order to Supply</p>
<p>Return PO Amendment to Supply</p>
<p>Stacked Fiscal Documents Menu ...</p>
<p>FMS Rejected Obligation Document Processing ...</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select Document Processing Menu Option: Process Receiving Report</td>
</tr>
<tr class="even">
<td>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</td>
</tr>
<tr class="odd">
<td><p>Select Purchase Order Number: ???</p>
<p>CHOOSE FROM:</p>
<p>H40006 07-14-94 ST Partial Order Received FCP: 1101 $ 429.00</p>
<p>H40007 07-14-94 ST Partial Order Received FCP: 1101 $ 429.00</p>
<p>H40008 07-14-94 ST Complete Order Received FCP: 1101 $ 98.00</p>
<p>H40021 07-15-94 ST Partial Order Received FCP: 1102 $ 123.00</p>
<p>H40024 07-21-94 ST Partial Order Received FCP: 1102 $ 113.00</p></td>
</tr>
<tr class="even">
<td><p>Select Purchase Order Number: H40024 688-H40024 07-21-94 ST Partial Order</p>
<p>Received</p>
<p>FCP: 1102 $ 113.00</p></td>
</tr>
</tbody>
</table>

### Review Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may review the purchase order if you like. The purchase order lists the vendor, the shipping address, the cost center, and each item.

<span id="_Toc222493056" class="anchor"></span>Figure 26: Review Order

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Do you want to review the Purchase Order and Receiving Report? NO// Y (YES)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PURCHASE ORDER: 688-H40024 STATUS: Partial Order Received</p>
<p>M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.: 2 07/21/94</p>
<p>REQUESTING SERVICE: FISCAL</p>
<p>VENDOR: IFVENDOR BUSINESS SUPPLY SHIP TO: WAREHOUSE</p>
<p>4000 RESERVOIR ROAD V.A. Medical Center</p>
<p>SUITE 200 8403 COLESVILLE ROAD</p>
<p>WASHINGTON, DC 20008 SUITE 200</p>
<p>202 555-5555 SILVER SPRIN, MD 20910</p>
<p>ACCT # 234902349</p>
<p>DELIVERY HOURS:</p>
<p>7-4:40</p>
<p>_______________________________________________________________________________</p>
<p>FOB POINT: ORIGIN |PROPOSAL: N/A |AUTHORITY:</p>
<p>COST CENTER: 880100 | | FAR 13</p>
<p>TYPE: DELIVERY &amp; PURCHASE ORDER| |AGENT:</p>
<p>DELIVER ON/BEFORE 7/31/94 |CONTRACT: | IFUSER,ONE</p>
<p>DISCOUNT TERM: NET30 | |DATE: 7/21/94</p>
<p>APP: 36X8180-1102 |</p>
<p>| |TOTAL: 113.00</p>
<p>-------------------------------------------------------------------------------</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>-------------------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>1 WIDGET 40 EA 2.00 80.00</p>
<p>QTY PREV RCVD: 30</p>
<p>PARTIAL NO.: 1,2</p>
<p>Items per EA: 1</p>
<p>2 EST. SHIPPING AND/OR HANDLING 33.00</p></td>
</tr>
</tbody>
</table>

### Review Receiving Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may also review the receiving report. The receiving report lists each time that the service recorded the partial receipt of an order. This report lists the items that were received, the amount, and the cost. You may process one of the partial receipts. Enter your electronic signature code. Transmit the report to Austin. Enter a caret (^) at the Select Station Number: prompt to return to the Document Processing Menu.

Tip: If there is a shipping charge, it will appear on the first partial receiving report.

<span id="_Toc222493057" class="anchor"></span>Figure 27: Review Receiving Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th> Review a Receiving Report? NO// Y (YES)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select PARTIAL DATE: 1 7-21-1994</td>
</tr>
<tr class="even">
<td><p>PURCHASE ORDER: 688-H40024 STATUS: Partial Order Received</p>
<p>PROCESSING: INVOICE/RECEIVING REPORT PARTIAL: 1 7/21/94</p>
<p>-------------------------------------------------------------------------------</p>
<p>UNIT QTY TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST REC COST</p>
<p>-------------------------------------------------------------------------------</p></td>
</tr>
<tr class="odd">
<td><p>1 TEST ITEM W/O ITEM MASTER NUMBER 40 EA 2.00 20 40.00</p>
<p>Estimated Shipping and/or Handling 33.00</p>
<p>Total Amount: 73.00</p>
<p>Processed By: /ES/IFUSER, ONE</p>
<p>ENTER &lt;CR&gt; TO CONTINUE</p></td>
</tr>
<tr class="even">
<td><p>Select PARTIAL DATE:</p>
<p>Partial Number to PROCESS: ???</p>
<p>CHOOSE FROM:</p>
<p>1 07-21-1994</p>
<p>2 07-21-1994 @ 12:00</p>
<p>Partial Number to PROCESS: 2 7-21-1994@12:00:00</p></td>
</tr>
<tr class="odd">
<td><p>OBLIGATION NUMBER: 688-H40024-02 PARTIAL #: 2</p>
<p>TOTAL AMOUNT OF RECEIVING REPORT: $20.00</p>
<p>TRANSACTION TYPE: RR TRANSACTION DATE: 072194 REF #: 688-H40024-02</p>
<p>LIQ. CODE: P</p>
<p>Item #: 1 FMS Line #: 001 BOC: 3150 FMS Amount: 20.00 Liq. Amount: 0.00</p>
<p>LIQUIDATION CODE: P</p></td>
</tr>
<tr class="even">
<td>Enter ELECTRONIC SIGNATURE CODE: Thank you.</td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Are you sure you wish to send this Receiving Report to Austin? YES// (YES)</p>
<p>TRANSMISSION DATE: T// (JUL 21, 1994)</p>
<p>Receiving report placed on transmission list.</p></td>
</tr>
</tbody>
</table>

# Process 1358 Invoices for Payment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After an invoice is sent to the Certifying Official (usually the Control Point Official) to be certified for payment, the Certifying Official returns it to the accounting office, where the Voucher Audit Clerk (or Accounting Technician if there is no Voucher Audit Clerk at your station) records the certification in IFCAP. (See the Voucher Auditor Manual for options used to process the Certified Invoices).

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Accounting Technician Menu, select Document Processing Menu.

From the Document Processing Menu, select Invoice Processing (ACCTG) Menu.

From the Invoice Processing (ACCTG) Menu, select Invoice Processing for Payment.

<span id="_Toc222493058" class="anchor"></span>Figure 28: Menu Path

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Invoice Processing for Payment</p>
<p>Return Invoice to Voucher Audit</p>
<p>PV Payment Voucher (PV) Inquiry</p>
<p>FMS Payment Voucher Error Processing</p>
<p>View Certified Invoice</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select Invoice Processing (ACCTG) Menu Option: Invoice Processing for Payment</td>
</tr>
</tbody>
</table>

### Select Station Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a STATION NUMBER. Enter the INVOICE TRACKING ID NUMBER recorded on the invoice before it was sent to the Certifying Official. Compare the purchase orders on the invoice and the IFCAP record of the invoice amount to make sure that they are the same. If the amounts are different, verify that there is no clerical error, then call the Control Point Official to correct the discrepancy. You may also display or print the 1358.

<span id="_Toc222493059" class="anchor"></span>Figure 29: Select Station Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select INVOICE TRACKING ID NUMBER: 198 EZ123 In Accounting 688-C452</p>
<p>23</p></td>
</tr>
<tr class="even">
<td>Post Liquidation to 1358 Obligation #: 688-C45223</td>
</tr>
<tr class="odd">
<td><p>Status: Obligated - 1358</p>
<p>Current amount obligated: $ 1,500.00 Authorization Balance: $ 1,500.00</p>
<p>Unliquidated Balance: $ 1,500.00</p></td>
</tr>
<tr class="even">
<td>Do you wish to display/print the entire 1358? No// YES</td>
</tr>
<tr class="odd">
<td><p>Select OBLIGATION NUMBER: 688-C45223 -- 1358 Obligated - 1358</p>
<p>FCP: 110 $ 1500.00</p>
<p>Do you wish to view the Authorization information? No// YES</p>
<p>DEVICE: LAT</p></td>
</tr>
<tr class="even">
<td><p>Obligation #: 688-C45223</p>
<p>Total Authorization: $ 0.00 Total Liquidation: $ 0.00</p>
<p>|AUTHORIZATION/ORDER REC| LIQUIDATION RECORD</p>
<p>Date/Time Reference No|Indiv/Daily Cumul | Liq. Amt | Unliq Bal.</p>
<p>_______________________________________________________________________________</p>
<p>10/13/94 | OBLIGATION | 1500.00| 1500.00| 1500.00| 1500.00</p>
<p>_______________________________________________________________________________</p>
<p>Post Liquidation to 1358 Obligation #: 688-C45223</p>
<p>Status: Obligated - 1358</p>
<p>Current amount obligated: $ 1,500.00 Authorization Balance: $ 1,500.00</p>
<p>Unliquidated Balance: $ 1,500.00</p></td>
</tr>
<tr class="odd">
<td>Do you wish to display/print the entire 1358 again? No//</td>
</tr>
<tr class="even">
<td>Ok to continue? Yes//</td>
</tr>
</tbody>
</table>

### Assign Liquidation Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will assign an entry number to the liquidation. Enter the date that you want the liquidation to take effect and the amount of the liquidation. Enter a reference for the liquidation and comments. Enter “N” at the “Would You Like to Enter Another Liquidation for This Obligation?” prompt if you are finished entering liquidations. You may also select another 1358.

<span id="_Toc222493060" class="anchor"></span>Figure 30: Assign Liquidation Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>This 1358 Liquidation entry is assigned entry number 688-C45223-0002.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>LIQUIDATION DATE: OCT 14, 1994@10:00:01// (OCT 14, 1994@10:00:01)</p>
<p>LIQUIDATION AMOUNT: (-999999999.99-999999999.99): 1500// $1,500.00</p></td>
</tr>
<tr class="even">
<td><p>REFERENCE:</p>
<p>COMMENTS: Some comments.</p></td>
</tr>
<tr class="odd">
<td>...Excuse me, Let me think about this for a moment... ---POSTED---</td>
</tr>
<tr class="even">
<td>Would you like to enter another Liquidation for THIS OBLIGATION? No//</td>
</tr>
<tr class="odd">
<td><p>Obligation #: 688-C45223</p>
<p>Sequence # Amount</p>
<p>0002 1500.00</p>
<p>Total: 1500.00</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td>Would you like to select another 1358 (obligation number)? Yes// NO</td>
</tr>
</tbody>
</table>

### Select Budget Object Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select BOC: prompt, enter the BOC for the 1358. If you do not know the BOC for this item, enter three question marks (???) and IFCAP will list the available budget object codes. enter “Y” at the OK To Process This Payment To FMS? prompt. Enter your ELECTRONIC SIGNATURE CODE. Enter another station number at the Select Station Number: prompt to process another invoice for payment or enter a caret (^) at the prompt to return to the Invoice Processing (ACCTG) Menu.

<span id="_Toc222493061" class="anchor"></span>Figure 31: Select BOC

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Unliquidated obligation amounts and BOCs on this order are:</p>
<p>$1,500.00 2515 Systems Analysis &amp; Programming (Comm Supplier)</p>
<p>Total Invoice Amount Certified for Payment=$1500.00</p>
<p>Select BOC: 2515 Systems Analysis &amp; Program</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FMS Line #1</p>
<p>OBLIGATION AMOUNT: 1500.00</p>
<p>ACCOUNTING LINE AMOUNT: 1500//</p>
<p>LIQUIDATION AMOUNT: 1425.00//</p>
<p>LIQUIDATION CODE: P// PARTIAL</p></td>
</tr>
<tr class="even">
<td>Select BOC:</td>
</tr>
<tr class="odd">
<td><p>OK to process this payment to FMS? NO// y (YES)</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p></td>
</tr>
<tr class="even">
<td><p>Transferring invoice data to PV documents for transmission to FMS.</p>
<p>688C4522301</p>
<p>Status has been changed from 'In Accounting'</p>
<p>to 'Transaction Complete'.</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Select STATION NUMBER ('^' TO EXIT): 688// ^</td>
</tr>
</tbody>
</table>

## Verifying Payment Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Eventually, a CAPPS report will print, listing the payment transmission you created. Look at the invoices on the report to see if any of your invoice payments are rejected. If you have rejects, use the following steps to edit and retransmit corrected payment information.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Accounting Technician Menu, select Document Processing Menu.

From the Document Processing Menu, select Invoice Processing (ACCTG) Menu.

### Enter and Verify Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the correct information about the invoice payment at the prompts.

<span id="_Toc222493062" class="anchor"></span>Figure 32: Enter and Verify Transmission

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Invoice Processing (ACCTG) Menu Option: FMS Payment Voucher Error Processing</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FMS Payment Voucher Error Processing</td>
</tr>
<tr class="even">
<td>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</td>
</tr>
<tr class="odd">
<td><p>Select one of the following:</p>
<p>PV Payment Voucher</p>
<p>Select Transaction Type: PV Payment Voucher</p></td>
</tr>
<tr class="even">
<td><p>Select Payment Voucher Number: PV-688C4522301</p>
<p>FMS Document: PV-688C4522301</p>
<p>Description: Payment Voucher</p>
<p>Status: TRANSMITTED</p>
<p>Created: OCT 14, 1994@10:03:05</p>
<p>This FMS document has been transmitted to FMS.</p>
<p>Press 'RETURN' to continue:</p></td>
</tr>
<tr class="odd">
<td><p>Do you still wish to rebuild and retransmit this Payment Voucher? NO// YES</p>
<p>PONUM=PV-688C4522301</p></td>
</tr>
<tr class="even">
<td><p>The Certified Invoice can now be displayed for your review.</p>
<p>Please review the source document very carefully and take</p>
<p>the appropriate corrective action.</p>
<p>Do you wish to display the source document? YES//</p></td>
</tr>
<tr class="odd">
<td>...Excuse me, Just a moment, please...</td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>INVOICE TRACKING LIST OCT 14,1994 10:53 PAGE 1</p>
<p>--------------------------------------------------------------------------------</p>
<p>ID NUMBER: 198 INVOICE/BILL NUMBER: EZ123</p>
<p>DATE OF INVOICE: OCT 13, 1994 DATE INVOICE RECEIVED: OCT 13, 1994</p>
<p>PROMPT PAY TYPE: NORMAL PURCHASE ORDER POINTER: 688-C45223</p>
<p>VENDOR: GHOST PROGRAMMERS DISCOUNT DAYS: 0</p>
<p>DISCOUNT TERMS: STANDARD APPROVED SHIPPING AMOUNT: $0.00</p>
<p>AMOUNT CERTIFIED FOR PAYMENT: $1,500.00</p>
<p>DATE GOODS/SERVICE RECEIVED: OCT 13, 1994</p>
<p>CERTIFICATION REQUIRED?: YES STATION NUMBER: 688</p>
<p>PURCHASE ORDER NUMBER: 688-C45223 PARTIAL NUMBER: 01</p>
<p>FMS PAYMENT VOUCHER #: 688C4522301 GROSS AMOUNT OF INVOICE: $1,500.00</p>
<p>STATUS: Transaction Complete EXPANDED PO NUMBER: 688-C45223</p>
<p>CURRENT INVOICE LOCATION: FISCAL</p>
<p>D/T CHARGED TO CURRENT LOC: OCT 14, 1994@09:51</p>
<p>DATE RETURNED TO FISCAL: OCT 14, 1994, CERTIFIED FOR PAYMENT BY: IFUSER, TWO</p>
<p>COMPLETED IN ACCOUNTING BY: IFUSER, TWO</p>
<p>CERTIFIED BY VALIDATION CODE: /ES/IFUSER, TWO</p>
<p>COMPLETED BY VALIDATION CODE: /ES/IFUSER, TWO</p>
<p>CHARGED TO CURRENT LOCATION BY: IFUSER, TWO</p>
<p>CERTIFIED BY VALIDATION VER: 1 CERTIFIED BY ESIG CODE: 9058</p>
<p>COMPLETED BY VALIDATION VER: &lt;HIDDEN&gt; COMPLETED BY ESIG CODE: 9058</p>
<p>CERTIFIED BY SIG DATE/TIME: OCT 14, 1994@09:53:04</p>
<p>COMPLETED BY SIG DATE/TIME: OCT 14, 1994@10:02:53</p>
<p>CERTIFYING SERVICE: INFORMATION RESOURCE MGMT</p>
<p>DATE/TIME CHARGED OUT: OCT 13, 1994@17:00</p>
<p>CHARGED BY: IFUSER, TWO</p>
<p>CERTIFYING SERVICE: FISCAL</p>
<p>DATE/TIME CHARGED OUT: OCT 14, 1994@09:51</p>
<p>CHARGED BY: IFUSER, TWO</p>
<p>BOC: 2515 Systems Analysis &amp; Programming (Comm Supplier)</p>
<p>ACCOUNTING LINE AMOUNT: $1,500.00 LIQUIDATION AMOUNT: $1,425.00</p>
<p>LIQUIDATION CODE: PARTIAL FMS LINE #: 1</p>
<p>PROMPT PAYMENT TERMS #: 1 DISCOUNT PERCENT: 5</p>
<p>DISCOUNT DAYS: 15</p>
<p>INVOICE TRACKING LIST OCT 14, 1994@10:53 PAGE 3</p>
<p>-------------------------------------------------------------------------------</p>
<p>PROMPT PAYMENT TERMS #: 2 DISCOUNT PERCENT: NET</p>
<p>DISCOUNT DAYS: 30</p>
<p>Press 'RETURN' to continue:</p></td>
</tr>
<tr class="even">
<td>Do you wish to rebuild and retransmit this FMS document? YES//</td>
</tr>
<tr class="odd">
<td>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</td>
</tr>
<tr class="even">
<td><p>Does this invoice need to be processed by Voucher Audit? NO// (NO)</p>
<p>Status has been changed from 'Transaction Complete'</p>
<p>to 'In Accounting'.</p></td>
</tr>
<tr class="odd">
<td><p>Do you wish to process this invoice at this time? YES// (YES)</p>
<p>Switching to 'Process Invoice in Accounting' Module.</p></td>
</tr>
<tr class="even">
<td><p>Unliquidated obligation amounts and BOCs on this order are:</p>
<p>$1,500.00 2515 Systems Analysis &amp; Programming (Comm Supplier)</p>
<p>Total Invoice Amount Certified for Payment=$1500.00</p></td>
</tr>
<tr class="odd">
<td><p>Select BOC: 2515 Systems Analysis &amp; Programming (Comm Supplier)</p>
<p>//</p>
<p>BOC: 2515 Systems Analysis &amp; Programming (Comm Supplier)</p>
<p>//</p></td>
</tr>
<tr class="even">
<td><p>FMS Line #1</p>
<p>OBLIGATION AMOUNT: 1500.00</p>
<p>ACCOUNTING LINE AMOUNT: 1500//</p>
<p>LIQUIDATION AMOUNT: 1425.00// 1450</p>
<p>LIQUIDATION CODE: PARTIAL//</p></td>
</tr>
<tr class="odd">
<td><p>Select BOC:</p>
<p>OK to process this payment to FMS? NO// Y (YES)</p></td>
</tr>
<tr class="even">
<td>Enter ELECTRONIC SIGNATURE CODE: Thank you.</td>
</tr>
<tr class="odd">
<td><p>Transferring invoice data to PV document for transmission to FMS.</p>
<p>688C4522301</p>
<p>Status has been changed from 'In Accounting'</p>
<p>to 'Transaction Complete'.</p></td>
</tr>
<tr class="even">
<td><p>Select STATION NUMBER ('^' TO EXIT): 688// ^</p>
<p>Returning to 'Process FMS/CAPPS Error Message' Module.</p>
<p>Press 'RETURN' to continue:</p></td>
</tr>
<tr class="odd">
<td><p>FMS Payment Voucher Error Processing</p>
<p>Select Payment Voucher Number: ^</p>
<p>Select Payment Voucher Number: NOT FOUND!</p>
<p>Select one of the following:</p>
<p>PV Payment Voucher</p>
<p>Select Transaction Type: ^</p></td>
</tr>
<tr class="even">
<td><p>Invoice Processing for Payment</p>
<p>Return Invoice to Voucher Audit</p>
<p>PV Payment Voucher (PV) Inquiry</p>
<p>FMS Payment Voucher Error Processing</p>
<p>View Certified Invoice</p>
<p>Select Invoice Processing (ACCTG) Menu Option:</p></td>
</tr>
</tbody>
</table>

# Resolving Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## FMS Error Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FMS documents are generated automatically as a result of certain IFCAP processes. For example, creation and generation of ceiling transactions in IFCAP results in Sub-allowance (SA) documents being created and transmitted to FMS. Additionally, when Accounting obligates purchase orders or invoices for payment, various types of FMS documents are automatically sent to Austin.

In designing the interface with FMS, IFCAP developers have built-in various edit checks to prevent rejection of FMS documents. An example of such functionality is the Required Fields File, explained earlier in this document, which ensures that all fields required for a given fund and type of FMS document are present on that FMS document before transmitting it to FMS. Even so, it is impossible to prevent every scenario that might cause FMS documents to be rejected. It is far less likely that the documents that IFCAP creates automatically will be rejected, compared with the documents that users create manually using the FMS Code Sheet Menu’s Create a Code Sheet option. That is because the automatic document processes contain more built-in protection against document rejection in FMS.

Because rejection of FMS documents is, to some extent, inevitable, there are options in IFCAP to assist users in correction and retransmission of the rejected documents. IFCAP will allow the user to correct errors by correcting the source document, then rebuilding the document and retransmitting it to FMS.

Once FMS has tried to process a document that has been rejected, it will send an error message containing all relevant FMS error codes to the appropriate recipients the following day. Appropriate recipients are those who are defined in the FCP file (420) to receive FMS notifications for their FCP. When the user has corrected a rejected document, the new document will automatically transmit to Austin. The only exceptions are the Budget documents, SA, ST, and AT, which must be generated again with the Generate Budget Code Sheets option of the Fund Distribution Module.

IFCAP transactions being transmitted to the FMS system in Austin are in the form of a mail message.

<span id="_Toc222493063" class="anchor"></span>Figure 33: Outgoing Message to FMS

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: GCS TRANSACTION FMS:SO, VR, IV [#21381] 07 Jul 94 14:55 13</p>
<p>Lines</p>
<p>From: POSTMASTER in 'IN' basket. Page 1</p>
<p>-----------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CTL^IFC^FMS^612^DOC^SO^10 ^612029^612C40011</p>
<p>^19940707^135811^001^001^001^~</p>
<p>BAT^~MO0^612029^~</p>
<p>DOC^~MO1^SO^612C40011 ^10 ^Y^~</p>
<p>MO2^94^07^07^^^^^^M^~</p>
<p>MO3^^^^^^^01^^^^^^^^^^^^^^^^^^^10.00^~</p>
<p>LIN^~MOA^001^^^^94^^0160A1^612^^181000^00^0100201B1^2660^^^^10.00</p>
<p>^D^~{</p>
<p>CTL^IFC^FMS^612^VRQ^ ^ ^</p>
<p>^61294070010^19940707^135931^001^001^001^~</p>
<p>VRQ^940707^135930^612^1981^768765498^^AMER SOCIETY OF ADDICTION</p>
<p>MEDI^5225 WISCONSIN AVENUE N^SUITE 409^WASHINGTON^DC^20015^T^Y^C^N^A^~{</p>
<p>CTL^IFC^FMS^612^DOC^IV^10 ^ ^612I40004</p>
<p>^19940707^140821^001^001^001^~</p>
<p>DOC^~IV1^IV^612I40004 ^10 ^Y^~</p>
<p>IV2^94^07^07^^^^^E^^^^^^^^^^^^94411020035^340.00^~</p>
<p>LIN^~IVA^001^189.60^I^^^^^612^^^^^^^^SFCS^^^06^^^94^^0160A1^612^^</p>
<p>844100^00^19EA</p>
<p>40200^2660^~IVB^01^~</p>
<p>LIN^~IVA^002^150.40^I^^^^^612^^^^^^^^SFPR^^^07^^^94^^0160A1^612^^</p>
<p>844100^00^19EA</p>
<p>40200^2660^~IVB^01^~ {</p></td>
</tr>
<tr class="even">
<td>Select MESSAGE Action: DELETE (from IN basket)// S</td>
</tr>
<tr class="odd">
<td>Select BASKET:</td>
</tr>
</tbody>
</table>

Once a message is received in the FMS system, a mail message is returned to the site confirming acceptance of the message.

Confirmation Message returning from Austin:

<span id="_Toc222493064" class="anchor"></span>Figure 34: Confirmation Message Returning from Austin

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: EDO1381 FMS CONFIRMATION [#21382] 07 JUL 94 14:08 CST 2</p>
<p>Lines</p>
<p>From: &lt;POSTMASTER@FOC-AUSTIN.VA.GOV&gt; in 'IN' basket. Page 1</p>
<p>-----------------------------------------------------------------</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Ref: Your FMS message #21381 with Austin ID #38883674,</p>
<p>is assigned confirmation number 941881357664928.</p></td>
</tr>
<tr class="even">
<td>Select MESSAGE Action: DELETE (from IN basket)// S</td>
</tr>
<tr class="odd">
<td>Select BASKET:</td>
</tr>
</tbody>
</table>

If FMS rejects a document from IFCAP, the FMS mail group will receive an electronic mail message from FMS notifying them of the rejected document. The message will include the FMS error code, along with a brief description of the error. The action the user must take to correct the rejected document varies according to the type of document that has rejected. See the *FMS Handbook* for a list of FMS error codes.

## Stack Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accounting Technician Menu has an option to allow inquiry into all documents and give users the status on each document. The data can be gathered by document type, status or a group of status. The user can see the document with or without code sheet information.

<span id="_Toc222493065" class="anchor"></span>Figure 35: Confirmation Message Returning from Austin

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Fund Distribution &amp; Accounting Menu Option: Accounting Technician Menu</p>
<p>Document Processing Menu ...</p>
<p>Accounting Utilities Menu ...</p>
<p>Reprint Menu ...</p>
<p>FMS Code Sheet Menu ...</p>
<p>Select Accounting Technician Menu Option: FMS Code Sheet Menu</p>
<p>Code Sheet Edit</p>
<p>Create a Code Sheet</p>
<p>Delete a Code Sheet</p>
<p>Keypunch a Code Sheet</p>
<p>Purge Transmission Records/Code Sheets</p>
<p>Retransmit Stack File Document</p>
<p>Review a Code Sheet</p>
<p>Stack Status Report</p>
<p>Select FMS Code Sheet Menu Option: STACK Status Report</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>START with TRANSACTION CODE: FIRST// SA</p>
<p>END with TRANSACTION CODE: LAST// ST</p></td>
</tr>
<tr class="even">
<td>Print documents created after DATE: JAN 1,1993// 7/4 (JUL 04,1994)</td>
</tr>
<tr class="odd">
<td><p>Select one of the following:</p>
<p>Q QUEUED FOR TRANSMISSION</p>
<p>M MARKED FOR IMMEDIATE TRANSMISSION BY EVENT</p>
<p>T TRANSMITTED</p>
<p>E ERROR DURING TRANSMISSION</p>
<p>A ACCEPTED BY FMS</p>
<p>R REJECTED BY FMS</p>
<p>N TRANSMITTED WITH NO CONFIRMATION MESSAGE RETURNED</p></td>
</tr>
<tr class="even">
<td>Select STATUS(s) to display: REJECTED BY FMS</td>
</tr>
<tr class="odd">
<td><p>Select one of the following:</p>
<p>Q QUEUED FOR TRANSMISSION</p>
<p>M MARKED FOR IMMEDIATE TRANSMISSION BY EVENT</p>
<p>T TRANSMITTED</p>
<p>E ERROR DURING TRANSMISSION</p>
<p>A ACCEPTED BY FMS</p>
<p>R REJECTED BY FMS</p>
<p>N TRANSMITTED WITH NO CONFIRMATION MESSAGE RETURNED</p></td>
</tr>
<tr class="even">
<td>Select STATUS(s) to display:</td>
</tr>
<tr class="odd">
<td><p>SELECTED STATUS(s) to display:</p>
<p>REJECTED BY FMS</p>
<p>Print DESCRIPTION of event? NO// Y (YES)</p>
<p>Print DOCUMENT code sheets? NO// (NO)</p>
<p>DEVICE: HOME// TELNET RIGHT MARGIN: 80// LAT</p></td>
</tr>
<tr class="even">
<td>&lt;*&gt; please wait &lt;*&gt;</td>
</tr>
<tr class="odd">
<td><p>GCS STACK FILE STATUS REPORT JUL 08, 1994@11:40:51 PAGE 1</p>
<p>TC TRAN CODE BATNUM DATE@TIME CREATED STATUS</p>
<p>SO 612A40024 JUL 05, 1994@12:18:59 REJECTED BY FMS</p>
<p>DESCR: Purchase Order Obligation</p>
<p>MAIL MSGS: 21291 CONFIRMATION:</p>
<p>TOTAL CODE SHEETS: 1</p></td>
</tr>
<tr class="even">
<td><p>Select FMS Code Sheet Menu Option: Stack Status Report</p>
<p>START with TRANSACTION CODE: FIRST// PV</p>
<p>END with TRANSACTION CODE: LAST// PVZ</p>
<p>Print documents created after DATE: JAN 1,1993//6/19 (JUN 19, 1994)</p></td>
</tr>
<tr class="odd">
<td><p>Select one of the following:</p>
<p>Q QUEUED FOR TRANSMISSION</p>
<p>M MARKED FOR IMMEDIATE TRANSMISSION BY EVENT</p>
<p>T TRANSMITTED</p>
<p>E ERROR DURING TRANSMISSION</p>
<p>A ACCEPTED BY FMS</p>
<p>R REJECTED BY FMS</p>
<p>N TRANSMITTED WITH NO CONFIRMATION MESSAGE RETURNED</p></td>
</tr>
<tr class="even">
<td>Select STATUS(s) to display: REJECTED BY FMS</td>
</tr>
<tr class="odd">
<td><p>Select one of the following:</p>
<p>Q QUEUED FOR TRANSMISSION</p>
<p>M MARKED FOR IMMEDIATE TRANSMISSION BY EVENT</p>
<p>T TRANSMITTED</p>
<p>E ERROR DURING TRANSMISSION</p>
<p>A ACCEPTED BY FMS</p>
<p>R REJECTED BY FMS</p>
<p>N TRANSMITTED WITH NO CONFIRMATION MESSAGE RETURNED</p></td>
</tr>
<tr class="even">
<td>Select STATUS(s) to display:</td>
</tr>
<tr class="odd">
<td><p>SELECTED STATUS(s) to display:</p>
<p>REJECTED BY FMS</p>
<p>Print DESCRIPTION of event? NO// Y (YES)</p>
<p>Print DOCUMENT code sheets? NO// Y (YES)</p>
<p>DEVICE: HOME// LAT</p></td>
</tr>
<tr class="even">
<td>&lt;*&gt; please wait &lt;*&gt;</td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>GCS STACK FILE STATUS REPORT JUL 25, 1994@15:11:02 PAGE 1</p>
<p>TC-TRAN CODE -BATNUM DATE@TIME CREATED STATUS</p>
<p>------------------------------------------------------------------------------</p>
<p>PV-612C4500800 JUN 20, 1994@14:49:04 REJECTED BY FMS</p>
<p>DESCR: WASH ISC TESTING PV</p>
<p>MAIL MSGS: 19520 CONFIRMATION:</p>
<p>* ACTUAL CODE SHEET:</p>
<p>CTL^IFC^FMS^612^DOC^PV^10 ^ ^612C4500800^19940620^144904^001^001^001^~</p>
<p>DOC^~PV1^PV^612C4500800^10 ^~</p>
<p>PV2^06^05^94^^^^^E^01^^^^^^^^^^THISISFAKE^^1.00^~</p>
<p>PV3^^^^^^^^^^^^^TEST 1^^^^^^^^X^^^~</p>
<p>LIN^~</p>
<p>PVA^001^SO^612C45008 ^001^94^06^02^^^^^^^^^^^^^^^^^^^^94^06^05^^10000.00^I^P^9</p>
<p>4^05^21^^^~</p>
<p>PVB^^^^^^^1.00^~</p>
<p>* END OF CODE SHEET *</p>
<p>TOTAL CODE SHEETS: 1</p></td>
</tr>
</tbody>
</table>

## FMS Inquiry Rejected Obligation Documents Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FMS Inquiry Rejected Obligation Documents menu allows correction of errors to any (MO or SO) document by reviewing and editing the original purchase order or 1358 document. Once edited the document is rebuilt and transmitted to FMS.

<span id="_Toc222493066" class="anchor"></span>Figure 36: Menu Path and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Accounting Technician Menu</p>
<p>Document Processing Menu ...</p>
<p>Accounting Utilities Menu ...</p>
<p>Reprint Menu ...</p>
<p>Receiving Report Transmission Menu ...</p>
<p>FMS Code Sheet Menu ...</p>
<p>Select Accounting Technician Menu Option: DOCument Processing Menu</p>
<p>1358 Processing Menu ...</p>
<p>Amendment Processing</p>
<p>General Post Funds Requests Processing</p>
<p>Invoice Processing (ACCTG) Menu ...</p>
<p>Obligation Processing</p>
<p>Process Receiving Report</p>
<p>Return Purchase Order to Supply</p>
<p>Return PO Amendment to Supply</p>
<p>Stacked Fiscal Documents Menu ...</p>
<p>FMS Rejected Obligation Document Processing ...</p>
<p>Select Document Processing Menu Option: FMS Rejected Obligation</p>
<p>Document Processing</p>
<p>FMS Inquiry Rejected Obligation Documents ...</p>
<p>FMS Rebuild/Transmit Rejected Obligation Documents ...</p>
<p>Select FMS Rejected Obligation Document Processing Option: FMS Inquiry Rejected Obligation Documents</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>MO/SO Rejected Document Inquiry for P.O.</p>
<p>SO Rejected Document Inquiry for 1358s</p>
<p>Select FMS Inquiry Rejected Obligation Documents Option: MO/SO</p>
<p>Rejected Document Inquiry for P.O.</p></td>
</tr>
<tr class="even">
<td><p>MO/SO Rejected Document Inquiry for P.O.</p>
<p>Select STATION NUMBER ('^' TO EXIT): 542// 612 MARTINEZ, CA</p>
<p>Select one of the following:</p>
<p>MO Miscellaneous Order</p>
<p>SO Service Order</p>
<p>Select Transaction Type: SO Service Order</p>
<p>Select Stack Document for Inquiry: A40024 SO-612A40024</p>
<p>FMS Document: SO-612A40024</p>
<p>Description: Purchase Order Obligation</p>
<p>Status: REJECTED BY FMS</p>
<p>Created: JUL 5, 1994@12:18:59</p>
<p>This FMS document has been rejected due to one or more errors.</p>
<p>The Certified Invoice will now be displayed for your review.</p>
<p>Please review the source document very carefully and take</p>
<p>the appropriate corrective action.</p>
<p>Press 'RETURN' to continue</p></td>
</tr>
<tr class="odd">
<td><p>PURCHASE ORDER: 612-A40024 STATUS: Transaction Complete</p>
<p>M.O.P.: CERTIFIED INVOICE LAST PARTIAL RECD.:</p>
<p>REQUESTING SERVICE: PPM</p>
<p>VENDOR: IFVENDOR LEASE INC SHIP TO: Warehouse</p>
<p>U.S. HIGHWAY #1 V.A. Medical Center</p>
<p>FAIRLESS HILLS, PA 19030 8403 Colesville Rd</p>
<p>800 555 5555 Silver SPRING, MD 20910</p>
<p>DELIVERY HOURS:</p>
<p>8:00 AM - 4:30 PM</p>
<p>______________________________________________________________________________</p>
<p>FOB POINT: DESTINATION |PROPOSAL: N/A |AUTHORITY:</p>
<p>COST CENTER: 161000 | | FAR 13</p>
<p>TYPE: PURCHASE ORDER | |AGENT:</p>
<p>DELIVER ON/BEFORE 7/15/94 |CONTRACT: | IFUSER, THREE</p>
<p>DISCOUNT TERM: NET30 | |DATE: 7/5/94</p>
<p>APP: 364/50161.001-120 | |ESTIMATED</p>
<p>| |TOTAL: 3.00</p>
<p>------------------------------------------------------------------------------</p>
<p>ENTER '^' TO HALT:</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>------------------------------------------------------------------------------</p>
<p>1 TEST 1 EA 3.00 3.00</p>
<p>* ESTIMATED PURCHASE ORDER *</p></td>
</tr>
<tr class="even">
<td><p>Select Stack Document for Inquiry:</p>
<p>Select Stack Document for Inquiry: NOT FOUND!</p>
<p>Select one of the following:</p>
<p>MO Miscellaneous Order</p>
<p>SO Service Order</p></td>
</tr>
</tbody>
</table>

<span id="_Toc222493067" class="anchor"></span>Figure 37: Enter Parameters and Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Transaction Type:</p>
<p>MO/SO Rejected Document Inquiry for P.O.</p>
<p>SO Rejected Document Inquiry for 1358s</p>
<p>Select FMS Inquiry Rejected Obligation Documents Option:</p>
<p>capture 3B. FMS Rebuild/Transmit Rejected Obligation Documents...</p>
<p>Select FMS Rejected Obligation Document Processing Option: FMS</p>
<p>REbuild/Transmit Rejected Obligation Documents</p>
<p>MO/SO Rebuild/Transmit for P.O.</p>
<p>SO Rebuild/Transmit for 1358s</p>
<p>Select FMS Rebuild/Transmit Rejected Obligation Documents Option: MO/SO Rebuild/Transmit for P.O.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>MO/SO Rebuild/Transmit for P.O.</p>
<p>Select STATION NUMBER ('^' TO EXIT): 542// 612 MARTINEZ, CA</p>
<p>Select one of the following:</p>
<p>MO Miscellaneous Order</p>
<p>SO Service Order</p>
<p>Select Transaction Type: MO Miscellaneous Order</p>
<p>Select Stack Document for Rebuild/Transmit: A40030</p>
<p>1 A40030 MO-612A40030</p>
<p>2 A40030 MO-612A40030 -612036</p>
<p>3 A40030 MO-612A40030 -612038</p>
<p>4 A40030 MO-612A40030 -612039</p>
<p>5 A40030 MO-612A40030 -612040</p>
<p>CHOOSE 1-5: 1 MO-612A40030</p></td>
</tr>
<tr class="even">
<td><p>FMS Document: MO-612A40030</p>
<p>Description: Purchase Order Obligation Rebuild/Transmit</p>
<p>Status: REJECTED BY FMS</p>
<p>Created: JUL 11, 1994@16:42:54</p>
<p>This FMS document has been rejected due to one or more errors.</p>
<p>The Purchase Order can now be displayed for your review.</p>
<p>Please review the source document very carefully and take appropriate corrective action.</p>
<p>Do you wish to display the source document? YES// YES</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>PURCHASE ORDER: 612-A40030 STATUS: Complete Order Received (Amended)</p>
<p>M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.: 1 07/11/94</p>
<p>REQUESTING SERVICE: SUPPLY</p>
<p>VENDOR: IFVENDOR MANUFACTURING CO SHIP TO: Warehouse</p>
<p>28200 A Road V.A. Medical Center</p>
<p>ROMULUS, MI 23456 8403 Colesville Rd</p>
<p>656 555 5555 Silver Spring, MD 20910</p>
<p>DELIVERY HOURS:</p>
<p>8:00 AM - 4:30 PM</p>
<p>DELIVERY LOCATION: SUPPLY</p></td>
</tr>
<tr class="odd">
<td><p>______________________________________________________________________________</p>
<p>FOB POINT: ORIGIN |PROPOSAL: N/A |AUTHORITY:</p>
<p>COST CENTER: 844100 | | FAR 13</p>
<p>TYPE: PURCHASE ORDER | |AGENT:</p>
<p>DELIVER ON/BEFORE 7/21/94 |CONTRACT: | IFAGENT 2</p>
<p>DISCOUNT TERM: NET30 | |DATE: 7/11/94</p>
<p>APP: 3640160.001.01-1102 | |</p>
<p>| |TOTAL: 18871.11</p>
<p>------------------------------------------------------------------------------</p>
<p>ENTER '^' TO HALT:</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>------------------------------------------------------------------------------</p>
<p>1 LOTS OF GOOD STUFF 110 EA 155.5555 17111.11</p>
<p>NSN: 7510-00-123-7777</p>
<p>QTY PREV RCVD: 100</p>
<p>PARTIAL NO.: 1</p>
<p>Items per EA: 1</p>
<p>3 GOOD STUFF 10 EA 150.00 1500.00</p>
<p>Items per EA: 1</p>
<p>4 MORE GOOD STUFF 10 EA 25.00 250.00</p>
<p>Items per EA: 1</p>
<p>5 EST. SHIPPING AND/OR HANDLING 10.00</p>
<p>IFCAP Training</p>
<p>V.A. TRANSACTION NUMBERS:</p>
<p>612-94-4-1102-0044</p>
<p>AMENDMENT NUMBER: 1 EFFECTIVE DATE: 7/11/94</p>
<p>ENTER '^' TO HALT:</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>------------------------------------------------------------------------------</p>
<p>*ADDED THROUGH AMENDMENT*</p>
<p>Item No. 3 Item Master File No.</p>
<p>GOOD STUFF</p>
<p>Items per EA: NSN:</p>
<p>10 EA at $ 150.0000 = $ 1500.00</p>
<p>AMENDMENT NUMBER: 2 EFFECTIVE DATE: 7/11/94</p>
<p>Currently:</p>
<p>Item No. 1 Item Master File No. 5505</p>
<p>LOTS OF GOOD STUFF</p>
<p>Items per EA: 1 NSN: 7510-00-123-7777</p>
<p>110 EA at $ 150.00 = $ 16500.00</p>
<p>ENTER '^' TO HALT:</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>------------------------------------------------------------------------------</p>
<p>Will now be AMENDED to read:</p>
<p>Item No. 1 Item Master File No. 5505</p>
<p>LOTS OF GOOD STUFF</p>
<p>Items per EA: 1 NSN: 7510-00-123-7777</p>
<p>110 EA $ 155.5555 = $ 17111.11</p>
<p>AMENDMENT NUMBER: 3 EFFECTIVE DATE: 7/12/94</p>
<p>*ADDED THROUGH AMENDMENT*</p>
<p>Item No. 4 Item Master File No.</p>
<p>MORE GOOD STUFF</p>
<p>Items per EA: 1 NSN:</p>
<p>10 EA at $ 25.0000 = $ 250.00</p>
<p>AMENDMENT NUMBER: 4 EFFECTIVE DATE: 7/12/94</p>
<p>ENTER '^' TO HALT:</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>------------------------------------------------------------------------------</p>
<p>Currently:</p>
<p>Item No. 1 Item Master File No. 5505</p>
<p>LOTS OF GOOD STUFF</p>
<p>Items per EA: 1 NSN: 7510-00-123-7777</p>
<p>100 EA at $ 155.56 = $ 15555.55</p>
<p>Will now be AMENDED to read:</p>
<p>Item No. 1 Item Master File No. 5505</p>
<p>LOTS OF GOOD STUFF</p>
<p>Items per EA: 1 NSN: 7510-00-123-7777</p>
<p>110 EA $ 155.5555 = $ 17111.11</p></td>
</tr>
<tr class="even">
<td><p>Review a Receiving Report? NO// (NO)</p>
<p>Do you wish to rebuild and retransmit this FMS document? YES//</p></td>
</tr>
<tr class="odd">
<td><p>PURCHASE ORDER - 612-A40030</p>
<p>COST CENTER: 844100 CONTROL POINT: 1102 MED CARE TEST2</p>
<p>BOC #1: 2660 AMOUNT: $ 18861.11</p>
<p>BOC #2: 2661 AMOUNT: $ 0.00</p>
<p>BOC #3: 2660 AMOUNT: $ 10.00</p>
<p>Justification(s):</p>
<p>Transaction Number: 612-94-4-1102-0044</p>
<p>Required for recreational activities in employee wellness.</p></td>
</tr>
<tr class="even">
<td><p>The information listed above is recorded in this PURCHASE ORDER.</p>
<p>Is the above information correct? YES// NO</p>
<p>Should the Cost Center or BOC information be edited at this time? NO// YES</p></td>
</tr>
<tr class="odd">
<td><p>...now editing the Cost Center...</p>
<p>COST CENTER: 844100//</p>
<p>...now editing the BOCs...</p>
<p>Do you wish to assign the same BOC to ALL items? NO//</p>
<p>Do you wish to edit specific line items? YES//</p>
<p>Select ITEM: 1 LOTS OF GOOD STUFF</p>
<p>STK#: NSN: 7510-00-123-7777</p>
<p>BOC: 2660 Operating Supplies and Ma Replace ... With 2661</p>
<p>Replace</p>
<p>2661 Expendable Furniture and</p>
<p>2661 Expendable Furniture and Fixtures and Decoras</p>
<p>Select ITEM:</p>
<p>...now recalculating FMS commodity lines...</p>
<p>PURCHASE ORDER - 612-A40030</p>
<p>COST CENTER: 844100 CONTROL POINT: 1102 MED CARE TEST2</p>
<p>BOC #1: 2660 AMOUNT: $ 1750.00</p>
<p>BOC #2: 2661 AMOUNT: $ 17111.11</p>
<p>BOC #3: 2660 AMOUNT: $ 10.00</p>
<p>Justification(s):</p>
<p>Transaction Number: 612-94-4-1102-0044</p>
<p>Required for recreational activities in employee</p>
<p>wellness.</p>
<p>The information listed above is recorded on this PURCHASE ORDER.</p></td>
</tr>
<tr class="even">
<td>Is the above information correct? YES//</td>
</tr>
<tr class="odd">
<td><p>Net Cost of Order: $ 18871.11</p>
<p>Control Point Balances</p>
<p>Uncommitted Balance: $ 166962.85</p>
<p>Unobligated Balance: $ 174399.35</p>
<p>Committed, Not Obligated: $ 7436.50</p>
<p>OK to Continue? YES// YES</p></td>
</tr>
<tr class="even">
<td><p>Select Obligation Processing Date: JUL 11,1994// (JUL 11, 1994)</p>
<p>This Purchase Order Obligation will now generate the</p>
<p>Original Entry Miscellaneous Order (MO) Document. The MO Document</p>
<p>will be marked for transmission to FMS.</p>
<p>Transmit this Document to FMS? YES//</p></td>
</tr>
<tr class="odd">
<td><p>The Electronic Signature must now be entered to generate the MO Document.</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p></td>
</tr>
<tr class="even">
<td><p>...now generating the FMS Miscellaneous Order (MO) Document..</p>
<p>...HMMM, LET ME THINK ABOUT THAT A MOMENT...</p>
<p>Select Stack Document for Rebuild/Transmit:</p>
<p>Select Stack Document for Rebuild/Transmit: NOT FOUND!</p>
<p>Select one of the following:</p>
<p>MO Miscellaneous Order</p>
<p>SO Service Order</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Select Transaction Type:</p>
<p>MO/SO Rebuild/Transmit for P.O.</p>
<p>SO Rebuild/Transmit for 1358s</p>
<p>Select FMS Rebuild/Transmit Rejected Obligation Documents Option:</p>
<p>FMS Inquiry Rejected Obligation Documents ...</p>
<p>FMS Rebuild/Transmit Rejected Obligation Documents ...</p>
<p>Select FMS Rejected Obligation Document Processing Option:</p></td>
</tr>
</tbody>
</table>

## Payment Error Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Payment Vouchers (PVs) transmitted to FMS are sometimes rejected by FMS. The Accounting Technician has two options to help view and correct such documents and return corrected document to FMS for processing.

<span id="_Toc222493068" class="anchor"></span>Figure 38: Payment Voucher Inquiry

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Accounting Technician Menu</p>
<p>Document Processing Menu ...</p>
<p>Accounting Utilities Menu ...</p>
<p>Reprint Menu ...</p>
<p>Receiving Report Transmission Menu ...</p>
<p>FMS Code Sheet Menu ...</p>
<p>Select Accounting Technician Menu Option: DOCument Processing</p>
<p>Menu</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The system can now generate a report that will list the type and</p>
<p>number of each document that is ready for processing at this</p>
<p>time.</p>
<p>But it may take a while to complete.</p>
<p>Do you want to run the report at this time? NO//</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><p>1358 Processing Menu ...</p>
<p>Amendment Processing</p>
<p>General Post Funds Requests Processing</p>
<p>Invoice Processing (ACCTG) Menu ...</p>
<p>Obligation Processing</p>
<p>Process Receiving Report</p>
<p>Return Purchase Order to Supply</p>
<p>Return PO Amendment to Supply</p>
<p>Stacked Fiscal Documents Menu ...</p>
<p>FMS Rejected Obligation Document Processing ...</p>
<p>Select Document Processing Menu Option: INVoice Processing</p></td>
</tr>
<tr class="even">
<td><p>(ACCTG) Menu</p>
<p>Invoice Processing for Payment</p>
<p>Return Invoice to Voucher Audit</p>
<p>PV Payment Voucher (PV) Inquiry</p>
<p>FMS Payment Voucher Error Processing</p>
<p>View Certified Invoice</p>
<p>Select Invoice Processing (ACCTG) Menu Option: PAYment Voucher</p>
<p>(PV) Inquiry</p></td>
</tr>
<tr class="odd">
<td><p>Payment Voucher (PV) Inquiry</p>
<p>Select STATION NUMBER ('^' TO EXIT): 542// 612 MARTINEZ, CA</p>
<p>Select one of the following:</p>
<p>PV Payment Voucher</p>
<p>Select Transaction Type: PV Payment Voucher</p></td>
</tr>
<tr class="even">
<td><p>Payment Voucher NumberC40011 PV-612C4001100</p>
<p>FMS Document: PV-612C4001100</p>
<p>Description: Payment Voucher</p>
<p>Status: REJECTED BY FMS</p>
<p>Created: JUL 7, 1994@13:55:02</p>
<p>This FMS document has been rejected due to one or more errors.</p>
<p>The Certified Invoice will now be displayed for your review.</p>
<p>Please review the source document very carefully and take</p>
<p>the appropriate corrective action.</p>
<p>Press 'RETURN' to continue:</p></td>
</tr>
<tr class="odd">
<td>...Alright, I'm tired. Please hold on...</td>
</tr>
<tr class="even">
<td><p>INVOICE TRACKING LIST JUL 26,1994 09:09 PAGE 1</p>
<p>------------------------------------------------------------------------------</p>
<p>ID NUMBER: 40075 INVOICE/BILL NUMBER: 123</p>
<p>DATE OF INVOICE: JUL 7, 1994, DATE INVOICE RECEIVED: JUL 7, 1994</p>
<p>INVOICE TYPE: NORMAL PURCHASE ORDER POINTER: 612-C40011</p>
<p>VENDOR: IFVENDOR CONSTRUCTION CO DISCOUNT DAYS: 0</p>
<p>DISCOUNT TERMS: STANDARD AMOUNT CERTIFIED FOR PAYMENT: $110.00</p>
<p>DATE GOODS/SERVICE RECEIVED: JUL 7, 1994</p>
<p>CERTIFICATION REQUIRED?: YES STATION NUMBER: 612</p>
<p>PURCHASE ORDER NUMBER: 612-C40011 FMS PAYMENT VOUCHER #: 612C4001100</p>
<p>GROSS AMOUNT OF INVOICE: $110.00 NET DAYS: 30</p>
<p>STATUS: Transaction Complete EXPANDED PO NUMBER: 612-C40011</p>
<p>CURRENT INVOICE LOCATION: FISCAL</p>
<p>D/T CHARGED TO CURRENT LOC: JUL 7, 1994@13:53</p>
<p>DATE RETURNED TO FISCAL: JUL 7, 1994, CERTIFIED FOR PAYMENT BY: IFUSER, THREE</p>
<p>COMPLETED IN ACCOUNTING BY: IFUSER, THREE</p>
<p>CERTIFIED BY VALIDATION CODE: /ES/IFUSER, THREE</p>
<p>COMPLETED BY VALIDATION CODE: /ES/IFUSER, THREE</p>
<p>INVOICE TRACKING LIST JUL 26, 1994@09:09 PAGE 2</p>
<p>------------------------------------------------------------------------------</p>
<p>CHARGED TO CURRENT LOCATION BY: IFUSER, THREE</p>
<p>CERTIFIED BY VALIDATION VER: 1 CERTIFIED BY ESIG CODE: 5711</p>
<p>COMPLETED BY VALIDATION VER: &lt;HIDDEN&gt; COMPLETED BY ESIG CODE: 5711</p>
<p>CERTIFIED BY SIG DATE/TIME: JUL 7, 1994@13:53:43</p>
<p>COMPLETED BY SIG DATE/TIME: JUL 7, 1994@13:55</p>
<p>CERTIFYING SERVICE: FISCAL</p>
<p>DATE/TIME CHARGED OUT: JUL 7, 1994@13:53</p>
<p>CHARGED BY: IFUSER, THREE</p>
<p>CERTIFYING SERVICE: FISCAL</p>
<p>DATE/TIME CHARGED OUT: JUL 7, 1994@13:53</p>
<p>CHARGED BY: IFUSER, THREE</p>
<p>BOC: 2660 Operating Supplies and Materials</p>
<p>ACCOUNTING LINE AMOUNT: $120.00 LIQUIDATION AMOUNT: $110.00</p>
<p>LIQUIDATION CODE: PARTIAL FMS LINE #: 1</p>
<p>PROMPT PAYMENT TERMS #: 1 DISCOUNT PERCENT: NET</p>
<p>DISCOUNT DAYS: 30</p>
<p>Press 'RETURN' to continue:</p></td>
</tr>
<tr class="odd">
<td><p>Payment Voucher Number</p>
<p>Payment Voucher Number NOT FOUND!</p>
<p>Select one of the following:</p>
<p>PV Payment Voucher</p>
<p>Select Transaction Type:</p></td>
</tr>
<tr class="even">
<td><p>Invoice Processing for Payment</p>
<p>Return Invoice to Voucher Audit</p>
<p>PV Payment Voucher (PV) Inquiry</p>
<p>FMS Payment Voucher Error Processing</p>
<p>View Certified Invoice</p></td>
</tr>
</tbody>
</table>

<span id="_Toc222493069" class="anchor"></span>Figure 39: FMS Payment Voucher Error Processing

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Invoice Processing (ACCTG) Menu Option: FMS Payment</p>
<p>Voucher Error Processing</p>
<p>FMS Payment Voucher Error Processing</p>
<p>Select Payment Voucher Number: PV-612C4001100</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FMS Document: PV-612C4001100</p>
<p>Description: Payment Voucher</p>
<p>Status: REJECTED BY FMS</p>
<p>Created: JUL 7, 1994@13:55:02</p>
<p>This FMS document has been rejected due to one or more errors.</p>
<p>PONUM=PV-612C4001100</p>
<p>The Certified Invoice can now be displayed for your review.</p>
<p>Please review the source document very carefully and take</p>
<p>the appropriate corrective action.</p>
<p>Do you wish to display the source document? YES// NO</p></td>
</tr>
<tr class="even">
<td><p>Do you wish to rebuild and retransmit this FMS document? YES//</p>
<p>Select STATION NUMBER ('^' TO EXIT): 612// MARTINEZ, CA</p>
<p>Does this invoice need to be processed by Voucher Audit? NO// Y (YES)</p>
<p>ARE YOU SURE? YES// (YES)</p></td>
</tr>
<tr class="odd">
<td><p>Status has been changed from 'Transaction Complete'</p>
<p>to 'Awaiting Voucher Audit Review'.</p>
<p>Press 'RETURN' to continue:</p></td>
</tr>
<tr class="even">
<td><p>Select Payment Voucher Number: PV-612C4001100</p>
<p>FMS Document: PV-612C4001100</p>
<p>Description: Payment Voucher</p>
<p>Status: REJECTED BY FMS</p>
<p>Created: JUL 7, 1994@13:55:02</p>
<p>This FMS document has been rejected due to one or more errors.</p>
<p>PONUM=PV-612C4001100</p>
<p>The Certified Invoice can now be displayed for your review.</p>
<p>Please review the source document very carefully and take</p>
<p>the appropriate corrective action.</p></td>
</tr>
<tr class="odd">
<td><p>Do you wish to display the source document? YES// NO</p>
<p>Do you wish to rebuild and retransmit this FMS document? YES//</p>
<p>Select STATION NUMBER ('^' TO EXIT): 612// MARTINEZ, CA</p>
<p>Does this invoice need to be processed by Voucher Audit? NO// (NO)</p>
<p>Status has been changed from 'Awaiting Voucher Audit Review'</p>
<p>to 'In Accounting'.</p>
<p>Do you wish to process this invoice at this time? YES// (YES)</p>
<p>Switching to 'Process Invoice in Accounting' Module.</p></td>
</tr>
<tr class="even">
<td><p>Unliquidated obligation amounts and BOCs on this order are:</p>
<p>$110.00 2660 Operating Supplies and Materials</p>
<p>Total Invoice Amount Certified for Payment=$110.00</p>
<p>Select BOC: 2660 Operating Supplies and Materials</p>
<p>//</p>
<p>BOC: 2660 Operating Supplies and Materials//</p>
<p>FMS Line #1</p>
<p>ACCOUNTING LINE AMOUNT: 120.00// 110.00</p>
<p>LIQUIDATION AMOUNT: 110.00//</p>
<p>LIQUIDATION CODE: PARTIAL//</p>
<p>Select BOC:</p>
<p>OK to process this payment to FMS? NO// Y (YES)</p>
<p>Enter ELECTRONIC SIGNATURE CODE: Thank you.</p>
<p>Transferring invoice data to PV documents for transmission to FMS.</p>
<p>Returning to 'Process FMS/CAPPS Error Message' Module.</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>FMS Payment Voucher Error Processing</p>
<p>Select Payment Voucher Number:</p>
<p>Select Payment Voucher Number: NOT FOUND!</p>
<p>Select one of the following:</p>
<p>PV Payment Voucher</p>
<p>Select Transaction Type:</p>
<p>Invoice Processing for Payment</p>
<p>Return Invoice to Voucher Audit</p>
<p>PV Payment Voucher (PV) Inquiry</p>
<p>FMS Payment Voucher Error Processing</p>
<p>View Certified Invoice</p>
<p>Select Invoice Processing (ACCTG) Menu Option:</p></td>
</tr>
</tbody>
</table>

# # Purchase Card Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purchase Card Transaction Print Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purchase Card Transaction Print menu has a number of options that assist the accounting technician with the monitoring of the Purchase Card program.

## Detailed Report of Unpaid PC Transactions by FCP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the unpaid purchase card total for each control point.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222493070" class="anchor"></span>Figure 40: Detailed Report of Unpaid PC Transactions by FCP

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Purchase Card Transactions Print Menu Option: detailed Report of Unpaid PC Transactions by FCP</p>
<p>Please select a device for printing this report.</p>
<p>DEVICE: UCX/TELNET Right Margin: 80//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DETAILED REPORT UNPAID PURCHASE CARD TRANSACTIONS BY FCP PAGE: 1</p>
<p>FCP PC NUMBER BUYER VENDOR</p>
<p>AMOUNT PURCHASE DATE COST CENTER BUDGET OBJECT CODE</p>
<p>FIRST LINE-ITEM DESCRIPTION</p>
<p>STATUS</p>
<p>-------------------------------------------------------------------</p>
<p>020 688-P80076 IFUSER, TWO K MEDLINE INDUSTRIES INC</p>
<p>70.00 SEP 02, 1998, 840500 2660 Operating Suppl</p>
<p>HEPARIN SODIUM INJECTION USP 1000 UNITS PER ML 30ML DERIVED</p>
<p>Ordered (No Fiscal Action Required)</p>
<p>020 688-P65054 LUCE, RANDY ADDRESSOGRAPH FARRINGTON/DATAC</p>
<p>10987.00 SEP 02, 1998, 840500 2424 Other Printing</p>
<p>DESCRIPTION</p>
<p>Ordered (No Fiscal Action Required)</p>
<p>020 688-P75198 LUCE, RANDY CERAMIC BARN</p>
<p>180.00 SEP 02, 1998, 840500 2220 Other Shipments</p>
<p>TEST ITEM</p>
<p>Ordered (No Fiscal Action Required)</p>
<p>CONTROL POINT 20 SUBTOTAL: 11237.00</p>
<p>036 688-P05176 IFVENDOR, TEN III PHD DVMIFVENDOR, ONE</p>
<p>27.60 MAY 01, 2000, 828100 2660 Operating Suppl</p>
<p>WOODEN WIDGETS-PINE-PAINTED</p>
<p>Ordered (No Fiscal Action Required)</p>
<p>036 688-P85010 IFUSER, TWO K GENERAL MEDICAL</p>
<p>62.90 OCT 27, 1997, 828100 2632 Other Medical a</p>
<p>GAUZE, PETROLATUM, STERILE INDIVIDUAL PACK WHITE ABSORBENT 1 X 36</p>
<p>Complete Order Received</p>
<p>CONTROL POINT 36 SUBTOTAL: 90.50</p></td>
</tr>
</tbody>
</table>

## Fiscal Daily Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report showing buyer, vendor, and status information for purchase card orders within a selected date range.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a beginning date and ending date for the report.

Specify whether you want to see Delivery Orders.

<span id="_Toc222493071" class="anchor"></span>Figure 41: Fiscal Daily Review

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Purchase Card Transactions Print Menu Option: fiscal Daily Review</p>
<p>Enter beginning date:030100 MAR 1,2000</p>
<p>Enter ending date: t JUN 15,2000</p>
<p>Do you want to see delivery orders? y YES</p>
<p>DEVICE: UCX/TELNET Right Margin: 80//</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>FISCAL DAILY REVIEW REPORT PAGE: 1</p>
<p>PURCHASE DATE BUYER VENDOR AMOUNT</p>
<p>STATUS TRANSACTION PO NUMBER</p>
<p>---------------------------------------------------------------------</p>
<p>DATE: JUN 15, 2000, CONTROL POINT: 20</p>
<p>APR 04, 2000, IFUSERUSER FOUR IFVENDOR1, FIVE 0.75</p>
<p>Ordered and Obligated 688-A09024</p>
<p>APR 04, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE 225.00</p>
<p>Ordered and Obligated 688-A09023</p>
<p>APR 03, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE 0.00</p>
<p>Ordered and Obligated 688-A09022</p>
<p>MAR 30, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE 151.25</p>
<p>Ordered and Obligated 688-A09021</p>
<p>DATE: JUN 15, 2000, CONTROL POINT: 20</p>
<p>MAR 29, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE -450.00</p>
<p>Partial Order Received 688-A09019</p>
<p>MAR 28, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE -700.00</p>
<p>Complete Order Received 688-A09018</p>
<p>MAR 27, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE 120.00</p>
<p>Ordered and Obligated 688-A09017</p>
<p>MAR 27, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE 150.00</p>
<p>Ordered and Obligated 688-A09016</p>
<p>DATE: JUN 15, 2000, CONTROL POINT: 20</p>
<p>MAR 23, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE -310.00</p>
<p>Partial Order Received 688-A09015</p>
<p>MAR 22, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE -350.00</p>
<p>Partial Order Received 688-A09014</p>
<p>MAR 22, 2000, IFUSERUSER, FOUR BAXTER HEALTHCARE/RENAL D 50.00</p>
<p>Partial Order Received 688-A09012</p>
<p>MAR 20, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE -50.00</p>
<p>Partial Order Received 688-A09009</p>
<p>DATE: JUN 15, 2000, CONTROL POINT: 20</p>
<p>MAR 20, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE -35.00</p>
<p>Complete Order Received 688-A09008</p>
<p>MAR 20, 2000, IFUSERUSER, FOUR IFVENDOR1, FIVE 200.00</p>
<p>Partial Order Received 688-A09007</p>
<p>MAR 10, 2000, IFUSERUSER, FOUR BAXTER HEALTHCARE/RENAL D 3600.00</p>
<p>Complete Order Received 688-A09004</p>
<p>CONTROL POINT 20 SUBTOTAL: 2502.00</p>
<p>DATE: JUN 15, 2000, CONTROL POINT: 36</p>
<p>MAY 01, 2000, IFVENDOR, TEN III PHD DVMIFVENDOR, ONE 27.60</p>
<p>Ordered (No Fiscal Action Required) 688-P05176</p>
<p>CONTROL POINT 36 SUBTOTAL: 27.60</p>
<p>JUN 09, 2000 IFUSER, ONE IFVENDOR, FOURR 150.00</p>
<p>Ordered and Obligated 688-A00087</p>
<p>JUN 09, 2000, IFUSER, ONE IFVENDOR, FOUR 300.00</p>
<p>Complete Order Received 688-A00086</p>
<p>DATE: JUN 15, 2000, CONTROL POINT: 60</p>
<p>JUN 09, 2000, IFUSER, ONE IFVENDOR, FOUR 150.00</p>
<p>Ordered and Obligated 688-A00085</p>
<p>JUN 08, 2000, IFUSER, ONE S.U.T. Business Services 144.00</p>
<p>Pending Fiscal Action 688-A00084</p></td>
</tr>
</tbody>
</table>

## History of Purchase Card Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of purchase card orders sorted by unpaid, paid or both status, for a selected date range.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a beginning date and ending date for the report.

The report can list paid orders, unpaid orders or both types of orders. At the Status: prompt enter “P” for paid orders; “U” for unpaid orders; or “B” for both types of orders.

<span id="_Toc222493072" class="anchor"></span>Figure 42: History of Purchase Card Transactions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Purchase Card Transactions Print Menu Option: HIStory of Purchase Card Transactions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enter beginning date: 030100 MAR 1,2000</p>
<p>Enter ending date: T JUN 15,2000</p>
<p>Select one of the following:</p>
<p>P Paid</p>
<p>U Unpaid</p>
<p>B Both</p>
<p>STATUS: Both</p>
<p>DEVICE: UCX/TELNET Right Margin: 80//</p></td>
</tr>
<tr class="even">
<td><p>060 P05182 MAY 18, 2000, IFUSER, FIVE IFVENDOR1, FIVE</p>
<p>250.00 842100 2660 Operating Supplies and Materials</p>
<p>TEST FOR PATCH 253 SAC PRCHEI ROUTINE.</p>
<p>Ordered (No Fiscal Action Required)</p>
<p>060 P05174 MAY 01, 2000, IFVENDOR, TEN DVM</p>
<p>0.00 842100 2660 Operating Supplies and Ma</p>
<p>WOODEN WIDGETS-PINE-PAINTED</p>
<p>Order Not Completely Prepared</p>
<p>060 P05170 APR 19, 2000, IFUSER, FIVE IFVENDOR1, FIVE</p>
<p>0.00 842100 2631 Drugs, Medicines and Chemical Suppl</p>
<p>MORPHINE NJ TUBEX 8MG (PKG.SIZE:10 X 1ML) (SCHEDULE II)</p>
<p>Order Not Completely Prepared</p>
<p>060 P85870 APR 13, 2000, SUPPLY, USER IFVENDOR, FOUR INC.</p>
<p>8.35 822300 2632 Other Medical and Dental Supplies</p>
<p>COVER ARMBOARD 9 INCH</p>
<p>Complete Order Received (Amended)</p>
<p>060 P05157 APR 04, 2000, IFUSER, FIVE IFVENDOR1, FIVE</p>
<p>200.00 820300 2631 Drugs, Medicines and Chem</p>
<p>MORPHINE NJ TUBEX 8MG (PKG.SIZE:10 X 1ML) (SCHEDULE II)</p>
<p>Ordered (No Fiscal Action Required)</p>
<p>060 P05154 APR 04, 2000, IFUSER, FIVE IFVENDOR1, FIVE</p>
<p>100.00 820300 2631 Drugs, Medicines and Chem</p>
<p>MORPHINE NJ TUBEX 8MG (PKG.SIZE:10 X 1ML) (SCHEDULE II)</p>
<p>Ordered (No Fiscal Action Required)</p>
<p>060 P05863 MAR 21, 2000, SUPPLY, USER FEDERAL MARKETING</p>
<p>75.30 820300 2660 Operating Supplies and Materials</p>
<p>BATTERY AAA ALKALINE 1.5 VOLTS</p>
<p>Ordered (No Fiscal Action)-Amended</p>
<p>060 P05845 MAR 10, 2000, SUPPLY, USER IFVENDOR, FOUR</p>
<p>120.12 822100 2692 Prosthetic Supplies</p>
<p>BATTERY AAA ALKALINE 1.5 VOLTS</p>
<p>Reconciled - Amended</p>
<p>060 P00089 MAR 10, 2000, SUPPLY, USER DSA</p>
<p>64.20 822100 2632 Other Medical and Dental Supplies</p>
<p>ADHESIVE TIES, SURGICAL, WHITE, 7-1/4 INCHES WIDE, 11-1/8 INCHES LONG,</p>
<p>Reconciled - Amended</p>
<p>060 P00088 MAR 10, 2000, SUPPLY, USER IFVENDOR, TWO</p>
<p>54.00 822100 2631 Drugs, Medicines and Chemical Suppl</p>
<p>2X2 LITER CONDITIONER, 1X2 LITER BUFFER ASTRA</p>
<p>Reconciled</p></td>
</tr>
</tbody>
</table>

## Reconciled Purchase Card Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of reconciled purchase card orders sorted by user and card number. A reconciled order has been paid in full and completed received.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a STATION NUMBER, beginning date and ending date for the report. Select a DEVICE for displaying the report.

<span id="_Toc222493073" class="anchor"></span>Figure 43: Reconciled Purchase Card Transactions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Purchase Card Transactions Print Menu Option: reconciled Purchase Card Transactions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</td>
</tr>
<tr class="even">
<td>Enter a beginning date: 030100 MAR 1,2000</td>
</tr>
<tr class="odd">
<td>Enter ending date: t JUN 15,2000</td>
</tr>
<tr class="even">
<td>DEVICE: UCX/TELNET Right Margin: 80//</td>
</tr>
<tr class="odd">
<td><p>RECONCILED PURCHASE CARD ORDERS JUN 15, 2000@13:00:14 PAGE 1</p>
<p>P.O. DATE DATE RECONCILED ORDER # $AMT TYPE(S/D)</p>
<p>VENDOR DESCRIPTION</p>
<p>STATUS</p>
<p>DOC-REF # RECONCILED $AMT RECONCILE VENDOR FINAL CHARGE</p>
<p>------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>BUYER: IFBUYER 3</p>
<p>APR 28, 1997, JUN 02, 2000, 688-P65024 667.14 D</p>
<p>IFVENDOR2, TWO SDFS</p>
<p>Reconciled</p>
<p>C68861470012001 150.20 IFVENDOR2, THREE NO</p>
<p>C68861470012006 667.14 IFVENDOR2, FOUR YES</p>
<p>RECONCILED SUBTOTAL - $817.34</p>
<p>BUYER SUBTOTAL - $667.14</p>
<p>BUYER: IFVENDOR, TEN</p>
<p>JUN 12, 2000, JUN 12, 2000, 688-P05185 13.08 SIMPLIFIED</p>
<p>IFVENDOR, FOUR Prosthetic Order</p>
<p>Reconciled</p>
<p>C68801620001001 25.55 YES</p>
<p>RECONCILED SUBTOTAL - $25.55</p>
<p>BUYER SUBTOTAL - $13.08</p>
<p>BUYER: IFBUYER 1</p>
<p>MAR 09, 2000, MAR 09, 2000, 688-P85834 12.12 DETAILED</p>
<p>IFVENDOR, FOUR BATTERY AAA ALKALINE 1.5 VOLTS</p>
<p>Reconciled – Amended</p>
<p>C-688000P85834 6.12 IFVENDOR, FOUR NO</p>
<p>C-6880002P85834 6.00 IFVENDOR, FOUR YES</p>
<p>RECONCILED SUBTOTAL - $12.12</p>
<p>BUYER SUBTOTAL - $12.12</p>
<p>BUYER: IFBUYER 2</p>
<p>NOV 20, 1998, APR 18, 2000, 688-P95080 13.20</p>
<p>FEDERAL MARKETING TESTING OPTIONS IN MNT (11-20-98).</p>
<p>Reconciled – Amended</p>
<p>C-688000P95080 5.00 FEDERAL MARKETING NO</p>
<p>C-6880002P95080 8.20 FEDERAL MARKETING YES</p>
<p>RECONCILED SUBTOTAL - $13.20</p>
<p>MAR 10, 2000, MAR 10, 2000, 688-P85846 10.00</p>
<p>IFVENDOR, FOUR INC. Test item for $10.00</p>
<p>Reconciled</p>
<p>C-688000P85846 10.00 IFVENDOR, FOUR YES</p>
<p>BUYER: IFBUYER 2</p>
<p>RECONCILED SUBTOTAL - $10.00</p>
<p>BUYER SUBTOTAL - $23.20</p></td>
</tr>
<tr class="odd">
<td>Press return to continue, '^' to exit:</td>
</tr>
</tbody>
</table>

## Unreconciled Purchase Card Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of the unreconciled purchase card orders.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a STATION NUMBER, beginning date and ending date for the report. Select a DEVICE for displaying the report.

## ET-FMS Document Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222493074" class="anchor"></span>Figure 44: Unreconciled Purchase Card Transactions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Purchase Card Transactions Print Menu Option: UNReconciled Purchase Card</p>
<p>Transactions</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</td>
</tr>
<tr class="even">
<td>Enter a beginning date: 030100 MAR 1,2000</td>
</tr>
<tr class="odd">
<td>Enter ending date: t JUN 15,2000</td>
</tr>
<tr class="even">
<td>DEVICE: UCX/TELNET Right Margin: 80//</td>
</tr>
<tr class="odd">
<td><p>UNRECONCILED PURCHASE CARD ORDERS JUN 15, 2000@15:27:57 PAGE 1</p>
<p>P.O. DATE ORDER # $AMT TYPE(S/D)</p>
<p>VENDOR DESCRIPTION</p>
<p>STATUS</p>
<p>COMMENTS</p>
<p>----------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>BUYER: IFUSER, TWO</p>
<p>APR 04, 2000, 688-P05160 165.00 DETAILED</p>
<p>BAXTER/HOSPITAL SUPPLY DIV NEEDLE JAMSHIDI BONE MARROW 11GA X</p>
<p>Ordered (No Fiscal Action Required)</p>
<p>Test Document</p>
<p>BUYER SUBTOTAL - $165.00</p>
<p>BUYER: IFUSER, ONE</p>
<p>MAR 02, 2000, 688-P05104 144.00</p>
<p>IFVENDOR, FOUR SHAVING KIT, SURGICAL PREPARATION.</p>
<p>Ordered (No Fiscal Action Required)</p>
<p>BUYER SUBTOTAL - $144.00</p></td>
</tr>
</tbody>
</table>

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a STATION NUMBER. At the Transaction Type: prompt, select ET. Enter the FMS ET Document ID, or two question marks (??) to see your choices.

<span id="_Toc222493075" class="anchor"></span>Figure 45: ET-FMS Document Display

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select one of the following:</p>
<p>ET Expenditure Transfer</p></td>
</tr>
<tr class="even">
<td>Select Transaction Type: et Expenditure Transfer</td>
</tr>
<tr class="odd">
<td><p>FMS ET Document ID: ??</p>
<p>Choose from:</p>
<p>FMS ET Document ID: ET-688HJCG1095</p></td>
</tr>
<tr class="even">
<td><p>FMS Document: ET-688HJCG1095</p>
<p>Description: Auto ET Document</p>
<p>Status: TRANSMITTED</p>
<p>Created: APR 27, 1998@15:54:44</p>
<p>Description Line #500 Line #</p>
<p>BBFY: 98 98</p>
<p>BBEY:</p>
<p>FUND: 0160A1 820100</p>
<p>STATION: 688 688</p>
<p>SUB STATION:</p>
<p>COST CENTER: 820100 820100</p>
<p>SUB COST CENTER: 00 00</p>
<p>FCP/PRJ: 0100E0198 0160A1</p>
<p>BOC: 2660 2660</p>
<p>JOB NO:</p>
<p>LINE AMOUNT: 39.15 39.15</p>
<p>LINE ACTION: D I</p>
<p>PURCHASE CARD ORDER: 688-P85231</p></td>
</tr>
</tbody>
</table>

## ET-FMS Document Rebuild

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will rebuild erroneous/rejected ET-documents.

## Purchase Card Transaction Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report listing accounting and item data for a purchase card order.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a STATION NUMBER. At the P.O./REQ. NO.: prompt, enter the Purchase Card obligation number, or a question mark (?) to see your choices.

<span id="_Toc222493076" class="anchor"></span>Figure 46: Purchase Card Transaction Status

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>P.O./REQ. NO.: P05027 688-P05027 11-19-99 PC Paid (Not Received)</td>
</tr>
<tr class="even">
<td><p>FCP: 060 $ 144.00</p>
<p>Transaction Number: 688-P05027 FCP: 060 Fiscal Service</p>
<p>Transaction Status: Paid (Not Received)</p>
<p>Date of Request: NOV 19, 1999, Date Required: NOV 29, 1999</p>
<p>Vendor: IFVENDOR, FOUR</p>
<p>Committed (Estimated) Cost: 144.00 Date Committed: NOV 29, 1999</p>
<p>Purchase Card Amount: 144.00 Date Signed: NOV 19, 1999@09:09:35</p>
<p>Transaction Amount: 144.00 Accounting Data: 3600160</p>
<p>Originator of Request: IFUSER, ONE</p>
<p>Requesting Service: FISCAL</p>
<p>Delivery Location:</p>
<p>Sort Group:</p>
<p>Do you wish to print this report? Yes// (Yes)</p>
<p>DEVICE: UCX/TELNET Right Margin: 80//</p>
<p>Transaction Number: 688-P05027 FCP: 060 Fiscal Service</p>
<p>Transaction Status: Paid (Not Received)</p>
<p>Date of Request: NOV 19, 1999, Date Required: NOV 29, 1999</p>
<p>Vendor: IFVENDOR, FOUR</p>
<p>Committed (Estimated) Cost: 144.00 Date Committed: NOV 29, 1999</p>
<p>Purchase Card Amount: 144.00 Date Signed: NOV 19, 1999@09:09:35</p>
<p>Transaction Amount: 144.00 Accounting Data: 3600160</p>
<p>Originator of Request: IFUSER, ONE</p>
<p>Requesting Service: FISCAL</p>
<p>Delivery Location:</p>
<p>Sort Group:</p>
<p>NOTE - You cannot use the PURCHASE CARD HOLDER field for lookups.</p></td>
</tr>
</tbody>
</table>

## Monitor Reconciled Orders by Card Holder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print vendor, accounting element, cost, and status information for reconciled orders.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the START WITH RECONCILE DATE: prompt, press \<Enter\> to accept the default RECONCILE DATE or to sort in sequence, starting from a certain reconcile date, type that reconcile date or enter “@” to include null reconcile date values. At the START WITH CARD HOLDER: prompt, press \<Enter\> to start with the first card holder and see all card holders, or to sort in sequence, starting from a certain card holder, type that card holder or enter “@” to include null card holder values

Select a DEVICE for displaying the report.

<span id="_Toc222493077" class="anchor"></span>Figure 47: Monitor Reconciled Orders by Card Holder

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Purchase Card Transactions Print Menu Option: <strong>MONITOR RECONCILED ORDERS BY C</strong> PRCH RECONCILE PRINT Monitor Reconciled Orders by Card Holder</p>
<p>START WITH RECONCILE DATE: FIRST// <strong>&lt;Enter&gt;</strong></p>
<p>START WITH CARD HOLDER: FIRST// <strong>&lt;Enter&gt;</strong></p></th>
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
<td>DEVICE: <strong>UCX/TELNET</strong> Right Margin: 80// <strong>&lt;Enter&gt;</strong></td>
</tr>
<tr class="even">
<td><p>PURCHASE CARD ORDER RECONCILE LIST JUN 16,2000 15:08 PAGE 1</p>
<p>TRANS DATE MERCHANT AMOUNT COMM AMT VARIANCE</p>
<p>PO# VENDOR FCP CC BOC</p>
<p>SUPPLY STATUS ET DOC ID</p>
<p>----------------------------------------------------------------------</p></td>
</tr>
<tr class="odd">
<td><p>RECONCILE DATE: OCT 20,1998</p>
<p>CARD HOLDER: SUPPLY, USER</p>
<p>OCT 19,1998 SOUTHERN OPTICAL 25.00 51.06 26.06</p>
<p>99998128</p>
<p>1788</p>
<p>OCT 20,1998 SOUTHERN OPTICAL 60.83 60.82 -.01</p>
<p>99998126</p>
<p>1787</p>
<p>RECONCILE DATE: OCT 23,1998</p>
<p>CARD HOLDER: SUPPLY, USER</p>
<p>OCT 23,1998 FEDERAL MARKETING 6.60 6.60 0</p>
<p>99998080</p>
<p>1810</p></td>
</tr>
</tbody>
</table>

## BOC Report for OA&MM/Fiscal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will allow users to specify a date and name range to print any Purchase Card transactions which include BOC numbers 2696 to 2699. It is used by OA&MM/Fiscal to perform Supply Funds reconciliation.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the START WITH CARD HOLDER: prompt, press \<Enter\> to accept the default FIRST and see all card holders, or enter a specific card holder.

At the START WITH TRANSACTION DATE: prompt, press \<Enter\> to start at the beginning of the file, or enter a specific TRANSACTION DATE.

Select a DEVICE for displaying the report.

<span id="_Toc222493078" class="anchor"></span>Figure 48: BOC Report for OA&MM/Fiscal

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Purchase Card Transactions Print Menu Option: boc Report for OA&amp;MM/Fiscal</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>* Previous selection: CARD HOLDER not null</p>
<p>START WITH CARD HOLDER: FIRST//</p></td>
</tr>
<tr class="even">
<td><p>* Previous selection: TRANSACTION DATE not null</p>
<p>START WITH TRANSACTION DATE: FIRST//</p></td>
</tr>
<tr class="odd">
<td>DEVICE: UCX/TELNET Right Margin: 80//</td>
</tr>
<tr class="even">
<td><p>PURCHASE CARD/SUPPLY FUND DOC ID RECONCILIATION</p>
<p>JUN 16,2000 15:19 PAGE 1</p>
<p>TRANSACTION</p>
<p>BOC DATE ORACLE DOCUMENT ID PURCHASE ORDER</p>
<p>COMMITTED</p>
<p>AMOUNT AMOUNT MERCHANT NAME</p>
<p>-----------------------------------------------------------------------</p></td>
</tr>
<tr class="odd">
<td><p>CARD HOLDER: IFUSER, TWO</p>
<p>2696 MAR 3,1999 C-662000P95005 662-P95005</p>
<p>1.50 1.50 SIMPLIFIED</p>
<p>2696 MAR 3,1999 C-662000P95006 662-P95006</p>
<p>2.50 2.50 IFVENDOR, FOUR</p></td>
</tr>
</tbody>
</table>

# Accounting Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter lists the options contained on the Utilities Menu. These options enable the Accounting Technician to Edit a BOC on an item in the ITEM file, Review VRQs, establish AR Vendors in the IFCAP Vendor file, edit entries in the Vendor file, clear a lock if necessary, lookup a vendor ID number in the Vendor file, and print a report of documents awaiting Fiscal action.

## Update Status of Funds Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was more useful when IFCAP was not being updated automatically if adjustments were made to the control point balances in the corporate ( now FMS) system. It allows the Accounting Technician to manually enter the current balance of the control point, as listed on the *Status of Allowance* report, into the IFCAP system thereby enabling the technician to see the effect of any transaction input into IFCAP against the actual balance recorded in FMS. To utilize this feature the field STATUS OF FUNDS TRACKING: in File 411 must be set to YES. This is done by the IFCAP Coordinator using the Site Parameter option. It would have to be set individually for each station on the computer system.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select FUND CONTROL POINT STATION NAME: prompt, enter the appropriate Station Number.

At the Select CONTROL POINT: prompt, enter the CONTROL POINT.

At the STATUS OF FUNDS BALANCE: prompt, enter the actual balance of the control point per the *Status of Allowance* report from FMS.

<span id="_Toc222493079" class="anchor"></span>Figure 49: Update Status of Funds Balances

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Utilities Menu Option: update Status of Funds Balances</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select FUND CONTROL POINT STATION NAME: 688 WASHINGTON, DC</td>
</tr>
<tr class="even">
<td><p>Select CONTROL POINT: 025 Radiology// 110 MAVIS .01 0160A1 10 0100 01004</p>
<p>2116</p></td>
</tr>
<tr class="odd">
<td><p>STATUS OF FUNDS BALANCE: 37513.35</p>
<p>Select CONTROL POINT: 060 Fiscal Service 0160A1 10 0100 010042100</p>
<p>STATUS OF FUNDS BALANCE: 12312.56</p>
<p>Select CONTROL POINT:</p></td>
</tr>
</tbody>
</table>

## Lookup Vendor ID Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is designed to permit Fiscal Service to lookup the Vendor ID Number, Alternate Address Indicator and Payment address information for any vendor in the vendor file.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select FUND CONTROL POINT STATION NAME: prompt, enter the appropriate Station Number.

At the Select CONTROL POINT: prompt, enter the CONTROL POINT.

At the Select Vendor Name or PO Number: prompt, enter the Vendor Name or purchase order number.

<span id="_Toc222493080" class="anchor"></span>Figure 50: Lookup Vendor ID Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Utilities Menu Option: look up Vendor ID Number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select Vendor Name or PO Number: IFVENDOR, FOUR</td>
</tr>
<tr class="even">
<td><p>1 IFVENDOR, FOUR EDI PH:800 333-8838 NO: 65</p>
<p>PAY ADD: DEPT LA 21061 FMS: IFVENDOR, FOUR</p>
<p>PASADENA, CA 91185 CODE:93086711305 FAX:301 111-2222</p>
<p>2 IFVENDOR, FOUR INC. EDI PH:800 333-8828 NO: 40179</p>
<p>PAY ADD:2424 WEST 23RD ST FMS: IFCAPVENDO52.FIVE</p>
<p>ERIE, PA 16514 CODE:250320960 FAX:510 444-9876</p>
<p>CHOOSE 1-2: 1 IFVENDOR, FOUR EDI PH:800 333-8838 NO: 65</p>
<p>PAY ADD: DEPT LA 21061 FMS: IFVENDOR, FOUR</p>
<p>PASADENA, CA 91185 CODE:93086711305 FAX:301 111-2222</p>
<p>Review current payment information on this Vendor? YES// y YES</p>
<p>Lookup Vendor ID Number</p>
<p>Payment Information</p>
<p>Vendor Name: IFVENDOR, FOUR</p>
<p>Vendor Number: 65 Non-Recurring/Recurring: RECURRING</p>
<p>FMS Vendor Code: 930867113</p>
<p>Alternate Address Indicator: 05</p>
<p>Address: DEPT LA 21061</p>
<p>2424 WEST 23RD STREET</p>
<p>PASADENA, CA 91185</p>
<p>Payment Contact Person: IFUSER, SEVEN</p>
<p>Select Vendor Name or PO Number:</p></td>
</tr>
</tbody>
</table>

## Vendor File Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option permits the Fiscal Service to edit the VENDOR NAME and PAYMENT ADDRESS fields of an entry in the Vendor File. In order to edit the VENDOR NAME and PAYMENT ADDRESS fields for a Medical/Surgical Prime (MSPV) Vendor (vendor numbers above 949,999), the Fiscal user must hold the PRCHVEN security key.

> **NOTE:** Changes made in this patch to security key permissions have no impact on the existing VRQ (FMS Vendor Request Document) process.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a STATION NUMBER.

At the VENDOR NAME: prompt, enter the name of the vendor you wish to edit, or enter two question marks (??) to see a list of those available.

If you changed any critical data fields, IFCAP may ask if you need to send a Vendor Request (VRQ) to Austin. If so, answer “YES” to generate a VRQ. If you made no change to critical fields, IFCAP will not ask you the question.

<span id="_Toc222493081" class="anchor"></span>Figure 51: Vendor File Edit

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Vendor File Edit</p>
<p>Fiscal may add new Vendors to the Vendor File.</p></td>
</tr>
<tr class="even">
<td>Select VENDOR NAME: ??</td>
</tr>
<tr class="odd">
<td><p>1 IFVENDOR, ONE PH:413 555-5555 NO: 41369</p>
<p>PAY ADD:8 HIGH ST FMS:</p>
<p>FLORENCE, MA 01062 CODE:98722987301 FAX:301 427-3711</p>
<p>::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::</p>
<p>5 IFVENDOR, ONE ‘S THINGS PH: NO: 41383</p>
<p>PAY ADD:9 HOGH FMS:</p>
<p>FLORENCE, MA 01063 CODE: FAX:</p></td>
</tr>
<tr class="even">
<td><p>CHOOSE 1-5: 1 IFVENDOR, ONE PH:413 269-2625 NO: 41369</p>
<p>PAY ADD:8 HIGH ST FMS:</p>
<p>FLORENCE, MA 01062 CODE:98722987301 FAX:301 427-3711</p></td>
</tr>
<tr class="odd">
<td>Review current payment information on this Vendor? YES//</td>
</tr>
<tr class="even">
<td><p>Vendor File Edit</p>
<p>Payment Information</p>
<p>Vendor Name: IFVENDOR, ONE</p>
<p>Vendor Number: 41369 Non-Recurring/Recurring: RECURRING</p>
<p>FMS Vendor Code: 987229873</p>
<p>Alternate Address Indicator: 01</p>
<p>Address: 8 HIGH ST</p>
<p>FLORENCE, MA 01062</p>
<p>Payment Contact Person: IFUSER, EIGHT</p></td>
</tr>
<tr class="odd">
<td>Edit the payment information on Vendor record? YES//</td>
</tr>
<tr class="even">
<td><p>Vendor File Edit</p>
<p>NAME: IFVENDOR, ONE //</p>
<p>TAX ID/SSN: 000000001//</p>
<p>SSN/TAX ID INDICATOR: TAX IDENTIFICATION NUMBER//</p>
<p>FMS VENDOR CODE: 000000001//</p>
<p>ALT-ADDR-IND: 01//</p>
<p>PAYMENT CONTACT PERSON: IFUSER, EIGHT //</p>
<p>PAYMENT PHONE NO.:</p>
<p>ORDERING ADDRESS: 8 HIGH ST</p>
<p>FLORENCE, MASSACHUSETTS 01061</p>
<p>PAYMENT ADDRESS1: 8 ANY ST// 10 South St.</p>
<p>PAYMENT ADDRESS2: BOX 000//</p>
<p>PAYMENT CITY: FLORENCE//</p>
<p>PAYMENT STATE: MASSACHUSETTS//</p>
<p>PAYMENT ZIP CODE: 01062//01061</p>
<p>1099 VENDOR INDICATOR: YES//</p>
<p>VENDOR TYPE: COMMERCIAL//</p>
<p>DUN &amp; BRADSTREET #: 987228934//</p>
<p>UEI:</p></td>
</tr>
<tr class="odd">
<td><p>DOES A VRQ NEED TO GO TO AUSTIN (YES/NO)? NO// YES</p>
<p>Creating the FMS VENDOR REQUEST.</p></td>
</tr>
<tr class="even">
<td>Enter RETURN to continue:</td>
</tr>
</tbody>
</table>

## Edit BOC in Item File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to edit the Budget Object Code (BOC) on an item in the Item File.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select ITEM MASTER NUMBER: prompt, enter the item number you want to edit, or enter two question marks (??) to see a list of those available.

At the BOC: prompt, enter the BOC you wish to apply to the item.

<span id="_Toc222493082" class="anchor"></span>Figure 52: Edit BOC in Item File

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Utilities Menu Option: edit BOC in Item File</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select ITEM MASTER NUMBER: 100012 ??</td>
</tr>
<tr class="even">
<td><p>Select ITEM MASTER NUMBER: 100</p>
<p>1 100 PROBE-EAR</p>
<p>2 100-0129 13 THIORRIDAZINE SOL 100MG/ML 4 OZ BT(MELLARIL)</p></td>
</tr>
<tr class="odd">
<td><p>CHOOSE 1-2: 1 100 PROBE-EAR</p>
<p>PROBE-EAR-SAO2 3700</p></td>
</tr>
<tr class="even">
<td>BOC: 2660 Operating Supplies and Materials// 2632 Other Medical and Dental Supplies</td>
</tr>
</tbody>
</table>

## Clear Program Lock

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the Accounting Technician to clear the system if a particular program lock is set. It might happen that two individuals try to batch documents at the same time.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select FISCAL LOCK TYPE: prompt, enter the Lock to be cleared, or enter two question marks (??) to see a list of those available.

<span id="_Toc222493083" class="anchor"></span>Figure 53: Edit BOC in Item File

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Utilities Menu Option: clear Program Lock</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Select FISCAL LOCK TYPE: ??</td>
</tr>
<tr class="even">
<td><p>Choose from:</p>
<p>BATCH/TRANSMIT</p>
<p>BUDGET RELEASE</p>
<p>CLI BATCH/TRANSMIT</p>
<p>CLM BATCH/TRANSMIT</p>
<p>ISM BATCH/TRANSMIT</p>
<p>LOG BATCH/TRANSMIT</p>
<p>PHA BATCH/TRANSMIT</p>
<p>PRC BATCH/TRANSMIT</p></td>
</tr>
<tr class="odd">
<td>Select FISCAL LOCK TYPE: batch/TRANSMIT</td>
</tr>
<tr class="even">
<td>BATCH/TRANSMIT Lock is not in use. No action taken</td>
</tr>
</tbody>
</table>

## Undelivered Orders Reconciliation Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates the 850 Undelivered Orders Reconciliation Report. This report is very resource intensive and should be scheduled to run in off-hours. The option can be invoked manually. This report restricts purchase orders from a single station and can be limited to a date range. The default date range is from T-90 days to T.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a STATION NUMBER.

At the Select BEGINNING DATE: prompt, enter a beginning date, or press \<Enter\> to accept the default 90-day period.

At the Select ENDING DATE: prompt, enter an ending date, or press \<Enter\> to accept the default.

Enter a DEVICE.

<span id="_Toc222493084" class="anchor"></span>Figure 54: Undelivered Orders Reconciliation Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Utilities Menu Option: undelivered Orders Reconciliation Report</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Are you sure that you want to manually run this option? NO// y YES</td>
</tr>
<tr class="even">
<td><p>Select STATION NUMBER ('^' TO EXIT): 688// WASHINGTON, DC</p>
<p>Select BEGINNING DATE: MAR 21, 2000// (MAR 21, 2000)</p>
<p>Select ENDING DATE: JUN 19, 2000// (JUN 19, 2000)</p>
<p>DEVICE: HOME// UCX/TELNET Right Margin: 80//</p></td>
</tr>
<tr class="odd">
<td><p>...EXCUSE ME, HOLD ON...850</p>
<p>UNDELIVERED ORDERS RECONCILIATION FOR STATION 688 FROM MAR 21, 2000, TO JUN 19, 2000</p>
<p>JUN 19,2000 17:54 PAGE 1</p>
<p>TRANS TRANS SOURCE COST</p>
<p>REF NO DATE CODE FCP CODE REQ DATE CENTER BOC</p>
<p>OBLIGATED ACCRUED UNDELIVERED</p>
<p>AMOUNT EXPENDITURES ORDERS</p>
<p>------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>APPROPRIATION: 3600160</p>
<p>A00061 05/01/00 MO. E 060 3 05/11/00 842100 2620 318.00 0.00 318.00</p>
<p>A00065 05/11/00 MO. E 060 3 05/21/00 842100 2620 216.00 72.00 144.00</p>
<p>A00066 05/12/00 MO. E 060 3 05/22/00 842100 2660 1728.00 576.00 1152.00</p>
<p>A00067 05/12/00 MO. E 060 3 05/22/00 842100 2660 288.00 192.00 96.00</p>
<p>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</p>
<p>APPROPRIATION: 36X8180</p>
<p>H00003 05/11/00 MO. E 562 3 05/21/00 882100 2660 216.00 0.00 216.00</p>
<p>NUMBER RECORDS 1</p>
<p>SUBTOTALS $ 216.00 0.00 216.00</p>
<p>TOTAL NUMBER RECORDS 25</p>
<p>TOTALS $ 5655.60 1032.00 4623.60</p></td>
</tr>
<tr class="odd">
<td>Would you like to run another reconciliation report? No// (No)</td>
</tr>
</tbody>
</table>

## Fiscal Pending Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will print all fiscal pending action 1358 and P.O. for fiscal obligation.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a DEVICE.

<span id="_Toc222493085" class="anchor"></span>Figure 55: Fiscal Pending Action

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Utilities Menu Option: fiscal Pending Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DEVICE: HOME// UCX/TELNET Right Margin: 80//</td>
</tr>
<tr class="even">
<td><p>Page 1</p>
<p>IFCAP OBLIGATIONS PENDING ACTION REPORT - Purchase Orders</p>
<p>PRINTED ON 19-Jun-00 AT 18:14:00</p>
<p>======================================================================</p>
<p>P.O. NUMBER FCP AMOUNT DATE STATUS</p>
<p>======================================================================</p>
<p>688-A00090 110 $ 120.00 06-19-00 Pending Fiscal Action</p>
<p>688-A00089 060 $ 150.00 06-19-00 Pending Fiscal Action</p>
<p>688-B00047 060 $ 24.00 06-13-00 Pending Fiscal Action</p>
<p>688-A00084 060 $ 144.00 06-08-00 Pending Fiscal Action</p>
<p>688-A00079 110 $ 442.00 05-26-00 Pending Fiscal Action</p>
<p>688-A00077 060 $ 144.00 05-25-00 Pending Fiscal Action</p>
<p>688-B00044 060 $ 11.00 05-19-00 Pending Fiscal Action</p>
<p>688-B00043 060 $ 30.00 05-19-00 Pending Fiscal Action</p>
<p>688-B00042 060 $ 14.00 05-16-00 Pending Fiscal Action</p>
<p>688-A00068 060 $ 290.00 05-12-00 Pending Fiscal Action</p></td>
</tr>
<tr class="odd">
<td>Press &lt;RET&gt; to continue or '^' to quit.</td>
</tr>
</tbody>
</table>

## History - Code Sheet/Obligation (PAT) Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to view the code sheets which have been prepared for a specific obligation number/purchase order.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the PURCHASE ORDER NUMBER: prompt, enter the obligation number you wish to view.

<span id="_Toc222493086" class="anchor"></span>Figure 56: History - Code Sheet/Obligation (PAT) Number

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Utilities Menu Option: history - Code Sheet/Obligation (PAT) Number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PURCHASE ORDER NUMBER: a00072 688-A00072 05-23-00 ST Partial Order Received (Amended)</p>
<p>FCP: 060 $ 285.12</p></td>
</tr>
<tr class="even">
<td><p>ANOTHER ONE:</p>
<p>PURCHASE ORDER NUMBER: 688-A00072</p></td>
</tr>
<tr class="odd">
<td><p>DATE: 5/23/2000 FCP: 060 Fiscal Service</p>
<p>STATUS: Partial Order Received (Amende</p>
<p>VENDOR: IFVENDOR, FOUR TOTAL: 285.12</p>
<p>FMS DOCUMENT(S):</p>
<p>TT/SC TR DATE REF SIG DATE/TIME SIGNED BY:</p>
<p>MO. E 052300 A00072 MAY 23, 2000@10:27:12 IFUSER, ONE</p>
<p>RR. E 052300 A00072 MAY 23, 2000@10:28 IFUSER, ONE</p>
<p>MO.M 052400 A00072 MAY 24, 2000@11:14:03 IFUSER, ONE</p>
<p>MO.M 052400 A00072 MAY 24, 2000@11:29:27 IFUSER, ONE</p>
<p>MO.M 052400 A00072 MAY 24, 2000@13:37:31 IFUSER, ONE</p></td>
</tr>
<tr class="even">
<td>Would you like to review the entire purchase order? NO// y (YES)</td>
</tr>
<tr class="odd">
<td><p>PURCHASE ORDER: 688-A00072 STATUS: Partial Order Received (Amended)</p>
<p>M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.: 2 05/24/00</p>
<p>REQUESTING SERVICE: FISCAL</p>
<p>VENDOR: IFVENDOR, FOUR SHIP TO: Washington VAMC</p>
<p>1000 BLVD OF THE ALLIES V.A. Medical Center</p>
<p>SUITE 510 50 Irving Street, NW</p>
<p>ROOM 543, POD 12 Washington, DC 20422</p>
<p>NORCROSS, GA 30071</p>
<p>800-555-5555</p>
<p>FMS Vendor Code: 93086711305</p></td>
</tr>
<tr class="even">
<td><p>FOB POINT: DESTINATION |PROPOSAL: N/A |AUTHORITY:</p>
<p>COST CENTER: 842100 | | FAR 13</p>
<p>TYPE: *DELIVERY &amp; PURCHASE ORDER| |AGENT:</p>
<p>DELIVER ON/BEFORE 6/2/2000 |CONTRACT: | IFUSER, ONE</p>
<p>DISCOUNT TERM: NET30 | DF454444 |DATE: 5/23/2000</p>
<p>APP: 3600160-060 |</p>
<p>| |TOTAL: 285.12</p>
<p>---------------------------------------------------------------------</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>------------------------------------------------------------------------</p></td>
</tr>
<tr class="odd">
<td><p>SHAVING KIT, SURGICAL 24 BX 12.00 288.00</p>
<p>PREPARATION. DISPOSABLE.</p>
<p>CONSISTS OF PLASTIC TRAY WITH</p>
<p>SEPARATIONS FOR RINSE AND SOAP</p>
<p>WATER, WATER REPELLENT LINEN</p>
<p>PROTECTOR, DOUBLE EDGE RAZOR</p>
<p>WITH BLADE, ANTI-INFECTIVE SOAP</p>
<p>OR DETERGENT, CLEAN UP MATERIAL</p>
<p>TO DRY SHAVEN AREA. FOR</p>
<p>PREPARATION OF SKIN PRIOR TO</p>
<p>OPERATIONS. (WHS LOC B11)</p>
<p>STK#: 13-9002</p>
<p>NSN: 6515-00-103-6659</p>
<p>QTY PREV RCVD: 16</p>
<p>PARTIAL NO.: 1,2</p>
<p>Items per BX: 24</p></td>
</tr>
<tr class="even">
<td><p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>----------------------------------------------------------------------</p>
<p>BOC: 2660 FMS LINE: 001 CONTRACT: DF454444</p>
<p>2 MAGNESIA AND ALUMINA ORAL 0 CS 0.00 0.00</p>
<p>SUSPENSION, USP. 5 FL OZ. (148</p>
<p>ML.) PLASTIC BOTTLE. EACH ML.</p>
<p>CONTAINS MAGNESIA HYDROXIDE 40</p>
<p>MG AND ALUMINUM HYDROXIDE 45 MG</p>
<p>(MAALOX) 48BT/CS</p>
<p>NDC:12233-1122-11</p>
<p>NSN: 6505-01-369-6028</p>
<p>Items per CS: 48</p>
<p>BOC: 2631 FMS LINE: 002</p>
<p>3 LESS 1 % FOR ITEMS: 1 2.88</p>
<p>IN ORDER TO RECEIVE PAYMENT VENDOR MUST SUBMIT INVOICE WITH</p>
<p>EITHER SIGNED BILLS OF LADING, FREIGHT BILL, PARCEL POST</p>
<p>RECEIPT FROM CARRIER. IF VENDOR MAKES SHIPMENT THROUGH</p>
<p>OTHER THAN COMMERCIAL CARRIES, OR IF THE VETERAN RECEIVES</p>
<p>ITEMS AT THE VENDOR'S BUSINESS LOCATION, VENDOR SHOULD SO</p>
<p>INDICATE ON THE INVOICE. VENDOR IS TO BILL ONLY FOR THOSE</p>
<p>ITEMS SHIPPED.</p></td>
</tr>
<tr class="odd">
<td><p>____________________________________________________________________ 1</p>
<p>AMENDMENT NUMBER: 1 EFFECTIVE DATE: 5/24/200</p>
<p>*ADDED THROUGH AMENDMENT*</p>
<p>Authority Edit is OTHER (specify type of modification and authority)</p></td>
</tr>
<tr class="even">
<td><p>AMENDMENT NUMBER: 2 EFFECTIVE DATE: 5/24/2000</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>-------------------------------------------------------------------</p>
<p>The following line item has been cancelled:</p>
<p>Item No. 2 Item Master File No. 103 BOC: 2631</p>
<p>MAGNESIA AND ALUMINA ORAL SUSPENSION, USP. 5 FL OZ. (148 ML</p>
<p>.) PLASTIC BOTTLE. EACH ML. CONTAINS MAGNESIA HYDROXIDE 40 MG</p>
<p>AND ALUMINUMHYDROXIDE 45 MG (MAALOX) 48BT/CS</p>
<p>NDC:12233-1122-11</p>
<p>Items per CS: 48 NSN: 6505-01-369-6028</p>
<p>12 CS at $ 24.0000 = $ 288.00</p>
<p>*ADDED THROUGH AMENDMENT*</p>
<p>Authority Edit is OTHER (specify type of modification and authority)</p></td>
</tr>
<tr class="odd">
<td><p>AMENDMENT NUMBER: 3 EFFECTIVE DATE: 5/24/2000</p>
<p>UNIT TOTAL</p>
<p>\ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>---------------------------------------------------------------------</p>
<p>ADMINISTRATIVE CERTIFICATION 2, DIRECT SHIPMENT RECEIVING REPORT, has been ADDED</p>
<p>*ADDED THROUGH AMENDMENT*</p>
<p>Authority Edit is OTHER (specify type of modification and authority)</p></td>
</tr>
<tr class="even">
<td><p>AMENDMENT NUMBER: 4 EFFECTIVE DATE: 5/24/2000</p>
<p>*ADDED THROUGH AMENDMENT*</p>
<p>Authority Edit is OTHER (specify type of modification and authority)</p>
<p>*ADDED THROUGH AMENDMENT*</p>
<p>UNIT TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST COST</p>
<p>--------------------------------------------------------------------</p>
<p>1% Discount For Item(s): 1</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Review a Receiving Report? NO// y (YES)</p>
<p>Select PARTIAL DATE: 1 5-23-2000</p></td>
</tr>
<tr class="odd">
<td><p>PURCHASE ORDER: 688-A00072 STATUS: Partial Order Received (Amended)</p>
<p>PROCESSING: INVOICE/RECEIVING REPORT PARTIAL: 1 5/23/2000</p>
<p>----------------------------------------------------------------------</p>
<p>UNIT QTY TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST REC COST</p>
<p>-----------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>1 SHAVING KIT, SURGICAL 24 BX 12.00 12 144.00</p>
<p>PREPARATION. DISPOSABLE.</p>
<p>CONSISTS OF PLASTIC TRAY WITH</p>
<p>SEPARATIONS FOR RINSE AND SOAP</p>
<p>WATER, WATER REPELLENT LINEN</p>
<p>PROTECTOR, DOUBLE EDGE RAZOR</p>
<p>WITH BLADE, ANTI-INFECTIVE SOAP</p>
<p>OR DETERGENT, CLEAN UP MATERIAL</p>
<p>TO DRY SHAVEN AREA. FOR</p>
<p>PREPARATION OF SKIN PRIOR TO</p>
<p>OPERATIONS. (WHS LOC B11)</p>
<p>IMF #: 104 CONTRACTS: DF454444</p>
<p>Total Amount: 144.00</p>
<p>Processed By: /ES/IFUSER, ONE</p></td>
</tr>
<tr class="odd">
<td>ENTER &lt;CR&gt; TO CONTINUE</td>
</tr>
<tr class="even">
<td><p>Select PARTIAL DATE: ?</p>
<p>Answer with PARTIAL NUMBER, or DATE</p>
<p>Choose from:</p>
<p>1 MAY 23, 2000</p>
<p>2 MAY 24, 2000</p>
<p>Select PARTIAL DATE: 2 5-24-2000</p></td>
</tr>
<tr class="odd">
<td><p>PURCHASE ORDER: 688-A00072 STATUS: Partial Order Received (Amended)</p>
<p>PROCESSING: INVOICE/RECEIVING REPORT PARTIAL: 2 5/24/2000</p>
<p>------------------------------------------------------------------------</p>
<p>UNIT QTY TOTAL</p>
<p>ITEM DESCRIPTION QTY UNIT COST REC COST</p>
<p>------------------------------------------------------------------------</p></td>
</tr>
<tr class="even">
<td><p>1 SHAVING KIT, SURGICAL 24 BX 12.00 4 48.00</p>
<p>PREPARATION. DISPOSABLE.</p>
<p>CONSISTS OF PLASTIC TRAY WITH</p>
<p>SEPARATIONS FOR RINSE AND SOAP</p>
<p>WATER, WATER REPELLENT LINEN</p>
<p>PROTECTOR, DOUBLE EDGE RAZOR</p>
<p>WITH BLADE, ANTI-INFECTIVE SOAP</p>
<p>OR DETERGENT, CLEAN UP MATERIAL</p>
<p>TO DRY SHAVEN AREA. FOR</p>
<p>PREPARATION OF SKIN PRIOR TO</p>
<p>OPERATIONS. (WHS LOC B11)</p>
<p>IMF #: 104 CONTRACTS: DF454444</p>
<p>Total Amount: 48.00</p>
<p>Processed By: /ES/IFUSER, ONE</p></td>
</tr>
</tbody>
</table>

## Review Vendor Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows Fiscal to review Vendor Requests *before* they are sent to Austin. This option was added to reduce the number of VRQs going to Austin. Reviewers are expected to check the VENDOR file in FMS, get any information available, and edit the vendor locally rather than sending a VRQ to Austin.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select VRQ Action: prompt, select the action, or enter two question marks (??) to see a list of actions.

<span id="_Toc222493087" class="anchor"></span>Figure 57: Review Vendor Entry (RE)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Utilities Menu Option: REVIEW VENDOR REQUEST</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>VENDOR review Jun 21, 2000, 13:42:06 Page: 1 of 3</p>
<p>VENDOR REQUESTs for review</p>
<p>+ Vendor Name FMS Vendor TAX/SSN</p>
<p>15 IFVENDOR, TWO 000000001</p>
<p>16 IFVENDOR, THREE 000000003</p>
<p>17 IFVENDOR, FOUR 000000004</p>
<p>18 IFVENDOR, FIVE 000000005</p>
<p>19 IFVENDOR, SIX 000000006</p>
<p>20 IFVENDOR, SEVEN 000000007</p>
<p>21 IFVENDOR, EIGHT 000000008</p>
<p>22 IFVENDOR, NINE 000000009</p>
<p>23 IFVENDOR1, FIVE 000000015</p>
<p>24 IFVENDOR, TEN 000000010</p>
<p>25 IFVENDOR1, ONE 000000011</p>
<p>26 IFVENDOR1, TWO</p>
<p>27 IFVENDOR1, THREE 000000013</p>
<p>28 IFVENDOR1, FOUR 000000014</p>
<p>+ Enter ?? for more actions</p></td>
</tr>
<tr class="even">
<td><p>RE Review Entry SD Send VENDOR REQUEST PE Print Entry</p>
<p>EV Edit Vendor Request DE Delete VENDOR REQUEST</p>
<p>Select VRQ Action: Next Screen// RE Review Entry</p></td>
</tr>
<tr class="odd">
<td>Select: (15-28): 22</td>
</tr>
<tr class="even">
<td>Enter RETURN to continue or '^' to exit:</td>
</tr>
<tr class="odd">
<td><p>VENDOR NAME: IFVENDOR, NINE PAGE: 2</p>
<p>FMS VENDOR CODE:</p>
<p>ALT-ADDR-IND:</p>
<p>TAX ID/SSN: 000000009</p>
<p>SSN/TAX ID IND: SOCIAL SECURITY NUMBER</p>
<p>NON-RECURRING/</p>
<p>RECURRUNG VENDOR: RECURRING</p>
<p>1099 VENDOR INDICATOR: YES</p>
<p>VENDOR TYPE: COMMERCIAL</p>
<p>DUN &amp; BRADSTREET: 410-555-5555</p>
<p>UEI:</p></td>
</tr>
<tr class="even">
<td>Enter RETURN to continue:</td>
</tr>
</tbody>
</table>

#### Edit Vendor Request

If you look up the Vendor in the Austin vendor file and find that the vendor information is there, you can edit the Vendor entry in IFCAP and enter the necessary data by selecting the Action code EV (Edit Vendor Request):

<span id="_Toc222493088" class="anchor"></span>Figure 58: Edit Vendor Request (EV)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>+ Vendor Name FMS Vendor TAX/SSN</p>
<p>15 IFVENDOR, TWO 000000002</p>
<p>16 IFVENDOR, THREE 000000003</p>
<p>17 IFVENDOR, FOUR 000000004</p>
<p>18 IFVENDOR, FIVE 000000005</p>
<p>19 IFVENDOR, SIX 000000006</p>
<p>20 IFVENDOR, SEVEN 000000007</p>
<p>21 IFVENDOR, EIGHT 000000008</p>
<p>22 IFVENDOR, NINE 000000009</p>
<p>23 IFVENDOR1, FIVE 000000015</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>+ Enter ?? for more actions</p>
<p>RE Review Entry SD Send VENDOR REQUEST PE Print Entry</p>
<p>EV Edit Vendor Request DE Delete VENDOR REQUEST</p>
<p>Select VRQ Action: Next Screen// ev Edit Vendor Request</p>
<p>Select: (15-28): 22</p></td>
</tr>
<tr class="even">
<td><p>IFVENDOR, NINE</p>
<p>Review current payment information on this Vendor? YES//</p></td>
</tr>
<tr class="odd">
<td><p>Review VENDOR REQUEST</p>
<p>Payment Information</p>
<p>Vendor Name: IFVENDOR, NINE</p>
<p>Vendor Number: 41367 Non-Recurring/Recurring: RECURRING</p>
<p>FMS Vendor Code:</p>
<p>Alternate Address Indicator:</p>
<p>Address: 923 ANY LN</p>
<p>ANNAAPOLIS, MD 20999</p></td>
</tr>
<tr class="even">
<td>Edit the payment information on Vendor record? YES//</td>
</tr>
<tr class="odd">
<td><p>Review VENDOR REQUEST</p>
<p>TAX ID/SSN: 000000009//</p>
<p>SSN/TAX ID INDICATOR: SOCIAL SECURITY NUMBER//</p>
<p>FMS VENDOR CODE:</p>
<p>ALT-ADDR-IND:</p>
<p>PAYMENT CONTACT PERSON:</p>
<p>PAYMENT PHONE NO.:</p>
<p>ORDERING ADDRESS: 923 ANY LN</p>
<p>ANNAAPOLIS, MARYLAND 20999</p>
<p>PAYMENT ADDRESS1: 923 ANY LN//</p>
<p>PAYMENT ADDRESS2:</p>
<p>PAYMENT CITY: ANNAAPOLIS//</p>
<p>PAYMENT STATE: MARYLAND//</p>
<p>PAYMENT ZIP CODE: 20999</p>
<p>1099 VENDOR INDICATOR: YES//</p>
<p>VENDOR TYPE: COMMERCIAL//</p>
<p>DUN &amp; BRADSTREET #:</p>
<p>UEI:</p></td>
</tr>
</tbody>
</table>

Delete Vendor Request

If you find that you do not want to send the VRQ to Austin, select the Action code DV (Delete Vendor Request). This will ensure that no VRQ is sent to the Austin Vendorizing Unit.

<span id="_Toc222493089" class="anchor"></span>Figure 59: Delete Vendor Request (DV)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select VRQ Action: Next Screen// NEXT SCREEN</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VENDOR review Jun 21, 2000, 14:01:58 Page: 2 of 3</td>
</tr>
<tr class="even">
<td><p>VENDOR REQUESTs for review</p>
<p>+ Vendor Name FMS Vendor TAX/SSN</p>
<p>15 IFVENDOR, TWO 000000002</p>
<p>16 IFVENDOR, THREE 000000003</p>
<p>17 IFVENDOR, FOUR 000000004</p>
<p>18 IFVENDOR, FIVE 000000005</p>
<p>19 IFVENDOR, SIX 000000006</p>
<p>20 IFVENDOR, SEVEN 000000007</p>
<p>21 IFVENDOR, EIGHT 000000008</p>
<p>22 IFVENDOR, NINE 000000009</p>
<p>23 IFVENDOR1, FIVE 000000015</p>
<p>+ Enter ?? for more actions</p></td>
</tr>
<tr class="odd">
<td><p>RE Review Entry SD Send VENDOR REQUEST PE Print Entry</p>
<p>EV Edit Vendor Request DE Delete VENDOR REQUEST</p>
<p>Select VRQ Action: Next Screen// de Delete VENDOR REQUEST</p>
<p>Select: (15-28): 22</p></td>
</tr>
<tr class="even">
<td>Do you want to delete IFVENDOR, NINE (YES/NO)? NO// y YES</td>
</tr>
<tr class="odd">
<td><p>VENDOR review Jun 21, 2000, 14:02:20 Page: 2 of 3</p>
<p>VENDOR REQUESTs for review</p>
<p>+ Vendor Name FMS Vendor TAX/SSN</p>
<p>15 IFVENDOR, TWO 000000002</p>
<p>16 IFVENDOR, FOUR 000000003</p>
<p>17 IFVENDOR, FOUR 000000004</p>
<p>18 IFVENDOR, FIVE 000000005</p>
<p>19 IFVENDOR, SIX 000000006</p>
<p>20 IFVENDOR, SEVEN 000000007</p>
<p>21 IFVENDOR, EIGHT 000000008</p>
<p>22 IFVENDOR1, FIVE 000000015</p>
<p>23 IFVENDOR, TEN 000000010</p>
<p>+ Enter ?? for more actions</p></td>
</tr>
<tr class="even">
<td><p>RE Review Entry SD Send VENDOR REQUEST PE Print Entry</p>
<p>EV Edit Vendor Request DE Delete VENDOR REQUEST</p>
<p>Select VRQ Action: Next Screen//</p></td>
</tr>
</tbody>
</table>

#### Send Vendor Request

If you determine that the Vendor does not exist in the Austin Vendor file, select the Action code SD (Send Vendor Request) to submit the VRQ to Austin.

<span id="_Toc222493090" class="anchor"></span>Figure 60: Send Vendor Request (SD)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select VRQ Action: Next Screen// NEXT SCREEN</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>RE Review Entry SD Send VENDOR REQUEST PE Print Entry</p>
<p>EV Edit Vendor Request DE Delete VENDOR REQUEST</p>
<p>Select VRQ Action: Next Screen// sd Send VENDOR REQUEST</p></td>
</tr>
<tr class="even">
<td><p>VENDOR review Jun 21, 2000, 14:06:12 Page: 2 of 3</p>
<p>VENDOR REQUESTs for review</p>
<p>+ Vendor Name FMS Vendor TAX/SSN</p></td>
</tr>
<tr class="odd">
<td><p>15 IFVENDOR, TWO 000000002</p>
<p>16 IFVENDOR, THREE 000000003</p>
<p>17 IFVENDOR, FOUR 000000004</p>
<p>18 IFVENDOR, FIVE 000000005</p>
<p>19 IFVENDOR, SIX 000000006</p>
<p>20 IFVENDOR, SEVEN 000000007</p>
<p>21 IFVENDOR, EIGHT 000000008</p>
<p>22 IFVENDOR1, FIVE 000000015</p>
<p>23 IFVENDOR, TEN 000000010</p></td>
</tr>
<tr class="even">
<td>+ Enter ?? for more actions</td>
</tr>
<tr class="odd">
<td>Select: (15-28): 16</td>
</tr>
<tr class="even">
<td>DOES A VRQ NEED TO GO TO AUSTIN (YES/NO)? NO// y YES</td>
</tr>
<tr class="odd">
<td><p>Creating the FMS VENDOR REQUEST.</p>
<p>Enter RETURN to continue:</p></td>
</tr>
<tr class="even">
<td><p>VENDOR review Jun 21, 2000, 14:06:34 Page: 1 of 3</p>
<p>VENDOR REQUESTs for review</p>
<p>15 IFVENDOR, TWO 000000002</p>
<p>16 IFVENDOR, FOUR 000000004</p>
<p>17 IFVENDOR, FIVE 000000005</p>
<p>18 IFVENDOR, SIX 000000006</p>
<p>19 IFVENDOR, SEVEN 000000007</p>
<p>20 IFVENDOR, EIGHT 000000008</p>
<p>21 IFVENDOR1, FIVE 000000015</p>
<p>22 IFVENDOR, TEN 000000010</p>
<p>23 IFVENDOR1, SIX 000000016</p>
<p>RE Review Entry SD Send VENDOR REQUEST PE Print Entry</p>
<p>EV Edit Vendor Request DE Delete VENDOR REQUEST</p></td>
</tr>
<tr class="odd">
<td>Select VRQ Action: Next Screen//</td>
</tr>
</tbody>
</table>

#### Print Vendor Request

To print a copy of the Vendor request, enter PE at the Select VRQ Action: prompt.

<span id="_Toc222493091" class="anchor"></span>Figure 61: Send Vendor Request (SD)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VENDOR REQUESTs for review</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>+ Vendor Name FMS Vendor TAX/SSN</p>
<p>15 IFVENDOR, TWO 000000002</p>
<p>16 IFVENDOR, FOUR 000000004</p>
<p>17 IFVENDOR, FIVE 000000005</p>
<p>18 IFVENDOR, SIX 000000006</p>
<p>19 IFVENDOR, SEVEN 000000007</p>
<p>20 IFVENDOR, EIGHT 00000000</p>
<p>21 IFVENDOR1, FIVE 000000015</p>
<p>22 IFVENDOR, TEN 000000010</p>
<p>23 MICROBIOLOGY LABS 000000016</p>
<p>+ Enter ?? for more actions</p>
<p>RE Review Entry SD Send VENDOR REQUEST PE Print Entry</p>
<p>EV Edit Vendor Request DE Delete VENDOR REQUEST</p></td>
</tr>
<tr class="even">
<td>Select VRQ Action: Next Screen//pe Print Entry</td>
</tr>
<tr class="odd">
<td>Select (s): (15-28): 23</td>
</tr>
<tr class="even">
<td>Select a printer: sf</td>
</tr>
<tr class="odd">
<td><p>1 SFCS6$PRT-10/6/UP SF CIOFO</p>
<p>2 SFCS6$PRT-12/6/UP SF CIOFO</p>
<p>3 SFCS6$PRT-16/6/UP SF CIOFO</p></td>
</tr>
<tr class="even">
<td>Choose 1-3&gt; 1 SFCS6$PRT-10/6/UP SF CIOFO</td>
</tr>
</tbody>
</table>

#### Quit from Review Vendor Request

To exit from the review option, enter Q (for Quit) at the Select VRQ Action: prompt.

<span id="_Toc222493092" class="anchor"></span>Figure 62: Quit Review Vendor Request (Q)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VENDOR review Jun 21, 2000, 14:15:41 Page: 1 of 3</p>
<p>VENDOR REQUESTs for review</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Vendor Name FMS Vendor TAX/SSN</p>
<p>1 IFVENDOR1, SEVEN 000000017</p>
<p>2 IFVENDOR1, EIGHT 000000018</p>
<p>3 IFVENDOR1, NINE 000000019</p>
<p>+ Enter ?? for more actions</p>
<p>RE Review Entry SD Send VENDOR REQUEST PE Print Entry</p>
<p>EV Edit Vendor Request DE Delete VENDOR REQUEST</p></td>
</tr>
<tr class="even">
<td>Select VRQ Action: Next Screen// q Q</td>
</tr>
</tbody>
</table>

## Setup Accounts Receivable Selected Vendor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option handles creation and editing of a VRQ for vendor records chosen by Accounts Receivable users. Once the VRQ is created, it will be reviewed by Fiscal or sent directly to Austin. The “CAN FISCAL ADD VENDORS?” flag in the ADMIN. ACTIVITY SITE PARAMETER (#411) file will govern whether Fiscal Service or Supply Service edits these vendor records. If the flag is set to YES, Fiscal will edit these records. Otherwise, Supply will have the honor. Fiscal will be able to review the Vendor Request, edit the Vendor entry, delete the request or send the VRQ to Austin. The option works the same way as the Review Vendor Request option.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Select EDIT Action: prompt, enter ER to edit the record.

<span id="_Toc222493093" class="anchor"></span>Figure 63: Setup AR Selected Vendor

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Utilities Menu Option: setup AR selected vendors</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Edit vendor selected by AR users</p>
<p>Vendor Name TAX/SSN VRQ DATA VRQ SENT</p>
<p>1</p>
<p>2 IFVENDOR1, FIVE 000000015 OK SENT</p>
<p>3 IFVENDOR2, ONE 000000021 OK</p>
<p>4 IFVENDOR1, TWO</p>
<p>Enter ?? for more actions</p></td>
</tr>
<tr class="even">
<td><p>ER EDIT Record PE Print Entry DR Delete EDIT Request</p>
<p>RR Review Record SV Send VRQ</p>
<p>Select EDIT Action: Quit// er EDIT Record</p>
<p>Select :(1-4): 3</p></td>
</tr>
<tr class="odd">
<td><p>Vendor Name: IFVENDOR2, ONE</p>
<p>Review the vendor selected? YES//</p></td>
</tr>
<tr class="even">
<td><p>Vendor Name: IFVENDOR2, ONE PAGE: 1</p>
<p>Ordering Address: 1234 THIS STREET</p>
<p>City, State, ZIP: CHARLES, MARYLAND 20678</p>
<p>FMS Name:</p>
<p>* Payment ADDRESS: 1117S JEFFERSON ST</p>
<p>* City, State, ZIP: ROANOKE, VIRGINIA 24011</p>
<p>PAYMENT CONTACT PERSON:</p>
<p>PAYMENT PHONE NUMBER:</p>
<p>* = REQUIRED FIELD</p>
<p>Enter RETURN to continue or '^' to exit:</p></td>
</tr>
<tr class="odd">
<td><p>Vendor Name: IFVENDOR2, ONE PAGE: 2</p>
<p>FMS VENDOR CODE:</p>
<p>ALT-ADDR-IND:</p>
<p>* TAX ID/SSN: 000000021</p>
<p>* SSN/TAX ID IND: SOCIAL SECURITY NUMBER</p>
<p>NON-RECURRING/</p>
<p>RECURRUNG VENDOR: RECURRING</p>
<p>1099 VENDOR INDICATOR: YES</p>
<p>* VENDOR TYPE: COMMERCIAL</p>
<p>DUN &amp; BRADSTREET:</p>
<p>* = REQUIRED FIELD</p>
<p>Enter RETURN to continue:</p>
<p>Edit the Vendor record? YES//</p></td>
</tr>
<tr class="even">
<td><p>Setup AR selected vendors</p>
<p>TAX ID/SSN: 000000021//</p>
<p>SSN/TAX ID INDICATOR: SOCIAL SECURITY NUMBER//</p>
<p>FMS VENDOR CODE:</p>
<p>ALT-ADDR-IND:</p>
<p>PAYMENT CONTACT PERSON:</p>
<p>PAYMENT PHONE NO.: 703 555 5555//</p>
<p>ORDERING ADDRESS: 1234 THIS STREET</p>
<p>CHARLES, MARYLAND 20678</p>
<p>PAYMENT ADDRESS1: 1117S JEFFERSON ST//</p>
<p>PAYMENT ADDRESS2:</p>
<p>PAYMENT CITY: ROANOKE//</p>
<p>PAYMENT STATE: VIRGINIA//</p>
<p>PAYMENT ZIP CODE: 24011//</p>
<p>1099 VENDOR INDICATOR: YES//</p>
<p>VENDOR TYPE: COMMERCIAL//</p>
<p>DUN &amp; BRADSTREET #:</p>
<p>RR Review Record SV Send VRQ</p></td>
</tr>
<tr class="odd">
<td><p>PRCO VENDOR EDIT FOR AR Jun 21, 2000, 14:23:14 Page: 1 of 1</p>
<p>Edit vendor selected by AR users</p>
<p>Vendor Name TAX/SSN VRQ DATA VRQ SENT</p>
<p>1 IFVENDOR1, TEN</p>
<p>2 IFVENDOR1, FIVE 000000015 OK SENT</p>
<p>3 IFVENDOR2, ONE 000000021 OK</p>
<p>4 IFVENDOR1, TWO</p></td>
</tr>
<tr class="even">
<td><p>Enter ?? for more actions</p>
<p>ER EDIT Record PE Print Entry DR Delete EDIT Request</p>
<p>RR Review Record SV Send VRQ</p></td>
</tr>
<tr class="odd">
<td>Select EDIT Action: Quit//</td>
</tr>
</tbody>
</table>

## Transaction Report – eCMS/IFCAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report displays information about HL7 transactions that occur between eCMS and IFCAP at your station. This option is available to Fiscal users who have the PRCHJFIS Security Key. The report is generated from data stored in the IFCAP/ECMS TRANSACTION (#414.06) file.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A report can be generated for a single 2237, a single eCMS Contact, a date range, a specific Station Number, a specific fund control point, a specific messaging Event type, multiple Event types or ALL the records.

> **NOTE:** if your Station is using the IFCAP sub-station functionality, a report can be generated for a specific sub-station.

> **NOTE:** At the DEVICE: HOME// prompt, the report can either be displayed to the screen or sent to a printer. The latter choice is appropriate when the report is long.

<span id="_Toc222493094" class="anchor"></span>Figure 64: eCMS/IFCAP Transaction Report

Select Accounting Utilities Menu \<TEST ACCOUNT\> Option: Transaction Report - eCMS

/IFCAP

Select a single 2237 TRANSACTION NUMBER? NO//

Select a single eCMS Contact? NO//

Select ALL DATES: (SEP 04, 2012 - JUL 26, 2013)? NO//

Starting date: TODAY/ (JUL 01, 2013)

Ending date: TODAY// (JUL 26, 2013)

Select a single STATION NUMBER? NO//

Select a single FUND CONTROL POINT? NO//

TRANSACTION EVENTS:

1 Sent to eCMS (includes re-sent 2237s)

2 Returned to Accountable Officer

3 Returned to Control Point

4 Cancelled within eCMS

Select one or more of the above events: 1-4// 2,3

Display event ERROR TEXT? NO//

All eCMS 2237s matching your selections below will be displayed:

All eCMS Contacts

Dates: (JUL 01, 2013 - JUL 26, 2013)

All Stations and Substations

All Fund Control Points

Event Types selected are:

2 = Returned to Accountable Officer

3 = Returned to Control Point

A note will display any errors, but not the full text.

DEVICE: HOME// TELNET RIGHT MARGIN: 80//

JUL 26, 2013@10:54 eCMS/IFCAP TRANSACTION LOG REPORT p. 1

eCMS 2237: ALL eCMS Contact: ALL Station: ALL

Report Date Range: JUL 01, 2013 - JUL 26, 2013, Control Point: ALL

Events: Returned to AO, Returned to CP

IFCAP Reference Message Event Event Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

886-13-4-013-0034 RETURN TO CONTROL POINT JUL 02, 2013@17:33:10

ACKNOWLEDGED: JUL 02, 2013@17:33:11

eCMS CONTACT: eCMS.User1@med.va.gov PHONE: 501-234-5678

RETURN/CANCEL DATE: JUL 02, 2013@16:33:08

REASON: Returned to the Control Point Level in IFCAP

987-13-4-013-0035 RETURN TO CONTROL POINT JUL 02, 2013@18:17:43

ACKNOWLEDGED: JUL 02, 2013@18:17:44

eCMS CONTACT: Ecms.User2@med.va.gov PHONE: 444-333-2222

RETURN/CANCEL DATE: JUL 02, 2013@17:17:39

REASON: Returned to the Control Point Level in IFCAP

Enter RETURN to continue or '^' to exit:

JUL 26, 2013@10:54 eCMS/IFCAP TRANSACTION LOG REPORT p.5

eCMS 2237: ALL eCMS Contact: ALL Station: ALL

Report Date Range: JUL 01, 2013 - JUL 26, 2013, Control Point: ALL

Events: Returned to AO, Returned to CP

IFCAP Reference Message Event Event Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

987-13-4-013-0058 RETURN TO ACCOUNTABLE OFFICER JUL 17, 2013@13:55:28

ACKNOWLEDGED: JUL 17, 2013@13:55:29

eCMS CONTACT: Ecms.User7@med.va.gov PHONE: 987-654-3210

RETURN/CANCEL DATE: JUL 17, 2013@12:55:24

REASON: Returned to the Accountable Officer Level in IFCAP

This RETURN TO ACCOUNTABLE OFFICER has ACKNOWLEDGMENT ERROR TEXT.

987-13-4-019-0021 RETURN TO CONTROL POINT JUL 11, 2013@18:12:48

ACKNOWLEDGED: JUL 11, 2013@18:12:49

eCMS CONTACT: Ecms.User1@med.va.gov PHONE: 501-234-5678

RETURN/CANCEL DATE: JUL 11, 2013@17:12:47

REASON: Returned to the Control Point Level in IFCAP

Enter RETURN to continue or '^' to exit:

JUL 26, 2013@10:54 eCMS/IFCAP TRANSACTION LOG REPORT p. 8

eCMS 2237: ALL eCMS Contact: ALL Station: ALL

Report Date Range: JUL 01, 2013 - JUL 26, 2013, Control Point: ALL

Events: Returned to AO, Returned to CP

IFCAP Reference Message Event Event Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

987-13-4-081-0040 RETURN TO CONTROL POINT JUL 11, 2013@17:10:55

ACKNOWLEDGED: JUL 11, 2013@17:10:56

eCMS CONTACT: Ecms.User9@med.va.gov PHONE: xxx xxx-xxxx

RETURN/CANCEL DATE: JUL 11, 2013@16:10:53

REASON: Returned to the Control Point Level in IFCAP

987-13-4-5082-0027 RETURN TO CONTROL POINT JUL 11, 2013@16:07:38

ACKNOWLEDGED: JUL 11, 2013@16:07:39

eCMS CONTACT: Ecms.User11@med.va.gov PHONE: xxx xxx-xxxx

RETURN/CANCEL DATE: JUL 11, 2013@15:07:34

REASON: Returned to the Control Point Level in IFCAP

END OF REPORT

# FMS Code Sheet Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is possible to create FMS documents manually using the FMS Code Sheet Menu. These options should be used only for creating those FMS documents that IFCAP does not generate automatically (*e.g.*, AO, TO).

Use of the manual code sheet option may mean you have to enter more fields on the document than you would enter if creating the document directly on-line in FMS. Although the menu refers to “code sheets,” you are actually creating FMS documents. Using the options on this menu you may create, edit, delete, review, retransmit and purge the documents. Documents created using this menu are stored in the Generic Code Sheet (#2100.1) file and appear on the Stack Status Report in the same way as the documents generated automatically.

## Menu Choices 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222493095" class="anchor"></span>Figure 65: FMS Code Sheet Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Technician Menu Option: FMS Code Sheet Menu</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Code Sheet Edit<br />
Create a Code Sheet<br />
Delete a Code Sheet<br />
Purge Transmission Records/Code Sheets<br />
Retransmit Stack File Document<br />
Review a Code Sheet<br />
Stack Status Report<br />
User Comments</td>
</tr>
</tbody>
</table>

### Transmission Records/Code Sheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine will delete Code Sheets from the Code Sheet file and Batch and Transmission records from the Transmission Record file. Deletion is based on the date a batch and a code sheet is created.

### Enter Parameters and Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a STATION NUMBER.

At the Batch Type: prompt, enter FINANCIAL MANAGEMENT.

At the Enter the number of days you wish to retain code sheets: prompt, enter the number of days you wish to retain code sheets.

<span id="_Toc222493096" class="anchor"></span>Figure 66: FMS Code Sheet Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER (^ TO EXIT): ALBANY.VA.GOV// NY VAMC 500</p>
<p>Station: ALBANY.VA.GOV (#500)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Batch Type: FINANCIAL MANAGEMENT</td>
</tr>
<tr class="even">
<td>Enter the number of days you wish to retain code sheets: (0-999999): 365//</td>
</tr>
<tr class="odd">
<td><p>This program will remove all stack file entries which were created before</p>
<p>JUN 22, 1999. I will now delete all code sheets and associated records which were created before JUN 22, 1999, for station 500.</p></td>
</tr>
<tr class="even">
<td>OK to continue? YES//</td>
</tr>
</tbody>
</table>

### Retransmit Stack File Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to retransmit a document, you can use this option to select a document in the Generic Code Sheet (#2100.1) file and retransmit the document. It will reset the Current Status to TRANSMITTED.

> **NOTE:** Documents with a current status of “FINAL - NO FURTHER ACTIVITY ALLOWED” cannot be retransmitted.

<span id="_Toc222493097" class="anchor"></span>Figure 67: Retransmit Stack File Document

| Select FMS Code Sheet Menu Option: retransmit Stack File Document |
|-------------------------------------------------------------------|
| Select Stack Document for Retransmission: ET-66BJJJ1003           |
| Current Status: REJECTED BY FMS                                   |
| Do you want to retransmit this document now? NO// y (YES)         |
| NEW Status: TRANSMITTED                                           |

### User Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option permits you to add text to the FMS document record in the Generic Code Sheet (#2100.1) file.

<span id="_Toc222493098" class="anchor"></span>Figure 68: User Comments

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select FMS Code Sheet Menu Option: User Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select Stack Document: ET-</p>
<p>1 ET-66BJJJ1001</p>
<p>2 ET-66BJJJ1002</p>
<p>3 ET-66BJJJ1003</p>
<p>4 ET-66BJJJ1004</p>
<p>5 ET-66BJJJ1005</p>
<p>Press &lt;RETURN&gt; to see more, '^' to exit this list, OR</p></td>
</tr>
<tr class="even">
<td>CHOOSE 1-5: 1 ET-66BJJJ1001</td>
</tr>
<tr class="odd">
<td><p>Current Status: REJECTED BY FMS</p>
<p>USER COMMENTS: do not correct or retransmit this document</p></td>
</tr>
</tbody>
</table>

# # The Logistics Data Query Tool 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Logistics Data Query Tool is designed to assist Chief Logistics Officers; Materiel Managers; Purchasing Agents; and members of the Facility Logistics Staff (including Inventory Managers; Supply, Processing, and Distribution (SPD) Technicians; Management Analysts; Warehouse Clerks; or Supply System Analysts). The Query Tool can be used to quickly access, analyze and verify IFCAP and Prosthetics procurement data and display it using a graphical user interface to the VistA data. You can sign-on to VistA, find data, view the data, or easily move the data into a Microsoft® Excel® spreadsheet.

The Query Tool is a Windows software application that acts as a “front-end” to enable you to more easily find, display, and export VistA data. The Query Tool is a substitute for the VA FileMan utility program which has traditionally been used to look directly at the MUMPS globals (files) which store VistA data. The Query Tool enables you to:

- Search for data and display data by a range of dates
- Sort and rearrange the view of the data; display the data in a custom view
- Exporting the data into a Microsoft Excel spreadsheet file

Information on what the Query Tool can do for you can be found in the Logistics Data Query Tool Manual.

\*The Logistics Data Query Tool Manual is available online at…

[<u>VA Software Document Library - IFCAP</u>](https://www.va.gov/vdl/application.asp?appid=42).

> **NOTE:** The PRCHL LOGISTICS DATA TOOL \[PRCHL GUI\] option has been marked Out of Order with patch PRC\*5.1\*247.

# Menu Outline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter lists each menu option assigned the standard menu configuration for an Accounting Technician. Main menu options are flush left. Subordinate options are spaced to the right. For example, if you wanted to use the “Single Receiving Report Reprint in Fiscal” option, you would select “Reprint Menu”, then “Receiving Report Reprint Menu”, then “Single Receiving Report Reprint in Fiscal”.

> **NOTE:** The Fee Basis - IFCAP Code Sheet Menu \[PRC FEE GECS MAIN MENU\] and all associated options were removed from the Accounting Technician Menu \[PRCFA ACCTG TECH\] as this functionality is no longer necessary.

<span id="_Toc222493099" class="anchor"></span>Figure 69: Accounting Technician Menu Outline

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select Accounting Technician Menu Option: ?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Document Processing Menu ...</p>
<p>1358 Processing Menu ...</p>
<p>Obligate 1358</p>
<p>Adjust (Increase/Decrease) 1358</p>
<p>Liquidate 1358</p>
<p>1358 Print Menu ...</p>
<p>Build List of 1358's Printed in Fiscal by Date</p>
<p>Print/Reprint 1358s from List</p>
<p>1358 Balance</p>
<p>Display/Print 1358</p>
<p>Close 1358</p>
<p>Recalculate 1358 Balances</p>
<p>Reopen a Closed 1358</p>
<p>Send 1358 back to Service without action</p>
<p>Amendment Processing</p>
<p>General Post Funds Requests Processing</p>
<p>Invoice Processing (ACCTG) Menu ...</p>
<p>Invoice Processing for Payment</p>
<p>Return Invoice to Voucher Audit</p>
<p>Payment Voucher (PV) Inquiry</p>
<p>FMS Payment Voucher Error Processing</p>
<p>View Certified Invoice</p>
<p>Review VENDOR REQUEST</p>
<p>Obligation Processing</p>
<p>Process Receiving Report</p>
<p>Return Purchase Order to Supply</p>
<p>Return PO Amendment to Supply</p>
<p>Stacked Fiscal Documents Menu ...</p>
<p>Print Stacked Fiscal Documents</p>
<p>Delete Stacked Fiscal Documents</p>
<p>FMS Rejected Obligation Document Processing ...</p>
<p>FMS Inquiry Rejected Obligation Documents ...</p>
<p>MO/SO Rejected Document Inquiry for P.O.</p>
<p>SO Rejected Document Inquiry for 1358s</p>
<p>ET-FMS Document Display</p>
<p>AR Rejected Document Inquiry</p>
<p>FMS Rebuild/Transmit Rejected Obligation Documents ...</p>
<p>MO/SO Rebuild/Transmit for P.O.</p>
<p>SO Rebuild/Transmit for 1358s</p>
<p>AR Rebuild/Transmit for PO/1358</p>
<p>ET-FMS Document Rebuild</p>
<p>Accounting Utilities Menu ...</p>
<p>Update Status of Funds Balances</p>
<p>Lookup Vendor ID Number</p>
<p>Vendor File Edit</p>
<p>Edit BOC in Item File</p>
<p>Clear Program Lock</p>
<p>Undelivered Orders Reconciliation Report</p>
<p>Fiscal Pending Action</p>
<p>History - Code Sheet/Obligation (PAT) Number</p>
<p>Review VENDOR REQUEST</p>
<p>Setup AR selected vendors</p>
<p>Transaction Report – eCMS/IFCAP</p></td>
</tr>
<tr class="even">
<td><p>Reprint Menu ...</p>
<p>Purchase Order Reprint Menu ...</p>
<p>Resend P.O. to Fiscal</p>
<p>Build List of POs Printed in Fiscal by Date</p>
<p>Print POs in Fiscal from List by Date</p>
<p>Single P.O. Reprint in P&amp;C</p>
<p>Receiving Report Reprint Menu ...</p>
<p>Single Receiving Report Reprint in Fiscal</p>
<p>Build List of Recv. Reports to Reprint by Date</p>
<p>Reprint Recv. Report on Fiscal from List</p>
<p>List of Receiving Reports Not Processed by Fiscal</p>
<p>History of Transmitted Receiving Reports</p>
<p>1358 Print Menu ...</p>
<p>Build List of 1358's Printed in Fiscal by Date</p>
<p>Print/Reprint 1358s from List</p>
<p>1358 Balance</p>
<p>Display/Print 135</p>
<p>Display 2237 Request</p>
<p>Receiving Report Transmission Menu ...</p>
<p>Change Transmission Date of Queued Receiving Rpt</p>
<p>Delete Receiving Report from Transmission List</p>
<p>Print Receiving Report Transmission List</p>
<p>Queue Single Receiving Report for Transmission</p>
<p>&gt; Out of order: No longer available, partial filing non-compliant</p>
<p>Re-transmit Single Receiving Report</p>
<p>Transmit Receiving Reports on Transmission List</p></td>
</tr>
<tr class="odd">
<td><p>FMS Code Sheet Menu ...</p>
<p>Code Sheet Edit</p>
<p>Create a Code Sheet</p>
<p>Delete a Code Sheet</p>
<p>Purge Transmission Records/Code Sheets</p>
<p>Retransmit Stack File Document</p>
<p>Review a Code Sheet</p>
<p>Stack Status Report</p>
<p>User Comments</p>
<p>IRS Offset Code Sheet Menu ...</p>
<p>Batch and Print Code Sheets</p>
<p>Retransmit Code Sheets Batch to Austin</p>
<p>Transmit Code Sheets to Austin</p>
<p>Print Obligated 1358s</p>
<p>Purchase Card Transactions Print Menu ...</p>
<p>Detailed Report on Unpaid PC Transactions by FCP</p>
<p>Fiscal Daily Review</p>
<p>History of Purchase Card Transactions</p>
<p>Reconciled Purchase Card Transactions</p>
<p>Unreconciled Purchase Card Transactions</p>
<p>ET-FMS Document Display</p>
<p>ET-FMS Document Rebuild</p>
<p>Purchase Card Transaction Status</p>
<p>Monitor Reconciled Orders by Card Holder</p>
<p>BOC Report for OA&amp;MM/Fiscal</p></td>
</tr>
<tr class="even">
<td>Select Accounting Technician Menu Option: ?</td>
</tr>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary defines terms in this manual that users might find unfamiliar.
0-9
| Term | Definition / Discussion                                                                                   |
|----------|---------------------------------------------------------------------------------------------------------------|
| 1358     | VA Form 1358, Estimated Obligation or Change in Obligation                                                    |
| 2138     | VA Form 90-2138, *Order for Supplies or Services* (first page of a VA Purchase Order)                         |
| 2139     | VA Form 90-2139, *Order for Supplies or Services* (Continuation) (continuation sheet for Form 90-2138)        |
| 2237     | VA Form 90-2237, *Request, Turn-in and Receipt for Property or Services* (used to request goods and services) |
A
| Term                                             | Definition / Discussion                                                                                                                                                                                                 |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A&MM                                                 | *See* Acquisition and Materiel Management (Service)                                                                                                                                                                         |
| AACS                                                 | Automated Allotment Control System—Central computer system developed by VHA to disburse funding from VACO to field stations.                                                                                                |
| Accounting Technician                                | Fiscal employee responsible for obligation and payment of received goods and services.                                                                                                                                      |
| Acquisition and Materiel Management (Service) (A&MM) | VA Service is responsible for contracting and for overseeing the acquisition, storage, and distribution of supplies, services, and equipment used by VA facilities                                                          |
| Activity Code                                        | The last two digits of the AACS number. It is defined by each station.                                                                                                                                                      |
| ADP Security Officer                                 | The individual at your station that is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored on it. Includes overseeing file access.                     |
| Agent Cashier                                        | The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.                                                                           |
| ALD Code                                             | Appropriation Limitation Department. A set of Fiscal codes which identifies the appropriation used for funding.                                                                                                             |
| Allowance table                                      | Reference table in FMS that provides financial information at the level immediately above the AACS, or sub-allowance level.                                                                                                 |
| Amendment                                            | A document which changes the information contained in a specified Purchase Order. Amendments are processed by the Purchasing & Contracting section of A&MM and obligated by Fiscal Service.                                 |
| AMIS                                                 | Automated Management Information System.                                                                                                                                                                                    |
| Application Coordinator                              | The individuals responsible for the implementation, training and troubleshooting of a software package within a service. IFCAP requires there to be an Application Coordinator designated for Fiscal Service, A&MM Service. |
| Approve Requests                                     | The use of an electronic signature by a Control Point Official to approve a 2237, 1358 or another request form and transmit said request to A&MM/Fiscal.                                                                    |
| Approving Official                                   | A user that approves reconciliations to ensure that they are correct and complete.                                                                                                                                          |
| Authorization                                        | Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.                                     |
| Authorization Balance                                | The amount of remaining money that can be authorized against the 1358 form. The service balance minus total authorizations.                                                                                                 |
B
| Term             | Definition / Discussion                                                                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Batch Number         | A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number. |
| Breakout Code        | A set of A&MM codes which identifies a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.). |
| Budget Analyst       | Fiscal employee responsible for distributing and transferring funds.                                                                                        |
| Budget Object Code   | Fiscal accounting element that tells what kind of item or service is being procured. Budget object codes are listed in VA Handbook 4671.2                   |
| Budget Sort Category | Used by Fiscal Service to identify the allocation of funds throughout their facility.                                                                       |
C
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CC</td>
<td>Credit Charge entry identifier used by FMS and CCS for charges paid to Vendor through Credit Card payment process.</td>
</tr>
<tr class="even">
<td>CCS</td>
<td>The Credit Card System. This is the database in Austin that processes credit card information from the external Credit Card Vendor system (currently CitiDirect) and then passes information on to FMS and IFCAP.</td>
</tr>
<tr class="odd">
<td>Ceiling Transactions</td>
<td>Funding distributed from Fiscal Service to IFCAP Control Points for spending. The Budget Analyst initiates these transactions using the Funds Distribution options.</td>
</tr>
<tr class="even">
<td>Chief Logistics Office (CLO)</td>
<td><p>The Chief Logistics Office (CLO) develops and fosters logistics best practices for the Veterans Health Administration. Through the VHA Acquisition Board the CLO develops the annual VHA Acquisition plan that forms the basis for VHA’s acquisition strategy. This strategy seeks to provide high quality health care products and services in the most cost-effective manner. This includes the attainment of socio-economic procurement goals. The CLO also develops and implements a comprehensive plan for the standardization of healthcare supplies and equipment. This includes the development and administration of clinical product user groups.</p>
<p>The CLO is also responsible for developing improvements to supply chain management within VHA. This includes the establishment and monitoring of logistics benchmarking data. The CLO serves as liaison for logistics staff in each of the 21 VISNs.</p>
<p>The head of CLO is the Chief Prosthetics and Clinical Logistics Officer (CPCLO).</p></td>
</tr>
<tr class="odd">
<td>Chief Prosthetics and Clinical Logistics Officer (CPCLO)</td>
<td>The official in charge of the VHA <strong>Chief Logistics Office (CLO)</strong>, also called the Clinical Logistics Office.</td>
</tr>
<tr class="even">
<td>CLA</td>
<td><em>See</em> Clinical Logistics Analyst</td>
</tr>
<tr class="odd">
<td>Classification of Request</td>
<td>An identifier a Control Point can assign to track requests that fall into a category (<em>e.g.</em>, Memberships, Replacement Parts, Food Group III).</td>
</tr>
<tr class="even">
<td>Clinical Logistics Analyst (CLA)</td>
<td><em>Logistics</em> refers to how resources are acquired, transported and stored along the supply chain. By having an efficient supply chain and proper logistical procedures, an organization can cut costs and increase efficiency. <em>Clinical logistics</em> refers specifically to resources used for clinical purposes. A CLA is a person who examines processes, methods and data for clinical logistics operations.</td>
</tr>
<tr class="odd">
<td>Clinical Logistics Office</td>
<td><em>See</em> Chief Logistics Office (CLO).</td>
</tr>
<tr class="even">
<td>Clinical Logistics Report Server (CLRS)</td>
<td>The CLRS project allows the extraction of selected procurement and inventory data from VHA facilities to a centralized Clinical Logistics Report Server. The server supports the collection, tracking, and reporting of National Performance Measures, assisting the Under Secretary for Health (USH) in evaluating facility performance in the areas of consolidation of high-tech equipment, standardization, socioeconomic goal accomplishment, acquisition, and inventory management.</td>
</tr>
<tr class="odd">
<td>CLRS</td>
<td><em>See</em> Clinical Logistics Report Server (CLRS).</td>
</tr>
<tr class="even">
<td>Common Numbering Series</td>
<td>This is a pre-set series of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinators establish the Common Numbering Series used by each facility.</td>
</tr>
<tr class="odd">
<td>Control Point</td>
<td>Financial element, existing ONLY in IFCAP, which corresponds to a set of elements in FMS that include the Account Classification Code (ACC) and define the Sub-Allowance on the FMS system. Used to permit the tracking of monies to a specified service, activity or purpose from an Appropriation or Fund.</td>
</tr>
<tr class="even">
<td>Control Point Clerk</td>
<td>The user within the service is designated to input requests (2237s) and maintain the Control Point records for a Service.</td>
</tr>
<tr class="odd">
<td>Control Point Official</td>
<td>The individual authorized to expend government funds for ordering supplies and services for their Control Point(s). This person has all the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.</td>
</tr>
<tr class="even">
<td>Control Point Official’s Balance</td>
<td>A running record of all the transactions generated and approved for a Control Point from within IFCAP. Effects changes to the control point that are initiated directly from within the FMS system. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.</td>
</tr>
<tr class="odd">
<td>Control Point Requestor</td>
<td>The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. This user can only view or edit their own requests. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&amp;MM.</td>
</tr>
<tr class="even">
<td>Cost Center</td>
<td>Cost Centers are unique numbers which define a service. One cost center must be attached to every Fund Control Point. This enables costs to be captured by service. Cost centers are listed in VA Handbook 4671.1.</td>
</tr>
</tbody>
</table>
D
| Term                    | Definition / Discussion                                                                                                                                                 |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Date Committed              | The date that you want IFCAP to commit funds to the purchase.                                                                                                               |
| Default                     | A suggested response that is provided by the system.                                                                                                                        |
| Deficiency                  | When a budget has obligated and expended more than it was funded.                                                                                                           |
| Delinquent Delivery Listing | A listing of all the Purchase Orders that have not had all the items received by the Warehouse on IFCAP. It is used to contact the vendor for updated delivery information. |
| Delivery Order              | An order for an item that the VA purchases through an established contract with a vendor who supplies the items.                                                            |
| Direct Delivery Patient     | A patient who has been designated to have goods delivered directly to him/her from the vendor.                                                                              |
| Discount Item               | This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.                 |
E
| Term                          | Definition / Discussion                                                                                                                                                                                   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| eCMS                              | The VA’s electronic Contract Management System hosted at the Austin Information Technology Center in Austin, Texas.                                                                                           |
| EDI                               | *See* Electronic Data Interchange (EDI).                                                                                                                                                                      |
| EDI Vendor                        | A vendor with whom the VA has negotiated an arrangement to submit, accept and fill orders electronically.                                                                                                     |
| EDI X12                           | “X12” is the U.S. standard ANSI ASC X12, which is the predominant standard used in North America. Thus, “EDI X12” refers to electronic data interchanges which meet the X12 standard. Also seen as “X12 EDI.” |
| Electronic Data Interchange (EDI) | Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.                                                                           |
| Electronic Signature              | The electronic signature code replaces the written signature on all IFCAP documents used within your facility. Documents going off station will require a written signature as well.                          |
| Expenditure Request               | A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).                                                                                      |
F
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FCP</td>
<td>Fund Control Point (see Control Point).</td>
</tr>
<tr class="even">
<td>Federal Tax ID</td>
<td>A unique number that identifies your station to the Internal Revenue Service.</td>
</tr>
<tr class="odd">
<td>FileMan</td>
<td><p>The FileMan modules are the “building blocks” for all of VistA. FileMan includes both a database management system (DBMS) and user interface.</p>
<p><em>Source:</em> <a href="http://www.hardhats.org/fileman/FMmain.html">http://www.hardhats.org/fileman/FMmain.html</a></p></td>
</tr>
<tr class="even">
<td>Fiscal Balance</td>
<td>The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidations submitted against the obligation.</td>
</tr>
<tr class="odd">
<td>Fiscal Quarter</td>
<td>The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.</td>
</tr>
<tr class="even">
<td>Fiscal Year</td>
<td>Twelve-month period from October 1 to September 30.</td>
</tr>
<tr class="odd">
<td>FMS</td>
<td>Financial Management System, the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.</td>
</tr>
<tr class="even">
<td>FOB</td>
<td><strong>Freight on Board.</strong> A FOB of “Destination” means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. A FOB of “Origin” means the Vendor has paid shipping costs directly to the shipper and then will include them on their Invoice.</td>
</tr>
<tr class="odd">
<td>FPDS</td>
<td>Federal Procurement Data System.</td>
</tr>
<tr class="even">
<td>FTEE</td>
<td>Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned to an FTEE of 0.5, as would a full-time employee that worked for half of a year.</td>
</tr>
<tr class="odd">
<td>Fund Control Point</td>
<td>IFCAP accounting element that is not used by FMS. See also control point.</td>
</tr>
<tr class="even">
<td>Funds Control</td>
<td>A group of Control Point options that allow the Control Point Clerk and/or Official to maintain and reconcile their funds.</td>
</tr>
<tr class="odd">
<td>Funds Distribution</td>
<td>A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.</td>
</tr>
</tbody>
</table>
G
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GBL</td>
<td>Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of $250.00.</td>
</tr>
<tr class="even">
<td>GL</td>
<td>General Ledger.</td>
</tr>
<tr class="odd">
<td>Globals</td>
<td><p>Globals are variables which are automatically and transparently stored on disk and persist beyond program, routine, or process completion. Globals are used exactly like ordinary variables, but with the caret character prefixed to the variable name.</p>
<p>Globals are stored in highly structured data files by MUMPS and accessed only as MUMPS globals. VistA file definitions and data are both stored in globals.</p></td>
</tr>
</tbody>
</table>
I
| Term                                   | Definition / Discussion                                                                                                                                                                                   |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Identification Number                      | A computer-generated number assigned to a code sheet.                                                                                                                                                         |
| IFCAP                                      | VA’s Integrated Funds Distribution Control Point Activity, Accounting and Procurement system.                                                                                                                 |
| Imprest Funds                              | Monies used for cash or 3<sup>rd</sup> party draft purchases at a VA facility.                                                                                                                                |
| Integrated Supply Management System (ISMS) | ISMS is the system which replaced LOG I for Expendable Inventory.                                                                                                                                             |
| ISMS                                       | See Integrated Supply Management System.                                                                                                                                                                      |
| Item File                                  | A listing of items specified by A&MM service as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history. |
| Item History                               | Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.                                                            |
| Item Master Number                         | A computer-generated number used to identify an item in the Item File.                                                                                                                                        |
J
| Term      | Definition / Discussion                                                                                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Justification | A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source. |
K
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Kernel</td>
<td><p>The Kernel is the software “scaffolding” that supports all VistA applications. The Kernel system permits any VistA software application to run without modification to its base structure no matter what hardware or software vendor the application was built on.</p>
<p>The Kernel includes several management tools including device, menu, programming, operations, security/auditing, task, user, and system management. Its framework provides a structurally sound computing environment that permits controlled user access, menus for choosing various computing activities, the ability to schedule tasks, application development tools, and numerous other management and operation tools.</p>
<p><em>Source:</em> <a href="http://hardhats.org/kernel/KRNmain.html">http://hardhats.org/kernel/KRNmain.html</a></p></td>
</tr>
</tbody>
</table>
L
| Term    | Definition / Discussion                                                                                                                                        |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Liquidation | The amount of money posted to the 1358 or Purchase Order as a payment to the vendor. They are processed through payment/invoice tracking.                          |
| LOG I       | LOG I is the name of the Logistics A&MM computer located at the Austin Automation Center. This system continues to support the Consolidated Memorandum of Receipt. |
M
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>M</td>
<td>The Massachusetts General Hospital Utility Multi-Programming System, or alternatively M, is a programming language originally created for use in the healthcare industry. M is designed to make writing database-driven applications easy while simultaneously making efficient use of computing resources. The most outstanding, and unusual, design feature of M is that database interaction is transparently built into the language. Many parts of VistA are written in M.</td>
</tr>
<tr class="even">
<td>MailMan</td>
<td><p>Mailman is an integrated data channel in VistA for the distribution of:</p>
<ul>
<li><p>Patches (Kernel Installation and Distribution System or KIDS builds)</p></li>
<li><p>Software releases (<em>KIDS</em> builds)</p></li>
<li><p>Computer-to-computer communications (HL7 transfers, Servers, etc.)</p></li>
<li><p>Person-to-person messaging (email)</p></li>
</ul>
<p><em>Source:</em> <a href="http://www.hardhats.org/cs/mailman/MMmain.html">http://www.hardhats.org/cs/mailman/MMmain.html</a></p></td>
</tr>
<tr class="odd">
<td>Mandatory Source</td>
<td>A Federal Agency that sells supplies and services to the VA, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.</td>
</tr>
<tr class="even">
<td>MSC Confirmation Message</td>
<td>A MailMan message generated by the Austin Message Switching Center that assigns an FMS number to an IFCAP transmission of documents.</td>
</tr>
<tr class="odd">
<td>MSPV</td>
<td>Medical/Surgical Prime Vendor</td>
</tr>
<tr class="even">
<td>MUMPS</td>
<td><em>See</em> <strong>M.</strong></td>
</tr>
</tbody>
</table>
O
| Term                   | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obligation                 | The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of an Order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Obligation (Actual) Amount | The actual dollar figure that has been obligated by Fiscal Service for a Purchase Order. The Control Point’s records are updated with actual cost automatically when Fiscal obligates the document on IFCAP.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Obligation Number          | The six-character number assigned to orders, requisitions and 1358s. (i.e. C prefix number that Fiscal Service assigns to the 1358.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Option                     | A Vista Option is an application component defined in VA Kernel to control user and remote server access to VistA applications. Options can appear on menu “trees” of options, through which the user navigates to execute application software. Types of options include menu (to allow grouping of options); edit (to edit application files via VA FileMan); inquire (to query the database via VA FileMan); print (to execute reports via VA FileMan); run routine (to execute custom application software); server (to process remote procedure calls via MailMan); and Broker (to process GUI remote procedure calls via Kernel Broker). |
| Organization Code          | The accounting element that’s functionally comparable to Cost Center but is used to organize purchases by the budget that funded them, not the purposes for spending the funds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Outstanding 2237           | A&MM report that lists all the IFCAP generated 2237s pending action in A&MM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
P
| Term                      | Definition / Discussion                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Partial                       | A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.                                                                                                                                                                                                                                                    |
| Partial Date                  | The date that a warehouse clerk created a receiving report for a shipment.                                                                                                                                                                                                                                                                                              |
| PAT Number                    | Pending Accounting Transaction number – the primary FMS reference number. See also Obligation Number.                                                                                                                                                                                                                                                                   |
| Personal Property Management  | A section of A&MM Service that is responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support. |
| POA                           | Purchase Order Acknowledgment. The message is received electronically from an EDI vendor acknowledging the placement of an order.                                                                                                                                                                                                                                       |
| PPM                           | Personal Property Management, now referred to at most sites as Acquisition and Materiel Management Service.                                                                                                                                                                                                                                                             |
| Program Code                  | Accounting element that identifies the VA initiative or program that the purchase will support.                                                                                                                                                                                                                                                                         |
| Prompt Payment Terms          | The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).                                                                                                                                                    |
| Purchase Card                 | A card, like a credit card, that Purchase Card Users use to make purchases. Purchase Cards are not credit cards but debit cards that spend money out of a deposited balance of VA funds.                                                                                                                                                                                |
| Purchase Card Coordinator     | A person authorized by a VA station to monitor and resolve delinquent purchase card orders, help VA services record, edit and approve purchase card orders in a timely manner, assign purchase cards to IFCAP users, and monitor the purchase card expenses of VAMC services.                                                                                           |
| Purchase Card Orders          | Orders funded by a purchase card.                                                                                                                                                                                                                                                                                                                                       |
| Purchase Card User            | A person who uses a purchase card. Purchase Card Users are responsible for recording their purchase card orders in IFCAP.                                                                                                                                                                                                                                               |
| Purchase History Add (PHA)    | Information about purchase orders which is automatically sent to Austin for archiving. This same transaction is also used to send a PO for EDI processing.                                                                                                                                                                                                              |
| Purchase History Modify (PHM) | Information about amendments; it is automatically sent to Austin for archiving.                                                                                                                                                                                                                                                                                         |
| Purchase Order                | A government document authorizing the purchase of the goods or services at the terms indicated.                                                                                                                                                                                                                                                                         |
| Purchase Order Acknowledgment | Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).                                                                                                                                                                                                                                                  |
| Purchase Order Status         | The status of completion of a purchase order (e.g., Pending Contracting Officer’s Signature, Pending Fiscal Action, Partial Order Received, etc.).                                                                                                                                                                                                                      |
| Purchasing Agents             | A&MM employees that are legally empowered to create purchase orders to obtain goods and services from commercial vendors.                                                                                                                                                                                                                                               |
Q
| Term          | Definition / Discussion                                                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Quarterly Report  | A Control Point listing of all transactions (Ceilings, Obligations, Adjustments) made against a Control Point’s Funds.                                                             |
| Quotation for Bid | Standard Form 18. Used by Purchasing Agents to obtain written bids from vendors. May be created automatically and transmitted electronically within the Purchasing Agent’s module. |
R
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Receiving Report</td>
<td>The VA document used to indicate the quantity and dollar value of the goods being received.</td>
</tr>
<tr class="even">
<td>Reconciliation</td>
<td>Comparing two records to validate IFCAP Purchase Card orders. Purchase Card Users compare IFCAP generated purchase card order data with the CC transaction sent from the CCS system in Austin.</td>
</tr>
<tr class="odd">
<td>Reference Number</td>
<td>Also known as the Transaction Number. The computer-generated number that identifies a request. It is comprised of the: Station Number-Fiscal Year-Quarter - Control Point – 4-digit Sequence Number.</td>
</tr>
<tr class="even">
<td>Repetitive (PR Card) Number</td>
<td>See Item Master Number.</td>
</tr>
<tr class="odd">
<td><p>Repetitive Item List</p>
<p>(RIL)</p></td>
<td>A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate 2237 requests from the list. A RIL can be created by using the Auto-Generate feature within the Inventory portion of the package.</td>
</tr>
<tr class="even">
<td>Requestor</td>
<td>See Control Point Requestor.</td>
</tr>
<tr class="odd">
<td>Requisition</td>
<td>An order from a government vendor.</td>
</tr>
<tr class="even">
<td>Running Balance</td>
<td>A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.</td>
</tr>
</tbody>
</table>
S
| Term          | Definition / Discussion                                                                                                                                                                                                                                                                            |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Section Request   | A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.                                                                                                                               |
| Service Balance   | The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorizations created by the service.                                                                                        |
| SF-18             | Request for Quotation.                                                                                                                                                                                                                                                                                 |
| SF-30             | Amendment of Solicitation/Modification of Contract.                                                                                                                                                                                                                                                    |
| Short Description | A phrase which describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).                                                                                              |
| Site Parameters   | Information (such as Station Number, Cashier’s address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter file.                                                                                                                                        |
| Sort Group        | An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.                                                                                                                                                  |
| Sort Order        | The order in which the budget categories will appear on the budget distribution reports.                                                                                                                                                                                                               |
| Special Remarks   | A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.                                                                                                                          |
| Stacked Documents | The purchase orders, receiving reports, and 1358s which are sent electronically to Fiscal and stored in a file for printing later rather than being printed immediately.                                                                                                                               |
| Status of Funds   | Fiscal’s on-line status report of the monies available to a Control Point. FMS updates this information automatically.                                                                                                                                                                                 |
| Sub-control Point | A user defined assignment of all or part of a ceiling transaction to a specific category (sub-control point) within a Control Point, Transactions can then be posted against this sub-control point, and a report can be generated to track use of specified funding within the overall control point. |
| Sub-cost Center   | A subcategory of Cost Center. IFCAP will not utilize a “sub-cost center” field but will send FMS the last two digits of the cost center as the FMS “sub-cost center” field.                                                                                                                            |
T
| Term                         | Definition / Discussion                                                                                                                                                               |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tasked Job                       | A job, usually a printout, that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.                              |
| TDA                              | See “Transfer of Disbursing Authority.”                                                                                                                                                   |
| Total Authorizations             | The total amount of the authorizations created for the 1358 obligation.                                                                                                                   |
| Total Liquidations               | The total amount of the liquidations against the 1358 obligation.                                                                                                                         |
| Transaction Number               | The number of the transaction that funded a Control Point (See Budget Analyst User’s Guide). It consists of the Station Number – Fiscal Year – Quarter – Control Point – Sequence Number. |
| Transfer of Disbursing Authority | The method used to allocate funds to a VA facility.                                                                                                                                       |
| Transmission Number              | A sequential number given to a data string when it is transmitted to the Austin DPC; used for tracking message traffic.                                                                   |
| Type Code                        | A set of A&MM codes that provides information concerning the vendor’s size and type of competition sought on a purchase order.                                                            |
U
| Term               | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unit of Issue          | A description of the quantity/packaging combination in which the item is issued to the end user; it may be different from the Unit of Purchase, which is the combination used when the item is procured from the vendor. For example, a vendor may sell an item in cases of 24 cans, but the end user receives individual cans from that case.                                                                                                                                                  |
| Unit of Purchase       | A description of the quantity/packaging combination in which VA purchases the item from the vendor; it may be different from the Unit of Issue, which is the combination used to issue the item to the end user. See also Unit Conversion Factor.                                                                                                                                                                                                                                               |
| Unit Conversion Factor | A number which expresses the ratio between the unit of measure and the unit of issue. Among other things, the conversion factor (which is part of the vendor data) is used at order release to calculate the due-ins and due-outs. Supply stations receive the conversion factor at the time of order release and use it to translate the order quantities into supply station amounts. If an item is procured, stocked and issued using the same units, then the conversion factor would be 1. |
V
| Term         | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Vendor file      | An IFCAP file of vendor information solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. The debtor’s address may be drawn from this file but is maintained separately. If the desired vendor is not in the file, contact A&MM Service to have it added.                                                                  |
| Vendor ID Number | The ID number assigned to a vendor by the FMS Vendor unit.                                                                                                                                                                                                                                                                                                                                                       |
| VRQ              | FMS Vendor Request document. When a new vendor is added to IFCAP a VRQ message is sent electronically to the Austin FMS Vendor unit to determine if the vendor exists in the central vendor system. If the vendor is not in the system, Austin will confirm information and establish the vendor in the central file. If vendor exists in central file already, Austin will verify the data. *See also*VUP. |
| VUP              | Vendor Update Message. This message is sent electronically from the FMS system to ALL IFCAP sites to ensure that the local vendor file contains the same data as the central vendor file in Austin. This message will contain the FMS Vendor ID for the vendor and the Alternate Address Indicator if applicable. *See also*VRQ.                                                                            |
X
| Term | Definition / Discussion |
|----------|-----------------------------|
| X12 EDI  | *See* EDI X12.              |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<Alt\> 1-3
A&MM 1-5, 2-1, 2-2
Accounting Technician 1-1, 1-5, 1-6, 3-1, 3-5, 5-3, 6-1, 7-1, 7-3, 8-2, 8-9, 13-2
Budget Object Code (BOC) 2-2, 4-1, 4-2, 5-4, 7-2
click 1-3
Clinical Logistics Office 12-1
Clinical Logistics Office Menu 12-1
Create a Code Sheet 8-1
documents
available 1-2
Financial Services Center 5-1, 5-6
FMS 1-6, 3-3, 3-6, 4-1, 4-2, 4-3, 5-3, 5-4, 5-5, 7-2, 8-1, 8-2, 8-4, 8-9
FMS Payment Voucher Error Processing 8-11
hyperlink
internal 1-2
hyperlinks 1-2
icon
Information 1-4
Technical Note 1-4
Tip 1-4
Warnings 1-4
icons
for boxed notes 1-4
IFCAP 1-4
Invoice Processing for Payment 7-1
manual
online 12-1
Manual 1-4
Obligate 1358 4-1
Obligation Processing 3-1, 3-3, 3-5, 3-6
OLCS 5-1, 5-6
Online Certification System 5-1, 5-6
operating system 1-3
Process Receiving Report 6-1
Purchase Order 1-5, 2-1, 3-1, 3-4, 3-7
Query Tool 1-4
Segregation of Duties 5-1, 5-6
Single Receiving Report Reprint in Fiscal 13-2
Source Code 2-2
Stack Status Report 8-2
