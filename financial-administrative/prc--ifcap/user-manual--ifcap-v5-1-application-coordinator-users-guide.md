---
title: IFCAP Version 5.1 Application Coordinator User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Application Coordinator User's Guide
app_code: PRC
app_name: IFCAP
section: FIN
app_status: active
pkg_ns: PRC
patch_ver: 5.1
patch_id: PRC*5.1
group_key: "PRC:PRC:5.1"
file_numbers: 
  - 446
security_keys: []
menu_options: 1
description: You have been selected as an Integrated Funds Distribution, Control Point Activity, Accounting, and Procurement (IFCAP) Application Coordinator. The IFCAP Application Coordinator User’s Guide will provide you with guidance and training for your new responsibilities.
audience: 
keywords: 
  - class
  - ifcap
  - strong
  - table
  - point
  - control
  - report
  - span
  - your
  - fiscal
page_count: 0
word_count: 26827
section_count: 11
table_count: 18
figure_count: 39
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1application_coord.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1application_coord.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

## Table of Contents

  - [Preface](#preface)
  - [Introduction](#introduction)
    - [How to Use This Guide](#how-to-use-this-guide)
    - [FileMan Date Conventions](#fileman-date-conventions)
  - [The Role of the Application Coordinator](#the-role-of-the-application-coordinator)
    - [Application Coordinator Responsibilities](#application-coordinator-responsibilities)
    - [On- Site Resources](#on-site-resources)
    - [Troubleshooting](#troubleshooting)
    - [Additional Recommendations](#additional-recommendations)
    - [References](#references)
  - [System Security](#system-security)
    - [Security Levels](#security-levels)
    - [System Access](#system-access)
    - [Menu and Security Keys](#menu-and-security-keys)
    - [Electronic Signature Codes](#electronic-signature-codes)
  - [Operation](#operation)
    - [Using IFCAP Files](#using-ifcap-files)
    - [Setting Site Parameters](#setting-site-parameters)
    - [EDI Vendor Edit](#edi-vendor-edit)
    - [Establish Common Numbering Series](#establish-common-numbering-series)
    - [Add/Edit Supply Personnel](#addedit-supply-personnel)
    - [Barcode Manager Menu](#barcode-manager-menu)
    - [Clear FMS Exception File Entries](#clear-fms-exception-file-entries)
    - [FMS Exception Transaction Report](#fms-exception-transaction-report)
    - [Procurement of Accounting Transactions Status Report](#procurement-of-accounting-transactions-status-report)
    - [Reinstate IFCAP Terminated User](#reinstate-ifcap-terminated-user)
    - [Substation Enter/Edit](#substation-enteredit)
    - [Clinical Logistics Office Menu](#clinical-logistics-office-menu)
    - [Compliance Reports (1358)](#compliance-reports-1358)
    - [Let Staff Replace Inventory Quantities](#let-staff-replace-inventory-quantities)
    - [On-Demand Users Enter/Edit](#on-demand-users-enteredit)
    - [Posted Dietetic Cost Report](#posted-dietetic-cost-report)
    - [Unposted Dietetic Cost Report](#unposted-dietetic-cost-report)
    - [Quarter Review of Vouchers](#quarter-review-of-vouchers)
    - [Establish IFCAP](#establish-ifcap)
    - [Test Account Set Up](#test-account-set-up)
  - [The Logistics Data Query Tool](#the-logistics-data-query-tool)
  - [Resolving Error Messages](#resolving-error-messages)
  - [Error Messages](#error-messages)
  - [Glossary](#glossary)
  - [Index](#index)
Integrated Funds Distribution Control Point Activity, Accounting and Procurement  
(IFCAP)Version 5.1IFCAP Application CoordinatorUser’s Guide
![](ifcap-version-5-1-application-coordinator-user-s-guide/001.png)
Revised March 2026Department of Veterans AffairsOffice of Information and Technology (OI&T)Management, Enrollment, and Financial SystemsTHIS PAGE INTENTIONALLY LEFT BLANK
Revision History
Initiated 12/29/04
<table>
<caption><p><span id="_Ref165946271" class="anchor"></span>Table 1: Icons Used in Boxed <em><u>NOTE</u></em>s</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 48%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author(s)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>March 2026</td>
<td>22.0</td>
<td><p>Updates based on patch PRC*5.1*257.</p>
<p>This manual has been updated to comply with the VA OIT-mandated user guide template.</p></td>
<td><p>Technical Writer,</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="even">
<td>September 2025</td>
<td>21.0</td>
<td>The PRCHL GUI Logistics Data Query Tool option has been marked Out of Order with patch PRC*5.1*247</td>
<td><p>Technical Writer,</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="odd">
<td>August 2021</td>
<td>20.0</td>
<td>Charge Card System replaced Credit Card System</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>October 2019</td>
<td>19.0</td>
<td><p>Patch PRC*5.1*198 (NIF/IFCAP IMF Interface Enhancement)</p>
<p>Updated table 3.2 to include the PRCHVEN key for both the Chief of Purchasing and the Chief of Accounting</p>
<p>Updated revision dates on first page and in footer</p></td>
<td><p>PMO Program Analyst,</p>
<p>NIF/IFCAP IMF Interface Enhancements Team </p></td>
</tr>
<tr class="odd">
<td>January 2019</td>
<td>18.0</td>
<td><p>Patch PRC*5.1*198 (NIF/IFCAP IMF Interface Enhancement)</p>
<p>Updated 4.3 EDI Vendor Edit Paragraph</p>
<ul>
<li><p>Added an additional sentence: “In order to update a Medical/Surgical Prime (MSPV) Vendor (vendor numbers above 949,999), the user must hold the PRCHVEN security key.”</p></li>
</ul>
<p>Updated Table 3-2</p>
<ul>
<li><p>Added “PRCHITEM SUPER” to the Associated Security Key(s) column for Item Managers</p></li>
</ul>
<p>Updated footer with revision date</p></td>
<td><p>PMO Program Analyst,</p>
<p>NIF/IFCAP IMF Interface Enhancements Team </p></td>
</tr>
<tr class="even">
<td>August 2018</td>
<td>17.0</td>
<td><p>Patch XU*8.0*679 (Signature Block restrictions)</p>
<p>Added <em><strong><u>NOTE</u></strong></em> to page 3-8</p></td>
<td><p>Project Manager, Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>August 2017</td>
<td>16.0</td>
<td><p>Patch PRC*5.1*194</p>
<p>The PRCHLO CLO PROCUREMENT option has been marked Out of Order. See Sections 4.12 and 4.12.1.</p></td>
<td><p>SQA Manager,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>January 2014</td>
<td>15.0</td>
<td><p>Patch PRC*5.1*174 (IFCAP/eCMS Interface)</p>
<p>Updated Table 3-2 with new Security Key information for the Transaction Report – eCMS/IFCAP.</p></td>
<td><p>Project Manager, Subject Matter Expert, Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>September 2013</td>
<td>14.0</td>
<td><p>Patch PRC*5.1*171</p>
<p>Removed option Enter/Edit Control Point Users from menus. See page 2-7.</p></td>
<td><p>Project Manager, Subject Matter Expert, Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>Jan 2013</td>
<td>13.0</td>
<td><p>As of Patch PRC*5.1*162,</p>
<p>The Authorization Detail 1358 - F23 [PRCHLO 1358 AUTHORIZATION DET] option, which previously displayed the user who posted a payment or credit to the IFCAP authorization, will now display POSTMASTER as the user for credit amounts that are posted due to the new Central Fee transactions.</p></td>
<td><p>Project Manager, Subject Matter Expert, Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>September 2012</td>
<td>12.5</td>
<td><p>Patch PRC*5.1*167 (eCMS Interface to IFCAP) updates:</p>
<p>Minor changes to menu commands in Section 4.5 “Add/Edit Supply Personnel.”</p>
<p>Updated Figure 4.11 “Sample Add/Edit Supply Personnel Screen.”</p>
<p>Updated instructions in section 4.19.3 “Add/Edit Supply Personnel” (Step 1).</p>
<p>Overall editorial review.</p></td>
<td><p>Project Manager, Subject Matter Expert, Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>October 2011</td>
<td>12.0</td>
<td>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358. See pages <a href="#PRC_158_A">4-17</a>, <a href="#PRC_158_B">7-1</a>.</td>
<td><p>Project Manager,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>July 2011</td>
<td>11.0</td>
<td>New OLP Domain and Mail Group created for PRC*5.1*153 and Updated Glossary to include reference to OLCS. See pages <a href="#PRC_153A">3-3</a> and <a href="#PRC_153B">7-10</a>.</td>
<td><p>Project Manager,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>May 2011</td>
<td>10.0</td>
<td>PRC*5.1*154, enforces Segregation of Duties in the Payment/Invoice Tracking module and adds a new Invoice Certification Report for Segregation of Duties to the Compliance Reports section. See pages <a href="#PRC_154a">4-19</a>, <a href="#PRC_154b">4-25</a>, <a href="#compliance-reports-1358">4-26 to 4-29</a></td>
<td><p>Project Manager,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>April 2011</td>
<td>9.0</td>
<td><p>PRC*5.1*151, update fields in the Control Point Activity CLRS</p>
<p>Extract Validation Template, see page <a href="#PRC_154b"><u>4-25</u></a>.</p></td>
<td><p>Project Manager,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>1/5/2011</td>
<td>8.0</td>
<td>Revised documentation related to changes implemented by PRC*5.1*148</td>
<td><p>Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>8/21//2009</td>
<td>7.0</td>
<td>Added documentation related to the enhancements implemented by PRC*5.1*130</td>
<td><p>Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>3/05/2008</td>
<td>6.0</td>
<td>Added documentation regarding new menu option PRCHMP CS PURGE ALL</td>
<td><p>SQA Analyst</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>05/30/07</td>
<td>5.0</td>
<td>Added information covering the use of the Logistics Data Query Tool (LDQT), per patch PRC*5.1*103; general update.</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>03/2007</td>
<td>4.0</td>
<td>Modified existing document for inclusion of on-demand functionality Patch PRC*5.1*98. Revisions made to bring document up-to-date.</td>
<td><p>Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>02/09/06</td>
<td>3.0</td>
<td>Added new options and reports for the Clinical Logistics Report Server (CLRS)</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>06/23/05</td>
<td>2.0</td>
<td>Added essential information about DynaMed-IFCAP Interface.</td>
<td><p>Subject Matter Expert,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>4/15/2005</td>
<td>1.0</td>
<td>Initial Publication</td>
<td><p>SEPG/SQA</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>12/29/04</td>
<td>1.0</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data; PDF file checked for accessibility to readers with disabilities.</td>
<td>Department of Veterans Affairs</td>
</tr>
</tbody>
</table>
<span id="_Ref165946271" class="anchor"></span>Table 1: Icons Used in Boxed *<u>NOTE</u>*s

## Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide explains how to implement the Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) system. The IFCAP package automated certain functions in Acquisition and Materiel Management (A&MM), Fiscal Service, and in all of the services that request supplies and services on Veterans Affairs (VA) Form 90-2237. The goal of IFCAP is to integrate these three areas and allow users to share procurement information. IFCAP has the following components or “modules.”

- FUNDS DISTRIBUTION allows Fiscal Service to establish Fund Control Points, and track funding for budget purposes.
- CONTROL POINT ACTIVITY automates the preparation of requests, the electronic transmission of requests to A&MM and Fiscal services and the bookkeeping processes within a service.
- PROCUREMENT allows A&MM to transfer IFCAP-generated requests onto purchase orders and requisitions, process receiving documents in the warehouse, and create and transmit code sheets to Austin.
- ACCOUNTING automates the creation of code sheets, handles the processing of certified invoices, and facilitates the electronic transmission of code sheets and receiving documents to the Financial Management System (FMS) located in Austin, Texas. In addition, IFCAP transfers obligation information back to the Control Point and updates the Control Point balance automatically.
- INVENTORY permits services to maintain their own on-line inventory and establish an average stock level, record the distribution of goods to secondary location(s), and automatically generate IFCAP requests for replenishment purposes. Secondary locations may maintain their own inventory if they wish.
- RFQ enables the Purchasing Agent (PA) to create a Request for Quotation (RFQ), evaluate bids, award the order, and generate the purchase order. Using IFCAP and the Electronic Data Interchange (EDI) functionality that currently exists in Austin, the PA can electronically send the RFQ to one or many vendors and receive the bids electronically
- PURCHASE CARD permits users at Service level and in A&MM to generate purchase orders against assigned credit card(s). Charges are passed electronically from the Austin Charge Card System (CCS) to IFCAP and users reconcile payments with IFCAP Purchase Orders. The assigned Approving Official then approves reconciled orders. The local IFCAP Purchase Card Registration file is maintained by the station designated Purchase Card Coordinator. Reconciled orders are then approved by assigned Approving Officials. There are many reports that provide data on the status of the purchase card orders and timeliness of the reconciliation and approval processes.
- DELIVERY ORDERS permit users to generate purchase orders for contract items at the Service level. Using switches that are site configurable, orders can bypass Fiscal and be obligated at time of signing by Service-level staff.

  THIS PAGE INTENTIONALLY LEFT BLANK

Table Of Contents

Tables

Table 1: Icons Used in Boxed *<u>NOTE</u>*s [4](#_Ref165946271)

Table 2: IFCAP User’s Guides [11](#_Ref166058625)

Table 3: Other IFCAP Documentation [13](#_Ref165795405)

Table 4: Security Key / Mail Group [17](#_Ref153262070)

Table 5: Menu Option / Security Key List [18](#_Ref166053851)

Table 6: PAT Number Series [37](#_Toc222493246)

Table 7: Error Messages [71](#_Ref166307934)

Figures

Figure 1: Sample IFCAP Menu Option User’s Toolbox Screen [23](#_Ref166314802)

Figure 2: Sample IFCAP Application Coordinator Menu [25](#_Ref153779165)

Figure 3: Sample Site Parameter Setup [27](#_Ref165799796)

Figure 4: Dedicated Printer Names [29](#_Toc522522806)

Figure 5: Sample Stack Documents Screen [31](#_Ref166314861)

Figure 6: Sample Stacked Documents for Receiving Reports Not Processed in Fiscal [31](#_Toc522522808)

Figure 7: Other System Setting Setup Example [32](#_Toc522522809)

Figure 8: Sample Address Codes and Screen Settings [33](#_Toc522522810)

Figure 9: Sample EDI Vendor Option [35](#_Ref166314901)

Figure 10: Sample 1: PAT Numbering System Setup [36](#_Ref154977508)

Figure 11: Sample 2: PAT Numbering System Setup [36](#_Ref165885126)

Figure 12: Sample Add/Edit Supply Personnel Screen [38](#_Toc522522814)

Figure 13: Barcode Manager Menu [39](#_Toc522522815)

Figure 14: FMS Exception File Entries Option Example [40](#_Toc522522816)

Figure 15: Sample PAT Status Report [40](#_Toc522522817)

Figure 16: Sample Clinical Logistics Office Menu Options [43](#_Toc522522818)

Figure 17: Sample CLO GIP Reports Option Selected [45](#_Toc522522819)

Figure 18: Sample CLO Procurement Reports Option Selected [45](#_Toc522522820)

Figure 19: CLO System Parameters Option Example [46](#PRC_154a)

Figure 20: Sample Procurement Extract Task Queued [47](#_Toc522522822)

Figure 21: Sample Procurement Extract Successfully Complete [47](#_Toc522522823)

Figure 22: Sample Flat File for Transfer Build Complete [48](#_Toc522522824)

Figure 23: Sample Flat Files Sent to Invalid / Undefined Extract Directory [48](#_Toc522522825)

Figure 24: Start of FTP Transfer [48](#_Toc522522826)

Figure 25: FTP Transfer Complete [49](#_Toc522522827)

Figure 26: GIP Reports Will Not Run – Needed Lock Unavailable [51](#_Toc522522828)

Figure 27: Procurement / Transfer Process Will Not Run – Needed Lock Unavailable [51](#_Toc522522829)

Figure 28: Username is Null [51](#_Toc522522830)

Figure 29: Password is Null [52](#_Toc522522831)

Figure 30: Error Writing Entry to File \#446.7 [52](#_Toc522522832)

Figure 31: CLRS Extract [52](#_Toc222493278)

Figure 32: Separation of Duties Violations [53](#_Toc522522833)

Figure 33: Sample Invoice/Tracking Module of 1358s [54](#_Toc222493280)

Figure 34: Sample Report Showing No 1358 Compliance Violations [55](#_Toc222493281)

Figure 35: Sample On-Demand User Option [57](#_Toc522522834)

Figure 36: Sample On-Demand User Option Removal [58](#_Toc522522835)

Figure 37: Sample Posted Dietetic Cost Report [58](#_Toc522522836)

Figure 38: Sample Unposted Dietetic Cost Report [60](#_Toc522522837)

Figure 39: Sample Data for Quarterly Review of Vouchers Report [61](#_Toc522522838)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You have been selected as an Integrated Funds Distribution, Control Point Activity, Accounting, and Procurement (IFCAP) Application Coordinator. The *IFCAP Application Coordinator User’s Guide* will provide you with guidance and training for your new responsibilities.

You will be responsible for planning and implementing new work methods and technology for employees throughout your medical center. You will train employees and assist all users when they run into difficulties. You will need to know how all system components work.

This guide is designed to assist you with various responsibilities. One section of this guide provides some information that you will find useful when troubleshooting. While there is no substitute for hands-on experience with the various IFCAP system options, the information in this user guide should be helpful.

We recommend that you establish and maintain open communication with your supervisor and Service Chief, and with your counterparts in Fiscal and Acquisitions and Materiel Management (A&MM), or Information Resource Management (IRM).

As an aside, you may also find that some of your colleagues will refer to you as the “ADPAC” (*ad-pack*). This term goes back to the days when computing operations were referred to as “automated data processing,” or ADP, and people with your assignment were called “ADP Application Coordinators.”

### How to Use This Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you start learning about your job as Application Coordinator, please take a few moments to familiarize yourself with how this guide is put together.

STEP 1. Read all of 1. It explains how to interpret the graphics and typestyles used in this guide.

STEP 2. If this is your first exposure to using VistA, you should become familiar with terminology and functions that are used throughout VistA applications. There are several manuals and guides that provide a foundation for use of Kernel, FileMan, and MailMan (see Glossary). These documents replace the old DHCP User’s Guide to Computing, which is obsolete. You will find these at:

Kernel: <http://www.va.gov/vdl/application.asp?appid=10>

FileMan: <http://www.va.gov/vdl/application.asp?appid=5>

MailMan: <http://www.va.gov/vdl/application.asp?appid=15>

STEP 3. Read the remainder of this guide.

#### Hypertext and Hyperlinks

This document contains “hypertext” that provides links to other parts of this document or to other related documents. *Hypertext* is a computer-based text retrieval system that enables you to access locations in electronic documents by clicking on *hyperlinks* in those documents. If you are viewing this document on your computer screen (as opposed to reading a printed copy), you will find certain hyperlinked words or phrases.

An internal or “cross-reference” hyperlink allows you to “jump” to another part of this document. Typically, these hyperlinks will be imbedded in sentences like “See the IFCAP Glossary in 8.” If you have the Web toolbar enabled in your copy of Word, just click the back ![](ifcap-version-5-1-application-coordinator-user-s-guide/002.png) icon on the toolbar to return to where you jumped from.

- Another kind of internal hyperlink uses “bookmarks” to direct you to other locations in this document. These are normally presented in a blue font. Again, click the back ![](ifcap-version-5-1-application-coordinator-user-s-guide/003.png) icon on the toolbar to return to the point where you jumped from.

Links to web pages or Internet sites should open in your web browser (typically Internet Explorer®). Use the browser’s “back” button to return to this document. Since Internet Explorer and Word are both Microsoft products, do not close the browser window, since this may (under certain circumstances) also close this document.

- Links to some external documents (for example, other Word documents) may (depending on your system settings) open in Word. Such links are also usually presented in a blue font. For example, *<u>NOTE</u>* the shortcut graphic with blue hyperlink to the other online documents shown in the boxed *<u>NOTE</u>* below. Use the back ![](ifcap-version-5-1-application-coordinator-user-s-guide/004.png) icon to return to where you jumped from.

In either case, you may click (or, depending on your computer’s operating system or software version, you may have to hold down the \<Ctrl\> key while clicking) on the link to see the other document or move to the specified place in this document.

#### Procedure Steps 

Procedures that you perform in an exact order will list the steps involved. Look for Step numbers as in the following samples:

STEP 1. Select the FMS Exception option.

STEP 2. Enter the latest date that you want to retain entries. IFCAP will delete all entries recorded before that retention date.

There are also paragraphs that simply discuss a process. In these instances, you do not need to perform any process discussed using a particular order.

#### Typographical Conventions

This guide uses a few conventions to help identify, clarify, or emphasize information.

- Type: The word “type” is used in this guide to mean straightforward typing at your terminal keyboard.
- Keys: In this guide, computer keys that you press, but which do not result in words appearing on your screen, are represented inside \<angle brackets\> using the r_ansi font (examples: \<Ctrl\>+\<S\>, \<Enter\>).
- \<Enter\>: The term \<Enter\> is used to indicate that you must send whatever you have been typing on your keyboard to the computer. When you have completed typing your response, you send it to the computer by pressing the return or enter key once.
- Emphasis: Italic text (such as *must* or *not*) is used to emphasize or draw your attention to a situation or process to perform. Pay close attention to statements containing italic text.
- Program and Utility Names: Names of software programs and utilities appear in bold type (like FileMan).
- Menus, Options, File and Field Names: Names of menus, menu options, files, and similar items are shown in the r_ansi font (as in “Select the FMS Exception option”).
- Alert Icons: Whenever you need to be aware of something important or informative, the Guide will display a boxed *<u>NOTE</u>* with an icon to alert you; icons are shown in Table 1. Look for these icons in the left and right margins of the document.

<table>
<caption><p><span id="_Ref166058625" class="anchor"></span>Table 2: IFCAP User’s Guides</p></caption>
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
<td>![](ifcap-version-5-1-application-coordinator-user-s-guide/005.png)</td>
<td><strong>Warning</strong>: Something that could adversely affect your use of the Query Tool or of the material available in the IFCAP databases.</td>
</tr>
<tr class="even">
<td>![](ifcap-version-5-1-application-coordinator-user-s-guide/006.png)</td>
<td><em><strong><u>TIP</u></strong></em>: Advice on how to more easily navigate or use the Guide or the software.</td>
</tr>
<tr class="odd">
<td>![](ifcap-version-5-1-application-coordinator-user-s-guide/007.png)</td>
<td><strong>Information</strong>: or <strong><em><u>NOTE</u></em>:</strong> Additional information that might be helpful to you or something you need to know about, but which is not critical to understanding or use of the software.</td>
</tr>
<tr class="even">
<td>![](ifcap-version-5-1-application-coordinator-user-s-guide/008.png)</td>
<td><strong>Technical <em><u>NOTE</u></em>:</strong> Information primarily of interest to software developers, IRM or Enterprise VistA Support (EVS) personnel. Most users can usually safely ignore such <em><strong><u>NOTE</u></strong></em>s.</td>
</tr>
<tr class="odd">
<td><p>![](ifcap-version-5-1-application-coordinator-user-s-guide/009.png)</p>
<p>![](ifcap-version-5-1-application-coordinator-user-s-guide/010.png)</p></td>
<td><strong>Question:</strong> A question that might come to your mind (hopefully, followed by an <strong>Answer</strong>!)</td>
</tr>
</tbody>
</table>

<span id="_Ref166058625" class="anchor"></span>Table 2: IFCAP User’s Guides

### FileMan Date Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout the guide, FileMan date conventions have been used. A date-valued response can be entered into MailMan in a variety of ways. The following is a typical help prompt for a date field:

Examples of Valid Dates:

JAN 20, 1957, or 20 JAN 57, or 1/20/57, or 012057.

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses CURRENT YEAR. Two-digit year

assumes no more than 20 years in the future, or 80 years in the past.

*<u>NOTE:</u>* If you do not specify the year when you enter a date, IFCAP will assume that you are referring to the current calendar year. This could cause some confusion around the fiscal year turnover period when you are more likely to be entering dates for next year (when the current Fiscal Year is the same as the next Calendar Year).

## The Role of the Application Coordinator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Application Coordinator Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As an Application Coordinator, you will need to know how IFCAP performs tasks, and how the principal elements of IFCAP work with each other. This knowledge will allow you to coordinate the implementation of IFCAP, train new users, inform management of your needs, and solve problems with the system. This chapter discusses those issues for which you will be responsible.

Just what does it mean to be an Application Coordinator? For one thing, it means that your responsibilities extend far beyond the normal boundaries. You’re no long “just” a Purchasing Agent or Accounting Technician. You will be interacting with all areas of A&MM, OA&L, Fiscal, and with the rest of your facility when supporting the Control Point Activities. You will be acting as liaison with VA management by both eliciting their support and providing the support (information) that IFCAP can provide.

You are no longer just a “subject-matter expert” in A&MM, OA&L, or Fiscal. In the eyes of the users, you will be considered a computer expert. You will be their first contact when something does not work. Your knowledge of IFCAP, as well as computers in general, is gained by using the system.

Ask for help from your Site Manager in learning about the equipment being used and then teach your users about the equipment as well.

#### Marketing and Demonstrating IFCAP

IFCAP influences your entire facility. IFCAP is not just a Fiscal and OA&L concern. IFCAP affects how every Control Point processes requests.

It is important for you to create a “positive image” of IFCAP when presenting it to new users. If you are enthusiastic about IFCAP, then the users will be enthusiastic.

You may wish to develop an IFCAP demonstration that you can present to groups of Service Chiefs, Supervisors, and users. This will be different from the individual training of users. Show the path of a request from the Control Point to OA&L Service, then to Fiscal for obligation, the Warehouse for Receiving, and back to Fiscal for processing payment to the Vendor. Users need to know how they fit into the IFCAP picture. You will find your job will be much easier if users understand *why* they must do it the IFCAP way. Don’t forget to include Fiscal and OA&L employees in this demonstration. It is critical that they understand how important *all* areas of IFCAP are to *their* job.

#### Software

Users may require experience with the system to understand what a job task or new functionality requires. Consequently, hands-on training should take place in the Test Account that has been set up by the Site Manager. In the Test Account, a user can go through all job-related menus and options and begin to feel comfortable using the system. Before training begins, users should read the appropriate job task manual or guide. See paragraph 2.5.

*<u>TIP:</u>* Consider depicting the path of a request from the control point to OA&L Service, then to Fiscal for obligation, and finally Warehouse for Receiving, and back to Fiscal for processing payment to the vendor. Users need to know how they fit into the IFCAP picture.

One-on-one training should occur when there won’t be significant interruption. Try to schedule any one-on-one sessions when the user has a good amount of free time. This will help ensure that training is more productive.

When training more than one user, try to keep the size of the training group to three or four. This small size will allow everyone to view a single terminal with ease and allow each user to perform one or more job tasks.

As training progresses, ensure that each user gets hands-on experience. The more experience the users gain in a training environment, the more confident each will be when on the job. Mistakes are also a part of learning; so, when necessary, demonstrate corrective techniques to ensure each user understands that most errors are recoverable.

*<u>NOTE:</u>* Training users in Control Points is a joint responsibility shared by OA&L and Fiscal staff. For instance, when A&MM instructs the Control Point Official/Clerk in entering a request (2237, Repetitive Item List) on IFCAP; instructions should also be given on tracking the status of the request or displaying a copy of the Request or Purchase Order, while Fiscal Service demonstrates the Funds Control portion of IFCAP.

#### Hardware

Some users may also require training in the operation of some of the hardware near their workstations or buildings. Equipment such as printers requires everyday replenishment of ink and paper. Consequently, users will need to know how to load paper correctly, form feed, line feed, and reset the printers and change ink cartridges or ribbons.

*<u>TIP</u>*: Write down the device number and default settings, when applicable.

#### User Support

Consider establishing an IFCAP support group for Control Points. The group might include Control Point Officials and Clerks from OA&L and Fiscal Coordinators – new and current users of IFCAP. Perhaps the group would meet once a month to discuss issues, problems, and solutions they’ve encountered daily or users may attend when they need some additional support. In either case, this might prove to be a great forum to address questions and introduce upcoming enhancements.

Another way to provide support to users of the Control Point module is to have experienced Control Point Clerks and Officials be a mentor to a new IFCAP user. The new user would call the experienced Clerk to ask questions. Together, they would find solutions and solve problems. When an answer to a question or resolution to a problem proves ineffective, you, as the Application Coordinator, would be their next resource.

You too may wish to become a part of a network of other IFCAP Application Coordinators. You will find the problems you encounter are universal and the other coordinators may have a solution.

#### Training

Training of users may be one of your duties as an Application Coordinator. You may have the responsibility of training new users or acclimating current users on new functionality. In either instance, your experience as a user and an Application Coordinator will help you relate new information to users in a familiar and easy manner and atmosphere.

Some current users may not be receptive to change. It is important that you listen to concerns and try to alleviate them. Spend time with users and demonstrate VistA functionality.

*<u>TIP</u>:* Some users may need to see, rather than read about, processes and get hands-on experience.

### On- Site Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are individuals at your site who can assist you with problems and information. The Site Manager will provide you with a Test Account that you may use to familiarize yourself with the IFCAP package. It is a good idea for you to engage your Fiscal or OA&L counterparts as you refresh yourself with the various functions of the system.

You should meet with the Site Manager regularly. The Site Manager will work with you to assist you in learning about the various workstation setups and printers in your area.

During your first meeting with the Site Manager, you will need to discuss who will be responsible for entering information into shared Veterans Health Information Systems and Technology Architecture (VistA) files. This includes adding new users and their assigned menus into the New Person (#200) file and requesting services into the Service/Section (#49) file.

Some Site Managers may have IRM staff enter this information from a list provided by the Application Coordinator, while other Site Managers may delegate the responsibility to you. If you are responsible for entering this information, you will be shown how.

In either case, compile a list of the individuals using IFCAP along with their primary menu name and authorized security key(s). In addition, list all Requesting Services that must be entered into the Service/Section (#49) file.

Work closely with the Site Manager, Fiscal, and OA&L staff to decide where the IFCAP equipment should be installed. Some locations may require that Engineering Service install conduits to hold the computer cables. Decisions must be made concerning which Control Points using IFCAP need individual workstations and which Control Points can share equipment. Perhaps a centrally located Terminal Room is available for use by smaller Control Point users.

Consult your Site Manager with questions you may have about equipment. Also, talk with the Information Resource Management (IRM) staff for your site. These two sources may prove invaluable to you as you gain experience in your position.

Your Site Manager will provide you with the device names or numbers of the printers dedicated to automatically print 2237s in OA&L, Unobligated purchase orders in Fiscal, Obligated purchase orders in OA&L, and receiving reports in the Warehouse. This information is used when establishing your Admin Activity Site Parameter (#411) file.

You will also need to discuss access to IFCAP files using *VA FileManager* (frequently referred to simply as “*FileMan*”). You will probably be called upon to generate specialized reports for management. To do this, you will need to have “read” access to IFCAP files.

### Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As the Application Coordinator, users may call you when there are problems with hardware or software. It may be as simple as a computer monitor being unplugged, or as serious as an error in the program. You will need to identify the nature of the problem and then work to resolve the issue.

You can usually identify software problems by identifying error codes. Impress upon your users that they should *always* immediately write down the following information concerning the error:

- Error message(s)
- Option selected
- Did they enter any unusual information?

When a circumstance occurs with a user consistently receiving error messages, sit with that user and observe the user’s responses to prompts. Sometimes, the user does not enter responses correctly. Of course, if the error continues to occur, contact the Site Manager.

Software problems sometimes occur when new software is loaded or a system is patched. You will be informed when new software is installed to anticipate possible functionality changes. You may find that reported problems are due to the user not fully understanding of the functionality introduced by the patch or installation. You may also find some users are not receptive to change.

Hardware problem diagnosis may prove to be a little more challenging. It would probably be to your advantage to start with the simplest and most obvious possible issue and progress to the least obvious (which may require contacting the Site Manager, IRM, or technician).

Some of the most obvious problems might be:

- Power is not on – Check the on/off switch and ensure that it is in the on position.
- Check the plug to ensure that the equipment is properly connected in the outlet.
- Check the connection of the power cord to the equipment. Wiggle the cable to the computer, it may be loose.
- If none of these suggestions resolve the situation and you have tried other approaches, call in reinforcements. The Site Manager and IRM are there to assist whenever possible.

The items listed above are suggestions on how you might resolve an equipment problem. However, there are standard troubleshooting techniques that technicians use which might be documented at your site. Check with your Site Manager and IRM staff for information.

*<u>TIP:</u>* Teach your users to check the \<No Scroll\> or \<Hold\> key (that’s the \<F1\> key if a personal computer emulator is being used) first when the keyboard seems “locked” or “frozen.” Then, check the cables to make sure they are securely attached.

### Additional Recommendations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Read this guide. It is important that you know as much about IFCAP and your responsibilities as possible. Also, read the IFCAP *Technical Manual* (*see* 2.5 below). This will give you a perspective on the various tasks and responsibilities of the system’s users.

- Meeting with your Site Manager. Collaboration is the key.
- Identifying and meeting with key people in Fiscal and OA&L services. It is critical that you have the support of all the Fiscal and OA&L supervisors.

Train new users. Remember, you’re teaching new users the way to do their jobs.

- Plan for disasters. You can often mitigate disasters with good planning.

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The IFCAP Monograph

To get an overview of what IFCAP is all about, you might want to look at the [IFCAP Monograph](http://www.va.gov/vdl/monograph/vista_monograph2005-06.htm). It’s available via a separate link near the top of the VDL page (just above the table which lists the other documents) or via this link:
> <https://www.va.gov/vdl/application.asp?appid=239>

#### The IFCAP User’s Guide Series

The series of IFCAP User’s Guides was designed to follow the functions which IFCAP provides and the “roles” which users play at various times within IFCAP. Consequently, these guides are known as “role-based” guides. The person performing a given role may or may not actually hold the position title indicated in the guide—but within IFCAP, that person carries out the duties associated with the role that is being performed.
Table 2 lists the documentation you may need when performing Application Coordinator functions. The listed documents are available online at the VistA Document Library (VDL):
> <https://www.va.gov/vdl/application.asp?appid=42>
<table>
<caption><p><span id="_Ref165795405" class="anchor"></span>Table 3: Other IFCAP Documentation</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th>Guide Name</th>
<th>Description and Use</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Accounting Technician User’s Guide</td>
<td>Provides the information needed to process an obligation, receiving report or amendment using IFCAP. In addition, it shows how to create or edit FMS documents that will be transmitted to FMS. All Accounting Technicians at your facility should be given a copy of the Accounting Technician Manual.</td>
</tr>
<tr class="even">
<td>Application Coordinator User’s Guide</td>
<td>Provides guidance to Application Coordinators when implementing IFCAP at a facility. This guide also contains information on options permitting Application Coordinators to enter the station address, common PAT numbering series, and the proper printer locations used by all IFCAP users.</td>
</tr>
<tr class="odd">
<td>Budget Analyst User’s Guide</td>
<td>This guide is used by the Budget Analyst, generally a person in Fiscal Service. It describes how to enter Ceiling Transactions that fund all Control Points. The Fiscal employee responsible for processing Transfers of Disbursing Authority (TDAs) and assigning ceilings to Control Points should be given a copy of the Budget Analyst User’s Guide.</td>
</tr>
<tr class="even">
<td>Control Point Clerk User’s Guide</td>
<td>This guide is used by those individuals who are responsible for creating requests (2237s, 1358s, etc.) that will be approved by their Control Point Official. The Control Point Clerks at your facility should be given a copy of the Control Point Clerk User’s Guide and the Control Point Requestor User’s Guide.</td>
</tr>
<tr class="odd">
<td>Control Point Official User’s Guide</td>
<td>This guide should be given to those individuals responsible for the management of Fund Control Point money. These users have been designated as the authority to approve requests for goods and services. There may be more than one Control Point Official for a Funds Control Point. This guide briefly covers those options used exclusively by the Control Point Official including Approve Requests. In most cases, the Control Point Official is only concerned with approving requests. The other options that make up the Control Point Official’s menu are discussed in the Control Point Clerk’s guide. The Control Point Officials at your facility should be given a copy of the Control Point Official User’s Guide, the Control Point Clerk User’s Guide, and the Control Point Requestor User’s Guide.</td>
</tr>
<tr class="even">
<td>Control Point Requestor User’s Guide</td>
<td>This guide is used by those individuals that create temporary requests (2237s, 1358s, etc.) but do not have access to the Control Point balance. The Requestors at your facility should be given a copy of the Control Point Requestor User’s Guide.</td>
</tr>
<tr class="odd">
<td>Delivery Order User’s Guide</td>
<td>This guide contains the functionality to permit Service level staff to generate orders for contracted items and depending on switch settings at the site to obligate them without passing them through Fiscal service. A copy of this guide should be provided to those staff members who are going to place orders for contract items.</td>
</tr>
<tr class="even">
<td>Generic Inventory User’s Guide</td>
<td><p>This guide describes the full functionality of the IFCAP Inventory system, which includes a warehouse; primary inventories that may or may not maintain a perpetual inventory; and secondary inventories (created by a primary), also maintaining perpetual inventory. The options also are included to control a dependent inventory point from the warehouse (Issue Book Processing option) or from the primary inventory (Stock Item Distribution Menu). While the warehouse, primary and secondary inventory are separate parts of the inventory system, the menu options for controlling stock in all three are identical in most respects. The differences lie in the stock request, stock distribution, and management functions.</p>
<p>See also the Point of Use Manual (https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1pou_manual.pdf)</p></td>
</tr>
<tr class="odd">
<td>PPM Accountable Officer User’s Guide</td>
<td>This guide describes the options that may be used by the Accountable Officer, Requisition Clerk, Warehouse staff and other PPM employees.</td>
</tr>
<tr class="even">
<td>Purchase Card User’s Guide</td>
<td>This guide contains full functionality to enable the site Card Coordinator to maintain the Registration file for Purchase Cards. It also contains the functionality for Service level and A&amp;MM staff to create purchase card orders which will be charged against assigned credit cards and reconciled against the charges received from the Austin Charge Card System (CCS). It also contains functionality for designated Approving Officials to approve a reconciliation done by a cardholder. All staff placing orders using government credit cards and their designated approving officials should be given a copy of this guide. A copy of the Coordinator’s part of the guide should be given to the person designated as the site Purchase Card Coordinator.</td>
</tr>
<tr class="odd">
<td>Purchasing Agent User’s Guide</td>
<td>This guide describes the options used to create, edit and display a Purchase Order, a Vendor, or an Item purchased on a repetitive basis. It contains the options that enable the Purchasing Agent (PA) to generate and process Requests for Quotation. In addition, the guide provides information concerning the printing of various management reports. The PAs at your facility should be given a copy of the Purchasing Agent User’s Guide.</td>
</tr>
<tr class="even">
<td>Requirements Analyst User’s Guide</td>
<td>This guide provides guidance for options used by the Requirements Analyst under the Personal Property Management (PPM) section of the Acquisition and Materiel Management (A&amp;MM). Service. These options are used to process requests and requisitions for Supply Fund and to create code sheets.</td>
</tr>
<tr class="odd">
<td>Requisition Clerk User’s Guide</td>
<td>This guide provides guidance for options used by Personal Property Management (PPM) personnel who process requisitions and Integrated Supply Management System (ISMS)/General Services Administration (GSA)/Defense Logistics Agency (DLA) code sheets.</td>
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
<span id="_Ref165795405" class="anchor"></span>Table 3: Other IFCAP Documentation

#### Other Documentation

Other documentation is available but will probably not be a part of your daily life as an Application Coordinator. These documents are listed in Table 3.
<table>
<caption><p><span id="_Ref153262070" class="anchor"></span>Table 4<span id="PRC_153A" class="anchor"></span>: Security Key / Mail Group</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th>Manual or Guide Name</th>
<th>Description and Use</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>Point of Use Manual</em></td>
<td><p>This guide describes the set up and functionality related to interfacing the inventory in a Secondary Inventory Point such as on a ward with an automated supply station.</p>
<p>It supplements—but does not replace— the <em>Generic Inventory User’s Guide</em>. It’s useful to programmers, site managers, and IRM technical staff setting up or maintaining the point of use interface. It is also useful to all Acquisition &amp; Materiel Management (A&amp;MM) personnel utilizing GIP.</p></td>
</tr>
<tr class="even">
<td><em>Logistics Data Query Tool User Manual</em></td>
<td>Provides information about the <em>Logistics Data Query Tool</em>. This manual is for users specifically designated to use this program.</td>
</tr>
<tr class="odd">
<td><em>DynaMed-IFCAP Implementation Guide</em></td>
<td>Describes the interface between <em>DynaMed</em>® (a commercial, off-the-shelf software package) and IFCAP. As of mid-2007, at Bay Pines VAMC <em>only,</em> <em>DynaMed</em> is used to control inventory.</td>
</tr>
<tr class="even">
<td><em>Package Security Guide</em></td>
<td>Specifies parameters controlling the release of sensitive information related to IFCAP.</td>
</tr>
<tr class="odd">
<td><em>Release Notes and Installation Guide</em></td>
<td>Provides information on how to install the latest version of IFACP at a physical site.</td>
</tr>
<tr class="even">
<td><em>Technical Manual</em></td>
<td>Provides technical information about the IFCAP package, including information to assist programmers, site managers, and Information Resources Management (IRM) technical personnel to operate, maintain, and troubleshoot IFCAP software.</td>
</tr>
<tr class="odd">
<td><em>DHCP User’s Guide to Computing</em> (obsolete)</td>
<td><p>There are several manuals and guides that provide a foundation for use of <em>Kernel</em>, <em>FileMan</em>, and <em>MailMan</em> (<em>see</em> Glossary). These documents replace the old <em>DHCP User’s Guide to Computing</em>, which is obsolete. You will find these at:</p>
<p><em>Kernel:</em> <a href="http://www.va.gov/vdl/application.asp?appid=10">http://www.va.gov/vdl/application.asp?appid=10</a></p>
<p><em>FileMan:</em> <a href="http://www.va.gov/vdl/application.asp?appid=5">http://www.va.gov/vdl/application.asp?appid=5</a></p>
<p><em>MailMan:</em> <a href="http://www.va.gov/vdl/application.asp?appid=15">http://www.va.gov/vdl/application.asp?appid=15</a></p></td>
</tr>
</tbody>
</table>
<span id="_Ref153262070" class="anchor"></span>Table 4<span id="PRC_153A" class="anchor"></span>: Security Key / Mail Group

## System Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Security Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP operates with three distinct levels of security:

- System Access
- Menu and Security Keys
- Electronic Signature Codes

This chapter of the guide discusses these three levels.

IFCAP has levels of security for all users. For instance, many of the areas require that a user gain access via a security key (assigned by an Application Coordinator, Site Manager, or IRM, depending on protocol).

As an Application Coordinator, you have access to areas in IFCAP that are restricted to certain personnel. You also have access to information that requires security measures and security checks. Your electronic signature code is one of the measures used to authenticate approval.

### System Access 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The same system of access currently in operation for all VistA applications at your medical center applies to IFCAP. The Site Manager or Application Coordinator must assign an access code to a user. Additionally, a verify code must be assigned or entered by the user. The access and verify code pair afford access to the VistA system. If the user fails to enter the proper set of codes in two or three attempts (the number of attempts is determined by the site), the terminal will lock and further efforts will not be allowed.

As a security measure, the system periodically requires verify codes to be changed as defined by system site parameters. The verify code may also be changed at any time by the user, (i.e., when an access or verify code may have been compromised).

Since access and verify codes cannot be viewed on the screen and are encrypted, these codes are safeguarded against exposure and possible use by unauthorized personnel.

### Menu and Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After a user enters the proper access and verify codes, IFCAP will display a menu. The menu presents *only* those options that a user has been assigned (security keys are the method by which a user may access certain options). Most users may never view many menu options. You will be given directions as to which user is assigned which option.

#### Menus

IFCAP uses standard menus to organize the various IFCAP options around the activities of specific job-related positions. For instance, only Control Point Officials will have the Approve Requests option on their standard job-related menu if they have been given the PRCSCPO security key.

The Site Manager has the authority to alter these standard menus, or this authority may be delegated to an Application Coordinator. Even if you do not have the authority to alter and assign menus, you will probably serve as the liaison between IFCAP users and the Site Manager recommending at times that the specialized menus be designed and assigned to users. Table 5 includes a standard listing for typical users.

Specialized menus are created using the Menu Manager. Use of this menu is not discussed in this guide. If authority for assigning additional menu options has been delegated to you, your Site Manager will instruct you in how to create new menus.

A single user should not have all IFCAP menus. It is inappropriate, for example, that a Control Point Official should have the Funds Distribution option that enters Ceiling Transactions. Restricting access to menus applies to Application Coordinators as well as management[^1]. No user can assign themselves additional menu options. Only the menu options required to accomplish their duties will be assigned.

*<u>TIP:</u>* Use the IFCAP standardized menus for an initial period for users to become familiar with available options. Evaluate the need for customized menus later.

#### Security Keys

Some IFCAP menus and options are restricted through the implementation of a “lock”. Only those users who hold the appropriate security key for the locked option (such as supervisors and their designated personnel) are granted access to that option. Users that do *not* hold the appropriate key will not see the option on their menus. In addition, the system verifies that the user holds the proper security key before permitting the user access to a restricted option. You should carefully examine the use of each security key and identify those users who should be holders of each security key.

#### Security Keys/Mail Groups

Security keys can be associated with mail groups, menu options and users.

IFCAP transmits data to the Austin Automation Center (AAC). Transmitting data to AAC may require (for each type of document), several domains, security keys, and mail groups.

The mail group members will be the recipients of MSC Confirmation Messages coming from the AAC verifying the receipt of transmissions from your facility. Please have your Site Manager or IRM add the identified IFCAP users as members to the mail groups listed in Table 4 and ensure that each is assigned the appropriate security key(s).

<table style="width:100%;">
<caption><p><span id="_Ref166053851" class="anchor"></span>Table 5: Menu Option / Security Key List</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 21%" />
<col style="width: 30%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Domain Name</strong></th>
<th><strong>Purpose</strong></th>
<th><strong>Security Key</strong></th>
<th><strong>Mail group</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>REDACTED (<em><strong>not in use)</strong></em></td>
<td>CALM</td>
<td>N/A</td>
<td>CLM</td>
</tr>
<tr class="even">
<td>REDACTED</td>
<td>Code Sheets</td>
<td>N/A</td>
<td>CLI</td>
</tr>
<tr class="odd">
<td>REDACTED</td>
<td><p>Receiving</p>
<p>Reports</p></td>
<td>PRCFA TRANSMIT</td>
<td>CLM</td>
</tr>
<tr class="even">
<td>REDACTED</td>
<td>DLA</td>
<td>PRCHPM CS TRANSMIT</td>
<td>DLA</td>
</tr>
<tr class="odd">
<td>REDACTED</td>
<td>Sends EDI orders to AAC</td>
<td>XMQ-EDP</td>
<td>EDP</td>
</tr>
<tr class="even">
<td>REDACTED</td>
<td>ISMS</td>
<td>N/A</td>
<td>ISM</td>
</tr>
<tr class="odd">
<td>REDACTED</td>
<td>Log</td>
<td>PRCHPM CS TRANSMIT</td>
<td>LOG</td>
</tr>
<tr class="even">
<td>REDACTED</td>
<td>Vendor</td>
<td>PRCFA TRANSMIT</td>
<td>MDY</td>
</tr>
<tr class="odd">
<td>REDACTED</td>
<td>ISMS</td>
<td>N/A</td>
<td>OGR</td>
</tr>
<tr class="even">
<td>REDACTED</td>
<td>Send 1358 User data to OLCS</td>
<td>N/A</td>
<td>OLP</td>
</tr>
<tr class="odd">
<td>REDACTED</td>
<td></td>
<td>N/A</td>
<td>PRC</td>
</tr>
</tbody>
</table>

<span id="_Ref166053851" class="anchor"></span>Table 5: Menu Option / Security Key List

A list of the standardized menu options and their associated security keys is in Table 5.

Names of individuals working with IFCAP must appear in the New Person (#200) file. The Site Manager usually performs this task, or it may be assigned to you, the Application Coordinator.

In either case, a list of IFCAP users should be compiled to include the menu(s) assigned (*e.g.*, PRCSCP OFFICIAL for Control Point Officials).

<table>
<caption><p><span id="_Toc222493246" class="anchor"></span>Table 6: PAT Number Series</p></caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Assigned Position or IFCAP Role</strong></th>
<th><strong>External Name</strong></th>
<th><strong>Internal Name</strong></th>
<th><strong>Associated Security Key(s)</strong></th>
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
<p>PRCH TRANSACTION COMPLETE</p>
<p>PRCHVEN</p></td>
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
<p>PRCFA SUPERVISOR</p>
<p>PRCSCPO</p></td>
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
<p>PRCASVC</p>
<p>PRCHVEN</p></td>
</tr>
<tr class="odd">
<td>Accounting Technician</td>
<td>Accounting Technician Menu</td>
<td>PRCFA ACTTG TECH</td>
<td><p>PRCFA VENDOR EDIT</p>
<p>PRCHPM CS PURGE CODE SHEETS</p>
<p>PRCHPM CS PURGE ALL</p>
<p>PRCHPM CS TRANSMIT</p>
<p>PRCF CC/SA MISMATCH OVERRIDEXUP</p>
<p>PRCASVC</p></td>
</tr>
<tr class="even">
<td>Item File Managers</td>
<td>Item File Edit</td>
<td>PRCHPC ITEM EDIT</td>
<td><p>PRCHITEM MASTER</p>
<p>PRCHITEM SUPER</p></td>
</tr>
<tr class="odd">
<td>Voucher Auditor</td>
<td>Payment /Invoice Tracking Menu</td>
<td>PRCFD PAYMENTS MENU</td>
<td>PRCFA VENDOR EDIT</td>
</tr>
<tr class="even">
<td>Person in A&amp;MM responsible for Warehouse Inventory</td>
<td>Warehouse Inventory</td>
<td>PRCPW MAIN MENU</td>
<td><p>PRCPW MGRKEY</p>
<p>PRCPW ADJAPPR</p>
<p>PRCNWHSE*</p></td>
</tr>
<tr class="odd">
<td>Person in Primary Inventory Point responsible for maintaining Inventory</td>
<td>Primary – General Inventory/Distribution Menu</td>
<td>PRCP MAIN MENU</td>
<td>PRCP MGRKEY*</td>
</tr>
<tr class="even">
<td>Person on the ward/clinic responsible for maintaining Inventory</td>
<td>Secondary--General Inventory/Distribution Menu</td>
<td>PRCP2 MAIN MENU</td>
<td><p>PRCP2 MGRKEY</p>
<p>PRCPSSQOH*</p></td>
</tr>
<tr class="odd">
<td>A&amp;MM and Fiscal Application Coordinators</td>
<td>IFCAP Application Coordinator Menu</td>
<td>PRCHUSER COORDINATOR</td>
<td></td>
</tr>
<tr class="even">
<td>/Logistics Application Coordinators</td>
<td>IFCAP Application Coordinator Menu</td>
<td>PRCHUSER COORDINATOR</td>
<td><p>PRCPAQOH*</p>
<p>PRCPODI</p>
<p>PRCHPM CS PURGE CODE SHEETS</p>
<p>PRCHPM CS PURGE ALL</p>
<p>PRCHPM CS TRANSMIT</p></td>
</tr>
<tr class="odd">
<td>Application Coordinator and Inventory Point Managers</td>
<td>Barcode Manager Menu</td>
<td>PRCT MGR</td>
<td></td>
</tr>
<tr class="even">
<td>Service Personnel responsible for performing Inventory</td>
<td>Barcode User</td>
<td>PRCT BARCODE USER</td>
<td></td>
</tr>
<tr class="odd">
<td>Service Personnel responsible for performing Inventory</td>
<td>Labels</td>
<td>PRCT LABELS</td>
<td></td>
</tr>
<tr class="even">
<td>IRM Service Personnel</td>
<td>Barcode Programmer</td>
<td>PRCT PROGRAMMER</td>
<td>PRCT MGR</td>
</tr>
<tr class="odd">
<td>Station Purchase Card Coordinator</td>
<td>Purchase Card Coordinator</td>
<td>PRCH CARD COORDINATOR MENU</td>
<td></td>
</tr>
<tr class="even">
<td>Service personnel ordering using a Credit Card</td>
<td>Purchase Card Menu</td>
<td>PRCH PURCHASE CARD MENU</td>
<td></td>
</tr>
<tr class="odd">
<td>Service personnel designated as Credit Card approving officials</td>
<td>Approving Official Menu</td>
<td>PRCH APPROVE</td>
<td>PRCH AR</td>
</tr>
<tr class="even">
<td>Service Control Point personnel ordering contract items</td>
<td>Delivery Orders Menu</td>
<td>PRCH DELIVERY ORDER MENU</td>
<td></td>
</tr>
<tr class="odd">
<td>Fiscal Accounting and Budget staff authorized to run the IFCAP-eCMS messaging transaction report</td>
<td>Transaction Report – eCMS/IFCAP</td>
<td>PRCHJ TRANS REPORT3</td>
<td>PRCHJFIS</td>
</tr>
</tbody>
</table>

<span id="_Toc222493246" class="anchor"></span>Table 6: PAT Number Series

\* Manager Only

\*\* If on-site automated supply stations are interfaced to GIP.

*<u>TIP:</u>* If your site is using the file access provisions of Kernel, ensure users have access to needed files. Contact your Site Manager or IRM for assistance.

As mentioned previously, certain menus require the user to have a security key to access available options. IFCAP looks to see if the user is an A&MM employee and position held. All A&MM employees must be identified using the Add/Edit Supply Personnel option of the IFCAP Application Coordinator Menu.

### Electronic Signature Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The final level of security in IFCAP involves the use of electronic signatures. The electronic signature code is not visible to the screen and is encrypted rendering them unreadable even when viewed in the user file by those with the highest levels of access. This signature code enables the system to limit to authorized individuals only, the ability to review or electronically pass a document to the next level of processing.

Electronic signature codes are required by IFCAP at every level a signature would be required on paper. Therefore, electronic signature codes are assigned to:

- Budget Analysts for distributing funds to control points
- Control Point Officials for approving requests
- Purchasing Agents for processing purchase orders
- Accounting Technicians for obligating documents and authorizing payments
- Warehouse workers for receiving purchases
- Purchase Card holders for processing credit card orders
- Delivery Order users to process delivery orders against existing contracts

#### Changing Your Electronic Signature Code

When necessary, you may edit your electronic signature code via the menu option Electronic Signature Code Edit.

STEP 1. From any IFCAP Menu (Figure 1: Sample IFCAP Menu Option User’s Toolbox Screen), select User’s Toolbox.

STEP 2. From the User’s Toolbox menu, select Edit Electronic Signature Code.

<span id="_Ref166314802" class="anchor"></span>Figure 1: Sample IFCAP Menu Option User’s Toolbox Screen

<table>
<caption><p><span id="_Ref166307934" class="anchor"></span>Table 7: Error Messages</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select IFCAP MENU Option: User’s Toolbox</th>
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
<p>INITIAL: BJ//</p>
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

<span id="_Ref166307934" class="anchor"></span>Table 7: Error Messages

*<u>NOTE:</u>* Your electronic signature is legal authorization to release government funds.

If the SIGNATURE BLOCK PRINTED NAME and SIGNATURE BLOCK TITLE fields are disabled at your site, contact your supervisor to request entry of your name and title.

STEP 3. At the INITIAL: prompt, enter your initials.

STEP 4. At the SIGNATURE BLOCK PRINTED NAME: prompt, enter your name, as you want it printed on forms that require your signature.

STEP 5. At the SIGNATURE BLOCK TITLE: prompt, enter your job title, as you want it printed on forms that require your signature.

STEP 6. At the appropriate prompts, enter your OFFICE PHONE number, your VOICE PAGER number, and your DIGITAL PAGER number.

STEP 7. Finally, at the ENTER NEW SIGNATURE CODE: prompt, enter your signature code; re-enter the same code when prompted.

## Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section presents the Application Coordinator options in the IFCAP Application Coordinator Menu (Figure 2). Many of these options are required in setting up and maintaining the functionality of the IFCAP package at your site. Becoming familiar with the various IFCAP guides and manuals will give you a better understanding of how different settings will affect IFCAP work at your facility.

<span id="_Ref153779165" class="anchor"></span>Figure 2: Sample IFCAP Application Coordinator Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>IFCAP Application Coordinator Menu</p>
<p>Site Parameters</p>
<p>EDI Vendor Edit</p>
<p>Establish Common Number Series</p>
<p>Add/Edit Supply Personnel</p>
<p>Barcode Manager Menu ...</p>
<p>Clear FMS Exception File Entries</p>
<p>FMS Exception Transaction Report</p>
<p>PAT Status Report</p>
<p>Repost FMS Exceptions</p>
<p>Reinstate IFCAP Terminated User</p>
<p>Substation Enter/Edit</p>
<p>Clinical Logistics Office Menu ...</p>
<p>Compliance Reports (1358)</p>
<p>Let Staff Replace Inventory Quantities</p>
<p>On-Demand Users Enter/Edit</p>
<p>Posted Dietetic Cost Report</p>
<p>Unposted Dietetic Cost Report</p>
<p>Quarterly Review of Vouchers</p>
<p>Select IFCAP Application Coordinator Menu Option:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Using IFCAP Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information entered into IFCAP is stored in files. These files allow users to access and share information quickly and easily. A good example of shared data is the information in the Vendor (#440) file. A&MM is responsible for entering and maintaining vendor data. The Control Points access this information when a user enters a request or when Purchasing and Contracting users create a quotation for bid or a purchase order. Fiscal Service uses the Vendor (#440) file to enter and store billing information.

*<u>TIP:</u>* When at a menu prompt enter:

- All or part of the option name, then \<Enter\>
- ?? (to see more options at the menu prompt)
- ??? (to see brief descriptions)
- ? OPTION (to see Help text)

When the system responds with a question of offers a prompt, and you do not understand the question or are unsure of how to respond, enter one (?) or two (??) question marks. The system will give you an explanation of the information needed or allow you to choose from a list of responses.

The remainder of this chapter discusses tasks you may perform as an Application Coordinator.

### Setting Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You will use the Site Parameters option on the IFCAP Application Coordinator Menu to record the basic information used by IFCAP: station numbers, medical center receiving address, delivery hours, invoicing address, and so on. This option also allows you to designate printers for specific print jobs after completion of the work.

*<u>TIP:</u>* If not already completed, perform the next two steps after you have created site parameters.

STEP 1. Use the Add/Edit Supply Personnel option from the IFCAP Application Coordinator Menu to add to or edit the list of A&MM Personnel. See section 4.4 for more information.

STEP 2. Use the Establish Common Number Series option from the IFCAP Application Coordinator Menu. See section 4.3 for more information.

As an Application Coordinator, you must make many decisions about your system before the system operates smoothly. Information used repeatedly by IFCAP is contained in the Site Parameters (#411) file; this information will remain largely unchanged once established. This includes addresses for the medical center and where certain documents should be printed on a recurring basis.

Enter the most commonly used address first, as it will be the default value when processing the majority of Purchase Orders. IFCAP allows you to input multiple addresses for your mail invoice location. The first entry *must* be FMS-VA- (Station Number) (*e.g.*, the setting for VAMC Marion would be FMS-VA-3 (610). The second entry *must* be for FISCAL. You may enter FISCAL SERVICE, FISCAL (04), or FISCAL (RO).

After you make these entries, you may enter any additional invoice address you choose. You may enter the names of services, allowing for invoices to be sent directly to the authorized individual who can certify them.

*<u>TIP:</u>* You may want to add a Receiving Location for Imprest Funds as well.

Figure 3 depicts the screen you will encounter when setting site parameters.

<span id="_Ref165799796" class="anchor"></span>Figure 3: Sample Site Parameter Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: site Parameters</p>
<p>STATION NUMBER:688 Enter your 3 digit station number</p>
<p>STATION: 688//</p>
<p>FACILITY TYPE:</p>
<p>Select RECEIVING LOCATION: 1<sup>st</sup> entry should be the Main receiving location at your site</p>
<p>RECEIVING LOCATION:</p>
<p>STREET ADDR.1:</p>
<p>STREET ADDR.2:</p>
<p>STREET ADDR.3:</p>
<p>CITY:</p>
<p>STATE:</p>
<p>ZIP CODE:</p>
<p>DELIVERY HOURS:</p>
<p>SHIP TO SUFFIX:</p>
<p>Select RECEIVING LOCATION:</p>
<p>Select MAIL INVOICE LOCATION: 1<sup>st</sup> entry should be for FMS in Austin, Tx</p>
<p>MAIL INVOICE LOCATION:</p>
<p>MAIL INVOICE ADDRESS1:</p>
<p>MAIL INVOICE ADDRESS2:</p>
<p>MAIL INVOICE ADDRESS3:</p>
<p>MAIL INVOICE CITY:</p>
<p>MAIL INVOICE STATE:</p>
<p>MAIL INVOICE ZIP:</p>
<p>BILL TO SUFFIX:</p>
<p>Select MAIL INVOICE LOCATION: 2<sup>nd</sup> entry should be for Fiscal Service at your site</p>
<p>HOSPITAL STREET ADDR.1:</p>
<p>HOSPITAL STREET ADDR.2:</p>
<p>HOSPITAL CITY:</p>
<p>HOSPITAL STATE:</p>
<p>HOSPITAL ZIP:</p>
<p>HOSPITAL PHONE:</p>
<p>PROMPT WHEN PRINTING?: will only appear if substation functionality is in use</p>
<p>Select PRINTER LOCATION: enter a ? to see the various printer locations</p>
<p>PRINTER LOCATION:</p>
<p>DEVICE:</p>
<p>Select PRINTER LOCATION:</p>
<p>PRIMARY STATION: Only 1 station entry can be the primary</p>
<p>FMS PAYMENTS BY STATION:</p>
<p>SUPPLY RECEIVING LOCATION:</p>
<p>RECEIPT BEFORE OBLIGATION OK?:</p>
<p>PRINT REC RPT IN FISCAL:</p>
<p>RECEIVING REPORT TRANS METHOD:</p>
<p>CODE SHEET RETENTION PERIOD:</p>
<p>DATE/TIME STAMP IN FISCAL:</p>
<p>SUPPLY ENTER BOC:</p>
<p>STATUS OF FUNDS TRACKING:</p>
<p>INTERMEDIATE PRODUCT CODE?:</p>
<p>PRINT FMS VENDOR ID:</p>
<p>Select ACTIVITY ADDRESS CODE (DLA):</p>
<p>ACTIVITY ADDRESS CODE (DLA):</p>
<p>PRIMARY ADDRESS?:</p>
<p>Select ACTIVITY ADDRESS CODE</p>
<p>DISPLAY UNOBLIGATED BALANCE?:</p>
<p>CAN FISCAL ADD VENDORS?:</p>
<p>ISSUE BOOK SORT DEFAULT:</p>
<p>SCREEN FOR FISCAL USER:</p>
<p>Select AUTHORIZED FISCAL USER:</p>
<p>ISMS TRANSACTION TIMEOUT: 99999</p>
<p>ISMS/LOG SWITCH: ISMS ONLY//</p>
<p>APPLICATION COORDINATOR:</p>
<p>FMS SECURITY CODE:</p>
<p>FISCAL REVIEW OF VRQ:</p>
<p>CARRY FORWARD 4TH QTR REQUESTS:</p>
<p>FMS-ET VENDOR CODE:</p>
<p>FMS-ET ALTERNATE ADDRESS IND.:</p>
<p>RANGE OF % FOR RECONCILING AMT:</p>
<p>STATION NUMBER: 2ND STATION ENTRY - A SITE MAY SUPPORT A CEMETERY OR REGIONAL OFFICE</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Select an Issue Book Sort Default

This code is used to sort items on the Issue Request form that prints in A&MM. It is used only for services not in the Inventory/Distribution file. Code “A” is used for an alphabetical sort on the short description; code “NSN” is used for a sort on the NSN.

#### Dedicated IFCAP Printers Settings

This section allows you to define the dedicated IFCAP printers and the forms and reports they print.

The majority of forms printed by IFCAP can always print to the same printer by defining the Printer Locations in the Site Parameter (#411) file.

<span id="_Toc522522806" class="anchor"></span>Figure 4: Dedicated Printer Names

| Printer Name          | Abbrev | Forms/Reports Printed                                                             |
|---------------------------|------------|---------------------------------------------------------------------------------------|
| Fiscal (P.O., 1358)       | -F         | POs and Amendments from A&MM and General Post 2237s and 1358s from all Control Points |
| Fiscal (Rec. Reports)     | -FR        | Receiving Reports after Warehouse signs                                               |
| Receiving (Supply)        | -R         | receiving reports after Warehouse signs                                               |
| Supply (PPM)              | -S         | 2237s from Control Points                                                             |
| Supply 2138               | -S8        | free-form POs or pre-printed 2138s                                                    |
| Supply 2139               | -S9        | pre-printed 2139s                                                                     |
| Accounts Rec.             | -A         | Not used by Accounts Receivable now                                                   |
| UB-82                     | -UB        | Not used by Accounts Receivable now                                                   |
| Imprest Funds P.O.        | -IFP       | Imprest Funds POs                                                                     |
| Imprest Funds Rec. Report | -IFR       | Imprest Funds Rec. Reports (rather than on the A&MM printer)                          |
| MailMessage               | -M         | Users can generate email messages instead of printing/displaying on screen            |

*<u>NOTE:</u>* When a printer is not defined, the user will be forced to select a printer each time a form is to be printed. If A&MM wishes to use more than one printer to print receiving reports, do not enter a device name for the Receiving (Supply) printer. IFCAP will ask for a device name and the user may enter the device name of the printer.

#### Integrated Site Substation Functionality

Only integrated sites that have invoked the substation functionality in IFCAP will be prompted with the “Prompt When Printing?” prompt when using the Site Parameters Menu option.

*<u>NOTE:</u>* This method for handling printers is only used during 2237 and 1358 approval processing.

Printers are handled differently for integrated sites that have invoked the Substation functionality in IFCAP. When a Printer Location is defined for the Substation, that printer will be used. When undefined, the Printer Location defined for the Primary Station will be used. When the Substation and Primary Station are not defined, the user will be prompted for a device. Additional flexibility is available through the “Prompt When Printing?” prompt.

- If you always want IFCAP to ask users for a device name and display the printer selected from the Substation Printer Location or Primary Station Printer Location as the default device, enter a “Y” or “YES” at the prompt.
- If you always want the printer selected from the Substation Printer Location or Primary Station Printer Location used for printing in the background, answer “N” or “NO” at the prompt. IFCAP will not ask users for a device name unless the Printer Location isn’t defined for either the Substation or the Primary Station.

#### Stacked Documents Options

You can find the following options on the Accounting Technician Menu.

- OPTION: Print Stacked Fiscal Documents – allows printing of specific documents at a user specified time and printer location. The site may “stack” the Unobligated Purchase Orders, Receiving Reports Not Processed by Fiscal, and Unobligated 1358 transactions. Any combination or all three document types may be stacked. See Figure 5.

<span id="_Ref166314861" class="anchor"></span>Figure 5: Sample Stack Documents Screen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: site Parameters</p>
<p>STATION NUMBER: 688</p>
<p>STATION: 688//</p>
<p>FACILITY TYPE: VAMC// ^printer use</p>
<p>Select PRINTER LOCATION: MAILMESSAGE// F</p>
<p>PRINTER LOCATION: FISCAL (P.O.,1358)//</p>
<p>DEVICE: SS3$PRT-16/6/UP LM 12 Replace</p>
<p>STACK DOCUMENTS: YES</p>
<p>DAYS FOR DOCUMENTS RETENTION: 7//</p>
<p>PRIMARY STATION: YES// ^</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

*<u>NOTE:</u>* Use of this feature will cause the documents that are designated for stacking to be stored in a file instead of immediately printing at the printer location defined in the Site Parameter (#411) file. You may enter any number of days you choose for days of retention.

<span id="_Toc522522808" class="anchor"></span>Figure 6: Sample Stacked Documents for Receiving Reports Not Processed in Fiscal

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: site Parameters</p>
<p>STATION NUMBER: 688</p>
<p>STATION: 688//</p>
<p>FACILITY TYPE: VAMC// ^printer use</p>
<p>Select PRINTER LOCATION: FR</p>
<p>PRINTER LOCATION: FISCAL (REC.REPORTS)//</p>
<p>DEVICE: SS3$PRT-10/6/UP//</p>
<p>STACK DOCUMENTS: YES//</p>
<p>DAYS FOR DOCUMENTS RETENTION: 7//</p>
<p>Select PRINTER LOCATION:</p>
<p>PRIMARY STATION: YES// ^</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- OPTION: Delete Stacked Fiscal Documents – allows the Accounting Supervisor to enter a date range to immediately delete printed stacked documents
- OPTION: Queued Purge of Fiscal Documents – automatically purges all printed documents from the stack file. This option is queued in TaskMan as a frequency driven background job to automatically purge all printed documents from the Site Parameter (#411) file up to the number of days set to retain in the file.

#### Primary Station and Other Settings

In addition to the items already discussed, you must answer several other system questions for your facility. Since there may be facilities that will not use all components of IFCAP, you must indicate which areas of IFCAP your site will or will not employ.

<span id="_Toc522522809" class="anchor"></span>Figure 7: Other System Setting Setup Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>PRIMARY STATION: YES//</p>
<p>FMS PAYMENTS BY STATION: ALL PAYMENTS//</p>
<p>SUPPLY RECEIVING LOCATION: WAREHOUSE//</p>
<p>RECEIPT BEFORE OBLIGATION OK?: YES//</p>
<p>PRINT REC RPT IN FISCAL: ASK TO PRINT RECEIVING REPORT IN FISCAL//</p>
<p>RECEIVING REPORT TRANS METHOD: ELECTRONIC - BATCH RELEASE//</p>
<p>CODE SHEET RETENTION PERIOD: 90//</p>
<p>DATE/TIME STAMP IN FISCAL: YES//</p>
<p>SUPPLY ENTER BOC: YES//</p>
<p>STATUS OF FUNDS TRACKING: NO//</p>
<p>INTERMEDIATE PRODUCT CODE?: NO//</p>
<p>PRINT FMS VENDOR ID: YES//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

STEP 1. If the site is the location of the primary Fiscal and A&MM functions, at the PRIMARY STATION: prompt, enter “Y” or “YES”.

STEP 2. At the FMS PAYMENT BY STATION: prompt, enter “A” for all payments, “C” for Certified only, or “N” for no payments.

STEP 3. At the SUPPLY RECEIVING LOCATION: prompt, enter “W” for Warehouse, “P” for Personnel Property Management, or “N” for no automated receiving.

STEP 4. At the RECEIPT BEFORE OBLIGATION OK?: prompt, if your site does not want to permit receiving to be done before obligation enter “N” or “NO”. If you want to allow users to enter receiving reports before the Accounting Technician obligates funds for the order enter “Y” or “YES”.

STEP 5. At the PRINT REC RPT IN FISCAL: prompt, enter “Y” or “YES” if you want the Warehouse Clerks to be able to transmit receiving reports to the printer in Fiscal Service.

STEP 6 At the RECEIVING REPORT TRANS METHOD: prompt, select the method you will use to transmit receiving reports to Austin:

- 0 (zero) if you wish to continue to mail your receiving reports.
- 1 to electronically transmit each receiving report as they are created.
- 2 to have receiving reports put into a batch for transmission.

It is strongly recommended that you use the batch release method.

STEP 7. At the DATE/TIME STAMP IN FISCAL: prompt, answer “Y” or “YES” if you wish to have the date/time of printing appear on the Unobligated purchase orders that print in Fiscal.

STEP 8. At the SUPPLY ENTER BOC: prompt, answer “Y” or “YES” if you wish to require A&MM to enter a Budget Object Code (BOC) on orders before they are signed and released.

STEP 9. At the STATUS OF FUNDS TRACKING: prompt, answer “Y” or “YES” if you wish to invoke this functionality to display control point balances during fiscal obligation of a document. At the end of the fiscal year, you may opt to have this set to “NO” to avoid waiting for the system to calculate the balance. The Budget Analyst may manually enter the actual FMS 826-control point balance from the Status of Allowance Report.

STEP 10. At the INTERMEDIATE PRODUCT CODE?: prompt, answer “N” or “NO”. This field is currently not being used.

STEP 11. At the PRINT FMS VENDOR ID: prompt, answers “Y” or “YES” if you wish to have the FMS Vendor ID print on purchase orders.

*<u>NOTE:</u>* IFCAP can delete Code Sheets automatically once they reach the number of days specified in the Code Sheet Retention Period. Contact your Site Manager, who will use the Task Manager Scheduling Option to set up a weekly or monthly purge of code sheets. Your Site Manager will ask you to specify which printer you wish to use to print the listing of deleted code sheets.

#### Address Codes and Screen Settings

STEP 1. At the SELECT ACTIVITY ADDRESS CODE: prompt, enter an activity address code. The activity address code is a six-digit code assigned to DLA requisitions for the site.

STEP 2. At the DISPLAY UNOBLIGATED BALANCE? prompt, enter “Y” or “YES” to allow accounting staff to see the Unobligated Balance of Control Points when obligating documents.

<span id="_Toc522522810" class="anchor"></span>Figure 8: Sample Address Codes and Screen Settings

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select ACTIVITY ADDRESS CODE (DLA): 369453//</p>
<p>ACTIVITY ADDRESS CODE (DLA): 369453//</p>
<p>PRIMARY ADDRESS?: NO//</p>
<p>Select ACTIVITY ADDRESS CODE (DLA):</p>
<p>DISPLAY UNOBLIGATED BALANCE?: YES//</p>
<p>CAN FISCAL ADD VENDORS?: YES//</p>
<p>ISSUE BOOK SORT DEFAULT: ALPHA//</p>
<p>SCREEN FOR FISCAL USER: YES//</p>
<p>Select AUTHORIZED FISCAL USER:</p>
<p>ISMS TRANSACTION TIMEOUT: 86400//</p>
<p>ISMS/LOG SWITCH: LOG ONLY//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

STEP 1. Enter vendors in the vendor file when processing invoices.

STEP 2. At the ISSUE BOOK SORT DEFAULT: prompt, enter “A” for alphanumeric or “N” for National Stock Number. This sets the order IFCAP will use to print issue book request forms in OA&L Service.

STEP 3. At the SCREEN FOR FISCAL USER: prompt, answer “Y” or “YES” if you wish to restrict the obligation of documents for specific stations to certain Fiscal staff. The system will then ask you to enter the name of the staff member(s) authorized to process documents for this station.

Set this prompt to “N” or “NO” if:

- You only have one station entry in the Site Parameter (#411) file.
- You want all your Fiscal staff authorized to obligate documents for all the stations on your system.

*<u>TIP:</u>* When you answer “Y” or “YES” for one station, you must define the authorized users for all the stations on your system.

STEP 4. At the ISMS TRANSACTION TIMEOUT: prompt, specify (in seconds) how long the system should wait before purging incoming transaction messages from ISMS and notifying ISMS to retransmit the messages. One day (86400) is recommended.

STEP 5. At the ISMS/LOG SWITCH: prompt, enter “LOG”. You will receive notification if you can set this prompt to another setting.

### EDI Vendor Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to update the EDI VENDOR (#.2) and the VENDOR ID NUMBER (#.4) fields in the Vendor (#440) file. See Figure 9. In order to update a Med/Surg Prime (MSPV) Vendor (vendor numbers above 949,999), the user must hold the PRCHVEN security key.

STEP 1. At the Select IFCAP Application Coordinator Menu Option: prompt, enter “EDI Vendor Edit”.

STEP 2. At the Select VENDOR NAME: prompt, enter the Vendor name.

STEP 3. At the EDI VENDOR?: prompt, enter “Y” or “YES” if the vendor can accept purchase orders electronically using EDI X12. The AAC maintains a listing of vendors who can accept orders using EDI functionality.

STEP 4. At the VENDOR ID NUMBER: prompt, enter the vendor ID number.

<span id="_Ref166314901" class="anchor"></span>Figure 9: Sample EDI Vendor Option

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: EDI Vendor Edit</p>
<p>Select VENDOR NAME: IFVENDOR,ONE MEDICAL PRODUCTS BARTON IFVENDOR,ONE PRODUCTS</p>
<p>PH:800 555-5555 NO: 55555</p>
<p>ORD ADD:P O BOX 421 FMS: IFVENDOR,ONE PERRYSBURG, OH 43551 CODE:00000000 FAX:</p>
<p>...OK? Yes// (Yes)</p>
<p>EDI VENDOR?: Y YES</p>
<p>VENDOR ID NUMBER: ?</p>
<p>Enter the vendor's EDI identification number. It should be 5-12 upper</p>
<p>case alpha/numeric characters.</p>
<p>VENDOR ID NUMBER: THIS IS PROVIDED BY THE EDI OFFICE IN AUSTIN</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Establish Common Numbering Series 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to establish the method for automatic numbering of purchase orders, requisitions, purchase card orders, delivery orders and 1358 obligations. You must specify the Using Section from A&MM or Fiscal Services that is responsible for assigning each Procurement Accounting Transaction (PAT) number series, as well as the fiscal year for which it is to be used. This specification will enable IFCAP to automatically generate PAT numbers for users in those sections. This prevents Purchasing Agents from selecting the common numbering series that was set aside for Accounting Technicians to use and vice versa.

When entering a new purchase order, the Purchasing Agent enters the first two or three digits of the common numbering series assigned to Purchasing Agents. IFCAP provides the next number in the series. Use the same procedure when selecting a PAT number for a Requisition or 1358.

*<u>TIP:</u>* You may use this option to tell IFCAP to assign numbers sequentially.

<span id="_Ref154977508" class="anchor"></span>Figure 10: Sample 1: PAT Numbering System Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: establish Common Number Series</p>
<p>Select PAT NUMBER COMMON NUMBERING SERIES: 610-A9</p>
<p>Are you adding ‘610-A9’ as a new PAT NUMBER (the 286TH)? No// Y (Yes)</p>
<p>COMMON NUMBERING SERIES: 610-A9//</p>
<p>LOWER BOUND: 1</p>
<p>UPPER BOUND: 9999</p>
<p>NEXT NUMBER: 1</p>
<p>USING SECTION: ??</p>
<p>1 PERSONAL PROPERTY</p>
<p>2 PURCHASING &amp; CONTRACTING</p>
<p>3 IMPREST FUNDS CLERK</p>
<p>4 ACCOUNTING TECHNICIAN</p>
<p>5 ACCOUNTS RECEIVABLE</p>
<p>PC AUTHORIZED BUYER</p>
<p>7 DO AUTHORIZED BUYER</p>
<p>USING SECTION: PUR PURCHASING &amp; CONTRACTING//</p>
<p>FISCAL YEAR: 09</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref165885126" class="anchor"></span>Figure 11: Sample 2: PAT Numbering System Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: ESTablish Common Number Series</p>
<p>Select PAT NUMBER COMMON NUMBERING SERIES: 662-U0 DO AUTHORIZED BUYER</p>
<p>COMMON NUMBERING SERIES: 662-U0</p>
<p>Are you adding ‘662-AU0’ as a new PAT NUMBER (the 286TH)? No// Y (Yes)</p>
<p>This is the using Section.</p>
<p>Choose from:</p>
<p>1 PERSONAL PROPERTY</p>
<p>2 PURCHASING &amp; CONTRACTING</p>
<p>3 IMPREST FUNDS CLERK</p>
<p>4 ACCOUNTING TECHNICIAN</p>
<p>5 ACCOUNTS RECEIVABLE</p>
<p>6 PC AUTHORIZED BUYER</p>
<p>7 DO AUTHORIZED BUYER</p>
<p>USING SECTION: DO AUTHORIZED BUYER//</p>
<p>FISCAL YEAR: 00//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

*<u>TIP:</u>* You may use this option to tell IFCAP to assign numbers sequentially.

To set up PAT number series for the fiscal year, enter each prefix used. For example:

| Station \# | PAT/Common Numbering Series + FY\* | Type of Purchase              | Funding            |
|----------------|----------------------------------------|-----------------------------------|------------------------|
| 610-           | A9                                     | Non-federal purchases using       | 36_0160 funds          |
| 610-           | B9                                     | Federal requisitions using        | 36_0160 funds          |
| 610-           | C9                                     | Certified invoice purchases using | 36_0160 funds          |
| 610-           | D9                                     | Non-federal purchases using       | 36\_/\_0161 funds      |
| 610-           | D95                                    | Certified invoice purchases using | 36\_/\_0161 funds      |
| 610-           | D98                                    | Federal requisitions using        | 36\_/\_0161 funds      |
| 610-           | IF                                     | Imprest funds purchases           |                        |
| 610-           | TA9                                    | Travel advances                   | \*9 = Fiscal Year 2009 |

When entering a new purchase order, the Purchasing Agent enters the first two or three digits of the common numbering series assigned to Purchasing Agents. IFCAP provides the next number in the series. Use the same procedure when selecting a PAT number for a Requisition or 1358.

*<u>TIP:</u>* You may use this option to tell IFCAP to assign numbers sequentially.

If you wish to establish PAT numbers to be used by different Purchasing Agents, you must instruct Purchasing Agent “A” to enter “A81”, Purchasing Agent “B” to enter “A82”, and Purchasing Agent “C” to enter “A83” when using the New Purchase Order option on their menu. Consider using this same process when you set up a numbering series used by Personal Property Management for requisitions or a series used by Fiscal for transactions.

### Add/Edit Supply Personnel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is simple, yet essential. It establishes the A&MM employees and positions in the New Person (#200) file. Without it, A&MM employees will not be able to accomplish any work with the options on their menu.

*<u>TIP</u>:* Personnel (such as Clerk-Typists) who are entering data, but not using an Electronic Signature, do not need to be entered in this file.

There are four types of Supply Personnel identified in this option:

- <u>WAREHOUSE</u> – This user processes Receiving Reports using the Receipt of Purchase Order option or Delete a Receiving Report under the Warehouse Menu.
- <u>PPM ACCOUNTABLE OFFICER</u> – This user uses the Process a Request in PPM or Edit a Request Signed in PPM as the Accountable Officer; or the Retransmit a 2237 to eCMS, or the Transaction Report - eCMS/IFCAP option.
- <u>PURCHASING AGENT</u> – This user is authorized to create purchase orders in IFCAP.
- <u>MANAGER</u> – This user is authorized to perform the functions of two or more of the Supply Personnel types listed above.

*<u>NOTE</u>:* A user identified as a manager cannot run the “Retransmit a 2237 to eCMS” option or the “Transaction Report - eCMS/IFCAP” option. These two options are available only to the user identified as PPM Accountable Officer.

<span id="_Toc522522814" class="anchor"></span>Figure 12: Sample Add/Edit Supply Personnel Screen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Add/Edit Supply Personnel</p>
<p>Select NEW PERSON NAME: IFUSER,TWO IW</p>
<p>SUPPLY EMPLOYEE: MANAGER// ?</p>
<p>1 WAREHOUSE</p>
<p>2 PPM ACCOUNTABLE OFFICER</p>
<p>3 PURCHASING AGENT</p>
<p>4 MANAGER</p>
<p>SUPPLY EMPLOYEE: PPM ACCOUNTABLE OFFICER</p>
<p>COMMERCIAL PHONE: 301-555-5555// &lt;= Enter the full 10 digit telephone number</p>
<p>FAX NUMBER: 301-555-5555//</p>
<p>EMAIL ADDRESS: IFUSER,TWO@FORUM.VA.GOV Replace</p>
<p>To edit the Signature Block Printed Name or title, Use TBOX</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Barcode Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Barcode processing was implemented to simplify the physical inventory process. Instead of counting inventory items manually and entering associated data via a terminal, data is collected at the inventory point using barcode equipment. Barcode assisted physical inventory can enhance the inventory process by:

- Improving the accuracy of the inventory data
- Reducing data entry errors
- Reducing the time consumed keying in the inventory data

Barcode technology introduced the use of the barcode label, reader/scanner, and printer. An inventory A&MM person operates a hand-held barcode reader to scan the appropriate barcode label affixed to the inventory bin, thus storing the inventory data in the barcode reader.

As required by respective services or at the end of the inventory cycle, data stored in the barcode reader is uploaded to IFCAP for processing. This involves physically connecting the barcode reader to the computer.

The Barcode Manager Menu contains the following options:

<span id="_Toc522522815" class="anchor"></span>Figure 13: Barcode Manager Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Barcode User</p>
<p>Download Barcode Program</p>
<p>Upload Barcode Data</p>
<p>Data Manager</p>
<p>Enter/Edit/View</p>
<p>Schedule Data to Process</p>
<p>Status of Data</p>
<p>Labels</p>
<p>Inquire Label</p>
<p>Print Labels</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

For detailed information on the use of the Barcode Manager Menu, see the [*Generic Inventory User’s Guide*](http://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1gip.doc).

### Clear FMS Exception File Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option clears the FMS Exception (#417.1) file of data entries earlier than the date you select.

STEP 1. From the Select IFCAP Application Coordinator Menu Option: prompt, select the Clear FMS Exception File Entries option.

STEP 2. Enter the latest date for which you want to retain entries. IFCAP will delete all entries recorded before that retention date.

<span id="_Toc522522816" class="anchor"></span>Figure 14: FMS Exception File Entries Option Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: Clear FMS Exception File Entries</p>
<p>This option will purge all FMS Exceptions File Entries earlier than the date which you select.</p>
<p>Enter date from which entries should be deleted: T-30 JAN 30,1995</p>
<p>Beginning File 417.1 cleanup..</p>
<p>End of processing</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### FMS Exception Transaction Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The control point reconciliation process was automated beginning with IFCAP version 5.0. Control Point files are automatically updated through MailMan messages transmitted from the Austin Automation Center (AAC). Occasionally, a site may receive a transaction for a control point where the FMS elements in IFCAP do not match the elements passed from FMS.

These transactions are stored in the FMS Exceptions (#417.1) file. This file is only used as a record of receipt. Any money associated with these transactions is not applied to any control point at the site. You may view these transactions by running the FMS Exception Transaction Report. This report generates a quarterly report of FMS transactions returned. The Budget Analyst will review the report, make necessary changes to the IFCAP control point setup, and use the Repost FMS Transactions option to enable the transaction to post correctly to the control point.

### Procurement of Accounting Transactions Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to generate a list of Procurement Accounting Transactions (PAT) by status or purchase order date. IFCAP sorts the PAT status reports by date. The following is an example of the report.

<span id="_Toc522522817" class="anchor"></span>Figure 15: Sample PAT Status Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: PAT Status Report</p>
<p>* Previous selection: DATE SIGNED not null</p>
<p>START WITH DATE SIGNED: FIRST//</p>
<p>* Previous selection: SUPPLY STATUS ORDER not null</p>
<p>START WITH SUPPLY STATUS ORDER: FIRST//</p>
<p>DEVICE: UCX/TELNET Right Margin: 80//</p>
<p>PROCUREMENT &amp; ACCOUNTING STATUS LIST DEC 7,1999 17:41 PAGE 1</p>
<p>PO # PO STATUS ASSIGNED</p>
<p>--------------------------------------------------------------------------------</p>
<p>B60008 Partial Order Received OCT 21,1997</p>
<p>B80001 Pending Fiscal Action OCT 9,1997</p>
<p>B80010 Cancelled Order DEC 15,1997</p>
<p>B80022 Ordered and Obligated FEB 4,1998</p>
<p>B90002 Pending Fiscal Action MAR 9,1999</p>
<p>B90003 Pending Fiscal Action MAR 16,1999</p>
<p>B90004 Pending Fiscal Action MAR 16,1999</p>
<p>B90005 Pending PPM Clerk Signature MAR 16,1999</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

STEP 1. From the START WITH DATE SIGNED: prompt, enter the earliest date that you want IFCAP to include in the report, or \<Enter\> to include all PAT status reports in the system.

STEP 2. At the START WITH SUPPLY STATUS ORDER: prompt, enter the first status order number that you want IFCAP to include in the report, or \<Enter\> to include all PAT status in the system.

STEP 3. At the DEVICE: prompt, specify an output device. IFCAP will create the Procurement and Accounting Status List, which shows every status within the date and number ranges you entered.

#### Repost FMS Exceptions

Use this option to attempt to repost FMS Exception file entries. It should be used only *after* you (or another authorized individual) has edited and reset the control point elements in IFCAP.

Occasionally, a site may receive a transaction for a control point containing FMS elements in IFCAP that do not match the elements passed from FMS. These transactions are stored in the FMS Exceptions (#417.1) file because they could not automatically update the control point files as a record of receipt. Duplicate entries are not posted to the FMS Transaction (#417) file.

As the Application Coordinator, you may view these transactions by running the FMS Exception Transaction Report. This report generates a quarterly accounting of FMS transactions returned. The Budget Analyst reviews the report, makes necessary changes to the IFCAP control point setup, and then uses the Repost FMS Transactions option.

### Reinstate IFCAP Terminated User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to reinstate a terminated IFCAP user who was removed by the Kernel functionality. For example, a user may have been terminated and then rehired. If appropriate, the user may also be added as a Supply employee when reinstated. You will receive a prompt to enter a name. You will then be asked to confirm the person is to be reinstated as an IFCAP user.

### Substation Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*<u>NOTE</u>*: The following step should be taken *only* if both of the following statements are true:

1.  You are an integrated facility (2 or more sites have been merged into one facility under one station number), *and*
2.  Your VISN CFO has indicated that your new integrated facility is to use Substation functionality in IFCAP.

> **CAUTION:** Once you invoke this feature, it cannot be reversed.

STEP 1. From the IFCAP Application Coordinator menu, select the Substation Enter/Edit Menu option.

If this option is invoked, IFCAP will request the substation entry as the control point users create 2237s and 1358s. When FMS documents are passed to the ACC, the substation will be passed and a few reports in FMS will show costing by substation.

Integrated sites may choose to invoke Substation functionality in IFCAP. This permits the Legacy site to be identified using the Primary Station Number (*e.g.,* XXX) and the substation code (*e.g.,* YY) assigned by headquarters. Thus, in IFCAP, the Legacy Station would be XXXYY. Using this system, 512A4 might represent Perry Point VAMC (a Legacy Site in the Maryland Health Care System), Station 512.

Use printer locations defined in the Site Parameter (#411) file via the Substation Enter/Edit Menu option when entering and/or approving 2237s and 1358s. When the appropriate printer location is defined for the substation attached to one of 2237s or 1358s documents, that printer location will be used. Otherwise, the printer location defined for the Primary Station will be used.

### Clinical Logistics Office Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Logistics Office (CLO) requires the ability to analyze field data, including specific reporting needs in performance measures and indicators. The Clinical Logistics Report Server (CLRS) will provide a temporary solution. Upon completion of the CLRS monthly reporting, Clinical Logistics data will reside on a server using Microsoft Structured Query Language (SQL) Server-based technology.

The CLRS tracks performance measures/indicators identified by CLO. It also provides a roll-up of station purchase order activity, which enables Clinical Logistics Analysts (CLA) to look at data pertaining to standardization, compliance, contracting, and related issues. CLAs also view <span id="PRC_158_A" class="anchor"></span>Inventory Point (GIP) station level statistics, so that Veterans Integrated Service Network (VISN) supply statistics at the VISN and national levels can be monitored and review 1358 Obligation transaction data as well.

Chief Logistics Officers and Central Office staff members can drill down to some of the indicator data via CLRS and its associated options.

Ultimately, the data gathered using the CLRS option will become part of the National Logistics Data Warehouse (NLD) strategy. The Data Warehousing Managers Group, which manages the Prosthetics server as well, will be performing the system administration functions for the CLRS.

The username and user DUZ are transmitted to the Clinical Logistics Report Server (CLRS) as part of the 1358 Authorization Detail record.

*<u>NOTE:</u>* As of Patch PRC\*5.1\*162, the Authorization Detail 1358 - F23 \[PRCHLO 1358 AUTHORIZATION DET\] option, which previously displayed the user who posted a payment or credit to the IFCAP authorization, will now display POSTMASTER as the user for credit amounts that are posted due to the new Central Fee transactions.

The CLO Menu enables the CLO to create reports. The menu contains three options:

<span id="_Toc522522818" class="anchor"></span>Figure 16: Sample Clinical Logistics Office Menu Options

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: CLINical Logistics Office Menu</p>
<p>CLO GIP Reports (CLRS)</p>
<p>CLO Procurement Reports (CLRS)</p>
<p>CLO System Parameters (CLRS)</p>
<p>CLRS Extract Validation Templates</p>
<p>Select Clinical Logistics Office menu option:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The two reporting options, CLO GIP Reports (CLRS) and CLO Procurement Reports (CLRS), are scheduled via *FileMan*. However, when the reports are needed off-cycle, or for some reason the scheduled jobs are not executed, these options can also be executed manually. The third option, CLO System Parameters (CLRS), is always run manually.

- Each month, routines are scheduled to run the data extracts needed for these reports. As part of this run, the *Virtual Memory System (VMS)* or Microsoft *Windows*® flat files for the Procurement and GIP extracts are created for *File Transfer Protocol (FTP)* transmission. One routine handles the Procurement data extracts, while another handles the GIP extracts.
- The first step in the CLRS reporting process to be run as indicated by the CLO is to extract the GIP data for the previous month (via PRCPLO CLO GIP OPTION \[PRCPLO3\]) and held in CLRS Report Storage (#446.7) file until it is transmitted to the CLRS.
- After that, the PRCHLO CLO PROCUREMENT \[PRCHLO5\] creates the Procurement extracts for the fiscal year when it is run according to CLO scheduling instructions.
- Finally, both extracts are sent to the CLRS via File Transfer Protocol (FTP).

With each run of the extracts, the data extracted to the CLRS Report Storage (#446.7) file clears, to avoid any lingering results from the previous run. This means that if another run doesn’t occur until the first of next month, data from the previous month will remain in CLRS Report Storage (#446.7) file until the next extract is generated. The previous month’s data is then deleted, and the file is repopulated with the results of the new extract run.

*<u>NOTE</u>*: The PRCHLO CLO PROCURMENT \[PRCHLO5\] option has been marked Out of Order with patch PRC\*5.1\*194.

#### CLO GIP Reports (CLRS)

The Clinical Logistics Office uses the CLO GIP Reports option to gather GIP information. It runs the *Stock Status Report* and *Days of Stock on Hand Report* for every combination of station and active inventory point present within a system and creates an extract in the CLRS Report Storage (#446.7) file.

These extracts are “\*” delimited and are stored in the file between report runs.

*<u>TIP</u>:* This option allows manual creation of the reports. When you use this option, the reports run immediately via a tasked-out job. Normally, the reports are created by means of a background job scheduled to run during off-peak hours.

<span id="_Toc522522819" class="anchor"></span>Figure 17: Sample CLO GIP Reports Option Selected

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CLO GIP Reports (CLRS)</p>
<p>CLO Procurement Reports (CLRS)</p>
<p>CLO System Parameters (CLRS)</p>
<p>Select Clinical Logistics Office Menu Option: CLO GIP Reports (CLRS)</p>
<p>Task # 2190 entered for the CLO GIP Reports.</p>
<p>Select Clinical Logistics Office Menu Option:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### CLO Procurement Reports (CLRS)

All purchase orders with the status of transaction complete, or transaction complete (amended) for a given monthly reporting cycle will be identified using this option.

<span id="_Toc522522820" class="anchor"></span>Figure 18: Sample CLO Procurement Reports Option Selected

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: CLINICAL Logistics Office Menu</p>
<p>CLO GIP Reports (CLRS)</p>
<p>CLO Procurement Reports (CLRS)</p>
<blockquote>
<p>&gt; Out of order: FTP SERVER SHUT DOWN, PRC*5.1*194</p>
</blockquote>
<p>CLO System Parameters (CLRS)</p>
<p>CLRS Extract Validation Templates</p>
<p>Select Clinical Logistics Office Menu Option: CLO PROcurement Reports (CLRS)</p>
<p>Task # 2191 entered for Procurement Reports.</p>
<p>Select Clinical Logistics Office Menu Option:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

All data will be pulled from the fields identified in the CLRS Reporting (Purchase Order Data) appendix to the *IFCAP Technical Manual.*

Upon completion of the extracts, the extracted data files will be sent via FTP to a directory location on the CLRS. The file transfer automatically occurs following the extract routine. The system sends advisory mail messages to the PRCPLO CLRS NOTIFICATIONS mail group.

Once CLRS receives the extracts, CLAs analyze the data.

Station level data is extracted/analyzed/cleansed monthly by CLAs.

*<u>TIP</u>:* This option allows manual creation of the reports. When you use this option, the reports run immediately via a tasked-out job. Normally, the reports are created by means of a background job scheduled to run during off-peak hours.

#### CLO System Parameters (CLRS)

There are several system parameters that are used for CLRS reporting. You may change these parameters when needed using the CLO System Parameters (CLRS) option.

<span id="PRC_154a" class="anchor"></span>Figure 19: CLO System Parameters Option Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: CLINICAl Logistics Office Menu</p>
<p>CLO GIP Reports (CLRS)</p>
<p>CLO Procurement Reports (CLRS)</p>
<p>CLO System Parameters (CLRS)</p>
<p>CLRS Extract Validation Templates</p>
<p>Select Clinical Logistics Office Menu Option: CLO SYStem Parameters (CLRS)</p>
<p>Stock on Hand Report Range: 90//180</p>
<p>Stock on Hand Report Range successfully set to 180</p>
<p>Stock on Hand Report Greater Than Range: 180//90</p>
<p>Stock on Hand Report Greater Than Range successfully set to 90</p>
<p>Stock Status Report Inactivity Range: 90//</p>
<p>CLRS Extract Directory: $1$DGA2:[ANONYMOUS.CLRS]// . . .(<em>NOTE: Fill in a valid value at your site.</em>)</p>
<p>CLRS Address: 10.2.3.4// . . .(<em>NOTE: This is an example. The P&amp;L office will supply the actual IP address.</em>)</p>
<p>CLRS Outlook Mail Group: <a href="mailto:VHACO10FPCLRS@e2k.va.gov//">VHACO10FPCLRS@e2k.va.gov//</a></p>
<p>User Name for CLRS Report Server Login: avalue //</p>
<p>Password for CLRS Report Server Login: avalue //</p>
<p>CLRS Regional Acquisition Center: ENTER VALID VALUE //</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Each parameter’s current value is displayed. You may enter a new value. Each time you change a parameter’s value, you will receive an on-screen confirmation message. Error messages will display when needed.

*<u>TIP</u>:* You should only change the value(s) of system parameter(s) when you are instructed to do so by CLO staff. To make changes, you must have the security key XUPROG, and you must coordinate with IRM.

#### CLRS Notification Messages

Members of the mail group PRCPLO CLRS NOTIFICATIONS receive status updates and exception messages concerning processes related to the CLRS.

The system will send the following messages to the mail group under the accompanying circumstance(s):

When a Procurement extract task is queued:

<span id="_Toc522522822" class="anchor"></span>Figure 20: Sample Procurement Extract Task Queued

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO Procurement Report Status for Dec 05, 2005@10:29:21 [#352893]</p>
<p>12/05/05@10:29 1 line</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>Task # 1189202 entered for Procurement Reports.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Procurement Extract Successfully Completed

When the Procurement extract completes successfully:

<span id="_Toc522522823" class="anchor"></span>Figure 21: Sample Procurement Extract Successfully Complete

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO Procurement Report Status for Dec 05, 2005@10:37:48 [#352896]</p>
<p>12/05/05@10:37 1 line</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>PO Procurement Data extract complete.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Transfer Build Completed

When the ^TMP file from the PO extract and the ^PRCP (#446.7) files for the GIP extracts have been pulled into the flat files for transfer:

<span id="_Toc522522824" class="anchor"></span>Figure 22: Sample Flat File for Transfer Build Complete

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO Environment Check &amp; Data Transfer for VMS / FTP , Dec 05, 2005</p>
<p>[#352897] 12/05/05@10:37 1 line</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>Built PO Activity Extracts and GIP Extracts for transfer</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Invalid/Undefined Extract Directory

When the system attempts to send the flat files to an invalid or undefined extract directory:

<span id="_Toc522522825" class="anchor"></span>Figure 23: Sample Flat Files Sent to Invalid / Undefined Extract Directory

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO Environment Check &amp; Data Transfer for VMS / FTP , Dec 05, 200</p>
<p>[#352894] 12/05/05@10:29 17 lines</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>Error with file deletion/cleanup prior to processing. Please contact IRM.</p>
<p>This error indicates the CLRS EXTRACT DIRECTORY has not</p>
<p>been properly set up during the installation of this patch.</p>
<p>(Please refer to the installation instructions for PRC*5.1*83)</p>
<p>A valid directory must be set up with the</p>
<p>proper read/write/execute/delete privileges.</p>
<p>In addition, the directory name which you create</p>
<p>must be added as the CLRS EXTRACT DIRECTORY</p>
<p>through the CLO System Parameters Option.</p>
<p>If the field is blank, you will generate this error.</p>
<p>Please confirm all steps have been performed</p>
<p>according to the Installation Guide for patch PRC*5.1*83.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### FTP Transfer Started

When the FTP transfer begins:

<span id="_Toc522522826" class="anchor"></span>Figure 24: Start of FTP Transfer

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO Environment Check &amp; Data Transfer for OS / FTP , Dec 13, 2005</p>
<p>[#353639] 12/13/05@12:44 23 lines</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*-------------------------------------------------------------------------------</p>
<p>Final FTP Setup complete, beginning FTP Transfer</p>
<p>The file transfer to the report server has been initiated.</p>
<p>You will be receiving a notification that the FTP</p>
<p>process has completed. The notification message</p>
<p>should be received within the hour. If you do not</p>
<p>receive the FTP process has completed message,</p>
<p>please contact IRM. IRM can confirm the process</p>
<p>is still running by performing the following</p>
<p>command:</p>
<p>At the Mumps Programmer prompt, type D ^%SS</p>
<p>See if there are any PRCHLO* routines running.</p>
<p>If these routines are present, the process is still</p>
<p>running. If you waited one hour, and did not get the</p>
<p>FTP process has completed message, a problem</p>
<p>was encountered. Further troubleshooting can be</p>
<p>performed by examining the LOGFILE CLRSxxxFTP1.LOG</p>
<p>where xxx is your station ID#. The logfile is</p>
<p>located in the following directory: $1$DGA2:[ANONYMOUS.CLRS]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### FTP Transfer Completed

When the FTP transfer completes:

<span id="_Toc522522827" class="anchor"></span>Figure 25: FTP Transfer Complete

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO Environment Check &amp; Data Transfer for OS / FTP , Dec 13, 2005</p>
<p>[#353640] 12/13/05@12:44 125 lines</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>The FTP Transfer process completed, Dec 13, 2005@12:44:51</p>
<p>The Clinical Logistics office should examine the Report Server</p>
<p>FTP directory for your files. If the files from your</p>
<p>station are not found, IRM can provide additional</p>
<p>troubleshooting steps by examining the LOGFILE</p>
<p>CLRSxxxFTP1.LOG where xxx is your station number.</p>
<p>The logfile is located in the directory: $1$DGA2:[ANONYMOUS.CLRS]</p>
<p>The contents of the logfile are listed below:</p>
<p>$ SET VERIFY=(PROCEDURE,IMAGE)</p>
<p>$ SET DEFAULT $1$DGA2:[ANONYMOUS.CLRS]</p>
<p>$ FTP 10.128.102.204 /INPUT=$1$DGA2:[ANONYMOUS.CLRS]CLRS500FTP.DAT</p>
<p>220 Microsoft FTP Service</p>
<p>Connected to vha16dw40.v16.med.va.gov.</p>
<p>331 Password required for clrsadmin.</p>
<p>230 User clrsadmin logged in.</p>
<p>Local directory now $1$DGA2:[ANONYMOUS.CLRS]</p>
<p>200 PORT command successful.</p>
<p>150 Opening ASCII mode data connection for ifcp500f1.txt.1.</p>
<p>226 Transfer complete.</p>
<p>local: $1$DGA2:[ANONYMOUS.CLRS]IFCP500F1.TXT.1 remote: ifcp500f1.txt.1</p>
<p>37881 bytes sent in 00:00:00.00 seconds (36993.16 Kbytes/s)</p>
<p>200 PORT command successful.</p>
<p>150 Opening ASCII mode data connection for ifcp500f10.txt.1.</p>
<p>226 Transfer complete.</p>
<p>local: $1$DGA2:[ANONYMOUS.CLRS]IFCP500F10.TXT.1 remote: ifcp500f10.txt.1</p>
<p>7880 bytes sent in 00:00:00.00 seconds (7695.31 Kbytes/s)</p>
<p>200 PORT command successful.</p>
<p>150 Opening ASCII mode data connection for ifcp500f11.txt.1.</p>
<p>226 Transfer complete.</p>
<p>local: $1$DGA2:[ANONYMOUS.CLRS]IFCP500F11.TXT.1 remote: ifcp500f11.txt.1</p>
<p>9724 bytes sent in 00:00:00.00 seconds (9496.09 Kbytes/s)</p>
<p>200 PORT command successful.</p>
<p>150 Opening ASCII mode data connection for ifcp500f12.txt.1.</p>
<p>226 Transfer complete.</p>
<p>local: $1$DGA2:[ANONYMOUS.CLRS]IFCP500F12.TXT.1 remote: ifcp500f12.txt.1</p>
<p>200 PORT command successful.</p>
<p>150 Opening ASCII mode data connection for ifcp500g1.txt.1.</p>
<p>226 Transfer complete.</p>
<p>local: $1$DGA2:[ANONYMOUS.CLRS]IFCP500G1.TXT.1 remote: ifcp500g1.txt.1</p>
<p>5633 bytes sent in 00:00:00.00 seconds (5500.98 Kbytes/s)</p>
<p>200 PORT command successful.</p>
<p>150 Opening ASCII mode data connection for ifcp500g2.txt.1.</p>
<p>226 Transfer complete.</p>
<p>local: $1$DGA2:[ANONYMOUS.CLRS]IFCP500G2.TXT.1 remote: ifcp500g2.txt.1</p>
<p>2731 bytes sent in 00:00:00.00 seconds (2666.99 Kbytes/s)</p>
<p>221</p>
<p>$ EXIT 3</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### GIP Reports Can’t Run

GIP reports can’t run – needed lock being unavailable due to a conflicting process running:

<span id="_Toc522522828" class="anchor"></span>Figure 26: GIP Reports Will Not Run – Needed Lock Unavailable

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO GIP Report Status for Dec 14, 2005@15:19:42</p>
<p>[#16840] 12/14/05@15:19 1 line</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>Error encountered when attempting to run CLO GIP Reports due to other CLRS extracts in progress, please try again later.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Procurement/Transfer Process Can’t Run

The Procurement/Transfer process can’t run— the lock needed is unavailable due to a conflicting process running:

<span id="_Toc522522829" class="anchor"></span>Figure 27: Procurement / Transfer Process Will Not Run – Needed Lock Unavailable

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO Environment Check &amp; Data Transfer for OS / FTP , Dec 14, 2005 [#5305]</p>
<p>12/14/05@14:12 3 lines</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>Error encountered when attempting to run CLO PO</p>
<p>activity reports due to other CLRS extracts in</p>
<p>progress. Please try again later.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### FTP Log-in Failed: Username is Null

<span id="_Toc522522830" class="anchor"></span>Figure 28: Username is Null

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO Environment Check &amp; Data Transfer for OS / FTP , A date [#5305]</p>
<p>3/10/09@14:12 2 lines</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p>
<p>There is no user name identified in the CLRS USER NAME Parameter.</p>
<p>Please correct and retry.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### FTP Log-in Failed Password is NULL

<span id="_Toc522522831" class="anchor"></span>Figure 29: Password is Null

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO Environment Check &amp; Data Transfer for OS / FTP , A date [#5305]</p>
<p>3/10/09@14:12 2 lines</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p>
<p>There is no password identified in the CLRS PASSWORD Parameter.</p>
<p>Please correct and retry.</p>
<p>Subj: CLO Environment Check &amp; Data Transfer for OS / FTP , A date [#5305]</p>
<p>3/10/09@14:12 2 lines</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

There is no password identified in the CLRS PASSWORD Parameter.

Please correct and retry.

#### Error Writing Entry to File \#446.7

<span id="_Toc522522832" class="anchor"></span>Figure 30: Error Writing Entry to File \#446.7

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: CLO GIP Report Status for Mar 08, 2007@12:59:11 [#56327380]</p>
<p>03/08/07@12:59 5 lines</p>
<p>From: CLINICAL LOGISTICS REPORT SERVER In ‘IN’ basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>Error saving to File #446.7 for Stock Status Report, related data:</p>
<p>Station: 036 MEMPHIS</p>
<p>Inventory Point: 28 RADIOLOGY</p>
<p>File #446.7 Field Set Attempted: 7///6*0*6*85448.49*0*85448.49*1*0*1*11*0*11</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### CLRS Extract Validation Templates

This set of templates enables the User to generate a printout of data from the appropriate IFCAP file associated with a specific data extract to assist in validating the data. There is a template that corresponds to each Procurement extract.

<span id="_Toc222493278" class="anchor"></span>Figure 31: CLRS Extract

<span id="PRC_154b" class="anchor"></span>Select Clinical Logistics Office Menu Option: CLRS Extract Validation Templates

Master Data PO - F1

Obligation Data PO - F2

Method of Purchase PO - F3

Discount Data PO - F4

Line Item Detail PO - F5

Inventory Line Item Data PO - F6

Receiving of Item on PO - F7

Item Description PO - F8

Partial Data PO - F9

Data 2237 Multiple of PO - F10

BOC DATA PO - F11

Comments PO first line - F12

Remarks PO first line - F13

Prompt Payment Terms PO - F14

Amount PO - F15

Amendment Data PO - F16

Changes PO Amendment - F17

Description of PO Amendment - F18

Breakout Code PO - F19

Control Point Activities - F20

Sub Control Point Activity - F21

Daily Record 1358 - F22

Authorization Detail 1358 - F23

IH Invoice Tracking Header - F24

IP Invoice Tracking Prompt Pmt Terms - F25

IF Invoice Tracking FMS Lines - F26

IC Invoice Tracking Certifying Svc - F27

The username and user DUZ are transmitted to the Clinical Logistics Report Server (CLRS) as part of the 1358 Authorization Detail record.

As of Patch PRC\*5.1\*162, the Authorization Detail 1358 - F23 \[PRCHLO 1358 AUTHORIZATION DET\] option, which previously displayed the user who posted a payment or credit to the IFCAP authorization, will now display POSTMASTER as the user for credit amounts that are posted due to the new Central Fee transactions. 

Fee Basis posts a credit amount to the IFCAP authorization when a payment line item is flagged as rejected. If the payment line item is flagged as rejected by a Fee Basis background job that is processing a transaction from Central Fee (Austin), the user recorded in the IFCAP transaction will be the POSTMASTER.

### Compliance Reports (1358)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Compliance Reports (1358) menu contains two reports that enable the site to monitor compliance with the GAO requirements to maintain a Separation of Duties within the 1358 process in IFCAP.

#### Separation of Duties Violations

The Separation of Duties Violations report will list any 1358 transactions that have the same User defined in more than one Role CP Clerk ((Requestor), CP Official (Approver) and Accounting Technician (Obligated by) for the time selected.

<span id="_Toc522522833" class="anchor"></span>Figure 32: Separation of Duties Violations

> Select Compliance Reports (1358) Option: separation of Duties Violations Report

> \(1358\)

> \* Previous selection: DATE SIGNED (APPROVED from May 10,2009 to May 13,2009

> START WITH DATE SIGNED (APPROVED): May 10,2009// 050709 (MAY 07, 2009)

> GO TO DATE SIGNED (APPROVED): May 13,2009// \<Enter\> (MAY 13, 2009)

> DEVICE: 0;80;9999 TELNET

> 1358 SEPARATION OF DUTIES VIOLATIONS MAY 13,2009 13:28 PAGE 1

> Sort Criteria: DATE SIGNED (APPROVED) from May 7,2009 to May 13,2009@24:00

> FORM TYPE equals 1358 ORDER

> (REQUESTOR=APPROVING OFFICIAL)!(REQUESTOR=OBLIGATED BY)!(APPROVIN

> G OFFICIAL=OBLIGATED BY)

> TRANSACTION#

> DATE APPROVING

> APPROVED REQUESTOR OFFICIAL OBLIGATED BY

> OBLIGATION

> \$ AMT TYPE

> --------------------------------------------------------------------------------

> 688-09-3-045-0059 05/07/09 IFUSER, ONE IFUSER, TWO IFUSER, ONE

> 688-C95107 199.99 OBLIG

> 688-09-3-045-0070 05/08/09 IFUSER, TWO IFUSER, TWO IFUSER, TWO

> 688-C95116 123.00 ADJUS

> 688-09-3-045-0065 05/08/09 IFUSER, ONE IFUSER, TWO IFUSER, TWO

> 688-C95115 10.00 ADJUS

*<u>NOTE</u>*: This report was scheduled as a tasked job during the installation of Patch PRC\*5.1\*130. The report is automatically generated daily (Monday through Saturday). The output will include any records generated the previous day.

*<u>NOTE</u>*: Monday’s report will contain records from Saturday & Sunday. The report will be sent to Users who are members of the 1358 Monitors mail group.

#### Invoice Certification Seg Duties Violation Report

This report shows requestors, approvers, obligators, and certifiers in IFCAP's Invoice/Tracking module of 1358s and identifies violations of segregation of duties policy. This report identifies 1358s based on certified invoices in the IFCAP invoice/tracking module and does not present 1358s which are certified in other VistA packages or other systems.

<span id="_Toc222493280" class="anchor"></span>Figure 33: Sample Invoice/Tracking Module of 1358s

Select Compliance Reports (1358) Option: Invoice Certification Seg Duties Violation Rpt

From Date: Apr 01, 2011// \<Enter\> (APR 01, 2011)

To Date: Apr 30, 2011// \<Enter\> (APR 30, 2011)

For all stations? YES// \<Enter\>

Only list 1358s with a violation (Y/N)? YES// \<Enter\>

DEVICE: HOME// \<Enter\> TELNET

IFCAP 1358 Segregation of Duties MAY 06, 2011@17:04:41 page 1

Including Certifications from Apr 01, 2011 to Apr 30, 2011@23:59:59 for all stations

Only 1358s with a segregation of duty violation shown.

1358 DATE/TIME EVENT/INV# ROLE NAME

---------- -------------- ----------- --------- ------------------------------

1 invoice certification was found during the report period.

1 1358 Obligation is referenced.

A violation of segregation of duties was detected on none of the 1358s.

*<u>NOTE:</u>* No violation was found, therefore no detailed data is shown in the report.

<span id="_Toc222493281" class="anchor"></span>Figure 34: Sample Report Showing No 1358 Compliance Violations

Select Compliance Reports (1358) Option: Invoice Certification Seg Duties

Violation Rpt

From Date: Apr 01, 2011// 090110 (SEP 01, 2010)

To Date: Sep 30, 2010// t (MAY 06, 2011)

For all stations? YES// n NO

Select ADMIN. ACTIVITY SITE PARAMETER STATION/SUBSTATION CODE: 688 WASHINGT

ON, DC

Only list 1358s with a violation (Y/N)? YES// n NO

DEVICE: HOME// TELNET

IFCAP 1358 Segregation of Duties MAY 06, 2011@17:10 page 1

Including Certifications from Sep 01, 2010 to May 06, 2011@23:59:59 for Station 688

1358 DATE/TIME EVENT/INV# ROLE NAME

---------- -------------- ----------- --------- ------------------------------

688-C05004 08/31/10@10:33 OBLIGATE REQUESTOR PRCAPPROVER,FOUR

APPROVER PRCAPPROVER,FOUR

OBLIGATOR PRCAPPROVER,FOUR

\*\*\*Approver previously acted as requestor on this transaction.

\*\*\*Obligator previously acted as requester on this transaction.

\*\*\*Obligator previously acted as approver on this transaction.

12/10/10@11:09 373 CERTIFIER VOUCHER,AUDIT

01/05/11@11:48 393 CERTIFIER VOUCHER,AUDIT

---------- -------------- ----------- --------- ------------------------------

688-C05010 09/08/10@10:29 OBLIGATE REQUESTOR PRCSUPERVISOR,ONE

APPROVER PRCSUPERVISOR,ONE

OBLIGATOR PRCSUPERVISOR,ONE

\*\*\*Approver previously acted as requestor on this transaction.

\*\*\*Obligator previously acted as requester on this transaction.

\*\*\*Obligator previously acted as approver on this transaction.

---------- -------------- ----------- --------- ------------------------------

688-C05012 09/09/10@16:36 OBLIGATE REQUESTOR CPCLERK,ONE

APPROVER CPCLERK,ONE

OBLIGATOR CPCLERK,ONE

\*\*\*Approver previously acted as requestor on this transaction.

\*\*\*Obligator previously acted as requester on this transaction.

\*\*\*Obligator previously acted as approver on this transaction.

---------- -------------- ----------- --------- ------------------------------

688-C05017 09/13/10@15:15 OBLIGATE REQUESTOR CPCLERK,FOUR

APPROVER PRCAPPROVER,TWO

OBLIGATOR PRCAPPROVER,TWO

\*\*\*Obligator previously acted as approver on this transaction.

01/04/11@12:17 391 CERTIFIER PRCVOUCHER,THREE

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

IFCAP 1358 Segregation of Duties MAY 06, 2011@17:10 page 5

Including Certifications from Sep 01, 2010 to May 06, 2011@23:59:59 for Station 688

1358 DATE/TIME EVENT/INV# ROLE NAME

---------- -------------- ----------- --------- ------------------------------

688-C05044 01/10/11@15:58 OBLIGATE REQUESTOR PRCTESTER,FIVE

APPROVER PRCAPPROVER,FOUR

OBLIGATOR PRCTESTER,SIX

01/10/11@16:03 397 CERTIFIER PRCTESTER,SEVEN

---------- -------------- ----------- --------- ------------------------------

688-C05045 02/14/11@11:22 OBLIGATE REQUESTOR PRCTEST,FIVE

APPROVER PRCAPPROVER,FIVE

OBLIGATOR PRCTESTER,SIX

02/14/11@16:10 398 CERTIFIER PRCTESTER,SEVEN

---------- -------------- ----------- --------- ------------------------------

688-C15208 11/22/10@11:05 OBLIGATE REQUESTOR PRCUSER,ONE

APPROVER PRCUSER,TWO

OBLIGATOR PRCTESTER,FIVE

11/22/10@11:20 360 CERTIFIER PRCCLERK,SIX

11/22/10@15:04 361 CERTIFIER CPTESTER,FIVE

\*\*\*User previously acted as obligator on a prior 1358 event.

11/23/10@17:23 363 CERTIFIER CPACCOUNT,TEN

11/24/10@11:32 364 CERTIFIER CPACCOUNT,TEN

11/24/10@12:14 365 CERTIFIER PRCCLERK,TWO

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

IFCAP 1358 Segregation of Duties MAY 06, 2011@17:10 page 8

Including Certifications from Sep 01, 2010 to May 06, 2011@23:59:59 for Station 688

1358 DATE/TIME EVENT/INV# ROLE NAME

---------- -------------- ----------- --------- ------------------------------

688-C15217 01/05/11@10:47 OBLIGATE REQUESTOR CPCLERK,ONE

APPROVER CPAPPROVER,TWO

OBLIGATOR PRCUSER,TEN

01/05/11@11:09 392 CERTIFIER CPAUDITOR,ONE

---------- -------------- ----------- --------- ------------------------------

25 invoice certifications were found during the report period.

14 1358 Obligations are referenced.

A violation of segregation of duties was detected on 5 of the 1358s.

### Let Staff Replace Inventory Quantities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option requires the PRCPAQOH security key and allows you to designate inventory staff who will be allowed to replace the on-hand quantities in the secondary inventory point in GIP with the on-hand quantities in the automated supply station linked to that inventory point. See the *Point of Use Manual* for additional information concerning this option.

### On-Demand Users Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option requires the PRCPODI security key and allows you to assign selected inventory users the ability to flag items in specific inventory points as being On-Demand or Standard. Users with the ability to flag an item as On-Demand are referred to as On-Demand users within the option.

The option was created to limit the number of inventory users that are permitted to change the On-Demand/Standard designation of an item. Since the On-Demand/Standard designation is used in calculating performance measures, improper use of the functionality could potentially permit inaccurate reporting.

It is expected that the Inventory Supervisors and Logistics Managers will determine who is to be listed as an On-Demand user and who is to be removed as an On-Demand user for a given inventory point.

<span id="_Toc522522834" class="anchor"></span>Figure 35: Sample On-Demand User Option

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP MENU Option: IFCAP Application Coordinator Menu</p>
<p>Select IFCAP Application Coordinator Menu Option: ON-Demand Users Enter/Edit</p>
<p>INVENTORY POINT MANAGER: IFUSER,ONE ONE 192-2</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&gt;&gt;IFUSER,ONE is not an On-Demand User in any Primary Inventory Point <em>Only primary inventory points are checked</em></td>
</tr>
<tr class="even">
<td><p>Select STATION NUMBER (‘^’ TO EXIT): 688// WASHINGTON, DC</p>
<p>SELECT INVENTORY POINT: SPD 688-SPD PRIMARY</p></td>
</tr>
<tr class="odd">
<td><p>Add as an On-Demand User? YES <em>Answer YES to add</em></p>
<p>&lt;&lt;Added&gt;&gt;</p></td>
</tr>
<tr class="even">
<td>Checking distribution points for 688-SPD... <em>This check is automatic and lists only Secondary Inventory points where user is or can be an On-Demand user.</em></td>
</tr>
<tr class="odd">
<td><p>IFUSER,ONE is a User and Manager on the following Inventory Points:</p>
<p>688-CLINIC USERONE’S Not On-Demand User</p>
<p>688-*USERTWO’S SECONDARY_42* Not On-Demand User</p>
<p>688-IFUSER Not On-Demand User</p>
<p>688-CASE CART Not On-Demand User</p>
<p>SELECT INVENTORY POINT:</p></td>
</tr>
</tbody>
</table>

An On-Demand user can also lose the ability to flag items.

<span id="_Toc522522835" class="anchor"></span>Figure 36: Sample On-Demand User Option Removal

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: on-Demand Users Enter/Edit</p>
<p>INVENTORY POINT MANAGER: IFUSER,ONE ONE 192-2</p>
<p>IFUSER,ONE is an On-Demand User in these Primary Inventory Points:</p>
<p>688-SPD</p>
<p>Select STATION NUMBER (‘^’ TO EXIT): 688// WASHINGTON, DC</p>
<p>SELECT INVENTORY POINT: spd 688-SPD PRIMARY</p>
<p>Remove as an On-Demand User? y YES</p>
<p>&lt;&lt;Removed&gt;&gt;</p>
<p>Checking distribution points for 688-SPD...</p>
<p>IFUSER,ONE is a User and Manager on the following Inventory Points:</p>
<p>688-CLINIC USERONE’S Not On-Demand User</p>
<p>688-*USERTWO’S SECONDARY_42* Not On-Demand User</p>
<p>688-IFUSER Not On-Demand User</p>
<p>688-CASE CART Not On-Demand User</p>
<p>SELECT INVENTORY POINT:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Posted Dietetic Cost Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report prints posted items with LOG voucher numbers. The report is sorted by Food Group and Date of Transaction. The report lists each inventory point, National Stock Number (NSN) of each item, short description of the item, and its LOG voucher number.

STEP 1. At the Start with Other Inventory Point Affected: prompt, enter the first inventory point that you want IFCAP to include in the report, or \<Enter\> \> to include all the inventory points in the system.

STEP 2. At the Start with Food Group: prompt, enter the first Food Group that you want IFCAP to include in the report, or \<Enter\> to include all the Food Groups in the system.

<span id="_Toc522522836" class="anchor"></span>Figure 37: Sample Posted Dietetic Cost Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>POSTED DIETETIC COST REPORT NOV 3,1999 10:36 PAGE 1</p>
<p>VOUCHER</p>
<p>NSN SHORT DESCRIPTION NUMBER</p>
<p>DATE OF</p>
<p>TRANSACTION AMOUNT PACK UNIT UNIT COST TOTAL</p>
<p>--------------------------------------------------------------------------------</p>
<p>OTHER INVENTORY POINT AFFECTED: 658-DIETETIC SUBSISTENCE</p>
<p>FOOD GROUP: Commercial Nutritional Products, Tube feedings &amp; supplements</p>
<p>8940-01-361-8272 DIET SUPMT THPELQD8OZ I90229</p>
<p>JAN 5,1999 6 24/PG 7.680 46.08</p>
<p>8940-01-361-8271 DIET SUPMT VANL LQD 8 OZ I90229</p>
<p>JAN 5,1999 6 24/PG 7.080 42.48</p>
<p>8940-01-361-8272 DIET SUPMT THPELQD8OZ I90233</p>
<p>JAN 6,1999 4 24/PG 7.680 30.72</p>
<p>8940-01-160-1299 DIET SUPMT THPE VAN 8 OZ I90233</p>
<p>JAN 6,1999 3 24/PG 8.160 24.48</p>
<p>8940-01-361-8271 DIET SUPMT VANL LQD 8 OZ I90233</p>
<p>JAN 6,1999 2 24/PG 7.080 14.16</p>
<p>8940-01-361-8269 DIET SUPMT CHOC LQD 8 OZ I90250</p>
<p>JAN 11,1999 3 24/PG 7.080 21.24</p>
<p>8940-01-361-8272 DIET SUPMT THPELQD8OZ I90250</p>
<p>JAN 11,1999 2 24/PG 7.680 15.36</p>
<p>8940-01-160-1299 DIET SUPMT THPE VAN 8 OZ I90250</p>
<p>JAN 11,1999 3 24/PG 8.160 24.48</p>
<p>8940-01-361-8271 DIET SUPMT VANL LQD 8 OZ I90250</p>
<p>JAN 11,1999 6 24/PG 7.080 42.48</p>
<p>8940-01-361-8272 DIET SUPMT THPELQD8OZ I90264</p>
<p>JAN 14,1999 9 24/PG 7.680 69.12</p>
<p>8940-01-160-1299 DIET SUPMT THPE VAN 8 OZ I90264</p>
<p>JAN 14,1999 2 24/PG 8.160 16.32</p>
<p>8940-01-361-8271 DIET SUPMT VANL LQD 8 OZ I90264</p>
<p>JAN 14,1999 2 24/PG 7.080 14.16</p>
<p>8940-01-361-8271 DIET SUPMT VANL LQD 8 OZ I90289</p>
<p>JAN 22,1999 11 24/PG 7.080 77.88</p>
<p>----------------- ---------</p>
<p>SUBTOTAL 522.72</p>
<p>SUBCOUNT 16</p>
<p>POSTED DIETETIC COST REPORT NOV 3,1999 10:36 PAGE 4</p>
<p>VOUCHER</p>
<p>NSN SHORT DESCRIPTION NUMBER</p>
<p>DATE OF</p>
<p>TRANSACTION AMOUNT PACK UNIT UNIT COST TOTAL</p>
<p>--------------------------------------------------------------------------------</p>
<p>FOOD GROUP: Commercial Nutritional Products, Tube feedings &amp; supplements</p>
<p>----------------- ---------</p>
<p>TOTAL 522.72</p>
<p>COUNT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

STEP 1. At the Start with Date of Transaction: prompt, enter the first transaction date that you want IFCAP to include in the report, or \<Enter\> to include all the transaction dates in the system.

STEP 2. Enter an output device. IFCAP prints the Posted Dietetic Cost Report, listing each inventory point, the National Stock Numbers of each item, the short description of the item, and its LOG voucher number.

### Unposted Dietetic Cost Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to generate a report showing unposted items sorted by PO number, food group, and date received.

<span id="_Toc522522837" class="anchor"></span>Figure 38: Sample Unposted Dietetic Cost Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select STATION NUMBER (‘^’ TO EXIT): 688// WASHINGTON, DC</p>
<p>START WITH FCP: FIRST//</p>
<p>* Previous selection: DATE RECEIVED not null</p>
<p>START WITH DATE RECEIVED: FIRST//</p>
<p>DEVICE: UCX/TELNET RIGHT MARGIN: 80//UNPOSTED DIETETIC COST REPORT NOV 8,1999 11:12 PAGE 1</p>
<p>PURCHASE UNIT</p>
<p>ORDER QTY BEING PACK OF</p>
<p>NUMBER FCP AMOUNT RECEIVED DATE RECEIVED MULT PURCHASE</p>
<p>DESCRIPTION</p>
<p>-------------------------------------------------------------------------------</p>
<p>FOOD GROUP: Fruits, Vegetables</p>
<p>688-G90001 4537 15.00 30 JUL 20,1999 1 BG</p>
<p>SQUASH, SUMMER SLICED, FROZEN TYPE II (A) YELLOW</p>
<p>CROOKNECK, EARLY YELLOW, STRAIGHT NECK GRADE A OR</p>
<p>B, 2-5 LB PG, FG 3</p>
<p>----------</p>
<p>SUBTOTAL 15.00</p>
<p>FOOD GROUP: EMPTY</p>
<p>688-G90003 4537 172.50 15 JUL 20,1999 1 EA</p>
<p>CABBAGE-STUFFED</p>
<p>----------</p>
<p>SUBTOTAL 172.50</p>
<p>TOTAL 187.50 -------</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

STEP 1. At the Start with Date Received: prompt, enter the first date received that you want IFCAP to include in the report, or \<Enter\> to include all the dates received.

STEP 2. Enter an output device. IFCAP generates the Unposted Dietetic Cost Report, listing each food group, the purchases for that food group, and their costs.

### Quarter Review of Vouchers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option in accordance with VA Directive 7127.1, March 27, 1996, *Accounting Requirements*.

- PURPOSE: This directive provides acquisition and materiel management policies required to audit VA vouchers.
- POLICY: All facilities using IFCAP will conduct a quarterly audit of all vouchers to determine that application of duplicate signatures on voucher documents are analyzed for validity of item or service requirement.
- RESPONSIBILITY: The Deputy Assistant Secretary for Acquisition and Materiel Management (90) will ensure a program is established to review and issue Department wide guidance and support.
- REFERENCES: OIG Report NO. 1AD-G07-116, *Audit of IFCAP<u>TIP</u>*: This report should be printed in Landscape Mode at 16 or 17 characters per inch (cpi).

STEP 1. You will be prompted for a starting date and an ending date to review.

STEP 2. Enter a device to display the information.

<span id="_Toc522522838" class="anchor"></span>Figure 39: Sample Data for Quarterly Review of Vouchers Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select IFCAP Application Coordinator Menu Option: QUARTERly Review of Vouchers</p>
<p>┌────────────────────────────────────────────────┐</p>
<p>| For proper format, this report MUST be printed │</p>
<p>│ in LANDSCAPE mode (16 or 17 cpi |</p>
<p>Start with Date: 010105 (JAN 01, 2005)</p>
<p>End with Date: 033105 (MAR 31, 2005)</p>
<p>DEVICE: HOME// 0;80;9999 TELNET TERMINAL</p>
<p>P.O.# FCP APPROVING OFFICIAL</p>
<p>PURCHASING AGENT</p>
<p>RECEIVING OFFICIAL</p>
<p>PARTIAL DATE</p>
<p>--------------------------------------------------------------------------------</p>
<p>111-T50564 041 MISCN EXPENSES TEST, USER</p>
<p>TEST, USER</p>
<p>SUPPLY, USER</p>
<p>Jan 27, 2005</p>
<p>111-T50560 041 MISCN EXPENSES TEST, USER</p>
<p>TEST, USER</p>
<p>PLACE, HOLDER</p>
<p>Jan 24, 2005</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Establish IFCAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The procedures discussed in the following paragraphs are presented in the order needed to bring up IFCAP. The following procedures would normally be performed when IFCAP is initially started at a site (go live situation). But as of this writing, IFCAP is a well-established package used by all sites that employ VistA. If there is a need to re-establish IFCAP due to a catastrophic failure or a natural disaster these procedures have been retained in the user’s guide.

The following paragraphs present step-by-step instructions on how to bring IFCAP up when it has not previously been installed.

*<u>NOTE</u>*: You may need all or part of these procedures. Each circumstance is different.

#### Loading Files

IFCAP users must appear in the New Person (#200) file. The Site Manager usually enters the users, or the task may be assigned to the Application Coordinator. In either case, it is essential that a list of IFCAP users be compiled, including each user’s assigned menu(s), *e.g.*, PRCSCP OFFICIAL for Control Point Officials.

*<u>TIP</u>*: If your site is using the file access provisions of Kernel, ensure users have access to the files that they will need. Contact your Site Manager/IRM for assistance.

Certain menus require that users have a security key to access options on those menus. These include the menus for Control Point Officials, Chiefs of P&C, PPM, the Warehouse, Accounting, and Inventory Managers.

STEP 1. Ensure all users are in the New Person (#200) file. See 3.3 above.

#### Menu and Security Keys

STEP 1. Work with your IRM Chief to make sure that each user is assigned the correct menus and security keys for their user category. See 3.3 above.

#### Add/Edit Supply Personnel

STEP 1. Work with your Acquisitions and Logistics staff to ensure that the appropriate Users are identified as Supply personnel. See Section 4.5 for more information.

#### Site Parameters

STEP 1. See 4.2 above for details.

#### Control Point Setup

To establish Fund Control Points, the Budget Analyst *must* use the Fund Distribution Program Menu.

STEP 1. Select the Budget Utilities Menu.

STEP 2. Select the FCP/CC/BOC Management Menu.

STEP 3. Select the Fund Control Point Management Menu.

STEP 4. Using the Add/Edit Control Point option, enter the required information for each of the Fund Control Points.

*<u>NOTE</u>*: You will also enter information concerning personnel for each Control Point. Control Point users must have been established in the New Person (#200) file. This establishes the Control Point and Control Point users with level of access to the Control Point (*e.g.*, Control Point Official, Control Point Clerk, and any Requestors for the Control Point).

IFCAP checks the Fund Control Point file to see if the order is being placed for a special Control Point when processing a request, purchase order, or requisition. “Special” Control Points include Supply Fund, General Post Fund, Construction, or Canteen appropriations.

Each of these types of special Control Points is processed differently by IFCAP to adhere to the requirements of FMS, CAPPS, LOG 1 and Department of Veterans Affairs (VA) policies and procedures.

The Control Point Add/Edit option on the Fund Control Point Management Menu allows you to identify which Fund Control Points are “special” Control Points, so the users will not be required to enter cost centers and/or BOCs.

The Budget Analyst should identify individuals designated as Releasing Officials for the FMS documents that are created within the Funds Distribution module. The Budget Analyst also selects the correct over-commit status allowed for each Control Point for the site.

*<u>NOTE</u>*: Enabling the station level over-commit switch will override each Control Point’s over-commit status. The switches that control the processing of orders without Fiscal concurrence are also set in this option.

#### Assign LOG Department Numbers to all Fund Control Points

Use the Assign LOG Department Number to Fund Control Point option on the PPM Utilities Menu to ensure each Control Point that generates requests has a LOG Department number as required when generating LOG code sheets. Remember: The control point cannot be used for doing business in IFCAP if it does not have an assigned LOG Department number.

*<u>TIP</u>*: Contact the PPM Accountable Officer to obtain LOG Department numbers.

STEP 1. Using the Assign LOG Department Number to Fund Control Point option, enter the required information for each new Fund Control Point.

#### Distribute Ceiling Amounts to Control Points

The ceilings are entered by Fiscal Service using the Funds Distribution Program Menu.

STEP 1. Initially, the Budget Analyst must first use the Add a New Transaction option to establish the ceiling amount; use the Release Transaction option to enter the ceiling amount into the Control Point Official’s running balance. Employ the Generate FMS Budget Documents option to create the FMS sub-allowance documents for transmission to FMS in Austin.

#### Build Vendor File

There are two ways of entering vendors into the Vendor (#440) file:

- The Purchasing Agent may establish a vendor at the time a new purchase order is being entered.
- You may use the Vendor File Edit option in the Purchasing Agent Menu (this option allows you to enter or edit vendor information).

Vendors under a special contract with the government to guarantee the delivery of goods directly to patients are to be identified in the Vendor (#440) file as Guaranteed Delivery Vendors. IFCAP processes the purchase orders placed with these vendors differently than other vendors.

STEP 1. Use the Federal Vendor Edit option on the PPM Utilities Menu to identify the GSA, DLA, and VA Supply Warehouse vendors used for creating requisitions and Issue Book transactions. You may have multiple entries for GSA, DLA, or the VA Supply Depot to account for the different offices providing service to your facility.

*<u>NOTE</u>*: You may identify only one VA Supply Warehouse vendor.

STEP 2. Employ the EDI Vendor Edit option from the IFCAP Application Coordinator Menu. This option establishes a vendor as an EDI vendor. If a designated EDI vendor is not entered through this option, Purchase Orders cannot be processed electronically. The vendor must exist in the station Vendor file to be selected in the EDI Vendor Edit option.

#### Build Item File

STEP 1. You must enter the repetitive purchases of any item in the Item Master (#441) file. Use the Item File Edit option on either the Posted Stock Management Menu of the Requisition Clerk Menu or the P&C Utilities Menu of the Purchasing Agent to enter or edit this information.

*<u>NOTE</u>*: You must coordinate with the National Item File (NIF) Item File group to ensure that your items receive National Item file numbers.

#### Inventory

#### Warehouse Inventory

Your site may wish to maintain a local Warehouse Inventory using IFCAP. The inventory can be created using the option Inventory Point Management on the Accountable Officer Menu. Once the Warehouse Inventory file has been established, the designated users, who are a part of the PPM staff, can use the Warehouse Inventory Main Menu \[PRCPW MAIN MENU\] to set up items.

#### Primary Inventory 

If some of your fund Control Points wish to run the General Inventory System, you may establish Primary Inventory Points for them using the option Inventory Point Management in the Accountable Officer Menu. This option allows you to add new Primary Inventory Points and establish control parameters that are similar to site parameters. You can also establish users for each inventory point, and their associated Fund Control Points(s). After setup is complete, the users will be able to enter the Primary Inventory Menu \[PRCP MAIN MENU\], enter the items on their individual inventory files, and establish Secondary Points.

#### FCP Monitor Fields

These fields are not included in the Site Parameters option but are in Site Parameter (#411) file. The fields are populated using FileMan. Refer to the [*DynaMed-IFCAP Implementation Guide*](http://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1p81ig.doc) for more information on the use of these fields.

### Test Account Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the following procedures in the order presented to bring up IFCAP on your test account.

Read Sections 4.1 above and 4.19 above before you begin entering information into a Test Account. The data going into the Test Account should be just enough to give users a “feel” for the system.

After you review the steps involved in loading the IFCAP files, you may consult the Site Manager for insight into the setting up of a Test Account that will be useful for training new users and refreshing current ones.

#### Set Up IFCAP

STEP 1. Follow the steps in 4.19 above to create IFCAP in your Test Account if you are not using a copy of your production system as a test system

#### Production/Training Field 

This field is not included in the Site Parameters option but rather is stored in the Site Parameter (#411) file. This field is populated using *FileMan*. Refer to the [*IFCAP Technical Manual*](http://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1tech_manual.doc), the PRODUCTION/TRAINING Flag, for more information regarding this field.

## The Logistics Data Query Tool 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Logistics Data Query Tool is designed to assist Chief Logistics Officers; Materiel Managers; Purchasing Agents; and members of the Facility Logistics Staff (including Inventory Managers; Supply, Processing, and Distribution (SPD) Technicians; Management Analysts; Warehouse Clerks; or Supply System Analysts). The Query Tool can be used to quickly access, analyze and verify IFCAP and Prosthetics procurement data and display it using a graphical user interface to the VistA data. You can sign-on to VistA, find data, view the data, or easily move the data into a Microsoft® Excel® spreadsheet.

The Query Tool is a Windows software application that acts as a “front-end” to enable you to more easily find, display, and export VistA data. The Query Tool is a substitute for the VA FileMan utility program which has traditionally been used to look directly at the MUMPS globals (files) that store VistA data. The Query Tool enables you to…

- Search for data and display data by a range of dates
- Sort and rearrange the view of the data; display the data in a custom view
- Exporting the data into a Microsoft Excel spreadsheet file

Information on what the Query Tool can do for you can be found in the *Logistics Data Query Tool User Manual*.

The Logistics Data Query Tool User Manual is available online at…

<http://www.va.gov/vdl/application.asp?appid=42>.

*<u>NOTE</u>*: The PRCHL LOGISTICS DATA TOOL \[PRCHL GUI\] option has been marked Out of Order with patch PRC\*5.1\*247.

  

## Resolving Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As the IFCAP Application Coordinator, you may be required to assist users in the resolution of various problems including error messages. This chapter is intended to guide you in some techniques or troubleshooting standards you can employ.

## Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The errors listed in Table 7 are error codes or messages that you or users may encounter when entering delivery orders, purchase orders, or purchase card orders. The errors are listed alphabetically by error code. You or the user can resolve some of the problems, and in other instances IRM staff assistance may be required.

If neither the user nor you can resolve the problem, record the error code and message and immediately report the error to IRM staff.

| Error Code    | Error Message                                                                                   | Reason                                                                                                                                                                                                                                    |
|---------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAUC^\<LIN\>  | No actual unit cost for this ITEM.                                                              | There is no Actual Unit Cost entry for the Line Item Number (\<LIN\>) in the Procurement & Accounting Transactions (#442) file.                                                                                                           |
| NCNO^\<LIN\>  | This order requires a contract number but none was entered for this item.                       | The order is a Direct Order, but there is no contract number entered for this Line Item Number (\<LIN\>) in the Procurement & Accounting Transactions (#442) file.                                                                        |
| NDD           | No delivery date for this P.O. in file 442.                                                     | There is no Delivery Date in the Procurement & Accounting Transactions (#442) file.                                                                                                                                                       |
| NDP0          | No record for direct delivery patient pointer.                                                  | The DIRECT DELIVERY PATIENT entered in the Procurement & Accounting Transactions (#442) file for this purchase order cannot be found in the Direct Delivery Patients (#440.2) file.                                                       |
| NFT0^\<SITE\> | No entry in file 411.2 for facility type pointer from file 411.                                 | There is no entry in the FACILITY TYPE (# 411.2) file for the Facility Type field of the Admin Activity Site Parameter (# 411) file.                                                                                                      |
| NFT^\<SITE\>  | No facility type pointer for site in file 411.                                                  | The Admin. Activity Site Parameter (#411) file has no entry in it.                                                                                                                                                                        |
| NI2N^\<ITEM\> | No contract number for item on this P.O.                                                        | There are no ITEMS listed under the Item multiple in the Procurement & Accounting Transactions (#442) file.                                                                                                                               |
| NMIC          | No mail invoice city in file 411.                                                               | The city listed for MAIL INVOICE could not be found in the Admin. Activity Site Parameter (#411) file.                                                                                                                                    |
| NMIL          | MAIL INVOICE LOCATION information in file 411 missing.                                          | The location for MAIL INVOICE cannot be found in the Admin. Activity Site Parameter (#411) file.                                                                                                                                          |
| NMIS          | No state file pointer in file 411.                                                              | No MAIL INVOICE STATE pointer in the Admin. Activity Site Parameter (#411) file.                                                                                                                                                          |
| NMIZ          | No mail invoice ZIP CODE entry in file 411.                                                     | No MAIL INVOICE ZIP CODE in the Admin. Activity Site Parameter (#411) file.                                                                                                                                                               |
| NOPR          | No PROPOSAL entry in file 442 for this P.O.                                                     | There is no PROPOSAL entry in the Procurement & Accounting Transactions (#442) file.                                                                                                                                                      |
| NOPT          | No patient file entry for direct delivery patient pointer.                                      | There is no entry in the Patient (#2) file matching the Direct Delivery Patient entered for this P.O. in the Procurement & Accounting Transactions (#442) file.                                                                           |
| NP12          | No node 12 in file 442 for this P.O.                                                            | No ELECTRONIC SIGNATURE in the Procurement & Accounting Transactions (#442) file.                                                                                                                                                         |
| NP12          | INVOICE ADDRESS pointer is missing.                                                             | No INVOICE ADDRESS in the Procurement & Accounting Transactions (#442) file.                                                                                                                                                              |
| NPH           | No phone number for this A&MM user in the person file.                                          | The New Person (#200) file does not have a phone number listed for this A&MM user.                                                                                                                                                        |
| NPH           | No phone number for this PPM in the person file.                                                | The New Person (#200) file does not have a phone number listed for this PPM.                                                                                                                                                              |
| NPHN          | No phone number node in the person file for this A&MM user.                                     | The New Person (#200) file does not have a phone number node for this A&MM user.                                                                                                                                                          |
| NPIA          | Invoice address missing.                                                                        | There is no INVOICE ADDRESS in node 12 in the Procurement & Accounting Transactions (#442) file.                                                                                                                                          |
| NPO0          | Zero node of record missing. Unable to check further.                                           | No Procurement & Accounting Transactions (#442) file entry exists.                                                                                                                                                                        |
| NPO1          | Node 1 missing in record.                                                                       | No VENDOR, SHIP TO or ACCOUNTING information found for the Procurement & Accounting Transactions (#442) file record.                                                                                                                      |
| NPOD          | No purchase order date in file 442 for this P.O.                                                | There is no PURCHASE ORDER DATE in the Procurement & Accounting Transactions (#442) file.                                                                                                                                                 |
| NPPM          | No purchasing agent entry in file 442 for this P.O.                                             | There is no Purchasing Agent/PPM Agent entry in the Procurement & Accounting Transactions (#442) file.                                                                                                                                    |
| NPPT          | No prompt payment terms entered in P.O.                                                         | There are no PROMPT PAYMENT TERMS entries in the Procurement & Accounting Transactions (#442) file.                                                                                                                                       |
| NQTY^\<LIN\>  | No quantity listed for this ITEM.                                                               | There is no QUANTITY listed for the Line Item Number (\<LIN\>) in the Procurement & Accounting Transactions (#442) file.                                                                                                                  |
| NRL           | No receiving location node in file 411.                                                         | No RECEIVING LOCATION node in the Admin. Activity Site Parameter (#411) file.                                                                                                                                                             |
| NSC           | No Source Code for type of order for this P.O.                                                  | No SOURCE CODE entry in the Procurement & Accounting Transactions (#442) file.                                                                                                                                                            |
| NSIT          | No site entry in file 442.                                                                      | No SITE entry in the Procurement & Accounting Transactions (#442) file.                                                                                                                                                                   |
| NSP0^\<SITE\> | No SITE information in file 411.                                                                | No FACILITY TYPE pointer in the Admin. Activity Site Parameter (#411) file that matches SITE in the Procurement & Accounting Transactions (#442) file.                                                                                    |
| NST0          | No record in the state file                                                                     | No STATE entry in the State (#5) file for Vendor Address State pointer in Vendor file.                                                                                                                                                    |
| NSTA          | Abbreviation missing in state file entry.                                                       | No Abbreviation in the STATE file.                                                                                                                                                                                                        |
| NSTA          | No Abbreviation in State file.                                                                  | There is no Abbreviation in the STATE file for this state.                                                                                                                                                                                |
| NSTDP         | No State file pointer in Direct Delivery Address in 440.2.                                      | No STATE file pointer in Direct Delivery Address field in Direct Delivery Patients file.                                                                                                                                                  |
| NSTL          | No Ship to pointer to entry in file 441.                                                        | No SHIP TO points to the Admin Activity Site Parameter (#411) file.                                                                                                                                                                       |
| NSTP          | No Vendor Address pointer to the State file.                                                    | No VENDOR ADDRESS State file pointer in the Vendor (#440) file.                                                                                                                                                                           |
| NSTS          | There is no Ship To suffix for receiving location for this EDI P.O.                             | The SHIP TO entry for this purchase order in the Procurement & Accounting Transactions (#442) file cannot be found in the Admin. Activity Site Parameter (#411) file (Ship To Suffix). An EDI purchase order requires the Ship To suffix. |
| NSTT          | No State file pointer in Receiving Location in file 411.                                        | No State File pointer in the Receiving Location multiple in the Admin. Activity Site Parameter (#411) file.                                                                                                                               |
| NUNI^\<LIN\>  | No name entry in unit of purchase file for unit of purchase pointer in ITEM entry in P.O. file. | No Name entry in the Unit of Issue file (file 420.5) for the Unit of Purchase entry for the Line Item Number (\<LIN\>) in the Procurement & Accounting Transactions (#442) file.                                                          |
| NUOP^\<LIN\>  | No unit of purchase pointer for this ITEM.                                                      | No Unit of Purchase pointer entered for the Line Item Number (\<LIN\>) in the Procurement & Accounting Transactions (#442) file.                                                                                                          |
| NUPN^\<LIN\>  | No entry in unit of issue file for unit of purchase pointer in ITEM entry in P.O. file.         | No entry in the Unit of Issue file (file 420.5) for the Unit of Purchase entry for the Line Item Number (\<LIN\>) in the Procurement & Accounting Transactions (#442) file.                                                               |
| NV0           | No vendor record found in vendor file.                                                          | No Vendor (#440) file entry for the Vendor pointer from the Procurement & Accounting Transactions (#442) file.                                                                                                                            |
| NVID          | Missing a vendor ID number for an EDI vendor.                                                   | There is no Vendor ID Number for an EDI Vendor in the Vendor (#440) file.                                                                                                                                                                 |

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="PRC_158_B" class="anchor"></span>*<u>NOTE</u>*: A separate *DynaMed-IFCAP Interface Glossary* is also available for sites using this interface. See [\\vhabayfas1\Public\Dynamed User Documentation](file://vhabayfas1/Public/Dynamed%20User%20Documentation).
| 0-9  |                                                                                                               |
|----------|---------------------------------------------------------------------------------------------------------------|
| Term     | Definition / Discussion                                                                                       |
| 1358 | VA Form 1358, *Estimated Obligation or Change in Obligation*                                                  |
| 2138 | VA Form 90-2138, *Order for Supplies or Services* (first page of a VA Purchase Order)                         |
| 2139 | VA Form 90-2139, *Order for Supplies or Services* (Continuation) (continuation sheet for Form 90-2138)        |
| 2237 | VA Form 90-2237, *Request, Turn-in and Receipt for Property or Services* (used to request goods and services) |
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>A</strong></th>
</tr>
<tr class="odd">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>A&amp;MM</strong></td>
<td><em>See</em> <strong>Acquisition and Materiel Management</strong> (Service)</td>
</tr>
<tr class="even">
<td><strong>AACS</strong></td>
<td>Automated Allotment Control System—Central computer system developed by VHA to disburse funding from VACO to field stations.</td>
</tr>
<tr class="odd">
<td><strong>Accounting Technician</strong></td>
<td>Fiscal employee responsible for obligation and payment of received goods and services.</td>
</tr>
<tr class="even">
<td><strong>Acquisition and Materiel Management (Service) (A&amp;MM)</strong></td>
<td>VA Service that is responsible for contracting and for overseeing the acquisition, storage, and distribution of supplies, services, and equipment used by VA facilities. See OA&amp;L.</td>
</tr>
<tr class="odd">
<td><strong>Activity Code</strong></td>
<td>The last two digits of the AACS number. It is defined by each station.</td>
</tr>
<tr class="even">
<td><strong>ADP Security Officer</strong></td>
<td>The individual at your station that is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing file access.</td>
</tr>
<tr class="odd">
<td><strong>Agent Cashier</strong></td>
<td>The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.</td>
</tr>
<tr class="even">
<td><p><strong>AITC</strong></p>
<p><strong>ALD Code</strong></p></td>
<td><p>Austin Information Technology Center located in Austin, Texas.</p>
<p>Appropriation Limitation Department. A set of Fiscal codes which identifies the appropriation used for funding.</p></td>
</tr>
<tr class="odd">
<td><strong>Allowance table</strong></td>
<td>Reference table in FMS that provides financial information at the level immediately above the AACS, or sub-allowance level.</td>
</tr>
<tr class="even">
<td><strong>Amendment</strong></td>
<td>A document which changes the information contained in a specified Purchase Order. Amendments are processed by the Purchasing &amp; Contracting section of A&amp;MM and obligated by Fiscal Service.</td>
</tr>
<tr class="odd">
<td><strong>AMIS</strong></td>
<td>Automated Management Information System.</td>
</tr>
<tr class="even">
<td><strong>Application Coordinator</strong></td>
<td>The individuals responsible for the implementation, training and troubleshooting of a software package within a service. IFCAP requires there to be an Application Coordinator designated for Fiscal Service, A&amp;MM Service.</td>
</tr>
<tr class="odd">
<td><strong>Approve Requests</strong></td>
<td>The use of an electronic signature by a Control Point Official to approve a 2237, 1358 or another request form and transmit said request to A&amp;MM/Fiscal.</td>
</tr>
<tr class="even">
<td><strong>Approving Official</strong></td>
<td>A user that approves reconciliations to ensure that they are correct and complete.</td>
</tr>
<tr class="odd">
<td><strong>Authorization</strong></td>
<td>Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.</td>
</tr>
<tr class="even">
<td><strong>Authorization Balance</strong></td>
<td>The amount of money remaining that can be authorized against 1358. The service balance minus total authorizations.</td>
</tr>
</tbody>
</table>
| B                    |                                                                                                                                                             |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                     | Definition / Discussion                                                                                                                                     |
| Batch Number         | A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number. |
| Breakout Code        | A set of A&MM codes which identifies a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.). |
| Budget Analyst       | Fiscal employee responsible for distributing and transferring funds.                                                                                        |
| Budget Object Code   | Fiscal accounting element that tells what kind of item or service is being procured. Budget object codes are listed in VA Handbook 4671.2                   |
| Budget Sort Category | Used by Fiscal Service to identify the allocation of funds throughout their facility.                                                                       |
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>C</strong></th>
</tr>
<tr class="odd">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CC</strong></td>
<td>Credit Charge entry identifier used by FMS and CCS for charges paid to Vendor through Credit Card payment process.</td>
</tr>
<tr class="even">
<td><strong>CCS</strong></td>
<td>The Charge Card System. This is the database in Austin that processes credit card information from the external Credit Card Vendor system (currently CitiDirect) and then passes information on to FMS and IFCAP.</td>
</tr>
<tr class="odd">
<td><strong>Ceiling Transactions</strong></td>
<td>Funding distributed from Fiscal Service to IFCAP Control Points for spending. The Budget Analyst initiates these transactions using the Funds Distribution options.</td>
</tr>
<tr class="even">
<td><strong>Chief Logistics Office (CLO)</strong></td>
<td><p>The Chief Logistics Office (CLO) develops and fosters logistics best practices for the Veterans Health Administration. Through the VHA Acquisition Board the CLO develops the annual VHA Acquisition plan that forms the basis for VHA’s acquisition strategy. This strategy seeks to provide high quality health care products and services in the most cost-effective manner. This includes the attainment of socio-economic procurement goals. The CLO also develops and implements a comprehensive plan for the standardization of healthcare supplies and equipment. This includes the development and administration of clinical product user groups.</p>
<p>The CLO is also responsible for developing improvements to supply chain management within VHA. This includes the establishment and monitoring of logistics benchmarking data. The CLO serves as liaison for logistics staff in each of the 21 VISNs.</p>
<p>The head of CLO is the <strong>Chief Prosthetics and Clinical Logistics Officer (CPCLO)</strong>.</p></td>
</tr>
<tr class="odd">
<td><strong>Chief Prosthetics and Clinical Logistics Officer (CPCLO)</strong></td>
<td>The official in charge of the VHA <strong>Chief Logistics Office (CLO)</strong>, also called the Clinical Logistics Office.</td>
</tr>
<tr class="even">
<td><strong>CLA</strong></td>
<td><em>See</em> <strong>Clinical Logistics Analyst</strong></td>
</tr>
<tr class="odd">
<td><strong>Classification of Request</strong></td>
<td>An identifier a Control Point can assign to track requests that fall into a category (<em>e.g.</em>, Memberships, Replacement Parts, Food Group III).</td>
</tr>
<tr class="even">
<td><strong>Clinical Logistics Analyst (CLA)</strong></td>
<td><em>Logistics</em> refers to how resources are acquired, transported and stored along the supply chain. By having an efficient supply chain and proper logistical procedures, an organization can cut costs and increase efficiency. <em>Clinical logistics</em> refers specifically to resources used for clinical purposes. A CLA is a person who examines processes, methods and data for clinical logistics operations.</td>
</tr>
<tr class="odd">
<td><strong>Clinical Logistics Office</strong></td>
<td><em>See</em> <strong>Chief Logistics Office (CLO).</strong></td>
</tr>
<tr class="even">
<td><strong>Clinical Logistics Report Server (CLRS)</strong></td>
<td>The CLRS project allows the extraction of selected procurement and inventory data from VHA facilities to a centralized Clinical Logistics Report Server. The server supports the collection, tracking, and reporting of National Performance Measures, assisting the Under Secretary for Health (USH) in evaluating facility performance in the areas of consolidation of high-tech equipment, standardization, socioeconomic goal accomplishment, acquisition, and inventory management.</td>
</tr>
<tr class="odd">
<td><strong>CLRS</strong></td>
<td><em>See</em> <strong>Clinical Logistics Report Server (CLRS)</strong>.</td>
</tr>
<tr class="even">
<td><strong>Common Numbering Series</strong></td>
<td>This is a pre-set series of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinators establish the Common Numbering Series used by each facility.</td>
</tr>
<tr class="odd">
<td><strong>Control Point</strong></td>
<td>Financial element, existing ONLY in IFCAP, which corresponds to a set of elements in FMS that include the Account Classification Code (ACC) and define the Sub-Allowance on the FMS system. Used to permit the tracking of monies to a specified service, activity or purpose from an Appropriation or Fund.</td>
</tr>
<tr class="even">
<td><strong>Control Point Clerk</strong></td>
<td>The user within the service who is designated to input requests (2237s) and maintain the Control Point records for a Service.</td>
</tr>
<tr class="odd">
<td><strong>Control Point Official</strong></td>
<td>The individual authorized to expend government funds for ordering of supplies and services for their Control Point(s). This person has all the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.</td>
</tr>
<tr class="even">
<td><strong>Control Point Official’s Balance</strong></td>
<td>A running record of all the transactions generated and approved for a Control Point from within IFCAP. Effects changes to the control point that are initiated directly from within the FMS system. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.</td>
</tr>
<tr class="odd">
<td><strong>Control Point Requestor</strong></td>
<td>The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. A user can only view or edit their own request. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&amp;MM.</td>
</tr>
<tr class="even">
<td><strong>Cost Center</strong></td>
<td>Cost Centers are unique numbers which define a service. One cost center must be attached to every Fund Control Point. This enables costs to be captured by service. Cost centers are listed in VA Handbook 4671.1.</td>
</tr>
</tbody>
</table>
| D                           |                                                                                                                                                                             |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                        | Definition / Discussion                                                                                                                                                 |
| Date Committed              | The date that you want IFCAP to commit funds to the purchase.                                                                                                               |
| Default                     | A suggested response that is provided by the system.                                                                                                                        |
| Deficiency                  | When a budget has obligated and expended more than it was funded.                                                                                                           |
| Delinquent Delivery Listing | A listing of all the Purchase Orders that have not had all the items received by the Warehouse on IFCAP. It is used to contact the vendor for updated delivery information. |
| Delivery Order              | An order for an item that the VA purchases through an established contract with a vendor who supplies the items.                                                            |
| Direct Delivery Patient     | A patient who has been designated to have goods delivered directly to him/her from the vendor.                                                                              |
| Discount Item               | This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.                 |
| E                                 |                                                                                                                                                                                                               |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                              | Definition / Discussion                                                                                                                                                                                   |
| eCMS                              | The VA’s electronic Contract Management System hosted at the Austin Information Technology Center in Austin, Texas.                                                                                           |
| EDI                               | *See*Electronic Data Interchange (EDI).                                                                                                                                                                  |
| EDI Vendor                        | A vendor with whom the VA has negotiated an arrangement to submit, accept and fill orders electronically.                                                                                                     |
| EDI X12                           | “X12” is the U.S. standard ANSI ASC X12, which is the predominant standard used in North America. Thus, “EDI X12” refers to electronic data interchanges which meet the X12 standard. Also seen as “X12 EDI.” |
| Electronic Data Interchange (EDI) | Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.                                                                           |
| Electronic Signature              | The electronic signature code replaces the written signature on all IFCAP documents used within your facility. Documents going off station will require a written signature as well.                          |
| Expenditure Request               | A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).                                                                                      |
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>F</strong></th>
</tr>
<tr class="odd">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>FCP</strong></td>
<td>Fund Control Point (see Control Point).</td>
</tr>
<tr class="even">
<td><strong>Federal Tax ID</strong></td>
<td>A unique number that identifies your station to the Internal Revenue Service.</td>
</tr>
<tr class="odd">
<td><strong>FileMan</strong></td>
<td><p>The FileMan modules are the “building blocks” for all of VistA. FileMan includes both a database management system (DBMS) and user interface.</p>
<p><em>Source :</em> <a href="http://www.hardhats.org/fileman/FMmain.html">http://www.hardhats.org/fileman/FMmain.html</a></p></td>
</tr>
<tr class="even">
<td><strong>Fiscal Balance</strong></td>
<td>The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidation submitted against the obligation.</td>
</tr>
<tr class="odd">
<td><strong>Fiscal Quarter</strong></td>
<td>The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.</td>
</tr>
<tr class="even">
<td><strong>Fiscal Year</strong></td>
<td>Twelve-month period from October 1 to September 30.</td>
</tr>
<tr class="odd">
<td><strong>FMS</strong></td>
<td>Financial Management System, the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.</td>
</tr>
<tr class="even">
<td><strong>FOB</strong></td>
<td><strong>Freight on Board.</strong> An FOB of “Destination” means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of “Origin” means the Vendor has paid shipping costs directly to the shipper and then will include them on their Invoice.</td>
</tr>
<tr class="odd">
<td><strong>FPDS</strong></td>
<td>Federal Procurement Data System.</td>
</tr>
<tr class="even">
<td><strong>FTEE</strong></td>
<td>Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned to an FTEE of 0.5, as would a full-time employee that worked for half of a year.</td>
</tr>
<tr class="odd">
<td><strong>Fund Control Point</strong></td>
<td>IFCAP accounting element that is not used by FMS. See also control point.</td>
</tr>
<tr class="even">
<td><strong>Funds Control</strong></td>
<td>A group of Control Point options that allow the Control Point Clerk and/or Official to maintain and reconcile their funds.</td>
</tr>
<tr class="odd">
<td><strong>Funds Distribution</strong></td>
<td>A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>G</strong></th>
</tr>
<tr class="odd">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>GBL</strong></td>
<td>Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of $250.00.</td>
</tr>
<tr class="even">
<td><strong>GL</strong></td>
<td>General Ledger.</td>
</tr>
<tr class="odd">
<td><strong>Globals</strong></td>
<td><p>Globals are variables which are automatically and transparently stored on disk and persist beyond program, routine, or process completion. Globals are used exactly like ordinary variables, but with the caret character prefixed to the variable name.</p>
<p>Globals are stored in highly structured data files by MUMPS and accessed only as MUMPS globals. VistA file definitions and data are both stored in globals.</p></td>
</tr>
</tbody>
</table>
| I                                          |                                                                                                                                                                                                               |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                                       | Definition / Discussion                                                                                                                                                                                   |
| Identification Number                      | A computer-generated number assigned to a code sheet.                                                                                                                                                         |
| Imprest Funds                              | Monies used for cash or 3<sup>rd</sup> party draft purchases at a VA facility.                                                                                                                                |
| Integrated Supply Management System (ISMS) | ISMS is the system which replaced LOG I for Expendable Inventory.                                                                                                                                             |
| ISMS                                       | See Integrated Supply Management System.                                                                                                                                                                      |
| Item File                                  | A listing of items specified by A&MM service as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history. |
| Item History                               | Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.                                                            |
| Item Master Number                         | A computer-generated number used to identify an item in the Item File.                                                                                                                                        |
| J             |                                                                                                                                                                                        |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term          | Definition / Discussion                                                                                                                                                            |
| Justification | A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source. |
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>K</strong></th>
</tr>
<tr class="odd">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Kernel</strong></td>
<td><p>The Kernel is the software “scaffolding” that supports all VistA applications. The Kernel system permits any VistA software application to run without modification to its base structure no matter what hardware or software vendor the application was built on.</p>
<p>The Kernel includes several management tools including device, menu, programming, operations, security/auditing, task, user, and system management. Its framework provides a structurally sound computing environment that permits controlled user access, menus for choosing various computing activities, the ability to schedule tasks, application development tools, and numerous other management and operation tools.</p>
<p><em>Source:</em> <a href="http://hardhats.org/kernel/KRNmain.html">http://hardhats.org/kernel/KRNmain.html</a></p></td>
</tr>
</tbody>
</table>
| L           |                                                                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term        | Definition / Discussion                                                                                                                                        |
| Liquidation | The amount of money posted to the 1358 or Purchase Order as a payment to the vendor. They are processed through payment/invoice tracking.                          |
| LOG I       | LOG I is the name of the Logistics A&MM computer located at the Austin Automation Center. This system continues to support the Consolidated Memorandum of Receipt. |
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>M</strong></th>
</tr>
<tr class="odd">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>M</strong></td>
<td>The Massachusetts General Hospital Utility Multi-Programming System, or alternatively M, is a programming language originally created for use in the healthcare industry. M is designed to make writing database-driven applications easy while simultaneously making efficient use of computing resources. The most outstanding, and unusual, design feature of M is that database interaction is transparently built into the language. Many parts of VistA are written in M.</td>
</tr>
<tr class="even">
<td><strong>MailMan</strong></td>
<td><p>Mailman is an integrated data channel in VistA for the distribution of:</p>
<ul>
<li><p>Patches (<em>Kernel Installation and Distribution System</em> or <em>KIDS</em> builds)</p></li>
<li><p>Software releases (<em>KIDS</em> builds)</p></li>
<li><p>Computer-to-computer communications (HL7 transfers, Servers, etc.)</p></li>
<li><p>Person-to-person messaging (email)</p></li>
</ul>
<p><em>Source :</em> <a href="http://www.hardhats.org/cs/mailman/MMmain.html">http://www.hardhats.org/cs/mailman/MMmain.html</a></p></td>
</tr>
<tr class="odd">
<td><strong>Mandatory Source</strong></td>
<td>A Federal Agency that sells supplies and services to the VA, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.</td>
</tr>
<tr class="even">
<td><strong>MSC Confirmation Message</strong></td>
<td>A MailMan message generated by the Austin Message Switching Center that assigns an FMS number to an IFCAP transmission of documents.</td>
</tr>
<tr class="odd">
<td><strong>MUMPS</strong></td>
<td><em>See</em> <strong>M.</strong></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>O</strong></th>
</tr>
<tr class="odd">
<th><strong>Term</strong></th>
<th><strong>Definition / Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="PRC_153B" class="anchor"></span><strong>OA&amp;L</strong></p>
<p><strong>Obligation</strong></p></td>
<td><p>Office of Acquisitions &amp; Logistics. {Formerly A&amp;MM).</p>
<p>The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of an Order.</p></td>
</tr>
<tr class="even">
<td><strong>Obligation (Actual) Amount</strong></td>
<td>The actual dollar figure that’s obligated by Fiscal Service for a Purchase Order. The Control Point’s records are updated with actual cost automatically when Fiscal obligates the document on IFCAP.</td>
</tr>
<tr class="odd">
<td><strong>Obligation Number</strong></td>
<td>The 6-character number assigned to orders, requisitions and 1358s. (i.e. C prefix number that Fiscal Service assigns to the 1358.)</td>
</tr>
<tr class="even">
<td><strong>OLCS</strong></td>
<td>On-Line Certification System that’s located at the Austin Information Technology Center.</td>
</tr>
<tr class="odd">
<td><strong>Option</strong></td>
<td>A VistA Option is an application component defined in VA Kernel to control user and remote server access to VistA applications. Options can appear on menu “trees” of options, through which the user navigates to execute application software. Types of options include menu (to allow grouping of options); edit (to edit application files via VA FileMan); inquire (to query the database via VA FileMan); print (to execute reports via VA FileMan); run routine (to execute custom application software); server (to process remote procedure calls via MailMan); and Broker (to process GUI remote procedure calls via Kernel Broker).</td>
</tr>
<tr class="even">
<td><strong>Organization Code</strong></td>
<td>Accounting element functionally comparable to Cost Center but used to organize purchases by the budget that funded them, not the purposes for spending the funds.</td>
</tr>
<tr class="odd">
<td><strong>Outstanding 2237</strong></td>
<td>A&amp;MM report that lists all the IFCAP generated 2237s pending action in A&amp;MM.</td>
</tr>
</tbody>
</table>
| P                             |                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                          | Definition / Discussion                                                                                                                                                                                                                                                                                                                                            |
| Partial                       | A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.                                                                                                                                                                                                                                                   |
| Partial Date                  | The date that a warehouse clerk created a receiving report for a shipment.                                                                                                                                                                                                                                                                                             |
| PAT Number                    | Pending Accounting Transaction number – the primary FMS reference number. See also Obligation Number.                                                                                                                                                                                                                                                                  |
| Personal Property Management  | A section of A&MM Service that’s responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support. |
| POA                           | Purchase Order Acknowledgment. The message that’s received electronically from an EDI vendor acknowledging the placement of an order.                                                                                                                                                                                                                                  |
| PPM                           | Personal Property Management, now referred to at most sites as Acquisition and Materiel Management Service.                                                                                                                                                                                                                                                            |
| Program Code                  | Accounting element that identifies the VA initiative or program that the purchase will support.                                                                                                                                                                                                                                                                        |
| Prompt Payment Terms          | The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).                                                                                                                                                   |
| Purchase Card                 | A card, like a credit card that Purchase Card Users use to make purchases. Purchase Cards are not credit cards but debit cards that spend money out of a deposited balance of VA funds.                                                                                                                                                                                |
| Purchase Card Coordinator     | A person authorized by a VA station to monitor and resolve delinquent purchase card orders, help VA services record, edit and approve purchase card orders in a timely manner, assign purchase cards to IFCAP users, and monitor the purchase card expenses of VAMC services.                                                                                          |
| Purchase Card Orders          | Orders funded by a purchase card.                                                                                                                                                                                                                                                                                                                                      |
| Purchase Card User            | A person who uses a purchase card. Purchase Card Users are responsible for recording their purchase card orders in IFCAP.                                                                                                                                                                                                                                              |
| Purchase History Add (PHA)    | Information about purchase orders which are automatically sent to Austin for archiving. This same transaction is also used to send a PO for EDI processing.                                                                                                                                                                                                            |
| Purchase History Modify (PHM) | Information about amendments which is automatically sent to Austin for archiving.                                                                                                                                                                                                                                                                                      |
| Purchase Order                | A government document authorizing the purchase of the goods or services at the terms indicated.                                                                                                                                                                                                                                                                        |
| Purchase Order Acknowledgment | Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).                                                                                                                                                                                                                                                 |
| Purchase Order Status         | The status of completion of a purchase order (e.g., Pending Contracting Officer’s Signature, Pending Fiscal Action, Partial Order Received, etc.).                                                                                                                                                                                                                     |
| Purchasing Agents             | A&MM employees who are legally empowered to create purchase orders to obtain goods and services from commercial vendors.                                                                                                                                                                                                                                               |
| Q                 |                                                                                                                                                                                    |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term              | Definition / Discussion                                                                                                                                                        |
| Quarterly Report  | A Control Point listing of all transactions (Ceilings, Obligations, and Adjustments) made against a Control Point’s Funds.                                                         |
| Quotation for Bid | Standard Form 18. Used by Purchasing Agents to obtain written bids from vendors. May be created automatically and transmitted electronically within the Purchasing Agent’s module. |
| R                           |                                                                                                                                                                                                                                                                                                             |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                        | Definition / Discussion                                                                                                                                                                                                                                                                                 |
| Receiving Report            | The VA document used to indicate the quantity and dollar value of the goods being received.                                                                                                                                                                                                                 |
| Reconciliation              | The comparing of two records to validate IFCAP Purchase Card orders. Purchase Card Users compare IFCAP generated purchase card order data with the CC transaction sent from the CCS system in Austin.                                                                                                       |
| Reference Number            | Also known as the Transaction Number. The computer-generated number that identifies a request. It is comprised of the: Station Number-Fiscal Year-Quarter - Control Point – 4-digit Sequence Number.                                                                                                        |
| Repetitive (PR Card) Number | See Item Master Number.                                                                                                                                                                                                                                                                                 |
| Repetitive Item List (RIL)  | A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate 2237 requests from the list. A RIL can be created by using the Auto-Generate feature within the Inventory portion of the package. |
| Requestor                   | See Control Point Requestor.                                                                                                                                                                                                                                                                            |
| Requisition                 | An order from a government vendor.                                                                                                                                                                                                                                                                          |
| Running Balance             | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.                                                                              |
| S                 |                                                                                                                                                                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term              | Definition / Discussion                                                                                                                                                                                                                                                                           |
| Section Request   | A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.                                                                                                                              |
| Service Balance   | The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorization created by the service.                                                                                        |
| SF-18             | Request for Quotation.                                                                                                                                                                                                                                                                                |
| SF-30             | Amendment of Solicitation/Modification of Contract.                                                                                                                                                                                                                                                   |
| Short Description | A phrase which describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).                                                                                             |
| Site Parameters   | Information (such as Station Number, Cashier’s address, printer location, etc.) that is unique to your station. All IFCAP uses a single Site Parameter file.                                                                                                                                          |
| Sort Group        | An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.                                                                                                                                                 |
| Sort Order        | The order in which the budget categories will appear on the budget distribution reports.                                                                                                                                                                                                              |
| Special Remarks   | A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.                                                                                                                         |
| Stacked Documents | The purchase orders, receiving reports, and 1358s which are sent electronically to Fiscal and stored in a file for printing later rather than being printed immediately.                                                                                                                              |
| Status of Funds   | Fiscal’s on-line status report of the monies available to a Control Point. FMS updates this information automatically.                                                                                                                                                                                |
| Sub-control Point | A user defined assignment of all or part of a ceiling transaction to a specific category (sub-control point) within a Control Point, Transactions can then be posted against this sub-control point and a report can be generated to track use of specified funding within the overall control point. |
| Sub-cost Center   | A subcategory of Cost Center. IFCAP will not utilize a ‘sub-cost center’ field but will send FMS the last two digits of the cost center as the FMS “sub-cost center” field.                                                                                                                           |
| T                                |                                                                                                                                                                                          |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                             | Definition / Discussion                                                                                                                                                              |
| Tasked Job                       | A job, usually a printout that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.                              |
| TDA                              | See “Transfer of Disbursing Authority.”                                                                                                                                                  |
| Total Authorizations             | The total amount of the authorizations created for the 1358 obligation.                                                                                                                  |
| Total Liquidations               | The total amount of the liquidation against the 1358 obligation.                                                                                                                         |
| Transaction Number               | The number of the transaction that funds a Control Point (See Budget Analyst User’s Guide). It consists of the Station Number – Fiscal Year – Quarter – Control Point – Sequence Number. |
| Transfer of Disbursing Authority | The method that’s used to allocate funds to a VA facility.                                                                                                                               |
| Transmission Number              | A sequential number given to a data string when it is transmitted to the Austin DPC; used for tracking message traffic.                                                                  |
| Type Code                        | A set of A&MM codes that provides information concerning the vendor’s size and type of competition sought on a purchase order.                                                           |
| U                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term                   | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Unit of Issue          | A description of the quantity/packaging combination in which the item is issued to the end user; it may be different from the Unit of Purchase, which is the combination used when the item is procured from the vendor. For example, a vendor may sell an item in cases of 24 cans, but the end user receives individual cans from that case.                                                                                                                                                  |
| Unit of Purchase       | A description of the quantity/packaging combination in which VA purchases the item from the vendor; it may be different from the Unit of Issue, which is the combination used to issue the item to the end user. See also Unit Conversion Factor.                                                                                                                                                                                                                                               |
| Unit Conversion Factor | A number which expresses the ratio between the unit of measure and the unit of issue. Among other things, the conversion factor (which is part of the vendor data) is used at order release to calculate the due-ins and due-outs. Supply stations receive the conversion factor at the time of order release and use it to translate the order quantities into supply station amounts. If an item is procured, stocked and issued using the same units, then the conversion factor would be 1. |
| V                |                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term             | Definition / Discussion                                                                                                                                                                                                                                                                                                                                                                                      |
| Vendor file      | An IFCAP file of vendor information solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. The debtor’s address may be drawn from this file but is maintained separately. If the desired vendor is not in the file, contact A&MM Service to have it added.                                                                  |
| Vendor ID Number | The ID number assigned to a vendor by the FMS Vendor unit.                                                                                                                                                                                                                                                                                                                                                       |
| VRQ              | FMS Vendor Request document. When a new vendor is added to IFCAP a VRQ message is sent electronically to the Austin FMS Vendor unit to determine if the vendor exists in the central vendor system. If the vendor is not in the system, Austin will confirm information and establish the vendor in the central file. If vendor exists in central file already, Austin will verify the data. *See also*VUP. |
| VUP              | Vendor Update Message. This message is sent electronically from the FMS system to ALL IFCAP sites to ensure that the local vendor file contains the same data as the central vendor file in Austin. This message will contain the FMS Vendor ID for the vendor and the Alternate Address Indicator if applicable. *See also*VRQ.                                                                            |
| X       |                             |
|-------------|-----------------------------|
| Term    | Definition / Discussion |
| X12 EDI | *See*EDI X12.          |

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<Alt\>, 3
1358, 29, 35, 38
2138, 29
2139, 29
2237, 8, 29
A&MM, 20, 25, 35
Accounting Technician, 5, 19, 20, 22, 35
Add/Edit Supply Personnel, 22, 38
Approve Requests, 16
Barcode Manager Menu, 21, 39, 40
Budget Analyst, 19, 22, 64
Ceiling Transactions, 16
click, 2
Clinical Logistics Analysts (CLAs), 43, 46
Clinical Logistics Office, 43, 69
Clinical Logistics Office Menu, 43, 69
Clinical Logistics Report Server, 46
Clinical Logistics Report Server (CLRS), 43
CLO GIP Reports (CLRS), 45
CLO Procurement Reports (CLRS), 46
CLO System Parameters (CLRS), 44, 47
CLRS REPORT STORAGE file (#446.7), 45
Compliance Reports (1358), 54
Control Point, 5, 7, 8, 16, 18, 20, 22, 25, 29, 40, 63, 64, 65, 67
Cost Center, 64
Days of Stock on Hand Report, 45
documents
available, 2
EDI Vendor Edit, 35
Electronic Signature, 22
Fiscal Year, 35, 37
FMS, 40
FMS Exception Transaction Report, 40, 41
Fund Control Point, 64, 65, 67
hyperlink
internal, 2
hyperlinks, 2
icon
Information, 4
Technical Note, 4
Tip, 4, 16, 23, 38, 45, 47, 48
Warnings, 4
icons
for boxed notes, 4
IFCAP, 4
Invoice Certification, 55
Invoices, 27, 37, 72
ISMS, 13, 17
Manual, 4
New Purchase Order, 36, 38, 65
OLCS, 87
operating system, 2
PAT Status Report, 41
Purchase Order, 8, 13, 22, 26, 27, 29, 35, 36, 38, 64, 65, 66, 71, 73, 74
Purchasing Agents, 13, 22, 35, 36, 38
Quarterly Report, 41
Query Tool, 4
Receiving Report, 8, 29
Receiving reports, 29
Reconciliations, 40
Requestor, 18
Requisition, 64
Separation of Duties Violations, 54
Site Parameters, 9, 15, 26, 67
Stock Status Report, 45
System Access, 15
Troubleshooting, 9
Unposted Dietetic Cost Report, 61
Vendor file, 26, 66, 75
Vendor File Edit, 65
[^1]: The only current exception to this rule relates to use of the *Logistics Data Query Tool*. Designated users of this tool can gain read-only access to data without going through a visible menu—although such users must have what’s called a “B-type” menu option assigned. See Table 5 for details.
