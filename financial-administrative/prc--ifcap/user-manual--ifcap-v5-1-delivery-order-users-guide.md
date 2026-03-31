---
title: IFCAP Version 5.1 Delivery Order User's Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Delivery Order User's Guide
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
description: 
audience: 
keywords: 
  - order
  - delivery
  - table
  - contents
  - number
  - edit
  - purchase
  - prompt
  - span
  - orders
page_count: 0
word_count: 10495
section_count: 23
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1delivery_orders.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/ifcp5_1delivery_orders.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP)Version 5.1Delivery OrderUser's Guide

![](ifcap-version-5-1-delivery-order-user-s-guide/001.png)

March 2026Department of Veterans AffairsOffice of Information and Technology (OI&T)Management, Enrollment, and Financial Systems

Revision History

Initiated 12/29/04

<table>
<caption><p><span id="_Toc222741870" class="anchor"></span>Table 1: Delivery Order Menu Options</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 46%" />
<col style="width: 22%" />
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
<td>6.0</td>
<td><p>Updates based on patch PRC*5.1*252.</p>
<p>This manual has been updated to comply with the VA OIT-mandated user guide template.</p></td>
<td><p>Technical Writer</p>
<p>HDSO Sustainment</p></td>
</tr>
<tr class="odd">
<td>May 2025</td>
<td>5.0</td>
<td>Patch PRC*5.1*238: FPDS Questions Removal</td>
<td><p>Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>October 2011</td>
<td>4.0</td>
<td>Patch PRC*5.1*158 Modification of title for IFCAP VA Form 1358.</td>
<td><p>Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>02/09/06</td>
<td>3.0</td>
<td>Updated to include new functionality introduced with patch PRC*5.1*79 (FPDS ICAR for VistA)</td>
<td><p>Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="even">
<td>12/29/04</td>
<td>2.0</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td><p>Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
<tr class="odd">
<td>12/29/04</td>
<td>1.0</td>
<td>PDF file checked for accessibility to readers with disabilities.</td>
<td><p>Technical Writer</p>
<p>Department of Veterans Affairs</p></td>
</tr>
</tbody>
</table>

<span id="_Toc222741870" class="anchor"></span>Table 1: Delivery Order Menu Options

Preface

This manual is designed to provide you with the information necessary to use the Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) system to report, record, and amend delivery orders. The IFCAP package has automated certain functions in Acquisition and Material Management Services (A&MM), Fiscal Service, and all of the services that request supplies and services. IFCAP automates the creation, approval, forwarding, monitoring, and payment of VA Forms 90-2237. IFCAP also functions as a database of procurement information.

Table of Contents

Tables:

[Table 1: Delivery Order Menu Options [3](#_Toc222741870)](#_Toc222741870)

Figures:

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Delivery Orders](#delivery-orders)
  - [How to Use This Manual](#how-to-use-this-manual)
  - [Reference Numbering System](#reference-numbering-system)
  - [Package Management, Legal Requirements and Security Measures](#package-management-legal-requirements-and-security-measures)
  - [Package Operation](#package-operation)
  - [Site Parameters and User Parameters](#site-parameters-and-user-parameters)
    - [Introduction](#introduction-1)
    - [EDI Release Switch](#edi-release-switch)
    - [Delivery Order Release Switch](#delivery-order-release-switch)
- [Delivery Orders](#delivery-orders-1)
  - [Introduction](#introduction-2)
  - [Enter Delivery Order](#enter-delivery-order)
    - [Introduction](#introduction-3)
    - [Menu Path](#menu-path)
    - [Setup Parameters](#setup-parameters)
    - [Delivery Date](#delivery-date)
    - [Review Delivery Order](#review-delivery-order)
  - [Edit Delivery Order](#edit-delivery-order)
    - [Introduction](#introduction-4)
    - [Menu Path](#menu-path-1)
    - [Edit Option Prompts](#edit-option-prompts)
  - [Enter Pharmaceutical PV Order](#enter-pharmaceutical-pv-order)
    - [Introduction](#introduction-5)
    - [Menu Path](#menu-path-2)
    - [Setup Parameters](#setup-parameters-1)
    - [Order Information](#order-information)
    - [Review Delivery Order](#review-delivery-order-1)
  - [Edit Pharmaceutical PV Order](#edit-pharmaceutical-pv-order)
  - [Introduction](#introduction-6)
  - [Menu Path](#menu-path-3)
  - [Edit option prompts](#edit-option-prompts-1)
  - [Delivery Order from Repetitive Item List](#delivery-order-from-repetitive-item-list)
    - [Introduction](#introduction-7)
    - [Menu Path](#menu-path-4)
    - [Select Repetitive Item List](#select-repetitive-item-list)
    - [Listing](#listing)
  - [Receive Delivery Order](#receive-delivery-order)
    - [Introduction](#introduction-8)
    - [Menu Path](#menu-path-5)
    - [Data Display](#data-display)
    - [Check for Shipping Discrepancy](#check-for-shipping-discrepancy)
    - [Receipt of Item](#receipt-of-item)
  - [Amendment to Delivery Order](#amendment-to-delivery-order)
    - [Introduction](#introduction-9)
    - [Menu Path](#menu-path-6)
    - [Order Information](#order-information-1)
    - [Item Information](#item-information)
    - [Delivery Schedules](#delivery-schedules)
  - [Adjustment Voucher to Delivery Order](#adjustment-voucher-to-delivery-order)
    - [Introduction](#introduction-10)
    - [Menu Path](#menu-path-7)
    - [Listing](#listing-1)
    - [Item Selection](#item-selection)
  - [Convert a Delivery Order to a 2237 Request](#convert-a-delivery-order-to-a-2237-request)
    - [Introduction](#introduction-11)
    - [Menu Path](#menu-path-8)
    - [Select Delivery Order](#select-delivery-order)
  - [Convert Delivery Order to a Purchase Card Order](#convert-delivery-order-to-a-purchase-card-order)
    - [Introduction](#introduction-12)
    - [Menu Path](#menu-path-9)
    - [Select Order Number](#select-order-number)
  - [Cancel an Incomplete Delivery Order](#cancel-an-incomplete-delivery-order)
    - [Introduction](#introduction-13)
    - [Menu Path](#menu-path-10)
    - [Cancel the Order](#cancel-the-order)
  - [Display Delivery Order](#display-delivery-order)
    - [Introduction](#introduction-14)
    - [Menu Path](#menu-path-11)
    - [Display Order](#display-order)
- [# Glossary](#glossary)
- [# Index](#index)

## Delivery Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Delivery Orders are orders for items that the VA purchases through an established contract with a vendor who supplies the items. This manual will teach you how to use IFCAP (Integrated Funds Distribution, Control Point Activity, Accounting and Procurement) to create and edit delivery orders, report the receipt of delivery orders, and translate delivery orders into 2237 requests and purchase card orders.

## How to Use This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual explains how to perform the tasks that the Delivery Order Menu was designed to help users accomplish. The authors of this manual have listed these tasks in successive order so that each instruction builds on the functionality and information from the previous instructions. This will allow new IFCAP Users to use this manual as a tutorial by following the instructions from beginning to end. Experienced users can use this manual as a reference tool by using the index and table of contents.

## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses a special paragraph numbering system to allow users to understand how the sections of the manual relate to each other. For example, this paragraph is section 1.3. This means that this paragraph is the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections 1.3.1 and 1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third subsection of Chapter 1. All that clear? All this means that users that want to divide their reading into manageable lessons can concentrate on one section and all of its subsections, e.g., section 1.3.5 and all of its subsections would make a coherent lesson.

## Package Management, Legal Requirements and Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the nature of the information being processed by IFCAP, special attention has been paid to limiting usage by Department of Veteran's Affair individuals. Individuals in the system who have authority to approve actions, at whatever level, have an electronic signature code. This code is required before the documents pass on to a new level for processing or review. Like the access and verify codes used when gaining access to the system, the electronic signature code will not be visible on the terminal screen. These codes are also encrypted so that even when viewed in the user file by those with the highest levels of access, they are unreadable. Electronic signature codes are required by IFCAP at every level that currently requires a signature on paper.

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

When you create delivery orders, you affect Control Point balances. Different kinds of IFCAP users have different menus. If the menus in this manual include options that you do not see on your screen, do not panic! If you do not know what to enter at an IFCAP prompt, enter one, two or three question marks and IFCAP will list your available options or explain the prompt. The more question marks you enter at the prompt, the more information IFCAP will provide.

The options you use on IFCAP have been divided into groups based on the type of work that you do. When you select these options, IFCAP will ask you a series of questions. If you do not understand the question or are unsure of how to respond, enter a question mark (?) and the computer will explain the question, or allow you to choose from a list of responses.

These are the options on the Delivery Order Menu.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Menu Option</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enter Delivery Order</td>
<td>Use this option to create a delivery order</td>
</tr>
<tr class="even">
<td>Edit Delivery Order</td>
<td><p>Use this option to edit a delivery order.</p>
<p>You can edit delivery orders until you authorize the order with your electronic signature code. Once the order has been authorized and electronically signed, editing (amending) can only be done in the ‘Amendment to Delivery Order’ option.</p></td>
</tr>
<tr class="odd">
<td>Enter Pharmaceutical PV Order</td>
<td>Use this option to place pharmaceutical delivery orders.</td>
</tr>
<tr class="even">
<td>Edit Pharmaceutical PV Order</td>
<td>Use this option to edit an existing pharmaceutical delivery order.</td>
</tr>
<tr class="odd">
<td>Create Delivery Order from Repetitive Item List</td>
<td>Use this option to create delivery orders from a repetitive item list.</td>
</tr>
<tr class="even">
<td>Receive Delivery Order</td>
<td>Use this option to record the receipt of items on a delivery order</td>
</tr>
<tr class="odd">
<td>Amendment to Delivery Order</td>
<td>Use this option to make changes to a delivery order after the IFCAP user has authorized the order with their electronic signature code.</td>
</tr>
<tr class="even">
<td>Adjustment Voucher to Delivery Order</td>
<td>Use this option to decrease the quantity received on a receiving report for a delivery order.</td>
</tr>
<tr class="odd">
<td>Convert a Delivery Order to a 2237 Request (CD2)</td>
<td>Use this option to convert a delivery order into a VA Form 90-2237 (Request, Turn-in and Receipt for Property or Services.)</td>
</tr>
<tr class="even">
<td>Convert a Delivery Order to a Purchase Card Order (CDP)</td>
<td>Use this option to convert a delivery order into a purchase card order</td>
</tr>
<tr class="odd">
<td>Cancel an Incomplete Delivery Order</td>
<td>Use this option to cancel an incomplete delivery order.</td>
</tr>
<tr class="even">
<td>Display Delivery Order</td>
<td>Use this option to display a delivery order.</td>
</tr>
</tbody>
</table>

## Site Parameters and User Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Site parameter switches have been added to IFCAP which allow Fiscal Service to bypass approvals on delivery orders. These switches can be set for a specific Fund Control Point or for the entire station. There are 3 switches, (1) EDI, (2) Delivery Orders, and (3) All Orders. These switches will be controlled by Fiscal Service.

### EDI Release Switch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the EDI Release Switch is on, EDI orders are sent immediately to vendors without a review from Fiscal Service. If the switch is off, Fiscal’s review is required before EDI orders are sent.

### Delivery Order Release Switch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Delivery orders are processed as "obligated" and sent immediately to vendors without Fiscal review, if the Delivery Order Release switch is on.

In addition, when the switch is on, IFCAP provides a report for Fiscal Service of the Delivery Orders that are obligated automatically (bypassing Fiscal). If the switch is off, Fiscal Service’s review will be required before these orders are sent. 1.6.4 All Orders Release Switch

When the "All Orders" release switch is set to "on", there will be no Fiscal review of any orders; all orders are obligated automatically without fiscal review.

# Delivery Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There will be a separate menu to accommodate delivery orders within IFCAP. A delivery order is an order of purchase, for which the VA has an established contract. The Delivery Order \[PRCH DELIVERY ORDER MENU\] menu is a stand-alone menu. This menu is designed for purchasing contract items and is not to be used to create requisitions. The Delivery Order Menu includes the following options:

- Enter Delivery Order
- Edit Delivery Order
- Enter Pharmaceutical PV Order
- Edit Pharmaceutical PV Order
- Create Delivery Order from Repetitive Item List
- Receive Delivery Order
- Amendment to Delivery Order
- Adjustment Voucher to Delivery Order
- (CD2) Convert Delivery Order to a 2237 Request
- (CDP) Convert Delivery Order to a Purchase Card Order
- Cancel an Incomplete Delivery Order
- Display Delivery Order

## Enter Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter Delivery Order and Edit Delivery Order options will allow users to place delivery orders at the service level. Delivery orders are placed against an existing contract. The Method of Processing (MOP) for Delivery Orders is “Invoice/ Receiving Report". This MOP is assigned as a default value. As with Control Point level purchase card orders (which require a receiving report), the process of creating a delivery order will be an abbreviated combination of the 2237 (file 410) and the purchase order (file 442) entry process.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497129" class="anchor"></span>Figure 1: Delivery Order Menu Path

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Select Delivery Order Menu Option: Enter Delivery Order

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the station number, if prompted. Next, enter the delivery order number followed by the Purchase Order (P.O.) date. IFCAP will then ask you if the order is an estimated order. At the Estimated Order? prompt enter “YES” or “NO”. The default is No. Estimated orders are orders that have an unknown cost or quantity. Orders for services, i.e., equipment repair, are often estimated orders, since the vendor doesn’t determine the actual cost until the vendor completes the repair. Enter the Invoice Address followed by the D.O. Vendor. Enter the name of the vendor, or the first few letters of the vendor's name. You can type three question marks (???) at the prompt to list all of the vendors in the system. If you do not know which vendor has the item you want, follow the instructions in section 3.4 of the Control Point Clerk's Guide, “How to Consult the Item Master File”. Enter the Fund Control Point (FCP) followed by the appropriate Cost Center.

Specify the location for delivery at the Delivery Location: prompt and enter where you want the vendor to deliver the purchase at the “Ship To:” prompt. Next, enter “O” for Origin at the F.O.B. (Freight on Board) Point: prompt, if additional freight charges are due to the carrier at the time of delivery. Otherwise, destination is the default selection and can be accepted by pressing the enter key.

<span id="_Toc222497130" class="anchor"></span>Figure 2: Setup Parameters

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

ENTER A NEW DELIVERY ORDER NUMBER OR A COMMON NUMBERING SERIES

DELIVERY ORDER: P98 999-P98 DO AUTHORIZED BUYER

Are you adding '999-P98082' as a new Purchase Order number ? Y (YES)

P.O. DATE: JUN 28,2005// (JUN 28, 2005)

METHOD OF PROCESSING: INVOICE/RECEIVING REPORT//

ESTIMATED ORDER?: N// NO

INVOICE ADDRESS: FMS//

PCDO VENDOR: 18 IFVNDOR INC PH:111 555-7771 NO: 18

ORD ADD:5301 ANY STREET FMS:IFVENDOR INC

ANYCITY, CA 99999-3196 CODE:P55396097 FAX:

...OK? Yes// (Yes)

FCP: 255 ABC FCP 0160A1 10 0100 989

COST CENTER: 215000 Telecommunications

Enter the word 'PATIENT' in the 'DELIVERY LOCATION' field for a direct delivery

to a patient.

DELIVERY LOCATION:

SHIP TO: ANYCITY VAMC//

F.O.B. POINT: DESTINATION// DESTINATION

### Delivery Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date that the purchase is due at the Delivery Date: prompt. Enter the proposal information that will subsequently be printed on the delivery order, if applicable at the Proposal: prompt. Not applicable can be entered in this free text field (3-45 characters).

At the Est. Shipping and/or handling: prompt, enter the estimated dollar amount between 0 and 9999.99. If there is estimated shipping and /or handling charges, enter the Budget Object Code (BOC) that will pay the charges at the Est. Shipping BOC: prompt.

Enter the line number at the Select Line-Item Number: prompt, followed by entering the Item Master number for the items on the delivery order at the Line Master File No.: prompt. A description is given and can be edited by entering Yes at the Edit? No// prompt.

Enter the quantity of units that you want to purchase. Enter the unit of purchase (boxes, cases, etc.). If you do not know the unit of purchase, enter two question marks (??) at the prompt and IFCAP will list the available units of purchase. Enter the cost per unit at the Actual Unit Cost: prompt. Enter the minimum number of units you can order per shipping package at the Packaging Multiple: prompt. Enter the Unit Conversion Factor. This number is used to convert quantities purchased from Unit of Purchase to Unit of Issue.

Enter the stock number supplied by the vendor for the item.

Enter the national stock number (NSN).

At the Contract: prompt, enter a contract number if the purchase price and vendor are established by a purchasing contract with that vendor.

Enter the Federal Supply Classification (FSC) for an item, or the Product Service Code (PSC) for a service. IFCAP might display some additional prompts based on your entry.

Enter the appropriate contract number at the Contract \#: prompt.

Enter the Budget Object Code classification for the item at the BOC: prompt. It is optional to Enter comments about the item at the Comments: prompt.

If the Vendor is an Electronic Data Interchange (EDI) vendor, you will be prompted with Backorder (EDI): prompt. Enter Y if the Electronic Data Interchange system has set a backorder flag for the item and you want the vendor to place the item on backorder if the item is not available for immediate shipping. At the Substitute (EDI): prompt, enter Y if the Vendor is an Electronic Data Interchange (EDI) vendor and you want the vendor to supply a substitute item (provided the item ordered is not available for immediate shipping).

At the Enter/Edit Delivery Schedule for this Item?: prompt, press the Enter Key or enter “N” if you want all of the items on your request delivered at once. If you enter a delivery schedule for the item, you are notifying the vendor that you want them to deliver different amounts of the items on different days. Make sure that the total number of items among all the delivery dates equals the total number of items you are ordering.

Enter the Sub-Control Point for the purchase if the purchase is from a specific budget within a Control Point.

If the entire delivery order is subject to a percent discount for prompt payment, enter the percentage of the discount at the Select Prompt Payment Percent: prompt, followed by entering the term in days for prompt payment, at the Days (TERM): prompt.

<span id="_Toc222497131" class="anchor"></span>Figure 3: Delivery Date

DELIVERY DATE: JUL 8,2005// (JUL 08, 2005)

PROPOSAL: N/A//

EST. SHIPPING AND/OR HANDLING:

Select LINE ITEM NUMBER: 1

LINE ITEM NUMBER: 1//

ITEM MASTER FILE NO.: 1 DIET SUPMT VANL LQD 8 OZS ............

DESCRIPTION:

DIETARY SUPPLEMENT, THERAPEUTIC. VANILLA FLAVOR; LIQUID

READY-TO-USE; 8 OZ. PULL-TOP CAN; GOOD TASTING ORAL OR TUBE FEEDING

SUPPLEMENT; CALORIES: 1 PER ML.; PROTEIN: 12-27%; FAT: 20-35%;

CARBOHYDRATE: 45-55%; LACTOSE FREE; LOW RESIDUE; CALORIE:NIROGEN RATIO

100-180:1; OSMOLALITY NOT TO EXCEED 625 MOSM/KG. WATER; VITAMINS AND

MINERALS: 100% OF U.S. RDAS IN 2000ML. OR LESS. (ENSURE)

Edit? NO//

QUANTITY: 12

UNIT OF PURCHASE: EA//

ACTUAL UNIT COST: \$0.8500//

PACKAGING MULTIPLE: 1//

UNIT CONVERSION FACTOR: 1//

VENDOR STOCK NUMBER:

NSN: 8940-01-361-8271//

FSC/PSC: 9999//

CONTRACT/BOA \#: DEVELOPMENT06//

BOC: 2660 Operating Supplies and Materials

2660 Operating Supplies and Materials

Select LINE ITEM NUMBER:

COMMENTS:

No existing text

Edit? NO//

Select SUB-CONTROL POINT:

Select PROMPT PAYMENT PERCENT: NET//

DAYS (TERM): 30//

BUSINESS TYPE: 1 SMALL

ITEM: 1, AMOUNT: 10.2

Review Delivery Order ? YES// (YES)

### Review Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After entering all of the required data for a delivery order, IFCAP will ask the user if they would like to ‘Review Delivery Order?’ and display the information for the delivery order in report form. An electronic signature is requested and then the system will display the ‘Cost of this request’ and the ‘Current Control Point Balance’. When an electronic signature code is entered, if the user utilizes the General Inventory Package, the due ins on the item will be set up. The DELIVERY ORDER switch at the station/Fund Control Point level that can be set by Fiscal. If set to YES, the order does not have to go through Fiscal for obligation. The proper FMS documents are created and sent to Austin. If the switch is set to NO, the order will be sent through Fiscal for the obligation process. IFCAP will generate a report that will show all delivery orders that did not come through Fiscal Service for obligation. This can be set up to run automatically on a designated printer in Accounting Service.

<span id="_Toc222497132" class="anchor"></span>Figure 4: Reviewing a Delivery Order

Review Delivery Order? YES// (YES)

DELIVER ORDER: 999-P98082 STATUS: Order Not Completely Prepared

M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.:

REQUESTING SERVICE:

VENDOR: IFVENDOR INC SHIP TO: ANYCITY VAMC

5301 ANY STREET V.A. Medical Center

ANYCITY, CA 99999-3196 50 Some Street, NW

111 555 7771 ANYCITY, DC 11111

FMS Vendor Code: P55396097

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: DESTINATION \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 215000 \| \|

TYPE: DELIVERY ORDER \| \|BUYER:

DELIVER ON/BEFORE 7/8/2005 \|CONTRACT: \| IFUSER SUPPLY

DISCOUNT TERM: NET30 \| DEVELOPMENT06 \|DATE: 6/28/2005

APP: 3650160-255 \| \|

\| \|TOTAL: 10.20

-----------------------------------------------------------------------

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

-----------------------------------------------------------------------

1 DIETARY SUPPLEMENT, 12 EA 0.85 10.20

THERAPEUTIC. VANILLA FLAVOR;

LIQUID READY-TO-USE; 8 OZ.

PULL-TOP CAN; GOOD TASTING ORAL

OR TUBE FEEDING SUPPLEMENT;

CALORIES: 1 PER ML.; PROTEIN:

12-27%; FAT: 20-35%;

CARBOHYDRATE: 45-55%; LACTOSE

FREE; LOW RESIDUE;

CALORIE:NIROGEN RATIO 100-180:1;

OSMOLALITY NOT TO EXCEED 625

MOSM/KG. WATER; VITAMINS AND

MINERALS: 100% OF U.S. RDAS IN

2000ML. OR LESS. (ENSURE)

NSN: 8940-01-361-8271

FOOD GROUP: 5

Items per EA: 1

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

-----------------------------------------------------------------------

BOC: 2660 FMS LINE: 001 CONTRACT: DEVELOPMENT06

END OF DISPLAY--PRESS RETURN OR ENTER '^' TO HALT:

Enter ELECTRONIC SIGNATURE CODE: Thank you.

Print Delivery Order? YES// n (NO)

Cost of this request: \$10.20

Current Control Point Balance: \$2465184.86

## Edit Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Delivery Order option has the same prompts as the Enter Delivery Order option. When a user has to modify the Delivery Order and has not signed off on it yet, they can use the Edit Delivery order option to make the changes. Users can accept the previously entered data at the prompts in the option or edit them by typing the entry after the default.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497133" class="anchor"></span>Figure 5: Editing a Delivery Order

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Select Delivery Orders Menu Option: Edit Delivery Order

### Edit Option Prompts 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the station number, if prompted, followed by the Delivery Order number. Information previously entered will appear as default responses. To accept a default, press the Enter key. To edit the information, simply enter the new response, and the system will accept it.

<span id="_Toc222497134" class="anchor"></span>Figure 6: Editing Options Prompts

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

P.O./REQ.NO.: 999-P98090 06-28-05 ST Order Not Completely Prepared

FCP: 255 \$ 30.15

P.O. DATE: JUN 28,2005//

METHOD OF PROCESSING: INVOICE/RECEIVING REPORT//

ESTIMATED ORDER?: N//

INVOICE ADDRESS: FMS//

PCDO VENDOR: IFVNDOR INC//

FCP: 255 ABC FCP Replace

COST CENTER: 215000//

Enter the word 'PATIENT' in the 'DELIVERY LOCATION' field for a direct delivery

to a patient.

DELIVERY LOCATION:

DELIVERY DATE: JUL 8,2005// (JUL 08, 2005)

PROPOSAL: N/A//

EST. SHIPPING AND/OR HANDLING:

Select LINE ITEM NUMBER: 1//

LINE ITEM NUMBER: 1//

ITEM MASTER FILE NO.: 1//.

DESCRIPTION:

DIETARY SUPPLEMENT, THERAPEUTIC. VANILLA FLAVOR; LIQUID

READY-TO-USE; 8 OZ. PULL-TOP CAN; GOOD TASTING ORAL OR TUBE FEEDING

SUPPLEMENT; CALORIES: 1 PER ML.; PROTEIN: 12-27%; FAT: 20-35%;

CARBOHYDRATE: 45-55%; LACTOSE FREE; LOW RESIDUE; CALORIE:NIROGEN RATIO

100-180:1; OSMOLALITY NOT TO EXCEED 625 MOSM/KG. WATER; VITAMINS AND

MINERALS: 100% OF U.S. RDAS IN 2000ML. OR LESS. (ENSURE)

Edit? NO//

QUANTITY: 12//

UNIT OF PURCHASE: EA//

ACTUAL UNIT COST: \$0.8500//

PACKAGING MULTIPLE: 1//

UNIT CONVERSION FACTOR: 1//

VENDOR STOCK NUMBER:

NSN: 8940-01-361-8271//

FSC/PSC: 9999//

CONTRACT/BOA \#: DEVELOPMENT06//

BOC: 2660 Operating Supplies and Materials Replace

Select LINE ITEM NUMBER:

COMMENTS:

No existing text

Edit? NO//

Select SUB-CONTROL POINT:

Select PROMPT PAYMENT PERCENT: NET//

PROMPT PAYMENT PERCENT: NET//

DAYS (TERM): 30//

BUSINESS TYPE: 1 SMALL

ITEM: 1, AMOUNT: 10.2

Review Delivery Order ? YES// (YES)

## Enter Pharmaceutical PV Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter Pharmaceutical PV Order and Edit Pharmaceutical PV Order options will allow users to place pharmaceutical PV orders for delivery at the service level. Pharmaceutical PV orders are placed against an existing contract. The Method of processing (MOP) for Pharmaceutical PV Orders is “Auto Bank Payment". This MOP is not entered by the user; it is populated automatically by the IFCAP system. No receiving is done on pharmaceutical orders. Once the user signs the Pharmaceutical PV Order with their electronic signature code, the status of the order automatically changes to "Complete Order Received”. There will be no receiving report transmitted to Austin.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497135" class="anchor"></span>Figure 7: Entering Pharmaceutical PV Order Menu Path

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Select Delivery Order Menu Option: Enter Pharmaceutical PVOrder

### Setup Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the station number, if prompted. Next, enter the purchase order number followed by the Purchase Order (P.O.) date. IFCAP will then ask you if the order is an estimated order. At the Estimated Order?” prompt enter “YES” or “NO”. The default is No. Estimated orders are orders that have an unknown cost or quantity. Orders for services, i.e., equipment repair, are often estimated orders, since the vendor doesn’t determine the actual cost until the vendor completes the repair. Enter the Invoice Address followed by the Purchase Card Delivery Order (P.C.D.O.) Vendor. Enter the name of the vendor, or the first few letters of the vendor's name. You can type three question marks (???) at the prompt to list all of the vendors in the system. If you do not know which vendor has the item you want, follow the instructions in the “How to Consult the Item Master File” section of the Control Point Clerk's Guide. Enter the Fund Control Point (FCP) followed by the appropriate Cost Center.

Specify the location for delivery at the Delivery Location: prompt and enter where you want the vendor to deliver the purchase at the “Ship To:” prompt.

<span id="_Toc222497136" class="anchor"></span>Figure 8: Pharmaceutical PV Order Setup Parameters

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

ENTER A NEW DELIVERY ORDER NUMBER OR A COMMON NUMBERING SERIES

DELIVERY ORDER: P98 999-P98 DO AUTHORIZED BUYER

Are you adding '999-P98083' as a new Purchase Order number ? Y (YES)

P.O. DATE: TODAY// (JUN 28, 2005)

PCDO VENDOR: 18 IFVENDOR INC PH:111 555-7771 NO: 18

ORD ADD:5301 ANY STREET FMS:IFVENDOR INC

ANYCITY, CA 99999-3196 CODE:P55396097 FAX:

...OK? Yes// (Yes)

FCP: 255 FCP 0160A1 10 0100 989

COST CENTER: 215000 Telecommunications

Enter the word 'PATIENT' in the 'DELIVERY LOCATION' field for a direct delivery

to a patient.

DELIVERY LOCATION:

SHIP TO: ANYCITY VAMC//

### Order Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the date that the purchase is due at the Delivery Date: prompt. Enter the line number at the Select Line-Item Number: prompt, followed by the Item Master number for the items on the delivery order at the Line Master File No.: prompt. The line items used must have a contract number assigned. A description is given and can be edited by entering Yes at the Edit? No// prompt. Enter the quantity of units that you want to purchase. Enter the unit of purchase (boxes, cases, etc.). If you do not know the unit of purchase, enter two question marks (??) at the prompt and IFCAP will list the available units of purchase. Enter the cost per unit at the Actual Unit Cost: prompt.

<span id="_Toc222497137" class="anchor"></span>Figure 9: Delivery Date Menu

DELIVERY DATE: TODAY+1// (JUN 29, 2005)

Select LINE ITEM NUMBER: 1

LINE ITEM NUMBER: 1//

ITEM MASTER FILE NO.: 1 DIET SUPMT VANL LQD 8 OZS ............

DESCRIPTION:

DIETARY SUPPLEMENT, THERAPEUTIC. VANILLA FLAVOR; LIQUID

READY-TO-USE; 8 OZ. PULL-TOP CAN; GOOD TASTING ORAL OR TUBE FEEDING

SUPPLEMENT; CALORIES: 1 PER ML.; PROTEIN: 12-27%; FAT: 20-35%;

CARBOHYDRATE: 45-55%; LACTOSE FREE; LOW RESIDUE; CALORIE:NIROGEN RATIO

100-180:1; OSMOLALITY NOT TO EXCEED 625 MOSM/KG. WATER; VITAMINS AND

MINERALS: 100% OF U.S. RDAS IN 2000ML. OR LESS. (ENSURE)

Edit? NO//

QUANTITY: 12

UNIT OF PURCHASE: EA//

ACTUAL UNIT COST: \$0.0000// 0.85 \$0.8500

BOC: 2660 Operating Supplies and Materials

2660 Operating Supplies and Materials

Select LINE ITEM NUMBER:

COMMENTS:

No existing text

Edit? NO//

BUSINESS TYPE: 1 SMALL

ITEM: 1, AMOUNT: 10.2

Review Delivery Order ? YES// (YES)

### Review Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After entering all of the required data for a delivery order, IFCAP will ask the user if they would like to Review Delivery Order and display the information. An electronic signature is requested and then the system will display the Cost of this request and the Current Control Point Balance. When an electronic signature code is entered, if the user utilizes the General Inventory Package, the due ins on the item will be set up.

<span id="_Toc222497138" class="anchor"></span>Figure 10: Reviewing a Delivery Order Menu

DELIVER ORDER: 999-P98083 STATUS: Order Not Completely Prepared

M.O.P.: AUTO BANK PAYMENT LAST PARTIAL RECD.:

REQUESTING SERVICE:

VENDOR: IFVENDOR INC SHIP TO: ANYCITY VAMC

5301 ANY STREET V.A. Medical Center

ANYCITY, CA 99999-3196 50 Some Street, NW

111 555 7771 ANYCITY, DC 11111

FMS Vendor Code: P55396097

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: DESTINATION \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 215000 \| \|

TYPE: DELIVERY ORDER \| \|BUYER:

DELIVER ON/BEFORE 6/29/2005 \|CONTRACT: \| IFBUYER

DISCOUNT TERM: \| DEVELOPMENT06 \|DATE: 6/28/2005

APP: 3650160-255 \| \|

\| \|TOTAL: 10.20

-------------------------------------------------------------------------------

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

-------------------------------------------------------------------------------

1 DIETARY SUPPLEMENT, 12 EA 0.85 10.20

THERAPEUTIC. VANILLA FLAVOR;

LIQUID READY-TO-USE; 8 OZ.

PULL-TOP CAN; GOOD TASTING ORAL

OR TUBE FEEDING SUPPLEMENT;

CALORIES: 1 PER ML.; PROTEIN:

12-27%; FAT: 20-35%;

CARBOHYDRATE: 45-55%; LACTOSE

FREE; LOW RESIDUE;

CALORIE:NIROGEN RATIO 100-180:1;

OSMOLALITY NOT TO EXCEED 625

MOSM/KG. WATER; VITAMINS AND

MINERALS: 100% OF U.S. RDAS IN

2000ML. OR LESS. (ENSURE)

NSN: 8940-01-361-8271

FOOD GROUP: 5

Items per EA: 1

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

-------------------------------------------------------------------------------

BOC: 2660 FMS LINE: 001 CONTRACT: DEVELOPMENT06

END OF DISPLAY--PRESS RETURN OR ENTER '^' TO HALT:

Enter ELECTRONIC SIGNATURE CODE: Thank you.

Print Delivery Order? YES// n (NO)

Cost of this request: \$10.20

Current Control Point Balance: \$2465174.66

...updating running balance status fields in 410...WITH 2237

...now generating the FMS Miscellaneous Order (MO) Document...

...HMMM, I'M WORKING AS FAST AS I CAN...

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

...now generating the PHA transaction

## Edit Pharmaceutical PV Order 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Pharmaceutical PV Order option has the same prompts as the Enter Pharmaceutical PV Order option. When a user has to modify the Pharmaceutical PV Order and has not signed off on it yet, they can use the Edit Delivery order option to make the changes. Users can accept the previously entered data at the prompts in the option or edit them by typing the new entry at the default.

## Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497139" class="anchor"></span>Figure 11: Editing a Pharmaceutical PV Order Menu

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Select Delivery Orders Menu Option: Edit Pharmaceutical PV Order

## Edit option prompts 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the station number if prompted, followed by the Purchase Order (P.O.) number. All prompts can be edited in this option. Information will default to what was previously entered. To accept a default, press the Enter key. To edit the information, simply enter the new response, and the system will accept it. Please see the Enter Pharmaceutical PV Order option documentation for a sample of the prompts.

## Delivery Order from Repetitive Item List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user creates a delivery order from a repetitive item list, IFCAP will adjust the due-in inventory balances for the items on the order.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497140" class="anchor"></span>Figure 12: Creating a Delivery Order from a Repetitive Item List Menu

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Select Delivery Order Menu Option: Create Delivery Order From Repetitive Item List

### Select Repetitive Item List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the repetitive item list you want to use at the Select Repetitive Item List Entry Number: prompt. If your station has substations, IFCAP will prompt you to enter the substation for which you are ordering the items. You can enter a question mark at the Substation: prompt to see a list of available substations.

<span id="_Toc222497141" class="anchor"></span>Figure 13: Selecting a Repetitive Item List Menu

Select REPETITIVE ITEM LIST ENTRY NUMBER: 999-00-3-036-828100-0001 04-13-00

\# OF ITEMS: 5TOTAL COST: 3885.26

This repetitive item list has the following vendors:

IFVENDOR,THREE

IFVENDOR,FOUR

IFVENDOR,FIVE

IFVENDOR,SIX

IFVENDOR,SEVEN

ENTER A NEW DELIVERY ORDER NUMBER OR A COMMON NUMBERING SERIES

DELIVERY ORDER: u0 999-U0 DO AUTHORIZED BUYER

Are you adding '999-U00044' as a new Purchase Order number ? y (YES)

Edit request 999-U00044? Yes// n (No)

Request 999-U00044 has been created.

The vendor for this request is: IFVENDOR,FOUR

Total cost of request: \$230.00

Total items on delivery request: 1

ENTER A NEW DELIVERY ORDER NUMBER OR A COMMON NUMBERING SERIES

DELIVERY ORDER: u0 999-U0 DO AUTHORIZED BUYER

Are you adding '999-U00045' as a new Purchase Order number ? y (YES)

Edit request 999-U00045? Yes// n (No)

Request 999-U00045 has been created.

The vendor for this request is: IFVENDOR,FIVE

Total cost of request: \$0.90

Total items on delivery request: 1

ENTER A NEW DELIVERY ORDER NUMBER OR A COMMON NUMBERING SERIES

DELIVERY ORDER: u0 999-U0 DO AUTHORIZED BUYER

Are you adding '999-U00046' as a new Purchase Order number ? y (YES)

Edit request 999-U00046? Yes// n (No)

Request 999-U00046 has been created.

The vendor for this request is: IFVENDOR,SEVEN

Total cost of request: \$20.28

Total items on delivery request: 1

Total number of requests generated: 3

Total cost of all requests: \$251.18

Generating delivery orders....

Request 999-00-3-036-0032 created.

Request 999-00-3-036-0033 created.

Request 999-00-3-036-0034 created.

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will print a report on the new delivery order, listing the delivery order number, the vendor, the number of items on the order, and the cost of the order. If the repetitive item list still has some items that do not have contract numbers, IFCAP will return to the Delivery Order Menu. If the repetitive item list is empty, IFCAP will prompt you to declare whether you want to re-use the repetitive item list. Enter “N” to delete the repetitive item list. IFCAP will return to the Delivery Order Menu.

<span id="_Toc222497142" class="anchor"></span>Figure 14: Confirmation of Re-Using the Repetitive Item List Prompt

Do you wish to re-use this list? No// (No)

End of processing.

## Receive Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is similar to the Receipt of Purchase Order option on the Warehouse Menu but is limited to Delivery Orders only. Users will only be able to report the receipt of items for which they are the authorized buyer. IFCAP will update inventory due ins at the end of the receipt process.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497143" class="anchor"></span>Figure 15: Receiving a Delivery Order Menu

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Delivery Order Menu Option: Receive Delivery Order

### Data Display 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the Station Number if prompted, and the Delivery Order number to be received, IFCAP will display the delivery order number with the station number as a prefix. In addition, the status of the order, the Fund Control Point, and the purchasing agent that created the delivery order is displayed. Type Y for Yes at the Review Delivery Order?: prompt.

<span id="_Toc222497144" class="anchor"></span>Figure 16: Data Display Menu

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

PURCHASE ORDER: U00001 999-U00001 02-23-00 ST Pending Fiscal Action

FCP: 081 \$ 106.20

PA/PPM/AUTHORIZED BUYER: IFUSER,TWO

REVIEW PURCHASE ORDER? NO// Y (YES)

### Check for Shipping Discrepancy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Compare the goods to the items on the delivery order record in IFCAP. The IFCAP line item for the goods should be the same as the goods delivered, unless the delivery order indicates that the item has been extracted for purchase elsewhere or canceled. Otherwise, if the goods delivered are not the same in type or quantity, there is a shipping discrepancy. If there is a discrepancy other than receipt of a lesser or greater quantity that IFCAP lists for the purchase, quit the Receive Delivery Order option by entering a caret (^) at the prompts. If there is a greater quantity delivered than IFCAP lists for the purchase, enter the date received.

<span id="_Toc222497145" class="anchor"></span>Figure 17: Checking for Shipping Discrepancy Menu

DELIVER ORDER: 999-U00001 STATUS: Pending Fiscal Action

M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.:

REQUESTING SERVICE:

VENDOR: IFVENDOR,ONE SHIP TO: Warehouse

GOVERNMENT CUSTOMER SERVICE V.A. Medical Center

3651 ANYROAD DRIVE 1 Main Street

ANYTOWN, IL 99999 ANYCITY, DC 11111

8005555555

ACCT \# 454207487013 DELIVERY HOURS:

FMS Vendor Code: 000987634 8 am - 4 pm

DELIVERY LOCATION: RM 3 BLD 6

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: DESTINATION \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 828100 \| \|

TYPE: DELIVERY ORDER \| \|BUYER:

DELIVER ON/BEFORE 3/4/2000 \|CONTRACT: \| IFUSER,TWO

DISCOUNT TERM: NET30 \| V797P1112A \|DATE: 2/23/2000

APP: 3640160-081 \| \|

\| \|TOTAL: 106.20

----------------------------------------------------------------------------

ITEM DESCRIPTION QTY UNIT COST COST

-------------------------------------------------------------------------------

1 THINGS-METAL-POINTED 12 EA 4.35 52.20

STK#: 8977

NSN: 7111-28-276-3377

Items per EA: 1

BOC: 2660 FMS LINE: 001 CONTRACT: V797P1112A

2 WIDGETS-WOODEN-MULTI-PURPOSE 10 EA 5.40 54.00

NSN: 7111-23-228-3937

Items per EA: 1

BOC: 2660 FMS LINE: 001 CONTRACT: V797P1112A

V.A. TRANSACTION NUMBERS:

999-00-2-081-0006

END OF DISPLAY--PRESS RETURN OR ENTER '^' TO HALT:

### Receipt of Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are no discrepancies between the shipment and the delivery order, enter the date received, followed by entering the line-item number for the purchase at the Line Item: prompt. Enter “A” at the Line Item: prompt to scroll through all outstanding items on the delivery order. Enter “C” to complete the delivery order as is. Enter your electronic signature code and print the receiving report. Type “Y” for yes at the Approve this receiving report and print in Receiving?: prompt. If the delivery order switch is not set to bypass Fiscal Service and the method of processing is not "Auto Bank Payment", IFCAP will ask you if you want to print the receiving report in Fiscal Service. If you want to enter another receiving report, enter another delivery order number at the Delivery Order: prompt. Otherwise, press the Enter key to return to the Delivery Order Menu.

*<u>NOTE:</u>* If you make a mistake during the Receive Delivery Order option, enter “N” at the DO YOU WANT TO ALSO PRINT THE REPORT IN FISCAL? prompt.

<span id="_Toc222497146" class="anchor"></span>Figure 18: Receipt of Item Menu

DATE RECEIVED: TODAY// (MAY 17, 2000)

LINE ITEM: 1

Item: 1 1 THINGS-METAL-POINTED

STK#: 8977 NSN: 7111-28-276-3377

THINGS-METAL-POINTED

UNIT OF PRCH: EA QTY ORDERED: 12 PREVIOUSLY RECEIVED: 0

QTY BEING RECEIVED: 10// AMOUNT: 43.50

LINE ITEM: C

Complete P.O. as is? YES// Y (YES)

PURCHASE ORDER: 999-U00001 STATUS: Pending Fiscal Action

PROCESSING: INVOICE/RECEIVING REPORT PARTIAL: 1 5/17/2000

-------------------------------------------------------------------------------

UNIT QTY TOTAL

ITEM DESCRIPTION QTY UNIT COST REC COST

-------------------------------------------------------------------------------

1 THINGS-METAL-POINTED 12 EA 4.35 10 43.50

IMF \#: 100002 CONTRACT: V797P1112A

2 WIDGETS-WOODEN-MULTI-PURPOSE 10 EA 5.40 10 54.00

IMF \#: 100003 CONTRACT: V797P1112A

Total Amount: 97.50

Approve this receiving report and print in Receiving ? YES// Y (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

Do you want to also print Receiving Report in FISCAL ? YES// \<ENTER\> (YES)

DELIVERY ORDER:

## Amendment to Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP will allow amendments to the following fields: SHIP TO; LINE ITEM ADD; LINE-ITEM EDIT; LINE ITEM DELETE; MAIL INVOICE; EST SHIPPING/HANDLING; PROMPT PAYMENT; Authority Edit and F.O.B.

A user can also amend a VENDOR; however, the system will prompt for a valid contract number for each line item. Amendments will follow the DELIVERY ORDER switch, and either be routed through Accounting Service or obligated automatically. Inventory due-ins information will also be updated through Accounting Service or obligated automatically.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497147" class="anchor"></span>Figure 19: Amending a Delivery Order Menu

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Select Delivery Order Menu Option: Amendment to Delivery Order

### Order Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number. Enter the purchase order number. IFCAP will display the date, A&MM status, Fund Control Point, cost of the order, and Vendor name. At the Effective Date: prompt, enter the date that the amendment will take effect, or press the Enter key to accept the default of today's date. At the Authority: prompt, enter the authority by which you amend the delivery order. If you do not know the applicable authorization, enter three question marks and IFCAP will list the available authority categories. Enter comments about the amendment if you like at the Type Comments: prompt. At the Contractor Required to Sign: prompt, enter “Y” if the contractor has to sign the amendment showing that they accept the terms of the amendment. The system will generate a list of available amendment types. Enter the type of amendment you are making to the delivery order.

The user must respond with the corresponding code from the list of Amendment (name) types. You may see additional prompts not described here, depending on which amendment type you choose. If you choose the amendment "Line Item Add", answer “Y” at the Add Line Item?: prompt and enter an Item Master File number and description for the item. Enter Quantity, Unit of Purchase, Unit of Cost, and Packaging information about the new item.

<span id="_Toc222497148" class="anchor"></span>Figure 20: Amendment Order Information Menu

Select STATION NUMBER ('^' TO EXIT): 111// \<ENTER\> MYTOWN, VA

Select Delivery Orders Menu Option: amendment To Delivery Order

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

PURCHASE ORDER: u0

1 U00001 999-U00001 02-04-00 ST Order Not Completely Prepared

FCP: 060 \$ 0.00

2 U00002 999-U00002 02-04-00 ST Cancelled Order

FCP: 110 \$ 3.40

3 U00003 999-U00003 02-04-00 ST Partial Order Received

FCP: 110 \$ 5144.00

4 U00004 999-U00004 02-04-00 ST Partial Order Received

FCP: 060 \$ 2660.00

5 U00005 999-U00005 02-04-00 ST Ordered (No Fiscal Action Required

FCP: 110 \$ 5.32

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5:

6 U00006 999-U00006 02-07-00 ST Ordered (No Fiscal Action Required

FCP: 060 \$ 5320.00

7 U00007 999-U00007 02-08-00 ST Cancelled Order

FCP: 110 \$ 0.00

8 U00008 999-U00008 02-08-00 ST Order Not Completely Prepared

FCP: 110 \$ 0.00

9 U00009 999-U00009 02-09-00 ST Order Not Completely Prepared

FCP: 110 \$ 1.00

10 U00010 999-U00010 02-09-00 ST Ordered (No Fiscal Action Required

FCP: 110 \$ 1.00

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-10: 6 999-U00006 02-07-00 ST Ordered (No Fiscal Action Required

FCP: 060 \$ 5320.00

Amendment Number: 1

...copying Purchase Order into work file...

...HMMM, HOLD ON...

EFFECTIVE DATE: TODAY// (JUN 07, 2000)

AUTHORITY: D// OTHER (specify type of modification and authority)

TYPE COMMENTS:

CONTRACTOR REQUIRED TO SIGN?: NO// NO

Select one of the following:

1 Change VENDOR

2 AUTHORITY Edit

3 LINE ITEM Add

4 LINE ITEM Delete

5 LINE ITEM Edit

6 F.O.B. Point

7 SHIP TO Edit

8 Edit MAIL INVOICE TO

9 EST. SHIPPING Edit

10 PROMPT PAYMENT Edit

Select TYPE OF AMENDMENT NUMBER: 3 LINE ITEM Add

...EXCUSE ME, JUST A MOMENT PLEASE...

ADD LINE ITEM 2? NO// y (YES)

ITEM MASTER FILE NO.: 3094 CONTRACT ITEM ..

DESCRIPTION:

1\> CONTRACT ITEM TO TEST DELIVERY ORDERS

EDIT Option:

QUANTITY: 12

UNIT OF PURCHASE: EA//

ACTUAL UNIT COST: \$2.6600//

PACKAGING MULTIPLE: 1//

### Item Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the Unit Conversion Factor. At the Vendor Stock Number: prompt, enter the stock number supplied by the vendor for the item. Enter the national stock number (NSN). Enter the Federal Supply Classification of the item. IFCAP might list some additional prompts based on the Federal Supply Classification. At the Contract \#: prompt, enter a contract number if the purchase price and vendor are established by the purchasing contract with that vendor. Enter the Budget Object Code classification for the item at the BOC: prompt. If you do not know the Budget Object Code, enter three question marks at the prompt and IFCAP will display the available Budget Object Codes. At the Backorder (EDI) prompt, enter “Y” if the Electronic Data Interchange system has set a backorder flag for the item. Also enter Yes if the vendor is an Electronic Data Interchange (EDI) vendor and you want the vendor to place the item on back order if the item is not available for immediate shipping. At the Substitute (EDI) prompt, enter “Y” if the vendor is an Electronic Data Interchange (EDI) vendor and you want the vendor to supply a substitute item (provided the item you ordered is not available for immediate shipping).

<span id="_Toc222497149" class="anchor"></span>Figure 21: Amendment Item Information

UNIT CONVERSION FACTOR: 1//

VENDOR STOCK NUMBER: 4565//

NSN: 7111-88-723-3375//

FEDERAL SUPPLY CLASSIFICATION: 9999//

CONTRACT/BOA \#: MCG-0079//

BOC: 2660 Operating Supplies and Materials Replace

BACKORDER (EDI):

SUBSTITUTE (EDI)

### Delivery Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Enter/Edit Delivery Schedule for this Item?: prompt, press the Enter key or enter “N” if you want all of the items on your request delivered at once. If you enter a delivery schedule for the item, you are notifying the vendor that you want them to deliver different amounts of the items on different days. Make sure that the total number of items among all of the delivery dates equals the total number of items you are ordering. To make additional amendments, choose a new type of amendment to the delivery order. Once again, a list is provided to choose from. If you choose the "F.O.B. Point" amendment, enter “O” for origin at the F.O.B. (Freight on Board) Point: prompt if additional freight charges are due to the carrier at the time of delivery. If there are estimated shipping and/or handling charges, enter the Budget Object Code (BOC) that will pay the charges at the Est. Shipping BOC: prompt. Enter another amendment number or press the Enter key. Enter the delivery date of the item. Enter the Amendment/Adjustment Status. You can enter a question mark at the prompt to see a list of available status. Enter a justification for the amendment. You can review the amendment by answering “YES” to the Review Amendment? YES// prompt. To approve the amendment, enter “Y” at the Approve and print Amendment number?: prompt. Enter your electronic signature code. Enter a printer device.

<span id="_Toc222497150" class="anchor"></span>Figure 22: Enter/Edit Delivery Schedule Menu

Select one of the following:

1 Change VENDOR

2 AUTHORITY Edit

3 LINE ITEM Add

4 LINE ITEM Delete

5 LINE ITEM Edit

6 F.O.B. Point

7 SHIP TO Edit

8 Edit MAIL INVOICE TO

9 EST. SHIPPING Edit

10 PROMPT PAYMENT Edit

Select TYPE OF AMENDMENT NUMBER:

DELIVERY DATE: FEB 17,2000//

AMENDMENT/ADJUSTMENT STATUS: Ordered (No Fiscal Action)-Amended

// 23

JUSTIFICATION: NEED IT

Review Amendment ? YES//

Approve Amendment number 1: ? NO// Y (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

SEND TO SUPPLY

QUEUE ON DEVICE:

## Adjustment Voucher to Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to decrease the quantity received on a receiving report for a delivery order. This option will follow the prompts of the current Adjustment Voucher option. Depending upon where the order is in the system, the system will update the status to one of the following:

- Ordered (No Fiscal Action Required) - Amended
- Partial Order Received (Amended)
- Complete Order Received (Amended)
- Transaction Complete (Amended)

*<u>Note:</u>* IFCAP does NOT transmit amendments to EDI orders to the EDI vendor. You must contact the vendor to inform the vendor of the amendment.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497151" class="anchor"></span>Figure 23: Adjustment Voucher for a Delivery Order Menu

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Select Delivery Order Menu Option: Adjustment Voucher to Delivery Order

### Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a station number. Enter a delivery order number or enter a question mark to see a list of available delivery orders. The system will display the adjustment number and ask the user “Do you wish to continue?” YES//.

At the Effective Date: prompt, enter the date that the adjustment will take effect. You may enter the new status of the delivery order at the Amendment/Adjustment Status: prompt or enter a question mark to see a list of valid status. If the status is changed to Partial Order Received, select a date of a receiving report at the Select Partial Date prompt. If you do not know the report date, enter a question mark and IFCAP will list the available dates.

<span id="_Toc222497152" class="anchor"></span>Figure 24: Adjustment Voucher Listing Menu

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

PURCHASE ORDER: U00001 999-U00001 02-23-00 ST Pending Fiscal Action

FCP: 081 \$ 106.20

Adjustment number: 1

Do you wish to continue? YES// Y (YES)

EFFECTIVE DATE: T (MAY 22, 2000)

AMENDMENT/ADJUSTMENT STATUS:

Select PARTIAL DATE: ?

Answer with PARTIAL NUMBER, or DATE:

1 MAY 17, 2000

Select PARTIAL DATE: 1 5-17-2000

...SORRY, THIS MAY TAKE A FEW MOMENTS...

### Item Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the item you want to adjust at the Select Item: prompt. Enter the actual quantity received at the Qty Being Received: prompt. You may select another item or press the Enter key. You can review the adjustment and edit the description of the adjustment voucher. If the adjustment is correct, approve the adjustment and enter your electronic signature code. IFCAP will update the record of items that are due at the inventory point based on the adjustment. Enter another delivery order at the Delivery Order: prompt or press the Enter key to return to the Delivery Order Menu.

<span id="_Toc222497153" class="anchor"></span>Figure 25: Adjustment Voucher Item Selection

Select ITEM: ?

Answer with ITEM LINE ITEM NUMBER

Choose from:

1 THINGS-METAL-POINTED

2 WIDGETS-WOODEN-MULTI-PURPOSE

Select ITEM: 1 THINGS-METAL-POINTED

QTY BEING RECEIVED: 10// 9

Select ITEM:

Review Adjustment ? YES// n (NO)

Edit Description ? NO// N (NO)

Approve and print (in FISCAL and SUPPLY) Adjustment no.: 1? NO// Y (YES)

Enter ELECTRONIC SIGNATURE CODE: Thank you.

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...

...please wait while I update the due-ins at the inventory points...

SEND TO SUPPLY

## Convert a Delivery Order to a 2237 Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IFCAP users may attempt to order items on a Delivery Order that must be ordered on a VA Form 90-2237 (Request, Turn-in and Receipt for Property or Services), such as posted stock items. Use this option to convert a delivery order into a 2237 order.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497154" class="anchor"></span>Figure 26: Converting a Delivery Order to a 2237 Request Menu

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Select Delivery Order Menu Option: Convert Delivery Order to a 2237 Request

### Select Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the Station Number, and a Delivery order number. IFCAP will display the number assigned by the system for the new 2237 order.

*<u>NOTE:</u>* You must use the “Edit A 2237 (Service)” option in the Process a Request Menu to submit the 2237 order for purchase.

<span id="_Toc222497155" class="anchor"></span>Figure 27: Selecting a Delivery Order Menu

Select Delivery Orders Menu Option: CD2 Convert Delivery Order to a 2237 Request

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

P.O./REQ. NO.: U0

1 U00001 999-U00001 02-04-00 ST Order Not Completely Prepared

FCP: 060 \$ 0.00

2 U00002 999-U00002 02-04-00 ST Cancelled Order

FCP: 110 \$ 3.40

3 U00007 999-U00007 02-08-00 ST Order Not Completely Prepared

FCP: 110 \$ 0.00

4 U00008 999-U00008 02-08-00 ST Order Not Completely Prepared

FCP: 110 \$ 0.00

5 U00009 999-U00009 02-09-00 ST Order Not Completely Prepared

FCP: 110 \$ 1.00

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 3 999-U00007 02-08-00 ST Order Not Completely Prepared

FCP: 110 \$ 0.00

1\) 999-IFUSER,THREE

2\) 999-IFUSER,THREE2

Select INVENTORY POINT: (1-2): 1 999-IFUSER,THREE

Use transaction 999-00-2-110-0047 to access this record

from your fund control point.

Conversion completed.

## Convert Delivery Order to a Purchase Card Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you create a delivery order for items that are not available on an established contract with a vendor, you will need to translate the delivery order into a purchase card order.

*<u>NOTE:</u>* Delivery Orders that have been completed and signed electronically cannot be converted to a Purchase Card Order

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497156" class="anchor"></span>Figure 28: Converting a Delivery Order to a Purchase Card Order Menu

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Delivery Orders Menu Option: Convert Delivery Order To a Purchase Card Order

### Select Order Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station Number and a Delivery Order Number. The system will ask for the Common Numbering Series, for the New Purchase Card Number. The user can enter double question marks (??) to see a display of options. After that selection has been made. IFCAP will display the assigned number for the new purchase card order.

<span id="_Toc222497157" class="anchor"></span>Figure 29: Selecting an Order Number Menu

You have 477 new messages. (Last arrival: 07 Jun 00 16:55)

Select Delivery Orders Menu Option: CDP Convert Delivery Order To a Purchase Ca

rd Order

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

Select DELIVERY ORDER NUMBER: U0

1 U00001 999-U00001 02-04-00 ST Order Not Completely Prepared

FCP: 060 \$ 0.00

2 U00002 999-U00002 02-04-00 ST Order Not Completely Prepared

FCP: 110 \$ 3.40

3 U00007 999-U00007 02-08-00 ST Order Not Completely Prepared

FCP: 110 \$ 0.00

4 U00008 999-U00008 02-08-00 ST Order Not Completely Prepared

FCP: 110 \$ 0.00

5 U00009 999-U00009 02-09-00 ST Order Not Completely Prepared

FCP: 110 \$ 1.00

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 2 999-U00002 02-04-00 ST Order Not Completely Prepared

FCP: 110 \$ 3.40

ENTER A NEW PURCHASE ORDER NUMBER OR A COMMON NUMBERING SERIES

PURCHASE ORDER: P05 999-P05 PC AUTHORIZED BUYER

Are you adding '999-P05184' as a new Purchase Order number ? Y (YES)

This delivery order is now converted to a purchase card order

The Deliver Order No: U00002 has been converted

to Purchase Card Order No: P05184

This purchase card order must be edited.

PURCHASE ORDER:

## Cancel an Incomplete Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cancel an Incomplete Delivery Order Option allows users to cancel incomplete delivery orders.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497158" class="anchor"></span>Figure 30: Canceling an Incomplete Delivery Order Menu

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Select Delivery Orders Menu Option: Cancel an Incomplete Delivery Order

### Cancel the Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Delivery Order Number. The user can enter double question marks (??) to see a display of delivery order numbers. After that selection has been made, IFCAP will ask “Are you sure you want to cancel this order?” NO//. The default is No, just in case the user accidentally enters too many returns. Respond Yes to cancel the requested delivery order number.

Select DELIVERY ORDER NUMBER: U00014 999-U00014 05-17-00 AB Order Not Completely Prepared

<span id="_Toc222497159" class="anchor"></span>Figure 31: Canceling the Order Confirmation Order

FCP: 081 \$ 0.00

Are sure you want to cancel this order? NO// Y (YES)

## Display Delivery Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Display Delivery Order Option allows users to display a complete report of a delivery order.

### Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc222497160" class="anchor"></span>Figure 32: Displaying a Delivery Order Menu Path

Enter Delivery Order

Edit Delivery Order

Enter Pharmaceutical PV Order

Edit Pharmaceutical PV Order

Create Delivery Order From Repetitive Item List

Receive Delivery Order

Amendment To Delivery Order

Adjustment Voucher To Delivery Order

CD2 Convert Delivery Order to a 2237 Request

CDP Convert Delivery Order To a Purchase Card Order

Cancel an Incomplete Delivery Order

Display Delivery Order

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Delivery Orders Menu Option: Display Delivery Order

### Display Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Station Number, followed by a Delivery Order Number. The user can enter double question marks (??) to see a display of delivery order ^numbers. After that selection has been made, IFCAP will display the complete delivery order.

The next prompt is “Review a Receiving Report?” NO//. If you would like to review the receiving report for this order enter “YES” at this prompt. If the user answers “NO”, the system will ask for another Delivery Order number to display. Enter another Delivery Order number or Press the Enter key to return to the Delivery Order Menu.

<span id="_Toc222497161" class="anchor"></span>Figure 33: Displaying a Delivery Order Menu

Select STATION NUMBER ('^' TO EXIT): 999// ANYCITY, DC

P.O./REQ.NO.: U00001 999-U00001

DELIVER ORDER: 999-U00001 STATUS: Pending Fiscal Action

M.O.P.: INVOICE/RECEIVING REPORT LAST PARTIAL RECD.: 1 05/17/00

REQUESTING SERVICE:

VENDOR: IFVENDOR,ONE SHIP TO: Warehouse

GOVERNMENT CUSTOMER SERVICE V.A. Medical Center

3651 ANYROAD DRIVE 1 Main Street

ANYTOWN, IL 99999 ANYCITY, DC 11111

8005555555

ACCT \# 454207487013 DELIVERY HOURS:

FMS Vendor Code: 000987634 8 am - 4 pm

DELIVERY LOCATION: RM 3 BLD 6

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOB POINT: DESTINATION \|PROPOSAL: N/A \|AUTHORITY:

COST CENTER: 828100 \| \|

TYPE: DELIVERY ORDER \| \|BUYER:

DELIVER ON/BEFORE 3/4/2000 \|CONTRACT: \| IFUSER,TWO

DISCOUNT TERM: NET30 \| V797P1112A \|DATE: 2/23/2000

APP: 3640160-081 \| \|

\| \|TOTAL: 106.20

-------------------------------------------------------------------------------

ENTER '^' TO HALT:

UNIT TOTAL

ITEM DESCRIPTION QTY UNIT COST COST

-------------------------------------------------------------------------------

1 THINGS-METAL-POINTED 12 EA 4.35 52.20

STK#: 8977

NSN: 7111-28-276-3377

QTY PREV RCVD: 10

PARTIAL NO.: 1

Items per EA: 1

BOC: 2660 FMS LINE: 001 CONTRACT: V797P1112A

2 WIDGETS-WOODEN-MULTI-PURPOSE 10 EA 5.40 54.00

NSN: 7111-23-228-3937

QTY PREV RCVD: 10

PARTIAL NO.: 1

Items per EA: 1

BOC: 2660 FMS LINE: 001 CONTRACT: V797P1112A

V.A. TRANSACTION NUMBERS:

999-00-2-081-0006

Review a Receiving Report ? NO// (NO)

P.O./REQ.NO.: \<ENTER\>

Select Delivery Orders Menu Option:

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term                                       | Definition                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1358                                       | VA Form 1358 Estimated Obligation or Change in Obligation.                                                                                                                                                                                                                                                                                                                                                      |
| 2138                                       | VA Form 90-2138, Order for Supplies or Services. First page of a VA Purchase Order.                                                                                                                                                                                                                                                                                                                             |
| 2139                                       | VA Form 90-2139, Order for Supplies or Services (Continuation). This is a continuation sheet for the 2138 form.                                                                                                                                                                                                                                                                                                 |
| 2237                                       | VA Form 90-2237, Request, Turn-in and Receipt for Property or Services. Used to request goods and services.                                                                                                                                                                                                                                                                                                     |
| A&MM                                       | Acquisition and Materiel Management Service.                                                                                                                                                                                                                                                                                                                                                                    |
| Accounting Technician                      | Fiscal employee responsible for obligation of and payment for goods and services. Accounting Technicians process accounting transactions and transmit them to FMS.                                                                                                                                                                                                                                              |
| ADP Security Officer                       | The individual at your station who’s responsible for the security of the computer system, both its physical integrity and the integrity of the records stored in it. Includes overseeing file access.                                                                                                                                                                                                           |
| Agent Cashier                              | The person in Fiscal Service (often physically located elsewhere) who makes or receives payments on debtor accounts and issues official receipts.                                                                                                                                                                                                                                                               |
| Allowance table                            | Reference table in FMS that provides financial information at the level immediately above the sub-allowance level.                                                                                                                                                                                                                                                                                              |
| Amendment                                  | A document that changes the information contained in a specified Order.                                                                                                                                                                                                                                                                                                                                         |
| Approve Requests                           | The use of an electronic signature by a Control Point Official to approve a 2237, 1358 or other request form and transmit said request to A&MM/Fiscal.                                                                                                                                                                                                                                                          |
| Authorization                              | A charge to a 1358 that has been obligated. Each authorization represents a deduction from the balance of a 1358 to cover an expense. Authorizations are useful when you have expenses from more than one vendor for a single 1358.                                                                                                                                                                             |
| Authorization Balance                      | The amount of remaining money that can be authorized against the 1358 form. The service balance minus total authorizations.                                                                                                                                                                                                                                                                                     |
| Batch Number                               | A unique number assigned by the computer to identify a batch (group) of Code Sheets. Code Sheets may be transmitted by Batch Number or Transmission Number.                                                                                                                                                                                                                                                     |
| Breakout Code                              | A set of A&MM codes which identifies a vendor by the type of ownership (e.g., Minority-owned, Vietnam Veteran Owned, Small Business Total Set Aside, etc.).                                                                                                                                                                                                                                                     |
| Budget Analyst                             | Fiscal employee responsible for distributing and transferring funds.                                                                                                                                                                                                                                                                                                                                            |
| Budget Object Code                         | Fiscal accounting element that tells what kind of item or service is being procured~~.~~ Budget object codes are listed in the VA Handbook 4671.2                                                                                                                                                                                                                                                               |
| Budget Sort Category                       | Used by Fiscal Service to identify the allocation of funds throughout their facility.                                                                                                                                                                                                                                                                                                                           |
| Ceiling Transactions                       | Funding distributed from Fiscal Service to IFCAP Control Points for spending. The Budget Analyst initiates these transactions using the Funds Distribution options.                                                                                                                                                                                                                                             |
| Classification of Request                  | An identifier a Control Point can assign to track requests that fall into a category, e.g., Memberships, Replacement Parts, and Food Group III.                                                                                                                                                                                                                                                                 |
| Common Numbering Series                    | This is a pre-set series of Procurement and Accounting Transaction (PAT) numbers used by Purchasing and Contracting, Personal Property Management, Accounting Technicians and Imprest Funds Clerks to generate new Purchase Orders/Requisitions/Accounting Transactions on IFCAP. The Application Coordinator establishes the Common Numbering Series used by each facility.                                    |
| Control Point                              | Financial element, existing ONLY in IFCAP, that corresponds to the ACC~~S~~ number in FMS. Also, the division of monies into a specified service, activity or purpose from an appropriation.                                                                                                                                                                                                                    |
| Control Point Clerk                        | The user within the service who is designated to input requests and maintain the Control Point records for a Service.                                                                                                                                                                                                                                                                                           |
| Control Point Official                     | The individual authorized to expend government funds for ordering supplies and services for their Control Point(s). This person has all of the options the Control Point Clerk has plus the ability to approve requests by using their electronic signature code.                                                                                                                                               |
| Control Point Official's Balance           | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated and remaining to be spent for a specified fiscal quarter.                                                                                                                                                                                   |
| Control Point Requestor                    | The lowest level Control Point user, who can only enter temporary requests (2237s, 1358s) to a Control Point. This user can only view or edit their own requests. A Control Point Clerk or Official must make these requests permanent before they can be approved and transmitted to A&MM/Fiscal.                                                                                                              |
| Cost Center                                | “Subsection” of a Fund Control Point. Cost centers allow fiscal staff to create total expense reports for a section or service and allow requestors to assign requests to that section or service. Cost centers are listed in the VA Handbook 4671.1.                                                                                                                                                           |
| Date Committed                             | The date that you want IFCAP to commit funds to the purchase.                                                                                                                                                                                                                                                                                                                                                   |
| Default                                    | A suggested response that is provided by the system.                                                                                                                                                                                                                                                                                                                                                            |
| Deficiency                                 | When a budget has obligated and expended more than it was funded (see MP-4, Part V, Section C).                                                                                                                                                                                                                                                                                                                 |
| Delinquent Delivery Listing                | A listing of all the Purchase Orders that have not had all the items received by the Warehouse on IFCAP. It is used to contact the vendor for updated delivery information.                                                                                                                                                                                                                                     |
| Direct Delivery Patient                    | A patient who has been designated to have goods delivered directly to him/her from the vendor.                                                                                                                                                                                                                                                                                                                  |
| Discount Item                              | This is a trade discount on a Purchase Order. The discount can apply to a line item or a quantity. This discount can be a percentage or a set dollar value.                                                                                                                                                                                                                                                     |
| EDI Vendor                                 | A vendor with whom the VA has negotiated an arrangement to accept and fill orders electronically.                                                                                                                                                                                                                                                                                                               |
| Electronic Data Interchange (EDI)          | Electronic Data Interchange is a method of electronically exchanging business documents according to established rules and formats.                                                                                                                                                                                                                                                                             |
| Electronic Signature                       | The electronic signature code replaces the written signature on all IFCAP documents used within your facility. Documents going off station will require a written signature as well.                                                                                                                                                                                                                            |
| Expenditure Request                        | A Control Point document that authorizes the expenditure of funds for supplies and/or services (e.g., 2237, 1358, etc.).                                                                                                                                                                                                                                                                                        |
| FCP                                        | Fund Control Point (see Control Point).                                                                                                                                                                                                                                                                                                                                                                         |
| Federal Tax ID                             | A unique number that identifies your station to the Internal Revenue Service.                                                                                                                                                                                                                                                                                                                                   |
| Fiscal Balance                             | The amount of money on a 1358 and any adjustments to that 1358 that have been obligated by Fiscal Service. This amount is reduced by any liquidations submitted against the obligation.                                                                                                                                                                                                                         |
| Fiscal Quarter                             | The fiscal year is broken into four three-month quarters. The first fiscal quarter begins on October 1.                                                                                                                                                                                                                                                                                                         |
| Fiscal Year                                | Twelve-month period from October 1 to September 30.                                                                                                                                                                                                                                                                                                                                                             |
| FMS                                        | Financial Management System, the primary accounting system for administrative appropriations. FMS has a comprehensive database that provides flexible on-line and/or batch processing, ad-hoc reporting, interactive query capability and extensive security. FMS is concerned with budget execution, general ledger, funds control, accounts receivable, accounts payable and cost accounting.                 |
| FOB                                        | Freight on Board. An FOB of "Destination" means that the vendor has included shipping costs in the invoice, and no shipping charges are due when the shipper arrives at the warehouse with the item. An FOB of "Origin" means that shipping charges are due to the shipper and must be paid when the shipper arrives at the warehouse with the item.                                                            |
| FPDS                                       | Federal Procurement Data System.                                                                                                                                                                                                                                                                                                                                                                                |
| FTEE                                       | Full Time Employee Equivalent. An FTEE of 1 stands for 1 fiscal year of full-time employment. This number is used to measure workforces. A part-time employee that worked half days for a year would be assigned as an FTEE of 0.5, as would a full-time employee that worked for half of a year.                                                                                                               |
| Fund Control Point                         | See Control Point                                                                                                                                                                                                                                                                                                                                                                                               |
| Funds Control                              | A group of Control Point options that allow the Control Point Clerk and/or Official to maintain and reconcile their funds.                                                                                                                                                                                                                                                                                      |
| Funds Distribution                         | A group of Fiscal options that allows the Budget Analyst to distribute funds to Control Points and track Budget Distribution Reports information.                                                                                                                                                                                                                                                               |
| GBL                                        | Government Bill of Lading. A document that authorizes the payment of shipping charges in excess of \$250.00.                                                                                                                                                                                                                                                                                                    |
| GL                                         | General Ledger.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Imprest Funds                              | Monies used for cash or 3rd party draft purchases at a VA facility.                                                                                                                                                                                                                                                                                                                                             |
| Integrated Supply Management System (ISMS) | ISMS is the system which replaced LOG I for Expendable Inventory. IFCAP sends PHA and PHM transactions to this system.                                                                                                                                                                                                                                                                                          |
| ISMS                                       | Integrated Supply Management System.                                                                                                                                                                                                                                                                                                                                                                            |
| Item File                                  | A listing of items specified by A&MMS as being purchased repetitively. This file maintains a full description of the item, related stock numbers, vendors, contract numbers and a procurement history.                                                                                                                                                                                                          |
| Item History                               | Procurement information stored in the Item File. A history is kept by Fund Control Point and is available to the Control Point at time of request.                                                                                                                                                                                                                                                              |
| Item Master Number                         | A computer-generated number used to identify an item in the Item File.                                                                                                                                                                                                                                                                                                                                          |
| Justification                              | A written explanation of why the Control Point requires the items requested. Adequate justification must be given if the goods are being requested from other than a mandatory source.                                                                                                                                                                                                                          |
| Liquidation                                | The amount of money to be paid to a vendor. The payment will be posted on the 1358 document and will reduce the Fiscal Balance. They are processed through payment/invoice tracking.                                                                                                                                                                                                                            |
| LOG I                                      | LOG I is the name of the Logistics A&MM computer located at the Austin Data Processing Center. This system continues to support the Consolidated Memorandum of Receipt.                                                                                                                                                                                                                                         |
| Mandatory Source                           | A Federal Agency that sells supplies and services to the VA. VA Supply Depot, Defense Logistics Agency (DLA), General Services Administration (GSA), etc.                                                                                                                                                                                                                                                       |
| MSC Confirmation Message                   | A MailMan message generated by the Austin Message Switching Center that assigns an FMS number to an IFCAP transmission of documents.                                                                                                                                                                                                                                                                            |
| Obligation                                 | The commitment of funds. The process Fiscal uses to set aside monies to cover the cost of an Order.                                                                                                                                                                                                                                                                                                             |
| Obligation (Actual) Amount                 | The actual dollar figure that has been obligated by Fiscal Service for a Purchase Order. The Control Point's records are updated with actual cost automatically when Fiscal obligates the document in IFCAP.                                                                                                                                                                                                    |
| Obligation Data                            | A Control Point option that allows the Control Point Clerk to enter data not recorded by IFCAP.                                                                                                                                                                                                                                                                                                                 |
| Organization Code                          | Accounting element that’s functionally comparable to Cost Center but used to organize purchases by the budget that funded them, not for the purpose of spending the funds.                                                                                                                                                                                                                                      |
| Outstanding 2237                           | A&MM report that lists all the IFCAP generated 2237s pending action in A&MM.                                                                                                                                                                                                                                                                                                                                    |
| PAID                                       | Personnel Accounting Integrated Data.                                                                                                                                                                                                                                                                                                                                                                           |
| Partial                                    | A Receiving Report (VA document that shows receipt of goods) for only some of the items ordered on a Purchase Order.                                                                                                                                                                                                                                                                                            |
| Partial Date                               | The date that a warehouse clerk created a receiving report for a shipment.                                                                                                                                                                                                                                                                                                                                      |
| PAT Number                                 | Pending Accounting Transaction number - the primary FMS reference number.                                                                                                                                                                                                                                                                                                                                       |
| Personal Property Management               | A section of A&MM Service who’s responsible for screening all requests for those items available from a Mandatory Source, VA Excess or Bulk sale. They also process all requisitions for goods from Federal Agencies and equipment requests. In addition, they maintain the inventory of Warehouse stocked items and all equipment (CMRs) at the facilities they support.                                       |
| PPM                                        | Personal Property Management.                                                                                                                                                                                                                                                                                                                                                                                   |
| Program Code                               | Accounting element that identifies the VA initiative or program that the purchase will support.                                                                                                                                                                                                                                                                                                                 |
| Prompt Payment Terms                       | The discount given to the VA for paying the vendor within a set number of days (e.g., 2% 20 days means the VA will save 2% of the total cost of the order if the vendor is paid within 20 days of receipt of goods).                                                                                                                                                                                            |
| Purchase History Add (PHA)                 | Procurement History Add transaction. This updates the Procurement History file in Austin when orders are obligated in IFCAP. This same transaction is also used to send a PO for EDI processing.                                                                                                                                                                                                                |
| Purchase History Mod (PHM)                     | Procurement History Modification. This updates the Procurement History file in Austin when orders are amended                                                                                                                                                                                                                                                                                                   |
| Purchase Order                             | A government document authorizing the purchase of goods or services at the terms indicated.                                                                                                                                                                                                                                                                                                                     |
| Purchase Order Acknowledgment              | Information returned by the vendor describing the status of items ordered (e.g., 10 CRTs shipped, 5 CRTs backordered).                                                                                                                                                                                                                                                                                          |
| Purchase Order Status                      | The status of completion of a purchase order (e.g., Pending Contracting Officer's Signature, Pending Fiscal Action, Partial Order Received, etc.).                                                                                                                                                                                                                                                              |
| Purchasing Agents                          | A&MM employees are legally empowered to create purchase orders to obtain goods and services from commercial vendors.                                                                                                                                                                                                                                                                                            |
| Quarterly Report                           | A Control Point listing of all transactions (Ceilings, Obligations, and Adjustments) made to a Control Point's Funds.                                                                                                                                                                                                                                                                                           |
| Quotation for Bid                          | Standard Form 18. Used by Purchasing Agents to obtain written/electronic bids from vendors.                                                                                                                                                                                                                                                                                                                     |
| Receiving Report                           | Report that Warehouse Clerk creates to record that the warehouse has received an item. The VA document used to indicate the quantity and dollar value of the goods being received.                                                                                                                                                                                                                              |
| Repetitive Item List                       | A method the Control Point uses to order items in the Item File. The Control Point enters the Item Master Number, the quantity and vendor and IFCAP can sort and generate requests from the list.                                                                                                                                                                                                               |
| Requestor                                  | See “Control Point Requestor.”                                                                                                                                                                                                                                                                                                                                                                                  |
| Requisition                                | The order form used to approve buying from a government vendor.                                                                                                                                                                                                                                                                                                                                                 |
| Running Balance                            | A running record of all the transactions generated and approved for a Control Point. Provides information that shows the total amount of funds committed, obligated, and remaining to be spent for a specified fiscal quarter.                                                                                                                                                                                  |
| Section Request                            | A temporary request for goods and/or services entered by a Control Point Requestor. These requests may or may not be made permanent by the Control Point Clerk/Official.                                                                                                                                                                                                                                        |
| Service Balance                            | The amount of money on the on the original 1358 and any adjustments to that 1358 when created by that service in their Fund Control Point. This amount is reduced by any authorization created by the service.                                                                                                                                                                                                  |
| SF-18                                      | Request for Quotation.                                                                                                                                                                                                                                                                                                                                                                                          |
| SF-30                                      | Amendment of Solicitation/Modification of Contract.                                                                                                                                                                                                                                                                                                                                                             |
| Short Description                          | A phrase which describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item, and the size of item (e.g., GLOVE-SURGICAL MEDIUM).                                                                                                                                                                                                       |
| Site Parameters                            | Information (such as Station Number, Cashier's address, printer location, etc.) that is unique to your station. All of IFCAP uses a single Site Parameter file.                                                                                                                                                                                                                                                 |
| Sort Group                                 | An identifier a Control Point can assign to a project or group of like requests. It is used to generate a report that will tell the cost of requests.                                                                                                                                                                                                                                                           |
| Sort Order                                 | The order in which the budget categories will appear on the budget distribution reports.                                                                                                                                                                                                                                                                                                                        |
| Special Remarks                            | A field on the Control Point Request that allows the CP Clerk to enter information of use to the Purchasing Agent or vendor. This field can be printed on the Purchase Order.                                                                                                                                                                                                                                   |
| Stacked Documents                          | The POs, RRs & 1358s which are sent electronically to Fiscal and stored in a file rather than being printed immediately.                                                                                                                                                                                                                                                                                        |
| Status of Funds                            | Fiscal's on-line status report of the monies available to a Control Point. FMS updates this information automatically.                                                                                                                                                                                                                                                                                          |
| Sub-control Point                          | A specific budget within a Control Point, defined by a Control Point user.                                                                                                                                                                                                                                                                                                                                      |
| Sub-cost Center                            | A subcategory of Cost Center. In IFCAP 5.0, the last two digits of the cost center, if anything other than "00" will be the 'sub-cost center' that is sent to FMS. IFCAP will not use a 'sub-cost center' field but will send FMS the last two digits of the cost center as the FMS 'sub-cost center' field, unless the last two digits of the cost center are '00'.                                            |
| Tasked Job                                 | A job, usually a printout, that has been scheduled to run at a predetermined time. Tasked jobs are set up to run without having a person watching over them.                                                                                                                                                                                                                                                    |
| TDA                                        | See "Transfer of Disbursing Authority."                                                                                                                                                                                                                                                                                                                                                                         |
| Total Authorizations                       | The total amount of the authorizations created for the 1358 obligation.                                                                                                                                                                                                                                                                                                                                         |
| Total Liquidations                         | The total amount of the liquidation against the 1358 obligation.                                                                                                                                                                                                                                                                                                                                                |
| Transaction Number                         | The number of the transaction that funds a Control Point (See Budget Analyst User's Guide). It consists of the Station Number - Fiscal Year - Quarter - Control Point - Sequence Number.                                                                                                                                                                                                                        |
| Transmission Number                        | A sequential number given to a data string when it is transmitted to the AAC; used for tracking message traffic.                                                                                                                                                                                                                                                                                                |
| Type Code                                  | A set of A&MM codes that provides information concerning the vendor’s size and type of competition sought on a purchase order.                                                                                                                                                                                                                                                                                  |
| Vendor file                                | An IFCAP file of vendors solicited by the facility. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. File 440 contains information about the vendors requested by your station. The debtor's address may be drawn from this file but is maintained separately. If the desired vendor is not in the file, contact A&MM Service to have it added. |
| Vendor ID Number                           | The ID number that is assigned to a vendor by FMS.                                                                                                                                                                                                                                                                                                                                                              |
| VRQ                                        | FMS Vendor Request document. When users send vendor information to FMS, FMS sends a VRQ document to IFCAP with the vendor information, ensuring that the information in the IFCAP vendor file matches the information in the FMS vendor table.                                                                                                                                                                  |

# # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2237, 1, 5, 27

Adjustment vouchers, 26

Amendment types, 22

Budget Object Code, 7, 24

Control Point, 10, 15

Delivery Orders, 1, 2, 3, 5, 6, 10, 13, 15, 17, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30

Fund Control Point, 10, 15

Justification, 24

PAID, 1

Partial Date, 26

Purchase Card Orders, 1, 3, 5, 28, 29

Purchase Order, 5

Receipt of item, 3

Receiving Report, 13, 21, 25, 26