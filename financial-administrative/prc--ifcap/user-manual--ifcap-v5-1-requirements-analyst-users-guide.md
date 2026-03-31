---
title: IFCAP Version 5.1 Requirements Analyst User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Requirements Analyst User's Guide
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
menu_options: 5
description: 
audience: 
keywords: 
  - strong
  - class
  - point
  - inventory
  - report
  - number
  - table
  - contents
  - warehouse
  - control
page_count: 0
word_count: 10957
section_count: 15
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1requirements_analyst.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1requirements_analyst.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP)Version 5.1Requirements AnalystUser's Guide

![](ifcap-version-5-1-requirements-analyst-user-s-guide/001.png)

March 2026Department of Veterans AffairsOffice of Information and Technology (OI&T)Management, Enrollment, and Financial Systems

Revision History

Initiated on 12/29/04

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 57%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description (Patch # if applic.)</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>March 2026</td>
<td>5.0</td>
<td><p>Updates based on patch PRC*5.1*252.</p>
<p>This manual has been updated to comply with the VA OIT-mandated user guide template.</p></td>
<td><p>Technical Writer,</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="odd">
<td>September 2013</td>
<td>4.0</td>
<td>Patch PRC*5.1*171. Removed option Enter/Edit Control Point Users from menus. See page 21.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>October 2011</td>
<td>3.0</td>
<td>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358. See page <a href="#glossary">31</a>.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>12/29/04</td>
<td>2.0</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>12/29/04</td>
<td>1.0</td>
<td>PDF file checked for accessibility to readers with disabilities.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
</tbody>
</table>

Preface

This document is for VA procurement personnel assigned the user category of Requirements Analyst in the Integrated Funds Distribution, Control Point Monitoring, Accounting and Procurement (IFCAP) system.

In IFCAP, VA employees request goods by creating electronic purchase orders, requisitions and issue book requests. As requisitions are delivered to the warehouse, the Requirements Analyst updates the inventory records for the warehouse. Requirements Analysts also fulfill issue book requests by creating picking tickets. Warehouse clerks use these picking tickets to supply the items from warehouse stock. Requirements Analysts also create requisitions and purchase orders to replace the stock depleted by issue book requests. This manual explains how to use IFCAP as a tool to perform some of the Requirements Analyst functions.

TABLE OF CONTENTS

# INTRODUCTION


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [INTRODUCTION](#introduction)
  - [The Role of the Requirements Analyst](#the-role-of-the-requirements-analyst)
  - [How to Use This Manual](#how-to-use-this-manual)
  - [Reference Numbering System](#reference-numbering-system)
  - [Package Management, Legal Requirements and Security Measures](#package-management-legal-requirements-and-security-measures)
  - [Package Operation](#package-operation)
- [UPDATING INVENTORY RECORDS](#updating-inventory-records)
  - [Introduction](#introduction-1)
  - [Run an Emergency Report](#run-an-emergency-report)
    - [Menu Path](#menu-path)
    - [Report Parameters](#report-parameters)
  - [Run an Auto-generate Report](#run-an-auto-generate-report)
    - [Report Parameters](#report-parameters-1)
    - [Group Categories](#group-categories)
    - [Start Auto-generation](#start-auto-generation)
    - [Print Error List](#print-error-list)
    - [Display Report](#display-report)
  - [Adjust Inventory Records](#adjust-inventory-records)
    - [Introduction](#introduction-2)
    - [Menu Path](#menu-path-1)
    - [Issue Book Adjustment](#issue-book-adjustment)
    - [Non-Issuable or Issuable Adjustment](#non-issuable-or-issuable-adjustment)
    - [Other Adjustment](#other-adjustment)
- [DETERMINING WHAT IS IN THE WAREHOUSE](#determining-what-is-in-the-warehouse)
  - [Introduction](#introduction-3)
  - [Determining Warehouse Stock for a Specific Item](#determining-warehouse-stock-for-a-specific-item)
    - [Menu Path](#menu-path-2)
    - [Select Distribution Point](#select-distribution-point)
    - [Display Report](#display-report-1)
- [CREATING A PICKING TICKET](#creating-a-picking-ticket)
  - [Introduction](#introduction-4)
  - [How to Turn Issue Book Requests into Picking Tickets](#how-to-turn-issue-book-requests-into-picking-tickets)
    - [Menu Path](#menu-path-3)
    - [Enter Electronic Signature](#enter-electronic-signature)
    - [Listing](#listing)
  - [Submit the Picking Ticket to Warehouse Staff](#submit-the-picking-ticket-to-warehouse-staff)
- [Menu Outline](#menu-outline)
- [ERROR MESSAGES AND THEIR RESOLUTION](#error-messages-and-their-resolution)
- [Glossary](#glossary)
- [Index](#index)

## The Role of the Requirements Analyst

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA employees request goods by creating electronic purchase orders, requisitions and issue book requests. As requisitions are delivered to the warehouse, the Requirements Analyst updates the inventory records for the warehouse. Requirements Analysts also fulfill issue book requests by creating picking tickets. Warehouse clerks use these picking tickets to supply the items from warehouse stock. Requirements Analysts also create requisitions and purchase orders to replace the stock depleted by issue book requests.

## How to Use This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual explains how to perform the role of the Requirements Analyst by dividing that role into small, manageable tasks. The authors of this manual have listed these tasks in successive order so that each instruction builds on the functionality and information from the previous instructions. This will allow new Requirements Analysts to use this manual as a tutorial by following the instructions from beginning to end. Experienced Requirements Analysts can use this manual as a reference tool by using the index and table of contents.

## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses a special paragraph numbering system to allow users to understand how the sections of the manual relate to each other. For example, this paragraph is section 1.3. This means that this paragraph is the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections 1.3.1 and 1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third subsection of Chapter 1. All clear? Actually, all this means is that users that want to divide their reading into manageable lessons can concentrate on one section and all of its subsections, e.g., section 1.3.5.4 and all of its subsections would make a coherent lesson.

## Package Management, Legal Requirements and Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to use IFCAP to create orders, users are given access to a set of IFCAP menu options designed for their use. Some of these menu options are additionally controlled by the use of access “keys.” These access keys are administered to individual users by the Information Resources Management Service at their facility. Also, each user is assigned a “signature code” that functions legally as their signature. Users must enter this signature to create any form in IFCAP that would require an authorizing signature if they created the form manually.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Novice users will be unfamiliar with the information that some of the IFCAP prompts require. IFCAP provides three levels of explanations for the prompts. Enter a question mark at the prompt to read a description of the prompt, two question marks to read a more complex explanation of the prompt, and three question marks to read a complete description of the prompt and read a list of acceptable responses to the prompt.

# UPDATING INVENTORY RECORDS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Run an Emergency Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control Point Official's Menu

LOG/GSA/DLA Code Sheets Menu

Requisition Processing

Posted Stock Management

Display/Print Menu (PPM)

Select RA (Requirements Analyst) Menu Option: Posted Stock Management

Inventory Point Management

Warehouse--General Inventory/Distribution Menu ...

Select Posted Stock Management Option: Warehouse--General Inventory/Distribution Menu

Select STATION NUMBER ('^' TO EXIT): 111// ANYCITY,NM

Select Supply Warehouse Inventory Point: ???

CHOOSE FROM:

WHSE SUPPLY WAREHOUSE

Auto-generate Orders

Barcode Manager Menu ...

Inventory File Maintenance Menu ...

Manager For Supply Warehouse Inventory Point Menu ...

Receiving and Distribution Menu ...

Reports Menu ...

Select Warehouse--General Inventory/Distribution Menu Option: Reports Menu

Adjustment Voucher Recap

Availability Listing

Cost Trend Analysis Report

Days Of Stock On Hand Report

Emergency Stock Report

Graph Usage

History Of Distribution Report

Inactive Items Report

Informational Reports Menu ...

Inventory Sales Report

Quantity Distribution Report

Stock Status Report

Transaction Register Report

Unit Costing Report

Usage Demand Analysis Report

Usage Demand Item Report

Voucher Summary Report

Select Reports Menu Option: Emergency Stock Report

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may limit the report to begin at a particular National Stock Number if you like. Enter an output device. The system will print or display the 'Emergency Stock Level Report,' which lists every item at or below the emergency stock level, grouped by inventory point. The report will list the National Stock Number of the item, its description, the master item number (#MI), the unit per issue, and the stock levels for the item. The report will also list the transaction and the purchase order for the item, the vendor and vendor number, the estimated date received, and the amount due to be received (Due-In). After printing or displaying the report, the system will return to the Reports Menu.

START WITH NSN: FIRST// @ \<\<-- ENTER '@' TO PRINT ITEMS WITHOUT A NSN

START WITH NSN: FIRST//

DEVICE: ;9999 HOME

EMERGENCY STOCK LEVEL REPORT DEC 14,1994 13:14 PAGE 1

NSN DESCRIPTION \[#MI\] UNIT per ISSUE

--------------------------------------------------------------------------------

INVENTORY POINT: 600-SUPPLY WAREHOUSE

6510-00-721-9789 BAND 6X4.5 TENSOR \[#8326\] 1 per BG

NORM LVL EMER LVL QTY ON-HAND QTY DUE-IN QTY DUE-OUT INT ORD PT

80 20 84

TRANSACTION \# PO \# VENDOR \[#V\] EST DATE RECD DUE-IN

600-95-1-999-0406 G50411 IFVENDOR,ONE \[#1172\] DEC 30, 1994 84

6510-00-721-9790 BAND 4X4.5 TENSOR \[#8325\] 1 per BG

NORM LVL EMER LVL QTY ON-HAND QTY DUE-IN QTY DUE-OUT INT ORD PT

80 20 84

TRANSACTION \# PO \# VENDOR \[#V\] EST DATE RECD DUE-IN

600-95-1-999-0406 G50411 IFVENDOR,ONE \[#1172\] DEC 30, 1994 84

\[END OF REPORT\]------------------------------------------------\[USER: IFUSER,ONE\]

\<Press RETURN to continue\>

Adjustment Voucher Recap

Availability Listing

Cost Trend Analysis Report

Days Of Stock On Hand Report

Emergency Stock Report

Graph Usage

History Of Distribution Report

Inactive Items Report

Informational Reports Menu ...

Inventory Sales Report

Quantity Distribution Report

Stock Status Report

Transaction Register Report

Unit Costing Report

Usage Demand Analysis Report

Usage Demand Item Report

Voucher Summary Report

Select Reports Menu Option:

## Run an Auto-generate Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list the cost center and the control point. Enter a fiscal year and fiscal quarter. If you already have a repetitive item list on file, IFCAP will ask you if you want to delete the repetitive item lists on file. If you auto-generate orders, IFCAP will generate another repetitive item list. Multiple repetitive item lists can cause duplicate orders.

Control Point Official's Menu ...

LOG/GSA/DLA Code Sheets Menu ...

Requisition Processing ...

Posted Stock Management ...

Display/Print Menu (PPM) ...

Select RA (Requirements Analyst) Menu Option: Posted Stock Management

Inventory Point Management

Warehouse--General Inventory/Distribution Menu ...

Select Posted Stock Management Option: Warehouse--General Inventory/Distribution

Menu

Select STATION NUMBER ('^' TO EXIT): 111// ANYCITY,NM

Select Supply Warehouse Inventory Point: Whse 111-WHSE SUPPLY WAREHOUSE

I N V E N T O R Y version 5.0T20

\(111\) Warehouse Inventory Point: WHSE IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> DISTRIBUTION HISTORY NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> OPENING MONTHLY INVENTORY BALANCES NEED TO BE SET.

Auto-generate Orders

Barcode Manager Menu ...

Inventory File Maintenance Menu ...

Manager For Supply Warehouse Inventory Point Menu ...

Receiving and Distribution Menu ...

Reports Menu ...

Select Warehouse--General Inventory/Distribution Menu Option: Auto-generate Orders

========== PART 1: REPETITIVE ITEM LIST NUMBER ==========

COST CENTER: 600000

FUND CONTROL POINT: 9988 LAB TESTING 988 SUPP FUND

Select FISCAL YEAR: 95//

Select QUARTER: 1//

I will generate requests for: 111-95-1-9988-600000

You currently have the following repetitive item lists on file:

111-95-1-9988-600000-0001 created: 12-06-94 item count: 1

Do you want to DELETE all the repetitive item lists on file? NO// Y (YES)

deleting repetitive item lists...

### Group Categories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may select all group categories and vendors, or select individual group categories and vendors. You can deselect a group category or vendor by reselecting it. Press the Enter key at the Select Group Category: prompt when you have finished selecting group categories. Press the Enter key at the Select Vendor Name: prompt when you have finished selecting vendors.

========== PART 2A: SELECTION OF GROUP CATEGORIES ==========

Selected group categories and vendors will be used to auto-generate the order.

Do you want to select ALL group categories? YES// (YES)

Currently selected group categories:

\<\< ALL GROUP CATEGORIES \>\>

You can DE-select one of the above group categories by reselecting it.

Select the name of the group category created for this primary, '^' to exit.

Select GROUP CATEGORY:

========== PART 2B: SELECTION OF VENDORS ==========

Do you want to select ALL vendors? YES// (YES)

Currently selected vendors:

\<\< ALL VENDORS \>\>

You can DE-select one of the above vendors by reselecting it.

Select the name of the vendor supplying this primary, '^' to exit.

Select VENDOR NAME:

\<\<\< NOTE: Auto-generating for ALL vendors.

### Start Auto-generation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you to confirm that you want to start the auto-generation. IFCAP will display a bar showing the percentage of auto-generation that it has completed. After IFCAP has generated the orders, IFCAP will create a new repetitive item list, and display a bar showing the percentage of item list creation that it has completed.

========== PART 3: START AUTO-GENERATION ==========

ARE YOU SURE YOU WANT TO START AUTO-GENERATION? YES// (YES)

\<\<\< Starting Auto-generation ...

% COMPLETE

0 10 20 30 40 50 60 70 80 90 100

\|----+----+----+----+----+----+----+----+----+----\|

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\<\<\< Finished !

\<\<\< Creating repetitive item list ... Number: 111-95-1-9988-600000-0002

\<\<\< Locking repetitive item list ...

\<\<\< Adding 1 items to repetitive item list ...

% COMPLETE

0 10 20 30 40 50 60 70 80 90 100

\|----+----+----+----+----+----+----+----+----+----\|

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Total number of items : 1

Total cost (all items): \$ 956.00

\<\<\< Unlocking repetitive item list ...

### Print Error List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will ask you if you want the auto-generation report to print the errors that occurred during auto-generation. IFCAP will print or display the "Auto-Generation" report, listing the items and quantity of the orders automatically generated, sorted by group category.

Do you want to print errors occurring during auto-generation? YES// (YES)

DEVICE: HOME// ;;9999 LAT

\<\*\> please wait \<\*\>

AUTO-GENERATION: SUGGESTED ORDERS FOR WHSE DEC 06, 1994@11:10:46 PAGE 1

ORDERING FROM VENDOR: IFVENDOR,TWO

REPETITIVE ITEM LIST NUMBER: 111-95-1-9988-600000-0002

WHSE VENDOR ISSUE ISSUE

MI# DESCRIPTION NSN UNIT/ISS UNIT/ISS MINIM MULT

--------------------------------------------------------------------------------

GROUP CATEGORY: 1: Office supplies (#2)

45 TESTING V5 6505-02-564-1255 1/EA 1/EA

ONHAND +DUEIN -DUEOUT =AVAIL STAND OPTN LEVEL CONV ORDER UNIT\$

10 2 0 12 350\* 35 490 1 478 2.000

TOTAL COST OF ORDER: 956

\[END OF REPORT\]------------------------------------------------\[USER: IFUSER,ONE\]

### Display Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you answered yes at the Do You Want To Print Errors Occurring During Auto-Generation?: prompt, IFCAP will also print or display the "Auto-Generation Error Report," listing each error by item and cause of error. IFCAP will return to the General Inventory/Distribution Menu.

AUTO-GENERATION ERROR REPORT FOR WHSE DEC 06, 1994@11:10:48 PAGE 1

MI# DESCRIPTION NSN

--------------------------------------------------------------------------------

8 ITEM \#8 6505-11-222-3333

-\> NORMAL STOCK LEVEL missing for item

40 PAINT 6540-11-411-1111

-\> GROUP CATEGORY missing for item

39 RULER 7510-11-113-1111

-\> GROUP CATEGORY missing for item

37 Ballpoint pen 7510-11-411-1234

-\> MANDATORY OR REQUESTED SOURCE is missing for item

\[END OF REPORT\]------------------------------------------------\[USER: IFUSER,ONE\]

\<Press RETURN to continue\>

Auto-generate Orders

Barcode Manager Menu ...

Inventory File Maintenance Menu ...

Manager For Supply Warehouse Inventory Point Menu ...

Receiving and Distribution Menu ...

Reports Menu ...

Select Warehouse--General Inventory/Distribution Menu Option:

## Adjust Inventory Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Often, discrepancies between records and stock are due to unit-of-issue conflicts, e.g., where the requisition specifies 10 boxes of six cans each, and the warehouse clerk counted a stock of 60 cans. Follow the instructions in this section to adjust these and other discrepancies between stock records and actual stock.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control Point Official's Menu ...

LOG/GSA/DLA Code Sheets Menu ...

Requisition Processing ...

Posted Stock Management ...

Display/Print Menu (PPM) ...

Select RA (Requirements Analyst) Menu Option: Posted Stock Management

Inventory Point Management

Warehouse--General Inventory/Distribution Menu ...

Select Posted Stock Management Option: Warehouse--General Inventory/Distribution Menu

Select STATION NUMBER ('^' TO EXIT): 111// ANYCITY,NM

Select Supply Warehouse Inventory Point: Whse 111-WHSE SUPPLY WAREHOUSE

Auto-generate Orders

Barcode Manager Menu ...

Inventory File Maintenance Menu ...

Manager For Supply Warehouse Inventory Point Menu ...

Receiving and Distribution Menu ...

Reports Menu ...

Select Warehouse--General Inventory/Distribution Menu Option: Inventory File Maintenance Menu

\(668\) Warehouse Inventory Point: WHSE 668 IFUSER,ONE

--\> USAGE/DISTRIBUTION TOTALS NEEDS TO BE PURGED.

--\> RECEIPTS HISTORY BY ITEM NEEDS TO BE PURGED.

--\> DISTRIBUTION HISTORY NEEDS TO BE PURGED.

--\> TRANSACTION REGISTER NEEDS TO BE PURGED.

--\> OPENING MONTHLY INVENTORY BALANCES NEED TO BE SET.

Adjust Inventory Quantity Menu ...

Automatic Level Setter

Enter/Edit Inventory Item Data

File Inquiry

Select Inventory File Maintenance Menu Option: Adjust Inventory Quantity Menu

Adjust Inventory Quantity

Approve Adjustments

Physical Count Form

Unapproved Adjustment Report

Select Adjust Inventory Quantity Menu Option: Adjust Inventory Quantity

Enter ELECTRONIC SIGNATURE CODE: Thank you.

### Issue Book Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are making an issue book adjustment, follow the instructions in the section below. Otherwise, skip this section and go to the next section.

#### Select Transaction Number

Select Issue Book Adjustment at the Select Type of Adjustment: prompt. Enter the transaction number of the issue book request at the Select Transaction Number: prompt. Enter the line number that you want to adjust. The system will display the item information, the quantity information, and the dollar value of the item.

Select one of the following:

1 Issue Book Adjustment

2 Non-Issuable or Issuable Adjustment

3 Other (GIP and FMS) Adjustment

4 Supply Only (GIP) Adjustment

Select TYPE of ADJUSTMENT: 1 Issue Book Adjustment

Select TRANSACTION NUMBER: 111-94-4-101-0409 OBL SUPPLY WAREHOUSE RULER

\>\> Reference Voucher Number: I40003

\>\> Distribution to: 111-NEWONE inventory point.

Select LINE ITEM Number: 1 IM#: 39 QTY POSTED: 1 INV VALUE: 3.75 SELL VALUE:

4.05

===================== C U R R E N T I T E M D A T A =====================

ITEM NUMBER: 39 RULER NSN: 7510-11-113-1111

UNIT/ISSUE : 1/EA

AVERAGE COST : 4.05

LAST COST : 0.00

TOTAL VALUE : 2061.00

QTY ON-HAND : 509

QTY NON-ISSUABLE:

======================= I S S U E B O O K D A T A =======================

QUANTITY ORDERED: 1

QUANTITY POSTED : 1

INVENTORY VALUE : 3.75

SELLING VALUE : 4.05

#### Enter Adjustment Data

The system will let you change the quantity of the item, the cash value of the item as inventory stock, and the cash value of the item when it is issued to the service. The system will add "reason text," or an explanation line, to the transaction explaining the reason for the adjustment. the default reason text is "Issue Book Adjustment,” but you can edit this explanation. When you have finished editing line numbers, press the Enter key at the Select Line Item Number: prompt. Answer Y at the Ready To Process Issue Book Adjustments?: prompt to transmit the adjustment. The system will list the number of the modification document and the VA MailMan message that lists the adjustment information. Enter another transaction number at the Select Transaction Number: prompt, or press the Enter key to return to the Adjust Inventory Quantity Menu.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* E N T E R A D J U S T M E N T D A T A \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\>\> Enter the adjusted quantity in the range -1 to 0. \<\<

ADJUSTED QUANTITY: 0//

\>\> Enter the adjusted value in the range -3.75 to 99999.99. \<\<

ADJUSTED TOTAL ISSUE BOOK INVENTORY VALUE: 2

\>\> Enter the adjusted value in the range -4.05 to 99999.99. \<\<

ADJUSTED TOTAL ISSUE BOOK SELLING VALUE: 4

\>\> Enter the reason text which will appear on the transaction register. \<\<

REASON TEXT: ISSUE BOOK adjustment Replace

Select LINE ITEM Number:

READY TO PROCESS ISSUE BOOK ADJUSTMENTS? YES// (YES)

FMS IV MODIFICATION 111I40003 document automatically transmitted..

LOG 605 Transmitted in MailMan Messages: 66141

Queueing Approval Form to Print on 'Fiscal (Receiving Reports)' Printer ...

Queueing Approval Form to Print on 'Supply (PPM)' Printer ...

Select TRANSACTION NUMBER:

Adjust Inventory Quantity

Approve Adjustments

Physical Count Form

Unapproved Adjustment Report

Select Adjust Inventory Quantity Menu Option:

### Non-Issuable or Issuable Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are making a non-issuable or issuable adjustment, follow the instructions in the section below. Otherwise, skip this section and go to the next section.

#### Select Item

Enter the name of the item or the item number at the Select Whse Item: prompt. If you do not know the name or number of the item, enter three question marks and the system will list the available items. The system will list the cost and quantity information for the item.

Select one of the following:

1 Issue Book Adjustment

2 Non-Issuable or Issuable Adjustment

3 Other (GIP and FMS) Adjustment

4 Supply Only (GIP) Adjustment

Select TYPE of ADJUSTMENT: Non-Issuable or Issuable Adjustment

\>\> Select an item number from the WHSE inventory point. \<\<

Select WHSE ITEM: ???

CHOOSE FROM:

8 ITEM \#8 NSN: 6505-11-222-3333

37 PEN NSN: 7510-11-411-1234

39 RULER NSN: 7510-11-113-1111

40 PAINT NSN: 6540-11-411-1111

45 TESTING V5 NSN: 6505-02-564-1255

Select WHSE ITEM: 40 PAINT PAINTNSN: 6540-11-411-1111

===================== C U R R E N T I T E M D A T A =====================

ITEM NUMBER: 40 PAINT NSN: 6540-11-411-1111

UNIT/ISSUE : ?/??

AVERAGE COST : 1.61

LAST COST : 0.00

TOTAL VALUE : 962.24

QTY ON-HAND : 599

QTY NON-ISSUABLE:

#### Enter Adjustment Data

At the Adjusted Quantity: prompt, enter a negative number for the amount of units you want to deduct from warehouse stock. Enter an alphanumeric code for the adjustment voucher number. The system will add "reason text," or an explanation line, to the transaction explaining the reason for the adjustment. the default reason text is "To Non-Issuable,” but you can edit this explanation. When you have finished adjusting warehouse items, press the Enter key at the Select Whse Item: prompt. Enter Y at the Ready To Process Non-Issuable Adjustments?: prompt to transmit the adjustment. The system will display the VA MailMan message number of the adjustment and return to the Adjust Inventory Quantity Menu.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* E N T E R A D J U S T M E N T D A T A \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\>\> Enter the adjusted quantity in the range -599 to 0. \<\<

ADJUSTED QUANTITY: 0// -4

\>\> Enter DOCUMENT IDENTIFIER number. \<\<

VOUCHER NUMBER: BR549

\>\> Enter the reason text which will appear on the transaction register. \<\<

REASON TEXT: TO non-issuable//

\>\> Select an item number from the WHSE inventory point. \<\<

Select WHSE ITEM:

READY TO PROCESS NON-ISSUABLE ADJUSTMENTS? YES// (YES).

LOG 605 Transmitted in MailMan Messages: 66145

Queueing Approval Form to Print on 'Fiscal (Receiving Reports)' Printer ...

Queueing Approval Form to Print on 'Supply (PPM)' Printer ...

Adjust Inventory Quantity

Approve Adjustments

Physical Count Form

Unapproved Adjustment Report

Select Adjust Inventory Quantity Menu Option:

### Other Adjustment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Enter Item

Enter the name of the item or the item number at the Select Whse Item: prompt. If you do not know the name or number of the item, enter three question marks and the system will list the available items. The system will list the cost and quantity information for the item.

Select one of the following:

1 Issue Book Adjustment

2 Non-Issuable or Issuable Adjustment

3 Other (GIP and FMS) Adjustment

4 Supply Only (GIP) Adjustment

Select TYPE of ADJUSTMENT: Other Adjustment

\>\> Select an item number from the WHSE inventory point. \<\<

Select WHSE ITEM: ???

CHOOSE FROM:

8 ITEM \#8 NSN: 6505-11-222-3333

37 PEN NSN: 7510-11-411-1234

39 RULER NSN: 7510-11-113-1111

40 PAINT NSN: 6540-11-411-1111

45 TESTING V5 NSN: 6505-02-564-1255

Select WHSE ITEM: 40 PAINT PAINTNSN: 6540-11-411-1111

===================== C U R R E N T I T E M D A T A =====================

ITEM NUMBER: 40 PAINT NSN: 6540-11-411-1111

UNIT/ISSUE : ?/??

AVERAGE COST : 1.61

LAST COST : 0.00

TOTAL VALUE : 962.24

QTY ON-HAND : 595

QTY NON-ISSUABLE: 4

#### Enter Adjustment Data

Enter a negative number at the Adjusted Quantity: prompt to subtract from the inventory quantity, or a positive number to add to the inventory quantity. You also need to enter the change in value, either positive or negative, to the overall value of the total inventory of the item. In the example below, adding 4 to the overall quantity at a value of \$1.61 per unit is an adjusted total inventory value of \$6.44. Enter an alphanumeric code for the adjustment voucher number. The system will list the available adjustments. Select the appropriate adjustment category. When you are finished adjusting warehouse items, press the Enter key at the Select Whse Item: prompt. Enter Y at the Ready To Process Inventory Adjustments?: prompt. The system will list the number of the FMS document and VA MailMan message it created to transmit the adjustment, and return to the Adjust Inventory Quantity Menu.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* E N T E R A D J U S T M E N T D A T A \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\>\> Enter the adjusted quantity in the range -595 to 99998. \<\<

ADJUSTED QUANTITY: 0// 4

\>\> Enter the adjusted value in the range -99999.99 to 99999.99. \<\<

ADJUSTED TOTAL INVENTORY VALUE: 6.44

\>\> Enter DOCUMENT IDENTIFIER number. \<\<

VOUCHER NUMBER: BR549

Select one of the following:

1 Transfer of stock to another VAMC Warehouse

2 Sale of stock to OGA

3 Transfer of excess stock to GSA

4 Adjustment of stock valuation

5 Writeoff damaged stock

6 Transfer Transportation expense to stock

7 Inventory Refund

Select TYPE of ADJUSTMENT: 4 Adjustment of stock valuation

\>\> Select an item number from the WHSE inventory point. \<\<

Select WHSE ITEM:

READY TO PROCESS INVENTORY ADJUSTMENTS? YES// (YES)

FMS SV 111A41 document automatically transmitted..

LOG 605 Transmitted in MailMan Messages: 66156

Queueing Approval Form to Print on 'Fiscal (Receiving Reports)' Printer ...

Queueing Approval Form to Print on 'Supply (PPM)' Printer ...

Adjust Inventory Quantity

Approve Adjustments

Physical Count Form

Unapproved Adjustment Report

Select Adjust Inventory Quantity Menu Option:

# DETERMINING WHAT IS IN THE WAREHOUSE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter explains how to determine the amount of warehouse stock for any item in the Item Master File. To determine warehouse stock for a specific issue book request, read the next chapter on creating a picking ticket.

## Determining Warehouse Stock for a Specific Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RA enters the item and IFCAP displays how much is in the warehouse. Display Item, item name at the SUPPLY WHSE ITEM: prompt.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control Point Official's Menu ...

LOG/GSA/DLA Code Sheets Menu ...

Requisition Processing ...

Posted Stock Management ...

Display/Print Menu (PPM) ...

Select RA (Requirements Analyst) Menu Option: Posted Stock Management

Inventory Point Management

Warehouse--General Inventory/Distribution Menu ...

Select Posted Stock Management Option: Warehouse--General Inventory/Distribution Menu

Select STATION NUMBER ('^' TO EXIT): 111// ANYCITY,NM

Select Supply Warehouse Inventory Point: Whse 111-WHSE SUPPLY WAREHOUSE

Auto-generate Orders

Barcode Manager Menu ...

Inventory File Maintenance Menu ...

Manager For Supply Warehouse Inventory Point Menu ...

Receiving and Distribution Menu ...

Reports Menu ...

Select Warehouse--General Inventory/Distribution Menu Option: Receiving and Distribution Menu

Display Item

Display Where An Item Is Stocked

Due-In Item Report

Enter/Edit Items On Distribution Point

Items Flagged 'Kill When Zero' Report

Order Form

Outstanding (Due-Outs) Transaction Listing

Packaging/Procurement Source Discrepancy Report

Post Issue Book Order

Print Item On Distribution Inventory Point

Purchase Order Receiving To Inventory Point

Select Receiving and Distribution Menu Option: Display Item

### Select Distribution Point

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the distribution point to select an item from a specific distribution point, or press the Enter key to select an item from the inventory point you entered at the Select Supply Warehouse Inventory Point: prompt. Enter the item at the Select (inventory point) Item: prompt.

Enter the DISTRIBUTION POINT to select an item from the distribution point, or Enter \<RETURN\> to select an item from the WHSE inventory point.

Select DISTRIBUTION POINT:

Select WHSE ITEM: ???

CHOOSE FROM:

8 ITEM \#8 NSN: 6505-11-222-3333

37 PEN NSN: 7510-11-411-1234

39 RULER NSN: 7510-11-113-1111

40 PAINT NSN: 6540-11-411-1111

45 TESTING V5 NSN: 6505-02-564-1255

Select WHSE ITEM: 37 PEN PENNSN: 7510-11-411-1234

### Display Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will create a "Display Item Report,” listing the item descriptions, stock levels, and usage history of the item. QTY ON HAND: is the number of units of the item that is in stock at the inventory point you selected, according to IFCAP records. Enter another item at the Select (inventory point) Item: prompt or press the Enter key to return to the Receiving and Distribution Menu.

DISPLAY ITEM REPORT FOR 111-WHSE AUG 12, 1994@14:03:53 PAGE: 1

NSN DESCRIPTION \[#MI\] GROUP : DESCRIPTION

--------------------------------------------------------------------------------

7510-11-411-1234 PEN \[#37\]

BOC: 2660 Operating Supplies and Materials

UNIT per ISSUE: 1 per EA

QTY ON HAND: 496 DUE-IN: 0 DUE-OUT: 99

QTY NON-ISS: 0

TOTAL VALUE: 1171.02

NORM STL LVL: REORDER PT: INT ORDER PT:

EMERGENCY LVL: ISSUE MULT: MIN ISSUE QTY: 1

LAST COST: LAST REC'D: AVERAGE COST: 2.361

MAIN STORAGE LOC: ?

-----USAGE/ISSUES HISTORY-----

DATE USED/ISSUED QTY USED/ISSUED COST USED/ISSUED

MAR 1994 9 17.080

JUN 1994 0 0.100

JUL 1994 1 2.360

AUG 1994 4 9.440

DISPLAY ITEM REPORT FOR 111-WHSE AUG 12, 1994@14:03:53 PAGE: 2

NSN DESCRIPTION \[#MI\] GROUP : DESCRIPTION

--------------------------------------------------------------------------------

-----RECEIPTS HISTORY-----

DATE RECEIVED QTY RECEIVED % STOCK ON HAND BEFORE RECEIPT

MAR 07, 1994 500 0.000

MAR 08, 1994 10 0.000

\[END OF REPORT\]------------------------------------------------\[USER: IFUSER,ONE\]

Select WHSE ITEM:

Display Item

Display Where An Item Is Stocked

Due-In Item Report

Enter/Edit Items On Distribution Point

Items Flagged 'Kill When Zero' Report

Order Form

Outstanding (Due-Outs) Transaction Listing

Packaging/Procurement Source Discrepancy Report

Post Issue Book Order

Print Item On Distribution Inventory Point

Purchase Order Receiving To Inventory Point

Select Receiving and Distribution Menu Option:

# CREATING A PICKING TICKET

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Picking tickets are instructions to warehouse staff to remove items from warehouse stock and deliver them to requesting services. Issue Book requests are fulfilled by creating picking tickets.

## How to Turn Issue Book Requests into Picking Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control Point Official's Menu ...

LOG/GSA/DLA Code Sheets Menu ...

Requisition Processing ...

Posted Stock Management ...

Display/Print Menu (PPM) ...

Select RA (Requirements Analyst) Menu Option: Posted Stock Management

Inventory Point Management

Warehouse--General Inventory/Distribution Menu ...

Select Posted Stock Management Option: Warehouse--General Inventory/Distribution Menu

Select STATION NUMBER ('^' TO EXIT): 111// ANYCITY,NM

Select Supply Warehouse Inventory Point: Whse 111-WHSE SUPPLY WAREHOUSE

Auto-generate Orders

Barcode Manager Menu ...

Inventory File Maintenance Menu ...

Manager For Supply Warehouse Inventory Point Menu ...

Receiving and Distribution Menu ...

Reports Menu ...

Select Warehouse--General Inventory/Distribution Menu Option: Receiving and Distribution Menu

Display Item

Display Where An Item Is Stocked

Due-In Item Report

Enter/Edit Items On Distribution Point

Items Flagged 'Kill When Zero' Report

Order Form

Outstanding (Due-Outs) Transaction Listing

Packaging/Procurement Source Discrepancy Report

Post Issue Book Order

Print Item On Distribution Inventory Point

Purchase Order Receiving To Inventory Point

Select Receiving and Distribution Menu Option: Post Issue Book Order

### Enter Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter your electronic signature code. Enter the transaction number of the issue book transaction. If you do not know the transaction number, enter three question marks at the prompt and IFCAP will list the available transactions.

Select STATION NUMBER ('^' TO EXIT): 111// ANYCITY,NM

Enter ELECTRONIC SIGNATURE CODE: Thank you.

Select TRANSACTION NUMBER: ???

1 111-94-3-101-0157 OBL SUPPLY WAREHOUSE C40119 RULER

2 111-94-3-101-0209 OBL SUPPLY WAREHOUSE TESTING ...V5

3 111-94-3-110-0046 OBL SUPPLY WAREHOUSE C40109 RULER

4 111-94-3-110-0060 OBL SUPPLY WAREHOUSE TESTING ...V5

5 111-94-3-110-0068 OBL SUPPLY WAREHOUSE A40917 ITEM \#8

TYPE '^' TO STOP, OR

CHOOSE 1-5: 1

+---------------------------------------------------------------------+

\|Distribution to Primary Inventory Point: SPD \|

+---------------------------------------------------------------------+

+---------------------------------------------------------------------+

\|This is the FIRST time this issue book has been POSTED. The \|

\|reference voucher number will automatically be generated from the \|

\|common numbering series when the issue book is posted. \|

+---------------------------------------------------------------------+

\<Press RETURN to continue\>

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list the issue book transaction number. Enter one of the commands at the bottom of the screen, or press the Enter key to quit.

Issue Book Posting Aug 15, 1994 10:23:05 Page: 1 of 1

ISSUE BOOK: 111-94-3-101-0157 POST TO: 111-SPD

REF#: to be generated UNIT QTY ESTIMATE \* \* Q U A N T I T Y \* \*

LINE DESCRIPTION IM# /IS ONHAND UNITCOST ORDERED REMAIN TO POST

1 RULER 39 1/EA 510 4.05 1 1 0

Enter ?? for more actions

EE E/E Inventory Items QE Qty to Enter CL Cancel Line Item

SN Show NSN QO Qty to On Hand SL Substitute Line Item

MF Make Final QR Qty to Remaining PI Post Issue Book

Select Item(s): Quit//

IFCAP will print the items that are not in the warehouse on a section of the picking ticket called “Exceptions to Issue Book Request.” Create a 2237

## Submit the Picking Ticket to Warehouse Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Make sure that you submit the picking ticket to the warehouse. If you do not submit the picking ticket to the warehouse, the recipient of the goods will assume that the warehouse has been delinquent on fulfilling the picking ticket.

# Menu Outline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select RA (Requirements Analyst) Menu Option:

Control Point Official's Menu ...

Display Control Point Activity Menu ...

Funds Control Menu ...

Status of Requests Reports Menu ...

Record Date Received by Service Menu ...

Record Receipt of Multiple Delivery Schedule Items

Multiple Delivery Schedule List

LOG/GSA/DLA Code Sheets Menu ...

Requisition Processing ...

Posted Stock Management ...

Display/Print Menu (PPM) ...

RA (Requirements Analyst) Menu

Control Point Official's Menu

Approve Requests

Requests Ready for Approval List

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

List 1358's with Open Authorizations

Print 1358

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

Display Control Point Activity Menu

Purchase Order Status

Transaction Status Report

Running Balances

Temporary Transaction Listing

Item History

PPM Status of Transactions Report

CP Entered, Not Approved Requests

Funds Control Menu

Assign Ceiling to Sub-Control Points

Correct Sub-Control Point Amounts

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

LOG/GSA/DLA Code Sheets Menu

Acquisitions Code Sheets Generation (LOG/GSA/DLA)

Receiving Code Sheets Generation (LOG/GSA/DLA)

Issues Code Sheet Generation (LOG)

Create or Edit Code Sheets Manually (LOG/GSA/DLA)

Create Code Sheet (LOG/GSA/DLA)

Edit Code Sheet (LOG/GSA/DLA)

Delete Existing Code Sheet (LOG/GSA/DLA)

Keypunch (direct entry) Menu (LOG/GSA/DLA)

Keypunch a Code Sheet (LOG/GSA/DLA)

Edit Keypunched Code Sheet (LOG/GSA/DLA)

Batch Management Menu (LOG/GSA/DLA)

Batch and Print Code Sheet (LOG/GSA/DLA)

Modify Batch Priority (LOG/GSA/DLA)

Reprint a Batch (LOG/GSA/DLA)

Code Sheet Transmission Menu (LOG/GSA/DLA)

Inquiry to Batch/Transmission

Requisition Processing

New Requisition

Edit an Incomplete Requisition

Amendment to Requisition

Cancel an Unobligated Requisition

Remove 2237 from Requisition

Display Purchase Order/Requisition

Change Delivery Date on Requisition

Enter DEPOT/GSA PUSH Order to PO Register

Change DEPOT/GSA PUSH Order on PO Register

Item File Edit

Requisition Register

Posted Stock Management

Inventory Point Management

Warehouse--General Inventory/Distribution Menu

Auto-generate Orders

Barcode Manager Menu

Barcode User Menu

Download Barcode Program

Upload Barcode Data

Data Manager Menu

Enter/Edit/View

Schedule Data To Process

Status Of Data

Labels Menu

Inquire Label

Print Labels

Programmer (Barcode) Menu

Comment Alignment

Design Label

Parameter Enter/Edit

Program Enter/Edit

Speciality Commands Enter/Edit

Inventory File Maintenance Menu

Adjust Inventory Quantity Menu

Adjust Inventory Quantity

Approve Adjustments

Physical Count Form

Unapproved Adjustment Report

Automatic Level Setter

Enter/Edit Inventory Item Data

File Inquiry

Manager For Supply Warehouse Inventory Point Menu

Balance Update Transaction (IM-6)

Clean Up Old Transactions And Due-Outs

Date Received Delete (for Issue Book Requests)

Distribution Costs Enter/Edit

Enter/Edit Inventory And Distribution Points

Group Category Enter/Edit

Inventory Control Parameters Print

Purge History Files Menu

History By Cost Center Purge

Receipts History By Item Purge

Transaction Register Purge

Usage/Distribution Monthly Totals Purge

Reprint Posted Picking Ticket

Storage Location Enter/Edit

Update Calculated Due-Ins/Outstanding Transaction

Receiving and Distribution Menu

Display Item

Display Where An Item Is Stocked

Due-In Item Report

Enter/Edit Items On Distribution Point

Items Flagged 'Kill When Zero' Report

Order Form

Outstanding (Due-Outs) Transaction Listing

Packaging/Procurement Source Discrepancy Report

Post Issue Book Order

Print Item On Distribution Inventory Point

Purchase Order Receiving To Inventory Point

Reports Menu

Adjustment Voucher Recap

Availability Listing

Cost Trend Analysis Report

Days Of Stock On Hand Report

Emergency Stock Report

Graph Usage

History Of Distribution Report

Inactive Items Report

Informational Reports Menu

Abbreviated Item Report

Comprehensive Item Report

Conversion Factor Report

Last Procurement Source For Item Report

Non-Issuable Stock Report

Substitute Listing Report

Inventory Sales Report

Quantity Distribution Report

Stock Status Report

Transaction Register Report

Unit Costing Report

Usage Demand Analysis Report

Usage Demand Item Report

Voucher Summary Report

Display/Print Menu (PPM)

Purchase Order Display

2237 Request Display

Item Display

History of Item Display /Print

Vendor Display

Mandatory Sources 850 Undelivered Orders

> **NOTE:** The options on the Control Point Official’s menu are explained in the Control Point Official manual. The options on the Warehouse--General Inventory/Distribution Menu are explained in the GIP manual. The options on the Requisition Clerk menu are explained in the Requisition Clerk manual.

# ERROR MESSAGES AND THEIR RESOLUTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are errors that you may encounter when processing a purchase order. Each error is listed alphabetically by code. While some of the problems may be fixed by the user, many must be fixed by your Information Resources Management Service. If this is the case, record the error code and message and report the error immediately to your Information Resources Management Service.

| Error Code | Error Message                                                                                 | Reason                                                                                                                                                  |
|----------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAUC^\<LIN\>   | "No actual unit cost for this ITEM."                                                              | There is no Actual Unit Cost entry for the \<LIN\> Item in the Procurement & Accounting Transactions file.                                                  |
| NCNO^\<LIN\>   | "This order requires a contract number but none was entered for this item.”                       | The order is a Direct Order. There is no contract number entered for this \<LIN\> Item in the Procurement & Accounting Transactions file.                   |
| NDD            | "No delivery date for this P.O. in file 442."                                                     | There is no Delivery Date in the Procurement & Accounting Transactions file.                                                                                |
| NDP0           | "No record for direct delivery patient pointer."                                                  | The Direct Delivery Patient entered in the Procurement & Accounting Transactions file for this purchase order cannot be found in file 440.2.                |
| NFT0^\<SITE\>  | "No entry in file 411.2 for facility type pointer from file 411."                                 | There is no entry in the Facility Type file (file 411.2) for the Facility Type field of the Admin. Activity Site Parameter file (file 411).                 |
| NFT^\<SITE\>   | "No facility type pointer for site in file 411."                                                  | The Admin. Activity Site Parameter file has no entry in it.                                                                                                 |
| NI2N^\<ITEM\>  | "No contract number for item on this P.O."                                                        | There are no ITEMS listed under the Item multiple in the Procurement & Accounting Transactions file (file 442).                                             |
| NMIC           | "No mail invoice city in file 411."                                                               | The city listed for No Mail Invoice could not be found in the Admin. Activity Site Parameter file.                                                          |
| NMIL           | “MAIL INVOICE LOCATION information in file 411 missing.”                                          | No MAIL INVOICE LOCATION in Admin. Activity Site Parameter file (file 411).                                                                                 |
| NMIS           | "No state file pointer in file 411."                                                              | No Mail Invoice State pointer in Admin. Activity Site Parameter file.                                                                                       |
| NMIZ           | "No mail invoice ZIP CODE entry in file 411."                                                     | No Mail Invoice Zip in Admin. Activity Site Parameter file.                                                                                                 |
| NOPR           | "No PROPOSAL entry in file 442 for this P.O."                                                     | There is no Proposal entry in Procurement & Accounting Transactions file.                                                                                   |
| NOPT           | "No patient file entry for direct delivery patient pointer."                                      | There is no entry in the Patient file (file 2) for the Direct Delivery Patient entered for this P.O. in file 442.                                           |
| NP12           | "No node 12 in file 442 for this P.O."                                                            | No electronic signature in Procurement & Accounting Transactions file (file 442).                                                                           |
| NP12           | "INVOICE ADDRESS pointer is missing.”                                                             | No invoice address in Procurement & Accounting Transactions file (file 442).                                                                                |
| NPH            | "No phone number for this PPM in the person file."                                                | The P&C user does not have a phone number entry in the Person File under his/her entry.                                                                     |
| NPH            | "No phone number for this PPM in the person file."                                                | The person file does not have a phone number listed for this PPM.                                                                                           |
| NPHN           | "No phone number node in the person file for this PPM."                                           | The P&C user does not have a phone number node in the Person File under his/her record entry.                                                               |
| NPIA           | "Invoice address missing."                                                                        | There is no Invoice Address in node 12 in the Procurement & Accounting Transactions file.                                                                   |
| NPO0           | "Zero node of record missing. Unable to check further."                                           | No Procurement & Accounting Transactions file (file 442) entry exists.                                                                                      |
| NPO1           | "Node 1 missing in record."                                                                       | No VENDOR, SHIP TO or ACCOUNTING information found for the Procurement & Accounting Transactions file record.                                               |
| NPOD           | "No purchase order date in file 442 for this P.O."                                                | There is no Purchase Order Date in the Procurement & Accounting Transactions file (file 442).                                                               |
| NPPM           | "No purchasing agent entry in file 442 for this P.O."                                             | There is no Purchasing Agent/PPM Agent entry in the Procurement & Accounting Transactions file.                                                             |
| NPPT           | "No prompt payment terms entered in P.O."                                                         | There are no Prompt Payment Terms entries in Procurement & Accounting Transactions file (file 442).                                                         |
| NQTY^\<LIN\>   | "No quantity listed for this ITEM."                                                               | There is no Quantity listed for the Line Item Number (\<LIN\>) in the Procurement & Accounting Transactions file.                                           |
| NRL            | "No receiving location node in file 411."                                                         | No Receiving Location node in Admin. Activity Site Parameter file.                                                                                          |
| NSC            | "No Source Code for type of order for this P.O."                                                  | No source code entry in the Procurement & Accounting Transactions file.                                                                                     |
| NSIT           | "No site entry in file 442."                                                                      | No Site entry in Procurement & Accounting Transactions file.                                                                                                |
| NSP0^\<SITE\>  | "No SITE information in file 411."                                                                | No FACILITY TYPE pointer in Admin. Activity Site Parameter file for SITE in Procurement & Accounting Transactions file.                                     |
| NST0           | "No record in the state file.”                                                                    | No STATE entry in State file (file 5) for Vendor Address State pointer in Vendor file.                                                                      |
| NSTA           | "Abbreviation missing in state file entry."                                                       | No Abbreviation in State file.                                                                                                                              |
| NSTA           | "No Abbreviation in State file."                                                                  | There is no abbreviation in the state file for this state.                                                                                                  |
| NSTDP          | "No State file pointer in Direct Delivery Address in 440.2."                                      | No State file pointer in Direct Delivery Address field in Direct Delivery Patients file.                                                                    |
| NSTL           | "No Ship to pointer to entry in file 441."                                                        | No Ship To pointer to Admin. Activity Site Parameter file.                                                                                                  |
| NSTP           | "No Vendor Address pointer to the State file."                                                    | No Vendor Address State file pointer in the Vendor file.                                                                                                    |
| NSTS           | "There is no Ship To suffix for receiving location for this EDI P.O."                             | The Ship To entry for this purchase order in file 442 cannot be found in file 411 (Ship To Suffix). An EDI purchase order requires the Ship To suffix.      |
| NSTT           | "No State file pointer in Receiving Location in file 411."                                        | No State File pointer in Receiving Location multiple in Admin. Activity Site Parameter file.                                                                |
| NUNI^\<LIN\>   | "No name entry in unit of purchase file for unit of purchase pointer in ITEM entry in P.O. file." | No Name entry in the Unit of Issue file (file 420.5) for the Unit of Purchase entry for the \<LIN\> Item in the Procurement & Accounting Transactions file. |
| NUOP^\<LIN\>   | "No unit of purchase pointer for this ITEM."                                                      | No Unit of Purchase pointer entered for the \<LIN\> Item in the Procurement & Accounting Transactions file.                                                 |
| NUPN^\<LIN\>   | "No entry in unit of issue file for unit of purchase pointer in ITEM entry in P.O. file."         | No entry in the Unit of Issue file (file 420.5) for the Unit of Purchase entry for the \<LIN\> Item in the Procurement & Accounting Transactions file.      |
| NV0            | "No vendor record found in vendor file."                                                          | No Vendor file (file 440) entry for the Vendor pointer from Procurement & Accounting Transactions file (file 442).                                          |
| NVID           | "Missing a vendor ID number for an EDI vendor."                                                   | There is no Vendor ID Number for an EDI Vendor in the Vendor file.                                                                                          |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1358</strong></td>
<td>VA Form 1358 Estimated Obligation or Change in Obligation.</td>
</tr>
<tr class="even">
<td><strong>2138</strong></td>
<td>VA Form 90-2138, Order for Supplies or Services. First page of a VA Purchase Order.</td>
</tr>
<tr class="odd">
<td><strong>2139</strong></td>
<td>VA Form 90-2139, Order for Supplies or Services (Continuation). This is a continuation sheet for the 2138 form.</td>
</tr>
<tr class="even">
<td><strong>2237</strong></td>
<td>VA Form 90-2237, Request, Turn-in and Receipt for Property or Services. Used to request goods and services.</td>
</tr>
<tr class="odd">
<td><strong>A&amp;MM</strong></td>
<td>Acquisition and Materiel Management Service.</td>
</tr>
<tr class="even">
<td><strong>AACS</strong></td>
<td>Automated Allotment Control System--Central computer system developed by VHA to disburse funding from VACO to field stations.</td>
</tr>
<tr class="odd">
<td><strong>Accounting Technician</strong></td>
<td>Fiscal employee responsible for obligation and payment of received goods and services.</td>
</tr>
<tr class="even">
<td><strong>Activity Code</strong></td>
<td>The last two digits of the AACS number. It is defined by each station.</td>
</tr>
<tr class="odd">
<td><strong>ADP Security Officer</strong></td>
<td>The individual at your station who is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing file access.</td>
</tr>
<tr class="even">
<td><strong>Agent Cashier</strong></td>
<td>The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.</td>
</tr>
<tr class="odd">
<td><strong>ALD Code</strong></td>
<td>Appropriation Limitation Department. A set of Fiscal codes that identifies the appropriation used for funding.</td>
</tr>
<tr class="even">
<td><strong>Allowance table</strong></td>
<td>Reference table in FMS that provides financial information at the level immediately above the AACS, or sub-allowance level.</td>
</tr>
<tr class="odd">
<td><strong>Amendment</strong></td>
<td>A document that changes the information contained in a specified Purchase Order. Amendments are processed by the Purchasing &amp; Contracting section of A&amp;MM and obligated by Fiscal Service.</td>
</tr>
<tr class="even">
<td><strong>AMIS</strong></td>
<td>Automated Management Information System.</td>
</tr>
<tr class="odd">
<td><strong>Application Coordinator</strong></td>
<td>The individuals responsible for the implementation, training and trouble-shooting of a software package within a service. IFCAP requires there be an Application Coordinator designated for Fiscal Service, A&amp;MM Service.</td>
</tr>
<tr class="even">
<td><strong>Approve Requests</strong></td>
<td>The use of an electronic signature by a Control Point Official to approve a 2237, 1358 or other request form and transmit said request to A&amp;MM/Fiscal.</td>
</tr>
<tr class="odd">
<td><strong>Approving Official</strong></td>
<td>A user that approves reconciliations to ensure that they are correct and complete.</td>
</tr>
<tr class="even">
<td><strong>Authorization</strong></td>
<td>Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.</td>
</tr>
<tr class="odd">
<td><strong>Authorization Balance</strong></td>
<td>The amount of money remaining that can be authorized against the 1358. The service balance minus total authorizations.</td>
</tr>
<tr class="even">
<td><strong>Batch Number</strong></td>
<td>A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number.</td>
</tr>
<tr class="odd">
<td><strong>Breakout Code</strong></td>
<td>A set of A&amp;MM codes which identifies a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.).</td>
</tr>
<tr class="even">
<td><strong>Budget Analyst</strong></td>
<td>Fiscal employee responsible for distributing and transferring funds.</td>
</tr>
<tr class="odd">
<td><strong>Budget Object Code</strong></td>
<td>Fiscal accounting element that tells what kind of item or service is being procured. Budget object codes are listed in VA Handbook 4671.2</td>
</tr>
<tr class="even">
<td><strong>Budget Sort Category</strong></td>
<td>Used by Fiscal Service to identify the allocation of funds throughout their facility.</td>
</tr>
<tr class="odd">
<td><strong>CCS</strong></td>
<td>The Credit Card System. This is the database in Austin that processes the credit card information from the external Credit Card Vendor system, currently CitiDirect, and then passes information on to FMS and IFCAP.</td>
</tr>
<tr class="even">
<td><strong>CC</strong></td>
<td>Credit Charge entry identifier used by FMS and CCS for charges paid to Vendor thru Credit Card payment process.</td>
</tr>
<tr class="odd">
<td><strong>Ceiling Transactions</strong></td>
<td>Funding distributed from Fiscal Service to IFCAP Control Points for spending. The Budget Analyst initiates these transactions using the Funds Distribution options.</td>
</tr>
<tr class="even">
<td><strong>Classification of Request</strong></td>
<td>An identifier a Control Point can assign to track requests that fall into a category, e.g., Memberships, Replacement Parts, Food Group III.</td>
</tr>
<tr class="odd">
<td><strong>Common Numbering Series</strong></td>
<td>This is a pre-set series of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinators establish the Common Numbering Series used by each facility.</td>
</tr>
<tr class="even">
<td><strong>Control Point</strong></td>
<td>Financial element, existing ONLY in IFCAP, which corresponds to a set of elements in FMS that include the Account Classification Code (ACC) and define the Sub-Allowance on the FMS system. Used to permit the tracking of monies to a specified service, activity or purpose from an Appropriation or Fund.</td>
</tr>
<tr class="odd">
<td><strong>Control Point Clerk</strong></td>
<td>The user within the service who is designated to input requests (2237s) and maintain the Control Point records for a Service.</td>
</tr>
<tr class="even">
<td><strong>Control Point Official</strong></td>
<td>The individual authorized to expend government funds for ordering of supplies and services for their Control Point(s). This person has all of the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.</td>
</tr>
<tr class="odd">
<td><strong>Control Point Official's Balance</strong></td>
<td>A running record of all the transactions generated and approved for a Control Point from within IFCAP and also. Effects changes to the control point that are initiated directly from within the FMS system. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.</td>
</tr>
<tr class="even">
<td><strong>Control Point Requestor</strong></td>
<td>The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. This user can only view or edit their own requests. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&amp;MM.</td>
</tr>
<tr class="odd">
<td><strong>Cost Center</strong></td>
<td>Cost Centers are unique numbers that define a service. One cost center must be attached to every Fund Control Point. This enables costs to be captured by service. Cost centers are listed in VA Handbook 4671.1.</td>
</tr>
<tr class="even">
<td><strong>Date Committed</strong></td>
<td>The date that you want IFCAP to commit funds to the purchase.</td>
</tr>
<tr class="odd">
<td><strong>Default</strong></td>
<td>A suggested response that is provided by the system.</td>
</tr>
<tr class="even">
<td><strong>Deficiency</strong></td>
<td>When a budget has obligated and expended more than it was funded.</td>
</tr>
<tr class="odd">
<td><strong>Delinquent Delivery Listing</strong></td>
<td>A listing of all the Purchase Orders that have not had all the items received by the Warehouse on IFCAP. It is used to contact the vendor for updated delivery information.</td>
</tr>
<tr class="even">
<td><strong>Delivery Order</strong></td>
<td>An order for an item that the VA purchases through an established contract with a vendor who supplies the items.</td>
</tr>
<tr class="odd">
<td><strong>Direct Delivery Patient</strong></td>
<td>A patient who has been designated to have goods delivered directly to him/her from the vendor.</td>
</tr>
<tr class="even">
<td><strong>Discount Item</strong></td>
<td>This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.</td>
</tr>
<tr class="odd">
<td><strong>EDI Vendor</strong></td>
<td>A vendor with whom the VA has negotiated an arrangement to submit, accept and fill orders electronically.</td>
</tr>
<tr class="even">
<td><strong>Electronic Data Interchange (EDI)</strong></td>
<td>Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.</td>
</tr>
<tr class="odd">
<td><strong>Electronic Signature</strong></td>
<td>The electronic signature code replaces the written signature on all IFCAP documents used within your facility. Documents going off-station will require a written signature as well.</td>
</tr>
<tr class="even">
<td><strong>Expenditure Request</strong></td>
<td>A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).</td>
</tr>
<tr class="odd">
<td><strong>FCP</strong></td>
<td>Fund Control Point (see Control Point).</td>
</tr>
<tr class="even">
<td><strong>Federal Tax ID</strong></td>
<td>A unique number that identifies your station to the Internal Revenue Service.</td>
</tr>
<tr class="odd">
<td><strong>Fiscal Balance</strong></td>
<td>The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidation submitted against the obligation.</td>
</tr>
<tr class="even">
<td><strong>Fiscal Quarter</strong></td>
<td>The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.</td>
</tr>
<tr class="odd">
<td><strong>Fiscal Year</strong></td>
<td>Twelve-month period from October 1 to September 30.</td>
</tr>
<tr class="even">
<td><strong>FMS</strong></td>
<td>Financial Management System, the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides for flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.</td>
</tr>
<tr class="odd">
<td><strong>FOB</strong></td>
<td><strong>Freight on Board.</strong> An FOB of "Destination" means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of "Origin" means the Vendor has paid shipping costs directly to the shipper and then will include them on their Invoice.</td>
</tr>
<tr class="even">
<td><strong>FPDS</strong></td>
<td>Federal Procurement Data System.</td>
</tr>
<tr class="odd">
<td><strong>FTEE</strong></td>
<td>Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned an FTEE of 0.5, as would a full-time employee that worked for half of a year.</td>
</tr>
<tr class="even">
<td><strong>Fund Control Point</strong></td>
<td>IFCAP accounting element that is not used by FMS. See also control point.</td>
</tr>
<tr class="odd">
<td><strong>Funds Control</strong></td>
<td>A group of Control Point options that allow the Control Point Clerk and/or Official to maintain and reconcile their funds.</td>
</tr>
<tr class="even">
<td><strong>Funds Distribution</strong></td>
<td>A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.</td>
</tr>
<tr class="odd">
<td><strong>GBL</strong></td>
<td>Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of $250.00.</td>
</tr>
<tr class="even">
<td><strong>GL</strong></td>
<td>General Ledger.</td>
</tr>
<tr class="odd">
<td><strong>Identification Number</strong></td>
<td>A computer-generated number assigned to a code sheet.</td>
</tr>
<tr class="even">
<td><strong>Imprest Funds</strong></td>
<td>Monies used for cash or 3rd party draft purchases at a VA facility.</td>
</tr>
<tr class="odd">
<td><strong>Integrated Supply Management System (ISMS)</strong></td>
<td>ISMS is the system that replaced LOG I for Expendable Inventory.</td>
</tr>
<tr class="even">
<td><strong>ISMS</strong></td>
<td>See Integrated Supply Management System.</td>
</tr>
<tr class="odd">
<td><strong>Item File</strong></td>
<td>A listing of items specified by A&amp;MM service as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history.</td>
</tr>
<tr class="even">
<td><strong>Item History</strong></td>
<td>Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.</td>
</tr>
<tr class="odd">
<td><strong>Item Master Number</strong></td>
<td>A computer generated number used to identify an item in the Item File.</td>
</tr>
<tr class="even">
<td><strong>Justification</strong></td>
<td>A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source.</td>
</tr>
<tr class="odd">
<td><strong>Liquidation</strong></td>
<td>The amount of money posted to the 1358 or Purchase Order as a payment to the vendor. They are processed through payment/invoice tracking.</td>
</tr>
<tr class="even">
<td><strong>LOG I</strong></td>
<td>LOG I is the name of the Logistics A&amp;MM computer located at the Austin Automation Center. This system continues to support the Consolidated Memorandum of Receipt.</td>
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
<td><strong>Obligation</strong></td>
<td>The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of an Order.</td>
</tr>
<tr class="even">
<td><strong>Obligation (Actual) Amount</strong></td>
<td>The actual dollar figure obligated by Fiscal Service for a Purchase Order. The Control Point's records are updated with actual cost automatically when Fiscal obligates the document on IFCAP.</td>
</tr>
<tr class="odd">
<td><strong>Obligation Data</strong></td>
<td>A Control Point option that allows the Control Point Clerk and/or Budget Analyst to enter data not recorded by IFCAP.</td>
</tr>
<tr class="even">
<td><strong>Obligation Number</strong></td>
<td>The 6-character number assigned to orders, requisitions and 1358s. (i.e. C prefix number that Fiscal Service assigns to the 1358.)</td>
</tr>
<tr class="odd">
<td><strong>Organization Code</strong></td>
<td>Accounting element functionally comparable to Cost Center, but used to organize purchases by the budget that funded them, not the purposes for spending the funds.</td>
</tr>
<tr class="even">
<td><strong>Outstanding 2237</strong></td>
<td>A&amp;MM report that lists all the IFCAP generated 2237s pending action in A&amp;MM.</td>
</tr>
<tr class="odd">
<td><strong>Partial</strong></td>
<td>A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.</td>
</tr>
<tr class="even">
<td><strong>Partial Date</strong></td>
<td>The date that a warehouse clerk created a receiving report for a shipment.</td>
</tr>
<tr class="odd">
<td><strong>PAT Number</strong></td>
<td>Pending Accounting Transaction number - the primary FMS reference number. See also Obligation Number.</td>
</tr>
<tr class="even">
<td><strong>Personal Property Management</strong></td>
<td>A section of A&amp;MM Service responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support.</td>
</tr>
<tr class="odd">
<td><strong>POA</strong></td>
<td>Purchase Order Acknowledgment. The message received electronically from an EDI vendor acknowledging the placement of an order.</td>
</tr>
<tr class="even">
<td><strong>PPM</strong></td>
<td>Personal Property Management now referred to at most sites as Acquisition and Materiel Management Service.</td>
</tr>
<tr class="odd">
<td><strong>Program Code</strong></td>
<td>Accounting element that identifies the VA initiative or program that the purchase will support.</td>
</tr>
<tr class="even">
<td><strong>Prompt Payment Terms</strong></td>
<td>The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).</td>
</tr>
<tr class="odd">
<td><strong>Purchase Card</strong></td>
<td>A card, similar to a credit card that Purchase Card Users use to make purchases. Purchase Cards are not credit cards but debit cards that spend money out of a deposited balance of VA funds.</td>
</tr>
<tr class="even">
<td><strong>Purchase Card Coordinator</strong></td>
<td>A person authorized by a VA station to monitor and resolve delinquent purchase card orders, help VA services record, edit and approve purchase card orders in a timely manner, assign purchase cards to IFCAP users, and monitor the purchase card expenses of VAMC services.</td>
</tr>
<tr class="odd">
<td><strong>Purchase Card Orders</strong></td>
<td>Orders funded by a purchase card.</td>
</tr>
<tr class="even">
<td><strong>Purchase Card User</strong></td>
<td>A person who uses a purchase card. Purchase Card Users are responsible for recording their purchase card orders in IFCAP.</td>
</tr>
<tr class="odd">
<td><strong>Purchase History Add (PHA)</strong></td>
<td>Information about purchase orders which is automatically sent to Austin for archiving. This same transaction is also used to send a PO for EDI processing.</td>
</tr>
<tr class="even">
<td><strong>Purchase History Modify (PHM)</strong></td>
<td>Information about amendments that is automatically sent to Austin for archiving.</td>
</tr>
<tr class="odd">
<td><strong>Purchase Order</strong></td>
<td>A government document authorizing the purchase of the goods or services at the terms indicated.</td>
</tr>
<tr class="even">
<td><strong>Purchase Order Acknowledgment</strong></td>
<td>Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).</td>
</tr>
<tr class="odd">
<td><strong>Purchase Order Status</strong></td>
<td>The status of completion of a purchase order (e.g., Pending Contracting Officer's Signature, Pending Fiscal Action, Partial Order Received, etc.).</td>
</tr>
<tr class="even">
<td><strong>Purchasing Agents</strong></td>
<td>A&amp;MM employees legally empowered to create purchase orders to obtain goods and services from commercial vendors.</td>
</tr>
<tr class="odd">
<td><strong>Quarterly Report</strong></td>
<td>A Control Point listing of all transactions (Ceilings, Obligations, Adjustments) made against a Control Point's Funds.</td>
</tr>
<tr class="even">
<td><strong>Quotation for Bid</strong></td>
<td>Standard Form 18. Used by Purchasing Agents to obtain written bids from vendors. May be created automatically and transmitted electronically within the Purchasing Agent's module.</td>
</tr>
<tr class="odd">
<td><strong>Receiving Report</strong></td>
<td>The VA document used to indicate the quantity and dollar value of the goods being received.</td>
</tr>
<tr class="even">
<td><strong>Reconciliation</strong></td>
<td>Comparing of two records to validate IFCAP Purchase Card orders. Purchase Card Users compare IFCAP generated purchase card order data with the CC transaction sent from the CCS system in Austin.</td>
</tr>
<tr class="odd">
<td><strong>Reference Number</strong></td>
<td>Also known as the Transaction Number. The computer generated number that identifies a request. It is comprised of the: Station Number-Fiscal Year-Quarter - Control Point - 4-digit Sequence Number.</td>
</tr>
<tr class="even">
<td><strong>Repetitive (PR Card) Number</strong></td>
<td>See Item Master Number.</td>
</tr>
<tr class="odd">
<td><p><strong>Repetitive Item List</strong></p>
<p><strong>(RIL)</strong></p></td>
<td>A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate 2237 requests from the list. A RIL can be created by using the Auto-Generate feature within the Inventory portion of the package.</td>
</tr>
<tr class="even">
<td><strong>Requestor</strong></td>
<td>See “Control Point Requestor.”</td>
</tr>
<tr class="odd">
<td><strong>Requisition</strong></td>
<td>An order from a Government vendor.</td>
</tr>
<tr class="even">
<td><strong>Running Balance</strong></td>
<td>A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.</td>
</tr>
<tr class="odd">
<td><strong>Section Request</strong></td>
<td>A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.</td>
</tr>
<tr class="even">
<td><strong>Service Balance</strong></td>
<td>The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorizations created by the service.</td>
</tr>
<tr class="odd">
<td><strong>SF-18</strong></td>
<td>Request for Quotation.</td>
</tr>
<tr class="even">
<td><strong>SF-30</strong></td>
<td>Amendment of Solicitation/Modification of Contract.</td>
</tr>
<tr class="odd">
<td><strong>Short Description</strong></td>
<td>A phrase that describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).</td>
</tr>
<tr class="even">
<td><strong>Site Parameters</strong></td>
<td>Information (such as Station Number, Cashier's address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter file.</td>
</tr>
<tr class="odd">
<td><strong>Sort Group</strong></td>
<td>An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.</td>
</tr>
<tr class="even">
<td><strong>Sort Order</strong></td>
<td>The order in which the budget categories will appear on the budget distribution reports.</td>
</tr>
<tr class="odd">
<td><strong>Special Remarks</strong></td>
<td>A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.</td>
</tr>
<tr class="even">
<td><strong>Stacked Documents</strong></td>
<td>The POs, RRs &amp; 1358s that are sent electronically to Fiscal and stored in a file for printing at a later time rather than being printed immediately.</td>
</tr>
<tr class="odd">
<td><strong>Status of Funds</strong></td>
<td>Fiscal's on-line status report of the monies available to a Control Point. FMS updates this information automatically.</td>
</tr>
<tr class="even">
<td><strong>Sub-control Point</strong></td>
<td>A user defined assignment of all or part of a ceiling transaction to a specific category (sub-control point) within a Control Point, Transactions can then be posted against this sub-control point and a report can be generated to track use of specified funding within the overall control point.</td>
</tr>
<tr class="odd">
<td><strong>Sub-cost Center</strong></td>
<td>A subcategory of Cost Center. IFCAP will not utilize a 'sub-cost center' field, but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field.</td>
</tr>
<tr class="even">
<td><strong>Tasked Job</strong></td>
<td>A job, usually a printout that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.</td>
</tr>
<tr class="odd">
<td><strong>TDA</strong></td>
<td>See "Transfer of Disbursing Authority.”</td>
</tr>
<tr class="even">
<td><strong>Total Authorizations</strong></td>
<td>The total amount of the authorizations created for the 1358 obligation.</td>
</tr>
<tr class="odd">
<td><strong>Total Liquidations</strong></td>
<td>The total amount of the liquidations against the 1358 obligation.</td>
</tr>
<tr class="even">
<td><strong>Transaction Number</strong></td>
<td>The number of the transaction that funded a Control Point (See Budget Analyst User's Guide). It consists of the Station Number - Fiscal Year - Quarter - Control Point - Sequence Number.</td>
</tr>
<tr class="odd">
<td><strong>Transfer of Disbursing Authority</strong></td>
<td>The method used to allocate funds to a VA facility.</td>
</tr>
<tr class="even">
<td><strong>Transmission Number</strong></td>
<td>A sequential number given to a data string when it is transmitted to the Austin DPC; used for tracking message traffic.</td>
</tr>
<tr class="odd">
<td><strong>Type Code</strong></td>
<td>A set of A&amp;MM codes that provides information concerning the vendor size and type of competition sought on a purchase order.</td>
</tr>
<tr class="even">
<td><strong>Vendor file</strong></td>
<td>An IFCAP file of vendor information solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. The debtor's address may be drawn from this file, but is maintained separately. If the desired vendor is not in the file, contact A&amp;MM Service to have it added.</td>
</tr>
<tr class="odd">
<td><strong>Vendor ID Number</strong></td>
<td>The ID number assigned to a vendor by the FMS Vendor unit.</td>
</tr>
<tr class="even">
<td><strong>VRQ</strong></td>
<td>FMS Vendor Request document. When a new vendor is added to IFCAP a VRQ message is sent electronically to the Austin FMS Vendor unit to determine if the vendor exists in the central vendor system. If the vendor is not in the system, Austin will confirm information and establish the vendor in the central file. If vendor exists in central file already, Austin will verify the data. See also VUP.</td>
</tr>
<tr class="odd">
<td><strong>VUP</strong></td>
<td>Vendor Update Message. This message is sent electronically from the FMS system to ALL IFCAP sites to ensure that the local vendor file contains the same data as the central vendor file in Austin. This message will contain the FMS Vendor ID for the vendor and also the Alternate Address Indicator if applicable. See also VRQ.</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2237, 34
Adjust Inventory Quantity, 20, 22, 25
FMS, 25
Invoices, 43, 44
Item Master File, 27
Numbering system, 5
Paragraph numbering, 5
Purchase Order, 43, 44, 45
Requirements Analyst, 5
Source Code, 45
Transaction Number, 18, 19
Vendor file, 46
