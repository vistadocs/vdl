---
title: IFCAP Version 5.1 Generic Inventory User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Generic Inventory User's Guide
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
menu_options: 0
description: > This option will automatically generate a Primary or Supply Warehouse Inventory Point repetitive item list or a Secondary Inventory Point Distribution Order. The auto-generation will use the selected group categories and those vendors (stored in the mandatory or suggested source ﬁeld in the Primar
audience: 
keywords: 
  - blockquote
  - class
  - style
  - width
  - table
  - strong
  - colspan
  - contents
  - report
  - even
page_count: 0
word_count: 34109
section_count: 62
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1gip.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1gip.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

> Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP)

> Version 5.1

Generic Inventory User’s Guide

![](ifcap-version-5-1-generic-inventory-user-s-guide/001.png)

> November 2025

> Department of Veterans Affairs

> Office of Information and Technology (OI&T) Management, Enrollment, and Financial Systems

> Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 43%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revision</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>October 2025</p>
</blockquote></td>
<td><blockquote>
<p>PRC*5.1*244</p>
</blockquote></td>
<td><blockquote>
<p>Addition of ABC Classification to screenshots within Select Whse Item, Inventory point data and within the document Glossary</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>September 2025</p>
</blockquote></td>
<td><blockquote>
<p>PRC*5.1*247</p>
</blockquote></td>
<td><blockquote>
<p>The PRCHL GUI Logistics Data Query Tool option has been marked Out of Order.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>October 2011</p>
</blockquote></td>
<td><blockquote>
<p>6.0</p>
</blockquote></td>
<td><blockquote>
<p>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358. See page <a href="#chapter-12.-glossary">11-1.</a></p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>06/07/2011</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
<td><blockquote>
<p>Patch PRC*5.1*142 - Print Transaction</p>
<p>Register – p. <a href="#report-parameters-8">7-55</a></p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>05/31/2007</p>
</blockquote></td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
<td><blockquote>
<p>Added information covering the use of the Logistics Data Query Tool (LDQT), per patch PRC*5.1*103;</p>
<p>general update.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/00/2007</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
<td><blockquote>
<p>Revised to include GIP On-Demand functionality for patch PRC*5.1*98 and National Documentation</p>
<p>Standards</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED REDACTED REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12/29/2004</p>
</blockquote></td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td><blockquote>
<p>PDF file checked for accessibility to</p>
<p>readers with disabilities</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12/29/2004</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Updated to comply with SOP 192- 352 Displaying Sensitive Data</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Preface

> This manual explains how to use the options in the Warehouse--General Inventory/Distribution Menu of the Integrated Funds Distribution, Control Point Monitoring, Accounting and Procurement (IFCAP) system. The Warehouse--General Inventory/Distribution Menu auto generates purchase orders for warehouse stock below stock thresholds, allows warehouse clerks to enter barcode inventory data into IFCAP, manage inventory records, and manage the supply and distribution of goods from the warehouse to the services the warehouse supports.

> THIS PAGE INTENTIONALLY LEFT BLANK

[Chapter 1. Introduction to the Generic Inventory Package 1-2](#chapter-1.-introduction-to-the-generic-inventory-package)

1.  
2.  
3.  

[The General Inventory System 1-2](#the-general-inventory-system)[Package Management 1-3](#package-management)[Package Operation 1-4](#package-operation)[Chapter 2. Auto-Generate Orders 2-1](#chapter-2.-auto-generate-orders)

1.  
2.  
3.  
4.  
5.  
6.  

[Introduction 2-1](#introduction)[Select Fiscal Year 2-1](#select-fiscal-year)[Select Group Category 2-2](#select-group-category)[Start Auto-Generation 2-4](#start-auto-generation)[Print Report 2-4](#print-report)[Report Display 2-7](#report-display)[Chapter 3. Barcode Manager Menu 3-1](#chapter-3.-barcode-manager-menu)

1.  1.  
    2.  
2.  1.  
    2.  
    3.  
3.  1.  
    2.  
4.  1.  
    2.  
    3.  
    4.  
    5.  

[Barcode User Menu 3-1](#barcode-user-menu)[Download Barcode Program 3-1](#download-barcode-program)[Upload Barcode Data 3-4](#upload-barcode-data)[Data Manager Menu 3-6](#data-manager-menu)[Enter/Edit/View 3-6](#entereditview)[Schedule Data to Process 3-10](#schedule-data-to-process)[Status of Data 3-13](#status-of-data)[Labels Menu 3-14](#labels-menu)[Inquire Label 3-14](#inquire-label)[Print Labels 3-17](#print-labels)[Programmer (Barcode) Menu 3-18](#programmer-barcode-menu)[Comment Alignment 3-18](#comment-alignment)[Design Label 3-21](#design-label)[Parameter Enter/Edit 3-29](#parameter-enteredit)[Program Enter/Edit 3-34](#program-enteredit)[Specialty Commands Enter/Edit 3-36](#specialty-commands-enteredit)[Chapter 4. Inventory File Maintenance Menu 4-1](#chapter-4.-inventory-file-maintenance-menu)

1.  1.  
    2.  
    3.  
2.  1.  
    2.  
    3.  
    4.  
    5.  
3.  1.  
    2.  

[Adjust Inventory Quantity Menu 4-1](#adjust-inventory-quantity-menu)[Issue Book Adjustment 4-3](#issue-book-adjustment)[Physical Count Form 4-12](#physical-count-form)[Unapproved Adjustment Report 4-16](#unapproved-adjustment-report)[Automatic Level Setter 4-19](#automatic-level-setter)[Level Parameters 4-19](#level-parameters)[Levels Set 4-21](#levels-set)[Update 4-22](#update)[Enter/Edit Inventory Item Data 4-24](#enteredit-inventory-item-data)[Item Selection 4-24](#item-selection)[File Inquiry 4-29](#file-inquiry)[File Review 4-29](#file-review)[Select Item 4-31](#select-item)[Chapter 5. Manager for Supply Warehouse Inventory Point Menu 5-1](#chapter-5.-manager-for-supply-warehouse-inventory-point-menu)

1.  1.  
2.  1.  
3.  1.  
4.  1.  
5.  1.  
6.  1.  
7.  1.  
8.  1.  
9.  1.  
    2.  
    3.  
    4.  
10. 1.  
11. 1.  
12. 1.  

[Balance Update Transaction (IM-6) 5-1](#balance-update-transaction-im-6)[Select Item 5-2](#select-item-1)[Clean Up Old Transactions and Due-Outs 5-3](#clean-up-old-transactions-and-due-outs)[Enter Date 5-5](#enter-date)[Date Received Delete (for Issue Book Requests) 5-6](#date-received-delete-for-issue-book-requests)[Enter Transaction Number 5-7](#enter-transaction-number)[Distribution Costs Enter/Edit 5-8](#distribution-costs-enteredit)[Enter Electronic Signature 5-9](#enter-electronic-signature)[Enter/Edit Inventory and Distribution Points 5-11](#enteredit-inventory-and-distribution-points)[Select Inventory Point 5-12](#select-inventory-point)[FMS Code Sheets Rebuild/Retransmit 5-13](#fms-code-sheets-rebuildretransmit)[Enter FMS Document Code 5-14](#enter-fms-document-code)[Group Category Enter/Edit 5-16](#group-category-enteredit)[Enter Group Category 5-17](#enter-group-category)[Inventory Control Parameters Print 5-18](#inventory-control-parameters-print)[Select Distribution Point 5-19](#select-distribution-point)[Purge History Files Menu 5-20](#purge-history-files-menu)[History By Cost Center Purge 5-20](#history-by-cost-center-purge)[Receipts History By Item Purge 5-23](#receipts-history-by-item-purge)[Transaction Register Purge 5-25](#transaction-register-purge)[Usage/Distribution Monthly Totals Purge 5-27](#usagedistribution-monthly-totals-purge)[Reprint Posted Picking Ticket 5-29](#reprint-posted-picking-ticket)[Transaction Register Type 5-30](#transaction-register-type)[Storage Location Enter/Edit 5-33](#storage-location-enteredit)[Select Storage Location 5-34](#select-storage-location)[Update Calculated Due-Ins/Outstanding Transaction 5-34](#update-calculated-due-insoutstanding-transaction)[Enter Start Date 5-35](#enter-start-date)[Chapter 6. Receiving and Distribution Menu 6-1](#chapter-6.-receiving-and-distribution-menu)

1.  1.  
    2.  
    3.  
2.  1.  
3.  1.  
4.  1.  
    2.  
5.  1.  
6.  1.  
7.  1.  
8.  1.  
9.  1.  
10. 1.  
11. 1.  
    2.  
    3.  

[On Demand Items 6-1](#on-demand-items)[Display Item 6-1](#display-item)[Enter Distribution Point 6-2](#enter-distribution-point)[Display Item Report 6-3](#display-item-report)[Display Where An Item Is Stocked 6-4](#display-where-an-item-is-stocked)[Select Item 6-5](#select-item-2)[Due-In Item Report 6-6](#due-in-item-report)[Enter National Stock Number 6-7](#enter-national-stock-number)[Enter/Edit Items On Distribution Point 6-9](#enteredit-items-on-distribution-point)[Enter Distribution Point 6-9](#enter-distribution-point-1)[Item Information 6-10](#item-information)[Items Flagged 'Kill When Zero' Report 6-11](#items-flagged-kill-when-zero-report)[Report Parameters 6-12](#report-parameters)[Order Form 6-13](#order-form)[Order Form Listing 6-15](#order-form-listing)[Outstanding (Due-Outs) Transaction Listing 6-17](#outstanding-due-outs-transaction-listing)[Report 6-18](#report)[Packaging/Procurement Source Discrepancy Report 6-20](#packagingprocurement-source-discrepancy-report)[Report 6-20](#report-1)[Post Issue Book Order 6-21](#post-issue-book-order)[Report 6-22](#report-2)[Print Item On Distribution Inventory Point 6-25](#print-item-on-distribution-inventory-point)[Print Report 6-25](#print-report-1)[Purchase Order Receiving To Inventory Point 6-26](#purchase-order-receiving-to-inventory-point)[Enter Electronic Signature 6-27](#enter-electronic-signature-1)[Display Receipt 6-28](#display-receipt)[Receipt Confirmation 6-29](#receipt-confirmation)[Chapter 7. Reports Menu 7-1](#chapter-7.-reports-menu)

1.  1.  
2.  1.  
3.  1.  
4.  1.  
    2.  
5.  1.  
6.  1.  
    2.  
7.  1.  
    2.  
8.  1.  
9.  1.  
    2.  
    3.  
    4.  
    5.  
    6.  
10. 1.  
    2.  
    3.  
11. 1.  
12. 1.  
13. 1.  
    2.  
14. 1.  
15. 1.  
    2.  
16. 1.  
17. 1.  

[Adjustment Voucher Recap 7-1](#adjustment-voucher-recap)[Print Report 7-2](#print-report-2)[Availability Listing 7-4](#availability-listing)[Listing 7-5](#listing)[Cost Trend Analysis Report 7-8](#cost-trend-analysis-report)[Long Report 7-9](#long-report)[Days Of Stock On Hand Report 7-12](#days-of-stock-on-hand-report)[Report Parameters 7-13](#report-parameters-1)[Report 7-14](#report-3)[Emergency Stock Report 7-15](#emergency-stock-report)[Report Parameters 7-16](#report-parameters-2)[Graph Usage 7-17](#graph-usage)[Select Item 7-19](#select-item-3)[Chart 7-19](#chart)[History of Distribution Report 7-20](#history-of-distribution-report)[Report Parameters 7-22](#report-parameters-3)[Report Display 7-22](#report-display-1)[Inactive Items Report 7-24](#inactive-items-report)[Report Parameters 7-24](#report-parameters-4)[Informational Reports Menu 7-25](#informational-reports-menu)[Abbreviated Item Report 7-26](#abbreviated-item-report)[Comprehensive Item Report 7-28](#comprehensive-item-report)[Conversion Factor Report 7-31](#conversion-factor-report)[Last Procurement Source For Item Report 7-34](#last-procurement-source-for-item-report)[Non-Issuable Stock Report 7-36](#non-issuable-stock-report)[Substitute Listing Report 7-39](#substitute-listing-report)[Inventory Sales Report 7-41](#inventory-sales-report)[Report Parameters 7-42](#report-parameters-5)[The Summary Report 7-43](#the-summary-report)[The Comprehensive Report 7-43](#the-comprehensive-report)[Quantity Distribution Report 7-46](#quantity-distribution-report)[Report Parameters 7-47](#report-parameters-6)[Stock Status Report 7-48](#stock-status-report)[Report Parameters 7-49](#report-parameters-7)[Transaction Register Report 7-51](#transaction-register-report)[Report Parameters 7-52](#report-parameters-8)[Report 7-53](#report-4)[Unit Costing Report 7-54](#unit-costing-report)[Report 7-55](#report-5)[Usage Demand Analysis Report 7-56](#usage-demand-analysis-report)[Report Parameters 7-57](#report-parameters-9)[Report 7-58](#report-6)[Usage Demand Item Report 7-58](#usage-demand-item-report)[Report Parameters 7-59](#report-parameters-10)[Voucher Summary Report 7-61](#voucher-summary-report)[Report Parameters 7-62](#report-parameters-11)[Chapter 8. Menu Outline 8-1](#chapter-8.-menu-outline)

[Chapter 9. On-Demand Items (ODI) 9-1](#chapter-9.-on-demand-items-odi)

1.  
2.  1.  
3.  1.  
    2.  
4.  1.  
    2.  
    3.  
    4.  
    5.  
    6.  
    7.  
    8.  
    9.  
    10. 
    11. 
    12. 
    13. 
    14. 
5.  1.  
    2.  

#### Tables

> [Table 1-1 GIP Options and Related Descriptions 1-4](#_bookmark4)

#### Figures

> [Figure 2-1 Select Fiscal Year Example 2-3](#_bookmark9)

> [Figure 2-2 Select Group Category Example 2-3](#_bookmark10)

> [Figure 2-3Start Auto-Generation Example 2-4](#_bookmark13)

> [Figure 2-4 Auto-Generation Report Example – Part 1 2-5](#_bookmark14)

> [Figure 2-5 Auto-Generation Report Example – Part 2 2-6](#_bookmark15)

> [Figure 2-6 Auto-Generation Error Report 2-7](#_bookmark17)

> [Figure 3-1 Menu Option Path Example 3-1](#_bookmark21)

> [Figure 3-2 Barcode User Menu Example 3-1](#_bookmark22)

> [Figure 3-3 Barcode Program Entry Example 3-3](#_bookmark23)

> [Figure 3-4 Download Complete Message Example 3-4](#_bookmark24)

> [Figure 3-5 Menu Option Path Example 3-5](#_bookmark26)

> [Figure 3-6 Update Barcode Data Selected Example 3-5](#_bookmark27)

> [Figure 3-7 Menu Option Path Example 3-6](#_bookmark30)

> [Figure 3-8 Menu Option Path Example 3-6](#_bookmark31)

> [Figure 3-9 Date and Time of Data Upload Screen Example 3-8](#_bookmark32)

> [Figure 3-10 Barcode Data Entry Screen Example 3-9](#_bookmark33)

> [Figure 3-11 Menu Option Path Example 3-10](#_bookmark35)

> [Figure 3-12 Schedule Data to Process from the Data Manager Menu Example 3-10](#_bookmark36)

> [Figure 3-13 Setup Data Screen Example 3-11](#_bookmark37)

> [Figure 3-14 Status Screen Example 3-11](#_bookmark38)

> [Figure 3-15 Menu Option Path Example 3-13](#_bookmark40)

> [Figure 3-16 Date and Time of Data Upload Screen Example 3-14](#_bookmark41)

> [Figure 3-17 Menu Option Path Example 3-15](#_bookmark44)

> [Figure 3-18 Label Name Entry Screen Example 3-15](#_bookmark45)

> [Figure 3-19 Menu Option Path Example 3-17](#_bookmark47)

> [Figure 3-20 Custom Label Selection Screen Example 3-17](#_bookmark48)

> [Figure 3-21 Menu Option Path Example 3-19](#_bookmark51)

> [Figure 3-22 Select Barcode Program Name Example 3-20](#_bookmark52)

> [Figure 3-23 Menu Option Path Example 3-21](#_bookmark54)

> [Figure 3-24 Editing an Existing Label Screen Example 3-22](#_bookmark55)

> [Figure 3-25 Special Routine Speciﬁed Screen Example 3-26](#_bookmark57)

> [Figure 3-26 Parameter Description Screen Example 3-27](#_bookmark58)

> [Figure 3-27 Executable Code Screen Example 3-28](#_bookmark59)

> [Figure 3-28 Menu Option Path Example 3-29](#_bookmark61)

> [Figure 3-29 Barcode Program Name Screen Example 3-30](#_bookmark62)

> [Figure 3-30 Upload Attempt Example 3-32](#_bookmark63)

> [Figure 3-31 Device Screen Example 3-32](#_bookmark64)

> [Figure 3-32 Menu Option Path Example 3-34](#_bookmark66)

> [Figure 3-33 Barcode Program Name Screen Example 3-35](#_bookmark67)

> [Figure 3-34 Menu Option Path Example 3-36](#_bookmark69)

> [Figure 3-35 Barcode Program Creation Screen Example 3-38](#_bookmark70)

> [Figure 3-36 Editing a Barcode Program Screen Example 3-39](#_bookmark72)

> [Figure 4-1 Menu Option Path Example 4-1](#_bookmark75)

> [Figure 4-2 Select Issue Book Adjustment Screen Example 4-3](#_bookmark77)

> [Figure 4-3 Data Adjustment Entry Screen Example 4-5](#_bookmark78)

> [Figure 4-4 Select Type of Adjustment Screen Example 4-6](#_bookmark79)

> [Figure 4-5 Enter Adjustment Data Screen Example 4-7](#_bookmark80)

> [Figure 4-6 Other Adjustments Screen Example 4-8](#_bookmark81)

> [Figure 4-7 Enter Adjustment Data Screen Example 4-9](#_bookmark82)

> [Figure 4-8 Menu Option Path Example 4-10](#_bookmark83)

> [Figure 4-9 Adjustment Number Screen Example 4-11](#_bookmark84)

> [Figure 4-10 Menu Option Path Example 4-12](#_bookmark86)

> [Figure 4-11 Select Access Code Screen Example 4-13](#_bookmark87)

> [Figure 4-12 Physical Count Form Report Screen Example 4-15](#_bookmark88)

> [Figure 4-13 Menu Option Path Example 4-16](#_bookmark90)

> [Figure 4-14 Adjustment Number Screen Example 4-17](#_bookmark91)

> [Figure 4-15 Adjustment Approval Form Screen Example 4-18](#_bookmark92)

> [Figure 4-16 Menu Option Path Example 4-19](#_bookmark94)

> [Figure 4-17 Automatic Level Setter Screen Example 4-19](#_bookmark96)

> [Figure 4-18 Levels Set Screen Example 4-21](#_bookmark98)

> [Figure 4-19 Update Levels Database Screen Example 4-22](#_bookmark100)

> [Figure 4-20 Menu Option Path Example 4-24](#_bookmark102)

> [Figure 4-21 Item Selection Screen Example 4-26](#_bookmark104)

> [Figure 4-22 Menu Option Path Example 4-29](#_bookmark106)

> [Figure 4-23 File Review Screen Example 4-29](#_bookmark108)

> [Figure 4-24 Select Warehouse Item Screen Example 4-31](#_bookmark110)

> [Figure 5-1 Menu Option Path Example 5-1](#_bookmark113)

> [Figure 5-2 Select Item Screen Example 5-2](#_bookmark115)

> [Figure 5-3 Menu Option Path Example 5-3](#_bookmark117)

> [Figure 5-4 Finalize Transactions and Update Due-Outs Screen Example 5-5](#_bookmark119)

> [Figure 5-5 Menu Option Path Example 5-6](#_bookmark121)

> [Figure 5-6 Enter Transaction Number Screen Example 5-7](#_bookmark123)

> [Figure 5-7 Menu Option Path Example 5-8](#_bookmark125)

> [Figure 5-8 Enter Electronic Signature Screen Example 5-9](#_bookmark127)

> [Figure 5-9 Menu Option Path Example 5-11](#_bookmark129)

> [Figure 5-10 Select Inventory Point Screen Example 5-12](#_bookmark131)

> [Figure 5-11 Menu Option Path Example 5-13](#_bookmark133)

> [Figure 5-12 Enter MS Document code Screen Example 5-15](#_bookmark135)

> [Figure 5-13 Menu Option Path Example 5-16](#_bookmark137)

> [Figure 5-14 Menu Option Path Example 5-18](#_bookmark140)

> [Figure 5-15 Select Distribution Point Screen Example 5-19](#_bookmark142)

> [Figure 5-16 Menu Option Path Example 5-20](#_bookmark145)

> [Figure 5-17 Purge Distribution History Screen Example 5-21](#_bookmark146)

> [Figure 5-18 Menu Option Path Example 5-23](#_bookmark148)

> [Figure 5-19 Purge Receipts History For All Items Screen Example 5-24](#_bookmark149)

> [Figure 5-20 Menu Option Path Example 5-25](#_bookmark151)

> [Figure 5-21 Purge Register of All Transactions Screen Example 5-26](#_bookmark152)

> [Figure 5-22 Menu Option Path Example 5-27](#_bookmark154)

> [Figure 5-23 Purge Monthly Usage and Distribution Totals Screen Example 5-28](#_bookmark155)

> [Figure 5-24 Menu Option Path Example 5-29](#_bookmark157)

> [Figure 5-25 Select Transaction Register Entry Screen Example 5-30](#_bookmark159)

> [Figure 5-26 Menu Option Path Example 5-33](#_bookmark161)

> [Figure 5-27 Select Storage Location Screen Example 5-34](#_bookmark163)

> [Figure 5-28 Menu Option Path Example 5-34](#_bookmark165)

> [Figure 5-29 Calculated Due-Ins Report Screen Example 5-35](#_bookmark167)

> [Figure 6-1 Menu Option Path Example 6-1](#_bookmark171)

> [Figure 6-2 Enter Distribution Point Screen Example 6-2](#_bookmark173)

> [Figure 6-3 Display Item Report Example 6-3](#_bookmark175)

> [Figure 6-4 Menu Option Path Example 6-5](#_bookmark177)

> [Figure 6-5 Select Item Screen Example 6-5](#_bookmark179)

> [Figure 6-6 Menu Option Path Example 6-6](#_bookmark181)

> [Figure 6-7 Enter National Stock Number Screen Example 6-7](#_bookmark183)

> [Figure 6-8 Menu Option Path Example 6-9](#_bookmark185)

> [Figure 6-9 Enter Distribution Point Screen Example 6-10](#_bookmark187)

> [Figure 6-10 Edit Information Screen Example 6-10](#_bookmark189)

> [Figure 6-11 Menu Option Path Example 6-11](#_bookmark191)

> [Figure 6-12 Report Parameters Screen Example 6-12](#_bookmark193)

> [Figure 6-13 Menu Option Path Example 6-13](#_bookmark195)

> [Figure 6-14 Order Form Screen Example 6-15](#_bookmark197)

> [Figure 6-15 Menu Option Path Example 6-17](#_bookmark199)

> [Figure 6-16 Outstanding Transaction Report Example 6-19](#_bookmark201)

> [Figure 6-17 Menu Option Path Example 6-20](#_bookmark203)

> [Figure 6-18 Packaging Discrepancy Report Example 6-21](#_bookmark205)

> [Figure 6-19 Menu Option Path Example 6-21](#_bookmark207)

> [Figure 6-20 Packaging Discrepancy Report Example 6-22](#_bookmark209)

> [Figure 6-21 Menu Option Path Example 6-25](#_bookmark211)

> [Figure 6-22 Comprehensive Item Report Example 6-25](#_bookmark213)

> [Figure 6-23 Menu Option Path Example 6-27](#_bookmark215)

> [Figure 6-24 Enter Electronic Signature Screen Example 6-28](#_bookmark217)

> [Figure 6-25 Purchase Order Receipt Screen Example 6-29](#_bookmark219)

> [Figure 6-26 Receipt Conﬁrmation Screen Example 6-29](#_bookmark221)

> [Figure 7-1 Menu Option Path Example 7-1](#_bookmark224)

> [Figure 7-2 Adjustment Report Screen Example 7-2](#_bookmark226)

> [Figure 7-3 All Adjustment Data Printed Example 7-3](#_bookmark227)

> [Figure 7-4 Menu Option Path Example 7-5](#_bookmark229)

> [Figure 7-5 Summary Availability Listing Screen Example 7-5](#_bookmark231)

> [Figure 7-6 Long Availability Listing Screen Example 7-7](#_bookmark232)

> [Figure 7-7 Availability Listing Report 7-7](#_bookmark233)

> [Figure 7-8 Menu Option Path Example 7-8](#_bookmark235)

> [Figure 7-9 Long Report Example 7-9](#_bookmark237)

> [Figure 7-10 Summary Report Example 7-11](#_bookmark238)

> [Figure 7-11 Menu Option Path Example 7-12](#_bookmark240)

> [Figure 7-12 Report Parameters Screen Example 7-13](#_bookmark242)

> [Figure 7-13 Days Of Stock On Hand Report Example 7-14](#_bookmark244)

> [Figure 7-14 Menu Option Path Example 7-15](#_bookmark246)

> [Figure 7-15 Emergency Stock Report Example 7-16](#_bookmark248)

> [Figure 7-16 Menu Option Path Example 7-17](#_bookmark250)

> [Figure 7-17 Select Item Screen Example 7-19](#_bookmark252)

> [Figure 7-18 Use of Item Chart Example 7-19](#_bookmark254)

> [Figure 7-19 Menu Option Path Example 7-20](#_bookmark256)

> [Figure 7-20 Report Parameters Screen Example 7-22](#_bookmark258)

> [Figure 7-21 Distribution Costing Report, Example 7-22](#_bookmark260)

> [Figure 7-22 Menu Option Path Example 7-24](#_bookmark262)

> [Figure 7-23 Reports Parameters Screen Example 7-25](#_bookmark264)

> [Figure 7-24 Menu Option Path Example 7-26](#_bookmark267)

> [Figure 7-25 Report Parameters Screen Example 7-27](#_bookmark268)

> [Figure 7-26 Menu Option Path Example 7-29](#_bookmark270)

> [Figure 7-27 Reports Parameter Screen Example 7-30](#_bookmark271)

> [Figure 7-28 Menu Option Path Example 7-31](#_bookmark273)

> [Figure 7-29 Report Parameters Screen Example 7-33](#_bookmark274)

> [Figure 7-30 Menu Option Path Example 7-34](#_bookmark276)

> [Figure 7-31 Report Parameters Screen Example 7-35](#_bookmark277)

> [Figure 7-32 Menu Option Path Example 7-36](#_bookmark279)

> [Figure 7-33 Report Parameters Screen Example 7-38](#_bookmark280)

> [Figure 7-34 Menu Option Path Example 7-39](#_bookmark282)

> [Figure 7-35 Report Parameters Screen Example 7-40](#_bookmark283)

> [Figure 7-36 Menu Option Path Example 7-41](#_bookmark285)

> [Figure 7-37 Report Parameters Screen Example 7-42](#_bookmark287)

> [Figure 7-38 Summary Report Screen Example 7-43](#_bookmark289)

> [Figure 7-39 Comprehensive Report Example 7-43](#_bookmark291)

> [Figure 7-40 Menu Option Path Example 7-46](#_bookmark293)

> [Figure 7-41 Report Parameters Screen Example 7-47](#_bookmark295)

> [Figure 7-42 Menu Option Path Example 7-48](#_bookmark297)

> [Figure 7-43 Report Parameters Screen Example 7-49](#_bookmark299)

> [Figure 7-44 Menu Option Path Example 7-51](#_bookmark301)

> [Figure 7-45 Report Parameters Screen Example 7-52](#_bookmark303)

> [Figure 7-46 Transaction Register Report Example 7-53](#_bookmark305)

> [Figure 7-47 Menu Option Path Example 7-54](#_bookmark307)

> [Figure 7-48 Unit Costing Example 7-55](#_bookmark309)

> [Figure 7-49 Menu Option Path Example 7-56](#_bookmark311)

> [Figure 7-50 Report Parameters Screen Example 7-57](#_bookmark313)

> [Figure 7-51 Usage Demand Analysis Report Example 7-58](#_bookmark315)

> [Figure 7-52 Menu Option Path Example 7-59](#_bookmark317)

> [Figure 7-53 Report Parameters Example 7-59](#_bookmark319)

> [Figure 7-54 Menu Option Path Example 7-61](#_bookmark321)

> [Figure 7-55 Report Parameters Screen Example 7-62](#_bookmark323)

> [Figure 8-1 Menu Option Assigned the Standard Menu Conﬁguration for the Warehouse--](#_bookmark325) [General Inventory/Distribution Menu 8-1](#_bookmark325)

> [Figure 9-1 Menu Option Path Example 9-1](#_bookmark329)

> [Figure 9-2 On-Demand Flag setting Example 9-3](#_bookmark331)

> [Figure 9-3 Menu Option Path Example 9-4](#_bookmark334)

> [Figure 9-4 Select Distribution Point Screen Example 9-5](#_bookmark335)

> [Figure 9-5 On-Demand Conﬂict Report Example 9-6](#_bookmark336)

> [Figure 9-6 Menu Option Path Example 9-7](#_bookmark338)

> [Figure 9-7Select Item Screen Example 9-7](#_bookmark339)

> [Figure 9-8 Menu Option Path Example 9-8](#_bookmark342)

> [Figure 9-9 Select Group Category Screen Example 9-8](#_bookmark343)

> [Figure 9-10 Abbreviated Item Report Example 9-9](#_bookmark344)

> [Figure 9-11 Menu Option Path Example 9-10](#_bookmark346)

> [Figure 9-12 Select Item Category Screen Example 9-11](#_bookmark347)

> [Figure 9-13 Select Report Type Screen Example 9-11](#_bookmark348)

> [Figure 9-14 Automatic Level Setter Report Example 9-12](#_bookmark349)

> [Figure 9-15 Menu Option Path Example 9-12](#_bookmark351)

> [Figure 9-16 Select Group Category Screen Example 9-13](#_bookmark352)

> [Figure 9-17 Comprehensive Item Report Example 9-13](#_bookmark353)

> [Figure 9-18 Menu Option Path Example 9-15](#_bookmark355)

> [Figure 9-19 Select Group Category Screen Example 9-15](#_bookmark356)

> [Figure 9-20 Select Report Type Screen Example 9-16](#_bookmark357)

> [Figure 9-21 Conversion Factor Report Example 9-16](#_bookmark358)

> [Figure 9-22 Menu Option Path Example 9-17](#_bookmark360)

> [Figure 9-23 Select Item and Date Screen Example 9-17](#_bookmark361)

> [Figure 9-24 Cost Trend Analysis Screen Example 9-18](#_bookmark362)

> [Figure 9-25 Menu Option Path Example 9-18](#_bookmark364)

> [Figure 9-26 Select Type of Report Screen Example 9-18](#_bookmark365)

> [Figure 9-27 Days of Stock On Hand Report Example 9-20](#_bookmark366)

> [Figure 9-28 Menu Option Path Example 9-20](#_bookmark368)

> [Figure 9-29 Select Item Screen Example 9-21](#_bookmark369)

> [Figure 9-30 Display Item Report Example 9-21](#_bookmark370)

> [Figure 9-31 Menu Option Path Example 9-23](#_bookmark372)

> [Figure 9-32 Select Item Screen Example 9-23](#_bookmark373)

> [Figure 9-33 Report Screen Example 9-23](#_bookmark374)

> [Figure 9-34 Menu Option Path Example 9-23](#_bookmark376)

> [Figure 9-35 Select Type Screen Example 9-24](#_bookmark377)

> [Figure 9-36 Select Display of Zero Quantity items Screen Example 9-25](#_bookmark378)

> [Figure 9-37 Inactive Item Report Example 9-25](#_bookmark379)

> [Figure 9-38 Menu Option Path Example 9-25](#_bookmark381)

> [Figure 9-39 Select Distribution Point Screen Example 9-26](#_bookmark382)

> [Figure 9-40 Report Screen Example 9-26](#_bookmark383)

> [Figure 9-41 Menu Option Path Example 9-27](#_bookmark385)

> [Figure 9-42 Select Distribution Point Screen Example 9-27](#_bookmark386)

> [Figure 9-43 Comprehensive Item Report Example 9-27](#_bookmark387)

> [Figure 9-44 Menu Option Path Example 9-28](#_bookmark389)

> [Figure 9-45 Select Data Screen Example 9-28](#_bookmark390)

> [Figure 9-46 Stock Status Report Example 9-29](#_bookmark391)

> [Figure 9-47 Menu Option Path Example 9-33](#_bookmark393)

> [Figure 9-48 Select Date, Category and Type of Item Screen Example 9-33](#_bookmark394)

> [Figure 9-49 Usage Demand Analysis Screen Example 9-35](#_bookmark395)

> [Figure 9-50 Menu Option Path Example 9-35](#_bookmark397)

> [Figure 9-51 Select Date, Items, Category, Item type and Item Order Screen Example 9-36](#_bookmark398)

> [Figure 9-52 Usage Demand Item Report Example 9-37](#_bookmark399)

> [Figure 9-53 Label Screen Example 9-38](#_bookmark402)

> [Figure 9-54 Pre-ODI Prim/Secondary Label Example 9-40](#_bookmark404)

> [Figure 11-1 Transaction Error Example 11-1](#_bookmark407)

> [Figure 11-2 System Error Occurred Screen Example 11-1](#_bookmark408)

> THIS PAGE INTENTIONALLY LEFT BLANK

> Introduction to the Generic Inventory Package

# Chapter 1. Introduction to the Generic Inventory Package


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Chapter 1. Introduction to the Generic Inventory Package](#chapter-1-introduction-to-the-generic-inventory-package)
  - [The General Inventory System](#the-general-inventory-system)
  - [Package Management](#package-management)
  - [Package Operation](#package-operation)
- [Chapter 2. Auto-Generate Orders](#chapter-2-auto-generate-orders)
  - [Introduction](#introduction)
  - [Select Fiscal Year](#select-fiscal-year)
  - [Select Group Category](#select-group-category)
  - [Start Auto-Generation](#start-auto-generation)
  - [Print Report](#print-report)
  - [Report Display](#report-display)
- [Chapter 3. Barcode Manager Menu](#chapter-3-barcode-manager-menu)
  - [Barcode User Menu](#barcode-user-menu)
    - [Download Barcode Program](#download-barcode-program)
    - [Upload Barcode Data](#upload-barcode-data)
  - [Data Manager Menu](#data-manager-menu)
    - [Enter/Edit/View](#entereditview)
    - [Schedule Data to Process](#schedule-data-to-process)
    - [Status of Data](#status-of-data)
  - [Labels Menu](#labels-menu)
    - [Inquire Label](#inquire-label)
    - [Print Labels](#print-labels)
  - [Programmer (Barcode) Menu](#programmer-barcode-menu)
    - [Comment Alignment](#comment-alignment)
    - [Design Label](#design-label)
    - [Parameter Enter/Edit](#parameter-enteredit)
    - [Program Enter/Edit](#program-enteredit)
    - [Specialty Commands Enter/Edit](#specialty-commands-enteredit)
- [Chapter 4. Inventory File Maintenance Menu](#chapter-4-inventory-file-maintenance-menu)
  - [Adjust Inventory Quantity Menu](#adjust-inventory-quantity-menu)
    - [Issue Book Adjustment](#issue-book-adjustment)
    - [Physical Count Form](#physical-count-form)
    - [Unapproved Adjustment Report](#unapproved-adjustment-report)
  - [Automatic Level Setter](#automatic-level-setter)
    - [Level Parameters](#level-parameters)
    - [Levels Set](#levels-set)
    - [Update](#update)
    - [Enter/Edit Inventory Item Data](#enteredit-inventory-item-data)
    - [Item Selection](#item-selection)
  - [File Inquiry](#file-inquiry)
    - [File Review](#file-review)
    - [Select Item](#select-item)
- [Chapter 5. Manager for Supply Warehouse Inventory Point Menu](#chapter-5-manager-for-supply-warehouse-inventory-point-menu)
  - [Balance Update Transaction (IM-6)](#balance-update-transaction-im-6)
    - [Select Item](#select-item-1)
  - [Clean Up Old Transactions and Due-Outs](#clean-up-old-transactions-and-due-outs)
    - [Enter Date](#enter-date)
  - [Date Received Delete (for Issue Book Requests)](#date-received-delete-for-issue-book-requests)
    - [Enter Transaction Number](#enter-transaction-number)
  - [Distribution Costs Enter/Edit](#distribution-costs-enteredit)
    - [Enter Electronic Signature](#enter-electronic-signature)
  - [Enter/Edit Inventory and Distribution Points](#enteredit-inventory-and-distribution-points)
    - [Select Inventory Point](#select-inventory-point)
  - [FMS Code Sheets Rebuild/Retransmit](#fms-code-sheets-rebuildretransmit)
    - [Enter FMS Document Code](#enter-fms-document-code)
  - [Group Category Enter/Edit](#group-category-enteredit)
    - [Enter Group Category](#enter-group-category)
  - [Inventory Control Parameters Print](#inventory-control-parameters-print)
    - [Select Distribution Point](#select-distribution-point)
  - [Purge History Files Menu](#purge-history-files-menu)
    - [History By Cost Center Purge](#history-by-cost-center-purge)
    - [Receipts History By Item Purge](#receipts-history-by-item-purge)
    - [Transaction Register Purge](#transaction-register-purge)
    - [Usage/Distribution Monthly Totals Purge](#usagedistribution-monthly-totals-purge)
  - [Reprint Posted Picking Ticket](#reprint-posted-picking-ticket)
    - [Transaction Register Type](#transaction-register-type)
  - [Storage Location Enter/Edit](#storage-location-enteredit)
    - [Select Storage Location](#select-storage-location)
  - [Update Calculated Due-Ins/Outstanding Transaction](#update-calculated-due-insoutstanding-transaction)
    - [Enter Start Date](#enter-start-date)
- [Chapter 6. Receiving and Distribution Menu](#chapter-6-receiving-and-distribution-menu)
  - [On Demand Items](#on-demand-items)
    - [Display Item](#display-item)
    - [Enter Distribution Point](#enter-distribution-point)
    - [Display Item Report](#display-item-report)
  - [Display Where An Item Is Stocked](#display-where-an-item-is-stocked)
    - [Select Item](#select-item-2)
  - [Due-In Item Report](#due-in-item-report)
    - [Enter National Stock Number](#enter-national-stock-number)
  - [Enter/Edit Items On Distribution Point](#enteredit-items-on-distribution-point)
    - [Enter Distribution Point](#enter-distribution-point-1)
    - [Item Information](#item-information)
  - [Items Flagged 'Kill When Zero' Report](#items-flagged-kill-when-zero-report)
    - [Report Parameters](#report-parameters)
  - [Order Form](#order-form)
    - [Order Form Listing](#order-form-listing)
  - [Outstanding (Due-Outs) Transaction Listing](#outstanding-due-outs-transaction-listing)
    - [Report](#report)
  - [Packaging/Procurement Source Discrepancy Report](#packagingprocurement-source-discrepancy-report)
    - [Report](#report-1)
  - [Post Issue Book Order](#post-issue-book-order)
    - [Report](#report-2)
  - [Print Item On Distribution Inventory Point](#print-item-on-distribution-inventory-point)
    - [Print Report](#print-report-1)
  - [Purchase Order Receiving To Inventory Point](#purchase-order-receiving-to-inventory-point)
    - [Enter Electronic Signature](#enter-electronic-signature-1)
    - [Display Receipt](#display-receipt)
    - [Receipt Confirmation](#receipt-confirmation)
- [Chapter 7. Reports Menu](#chapter-7-reports-menu)
  - [Adjustment Voucher Recap](#adjustment-voucher-recap)
    - [Print Report](#print-report-2)
  - [Availability Listing](#availability-listing)
    - [Listing](#listing)
  - [Cost Trend Analysis Report](#cost-trend-analysis-report)
    - [Long Report](#long-report)
  - [Days Of Stock On Hand Report](#days-of-stock-on-hand-report)
    - [Report Parameters](#report-parameters-1)
    - [Report](#report-3)
  - [Emergency Stock Report](#emergency-stock-report)
    - [Report Parameters](#report-parameters-2)
  - [Graph Usage](#graph-usage)
    - [Select Item](#select-item-3)
    - [Chart](#chart)
  - [History of Distribution Report](#history-of-distribution-report)
    - [Report Parameters](#report-parameters-3)
    - [Report Display](#report-display-1)
  - [Inactive Items Report](#inactive-items-report)
    - [Report Parameters](#report-parameters-4)
  - [Informational Reports Menu](#informational-reports-menu)
    - [Abbreviated Item Report](#abbreviated-item-report)
    - [Comprehensive Item Report](#comprehensive-item-report)
    - [Conversion Factor Report](#conversion-factor-report)
    - [Last Procurement Source For Item Report](#last-procurement-source-for-item-report)
    - [Non-Issuable Stock Report](#non-issuable-stock-report)
    - [Substitute Listing Report](#substitute-listing-report)
  - [Inventory Sales Report](#inventory-sales-report)
    - [Report Parameters](#report-parameters-5)
    - [The Summary Report](#the-summary-report)
    - [The Comprehensive Report](#the-comprehensive-report)
  - [Quantity Distribution Report](#quantity-distribution-report)
    - [Report Parameters](#report-parameters-6)
  - [Stock Status Report](#stock-status-report)
    - [Report Parameters](#report-parameters-7)
  - [Transaction Register Report](#transaction-register-report)
    - [Report Parameters](#report-parameters-8)
    - [Report](#report-4)
  - [Unit Costing Report](#unit-costing-report)
    - [Report](#report-5)
  - [Usage Demand Analysis Report](#usage-demand-analysis-report)
    - [Report Parameters](#report-parameters-9)
    - [Report](#report-6)
  - [Usage Demand Item Report](#usage-demand-item-report)
    - [Report Parameters](#report-parameters-10)
  - [Voucher Summary Report](#voucher-summary-report)
    - [Report Parameters](#report-parameters-11)
- [Chapter 8. Menu Outline](#chapter-8-menu-outline)
- [Chapter 9. On-Demand Items (ODI)](#chapter-9-on-demand-items-odi)
  - [ODI Flag Authorization](#odi-flag-authorization)
  - [Flag an Item as ODI](#flag-an-item-as-odi)
    - [Select Special Parameters](#select-special-parameters)
  - [Reports – Primary & Secondary Level](#reports-primary-secondary-level)
    - [On Demand Conflict Report](#on-demand-conflict-report)
    - [On-Demand Audit Activity Report](#on-demand-audit-activity-report)
  - [Modified Reports – Primary & Secondary Level](#modified-reports-primary-secondary-level)
    - [Abbreviated Item Report \[PRCPRAIR\]](#abbreviated-item-report-prcprair)
    - [Automatic Level Setter \[PRCPRALS\]](#automatic-level-setter-prcprals)
    - [Comprehensive Item Report \[PRCPRCOM\]](#comprehensive-item-report-prcprcom)
    - [Conversion Factor Report \[PRCPRCFR\]](#conversion-factor-report-prcprcfr)
    - [Cost Trend Analysis Report \[PRCPRCTA\]](#cost-trend-analysis-report-prcprcta)
    - [Days of Stock On Hand Report \[PRCPRSOH\]](#days-of-stock-on-hand-report-prcprsoh)
    - [Display Item \[PRCPRITO\]](#display-item-prcprito)
    - [Display Where an Item is Stocked \[PRCPRSTK\]](#display-where-an-item-is-stocked-prcprstk)
    - [Inactive Items Report \[PRCPRIIR\]](#inactive-items-report-prcpriir)
    - [Inventory Control Parameters Print \[PRCPRINV\]](#inventory-control-parameters-print-prcprinv)
    - [Print Item on Distribution Inventory Point \[DISTPT^PRCPRCOM\]](#print-item-on-distribution-inventory-point-distptprcprcom)
    - [Stock Status Report \[PRCPPOLM\]](#stock-status-report-prcppolm)
    - [Usage Demand Analysis \[PRCPRUS1\]](#usage-demand-analysis-prcprus1)
    - [Usage Demand Item Report \[PRCPRUSE\]](#usage-demand-item-report-prcpruse)
  - [Barcode Label Modification](#barcode-label-modification)
    - [Primary/Secondary Label](#primarysecondary-label)
    - [Pre-ODI Prim/Secondary Label](#pre-odi-primsecondary-label)
- [Chapter 10. The Logistics Data Query Tool](#chapter-10-the-logistics-data-query-tool)
- [Chapter 11. Error Messages and Their Resolution](#chapter-11-error-messages-and-their-resolution)
- [Chapter 12. Glossary](#chapter-12-glossary)
- [Index](#index)

## The General Inventory System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IFCAP General Inventory System is used to manage the receipt, distribution, and maintenance of stock items received for the supply warehouse from outside vendors and distributed to primary inventory points. The system also manages receipt and distribution of items from primary inventory points to secondary inventory points.

> “Inventory system” refers to:

- The *Supply* Warehouse, which maintains a supply of items that are repetitively used by the services (“posted stock”);
- The Primary Inventory, which receives supplies directly from the warehouse or from outside vendors; and distributes supplies to its subordinate secondary inventory points.
- The Secondary Inventory, which is set up by a primary inventory point and which is directly dependent on that primary inventory point for receipt of orders.

> The manner in which the inventory system is set up aﬀects the functionality of each of the three parts of the inventory system.

> If the warehouse is running the inventory system, it may have several primaries being supplied by it. Those that keep perpetual inventory (i.e., keep records of stock received, costs, and distribution) will have independent functionality as described by the menu options in this manual. The primaries not keeping perpetual inventory will be managed by the warehouse and have no independent functions.

> A similar situation holds for the secondary inventory. A primary inventory point that is keeping a perpetual inventory can create a secondary inventory point. A primary, which has no independent functions, cannot create a secondary. If the secondary inventory is set up to keep a perpetual inventory, the secondary inventory menu options in this manual may be used at the secondary point. If the secondary does not keep perpetual inventory, the secondary will be managed by it’s primary, and have no independent functions. The options used in IFCAP have been divided into groups based on the type of work you do.

> Primary and Secondary inventory points may choose to designate certain items as On-Demand items due to their requirement to track and keep on hand even infrequently used items.

## Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Due to the nature of the information being processed by IFCAP, special attention has been paid to limiting usage to authorized individuals. Individuals in the system who have authority to approve actions, at whatever level, have an electronic signature code. This code is required before the documents pass on to a new level for processing or review. Like the access and verify codes used when gaining access to the system, the electronic signature code will not be visible on the terminal screen. These codes are also encrypted so that even when viewed in the user ﬁle by those with the highest levels of access, they are unreadable. Electronic signature codes are required by IFCAP at every level that currently requires a signature on paper.

> Introduction to the Generic Inventory Package

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The structured options of IFCAP's General Inventory module are called the menus, just like a menu in a restaurant. You select the option name or number that corresponds to your duties in General Inventory. IFCAP asks a sANYTOWNs of questions using terms familiar to you. If you do not understand the question or are unsure of how to respond, enter a question mark (?), and the computer will give you an explanation of the information needed, or allow you to choose from a list of responses.

> Below is a brief description of the main options to be found in the General Inventory Package.

> Some options will only be valid for certain users, Primary, Secondary, or Supply Warehouse.

> <span id="_bookmark4" class="anchor"></span>Table 1-1 GIP Options and Related Descriptions

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 24%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Inventory Point</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Auto-Generate Orders</p>
</blockquote></td>
<td><blockquote>
<p>Primary, Secondary and Supply Warehouse</p>
</blockquote></td>
<td><blockquote>
<p>This option will automatically generate a Primary or Supply Warehouse Inventory Point Repetitive Item list or a Secondary inventory point distribution order.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Barcode Manager Menu</p>
</blockquote></td>
<td><blockquote>
<p>Primary, Secondary and Supply Warehouse</p>
</blockquote></td>
<td><blockquote>
<p>This menu contains options that allow the user to implement barcode processing for the collection of inventory point data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Inventory File Maintenance</p>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Primary, Secondary and Supply Warehouse</p>
</blockquote></td>
<td><blockquote>
<p>The menu includes options for an inventory point to maintain the items stored for that particular inventory point.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Manager for Inventory Point Menu</p>
</blockquote></td>
<td><blockquote>
<p>Primary, Secondary and Supply Warehouse</p>
</blockquote></td>
<td><blockquote>
<p>This menu includes options for editing inventory point control parameters and for calculating due-ins, etc.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Receiving and Distribution</p>
<p>Menu</p>
</blockquote></td>
<td><blockquote>
<p>Primary and Supply Warehouse</p>
</blockquote></td>
<td><blockquote>
<p>This menu contains options for the handling of receiving and distribution.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reports Menu</p>
</blockquote></td>
<td><blockquote>
<p>Primary, Secondary and Supply Warehouse</p>
</blockquote></td>
<td><blockquote>
<p>The menu contains options for the running of reports concerning inventory points.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 24%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Inventory Point</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Stock Replenishment Menu</p>
</blockquote></td>
<td><blockquote>
<p>Secondary</p>
</blockquote></td>
<td><blockquote>
<p>This menu contains options for requesting supplies from a Primary Inventory point.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Chapter 2. Auto-Generate Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will automatically generate a Primary or Supply Warehouse Inventory Point repetitive item list or a Secondary Inventory Point Distribution Order. The auto-generation will use the selected group categories and those vendors (stored in the mandatory or suggested source ﬁeld in the Primary and Warehouse Inventory Points) for selecting the items. When an item's available quantity (quantity on-hand plus quantity due-in minus quantity due-out) falls below or equal to the standard re-order point, the item will be ordered. When an item's available quantity falls below or equal to the optional re-order point, the item will be ordered if there are other items for the same vendor which are being ordered due to the available quantity falling below the standard re-order point. If items only fall below the optional order point for a vendor, the order will not be generated.

> The quantity to order is the diﬀerence between the available quantity on hand and the normal stock level. Conversion factors (Warehouse to Primary, vendor to Primary, or vendor to Warehouse), vendor minimal issue quantity, and vendor issue multiple also factor into the total quantity of an item to order.

> On-Demand items with a zero normal stock level will be included in the re-order calculations and will be excluded from the Error List.

> The auto-generation of Secondary Distribution Orders will use the selected primary distribution point (stored in the mandatory or suggested source ﬁeld in the secondary) for selecting the items. When an item's available quantity (quantity on-hand plus quantity due-in) falls below or equal to the standard reorder point, the item will be ordered.

> At completion of auto-generation, a sANYTOWNs of reports can be generated. The user will be prompted only for those reports that contain data that would be included on that report. These reports will aid in determining why an item was or was not ordered.

## Select Fiscal Year

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Auto-generate Orders from the Warehouse--General Inventory/Distribution Menu. GIP will list the cost center and the control point. Enter a ﬁscal year and ﬁscal quarter. Refer to [Figure 2-1.](#_bookmark9) If you already have a repetitive item list on ﬁle, GIP will ask you if you want to delete

> Auto-Generate Orders

> the repetitive item lists on ﬁle. If you auto-generate orders, GIP will generate another repetitive item list. Multiple repetitive item lists can cause duplicate orders.

## Select Group Category

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As the example shows in [Figure 2-2,](#_bookmark10) you may select all group categories and vendors, or select individual group categories and vendors. You can deselect a group category or vendor by reselecting it. Press the Enter key at the Select Group Category: prompt when you have ﬁnished selecting group categories. Press the Enter key at the Select Vendor Name: prompt when you have ﬁnished selecting vendors.

Auto-Generate Orders

> <span id="_bookmark9" class="anchor"></span>Figure 2-1 Select Fiscal Year Example

> <span id="_bookmark10" class="anchor"></span>Figure 2-2 Select Group Category Example

> Auto-Generate Orders

## Start Auto-Generation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> GIP will ask you to conﬁrm that you want to start the auto-generation. Refer to [Figure 2-3](#_bookmark13). GIP will display a bar showing the percentage of auto-generation that it has completed. After GIP has generated the orders, GIP will create a new repetitive item list, and display a bar showing the percentage of item list creation that it has completed.

## Print Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> GIP will ask you if you want the auto-generation report to print the errors that occurred during auto-generation. GIP will also ask if you want to print items, which were not ordered. GIP will print or display the “Auto-Generation” report, listing the items and quantity on the order automatically generated, sorted by group category.

> <span id="_bookmark13" class="anchor"></span>Figure 2-3Start Auto-Generation Example

Auto-Generate Orders

> <span id="_bookmark14" class="anchor"></span>Figure 2-4 Auto-Generation Report Example – Part 1

> Auto-Generate Orders

> This report will identify On-Demand items by showing a D in the OD column when run at the Primary or Secondary level. Reference [Figure 2-5](#_bookmark15).

> <span id="_bookmark15" class="anchor"></span>Figure 2-5 Auto-Generation Report Example – Part 2

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 36%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>    </p>
</blockquote></th>
<th>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>   </td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>   </td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>   </td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td>   </td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p></p>
<p>    </p>
<p>   </p>
</blockquote></td>
</tr>
</tbody>
</table>

Auto-Generate Orders

## Report Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you answered yes at the Do You Want To Print Errors Occurring During Auto-Generation?: prompt, GIP will also print or display the “Auto-Generation Error Report”, [Figure 2-6.](#_bookmark17) It lists each error by item and cause of error. GIP will return to the General Inventory/Distribution Menu.

> <span id="_bookmark17" class="anchor"></span>Figure 2-6 Auto-Generation Error Report

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 63%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p>   </p>
<p>    </p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
<p>    </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Auto-Generate Orders

Auto-Generate Orders

> THIS PAGE INTENTIONALLY LEFT BLANK

# Chapter 3. Barcode Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Barcode Manager Menu allows you to manage barcode data and barcode programs.

## Barcode User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Download Barcode Program

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to copy a program from GIP to a barcode reader. Select the Barcode Manager’s Menu option, depicted in [Figure 3-1.](#_bookmark21) <span id="_bookmark21" class="anchor"></span>Figure 3-1 Menu Option Path Example

> Select Barcode User Menu from the Barcode Manager Menu. Select Download Barcode Program from the Barcode User Menu. Depicted in [Figure 3-2.](#_bookmark22)

> <span id="_bookmark22" class="anchor"></span>Figure 3-2 Barcode User Menu Example

> Barcode Manager Menu

1.  Select Program

> [Figure 3-3](#_bookmark23) illustrates the screen that will be displayed. Enter the name of the barcode program you want to download. GIP will warn you that when a program is sent to the barcode reader, all data stored on the barcode reader is lost, and that you should make sure that previous users of this barcode reader have no need for data, if any, that might exist on the reader.

> Connect the barcode reader to the output device. Clear the barcode reader by turning the reader oﬀ and back on. Enter the name of the device you connected to the barcode reader at the Device: prompt.

Barcode Manager Menu

> <span id="_bookmark23" class="anchor"></span>Figure 3-3 Barcode Program Entry Example

2.  Reader

> GIP will send the program to the reader and inform you when the download is complete. Refer to [Figure 3-4.](#_bookmark24) The barcode reader is now ready to use the program. GIP will return to the Barcode User Menu.

> Barcode Manager Menu

> <span id="_bookmark24" class="anchor"></span>Figure 3-4 Download Complete Message Example

### Upload Barcode Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to transmit data from the barcode reader to the barcode data sub-ﬁeld of the BARCODE PROGRAM ﬁle in GIP.

Barcode Manager Menu

> <span id="_bookmark26" class="anchor"></span>Figure 3-5 Menu Option Path Example

3.  Enter Device

> Select Upload Barcode Data from the Barcode User Menu, [Figure 3-6.](#_bookmark27) Enter the device to which the barcode reader is connected at the Device: prompt. Use the TRANSMIT option on the barcode reader to send the data. After the barcode reader sends the data, GIP will return to the Barcode User Menu.

> <span id="_bookmark27" class="anchor"></span>Figure 3-6 Update Barcode Data Selected Example

> Barcode Manager Menu

## Data Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enter/Edit/View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow users to view barcode data, determine the status of that data, enter barcode data and edit barcode data.

> <span id="_bookmark30" class="anchor"></span>Figure 3-7 Menu Option Path Example

4.  Select Barcode Program

> Select Data Manager Menu from the Barcode Manager Menu, as depicted in [Figure 3-8.](#_bookmark31) Select Enter/Edit/View from the Data Manager Menu. Enter the name of the barcode program.

> <span id="_bookmark31" class="anchor"></span>Figure 3-8 Menu Option Path Example

Barcode Manager Menu

5.  Set Date and Time

> Enter the date AND TIME that you want GIP to upload the barcode data in the following format: date@military time. Refer to [Figure 3-9.](#_bookmark32)

> For example, if you wanted to upload the barcode data today at 2:30 pm enter T@14:30 at the Select Date/Time Of Data Upload: prompt. If you wanted to upload the barcode data on June 11, 2012 at 9:15 a.m., enter Jun 11, 2012@09:15 at the Select Date/Time Of Data Upload: prompt. GIP will ask you to conﬁrm that you want to enter the new upload time, if you are

> Barcode Manager Menu

> entering new upload data. Enter Y for yes. Enter the user assigned to the barcode data at the User: prompt. At the Status: prompt, enter the status of the data you are uploading. Start here

> <span id="_bookmark32" class="anchor"></span>Figure 3-9 Date and Time of Data Upload Screen Example

>          

>       

>              

>   

>  

>            

>             

>           

>       

>       

>         

>            

            

> 

>           

>        

>   

          

>     

           

>      

>     

          

>      

>       

> 

Barcode Manager Menu

6.  Enter Barcode Data

> Enter the barcode data at the prompt, as shown in [Figure 3-10.](#_bookmark33) You may enter another upload time at the Select Date/Time Of Data Upload: prompt or press the Enter key if you are ﬁnished entering or editing upload data. GIP will return to the Data Manager Menu.

> <span id="_bookmark33" class="anchor"></span>Figure 3-10 Barcode Data Entry Screen Example

> Barcode Manager Menu

### Schedule Data to Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to reschedule the processing of data that may have failed to run because of an error.

> Select the Barcode Manager’s Menu option, depicted in [Figure 3-11](#_bookmark35).

> <span id="_bookmark35" class="anchor"></span>Figure 3-11 Menu Option Path Example

> Select Data Manager Menu from the Barcode Manager Menu. Select Schedule Data to Process from the Data Manager Menu, shown in [Figure 3-12](#_bookmark36).

> <span id="_bookmark36" class="anchor"></span>Figure 3-12 Schedule Data to Process from the Data Manager Menu Example

Barcode Manager Menu

7.  Setup Data

> Enter a station number and a primary inventory point, as depicted in [Figure 3-13.](#_bookmark37) Enter a barcode program name. If you do not know the program name, enter three question marks and GIP will list the available barcode programs. Enter the date and time that the data is scheduled for upload. If you do not remember the date and time, enter three question marks at the prompt and GIP will list the upload times.

> <span id="_bookmark37" class="anchor"></span>Figure 3-13 Setup Data Screen Example

8.  Status Display

> GIP will display the status of the upload you selected and ask you to conﬁrm that you want to reschedule the data. Refer to Answer Y. GIP will return to the Data Manager Menu.

> <span id="_bookmark38" class="anchor"></span>Figure 3-14 Status Screen Example

> Barcode Manager Menu

Barcode Manager Menu

### Status of Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print the status of data that is being uploaded or has been uploaded from barcode readers.

> Select the Barcode Manager’s Menu option and other options as depicted in [Figure 3-15](#_bookmark40).

> <span id="_bookmark40" class="anchor"></span>Figure 3-15 Menu Option Path Example

> Barcode Manager Menu

9.  Enter Date and Time

> Enter the date and time of the ﬁrst data upload, or press the Enter key to include all of the data uploads in the system. GIP will print or display the 'Barcode Program List' report, listing each upload, the user assigned to the upload, and the status of the upload. After printing or displaying the report, GIP will return to the Data Manager Menu.

> <span id="_bookmark41" class="anchor"></span>Figure 3-16 Date and Time of Data Upload Screen Example

## Labels Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Inquire Label

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to view information about a customized VA FileMan label.

Barcode Manager Menu

> <span id="_bookmark44" class="anchor"></span>Figure 3-17 Menu Option Path Example

10. Enter Label Name

> Enter the label name at the Select Custom Label Name: prompt, as depicted in [Figure 3-18.](#_bookmark45) If you do not know the label name, enter three question marks and GIP will list the available custom labels. GIP will list the label name and its associated ﬁle, and the executable File Man code that creates the label. Enter another label name at the Select Custom Label Name: prompt, or press the Enter key to return to the Labels Menu.

> <span id="_bookmark45" class="anchor"></span>Figure 3-18 Label Name Entry Screen Example

> Barcode Manager Menu

Barcode Manager Menu

### Print Labels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to print a customized FileMan label.

> <span id="_bookmark47" class="anchor"></span>Figure 3-19 Menu Option Path Example

11. Select Label 2

> Select the custom label of the item or items you want to print at the Select Custom Label Name: prompt, or enter three question marks at the prompt to see the list of available custom labels. You can select items for printing, or print a range of inventory items. Enter the time that you want the report to print at the Requested Start Time: prompt, or press the Enter key to print the report now. GIP will return to the Labels Menu.

> <span id="_bookmark48" class="anchor"></span>Figure 3-20 Custom Label Selection Screen Example

> Barcode Manager Menu

## Programmer (Barcode) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Comment Alignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the alignment of comments in a barcode program. You can also align comments by using the FileMan programmer 'Y' option during the edit function. By executing the following code, comments can be aligned at any column for a range of lines:

> S Y=\[column\] D CON^PRCTBAR

> While editing your barcode program, decide your comment alignment at the 28th column for lines 20-40. At the 'Edit option:' prompt, enter a 'Y'. You would then enter:

> S Y=\[column\] D CON^PRCTBAR

Barcode Manager Menu

> FileMan will then ask the range of lines you want to process. By entering the range of 20-40, the lines will have comments aligned to the 28 columns.

> <span id="_bookmark51" class="anchor"></span>Figure 3-21 Menu Option Path Example

> Barcode Manager Menu

12. Select Barcode Program

> Enter the barcode program name to which you want to add comments. Refer to [Figure 3-22](#_bookmark52). Enter the character column where you want all comments to begin. If you want to line up all comment lines (::) in you BARCODE program at a certain column, enter the column you wish all comments to begin. For example, if some of your comments begin at column 37 in some lines and some comments begin at column 40 in other lines, you may want to have all comments begin at column 35 for readability. Valid choices are 30, 35, 40 and 45. Enter the range where you want the comments to begin and end. GIP will change the barcode program and return to the Programmer (Barcode) Menu.

> <span id="_bookmark52" class="anchor"></span>Figure 3-22 Select Barcode Program Name Example

Barcode Manager Menu

### Design Label

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the designing of a customized report or label. It interfaces with VA FileMan, but allows users to design a FileMan report using a word-processing ﬁeld with parameters.

> <span id="_bookmark54" class="anchor"></span>Figure 3-23 Menu Option Path Example

> Barcode Manager Menu

13. Edit Label

> You may edit an existing label by entering an existing label name at the Select Custom Label Name: prompt, or enter the name of the new label you wish to create. Refer to [Figure 3-24](#_bookmark55).

> You can change the name at the Name: prompt. At the File: prompt, enter the name of the ﬁle that the label will print from during search and sort functions. For example: If you want to print a label for all drugs in the drug ﬁle, you would enter 50 or DRUG for this ﬁeld and labels will print from this ﬁle. If this ﬁeld is not deﬁned, then the label will be considered to be just free text and not associated with a ﬁle. If you do not know the ﬁle name, enter three question marks at the prompt and GIP will list the available ﬁles.\\

> <span id="_bookmark55" class="anchor"></span>Figure 3-24 Editing an Existing Label Screen Example

Barcode Manager Menu

>     

>    

>               

>              

>               

>              

>             

>  

>  

>   

>   

>   

>  

>  

>   

>  

>   

>    

>   

>  

>  

>   

>   

>    

>   

>   

>  

>  

>     

>   

> Barcode Manager Menu

14. Select Routine

> If you want to specify a special routine to print the labels, enter the routine name at the Label Routine: prompt (

<span id="_bookmark56" class="anchor"></span>Barcode Manager Menu

> [Figure 3-25](#_bookmark56)). At the Specialty Commands: prompt, enter the specialty command for the label. At the Text: prompt, enter the commands that describe the label. At the Parameter: prompt, enter the parameter number on the label. Enter three question marks to see a list of available parameters.

> Barcode Manager Menu

> <span id="_bookmark57" class="anchor"></span>Figure 3-25 Special Routine Specified Screen Example

>  

>      

>         

>  

>   

>   

>  

>     

> 

>  

> 

> 

>  

>    

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 21%" />
<col style="width: 17%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

>         

>   

>  

Barcode Manager Menu

15. Enter Description

> Enter the description of the parameter at the Description: prompt. Refer to [Figure 3-36.](#_bookmark72) Enter the parameter type at the Parameter: prompt. Enter the barcode type of the parameter at the Barcode Type: prompt. Enter the text you want printed before the parameter at the Pre-text: prompt. Enter the text you want printed after the parameter at the Post-text: prompt.

> <span id="_bookmark58" class="anchor"></span>Figure 3-26 Parameter Description Screen Example

> Barcode Manager Menu

16. Entering Executable Code

> Enter the number of tabs at the Tab: prompt. [Figure 3-27](#_bookmark59) is an example of such. Enter the executable M code for the parameter at the Xecutable Code: prompt. Enter another parameter name at the Parameter: prompt to create or edit another parameter, or press the Enter key if you are through editing and creating parameters. GIP will check the report integrity of the parameter and compile a report. Enter another custom label name to enter or edit another label, or press the Enter key to return to the Programmer (Barcode) Menu.

> <span id="_bookmark59" class="anchor"></span>Figure 3-27 Executable Code Screen Example

Barcode Manager Menu

### Parameter Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to enter and edit barcode program parameters. Some of the parameters that may be edited are Routine and Line Tag that process data, Time to Queue Routine that process the data, etc.

> <span id="_bookmark61" class="anchor"></span>Figure 3-28 Menu Option Path Example

> Barcode Manager Menu

17. Enter Barcode Program Name

> Enter the name of the barcode program you want to edit or create. Refer to [Figure 3-29.](#_bookmark62) If you enter the name of an existing barcode program, GIP will allow you to edit the program name, identiﬁer, upload routine, data processor routine, the time GIP will queue the routine, whether the routine will prompt for a device or run in the background, the number of days before uploads are purged, and any specialty commands.

> <span id="_bookmark62" class="anchor"></span>Figure 3-29 Barcode Program Name Screen Example

Barcode Manager Menu

> At the Identiﬁer: prompt, enter a package namespace followed by two characters. The identiﬁer acts as a “tag” added to the barcode program that identiﬁes what kind of data the program is downloading. For example: If the program handles inventory of formulary drugs for outpatient, the identiﬁer might be 'PSOFM'. The 'PSO' is the outpatient namespace and 'FM' is two characters that further describe the type of program.

18. Upload Routine

> At the Post Upload Routine: prompt, enter the ANSI-M routine that will be called directly after a successful upload of data has taken place. This ﬁeld can also contain a line tag. The dash (-) is used, instead of the up-arrow (^) to separate the line tag from the routine. For example, if the routine that should be called is EN^ENG you would enter EN-ENG in this ﬁeld. At the Data Processor Routine: prompt, enter the ANSI-MUMPS routine that will be tasked to Task Manager after data is uploaded from the barcode reader. This routine will be responsible for the processing of data in the BARCODE DATA multiple (data upload from the barcode reader). This ﬁeld can also contain a line tag. Use a dash (-) instead of an up-arrow (^) to separate the line tag from the routine. For example, if the routine that should be called is EN^ENG, enter EN-ENG at the prompt.

> At the Time To Queue: prompt, enter the time of day that the system should process the data. For example, if 1AM is entered into this ﬁeld, the system will not process the entry until 1 a.m.

> Barcode Manager Menu

> Users can upload data from a barcode reader anytime; this prompt allows each site to specify what time of the day to process the data. If you do not specify a time at this prompt, the system will attempt to process data as soon as users upload it to GIP. [Figure 3-30](#_bookmark63) is a depiction of this type of attempt.

> <span id="_bookmark63" class="anchor"></span>Figure 3-30 Upload Attempt Example

19. Enter Device

> At the Is Device Required?: prompt, enter N if you want this program to run in the background. At the Purge Days: prompt, enter the number of days that GIP will store barcode data, or press the Enter key for the default time of seven days. The GIP design team recommends that you keep this data for at least seven days.

> At the Specialty Commands: prompt, enter any specialty commands for the barcode program. Enter three question marks at the prompt to see the available specialty commands.

> Enter another barcode program name at the prompt, or press the Enter key to return to the Programmer (Barcode) Menu.

> <span id="_bookmark64" class="anchor"></span>Figure 3-31 Device Screen Example

Barcode Manager Menu

> Barcode Manager Menu

### Program Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows users to enter or edit barcode programs.

> <span id="_bookmark66" class="anchor"></span>Figure 3-32 Menu Option Path Example

Barcode Manager Menu

20. Select Barcode Program

> Enter the name of the barcode program you wish to enter or edit. Refer to [Figure 3-33.](#_bookmark67) The system will display two VA FileMan word processing ﬁelds. This ﬁrst word processing ﬁeld will allow you to edit the name of the barcode program. The second ﬁeld will allow you to edit the program code. After you ﬁnish editing the program name and program code, the system will return to the Programmer (Barcode) Menu.

> <span id="_bookmark67" class="anchor"></span>Figure 3-33 Barcode Program Name Screen Example

>     

>  

>    

>   

> 

>  

>   

>             

>           

>    

>         

>        

> 

>   

>    

>   

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 2%" />
<col style="width: 11%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>         </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
</tr>
</tbody>
</table>

>     

>         

> Barcode Manager Menu

### Specialty Commands Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows users to enter and edit specialty commands for the Intermec Trakker 9440 and Label 3X1/Intermec 8646.

> <span id="_bookmark69" class="anchor"></span>Figure 3-34 Menu Option Path Example

Barcode Manager Menu

21. Creating a Barcode Program

> If you are editing an existing barcode program, proceed to paragraph [0](#_bookmark71).

> [Figure 3-35](#_bookmark70) displays and example of creating a barcode program. Enter the name you want to assign to the barcode program. At the Barcode Program Identiﬁer: prompt, enter a package namespace followed by two characters. The identiﬁer acts as a “tag” added to the barcode program that identiﬁes what kind of data the program is downloading. For example: If the program handles inventory of formulary drugs for outpatient, the identiﬁer might be 'PSOFM'.

> Barcode Manager Menu

> <span id="_bookmark70" class="anchor"></span>Figure 3-35 Barcode Program Creation Screen Example

> <span id="_bookmark71" class="anchor"></span>The 'PSO' is the outpatient namespace and 'FM' is two characters that further describe the type of program. GIP will start the VA FileMan line editor. Enter the barcode program code in the line editor. After you ﬁnish entering the barcode program code, GIP will return to the Programmer (Barcode) Menu.

Barcode Manager Menu

22. Editing a Barcode Program

> [Figure 3-36](#_bookmark72) displays an example of editing a barcode program. Enter a barcode program name. If you do not know the name of the program you want to edit, enter three question marks at the prompt and GIP will list the available barcode programs. GIP will start the VA FileMan editor and allow you to edit the barcode program name and program code. After you ﬁnish editing the program code, GIP will return to the Programmer (Barcode) Menu.

> <span id="_bookmark72" class="anchor"></span>Figure 3-36 Editing a Barcode Program Screen Example

>     

>  

>    

>   

>  

>   

>             

>           

>    

>         

>     

>    

>   

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 10%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p></p>
<p></p>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>         </p>
<p>   </p>
<p> </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>       </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>     </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>  </p>
</blockquote></td>
</tr>
</tbody>
</table>

> Barcode Manager Menu

Barcode Manager Menu

> THIS PAGE INTENTIONALLY LEFT BLANK

# Chapter 4. Inventory File Maintenance Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Adjust Inventory Quantity Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to adjust the warehouse quantity on-hand for selected items. There are four types of adjustments: an issue adjustment, to/from non-issuable, other type adjustment (actual count, etc), and Supply Only (GIP) Adjustment. After you make an adjustment, GIP creates and transmits the correct code sheets automatically.

> Select Inventory File Maintenance Menu from the Warehouse--General Inventory/Distribution Menu.

> Select Adjust Inventory Quantity Menu from the Inventory File Maintenance Menu. Select Adjust Inventory Quantity from the Adjust Inventory Quantity Menu.

> <span id="_bookmark75" class="anchor"></span>Figure 4-1 Menu Option Path Example

> Inventory File Maintenance Menu

Inventory File Maintenance Menu

### Issue Book Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you are making an issue book adjustment, follow the instructions in the section below. Otherwise, skip this section and go to the next section.

1.  Select Type of Adjustment

> Select Issue Book Adjustment at the Select Type of Adjustment: prompt. Refer to [Figure 4-2](#_bookmark77). Enter the transaction number of the issue book request at the Select Transaction Number: prompt. Enter the line number that you want to adjust. The system will display the item information, the quantity information, and the dollar value of the item.

> <span id="_bookmark77" class="anchor"></span>Figure 4-2 Select Issue Book Adjustment Screen Example

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 14%" />
<col style="width: 3%" />
<col style="width: 12%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p>     </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p>   </p>
</blockquote></th>
<th>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td> </td>
</tr>
<tr class="even">
<td> </td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>  </td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>  </td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>   </p>
<p>   </p>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>

> Inventory File Maintenance Menu

2.  Enter Adjustment Data

> Figure 4-3 displays an example of data entry adjustments. The system will let you change the quantity of the item, the cash value of the item as inventory stock, and the cash value of the item when it is issued to the service. The system will add “reason text”, or an explanation line, to the transaction explaining the reason for the adjustment. The default reason text is “Issue Book Adjustment,” but you can edit this explanation. When you have ﬁnished editing line numbers, press the Enter key at the Select Line Item Number: prompt. Answer Y at the Ready To Process Issue Book Adjustments?: prompt to process the adjustment and update the inventory point. The system will list the number of the FMS document sent to FMS and the VA MailMan message that contained the ISMS/LOG code sheet. Enter another transaction number at the Select Transaction Number: prompt, or press the Enter key to return to the Adjust Inventory Quantity Menu.

Inventory File Maintenance Menu

> <span id="_bookmark78" class="anchor"></span>Figure 4-3 Data Adjustment Entry Screen Example

> Inventory File Maintenance Menu

3.  Non-Issuable or Issuable Adjustment

> If you are making a non-issuable or issuable adjustment, follow the instructions in the section below. Otherwise, skip this section and go to the next section.

1.  Select Type of Adjustment

> Select Non-Issuable or Issuable Adjustment at the Select Type of Adjustment: prompt. Refer to [Figure 4-4.](#_bookmark79) Enter the name of the item or the item number at the Select Whse Item: prompt. If you do not know the name or number of the item, enter three question marks and the system will list the available items. The system will list the cost and quantity information for the item.

> <span id="_bookmark79" class="anchor"></span>Figure 4-4 Select Type of Adjustment Screen Example

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 4%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>  </p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>   </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Enter Adjustment Data

> At the Adjusted Quantity: prompt, ([Figure 4-5](#_bookmark80)) enter a negative number for the amount of units you want to deduct from warehouse stock. Enter an alphanumeric code for the adjustment voucher number. The system will add “reason text”, or an explanation line, to the transaction

Inventory File Maintenance Menu

> explaining the reason for the adjustment. The default reason text is “To Non-Issuable,” but you can edit this explanation. When you have ﬁnished adjusting warehouse items, press the Enter key at the Select Whse Item: prompt. Enter Y at the Ready To Process Non-Issuable Adjustments?: prompt to transmit the adjustment. The system will display the VA MailMan message number of the adjustment and return to the Adjust Inventory Quantity Menu.

> <span id="_bookmark80" class="anchor"></span>Figure 4-5 Enter Adjustment Data Screen Example

4.  Other Adjustment

> Select Other Adjustments at the Select Type Of Adjustment: prompt. Refer to [Figure 4-6.](#_bookmark81) Enter the name of the item or the item number at the Select Whse Item: prompt. If you do not know

> Inventory File Maintenance Menu

> the name or number of the item, enter three question marks and the system will list the available items. The system will list the cost and quantity information for the item.

> <span id="_bookmark81" class="anchor"></span>Figure 4-6 Other Adjustments Screen Example

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 4%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>  </p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>   </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Enter Adjustment Data

> Enter a negative number at the Adjusted Quantity: prompt to subtract from the inventory quantity, or a positive number to add to the inventory quantity. You also need to enter the change in value, either positive or negative, to the overall value of the total inventory of the item. In the example below, adding 4 to the overall quantity at a value of \$1.61 per unit is an

Inventory File Maintenance Menu

> adjusted total inventory value of \$6.44. Enter an alphanumeric code for the adjustment voucher number. The system will list the available adjustments. Select the appropriate adjustment category. When you are ﬁnished adjusting warehouse items, press the Enter key at the Select Whse Item: prompt. Enter Y at the Ready To Process Inventory Adjustments?: prompt. The system will list the number of the FMS document and VA MailMan message it created to transmit the adjustment, and return to the Adjust Inventory Quantity Menu. [Figure](#_bookmark82) [4-7](#_bookmark82) depicts this process.

> <span id="_bookmark82" class="anchor"></span>Figure 4-7 Enter Adjustment Data Screen Example

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p>      </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>    </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>     </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>    </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>

> Inventory File Maintenance Menu

5.  Approve Adjustments

> Use this option to approve entire adjustments (all items) or single items on an adjustment. When an item adjustment is approved, the item adjustment will no longer appear on the 'Unapproved Adjustment Report.'

> <span id="_bookmark83" class="anchor"></span>Figure 4-8 Menu Option Path Example

Inventory File Maintenance Menu

6.  Enter Adjustment Number

> Enter the number of the adjustment that you want to approve. If you do not know the adjustment number, enter three question marks at the prompt and the system will list the available adjustments. You may approve all of the items on the adjustment, or select individual items for approval. Press the Enter key at the Select Item: and Select Adjustment Number: prompts when you have ﬁnished approving adjustments. The system will return to the Adjust Inventory Quantity Menu. [Figure 4-9](#_bookmark84) displays this process.

> <span id="_bookmark84" class="anchor"></span>Figure 4-9 Adjustment Number Screen Example

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 34%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Inventory File Maintenance Menu

### Physical Count Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to print the physical count form for the warehouse, sorted by main storage location, account code, and National Stock Number.

> <span id="_bookmark86" class="anchor"></span>Figure 4-10 Menu Option Path Example

Inventory File Maintenance Menu

7.  Select Account Codes

> The system will ask you if you want to select all account codes. If it would be easier for you to list the account codes you DO NOT want to select than to list the account codes you DO want to select, enter Y at this prompt, and enter the account codes you want to de-select at the Select Account Code: prompt. Press the Enter key at the Select Account Code: prompt when you have ﬁnished selecting and deselecting account codes.

> <span id="_bookmark87" class="anchor"></span>Figure 4-11 Select Access Code Screen Example

> Inventory File Maintenance Menu

>            

>          

>    

>     

>            

>           

>     

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 48%" />
<col style="width: 20%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

>       

>  

>    

>     

>            

>    

> 

>            

>           

>     

>    

>    

Inventory File Maintenance Menu

8.  Report Listing

> The system will generate the “Physical Count Form Report”, listing each account code you selected, the items assigned to that account code, the unit of issue, and the amount of stock on hand for each item. Refer to [Figure 4-12.](#_bookmark88) After printing the report, the system will return to the Adjust Inventory Quantity Menu.

> <span id="_bookmark88" class="anchor"></span>Figure 4-12 Physical Count Form Report Screen Example

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 32%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Inventory File Maintenance Menu

### Unapproved Adjustment Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a report showing the adjustments and items, which have not been approved. Adjustments can be approved using the option 'Approve Adjustments.'

> <span id="_bookmark90" class="anchor"></span>Figure 4-13 Menu Option Path Example

Inventory File Maintenance Menu

9.  Enter Adjustment Number

> Press the Enter key at the Select Adjustment Number: prompt to list all the adjustments, or enter an adjustment number. If you do not know the adjustment number, enter three question marks at the prompt to see a list of available adjustment numbers. You may enter several adjustment numbers. When you have ﬁnished entering adjustment numbers, press the Enter key at the Select Adjustment Number: prompt. [Figure 4-14](#_bookmark91) displays this process.

> <span id="_bookmark91" class="anchor"></span>Figure 4-14 Adjustment Number Screen Example

> Inventory File Maintenance Menu

10. Print Form

> The system will print an “Adjustment Approval Form,” listing each item on adjustment number, the quantity, the cost that the warehouse sells the item, and the value of the item as inventory stock. Refer to [Figure 4-15.](#_bookmark92) The form will also list the type of adjustment and the adjustment amount. The form will have signature blocks for the accountable oﬃcer and the approving oﬃcial. After printing the form, the system will return to the Adjust Inventory Quantity Menu.

> <span id="_bookmark92" class="anchor"></span>Figure 4-15 Adjustment Approval Form Screen Example

>   

>    

>   

>       

>          

>      

>      

>        

> 

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 23%" />
<col style="width: 13%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p> </p>
</blockquote></th>
<th>  </th>
<th></th>
<th> </th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>   </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>      </p>
</blockquote></td>
<td>      </td>
<td>    </td>
<td>     </td>
<td> </td>
</tr>
<tr class="even">
<td><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

>       

>           

>     

>    

>   

>   

Inventory File Maintenance Menu

## Automatic Level Setter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report will print the current inventory levels versus the computer-estimated levels. If you have the manager key for the inventory point, you will have the option to automatically update the current levels to the estimated levels.

> <span id="_bookmark94" class="anchor"></span>Figure 4-16 Menu Option Path Example

### Level Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select whether you want to set the levels for an item or for a group category. Select or deselect items or group categories from your list until you have ﬁnished building your list, then press the Enter key at the Select Group Category: prompt. Refer to [Figure 4-17](#_bookmark96).

> <span id="_bookmark96" class="anchor"></span>Figure 4-17 Automatic Level Setter Screen Example

> Inventory File Maintenance Menu

>         

>     

> 

>      

>       

>     

<table>
<colgroup>
<col style="width: 70%" />
<col style="width: 23%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>   </p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td> </td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

>  

>   

>       

> 

>      

>  

> 

>          

> 

>      

>       

>              

> 

>   

Inventory File Maintenance Menu

### Levels Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will then generate an average, or normal stock level for the items you selected, based on the days between the month you enter at the Start Usage Average with Date (Month Year): prompt and today's date. The system will divide the days in the time range by the number of items used during that time range to determine the average time in which one unit of the item is used. For example, if 90 printer cartridges are used in 180 days, each printer cartridge is equivalent to two days of average use for your inventory point. Enter the number of day's worth of the item that you want as the normal stock level. The system will determine how many units you must maintain at the inventory point to maintain that many day's worth of stock. For example, if you selected thirty days' worth of printer cartridges, an inventory point with an average use of two days per printer cartridge would stock ﬁfteen printer cartridges as the normal stock level.

> Enter the percentage of the normal stock level that you want to be the emergency stock level. For example, if you entered 20 at this prompt, and the normal stock level was ﬁfteen printer cartridges, the system would assign 20% of the normal stock level, or three printer cartridges, as the emergency stock level.

> Enter the percentage of the normal stock level that you want to be the standard reorder point, or the level at which the system will alert you to order more stock. For example, if you entered 50 at this prompt, and the normal stock level was ﬁfteen printer cartridges, the system would assign 50% of the normal stock level, or eight printer cartridges (rounding up), as the standard reorder point.

> Enter the percentage of the normal stock level that you want to be the optional reorder point, or the level at which the system will alert you that you might want to order more stock. For example, if you entered 75 at this prompt, and the normal stock level was ﬁfteen printer cartridges, the system would assign 75% of the normal stock level, or 12 printer cartridges (rounding up), as the standard reorder point. [Figure 4-18](#_bookmark98) displays an example of the process.

> <span id="_bookmark98" class="anchor"></span>Figure 4-18 Levels Set Screen Example

> Inventory File Maintenance Menu

### Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter Y at the Do you want to update the levels in the database?: prompt. The system will print the “Automatic Level Setter Report,” listing the new levels for each item. After printing the report, the system will return to the Inventory File Maintenance Menu. Refer to [Figure 4-19](#_bookmark100).

> <span id="_bookmark100" class="anchor"></span>Figure 4-19 Update Levels Database Screen Example

Inventory File Maintenance Menu

>             

> 

>            

>           

>             

>                

>    

> 

>   

>    

>          

>         

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 36%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>   </p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td> </td>
</tr>
</tbody>
</table>

> 

>  

>         

>           

>        

>       

>   

>    

> Inventory File Maintenance Menu

### Enter/Edit Inventory Item Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to add, delete, or change items in the inventory point record.

> <span id="_bookmark102" class="anchor"></span>Figure 4-20 Menu Option Path Example

### Item Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter an item at the Select Whse Item: prompt. If you do not know the name of the item, enter three question marks at the prompt to see a list of available warehouse items. The system will

Inventory File Maintenance Menu

> list three screens of descriptions of the item and allow you to select information items to edit. At the Select Items: prompt, enter another item to edit or press the Enter key to return to the Inventory File Maintenance Menu. This process is depicted in [Figure 4-22.](#_bookmark106)

> Inventory File Maintenance Menu

> <span id="_bookmark104" class="anchor"></span>Figure 4-21 Item Selection Screen Example

>    

>  

>   

>  

>  

>  

>   

>     

>   

>   

>            

>           

> 

>  

>    

>  

>    

>   

>     

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 29%" />
<col style="width: 12%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p> </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>     </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

>   

>   

>    

>     

Inventory File Maintenance Menu

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 34%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"></th>
<th><blockquote>
<p>    </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p>    </p>
</blockquote></td>
</tr>
</tbody>
</table>

>      

>          

>     

>   

>           

>           

>         

>    

>   

>           

>      

>             

>       

>     

>  

>    

>           

>          

>    

>    

>   

> Inventory File Maintenance Menu

Inventory File Maintenance Menu

## File Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow the user to inquire to VA FileMan ﬁle entries. The option will display selected entry data on the screen for the user to review.

> <span id="_bookmark106" class="anchor"></span>Figure 4-22 Menu Option Path Example

### File Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will list the available ﬁles that you can review. Select a ﬁle. If you enter Yes at the Do You Want To See The Inventory Point Parameters?: prompt, the system will list the inventory data for the inventory point, including its associated cost centers, distribution points and authorized users. Refer to [Figure 4-23.](#_bookmark108)

> <span id="_bookmark108" class="anchor"></span>Figure 4-23 File Review Screen Example

> Inventory File Maintenance Menu

>   

>   

>       

>            

>               

>       

>      

>      

>  

>     

>          

>           

> 

>          

>   

>         

>      

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 17%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

>   

>   

>   

Inventory File Maintenance Menu

### Select Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter an item at the Select Whse Item: prompt. If you do not know the item name or number, enter three question marks at the prompt and the system will list the available items. The system will list the number of units on hand, the last four issues of the item, and other inventory information about the item. Enter another item at the Select Whse Item: prompt to review another inventory item, or press the Enter key to return to the Inventory File Maintenance Menu. The process is depicted in [Figure 4-24](#_bookmark110).

> <span id="_bookmark110" class="anchor"></span>Figure 4-24 Select Warehouse Item Screen Example

> Inventory File Maintenance Menu

Inventory File Maintenance Menu

> THIS PAGE INTENTIONALLY LEFT BLANK

# Chapter 5. Manager for Supply Warehouse Inventory Point Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu contains options for editing warehouse control parameters, calculating/updating due-ins and due-outs, reprinting an issue book picking ticket, and creating and transmitting Integrated Supply Management System (ISMS) code sheets.

## Balance Update Transaction (IM-6)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This ISMS transaction will send a snapshot of the current warehouse inventory balances to ISMS. ISMS will use the balances contained in this transaction to replace the current ISMS balances.

> <span id="_bookmark113" class="anchor"></span>Figure 5-1 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

### Select Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter an item at the Select Whse Item: prompt or press the Enter key to select all items. The system will create a code sheet and send you a MailMan message notifying you of the code sheet and any items not transmitted due to errors. Refer to [Figure 5-2.](#_bookmark115)

> Enter a start time, or press the Enter key at the prompt to request that the system perform the balance automatically. The system will automatically return to the Manager For Supply Warehouse Inventory Point Menu.

> <span id="_bookmark115" class="anchor"></span>Figure 5-2 Select Item Screen Example

> Manager for Supply Warehouse Inventory Point Menu

## Clean Up Old Transactions and Due-Outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option can be used to recalculate the due-outs from the warehouse inventory point for issue book requests not posted.

> The due-out quantity is calculated from issue book request ordered after a speciﬁed date. The date selected should be the date the last issue book request has NOT been posted (probably 6 to 9 months in the past). All issue book request before the speciﬁed date will be made ﬁnal and can no longer be selected for posting. The due-out quantity stored in the inventory point will be updated to the newly calculated due-out quantity. This option should be run at NIGHT since it will lock the transaction (2237) ﬁle, and services will be unable to create ANY orders.

> <span id="_bookmark117" class="anchor"></span>Figure 5-3 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

> Manager for Supply Warehouse Inventory Point Menu

### Enter Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter the last date that you want the system to remove due-outs and make all transactions ﬁnal. Enter when you want the system to begin, or press the Enter key for the system to begin the process immediately. The system will return to the Manager For Supply Warehouse Inventory Point Menu and print the “Outstanding Transaction Report” on the output device you selected. Refer to [Figure 5-4](#_bookmark119) for an example.

> <span id="_bookmark119" class="anchor"></span>Figure 5-4 Finalize Transactions and Update Due-Outs Screen Example

> Manager for Supply Warehouse Inventory Point Menu

## Date Received Delete (for Issue Book Requests)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the user to delete or change the 'DATE RECEIVED' ﬁeld on an issue book request. This ﬁeld is set when an issue book request is ﬁnalized during the Post Issue Book Order option. If the user accidentally speciﬁed that an issue book request was ﬁnal when it was not, they can delete this ﬁeld, and they will then be allowed to post additional items on the issue book request.

> <span id="_bookmark121" class="anchor"></span>Figure 5-5 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

### Enter Transaction Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter a transaction number at the prompt. Refer to [Figure 5-6.](#_bookmark123) If you do not know the transaction number, enter three question marks and the system will list the available transaction numbers. Enter the date that the issue book was ﬁnalized. Enter another item at the Select Control Point Activity Transaction Number: prompt, or press the Enter key to return to the Manager For Supply Warehouse Inventory Point Menu.

> <span id="_bookmark123" class="anchor"></span>Figure 5-6 Enter Transaction Number Screen Example

> Manager for Supply Warehouse Inventory Point Menu

## Distribution Costs Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows users to enter or edit the costing data displayed on the 'History of Distribution Report.'

> <span id="_bookmark125" class="anchor"></span>Figure 5-7 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

### Enter Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter your electronic signature code. Enter the inventory or distribution point at the Select Distribution Inventory Point: prompt. If you do not know the distribution inventory point, enter three question marks and the system will list the available distribution inventory points. Enter the new distribution cost at the Total Cost: prompt. Enter a new distribution inventory point at the Select Distribution Inventory Point: prompt, or press the Enter key to return to the Manager For Supply Warehouse Inventory Point Menu. [Figure 5-8](#_bookmark127) to see the process.

> <span id="_bookmark127" class="anchor"></span>Figure 5-8 Enter Electronic Signature Screen Example

> Manager for Supply Warehouse Inventory Point Menu

> Manager for Supply Warehouse Inventory Point Menu

## Enter/Edit Inventory and Distribution Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow the inventory point manager to edit the control parameters for the inventory point and distribution points. The control parameters include the cost center, fund control points, inventory point users, distribution points, etc.

> <span id="_bookmark129" class="anchor"></span>Figure 5-9 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

### Select Inventory Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter the inventory point. Refer to [Figure 5-10](#_bookmark131) for an example. If you do not know the name of the inventory point, enter three question marks and the system will list the available inventory points. The system will present you with three screens of information about the inventory point you selected. Below each screen will be a set of options you can use to change the inventory point information. Enter another inventory point at the Select a 'Warehouse' Type Inventory Point: prompt or press the Enter key to return to the Manager For Supply Warehouse Inventory Point Menu.

> <span id="_bookmark131" class="anchor"></span>Figure 5-10 Select Inventory Point Screen Example

> Manager for Supply Warehouse Inventory Point Menu

## FMS Code Sheets Rebuild/Retransmit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will rebuild and retransmit the FMS code sheets (IV and SV) from the Generic Code Sheet stack ﬁle.

> <span id="_bookmark133" class="anchor"></span>Figure 5-11 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

### Enter FMS Document Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter the FMS document code at the Select Rejected IV or SV Document to Regenerate: prompt. If you do not know the code, enter a question mark and GIP will display a list of available FMS documents. If the transaction was processed in a previous month, GIP will allow you to process the transaction for the original processing date or today's date. You can select another FMS document at the Select Rejected IV or SV Document to Regenerate: prompt, or press the Enter

> Manager for Supply Warehouse Inventory Point Menu

> key to return to the Manager For Supply Warehouse Inventory Point Menu. Refer to [Figure](#_bookmark135) [5-12](#_bookmark135).

> <span id="_bookmark135" class="anchor"></span>Figure 5-12 Enter MS Document code Screen Example

> 

>      

>      

>       

>  

> 

>         

>  

> 

>  

> 

>         

> 

>           

> 

> 

>            

>            

>              

>              

>           

>        

> 

>          

> Manager for Supply Warehouse Inventory Point Menu

## Group Category Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow the manager of an inventory point to change or remove group categories, which have been set up for the inventory point.

> <span id="_bookmark137" class="anchor"></span>Figure 5-13 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

### Enter Group Category

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter a group category. Group categories are groups of items that allow users to obtain the rates of use of categories of items, e.g., the rate of linen use, energy consumption, etc. If you want to edit an existing group category, but you don't know the name of the category, enter three question marks at the Select Group Category: prompt and the system will list the available categories. You may assign a code to the category. Enter the name of the group category at the Description: prompt. You may enter another group category at the Select Group Category: prompt, or press the Enter key to return to the Manager For Supply Warehouse Inventory Point Menu.

> Manager for Supply Warehouse Inventory Point Menu

## Inventory Control Parameters Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print the control parameters for the inventory point or a selected distribution point. The parameters include the number of items stored in the inventory point, the cost center, fund control points, inventory point users (showing managers), distribution points, etc.

> <span id="_bookmark140" class="anchor"></span>Figure 5-14 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

### Select Distribution Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter a distribution point at the Select Distribution Point: prompt. If you do not know the name of the distribution point, enter three question marks and the system will list the available distribution points. The system will print the inventory parameters for the distribution point you selected, including the inventory point type, the distribution features of the inventory point, the number of standard, On-Demand, and total items stored in the inventory point, the Control Points that request items from the inventory point, the managers and On-Demand Item managers, and other authorized users of the inventory point. Hit the return key at the Select DISTRIBUTION POINT prompt if you wish to see the parameters for the Warehouse inventory point. After printing the report, the system will return to the Manager For Supply Warehouse Inventory Point Menu. [Figure 5-15](#_bookmark142) displays the process.

> <span id="_bookmark142" class="anchor"></span>Figure 5-15 Select Distribution Point Screen Example

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 48%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p>  </p>
</blockquote></th>
<th colspan="3" rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Manager for Supply Warehouse Inventory Point Menu

<table>
<colgroup>
<col style="width: 73%" />
<col style="width: 4%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>     </p>
<p>    </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>   </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>   </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 11%" />
<col style="width: 30%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p> </p>
</blockquote></th>
<th></th>
<th><blockquote>
<p> </p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td> </td>
</tr>
</tbody>
</table>

## Purge History Files Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu contains options allowing the user to purge various history ﬁles, in order to free up disk space.

### History By Cost Center Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option purges the Distribution/Usage History totals by cost center, for the month speciﬁed by the user. This ﬁle is used to create the month-end distribution report used by accounting.

> <span id="_bookmark145" class="anchor"></span>Figure 5-16 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

1.  Purge Data Prompt

> The system will warn you that it will purge the distribution history for the inventory point up to a certain date and ask you to conﬁrm that you want to purge the distribution history. If you answer Yes at the Are You Sure?: prompt, the system will purge the distribution history and return to the Purge History Files Menu. [Figure 5-17](#_bookmark146) is an example.

> <span id="_bookmark146" class="anchor"></span>Figure 5-17 Purge Distribution History Screen Example

> Manager for Supply Warehouse Inventory Point Menu

> Manager for Supply Warehouse Inventory Point Menu

### Receipts History By Item Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will purge the receipts history for items stored in the inventory point. This option should be run once a month and will purge stored data, which is older than 13 months.

> <span id="_bookmark148" class="anchor"></span>Figure 5-18 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

2.  Purge Data Prompt

> The system will warn you that it will purge the receipts history for the inventory point up to a certain date and ask you to conﬁrm that you want to purge the receipts history. Refer to [Figure](#_bookmark149) [5-19](#_bookmark149). If you answer Yes at the Are You Sure?: prompt, the system will purge the receipts history and return to the Purge History Files Menu.

> <span id="_bookmark149" class="anchor"></span>Figure 5-19 Purge Receipts History For All Items Screen Example

> Manager for Supply Warehouse Inventory Point Menu

### Transaction Register Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Figure 5-20](#_bookmark151) Transaction Register Purge option. This option will purge the transaction register for all transactions which aﬀect the inventory point that are older than 13 months. This option should be run once a month in order to free up disk space. The data is used for printing the inventory transaction register report.

> <span id="_bookmark151" class="anchor"></span>Figure 5-20 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

3.  Purge Data Prompt

> The system will warn you that it will purge the register of all transactions that aﬀect the inventory point up to a certain date and ask you to conﬁrm that you want to purge the transaction register. If you answer Yes at the Are You Sure?: prompt, the system will purge the transaction register and return to the Purge History Files Menu. [Figure 5-22](#_bookmark154) illustrates the screen.

> <span id="_bookmark152" class="anchor"></span>Figure 5-21 Purge Register of All Transactions Screen Example

> Manager for Supply Warehouse Inventory Point Menu

### Usage/Distribution Monthly Totals Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will purge the usage/distribution totals for items stored in the inventory point and are older than 13 months. This option should be run once a month in order to free up disk space. The data is used in the 'Usage Reports.'

> <span id="_bookmark154" class="anchor"></span>Figure 5-22 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

4.  Purge Data Prompt

> The system will warn you that it will purge the monthly usage and distribution totals for all the items in the inventory point up to a certain date and ask you to conﬁrm that you want to purge the monthly usage and distribution totals. If you answer Yes at the Are You Sure?: prompt, the system will purge the monthly usage and distribution totals and return to the Purge History Files Menu. [Figure 5-23](#_bookmark155) is an example of the screen.

> <span id="_bookmark155" class="anchor"></span>Figure 5-23 Purge Monthly Usage and Distribution Totals Screen Example

> Manager for Supply Warehouse Inventory Point Menu

## Reprint Posted Picking Ticket

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option can be used by the manager of the warehouse inventory point to reprint a picking ticket from an issue book request posted at a speciﬁc time.

> <span id="_bookmark157" class="anchor"></span>Figure 5-24 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

### Transaction Register Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter which kind of transaction register you want to reprint: an (A)djustment, an (RC) Receipt, an (R) Distribution regular, a (C) Distribution Call-in, an (E) Distribution Emergency, a (U)sage, a (P)hysical count, or (S) for a case cart/instrument kit assembly or disassembly. Enter the speciﬁc transaction you want to reprint. The system will print the picking ticket on the output device that you specify, and return to the Manager For Supply Warehouse Inventory Point Menu.

> [Figure 5-25](#_bookmark159) displays the screen.

> <span id="_bookmark159" class="anchor"></span>Figure 5-25 Select Transaction Register Entry Screen Example

<table style="width:100%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 51%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p> </p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p> </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Manager for Supply Warehouse Inventory Point Menu

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 38%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 

>            

>             

>            

>            

>         

> 

>          

> 

>        

>   

>   

>        

>   

>    

>          

>        

>      

> Manager for Supply Warehouse Inventory Point Menu

> 

>   

>     

>               

>        

>    

>      

>          

>  

>          

>           

>    

>   

>    

>   

>      

>   

>    

> Manager for Supply Warehouse Inventory Point Menu

## Storage Location Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow the manager of an inventory point to change or remove storage locations, which have been set up for the inventory point.

> <span id="_bookmark161" class="anchor"></span>Figure 5-26 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

### Select Storage Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Figure 5-27](#_bookmark163)displays an example of the Select Storage Location screen. Enter the storage location you wish to enter or edit. You may change the name and the expanded description of the storage location. You may enter another storage location at the Select Storage Location: prompt, or press the Enter key to return to the Manager For Supply Warehouse Inventory Point Menu.

> <span id="_bookmark163" class="anchor"></span>Figure 5-27 Select Storage Location Screen Example

## Update Calculated Due-Ins/Outstanding Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a report showing the calculated due-ins or will update the inventory point with the calculated due-ins.

> The calculated due-ins are based on transactions (2237's) and purchase orders, which have not been received in after a speciﬁed date. The date entered should represent the date the last transaction or purchase order was received in (probably no later than 6 to 9 months in the past).

> The report should be run before doing the update so the results can be veriﬁed ﬁrst. The report will show a listing of the calculated due-ins compared to the total due-in quantity stored in the inventory point. If the due-ins disagree, the update should be performed. The report may not agree with the 'Due-In Item Report' since the 'Due-In Item Report' uses the stored values and not the calculated values.

> The update will remove all due-ins stored in the inventory point and reset the due-ins to the

> newly calculated values.

> <span id="_bookmark165" class="anchor"></span>Figure 5-28 Menu Option Path Example

> Manager for Supply Warehouse Inventory Point Menu

### Enter Start Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Figure 5-29](#_bookmark167) depicts an example of Calculated Due-Ins Report Screen. Enter the ﬁrst date that you want the system to update due-ins and outstanding transactions. You may print the report with calculated due-ins, or update due-ins for the inventory point. After printing the report or updating the due-ins, the system will return to the Manager For Supply Warehouse Inventory Point Menu.

> <span id="_bookmark167" class="anchor"></span>Figure 5-29 Calculated Due-Ins Report Screen Example

> Manager for Supply Warehouse Inventory Point Menu

# Chapter 6. Receiving and Distribution Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu lists all the options that manage the receiving of goods in the warehouse, and distributing goods from the warehouse.

## On Demand Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Items in Primary or Secondary Inventory Points may be ﬂagged as On-Demand items. On- Demand items will be identiﬁed by a (D) after the item when listed on many of the reports. Reports will calculate the totals for both the regular items and the On-Demand items independently. Refer to Chapter 9 for more information concerning On-demand Items.

### Display Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a comprehensive item report for a selected item stored in the inventory point or a selected item stored in a distribution point.

> <span id="_bookmark171" class="anchor"></span>Figure 6-1 Menu Option Path Example

> Receiving and Distribution Menu

### Enter Distribution Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter the distribution point at the Select Distribution Point: prompt, enter three question marks to see a list of available distribution points, or press the Enter key to select an item from the main inventory point. Enter an inventory item at the Select SPD Item: prompt. Refer to [Figure](#_bookmark173) [6-2.](#_bookmark173)

> <span id="_bookmark173" class="anchor"></span>Figure 6-2 Enter Distribution Point Screen Example

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 41%" />
<col style="width: 10%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="4"><blockquote>
<p></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="10"><blockquote>
<p>       </p>
<p>   </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"></td>
<td></td>
<td colspan="3"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"></td>
<td></td>
<td colspan="3"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="4"><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 5%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th><blockquote>
<p>Receiving and Distribution Menu</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>   </p>
<p>  </p>
<p>  </p>
<p>  </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>    </p>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>    </p>
</blockquote></td>
</tr>
</tbody>
</table>

### Display Item Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will print a “Display Item Report,” listing the inventory item you selected, the quantity on hand, and the stock levels deﬁned for the item. An example of this screen is in [Figure 6-3.](#_bookmark175) Enter another inventory item at the Select SPD Item: prompt, or press the Enter key to return to the Receiving and Distribution Menu.

> <span id="_bookmark175" class="anchor"></span>Figure 6-3 Display Item Report Example

> Receiving and Distribution Menu

## Display Where An Item Is Stocked

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a report showing which inventory points stock a speciﬁed item. The report will show the distribution point, quantity on hand, unit per issue and within primary and secondary inventory points, whether the item is ﬂagged as On-Demand.

Receiving and Distribution Menu

> <span id="_bookmark177" class="anchor"></span>Figure 6-4 Menu Option Path Example

### Select Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter a warehouse item at the Select Whse Item: prompt, or enter three question marks to see a list of the available items. The system will list the distribution points that have the item you selected, the quantity on hand, and the units per issue. Enter another item at the Select Whse Item: prompt, or press the enter key to return to the Receiving and Distribution Menu. Refer to [Figure 6-5.](#_bookmark179)

> <span id="_bookmark179" class="anchor"></span>Figure 6-5 Select Item Screen Example

> Receiving and Distribution Menu

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 26%" />
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 3%" />
<col style="width: 7%" />
<col style="width: 22%" />
<col style="width: 2%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p> </p>
</blockquote></th>
<th colspan="2"><blockquote>
<p> </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p> </p>
</blockquote></th>
<th colspan="3"><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="9"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="9"><blockquote>
<p>  </p>
</blockquote></td>
</tr>
</tbody>
</table>

## Due-In Item Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a report showing the inventory point items which have outstanding transactions stored (in the inventory point) as due-ins. The report will display the outstanding transaction, associated purchase order, vendor, estimated delivery date or partial numbers not received in, and the due-in quantity.

> The results of this report may not agree with the report generated by the option 'Update Calculated Due-Ins/Outstanding Transactions.' The 'Update' option will print a report showing the calculated due-ins not the stored due-ins. If the 'Update' option is run and the update is performed, the 'Due-In Item Report' option can be run and will agree with the 'Update' report since the 'Update' option will store the calculated due-ins.

> <span id="_bookmark181" class="anchor"></span>Figure 6-6 Menu Option Path Example

Receiving and Distribution Menu

### Enter National Stock Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter the ﬁrst National Stock Number (NSN) that you want to appear on the report, or press the Enter key to list all items with due-ins. The system will print the “Due-in Report,” listing each item that has a due in and a National Stock Number in the range that you speciﬁed. After printing the report, the system will return to the Receiving and Distribution Menu. [Figure 6-7](#_bookmark183) displays the process.

> <span id="_bookmark183" class="anchor"></span>Figure 6-7 Enter National Stock Number Screen Example

> Receiving and Distribution Menu

Receiving and Distribution Menu

## Enter/Edit Items On Distribution Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows a warehouse or primary inventory point to update information on selected items for a distribution point. In order to select a distribution point, the distribution point must not be maintaining their inventory items.

> <span id="_bookmark185" class="anchor"></span>Figure 6-8 Menu Option Path Example

### Enter Distribution Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter a distribution point. Enter an item in the distribution point. The system will display the mandatory source for the item, the unit per issue, the unit per receipt (on purchase orders), and

> Receiving and Distribution Menu

> the conversion factor (from unit per receipt to unit per issue). Refer to [Figure 6-9](#_bookmark187) illustrates the process.

> <span id="_bookmark187" class="anchor"></span>Figure 6-9 Enter Distribution Point Screen Example

### Item Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may edit the unit of issue, the package multiple (the number of units of issue in each package delivered from the vendor), the procurement source, and the unit conversion factor for the source. You can enter multiple procurement sources. Enter the last cost per unit of issue for the item. You can determine this cost from the last purchase order for the item. Enter the normal stock level units of issue of the item. Enter the main storage location of the item. Enter another item at the Select (distribution point) item: prompt, or press the Enter key. Enter another distribution point at the Select Distribution Point: prompt, or press the Enter key to return to the Receiving and Distribution Menu. [Figure 6-10](#_bookmark189) depicts these activities.

> <span id="_bookmark189" class="anchor"></span>Figure 6-10 Edit Information Screen Example

Receiving and Distribution Menu

## Items Flagged 'Kill When Zero' Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a report showing the items in the inventory which are ﬂagged 'delete item when inventory 0.' The report will show the item information, unit per issue, and quantity on- hand.

> <span id="_bookmark191" class="anchor"></span>Figure 6-11 Menu Option Path Example

> Receiving and Distribution Menu

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter the ﬁrst NSN that you want to appear on the report, or press the Enter key to list all items ﬂagged 'Kill When Zero'. The system will print the “Kill When Zero Report,” listing each item that is ﬂagged 'Kill When Zero' and has a National Stock Number in the range that you speciﬁed. After printing the report, the system will return to the Receiving and Distribution Menu. [Figure](#_bookmark193) [6-12](#_bookmark193) illustrates the process.

> <span id="_bookmark193" class="anchor"></span>Figure 6-12 Report Parameters Screen Example

Receiving and Distribution Menu

<table style="width:100%;">
<colgroup>
<col style="width: 20%" />
<col style="width: 23%" />
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="7"><blockquote>
<p> </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>   </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>   </p>
</blockquote></td>
<td colspan="3"></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
<p> </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
<p> </p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>  </p>
</blockquote></td>
<td colspan="5"><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Order Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a catalog of items, which a distribution point can use for ordering and restocking its inventory point.

> <span id="_bookmark195" class="anchor"></span>Figure 6-13 Menu Option Path Example

> Receiving and Distribution Menu

Receiving and Distribution Menu

### Order Form Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Order Form will print a list of items in the current or selected inventory point with blanks for daily ordering. The report is sorted by main storage location and description. At the Select Distribution Point: prompt, select the distribution point for printing the order form or press the Enter key to select the current inventory point. Enter the date of the order form. The system will print an order form for the date you specify, listing each item to be ordered, the standard reorder level, and the normal stock level. After printing the report, the system will return to the Receiving and Distribution Menu. [Figure 6-14](#_bookmark197) is an example of the form.

> <span id="_bookmark197" class="anchor"></span>Figure 6-14 Order Form Screen Example

> Receiving and Distribution Menu

>    

>         

>        

>       

> 

>    

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 11%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p> </p>
</blockquote></th>
<th colspan="2"><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th colspan="4"><blockquote>
<p></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>

>    

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 11%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>  </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="4"><blockquote>
<p></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>

>       

>    

Receiving and Distribution Menu

## Outstanding (Due-Outs) Transaction Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option can be used to recalculate the due-outs from the warehouse inventory point for issue book requests not posted.

> The due-out quantity is calculated from issue book request, which have not been posted to the primary inventory point.

> This option should be run at NIGHT since it is CPU-intensive.

> After the option has calculated the due-outs, a report will print displaying the outstanding issue book request, line item numbers due out, date of the request, primary inventory point making the request, and the outstanding due-out quantity.

> The report will also show the warehouse quantity on-hand and stored quantity due out compared to the total calculated quantity outstanding (due-out). If the quantity due out and the quantity outstanding disagree, the 'Clean Up Old Transactions and Due-Outs' option should be used.

> <span id="_bookmark199" class="anchor"></span>Figure 6-15 Menu Option Path Example

> Receiving and Distribution Menu

### Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report will take a while to run. The developers of the Generic Inventory Package recommend that you run this report at night, when fewer users are using system resources. The system will print the 'Outstanding Transaction Report', listing the National Stock Number of each item with a due out, the description of the item, the quantity on hand, the quantity due- out, and the quantity outstanding. After printing the report, the system will return to the Receiving and Distribution Menu. Refer to [Figure 6-16](#_bookmark201) for an example.

Receiving and Distribution Menu

> <span id="_bookmark201" class="anchor"></span>Figure 6-16 Outstanding Transaction Report Example

>              

>     

>   

>    

>        

>   

>  

>  

>     

> 

> 

>   

>  

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 32%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 15%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="4"><blockquote>
<p> </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

>    

> 

>       

>   

>    

>    

> Receiving and Distribution Menu

## Packaging/Procurement Source Discrepancy Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a report of discrepancies found with items stored in the inventory point. Discrepancies include packaging and unit discrepancies and vendor discrepancies.

> <span id="_bookmark203" class="anchor"></span>Figure 6-17 Menu Option Path Example

### Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will print the 'Packaging Discrepancy Report', listing each item with a discrepancy, its stock number, its description, and the discrepancies for the item. After printing the report, the system will return to the Receiving and Distribution Menu. Refer to [Figure 6-18](#_bookmark205) for an example.

Receiving and Distribution Menu

> <span id="_bookmark205" class="anchor"></span>Figure 6-18 Packaging Discrepancy Report Example

## Post Issue Book Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new List Manager screen should be used by the warehouse to post an issue book distribution order. When posting the order, the quantity on-hand and quantity due out in the warehouse is adjusted, and the quantity on-hand and due-in in the primary is adjusted. At completion of posting, the FMS and ISMS code sheets are automatically created and transmitted to Austin.

> <span id="_bookmark207" class="anchor"></span>Figure 6-19 Menu Option Path Example

> Receiving and Distribution Menu

### Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will print the 'Packaging Discrepancy Report' for the inventory items you selected, the National Stock Number for each item, the item description, the item number, and the unit per issue. After printing the report, the system will return to the Receiving and Distribution Menu. Refer to [Figure 6-20.](#_bookmark209)

> <span id="_bookmark209" class="anchor"></span>Figure 6-20 Packaging Discrepancy Report Example

Receiving and Distribution Menu

> 

>       

>             

>          

> 

>              

> 

>          

> 

>              

> 

>           

> 

>              

> 

> 

>              

> 

>          

> 

>              

> 

>          

> 

>              

> 

>           

> 

>              

> 

> Receiving and Distribution Menu

>            

> 

>              

> 

>           

> 

>              

> 

>            

> 

>              

> 

>          

> 

>              

> 

>   

>    

Receiving and Distribution Menu

## Print Item On Distribution Inventory Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a comprehensive item report of items stored for a selected distribution point.

> <span id="_bookmark211" class="anchor"></span>Figure 6-21 Menu Option Path Example

### Print Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter a distribution point and an output device. The system will print the 'Comprehensive Item Report', [Figure 6-22,](#_bookmark213) listing each item, its description, the item number, and its group category. The report also lists stock levels, reorder points, whether the item is On-Demand, and the available vendors. After printing the report, the system will return to the Receiving and Distribution Menu.

> <span id="_bookmark213" class="anchor"></span>Figure 6-22 Comprehensive Item Report Example

> Receiving and Distribution Menu

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 22%" />
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p> </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th> </th>
<th><blockquote>
<p></p>
</blockquote></th>
<th>  </th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td> </td>
<td><blockquote>
<p></p>
</blockquote></td>
<td>  </td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td> </td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
<p> </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
<p> </p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
<p></p>
</blockquote></th>
<th><p></p>
<p></p></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>   </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Purchase Order Receiving To Inventory Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows users to receive items on the purchase order to the inventory point.

Receiving and Distribution Menu

> <span id="_bookmark215" class="anchor"></span>Figure 6-23 Menu Option Path Example

### Enter Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter your electronic signature code. Enter a purchase order number. If you do not know the purchase order number, enter the ﬁrst part of the number or three question marks and the system will list the available purchase orders. The system will display all the partial shipments not yet received for the purchase order you select. Select a partial date. Refer to [Figure 6-24](#_bookmark217).

> Receiving and Distribution Menu

> <span id="_bookmark217" class="anchor"></span>Figure 6-24 Enter Electronic Signature Screen Example

### Display Receipt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will display the purchase order receipt for the partial shipment, including the line description for the items, the inventory number, the quantity on the purchase order, the conversion factor, the quantity received (after converting the quantity), the average cost, the unit cost (from the purchase order) and the total cost of the item. Enter RO for received order at the Select Item(s): prompt. Refer to [Figure 6-25.](#_bookmark219)

Receiving and Distribution Menu

> <span id="_bookmark219" class="anchor"></span>Figure 6-25 Purchase Order Receipt Screen Example

### Receipt Confirmation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will ask you to conﬁrm that you want to receive the purchase order. The system will record the receipt of the item and transmit a code sheet of the receipt to Austin. The system will display the MailMan message number(s) of the code sheet transmission. Read this message to ensure that the data in the code sheet is accurate. The system will return to the Receiving and Distribution Menu. Refer to [Figure 6-26](#_bookmark221)

> <span id="_bookmark221" class="anchor"></span>Figure 6-26 Receipt Confirmation Screen Example

> Receiving and Distribution Menu

# Chapter 7. Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu contains various reports that allow the user to manage inventory and track distribution of expendable supplies.

## Adjustment Voucher Recap

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a new report, which lists all the adjustments that were made to the inventory point, whether they were quantity or dollar amount changes, and who made them.

> <span id="_bookmark224" class="anchor"></span>Figure 7-1 Menu Option Path Example

> Reports Menu

### Print Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may print all adjustment data, or just a summary report, [Figure 7-2](#_bookmark226). If you print a summary report, the report will list the overall dollar amount additions, and subtractions and diﬀerence for each account. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark226" class="anchor"></span>Figure 7-2 Adjustment Report Screen Example

<table>
<colgroup>
<col style="width: 93%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>    </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>     </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>     </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>     </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

Reports Menu

> If you print all data ([Figure 7-3](#_bookmark227)), the report will list each item in the inventory point that had an adjustment for the month you speciﬁed, the reference number of each adjustment, the eﬀect of each adjustment on stock level and value, and the user that made the adjustment. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark227" class="anchor"></span>Figure 7-3 All Adjustment Data Printed Example

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="6"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> </td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td> </td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td> </td>
</tr>
</tbody>
</table>

> Reports Menu

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 1%" />
<col style="width: 7%" />
<col style="width: 18%" />
<col style="width: 6%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="6"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> </td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td>  </td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="8"><blockquote>
<p>      </p>
<p>   </p>
<p>   </p>
</blockquote></td>
</tr>
</tbody>
</table>

## Availability Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new report lists the stock on hand, the unit costs and some usage history, but isn't as long and time-consuming to generate as the Comprehensive Item Report.

Reports Menu

> <span id="_bookmark229" class="anchor"></span>Figure 7-4 Menu Option Path Example

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Availability Listing will display the current quantity and value of the inventory point items. You may print a summary report, which will only list the total values of each account, or you may print a complete report that lists the quantity and dollar values for every item for the accounts that you deﬁne. You can sort the items in the long report by account code or NSN. [Figure 7-5](#_bookmark231) displays an example.

> <span id="_bookmark231" class="anchor"></span>Figure 7-5 Summary Availability Listing Screen Example

> Reports Menu

>   

>  

>    

> 

>       

> 

> 

>           

>              

> 

>        

>  

> 

>        

>              

> 

>          

>              

> 

>        

>  

> 

>         

>              

> 

>         

>              

> 

>    

Reports Menu

> In the long report, the report will list each item in the accounts you speciﬁed, the quantities, the item values, and the total value for all the items in stock. [Figure 7-6](#_bookmark232) illustrates the report.

> <span id="_bookmark232" class="anchor"></span>Figure 7-6 Long Availability Listing Screen Example

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>  </p>
</blockquote></th>
<th colspan="5"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>  </td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>  </td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> After listing each item, the system will print an 'Availability Listing Report.' If you selected a summary report only, the system will skip the above item listing and just print the 'Availability Listing Report Summary.' This report lists the overall values for each account in the inventory point. After printing the report, the system will return to the Reports Menu. Refer to [Figure](#_bookmark233) [7-7.](#_bookmark233)

> <span id="_bookmark233" class="anchor"></span>Figure 7-7 Availability Listing Report

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 45%" />
<col style="width: 11%" />
<col style="width: 6%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>Reports Menu</th>
<th></th>
<th></th>
<th colspan="2" rowspan="2"></th>
</tr>
<tr class="odd">
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> </td>
<td><blockquote>
<p>   </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>  </p>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>  </p>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>  </p>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>  </p>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>  </p>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>  </p>
<p>   </p>
</blockquote></td>
</tr>
</tbody>
</table>

## Cost Trend Analysis Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new report lists the history of what you’ve paid for warehouse items for a time period that you deﬁne.

> <span id="_bookmark235" class="anchor"></span>Figure 7-8 Menu Option Path Example

Reports Menu

### Long Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will generate the average item cost over the period that you specify at the Start With Date: and End With Date: prompts. You may also limit the report to a range of National Stock Numbers that you specify. You may print a summary report, which lists only the average cost over the entire period, or the long report, which lists an average cost for every month in the range that you speciﬁed. After the system prints one of the reports, it will return to the Reports Menu. [Figure 7-9](#_bookmark237) and [Figure 7-10](#_bookmark238) are examples of the reports:

> <span id="_bookmark237" class="anchor"></span>Figure 7-9 Long Report Example

> Reports Menu

> 

>        

> 

>    

>    

> 

>      

> 

>           

>   

>    

>          

>           

>         

> 

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> </td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

>        

>      

>   

>       

>      

>   

Reports Menu

> <span id="_bookmark238" class="anchor"></span>Figure 7-10 Summary Report Example

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="8"><blockquote>
<p>          </p>
<p>         </p>
<p>          </p>
<p>        </p>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="8"><blockquote>
<p>      </p>
<p>      </p>
<p>       </p>
</blockquote></td>
</tr>
</tbody>
</table>

> Reports Menu

## Days Of Stock On Hand Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new report computes how many days of stock you have on hand based on recent use, and lists all the items of greater or lesser day's worth of stock.

> <span id="_bookmark240" class="anchor"></span>Figure 7-11 Menu Option Path Example

Reports Menu

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will generate the average duration per item over the period that you specify at the Start With Date: and End With Date: prompts. You may also limit the report to a range of National Stock Numbers. Refer to [Figure 7-12.](#_bookmark242)

> <span id="_bookmark242" class="anchor"></span>Figure 7-12 Report Parameters Screen Example

> Reports Menu

### Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will print the 'Days Of Stock On Hand Report', [Figure 7-13,](#_bookmark244) listing the National Stock Number of the item, its description and item number, the total usage of the item during the period, the average days per item, the quantity on hand, how many days of stock your quantity represents, and the value of that stock. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark244" class="anchor"></span>Figure 7-13 Days Of Stock On Hand Report Example

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 24%" />
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 15%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"></th>
<th></th>
<th><blockquote>
<p> </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td> </td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

Reports Menu

## Emergency Stock Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Emergency Stock Report, [Figure 7-15,](#_bookmark248) shows all items that are at or below their deﬁned emergency stock levels. This report has been updated so that it doesn’t show items marked 'kill when zero'.

> <span id="_bookmark246" class="anchor"></span>Figure 7-14 Menu Option Path Example

> Reports Menu

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may limit the report to begin at a particular National Stock Number if you like. Enter an output device. The system will print or display the 'Emergency Stock Level Report,' which lists every item at or below the emergency stock level, grouped by inventory point. The report will list the National Stock Number of the item, its description, the master item number (#MI), the unit per issue, and the stock levels for the item. The report will also list the transaction and the purchase order for the item, the vendor and vendor number, the estimated date received, and the amount due to be received (Due-In). After printing or displaying the report, the system will return to the Reports Menu.

> <span id="_bookmark248" class="anchor"></span>Figure 7-15 Emergency Stock Report Example

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 2%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 6%" />
<col style="width: 29%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th> </th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>   </p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td> </td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 2%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 16%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="4"><blockquote>
<p>   </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

Reports Menu

## Graph Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option creates graphs of frequency of usage and average use of an item that you specify.

> <span id="_bookmark250" class="anchor"></span>Figure 7-16 Menu Option Path Example

> Reports Menu

Reports Menu

### Select Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter a warehouse item. If you do not know the name of the item, enter three question marks and the system will list the available items. The system will create a bar chart of the usage history of the item unless you answer No at the Do You Want a Bar Chart?: prompt. If you answer No at the prompt, the system will create a chart using single lines instead of bars.

> Include zero values if you want the system to compute an actual average use over the last year. Do not include zero values if you want the system to compute an average using only the months in which the item was used. Refer to [Figure 7-17](#_bookmark252)

> <span id="_bookmark252" class="anchor"></span>Figure 7-17 Select Item Screen Example

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 39%" />
<col style="width: 18%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>   </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td> </td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td> </td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Chart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will create a chart depicting the use of the item over the past year, and the average rate of use of the item. Refer to [Figure 7-18.](#_bookmark254) Press the Enter key at the Select Action: prompt. Enter another item at the Select Whse Item: prompt, or press the Enter key to return to the Reports Menu.

> <span id="_bookmark254" class="anchor"></span>Figure 7-18 Use of Item Chart Example

> Reports Menu

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 22%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="9"><blockquote>
<p>    </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td> </td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td> </td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td>  </td>
</tr>
</tbody>
</table>

## History of Distribution Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a report showing the distribution history to or from the inventory point by cost center and by MIS costing section.

> <span id="_bookmark256" class="anchor"></span>Figure 7-19 Menu Option Path Example

Reports Menu

>    

>     

>        

>     

>   

>       

>   

>  

>    

>      

>   

>  

>    

>   

>    

>   

>   

>   

>   

>   

>    

>    

>   

>        

> Reports Menu

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may create a report that lists all distributions to the inventory point, or a report that lists all distributions from the inventory point. Enter the date range that you want the system to search for distributions. You can also have the system separate the costs on the report by MIS costing sections. An MIS costing section allocates the costs for an inventory point for various functions (surgery, medicine, psychiatry, etc.). Refer to [Figure 7-20](#_bookmark258)

> <span id="_bookmark258" class="anchor"></span>Figure 7-20 Report Parameters Screen Example

### Report Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will print the “Distribution Costing Report,”, [Figure 7-21,](#_bookmark260) listing each distribution and its cost. If you printed a report that listed each costing section separately, the system will list the amount per each costing section at the bottom of the report. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark260" class="anchor"></span>Figure 7-21 Distribution Costing Report, Example

Reports Menu

>      

> 

>       

>       

>    

>       

>       

>       

>     

>       

>       

>       

>     

>       

>       

>    

> 

>     

>     

>   

> 

>     

>       

>     

>       

>   

> Reports Menu

## Inactive Items Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists items that haven’t been issued or received in the last 90 days.

> <span id="_bookmark262" class="anchor"></span>Figure 7-22 Menu Option Path Example

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may start the report at a National Stock Number that you deﬁne. The cutoﬀ date you deﬁne is the earliest date that the system will search for a receipt or issue. The system will print the 'Inactive Item Report,' listing each inactive item by National Stock Number, description, last usage, last receipt, the quantity on hand, the value of the stock, and whether or not the item

Reports Menu

> has been marked 'Kill When Zero'. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark264" class="anchor"></span>Figure 7-23 Reports Parameters Screen Example

## Informational Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu lists options that allow IFCAP users to learn about the items stored in an inventory point.

> Reports Menu

### Abbreviated Item Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new report oﬀers a summary of the comprehensive item report, listing the most commonly needed item information. It is a brief, concise alternative to the comprehensive item report.

> <span id="_bookmark267" class="anchor"></span>Figure 7-24 Menu Option Path Example

Reports Menu

1.  Report Parameters

> You can start the report at a NSN that you specify. Refer to [Figure 7-25](#_bookmark268)The system will print the 'Abbreviated Item Report', listing the National Stock Number, its description, the quantity on hand, the unit of issue, and where it is stored. After the system prints the report, the system will return to the Informational Reports Menu.

> <span id="_bookmark268" class="anchor"></span>Figure 7-25 Report Parameters Screen Example

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p></p>
<p>       </p>
<p></p>
<p>   </p>
<p>   </p>
<p>  </p>
<p>   </p>
<p>         </p>
<p>       </p>
<p>       </p>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td> </td>
</tr>
</tbody>
</table>

> Reports Menu

### Comprehensive Item Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report is a long, comprehensive report of every item in an inventory point. The Generic Inventory Package Design Team recommends that you consider running the abbreviated item report instead. If the abbreviated item report does not give you the information you need, run this report at night when fewer users are using system resources.

Reports Menu

> <span id="_bookmark270" class="anchor"></span>Figure 7-26 Menu Option Path Example

>  

>    

>     

>        

>     

>   

>       

>   

>  

>    

>      

>   

>  

>    

>   

>    

>   

>   

>   

>   

>   

>    

>    

>   

>       

>   

> Reports Menu

2.  Report Parameters

> You can start the report at a NSN that you deﬁne. The system will print the 'Comprehensive Item Report' listing the National Stock Number of each item in the inventory point, its name, unit, stock level, quantity data, storage location, and possible vendors for the item. After printing the report, the system will return to the Informational Reports Menu. [Figure 7-27](#_bookmark271) is an example of the process.

> <span id="_bookmark271" class="anchor"></span>Figure 7-27 Reports Parameter Screen Example

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p> </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th> </th>
<th><blockquote>
<p></p>
</blockquote></th>
<th>  </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td> </td>
<td></td>
<td>  </td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td> </td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Reports Menu

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="even">
<td>  </td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
</tr>
</tbody>
</table>

### Conversion Factor Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new report lists the conversion factors for each item. This can be especially useful if items are recorded in diﬀerent places using diﬀerent units of issue. For example, if in the warehouse, items are recorded by box, and in the primary inventory point by each, then there would be a conversion factor of 24 (assuming 24 units per box). This report also lists conversion factors from primary to secondary (e.g., box to case to item). Refer to [Figure 7-28.](#_bookmark273)

> <span id="_bookmark273" class="anchor"></span>Figure 7-28 Menu Option Path Example

> Reports Menu

3.  Report Parameters

> The Conversion Factor Report will display the inventory point items with procurement sources and conversion factors. This report will sort the Warehouse inventory items by National Stock Number and procurement source. You may start the report at a National Stock Number that you deﬁne. The system will print the 'Conversion Factor Report', listing each item by National Stock Number, description, procurement source, unit of issue, and conversion factor. After printing the report, the system will return to the Informational Reports Menu.

Reports Menu

<span id="_bookmark274" class="anchor"></span>Figure 7-29 Report Parameters Screen Example

> 

>        

> 

>    

>    

>   

>    

>          

>      

>     

> 

>      

>     

> 

>   

>    

>          

>      

>     

> 

>        

>      

>      

>     

>        

>      

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Reports Menu</p>
</blockquote></th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>      </p>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><p></p>
<p></p></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Last Procurement Source For Item Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a report showing the items in the inventory point and the last vendor the item was ordered from. The report will display the item information, unit per issue, quantity on-hand, last vendor, purchase order number, unit per receipt, unit price, and quantity ordered.

> <span id="_bookmark276" class="anchor"></span>Figure 7-30 Menu Option Path Example

Reports Menu

4.  Report Parameters

> You may start the report at a National Stock Number that you deﬁne. The system will print the 'Last Procurement Source' report, listing items by National Stock Number, description, quantity on hand, unit per issue, and the last vendor from which the item was procured. After printing the report, the system will return to the Informational Reports Menu.

> <span id="_bookmark277" class="anchor"></span>Figure 7-31 Report Parameters Screen Example

> Reports Menu

### Non-Issuable Stock Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a new report that lists items that have a non-issuable stock status, e.g., recall items, safety hazards, and defects.

> <span id="_bookmark279" class="anchor"></span>Figure 7-32 Menu Option Path Example

Reports Menu

>       

>   

>  

>    

>      

>   

>  

>    

>   

>    

>   

>   

>   

>   

>   

>    

>    

>   

>       

>   

>   

>   

>      

>   

>   

>        

> Reports Menu

5.  Report Parameters

> You may create a report for all items in the inventory point, or select individual items. The system will create a 'Non-issuable Stock Report', listing each item with non-issuable stock by National Stock Number, its description, the quantity on hand, the units per issue, and the non- issuable quantity. After printing the report, the system will return to the Informational Reports Menu. Refer to [Figure 7-33](#_bookmark280)

> <span id="_bookmark280" class="anchor"></span>Figure 7-33 Report Parameters Screen Example

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p>     </p>
<p>   </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>

>   

>    

>          

>      

> 

>       

>    

>   

Reports Menu

### Substitute Listing Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new report lists all available substitutes for an inventory item that you specify.

> <span id="_bookmark282" class="anchor"></span>Figure 7-34 Menu Option Path Example

> Reports Menu

6.  Report Parameters

> The Substitute Listing Report will display inventory items, which have at least one substitute item, deﬁned for the item. The report will sort Warehouse inventory items by National Stock Number. After printing the report, the system will return to the Informational Reports Menu. Refer to [Figure 7-35](#_bookmark283).

> <span id="_bookmark283" class="anchor"></span>Figure 7-35 Report Parameters Screen Example

Reports Menu

## Inventory Sales Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new report lists sales to each primary from the warehouse or to each secondary from a primary. The report provides a summary (dollar value) report or a detailed report (for each item by date and dollar value and quantity).

> <span id="_bookmark285" class="anchor"></span>Figure 7-36 Menu Option Path Example

> Reports Menu

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Inventory Sales Report will display all sales from the warehouse to the primary inventory points. This report is sorted by NSN, distribution point, and date issued. Refer to [Figure 7-37](#_bookmark287). You may start and end the report at National Stock Numbers that you specify. You also may select all distribution points, or individual distribution points. Enter the ﬁrst and last date that you want the report to display. You may print a summary report or a comprehensive report.

> <span id="_bookmark287" class="anchor"></span>Figure 7-37 Report Parameters Screen Example

Reports Menu

### The Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The summary report, [Figure 7-38,](#_bookmark289) will list the total sales to each distribution point. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark289" class="anchor"></span>Figure 7-38 Summary Report Screen Example

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 27%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>   </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### The Comprehensive Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The comprehensive report, [Figure 7-39,](#_bookmark291) will list inventory sales for each item that was sold in the date range that you speciﬁed. The report will list the items by National Stock Number, Description, the date of the sale, the quantity sold, the cost per item, the total value of the sale, and the inventory point that bought the item. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark291" class="anchor"></span>Figure 7-39 Comprehensive Report Example

> Reports Menu

<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 46%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>  </p>
<p>   </p>
<p>        </p>
<p>          </p>
<p>        </p>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>   </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>  </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>   </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>  </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>   </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>  </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 42%" />
<col style="width: 9%" />
<col style="width: 12%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"></th>
<th><blockquote>
<p>Reports Menu</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>   </td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>   </td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>  </td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>   </td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>  </td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p> </p>
<p> </p>
<p> </p>
<p>  </p>
<p>   </p>
</blockquote></td>
</tr>
</tbody>
</table>

> Reports Menu

## Quantity Distribution Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new report lists quantities distributed to primary or secondary inventory points. For an item you specify, this report will tell you the usage of the item over the last twelve months.

> <span id="_bookmark293" class="anchor"></span>Figure 7-40 Menu Option Path Example

Reports Menu

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Quantity Distribution Report will display all sales from the Warehouse to the Primary inventory points. This report is sorted by NSN and date issued. Refer to [Figure 7-41](#_bookmark295). You may start and end the report at speciﬁc National Stock Numbers. The system will print a 'Quantity Distribution Report', listing each item by National Stock Number, description, unit of issue reorder points, and usage over the last twelve months. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark295" class="anchor"></span>Figure 7-41 Report Parameters Screen Example

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 4%" />
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>   </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th> </th>
<th> </th>
<th colspan="2"><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="10"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Reports Menu

## Stock Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report provides a comprehensive review of your current monthly inventory status, including total sales, total receipts, total balance, turnover rate, due-ins, due-outs, non-issuable, and long supply (more than 3 months on hand).

> <span id="_bookmark297" class="anchor"></span>Figure 7-42 Menu Option Path Example

Reports Menu

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Stock Status Report will print a summary of all issues, receipts, and adjustments with the opening and closing balances by account codes. It will calculate the turnover rate, inactive item percent, long supply percent, and non-issuable percent. Enter the month and year that you want the report to print at the Print Stock Status for Month and Year: prompt. At the Enter Inactivity Cutoﬀ Month And Year: prompt, enter the earliest date that the system will look for inactivity for items. The system will print the 'Stock Status Report' in four sections. The ﬁrst section lists the balances for the accounts. The second section lists the receipts and issues among the accounts. The 'Current Data' section of the report lists the value, due-ins and due- outs for each account, inactive items, items of more than 90 days worth of stock, and non- issuable items. After printing the report, the system will return to the Reports Menu. [Figure](#_bookmark299)

> [7-43](#_bookmark299) illustrates the process.

> <span id="_bookmark299" class="anchor"></span>Figure 7-43 Report Parameters Screen Example

> Reports Menu

>          

>      

>            

> 

>        

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

> 

>        

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> 

>        

>       

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 5%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"></th>
<th><blockquote>
<p>  </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td> </td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

>          

>        

>        

Reports Menu

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="9"><blockquote>
<p>       </p>
<p>             </p>
<p>        </p>
<p>        </p>
<p>        </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td> </td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="9"><blockquote>
<p>  </p>
<p>   </p>
</blockquote></td>
</tr>
</tbody>
</table>

## Transaction Register Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows you to print a history of issues, receipts, and adjustments for selected items. New functionality will allow you to print only those items, which are out of balance.

> <span id="_bookmark301" class="anchor"></span>Figure 7-44 Menu Option Path Example

> Reports Menu

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Transaction Register Report will print all activity for speciﬁed items. It will display the open balance, activity, and closing balance. If the calculated closing balance is diﬀerent than the stored inventory value for the current month and year, the current on-hand value will be displayed under the calculated closing balance. Enter the month and year that you want to print the transaction register. You may print only the items with a value discrepancy, or print all the items. Refer to [Figure 7-45](#_bookmark303).

> <span id="_bookmark303" class="anchor"></span>Figure 7-45 Report Parameters Screen Example

Reports Menu

### Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will print the 'Transaction Register Report', [Figure 7-46,](#_bookmark305) listing each item by National Stock Number, item description, transaction identiﬁcation number, transaction amounts, and the eﬀect of the transaction on the inventory balance. Enter a caret (^) at the Select Item Master Number: prompt to return to the Reports Menu.

> <span id="_bookmark305" class="anchor"></span>Figure 7-46 Transaction Register Report Example

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 8%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Reports Menu</p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>   </p>
</blockquote>
<p> </p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>   </p>
<p>      </p>
<p>    </p>
</blockquote></td>
<td><p></p>
<p></p></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>  </p>
</blockquote>
<p> </p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>      </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>      </p>
<p>        </p>
<p>       </p>
<p>  </p>
<p>   </p>
<p>     </p>
<p>    </p>
</blockquote></td>
</tr>
</tbody>
</table>

## Unit Costing Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This new report lists unit costs and average costs of items, which helps you spot items with signiﬁcant diﬀerences between these costs.

> <span id="_bookmark307" class="anchor"></span>Figure 7-47 Menu Option Path Example

Reports Menu

### Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will print a report showing the unit costing for each item stored in the warehouse inventory point, [Figure 7-48.](#_bookmark309) You can use this report to verify the current costing values stored. Enter an output device. The system will print the 'Unit Costing Report', listing each item by National Stock Number, its description, its average cost, its last cost, and its unit cost. The average cost and last cost are deﬁned in the inventory point for each item. The unit cost is deﬁned in the item master ﬁle for the warehouse vendor. If the mandatory source in the item master ﬁle is not the warehouse, the unit cost will print NOT REQ (for not required). Otherwise, the system will display the unit cost. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark309" class="anchor"></span>Figure 7-48 Unit Costing Example

> Reports Menu

## Usage Demand Analysis Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report allows you to look at items that have radically increasing or decreasing usage between two time periods that you deﬁne.

> <span id="_bookmark311" class="anchor"></span>Figure 7-49 Menu Option Path Example

Reports Menu

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At the Compare Usage To Date (Month Year): prompt, [Figure 7-50,](#_bookmark313) enter the reference date against which the system will compare other dates for usage diﬀerences. Enter the beginning month of the date range at the Start Comparison Usage With Date (Month Year): prompt. Enter the last month of the date range at the End Comparison Usage With Date (Month Year): prompt. Enter the minimum number of change that the system will deﬁne as a signiﬁcant usage diﬀerence at the Enter The Percentage Of Change: prompt. You may create a report that lists signiﬁcant usage increases or decreases, but not both in the same report.

> <span id="_bookmark313" class="anchor"></span>Figure 7-50 Report Parameters Screen Example

> Reports Menu

### Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system will create a 'Usage Demand Analysis Report', [Figure 7-51,](#_bookmark315) showing each item that had a signiﬁcant usage decrease or increase, depending on which type of usage change you selected, and the percentage of that change. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark315" class="anchor"></span>Figure 7-51 Usage Demand Analysis Report Example

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 61%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p>   </p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

## Usage Demand Item Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Usage Demand Item Report will show the quantity of items used within a speciﬁed date period.

Reports Menu

> <span id="_bookmark317" class="anchor"></span>Figure 7-52 Menu Option Path Example

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter the ﬁrst and last month of the date range in which you want to see the usage history. You may also limit the report to a range of National Stock Numbers. The system will print the 'Usage Demand Item Report', listing each item by National Stock Number, its description, and the usage for each month in the date range you speciﬁed. After printing the report, the system will return to the Reports Menu. Refer to [Figure 7-53.](#_bookmark319)

> <span id="_bookmark319" class="anchor"></span>Figure 7-53 Report Parameters Example

> Reports Menu

>       

>      

> 

>       

>       

>           

>      

> 

>        

> 

>    

>    

>   

>          

>           

>         

> 

>        

>         

>        

>        

>         

>        

>       

>         

>        

>       

>         

>        

>        

Reports Menu

## Voucher Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists receipts and issues in more detail than the stock status report. This report has been modiﬁed to run faster. The Voucher Summary Report is a listing of all issues, receipts, and adjustments, and the opening and closing balances for each account.

> <span id="_bookmark321" class="anchor"></span>Figure 7-54 Menu Option Path Example

> Reports Menu

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter the month that you want the report to display. The system will print the 'Voucher Summary report', listing each voucher by reference number, its issues, receipts, all other adjustments and the eﬀect of the adjustments on the balances. After printing the report, the system will return to the Reports Menu.

> <span id="_bookmark323" class="anchor"></span>Figure 7-55 Report Parameters Screen Example

<table>
<colgroup>
<col style="width: 73%" />
<col style="width: 14%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p> </p>
<p>      </p>
<p>     </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>   </p>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote>
<p></p></td>
</tr>
</tbody>
</table>

Reports Menu

> 

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

>      

> 

>      

> 

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 30%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

>        

>       

> 

>        

>       

>          

>      

>      

>           

> 

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 17%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Reports Menu

>      

> 

> 

> 

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 29%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>    </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

>        

>       

>          

>      

>      

>           

> 

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

>       

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 29%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Reports Menu

<table style="width:100%;">
<colgroup>
<col style="width: 56%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>     </p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td>     </td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>      </td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

>          

>      

>      

>           

> 

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> </td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>   </p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>    </p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>   </p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>    </p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>    </p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 35%" />
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>    </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

>      

>          

>      

>       

>           

> 

>       

>        

> Reports Menu

# Chapter 8. Menu Outline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter lists each menu option assigned the standard menu conﬁguration for the Warehouse--General Inventory/Distribution Menu. Main menu options are ﬂush left. Subordinate options are indented to the right. For example, if you wanted to use the “Status Of Data” option, you would select “Barcode Manager Menu”, then “Data Manager Menu”, then “Status Of Data”. Refer to [Figure 8-1](#_bookmark325)

> <span id="_bookmark325" class="anchor"></span>Figure 8-1 Menu Option Assigned the Standard Menu Configuration for the Warehouse--General Inventory/Distribution Menu

> Menu Outline

>   

>    

>  

>       

>    

>      

>       

>   

>     

>   

>    

>    

>     

>     

>   

>    

>    

>   

>    

>    

>  

>      

>   

>     

>      

>  

>    

>    

>    

>      

>      

Menu Outline

# Chapter 9. On-Demand Items (ODI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> New On-demand item functionality was added with patch PRC\*5.1\*98. It enables an authorized Inventory manager to diﬀerentiate between standard (routinely used and maintained in the inventory) items and on-demand (rarely or inconsistently used) items that must be on hand in case of an emergency or due to a seasonal need. On-demand items can exist only in Primary and Secondary Inventory Points .

> Data stored in the new On-Demand Flag Audit multiple will be purged whenever the existing background Inventory Automatic Purge is run. The system will delete an entry older than 13 months if the entry is not one of the three most recent entries in the Audit ﬁle. The automatic purge only runs against inventory points that are ﬂagged for inclusion in the automatic purge. Therefore, in order to purge the audit records, you must ﬂag the inventory point housing those items as yes for the automatic purge ﬂag.

> Information addressing the auto-generation of orders containing ODIs is covered in Chapter 2. The suggested orders report generated as part of the auto-generation process was modiﬁed to ﬂag ODIs.

## ODI Flag Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IFCAP Application Coordinator will utilize a new menu option, On-Demand Users Enter/Edit \[PRCP ON-DEMAND USERS\], to enter into the new IFCAP software, those managers identiﬁed by the VISN CLO as authorized to ﬂag items as ODI.

> Refer to the Application Coordinator User’s Guide:<http://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1application_coord.pdf> for further information on this new option.

## Flag an Item as ODI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Those managers authorized to deﬁne an ODI will utilize a new feature under the Special Parameters selection on the Enter/Edit Inventory Item Data option in the existing Inventory File Maintenance menu.

> <span id="_bookmark329" class="anchor"></span>Figure 9-1 Menu Option Path Example

> On-Demand Items (ODI)

>         

>       

>         

>       

>       

>         

>   

>    

>    

>    

>    

>    

>  

>    

>    

>   

>          

>           

>         

>       

>         

>       

>       

>         

>       

On-Demand Items (ODI)

### Select Special Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The manager can identify an item as On-Demand by setting the ﬂag to Yes or change it back to a Standard item by resetting the ﬂag to No. The user must enter a reason for the change when the ﬂag is set to On-Demand or re-set to Standard. Refer to [Figure 9-2](#_bookmark331)

> <span id="_bookmark331" class="anchor"></span>Figure 9-2 On-Demand Flag setting Example

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 16%" />
<col style="width: 30%" />
<col style="width: 11%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p> </p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> On-Demand Items (ODI)

## Reports – Primary & Secondary Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### On Demand Conflict Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new On-Demand Conﬂict Report \[PRCP ON-DEMAND CONFLICT REPORT\] will identify items ﬂagged as On-Demand in the Primary but are not ﬂagged as ODI in the distribution points for the Primary.

> <span id="_bookmark334" class="anchor"></span>Figure 9-3 Menu Option Path Example

1.  Select Distribution Point, Group Category and Item Order

On-Demand Items (ODI)

> <span id="_bookmark335" class="anchor"></span>Figure 9-4 Select Distribution Point Screen Example

> 

>      

>        

>       

>      

>  

> 

>          

> 

>      

>       

>             

> 

>   

>      

>  

> 

>          

> 

>      

>       

>              

>   

>            

> 

>        

>      

> 

>         

>      

> On-Demand Items (ODI)

2.  Display Report

> <span id="_bookmark336" class="anchor"></span>Figure 9-5 On-Demand Conflict Report Example

On-Demand Items (ODI)

### On-Demand Audit Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new On-Demand Audit Activity Report \[PRCP ON-DEMAND AUDIT REPORT\] provides a list of items for which the On-Demand setting has been changed. The values listed include the User that made the change, the date and time that the change occurred, and the text the User entered as their reason for setting the ﬂag.

> <span id="_bookmark338" class="anchor"></span>Figure 9-6 Menu Option Path Example

3.  Select Item(s)

> <span id="_bookmark339" class="anchor"></span>Figure 9-7Select Item Screen Example

> On-Demand Items (ODI)

## Modified Reports – Primary & Secondary Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Abbreviated Item Report \[PRCPRAIR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark342" class="anchor"></span>Figure 9-8 Menu Option Path Example

4.  Select Group Category

> <span id="_bookmark343" class="anchor"></span>Figure 9-9 Select Group Category Screen Example

On-Demand Items (ODI)

5.  Display Report:

> <span id="_bookmark344" class="anchor"></span>Figure 9-10 Abbreviated Item Report Example

> On-Demand Items (ODI)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 17%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p>   </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> </td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>   </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td>  </td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Automatic Level Setter \[PRCPRALS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark346" class="anchor"></span>Figure 9-11 Menu Option Path Example

On-Demand Items (ODI)

6.  Select Item or Category

> <span id="_bookmark347" class="anchor"></span>Figure 9-12 Select Item Category Screen Example

7.  Select Report Type

> <span id="_bookmark348" class="anchor"></span>Figure 9-13 Select Report Type Screen Example

> On-Demand Items (ODI)

>    

>    

>       

>          

> 

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p></p>
<p>9.4.2.3 Display Report</p>
</blockquote></th>
<th colspan="5" rowspan="2"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p><span id="_bookmark349" class="anchor"></span><strong>Figure 9-14 Automatic Level Setter Report Example</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>    </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td> </td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p>    </p>
</blockquote></td>
</tr>
<tr class="odd">
<td>  </td>
<td colspan="2"><blockquote>
<p>    </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td> </td>
<td> </td>
</tr>
</tbody>
</table>

### Comprehensive Item Report \[PRCPRCOM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark351" class="anchor"></span>Figure 9-15 Menu Option Path Example

On-Demand Items (ODI)

8.  Select Group Category

> <span id="_bookmark352" class="anchor"></span>Figure 9-16 Select Group Category Screen Example

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 42%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>          </p>
<p>      </p>
<blockquote>
<p>      </p>
<p>        </p>
<p>      </p>
<p>      </p>
<p>        </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p>     </p>
<p>    </p>
</blockquote></td>
<td><blockquote>
<p>     </p>
<p>    </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

9.  Report Display

> <span id="_bookmark353" class="anchor"></span>Figure 9-17 Comprehensive Item Report Example

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 30%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p> </p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p> </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>  </td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>  </td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 28%" />
<col style="width: 8%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th> </th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>  </td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>  </td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td>  </td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td> </td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 11%" />
<col style="width: 36%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>On-Demand Items (ODI)</p>
</blockquote></th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p> </p>
<p>  </p>
<p> </p>
<blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
<p></p>
<p></p>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
<p> </p>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p>  </p>
<p>  </p>
</blockquote></td>
</tr>
</tbody>
</table>

On-Demand Items (ODI)

### Conversion Factor Report \[PRCPRCFR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark355" class="anchor"></span>Figure 9-18 Menu Option Path Example

10. Select Group Category

> <span id="_bookmark356" class="anchor"></span>Figure 9-19 Select Group Category Screen Example

> On-Demand Items (ODI)

11. Select Report Type

> <span id="_bookmark357" class="anchor"></span>Figure 9-20 Select Report Type Screen Example

12. Display Report

> *See also paragraph [6.3](#due-in-item-report).*

> <span id="_bookmark358" class="anchor"></span>Figure 9-21 Conversion Factor Report Example

### Cost Trend Analysis Report \[PRCPRCTA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists the history of what you’ve paid for items for a time period that you deﬁne.

On-Demand Items (ODI)

> <span id="_bookmark360" class="anchor"></span>Figure 9-22 Menu Option Path Example

13. Select Item and Date

> <span id="_bookmark361" class="anchor"></span>Figure 9-23 Select Item and Date Screen Example

> On-Demand Items (ODI)

14. Display Report

> <span id="_bookmark362" class="anchor"></span>Figure 9-24 Cost Trend Analysis Screen Example

### Days of Stock On Hand Report \[PRCPRSOH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark364" class="anchor"></span>Figure 9-25 Menu Option Path Example

15. Select Type of Report

> <span id="_bookmark365" class="anchor"></span>Figure 9-26 Select Type of Report Screen Example

On-Demand Items (ODI)

> 

>       

>      

>         

> 

>       

>       

>             

>      

>        

>       

>       

>     

>  

>  

>             

>        

>        

>  

>            

>      

>  

>          

>      

>       

>              

>   

> 

>          

>     

>    

> On-Demand Items (ODI)

16. Display Report

> <span id="_bookmark366" class="anchor"></span>Figure 9-27 Days of Stock On Hand Report Example

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th></th>
<th>  </th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td> </td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

### Display Item \[PRCPRITO\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark368" class="anchor"></span>Figure 9-28 Menu Option Path Example

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 9%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th><blockquote>
<p>On-Demand Items (ODI)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>9.4.7.1 Select Item</p>
<p><span id="_bookmark369" class="anchor"></span><strong>Figure 9-29 Select Item Screen Example</strong></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="odd">
<td>      </td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>        </td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>      </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>      </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>       </td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>            </p>
<p>          </p>
<p>  </p>
<p>   </p>
<p>   </p>
<p>   </p>
<p>   </p>
<p>   </p>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>

> 9.4.7.2 Display Report

> <span id="_bookmark370" class="anchor"></span>Figure 9-30 Display Item Report Example

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th>On-Demand Items (ODI)</th>
<th colspan="8"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> </td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="7"><blockquote>
<p>    </p>
</blockquote></td>
</tr>
<tr class="even">
<td><p> </p>
<p>  </p></td>
<td><blockquote>
<p></p>
<p></p>
</blockquote></td>
<td colspan="7"><blockquote>
<p>       </p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>    </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

On-Demand Items (ODI)

### Display Where an Item is Stocked \[PRCPRSTK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *See also paragraph 6.4.*

> <span id="_bookmark372" class="anchor"></span>Figure 9-31 Menu Option Path Example

17. Select Item

> <span id="_bookmark373" class="anchor"></span>Figure 9-32 Select Item Screen Example

18. Display Report

> <span id="_bookmark374" class="anchor"></span>Figure 9-33 Report Screen Example

<table style="width:100%;">
<colgroup>
<col style="width: 5%" />
<col style="width: 38%" />
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p>  </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>  </p>
</blockquote></td>
</tr>
</tbody>
</table>

### Inactive Items Report \[PRCPRIIR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark376" class="anchor"></span>Figure 9-34 Menu Option Path Example

> On-Demand Items (ODI)

19. Select Type

> <span id="_bookmark377" class="anchor"></span>Figure 9-35 Select Type Screen Example

On-Demand Items (ODI)

20. Select Display of Zero Quantity items

> <span id="_bookmark378" class="anchor"></span>Figure 9-36 Select Display of Zero Quantity items Screen Example

21. Display Report

> <span id="_bookmark379" class="anchor"></span>Figure 9-37 Inactive Item Report Example

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 7%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><p>         </p>
<blockquote>
<p>           </p>
<p>         </p>
</blockquote>
<p>      </p>
<blockquote>
<p>        </p>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Inventory Control Parameters Print \[PRCPRINV\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *See also paragraph [5.9.3](#transaction-register-purge).*

> <span id="_bookmark381" class="anchor"></span>Figure 9-38 Menu Option Path Example

> On-Demand Items (ODI)

22. Select Distribution Point

> <span id="_bookmark382" class="anchor"></span>Figure 9-39 Select Distribution Point Screen Example

23. Display Report

> <span id="_bookmark383" class="anchor"></span>Figure 9-40 Report Screen Example

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 3%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>  </p>
</blockquote></th>
<th></th>
<th><blockquote>
<p> </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>   </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>   </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
</tr>
</tbody>
</table>

On-Demand Items (ODI)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 5%" />
<col style="width: 21%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p> </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th>  </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td> </td>
</tr>
</tbody>
</table>

### Print Item on Distribution Inventory Point \[DISTPT^PRCPRCOM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *See also paragraph [6.11.](#purchase-order-receiving-to-inventory-point)*

> <span id="_bookmark385" class="anchor"></span>Figure 9-41 Menu Option Path Example

24. Select Distribution Point

> <span id="_bookmark386" class="anchor"></span>Figure 9-42 Select Distribution Point Screen Example

25. Display Report

> <span id="_bookmark387" class="anchor"></span>Figure 9-43 Comprehensive Item Report Example

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 35%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>On-Demand Items (ODI)</p>
</blockquote></th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p> </p>
<p>  </p>
<p> </p>
<blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
<p> </p>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p>  </p>
<p>  </p>
</blockquote></td>
</tr>
</tbody>
</table>

### Stock Status Report \[PRCPPOLM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark389" class="anchor"></span>Figure 9-44 Menu Option Path Example

26. Select Date

> <span id="_bookmark390" class="anchor"></span>Figure 9-45 Select Data Screen Example

On-Demand Items (ODI)

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>9.4.12.2 Display Report</p>
<p><span id="_bookmark391" class="anchor"></span><strong>Figure 9-46 Stock Status Report Example</strong></p>
</blockquote></th>
<th colspan="4"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>    </p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td> </td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td> </td>
<td></td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p></p>
<p>  </p>
<p>       </p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p></p>
<p>       </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p></p>
<p>       </p>
<p>      </p>
<p> </p>
<p>     </p>
</blockquote></td>
</tr>
</tbody>
</table>

> On-Demand Items (ODI)

>            

>        

>        

>        

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 27%" />
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p>  </p>
</blockquote></th>
<th>  </th>
<th><blockquote>
<p> </p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p> </p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
</tbody>
</table>

>   

>      

>  

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

>       

>          

>        

>            

> 

>   

>        

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"></th>
<th>On-Demand Items (ODI)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 

>        

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> 

>        

>       

>  

>      

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 11%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p> </p>
</blockquote></th>
<th><blockquote>
<p> </p>
</blockquote></th>
<th> </th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p> </p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th> </th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p> </p>
</blockquote></th>
<th> </th>
<th><blockquote>
<p></p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

>   

>      

> On-Demand Items (ODI)

>  

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

>       

>          

>        

>            

> 

<table style="width:100%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p> </p>
<p> </p>
</blockquote></th>
<th><blockquote>
<p></p>
<p></p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 

>        

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> 

>        

>       

>  

On-Demand Items (ODI)

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="12"><blockquote>
<p>     </p>
<p>           </p>
<p>       </p>
<p>       </p>
<p>       </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p>  </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="12"><blockquote>
<p>  </p>
<p>     </p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="12"><blockquote>
<p>  </p>
</blockquote></td>
</tr>
</tbody>
</table>

### Usage Demand Analysis \[PRCPRUS1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark393" class="anchor"></span>Figure 9-47 Menu Option Path Example

27. Select Date, Category and Type of Item

> <span id="_bookmark394" class="anchor"></span>Figure 9-48 Select Date, Category and Type of Item Screen Example

> On-Demand Items (ODI)

>       

>     

>    

>    

>              

>  

> 

>      

>  

> 

>          

>      

>       

>              

>   

>            

> 

>          

> 

>     

>    

>    

>       

>          

> 

>         

>      

> 

>     

>   

>   

On-Demand Items (ODI)

28. Display Report

> <span id="_bookmark395" class="anchor"></span>Figure 9-49 Usage Demand Analysis Screen Example

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>    </p>
</blockquote></th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>    </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="5"> </td>
</tr>
</tbody>
</table>

### Usage Demand Item Report \[PRCPRUSE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark397" class="anchor"></span>Figure 9-50 Menu Option Path Example

> On-Demand Items (ODI)

29. Select Date, Items, Category, Item type and Item Order

> <span id="_bookmark398" class="anchor"></span>Figure 9-51 Select Date, Items, Category, Item type and Item Order Screen Example

On-Demand Items (ODI)

>              

> 

>   

>          

>     

>    

>    

>       

>          

>         

>      

> 

>     

>   

>   

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 18%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>  </th>
<th colspan="10"><blockquote>
<p> </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="6"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="3"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p>9.4.14.2 Display Report</p>
</blockquote></td>
<td colspan="3"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p><span id="_bookmark399" class="anchor"></span><strong>Figure 9-52 Usage Demand Item Report Example</strong></p>
</blockquote></td>
<td colspan="3"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p>    </p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>  </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p>       </p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>    </p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p>  </p>
</blockquote></td>
<td colspan="3"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="3"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="11"><blockquote>
<p></p>
<p>   </p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11"><blockquote>
<p>    </p>
</blockquote></td>
</tr>
</tbody>
</table>

> On-Demand Items (ODI)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 7%" />
<col style="width: 3%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 3%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th colspan="2"> </th>
<th colspan="7"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td> </td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td> </td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 41%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>   </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Barcode Label Modification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The existing Primary/Secondary barcode label has been modiﬁed to support On-Demand functionality. Parameter two used to hold the Mandatory Source (Vendor File 440 IEN). That value was removed from the label and replaced with a ﬁeld that notes the On-Demand Flag value. If an item is On-Demand the value “OD:Y” will display. If the item is not On-Demand the value “OD:N” will be displayed. The pre- existing label is renamed Pre-ODI Prim/Secondary Label and is available for review.

### Primary/Secondary Label

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This label updated an existing nationally released PRIMARY/SECONDARY LABEL. The vendor information at the end of the second line was replaced with the on-demand item indicator. An example of the former label can be seen in the section on PRE-ODI PRIM/SECONDARY LABEL.

> <span id="_bookmark402" class="anchor"></span>Figure 9-53 Label Screen Example

On-Demand Items (ODI)

>     

> 

> 

>    

> 

>     

>  

>    

>     

>      

>    

>    

>    

>   

>    

>     

>   

>     

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 6%" />
<col style="width: 13%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p> </p>
</blockquote></th>
<th colspan="4"><blockquote>
<p> </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>  </p>
</blockquote></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>   </p>
</blockquote></td>
</tr>
</tbody>
</table>

### Pre-ODI Prim/Secondary Label

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This label was created to store a copy of the PRIMARY/SECONDARY LABEL that was resident on your system at the time the On-Demand Items patch PRC\*5.1\*98 was installed. The example shown below is the nationally released version of the PRIMARY/SECONDARY LABEL prior to the On-Demand Item enhancements. If your site had modiﬁed the PRIMARY/SECONDARY LABEL

> On-Demand Items (ODI)

> prior to the release of the On-Demand Items patch PRC\*5.1\*98, your PRE-ODI PRIM/SECONDARY LABEL will diﬀer from the example shown, [Figure 9-54.](#_bookmark404)

> <span id="_bookmark404" class="anchor"></span>Figure 9-54 Pre-ODI Prim/Secondary Label Example

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 6%" />
<col style="width: 13%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p> </p>
</blockquote></th>
<th colspan="4"><blockquote>
<p> </p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>  </p>
</blockquote></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p> </p>
</blockquote></td>
<td colspan="2"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p> </p>
</blockquote></td>
<td><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p> </p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p> </p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p>  </p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p></p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>   </p>
</blockquote></td>
</tr>
</tbody>
</table>

# Chapter 10. The Logistics Data Query Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Logistics Data Query Tool is designed to assist Chief Logistics Oﬃcers; MatANYTOWNl Managers; Purchasing Agents; and members of the Facility Logistics Staﬀ (including Inventory Managers; Supply, Processing, and Distribution (SPD) Technicians; Management Analysts; Warehouse Clerks; or Supply System Analysts). The Query Tool can be used to quickly access, analyze and verify IFCAP and Prosthetics procurement data and display it using a graphical user interface to the VistA data. You can sign-on to VistA, ﬁnd data, view the data, or easily move the data into a Microsoft® Excel® spreadsheet.

> The Query Tool is a Windows software application that acts as a “front-end” to enable you to more easily ﬁnd, display, and export VistA data. The Query Tool is a substitute for the VA FileMan utility program which has traditionally been used to look directly at the MUMPS globals (ﬁles) which store VistA data. The Query Tool enables you to…

- Search for data and display data by a range of dates
- Sort and rearrange the view of the data; display the data in a custom view
- Export the data into a Microsoft Excel spreadsheet ﬁle

> Information on what the Query Tool can do for you can be found in the *Logistics Data Query*

> *Tool User Manual*.

![](ifcap-version-5-1-generic-inventory-user-s-guide/002.png)![](ifcap-version-5-1-generic-inventory-user-s-guide/003.png)![](ifcap-version-5-1-generic-inventory-user-s-guide/004.png)

> \*\<u>NOTE</u>*: The PRCHL LOGISTICS DATA TOOL \[PRCHL GUI\] option has been marked Out of Order with patch PRC\*5.1\*247.

> The Logistics Data Query Tool

> THIS PAGE INTENTIONALLY LEFT BLANK

# Chapter 11. Error Messages and Their Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As you use IFCAP to request goods and services, you will receive errors. Some errors are user errors. User errors mean that IFCAP has determined that the information you have entered in the system is either incomplete or inconsistent, and look like this:

> <span id="_bookmark407" class="anchor"></span>Figure 11-1 Transaction Error Example

> This guide and the online option descriptions should help you with these errors.

> System errors occur when IFCAP fails to function properly. When these errors occur, IFCAP will display the error code. Record the error code and notify your IRM service.

> <span id="_bookmark408" class="anchor"></span>Figure 11-2 System Error Occurred Screen Example

> Error Messages and Their Resolution

> THIS PAGE INTENTIONALLY LEFT BLANK

# Chapter 12. Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>0-9</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>1358</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA Form 1358, <em>Obligation or Change in Obligation</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>2138</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA Form 90-2138, <em>Order for Supplies or Services</em> (ﬁrst page of a VA Purchase Order)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>2139</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA Form 90-2139, <em>Order for Supplies or Services</em> (Continuation) (continuation sheet for Form 90-2138)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>2237</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA Form 90-2237, <em>Request, Turn-in and Receipt for Property or Services</em> (used to request goods and services)</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>A</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>A&amp;MM</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>See</em> <strong>Acquisition and MatANYTOWNl Management</strong> (Service)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>AACS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Automated Allotment Control System—Central computer system developed by VHA to disburse funding from VACO to ﬁeld stations.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>ABC Classiﬁcation</strong></p>
</blockquote></td>
<td><blockquote>
<p>This optional ﬁeld displays the ABC classiﬁcation assigned by the facility inventory managers.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Accounting Technician</strong></p>
</blockquote></td>
<td><blockquote>
<p>Fiscal employee responsible for obligation and payment of received goods and services.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Acquisition and</strong></p>
<p><strong>MatANYTOWNl</strong></p>
<p><strong>Management (Service) (A&amp;MM)</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA Service responsible for contracting and for overseeing the acquisition, storage, and distribution of supplies, services, and equipment used by VA facilities</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Activity Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>The last two digits of the AACS number. It is deﬁned by each station.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>ADP Security Oﬃcer</strong></p>
</blockquote></td>
<td><blockquote>
<p>The individual at your station who is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing ﬁle access.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>A</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><strong>Definition / Discussion</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Agent Cashier</strong></p>
</blockquote></td>
<td><blockquote>
<p>The person in Fiscal Service (often physically located elsewhere) who</p>
<p>makes or receives payments on debtor accounts and issues oﬃcial receipts.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>ALD Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>Appropriation Limitation Department. A set of Fiscal codes which identiﬁes the appropriation used for funding.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Allowance table</strong></p>
</blockquote></td>
<td><blockquote>
<p>Reference table in FMS that provides ﬁnancial information at the level immediately above the AACS, or sub-allowance level.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Amendment</strong></p>
</blockquote></td>
<td><blockquote>
<p>A document which changes the information contained in a speciﬁed Purchase Order. Amendments are processed by the Purchasing &amp; Contracting section of A&amp;MM and obligated by Fiscal Service.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>AMIS</strong></p>
</blockquote></td>
<td>Automated Management Information System.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Application</strong></p>
<p><strong>Coordinator</strong></p>
</blockquote></td>
<td><blockquote>
<p>The individual responsible for the implementation, training and trouble-shooting of a software package within a service. IFCAP requires there be an Application Coordinator designated for Fiscal Service, A&amp;MM Service.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Approve Requests</strong></p>
</blockquote></td>
<td><blockquote>
<p>The use of an electronic signature by a Control Point Oﬃcial to approve a 2237, 1358 or other request form and transmit said request to A&amp;MM/Fiscal.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Approving Oﬃcial</strong></p>
</blockquote></td>
<td><blockquote>
<p>A user that approves reconciliations to ensure that they are correct and complete.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Authorization</strong></p>
</blockquote></td>
<td><blockquote>
<p>Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Authorization Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>The amount of money remaining that can be authorized against the 1358. The service balance minus total authorizations.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>B</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Batch Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Breakout Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>A set of A&amp;MM codes which identiﬁes a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Budget Analyst</strong></p>
</blockquote></td>
<td><blockquote>
<p>Fiscal employee responsible for distributing and transferring funds.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Budget Object Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>Fiscal accounting element that tells what kind of item or service is being procured. Budget object codes are listed in VA Handbook 4671.2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Budget Sort Category</strong></p>
</blockquote></td>
<td><blockquote>
<p>Used by Fiscal Service to identify the allocation of funds throughout their facility.</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>C</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>CC</strong></p>
</blockquote></td>
<td><blockquote>
<p>Credit Charge entry identiﬁer used by FMS and CCS for charges paid to Vendor thru Credit Card payment process.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>CCS</strong></p>
</blockquote></td>
<td><blockquote>
<p>The Credit Card System. This is the database in Austin that processes the credit card information from the external Credit Card Vendor system (currently CitiDirect), and then passes information on to FMS and IFCAP.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>C</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Ceiling Transactions</strong></p>
</blockquote></td>
<td><blockquote>
<p>Funding distributed from Fiscal Service to IFCAP Control Points for</p>
<p>spending. The Budget Analyst initiates these transactions using the Funds Distribution options.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Chief Logistics Oﬃce</strong></p>
<p><strong>(CLO)</strong></p>
</blockquote></td>
<td><blockquote>
<p>The Chief Logistics Oﬃce (CLO) develops and fosters logistics best practices for the Veterans Health Administration. Through the VHA Acquisition Board the CLO develops the annual VHA Acquisition plan that forms the basis for VHA’s acquisition strategy. This strategy seeks to procure high quality health care products and services in the most cost eﬀective manner. This includes the attainment of socio-economic procurement goals. The CLO also develops and implements a comprehensive plan for the standardization of healthcare supplies and equipment. This includes the development and administration of clinical product user groups.</p>
<p>The CLO is also responsible for developing improvements to supply chain management within VHA. This includes the establishment and monitoring of logistics benchmarking data. The CLO serves as liaison for logistics staﬀ in each of the 21 VISNs.</p>
<p>The head of CLO is the <strong>Chief Prosthetics and Clinical Logistics Oﬃcer</strong></p>
<p><strong>(CPCLO)</strong>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Chief Prosthetics and Clinical Logistics Oﬃcer (CPCLO)</strong></p>
</blockquote></td>
<td><blockquote>
<p>The oﬃcial in charge of the VHA <strong>Chief Logistics Oﬃce (CLO)</strong>, also called the Clinical Logistics Oﬃce.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>CLA</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>See</em> <strong>Clinical Logistics Analyst</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>C</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Classiﬁcation of</strong></p>
<p><strong>Request</strong></p>
</blockquote></td>
<td><blockquote>
<p>An identiﬁer a Control Point can assign to track requests that fall into</p>
<p>a category (<em>e.g.</em>, Memberships, Replacement Parts, Food Group III).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Clinical Logistics</strong></p>
<p><strong>Analyst (CLA)</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>Logistics</em> refers to how resources are acquired, transported and stored along the supply chain. By having an eﬃcient supply chain and proper logistical procedures, an organization can cut costs and increase eﬃciency. <em>Clinical logistics</em> refers speciﬁcally to resources used for clinical purposes. A CLA is a person who examines</p>
<p>processes, methods and data for clinical logistics operations.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Clinical Logistics Oﬃce</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>See</em> <strong>Chief Logistics Oﬃce (CLO).</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Clinical Logistics</strong></p>
<p><strong>Report Server (CLRS)</strong></p>
</blockquote></td>
<td><blockquote>
<p>The CLRS project allows the extraction of selected procurement and inventory data from VHA facilities to a centralized Clinical Logistics Report Server. The server supports the collection, tracking, and reporting of National Performance Measures, assisting the Under Secretary for Health (USH) in evaluating facility performance in the areas of consolidation of high tech equipment, standardization, socioeconomic goal accomplishment, acquisition, and inventory management.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>CLRS</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>See</em> <strong>Clinical Logistics Report Server (CLRS)</strong>.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Common Numbering SANYTOWNs</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a pre-set sANYTOWNs of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinators establish the Common Numbering SANYTOWNs used by each facility.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Control Point</strong></p>
</blockquote></td>
<td><blockquote>
<p>Financial element, existing ONLY in IFCAP, which corresponds to a set of elements in FMS that include the Account Classiﬁcation Code (ACC) and deﬁne the Sub-Allowance on the FMS system. Used to permit the tracking of monies to a speciﬁed service, activity or purpose from</p>
<p>an Appropriation or Fund.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>C</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Control Point Clerk</strong></p>
</blockquote></td>
<td><blockquote>
<p>The user within the service who is designated to input requests</p>
<p>(2237s) and maintain the Control Point records for a Service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Control Point Oﬃcial</strong></p>
</blockquote></td>
<td><blockquote>
<p>The individual authorized to expend government funds for ordering of supplies and services for their Control Point(s). This person has all of the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Control Point Oﬃcial’s</strong></p>
<p><strong>Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>A running record of all the transactions generated and approved for a Control Point from within IFCAP and also. Eﬀects changes to the control point that are initiated directly from within the FMS system. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a speciﬁed ﬁscal quarter.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Control Point Requestor</strong></p>
</blockquote></td>
<td><blockquote>
<p>The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. This user can only view or edit their own requests. A Control Point Clerk or Oﬃcial must make these requests permanent before they can be approved and transmitted to A&amp;MM.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Cost Center</strong></p>
</blockquote></td>
<td><blockquote>
<p>Cost Centers are unique numbers which deﬁne a service. One cost center must be attached to every Fund Control Point. This enables costs to be captured by service. Cost centers are listed in VA</p>
<p>Handbook 4671.1.</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>D</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Date Committed</strong></p>
</blockquote></td>
<td><blockquote>
<p>The date that you want IFCAP to commit funds to the purchase.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Default</strong></p>
</blockquote></td>
<td><blockquote>
<p>A suggested response that is provided by the system.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Deﬁciency</strong></p>
</blockquote></td>
<td><blockquote>
<p>When a budget has obligated and expended more than it was funded.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Delinquent Delivery</strong></p>
<p><strong>Listing</strong></p>
</blockquote></td>
<td><blockquote>
<p>A listing of all the Purchase Orders that have not had all the items received by the Warehouse on IFCAP. It is used to contact the vendor for updated delivery information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>D</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Delivery Order</strong></p>
</blockquote></td>
<td><blockquote>
<p>An order for an item that the VA purchases through an established</p>
<p>contract with a vendor who supplies the items.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Direct Delivery</strong></p>
<p><strong>Patient</strong></p>
</blockquote></td>
<td><blockquote>
<p>A patient who has been designated to have goods delivered directly to him/her from the vendor.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Discount Item</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>E</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>EDI</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>See</em> <strong>Electronic Data Interchange (EDI).</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>EDI Vendor</strong></p>
</blockquote></td>
<td><blockquote>
<p>A vendor with whom the VA has negotiated an arrangement to submit, accept and ﬁll orders electronically.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>EDI X12</strong></p>
</blockquote></td>
<td><blockquote>
<p>“X12” is the U.S. standard ANSI ASC X12, which is the predominant standard used in North America. Thus, “EDI X12” refers to electronic data interchanges which meet the X12 standard. Also seen as “X12 EDI.”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Electronic Data Interchange (EDI)</strong></p>
</blockquote></td>
<td><blockquote>
<p>Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Electronic Signature</strong></p>
</blockquote></td>
<td><blockquote>
<p>The electronic signature code replaces the written signature on all IFCAP documents used within your facility. Documents going oﬀ- station will require a written signature as well.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Expenditure Request</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).</p>
</blockquote></td>
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
<th colspan="2"><blockquote>
<p><strong>F</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>FCP</strong></p>
</blockquote></td>
<td><blockquote>
<p>Fund Control Point (see Control Point).</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Glossary

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Federal Tax ID</strong></p>
</blockquote></th>
<th><blockquote>
<p>A unique number that identiﬁes your station to the Internal Revenue</p>
<p>Service.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>FileMan</strong></p>
</blockquote></td>
<td><blockquote>
<p>The FileMan modules are the “building blocks” for all of VistA. FileMan includes both a database management system (DBMS) and user interface.</p>
<p><em>Source:</em> <a href="http://www.hardhats.org/fileman/FMmain.html">http://www.hardhats.org/ﬁleman/FMmain.html</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Fiscal Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidations submitted against the obligation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Fiscal Quarter</strong></p>
</blockquote></td>
<td><blockquote>
<p>The ﬁscal year is broken into four three month quarters. The ﬁrst ﬁscal quarter begins on October 1.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Fiscal Year</strong></p>
</blockquote></td>
<td><blockquote>
<p>Twelve month period from October 1 to September 30.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>FMS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Financial Management System, the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides for ﬂexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>FOB</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Freight on Board.</strong> An FOB of “Destination” means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of “Origin” means the Vendor has paid shipping costs directly to the shipper and then will include them on their Invoice.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>FPDS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Federal Procurement Data System.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>FTEE</strong></p>
</blockquote></td>
<td><blockquote>
<p>Full Time Employee Equivalent. An FTEE of 1 stands for 1 ﬁscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned an FTEE of 0.5, as would a full-time employee that worked for half of a year.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Fund Control Point</strong></p>
</blockquote></td>
<td><blockquote>
<p>IFCAP accounting element that is not used by FMS. See also control point.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Glossary

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Funds Control</strong></p>
</blockquote></th>
<th><blockquote>
<p>A group of Control Point options that allow the Control Point Clerk</p>
<p>and/or Oﬃcial to maintain and reconcile their funds.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Funds Distribution</strong></p>
</blockquote></td>
<td><blockquote>
<p>A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>G</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>GBL</strong></p>
</blockquote></td>
<td><blockquote>
<p>Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of $250.00.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>GL</strong></p>
</blockquote></td>
<td><blockquote>
<p>General Ledger.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Globals</strong></p>
</blockquote></td>
<td><blockquote>
<p>Globals are variables which are automatically and transparently stored on disk and persist beyond program, routine, or process completion. Globals are used exactly like ordinary variables, but with the caret character preﬁxed to the variable name.</p>
<p>Globals are stored in highly structured data ﬁles by MUMPS, and accessed only as MUMPS globals. VistA ﬁle deﬁnitions and data are</p>
<p>both stored in globals.</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>I</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Identiﬁcation Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>A computer-generated number assigned to a code sheet.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Imprest Funds</strong></p>
</blockquote></td>
<td><blockquote>
<p>Monies used for cash or 3<sup>rd</sup> party draft purchases at a VA facility.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Integrated Supply Management System (ISMS)</strong></p>
</blockquote></td>
<td><blockquote>
<p>ISMS is the system which replaced LOG I for Expendable Inventory.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>ISMS</strong></p>
</blockquote></td>
<td><blockquote>
<p>See Integrated Supply Management System.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>I</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Item File</strong></p>
</blockquote></td>
<td><blockquote>
<p>A listing of items speciﬁed by A&amp;MM service as being purchased</p>
<p>repetitively. This ﬁle maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Item History</strong></p>
</blockquote></td>
<td><blockquote>
<p>Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Item Master Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>A computer generated number used to identify an item in the Item File.</p>
</blockquote></td>
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
<th colspan="2"><blockquote>
<p><strong>J</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Justification</strong></p>
</blockquote></td>
<td><blockquote>
<p>A written explanation of why the Control Point requires the items requested. Adequate justiﬁcation must be given if the goods are</p>
<p>being requested from other than a mandatory source.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>K</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Kernel</strong></p>
</blockquote></td>
<td><blockquote>
<p>The Kernel is the software “scaﬀolding” that supports all VistA applications. The Kernel system permits any VistA software application to run without modiﬁcation to its base structure no matter what hardware or software vendor the application was built on.</p>
<p>The Kernel includes a number of management tools including device, menu, programming, operations, security/auditing, task, user, and system management. Its framework provides a structurally sound computing environment that permits controlled user access, menus for choosing various computing activities, the ability to schedule tasks, application development tools, and numerous other management and operation tools.</p>
<p><em>Source:</em> <a href="http://hardhats.org/kernel/KRNmain.html">http://hardhats.org/kernel/KRNmain.html</a></p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>L</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Liquidation</strong></p>
</blockquote></td>
<td><blockquote>
<p>The amount of money posted to the 1358 or Purchase Order as a payment to the vendor. They are processed through payment/invoice tracking.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>LOG I</strong></p>
</blockquote></td>
<td><blockquote>
<p>LOG I is the name of the Logistics A&amp;MM computer located at the Austin Automation Center. This system continues to support the</p>
<p>Consolidated Memorandum of Receipt.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>M</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>M</strong></p>
</blockquote></td>
<td><blockquote>
<p>The Massachusetts General Hospital Utility Multi-Programming System, or alternatively M, is a programming language originally created for use in the healthcare industry. M is designed to make writing database-driven applications easy while simultaneously making eﬃcient use of computing resources. The most outstanding, and unusual, design feature of M is that database interaction is transparently built into the language. Many parts of VistA are written in M.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>MailMan</strong></p>
</blockquote></td>
<td><blockquote>
<p>Mailman is an integrated data channel in VistA for the distribution of:</p>
</blockquote>
<ul>
<li><p>Patches (<em>Kernel Installation and Distribution System</em> or <em>KIDS</em></p></li>
</ul>
<blockquote>
<p>builds)</p>
</blockquote>
<ul>
<li><p>Software releases (<em>KIDS</em> builds)</p></li>
<li><p>Computer-to-computer communications (HL7 transfers, Servers, etc.)</p></li>
<li><p>Person-to-person messaging (email)</p></li>
</ul>
<blockquote>
<p><em>Source:</em> <a href="http://www.hardhats.org/cs/mailman/MMmain.html">http://www.hardhats.org/cs/mailman/MMmain.html</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Mandatory Source</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Federal Agency that sells supplies and services to the VA, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>MSC Conﬁrmation</strong></p>
<p><strong>Message</strong></p>
</blockquote></td>
<td><blockquote>
<p>A MailMan message generated by the Austin Message Switching Center that assigns an FMS number to an IFCAP transmission of documents.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>MUMPS</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>See</em> <strong>M.</strong></p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>O</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Obligation</strong></p>
</blockquote></td>
<td><blockquote>
<p>The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of an Order.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Obligation (Actual)</strong></p>
<p><strong>Amount</strong></p>
</blockquote></td>
<td><blockquote>
<p>The actual dollar ﬁgure obligated by Fiscal Service for a Purchase Order. The Control Point’s records are updated with actual cost</p>
<p>automatically when Fiscal obligates the document on IFCAP.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>O</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Obligation Data</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Control Point option that allows the Control Point Clerk and/or</p>
<p>Budget Analyst to enter data not recorded by IFCAP.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Obligation Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>The 6 character number assigned to orders, requisitions and 1358s. (ie C preﬁx number that Fiscal Service assigns to the 1358.)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Option</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Vista Option is an application component deﬁned in VA Kernel to control user and remote server access to VistA applications. Options can appear on menu “trees” of options, through which the user navigates to execute application software. Types of options include menu (to allow grouping of options); edit (to edit application ﬁles via VA FileMan); inquire (to query the database via VA FileMan); print (to execute reports via VA FileMan); run routine (to execute custom application software); server (to process remote procedure calls via MailMan); and Broker (to process GUI remote procedure calls via Kernel Broker).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Organization Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>Accounting element functionally comparable to Cost Center, but used to organize purchases by the budget that funded them, not the purposes for spending the funds.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Outstanding 2237</strong></p>
</blockquote></td>
<td><blockquote>
<p>A&amp;MM report that lists all the IFCAP generated 2237s pending action in A&amp;MM.</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>P</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Partial</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Partial Date</strong></p>
</blockquote></td>
<td><blockquote>
<p>The date that a warehouse clerk created a receiving report for a shipment.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PAT Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>Pending Accounting Transaction number – the primary FMS reference number. See also Obligation Number.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>P</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Personal Property</strong></p>
<p><strong>Management</strong></p>
</blockquote></td>
<td><blockquote>
<p>A section of A&amp;MM Service responsible for screening all requests for</p>
<p>those items available from a Mandatory Source, VA Excess or Bulk sale. They also process requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>POA</strong></p>
</blockquote></td>
<td><blockquote>
<p>Purchase Order Acknowledgment. The message received electronically from an EDI vendor acknowledging the placement of an order.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PPM</strong></p>
</blockquote></td>
<td><blockquote>
<p>Personal Property Management, now referred to at most sites as Acquisition and MatANYTOWNl Management Service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Program Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>Accounting element that identiﬁes the VA initiative or program that the purchase will support.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Prompt PaymentTerms</strong></p>
</blockquote></td>
<td><blockquote>
<p>The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Purchase Card</strong></p>
</blockquote></td>
<td><blockquote>
<p>A card, similar to a credit card, that Purchase Card Users use to make purchases. Purchase Cards are not credit cards but debit cards that spend money out of a deposited balance of VA funds.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Purchase Card Coordinator</strong></p>
</blockquote></td>
<td><blockquote>
<p>A person authorized by a VA station to monitor and resolve delinquent purchase card orders, help VA services record, edit and approve purchase card orders in a timely manner, assign purchase cards to IFCAP users, and monitor the purchase card expenses of VAMC services.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Purchase Card Orders</strong></p>
</blockquote></td>
<td><blockquote>
<p>Orders funded by a purchase card.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Purchase Card User</strong></p>
</blockquote></td>
<td><blockquote>
<p>A person who uses a purchase card. Purchase Card Users are responsible for recording their purchase card orders in IFCAP.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>P</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Purchase History Add</strong></p>
<p><strong>(PHA)</strong></p>
</blockquote></td>
<td><blockquote>
<p>Information about purchase orders which is automatically sent to</p>
<p>Austin for archiving. This same transaction is also used to send a PO for EDI processing.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Purchase History Modify (PHM)</strong></p>
</blockquote></td>
<td><blockquote>
<p>Information about amendments which is automatically sent to Austin for archiving.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Purchase Order</strong></p>
</blockquote></td>
<td><blockquote>
<p>A government document authorizing the purchase of the goods or services at the terms indicated.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Purchase Order Acknowledgment</strong></p>
</blockquote></td>
<td><blockquote>
<p>Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Purchase Order Status</strong></p>
</blockquote></td>
<td><blockquote>
<p>The status of completion of a purchase order (e.g., Pending Contracting Oﬃcer’s Signature, Pending Fiscal Action, Partial Order Received, etc.).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Purchasing Agents</strong></p>
</blockquote></td>
<td><blockquote>
<p>A&amp;MM employees legally empowered to create purchase orders to obtain goods and services from commercial vendors.</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>Q</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Quarterly Report</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Control Point listing of all transactions (Ceilings, Obligations, Adjustments) made against a Control Point’s Funds.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Quotation for Bid</strong></p>
</blockquote></td>
<td><blockquote>
<p>Standard Form 18. Used by Purchasing Agents to obtain written bids from vendors. May be created automatically and transmitted electronically within the Purchasing Agent’s module.</p>
</blockquote></td>
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
<th colspan="2"><blockquote>
<p><strong>R</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Receiving Report</strong></p>
</blockquote></td>
<td><blockquote>
<p>The VA document used to indicate the quantity and dollar value of</p>
<p>the goods being received.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>R</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Reconciliation</strong></p>
</blockquote></td>
<td><blockquote>
<p>Comparing of two records to validate IFCAP Purchase Card orders.</p>
<p>Purchase Card Users compare IFCAP generated purchase card order data with the CC transaction sent from the CCS system in Austin.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Reference Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>Also known as the Transaction Number. The computer generated number that identiﬁes a request. It is comprised of the: Station Number-Fiscal Year-Quarter - Control Point – 4-digit Sequence Number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Repetitive (PR Card)</strong></p>
<p><strong>Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>See <strong>Item Master Number</strong>.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Repetitive Item List</strong></p>
<p><strong>(RIL)</strong></p>
</blockquote></td>
<td><blockquote>
<p>A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate 2237 requests from the list. A RIL can be created by using the Auto-Generate feature within the Inventory portion of the package.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Requestor</strong></p>
</blockquote></td>
<td><blockquote>
<p>See <strong>Control Point Requestor</strong>.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Requisition</strong></p>
</blockquote></td>
<td><blockquote>
<p>An order from a Government vendor.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Running Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a speciﬁed</p>
<p>ﬁscal quarter.</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>S</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Section Request</strong></p>
</blockquote></td>
<td><blockquote>
<p>A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Oﬃcial.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Service Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorizations created by the service.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>S</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>SF-18</strong></p>
</blockquote></td>
<td><blockquote>
<p>Request for Quotation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>SF-30</strong></p>
</blockquote></td>
<td><blockquote>
<p>Amendment of Solicitation/Modiﬁcation of Contract.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Short Description</strong></p>
</blockquote></td>
<td><blockquote>
<p>A phrase which describes the item in the Item Master ﬁle. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Site Parameters</strong></p>
</blockquote></td>
<td><blockquote>
<p>Information (such as Station Number, Cashier’s address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter ﬁle.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Sort Group</strong></p>
</blockquote></td>
<td><blockquote>
<p>An identiﬁer a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Sort Order</strong></p>
</blockquote></td>
<td><blockquote>
<p>The order in which the budget categories will appear on the budget distribution reports.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Special Remarks</strong></p>
</blockquote></td>
<td><blockquote>
<p>A ﬁeld on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This ﬁeld can be printed on the Purchase Order.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Stacked Documents</strong></p>
</blockquote></td>
<td><blockquote>
<p>The purchase orders, receiving reports, and 1358s which are sent electronically to Fiscal and stored in a ﬁle for printing at a later time rather than being printed immediately.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Standard Items</strong></p>
</blockquote></td>
<td><blockquote>
<p>Items in the inventory which are routinely used and tracked. Items that do not meet the criteria of being On-Demand.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Status of Funds</strong></p>
</blockquote></td>
<td><blockquote>
<p>Fiscal’s on-line status report of the monies available to a Control Point. FMS updates this information automatically.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Sub-control Point</strong></p>
</blockquote></td>
<td><blockquote>
<p>A user deﬁned assignment of all or part of a ceiling transaction to a speciﬁc category (sub-control point) within a Control Point, Transactions can then be posted against this sub-control point and a report can be generated to track use of speciﬁed funding within the</p>
<p>overall control point..</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>S</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Sub-cost Center</strong></p>
</blockquote></td>
<td><blockquote>
<p>A subcategory of Cost Center. IFCAP will not utilize a ‘sub-cost center’</p>
<p>ﬁeld, but will send FMS the last two digits of the cost center as the FMS ‘sub-cost center’ ﬁeld.</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>T</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Tasked Job</strong></p>
</blockquote></td>
<td><blockquote>
<p>A job, usually a printout that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>TDA</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>See</em> <strong>Transfer of Disbursing Authority</strong>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Total Authorizations</strong></p>
</blockquote></td>
<td><blockquote>
<p>The total amount of the authorizations created for the 1358 obligation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Total Liquidations</strong></p>
</blockquote></td>
<td><blockquote>
<p>The total amount of the liquidations against the 1358 obligation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Transaction Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>The number of the transaction that funded a Control Point (See Budget Analyst User’s Guide). It consists of the Station Number – Fiscal Year – Quarter – Control Point – Sequence Number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Transfer of Disbursing Authority</strong></p>
</blockquote></td>
<td><blockquote>
<p>The method used to allocate funds to a VA facility.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Transmission Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>A sequential number given to a data string when it is transmitted to the Austin DPC; used for tracking message traﬃc.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Type Code</strong></p>
</blockquote></td>
<td><blockquote>
<p>A set of A&amp;MM codes that provides information concerning the vendor size and type of competition sought on a purchase order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>U</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Unit of Issue</strong></p>
</blockquote></td>
<td><blockquote>
<p>A description of the quantity/packaging combination in which the item is issued to the end user; it may be diﬀerent from the Unit of Purchase, which is the combination used when the item is procured from the vendor. For example, a vendor may sell an item in cases of 24 cans, but the end user receives individual cans from that case.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Unit of Purchase</strong></p>
</blockquote></td>
<td><blockquote>
<p>A description of the quantity/packaging combination in which VA purchases the item from the vendor; it may be diﬀerent from the Unit of Issue, which is the combination used to actually issue the item to the end user. See also Unit Conversion Factor.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Unit Conversion Factor</strong></p>
</blockquote></td>
<td><blockquote>
<p>A number which expresses the ratio between the unit of measure and the unit of issue. Among other things, the conversion factor (which is part of the vendor data) is used at order release to calculate the due- ins and due-outs. Supply stations receive the conversion factor at the time of order release and use it to translate the order quantities into supply station amounts. If an item is procured, stocked and issued</p>
<p>using the same units, then the conversion factor would be 1.</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p><strong>V</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Vendor ﬁle</strong></p>
</blockquote></td>
<td><blockquote>
<p>An IFCAP ﬁle of vendor information solicited by the facility. This ﬁle contains ordering and billing addresses, contract information, FPDS information and telephone numbers. The debtor’s address may be drawn from this ﬁle, but is maintained separately. If the desired vendor is not in the ﬁle, contact A&amp;MM Service to have it added.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Vendor ID Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>The ID number assigned to a vendor by the FMS Vendor unit.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VRQ</strong></p>
</blockquote></td>
<td><blockquote>
<p>FMS Vendor Request document. When a new vendor is added to IFCAP a VRQ message is sent electronically to the Austin FMS Vendor unit to determine if the vendor exists in the central vendor system. If the vendor is not in the system, Austin will conﬁrm information and establish the vendor in the central ﬁle. If vendor exists in central ﬁle</p>
<p>already, Austin will verify the data. <em>See also</em> <strong>VUP</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Glossary

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>V</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VUP</strong></p>
</blockquote></td>
<td><blockquote>
<p>FMS Vendor Update Message. This message is sent electronically</p>
<p>from the FMS system to ALL IFCAP sites to ensure that the local vendor ﬁle contains the same data as the central vendor ﬁle in Austin. This message will contain the FMS Vendor ID for the vendor and also</p>
<p>the Alternate Address Indicator if applicable. <em>See also</em> <strong>VRQ</strong>.</p>
</blockquote></td>
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
<th colspan="2"><blockquote>
<p><strong>X</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Term</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition / Discussion</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>X12 EDI</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>See</em> <strong>EDI X12.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 2237, 5-3, 5-34
> Abbreviated Item Report, 7-27, 7-28
> Adjust Inventory Quantity, 4-1, 4-5, 4-8, 4-
> 10, 4-12, 4-16, 4-19
> Adjustment Voucher Recap, 7-1 Approve Adjustments, 4-11, 4-18
> Auto-generate Orders, 2-1 Automatic Level Setter, 4-24 Availability Listing, 7-4, 7-5, 7-8
> Balance Update Transaction (IM-6), 5-1 Barcode Manager Menu, 3-1, 3-7, 3-10
> Barcode User Menu, 3-1, 3-4, 3-5
> Clean Up Old Transactions And Due-Outs, 6- 17
> Comment Alignment, 3-19
> Comprehensive Item Report, 6-25, 7-4, 7-
> 29, 7-31
> Control Point, 5-8, 5-19
> Conversion Factor Report, 7-32, 7-33
> Cost Center, 5-21
> Cost Trend Analysis Report, 7-8
> Data Manager Menu, 3-6, 3-7, 3-9, 3-10, 3-
> 12, 3-14
> Date Received Delete (for Issue Book Requests), 5-6
> Days Of Stock On Hand Report, 7-12, 7-15 Design Label, 3-22
> Display Item, 6-1, 6-3
> Display Where An Item Is Stocked, 6-4 Distribution Costs Enter/Edit, 5-9
> Download Barcode Program, 3-1 Due-In Item Report, 5-35, 6-6, 6-7 Emergency Stock Report, 7-15 Enter/Edit Inventory Item Data, 4-26
> Enter/Edit Items On Distribution Point, 6-9 Enter/Edit/View, 3-6, 3-7
> File Inquiry, 4-31
> FMS, 4-10, 6-21
> Graph Usage, 7-18
> Group Category Enter/Edit, 5-16 History By Cost Center Purge, 5-21 Inactive Items Report, 7-25 Inquire Label, 3-14
> Inventory Control Parameters Print, 5-18 Inventory Sales Report, 7-43, 7-44
> ISMS, 5-1, 5-2, 6-21
> Items Flagged 'Kill When Zero' Report, 6-11 Labels Menu, 3-14, 3-15, 3-18
> Last Procurement Source For Item Report, 7-35
> Non-Issuable Stock Report, 7-38 Order Form, 6-13, 6-15
> Outstanding (Due-Outs) Transaction Listing,
> 6-17
> Packaging/Procurement Source Discrepancy Report, 6-20
> Parameter Enter/Edit, 3-30
> Physical Count Form, 4-14, 4-16 Post Issue Book Order, 6-21
> Index
> Print Item On Distribution Inventory Point,
> 6-25
> Print Labels, 3-18
> Program Enter/Edit, 3-35
> Programmer (Barcode) Menu, 3-19, 3-21, 3-
> 29, 3-33, 3-36, 3-39, 3-40
> Purchase Order, 6-27
> Purchase Order Receiving To Inventory Point, 6-27
> Quantity Distribution Report, 7-48, 7-49 Receipts History By Item Purge, 5-23 Reprint Posted Picking Ticket, 5-29 Stock Status Report, 7-50, 7-51
> Storage Location Enter/Edit, 5-33 Substitute Listing Report, 7-40, 7-42
> Transaction Number, 4-3, 4-5, 5-8 Transaction Register Purge, 5-25 Transaction Register Report, 7-54, 7-55, 7-
> 56
> Unapproved Adjustment Report, 4-11, 4-18
> Unit Costing Report, 7-57, 7-58
> Update Calculated Due-Ins/Outstanding Transaction, 5-34, 6-6
> Upload Barcode Data, 3-4, 3-5
> Usage Demand Analysis Report, 7-59, 7-61
> Usage Demand Item Report, 7-62, 7-63
> Usage/Distribution Monthly Totals Purge, 5- 27
> Voucher Summary Report, 7-64
