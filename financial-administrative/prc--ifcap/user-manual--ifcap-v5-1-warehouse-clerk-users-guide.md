---
title: IFCAP Version 5.1 Warehouse Clerk User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Warehouse Clerk User's Guide
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
menu_options: 4
description: 
audience: 
keywords: 
  - order
  - purchase
  - receiving
  - class
  - number
  - report
  - table
  - contents
  - warehouse
  - ifcap
page_count: 0
word_count: 9512
section_count: 17
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1warehouse_clerk.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1warehouse_clerk.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP)Version 5.1Warehouse ClerkUser's Guide

![](ifcap-version-5-1-warehouse-clerk-user-s-guide/001.png)

March 2026Department of Veterans AffairsOffice of Information and Technology (OI&T)Management, Enrollment, and Financial Systems

Revision History

Initiated on 12/29/04

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 49%" />
<col style="width: 21%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description (Patch # if applicable)</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>March 2026</td>
<td>4.0</td>
<td><p>Updates based on patch PRC*5.1*252.</p>
<p>This manual has been updated to comply with the VA OIT-mandated user guide template.</p></td>
<td><p>Technical Writer,</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="odd">
<td>October 2011</td>
<td>3.0</td>
<td>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358. See page <a href="#PRC_158_A">20</a>.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>12/29/04</td>
<td>2.0</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>12/29/04</td>
<td>1.0</td>
<td>PDF file checked for accessibility to readers with disabilities.</td>
<td><p>Technical Writer,</p>
<p>Department of Veterans Affairs</p></td>
</tr>
</tbody>
</table>

###########  PREFACE

This user's guide is for VA personnel that use the Warehouse menus in the Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) system.

Table of Contents

1 INTRODUCTION [1](#introduction)

1.1 The Role of the Warehouse Clerk [1](#the-role-of-the-warehouse-clerk)

1.2 How to Use This Manual [1](#how-to-use-this-manual)

1.3 Reference Numbering System [1](#reference-numbering-system)

1.4 Package Management, Legal Requirements and Security Measures [1](#package-management-legal-requirements-and-security-measures)

1.5 Package Operation [2](#package-operation)

1.6 Features [2](#features)

1.6.1 Receiving Report Processing [2](#receiving-report-processing)

1.6.2 Shipping Charges [2](#shipping-charges)

2 RECEIVING GOODS IN THE WAREHOUSE [3](#receiving-goods-in-the-warehouse)

2.1 Introduction [3](#introduction-1)

2.2 Receiving Goods and Equipment [3](#receiving-goods-and-equipment)

2.2.1 Menu Path [3](#menu-path)

2.2.2 Review the Requisition or Purchase Order [3](#review-the-requisition-or-purchase-order)

2.2.3 Check for Shipping Discrepancy [4](#check-for-shipping-discrepancy)

2.2.4 Receipt of Item [6](#receipt-of-item)

2.3 What if the Requisition or Purchase Order Number Is Not on the Invoice? [7](#what-if-the-requisition-or-purchase-order-number-is-not-on-the-invoice)

2.4 What if the Requisition or Purchase Order Number Is Not in IFCAP? [8](#what-if-the-requisition-or-purchase-order-number-is-not-in-ifcap)

3 SUPPLEMENTARY MENU OPTIONS [8](#supplementary-menu-options)

3.1 Introduction [8](#introduction-2)

3.2 Print Receiving Report [8](#print-receiving-report)

3.2.1 Menu Path [8](#menu-path-1)

3.2.2 Select Order Number [9](#select-order-number)

3.2.3 Enter Date [9](#enter-date)

3.3 Purchase Order Display [10](#purchase-order-display)

3.3.1 Menu Path [10](#menu-path-2)

3.3.2 Enter Order Number [10](#enter-order-number)

3.3.3 Display Order [10](#display-order)

3.3.4 Review Receiving Report [14](#review-receiving-report)

3.4 Delete a Receiving Report [15](#delete-a-receiving-report)

3.4.1 Introduction [15](#introduction-3)

3.4.2 Menu Path [15](#menu-path-3)

3.4.3 Enter Order Number [15](#enter-order-number-1)

3.4.4 Display Order [16](#display-order-1)

3.5 Warehouse Receiving Statistics [17](#warehouse-receiving-statistics)

3.5.1 Introduction [17](#introduction-4)

3.5.2 Menu Path [17](#menu-path-4)

3.5.3 List Statistics [18](#list-statistics)

3.5.4 Print Statistics [18](#print-statistics)

3.6 Imprest Funds Purchase Orders Receiving [20](#imprest-funds-purchase-orders-receiving)

3.6.1 Introduction [20](#introduction-5)

3.6.2 Menu Path [20](#menu-path-5)

3.6.3 Enter Order Number [21](#enter-order-number-2)

3.6.4 Enter Delivery Date [21](#enter-delivery-date)

4 ERROR MESSAGES AND THEIR RESOLUTION [22](#error-messages-and-their-resolution)

5 Glossary [24](#glossary)

6 Index [38](#index)

# INTRODUCTION


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [INTRODUCTION](#introduction)
  - [The Role of the Warehouse Clerk](#the-role-of-the-warehouse-clerk)
  - [How to Use This Manual](#how-to-use-this-manual)
  - [Reference Numbering System](#reference-numbering-system)
  - [Package Management, Legal Requirements and Security Measures](#package-management-legal-requirements-and-security-measures)
  - [Package Operation](#package-operation)
  - [Features](#features)
    - [Receiving Report Processing](#receiving-report-processing)
    - [Shipping Charges](#shipping-charges)
- [RECEIVING GOODS IN THE WAREHOUSE](#receiving-goods-in-the-warehouse)
  - [Introduction](#introduction-1)
  - [Receiving Goods and Equipment](#receiving-goods-and-equipment)
    - [Menu Path](#menu-path)
    - [Review the Requisition or Purchase Order](#review-the-requisition-or-purchase-order)
    - [Check for Shipping Discrepancy](#check-for-shipping-discrepancy)
    - [Receipt of Item](#receipt-of-item)
  - [What if the Requisition or Purchase Order Number Is Not on the Invoice?](#what-if-the-requisition-or-purchase-order-number-is-not-on-the-invoice)
  - [What if the Requisition or Purchase Order Number Is Not in IFCAP?](#what-if-the-requisition-or-purchase-order-number-is-not-in-ifcap)
- [SUPPLEMENTARY MENU OPTIONS](#supplementary-menu-options)
  - [Introduction](#introduction-2)
  - [Print Receiving Report](#print-receiving-report)
    - [Menu Path](#menu-path-1)
    - [Select Order Number](#select-order-number)
    - [Enter Date](#enter-date)
  - [Purchase Order Display](#purchase-order-display)
    - [Menu Path](#menu-path-2)
    - [Enter Order Number](#enter-order-number)
    - [Display Order](#display-order)
    - [Review Receiving Report](#review-receiving-report)
  - [Delete a Receiving Report](#delete-a-receiving-report)
    - [Introduction](#introduction-3)
    - [Menu Path](#menu-path-3)
    - [Enter Order Number](#enter-order-number-1)
    - [Display Order](#display-order-1)
  - [Warehouse Receiving Statistics](#warehouse-receiving-statistics)
    - [Introduction](#introduction-4)
    - [Menu Path](#menu-path-4)
    - [List Statistics](#list-statistics)
    - [Print Statistics](#print-statistics)
  - [Imprest Funds Purchase Orders Receiving](#imprest-funds-purchase-orders-receiving)
    - [Introduction](#introduction-5)
    - [Menu Path](#menu-path-5)
    - [Enter Order Number](#enter-order-number-2)
    - [Enter Delivery Date](#enter-delivery-date)
- [ERROR MESSAGES AND THEIR RESOLUTION](#error-messages-and-their-resolution)
- [Glossary](#glossary)
- [Index](#index)

## The Role of the Warehouse Clerk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In IFCAP, VA employees request goods and services by creating electronic requests. Those requests are funded by an operating budget called a Control Point. Purchasing Agents and Requisition Clerks are responsible for creating purchase orders and requisitions to fulfill those requests. Control Point users may also create Purchase Card Orders. As vendors deliver items from these purchase orders, requisitions and purchase card orders to the warehouse, warehouse staff will record the arrival of the items, deliver the items, and record any shipping discrepancies. Not all purchase card orders are received in the Warehouse.

## How to Use This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual explains how to perform the role of the Warehouse Clerk by dividing that role into small, manageable tasks. The authors of this manual have listed these tasks in successive order so that each instruction builds on the information from previous instructions. This will allow new Warehouse Clerks to use this manual as a tutorial by following the instructions in the guide from beginning to end. Experienced Warehouse Clerks can use this manual as a reference tool by using the index and table of contents.

## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses a special paragraph numbering system to allow users to understand how the sections of the manual relate to each other. For example, this paragraph is section 1.3. This means that this paragraph is the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections 1.3.1 and 1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third subsection of Chapter 1. All clear? Actually, all this means is that users that want to divide their reading into manageable lessons can concentrate on one section and all of its subsections, for example, section 1.3.5.4 and all of its subsections would make a coherent lesson.

## Package Management, Legal Requirements and Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to use IFCAP to enter received goods and resolve shipping discrepancies, IFCAP users are given access to a set of IFCAP menu options designed for their use. Some of these menu options are additionally controlled by access "keys." The Information Resources Management Service at their facility administers these access keys to individual Warehouse Clerks. Also, each IFCAP user has a "signature code" that functions legally as their signature. IFCAP users must enter an electronic signature code password to create any form in IFCAP that would require an authorizing signature if they created the form manually.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Novice Warehouse Clerks will be unfamiliar with the information that some of the IFCAP prompts require. IFCAP provides three levels of explanations for the prompts. Enter a question mark at the prompt to read a description of the prompt, two question marks to read a more complex explanation of the prompt, and three question marks to read a complete description of the prompt and read a list of acceptable responses to the prompt.

## Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Receiving Report Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Warehouse/Receiving functionality allows users to create Receiving Reports for items received from a Vendor. IFCAP can transmit Receiving Report to Fiscal for further processing. After Fiscal processes the Receiving Report they determine if the Receiving Report information will be sent to Austin. Receiving Reports will eventually be posted into the CAPPS system in Austin to permit payment to the Vendor. The credit card holder may do the purchase card receiving process in the Service.

The Receiving Report goes to a system called IFRR/NRR. This system microfilms the receiving reports and gives them an identifying “DLN” (document locator number). The IFCAP receiving report will be processed into CAPPS and IFRR will create and transmit the RT document, including the DLN, to FMS. If a Federal Receiving Report is sent to Austin the INRR system will process those.

### Shipping Charges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Shipping charges are applied to the first partial shipment received for an order. Users that mistakenly enter a partial Receiving Report for goods that have not been received can delete the partial Receiving Report. If they delete the partial Receiving Report, IFCAP will ask the user if they also want to delete the shipping charges associated with that receiving report, using the following prompt:

Shipping charges are \$ , Do you wish to delete? Y/N//

If other partials have been received, this message will not appear. If the shipping charges are removed with the first partial they will be re-established when the next partial is received.

# RECEIVING GOODS IN THE WAREHOUSE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter explains how to use IFCAP to report the receipt of goods in the warehouse, and how to locate the IFCAP record of the purchase order for the goods.

## Receiving Goods and Equipment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Receipt of Purchase Order from the Warehouse Menu. Enter a station number. At the PURCHASE ORDER: prompt, enter the purchase order number on the packing slip or invoice that came with the goods. If the order number is not on the invoice, skip to section 2.3.

Select Warehouse Option: ?

Receipt of Purchase Order

Print Receiving Report

Purchase Order Display

Delete a Receiving Report

Warehouse Receiving Statistics

Imprest Funds Purchase Orders Receiving

Select Warehouse Option: Receipt of Purchase Order

Select STATION NUMBER ('^' TO EXIT): 111// ANYTOWN,NV

### Review the Requisition or Purchase Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the purchase order number with the station number as a prefix, the type of order, the status of the order, the Fund Control Point, total amount of the order, and the purchasing agent that created the purchase order. Type Y for yes at the Review Purchase Order?: prompt to review the items on the order.

PURCHASE ORDER: a00002 111-A00002 01-28-00 ST Ordered and Obligated

FCP: 081 \$ 206.20

PA/PPM/AUTHORIZED BUYER: IFBUYER,ONE

REVIEW PURCHASE ORDER? NO// Y (YES)

### Check for Shipping Discrepancy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Compare the goods received to the items on the requisition or purchase order record in IFCAP. The IFCAP line item for the goods should be the same as the goods delivered, unless the requisition or purchase order indicates that the item has been extracted for purchase elsewhere or canceled. Otherwise, if the goods delivered are not the same in type or quantity, there is a shipping discrepancy. If there is a discrepancy other than receipt of lesser or greater quantity than IFCAP lists for the purchase, quit the Receipt of Purchase Order option by entering a caret (^) at the prompts. If there is a greater quantity delivered than IFCAP lists for the purchase, enter the date received.

PURCHASE ORDER: 111-A00002 STATUS: Ordered and Obligated

M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.:

REQUESTING SERVICE: MEDICINE

VENDOR: IFVENDOR,ONE SHIP TO: Warehouse

1000 S BOULEVARD V.A. Medical Center

SUITE 100 1 Main Street

ROOM 100, POD 12 ANYTOWN, NV 99999

ANYTOWN, GA 11111 DELIVERY HOURS:

8003338838 8 am - 4 pm

ACCT \# 883198

DELIVERY LOCATION: BDL3

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: DESTINATION \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 828100 \| \| FAR 13

TYPE: \*DELIVERY & PURCHASE ORDER\| \|AGENT:

DELIVER ON/BEFORE 2/7/2000 \|CONTRACT: \| IFBUYER,ONE

DISCOUNT TERM: NET30 \| \*VANAC90N3198010 \|DATE: 1/28/2000

APP: 3640160-081 \| \|

\| \|TOTAL: 206.20

--------------------------------------------------------------------------------

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------

1 POST-IT-NOTES 3X3, YELLOW. 220 UN 0.25 55.00

UNRULED. 100 SHEETS TO PAD.

ADHESIVE ON BACK

NSN: 7530-01-116-7867

QTY PREV RCVD: 0

Items per UN: 12

BOC: 2660 FMS LINE: 001

2 44 BX 1.05 151.20

NSN: 7510-01-432-4323

Items per BX: 144

BOC: 2660 FMS LINE: 001 CONTRACT: VANAC90N3198010

V.A. TRANSACTION NUMBERS:

111-00-2-081-0002

END OF DISPLAY--PRESS RETURN OR ENTER '^' TO HALT:

DATE RECEIVED: TODAY// (FEB 11, 2000)

LINE ITEM: 1

Item: 1 1 POST-IT-NOTES 3X3, YELLOW. UNRULED. 100 SHEETS TO PAD. ADHE

STK#: NSN: 7530-01-116-7867

POST-IT-NOTES 3X3, YELLOW. UNRULED. 100 SHEETS TO PAD. ADHESIVE

ON BACK

UNIT OF PRCH: UN QTY ORDERED: 220 PREVIOUSLY RECEIVED: 0

QTY BEING RECEIVED: 55 AMOUNT: 55

### Receipt of Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are no discrepancies between the shipment and the requisition or purchase order, enter the line item number for the item at the Line Item: prompt. Enter A if the shipment represents all outstanding items on the requisition or purchase order. Enter C for "complete," ONLY if there are no more goods left to receive on the requisition or purchase order. Enter your electronic signature code and print the receiving report. Type Y for yes at the Approve this receiving report and print in Receiving?: prompt. Type Y for yes at the Do you want to also print Receiving Report in FISCAL?: prompt. If you want to enter another received purchase order, enter another requisition or purchase order number at the Purchase Order: prompt. Otherwise, press the Enter key to return to the Warehouse menu.

> **NOTE:** If you make a mistake during the Receipt of Purchase Order option, enter N at the DO YOU WANT TO ALSO PRINT THE REPORT IN FISCAL? prompt.

LINE ITEM: C

Complete P.O. as is? YES// Y (YES)

PURCHASE ORDER: 111-A00002 STATUS: Ordered and Obligated

PROCESSING: INVOICE/RECEIVING REPORT PARTIAL: 1 2/11/2000

--------------------------------------------------------------------------------

UNIT QTY TOTAL

ITEM DESCRIPTION QTY UNIT COST REC COST

--------------------------------------------------------------------------------

1 POST-IT-NOTES 3X3, YELLOW. 220 UN 0.25 220 55.00

UNRULED. 100 SHEETS TO PAD.

ADHESIVE ON BACK

IMF \#: 30

2 ERASERS 144 BX 1.05 144 151.20

IMF \#: 170 CONTRACT: VANAC90N3198010

Total Amount: 206.20

Approve this receiving report and print in Receiving ? YES// Y (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

Do you want to also print Receiving Report in FISCAL ? YES// Y (YES)

PURCHASE ORDER:

## What if the Requisition or Purchase Order Number Is Not on the Invoice?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the vendor name at the Purchase Order: prompt. Scroll through the requisitions or purchase orders in the system for that vendor. Record the requisition or purchase order numbers for any order that may be possible matches.

Select Warehouse Option: RECeipt of Purchase Order

Select STATION NUMBER ('^' TO EXIT): 111// ANYTOWN, NV

PURCHASE ORDER: IFVENDOR,TWO

1 IFVENDOR,TWO IFVENDOR,TWO PH:555 222-2625 NO: 41369

ORD ADD:777 HIGH RD FMS:

ANYTOWN, MA 11111 CODE:98722987301 FAX:301 427-3711

2 IFVENDOR,TWO IFVENDOR,TWO EDI PH:555 777-9191 NO: 41380

ORD ADD:777 HIGH RD FMS:

ANYTOWN, MA 11111 CODE: FAX:

CODE: FAX:

Business Type Undefined

CHOOSE 1-2: 1 IFVENDOR,TWO PH:555 222-2625 NO: 41369

ORD ADD:777 HIGH RD FMS:

ANYTOWN, MA 11111 CODE:98722987301 FAX:333 444-3711

1 IFVENDOR,TWO 111-A05100 02-22-00 PC Order Not Completely Prepared

FCP: 911 \$ 38.40

2 IFVENDOR,TWO 111-A05099 02-22-00 PC Partial Order Received

FCP: 911 \$ 38.40

3 IFVENDOR,TWO 111-A05098 02-22-00 PC Ordered (No Fiscal Action Required

FCP: 911 \$ 38.40

4 IFVENDOR,TWO 111-P05087 02-10-00 PC Ordered (No Fiscal Action Required

FCP: 110 \$ 10.90

5 IFVENDOR,TWO 111-P05086 02-10-00 PC Order Not Completely Prepared

FCP: 911 \$ 0.00

## What if the Requisition or Purchase Order Number Is Not in IFCAP?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sometimes, you will not be able to find the record of an item you receive. If this happens, call the Purchasing Agent in the Purchasing and Contracting Section, describe or show them the invoice, and ask them to locate the requisition or purchase order number.

# SUPPLEMENTARY MENU OPTIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter explains how to use the following menu options:

- Print Receiving Report
- Purchase Order Display
- Delete a Receiving Report
- Warehouse Receiving Statistics
- Imprest Funds Purchase Orders Receiving

## Print Receiving Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Receipt of Purchase Order

Print Receiving Report

Purchase Order Display

Delete a Receiving Report

Warehouse Receiving Statistics

Imprest Funds Purchase Orders Receiving

Select Warehouse Option: Print Receiving Report

Select STATION NUMBER ('^' TO EXIT): 111// ANYTOWN,NV

### Select Order Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a purchase order or requisition number at the P.O./Req. No.: prompt. If you do not know the purchase order or requisition number, enter the first few characters of the number. If you do not know the first few characters of the number, enter three question marks at the prompt and IFCAP will list all the available purchase orders and requisitions.

P.O./REQ.NO.: G90003 111-G90003 07-20-99 ST Transaction Complete

FCP: 4537 \$ 172.50

RECEIVING REPORT DATE:

P.O./REQ.NO.: G90003 111-G90003 07-20-99 ST Transaction Complete

FCP: 4537 \$ 172.50

### Enter Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date of the receiving report that you want to print. If you do not know the date of the receiving report, enter three question marks and IFCAP will list the available receiving reports by date. IFCAP will send the receiving report to the printer designated as the Receiving (Supply) printer. If no printer has been designated you will receive a DEVICE: prompt. Enter the name of the printer where you would like the receiving report to print. Enter another purchase order or requisition number at the P.O./Req. No.: prompt or press the Enter key to return to the Warehouse Menu.

Select Warehouse Option:

RECEIVING REPORT DATE: ??

Choose from:

1 JAN 22, 1999

2 JAN 22, 1999

3 JAN 22, 1999@12:00

## Purchase Order Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Receipt of Purchase Order

Print Receiving Report

Purchase Order Display

Warehouse Receiving Statistics

Imprest Funds Purchase Orders Receiving

Select Warehouse Option: Purchase Order Display

Select STATION NUMBER ('^' TO EXIT): 111// ANYTOWN,NV

### Enter Order Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a purchase order or requisition number at the P.O./Req. No.: prompt. If you do not know the purchase order or requisition number, enter the first few characters of the number. If you do not know the first few characters of the number, enter three question marks at the prompt and IFCAP will list all the available purchase orders and requisitions.

P.O./REQ.NO.: A41218 111-A41218 10-06-94 ST Partial Order Received (Amended)

FCP: 101 \$ 504.00

RECEIVING REPORT DATE:

### Display Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the purchase order you selected, the status, the last receiving report (Last Partial Received), a description of each item on the order and any amendments processed against the order. The user may also display receiving reports.

P.O./REQ.NO.: a00011 111-A00011 10-25-99 ST Complete Order Received

FCP: 110 \$ 18.60

PURCHASE ORDER: 111-A00011 STATUS: Complete Order Received

M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.: 2 02/02/00

REQUESTING SERVICE: FISCAL

PURCHASE ORDER: 111-A90013 STATUS: Complete Order Received (Amended)

M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.: 3 01/14/99

REQUESTING SERVICE: FISCAL

VENDOR: IFVENDOR,ONE SHIP TO: ANYTOWN VAMC

555 STREET CT V.A. Medical Center

SUITE 555 50 STREET WAY, NW

MYTOWN, GA 99999 ANYTOWN, NV 99999

555 333 8888

ACCT \# 883198

FMS Vendor Code: 93086713304

\*EDI ORDER\* DO NOT MAIL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: DESTINATION \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 882100 \| \| FAR 13

TYPE: PURCHASE ORDER \| \|AGENT:

DELIVER ON/BEFORE 1/24/1999 \|CONTRACT: \| IFBUYER,TWO

DISCOUNT TERM: NET30 \| \|DATE: 1/14/1999

APP: 36X8180-5500 \| \|

\| \|TOTAL: 320.00

--------------------------------------------------------------------------------

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------

1 Test MEM-0897-70466 2 EA 100.00 200.00

QTY PREV RCVD: 2

PARTIAL NO.: 1,2,3

Items per EA: 1

BOC: 2660 FMS LINE: 001

2 EST. SHIPPING AND/OR HANDLING 120.00

AMENDMENT NUMBER: 1 EFFECTIVE DATE: 1/14/1999

Adjustment Voucher for Purchase Order 111-A90013

Item No. 1 Test MEM-0897-70466

Items per EA: 1

2 EA at \$ 100.00 = \$ 200.00

ORIGINALLY QTY RECEIVED = 2 ,COST = \$ 200

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------

will now read: QTY RECEIVED=0, COST=\$0

Vendor: IFVENDOR,ONE

APPROPRIATION: 36X8180

This Receiving Report will now read:

Total Amount: 0

AMENDMENT NUMBER: 2 EFFECTIVE DATE: 1/14/1999

\*\*ADDED THROUGH AMENDMENT\*\*

Estimated Shipping and/or Handling of \$120.00 has been added

BOC: 2660

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

--------------------------------------------------------------------------------

\*ADDED THROUGH AMENDMENT\*

Authority Edit is OTHER (specify type of modification and authority)

Review a Receiving Report ? NO// Y (YES)

Select PARTIAL DATE: 1 1-14-1999

PURCHASE ORDER: 111-A90013 STATUS: Complete Order Received (Amended)

PROCESSING: INVOICE/RECEIVING REPORT PARTIAL: 1 1/14/1999

--------------------------------------------------------------------------------

UNIT QTY TOTAL

ITEM DESCRIPTION QTY UNIT COST REC COST

--------------------------------------------------------------------------------

1 Test MEM-0897-70466 2 EA 100.00 2 200.00

Estimated Shipping and/or Handling 120.00

Total Amount: 320.00

Term Discount Amount: 120.00

Net Amount: 200.00

Processed By: /ES/ IFBUYER,TWO

### Review Receiving Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may also review a receiving report by entering a Y for (YES) at the prompt: Review a Receiving Report. Enter the date of the receiving report at the Select Partial Date: prompt. The receiving report will list the item number, the item description, the quantity ordered, the unit of issue, the unit cost, the quantity received, and the total cost of the quantity received. Enter another partial date at the prompt or press the Enter key if you do not want to view any more receiving reports for this requisition or purchase order. Enter another requisition or purchase order at the P.O./Req. No: prompt or press the Enter key to return to the Warehouse Menu.

Review a Receiving Report ? NO// Y (YES)

Select PARTIAL DATE: ???

1 JUL 20, 1999

Select PARTIAL DATE: 1

PURCHASE ORDER: 111-G90003 STATUS: Transaction Complete

PROCESSING: INVOICE/RECEIVING REPORT PARTIAL: 1 7/20/1999

--------------------------------------------------------------------------------

UNIT QTY TOTAL

ITEM DESCRIPTION QTY UNIT COST REC COST

--------------------------------------------------------------------------------

1 DOLLS-RAGGEDY ANN-STUFFED 15 EA 11.50 15 172.50

IMF \#: 12003 CONTRACT: V797P6582A

Total Amount: 172.50

Processed By: /ES/ IFBUYER,THREE

ENTER \<CR\> TO CONTINUE

Select PARTIAL DATE:

P.O./REQ.NO.:

Receipt of Purchase Order

## Delete a Receiving Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is usually reserved for warehouse managers and supervisors. It is locked with the Security Key *PRCHRECDEL*.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Receipt of Purchase Order

Print Receiving Report

Purchase Order Display

Delete a Receiving Report

Warehouse Receiving Statistics

Imprest Funds Purchase Orders Receiving

Select Warehouse Option: Delete a Receiving Report

Select STATION NUMBER ('^' TO EXIT): 111// ANYTOWN,NV

### Enter Order Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a purchase order or requisition number at the P.O./Req. No.: prompt. If you do not know the purchase order or requisition number, enter the first few characters of the number. If you do not know the first few characters of the number, enter three question marks at the prompt and IFCAP will list all the available purchase orders and requisitions. Enter the date of the receiving report you wish to delete at the Select Partial Date: prompt. If you do not know the date of the receiving report, enter three question marks at the prompt and IFCAP will list the available receiving reports.

P.O./REQ.NO.: A40005 111-A40005 11-24-93 ST Partial Order Received (Amended)

FCP: 101 \$ 33.00

Select PARTIAL DATE: ???

CHOOSE FROM:

1 06-30-1994

2 02-18-1999

3 02-22-1999

4 05-16-1999

5 05-26-1999

6 02-26-2000

Select PARTIAL DATE: 12 6-30-1994

### Display Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will display the purchase order number, the status of the purchase order, and the receiving record of each item. IFCAP will ask you to confirm that you want to delete the receiving report. IFCAP will display the current status of the order. Enter the new status you want to assign to the order at the Update Supply Status: prompt. Enter another purchase order or requisition number at the P.O./Req. No.: prompt or press the Enter key to return to the Warehouse Menu.

PURCHASE ORDER: 111-A40005 STATUS: Partial Order Received (Amended)

PROCESSING: INVOICE/RECEIVING REPORT PARTIAL: 12 6/30/94

--------------------------------------------------------------------------------

UNIT QTY TOTAL

ITEM DESCRIPTION QTY UNIT COST REC COST

--------------------------------------------------------------------------------

2 TEST ITEM \#3 30 BX 0.69 -1 -0.69

Total Amount: -0.69

Processed By: IFVENDOR,THREE

Are you sure you want to delete this Receiving Report ? NO// Y (YES)

SORRY, I'M WORKING AS FAST AS I CAN...

Receiving Report Deleted

Update SUPPLY STATUS: Partial Order Received (Amended)//

P.O./REQ.NO.:

Receipt of Purchase Order

Print Receiving Report

Purchase Order Display

Delete a Receiving Report

Warehouse Receiving Statistics

Imprest Funds Purchase Orders Receiving

Select Warehouse Option:

## Warehouse Receiving Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints the number of purchase orders and line items processed by each warehouse clerk for the time range that you define.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Receipt of Purchase Order

Print Receiving Report

Purchase Order Display

Delete a Receiving Report

Warehouse Receiving Statistics

Imprest Funds Purchase Orders Receiving

Select Warehouse Option: Warehouse Receiving Statistics

### List Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will list statistics for each Warehouse Clerk in alphabetical order. However, you can start the report with a specific name. You can also specify the earliest date that you want IFCAP to use to compile statistics.

START WITH WAREHOUSE APPROVED BY: IFBUYER,FOUR //

\* Previous selection: DATE not null

START WITH DATE: FIRST//

DEVICE: UCX/TELNET RIGHT MARGIN: 80//

### Print Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will print the 'Warehouse Receiving Report Statistics' report, which lists the total amount of line items processed on receiving reports by a warehouse clerk (Subtotal), the number of receiving reports processed by the warehouse clerk (Sub count), and the average amount of line items per receiving report, rounded to the nearest whole number (Sub mean). At the end of the report, IFCAP will list the total number of line items processed by the warehouse for the time period (Total), the total number of receiving reports processed by the warehouse for the time period (Count), and the average amount of line items per receiving report, rounded to the nearest whole number (Mean). After printing the report, IFCAP will return to the Warehouse menu.

Select Warehouse Option: Warehouse Receiving Statistics

START WITH WAREHOUSE APPROVED BY: IFBUYER,FOUR //

START WITH DATE: IFBUYER,FOUR//

DEVICE: UCX/TELNET Right Margin: 80//

WAREHOUSE RECEIVING REPORT STATISTICS FEB 24,2000 17:46 PAGE 1

LINECOUNT

--------------------------------------------------------------------------------

WAREHOUSE APPROVED BY: IFBUYER,FIVE

SUBTOTAL 1

SUBCOUNT 1

SUBMEAN 1

WAREHOUSE APPROVED BY: IFBUYER,SIX

SUBTOTAL 183

SUBCOUNT 108

SUBMEAN 2

WAREHOUSE APPROVED BY: IFBUYER,SEVEN

SUBTOTAL 7

SUBCOUNT 6

SUBMEAN 1

WAREHOUSE APPROVED BY: IFBUYER, EIGHT

SUBTOTAL 1

SUBCOUNT 1

SUBMEAN 1

WAREHOUSE APPROVED BY: IFBUYER, NINE

SUBTOTAL 3

SUBCOUNT 2

SUBMEAN 2

WAREHOUSE APPROVED BY: IFBUYER,TEN

SUBTOTAL 16

SUBCOUNT 16

SUBMEAN 1

WAREHOUSE APPROVED BY: IFBUYER1ONE

SUBTOTAL 5

SUBCOUNT 5

SUBMEAN 1

WAREHOUSE APPROVED BY: IFBUYER,ONE

SUBTOTAL 6

SUBCOUNT 6

SUBMEAN 1

WAREHOUSE APPROVED BY: IFBUYER1,TWO

SUBTOTAL 2

SUBCOUNT 2

SUBMEAN 1

WAREHOUSE APPROVED BY: IFBUYER1,THREE

SUBTOTAL 3

SUBCOUNT 1

SUBMEAN 3

WAREHOUSE APPROVED BY: IFBUYER1,FOUR

SUBTOTAL 4

SUBCOUNT 3

SUBMEAN 1

WAREHOUSE APPROVED BY: IFBUYER1,FIVE

SUBTOTAL 8

SUBCOUNT 7

SUBMEAN 1

WAREHOUSE APPROVED BY: IFBUYER1,SIX

SUBTOTAL 1

SUBCOUNT 1

SUBMEAN 1

TOTAL 240

COUNT 159

MEAN 2

## Imprest Funds Purchase Orders Receiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the Warehouse Clerk to enter receiving information for an Imprest funds purchase order, which will complete the purchase order.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Receipt of Purchase Order

Print Receiving Report

Purchase Order Display

Delete a Receiving Report

Warehouse Receiving Statistics

Imprest Funds Purchase Orders Receiving

Select Warehouse Option: Imprest Funds Purchase Orders Receiving

Select STATION NUMBER ('^' TO EXIT): 111// ANYTOWN,NV

### Enter Order Number 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a purchase order or requisition number at the P.O./Req. No.: prompt. If you do not know the purchase order or requisition number, enter the first few characters of the number. If you do not know the first few characters of the number, enter three question marks at the prompt and IFCAP will list all the available purchase orders and requisitions. After you select a purchase order, IFCAP will display the status of the purchase order, the Fund Control Point that is funding the purchase, and the obligated amount of the purchase. You may also review the purchase order.

PURCHASE ORDER: if8011 111-IF8011 02-18-98 IF Pending Fiscal Action

FCP: 126 \$ 15.00

PA/PPM/AUTHORIZED BUYER: IFBUYER1,TWO

### Enter Delivery Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date that you received the delivery at the Date Received: prompt or press the Enter key to accept the default of today's date. At the Complete P.O. As Is?: prompt, press the Enter key to continue processing the receiving report. Press the Enter key at the Approve This Receiving Report And Complete The P.O.?: prompt. Enter your electronic signature code. You may also print the receiving report in Fiscal Service. Enter another purchase order or requisition number at the Purchase Order: prompt or press the Enter key to return to the Warehouse Menu.

REVIEW PURCHASE ORDER? NO// (NO)

DATE RECEIVED: TODAY// (FEB 24, 2000)

Complete P.O. as is? YES// (YES)

PURCHASE ORDER: 111-IF8011 STATUS: Pending Fiscal Action

PROCESSING: IMPREST FUNDS/CASHIER PARTIAL: 1 2/24/2000

--------------------------------------------------------------------------------

UNIT QTY TOTAL

ITEM DESCRIPTION QTY UNIT COST REC COST

--------------------------------------------------------------------------------

1 BATTERY, NONRECHARGEABLE. 1.5 12 EA 1.25 12 15.00

VOLTS, CYLINDRICAL SHAPE, 1

TERMINAL. FLAT SURFACE TYPE,

1.344 INCHES NOMINAL, 2.406

INCHES LONG, SIZE D FOR

INDUSTRIAL FLASHLIGHT USE. 24S

IMF \#: 105

Total Amount: 15.00

Approve this receiving report and complete the P.O.? YES// (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

Do you want to also print Receiving Report in FISCAL ? Yes// (Yes)

# ERROR MESSAGES AND THEIR RESOLUTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you use IFCAP to request goods and services, you may encounter errors or warning messages. Some errors may require assistance from your IRM section. User errors mean that the information you have entered in the system is either incomplete or inconsistent.

Select TRANSACTION: 10195

Incorrect format - please re-enter number

Select TRANSACTION:

<span id="PRC_158_A" class="anchor"></span>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1358</td>
<td>VA Form 1358, Estimated Obligation or Change in Obligation.</td>
</tr>
<tr class="even">
<td>2138</td>
<td>VA Form 90-2138, Order for Supplies or Services. First page of a VA Purchase Order.</td>
</tr>
<tr class="odd">
<td>2139</td>
<td>VA Form 90-2139, Order for Supplies or Services (Continuation). This is a continuation sheet for the 2138 form.</td>
</tr>
<tr class="even">
<td>2237</td>
<td>VA Form 90-2237, Request, Turn-in and Receipt for Property or Services. Used to request goods and services.</td>
</tr>
<tr class="odd">
<td>A&amp;MM</td>
<td>Acquisition and Materiel Management Service.</td>
</tr>
<tr class="even">
<td>AACS</td>
<td>Automated Allotment Control System--Central computer system developed by VHA to disburse funding from VACO to field stations.</td>
</tr>
<tr class="odd">
<td>Accounting Technician</td>
<td>Fiscal employee responsible for obligation and payment of received goods and services.</td>
</tr>
<tr class="even">
<td>Activity Code</td>
<td>The last two digits of the AACS number. It is defined by each station.</td>
</tr>
<tr class="odd">
<td>ADP Security Officer</td>
<td>The individual at your station who is responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing file access.</td>
</tr>
<tr class="even">
<td>Agent Cashier</td>
<td>The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.</td>
</tr>
<tr class="odd">
<td>ALD Code</td>
<td>Appropriation Limitation Department. A set of Fiscal codes that identifies the appropriation used for funding.</td>
</tr>
<tr class="even">
<td>Allowance table</td>
<td>Reference table in FMS that provides financial information at the level immediately above the AACS, or sub-allowance level.</td>
</tr>
<tr class="odd">
<td>Amendment</td>
<td>A document that changes the information contained in a specified Purchase Order. Amendments are processed by the Purchasing &amp; Contracting section of A&amp;MM and obligated by Fiscal Service.</td>
</tr>
<tr class="even">
<td>AMIS</td>
<td>Automated Management Information System.</td>
</tr>
<tr class="odd">
<td>Application Coordinator</td>
<td>The individuals responsible for the implementation, training and trouble-shooting of a software package within a service. IFCAP requires there be an Application Coordinator designated for Fiscal Service, A&amp;MM Service.</td>
</tr>
<tr class="even">
<td>Approve Requests</td>
<td>The use of an electronic signature by a Control Point Official to approve a 2237, 1358 or other request form and transmit said request to A&amp;MM/Fiscal.</td>
</tr>
<tr class="odd">
<td>Approving Official</td>
<td>A user that approves reconciliations to ensure that they are correct and complete.</td>
</tr>
<tr class="even">
<td>Authorization</td>
<td>Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.</td>
</tr>
<tr class="odd">
<td>Authorization Balance</td>
<td>The amount of money remaining that can be authorized against the 1358. The service balance minus total authorizations.</td>
</tr>
<tr class="even">
<td>Batch Number</td>
<td>A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number.</td>
</tr>
<tr class="odd">
<td>Breakout Code</td>
<td>A set of A&amp;MM codes which identifies a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.).</td>
</tr>
<tr class="even">
<td>Budget Analyst</td>
<td>Fiscal employee responsible for distributing and transferring funds.</td>
</tr>
<tr class="odd">
<td>Budget Object Code</td>
<td>Fiscal accounting element that tells what kind of item or service is being procured. Budget object codes replaced sub accounts in IFCAP 5.0. . . Budget object codes are listed in VA Handbook 4671.2</td>
</tr>
<tr class="even">
<td>Budget Sort Category</td>
<td>Used by Fiscal Service to identify the allocation of funds throughout their facility.</td>
</tr>
<tr class="odd">
<td>CCS</td>
<td>The Credit Card System. This is the database in Austin that processes the credit card information from the external Credit Card Vendor system, currently CitiDirect, and then passes information on to FMS and IFCAP.</td>
</tr>
<tr class="even">
<td>CC</td>
<td>Credit Charge entry identifier used by FMS and CCS for charges paid to Vendor thru Credit Card payment process.</td>
</tr>
<tr class="odd">
<td>Ceiling Transactions</td>
<td>Funding distributed from Fiscal Service to IFCAP Control Points for spending. The Budget Analyst initiates these transactions using the Funds Distribution options.</td>
</tr>
<tr class="even">
<td>Classification of Request</td>
<td>An identifier a Control Point can assign to track requests that fall into a category, e.g., Memberships, Replacement Parts, Food Group III.</td>
</tr>
<tr class="odd">
<td>Common Numbering Series</td>
<td>This is a pre-set series of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinators establish the Common Numbering Series used by each facility.</td>
</tr>
<tr class="even">
<td>Control Point</td>
<td>Financial element, existing ONLY in IFCAP, which corresponds to a set of elements in FMS that include the Account Classification Code (ACC) and define the Sub-Allowance on the FMS system. Used to permit the tracking of monies to a specified service, activity or purpose from an Appropriation or Fund.</td>
</tr>
<tr class="odd">
<td>Control Point Clerk</td>
<td>The user within the service who is designated to input requests (2237s) and maintain the Control Point records for a Service.</td>
</tr>
<tr class="even">
<td>Control Point Official</td>
<td>The individual authorized to expend government funds for ordering of supplies and services for their Control Point(s). This person has all of the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.</td>
</tr>
<tr class="odd">
<td>Control Point Official's Balance</td>
<td>A running record of all the transactions generated and approved for a Control Point from within IFCAP and also. Effects changes to the control point that are initiated directly from within the FMS system. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.</td>
</tr>
<tr class="even">
<td>Control Point Requestor</td>
<td>The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. This user can only view or edit their own requests. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&amp;MM.</td>
</tr>
<tr class="odd">
<td>Cost Center</td>
<td>Cost Centers are unique numbers that define a service. One cost center must be attached to every Fund Control Point. This enables costs to be captured by service. Cost centers are listed in VA Handbook 4671.1.</td>
</tr>
<tr class="even">
<td>Date Committed</td>
<td>The date that you want IFCAP to commit funds to the purchase.</td>
</tr>
<tr class="odd">
<td>Default</td>
<td>A suggested response that is provided by the system.</td>
</tr>
<tr class="even">
<td>Deficiency</td>
<td>When a budget has obligated and expended more than it was funded.</td>
</tr>
<tr class="odd">
<td>Delinquent Delivery Listing</td>
<td>A listing of all the Purchase Orders that have not had all the items received by the Warehouse on IFCAP. It is used to contact the vendor for updated delivery information.</td>
</tr>
<tr class="even">
<td>Delivery Order</td>
<td>An order for an item that the VA purchases through an established contract with a vendor who supplies the items.</td>
</tr>
<tr class="odd">
<td>Direct Delivery Patient</td>
<td>A patient who has been designated to have goods delivered directly to him/her from the vendor.</td>
</tr>
<tr class="even">
<td>Discount Item</td>
<td>This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.</td>
</tr>
<tr class="odd">
<td>EDI Vendor</td>
<td>A vendor with whom the VA has negotiated an arrangement to submit, accept and fill orders electronically.</td>
</tr>
<tr class="even">
<td>Electronic Data Interchange (EDI)</td>
<td>Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.</td>
</tr>
<tr class="odd">
<td>Electronic Signature</td>
<td>The electronic signature code replaces the written signature on all IFCAP documents used within your facility. Documents going off-station will require a written signature as well.</td>
</tr>
<tr class="even">
<td>Expenditure Request</td>
<td>A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).</td>
</tr>
<tr class="odd">
<td>FCP</td>
<td>Fund Control Point (see Control Point).</td>
</tr>
<tr class="even">
<td>Federal Tax ID</td>
<td>A unique number that identifies your station to the Internal Revenue Service.</td>
</tr>
<tr class="odd">
<td>Fiscal Balance</td>
<td>The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidation submitted against the obligation.</td>
</tr>
<tr class="even">
<td>Fiscal Quarter</td>
<td>The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.</td>
</tr>
<tr class="odd">
<td>Fiscal Year</td>
<td>Twelve-month period from October 1 to September 30.</td>
</tr>
<tr class="even">
<td>FMS</td>
<td>Financial Management System, the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides for flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.</td>
</tr>
<tr class="odd">
<td>FOB</td>
<td>Freight on Board. An FOB of "Destination" means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of "Origin" means that shipping charges are due to the shipper and must be paid when the shipper arrives at the warehouse with the item.</td>
</tr>
<tr class="even">
<td>FPDS</td>
<td>Federal Procurement Data System.</td>
</tr>
<tr class="odd">
<td>FTEE</td>
<td>Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned an FTEE of 0.5, as would a full-time employee that worked for half of a year.</td>
</tr>
<tr class="even">
<td>Fund Control Point</td>
<td>IFCAP accounting element that is not used by FMS. See also control point.</td>
</tr>
<tr class="odd">
<td>Funds Control</td>
<td>A group of Control Point options that allow the Control Point Clerk and/or Official to maintain and reconcile their funds.</td>
</tr>
<tr class="even">
<td>Funds Distribution</td>
<td>A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.</td>
</tr>
<tr class="odd">
<td>GBL</td>
<td>Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of $250.00.</td>
</tr>
<tr class="even">
<td>GL</td>
<td>General Ledger.</td>
</tr>
<tr class="odd">
<td>Identification Number</td>
<td>A computer-generated number assigned to a code sheet.</td>
</tr>
<tr class="even">
<td>Imprest Funds</td>
<td>Monies used for cash or 3rd party draft purchases at a VA facility.</td>
</tr>
<tr class="odd">
<td>Integrated Supply Management System (ISMS)</td>
<td>ISMS is the system that replaced LOG I for Expendable Inventory.</td>
</tr>
<tr class="even">
<td>ISMS</td>
<td>See Integrated Supply Management System.</td>
</tr>
<tr class="odd">
<td>Item File</td>
<td>A listing of items specified by A&amp;MM service as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history.</td>
</tr>
<tr class="even">
<td>Item History</td>
<td>Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.</td>
</tr>
<tr class="odd">
<td>Item Master Number</td>
<td>A computer generated number used to identify an item in the Item File.</td>
</tr>
<tr class="even">
<td>Justification</td>
<td>A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source.</td>
</tr>
<tr class="odd">
<td>Liquidation</td>
<td>The amount of money posted to the 1358 or Purchase Order as a payment to the vendor. They are processed through payment/invoice tracking.</td>
</tr>
<tr class="even">
<td>LOG I</td>
<td>LOG I is the name of the Logistics A&amp;MM computer located at the Austin Automation Center. This system continues to support the Consolidated Memorandum of Receipt.</td>
</tr>
<tr class="odd">
<td>Mandatory Source</td>
<td>A Federal Agency that sells supplies and services to the VA. VA Supply Depot, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.</td>
</tr>
<tr class="even">
<td>MSC Confirmation Message</td>
<td>A MailMan message generated by the Austin Message Switching Center that assigns an FMS number to an IFCAP transmission of documents.</td>
</tr>
<tr class="odd">
<td>Obligation</td>
<td>The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of an Order.</td>
</tr>
<tr class="even">
<td>Obligation (Actual) Amount</td>
<td>The actual dollar figure obligated by Fiscal Service for a Purchase Order. The Control Point's records are updated with actual cost automatically when Fiscal obligates the document on IFCAP.</td>
</tr>
<tr class="odd">
<td>Obligation Data</td>
<td>A Control Point option that allows the Control Point Clerk and/or Budget Analyst to enter data not recorded by IFCAP.</td>
</tr>
<tr class="even">
<td>Obligation Number</td>
<td>The C prefix number that Fiscal Service assigns to the 1358.</td>
</tr>
<tr class="odd">
<td>Organization Code</td>
<td>Accounting element functionally comparable to Cost Center but used to organize purchases by the budget that funded them, not the purpose for spending the funds.</td>
</tr>
<tr class="even">
<td>Outstanding 2237</td>
<td>A&amp;MM report that lists all the IFCAP generated 2237s pending action in A&amp;MM.</td>
</tr>
<tr class="odd">
<td>PAID</td>
<td>Paid Accounting Integrated Data. The VistA software used by stations to process timecard data to the PAID system in Austin.</td>
</tr>
<tr class="even">
<td>Partial</td>
<td>A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.</td>
</tr>
<tr class="odd">
<td>Partial Date</td>
<td>The date that a warehouse clerk created a receiving report for a shipment.</td>
</tr>
<tr class="even">
<td>PAT Number</td>
<td>Pending Accounting Transaction number - the primary FMS reference number. See also Obligation Number.</td>
</tr>
<tr class="odd">
<td>Personal Property Management</td>
<td>A section of A&amp;MM Service responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process all requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support.</td>
</tr>
<tr class="even">
<td>PPM</td>
<td>Personal Property Management now referred to at most sites as Acquisition and Materiel Management Service.</td>
</tr>
<tr class="odd">
<td>Program Code</td>
<td>Accounting element that identifies the VA initiative or program that the purchase will support.</td>
</tr>
<tr class="even">
<td>Prompt Payment Terms</td>
<td>The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).</td>
</tr>
<tr class="odd">
<td>Purchase Card</td>
<td>A card, similar to a credit card that Purchase Card Users use to make purchases. Purchase Cards are not credit cards but debit cards that spend money out of a deposited balance of VA funds.</td>
</tr>
<tr class="even">
<td>Purchase Card Coordinator</td>
<td>A person authorized by a VA station to monitor and resolve delinquent purchase card orders, help VA services record, edit and approve purchase card orders in a timely manner, assign purchase cards to IFCAP users, and monitor the purchase card expenses of VAMC services.</td>
</tr>
<tr class="odd">
<td>Purchase Card Orders</td>
<td>Orders funded by a purchase card.</td>
</tr>
<tr class="even">
<td>Purchase Card User</td>
<td>A person who uses a purchase card. Purchase Card Users are responsible for recording their purchase card orders in IFCAP.</td>
</tr>
<tr class="odd">
<td>Purchase History Add (PHA)</td>
<td>Information about purchase orders which is automatically sent to Austin for archiving. This same transaction is also used to send a PO for EDI processing.</td>
</tr>
<tr class="even">
<td>Purchase History Modify (PHM)</td>
<td>Information about amendments that is automatically sent to Austin for archiving.</td>
</tr>
<tr class="odd">
<td>Purchase Order</td>
<td>A government document authorizing the purchase of the goods or services at the terms indicated.</td>
</tr>
<tr class="even">
<td>Purchase Order Acknowledgment</td>
<td>Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).</td>
</tr>
<tr class="odd">
<td>Purchase Order Status</td>
<td>The status of completion of a purchase order (e.g., Pending Contracting Officer's Signature, Pending Fiscal Action, Partial Order Received, etc.).</td>
</tr>
<tr class="even">
<td>Purchasing Agents</td>
<td>A&amp;MM employees legally empowered to create purchase orders to obtain goods and services from commercial vendors.</td>
</tr>
<tr class="odd">
<td>Quarterly Report</td>
<td>A Control Point listing of all transactions (Ceilings, Obligations, Adjustments) made against a Control Point's Funds.</td>
</tr>
<tr class="even">
<td>Quotation for Bid</td>
<td>Standard Form 18. Used by Purchasing Agents to obtain written bids from vendors. May be created automatically and transmitted electronically within the Purchasing Agent's module.</td>
</tr>
<tr class="odd">
<td>Receiving Report</td>
<td>Report that Warehouse Clerk creates to record that the warehouse has received an item.</td>
</tr>
<tr class="even">
<td>Receiving Report</td>
<td>The VA document used to indicate the quantity and dollar value of the goods being received.</td>
</tr>
<tr class="odd">
<td>Reconciliation</td>
<td>Comparing of two records to validate IFCAP Purchase Card orders. Purchase Card Users compare IFCAP generated purchase card order data with the CC transaction sent from the CCS system in Austin.</td>
</tr>
<tr class="even">
<td>Reference Number</td>
<td>Also known as the Transaction Number. The computer generated number that identifies a request. It is comprised of the: Station Number-Fiscal Year-Quarter - Control Point – 4-digit Sequence Number.</td>
</tr>
<tr class="odd">
<td>Repetitive (PR Card) Number</td>
<td>See Item Master Number.</td>
</tr>
<tr class="even">
<td><p>Repetitive Item List</p>
<p>(RIL)</p></td>
<td>A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate 2237 requests from the list. A RIL can be created by using the Auto-Generate feature within the Inventory portion of the package.</td>
</tr>
<tr class="odd">
<td>Requestor</td>
<td>See “Control Point Requestor.”</td>
</tr>
<tr class="even">
<td>Requisition</td>
<td>An order from a Government vendor.</td>
</tr>
<tr class="odd">
<td>Running Balance</td>
<td>A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.</td>
</tr>
<tr class="even">
<td>Section Request</td>
<td>A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.</td>
</tr>
<tr class="odd">
<td>Service Balance</td>
<td>The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorizations created by the service.</td>
</tr>
<tr class="even">
<td>SF-18</td>
<td>Request for Quotation.</td>
</tr>
<tr class="odd">
<td>SF-30</td>
<td>Amendment of Solicitation/Modification of Contract.</td>
</tr>
<tr class="even">
<td>Short Description</td>
<td>A phrase that describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).</td>
</tr>
<tr class="odd">
<td>Site Parameters</td>
<td>Information (such as Station Number, Cashier's address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter file.</td>
</tr>
<tr class="even">
<td>Sort Group</td>
<td>An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.</td>
</tr>
<tr class="odd">
<td>Sort Order</td>
<td>The order in which the budget categories will appear on the budget distribution reports.</td>
</tr>
<tr class="even">
<td>Special Remarks</td>
<td>A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.</td>
</tr>
<tr class="odd">
<td>Stacked Documents</td>
<td>The POs, RRs &amp; 1358s that are sent electronically to Fiscal and stored in a file for printing at a later time rather than being printed immediately.</td>
</tr>
<tr class="even">
<td>Status of Funds</td>
<td>Fiscal's on-line status report of the monies available to a Control Point. FMS updates this information automatically.</td>
</tr>
<tr class="odd">
<td>Sub-control Point</td>
<td>A user defined assignment of all or part of a ceiling transaction to a specific category (sub-control point) within a Control Point. Transactions can then be posted against this sub-control point and a report can be generated to track use of specified funding within the overall control point..</td>
</tr>
<tr class="even">
<td>Sub-cost Center</td>
<td>A subcategory of Cost Center. IFCAP will not utilize a 'sub-cost center' field but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field.</td>
</tr>
<tr class="odd">
<td>Tasked Job</td>
<td>A job, usually a printout that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.</td>
</tr>
<tr class="even">
<td>TDA</td>
<td>See "Transfer of Disbursing Authority."</td>
</tr>
<tr class="odd">
<td>Total Authorizations</td>
<td>The total amount of the authorizations created for the 1358 obligation.</td>
</tr>
<tr class="even">
<td>Total Liquidations</td>
<td>The total amount of the liquidations against the 1358 obligation.</td>
</tr>
<tr class="odd">
<td>Transaction Number</td>
<td>The number of the transaction that funded a Control Point (See Budget Analyst User's Guide). It consists of the Station Number - Fiscal Year - Quarter - Control Point - Sequence Number.</td>
</tr>
<tr class="even">
<td>Transfer of Disbursing Authority</td>
<td>The method used to allocate funds to a VA facility.</td>
</tr>
<tr class="odd">
<td>Transmission Number</td>
<td>A sequential number given to a data string when it is transmitted to the Austin DPC; used for tracking message traffic.</td>
</tr>
<tr class="even">
<td>Type Code</td>
<td>A set of A&amp;MM codes that provides information concerning the vendor size and type of competition sought on a purchase order.</td>
</tr>
<tr class="odd">
<td>Vendor file</td>
<td>An IFCAP file of vendor information solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. The debtor's address may be drawn from this file but is maintained separately. If the desired vendor is not in the file, contact A&amp;MM Service to have it added.</td>
</tr>
<tr class="even">
<td>Vendor ID Number</td>
<td>The ID number assigned to a vendor by the FMS Vendor unit.</td>
</tr>
<tr class="odd">
<td>VRQ</td>
<td>FMS Vendor Request document. When a new vendor is added to IFCAP a VRQ message is sent electronically to the Austin FMS Vendor unit to determine if the vendor exists in the central vendor system. If the vendor is not in the system, Austin will confirm information and establish the vendor in the central file. If vendor exists in central file already, Austin will verify the data. See also VUP.</td>
</tr>
<tr class="even">
<td>VUP</td>
<td>Vendor Update Message. This message is sent electronically from the FMS system to ALL IFCAP sites to ensure that the local vendor file contains the same data as the central vendor file in Austin. This message will contain the FMS Vendor ID for the vendor and also the Alternate Address Indicator if applicable. See also VRQ.</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Imprest Funds, 9
Imprest Funds Purchase Orders Receiving, 23
Print Receiving Report, 10
Purchase Order, 3, 4, 7, 8, 9, 11, 23
Purchase Order Display, 11
Receipt of Purchase Order, 3, 4, 7
Warehouse Receiving Statistics, 19
